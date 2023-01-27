# encoding: utf-8
# module System.DirectoryServices.Protocols calls itself Protocols
# from System.DirectoryServices.Protocols, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, IAsyncResult, IDisposable, 
    Int64, MulticastDelegate, TimeSpan, Type, Uri)

from System.Collections import (CollectionBase, DictionaryBase, ICollection, 
    IEnumerator, IList, ReadOnlyCollectionBase)

from System.Collections.Specialized import StringCollection

from System.Net import NetworkCredential

from System.Security.Authentication import (CipherAlgorithmType, 
    HashAlgorithmType)

from System.Security.Cryptography.X509Certificates import (X509Certificate, 
    X509CertificateCollection)

from System.Security.Principal import SecurityIdentifier

from System.Xml import XmlDocument, XmlNode

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DirectoryOperation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DirectoryRequest(DirectoryOperation): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Controls(self) -> DirectoryControlCollection:
        """ Get: Controls(self: DirectoryRequest) -> DirectoryControlCollection """
        ...

    @property
    def RequestId(self) -> str:
        """
        Get: RequestId(self: DirectoryRequest) -> str
        Set: RequestId(self: DirectoryRequest) = value
        """
        ...


    def ToXmlNode(self, *args): #cannot find CLR method
        """ ToXmlNode(self: DirectoryRequest, doc: XmlDocument) -> XmlElement """
        ...


class AddRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    AddRequest()
    AddRequest(distinguishedName: str, *attributes: Array[DirectoryAttribute])
    AddRequest(distinguishedName: str, objectClass: str)
    """
    @property
    def Attributes(self) -> DirectoryAttributeCollection:
        """ Get: Attributes(self: AddRequest) -> DirectoryAttributeCollection """
        ...

    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: AddRequest) -> str
        Set: DistinguishedName(self: AddRequest) = value
        """
        ...


    def __new__(cls, distinguishedName:str = ..., *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str, *attributes: Array[DirectoryAttribute])
        __new__(cls: type, distinguishedName: str, objectClass: str)
        """
        ...


class DirectoryResponse(DirectoryOperation): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Controls(self) -> Array:
        """ Get: Controls(self: DirectoryResponse) -> Array[DirectoryControl] """
        ...

    @property
    def ErrorMessage(self) -> str:
        """ Get: ErrorMessage(self: DirectoryResponse) -> str """
        ...

    @property
    def MatchedDN(self) -> str:
        """ Get: MatchedDN(self: DirectoryResponse) -> str """
        ...

    @property
    def Referral(self) -> Array:
        """ Get: Referral(self: DirectoryResponse) -> Array[Uri] """
        ...

    @property
    def RequestId(self) -> str:
        """ Get: RequestId(self: DirectoryResponse) -> str """
        ...

    @property
    def ResultCode(self) -> ResultCode:
        """ Get: ResultCode(self: DirectoryResponse) -> ResultCode """
        ...



class AddResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DirectoryControl: # skipped bases: <type 'object'>, <type 'object'>
    """ DirectoryControl(type: str, value: Array[Byte], isCritical: bool, serverSide: bool) """
    @property
    def IsCritical(self) -> bool:
        """
        Get: IsCritical(self: DirectoryControl) -> bool
        Set: IsCritical(self: DirectoryControl) = value
        """
        ...

    @property
    def ServerSide(self) -> bool:
        """
        Get: ServerSide(self: DirectoryControl) -> bool
        Set: ServerSide(self: DirectoryControl) = value
        """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: DirectoryControl) -> str """
        ...


    def GetValue(self) -> Array:
        """ GetValue(self: DirectoryControl) -> Array[Byte] """
        ...


class AsqRequestControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    AsqRequestControl()
    AsqRequestControl(attributeName: str)
    """
    @property
    def AttributeName(self) -> str:
        """
        Get: AttributeName(self: AsqRequestControl) -> str
        Set: AttributeName(self: AsqRequestControl) = value
        """
        ...



class AsqResponseControl(DirectoryControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> ResultCode:
        """ Get: Result(self: AsqResponseControl) -> ResultCode """
        ...



class AuthType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthType, values: Anonymous (0), Basic (1), Digest (4), Dpa (6), External (8), Kerberos (9), Msn (7), Negotiate (2), Ntlm (3), Sicily (5) """
    Anonymous: AuthType = ...
    Basic: AuthType = ...
    Digest: AuthType = ...
    Dpa: AuthType = ...
    External: AuthType = ...
    Kerberos: AuthType = ...
    Msn: AuthType = ...
    Negotiate: AuthType = ...
    Ntlm: AuthType = ...
    Sicily: AuthType = ...
    value__ = ...


class DirectoryException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DirectoryException(message: str, inner: Exception)
    DirectoryException(message: str)
    DirectoryException()
    """
    SerializeObjectState = ...


class BerConversionException(DirectoryException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    BerConversionException()
    BerConversionException(message: str)
    BerConversionException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class BerConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Decode(format:str, value:Array) -> Array:
        """ Decode(format: str, value: Array[Byte]) -> Array[object] """
        ...

    @staticmethod
    def Encode(format:str, value:Array) -> Array:
        """ Encode(format: str, *value: Array[object]) -> Array[Byte] """
        ...


class CompareRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    CompareRequest()
    CompareRequest(distinguishedName: str, attributeName: str, value: str)
    CompareRequest(distinguishedName: str, attributeName: str, value: Array[Byte])
    CompareRequest(distinguishedName: str, attributeName: str, value: Uri)
    CompareRequest(distinguishedName: str, assertion: DirectoryAttribute)
    """
    @property
    def Assertion(self) -> DirectoryAttribute:
        """ Get: Assertion(self: CompareRequest) -> DirectoryAttribute """
        ...

    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: CompareRequest) -> str
        Set: DistinguishedName(self: CompareRequest) = value
        """
        ...


    def __new__(cls, distinguishedName:str = ..., *__args:DirectoryAttribute) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str, attributeName: str, value: str)
        __new__(cls: type, distinguishedName: str, attributeName: str, value: Array[Byte])
        __new__(cls: type, distinguishedName: str, attributeName: str, value: Uri)
        __new__(cls: type, distinguishedName: str, assertion: DirectoryAttribute)
        """
        ...


class CompareResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CrossDomainMoveControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    CrossDomainMoveControl()
    CrossDomainMoveControl(targetDomainController: str)
    """
    @property
    def TargetDomainController(self) -> str:
        """
        Get: TargetDomainController(self: CrossDomainMoveControl) -> str
        Set: TargetDomainController(self: CrossDomainMoveControl) = value
        """
        ...



class DeleteRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    DeleteRequest()
    DeleteRequest(distinguishedName: str)
    """
    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: DeleteRequest) -> str
        Set: DistinguishedName(self: DeleteRequest) = value
        """
        ...


    def __new__(cls, distinguishedName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str)
        """
        ...


class DeleteResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DereferenceAlias(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DereferenceAlias, values: Always (3), FindingBaseObject (2), InSearching (1), Never (0) """
    Always: DereferenceAlias = ...
    FindingBaseObject: DereferenceAlias = ...
    InSearching: DereferenceAlias = ...
    Never: DereferenceAlias = ...
    value__ = ...


class DereferenceConnectionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DereferenceConnectionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, primaryConnection:LdapConnection, connectionToDereference:LdapConnection, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DereferenceConnectionCallback, primaryConnection: LdapConnection, connectionToDereference: LdapConnection, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DereferenceConnectionCallback, result: IAsyncResult) """
        ...

    def Invoke(self, primaryConnection:LdapConnection, connectionToDereference:LdapConnection): # -> 
        """ Invoke(self: DereferenceConnectionCallback, primaryConnection: LdapConnection, connectionToDereference: LdapConnection) """
        ...


class DirectoryAttribute(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    DirectoryAttribute()
    DirectoryAttribute(name: str, value: str)
    DirectoryAttribute(name: str, value: Array[Byte])
    DirectoryAttribute(name: str, value: Uri)
    DirectoryAttribute(name: str, *values: Array[object])
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: DirectoryAttribute) -> str
        Set: Name(self: DirectoryAttribute) = value
        """
        ...


    def Add(self, value:Array) -> int:
        """
        Add(self: DirectoryAttribute, value: Array[Byte]) -> int
        Add(self: DirectoryAttribute, value: str) -> int
        Add(self: DirectoryAttribute, value: Uri) -> int
        """
        ...

    def AddRange(self, values:Array): # -> 
        """ AddRange(self: DirectoryAttribute, values: Array[object]) """
        ...

    def Contains(self, value:object) -> bool:
        """ Contains(self: DirectoryAttribute, value: object) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryAttribute, array: Array[object], index: int) """
        ...

    def GetValues(self, valuesType:Type) -> Array:
        """ GetValues(self: DirectoryAttribute, valuesType: Type) -> Array[object] """
        ...

    def IndexOf(self, value:object) -> int:
        """ IndexOf(self: DirectoryAttribute, value: object) -> int """
        ...

    def Insert(self, index:int, value:Array): # -> 
        """ Insert(self: DirectoryAttribute, index: int, value: Array[Byte])Insert(self: DirectoryAttribute, index: int, value: str)Insert(self: DirectoryAttribute, index: int, value: Uri) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: DirectoryAttribute, value: object) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DirectoryAttributeCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DirectoryAttributeCollection() """
    def Add(self, attribute:DirectoryAttribute) -> int:
        """ Add(self: DirectoryAttributeCollection, attribute: DirectoryAttribute) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: DirectoryAttributeCollection, attributes: Array[DirectoryAttribute])AddRange(self: DirectoryAttributeCollection, attributeCollection: DirectoryAttributeCollection) """
        ...

    def Contains(self, value:DirectoryAttribute) -> bool:
        """ Contains(self: DirectoryAttributeCollection, value: DirectoryAttribute) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryAttributeCollection, array: Array[DirectoryAttribute], index: int) """
        ...

    def IndexOf(self, value:DirectoryAttribute) -> int:
        """ IndexOf(self: DirectoryAttributeCollection, value: DirectoryAttribute) -> int """
        ...

    def Insert(self, index:int, value:DirectoryAttribute): # -> 
        """ Insert(self: DirectoryAttributeCollection, index: int, value: DirectoryAttribute) """
        ...

    def Remove(self, value:DirectoryAttribute): # -> 
        """ Remove(self: DirectoryAttributeCollection, value: DirectoryAttribute) """
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


class DirectoryAttributeModification(DirectoryAttribute): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DirectoryAttributeModification() """
    @property
    def Operation(self) -> DirectoryAttributeOperation:
        """
        Get: Operation(self: DirectoryAttributeModification) -> DirectoryAttributeOperation
        Set: Operation(self: DirectoryAttributeModification) = value
        """
        ...



class DirectoryAttributeModificationCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DirectoryAttributeModificationCollection() """
    def Add(self, attribute:DirectoryAttributeModification) -> int:
        """ Add(self: DirectoryAttributeModificationCollection, attribute: DirectoryAttributeModification) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: DirectoryAttributeModificationCollection, attributes: Array[DirectoryAttributeModification])AddRange(self: DirectoryAttributeModificationCollection, attributeCollection: DirectoryAttributeModificationCollection) """
        ...

    def Contains(self, value:DirectoryAttributeModification) -> bool:
        """ Contains(self: DirectoryAttributeModificationCollection, value: DirectoryAttributeModification) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryAttributeModificationCollection, array: Array[DirectoryAttributeModification], index: int) """
        ...

    def IndexOf(self, value:DirectoryAttributeModification) -> int:
        """ IndexOf(self: DirectoryAttributeModificationCollection, value: DirectoryAttributeModification) -> int """
        ...

    def Insert(self, index:int, value:DirectoryAttributeModification): # -> 
        """ Insert(self: DirectoryAttributeModificationCollection, index: int, value: DirectoryAttributeModification) """
        ...

    def Remove(self, value:DirectoryAttributeModification): # -> 
        """ Remove(self: DirectoryAttributeModificationCollection, value: DirectoryAttributeModification) """
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


class DirectoryAttributeOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DirectoryAttributeOperation, values: Add (0), Delete (1), Replace (2) """
    Add: DirectoryAttributeOperation = ...
    Delete: DirectoryAttributeOperation = ...
    Replace: DirectoryAttributeOperation = ...
    value__ = ...


class DirectoryConnection: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """ Get: ClientCertificates(self: DirectoryConnection) -> X509CertificateCollection """
        ...

    @property
    def Credential(self): # -> 
        """ Set: Credential(self: DirectoryConnection) = value """
        ...

    @property
    def Directory(self) -> DirectoryIdentifier:
        """ Get: Directory(self: DirectoryConnection) -> DirectoryIdentifier """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: DirectoryConnection) -> TimeSpan
        Set: Timeout(self: DirectoryConnection) = value
        """
        ...


    def SendRequest(self, request:DirectoryRequest) -> DirectoryResponse:
        """ SendRequest(self: DirectoryConnection, request: DirectoryRequest) -> DirectoryResponse """
        ...


class DirectoryControlCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DirectoryControlCollection() """
    def Add(self, control:DirectoryControl) -> int:
        """ Add(self: DirectoryControlCollection, control: DirectoryControl) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: DirectoryControlCollection, controls: Array[DirectoryControl])AddRange(self: DirectoryControlCollection, controlCollection: DirectoryControlCollection) """
        ...

    def Contains(self, value:DirectoryControl) -> bool:
        """ Contains(self: DirectoryControlCollection, value: DirectoryControl) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryControlCollection, array: Array[DirectoryControl], index: int) """
        ...

    def IndexOf(self, value:DirectoryControl) -> int:
        """ IndexOf(self: DirectoryControlCollection, value: DirectoryControl) -> int """
        ...

    def Insert(self, index:int, value:DirectoryControl): # -> 
        """ Insert(self: DirectoryControlCollection, index: int, value: DirectoryControl) """
        ...

    def Remove(self, value:DirectoryControl): # -> 
        """ Remove(self: DirectoryControlCollection, value: DirectoryControl) """
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


class DirectoryIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DirectoryNotificationControl(DirectoryControl): # skipped bases: <type 'object'>
    """ DirectoryNotificationControl() """
    pass

