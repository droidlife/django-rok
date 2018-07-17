import paramiko
import sys
from django_rok.re_forward_port import reverse_forward_tunnel
from django_rok.util import bcolors
ssh_port = 22
localhost = '127.0.0.1'


def create_ssh_tunnel(localport, remote_host, remote_port, username, password=None, pkey=None):
    transport = paramiko.Transport((remote_host, ssh_port))

    transport.connect(hostkey=None,
                      username=username,
                      password=password,
                      pkey=pkey)

    reverse_tunnel_url = 'http://' + str(remote_host) + ':' + str(remote_port)
    initalizing_info = bcolors.OKGREEN + 'Starting Reverse Tunnel at ' + reverse_tunnel_url + bcolors.ENDC

    try:
        print(initalizing_info)
        reverse_forward_tunnel(remote_port, localhost, localport, transport)
    except KeyboardInterrupt:
        print('Ssh Tunelling Stopped')
        sys.exit(0)
