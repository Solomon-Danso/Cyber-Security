=> Subnetting are in bits and are in the format 255.255.255.0
255.255.255.0 is a /24 network, popularly used in households and SME
The host refers to how many switches are 0 
For 255.255.255.0

128 64 32 16 8 4 2 1  128 64 32 16 8 4 2 1   128 64 32 16 8 4 2 1 
1   1  1  1  1 1 1 1  1  1  1  1  1 1 1 1    1   1  1  1  1 1 1 1  


128 64 32 16 8 4 2 1 
0   0  0  0  0 0 0 0

8 zeros(0) therefore the host = 2^8 => 256 available devices that can connect to network 

24 ones(1), that is why the network is a /24 network 

IPV4 is 32 bits because 24+8 => 32

128+64+32+16+8+4+2+1 => 255 

As we keep turning the ones to zero the number of devices will increase  

for 10 zeros(0) the available host will be 2^10 => 1024 devices 

255.255.0.0 => 16 bits 
255.0.0.0 => 8 bits 

Example 1
192.168.1.0/24 

Subnet Mask => 255.255.255.0
Host => 2^8 => 256-2 => 254 (because one device 1p will be network and the other will be broadcast )
Network => 192.168.1.0
Broadcast => 192.168.1.255

Example 2
192.168.1.0/28 
Subnet Mask = 255.255.255.240 (128+64+32+16=240)
HOST => 2^4 => 16-2 =14
Network => 192.168.1.0
Broadcast => 192.168.1.15

Example 3
192.168.0.0/22
Subnet = 255.255.252.0
Host =2^10-2= 1022
Network => 192.168.0.0
Broadcast => 192.168.3.255
1022/255 = 4
For every 255 = 1
therefore 4 => 3.255

Example 5 
192.168.1.0/26 
Subnet = 255.255.255.192
          8, 16  24  (25,26)=> 128+64 
Host = 32-26 = 6 => 2^6-2 = 62 (64 host but network and broadcast will take one each so 62)
Network => 192.168.1.0
Broadcast => 192.168.1.63


















