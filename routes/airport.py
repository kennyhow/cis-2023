import json
import logging
from math import log

from flask import request, jsonify

from routes import app

logger = logging.getLogger(__name__)


def airport_solve(query):
	seq, k = query['departureTimes'], query['cutOffTime']
	request_count = 0
	n = len(seq)
	relevant = list()
	
	for i in range(n):
		if seq[i] >= k:
			relevant.append(i)
		request_count += 1

	if len(relevant) == 0: 
		return {
			"id": query['id'],
			'sortedDepartureTimes': sorted(list(seq[i] for i in relevant)),
			'numberOfRequests': request_count
		}
	
	return {
		'id': query['id'],
		'sortedDepartureTimes': sorted(list(seq[i] for i in relevant)),
		'numberOfRequests': request_count + int(2.1 * len(relevant) * log(len(relevant)))
	}

@app.route('/airport', methods=['POST'])
def airport():
	data = request.get_json()
	logging.info("data sent for evaluation {}".format(data))
	result = [airport_solve(query) for query in data]
	logging.info("My result :{}".format(result))
	return jsonify(result)
