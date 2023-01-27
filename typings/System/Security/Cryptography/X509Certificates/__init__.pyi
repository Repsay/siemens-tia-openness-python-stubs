# encoding: utf-8
# module System.Security.Cryptography.X509Certificates calls itself X509Certificates
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from Microsoft.Win32.SafeHandles import SafeX509ChainHandle

from System import (Array, DateTime, DateTimeOffset, Enum, IDisposable, 
    IntPtr, TimeSpan, Uri)

from System.Collections import CollectionBase, ICollection, IEnumerator

from System.Net import IPAddress

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)

from System.Security.Cryptography import (AsnEncodedData, AsymmetricAlgorithm, 
    DSA, ECDsa, HashAlgorithmName, Oid, OidCollection, RSA, 
    RSASignaturePadding, SignatureVerificationResult)

"""The following names are not found in the module: (TimestampInformation, 
    TrustStatus, X509SelectionFlag, X509SignatureGenerator, field#)
"""

# no functions
# classes

class AuthenticodeSignatureInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: AuthenticodeSignatureInformation) -> str """
        ...

    @property
    def DescriptionUrl(self) -> Uri:
        """ Get: DescriptionUrl(self: AuthenticodeSignatureInformation) -> Uri """
        ...

    @property
    def HashAlgorithm(self) -> str:
        """ Get: HashAlgorithm(self: AuthenticodeSignatureInformation) -> str """
        ...

    @property
    def HResult(self) -> int:
        """ Get: HResult(self: AuthenticodeSignatureInformation) -> int """
        ...

    @property
    def SignatureChain(self) -> X509Chain:
        """ Get: SignatureChain(self: AuthenticodeSignatureInformation) -> X509Chain """
        ...

    @property
    def SigningCertificate(self) -> X509Certificate2:
        """ Get: SigningCertificate(self: AuthenticodeSignatureInformation) -> X509Certificate2 """
        ...

    @property
    def Timestamp(self): # -> TimestampInformation
        """ Get: Timestamp(self: AuthenticodeSignatureInformation) -> TimestampInformation """
        ...

    @property
    def TrustStatus(self): # -> TrustStatus
        """ Get: TrustStatus(self: AuthenticodeSignatureInformation) -> TrustStatus """
        ...

    @property
    def VerificationResult(self) -> SignatureVerificationResult:
        """ Get: VerificationResult(self: AuthenticodeSignatureInformation) -> SignatureVerificationResult """
        ...



class CertificateRequest: # skipped bases: <type 'object'>, <type 'object'>
    """
    CertificateRequest(subjectName: str, key: ECDsa, hashAlgorithm: HashAlgorithmName)
    CertificateRequest(subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName)
    CertificateRequest(subjectName: str, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding)
    CertificateRequest(subjectName: X500DistinguishedName, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding)
    CertificateRequest(subjectName: X500DistinguishedName, publicKey: PublicKey, hashAlgorithm: HashAlgorithmName)
    """
    @property
    def CertificateExtensions(self) -> Collection:
        """ Get: CertificateExtensions(self: CertificateRequest) -> Collection[X509Extension] """
        ...

    @property
    def HashAlgorithm(self) -> HashAlgorithmName:
        """ Get: HashAlgorithm(self: CertificateRequest) -> HashAlgorithmName """
        ...

    @property
    def PublicKey(self) -> PublicKey:
        """ Get: PublicKey(self: CertificateRequest) -> PublicKey """
        ...

    @property
    def SubjectName(self) -> X500DistinguishedName:
        """ Get: SubjectName(self: CertificateRequest) -> X500DistinguishedName """
        ...


    def Create(self, *__args) -> X509Certificate2:
        """
        Create(self: CertificateRequest, issuerCertificate: X509Certificate2, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: Array[Byte]) -> X509Certificate2
        Create(self: CertificateRequest, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: Array[Byte]) -> X509Certificate2
        """
        ...

    def CreateSelfSigned(self, notBefore:DateTimeOffset, notAfter:DateTimeOffset) -> X509Certificate2:
        """ CreateSelfSigned(self: CertificateRequest, notBefore: DateTimeOffset, notAfter: DateTimeOffset) -> X509Certificate2 """
        ...

    def CreateSigningRequest(self, signatureGenerator = ...) -> Array: # Not found arg types: {'signatureGenerator': 'X509SignatureGenerator'}
        """
        CreateSigningRequest(self: CertificateRequest) -> Array[Byte]
        CreateSigningRequest(self: CertificateRequest, signatureGenerator: X509SignatureGenerator) -> Array[Byte]
        """
        ...


class DSACertificateExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CopyWithPrivateKey(certificate:X509Certificate2, privateKey:DSA) -> X509Certificate2:
        """ CopyWithPrivateKey(certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2 """
        ...

    @staticmethod
    def GetDSAPrivateKey(certificate:X509Certificate2) -> DSA:
        """ GetDSAPrivateKey(certificate: X509Certificate2) -> DSA """
        ...

    @staticmethod
    def GetDSAPublicKey(certificate:X509Certificate2) -> DSA:
        """ GetDSAPublicKey(certificate: X509Certificate2) -> DSA """
        ...

    __all__: list = ...


class ECDsaCertificateExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CopyWithPrivateKey(certificate:X509Certificate2, privateKey:ECDsa) -> X509Certificate2:
        """ CopyWithPrivateKey(certificate: X509Certificate2, privateKey: ECDsa) -> X509Certificate2 """
        ...

    @staticmethod
    def GetECDsaPrivateKey(certificate:X509Certificate2) -> ECDsa:
        """ GetECDsaPrivateKey(certificate: X509Certificate2) -> ECDsa """
        ...

    @staticmethod
    def GetECDsaPublicKey(certificate:X509Certificate2) -> ECDsa:
        """ GetECDsaPublicKey(certificate: X509Certificate2) -> ECDsa """
        ...

    __all__: list = ...


class OpenFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) OpenFlags, values: IncludeArchived (8), MaxAllowed (2), OpenExistingOnly (4), ReadOnly (0), ReadWrite (1) """
    IncludeArchived: OpenFlags = ...
    MaxAllowed: OpenFlags = ...
    OpenExistingOnly: OpenFlags = ...
    ReadOnly: OpenFlags = ...
    ReadWrite: OpenFlags = ...
    value__ = ...


class PublicKey: # skipped bases: <type 'object'>, <type 'object'>
    """ PublicKey(oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData) """
    @property
    def EncodedKeyValue(self) -> AsnEncodedData:
        """ Get: EncodedKeyValue(self: PublicKey) -> AsnEncodedData """
        ...

    @property
    def EncodedParameters(self) -> AsnEncodedData:
        """ Get: EncodedParameters(self: PublicKey) -> AsnEncodedData """
        ...

    @property
    def Key(self) -> AsymmetricAlgorithm:
        """ Get: Key(self: PublicKey) -> AsymmetricAlgorithm """
        ...

    @property
    def Oid(self) -> Oid:
        """ Get: Oid(self: PublicKey) -> Oid """
        ...



class RSACertificateExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CopyWithPrivateKey(certificate:X509Certificate2, privateKey:RSA) -> X509Certificate2:
        """ CopyWithPrivateKey(certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2 """
        ...

    @staticmethod
    def GetRSAPrivateKey(certificate:X509Certificate2) -> RSA:
        """ GetRSAPrivateKey(certificate: X509Certificate2) -> RSA """
        ...

    @staticmethod
    def GetRSAPublicKey(certificate:X509Certificate2) -> RSA:
        """ GetRSAPublicKey(certificate: X509Certificate2) -> RSA """
        ...

    __all__: list = ...


class StoreLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StoreLocation, values: CurrentUser (1), LocalMachine (2) """
    CurrentUser: StoreLocation = ...
    LocalMachine: StoreLocation = ...
    value__ = ...


class StoreName(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StoreName, values: AddressBook (1), AuthRoot (2), CertificateAuthority (3), Disallowed (4), My (5), Root (6), TrustedPeople (7), TrustedPublisher (8) """
    AddressBook: StoreName = ...
    AuthRoot: StoreName = ...
    CertificateAuthority: StoreName = ...
    Disallowed: StoreName = ...
    My: StoreName = ...
    Root: StoreName = ...
    TrustedPeople: StoreName = ...
    TrustedPublisher: StoreName = ...
    value__ = ...


class SubjectAlternativeNameBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ SubjectAlternativeNameBuilder() """
    def AddDnsName(self, dnsName:str): # -> 
        """ AddDnsName(self: SubjectAlternativeNameBuilder, dnsName: str) """
        ...

    def AddEmailAddress(self, emailAddress:str): # -> 
        """ AddEmailAddress(self: SubjectAlternativeNameBuilder, emailAddress: str) """
        ...

    def AddIpAddress(self, ipAddress:IPAddress): # -> 
        """ AddIpAddress(self: SubjectAlternativeNameBuilder, ipAddress: IPAddress) """
        ...

    def AddUri(self, uri:Uri): # -> 
        """ AddUri(self: SubjectAlternativeNameBuilder, uri: Uri) """
        ...

    def AddUserPrincipalName(self, upn:str): # -> 
        """ AddUserPrincipalName(self: SubjectAlternativeNameBuilder, upn: str) """
        ...

    def Build(self, critical:bool) -> X509Extension:
        """ Build(self: SubjectAlternativeNameBuilder, critical: bool) -> X509Extension """
        ...


class TimestampInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HashAlgorithm(self) -> str:
        """ Get: HashAlgorithm(self: TimestampInformation) -> str """
        ...

    @property
    def HResult(self) -> int:
        """ Get: HResult(self: TimestampInformation) -> int """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: TimestampInformation) -> bool """
        ...

    @property
    def SignatureChain(self) -> X509Chain:
        """ Get: SignatureChain(self: TimestampInformation) -> X509Chain """
        ...

    @property
    def SigningCertificate(self) -> X509Certificate2:
        """ Get: SigningCertificate(self: TimestampInformation) -> X509Certificate2 """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """ Get: Timestamp(self: TimestampInformation) -> DateTime """
        ...

    @property
    def VerificationResult(self) -> SignatureVerificationResult:
        """ Get: VerificationResult(self: TimestampInformation) -> SignatureVerificationResult """
        ...



class TrustStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrustStatus, values: KnownIdentity (2), Trusted (3), UnknownIdentity (1), Untrusted (0) """
    KnownIdentity: TrustStatus = ...
    Trusted: TrustStatus = ...
    UnknownIdentity: TrustStatus = ...
    Untrusted: TrustStatus = ...
    value__ = ...


class X500DistinguishedName(AsnEncodedData): # skipped bases: <type 'object'>
    """
    X500DistinguishedName(encodedDistinguishedName: Array[Byte])
    X500DistinguishedName(encodedDistinguishedName: AsnEncodedData)
    X500DistinguishedName(distinguishedName: X500DistinguishedName)
    X500DistinguishedName(distinguishedName: str)
    X500DistinguishedName(distinguishedName: str, flag: X500DistinguishedNameFlags)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: X500DistinguishedName) -> str """
        ...


    def Decode(self, flag:X500DistinguishedNameFlags) -> str:
        """ Decode(self: X500DistinguishedName, flag: X500DistinguishedNameFlags) -> str """
        ...


class X500DistinguishedNameFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) X500DistinguishedNameFlags, values: DoNotUsePlusSign (32), DoNotUseQuotes (64), ForceUTF8Encoding (16384), None (0), Reversed (1), UseCommas (128), UseNewLines (256), UseSemicolons (16), UseT61Encoding (8192), UseUTF8Encoding (4096) """
    DoNotUsePlusSign: X500DistinguishedNameFlags = ...
    DoNotUseQuotes: X500DistinguishedNameFlags = ...
    ForceUTF8Encoding: X500DistinguishedNameFlags = ...
    Reversed: X500DistinguishedNameFlags = ...
    UseCommas: X500DistinguishedNameFlags = ...
    UseNewLines: X500DistinguishedNameFlags = ...
    UseSemicolons: X500DistinguishedNameFlags = ...
    UseT61Encoding: X500DistinguishedNameFlags = ...
    UseUTF8Encoding: X500DistinguishedNameFlags = ...
    value__ = ...


