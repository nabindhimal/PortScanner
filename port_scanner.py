import socket
import termcolor

def scan(target, ports):
#	print(termcolor.colored(('\n' + ' Starting Scan For ' + str(target)),'green'))
	print(termcolor.colored(('\n' + ' Starting Scan For ' + str(target)), 'red'), end='\n', flush=True)
	for port in range(1,ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(f"[+] Port Opened: {port}")
		sys.stdout.flush()
		sock.close()
	except:
		# print(f"[-] Port Closed: {port}")
		pass
targets = input("[*] Enter Targets To Scan(Split them by comma): ")
ports =int(input("[*] How many ports do you want to scan?: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	sys.stdout.flush()
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)
