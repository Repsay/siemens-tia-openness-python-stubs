# encoding: utf-8
# module System.Security.Cryptography.Xml calls itself Xml
# from System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Type

from System.Collections import (ArrayList, Hashtable, ICollection, 
    IEnumerable, IEnumerator, IList)

from System.IO import Stream

from System.Messaging import HashAlgorithm

from System.Security.Cryptography import (AsymmetricAlgorithm, CipherMode, 
    DSA, KeyedHashAlgorithm, PaddingMode, RSA, SymmetricAlgorithm)

from System.Security.Cryptography.X509Certificates import (X509Certificate, 
    X509Certificate2)

from System.Security.Policy import Evidence

from System.Text import Encoding

from System.Xml import XmlDocument, XmlElement, XmlNodeList, XmlResolver

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: Func, field#
"""

# no functions
# classes

class CipherData: # skipped bases: <type 'object'>, <type 'object'>
    """
    CipherData()
    CipherData(cipherValue: Array[Byte])
    CipherData(cipherReference: CipherReference)
    """
    @property
    def CipherReference(self) -> CipherReference:
        """
        Get: CipherReference(self: CipherData) -> CipherReference
        Set: CipherReference(self: CipherData) = value
        """
        ...

    @property
    def CipherValue(self) -> Array:
        """
        Get: CipherValue(self: CipherData) -> Array[Byte]
        Set: CipherValue(self: CipherData) = value
        """
        ...


    def GetXml(self) -> XmlElement:
        """ GetXml(self: CipherData) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: CipherData, value: XmlElement) """
        ...


class EncryptedReference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CacheValid(self):
        ...

    @property
    def ReferenceType(self):
        ...

    @property
    def TransformChain(self) -> TransformChain:
        """
        Get: TransformChain(self: EncryptedReference) -> TransformChain
        Set: TransformChain(self: EncryptedReference) = value
        """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: EncryptedReference) -> str
        Set: Uri(self: EncryptedReference) = value
        """
        ...


    def AddTransform(self, transform:Transform): # -> 
        """ AddTransform(self: EncryptedReference, transform: Transform) """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: EncryptedReference) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: EncryptedReference, value: XmlElement) """
        ...


class CipherReference(EncryptedReference): # skipped bases: <type 'object'>
    """
    CipherReference()
    CipherReference(uri: str)
    CipherReference(uri: str, transformChain: TransformChain)
    """
    pass

class DataObject: # skipped bases: <type 'object'>, <type 'object'>
    """
    DataObject()
    DataObject(id: str, mimeType: str, encoding: str, data: XmlElement)
    """
    @property
    def Data(self) -> XmlNodeList:
        """
        Get: Data(self: DataObject) -> XmlNodeList
        Set: Data(self: DataObject) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: DataObject) -> str
        Set: Encoding(self: DataObject) = value
        """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: DataObject) -> str
        Set: Id(self: DataObject) = value
        """
        ...

    @property
    def MimeType(self) -> str:
        """
        Get: MimeType(self: DataObject) -> str
        Set: MimeType(self: DataObject) = value
        """
        ...


    def GetXml(self) -> XmlElement:
        """ GetXml(self: DataObject) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: DataObject, value: XmlElement) """
        ...


class DataReference(EncryptedReference): # skipped bases: <type 'object'>
    """
    DataReference()
    DataReference(uri: str)
    DataReference(uri: str, transformChain: TransformChain)
    """
    pass

class KeyInfoClause: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetXml(self) -> XmlElement:
        """ GetXml(self: KeyInfoClause) -> XmlElement """
        ...

    def LoadXml(self, element:XmlElement): # -> 
        """ LoadXml(self: KeyInfoClause, element: XmlElement) """
        ...


