# Use this to ping check a set of IPs.getstatusoutput('ping -c1' + str(i))

import subprocess as sp

def PingCheck():
    ipRange = input(str("Welcome to PingCheck, please enter the IP range you want to check.\n\nPlease use the following format, x.x.x.y-z "))
    firstOctet = str(ipRange).split('.')[0]
    secondOctet = str(ipRange).split('.')[1]
    thirdOctet = str(ipRange).split('.')[2]
    lastOctetRange = str(ipRange).split('.')[3]
    beginningIp = int(str(lastOctetRange).split('-')[0])
    finalIp = int(str(lastOctetRange).split('-')[1])
    dot = "."
    subnetOctets = [firstOctet, secondOctet, thirdOctet]
    subnet = dot.join(subnetOctets) + "."
    pingSet = []
    for i in range(beginningIp, finalIp + 1, 1):
        pingSet.append(subnet+str(i))
    print (pingSet)
    for i in pingSet:
        status,result = sp.getstatusoutput("ping -c1 -W2 " + str(i))
        if status == 0:
            print(i + " is UP !")
        else:
            print(i + " is DOWN !")
if __name__ == '__main__':
    PingCheck()
