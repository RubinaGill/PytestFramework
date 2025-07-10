import os

def is_running_in_docker():
    return os.environ.get('IN_DOCKER', 'false').lower() == 'true'
