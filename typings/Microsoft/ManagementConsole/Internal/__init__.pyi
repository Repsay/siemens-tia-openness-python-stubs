# encoding: utf-8
# module Microsoft.ManagementConsole.Internal calls itself Internal
# from MMCEx, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, MMCFxCommon, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import Request

from System import (Array, Char, Enum, Guid, IDisposable, IntPtr, 
    MarshalByRefObject, TimeSpan, UInt32, Uri)

from System.Collections.Generic import List

from System.Diagnostics import TraceEventType, TraceSource

from System.Runtime.Serialization import ISerializable

from System.Web.UI import Control

from System.Web.UI.MobileControls import Command

from System.Windows.Forms import IWin32Window, ImageList, Keys

from typing import Self

from Windows.Foundation import Point

"""The following names are not found in the module: (ActionStates, 
    ActionsInsertionLocation, BoundEvent, DWordValueKey, IRequestStatus, 
    ISnapInClient, ISnapInMessagePumpProxy, ISnapInPlatform, 
    ListViewColumnFormat, ListViewMode, ListViewOptions, MessageViewIcon, 
    NodeIdType, RequestState, ScopeNodeInsert, SharedDataObjectUpdate, 
    SnapInType, StandardVerbs, StringValueKey, ViewActionType, ViewSetData, 
    WindowsMessage, field#)
"""

# no functions
# classes

class ActionsPaneItemData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: ActionsPaneItemData) -> int
        Set: Id(self: ActionsPaneItemData) = value
        """
        ...

    @property
    def InsertionLocation(self): # -> ActionsInsertionLocation
        """
        Get: InsertionLocation(self: ActionsPaneItemData) -> ActionsInsertionLocation
        Set: InsertionLocation(self: ActionsPaneItemData) = value
        """
        ...


    def Validate(self): # -> 
        """ Validate(self: ActionsPaneItemData) """
        ...


class ActionsPaneExtendedItemData(ActionsPaneItemData): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ActionsPaneExtendedItemData) -> str
        Set: Description(self: ActionsPaneExtendedItemData) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ActionsPaneExtendedItemData) -> str
        Set: DisplayName(self: ActionsPaneExtendedItemData) = value
        """
        ...

    @property
    def ImageIndex(self) -> int:
        """
        Get: ImageIndex(self: ActionsPaneExtendedItemData) -> int
        Set: ImageIndex(self: ActionsPaneExtendedItemData) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ActionsPaneExtendedItemData) -> str
        Set: LanguageIndependentName(self: ActionsPaneExtendedItemData) = value
        """
        ...

    @property
    def MnemonicDisplayName(self) -> str:
        """
        Get: MnemonicDisplayName(self: ActionsPaneExtendedItemData) -> str
        Set: MnemonicDisplayName(self: ActionsPaneExtendedItemData) = value
        """
        ...


    @staticmethod
    def ValidateDescription(description:str): # -> 
        """ ValidateDescription(description: str) """
        ...

    @staticmethod
    def ValidateDisplayName(displayName:str): # -> 
        """ ValidateDisplayName(displayName: str) """
        ...

    @staticmethod
    def ValidateLanguageIndependentName(languageIndependentName:str): # -> 
        """ ValidateLanguageIndependentName(languageIndependentName: str) """
        ...

    @staticmethod
    def ValidateMnemonicDisplayName(displayName:str, propertyName:str): # -> 
        """ ValidateMnemonicDisplayName(displayName: str, propertyName: str) """
        ...


class ActionData(ActionsPaneExtendedItemData): # skipped bases: <type 'object'>
    """ ActionData() """
    @property
    def ExecuteSync(self) -> bool:
        """
        Get: ExecuteSync(self: ActionData) -> bool
        Set: ExecuteSync(self: ActionData) = value
        """
        ...

    @property
    def State(self): # -> ActionStates
        """
        Get: State(self: ActionData) -> ActionStates
        Set: State(self: ActionData) = value
        """
        ...



class RequestInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class NodeRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: NodeRequestInfo) -> int
        Set: ScopeNodeId(self: NodeRequestInfo) = value
        """
        ...



class ActionNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ ActionNodeRequestInfo() """
    @property
    def ActionId(self) -> int:
        """
        Get: ActionId(self: ActionNodeRequestInfo) -> int
        Set: ActionId(self: ActionNodeRequestInfo) = value
        """
        ...



class ActionSeparatorItemData(ActionsPaneItemData): # skipped bases: <type 'object'>
    """ ActionSeparatorItemData() """
    pass

class ActionsInsertionLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActionsInsertionLocation, values: Help (2), Top (0), View (1) """
    Help: ActionsInsertionLocation = ...
    Top: ActionsInsertionLocation = ...
    value__ = ...
    View: ActionsInsertionLocation = ...


class ActionsPaneItemCollectionData(ActionsPaneExtendedItemData): # skipped bases: <type 'object'>
    """ ActionsPaneItemCollectionData() """
    @property
    def RenderAsRegion(self) -> bool:
        """
        Get: RenderAsRegion(self: ActionsPaneItemCollectionData) -> bool
        Set: RenderAsRegion(self: ActionsPaneItemCollectionData) = value
        """
        ...


    def GetItems(self) -> Array:
        """ GetItems(self: ActionsPaneItemCollectionData) -> Array[ActionsPaneItemData] """
        ...

    def SetItems(self, items:Array): # -> 
        """ SetItems(self: ActionsPaneItemCollectionData, items: Array[ActionsPaneItemData]) """
        ...


class ActionsPaneRootData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetDescription(self) -> Array:
        """ GetDescription(self: ActionsPaneRootData) -> Array[str] """
        ...

    def GetDisplayName(self) -> Array:
        """ GetDisplayName(self: ActionsPaneRootData) -> Array[str] """
        ...

    def GetExecuteSync(self) -> Array:
        """ GetExecuteSync(self: ActionsPaneRootData) -> Array[bool] """
        ...

    def GetId(self) -> Array:
        """ GetId(self: ActionsPaneRootData) -> Array[int] """
        ...

    def GetImageIndex(self) -> Array:
        """ GetImageIndex(self: ActionsPaneRootData) -> Array[int] """
        ...

    def GetInsertionLocation(self) -> Array:
        """ GetInsertionLocation(self: ActionsPaneRootData) -> Array[ActionsInsertionLocation] """
        ...

    def GetItemsCount(self) -> Array:
        """ GetItemsCount(self: ActionsPaneRootData) -> Array[int] """
        ...

    def GetItemType(self) -> Array:
        """ GetItemType(self: ActionsPaneRootData) -> Array[ActionsPaneRootItemType] """
        ...

    def GetLanguageIndependentName(self) -> Array:
        """ GetLanguageIndependentName(self: ActionsPaneRootData) -> Array[str] """
        ...

    def GetMnemonicDisplayName(self) -> Array:
        """ GetMnemonicDisplayName(self: ActionsPaneRootData) -> Array[str] """
        ...

    def GetRenderAsRegion(self) -> Array:
        """ GetRenderAsRegion(self: ActionsPaneRootData) -> Array[bool] """
        ...

    def GetState(self) -> Array:
        """ GetState(self: ActionsPaneRootData) -> Array[ActionStates] """
        ...

    def Read(self) -> ActionsPaneItemCollectionData:
        """ Read(self: ActionsPaneRootData) -> ActionsPaneItemCollectionData """
        ...

    def SetDescription(self, value:Array): # -> 
        """ SetDescription(self: ActionsPaneRootData, value: Array[str]) """
        ...

    def SetDisplayName(self, value:Array): # -> 
        """ SetDisplayName(self: ActionsPaneRootData, value: Array[str]) """
        ...

    def SetExecuteSync(self, value:Array): # -> 
        """ SetExecuteSync(self: ActionsPaneRootData, value: Array[bool]) """
        ...

    def SetId(self, value:Array): # -> 
        """ SetId(self: ActionsPaneRootData, value: Array[int]) """
        ...

    def SetImageIndex(self, value:Array): # -> 
        """ SetImageIndex(self: ActionsPaneRootData, value: Array[int]) """
        ...

    def SetInsertionLocation(self, value:Array): # -> 
        """ SetInsertionLocation(self: ActionsPaneRootData, value: Array[ActionsInsertionLocation]) """
        ...

    def SetItemsCount(self, value:Array): # -> 
        """ SetItemsCount(self: ActionsPaneRootData, value: Array[int]) """
        ...

    def SetItemType(self, value:Array): # -> 
        """ SetItemType(self: ActionsPaneRootData, value: Array[ActionsPaneRootItemType]) """
        ...

    def SetLanguageIndependentName(self, value:Array): # -> 
        """ SetLanguageIndependentName(self: ActionsPaneRootData, value: Array[str]) """
        ...

    def SetMnemonicDisplayName(self, value:Array): # -> 
        """ SetMnemonicDisplayName(self: ActionsPaneRootData, value: Array[str]) """
        ...

    def SetRenderAsRegion(self, value:Array): # -> 
        """ SetRenderAsRegion(self: ActionsPaneRootData, value: Array[bool]) """
        ...

    def SetState(self, value:Array): # -> 
        """ SetState(self: ActionsPaneRootData, value: Array[ActionStates]) """
        ...

    def Write(self, data:ActionsPaneItemCollectionData): # -> 
        """ Write(self: ActionsPaneRootData, data: ActionsPaneItemCollectionData) """
        ...


class ActionsPaneRootItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActionsPaneRootItemType, values: Action (1), Collection (2), Separator (0) """
    Action: ActionsPaneRootItemType = ...
    Collection: ActionsPaneRootItemType = ...
    Separator: ActionsPaneRootItemType = ...
    value__ = ...


