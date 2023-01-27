# encoding: utf-8
# module Microsoft.DataWarehouse.Interfaces calls itself Interfaces
# from Microsoft.DataWarehouse.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Vbe.Interop.Forms import Control

from System import (Array, AsyncCallback, Enum, Guid, IAsyncResult, 
    IServiceProvider, MulticastDelegate, UInt16, UInt32, UIntPtr)

from System.ComponentModel.Design import CommandID, MenuCommand

from System.Reflection import AssemblyName

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IDbConnection, field#)
"""

# no functions
# classes

class ConfigurationSettingsChangedEventArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ ConfigurationSettingsChangedEventArgs(settingName: str) """
    @property
    def SettingName(self) -> str:
        """ Get: SettingName(self: ConfigurationSettingsChangedEventArgs) -> str """
        ...



class ConfigurationSettingsChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ConfigurationSettingsChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ConfigurationSettingsChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ConfigurationSettingsChangedEventHandler, sender: object, e: ConfigurationSettingsChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ConfigurationSettingsChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ConfigurationSettingsChangedEventArgs): # -> 
        """ Invoke(self: ConfigurationSettingsChangedEventHandler, sender: object, e: ConfigurationSettingsChangedEventArgs) """
        ...


class DataSourceDescriptorPropertyChangedEventArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ DataSourceDescriptorPropertyChangedEventArgs(name: str, oldValue: object, newValue: object) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DataSourceDescriptorPropertyChangedEventArgs) -> str """
        ...

    @property
    def NewValue(self) -> object:
        """ Get: NewValue(self: DataSourceDescriptorPropertyChangedEventArgs) -> object """
        ...

    @property
    def OldValue(self) -> object:
        """ Get: OldValue(self: DataSourceDescriptorPropertyChangedEventArgs) -> object """
        ...



class DataSourceDescriptorPropertyChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataSourceDescriptorPropertyChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataSourceDescriptorPropertyChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataSourceDescriptorPropertyChangedEventHandler, sender: object, e: DataSourceDescriptorPropertyChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataSourceDescriptorPropertyChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataSourceDescriptorPropertyChangedEventArgs): # -> 
        """ Invoke(self: DataSourceDescriptorPropertyChangedEventHandler, sender: object, e: DataSourceDescriptorPropertyChangedEventArgs) """
        ...


class DataSourceKinds: # skipped bases: <type 'object'>, <type 'object'>
    """ DataSourceKinds() """
    AnalysisServices: Guid = ...
    ConnectedDataSource: Guid = ...
    DataTransformations: Guid = ...
    ObjectModel: Guid = ...
    Reports: Guid = ...


class DwObjectKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DwObjectKind, values: AnalysisServices (1), AnalysisServicesViewers (257), DataTransformationServices (2), DataTransformationServicesViewers (258) """
    AnalysisServices: DwObjectKind = ...
    AnalysisServicesViewers: DwObjectKind = ...
    DataTransformationServices: DwObjectKind = ...
    DataTransformationServicesViewers: DwObjectKind = ...
    value__ = ...


class ICommandTarget: # skipped bases: <type 'object'>
    """ no doc """
    def InvokeCommand(self, menuCommand:MenuCommand) -> bool:
        """ InvokeCommand(self: ICommandTarget, menuCommand: MenuCommand) -> bool """
        ...

    def ProvideStatusForCommand(self, menuCommand:MenuCommand) -> bool:
        """ ProvideStatusForCommand(self: ICommandTarget, menuCommand: MenuCommand) -> bool """
        ...


class ICommandTargetMenuService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RootCommandTarget(self) -> ICommandTarget:
        """
        Get: RootCommandTarget(self: ICommandTargetMenuService) -> ICommandTarget
        Set: RootCommandTarget(self: ICommandTargetMenuService) = value
        """
        ...


    def GetCommandInfo(self, commandId, menuCommand) -> Tuple_[bool, MenuCommand]:
        """ GetCommandInfo(self: ICommandTargetMenuService, commandId: CommandID) -> (bool, MenuCommand) """
        ...

    def InvokeCommand(self, commandID:CommandID) -> bool:
        """ InvokeCommand(self: ICommandTargetMenuService, commandID: CommandID) -> bool """
        ...

    def ShowContextMenu(self, menuID:CommandID, x:int, y:int): # -> 
        """ ShowContextMenu(self: ICommandTargetMenuService, menuID: CommandID, x: int, y: int) """
        ...


