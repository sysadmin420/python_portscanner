# python portscanner
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from services import common_services
from http_header import request_header
socket.setdefaulttimeout(0.5)
parser = argparse.ArgumentParser(description="TCP/UDP - portscanner")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("--ipv4", type=str, help="Target IPv4 address")
group.add_argument("--ipv6", type=str, help="Target IPv6 address" )
parser.add_argument("-t", "--threads", type=int, help="Number of Threads", default=100)
args = parser.parse_args()

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
def tcp_scan(scan_ip: str, scan_port: int, ipv6=False):
	internet_protocol = socket.AF_INET6 if ipv6 else socket.AF_INET
	tcp_socket = socket.socket(internet_protocol, socket.SOCK_STREAM)

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
def udp_scan(scan_ip: str, scan_port: int, ipv6=False):

	# udp scan
	internet_protocol = socket.AF_INET6 if ipv6 else socket.AF_INET
	with socket.socket(internet_protocol, socket.SOCK_DGRAM) as udp_socket:

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

# main portscan + http-header service & version detection
def portscanning(target: str, port: int, ipv6=False):
	results: list[port] = []

	tcp_result = tcp_scan(target, port, ipv6)

	if tcp_result:
		http_header = request_header(
			ip_addr=target,
			port=port,
			common_service=tcp_result.service,
			ipv6=ipv6
		)

		if http_header:
			results.append(http_header)

		else:
			results.append(tcp_result)

	udp_result = udp_scan(target, port, ipv6)

	if udp_result:
		results.append(udp_result)

	return results

def main(target: str, ipv6=False):
	ports = []

	# multi threading
	with ThreadPoolExecutor(max_workers=args.threads) as executor:

		results = executor.map(
			lambda port: portscanning(target, port, ipv6),
			range(1, 10001)
		)

		for result in results:
			ports.extend(result)

	return ports


if __name__ == "__main__":
	if args.ipv6:
		target_ip: str = args.ipv6
		ipv6 = True

	elif args.ipv4:
		target_ip: str = args.ipv4
		ipv6 = False

	if args.threads < 1:
		parser.error("minimum Thread amount: 1")

	print(f"scanning {target_ip}...")
	results = main(target=target_ip, ipv6=ipv6)

	for port in results:
		print(port)