class ActionStates(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ActionStates, values: Bulleted (4), Checked (2), Enabled (1) """
    Bulleted: ActionStates = ...
    Checked: ActionStates = ...
    Enabled: ActionStates = ...
    value__ = ...


class ViewRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ViewSelectionRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SelectionId(self) -> int:
        """
        Get: SelectionId(self: ViewSelectionRequestInfo) -> int
        Set: SelectionId(self: ViewSelectionRequestInfo) = value
        """
        ...



class ActionViewRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ ActionViewRequestInfo() """
    @property
    def ActionId(self) -> int:
        """
        Get: ActionId(self: ActionViewRequestInfo) -> int
        Set: ActionId(self: ActionViewRequestInfo) = value
        """
        ...

    @property
    def SelectionDependent(self) -> bool:
        """
        Get: SelectionDependent(self: ActionViewRequestInfo) -> bool
        Set: SelectionDependent(self: ActionViewRequestInfo) = value
        """
        ...



class ActivateNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ ActivateNodeRequestInfo() """
    pass

class PropertyPageMessageRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PageId(self) -> int:
        """
        Get: PageId(self: PropertyPageMessageRequestInfo) -> int
        Set: PageId(self: PropertyPageMessageRequestInfo) = value
        """
        ...

    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: PropertyPageMessageRequestInfo) -> int
        Set: SheetId(self: PropertyPageMessageRequestInfo) = value
        """
        ...



class ApplyPropertyPageMessageRequestInfo(PropertyPageMessageRequestInfo): # skipped bases: <type 'object'>
    """ ApplyPropertyPageMessageRequestInfo() """
    pass

class Command: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class ViewCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ViewInstanceId(self) -> int:
        """
        Get: ViewInstanceId(self: ViewCommand) -> int
        Set: ViewInstanceId(self: ViewCommand) = value
        """
        ...



class BatchSelectionDataUpdatesCommand(ViewCommand): # skipped bases: <type 'object'>
    """ BatchSelectionDataUpdatesCommand() """
    @property
    def Begin(self) -> bool:
        """
        Get: Begin(self: BatchSelectionDataUpdatesCommand) -> bool
        Set: Begin(self: BatchSelectionDataUpdatesCommand) = value
        """
        ...



class BeginInvokeCommand(Command): # skipped bases: <type 'object'>
    """ BeginInvokeCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: BeginInvokeCommand) -> int
        Set: Id(self: BeginInvokeCommand) = value
        """
        ...



class Notification: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class BeginInvokeNotification(Notification): # skipped bases: <type 'object'>
    """ BeginInvokeNotification() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: BeginInvokeNotification) -> int
        Set: Id(self: BeginInvokeNotification) = value
        """
        ...



class ConsoleDialogCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OwnerId(self) -> int:
        """
        Get: OwnerId(self: ConsoleDialogCommand) -> int
        Set: OwnerId(self: ConsoleDialogCommand) = value
        """
        ...


    ConsoleWindowOwnerId: int = ...


class BeginModalLoopConsoleDialogCommand(ConsoleDialogCommand): # skipped bases: <type 'object'>
    """ BeginModalLoopConsoleDialogCommand() """
    DefaultTimeout: TimeSpan = ...
    MaxTimeout: TimeSpan = ...


class CommandResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class BeginModalLoopConsoleDialogCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ BeginModalLoopConsoleDialogCommandResult() """
    @property
    def Window(self) -> IWin32Window:
        """
        Get: Window(self: BeginModalLoopConsoleDialogCommandResult) -> IWin32Window
        Set: Window(self: BeginModalLoopConsoleDialogCommandResult) = value
        """
        ...



class PropertySheetCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PageId(self) -> int:
        """
        Get: PageId(self: PropertySheetCommand) -> int
        Set: PageId(self: PropertySheetCommand) = value
        """
        ...

    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: PropertySheetCommand) -> int
        Set: SheetId(self: PropertySheetCommand) = value
        """
        ...



class CancelToClosePropertySheetCommand(PropertySheetCommand): # skipped bases: <type 'object'>
    """ CancelToClosePropertySheetCommand() """
    pass

class DataCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataObjectId(self) -> int:
        """
        Get: DataObjectId(self: DataCommand) -> int
        Set: DataObjectId(self: DataCommand) = value
        """
        ...


    PrimaryDataObjectId: int = ...


class ChangeNotificationSubscriptionCommand(DataCommand): # skipped bases: <type 'object'>
    """ ChangeNotificationSubscriptionCommand() """
    @property
    def IsActive(self) -> bool:
        """
        Get: IsActive(self: ChangeNotificationSubscriptionCommand) -> bool
        Set: IsActive(self: ChangeNotificationSubscriptionCommand) = value
        """
        ...



class ChangeSelectionDataViewRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ ChangeSelectionDataViewRequestInfo() """
    def GetResultNodeIds(self) -> Array:
        """ GetResultNodeIds(self: ChangeSelectionDataViewRequestInfo) -> Array[int] """
        ...

    def GetScopeNodeIds(self) -> Array:
        """ GetScopeNodeIds(self: ChangeSelectionDataViewRequestInfo) -> Array[int] """
        ...

    def SetResultNodeIds(self, resultNodeIds:Array): # -> 
        """ SetResultNodeIds(self: ChangeSelectionDataViewRequestInfo, resultNodeIds: Array[int]) """
        ...

    def SetScopeNodeIds(self, scopeNodeIds:Array): # -> 
        """ SetScopeNodeIds(self: ChangeSelectionDataViewRequestInfo, scopeNodeIds: Array[int]) """
        ...


class ClearDirtyFlagPropertySheetCommand(PropertySheetCommand): # skipped bases: <type 'object'>
    """ ClearDirtyFlagPropertySheetCommand() """
    pass

class ClipboardData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClipboardFormatId(self) -> str:
        """
        Get: ClipboardFormatId(self: ClipboardData) -> str
        Set: ClipboardFormatId(self: ClipboardData) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ClipboardData, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ClipboardData) -> int """
        ...

    def GetValue(self) -> Array:
        """ GetValue(self: ClipboardData) -> Array[Byte] """
        ...

    def SetValue(self, value:Array): # -> 
        """ SetValue(self: ClipboardData, value: Array[Byte]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ColumnCollectionChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ColumnCollectionChangeType, values: Add (0), Modify (2), Remove (1) """
    Add: ColumnCollectionChangeType = ...
    Modify: ColumnCollectionChangeType = ...
    Remove: ColumnCollectionChangeType = ...
    value__ = ...


class ColumnData: # skipped bases: <type 'object'>, <type 'object'>
    """ ColumnData() """
    @property
    def Format(self): # -> ListViewColumnFormat
        """
        Get: Format(self: ColumnData) -> ListViewColumnFormat
        Set: Format(self: ColumnData) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: ColumnData) -> int """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ColumnData) -> str
        Set: Title(self: ColumnData) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: ColumnData) -> bool
        Set: Visible(self: ColumnData) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: ColumnData) -> int
        Set: Width(self: ColumnData) = value
        """
        ...


    def Validate(self): # -> 
        """ Validate(self: ColumnData) """
        ...

    @staticmethod
    def ValidateFormat(format): # ->  # Not found arg types: {'format': 'ListViewColumnFormat'}
        """ ValidateFormat(format: ListViewColumnFormat) """
        ...

    @staticmethod
    def ValidateTitle(title:str): # -> 
        """ ValidateTitle(title: str) """
        ...

    @staticmethod
    def ValidateWidth(width:int): # -> 
        """ ValidateWidth(width: int) """
        ...


class ColumnVisibilityChangedNotification(Notification): # skipped bases: <type 'object'>
    """ ColumnVisibilityChangedNotification() """
    def GetHiddenIds(self) -> Array:
        """ GetHiddenIds(self: ColumnVisibilityChangedNotification) -> Array[int] """
        ...

    def GetVisibleIds(self) -> Array:
        """ GetVisibleIds(self: ColumnVisibilityChangedNotification) -> Array[int] """
        ...

    def SetHiddenIds(self, hiddenIds:Array): # -> 
        """ SetHiddenIds(self: ColumnVisibilityChangedNotification, hiddenIds: Array[int]) """
        ...

    def SetVisibleIds(self, visibleIds:Array): # -> 
        """ SetVisibleIds(self: ColumnVisibilityChangedNotification, visibleIds: Array[int]) """
        ...


class RequestResponse: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class CompareSelectionObjectsResponse(RequestResponse): # skipped bases: <type 'object'>
    """ CompareSelectionObjectsResponse() """
    @property
    def Result(self) -> bool:
        """
        Get: Result(self: CompareSelectionObjectsResponse) -> bool
        Set: Result(self: CompareSelectionObjectsResponse) = value
        """
        ...



class CompareViewSelectionsRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ CompareViewSelectionsRequestInfo() """
    @property
    def SelectionIdToCompare(self) -> int:
        """
        Get: SelectionIdToCompare(self: CompareViewSelectionsRequestInfo) -> int
        Set: SelectionIdToCompare(self: CompareViewSelectionsRequestInfo) = value
        """
        ...



class ComponentAbandonedNotification(Notification): # skipped bases: <type 'object'>
    """ ComponentAbandonedNotification(componentId: int) """
    @property
    def Id(self) -> int:
        """ Get: Id(self: ComponentAbandonedNotification) -> int """
        ...


    def __new__(cls, componentId:int) -> Self:
        """ __new__(cls: type, componentId: int) """
        ...


class CreateCustomRequestStatusCommand(Command): # skipped bases: <type 'object'>
    """ CreateCustomRequestStatusCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: CreateCustomRequestStatusCommand) -> int
        Set: ScopeNodeId(self: CreateCustomRequestStatusCommand) = value
        """
        ...



class CreateCustomRequestStatusCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ CreateCustomRequestStatusCommandResult() """
    @property
    def RequestStatus(self): # -> IRequestStatus
        """
        Get: RequestStatus(self: CreateCustomRequestStatusCommandResult) -> IRequestStatus
        Set: RequestStatus(self: CreateCustomRequestStatusCommandResult) = value
        """
        ...



class CreatePropertySheetCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HideApplyButton(self) -> bool:
        """
        Get: HideApplyButton(self: CreatePropertySheetCommand) -> bool
        Set: HideApplyButton(self: CreatePropertySheetCommand) = value
        """
        ...

    @property
    def PropertyPagesData(self) -> Array:
        """
        Get: PropertyPagesData(self: CreatePropertySheetCommand) -> Array[PropertyPageInfo]
        Set: PropertyPagesData(self: CreatePropertySheetCommand) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: CreatePropertySheetCommand) -> str
        Set: Title(self: CreatePropertySheetCommand) = value
        """
        ...



class CreatePropertySheetCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ CreatePropertySheetCommandResult() """
    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: CreatePropertySheetCommandResult) -> int
        Set: SheetId(self: CreatePropertySheetCommandResult) = value
        """
        ...



class CreatePropertySheetForScopeNodeCommand(CreatePropertySheetCommand): # skipped bases: <type 'object'>
    """ CreatePropertySheetForScopeNodeCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: CreatePropertySheetForScopeNodeCommand) -> int
        Set: ScopeNodeId(self: CreatePropertySheetForScopeNodeCommand) = value
        """
        ...



class CreatePropertySheetForViewCommand(CreatePropertySheetCommand): # skipped bases: <type 'object'>
    """ CreatePropertySheetForViewCommand() """
    @property
    def ViewId(self) -> int:
        """
        Get: ViewId(self: CreatePropertySheetForViewCommand) -> int
        Set: ViewId(self: CreatePropertySheetForViewCommand) = value
        """
        ...



class CutOrMoveNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ CutOrMoveNodeRequestInfo() """
    pass

class CutOrMoveViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ CutOrMoveViewSelectionRequestInfo() """
    pass

