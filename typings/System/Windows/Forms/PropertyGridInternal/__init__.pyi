# encoding: utf-8
# module System.Windows.Forms.PropertyGridInternal calls itself PropertyGridInternal
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Guid

from System.ComponentModel import AttributeCollection

from System.ComponentModel.Design import CommandID

from System.Windows.Forms.Design import PropertyTab


# no functions
# classes

class IRootGridEntry: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BrowsableAttributes(self) -> AttributeCollection:
        """
        Get: BrowsableAttributes(self: IRootGridEntry) -> AttributeCollection
        Set: BrowsableAttributes(self: IRootGridEntry) = value
        """
        ...


    def ResetBrowsableAttributes(self): # -> 
        """ ResetBrowsableAttributes(self: IRootGridEntry) """
        ...

    def ShowCategories(self, showCategories:bool): # -> 
        """ ShowCategories(self: IRootGridEntry, showCategories: bool) """
        ...


class PropertiesTab(PropertyTab): # skipped bases: <type 'IExtenderProvider'>, <type 'object'>
    """ PropertiesTab() """
    pass

class PropertyGridCommands: # skipped bases: <type 'object'>, <type 'object'>
    """ PropertyGridCommands() """
    Commands: CommandID = ...
    Description: CommandID = ...
    Hide: CommandID = ...
    Reset: CommandID = ...
    wfcMenuCommand: Guid = ...
    wfcMenuGroup: Guid = ...


