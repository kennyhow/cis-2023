import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def digital_solve(query):
    n = query['generations']
    s = query['colony']
    
    # count[i][j] => number of pairs (i, j) in that specific order
    pair_count = [[0 for i in range(10)] for j in range(10)] 
    for i in range(len(s) - 1):
        a, b = int(s[i]), int(s[i + 1])
        pair_count[a][b] += 1
    #logging.info("pair count is {}".format(pair_count))
        
    current_sum = sum(int(x) for x in s)
    #logging.info("current sum is {}".format(current_sum))
    for i in range(n):
        old_current_sum = current_sum
        tmp_pair_count = [[0 for i in range(10)] for j in range(10)]
        for a in range(10):
            for b in range(10):
                new_digit = (old_current_sum + (a - b if a >= b else 10 - (b - a))) % 10
                current_sum = (current_sum + new_digit * pair_count[a][b])
                tmp_pair_count[a][new_digit] += pair_count[a][b]
                tmp_pair_count[new_digit][b] += pair_count[a][b]
        pair_count = [row[::] for row in tmp_pair_count]
    return current_sum
    

@app.route('/digital-colony', methods=['POST'])
def digitalcolony():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = [digital_solve(row) for row in data]
    logging.info("My result :{}".format(result))
    return json.dumps(result)