class DataChangeNotification(Notification): # skipped bases: <type 'object'>
    """ DataChangeNotification() """
    @property
    def DataObjectId(self) -> int:
        """
        Get: DataObjectId(self: DataChangeNotification) -> int
        Set: DataObjectId(self: DataChangeNotification) = value
        """
        ...


    def GetChangedClipboardFormatIds(self) -> Array:
        """ GetChangedClipboardFormatIds(self: DataChangeNotification) -> Array[str] """
        ...

    def GetRemovedClipboardFormatIds(self) -> Array:
        """ GetRemovedClipboardFormatIds(self: DataChangeNotification) -> Array[str] """
        ...

    def SetChangedClipboardFormatIds(self, changedClipboardFormatIds:Array): # -> 
        """ SetChangedClipboardFormatIds(self: DataChangeNotification, changedClipboardFormatIds: Array[str]) """
        ...

    def SetRemovedClipboardFormatIds(self, removedClipboardFormatIds:Array): # -> 
        """ SetRemovedClipboardFormatIds(self: DataChangeNotification, removedClipboardFormatIds: Array[str]) """
        ...


class DataFormatConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClipboardFormatId(self) -> str:
        """
        Get: ClipboardFormatId(self: DataFormatConfiguration) -> str
        Set: ClipboardFormatId(self: DataFormatConfiguration) = value
        """
        ...

    @property
    def RequiresQuery(self) -> bool:
        """
        Get: RequiresQuery(self: DataFormatConfiguration) -> bool
        Set: RequiresQuery(self: DataFormatConfiguration) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: DataFormatConfiguration, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DataFormatConfiguration) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DeactivateNodeNotification(Notification): # skipped bases: <type 'object'>
    """ DeactivateNodeNotification() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: DeactivateNodeNotification) -> int
        Set: ScopeNodeId(self: DeactivateNodeNotification) = value
        """
        ...



class DeleteNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ DeleteNodeRequestInfo() """
    pass

class DeleteScopeNodesCommand(Command): # skipped bases: <type 'object'>
    """ DeleteScopeNodesCommand() """
    def GetIds(self) -> Array:
        """ GetIds(self: DeleteScopeNodesCommand) -> Array[int] """
        ...

    def SetIds(self, ids:Array): # -> 
        """ SetIds(self: DeleteScopeNodesCommand, ids: Array[int]) """
        ...


class DeleteViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ DeleteViewSelectionRequestInfo() """
    pass

class PropertyPageNotification(Notification): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PageId(self) -> int:
        """
        Get: PageId(self: PropertyPageNotification) -> int
        Set: PageId(self: PropertyPageNotification) = value
        """
        ...

    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: PropertyPageNotification) -> int
        Set: SheetId(self: PropertyPageNotification) = value
        """
        ...



class DestroyPropertyPageNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ DestroyPropertyPageNotification() """
    pass

class DragAndDropVerb(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DragAndDropVerb, values: CopyHere (0), MoveHere (1) """
    CopyHere: DragAndDropVerb = ...
    MoveHere: DragAndDropVerb = ...
    value__ = ...


class EndModalLoopConsoleDialogCommand(ConsoleDialogCommand): # skipped bases: <type 'object'>
    """ EndModalLoopConsoleDialogCommand() """
    pass

class ExpandConsoleScopeNodeCommand(ViewCommand): # skipped bases: <type 'object'>
    """ ExpandConsoleScopeNodeCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: ExpandConsoleScopeNodeCommand) -> int
        Set: ScopeNodeId(self: ExpandConsoleScopeNodeCommand) = value
        """
        ...



class ExpandFromLoadScopeNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ ExpandFromLoadScopeNodeRequestInfo() """
    pass

class ExpandFromLoadScopeNodeRequestResponse(RequestResponse): # skipped bases: <type 'object'>
    """ ExpandFromLoadScopeNodeRequestResponse() """
    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: ExpandFromLoadScopeNodeRequestResponse) -> bool
        Set: Handled(self: ExpandFromLoadScopeNodeRequestResponse) = value
        """
        ...



class ExpandScopeNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ ExpandScopeNodeRequestInfo() """
    pass

class ExtensionPagesRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ ExtensionPagesRequestInfo() """
    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: ExtensionPagesRequestInfo) -> int
        Set: SheetId(self: ExtensionPagesRequestInfo) = value
        """
        ...



class FindPropertySheetCommand(Command): # skipped bases: <type 'object'>
    """ no doc """
    pass

class FindPropertySheetCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ FindPropertySheetCommandResult() """
    @property
    def SheetExists(self) -> bool:
        """
        Get: SheetExists(self: FindPropertySheetCommandResult) -> bool
        Set: SheetExists(self: FindPropertySheetCommandResult) = value
        """
        ...



class FindPropertySheetForScopeNodeCommand(FindPropertySheetCommand): # skipped bases: <type 'object'>
    """ FindPropertySheetForScopeNodeCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: FindPropertySheetForScopeNodeCommand) -> int
        Set: ScopeNodeId(self: FindPropertySheetForScopeNodeCommand) = value
        """
        ...



class FindPropertySheetForViewCommand(FindPropertySheetCommand): # skipped bases: <type 'object'>
    """ FindPropertySheetForViewCommand() """
    @property
    def SelectionId(self) -> int:
        """
        Get: SelectionId(self: FindPropertySheetForViewCommand) -> int
        Set: SelectionId(self: FindPropertySheetForViewCommand) = value
        """
        ...



class ViewDescriptionData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ViewDescriptionData) -> str
        Set: DisplayName(self: ViewDescriptionData) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: ViewDescriptionData) -> int
        Set: Id(self: ViewDescriptionData) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ViewDescriptionData) -> str
        Set: LanguageIndependentName(self: ViewDescriptionData) = value
        """
        ...


    def Validate(self): # -> 
        """ Validate(self: ViewDescriptionData) """
        ...

    @staticmethod
    def ValidateDisplayName(displayName:str): # -> 
        """ ValidateDisplayName(displayName: str) """
        ...

    @staticmethod
    def ValidateLanguageIndependentName(languageIndependentName:str): # -> 
        """ ValidateLanguageIndependentName(languageIndependentName: str) """
        ...

    ExDefaultViewId: int = ...
    ExErrorViewId: int = ...


class FormViewDescriptionData(ViewDescriptionData): # skipped bases: <type 'object'>
    """ FormViewDescriptionData() """
    pass

class GetListViewModeCommand(ViewCommand): # skipped bases: <type 'object'>
    """ GetListViewModeCommand() """
    pass

class GetListViewModeCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ GetListViewModeCommandResult() """
    @property
    def Mode(self): # -> ListViewMode
        """
        Get: Mode(self: GetListViewModeCommandResult) -> ListViewMode
        Set: Mode(self: GetListViewModeCommandResult) = value
        """
        ...



class GetPopupParentWindowCommand(ConsoleDialogCommand): # skipped bases: <type 'object'>
    """ GetPopupParentWindowCommand() """
    pass

class GetPopupParentWindowCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ GetPopupParentWindowCommandResult() """
    @property
    def ParentWindow(self) -> IWin32Window:
        """
        Get: ParentWindow(self: GetPopupParentWindowCommandResult) -> IWin32Window
        Set: ParentWindow(self: GetPopupParentWindowCommandResult) = value
        """
        ...



class GlobalConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def SnapInHostingOptions(self, *args): #cannot find CLR method
        """ no doc """
        ...

    __all__: list = ...


class HideViewNotification(Notification): # skipped bases: <type 'object'>
    """ HideViewNotification() """
    pass

class HtmlViewDescriptionData(ViewDescriptionData): # skipped bases: <type 'object'>
    """
    HtmlViewDescriptionData()
    HtmlViewDescriptionData(url: Uri)
    """
    @property
    def Url(self) -> Uri:
        """
        Get: Url(self: HtmlViewDescriptionData) -> Uri
        Set: Url(self: HtmlViewDescriptionData) = value
        """
        ...


    @staticmethod
    def ValidateUrl(url:Uri): # -> 
        """ ValidateUrl(url: Uri) """
        ...

    def __new__(cls, url:Uri = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, url: Uri)
        """
        ...


class IClassLibraryServices: # skipped bases: <type 'object'>
    """ no doc """
    def CreateMessagePumpProxy(self): # -> ISnapInMessagePumpProxy
        """ CreateMessagePumpProxy(self: IClassLibraryServices) -> ISnapInMessagePumpProxy """
        ...

    def CreateSnapIn(self, assemblyName:str, typeName:str): # -> ISnapInClient
        """ CreateSnapIn(self: IClassLibraryServices, assemblyName: str, typeName: str) -> ISnapInClient """
        ...


class IMessageClient: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessNotification(self, notification:Notification): # -> 
        """ ProcessNotification(self: IMessageClient, notification: Notification) """
        ...

    def ProcessRequest(self, request:Request): # -> 
        """ ProcessRequest(self: IMessageClient, request: Request) """
        ...


class InitializePropertyPageNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ InitializePropertyPageNotification() """
    pass

class InitializeViewRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ InitializeViewRequestInfo() """
    pass

class InsertScopeNodesCommand(Command): # skipped bases: <type 'object'>
    """ InsertScopeNodesCommand() """
    pass

class InsertScopeNodesCommandReader(IDisposable): # skipped bases: <type 'object'>
    """ InsertScopeNodesCommandReader(source: InsertScopeNodesCommand) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: InsertScopeNodesCommandReader) -> int """
        ...


    def ReadScopeNodeInsert(self): # -> ScopeNodeInsert
        """ ReadScopeNodeInsert(self: InsertScopeNodesCommandReader) -> ScopeNodeInsert """
        ...


class InsertScopeNodesCommandWriter(IDisposable): # skipped bases: <type 'object'>
    """ InsertScopeNodesCommandWriter(capacity: int) """
    def Flush(self) -> InsertScopeNodesCommand:
        """ Flush(self: InsertScopeNodesCommandWriter) -> InsertScopeNodesCommand """
        ...

    def WriteScopeNodeInsert(self, obj): # ->  # Not found arg types: {'obj': 'ScopeNodeInsert'}
        """ WriteScopeNodeInsert(self: InsertScopeNodesCommandWriter, obj: ScopeNodeInsert) """
        ...


class IRequestStatus: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanCancel(self) -> bool:
        """
        Get: CanCancel(self: IRequestStatus) -> bool
        Set: CanCancel(self: IRequestStatus) = value
        """
        ...

    @property
    def IsCancelExposed(self) -> bool:
        """ Get: IsCancelExposed(self: IRequestStatus) -> bool """
        ...

    @property
    def IsCancelSignaled(self) -> bool:
        """ Get: IsCancelSignaled(self: IRequestStatus) -> bool """
        ...

    @property
    def RequestState(self): # -> RequestState
        """
        Get: RequestState(self: IRequestStatus) -> RequestState
        Set: RequestState(self: IRequestStatus) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: IRequestStatus) -> str
        Set: Title(self: IRequestStatus) = value
        """
        ...


    def ProcessResponse(self, response:RequestResponse): # -> 
        """ ProcessResponse(self: IRequestStatus, response: RequestResponse) """
        ...

    def ReportProgress(self, workProcessed:int, totalWork:int, statusText:str): # -> 
        """ ReportProgress(self: IRequestStatus, workProcessed: int, totalWork: int, statusText: str) """
        ...

    def SetCompletionText(self, completionText:str, isSuccess:bool): # -> 
        """ SetCompletionText(self: IRequestStatus, completionText: str, isSuccess: bool) """
        ...


