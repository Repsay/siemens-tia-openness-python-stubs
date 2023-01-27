# encoding: utf-8
# module Microsoft.PowerShell.Commands.Management calls itself Management
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Transactions import IEnlistmentNotification


# no functions
# classes

class TransactedString(IEnlistmentNotification): # skipped bases: <type 'object'>
    """
    TransactedString()
    TransactedString(value: str)
    """
    @property
    def Length(self) -> int:
        """ Get: Length(self: TransactedString) -> int """
        ...


    def Append(self, text:str): # -> 
        """ Append(self: TransactedString, text: str) """
        ...

    def Remove(self, startIndex:int, length:int): # -> 
        """ Remove(self: TransactedString, startIndex: int, length: int) """
        ...

    def ToString(self) -> str:
        """ ToString(self: TransactedString) -> str """
        ...


