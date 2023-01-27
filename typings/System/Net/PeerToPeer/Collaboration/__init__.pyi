# encoding: utf-8
# module System.Net.PeerToPeer.Collaboration calls itself Collaboration
# from System.Net, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Enum, EventArgs, Guid, IDisposable, IEquatable

from System.ComponentModel import (AsyncCompletedEventArgs, 
    ISynchronizeInvoke)

from System.Net import IPEndPoint

from System.Net.Mail import MailAddress

from System.Net.PeerToPeer import PeerName

from System.Runtime.Serialization import ISerializable

from System.Security import CodeAccessPermission, IPermission

from System.Security.Cryptography.X509Certificates import X509Certificate2

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ApplicationChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerApplication(self) -> PeerApplication:
        """ Get: PeerApplication(self: ApplicationChangedEventArgs) -> PeerApplication """
        ...

    @property
    def PeerChangeType(self) -> PeerChangeType:
        """ Get: PeerChangeType(self: ApplicationChangedEventArgs) -> PeerChangeType """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: ApplicationChangedEventArgs) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: ApplicationChangedEventArgs) -> PeerEndPoint """
        ...



class ContactManager(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocalContact(self) -> PeerContact:
        """ Get: LocalContact() -> PeerContact """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: ContactManager) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: ContactManager) = value
        """
        ...


    def AddContact(self, peerContact:PeerContact): # -> 
        """ AddContact(self: ContactManager, peerContact: PeerContact) """
        ...

    def CreateContact(self, peerNearMe:PeerNearMe) -> PeerContact:
        """ CreateContact(self: ContactManager, peerNearMe: PeerNearMe) -> PeerContact """
        ...

    def CreateContactAsync(self, peerNearMe:PeerNearMe, userToken:object): # -> 
        """ CreateContactAsync(self: ContactManager, peerNearMe: PeerNearMe, userToken: object) """
        ...

    def DeleteContact(self, *__args:PeerContact): # -> 
        """ DeleteContact(self: ContactManager, peerContact: PeerContact)DeleteContact(self: ContactManager, peerName: PeerName) """
        ...

    def GetContact(self, peerName:PeerName) -> PeerContact:
        """ GetContact(self: ContactManager, peerName: PeerName) -> PeerContact """
        ...

    def GetContacts(self) -> PeerContactCollection:
        """ GetContacts(self: ContactManager) -> PeerContactCollection """
        ...

    def UpdateContact(self, peerContact:PeerContact): # -> 
        """ UpdateContact(self: ContactManager, peerContact: PeerContact) """
        ...

    ApplicationChanged = ...
    CreateContactCompleted = ...
    NameChanged = ...
    ObjectChanged = ...
    PresenceChanged = ...
    SubscriptionListChanged = ...


class CreateContactCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: CreateContactCompletedEventArgs) -> PeerContact """
        ...



class InviteCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InviteResponse(self) -> PeerInvitationResponse:
        """ Get: InviteResponse(self: InviteCompletedEventArgs) -> PeerInvitationResponse """
        ...



class NameChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NameChangedEventArgs) -> str """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: NameChangedEventArgs) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: NameChangedEventArgs) -> PeerEndPoint """
        ...



class ObjectChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerChangeType(self) -> PeerChangeType:
        """ Get: PeerChangeType(self: ObjectChangedEventArgs) -> PeerChangeType """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: ObjectChangedEventArgs) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: ObjectChangedEventArgs) -> PeerEndPoint """
        ...

    @property
    def PeerObject(self) -> PeerObject:
        """ Get: PeerObject(self: ObjectChangedEventArgs) -> PeerObject """
        ...



