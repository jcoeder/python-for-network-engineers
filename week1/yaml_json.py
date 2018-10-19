import yaml
import json

my_list = ['abc', 1, {'ip':'10.10.10.10', 'make':'cisco', 'attribs': [0, 1, 2, 'a']}, 47, 'the meaning of everything']

#print('Print List')
#print(my_list)

#print('Lenth of List')
#print(len(my_list))

#print('Yaml dump of list')
#print(yaml.dump(my_list))

#print('Yaml dump of list default_flow_style True')
#print(yaml.dump(my_list, default_flow_style=True))

#print('Yaml dump of list default_flow_style False')
#print(yaml.dump(my_list, default_flow_style=False))

#print('json dump of list')
#print(json.dumps(my_list))

with open('some_yaml.yaml', 'w') as f:
	f.write(yaml.dump(my_list, default_flow_style=False))

with open('some_json.json', 'w') as f:
	json.dump(my_list, f)

with open('some_json2.json', 'w') as f:
	f.write(json.dumps(my_list))