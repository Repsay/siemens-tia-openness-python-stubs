# encoding: utf-8
# module System.Security.AccessControl calls itself AccessControl
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Byte, Enum, Guid, Type, 
    UnauthorizedAccessException)

from System.Collections import (ICollection, IEnumerator, 
    ReadOnlyCollectionBase)

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Principal import IdentityReference, SecurityIdentifier

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AccessControlActions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AccessControlActions, values: Change (2), None (0), View (1) """
    Change: AccessControlActions = ...
    value__ = ...
    View: AccessControlActions = ...


class AccessControlModification(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AccessControlModification, values: Add (0), Remove (3), RemoveAll (4), RemoveSpecific (5), Reset (2), Set (1) """
    Add: AccessControlModification = ...
    Remove: AccessControlModification = ...
    RemoveAll: AccessControlModification = ...
    RemoveSpecific: AccessControlModification = ...
    Reset: AccessControlModification = ...
    Set: AccessControlModification = ...
    value__ = ...


class AccessControlSections(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AccessControlSections, values: Access (2), All (15), Audit (1), Group (8), None (0), Owner (4) """
    Access: AccessControlSections = ...
    All: AccessControlSections = ...
    Audit: AccessControlSections = ...
    Group: AccessControlSections = ...
    Owner: AccessControlSections = ...
    value__ = ...


class AccessControlType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AccessControlType, values: Allow (0), Deny (1) """
    Allow: AccessControlType = ...
    Deny: AccessControlType = ...
    value__ = ...


class AccessRule: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessControlType(self) -> AccessControlType:
        """ Get: AccessControlType(self: AccessRule) -> AccessControlType """
        ...

    @property
    def AccessMask(self):
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) """
        ...


class AceEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AceFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AceFlags, values: AuditFlags (192), ContainerInherit (2), FailedAccess (128), InheritanceFlags (15), Inherited (16), InheritOnly (8), None (0), NoPropagateInherit (4), ObjectInherit (1), SuccessfulAccess (64) """
    AuditFlags: AceFlags = ...
    ContainerInherit: AceFlags = ...
    FailedAccess: AceFlags = ...
    InheritanceFlags: AceFlags = ...
    Inherited: AceFlags = ...
    InheritOnly: AceFlags = ...
    NoPropagateInherit: AceFlags = ...
    ObjectInherit: AceFlags = ...
    SuccessfulAccess: AceFlags = ...
    value__ = ...


class AceQualifier(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AceQualifier, values: AccessAllowed (0), AccessDenied (1), SystemAlarm (3), SystemAudit (2) """
    AccessAllowed: AceQualifier = ...
    AccessDenied: AceQualifier = ...
    SystemAlarm: AceQualifier = ...
    SystemAudit: AceQualifier = ...
    value__ = ...


class AceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AceType, values: AccessAllowed (0), AccessAllowedCallback (9), AccessAllowedCallbackObject (11), AccessAllowedCompound (4), AccessAllowedObject (5), AccessDenied (1), AccessDeniedCallback (10), AccessDeniedCallbackObject (12), AccessDeniedObject (6), MaxDefinedAceType (16), SystemAlarm (3), SystemAlarmCallback (14), SystemAlarmCallbackObject (16), SystemAlarmObject (8), SystemAudit (2), SystemAuditCallback (13), SystemAuditCallbackObject (15), SystemAuditObject (7) """
    AccessAllowed: AceType = ...
    AccessAllowedCallback: AceType = ...
    AccessAllowedCallbackObject: AceType = ...
    AccessAllowedCompound: AceType = ...
    AccessAllowedObject: AceType = ...
    AccessDenied: AceType = ...
    AccessDeniedCallback: AceType = ...
    AccessDeniedCallbackObject: AceType = ...
    AccessDeniedObject: AceType = ...
    MaxDefinedAceType: AceType = ...
    SystemAlarm: AceType = ...
    SystemAlarmCallback: AceType = ...
    SystemAlarmCallbackObject: AceType = ...
    SystemAlarmObject: AceType = ...
    SystemAudit: AceType = ...
    SystemAuditCallback: AceType = ...
    SystemAuditCallbackObject: AceType = ...
    SystemAuditObject: AceType = ...
    value__ = ...


class AuditFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AuditFlags, values: Failure (2), None (0), Success (1) """
    Failure: AuditFlags = ...
    Success: AuditFlags = ...
    value__ = ...


class AuditRule: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessMask(self):
        ...

    @property
    def AuditFlags(self) -> AuditFlags:
        """ Get: AuditFlags(self: AuditRule) -> AuditFlags """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, identity: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, auditFlags: AuditFlags) """
        ...


class AuthorizationRule: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AccessMask(self):
        ...

    @property
    def IdentityReference(self) -> IdentityReference:
        """ Get: IdentityReference(self: AuthorizationRule) -> IdentityReference """
        ...

    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """ Get: InheritanceFlags(self: AuthorizationRule) -> InheritanceFlags """
        ...

    @property
    def IsInherited(self) -> bool:
        """ Get: IsInherited(self: AuthorizationRule) -> bool """
        ...

    @property
    def PropagationFlags(self) -> PropagationFlags:
        """ Get: PropagationFlags(self: AuthorizationRule) -> PropagationFlags """
        ...



class AuthorizationRuleCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AuthorizationRuleCollection() """
    def AddRule(self, rule:AuthorizationRule): # -> 
        """ AddRule(self: AuthorizationRuleCollection, rule: AuthorizationRule) """
        ...

    def CopyTo(self, rules:Array, index:int): # -> 
        """ CopyTo(self: AuthorizationRuleCollection, rules: Array[AuthorizationRule], index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class GenericAce: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AceFlags(self) -> AceFlags:
        """
        Get: AceFlags(self: GenericAce) -> AceFlags
        Set: AceFlags(self: GenericAce) = value
        """
        ...

    @property
    def AceType(self) -> AceType:
        """ Get: AceType(self: GenericAce) -> AceType """
        ...

    @property
    def AuditFlags(self) -> AuditFlags:
        """ Get: AuditFlags(self: GenericAce) -> AuditFlags """
        ...

    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: GenericAce) -> int """
        ...

    @property
    def InheritanceFlags(self) -> InheritanceFlags:
        """ Get: InheritanceFlags(self: GenericAce) -> InheritanceFlags """
        ...

    @property
    def IsInherited(self) -> bool:
        """ Get: IsInherited(self: GenericAce) -> bool """
        ...

    @property
    def PropagationFlags(self) -> PropagationFlags:
        """ Get: PropagationFlags(self: GenericAce) -> PropagationFlags """
        ...


    def Copy(self) -> GenericAce:
        """ Copy(self: GenericAce) -> GenericAce """
        ...

    @staticmethod
    def CreateFromBinaryForm(binaryForm:Array, offset:int) -> GenericAce:
        """ CreateFromBinaryForm(binaryForm: Array[Byte], offset: int) -> GenericAce """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: GenericAce, o: object) -> bool """
        ...

    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: GenericAce, binaryForm: Array[Byte], offset: int) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GenericAce) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class KnownAce(GenericAce): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessMask(self) -> int:
        """
        Get: AccessMask(self: KnownAce) -> int
        Set: AccessMask(self: KnownAce) = value
        """
        ...

    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """
        Get: SecurityIdentifier(self: KnownAce) -> SecurityIdentifier
        Set: SecurityIdentifier(self: KnownAce) = value
        """
        ...



