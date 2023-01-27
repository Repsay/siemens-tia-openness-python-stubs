# encoding: utf-8
# module System.IdentityModel.Claims calls itself Claims
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, IDisposable, Uri

from System.Collections import IEnumerable, IEqualityComparer

from System.Net.Mail import MailAddress

from System.Security.Cryptography import RSA

from System.Security.Cryptography.X509Certificates import (
    X500DistinguishedName, X509Certificate2)

from System.Security.Principal import SecurityIdentifier, WindowsIdentity

from typing import Self

"""The following names are not found in the module: IIdentityInfo
"""

# no functions
# classes

class Claim: # skipped bases: <type 'object'>, <type 'object'>
    """ Claim(claimType: str, resource: object, right: str) """
    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType(self: Claim) -> str """
        ...

    @property
    def DefaultComparer(self) -> IEqualityComparer:
        """ Get: DefaultComparer() -> IEqualityComparer[Claim] """
        ...

    @property
    def Resource(self) -> object:
        """ Get: Resource(self: Claim) -> object """
        ...

    @property
    def Right(self) -> str:
        """ Get: Right(self: Claim) -> str """
        ...

    @property
    def System(self) -> Claim:
        """ Get: System() -> Claim """
        ...


    @staticmethod
    def CreateDenyOnlyWindowsSidClaim(sid:SecurityIdentifier) -> Claim:
        """ CreateDenyOnlyWindowsSidClaim(sid: SecurityIdentifier) -> Claim """
        ...

    @staticmethod
    def CreateDnsClaim(dns:str) -> Claim:
        """ CreateDnsClaim(dns: str) -> Claim """
        ...

    @staticmethod
    def CreateHashClaim(hash:Array) -> Claim:
        """ CreateHashClaim(hash: Array[Byte]) -> Claim """
        ...

    @staticmethod
    def CreateMailAddressClaim(mailAddress:MailAddress) -> Claim:
        """ CreateMailAddressClaim(mailAddress: MailAddress) -> Claim """
        ...

    @staticmethod
    def CreateNameClaim(name:str) -> Claim:
        """ CreateNameClaim(name: str) -> Claim """
        ...

    @staticmethod
    def CreateRsaClaim(rsa:RSA) -> Claim:
        """ CreateRsaClaim(rsa: RSA) -> Claim """
        ...

    @staticmethod
    def CreateSpnClaim(spn:str) -> Claim:
        """ CreateSpnClaim(spn: str) -> Claim """
        ...

    @staticmethod
    def CreateThumbprintClaim(thumbprint:Array) -> Claim:
        """ CreateThumbprintClaim(thumbprint: Array[Byte]) -> Claim """
        ...

    @staticmethod
    def CreateUpnClaim(upn:str) -> Claim:
        """ CreateUpnClaim(upn: str) -> Claim """
        ...

    @staticmethod
    def CreateUriClaim(uri:Uri) -> Claim:
        """ CreateUriClaim(uri: Uri) -> Claim """
        ...

    @staticmethod
    def CreateWindowsSidClaim(sid:SecurityIdentifier) -> Claim:
        """ CreateWindowsSidClaim(sid: SecurityIdentifier) -> Claim """
        ...

    @staticmethod
    def CreateX500DistinguishedNameClaim(x500DistinguishedName:X500DistinguishedName) -> Claim:
        """ CreateX500DistinguishedNameClaim(x500DistinguishedName: X500DistinguishedName) -> Claim """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Claim, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Claim) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Claim) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class ClaimSet(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ClaimSet) -> int """
        ...

    @property
    def Issuer(self) -> ClaimSet:
        """ Get: Issuer(self: ClaimSet) -> ClaimSet """
        ...

    @property
    def System(self) -> ClaimSet:
        """ Get: System() -> ClaimSet """
        ...

    @property
    def Windows(self) -> ClaimSet:
        """ Get: Windows() -> ClaimSet """
        ...


    def ContainsClaim(self, claim:Claim, comparer:IEqualityComparer = ...) -> bool:
        """
        ContainsClaim(self: ClaimSet, claim: Claim, comparer: IEqualityComparer[Claim]) -> bool
        ContainsClaim(self: ClaimSet, claim: Claim) -> bool
        """
        ...

    def FindClaims(self, claimType:str, right:str) -> IEnumerable:
        """ FindClaims(self: ClaimSet, claimType: str, right: str) -> IEnumerable[Claim] """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Claim](enumerable: IEnumerable[Claim], value: Claim) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...



class ClaimTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Anonymous(self) -> str:
        """ Get: Anonymous() -> str """
        ...

    @property
    def Authentication(self) -> str:
        """ Get: Authentication() -> str """
        ...

    @property
    def AuthorizationDecision(self) -> str:
        """ Get: AuthorizationDecision() -> str """
        ...

    @property
    def Country(self) -> str:
        """ Get: Country() -> str """
        ...

    @property
    def DateOfBirth(self) -> str:
        """ Get: DateOfBirth() -> str """
        ...

    @property
    def DenyOnlySid(self) -> str:
        """ Get: DenyOnlySid() -> str """
        ...

    @property
    def Dns(self) -> str:
        """ Get: Dns() -> str """
        ...

    @property
    def Email(self) -> str:
        """ Get: Email() -> str """
        ...

    @property
    def Gender(self) -> str:
        """ Get: Gender() -> str """
        ...

    @property
    def GivenName(self) -> str:
        """ Get: GivenName() -> str """
        ...

    @property
    def Hash(self) -> str:
        """ Get: Hash() -> str """
        ...

    @property
    def HomePhone(self) -> str:
        """ Get: HomePhone() -> str """
        ...

    @property
    def Locality(self) -> str:
        """ Get: Locality() -> str """
        ...

    @property
    def MobilePhone(self) -> str:
        """ Get: MobilePhone() -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name() -> str """
        ...

    @property
    def NameIdentifier(self) -> str:
        """ Get: NameIdentifier() -> str """
        ...

    @property
    def OtherPhone(self) -> str:
        """ Get: OtherPhone() -> str """
        ...

    @property
    def PostalCode(self) -> str:
        """ Get: PostalCode() -> str """
        ...

    @property
    def PPID(self) -> str:
        """ Get: PPID() -> str """
        ...

    @property
    def Rsa(self) -> str:
        """ Get: Rsa() -> str """
        ...

    @property
    def Sid(self) -> str:
        """ Get: Sid() -> str """
        ...

    @property
    def Spn(self) -> str:
        """ Get: Spn() -> str """
        ...

    @property
    def StateOrProvince(self) -> str:
        """ Get: StateOrProvince() -> str """
        ...

    @property
    def StreetAddress(self) -> str:
        """ Get: StreetAddress() -> str """
        ...

    @property
    def Surname(self) -> str:
        """ Get: Surname() -> str """
        ...

    @property
    def System(self) -> str:
        """ Get: System() -> str """
        ...

    @property
    def Thumbprint(self) -> str:
        """ Get: Thumbprint() -> str """
        ...

    @property
    def Upn(self) -> str:
        """ Get: Upn() -> str """
        ...

    @property
    def Uri(self) -> str:
        """ Get: Uri() -> str """
        ...

    @property
    def Webpage(self) -> str:
        """ Get: Webpage() -> str """
        ...

    @property
    def X500DistinguishedName(self) -> str:
        """ Get: X500DistinguishedName() -> str """
        ...


    __all__: list = ...


class DefaultClaimSet(ClaimSet): # skipped bases: <type 'IEnumerable[Claim]'>, <type 'IEnumerable'>, <type 'object'>
    """
    DefaultClaimSet(*claims: Array[Claim])
    DefaultClaimSet(claims: IList[Claim])
    DefaultClaimSet(issuer: ClaimSet, *claims: Array[Claim])
    DefaultClaimSet(issuer: ClaimSet, claims: IList[Claim])
    """
    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: DefaultClaimSet, issuer: ClaimSet, claims: IList[Claim]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DefaultClaimSet) -> str """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type, *claims: Array[Claim])
        __new__(cls: type, claims: IList[Claim])
        __new__(cls: type, issuer: ClaimSet, *claims: Array[Claim])
        __new__(cls: type, issuer: ClaimSet, claims: IList[Claim])
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class Rights: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Identity(self) -> str:
        """ Get: Identity() -> str """
        ...

    @property
    def PossessProperty(self) -> str:
        """ Get: PossessProperty() -> str """
        ...


    __all__: list = ...


class WindowsClaimSet(IDisposable, ClaimSet, IIdentityInfo): # skipped bases: <type 'IEnumerable[Claim]'>, <type 'IEnumerable'>, <type 'object'>
    """
    WindowsClaimSet(windowsIdentity: WindowsIdentity)
    WindowsClaimSet(windowsIdentity: WindowsIdentity, includeWindowsGroups: bool)
    WindowsClaimSet(windowsIdentity: WindowsIdentity, expirationTime: DateTime)
    WindowsClaimSet(windowsIdentity: WindowsIdentity, includeWindowsGroups: bool, expirationTime: DateTime)
    WindowsClaimSet(windowsIdentity: WindowsIdentity, authenticationType: str, includeWindowsGroups: bool, expirationTime: DateTime)
    """
    @property
    def ExpirationTime(self) -> DateTime:
        """ Get: ExpirationTime(self: WindowsClaimSet) -> DateTime """
        ...

    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity(self: WindowsClaimSet) -> WindowsIdentity """
        ...


    def ToString(self) -> str:
        """ ToString(self: WindowsClaimSet) -> str """
        ...

    def __new__(cls, windowsIdentity:WindowsIdentity, *__args:bool) -> Self:
        """
        __new__(cls: type, windowsIdentity: WindowsIdentity)
        __new__(cls: type, windowsIdentity: WindowsIdentity, includeWindowsGroups: bool)
        __new__(cls: type, windowsIdentity: WindowsIdentity, expirationTime: DateTime)
        __new__(cls: type, windowsIdentity: WindowsIdentity, includeWindowsGroups: bool, expirationTime: DateTime)
        __new__(cls: type, windowsIdentity: WindowsIdentity, authenticationType: str, includeWindowsGroups: bool, expirationTime: DateTime)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class X509CertificateClaimSet(IDisposable, ClaimSet, IIdentityInfo): # skipped bases: <type 'IEnumerable[Claim]'>, <type 'IEnumerable'>, <type 'object'>
    """ X509CertificateClaimSet(certificate: X509Certificate2) """
    @property
    def ExpirationTime(self) -> DateTime:
        """ Get: ExpirationTime(self: X509CertificateClaimSet) -> DateTime """
        ...

    @property
    def X509Certificate(self) -> X509Certificate2:
        """ Get: X509Certificate(self: X509CertificateClaimSet) -> X509Certificate2 """
        ...


    def ToString(self) -> str:
        """ ToString(self: X509CertificateClaimSet) -> str """
        ...

    def __new__(cls, certificate:X509Certificate2) -> Self:
        """ __new__(cls: type, certificate: X509Certificate2) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


