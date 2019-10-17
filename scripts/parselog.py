#!/usr/bin/python3

import json
import yaml

dumpbox = {"errorips":[]}

## open files/log.example
with open("/home/student/ans/files/log.example") as lef:
    for line in lef:
        if "ERROR" in line:
            loggedip = line.split()[1]
            dumpbox["errorips"].append(loggedip)

print(json.dumps(dumpbox))
#with open("/home/student/ans/files/parsed.ips","w") as iif:
#    iif.write(yaml.dump(dumpbox))



    

## parse files/log.example for ERROR and collect second item in the line (IP)
## store in dictionary {'erroips': [list of ips]}

## dump (pring) collected IPs out as json