class DSAKeyValue(KeyInfoClause): # skipped bases: <type 'object'>
    """
    DSAKeyValue()
    DSAKeyValue(key: DSA)
    """
    @property
    def Key(self) -> DSA:
        """
        Get: Key(self: DSAKeyValue) -> DSA
        Set: Key(self: DSAKeyValue) = value
        """
        ...


    def __new__(cls, key:DSA = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: DSA)
        """
        ...


class EncryptedType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CipherData(self) -> CipherData:
        """
        Get: CipherData(self: EncryptedType) -> CipherData
        Set: CipherData(self: EncryptedType) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: EncryptedType) -> str
        Set: Encoding(self: EncryptedType) = value
        """
        ...

    @property
    def EncryptionMethod(self) -> EncryptionMethod:
        """
        Get: EncryptionMethod(self: EncryptedType) -> EncryptionMethod
        Set: EncryptionMethod(self: EncryptedType) = value
        """
        ...

    @property
    def EncryptionProperties(self) -> EncryptionPropertyCollection:
        """ Get: EncryptionProperties(self: EncryptedType) -> EncryptionPropertyCollection """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: EncryptedType) -> str
        Set: Id(self: EncryptedType) = value
        """
        ...

    @property
    def KeyInfo(self) -> KeyInfo:
        """
        Get: KeyInfo(self: EncryptedType) -> KeyInfo
        Set: KeyInfo(self: EncryptedType) = value
        """
        ...

    @property
    def MimeType(self) -> str:
        """
        Get: MimeType(self: EncryptedType) -> str
        Set: MimeType(self: EncryptedType) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: EncryptedType) -> str
        Set: Type(self: EncryptedType) = value
        """
        ...


    def AddProperty(self, ep:EncryptionProperty): # -> 
        """ AddProperty(self: EncryptedType, ep: EncryptionProperty) """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: EncryptedType) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: EncryptedType, value: XmlElement) """
        ...


class EncryptedData(EncryptedType): # skipped bases: <type 'object'>
    """ EncryptedData() """
    pass

class EncryptedKey(EncryptedType): # skipped bases: <type 'object'>
    """ EncryptedKey() """
    @property
    def CarriedKeyName(self) -> str:
        """
        Get: CarriedKeyName(self: EncryptedKey) -> str
        Set: CarriedKeyName(self: EncryptedKey) = value
        """
        ...

    @property
    def Recipient(self) -> str:
        """
        Get: Recipient(self: EncryptedKey) -> str
        Set: Recipient(self: EncryptedKey) = value
        """
        ...

    @property
    def ReferenceList(self) -> ReferenceList:
        """ Get: ReferenceList(self: EncryptedKey) -> ReferenceList """
        ...


    def AddReference(self, *__args:DataReference): # -> 
        """ AddReference(self: EncryptedKey, dataReference: DataReference)AddReference(self: EncryptedKey, keyReference: KeyReference) """
        ...


class EncryptedXml: # skipped bases: <type 'object'>, <type 'object'>
    """
    EncryptedXml()
    EncryptedXml(document: XmlDocument)
    EncryptedXml(document: XmlDocument, evidence: Evidence)
    """
    @property
    def DocumentEvidence(self) -> Evidence:
        """
        Get: DocumentEvidence(self: EncryptedXml) -> Evidence
        Set: DocumentEvidence(self: EncryptedXml) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: EncryptedXml) -> Encoding
        Set: Encoding(self: EncryptedXml) = value
        """
        ...

    @property
    def Mode(self) -> CipherMode:
        """
        Get: Mode(self: EncryptedXml) -> CipherMode
        Set: Mode(self: EncryptedXml) = value
        """
        ...

    @property
    def Padding(self) -> PaddingMode:
        """
        Get: Padding(self: EncryptedXml) -> PaddingMode
        Set: Padding(self: EncryptedXml) = value
        """
        ...

    @property
    def Recipient(self) -> str:
        """
        Get: Recipient(self: EncryptedXml) -> str
        Set: Recipient(self: EncryptedXml) = value
        """
        ...

    @property
    def Resolver(self) -> XmlResolver:
        """
        Get: Resolver(self: EncryptedXml) -> XmlResolver
        Set: Resolver(self: EncryptedXml) = value
        """
        ...

    @property
    def XmlDSigSearchDepth(self) -> int:
        """
        Get: XmlDSigSearchDepth(self: EncryptedXml) -> int
        Set: XmlDSigSearchDepth(self: EncryptedXml) = value
        """
        ...


    def AddKeyNameMapping(self, keyName:str, keyObject:object): # -> 
        """ AddKeyNameMapping(self: EncryptedXml, keyName: str, keyObject: object) """
        ...

    def ClearKeyNameMappings(self): # -> 
        """ ClearKeyNameMappings(self: EncryptedXml) """
        ...

    def DecryptData(self, encryptedData:EncryptedData, symmetricAlgorithm:SymmetricAlgorithm) -> Array:
        """ DecryptData(self: EncryptedXml, encryptedData: EncryptedData, symmetricAlgorithm: SymmetricAlgorithm) -> Array[Byte] """
        ...

    def DecryptDocument(self): # -> 
        """ DecryptDocument(self: EncryptedXml) """
        ...

    def DecryptEncryptedKey(self, encryptedKey:EncryptedKey) -> Array:
        """ DecryptEncryptedKey(self: EncryptedXml, encryptedKey: EncryptedKey) -> Array[Byte] """
        ...

    @staticmethod
    def DecryptKey(keyData:Array, *__args:SymmetricAlgorithm) -> Array:
        """
        DecryptKey(keyData: Array[Byte], symmetricAlgorithm: SymmetricAlgorithm) -> Array[Byte]
        DecryptKey(keyData: Array[Byte], rsa: RSA, useOAEP: bool) -> Array[Byte]
        """
        ...

    def Encrypt(self, inputElement:XmlElement, *__args:X509Certificate2) -> EncryptedData:
        """
        Encrypt(self: EncryptedXml, inputElement: XmlElement, certificate: X509Certificate2) -> EncryptedData
        Encrypt(self: EncryptedXml, inputElement: XmlElement, keyName: str) -> EncryptedData
        """
        ...

    def EncryptData(self, *__args) -> Array:
        """
        EncryptData(self: EncryptedXml, plaintext: Array[Byte], symmetricAlgorithm: SymmetricAlgorithm) -> Array[Byte]
        EncryptData(self: EncryptedXml, inputElement: XmlElement, symmetricAlgorithm: SymmetricAlgorithm, content: bool) -> Array[Byte]
        """
        ...

    @staticmethod
    def EncryptKey(keyData:Array, *__args:SymmetricAlgorithm) -> Array:
        """
        EncryptKey(keyData: Array[Byte], symmetricAlgorithm: SymmetricAlgorithm) -> Array[Byte]
        EncryptKey(keyData: Array[Byte], rsa: RSA, useOAEP: bool) -> Array[Byte]
        """
        ...

    def GetDecryptionIV(self, encryptedData:EncryptedData, symmetricAlgorithmUri:str) -> Array:
        """ GetDecryptionIV(self: EncryptedXml, encryptedData: EncryptedData, symmetricAlgorithmUri: str) -> Array[Byte] """
        ...

    def GetDecryptionKey(self, encryptedData:EncryptedData, symmetricAlgorithmUri:str) -> SymmetricAlgorithm:
        """ GetDecryptionKey(self: EncryptedXml, encryptedData: EncryptedData, symmetricAlgorithmUri: str) -> SymmetricAlgorithm """
        ...

    def GetIdElement(self, document:XmlDocument, idValue:str) -> XmlElement:
        """ GetIdElement(self: EncryptedXml, document: XmlDocument, idValue: str) -> XmlElement """
        ...

    def ReplaceData(self, inputElement:XmlElement, decryptedData:Array): # -> 
        """ ReplaceData(self: EncryptedXml, inputElement: XmlElement, decryptedData: Array[Byte]) """
        ...

    @staticmethod
    def ReplaceElement(inputElement:XmlElement, encryptedData:EncryptedData, content:bool): # -> 
        """ ReplaceElement(inputElement: XmlElement, encryptedData: EncryptedData, content: bool) """
        ...

    XmlEncAES128KeyWrapUrl: str = ...
    XmlEncAES128Url: str = ...
    XmlEncAES192KeyWrapUrl: str = ...
    XmlEncAES192Url: str = ...
    XmlEncAES256KeyWrapUrl: str = ...
    XmlEncAES256Url: str = ...
    XmlEncDESUrl: str = ...
    XmlEncElementContentUrl: str = ...
    XmlEncElementUrl: str = ...
    XmlEncEncryptedKeyUrl: str = ...
    XmlEncNamespaceUrl: str = ...
    XmlEncRSA15Url: str = ...
    XmlEncRSAOAEPUrl: str = ...
    XmlEncSHA256Url: str = ...
    XmlEncSHA512Url: str = ...
    XmlEncTripleDESKeyWrapUrl: str = ...
    XmlEncTripleDESUrl: str = ...


class EncryptionMethod: # skipped bases: <type 'object'>, <type 'object'>
    """
    EncryptionMethod()
    EncryptionMethod(algorithm: str)
    """
    @property
    def KeyAlgorithm(self) -> str:
        """
        Get: KeyAlgorithm(self: EncryptionMethod) -> str
        Set: KeyAlgorithm(self: EncryptionMethod) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: EncryptionMethod) -> int
        Set: KeySize(self: EncryptionMethod) = value
        """
        ...


    def GetXml(self) -> XmlElement:
        """ GetXml(self: EncryptionMethod) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: EncryptionMethod, value: XmlElement) """
        ...


class EncryptionProperty: # skipped bases: <type 'object'>, <type 'object'>
    """
    EncryptionProperty()
    EncryptionProperty(elementProperty: XmlElement)
    """
    @property
    def Id(self) -> str:
        """ Get: Id(self: EncryptionProperty) -> str """
        ...

    @property
    def PropertyElement(self) -> XmlElement:
        """
        Get: PropertyElement(self: EncryptionProperty) -> XmlElement
        Set: PropertyElement(self: EncryptionProperty) = value
        """
        ...

    @property
    def Target(self) -> str:
        """ Get: Target(self: EncryptionProperty) -> str """
        ...


    def GetXml(self) -> XmlElement:
        """ GetXml(self: EncryptionProperty) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: EncryptionProperty, value: XmlElement) """
        ...


class EncryptionPropertyCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ EncryptionPropertyCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: EncryptionPropertyCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: EncryptionPropertyCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: EncryptionPropertyCollection) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: EncryptionPropertyCollection, array: Array, index: int)CopyTo(self: EncryptionPropertyCollection, array: Array[EncryptionProperty], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: EncryptionPropertyCollection) -> IEnumerator """
        ...

    def Item(self, index:int) -> EncryptionProperty:
        """ Item(self: EncryptionPropertyCollection, index: int) -> EncryptionProperty """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class IRelDecryptor: # skipped bases: <type 'object'>
    """ no doc """
    def Decrypt(self, encryptionMethod:EncryptionMethod, keyInfo:KeyInfo, toDecrypt:Stream) -> Stream:
        """ Decrypt(self: IRelDecryptor, encryptionMethod: EncryptionMethod, keyInfo: KeyInfo, toDecrypt: Stream) -> Stream """
        ...


