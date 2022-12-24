#first need to install xmltodict:
#pip install xmltodict

import xmltodict   

#get the XML file data
stream = open('sample.xml','r')

#parse the XML file into an "OrderedDict"
xml = xmltodict.parse(stream.read())

#iterate through items in the XML object
for e in xml["People"]["Person"]:
    print(e)
