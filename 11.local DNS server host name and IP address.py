import socket
# Get hostname
hostname = socket.gethostname()
# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
# Connect to a public DNS server (no data is sent)
s.connect((&quot;8.8.8.8&quot;, 80))
ip_address = s.getsockname()[0]
finally:
s.close()
print(&quot;Host Name :&quot;, hostname)
print(&quot;IP Address:&quot;, ip_address)
