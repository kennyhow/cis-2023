import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def monkey_solve(w, v, f):
    dp = [[0 for i in range(v + 1)] for j in range(w + 1)] # dp[weight][volume] => max value possible
    for weight, volume, value in f:
        for i in reversed(range(w + 1 - weight)):
            for j in reversed(range(v + 1 - volume)):
                dp[i + weight][j + volume] = max(dp[i + weight][j + volume], dp[i][j] + value)
    return max(max(row) for row in dp)

@app.route('/greedymonkey', methods=['POST'])
def greedyMonkey():
    data = json.loads(request.data)
    logging.info("data sent for evaluation {}".format(data))
    w = data.get('w')
    v = data.get('v')
    f = data.get('f')
    result = monkey_solve(w, v, f)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
