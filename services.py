common_services = {
	# file transfer
	20: "ftp-data",
	21: "ftp",
	69: "tftp",
	115: "sftp",
	989: "ftps-data",
	990: "ftps",

	# remote access / administration
	22: "ssh",
	23: "telnet",
	3389: "rdp",
	5900: "vnc",
	5901: "vnc",
	5800: "vnc-http",
	5985: "winrm-http",
	5986: "winrm-https",
	623: "ipmi",
	664: "ipmi",
	512: "rexec",
	513: "rlogin",
	514: "syslog",

	# mail
	25: "smtp",
	109: "pop3",
	110: "pop3",
	143: "imap",
	465: "smtps",
	587: "smtp-submission",
	993: "imaps",
	995: "pop3s",

	# DNS / DHCP / network
	53: "dns",
	67: "dhcp-server",
	68: "dhcp-client",
	123: "ntp",
	161: "snmp",
	162: "snmptrap",
	500: "isakmp",
	520: "rip",
	546: "dhcpv6-client",
	547: "dhcpv6-server",
	853: "dns-tls",
	5353: "mdns",
	5355: "llmnr",

	# HTTP / HTTPS / Web
	80: "http",
	81: "http",
	443: "https",
	8008: "http",
	8081: "http",
	8088: "http",
	8089: "http",
	8280: "apache-http",
	8443: "https",
	8888: "http",
	9090: "prometheus",
	9200: "elasticsearch",
	9300: "elasticsearch-cluster",

	# proxies
	1080: "socks-proxy",
	3128: "squid-proxy",
	8080: "http-proxy",

	# SMB / windows
	135: "msrpc",
	137: "netbios-ns",
	138: "netbios-dgm",
	139: "netbios-ssn",
	445: "smb",

	# LDAP / kerberos
	88: "kerberos",
	389: "ldap",
	464: "kerberos-password",
	543: "kerberos-login",
	544: "kerberos-remote-shell",
	636: "ldaps",
	749: "kerberos-admin",

	# databases
	118: "sql",
	156: "sql",
	1433: "mssql",
	1521: "oracle",
	1830: "oracle",
	3306: "mysql",
	5432: "postgresql",
	6379: "redis",
	9042: "cassandra",
	9105: "xadmin",
	27017: "mongodb",
	27018: "mongodb",
	28017: "mongodb-http",

	# CMS
	2082: "cpanel",
	2083: "cpanel-ssl",
	2086: "whm",
	2087: "whm-ssl",
	9000: "php-fpm",
	10000: "webmin",

	# message brokers
	1883: "mqtt",
	8883: "mqtt-tls",
	5672: "amqp",
	5671: "amqp-tls",
	61616: "activemq",

	# IRC / XMPP
	194: "irc",
	5222: "xmpp",
	5223: "xmpp-tls",
	6665: "irc",
	6666: "irc",
	6667: "irc",
	6668: "irc",
	6669: "irc",

	# SIP / VoIP
	5060: "sip",
	5061: "sip-tls",

	# VNC / remote desktop
	5902: "vnc",
	5938: "teamviewer",

	# X11
	6000: "x11",
	6001: "x11",
	6002: "x11",
	6003: "x11",

	# TOR / onion
	9001: "tor",
	9030: "tor-dir",
	9050: "tor-socks",
	9051: "tor-control",

	# I2P
	4444: "i2p-http-proxy",
	4445: "i2p-https-proxy",
	7657: "i2p-router-console",
	7658: "i2p-i2ptunnel",
	7659: "i2p-sam",
	7660: "i2p-sam",
	7654: "i2p-http",

	# kubernetes / containers
	2375: "docker-api",
	2376: "docker-api-tls",
	6443: "kubernetes-api",
	10250: "kubelet",

	# monitoring / infrastructure
	3000: "development-http",
	9100: "jetdirect",
	10050: "zabbix-agent",
	10051: "zabbix-server",

	# Git / development
	9418: "git",
	5000: "development-http",

	# VPN
	1194: "openvpn",
	51820: "wireguard",

	# UPnP / SSDP
	1900: "ssdp",

	# NFS / RPC
	111: "rpcbind",
	2049: "nfs",

	# FTP alternatives
	2121: "ftp",

	# printer / network management
	515: "lpd",
	631: "ipp",

	# FRITZ!Box / AVM
	8181: "fritzbox-http",
	8182: "fritzbox-network-block",
	8183: "fritzbox-update",
	8184: "fritzbox-ticket-login",
	8185: "fritzbox-guestnetwork",
	8186: "fritzbox-guestnetwork-login",
	8189: "fritzbox-guestnetwork-info",
	49000: "upnp",
	49200: "fritz!-media-server",
	49443: "upnp-https",
	53805: "fritz!-mesh-discovery",
	57557: "fritz!-mesh",
}
