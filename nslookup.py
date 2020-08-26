import socket
#from netaddr import IPNetwork

file = 'Targets.txt'
f = open(file, 'r')
lines = f.readlines()
f.close()
for i in lines:    
	host = i.strip()
	#ip = IPNetwork(host)
	if host !="": 
		try: 
			hname, aliases, ipaddrs = socket.gethostbyaddr(host)
			print("{} , {} , {}".format(host,hname,ipaddrs))
		except Exception as e:
			print(host,",NotAvailable")