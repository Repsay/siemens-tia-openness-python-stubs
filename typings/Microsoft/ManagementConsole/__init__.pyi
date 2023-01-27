# encoding: utf-8
# module Microsoft.ManagementConsole calls itself ManagementConsole
# from MMCEx, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, MMCFxCommon, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.ManagementConsole, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.ManagementConsole.Internal import (DragAndDropVerb, 
    MessageViewIcon, StandardVerbs)

from Microsoft.Office.Interop.Outlook import PropertyPage

from Microsoft.SqlServer.Management.Smo import AsyncStatus

from System import (Action, Array, Attribute, Console, Enum, EventArgs, Guid, 
    Type, Uri)

from System.Collections import (CollectionBase, ICollection, IComparer, 
    IEnumerator)

from System.ComponentModel import ISynchronizeInvoke

from System.Configuration.Install import Installer

from System.Diagnostics import TraceSource

from System.Drawing import Color, Image

from System.IdentityModel.Protocols.WSTrust import Status

from System.Web.UI import Control

from System.Web.UI.WebControls import FormView

from System.Windows.Forms import BaseCollection, DialogResult, Form, View

from typing import Self

from Windows.Foundation import Point

"""The following names are not found in the module: (
    ActionsPaneItemCollection, BoundEvent, MmcListViewColumnCollection, 
    MmcListViewColumnFormat, MmcListViewMode, MmcListViewOptions, 
    NamespaceSnapInBase, NodeSubItemDisplayNameCollection, PropertySheet, 
    ResultNodeCollection, ScopeNode, ScopeNodeCollection, 
    SelectedNodeCollection, SelectionData, SharedDataItem, 
    SnapInHelpTopicCallback, SnapInImageList, SyncStatus, 
    ViewDescriptionCollection, WritableSharedData, WritableSharedDataItem, 
    field#)
"""

# no functions
# classes

class ActionsPaneItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: ActionsPaneItem) -> object
        Set: Tag(self: ActionsPaneItem) = value
        """
        ...



class ActionsPaneExtendedItem(ActionsPaneItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ActionsPaneExtendedItem) -> str
        Set: Description(self: ActionsPaneExtendedItem) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ActionsPaneExtendedItem) -> str
        Set: DisplayName(self: ActionsPaneExtendedItem) = value
        """
        ...

    @property
    def ImageIndex(self) -> int:
        """
        Get: ImageIndex(self: ActionsPaneExtendedItem) -> int
        Set: ImageIndex(self: ActionsPaneExtendedItem) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ActionsPaneExtendedItem) -> str
        Set: LanguageIndependentName(self: ActionsPaneExtendedItem) = value
        """
        ...

    @property
    def MnemonicDisplayName(self) -> str:
        """
        Get: MnemonicDisplayName(self: ActionsPaneExtendedItem) -> str
        Set: MnemonicDisplayName(self: ActionsPaneExtendedItem) = value
        """
        ...



class ActionBase(ActionsPaneExtendedItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bulleted(self) -> bool:
        """
        Get: Bulleted(self: ActionBase) -> bool
        Set: Bulleted(self: ActionBase) = value
        """
        ...

    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: ActionBase) -> bool
        Set: Checked(self: ActionBase) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ActionBase) -> bool
        Set: Enabled(self: ActionBase) = value
        """
        ...



class Action(ActionBase): # skipped bases: <type 'object'>
    """
    Action()
    Action(displayName: str, description: str)
    Action(displayName: str, description: str, imageIndex: int)
    Action(displayName: str, description: str, imageIndex: int, tag: object)
    """
    def ActionEventHandler(self, *args): #cannot find CLR method
        """ ActionEventHandler(object: object, method: IntPtr) """
        ...

    def __new__(cls, displayName:str = ..., description:str = ..., imageIndex:int = ..., tag:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, imageIndex: int)
        __new__(cls: type, displayName: str, description: str, imageIndex: int, tag: object)
        """
        ...

    Triggered = ...


class ActionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActionEventArgs(action: Action, status: AsyncStatus) """
    @property
    def Action(self) -> Action:
        """ Get: Action(self: ActionEventArgs) -> Action """
        ...

    @property
    def Status(self) -> AsyncStatus:
        """ Get: Status(self: ActionEventArgs) -> AsyncStatus """
        ...


    def __new__(cls, action:Action, status:AsyncStatus) -> Self:
        """ __new__(cls: type, action: Action, status: AsyncStatus) """
        ...


class ActionGroup(ActionsPaneExtendedItem): # skipped bases: <type 'object'>
    """
    ActionGroup()
    ActionGroup(displayName: str, description: str)
    ActionGroup(displayName: str, description: str, imageIndex: int)
    ActionGroup(displayName: str, description: str, imageIndex: int, tag: object)
    """
    @property
    def Items(self): # -> ActionsPaneItemCollection
        """ Get: Items(self: ActionGroup) -> ActionsPaneItemCollection """
        ...

    @property
    def RenderAsRegion(self) -> bool:
        """
        Get: RenderAsRegion(self: ActionGroup) -> bool
        Set: RenderAsRegion(self: ActionGroup) = value
        """
        ...


    def __new__(cls, displayName:str = ..., description:str = ..., imageIndex:int = ..., tag:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, imageIndex: int)
        __new__(cls: type, displayName: str, description: str, imageIndex: int, tag: object)
        """
        ...


class ActionSeparator(ActionsPaneItem): # skipped bases: <type 'object'>
    """ ActionSeparator() """
    pass

class BaseCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: BaseCollection) -> object """
        ...


    def AddRange(self, *args): #cannot find CLR method
        """ AddRange(self: BaseCollection, items: Array[object]) """
        ...

    def Contains(self, item:object) -> bool:
        """ Contains(self: BaseCollection, item: object) -> bool """
        ...

    def Insert(self, *args): #cannot find CLR method
        """ Insert(self: BaseCollection, index: int, item: object) """
        ...

    def InsertRange(self, *args): #cannot find CLR method
        """ InsertRange(self: BaseCollection, index: int, items: Array[object]) """
        ...

    def OnItemsAdded(self, *args): #cannot find CLR method
        """ OnItemsAdded(self: BaseCollection, index: int, items: Array[object]) """
        ...

    def OnItemsRemoved(self, *args): #cannot find CLR method
        """ OnItemsRemoved(self: BaseCollection, index: int, items: Array[object]) """
        ...


class ActionsPaneItemCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ActionsPaneItemCollection() """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ActionsPaneItemCollection, array: Array[ActionsPaneItem], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ActionsPaneItemCollection) -> Array[ActionsPaneItem] """
        ...


class Status: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Title(self) -> str:
        """
        Get: Title(self: Status) -> str
        Set: Title(self: Status) = value
        """
        ...


    def Complete(self, completionText:str, success:bool): # -> 
        """ Complete(self: Status, completionText: str, success: bool) """
        ...

    def ReportProgress(self, workProcessed:int, totalWork:int, statusText:str): # -> 
        """ ReportProgress(self: Status, workProcessed: int, totalWork: int, statusText: str) """
        ...


class AsyncStatus(Status): # skipped bases: <type 'object'>
    """ no doc """
    def EnableManualCompletion(self): # -> 
        """ EnableManualCompletion(self: AsyncStatus) """
        ...


class NodeId: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class CustomNodeId(NodeId): # skipped bases: <type 'object'>
    """
    CustomNodeId()
    CustomNodeId(customId: Array[Byte])
    """
    def GetCustomId(self) -> Array:
        """ GetCustomId(self: CustomNodeId) -> Array[Byte] """
        ...

    def SetCustomId(self, customId:Array): # -> 
        """ SetCustomId(self: CustomNodeId, customId: Array[Byte]) """
        ...

    def __new__(cls, customId:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, customId: Array[Byte])
        """
        ...