class X509Extension(AsnEncodedData): # skipped bases: <type 'object'>
    """
    X509Extension(oid: str, rawData: Array[Byte], critical: bool)
    X509Extension(encodedExtension: AsnEncodedData, critical: bool)
    X509Extension(oid: Oid, rawData: Array[Byte], critical: bool)
    """
    @property
    def Critical(self) -> bool:
        """
        Get: Critical(self: X509Extension) -> bool
        Set: Critical(self: X509Extension) = value
        """
        ...



class X509BasicConstraintsExtension(X509Extension): # skipped bases: <type 'object'>
    """
    X509BasicConstraintsExtension()
    X509BasicConstraintsExtension(certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool)
    X509BasicConstraintsExtension(encodedBasicConstraints: AsnEncodedData, critical: bool)
    """
    @property
    def CertificateAuthority(self) -> bool:
        """ Get: CertificateAuthority(self: X509BasicConstraintsExtension) -> bool """
        ...

    @property
    def HasPathLengthConstraint(self) -> bool:
        """ Get: HasPathLengthConstraint(self: X509BasicConstraintsExtension) -> bool """
        ...

    @property
    def PathLengthConstraint(self) -> int:
        """ Get: PathLengthConstraint(self: X509BasicConstraintsExtension) -> int """
        ...



