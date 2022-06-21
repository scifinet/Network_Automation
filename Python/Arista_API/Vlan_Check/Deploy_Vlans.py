from jsonrpclib import Server
import ssl
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

Switches = open('git/Network_Automation/Python/Arista_API/Vlan_Check/Arista_Switches.txt', 'r').readlines()
Switch_List = []
Invalid_VlanID_List = []
Valid_VlanID_List = []
Unreachable_Devices = []
Deployed_Vlans = {}
Has_Vlans = {}
Missing_Vlans = {}
Vlan_Names = {}
Added_Vlans = []

### ADD DEVICES FROM 'Swithes' TO A LIST AND ADD EACH DEVICE AS A KEY TO THE Has_Vlans OR Missing_Vlans DICT ###
for i in Switches:
    Switch_List.append("{}".format(i.strip()))
    Has_Vlans["{}".format(i.strip())] = []
    Missing_Vlans["{}".format(i.strip())] = []

### TEST DEVICES FROM 'Switches' FOR REACHABILITY AND REMOVE ANY THAT ARE UNREACHABLE FROM SWITCH_LIST AND Has_Vlans AND Missing_Vlans DICT ###
for device in Switch_List:
    try:
        requests.get(f'https://{device}', verify=False, timeout=.3)
    except:
        Switch_List.remove(device)
        Unreachable_Devices.append(device)
        Has_Vlans.pop(device)
        Missing_Vlans.pop(device)

### GATHER LOGIN CREDENTIALS ###
username = input("Enter username: ")
print("Enter password:")
password = getpass()
print("\n\n### LOGGING INTO DEVICES... ###\n\n")

### GATHER ALL VLANS(values) DEPLOYED TO EACH DEVICE(key) IN SWITCH_LIST AND STORE IN Deployed_Vlans DICT ###
for device in Switch_List:
    VlanID_List = []
    switch = Server(f'https://{username}:{password}@{device}/command-api')
    vlan_check = switch.runCmds(1, ['show vlan'])
    for vlan_id in vlan_check[0]['vlans'].keys():
        VlanID_List.append(vlan_id)
    Deployed_Vlans[device] = VlanID_List

### ASK USER FOR WHICH VLANS TO LOOK FOR AND STORE ENTRY IN test_vlans LIST ###
vlan_query = input('\nEnter VLAN #\'s to check for. Check for multiple VLANs by separating them with a comma.\nDesired vlans: ')
test_vlans = (vlan_query.replace(' ','')).split(',')

### LOOP OVER test_vlans LIST UNTIL EMPTY TO TEST IF ITEM IS A VALID VLAN. REMOVE ITEM FROM test_vlans AFTER TEST AND STORE RESULT IN VALID OR INVALID LIST ###
while len(test_vlans) >> 0:
    for i in test_vlans:
        try:
            if int(i) not in range(4095):
                test_vlans.remove(i)
                Invalid_VlanID_List.append(i)
            else:
                test_vlans.remove(i)
                Valid_VlanID_List.append(i)
                break
        except ValueError:
            test_vlans.remove(i)
            Invalid_VlanID_List.append(i)
            continue

### TEST IF USER SPECIFIED VALID VLANS EXIST IN DEVICE. IF SO, ADD VLAN TO Has_Vlans DICT(key=device, values=vlans). IF NOT, ADD VLAN TO Missing_Vlans ###
### ASK USER TO NAME SPECIFIED VALID VLANS ###
for i in Valid_VlanID_List:
    for switch, vlan in Deployed_Vlans.items():
        if i in vlan:
            Has_Vlans[switch].append(i)
        else:
            Missing_Vlans[switch].append(i)
    Vlan_Names[i] = input('Please give name for vlan ' + i + ': ')

### USER READABLE OUTPUT TO INFORM ABOUT ABOVE LOGIC ###
print("\n\n### CHECKING SWITCHES FOR DESIRED VLANS ###\n\n",Unreachable_Devices,"cannot be reached--REMOVING from scope\n")
print("\n\n### INVALID VLANS DETECTED ###\n")
print(Invalid_VlanID_List, "are not valid vlans--REMOVING from scope\n")
print("\n### LOOKING FOR VLANS ###\n")
print("(Vlan ID: Vlan Name)")
print("--------------------")
print(Vlan_Names, "\n")
print("\n### VLAN INFORMATION FOUND ###\n")

### INFORM USER OF EACH DEVICE AND IF THEIR SPECIFIED VLAN IS DEPLOYED OR NOT. ASK IF USER WANTS TO DEPLOY ANY MISSING VLANS ###
for switch, vlans in Has_Vlans.items():
    if Valid_VlanID_List == vlans:
        print(switch, "has all desired vlans deployed.")
    else:
        #print(switch, "has the following vlans deployed:\n", Has_Vlans[switch])
        print(switch, "does not have the following vlans deployed:", Missing_Vlans[switch], "\n")
deploy = input("Proceed with deploying missing vlans? (yes/no): ")

### DEPLOYS VLANS MISSING FROM DEVICE LIST. INFORMS USER THE PROGRAM IS FINISHED. ###
if deploy.lower() == 'yes':
    try:
        for device in Missing_Vlans.keys():
            switch = Server(f'https://{username}:{password}@{device}/command-api')
            for vlan in Missing_Vlans[device]:
                switch.runCmds(version=1, cmds=['conf t', 'vlan ' + vlan, 'name ' + Vlan_Names[vlan]], format='json', autoComplete=True)
                Added_Vlans.append(vlan)
            print("DEPLOYED vlans",Added_Vlans, "to", device)
            Added_Vlans.clear()
    except:
        print("Credentials failed.")
else:
    print("No action taken")
