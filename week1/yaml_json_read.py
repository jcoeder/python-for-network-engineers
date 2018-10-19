import yaml
import json
from pprint import pprint as pp

with open('some_yaml.yaml', 'r') as yaml_var:
	yaml_list = yaml.load(yaml_var)

pp(yaml_list)


print('')
print('')
print('')



with open('some_json.json') as json_var:
	json_list = json.load(json_var)

pp(json_list)