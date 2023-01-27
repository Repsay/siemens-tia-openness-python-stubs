# encoding: utf-8
# module Microsoft.PowerShell calls itself PowerShell
# from Microsoft.PowerShell.ConsoleHost, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Management, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Utility, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Security, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Diagnostics, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Guid, Int64, UInt32

from System.Management.Automation import (AuthorizationManager, PSInstaller, 
    PSObject, PSSnapIn, PSTypeConverter)

from System.Management.Automation.Runspaces import RunspaceConfiguration

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AdapterCodeMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ConvertDNWithBinaryToString(deInstance:PSObject, dnWithBinaryInstance:PSObject) -> str:
        """ ConvertDNWithBinaryToString(deInstance: PSObject, dnWithBinaryInstance: PSObject) -> str """
        ...

    @staticmethod
    def ConvertLargeIntegerToInt64(deInstance:PSObject, largeIntegerInstance:PSObject) -> Int64:
        """ ConvertLargeIntegerToInt64(deInstance: PSObject, largeIntegerInstance: PSObject) -> Int64 """
        ...

    __all__: list = ...


class ConsoleShell: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Start(configuration:RunspaceConfiguration, bannerText:str, helpText:str, args:Array) -> int:
        """ Start(configuration: RunspaceConfiguration, bannerText: str, helpText: str, args: Array[str]) -> int """
        ...

    __all__: list = ...


class DeserializingTypeConverter(PSTypeConverter): # skipped bases: <type 'object'>
    """ DeserializingTypeConverter() """
    @staticmethod
    def GetFormatViewDefinitionInstanceId(instance:PSObject) -> Guid:
        """ GetFormatViewDefinitionInstanceId(instance: PSObject) -> Guid """
        ...

    @staticmethod
    def GetInvocationInfo(instance:PSObject) -> PSObject:
        """ GetInvocationInfo(instance: PSObject) -> PSObject """
        ...

    @staticmethod
    def GetParameterSetMetadataFlags(instance:PSObject) -> UInt32:
        """ GetParameterSetMetadataFlags(instance: PSObject) -> UInt32 """
        ...


class EngineInstaller(PSInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ EngineInstaller() """
    pass

class ExecutionPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExecutionPolicy, values: AllSigned (2), Bypass (4), Default (3), RemoteSigned (1), Restricted (3), Undefined (5), Unrestricted (0) """
    AllSigned: ExecutionPolicy = ...
    Bypass: ExecutionPolicy = ...
    Default: ExecutionPolicy = ...
    RemoteSigned: ExecutionPolicy = ...
    Restricted: ExecutionPolicy = ...
    Undefined: ExecutionPolicy = ...
    Unrestricted: ExecutionPolicy = ...
    value__ = ...


class ExecutionPolicyScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExecutionPolicyScope, values: CurrentUser (1), LocalMachine (2), MachinePolicy (4), Process (0), UserPolicy (3) """
    CurrentUser: ExecutionPolicyScope = ...
    LocalMachine: ExecutionPolicyScope = ...
    MachinePolicy: ExecutionPolicyScope = ...
    Process: ExecutionPolicyScope = ...
    UserPolicy: ExecutionPolicyScope = ...
    value__ = ...


class PSAuthorizationManager(AuthorizationManager): # skipped bases: <type 'object'>
    """ PSAuthorizationManager(shellId: str) """
    pass

class PSCorePSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PSCorePSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSCorePSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSCorePSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSCorePSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSCorePSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSCorePSSnapIn) -> str """
        ...



class PSHostPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PSHostPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSHostPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSHostPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSHostPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSHostPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSHostPSSnapIn) -> str """
        ...



class PSManagementPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PSManagementPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSManagementPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSManagementPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSManagementPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSManagementPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSManagementPSSnapIn) -> str """
        ...



class PSSecurityPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PSSecurityPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSSecurityPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSSecurityPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSSecurityPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSSecurityPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSSecurityPSSnapIn) -> str """
        ...



class PSUtilityPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PSUtilityPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSUtilityPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSUtilityPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSUtilityPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSUtilityPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSUtilityPSSnapIn) -> str """
        ...



class ToStringCodeMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def PropertyValueCollection(instance:PSObject) -> str:
        """ PropertyValueCollection(instance: PSObject) -> str """
        ...

    @staticmethod
    def Type(instance:PSObject) -> str:
        """ Type(instance: PSObject) -> str """
        ...

    @staticmethod
    def XmlNode(instance:PSObject) -> str:
        """ XmlNode(instance: PSObject) -> str """
        ...

    @staticmethod
    def XmlNodeList(instance:PSObject) -> str:
        """ XmlNodeList(instance: PSObject) -> str """
        ...

    __all__: list = ...


class UnmanagedPSEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ UnmanagedPSEntry() """
    def Start(self, consoleFilePath:str, args:Array) -> int:
        """ Start(self: UnmanagedPSEntry, consoleFilePath: str, args: Array[str]) -> int """
        ...


# variables with complex values

