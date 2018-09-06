from ciscoconfparse import CiscoConfParse
import re

cisco_cfg = CiscoConfParse("cisco_conf.cfg")

maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in maps:
    print(i.children)
print('##########################################')
print('##########################################')
print('##########################################')

group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"group2")

for i in group2:
    print(i)

print('##########################################')
print('##########################################')
print('##########################################')

#Using ciscoconfparse find the crypto maps that are not using AES
#(based-on the transform set name). Print these entries and their
#corresponding transform set name.
not_aes = cisco_cfg.find_objects_wo_child(r'^crypto map', r'set transform-set AES')
#for i in not_aes:
#    print(i)
#print(not_aes)
for list_entry in not_aes:
    for child in list_entry.children:
        if 'transform' in child.text:
            match = re.search(r'set transform-set (.*)$', child.text)
            encryption = match.group(1)
    print ("{}".format(list_entry.text.strip()))
    print ("  set transform-set {}".format(encryption))
print()
