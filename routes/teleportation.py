import json
import logging

from flask import request
from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 9

from routes import app

logger = logging.getLogger(__name__)

SQRT = [Decimal(i).sqrt() for i in range(20005)]

def dist(p, q):
    x1, y1 = p
    x2, y2 = q
    return (x1 - x2)**2 + (y1 - y2)**2

def teleportation_solve(k, portals, destinations):
    destinations = [(0, 0)] + destinations
    next_dist = [dist(destinations[i], destinations[i + 1]) for i in range(len(destinations) - 1)]
    portal_dist = [min(dist(portal, destinations[i]) for portal in portals) for i in range(len(destinations))]

    #logging.info("next_dist: {}".format(next_dist))
    #logging.info("portal_dist: {}".format(portal_dist))

    total = sum(map(lambda i: SQRT[i], next_dist))
    saved_dist = list()
    for i in range(len(next_dist)):
        current_distance = next_dist[i]
        portal_distance = portal_dist[i + 1]
        if current_distance > portal_distance:
            saved_dist.append(SQRT[current_distance] - SQRT[portal_distance])

    saved_dist.sort()
    #logging.info(saved_dist)
    total -= sum(saved_dist[-k:])
    return float(total)


@app.route('/teleportation', methods=['POST'])
def teleportation():
    data = request.get_json()
    k, p, q = data['k'], data['p'], data['q']
    result = teleportation_solve(k, p, q)
    return json.dumps(result)
