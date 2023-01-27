# encoding: utf-8
# module System.Security.Claims calls itself Claims
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Nullable, Predicate

from System.Collections import IDictionary, IEnumerable

from System.IdentityModel.Configuration import ICustomIdentityConfiguration

from System.IdentityModel.Policy import AuthorizationContext

from System.IO import BinaryWriter

from System.Security.Principal import IIdentity, IPrincipal

"""The following names are not found in the module: (Func, 
    Func, ClaimsIdentity])
"""

# no functions
# classes

class AuthenticationInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthenticationInformation() """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: AuthenticationInformation) -> str
        Set: Address(self: AuthenticationInformation) = value
        """
        ...

    @property
    def AuthorizationContexts(self) -> Collection:
        """ Get: AuthorizationContexts(self: AuthenticationInformation) -> Collection[AuthenticationContext] """
        ...

    @property
    def DnsName(self) -> str:
        """
        Get: DnsName(self: AuthenticationInformation) -> str
        Set: DnsName(self: AuthenticationInformation) = value
        """
        ...

    @property
    def NotOnOrAfter(self) -> Nullable:
        """
        Get: NotOnOrAfter(self: AuthenticationInformation) -> Nullable[DateTime]
        Set: NotOnOrAfter(self: AuthenticationInformation) = value
        """
        ...

    @property
    def Session(self) -> str:
        """
        Get: Session(self: AuthenticationInformation) -> str
        Set: Session(self: AuthenticationInformation) = value
        """
        ...



class AuthenticationTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Basic: str = ...
    Federation: str = ...
    Kerberos: str = ...
    Negotiate: str = ...
    Password: str = ...
    Signature: str = ...
    Windows: str = ...
    X509: str = ...
    __all__: list = ...


class AuthorizationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    AuthorizationContext(principal: ClaimsPrincipal, resource: str, action: str)
    AuthorizationContext(principal: ClaimsPrincipal, resource: Collection[Claim], action: Collection[Claim])
    """
    @property
    def Action(self) -> Collection:
        """ Get: Action(self: AuthorizationContext) -> Collection[Claim] """
        ...

    @property
    def Principal(self) -> ClaimsPrincipal:
        """ Get: Principal(self: AuthorizationContext) -> ClaimsPrincipal """
        ...

    @property
    def Resource(self) -> Collection:
        """ Get: Resource(self: AuthorizationContext) -> Collection[Claim] """
        ...



class Claim: # skipped bases: <type 'object'>, <type 'object'>
    """
    Claim(reader: BinaryReader)
    Claim(reader: BinaryReader, subject: ClaimsIdentity)
    Claim(type: str, value: str)
    Claim(type: str, value: str, valueType: str)
    Claim(type: str, value: str, valueType: str, issuer: str)
    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str)
    Claim(type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity)
    """
    @property
    def CustomSerializationData(self):
        ...

    @property
    def Issuer(self) -> str:
        """ Get: Issuer(self: Claim) -> str """
        ...

    @property
    def OriginalIssuer(self) -> str:
        """ Get: OriginalIssuer(self: Claim) -> str """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: Claim) -> IDictionary[str, str] """
        ...

    @property
    def Subject(self) -> ClaimsIdentity:
        """ Get: Subject(self: Claim) -> ClaimsIdentity """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: Claim) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: Claim) -> str """
        ...

    @property
    def ValueType(self) -> str:
        """ Get: ValueType(self: Claim) -> str """
        ...


    def Clone(self, identity:ClaimsIdentity = ...) -> Claim:
        """
        Clone(self: Claim) -> Claim
        Clone(self: Claim, identity: ClaimsIdentity) -> Claim
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: Claim) -> str """
        ...

    def WriteTo(self, writer:BinaryWriter): # -> 
        """ WriteTo(self: Claim, writer: BinaryWriter) """
        ...


class ClaimProperties: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Namespace: str = ...
    SamlAttributeDisplayName: str = ...
    SamlAttributeNameFormat: str = ...
    SamlNameIdentifierFormat: str = ...
    SamlNameIdentifierNameQualifier: str = ...
    SamlNameIdentifierSPNameQualifier: str = ...
    SamlNameIdentifierSPProvidedId: str = ...
    __all__: list = ...


class ClaimsAuthenticationManager(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ ClaimsAuthenticationManager() """
    def Authenticate(self, resourceName:str, incomingPrincipal:ClaimsPrincipal) -> ClaimsPrincipal:
        """ Authenticate(self: ClaimsAuthenticationManager, resourceName: str, incomingPrincipal: ClaimsPrincipal) -> ClaimsPrincipal """
        ...


class ClaimsAuthorizationManager(ICustomIdentityConfiguration): # skipped bases: <type 'object'>
    """ ClaimsAuthorizationManager() """
    def CheckAccess(self, context:AuthorizationContext) -> bool:
        """ CheckAccess(self: ClaimsAuthorizationManager, context: AuthorizationContext) -> bool """
        ...


