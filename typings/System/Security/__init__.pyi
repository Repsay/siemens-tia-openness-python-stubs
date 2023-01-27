# encoding: utf-8
# module System.Security calls itself Security
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Char, Enum, IDisposable, IntPtr, 
    SystemException, Type)

from System.Collections import (ArrayList, Hashtable, ICollection, 
    IEnumerator)

from System.Reflection import Assembly, AssemblyName, MethodInfo

from System.Runtime.Serialization import IDeserializationCallback

from System.Security.Permissions import (HostProtectionResource, 
    SecurityAction)

from System.Security.Policy import (ApplicationTrust, Evidence, EvidenceBase, 
    PolicyLevel, TrustManagerContext)

from System.Threading import AsyncFlowControl, ContextCallback

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    ISecurityElementFactory, field#)
"""

# no functions
# classes

class AllowPartiallyTrustedCallersAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AllowPartiallyTrustedCallersAttribute() """
    @property
    def PartialTrustVisibilityLevel(self) -> PartialTrustVisibilityLevel:
        """
        Get: PartialTrustVisibilityLevel(self: AllowPartiallyTrustedCallersAttribute) -> PartialTrustVisibilityLevel
        Set: PartialTrustVisibilityLevel(self: AllowPartiallyTrustedCallersAttribute) = value
        """
        ...



class CodeAccessPermission(IPermission, IStackWalk): # skipped bases: <type 'ISecurityEncodable'>, <type 'object'>
    """ no doc """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: CodeAccessPermission, obj: object) -> bool """
        ...

    def FromXml(self, elem:SecurityElement): # -> 
        """ FromXml(self: CodeAccessPermission, elem: SecurityElement) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CodeAccessPermission) -> int """
        ...

    @staticmethod
    def RevertAll(): # -> 
        """ RevertAll() """
        ...

    @staticmethod
    def RevertAssert(): # -> 
        """ RevertAssert() """
        ...

    @staticmethod
    def RevertDeny(): # -> 
        """ RevertDeny() """
        ...

    @staticmethod
    def RevertPermitOnly(): # -> 
        """ RevertPermitOnly() """
        ...

    def ToString(self) -> str:
        """ ToString(self: CodeAccessPermission) -> str """
        ...

    def ToXml(self) -> SecurityElement:
        """ ToXml(self: CodeAccessPermission) -> SecurityElement """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class HostProtectionException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HostProtectionException()
    HostProtectionException(message: str)
    HostProtectionException(message: str, e: Exception)
    HostProtectionException(message: str, protectedResources: HostProtectionResource, demandedResources: HostProtectionResource)
    """
    @property
    def DemandedResources(self) -> HostProtectionResource:
        """ Get: DemandedResources(self: HostProtectionException) -> HostProtectionResource """
        ...

    @property
    def ProtectedResources(self) -> HostProtectionResource:
        """ Get: ProtectedResources(self: HostProtectionException) -> HostProtectionResource """
        ...


    SerializeObjectState = ...