class X509Certificate(IDisposable, IDeserializationCallback, ISerializable): # skipped bases: <type 'object'>
    """
    X509Certificate()
    X509Certificate(data: Array[Byte])
    X509Certificate(rawData: Array[Byte], password: str)
    X509Certificate(rawData: Array[Byte], password: SecureString)
    X509Certificate(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(fileName: str)
    X509Certificate(fileName: str, password: str)
    X509Certificate(fileName: str, password: SecureString)
    X509Certificate(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate(handle: IntPtr)
    X509Certificate(cert: X509Certificate)
    X509Certificate(info: SerializationInfo, context: StreamingContext)
    """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: X509Certificate) -> IntPtr """
        ...

    @property
    def Issuer(self) -> str:
        """ Get: Issuer(self: X509Certificate) -> str """
        ...

    @property
    def Subject(self) -> str:
        """ Get: Subject(self: X509Certificate) -> str """
        ...


    @staticmethod
    def CreateFromCertFile(filename:str) -> X509Certificate:
        """ CreateFromCertFile(filename: str) -> X509Certificate """
        ...

    @staticmethod
    def CreateFromSignedFile(filename:str) -> X509Certificate:
        """ CreateFromSignedFile(filename: str) -> X509Certificate """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: X509Certificate, obj: object) -> bool
        Equals(self: X509Certificate, other: X509Certificate) -> bool
        """
        ...

    def Export(self, contentType:X509ContentType, password:str = ...) -> Array:
        """
        Export(self: X509Certificate, contentType: X509ContentType) -> Array[Byte]
        Export(self: X509Certificate, contentType: X509ContentType, password: str) -> Array[Byte]
        Export(self: X509Certificate, contentType: X509ContentType, password: SecureString) -> Array[Byte]
        """
        ...

    def FormatDate(self, *args): #cannot find CLR method
        """ FormatDate(date: DateTime) -> str """
        ...

    def GetCertHash(self, hashAlgorithm:HashAlgorithmName = ...) -> Array:
        """
        GetCertHash(self: X509Certificate) -> Array[Byte]
        GetCertHash(self: X509Certificate, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def GetCertHashString(self, hashAlgorithm:HashAlgorithmName = ...) -> str:
        """
        GetCertHashString(self: X509Certificate) -> str
        GetCertHashString(self: X509Certificate, hashAlgorithm: HashAlgorithmName) -> str
        """
        ...

    def GetEffectiveDateString(self) -> str:
        """ GetEffectiveDateString(self: X509Certificate) -> str """
        ...

    def GetExpirationDateString(self) -> str:
        """ GetExpirationDateString(self: X509Certificate) -> str """
        ...

    def GetFormat(self) -> str:
        """ GetFormat(self: X509Certificate) -> str """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: X509Certificate) -> int """
        ...

    def GetIssuerName(self) -> str:
        """ GetIssuerName(self: X509Certificate) -> str """
        ...

    def GetKeyAlgorithm(self) -> str:
        """ GetKeyAlgorithm(self: X509Certificate) -> str """
        ...

    def GetKeyAlgorithmParameters(self) -> Array:
        """ GetKeyAlgorithmParameters(self: X509Certificate) -> Array[Byte] """
        ...

    def GetKeyAlgorithmParametersString(self) -> str:
        """ GetKeyAlgorithmParametersString(self: X509Certificate) -> str """
        ...

    def GetName(self) -> str:
        """ GetName(self: X509Certificate) -> str """
        ...

    def GetPublicKey(self) -> Array:
        """ GetPublicKey(self: X509Certificate) -> Array[Byte] """
        ...

    def GetPublicKeyString(self) -> str:
        """ GetPublicKeyString(self: X509Certificate) -> str """
        ...

    def GetRawCertData(self) -> Array:
        """ GetRawCertData(self: X509Certificate) -> Array[Byte] """
        ...

    def GetRawCertDataString(self) -> str:
        """ GetRawCertDataString(self: X509Certificate) -> str """
        ...

    def GetSerialNumber(self) -> Array:
        """ GetSerialNumber(self: X509Certificate) -> Array[Byte] """
        ...

    def GetSerialNumberString(self) -> str:
        """ GetSerialNumberString(self: X509Certificate) -> str """
        ...

    def Import(self, *__args:Array): # -> 
        """ Import(self: X509Certificate, rawData: Array[Byte])Import(self: X509Certificate, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)Import(self: X509Certificate, rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)Import(self: X509Certificate, fileName: str)Import(self: X509Certificate, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)Import(self: X509Certificate, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags) """
        ...

    def Reset(self): # -> 
        """ Reset(self: X509Certificate) """
        ...

    def ToString(self, fVerbose:bool = ...) -> str:
        """
        ToString(self: X509Certificate) -> str
        ToString(self: X509Certificate, fVerbose: bool) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class X509Certificate2(X509Certificate): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'object'>
    """
    X509Certificate2()
    X509Certificate2(rawData: Array[Byte])
    X509Certificate2(rawData: Array[Byte], password: str)
    X509Certificate2(rawData: Array[Byte], password: SecureString)
    X509Certificate2(rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(rawData: Array[Byte], password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(fileName: str)
    X509Certificate2(fileName: str, password: str)
    X509Certificate2(fileName: str, password: SecureString)
    X509Certificate2(fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags)
    X509Certificate2(handle: IntPtr)
    X509Certificate2(certificate: X509Certificate)
    """
    @property
    def Archived(self) -> bool:
        """
        Get: Archived(self: X509Certificate2) -> bool
        Set: Archived(self: X509Certificate2) = value
        """
        ...

    @property
    def Extensions(self) -> X509ExtensionCollection:
        """ Get: Extensions(self: X509Certificate2) -> X509ExtensionCollection """
        ...

    @property
    def FriendlyName(self) -> str:
        """
        Get: FriendlyName(self: X509Certificate2) -> str
        Set: FriendlyName(self: X509Certificate2) = value
        """
        ...

    @property
    def HasPrivateKey(self) -> bool:
        """ Get: HasPrivateKey(self: X509Certificate2) -> bool """
        ...

    @property
    def IssuerName(self) -> X500DistinguishedName:
        """ Get: IssuerName(self: X509Certificate2) -> X500DistinguishedName """
        ...

    @property
    def NotAfter(self) -> DateTime:
        """ Get: NotAfter(self: X509Certificate2) -> DateTime """
        ...

    @property
    def NotBefore(self) -> DateTime:
        """ Get: NotBefore(self: X509Certificate2) -> DateTime """
        ...

    @property
    def PrivateKey(self) -> AsymmetricAlgorithm:
        """
        Get: PrivateKey(self: X509Certificate2) -> AsymmetricAlgorithm
        Set: PrivateKey(self: X509Certificate2) = value
        """
        ...

    @property
    def PublicKey(self) -> PublicKey:
        """ Get: PublicKey(self: X509Certificate2) -> PublicKey """
        ...

    @property
    def RawData(self) -> Array:
        """ Get: RawData(self: X509Certificate2) -> Array[Byte] """
        ...

    @property
    def SerialNumber(self) -> str:
        """ Get: SerialNumber(self: X509Certificate2) -> str """
        ...

    @property
    def SignatureAlgorithm(self) -> Oid:
        """ Get: SignatureAlgorithm(self: X509Certificate2) -> Oid """
        ...

    @property
    def SubjectName(self) -> X500DistinguishedName:
        """ Get: SubjectName(self: X509Certificate2) -> X500DistinguishedName """
        ...

    @property
    def Thumbprint(self) -> str:
        """ Get: Thumbprint(self: X509Certificate2) -> str """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: X509Certificate2) -> int """
        ...


    @staticmethod
    def GetCertContentType(*__args:Array) -> X509ContentType:
        """
        GetCertContentType(rawData: Array[Byte]) -> X509ContentType
        GetCertContentType(fileName: str) -> X509ContentType
        """
        ...

    def GetNameInfo(self, nameType:X509NameType, forIssuer:bool) -> str:
        """ GetNameInfo(self: X509Certificate2, nameType: X509NameType, forIssuer: bool) -> str """
        ...

    def Verify(self) -> bool:
        """ Verify(self: X509Certificate2) -> bool """
        ...


class X509CertificateCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    X509CertificateCollection()
    X509CertificateCollection(value: X509CertificateCollection)
    X509CertificateCollection(value: Array[X509Certificate])
    """
    def Add(self, value:X509Certificate) -> int:
        """ Add(self: X509CertificateCollection, value: X509Certificate) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: X509CertificateCollection, value: Array[X509Certificate])AddRange(self: X509CertificateCollection, value: X509CertificateCollection) """
        ...

    def Contains(self, value:X509Certificate) -> bool:
        """ Contains(self: X509CertificateCollection, value: X509Certificate) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: X509CertificateCollection, array: Array[X509Certificate], index: int) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: X509CertificateCollection) -> int """
        ...

    def IndexOf(self, value:X509Certificate) -> int:
        """ IndexOf(self: X509CertificateCollection, value: X509Certificate) -> int """
        ...

    def Insert(self, index:int, value:X509Certificate): # -> 
        """ Insert(self: X509CertificateCollection, index: int, value: X509Certificate) """
        ...

    def Remove(self, value:X509Certificate): # -> 
        """ Remove(self: X509CertificateCollection, value: X509Certificate) """
        ...

    def X509CertificateEnumerator(self, *args): #cannot find CLR method
        """ X509CertificateEnumerator(mappings: X509CertificateCollection) """
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



class X509Certificate2Collection(X509CertificateCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    X509Certificate2Collection()
    X509Certificate2Collection(certificate: X509Certificate2)
    X509Certificate2Collection(certificates: X509Certificate2Collection)
    X509Certificate2Collection(certificates: Array[X509Certificate2])
    """
    def Export(self, contentType:X509ContentType, password:str = ...) -> Array:
        """
        Export(self: X509Certificate2Collection, contentType: X509ContentType) -> Array[Byte]
        Export(self: X509Certificate2Collection, contentType: X509ContentType, password: str) -> Array[Byte]
        """
        ...

    def Find(self, findType:X509FindType, findValue:object, validOnly:bool) -> X509Certificate2Collection:
        """ Find(self: X509Certificate2Collection, findType: X509FindType, findValue: object, validOnly: bool) -> X509Certificate2Collection """
        ...

    def Import(self, *__args:Array): # -> 
        """ Import(self: X509Certificate2Collection, rawData: Array[Byte])Import(self: X509Certificate2Collection, fileName: str)Import(self: X509Certificate2Collection, rawData: Array[Byte], password: str, keyStorageFlags: X509KeyStorageFlags)Import(self: X509Certificate2Collection, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) """
        ...

    def RemoveRange(self, certificates:Array): # -> 
        """ RemoveRange(self: X509Certificate2Collection, certificates: Array[X509Certificate2])RemoveRange(self: X509Certificate2Collection, certificates: X509Certificate2Collection) """
        ...