class KeyInfo(IEnumerable): # skipped bases: <type 'object'>
    """ KeyInfo() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: KeyInfo) -> int """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: KeyInfo) -> str
        Set: Id(self: KeyInfo) = value
        """
        ...


    def AddClause(self, clause:KeyInfoClause): # -> 
        """ AddClause(self: KeyInfo, clause: KeyInfoClause) """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: KeyInfo) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: KeyInfo, value: XmlElement) """
        ...


class KeyInfoEncryptedKey(KeyInfoClause): # skipped bases: <type 'object'>
    """
    KeyInfoEncryptedKey()
    KeyInfoEncryptedKey(encryptedKey: EncryptedKey)
    """
    @property
    def EncryptedKey(self) -> EncryptedKey:
        """
        Get: EncryptedKey(self: KeyInfoEncryptedKey) -> EncryptedKey
        Set: EncryptedKey(self: KeyInfoEncryptedKey) = value
        """
        ...


    def __new__(cls, encryptedKey:EncryptedKey = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, encryptedKey: EncryptedKey)
        """
        ...


class KeyInfoName(KeyInfoClause): # skipped bases: <type 'object'>
    """
    KeyInfoName()
    KeyInfoName(keyName: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: KeyInfoName) -> str
        Set: Value(self: KeyInfoName) = value
        """
        ...


    def __new__(cls, keyName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keyName: str)
        """
        ...


