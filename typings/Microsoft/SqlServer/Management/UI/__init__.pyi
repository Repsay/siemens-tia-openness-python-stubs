# encoding: utf-8
# module Microsoft.SqlServer.Management.UI calls itself UI
# from Microsoft.SqlServer.WizardFramework, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.WizardFrameworkLite, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.CustomControls, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.GridControl, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.NetEnterpriseServers import (ExceptionMessageBox, 
    ExceptionMessageBoxButtons, ExceptionMessageBoxSymbol)

from Microsoft.Office.Interop.Excel import Button, TextBox

from Microsoft.Office.Interop.Word import CheckBox

from Microsoft.Win32 import RegistryKey

from System import (AsyncCallback, Enum, EventArgs, IAsyncResult, Int64, 
    MulticastDelegate)

from System.Collections import ArrayList, IEnumerator

from System.ComponentModel import CancelEventArgs

from System.Drawing import Color, Font, Image

from System.Reflection.Emit import Label

from System.Threading import ThreadStart

from System.Web.UI import UserControl

from System.Web.UI.MobileControls import Form

from typing import Self

"""The following names are not found in the module: (BoundEvent, DialogResult, 
    IWin32Window, LinkLabel, MessageBoxIcon, RichTextBox, ScriptTextFormat, 
    field#)
"""

# no functions
# classes

class WizardPage(UserControl): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    WizardPage()
    WizardPage(wizard: WizardForm)
    WizardPage(wizard: WizardForm, nextPage: WizardPage)
    """
    @property
    def Back(self) -> WizardPage:
        """
        Get: Back(self: WizardPage) -> WizardPage
        Set: Back(self: WizardPage) = value
        """
        ...

    @property
    def BackEnabled(self) -> bool:
        """
        Get: BackEnabled(self: WizardPage) -> bool
        Set: BackEnabled(self: WizardPage) = value
        """
        ...

    @property
    def BoldFont(self) -> Font:
        """ Get: BoldFont(self: WizardPage) -> Font """
        ...

    @property
    def FinishEnabled(self) -> bool:
        """
        Get: FinishEnabled(self: WizardPage) -> bool
        Set: FinishEnabled(self: WizardPage) = value
        """
        ...

    @property
    def Glyph(self) -> Image:
        """
        Get: Glyph(self: WizardPage) -> Image
        Set: Glyph(self: WizardPage) = value
        """
        ...

    @property
    def HelpTopicID(self) -> Int64:
        """
        Get: HelpTopicID(self: WizardPage) -> Int64
        Set: HelpTopicID(self: WizardPage) = value
        """
        ...

    @property
    def HelpTopicKeyword(self) -> str:
        """
        Get: HelpTopicKeyword(self: WizardPage) -> str
        Set: HelpTopicKeyword(self: WizardPage) = value
        """
        ...

    @property
    def HideShowTipsForThisPage(self) -> bool:
        """
        Get: HideShowTipsForThisPage(self: WizardPage) -> bool
        Set: HideShowTipsForThisPage(self: WizardPage) = value
        """
        ...

    @property
    def IsScaled(self) -> bool:
        """
        Get: IsScaled(self: WizardPage) -> bool
        Set: IsScaled(self: WizardPage) = value
        """
        ...

    @property
    def LeftAlignedGlyph(self) -> bool:
        """
        Get: LeftAlignedGlyph(self: WizardPage) -> bool
        Set: LeftAlignedGlyph(self: WizardPage) = value
        """
        ...

    @property
    def Next(self) -> WizardPage:
        """
        Get: Next(self: WizardPage) -> WizardPage
        Set: Next(self: WizardPage) = value
        """
        ...

    @property
    def NextEnabled(self) -> bool:
        """
        Get: NextEnabled(self: WizardPage) -> bool
        Set: NextEnabled(self: WizardPage) = value
        """
        ...

    @property
    def NormalFont(self) -> Font:
        """ Get: NormalFont(self: WizardPage) -> Font """
        ...

    @property
    def PageID(self) -> int:
        """
        Get: PageID(self: WizardPage) -> int
        Set: PageID(self: WizardPage) = value
        """
        ...

    @property
    def PageInitialized(self) -> bool:
        """
        Get: PageInitialized(self: WizardPage) -> bool
        Set: PageInitialized(self: WizardPage) = value
        """
        ...

    @property
    def PageTitleFont(self) -> Font:
        """ Get: PageTitleFont(self: WizardPage) -> Font """
        ...

    @property
    def SubTitle(self) -> str:
        """
        Get: SubTitle(self: WizardPage) -> str
        Set: SubTitle(self: WizardPage) = value
        """
        ...

    @property
    def TipText(self) -> str:
        """
        Get: TipText(self: WizardPage) -> str
        Set: TipText(self: WizardPage) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: WizardPage) -> str
        Set: Title(self: WizardPage) = value
        """
        ...

    @property
    def TitleFont(self) -> Font:
        """ Get: TitleFont(self: WizardPage) -> Font """
        ...

    @property
    def Wizard(self) -> WizardForm:
        """
        Get: Wizard(self: WizardPage) -> WizardForm
        Set: Wizard(self: WizardPage) = value
        """
        ...

    @property
    def WizardInputs(self) -> WizardInputs:
        """ Get: WizardInputs(self: WizardPage) -> WizardInputs """
        ...


    def OnEnteredPage(self, *args): #cannot find CLR method
        """ OnEnteredPage(self: WizardPage, e: EventArgs) """
        ...

    def OnEnterPage(self, *args): #cannot find CLR method
        """ OnEnterPage(self: WizardPage, e: EventArgs) """
        ...

    def OnInitializePage(self, *args): #cannot find CLR method
        """ OnInitializePage(self: WizardPage, e: EventArgs) """
        ...

    def OnLeavePage(self, *args): #cannot find CLR method
        """ OnLeavePage(self: WizardPage, e: LeavePageEventArgs) """
        ...

    def SetFontStyles(self, *args): #cannot find CLR method
        """ SetFontStyles(self: WizardPage)SetFontStyles(topControl: Control, parent: Control, referenceFont: Font) """
        ...

    def ShowMessage(self, owner, *__args:Exception): # -> DialogResult # Not found arg types: {'owner': 'IWin32Window'}
        """
        ShowMessage(self: WizardPage, owner: IWin32Window, str: str, ex: Exception) -> DialogResult
        ShowMessage(self: WizardPage, owner: IWin32Window, ex: Exception) -> DialogResult
        """
        ...

    def __new__(cls, wizard:WizardForm = ..., nextPage:WizardPage = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, wizard: WizardForm)
        __new__(cls: type, wizard: WizardForm, nextPage: WizardPage)
        """
        ...


