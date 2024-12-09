import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Name of bulb to change")
parser.add_argument("-c", "--color", help="Change the color of the bulb", default=None)
parser.add_argument("--off", help="Turn off a bulb", action="store_true")
args = parser.parse_args()

ips = {'reading_light': '192.168.0.167', 'bar_2': '192.168.0.66', 'bed_2': '192.168.0.142', 'bed_1': '192.168.0.40', 'bar_1': '192.168.0.4'}
port = 38899
sock = ''

def changeColor(ip, color, dim):
    msg = '{{"method":"setPilot", "params":{{"r":{},"g":{},"b":{},"dimming":{}}}}}'.format(color[0], color[1], color[2], dim)
    sock.sendto(bytes(msg, 'utf-8'), (ip, port))

def bulbOff(ip):
    msg = '{"method":"setPilot", "params":{"state":false}}'
    print(msg)
    sock.sendto(bytes(msg, 'utf-8'), (ip, port))

# Socket to talk to bulbs
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Collecting args
target_bulb = args.n
target_col = ''
dim = 50

if args.color == 'red':
    target_col = [255, 0, 0]
elif args.color == 'blue':
    target_col = [0, 0, 255]
elif args.color == 'green':
    target_col = [0, 255, 0]
elif args.color != None: #-c '244 244 244'
    target_col = [int(c) for c in args.color.split(' ')]

if args.color != None:
    changeColor(ips[target_bulb], target_col, dim)

if args.off:
    bulbOff(ips[target_bulb])



# Test code to change bulbs
'''
val = 0
dim = 50
for light in ips:
    print(light, val) 
    changeColor(ips[light], val, 0, 0, dim)
    val += 255 / 5
'''