class QualifiedAce(KnownAce): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AceQualifier(self) -> AceQualifier:
        """ Get: AceQualifier(self: QualifiedAce) -> AceQualifier """
        ...

    @property
    def IsCallback(self) -> bool:
        """ Get: IsCallback(self: QualifiedAce) -> bool """
        ...

    @property
    def OpaqueLength(self) -> int:
        """ Get: OpaqueLength(self: QualifiedAce) -> int """
        ...


    def GetOpaque(self) -> Array:
        """ GetOpaque(self: QualifiedAce) -> Array[Byte] """
        ...

    def SetOpaque(self, opaque:Array): # -> 
        """ SetOpaque(self: QualifiedAce, opaque: Array[Byte]) """
        ...


class CommonAce(QualifiedAce): # skipped bases: <type 'object'>
    """ CommonAce(flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte]) """
    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: CommonAce) -> int """
        ...


    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: CommonAce, binaryForm: Array[Byte], offset: int) """
        ...

    @staticmethod
    def MaxOpaqueLength(isCallback:bool) -> int:
        """ MaxOpaqueLength(isCallback: bool) -> int """
        ...

    def __new__(cls, flags:AceFlags, qualifier:AceQualifier, accessMask:int, sid:SecurityIdentifier, isCallback:bool, opaque:Array) -> Self:
        """ __new__(cls: type, flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, isCallback: bool, opaque: Array[Byte]) """
        ...


