# encoding: utf-8
# module System.Windows.Input calls itself Input
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ICommand: # skipped bases: <type 'object'>
    """ no doc """
    def CanExecute(self, parameter:object) -> bool:
        """ CanExecute(self: ICommand, parameter: object) -> bool """
        ...

    def Execute(self, parameter:object): # -> 
        """ Execute(self: ICommand, parameter: object) """
        ...

    CanExecuteChanged = ...