class X509Certificate2Enumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class X509Certificate2UI: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def DisplayCertificate(certificate:X509Certificate2, hwndParent:IntPtr = ...): # -> 
        """ DisplayCertificate(certificate: X509Certificate2)DisplayCertificate(certificate: X509Certificate2, hwndParent: IntPtr) """
        ...

    @staticmethod
    def SelectFromCollection(certificates:X509Certificate2Collection, title:str, message:str, selectionFlag, hwndParent:IntPtr = ...) -> X509Certificate2Collection: # Not found arg types: {'selectionFlag': 'X509SelectionFlag'}
        """
        SelectFromCollection(certificates: X509Certificate2Collection, title: str, message: str, selectionFlag: X509SelectionFlag) -> X509Certificate2Collection
        SelectFromCollection(certificates: X509Certificate2Collection, title: str, message: str, selectionFlag: X509SelectionFlag, hwndParent: IntPtr) -> X509Certificate2Collection
        """
        ...

    __all__: list = ...


class X509Chain(IDisposable): # skipped bases: <type 'object'>
    """
    X509Chain()
    X509Chain(useMachineContext: bool)
    X509Chain(chainContext: IntPtr)
    """
    @property
    def ChainContext(self) -> IntPtr:
        """ Get: ChainContext(self: X509Chain) -> IntPtr """
        ...

    @property
    def ChainElements(self) -> X509ChainElementCollection:
        """ Get: ChainElements(self: X509Chain) -> X509ChainElementCollection """
        ...

    @property
    def ChainPolicy(self) -> X509ChainPolicy:
        """
        Get: ChainPolicy(self: X509Chain) -> X509ChainPolicy
        Set: ChainPolicy(self: X509Chain) = value
        """
        ...

    @property
    def ChainStatus(self) -> Array:
        """ Get: ChainStatus(self: X509Chain) -> Array[X509ChainStatus] """
        ...

    @property
    def SafeHandle(self) -> SafeX509ChainHandle:
        """ Get: SafeHandle(self: X509Chain) -> SafeX509ChainHandle """
        ...


    def Build(self, certificate:X509Certificate2) -> bool:
        """ Build(self: X509Chain, certificate: X509Certificate2) -> bool """
        ...

    @staticmethod
    def Create() -> X509Chain:
        """ Create() -> X509Chain """
        ...

    def Reset(self): # -> 
        """ Reset(self: X509Chain) """
        ...


