# encoding: utf-8
# module System.Management.Instrumentation calls itself Instrumentation
# from System.Management, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Management.Instrumentation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, Type

from System.Configuration.Install import Installer

from System.Reflection import Assembly

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IWbemProviderInit, IWbemServices, ManagementConfigurationType, 
    ManagementQualifierFlavors, field#)
"""

# no functions
# classes

class BaseEvent(IEvent): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DefaultManagementInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ DefaultManagementInstaller() """
    pass

class DefaultManagementProjectInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ DefaultManagementProjectInstaller() """
    pass

class IEvent: # skipped bases: <type 'object'>
    """ no doc """
    def Fire(self): # -> 
        """ Fire(self: IEvent) """
        ...


class IgnoreMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IgnoreMemberAttribute() """
    pass

class IInstance: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Published(self) -> bool:
        """
        Get: Published(self: IInstance) -> bool
        Set: Published(self: IInstance) = value
        """
        ...



class Instance(IInstance): # skipped bases: <type 'object'>
    """ no doc """
    pass

class InstrumentationBaseException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstrumentationBaseException()
    InstrumentationBaseException(message: str)
    InstrumentationBaseException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstrumentationException(InstrumentationBaseException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstrumentationException()
    InstrumentationException(message: str)
    InstrumentationException(innerException: Exception)
    InstrumentationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceNotFoundException(InstrumentationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceNotFoundException()
    InstanceNotFoundException(message: str)
    InstanceNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Instrumentation: # skipped bases: <type 'object'>, <type 'object'>
    """ Instrumentation() """
    @staticmethod
    def Fire(eventData:object): # -> 
        """ Fire(eventData: object) """
        ...

    @staticmethod
    def IsAssemblyRegistered(assemblyToRegister:Assembly) -> bool:
        """ IsAssemblyRegistered(assemblyToRegister: Assembly) -> bool """
        ...

    @staticmethod
    def Publish(instanceData:object): # -> 
        """ Publish(instanceData: object) """
        ...

    @staticmethod
    def RegisterAssembly(assemblyToRegister:Assembly): # -> 
        """ RegisterAssembly(assemblyToRegister: Assembly) """
        ...

    @staticmethod
    def Revoke(instanceData:object): # -> 
        """ Revoke(instanceData: object) """
        ...

    @staticmethod
    def SetBatchSize(instrumentationClass:Type, batchSize:int): # -> 
        """ SetBatchSize(instrumentationClass: Type, batchSize: int) """
        ...


class InstrumentationClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InstrumentationClassAttribute(instrumentationType: InstrumentationType)
    InstrumentationClassAttribute(instrumentationType: InstrumentationType, managedBaseClassName: str)
    """
    @property
    def InstrumentationType(self) -> InstrumentationType:
        """ Get: InstrumentationType(self: InstrumentationClassAttribute) -> InstrumentationType """
        ...

    @property
    def ManagedBaseClassName(self) -> str:
        """ Get: ManagedBaseClassName(self: InstrumentationClassAttribute) -> str """
        ...


    def __new__(cls, instrumentationType:InstrumentationType, managedBaseClassName:str = ...) -> Self:
        """
        __new__(cls: type, instrumentationType: InstrumentationType)
        __new__(cls: type, instrumentationType: InstrumentationType, managedBaseClassName: str)
        """
        ...


class InstrumentationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Publish(value:object): # -> 
        """ Publish(value: object) """
        ...

    @staticmethod
    def RegisterAssembly(managementAssembly:Assembly): # -> 
        """ RegisterAssembly(managementAssembly: Assembly) """
        ...

    @staticmethod
    def RegisterType(managementType:Type): # -> 
        """ RegisterType(managementType: Type) """
        ...

    @staticmethod
    def Revoke(value:object): # -> 
        """ Revoke(value: object) """
        ...

    @staticmethod
    def UnregisterAssembly(managementAssembly:Assembly): # -> 
        """ UnregisterAssembly(managementAssembly: Assembly) """
        ...

    @staticmethod
    def UnregisterType(managementType:Type): # -> 
        """ UnregisterType(managementType: Type) """
        ...

    __all__: list = ...


class InstrumentationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstrumentationType, values: Abstract (2), Event (1), Instance (0) """
    Abstract: InstrumentationType = ...
    Event: InstrumentationType = ...
    Instance: InstrumentationType = ...
    value__ = ...


class InstrumentedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InstrumentedAttribute()
    InstrumentedAttribute(namespaceName: str)
    InstrumentedAttribute(namespaceName: str, securityDescriptor: str)
    """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: InstrumentedAttribute) -> str """
        ...

    @property
    def SecurityDescriptor(self) -> str:
        """ Get: SecurityDescriptor(self: InstrumentedAttribute) -> str """
        ...


    def __new__(cls, namespaceName:str = ..., securityDescriptor:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, namespaceName: str)
        __new__(cls: type, namespaceName: str, securityDescriptor: str)
        """
        ...


class ManagedCommonProvider(IWbemServices, IWbemProviderInit): # skipped bases: <type 'object'>
    """ ManagedCommonProvider() """
    pass

class ManagedNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagedNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ManagedNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ManagementMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ManagementMemberAttribute) -> str
        Set: Name(self: ManagementMemberAttribute) = value
        """
        ...



class ManagementNewInstanceAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class ManagementBindAttribute(ManagementNewInstanceAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementBindAttribute() """
    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementBindAttribute) -> Type
        Set: Schema(self: ManagementBindAttribute) = value
        """
        ...



class ManagementCommitAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementCommitAttribute() """
    pass

class ManagementConfigurationAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementConfigurationAttribute() """
    @property
    def Mode(self): # -> ManagementConfigurationType
        """
        Get: Mode(self: ManagementConfigurationAttribute) -> ManagementConfigurationType
        Set: Mode(self: ManagementConfigurationAttribute) = value
        """
        ...

    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementConfigurationAttribute) -> Type
        Set: Schema(self: ManagementConfigurationAttribute) = value
        """
        ...



class ManagementConfigurationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ManagementConfigurationType, values: Apply (0), OnCommit (1) """
    Apply: ManagementConfigurationType = ...
    OnCommit: ManagementConfigurationType = ...
    value__ = ...


class ManagementCreateAttribute(ManagementNewInstanceAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementCreateAttribute() """
    pass

class ManagementEntityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementEntityAttribute() """
    @property
    def External(self) -> bool:
        """
        Get: External(self: ManagementEntityAttribute) -> bool
        Set: External(self: ManagementEntityAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ManagementEntityAttribute) -> str
        Set: Name(self: ManagementEntityAttribute) = value
        """
        ...

    @property
    def Singleton(self) -> bool:
        """
        Get: Singleton(self: ManagementEntityAttribute) -> bool
        Set: Singleton(self: ManagementEntityAttribute) = value
        """
        ...



class ManagementEnumeratorAttribute(ManagementNewInstanceAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementEnumeratorAttribute() """
    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementEnumeratorAttribute) -> Type
        Set: Schema(self: ManagementEnumeratorAttribute) = value
        """
        ...



class ManagementHostingModel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ManagementHostingModel, values: Decoupled (0), LocalService (2), LocalSystem (3), NetworkService (1) """
    Decoupled: ManagementHostingModel = ...
    LocalService: ManagementHostingModel = ...
    LocalSystem: ManagementHostingModel = ...
    NetworkService: ManagementHostingModel = ...
    value__ = ...


class ManagementInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ ManagementInstaller() """
    pass

class ManagementKeyAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementKeyAttribute() """
    pass

class ManagementNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ManagementNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ManagementProbeAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementProbeAttribute() """
    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementProbeAttribute) -> Type
        Set: Schema(self: ManagementProbeAttribute) = value
        """
        ...



class ManagementQualifierAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementQualifierAttribute(name: str) """
    @property
    def Flavor(self): # -> ManagementQualifierFlavors
        """
        Get: Flavor(self: ManagementQualifierAttribute) -> ManagementQualifierFlavors
        Set: Flavor(self: ManagementQualifierAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ManagementQualifierAttribute) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ManagementQualifierAttribute) -> object
        Set: Value(self: ManagementQualifierAttribute) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ManagementQualifierFlavors(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ManagementQualifierFlavors, values: Amended (1), ClassOnly (4), DisableOverride (2), ThisClassOnly (8) """
    Amended: ManagementQualifierFlavors = ...
    ClassOnly: ManagementQualifierFlavors = ...
    DisableOverride: ManagementQualifierFlavors = ...
    ThisClassOnly: ManagementQualifierFlavors = ...
    value__ = ...


class ManagementReferenceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementReferenceAttribute() """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: ManagementReferenceAttribute) -> str
        Set: Type(self: ManagementReferenceAttribute) = value
        """
        ...



class ManagementRemoveAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementRemoveAttribute() """
    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementRemoveAttribute) -> Type
        Set: Schema(self: ManagementRemoveAttribute) = value
        """
        ...



class ManagementTaskAttribute(ManagementMemberAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagementTaskAttribute() """
    @property
    def Schema(self) -> Type:
        """
        Get: Schema(self: ManagementTaskAttribute) -> Type
        Set: Schema(self: ManagementTaskAttribute) = value
        """
        ...



class WmiConfigurationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WmiConfigurationAttribute(scope: str) """
    @property
    def HostingGroup(self) -> str:
        """
        Get: HostingGroup(self: WmiConfigurationAttribute) -> str
        Set: HostingGroup(self: WmiConfigurationAttribute) = value
        """
        ...

    @property
    def HostingModel(self) -> ManagementHostingModel:
        """
        Get: HostingModel(self: WmiConfigurationAttribute) -> ManagementHostingModel
        Set: HostingModel(self: WmiConfigurationAttribute) = value
        """
        ...

    @property
    def IdentifyLevel(self) -> bool:
        """
        Get: IdentifyLevel(self: WmiConfigurationAttribute) -> bool
        Set: IdentifyLevel(self: WmiConfigurationAttribute) = value
        """
        ...

    @property
    def NamespaceSecurity(self) -> str:
        """
        Get: NamespaceSecurity(self: WmiConfigurationAttribute) -> str
        Set: NamespaceSecurity(self: WmiConfigurationAttribute) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """ Get: Scope(self: WmiConfigurationAttribute) -> str """
        ...

    @property
    def SecurityRestriction(self) -> str:
        """
        Get: SecurityRestriction(self: WmiConfigurationAttribute) -> str
        Set: SecurityRestriction(self: WmiConfigurationAttribute) = value
        """
        ...


    def __new__(cls, scope:str) -> Self:
        """ __new__(cls: type, scope: str) """
        ...


class WmiProviderInstallationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WmiProviderInstallationException()
    WmiProviderInstallationException(message: str)
    WmiProviderInstallationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