class GenericAcl(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: GenericAcl) -> int """
        ...

    @property
    def Revision(self) -> Byte:
        """ Get: Revision(self: GenericAcl) -> Byte """
        ...


    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: GenericAcl, binaryForm: Array[Byte], offset: int) """
        ...

    def GetEnumerator(self) -> AceEnumerator:
        """ GetEnumerator(self: GenericAcl) -> AceEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    AclRevision: Byte = ...
    AclRevisionDS: Byte = ...
    MaxBinaryLength: int = ...


class CommonAcl(GenericAcl): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def IsCanonical(self) -> bool:
        """ Get: IsCanonical(self: CommonAcl) -> bool """
        ...

    @property
    def IsContainer(self) -> bool:
        """ Get: IsContainer(self: CommonAcl) -> bool """
        ...

    @property
    def IsDS(self) -> bool:
        """ Get: IsDS(self: CommonAcl) -> bool """
        ...


    def Purge(self, sid:SecurityIdentifier): # -> 
        """ Purge(self: CommonAcl, sid: SecurityIdentifier) """
        ...

    def RemoveInheritedAces(self): # -> 
        """ RemoveInheritedAces(self: CommonAcl) """
        ...


class CommonObjectSecurity(ObjectSecurity): # skipped bases: <type 'object'>
    """ no doc """
    def AddAccessRule(self, *args): #cannot find CLR method
        """ AddAccessRule(self: CommonObjectSecurity, rule: AccessRule) """
        ...

    def AddAuditRule(self, *args): #cannot find CLR method
        """ AddAuditRule(self: CommonObjectSecurity, rule: AuditRule) """
        ...

    def GetAccessRules(self, includeExplicit:bool, includeInherited:bool, targetType:Type) -> AuthorizationRuleCollection:
        """ GetAccessRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection """
        ...

    def GetAuditRules(self, includeExplicit:bool, includeInherited:bool, targetType:Type) -> AuthorizationRuleCollection:
        """ GetAuditRules(self: CommonObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection """
        ...

    def RemoveAccessRule(self, *args): #cannot find CLR method
        """ RemoveAccessRule(self: CommonObjectSecurity, rule: AccessRule) -> bool """
        ...

    def RemoveAccessRuleAll(self, *args): #cannot find CLR method
        """ RemoveAccessRuleAll(self: CommonObjectSecurity, rule: AccessRule) """
        ...

    def RemoveAccessRuleSpecific(self, *args): #cannot find CLR method
        """ RemoveAccessRuleSpecific(self: CommonObjectSecurity, rule: AccessRule) """
        ...

    def RemoveAuditRule(self, *args): #cannot find CLR method
        """ RemoveAuditRule(self: CommonObjectSecurity, rule: AuditRule) -> bool """
        ...

    def RemoveAuditRuleAll(self, *args): #cannot find CLR method
        """ RemoveAuditRuleAll(self: CommonObjectSecurity, rule: AuditRule) """
        ...

    def RemoveAuditRuleSpecific(self, *args): #cannot find CLR method
        """ RemoveAuditRuleSpecific(self: CommonObjectSecurity, rule: AuditRule) """
        ...

    def ResetAccessRule(self, *args): #cannot find CLR method
        """ ResetAccessRule(self: CommonObjectSecurity, rule: AccessRule) """
        ...

    def SetAccessRule(self, *args): #cannot find CLR method
        """ SetAccessRule(self: CommonObjectSecurity, rule: AccessRule) """
        ...

    def SetAuditRule(self, *args): #cannot find CLR method
        """ SetAuditRule(self: CommonObjectSecurity, rule: AuditRule) """
        ...


class GenericSecurityDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: GenericSecurityDescriptor) -> int """
        ...

    @property
    def ControlFlags(self) -> ControlFlags:
        """ Get: ControlFlags(self: GenericSecurityDescriptor) -> ControlFlags """
        ...

    @property
    def Group(self) -> SecurityIdentifier:
        """
        Get: Group(self: GenericSecurityDescriptor) -> SecurityIdentifier
        Set: Group(self: GenericSecurityDescriptor) = value
        """
        ...

    @property
    def Owner(self) -> SecurityIdentifier:
        """
        Get: Owner(self: GenericSecurityDescriptor) -> SecurityIdentifier
        Set: Owner(self: GenericSecurityDescriptor) = value
        """
        ...

    @property
    def Revision(self) -> Byte:
        """ Get: Revision() -> Byte """
        ...


    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: GenericSecurityDescriptor, binaryForm: Array[Byte], offset: int) """
        ...

    def GetSddlForm(self, includeSections:AccessControlSections) -> str:
        """ GetSddlForm(self: GenericSecurityDescriptor, includeSections: AccessControlSections) -> str """
        ...

    @staticmethod
    def IsSddlConversionSupported() -> bool:
        """ IsSddlConversionSupported() -> bool """
        ...



class CommonSecurityDescriptor(GenericSecurityDescriptor): # skipped bases: <type 'object'>
    """
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, sddlForm: str)
    CommonSecurityDescriptor(isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
    """
    @property
    def DiscretionaryAcl(self) -> DiscretionaryAcl:
        """
        Get: DiscretionaryAcl(self: CommonSecurityDescriptor) -> DiscretionaryAcl
        Set: DiscretionaryAcl(self: CommonSecurityDescriptor) = value
        """
        ...

    @property
    def IsContainer(self) -> bool:
        """ Get: IsContainer(self: CommonSecurityDescriptor) -> bool """
        ...

    @property
    def IsDiscretionaryAclCanonical(self) -> bool:
        """ Get: IsDiscretionaryAclCanonical(self: CommonSecurityDescriptor) -> bool """
        ...

    @property
    def IsDS(self) -> bool:
        """ Get: IsDS(self: CommonSecurityDescriptor) -> bool """
        ...

    @property
    def IsSystemAclCanonical(self) -> bool:
        """ Get: IsSystemAclCanonical(self: CommonSecurityDescriptor) -> bool """
        ...

    @property
    def SystemAcl(self) -> SystemAcl:
        """
        Get: SystemAcl(self: CommonSecurityDescriptor) -> SystemAcl
        Set: SystemAcl(self: CommonSecurityDescriptor) = value
        """
        ...


    def AddDiscretionaryAcl(self, revision:Byte, trusted:int): # -> 
        """ AddDiscretionaryAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int) """
        ...

    def AddSystemAcl(self, revision:Byte, trusted:int): # -> 
        """ AddSystemAcl(self: CommonSecurityDescriptor, revision: Byte, trusted: int) """
        ...

    def PurgeAccessControl(self, sid:SecurityIdentifier): # -> 
        """ PurgeAccessControl(self: CommonSecurityDescriptor, sid: SecurityIdentifier) """
        ...

    def PurgeAudit(self, sid:SecurityIdentifier): # -> 
        """ PurgeAudit(self: CommonSecurityDescriptor, sid: SecurityIdentifier) """
        ...

    def SetDiscretionaryAclProtection(self, isProtected:bool, preserveInheritance:bool): # -> 
        """ SetDiscretionaryAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool) """
        ...

    def SetSystemAclProtection(self, isProtected:bool, preserveInheritance:bool): # -> 
        """ SetSystemAclProtection(self: CommonSecurityDescriptor, isProtected: bool, preserveInheritance: bool) """
        ...

    def __new__(cls, isContainer:bool, isDS:bool, *__args:RawSecurityDescriptor) -> Self:
        """
        __new__(cls: type, isContainer: bool, isDS: bool, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl)
        __new__(cls: type, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor)
        __new__(cls: type, isContainer: bool, isDS: bool, sddlForm: str)
        __new__(cls: type, isContainer: bool, isDS: bool, binaryForm: Array[Byte], offset: int)
        """
        ...


class CompoundAce(KnownAce): # skipped bases: <type 'object'>
    """ CompoundAce(flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier) """
    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: CompoundAce) -> int """
        ...

    @property
    def CompoundAceType(self) -> CompoundAceType:
        """
        Get: CompoundAceType(self: CompoundAce) -> CompoundAceType
        Set: CompoundAceType(self: CompoundAce) = value
        """
        ...


    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: CompoundAce, binaryForm: Array[Byte], offset: int) """
        ...

    def __new__(cls, flags:AceFlags, accessMask:int, compoundAceType:CompoundAceType, sid:SecurityIdentifier) -> Self:
        """ __new__(cls: type, flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: SecurityIdentifier) """
        ...


class CompoundAceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompoundAceType, values: Impersonation (1) """
    Impersonation: CompoundAceType = ...
    value__ = ...


class ControlFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ControlFlags, values: DiscretionaryAclAutoInherited (1024), DiscretionaryAclAutoInheritRequired (256), DiscretionaryAclDefaulted (8), DiscretionaryAclPresent (4), DiscretionaryAclProtected (4096), DiscretionaryAclUntrusted (64), GroupDefaulted (2), None (0), OwnerDefaulted (1), RMControlValid (16384), SelfRelative (32768), ServerSecurity (128), SystemAclAutoInherited (2048), SystemAclAutoInheritRequired (512), SystemAclDefaulted (32), SystemAclPresent (16), SystemAclProtected (8192) """
    DiscretionaryAclAutoInherited: ControlFlags = ...
    DiscretionaryAclAutoInheritRequired: ControlFlags = ...
    DiscretionaryAclDefaulted: ControlFlags = ...
    DiscretionaryAclPresent: ControlFlags = ...
    DiscretionaryAclProtected: ControlFlags = ...
    DiscretionaryAclUntrusted: ControlFlags = ...
    GroupDefaulted: ControlFlags = ...
    OwnerDefaulted: ControlFlags = ...
    RMControlValid: ControlFlags = ...
    SelfRelative: ControlFlags = ...
    ServerSecurity: ControlFlags = ...
    SystemAclAutoInherited: ControlFlags = ...
    SystemAclAutoInheritRequired: ControlFlags = ...
    SystemAclDefaulted: ControlFlags = ...
    SystemAclPresent: ControlFlags = ...
    SystemAclProtected: ControlFlags = ...
    value__ = ...


class CryptoKeyAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    CryptoKeyAccessRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
    CryptoKeyAccessRule(identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType)
    """
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """ Get: CryptoKeyRights(self: CryptoKeyAccessRule) -> CryptoKeyRights """
        ...



class CryptoKeyAuditRule(AuditRule): # skipped bases: <type 'object'>
    """
    CryptoKeyAuditRule(identity: IdentityReference, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
    CryptoKeyAuditRule(identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags)
    """
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:
        """ Get: CryptoKeyRights(self: CryptoKeyAuditRule) -> CryptoKeyRights """
        ...



class CryptoKeyRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CryptoKeyRights, values: ChangePermissions (262144), Delete (65536), FullControl (2032027), GenericAll (268435456), GenericExecute (536870912), GenericRead (-2147483648), GenericWrite (1073741824), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16) """
    ChangePermissions: CryptoKeyRights = ...
    Delete: CryptoKeyRights = ...
    FullControl: CryptoKeyRights = ...
    GenericAll: CryptoKeyRights = ...
    GenericExecute: CryptoKeyRights = ...
    GenericRead: CryptoKeyRights = ...
    GenericWrite: CryptoKeyRights = ...
    ReadAttributes: CryptoKeyRights = ...
    ReadData: CryptoKeyRights = ...
    ReadExtendedAttributes: CryptoKeyRights = ...
    ReadPermissions: CryptoKeyRights = ...
    Synchronize: CryptoKeyRights = ...
    TakeOwnership: CryptoKeyRights = ...
    value__ = ...
    WriteAttributes: CryptoKeyRights = ...
    WriteData: CryptoKeyRights = ...
    WriteExtendedAttributes: CryptoKeyRights = ...


class NativeObjectSecurity(CommonObjectSecurity): # skipped bases: <type 'object'>
    """ no doc """
    def ExceptionFromErrorCode(self, *args): #cannot find CLR method
        """ ExceptionFromErrorCode(object: object, method: IntPtr) """
        ...



class CryptoKeySecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """
    CryptoKeySecurity()
    CryptoKeySecurity(securityDescriptor: CommonSecurityDescriptor)
    """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: CryptoKeySecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: CryptoKeySecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: CryptoKeySecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: CryptoKeySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class CustomAce(GenericAce): # skipped bases: <type 'object'>
    """ CustomAce(type: AceType, flags: AceFlags, opaque: Array[Byte]) """
    @property
    def OpaqueLength(self) -> int:
        """ Get: OpaqueLength(self: CustomAce) -> int """
        ...


    def GetOpaque(self) -> Array:
        """ GetOpaque(self: CustomAce) -> Array[Byte] """
        ...

    def SetOpaque(self, opaque:Array): # -> 
        """ SetOpaque(self: CustomAce, opaque: Array[Byte]) """
        ...

    def __new__(cls, type:AceType, flags:AceFlags, opaque:Array) -> Self:
        """ __new__(cls: type, type: AceType, flags: AceFlags, opaque: Array[Byte]) """
        ...

    MaxOpaqueLength: int = ...


class DirectoryObjectSecurity(ObjectSecurity): # skipped bases: <type 'object'>
    """ no doc """
    def AddAccessRule(self, *args): #cannot find CLR method
        """ AddAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) """
        ...

    def AddAuditRule(self, *args): #cannot find CLR method
        """ AddAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule) """
        ...

    def GetAccessRules(self, includeExplicit:bool, includeInherited:bool, targetType:Type) -> AuthorizationRuleCollection:
        """ GetAccessRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection """
        ...

    def GetAuditRules(self, includeExplicit:bool, includeInherited:bool, targetType:Type) -> AuthorizationRuleCollection:
        """ GetAuditRules(self: DirectoryObjectSecurity, includeExplicit: bool, includeInherited: bool, targetType: Type) -> AuthorizationRuleCollection """
        ...

    def RemoveAccessRule(self, *args): #cannot find CLR method
        """ RemoveAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) -> bool """
        ...

    def RemoveAccessRuleAll(self, *args): #cannot find CLR method
        """ RemoveAccessRuleAll(self: DirectoryObjectSecurity, rule: ObjectAccessRule) """
        ...

    def RemoveAccessRuleSpecific(self, *args): #cannot find CLR method
        """ RemoveAccessRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAccessRule) """
        ...

    def RemoveAuditRule(self, *args): #cannot find CLR method
        """ RemoveAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule) -> bool """
        ...

    def RemoveAuditRuleAll(self, *args): #cannot find CLR method
        """ RemoveAuditRuleAll(self: DirectoryObjectSecurity, rule: ObjectAuditRule) """
        ...

    def RemoveAuditRuleSpecific(self, *args): #cannot find CLR method
        """ RemoveAuditRuleSpecific(self: DirectoryObjectSecurity, rule: ObjectAuditRule) """
        ...

    def ResetAccessRule(self, *args): #cannot find CLR method
        """ ResetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) """
        ...

    def SetAccessRule(self, *args): #cannot find CLR method
        """ SetAccessRule(self: DirectoryObjectSecurity, rule: ObjectAccessRule) """
        ...

    def SetAuditRule(self, *args): #cannot find CLR method
        """ SetAuditRule(self: DirectoryObjectSecurity, rule: ObjectAuditRule) """
        ...


class FileSystemSecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: FileSystemSecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: FileSystemSecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: FileSystemSecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: FileSystemSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class DirectorySecurity(FileSystemSecurity): # skipped bases: <type 'object'>
    """
    DirectorySecurity()
    DirectorySecurity(name: str, includeSections: AccessControlSections)
    """
    def __new__(cls, name:str = ..., includeSections:AccessControlSections = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, includeSections: AccessControlSections)
        """
        ...