class KeyInfoNode(KeyInfoClause): # skipped bases: <type 'object'>
    """
    KeyInfoNode()
    KeyInfoNode(node: XmlElement)
    """
    @property
    def Value(self) -> XmlElement:
        """
        Get: Value(self: KeyInfoNode) -> XmlElement
        Set: Value(self: KeyInfoNode) = value
        """
        ...


    def __new__(cls, node:XmlElement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, node: XmlElement)
        """
        ...


class KeyInfoRetrievalMethod(KeyInfoClause): # skipped bases: <type 'object'>
    """
    KeyInfoRetrievalMethod()
    KeyInfoRetrievalMethod(strUri: str)
    KeyInfoRetrievalMethod(strUri: str, typeName: str)
    """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: KeyInfoRetrievalMethod) -> str
        Set: Type(self: KeyInfoRetrievalMethod) = value
        """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: KeyInfoRetrievalMethod) -> str
        Set: Uri(self: KeyInfoRetrievalMethod) = value
        """
        ...


    def __new__(cls, strUri:str = ..., typeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, strUri: str)
        __new__(cls: type, strUri: str, typeName: str)
        """
        ...


class KeyInfoX509Data(KeyInfoClause): # skipped bases: <type 'object'>
    """
    KeyInfoX509Data()
    KeyInfoX509Data(rgbCert: Array[Byte])
    KeyInfoX509Data(cert: X509Certificate)
    KeyInfoX509Data(cert: X509Certificate, includeOption: X509IncludeOption)
    """
    @property
    def Certificates(self) -> ArrayList:
        """ Get: Certificates(self: KeyInfoX509Data) -> ArrayList """
        ...

    @property
    def CRL(self) -> Array:
        """
        Get: CRL(self: KeyInfoX509Data) -> Array[Byte]
        Set: CRL(self: KeyInfoX509Data) = value
        """
        ...

    @property
    def IssuerSerials(self) -> ArrayList:
        """ Get: IssuerSerials(self: KeyInfoX509Data) -> ArrayList """
        ...

    @property
    def SubjectKeyIds(self) -> ArrayList:
        """ Get: SubjectKeyIds(self: KeyInfoX509Data) -> ArrayList """
        ...

    @property
    def SubjectNames(self) -> ArrayList:
        """ Get: SubjectNames(self: KeyInfoX509Data) -> ArrayList """
        ...


    def AddCertificate(self, certificate:X509Certificate): # -> 
        """ AddCertificate(self: KeyInfoX509Data, certificate: X509Certificate) """
        ...

    def AddIssuerSerial(self, issuerName:str, serialNumber:str): # -> 
        """ AddIssuerSerial(self: KeyInfoX509Data, issuerName: str, serialNumber: str) """
        ...

    def AddSubjectKeyId(self, subjectKeyId:Array): # -> 
        """ AddSubjectKeyId(self: KeyInfoX509Data, subjectKeyId: Array[Byte])AddSubjectKeyId(self: KeyInfoX509Data, subjectKeyId: str) """
        ...

    def AddSubjectName(self, subjectName:str): # -> 
        """ AddSubjectName(self: KeyInfoX509Data, subjectName: str) """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, rgbCert: Array[Byte])
        __new__(cls: type, cert: X509Certificate)
        __new__(cls: type, cert: X509Certificate, includeOption: X509IncludeOption)
        """
        ...


class KeyReference(EncryptedReference): # skipped bases: <type 'object'>
    """
    KeyReference()
    KeyReference(uri: str)
    KeyReference(uri: str, transformChain: TransformChain)
    """
    pass

class Reference: # skipped bases: <type 'object'>, <type 'object'>
    """
    Reference()
    Reference(stream: Stream)
    Reference(uri: str)
    """
    @property
    def DigestMethod(self) -> str:
        """
        Get: DigestMethod(self: Reference) -> str
        Set: DigestMethod(self: Reference) = value
        """
        ...

    @property
    def DigestValue(self) -> Array:
        """
        Get: DigestValue(self: Reference) -> Array[Byte]
        Set: DigestValue(self: Reference) = value
        """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: Reference) -> str
        Set: Id(self: Reference) = value
        """
        ...

    @property
    def TransformChain(self) -> TransformChain:
        """
        Get: TransformChain(self: Reference) -> TransformChain
        Set: TransformChain(self: Reference) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: Reference) -> str
        Set: Type(self: Reference) = value
        """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: Reference) -> str
        Set: Uri(self: Reference) = value
        """
        ...


    def AddTransform(self, transform:Transform): # -> 
        """ AddTransform(self: Reference, transform: Transform) """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: Reference) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: Reference, value: XmlElement) """
        ...


