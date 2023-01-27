# encoding: utf-8
# module Microsoft.PowerShell.Cmdletization.Xml calls itself Xml
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ConfirmImpact(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfirmImpact, values: High (3), Low (1), Medium (2), None (0) """
    High: ConfirmImpact = ...
    Low: ConfirmImpact = ...
    Medium: ConfirmImpact = ...
    value__ = ...


class ItemsChoiceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ItemsChoiceType, values: ExcludeQuery (0), MaxValueQuery (1), MinValueQuery (2), RegularQuery (3) """
    ExcludeQuery: ItemsChoiceType = ...
    MaxValueQuery: ItemsChoiceType = ...
    MinValueQuery: ItemsChoiceType = ...
    RegularQuery: ItemsChoiceType = ...
    value__ = ...


