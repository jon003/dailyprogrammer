#!/usr/bin/python

import socket
import sys 

irc_server = 'chat.freenode.net'
irc_port = 6667
irc_nick = 'rdp258E'

nicksend = 'NICK  ' + irc_nick + '\r\n'
usersend = 'USER rpd258E 0 * rpd258E' + '\r\n'

debug = 1

if debug:
	print('DEBUG: NICKLINE: %s' % nicksend)
	print('DEBUG: USERLINE: %s' % usersend)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # this options mean ipv4, tcp
	print('Socket created.')
except socket.error, msg:
	print('Failed to create socket.  Error: ' + str(msg[0]) + ' Error Message: ' + msg[1])


try:
	remote_ip = socket.gethostbyname(irc_server)
except socket.gaierror:
	# can't resolve hostname
	print('Could not resolve: ' + irc_server)

print('Hostname lookup reports ' + irc_server + ' as ' + remote_ip)

try:
	s.connect((remote_ip, irc_port))
except Exception as msg:
	print('Connection failed: ' + msg)

print('Connected to ' + str(remote_ip) + ' on ' + str(irc_port))

try:
	s.send(nicksend)
	if debug:
		print('DEBUG: Sent nick.')
	s.send(usersend)
	if debug:
		print('DEBUG: Sent user.')
except socket.error:
	print('Send failed')

buffer = ''
if debug:
	print('DEBUG: entering main buffer loop.')

while True:
	if '\r\n' not in buffer:
		buffer += s.recv(512)
	line, buffer = buffer.split('\r\n', 1)
	print line
	line = line.split()
	if line[0] == 'PING':
		print('Recieved PING request')
		s.send('PONG %s\r\n' % line[1])

s.close()