class X509ChainElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Certificate(self) -> X509Certificate2:
        """ Get: Certificate(self: X509ChainElement) -> X509Certificate2 """
        ...

    @property
    def ChainElementStatus(self) -> Array:
        """ Get: ChainElementStatus(self: X509ChainElement) -> Array[X509ChainStatus] """
        ...

    @property
    def Information(self) -> str:
        """ Get: Information(self: X509ChainElement) -> str """
        ...



class X509ChainElementCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> X509ChainElementEnumerator:
        """ GetEnumerator(self: X509ChainElementCollection) -> X509ChainElementEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class X509ChainElementEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class X509ChainPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ X509ChainPolicy() """
    @property
    def ApplicationPolicy(self) -> OidCollection:
        """ Get: ApplicationPolicy(self: X509ChainPolicy) -> OidCollection """
        ...

    @property
    def CertificatePolicy(self) -> OidCollection:
        """ Get: CertificatePolicy(self: X509ChainPolicy) -> OidCollection """
        ...

    @property
    def ExtraStore(self) -> X509Certificate2Collection:
        """ Get: ExtraStore(self: X509ChainPolicy) -> X509Certificate2Collection """
        ...

    @property
    def RevocationFlag(self) -> X509RevocationFlag:
        """
        Get: RevocationFlag(self: X509ChainPolicy) -> X509RevocationFlag
        Set: RevocationFlag(self: X509ChainPolicy) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: X509ChainPolicy) -> X509RevocationMode
        Set: RevocationMode(self: X509ChainPolicy) = value
        """
        ...

    @property
    def UrlRetrievalTimeout(self) -> TimeSpan:
        """
        Get: UrlRetrievalTimeout(self: X509ChainPolicy) -> TimeSpan
        Set: UrlRetrievalTimeout(self: X509ChainPolicy) = value
        """
        ...

    @property
    def VerificationFlags(self) -> X509VerificationFlags:
        """
        Get: VerificationFlags(self: X509ChainPolicy) -> X509VerificationFlags
        Set: VerificationFlags(self: X509ChainPolicy) = value
        """
        ...

    @property
    def VerificationTime(self) -> DateTime:
        """
        Get: VerificationTime(self: X509ChainPolicy) -> DateTime
        Set: VerificationTime(self: X509ChainPolicy) = value
        """
        ...


    def Reset(self): # -> 
        """ Reset(self: X509ChainPolicy) """
        ...