class ReferenceList(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ReferenceList() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReferenceList) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: ReferenceList) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: ReferenceList) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ReferenceList, array: Array, index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReferenceList) -> IEnumerator """
        ...

    def Item(self, index:int) -> EncryptedReference:
        """ Item(self: ReferenceList, index: int) -> EncryptedReference """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class RSAKeyValue(KeyInfoClause): # skipped bases: <type 'object'>
    """
    RSAKeyValue()
    RSAKeyValue(key: RSA)
    """
    @property
    def Key(self) -> RSA:
        """
        Get: Key(self: RSAKeyValue) -> RSA
        Set: Key(self: RSAKeyValue) = value
        """
        ...


    def __new__(cls, key:RSA = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: RSA)
        """
        ...


class Signature: # skipped bases: <type 'object'>, <type 'object'>
    """ Signature() """
    @property
    def Id(self) -> str:
        """
        Get: Id(self: Signature) -> str
        Set: Id(self: Signature) = value
        """
        ...

    @property
    def KeyInfo(self) -> KeyInfo:
        """
        Get: KeyInfo(self: Signature) -> KeyInfo
        Set: KeyInfo(self: Signature) = value
        """
        ...

    @property
    def ObjectList(self) -> IList:
        """
        Get: ObjectList(self: Signature) -> IList
        Set: ObjectList(self: Signature) = value
        """
        ...

    @property
    def SignatureValue(self) -> Array:
        """
        Get: SignatureValue(self: Signature) -> Array[Byte]
        Set: SignatureValue(self: Signature) = value
        """
        ...

    @property
    def SignedInfo(self) -> SignedInfo:
        """
        Get: SignedInfo(self: Signature) -> SignedInfo
        Set: SignedInfo(self: Signature) = value
        """
        ...


    def AddObject(self, dataObject:DataObject): # -> 
        """ AddObject(self: Signature, dataObject: DataObject) """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: Signature) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: Signature, value: XmlElement) """
        ...


class SignedInfo(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ SignedInfo() """
    @property
    def CanonicalizationMethod(self) -> str:
        """
        Get: CanonicalizationMethod(self: SignedInfo) -> str
        Set: CanonicalizationMethod(self: SignedInfo) = value
        """
        ...

    @property
    def CanonicalizationMethodObject(self) -> Transform:
        """ Get: CanonicalizationMethodObject(self: SignedInfo) -> Transform """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SignedInfo) -> str
        Set: Id(self: SignedInfo) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SignedInfo) -> bool """
        ...

    @property
    def References(self) -> ArrayList:
        """ Get: References(self: SignedInfo) -> ArrayList """
        ...

    @property
    def SignatureLength(self) -> str:
        """
        Get: SignatureLength(self: SignedInfo) -> str
        Set: SignatureLength(self: SignedInfo) = value
        """
        ...

    @property
    def SignatureMethod(self) -> str:
        """
        Get: SignatureMethod(self: SignedInfo) -> str
        Set: SignatureMethod(self: SignedInfo) = value
        """
        ...


    def AddReference(self, reference:Reference): # -> 
        """ AddReference(self: SignedInfo, reference: Reference) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SignedInfo) -> IEnumerator """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: SignedInfo) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: SignedInfo, value: XmlElement) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SignedXml: # skipped bases: <type 'object'>, <type 'object'>
    """
    SignedXml()
    SignedXml(document: XmlDocument)
    SignedXml(elem: XmlElement)
    """
    @property
    def EncryptedXml(self) -> EncryptedXml:
        """
        Get: EncryptedXml(self: SignedXml) -> EncryptedXml
        Set: EncryptedXml(self: SignedXml) = value
        """
        ...

    @property
    def KeyInfo(self) -> KeyInfo:
        """
        Get: KeyInfo(self: SignedXml) -> KeyInfo
        Set: KeyInfo(self: SignedXml) = value
        """
        ...

    @property
    def Resolver(self): # -> 
        """ Set: Resolver(self: SignedXml) = value """
        ...

    @property
    def SafeCanonicalizationMethods(self) -> Collection:
        """ Get: SafeCanonicalizationMethods(self: SignedXml) -> Collection[str] """
        ...

    @property
    def Signature(self) -> Signature:
        """ Get: Signature(self: SignedXml) -> Signature """
        ...

    @property
    def SignatureFormatValidator(self): # -> Func
        """
        Get: SignatureFormatValidator(self: SignedXml) -> Func[SignedXml, bool]
        Set: SignatureFormatValidator(self: SignedXml) = value
        """
        ...

    @property
    def SignatureLength(self) -> str:
        """ Get: SignatureLength(self: SignedXml) -> str """
        ...

    @property
    def SignatureMethod(self) -> str:
        """ Get: SignatureMethod(self: SignedXml) -> str """
        ...

    @property
    def SignatureValue(self) -> Array:
        """ Get: SignatureValue(self: SignedXml) -> Array[Byte] """
        ...

    @property
    def SignedInfo(self) -> SignedInfo:
        """ Get: SignedInfo(self: SignedXml) -> SignedInfo """
        ...

    @property
    def SigningKey(self) -> AsymmetricAlgorithm:
        """
        Get: SigningKey(self: SignedXml) -> AsymmetricAlgorithm
        Set: SigningKey(self: SignedXml) = value
        """
        ...

    @property
    def SigningKeyName(self) -> str:
        """
        Get: SigningKeyName(self: SignedXml) -> str
        Set: SigningKeyName(self: SignedXml) = value
        """
        ...


    def AddObject(self, dataObject:DataObject): # -> 
        """ AddObject(self: SignedXml, dataObject: DataObject) """
        ...

    def AddReference(self, reference:Reference): # -> 
        """ AddReference(self: SignedXml, reference: Reference) """
        ...

    def CheckSignature(self, *__args:AsymmetricAlgorithm) -> bool:
        """
        CheckSignature(self: SignedXml) -> bool
        CheckSignature(self: SignedXml, key: AsymmetricAlgorithm) -> bool
        CheckSignature(self: SignedXml, macAlg: KeyedHashAlgorithm) -> bool
        CheckSignature(self: SignedXml, certificate: X509Certificate2, verifySignatureOnly: bool) -> bool
        """
        ...

    def CheckSignatureReturningKey(self, signingKey) -> Tuple_[bool, AsymmetricAlgorithm]:
        """ CheckSignatureReturningKey(self: SignedXml) -> (bool, AsymmetricAlgorithm) """
        ...

    def ComputeSignature(self, macAlg:KeyedHashAlgorithm = ...): # -> 
        """ ComputeSignature(self: SignedXml)ComputeSignature(self: SignedXml, macAlg: KeyedHashAlgorithm) """
        ...

    def GetIdElement(self, document:XmlDocument, idValue:str) -> XmlElement:
        """ GetIdElement(self: SignedXml, document: XmlDocument, idValue: str) -> XmlElement """
        ...

    def GetPublicKey(self, *args): #cannot find CLR method
        """ GetPublicKey(self: SignedXml) -> AsymmetricAlgorithm """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: SignedXml) -> XmlElement """
        ...

    def LoadXml(self, value:XmlElement): # -> 
        """ LoadXml(self: SignedXml, value: XmlElement) """
        ...

    m_signature = ...
    m_strSigningKeyName = ...
    XmlDecryptionTransformUrl: str = ...
    XmlDsigBase64TransformUrl: str = ...
    XmlDsigC14NTransformUrl: str = ...
    XmlDsigC14NWithCommentsTransformUrl: str = ...
    XmlDsigCanonicalizationUrl: str = ...
    XmlDsigCanonicalizationWithCommentsUrl: str = ...
    XmlDsigDSAUrl: str = ...
    XmlDsigEnvelopedSignatureTransformUrl: str = ...
    XmlDsigExcC14NTransformUrl: str = ...
    XmlDsigExcC14NWithCommentsTransformUrl: str = ...
    XmlDsigHMACSHA1Url: str = ...
    XmlDsigMinimalCanonicalizationUrl: str = ...
    XmlDsigNamespaceUrl: str = ...
    XmlDsigRSASHA1Url: str = ...
    XmlDsigRSASHA256Url: str = ...
    XmlDsigRSASHA384Url: str = ...
    XmlDsigRSASHA512Url: str = ...
    XmlDsigSHA1Url: str = ...
    XmlDsigSHA256Url: str = ...
    XmlDsigSHA384Url: str = ...
    XmlDsigSHA512Url: str = ...
    XmlDsigXPathTransformUrl: str = ...
    XmlDsigXsltTransformUrl: str = ...
    XmlLicenseTransformUrl: str = ...


