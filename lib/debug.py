#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    v1 = Visitor("Payne")
    v2 = Visitor("Pymon")
    p1 = NationalPark("Yose")
    p2 = NationalPark("Jose")

    t1 = Trip(v1, p1, "Oct 1", "Oct 2")
    t2 = Trip(v1, p1, "Oct 2", "Oct 3")
    t3 = Trip(v2, p2, "Nov 2", "Dec 3")

    # v1.trips()
    v1.national_parks()

    ipdb.set_trace()