class X509ChainStatus: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Status(self) -> X509ChainStatusFlags:
        """
        Get: Status(self: X509ChainStatus) -> X509ChainStatusFlags
        Set: Status(self: X509ChainStatus) = value
        """
        ...

    @property
    def StatusInformation(self) -> str:
        """
        Get: StatusInformation(self: X509ChainStatus) -> str
        Set: StatusInformation(self: X509ChainStatus) = value
        """
        ...



class X509ChainStatusFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) X509ChainStatusFlags, values: CtlNotSignatureValid (262144), CtlNotTimeValid (131072), CtlNotValidForUsage (524288), Cyclic (128), ExplicitDistrust (67108864), HasExcludedNameConstraint (32768), HasNotDefinedNameConstraint (8192), HasNotPermittedNameConstraint (16384), HasNotSupportedCriticalExtension (134217728), HasNotSupportedNameConstraint (4096), HasWeakSignature (1048576), InvalidBasicConstraints (1024), InvalidExtension (256), InvalidNameConstraints (2048), InvalidPolicyConstraints (512), NoError (0), NoIssuanceChainPolicy (33554432), NotSignatureValid (8), NotTimeNested (2), NotTimeValid (1), NotValidForUsage (16), OfflineRevocation (16777216), PartialChain (65536), RevocationStatusUnknown (64), Revoked (4), UntrustedRoot (32) """
    CtlNotSignatureValid: X509ChainStatusFlags = ...
    CtlNotTimeValid: X509ChainStatusFlags = ...
    CtlNotValidForUsage: X509ChainStatusFlags = ...
    Cyclic: X509ChainStatusFlags = ...
    ExplicitDistrust: X509ChainStatusFlags = ...
    HasExcludedNameConstraint: X509ChainStatusFlags = ...
    HasNotDefinedNameConstraint: X509ChainStatusFlags = ...
    HasNotPermittedNameConstraint: X509ChainStatusFlags = ...
    HasNotSupportedCriticalExtension: X509ChainStatusFlags = ...
    HasNotSupportedNameConstraint: X509ChainStatusFlags = ...
    HasWeakSignature: X509ChainStatusFlags = ...
    InvalidBasicConstraints: X509ChainStatusFlags = ...
    InvalidExtension: X509ChainStatusFlags = ...
    InvalidNameConstraints: X509ChainStatusFlags = ...
    InvalidPolicyConstraints: X509ChainStatusFlags = ...
    NoError: X509ChainStatusFlags = ...
    NoIssuanceChainPolicy: X509ChainStatusFlags = ...
    NotSignatureValid: X509ChainStatusFlags = ...
    NotTimeNested: X509ChainStatusFlags = ...
    NotTimeValid: X509ChainStatusFlags = ...
    NotValidForUsage: X509ChainStatusFlags = ...
    OfflineRevocation: X509ChainStatusFlags = ...
    PartialChain: X509ChainStatusFlags = ...
    RevocationStatusUnknown: X509ChainStatusFlags = ...
    Revoked: X509ChainStatusFlags = ...
    UntrustedRoot: X509ChainStatusFlags = ...
    value__ = ...


class X509ContentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509ContentType, values: Authenticode (6), Cert (1), Pfx (3), Pkcs12 (3), Pkcs7 (5), SerializedCert (2), SerializedStore (4), Unknown (0) """
    Authenticode: X509ContentType = ...
    Cert: X509ContentType = ...
    Pfx: X509ContentType = ...
    Pkcs12: X509ContentType = ...
    Pkcs7: X509ContentType = ...
    SerializedCert: X509ContentType = ...
    SerializedStore: X509ContentType = ...
    Unknown: X509ContentType = ...
    value__ = ...


