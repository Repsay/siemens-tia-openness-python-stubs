# encoding: utf-8
# module Microsoft.ManagementConsole.Advanced calls itself Advanced
# from MMCEx, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.ManagementConsole, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Guid, TimeSpan

from System.ComponentModel import Component

from System.Windows.Forms import (DialogResult, Form, HelpNavigator, 
    IWin32Window, MessageBoxButtons, MessageBoxDefaultButton, MessageBoxIcon, 
    MessageBoxOptions)

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    NamespaceSnapInBase, PrimaryScopeNode, PropertySheet, ScopeNodeCollection, 
    SharedData, SnapInBase)
"""

# no functions
# classes

class Console: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Show(self, form:Form): # -> 
        """ Show(self: Console, form: Form) """
        ...

    def ShowDialog(self, *__args:Form) -> DialogResult:
        """
        ShowDialog(self: Console, form: Form) -> DialogResult
        ShowDialog(self: Console, form: Form, waitCursor: WaitCursor) -> DialogResult
        ShowDialog(self: Console, commonDialog: CommonDialog) -> DialogResult
        ShowDialog(self: Console, parameters: MessageBoxParameters) -> DialogResult
        """
        ...


class ExtendsNodeTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExtendsNodeTypeAttribute(nodeType: str) """
    @property
    def NodeType(self) -> Guid:
        """ Get: NodeType(self: ExtendsNodeTypeAttribute) -> Guid """
        ...


    def __new__(cls, nodeType:str) -> Self:
        """ __new__(cls: type, nodeType: str) """
        ...


class ISnapInFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateSnapIn(self, bookkeepingId, snapInKey, snapIn) -> object:
        """ CreateSnapIn(self: ISnapInFactory, bookkeepingId: int, snapInKey: str) -> object """
        ...


class FrameworkSnapInFactory(ISnapInFactory): # skipped bases: <type 'object'>
    """ FrameworkSnapInFactory() """
    pass

class MessageBoxParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ MessageBoxParameters() """
    @property
    def Buttons(self) -> MessageBoxButtons:
        """
        Get: Buttons(self: MessageBoxParameters) -> MessageBoxButtons
        Set: Buttons(self: MessageBoxParameters) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: MessageBoxParameters) -> str
        Set: Caption(self: MessageBoxParameters) = value
        """
        ...

    @property
    def DefaultButton(self) -> MessageBoxDefaultButton:
        """
        Get: DefaultButton(self: MessageBoxParameters) -> MessageBoxDefaultButton
        Set: DefaultButton(self: MessageBoxParameters) = value
        """
        ...

    @property
    def HelpFilePath(self) -> str:
        """
        Get: HelpFilePath(self: MessageBoxParameters) -> str
        Set: HelpFilePath(self: MessageBoxParameters) = value
        """
        ...

    @property
    def HelpTopicId(self) -> object:
        """
        Get: HelpTopicId(self: MessageBoxParameters) -> object
        Set: HelpTopicId(self: MessageBoxParameters) = value
        """
        ...

    @property
    def Icon(self) -> MessageBoxIcon:
        """
        Get: Icon(self: MessageBoxParameters) -> MessageBoxIcon
        Set: Icon(self: MessageBoxParameters) = value
        """
        ...

    @property
    def Navigator(self) -> HelpNavigator:
        """
        Get: Navigator(self: MessageBoxParameters) -> HelpNavigator
        Set: Navigator(self: MessageBoxParameters) = value
        """
        ...

    @property
    def Options(self) -> MessageBoxOptions:
        """
        Get: Options(self: MessageBoxParameters) -> MessageBoxOptions
        Set: Options(self: MessageBoxParameters) = value
        """
        ...

    @property
    def ShowHelp(self) -> bool:
        """
        Get: ShowHelp(self: MessageBoxParameters) -> bool
        Set: ShowHelp(self: MessageBoxParameters) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: MessageBoxParameters) -> str
        Set: Text(self: MessageBoxParameters) = value
        """
        ...



class NamespaceExtension(NamespaceSnapInBase): # skipped bases: <type 'ISynchronizeInvoke'>, <type 'object'>
    """ no doc """
    @property
    def PrimaryNode(self): # -> PrimaryScopeNode
        """ Get: PrimaryNode(self: NamespaceExtension) -> PrimaryScopeNode """
        ...


    def OnRetrievePersistenceKey(self, *args): #cannot find CLR method
        """ OnRetrievePersistenceKey(self: NamespaceExtension) -> str """
        ...

    def OnSharedDataChanged(self, *args): #cannot find CLR method
        """ OnSharedDataChanged(self: NamespaceExtension, item: SharedDataItem) """
        ...


class PrimaryScopeNode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Children(self): # -> ScopeNodeCollection
        """ Get: Children(self: PrimaryScopeNode) -> ScopeNodeCollection """
        ...

    @property
    def NodeType(self) -> Guid:
        """ Get: NodeType(self: PrimaryScopeNode) -> Guid """
        ...

    @property
    def SharedData(self): # -> SharedData
        """ Get: SharedData(self: PrimaryScopeNode) -> SharedData """
        ...



class PrimarySnapInDataException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrimarySnapInDataException()
    PrimarySnapInDataException(message: str)
    PrimarySnapInDataException(message: str, innerException: Exception)
    PrimarySnapInDataException(information: SerializationInfo, context: StreamingContext)
    """
    SerializeObjectState = ...