class Transform: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Algorithm(self) -> str:
        """
        Get: Algorithm(self: Transform) -> str
        Set: Algorithm(self: Transform) = value
        """
        ...

    @property
    def Context(self) -> XmlElement:
        """
        Get: Context(self: Transform) -> XmlElement
        Set: Context(self: Transform) = value
        """
        ...

    @property
    def InputTypes(self) -> Array:
        """ Get: InputTypes(self: Transform) -> Array[Type] """
        ...

    @property
    def OutputTypes(self) -> Array:
        """ Get: OutputTypes(self: Transform) -> Array[Type] """
        ...

    @property
    def PropagatedNamespaces(self) -> Hashtable:
        """ Get: PropagatedNamespaces(self: Transform) -> Hashtable """
        ...

    @property
    def Resolver(self): # -> 
        """ Set: Resolver(self: Transform) = value """
        ...


    def GetDigestedOutput(self, hash:HashAlgorithm) -> Array:
        """ GetDigestedOutput(self: Transform, hash: HashAlgorithm) -> Array[Byte] """
        ...

    def GetInnerXml(self, *args): #cannot find CLR method
        """ GetInnerXml(self: Transform) -> XmlNodeList """
        ...

    def GetOutput(self, type:Type = ...) -> object:
        """
        GetOutput(self: Transform) -> object
        GetOutput(self: Transform, type: Type) -> object
        """
        ...

    def GetXml(self) -> XmlElement:
        """ GetXml(self: Transform) -> XmlElement """
        ...

    def LoadInnerXml(self, nodeList:XmlNodeList): # -> 
        """ LoadInnerXml(self: Transform, nodeList: XmlNodeList) """
        ...

    def LoadInput(self, obj:object): # -> 
        """ LoadInput(self: Transform, obj: object) """
        ...


