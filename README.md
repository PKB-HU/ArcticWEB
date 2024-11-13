# ArcticWEB

## Client-server communication protocol

### Handshake

Between Client and Main server on port 5667:
Server          Client
|  <----------  '0' This is a client
serverlist------>|  Server sends back list of available servers
|  <--------Server name user chose
server IP ------>|  The IP of the server chosen by the user

### Connecting to Content server

The content server IP is sent to the client in the handshake step. The server is available on port 5666.

The Content server sends the client the configs, like how the application should look like, what error messages to display and so on.
The complete list is the following:
- server name
- server displayname
- buttonframe background
- opacity
- label color
- label background color
- label size
- background color
- font color
- font background color
- result textbox color
- result textbox edge color
- result textbox edge color(if selected)
- result textbox edge size
- searchbar color
- searchbar edge color
- searchbar edge color(if selected)
- searchbar edge size
- send-command button background color
- send-command button text color
- send-command button background color(if button is pressed)
- send-command button text color(if button is pressed)
- refresh-list button background color
- refresh-list button text color
- refresh-list button background color(if button is pressed)
- refresh-list button text color(if button is pressed)
- create-new button background color
- create-new button text color
- create-new button background color(if button is pressed)
- create-new button text color(if button is pressed)
- starting label text
- site not found error message
- user-got-admin-rights message
- under-maintenance error message
- user-not-on-whitelist error message
- help message
- successful-admin-promotion message
- failed-admin-promotion message
- successfull-whitelist-update message
- failed-whitelist-update message
- command-disabled error message
- rules message

After this, the server goes into command-processing mode and waits for messages from the client.

### Client commands

The server can process the following commands:

- usr<username>: this informs the server about the nickname of the connected user. The server sends back a 1 if the user is admin, otherwise sends a 0.
- need<sitename>: the server sends back the requested site.
- create<siteName>: creates a site, and writes subsequent messages into it, until it encounters a message with the content "//quit".
- list: sends back the list of available sites
- ###close: closes the connection, disconnects the user.
- addAdmin: tries to promote next user sent to the server to admin. Sends back a 1 if successfull, 0 if failed.
- whitelist: tries to add the next user sent to the server to the whitelist. Sends back a 1 if successfull, 0 if failed.