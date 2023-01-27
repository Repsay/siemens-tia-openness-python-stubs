# encoding: utf-8
# module System.Net.PeerToPeer calls itself PeerToPeer
# from System.Net, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Enum, IDisposable, IEquatable

from System.ComponentModel import (AsyncCompletedEventArgs, 
    ProgressChangedEventArgs)

from System.Net import IPEndPointCollection

from System.Runtime.Serialization import ISerializable

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Cloud(ISerializable, IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Global(self) -> Cloud:
        """ Get: Global() -> Cloud """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Cloud) -> str """
        ...

    @property
    def Scope(self) -> PnrpScope:
        """ Get: Scope(self: Cloud) -> PnrpScope """
        ...

    @property
    def ScopeId(self) -> int:
        """ Get: ScopeId(self: Cloud) -> int """
        ...


    @staticmethod
    def GetAvailableClouds() -> CloudCollection:
        """ GetAvailableClouds() -> CloudCollection """
        ...

    @staticmethod
    def GetCloudByName(cloudName:str) -> Cloud:
        """ GetCloudByName(cloudName: str) -> Cloud """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Cloud) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Cloud) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    AllLinkLocal: Cloud = ...
    Available: Cloud = ...


class CloudCollection(Collection): # skipped bases: <type 'IReadOnlyList[Cloud]'>, <type 'IReadOnlyCollection[Cloud]'>, <type 'ICollection[Cloud]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[Cloud]'>, <type 'ICollection'>, <type 'IEnumerable[Cloud]'>, <type 'object'>
    """ CloudCollection() """
    pass

class PeerName(ISerializable, IEquatable): # skipped bases: <type 'object'>
    """
    PeerName(remotePeerName: str)
    PeerName(classifier: str, peerNameType: PeerNameType)
    """
    @property
    def Authority(self) -> str:
        """ Get: Authority(self: PeerName) -> str """
        ...

    @property
    def Classifier(self) -> str:
        """ Get: Classifier(self: PeerName) -> str """
        ...

    @property
    def IsSecured(self) -> bool:
        """ Get: IsSecured(self: PeerName) -> bool """
        ...

    @property
    def PeerHostName(self) -> str:
        """ Get: PeerHostName(self: PeerName) -> str """
        ...


    @staticmethod
    def CreateFromPeerHostName(peerHostName:str) -> PeerName:
        """ CreateFromPeerHostName(peerHostName: str) -> PeerName """
        ...

    @staticmethod
    def CreateRelativePeerName(peerName:PeerName, classifier:str) -> PeerName:
        """ CreateRelativePeerName(peerName: PeerName, classifier: str) -> PeerName """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: PeerName) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PeerNameRecord(ISerializable): # skipped bases: <type 'object'>
    """ PeerNameRecord() """
    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: PeerNameRecord) -> str
        Set: Comment(self: PeerNameRecord) = value
        """
        ...

    @property
    def Data(self) -> Array:
        """
        Get: Data(self: PeerNameRecord) -> Array[Byte]
        Set: Data(self: PeerNameRecord) = value
        """
        ...

    @property
    def EndPointCollection(self) -> IPEndPointCollection:
        """ Get: EndPointCollection(self: PeerNameRecord) -> IPEndPointCollection """
        ...

    @property
    def PeerName(self) -> PeerName:
        """
        Get: PeerName(self: PeerNameRecord) -> PeerName
        Set: PeerName(self: PeerNameRecord) = value
        """
        ...



class PeerNameRecordCollection(Collection): # skipped bases: <type 'ICollection[PeerNameRecord]'>, <type 'IReadOnlyList[PeerNameRecord]'>, <type 'IEnumerable[PeerNameRecord]'>, <type 'IList[PeerNameRecord]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[PeerNameRecord]'>, <type 'ICollection'>, <type 'object'>
    """ PeerNameRecordCollection() """
    pass