class TransformChain: # skipped bases: <type 'object'>, <type 'object'>
    """ TransformChain() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: TransformChain) -> int """
        ...


    def Add(self, transform:Transform): # -> 
        """ Add(self: TransformChain, transform: Transform) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TransformChain) -> IEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class X509IssuerSerial: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IssuerName(self) -> str:
        """
        Get: IssuerName(self: X509IssuerSerial) -> str
        Set: IssuerName(self: X509IssuerSerial) = value
        """
        ...

    @property
    def SerialNumber(self) -> str:
        """
        Get: SerialNumber(self: X509IssuerSerial) -> str
        Set: SerialNumber(self: X509IssuerSerial) = value
        """
        ...



class XmlDecryptionTransform(Transform): # skipped bases: <type 'object'>
    """ XmlDecryptionTransform() """
    @property
    def EncryptedXml(self) -> EncryptedXml:
        """
        Get: EncryptedXml(self: XmlDecryptionTransform) -> EncryptedXml
        Set: EncryptedXml(self: XmlDecryptionTransform) = value
        """
        ...


    def AddExceptUri(self, uri:str): # -> 
        """ AddExceptUri(self: XmlDecryptionTransform, uri: str) """
        ...

    def IsTargetElement(self, *args): #cannot find CLR method
        """ IsTargetElement(self: XmlDecryptionTransform, inputElement: XmlElement, idValue: str) -> bool """
        ...


class XmlDsigBase64Transform(Transform): # skipped bases: <type 'object'>
    """ XmlDsigBase64Transform() """
    pass

class XmlDsigC14NTransform(Transform): # skipped bases: <type 'object'>
    """
    XmlDsigC14NTransform()
    XmlDsigC14NTransform(includeComments: bool)
    """
    def __new__(cls, includeComments:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeComments: bool)
        """
        ...


