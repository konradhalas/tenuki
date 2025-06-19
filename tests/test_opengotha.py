import os

from xmldiff import main as xmldiff

from tenuki.opengotha import Player, export_players_to_xml


def test_opengotha_export():
    players = [
        Player(
            last_name="Chó",
            first_name="Chikun",
            country="pl",
            club="Wars",
            rank="9p",
            egd_pin="12001704",
            gor=2937,
            is_present=True,
        )
    ]

    export_data = export_players_to_xml(players)

    test_data = open(
        os.path.join(os.path.dirname(__file__), "data/opengotha/tournament_export.xml"),
        "rb",
    ).read()  # noqa: F821
    assert not xmldiff.diff_texts(test_data, export_data)
