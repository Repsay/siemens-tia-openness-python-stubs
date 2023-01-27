# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.SystemMetadataProvider calls itself SystemMetadataProvider
# from Microsoft.SqlServer.Management.SystemMetadataProvider, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.SqlParser.Metadata import (CollationInfo, 
    IMutableDatabase, IMutableServer, IServer)

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    MetadataProviderBase)


# no functions
# classes

class SystemMetadataFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateDatabase(server:IServer, name:str, collationInfo:CollationInfo) -> IMutableDatabase:
        """ CreateDatabase(server: IServer, name: str, collationInfo: CollationInfo) -> IMutableDatabase """
        ...

    @staticmethod
    def CreateServer(collationInfo:CollationInfo) -> IMutableServer:
        """ CreateServer(collationInfo: CollationInfo) -> IMutableServer """
        ...

    __all__: list = ...


class SystemMetadataProvider(MetadataProviderBase): # skipped bases: <type 'IMetadataProvider'>, <type 'object'>
    """ SystemMetadataProvider(collationInfo: CollationInfo) """
    def AddDatabase(self, name:str, collationInfo:CollationInfo): # -> 
        """ AddDatabase(self: SystemMetadataProvider, name: str, collationInfo: CollationInfo) """
        ...


