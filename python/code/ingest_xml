#first need to install xmltodict:
#pip3 install xmltodict

import xmltodict   

def inxml():

    #get the XML file data
    stream = open('scan.xml','r')

    #parse the XML file into an "OrderedDict"
    xml = xmltodict.parse(stream.read())

    #iterate through items in the XML object
    for e in xml["nmaprun"]["host"]:
        # if e["status"]["@state"] == "down":
        #     print("host is down")
        if e["status"]["@state"] == "up":
            print(e["address"]["@addr"])
        
         

#each host is a dictionary and it has sub dictionaries with it
#You iterate throught it but if you iterate through the 
# first host which is ["host"][0] you will end up iterating through a list of dictionary keys like "status" and not other hosts
#Justa Puma
