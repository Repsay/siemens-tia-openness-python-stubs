# encoding: utf-8
# module System.Management.Automation.Provider calls itself Provider
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Attribute, Enum, IDisposable, Int64

from System.Collections import IList

from System.IO import SeekOrigin

from System.Management.Automation import (CommandInvocationIntrinsics, 
    ErrorRecord, IResourceSupplier, InformationRecord, PSCredential, PSObject, 
    PSTransactionContext, ProgressRecord, ProviderIntrinsics, SessionState, 
    SwitchParameter)

from System.Management.Automation.Host import PSHost

from System.Security.AccessControl import (AccessControlSections, 
    ObjectSecurity)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CmdletProvider(IResourceSupplier): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Credential(self) -> PSCredential:
        """ Get: Credential(self: CmdletProvider) -> PSCredential """
        ...

    @property
    def CurrentPSTransaction(self) -> PSTransactionContext:
        """ Get: CurrentPSTransaction(self: CmdletProvider) -> PSTransactionContext """
        ...

    @property
    def DynamicParameters(self):
        ...

    @property
    def Exclude(self) -> Collection:
        """ Get: Exclude(self: CmdletProvider) -> Collection[str] """
        ...

    @property
    def Filter(self) -> str:
        """ Get: Filter(self: CmdletProvider) -> str """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """ Get: Force(self: CmdletProvider) -> SwitchParameter """
        ...

    @property
    def Host(self) -> PSHost:
        """ Get: Host(self: CmdletProvider) -> PSHost """
        ...

    @property
    def Include(self) -> Collection:
        """ Get: Include(self: CmdletProvider) -> Collection[str] """
        ...

    @property
    def InvokeCommand(self) -> CommandInvocationIntrinsics:
        """ Get: InvokeCommand(self: CmdletProvider) -> CommandInvocationIntrinsics """
        ...

    @property
    def InvokeProvider(self) -> ProviderIntrinsics:
        """ Get: InvokeProvider(self: CmdletProvider) -> ProviderIntrinsics """
        ...

    @property
    def ProviderInfo(self):
        ...

    @property
    def PSDriveInfo(self):
        ...

    @property
    def SessionState(self) -> SessionState:
        """ Get: SessionState(self: CmdletProvider) -> SessionState """
        ...

    @property
    def Stopping(self) -> bool:
        """ Get: Stopping(self: CmdletProvider) -> bool """
        ...


    def ShouldContinue(self, query:str, caption:str, yesToAll:bool = ..., noToAll:bool = ...) -> Tuple_[bool, bool, bool]:
        """
        ShouldContinue(self: CmdletProvider, query: str, caption: str) -> bool
        ShouldContinue(self: CmdletProvider, query: str, caption: str, yesToAll: bool, noToAll: bool) -> (bool, bool, bool)
        """
        ...

    def ShouldProcess(self, *__args:str) -> bool:
        """
        ShouldProcess(self: CmdletProvider, target: str) -> bool
        ShouldProcess(self: CmdletProvider, target: str, action: str) -> bool
        ShouldProcess(self: CmdletProvider, verboseDescription: str, verboseWarning: str, caption: str) -> bool
        ShouldProcess(self: CmdletProvider, verboseDescription: str, verboseWarning: str, caption: str) -> (bool, ShouldProcessReason)
        """
        ...

    def Start(self, *args): #cannot find CLR method
        """ Start(self: CmdletProvider, providerInfo: ProviderInfo) -> ProviderInfo """
        ...

    def StartDynamicParameters(self, *args): #cannot find CLR method
        """ StartDynamicParameters(self: CmdletProvider) -> object """
        ...

    def Stop(self, *args): #cannot find CLR method
        """ Stop(self: CmdletProvider) """
        ...

    def StopProcessing(self, *args): #cannot find CLR method
        """ StopProcessing(self: CmdletProvider) """
        ...

    def ThrowTerminatingError(self, errorRecord:ErrorRecord): # -> 
        """ ThrowTerminatingError(self: CmdletProvider, errorRecord: ErrorRecord) """
        ...

    def TransactionAvailable(self) -> bool:
        """ TransactionAvailable(self: CmdletProvider) -> bool """
        ...

    def WriteDebug(self, text:str): # -> 
        """ WriteDebug(self: CmdletProvider, text: str) """
        ...

    def WriteError(self, errorRecord:ErrorRecord): # -> 
        """ WriteError(self: CmdletProvider, errorRecord: ErrorRecord) """
        ...

    def WriteInformation(self, *__args:InformationRecord): # -> 
        """ WriteInformation(self: CmdletProvider, record: InformationRecord)WriteInformation(self: CmdletProvider, messageData: object, tags: Array[str]) """
        ...

    def WriteItemObject(self, item:object, path:str, isContainer:bool): # -> 
        """ WriteItemObject(self: CmdletProvider, item: object, path: str, isContainer: bool) """
        ...

    def WriteProgress(self, progressRecord:ProgressRecord): # -> 
        """ WriteProgress(self: CmdletProvider, progressRecord: ProgressRecord) """
        ...

    def WritePropertyObject(self, propertyValue:object, path:str): # -> 
        """ WritePropertyObject(self: CmdletProvider, propertyValue: object, path: str) """
        ...

    def WriteSecurityDescriptorObject(self, securityDescriptor:ObjectSecurity, path:str): # -> 
        """ WriteSecurityDescriptorObject(self: CmdletProvider, securityDescriptor: ObjectSecurity, path: str) """
        ...

    def WriteVerbose(self, text:str): # -> 
        """ WriteVerbose(self: CmdletProvider, text: str) """
        ...

    def WriteWarning(self, text:str): # -> 
        """ WriteWarning(self: CmdletProvider, text: str) """
        ...


class CmdletProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CmdletProviderAttribute(providerName: str, providerCapabilities: ProviderCapabilities) """
    @property
    def ProviderCapabilities(self) -> ProviderCapabilities:
        """ Get: ProviderCapabilities(self: CmdletProviderAttribute) -> ProviderCapabilities """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: CmdletProviderAttribute) -> str """
        ...


    def __new__(cls, providerName:str, providerCapabilities:ProviderCapabilities) -> Self:
        """ __new__(cls: type, providerName: str, providerCapabilities: ProviderCapabilities) """
        ...


class DriveCmdletProvider(CmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ no doc """
    def InitializeDefaultDrives(self, *args): #cannot find CLR method
        """ InitializeDefaultDrives(self: DriveCmdletProvider) -> Collection[PSDriveInfo] """
        ...

    def NewDrive(self, *args): #cannot find CLR method
        """ NewDrive(self: DriveCmdletProvider, drive: PSDriveInfo) -> PSDriveInfo """
        ...

    def NewDriveDynamicParameters(self, *args): #cannot find CLR method
        """ NewDriveDynamicParameters(self: DriveCmdletProvider) -> object """
        ...

    def RemoveDrive(self, *args): #cannot find CLR method
        """ RemoveDrive(self: DriveCmdletProvider, drive: PSDriveInfo) -> PSDriveInfo """
        ...


class ItemCmdletProvider(DriveCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ no doc """
    def ClearItem(self, *args): #cannot find CLR method
        """ ClearItem(self: ItemCmdletProvider, path: str) """
        ...

    def ClearItemDynamicParameters(self, *args): #cannot find CLR method
        """ ClearItemDynamicParameters(self: ItemCmdletProvider, path: str) -> object """
        ...

    def ExpandPath(self, *args): #cannot find CLR method
        """ ExpandPath(self: ItemCmdletProvider, path: str) -> Array[str] """
        ...

    def GetItem(self, *args): #cannot find CLR method
        """ GetItem(self: ItemCmdletProvider, path: str) """
        ...

    def GetItemDynamicParameters(self, *args): #cannot find CLR method
        """ GetItemDynamicParameters(self: ItemCmdletProvider, path: str) -> object """
        ...

    def InvokeDefaultAction(self, *args): #cannot find CLR method
        """ InvokeDefaultAction(self: ItemCmdletProvider, path: str) """
        ...

    def InvokeDefaultActionDynamicParameters(self, *args): #cannot find CLR method
        """ InvokeDefaultActionDynamicParameters(self: ItemCmdletProvider, path: str) -> object """
        ...

    def IsValidPath(self, *args): #cannot find CLR method
        """ IsValidPath(self: ItemCmdletProvider, path: str) -> bool """
        ...

    def ItemExists(self, *args): #cannot find CLR method
        """ ItemExists(self: ItemCmdletProvider, path: str) -> bool """
        ...

    def ItemExistsDynamicParameters(self, *args): #cannot find CLR method
        """ ItemExistsDynamicParameters(self: ItemCmdletProvider, path: str) -> object """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: ItemCmdletProvider, path: str, value: object) """
        ...

    def SetItemDynamicParameters(self, *args): #cannot find CLR method
        """ SetItemDynamicParameters(self: ItemCmdletProvider, path: str, value: object) -> object """
        ...


class ContainerCmdletProvider(ItemCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ no doc """
    def ConvertPath(self, *args): #cannot find CLR method
        """ ConvertPath(self: ContainerCmdletProvider, path: str, filter: str, updatedPath: str, updatedFilter: str) -> (bool, str, str) """
        ...

    def CopyItem(self, *args): #cannot find CLR method
        """ CopyItem(self: ContainerCmdletProvider, path: str, copyPath: str, recurse: bool) """
        ...

    def CopyItemDynamicParameters(self, *args): #cannot find CLR method
        """ CopyItemDynamicParameters(self: ContainerCmdletProvider, path: str, destination: str, recurse: bool) -> object """
        ...

    def GetChildItems(self, *args): #cannot find CLR method
        """ GetChildItems(self: ContainerCmdletProvider, path: str, recurse: bool)GetChildItems(self: ContainerCmdletProvider, path: str, recurse: bool, depth: UInt32) """
        ...

    def GetChildItemsDynamicParameters(self, *args): #cannot find CLR method
        """ GetChildItemsDynamicParameters(self: ContainerCmdletProvider, path: str, recurse: bool) -> object """
        ...

    def GetChildNames(self, *args): #cannot find CLR method
        """ GetChildNames(self: ContainerCmdletProvider, path: str, returnContainers: ReturnContainers) """
        ...

    def GetChildNamesDynamicParameters(self, *args): #cannot find CLR method
        """ GetChildNamesDynamicParameters(self: ContainerCmdletProvider, path: str) -> object """
        ...

    def HasChildItems(self, *args): #cannot find CLR method
        """ HasChildItems(self: ContainerCmdletProvider, path: str) -> bool """
        ...

    def NewItem(self, *args): #cannot find CLR method
        """ NewItem(self: ContainerCmdletProvider, path: str, itemTypeName: str, newItemValue: object) """
        ...

    def NewItemDynamicParameters(self, *args): #cannot find CLR method
        """ NewItemDynamicParameters(self: ContainerCmdletProvider, path: str, itemTypeName: str, newItemValue: object) -> object """
        ...

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: ContainerCmdletProvider, path: str, recurse: bool) """
        ...

    def RemoveItemDynamicParameters(self, *args): #cannot find CLR method
        """ RemoveItemDynamicParameters(self: ContainerCmdletProvider, path: str, recurse: bool) -> object """
        ...

    def RenameItem(self, *args): #cannot find CLR method
        """ RenameItem(self: ContainerCmdletProvider, path: str, newName: str) """
        ...

    def RenameItemDynamicParameters(self, *args): #cannot find CLR method
        """ RenameItemDynamicParameters(self: ContainerCmdletProvider, path: str, newName: str) -> object """
        ...


class ICmdletProviderSupportsHelp: # skipped bases: <type 'object'>
    """ no doc """
    def GetHelpMaml(self, helpItemName:str, path:str) -> str:
        """ GetHelpMaml(self: ICmdletProviderSupportsHelp, helpItemName: str, path: str) -> str """
        ...


class IContentCmdletProvider: # skipped bases: <type 'object'>
    """ no doc """
    def ClearContent(self, path:str): # -> 
        """ ClearContent(self: IContentCmdletProvider, path: str) """
        ...

    def ClearContentDynamicParameters(self, path:str) -> object:
        """ ClearContentDynamicParameters(self: IContentCmdletProvider, path: str) -> object """
        ...

    def GetContentReader(self, path:str) -> IContentReader:
        """ GetContentReader(self: IContentCmdletProvider, path: str) -> IContentReader """
        ...

    def GetContentReaderDynamicParameters(self, path:str) -> object:
        """ GetContentReaderDynamicParameters(self: IContentCmdletProvider, path: str) -> object """
        ...

    def GetContentWriter(self, path:str) -> IContentWriter:
        """ GetContentWriter(self: IContentCmdletProvider, path: str) -> IContentWriter """
        ...

    def GetContentWriterDynamicParameters(self, path:str) -> object:
        """ GetContentWriterDynamicParameters(self: IContentCmdletProvider, path: str) -> object """
        ...


class IContentReader(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: IContentReader) """
        ...

    def Read(self, readCount:Int64) -> IList:
        """ Read(self: IContentReader, readCount: Int64) -> IList """
        ...

    def Seek(self, offset:Int64, origin:SeekOrigin): # -> 
        """ Seek(self: IContentReader, offset: Int64, origin: SeekOrigin) """
        ...