class HostSecurityManager: # skipped bases: <type 'object'>, <type 'object'>
    """ HostSecurityManager() """
    @property
    def DomainPolicy(self) -> PolicyLevel:
        """ Get: DomainPolicy(self: HostSecurityManager) -> PolicyLevel """
        ...

    @property
    def Flags(self) -> HostSecurityManagerOptions:
        """ Get: Flags(self: HostSecurityManager) -> HostSecurityManagerOptions """
        ...


    def DetermineApplicationTrust(self, applicationEvidence:Evidence, activatorEvidence:Evidence, context:TrustManagerContext) -> ApplicationTrust:
        """ DetermineApplicationTrust(self: HostSecurityManager, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust """
        ...

    def GenerateAppDomainEvidence(self, evidenceType:Type) -> EvidenceBase:
        """ GenerateAppDomainEvidence(self: HostSecurityManager, evidenceType: Type) -> EvidenceBase """
        ...

    def GenerateAssemblyEvidence(self, evidenceType:Type, assembly:Assembly) -> EvidenceBase:
        """ GenerateAssemblyEvidence(self: HostSecurityManager, evidenceType: Type, assembly: Assembly) -> EvidenceBase """
        ...

    def GetHostSuppliedAppDomainEvidenceTypes(self) -> Array:
        """ GetHostSuppliedAppDomainEvidenceTypes(self: HostSecurityManager) -> Array[Type] """
        ...

    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly:Assembly) -> Array:
        """ GetHostSuppliedAssemblyEvidenceTypes(self: HostSecurityManager, assembly: Assembly) -> Array[Type] """
        ...

    def ProvideAppDomainEvidence(self, inputEvidence:Evidence) -> Evidence:
        """ ProvideAppDomainEvidence(self: HostSecurityManager, inputEvidence: Evidence) -> Evidence """
        ...

    def ProvideAssemblyEvidence(self, loadedAssembly:Assembly, inputEvidence:Evidence) -> Evidence:
        """ ProvideAssemblyEvidence(self: HostSecurityManager, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence """
        ...

    def ResolvePolicy(self, evidence:Evidence) -> PermissionSet:
        """ ResolvePolicy(self: HostSecurityManager, evidence: Evidence) -> PermissionSet """
        ...


class HostSecurityManagerOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) HostSecurityManagerOptions, values: AllFlags (31), HostAppDomainEvidence (1), HostAssemblyEvidence (4), HostDetermineApplicationTrust (8), HostPolicyLevel (2), HostResolvePolicy (16), None (0) """
    AllFlags: HostSecurityManagerOptions = ...
    HostAppDomainEvidence: HostSecurityManagerOptions = ...
    HostAssemblyEvidence: HostSecurityManagerOptions = ...
    HostDetermineApplicationTrust: HostSecurityManagerOptions = ...
    HostPolicyLevel: HostSecurityManagerOptions = ...
    HostResolvePolicy: HostSecurityManagerOptions = ...
    value__ = ...


class IEvidenceFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Evidence(self) -> Evidence:
        """ Get: Evidence(self: IEvidenceFactory) -> Evidence """
        ...



class ISecurityEncodable: # skipped bases: <type 'object'>
    """ no doc """
    def FromXml(self, e:SecurityElement): # -> 
        """ FromXml(self: ISecurityEncodable, e: SecurityElement) """
        ...

    def ToXml(self) -> SecurityElement:
        """ ToXml(self: ISecurityEncodable) -> SecurityElement """
        ...


class IPermission(ISecurityEncodable): # skipped bases: <type 'object'>
    """ no doc """
    def Copy(self) -> IPermission:
        """ Copy(self: IPermission) -> IPermission """
        ...

    def Demand(self): # -> 
        """ Demand(self: IPermission) """
        ...

    def Intersect(self, target:IPermission) -> IPermission:
        """ Intersect(self: IPermission, target: IPermission) -> IPermission """
        ...

    def IsSubsetOf(self, target:IPermission) -> bool:
        """ IsSubsetOf(self: IPermission, target: IPermission) -> bool """
        ...

    def Union(self, target:IPermission) -> IPermission:
        """ Union(self: IPermission, target: IPermission) -> IPermission """
        ...


class ISecurityPolicyEncodable: # skipped bases: <type 'object'>
    """ no doc """
    def FromXml(self, e:SecurityElement, level:PolicyLevel): # -> 
        """ FromXml(self: ISecurityPolicyEncodable, e: SecurityElement, level: PolicyLevel) """
        ...

    def ToXml(self, level:PolicyLevel) -> SecurityElement:
        """ ToXml(self: ISecurityPolicyEncodable, level: PolicyLevel) -> SecurityElement """
        ...


class IStackWalk: # skipped bases: <type 'object'>
    """ no doc """
    def Assert(self): # -> 
        """ Assert(self: IStackWalk) """
        ...

    def Demand(self): # -> 
        """ Demand(self: IStackWalk) """
        ...

    def Deny(self): # -> 
        """ Deny(self: IStackWalk) """
        ...

    def PermitOnly(self): # -> 
        """ PermitOnly(self: IStackWalk) """
        ...


class ManifestKinds(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ManifestKinds, values: Application (2), ApplicationAndDeployment (3), Deployment (1), None (0) """
    Application: ManifestKinds = ...
    ApplicationAndDeployment: ManifestKinds = ...
    Deployment: ManifestKinds = ...
    value__ = ...


