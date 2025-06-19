import unicodedata
from dataclasses import dataclass
from typing import Callable
from xml.etree import ElementTree


@dataclass(frozen=True)
class Player:
    first_name: str
    last_name: str
    rank: str
    country: str
    club: str
    is_present: bool
    egd_pin: str | None
    gor: int | None = None


def clean_name(name: str) -> str:
    name = name.strip().replace(" ", "_")
    return unicodedata.normalize("NFKD", name).encode("ASCII", "ignore").decode("ASCII")


def export_players_to_xml(players: list[Player], name_cleaner: Callable[[str], str] = clean_name) -> bytes:
    root_el = ElementTree.Element("Tournament")
    players_el = ElementTree.SubElement(root_el, "Players")
    for player in players:
        player_el = ElementTree.SubElement(players_el, "Player")
        player_el.set("name", name_cleaner(player.last_name))
        player_el.set("firstName", name_cleaner(player.first_name))
        player_el.set("grade", player.rank)
        player_el.set("rank", player.rank)
        player_el.set("country", player.country)
        player_el.set("club", player.club)
        if player.egd_pin:
            player_el.set("egfPin", player.egd_pin)
        if player.gor:
            player_el.set("rating", str(player.gor))
        player_el.set("registeringStatus", "FIN" if player.is_present else "PRE")
    return ElementTree.tostring(root_el, encoding="utf8")
