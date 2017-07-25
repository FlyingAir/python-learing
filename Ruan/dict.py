d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
def method_name():
    return d.items
for (key, value) in method_name()():
    print("%s: %s" % (key, value))




if(d['Adam']==95):
	print(d['Adam'],'Adam')