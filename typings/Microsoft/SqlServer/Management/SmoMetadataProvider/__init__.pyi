# encoding: utf-8
# module Microsoft.SqlServer.Management.SmoMetadataProvider calls itself SmoMetadataProvider
# from Microsoft.SqlServer.Management.SmoMetadataProvider, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import ServerConnection

from Microsoft.SqlServer.Management.Smo import Server, SqlSmoObject

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    MetadataProviderBase)


# no functions
# classes

class ISmoDatabaseObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SmoObject(self) -> SqlSmoObject:
        """ Get: SmoObject(self: ISmoDatabaseObject) -> SqlSmoObject """
        ...



class SmoMetadataProvider(MetadataProviderBase): # skipped bases: <type 'IMetadataProvider'>, <type 'object'>
    """ no doc """
    @property
    def SmoServer(self) -> Server:
        """ Get: SmoServer(self: SmoMetadataProvider) -> Server """
        ...


    @staticmethod
    def CreateConnectedProvider(connection:ServerConnection, refreshDbListMillisecond:int = ...) -> SmoMetadataProvider:
        """
        CreateConnectedProvider(connection: ServerConnection) -> SmoMetadataProvider
        CreateConnectedProvider(connection: ServerConnection, refreshDbListMillisecond: int) -> SmoMetadataProvider
        """
        ...

    @staticmethod
    def CreateDisconnectedProvider(server:Server) -> SmoMetadataProvider:
        """ CreateDisconnectedProvider(server: Server) -> SmoMetadataProvider """
        ...