class IConfigurationSettings: # skipped bases: <type 'object'>
    """ no doc """
    def GetSetting(self, settingName:str, indexes:Array = ...) -> object:
        """
        GetSetting(self: IConfigurationSettings, settingName: str) -> object
        GetSetting(self: IConfigurationSettings, settingName: str, *indexes: Array[str]) -> object
        """
        ...

    def OnSettingChanged(self, settingName:str): # -> 
        """ OnSettingChanged(self: IConfigurationSettings, settingName: str) """
        ...

    def SetSetting(self, settingName:str, settingValue:object, indexes:Array = ...): # -> 
        """ SetSetting(self: IConfigurationSettings, settingName: str, settingValue: object)SetSetting(self: IConfigurationSettings, settingName: str, settingValue: object, *indexes: Array[str]) """
        ...

    SettingChanged = ...


class IConfigurationSettings2(IConfigurationSettings): # skipped bases: <type 'object'>
    """ no doc """
    def GetActiveConfigurationName(self) -> str:
        """ GetActiveConfigurationName(self: IConfigurationSettings2) -> str """
        ...

    def GetConfigurationOptions(self) -> Array:
        """ GetConfigurationOptions(self: IConfigurationSettings2) -> Array[KeyValuePair[str, object]] """
        ...

    def GetSpecificSetting(self, configName:str, collectionName:str, nestedId:Array = ...) -> object:
        """
        GetSpecificSetting(self: IConfigurationSettings2, configName: str, collectionName: str, *nestedId: Array[str]) -> object
        GetSpecificSetting(self: IConfigurationSettings2, configName: str, collectionName: str) -> object
        """
        ...

    def MoveAllSettings(self, collectionName:str, newCollectionName:str, transformConfogurationValueCallback:TransformConfigurationValueCallback, nestedId:Array): # -> 
        """ MoveAllSettings(self: IConfigurationSettings2, collectionName: str, newCollectionName: str, transformConfogurationValueCallback: TransformConfigurationValueCallback, *nestedId: Array[str]) """
        ...

    def RemoveActiveSetting(self, collectionName:str, nestedId:Array): # -> 
        """ RemoveActiveSetting(self: IConfigurationSettings2, collectionName: str, *nestedId: Array[str]) """
        ...

    def RemoveAllSettings(self, collectionName:str, nestedId:Array): # -> 
        """ RemoveAllSettings(self: IConfigurationSettings2, collectionName: str, *nestedId: Array[str]) """
        ...

    def RenameAllSettings(self, collectionName:str, newConfigurationSettingName:str, nestedId:Array): # -> 
        """ RenameAllSettings(self: IConfigurationSettings2, collectionName: str, newConfigurationSettingName: str, *nestedId: Array[str]) """
        ...

    def SetActiveSetting(self, collectionName:str, configurationSettingValue:object, configurationSettingName:str, nestedId:Array): # -> 
        """ SetActiveSetting(self: IConfigurationSettings2, collectionName: str, configurationSettingValue: object, configurationSettingName: str, *nestedId: Array[str]) """
        ...

    def SetAllSettings(self, collectionName:str, configurationSettingValue:object, configurationSettingName:str, nestedId:Array): # -> 
        """ SetAllSettings(self: IConfigurationSettings2, collectionName: str, configurationSettingValue: object, configurationSettingName: str, *nestedId: Array[str]) """
        ...

    def SetSpecificSetting(self, configName:str, collectionName:str, configurationSettingValue:object, configurationSettingName:str, nestedId:Array): # -> 
        """ SetSpecificSetting(self: IConfigurationSettings2, configName: str, collectionName: str, configurationSettingValue: object, configurationSettingName: str, *nestedId: Array[str]) """
        ...


