'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: security
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *


class Security:
    @staticmethod
    def disable() -> None:
        '''
        Disables tracking security state changes.
        '''

        cmd_dict = {
            'method': 'Security.disable',
        }
        response = yield cmd_dict

    @staticmethod
    def enable() -> None:
        '''
        Enables tracking security state changes.
        '''

        cmd_dict = {
            'method': 'Security.enable',
        }
        response = yield cmd_dict

    @staticmethod
    def set_ignore_certificate_errors(ignore: bool) -> None:
        '''
        Enable/disable whether all certificate errors should be ignored.
        
        :param ignore: If true, all certificate errors will be ignored.
        '''

        cmd_dict = {
            'method': 'Security.setIgnoreCertificateErrors',
            'params': {
                'ignore': ignore,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def handle_certificate_error(event_id: int, action: CertificateErrorAction) -> None:
        '''
        Handles a certificate error that fired a certificateError event.
        
        :param event_id: The ID of the event.
        :param action: The action to take on the certificate error.
        '''

        cmd_dict = {
            'method': 'Security.handleCertificateError',
            'params': {
                'eventId': event_id,
                'action': action,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_override_certificate_errors(override: bool) -> None:
        '''
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
        be handled by the DevTools client and should be answered with `handleCertificateError` commands.
        
        :param override: If true, certificate errors will be overridden.
        '''

        cmd_dict = {
            'method': 'Security.setOverrideCertificateErrors',
            'params': {
                'override': override,
            }
        }
        response = yield cmd_dict