class IContentWriter(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: IContentWriter) """
        ...

    def Seek(self, offset:Int64, origin:SeekOrigin): # -> 
        """ Seek(self: IContentWriter, offset: Int64, origin: SeekOrigin) """
        ...

    def Write(self, content:IList) -> IList:
        """ Write(self: IContentWriter, content: IList) -> IList """
        ...


class IPropertyCmdletProvider: # skipped bases: <type 'object'>
    """ no doc """
    def ClearProperty(self, path:str, propertyToClear:Collection): # -> 
        """ ClearProperty(self: IPropertyCmdletProvider, path: str, propertyToClear: Collection[str]) """
        ...

    def ClearPropertyDynamicParameters(self, path:str, propertyToClear:Collection) -> object:
        """ ClearPropertyDynamicParameters(self: IPropertyCmdletProvider, path: str, propertyToClear: Collection[str]) -> object """
        ...

    def GetProperty(self, path:str, providerSpecificPickList:Collection): # -> 
        """ GetProperty(self: IPropertyCmdletProvider, path: str, providerSpecificPickList: Collection[str]) """
        ...

    def GetPropertyDynamicParameters(self, path:str, providerSpecificPickList:Collection) -> object:
        """ GetPropertyDynamicParameters(self: IPropertyCmdletProvider, path: str, providerSpecificPickList: Collection[str]) -> object """
        ...

    def SetProperty(self, path:str, propertyValue:PSObject): # -> 
        """ SetProperty(self: IPropertyCmdletProvider, path: str, propertyValue: PSObject) """
        ...

    def SetPropertyDynamicParameters(self, path:str, propertyValue:PSObject) -> object:
        """ SetPropertyDynamicParameters(self: IPropertyCmdletProvider, path: str, propertyValue: PSObject) -> object """
        ...


class IDynamicPropertyCmdletProvider(IPropertyCmdletProvider): # skipped bases: <type 'object'>
    """ no doc """
    def CopyProperty(self, sourcePath:str, sourceProperty:str, destinationPath:str, destinationProperty:str): # -> 
        """ CopyProperty(self: IDynamicPropertyCmdletProvider, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) """
        ...

    def CopyPropertyDynamicParameters(self, sourcePath:str, sourceProperty:str, destinationPath:str, destinationProperty:str) -> object:
        """ CopyPropertyDynamicParameters(self: IDynamicPropertyCmdletProvider, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) -> object """
        ...

    def MoveProperty(self, sourcePath:str, sourceProperty:str, destinationPath:str, destinationProperty:str): # -> 
        """ MoveProperty(self: IDynamicPropertyCmdletProvider, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) """
        ...

    def MovePropertyDynamicParameters(self, sourcePath:str, sourceProperty:str, destinationPath:str, destinationProperty:str) -> object:
        """ MovePropertyDynamicParameters(self: IDynamicPropertyCmdletProvider, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) -> object """
        ...

    def NewProperty(self, path:str, propertyName:str, propertyTypeName:str, value:object): # -> 
        """ NewProperty(self: IDynamicPropertyCmdletProvider, path: str, propertyName: str, propertyTypeName: str, value: object) """
        ...

    def NewPropertyDynamicParameters(self, path:str, propertyName:str, propertyTypeName:str, value:object) -> object:
        """ NewPropertyDynamicParameters(self: IDynamicPropertyCmdletProvider, path: str, propertyName: str, propertyTypeName: str, value: object) -> object """
        ...

    def RemoveProperty(self, path:str, propertyName:str): # -> 
        """ RemoveProperty(self: IDynamicPropertyCmdletProvider, path: str, propertyName: str) """
        ...

    def RemovePropertyDynamicParameters(self, path:str, propertyName:str) -> object:
        """ RemovePropertyDynamicParameters(self: IDynamicPropertyCmdletProvider, path: str, propertyName: str) -> object """
        ...

    def RenameProperty(self, path:str, sourceProperty:str, destinationProperty:str): # -> 
        """ RenameProperty(self: IDynamicPropertyCmdletProvider, path: str, sourceProperty: str, destinationProperty: str) """
        ...

    def RenamePropertyDynamicParameters(self, path:str, sourceProperty:str, destinationProperty:str) -> object:
        """ RenamePropertyDynamicParameters(self: IDynamicPropertyCmdletProvider, path: str, sourceProperty: str, destinationProperty: str) -> object """
        ...


class ISecurityDescriptorCmdletProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetSecurityDescriptor(self, path:str, includeSections:AccessControlSections): # -> 
        """ GetSecurityDescriptor(self: ISecurityDescriptorCmdletProvider, path: str, includeSections: AccessControlSections) """
        ...

    def NewSecurityDescriptorFromPath(self, path:str, includeSections:AccessControlSections) -> ObjectSecurity:
        """ NewSecurityDescriptorFromPath(self: ISecurityDescriptorCmdletProvider, path: str, includeSections: AccessControlSections) -> ObjectSecurity """
        ...

    def NewSecurityDescriptorOfType(self, type:str, includeSections:AccessControlSections) -> ObjectSecurity:
        """ NewSecurityDescriptorOfType(self: ISecurityDescriptorCmdletProvider, type: str, includeSections: AccessControlSections) -> ObjectSecurity """
        ...

    def SetSecurityDescriptor(self, path:str, securityDescriptor:ObjectSecurity): # -> 
        """ SetSecurityDescriptor(self: ISecurityDescriptorCmdletProvider, path: str, securityDescriptor: ObjectSecurity) """
        ...


class NavigationCmdletProvider(ContainerCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ no doc """
    def GetChildName(self, *args): #cannot find CLR method
        """ GetChildName(self: NavigationCmdletProvider, path: str) -> str """
        ...

    def GetParentPath(self, *args): #cannot find CLR method
        """ GetParentPath(self: NavigationCmdletProvider, path: str, root: str) -> str """
        ...

    def IsItemContainer(self, *args): #cannot find CLR method
        """ IsItemContainer(self: NavigationCmdletProvider, path: str) -> bool """
        ...

    def MakePath(self, *args): #cannot find CLR method
        """
        MakePath(self: NavigationCmdletProvider, parent: str, child: str) -> str
        MakePath(self: NavigationCmdletProvider, parent: str, child: str, childIsLeaf: bool) -> str
        """
        ...

    def MoveItem(self, *args): #cannot find CLR method
        """ MoveItem(self: NavigationCmdletProvider, path: str, destination: str) """
        ...

    def MoveItemDynamicParameters(self, *args): #cannot find CLR method
        """ MoveItemDynamicParameters(self: NavigationCmdletProvider, path: str, destination: str) -> object """
        ...

    def NormalizeRelativePath(self, *args): #cannot find CLR method
        """ NormalizeRelativePath(self: NavigationCmdletProvider, path: str, basePath: str) -> str """
        ...


class ProviderCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ProviderCapabilities, values: Credentials (32), Exclude (2), ExpandWildcards (8), Filter (4), Include (1), None (0), ShouldProcess (16), Transactions (64) """
    Credentials: ProviderCapabilities = ...
    Exclude: ProviderCapabilities = ...
    ExpandWildcards: ProviderCapabilities = ...
    Filter: ProviderCapabilities = ...
    Include: ProviderCapabilities = ...
    ShouldProcess: ProviderCapabilities = ...
    Transactions: ProviderCapabilities = ...
    value__ = ...