class ISnapInClient(IMessageClient): # skipped bases: <type 'object'>
    """ no doc """
    def CreateView(self, nodeId:int, componentId:int, viewDescriptionId:int, viewInstanceId:int) -> IMessageClient:
        """ CreateView(self: ISnapInClient, nodeId: int, componentId: int, viewDescriptionId: int, viewInstanceId: int) -> IMessageClient """
        ...

    def Initialize(self, snapInPlatform): # ->  # Not found arg types: {'snapInPlatform': 'ISnapInPlatform'}
        """ Initialize(self: ISnapInClient, snapInPlatform: ISnapInPlatform) """
        ...


class ISnapInMessagePumpProxy: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LastKeyboardMessage(self): # -> WindowsMessage
        """ Get: LastKeyboardMessage(self: ISnapInMessagePumpProxy) -> WindowsMessage """
        ...


    def ExitThread(self): # -> 
        """ ExitThread(self: ISnapInMessagePumpProxy) """
        ...

    def Run(self): # -> 
        """ Run(self: ISnapInMessagePumpProxy) """
        ...


class ISnapInPlatform: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessCommand(self, command:Command) -> CommandResult:
        """ ProcessCommand(self: ISnapInPlatform, command: Command) -> CommandResult """
        ...


class IsScopeNodeVisuallyExpandedCommand(ViewCommand): # skipped bases: <type 'object'>
    """ IsScopeNodeVisuallyExpandedCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: IsScopeNodeVisuallyExpandedCommand) -> int
        Set: ScopeNodeId(self: IsScopeNodeVisuallyExpandedCommand) = value
        """
        ...



class IsScopeNodeVisuallyExpandedCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ IsScopeNodeVisuallyExpandedCommandResult() """
    @property
    def IsExpanded(self) -> bool:
        """
        Get: IsExpanded(self: IsScopeNodeVisuallyExpandedCommandResult) -> bool
        Set: IsExpanded(self: IsScopeNodeVisuallyExpandedCommandResult) = value
        """
        ...



class KeepAlivePurpose(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeepAlivePurpose, values: Clipboard (0), RunningTask (1) """
    Clipboard: KeepAlivePurpose = ...
    RunningTask: KeepAlivePurpose = ...
    value__ = ...


class KeepAliveViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ KeepAliveViewSelectionRequestInfo() """
    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: KeepAliveViewSelectionRequestInfo) -> bool
        Set: KeepAlive(self: KeepAliveViewSelectionRequestInfo) = value
        """
        ...

    @property
    def Purpose(self) -> KeepAlivePurpose:
        """
        Get: Purpose(self: KeepAliveViewSelectionRequestInfo) -> KeepAlivePurpose
        Set: Purpose(self: KeepAliveViewSelectionRequestInfo) = value
        """
        ...



class KillActivePropertyPageMessageRequestInfo(PropertyPageMessageRequestInfo): # skipped bases: <type 'object'>
    """ KillActivePropertyPageMessageRequestInfo() """
    pass

class ListViewColumnFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListViewColumnFormat, values: Center (1), Left (0), Right (2) """
    Center: ListViewColumnFormat = ...
    Left: ListViewColumnFormat = ...
    Right: ListViewColumnFormat = ...
    value__ = ...


class ListViewDescriptionData(ViewDescriptionData): # skipped bases: <type 'object'>
    """
    ListViewDescriptionData()
    ListViewDescriptionData(options: ListViewOptions)
    """
    @property
    def Options(self): # -> ListViewOptions
        """
        Get: Options(self: ListViewDescriptionData) -> ListViewOptions
        Set: Options(self: ListViewDescriptionData) = value
        """
        ...


    def __new__(cls, options = ...) -> Self: # Not found arg types: {'options': 'ListViewOptions'}
        """
        __new__(cls: type)
        __new__(cls: type, options: ListViewOptions)
        """
        ...


class ListViewMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListViewMode, values: LargeIcon (2), List (1), Report (0), SmallIcon (3) """
    LargeIcon: ListViewMode = ...
    List: ListViewMode = ...
    Report: ListViewMode = ...
    SmallIcon: ListViewMode = ...
    value__ = ...


class ListViewOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ListViewOptions, values: All (255), AllowPasteOnResultNodes (32), AllowUserInitiatedModeChanges (128), DisableUserInitiatedSort (8), ExcludeScopeNodes (4), HideSelection (2), None (0), SingleSelect (1), UseCustomSorting (16), UseFontLinking (64) """
    All: ListViewOptions = ...
    AllowPasteOnResultNodes: ListViewOptions = ...
    AllowUserInitiatedModeChanges: ListViewOptions = ...
    DisableUserInitiatedSort: ListViewOptions = ...
    ExcludeScopeNodes: ListViewOptions = ...
    HideSelection: ListViewOptions = ...
    SingleSelect: ListViewOptions = ...
    UseCustomSorting: ListViewOptions = ...
    UseFontLinking: ListViewOptions = ...
    value__ = ...


class LoadDataRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ LoadDataRequestInfo() """
    def GetDataBlob(self) -> Array:
        """ GetDataBlob(self: LoadDataRequestInfo) -> Array[Byte] """
        ...

    def SetDataBlob(self, dataBlob:Array): # -> 
        """ SetDataBlob(self: LoadDataRequestInfo, dataBlob: Array[Byte]) """
        ...


class LoadViewDataRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ LoadViewDataRequestInfo() """
    def GetDataBlob(self) -> Array:
        """ GetDataBlob(self: LoadViewDataRequestInfo) -> Array[Byte] """
        ...

    def SetDataBlob(self, dataBlob:Array): # -> 
        """ SetDataBlob(self: LoadViewDataRequestInfo, dataBlob: Array[Byte]) """
        ...


class LoseKeyboardFocusCommand(ViewCommand): # skipped bases: <type 'object'>
    """ LoseKeyboardFocusCommand() """
    @property
    def Forward(self) -> bool:
        """
        Get: Forward(self: LoseKeyboardFocusCommand) -> bool
        Set: Forward(self: LoseKeyboardFocusCommand) = value
        """
        ...



class LoseKeyboardFocusCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ LoseKeyboardFocusCommandResult() """
    @property
    def FocusChanged(self) -> bool:
        """
        Get: FocusChanged(self: LoseKeyboardFocusCommandResult) -> bool
        Set: FocusChanged(self: LoseKeyboardFocusCommandResult) = value
        """
        ...



class MessageViewDescriptionData(ViewDescriptionData): # skipped bases: <type 'object'>
    """
    MessageViewDescriptionData()
    MessageViewDescriptionData(title: str, bodyText: str, iconId: MessageViewIcon)
    """
    @property
    def BodyText(self) -> str:
        """
        Get: BodyText(self: MessageViewDescriptionData) -> str
        Set: BodyText(self: MessageViewDescriptionData) = value
        """
        ...

    @property
    def IconId(self): # -> MessageViewIcon
        """
        Get: IconId(self: MessageViewDescriptionData) -> MessageViewIcon
        Set: IconId(self: MessageViewDescriptionData) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: MessageViewDescriptionData) -> str
        Set: Title(self: MessageViewDescriptionData) = value
        """
        ...


    @staticmethod
    def ValidateIconId(iconId): # ->  # Not found arg types: {'iconId': 'MessageViewIcon'}
        """ ValidateIconId(iconId: MessageViewIcon) """
        ...

    @staticmethod
    def ValidateText(bodyText:str): # -> 
        """ ValidateText(bodyText: str) """
        ...

    @staticmethod
    def ValidateTitle(title:str): # -> 
        """ ValidateTitle(title: str) """
        ...

    def __new__(cls, title:str = ..., bodyText:str = ..., iconId = ...) -> Self: # Not found arg types: {'iconId': 'MessageViewIcon'}
        """
        __new__(cls: type)
        __new__(cls: type, title: str, bodyText: str, iconId: MessageViewIcon)
        """
        ...


