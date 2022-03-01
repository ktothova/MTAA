import socketserver
import socket
import sys
import time
import logging
import sipfullproxy as proxy

HOST, PORT = '0.0.0.0', 5060


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    server = socketserver.UDPServer((HOST, PORT), proxy.UDPHandler)
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()