class Peer(IDisposable, ISerializable, IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsOnline(self) -> bool:
        """ Get: IsOnline(self: Peer) -> bool """
        ...

    @property
    def PeerEndPoints(self) -> PeerEndPointCollection:
        """ Get: PeerEndPoints(self: Peer) -> PeerEndPointCollection """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: Peer) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: Peer) = value
        """
        ...


    def GetObjects(self, objectId:Guid = ...) -> PeerObjectCollection:
        """
        GetObjects(self: Peer) -> PeerObjectCollection
        GetObjects(self: Peer, objectId: Guid) -> PeerObjectCollection
        """
        ...

    def GetPresenceInfo(self, peerEndPoint:PeerEndPoint) -> PeerPresenceInfo:
        """ GetPresenceInfo(self: Peer, peerEndPoint: PeerEndPoint) -> PeerPresenceInfo """
        ...

    def Invite(self, applicationToInvite:PeerApplication = ..., message:str = ..., invitationData:Array = ...) -> PeerInvitationResponse:
        """
        Invite(self: Peer) -> PeerInvitationResponse
        Invite(self: Peer, applicationToInvite: PeerApplication, message: str, invitationData: Array[Byte]) -> PeerInvitationResponse
        """
        ...

    def InviteAsync(self, *__args:object): # -> 
        """ InviteAsync(self: Peer, userToken: object)InviteAsync(self: Peer, applicationToInvite: PeerApplication, message: str, invitationData: Array[Byte], userToken: object) """
        ...

    def InviteAsyncCancel(self, userToken:object): # -> 
        """ InviteAsyncCancel(self: Peer, userToken: object) """
        ...

    def OnInviteCompleted(self, *args): #cannot find CLR method
        """ OnInviteCompleted(self: Peer, e: InviteCompletedEventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Peer) -> str """
        ...

    InviteCompleted = ...


class PeerApplication(IDisposable, ISerializable, IEquatable): # skipped bases: <type 'object'>
    """
    PeerApplication()
    PeerApplication(id: Guid, description: str, data: Array[Byte], path: str, commandLineArgs: str, peerScope: PeerScope)
    """
    @property
    def CommandLineArgs(self) -> str:
        """
        Get: CommandLineArgs(self: PeerApplication) -> str
        Set: CommandLineArgs(self: PeerApplication) = value
        """
        ...

    @property
    def Data(self) -> Array:
        """
        Get: Data(self: PeerApplication) -> Array[Byte]
        Set: Data(self: PeerApplication) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PeerApplication) -> str
        Set: Description(self: PeerApplication) = value
        """
        ...

    @property
    def Id(self) -> Guid:
        """
        Get: Id(self: PeerApplication) -> Guid
        Set: Id(self: PeerApplication) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: PeerApplication) -> str
        Set: Path(self: PeerApplication) = value
        """
        ...

    @property
    def PeerScope(self) -> PeerScope:
        """
        Get: PeerScope(self: PeerApplication) -> PeerScope
        Set: PeerScope(self: PeerApplication) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: PeerApplication) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: PeerApplication) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerApplication) -> int """
        ...

    def OnApplicationChanged(self, *args): #cannot find CLR method
        """ OnApplicationChanged(self: PeerApplication, appChangedArgs: ApplicationChangedEventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PeerApplication) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    ApplicationChanged = ...


class PeerApplicationCollection(Collection): # skipped bases: <type 'ICollection[PeerApplication]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[PeerApplication]'>, <type 'IReadOnlyCollection[PeerApplication]'>, <type 'IList[PeerApplication]'>, <type 'IReadOnlyList[PeerApplication]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PeerApplicationCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PeerApplicationLaunchInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Data(self) -> Array:
        """ Get: Data(self: PeerApplicationLaunchInfo) -> Array[Byte] """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: PeerApplicationLaunchInfo) -> str """
        ...

    @property
    def PeerApplication(self) -> PeerApplication:
        """ Get: PeerApplication(self: PeerApplicationLaunchInfo) -> PeerApplication """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: PeerApplicationLaunchInfo) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: PeerApplicationLaunchInfo) -> PeerEndPoint """
        ...



class PeerApplicationRegistrationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerApplicationRegistrationType, values: AllUsers (1), CurrentUser (0) """
    AllUsers: PeerApplicationRegistrationType = ...
    CurrentUser: PeerApplicationRegistrationType = ...
    value__ = ...


class PeerChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerChangeType, values: Added (0), Deleted (1), Updated (2) """
    Added: PeerChangeType = ...
    Deleted: PeerChangeType = ...
    Updated: PeerChangeType = ...
    value__ = ...


