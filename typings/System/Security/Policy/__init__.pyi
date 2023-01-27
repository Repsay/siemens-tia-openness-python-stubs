# encoding: utf-8
# module System.Security.Policy calls itself Policy
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (ActivationContext, ApplicationId, ApplicationIdentity, 
    Array, Enum, SystemException, Type, Version)

from System.Collections import ICollection, IEnumerator, IList

from System.Messaging import HashAlgorithm

from System.Reflection import Assembly

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)

from System.Security import (IPermission, ISecurityEncodable, 
    ISecurityPolicyEncodable, NamedPermissionSet, PermissionSet, 
    PolicyLevelType, SecurityElement, SecurityZone)

from System.Security.Cryptography.X509Certificates import X509Certificate

from System.Security.Permissions import StrongNamePublicKeyBlob

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IConstantMembershipCondition, IDelayEvaluatedEvidence, 
    IReportMatchMembershipCondition, IUnionSemanticCodeGroup, T, field#)
"""

# no functions
# classes

class IMembershipCondition(ISecurityPolicyEncodable, ISecurityEncodable): # skipped bases: <type 'object'>
    """ no doc """
    def Check(self, evidence:Evidence) -> bool:
        """ Check(self: IMembershipCondition, evidence: Evidence) -> bool """
        ...

    def Copy(self) -> IMembershipCondition:
        """ Copy(self: IMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: IMembershipCondition, obj: object) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: IMembershipCondition) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class AllMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ AllMembershipCondition() """
    def Copy(self) -> IMembershipCondition:
        """ Copy(self: AllMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: AllMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: AllMembershipCondition, e: SecurityElement, level: PolicyLevel)FromXml(self: AllMembershipCondition, e: SecurityElement) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AllMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: AllMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: AllMembershipCondition, level: PolicyLevel) -> SecurityElement
        ToXml(self: AllMembershipCondition) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EvidenceBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clone(self) -> EvidenceBase:
        """ Clone(self: EvidenceBase) -> EvidenceBase """
        ...


