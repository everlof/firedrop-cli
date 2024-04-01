import argparse
import requests
import logging

from importlib.metadata import version
import os

def get_protocol():
    return os.getenv('PROTOCOL', 'https')

def get_host():
    return os.getenv('HOST', 'api.example.com')

def get_port():
    return os.getenv('PORT', '443')

def get_package_version(package_name):
    try:
        return version(package_name)
    except Exception:
        return None

def main(args):
    parser = argparse.ArgumentParser(description='Firedrop CLI')
    parser.add_argument('--version', action='version', version=get_package_version("firedrop_cli"))
    args = parser.parse_args()

    url = f'{get_protocol()}://{get_host()}:{get_port()}/url-drop-e9c1d/us-central1/send_url'
    logging.debug("URL: ", url)

    data = {
        'token': '387295C4790E4EF58F38EF70F18C83DB',
        'url': 'https://mjukis.dev/'
    }

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Success")
    else:
        print(f'Error: {response.status_code}')


