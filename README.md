# ArcticWEB

## Client-server communication protocol

### Handshake

Between Client and Main server:
Server          Client
|  <----------  '0' This is a client
serverlist------>|  Server sends back list of available servers
|  <--------Server name user chose
server IP ------>|  The IP of the server chosen by the user

