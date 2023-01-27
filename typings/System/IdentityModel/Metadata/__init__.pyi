# encoding: utf-8
# module System.IdentityModel.Metadata calls itself Metadata
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import DateTime, Enum, Nullable, Uri

from System.Collections import ICollection, SortedList

from System.Collections.Generic import List

from System.Collections.ObjectModel import KeyedCollection

from System.Globalization import CultureInfo

from System.IdentityModel.Selectors import (SecurityTokenSerializer, 
    X509CertificateValidator)

from System.IdentityModel.Tokens import (SecurityKeyIdentifier, 
    SigningCredentials)

from System.IO import Stream

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    X509RevocationMode)

from System.ServiceModel.Security import X509CertificateValidationMode

from System.Xml import XmlReader

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class RoleDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Contacts(self) -> ICollection:
        """ Get: Contacts(self: RoleDescriptor) -> ICollection[ContactPerson] """
        ...

    @property
    def ErrorUrl(self) -> Uri:
        """
        Get: ErrorUrl(self: RoleDescriptor) -> Uri
        Set: ErrorUrl(self: RoleDescriptor) = value
        """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: RoleDescriptor) -> ICollection[KeyDescriptor] """
        ...

    @property
    def Organization(self) -> Organization:
        """
        Get: Organization(self: RoleDescriptor) -> Organization
        Set: Organization(self: RoleDescriptor) = value
        """
        ...

    @property
    def ProtocolsSupported(self) -> ICollection:
        """ Get: ProtocolsSupported(self: RoleDescriptor) -> ICollection[Uri] """
        ...

    @property
    def ValidUntil(self) -> DateTime:
        """
        Get: ValidUntil(self: RoleDescriptor) -> DateTime
        Set: ValidUntil(self: RoleDescriptor) = value
        """
        ...



class WebServiceDescriptor(RoleDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ClaimTypesOffered(self) -> ICollection:
        """ Get: ClaimTypesOffered(self: WebServiceDescriptor) -> ICollection[DisplayClaim] """
        ...

    @property
    def ClaimTypesRequested(self) -> ICollection:
        """ Get: ClaimTypesRequested(self: WebServiceDescriptor) -> ICollection[DisplayClaim] """
        ...

    @property
    def ServiceDescription(self) -> str:
        """
        Get: ServiceDescription(self: WebServiceDescriptor) -> str
        Set: ServiceDescription(self: WebServiceDescriptor) = value
        """
        ...

    @property
    def ServiceDisplayName(self) -> str:
        """
        Get: ServiceDisplayName(self: WebServiceDescriptor) -> str
        Set: ServiceDisplayName(self: WebServiceDescriptor) = value
        """
        ...

    @property
    def TargetScopes(self) -> ICollection:
        """ Get: TargetScopes(self: WebServiceDescriptor) -> ICollection[EndpointReference] """
        ...

    @property
    def TokenTypesOffered(self) -> ICollection:
        """ Get: TokenTypesOffered(self: WebServiceDescriptor) -> ICollection[Uri] """
        ...



class ApplicationServiceDescriptor(WebServiceDescriptor): # skipped bases: <type 'object'>
    """ ApplicationServiceDescriptor() """
    @property
    def Endpoints(self) -> ICollection:
        """ Get: Endpoints(self: ApplicationServiceDescriptor) -> ICollection[EndpointReference] """
        ...

    @property
    def PassiveRequestorEndpoints(self) -> ICollection:
        """ Get: PassiveRequestorEndpoints(self: ApplicationServiceDescriptor) -> ICollection[EndpointReference] """
        ...



class ContactPerson: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContactPerson()
    ContactPerson(contactType: ContactType)
    """
    @property
    def Company(self) -> str:
        """
        Get: Company(self: ContactPerson) -> str
        Set: Company(self: ContactPerson) = value
        """
        ...

    @property
    def EmailAddresses(self) -> ICollection:
        """ Get: EmailAddresses(self: ContactPerson) -> ICollection[str] """
        ...

    @property
    def GivenName(self) -> str:
        """
        Get: GivenName(self: ContactPerson) -> str
        Set: GivenName(self: ContactPerson) = value
        """
        ...

    @property
    def Surname(self) -> str:
        """
        Get: Surname(self: ContactPerson) -> str
        Set: Surname(self: ContactPerson) = value
        """
        ...

    @property
    def TelephoneNumbers(self) -> ICollection:
        """ Get: TelephoneNumbers(self: ContactPerson) -> ICollection[str] """
        ...

    @property
    def Type(self) -> ContactType:
        """
        Get: Type(self: ContactPerson) -> ContactType
        Set: Type(self: ContactPerson) = value
        """
        ...