class XmlDsigC14NWithCommentsTransform(XmlDsigC14NTransform): # skipped bases: <type 'object'>
    """ XmlDsigC14NWithCommentsTransform() """
    pass

class XmlDsigEnvelopedSignatureTransform(Transform): # skipped bases: <type 'object'>
    """
    XmlDsigEnvelopedSignatureTransform()
    XmlDsigEnvelopedSignatureTransform(includeComments: bool)
    """
    def __new__(cls, includeComments:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeComments: bool)
        """
        ...


class XmlDsigExcC14NTransform(Transform): # skipped bases: <type 'object'>
    """
    XmlDsigExcC14NTransform()
    XmlDsigExcC14NTransform(includeComments: bool)
    XmlDsigExcC14NTransform(inclusiveNamespacesPrefixList: str)
    XmlDsigExcC14NTransform(includeComments: bool, inclusiveNamespacesPrefixList: str)
    """
    @property
    def InclusiveNamespacesPrefixList(self) -> str:
        """
        Get: InclusiveNamespacesPrefixList(self: XmlDsigExcC14NTransform) -> str
        Set: InclusiveNamespacesPrefixList(self: XmlDsigExcC14NTransform) = value
        """
        ...


    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeComments: bool)
        __new__(cls: type, inclusiveNamespacesPrefixList: str)
        __new__(cls: type, includeComments: bool, inclusiveNamespacesPrefixList: str)
        """
        ...


class XmlDsigExcC14NWithCommentsTransform(XmlDsigExcC14NTransform): # skipped bases: <type 'object'>
    """
    XmlDsigExcC14NWithCommentsTransform()
    XmlDsigExcC14NWithCommentsTransform(inclusiveNamespacesPrefixList: str)
    """
    pass

class XmlDsigXPathTransform(Transform): # skipped bases: <type 'object'>
    """ XmlDsigXPathTransform() """
    pass

class XmlDsigXsltTransform(Transform): # skipped bases: <type 'object'>
    """
    XmlDsigXsltTransform()
    XmlDsigXsltTransform(includeComments: bool)
    """
    def __new__(cls, includeComments:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, includeComments: bool)
        """
        ...


class XmlLicenseTransform(Transform): # skipped bases: <type 'object'>
    """ XmlLicenseTransform() """
    @property
    def Decryptor(self) -> IRelDecryptor:
        """
        Get: Decryptor(self: XmlLicenseTransform) -> IRelDecryptor
        Set: Decryptor(self: XmlLicenseTransform) = value
        """
        ...



