# encoding: utf-8
# module System.Messaging calls itself Messaging
# from System.Messaging, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, Enum, EventArgs, Guid, 
    IAsyncResult, ICloneable, IDisposable, Int16, Int64, IntPtr, 
    MarshalByRefObject, MulticastDelegate, TimeSpan)

from System.Collections import (CollectionBase, IDictionary, IEnumerable, 
    IEnumerator)

from System.ComponentModel import Component, ISynchronizeInvoke

from System.Configuration.Install import ComponentInstaller, UninstallAction

from System.EnterpriseServices import DescriptionAttribute

from System.IO import Stream

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Runtime.Serialization.Formatters import (FormatterAssemblyStyle, 
    FormatterTypeStyle)

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AccessControlEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    AccessControlEntry()
    AccessControlEntry(trustee: Trustee)
    AccessControlEntry(trustee: Trustee, genericAccessRights: GenericAccessRights, standardAccessRights: StandardAccessRights, entryType: AccessControlEntryType)
    """
    @property
    def CustomAccessRights(self):
        ...

    @property
    def EntryType(self) -> AccessControlEntryType:
        """
        Get: EntryType(self: AccessControlEntry) -> AccessControlEntryType
        Set: EntryType(self: AccessControlEntry) = value
        """
        ...

    @property
    def GenericAccessRights(self) -> GenericAccessRights:
        """
        Get: GenericAccessRights(self: AccessControlEntry) -> GenericAccessRights
        Set: GenericAccessRights(self: AccessControlEntry) = value
        """
        ...

    @property
    def StandardAccessRights(self) -> StandardAccessRights:
        """
        Get: StandardAccessRights(self: AccessControlEntry) -> StandardAccessRights
        Set: StandardAccessRights(self: AccessControlEntry) = value
        """
        ...

    @property
    def Trustee(self) -> Trustee:
        """
        Get: Trustee(self: AccessControlEntry) -> Trustee
        Set: Trustee(self: AccessControlEntry) = value
        """
        ...



class AccessControlEntryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AccessControlEntryType, values: Allow (1), Deny (3), Revoke (4), Set (2) """
    Allow: AccessControlEntryType = ...
    Deny: AccessControlEntryType = ...
    Revoke: AccessControlEntryType = ...
    Set: AccessControlEntryType = ...
    value__ = ...