class ApplicationDirectory(EvidenceBase): # skipped bases: <type 'object'>
    """ ApplicationDirectory(name: str) """
    @property
    def Directory(self) -> str:
        """ Get: Directory(self: ApplicationDirectory) -> str """
        ...


    def Copy(self) -> object:
        """ Copy(self: ApplicationDirectory) -> object """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: ApplicationDirectory, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ApplicationDirectory) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ApplicationDirectory) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ApplicationDirectoryMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ ApplicationDirectoryMembershipCondition() """
    def Copy(self) -> IMembershipCondition:
        """ Copy(self: ApplicationDirectoryMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: ApplicationDirectoryMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: ApplicationDirectoryMembershipCondition, e: SecurityElement)FromXml(self: ApplicationDirectoryMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ApplicationDirectoryMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ApplicationDirectoryMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: ApplicationDirectoryMembershipCondition) -> SecurityElement
        ToXml(self: ApplicationDirectoryMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ApplicationSecurityInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ApplicationSecurityInfo(activationContext: ActivationContext) """
    @property
    def ApplicationEvidence(self) -> Evidence:
        """
        Get: ApplicationEvidence(self: ApplicationSecurityInfo) -> Evidence
        Set: ApplicationEvidence(self: ApplicationSecurityInfo) = value
        """
        ...

    @property
    def ApplicationId(self) -> ApplicationId:
        """
        Get: ApplicationId(self: ApplicationSecurityInfo) -> ApplicationId
        Set: ApplicationId(self: ApplicationSecurityInfo) = value
        """
        ...

    @property
    def DefaultRequestSet(self) -> PermissionSet:
        """
        Get: DefaultRequestSet(self: ApplicationSecurityInfo) -> PermissionSet
        Set: DefaultRequestSet(self: ApplicationSecurityInfo) = value
        """
        ...

    @property
    def DeploymentId(self) -> ApplicationId:
        """
        Get: DeploymentId(self: ApplicationSecurityInfo) -> ApplicationId
        Set: DeploymentId(self: ApplicationSecurityInfo) = value
        """
        ...



class ApplicationSecurityManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationTrustManager(self) -> IApplicationTrustManager:
        """ Get: ApplicationTrustManager() -> IApplicationTrustManager """
        ...

    @property
    def UserApplicationTrusts(self) -> ApplicationTrustCollection:
        """ Get: UserApplicationTrusts() -> ApplicationTrustCollection """
        ...


    @staticmethod
    def DetermineApplicationTrust(activationContext:ActivationContext, context:TrustManagerContext) -> bool:
        """ DetermineApplicationTrust(activationContext: ActivationContext, context: TrustManagerContext) -> bool """
        ...

    __all__: list = ...


class ApplicationTrust(EvidenceBase, ISecurityEncodable): # skipped bases: <type 'object'>
    """
    ApplicationTrust(applicationIdentity: ApplicationIdentity)
    ApplicationTrust()
    ApplicationTrust(defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName])
    """
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """
        Get: ApplicationIdentity(self: ApplicationTrust) -> ApplicationIdentity
        Set: ApplicationIdentity(self: ApplicationTrust) = value
        """
        ...

    @property
    def DefaultGrantSet(self) -> PolicyStatement:
        """
        Get: DefaultGrantSet(self: ApplicationTrust) -> PolicyStatement
        Set: DefaultGrantSet(self: ApplicationTrust) = value
        """
        ...

    @property
    def ExtraInfo(self) -> object:
        """
        Get: ExtraInfo(self: ApplicationTrust) -> object
        Set: ExtraInfo(self: ApplicationTrust) = value
        """
        ...

    @property
    def FullTrustAssemblies(self) -> IList:
        """ Get: FullTrustAssemblies(self: ApplicationTrust) -> IList[StrongName] """
        ...

    @property
    def IsApplicationTrustedToRun(self) -> bool:
        """
        Get: IsApplicationTrustedToRun(self: ApplicationTrust) -> bool
        Set: IsApplicationTrustedToRun(self: ApplicationTrust) = value
        """
        ...

    @property
    def Persist(self) -> bool:
        """
        Get: Persist(self: ApplicationTrust) -> bool
        Set: Persist(self: ApplicationTrust) = value
        """
        ...


    def __new__(cls, *__args:ApplicationIdentity) -> Self:
        """
        __new__(cls: type, applicationIdentity: ApplicationIdentity)
        __new__(cls: type)
        __new__(cls: type, defaultGrantSet: PermissionSet, fullTrustAssemblies: IEnumerable[StrongName])
        """
        ...


class ApplicationTrustCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, trust:ApplicationTrust) -> int:
        """ Add(self: ApplicationTrustCollection, trust: ApplicationTrust) -> int """
        ...

    def AddRange(self, trusts:Array): # -> 
        """ AddRange(self: ApplicationTrustCollection, trusts: Array[ApplicationTrust])AddRange(self: ApplicationTrustCollection, trusts: ApplicationTrustCollection) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ApplicationTrustCollection) """
        ...

    def Find(self, applicationIdentity:ApplicationIdentity, versionMatch:ApplicationVersionMatch) -> ApplicationTrustCollection:
        """ Find(self: ApplicationTrustCollection, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection """
        ...

    def GetEnumerator(self) -> ApplicationTrustEnumerator:
        """ GetEnumerator(self: ApplicationTrustCollection) -> ApplicationTrustEnumerator """
        ...

    def Remove(self, *__args:ApplicationTrust): # -> 
        """ Remove(self: ApplicationTrustCollection, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch)Remove(self: ApplicationTrustCollection, trust: ApplicationTrust) """
        ...

    def RemoveRange(self, trusts:Array): # -> 
        """ RemoveRange(self: ApplicationTrustCollection, trusts: Array[ApplicationTrust])RemoveRange(self: ApplicationTrustCollection, trusts: ApplicationTrustCollection) """
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


class ApplicationTrustEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ApplicationVersionMatch(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ApplicationVersionMatch, values: MatchAllVersions (1), MatchExactVersion (0) """
    MatchAllVersions: ApplicationVersionMatch = ...
    MatchExactVersion: ApplicationVersionMatch = ...
    value__ = ...


class CodeConnectAccess: # skipped bases: <type 'object'>, <type 'object'>
    """ CodeConnectAccess(allowScheme: str, allowPort: int) """
    @property
    def Port(self) -> int:
        """ Get: Port(self: CodeConnectAccess) -> int """
        ...

    @property
    def Scheme(self) -> str:
        """ Get: Scheme(self: CodeConnectAccess) -> str """
        ...


    @staticmethod
    def CreateAnySchemeAccess(allowPort:int) -> CodeConnectAccess:
        """ CreateAnySchemeAccess(allowPort: int) -> CodeConnectAccess """
        ...

    @staticmethod
    def CreateOriginSchemeAccess(allowPort:int) -> CodeConnectAccess:
        """ CreateOriginSchemeAccess(allowPort: int) -> CodeConnectAccess """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: CodeConnectAccess, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CodeConnectAccess) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    AnyScheme: str = ...
    DefaultPort: int = ...
    OriginPort: int = ...
    OriginScheme: str = ...


