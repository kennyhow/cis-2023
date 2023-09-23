import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def calendar_solve(query):
	# dp[a][b][c][d][e] = max profit if we work up to `a` days on monday, etc
	dp = [[[[[[[0 for a in range(13)] for b in range(13)] for c in range(13)] for d in range(13)] for e in range(13)] for f in range(13)] for g in range(13)]
	
	# prev[a][b][c][d][e] = prev lessionId ...
	prev = [[[[[[[-1 for a in range(13)] for b in range(13)] for c in range(13)] for d in range(13)] for e in range(13)] for f in range(13)] for g in range(13)]
	
	for lesson in query:
		lessonID, duration, profit, days = query['lessonRequestId'], query['duration'], query['potentialEarnings'], query['availableDays']
		for i, day in enumerate(['monday', 'tuesday', 'wednesday', 'thursday', 'friday']):
			if day in days:
				pass

@app.route('/calendar-scheduling', methods=['POST'])
def calendar_scheduling():
	data = request.get_json()
	logging.info("data sent for evaluation {}".format(data))
	result = calendar_solve(data)
	logging.info("My result :{}".format(result))
	return json.dumps(result)
