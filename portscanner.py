# python portscanner
import sys
import socket
from concurrent.futures import ThreadPoolExecutor
from services import common_services
socket.setdefaulttimeout(0.5)

# create port object
class port:
	def __init__(self, number):
		self.number = number
		self.open = False
		self.service = None
		self.protocol = None

	def __str__(self):
		status = "open" if self.open else "closed"
		service = self.service or "unknown"

		return f"port {self.number}/{self.protocol}: {status} - {service}"

# tcp/IPV4 portscanning
def tcp_scan(scan_ip: str, scan_port: int):
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# tcp scan
	result = tcp_socket.connect_ex((scan_ip, scan_port))
	tcp_socket.close()

	if result == 0:
		tcp_port = port(int(scan_port))
		tcp_port.open = True
		tcp_port.protocol = "TCP"

		# service detection
		if tcp_port.number in common_services:
			tcp_port.service = common_services[scan_port]

		return tcp_port

# udp/IPV4 portscanning
def udp_scan(scan_ip: str, scan_port: int):

	# udp scan
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:

		try:
			udp_socket.sendto(b'str', (scan_ip, scan_port))
			udp_response = udp_socket.recvfrom(1024)

		except socket.timeout:
			return None

	udp_port = port(int(scan_port))
	udp_port.open = True
	udp_port.protocol = "UDP"
	udp_port.service = common_services.get(scan_port)

	return udp_port

def portscanning(target: str, port: int):
	results: list[port] = []

	tcp_result = tcp_scan(target, port)

	if tcp_result:
		results.append(tcp_result)

	udp_result = udp_scan(target, port)

	if udp_result:
		results.append(udp_result)

	return results

def main(target):
	ports = []

	# multi threading
	with ThreadPoolExecutor(max_workers=250) as executor:

		results = executor.map(
			lambda port: portscanning(target, port),
			range(1, 10001)
		)

		for result in results:
			ports.extend(result)

	return ports


if __name__ == "__main__":

	if len(sys.argv) != 2:
		print(f"Usage: python3 {sys.argv[0]} <ip>")
		sys.exit(1)

	target_ip: str = sys.argv[1]
	print(f"scanning {target_ip}...")
	results = main(target_ip)

	for port in results:
		print(port)






