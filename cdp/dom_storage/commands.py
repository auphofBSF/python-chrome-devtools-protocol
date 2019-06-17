'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: dom_storage
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


class DOMStorage:
    @staticmethod
    def clear(storage_id: StorageId) -> None:
        '''
        
        
        :param storage_id: 
        '''

        cmd_dict = {
            'method': 'DOMStorage.clear',
            'params': {
                'storageId': storage_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def disable() -> None:
        '''
        Disables storage tracking, prevents storage events from being sent to the client.
        '''

        cmd_dict = {
            'method': 'DOMStorage.disable',
        }
        response = yield cmd_dict

    @staticmethod
    def enable() -> None:
        '''
        Enables storage tracking, storage events will now be delivered to the client.
        '''

        cmd_dict = {
            'method': 'DOMStorage.enable',
        }
        response = yield cmd_dict

    @staticmethod
    def get_dom_storage_items(storage_id: StorageId) -> typing.List['Item']:
        '''
        
        
        :param storage_id: 
        :returns: 
        '''

        cmd_dict = {
            'method': 'DOMStorage.getDOMStorageItems',
            'params': {
                'storageId': storage_id,
            }
        }
        response = yield cmd_dict
        return [Item.from_response(i) for i in response['entries']]

    @staticmethod
    def remove_dom_storage_item(storage_id: StorageId, key: str) -> None:
        '''
        
        
        :param storage_id: 
        :param key: 
        '''

        cmd_dict = {
            'method': 'DOMStorage.removeDOMStorageItem',
            'params': {
                'storageId': storage_id,
                'key': key,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_dom_storage_item(storage_id: StorageId, key: str, value: str) -> None:
        '''
        
        
        :param storage_id: 
        :param key: 
        :param value: 
        '''

        cmd_dict = {
            'method': 'DOMStorage.setDOMStorageItem',
            'params': {
                'storageId': storage_id,
                'key': key,
                'value': value,
            }
        }
        response = yield cmd_dict