class MessageViewIcon(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MessageViewIcon, values: Error (1), Information (4), None (0), Question (2), Warning (3) """
    Error: MessageViewIcon = ...
    Information: MessageViewIcon = ...
    Question: MessageViewIcon = ...
    value__ = ...
    Warning: MessageViewIcon = ...


class MouseActivateCommand(ViewCommand): # skipped bases: <type 'object'>
    """ MouseActivateCommand() """
    @property
    def HitTestResult(self) -> int:
        """
        Get: HitTestResult(self: MouseActivateCommand) -> int
        Set: HitTestResult(self: MouseActivateCommand) = value
        """
        ...

    @property
    def TopLevelWindow(self) -> IntPtr:
        """
        Get: TopLevelWindow(self: MouseActivateCommand) -> IntPtr
        Set: TopLevelWindow(self: MouseActivateCommand) = value
        """
        ...



class NamespaceExtensionInitNotification(Notification): # skipped bases: <type 'object'>
    """ NamespaceExtensionInitNotification() """
    @property
    def PrimaryNodeType(self) -> Guid:
        """
        Get: PrimaryNodeType(self: NamespaceExtensionInitNotification) -> Guid
        Set: PrimaryNodeType(self: NamespaceExtensionInitNotification) = value
        """
        ...



class NodeData: # skipped bases: <type 'object'>, <type 'object'>
    """ NodeData() """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: NodeData) -> str
        Set: DisplayName(self: NodeData) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: NodeData) -> int
        Set: Id(self: NodeData) = value
        """
        ...

    @property
    def ImageIndex(self) -> int:
        """
        Get: ImageIndex(self: NodeData) -> int
        Set: ImageIndex(self: NodeData) = value
        """
        ...


    def GetSubItems(self) -> Array:
        """ GetSubItems(self: NodeData) -> Array[NodeSubItemData] """
        ...

    def SetSubItems(self, subItems:Array): # -> 
        """ SetSubItems(self: NodeData, subItems: Array[NodeSubItemData]) """
        ...


class NodeIdData: # skipped bases: <type 'object'>, <type 'object'>
    """ NodeIdData() """
    @property
    def NameId(self) -> str:
        """
        Get: NameId(self: NodeIdData) -> str
        Set: NameId(self: NodeIdData) = value
        """
        ...

    @property
    def Type(self): # -> NodeIdType
        """
        Get: Type(self: NodeIdData) -> NodeIdType
        Set: Type(self: NodeIdData) = value
        """
        ...


    def GetCustomId(self) -> Array:
        """ GetCustomId(self: NodeIdData) -> Array[Byte] """
        ...

    def SetCustomId(self, customId:Array): # -> 
        """ SetCustomId(self: NodeIdData, customId: Array[Byte]) """
        ...


class NodeIdType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NodeIdType, values: Custom (2), Display (0), LanguageIndependent (1) """
    Custom: NodeIdType = ...
    Display: NodeIdType = ...
    LanguageIndependent: NodeIdType = ...
    value__ = ...


class NodeSubItemData: # skipped bases: <type 'object'>, <type 'object'>
    """ NodeSubItemData() """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: NodeSubItemData) -> str
        Set: DisplayName(self: NodeSubItemData) = value
        """
        ...



class NodeType: # skipped bases: <type 'object'>, <type 'object'>
    """ NodeType() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: NodeType) -> str
        Set: Description(self: NodeType) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Get: Guid(self: NodeType) -> Guid
        Set: Guid(self: NodeType) = value
        """
        ...



class OkPropertyPageMessageRequestInfo(PropertyPageMessageRequestInfo): # skipped bases: <type 'object'>
    """ OkPropertyPageMessageRequestInfo() """
    pass

class PagesForNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ PagesForNodeRequestInfo() """
    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: PagesForNodeRequestInfo) -> int
        Set: SheetId(self: PagesForNodeRequestInfo) = value
        """
        ...



class PagesForViewRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ PagesForViewRequestInfo() """
    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: PagesForViewRequestInfo) -> int
        Set: SheetId(self: PagesForViewRequestInfo) = value
        """
        ...



class PasteNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ PasteNodeRequestInfo() """
    @property
    def DataObjectId(self) -> int:
        """
        Get: DataObjectId(self: PasteNodeRequestInfo) -> int
        Set: DataObjectId(self: PasteNodeRequestInfo) = value
        """
        ...

    @property
    def PasteType(self) -> DragAndDropVerb:
        """
        Get: PasteType(self: PasteNodeRequestInfo) -> DragAndDropVerb
        Set: PasteType(self: PasteNodeRequestInfo) = value
        """
        ...



class PasteResponse(RequestResponse): # skipped bases: <type 'object'>
    """ PasteResponse() """
    @property
    def AcceptPaste(self) -> bool:
        """
        Get: AcceptPaste(self: PasteResponse) -> bool
        Set: AcceptPaste(self: PasteResponse) = value
        """
        ...



class PasteTargetInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ PasteTargetInfo() """
    @property
    def DefaultDragAndDropVerb(self) -> DragAndDropVerb:
        """
        Get: DefaultDragAndDropVerb(self: PasteTargetInfo) -> DragAndDropVerb
        Set: DefaultDragAndDropVerb(self: PasteTargetInfo) = value
        """
        ...


    def GetAllowedClipboardFormats(self) -> Array:
        """ GetAllowedClipboardFormats(self: PasteTargetInfo) -> Array[str] """
        ...

    def SetAllowedClipboardFormats(self, allowedClipboardFormats:Array): # -> 
        """ SetAllowedClipboardFormats(self: PasteTargetInfo, allowedClipboardFormats: Array[str]) """
        ...


class PasteViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ PasteViewSelectionRequestInfo() """
    @property
    def DataObjectId(self) -> int:
        """
        Get: DataObjectId(self: PasteViewSelectionRequestInfo) -> int
        Set: DataObjectId(self: PasteViewSelectionRequestInfo) = value
        """
        ...

    @property
    def PasteType(self) -> DragAndDropVerb:
        """
        Get: PasteType(self: PasteViewSelectionRequestInfo) -> DragAndDropVerb
        Set: PasteType(self: PasteViewSelectionRequestInfo) = value
        """
        ...



class PersistenceCompletedResponse(RequestResponse): # skipped bases: <type 'object'>
    """ PersistenceCompletedResponse() """
    def GetDataBlob(self) -> Array:
        """ GetDataBlob(self: PersistenceCompletedResponse) -> Array[Byte] """
        ...

    def SetDataBlob(self, data:Array): # -> 
        """ SetDataBlob(self: PersistenceCompletedResponse, data: Array[Byte]) """
        ...


class PersistenceKeyRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ PersistenceKeyRequestInfo() """
    pass

class PersistenceKeyRetrievalCompletedResponse(RequestResponse): # skipped bases: <type 'object'>
    """ PersistenceKeyRetrievalCompletedResponse() """
    @property
    def PersistenceKey(self) -> str:
        """
        Get: PersistenceKey(self: PersistenceKeyRetrievalCompletedResponse) -> str
        Set: PersistenceKey(self: PersistenceKeyRetrievalCompletedResponse) = value
        """
        ...



class PrimarySnapInDataException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrimarySnapInDataException()
    PrimarySnapInDataException(message: str)
    PrimarySnapInDataException(message: str, innerException: Exception)
    PrimarySnapInDataException(information: SerializationInfo, context: StreamingContext)
    """
    SerializeObjectState = ...


class PrintNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ PrintNodeRequestInfo() """
    pass

class PrintViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ PrintViewSelectionRequestInfo() """
    pass

class ProcessDialogKeyPropertySheetCommand(PropertySheetCommand): # skipped bases: <type 'object'>
    """ ProcessDialogKeyPropertySheetCommand() """
    @property
    def KeyData(self) -> Keys:
        """
        Get: KeyData(self: ProcessDialogKeyPropertySheetCommand) -> Keys
        Set: KeyData(self: ProcessDialogKeyPropertySheetCommand) = value
        """
        ...



class ProcessMnemonicNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ ProcessMnemonicNotification() """
    @property
    def CharCode(self) -> Char:
        """
        Get: CharCode(self: ProcessMnemonicNotification) -> Char
        Set: CharCode(self: ProcessMnemonicNotification) = value
        """
        ...



class ProcessViewCmdKeyCommand(ViewCommand): # skipped bases: <type 'object'>
    """ ProcessViewCmdKeyCommand() """
    pass

class ProcessViewCmdKeyCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ ProcessViewCmdKeyCommandResult() """
    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: ProcessViewCmdKeyCommandResult) -> bool
        Set: Handled(self: ProcessViewCmdKeyCommandResult) = value
        """
        ...



class ProcessViewDialogKeyCommand(ViewCommand): # skipped bases: <type 'object'>
    """ ProcessViewDialogKeyCommand() """
    pass

class PropertyPageInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ PropertyPageInfo() """
    @property
    def Height(self) -> int:
        """
        Get: Height(self: PropertyPageInfo) -> int
        Set: Height(self: PropertyPageInfo) = value
        """
        ...

    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: PropertyPageInfo) -> str
        Set: HelpTopic(self: PropertyPageInfo) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: PropertyPageInfo) -> str
        Set: Title(self: PropertyPageInfo) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: PropertyPageInfo) -> int
        Set: Width(self: PropertyPageInfo) = value
        """
        ...



class PropertyPageMessageResponse(RequestResponse): # skipped bases: <type 'object'>
    """ PropertyPageMessageResponse() """
    @property
    def AllowRequestedOperation(self) -> bool:
        """
        Get: AllowRequestedOperation(self: PropertyPageMessageResponse) -> bool
        Set: AllowRequestedOperation(self: PropertyPageMessageResponse) = value
        """
        ...

    @property
    def NewActivePageId(self) -> int:
        """
        Get: NewActivePageId(self: PropertyPageMessageResponse) -> int
        Set: NewActivePageId(self: PropertyPageMessageResponse) = value
        """
        ...



class PropertyPageShowCustomHelpTopicNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ PropertyPageShowCustomHelpTopicNotification() """
    pass

class PropertyPagesResponse(RequestResponse): # skipped bases: <type 'object'>
    """ PropertyPagesResponse() """
    def GetPropertyPages(self) -> Array:
        """ GetPropertyPages(self: PropertyPagesResponse) -> Array[PropertyPageInfo] """
        ...

    def SetPropertyPages(self, propertyPagesData:Array): # -> 
        """ SetPropertyPages(self: PropertyPagesResponse, propertyPagesData: Array[PropertyPageInfo]) """
        ...


class PropertySheetExtensionInitNotification(Notification): # skipped bases: <type 'object'>
    """ PropertySheetExtensionInitNotification() """
    def GetPrimaryNodeTypes(self) -> Array:
        """ GetPrimaryNodeTypes(self: PropertySheetExtensionInitNotification) -> Array[Guid] """
        ...

    def SetPrimaryNodeTypes(self, primaryNodeTypes:Array): # -> 
        """ SetPrimaryNodeTypes(self: PropertySheetExtensionInitNotification, primaryNodeTypes: Array[Guid]) """
        ...


class QueryCancelPropertyPageMessageRequestInfo(PropertyPageMessageRequestInfo): # skipped bases: <type 'object'>
    """ QueryCancelPropertyPageMessageRequestInfo() """
    pass

class ReadDataCommand(DataCommand): # skipped bases: <type 'object'>
    """ ReadDataCommand() """
    @property
    def ClipboardFormatId(self) -> str:
        """
        Get: ClipboardFormatId(self: ReadDataCommand) -> str
        Set: ClipboardFormatId(self: ReadDataCommand) = value
        """
        ...

    @property
    def ReadTimeout(self) -> TimeSpan:
        """ Get: ReadTimeout(self: ReadDataCommand) -> TimeSpan """
        ...



class ReadDataCommandResult(CommandResult): # skipped bases: <type 'object'>
    """ ReadDataCommandResult() """
    @property
    def Data(self) -> ClipboardData:
        """
        Get: Data(self: ReadDataCommandResult) -> ClipboardData
        Set: Data(self: ReadDataCommandResult) = value
        """
        ...



class ReadSharedDataNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ ReadSharedDataNodeRequestInfo() """
    @property
    def RequestedClipboardFormatId(self) -> str:
        """
        Get: RequestedClipboardFormatId(self: ReadSharedDataNodeRequestInfo) -> str
        Set: RequestedClipboardFormatId(self: ReadSharedDataNodeRequestInfo) = value
        """
        ...



class ReadSharedDataResponse(RequestResponse): # skipped bases: <type 'object'>
    """ ReadSharedDataResponse() """
    @property
    def RequestedClipboardData(self) -> ClipboardData:
        """
        Get: RequestedClipboardData(self: ReadSharedDataResponse) -> ClipboardData
        Set: RequestedClipboardData(self: ReadSharedDataResponse) = value
        """
        ...



class ReadSharedDataViewRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ ReadSharedDataViewRequestInfo() """
    @property
    def RequestedClipboardFormatId(self) -> str:
        """
        Get: RequestedClipboardFormatId(self: ReadSharedDataViewRequestInfo) -> str
        Set: RequestedClipboardFormatId(self: ReadSharedDataViewRequestInfo) = value
        """
        ...



class RefreshNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ RefreshNodeRequestInfo() """
    pass

class RefreshViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ RefreshViewSelectionRequestInfo() """
    pass

class RegisterUIThreadCommand(Command): # skipped bases: <type 'object'>
    """ RegisterUIThreadCommand() """
    @property
    def Register(self) -> bool:
        """
        Get: Register(self: RegisterUIThreadCommand) -> bool
        Set: Register(self: RegisterUIThreadCommand) = value
        """
        ...

    @property
    def UnmanagedThreadId(self) -> UInt32:
        """
        Get: UnmanagedThreadId(self: RegisterUIThreadCommand) -> UInt32
        Set: UnmanagedThreadId(self: RegisterUIThreadCommand) = value
        """
        ...



class RenameNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ RenameNodeRequestInfo() """
    @property
    def NewDisplayName(self) -> str:
        """
        Get: NewDisplayName(self: RenameNodeRequestInfo) -> str
        Set: NewDisplayName(self: RenameNodeRequestInfo) = value
        """
        ...



class RenameViewSelectionRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ RenameViewSelectionRequestInfo() """
    @property
    def NewDisplayName(self) -> str:
        """
        Get: NewDisplayName(self: RenameViewSelectionRequestInfo) -> str
        Set: NewDisplayName(self: RenameViewSelectionRequestInfo) = value
        """
        ...



class Request(MarshalByRefObject): # skipped bases: <type 'object'>
    """ Request(requestInfo: RequestInfo, requestStatus: IRequestStatus) """
    @property
    def RequestInfo(self) -> RequestInfo:
        """ Get: RequestInfo(self: Request) -> RequestInfo """
        ...

    @property
    def RequestStatus(self) -> IRequestStatus:
        """ Get: RequestStatus(self: Request) -> IRequestStatus """
        ...


    def __new__(cls, requestInfo:RequestInfo, requestStatus:IRequestStatus) -> Self:
        """ __new__(cls: type, requestInfo: RequestInfo, requestStatus: IRequestStatus) """
        ...


class RequestState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RequestState, values: Complete (2), Pending (1), Synchronous (0) """
    Complete: RequestState = ...
    Pending: RequestState = ...
    Synchronous: RequestState = ...
    value__ = ...


class RequestWriteDataCommand(DataCommand): # skipped bases: <type 'object'>
    """ RequestWriteDataCommand() """
    @property
    def RequestedValue(self) -> ClipboardData:
        """
        Get: RequestedValue(self: RequestWriteDataCommand) -> ClipboardData
        Set: RequestedValue(self: RequestWriteDataCommand) = value
        """
        ...



class ResetPropertyPageNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ ResetPropertyPageNotification() """
    pass

class ResultNodeCollectionChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResultNodeCollectionChangeType, values: Add (0), Modify (2), Remove (1) """
    Add: ResultNodeCollectionChangeType = ...
    Modify: ResultNodeCollectionChangeType = ...
    Remove: ResultNodeCollectionChangeType = ...
    value__ = ...


class SaveDataRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ SaveDataRequestInfo() """
    @property
    def ClearModified(self) -> bool:
        """
        Get: ClearModified(self: SaveDataRequestInfo) -> bool
        Set: ClearModified(self: SaveDataRequestInfo) = value
        """
        ...



class SaveViewDataRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ SaveViewDataRequestInfo() """
    @property
    def ClearModified(self) -> bool:
        """
        Get: ClearModified(self: SaveViewDataRequestInfo) -> bool
        Set: ClearModified(self: SaveViewDataRequestInfo) = value
        """
        ...



class SaveViewDataResponse(RequestResponse): # skipped bases: <type 'object'>
    """ SaveViewDataResponse() """
    def GetDataBlob(self) -> Array:
        """ GetDataBlob(self: SaveViewDataResponse) -> Array[Byte] """
        ...

    def SetDataBlob(self, data:Array): # -> 
        """ SetDataBlob(self: SaveViewDataResponse, data: Array[Byte]) """
        ...


class ScopeNodeData(NodeData): # skipped bases: <type 'object'>
    """ ScopeNodeData() """
    @property
    def EnabledVerbs(self): # -> StandardVerbs
        """
        Get: EnabledVerbs(self: ScopeNodeData) -> StandardVerbs
        Set: EnabledVerbs(self: ScopeNodeData) = value
        """
        ...

    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: ScopeNodeData) -> str
        Set: HelpTopic(self: ScopeNodeData) = value
        """
        ...

    @property
    def HideExpandIcon(self) -> bool:
        """
        Get: HideExpandIcon(self: ScopeNodeData) -> bool
        Set: HideExpandIcon(self: ScopeNodeData) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ScopeNodeData) -> str
        Set: LanguageIndependentName(self: ScopeNodeData) = value
        """
        ...

    @property
    def NodeType(self) -> Guid:
        """
        Get: NodeType(self: ScopeNodeData) -> Guid
        Set: NodeType(self: ScopeNodeData) = value
        """
        ...

    @property
    def PasteTargetInfo(self) -> PasteTargetInfo:
        """ Get: PasteTargetInfo(self: ScopeNodeData) -> PasteTargetInfo """
        ...

    @property
    def SelectedImageIndex(self) -> int:
        """
        Get: SelectedImageIndex(self: ScopeNodeData) -> int
        Set: SelectedImageIndex(self: ScopeNodeData) = value
        """
        ...

    @property
    def SendActivation(self) -> bool:
        """
        Get: SendActivation(self: ScopeNodeData) -> bool
        Set: SendActivation(self: ScopeNodeData) = value
        """
        ...

    @property
    def SendDeactivation(self) -> bool:
        """
        Get: SendDeactivation(self: ScopeNodeData) -> bool
        Set: SendDeactivation(self: ScopeNodeData) = value
        """
        ...

    @property
    def ViewSetId(self) -> int:
        """
        Get: ViewSetId(self: ScopeNodeData) -> int
        Set: ViewSetId(self: ScopeNodeData) = value
        """
        ...



class ScopeNodeInsert: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Actions(self) -> ActionsPaneRootData:
        """
        Get: Actions(self: ScopeNodeInsert) -> ActionsPaneRootData
        Set: Actions(self: ScopeNodeInsert) = value
        """
        ...

    @property
    def HelpActions(self) -> ActionsPaneRootData:
        """
        Get: HelpActions(self: ScopeNodeInsert) -> ActionsPaneRootData
        Set: HelpActions(self: ScopeNodeInsert) = value
        """
        ...

    @property
    def InitialSharedData(self): # -> SharedDataObjectUpdate
        """ Get: InitialSharedData(self: ScopeNodeInsert) -> SharedDataObjectUpdate """
        ...

    @property
    def InsertionIndex(self) -> int:
        """
        Get: InsertionIndex(self: ScopeNodeInsert) -> int
        Set: InsertionIndex(self: ScopeNodeInsert) = value
        """
        ...

    @property
    def NodeData(self) -> ScopeNodeData:
        """
        Get: NodeData(self: ScopeNodeInsert) -> ScopeNodeData
        Set: NodeData(self: ScopeNodeInsert) = value
        """
        ...

    @property
    def ParentScopeNodeId(self) -> int:
        """
        Get: ParentScopeNodeId(self: ScopeNodeInsert) -> int
        Set: ParentScopeNodeId(self: ScopeNodeInsert) = value
        """
        ...



class ScopeNodeShowCustomHelpTopicNotification(Notification): # skipped bases: <type 'object'>
    """ ScopeNodeShowCustomHelpTopicNotification() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: ScopeNodeShowCustomHelpTopicNotification) -> int
        Set: Id(self: ScopeNodeShowCustomHelpTopicNotification) = value
        """
        ...



class SelectionCardinality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SelectionCardinality, values: Multiple (2), None (0), Single (1) """
    Multiple: SelectionCardinality = ...
    Single: SelectionCardinality = ...
    value__ = ...