class ActionsWizardPage(WizardPage): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'object'>
    """ ActionsWizardPage(wiz: WizardForm) """
    @property
    def Actions(self) -> WizardActions:
        """ Get: Actions(self: ActionsWizardPage) -> WizardActions """
        ...

    @property
    def AllowOpenScriptWindow(self) -> bool:
        """
        Get: AllowOpenScriptWindow(self: ActionsWizardPage) -> bool
        Set: AllowOpenScriptWindow(self: ActionsWizardPage) = value
        """
        ...

    @property
    def ExecuteNowText(self) -> str:
        """
        Get: ExecuteNowText(self: ActionsWizardPage) -> str
        Set: ExecuteNowText(self: ActionsWizardPage) = value
        """
        ...

    @property
    def GenerateScriptFileText(self) -> str:
        """
        Get: GenerateScriptFileText(self: ActionsWizardPage) -> str
        Set: GenerateScriptFileText(self: ActionsWizardPage) = value
        """
        ...

    @property
    def IsExecuteNow(self) -> bool:
        """
        Get: IsExecuteNow(self: ActionsWizardPage) -> bool
        Set: IsExecuteNow(self: ActionsWizardPage) = value
        """
        ...

    @property
    def IsGenerateScriptFile(self) -> bool:
        """
        Get: IsGenerateScriptFile(self: ActionsWizardPage) -> bool
        Set: IsGenerateScriptFile(self: ActionsWizardPage) = value
        """
        ...

    @property
    def IsOpenScriptWindow(self) -> bool:
        """
        Get: IsOpenScriptWindow(self: ActionsWizardPage) -> bool
        Set: IsOpenScriptWindow(self: ActionsWizardPage) = value
        """
        ...

    @property
    def OpenScriptWindowText(self) -> str:
        """
        Get: OpenScriptWindowText(self: ActionsWizardPage) -> str
        Set: OpenScriptWindowText(self: ActionsWizardPage) = value
        """
        ...


    def InitializePage(self, *args): #cannot find CLR method
        """ InitializePage(self: ActionsWizardPage) """
        ...

    WizardActionsInputName: str = ...


class DFW: # skipped bases: <type 'object'>, <type 'object'>
    """ DFW() """
    wiAddControl: str = ...
    wiCancelAllControl: str = ...
    wiCancelControl: str = ...
    wiConnection: str = ...
    wiConnectionName: str = ...
    wiConnectionPage: str = ...
    wiConnectionString: str = ...
    wiCRelationList: str = ...
    wiDataAdapters: str = ...
    wiDataSet: str = ...
    wiDataSetName: str = ...
    wiDataSetProjectItem: str = ...
    wiDataSetType: str = ...
    wiDeleteControl: str = ...
    wiDetailTable: str = ...
    wiEmbeddedGrid: str = ...
    wiFieldsPage: str = ...
    wiFormProjectItem: str = ...
    wiGrid: str = ...
    wiIncludeLoadButton: str = ...
    wiIncludeUpdateButton: str = ...
    wiLoadMethod: str = ...
    wiMasterTable: str = ...
    wiMethodsPage: str = ...
    wiNameSpaceName: str = ...
    wiNavigationControl: str = ...
    wiOneForm: str = ...
    wiRelationsPage: str = ...
    wiSelectedDetailColumns: str = ...
    wiSelectedMasterColumns: str = ...
    wiSelectedSProcs: str = ...
    wiSelectedTables: str = ...
    wiSelectedViews: str = ...
    wiStronglyTypedName: str = ...
    wiTablesPage: str = ...
    wiTaskName: str = ...
    wiUpdateMethod: str = ...
    wiVBProject: str = ...


class FinishWizardPage(WizardPage): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'object'>
    """ FinishWizardPage(wiz: WizardForm) """
    @property
    def AutoFormat(self) -> bool:
        """
        Get: AutoFormat(self: FinishWizardPage) -> bool
        Set: AutoFormat(self: FinishWizardPage) = value
        """
        ...

    @property
    def ClickFinishText(self) -> str:
        """
        Get: ClickFinishText(self: FinishWizardPage) -> str
        Set: ClickFinishText(self: FinishWizardPage) = value
        """
        ...


    @staticmethod
    def PrepareForRtf(s:str) -> str:
        """ PrepareForRtf(s: str) -> str """
        ...

    RtfBeginIndentedList: str = ...
    RtfBeginList: str = ...
    RtfBoldOff: str = ...
    RtfBoldOn: str = ...
    RtfEndList: str = ...
    RtfNewParagraph: str = ...


class Generic: # skipped bases: <type 'object'>, <type 'object'>
    """ Generic() """
    wiApplication: str = ...
    wiContextParams: str = ...
    wiCustomParams: str = ...
    wiDesignerType: str = ...
    wiHost: str = ...
    wiHTMLWindow: str = ...
    wiResult: str = ...
    wiServiceProvider: str = ...
    wiTaskName: str = ...
    wiWebForm: str = ...
    wiWinForm: str = ...
    wiWizardCallback: str = ...
    wiWizardInitialized: str = ...


