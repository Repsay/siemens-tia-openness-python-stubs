# encoding: utf-8
# module Microsoft.Windows.Input calls itself Input
# from System.Windows.Controls.Ribbon, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Windows.Input import ICommand

"""The following names are not found in the module: ICommandSource
"""

# no functions
# classes

class IPreviewCommand(ICommand): # skipped bases: <type 'object'>
    """ no doc """
    def CancelPreview(self): # -> 
        """ CancelPreview(self: IPreviewCommand) """
        ...

    def Preview(self, parameter:object): # -> 
        """ Preview(self: IPreviewCommand, parameter: object) """
        ...


class IPreviewCommandSource(ICommandSource): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PreviewCommandParameter(self) -> object:
        """ Get: PreviewCommandParameter(self: IPreviewCommandSource) -> object """
        ...