class SelectResultNodeCommand(ViewCommand): # skipped bases: <type 'object'>
    """ SelectResultNodeCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: SelectResultNodeCommand) -> int
        Set: Id(self: SelectResultNodeCommand) = value
        """
        ...

    @property
    def Scheduled(self) -> bool:
        """
        Get: Scheduled(self: SelectResultNodeCommand) -> bool
        Set: Scheduled(self: SelectResultNodeCommand) = value
        """
        ...

    @property
    def SelectionState(self) -> bool:
        """
        Get: SelectionState(self: SelectResultNodeCommand) -> bool
        Set: SelectionState(self: SelectResultNodeCommand) = value
        """
        ...



class SelectScopeNodeCommand(ViewCommand): # skipped bases: <type 'object'>
    """ SelectScopeNodeCommand() """
    @property
    def ScopeNodeId(self) -> int:
        """
        Get: ScopeNodeId(self: SelectScopeNodeCommand) -> int
        Set: ScopeNodeId(self: SelectScopeNodeCommand) = value
        """
        ...


    def GetRelativePath(self) -> Array:
        """ GetRelativePath(self: SelectScopeNodeCommand) -> Array[NodeIdData] """
        ...

    def SetRelativePath(self, relativePath:Array): # -> 
        """ SetRelativePath(self: SelectScopeNodeCommand, relativePath: Array[NodeIdData]) """
        ...


class SerializableImageListWrapper(ISerializable): # skipped bases: <type 'object'>
    """ SerializableImageListWrapper() """
    @property
    def ImageList(self) -> ImageList:
        """
        Get: ImageList(self: SerializableImageListWrapper) -> ImageList
        Set: ImageList(self: SerializableImageListWrapper) = value
        """
        ...



class SetActivePagePropertySheetCommand(PropertySheetCommand): # skipped bases: <type 'object'>
    """ SetActivePagePropertySheetCommand() """
    @property
    def NewActivePageId(self) -> int:
        """
        Get: NewActivePageId(self: SetActivePagePropertySheetCommand) -> int
        Set: NewActivePageId(self: SetActivePagePropertySheetCommand) = value
        """
        ...



class SetActivePropertyPageNotification(PropertyPageNotification): # skipped bases: <type 'object'>
    """ SetActivePropertyPageNotification() """
    pass

class SetDirtyFlagPropertySheetCommand(PropertySheetCommand): # skipped bases: <type 'object'>
    """ SetDirtyFlagPropertySheetCommand() """
    pass

class SetFormViewControlCommand(ViewCommand): # skipped bases: <type 'object'>
    """ SetFormViewControlCommand() """
    @property
    def Handle(self) -> IntPtr:
        """
        Get: Handle(self: SetFormViewControlCommand) -> IntPtr
        Set: Handle(self: SetFormViewControlCommand) = value
        """
        ...



class SetNewSelectionCommand(ViewCommand): # skipped bases: <type 'object'>
    """ SetNewSelectionCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: SetNewSelectionCommand) -> int
        Set: Id(self: SetNewSelectionCommand) = value
        """
        ...

    @property
    def SelectionCardinality(self) -> SelectionCardinality:
        """
        Get: SelectionCardinality(self: SetNewSelectionCommand) -> SelectionCardinality
        Set: SelectionCardinality(self: SetNewSelectionCommand) = value
        """
        ...

    @property
    def UniqueNodeTypes(self) -> Array:
        """
        Get: UniqueNodeTypes(self: SetNewSelectionCommand) -> Array[Guid]
        Set: UniqueNodeTypes(self: SetNewSelectionCommand) = value
        """
        ...

    @property
    def UpdatedSharedData(self): # -> SharedDataObjectUpdate
        """
        Get: UpdatedSharedData(self: SetNewSelectionCommand) -> SharedDataObjectUpdate
        Set: UpdatedSharedData(self: SetNewSelectionCommand) = value
        """
        ...



