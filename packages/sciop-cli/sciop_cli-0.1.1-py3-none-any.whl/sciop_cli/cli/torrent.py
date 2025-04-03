from pathlib import Path
from typing import cast

import click

from sciop_cli.const import DEFAULT_TORRENT_CREATOR
from sciop_cli.data import get_default_trackers
from sciop_cli.torrent import create_torrent
from sciop_cli.types import PieceSize


@click.group()
def torrent() -> None:
    """
    Create and manage torrents
    """


@torrent.command()
def pack() -> None:
    """
    Pack a directory to prepare it for torrent creation

    - Generate a manifest for the directory
    - Archive small files
    - Emit a .packmap.json description of the packing operation
    """
    raise NotImplementedError()


@torrent.command()
@click.option(
    "-p",
    "--path",
    required=True,
    help="Path to a directory or file to create .torrent from",
    type=click.Path(exists=True),
)
@click.option(
    "-t",
    "--tracker",
    required=False,
    default=None,
    multiple=True,
    help="Trackers to add to the torrent. can be used multiple times for multiple trackers. "
    "If not present, use the default trackers from https://sciop.net/docs/uploading/default_trackers.txt",
)
@click.option(
    "--no-default-trackers",
    is_flag=True,
    default=False,
    help="Do not use the default trackers if no trackers are provided",
)
@click.option(
    "-s",
    "--piece-size",
    default=512 * (2**10),
    help="Piece size, in bytes",
    show_default=True,
)
@click.option(
    "--comment",
    default=None,
    required=False,
    help="Optional comment field for torrent",
)
@click.option(
    "--creator",
    default=DEFAULT_TORRENT_CREATOR,
    show_default=True,
    required=False,
    help="Optional creator field for torrent",
)
@click.option(
    "-w",
    "--webseed",
    required=False,
    default=None,
    multiple=True,
    help="Add HTTP webseeds as additional sources for torrent. Can be used multiple times. "
    "See https://www.bittorrent.org/beps/bep_0019.html",
)
@click.option(
    "--similar",
    required=False,
    default=None,
    multiple=True,
    help="Add infohash of a similar torrent. "
    "Similar torrents are torrents who have files in common with this torrent, "
    "clients are able to reuse files from the other torrents if they already have them downloaded.",
)
@click.option("--progress/--no-progress", default=True, help="Enable progress bar (default True)")
@click.option(
    "-o",
    "--output",
    required=False,
    default=None,
    type=click.Path(exists=False),
    help=".torrent file to write to. Otherwise to stdout",
)
def create(
    path: Path,
    tracker: list[str] | None = None,
    no_default_trackers: bool = False,
    piece_size: PieceSize = 512 * (2**10),
    comment: str | None = None,
    creator: str = DEFAULT_TORRENT_CREATOR,
    webseed: list[str] | None = None,
    similar: list[str] | None = None,
    progress: bool = True,
    output: Path | None = None,
) -> None:
    """
    Create a torrent from a file or directory.

    Uses libtorrent to create standard torrent files.
    Will create a hybrid v1/v2 torrent file.

    See https://www.libtorrent.org/reference-Create_Torrents.html
    form details on fields, all input here is passed through to
    libtorrent's creation methods.
    """
    if tracker is None and not no_default_trackers:
        tracker = get_default_trackers()
    result = create_torrent(
        path,
        trackers=tracker,
        piece_size=piece_size,
        comment=comment,
        creator=creator,
        webseeds=webseed,
        similar=similar,
        pbar=progress,
        bencode=True,
    )
    result = cast(bytes, result)
    if output:
        with open(output, "wb") as f:
            f.write(result)
    else:
        click.echo(result)
