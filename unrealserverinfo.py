# Little script to get the server info of a Rune server.
# I expect this to work for other Unreal Engine 1 games as well.
import socket

# The remote host
HOST = # TODO
# The remote port
PORT = # TODO

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))
s.sendall('\\info\\')
data = s.recv(256)
s.close()
serverinfo = repr(data)[3:-3].split("\\\\")
if serverinfo[-1] == 'final' and (len(serverinfo) % 2) != 0:
  pairs = zip(serverinfo[::2], serverinfo[1::2])
  for el in pairs:
    print el[0] + ": " + el[1]
else:
  print "Oops, something went wrong."