class ContactType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContactType, values: Administrative (3), Billing (4), Other (5), Support (2), Technical (1), Unspecified (0) """
    Administrative: ContactType = ...
    Billing: ContactType = ...
    Other: ContactType = ...
    Support: ContactType = ...
    Technical: ContactType = ...
    Unspecified: ContactType = ...
    value__ = ...


class DisplayClaim: # skipped bases: <type 'object'>, <type 'object'>
    """
    DisplayClaim(claimType: str)
    DisplayClaim(claimType: str, displayTag: str, description: str)
    DisplayClaim(claimType: str, displayTag: str, description: str, displayValue: str)
    DisplayClaim(claimType: str, displayTag: str, description: str, displayValue: str, optional: bool)
    """
    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType(self: DisplayClaim) -> str """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: DisplayClaim) -> str
        Set: Description(self: DisplayClaim) = value
        """
        ...

    @property
    def DisplayTag(self) -> str:
        """
        Get: DisplayTag(self: DisplayClaim) -> str
        Set: DisplayTag(self: DisplayClaim) = value
        """
        ...

    @property
    def DisplayValue(self) -> str:
        """
        Get: DisplayValue(self: DisplayClaim) -> str
        Set: DisplayValue(self: DisplayClaim) = value
        """
        ...

    @property
    def Optional(self) -> bool:
        """
        Get: Optional(self: DisplayClaim) -> bool
        Set: Optional(self: DisplayClaim) = value
        """
        ...

    @property
    def WriteOptionalAttribute(self) -> bool:
        """
        Get: WriteOptionalAttribute(self: DisplayClaim) -> bool
        Set: WriteOptionalAttribute(self: DisplayClaim) = value
        """
        ...


    @staticmethod
    def CreateDisplayClaimFromClaimType(claimType:str) -> DisplayClaim:
        """ CreateDisplayClaimFromClaimType(claimType: str) -> DisplayClaim """
        ...


class EncryptionMethod: # skipped bases: <type 'object'>, <type 'object'>
    """ EncryptionMethod(algorithm: Uri) """
    @property
    def Algorithm(self) -> Uri:
        """
        Get: Algorithm(self: EncryptionMethod) -> Uri
        Set: Algorithm(self: EncryptionMethod) = value
        """
        ...



class MetadataBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SigningCredentials(self) -> SigningCredentials:
        """
        Get: SigningCredentials(self: MetadataBase) -> SigningCredentials
        Set: SigningCredentials(self: MetadataBase) = value
        """
        ...



class EntitiesDescriptor(MetadataBase): # skipped bases: <type 'object'>
    """
    EntitiesDescriptor()
    EntitiesDescriptor(entityGroupList: Collection[EntitiesDescriptor])
    EntitiesDescriptor(entityList: Collection[EntityDescriptor])
    EntitiesDescriptor(entityList: Collection[EntityDescriptor], entityGroupList: Collection[EntitiesDescriptor])
    """
    @property
    def ChildEntities(self) -> ICollection:
        """ Get: ChildEntities(self: EntitiesDescriptor) -> ICollection[EntityDescriptor] """
        ...

    @property
    def ChildEntityGroups(self) -> ICollection:
        """ Get: ChildEntityGroups(self: EntitiesDescriptor) -> ICollection[EntitiesDescriptor] """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EntitiesDescriptor) -> str
        Set: Name(self: EntitiesDescriptor) = value
        """
        ...


    def __new__(cls, *__args:Collection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, entityGroupList: Collection[EntitiesDescriptor])
        __new__(cls: type, entityList: Collection[EntityDescriptor])
        __new__(cls: type, entityList: Collection[EntityDescriptor], entityGroupList: Collection[EntitiesDescriptor])
        """
        ...


class EntityDescriptor(MetadataBase): # skipped bases: <type 'object'>
    """
    EntityDescriptor()
    EntityDescriptor(entityId: EntityId)
    """
    @property
    def Contacts(self) -> ICollection:
        """ Get: Contacts(self: EntityDescriptor) -> ICollection[ContactPerson] """
        ...

    @property
    def EntityId(self) -> EntityId:
        """
        Get: EntityId(self: EntityDescriptor) -> EntityId
        Set: EntityId(self: EntityDescriptor) = value
        """
        ...

    @property
    def FederationId(self) -> str:
        """
        Get: FederationId(self: EntityDescriptor) -> str
        Set: FederationId(self: EntityDescriptor) = value
        """
        ...

    @property
    def Organization(self) -> Organization:
        """
        Get: Organization(self: EntityDescriptor) -> Organization
        Set: Organization(self: EntityDescriptor) = value
        """
        ...

    @property
    def RoleDescriptors(self) -> ICollection:
        """ Get: RoleDescriptors(self: EntityDescriptor) -> ICollection[RoleDescriptor] """
        ...


    def __new__(cls, entityId:EntityId = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, entityId: EntityId)
        """
        ...