class DiscretionaryAcl(CommonAcl): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    DiscretionaryAcl(isContainer: bool, isDS: bool, capacity: int)
    DiscretionaryAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)
    DiscretionaryAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """
    def AddAccess(self, accessType:AccessControlType, sid:SecurityIdentifier, *__args:ObjectAccessRule): # -> 
        """ AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)AddAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def RemoveAccess(self, accessType:AccessControlType, sid:SecurityIdentifier, *__args:ObjectAccessRule) -> bool:
        """
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule) -> bool
        RemoveAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool
        """
        ...

    def RemoveAccessSpecific(self, accessType:AccessControlType, sid:SecurityIdentifier, *__args:ObjectAccessRule): # -> 
        """ RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)RemoveAccessSpecific(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def SetAccess(self, accessType:AccessControlType, sid:SecurityIdentifier, *__args:ObjectAccessRule): # -> 
        """ SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, rule: ObjectAccessRule)SetAccess(self: DiscretionaryAcl, accessType: AccessControlType, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def __new__(cls, isContainer:bool, isDS:bool, *__args:int) -> Self:
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        ...


class EventWaitHandleAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    EventWaitHandleAccessRule(identity: IdentityReference, eventRights: EventWaitHandleRights, type: AccessControlType)
    EventWaitHandleAccessRule(identity: str, eventRights: EventWaitHandleRights, type: AccessControlType)
    """
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """ Get: EventWaitHandleRights(self: EventWaitHandleAccessRule) -> EventWaitHandleRights """
        ...



class EventWaitHandleAuditRule(AuditRule): # skipped bases: <type 'object'>
    """ EventWaitHandleAuditRule(identity: IdentityReference, eventRights: EventWaitHandleRights, flags: AuditFlags) """
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:
        """ Get: EventWaitHandleRights(self: EventWaitHandleAuditRule) -> EventWaitHandleRights """
        ...



class EventWaitHandleRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventWaitHandleRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288) """
    ChangePermissions: EventWaitHandleRights = ...
    Delete: EventWaitHandleRights = ...
    FullControl: EventWaitHandleRights = ...
    Modify: EventWaitHandleRights = ...
    ReadPermissions: EventWaitHandleRights = ...
    Synchronize: EventWaitHandleRights = ...
    TakeOwnership: EventWaitHandleRights = ...
    value__ = ...


class EventWaitHandleSecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """ EventWaitHandleSecurity() """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: EventWaitHandleSecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: EventWaitHandleSecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: EventWaitHandleSecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: EventWaitHandleSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class FileSecurity(FileSystemSecurity): # skipped bases: <type 'object'>
    """
    FileSecurity()
    FileSecurity(fileName: str, includeSections: AccessControlSections)
    """
    def __new__(cls, fileName:str = ..., includeSections:AccessControlSections = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, includeSections: AccessControlSections)
        """
        ...


class FileSystemAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, type: AccessControlType)
    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, type: AccessControlType)
    FileSystemAccessRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    FileSystemAccessRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """ Get: FileSystemRights(self: FileSystemAccessRule) -> FileSystemRights """
        ...



class FileSystemAuditRule(AuditRule): # skipped bases: <type 'object'>
    """
    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, flags: AuditFlags)
    FileSystemAuditRule(identity: IdentityReference, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags)
    FileSystemAuditRule(identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """
    @property
    def FileSystemRights(self) -> FileSystemRights:
        """ Get: FileSystemRights(self: FileSystemAuditRule) -> FileSystemRights """
        ...



class FileSystemRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileSystemRights, values: AppendData (4), ChangePermissions (262144), CreateDirectories (4), CreateFiles (2), Delete (65536), DeleteSubdirectoriesAndFiles (64), ExecuteFile (32), FullControl (2032127), ListDirectory (1), Modify (197055), Read (131209), ReadAndExecute (131241), ReadAttributes (128), ReadData (1), ReadExtendedAttributes (8), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288), Traverse (32), Write (278), WriteAttributes (256), WriteData (2), WriteExtendedAttributes (16) """
    AppendData: FileSystemRights = ...
    ChangePermissions: FileSystemRights = ...
    CreateDirectories: FileSystemRights = ...
    CreateFiles: FileSystemRights = ...
    Delete: FileSystemRights = ...
    DeleteSubdirectoriesAndFiles: FileSystemRights = ...
    ExecuteFile: FileSystemRights = ...
    FullControl: FileSystemRights = ...
    ListDirectory: FileSystemRights = ...
    Modify: FileSystemRights = ...
    Read: FileSystemRights = ...
    ReadAndExecute: FileSystemRights = ...
    ReadAttributes: FileSystemRights = ...
    ReadData: FileSystemRights = ...
    ReadExtendedAttributes: FileSystemRights = ...
    ReadPermissions: FileSystemRights = ...
    Synchronize: FileSystemRights = ...
    TakeOwnership: FileSystemRights = ...
    Traverse: FileSystemRights = ...
    value__ = ...
    Write: FileSystemRights = ...
    WriteAttributes: FileSystemRights = ...
    WriteData: FileSystemRights = ...
    WriteExtendedAttributes: FileSystemRights = ...


class InheritanceFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InheritanceFlags, values: ContainerInherit (1), None (0), ObjectInherit (2) """
    ContainerInherit: InheritanceFlags = ...
    ObjectInherit: InheritanceFlags = ...
    value__ = ...


class MutexAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    MutexAccessRule(identity: IdentityReference, eventRights: MutexRights, type: AccessControlType)
    MutexAccessRule(identity: str, eventRights: MutexRights, type: AccessControlType)
    """
    @property
    def MutexRights(self) -> MutexRights:
        """ Get: MutexRights(self: MutexAccessRule) -> MutexRights """
        ...



class MutexAuditRule(AuditRule): # skipped bases: <type 'object'>
    """ MutexAuditRule(identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags) """
    @property
    def MutexRights(self) -> MutexRights:
        """ Get: MutexRights(self: MutexAuditRule) -> MutexRights """
        ...



class MutexRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MutexRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031617), Modify (1), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288) """
    ChangePermissions: MutexRights = ...
    Delete: MutexRights = ...
    FullControl: MutexRights = ...
    Modify: MutexRights = ...
    ReadPermissions: MutexRights = ...
    Synchronize: MutexRights = ...
    TakeOwnership: MutexRights = ...
    value__ = ...


class MutexSecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """
    MutexSecurity()
    MutexSecurity(name: str, includeSections: AccessControlSections)
    """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: MutexSecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: MutexSecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: MutexSecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: MutexSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class ObjectAccessRule(AccessRule): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InheritedObjectType(self) -> Guid:
        """ Get: InheritedObjectType(self: ObjectAccessRule) -> Guid """
        ...

    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """ Get: ObjectFlags(self: ObjectAccessRule) -> ObjectAceFlags """
        ...

    @property
    def ObjectType(self) -> Guid:
        """ Get: ObjectType(self: ObjectAccessRule) -> Guid """
        ...



class ObjectAce(QualifiedAce): # skipped bases: <type 'object'>
    """ ObjectAce(aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte]) """
    @property
    def BinaryLength(self) -> int:
        """ Get: BinaryLength(self: ObjectAce) -> int """
        ...

    @property
    def InheritedObjectAceType(self) -> Guid:
        """
        Get: InheritedObjectAceType(self: ObjectAce) -> Guid
        Set: InheritedObjectAceType(self: ObjectAce) = value
        """
        ...

    @property
    def ObjectAceFlags(self) -> ObjectAceFlags:
        """
        Get: ObjectAceFlags(self: ObjectAce) -> ObjectAceFlags
        Set: ObjectAceFlags(self: ObjectAce) = value
        """
        ...

    @property
    def ObjectAceType(self) -> Guid:
        """
        Get: ObjectAceType(self: ObjectAce) -> Guid
        Set: ObjectAceType(self: ObjectAce) = value
        """
        ...


    def GetBinaryForm(self, binaryForm:Array, offset:int): # -> 
        """ GetBinaryForm(self: ObjectAce, binaryForm: Array[Byte], offset: int) """
        ...

    @staticmethod
    def MaxOpaqueLength(isCallback:bool) -> int:
        """ MaxOpaqueLength(isCallback: bool) -> int """
        ...

    def __new__(cls, aceFlags:AceFlags, qualifier:AceQualifier, accessMask:int, sid:SecurityIdentifier, flags:ObjectAceFlags, type:Guid, inheritedType:Guid, isCallback:bool, opaque:Array) -> Self:
        """ __new__(cls: type, aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: SecurityIdentifier, flags: ObjectAceFlags, type: Guid, inheritedType: Guid, isCallback: bool, opaque: Array[Byte]) """
        ...


class ObjectAceFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ObjectAceFlags, values: InheritedObjectAceTypePresent (2), None (0), ObjectAceTypePresent (1) """
    InheritedObjectAceTypePresent: ObjectAceFlags = ...
    ObjectAceTypePresent: ObjectAceFlags = ...
    value__ = ...


