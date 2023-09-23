case = {'a': 0, 'b': 2, 'c': 3}
this_value_should_indicate_failure = False
x = 'if this_value_should_indicate_failure == False: case[\'a\'] = case[\'a\'] + 4\nif this_value_should_indicate_failure == False: case[\'b\'] = case[\'b\'] - 4\nprint("case is: ", case)\nif case[\'a\'] == 4:\n\tthis_value_should_indicate_failure = True\nelse:\n\tprint("AHHHH WOWOWO")\n\nif this_value_should_indicate_failure == False: case[\'c\'] = 7'
exec(x)
print(this_value_should_indicate_failure)