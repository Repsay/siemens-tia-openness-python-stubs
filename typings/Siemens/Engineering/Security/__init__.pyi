# encoding: utf-8
# module Siemens.Engineering.Security calls itself Security
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.HW.Features import DeviceItemFeature

from System import DateTime, Enum, IEquatable, UInt32

from System.IO import FileInfo

from System.Security import SecureString

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class Certificate(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Certificate Item """
    @property
    def HasPrivateKey(self) -> bool:
        """
        Indicates whether the certificate contains a private key or not.

        Get: HasPrivateKey(self: Certificate) -> bool
        """
        ...

    @property
    def Id(self) -> UInt32:
        """
        Identification of a Certificate

        Get: Id(self: Certificate) -> UInt32
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Certificate) -> IEngineeringObject
        """
        ...

    @property
    def SubjectCommonName(self) -> str:
        """
        The subject common name of the certificate.

        Get: SubjectCommonName(self: Certificate) -> str
        """
        ...

    @property
    def ValidUntil(self) -> DateTime:
        """
        The valid until date of the certificate.

        Get: ValidUntil(self: Certificate) -> DateTime
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: Certificate)

            Deletes this instance.
        """
        ...

    def Export(self, filePath:FileInfo, exportFormat:CertificateExportFormat): # ->
        """
        Export(self: Certificate, filePath: FileInfo, exportFormat: CertificateExportFormat)

            Export the certificate

            filePath: Path to exported certificate

            exportFormat: Export format
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Certificate) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Certificate) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CertificateComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of certificates """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: CertificateComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CertificateComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath:FileInfo, password:SecureString = ...) -> Certificate:
        """
        Import(self: CertificateComposition, filePath: FileInfo) -> Certificate

            Imports a certificate

            filePath: Path to certificate file

            Returns: Siemens.Engineering.Security.Certificate

        Import(self: CertificateComposition, filePath: FileInfo, password: SecureString) -> Certificate

            Imports a certificate

            filePath: Path to certificate file

            password: The password of the certificate file

            Returns: Siemens.Engineering.Security.Certificate
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CertificateComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Certificate](enumerable: IEnumerable[Certificate], value: Certificate) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CertificateExportFormat(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Exported certificate format.

    enum CertificateExportFormat, values: Cer (1), Der (2), None (0)
    """
    Cer: CertificateExportFormat = ...
    Der: CertificateExportFormat = ...
    value__ = ...


class CertificateTemplate(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Certificate Template """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CertificateTemplate) -> IEngineeringObject
        """
        ...

    @property
    def Signature(self) -> SignatureAlgorithm:
        """
        The signature algorithm

        Get: Signature(self: CertificateTemplate) -> SignatureAlgorithm

        Set: Signature(self: CertificateTemplate) = value
        """
        ...

    @property
    def SubjectAlternativeNames(self) -> SubjectAlternativeNameComposition:
        """
        All subject alternative name entries.

        Get: SubjectAlternativeNames(self: CertificateTemplate) -> SubjectAlternativeNameComposition
        """
        ...

    @property
    def SubjectCommonName(self) -> str:
        """
        The subject common name of the certificate.

        Get: SubjectCommonName(self: CertificateTemplate) -> str

        Set: SubjectCommonName(self: CertificateTemplate) = value
        """
        ...

    @property
    def Usage(self) -> CertificateUsage:
        """
        The usage for the certificate

        Get: Usage(self: CertificateTemplate) -> CertificateUsage

        Set: Usage(self: CertificateTemplate) = value
        """
        ...

    @property
    def ValidFrom(self) -> DateTime:
        """
        The valid from date of the certificate.

        Get: ValidFrom(self: CertificateTemplate) -> DateTime

        Set: ValidFrom(self: CertificateTemplate) = value
        """
        ...

    @property
    def ValidUntil(self) -> DateTime:
        """
        The valid until date of the certificate.

        Get: ValidUntil(self: CertificateTemplate) -> DateTime

        Set: ValidUntil(self: CertificateTemplate) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CertificateTemplate) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CertificateTemplate) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CertificateUsage(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The key usage for a certificate

    enum CertificateUsage, values: None (0), OpcUaClient (2), OpcUaClientServer (3), OpcUaServer (4), Tls (1), WebServer (5)
    """
    OpcUaClient: CertificateUsage = ...
    OpcUaClientServer: CertificateUsage = ...
    OpcUaServer: CertificateUsage = ...
    Tls: CertificateUsage = ...
    value__ = ...
    WebServer: CertificateUsage = ...


class LocalCertificateManager(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Device certificate manager operates on local and global certificates """
    @property
    def EnableGlobalCertificatesStore(self) -> bool:
        """
        Enables or disables the global certificate store

        Get: EnableGlobalCertificatesStore(self: LocalCertificateManager) -> bool

        Set: EnableGlobalCertificatesStore(self: LocalCertificateManager) = value
        """
        ...

    @property
    def LocalCertificateStore(self) -> LocalCertificateStore:
        """
        The local certificate store

        Get: LocalCertificateStore(self: LocalCertificateManager) -> LocalCertificateStore
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LocalCertificateManager) -> IEngineeringObject
        """
        ...



class LocalCertificateStore(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The Local Store holds all not-public certificates """
    @property
    def Certificates(self) -> CertificateComposition:
        """
        Collections of all self signed certificates

        Get: Certificates(self: LocalCertificateStore) -> CertificateComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LocalCertificateStore) -> IEngineeringObject
        """
        ...


    def GetCertificateTemplate(self, certificateUsage:CertificateUsage) -> CertificateTemplate:
        """
        GetCertificateTemplate(self: LocalCertificateStore, certificateUsage: CertificateUsage) -> CertificateTemplate

            Get default template values for specific

            certificateUsage: This is a usage

            Returns: Siemens.Engineering.Security.CertificateTemplate
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LocalCertificateStore) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LocalCertificateStore) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SignatureAlgorithm(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The signature of a certificate, i.e. the algorithm

    enum SignatureAlgorithm, values: None (0), Sha1RSA (1), Sha256RSA (2)
    """
    Sha1RSA: SignatureAlgorithm = ...
    Sha256RSA: SignatureAlgorithm = ...
    value__ = ...


class SubjectAlternativeName(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ An entry of SubjectAlternativeNames """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SubjectAlternativeName) -> IEngineeringObject
        """
        ...

    @property
    def Type(self) -> SubjectAlternativeNameType:
        """
        The type of the entry

        Get: Type(self: SubjectAlternativeName) -> SubjectAlternativeNameType
        """
        ...

    @property
    def Value(self) -> str:
        """
        The value of the entry

        Get: Value(self: SubjectAlternativeName) -> str
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: SubjectAlternativeName)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SubjectAlternativeName) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SubjectAlternativeName) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SubjectAlternativeNameComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The composition of all subject alternative name entries """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SubjectAlternativeNameComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SubjectAlternativeNameComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SubjectAlternativeNameComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SubjectAlternativeName](enumerable: IEnumerable[SubjectAlternativeName], value: SubjectAlternativeName) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SubjectAlternativeNameType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The subject alternative name type

    enum SubjectAlternativeNameType, values: Dns (1), Email (2), IP (3), None (0), Uri (4)
    """
    Dns: SubjectAlternativeNameType = ...
    Email: SubjectAlternativeNameType = ...
    IP: SubjectAlternativeNameType = ...
    Uri: SubjectAlternativeNameType = ...
    value__ = ...