class AccessControlList(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ AccessControlList() """
    def Add(self, entry:AccessControlEntry) -> int:
        """ Add(self: AccessControlList, entry: AccessControlEntry) -> int """
        ...

    def Contains(self, entry:AccessControlEntry) -> bool:
        """ Contains(self: AccessControlList, entry: AccessControlEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AccessControlList, array: Array[AccessControlEntry], index: int) """
        ...

    def IndexOf(self, entry:AccessControlEntry) -> int:
        """ IndexOf(self: AccessControlList, entry: AccessControlEntry) -> int """
        ...

    def Insert(self, index:int, entry:AccessControlEntry): # -> 
        """ Insert(self: AccessControlList, index: int, entry: AccessControlEntry) """
        ...

    def Remove(self, entry:AccessControlEntry): # -> 
        """ Remove(self: AccessControlList, entry: AccessControlEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class AcknowledgeTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AcknowledgeTypes, values: FullReachQueue (5), FullReceive (14), NegativeReceive (8), None (0), NotAcknowledgeReachQueue (4), NotAcknowledgeReceive (12), PositiveArrival (1), PositiveReceive (2) """
    FullReachQueue: AcknowledgeTypes = ...
    FullReceive: AcknowledgeTypes = ...
    NegativeReceive: AcknowledgeTypes = ...
    NotAcknowledgeReachQueue: AcknowledgeTypes = ...
    NotAcknowledgeReceive: AcknowledgeTypes = ...
    PositiveArrival: AcknowledgeTypes = ...
    PositiveReceive: AcknowledgeTypes = ...
    value__ = ...


class Acknowledgment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Acknowledgment, values: AccessDenied (32772), BadDestinationQueue (32768), BadEncryption (32775), BadSignature (32774), CouldNotEncrypt (32776), HopCountExceeded (32773), None (0), NotTransactionalMessage (32778), NotTransactionalQueue (32777), Purged (32769), QueueDeleted (49152), QueueExceedMaximumSize (32771), QueuePurged (49153), ReachQueue (2), ReachQueueTimeout (32770), Receive (16384), ReceiveTimeout (49154) """
    AccessDenied: Acknowledgment = ...
    BadDestinationQueue: Acknowledgment = ...
    BadEncryption: Acknowledgment = ...
    BadSignature: Acknowledgment = ...
    CouldNotEncrypt: Acknowledgment = ...
    HopCountExceeded: Acknowledgment = ...
    NotTransactionalMessage: Acknowledgment = ...
    NotTransactionalQueue: Acknowledgment = ...
    Purged: Acknowledgment = ...
    QueueDeleted: Acknowledgment = ...
    QueueExceedMaximumSize: Acknowledgment = ...
    QueuePurged: Acknowledgment = ...
    ReachQueue: Acknowledgment = ...
    ReachQueueTimeout: Acknowledgment = ...
    Receive: Acknowledgment = ...
    ReceiveTimeout: Acknowledgment = ...
    value__ = ...


class ActiveXMessageFormatter(IMessageFormatter): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ ActiveXMessageFormatter() """
    def Clone(self) -> object:
        """ Clone(self: ActiveXMessageFormatter) -> object """
        ...

    @staticmethod
    def InitStreamedObject(streamedObject:object): # -> 
        """ InitStreamedObject(streamedObject: object) """
        ...


class BinaryMessageFormatter(IMessageFormatter): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    BinaryMessageFormatter()
    BinaryMessageFormatter(topObjectFormat: FormatterAssemblyStyle, typeFormat: FormatterTypeStyle)
    """
    @property
    def TopObjectFormat(self) -> FormatterAssemblyStyle:
        """
        Get: TopObjectFormat(self: BinaryMessageFormatter) -> FormatterAssemblyStyle
        Set: TopObjectFormat(self: BinaryMessageFormatter) = value
        """
        ...

    @property
    def TypeFormat(self) -> FormatterTypeStyle:
        """
        Get: TypeFormat(self: BinaryMessageFormatter) -> FormatterTypeStyle
        Set: TypeFormat(self: BinaryMessageFormatter) = value
        """
        ...


    def Clone(self) -> object:
        """ Clone(self: BinaryMessageFormatter) -> object """
        ...


class CryptographicProviderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CryptographicProviderType, values: Dss (3), Fortezza (4), MicrosoftExchange (5), None (0), RsaFull (1), RsqSig (2), Ssl (6), SttAcq (8), SttBrnd (9), SttIss (11), SttMer (7), SttRoot (10) """
    Dss: CryptographicProviderType = ...
    Fortezza: CryptographicProviderType = ...
    MicrosoftExchange: CryptographicProviderType = ...
    RsaFull: CryptographicProviderType = ...
    RsqSig: CryptographicProviderType = ...
    Ssl: CryptographicProviderType = ...
    SttAcq: CryptographicProviderType = ...
    SttBrnd: CryptographicProviderType = ...
    SttIss: CryptographicProviderType = ...
    SttMer: CryptographicProviderType = ...
    SttRoot: CryptographicProviderType = ...
    value__ = ...


class Cursor(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: Cursor) """
        ...


class DefaultPropertiesToSend: # skipped bases: <type 'object'>, <type 'object'>
    """ DefaultPropertiesToSend() """
    @property
    def AcknowledgeType(self) -> AcknowledgeTypes:
        """
        Get: AcknowledgeType(self: DefaultPropertiesToSend) -> AcknowledgeTypes
        Set: AcknowledgeType(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def AdministrationQueue(self) -> MessageQueue:
        """
        Get: AdministrationQueue(self: DefaultPropertiesToSend) -> MessageQueue
        Set: AdministrationQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def AppSpecific(self) -> int:
        """
        Get: AppSpecific(self: DefaultPropertiesToSend) -> int
        Set: AppSpecific(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def AttachSenderId(self) -> bool:
        """
        Get: AttachSenderId(self: DefaultPropertiesToSend) -> bool
        Set: AttachSenderId(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def EncryptionAlgorithm(self) -> EncryptionAlgorithm:
        """
        Get: EncryptionAlgorithm(self: DefaultPropertiesToSend) -> EncryptionAlgorithm
        Set: EncryptionAlgorithm(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def Extension(self) -> Array:
        """
        Get: Extension(self: DefaultPropertiesToSend) -> Array[Byte]
        Set: Extension(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def HashAlgorithm(self) -> HashAlgorithm:
        """
        Get: HashAlgorithm(self: DefaultPropertiesToSend) -> HashAlgorithm
        Set: HashAlgorithm(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: DefaultPropertiesToSend) -> str
        Set: Label(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def Priority(self) -> MessagePriority:
        """
        Get: Priority(self: DefaultPropertiesToSend) -> MessagePriority
        Set: Priority(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def Recoverable(self) -> bool:
        """
        Get: Recoverable(self: DefaultPropertiesToSend) -> bool
        Set: Recoverable(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def ResponseQueue(self) -> MessageQueue:
        """
        Get: ResponseQueue(self: DefaultPropertiesToSend) -> MessageQueue
        Set: ResponseQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def TimeToBeReceived(self) -> TimeSpan:
        """
        Get: TimeToBeReceived(self: DefaultPropertiesToSend) -> TimeSpan
        Set: TimeToBeReceived(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def TimeToReachQueue(self) -> TimeSpan:
        """
        Get: TimeToReachQueue(self: DefaultPropertiesToSend) -> TimeSpan
        Set: TimeToReachQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def TransactionStatusQueue(self) -> MessageQueue:
        """
        Get: TransactionStatusQueue(self: DefaultPropertiesToSend) -> MessageQueue
        Set: TransactionStatusQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def UseAuthentication(self) -> bool:
        """
        Get: UseAuthentication(self: DefaultPropertiesToSend) -> bool
        Set: UseAuthentication(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def UseDeadLetterQueue(self) -> bool:
        """
        Get: UseDeadLetterQueue(self: DefaultPropertiesToSend) -> bool
        Set: UseDeadLetterQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def UseEncryption(self) -> bool:
        """
        Get: UseEncryption(self: DefaultPropertiesToSend) -> bool
        Set: UseEncryption(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def UseJournalQueue(self) -> bool:
        """
        Get: UseJournalQueue(self: DefaultPropertiesToSend) -> bool
        Set: UseJournalQueue(self: DefaultPropertiesToSend) = value
        """
        ...

    @property
    def UseTracing(self) -> bool:
        """
        Get: UseTracing(self: DefaultPropertiesToSend) -> bool
        Set: UseTracing(self: DefaultPropertiesToSend) = value
        """
        ...



class EncryptionAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EncryptionAlgorithm, values: None (0), Rc2 (26114), Rc4 (26625) """
    Rc2: EncryptionAlgorithm = ...
    Rc4: EncryptionAlgorithm = ...
    value__ = ...


class EncryptionRequired(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EncryptionRequired, values: Body (2), None (0), Optional (1) """
    Body: EncryptionRequired = ...
    Optional: EncryptionRequired = ...
    value__ = ...


class GenericAccessRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) GenericAccessRights, values: All (268435456), Execute (536870912), None (0), Read (-2147483648), Write (1073741824) """
    All: GenericAccessRights = ...
    Execute: GenericAccessRights = ...
    Read: GenericAccessRights = ...
    value__ = ...
    Write: GenericAccessRights = ...


class HashAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HashAlgorithm, values: Mac (32773), Md2 (32769), Md4 (32770), Md5 (32771), None (0), Sha (32772), Sha256 (32780), Sha384 (32781), Sha512 (32782) """
    Mac: HashAlgorithm = ...
    Md2: HashAlgorithm = ...
    Md4: HashAlgorithm = ...
    Md5: HashAlgorithm = ...
    Sha: HashAlgorithm = ...
    Sha256: HashAlgorithm = ...
    Sha384: HashAlgorithm = ...
    Sha512: HashAlgorithm = ...
    value__ = ...


class IMessageFormatter(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    def CanRead(self, message:Message) -> bool:
        """ CanRead(self: IMessageFormatter, message: Message) -> bool """
        ...

    def Read(self, message:Message) -> object:
        """ Read(self: IMessageFormatter, message: Message) -> object """
        ...

    def Write(self, message:Message, obj:object): # -> 
        """ Write(self: IMessageFormatter, message: Message, obj: object) """
        ...


class Message(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    Message()
    Message(body: object)
    Message(body: object, formatter: IMessageFormatter)
    """
    @property
    def AcknowledgeType(self) -> AcknowledgeTypes:
        """
        Get: AcknowledgeType(self: Message) -> AcknowledgeTypes
        Set: AcknowledgeType(self: Message) = value
        """
        ...

    @property
    def Acknowledgment(self) -> Acknowledgment:
        """ Get: Acknowledgment(self: Message) -> Acknowledgment """
        ...

    @property
    def AdministrationQueue(self) -> MessageQueue:
        """
        Get: AdministrationQueue(self: Message) -> MessageQueue
        Set: AdministrationQueue(self: Message) = value
        """
        ...

    @property
    def AppSpecific(self) -> int:
        """
        Get: AppSpecific(self: Message) -> int
        Set: AppSpecific(self: Message) = value
        """
        ...

    @property
    def ArrivedTime(self) -> DateTime:
        """ Get: ArrivedTime(self: Message) -> DateTime """
        ...

    @property
    def AttachSenderId(self) -> bool:
        """
        Get: AttachSenderId(self: Message) -> bool
        Set: AttachSenderId(self: Message) = value
        """
        ...

    @property
    def Authenticated(self) -> bool:
        """ Get: Authenticated(self: Message) -> bool """
        ...

    @property
    def AuthenticationProviderName(self) -> str:
        """
        Get: AuthenticationProviderName(self: Message) -> str
        Set: AuthenticationProviderName(self: Message) = value
        """
        ...

    @property
    def AuthenticationProviderType(self) -> CryptographicProviderType:
        """
        Get: AuthenticationProviderType(self: Message) -> CryptographicProviderType
        Set: AuthenticationProviderType(self: Message) = value
        """
        ...

    @property
    def Body(self) -> object:
        """
        Get: Body(self: Message) -> object
        Set: Body(self: Message) = value
        """
        ...

    @property
    def BodyStream(self) -> Stream:
        """
        Get: BodyStream(self: Message) -> Stream
        Set: BodyStream(self: Message) = value
        """
        ...

    @property
    def BodyType(self) -> int:
        """
        Get: BodyType(self: Message) -> int
        Set: BodyType(self: Message) = value
        """
        ...

    @property
    def ConnectorType(self) -> Guid:
        """
        Get: ConnectorType(self: Message) -> Guid
        Set: ConnectorType(self: Message) = value
        """
        ...

    @property
    def CorrelationId(self) -> str:
        """
        Get: CorrelationId(self: Message) -> str
        Set: CorrelationId(self: Message) = value
        """
        ...

    @property
    def DestinationQueue(self) -> MessageQueue:
        """ Get: DestinationQueue(self: Message) -> MessageQueue """
        ...

    @property
    def DestinationSymmetricKey(self) -> Array:
        """
        Get: DestinationSymmetricKey(self: Message) -> Array[Byte]
        Set: DestinationSymmetricKey(self: Message) = value
        """
        ...

    @property
    def DigitalSignature(self) -> Array:
        """
        Get: DigitalSignature(self: Message) -> Array[Byte]
        Set: DigitalSignature(self: Message) = value
        """
        ...

    @property
    def EncryptionAlgorithm(self) -> EncryptionAlgorithm:
        """
        Get: EncryptionAlgorithm(self: Message) -> EncryptionAlgorithm
        Set: EncryptionAlgorithm(self: Message) = value
        """
        ...

    @property
    def Extension(self) -> Array:
        """
        Get: Extension(self: Message) -> Array[Byte]
        Set: Extension(self: Message) = value
        """
        ...

    @property
    def Formatter(self) -> IMessageFormatter:
        """
        Get: Formatter(self: Message) -> IMessageFormatter
        Set: Formatter(self: Message) = value
        """
        ...

    @property
    def HashAlgorithm(self) -> HashAlgorithm:
        """
        Get: HashAlgorithm(self: Message) -> HashAlgorithm
        Set: HashAlgorithm(self: Message) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: Message) -> str """
        ...

    @property
    def IsFirstInTransaction(self) -> bool:
        """ Get: IsFirstInTransaction(self: Message) -> bool """
        ...

    @property
    def IsLastInTransaction(self) -> bool:
        """ Get: IsLastInTransaction(self: Message) -> bool """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: Message) -> str
        Set: Label(self: Message) = value
        """
        ...

    @property
    def LookupId(self) -> Int64:
        """ Get: LookupId(self: Message) -> Int64 """
        ...

    @property
    def MessageType(self) -> MessageType:
        """ Get: MessageType(self: Message) -> MessageType """
        ...

    @property
    def Priority(self) -> MessagePriority:
        """
        Get: Priority(self: Message) -> MessagePriority
        Set: Priority(self: Message) = value
        """
        ...

    @property
    def Recoverable(self) -> bool:
        """
        Get: Recoverable(self: Message) -> bool
        Set: Recoverable(self: Message) = value
        """
        ...

    @property
    def ResponseQueue(self) -> MessageQueue:
        """
        Get: ResponseQueue(self: Message) -> MessageQueue
        Set: ResponseQueue(self: Message) = value
        """
        ...

    @property
    def SecurityContext(self) -> SecurityContext:
        """
        Get: SecurityContext(self: Message) -> SecurityContext
        Set: SecurityContext(self: Message) = value
        """
        ...

    @property
    def SenderCertificate(self) -> Array:
        """
        Get: SenderCertificate(self: Message) -> Array[Byte]
        Set: SenderCertificate(self: Message) = value
        """
        ...

    @property
    def SenderId(self) -> Array:
        """ Get: SenderId(self: Message) -> Array[Byte] """
        ...

    @property
    def SenderVersion(self) -> Int64:
        """ Get: SenderVersion(self: Message) -> Int64 """
        ...

    @property
    def SentTime(self) -> DateTime:
        """ Get: SentTime(self: Message) -> DateTime """
        ...

    @property
    def SourceMachine(self) -> str:
        """ Get: SourceMachine(self: Message) -> str """
        ...

    @property
    def TimeToBeReceived(self) -> TimeSpan:
        """
        Get: TimeToBeReceived(self: Message) -> TimeSpan
        Set: TimeToBeReceived(self: Message) = value
        """
        ...

    @property
    def TimeToReachQueue(self) -> TimeSpan:
        """
        Get: TimeToReachQueue(self: Message) -> TimeSpan
        Set: TimeToReachQueue(self: Message) = value
        """
        ...

    @property
    def TransactionId(self) -> str:
        """ Get: TransactionId(self: Message) -> str """
        ...

    @property
    def TransactionStatusQueue(self) -> MessageQueue:
        """
        Get: TransactionStatusQueue(self: Message) -> MessageQueue
        Set: TransactionStatusQueue(self: Message) = value
        """
        ...

    @property
    def UseAuthentication(self) -> bool:
        """
        Get: UseAuthentication(self: Message) -> bool
        Set: UseAuthentication(self: Message) = value
        """
        ...

    @property
    def UseDeadLetterQueue(self) -> bool:
        """
        Get: UseDeadLetterQueue(self: Message) -> bool
        Set: UseDeadLetterQueue(self: Message) = value
        """
        ...

    @property
    def UseEncryption(self) -> bool:
        """
        Get: UseEncryption(self: Message) -> bool
        Set: UseEncryption(self: Message) = value
        """
        ...

    @property
    def UseJournalQueue(self) -> bool:
        """
        Get: UseJournalQueue(self: Message) -> bool
        Set: UseJournalQueue(self: Message) = value
        """
        ...

    @property
    def UseTracing(self) -> bool:
        """
        Get: UseTracing(self: Message) -> bool
        Set: UseTracing(self: Message) = value
        """
        ...


    def __new__(cls, body:object = ..., formatter:IMessageFormatter = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, body: object)
        __new__(cls: type, body: object, formatter: IMessageFormatter)
        """
        ...

    InfiniteTimeout: TimeSpan = ...


class MessageEnumerator(IEnumerator, IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CursorHandle(self) -> IntPtr:
        """ Get: CursorHandle(self: MessageEnumerator) -> IntPtr """
        ...


    def Close(self): # -> 
        """ Close(self: MessageEnumerator) """
        ...

    def RemoveCurrent(self, *__args:MessageQueueTransaction) -> Message:
        """
        RemoveCurrent(self: MessageEnumerator) -> Message
        RemoveCurrent(self: MessageEnumerator, transaction: MessageQueueTransaction) -> Message
        RemoveCurrent(self: MessageEnumerator, transactionType: MessageQueueTransactionType) -> Message
        RemoveCurrent(self: MessageEnumerator, timeout: TimeSpan) -> Message
        RemoveCurrent(self: MessageEnumerator, timeout: TimeSpan, transaction: MessageQueueTransaction) -> Message
        RemoveCurrent(self: MessageEnumerator, timeout: TimeSpan, transactionType: MessageQueueTransactionType) -> Message
        """
        ...


class MessageLookupAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageLookupAction, values: Current (0), First (4), Last (8), Next (1), Previous (2) """
    Current: MessageLookupAction = ...
    First: MessageLookupAction = ...
    Last: MessageLookupAction = ...
    Next: MessageLookupAction = ...
    Previous: MessageLookupAction = ...
    value__ = ...


class MessagePriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessagePriority, values: AboveNormal (4), High (5), Highest (7), Low (2), Lowest (0), Normal (3), VeryHigh (6), VeryLow (1) """
    AboveNormal: MessagePriority = ...
    High: MessagePriority = ...
    Highest: MessagePriority = ...
    Low: MessagePriority = ...
    Lowest: MessagePriority = ...
    Normal: MessagePriority = ...
    value__ = ...
    VeryHigh: MessagePriority = ...
    VeryLow: MessagePriority = ...


class MessagePropertyFilter(ICloneable): # skipped bases: <type 'object'>
    """ MessagePropertyFilter() """
    @property
    def AcknowledgeType(self) -> bool:
        """
        Get: AcknowledgeType(self: MessagePropertyFilter) -> bool
        Set: AcknowledgeType(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Acknowledgment(self) -> bool:
        """
        Get: Acknowledgment(self: MessagePropertyFilter) -> bool
        Set: Acknowledgment(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def AdministrationQueue(self) -> bool:
        """
        Get: AdministrationQueue(self: MessagePropertyFilter) -> bool
        Set: AdministrationQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def AppSpecific(self) -> bool:
        """
        Get: AppSpecific(self: MessagePropertyFilter) -> bool
        Set: AppSpecific(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def ArrivedTime(self) -> bool:
        """
        Get: ArrivedTime(self: MessagePropertyFilter) -> bool
        Set: ArrivedTime(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def AttachSenderId(self) -> bool:
        """
        Get: AttachSenderId(self: MessagePropertyFilter) -> bool
        Set: AttachSenderId(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Authenticated(self) -> bool:
        """
        Get: Authenticated(self: MessagePropertyFilter) -> bool
        Set: Authenticated(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def AuthenticationProviderName(self) -> bool:
        """
        Get: AuthenticationProviderName(self: MessagePropertyFilter) -> bool
        Set: AuthenticationProviderName(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def AuthenticationProviderType(self) -> bool:
        """
        Get: AuthenticationProviderType(self: MessagePropertyFilter) -> bool
        Set: AuthenticationProviderType(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Body(self) -> bool:
        """
        Get: Body(self: MessagePropertyFilter) -> bool
        Set: Body(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def ConnectorType(self) -> bool:
        """
        Get: ConnectorType(self: MessagePropertyFilter) -> bool
        Set: ConnectorType(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def CorrelationId(self) -> bool:
        """
        Get: CorrelationId(self: MessagePropertyFilter) -> bool
        Set: CorrelationId(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DefaultBodySize(self) -> int:
        """
        Get: DefaultBodySize(self: MessagePropertyFilter) -> int
        Set: DefaultBodySize(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DefaultExtensionSize(self) -> int:
        """
        Get: DefaultExtensionSize(self: MessagePropertyFilter) -> int
        Set: DefaultExtensionSize(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DefaultLabelSize(self) -> int:
        """
        Get: DefaultLabelSize(self: MessagePropertyFilter) -> int
        Set: DefaultLabelSize(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DestinationQueue(self) -> bool:
        """
        Get: DestinationQueue(self: MessagePropertyFilter) -> bool
        Set: DestinationQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DestinationSymmetricKey(self) -> bool:
        """
        Get: DestinationSymmetricKey(self: MessagePropertyFilter) -> bool
        Set: DestinationSymmetricKey(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def DigitalSignature(self) -> bool:
        """
        Get: DigitalSignature(self: MessagePropertyFilter) -> bool
        Set: DigitalSignature(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def EncryptionAlgorithm(self) -> bool:
        """
        Get: EncryptionAlgorithm(self: MessagePropertyFilter) -> bool
        Set: EncryptionAlgorithm(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Extension(self) -> bool:
        """
        Get: Extension(self: MessagePropertyFilter) -> bool
        Set: Extension(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def HashAlgorithm(self) -> bool:
        """
        Get: HashAlgorithm(self: MessagePropertyFilter) -> bool
        Set: HashAlgorithm(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Id(self) -> bool:
        """
        Get: Id(self: MessagePropertyFilter) -> bool
        Set: Id(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def IsFirstInTransaction(self) -> bool:
        """
        Get: IsFirstInTransaction(self: MessagePropertyFilter) -> bool
        Set: IsFirstInTransaction(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def IsLastInTransaction(self) -> bool:
        """
        Get: IsLastInTransaction(self: MessagePropertyFilter) -> bool
        Set: IsLastInTransaction(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Label(self) -> bool:
        """
        Get: Label(self: MessagePropertyFilter) -> bool
        Set: Label(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def LookupId(self) -> bool:
        """
        Get: LookupId(self: MessagePropertyFilter) -> bool
        Set: LookupId(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def MessageType(self) -> bool:
        """
        Get: MessageType(self: MessagePropertyFilter) -> bool
        Set: MessageType(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Priority(self) -> bool:
        """
        Get: Priority(self: MessagePropertyFilter) -> bool
        Set: Priority(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def Recoverable(self) -> bool:
        """
        Get: Recoverable(self: MessagePropertyFilter) -> bool
        Set: Recoverable(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def ResponseQueue(self) -> bool:
        """
        Get: ResponseQueue(self: MessagePropertyFilter) -> bool
        Set: ResponseQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def SenderCertificate(self) -> bool:
        """
        Get: SenderCertificate(self: MessagePropertyFilter) -> bool
        Set: SenderCertificate(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def SenderId(self) -> bool:
        """
        Get: SenderId(self: MessagePropertyFilter) -> bool
        Set: SenderId(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def SenderVersion(self) -> bool:
        """
        Get: SenderVersion(self: MessagePropertyFilter) -> bool
        Set: SenderVersion(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def SentTime(self) -> bool:
        """
        Get: SentTime(self: MessagePropertyFilter) -> bool
        Set: SentTime(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def SourceMachine(self) -> bool:
        """
        Get: SourceMachine(self: MessagePropertyFilter) -> bool
        Set: SourceMachine(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def TimeToBeReceived(self) -> bool:
        """
        Get: TimeToBeReceived(self: MessagePropertyFilter) -> bool
        Set: TimeToBeReceived(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def TimeToReachQueue(self) -> bool:
        """
        Get: TimeToReachQueue(self: MessagePropertyFilter) -> bool
        Set: TimeToReachQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def TransactionId(self) -> bool:
        """
        Get: TransactionId(self: MessagePropertyFilter) -> bool
        Set: TransactionId(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def TransactionStatusQueue(self) -> bool:
        """
        Get: TransactionStatusQueue(self: MessagePropertyFilter) -> bool
        Set: TransactionStatusQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def UseAuthentication(self) -> bool:
        """
        Get: UseAuthentication(self: MessagePropertyFilter) -> bool
        Set: UseAuthentication(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def UseDeadLetterQueue(self) -> bool:
        """
        Get: UseDeadLetterQueue(self: MessagePropertyFilter) -> bool
        Set: UseDeadLetterQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def UseEncryption(self) -> bool:
        """
        Get: UseEncryption(self: MessagePropertyFilter) -> bool
        Set: UseEncryption(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def UseJournalQueue(self) -> bool:
        """
        Get: UseJournalQueue(self: MessagePropertyFilter) -> bool
        Set: UseJournalQueue(self: MessagePropertyFilter) = value
        """
        ...

    @property
    def UseTracing(self) -> bool:
        """
        Get: UseTracing(self: MessagePropertyFilter) -> bool
        Set: UseTracing(self: MessagePropertyFilter) = value
        """
        ...


    def ClearAll(self): # -> 
        """ ClearAll(self: MessagePropertyFilter) """
        ...

    def SetAll(self): # -> 
        """ SetAll(self: MessagePropertyFilter) """
        ...

    def SetDefaults(self): # -> 
        """ SetDefaults(self: MessagePropertyFilter) """
        ...


class MessageQueue(IEnumerable, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    MessageQueue()
    MessageQueue(path: str)
    MessageQueue(path: str, accessMode: QueueAccessMode)
    MessageQueue(path: str, sharedModeDenyReceive: bool)
    MessageQueue(path: str, sharedModeDenyReceive: bool, enableCache: bool)
    MessageQueue(path: str, sharedModeDenyReceive: bool, enableCache: bool, accessMode: QueueAccessMode)
    """
    @property
    def AccessMode(self) -> QueueAccessMode:
        """ Get: AccessMode(self: MessageQueue) -> QueueAccessMode """
        ...

    @property
    def Authenticate(self) -> bool:
        """
        Get: Authenticate(self: MessageQueue) -> bool
        Set: Authenticate(self: MessageQueue) = value
        """
        ...

    @property
    def BasePriority(self) -> Int16:
        """
        Get: BasePriority(self: MessageQueue) -> Int16
        Set: BasePriority(self: MessageQueue) = value
        """
        ...

    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: MessageQueue) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: MessageQueue) -> bool """
        ...

    @property
    def Category(self) -> Guid:
        """
        Get: Category(self: MessageQueue) -> Guid
        Set: Category(self: MessageQueue) = value
        """
        ...

    @property
    def CreateTime(self) -> DateTime:
        """ Get: CreateTime(self: MessageQueue) -> DateTime """
        ...

    @property
    def DefaultPropertiesToSend(self) -> DefaultPropertiesToSend:
        """
        Get: DefaultPropertiesToSend(self: MessageQueue) -> DefaultPropertiesToSend
        Set: DefaultPropertiesToSend(self: MessageQueue) = value
        """
        ...

    @property
    def DenySharedReceive(self) -> bool:
        """
        Get: DenySharedReceive(self: MessageQueue) -> bool
        Set: DenySharedReceive(self: MessageQueue) = value
        """
        ...

    @property
    def EnableConnectionCache(self) -> bool:
        """
        Get: EnableConnectionCache() -> bool
        Set: EnableConnectionCache() = value
        """
        ...

    @property
    def EncryptionRequired(self) -> EncryptionRequired:
        """
        Get: EncryptionRequired(self: MessageQueue) -> EncryptionRequired
        Set: EncryptionRequired(self: MessageQueue) = value
        """
        ...

    @property
    def FormatName(self) -> str:
        """ Get: FormatName(self: MessageQueue) -> str """
        ...

    @property
    def Formatter(self) -> IMessageFormatter:
        """
        Get: Formatter(self: MessageQueue) -> IMessageFormatter
        Set: Formatter(self: MessageQueue) = value
        """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: MessageQueue) -> Guid """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MessageQueue) -> str
        Set: Label(self: MessageQueue) = value
        """
        ...

    @property
    def LastModifyTime(self) -> DateTime:
        """ Get: LastModifyTime(self: MessageQueue) -> DateTime """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: MessageQueue) -> str
        Set: MachineName(self: MessageQueue) = value
        """
        ...

    @property
    def MaximumJournalSize(self) -> Int64:
        """
        Get: MaximumJournalSize(self: MessageQueue) -> Int64
        Set: MaximumJournalSize(self: MessageQueue) = value
        """
        ...

    @property
    def MaximumQueueSize(self) -> Int64:
        """
        Get: MaximumQueueSize(self: MessageQueue) -> Int64
        Set: MaximumQueueSize(self: MessageQueue) = value
        """
        ...

    @property
    def MessageReadPropertyFilter(self) -> MessagePropertyFilter:
        """
        Get: MessageReadPropertyFilter(self: MessageQueue) -> MessagePropertyFilter
        Set: MessageReadPropertyFilter(self: MessageQueue) = value
        """
        ...

    @property
    def MulticastAddress(self) -> str:
        """
        Get: MulticastAddress(self: MessageQueue) -> str
        Set: MulticastAddress(self: MessageQueue) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: MessageQueue) -> str
        Set: Path(self: MessageQueue) = value
        """
        ...

    @property
    def QueueName(self) -> str:
        """
        Get: QueueName(self: MessageQueue) -> str
        Set: QueueName(self: MessageQueue) = value
        """
        ...

    @property
    def ReadHandle(self) -> IntPtr:
        """ Get: ReadHandle(self: MessageQueue) -> IntPtr """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: MessageQueue) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: MessageQueue) = value
        """
        ...

    @property
    def Transactional(self) -> bool:
        """ Get: Transactional(self: MessageQueue) -> bool """
        ...

    @property
    def UseJournalQueue(self) -> bool:
        """
        Get: UseJournalQueue(self: MessageQueue) -> bool
        Set: UseJournalQueue(self: MessageQueue) = value
        """
        ...

    @property
    def WriteHandle(self) -> IntPtr:
        """ Get: WriteHandle(self: MessageQueue) -> IntPtr """
        ...


    def BeginPeek(self, timeout:TimeSpan = ..., *__args:object) -> IAsyncResult:
        """
        BeginPeek(self: MessageQueue) -> IAsyncResult
        BeginPeek(self: MessageQueue, timeout: TimeSpan) -> IAsyncResult
        BeginPeek(self: MessageQueue, timeout: TimeSpan, stateObject: object) -> IAsyncResult
        BeginPeek(self: MessageQueue, timeout: TimeSpan, stateObject: object, callback: AsyncCallback) -> IAsyncResult
        BeginPeek(self: MessageQueue, timeout: TimeSpan, cursor: Cursor, action: PeekAction, state: object, callback: AsyncCallback) -> IAsyncResult
        """
        ...

    def BeginReceive(self, timeout:TimeSpan = ..., *__args:object) -> IAsyncResult:
        """
        BeginReceive(self: MessageQueue) -> IAsyncResult
        BeginReceive(self: MessageQueue, timeout: TimeSpan) -> IAsyncResult
        BeginReceive(self: MessageQueue, timeout: TimeSpan, stateObject: object) -> IAsyncResult
        BeginReceive(self: MessageQueue, timeout: TimeSpan, stateObject: object, callback: AsyncCallback) -> IAsyncResult
        BeginReceive(self: MessageQueue, timeout: TimeSpan, cursor: Cursor, state: object, callback: AsyncCallback) -> IAsyncResult
        """
        ...

    @staticmethod
    def ClearConnectionCache(): # -> 
        """ ClearConnectionCache() """
        ...

    def Close(self): # -> 
        """ Close(self: MessageQueue) """
        ...

    @staticmethod
    def Create(path:str, transactional:bool = ...) -> MessageQueue:
        """
        Create(path: str) -> MessageQueue
        Create(path: str, transactional: bool) -> MessageQueue
        """
        ...

    def CreateCursor(self) -> Cursor:
        """ CreateCursor(self: MessageQueue) -> Cursor """
        ...

    @staticmethod
    def Delete(path:str): # -> 
        """ Delete(path: str) """
        ...

    def EndPeek(self, asyncResult:IAsyncResult) -> Message:
        """ EndPeek(self: MessageQueue, asyncResult: IAsyncResult) -> Message """
        ...

    def EndReceive(self, asyncResult:IAsyncResult) -> Message:
        """ EndReceive(self: MessageQueue, asyncResult: IAsyncResult) -> Message """
        ...

    @staticmethod
    def Exists(path:str) -> bool:
        """ Exists(path: str) -> bool """
        ...

    def GetAllMessages(self) -> Array:
        """ GetAllMessages(self: MessageQueue) -> Array[Message] """
        ...

    @staticmethod
    def GetMachineId(machineName:str) -> Guid:
        """ GetMachineId(machineName: str) -> Guid """
        ...

    def GetMessageEnumerator(self) -> MessageEnumerator:
        """ GetMessageEnumerator(self: MessageQueue) -> MessageEnumerator """
        ...

    def GetMessageEnumerator2(self) -> MessageEnumerator:
        """ GetMessageEnumerator2(self: MessageQueue) -> MessageEnumerator """
        ...

    @staticmethod
    def GetMessageQueueEnumerator(criteria=None) -> MessageQueueEnumerator:
        """
        GetMessageQueueEnumerator() -> MessageQueueEnumerator
        GetMessageQueueEnumerator(criteria: MessageQueueCriteria) -> MessageQueueEnumerator
        """
        ...

    @staticmethod
    def GetPrivateQueuesByMachine(machineName:str) -> Array:
        """ GetPrivateQueuesByMachine(machineName: str) -> Array[MessageQueue] """
        ...

    @staticmethod
    def GetPublicQueues(criteria=None) -> Array:
        """
        GetPublicQueues() -> Array[MessageQueue]
        GetPublicQueues(criteria: MessageQueueCriteria) -> Array[MessageQueue]
        """
        ...

    @staticmethod
    def GetPublicQueuesByCategory(category:Guid) -> Array:
        """ GetPublicQueuesByCategory(category: Guid) -> Array[MessageQueue] """
        ...

    @staticmethod
    def GetPublicQueuesByLabel(label:str) -> Array:
        """ GetPublicQueuesByLabel(label: str) -> Array[MessageQueue] """
        ...

    @staticmethod
    def GetPublicQueuesByMachine(machineName:str) -> Array:
        """ GetPublicQueuesByMachine(machineName: str) -> Array[MessageQueue] """
        ...

    @staticmethod
    def GetSecurityContext() -> SecurityContext:
        """ GetSecurityContext() -> SecurityContext """
        ...

    def Peek(self, timeout:TimeSpan = ..., cursor:Cursor = ..., action:PeekAction = ...) -> Message:
        """
        Peek(self: MessageQueue) -> Message
        Peek(self: MessageQueue, timeout: TimeSpan) -> Message
        Peek(self: MessageQueue, timeout: TimeSpan, cursor: Cursor, action: PeekAction) -> Message
        """
        ...

    def PeekByCorrelationId(self, correlationId:str, timeout:TimeSpan = ...) -> Message:
        """
        PeekByCorrelationId(self: MessageQueue, correlationId: str) -> Message
        PeekByCorrelationId(self: MessageQueue, correlationId: str, timeout: TimeSpan) -> Message
        """
        ...

    def PeekById(self, id:str, timeout:TimeSpan = ...) -> Message:
        """
        PeekById(self: MessageQueue, id: str) -> Message
        PeekById(self: MessageQueue, id: str, timeout: TimeSpan) -> Message
        """
        ...

    def PeekByLookupId(self, *__args:Int64) -> Message:
        """
        PeekByLookupId(self: MessageQueue, lookupId: Int64) -> Message
        PeekByLookupId(self: MessageQueue, action: MessageLookupAction, lookupId: Int64) -> Message
        """
        ...

    def Purge(self): # -> 
        """ Purge(self: MessageQueue) """
        ...

    def Receive(self, *__args:MessageQueueTransaction) -> Message:
        """
        Receive(self: MessageQueue) -> Message
        Receive(self: MessageQueue, transaction: MessageQueueTransaction) -> Message
        Receive(self: MessageQueue, transactionType: MessageQueueTransactionType) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan, cursor: Cursor) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan, transaction: MessageQueueTransaction) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan, transactionType: MessageQueueTransactionType) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan, cursor: Cursor, transaction: MessageQueueTransaction) -> Message
        Receive(self: MessageQueue, timeout: TimeSpan, cursor: Cursor, transactionType: MessageQueueTransactionType) -> Message
        """
        ...

    def ReceiveByCorrelationId(self, correlationId:str, *__args:MessageQueueTransaction) -> Message:
        """
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str) -> Message
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str, transaction: MessageQueueTransaction) -> Message
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str, transactionType: MessageQueueTransactionType) -> Message
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str, timeout: TimeSpan) -> Message
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str, timeout: TimeSpan, transaction: MessageQueueTransaction) -> Message
        ReceiveByCorrelationId(self: MessageQueue, correlationId: str, timeout: TimeSpan, transactionType: MessageQueueTransactionType) -> Message
        """
        ...

    def ReceiveById(self, id:str, *__args:MessageQueueTransaction) -> Message:
        """
        ReceiveById(self: MessageQueue, id: str) -> Message
        ReceiveById(self: MessageQueue, id: str, transaction: MessageQueueTransaction) -> Message
        ReceiveById(self: MessageQueue, id: str, transactionType: MessageQueueTransactionType) -> Message
        ReceiveById(self: MessageQueue, id: str, timeout: TimeSpan) -> Message
        ReceiveById(self: MessageQueue, id: str, timeout: TimeSpan, transaction: MessageQueueTransaction) -> Message
        ReceiveById(self: MessageQueue, id: str, timeout: TimeSpan, transactionType: MessageQueueTransactionType) -> Message
        """
        ...

    def ReceiveByLookupId(self, *__args:Int64) -> Message:
        """
        ReceiveByLookupId(self: MessageQueue, lookupId: Int64) -> Message
        ReceiveByLookupId(self: MessageQueue, action: MessageLookupAction, lookupId: Int64, transactionType: MessageQueueTransactionType) -> Message
        ReceiveByLookupId(self: MessageQueue, action: MessageLookupAction, lookupId: Int64, transaction: MessageQueueTransaction) -> Message
        """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: MessageQueue) """
        ...

    def ResetPermissions(self): # -> 
        """ ResetPermissions(self: MessageQueue) """
        ...

    def Send(self, obj:object, *__args:MessageQueueTransaction): # -> 
        """ Send(self: MessageQueue, obj: object)Send(self: MessageQueue, obj: object, transaction: MessageQueueTransaction)Send(self: MessageQueue, obj: object, transactionType: MessageQueueTransactionType)Send(self: MessageQueue, obj: object, label: str)Send(self: MessageQueue, obj: object, label: str, transaction: MessageQueueTransaction)Send(self: MessageQueue, obj: object, label: str, transactionType: MessageQueueTransactionType) """
        ...

    def SetPermissions(self, *__args:MessageQueueAccessControlEntry): # -> 
        """ SetPermissions(self: MessageQueue, user: str, rights: MessageQueueAccessRights)SetPermissions(self: MessageQueue, user: str, rights: MessageQueueAccessRights, entryType: AccessControlEntryType)SetPermissions(self: MessageQueue, ace: MessageQueueAccessControlEntry)SetPermissions(self: MessageQueue, dacl: AccessControlList) """
        ...

    def __new__(cls, path:str = ..., *__args:QueueAccessMode) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, accessMode: QueueAccessMode)
        __new__(cls: type, path: str, sharedModeDenyReceive: bool)
        __new__(cls: type, path: str, sharedModeDenyReceive: bool, enableCache: bool)
        __new__(cls: type, path: str, sharedModeDenyReceive: bool, enableCache: bool, accessMode: QueueAccessMode)
        """
        ...

    InfiniteQueueSize: Int64 = ...
    InfiniteTimeout: TimeSpan = ...
    PeekCompleted = ...
    ReceiveCompleted = ...


class MessageQueueAccessControlEntry(AccessControlEntry): # skipped bases: <type 'object'>
    """
    MessageQueueAccessControlEntry(trustee: Trustee, rights: MessageQueueAccessRights)
    MessageQueueAccessControlEntry(trustee: Trustee, rights: MessageQueueAccessRights, entryType: AccessControlEntryType)
    """
    @property
    def MessageQueueAccessRights(self) -> MessageQueueAccessRights:
        """
        Get: MessageQueueAccessRights(self: MessageQueueAccessControlEntry) -> MessageQueueAccessRights
        Set: MessageQueueAccessRights(self: MessageQueueAccessControlEntry) = value
        """
        ...



class MessageQueueAccessRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MessageQueueAccessRights, values: ChangeQueuePermissions (262144), DeleteJournalMessage (8), DeleteMessage (1), DeleteQueue (65536), FullControl (983103), GenericRead (131115), GenericWrite (131108), GetQueuePermissions (131072), GetQueueProperties (32), PeekMessage (2), ReceiveJournalMessage (10), ReceiveMessage (3), SetQueueProperties (16), TakeQueueOwnership (524288), WriteMessage (4) """
    ChangeQueuePermissions: MessageQueueAccessRights = ...
    DeleteJournalMessage: MessageQueueAccessRights = ...
    DeleteMessage: MessageQueueAccessRights = ...
    DeleteQueue: MessageQueueAccessRights = ...
    FullControl: MessageQueueAccessRights = ...
    GenericRead: MessageQueueAccessRights = ...
    GenericWrite: MessageQueueAccessRights = ...
    GetQueuePermissions: MessageQueueAccessRights = ...
    GetQueueProperties: MessageQueueAccessRights = ...
    PeekMessage: MessageQueueAccessRights = ...
    ReceiveJournalMessage: MessageQueueAccessRights = ...
    ReceiveMessage: MessageQueueAccessRights = ...
    SetQueueProperties: MessageQueueAccessRights = ...
    TakeQueueOwnership: MessageQueueAccessRights = ...
    value__ = ...
    WriteMessage: MessageQueueAccessRights = ...


class MessageQueueCriteria: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageQueueCriteria() """
    @property
    def Category(self) -> Guid:
        """
        Get: Category(self: MessageQueueCriteria) -> Guid
        Set: Category(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def CreatedAfter(self) -> DateTime:
        """
        Get: CreatedAfter(self: MessageQueueCriteria) -> DateTime
        Set: CreatedAfter(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def CreatedBefore(self) -> DateTime:
        """
        Get: CreatedBefore(self: MessageQueueCriteria) -> DateTime
        Set: CreatedBefore(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MessageQueueCriteria) -> str
        Set: Label(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: MessageQueueCriteria) -> str
        Set: MachineName(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def ModifiedAfter(self) -> DateTime:
        """
        Get: ModifiedAfter(self: MessageQueueCriteria) -> DateTime
        Set: ModifiedAfter(self: MessageQueueCriteria) = value
        """
        ...

    @property
    def ModifiedBefore(self) -> DateTime:
        """
        Get: ModifiedBefore(self: MessageQueueCriteria) -> DateTime
        Set: ModifiedBefore(self: MessageQueueCriteria) = value
        """
        ...


    def ClearAll(self): # -> 
        """ ClearAll(self: MessageQueueCriteria) """
        ...


class MessageQueueEnumerator(IEnumerator, IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocatorHandle(self) -> IntPtr:
        """ Get: LocatorHandle(self: MessageQueueEnumerator) -> IntPtr """
        ...


    def Close(self): # -> 
        """ Close(self: MessageQueueEnumerator) """
        ...


class MessageQueueErrorCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageQueueErrorCode, values: AccessDenied (-1072824283), BadSecurityContext (-1072824267), Base (-1072824320), BufferOverflow (-1072824294), CannotCreateCertificateStore (-1072824209), CannotCreateHashEx (-1072824191), CannotCreateOnGlobalCatalog (-1072824201), CannotGetDistinguishedName (-1072824194), CannotGrantAddGuid (-1072824206), CannotHashDataEx (-1072824193), CannotImpersonateClient (-1072824284), CannotJoinDomain (-1072824202), CannotLoadMsmqOcm (-1072824205), CannotOpenCertificateStore (-1072824208), CannotSetCryptographicSecurityDescriptor (-1072824212), CannotSignDataEx (-1072824192), CertificateNotProvided (-1072824211), ComputerDoesNotSupportEncryption (-1072824269), CorruptedInternalCertificate (-1072824275), CorruptedPersonalCertStore (-1072824271), CorruptedQueueWasDeleted (-1072824216), CorruptedSecurityData (-1072824272), CouldNotGetAccountInfo (-1072824265), CouldNotGetUserSid (-1072824266), DeleteConnectedNetworkInUse (-1072824248), DependentClientLicenseOverflow (-1072824217), DsError (-1072824253), DsIsFull (-1072824254), DtcConnect (-1072824244), EncryptionProviderNotSupported (-1072824213), FailVerifySignatureEx (-1072824190), FormatNameBufferTooSmall (-1072824289), Generic (-1072824319), GuidNotMatching (-1072824200), IllegalContext (-1072824229), IllegalCriteriaColumns (-1072824264), IllegalCursorAction (-1072824292), IllegalEnterpriseOperation (-1072824207), IllegalFormatName (-1072824290), IllegalMessageProperties (-1072824255), IllegalOperation (-1072824220), IllegalPrivateProperties (-1072824197), IllegalPropertyId (-1072824263), IllegalPropertySize (-1072824261), IllegalPropertyValue (-1072824296), IllegalPropertyVt (-1072824295), IllegalQueuePathName (-1072824300), IllegalQueueProperties (-1072824259), IllegalRelation (-1072824262), IllegalRestrictionPropertyId (-1072824260), IllegalSecurityDescriptor (-1072824287), IllegalSort (-1072824304), IllegalSortPropertyId (-1072824228), IllegalUser (-1072824303), InsufficientProperties (-1072824257), InsufficientResources (-1072824281), InvalidCertificate (-1072824276), InvalidHandle (-1072824313), InvalidOwner (-1072824252), InvalidParameter (-1072824314), IOTimeout (-1072824293), LabelBufferTooSmall (-1072824226), MachineExists (-1072824256), MachineNotFound (-1072824307), MessageAlreadyReceived (-1072824291), MessageNotFound (-1072824184), MessageStorageFailed (-1072824278), MissingConnectorType (-1072824235), MqisReadOnlyMode (-1072824224), MqisServerEmpty (-1072824225), NoDs (-1072824301), NoEntryPointMsmqOcm (-1072824204), NoGlobalCatalogInDomain (-1072824196), NoInternalUserCertificate (-1072824273), NoMsmqServersOnDc (-1072824203), NoMsmqServersOnGlobalCatalog (-1072824195), NoResponseFromObjectServer (-1072824247), ObjectServerNotAvailable (-1072824246), OperationCanceled (-1072824312), PrivilegeNotHeld (-1072824282), Property (-1072824318), PropertyNotAllowed (-1072824258), ProviderNameBufferTooSmall (-1072824221), PublicKeyDoesNotExist (-1072824198), PublicKeyNotFound (-1072824199), QDnsPropertyNotSupported (-1072824210), QueueDeleted (-1072824230), QueueExists (-1072824315), QueueNotAvailable (-1072824245), QueueNotFound (-1072824317), RemoteMachineNotAvailable (-1072824215), ResultBufferTooSmall (-1072824250), SecurityDescriptorBufferTooSmall (-1072824285), SenderCertificateBufferTooSmall (-1072824277), SenderIdBufferTooSmall (-1072824286), ServiceNotAvailable (-1072824309), SharingViolation (-1072824311), SignatureBufferTooSmall (-1072824222), StaleHandle (-1072824234), SymmetricKeyBufferTooSmall (-1072824223), TransactionEnlist (-1072824232), TransactionImport (-1072824242), TransactionSequence (-1072824239), TransactionUsage (-1072824240), UnsupportedAccessMode (-1072824251), UnsupportedFormatNameOperation (-1072824288), UnsupportedOperation (-1072824214), UserBufferTooSmall (-1072824280), WksCantServeClient (-1072824218), WriteNotAllowed (-1072824219) """
    AccessDenied: MessageQueueErrorCode = ...
    BadSecurityContext: MessageQueueErrorCode = ...
    Base: MessageQueueErrorCode = ...
    BufferOverflow: MessageQueueErrorCode = ...
    CannotCreateCertificateStore: MessageQueueErrorCode = ...
    CannotCreateHashEx: MessageQueueErrorCode = ...
    CannotCreateOnGlobalCatalog: MessageQueueErrorCode = ...
    CannotGetDistinguishedName: MessageQueueErrorCode = ...
    CannotGrantAddGuid: MessageQueueErrorCode = ...
    CannotHashDataEx: MessageQueueErrorCode = ...
    CannotImpersonateClient: MessageQueueErrorCode = ...
    CannotJoinDomain: MessageQueueErrorCode = ...
    CannotLoadMsmqOcm: MessageQueueErrorCode = ...
    CannotOpenCertificateStore: MessageQueueErrorCode = ...
    CannotSetCryptographicSecurityDescriptor: MessageQueueErrorCode = ...
    CannotSignDataEx: MessageQueueErrorCode = ...
    CertificateNotProvided: MessageQueueErrorCode = ...
    ComputerDoesNotSupportEncryption: MessageQueueErrorCode = ...
    CorruptedInternalCertificate: MessageQueueErrorCode = ...
    CorruptedPersonalCertStore: MessageQueueErrorCode = ...
    CorruptedQueueWasDeleted: MessageQueueErrorCode = ...
    CorruptedSecurityData: MessageQueueErrorCode = ...
    CouldNotGetAccountInfo: MessageQueueErrorCode = ...
    CouldNotGetUserSid: MessageQueueErrorCode = ...
    DeleteConnectedNetworkInUse: MessageQueueErrorCode = ...
    DependentClientLicenseOverflow: MessageQueueErrorCode = ...
    DsError: MessageQueueErrorCode = ...
    DsIsFull: MessageQueueErrorCode = ...
    DtcConnect: MessageQueueErrorCode = ...
    EncryptionProviderNotSupported: MessageQueueErrorCode = ...
    FailVerifySignatureEx: MessageQueueErrorCode = ...
    FormatNameBufferTooSmall: MessageQueueErrorCode = ...
    Generic: MessageQueueErrorCode = ...
    GuidNotMatching: MessageQueueErrorCode = ...
    IllegalContext: MessageQueueErrorCode = ...
    IllegalCriteriaColumns: MessageQueueErrorCode = ...
    IllegalCursorAction: MessageQueueErrorCode = ...
    IllegalEnterpriseOperation: MessageQueueErrorCode = ...
    IllegalFormatName: MessageQueueErrorCode = ...
    IllegalMessageProperties: MessageQueueErrorCode = ...
    IllegalOperation: MessageQueueErrorCode = ...
    IllegalPrivateProperties: MessageQueueErrorCode = ...
    IllegalPropertyId: MessageQueueErrorCode = ...
    IllegalPropertySize: MessageQueueErrorCode = ...
    IllegalPropertyValue: MessageQueueErrorCode = ...
    IllegalPropertyVt: MessageQueueErrorCode = ...
    IllegalQueuePathName: MessageQueueErrorCode = ...
    IllegalQueueProperties: MessageQueueErrorCode = ...
    IllegalRelation: MessageQueueErrorCode = ...
    IllegalRestrictionPropertyId: MessageQueueErrorCode = ...
    IllegalSecurityDescriptor: MessageQueueErrorCode = ...
    IllegalSort: MessageQueueErrorCode = ...
    IllegalSortPropertyId: MessageQueueErrorCode = ...
    IllegalUser: MessageQueueErrorCode = ...
    InsufficientProperties: MessageQueueErrorCode = ...
    InsufficientResources: MessageQueueErrorCode = ...
    InvalidCertificate: MessageQueueErrorCode = ...
    InvalidHandle: MessageQueueErrorCode = ...
    InvalidOwner: MessageQueueErrorCode = ...
    InvalidParameter: MessageQueueErrorCode = ...
    IOTimeout: MessageQueueErrorCode = ...
    LabelBufferTooSmall: MessageQueueErrorCode = ...
    MachineExists: MessageQueueErrorCode = ...
    MachineNotFound: MessageQueueErrorCode = ...
    MessageAlreadyReceived: MessageQueueErrorCode = ...
    MessageNotFound: MessageQueueErrorCode = ...
    MessageStorageFailed: MessageQueueErrorCode = ...
    MissingConnectorType: MessageQueueErrorCode = ...
    MqisReadOnlyMode: MessageQueueErrorCode = ...
    MqisServerEmpty: MessageQueueErrorCode = ...
    NoDs: MessageQueueErrorCode = ...
    NoEntryPointMsmqOcm: MessageQueueErrorCode = ...
    NoGlobalCatalogInDomain: MessageQueueErrorCode = ...
    NoInternalUserCertificate: MessageQueueErrorCode = ...
    NoMsmqServersOnDc: MessageQueueErrorCode = ...
    NoMsmqServersOnGlobalCatalog: MessageQueueErrorCode = ...
    NoResponseFromObjectServer: MessageQueueErrorCode = ...
    ObjectServerNotAvailable: MessageQueueErrorCode = ...
    OperationCanceled: MessageQueueErrorCode = ...
    PrivilegeNotHeld: MessageQueueErrorCode = ...
    Property: MessageQueueErrorCode = ...
    PropertyNotAllowed: MessageQueueErrorCode = ...
    ProviderNameBufferTooSmall: MessageQueueErrorCode = ...
    PublicKeyDoesNotExist: MessageQueueErrorCode = ...
    PublicKeyNotFound: MessageQueueErrorCode = ...
    QDnsPropertyNotSupported: MessageQueueErrorCode = ...
    QueueDeleted: MessageQueueErrorCode = ...
    QueueExists: MessageQueueErrorCode = ...
    QueueNotAvailable: MessageQueueErrorCode = ...
    QueueNotFound: MessageQueueErrorCode = ...
    RemoteMachineNotAvailable: MessageQueueErrorCode = ...
    ResultBufferTooSmall: MessageQueueErrorCode = ...
    SecurityDescriptorBufferTooSmall: MessageQueueErrorCode = ...
    SenderCertificateBufferTooSmall: MessageQueueErrorCode = ...
    SenderIdBufferTooSmall: MessageQueueErrorCode = ...
    ServiceNotAvailable: MessageQueueErrorCode = ...
    SharingViolation: MessageQueueErrorCode = ...
    SignatureBufferTooSmall: MessageQueueErrorCode = ...
    StaleHandle: MessageQueueErrorCode = ...
    SymmetricKeyBufferTooSmall: MessageQueueErrorCode = ...
    TransactionEnlist: MessageQueueErrorCode = ...
    TransactionImport: MessageQueueErrorCode = ...
    TransactionSequence: MessageQueueErrorCode = ...
    TransactionUsage: MessageQueueErrorCode = ...
    UnsupportedAccessMode: MessageQueueErrorCode = ...
    UnsupportedFormatNameOperation: MessageQueueErrorCode = ...
    UnsupportedOperation: MessageQueueErrorCode = ...
    UserBufferTooSmall: MessageQueueErrorCode = ...
    value__ = ...
    WksCantServeClient: MessageQueueErrorCode = ...
    WriteNotAllowed: MessageQueueErrorCode = ...


class MessageQueueException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: MessageQueueException) -> str """
        ...

    @property
    def MessageQueueErrorCode(self) -> MessageQueueErrorCode:
        """ Get: MessageQueueErrorCode(self: MessageQueueException) -> MessageQueueErrorCode """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: MessageQueueException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class MessageQueueInstaller(ComponentInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    MessageQueueInstaller()
    MessageQueueInstaller(componentToCopy: MessageQueue)
    """
    @property
    def Authenticate(self) -> bool:
        """
        Get: Authenticate(self: MessageQueueInstaller) -> bool
        Set: Authenticate(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def BasePriority(self) -> Int16:
        """
        Get: BasePriority(self: MessageQueueInstaller) -> Int16
        Set: BasePriority(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def Category(self) -> Guid:
        """
        Get: Category(self: MessageQueueInstaller) -> Guid
        Set: Category(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def EncryptionRequired(self) -> EncryptionRequired:
        """
        Get: EncryptionRequired(self: MessageQueueInstaller) -> EncryptionRequired
        Set: EncryptionRequired(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MessageQueueInstaller) -> str
        Set: Label(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def MaximumJournalSize(self) -> Int64:
        """
        Get: MaximumJournalSize(self: MessageQueueInstaller) -> Int64
        Set: MaximumJournalSize(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def MaximumQueueSize(self) -> Int64:
        """
        Get: MaximumQueueSize(self: MessageQueueInstaller) -> Int64
        Set: MaximumQueueSize(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def MulticastAddress(self) -> str:
        """
        Get: MulticastAddress(self: MessageQueueInstaller) -> str
        Set: MulticastAddress(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: MessageQueueInstaller) -> str
        Set: Path(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def Permissions(self) -> AccessControlList:
        """
        Get: Permissions(self: MessageQueueInstaller) -> AccessControlList
        Set: Permissions(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def Transactional(self) -> bool:
        """
        Get: Transactional(self: MessageQueueInstaller) -> bool
        Set: Transactional(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def UninstallAction(self) -> UninstallAction:
        """
        Get: UninstallAction(self: MessageQueueInstaller) -> UninstallAction
        Set: UninstallAction(self: MessageQueueInstaller) = value
        """
        ...

    @property
    def UseJournalQueue(self) -> bool:
        """
        Get: UseJournalQueue(self: MessageQueueInstaller) -> bool
        Set: UseJournalQueue(self: MessageQueueInstaller) = value
        """
        ...


    def Commit(self, savedState:IDictionary): # -> 
        """ Commit(self: MessageQueueInstaller, savedState: IDictionary) """
        ...

    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: MessageQueueInstaller, stateSaver: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: MessageQueueInstaller, savedState: IDictionary) """
        ...

    def Uninstall(self, savedState:IDictionary): # -> 
        """ Uninstall(self: MessageQueueInstaller, savedState: IDictionary) """
        ...

    def __new__(cls, componentToCopy:MessageQueue = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, componentToCopy: MessageQueue)
        """
        ...


class MessageQueuePermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    MessageQueuePermission()
    MessageQueuePermission(state: PermissionState)
    MessageQueuePermission(permissionAccess: MessageQueuePermissionAccess, path: str)
    MessageQueuePermission(permissionAccess: MessageQueuePermissionAccess, machineName: str, label: str, category: str)
    MessageQueuePermission(permissionAccessEntries: Array[MessageQueuePermissionEntry])
    """
    @property
    def PermissionEntries(self) -> MessageQueuePermissionEntryCollection:
        """ Get: PermissionEntries(self: MessageQueuePermission) -> MessageQueuePermissionEntryCollection """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, permissionAccess: MessageQueuePermissionAccess, path: str)
        __new__(cls: type, permissionAccess: MessageQueuePermissionAccess, machineName: str, label: str, category: str)
        __new__(cls: type, permissionAccessEntries: Array[MessageQueuePermissionEntry])
        """
        ...


class MessageQueuePermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MessageQueuePermissionAccess, values: Administer (62), Browse (2), None (0), Peek (10), Receive (26), Send (6) """
    Administer: MessageQueuePermissionAccess = ...
    Browse: MessageQueuePermissionAccess = ...
    Peek: MessageQueuePermissionAccess = ...
    Receive: MessageQueuePermissionAccess = ...
    Send: MessageQueuePermissionAccess = ...
    value__ = ...


class MessageQueuePermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessageQueuePermissionAttribute(action: SecurityAction) """
    @property
    def Category(self) -> str:
        """
        Get: Category(self: MessageQueuePermissionAttribute) -> str
        Set: Category(self: MessageQueuePermissionAttribute) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: MessageQueuePermissionAttribute) -> str
        Set: Label(self: MessageQueuePermissionAttribute) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: MessageQueuePermissionAttribute) -> str
        Set: MachineName(self: MessageQueuePermissionAttribute) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: MessageQueuePermissionAttribute) -> str
        Set: Path(self: MessageQueuePermissionAttribute) = value
        """
        ...

    @property
    def PermissionAccess(self) -> MessageQueuePermissionAccess:
        """
        Get: PermissionAccess(self: MessageQueuePermissionAttribute) -> MessageQueuePermissionAccess
        Set: PermissionAccess(self: MessageQueuePermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: MessageQueuePermissionAttribute) -> IPermission """
        ...


class MessageQueuePermissionEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    MessageQueuePermissionEntry(permissionAccess: MessageQueuePermissionAccess, path: str)
    MessageQueuePermissionEntry(permissionAccess: MessageQueuePermissionAccess, machineName: str, label: str, category: str)
    """
    @property
    def Category(self) -> str:
        """ Get: Category(self: MessageQueuePermissionEntry) -> str """
        ...

    @property
    def Label(self) -> str:
        """ Get: Label(self: MessageQueuePermissionEntry) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: MessageQueuePermissionEntry) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: MessageQueuePermissionEntry) -> str """
        ...

    @property
    def PermissionAccess(self) -> MessageQueuePermissionAccess:
        """ Get: PermissionAccess(self: MessageQueuePermissionEntry) -> MessageQueuePermissionAccess """
        ...



class MessageQueuePermissionEntryCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:MessageQueuePermissionEntry) -> int:
        """ Add(self: MessageQueuePermissionEntryCollection, value: MessageQueuePermissionEntry) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: MessageQueuePermissionEntryCollection, value: Array[MessageQueuePermissionEntry])AddRange(self: MessageQueuePermissionEntryCollection, value: MessageQueuePermissionEntryCollection) """
        ...

    def Contains(self, value:MessageQueuePermissionEntry) -> bool:
        """ Contains(self: MessageQueuePermissionEntryCollection, value: MessageQueuePermissionEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessageQueuePermissionEntryCollection, array: Array[MessageQueuePermissionEntry], index: int) """
        ...

    def IndexOf(self, value:MessageQueuePermissionEntry) -> int:
        """ IndexOf(self: MessageQueuePermissionEntryCollection, value: MessageQueuePermissionEntry) -> int """
        ...

    def Insert(self, index:int, value:MessageQueuePermissionEntry): # -> 
        """ Insert(self: MessageQueuePermissionEntryCollection, index: int, value: MessageQueuePermissionEntry) """
        ...

    def Remove(self, value:MessageQueuePermissionEntry): # -> 
        """ Remove(self: MessageQueuePermissionEntryCollection, value: MessageQueuePermissionEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class MessageQueueTransaction(IDisposable): # skipped bases: <type 'object'>
    """ MessageQueueTransaction() """
    @property
    def Status(self) -> MessageQueueTransactionStatus:
        """ Get: Status(self: MessageQueueTransaction) -> MessageQueueTransactionStatus """
        ...


    def Abort(self): # -> 
        """ Abort(self: MessageQueueTransaction) """
        ...

    def Begin(self): # -> 
        """ Begin(self: MessageQueueTransaction) """
        ...

    def Commit(self): # -> 
        """ Commit(self: MessageQueueTransaction) """
        ...


class MessageQueueTransactionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageQueueTransactionStatus, values: Aborted (0), Committed (1), Initialized (2), Pending (3) """
    Aborted: MessageQueueTransactionStatus = ...
    Committed: MessageQueueTransactionStatus = ...
    Initialized: MessageQueueTransactionStatus = ...
    Pending: MessageQueueTransactionStatus = ...
    value__ = ...


class MessageQueueTransactionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageQueueTransactionType, values: Automatic (1), None (0), Single (3) """
    Automatic: MessageQueueTransactionType = ...
    Single: MessageQueueTransactionType = ...
    value__ = ...


class MessageType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageType, values: Acknowledgment (1), Normal (2), Report (3) """
    Acknowledgment: MessageType = ...
    Normal: MessageType = ...
    Report: MessageType = ...
    value__ = ...


class MessagingDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MessagingDescriptionAttribute(description: str) """
    pass

class PeekAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeekAction, values: Current (-2147483648), Next (-2147483647) """
    Current: PeekAction = ...
    Next: PeekAction = ...
    value__ = ...


class PeekCompletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsyncResult(self) -> IAsyncResult:
        """
        Get: AsyncResult(self: PeekCompletedEventArgs) -> IAsyncResult
        Set: AsyncResult(self: PeekCompletedEventArgs) = value
        """
        ...

    @property
    def Message(self) -> Message:
        """ Get: Message(self: PeekCompletedEventArgs) -> Message """
        ...



class PeekCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PeekCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PeekCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PeekCompletedEventHandler, sender: object, e: PeekCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PeekCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PeekCompletedEventArgs): # -> 
        """ Invoke(self: PeekCompletedEventHandler, sender: object, e: PeekCompletedEventArgs) """
        ...


class QueueAccessMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueueAccessMode, values: Peek (32), PeekAndAdmin (160), Receive (1), ReceiveAndAdmin (129), Send (2), SendAndReceive (3) """
    Peek: QueueAccessMode = ...
    PeekAndAdmin: QueueAccessMode = ...
    Receive: QueueAccessMode = ...
    ReceiveAndAdmin: QueueAccessMode = ...
    Send: QueueAccessMode = ...
    SendAndReceive: QueueAccessMode = ...
    value__ = ...


class ReceiveCompletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsyncResult(self) -> IAsyncResult:
        """
        Get: AsyncResult(self: ReceiveCompletedEventArgs) -> IAsyncResult
        Set: AsyncResult(self: ReceiveCompletedEventArgs) = value
        """
        ...

    @property
    def Message(self) -> Message:
        """ Get: Message(self: ReceiveCompletedEventArgs) -> Message """
        ...



class ReceiveCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReceiveCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ReceiveCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReceiveCompletedEventHandler, sender: object, e: ReceiveCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReceiveCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ReceiveCompletedEventArgs): # -> 
        """ Invoke(self: ReceiveCompletedEventHandler, sender: object, e: ReceiveCompletedEventArgs) """
        ...


class SecurityContext(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class StandardAccessRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StandardAccessRights, values: All (2031616), Delete (65536), Execute (131072), ModifyOwner (524288), None (0), Read (131072), ReadSecurity (131072), Required (851968), Synchronize (1048576), Write (131072), WriteSecurity (262144) """
    All: StandardAccessRights = ...
    Delete: StandardAccessRights = ...
    Execute: StandardAccessRights = ...
    ModifyOwner: StandardAccessRights = ...
    Read: StandardAccessRights = ...
    ReadSecurity: StandardAccessRights = ...
    Required: StandardAccessRights = ...
    Synchronize: StandardAccessRights = ...
    value__ = ...
    Write: StandardAccessRights = ...
    WriteSecurity: StandardAccessRights = ...


class Trustee: # skipped bases: <type 'object'>, <type 'object'>
    """
    Trustee()
    Trustee(name: str)
    Trustee(name: str, systemName: str)
    Trustee(name: str, systemName: str, trusteeType: TrusteeType)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: Trustee) -> str
        Set: Name(self: Trustee) = value
        """
        ...

    @property
    def SystemName(self) -> str:
        """
        Get: SystemName(self: Trustee) -> str
        Set: SystemName(self: Trustee) = value
        """
        ...

    @property
    def TrusteeType(self) -> TrusteeType:
        """
        Get: TrusteeType(self: Trustee) -> TrusteeType
        Set: TrusteeType(self: Trustee) = value
        """
        ...



class TrusteeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrusteeType, values: Alias (4), Computer (5), Domain (3), Group (2), Unknown (0), User (1) """
    Alias: TrusteeType = ...
    Computer: TrusteeType = ...
    Domain: TrusteeType = ...
    Group: TrusteeType = ...
    Unknown: TrusteeType = ...
    User: TrusteeType = ...
    value__ = ...


class XmlMessageFormatter(IMessageFormatter): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    XmlMessageFormatter()
    XmlMessageFormatter(targetTypeNames: Array[str])
    XmlMessageFormatter(targetTypes: Array[Type])
    """
    @property
    def TargetTypeNames(self) -> Array:
        """
        Get: TargetTypeNames(self: XmlMessageFormatter) -> Array[str]
        Set: TargetTypeNames(self: XmlMessageFormatter) = value
        """
        ...

    @property
    def TargetTypes(self) -> Array:
        """
        Get: TargetTypes(self: XmlMessageFormatter) -> Array[Type]
        Set: TargetTypes(self: XmlMessageFormatter) = value
        """
        ...


    def Clone(self) -> object:
        """ Clone(self: XmlMessageFormatter) -> object """
        ...


# variables with complex values