class SetPropertyPageControlCommand(Command): # skipped bases: <type 'object'>
    """ SetPropertyPageControlCommand() """
    @property
    def Control(self) -> Control:
        """
        Get: Control(self: SetPropertyPageControlCommand) -> Control
        Set: Control(self: SetPropertyPageControlCommand) = value
        """
        ...

    @property
    def Handle(self) -> IntPtr:
        """
        Get: Handle(self: SetPropertyPageControlCommand) -> IntPtr
        Set: Handle(self: SetPropertyPageControlCommand) = value
        """
        ...

    @property
    def PageId(self) -> int:
        """
        Get: PageId(self: SetPropertyPageControlCommand) -> int
        Set: PageId(self: SetPropertyPageControlCommand) = value
        """
        ...

    @property
    def SheetId(self) -> int:
        """
        Get: SheetId(self: SetPropertyPageControlCommand) -> int
        Set: SheetId(self: SetPropertyPageControlCommand) = value
        """
        ...



class SetViewSetDataCommand(Command): # skipped bases: <type 'object'>
    """ SetViewSetDataCommand() """
    @property
    def ViewSet(self): # -> ViewSetData
        """
        Get: ViewSet(self: SetViewSetDataCommand) -> ViewSetData
        Set: ViewSet(self: SetViewSetDataCommand) = value
        """
        ...



class SharedDataObjectUpdate: # skipped bases: <type 'object'>, <type 'object'>
    """ SharedDataObjectUpdate() """
    def GetAddedFormats(self) -> Array:
        """ GetAddedFormats(self: SharedDataObjectUpdate) -> Array[DataFormatConfiguration] """
        ...

    def GetChangedFormats(self) -> Array:
        """ GetChangedFormats(self: SharedDataObjectUpdate) -> Array[DataFormatConfiguration] """
        ...

    def GetRemovedClipboardFormatIds(self) -> Array:
        """ GetRemovedClipboardFormatIds(self: SharedDataObjectUpdate) -> Array[str] """
        ...

    def GetUpdatedData(self) -> Array:
        """ GetUpdatedData(self: SharedDataObjectUpdate) -> Array[ClipboardData] """
        ...

    def SetAddedFormats(self, addedFormats:Array): # -> 
        """ SetAddedFormats(self: SharedDataObjectUpdate, addedFormats: Array[DataFormatConfiguration]) """
        ...

    def SetChangedFormats(self, changedFormats:Array): # -> 
        """ SetChangedFormats(self: SharedDataObjectUpdate, changedFormats: Array[DataFormatConfiguration]) """
        ...

    def SetRemovedClipboardFormatIds(self, removedClipboardFormatIds:Array): # -> 
        """ SetRemovedClipboardFormatIds(self: SharedDataObjectUpdate, removedClipboardFormatIds: Array[str]) """
        ...

    def SetUpdatedData(self, updatedData:Array): # -> 
        """ SetUpdatedData(self: SharedDataObjectUpdate, updatedData: Array[ClipboardData]) """
        ...


class ShowContextMenuCommand(ViewCommand): # skipped bases: <type 'object'>
    """ ShowContextMenuCommand() """
    @property
    def OnResultItem(self) -> bool:
        """
        Get: OnResultItem(self: ShowContextMenuCommand) -> bool
        Set: OnResultItem(self: ShowContextMenuCommand) = value
        """
        ...

    @property
    def Point(self) -> Point:
        """
        Get: Point(self: ShowContextMenuCommand) -> Point
        Set: Point(self: ShowContextMenuCommand) = value
        """
        ...



class ShowHelpTopicCommand(Command): # skipped bases: <type 'object'>
    """ ShowHelpTopicCommand() """
    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: ShowHelpTopicCommand) -> str
        Set: HelpTopic(self: ShowHelpTopicCommand) = value
        """
        ...



class ShowInitializationWizardRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ ShowInitializationWizardRequestInfo() """
    pass

class ShowInitializationWizardResponse(RequestResponse): # skipped bases: <type 'object'>
    """ ShowInitializationWizardResponse() """
    @property
    def AddSnapInToConsole(self) -> bool:
        """
        Get: AddSnapInToConsole(self: ShowInitializationWizardResponse) -> bool
        Set: AddSnapInToConsole(self: ShowInitializationWizardResponse) = value
        """
        ...



class ShowViewNotification(Notification): # skipped bases: <type 'object'>
    """ ShowViewNotification() """
    pass

class ShutdownRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ ShutdownRequestInfo() """
    pass

class ShutdownViewRequestInfo(ViewRequestInfo): # skipped bases: <type 'object'>
    """ ShutdownViewRequestInfo() """
    pass

class SnapInData: # skipped bases: <type 'object'>, <type 'object'>
    """ SnapInData() """
    @property
    def IsModified(self) -> bool:
        """
        Get: IsModified(self: SnapInData) -> bool
        Set: IsModified(self: SnapInData) = value
        """
        ...

    @property
    def LargeImages(self) -> ImageList:
        """
        Get: LargeImages(self: SnapInData) -> ImageList
        Set: LargeImages(self: SnapInData) = value
        """
        ...

    @property
    def SmallImages(self) -> ImageList:
        """
        Get: SmallImages(self: SnapInData) -> ImageList
        Set: SmallImages(self: SnapInData) = value
        """
        ...



class SnapInRegistrationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ SnapInRegistrationInfo() """
    @property
    def ExtendedNodeTypes(self) -> List:
        """ Get: ExtendedNodeTypes(self: SnapInRegistrationInfo) -> List[Guid] """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SnapInRegistrationInfo) -> str
        Set: Id(self: SnapInRegistrationInfo) = value
        """
        ...

    @property
    def NodeTypes(self) -> List:
        """ Get: NodeTypes(self: SnapInRegistrationInfo) -> List[NodeType] """
        ...

    @property
    def SnapInType(self): # -> SnapInType
        """
        Get: SnapInType(self: SnapInRegistrationInfo) -> SnapInType
        Set: SnapInType(self: SnapInRegistrationInfo) = value
        """
        ...


    def DWordValueKey(self, *args): #cannot find CLR method
        """ enum DWordValueKey, values: FolderBitmapsColorMask (0), UseCustomHelp (1) """
        ...

    def GetDWordProperty(self, key) -> int: # Not found arg types: {'key': 'DWordValueKey'}
        """ GetDWordProperty(self: SnapInRegistrationInfo, key: DWordValueKey) -> int """
        ...

    def GetStringProperty(self, key) -> str: # Not found arg types: {'key': 'StringValueKey'}
        """ GetStringProperty(self: SnapInRegistrationInfo, key: StringValueKey) -> str """
        ...

    @staticmethod
    def LoadFromStore(id:str) -> SnapInRegistrationInfo:
        """ LoadFromStore(id: str) -> SnapInRegistrationInfo """
        ...

    def RemoveFromStore(self): # -> 
        """ RemoveFromStore(self: SnapInRegistrationInfo) """
        ...

    def SetDWordProperty(self, key, value:int): # ->  # Not found arg types: {'key': 'DWordValueKey'}
        """ SetDWordProperty(self: SnapInRegistrationInfo, key: DWordValueKey, value: int) """
        ...

    def SetStringProperty(self, key, value:str): # ->  # Not found arg types: {'key': 'StringValueKey'}
        """ SetStringProperty(self: SnapInRegistrationInfo, key: StringValueKey, value: str) """
        ...

    def StringValueKey(self, *args): #cannot find CLR method
        """ enum StringValueKey, values: About (16), ApplicationBase (1), AssemblyName (13), ConfigurationFile (2), Description (10), DescriptionStringIndirect (18), DynamicBase (3), FxVersion (15), HelpTopic (25), IconIndirect (21), LargeFolderBitmapIndirect (22), LicenseFile (4), LinkedHelpTopics (26), ModuleName (12), NameString (9), NameStringIndirect (17), PrivateBinPath (5), PrivateBinPathProbe (6), ResourceModule (7), RootNodeType (8), RuntimeVersion (14), SmallFolderBitmapIndirect (23), SmallSelectedFolderBitmapIndirect (24), Type (0), Vendor (11), VendorStringIndirect (19), VersionStringIndirect (20) """
        ...

    def WriteToStore(self): # -> 
        """ WriteToStore(self: SnapInRegistrationInfo) """
        ...



class SnapInType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SnapInType, values: ActionsPane (2), Namespace (1), PropertySheet (3), StandAlone (0), Unknown (-1) """
    ActionsPane: SnapInType = ...
    Namespace: SnapInType = ...
    PropertySheet: SnapInType = ...
    StandAlone: SnapInType = ...
    Unknown: SnapInType = ...
    value__ = ...


class SortListViewCommand(ViewCommand): # skipped bases: <type 'object'>
    """ SortListViewCommand() """
    @property
    def ColumnIndex(self) -> int:
        """
        Get: ColumnIndex(self: SortListViewCommand) -> int
        Set: ColumnIndex(self: SortListViewCommand) = value
        """
        ...

    @property
    def Descending(self) -> bool:
        """
        Get: Descending(self: SortListViewCommand) -> bool
        Set: Descending(self: SortListViewCommand) = value
        """
        ...

    @property
    def HideSortIcon(self) -> bool:
        """
        Get: HideSortIcon(self: SortListViewCommand) -> bool
        Set: HideSortIcon(self: SortListViewCommand) = value
        """
        ...


    def GetIds(self) -> Array:
        """ GetIds(self: SortListViewCommand) -> Array[int] """
        ...

    def SetIds(self, ids:Array): # -> 
        """ SetIds(self: SortListViewCommand, ids: Array[int]) """
        ...


class SortListViewRequestInfo(RequestInfo): # skipped bases: <type 'object'>
    """ SortListViewRequestInfo() """
    @property
    def ColumnIndex(self) -> int:
        """
        Get: ColumnIndex(self: SortListViewRequestInfo) -> int
        Set: ColumnIndex(self: SortListViewRequestInfo) = value
        """
        ...

    @property
    def Descending(self) -> bool:
        """
        Get: Descending(self: SortListViewRequestInfo) -> bool
        Set: Descending(self: SortListViewRequestInfo) = value
        """
        ...



class SortListViewResponse(RequestResponse): # skipped bases: <type 'object'>
    """ SortListViewResponse() """
    def GetIds(self) -> Array:
        """ GetIds(self: SortListViewResponse) -> Array[int] """
        ...

    def SetIds(self, ids:Array): # -> 
        """ SetIds(self: SortListViewResponse, ids: Array[int]) """
        ...


