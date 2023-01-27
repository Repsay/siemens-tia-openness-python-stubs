# encoding: utf-8
# module System.Configuration.Internal calls itself Internal
# from System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, EventArgs, IAsyncResult, 
    IDisposable, MulticastDelegate, Type)

from System.Configuration import (Configuration, ConfigurationAllowDefinition, 
    ConfigurationAllowExeDefinition, ConfigurationBuilder, 
    ConfigurationSection, ProtectedConfigurationProvider, 
    ProtectedConfigurationSection)

from System.IO import Stream

from System.Security import PermissionSet

from System.Xml import XmlNode

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class DelegatingConfigHost(IInternalConfigurationBuilderHost, IInternalConfigHost): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConfigBuilderHost(self):
        ...

    @property
    def Host(self):
        ...



class IConfigErrorInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Filename(self) -> str:
        """ Get: Filename(self: IConfigErrorInfo) -> str """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: IConfigErrorInfo) -> int """
        ...



class IConfigSystem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Host(self) -> IInternalConfigHost:
        """ Get: Host(self: IConfigSystem) -> IInternalConfigHost """
        ...

    @property
    def Root(self) -> IInternalConfigRoot:
        """ Get: Root(self: IConfigSystem) -> IInternalConfigRoot """
        ...


    def Init(self, typeConfigHost:Type, hostInitParams:Array): # -> 
        """ Init(self: IConfigSystem, typeConfigHost: Type, *hostInitParams: Array[object]) """
        ...


class IConfigurationManagerHelper: # skipped bases: <type 'object'>
    """ no doc """
    def EnsureNetConfigLoaded(self): # -> 
        """ EnsureNetConfigLoaded(self: IConfigurationManagerHelper) """
        ...


class IConfigurationManagerInternal: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationConfigUri(self) -> str:
        """ Get: ApplicationConfigUri(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeLocalConfigDirectory(self) -> str:
        """ Get: ExeLocalConfigDirectory(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeLocalConfigPath(self) -> str:
        """ Get: ExeLocalConfigPath(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeProductName(self) -> str:
        """ Get: ExeProductName(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeProductVersion(self) -> str:
        """ Get: ExeProductVersion(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeRoamingConfigDirectory(self) -> str:
        """ Get: ExeRoamingConfigDirectory(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def ExeRoamingConfigPath(self) -> str:
        """ Get: ExeRoamingConfigPath(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def MachineConfigPath(self) -> str:
        """ Get: MachineConfigPath(self: IConfigurationManagerInternal) -> str """
        ...

    @property
    def SetConfigurationSystemInProgress(self) -> bool:
        """ Get: SetConfigurationSystemInProgress(self: IConfigurationManagerInternal) -> bool """
        ...

    @property
    def SupportsUserConfig(self) -> bool:
        """ Get: SupportsUserConfig(self: IConfigurationManagerInternal) -> bool """
        ...

    @property
    def UserConfigFilename(self) -> str:
        """ Get: UserConfigFilename(self: IConfigurationManagerInternal) -> str """
        ...



class IInternalConfigClientHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetExeConfigPath(self) -> str:
        """ GetExeConfigPath(self: IInternalConfigClientHost) -> str """
        ...

    def GetLocalUserConfigPath(self) -> str:
        """ GetLocalUserConfigPath(self: IInternalConfigClientHost) -> str """
        ...

    def GetRoamingUserConfigPath(self) -> str:
        """ GetRoamingUserConfigPath(self: IInternalConfigClientHost) -> str """
        ...

    def IsExeConfig(self, configPath:str) -> bool:
        """ IsExeConfig(self: IInternalConfigClientHost, configPath: str) -> bool """
        ...

    def IsLocalUserConfig(self, configPath:str) -> bool:
        """ IsLocalUserConfig(self: IInternalConfigClientHost, configPath: str) -> bool """
        ...

    def IsRoamingUserConfig(self, configPath:str) -> bool:
        """ IsRoamingUserConfig(self: IInternalConfigClientHost, configPath: str) -> bool """
        ...


class IInternalConfigConfigurationFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, typeConfigHost:Type, hostInitConfigurationParams:Array) -> Configuration:
        """ Create(self: IInternalConfigConfigurationFactory, typeConfigHost: Type, *hostInitConfigurationParams: Array[object]) -> Configuration """
        ...

    def NormalizeLocationSubPath(self, subPath:str, errorInfo:IConfigErrorInfo) -> str:
        """ NormalizeLocationSubPath(self: IInternalConfigConfigurationFactory, subPath: str, errorInfo: IConfigErrorInfo) -> str """
        ...


class IInternalConfigHost: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsRemote(self) -> bool:
        """ Get: IsRemote(self: IInternalConfigHost) -> bool """
        ...

    @property
    def SupportsChangeNotifications(self) -> bool:
        """ Get: SupportsChangeNotifications(self: IInternalConfigHost) -> bool """
        ...

    @property
    def SupportsLocation(self) -> bool:
        """ Get: SupportsLocation(self: IInternalConfigHost) -> bool """
        ...

    @property
    def SupportsPath(self) -> bool:
        """ Get: SupportsPath(self: IInternalConfigHost) -> bool """
        ...

    @property
    def SupportsRefresh(self) -> bool:
        """ Get: SupportsRefresh(self: IInternalConfigHost) -> bool """
        ...


    def CreateConfigurationContext(self, configPath:str, locationSubPath:str) -> object:
        """ CreateConfigurationContext(self: IInternalConfigHost, configPath: str, locationSubPath: str) -> object """
        ...

    def CreateDeprecatedConfigContext(self, configPath:str) -> object:
        """ CreateDeprecatedConfigContext(self: IInternalConfigHost, configPath: str) -> object """
        ...

    def DecryptSection(self, encryptedXml:str, protectionProvider:ProtectedConfigurationProvider, protectedConfigSection:ProtectedConfigurationSection) -> str:
        """ DecryptSection(self: IInternalConfigHost, encryptedXml: str, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> str """
        ...

    def DeleteStream(self, streamName:str): # -> 
        """ DeleteStream(self: IInternalConfigHost, streamName: str) """
        ...

    def EncryptSection(self, clearTextXml:str, protectionProvider:ProtectedConfigurationProvider, protectedConfigSection:ProtectedConfigurationSection) -> str:
        """ EncryptSection(self: IInternalConfigHost, clearTextXml: str, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> str """
        ...

    def GetConfigPathFromLocationSubPath(self, configPath:str, locationSubPath:str) -> str:
        """ GetConfigPathFromLocationSubPath(self: IInternalConfigHost, configPath: str, locationSubPath: str) -> str """
        ...

    def GetConfigType(self, typeName:str, throwOnError:bool) -> Type:
        """ GetConfigType(self: IInternalConfigHost, typeName: str, throwOnError: bool) -> Type """
        ...

    def GetConfigTypeName(self, t:Type) -> str:
        """ GetConfigTypeName(self: IInternalConfigHost, t: Type) -> str """
        ...

    def GetRestrictedPermissions(self, configRecord, permissionSet, isHostReady) -> Tuple_[PermissionSet, bool]:
        """ GetRestrictedPermissions(self: IInternalConfigHost, configRecord: IInternalConfigRecord) -> (PermissionSet, bool) """
        ...

    def GetStreamName(self, configPath:str) -> str:
        """ GetStreamName(self: IInternalConfigHost, configPath: str) -> str """
        ...

    def GetStreamNameForConfigSource(self, streamName:str, configSource:str) -> str:
        """ GetStreamNameForConfigSource(self: IInternalConfigHost, streamName: str, configSource: str) -> str """
        ...

    def GetStreamVersion(self, streamName:str) -> object:
        """ GetStreamVersion(self: IInternalConfigHost, streamName: str) -> object """
        ...

    def Impersonate(self) -> IDisposable:
        """ Impersonate(self: IInternalConfigHost) -> IDisposable """
        ...

    def Init(self, configRoot:IInternalConfigRoot, hostInitParams:Array): # -> 
        """ Init(self: IInternalConfigHost, configRoot: IInternalConfigRoot, *hostInitParams: Array[object]) """
        ...

    def InitForConfiguration(self, locationSubPath, configPath, locationConfigPath, configRoot, hostInitConfigurationParams) -> Tuple_[str, str, str]:
        """ InitForConfiguration(self: IInternalConfigHost, locationSubPath: str, configRoot: IInternalConfigRoot, *hostInitConfigurationParams: Array[object]) -> (str, str, str) """
        ...

    def IsAboveApplication(self, configPath:str) -> bool:
        """ IsAboveApplication(self: IInternalConfigHost, configPath: str) -> bool """
        ...

    def IsConfigRecordRequired(self, configPath:str) -> bool:
        """ IsConfigRecordRequired(self: IInternalConfigHost, configPath: str) -> bool """
        ...

    def IsDefinitionAllowed(self, configPath:str, allowDefinition:ConfigurationAllowDefinition, allowExeDefinition:ConfigurationAllowExeDefinition) -> bool:
        """ IsDefinitionAllowed(self: IInternalConfigHost, configPath: str, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition) -> bool """
        ...

    def IsFile(self, streamName:str) -> bool:
        """ IsFile(self: IInternalConfigHost, streamName: str) -> bool """
        ...

    def IsFullTrustSectionWithoutAptcaAllowed(self, configRecord:IInternalConfigRecord) -> bool:
        """ IsFullTrustSectionWithoutAptcaAllowed(self: IInternalConfigHost, configRecord: IInternalConfigRecord) -> bool """
        ...

    def IsInitDelayed(self, configRecord:IInternalConfigRecord) -> bool:
        """ IsInitDelayed(self: IInternalConfigHost, configRecord: IInternalConfigRecord) -> bool """
        ...

    def IsLocationApplicable(self, configPath:str) -> bool:
        """ IsLocationApplicable(self: IInternalConfigHost, configPath: str) -> bool """
        ...

    def IsSecondaryRoot(self, configPath:str) -> bool:
        """ IsSecondaryRoot(self: IInternalConfigHost, configPath: str) -> bool """
        ...

    def IsTrustedConfigPath(self, configPath:str) -> bool:
        """ IsTrustedConfigPath(self: IInternalConfigHost, configPath: str) -> bool """
        ...

    def OpenStreamForRead(self, streamName:str, assertPermissions:bool = ...) -> Stream:
        """
        OpenStreamForRead(self: IInternalConfigHost, streamName: str) -> Stream
        OpenStreamForRead(self: IInternalConfigHost, streamName: str, assertPermissions: bool) -> Stream
        """
        ...

    def OpenStreamForWrite(self, streamName:str, templateStreamName:str, writeContext:object, assertPermissions:bool = ...) -> Tuple_[Stream, object]:
        """
        OpenStreamForWrite(self: IInternalConfigHost, streamName: str, templateStreamName: str, writeContext: object) -> (Stream, object)
        OpenStreamForWrite(self: IInternalConfigHost, streamName: str, templateStreamName: str, writeContext: object, assertPermissions: bool) -> (Stream, object)
        """
        ...

    def PrefetchAll(self, configPath:str, streamName:str) -> bool:
        """ PrefetchAll(self: IInternalConfigHost, configPath: str, streamName: str) -> bool """
        ...

    def PrefetchSection(self, sectionGroupName:str, sectionName:str) -> bool:
        """ PrefetchSection(self: IInternalConfigHost, sectionGroupName: str, sectionName: str) -> bool """
        ...

    def RequireCompleteInit(self, configRecord:IInternalConfigRecord): # -> 
        """ RequireCompleteInit(self: IInternalConfigHost, configRecord: IInternalConfigRecord) """
        ...

    def StartMonitoringStreamForChanges(self, streamName:str, callback:StreamChangeCallback) -> object:
        """ StartMonitoringStreamForChanges(self: IInternalConfigHost, streamName: str, callback: StreamChangeCallback) -> object """
        ...

    def StopMonitoringStreamForChanges(self, streamName:str, callback:StreamChangeCallback): # -> 
        """ StopMonitoringStreamForChanges(self: IInternalConfigHost, streamName: str, callback: StreamChangeCallback) """
        ...

    def VerifyDefinitionAllowed(self, configPath:str, allowDefinition:ConfigurationAllowDefinition, allowExeDefinition:ConfigurationAllowExeDefinition, errorInfo:IConfigErrorInfo): # -> 
        """ VerifyDefinitionAllowed(self: IInternalConfigHost, configPath: str, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition, errorInfo: IConfigErrorInfo) """
        ...

    def WriteCompleted(self, streamName:str, success:bool, writeContext:object, assertPermissions:bool = ...): # -> 
        """ WriteCompleted(self: IInternalConfigHost, streamName: str, success: bool, writeContext: object)WriteCompleted(self: IInternalConfigHost, streamName: str, success: bool, writeContext: object, assertPermissions: bool) """
        ...


class IInternalConfigRecord: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConfigPath(self) -> str:
        """ Get: ConfigPath(self: IInternalConfigRecord) -> str """
        ...

    @property
    def HasInitErrors(self) -> bool:
        """ Get: HasInitErrors(self: IInternalConfigRecord) -> bool """
        ...

    @property
    def StreamName(self) -> str:
        """ Get: StreamName(self: IInternalConfigRecord) -> str """
        ...


    def GetLkgSection(self, configKey:str) -> object:
        """ GetLkgSection(self: IInternalConfigRecord, configKey: str) -> object """
        ...

    def GetSection(self, configKey:str) -> object:
        """ GetSection(self: IInternalConfigRecord, configKey: str) -> object """
        ...

    def RefreshSection(self, configKey:str): # -> 
        """ RefreshSection(self: IInternalConfigRecord, configKey: str) """
        ...

    def Remove(self): # -> 
        """ Remove(self: IInternalConfigRecord) """
        ...

    def ThrowIfInitErrors(self): # -> 
        """ ThrowIfInitErrors(self: IInternalConfigRecord) """
        ...


class IInternalConfigRoot: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDesignTime(self) -> bool:
        """ Get: IsDesignTime(self: IInternalConfigRoot) -> bool """
        ...


    def GetConfigRecord(self, configPath:str) -> IInternalConfigRecord:
        """ GetConfigRecord(self: IInternalConfigRoot, configPath: str) -> IInternalConfigRecord """
        ...

    def GetSection(self, section:str, configPath:str) -> object:
        """ GetSection(self: IInternalConfigRoot, section: str, configPath: str) -> object """
        ...

    def GetUniqueConfigPath(self, configPath:str) -> str:
        """ GetUniqueConfigPath(self: IInternalConfigRoot, configPath: str) -> str """
        ...

    def GetUniqueConfigRecord(self, configPath:str) -> IInternalConfigRecord:
        """ GetUniqueConfigRecord(self: IInternalConfigRoot, configPath: str) -> IInternalConfigRecord """
        ...

    def Init(self, host:IInternalConfigHost, isDesignTime:bool): # -> 
        """ Init(self: IInternalConfigRoot, host: IInternalConfigHost, isDesignTime: bool) """
        ...

    def RemoveConfig(self, configPath:str): # -> 
        """ RemoveConfig(self: IInternalConfigRoot, configPath: str) """
        ...

    ConfigChanged = ...
    ConfigRemoved = ...


class IInternalConfigSettingsFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CompleteInit(self): # -> 
        """ CompleteInit(self: IInternalConfigSettingsFactory) """
        ...

    def SetConfigurationSystem(self, internalConfigSystem:IInternalConfigSystem, initComplete:bool): # -> 
        """ SetConfigurationSystem(self: IInternalConfigSettingsFactory, internalConfigSystem: IInternalConfigSystem, initComplete: bool) """
        ...


class IInternalConfigSystem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SupportsUserConfig(self) -> bool:
        """ Get: SupportsUserConfig(self: IInternalConfigSystem) -> bool """
        ...


    def GetSection(self, configKey:str) -> object:
        """ GetSection(self: IInternalConfigSystem, configKey: str) -> object """
        ...

    def RefreshConfig(self, sectionName:str): # -> 
        """ RefreshConfig(self: IInternalConfigSystem, sectionName: str) """
        ...


class IInternalConfigurationBuilderHost: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessConfigurationSection(self, configSection:ConfigurationSection, builder:ConfigurationBuilder) -> ConfigurationSection:
        """ ProcessConfigurationSection(self: IInternalConfigurationBuilderHost, configSection: ConfigurationSection, builder: ConfigurationBuilder) -> ConfigurationSection """
        ...

    def ProcessRawXml(self, rawXml:XmlNode, builder:ConfigurationBuilder) -> XmlNode:
        """ ProcessRawXml(self: IInternalConfigurationBuilderHost, rawXml: XmlNode, builder: ConfigurationBuilder) -> XmlNode """
        ...


class InternalConfigEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InternalConfigEventArgs(configPath: str) """
    @property
    def ConfigPath(self) -> str:
        """
        Get: ConfigPath(self: InternalConfigEventArgs) -> str
        Set: ConfigPath(self: InternalConfigEventArgs) = value
        """
        ...


    def __new__(cls, configPath:str) -> Self:
        """ __new__(cls: type, configPath: str) """
        ...


class InternalConfigEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InternalConfigEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InternalConfigEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InternalConfigEventHandler, sender: object, e: InternalConfigEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InternalConfigEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InternalConfigEventArgs): # -> 
        """ Invoke(self: InternalConfigEventHandler, sender: object, e: InternalConfigEventArgs) """
        ...


class StreamChangeCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StreamChangeCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, streamName:str, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StreamChangeCallback, streamName: str, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StreamChangeCallback, result: IAsyncResult) """
        ...

    def Invoke(self, streamName:str): # -> 
        """ Invoke(self: StreamChangeCallback, streamName: str) """
        ...


