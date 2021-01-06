#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Factories
'''

import urllib.parse
from restdict.client import RestDict
from restdict.server import DictServer


def new_server(server_address):
    '''
    Create new Web server with API REST
    '''
    return DictServer(server_address)


def new_client(server_api_uri):
    '''
    Create new client connected to a given API URI
    '''
    return RestDict(server_api_uri)

def connect_restdict(server_api_uri, dict_name=None):
    rest_dict = new_client(server_api_uri)
    rest_dict.connect_restdict(dict_name)
    return rest_dict

def new_restdict(server_api_uri, dict_name=None):
    rest_dict = new_client(server_api_uri)
    rest_dict.new_restdict(dict_name)
    return rest_dict


def delete_restdict(server_api_uri, dict_name=None):
    rest_dict = new_client(server_api_uri)
    rest_dict.delete_restdict(dict_name)
       