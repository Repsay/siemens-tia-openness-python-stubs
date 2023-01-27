# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.Parser.Internals calls itself Internals
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ParseContextState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParseContextState, values: BindCompleted (4), Binding (3), Initial (0), ParseCompleted (2), Parsing (1) """
    BindCompleted: ParseContextState = ...
    Binding: ParseContextState = ...
    Initial: ParseContextState = ...
    ParseCompleted: ParseContextState = ...
    Parsing: ParseContextState = ...
    value__ = ...


