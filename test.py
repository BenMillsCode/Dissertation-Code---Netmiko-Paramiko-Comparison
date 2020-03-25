import re

output = '''
Building configuration...

Current configuration : 1457 bytes
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R1
!
boot-start-marker
boot-end-marker
!
!
no aaa new-model
memory-size iomem 5
ip cef
!
!
!
!
no ip domain lookup
ip domain name R1.com
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
username admin privilege 15 secret 5 $1$ywB0$NmQtAbHT/ApaQ6fGgd0U.0
archive
 log config
  hidekeys
!
!
!
!
!
!
interface FastEthernet0/0
 ip address 192.168.0.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface Serial1/0
 ip address 192.168.12.1 255.255.255.252
 no fair-queue
 serial restart-delay 0
!
interface Serial1/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial1/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial1/3
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial2/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial2/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial2/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial2/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 log-adjacency-changes
!
!
!
ip http server
no ip http secure-server
!
!
!
!
!
!
!
control-plane
!
!
!
!
!
!
!
!
!
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input ssh
!

!
webvpn cef
!
end
'''

networks = re.findall("\d+\.\d+\.\d+\.\d+\s\d+\.\d+\.\d+\.\d+", output)

for network in networks:
    netmask = network.split()[1]
    nmconv = netmask.split(".")

    wildcard = []
    for num in nmconv:
        wildcard.append(str(255 - int(num)))
    command = "network " + network.replace(netmask, ".".join(wildcard))
    
    print(command)
    #networks.replace(netmask, )