class ObjectAuditRule(AuditRule): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InheritedObjectType(self) -> Guid:
        """ Get: InheritedObjectType(self: ObjectAuditRule) -> Guid """
        ...

    @property
    def ObjectFlags(self) -> ObjectAceFlags:
        """ Get: ObjectFlags(self: ObjectAuditRule) -> ObjectAceFlags """
        ...

    @property
    def ObjectType(self) -> Guid:
        """ Get: ObjectType(self: ObjectAuditRule) -> Guid """
        ...



class ObjectSecurity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: ObjectSecurity) -> Type """
        ...

    @property
    def AccessRulesModified(self):
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: ObjectSecurity) -> Type """
        ...

    @property
    def AreAccessRulesCanonical(self) -> bool:
        """ Get: AreAccessRulesCanonical(self: ObjectSecurity) -> bool """
        ...

    @property
    def AreAccessRulesProtected(self) -> bool:
        """ Get: AreAccessRulesProtected(self: ObjectSecurity) -> bool """
        ...

    @property
    def AreAuditRulesCanonical(self) -> bool:
        """ Get: AreAuditRulesCanonical(self: ObjectSecurity) -> bool """
        ...

    @property
    def AreAuditRulesProtected(self) -> bool:
        """ Get: AreAuditRulesProtected(self: ObjectSecurity) -> bool """
        ...

    @property
    def AuditRulesModified(self):
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: ObjectSecurity) -> Type """
        ...

    @property
    def GroupModified(self):
        ...

    @property
    def IsContainer(self):
        ...

    @property
    def IsDS(self):
        ...

    @property
    def OwnerModified(self):
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: ObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: ObjectSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...

    def GetGroup(self, targetType:Type) -> IdentityReference:
        """ GetGroup(self: ObjectSecurity, targetType: Type) -> IdentityReference """
        ...

    def GetOwner(self, targetType:Type) -> IdentityReference:
        """ GetOwner(self: ObjectSecurity, targetType: Type) -> IdentityReference """
        ...

    def GetSecurityDescriptorBinaryForm(self) -> Array:
        """ GetSecurityDescriptorBinaryForm(self: ObjectSecurity) -> Array[Byte] """
        ...

    def GetSecurityDescriptorSddlForm(self, includeSections:AccessControlSections) -> str:
        """ GetSecurityDescriptorSddlForm(self: ObjectSecurity, includeSections: AccessControlSections) -> str """
        ...

    @staticmethod
    def IsSddlConversionSupported() -> bool:
        """ IsSddlConversionSupported() -> bool """
        ...

    def ModifyAccess(self, *args): #cannot find CLR method
        """ ModifyAccess(self: ObjectSecurity, modification: AccessControlModification, rule: AccessRule) -> (bool, bool) """
        ...

    def ModifyAccessRule(self, modification, rule, modified) -> Tuple_[bool, bool]:
        """ ModifyAccessRule(self: ObjectSecurity, modification: AccessControlModification, rule: AccessRule) -> (bool, bool) """
        ...

    def ModifyAudit(self, *args): #cannot find CLR method
        """ ModifyAudit(self: ObjectSecurity, modification: AccessControlModification, rule: AuditRule) -> (bool, bool) """
        ...

    def ModifyAuditRule(self, modification, rule, modified) -> Tuple_[bool, bool]:
        """ ModifyAuditRule(self: ObjectSecurity, modification: AccessControlModification, rule: AuditRule) -> (bool, bool) """
        ...

    def Persist(self, *args): #cannot find CLR method
        """ Persist(self: ObjectSecurity, name: str, includeSections: AccessControlSections)Persist(self: ObjectSecurity, handle: SafeHandle, includeSections: AccessControlSections)Persist(self: ObjectSecurity, enableOwnershipPrivilege: bool, name: str, includeSections: AccessControlSections) """
        ...

    def PurgeAccessRules(self, identity:IdentityReference): # -> 
        """ PurgeAccessRules(self: ObjectSecurity, identity: IdentityReference) """
        ...

    def PurgeAuditRules(self, identity:IdentityReference): # -> 
        """ PurgeAuditRules(self: ObjectSecurity, identity: IdentityReference) """
        ...

    def ReadLock(self, *args): #cannot find CLR method
        """ ReadLock(self: ObjectSecurity) """
        ...

    def ReadUnlock(self, *args): #cannot find CLR method
        """ ReadUnlock(self: ObjectSecurity) """
        ...

    def SetAccessRuleProtection(self, isProtected:bool, preserveInheritance:bool): # -> 
        """ SetAccessRuleProtection(self: ObjectSecurity, isProtected: bool, preserveInheritance: bool) """
        ...

    def SetAuditRuleProtection(self, isProtected:bool, preserveInheritance:bool): # -> 
        """ SetAuditRuleProtection(self: ObjectSecurity, isProtected: bool, preserveInheritance: bool) """
        ...

    def SetGroup(self, identity:IdentityReference): # -> 
        """ SetGroup(self: ObjectSecurity, identity: IdentityReference) """
        ...

    def SetOwner(self, identity:IdentityReference): # -> 
        """ SetOwner(self: ObjectSecurity, identity: IdentityReference) """
        ...

    def SetSecurityDescriptorBinaryForm(self, binaryForm:Array, includeSections:AccessControlSections = ...): # -> 
        """ SetSecurityDescriptorBinaryForm(self: ObjectSecurity, binaryForm: Array[Byte])SetSecurityDescriptorBinaryForm(self: ObjectSecurity, binaryForm: Array[Byte], includeSections: AccessControlSections) """
        ...

    def SetSecurityDescriptorSddlForm(self, sddlForm:str, includeSections:AccessControlSections = ...): # -> 
        """ SetSecurityDescriptorSddlForm(self: ObjectSecurity, sddlForm: str)SetSecurityDescriptorSddlForm(self: ObjectSecurity, sddlForm: str, includeSections: AccessControlSections) """
        ...

    def WriteLock(self, *args): #cannot find CLR method
        """ WriteLock(self: ObjectSecurity) """
        ...

    def WriteUnlock(self, *args): #cannot find CLR method
        """ WriteUnlock(self: ObjectSecurity) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, isContainer: bool, isDS: bool)
        __new__(cls: type, securityDescriptor: CommonSecurityDescriptor)
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class PrivilegeNotHeldException(UnauthorizedAccessException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrivilegeNotHeldException()
    PrivilegeNotHeldException(privilege: str)
    PrivilegeNotHeldException(privilege: str, inner: Exception)
    """
    @property
    def PrivilegeName(self) -> str:
        """ Get: PrivilegeName(self: PrivilegeNotHeldException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PrivilegeNotHeldException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PropagationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropagationFlags, values: InheritOnly (2), None (0), NoPropagateInherit (1) """
    InheritOnly: PropagationFlags = ...
    NoPropagateInherit: PropagationFlags = ...
    value__ = ...


class RawAcl(GenericAcl): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    RawAcl(revision: Byte, capacity: int)
    RawAcl(binaryForm: Array[Byte], offset: int)
    """
    def InsertAce(self, index:int, ace:GenericAce): # -> 
        """ InsertAce(self: RawAcl, index: int, ace: GenericAce) """
        ...

    def RemoveAce(self, index:int): # -> 
        """ RemoveAce(self: RawAcl, index: int) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, revision: Byte, capacity: int)
        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        ...


class RawSecurityDescriptor(GenericSecurityDescriptor): # skipped bases: <type 'object'>
    """
    RawSecurityDescriptor(flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)
    RawSecurityDescriptor(sddlForm: str)
    RawSecurityDescriptor(binaryForm: Array[Byte], offset: int)
    """
    @property
    def DiscretionaryAcl(self) -> RawAcl:
        """
        Get: DiscretionaryAcl(self: RawSecurityDescriptor) -> RawAcl
        Set: DiscretionaryAcl(self: RawSecurityDescriptor) = value
        """
        ...

    @property
    def ResourceManagerControl(self) -> Byte:
        """
        Get: ResourceManagerControl(self: RawSecurityDescriptor) -> Byte
        Set: ResourceManagerControl(self: RawSecurityDescriptor) = value
        """
        ...

    @property
    def SystemAcl(self) -> RawAcl:
        """
        Get: SystemAcl(self: RawSecurityDescriptor) -> RawAcl
        Set: SystemAcl(self: RawSecurityDescriptor) = value
        """
        ...


    def SetFlags(self, flags:ControlFlags): # -> 
        """ SetFlags(self: RawSecurityDescriptor, flags: ControlFlags) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, flags: ControlFlags, owner: SecurityIdentifier, group: SecurityIdentifier, systemAcl: RawAcl, discretionaryAcl: RawAcl)
        __new__(cls: type, sddlForm: str)
        __new__(cls: type, binaryForm: Array[Byte], offset: int)
        """
        ...


class RegistryAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, type: AccessControlType)
    RegistryAccessRule(identity: str, registryRights: RegistryRights, type: AccessControlType)
    RegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    RegistryAccessRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType)
    """
    @property
    def RegistryRights(self) -> RegistryRights:
        """ Get: RegistryRights(self: RegistryAccessRule) -> RegistryRights """
        ...



class RegistryAuditRule(AuditRule): # skipped bases: <type 'object'>
    """
    RegistryAuditRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    RegistryAuditRule(identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags)
    """
    @property
    def RegistryRights(self) -> RegistryRights:
        """ Get: RegistryRights(self: RegistryAuditRule) -> RegistryRights """
        ...



class RegistryRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistryRights, values: ChangePermissions (262144), CreateLink (32), CreateSubKey (4), Delete (65536), EnumerateSubKeys (8), ExecuteKey (131097), FullControl (983103), Notify (16), QueryValues (1), ReadKey (131097), ReadPermissions (131072), SetValue (2), TakeOwnership (524288), WriteKey (131078) """
    ChangePermissions: RegistryRights = ...
    CreateLink: RegistryRights = ...
    CreateSubKey: RegistryRights = ...
    Delete: RegistryRights = ...
    EnumerateSubKeys: RegistryRights = ...
    ExecuteKey: RegistryRights = ...
    FullControl: RegistryRights = ...
    Notify: RegistryRights = ...
    QueryValues: RegistryRights = ...
    ReadKey: RegistryRights = ...
    ReadPermissions: RegistryRights = ...
    SetValue: RegistryRights = ...
    TakeOwnership: RegistryRights = ...
    value__ = ...
    WriteKey: RegistryRights = ...


class RegistrySecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """ RegistrySecurity() """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: RegistrySecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: RegistrySecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: RegistrySecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: RegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class ResourceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResourceType, values: DSObject (8), DSObjectAll (9), FileObject (1), KernelObject (6), LMShare (5), Printer (3), ProviderDefined (10), RegistryKey (4), RegistryWow6432Key (12), Service (2), Unknown (0), WindowObject (7), WmiGuidObject (11) """
    DSObject: ResourceType = ...
    DSObjectAll: ResourceType = ...
    FileObject: ResourceType = ...
    KernelObject: ResourceType = ...
    LMShare: ResourceType = ...
    Printer: ResourceType = ...
    ProviderDefined: ResourceType = ...
    RegistryKey: ResourceType = ...
    RegistryWow6432Key: ResourceType = ...
    Service: ResourceType = ...
    Unknown: ResourceType = ...
    value__ = ...
    WindowObject: ResourceType = ...
    WmiGuidObject: ResourceType = ...


class SecurityInfos(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SecurityInfos, values: DiscretionaryAcl (4), Group (2), Owner (1), SystemAcl (8) """
    DiscretionaryAcl: SecurityInfos = ...
    Group: SecurityInfos = ...
    Owner: SecurityInfos = ...
    SystemAcl: SecurityInfos = ...
    value__ = ...


class SemaphoreAccessRule(AccessRule): # skipped bases: <type 'object'>
    """
    SemaphoreAccessRule(identity: IdentityReference, eventRights: SemaphoreRights, type: AccessControlType)
    SemaphoreAccessRule(identity: str, eventRights: SemaphoreRights, type: AccessControlType)
    """
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
        """ Get: SemaphoreRights(self: SemaphoreAccessRule) -> SemaphoreRights """
        ...



class SemaphoreAuditRule(AuditRule): # skipped bases: <type 'object'>
    """ SemaphoreAuditRule(identity: IdentityReference, eventRights: SemaphoreRights, flags: AuditFlags) """
    @property
    def SemaphoreRights(self) -> SemaphoreRights:
        """ Get: SemaphoreRights(self: SemaphoreAuditRule) -> SemaphoreRights """
        ...



class SemaphoreRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SemaphoreRights, values: ChangePermissions (262144), Delete (65536), FullControl (2031619), Modify (2), ReadPermissions (131072), Synchronize (1048576), TakeOwnership (524288) """
    ChangePermissions: SemaphoreRights = ...
    Delete: SemaphoreRights = ...
    FullControl: SemaphoreRights = ...
    Modify: SemaphoreRights = ...
    ReadPermissions: SemaphoreRights = ...
    Synchronize: SemaphoreRights = ...
    TakeOwnership: SemaphoreRights = ...
    value__ = ...


class SemaphoreSecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """
    SemaphoreSecurity()
    SemaphoreSecurity(name: str, includeSections: AccessControlSections)
    """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: SemaphoreSecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: SemaphoreSecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: SemaphoreSecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: SemaphoreSecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


class SystemAcl(CommonAcl): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SystemAcl(isContainer: bool, isDS: bool, capacity: int)
    SystemAcl(isContainer: bool, isDS: bool, revision: Byte, capacity: int)
    SystemAcl(isContainer: bool, isDS: bool, rawAcl: RawAcl)
    """
    def AddAudit(self, *__args): # -> 
        """ AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)AddAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)AddAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def RemoveAudit(self, *__args) -> bool:
        """
        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool
        RemoveAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule) -> bool
        RemoveAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) -> bool
        """
        ...

    def RemoveAuditSpecific(self, *__args): # -> 
        """ RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)RemoveAuditSpecific(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)RemoveAuditSpecific(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def SetAudit(self, *__args): # -> 
        """ SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags)SetAudit(self: SystemAcl, sid: SecurityIdentifier, rule: ObjectAuditRule)SetAudit(self: SystemAcl, auditFlags: AuditFlags, sid: SecurityIdentifier, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: Guid, inheritedObjectType: Guid) """
        ...

    def __new__(cls, isContainer:bool, isDS:bool, *__args:int) -> Self:
        """
        __new__(cls: type, isContainer: bool, isDS: bool, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, revision: Byte, capacity: int)
        __new__(cls: type, isContainer: bool, isDS: bool, rawAcl: RawAcl)
        """
        ...


