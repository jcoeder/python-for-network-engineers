from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_conf.cfg")
print (cisco_cfg)

print('##################')

#Find all lines that begin with "interface"
#returns list
intf = cisco_cfg.find_objects(r"^interface")
print (intf)

print('##################')

#Interate over list and print one interface per list
for i in intf:
	print i.text

print('##################')

#pull the 4th interface in the list
fa4 = intf[4]
print(fa4)

print('##################')


#Prints the children under the 4th interface in a list
print(fa4.children)

print('##################')


#Print the children one row at a time
for i in intf[4].children:
	print i.text

print('##################')

#Print the children one row at a time
for i in fa4.children:
	print i.text

#DOES NOT EXIST IN THIS CONFIG
#print('##################')
#
#crypto_pki = cisco_cfg.find_objects(r"^crypto pki certificate")
#print (crypto_pki)
#print (crypto_pki.children[0])

print('##################')

