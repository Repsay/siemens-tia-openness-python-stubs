# encoding: utf-8
# module Microsoft.PowerShell.Cmdletization.Cim calls itself Cim
# from Microsoft.PowerShell.Commands.Management, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.PowerShell.Cmdletization import SessionBasedCmdletAdapter

from System import Array, SystemException

from System.Management.Automation import (IContainsErrorRecord, 
    IDynamicParameters)

"""The following names are not found in the module: BoundEvent, QueryBuilder
"""

# no functions
# classes

class CimCmdletAdapter(SessionBasedCmdletAdapter, IDynamicParameters): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ CimCmdletAdapter() """
    @property
    def CimSession(self) -> Array:
        """
        Get: CimSession(self: CimCmdletAdapter) -> Array[CimSession]
        Set: CimSession(self: CimCmdletAdapter) = value
        """
        ...


    def GetQueryBuilder(self): # -> QueryBuilder
        """ GetQueryBuilder(self: CimCmdletAdapter) -> QueryBuilder """
        ...


class CimJobException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CimJobException()
    CimJobException(message: str)
    CimJobException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


