import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def railway_solve(query):
    query = list(map(int, query.split(', ')))
    k, n, seq = query[0], query[1], query[2:]
    
    dp = [0 for i in range(k + 1)] # dp[i] => number of ways to construct segment of length k
    dp[0] = 1
    for val in seq:
        for i in range(len(dp) - val):
            dp[i + val] += dp[i]
    return dp[-1]

    

@app.route('/', methods=['POST'])
def railway():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = [railway_solve(row) for row in data]
    logging.info("My result :{}".format(result))
    return json.dumps(result)
