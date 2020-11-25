from django.apps import AppConfig

"""
---------------------------------------------------------------------------------------------------------------------------------------------
django.apps is a registry of installed applications that stores configuration
which is then imported from elsewhere.
---------------------------------------------------------------------------------------------------------------------------------------------
"""


class AccountConfig(AppConfig):
    name = 'account'

"""
---------------------------------------------------------------------------------------------------------------------------------------------
AccountConfig is a class with a module for associating with values in it's configured state.
Default values are defined and provides a description of each parameter.
---------------------------------------------------------------------------------------------------------------------------------------------
"""