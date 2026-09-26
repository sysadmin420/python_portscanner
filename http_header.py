# http-header service & version detection python
import requests

# create header object
class http_header:
	def __init__(self):
		self.port = None
		self.open = False
		self.service = None
		self.version = None

	def __str__(self):
		status = "open" if self.open else "closed"
		service = self.service or "unknown"
		version = self.version or "unknown"

		return f"port {self.port}/TCP: {status} - {service} {version}"

# request http-headers
def request_header(ip_addr: str, port: int, common_service: str, ipv6=False):
	try:

		if common_service == "https":
			http_protocol = "https"

		else:
			http_protocol = "http"

		target_url = f"{hypertext}://{ip_addr}:{port}/"

		if ipv6 == True:
			target_url = f"{http_protocol}://[{ip_addr}]:{port}/"

		response = requests.get(
			target_url,
			timeout=1
		)

		server_header = http_header()

		server_header.port = port
		server_header.open = True
		server_header.service = common_service
		server_header.version = response.headers.get("Server")

		return server_header

	except requests.RequestException:
		return None