class EntityId: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityId()
    EntityId(id: str)
    """
    @property
    def Id(self) -> str:
        """
        Get: Id(self: EntityId) -> str
        Set: Id(self: EntityId) = value
        """
        ...



class SingleSignOnDescriptor(RoleDescriptor): # skipped bases: <type 'object'>
    """ SingleSignOnDescriptor() """
    @property
    def ArtifactResolutionServices(self) -> IndexedProtocolEndpointDictionary:
        """ Get: ArtifactResolutionServices(self: SingleSignOnDescriptor) -> IndexedProtocolEndpointDictionary """
        ...

    @property
    def NameIdentifierFormats(self) -> ICollection:
        """ Get: NameIdentifierFormats(self: SingleSignOnDescriptor) -> ICollection[Uri] """
        ...

    @property
    def SingleLogoutServices(self) -> Collection:
        """ Get: SingleLogoutServices(self: SingleSignOnDescriptor) -> Collection[ProtocolEndpoint] """
        ...



class IdentityProviderSingleSignOnDescriptor(SingleSignOnDescriptor): # skipped bases: <type 'object'>
    """ IdentityProviderSingleSignOnDescriptor() """
    @property
    def SingleSignOnServices(self) -> ICollection:
        """ Get: SingleSignOnServices(self: IdentityProviderSingleSignOnDescriptor) -> ICollection[ProtocolEndpoint] """
        ...

    @property
    def SupportedAttributes(self) -> ICollection:
        """ Get: SupportedAttributes(self: IdentityProviderSingleSignOnDescriptor) -> ICollection[Saml2Attribute] """
        ...

    @property
    def WantAuthenticationRequestsSigned(self) -> bool:
        """
        Get: WantAuthenticationRequestsSigned(self: IdentityProviderSingleSignOnDescriptor) -> bool
        Set: WantAuthenticationRequestsSigned(self: IdentityProviderSingleSignOnDescriptor) = value
        """
        ...



class ProtocolEndpoint: # skipped bases: <type 'object'>, <type 'object'>
    """
    ProtocolEndpoint()
    ProtocolEndpoint(binding: Uri, location: Uri)
    """
    @property
    def Binding(self) -> Uri:
        """
        Get: Binding(self: ProtocolEndpoint) -> Uri
        Set: Binding(self: ProtocolEndpoint) = value
        """
        ...

    @property
    def Location(self) -> Uri:
        """
        Get: Location(self: ProtocolEndpoint) -> Uri
        Set: Location(self: ProtocolEndpoint) = value
        """
        ...

    @property
    def ResponseLocation(self) -> Uri:
        """
        Get: ResponseLocation(self: ProtocolEndpoint) -> Uri
        Set: ResponseLocation(self: ProtocolEndpoint) = value
        """
        ...



class IndexedProtocolEndpoint(ProtocolEndpoint): # skipped bases: <type 'object'>
    """
    IndexedProtocolEndpoint()
    IndexedProtocolEndpoint(index: int, binding: Uri, location: Uri)
    """
    @property
    def Index(self) -> int:
        """
        Get: Index(self: IndexedProtocolEndpoint) -> int
        Set: Index(self: IndexedProtocolEndpoint) = value
        """
        ...

    @property
    def IsDefault(self) -> Nullable:
        """
        Get: IsDefault(self: IndexedProtocolEndpoint) -> Nullable[bool]
        Set: IsDefault(self: IndexedProtocolEndpoint) = value
        """
        ...



class IndexedProtocolEndpointDictionary(SortedList): # skipped bases: <type 'IEnumerable[KeyValuePair[int, IndexedProtocolEndpoint]]'>, <type 'ICollection[KeyValuePair[int, IndexedProtocolEndpoint]]'>, <type 'IDictionary[int, IndexedProtocolEndpoint]'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[KeyValuePair[int, IndexedProtocolEndpoint]]'>, <type 'IReadOnlyDictionary[int, IndexedProtocolEndpoint]'>, <type 'ICollection'>, <type 'object'>
    """ IndexedProtocolEndpointDictionary() """
    @property
    def Default(self) -> IndexedProtocolEndpoint:
        """ Get: Default(self: IndexedProtocolEndpointDictionary) -> IndexedProtocolEndpoint """
        ...



class KeyDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """
    KeyDescriptor()
    KeyDescriptor(ski: SecurityKeyIdentifier)
    """
    @property
    def EncryptionMethods(self) -> ICollection:
        """ Get: EncryptionMethods(self: KeyDescriptor) -> ICollection[EncryptionMethod] """
        ...

    @property
    def KeyInfo(self) -> SecurityKeyIdentifier:
        """
        Get: KeyInfo(self: KeyDescriptor) -> SecurityKeyIdentifier
        Set: KeyInfo(self: KeyDescriptor) = value
        """
        ...

    @property
    def Use(self) -> KeyType:
        """
        Get: Use(self: KeyDescriptor) -> KeyType
        Set: Use(self: KeyDescriptor) = value
        """
        ...



class KeyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyType, values: Encryption (2), Signing (1), Unspecified (0) """
    Encryption: KeyType = ...
    Signing: KeyType = ...
    Unspecified: KeyType = ...
    value__ = ...


class LocalizedEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Language(self) -> CultureInfo:
        """
        Get: Language(self: LocalizedEntry) -> CultureInfo
        Set: Language(self: LocalizedEntry) = value
        """
        ...



class LocalizedEntryCollection(KeyedCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[T]'>, <type 'IReadOnlyList[T]'>, <type 'ICollection[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'ICollection'>, <type 'object'>
    """ LocalizedEntryCollection[T]() """
    pass

class LocalizedName(LocalizedEntry): # skipped bases: <type 'object'>
    """
    LocalizedName()
    LocalizedName(name: str, language: CultureInfo)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: LocalizedName) -> str
        Set: Name(self: LocalizedName) = value
        """
        ...



class LocalizedUri(LocalizedEntry): # skipped bases: <type 'object'>
    """
    LocalizedUri()
    LocalizedUri(uri: Uri, language: CultureInfo)
    """
    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: LocalizedUri) -> Uri
        Set: Uri(self: LocalizedUri) = value
        """
        ...



class MetadataSerializationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MetadataSerializationException()
    MetadataSerializationException(message: str)
    MetadataSerializationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MetadataSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """
    MetadataSerializer()
    MetadataSerializer(tokenSerializer: SecurityTokenSerializer)
    """
    @property
    def CertificateValidationMode(self) -> X509CertificateValidationMode:
        """
        Get: CertificateValidationMode(self: MetadataSerializer) -> X509CertificateValidationMode
        Set: CertificateValidationMode(self: MetadataSerializer) = value
        """
        ...

    @property
    def CertificateValidator(self) -> X509CertificateValidator:
        """
        Get: CertificateValidator(self: MetadataSerializer) -> X509CertificateValidator
        Set: CertificateValidator(self: MetadataSerializer) = value
        """
        ...

    @property
    def RevocationMode(self) -> X509RevocationMode:
        """
        Get: RevocationMode(self: MetadataSerializer) -> X509RevocationMode
        Set: RevocationMode(self: MetadataSerializer) = value
        """
        ...

    @property
    def SecurityTokenSerializer(self) -> SecurityTokenSerializer:
        """ Get: SecurityTokenSerializer(self: MetadataSerializer) -> SecurityTokenSerializer """
        ...

    @property
    def TrustedIssuers(self) -> List:
        """ Get: TrustedIssuers(self: MetadataSerializer) -> List[str] """
        ...

    @property
    def TrustedStoreLocation(self) -> StoreLocation:
        """
        Get: TrustedStoreLocation(self: MetadataSerializer) -> StoreLocation
        Set: TrustedStoreLocation(self: MetadataSerializer) = value
        """
        ...


    def CreateApplicationServiceInstance(self, *args): #cannot find CLR method
        """ CreateApplicationServiceInstance(self: MetadataSerializer) -> ApplicationServiceDescriptor """
        ...

    def CreateContactPersonInstance(self, *args): #cannot find CLR method
        """ CreateContactPersonInstance(self: MetadataSerializer) -> ContactPerson """
        ...

    def CreateEntitiesDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateEntitiesDescriptorInstance(self: MetadataSerializer) -> EntitiesDescriptor """
        ...

    def CreateEntityDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateEntityDescriptorInstance(self: MetadataSerializer) -> EntityDescriptor """
        ...

    def CreateIdentityProviderSingleSignOnDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateIdentityProviderSingleSignOnDescriptorInstance(self: MetadataSerializer) -> IdentityProviderSingleSignOnDescriptor """
        ...

    def CreateIndexedProtocolEndpointInstance(self, *args): #cannot find CLR method
        """ CreateIndexedProtocolEndpointInstance(self: MetadataSerializer) -> IndexedProtocolEndpoint """
        ...

    def CreateKeyDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateKeyDescriptorInstance(self: MetadataSerializer) -> KeyDescriptor """
        ...

    def CreateLocalizedNameInstance(self, *args): #cannot find CLR method
        """ CreateLocalizedNameInstance(self: MetadataSerializer) -> LocalizedName """
        ...

    def CreateLocalizedUriInstance(self, *args): #cannot find CLR method
        """ CreateLocalizedUriInstance(self: MetadataSerializer) -> LocalizedUri """
        ...

    def CreateOrganizationInstance(self, *args): #cannot find CLR method
        """ CreateOrganizationInstance(self: MetadataSerializer) -> Organization """
        ...

    def CreateProtocolEndpointInstance(self, *args): #cannot find CLR method
        """ CreateProtocolEndpointInstance(self: MetadataSerializer) -> ProtocolEndpoint """
        ...

    def CreateSecurityTokenServiceDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateSecurityTokenServiceDescriptorInstance(self: MetadataSerializer) -> SecurityTokenServiceDescriptor """
        ...

    def CreateServiceProviderSingleSignOnDescriptorInstance(self, *args): #cannot find CLR method
        """ CreateServiceProviderSingleSignOnDescriptorInstance(self: MetadataSerializer) -> ServiceProviderSingleSignOnDescriptor """
        ...

    def GetMetadataSigningCertificate(self, *args): #cannot find CLR method
        """ GetMetadataSigningCertificate(self: MetadataSerializer, ski: SecurityKeyIdentifier) -> X509Certificate2 """
        ...

    def ReadApplicationServiceDescriptor(self, *args): #cannot find CLR method
        """ ReadApplicationServiceDescriptor(self: MetadataSerializer, reader: XmlReader) -> ApplicationServiceDescriptor """
        ...

    def ReadAttribute(self, *args): #cannot find CLR method
        """ ReadAttribute(self: MetadataSerializer, reader: XmlReader) -> Saml2Attribute """
        ...

    def ReadContactPerson(self, *args): #cannot find CLR method
        """ ReadContactPerson(self: MetadataSerializer, reader: XmlReader) -> ContactPerson """
        ...

    def ReadCustomAttributes(self, *args): #cannot find CLR method
        """ ReadCustomAttributes[T](self: MetadataSerializer, reader: XmlReader, target: T) """
        ...

    def ReadCustomElement(self, *args): #cannot find CLR method
        """ ReadCustomElement[T](self: MetadataSerializer, reader: XmlReader, target: T) -> bool """
        ...

    def ReadCustomRoleDescriptor(self, *args): #cannot find CLR method
        """ ReadCustomRoleDescriptor(self: MetadataSerializer, xsiType: str, reader: XmlReader, entityDescriptor: EntityDescriptor) """
        ...

    def ReadDisplayClaim(self, *args): #cannot find CLR method
        """ ReadDisplayClaim(self: MetadataSerializer, reader: XmlReader) -> DisplayClaim """
        ...

    def ReadEntitiesDescriptor(self, *args): #cannot find CLR method
        """ ReadEntitiesDescriptor(self: MetadataSerializer, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> EntitiesDescriptor """
        ...

    def ReadEntityDescriptor(self, *args): #cannot find CLR method
        """ ReadEntityDescriptor(self: MetadataSerializer, inputReader: XmlReader, tokenResolver: SecurityTokenResolver) -> EntityDescriptor """
        ...

    def ReadIdentityProviderSingleSignOnDescriptor(self, *args): #cannot find CLR method
        """ ReadIdentityProviderSingleSignOnDescriptor(self: MetadataSerializer, reader: XmlReader) -> IdentityProviderSingleSignOnDescriptor """
        ...

    def ReadIndexedProtocolEndpoint(self, *args): #cannot find CLR method
        """ ReadIndexedProtocolEndpoint(self: MetadataSerializer, reader: XmlReader) -> IndexedProtocolEndpoint """
        ...

    def ReadKeyDescriptor(self, *args): #cannot find CLR method
        """ ReadKeyDescriptor(self: MetadataSerializer, reader: XmlReader) -> KeyDescriptor """
        ...

    def ReadLocalizedName(self, *args): #cannot find CLR method
        """ ReadLocalizedName(self: MetadataSerializer, reader: XmlReader) -> LocalizedName """
        ...

    def ReadLocalizedUri(self, *args): #cannot find CLR method
        """ ReadLocalizedUri(self: MetadataSerializer, reader: XmlReader) -> LocalizedUri """
        ...

    def ReadMetadata(self, *__args:XmlReader) -> MetadataBase:
        """
        ReadMetadata(self: MetadataSerializer, reader: XmlReader) -> MetadataBase
        ReadMetadata(self: MetadataSerializer, stream: Stream) -> MetadataBase
        ReadMetadata(self: MetadataSerializer, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> MetadataBase
        """
        ...

    def ReadMetadataCore(self, *args): #cannot find CLR method
        """ ReadMetadataCore(self: MetadataSerializer, reader: XmlReader, tokenResolver: SecurityTokenResolver) -> MetadataBase """
        ...

    def ReadOrganization(self, *args): #cannot find CLR method
        """ ReadOrganization(self: MetadataSerializer, reader: XmlReader) -> Organization """
        ...

    def ReadProtocolEndpoint(self, *args): #cannot find CLR method
        """ ReadProtocolEndpoint(self: MetadataSerializer, reader: XmlReader) -> ProtocolEndpoint """
        ...

    def ReadRoleDescriptorAttributes(self, *args): #cannot find CLR method
        """ ReadRoleDescriptorAttributes(self: MetadataSerializer, reader: XmlReader, roleDescriptor: RoleDescriptor) """
        ...

    def ReadRoleDescriptorElement(self, *args): #cannot find CLR method
        """ ReadRoleDescriptorElement(self: MetadataSerializer, reader: XmlReader, roleDescriptor: RoleDescriptor) -> bool """
        ...

    def ReadSecurityTokenServiceDescriptor(self, *args): #cannot find CLR method
        """ ReadSecurityTokenServiceDescriptor(self: MetadataSerializer, reader: XmlReader) -> SecurityTokenServiceDescriptor """
        ...

    def ReadServiceProviderSingleSignOnDescriptor(self, *args): #cannot find CLR method
        """ ReadServiceProviderSingleSignOnDescriptor(self: MetadataSerializer, reader: XmlReader) -> ServiceProviderSingleSignOnDescriptor """
        ...

    def ReadSingleSignOnDescriptorAttributes(self, *args): #cannot find CLR method
        """ ReadSingleSignOnDescriptorAttributes(self: MetadataSerializer, reader: XmlReader, roleDescriptor: SingleSignOnDescriptor) """
        ...

    def ReadSingleSignOnDescriptorElement(self, *args): #cannot find CLR method
        """ ReadSingleSignOnDescriptorElement(self: MetadataSerializer, reader: XmlReader, singleSignOnDescriptor: SingleSignOnDescriptor) -> bool """
        ...

    def ReadWebServiceDescriptorAttributes(self, *args): #cannot find CLR method
        """ ReadWebServiceDescriptorAttributes(self: MetadataSerializer, reader: XmlReader, roleDescriptor: WebServiceDescriptor) """
        ...

    def ReadWebServiceDescriptorElement(self, reader:XmlReader, roleDescriptor:WebServiceDescriptor) -> bool:
        """ ReadWebServiceDescriptorElement(self: MetadataSerializer, reader: XmlReader, roleDescriptor: WebServiceDescriptor) -> bool """
        ...

    def ValidateIssuer(self, *args): #cannot find CLR method
        """ ValidateIssuer(self: MetadataSerializer, signingCertificate: X509Certificate2) """
        ...

    def ValidateSigningCredential(self, *args): #cannot find CLR method
        """ ValidateSigningCredential(self: MetadataSerializer, signingCredentials: SigningCredentials) """
        ...

    def WriteApplicationServiceDescriptor(self, *args): #cannot find CLR method
        """ WriteApplicationServiceDescriptor(self: MetadataSerializer, writer: XmlWriter, appService: ApplicationServiceDescriptor) """
        ...

    def WriteAttribute(self, *args): #cannot find CLR method
        """ WriteAttribute(self: MetadataSerializer, writer: XmlWriter, data: Saml2Attribute) """
        ...

    def WriteContactPerson(self, *args): #cannot find CLR method
        """ WriteContactPerson(self: MetadataSerializer, writer: XmlWriter, contactPerson: ContactPerson) """
        ...

    def WriteCustomAttributes(self, *args): #cannot find CLR method
        """ WriteCustomAttributes[T](self: MetadataSerializer, writer: XmlWriter, source: T) """
        ...

    def WriteCustomElements(self, *args): #cannot find CLR method
        """ WriteCustomElements[T](self: MetadataSerializer, writer: XmlWriter, source: T) """
        ...

    def WriteDisplayClaim(self, *args): #cannot find CLR method
        """ WriteDisplayClaim(self: MetadataSerializer, writer: XmlWriter, claim: DisplayClaim) """
        ...

    def WriteEntitiesDescriptor(self, *args): #cannot find CLR method
        """ WriteEntitiesDescriptor(self: MetadataSerializer, inputWriter: XmlWriter, entitiesDescriptor: EntitiesDescriptor) """
        ...

    def WriteEntityDescriptor(self, *args): #cannot find CLR method
        """ WriteEntityDescriptor(self: MetadataSerializer, inputWriter: XmlWriter, entityDescriptor: EntityDescriptor) """
        ...

    def WriteIdentityProviderSingleSignOnDescriptor(self, *args): #cannot find CLR method
        """ WriteIdentityProviderSingleSignOnDescriptor(self: MetadataSerializer, writer: XmlWriter, identityProviderSingleSignOnDescriptor: IdentityProviderSingleSignOnDescriptor) """
        ...

    def WriteIndexedProtocolEndpoint(self, *args): #cannot find CLR method
        """ WriteIndexedProtocolEndpoint(self: MetadataSerializer, writer: XmlWriter, indexedEP: IndexedProtocolEndpoint, element: XmlQualifiedName) """
        ...

    def WriteKeyDescriptor(self, *args): #cannot find CLR method
        """ WriteKeyDescriptor(self: MetadataSerializer, writer: XmlWriter, keyDescriptor: KeyDescriptor) """
        ...

    def WriteLocalizedName(self, *args): #cannot find CLR method
        """ WriteLocalizedName(self: MetadataSerializer, writer: XmlWriter, name: LocalizedName, element: XmlQualifiedName) """
        ...

    def WriteLocalizedUri(self, *args): #cannot find CLR method
        """ WriteLocalizedUri(self: MetadataSerializer, writer: XmlWriter, uri: LocalizedUri, element: XmlQualifiedName) """
        ...

    def WriteMetadata(self, *__args): # -> 
        """ WriteMetadata(self: MetadataSerializer, stream: Stream, metadata: MetadataBase)WriteMetadata(self: MetadataSerializer, writer: XmlWriter, metadata: MetadataBase) """
        ...

    def WriteMetadataCore(self, *args): #cannot find CLR method
        """ WriteMetadataCore(self: MetadataSerializer, writer: XmlWriter, metadataBase: MetadataBase) """
        ...

    def WriteOrganization(self, *args): #cannot find CLR method
        """ WriteOrganization(self: MetadataSerializer, writer: XmlWriter, organization: Organization) """
        ...

    def WriteProtocolEndpoint(self, *args): #cannot find CLR method
        """ WriteProtocolEndpoint(self: MetadataSerializer, writer: XmlWriter, endpoint: ProtocolEndpoint, element: XmlQualifiedName) """
        ...

    def WriteRoleDescriptorAttributes(self, *args): #cannot find CLR method
        """ WriteRoleDescriptorAttributes(self: MetadataSerializer, writer: XmlWriter, roleDescriptor: RoleDescriptor) """
        ...

    def WriteRoleDescriptorElements(self, *args): #cannot find CLR method
        """ WriteRoleDescriptorElements(self: MetadataSerializer, writer: XmlWriter, roleDescriptor: RoleDescriptor) """
        ...

    def WriteSecurityTokenServiceDescriptor(self, *args): #cannot find CLR method
        """ WriteSecurityTokenServiceDescriptor(self: MetadataSerializer, writer: XmlWriter, securityTokenServiceDescriptor: SecurityTokenServiceDescriptor) """
        ...

    def WriteServiceProviderSingleSignOnDescriptor(self, *args): #cannot find CLR method
        """ WriteServiceProviderSingleSignOnDescriptor(self: MetadataSerializer, writer: XmlWriter, serviceProviderSingleSignOnDescriptor: ServiceProviderSingleSignOnDescriptor) """
        ...

    def WriteSingleSignOnDescriptorAttributes(self, *args): #cannot find CLR method
        """ WriteSingleSignOnDescriptorAttributes(self: MetadataSerializer, writer: XmlWriter, singleSignOnDescriptor: SingleSignOnDescriptor) """
        ...

    def WriteSingleSignOnDescriptorElements(self, *args): #cannot find CLR method
        """ WriteSingleSignOnDescriptorElements(self: MetadataSerializer, writer: XmlWriter, singleSignOnDescriptor: SingleSignOnDescriptor) """
        ...

    def WriteWebServiceDescriptorAttributes(self, *args): #cannot find CLR method
        """ WriteWebServiceDescriptorAttributes(self: MetadataSerializer, writer: XmlWriter, wsDescriptor: WebServiceDescriptor) """
        ...

    def WriteWebServiceDescriptorElements(self, *args): #cannot find CLR method
        """ WriteWebServiceDescriptorElements(self: MetadataSerializer, writer: XmlWriter, wsDescriptor: WebServiceDescriptor) """
        ...

    LanguageAttribute: str = ...
    LanguageLocalName: str = ...
    LanguageNamespaceUri: str = ...
    LanguagePrefix: str = ...


class Organization: # skipped bases: <type 'object'>, <type 'object'>
    """
    Organization()
    Organization(names: LocalizedEntryCollection[LocalizedName], displayNames: LocalizedEntryCollection[LocalizedName], urls: LocalizedEntryCollection[LocalizedUri])
    """
    @property
    def DisplayNames(self) -> LocalizedEntryCollection:
        """ Get: DisplayNames(self: Organization) -> LocalizedEntryCollection[LocalizedName] """
        ...

    @property
    def Names(self) -> LocalizedEntryCollection:
        """ Get: Names(self: Organization) -> LocalizedEntryCollection[LocalizedName] """
        ...

    @property
    def Urls(self) -> LocalizedEntryCollection:
        """ Get: Urls(self: Organization) -> LocalizedEntryCollection[LocalizedUri] """
        ...



class SecurityTokenServiceDescriptor(WebServiceDescriptor): # skipped bases: <type 'object'>
    """ SecurityTokenServiceDescriptor() """
    @property
    def PassiveRequestorEndpoints(self) -> Collection:
        """ Get: PassiveRequestorEndpoints(self: SecurityTokenServiceDescriptor) -> Collection[EndpointReference] """
        ...

    @property
    def SecurityTokenServiceEndpoints(self) -> Collection:
        """ Get: SecurityTokenServiceEndpoints(self: SecurityTokenServiceDescriptor) -> Collection[EndpointReference] """
        ...



class ServiceProviderSingleSignOnDescriptor(SingleSignOnDescriptor): # skipped bases: <type 'object'>
    """
    ServiceProviderSingleSignOnDescriptor()
    ServiceProviderSingleSignOnDescriptor(collection: IndexedProtocolEndpointDictionary)
    """
    @property
    def AssertionConsumerServices(self) -> IndexedProtocolEndpointDictionary:
        """ Get: AssertionConsumerServices(self: ServiceProviderSingleSignOnDescriptor) -> IndexedProtocolEndpointDictionary """
        ...

    @property
    def AuthenticationRequestsSigned(self) -> bool:
        """
        Get: AuthenticationRequestsSigned(self: ServiceProviderSingleSignOnDescriptor) -> bool
        Set: AuthenticationRequestsSigned(self: ServiceProviderSingleSignOnDescriptor) = value
        """
        ...

    @property
    def WantAssertionsSigned(self) -> bool:
        """
        Get: WantAssertionsSigned(self: ServiceProviderSingleSignOnDescriptor) -> bool
        Set: WantAssertionsSigned(self: ServiceProviderSingleSignOnDescriptor) = value
        """
        ...


    def __new__(cls, collection:IndexedProtocolEndpointDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, collection: IndexedProtocolEndpointDictionary)
        """
        ...