class PermissionSet(IStackWalk, IDeserializationCallback, ISecurityEncodable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    PermissionSet(state: PermissionState)
    PermissionSet(permSet: PermissionSet)
    """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: PermissionSet) -> bool """
        ...


    def AddPermission(self, perm:IPermission) -> IPermission:
        """ AddPermission(self: PermissionSet, perm: IPermission) -> IPermission """
        ...

    def AddPermissionImpl(self, *args): #cannot find CLR method
        """ AddPermissionImpl(self: PermissionSet, perm: IPermission) -> IPermission """
        ...

    def ContainsNonCodeAccessPermissions(self) -> bool:
        """ ContainsNonCodeAccessPermissions(self: PermissionSet) -> bool """
        ...

    @staticmethod
    def ConvertPermissionSet(inFormat:str, inData:Array, outFormat:str) -> Array:
        """ ConvertPermissionSet(inFormat: str, inData: Array[Byte], outFormat: str) -> Array[Byte] """
        ...

    def Copy(self) -> PermissionSet:
        """ Copy(self: PermissionSet) -> PermissionSet """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: PermissionSet, obj: object) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PermissionSet) -> IEnumerator """
        ...

    def GetEnumeratorImpl(self, *args): #cannot find CLR method
        """ GetEnumeratorImpl(self: PermissionSet) -> IEnumerator """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PermissionSet) -> int """
        ...

    def GetPermission(self, permClass:Type) -> IPermission:
        """ GetPermission(self: PermissionSet, permClass: Type) -> IPermission """
        ...

    def GetPermissionImpl(self, *args): #cannot find CLR method
        """ GetPermissionImpl(self: PermissionSet, permClass: Type) -> IPermission """
        ...

    def Intersect(self, other:PermissionSet) -> PermissionSet:
        """ Intersect(self: PermissionSet, other: PermissionSet) -> PermissionSet """
        ...

    def IsEmpty(self) -> bool:
        """ IsEmpty(self: PermissionSet) -> bool """
        ...

    def IsSubsetOf(self, target:PermissionSet) -> bool:
        """ IsSubsetOf(self: PermissionSet, target: PermissionSet) -> bool """
        ...

    def IsUnrestricted(self) -> bool:
        """ IsUnrestricted(self: PermissionSet) -> bool """
        ...

    def RemovePermission(self, permClass:Type) -> IPermission:
        """ RemovePermission(self: PermissionSet, permClass: Type) -> IPermission """
        ...

    def RemovePermissionImpl(self, *args): #cannot find CLR method
        """ RemovePermissionImpl(self: PermissionSet, permClass: Type) -> IPermission """
        ...

    @staticmethod
    def RevertAssert(): # -> 
        """ RevertAssert() """
        ...

    def SetPermission(self, perm:IPermission) -> IPermission:
        """ SetPermission(self: PermissionSet, perm: IPermission) -> IPermission """
        ...

    def SetPermissionImpl(self, *args): #cannot find CLR method
        """ SetPermissionImpl(self: PermissionSet, perm: IPermission) -> IPermission """
        ...

    def ToString(self) -> str:
        """ ToString(self: PermissionSet) -> str """
        ...

    def Union(self, other:PermissionSet) -> PermissionSet:
        """ Union(self: PermissionSet, other: PermissionSet) -> PermissionSet """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NamedPermissionSet(PermissionSet): # skipped bases: <type 'ISecurityEncodable'>, <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IStackWalk'>, <type 'object'>
    """
    NamedPermissionSet(name: str)
    NamedPermissionSet(name: str, state: PermissionState)
    NamedPermissionSet(name: str, permSet: PermissionSet)
    NamedPermissionSet(permSet: NamedPermissionSet)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: NamedPermissionSet) -> str
        Set: Description(self: NamedPermissionSet) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NamedPermissionSet) -> str
        Set: Name(self: NamedPermissionSet) = value
        """
        ...



class PartialTrustVisibilityLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PartialTrustVisibilityLevel, values: NotVisibleByDefault (1), VisibleToAllHosts (0) """
    NotVisibleByDefault: PartialTrustVisibilityLevel = ...
    value__ = ...
    VisibleToAllHosts: PartialTrustVisibilityLevel = ...


class PolicyLevelType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PolicyLevelType, values: AppDomain (3), Enterprise (2), Machine (1), User (0) """
    AppDomain: PolicyLevelType = ...
    Enterprise: PolicyLevelType = ...
    Machine: PolicyLevelType = ...
    User: PolicyLevelType = ...
    value__ = ...


class ReadOnlyPermissionSet(PermissionSet): # skipped bases: <type 'ISecurityEncodable'>, <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IStackWalk'>, <type 'object'>
    """ ReadOnlyPermissionSet(permissionSetXml: SecurityElement) """
    pass

class SecureString(IDisposable): # skipped bases: <type 'object'>
    """
    SecureString()
    SecureString(value: Char*, length: int)
    """
    @property
    def Length(self) -> int:
        """ Get: Length(self: SecureString) -> int """
        ...


    def AppendChar(self, c:Char): # -> 
        """ AppendChar(self: SecureString, c: Char) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SecureString) """
        ...

    def Copy(self) -> SecureString:
        """ Copy(self: SecureString) -> SecureString """
        ...

    def InsertAt(self, index:int, c:Char): # -> 
        """ InsertAt(self: SecureString, index: int, c: Char) """
        ...

    def IsReadOnly(self) -> bool:
        """ IsReadOnly(self: SecureString) -> bool """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: SecureString) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SecureString, index: int) """
        ...

    def SetAt(self, index:int, c:Char): # -> 
        """ SetAt(self: SecureString, index: int, c: Char) """
        ...


class SecureStringMarshal: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def SecureStringToCoTaskMemAnsi(s:SecureString) -> IntPtr:
        """ SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToCoTaskMemUnicode(s:SecureString) -> IntPtr:
        """ SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToGlobalAllocAnsi(s:SecureString) -> IntPtr:
        """ SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToGlobalAllocUnicode(s:SecureString) -> IntPtr:
        """ SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr """
        ...

    __all__: list = ...


