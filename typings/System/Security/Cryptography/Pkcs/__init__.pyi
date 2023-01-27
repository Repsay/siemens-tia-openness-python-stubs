# encoding: utf-8
# module System.Security.Cryptography.Pkcs calls itself Pkcs
# from System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, Enum

from System.Collections import ICollection, IEnumerator

from System.Security.Cryptography import (AsnEncodedData, 
    CryptographicAttributeObject, CryptographicAttributeObjectCollection, Oid)

from System.Security.Cryptography.X509Certificates import (X509Certificate2, 
    X509Certificate2Collection, X509IncludeOption)

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AlgorithmIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """
    AlgorithmIdentifier()
    AlgorithmIdentifier(oid: Oid)
    AlgorithmIdentifier(oid: Oid, keyLength: int)
    """
    @property
    def KeyLength(self) -> int:
        """
        Get: KeyLength(self: AlgorithmIdentifier) -> int
        Set: KeyLength(self: AlgorithmIdentifier) = value
        """
        ...

    @property
    def Oid(self) -> Oid:
        """
        Get: Oid(self: AlgorithmIdentifier) -> Oid
        Set: Oid(self: AlgorithmIdentifier) = value
        """
        ...

    @property
    def Parameters(self) -> Array:
        """
        Get: Parameters(self: AlgorithmIdentifier) -> Array[Byte]
        Set: Parameters(self: AlgorithmIdentifier) = value
        """
        ...



class CmsRecipient: # skipped bases: <type 'object'>, <type 'object'>
    """
    CmsRecipient(certificate: X509Certificate2)
    CmsRecipient(recipientIdentifierType: SubjectIdentifierType, certificate: X509Certificate2)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: CmsRecipient) -> X509Certificate2 """
        ...

    @property
    def RecipientIdentifierType(self) -> SubjectIdentifierType:
        """ Get: RecipientIdentifierType(self: CmsRecipient) -> SubjectIdentifierType """
        ...



class CmsRecipientCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    CmsRecipientCollection()
    CmsRecipientCollection(recipient: CmsRecipient)
    CmsRecipientCollection(recipientIdentifierType: SubjectIdentifierType, certificates: X509Certificate2Collection)
    """
    def Add(self, recipient:CmsRecipient) -> int:
        """ Add(self: CmsRecipientCollection, recipient: CmsRecipient) -> int """
        ...

    def GetEnumerator(self) -> CmsRecipientEnumerator:
        """ GetEnumerator(self: CmsRecipientCollection) -> CmsRecipientEnumerator """
        ...

    def Remove(self, recipient:CmsRecipient): # -> 
        """ Remove(self: CmsRecipientCollection, recipient: CmsRecipient) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class CmsRecipientEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CmsSigner: # skipped bases: <type 'object'>, <type 'object'>
    """
    CmsSigner()
    CmsSigner(signerIdentifierType: SubjectIdentifierType)
    CmsSigner(certificate: X509Certificate2)
    CmsSigner(parameters: CspParameters)
    CmsSigner(signerIdentifierType: SubjectIdentifierType, certificate: X509Certificate2)
    """
    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: CmsSigner) -> X509Certificate2
        Set: Certificate(self: CmsSigner) = value
        """
        ...

    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: CmsSigner) -> X509Certificate2Collection """
        ...

    @property
    def DigestAlgorithm(self) -> Oid:
        """
        Get: DigestAlgorithm(self: CmsSigner) -> Oid
        Set: DigestAlgorithm(self: CmsSigner) = value
        """
        ...

    @property
    def IncludeOption(self) -> X509IncludeOption:
        """
        Get: IncludeOption(self: CmsSigner) -> X509IncludeOption
        Set: IncludeOption(self: CmsSigner) = value
        """
        ...

    @property
    def SignedAttributes(self) -> CryptographicAttributeObjectCollection:
        """ Get: SignedAttributes(self: CmsSigner) -> CryptographicAttributeObjectCollection """
        ...

    @property
    def SignerIdentifierType(self) -> SubjectIdentifierType:
        """
        Get: SignerIdentifierType(self: CmsSigner) -> SubjectIdentifierType
        Set: SignerIdentifierType(self: CmsSigner) = value
        """
        ...

    @property
    def UnsignedAttributes(self) -> CryptographicAttributeObjectCollection:
        """ Get: UnsignedAttributes(self: CmsSigner) -> CryptographicAttributeObjectCollection """
        ...



class ContentInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContentInfo(content: Array[Byte])
    ContentInfo(contentType: Oid, content: Array[Byte])
    """
    @property
    def Content(self) -> Array:
        """ Get: Content(self: ContentInfo) -> Array[Byte] """
        ...

    @property
    def ContentType(self) -> Oid:
        """ Get: ContentType(self: ContentInfo) -> Oid """
        ...


    @staticmethod
    def GetContentType(encodedMessage:Array) -> Oid:
        """ GetContentType(encodedMessage: Array[Byte]) -> Oid """
        ...


class EnvelopedCms: # skipped bases: <type 'object'>, <type 'object'>
    """
    EnvelopedCms()
    EnvelopedCms(contentInfo: ContentInfo)
    EnvelopedCms(recipientIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo)
    EnvelopedCms(contentInfo: ContentInfo, encryptionAlgorithm: AlgorithmIdentifier)
    EnvelopedCms(recipientIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo, encryptionAlgorithm: AlgorithmIdentifier)
    """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: EnvelopedCms) -> X509Certificate2Collection """
        ...

    @property
    def ContentEncryptionAlgorithm(self) -> AlgorithmIdentifier:
        """ Get: ContentEncryptionAlgorithm(self: EnvelopedCms) -> AlgorithmIdentifier """
        ...

    @property
    def ContentInfo(self) -> ContentInfo:
        """ Get: ContentInfo(self: EnvelopedCms) -> ContentInfo """
        ...

    @property
    def RecipientInfos(self) -> RecipientInfoCollection:
        """ Get: RecipientInfos(self: EnvelopedCms) -> RecipientInfoCollection """
        ...

    @property
    def UnprotectedAttributes(self) -> CryptographicAttributeObjectCollection:
        """ Get: UnprotectedAttributes(self: EnvelopedCms) -> CryptographicAttributeObjectCollection """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: EnvelopedCms) -> int """
        ...


    def Decode(self, encodedMessage:Array): # -> 
        """ Decode(self: EnvelopedCms, encodedMessage: Array[Byte]) """
        ...

    def Decrypt(self, *__args:RecipientInfo): # -> 
        """ Decrypt(self: EnvelopedCms)Decrypt(self: EnvelopedCms, recipientInfo: RecipientInfo)Decrypt(self: EnvelopedCms, extraStore: X509Certificate2Collection)Decrypt(self: EnvelopedCms, recipientInfo: RecipientInfo, extraStore: X509Certificate2Collection) """
        ...

    def Encode(self) -> Array:
        """ Encode(self: EnvelopedCms) -> Array[Byte] """
        ...

    def Encrypt(self, *__args:CmsRecipient): # -> 
        """ Encrypt(self: EnvelopedCms)Encrypt(self: EnvelopedCms, recipient: CmsRecipient)Encrypt(self: EnvelopedCms, recipients: CmsRecipientCollection) """
        ...


class KeyAgreeKeyChoice(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyAgreeKeyChoice, values: EphemeralKey (1), StaticKey (2), Unknown (0) """
    EphemeralKey: KeyAgreeKeyChoice = ...
    StaticKey: KeyAgreeKeyChoice = ...
    Unknown: KeyAgreeKeyChoice = ...
    value__ = ...


class RecipientInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EncryptedKey(self) -> Array:
        """ Get: EncryptedKey(self: RecipientInfo) -> Array[Byte] """
        ...

    @property
    def KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier:
        """ Get: KeyEncryptionAlgorithm(self: RecipientInfo) -> AlgorithmIdentifier """
        ...

    @property
    def RecipientIdentifier(self) -> SubjectIdentifier:
        """ Get: RecipientIdentifier(self: RecipientInfo) -> SubjectIdentifier """
        ...

    @property
    def Type(self) -> RecipientInfoType:
        """ Get: Type(self: RecipientInfo) -> RecipientInfoType """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: RecipientInfo) -> int """
        ...



class KeyAgreeRecipientInfo(RecipientInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Date(self) -> DateTime:
        """ Get: Date(self: KeyAgreeRecipientInfo) -> DateTime """
        ...

    @property
    def OriginatorIdentifierOrKey(self) -> SubjectIdentifierOrKey:
        """ Get: OriginatorIdentifierOrKey(self: KeyAgreeRecipientInfo) -> SubjectIdentifierOrKey """
        ...

    @property
    def OtherKeyAttribute(self) -> CryptographicAttributeObject:
        """ Get: OtherKeyAttribute(self: KeyAgreeRecipientInfo) -> CryptographicAttributeObject """
        ...



class KeyTransRecipientInfo(RecipientInfo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class Pkcs9AttributeObject(AsnEncodedData): # skipped bases: <type 'object'>
    """
    Pkcs9AttributeObject()
    Pkcs9AttributeObject(oid: str, encodedData: Array[Byte])
    Pkcs9AttributeObject(oid: Oid, encodedData: Array[Byte])
    Pkcs9AttributeObject(asnEncodedData: AsnEncodedData)
    """
    pass

class Pkcs9ContentType(Pkcs9AttributeObject): # skipped bases: <type 'object'>
    """ Pkcs9ContentType() """
    @property
    def ContentType(self) -> Oid:
        """ Get: ContentType(self: Pkcs9ContentType) -> Oid """
        ...



class Pkcs9DocumentDescription(Pkcs9AttributeObject): # skipped bases: <type 'object'>
    """
    Pkcs9DocumentDescription()
    Pkcs9DocumentDescription(documentDescription: str)
    Pkcs9DocumentDescription(encodedDocumentDescription: Array[Byte])
    """
    @property
    def DocumentDescription(self) -> str:
        """ Get: DocumentDescription(self: Pkcs9DocumentDescription) -> str """
        ...



class Pkcs9DocumentName(Pkcs9AttributeObject): # skipped bases: <type 'object'>
    """
    Pkcs9DocumentName()
    Pkcs9DocumentName(documentName: str)
    Pkcs9DocumentName(encodedDocumentName: Array[Byte])
    """
    @property
    def DocumentName(self) -> str:
        """ Get: DocumentName(self: Pkcs9DocumentName) -> str """
        ...



class Pkcs9MessageDigest(Pkcs9AttributeObject): # skipped bases: <type 'object'>
    """ Pkcs9MessageDigest() """
    @property
    def MessageDigest(self) -> Array:
        """ Get: MessageDigest(self: Pkcs9MessageDigest) -> Array[Byte] """
        ...



class Pkcs9SigningTime(Pkcs9AttributeObject): # skipped bases: <type 'object'>
    """
    Pkcs9SigningTime()
    Pkcs9SigningTime(signingTime: DateTime)
    Pkcs9SigningTime(encodedSigningTime: Array[Byte])
    """
    @property
    def SigningTime(self) -> DateTime:
        """ Get: SigningTime(self: Pkcs9SigningTime) -> DateTime """
        ...



class PublicKeyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Algorithm(self) -> AlgorithmIdentifier:
        """ Get: Algorithm(self: PublicKeyInfo) -> AlgorithmIdentifier """
        ...

    @property
    def KeyValue(self) -> Array:
        """ Get: KeyValue(self: PublicKeyInfo) -> Array[Byte] """
        ...



class RecipientInfoCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> RecipientInfoEnumerator:
        """ GetEnumerator(self: RecipientInfoCollection) -> RecipientInfoEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class RecipientInfoEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class RecipientInfoType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecipientInfoType, values: KeyAgreement (2), KeyTransport (1), Unknown (0) """
    KeyAgreement: RecipientInfoType = ...
    KeyTransport: RecipientInfoType = ...
    Unknown: RecipientInfoType = ...
    value__ = ...


class SignedCms: # skipped bases: <type 'object'>, <type 'object'>
    """
    SignedCms()
    SignedCms(signerIdentifierType: SubjectIdentifierType)
    SignedCms(contentInfo: ContentInfo)
    SignedCms(signerIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo)
    SignedCms(contentInfo: ContentInfo, detached: bool)
    SignedCms(signerIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo, detached: bool)
    """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: SignedCms) -> X509Certificate2Collection """
        ...

    @property
    def ContentInfo(self) -> ContentInfo:
        """ Get: ContentInfo(self: SignedCms) -> ContentInfo """
        ...

    @property
    def Detached(self) -> bool:
        """ Get: Detached(self: SignedCms) -> bool """
        ...

    @property
    def SignerInfos(self) -> SignerInfoCollection:
        """ Get: SignerInfos(self: SignedCms) -> SignerInfoCollection """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: SignedCms) -> int """
        ...


    def CheckHash(self): # -> 
        """ CheckHash(self: SignedCms) """
        ...

    def CheckSignature(self, *__args:bool): # -> 
        """ CheckSignature(self: SignedCms, verifySignatureOnly: bool)CheckSignature(self: SignedCms, extraStore: X509Certificate2Collection, verifySignatureOnly: bool) """
        ...

    def ComputeSignature(self, signer:CmsSigner = ..., silent:bool = ...): # -> 
        """ ComputeSignature(self: SignedCms)ComputeSignature(self: SignedCms, signer: CmsSigner)ComputeSignature(self: SignedCms, signer: CmsSigner, silent: bool) """
        ...

    def Decode(self, encodedMessage:Array): # -> 
        """ Decode(self: SignedCms, encodedMessage: Array[Byte]) """
        ...

    def Encode(self) -> Array:
        """ Encode(self: SignedCms) -> Array[Byte] """
        ...

    def RemoveSignature(self, *__args:int): # -> 
        """ RemoveSignature(self: SignedCms, index: int)RemoveSignature(self: SignedCms, signerInfo: SignerInfo) """
        ...


class SignerInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: SignerInfo) -> X509Certificate2 """
        ...

    @property
    def CounterSignerInfos(self) -> SignerInfoCollection:
        """ Get: CounterSignerInfos(self: SignerInfo) -> SignerInfoCollection """
        ...

    @property
    def DigestAlgorithm(self) -> Oid:
        """ Get: DigestAlgorithm(self: SignerInfo) -> Oid """
        ...

    @property
    def SignatureAlgorithm(self) -> Oid:
        """ Get: SignatureAlgorithm(self: SignerInfo) -> Oid """
        ...

    @property
    def SignedAttributes(self) -> CryptographicAttributeObjectCollection:
        """ Get: SignedAttributes(self: SignerInfo) -> CryptographicAttributeObjectCollection """
        ...

    @property
    def SignerIdentifier(self) -> SubjectIdentifier:
        """ Get: SignerIdentifier(self: SignerInfo) -> SubjectIdentifier """
        ...

    @property
    def UnsignedAttributes(self) -> CryptographicAttributeObjectCollection:
        """ Get: UnsignedAttributes(self: SignerInfo) -> CryptographicAttributeObjectCollection """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: SignerInfo) -> int """
        ...


    def CheckHash(self): # -> 
        """ CheckHash(self: SignerInfo) """
        ...

    def CheckSignature(self, *__args:bool): # -> 
        """ CheckSignature(self: SignerInfo, verifySignatureOnly: bool)CheckSignature(self: SignerInfo, extraStore: X509Certificate2Collection, verifySignatureOnly: bool) """
        ...

    def ComputeCounterSignature(self, signer:CmsSigner = ...): # -> 
        """ ComputeCounterSignature(self: SignerInfo)ComputeCounterSignature(self: SignerInfo, signer: CmsSigner) """
        ...

    def GetSignature(self) -> Array:
        """ GetSignature(self: SignerInfo) -> Array[Byte] """
        ...

    def RemoveCounterSignature(self, *__args:int): # -> 
        """ RemoveCounterSignature(self: SignerInfo, index: int)RemoveCounterSignature(self: SignerInfo, counterSignerInfo: SignerInfo) """
        ...


class SignerInfoCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> SignerInfoEnumerator:
        """ GetEnumerator(self: SignerInfoCollection) -> SignerInfoEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SignerInfoEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SubjectIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SubjectIdentifierType:
        """ Get: Type(self: SubjectIdentifier) -> SubjectIdentifierType """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SubjectIdentifier) -> object """
        ...



class SubjectIdentifierOrKey: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SubjectIdentifierOrKeyType:
        """ Get: Type(self: SubjectIdentifierOrKey) -> SubjectIdentifierOrKeyType """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SubjectIdentifierOrKey) -> object """
        ...



class SubjectIdentifierOrKeyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SubjectIdentifierOrKeyType, values: IssuerAndSerialNumber (1), PublicKeyInfo (3), SubjectKeyIdentifier (2), Unknown (0) """
    IssuerAndSerialNumber: SubjectIdentifierOrKeyType = ...
    PublicKeyInfo: SubjectIdentifierOrKeyType = ...
    SubjectKeyIdentifier: SubjectIdentifierOrKeyType = ...
    Unknown: SubjectIdentifierOrKeyType = ...
    value__ = ...


class SubjectIdentifierType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SubjectIdentifierType, values: IssuerAndSerialNumber (1), NoSignature (3), SubjectKeyIdentifier (2), Unknown (0) """
    IssuerAndSerialNumber: SubjectIdentifierType = ...
    NoSignature: SubjectIdentifierType = ...
    SubjectKeyIdentifier: SubjectIdentifierType = ...
    Unknown: SubjectIdentifierType = ...
    value__ = ...