class StandardVerbs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StandardVerbs, values: Copy (2), Cut (1), Delete (8), None (0), Paste (4), Print (128), Properties (16), Refresh (64), Rename (32) """
    Copy: StandardVerbs = ...
    Cut: StandardVerbs = ...
    Delete: StandardVerbs = ...
    Paste: StandardVerbs = ...
    Print: StandardVerbs = ...
    Properties: StandardVerbs = ...
    Refresh: StandardVerbs = ...
    Rename: StandardVerbs = ...
    value__ = ...


class TempClassForFixingIssue: # skipped bases: <type 'object'>, <type 'object'>
    """ TempClassForFixingIssue() """
    @property
    def Count(self) -> int:
        """
        Get: Count(self: TempClassForFixingIssue) -> int
        Set: Count(self: TempClassForFixingIssue) = value
        """
        ...



class TraceUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def TraceException(source:TraceSource, severity:TraceEventType, eventId:int, ex:Exception, message:str): # -> 
        """ TraceException(source: TraceSource, severity: TraceEventType, eventId: int, ex: Exception, message: str) """
        ...

    __all__: list = ...


class UpdateColumnsCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateColumnsCommand() """
    @property
    def ChangeType(self) -> ColumnCollectionChangeType:
        """
        Get: ChangeType(self: UpdateColumnsCommand) -> ColumnCollectionChangeType
        Set: ChangeType(self: UpdateColumnsCommand) = value
        """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: UpdateColumnsCommand) -> int
        Set: Index(self: UpdateColumnsCommand) = value
        """
        ...


    def GetData(self) -> Array:
        """ GetData(self: UpdateColumnsCommand) -> Array[ColumnData] """
        ...

    def SetData(self, data:Array): # -> 
        """ SetData(self: UpdateColumnsCommand, data: Array[ColumnData]) """
        ...


class UpdateDataChangeNodeRequestInfo(NodeRequestInfo): # skipped bases: <type 'object'>
    """ UpdateDataChangeNodeRequestInfo() """
    @property
    def RequestedValue(self) -> ClipboardData:
        """
        Get: RequestedValue(self: UpdateDataChangeNodeRequestInfo) -> ClipboardData
        Set: RequestedValue(self: UpdateDataChangeNodeRequestInfo) = value
        """
        ...



class UpdateListViewModeCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateListViewModeCommand() """
    @property
    def Mode(self) -> ListViewMode:
        """
        Get: Mode(self: UpdateListViewModeCommand) -> ListViewMode
        Set: Mode(self: UpdateListViewModeCommand) = value
        """
        ...



class UpdateMessageViewCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateMessageViewCommand() """
    @property
    def Data(self) -> MessageViewDescriptionData:
        """
        Get: Data(self: UpdateMessageViewCommand) -> MessageViewDescriptionData
        Set: Data(self: UpdateMessageViewCommand) = value
        """
        ...



class UpdateResultNodesCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateResultNodesCommand() """
    @property
    def ChangeType(self) -> ResultNodeCollectionChangeType:
        """
        Get: ChangeType(self: UpdateResultNodesCommand) -> ResultNodeCollectionChangeType
        Set: ChangeType(self: UpdateResultNodesCommand) = value
        """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: UpdateResultNodesCommand) -> int
        Set: Index(self: UpdateResultNodesCommand) = value
        """
        ...


    def GetData(self) -> Array:
        """ GetData(self: UpdateResultNodesCommand) -> Array[NodeData] """
        ...

    def SetData(self, data:Array): # -> 
        """ SetData(self: UpdateResultNodesCommand, data: Array[NodeData]) """
        ...


class UpdateScopeNodeCommand(Command): # skipped bases: <type 'object'>
    """ UpdateScopeNodeCommand() """
    @property
    def Actions(self) -> ActionsPaneRootData:
        """
        Get: Actions(self: UpdateScopeNodeCommand) -> ActionsPaneRootData
        Set: Actions(self: UpdateScopeNodeCommand) = value
        """
        ...

    @property
    def HelpActions(self) -> ActionsPaneRootData:
        """
        Get: HelpActions(self: UpdateScopeNodeCommand) -> ActionsPaneRootData
        Set: HelpActions(self: UpdateScopeNodeCommand) = value
        """
        ...

    @property
    def NodeData(self) -> ScopeNodeData:
        """
        Get: NodeData(self: UpdateScopeNodeCommand) -> ScopeNodeData
        Set: NodeData(self: UpdateScopeNodeCommand) = value
        """
        ...

    @property
    def UpdatedSharedData(self) -> SharedDataObjectUpdate:
        """
        Get: UpdatedSharedData(self: UpdateScopeNodeCommand) -> SharedDataObjectUpdate
        Set: UpdatedSharedData(self: UpdateScopeNodeCommand) = value
        """
        ...



class UpdateSharedDataViewRequestInfo(ViewSelectionRequestInfo): # skipped bases: <type 'object'>
    """ UpdateSharedDataViewRequestInfo() """
    @property
    def RequestedValue(self) -> ClipboardData:
        """
        Get: RequestedValue(self: UpdateSharedDataViewRequestInfo) -> ClipboardData
        Set: RequestedValue(self: UpdateSharedDataViewRequestInfo) = value
        """
        ...



class UpdateSnapInCommand(Command): # skipped bases: <type 'object'>
    """ UpdateSnapInCommand() """
    @property
    def SnapInData(self) -> SnapInData:
        """
        Get: SnapInData(self: UpdateSnapInCommand) -> SnapInData
        Set: SnapInData(self: UpdateSnapInCommand) = value
        """
        ...



class UpdateSnapInConfigCommand(Command): # skipped bases: <type 'object'>
    """ UpdateSnapInConfigCommand() """
    @property
    def WaitDialogDelay(self) -> TimeSpan:
        """
        Get: WaitDialogDelay(self: UpdateSnapInConfigCommand) -> TimeSpan
        Set: WaitDialogDelay(self: UpdateSnapInConfigCommand) = value
        """
        ...



class UpdateSnapInExtensionsCommand(Command): # skipped bases: <type 'object'>
    """ UpdateSnapInExtensionsCommand() """
    pass

class UpdateViewActionsCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewActionsCommand() """
    @property
    def ActionType(self): # -> ViewActionType
        """
        Get: ActionType(self: UpdateViewActionsCommand) -> ViewActionType
        Set: ActionType(self: UpdateViewActionsCommand) = value
        """
        ...

    @property
    def Data(self) -> ActionsPaneItemCollectionData:
        """
        Get: Data(self: UpdateViewActionsCommand) -> ActionsPaneItemCollectionData
        Set: Data(self: UpdateViewActionsCommand) = value
        """
        ...



class UpdateViewDescriptionBarTextCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewDescriptionBarTextCommand() """
    @property
    def DescriptionBarText(self) -> str:
        """
        Get: DescriptionBarText(self: UpdateViewDescriptionBarTextCommand) -> str
        Set: DescriptionBarText(self: UpdateViewDescriptionBarTextCommand) = value
        """
        ...



class UpdateViewModifiedStateCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewModifiedStateCommand() """
    @property
    def IsModified(self) -> bool:
        """
        Get: IsModified(self: UpdateViewModifiedStateCommand) -> bool
        Set: IsModified(self: UpdateViewModifiedStateCommand) = value
        """
        ...



class UpdateViewPasteTargetInfoCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewPasteTargetInfoCommand() """
    @property
    def PasteTargetInfo(self) -> PasteTargetInfo:
        """
        Get: PasteTargetInfo(self: UpdateViewPasteTargetInfoCommand) -> PasteTargetInfo
        Set: PasteTargetInfo(self: UpdateViewPasteTargetInfoCommand) = value
        """
        ...



class UpdateViewSelectionDescriptionCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewSelectionDescriptionCommand() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: UpdateViewSelectionDescriptionCommand) -> str
        Set: Description(self: UpdateViewSelectionDescriptionCommand) = value
        """
        ...



class UpdateViewSelectionDisplayNameCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewSelectionDisplayNameCommand() """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: UpdateViewSelectionDisplayNameCommand) -> str
        Set: DisplayName(self: UpdateViewSelectionDisplayNameCommand) = value
        """
        ...



class UpdateViewSelectionHelpTopicCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewSelectionHelpTopicCommand() """
    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: UpdateViewSelectionHelpTopicCommand) -> str
        Set: HelpTopic(self: UpdateViewSelectionHelpTopicCommand) = value
        """
        ...



class UpdateViewSharedDataCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewSharedDataCommand() """
    @property
    def UpdatedSharedData(self) -> SharedDataObjectUpdate:
        """
        Get: UpdatedSharedData(self: UpdateViewSharedDataCommand) -> SharedDataObjectUpdate
        Set: UpdatedSharedData(self: UpdateViewSharedDataCommand) = value
        """
        ...



class UpdateViewStandardVerbsCommand(ViewCommand): # skipped bases: <type 'object'>
    """ UpdateViewStandardVerbsCommand() """
    @property
    def EnabledVerbs(self) -> StandardVerbs:
        """
        Get: EnabledVerbs(self: UpdateViewStandardVerbsCommand) -> StandardVerbs
        Set: EnabledVerbs(self: UpdateViewStandardVerbsCommand) = value
        """
        ...



class ViewActionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ViewActionType, values: Global (1), Help (3), Mode (2), Selection (0) """
    Global: ViewActionType = ...
    Help: ViewActionType = ...
    Mode: ViewActionType = ...
    Selection: ViewActionType = ...
    value__ = ...


class ViewKeyboardFocusNotification(Notification): # skipped bases: <type 'object'>
    """ ViewKeyboardFocusNotification() """
    @property
    def Forward(self) -> bool:
        """
        Get: Forward(self: ViewKeyboardFocusNotification) -> bool
        Set: Forward(self: ViewKeyboardFocusNotification) = value
        """
        ...



class ViewSelectionShowCustomHelpTopicNotification(Notification): # skipped bases: <type 'object'>
    """ ViewSelectionShowCustomHelpTopicNotification() """
    pass

class ViewSetData: # skipped bases: <type 'object'>, <type 'object'>
    """
    ViewSetData()
    ViewSetData(viewDescriptionData: Array[ViewDescriptionData])
    """
    @property
    def DefaultIndex(self) -> int:
        """
        Get: DefaultIndex(self: ViewSetData) -> int
        Set: DefaultIndex(self: ViewSetData) = value
        """
        ...

    @property
    def ViewSetId(self) -> int:
        """
        Get: ViewSetId(self: ViewSetData) -> int
        Set: ViewSetId(self: ViewSetData) = value
        """
        ...


    def GetViewDescriptions(self) -> Array:
        """ GetViewDescriptions(self: ViewSetData) -> Array[ViewDescriptionData] """
        ...

    def SetViewDescriptions(self, viewDescriptionData:Array): # -> 
        """ SetViewDescriptions(self: ViewSetData, viewDescriptionData: Array[ViewDescriptionData]) """
        ...


class WindowsMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ WindowsMessage(m: Message) """
    @property
    def LParam(self) -> IntPtr:
        """ Get: LParam(self: WindowsMessage) -> IntPtr """
        ...

    @property
    def Message(self) -> UInt32:
        """ Get: Message(self: WindowsMessage) -> UInt32 """
        ...

    @property
    def WParam(self) -> IntPtr:
        """ Get: WParam(self: WindowsMessage) -> IntPtr """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: WindowsMessage, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: WindowsMessage) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