class PeerNameRegistration(IDisposable, ISerializable): # skipped bases: <type 'object'>
    """
    PeerNameRegistration()
    PeerNameRegistration(name: PeerName, port: int)
    PeerNameRegistration(name: PeerName, port: int, cloud: Cloud)
    """
    @property
    def Cloud(self) -> Cloud:
        """
        Get: Cloud(self: PeerNameRegistration) -> Cloud
        Set: Cloud(self: PeerNameRegistration) = value
        """
        ...

    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: PeerNameRegistration) -> str
        Set: Comment(self: PeerNameRegistration) = value
        """
        ...

    @property
    def Data(self) -> Array:
        """
        Get: Data(self: PeerNameRegistration) -> Array[Byte]
        Set: Data(self: PeerNameRegistration) = value
        """
        ...

    @property
    def EndPointCollection(self) -> IPEndPointCollection:
        """ Get: EndPointCollection(self: PeerNameRegistration) -> IPEndPointCollection """
        ...

    @property
    def PeerName(self) -> PeerName:
        """
        Get: PeerName(self: PeerNameRegistration) -> PeerName
        Set: PeerName(self: PeerNameRegistration) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: PeerNameRegistration) -> int
        Set: Port(self: PeerNameRegistration) = value
        """
        ...

    @property
    def UseAutoEndPointSelection(self) -> bool:
        """
        Get: UseAutoEndPointSelection(self: PeerNameRegistration) -> bool
        Set: UseAutoEndPointSelection(self: PeerNameRegistration) = value
        """
        ...


    def IsRegistered(self) -> bool:
        """ IsRegistered(self: PeerNameRegistration) -> bool """
        ...

    def Start(self): # -> 
        """ Start(self: PeerNameRegistration) """
        ...

    def Stop(self): # -> 
        """ Stop(self: PeerNameRegistration) """
        ...

    def Update(self): # -> 
        """ Update(self: PeerNameRegistration) """
        ...


class PeerNameResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerNameResolver() """
    def OnResolveCompleted(self, *args): #cannot find CLR method
        """ OnResolveCompleted(self: PeerNameResolver, e: ResolveCompletedEventArgs) """
        ...

    def OnResolveProgressChanged(self, *args): #cannot find CLR method
        """ OnResolveProgressChanged(self: PeerNameResolver, e: ResolveProgressChangedEventArgs) """
        ...

    def Resolve(self, peerName:PeerName, *__args:Cloud) -> PeerNameRecordCollection:
        """
        Resolve(self: PeerNameResolver, peerName: PeerName) -> PeerNameRecordCollection
        Resolve(self: PeerNameResolver, peerName: PeerName, cloud: Cloud) -> PeerNameRecordCollection
        Resolve(self: PeerNameResolver, peerName: PeerName, maxRecords: int) -> PeerNameRecordCollection
        Resolve(self: PeerNameResolver, peerName: PeerName, cloud: Cloud, maxRecords: int) -> PeerNameRecordCollection
        """
        ...

    def ResolveAsync(self, peerName:PeerName, *__args:object): # -> 
        """ ResolveAsync(self: PeerNameResolver, peerName: PeerName, userState: object)ResolveAsync(self: PeerNameResolver, peerName: PeerName, cloud: Cloud, userState: object)ResolveAsync(self: PeerNameResolver, peerName: PeerName, maxRecords: int, userState: object)ResolveAsync(self: PeerNameResolver, peerName: PeerName, cloud: Cloud, maxRecords: int, userState: object) """
        ...

    def ResolveAsyncCancel(self, userState:object): # -> 
        """ ResolveAsyncCancel(self: PeerNameResolver, userState: object) """
        ...

    ResolveCompleted = ...
    ResolveProgressChanged = ...


class PeerNameType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerNameType, values: Secured (0), Unsecured (1) """
    Secured: PeerNameType = ...
    Unsecured: PeerNameType = ...
    value__ = ...


class PeerToPeerException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PeerToPeerException()
    PeerToPeerException(message: str)
    PeerToPeerException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PnrpPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ PnrpPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class PnrpPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PnrpPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PnrpPermissionAttribute) -> IPermission """
        ...


class PnrpScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PnrpScope, values: All (0), Global (1), LinkLocal (3), SiteLocal (2) """
    All: PnrpScope = ...
    Global: PnrpScope = ...
    LinkLocal: PnrpScope = ...
    SiteLocal: PnrpScope = ...
    value__ = ...


class ResolveCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ ResolveCompletedEventArgs(peerNameRecordCollection: PeerNameRecordCollection, error: Exception, canceled: bool, userToken: object) """
    @property
    def PeerNameRecordCollection(self) -> PeerNameRecordCollection:
        """ Get: PeerNameRecordCollection(self: ResolveCompletedEventArgs) -> PeerNameRecordCollection """
        ...



class ResolveProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ ResolveProgressChangedEventArgs(peerNameRecord: PeerNameRecord, userToken: object) """
    @property
    def PeerNameRecord(self) -> PeerNameRecord:
        """ Get: PeerNameRecord(self: ResolveProgressChangedEventArgs) -> PeerNameRecord """
        ...



# variables with complex values

