import netmiko, time, re

#Start in-code timer
start = time.time()

#Router connection details
three_routers = [{
    "host":"192.168.0.1",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.0.2",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.0.3",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }]

#Connection Loop Starts
for router in three_routers:

    #Connect to the router
    connected = netmiko.ConnectHandler(**router)

    #Start OSPF command list
    ospf_set = ["router ospf 1"]

    #Get the connected networks
    output = connected.send_command("show ip route connected")

    #Find the networks from the response using regular expression
    networks = re.findall(r"\d+\.\d+\.\d+\.\d+/\d\d", output)

    #loop through the networks
    for network in networks:

        #Seperate the network address from the subnet mask
        net_ip = network.split("/")[0]

        slash_mask = int(network.split("/")[1])

        #Convert Slash notation subnet mask to binary
        bin_mask = ("0" * slash_mask) + ("1" * (32 - slash_mask))

        #Convert Binary in to IP format Subnet mask
        new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

        new_mask = list(map(str, new_mask))

        #Add the network command to the OSPF command list
        ospf_set.append("network " + net_ip + " " + ".".join(new_mask) + " area 0\n")
    
    #Send the command list to the router
    connected.send_config_set(ospf_set)
    
    #Disconnect from the router
    connected.disconnect()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))
