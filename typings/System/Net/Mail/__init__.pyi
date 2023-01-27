# encoding: utf-8
# module System.Net.Mail calls itself Mail
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, AsyncCallback, Enum, IAsyncResult, IDisposable, 
    MulticastDelegate, Uri)

from System.Collections.Specialized import NameValueCollection

from System.ComponentModel import AsyncCompletedEventArgs

from System.IO import Stream

from System.Net import ICredentialsByHost, ServicePoint

from System.Net.Mime import (ContentDisposition, ContentType, 
    TransferEncoding)

from System.Security import CodeAccessPermission, IPermission

from System.Security.Cryptography.X509Certificates import (
    X509CertificateCollection)

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Text import Encoding

from System.Threading.Tasks import Task

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AttachmentBase(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentId(self) -> str:
        """
        Get: ContentId(self: AttachmentBase) -> str
        Set: ContentId(self: AttachmentBase) = value
        """
        ...

    @property
    def ContentStream(self) -> Stream:
        """ Get: ContentStream(self: AttachmentBase) -> Stream """
        ...

    @property
    def ContentType(self) -> ContentType:
        """
        Get: ContentType(self: AttachmentBase) -> ContentType
        Set: ContentType(self: AttachmentBase) = value
        """
        ...

    @property
    def TransferEncoding(self) -> TransferEncoding:
        """
        Get: TransferEncoding(self: AttachmentBase) -> TransferEncoding
        Set: TransferEncoding(self: AttachmentBase) = value
        """
        ...



class AlternateView(AttachmentBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    AlternateView(fileName: str)
    AlternateView(fileName: str, mediaType: str)
    AlternateView(fileName: str, contentType: ContentType)
    AlternateView(contentStream: Stream)
    AlternateView(contentStream: Stream, mediaType: str)
    AlternateView(contentStream: Stream, contentType: ContentType)
    """
    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: AlternateView) -> Uri
        Set: BaseUri(self: AlternateView) = value
        """
        ...

    @property
    def LinkedResources(self) -> LinkedResourceCollection:
        """ Get: LinkedResources(self: AlternateView) -> LinkedResourceCollection """
        ...


    @staticmethod
    def CreateAlternateViewFromString(content:str, *__args:ContentType) -> AlternateView:
        """
        CreateAlternateViewFromString(content: str) -> AlternateView
        CreateAlternateViewFromString(content: str, contentEncoding: Encoding, mediaType: str) -> AlternateView
        CreateAlternateViewFromString(content: str, contentType: ContentType) -> AlternateView
        """
        ...


class AlternateViewCollection(IDisposable, Collection): # skipped bases: <type 'IEnumerable[AlternateView]'>, <type 'ICollection[AlternateView]'>, <type 'IReadOnlyCollection[AlternateView]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[AlternateView]'>, <type 'IReadOnlyList[AlternateView]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class Attachment(AttachmentBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    Attachment(fileName: str)
    Attachment(fileName: str, mediaType: str)
    Attachment(fileName: str, contentType: ContentType)
    Attachment(contentStream: Stream, name: str)
    Attachment(contentStream: Stream, name: str, mediaType: str)
    Attachment(contentStream: Stream, contentType: ContentType)
    """
    @property
    def ContentDisposition(self) -> ContentDisposition:
        """ Get: ContentDisposition(self: Attachment) -> ContentDisposition """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Attachment) -> str
        Set: Name(self: Attachment) = value
        """
        ...

    @property
    def NameEncoding(self) -> Encoding:
        """
        Get: NameEncoding(self: Attachment) -> Encoding
        Set: NameEncoding(self: Attachment) = value
        """
        ...


    @staticmethod
    def CreateAttachmentFromString(content:str, *__args:str) -> Attachment:
        """
        CreateAttachmentFromString(content: str, name: str) -> Attachment
        CreateAttachmentFromString(content: str, name: str, contentEncoding: Encoding, mediaType: str) -> Attachment
        CreateAttachmentFromString(content: str, contentType: ContentType) -> Attachment
        """
        ...


class AttachmentCollection(IDisposable, Collection): # skipped bases: <type 'IReadOnlyCollection[Attachment]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[Attachment]'>, <type 'IList[Attachment]'>, <type 'IEnumerable[Attachment]'>, <type 'ICollection'>, <type 'IReadOnlyList[Attachment]'>, <type 'object'>
    """ no doc """
    pass

class DeliveryNotificationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DeliveryNotificationOptions, values: Delay (4), Never (134217728), None (0), OnFailure (2), OnSuccess (1) """
    Delay: DeliveryNotificationOptions = ...
    Never: DeliveryNotificationOptions = ...
    OnFailure: DeliveryNotificationOptions = ...
    OnSuccess: DeliveryNotificationOptions = ...
    value__ = ...


class LinkedResource(AttachmentBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    LinkedResource(fileName: str)
    LinkedResource(fileName: str, mediaType: str)
    LinkedResource(fileName: str, contentType: ContentType)
    LinkedResource(contentStream: Stream)
    LinkedResource(contentStream: Stream, mediaType: str)
    LinkedResource(contentStream: Stream, contentType: ContentType)
    """
    @property
    def ContentLink(self) -> Uri:
        """
        Get: ContentLink(self: LinkedResource) -> Uri
        Set: ContentLink(self: LinkedResource) = value
        """
        ...


    @staticmethod
    def CreateLinkedResourceFromString(content:str, *__args:ContentType) -> LinkedResource:
        """
        CreateLinkedResourceFromString(content: str) -> LinkedResource
        CreateLinkedResourceFromString(content: str, contentEncoding: Encoding, mediaType: str) -> LinkedResource
        CreateLinkedResourceFromString(content: str, contentType: ContentType) -> LinkedResource
        """
        ...


class LinkedResourceCollection(IDisposable, Collection): # skipped bases: <type 'IReadOnlyCollection[LinkedResource]'>, <type 'IEnumerable[LinkedResource]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[LinkedResource]'>, <type 'IList[LinkedResource]'>, <type 'ICollection'>, <type 'IReadOnlyList[LinkedResource]'>, <type 'object'>
    """ no doc """
    pass

class MailAddress: # skipped bases: <type 'object'>, <type 'object'>
    """
    MailAddress(address: str)
    MailAddress(address: str, displayName: str)
    MailAddress(address: str, displayName: str, displayNameEncoding: Encoding)
    """
    @property
    def Address(self) -> str:
        """ Get: Address(self: MailAddress) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: MailAddress) -> str """
        ...

    @property
    def Host(self) -> str:
        """ Get: Host(self: MailAddress) -> str """
        ...

    @property
    def User(self) -> str:
        """ Get: User(self: MailAddress) -> str """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: MailAddress, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MailAddress) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MailAddress) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MailAddressCollection(Collection): # skipped bases: <type 'IEnumerable[MailAddress]'>, <type 'ICollection[MailAddress]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[MailAddress]'>, <type 'IReadOnlyList[MailAddress]'>, <type 'IReadOnlyCollection[MailAddress]'>, <type 'ICollection'>, <type 'object'>
    """ MailAddressCollection() """
    def ToString(self) -> str:
        """ ToString(self: MailAddressCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class MailMessage(IDisposable): # skipped bases: <type 'object'>
    """
    MailMessage()
    MailMessage(from: str, to: str)
    MailMessage(from: str, to: str, subject: str, body: str)
    MailMessage(from: MailAddress, to: MailAddress)
    """
    @property
    def AlternateViews(self) -> AlternateViewCollection:
        """ Get: AlternateViews(self: MailMessage) -> AlternateViewCollection """
        ...

    @property
    def Attachments(self) -> AttachmentCollection:
        """ Get: Attachments(self: MailMessage) -> AttachmentCollection """
        ...

    @property
    def Bcc(self) -> MailAddressCollection:
        """ Get: Bcc(self: MailMessage) -> MailAddressCollection """
        ...

    @property
    def Body(self) -> str:
        """
        Get: Body(self: MailMessage) -> str
        Set: Body(self: MailMessage) = value
        """
        ...

    @property
    def BodyEncoding(self) -> Encoding:
        """
        Get: BodyEncoding(self: MailMessage) -> Encoding
        Set: BodyEncoding(self: MailMessage) = value
        """
        ...

    @property
    def BodyTransferEncoding(self) -> TransferEncoding:
        """
        Get: BodyTransferEncoding(self: MailMessage) -> TransferEncoding
        Set: BodyTransferEncoding(self: MailMessage) = value
        """
        ...

    @property
    def CC(self) -> MailAddressCollection:
        """ Get: CC(self: MailMessage) -> MailAddressCollection """
        ...

    @property
    def DeliveryNotificationOptions(self) -> DeliveryNotificationOptions:
        """
        Get: DeliveryNotificationOptions(self: MailMessage) -> DeliveryNotificationOptions
        Set: DeliveryNotificationOptions(self: MailMessage) = value
        """
        ...

    @property
    def From(self) -> MailAddress:
        """
        Get: From(self: MailMessage) -> MailAddress
        Set: From(self: MailMessage) = value
        """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: MailMessage) -> NameValueCollection """
        ...

    @property
    def HeadersEncoding(self) -> Encoding:
        """
        Get: HeadersEncoding(self: MailMessage) -> Encoding
        Set: HeadersEncoding(self: MailMessage) = value
        """
        ...

    @property
    def IsBodyHtml(self) -> bool:
        """
        Get: IsBodyHtml(self: MailMessage) -> bool
        Set: IsBodyHtml(self: MailMessage) = value
        """
        ...

    @property
    def Priority(self) -> MailPriority:
        """
        Get: Priority(self: MailMessage) -> MailPriority
        Set: Priority(self: MailMessage) = value
        """
        ...

    @property
    def ReplyTo(self) -> MailAddress:
        """
        Get: ReplyTo(self: MailMessage) -> MailAddress
        Set: ReplyTo(self: MailMessage) = value
        """
        ...

    @property
    def ReplyToList(self) -> MailAddressCollection:
        """ Get: ReplyToList(self: MailMessage) -> MailAddressCollection """
        ...

    @property
    def Sender(self) -> MailAddress:
        """
        Get: Sender(self: MailMessage) -> MailAddress
        Set: Sender(self: MailMessage) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: MailMessage) -> str
        Set: Subject(self: MailMessage) = value
        """
        ...

    @property
    def SubjectEncoding(self) -> Encoding:
        """
        Get: SubjectEncoding(self: MailMessage) -> Encoding
        Set: SubjectEncoding(self: MailMessage) = value
        """
        ...

    @property
    def To(self) -> MailAddressCollection:
        """ Get: To(self: MailMessage) -> MailAddressCollection """
        ...



class MailPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MailPriority, values: High (2), Low (1), Normal (0) """
    High: MailPriority = ...
    Low: MailPriority = ...
    Normal: MailPriority = ...
    value__ = ...


class SendCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SendCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AsyncCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SendCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AsyncCompletedEventArgs): # -> 
        """ Invoke(self: SendCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs) """
        ...


class SmtpAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SmtpAccess, values: Connect (1), ConnectToUnrestrictedPort (2), None (0) """
    Connect: SmtpAccess = ...
    ConnectToUnrestrictedPort: SmtpAccess = ...
    value__ = ...


class SmtpClient(IDisposable): # skipped bases: <type 'object'>
    """
    SmtpClient()
    SmtpClient(host: str)
    SmtpClient(host: str, port: int)
    """
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """ Get: ClientCertificates(self: SmtpClient) -> X509CertificateCollection """
        ...

    @property
    def Credentials(self) -> ICredentialsByHost:
        """
        Get: Credentials(self: SmtpClient) -> ICredentialsByHost
        Set: Credentials(self: SmtpClient) = value
        """
        ...

    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """
        Get: DeliveryFormat(self: SmtpClient) -> SmtpDeliveryFormat
        Set: DeliveryFormat(self: SmtpClient) = value
        """
        ...

    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """
        Get: DeliveryMethod(self: SmtpClient) -> SmtpDeliveryMethod
        Set: DeliveryMethod(self: SmtpClient) = value
        """
        ...

    @property
    def EnableSsl(self) -> bool:
        """
        Get: EnableSsl(self: SmtpClient) -> bool
        Set: EnableSsl(self: SmtpClient) = value
        """
        ...

    @property
    def Host(self) -> str:
        """
        Get: Host(self: SmtpClient) -> str
        Set: Host(self: SmtpClient) = value
        """
        ...

    @property
    def PickupDirectoryLocation(self) -> str:
        """
        Get: PickupDirectoryLocation(self: SmtpClient) -> str
        Set: PickupDirectoryLocation(self: SmtpClient) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: SmtpClient) -> int
        Set: Port(self: SmtpClient) = value
        """
        ...

    @property
    def ServicePoint(self) -> ServicePoint:
        """ Get: ServicePoint(self: SmtpClient) -> ServicePoint """
        ...

    @property
    def TargetName(self) -> str:
        """
        Get: TargetName(self: SmtpClient) -> str
        Set: TargetName(self: SmtpClient) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: SmtpClient) -> int
        Set: Timeout(self: SmtpClient) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: SmtpClient) -> bool
        Set: UseDefaultCredentials(self: SmtpClient) = value
        """
        ...


    def OnSendCompleted(self, *args): #cannot find CLR method
        """ OnSendCompleted(self: SmtpClient, e: AsyncCompletedEventArgs) """
        ...

    def Send(self, *__args:MailMessage): # -> 
        """ Send(self: SmtpClient, from: str, recipients: str, subject: str, body: str)Send(self: SmtpClient, message: MailMessage) """
        ...

    def SendAsync(self, *__args): # -> 
        """ SendAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str, userToken: object)SendAsync(self: SmtpClient, message: MailMessage, userToken: object) """
        ...

    def SendAsyncCancel(self): # -> 
        """ SendAsyncCancel(self: SmtpClient) """
        ...

    def SendMailAsync(self, *__args:MailMessage) -> Task:
        """
        SendMailAsync(self: SmtpClient, from: str, recipients: str, subject: str, body: str) -> Task
        SendMailAsync(self: SmtpClient, message: MailMessage) -> Task
        """
        ...

    SendCompleted = ...


class SmtpDeliveryFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SmtpDeliveryFormat, values: International (1), SevenBit (0) """
    International: SmtpDeliveryFormat = ...
    SevenBit: SmtpDeliveryFormat = ...
    value__ = ...


class SmtpDeliveryMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SmtpDeliveryMethod, values: Network (0), PickupDirectoryFromIis (2), SpecifiedPickupDirectory (1) """
    Network: SmtpDeliveryMethod = ...
    PickupDirectoryFromIis: SmtpDeliveryMethod = ...
    SpecifiedPickupDirectory: SmtpDeliveryMethod = ...
    value__ = ...


class SmtpException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SmtpException(statusCode: SmtpStatusCode)
    SmtpException(statusCode: SmtpStatusCode, message: str)
    SmtpException()
    SmtpException(message: str)
    SmtpException(message: str, innerException: Exception)
    """
    @property
    def StatusCode(self) -> SmtpStatusCode:
        """
        Get: StatusCode(self: SmtpException) -> SmtpStatusCode
        Set: StatusCode(self: SmtpException) = value
        """
        ...


    SerializeObjectState = ...


class SmtpFailedRecipientException(SmtpException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SmtpFailedRecipientException()
    SmtpFailedRecipientException(message: str)
    SmtpFailedRecipientException(message: str, innerException: Exception)
    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str)
    SmtpFailedRecipientException(statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str)
    SmtpFailedRecipientException(message: str, failedRecipient: str, innerException: Exception)
    """
    @property
    def FailedRecipient(self) -> str:
        """ Get: FailedRecipient(self: SmtpFailedRecipientException) -> str """
        ...


    SerializeObjectState = ...