class PeerCollaboration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationLaunchInfo(self) -> PeerApplicationLaunchInfo:
        """ Get: ApplicationLaunchInfo() -> PeerApplicationLaunchInfo """
        ...

    @property
    def ContactManager(self) -> ContactManager:
        """ Get: ContactManager() -> ContactManager """
        ...

    @property
    def LocalEndPointName(self) -> str:
        """
        Get: LocalEndPointName() -> str
        Set: LocalEndPointName() = value
        """
        ...

    @property
    def LocalPresenceInfo(self) -> PeerPresenceInfo:
        """
        Get: LocalPresenceInfo() -> PeerPresenceInfo
        Set: LocalPresenceInfo() = value
        """
        ...

    @property
    def SignInScope(self) -> PeerScope:
        """ Get: SignInScope() -> PeerScope """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject() -> ISynchronizeInvoke
        Set: SynchronizingObject() = value
        """
        ...


    @staticmethod
    def DeleteObject(peerObject:PeerObject): # -> 
        """ DeleteObject(peerObject: PeerObject) """
        ...

    @staticmethod
    def GetLocalRegisteredApplications(type=None) -> PeerApplicationCollection:
        """
        GetLocalRegisteredApplications() -> PeerApplicationCollection
        GetLocalRegisteredApplications(type: PeerApplicationRegistrationType) -> PeerApplicationCollection
        """
        ...

    @staticmethod
    def GetLocalSetObjects() -> PeerObjectCollection:
        """ GetLocalSetObjects() -> PeerObjectCollection """
        ...

    @staticmethod
    def GetPeersNearMe() -> PeerNearMeCollection:
        """ GetPeersNearMe() -> PeerNearMeCollection """
        ...

    @staticmethod
    def RegisterApplication(application:PeerApplication, type:PeerApplicationRegistrationType): # -> 
        """ RegisterApplication(application: PeerApplication, type: PeerApplicationRegistrationType) """
        ...

    @staticmethod
    def SetObject(peerObject:PeerObject): # -> 
        """ SetObject(peerObject: PeerObject) """
        ...

    @staticmethod
    def SignIn(peerScope:PeerScope): # -> 
        """ SignIn(peerScope: PeerScope) """
        ...

    @staticmethod
    def SignOut(peerScope:PeerScope): # -> 
        """ SignOut(peerScope: PeerScope) """
        ...

    @staticmethod
    def UnregisterApplication(application:PeerApplication, type:PeerApplicationRegistrationType): # -> 
        """ UnregisterApplication(application: PeerApplication, type: PeerApplicationRegistrationType) """
        ...

    LocalApplicationChanged = ...
    LocalNameChanged = ...
    LocalObjectChanged = ...
    LocalPresenceChanged = ...
    __all__: list = ...


class PeerCollaborationPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ PeerCollaborationPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class PeerCollaborationPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PeerCollaborationPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PeerCollaborationPermissionAttribute) -> IPermission """
        ...


class PeerContact(Peer, IEquatable): # skipped bases: <type 'IDisposable'>, <type 'IEquatable[Peer]'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Credentials(self) -> X509Certificate2:
        """ Get: Credentials(self: PeerContact) -> X509Certificate2 """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: PeerContact) -> str
        Set: DisplayName(self: PeerContact) = value
        """
        ...

    @property
    def EmailAddress(self) -> MailAddress:
        """
        Get: EmailAddress(self: PeerContact) -> MailAddress
        Set: EmailAddress(self: PeerContact) = value
        """
        ...

    @property
    def IsSubscribed(self) -> bool:
        """ Get: IsSubscribed(self: PeerContact) -> bool """
        ...

    @property
    def Nickname(self) -> str:
        """
        Get: Nickname(self: PeerContact) -> str
        Set: Nickname(self: PeerContact) = value
        """
        ...

    @property
    def PeerName(self) -> PeerName:
        """ Get: PeerName(self: PeerContact) -> PeerName """
        ...

    @property
    def SubscribeAllowed(self) -> SubscriptionType:
        """
        Get: SubscribeAllowed(self: PeerContact) -> SubscriptionType
        Set: SubscribeAllowed(self: PeerContact) = value
        """
        ...


    @staticmethod
    def FromXml(peerContactXml:str) -> PeerContact:
        """ FromXml(peerContactXml: str) -> PeerContact """
        ...

    def GetApplications(self, *__args:Guid) -> PeerApplicationCollection:
        """
        GetApplications(self: PeerContact) -> PeerApplicationCollection
        GetApplications(self: PeerContact, applicationId: Guid) -> PeerApplicationCollection
        GetApplications(self: PeerContact, peerEndPoint: PeerEndPoint) -> PeerApplicationCollection
        GetApplications(self: PeerContact, peerEndPoint: PeerEndPoint, applicationId: Guid) -> PeerApplicationCollection
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerContact) -> int """
        ...

    def OnApplicationChanged(self, *args): #cannot find CLR method
        """ OnApplicationChanged(self: PeerContact, appChangedArgs: ApplicationChangedEventArgs) """
        ...

    def OnObjectChanged(self, *args): #cannot find CLR method
        """ OnObjectChanged(self: PeerContact, objChangedArgs: ObjectChangedEventArgs) """
        ...

    def OnPresenceChanged(self, *args): #cannot find CLR method
        """ OnPresenceChanged(self: PeerContact, presenceChangedArgs: PresenceChangedEventArgs) """
        ...

    def OnSubscribeCompleted(self, *args): #cannot find CLR method
        """ OnSubscribeCompleted(self: PeerContact, e: SubscribeCompletedEventArgs) """
        ...

    def Subscribe(self): # -> 
        """ Subscribe(self: PeerContact) """
        ...

    def SubscribeAsync(self, userToken:object): # -> 
        """ SubscribeAsync(self: PeerContact, userToken: object) """
        ...

    def ToXml(self) -> str:
        """ ToXml(self: PeerContact) -> str """
        ...

    def Unsubscribe(self): # -> 
        """ Unsubscribe(self: PeerContact) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    ApplicationChanged = ...
    ObjectChanged = ...
    PresenceChanged = ...
    SubscribeCompleted = ...


class PeerContactCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[PeerContact]'>, <type 'IList[PeerContact]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[PeerContact]'>, <type 'IEnumerable[PeerContact]'>, <type 'ICollection[PeerContact]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PeerContactCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PeerEndPoint(IDisposable, ISerializable, IEquatable): # skipped bases: <type 'object'>
    """
    PeerEndPoint()
    PeerEndPoint(endPoint: IPEndPoint)
    PeerEndPoint(endPoint: IPEndPoint, endPointName: str)
    """
    @property
    def EndPoint(self) -> IPEndPoint:
        """
        Get: EndPoint(self: PeerEndPoint) -> IPEndPoint
        Set: EndPoint(self: PeerEndPoint) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PeerEndPoint) -> str
        Set: Name(self: PeerEndPoint) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: PeerEndPoint) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: PeerEndPoint) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerEndPoint) -> int """
        ...

    def OnNameChanged(self, *args): #cannot find CLR method
        """ OnNameChanged(self: PeerEndPoint, nameChangedArgs: NameChangedEventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PeerEndPoint) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    NameChanged = ...


class PeerEndPointCollection(Collection, IEquatable): # skipped bases: <type 'IEnumerable[PeerEndPoint]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[PeerEndPoint]'>, <type 'IReadOnlyCollection[PeerEndPoint]'>, <type 'IReadOnlyList[PeerEndPoint]'>, <type 'ICollection'>, <type 'IList[PeerEndPoint]'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PeerEndPointCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PeerInvitationResponse: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PeerInvitationResponseType(self) -> PeerInvitationResponseType:
        """ Get: PeerInvitationResponseType(self: PeerInvitationResponse) -> PeerInvitationResponseType """
        ...



class PeerInvitationResponseType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerInvitationResponseType, values: Accepted (1), Declined (0), Expired (2) """
    Accepted: PeerInvitationResponseType = ...
    Declined: PeerInvitationResponseType = ...
    Expired: PeerInvitationResponseType = ...
    value__ = ...


class PeerNearMe(Peer, IEquatable): # skipped bases: <type 'IDisposable'>, <type 'IEquatable[Peer]'>, <type 'ISerializable'>, <type 'object'>
    """ PeerNearMe() """
    @property
    def Nickname(self) -> str:
        """ Get: Nickname(self: PeerNearMe) -> str """
        ...


    def AddToContactManager(self, displayName:str = ..., nickname:str = ..., emailAddress:MailAddress = ...) -> PeerContact:
        """
        AddToContactManager(self: PeerNearMe) -> PeerContact
        AddToContactManager(self: PeerNearMe, displayName: str, nickname: str, emailAddress: MailAddress) -> PeerContact
        """
        ...

    @staticmethod
    def CreateFromPeerEndPoint(peerEndPoint:PeerEndPoint) -> PeerNearMe:
        """ CreateFromPeerEndPoint(peerEndPoint: PeerEndPoint) -> PeerNearMe """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerNearMe) -> int """
        ...

    def InternalRefreshData(self, *args): #cannot find CLR method
        """ InternalRefreshData(self: PeerNearMe, state: object) """
        ...

    def OnRefreshDataCompleted(self, *args): #cannot find CLR method
        """ OnRefreshDataCompleted(self: PeerNearMe, e: RefreshDataCompletedEventArgs) """
        ...

    def RefreshData(self): # -> 
        """ RefreshData(self: PeerNearMe) """
        ...

    def RefreshDataAsync(self, userToken:object): # -> 
        """ RefreshDataAsync(self: PeerNearMe, userToken: object) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    PeerNearMeChanged = ...
    RefreshDataCompleted = ...


class PeerNearMeChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerChangeType(self) -> PeerChangeType:
        """ Get: PeerChangeType(self: PeerNearMeChangedEventArgs) -> PeerChangeType """
        ...

    @property
    def PeerNearMe(self) -> PeerNearMe:
        """ Get: PeerNearMe(self: PeerNearMeChangedEventArgs) -> PeerNearMe """
        ...



