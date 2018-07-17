from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from django_rok.ssh_tunnel import create_ssh_tunnel
import sys
import os
import threading
from django_rok.util import bcolors


class Command(BaseCommand):
    help = 'Command to run runrok server along with django development server'

    def parse_argumens(self, *args, **options):
        args_dict = {
            'remote_host': None,
            'remote_port': None,
            'env': 'dev',
            'local_port': 8000,
            'user_name': None,
            'password': None,
            'pkey': None
        }

        if hasattr(settings, 'ROK_REMOTE_HOST'):
            args_dict['remote_host'] = settings.ROK_REMOTE_HOST
        else:
            if 'remote_host' in options and options['remote_host']:
                args_dict['remote_host'] = options['remote_host']
            else:
                raise Exception(bcolors.WARNING + 'No remote host found. ' +
                                'Please add it in setting.py like ROK_REMOTE_HOST=192.168.1.1' +
                                ' or pass using command line like -r 192.168.1.1 ' + bcolors.ENDC)

        if hasattr(settings, 'ROK_REMOTE_PORT'):
            args_dict['remote_port'] = settings.ROK_REMOTE_PORT
        else:
            if 'remote_port' in options and options['remote_port']:
                args_dict['remote_port'] = options['remote_port']
            else:
                raise Exception(bcolors.WARNING + 'No remote port found. ' +
                                'Please add it in setting.py like ROK_REMOTE_PORT=9000' +
                                ' or pass using command line like -rp 9000 ' + bcolors.ENDC)

        if hasattr(settings, 'ROK_USERNAME'):
            args_dict['user_name'] = settings.ROK_USERNAME
        else:
            if 'user_name' in options and options['user_name']:
                args_dict['user_name'] = options['user_name']
            else:
                raise Exception(bcolors.WARNING + 'No remote username found. ' +
                                'Please add it in setting.py like ROK_USERNAME=root' +
                                ' or pass using command line like -u root ' + bcolors.ENDC)

        if hasattr(settings, 'ROK_LOCAL_PORT'):
            args_dict['local_port'] = settings.ROK_LOCAL_PORT
        else:
            if 'local_port' in options and options['local_port']:
                args_dict['local_port'] = options['local_port']
            else:
                if not os.environ.get('RUN_MAIN', False):
                    print(bcolors.OKBLUE + 'No local port specified. Using default 8000' + bcolors.ENDC)

        if hasattr(settings, 'ROK_PASSWORD'):
            args_dict['password'] = settings.ROK_PASSWORD
        else:
            if 'password' in options and options['password']:
                args_dict['password'] = options['password']
            else:
                if not os.environ.get('RUN_MAIN', False):
                    print(bcolors.OKBLUE + 'No Password specified. Connecting without it.' + bcolors.ENDC)

        if hasattr(settings, 'ROK_KEY'):
            args_dict['pkey'] = settings.ROK_KEY
        else:
            if 'pkey' in options and options['pkey']:
                args_dict['pkey'] = options['pkey']
            else:
                if not os.environ.get('RUN_MAIN', False):
                    print(bcolors.OKBLUE + 'No private key specified. Connecting without it' + bcolors.ENDC)

        if hasattr(settings, 'ROK_ENV'):
            args_dict['env'] = settings.ROK_ENV
        else:
            if 'env' in options and options['env']:
                args_dict['env'] = options['env']

        if not os.environ.get('RUN_MAIN', False):
            print(bcolors.OKBLUE + 'Using ' + args_dict['env'] + ' environment.' + bcolors.ENDC)

        return args_dict

    def add_arguments(self, parser):
        parser.add_argument('-lp', dest='local_port', help='The local port to forward the request.', type=int)
        parser.add_argument('-rp', dest='remote_port', help='The remote port for ssh connection.', type=int)
        parser.add_argument('-r', dest='remote_host', help='The remote host for ssh connection')
        parser.add_argument('-u', dest='user_name', help='The username for remote host')
        parser.add_argument('-p', dest='password', help='The password for remote host(If there)')
        parser.add_argument('-key', dest='pkey', help='The private key for remote host(If there)')
        parser.add_argument('-env', dest='env', help='Which env the server is running on')

    def handle(self, *args, **options):
        args_data = self.parse_argumens(*args, **options)
        try:
            if not os.environ.get('RUN_MAIN', False):
                ssh_tunnel_thread = threading.Thread(target=create_ssh_tunnel,
                                                     args=(args_data['local_port'], args_data['remote_host'],
                                                           args_data['remote_port'], args_data['user_name'],
                                                           args_data['password'], args_data['pkey']))
                ssh_tunnel_thread.start()

            if args_data['env'] != 'PRODUCTION':
                call_command('runserver', args_data['local_port'])
        except Exception:
            sys.exit()