class SmtpFailedRecipientsException(SmtpFailedRecipientException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SmtpFailedRecipientsException()
    SmtpFailedRecipientsException(message: str)
    SmtpFailedRecipientsException(message: str, innerException: Exception)
    SmtpFailedRecipientsException(message: str, innerExceptions: Array[SmtpFailedRecipientException])
    """
    @property
    def InnerExceptions(self) -> Array:
        """ Get: InnerExceptions(self: SmtpFailedRecipientsException) -> Array[SmtpFailedRecipientException] """
        ...


    SerializeObjectState = ...


class SmtpPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    SmtpPermission(state: PermissionState)
    SmtpPermission(unrestricted: bool)
    SmtpPermission(access: SmtpAccess)
    """
    @property
    def Access(self) -> SmtpAccess:
        """ Get: Access(self: SmtpPermission) -> SmtpAccess """
        ...


    def AddPermission(self, access:SmtpAccess): # -> 
        """ AddPermission(self: SmtpPermission, access: SmtpAccess) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, unrestricted: bool)
        __new__(cls: type, access: SmtpAccess)
        """
        ...


class SmtpPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SmtpPermissionAttribute(action: SecurityAction) """
    @property
    def Access(self) -> str:
        """
        Get: Access(self: SmtpPermissionAttribute) -> str
        Set: Access(self: SmtpPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SmtpPermissionAttribute) -> IPermission """
        ...


class SmtpStatusCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SmtpStatusCode, values: BadCommandSequence (503), CannotVerifyUserWillAttemptDelivery (252), ClientNotPermitted (454), CommandNotImplemented (502), CommandParameterNotImplemented (504), CommandUnrecognized (500), ExceededStorageAllocation (552), GeneralFailure (-1), HelpMessage (214), InsufficientStorage (452), LocalErrorInProcessing (451), MailboxBusy (450), MailboxNameNotAllowed (553), MailboxUnavailable (550), MustIssueStartTlsFirst (530), Ok (250), ServiceClosingTransmissionChannel (221), ServiceNotAvailable (421), ServiceReady (220), StartMailInput (354), SyntaxError (501), SystemStatus (211), TransactionFailed (554), UserNotLocalTryAlternatePath (551), UserNotLocalWillForward (251) """
    BadCommandSequence: SmtpStatusCode = ...
    CannotVerifyUserWillAttemptDelivery: SmtpStatusCode = ...
    ClientNotPermitted: SmtpStatusCode = ...
    CommandNotImplemented: SmtpStatusCode = ...
    CommandParameterNotImplemented: SmtpStatusCode = ...
    CommandUnrecognized: SmtpStatusCode = ...
    ExceededStorageAllocation: SmtpStatusCode = ...
    GeneralFailure: SmtpStatusCode = ...
    HelpMessage: SmtpStatusCode = ...
    InsufficientStorage: SmtpStatusCode = ...
    LocalErrorInProcessing: SmtpStatusCode = ...
    MailboxBusy: SmtpStatusCode = ...
    MailboxNameNotAllowed: SmtpStatusCode = ...
    MailboxUnavailable: SmtpStatusCode = ...
    MustIssueStartTlsFirst: SmtpStatusCode = ...
    Ok: SmtpStatusCode = ...
    ServiceClosingTransmissionChannel: SmtpStatusCode = ...
    ServiceNotAvailable: SmtpStatusCode = ...
    ServiceReady: SmtpStatusCode = ...
    StartMailInput: SmtpStatusCode = ...
    SyntaxError: SmtpStatusCode = ...
    SystemStatus: SmtpStatusCode = ...
    TransactionFailed: SmtpStatusCode = ...
    UserNotLocalTryAlternatePath: SmtpStatusCode = ...
    UserNotLocalWillForward: SmtpStatusCode = ...
    value__ = ...