class CodeGroup: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AttributeString(self) -> str:
        """ Get: AttributeString(self: CodeGroup) -> str """
        ...

    @property
    def Children(self) -> IList:
        """
        Get: Children(self: CodeGroup) -> IList
        Set: Children(self: CodeGroup) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: CodeGroup) -> str
        Set: Description(self: CodeGroup) = value
        """
        ...

    @property
    def MembershipCondition(self) -> IMembershipCondition:
        """
        Get: MembershipCondition(self: CodeGroup) -> IMembershipCondition
        Set: MembershipCondition(self: CodeGroup) = value
        """
        ...

    @property
    def MergeLogic(self) -> str:
        """ Get: MergeLogic(self: CodeGroup) -> str """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeGroup) -> str
        Set: Name(self: CodeGroup) = value
        """
        ...

    @property
    def PermissionSetName(self) -> str:
        """ Get: PermissionSetName(self: CodeGroup) -> str """
        ...

    @property
    def PolicyStatement(self) -> PolicyStatement:
        """
        Get: PolicyStatement(self: CodeGroup) -> PolicyStatement
        Set: PolicyStatement(self: CodeGroup) = value
        """
        ...


    def AddChild(self, group:CodeGroup): # -> 
        """ AddChild(self: CodeGroup, group: CodeGroup) """
        ...

    def Copy(self) -> CodeGroup:
        """ Copy(self: CodeGroup) -> CodeGroup """
        ...

    def CreateXml(self, *args): #cannot find CLR method
        """ CreateXml(self: CodeGroup, element: SecurityElement, level: PolicyLevel) """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: CodeGroup, o: object) -> bool
        Equals(self: CodeGroup, cg: CodeGroup, compareChildren: bool) -> bool
        """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: CodeGroup, e: SecurityElement, level: PolicyLevel)FromXml(self: CodeGroup, e: SecurityElement) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CodeGroup) -> int """
        ...

    def ParseXml(self, *args): #cannot find CLR method
        """ ParseXml(self: CodeGroup, e: SecurityElement, level: PolicyLevel) """
        ...

    def RemoveChild(self, group:CodeGroup): # -> 
        """ RemoveChild(self: CodeGroup, group: CodeGroup) """
        ...

    def Resolve(self, evidence:Evidence) -> PolicyStatement:
        """ Resolve(self: CodeGroup, evidence: Evidence) -> PolicyStatement """
        ...

    def ResolveMatchingCodeGroups(self, evidence:Evidence) -> CodeGroup:
        """ ResolveMatchingCodeGroups(self: CodeGroup, evidence: Evidence) -> CodeGroup """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: CodeGroup) -> SecurityElement
        ToXml(self: CodeGroup, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Evidence(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    Evidence()
    Evidence(evidence: Evidence)
    Evidence(hostEvidence: Array[object], assemblyEvidence: Array[object])
    Evidence(hostEvidence: Array[EvidenceBase], assemblyEvidence: Array[EvidenceBase])
    """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: Evidence) -> bool """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: Evidence) -> bool
        Set: Locked(self: Evidence) = value
        """
        ...


    def AddAssembly(self, id:object): # -> 
        """ AddAssembly(self: Evidence, id: object) """
        ...

    def AddAssemblyEvidence(self, evidence): # ->  # Not found arg types: {'evidence': 'T'}
        """ AddAssemblyEvidence[T](self: Evidence, evidence: T) """
        ...

    def AddHost(self, id:object): # -> 
        """ AddHost(self: Evidence, id: object) """
        ...

    def AddHostEvidence(self, evidence): # ->  # Not found arg types: {'evidence': 'T'}
        """ AddHostEvidence[T](self: Evidence, evidence: T) """
        ...

    def Clear(self): # -> 
        """ Clear(self: Evidence) """
        ...

    def Clone(self) -> Evidence:
        """ Clone(self: Evidence) -> Evidence """
        ...

    def GetAssemblyEnumerator(self) -> IEnumerator:
        """ GetAssemblyEnumerator(self: Evidence) -> IEnumerator """
        ...

    def GetAssemblyEvidence(self): # -> T
        """ GetAssemblyEvidence[T](self: Evidence) -> T """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Evidence) -> IEnumerator """
        ...

    def GetHostEnumerator(self) -> IEnumerator:
        """ GetHostEnumerator(self: Evidence) -> IEnumerator """
        ...

    def GetHostEvidence(self): # -> T
        """ GetHostEvidence[T](self: Evidence) -> T """
        ...

    def Merge(self, evidence:Evidence): # -> 
        """ Merge(self: Evidence, evidence: Evidence) """
        ...

    def RemoveType(self, t:Type): # -> 
        """ RemoveType(self: Evidence, t: Type) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class FileCodeGroup(IUnionSemanticCodeGroup, CodeGroup): # skipped bases: <type 'object'>
    """ FileCodeGroup(membershipCondition: IMembershipCondition, access: FileIOPermissionAccess) """
    pass