class PropertySheetExtension(SnapInBase): # skipped bases: <type 'ISynchronizeInvoke'>, <type 'object'>
    """ no doc """
    @property
    def ExtensionPropertySheet(self): # -> PropertySheet
        """ Get: ExtensionPropertySheet(self: PropertySheetExtension) -> PropertySheet """
        ...

    @property
    def SharedData(self): # -> SharedData
        """ Get: SharedData(self: PropertySheetExtension) -> SharedData """
        ...


    def GetNodeTypes(self) -> Array:
        """ GetNodeTypes(self: PropertySheetExtension) -> Array[Guid] """
        ...

    def OnAddPropertyPages(self, *args): #cannot find CLR method
        """ OnAddPropertyPages(self: PropertySheetExtension, propertyPageCollection: PropertyPageCollection) """
        ...

    def OnSharedDataChanged(self, *args): #cannot find CLR method
        """ OnSharedDataChanged(self: PropertySheetExtension, item: SharedDataItem) """
        ...


class WaitCursor: # skipped bases: <type 'object'>, <type 'object'>
    """ WaitCursor() """
    @property
    def DialogResult(self) -> DialogResult:
        """
        Get: DialogResult(self: WaitCursor) -> DialogResult
        Set: DialogResult(self: WaitCursor) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: WaitCursor) -> TimeSpan
        Set: Timeout(self: WaitCursor) = value
        """
        ...


    def Exit(self): # -> 
        """ Exit(self: WaitCursor) """
        ...

    def OnStart(self, *args): #cannot find CLR method
        """ OnStart(self: WaitCursor) """
        ...

    Start = ...


class WaitDialog(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ WaitDialog() """
    @property
    def CanCancel(self) -> bool:
        """
        Get: CanCancel(self: WaitDialog) -> bool
        Set: CanCancel(self: WaitDialog) = value
        """
        ...

    @property
    def DisplayDelay(self) -> TimeSpan:
        """
        Get: DisplayDelay(self: WaitDialog) -> TimeSpan
        Set: DisplayDelay(self: WaitDialog) = value
        """
        ...

    @property
    def MinimumDisplayTime(self) -> TimeSpan:
        """
        Get: MinimumDisplayTime(self: WaitDialog) -> TimeSpan
        Set: MinimumDisplayTime(self: WaitDialog) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WaitDialog) -> str
        Set: Name(self: WaitDialog) = value
        """
        ...

    @property
    def StatusText(self) -> str:
        """
        Get: StatusText(self: WaitDialog) -> str
        Set: StatusText(self: WaitDialog) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: WaitDialog) -> str
        Set: Title(self: WaitDialog) = value
        """
        ...

    @property
    def TotalWork(self) -> int:
        """
        Get: TotalWork(self: WaitDialog) -> int
        Set: TotalWork(self: WaitDialog) = value
        """
        ...

    @property
    def WorkProcessed(self) -> int:
        """
        Get: WorkProcessed(self: WaitDialog) -> int
        Set: WorkProcessed(self: WaitDialog) = value
        """
        ...


    def CompleteDialog(self): # -> 
        """ CompleteDialog(self: WaitDialog) """
        ...

    def ShowDialog(self, owner:IWin32Window = ...): # -> 
        """ ShowDialog(self: WaitDialog)ShowDialog(self: WaitDialog, owner: IWin32Window) """
        ...

    def UpdateProgress(self, workProcessed:int, totalWork:int, statusText:str): # -> 
        """ UpdateProgress(self: WaitDialog, workProcessed: int, totalWork: int, statusText: str) """
        ...

    Cancel = ...


