import io
import json
import os
import paramiko
import select
import socket
import sys
import threading
import urllib.request
from datetime import datetime
from optparse import OptionParser
from platformdirs import user_config_dir

def connection_handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        print(f'Incoming request to {host}:{port} failed:', e)
        return

    print(f'Received incoming request to {host}:{port}')
    while True:
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
    chan.close()
    sock.close()

def await_connections(remote_host, remote_port, transport):
    while True:
        chan = transport.accept(1000)
        if chan is None:
            continue
        threading.Thread(target=connection_handler, daemon=True, args=(chan, remote_host, remote_port)).start()

def config(key=None, value=None):
    app_name = __name__.split('.')[0]
    config_dir = user_config_dir(app_name)
    config_file = os.path.join(config_dir, 'config.json')

    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
    else:
        config = {}

    if key is not None:
        config[key] = value
        with open(config_file, 'w') as f:
            json.dump(config, f)
    else:
        return config

def load_options():
    parser = OptionParser(usage='\t%prog public_hostname [-h forward_host] [-p forward_port]\n\t%prog --configure', add_help_option=False)
    parser.add_option('-c', '--configure', action='store_true', dest='configure')
    parser.add_option('-h', '--host', action='store', dest='host', type='string', default='localhost')
    parser.add_option('-p', '--port', action='store', dest='port', type='int', default=8080)
    options, args = parser.parse_args()

    hostname = args[0] if len(args) > 0 else None
    if not options.configure and not hostname:
        parser.error('see usage instructions above')

    if options.configure:
        config('server_name', input('Enter server name: '))
        config('secret_key', input('Enter secret key: '))
        print('Configuration saved.')
        sys.exit(1)

    c = config()
    if 'server_name' not in c or 'secret_key' not in c or not c['server_name'] or not c['secret_key']:
        parser.error('configuration required')

    return {
        'hostname':     hostname,
        'server_name':  c['server_name'],
        'secret_key':   c['secret_key'],
        'forward_host': options.host,
        'forward_port': options.port
    }

def get_port_mapping(hostname, server_name, secret_key):
    request_body = json.dumps({ 'hostname': hostname }).encode('utf-8')
    request = urllib.request.Request(f'https://{server_name}/mappings', data=request_body, method='POST')
    request.add_header('Authorization', f'Bearer {secret_key}')
    request.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(request) as response:
            if response.status in [200, 201]:
                return json.load(response)
            else:
                return False
    except urllib.error.URLError as e:
        print('Failed to request port mapping:', e.reason)
        return False

def run():
    opts = load_options()
    hostname     = opts['hostname']
    server_name  = opts['server_name']
    secret_key   = opts['secret_key']
    forward_host = opts['forward_host']
    forward_port = opts['forward_port']

    response = get_port_mapping(hostname, server_name, secret_key)
    if not response:
        sys.exit(1)

    tunnel_domain = response['tunnel']['domain']
    tunnel_host   = response['tunnel']['host']
    tunnel_port   = response['tunnel']['port']
    tunnel_user   = response['tunnel']['user']
    tunnel_key    = response['tunnel']['key']
    remote_host   = response['mapping']['hostname']
    remote_port   = response['mapping']['port']
    expiration    = response['mapping']['expiration']

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key(io.StringIO(tunnel_key))
        client.connect(f'{tunnel_host}.{tunnel_domain}', tunnel_port, username=tunnel_user, pkey=private_key)
        transport = client.get_transport()
        transport.request_port_forward('', remote_port)
    except Exception as e:
        print(f'Failed to establish port forwarding:', e)
        sys.exit(1)

    exp_str = datetime.fromtimestamp(expiration).strftime('%-m/%-d/%Y %-I:%M:%S %p')
    print(f'{forward_host}:{forward_port} forwarded to {remote_host}.{tunnel_domain} until {exp_str}')

    try:
        await_connections(forward_host, forward_port, transport)
    except KeyboardInterrupt:
        print()
        print('Port forwarding stopped')
        sys.exit(0)
