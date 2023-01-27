# encoding: utf-8
# module Microsoft.PowerShell.Commands.Internal calls itself Internal
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32 import (RegistryKeyPermissionCheck, RegistryValueKind, 
    RegistryValueOptions)

from System import Array, IDisposable, MarshalByRefObject, Type

from System.Security.AccessControl import (AccessControlSections, 
    AccessControlType, AccessRule, AuditFlags, AuditRule, InheritanceFlags, 
    NativeObjectSecurity, PropagationFlags, RegistryRights)

from System.Security.Principal import IdentityReference


# no functions
# classes

class RemotingErrorResources: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CouldNotResolveRoleDefinitionPrincipal(self) -> str:
        """ Get: CouldNotResolveRoleDefinitionPrincipal() -> str """
        ...

    @property
    def WinRMRestartWarning(self) -> str:
        """ Get: WinRMRestartWarning() -> str """
        ...


    __all__: list = ...


class TransactedRegistryAccessRule(AccessRule): # skipped bases: <type 'object'>
    """ TransactedRegistryAccessRule(identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) """
    @property
    def RegistryRights(self) -> RegistryRights:
        """ Get: RegistryRights(self: TransactedRegistryAccessRule) -> RegistryRights """
        ...



class TransactedRegistryAuditRule(AuditRule): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RegistryRights(self) -> RegistryRights:
        """ Get: RegistryRights(self: TransactedRegistryAuditRule) -> RegistryRights """
        ...



class TransactedRegistryKey(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: TransactedRegistryKey) -> str """
        ...

    @property
    def SubKeyCount(self) -> int:
        """ Get: SubKeyCount(self: TransactedRegistryKey) -> int """
        ...

    @property
    def ValueCount(self) -> int:
        """ Get: ValueCount(self: TransactedRegistryKey) -> int """
        ...


    def Close(self): # -> 
        """ Close(self: TransactedRegistryKey) """
        ...

    def CreateSubKey(self, subkey:str, permissionCheck:RegistryKeyPermissionCheck = ..., registrySecurity:TransactedRegistrySecurity = ...) -> TransactedRegistryKey:
        """
        CreateSubKey(self: TransactedRegistryKey, subkey: str) -> TransactedRegistryKey
        CreateSubKey(self: TransactedRegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> TransactedRegistryKey
        CreateSubKey(self: TransactedRegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: TransactedRegistrySecurity) -> TransactedRegistryKey
        """
        ...

    def DeleteSubKey(self, subkey:str, throwOnMissingSubKey:bool = ...): # -> 
        """ DeleteSubKey(self: TransactedRegistryKey, subkey: str)DeleteSubKey(self: TransactedRegistryKey, subkey: str, throwOnMissingSubKey: bool) """
        ...

    def DeleteSubKeyTree(self, subkey:str): # -> 
        """ DeleteSubKeyTree(self: TransactedRegistryKey, subkey: str) """
        ...

    def DeleteValue(self, name:str, throwOnMissingValue:bool = ...): # -> 
        """ DeleteValue(self: TransactedRegistryKey, name: str)DeleteValue(self: TransactedRegistryKey, name: str, throwOnMissingValue: bool) """
        ...

    def Flush(self): # -> 
        """ Flush(self: TransactedRegistryKey) """
        ...

    def GetAccessControl(self, includeSections:AccessControlSections = ...) -> TransactedRegistrySecurity:
        """
        GetAccessControl(self: TransactedRegistryKey) -> TransactedRegistrySecurity
        GetAccessControl(self: TransactedRegistryKey, includeSections: AccessControlSections) -> TransactedRegistrySecurity
        """
        ...

    def GetSubKeyNames(self) -> Array:
        """ GetSubKeyNames(self: TransactedRegistryKey) -> Array[str] """
        ...

    def GetValue(self, name:str, defaultValue:object = ..., options:RegistryValueOptions = ...) -> object:
        """
        GetValue(self: TransactedRegistryKey, name: str) -> object
        GetValue(self: TransactedRegistryKey, name: str, defaultValue: object) -> object
        GetValue(self: TransactedRegistryKey, name: str, defaultValue: object, options: RegistryValueOptions) -> object
        """
        ...

    def GetValueKind(self, name:str) -> RegistryValueKind:
        """ GetValueKind(self: TransactedRegistryKey, name: str) -> RegistryValueKind """
        ...

    def GetValueNames(self) -> Array:
        """ GetValueNames(self: TransactedRegistryKey) -> Array[str] """
        ...

    def OpenSubKey(self, name:str, *__args:bool) -> TransactedRegistryKey:
        """
        OpenSubKey(self: TransactedRegistryKey, name: str, writable: bool) -> TransactedRegistryKey
        OpenSubKey(self: TransactedRegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck) -> TransactedRegistryKey
        OpenSubKey(self: TransactedRegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> TransactedRegistryKey
        OpenSubKey(self: TransactedRegistryKey, name: str) -> TransactedRegistryKey
        """
        ...

    def SetAccessControl(self, registrySecurity:TransactedRegistrySecurity): # -> 
        """ SetAccessControl(self: TransactedRegistryKey, registrySecurity: TransactedRegistrySecurity) """
        ...

    def SetValue(self, name:str, value:object, valueKind:RegistryValueKind = ...): # -> 
        """ SetValue(self: TransactedRegistryKey, name: str, value: object)SetValue(self: TransactedRegistryKey, name: str, value: object, valueKind: RegistryValueKind) """
        ...

    def ToString(self) -> str:
        """ ToString(self: TransactedRegistryKey) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class TransactedRegistrySecurity(NativeObjectSecurity): # skipped bases: <type 'object'>
    """ TransactedRegistrySecurity() """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: TransactedRegistrySecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: TransactedRegistrySecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: TransactedRegistrySecurity) -> Type """
        ...


    def AccessRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, type:AccessControlType) -> AccessRule:
        """ AccessRuleFactory(self: TransactedRegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule """
        ...

    def AuditRuleFactory(self, identityReference:IdentityReference, accessMask:int, isInherited:bool, inheritanceFlags:InheritanceFlags, propagationFlags:PropagationFlags, flags:AuditFlags) -> AuditRule:
        """ AuditRuleFactory(self: TransactedRegistrySecurity, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule """
        ...


# variables with complex values

