import socket

ips = ['192.168.0.167']
port = 38899
sock = ''

def changeColor(ip, r, g, b, dim):
    msg = '{"method":"setPilot", "params":{"r":r,"g":g,"b":b,"dimming":dim}}'
    sock.sendto(bytes(msg, 'utf-8'), (ip, port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

changeColor(ips[0], 0, 0, 255, 50)
