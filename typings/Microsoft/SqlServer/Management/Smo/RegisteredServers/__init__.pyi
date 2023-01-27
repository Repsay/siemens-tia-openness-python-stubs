# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.RegisteredServers calls itself RegisteredServers
# from Microsoft.SqlServer.SmoExtended, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IAlterable, ICreatable, 
    IDroppable)

from Microsoft.SqlServer.Management.Sdk.Sfc import Urn

from Microsoft.SqlServer.Management.Smo import SmoObjectBase

from System import Guid

from System.Collections import ICollection, IEnumerator

from System.DirectoryServices import PropertyCollection

from System.Security import SecureString

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class RegSvrSmoObject(SmoObjectBase): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: RegSvrSmoObject) -> str
        Set: Name(self: RegSvrSmoObject) = value
        """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: RegSvrSmoObject) -> PropertyCollection """
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: RegSvrSmoObject) -> Urn """
        ...

    @property
    def UrnSkeleton(self):
        ...


    def CheckObjectState(self, *args): #cannot find CLR method
        """ CheckObjectState(self: RegSvrSmoObject) """
        ...

    def ImplInitialize(self, *args): #cannot find CLR method
        """ ImplInitialize(self: RegSvrSmoObject, fields: Array[str], orderby: Array[OrderBy]) -> bool """
        ...

    def Initialize(self) -> bool:
        """ Initialize(self: RegSvrSmoObject) -> bool """
        ...

    def IsObjectInitialized(self, *args): #cannot find CLR method
        """ IsObjectInitialized(self: RegSvrSmoObject) -> bool """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: RegSvrSmoObject) """
        ...

    def SetParentImpl(self, *args): #cannot find CLR method
        """ SetParentImpl(self: RegSvrSmoObject, newParent: RegSvrSmoObject) """
        ...

    def Trace(self, *args): #cannot find CLR method
        """ Trace(traceText: str) """
        ...

    def UpdateObjectState(self, *args): #cannot find CLR method
        """ UpdateObjectState(self: RegSvrSmoObject) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, parentColl: RegSvrCollectionBase, name: str)
        __new__(cls: type)
        """
        ...


class RegisteredServer(IDroppable, IAlterable, ICreatable, RegSvrSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """
    RegisteredServer()
    RegisteredServer(serverGroup: ServerGroup, name: str)
    RegisteredServer(name: str)
    RegisteredServer(regServers: RegisteredServerCollection, name: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: RegisteredServer) -> str
        Set: Description(self: RegisteredServer) = value
        """
        ...

    @property
    def Login(self) -> str:
        """
        Get: Login(self: RegisteredServer) -> str
        Set: Login(self: RegisteredServer) = value
        """
        ...

    @property
    def LoginSecure(self) -> bool:
        """
        Get: LoginSecure(self: RegisteredServer) -> bool
        Set: LoginSecure(self: RegisteredServer) = value
        """
        ...

    @property
    def Parent(self) -> ServerGroup:
        """
        Get: Parent(self: RegisteredServer) -> ServerGroup
        Set: Parent(self: RegisteredServer) = value
        """
        ...

    @property
    def SecurePassword(self) -> SecureString:
        """
        Get: SecurePassword(self: RegisteredServer) -> SecureString
        Set: SecurePassword(self: RegisteredServer) = value
        """
        ...

    @property
    def ServerInstance(self) -> str:
        """
        Get: ServerInstance(self: RegisteredServer) -> str
        Set: ServerInstance(self: RegisteredServer) = value
        """
        ...


    def GetSmoObject(self, urn:Urn) -> RegSvrSmoObject:
        """ GetSmoObject(self: RegisteredServer, urn: Urn) -> RegSvrSmoObject """
        ...


class RegSvrCollectionBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: RegSvrCollectionBase) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: RegSvrCollectionBase) -> object """
        ...


    initialized = ...
    innerColl = ...


class RegisteredServerCollection(RegSvrCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServerGroup:
        """ Get: Parent(self: RegisteredServerCollection) -> ServerGroup """
        ...


    def Add(self, registeredServer:RegisteredServer): # -> 
        """ Add(self: RegisteredServerCollection, registeredServer: RegisteredServer) """
        ...

    def Contains(self, key:str) -> bool:
        """ Contains(self: RegisteredServerCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: RegisteredServerCollection) -> IEnumerator """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: RegisteredServerCollection, key: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServerGroupBase(IDroppable, IAlterable, ICreatable, RegSvrSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def RegisteredServers(self) -> RegisteredServerCollection:
        """ Get: RegisteredServers(self: ServerGroupBase) -> RegisteredServerCollection """
        ...

    @property
    def ServerGroups(self) -> ServerGroupCollection:
        """ Get: ServerGroups(self: ServerGroupBase) -> ServerGroupCollection """
        ...


    def ClearCollections(self, *args): #cannot find CLR method
        """ ClearCollections(self: ServerGroupBase) """
        ...

    def GetSmoObject(self, urn:Urn) -> RegSvrSmoObject:
        """ GetSmoObject(self: ServerGroupBase, urn: Urn) -> RegSvrSmoObject """
        ...


class ServerGroup(ServerGroupBase): # skipped bases: <type 'ICreatable'>, <type 'ISfcValidate'>, <type 'IAlterable'>, <type 'IDroppable'>, <type 'object'>
    """
    ServerGroup()
    ServerGroup(serverGroup: ServerGroup, name: str)
    ServerGroup(name: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ServerGroup) -> str
        Set: Description(self: ServerGroup) = value
        """
        ...

    @property
    def Parent(self) -> ServerGroup:
        """
        Get: Parent(self: ServerGroup) -> ServerGroup
        Set: Parent(self: ServerGroup) = value
        """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ServerGroup) -> str """
        ...

    @property
    def ServerType(self) -> Guid:
        """ Get: ServerType(self: ServerGroup) -> Guid """
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: ServerGroup) -> Urn """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serverGroup: ServerGroup, name: str)
        __new__(cls: type, name: str)
        """
        ...


class ServerGroupCollection(RegSvrCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ServerGroup:
        """ Get: Parent(self: ServerGroupCollection) -> ServerGroup """
        ...


    def Add(self, registeredServer:ServerGroup): # -> 
        """ Add(self: ServerGroupCollection, registeredServer: ServerGroup) """
        ...

    def Contains(self, key:str) -> bool:
        """ Contains(self: ServerGroupCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServerGroupCollection) -> IEnumerator """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: ServerGroupCollection, key: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