class FirstMatchCodeGroup(CodeGroup): # skipped bases: <type 'object'>
    """ FirstMatchCodeGroup(membershipCondition: IMembershipCondition, policy: PolicyStatement) """
    pass

class GacInstalled(EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ GacInstalled() """
    def Copy(self) -> object:
        """ Copy(self: GacInstalled) -> object """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: GacInstalled, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GacInstalled) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: GacInstalled) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class GacMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ GacMembershipCondition() """
    def Copy(self) -> IMembershipCondition:
        """ Copy(self: GacMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: GacMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: GacMembershipCondition, e: SecurityElement)FromXml(self: GacMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GacMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: GacMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: GacMembershipCondition) -> SecurityElement
        ToXml(self: GacMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Hash(EvidenceBase, ISerializable): # skipped bases: <type 'object'>
    """ Hash(assembly: Assembly) """
    @property
    def MD5(self) -> Array:
        """ Get: MD5(self: Hash) -> Array[Byte] """
        ...

    @property
    def SHA1(self) -> Array:
        """ Get: SHA1(self: Hash) -> Array[Byte] """
        ...

    @property
    def SHA256(self) -> Array:
        """ Get: SHA256(self: Hash) -> Array[Byte] """
        ...


    @staticmethod
    def CreateMD5(md5:Array) -> Hash:
        """ CreateMD5(md5: Array[Byte]) -> Hash """
        ...

    @staticmethod
    def CreateSHA1(sha1:Array) -> Hash:
        """ CreateSHA1(sha1: Array[Byte]) -> Hash """
        ...

    @staticmethod
    def CreateSHA256(sha256:Array) -> Hash:
        """ CreateSHA256(sha256: Array[Byte]) -> Hash """
        ...

    def GenerateHash(self, hashAlg:HashAlgorithm) -> Array:
        """ GenerateHash(self: Hash, hashAlg: HashAlgorithm) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: Hash) -> str """
        ...

    def __new__(cls, assembly:Assembly) -> Self:
        """ __new__(cls: type, assembly: Assembly) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class HashMembershipCondition(IReportMatchMembershipCondition, IDeserializationCallback, ISerializable): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ HashMembershipCondition(hashAlg: HashAlgorithm, value: Array[Byte]) """
    @property
    def HashAlgorithm(self) -> HashAlgorithm:
        """
        Get: HashAlgorithm(self: HashMembershipCondition) -> HashAlgorithm
        Set: HashAlgorithm(self: HashMembershipCondition) = value
        """
        ...

    @property
    def HashValue(self) -> Array:
        """
        Get: HashValue(self: HashMembershipCondition) -> Array[Byte]
        Set: HashValue(self: HashMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: HashMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: HashMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: HashMembershipCondition, e: SecurityElement)FromXml(self: HashMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: HashMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: HashMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: HashMembershipCondition) -> SecurityElement
        ToXml(self: HashMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IApplicationTrustManager(ISecurityEncodable): # skipped bases: <type 'object'>
    """ no doc """
    def DetermineApplicationTrust(self, activationContext:ActivationContext, context:TrustManagerContext) -> ApplicationTrust:
        """ DetermineApplicationTrust(self: IApplicationTrustManager, activationContext: ActivationContext, context: TrustManagerContext) -> ApplicationTrust """
        ...


class IIdentityPermissionFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateIdentityPermission(self, evidence:Evidence) -> IPermission:
        """ CreateIdentityPermission(self: IIdentityPermissionFactory, evidence: Evidence) -> IPermission """
        ...


class NetCodeGroup(IUnionSemanticCodeGroup, CodeGroup): # skipped bases: <type 'object'>
    """ NetCodeGroup(membershipCondition: IMembershipCondition) """
    def AddConnectAccess(self, originScheme:str, connectAccess:CodeConnectAccess): # -> 
        """ AddConnectAccess(self: NetCodeGroup, originScheme: str, connectAccess: CodeConnectAccess) """
        ...

    def GetConnectAccessRules(self) -> Array:
        """ GetConnectAccessRules(self: NetCodeGroup) -> Array[DictionaryEntry] """
        ...

    def ResetConnectAccess(self): # -> 
        """ ResetConnectAccess(self: NetCodeGroup) """
        ...

    AbsentOriginScheme: str = ...
    AnyOtherOriginScheme: str = ...


class PermissionRequestEvidence(EvidenceBase): # skipped bases: <type 'object'>
    """ PermissionRequestEvidence(request: PermissionSet, optional: PermissionSet, denied: PermissionSet) """
    @property
    def DeniedPermissions(self) -> PermissionSet:
        """ Get: DeniedPermissions(self: PermissionRequestEvidence) -> PermissionSet """
        ...

    @property
    def OptionalPermissions(self) -> PermissionSet:
        """ Get: OptionalPermissions(self: PermissionRequestEvidence) -> PermissionSet """
        ...

    @property
    def RequestedPermissions(self) -> PermissionSet:
        """ Get: RequestedPermissions(self: PermissionRequestEvidence) -> PermissionSet """
        ...


    def Copy(self) -> PermissionRequestEvidence:
        """ Copy(self: PermissionRequestEvidence) -> PermissionRequestEvidence """
        ...

    def ToString(self) -> str:
        """ ToString(self: PermissionRequestEvidence) -> str """
        ...

    def __new__(cls, request:PermissionSet, optional:PermissionSet, denied:PermissionSet) -> Self:
        """ __new__(cls: type, request: PermissionSet, optional: PermissionSet, denied: PermissionSet) """
        ...


class PolicyException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PolicyException()
    PolicyException(message: str)
    PolicyException(message: str, exception: Exception)
    """
    SerializeObjectState = ...


class PolicyLevel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def FullTrustAssemblies(self) -> IList:
        """ Get: FullTrustAssemblies(self: PolicyLevel) -> IList """
        ...

    @property
    def Label(self) -> str:
        """ Get: Label(self: PolicyLevel) -> str """
        ...

    @property
    def NamedPermissionSets(self) -> IList:
        """ Get: NamedPermissionSets(self: PolicyLevel) -> IList """
        ...

    @property
    def RootCodeGroup(self) -> CodeGroup:
        """
        Get: RootCodeGroup(self: PolicyLevel) -> CodeGroup
        Set: RootCodeGroup(self: PolicyLevel) = value
        """
        ...

    @property
    def StoreLocation(self) -> str:
        """ Get: StoreLocation(self: PolicyLevel) -> str """
        ...

    @property
    def Type(self) -> PolicyLevelType:
        """ Get: Type(self: PolicyLevel) -> PolicyLevelType """
        ...


    def AddFullTrustAssembly(self, *__args:StrongName): # -> 
        """ AddFullTrustAssembly(self: PolicyLevel, sn: StrongName)AddFullTrustAssembly(self: PolicyLevel, snMC: StrongNameMembershipCondition) """
        ...

    def AddNamedPermissionSet(self, permSet:NamedPermissionSet): # -> 
        """ AddNamedPermissionSet(self: PolicyLevel, permSet: NamedPermissionSet) """
        ...

    def ChangeNamedPermissionSet(self, name:str, pSet:PermissionSet) -> NamedPermissionSet:
        """ ChangeNamedPermissionSet(self: PolicyLevel, name: str, pSet: PermissionSet) -> NamedPermissionSet """
        ...

    @staticmethod
    def CreateAppDomainLevel() -> PolicyLevel:
        """ CreateAppDomainLevel() -> PolicyLevel """
        ...

    def FromXml(self, e:SecurityElement): # -> 
        """ FromXml(self: PolicyLevel, e: SecurityElement) """
        ...

    def GetNamedPermissionSet(self, name:str) -> NamedPermissionSet:
        """ GetNamedPermissionSet(self: PolicyLevel, name: str) -> NamedPermissionSet """
        ...

    def Recover(self): # -> 
        """ Recover(self: PolicyLevel) """
        ...

    def RemoveFullTrustAssembly(self, *__args:StrongName): # -> 
        """ RemoveFullTrustAssembly(self: PolicyLevel, sn: StrongName)RemoveFullTrustAssembly(self: PolicyLevel, snMC: StrongNameMembershipCondition) """
        ...

    def RemoveNamedPermissionSet(self, *__args:NamedPermissionSet) -> NamedPermissionSet:
        """
        RemoveNamedPermissionSet(self: PolicyLevel, permSet: NamedPermissionSet) -> NamedPermissionSet
        RemoveNamedPermissionSet(self: PolicyLevel, name: str) -> NamedPermissionSet
        """
        ...

    def Reset(self): # -> 
        """ Reset(self: PolicyLevel) """
        ...

    def Resolve(self, evidence:Evidence) -> PolicyStatement:
        """ Resolve(self: PolicyLevel, evidence: Evidence) -> PolicyStatement """
        ...

    def ResolveMatchingCodeGroups(self, evidence:Evidence) -> CodeGroup:
        """ ResolveMatchingCodeGroups(self: PolicyLevel, evidence: Evidence) -> CodeGroup """
        ...

    def ToXml(self) -> SecurityElement:
        """ ToXml(self: PolicyLevel) -> SecurityElement """
        ...


class PolicyStatement(ISecurityPolicyEncodable, ISecurityEncodable): # skipped bases: <type 'object'>
    """
    PolicyStatement(permSet: PermissionSet)
    PolicyStatement(permSet: PermissionSet, attributes: PolicyStatementAttribute)
    """
    @property
    def Attributes(self) -> PolicyStatementAttribute:
        """
        Get: Attributes(self: PolicyStatement) -> PolicyStatementAttribute
        Set: Attributes(self: PolicyStatement) = value
        """
        ...

    @property
    def AttributeString(self) -> str:
        """ Get: AttributeString(self: PolicyStatement) -> str """
        ...

    @property
    def PermissionSet(self) -> PermissionSet:
        """
        Get: PermissionSet(self: PolicyStatement) -> PermissionSet
        Set: PermissionSet(self: PolicyStatement) = value
        """
        ...


    def Copy(self) -> PolicyStatement:
        """ Copy(self: PolicyStatement) -> PolicyStatement """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: PolicyStatement, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PolicyStatement) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PolicyStatementAttribute(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PolicyStatementAttribute, values: All (3), Exclusive (1), LevelFinal (2), Nothing (0) """
    All: PolicyStatementAttribute = ...
    Exclusive: PolicyStatementAttribute = ...
    LevelFinal: PolicyStatementAttribute = ...
    Nothing: PolicyStatementAttribute = ...
    value__ = ...


class Publisher(EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ Publisher(cert: X509Certificate) """
    @property
    def Certificate(self) -> X509Certificate:
        """ Get: Certificate(self: Publisher) -> X509Certificate """
        ...


    def Copy(self) -> object:
        """ Copy(self: Publisher) -> object """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Publisher, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Publisher) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Publisher) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, cert:X509Certificate) -> Self:
        """ __new__(cls: type, cert: X509Certificate) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class PublisherMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ PublisherMembershipCondition(certificate: X509Certificate) """
    @property
    def Certificate(self) -> X509Certificate:
        """
        Get: Certificate(self: PublisherMembershipCondition) -> X509Certificate
        Set: Certificate(self: PublisherMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: PublisherMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: PublisherMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: PublisherMembershipCondition, e: SecurityElement)FromXml(self: PublisherMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PublisherMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: PublisherMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: PublisherMembershipCondition) -> SecurityElement
        ToXml(self: PublisherMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Site(EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ Site(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: Site) -> str """
        ...


    def Copy(self) -> object:
        """ Copy(self: Site) -> object """
        ...

    @staticmethod
    def CreateFromUrl(url:str) -> Site:
        """ CreateFromUrl(url: str) -> Site """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Site, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Site) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Site) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SiteMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ SiteMembershipCondition(site: str) """
    @property
    def Site(self) -> str:
        """
        Get: Site(self: SiteMembershipCondition) -> str
        Set: Site(self: SiteMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: SiteMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: SiteMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: SiteMembershipCondition, e: SecurityElement)FromXml(self: SiteMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SiteMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SiteMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: SiteMembershipCondition) -> SecurityElement
        ToXml(self: SiteMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class StrongName(IDelayEvaluatedEvidence, EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ StrongName(blob: StrongNamePublicKeyBlob, name: str, version: Version) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: StrongName) -> str """
        ...

    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """ Get: PublicKey(self: StrongName) -> StrongNamePublicKeyBlob """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: StrongName) -> Version """
        ...


    def Copy(self) -> object:
        """ Copy(self: StrongName) -> object """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: StrongName, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StrongName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: StrongName) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, blob:StrongNamePublicKeyBlob, name:str, version:Version) -> Self:
        """ __new__(cls: type, blob: StrongNamePublicKeyBlob, name: str, version: Version) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class StrongNameMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ StrongNameMembershipCondition(blob: StrongNamePublicKeyBlob, name: str, version: Version) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: StrongNameMembershipCondition) -> str
        Set: Name(self: StrongNameMembershipCondition) = value
        """
        ...

    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """
        Get: PublicKey(self: StrongNameMembershipCondition) -> StrongNamePublicKeyBlob
        Set: PublicKey(self: StrongNameMembershipCondition) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: StrongNameMembershipCondition) -> Version
        Set: Version(self: StrongNameMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: StrongNameMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: StrongNameMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: StrongNameMembershipCondition, e: SecurityElement)FromXml(self: StrongNameMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StrongNameMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: StrongNameMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: StrongNameMembershipCondition) -> SecurityElement
        ToXml(self: StrongNameMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TrustManagerContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    TrustManagerContext()
    TrustManagerContext(uiContext: TrustManagerUIContext)
    """
    @property
    def IgnorePersistedDecision(self) -> bool:
        """
        Get: IgnorePersistedDecision(self: TrustManagerContext) -> bool
        Set: IgnorePersistedDecision(self: TrustManagerContext) = value
        """
        ...

    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: TrustManagerContext) -> bool
        Set: KeepAlive(self: TrustManagerContext) = value
        """
        ...

    @property
    def NoPrompt(self) -> bool:
        """
        Get: NoPrompt(self: TrustManagerContext) -> bool
        Set: NoPrompt(self: TrustManagerContext) = value
        """
        ...

    @property
    def Persist(self) -> bool:
        """
        Get: Persist(self: TrustManagerContext) -> bool
        Set: Persist(self: TrustManagerContext) = value
        """
        ...

    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity:
        """
        Get: PreviousApplicationIdentity(self: TrustManagerContext) -> ApplicationIdentity
        Set: PreviousApplicationIdentity(self: TrustManagerContext) = value
        """
        ...

    @property
    def UIContext(self) -> TrustManagerUIContext:
        """
        Get: UIContext(self: TrustManagerContext) -> TrustManagerUIContext
        Set: UIContext(self: TrustManagerContext) = value
        """
        ...



class TrustManagerUIContext(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrustManagerUIContext, values: Install (0), Run (2), Upgrade (1) """
    Install: TrustManagerUIContext = ...
    Run: TrustManagerUIContext = ...
    Upgrade: TrustManagerUIContext = ...
    value__ = ...


class UnionCodeGroup(IUnionSemanticCodeGroup, CodeGroup): # skipped bases: <type 'object'>
    """ UnionCodeGroup(membershipCondition: IMembershipCondition, policy: PolicyStatement) """
    pass

class Url(EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ Url(name: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: Url) -> str """
        ...


    def Copy(self) -> object:
        """ Copy(self: Url) -> object """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Url, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Url) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Url) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class UrlMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ UrlMembershipCondition(url: str) """
    @property
    def Url(self) -> str:
        """
        Get: Url(self: UrlMembershipCondition) -> str
        Set: Url(self: UrlMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: UrlMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: UrlMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: UrlMembershipCondition, e: SecurityElement, level: PolicyLevel)FromXml(self: UrlMembershipCondition, e: SecurityElement) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: UrlMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: UrlMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: UrlMembershipCondition) -> SecurityElement
        ToXml(self: UrlMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Zone(EvidenceBase, IIdentityPermissionFactory): # skipped bases: <type 'object'>
    """ Zone(zone: SecurityZone) """
    @property
    def SecurityZone(self) -> SecurityZone:
        """ Get: SecurityZone(self: Zone) -> SecurityZone """
        ...


    def Copy(self) -> object:
        """ Copy(self: Zone) -> object """
        ...

    @staticmethod
    def CreateFromUrl(url:str) -> Zone:
        """ CreateFromUrl(url: str) -> Zone """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Zone, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Zone) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Zone) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, zone:SecurityZone) -> Self:
        """ __new__(cls: type, zone: SecurityZone) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ZoneMembershipCondition(IReportMatchMembershipCondition, IConstantMembershipCondition): # skipped bases: <type 'IMembershipCondition'>, <type 'ISecurityEncodable'>, <type 'ISecurityPolicyEncodable'>, <type 'object'>
    """ ZoneMembershipCondition(zone: SecurityZone) """
    @property
    def SecurityZone(self) -> SecurityZone:
        """
        Get: SecurityZone(self: ZoneMembershipCondition) -> SecurityZone
        Set: SecurityZone(self: ZoneMembershipCondition) = value
        """
        ...


    def Copy(self) -> IMembershipCondition:
        """ Copy(self: ZoneMembershipCondition) -> IMembershipCondition """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: ZoneMembershipCondition, o: object) -> bool """
        ...

    def FromXml(self, e:SecurityElement, level:PolicyLevel = ...): # -> 
        """ FromXml(self: ZoneMembershipCondition, e: SecurityElement)FromXml(self: ZoneMembershipCondition, e: SecurityElement, level: PolicyLevel) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ZoneMembershipCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ZoneMembershipCondition) -> str """
        ...

    def ToXml(self, level:PolicyLevel = ...) -> SecurityElement:
        """
        ToXml(self: ZoneMembershipCondition) -> SecurityElement
        ToXml(self: ZoneMembershipCondition, level: PolicyLevel) -> SecurityElement
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


