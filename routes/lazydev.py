from typing import Dict, List

import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:

	classes = {k: v for d in classes for k, v in d.items()}  # merge to 1 dict
	answer = {statement: list() for statement in statements}
	for statement in statements:
		s = statement.split('.')
		if len(s) == 1:
			answer[statement] = [word for word in classes.keys() if word.startswith(s)]
		else:
			current_word = s[0]
			if current_word not in classes.keys():
				break
			else:
				for i in range(1, len(s)):
					if current_word not in classes:
						break
					if i == len(s) - 1:
						if isinstance(classes[current_word], dict):
							answer[statement] = [
							 word for word in classes[current_word] if word.startswith(s[i])
							]
						elif isinstance(classes[current_word], str):
							pass
						elif isinstance(classes[current_word], list):
							answer[statement] = [
							 word for word in classes[current_word] if word.startswith(s[i])
							]
					else:
						if isinstance(classes[current_word], dict):
							if s[i] in classes[current_word]:
								current_word = classes[current_word][s[i]]
						else:
							break

	for statement in statements:
		if statement not in answer or len(answer[statement]) == 0:
			answer[statement] = [""]
		answer[statement] = sorted(answer[statement])[:5]

	return answer

@app.route('/lazydev', methods=['POST'])
def lazydev():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    classes, statements = data['classes'], data['statements']
    result = getNextProbableWords(classes, statements)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
