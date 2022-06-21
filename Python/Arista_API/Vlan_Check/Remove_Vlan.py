from jsonrpclib import Server
import ssl
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

Switches = open('git/Network_Automation/Python/Arista_API/Vlan_Check/Hillsboro_BP_Switches.txt', 'r').readlines()
Switch_List = []
Invalid_VlanID_List = []
Valid_VlanID_List = []
Unreachable_Devices = []
Deployed_Vlans = {}
Has_Vlans = {}
Missing_Vlans = {}
Vlan_Names = {}
Removed_Vlans = []

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

username = input("Enter username: ")
print("Enter password:")
password = getpass()
print("\n\n### LOGGING INTO DEVICES... ###\n\n")

for device in Switch_List:
    VlanID_List = []
    switch = Server(f'https://{username}:{password}@{device}/command-api')
    vlan_check = switch.runCmds(1, ['show vlan'])
    for vlan_id in vlan_check[0]['vlans'].keys():
        VlanID_List.append(vlan_id)
    Deployed_Vlans[device] = VlanID_List

vlan_query = input('\nEnter VLAN #\'s to check for. Check for multiple VLANs by separating them with a comma.\nDesired vlans: ')
test_vlans = (vlan_query.replace(' ','')).split(',')

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

for i in Valid_VlanID_List:
    for switch, vlan in Deployed_Vlans.items():
        if i in vlan:
            Has_Vlans[switch].append(i)
        else:
            Missing_Vlans[switch].append(i)
    # Vlan_Names[i] = input('Please give name for vlan ' + i + ': ')

print("\n\n### CHECKING SWITCHES FOR DESIRED VLANS ###\n\n",Unreachable_Devices,"cannot be reached--REMOVING from scope\n")
print("\n\n### INVALID VLANS DETECTED ###\n")
print(Invalid_VlanID_List, "are not valid vlans--REMOVING from scope\n")
print("\n### LOOKING FOR VLANS ###\n")
print("(Vlan IDs)")
print("---------")
print(Valid_VlanID_List, "\n")
print("\n### VLAN INFORMATION FOUND ###\n")
for switch, vlans in Missing_Vlans.items():
    if Valid_VlanID_List == vlans:
        print(switch, "does not have the specified vlans deployed:", Missing_Vlans[switch], "\n")
    else:
        print(switch, "has all specified vlans deployed. (",Valid_VlanID_List,")")
        # print(switch, "does not have the following vlans deployed:", Missing_Vlans[switch], "\n")
remove = input("Proceed with removing specified vlans from switches with them deployed? (yes/no): ")

if remove.lower() == 'yes':
    try:
        for device in Has_Vlans.keys():
            switch = Server(f'https://{username}:{password}@{device}/command-api')
            for vlan in Has_Vlans[device]:
                switch.runCmds(version=1, cmds=['conf t', 'no vlan ' + vlan], format='json', autoComplete=True)
                Removed_Vlans.append(vlan)
            print("REMOVED vlans", Removed_Vlans, "from", device)
            Removed_Vlans.clear()
    except:
        print("Credentials failed.")
else:
    print("No action taken")