class SecurityContext(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Capture() -> SecurityContext:
        """ Capture() -> SecurityContext """
        ...

    def CreateCopy(self) -> SecurityContext:
        """ CreateCopy(self: SecurityContext) -> SecurityContext """
        ...

    @staticmethod
    def IsFlowSuppressed() -> bool:
        """ IsFlowSuppressed() -> bool """
        ...

    @staticmethod
    def IsWindowsIdentityFlowSuppressed() -> bool:
        """ IsWindowsIdentityFlowSuppressed() -> bool """
        ...

    @staticmethod
    def RestoreFlow(): # -> 
        """ RestoreFlow() """
        ...

    @staticmethod
    def Run(securityContext:SecurityContext, callback:ContextCallback, state:object): # -> 
        """ Run(securityContext: SecurityContext, callback: ContextCallback, state: object) """
        ...

    @staticmethod
    def SuppressFlow() -> AsyncFlowControl:
        """ SuppressFlow() -> AsyncFlowControl """
        ...

    @staticmethod
    def SuppressFlowWindowsIdentity() -> AsyncFlowControl:
        """ SuppressFlowWindowsIdentity() -> AsyncFlowControl """
        ...


class SecurityContextSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityContextSource, values: CurrentAppDomain (0), CurrentAssembly (1) """
    CurrentAppDomain: SecurityContextSource = ...
    CurrentAssembly: SecurityContextSource = ...
    value__ = ...


class SecurityCriticalAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SecurityCriticalAttribute()
    SecurityCriticalAttribute(scope: SecurityCriticalScope)
    """
    @property
    def Scope(self) -> SecurityCriticalScope:
        """ Get: Scope(self: SecurityCriticalAttribute) -> SecurityCriticalScope """
        ...


    def __new__(cls, scope:SecurityCriticalScope = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, scope: SecurityCriticalScope)
        """
        ...


class SecurityCriticalScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityCriticalScope, values: Everything (1), Explicit (0) """
    Everything: SecurityCriticalScope = ...
    Explicit: SecurityCriticalScope = ...
    value__ = ...


class SecurityElement(ISecurityElementFactory): # skipped bases: <type 'object'>
    """
    SecurityElement(tag: str)
    SecurityElement(tag: str, text: str)
    """
    @property
    def Attributes(self) -> Hashtable:
        """
        Get: Attributes(self: SecurityElement) -> Hashtable
        Set: Attributes(self: SecurityElement) = value
        """
        ...

    @property
    def Children(self) -> ArrayList:
        """
        Get: Children(self: SecurityElement) -> ArrayList
        Set: Children(self: SecurityElement) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: SecurityElement) -> str
        Set: Tag(self: SecurityElement) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: SecurityElement) -> str
        Set: Text(self: SecurityElement) = value
        """
        ...


    def AddAttribute(self, name:str, value:str): # -> 
        """ AddAttribute(self: SecurityElement, name: str, value: str) """
        ...

    def AddChild(self, child:SecurityElement): # -> 
        """ AddChild(self: SecurityElement, child: SecurityElement) """
        ...

    def Attribute(self, name:str) -> str:
        """ Attribute(self: SecurityElement, name: str) -> str """
        ...

    def Copy(self) -> SecurityElement:
        """ Copy(self: SecurityElement) -> SecurityElement """
        ...

    def Equal(self, other:SecurityElement) -> bool:
        """ Equal(self: SecurityElement, other: SecurityElement) -> bool """
        ...

    @staticmethod
    def Escape(str:str) -> str:
        """ Escape(str: str) -> str """
        ...

    @staticmethod
    def FromString(xml:str) -> SecurityElement:
        """ FromString(xml: str) -> SecurityElement """
        ...

    @staticmethod
    def IsValidAttributeName(name:str) -> bool:
        """ IsValidAttributeName(name: str) -> bool """
        ...

    @staticmethod
    def IsValidAttributeValue(value:str) -> bool:
        """ IsValidAttributeValue(value: str) -> bool """
        ...

    @staticmethod
    def IsValidTag(tag:str) -> bool:
        """ IsValidTag(tag: str) -> bool """
        ...

    @staticmethod
    def IsValidText(text:str) -> bool:
        """ IsValidText(text: str) -> bool """
        ...

    def SearchForChildByTag(self, tag:str) -> SecurityElement:
        """ SearchForChildByTag(self: SecurityElement, tag: str) -> SecurityElement """
        ...

    def SearchForTextOfTag(self, tag:str) -> str:
        """ SearchForTextOfTag(self: SecurityElement, tag: str) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: SecurityElement) -> str """
        ...


class SecurityException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SecurityException()
    SecurityException(message: str)
    SecurityException(message: str, type: Type)
    SecurityException(message: str, type: Type, state: str)
    SecurityException(message: str, inner: Exception)
    SecurityException(message: str, assemblyName: AssemblyName, grant: PermissionSet, refused: PermissionSet, method: MethodInfo, action: SecurityAction, demanded: object, permThatFailed: IPermission, evidence: Evidence)
    SecurityException(message: str, deny: object, permitOnly: object, method: MethodInfo, demanded: object, permThatFailed: IPermission)
    """
    @property
    def Action(self) -> SecurityAction:
        """
        Get: Action(self: SecurityException) -> SecurityAction
        Set: Action(self: SecurityException) = value
        """
        ...

    @property
    def Demanded(self) -> object:
        """
        Get: Demanded(self: SecurityException) -> object
        Set: Demanded(self: SecurityException) = value
        """
        ...

    @property
    def DenySetInstance(self) -> object:
        """
        Get: DenySetInstance(self: SecurityException) -> object
        Set: DenySetInstance(self: SecurityException) = value
        """
        ...

    @property
    def FailedAssemblyInfo(self) -> AssemblyName:
        """
        Get: FailedAssemblyInfo(self: SecurityException) -> AssemblyName
        Set: FailedAssemblyInfo(self: SecurityException) = value
        """
        ...

    @property
    def FirstPermissionThatFailed(self) -> IPermission:
        """
        Get: FirstPermissionThatFailed(self: SecurityException) -> IPermission
        Set: FirstPermissionThatFailed(self: SecurityException) = value
        """
        ...

    @property
    def GrantedSet(self) -> str:
        """
        Get: GrantedSet(self: SecurityException) -> str
        Set: GrantedSet(self: SecurityException) = value
        """
        ...

    @property
    def Method(self) -> MethodInfo:
        """
        Get: Method(self: SecurityException) -> MethodInfo
        Set: Method(self: SecurityException) = value
        """
        ...

    @property
    def PermissionState(self) -> str:
        """
        Get: PermissionState(self: SecurityException) -> str
        Set: PermissionState(self: SecurityException) = value
        """
        ...

    @property
    def PermissionType(self) -> Type:
        """
        Get: PermissionType(self: SecurityException) -> Type
        Set: PermissionType(self: SecurityException) = value
        """
        ...

    @property
    def PermitOnlySetInstance(self) -> object:
        """
        Get: PermitOnlySetInstance(self: SecurityException) -> object
        Set: PermitOnlySetInstance(self: SecurityException) = value
        """
        ...

    @property
    def RefusedSet(self) -> str:
        """
        Get: RefusedSet(self: SecurityException) -> str
        Set: RefusedSet(self: SecurityException) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: SecurityException) -> str
        Set: Url(self: SecurityException) = value
        """
        ...

    @property
    def Zone(self) -> SecurityZone:
        """
        Get: Zone(self: SecurityException) -> SecurityZone
        Set: Zone(self: SecurityException) = value
        """
        ...


    SerializeObjectState = ...


class SecurityManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CheckExecutionRights(self) -> bool:
        """
        Get: CheckExecutionRights() -> bool
        Set: CheckExecutionRights() = value
        """
        ...

    @property
    def SecurityEnabled(self) -> bool:
        """
        Get: SecurityEnabled() -> bool
        Set: SecurityEnabled() = value
        """
        ...


    @staticmethod
    def CurrentThreadRequiresSecurityContextCapture() -> bool:
        """ CurrentThreadRequiresSecurityContextCapture() -> bool """
        ...

    @staticmethod
    def GetStandardSandbox(evidence:Evidence) -> PermissionSet:
        """ GetStandardSandbox(evidence: Evidence) -> PermissionSet """
        ...

    @staticmethod
    def GetZoneAndOrigin(zone, origin) -> Tuple_[ArrayList, ArrayList]:
        """ GetZoneAndOrigin() -> (ArrayList, ArrayList) """
        ...

    @staticmethod
    def IsGranted(perm:IPermission) -> bool:
        """ IsGranted(perm: IPermission) -> bool """
        ...

    @staticmethod
    def LoadPolicyLevelFromFile(path:str, type:PolicyLevelType) -> PolicyLevel:
        """ LoadPolicyLevelFromFile(path: str, type: PolicyLevelType) -> PolicyLevel """
        ...

    @staticmethod
    def LoadPolicyLevelFromString(str:str, type:PolicyLevelType) -> PolicyLevel:
        """ LoadPolicyLevelFromString(str: str, type: PolicyLevelType) -> PolicyLevel """
        ...

    @staticmethod
    def PolicyHierarchy() -> IEnumerator:
        """ PolicyHierarchy() -> IEnumerator """
        ...

    @staticmethod
    def ResolvePolicy(*__args:Evidence) -> PermissionSet:
        """
        ResolvePolicy(evidence: Evidence, reqdPset: PermissionSet, optPset: PermissionSet, denyPset: PermissionSet) -> (PermissionSet, PermissionSet)
        ResolvePolicy(evidence: Evidence) -> PermissionSet
        ResolvePolicy(evidences: Array[Evidence]) -> PermissionSet
        """
        ...

    @staticmethod
    def ResolvePolicyGroups(evidence:Evidence) -> IEnumerator:
        """ ResolvePolicyGroups(evidence: Evidence) -> IEnumerator """
        ...

    @staticmethod
    def ResolveSystemPolicy(evidence:Evidence) -> PermissionSet:
        """ ResolveSystemPolicy(evidence: Evidence) -> PermissionSet """
        ...

    @staticmethod
    def SavePolicy(): # -> 
        """ SavePolicy() """
        ...

    @staticmethod
    def SavePolicyLevel(level:PolicyLevel): # -> 
        """ SavePolicyLevel(level: PolicyLevel) """
        ...

    __all__: list = ...


class SecurityRulesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecurityRulesAttribute(ruleSet: SecurityRuleSet) """
    @property
    def RuleSet(self) -> SecurityRuleSet:
        """ Get: RuleSet(self: SecurityRulesAttribute) -> SecurityRuleSet """
        ...

    @property
    def SkipVerificationInFullTrust(self) -> bool:
        """
        Get: SkipVerificationInFullTrust(self: SecurityRulesAttribute) -> bool
        Set: SkipVerificationInFullTrust(self: SecurityRulesAttribute) = value
        """
        ...


    def __new__(cls, ruleSet:SecurityRuleSet) -> Self:
        """ __new__(cls: type, ruleSet: SecurityRuleSet) """
        ...


