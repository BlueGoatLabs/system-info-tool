import platform
import socket

print("=== SYSTEM INFO ===")

print("System:", platform.system())
print("Node Name:", platform.node())
print("Release:", platform.release())
print("Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("IP Address:", ip_address)