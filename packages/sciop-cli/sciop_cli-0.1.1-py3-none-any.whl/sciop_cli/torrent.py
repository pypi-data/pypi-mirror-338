from math import floor
from pathlib import Path

import bencode_rs
import libtorrent
from pydantic import TypeAdapter
from tqdm import tqdm

from sciop_cli.const import DEFAULT_TORRENT_CREATOR, EXCLUDE_FILES
from sciop_cli.types import PieceSize


def estimate_piece_size(
    data_size: int, min_pieces: int = 2000, min_piece_size: int = 256 * (2**10)
) -> int:
    """
    Estimate the best piece size given some total size (in bytes) of a torrent

    Largest piece size that still gives us min_pieces.
    Files smaller than the piece size will be packed together into archives,
    so padding files are not much of an overhead concern here.

    pieces = ceil(size / (multiplier * 16KiB))
    pieces * (multiplier * 16KiB) = size
    multiplier = floor(size / (pieces * 16KiB))

    """
    block = 16 * (2**10)
    multiplier = floor(data_size / (min_pieces * block))
    piece_size = round(multiplier * block)
    return max(piece_size, min_piece_size)


def create_torrent(
    path: Path,
    trackers: list[str] | None = None,
    comment: str | None = None,
    creator: str = DEFAULT_TORRENT_CREATOR,
    webseeds: list[str] | None = None,
    similar: list[str] | None = None,
    bencode: bool = True,
    piece_size: PieceSize = 512 * (2**10),
    pbar: bool = False,
) -> dict | bytes:
    path = Path(path)
    fs = libtorrent.file_storage()

    if path.is_dir():
        # get paths and sort
        paths = []
        for _path in path.rglob("*"):
            if _path.name not in EXCLUDE_FILES and _path.is_file():
                # no absolute paths in the torrent plz
                rel_path = _path.relative_to(path)
                # add the parent again as the root
                rel_path = Path(path.name) / rel_path
                paths.append((str(rel_path), _path.stat().st_size))
        paths = sorted(paths, key=lambda x: x[0])
        for p, size in paths:
            fs.add_file(p, size)

    else:
        fs.add_file(path.name, path.stat().st_size)

    piece_size = TypeAdapter(PieceSize).validate_python(piece_size)

    torrent = libtorrent.create_torrent(fs, piece_size=piece_size)

    if trackers:
        for tracker in trackers:
            torrent.add_tracker(tracker)

    if webseeds:
        for webseed in webseeds:
            torrent.add_url_seed(webseed)

    if similar:
        for s in similar:
            torrent.add_similar_torrent(s)

    if comment:
        torrent.set_comment(comment)

    torrent.set_creator(creator)

    _pbar = None
    if pbar:
        _pbar = tqdm(desc="hashing pieces...", total=torrent.num_pieces())

        def _pbar_callback(piece_index: int) -> None:
            _pbar.update()

        libtorrent.set_piece_hashes(torrent, str(path.parent.resolve()), _pbar_callback)
        _pbar.close()
    else:
        libtorrent.set_piece_hashes(torrent, str(path.parent.resolve()))

    ret = torrent.generate()
    if bencode:
        return bencode_rs.bencode(ret)
    else:
        return ret
