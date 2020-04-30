# How to Recreate the Topology

The steps below show how to recreate the topology created in GNS3, that was used in all the tests.

*Step 1 – The simulated network devices are put in the configuration shown in the figure below, in this dissertation the router c3725, an unmanaged switch and a simulated Ubuntu Linux PC was used. 

*Step 2 – Connect the devices in the configuration shown in the figure above. In the case of this topology, the routers were connected using Serial links. The other connections, Router to Switch and PC to Switch used FastEthernet cabling. The exact interfaces used are shown below in Table 1.
Table 1: Interface Usage Table
Device	Interface to R1	Interface to R2	Interface to R3	Interface to Switch
R1	N/A	Serial S0/1	N/A	Fast Ethernet 0/0
R2	Serial 0/1	N/A	Serial 1/1	Fast Ethernet 0/0
R3	N/A	Seial 1/1	N/A	Fast Ethernet 0/0
* Step 3 – Basic configuration was implemented on each router, shown in Table 2 on the next page. This allowed the routers and PC to connect, over the Secure Shell Protocol version 2.
* Step 4 – The PC was configured to install the necessary resources needed to complete all the tests. This included installing the latest version of Python, which is Python 3.8 and installing the necessary Python libraries used in the test. These being Paramiko, Netmiko and SCP libraries.
* Step 5 – Once all the prior steps have been completed the test can be conducted, any additional configuration on the routers was added per test. The in-depth router configurations and the individual commands used to configure the Ubuntu PC can be found in Appendix IV.