class CustomStatus(Status): # skipped bases: <type 'object'>
    """ CustomStatus() """
    def Start(self, owner): # ->  # Not found arg types: {'owner': 'ScopeNode'}
        """ Start(self: CustomStatus, owner: ScopeNode) """
        ...


class DisplayNameNodeId(NodeId): # skipped bases: <type 'object'>
    """
    DisplayNameNodeId()
    DisplayNameNodeId(displayName: str)
    """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: DisplayNameNodeId) -> str
        Set: DisplayName(self: DisplayNameNodeId) = value
        """
        ...


    def __new__(cls, displayName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str)
        """
        ...


class DragAndDropVerb(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DragAndDropVerb, values: CopyHere (0), MoveHere (1) """
    CopyHere: DragAndDropVerb = ...
    MoveHere: DragAndDropVerb = ...
    value__ = ...


class ExecutiveTraceEventId(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExecutiveTraceEventId, values: Framework (12), FxComponent (3), FxComponentData (2), FxDataObject (4), FxSnapInFactory (10), Operations (11), RequestStatus (7), SnapInDocument (1), SnapInHost (0), SnapInThread (8), UIThread (9), ViewHost (6), ViewZone (5) """
    Framework: ExecutiveTraceEventId = ...
    FxComponent: ExecutiveTraceEventId = ...
    FxComponentData: ExecutiveTraceEventId = ...
    FxDataObject: ExecutiveTraceEventId = ...
    FxSnapInFactory: ExecutiveTraceEventId = ...
    Operations: ExecutiveTraceEventId = ...
    RequestStatus: ExecutiveTraceEventId = ...
    SnapInDocument: ExecutiveTraceEventId = ...
    SnapInHost: ExecutiveTraceEventId = ...
    SnapInThread: ExecutiveTraceEventId = ...
    UIThread: ExecutiveTraceEventId = ...
    value__ = ...
    ViewHost: ExecutiveTraceEventId = ...
    ViewZone: ExecutiveTraceEventId = ...


class View: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActionsPaneItems(self) -> ActionsPaneItemCollection:
        """ Get: ActionsPaneItems(self: View) -> ActionsPaneItemCollection """
        ...

    @property
    def DescriptionBarText(self) -> str:
        """
        Get: DescriptionBarText(self: View) -> str
        Set: DescriptionBarText(self: View) = value
        """
        ...

    @property
    def IsModified(self) -> bool:
        """
        Get: IsModified(self: View) -> bool
        Set: IsModified(self: View) = value
        """
        ...

    @property
    def ModeActionsPaneItems(self) -> ActionsPaneItemCollection:
        """ Get: ModeActionsPaneItems(self: View) -> ActionsPaneItemCollection """
        ...

    @property
    def ScopeNode(self): # -> ScopeNode
        """ Get: ScopeNode(self: View) -> ScopeNode """
        ...

    @property
    def SelectionData(self): # -> SelectionData
        """ Get: SelectionData(self: View) -> SelectionData """
        ...

    @property
    def SharedTag(self) -> object:
        """
        Get: SharedTag(self: View) -> object
        Set: SharedTag(self: View) = value
        """
        ...

    @property
    def SnapIn(self): # -> NamespaceSnapInBase
        """ Get: SnapIn(self: View) -> NamespaceSnapInBase """
        ...

    @property
    def ViewDescriptionTag(self) -> object:
        """ Get: ViewDescriptionTag(self: View) -> object """
        ...


    def ExpandScopeNode(self, targetNode): # ->  # Not found arg types: {'targetNode': 'ScopeNode'}
        """ ExpandScopeNode(self: View, targetNode: ScopeNode) """
        ...

    def IsScopeNodeVisuallyExpanded(self, node) -> bool: # Not found arg types: {'node': 'ScopeNode'}
        """ IsScopeNodeVisuallyExpanded(self: View, node: ScopeNode) -> bool """
        ...

    def OnAction(self, *args): #cannot find CLR method
        """ OnAction(self: View, action: Action, status: AsyncStatus) """
        ...

    def OnAddPropertyPages(self, *args): #cannot find CLR method
        """ OnAddPropertyPages(self: View, propertyPageCollection: PropertyPageCollection) """
        ...

    def OnCut(self, *args): #cannot find CLR method
        """ OnCut(self: View, selectionValue: object, status: AsyncStatus) """
        ...

    def OnDelete(self, *args): #cannot find CLR method
        """ OnDelete(self: View, status: SyncStatus) """
        ...

    def OnGetSharedData(self, *args): #cannot find CLR method
        """ OnGetSharedData(self: View, selectionValue: object, item: WritableSharedDataItem, status: SyncStatus) -> Array[Byte] """
        ...

    def OnHide(self, *args): #cannot find CLR method
        """ OnHide(self: View) """
        ...

    def OnInitialize(self, *args): #cannot find CLR method
        """ OnInitialize(self: View, status: AsyncStatus) """
        ...

    def OnLoadCustomData(self, *args): #cannot find CLR method
        """ OnLoadCustomData(self: View, status: AsyncStatus, customData: Array[Byte]) """
        ...

    def OnModeAction(self, *args): #cannot find CLR method
        """ OnModeAction(self: View, action: Action, status: AsyncStatus) """
        ...

    def OnPaste(self, *args): #cannot find CLR method
        """ OnPaste(self: View, data: SharedData, pasteType: DragAndDropVerb, status: SyncStatus) -> bool """
        ...

    def OnPrint(self, *args): #cannot find CLR method
        """ OnPrint(self: View, status: SyncStatus) """
        ...

    def OnRefresh(self, *args): #cannot find CLR method
        """ OnRefresh(self: View, status: AsyncStatus) """
        ...

    def OnRename(self, *args): #cannot find CLR method
        """ OnRename(self: View, newText: str, status: SyncStatus) """
        ...

    def OnSaveCustomData(self, *args): #cannot find CLR method
        """ OnSaveCustomData(self: View, status: SyncStatus) -> Array[Byte] """
        ...

    def OnSelectionAction(self, *args): #cannot find CLR method
        """ OnSelectionAction(self: View, action: Action, status: AsyncStatus) """
        ...

    def OnSharedDataChangeRequested(self, *args): #cannot find CLR method
        """ OnSharedDataChangeRequested(self: View, selectionValue: object, item: WritableSharedDataItem, newValue: Array[Byte], status: AsyncStatus) """
        ...

    def OnShow(self, *args): #cannot find CLR method
        """ OnShow(self: View) """
        ...

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: View, status: SyncStatus) """
        ...

    def OnSyncAction(self, *args): #cannot find CLR method
        """ OnSyncAction(self: View, action: SyncAction, status: SyncStatus) """
        ...

    def OnSyncModeAction(self, *args): #cannot find CLR method
        """ OnSyncModeAction(self: View, action: SyncAction, status: SyncStatus) """
        ...

    def OnSyncSelectionAction(self, *args): #cannot find CLR method
        """ OnSyncSelectionAction(self: View, action: SyncAction, status: SyncStatus) """
        ...

    def SelectScopeNode(self, *__args): # ->  # Not found arg types: {'*__args': 'ScopeNode'}
        """ SelectScopeNode(self: View, scopeNode: ScopeNode)SelectScopeNode(self: View, startNode: ScopeNode, relativePath: Array[NodeId]) """
        ...


class FormView(View): # skipped bases: <type 'object'>
    """ FormView() """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: FormView) -> Control """
        ...

    @property
    def ControlType(self) -> Type:
        """ Get: ControlType(self: FormView) -> Type """
        ...


    def ShowContextMenu(self, point:Point, onResultItem:bool): # -> 
        """ ShowContextMenu(self: FormView, point: Point, onResultItem: bool) """
        ...


class ViewDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ViewDescription) -> str
        Set: DisplayName(self: ViewDescription) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ViewDescription) -> str
        Set: LanguageIndependentName(self: ViewDescription) = value
        """
        ...

    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: ViewDescription) -> object
        Set: Tag(self: ViewDescription) = value
        """
        ...

    @property
    def ViewType(self) -> Type:
        """
        Get: ViewType(self: ViewDescription) -> Type
        Set: ViewType(self: ViewDescription) = value
        """
        ...



class FormViewDescription(ViewDescription): # skipped bases: <type 'object'>
    """
    FormViewDescription()
    FormViewDescription(controlType: Type)
    """
    @property
    def ControlType(self) -> Type:
        """
        Get: ControlType(self: FormViewDescription) -> Type
        Set: ControlType(self: FormViewDescription) = value
        """
        ...


    def __new__(cls, controlType:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, controlType: Type)
        """
        ...


class HtmlView(View): # skipped bases: <type 'object'>
    """ HtmlView() """
    @property
    def Url(self) -> Uri:
        """ Get: Url(self: HtmlView) -> Uri """
        ...



class HtmlViewDescription(ViewDescription): # skipped bases: <type 'object'>
    """
    HtmlViewDescription()
    HtmlViewDescription(url: Uri)
    """
    @property
    def Url(self) -> Uri:
        """
        Get: Url(self: HtmlViewDescription) -> Uri
        Set: Url(self: HtmlViewDescription) = value
        """
        ...


    def __new__(cls, url:Uri = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, url: Uri)
        """
        ...


class IFormViewControl: # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self, view:FormView): # -> 
        """ Initialize(self: IFormViewControl, view: FormView) """
        ...


class IResultNodeComparer(IComparer): # skipped bases: <type 'object'>
    """ no doc """
    def SetColumnIndex(self, index:int): # -> 
        """ SetColumnIndex(self: IResultNodeComparer, index: int) """
        ...


class LanguageIndependentNameNodeId(NodeId): # skipped bases: <type 'object'>
    """
    LanguageIndependentNameNodeId()
    LanguageIndependentNameNodeId(languageIndependentName: str)
    """
    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: LanguageIndependentNameNodeId) -> str
        Set: LanguageIndependentName(self: LanguageIndependentNameNodeId) = value
        """
        ...


    def __new__(cls, languageIndependentName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, languageIndependentName: str)
        """
        ...


class MessageView(View): # skipped bases: <type 'object'>
    """ MessageView() """
    @property
    def BodyText(self) -> str:
        """
        Get: BodyText(self: MessageView) -> str
        Set: BodyText(self: MessageView) = value
        """
        ...

    @property
    def IconId(self) -> MessageViewIcon:
        """
        Get: IconId(self: MessageView) -> MessageViewIcon
        Set: IconId(self: MessageView) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: MessageView) -> str
        Set: Title(self: MessageView) = value
        """
        ...


    def Update(self, title:str, bodyText:str, iconId:MessageViewIcon): # -> 
        """ Update(self: MessageView, title: str, bodyText: str, iconId: MessageViewIcon) """
        ...


class MessageViewDescription(ViewDescription): # skipped bases: <type 'object'>
    """
    MessageViewDescription()
    MessageViewDescription(title: str, bodyText: str, iconId: MessageViewIcon)
    """
    @property
    def BodyText(self) -> str:
        """
        Get: BodyText(self: MessageViewDescription) -> str
        Set: BodyText(self: MessageViewDescription) = value
        """
        ...

    @property
    def IconId(self) -> MessageViewIcon:
        """
        Get: IconId(self: MessageViewDescription) -> MessageViewIcon
        Set: IconId(self: MessageViewDescription) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: MessageViewDescription) -> str
        Set: Title(self: MessageViewDescription) = value
        """
        ...


    def __new__(cls, title:str = ..., bodyText:str = ..., iconId:MessageViewIcon = ...) -> Self:
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