class IDataSourceDescriptor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Kind(self) -> Guid:
        """ Get: Kind(self: IDataSourceDescriptor) -> Guid """
        ...

    @property
    def Moniker(self) -> str:
        """ Get: Moniker(self: IDataSourceDescriptor) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDataSourceDescriptor) -> str """
        ...

    @property
    def Prepared(self) -> bool:
        """ Get: Prepared(self: IDataSourceDescriptor) -> bool """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: IDataSourceDescriptor) -> bool """
        ...


    def GetChildDescriptors(self) -> Array:
        """ GetChildDescriptors(self: IDataSourceDescriptor) -> Array[IDataSourceDescriptor] """
        ...

    def GetProperty(self, name:str) -> object:
        """ GetProperty(self: IDataSourceDescriptor, name: str) -> object """
        ...

    def Prepare(self): # -> 
        """ Prepare(self: IDataSourceDescriptor) """
        ...

    def SetProperty(self, name:str, value:object): # -> 
        """ SetProperty(self: IDataSourceDescriptor, name: str, value: object) """
        ...

    Invalidated = ...
    PropertyChanged = ...


class IDataSourceDescriptorProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetRootDescriptor(self) -> IDataSourceDescriptor:
        """ GetRootDescriptor(self: IDataSourceDescriptorProvider) -> IDataSourceDescriptor """
        ...


class IDataSourceDescriptorService: # skipped bases: <type 'object'>
    """ no doc """
    def FindDataSource(self, moniker:str) -> IDataSourceDescriptor:
        """ FindDataSource(self: IDataSourceDescriptorService, moniker: str) -> IDataSourceDescriptor """
        ...

    def GetDataSources(self) -> Array:
        """ GetDataSources(self: IDataSourceDescriptorService) -> Array[IDataSourceDescriptor] """
        ...


class IDeploymentModuleResolver: # skipped bases: <type 'object'>
    """ no doc """
    def FindModuleFromAssemblyName(self, assemblyName, moduleSignature, modulePath) -> Tuple_[str, str]:
        """ FindModuleFromAssemblyName(self: IDeploymentModuleResolver, assemblyName: AssemblyName) -> (str, str) """
        ...

    def FindModuleFromFileInfo(self, filePath, modulePath, moduleSignature, foundLanguage, foundMSVersion, foundLSVersion) -> Tuple_[str, str, UInt16, UInt32, UInt32]:
        """ FindModuleFromFileInfo(self: IDeploymentModuleResolver, filePath: str) -> (str, str, UInt16, UInt32, UInt32) """
        ...


class IDesignerToolWindow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IDesignerToolWindow) -> str
        Set: Caption(self: IDesignerToolWindow) = value
        """
        ...

    @property
    def Client(self) -> Control:
        """ Get: Client(self: IDesignerToolWindow) -> Control """
        ...

    @property
    def IsVisible(self) -> bool:
        """ Get: IsVisible(self: IDesignerToolWindow) -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: IDesignerToolWindow) """
        ...

    def Hide(self): # -> 
        """ Hide(self: IDesignerToolWindow) """
        ...

    def SetBitmap(self, bitmapResource:int, bitmapIndex:int): # -> 
        """ SetBitmap(self: IDesignerToolWindow, bitmapResource: int, bitmapIndex: int) """
        ...

    def SetViewCommand(self, commandID:CommandID): # -> 
        """ SetViewCommand(self: IDesignerToolWindow, commandID: CommandID) """
        ...

    def Show(self, activate:bool): # -> 
        """ Show(self: IDesignerToolWindow, activate: bool) """
        ...


class IDesignerToolWindowAwareControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ServiceProvider(self) -> IServiceProvider:
        """
        Get: ServiceProvider(self: IDesignerToolWindowAwareControl) -> IServiceProvider
        Set: ServiceProvider(self: IDesignerToolWindowAwareControl) = value
        """
        ...



class IDesignerToolWindowEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnToolWindowClose(self): # -> 
        """ OnToolWindowClose(self: IDesignerToolWindowEvents) """
        ...

    def OnToolWindowHide(self): # -> 
        """ OnToolWindowHide(self: IDesignerToolWindowEvents) """
        ...

    def OnToolWindowShow(self): # -> 
        """ OnToolWindowShow(self: IDesignerToolWindowEvents) """
        ...


class IDesignerToolWindowFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateToolWindow(self, sp:IServiceProvider, toolwindowGuid:Guid, toolwindowId:UInt32): # -> 
        """ CreateToolWindow(self: IDesignerToolWindowFactory, sp: IServiceProvider, toolwindowGuid: Guid, toolwindowId: UInt32) """
        ...


class IDesignerToolWindowService: # skipped bases: <type 'object'>
    """ no doc """
    def CreateToolWindow(self, persistanceSlot:Guid, windowId:UInt32, context:Guid = ..., caption:str = ..., client:Control = ...) -> IDesignerToolWindow:
        """
        CreateToolWindow(self: IDesignerToolWindowService, persistanceSlot: Guid, windowId: UInt32, context: Guid, caption: str, client: Control) -> IDesignerToolWindow
        CreateToolWindow(self: IDesignerToolWindowService, persistanceSlot: Guid, windowId: UInt32)
        """
        ...

    def FindToolWindow(self, persistanceSlot:Guid, windowId:UInt32) -> IDesignerToolWindow:
        """ FindToolWindow(self: IDesignerToolWindowService, persistanceSlot: Guid, windowId: UInt32) -> IDesignerToolWindow """
        ...

    def GetToolWindow(self, persistanceSlot:Guid, windowId:UInt32) -> IDesignerToolWindow:
        """ GetToolWindow(self: IDesignerToolWindowService, persistanceSlot: Guid, windowId: UInt32) -> IDesignerToolWindow """
        ...


