# encoding: utf-8
# module System.Security.Cryptography calls itself Cryptography
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from Microsoft.Win32.SafeHandles import (SafeNCryptKeyHandle, 
    SafeNCryptProviderHandle, SafeNCryptSecretHandle)

from System import (ActivationContext, Array, Enum, IDisposable, IEquatable, 
    IntPtr, Nullable, SystemException, Type)

from System.Collections import ICollection, IEnumerator

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IO import Stream

from System.Security import ManifestKinds, SecureString

from System.Security.AccessControl import CryptoKeySecurity

from System.Security.Cryptography.X509Certificates import (X509RevocationFlag, 
    X509RevocationMode)

from typing import Self

"""The following names are not found in the module: (
    AuthenticodeSignatureInformation, BoundEvent, CngKeyBlobFormat, 
    CngKeyCreationParameters, CngKeyOpenOptions, CngKeyUsages, CngProperty, 
    CngPropertyCollection, CngPropertyOptions, CngProvider, CngUIPolicy, 
    CngUIProtectionLevels, CryptographicAttributeObjectEnumerator, 
    ECDiffieHellmanKeyDerivationFunction, ECDiffieHellmanPublicKey, 
    ECParameters, ICngSymmetricAlgorithm, 
    ManifestSignatureInformationCollection, StrongNameSignatureInformation, 
    field#)
"""

# no functions
# classes

class SymmetricAlgorithm(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BlockSize(self) -> int:
        """
        Get: BlockSize(self: SymmetricAlgorithm) -> int
        Set: BlockSize(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def FeedbackSize(self) -> int:
        """
        Get: FeedbackSize(self: SymmetricAlgorithm) -> int
        Set: FeedbackSize(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def IV(self) -> Array:
        """
        Get: IV(self: SymmetricAlgorithm) -> Array[Byte]
        Set: IV(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def Key(self) -> Array:
        """
        Get: Key(self: SymmetricAlgorithm) -> Array[Byte]
        Set: Key(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: SymmetricAlgorithm) -> int
        Set: KeySize(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def LegalBlockSizes(self) -> Array:
        """ Get: LegalBlockSizes(self: SymmetricAlgorithm) -> Array[KeySizes] """
        ...

    @property
    def LegalKeySizes(self) -> Array:
        """ Get: LegalKeySizes(self: SymmetricAlgorithm) -> Array[KeySizes] """
        ...

    @property
    def Mode(self) -> CipherMode:
        """
        Get: Mode(self: SymmetricAlgorithm) -> CipherMode
        Set: Mode(self: SymmetricAlgorithm) = value
        """
        ...

    @property
    def Padding(self) -> PaddingMode:
        """
        Get: Padding(self: SymmetricAlgorithm) -> PaddingMode
        Set: Padding(self: SymmetricAlgorithm) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: SymmetricAlgorithm) """
        ...

    @staticmethod
    def Create(algName:str = ...) -> SymmetricAlgorithm:
        """
        Create(algName: str) -> SymmetricAlgorithm
        Create() -> SymmetricAlgorithm
        """
        ...

    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateDecryptor(self: SymmetricAlgorithm) -> ICryptoTransform
        CreateDecryptor(self: SymmetricAlgorithm, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateEncryptor(self: SymmetricAlgorithm) -> ICryptoTransform
        CreateEncryptor(self: SymmetricAlgorithm, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: SymmetricAlgorithm) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: SymmetricAlgorithm) """
        ...

    def ValidKeySize(self, bitLength:int) -> bool:
        """ ValidKeySize(self: SymmetricAlgorithm, bitLength: int) -> bool """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class Aes(SymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class AesCng(ICngSymmetricAlgorithm, Aes): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    AesCng()
    AesCng(keyName: str)
    AesCng(keyName: str, provider: CngProvider)
    AesCng(keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions)
    """
    @property
    def Key(self) -> Array:
        """
        Get: Key(self: AesCng) -> Array[Byte]
        Set: Key(self: AesCng) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: AesCng) -> int
        Set: KeySize(self: AesCng) = value
        """
        ...


    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateDecryptor(self: AesCng) -> ICryptoTransform
        CreateDecryptor(self: AesCng, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateEncryptor(self: AesCng) -> ICryptoTransform
        CreateEncryptor(self: AesCng, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: AesCng) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: AesCng) """
        ...

    def __new__(cls, keyName:str = ..., provider = ..., openOptions = ...) -> Self: # Not found arg types: {'provider': 'CngProvider', 'openOptions': 'CngKeyOpenOptions'}
        """
        __new__(cls: type)
        __new__(cls: type, keyName: str)
        __new__(cls: type, keyName: str, provider: CngProvider)
        __new__(cls: type, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions)
        """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class AesCryptoServiceProvider(Aes): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ AesCryptoServiceProvider() """
    @property
    def Key(self) -> Array:
        """
        Get: Key(self: AesCryptoServiceProvider) -> Array[Byte]
        Set: Key(self: AesCryptoServiceProvider) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: AesCryptoServiceProvider) -> int
        Set: KeySize(self: AesCryptoServiceProvider) = value
        """
        ...


    def CreateDecryptor(self, key:Array = ..., iv:Array = ...) -> ICryptoTransform:
        """
        CreateDecryptor(self: AesCryptoServiceProvider) -> ICryptoTransform
        CreateDecryptor(self: AesCryptoServiceProvider, key: Array[Byte], iv: Array[Byte]) -> ICryptoTransform
        """
        ...

    def CreateEncryptor(self, key:Array = ..., iv:Array = ...) -> ICryptoTransform:
        """
        CreateEncryptor(self: AesCryptoServiceProvider) -> ICryptoTransform
        CreateEncryptor(self: AesCryptoServiceProvider, key: Array[Byte], iv: Array[Byte]) -> ICryptoTransform
        """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: AesCryptoServiceProvider) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: AesCryptoServiceProvider) """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class AesManaged(Aes): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ AesManaged() """
    @property
    def FeedbackSize(self) -> int:
        """
        Get: FeedbackSize(self: AesManaged) -> int
        Set: FeedbackSize(self: AesManaged) = value
        """
        ...

    @property
    def IV(self) -> Array:
        """
        Get: IV(self: AesManaged) -> Array[Byte]
        Set: IV(self: AesManaged) = value
        """
        ...

    @property
    def Key(self) -> Array:
        """
        Get: Key(self: AesManaged) -> Array[Byte]
        Set: Key(self: AesManaged) = value
        """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: AesManaged) -> int
        Set: KeySize(self: AesManaged) = value
        """
        ...

    @property
    def Mode(self) -> CipherMode:
        """
        Get: Mode(self: AesManaged) -> CipherMode
        Set: Mode(self: AesManaged) = value
        """
        ...

    @property
    def Padding(self) -> PaddingMode:
        """
        Get: Padding(self: AesManaged) -> PaddingMode
        Set: Padding(self: AesManaged) = value
        """
        ...


    def CreateDecryptor(self, key:Array = ..., iv:Array = ...) -> ICryptoTransform:
        """
        CreateDecryptor(self: AesManaged) -> ICryptoTransform
        CreateDecryptor(self: AesManaged, key: Array[Byte], iv: Array[Byte]) -> ICryptoTransform
        """
        ...

    def CreateEncryptor(self, key:Array = ..., iv:Array = ...) -> ICryptoTransform:
        """
        CreateEncryptor(self: AesManaged) -> ICryptoTransform
        CreateEncryptor(self: AesManaged, key: Array[Byte], iv: Array[Byte]) -> ICryptoTransform
        """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: AesManaged) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: AesManaged) """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class AsnEncodedData: # skipped bases: <type 'object'>, <type 'object'>
    """
    AsnEncodedData(rawData: Array[Byte])
    AsnEncodedData(oid: str, rawData: Array[Byte])
    AsnEncodedData(oid: Oid, rawData: Array[Byte])
    AsnEncodedData(asnEncodedData: AsnEncodedData)
    """
    @property
    def Oid(self) -> Oid:
        """
        Get: Oid(self: AsnEncodedData) -> Oid
        Set: Oid(self: AsnEncodedData) = value
        """
        ...

    @property
    def RawData(self) -> Array:
        """
        Get: RawData(self: AsnEncodedData) -> Array[Byte]
        Set: RawData(self: AsnEncodedData) = value
        """
        ...


    def CopyFrom(self, asnEncodedData:AsnEncodedData): # -> 
        """ CopyFrom(self: AsnEncodedData, asnEncodedData: AsnEncodedData) """
        ...

    def Format(self, multiLine:bool) -> str:
        """ Format(self: AsnEncodedData, multiLine: bool) -> str """
        ...


class AsnEncodedDataCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    AsnEncodedDataCollection()
    AsnEncodedDataCollection(asnEncodedData: AsnEncodedData)
    """
    def Add(self, asnEncodedData:AsnEncodedData) -> int:
        """ Add(self: AsnEncodedDataCollection, asnEncodedData: AsnEncodedData) -> int """
        ...

    def GetEnumerator(self) -> AsnEncodedDataEnumerator:
        """ GetEnumerator(self: AsnEncodedDataCollection) -> AsnEncodedDataEnumerator """
        ...

    def Remove(self, asnEncodedData:AsnEncodedData): # -> 
        """ Remove(self: AsnEncodedDataCollection, asnEncodedData: AsnEncodedData) """
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


class AsnEncodedDataEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AsymmetricAlgorithm(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """ Get: KeyExchangeAlgorithm(self: AsymmetricAlgorithm) -> str """
        ...

    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: AsymmetricAlgorithm) -> int
        Set: KeySize(self: AsymmetricAlgorithm) = value
        """
        ...

    @property
    def LegalKeySizes(self) -> Array:
        """ Get: LegalKeySizes(self: AsymmetricAlgorithm) -> Array[KeySizes] """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """ Get: SignatureAlgorithm(self: AsymmetricAlgorithm) -> str """
        ...


    def Clear(self): # -> 
        """ Clear(self: AsymmetricAlgorithm) """
        ...

    @staticmethod
    def Create(algName:str = ...) -> AsymmetricAlgorithm:
        """
        Create(algName: str) -> AsymmetricAlgorithm
        Create() -> AsymmetricAlgorithm
        """
        ...

    def FromXmlString(self, xmlString:str): # -> 
        """ FromXmlString(self: AsymmetricAlgorithm, xmlString: str) """
        ...

    def ToXmlString(self, includePrivateParameters:bool) -> str:
        """ ToXmlString(self: AsymmetricAlgorithm, includePrivateParameters: bool) -> str """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class AsymmetricKeyExchangeDeformatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Parameters(self) -> str:
        """
        Get: Parameters(self: AsymmetricKeyExchangeDeformatter) -> str
        Set: Parameters(self: AsymmetricKeyExchangeDeformatter) = value
        """
        ...


    def DecryptKeyExchange(self, rgb:Array) -> Array:
        """ DecryptKeyExchange(self: AsymmetricKeyExchangeDeformatter, rgb: Array[Byte]) -> Array[Byte] """
        ...

    def SetKey(self, key:AsymmetricAlgorithm): # -> 
        """ SetKey(self: AsymmetricKeyExchangeDeformatter, key: AsymmetricAlgorithm) """
        ...


class AsymmetricKeyExchangeFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Parameters(self) -> str:
        """ Get: Parameters(self: AsymmetricKeyExchangeFormatter) -> str """
        ...


    def CreateKeyExchange(self, data:Array, symAlgType:Type = ...) -> Array:
        """
        CreateKeyExchange(self: AsymmetricKeyExchangeFormatter, data: Array[Byte]) -> Array[Byte]
        CreateKeyExchange(self: AsymmetricKeyExchangeFormatter, data: Array[Byte], symAlgType: Type) -> Array[Byte]
        """
        ...

    def SetKey(self, key:AsymmetricAlgorithm): # -> 
        """ SetKey(self: AsymmetricKeyExchangeFormatter, key: AsymmetricAlgorithm) """
        ...


class AsymmetricSignatureDeformatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def SetHashAlgorithm(self, strName:str): # -> 
        """ SetHashAlgorithm(self: AsymmetricSignatureDeformatter, strName: str) """
        ...

    def SetKey(self, key:AsymmetricAlgorithm): # -> 
        """ SetKey(self: AsymmetricSignatureDeformatter, key: AsymmetricAlgorithm) """
        ...

    def VerifySignature(self, *__args) -> bool:
        """
        VerifySignature(self: AsymmetricSignatureDeformatter, hash: HashAlgorithm, rgbSignature: Array[Byte]) -> bool
        VerifySignature(self: AsymmetricSignatureDeformatter, rgbHash: Array[Byte], rgbSignature: Array[Byte]) -> bool
        """
        ...


class AsymmetricSignatureFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateSignature(self, *__args:HashAlgorithm) -> Array:
        """
        CreateSignature(self: AsymmetricSignatureFormatter, hash: HashAlgorithm) -> Array[Byte]
        CreateSignature(self: AsymmetricSignatureFormatter, rgbHash: Array[Byte]) -> Array[Byte]
        """
        ...

    def SetHashAlgorithm(self, strName:str): # -> 
        """ SetHashAlgorithm(self: AsymmetricSignatureFormatter, strName: str) """
        ...

    def SetKey(self, key:AsymmetricAlgorithm): # -> 
        """ SetKey(self: AsymmetricSignatureFormatter, key: AsymmetricAlgorithm) """
        ...


class CipherMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CipherMode, values: CBC (1), CFB (4), CTS (5), ECB (2), OFB (3) """
    CBC: CipherMode = ...
    CFB: CipherMode = ...
    CTS: CipherMode = ...
    ECB: CipherMode = ...
    OFB: CipherMode = ...
    value__ = ...


class CngAlgorithm(IEquatable): # skipped bases: <type 'object'>
    """ CngAlgorithm(algorithm: str) """
    @property
    def Algorithm(self) -> str:
        """ Get: Algorithm(self: CngAlgorithm) -> str """
        ...

    @property
    def ECDiffieHellman(self) -> CngAlgorithm:
        """ Get: ECDiffieHellman() -> CngAlgorithm """
        ...

    @property
    def ECDiffieHellmanP256(self) -> CngAlgorithm:
        """ Get: ECDiffieHellmanP256() -> CngAlgorithm """
        ...

    @property
    def ECDiffieHellmanP384(self) -> CngAlgorithm:
        """ Get: ECDiffieHellmanP384() -> CngAlgorithm """
        ...

    @property
    def ECDiffieHellmanP521(self) -> CngAlgorithm:
        """ Get: ECDiffieHellmanP521() -> CngAlgorithm """
        ...

    @property
    def ECDsa(self) -> CngAlgorithm:
        """ Get: ECDsa() -> CngAlgorithm """
        ...

    @property
    def ECDsaP256(self) -> CngAlgorithm:
        """ Get: ECDsaP256() -> CngAlgorithm """
        ...

    @property
    def ECDsaP384(self) -> CngAlgorithm:
        """ Get: ECDsaP384() -> CngAlgorithm """
        ...

    @property
    def ECDsaP521(self) -> CngAlgorithm:
        """ Get: ECDsaP521() -> CngAlgorithm """
        ...

    @property
    def MD5(self) -> CngAlgorithm:
        """ Get: MD5() -> CngAlgorithm """
        ...

    @property
    def Rsa(self) -> CngAlgorithm:
        """ Get: Rsa() -> CngAlgorithm """
        ...

    @property
    def Sha1(self) -> CngAlgorithm:
        """ Get: Sha1() -> CngAlgorithm """
        ...

    @property
    def Sha256(self) -> CngAlgorithm:
        """ Get: Sha256() -> CngAlgorithm """
        ...

    @property
    def Sha384(self) -> CngAlgorithm:
        """ Get: Sha384() -> CngAlgorithm """
        ...

    @property
    def Sha512(self) -> CngAlgorithm:
        """ Get: Sha512() -> CngAlgorithm """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: CngAlgorithm) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CngAlgorithm) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class CngAlgorithmGroup(IEquatable): # skipped bases: <type 'object'>
    """ CngAlgorithmGroup(algorithmGroup: str) """
    @property
    def AlgorithmGroup(self) -> str:
        """ Get: AlgorithmGroup(self: CngAlgorithmGroup) -> str """
        ...

    @property
    def DiffieHellman(self) -> CngAlgorithmGroup:
        """ Get: DiffieHellman() -> CngAlgorithmGroup """
        ...

    @property
    def Dsa(self) -> CngAlgorithmGroup:
        """ Get: Dsa() -> CngAlgorithmGroup """
        ...

    @property
    def ECDiffieHellman(self) -> CngAlgorithmGroup:
        """ Get: ECDiffieHellman() -> CngAlgorithmGroup """
        ...

    @property
    def ECDsa(self) -> CngAlgorithmGroup:
        """ Get: ECDsa() -> CngAlgorithmGroup """
        ...

    @property
    def Rsa(self) -> CngAlgorithmGroup:
        """ Get: Rsa() -> CngAlgorithmGroup """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: CngAlgorithmGroup) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CngAlgorithmGroup) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class CngExportPolicies(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngExportPolicies, values: AllowArchiving (4), AllowExport (1), AllowPlaintextArchiving (8), AllowPlaintextExport (2), None (0) """
    AllowArchiving: CngExportPolicies = ...
    AllowExport: CngExportPolicies = ...
    AllowPlaintextArchiving: CngExportPolicies = ...
    AllowPlaintextExport: CngExportPolicies = ...
    value__ = ...


class CngKey(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Algorithm(self) -> CngAlgorithm:
        """ Get: Algorithm(self: CngKey) -> CngAlgorithm """
        ...

    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup:
        """ Get: AlgorithmGroup(self: CngKey) -> CngAlgorithmGroup """
        ...

    @property
    def ExportPolicy(self) -> CngExportPolicies:
        """ Get: ExportPolicy(self: CngKey) -> CngExportPolicies """
        ...

    @property
    def Handle(self) -> SafeNCryptKeyHandle:
        """ Get: Handle(self: CngKey) -> SafeNCryptKeyHandle """
        ...

    @property
    def IsEphemeral(self) -> bool:
        """ Get: IsEphemeral(self: CngKey) -> bool """
        ...

    @property
    def IsMachineKey(self) -> bool:
        """ Get: IsMachineKey(self: CngKey) -> bool """
        ...

    @property
    def KeyName(self) -> str:
        """ Get: KeyName(self: CngKey) -> str """
        ...

    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: CngKey) -> int """
        ...

    @property
    def KeyUsage(self): # -> CngKeyUsages
        """ Get: KeyUsage(self: CngKey) -> CngKeyUsages """
        ...

    @property
    def ParentWindowHandle(self) -> IntPtr:
        """
        Get: ParentWindowHandle(self: CngKey) -> IntPtr
        Set: ParentWindowHandle(self: CngKey) = value
        """
        ...

    @property
    def Provider(self): # -> CngProvider
        """ Get: Provider(self: CngKey) -> CngProvider """
        ...

    @property
    def ProviderHandle(self) -> SafeNCryptProviderHandle:
        """ Get: ProviderHandle(self: CngKey) -> SafeNCryptProviderHandle """
        ...

    @property
    def UIPolicy(self): # -> CngUIPolicy
        """ Get: UIPolicy(self: CngKey) -> CngUIPolicy """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: CngKey) -> str """
        ...


    @staticmethod
    def Create(algorithm:CngAlgorithm, keyName:str = ..., creationParameters = ...) -> CngKey: # Not found arg types: {'creationParameters': 'CngKeyCreationParameters'}
        """
        Create(algorithm: CngAlgorithm) -> CngKey
        Create(algorithm: CngAlgorithm, keyName: str) -> CngKey
        Create(algorithm: CngAlgorithm, keyName: str, creationParameters: CngKeyCreationParameters) -> CngKey
        """
        ...

    def Delete(self): # -> 
        """ Delete(self: CngKey) """
        ...

    @staticmethod
    def Exists(keyName:str, provider = ..., options = ...) -> bool: # Not found arg types: {'options': 'CngKeyOpenOptions', 'provider': 'CngProvider'}
        """
        Exists(keyName: str) -> bool
        Exists(keyName: str, provider: CngProvider) -> bool
        Exists(keyName: str, provider: CngProvider, options: CngKeyOpenOptions) -> bool
        """
        ...

    def Export(self, format) -> Array: # Not found arg types: {'format': 'CngKeyBlobFormat'}
        """ Export(self: CngKey, format: CngKeyBlobFormat) -> Array[Byte] """
        ...

    def GetProperty(self, name:str, options): # -> CngProperty # Not found arg types: {'options': 'CngPropertyOptions'}
        """ GetProperty(self: CngKey, name: str, options: CngPropertyOptions) -> CngProperty """
        ...

    def HasProperty(self, name:str, options) -> bool: # Not found arg types: {'options': 'CngPropertyOptions'}
        """ HasProperty(self: CngKey, name: str, options: CngPropertyOptions) -> bool """
        ...

    @staticmethod
    def Import(keyBlob:Array, format, provider = ...) -> CngKey: # Not found arg types: {'format': 'CngKeyBlobFormat', 'provider': 'CngProvider'}
        """
        Import(keyBlob: Array[Byte], format: CngKeyBlobFormat) -> CngKey
        Import(keyBlob: Array[Byte], format: CngKeyBlobFormat, provider: CngProvider) -> CngKey
        """
        ...

    @staticmethod
    def Open(*__args:str) -> CngKey:
        """
        Open(keyName: str) -> CngKey
        Open(keyName: str, provider: CngProvider) -> CngKey
        Open(keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> CngKey
        Open(keyHandle: SafeNCryptKeyHandle, keyHandleOpenOptions: CngKeyHandleOpenOptions) -> CngKey
        """
        ...

    def SetProperty(self, property): # ->  # Not found arg types: {'property': 'CngProperty'}
        """ SetProperty(self: CngKey, property: CngProperty) """
        ...


class CngKeyBlobFormat(IEquatable): # skipped bases: <type 'object'>
    """ CngKeyBlobFormat(format: str) """
    @property
    def EccFullPrivateBlob(self) -> CngKeyBlobFormat:
        """ Get: EccFullPrivateBlob() -> CngKeyBlobFormat """
        ...

    @property
    def EccFullPublicBlob(self) -> CngKeyBlobFormat:
        """ Get: EccFullPublicBlob() -> CngKeyBlobFormat """
        ...

    @property
    def EccPrivateBlob(self) -> CngKeyBlobFormat:
        """ Get: EccPrivateBlob() -> CngKeyBlobFormat """
        ...

    @property
    def EccPublicBlob(self) -> CngKeyBlobFormat:
        """ Get: EccPublicBlob() -> CngKeyBlobFormat """
        ...

    @property
    def Format(self) -> str:
        """ Get: Format(self: CngKeyBlobFormat) -> str """
        ...

    @property
    def GenericPrivateBlob(self) -> CngKeyBlobFormat:
        """ Get: GenericPrivateBlob() -> CngKeyBlobFormat """
        ...

    @property
    def GenericPublicBlob(self) -> CngKeyBlobFormat:
        """ Get: GenericPublicBlob() -> CngKeyBlobFormat """
        ...

    @property
    def OpaqueTransportBlob(self) -> CngKeyBlobFormat:
        """ Get: OpaqueTransportBlob() -> CngKeyBlobFormat """
        ...

    @property
    def Pkcs8PrivateBlob(self) -> CngKeyBlobFormat:
        """ Get: Pkcs8PrivateBlob() -> CngKeyBlobFormat """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: CngKeyBlobFormat) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CngKeyBlobFormat) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class CngKeyCreationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngKeyCreationOptions, values: MachineKey (32), None (0), OverwriteExistingKey (128) """
    MachineKey: CngKeyCreationOptions = ...
    OverwriteExistingKey: CngKeyCreationOptions = ...
    value__ = ...


class CngKeyCreationParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ CngKeyCreationParameters() """
    @property
    def ExportPolicy(self) -> Nullable:
        """
        Get: ExportPolicy(self: CngKeyCreationParameters) -> Nullable[CngExportPolicies]
        Set: ExportPolicy(self: CngKeyCreationParameters) = value
        """
        ...

    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions:
        """
        Get: KeyCreationOptions(self: CngKeyCreationParameters) -> CngKeyCreationOptions
        Set: KeyCreationOptions(self: CngKeyCreationParameters) = value
        """
        ...

    @property
    def KeyUsage(self) -> Nullable:
        """
        Get: KeyUsage(self: CngKeyCreationParameters) -> Nullable[CngKeyUsages]
        Set: KeyUsage(self: CngKeyCreationParameters) = value
        """
        ...

    @property
    def Parameters(self): # -> CngPropertyCollection
        """ Get: Parameters(self: CngKeyCreationParameters) -> CngPropertyCollection """
        ...

    @property
    def ParentWindowHandle(self) -> IntPtr:
        """
        Get: ParentWindowHandle(self: CngKeyCreationParameters) -> IntPtr
        Set: ParentWindowHandle(self: CngKeyCreationParameters) = value
        """
        ...

    @property
    def Provider(self): # -> CngProvider
        """
        Get: Provider(self: CngKeyCreationParameters) -> CngProvider
        Set: Provider(self: CngKeyCreationParameters) = value
        """
        ...

    @property
    def UIPolicy(self): # -> CngUIPolicy
        """
        Get: UIPolicy(self: CngKeyCreationParameters) -> CngUIPolicy
        Set: UIPolicy(self: CngKeyCreationParameters) = value
        """
        ...



class CngKeyHandleOpenOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngKeyHandleOpenOptions, values: EphemeralKey (1), None (0) """
    EphemeralKey: CngKeyHandleOpenOptions = ...
    value__ = ...


class CngKeyOpenOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngKeyOpenOptions, values: MachineKey (32), None (0), Silent (64), UserKey (0) """
    MachineKey: CngKeyOpenOptions = ...
    Silent: CngKeyOpenOptions = ...
    UserKey: CngKeyOpenOptions = ...
    value__ = ...


class CngKeyUsages(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngKeyUsages, values: AllUsages (16777215), Decryption (1), KeyAgreement (4), None (0), Signing (2) """
    AllUsages: CngKeyUsages = ...
    Decryption: CngKeyUsages = ...
    KeyAgreement: CngKeyUsages = ...
    Signing: CngKeyUsages = ...
    value__ = ...


class CngProperty(IEquatable): # skipped bases: <type 'object'>
    """ CngProperty(name: str, value: Array[Byte], options: CngPropertyOptions) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CngProperty) -> str """
        ...

    @property
    def Options(self): # -> CngPropertyOptions
        """ Get: Options(self: CngProperty) -> CngPropertyOptions """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: CngProperty) -> int """
        ...

    def GetValue(self) -> Array:
        """ GetValue(self: CngProperty) -> Array[Byte] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CngPropertyCollection(Collection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection[CngProperty]'>, <type 'IList'>, <type 'IList[CngProperty]'>, <type 'IEnumerable[CngProperty]'>, <type 'IReadOnlyCollection[CngProperty]'>, <type 'ICollection'>, <type 'IReadOnlyList[CngProperty]'>, <type 'object'>
    """ CngPropertyCollection() """
    pass

class CngPropertyOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngPropertyOptions, values: CustomProperty (1073741824), None (0), Persist (-2147483648) """
    CustomProperty: CngPropertyOptions = ...
    Persist: CngPropertyOptions = ...
    value__ = ...


class CngProvider(IEquatable): # skipped bases: <type 'object'>
    """ CngProvider(provider: str) """
    @property
    def MicrosoftSmartCardKeyStorageProvider(self) -> CngProvider:
        """ Get: MicrosoftSmartCardKeyStorageProvider() -> CngProvider """
        ...

    @property
    def MicrosoftSoftwareKeyStorageProvider(self) -> CngProvider:
        """ Get: MicrosoftSoftwareKeyStorageProvider() -> CngProvider """
        ...

    @property
    def Provider(self) -> str:
        """ Get: Provider(self: CngProvider) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: CngProvider) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CngProvider) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class CngUIPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """
    CngUIPolicy(protectionLevel: CngUIProtectionLevels)
    CngUIPolicy(protectionLevel: CngUIProtectionLevels, friendlyName: str)
    CngUIPolicy(protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str)
    CngUIPolicy(protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str, useContext: str)
    CngUIPolicy(protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str, useContext: str, creationTitle: str)
    """
    @property
    def CreationTitle(self) -> str:
        """ Get: CreationTitle(self: CngUIPolicy) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: CngUIPolicy) -> str """
        ...

    @property
    def FriendlyName(self) -> str:
        """ Get: FriendlyName(self: CngUIPolicy) -> str """
        ...

    @property
    def ProtectionLevel(self): # -> CngUIProtectionLevels
        """ Get: ProtectionLevel(self: CngUIPolicy) -> CngUIProtectionLevels """
        ...

    @property
    def UseContext(self) -> str:
        """ Get: UseContext(self: CngUIPolicy) -> str """
        ...



class CngUIProtectionLevels(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CngUIProtectionLevels, values: ForceHighProtection (2), None (0), ProtectKey (1) """
    ForceHighProtection: CngUIProtectionLevels = ...
    ProtectKey: CngUIProtectionLevels = ...
    value__ = ...


class CryptoAPITransform(ICryptoTransform): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def KeyHandle(self) -> IntPtr:
        """ Get: KeyHandle(self: CryptoAPITransform) -> IntPtr """
        ...


    def Clear(self): # -> 
        """ Clear(self: CryptoAPITransform) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: CryptoAPITransform) """
        ...

    def Reset(self): # -> 
        """ Reset(self: CryptoAPITransform) """
        ...


class CryptoConfig: # skipped bases: <type 'object'>, <type 'object'>
    """ CryptoConfig() """
    @property
    def AllowOnlyFipsAlgorithms(self) -> bool:
        """ Get: AllowOnlyFipsAlgorithms() -> bool """
        ...


    @staticmethod
    def AddAlgorithm(algorithm:Type, names:Array): # -> 
        """ AddAlgorithm(algorithm: Type, *names: Array[str]) """
        ...

    @staticmethod
    def AddOID(oid:str, names:Array): # -> 
        """ AddOID(oid: str, *names: Array[str]) """
        ...

    @staticmethod
    def CreateFromName(name:str, args:Array = ...) -> object:
        """
        CreateFromName(name: str, *args: Array[object]) -> object
        CreateFromName(name: str) -> object
        """
        ...

    @staticmethod
    def EncodeOID(str:str) -> Array:
        """ EncodeOID(str: str) -> Array[Byte] """
        ...

    @staticmethod
    def MapNameToOID(name:str) -> str:
        """ MapNameToOID(name: str) -> str """
        ...



class CryptographicAttributeObject: # skipped bases: <type 'object'>, <type 'object'>
    """
    CryptographicAttributeObject(oid: Oid)
    CryptographicAttributeObject(oid: Oid, values: AsnEncodedDataCollection)
    """
    @property
    def Oid(self) -> Oid:
        """ Get: Oid(self: CryptographicAttributeObject) -> Oid """
        ...

    @property
    def Values(self) -> AsnEncodedDataCollection:
        """ Get: Values(self: CryptographicAttributeObject) -> AsnEncodedDataCollection """
        ...



class CryptographicAttributeObjectCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    CryptographicAttributeObjectCollection()
    CryptographicAttributeObjectCollection(attribute: CryptographicAttributeObject)
    """
    def Add(self, *__args:AsnEncodedData) -> int:
        """
        Add(self: CryptographicAttributeObjectCollection, asnEncodedData: AsnEncodedData) -> int
        Add(self: CryptographicAttributeObjectCollection, attribute: CryptographicAttributeObject) -> int
        """
        ...

    def GetEnumerator(self): # -> CryptographicAttributeObjectEnumerator
        """ GetEnumerator(self: CryptographicAttributeObjectCollection) -> CryptographicAttributeObjectEnumerator """
        ...

    def Remove(self, attribute:CryptographicAttributeObject): # -> 
        """ Remove(self: CryptographicAttributeObjectCollection, attribute: CryptographicAttributeObject) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class CryptographicAttributeObjectEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CryptographicException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CryptographicException()
    CryptographicException(message: str)
    CryptographicException(format: str, insert: str)
    CryptographicException(message: str, inner: Exception)
    CryptographicException(hr: int)
    """
    SerializeObjectState = ...


class CryptographicUnexpectedOperationException(CryptographicException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CryptographicUnexpectedOperationException()
    CryptographicUnexpectedOperationException(message: str)
    CryptographicUnexpectedOperationException(format: str, insert: str)
    CryptographicUnexpectedOperationException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class CryptoStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    CryptoStream(stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode)
    CryptoStream(stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: bool)
    """
    @property
    def HasFlushedFinalBlock(self) -> bool:
        """ Get: HasFlushedFinalBlock(self: CryptoStream) -> bool """
        ...


    def Clear(self): # -> 
        """ Clear(self: CryptoStream) """
        ...

    def FlushFinalBlock(self): # -> 
        """ FlushFinalBlock(self: CryptoStream) """
        ...

    def __new__(cls, stream:Stream, transform:ICryptoTransform, mode:CryptoStreamMode, leaveOpen:bool = ...) -> Self:
        """
        __new__(cls: type, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode)
        __new__(cls: type, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: bool)
        """
        ...


class CryptoStreamMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CryptoStreamMode, values: Read (0), Write (1) """
    Read: CryptoStreamMode = ...
    value__ = ...
    Write: CryptoStreamMode = ...


class CspKeyContainerInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ CspKeyContainerInfo(parameters: CspParameters) """
    @property
    def Accessible(self) -> bool:
        """ Get: Accessible(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """ Get: CryptoKeySecurity(self: CspKeyContainerInfo) -> CryptoKeySecurity """
        ...

    @property
    def Exportable(self) -> bool:
        """ Get: Exportable(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def HardwareDevice(self) -> bool:
        """ Get: HardwareDevice(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def KeyContainerName(self) -> str:
        """ Get: KeyContainerName(self: CspKeyContainerInfo) -> str """
        ...

    @property
    def KeyNumber(self) -> KeyNumber:
        """ Get: KeyNumber(self: CspKeyContainerInfo) -> KeyNumber """
        ...

    @property
    def MachineKeyStore(self) -> bool:
        """ Get: MachineKeyStore(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def Protected(self) -> bool:
        """ Get: Protected(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: CspKeyContainerInfo) -> str """
        ...

    @property
    def ProviderType(self) -> int:
        """ Get: ProviderType(self: CspKeyContainerInfo) -> int """
        ...

    @property
    def RandomlyGenerated(self) -> bool:
        """ Get: RandomlyGenerated(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def Removable(self) -> bool:
        """ Get: Removable(self: CspKeyContainerInfo) -> bool """
        ...

    @property
    def UniqueKeyContainerName(self) -> str:
        """ Get: UniqueKeyContainerName(self: CspKeyContainerInfo) -> str """
        ...



class CspParameters: # skipped bases: <type 'object'>, <type 'object'>
    """
    CspParameters()
    CspParameters(dwTypeIn: int)
    CspParameters(dwTypeIn: int, strProviderNameIn: str)
    CspParameters(dwTypeIn: int, strProviderNameIn: str, strContainerNameIn: str)
    CspParameters(providerType: int, providerName: str, keyContainerName: str, cryptoKeySecurity: CryptoKeySecurity, keyPassword: SecureString)
    CspParameters(providerType: int, providerName: str, keyContainerName: str, cryptoKeySecurity: CryptoKeySecurity, parentWindowHandle: IntPtr)
    """
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """
        Get: CryptoKeySecurity(self: CspParameters) -> CryptoKeySecurity
        Set: CryptoKeySecurity(self: CspParameters) = value
        """
        ...

    @property
    def Flags(self) -> CspProviderFlags:
        """
        Get: Flags(self: CspParameters) -> CspProviderFlags
        Set: Flags(self: CspParameters) = value
        """
        ...

    @property
    def KeyPassword(self) -> SecureString:
        """
        Get: KeyPassword(self: CspParameters) -> SecureString
        Set: KeyPassword(self: CspParameters) = value
        """
        ...

    @property
    def ParentWindowHandle(self) -> IntPtr:
        """
        Get: ParentWindowHandle(self: CspParameters) -> IntPtr
        Set: ParentWindowHandle(self: CspParameters) = value
        """
        ...


    KeyContainerName = ...
    KeyNumber = ...
    ProviderName = ...
    ProviderType = ...


class CspProviderFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CspProviderFlags, values: CreateEphemeralKey (128), NoFlags (0), NoPrompt (64), UseArchivableKey (16), UseDefaultKeyContainer (2), UseExistingKey (8), UseMachineKeyStore (1), UseNonExportableKey (4), UseUserProtectedKey (32) """
    CreateEphemeralKey: CspProviderFlags = ...
    NoFlags: CspProviderFlags = ...
    NoPrompt: CspProviderFlags = ...
    UseArchivableKey: CspProviderFlags = ...
    UseDefaultKeyContainer: CspProviderFlags = ...
    UseExistingKey: CspProviderFlags = ...
    UseMachineKeyStore: CspProviderFlags = ...
    UseNonExportableKey: CspProviderFlags = ...
    UseUserProtectedKey: CspProviderFlags = ...
    value__ = ...


class DataProtectionScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataProtectionScope, values: CurrentUser (0), LocalMachine (1) """
    CurrentUser: DataProtectionScope = ...
    LocalMachine: DataProtectionScope = ...
    value__ = ...


class DataProtector: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self):
        ...

    @property
    def PrependHashedPurposeToPlaintext(self):
        ...

    @property
    def PrimaryPurpose(self):
        ...

    @property
    def SpecificPurposes(self):
        ...


    @staticmethod
    def Create(providerClass:str, applicationName:str, primaryPurpose:str, specificPurposes:Array) -> DataProtector:
        """ Create(providerClass: str, applicationName: str, primaryPurpose: str, *specificPurposes: Array[str]) -> DataProtector """
        ...

    def GetHashedPurpose(self, *args): #cannot find CLR method
        """ GetHashedPurpose(self: DataProtector) -> Array[Byte] """
        ...

    def IsReprotectRequired(self, encryptedData:Array) -> bool:
        """ IsReprotectRequired(self: DataProtector, encryptedData: Array[Byte]) -> bool """
        ...

    def Protect(self, userData:Array) -> Array:
        """ Protect(self: DataProtector, userData: Array[Byte]) -> Array[Byte] """
        ...

    def ProviderProtect(self, *args): #cannot find CLR method
        """ ProviderProtect(self: DataProtector, userData: Array[Byte]) -> Array[Byte] """
        ...

    def ProviderUnprotect(self, *args): #cannot find CLR method
        """ ProviderUnprotect(self: DataProtector, encryptedData: Array[Byte]) -> Array[Byte] """
        ...

    def Unprotect(self, encryptedData:Array) -> Array:
        """ Unprotect(self: DataProtector, encryptedData: Array[Byte]) -> Array[Byte] """
        ...


class DeriveBytes(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetBytes(self, cb:int) -> Array:
        """ GetBytes(self: DeriveBytes, cb: int) -> Array[Byte] """
        ...

    def Reset(self): # -> 
        """ Reset(self: DeriveBytes) """
        ...


class DES(SymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsSemiWeakKey(rgbKey:Array) -> bool:
        """ IsSemiWeakKey(rgbKey: Array[Byte]) -> bool """
        ...

    @staticmethod
    def IsWeakKey(rgbKey:Array) -> bool:
        """ IsWeakKey(rgbKey: Array[Byte]) -> bool """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class DESCryptoServiceProvider(DES): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ DESCryptoServiceProvider() """
    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateDecryptor(self: DESCryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateEncryptor(self: DESCryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: DESCryptoServiceProvider) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: DESCryptoServiceProvider) """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class DpapiDataProtector(DataProtector): # skipped bases: <type 'object'>
    """ DpapiDataProtector(appName: str, primaryPurpose: str, *specificPurpose: Array[str]) """
    @property
    def Scope(self) -> DataProtectionScope:
        """
        Get: Scope(self: DpapiDataProtector) -> DataProtectionScope
        Set: Scope(self: DpapiDataProtector) = value
        """
        ...



class DSA(AsymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def CreateSignature(self, rgbHash:Array) -> Array:
        """ CreateSignature(self: DSA, rgbHash: Array[Byte]) -> Array[Byte] """
        ...

    def ExportParameters(self, includePrivateParameters:bool) -> DSAParameters:
        """ ExportParameters(self: DSA, includePrivateParameters: bool) -> DSAParameters """
        ...

    def HashData(self, *args): #cannot find CLR method
        """
        HashData(self: DSA, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        HashData(self: DSA, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def ImportParameters(self, parameters:DSAParameters): # -> 
        """ ImportParameters(self: DSA, parameters: DSAParameters) """
        ...

    def SignData(self, data:Array, *__args:HashAlgorithmName) -> Array:
        """
        SignData(self: DSA, data: Array[Byte], hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        SignData(self: DSA, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        SignData(self: DSA, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def VerifyData(self, data, *__args) -> bool:
        """
        VerifyData(self: DSA, data: Array[Byte], signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        VerifyData(self: DSA, data: Array[Byte], offset: int, count: int, signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        VerifyData(self: DSA, data: Stream, signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        """
        ...

    def VerifySignature(self, rgbHash:Array, rgbSignature:Array) -> bool:
        """ VerifySignature(self: DSA, rgbHash: Array[Byte], rgbSignature: Array[Byte]) -> bool """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class DSACng(DSA): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    DSACng()
    DSACng(keySize: int)
    DSACng(key: CngKey)
    """
    @property
    def Key(self) -> CngKey:
        """ Get: Key(self: DSACng) -> CngKey """
        ...

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """ Get: KeyExchangeAlgorithm(self: DSACng) -> str """
        ...

    @property
    def LegalKeySizes(self) -> Array:
        """ Get: LegalKeySizes(self: DSACng) -> Array[KeySizes] """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """ Get: SignatureAlgorithm(self: DSACng) -> str """
        ...


    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keySize: int)
        __new__(cls: type, key: CngKey)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class DSACryptoServiceProvider(ICspAsymmetricAlgorithm, DSA): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    DSACryptoServiceProvider()
    DSACryptoServiceProvider(dwKeySize: int)
    DSACryptoServiceProvider(parameters: CspParameters)
    DSACryptoServiceProvider(dwKeySize: int, parameters: CspParameters)
    """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """ Get: KeyExchangeAlgorithm(self: DSACryptoServiceProvider) -> str """
        ...

    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: DSACryptoServiceProvider) -> int """
        ...

    @property
    def PersistKeyInCsp(self) -> bool:
        """
        Get: PersistKeyInCsp(self: DSACryptoServiceProvider) -> bool
        Set: PersistKeyInCsp(self: DSACryptoServiceProvider) = value
        """
        ...

    @property
    def PublicOnly(self) -> bool:
        """ Get: PublicOnly(self: DSACryptoServiceProvider) -> bool """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """ Get: SignatureAlgorithm(self: DSACryptoServiceProvider) -> str """
        ...

    @property
    def UseMachineKeyStore(self) -> bool:
        """
        Get: UseMachineKeyStore() -> bool
        Set: UseMachineKeyStore() = value
        """
        ...


    def SignHash(self, rgbHash:Array, str:str) -> Array:
        """ SignHash(self: DSACryptoServiceProvider, rgbHash: Array[Byte], str: str) -> Array[Byte] """
        ...

    def VerifyHash(self, rgbHash:Array, str:str, rgbSignature:Array) -> bool:
        """ VerifyHash(self: DSACryptoServiceProvider, rgbHash: Array[Byte], str: str, rgbSignature: Array[Byte]) -> bool """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dwKeySize: int)
        __new__(cls: type, parameters: CspParameters)
        __new__(cls: type, dwKeySize: int, parameters: CspParameters)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class DSAParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Counter = ...
    G = ...
    J = ...
    P = ...
    Q = ...
    Seed = ...
    X = ...
    Y = ...


class DSASignatureDeformatter(AsymmetricSignatureDeformatter): # skipped bases: <type 'object'>
    """
    DSASignatureDeformatter()
    DSASignatureDeformatter(key: AsymmetricAlgorithm)
    """
    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class DSASignatureFormatter(AsymmetricSignatureFormatter): # skipped bases: <type 'object'>
    """
    DSASignatureFormatter()
    DSASignatureFormatter(key: AsymmetricAlgorithm)
    """
    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class ECCurve: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsCharacteristic2(self) -> bool:
        """ Get: IsCharacteristic2(self: ECCurve) -> bool """
        ...

    @property
    def IsExplicit(self) -> bool:
        """ Get: IsExplicit(self: ECCurve) -> bool """
        ...

    @property
    def IsNamed(self) -> bool:
        """ Get: IsNamed(self: ECCurve) -> bool """
        ...

    @property
    def IsPrime(self) -> bool:
        """ Get: IsPrime(self: ECCurve) -> bool """
        ...

    @property
    def Oid(self) -> Oid:
        """ Get: Oid(self: ECCurve) -> Oid """
        ...


    @staticmethod
    def CreateFromFriendlyName(oidFriendlyName:str) -> ECCurve:
        """ CreateFromFriendlyName(oidFriendlyName: str) -> ECCurve """
        ...

    @staticmethod
    def CreateFromOid(curveOid:Oid) -> ECCurve:
        """ CreateFromOid(curveOid: Oid) -> ECCurve """
        ...

    @staticmethod
    def CreateFromValue(oidValue:str) -> ECCurve:
        """ CreateFromValue(oidValue: str) -> ECCurve """
        ...

    def ECCurveType(self, *args): #cannot find CLR method
        """ enum ECCurveType, values: Characteristic2 (4), Implicit (0), Named (5), PrimeMontgomery (3), PrimeShortWeierstrass (1), PrimeTwistedEdwards (2) """
        ...

    def NamedCurves(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Validate(self): # -> 
        """ Validate(self: ECCurve) """
        ...

    A = ...
    B = ...
    Cofactor = ...
    CurveType = ...
    G = ...
    Hash = ...
    Order = ...
    Polynomial = ...
    Prime = ...
    Seed = ...


class ECDiffieHellman(AsymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def PublicKey(self): # -> ECDiffieHellmanPublicKey
        """ Get: PublicKey(self: ECDiffieHellman) -> ECDiffieHellmanPublicKey """
        ...


    def DeriveKeyFromHash(self, otherPartyPublicKey, hashAlgorithm:HashAlgorithmName, secretPrepend:Array = ..., secretAppend:Array = ...) -> Array: # Not found arg types: {'otherPartyPublicKey': 'ECDiffieHellmanPublicKey'}
        """
        DeriveKeyFromHash(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        DeriveKeyFromHash(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, secretPrepend: Array[Byte], secretAppend: Array[Byte]) -> Array[Byte]
        """
        ...

    def DeriveKeyFromHmac(self, otherPartyPublicKey, hashAlgorithm:HashAlgorithmName, hmacKey:Array, secretPrepend:Array = ..., secretAppend:Array = ...) -> Array: # Not found arg types: {'otherPartyPublicKey': 'ECDiffieHellmanPublicKey'}
        """
        DeriveKeyFromHmac(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: Array[Byte]) -> Array[Byte]
        DeriveKeyFromHmac(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: Array[Byte], secretPrepend: Array[Byte], secretAppend: Array[Byte]) -> Array[Byte]
        """
        ...

    def DeriveKeyMaterial(self, otherPartyPublicKey) -> Array: # Not found arg types: {'otherPartyPublicKey': 'ECDiffieHellmanPublicKey'}
        """ DeriveKeyMaterial(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> Array[Byte] """
        ...

    def DeriveKeyTls(self, otherPartyPublicKey, prfLabel:Array, prfSeed:Array) -> Array: # Not found arg types: {'otherPartyPublicKey': 'ECDiffieHellmanPublicKey'}
        """ DeriveKeyTls(self: ECDiffieHellman, otherPartyPublicKey: ECDiffieHellmanPublicKey, prfLabel: Array[Byte], prfSeed: Array[Byte]) -> Array[Byte] """
        ...

    def ExportExplicitParameters(self, includePrivateParameters:bool): # -> ECParameters
        """ ExportExplicitParameters(self: ECDiffieHellman, includePrivateParameters: bool) -> ECParameters """
        ...

    def ExportParameters(self, includePrivateParameters:bool): # -> ECParameters
        """ ExportParameters(self: ECDiffieHellman, includePrivateParameters: bool) -> ECParameters """
        ...

    def GenerateKey(self, curve:ECCurve): # -> 
        """ GenerateKey(self: ECDiffieHellman, curve: ECCurve) """
        ...

    def ImportParameters(self, parameters): # ->  # Not found arg types: {'parameters': 'ECParameters'}
        """ ImportParameters(self: ECDiffieHellman, parameters: ECParameters) """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class ECDiffieHellmanCng(ECDiffieHellman): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ECDiffieHellmanCng()
    ECDiffieHellmanCng(keySize: int)
    ECDiffieHellmanCng(curve: ECCurve)
    ECDiffieHellmanCng(key: CngKey)
    """
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """
        Get: HashAlgorithm(self: ECDiffieHellmanCng) -> CngAlgorithm
        Set: HashAlgorithm(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def HmacKey(self) -> Array:
        """
        Get: HmacKey(self: ECDiffieHellmanCng) -> Array[Byte]
        Set: HmacKey(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def Key(self) -> CngKey:
        """ Get: Key(self: ECDiffieHellmanCng) -> CngKey """
        ...

    @property
    def KeyDerivationFunction(self): # -> ECDiffieHellmanKeyDerivationFunction
        """
        Get: KeyDerivationFunction(self: ECDiffieHellmanCng) -> ECDiffieHellmanKeyDerivationFunction
        Set: KeyDerivationFunction(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def Label(self) -> Array:
        """
        Get: Label(self: ECDiffieHellmanCng) -> Array[Byte]
        Set: Label(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def SecretAppend(self) -> Array:
        """
        Get: SecretAppend(self: ECDiffieHellmanCng) -> Array[Byte]
        Set: SecretAppend(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def SecretPrepend(self) -> Array:
        """
        Get: SecretPrepend(self: ECDiffieHellmanCng) -> Array[Byte]
        Set: SecretPrepend(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def Seed(self) -> Array:
        """
        Get: Seed(self: ECDiffieHellmanCng) -> Array[Byte]
        Set: Seed(self: ECDiffieHellmanCng) = value
        """
        ...

    @property
    def UseSecretAgreementAsHmacKey(self) -> bool:
        """ Get: UseSecretAgreementAsHmacKey(self: ECDiffieHellmanCng) -> bool """
        ...


    def DeriveSecretAgreementHandle(self, otherPartyPublicKey) -> SafeNCryptSecretHandle: # Not found arg types: {'otherPartyPublicKey': 'ECDiffieHellmanPublicKey'}
        """
        DeriveSecretAgreementHandle(self: ECDiffieHellmanCng, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> SafeNCryptSecretHandle
        DeriveSecretAgreementHandle(self: ECDiffieHellmanCng, otherPartyPublicKey: CngKey) -> SafeNCryptSecretHandle
        """
        ...

    def FromXmlString(self, *__args:str): # -> 
        """ FromXmlString(self: ECDiffieHellmanCng, xmlString: str)FromXmlString(self: ECDiffieHellmanCng, xml: str, format: ECKeyXmlFormat) """
        ...

    def ToXmlString(self, *__args:bool) -> str:
        """
        ToXmlString(self: ECDiffieHellmanCng, includePrivateParameters: bool) -> str
        ToXmlString(self: ECDiffieHellmanCng, format: ECKeyXmlFormat) -> str
        """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keySize: int)
        __new__(cls: type, curve: ECCurve)
        __new__(cls: type, key: CngKey)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class ECDiffieHellmanPublicKey(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def ExportExplicitParameters(self): # -> ECParameters
        """ ExportExplicitParameters(self: ECDiffieHellmanPublicKey) -> ECParameters """
        ...

    def ExportParameters(self): # -> ECParameters
        """ ExportParameters(self: ECDiffieHellmanPublicKey) -> ECParameters """
        ...

    def ToByteArray(self) -> Array:
        """ ToByteArray(self: ECDiffieHellmanPublicKey) -> Array[Byte] """
        ...

    def ToXmlString(self) -> str:
        """ ToXmlString(self: ECDiffieHellmanPublicKey) -> str """
        ...


class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def BlobFormat(self) -> CngKeyBlobFormat:
        """ Get: BlobFormat(self: ECDiffieHellmanCngPublicKey) -> CngKeyBlobFormat """
        ...


    @staticmethod
    def FromByteArray(publicKeyBlob:Array, format:CngKeyBlobFormat) -> ECDiffieHellmanPublicKey:
        """ FromByteArray(publicKeyBlob: Array[Byte], format: CngKeyBlobFormat) -> ECDiffieHellmanPublicKey """
        ...

    @staticmethod
    def FromXmlString(xml:str) -> ECDiffieHellmanCngPublicKey:
        """ FromXmlString(xml: str) -> ECDiffieHellmanCngPublicKey """
        ...

    def Import(self) -> CngKey:
        """ Import(self: ECDiffieHellmanCngPublicKey) -> CngKey """
        ...


class ECDiffieHellmanKeyDerivationFunction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ECDiffieHellmanKeyDerivationFunction, values: Hash (0), Hmac (1), Tls (2) """
    Hash: ECDiffieHellmanKeyDerivationFunction = ...
    Hmac: ECDiffieHellmanKeyDerivationFunction = ...
    Tls: ECDiffieHellmanKeyDerivationFunction = ...
    value__ = ...


class ECDsa(AsymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def ExportExplicitParameters(self, includePrivateParameters:bool): # -> ECParameters
        """ ExportExplicitParameters(self: ECDsa, includePrivateParameters: bool) -> ECParameters """
        ...

    def ExportParameters(self, includePrivateParameters:bool): # -> ECParameters
        """ ExportParameters(self: ECDsa, includePrivateParameters: bool) -> ECParameters """
        ...

    def GenerateKey(self, curve:ECCurve): # -> 
        """ GenerateKey(self: ECDsa, curve: ECCurve) """
        ...

    def HashData(self, *args): #cannot find CLR method
        """
        HashData(self: ECDsa, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        HashData(self: ECDsa, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def ImportParameters(self, parameters): # ->  # Not found arg types: {'parameters': 'ECParameters'}
        """ ImportParameters(self: ECDsa, parameters: ECParameters) """
        ...

    def SignData(self, data:Array, *__args:HashAlgorithmName) -> Array:
        """
        SignData(self: ECDsa, data: Array[Byte], hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        SignData(self: ECDsa, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        SignData(self: ECDsa, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def SignHash(self, hash:Array) -> Array:
        """ SignHash(self: ECDsa, hash: Array[Byte]) -> Array[Byte] """
        ...

    def VerifyData(self, data, *__args) -> bool:
        """
        VerifyData(self: ECDsa, data: Array[Byte], signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        VerifyData(self: ECDsa, data: Array[Byte], offset: int, count: int, signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        VerifyData(self: ECDsa, data: Stream, signature: Array[Byte], hashAlgorithm: HashAlgorithmName) -> bool
        """
        ...

    def VerifyHash(self, hash:Array, signature:Array) -> bool:
        """ VerifyHash(self: ECDsa, hash: Array[Byte], signature: Array[Byte]) -> bool """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class ECDsaCng(ECDsa): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ECDsaCng()
    ECDsaCng(keySize: int)
    ECDsaCng(curve: ECCurve)
    ECDsaCng(key: CngKey)
    """
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """
        Get: HashAlgorithm(self: ECDsaCng) -> CngAlgorithm
        Set: HashAlgorithm(self: ECDsaCng) = value
        """
        ...

    @property
    def Key(self) -> CngKey:
        """ Get: Key(self: ECDsaCng) -> CngKey """
        ...


    def FromXmlString(self, *__args:str): # -> 
        """ FromXmlString(self: ECDsaCng, xmlString: str)FromXmlString(self: ECDsaCng, xml: str, format: ECKeyXmlFormat) """
        ...

    def ToXmlString(self, *__args:bool) -> str:
        """
        ToXmlString(self: ECDsaCng, includePrivateParameters: bool) -> str
        ToXmlString(self: ECDsaCng, format: ECKeyXmlFormat) -> str
        """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keySize: int)
        __new__(cls: type, curve: ECCurve)
        __new__(cls: type, key: CngKey)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class ECKeyXmlFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ECKeyXmlFormat, values: Rfc4050 (0) """
    Rfc4050: ECKeyXmlFormat = ...
    value__ = ...


class ECParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Validate(self): # -> 
        """ Validate(self: ECParameters) """
        ...

    Curve = ...
    D = ...
    Q = ...


class ECPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    X = ...
    Y = ...


class FromBase64Transform(ICryptoTransform): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FromBase64Transform()
    FromBase64Transform(whitespaces: FromBase64TransformMode)
    """
    def Clear(self): # -> 
        """ Clear(self: FromBase64Transform) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: FromBase64Transform) """
        ...


class FromBase64TransformMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FromBase64TransformMode, values: DoNotIgnoreWhiteSpaces (1), IgnoreWhiteSpaces (0) """
    DoNotIgnoreWhiteSpaces: FromBase64TransformMode = ...
    IgnoreWhiteSpaces: FromBase64TransformMode = ...
    value__ = ...


class HashAlgorithm(ICryptoTransform): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Hash(self) -> Array:
        """ Get: Hash(self: HashAlgorithm) -> Array[Byte] """
        ...

    @property
    def HashSize(self) -> int:
        """ Get: HashSize(self: HashAlgorithm) -> int """
        ...


    def Clear(self): # -> 
        """ Clear(self: HashAlgorithm) """
        ...

    def ComputeHash(self, *__args:Stream) -> Array:
        """
        ComputeHash(self: HashAlgorithm, inputStream: Stream) -> Array[Byte]
        ComputeHash(self: HashAlgorithm, buffer: Array[Byte]) -> Array[Byte]
        ComputeHash(self: HashAlgorithm, buffer: Array[Byte], offset: int, count: int) -> Array[Byte]
        """
        ...

    @staticmethod
    def Create(hashName:str = ...) -> HashAlgorithm:
        """
        Create(hashName: str) -> HashAlgorithm
        Create() -> HashAlgorithm
        """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: HashAlgorithm) """
        ...

    def HashCore(self, *args): #cannot find CLR method
        """ HashCore(self: HashAlgorithm, array: Array[Byte], ibStart: int, cbSize: int) """
        ...

    def HashFinal(self, *args): #cannot find CLR method
        """ HashFinal(self: HashAlgorithm) -> Array[Byte] """
        ...

    def Initialize(self): # -> 
        """ Initialize(self: HashAlgorithm) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class HashAlgorithmName(IEquatable): # skipped bases: <type 'object'>
    """ HashAlgorithmName(name: str) """
    @property
    def MD5(self) -> HashAlgorithmName:
        """ Get: MD5() -> HashAlgorithmName """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: HashAlgorithmName) -> str """
        ...

    @property
    def SHA1(self) -> HashAlgorithmName:
        """ Get: SHA1() -> HashAlgorithmName """
        ...

    @property
    def SHA256(self) -> HashAlgorithmName:
        """ Get: SHA256() -> HashAlgorithmName """
        ...

    @property
    def SHA384(self) -> HashAlgorithmName:
        """ Get: SHA384() -> HashAlgorithmName """
        ...

    @property
    def SHA512(self) -> HashAlgorithmName:
        """ Get: SHA512() -> HashAlgorithmName """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: HashAlgorithmName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: HashAlgorithmName) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class KeyedHashAlgorithm(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    @property
    def Key(self) -> Array:
        """
        Get: Key(self: KeyedHashAlgorithm) -> Array[Byte]
        Set: Key(self: KeyedHashAlgorithm) = value
        """
        ...


    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMAC(KeyedHashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    @property
    def BlockSizeValue(self):
        ...

    @property
    def HashName(self) -> str:
        """
        Get: HashName(self: HMAC) -> str
        Set: HashName(self: HMAC) = value
        """
        ...


    def Initialize(self): # -> 
        """ Initialize(self: HMAC) """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACMD5(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACMD5()
    HMACMD5(key: Array[Byte])
    """
    def __new__(cls, key:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACRIPEMD160(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACRIPEMD160()
    HMACRIPEMD160(key: Array[Byte])
    """
    def __new__(cls, key:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACSHA1(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACSHA1()
    HMACSHA1(key: Array[Byte])
    HMACSHA1(key: Array[Byte], useManagedSha1: bool)
    """
    def __new__(cls, key:Array = ..., useManagedSha1:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        __new__(cls: type, key: Array[Byte], useManagedSha1: bool)
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACSHA256(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACSHA256()
    HMACSHA256(key: Array[Byte])
    """
    def __new__(cls, key:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACSHA384(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACSHA384()
    HMACSHA384(key: Array[Byte])
    """
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """
        Get: ProduceLegacyHmacValues(self: HMACSHA384) -> bool
        Set: ProduceLegacyHmacValues(self: HMACSHA384) = value
        """
        ...


    def __new__(cls, key:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class HMACSHA512(HMAC): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    HMACSHA512()
    HMACSHA512(key: Array[Byte])
    """
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """
        Get: ProduceLegacyHmacValues(self: HMACSHA512) -> bool
        Set: ProduceLegacyHmacValues(self: HMACSHA512) = value
        """
        ...


    def __new__(cls, key:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class ICryptoTransform(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanReuseTransform(self) -> bool:
        """ Get: CanReuseTransform(self: ICryptoTransform) -> bool """
        ...

    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """ Get: CanTransformMultipleBlocks(self: ICryptoTransform) -> bool """
        ...

    @property
    def InputBlockSize(self) -> int:
        """ Get: InputBlockSize(self: ICryptoTransform) -> int """
        ...

    @property
    def OutputBlockSize(self) -> int:
        """ Get: OutputBlockSize(self: ICryptoTransform) -> int """
        ...


    def TransformBlock(self, inputBuffer:Array, inputOffset:int, inputCount:int, outputBuffer:Array, outputOffset:int) -> int:
        """ TransformBlock(self: ICryptoTransform, inputBuffer: Array[Byte], inputOffset: int, inputCount: int, outputBuffer: Array[Byte], outputOffset: int) -> int """
        ...

    def TransformFinalBlock(self, inputBuffer:Array, inputOffset:int, inputCount:int) -> Array:
        """ TransformFinalBlock(self: ICryptoTransform, inputBuffer: Array[Byte], inputOffset: int, inputCount: int) -> Array[Byte] """
        ...


class ICspAsymmetricAlgorithm: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """ Get: CspKeyContainerInfo(self: ICspAsymmetricAlgorithm) -> CspKeyContainerInfo """
        ...


    def ExportCspBlob(self, includePrivateParameters:bool) -> Array:
        """ ExportCspBlob(self: ICspAsymmetricAlgorithm, includePrivateParameters: bool) -> Array[Byte] """
        ...

    def ImportCspBlob(self, rawData:Array): # -> 
        """ ImportCspBlob(self: ICspAsymmetricAlgorithm, rawData: Array[Byte]) """
        ...


class IncrementalHash(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlgorithmName(self) -> HashAlgorithmName:
        """ Get: AlgorithmName(self: IncrementalHash) -> HashAlgorithmName """
        ...


    def AppendData(self, data:Array, offset:int = ..., count:int = ...): # -> 
        """ AppendData(self: IncrementalHash, data: Array[Byte])AppendData(self: IncrementalHash, data: Array[Byte], offset: int, count: int) """
        ...

    @staticmethod
    def CreateHash(hashAlgorithm:HashAlgorithmName) -> IncrementalHash:
        """ CreateHash(hashAlgorithm: HashAlgorithmName) -> IncrementalHash """
        ...

    @staticmethod
    def CreateHMAC(hashAlgorithm:HashAlgorithmName, key:Array) -> IncrementalHash:
        """ CreateHMAC(hashAlgorithm: HashAlgorithmName, key: Array[Byte]) -> IncrementalHash """
        ...

    def GetHashAndReset(self) -> Array:
        """ GetHashAndReset(self: IncrementalHash) -> Array[Byte] """
        ...


class KeyNumber(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyNumber, values: Exchange (1), Signature (2) """
    Exchange: KeyNumber = ...
    Signature: KeyNumber = ...
    value__ = ...


class KeySizes: # skipped bases: <type 'object'>, <type 'object'>
    """ KeySizes(minSize: int, maxSize: int, skipSize: int) """
    @property
    def MaxSize(self) -> int:
        """ Get: MaxSize(self: KeySizes) -> int """
        ...

    @property
    def MinSize(self) -> int:
        """ Get: MinSize(self: KeySizes) -> int """
        ...

    @property
    def SkipSize(self) -> int:
        """ Get: SkipSize(self: KeySizes) -> int """
        ...



class MACTripleDES(KeyedHashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """
    MACTripleDES()
    MACTripleDES(rgbKey: Array[Byte])
    MACTripleDES(strTripleDES: str, rgbKey: Array[Byte])
    """
    @property
    def Padding(self) -> PaddingMode:
        """
        Get: Padding(self: MACTripleDES) -> PaddingMode
        Set: Padding(self: MACTripleDES) = value
        """
        ...


    def Initialize(self): # -> 
        """ Initialize(self: MACTripleDES) """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, rgbKey: Array[Byte])
        __new__(cls: type, strTripleDES: str, rgbKey: Array[Byte])
        """
        ...

    HashSizeValue = ...
    HashValue = ...
    KeyValue = ...
    State = ...


class ManifestSignatureInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AuthenticodeSignature(self): # -> AuthenticodeSignatureInformation
        """ Get: AuthenticodeSignature(self: ManifestSignatureInformation) -> AuthenticodeSignatureInformation """
        ...

    @property
    def Manifest(self) -> ManifestKinds:
        """ Get: Manifest(self: ManifestSignatureInformation) -> ManifestKinds """
        ...

    @property
    def StrongNameSignature(self): # -> StrongNameSignatureInformation
        """ Get: StrongNameSignature(self: ManifestSignatureInformation) -> StrongNameSignatureInformation """
        ...


    @staticmethod
    def VerifySignature(application:ActivationContext, manifests:ManifestKinds = ..., revocationFlag:X509RevocationFlag = ..., revocationMode:X509RevocationMode = ...): # -> ManifestSignatureInformationCollection
        """
        VerifySignature(application: ActivationContext) -> ManifestSignatureInformationCollection
        VerifySignature(application: ActivationContext, manifests: ManifestKinds) -> ManifestSignatureInformationCollection
        VerifySignature(application: ActivationContext, manifests: ManifestKinds, revocationFlag: X509RevocationFlag, revocationMode: X509RevocationMode) -> ManifestSignatureInformationCollection
        """
        ...


class ManifestSignatureInformationCollection(ReadOnlyCollection): # skipped bases: <type 'IReadOnlyCollection[ManifestSignatureInformation]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[ManifestSignatureInformation]'>, <type 'IList[ManifestSignatureInformation]'>, <type 'ICollection[ManifestSignatureInformation]'>, <type 'ICollection'>, <type 'IReadOnlyList[ManifestSignatureInformation]'>, <type 'object'>
    """ no doc """
    pass

class MaskGenerationMethod: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GenerateMask(self, rgbSeed:Array, cbReturn:int) -> Array:
        """ GenerateMask(self: MaskGenerationMethod, rgbSeed: Array[Byte], cbReturn: int) -> Array[Byte] """
        ...


class MD5(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class MD5Cng(MD5): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ MD5Cng() """
    def Initialize(self): # -> 
        """ Initialize(self: MD5Cng) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class MD5CryptoServiceProvider(MD5): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ MD5CryptoServiceProvider() """
    def Initialize(self): # -> 
        """ Initialize(self: MD5CryptoServiceProvider) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class MemoryProtectionScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemoryProtectionScope, values: CrossProcess (1), SameLogon (2), SameProcess (0) """
    CrossProcess: MemoryProtectionScope = ...
    SameLogon: MemoryProtectionScope = ...
    SameProcess: MemoryProtectionScope = ...
    value__ = ...


class Oid: # skipped bases: <type 'object'>, <type 'object'>
    """
    Oid()
    Oid(oid: str)
    Oid(value: str, friendlyName: str)
    Oid(oid: Oid)
    """
    @property
    def FriendlyName(self) -> str:
        """
        Get: FriendlyName(self: Oid) -> str
        Set: FriendlyName(self: Oid) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: Oid) -> str
        Set: Value(self: Oid) = value
        """
        ...


    @staticmethod
    def FromFriendlyName(friendlyName:str, group:OidGroup) -> Oid:
        """ FromFriendlyName(friendlyName: str, group: OidGroup) -> Oid """
        ...

    @staticmethod
    def FromOidValue(oidValue:str, group:OidGroup) -> Oid:
        """ FromOidValue(oidValue: str, group: OidGroup) -> Oid """
        ...


class OidCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ OidCollection() """
    def Add(self, oid:Oid) -> int:
        """ Add(self: OidCollection, oid: Oid) -> int """
        ...

    def GetEnumerator(self) -> OidEnumerator:
        """ GetEnumerator(self: OidCollection) -> OidEnumerator """
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


class OidEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class OidGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OidGroup, values: All (0), Attribute (5), EncryptionAlgorithm (2), EnhancedKeyUsage (7), ExtensionOrAttribute (6), HashAlgorithm (1), KeyDerivationFunction (10), Policy (8), PublicKeyAlgorithm (3), SignatureAlgorithm (4), Template (9) """
    All: OidGroup = ...
    Attribute: OidGroup = ...
    EncryptionAlgorithm: OidGroup = ...
    EnhancedKeyUsage: OidGroup = ...
    ExtensionOrAttribute: OidGroup = ...
    HashAlgorithm: OidGroup = ...
    KeyDerivationFunction: OidGroup = ...
    Policy: OidGroup = ...
    PublicKeyAlgorithm: OidGroup = ...
    SignatureAlgorithm: OidGroup = ...
    Template: OidGroup = ...
    value__ = ...


class PaddingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PaddingMode, values: ANSIX923 (4), ISO10126 (5), None (1), PKCS7 (2), Zeros (3) """
    ANSIX923: PaddingMode = ...
    ISO10126: PaddingMode = ...
    PKCS7: PaddingMode = ...
    value__ = ...
    Zeros: PaddingMode = ...


class PasswordDeriveBytes(DeriveBytes): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    PasswordDeriveBytes(strPassword: str, rgbSalt: Array[Byte])
    PasswordDeriveBytes(password: Array[Byte], salt: Array[Byte])
    PasswordDeriveBytes(strPassword: str, rgbSalt: Array[Byte], strHashName: str, iterations: int)
    PasswordDeriveBytes(password: Array[Byte], salt: Array[Byte], hashName: str, iterations: int)
    PasswordDeriveBytes(strPassword: str, rgbSalt: Array[Byte], cspParams: CspParameters)
    PasswordDeriveBytes(password: Array[Byte], salt: Array[Byte], cspParams: CspParameters)
    PasswordDeriveBytes(strPassword: str, rgbSalt: Array[Byte], strHashName: str, iterations: int, cspParams: CspParameters)
    PasswordDeriveBytes(password: Array[Byte], salt: Array[Byte], hashName: str, iterations: int, cspParams: CspParameters)
    """
    @property
    def HashName(self) -> str:
        """
        Get: HashName(self: PasswordDeriveBytes) -> str
        Set: HashName(self: PasswordDeriveBytes) = value
        """
        ...

    @property
    def IterationCount(self) -> int:
        """
        Get: IterationCount(self: PasswordDeriveBytes) -> int
        Set: IterationCount(self: PasswordDeriveBytes) = value
        """
        ...

    @property
    def Salt(self) -> Array:
        """
        Get: Salt(self: PasswordDeriveBytes) -> Array[Byte]
        Set: Salt(self: PasswordDeriveBytes) = value
        """
        ...


    def CryptDeriveKey(self, algname:str, alghashname:str, keySize:int, rgbIV:Array) -> Array:
        """ CryptDeriveKey(self: PasswordDeriveBytes, algname: str, alghashname: str, keySize: int, rgbIV: Array[Byte]) -> Array[Byte] """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, strPassword: str, rgbSalt: Array[Byte])
        __new__(cls: type, password: Array[Byte], salt: Array[Byte])
        __new__(cls: type, strPassword: str, rgbSalt: Array[Byte], strHashName: str, iterations: int)
        __new__(cls: type, password: Array[Byte], salt: Array[Byte], hashName: str, iterations: int)
        __new__(cls: type, strPassword: str, rgbSalt: Array[Byte], cspParams: CspParameters)
        __new__(cls: type, password: Array[Byte], salt: Array[Byte], cspParams: CspParameters)
        __new__(cls: type, strPassword: str, rgbSalt: Array[Byte], strHashName: str, iterations: int, cspParams: CspParameters)
        __new__(cls: type, password: Array[Byte], salt: Array[Byte], hashName: str, iterations: int, cspParams: CspParameters)
        """
        ...


class PKCS1MaskGenerationMethod(MaskGenerationMethod): # skipped bases: <type 'object'>
    """ PKCS1MaskGenerationMethod() """
    @property
    def HashName(self) -> str:
        """
        Get: HashName(self: PKCS1MaskGenerationMethod) -> str
        Set: HashName(self: PKCS1MaskGenerationMethod) = value
        """
        ...



class ProtectedData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Protect(userData:Array, optionalEntropy:Array, scope:DataProtectionScope) -> Array:
        """ Protect(userData: Array[Byte], optionalEntropy: Array[Byte], scope: DataProtectionScope) -> Array[Byte] """
        ...

    @staticmethod
    def Unprotect(encryptedData:Array, optionalEntropy:Array, scope:DataProtectionScope) -> Array:
        """ Unprotect(encryptedData: Array[Byte], optionalEntropy: Array[Byte], scope: DataProtectionScope) -> Array[Byte] """
        ...

    __all__: list = ...


class ProtectedMemory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Protect(userData:Array, scope:MemoryProtectionScope): # -> 
        """ Protect(userData: Array[Byte], scope: MemoryProtectionScope) """
        ...

    @staticmethod
    def Unprotect(encryptedData:Array, scope:MemoryProtectionScope): # -> 
        """ Unprotect(encryptedData: Array[Byte], scope: MemoryProtectionScope) """
        ...

    __all__: list = ...


class RandomNumberGenerator(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Create(rngName=None) -> RandomNumberGenerator:
        """
        Create() -> RandomNumberGenerator
        Create(rngName: str) -> RandomNumberGenerator
        """
        ...

    def GetBytes(self, data:Array, offset:int = ..., count:int = ...): # -> 
        """ GetBytes(self: RandomNumberGenerator, data: Array[Byte], offset: int, count: int)GetBytes(self: RandomNumberGenerator, data: Array[Byte]) """
        ...

    def GetNonZeroBytes(self, data:Array): # -> 
        """ GetNonZeroBytes(self: RandomNumberGenerator, data: Array[Byte]) """
        ...


class RC2(SymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def EffectiveKeySize(self) -> int:
        """
        Get: EffectiveKeySize(self: RC2) -> int
        Set: EffectiveKeySize(self: RC2) = value
        """
        ...


    BlockSizeValue = ...
    EffectiveKeySizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class RC2CryptoServiceProvider(RC2): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ RC2CryptoServiceProvider() """
    @property
    def UseSalt(self) -> bool:
        """
        Get: UseSalt(self: RC2CryptoServiceProvider) -> bool
        Set: UseSalt(self: RC2CryptoServiceProvider) = value
        """
        ...


    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateDecryptor(self: RC2CryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateEncryptor(self: RC2CryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: RC2CryptoServiceProvider) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: RC2CryptoServiceProvider) """
        ...

    BlockSizeValue = ...
    EffectiveKeySizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class Rfc2898DeriveBytes(DeriveBytes): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    Rfc2898DeriveBytes(password: str, saltSize: int)
    Rfc2898DeriveBytes(password: str, saltSize: int, iterations: int)
    Rfc2898DeriveBytes(password: str, saltSize: int, iterations: int, hashAlgorithm: HashAlgorithmName)
    Rfc2898DeriveBytes(password: str, salt: Array[Byte])
    Rfc2898DeriveBytes(password: str, salt: Array[Byte], iterations: int)
    Rfc2898DeriveBytes(password: str, salt: Array[Byte], iterations: int, hashAlgorithm: HashAlgorithmName)
    Rfc2898DeriveBytes(password: Array[Byte], salt: Array[Byte], iterations: int)
    Rfc2898DeriveBytes(password: Array[Byte], salt: Array[Byte], iterations: int, hashAlgorithm: HashAlgorithmName)
    """
    @property
    def IterationCount(self) -> int:
        """
        Get: IterationCount(self: Rfc2898DeriveBytes) -> int
        Set: IterationCount(self: Rfc2898DeriveBytes) = value
        """
        ...

    @property
    def Salt(self) -> Array:
        """
        Get: Salt(self: Rfc2898DeriveBytes) -> Array[Byte]
        Set: Salt(self: Rfc2898DeriveBytes) = value
        """
        ...


    def CryptDeriveKey(self, algname:str, alghashname:str, keySize:int, rgbIV:Array) -> Array:
        """ CryptDeriveKey(self: Rfc2898DeriveBytes, algname: str, alghashname: str, keySize: int, rgbIV: Array[Byte]) -> Array[Byte] """
        ...

    def __new__(cls, password:str, *__args:int) -> Self:
        """
        __new__(cls: type, password: str, saltSize: int)
        __new__(cls: type, password: str, saltSize: int, iterations: int)
        __new__(cls: type, password: str, saltSize: int, iterations: int, hashAlgorithm: HashAlgorithmName)
        __new__(cls: type, password: str, salt: Array[Byte])
        __new__(cls: type, password: str, salt: Array[Byte], iterations: int)
        __new__(cls: type, password: str, salt: Array[Byte], iterations: int, hashAlgorithm: HashAlgorithmName)
        __new__(cls: type, password: Array[Byte], salt: Array[Byte], iterations: int)
        __new__(cls: type, password: Array[Byte], salt: Array[Byte], iterations: int, hashAlgorithm: HashAlgorithmName)
        """
        ...


class Rijndael(SymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class RijndaelManaged(Rijndael): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ RijndaelManaged() """
    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateDecryptor(self: RijndaelManaged, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateEncryptor(self: RijndaelManaged, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: RijndaelManaged) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: RijndaelManaged) """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class RijndaelManagedTransform(ICryptoTransform): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def BlockSizeValue(self) -> int:
        """ Get: BlockSizeValue(self: RijndaelManagedTransform) -> int """
        ...


    def Clear(self): # -> 
        """ Clear(self: RijndaelManagedTransform) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: RijndaelManagedTransform) """
        ...

    def Reset(self): # -> 
        """ Reset(self: RijndaelManagedTransform) """
        ...


class RIPEMD160(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class RIPEMD160Managed(RIPEMD160): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ RIPEMD160Managed() """
    def Initialize(self): # -> 
        """ Initialize(self: RIPEMD160Managed) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class RNGCryptoServiceProvider(RandomNumberGenerator): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    RNGCryptoServiceProvider()
    RNGCryptoServiceProvider(str: str)
    RNGCryptoServiceProvider(rgb: Array[Byte])
    RNGCryptoServiceProvider(cspParams: CspParameters)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, str: str)
        __new__(cls: type, rgb: Array[Byte])
        __new__(cls: type, cspParams: CspParameters)
        """
        ...


class RSA(AsymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def Decrypt(self, data:Array, padding:RSAEncryptionPadding) -> Array:
        """ Decrypt(self: RSA, data: Array[Byte], padding: RSAEncryptionPadding) -> Array[Byte] """
        ...

    def DecryptValue(self, rgb:Array) -> Array:
        """ DecryptValue(self: RSA, rgb: Array[Byte]) -> Array[Byte] """
        ...

    def Encrypt(self, data:Array, padding:RSAEncryptionPadding) -> Array:
        """ Encrypt(self: RSA, data: Array[Byte], padding: RSAEncryptionPadding) -> Array[Byte] """
        ...

    def EncryptValue(self, rgb:Array) -> Array:
        """ EncryptValue(self: RSA, rgb: Array[Byte]) -> Array[Byte] """
        ...

    def ExportParameters(self, includePrivateParameters:bool) -> RSAParameters:
        """ ExportParameters(self: RSA, includePrivateParameters: bool) -> RSAParameters """
        ...

    def HashData(self, *args): #cannot find CLR method
        """
        HashData(self: RSA, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        HashData(self: RSA, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[Byte]
        """
        ...

    def ImportParameters(self, parameters:RSAParameters): # -> 
        """ ImportParameters(self: RSA, parameters: RSAParameters) """
        ...

    def SignData(self, data, *__args) -> Array:
        """
        SignData(self: RSA, data: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> Array[Byte]
        SignData(self: RSA, data: Array[Byte], offset: int, count: int, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> Array[Byte]
        SignData(self: RSA, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> Array[Byte]
        """
        ...

    def SignHash(self, hash:Array, hashAlgorithm:HashAlgorithmName, padding:RSASignaturePadding) -> Array:
        """ SignHash(self: RSA, hash: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> Array[Byte] """
        ...

    def VerifyData(self, data, *__args) -> bool:
        """
        VerifyData(self: RSA, data: Array[Byte], signature: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool
        VerifyData(self: RSA, data: Array[Byte], offset: int, count: int, signature: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool
        VerifyData(self: RSA, data: Stream, signature: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool
        """
        ...

    def VerifyHash(self, hash:Array, signature:Array, hashAlgorithm:HashAlgorithmName, padding:RSASignaturePadding) -> bool:
        """ VerifyHash(self: RSA, hash: Array[Byte], signature: Array[Byte], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class RSACng(RSA): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    RSACng()
    RSACng(keySize: int)
    RSACng(key: CngKey)
    """
    @property
    def Key(self) -> CngKey:
        """ Get: Key(self: RSACng) -> CngKey """
        ...


    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keySize: int)
        __new__(cls: type, key: CngKey)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class RSACryptoServiceProvider(ICspAsymmetricAlgorithm, RSA): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    RSACryptoServiceProvider()
    RSACryptoServiceProvider(dwKeySize: int)
    RSACryptoServiceProvider(parameters: CspParameters)
    RSACryptoServiceProvider(dwKeySize: int, parameters: CspParameters)
    """
    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: RSACryptoServiceProvider) -> int """
        ...

    @property
    def PersistKeyInCsp(self) -> bool:
        """
        Get: PersistKeyInCsp(self: RSACryptoServiceProvider) -> bool
        Set: PersistKeyInCsp(self: RSACryptoServiceProvider) = value
        """
        ...

    @property
    def PublicOnly(self) -> bool:
        """ Get: PublicOnly(self: RSACryptoServiceProvider) -> bool """
        ...

    @property
    def UseMachineKeyStore(self) -> bool:
        """
        Get: UseMachineKeyStore() -> bool
        Set: UseMachineKeyStore() = value
        """
        ...


    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dwKeySize: int)
        __new__(cls: type, parameters: CspParameters)
        __new__(cls: type, dwKeySize: int, parameters: CspParameters)
        """
        ...

    KeySizeValue = ...
    LegalKeySizesValue = ...


class RSAEncryptionPadding(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Mode(self) -> RSAEncryptionPaddingMode:
        """ Get: Mode(self: RSAEncryptionPadding) -> RSAEncryptionPaddingMode """
        ...

    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName:
        """ Get: OaepHashAlgorithm(self: RSAEncryptionPadding) -> HashAlgorithmName """
        ...

    @property
    def OaepSHA1(self) -> RSAEncryptionPadding:
        """ Get: OaepSHA1() -> RSAEncryptionPadding """
        ...

    @property
    def OaepSHA256(self) -> RSAEncryptionPadding:
        """ Get: OaepSHA256() -> RSAEncryptionPadding """
        ...

    @property
    def OaepSHA384(self) -> RSAEncryptionPadding:
        """ Get: OaepSHA384() -> RSAEncryptionPadding """
        ...

    @property
    def OaepSHA512(self) -> RSAEncryptionPadding:
        """ Get: OaepSHA512() -> RSAEncryptionPadding """
        ...

    @property
    def Pkcs1(self) -> RSAEncryptionPadding:
        """ Get: Pkcs1() -> RSAEncryptionPadding """
        ...


    @staticmethod
    def CreateOaep(hashAlgorithm:HashAlgorithmName) -> RSAEncryptionPadding:
        """ CreateOaep(hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RSAEncryptionPadding) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RSAEncryptionPadding) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RSAEncryptionPaddingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RSAEncryptionPaddingMode, values: Oaep (1), Pkcs1 (0) """
    Oaep: RSAEncryptionPaddingMode = ...
    Pkcs1: RSAEncryptionPaddingMode = ...
    value__ = ...


class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter): # skipped bases: <type 'object'>
    """
    RSAOAEPKeyExchangeDeformatter()
    RSAOAEPKeyExchangeDeformatter(key: AsymmetricAlgorithm)
    """
    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter): # skipped bases: <type 'object'>
    """
    RSAOAEPKeyExchangeFormatter()
    RSAOAEPKeyExchangeFormatter(key: AsymmetricAlgorithm)
    """
    @property
    def Parameter(self) -> Array:
        """
        Get: Parameter(self: RSAOAEPKeyExchangeFormatter) -> Array[Byte]
        Set: Parameter(self: RSAOAEPKeyExchangeFormatter) = value
        """
        ...

    @property
    def Rng(self) -> RandomNumberGenerator:
        """
        Get: Rng(self: RSAOAEPKeyExchangeFormatter) -> RandomNumberGenerator
        Set: Rng(self: RSAOAEPKeyExchangeFormatter) = value
        """
        ...


    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSAParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    D = ...
    DP = ...
    DQ = ...
    Exponent = ...
    InverseQ = ...
    Modulus = ...
    P = ...
    Q = ...


class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter): # skipped bases: <type 'object'>
    """
    RSAPKCS1KeyExchangeDeformatter()
    RSAPKCS1KeyExchangeDeformatter(key: AsymmetricAlgorithm)
    """
    @property
    def RNG(self) -> RandomNumberGenerator:
        """
        Get: RNG(self: RSAPKCS1KeyExchangeDeformatter) -> RandomNumberGenerator
        Set: RNG(self: RSAPKCS1KeyExchangeDeformatter) = value
        """
        ...


    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter): # skipped bases: <type 'object'>
    """
    RSAPKCS1KeyExchangeFormatter()
    RSAPKCS1KeyExchangeFormatter(key: AsymmetricAlgorithm)
    """
    @property
    def Rng(self) -> RandomNumberGenerator:
        """
        Get: Rng(self: RSAPKCS1KeyExchangeFormatter) -> RandomNumberGenerator
        Set: Rng(self: RSAPKCS1KeyExchangeFormatter) = value
        """
        ...


    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter): # skipped bases: <type 'object'>
    """
    RSAPKCS1SignatureDeformatter()
    RSAPKCS1SignatureDeformatter(key: AsymmetricAlgorithm)
    """
    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter): # skipped bases: <type 'object'>
    """
    RSAPKCS1SignatureFormatter()
    RSAPKCS1SignatureFormatter(key: AsymmetricAlgorithm)
    """
    def __new__(cls, key:AsymmetricAlgorithm = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: AsymmetricAlgorithm)
        """
        ...


class RSASignaturePadding(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Mode(self) -> RSASignaturePaddingMode:
        """ Get: Mode(self: RSASignaturePadding) -> RSASignaturePaddingMode """
        ...

    @property
    def Pkcs1(self) -> RSASignaturePadding:
        """ Get: Pkcs1() -> RSASignaturePadding """
        ...

    @property
    def Pss(self) -> RSASignaturePadding:
        """ Get: Pss() -> RSASignaturePadding """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: RSASignaturePadding) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RSASignaturePadding) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RSASignaturePaddingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RSASignaturePaddingMode, values: Pkcs1 (0), Pss (1) """
    Pkcs1: RSASignaturePaddingMode = ...
    Pss: RSASignaturePaddingMode = ...
    value__ = ...


class SHA1(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA1Cng(SHA1): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA1Cng() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA1Cng) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA1CryptoServiceProvider(SHA1): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA1CryptoServiceProvider() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA1CryptoServiceProvider) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA1Managed(SHA1): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA1Managed() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA1Managed) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA256(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA256Cng(SHA256): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA256Cng() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA256Cng) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA256CryptoServiceProvider(SHA256): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA256CryptoServiceProvider() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA256CryptoServiceProvider) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA256Managed(SHA256): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA256Managed() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA256Managed) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA384(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA384Cng(SHA384): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA384Cng() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA384Cng) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA384CryptoServiceProvider(SHA384): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA384CryptoServiceProvider() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA384CryptoServiceProvider) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA384Managed(SHA384): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA384Managed() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA384Managed) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA512(HashAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ no doc """
    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA512Cng(SHA512): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA512Cng() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA512Cng) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA512CryptoServiceProvider(SHA512): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA512CryptoServiceProvider() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA512CryptoServiceProvider) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SHA512Managed(SHA512): # skipped bases: <type 'IDisposable'>, <type 'ICryptoTransform'>, <type 'object'>
    """ SHA512Managed() """
    def Initialize(self): # -> 
        """ Initialize(self: SHA512Managed) """
        ...

    HashSizeValue = ...
    HashValue = ...
    State = ...


class SignatureDescription: # skipped bases: <type 'object'>, <type 'object'>
    """
    SignatureDescription()
    SignatureDescription(el: SecurityElement)
    """
    @property
    def DeformatterAlgorithm(self) -> str:
        """
        Get: DeformatterAlgorithm(self: SignatureDescription) -> str
        Set: DeformatterAlgorithm(self: SignatureDescription) = value
        """
        ...

    @property
    def DigestAlgorithm(self) -> str:
        """
        Get: DigestAlgorithm(self: SignatureDescription) -> str
        Set: DigestAlgorithm(self: SignatureDescription) = value
        """
        ...

    @property
    def FormatterAlgorithm(self) -> str:
        """
        Get: FormatterAlgorithm(self: SignatureDescription) -> str
        Set: FormatterAlgorithm(self: SignatureDescription) = value
        """
        ...

    @property
    def KeyAlgorithm(self) -> str:
        """
        Get: KeyAlgorithm(self: SignatureDescription) -> str
        Set: KeyAlgorithm(self: SignatureDescription) = value
        """
        ...


    def CreateDeformatter(self, key:AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """ CreateDeformatter(self: SignatureDescription, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter """
        ...

    def CreateDigest(self) -> HashAlgorithm:
        """ CreateDigest(self: SignatureDescription) -> HashAlgorithm """
        ...

    def CreateFormatter(self, key:AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """ CreateFormatter(self: SignatureDescription, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter """
        ...


class SignatureVerificationResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SignatureVerificationResult, values: AssemblyIdentityMismatch (1), BadDigest (-2146869232), BadSignatureFormat (-2146762749), BasicConstraintsNotObserved (-2146869223), CertificateExpired (-2146762495), CertificateExplicitlyDistrusted (-2146762479), CertificateMalformed (-2146762488), CertificateNotExplicitlyTrusted (-2146762748), CertificateRevoked (-2146762484), CertificateUsageNotAllowed (-2146762490), ContainingSignatureInvalid (2), CouldNotBuildChain (-2146762486), GenericTrustFailure (-2146762485), InvalidCertificateName (-2146762476), InvalidCertificatePolicy (-2146762477), InvalidCertificateRole (-2146762493), InvalidCertificateSignature (-2146869244), InvalidCertificateUsage (-2146762480), InvalidCountersignature (-2146869245), InvalidSignerCertificate (-2146869246), InvalidTimePeriodNesting (-2146762494), InvalidTimestamp (-2146869243), IssuerChainingError (-2146762489), MissingSignature (-2146762496), PathLengthConstraintViolated (-2146762492), PublicKeyTokenMismatch (3), PublisherMismatch (4), RevocationCheckFailure (-2146762482), SystemError (-2146869247), UnknownCriticalExtension (-2146762491), UnknownTrustProvider (-2146762751), UnknownVerificationAction (-2146762750), UntrustedCertificationAuthority (-2146762478), UntrustedRootCertificate (-2146762487), UntrustedTestRootCertificate (-2146762483), Valid (0) """
    AssemblyIdentityMismatch: SignatureVerificationResult = ...
    BadDigest: SignatureVerificationResult = ...
    BadSignatureFormat: SignatureVerificationResult = ...
    BasicConstraintsNotObserved: SignatureVerificationResult = ...
    CertificateExpired: SignatureVerificationResult = ...
    CertificateExplicitlyDistrusted: SignatureVerificationResult = ...
    CertificateMalformed: SignatureVerificationResult = ...
    CertificateNotExplicitlyTrusted: SignatureVerificationResult = ...
    CertificateRevoked: SignatureVerificationResult = ...
    CertificateUsageNotAllowed: SignatureVerificationResult = ...
    ContainingSignatureInvalid: SignatureVerificationResult = ...
    CouldNotBuildChain: SignatureVerificationResult = ...
    GenericTrustFailure: SignatureVerificationResult = ...
    InvalidCertificateName: SignatureVerificationResult = ...
    InvalidCertificatePolicy: SignatureVerificationResult = ...
    InvalidCertificateRole: SignatureVerificationResult = ...
    InvalidCertificateSignature: SignatureVerificationResult = ...
    InvalidCertificateUsage: SignatureVerificationResult = ...
    InvalidCountersignature: SignatureVerificationResult = ...
    InvalidSignerCertificate: SignatureVerificationResult = ...
    InvalidTimePeriodNesting: SignatureVerificationResult = ...
    InvalidTimestamp: SignatureVerificationResult = ...
    IssuerChainingError: SignatureVerificationResult = ...
    MissingSignature: SignatureVerificationResult = ...
    PathLengthConstraintViolated: SignatureVerificationResult = ...
    PublicKeyTokenMismatch: SignatureVerificationResult = ...
    PublisherMismatch: SignatureVerificationResult = ...
    RevocationCheckFailure: SignatureVerificationResult = ...
    SystemError: SignatureVerificationResult = ...
    UnknownCriticalExtension: SignatureVerificationResult = ...
    UnknownTrustProvider: SignatureVerificationResult = ...
    UnknownVerificationAction: SignatureVerificationResult = ...
    UntrustedCertificationAuthority: SignatureVerificationResult = ...
    UntrustedRootCertificate: SignatureVerificationResult = ...
    UntrustedTestRootCertificate: SignatureVerificationResult = ...
    Valid: SignatureVerificationResult = ...
    value__ = ...


class StrongNameSignatureInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HashAlgorithm(self) -> str:
        """ Get: HashAlgorithm(self: StrongNameSignatureInformation) -> str """
        ...

    @property
    def HResult(self) -> int:
        """ Get: HResult(self: StrongNameSignatureInformation) -> int """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: StrongNameSignatureInformation) -> bool """
        ...

    @property
    def PublicKey(self) -> AsymmetricAlgorithm:
        """ Get: PublicKey(self: StrongNameSignatureInformation) -> AsymmetricAlgorithm """
        ...

    @property
    def VerificationResult(self) -> SignatureVerificationResult:
        """ Get: VerificationResult(self: StrongNameSignatureInformation) -> SignatureVerificationResult """
        ...



class ToBase64Transform(ICryptoTransform): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ ToBase64Transform() """
    def Clear(self): # -> 
        """ Clear(self: ToBase64Transform) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: ToBase64Transform) """
        ...


class TripleDES(SymmetricAlgorithm): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsWeakKey(rgbKey:Array) -> bool:
        """ IsWeakKey(rgbKey: Array[Byte]) -> bool """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class TripleDESCng(ICngSymmetricAlgorithm, TripleDES): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    TripleDESCng()
    TripleDESCng(keyName: str)
    TripleDESCng(keyName: str, provider: CngProvider)
    TripleDESCng(keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions)
    """
    @property
    def KeySize(self) -> int:
        """
        Get: KeySize(self: TripleDESCng) -> int
        Set: KeySize(self: TripleDESCng) = value
        """
        ...


    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateDecryptor(self: TripleDESCng) -> ICryptoTransform
        CreateDecryptor(self: TripleDESCng, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """
        CreateEncryptor(self: TripleDESCng) -> ICryptoTransform
        CreateEncryptor(self: TripleDESCng, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform
        """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: TripleDESCng) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: TripleDESCng) """
        ...

    def __new__(cls, keyName:str = ..., provider:CngProvider = ..., openOptions:CngKeyOpenOptions = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keyName: str)
        __new__(cls: type, keyName: str, provider: CngProvider)
        __new__(cls: type, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions)
        """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


class TripleDESCryptoServiceProvider(TripleDES): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ TripleDESCryptoServiceProvider() """
    def CreateDecryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateDecryptor(self: TripleDESCryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def CreateEncryptor(self, rgbKey:Array = ..., rgbIV:Array = ...) -> ICryptoTransform:
        """ CreateEncryptor(self: TripleDESCryptoServiceProvider, rgbKey: Array[Byte], rgbIV: Array[Byte]) -> ICryptoTransform """
        ...

    def GenerateIV(self): # -> 
        """ GenerateIV(self: TripleDESCryptoServiceProvider) """
        ...

    def GenerateKey(self): # -> 
        """ GenerateKey(self: TripleDESCryptoServiceProvider) """
        ...

    BlockSizeValue = ...
    FeedbackSizeValue = ...
    IVValue = ...
    KeySizeValue = ...
    KeyValue = ...
    LegalBlockSizesValue = ...
    LegalKeySizesValue = ...
    ModeValue = ...
    PaddingValue = ...


# variables with complex values

