import socket
import sys
import time

server = "irc.chat.twitch.tv"
port = 6667
channel = ""
botnick = ""
token = ""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to: " + server
irc.connect((server, port))
print "connected."

irc.send("PASS " + token + "\r\n")
irc.send("NICK " + botnick + "\r\n")
irc.send("JOIN "+ channel + "\r\n")

while True:
    text = irc.recv(2040)
    print text

    #returns 'PONG' back to the server (prevents pinging out!)
    if text.find('PING') != -1:
        irc.send('PONG ' + text.split()[1] + '\r\n')
    time.sleep(1)