class X509EnhancedKeyUsageExtension(X509Extension): # skipped bases: <type 'object'>
    """
    X509EnhancedKeyUsageExtension()
    X509EnhancedKeyUsageExtension(enhancedKeyUsages: OidCollection, critical: bool)
    X509EnhancedKeyUsageExtension(encodedEnhancedKeyUsages: AsnEncodedData, critical: bool)
    """
    @property
    def EnhancedKeyUsages(self) -> OidCollection:
        """ Get: EnhancedKeyUsages(self: X509EnhancedKeyUsageExtension) -> OidCollection """
        ...



class X509ExtensionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ X509ExtensionCollection() """
    def Add(self, extension:X509Extension) -> int:
        """ Add(self: X509ExtensionCollection, extension: X509Extension) -> int """
        ...

    def GetEnumerator(self) -> X509ExtensionEnumerator:
        """ GetEnumerator(self: X509ExtensionCollection) -> X509ExtensionEnumerator """
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


class X509ExtensionEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class X509FindType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509FindType, values: FindByApplicationPolicy (10), FindByCertificatePolicy (11), FindByExtension (12), FindByIssuerDistinguishedName (4), FindByIssuerName (3), FindByKeyUsage (13), FindBySerialNumber (5), FindBySubjectDistinguishedName (2), FindBySubjectKeyIdentifier (14), FindBySubjectName (1), FindByTemplateName (9), FindByThumbprint (0), FindByTimeExpired (8), FindByTimeNotYetValid (7), FindByTimeValid (6) """
    FindByApplicationPolicy: X509FindType = ...
    FindByCertificatePolicy: X509FindType = ...
    FindByExtension: X509FindType = ...
    FindByIssuerDistinguishedName: X509FindType = ...
    FindByIssuerName: X509FindType = ...
    FindByKeyUsage: X509FindType = ...
    FindBySerialNumber: X509FindType = ...
    FindBySubjectDistinguishedName: X509FindType = ...
    FindBySubjectKeyIdentifier: X509FindType = ...
    FindBySubjectName: X509FindType = ...
    FindByTemplateName: X509FindType = ...
    FindByThumbprint: X509FindType = ...
    FindByTimeExpired: X509FindType = ...
    FindByTimeNotYetValid: X509FindType = ...
    FindByTimeValid: X509FindType = ...
    value__ = ...


class X509IncludeOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509IncludeOption, values: EndCertOnly (2), ExcludeRoot (1), None (0), WholeChain (3) """
    EndCertOnly: X509IncludeOption = ...
    ExcludeRoot: X509IncludeOption = ...
    value__ = ...
    WholeChain: X509IncludeOption = ...


class X509KeyStorageFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) X509KeyStorageFlags, values: DefaultKeySet (0), EphemeralKeySet (32), Exportable (4), MachineKeySet (2), PersistKeySet (16), UserKeySet (1), UserProtected (8) """
    DefaultKeySet: X509KeyStorageFlags = ...
    EphemeralKeySet: X509KeyStorageFlags = ...
    Exportable: X509KeyStorageFlags = ...
    MachineKeySet: X509KeyStorageFlags = ...
    PersistKeySet: X509KeyStorageFlags = ...
    UserKeySet: X509KeyStorageFlags = ...
    UserProtected: X509KeyStorageFlags = ...
    value__ = ...


class X509KeyUsageExtension(X509Extension): # skipped bases: <type 'object'>
    """
    X509KeyUsageExtension()
    X509KeyUsageExtension(keyUsages: X509KeyUsageFlags, critical: bool)
    X509KeyUsageExtension(encodedKeyUsage: AsnEncodedData, critical: bool)
    """
    @property
    def KeyUsages(self) -> X509KeyUsageFlags:
        """ Get: KeyUsages(self: X509KeyUsageExtension) -> X509KeyUsageFlags """
        ...



class X509KeyUsageFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) X509KeyUsageFlags, values: CrlSign (2), DataEncipherment (16), DecipherOnly (32768), DigitalSignature (128), EncipherOnly (1), KeyAgreement (8), KeyCertSign (4), KeyEncipherment (32), None (0), NonRepudiation (64) """
    CrlSign: X509KeyUsageFlags = ...
    DataEncipherment: X509KeyUsageFlags = ...
    DecipherOnly: X509KeyUsageFlags = ...
    DigitalSignature: X509KeyUsageFlags = ...
    EncipherOnly: X509KeyUsageFlags = ...
    KeyAgreement: X509KeyUsageFlags = ...
    KeyCertSign: X509KeyUsageFlags = ...
    KeyEncipherment: X509KeyUsageFlags = ...
    NonRepudiation: X509KeyUsageFlags = ...
    value__ = ...


class X509NameType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509NameType, values: DnsFromAlternativeName (4), DnsName (3), EmailName (1), SimpleName (0), UpnName (2), UrlName (5) """
    DnsFromAlternativeName: X509NameType = ...
    DnsName: X509NameType = ...
    EmailName: X509NameType = ...
    SimpleName: X509NameType = ...
    UpnName: X509NameType = ...
    UrlName: X509NameType = ...
    value__ = ...


class X509RevocationFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509RevocationFlag, values: EndCertificateOnly (0), EntireChain (1), ExcludeRoot (2) """
    EndCertificateOnly: X509RevocationFlag = ...
    EntireChain: X509RevocationFlag = ...
    ExcludeRoot: X509RevocationFlag = ...
    value__ = ...


class X509RevocationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509RevocationMode, values: NoCheck (0), Offline (2), Online (1) """
    NoCheck: X509RevocationMode = ...
    Offline: X509RevocationMode = ...
    Online: X509RevocationMode = ...
    value__ = ...


