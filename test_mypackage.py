# Import pytest instead of nose.tools

import pytest
import ex47
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "この部屋には金があります。北にドアがあります。")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "中央のテストルーム。")
    north = Room("North", "北のテストルーム。")
    south = Room("South", "南のテストルーム。")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "西と下に穴に行けます。")
    west = Room("Trees", "ここには木があり、東に行けます。")
    down = Room("Dungeon", "ここは暗くて、上に行けます。")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

