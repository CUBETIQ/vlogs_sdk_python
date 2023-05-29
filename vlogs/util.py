import os
import socket
import uuid


def generate_uuid():
    return str(uuid.uuid4())


def get_system_hostname():
    name = 'localhost'
    if hasattr(socket, 'gethostname'):
        name = socket.gethostname()
    elif 'HOSTNAME' in os.environ:
        name = os.environ['HOSTNAME']

    return name


def get_system_username():
    name = 'unknown'
    if hasattr(os, 'getlogin'):
        name = os.getlogin()
    elif 'USER' in os.environ:
        name = os.environ['USER']

    return name