class IProgress: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AbortPrompt(self) -> str:
        """
        Get: AbortPrompt(self: IProgress) -> str
        Set: AbortPrompt(self: IProgress) = value
        """
        ...

    @property
    def ActionUpdateEnabled(self) -> bool:
        """
        Get: ActionUpdateEnabled(self: IProgress) -> bool
        Set: ActionUpdateEnabled(self: IProgress) = value
        """
        ...

    @property
    def AllowAbort(self) -> bool:
        """
        Get: AllowAbort(self: IProgress) -> bool
        Set: AllowAbort(self: IProgress) = value
        """
        ...

    @property
    def IsAborted(self) -> bool:
        """ Get: IsAborted(self: IProgress) -> bool """
        ...

    @property
    def WorkerThreadStart(self) -> ThreadStart:
        """
        Get: WorkerThreadStart(self: IProgress) -> ThreadStart
        Set: WorkerThreadStart(self: IProgress) = value
        """
        ...


    def AddAction(self, description:str) -> int:
        """ AddAction(self: IProgress, description: str) -> int """
        ...

    def AddActionDynamic(self, description:str): # -> 
        """ AddActionDynamic(self: IProgress, description: str) """
        ...

    def AddActionException(self, actionIndex:int, e:Exception): # -> 
        """ AddActionException(self: IProgress, actionIndex: int, e: Exception) """
        ...

    def AddActionInfoString(self, actionIndex:int, infoString:str): # -> 
        """ AddActionInfoString(self: IProgress, actionIndex: int, infoString: str) """
        ...

    def ShowMessageBox(self, ex:Exception, buttons:ExceptionMessageBoxButtons, symbol:ExceptionMessageBoxSymbol): # -> DialogResult
        """ ShowMessageBox(self: IProgress, ex: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol) -> DialogResult """
        ...

    def UpdateActionDescription(self, actionIndex:int, description:str): # -> 
        """ UpdateActionDescription(self: IProgress, actionIndex: int, description: str) """
        ...

    def UpdateActionProgress(self, actionIndex:int, *__args:int): # -> 
        """ UpdateActionProgress(self: IProgress, actionIndex: int, percentComplete: int)UpdateActionProgress(self: IProgress, actionIndex: int, description: str) """
        ...

    def UpdateActionStatus(self, actionIndex:int, status:ProgressStatus): # -> 
        """ UpdateActionStatus(self: IProgress, actionIndex: int, status: ProgressStatus) """
        ...

    def WorkerThreadExiting(self, result:OperationStatus): # -> 
        """ WorkerThreadExiting(self: IProgress, result: OperationStatus) """
        ...


class IsInvalidCharacterEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ IsInvalidCharacterEventArgs(hasInValidCharacter: bool) """
    @property
    def HasInValidCharacter(self) -> bool:
        """ Get: HasInValidCharacter(self: IsInvalidCharacterEventArgs) -> bool """
        ...


    def __new__(cls, hasInValidCharacter:bool) -> Self:
        """ __new__(cls: type, hasInValidCharacter: bool) """
        ...


class LeavePageEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """
    LeavePageEventArgs(forward: bool, cancel: bool)
    LeavePageEventArgs(button: WizardButton, cancel: bool)
    """
    @property
    def Button(self) -> WizardButton:
        """ Get: Button(self: LeavePageEventArgs) -> WizardButton """
        ...

    @property
    def Forward(self) -> bool:
        """ Get: Forward(self: LeavePageEventArgs) -> bool """
        ...



class LocalizableLinkLabel(LinkLabel): # skipped bases: <type 'IPersistStreamInit'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IAutomationLiveRegion'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IWin32Window'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IButtonControl'>, <type 'object'>
    """ LocalizableLinkLabel() """
    @property
    def LinkDelimiter(self) -> str:
        """
        Get: LinkDelimiter(self: LocalizableLinkLabel) -> str
        Set: LinkDelimiter(self: LocalizableLinkLabel) = value
        """
        ...



class MultiExceptionMessageBox(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    MultiExceptionMessageBox(caption: str, subTitle: str, exceptionsCollection: ArrayList)
    MultiExceptionMessageBox()
    """
    def __new__(cls, caption:str = ..., subTitle:str = ..., exceptionsCollection:ArrayList = ...) -> Self:
        """
        __new__(cls: type, caption: str, subTitle: str, exceptionsCollection: ArrayList)
        __new__(cls: type)
        """
        ...


class OperationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationStatus, values: Aborted (4), CompletedWithErrors (2), Error (3), InProgress (0), Invalid (-1), StatusCount (5), Success (1) """
    Aborted: OperationStatus = ...
    CompletedWithErrors: OperationStatus = ...
    Error: OperationStatus = ...
    InProgress: OperationStatus = ...
    Invalid: OperationStatus = ...
    StatusCount: OperationStatus = ...
    Success: OperationStatus = ...
    value__ = ...


class ProgressControlBase(UserControl): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ no doc """
    @property
    def CtrlStatus(self):
        ...

    @property
    def IsAborted(self) -> bool:
        """ Get: IsAborted(self: ProgressControlBase) -> bool """
        ...

    @property
    def MessageOwner(self):
        ...

    @property
    def WorkerThreadStart(self) -> ThreadStart:
        """
        Get: WorkerThreadStart(self: ProgressControlBase) -> ThreadStart
        Set: WorkerThreadStart(self: ProgressControlBase) = value
        """
        ...


    def Abort(self, *args): #cannot find CLR method
        """ Abort(self: ProgressControlBase, promptText: str, sourceText: str) """
        ...

    def Close(self, *args): #cannot find CLR method
        """ Close(self: ProgressControlBase) """
        ...

    def CtrlStatusChanged(self, *args): #cannot find CLR method
        """ CtrlStatusChanged(self: ProgressControlBase) """
        ...

    def Reset(self): # -> 
        """ Reset(self: ProgressControlBase) """
        ...

    def Start(self): # -> 
        """ Start(self: ProgressControlBase) """
        ...

    def WorkerThreadExiting(self, result:OperationStatus): # -> 
        """ WorkerThreadExiting(self: ProgressControlBase, result: OperationStatus) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, messageOwner: IWin32Window) """
        ...

    ProgressCtrlStatusChanged = ...


class ProgressCtrlStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProgressCtrlStatus, values: Aborted (5), Aborting (4), Closed (6), CompletedWithErrors (2), Error (3), InProgress (0), Invalid (-1), StatusCount (7), Success (1) """
    Aborted: ProgressCtrlStatus = ...
    Aborting: ProgressCtrlStatus = ...
    Closed: ProgressCtrlStatus = ...
    CompletedWithErrors: ProgressCtrlStatus = ...
    Error: ProgressCtrlStatus = ...
    InProgress: ProgressCtrlStatus = ...
    Invalid: ProgressCtrlStatus = ...
    StatusCount: ProgressCtrlStatus = ...
    Success: ProgressCtrlStatus = ...
    value__ = ...


class ProgressCtrlStatusChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ProgressCtrlStatusChangedEventArgs() """
    @property
    def Status(self) -> ProgressCtrlStatus:
        """
        Get: Status(self: ProgressCtrlStatusChangedEventArgs) -> ProgressCtrlStatus
        Set: Status(self: ProgressCtrlStatusChangedEventArgs) = value
        """
        ...



class ProgressCtrlStatusChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProgressCtrlStatusChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:ProgressCtrlStatusChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProgressCtrlStatusChangedEventHandler, source: object, e: ProgressCtrlStatusChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProgressCtrlStatusChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:ProgressCtrlStatusChangedEventArgs): # -> 
        """ Invoke(self: ProgressCtrlStatusChangedEventHandler, source: object, e: ProgressCtrlStatusChangedEventArgs) """
        ...


class ProgressDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ProgressDialog() """
    @property
    def AbortPrompt(self) -> str:
        """
        Get: AbortPrompt(self: ProgressDialog) -> str
        Set: AbortPrompt(self: ProgressDialog) = value
        """
        ...

    @property
    def AllowAbort(self) -> bool:
        """
        Get: AllowAbort(self: ProgressDialog) -> bool
        Set: AllowAbort(self: ProgressDialog) = value
        """
        ...

    @property
    def FormID(self) -> int:
        """
        Get: FormID(self: ProgressDialog) -> int
        Set: FormID(self: ProgressDialog) = value
        """
        ...

    @property
    def IsAborted(self) -> bool:
        """ Get: IsAborted(self: ProgressDialog) -> bool """
        ...

    @property
    def WorkerThreadStart(self) -> ThreadStart:
        """
        Get: WorkerThreadStart(self: ProgressDialog) -> ThreadStart
        Set: WorkerThreadStart(self: ProgressDialog) = value
        """
        ...


    def ShowMessageBox(self, ex:Exception, buttons:ExceptionMessageBoxButtons, symbol:ExceptionMessageBoxSymbol): # -> DialogResult
        """ ShowMessageBox(self: ProgressDialog, ex: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol) -> DialogResult """
        ...

    def UpdateProgress(self, description:str): # -> 
        """ UpdateProgress(self: ProgressDialog, description: str) """
        ...

    def WorkerThreadExiting(self, result:OperationStatus): # -> 
        """ WorkerThreadExiting(self: ProgressDialog, result: OperationStatus) """
        ...


class ProgressReportControl(ProgressControlBase): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'object'>
    """ ProgressReportControl(messageOwner: IWin32Window) """
    @property
    def AbortButton(self) -> Button:
        """ Get: AbortButton(self: ProgressReportControl) -> Button """
        ...

    @property
    def AbortPrompt(self) -> str:
        """
        Get: AbortPrompt(self: ProgressReportControl) -> str
        Set: AbortPrompt(self: ProgressReportControl) = value
        """
        ...

    @property
    def ActionUpdateEnabled(self) -> bool:
        """
        Get: ActionUpdateEnabled(self: ProgressReportControl) -> bool
        Set: ActionUpdateEnabled(self: ProgressReportControl) = value
        """
        ...

    @property
    def AllowAbort(self) -> bool:
        """
        Get: AllowAbort(self: ProgressReportControl) -> bool
        Set: AllowAbort(self: ProgressReportControl) = value
        """
        ...

    @property
    def MessageTitle(self) -> str:
        """
        Get: MessageTitle(self: ProgressReportControl) -> str
        Set: MessageTitle(self: ProgressReportControl) = value
        """
        ...

    @property
    def ShowButtons(self) -> bool:
        """
        Get: ShowButtons(self: ProgressReportControl) -> bool
        Set: ShowButtons(self: ProgressReportControl) = value
        """
        ...

    @property
    def ShowCloseButton(self) -> bool:
        """
        Get: ShowCloseButton(self: ProgressReportControl) -> bool
        Set: ShowCloseButton(self: ProgressReportControl) = value
        """
        ...


    def AddAction(self, description:str) -> int:
        """ AddAction(self: ProgressReportControl, description: str) -> int """
        ...

    def AddActionDynamic(self, description:str): # -> 
        """ AddActionDynamic(self: ProgressReportControl, description: str) """
        ...

    def AddActionException(self, actionIndex:int, e:Exception): # -> 
        """ AddActionException(self: ProgressReportControl, actionIndex: int, e: Exception) """
        ...

    def AddActionInfoString(self, actionIndex:int, infoString:str): # -> 
        """ AddActionInfoString(self: ProgressReportControl, actionIndex: int, infoString: str) """
        ...

    def ShowMessageBox(self, ex:Exception, buttons:ExceptionMessageBoxButtons, symbol:ExceptionMessageBoxSymbol): # -> DialogResult
        """ ShowMessageBox(self: ProgressReportControl, ex: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol) -> DialogResult """
        ...

    def UpdateActionDescription(self, actionIndex:int, description:str): # -> 
        """ UpdateActionDescription(self: ProgressReportControl, actionIndex: int, description: str) """
        ...

    def UpdateActionProgress(self, actionIndex:int, *__args:int): # -> 
        """ UpdateActionProgress(self: ProgressReportControl, actionIndex: int, percentComplete: int)UpdateActionProgress(self: ProgressReportControl, actionIndex: int, progressDescription: str) """
        ...

    def UpdateActionStatus(self, actionIndex:int, status:ProgressStatus): # -> 
        """ UpdateActionStatus(self: ProgressReportControl, actionIndex: int, status: ProgressStatus) """
        ...


class ProgressReportDialog(Form, IProgress): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ProgressReportDialog() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ProgressReportDialog) -> str
        Set: Description(self: ProgressReportDialog) = value
        """
        ...

    @property
    def FormID(self) -> int:
        """
        Get: FormID(self: ProgressReportDialog) -> int
        Set: FormID(self: ProgressReportDialog) = value
        """
        ...