class ClaimsIdentity(IIdentity): # skipped bases: <type 'object'>
    """
    ClaimsIdentity()
    ClaimsIdentity(identity: IIdentity)
    ClaimsIdentity(claims: IEnumerable[Claim])
    ClaimsIdentity(authenticationType: str)
    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str)
    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim])
    ClaimsIdentity(authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(identity: IIdentity, claims: IEnumerable[Claim], authenticationType: str, nameType: str, roleType: str)
    ClaimsIdentity(reader: BinaryReader)
    """
    @property
    def Actor(self) -> ClaimsIdentity:
        """
        Get: Actor(self: ClaimsIdentity) -> ClaimsIdentity
        Set: Actor(self: ClaimsIdentity) = value
        """
        ...

    @property
    def BootstrapContext(self) -> object:
        """
        Get: BootstrapContext(self: ClaimsIdentity) -> object
        Set: BootstrapContext(self: ClaimsIdentity) = value
        """
        ...

    @property
    def Claims(self) -> IEnumerable:
        """ Get: Claims(self: ClaimsIdentity) -> IEnumerable[Claim] """
        ...

    @property
    def CustomSerializationData(self):
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: ClaimsIdentity) -> str
        Set: Label(self: ClaimsIdentity) = value
        """
        ...

    @property
    def NameClaimType(self) -> str:
        """ Get: NameClaimType(self: ClaimsIdentity) -> str """
        ...

    @property
    def RoleClaimType(self) -> str:
        """ Get: RoleClaimType(self: ClaimsIdentity) -> str """
        ...


    def AddClaim(self, claim:Claim): # -> 
        """ AddClaim(self: ClaimsIdentity, claim: Claim) """
        ...

    def AddClaims(self, claims:IEnumerable): # -> 
        """ AddClaims(self: ClaimsIdentity, claims: IEnumerable[Claim]) """
        ...

    def Clone(self) -> ClaimsIdentity:
        """ Clone(self: ClaimsIdentity) -> ClaimsIdentity """
        ...

    def CreateClaim(self, *args): #cannot find CLR method
        """ CreateClaim(self: ClaimsIdentity, reader: BinaryReader) -> Claim """
        ...

    def FindAll(self, *__args:Predicate) -> IEnumerable:
        """
        FindAll(self: ClaimsIdentity, match: Predicate[Claim]) -> IEnumerable[Claim]
        FindAll(self: ClaimsIdentity, type: str) -> IEnumerable[Claim]
        """
        ...

    def FindFirst(self, *__args:Predicate) -> Claim:
        """
        FindFirst(self: ClaimsIdentity, match: Predicate[Claim]) -> Claim
        FindFirst(self: ClaimsIdentity, type: str) -> Claim
        """
        ...

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: ClaimsIdentity, info: SerializationInfo, context: StreamingContext) """
        ...

    def HasClaim(self, *__args:Predicate) -> bool:
        """
        HasClaim(self: ClaimsIdentity, match: Predicate[Claim]) -> bool
        HasClaim(self: ClaimsIdentity, type: str, value: str) -> bool
        """
        ...

    def RemoveClaim(self, claim:Claim): # -> 
        """ RemoveClaim(self: ClaimsIdentity, claim: Claim) """
        ...

    def TryRemoveClaim(self, claim:Claim) -> bool:
        """ TryRemoveClaim(self: ClaimsIdentity, claim: Claim) -> bool """
        ...

    def WriteTo(self, writer:BinaryWriter): # -> 
        """ WriteTo(self: ClaimsIdentity, writer: BinaryWriter) """
        ...

    DefaultIssuer: str = ...
    DefaultNameClaimType: str = ...
    DefaultRoleClaimType: str = ...


