import json
import logging
import re

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def swiss_solve(code, case):
	# this is beeg monkaS
	count = 0
	case['this_value_should_indicate_failure'] = False

	if_index = [code[i].startswith('if ') for i in range(len(code))]
	endif_index = [code[i] == 'endif' for i in range(len(code))]
	fail_index = [code[i] == 'fail' for i in range(len(code))]
	for i in range(len(code)):
		if if_index[i]:
			code[i] = code[i][3:]
		elif endif_index[i] or fail_index[i]:
			code[i] = ''

	to_replace = list(reversed(list(sorted(list(case.keys()), key = len))))
	for i in range(len(code)):
		for j, key in enumerate(to_replace):
			code[i] = code[i].replace(key, "{}['{}']".format(4 * chr(1), key))
	for i in range(len(code)):
		code[i] = code[i].replace(4 * chr(1), 'case')

	for i in range(len(code)):
		if if_index[i]:
			code[i] = 'if ' + code[i]
		elif endif_index[i]:
			code[i] = 'endif'
		elif fail_index[i]:
			code[i] = 'fail'

	for i in range(len(code)):
		code[i] = code[i].replace('/', '//')
		x = code[i].startswith('if ')
		if code[i] == 'endif':
			code[i] = ''
			count -= 1
			continue
		if code[i] == 'fail':
			code[i] = 'case["this_value_should_indicate_failure"] = True'
		if x == False and not fail_index[i]:
			code[i] = "if case['this_value_should_indicate_failure'] == False: " + code[i]
		code[i] = '\t' * count + code[i]
		count += x
		if x:
			code[i] += ':'
	
	return '\n'.join(code)
	exec('\n'.join(code))
	return {'is_solvable': not case["this_value_should_indicate_failure"], 'variables': {k: v for k, v in case.items() if k != 'this_value_should_indicate_failure'}}


@app.route('/swissbyte', methods=['POST'])
def swissbyte():
	data = request.get_json()
	#logging.info("data sent for evaluation {}".format(data))
	code, cases = data['code'], data['cases']
	processed_code = swiss_solve(code, cases[0])
	outcomes = list()
	for case in cases:
		case['this_value_should_indicate_failure'] = False
		exec(processed_code)
		outcomes.append({'is_solvable': not case["this_value_should_indicate_failure"], 'variables': {k: v for k, v in case.items() if k != 'this_value_should_indicate_failure'}})
	result = {"outcomes": outcomes}
	#logging.info("My result :{}".format(result))
	return json.dumps(result)
