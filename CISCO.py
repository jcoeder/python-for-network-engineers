from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_conf.cfg")

maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in maps:
    print(i.children)

print('##########################################')
print('##########################################')
print('##########################################')

group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"group2")

print(group2)

for i in group2:
    print(i)