class DirectoryOperationException(DirectoryException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DirectoryOperationException()
    DirectoryOperationException(message: str)
    DirectoryOperationException(message: str, inner: Exception)
    DirectoryOperationException(response: DirectoryResponse)
    DirectoryOperationException(response: DirectoryResponse, message: str)
    DirectoryOperationException(response: DirectoryResponse, message: str, inner: Exception)
    """
    @property
    def Response(self) -> DirectoryResponse:
        """ Get: Response(self: DirectoryOperationException) -> DirectoryResponse """
        ...


    SerializeObjectState = ...


class DirectorySynchronizationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DirectorySynchronizationOptions, values: IncrementalValues (2147483648), None (0), ObjectSecurity (1), ParentsFirst (2048), PublicDataOnly (8192) """
    IncrementalValues: DirectorySynchronizationOptions = ...
    ObjectSecurity: DirectorySynchronizationOptions = ...
    ParentsFirst: DirectorySynchronizationOptions = ...
    PublicDataOnly: DirectorySynchronizationOptions = ...
    value__ = ...


class DirSyncRequestControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    DirSyncRequestControl()
    DirSyncRequestControl(cookie: Array[Byte])
    DirSyncRequestControl(cookie: Array[Byte], option: DirectorySynchronizationOptions)
    DirSyncRequestControl(cookie: Array[Byte], option: DirectorySynchronizationOptions, attributeCount: int)
    """
    @property
    def AttributeCount(self) -> int:
        """
        Get: AttributeCount(self: DirSyncRequestControl) -> int
        Set: AttributeCount(self: DirSyncRequestControl) = value
        """
        ...

    @property
    def Cookie(self) -> Array:
        """
        Get: Cookie(self: DirSyncRequestControl) -> Array[Byte]
        Set: Cookie(self: DirSyncRequestControl) = value
        """
        ...

    @property
    def Option(self) -> DirectorySynchronizationOptions:
        """
        Get: Option(self: DirSyncRequestControl) -> DirectorySynchronizationOptions
        Set: Option(self: DirSyncRequestControl) = value
        """
        ...



class DirSyncResponseControl(DirectoryControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Cookie(self) -> Array:
        """ Get: Cookie(self: DirSyncResponseControl) -> Array[Byte] """
        ...

    @property
    def MoreData(self) -> bool:
        """ Get: MoreData(self: DirSyncResponseControl) -> bool """
        ...

    @property
    def ResultSize(self) -> int:
        """ Get: ResultSize(self: DirSyncResponseControl) -> int """
        ...



class DomainScopeControl(DirectoryControl): # skipped bases: <type 'object'>
    """ DomainScopeControl() """
    pass

class DsmlAuthRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    DsmlAuthRequest()
    DsmlAuthRequest(principal: str)
    """
    @property
    def Principal(self) -> str:
        """
        Get: Principal(self: DsmlAuthRequest) -> str
        Set: Principal(self: DsmlAuthRequest) = value
        """
        ...


    def __new__(cls, principal:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, principal: str)
        """
        ...


class DsmlAuthResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DsmlDirectoryIdentifier(DirectoryIdentifier): # skipped bases: <type 'object'>
    """ DsmlDirectoryIdentifier(serverUri: Uri) """
    @property
    def ServerUri(self) -> Uri:
        """ Get: ServerUri(self: DsmlDirectoryIdentifier) -> Uri """
        ...


    def __new__(cls, serverUri:Uri) -> Self:
        """ __new__(cls: type, serverUri: Uri) """
        ...


class DsmlDocument: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ToXml(self) -> XmlDocument:
        """ ToXml(self: DsmlDocument) -> XmlDocument """
        ...


class DsmlDocumentProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DsmlDocumentProcessing, values: Parallel (1), Sequential (0) """
    Parallel: DsmlDocumentProcessing = ...
    Sequential: DsmlDocumentProcessing = ...
    value__ = ...


class DsmlErrorProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DsmlErrorProcessing, values: Exit (1), Resume (0) """
    Exit: DsmlErrorProcessing = ...
    Resume: DsmlErrorProcessing = ...
    value__ = ...


class DsmlErrorResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Detail(self) -> str:
        """ Get: Detail(self: DsmlErrorResponse) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: DsmlErrorResponse) -> str """
        ...

    @property
    def Type(self) -> ErrorResponseCategory:
        """ Get: Type(self: DsmlErrorResponse) -> ErrorResponseCategory """
        ...



class DsmlInvalidDocumentException(DirectoryException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DsmlInvalidDocumentException()
    DsmlInvalidDocumentException(message: str)
    DsmlInvalidDocumentException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class DsmlRequestDocument(IList, DsmlDocument): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DsmlRequestDocument() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DsmlRequestDocument) -> int """
        ...

    @property
    def DocumentProcessing(self) -> DsmlDocumentProcessing:
        """
        Get: DocumentProcessing(self: DsmlRequestDocument) -> DsmlDocumentProcessing
        Set: DocumentProcessing(self: DsmlRequestDocument) = value
        """
        ...

    @property
    def ErrorProcessing(self) -> DsmlErrorProcessing:
        """
        Get: ErrorProcessing(self: DsmlRequestDocument) -> DsmlErrorProcessing
        Set: ErrorProcessing(self: DsmlRequestDocument) = value
        """
        ...

    @property
    def IsSynchronized(self):
        ...

    @property
    def RequestId(self) -> str:
        """
        Get: RequestId(self: DsmlRequestDocument) -> str
        Set: RequestId(self: DsmlRequestDocument) = value
        """
        ...

    @property
    def ResponseOrder(self) -> DsmlResponseOrder:
        """
        Get: ResponseOrder(self: DsmlRequestDocument) -> DsmlResponseOrder
        Set: ResponseOrder(self: DsmlRequestDocument) = value
        """
        ...

    @property
    def SyncRoot(self):
        ...


    def CopyTo(self, value:Array, i:int): # -> 
        """ CopyTo(self: DsmlRequestDocument, value: Array[DirectoryRequest], i: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DsmlRequestDocument) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class DsmlResponseDocument(DsmlDocument, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsErrorResponse(self) -> bool:
        """ Get: IsErrorResponse(self: DsmlResponseDocument) -> bool """
        ...

    @property
    def IsOperationError(self) -> bool:
        """ Get: IsOperationError(self: DsmlResponseDocument) -> bool """
        ...

    @property
    def RequestId(self) -> str:
        """ Get: RequestId(self: DsmlResponseDocument) -> str """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DsmlResponseDocument) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DsmlResponseOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DsmlResponseOrder, values: Sequential (0), Unordered (1) """
    Sequential: DsmlResponseOrder = ...
    Unordered: DsmlResponseOrder = ...
    value__ = ...


class DsmlSoapConnection(DirectoryConnection): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SessionId(self) -> str:
        """ Get: SessionId(self: DsmlSoapConnection) -> str """
        ...

    @property
    def SoapRequestHeader(self) -> XmlNode:
        """
        Get: SoapRequestHeader(self: DsmlSoapConnection) -> XmlNode
        Set: SoapRequestHeader(self: DsmlSoapConnection) = value
        """
        ...


    def BeginSession(self): # -> 
        """ BeginSession(self: DsmlSoapConnection) """
        ...

    def EndSession(self): # -> 
        """ EndSession(self: DsmlSoapConnection) """
        ...