class ProgressReportWizardPage(WizardPage, IProgress): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'object'>
    """ ProgressReportWizardPage(wiz: WizardForm) """
    @property
    def ShowBackOnIncompleteOperation(self) -> bool:
        """
        Get: ShowBackOnIncompleteOperation(self: ProgressReportWizardPage) -> bool
        Set: ShowBackOnIncompleteOperation(self: ProgressReportWizardPage) = value
        """
        ...



class ProgressStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProgressStatus, values: Aborted (6), Error (5), InProgress (1), Invalid (-1), NotStarted (0), RolledBack (7), StatusCount (8), Success (2), SuccessWithInfo (3), Warning (4) """
    Aborted: ProgressStatus = ...
    Error: ProgressStatus = ...
    InProgress: ProgressStatus = ...
    Invalid: ProgressStatus = ...
    NotStarted: ProgressStatus = ...
    RolledBack: ProgressStatus = ...
    StatusCount: ProgressStatus = ...
    Success: ProgressStatus = ...
    SuccessWithInfo: ProgressStatus = ...
    value__ = ...
    Warning: ProgressStatus = ...


class ProjectItemContextParams(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProjectItemContextParams, values: InstallationDirectory (6), ItemName (4), LocalDirectory (3), ProjectItems (2), ProjectName (1), SolutionDirectory (5), WizardType (0) """
    InstallationDirectory: ProjectItemContextParams = ...
    ItemName: ProjectItemContextParams = ...
    LocalDirectory: ProjectItemContextParams = ...
    ProjectItems: ProjectItemContextParams = ...
    ProjectName: ProjectItemContextParams = ...
    SolutionDirectory: ProjectItemContextParams = ...
    value__ = ...
    WizardType: ProjectItemContextParams = ...


class ScriptFilePropertiesWizardPage(WizardPage): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'object'>
    """ ScriptFilePropertiesWizardPage(wiz: WizardForm) """
    @property
    def AppendToExistingFile(self) -> bool:
        """
        Get: AppendToExistingFile(self: ScriptFilePropertiesWizardPage) -> bool
        Set: AppendToExistingFile(self: ScriptFilePropertiesWizardPage) = value
        """
        ...

    @property
    def DefaultScriptPath(self) -> str:
        """
        Get: DefaultScriptPath(self: ScriptFilePropertiesWizardPage) -> str
        Set: DefaultScriptPath(self: ScriptFilePropertiesWizardPage) = value
        """
        ...

    @property
    def OverwriteExistingFile(self) -> bool:
        """
        Get: OverwriteExistingFile(self: ScriptFilePropertiesWizardPage) -> bool
        Set: OverwriteExistingFile(self: ScriptFilePropertiesWizardPage) = value
        """
        ...

    @property
    def ScriptPath(self) -> str:
        """ Get: ScriptPath(self: ScriptFilePropertiesWizardPage) -> str """
        ...

    @property
    def TextFormat(self): # -> ScriptTextFormat
        """
        Get: TextFormat(self: ScriptFilePropertiesWizardPage) -> ScriptTextFormat
        Set: TextFormat(self: ScriptFilePropertiesWizardPage) = value
        """
        ...

    @property
    def UseUnicodeFormat(self) -> bool:
        """
        Get: UseUnicodeFormat(self: ScriptFilePropertiesWizardPage) -> bool
        Set: UseUnicodeFormat(self: ScriptFilePropertiesWizardPage) = value
        """
        ...

    @property
    def UseWindowsFormat(self) -> bool:
        """
        Get: UseWindowsFormat(self: ScriptFilePropertiesWizardPage) -> bool
        Set: UseWindowsFormat(self: ScriptFilePropertiesWizardPage) = value
        """
        ...


    def CreateScriptFile(self, scriptText:str): # -> 
        """ CreateScriptFile(self: ScriptFilePropertiesWizardPage, scriptText: str) """
        ...

    def ScriptTextFormat(self, *args): #cannot find CLR method
        """ enum ScriptTextFormat, values: ANSI (0), Unicode (1), Windows (0) """
        ...

    OverwriteExistingFileInputName: str = ...
    ScriptPathInputName: str = ...
    UseUnicodeFormatInputName: str = ...


class Separator(Label): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IViewObject2'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IAutomationLiveRegion'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'object'>
    """ Separator() """
    pass

class SqlExceptionMessageBox(ExceptionMessageBox): # skipped bases: <type 'object'>
    """
    SqlExceptionMessageBox()
    SqlExceptionMessageBox(exception: Exception)
    SqlExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons)
    SqlExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol)
    SqlExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defbtn: ExceptionMessageBoxDefaultButton)
    SqlExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defbtn: ExceptionMessageBoxDefaultButton, options: ExceptionMessageBoxOptions)
    """
    @staticmethod
    def SetHelpContext(*__args): # -> 
        """ SetHelpContext(ex: Exception, productName: str, productVersion: str, messageSource: str, messageID: str)SetHelpContext(ex: Exception, messageSource: str, messageID: str)SetHelpContext(self: SqlExceptionMessageBox, messageSource: str, messageID: str) """
        ...

    BaseHelpUrl: str = ...
    BaseHelpUrlParam: str = ...
    FwlinkID: str = ...
    FwlinkValue: str = ...
    MessageID: str = ...
    MessageIDParam: str = ...
    MessageSource: str = ...
    MessageSourceParam: str = ...
    ProductName: str = ...
    ProductNameParam: str = ...
    ProductVersion: str = ...
    ProductVersionParam: str = ...


