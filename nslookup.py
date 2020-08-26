import socket

file = 'Targets.txt'
f = open(file, 'r')
lines = f.readlines()
f.close()
for i in lines:    
	host = i.strip()
	if host !="": 
		try: 
			hname, aliases, ipaddrs = socket.gethostbyaddr(host)
			print("{} , {} ".format(hname,ipaddrs))
		except Exception as e:
			print(host,",NotAvailable")