class SecurityRuleSet(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityRuleSet, values: Level1 (1), Level2 (2), None (0) """
    Level1: SecurityRuleSet = ...
    Level2: SecurityRuleSet = ...
    value__ = ...


class SecuritySafeCriticalAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecuritySafeCriticalAttribute() """
    pass

class SecurityState: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def EnsureState(self): # -> 
        """ EnsureState(self: SecurityState) """
        ...

    def IsStateAvailable(self) -> bool:
        """ IsStateAvailable(self: SecurityState) -> bool """
        ...


class SecurityTransparentAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecurityTransparentAttribute() """
    pass

class SecurityTreatAsSafeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecurityTreatAsSafeAttribute() """
    pass

class SecurityZone(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityZone, values: Internet (3), Intranet (1), MyComputer (0), NoZone (-1), Trusted (2), Untrusted (4) """
    Internet: SecurityZone = ...
    Intranet: SecurityZone = ...
    MyComputer: SecurityZone = ...
    NoZone: SecurityZone = ...
    Trusted: SecurityZone = ...
    Untrusted: SecurityZone = ...
    value__ = ...


class SuppressUnmanagedCodeSecurityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SuppressUnmanagedCodeSecurityAttribute() """
    pass

class UnverifiableCodeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UnverifiableCodeAttribute() """
    pass

class VerificationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    VerificationException()
    VerificationException(message: str)
    VerificationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XmlSyntaxException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XmlSyntaxException()
    XmlSyntaxException(message: str)
    XmlSyntaxException(message: str, inner: Exception)
    XmlSyntaxException(lineNumber: int)
    XmlSyntaxException(lineNumber: int, message: str)
    """
    SerializeObjectState = ...


# variables with complex values

