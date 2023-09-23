import json
import logging

from flask import request
from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 6

from routes import app

logger = logging.getLogger(__name__)

def dist(p, q):
    x1, y1 = p
    x2, y2 = q
    return Decimal((x1 - x2)**2 + (y1 - y2)**2).sqrt()

def teleportation_solve(k, portals, destinations):
    closest_portal_dist = list()
    for q in destinations:
        closest_portal_dist.append(min(dist(p, q) for p in portals))
    
    next_distances = [dist((0, 0), destinations[0])] + [dist(destinations[i], destinations[i + 1]) for i in range(len(destinations) - 1)]
    total = sum(next_distances)
    saved_distances = list()
    for i in range(len(destinations)):
        current_distance = next_distances[i]
        teleport_distance = closest_portal_dist[i]
        if teleport_distance < current_distance:
            saved_distances.append(current_distance - teleport_distance)
    saved_distances.sort()
    #logging.info(saved_distances)
    total -= sum(saved_distances[-k:])
    return str(round(total, 2))


@app.route('/teleportation', methods=['POST'])
def teleportation():
    data = request.get_json()
    k, p, q = data['k'], data['p'], data['q']
    result = teleportation_solve(k, p, q)
    return json.dumps(result)