class IDWDesignerService: # skipped bases: <type 'object'>
    """ no doc """
    def CanPerformOperation(self, vsHierarchy:object, itemId:UIntPtr, connectionString:str, operation:str, objectUrn:str) -> bool:
        """ CanPerformOperation(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, connectionString: str, operation: str, objectUrn: str) -> bool """
        ...

    def CloseDesigner(self, window:object, saveChanges:bool): # -> 
        """ CloseDesigner(self: IDWDesignerService, window: object, saveChanges: bool) """
        ...

    def OpenDesigner(self, vsHierarchy, itemId, *__args): # -> 
        """ OpenDesigner(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, connectionString: str, objectUrn: str)OpenDesigner(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, objectType: DwObjectKind, connectionString: str, objectUrn: str)OpenDesigner(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, objectType: DwObjectKind, connectionString: str, objectUrn: str, *arguments: Array[object]) """
        ...

    def OpenDesignerEx(self, vsHierarchy:object, itemId:UIntPtr, objectType:DwObjectKind, connectionString:str, objectUrn:str, arguments:Array) -> object:
        """ OpenDesignerEx(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, objectType: DwObjectKind, connectionString: str, objectUrn: str, *arguments: Array[object]) -> object """
        ...

    def PerformOperation(self, vsHierarchy:object, itemId:UIntPtr, connectionString:str, operation:str, objectUrn:str): # -> 
        """ PerformOperation(self: IDWDesignerService, vsHierarchy: object, itemId: UIntPtr, connectionString: str, operation: str, objectUrn: str) """
        ...

    def RunWizard(self, vsHierarchy:object, connectionString:str, parentObjectUrn:str, objectType:str): # -> 
        """ RunWizard(self: IDWDesignerService, vsHierarchy: object, connectionString: str, parentObjectUrn: str, objectType: str) """
        ...


class IMiningModelDrillThroughHandler: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connection(self): # -> IDbConnection
        """
        Get: Connection(self: IMiningModelDrillThroughHandler) -> IDbConnection
        Set: Connection(self: IMiningModelDrillThroughHandler) = value
        """
        ...

    @property
    def MiningModelName(self) -> str:
        """
        Get: MiningModelName(self: IMiningModelDrillThroughHandler) -> str
        Set: MiningModelName(self: IMiningModelDrillThroughHandler) = value
        """
        ...

    @property
    def NodeText(self) -> str:
        """
        Get: NodeText(self: IMiningModelDrillThroughHandler) -> str
        Set: NodeText(self: IMiningModelDrillThroughHandler) = value
        """
        ...

    @property
    def QueryString(self) -> str:
        """
        Get: QueryString(self: IMiningModelDrillThroughHandler) -> str
        Set: QueryString(self: IMiningModelDrillThroughHandler) = value
        """
        ...


    def ShowDrillThrough(self): # -> 
        """ ShowDrillThrough(self: IMiningModelDrillThroughHandler) """
        ...


class IMiningModelViewerControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: IMiningModelViewerControl) -> str
        Set: ConnectionString(self: IMiningModelViewerControl) = value
        """
        ...

    @property
    def MiningModelName(self) -> str:
        """
        Get: MiningModelName(self: IMiningModelViewerControl) -> str
        Set: MiningModelName(self: IMiningModelViewerControl) = value
        """
        ...

    @property
    def ServiceProvider(self) -> IServiceProvider:
        """
        Get: ServiceProvider(self: IMiningModelViewerControl) -> IServiceProvider
        Set: ServiceProvider(self: IMiningModelViewerControl) = value
        """
        ...


    def LoadViewerData(self, context:object) -> bool:
        """ LoadViewerData(self: IMiningModelViewerControl, context: object) -> bool """
        ...

    def ViewerActivated(self, isActivated:bool): # -> 
        """ ViewerActivated(self: IMiningModelViewerControl, isActivated: bool) """
        ...


class IMiningModelViewerControl2(IMiningModelViewerControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DbConnection(self): # -> IDbConnection
        """
        Get: DbConnection(self: IMiningModelViewerControl2) -> IDbConnection
        Set: DbConnection(self: IMiningModelViewerControl2) = value
        """
        ...



class IRootCommandTargetProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetRootCommandTarget(self) -> object:
        """ GetRootCommandTarget(self: IRootCommandTargetProvider) -> object """
        ...


class MenuCommandEx(MenuCommand): # skipped bases: <type 'object'>
    """ MenuCommandEx(commandId: CommandID) """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: MenuCommandEx) -> str
        Set: Text(self: MenuCommandEx) = value
        """
        ...



class TransformConfigurationValueCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TransformConfigurationValueCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, value:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TransformConfigurationValueCallback, value: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: TransformConfigurationValueCallback, result: IAsyncResult) -> object """
        ...

    def Invoke(self, value:object) -> object:
        """ Invoke(self: TransformConfigurationValueCallback, value: object) -> object """
        ...


# variables with complex values