class ClaimsPrincipal(IPrincipal): # skipped bases: <type 'object'>
    """
    ClaimsPrincipal()
    ClaimsPrincipal(identities: IEnumerable[ClaimsIdentity])
    ClaimsPrincipal(identity: IIdentity)
    ClaimsPrincipal(principal: IPrincipal)
    ClaimsPrincipal(reader: BinaryReader)
    """
    @property
    def Claims(self) -> IEnumerable:
        """ Get: Claims(self: ClaimsPrincipal) -> IEnumerable[Claim] """
        ...

    @property
    def ClaimsPrincipalSelector(self): # -> Func
        """
        Get: ClaimsPrincipalSelector() -> Func[ClaimsPrincipal]
        Set: ClaimsPrincipalSelector() = value
        """
        ...

    @property
    def Current(self) -> ClaimsPrincipal:
        """ Get: Current() -> ClaimsPrincipal """
        ...

    @property
    def CustomSerializationData(self):
        ...

    @property
    def Identities(self) -> IEnumerable:
        """ Get: Identities(self: ClaimsPrincipal) -> IEnumerable[ClaimsIdentity] """
        ...

    @property
    def PrimaryIdentitySelector(self): # -> Func, ClaimsIdentity]
        """
        Get: PrimaryIdentitySelector() -> Func[IEnumerable[ClaimsIdentity], ClaimsIdentity]
        Set: PrimaryIdentitySelector() = value
        """
        ...


    def AddIdentities(self, identities:IEnumerable): # -> 
        """ AddIdentities(self: ClaimsPrincipal, identities: IEnumerable[ClaimsIdentity]) """
        ...

    def AddIdentity(self, identity:ClaimsIdentity): # -> 
        """ AddIdentity(self: ClaimsPrincipal, identity: ClaimsIdentity) """
        ...

    def Clone(self) -> ClaimsPrincipal:
        """ Clone(self: ClaimsPrincipal) -> ClaimsPrincipal """
        ...

    def CreateClaimsIdentity(self, *args): #cannot find CLR method
        """ CreateClaimsIdentity(self: ClaimsPrincipal, reader: BinaryReader) -> ClaimsIdentity """
        ...

    def FindAll(self, *__args:Predicate) -> IEnumerable:
        """
        FindAll(self: ClaimsPrincipal, match: Predicate[Claim]) -> IEnumerable[Claim]
        FindAll(self: ClaimsPrincipal, type: str) -> IEnumerable[Claim]
        """
        ...

    def FindFirst(self, *__args:Predicate) -> Claim:
        """
        FindFirst(self: ClaimsPrincipal, match: Predicate[Claim]) -> Claim
        FindFirst(self: ClaimsPrincipal, type: str) -> Claim
        """
        ...

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: ClaimsPrincipal, info: SerializationInfo, context: StreamingContext) """
        ...

    def HasClaim(self, *__args:Predicate) -> bool:
        """
        HasClaim(self: ClaimsPrincipal, match: Predicate[Claim]) -> bool
        HasClaim(self: ClaimsPrincipal, type: str, value: str) -> bool
        """
        ...

    def WriteTo(self, writer:BinaryWriter): # -> 
        """ WriteTo(self: ClaimsPrincipal, writer: BinaryWriter) """
        ...



class ClaimTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Actor: str = ...
    Anonymous: str = ...
    Authentication: str = ...
    AuthenticationInstant: str = ...
    AuthenticationMethod: str = ...
    AuthorizationDecision: str = ...
    CookiePath: str = ...
    Country: str = ...
    DateOfBirth: str = ...
    DenyOnlyPrimaryGroupSid: str = ...
    DenyOnlyPrimarySid: str = ...
    DenyOnlySid: str = ...
    DenyOnlyWindowsDeviceGroup: str = ...
    Dns: str = ...
    Dsa: str = ...
    Email: str = ...
    Expiration: str = ...
    Expired: str = ...
    Gender: str = ...
    GivenName: str = ...
    GroupSid: str = ...
    Hash: str = ...
    HomePhone: str = ...
    IsPersistent: str = ...
    Locality: str = ...
    MobilePhone: str = ...
    Name: str = ...
    NameIdentifier: str = ...
    OtherPhone: str = ...
    PostalCode: str = ...
    PrimaryGroupSid: str = ...
    PrimarySid: str = ...
    Role: str = ...
    Rsa: str = ...
    SerialNumber: str = ...
    Sid: str = ...
    Spn: str = ...
    StateOrProvince: str = ...
    StreetAddress: str = ...
    Surname: str = ...
    System: str = ...
    Thumbprint: str = ...
    Upn: str = ...
    Uri: str = ...
    UserData: str = ...
    Version: str = ...
    Webpage: str = ...
    WindowsAccountName: str = ...
    WindowsDeviceClaim: str = ...
    WindowsDeviceGroup: str = ...
    WindowsFqbnVersion: str = ...
    WindowsSubAuthority: str = ...
    WindowsUserClaim: str = ...
    X500DistinguishedName: str = ...
    __all__: list = ...


class ClaimValueTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Base64Binary: str = ...
    Base64Octet: str = ...
    Boolean: str = ...
    Date: str = ...
    DateTime: str = ...
    DaytimeDuration: str = ...
    DnsName: str = ...
    Double: str = ...
    DsaKeyValue: str = ...
    Email: str = ...
    Fqbn: str = ...
    HexBinary: str = ...
    Integer: str = ...
    Integer32: str = ...
    Integer64: str = ...
    KeyInfo: str = ...
    Rfc822Name: str = ...
    Rsa: str = ...
    RsaKeyValue: str = ...
    Sid: str = ...
    String: str = ...
    Time: str = ...
    UInteger32: str = ...
    UInteger64: str = ...
    UpnName: str = ...
    X500Name: str = ...
    YearMonthDuration: str = ...
    __all__: list = ...


class DynamicRoleClaimProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity:ClaimsIdentity, claims:IEnumerable): # -> 
        """ AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: IEnumerable[Claim]) """
        ...

    __all__: list = ...