class PeerNearMeCollection(Collection): # skipped bases: <type 'IReadOnlyList[PeerNearMe]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[PeerNearMe]'>, <type 'IEnumerable[PeerNearMe]'>, <type 'ICollection[PeerNearMe]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[PeerNearMe]'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PeerNearMeCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PeerObject(IDisposable, ISerializable, IEquatable): # skipped bases: <type 'object'>
    """
    PeerObject()
    PeerObject(Id: Guid, data: Array[Byte], peerScope: PeerScope)
    """
    @property
    def Data(self) -> Array:
        """
        Get: Data(self: PeerObject) -> Array[Byte]
        Set: Data(self: PeerObject) = value
        """
        ...

    @property
    def Id(self) -> Guid:
        """
        Get: Id(self: PeerObject) -> Guid
        Set: Id(self: PeerObject) = value
        """
        ...

    @property
    def PeerScope(self) -> PeerScope:
        """
        Get: PeerScope(self: PeerObject) -> PeerScope
        Set: PeerScope(self: PeerObject) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: PeerObject) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: PeerObject) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: PeerObject) -> int """
        ...

    def OnObjectChanged(self, *args): #cannot find CLR method
        """ OnObjectChanged(self: PeerObject, objChangedArgs: ObjectChangedEventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PeerObject) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    ObjectChanged = ...


class PeerObjectCollection(Collection): # skipped bases: <type 'ICollection[PeerObject]'>, <type 'IReadOnlyCollection[PeerObject]'>, <type 'IList[PeerObject]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[PeerObject]'>, <type 'IEnumerable[PeerObject]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PeerObjectCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PeerPresenceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    PeerPresenceInfo()
    PeerPresenceInfo(presenceStatus: PeerPresenceStatus, description: str)
    """
    @property
    def DescriptiveText(self) -> str:
        """
        Get: DescriptiveText(self: PeerPresenceInfo) -> str
        Set: DescriptiveText(self: PeerPresenceInfo) = value
        """
        ...

    @property
    def PresenceStatus(self) -> PeerPresenceStatus:
        """
        Get: PresenceStatus(self: PeerPresenceInfo) -> PeerPresenceStatus
        Set: PresenceStatus(self: PeerPresenceInfo) = value
        """
        ...



class PeerPresenceStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerPresenceStatus, values: Away (2), BeRightBack (3), Busy (5), Idle (4), Offline (0), Online (7), OnThePhone (6), OutToLunch (1) """
    Away: PeerPresenceStatus = ...
    BeRightBack: PeerPresenceStatus = ...
    Busy: PeerPresenceStatus = ...
    Idle: PeerPresenceStatus = ...
    Offline: PeerPresenceStatus = ...
    Online: PeerPresenceStatus = ...
    OnThePhone: PeerPresenceStatus = ...
    OutToLunch: PeerPresenceStatus = ...
    value__ = ...


class PeerScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerScope, values: All (3), Internet (2), NearMe (1), None (0) """
    All: PeerScope = ...
    Internet: PeerScope = ...
    NearMe: PeerScope = ...
    value__ = ...


class PresenceChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerChangeType(self) -> PeerChangeType:
        """ Get: PeerChangeType(self: PresenceChangedEventArgs) -> PeerChangeType """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: PresenceChangedEventArgs) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: PresenceChangedEventArgs) -> PeerEndPoint """
        ...

    @property
    def PeerPresenceInfo(self) -> PeerPresenceInfo:
        """ Get: PeerPresenceInfo(self: PresenceChangedEventArgs) -> PeerPresenceInfo """
        ...



class RefreshDataCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: RefreshDataCompletedEventArgs) -> PeerEndPoint """
        ...



class SubscribeCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: SubscribeCompletedEventArgs) -> PeerContact """
        ...

    @property
    def PeerNearMe(self) -> PeerNearMe:
        """ Get: PeerNearMe(self: SubscribeCompletedEventArgs) -> PeerNearMe """
        ...



class SubscriptionListChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PeerChangeType(self) -> PeerChangeType:
        """ Get: PeerChangeType(self: SubscriptionListChangedEventArgs) -> PeerChangeType """
        ...

    @property
    def PeerContact(self) -> PeerContact:
        """ Get: PeerContact(self: SubscriptionListChangedEventArgs) -> PeerContact """
        ...

    @property
    def PeerEndPoint(self) -> PeerEndPoint:
        """ Get: PeerEndPoint(self: SubscriptionListChangedEventArgs) -> PeerEndPoint """
        ...



class SubscriptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SubscriptionType, values: Allowed (1), Blocked (0) """
    Allowed: SubscriptionType = ...
    Blocked: SubscriptionType = ...
    value__ = ...