class MmcListView(View): # skipped bases: <type 'object'>
    """ MmcListView() """
    @property
    def Columns(self): # -> MmcListViewColumnCollection
        """ Get: Columns(self: MmcListView) -> MmcListViewColumnCollection """
        ...

    @property
    def Mode(self): # -> MmcListViewMode
        """
        Get: Mode(self: MmcListView) -> MmcListViewMode
        Set: Mode(self: MmcListView) = value
        """
        ...

    @property
    def Options(self): # -> MmcListViewOptions
        """ Get: Options(self: MmcListView) -> MmcListViewOptions """
        ...

    @property
    def ResultNodes(self): # -> ResultNodeCollection
        """ Get: ResultNodes(self: MmcListView) -> ResultNodeCollection """
        ...

    @property
    def SelectedNodes(self): # -> SelectedNodeCollection
        """ Get: SelectedNodes(self: MmcListView) -> SelectedNodeCollection """
        ...

    @property
    def Sorter(self) -> IResultNodeComparer:
        """
        Get: Sorter(self: MmcListView) -> IResultNodeComparer
        Set: Sorter(self: MmcListView) = value
        """
        ...


    def OnColumnVisibilityChanged(self, *args): #cannot find CLR method
        """ OnColumnVisibilityChanged(self: MmcListView) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: MmcListView, status: SyncStatus) """
        ...

    def OnSortCompleted(self, *args): #cannot find CLR method
        """ OnSortCompleted(self: MmcListView, columnIndex: int, descending: bool) """
        ...

    def Sort(self, columnIndex:int, descending:bool = ..., hideSortIcon:bool = ...): # -> 
        """ Sort(self: MmcListView, columnIndex: int)Sort(self: MmcListView, columnIndex: int, descending: bool)Sort(self: MmcListView, columnIndex: int, descending: bool, hideSortIcon: bool) """
        ...


class MmcListViewColumn: # skipped bases: <type 'object'>, <type 'object'>
    """
    MmcListViewColumn()
    MmcListViewColumn(title: str)
    MmcListViewColumn(title: str, width: int)
    MmcListViewColumn(title: str, width: int, format: MmcListViewColumnFormat)
    MmcListViewColumn(title: str, width: int, format: MmcListViewColumnFormat, visible: bool)
    """
    @property
    def Format(self): # -> MmcListViewColumnFormat
        """
        Get: Format(self: MmcListViewColumn) -> MmcListViewColumnFormat
        Set: Format(self: MmcListViewColumn) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: MmcListViewColumn) -> str
        Set: Title(self: MmcListViewColumn) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: MmcListViewColumn) -> bool
        Set: Visible(self: MmcListViewColumn) = value
        """
        ...


    def SetWidth(self, width:int): # -> 
        """ SetWidth(self: MmcListViewColumn, width: int) """
        ...


class MmcListViewColumnCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MmcListViewColumnCollection, array: Array[MmcListViewColumn], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: MmcListViewColumnCollection) -> Array[MmcListViewColumn] """
        ...


class MmcListViewColumnFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MmcListViewColumnFormat, values: Center (1), Left (0), Right (2) """
    Center: MmcListViewColumnFormat = ...
    Left: MmcListViewColumnFormat = ...
    Right: MmcListViewColumnFormat = ...
    value__ = ...


class MmcListViewDescription(ViewDescription): # skipped bases: <type 'object'>
    """
    MmcListViewDescription()
    MmcListViewDescription(options: MmcListViewOptions)
    """
    @property
    def Options(self): # -> MmcListViewOptions
        """
        Get: Options(self: MmcListViewDescription) -> MmcListViewOptions
        Set: Options(self: MmcListViewDescription) = value
        """
        ...


    def __new__(cls, options = ...) -> Self: # Not found arg types: {'options': 'MmcListViewOptions'}
        """
        __new__(cls: type)
        __new__(cls: type, options: MmcListViewOptions)
        """
        ...


class MmcListViewMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MmcListViewMode, values: LargeIcon (2), List (1), Report (0), SmallIcon (3) """
    LargeIcon: MmcListViewMode = ...
    List: MmcListViewMode = ...
    Report: MmcListViewMode = ...
    SmallIcon: MmcListViewMode = ...
    value__ = ...


class MmcListViewOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MmcListViewOptions, values: All (255), AllowPasteOnResultNodes (32), AllowUserInitiatedModeChanges (128), DisableUserInitiatedSort (8), ExcludeScopeNodes (4), HideSelection (2), None (0), SingleSelect (1), UseCustomSorting (16), UseFontLinking (64) """
    All: MmcListViewOptions = ...
    AllowPasteOnResultNodes: MmcListViewOptions = ...
    AllowUserInitiatedModeChanges: MmcListViewOptions = ...
    DisableUserInitiatedSort: MmcListViewOptions = ...
    ExcludeScopeNodes: MmcListViewOptions = ...
    HideSelection: MmcListViewOptions = ...
    SingleSelect: MmcListViewOptions = ...
    UseCustomSorting: MmcListViewOptions = ...
    UseFontLinking: MmcListViewOptions = ...
    value__ = ...


class SnapInBase(ISynchronizeInvoke): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self):
        ...

    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: SnapInBase) -> object
        Set: Tag(self: SnapInBase) = value
        """
        ...


    def OnInitialize(self, *args): #cannot find CLR method
        """ OnInitialize(self: SnapInBase) """
        ...

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: SnapInBase, status: AsyncStatus) """
        ...

    def RegisterCurrentThreadForUI(self): # -> 
        """ RegisterCurrentThreadForUI(self: SnapInBase) """
        ...

    def ShowHelpTopic(self, helpTopic:str): # -> 
        """ ShowHelpTopic(self: SnapInBase, helpTopic: str) """
        ...

    def UnregisterCurrentThreadForUI(self): # -> 
        """ UnregisterCurrentThreadForUI(self: SnapInBase) """
        ...


class NamespaceSnapInBase(SnapInBase): # skipped bases: <type 'ISynchronizeInvoke'>, <type 'object'>
    """ no doc """
    @property
    def Console(self) -> Console:
        """ Get: Console(self: NamespaceSnapInBase) -> Console """
        ...

    @property
    def IsModified(self) -> bool:
        """
        Get: IsModified(self: NamespaceSnapInBase) -> bool
        Set: IsModified(self: NamespaceSnapInBase) = value
        """
        ...

    @property
    def LargeImages(self): # -> SnapInImageList
        """ Get: LargeImages(self: NamespaceSnapInBase) -> SnapInImageList """
        ...

    @property
    def SmallImages(self): # -> SnapInImageList
        """ Get: SmallImages(self: NamespaceSnapInBase) -> SnapInImageList """
        ...


    def OnLoadCustomData(self, *args): #cannot find CLR method
        """ OnLoadCustomData(self: NamespaceSnapInBase, status: AsyncStatus, persistenceData: Array[Byte]) """
        ...

    def OnSaveCustomData(self, *args): #cannot find CLR method
        """ OnSaveCustomData(self: NamespaceSnapInBase, status: SyncStatus) -> Array[Byte] """
        ...

    def UpdateSnapInExtensions(self): # -> 
        """ UpdateSnapInExtensions(self: NamespaceSnapInBase) """
        ...