class DsmlSoapHttpConnection(DsmlSoapConnection): # skipped bases: <type 'object'>
    """
    DsmlSoapHttpConnection(uri: Uri)
    DsmlSoapHttpConnection(identifier: DsmlDirectoryIdentifier)
    DsmlSoapHttpConnection(identifier: DsmlDirectoryIdentifier, credential: NetworkCredential)
    DsmlSoapHttpConnection(identifier: DsmlDirectoryIdentifier, credential: NetworkCredential, authType: AuthType)
    """
    @property
    def AuthType(self) -> AuthType:
        """
        Get: AuthType(self: DsmlSoapHttpConnection) -> AuthType
        Set: AuthType(self: DsmlSoapHttpConnection) = value
        """
        ...

    @property
    def SoapActionHeader(self) -> str:
        """
        Get: SoapActionHeader(self: DsmlSoapHttpConnection) -> str
        Set: SoapActionHeader(self: DsmlSoapHttpConnection) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: DsmlSoapHttpConnection) -> TimeSpan
        Set: Timeout(self: DsmlSoapHttpConnection) = value
        """
        ...


    def Abort(self, asyncResult:IAsyncResult): # -> 
        """ Abort(self: DsmlSoapHttpConnection, asyncResult: IAsyncResult) """
        ...

    def BeginSendRequest(self, request:DsmlRequestDocument, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSendRequest(self: DsmlSoapHttpConnection, request: DsmlRequestDocument, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndSendRequest(self, asyncResult:IAsyncResult) -> DsmlResponseDocument:
        """ EndSendRequest(self: DsmlSoapHttpConnection, asyncResult: IAsyncResult) -> DsmlResponseDocument """
        ...

    def SendRequest(self, request:DirectoryRequest) -> DirectoryResponse:
        """
        SendRequest(self: DsmlSoapHttpConnection, request: DirectoryRequest) -> DirectoryResponse
        SendRequest(self: DsmlSoapHttpConnection, request: DsmlRequestDocument) -> DsmlResponseDocument
        """
        ...

    def __new__(cls, *__args:Uri) -> Self:
        """
        __new__(cls: type, uri: Uri)
        __new__(cls: type, identifier: DsmlDirectoryIdentifier)
        __new__(cls: type, identifier: DsmlDirectoryIdentifier, credential: NetworkCredential)
        __new__(cls: type, identifier: DsmlDirectoryIdentifier, credential: NetworkCredential, authType: AuthType)
        """
        ...


class ErrorResponseCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ErrorResponseCategory, values: AuthenticationFailed (5), ConnectionClosed (2), CouldNotConnect (1), GatewayInternalError (4), MalformedRequest (3), NotAttempted (0), Other (7), UnresolvableUri (6) """
    AuthenticationFailed: ErrorResponseCategory = ...
    ConnectionClosed: ErrorResponseCategory = ...
    CouldNotConnect: ErrorResponseCategory = ...
    GatewayInternalError: ErrorResponseCategory = ...
    MalformedRequest: ErrorResponseCategory = ...
    NotAttempted: ErrorResponseCategory = ...
    Other: ErrorResponseCategory = ...
    UnresolvableUri: ErrorResponseCategory = ...
    value__ = ...


class ErrorResponseException(DirectoryException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ErrorResponseException()
    ErrorResponseException(message: str)
    ErrorResponseException(message: str, inner: Exception)
    ErrorResponseException(response: DsmlErrorResponse)
    ErrorResponseException(response: DsmlErrorResponse, message: str)
    ErrorResponseException(response: DsmlErrorResponse, message: str, inner: Exception)
    """
    @property
    def Response(self) -> DsmlErrorResponse:
        """ Get: Response(self: ErrorResponseException) -> DsmlErrorResponse """
        ...


    SerializeObjectState = ...


class ExtendedDNControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    ExtendedDNControl()
    ExtendedDNControl(flag: ExtendedDNFlag)
    """
    @property
    def Flag(self) -> ExtendedDNFlag:
        """
        Get: Flag(self: ExtendedDNControl) -> ExtendedDNFlag
        Set: Flag(self: ExtendedDNControl) = value
        """
        ...



class ExtendedDNFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExtendedDNFlag, values: HexString (0), StandardString (1) """
    HexString: ExtendedDNFlag = ...
    StandardString: ExtendedDNFlag = ...
    value__ = ...


class ExtendedRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    ExtendedRequest()
    ExtendedRequest(requestName: str)
    ExtendedRequest(requestName: str, requestValue: Array[Byte])
    """
    @property
    def RequestName(self) -> str:
        """
        Get: RequestName(self: ExtendedRequest) -> str
        Set: RequestName(self: ExtendedRequest) = value
        """
        ...

    @property
    def RequestValue(self) -> Array:
        """
        Get: RequestValue(self: ExtendedRequest) -> Array[Byte]
        Set: RequestValue(self: ExtendedRequest) = value
        """
        ...


    def __new__(cls, requestName:str = ..., requestValue:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, requestName: str)
        __new__(cls: type, requestName: str, requestValue: Array[Byte])
        """
        ...


class ExtendedResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ResponseName(self) -> str:
        """ Get: ResponseName(self: ExtendedResponse) -> str """
        ...

    @property
    def ResponseValue(self) -> Array:
        """ Get: ResponseValue(self: ExtendedResponse) -> Array[Byte] """
        ...



class LazyCommitControl(DirectoryControl): # skipped bases: <type 'object'>
    """ LazyCommitControl() """
    pass

class LdapConnection(IDisposable, DirectoryConnection): # skipped bases: <type 'object'>
    """
    LdapConnection(server: str)
    LdapConnection(identifier: LdapDirectoryIdentifier)
    LdapConnection(identifier: LdapDirectoryIdentifier, credential: NetworkCredential)
    LdapConnection(identifier: LdapDirectoryIdentifier, credential: NetworkCredential, authType: AuthType)
    """
    @property
    def AuthType(self) -> AuthType:
        """
        Get: AuthType(self: LdapConnection) -> AuthType
        Set: AuthType(self: LdapConnection) = value
        """
        ...

    @property
    def AutoBind(self) -> bool:
        """
        Get: AutoBind(self: LdapConnection) -> bool
        Set: AutoBind(self: LdapConnection) = value
        """
        ...

    @property
    def SessionOptions(self) -> LdapSessionOptions:
        """ Get: SessionOptions(self: LdapConnection) -> LdapSessionOptions """
        ...


    def Abort(self, asyncResult:IAsyncResult): # -> 
        """ Abort(self: LdapConnection, asyncResult: IAsyncResult) """
        ...

    def BeginSendRequest(self, request, *__args) -> IAsyncResult:
        """
        BeginSendRequest(self: LdapConnection, request: DirectoryRequest, partialMode: PartialResultProcessing, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSendRequest(self: LdapConnection, request: DirectoryRequest, requestTimeout: TimeSpan, partialMode: PartialResultProcessing, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Bind(self, newCredential:NetworkCredential = ...): # -> 
        """ Bind(self: LdapConnection)Bind(self: LdapConnection, newCredential: NetworkCredential) """
        ...

    def EndSendRequest(self, asyncResult:IAsyncResult) -> DirectoryResponse:
        """ EndSendRequest(self: LdapConnection, asyncResult: IAsyncResult) -> DirectoryResponse """
        ...

    def GetPartialResults(self, asyncResult:IAsyncResult) -> PartialResultsCollection:
        """ GetPartialResults(self: LdapConnection, asyncResult: IAsyncResult) -> PartialResultsCollection """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, server: str)
        __new__(cls: type, identifier: LdapDirectoryIdentifier)
        __new__(cls: type, identifier: LdapDirectoryIdentifier, credential: NetworkCredential)
        __new__(cls: type, identifier: LdapDirectoryIdentifier, credential: NetworkCredential, authType: AuthType)
        """
        ...


class LdapDirectoryIdentifier(DirectoryIdentifier): # skipped bases: <type 'object'>
    """
    LdapDirectoryIdentifier(server: str)
    LdapDirectoryIdentifier(server: str, portNumber: int)
    LdapDirectoryIdentifier(server: str, fullyQualifiedDnsHostName: bool, connectionless: bool)
    LdapDirectoryIdentifier(server: str, portNumber: int, fullyQualifiedDnsHostName: bool, connectionless: bool)
    LdapDirectoryIdentifier(servers: Array[str], fullyQualifiedDnsHostName: bool, connectionless: bool)
    LdapDirectoryIdentifier(servers: Array[str], portNumber: int, fullyQualifiedDnsHostName: bool, connectionless: bool)
    """
    @property
    def Connectionless(self) -> bool:
        """ Get: Connectionless(self: LdapDirectoryIdentifier) -> bool """
        ...

    @property
    def FullyQualifiedDnsHostName(self) -> bool:
        """ Get: FullyQualifiedDnsHostName(self: LdapDirectoryIdentifier) -> bool """
        ...

    @property
    def PortNumber(self) -> int:
        """ Get: PortNumber(self: LdapDirectoryIdentifier) -> int """
        ...

    @property
    def Servers(self) -> Array:
        """ Get: Servers(self: LdapDirectoryIdentifier) -> Array[str] """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, server: str)
        __new__(cls: type, server: str, portNumber: int)
        __new__(cls: type, server: str, fullyQualifiedDnsHostName: bool, connectionless: bool)
        __new__(cls: type, server: str, portNumber: int, fullyQualifiedDnsHostName: bool, connectionless: bool)
        __new__(cls: type, servers: Array[str], fullyQualifiedDnsHostName: bool, connectionless: bool)
        __new__(cls: type, servers: Array[str], portNumber: int, fullyQualifiedDnsHostName: bool, connectionless: bool)
        """
        ...


class LdapException(DirectoryException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LdapException()
    LdapException(message: str)
    LdapException(message: str, inner: Exception)
    LdapException(errorCode: int)
    LdapException(errorCode: int, message: str)
    LdapException(errorCode: int, message: str, serverErrorMessage: str)
    LdapException(errorCode: int, message: str, inner: Exception)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: LdapException) -> int """
        ...

    @property
    def PartialResults(self) -> PartialResultsCollection:
        """ Get: PartialResults(self: LdapException) -> PartialResultsCollection """
        ...

    @property
    def ServerErrorMessage(self) -> str:
        """ Get: ServerErrorMessage(self: LdapException) -> str """
        ...


    SerializeObjectState = ...


class LdapSessionOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoReconnect(self) -> bool:
        """
        Get: AutoReconnect(self: LdapSessionOptions) -> bool
        Set: AutoReconnect(self: LdapSessionOptions) = value
        """
        ...

    @property
    def DomainName(self) -> str:
        """
        Get: DomainName(self: LdapSessionOptions) -> str
        Set: DomainName(self: LdapSessionOptions) = value
        """
        ...

    @property
    def HostName(self) -> str:
        """
        Get: HostName(self: LdapSessionOptions) -> str
        Set: HostName(self: LdapSessionOptions) = value
        """
        ...

    @property
    def HostReachable(self) -> bool:
        """ Get: HostReachable(self: LdapSessionOptions) -> bool """
        ...

    @property
    def LocatorFlag(self) -> LocatorFlags:
        """
        Get: LocatorFlag(self: LdapSessionOptions) -> LocatorFlags
        Set: LocatorFlag(self: LdapSessionOptions) = value
        """
        ...

    @property
    def PingKeepAliveTimeout(self) -> TimeSpan:
        """
        Get: PingKeepAliveTimeout(self: LdapSessionOptions) -> TimeSpan
        Set: PingKeepAliveTimeout(self: LdapSessionOptions) = value
        """
        ...

    @property
    def PingLimit(self) -> int:
        """
        Get: PingLimit(self: LdapSessionOptions) -> int
        Set: PingLimit(self: LdapSessionOptions) = value
        """
        ...

    @property
    def PingWaitTimeout(self) -> TimeSpan:
        """
        Get: PingWaitTimeout(self: LdapSessionOptions) -> TimeSpan
        Set: PingWaitTimeout(self: LdapSessionOptions) = value
        """
        ...

    @property
    def ProtocolVersion(self) -> int:
        """
        Get: ProtocolVersion(self: LdapSessionOptions) -> int
        Set: ProtocolVersion(self: LdapSessionOptions) = value
        """
        ...

    @property
    def QueryClientCertificate(self) -> QueryClientCertificateCallback:
        """
        Get: QueryClientCertificate(self: LdapSessionOptions) -> QueryClientCertificateCallback
        Set: QueryClientCertificate(self: LdapSessionOptions) = value
        """
        ...

    @property
    def ReferralCallback(self) -> ReferralCallback:
        """
        Get: ReferralCallback(self: LdapSessionOptions) -> ReferralCallback
        Set: ReferralCallback(self: LdapSessionOptions) = value
        """
        ...

    @property
    def ReferralChasing(self) -> ReferralChasingOptions:
        """
        Get: ReferralChasing(self: LdapSessionOptions) -> ReferralChasingOptions
        Set: ReferralChasing(self: LdapSessionOptions) = value
        """
        ...

    @property
    def ReferralHopLimit(self) -> int:
        """
        Get: ReferralHopLimit(self: LdapSessionOptions) -> int
        Set: ReferralHopLimit(self: LdapSessionOptions) = value
        """
        ...

    @property
    def RootDseCache(self) -> bool:
        """
        Get: RootDseCache(self: LdapSessionOptions) -> bool
        Set: RootDseCache(self: LdapSessionOptions) = value
        """
        ...

    @property
    def SaslMethod(self) -> str:
        """
        Get: SaslMethod(self: LdapSessionOptions) -> str
        Set: SaslMethod(self: LdapSessionOptions) = value
        """
        ...

    @property
    def Sealing(self) -> bool:
        """
        Get: Sealing(self: LdapSessionOptions) -> bool
        Set: Sealing(self: LdapSessionOptions) = value
        """
        ...

    @property
    def SecureSocketLayer(self) -> bool:
        """
        Get: SecureSocketLayer(self: LdapSessionOptions) -> bool
        Set: SecureSocketLayer(self: LdapSessionOptions) = value
        """
        ...

    @property
    def SecurityContext(self) -> object:
        """ Get: SecurityContext(self: LdapSessionOptions) -> object """
        ...

    @property
    def SendTimeout(self) -> TimeSpan:
        """
        Get: SendTimeout(self: LdapSessionOptions) -> TimeSpan
        Set: SendTimeout(self: LdapSessionOptions) = value
        """
        ...

    @property
    def Signing(self) -> bool:
        """
        Get: Signing(self: LdapSessionOptions) -> bool
        Set: Signing(self: LdapSessionOptions) = value
        """
        ...

    @property
    def SslInformation(self) -> SecurityPackageContextConnectionInformation:
        """ Get: SslInformation(self: LdapSessionOptions) -> SecurityPackageContextConnectionInformation """
        ...

    @property
    def SspiFlag(self) -> int:
        """
        Get: SspiFlag(self: LdapSessionOptions) -> int
        Set: SspiFlag(self: LdapSessionOptions) = value
        """
        ...

    @property
    def TcpKeepAlive(self) -> bool:
        """
        Get: TcpKeepAlive(self: LdapSessionOptions) -> bool
        Set: TcpKeepAlive(self: LdapSessionOptions) = value
        """
        ...

    @property
    def VerifyServerCertificate(self) -> VerifyServerCertificateCallback:
        """
        Get: VerifyServerCertificate(self: LdapSessionOptions) -> VerifyServerCertificateCallback
        Set: VerifyServerCertificate(self: LdapSessionOptions) = value
        """
        ...


    def FastConcurrentBind(self): # -> 
        """ FastConcurrentBind(self: LdapSessionOptions) """
        ...

    def StartTransportLayerSecurity(self, controls:DirectoryControlCollection): # -> 
        """ StartTransportLayerSecurity(self: LdapSessionOptions, controls: DirectoryControlCollection) """
        ...

    def StopTransportLayerSecurity(self): # -> 
        """ StopTransportLayerSecurity(self: LdapSessionOptions) """
        ...


class LocatorFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LocatorFlags, values: AvoidSelf (16384), DirectoryServicesPreferred (32), DirectoryServicesRequired (16), ForceRediscovery (1), GCRequired (64), GoodTimeServerPreferred (8192), IPRequired (512), IsDnsName (131072), IsFlatName (65536), KdcRequired (1024), None (0), OnlyLdapNeeded (32768), PdcRequired (128), ReturnDnsName (1073741824), ReturnFlatName (2147483648), TimeServerRequired (2048), WriteableRequired (4096) """
    AvoidSelf: LocatorFlags = ...
    DirectoryServicesPreferred: LocatorFlags = ...
    DirectoryServicesRequired: LocatorFlags = ...
    ForceRediscovery: LocatorFlags = ...
    GCRequired: LocatorFlags = ...
    GoodTimeServerPreferred: LocatorFlags = ...
    IPRequired: LocatorFlags = ...
    IsDnsName: LocatorFlags = ...
    IsFlatName: LocatorFlags = ...
    KdcRequired: LocatorFlags = ...
    OnlyLdapNeeded: LocatorFlags = ...
    PdcRequired: LocatorFlags = ...
    ReturnDnsName: LocatorFlags = ...
    ReturnFlatName: LocatorFlags = ...
    TimeServerRequired: LocatorFlags = ...
    value__ = ...
    WriteableRequired: LocatorFlags = ...


class ModifyDNRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    ModifyDNRequest()
    ModifyDNRequest(distinguishedName: str, newParentDistinguishedName: str, newName: str)
    """
    @property
    def DeleteOldRdn(self) -> bool:
        """
        Get: DeleteOldRdn(self: ModifyDNRequest) -> bool
        Set: DeleteOldRdn(self: ModifyDNRequest) = value
        """
        ...

    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: ModifyDNRequest) -> str
        Set: DistinguishedName(self: ModifyDNRequest) = value
        """
        ...

    @property
    def NewName(self) -> str:
        """
        Get: NewName(self: ModifyDNRequest) -> str
        Set: NewName(self: ModifyDNRequest) = value
        """
        ...

    @property
    def NewParentDistinguishedName(self) -> str:
        """
        Get: NewParentDistinguishedName(self: ModifyDNRequest) -> str
        Set: NewParentDistinguishedName(self: ModifyDNRequest) = value
        """
        ...


    def __new__(cls, distinguishedName:str = ..., newParentDistinguishedName:str = ..., newName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str, newParentDistinguishedName: str, newName: str)
        """
        ...


class ModifyDNResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ModifyRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    ModifyRequest()
    ModifyRequest(distinguishedName: str, *modifications: Array[DirectoryAttributeModification])
    ModifyRequest(distinguishedName: str, operation: DirectoryAttributeOperation, attributeName: str, *values: Array[object])
    """
    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: ModifyRequest) -> str
        Set: DistinguishedName(self: ModifyRequest) = value
        """
        ...

    @property
    def Modifications(self) -> DirectoryAttributeModificationCollection:
        """ Get: Modifications(self: ModifyRequest) -> DirectoryAttributeModificationCollection """
        ...


    def __new__(cls, distinguishedName:str = ..., *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str, *modifications: Array[DirectoryAttributeModification])
        __new__(cls: type, distinguishedName: str, operation: DirectoryAttributeOperation, attributeName: str, *values: Array[object])
        """
        ...


class ModifyResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    pass

class NotifyOfNewConnectionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ NotifyOfNewConnectionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, primaryConnection:LdapConnection, referralFromConnection:LdapConnection, newDistinguishedName:str, identifier:LdapDirectoryIdentifier, newConnection:LdapConnection, credential:NetworkCredential, currentUserToken:Int64, errorCodeFromBind:int, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: NotifyOfNewConnectionCallback, primaryConnection: LdapConnection, referralFromConnection: LdapConnection, newDistinguishedName: str, identifier: LdapDirectoryIdentifier, newConnection: LdapConnection, credential: NetworkCredential, currentUserToken: Int64, errorCodeFromBind: int, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: NotifyOfNewConnectionCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, primaryConnection:LdapConnection, referralFromConnection:LdapConnection, newDistinguishedName:str, identifier:LdapDirectoryIdentifier, newConnection:LdapConnection, credential:NetworkCredential, currentUserToken:Int64, errorCodeFromBind:int) -> bool:
        """ Invoke(self: NotifyOfNewConnectionCallback, primaryConnection: LdapConnection, referralFromConnection: LdapConnection, newDistinguishedName: str, identifier: LdapDirectoryIdentifier, newConnection: LdapConnection, credential: NetworkCredential, currentUserToken: Int64, errorCodeFromBind: int) -> bool """
        ...


class PageResultRequestControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    PageResultRequestControl()
    PageResultRequestControl(pageSize: int)
    PageResultRequestControl(cookie: Array[Byte])
    """
    @property
    def Cookie(self) -> Array:
        """
        Get: Cookie(self: PageResultRequestControl) -> Array[Byte]
        Set: Cookie(self: PageResultRequestControl) = value
        """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: PageResultRequestControl) -> int
        Set: PageSize(self: PageResultRequestControl) = value
        """
        ...



class PageResultResponseControl(DirectoryControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Cookie(self) -> Array:
        """ Get: Cookie(self: PageResultResponseControl) -> Array[Byte] """
        ...

    @property
    def TotalCount(self) -> int:
        """ Get: TotalCount(self: PageResultResponseControl) -> int """
        ...



class PartialResultProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PartialResultProcessing, values: NoPartialResultSupport (0), ReturnPartialResults (1), ReturnPartialResultsAndNotifyCallback (2) """
    NoPartialResultSupport: PartialResultProcessing = ...
    ReturnPartialResults: PartialResultProcessing = ...
    ReturnPartialResultsAndNotifyCallback: PartialResultProcessing = ...
    value__ = ...


class PartialResultsCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, value:object) -> bool:
        """ Contains(self: PartialResultsCollection, value: object) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: PartialResultsCollection, values: Array[object], index: int) """
        ...

    def IndexOf(self, value:object) -> int:
        """ IndexOf(self: PartialResultsCollection, value: object) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PermissiveModifyControl(DirectoryControl): # skipped bases: <type 'object'>
    """ PermissiveModifyControl() """
    pass

class QueryClientCertificateCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ QueryClientCertificateCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, connection:LdapConnection, trustedCAs:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: QueryClientCertificateCallback, connection: LdapConnection, trustedCAs: Array[Array[Byte]], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> X509Certificate:
        """ EndInvoke(self: QueryClientCertificateCallback, result: IAsyncResult) -> X509Certificate """
        ...

    def Invoke(self, connection:LdapConnection, trustedCAs:Array) -> X509Certificate:
        """ Invoke(self: QueryClientCertificateCallback, connection: LdapConnection, trustedCAs: Array[Array[Byte]]) -> X509Certificate """
        ...


class QueryForConnectionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ QueryForConnectionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, primaryConnection:LdapConnection, referralFromConnection:LdapConnection, newDistinguishedName:str, identifier:LdapDirectoryIdentifier, credential:NetworkCredential, currentUserToken:Int64, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: QueryForConnectionCallback, primaryConnection: LdapConnection, referralFromConnection: LdapConnection, newDistinguishedName: str, identifier: LdapDirectoryIdentifier, credential: NetworkCredential, currentUserToken: Int64, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> LdapConnection:
        """ EndInvoke(self: QueryForConnectionCallback, result: IAsyncResult) -> LdapConnection """
        ...

    def Invoke(self, primaryConnection:LdapConnection, referralFromConnection:LdapConnection, newDistinguishedName:str, identifier:LdapDirectoryIdentifier, credential:NetworkCredential, currentUserToken:Int64) -> LdapConnection:
        """ Invoke(self: QueryForConnectionCallback, primaryConnection: LdapConnection, referralFromConnection: LdapConnection, newDistinguishedName: str, identifier: LdapDirectoryIdentifier, credential: NetworkCredential, currentUserToken: Int64) -> LdapConnection """
        ...


class QuotaControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    QuotaControl()
    QuotaControl(querySid: SecurityIdentifier)
    """
    @property
    def QuerySid(self) -> SecurityIdentifier:
        """
        Get: QuerySid(self: QuotaControl) -> SecurityIdentifier
        Set: QuerySid(self: QuotaControl) = value
        """
        ...



class ReferralCallback: # skipped bases: <type 'object'>, <type 'object'>
    """ ReferralCallback() """
    @property
    def DereferenceConnection(self) -> DereferenceConnectionCallback:
        """
        Get: DereferenceConnection(self: ReferralCallback) -> DereferenceConnectionCallback
        Set: DereferenceConnection(self: ReferralCallback) = value
        """
        ...

    @property
    def NotifyNewConnection(self) -> NotifyOfNewConnectionCallback:
        """
        Get: NotifyNewConnection(self: ReferralCallback) -> NotifyOfNewConnectionCallback
        Set: NotifyNewConnection(self: ReferralCallback) = value
        """
        ...

    @property
    def QueryForConnection(self) -> QueryForConnectionCallback:
        """
        Get: QueryForConnection(self: ReferralCallback) -> QueryForConnectionCallback
        Set: QueryForConnection(self: ReferralCallback) = value
        """
        ...



class ReferralChasingOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ReferralChasingOptions, values: All (96), External (64), None (0), Subordinate (32) """
    All: ReferralChasingOptions = ...
    External: ReferralChasingOptions = ...
    Subordinate: ReferralChasingOptions = ...
    value__ = ...


class ResultCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResultCode, values: AdminLimitExceeded (11), AffectsMultipleDsas (71), AliasDereferencingProblem (36), AliasProblem (33), AttributeOrValueExists (20), AuthMethodNotSupported (7), Busy (51), CompareFalse (5), CompareTrue (6), ConfidentialityRequired (13), ConstraintViolation (19), EntryAlreadyExists (68), InappropriateAuthentication (48), InappropriateMatching (18), InsufficientAccessRights (50), InvalidAttributeSyntax (21), InvalidDNSyntax (34), LoopDetect (54), NamingViolation (64), NoSuchAttribute (16), NoSuchObject (32), NotAllowedOnNonLeaf (66), NotAllowedOnRdn (67), ObjectClassModificationsProhibited (69), ObjectClassViolation (65), OffsetRangeError (61), OperationsError (1), Other (80), ProtocolError (2), Referral (10), ReferralV2 (9), ResultsTooLarge (70), SaslBindInProgress (14), SizeLimitExceeded (4), SortControlMissing (60), StrongAuthRequired (8), Success (0), TimeLimitExceeded (3), Unavailable (52), UnavailableCriticalExtension (12), UndefinedAttributeType (17), UnwillingToPerform (53), VirtualListViewError (76) """
    AdminLimitExceeded: ResultCode = ...
    AffectsMultipleDsas: ResultCode = ...
    AliasDereferencingProblem: ResultCode = ...
    AliasProblem: ResultCode = ...
    AttributeOrValueExists: ResultCode = ...
    AuthMethodNotSupported: ResultCode = ...
    Busy: ResultCode = ...
    CompareFalse: ResultCode = ...
    CompareTrue: ResultCode = ...
    ConfidentialityRequired: ResultCode = ...
    ConstraintViolation: ResultCode = ...
    EntryAlreadyExists: ResultCode = ...
    InappropriateAuthentication: ResultCode = ...
    InappropriateMatching: ResultCode = ...
    InsufficientAccessRights: ResultCode = ...
    InvalidAttributeSyntax: ResultCode = ...
    InvalidDNSyntax: ResultCode = ...
    LoopDetect: ResultCode = ...
    NamingViolation: ResultCode = ...
    NoSuchAttribute: ResultCode = ...
    NoSuchObject: ResultCode = ...
    NotAllowedOnNonLeaf: ResultCode = ...
    NotAllowedOnRdn: ResultCode = ...
    ObjectClassModificationsProhibited: ResultCode = ...
    ObjectClassViolation: ResultCode = ...
    OffsetRangeError: ResultCode = ...
    OperationsError: ResultCode = ...
    Other: ResultCode = ...
    ProtocolError: ResultCode = ...
    Referral: ResultCode = ...
    ReferralV2: ResultCode = ...
    ResultsTooLarge: ResultCode = ...
    SaslBindInProgress: ResultCode = ...
    SizeLimitExceeded: ResultCode = ...
    SortControlMissing: ResultCode = ...
    StrongAuthRequired: ResultCode = ...
    Success: ResultCode = ...
    TimeLimitExceeded: ResultCode = ...
    Unavailable: ResultCode = ...
    UnavailableCriticalExtension: ResultCode = ...
    UndefinedAttributeType: ResultCode = ...
    UnwillingToPerform: ResultCode = ...
    value__ = ...
    VirtualListViewError: ResultCode = ...


class SearchOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchOption, values: DomainScope (1), PhantomRoot (2) """
    DomainScope: SearchOption = ...
    PhantomRoot: SearchOption = ...
    value__ = ...


class SearchOptionsControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    SearchOptionsControl()
    SearchOptionsControl(flags: SearchOption)
    """
    @property
    def SearchOption(self) -> SearchOption:
        """
        Get: SearchOption(self: SearchOptionsControl) -> SearchOption
        Set: SearchOption(self: SearchOptionsControl) = value
        """
        ...



class SearchRequest(DirectoryRequest): # skipped bases: <type 'object'>
    """
    SearchRequest()
    SearchRequest(distinguishedName: str, filter: XmlDocument, searchScope: SearchScope, *attributeList: Array[str])
    SearchRequest(distinguishedName: str, ldapFilter: str, searchScope: SearchScope, *attributeList: Array[str])
    """
    @property
    def Aliases(self) -> DereferenceAlias:
        """
        Get: Aliases(self: SearchRequest) -> DereferenceAlias
        Set: Aliases(self: SearchRequest) = value
        """
        ...

    @property
    def Attributes(self) -> StringCollection:
        """ Get: Attributes(self: SearchRequest) -> StringCollection """
        ...

    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: SearchRequest) -> str
        Set: DistinguishedName(self: SearchRequest) = value
        """
        ...

    @property
    def Filter(self) -> object:
        """
        Get: Filter(self: SearchRequest) -> object
        Set: Filter(self: SearchRequest) = value
        """
        ...

    @property
    def Scope(self) -> SearchScope:
        """
        Get: Scope(self: SearchRequest) -> SearchScope
        Set: Scope(self: SearchRequest) = value
        """
        ...

    @property
    def SizeLimit(self) -> int:
        """
        Get: SizeLimit(self: SearchRequest) -> int
        Set: SizeLimit(self: SearchRequest) = value
        """
        ...

    @property
    def TimeLimit(self) -> TimeSpan:
        """
        Get: TimeLimit(self: SearchRequest) -> TimeSpan
        Set: TimeLimit(self: SearchRequest) = value
        """
        ...

    @property
    def TypesOnly(self) -> bool:
        """
        Get: TypesOnly(self: SearchRequest) -> bool
        Set: TypesOnly(self: SearchRequest) = value
        """
        ...


    def __new__(cls, distinguishedName=None, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, distinguishedName: str, filter: XmlDocument, searchScope: SearchScope, *attributeList: Array[str])
        __new__(cls: type, distinguishedName: str, ldapFilter: str, searchScope: SearchScope, *attributeList: Array[str])
        """
        ...


class SearchResponse(DirectoryResponse): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Entries(self) -> SearchResultEntryCollection:
        """ Get: Entries(self: SearchResponse) -> SearchResultEntryCollection """
        ...

    @property
    def References(self) -> SearchResultReferenceCollection:
        """ Get: References(self: SearchResponse) -> SearchResultReferenceCollection """
        ...



class SearchResultAttributeCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def AttributeNames(self) -> ICollection:
        """ Get: AttributeNames(self: SearchResultAttributeCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: SearchResultAttributeCollection) -> ICollection """
        ...


    def Contains(self, attributeName:str) -> bool:
        """ Contains(self: SearchResultAttributeCollection, attributeName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SearchResultEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> SearchResultAttributeCollection:
        """ Get: Attributes(self: SearchResultEntry) -> SearchResultAttributeCollection """
        ...

    @property
    def Controls(self) -> Array:
        """ Get: Controls(self: SearchResultEntry) -> Array[DirectoryControl] """
        ...

    @property
    def DistinguishedName(self) -> str:
        """ Get: DistinguishedName(self: SearchResultEntry) -> str """
        ...



class SearchResultEntryCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, value:SearchResultEntry) -> bool:
        """ Contains(self: SearchResultEntryCollection, value: SearchResultEntry) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: SearchResultEntryCollection, values: Array[SearchResultEntry], index: int) """
        ...

    def IndexOf(self, value:SearchResultEntry) -> int:
        """ IndexOf(self: SearchResultEntryCollection, value: SearchResultEntry) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SearchResultReference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Controls(self) -> Array:
        """ Get: Controls(self: SearchResultReference) -> Array[DirectoryControl] """
        ...

    @property
    def Reference(self) -> Array:
        """ Get: Reference(self: SearchResultReference) -> Array[Uri] """
        ...



class SearchResultReferenceCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, value:SearchResultReference) -> bool:
        """ Contains(self: SearchResultReferenceCollection, value: SearchResultReference) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: SearchResultReferenceCollection, values: Array[SearchResultReference], index: int) """
        ...

    def IndexOf(self, value:SearchResultReference) -> int:
        """ IndexOf(self: SearchResultReferenceCollection, value: SearchResultReference) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SearchScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchScope, values: Base (0), OneLevel (1), Subtree (2) """
    Base: SearchScope = ...
    OneLevel: SearchScope = ...
    Subtree: SearchScope = ...
    value__ = ...


class SecurityDescriptorFlagControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    SecurityDescriptorFlagControl()
    SecurityDescriptorFlagControl(masks: SecurityMasks)
    """
    @property
    def SecurityMasks(self) -> SecurityMasks:
        """
        Get: SecurityMasks(self: SecurityDescriptorFlagControl) -> SecurityMasks
        Set: SecurityMasks(self: SecurityDescriptorFlagControl) = value
        """
        ...



class SecurityMasks(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SecurityMasks, values: Dacl (4), Group (2), None (0), Owner (1), Sacl (8) """
    Dacl: SecurityMasks = ...
    Group: SecurityMasks = ...
    Owner: SecurityMasks = ...
    Sacl: SecurityMasks = ...
    value__ = ...


class SecurityPackageContextConnectionInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AlgorithmIdentifier(self) -> CipherAlgorithmType:
        """ Get: AlgorithmIdentifier(self: SecurityPackageContextConnectionInformation) -> CipherAlgorithmType """
        ...

    @property
    def CipherStrength(self) -> int:
        """ Get: CipherStrength(self: SecurityPackageContextConnectionInformation) -> int """
        ...

    @property
    def ExchangeStrength(self) -> int:
        """ Get: ExchangeStrength(self: SecurityPackageContextConnectionInformation) -> int """
        ...

    @property
    def Hash(self) -> HashAlgorithmType:
        """ Get: Hash(self: SecurityPackageContextConnectionInformation) -> HashAlgorithmType """
        ...

    @property
    def HashStrength(self) -> int:
        """ Get: HashStrength(self: SecurityPackageContextConnectionInformation) -> int """
        ...

    @property
    def KeyExchangeAlgorithm(self) -> int:
        """ Get: KeyExchangeAlgorithm(self: SecurityPackageContextConnectionInformation) -> int """
        ...

    @property
    def Protocol(self) -> SecurityProtocol:
        """ Get: Protocol(self: SecurityPackageContextConnectionInformation) -> SecurityProtocol """
        ...



class SecurityProtocol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityProtocol, values: Pct1Client (2), Pct1Server (1), Ssl2Client (8), Ssl2Server (4), Ssl3Client (32), Ssl3Server (16), Tls1Client (128), Tls1Server (64) """
    Pct1Client: SecurityProtocol = ...
    Pct1Server: SecurityProtocol = ...
    Ssl2Client: SecurityProtocol = ...
    Ssl2Server: SecurityProtocol = ...
    Ssl3Client: SecurityProtocol = ...
    Ssl3Server: SecurityProtocol = ...
    Tls1Client: SecurityProtocol = ...
    Tls1Server: SecurityProtocol = ...
    value__ = ...


class ShowDeletedControl(DirectoryControl): # skipped bases: <type 'object'>
    """ ShowDeletedControl() """
    pass

class SortKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    SortKey()
    SortKey(attributeName: str, matchingRule: str, reverseOrder: bool)
    """
    @property
    def AttributeName(self) -> str:
        """
        Get: AttributeName(self: SortKey) -> str
        Set: AttributeName(self: SortKey) = value
        """
        ...

    @property
    def MatchingRule(self) -> str:
        """
        Get: MatchingRule(self: SortKey) -> str
        Set: MatchingRule(self: SortKey) = value
        """
        ...

    @property
    def ReverseOrder(self) -> bool:
        """
        Get: ReverseOrder(self: SortKey) -> bool
        Set: ReverseOrder(self: SortKey) = value
        """
        ...



class SortRequestControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    SortRequestControl(*sortKeys: Array[SortKey])
    SortRequestControl(attributeName: str, reverseOrder: bool)
    SortRequestControl(attributeName: str, matchingRule: str, reverseOrder: bool)
    """
    @property
    def SortKeys(self) -> Array:
        """
        Get: SortKeys(self: SortRequestControl) -> Array[SortKey]
        Set: SortKeys(self: SortRequestControl) = value
        """
        ...



class SortResponseControl(DirectoryControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AttributeName(self) -> str:
        """ Get: AttributeName(self: SortResponseControl) -> str """
        ...

    @property
    def Result(self) -> ResultCode:
        """ Get: Result(self: SortResponseControl) -> ResultCode """
        ...



class TlsOperationException(DirectoryOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TlsOperationException()
    TlsOperationException(message: str)
    TlsOperationException(message: str, inner: Exception)
    TlsOperationException(response: DirectoryResponse)
    TlsOperationException(response: DirectoryResponse, message: str)
    TlsOperationException(response: DirectoryResponse, message: str, inner: Exception)
    """
    SerializeObjectState = ...


class TreeDeleteControl(DirectoryControl): # skipped bases: <type 'object'>
    """ TreeDeleteControl() """
    pass

class VerifyNameControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    VerifyNameControl()
    VerifyNameControl(serverName: str)
    VerifyNameControl(serverName: str, flag: int)
    """
    @property
    def Flag(self) -> int:
        """
        Get: Flag(self: VerifyNameControl) -> int
        Set: Flag(self: VerifyNameControl) = value
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Get: ServerName(self: VerifyNameControl) -> str
        Set: ServerName(self: VerifyNameControl) = value
        """
        ...



class VerifyServerCertificateCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ VerifyServerCertificateCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, connection:LdapConnection, certificate:X509Certificate, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: VerifyServerCertificateCallback, connection: LdapConnection, certificate: X509Certificate, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: VerifyServerCertificateCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, connection:LdapConnection, certificate:X509Certificate) -> bool:
        """ Invoke(self: VerifyServerCertificateCallback, connection: LdapConnection, certificate: X509Certificate) -> bool """
        ...


class VlvRequestControl(DirectoryControl): # skipped bases: <type 'object'>
    """
    VlvRequestControl()
    VlvRequestControl(beforeCount: int, afterCount: int, offset: int)
    VlvRequestControl(beforeCount: int, afterCount: int, target: str)
    VlvRequestControl(beforeCount: int, afterCount: int, target: Array[Byte])
    """
    @property
    def AfterCount(self) -> int:
        """
        Get: AfterCount(self: VlvRequestControl) -> int
        Set: AfterCount(self: VlvRequestControl) = value
        """
        ...

    @property
    def BeforeCount(self) -> int:
        """
        Get: BeforeCount(self: VlvRequestControl) -> int
        Set: BeforeCount(self: VlvRequestControl) = value
        """
        ...

    @property
    def ContextId(self) -> Array:
        """
        Get: ContextId(self: VlvRequestControl) -> Array[Byte]
        Set: ContextId(self: VlvRequestControl) = value
        """
        ...

    @property
    def EstimateCount(self) -> int:
        """
        Get: EstimateCount(self: VlvRequestControl) -> int
        Set: EstimateCount(self: VlvRequestControl) = value
        """
        ...

    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: VlvRequestControl) -> int
        Set: Offset(self: VlvRequestControl) = value
        """
        ...

    @property
    def Target(self) -> Array:
        """
        Get: Target(self: VlvRequestControl) -> Array[Byte]
        Set: Target(self: VlvRequestControl) = value
        """
        ...



class VlvResponseControl(DirectoryControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentCount(self) -> int:
        """ Get: ContentCount(self: VlvResponseControl) -> int """
        ...

    @property
    def ContextId(self) -> Array:
        """ Get: ContextId(self: VlvResponseControl) -> Array[Byte] """
        ...

    @property
    def Result(self) -> ResultCode:
        """ Get: Result(self: VlvResponseControl) -> ResultCode """
        ...

    @property
    def TargetPosition(self) -> int:
        """ Get: TargetPosition(self: VlvResponseControl) -> int """
        ...



