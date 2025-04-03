import bencode_rs
from click.testing import CliRunner

from sciop_cli.cli import torrent

from ..conftest import DATA_DIR


def test_create_torrent(tmp_path):
    trackers = ["udp://example.com:6969", "http://example.com/announce.php"]
    webseeds = ["https://example.com/files"]
    output = tmp_path / "basic.torrent"
    args = [
        "-p",
        str(DATA_DIR / "basic"),
        "-o",
        str(output),
        "--creator",
        "sciop-tests",
        "--comment",
        "test",
        "-s",
        16 * (2**10),
    ]
    for tracker in trackers:
        args.extend(["--tracker", tracker])
    for webseed in webseeds:
        args.extend(["--webseed", webseed])

    runner = CliRunner()
    result = runner.invoke(torrent.create, args)
    assert result.exit_code == 0
    expected = bencode_rs.bdecode((DATA_DIR / "basic.torrent").read_bytes())
    created = bencode_rs.bdecode(output.read_bytes())

    # remove creation_date, which can't be set from python libtorrent
    del expected[b"creation date"]
    del created[b"creation date"]

    assert bencode_rs.bencode(expected) == bencode_rs.bencode(created)