class Node: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: Node) -> str
        Set: DisplayName(self: Node) = value
        """
        ...

    @property
    def Id(self):
        ...

    @property
    def ImageIndex(self) -> int:
        """
        Get: ImageIndex(self: Node) -> int
        Set: ImageIndex(self: Node) = value
        """
        ...

    @property
    def SnapIn(self) -> NamespaceSnapInBase:
        """ Get: SnapIn(self: Node) -> NamespaceSnapInBase """
        ...

    @property
    def SubItemDisplayNames(self): # -> NodeSubItemDisplayNameCollection
        """
        Get: SubItemDisplayNames(self: Node) -> NodeSubItemDisplayNameCollection
        Set: SubItemDisplayNames(self: Node) = value
        """
        ...

    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: Node) -> object
        Set: Tag(self: Node) = value
        """
        ...



class NodeSubItemDisplayNameCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: NodeSubItemDisplayNameCollection, array: Array[str], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: NodeSubItemDisplayNameCollection) -> Array[str] """
        ...


class NodeTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NodeTypeAttribute(guid: str) """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: NodeTypeAttribute) -> str
        Set: Description(self: NodeTypeAttribute) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: NodeTypeAttribute) -> Guid """
        ...


    def __new__(cls, guid:str) -> Self:
        """ __new__(cls: type, guid: str) """
        ...


class PropertyPage: # skipped bases: <type 'object'>, <type 'object'>
    """ PropertyPage() """
    @property
    def Control(self) -> Control:
        """
        Get: Control(self: PropertyPage) -> Control
        Set: Control(self: PropertyPage) = value
        """
        ...

    @property
    def Destroyed(self) -> bool:
        """ Get: Destroyed(self: PropertyPage) -> bool """
        ...

    @property
    def Dirty(self) -> bool:
        """
        Get: Dirty(self: PropertyPage) -> bool
        Set: Dirty(self: PropertyPage) = value
        """
        ...

    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: PropertyPage) -> str
        Set: HelpTopic(self: PropertyPage) = value
        """
        ...

    @property
    def Initialized(self) -> bool:
        """ Get: Initialized(self: PropertyPage) -> bool """
        ...

    @property
    def ParentSheet(self): # -> PropertySheet
        """ Get: ParentSheet(self: PropertyPage) -> PropertySheet """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: PropertyPage) -> str
        Set: Title(self: PropertyPage) = value
        """
        ...


    def OnApply(self, *args): #cannot find CLR method
        """ OnApply(self: PropertyPage) -> bool """
        ...

    def OnCancel(self, *args): #cannot find CLR method
        """ OnCancel(self: PropertyPage) """
        ...

    def OnDestroy(self, *args): #cannot find CLR method
        """ OnDestroy(self: PropertyPage) """
        ...

    def OnInitialize(self, *args): #cannot find CLR method
        """ OnInitialize(self: PropertyPage) """
        ...

    def OnKillActive(self, *args): #cannot find CLR method
        """ OnKillActive(self: PropertyPage) -> bool """
        ...

    def OnOK(self, *args): #cannot find CLR method
        """ OnOK(self: PropertyPage) -> bool """
        ...

    def OnSetActive(self, *args): #cannot find CLR method
        """ OnSetActive(self: PropertyPage) """
        ...

    def QueryCancel(self, *args): #cannot find CLR method
        """ QueryCancel(self: PropertyPage) -> bool """
        ...


class PropertyPageCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ PropertyPageCollection() """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PropertyPageCollection, array: Array[PropertyPage], index: int) """
        ...


class PropertySheet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: PropertySheet) -> int """
        ...

    @property
    def SelectionObject(self) -> object:
        """ Get: SelectionObject(self: PropertySheet) -> object """
        ...

    @property
    def SnapIn(self) -> SnapInBase:
        """ Get: SnapIn(self: PropertySheet) -> SnapInBase """
        ...


    def CancelToClose(self): # -> 
        """ CancelToClose(self: PropertySheet) """
        ...

    def GetPropertyPage(self, index:int) -> PropertyPage:
        """ GetPropertyPage(self: PropertySheet, index: int) -> PropertyPage """
        ...

    def SetActivePage(self, index:int): # -> 
        """ SetActivePage(self: PropertySheet, index: int) """
        ...

    def Show(self, form:Form): # -> 
        """ Show(self: PropertySheet, form: Form) """
        ...

    def ShowDialog(self, *__args:Form) -> DialogResult:
        """
        ShowDialog(self: PropertySheet, form: Form) -> DialogResult
        ShowDialog(self: PropertySheet, form: Form, waitCursor: WaitCursor) -> DialogResult
        ShowDialog(self: PropertySheet, commonDialog: CommonDialog) -> DialogResult
        ShowDialog(self: PropertySheet, parameters: MessageBoxParameters) -> DialogResult
        """
        ...


class PublishesNodeTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PublishesNodeTypeAttribute(guid: str) """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: PublishesNodeTypeAttribute) -> str
        Set: Description(self: PublishesNodeTypeAttribute) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: PublishesNodeTypeAttribute) -> Guid """
        ...


    def __new__(cls, guid:str) -> Self:
        """ __new__(cls: type, guid: str) """
        ...


class ResultNode(Node): # skipped bases: <type 'object'>
    """ ResultNode() """
    def SendSelectionRequest(self, selected:bool): # -> 
        """ SendSelectionRequest(self: ResultNode, selected: bool) """
        ...


class ResultNodeCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ResultNodeCollection, array: Array[ResultNode], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ResultNodeCollection) -> Array[ResultNode] """
        ...


class ScopeNode(Node): # skipped bases: <type 'object'>
    """
    ScopeNode()
    ScopeNode(nodeType: Guid)
    ScopeNode(hideExpandIcon: bool)
    ScopeNode(nodeType: Guid, hideExpandIcon: bool)
    """
    @property
    def ActionsPaneHelpItems(self) -> ActionsPaneItemCollection:
        """ Get: ActionsPaneHelpItems(self: ScopeNode) -> ActionsPaneItemCollection """
        ...

    @property
    def ActionsPaneItems(self) -> ActionsPaneItemCollection:
        """ Get: ActionsPaneItems(self: ScopeNode) -> ActionsPaneItemCollection """
        ...

    @property
    def Children(self): # -> ScopeNodeCollection
        """ Get: Children(self: ScopeNode) -> ScopeNodeCollection """
        ...

    @property
    def DefaultDragAndDropVerb(self) -> DragAndDropVerb:
        """
        Get: DefaultDragAndDropVerb(self: ScopeNode) -> DragAndDropVerb
        Set: DefaultDragAndDropVerb(self: ScopeNode) = value
        """
        ...

    @property
    def EnabledStandardVerbs(self) -> StandardVerbs:
        """
        Get: EnabledStandardVerbs(self: ScopeNode) -> StandardVerbs
        Set: EnabledStandardVerbs(self: ScopeNode) = value
        """
        ...

    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: ScopeNode) -> str
        Set: HelpTopic(self: ScopeNode) = value
        """
        ...

    @property
    def LanguageIndependentName(self) -> str:
        """
        Get: LanguageIndependentName(self: ScopeNode) -> str
        Set: LanguageIndependentName(self: ScopeNode) = value
        """
        ...

    @property
    def NodeType(self) -> Guid:
        """ Get: NodeType(self: ScopeNode) -> Guid """
        ...

    @property
    def Parent(self) -> ScopeNode:
        """ Get: Parent(self: ScopeNode) -> ScopeNode """
        ...

    @property
    def SelectedImageIndex(self) -> int:
        """
        Get: SelectedImageIndex(self: ScopeNode) -> int
        Set: SelectedImageIndex(self: ScopeNode) = value
        """
        ...

    @property
    def SharedData(self): # -> WritableSharedData
        """ Get: SharedData(self: ScopeNode) -> WritableSharedData """
        ...

    @property
    def ViewDescriptions(self): # -> ViewDescriptionCollection
        """
        Get: ViewDescriptions(self: ScopeNode) -> ViewDescriptionCollection
        Set: ViewDescriptions(self: ScopeNode) = value
        """
        ...


    def GetAllowedClipboardFormatIdsForPaste(self) -> Array:
        """ GetAllowedClipboardFormatIdsForPaste(self: ScopeNode) -> Array[str] """
        ...

    def OnAction(self, *args): #cannot find CLR method
        """ OnAction(self: ScopeNode, action: Action, status: AsyncStatus) """
        ...

    def OnAddPropertyPages(self, *args): #cannot find CLR method
        """ OnAddPropertyPages(self: ScopeNode, propertyPageCollection: PropertyPageCollection) """
        ...

    def OnCut(self, *args): #cannot find CLR method
        """ OnCut(self: ScopeNode, status: AsyncStatus) """
        ...

    def OnDelete(self, *args): #cannot find CLR method
        """ OnDelete(self: ScopeNode, status: SyncStatus) """
        ...

    def OnExpand(self, *args): #cannot find CLR method
        """ OnExpand(self: ScopeNode, status: AsyncStatus) """
        ...

    def OnExpandFromLoad(self, *args): #cannot find CLR method
        """ OnExpandFromLoad(self: ScopeNode, status: SyncStatus) -> bool """
        ...

    def OnGetSharedData(self, *args): #cannot find CLR method
        """ OnGetSharedData(self: ScopeNode, item: WritableSharedDataItem, status: SyncStatus) -> Array[Byte] """
        ...

    def OnPaste(self, *args): #cannot find CLR method
        """ OnPaste(self: ScopeNode, data: SharedData, pasteType: DragAndDropVerb, status: SyncStatus) -> bool """
        ...

    def OnPrint(self, *args): #cannot find CLR method
        """ OnPrint(self: ScopeNode, status: SyncStatus) """
        ...

    def OnRefresh(self, *args): #cannot find CLR method
        """ OnRefresh(self: ScopeNode, status: AsyncStatus) """
        ...

    def OnRename(self, *args): #cannot find CLR method
        """ OnRename(self: ScopeNode, newText: str, status: SyncStatus) """
        ...

    def OnSharedDataChangeRequested(self, *args): #cannot find CLR method
        """ OnSharedDataChangeRequested(self: ScopeNode, item: WritableSharedDataItem, newValue: Array[Byte], status: AsyncStatus) """
        ...

    def OnSyncAction(self, *args): #cannot find CLR method
        """ OnSyncAction(self: ScopeNode, action: SyncAction, status: SyncStatus) """
        ...

    def SetAllowedClipboardFormatIdsForPaste(self, clipboardFormats:Array): # -> 
        """ SetAllowedClipboardFormatIdsForPaste(self: ScopeNode, clipboardFormats: Array[str]) """
        ...

    def ShowPropertySheet(self, title:str, hideApplyButton:bool = ...) -> bool:
        """
        ShowPropertySheet(self: ScopeNode, title: str) -> bool
        ShowPropertySheet(self: ScopeNode, title: str, hideApplyButton: bool) -> bool
        """
        ...

    def __new__(cls, *__args:Guid) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, nodeType: Guid)
        __new__(cls: type, hideExpandIcon: bool)
        __new__(cls: type, nodeType: Guid, hideExpandIcon: bool)
        """
        ...

    ActionsActivated = ...
    ActionsDeactivated = ...


class ScopeNodeCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ScopeNodeCollection() """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ScopeNodeCollection, array: Array[ScopeNode], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ScopeNodeCollection) -> Array[ScopeNode] """
        ...


class SelectedNodeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, node:Node) -> bool:
        """ Contains(self: SelectedNodeCollection, node: Node) -> bool """
        ...

    def IndexOf(self, node:Node) -> int:
        """ IndexOf(self: SelectedNodeCollection, node: Node) -> int """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: SelectedNodeCollection) -> Array[Node] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SelectionData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActionsPaneHelpItems(self) -> ActionsPaneItemCollection:
        """ Get: ActionsPaneHelpItems(self: SelectionData) -> ActionsPaneItemCollection """
        ...

    @property
    def ActionsPaneItems(self) -> ActionsPaneItemCollection:
        """ Get: ActionsPaneItems(self: SelectionData) -> ActionsPaneItemCollection """
        ...

    @property
    def DefaultDragAndDropVerb(self) -> DragAndDropVerb:
        """
        Get: DefaultDragAndDropVerb(self: SelectionData) -> DragAndDropVerb
        Set: DefaultDragAndDropVerb(self: SelectionData) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: SelectionData) -> str
        Set: Description(self: SelectionData) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: SelectionData) -> str
        Set: DisplayName(self: SelectionData) = value
        """
        ...

    @property
    def EnabledStandardVerbs(self) -> StandardVerbs:
        """
        Get: EnabledStandardVerbs(self: SelectionData) -> StandardVerbs
        Set: EnabledStandardVerbs(self: SelectionData) = value
        """
        ...

    @property
    def HelpTopic(self) -> str:
        """
        Get: HelpTopic(self: SelectionData) -> str
        Set: HelpTopic(self: SelectionData) = value
        """
        ...

    @property
    def SelectionObject(self) -> object:
        """ Get: SelectionObject(self: SelectionData) -> object """
        ...

    @property
    def SharedData(self): # -> WritableSharedData
        """
        Get: SharedData(self: SelectionData) -> WritableSharedData
        Set: SharedData(self: SelectionData) = value
        """
        ...


    def BeginUpdates(self): # -> 
        """ BeginUpdates(self: SelectionData) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SelectionData) """
        ...

    def EndUpdates(self): # -> 
        """ EndUpdates(self: SelectionData) """
        ...

    def GetAllowedClipboardFormatIdsForPaste(self) -> Array:
        """ GetAllowedClipboardFormatIdsForPaste(self: SelectionData) -> Array[str] """
        ...

    def GetUniqueNodeTypes(self) -> Array:
        """ GetUniqueNodeTypes(self: SelectionData) -> Array[Guid] """
        ...

    def SetAllowedClipboardFormatIdsForPaste(self, clipboardFormats:Array): # -> 
        """ SetAllowedClipboardFormatIdsForPaste(self: SelectionData, clipboardFormats: Array[str]) """
        ...

    def ShowPropertySheet(self, title:str, hideApplyButton:bool = ...) -> bool:
        """
        ShowPropertySheet(self: SelectionData, title: str) -> bool
        ShowPropertySheet(self: SelectionData, title: str, hideApplyButton: bool) -> bool
        """
        ...

    def Update(self, selectionValue:object, multiSelection:bool, uniqueNodeTypes:Array, sharedData): # ->  # Not found arg types: {'sharedData': 'WritableSharedData'}
        """ Update(self: SelectionData, selectionValue: object, multiSelection: bool, uniqueNodeTypes: Array[Guid], sharedData: WritableSharedData) """
        ...


class SharedData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Add(self, item): # ->  # Not found arg types: {'item': 'SharedDataItem'}
        """ Add(self: SharedData, item: SharedDataItem) """
        ...

    def GetItem(self, clipboardFormatId:str): # -> SharedDataItem
        """ GetItem(self: SharedData, clipboardFormatId: str) -> SharedDataItem """
        ...

    def Remove(self, clipboardFormatId:str): # -> 
        """ Remove(self: SharedData, clipboardFormatId: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SharedDataItemBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClipboardFormatId(self) -> str:
        """ Get: ClipboardFormatId(self: SharedDataItemBase) -> str """
        ...


    def GetData(self) -> Array:
        """ GetData(self: SharedDataItemBase) -> Array[Byte] """
        ...


class SharedDataItem(SharedDataItemBase): # skipped bases: <type 'object'>
    """ SharedDataItem(clipboardFormatId: str) """
    def RequestDataUpdate(self, value:Array): # -> 
        """ RequestDataUpdate(self: SharedDataItem, value: Array[Byte]) """
        ...

    def __new__(cls, clipboardFormatId:str) -> Self:
        """ __new__(cls: type, clipboardFormatId: str) """
        ...


class SnapIn(NamespaceSnapInBase): # skipped bases: <type 'ISynchronizeInvoke'>, <type 'object'>
    """ no doc """
    @property
    def RootNode(self) -> ScopeNode:
        """
        Get: RootNode(self: SnapIn) -> ScopeNode
        Set: RootNode(self: SnapIn) = value
        """
        ...


    def OnShowInitializationWizard(self, *args): #cannot find CLR method
        """ OnShowInitializationWizard(self: SnapIn) -> bool """
        ...


class SnapInAboutAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SnapInAboutAttribute(resourceModule: str) """
    @property
    def ApplicationBaseRelative(self) -> bool:
        """
        Get: ApplicationBaseRelative(self: SnapInAboutAttribute) -> bool
        Set: ApplicationBaseRelative(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def DescriptionId(self) -> int:
        """
        Get: DescriptionId(self: SnapInAboutAttribute) -> int
        Set: DescriptionId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def DisplayNameId(self) -> int:
        """
        Get: DisplayNameId(self: SnapInAboutAttribute) -> int
        Set: DisplayNameId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def FolderBitmapsColorMask(self) -> int:
        """
        Get: FolderBitmapsColorMask(self: SnapInAboutAttribute) -> int
        Set: FolderBitmapsColorMask(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def IconId(self) -> int:
        """
        Get: IconId(self: SnapInAboutAttribute) -> int
        Set: IconId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def LargeFolderBitmapId(self) -> int:
        """
        Get: LargeFolderBitmapId(self: SnapInAboutAttribute) -> int
        Set: LargeFolderBitmapId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def ResourceModule(self) -> str:
        """ Get: ResourceModule(self: SnapInAboutAttribute) -> str """
        ...

    @property
    def SmallFolderBitmapId(self) -> int:
        """
        Get: SmallFolderBitmapId(self: SnapInAboutAttribute) -> int
        Set: SmallFolderBitmapId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def SmallFolderSelectedBitmapId(self) -> int:
        """
        Get: SmallFolderSelectedBitmapId(self: SnapInAboutAttribute) -> int
        Set: SmallFolderSelectedBitmapId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def VendorId(self) -> int:
        """
        Get: VendorId(self: SnapInAboutAttribute) -> int
        Set: VendorId(self: SnapInAboutAttribute) = value
        """
        ...

    @property
    def VersionId(self) -> int:
        """
        Get: VersionId(self: SnapInAboutAttribute) -> int
        Set: VersionId(self: SnapInAboutAttribute) = value
        """
        ...


    def __new__(cls, resourceModule:str) -> Self:
        """ __new__(cls: type, resourceModule: str) """
        ...


class SnapInCallbackService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def RegisterSnapInHelpTopicCallback(snapInInstance:SnapInBase, callback): # ->  # Not found arg types: {'callback': 'SnapInHelpTopicCallback'}
        """ RegisterSnapInHelpTopicCallback(snapInInstance: SnapInBase, callback: SnapInHelpTopicCallback) """
        ...

    def SnapInHelpTopicCallback(self, *args): #cannot find CLR method
        """ SnapInHelpTopicCallback(object: object, method: IntPtr) """
        ...

    __all__: list = ...


class SnapInHelpTopicAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SnapInHelpTopicAttribute(topic: str) """
    @property
    def ApplicationBaseRelative(self) -> bool:
        """
        Get: ApplicationBaseRelative(self: SnapInHelpTopicAttribute) -> bool
        Set: ApplicationBaseRelative(self: SnapInHelpTopicAttribute) = value
        """
        ...

    @property
    def Topic(self) -> str:
        """ Get: Topic(self: SnapInHelpTopicAttribute) -> str """
        ...


    def __new__(cls, topic:str) -> Self:
        """ __new__(cls: type, topic: str) """
        ...


class SnapInImageList(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ SnapInImageList() """
    @property
    def Empty(self) -> bool:
        """ Get: Empty(self: SnapInImageList) -> bool """
        ...

    @property
    def TransparentColor(self) -> Color:
        """
        Get: TransparentColor(self: SnapInImageList) -> Color
        Set: TransparentColor(self: SnapInImageList) = value
        """
        ...


    def Add(self, value:Image, transparentColor:Color = ...) -> int:
        """ Add(self: SnapInImageList, value: Icon)Add(self: SnapInImageList, value: Image)Add(self: SnapInImageList, value: Image, transparentColor: Color) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: SnapInImageList, value: Array[Icon])AddRange(self: SnapInImageList, value: Array[Image]) """
        ...

    def AddStrip(self, value:Image) -> int:
        """ AddStrip(self: SnapInImageList, value: Image) -> int """
        ...

    def Clear(self): # -> 
        """ Clear(self: SnapInImageList) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SnapInImageList) -> IEnumerator """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SnapInImageList, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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


class SnapInInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ SnapInInstaller() """
    pass

class SnapInLinkedHelpTopicAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SnapInLinkedHelpTopicAttribute(topic: str) """
    @property
    def ApplicationBaseRelative(self) -> bool:
        """
        Get: ApplicationBaseRelative(self: SnapInLinkedHelpTopicAttribute) -> bool
        Set: ApplicationBaseRelative(self: SnapInLinkedHelpTopicAttribute) = value
        """
        ...

    @property
    def Topic(self) -> str:
        """ Get: Topic(self: SnapInLinkedHelpTopicAttribute) -> str """
        ...


    def __new__(cls, topic:str) -> Self:
        """ __new__(cls: type, topic: str) """
        ...


class SnapInSettingsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SnapInSettingsAttribute(guid: str) """
    @property
    def ConfigurationFile(self) -> str:
        """
        Get: ConfigurationFile(self: SnapInSettingsAttribute) -> str
        Set: ConfigurationFile(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: SnapInSettingsAttribute) -> str
        Set: Description(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: SnapInSettingsAttribute) -> str
        Set: DisplayName(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def DynamicBase(self) -> str:
        """
        Get: DynamicBase(self: SnapInSettingsAttribute) -> str
        Set: DynamicBase(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: SnapInSettingsAttribute) -> Guid """
        ...

    @property
    def LicenseFile(self) -> str:
        """
        Get: LicenseFile(self: SnapInSettingsAttribute) -> str
        Set: LicenseFile(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def PrivateBinPath(self) -> str:
        """
        Get: PrivateBinPath(self: SnapInSettingsAttribute) -> str
        Set: PrivateBinPath(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def PrivateBinPathProbe(self) -> str:
        """
        Get: PrivateBinPathProbe(self: SnapInSettingsAttribute) -> str
        Set: PrivateBinPathProbe(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def UseCustomHelp(self) -> bool:
        """
        Get: UseCustomHelp(self: SnapInSettingsAttribute) -> bool
        Set: UseCustomHelp(self: SnapInSettingsAttribute) = value
        """
        ...

    @property
    def Vendor(self) -> str:
        """
        Get: Vendor(self: SnapInSettingsAttribute) -> str
        Set: Vendor(self: SnapInSettingsAttribute) = value
        """
        ...


    def __new__(cls, guid:str) -> Self:
        """ __new__(cls: type, guid: str) """
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


class SyncAction(ActionBase): # skipped bases: <type 'object'>
    """
    SyncAction()
    SyncAction(displayName: str, description: str)
    SyncAction(displayName: str, description: str, imageIndex: int)
    SyncAction(displayName: str, description: str, imageIndex: int, tag: object)
    """
    def SyncActionEventHandler(self, *args): #cannot find CLR method
        """ SyncActionEventHandler(object: object, method: IntPtr) """
        ...

    def __new__(cls, displayName:str = ..., description:str = ..., imageIndex:int = ..., tag:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str, description: str)
        __new__(cls: type, displayName: str, description: str, imageIndex: int)
        __new__(cls: type, displayName: str, description: str, imageIndex: int, tag: object)
        """
        ...

    Triggered = ...


class SyncActionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SyncActionEventArgs(action: SyncAction, status: SyncStatus) """
    @property
    def Action(self) -> SyncAction:
        """ Get: Action(self: SyncActionEventArgs) -> SyncAction """
        ...

    @property
    def Status(self): # -> SyncStatus
        """ Get: Status(self: SyncActionEventArgs) -> SyncStatus """
        ...


    def __new__(cls, action:SyncAction, status) -> Self: # Not found arg types: {'status': 'SyncStatus'}
        """ __new__(cls: type, action: SyncAction, status: SyncStatus) """
        ...


class SyncStatus(Status): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanCancel(self) -> bool:
        """
        Get: CanCancel(self: SyncStatus) -> bool
        Set: CanCancel(self: SyncStatus) = value
        """
        ...

    @property
    def IsCancelSignaled(self) -> bool:
        """ Get: IsCancelSignaled(self: SyncStatus) -> bool """
        ...



class TraceSources: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExecutiveSource(self) -> TraceSource:
        """ Get: ExecutiveSource() -> TraceSource """
        ...




class ViewDescriptionCollection(BaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ViewDescriptionCollection() """
    @property
    def DefaultIndex(self) -> int:
        """
        Get: DefaultIndex(self: ViewDescriptionCollection) -> int
        Set: DefaultIndex(self: ViewDescriptionCollection) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: ViewDescriptionCollection) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ViewDescriptionCollection, array: Array[ViewDescription], index: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ViewDescriptionCollection) -> Array[ViewDescription] """
        ...


class WritableSharedData: # skipped bases: <type 'object'>, <type 'object'>
    """ WritableSharedData() """
    def Add(self, item): # ->  # Not found arg types: {'item': 'WritableSharedDataItem'}
        """ Add(self: WritableSharedData, item: WritableSharedDataItem) """
        ...

    def GetItem(self, clipboardFormatId:str): # -> WritableSharedDataItem
        """ GetItem(self: WritableSharedData, clipboardFormatId: str) -> WritableSharedDataItem """
        ...

    def Remove(self, clipboardFormatId:str): # -> 
        """ Remove(self: WritableSharedData, clipboardFormatId: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WritableSharedDataItem(SharedDataItemBase): # skipped bases: <type 'object'>
    """ WritableSharedDataItem(clipboardFormatId: str, requiresCallback: bool) """
    @property
    def RequiresCallback(self) -> bool:
        """ Get: RequiresCallback(self: WritableSharedDataItem) -> bool """
        ...


    def SetData(self, value:Array): # -> 
        """ SetData(self: WritableSharedDataItem, value: Array[Byte]) """
        ...

    def __new__(cls, clipboardFormatId:str, requiresCallback:bool) -> Self:
        """ __new__(cls: type, clipboardFormatId: str, requiresCallback: bool) """
        ...


# variables with complex values