class SqlTextBox(TextBox): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'object'>
    """ SqlTextBox() """
    @property
    def ExcludedCharacters(self) -> str:
        """
        Get: ExcludedCharacters(self: SqlTextBox) -> str
        Set: ExcludedCharacters(self: SqlTextBox) = value
        """
        ...

    @property
    def IncludedCharacters(self) -> str:
        """
        Get: IncludedCharacters(self: SqlTextBox) -> str
        Set: IncludedCharacters(self: SqlTextBox) = value
        """
        ...


    def InvalidCharacterEnteredHandler(self, *args): #cannot find CLR method
        """ InvalidCharacterEnteredHandler(object: object, method: IntPtr) """
        ...

    def OnInvalidCharacterEntered(self, *args): #cannot find CLR method
        """ OnInvalidCharacterEntered(self: SqlTextBox, e: IsInvalidCharacterEventArgs) """
        ...

    InvalidCharacterEntered = ...


class WizardActions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WizardActions, values: ExecuteNow (1), GenerateScriptFile (2), NeedScript (6), OpenScriptWindow (4) """
    ExecuteNow: WizardActions = ...
    GenerateScriptFile: WizardActions = ...
    NeedScript: WizardActions = ...
    OpenScriptWindow: WizardActions = ...
    value__ = ...


class WizardButton(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WizardButton, values: Back (1), Cancel (0), Finish (3), Next (2) """
    Back: WizardButton = ...
    Cancel: WizardButton = ...
    Finish: WizardButton = ...
    Next: WizardButton = ...
    value__ = ...


class WizardCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WizardCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, wizardInputs:WizardInputs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WizardCallback, wizardInputs: WizardInputs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WizardCallback, result: IAsyncResult) """
        ...

    def Invoke(self, wizardInputs:WizardInputs): # -> 
        """ Invoke(self: WizardCallback, wizardInputs: WizardInputs) """
        ...


class WizardEngine: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TasksRegistered(self) -> bool:
        """ Get: TasksRegistered(self: WizardEngine) -> bool """
        ...


    def AddOnListChanged(self, wt:WizardTask): # -> 
        """ AddOnListChanged(self: WizardEngine, wt: WizardTask) """
        ...

    def AddTask(self, wt:WizardTask): # -> 
        """ AddTask(self: WizardEngine, wt: WizardTask) """
        ...

    def Execute(self, wi:WizardInputs): # -> 
        """ Execute(self: WizardEngine, wi: WizardInputs) """
        ...

    def OnListChanged(self, wi:WizardInputs): # -> 
        """ OnListChanged(self: WizardEngine, wi: WizardInputs) """
        ...

    def RemoveOnListChanged(self, wizardTask:WizardTask): # -> 
        """ RemoveOnListChanged(self: WizardEngine, wizardTask: WizardTask) """
        ...

    engineTasks = ...
    registeredTasks = ...


class WizardForm(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ no doc """
    @property
    def ActivePage(self) -> WizardPage:
        """ Get: ActivePage(self: WizardForm) -> WizardPage """
        ...

    @property
    def ApplicationName(self) -> str:
        """ Get: ApplicationName(self: WizardForm) -> str """
        ...

    @property
    def BackButton(self) -> Button:
        """ Get: BackButton(self: WizardForm) -> Button """
        ...

    @property
    def BackEnabled(self) -> bool:
        """
        Get: BackEnabled(self: WizardForm) -> bool
        Set: BackEnabled(self: WizardForm) = value
        """
        ...

    @property
    def BoldFont(self) -> Font:
        """ Get: BoldFont(self: WizardForm) -> Font """
        ...

    @property
    def CancelEnabled(self) -> bool:
        """
        Get: CancelEnabled(self: WizardForm) -> bool
        Set: CancelEnabled(self: WizardForm) = value
        """
        ...

    @property
    def CustomFinishButtonInternalToolTipText(self) -> str:
        """
        Get: CustomFinishButtonInternalToolTipText(self: WizardForm) -> str
        Set: CustomFinishButtonInternalToolTipText(self: WizardForm) = value
        """
        ...

    @property
    def CustomFinishButtonText(self) -> str:
        """
        Get: CustomFinishButtonText(self: WizardForm) -> str
        Set: CustomFinishButtonText(self: WizardForm) = value
        """
        ...

    @property
    def CustomFinishButtonToolTipText(self) -> str:
        """
        Get: CustomFinishButtonToolTipText(self: WizardForm) -> str
        Set: CustomFinishButtonToolTipText(self: WizardForm) = value
        """
        ...

    @property
    def EnableFinishAutomatically(self) -> bool:
        """
        Get: EnableFinishAutomatically(self: WizardForm) -> bool
        Set: EnableFinishAutomatically(self: WizardForm) = value
        """
        ...

    @property
    def EnableInfoPanel(self) -> bool:
        """
        Get: EnableInfoPanel(self: WizardForm) -> bool
        Set: EnableInfoPanel(self: WizardForm) = value
        """
        ...

    @property
    def FinishButton(self) -> Button:
        """ Get: FinishButton(self: WizardForm) -> Button """
        ...

    @property
    def FinishButtonText(self) -> str:
        """
        Get: FinishButtonText(self: WizardForm) -> str
        Set: FinishButtonText(self: WizardForm) = value
        """
        ...

    @property
    def FinishEnabled(self) -> bool:
        """
        Get: FinishEnabled(self: WizardForm) -> bool
        Set: FinishEnabled(self: WizardForm) = value
        """
        ...

    @property
    def FirstPage(self) -> WizardPage:
        """
        Get: FirstPage(self: WizardForm) -> WizardPage
        Set: FirstPage(self: WizardForm) = value
        """
        ...

    @property
    def GetCancelButton(self) -> Button:
        """ Get: GetCancelButton(self: WizardForm) -> Button """
        ...

    @property
    def GetHelpButton(self) -> Button:
        """ Get: GetHelpButton(self: WizardForm) -> Button """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: WizardForm) -> str
        Set: HelpFile(self: WizardForm) = value
        """
        ...

    @property
    def InfoIcon(self): # -> MessageBoxIcon
        """
        Get: InfoIcon(self: WizardForm) -> MessageBoxIcon
        Set: InfoIcon(self: WizardForm) = value
        """
        ...

    @property
    def InfoText(self) -> str:
        """
        Get: InfoText(self: WizardForm) -> str
        Set: InfoText(self: WizardForm) = value
        """
        ...

    @property
    def LastPage(self) -> WizardPage:
        """
        Get: LastPage(self: WizardForm) -> WizardPage
        Set: LastPage(self: WizardForm) = value
        """
        ...

    @property
    def NextButton(self) -> Button:
        """ Get: NextButton(self: WizardForm) -> Button """
        ...

    @property
    def NextEnabled(self) -> bool:
        """
        Get: NextEnabled(self: WizardForm) -> bool
        Set: NextEnabled(self: WizardForm) = value
        """
        ...

    @property
    def NormalFont(self) -> Font:
        """ Get: NormalFont(self: WizardForm) -> Font """
        ...

    @property
    def PageTitleFont(self) -> Font:
        """ Get: PageTitleFont(self: WizardForm) -> Font """
        ...

    @property
    def ProgressPage(self) -> WizardPage:
        """
        Get: ProgressPage(self: WizardForm) -> WizardPage
        Set: ProgressPage(self: WizardForm) = value
        """
        ...

    @property
    def ShowHelp(self) -> bool:
        """
        Get: ShowHelp(self: WizardForm) -> bool
        Set: ShowHelp(self: WizardForm) = value
        """
        ...

    @property
    def ShowInfoPanel(self) -> bool:
        """
        Get: ShowInfoPanel(self: WizardForm) -> bool
        Set: ShowInfoPanel(self: WizardForm) = value
        """
        ...

    @property
    def ShowTitleCheckBox(self) -> bool:
        """
        Get: ShowTitleCheckBox(self: WizardForm) -> bool
        Set: ShowTitleCheckBox(self: WizardForm) = value
        """
        ...

    @property
    def ShowTitlePageFromTitleCheckBox(self) -> bool:
        """
        Get: ShowTitlePageFromTitleCheckBox(self: WizardForm) -> bool
        Set: ShowTitlePageFromTitleCheckBox(self: WizardForm) = value
        """
        ...

    @property
    def TipText(self) -> str:
        """
        Get: TipText(self: WizardForm) -> str
        Set: TipText(self: WizardForm) = value
        """
        ...

    @property
    def TitleCaption(self) -> str:
        """
        Get: TitleCaption(self: WizardForm) -> str
        Set: TitleCaption(self: WizardForm) = value
        """
        ...

    @property
    def TitleCheckBox(self) -> CheckBox:
        """ Get: TitleCheckBox(self: WizardForm) -> CheckBox """
        ...

    @property
    def TitleCheckBoxRegistryKey(self) -> RegistryKey:
        """
        Get: TitleCheckBoxRegistryKey(self: WizardForm) -> RegistryKey
        Set: TitleCheckBoxRegistryKey(self: WizardForm) = value
        """
        ...

    @property
    def TitleCheckBoxRegistryValue(self) -> str:
        """
        Get: TitleCheckBoxRegistryValue(self: WizardForm) -> str
        Set: TitleCheckBoxRegistryValue(self: WizardForm) = value
        """
        ...

    @property
    def TitleFillerGlyph(self) -> Image:
        """
        Get: TitleFillerGlyph(self: WizardForm) -> Image
        Set: TitleFillerGlyph(self: WizardForm) = value
        """
        ...

    @property
    def TitleFont(self) -> Font:
        """ Get: TitleFont(self: WizardForm) -> Font """
        ...

    @property
    def TitleGlyph(self) -> Image:
        """
        Get: TitleGlyph(self: WizardForm) -> Image
        Set: TitleGlyph(self: WizardForm) = value
        """
        ...

    @property
    def TitleGlyphBackColor(self) -> Color:
        """
        Get: TitleGlyphBackColor(self: WizardForm) -> Color
        Set: TitleGlyphBackColor(self: WizardForm) = value
        """
        ...

    @property
    def TitleHelpTopicKeyword(self) -> str:
        """
        Get: TitleHelpTopicKeyword(self: WizardForm) -> str
        Set: TitleHelpTopicKeyword(self: WizardForm) = value
        """
        ...

    @property
    def TitleText(self) -> str:
        """
        Get: TitleText(self: WizardForm) -> str
        Set: TitleText(self: WizardForm) = value
        """
        ...

    @property
    def WizardCancelButton(self) -> Button:
        """ Get: WizardCancelButton(self: WizardForm) -> Button """
        ...

    @property
    def WizardInputs(self) -> WizardInputs:
        """
        Get: WizardInputs(self: WizardForm) -> WizardInputs
        Set: WizardInputs(self: WizardForm) = value
        """
        ...


    def BackPage(self): # -> 
        """ BackPage(self: WizardForm) """
        ...

    def Cancel(self): # -> 
        """ Cancel(self: WizardForm) """
        ...

    def FillSummaryText(self, summaryTextBox): # ->  # Not found arg types: {'summaryTextBox': 'RichTextBox'}
        """ FillSummaryText(self: WizardForm, summaryTextBox: RichTextBox) """
        ...

    def Finish(self) -> bool:
        """ Finish(self: WizardForm) -> bool """
        ...

    def GetInitialClientSize(self, *args): #cannot find CLR method
        """ GetInitialClientSize(self: WizardForm) -> Size """
        ...

    def GetPageSize(self, *args): #cannot find CLR method
        """ GetPageSize(self: WizardForm) -> Size """
        ...

    def GetSummaryText(self) -> str:
        """ GetSummaryText(self: WizardForm) -> str """
        ...

    def NextPage(self, nextPage:WizardPage = ...): # -> 
        """ NextPage(self: WizardForm)NextPage(self: WizardForm, nextPage: WizardPage) """
        ...

    def OnCancel(self, *args): #cannot find CLR method
        """ OnCancel(self: WizardForm, e: EventArgs) """
        ...

    def OnFinish(self, *args): #cannot find CLR method
        """ OnFinish(self: WizardForm, e: CancelEventArgs) """
        ...

    def OnHelpDisplay(self, *args): #cannot find CLR method
        """ OnHelpDisplay(self: WizardForm) """
        ...

    def OnInitializeProgressPage(self, *args): #cannot find CLR method
        """ OnInitializeProgressPage(self: WizardForm) """
        ...

    def OnNextWizardPage(self, page:WizardPage): # -> 
        """ OnNextWizardPage(self: WizardForm, page: WizardPage) """
        ...

    def PreparePages(self, *args): #cannot find CLR method
        """ PreparePages(self: WizardForm, wizardPages: Array[WizardPage]) """
        ...

    def ShowMessage(self, owner, *__args:Exception): # -> DialogResult # Not found arg types: {'owner': 'IWin32Window'}
        """
        ShowMessage(self: WizardForm, owner: IWin32Window, message: str, ex: Exception) -> DialogResult
        ShowMessage(self: WizardForm, owner: IWin32Window, ex: Exception) -> DialogResult
        """
        ...

    def UpdateFinishButtonText(self, *args): #cannot find CLR method
        """ UpdateFinishButtonText(self: WizardForm, isFinishPage: bool) """
        ...

    def __new__(cls, serviceProvider=None):
        """ no doc """
        ...


class WizardInputs: # skipped bases: <type 'object'>, <type 'object'>
    """ WizardInputs() """
    @property
    def CurrentTask(self) -> str:
        """
        Get: CurrentTask(self: WizardInputs) -> str
        Set: CurrentTask(self: WizardInputs) = value
        """
        ...


    def AddEditItem(self, *__args): # -> 
        """ AddEditItem(self: WizardInputs, taskName: str, name: str, value: object)AddEditItem(self: WizardInputs, name: str, value: object)AddEditItem(self: WizardInputs, taskName: str, enumName: int, value: object)AddEditItem(self: WizardInputs, enumName: int, value: object) """
        ...

    def AddItem(self, *__args): # -> 
        """ AddItem(self: WizardInputs, taskName: str, name: str, value: object)AddItem(self: WizardInputs, name: str, value: object)AddItem(self: WizardInputs, taskName: str, enumName: int, value: object)AddItem(self: WizardInputs, enumName: int, value: object) """
        ...

    def EditItem(self, *__args): # -> 
        """ EditItem(self: WizardInputs, taskName: str, name: str, value: object)EditItem(self: WizardInputs, name: str, value: object)EditItem(self: WizardInputs, taskName: str, enumName: int, value: object)EditItem(self: WizardInputs, enumName: int, value: object) """
        ...

    def FindBool(self, *__args:int) -> bool:
        """
        FindBool(self: WizardInputs, taskName: str, enumName: int) -> bool
        FindBool(self: WizardInputs, enumName: int) -> bool
        FindBool(self: WizardInputs, taskName: str, name: str) -> bool
        FindBool(self: WizardInputs, name: str) -> bool
        """
        ...

    def FindItem(self, *__args:str) -> object:
        """
        FindItem(self: WizardInputs, taskName: str, name: str) -> object
        FindItem(self: WizardInputs, name: str) -> object
        FindItem(self: WizardInputs, taskName: str, enumName: int) -> object
        FindItem(self: WizardInputs, enumName: int) -> object
        """
        ...

    def FindString(self, *__args:int) -> str:
        """
        FindString(self: WizardInputs, taskName: str, enumName: int) -> str
        FindString(self: WizardInputs, enumName: int) -> str
        FindString(self: WizardInputs, taskName: str, name: str) -> str
        FindString(self: WizardInputs, name: str) -> str
        """
        ...

    def GetTaskItemEnumerator(self, taskName:str) -> IEnumerator:
        """ GetTaskItemEnumerator(self: WizardInputs, taskName: str) -> IEnumerator """
        ...

    def GetTaskNamesEnumerator(self) -> IEnumerator:
        """ GetTaskNamesEnumerator(self: WizardInputs) -> IEnumerator """
        ...

    def RemoveItem(self, *__args:str): # -> 
        """ RemoveItem(self: WizardInputs, taskName: str, name: str)RemoveItem(self: WizardInputs, name: str)RemoveItem(self: WizardInputs, taskName: str, enumName: int)RemoveItem(self: WizardInputs, enumName: int) """
        ...


class WizardTask: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Finished(self) -> bool:
        """ Get: Finished(self: WizardTask) -> bool """
        ...

    @property
    def TaskName(self) -> str:
        """
        Get: TaskName(self: WizardTask) -> str
        Set: TaskName(self: WizardTask) = value
        """
        ...


    def Execute(self, wi:WizardInputs): # -> 
        """ Execute(self: WizardTask, wi: WizardInputs) """
        ...

    def OnListChanged(self, wi:WizardInputs): # -> 
        """ OnListChanged(self: WizardTask, wi: WizardInputs) """
        ...

    def UndoTask(self, wi:WizardInputs): # -> 
        """ UndoTask(self: WizardTask, wi: WizardInputs) """
        ...


# variables with complex values