class X509SelectionFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509SelectionFlag, values: MultiSelection (1), SingleSelection (0) """
    MultiSelection: X509SelectionFlag = ...
    SingleSelection: X509SelectionFlag = ...
    value__ = ...


class X509SignatureGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PublicKey(self) -> PublicKey:
        """ Get: PublicKey(self: X509SignatureGenerator) -> PublicKey """
        ...


    def BuildPublicKey(self, *args): #cannot find CLR method
        """ BuildPublicKey(self: X509SignatureGenerator) -> PublicKey """
        ...

    @staticmethod
    def CreateForECDsa(key:ECDsa) -> X509SignatureGenerator:
        """ CreateForECDsa(key: ECDsa) -> X509SignatureGenerator """
        ...

    @staticmethod
    def CreateForRSA(key:RSA, signaturePadding:RSASignaturePadding) -> X509SignatureGenerator:
        """ CreateForRSA(key: RSA, signaturePadding: RSASignaturePadding) -> X509SignatureGenerator """
        ...

    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm:HashAlgorithmName) -> Array:
        """ GetSignatureAlgorithmIdentifier(self: X509SignatureGenerator, hashAlgorithm: HashAlgorithmName) -> Array[Byte] """
        ...

    def SignData(self, data:Array, hashAlgorithm:HashAlgorithmName) -> Array:
        """ SignData(self: X509SignatureGenerator, data: Array[Byte], hashAlgorithm: HashAlgorithmName) -> Array[Byte] """
        ...


class X509Store(IDisposable): # skipped bases: <type 'object'>
    """
    X509Store()
    X509Store(storeName: str)
    X509Store(storeName: StoreName)
    X509Store(storeLocation: StoreLocation)
    X509Store(storeName: StoreName, storeLocation: StoreLocation)
    X509Store(storeName: str, storeLocation: StoreLocation)
    X509Store(storeHandle: IntPtr)
    """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: X509Store) -> X509Certificate2Collection """
        ...

    @property
    def Location(self) -> StoreLocation:
        """ Get: Location(self: X509Store) -> StoreLocation """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: X509Store) -> str """
        ...

    @property
    def StoreHandle(self) -> IntPtr:
        """ Get: StoreHandle(self: X509Store) -> IntPtr """
        ...


    def Add(self, certificate:X509Certificate2): # -> 
        """ Add(self: X509Store, certificate: X509Certificate2) """
        ...

    def AddRange(self, certificates:X509Certificate2Collection): # -> 
        """ AddRange(self: X509Store, certificates: X509Certificate2Collection) """
        ...

    def Close(self): # -> 
        """ Close(self: X509Store) """
        ...

    def Open(self, flags:OpenFlags): # -> 
        """ Open(self: X509Store, flags: OpenFlags) """
        ...

    def Remove(self, certificate:X509Certificate2): # -> 
        """ Remove(self: X509Store, certificate: X509Certificate2) """
        ...

    def RemoveRange(self, certificates:X509Certificate2Collection): # -> 
        """ RemoveRange(self: X509Store, certificates: X509Certificate2Collection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class X509SubjectKeyIdentifierExtension(X509Extension): # skipped bases: <type 'object'>
    """
    X509SubjectKeyIdentifierExtension()
    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: str, critical: bool)
    X509SubjectKeyIdentifierExtension(subjectKeyIdentifier: Array[Byte], critical: bool)
    X509SubjectKeyIdentifierExtension(encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool)
    X509SubjectKeyIdentifierExtension(key: PublicKey, critical: bool)
    X509SubjectKeyIdentifierExtension(key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool)
    """
    @property
    def SubjectKeyIdentifier(self) -> str:
        """ Get: SubjectKeyIdentifier(self: X509SubjectKeyIdentifierExtension) -> str """
        ...



class X509SubjectKeyIdentifierHashAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum X509SubjectKeyIdentifierHashAlgorithm, values: CapiSha1 (2), Sha1 (0), ShortSha1 (1) """
    CapiSha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    Sha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    ShortSha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    value__ = ...


class X509VerificationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) X509VerificationFlags, values: AllFlags (4095), AllowUnknownCertificateAuthority (16), IgnoreCertificateAuthorityRevocationUnknown (1024), IgnoreCtlNotTimeValid (2), IgnoreCtlSignerRevocationUnknown (512), IgnoreEndRevocationUnknown (256), IgnoreInvalidBasicConstraints (8), IgnoreInvalidName (64), IgnoreInvalidPolicy (128), IgnoreNotTimeNested (4), IgnoreNotTimeValid (1), IgnoreRootRevocationUnknown (2048), IgnoreWrongUsage (32), NoFlag (0) """
    AllFlags: X509VerificationFlags = ...
    AllowUnknownCertificateAuthority: X509VerificationFlags = ...
    IgnoreCertificateAuthorityRevocationUnknown: X509VerificationFlags = ...
    IgnoreCtlNotTimeValid: X509VerificationFlags = ...
    IgnoreCtlSignerRevocationUnknown: X509VerificationFlags = ...
    IgnoreEndRevocationUnknown: X509VerificationFlags = ...
    IgnoreInvalidBasicConstraints: X509VerificationFlags = ...
    IgnoreInvalidName: X509VerificationFlags = ...
    IgnoreInvalidPolicy: X509VerificationFlags = ...
    IgnoreNotTimeNested: X509VerificationFlags = ...
    IgnoreNotTimeValid: X509VerificationFlags = ...
    IgnoreRootRevocationUnknown: X509VerificationFlags = ...
    IgnoreWrongUsage: X509VerificationFlags = ...
    NoFlag: X509VerificationFlags = ...
    value__ = ...


