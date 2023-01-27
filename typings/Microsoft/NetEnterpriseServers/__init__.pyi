# encoding: utf-8
# module Microsoft.NetEnterpriseServers calls itself NetEnterpriseServers
# from Microsoft.NetEnterpriseServers.ExceptionMessageBox, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32 import RegistryKey

from System import (AsyncCallback, Enum, EventArgs, IAsyncResult, 
    MulticastDelegate)

from System.Collections import IDictionary

from System.Drawing import Bitmap, Font

from typing import Self

"""The following names are not found in the module: (DialogResult, 
    IWin32Window, field#)
"""

# no functions
# classes

class CopyToClipboardEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    CopyToClipboardEventArgs(clipboardText: str)
    CopyToClipboardEventArgs()
    """
    @property
    def ClipboardText(self) -> str:
        """ Get: ClipboardText(self: CopyToClipboardEventArgs) -> str """
        ...

    @property
    def EventHandled(self) -> bool:
        """
        Get: EventHandled(self: CopyToClipboardEventArgs) -> bool
        Set: EventHandled(self: CopyToClipboardEventArgs) = value
        """
        ...


    def __new__(cls, clipboardText:str = ...) -> Self:
        """
        __new__(cls: type, clipboardText: str)
        __new__(cls: type)
        """
        ...


class CopyToClipboardEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CopyToClipboardEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CopyToClipboardEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CopyToClipboardEventHandler, sender: object, e: CopyToClipboardEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CopyToClipboardEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CopyToClipboardEventArgs): # -> 
        """ Invoke(self: CopyToClipboardEventHandler, sender: object, e: CopyToClipboardEventArgs) """
        ...


class ExceptionMessageBox: # skipped bases: <type 'object'>, <type 'object'>
    """
    ExceptionMessageBox()
    ExceptionMessageBox(exception: Exception)
    ExceptionMessageBox(text: str)
    ExceptionMessageBox(text: str, caption: str)
    ExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons)
    ExceptionMessageBox(text: str, caption: str, buttons: ExceptionMessageBoxButtons)
    ExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol)
    ExceptionMessageBox(text: str, caption: str, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol)
    ExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defaultButton: ExceptionMessageBoxDefaultButton)
    ExceptionMessageBox(text: str, caption: str, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defaultButton: ExceptionMessageBoxDefaultButton)
    ExceptionMessageBox(exception: Exception, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defaultButton: ExceptionMessageBoxDefaultButton, options: ExceptionMessageBoxOptions)
    ExceptionMessageBox(text: str, caption: str, buttons: ExceptionMessageBoxButtons, symbol: ExceptionMessageBoxSymbol, defaultButton: ExceptionMessageBoxDefaultButton, options: ExceptionMessageBoxOptions)
    """
    @property
    def AbortButtonText(self) -> str:
        """ Get: AbortButtonText() -> str """
        ...

    @property
    def Beep(self) -> bool:
        """
        Get: Beep(self: ExceptionMessageBox) -> bool
        Set: Beep(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def Buttons(self) -> ExceptionMessageBoxButtons:
        """
        Get: Buttons(self: ExceptionMessageBox) -> ExceptionMessageBoxButtons
        Set: Buttons(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CancelButtonText(self) -> str:
        """ Get: CancelButtonText() -> str """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ExceptionMessageBox) -> str
        Set: Caption(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CheckboxRegistryKey(self) -> RegistryKey:
        """
        Get: CheckboxRegistryKey(self: ExceptionMessageBox) -> RegistryKey
        Set: CheckboxRegistryKey(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CheckboxRegistryMeansDontShowDialog(self) -> bool:
        """
        Get: CheckboxRegistryMeansDontShowDialog(self: ExceptionMessageBox) -> bool
        Set: CheckboxRegistryMeansDontShowDialog(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CheckboxRegistryValue(self) -> str:
        """
        Get: CheckboxRegistryValue(self: ExceptionMessageBox) -> str
        Set: CheckboxRegistryValue(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CheckboxText(self) -> str:
        """
        Get: CheckboxText(self: ExceptionMessageBox) -> str
        Set: CheckboxText(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def CustomDialogResult(self) -> ExceptionMessageBoxDialogResult:
        """ Get: CustomDialogResult(self: ExceptionMessageBox) -> ExceptionMessageBoxDialogResult """
        ...

    @property
    def CustomSymbol(self) -> Bitmap:
        """
        Get: CustomSymbol(self: ExceptionMessageBox) -> Bitmap
        Set: CustomSymbol(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def Data(self) -> IDictionary:
        """ Get: Data(self: ExceptionMessageBox) -> IDictionary """
        ...

    @property
    def DefaultButton(self) -> ExceptionMessageBoxDefaultButton:
        """
        Get: DefaultButton(self: ExceptionMessageBox) -> ExceptionMessageBoxDefaultButton
        Set: DefaultButton(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def DefaultDialogResult(self): # -> DialogResult
        """
        Get: DefaultDialogResult(self: ExceptionMessageBox) -> DialogResult
        Set: DefaultDialogResult(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def FailButtonText(self) -> str:
        """ Get: FailButtonText() -> str """
        ...

    @property
    def Font(self) -> Font:
        """
        Get: Font(self: ExceptionMessageBox) -> Font
        Set: Font(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def HelpLink(self) -> str:
        """
        Get: HelpLink(self: ExceptionMessageBox) -> str
        Set: HelpLink(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def IgnoreButtonText(self) -> str:
        """ Get: IgnoreButtonText() -> str """
        ...

    @property
    def InnerException(self) -> Exception:
        """
        Get: InnerException(self: ExceptionMessageBox) -> Exception
        Set: InnerException(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def IsCheckboxChecked(self) -> bool:
        """
        Get: IsCheckboxChecked(self: ExceptionMessageBox) -> bool
        Set: IsCheckboxChecked(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def Message(self) -> Exception:
        """
        Get: Message(self: ExceptionMessageBox) -> Exception
        Set: Message(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def MessageLevelDefault(self) -> int:
        """
        Get: MessageLevelDefault(self: ExceptionMessageBox) -> int
        Set: MessageLevelDefault(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def NoButtonText(self) -> str:
        """ Get: NoButtonText() -> str """
        ...

    @property
    def OKButtonText(self) -> str:
        """ Get: OKButtonText() -> str """
        ...

    @property
    def Options(self) -> ExceptionMessageBoxOptions:
        """
        Get: Options(self: ExceptionMessageBox) -> ExceptionMessageBoxOptions
        Set: Options(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def RetryButtonText(self) -> str:
        """ Get: RetryButtonText() -> str """
        ...

    @property
    def ShowCheckbox(self) -> bool:
        """
        Get: ShowCheckbox(self: ExceptionMessageBox) -> bool
        Set: ShowCheckbox(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def ShowToolBar(self) -> bool:
        """
        Get: ShowToolBar(self: ExceptionMessageBox) -> bool
        Set: ShowToolBar(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def Symbol(self) -> ExceptionMessageBoxSymbol:
        """
        Get: Symbol(self: ExceptionMessageBox) -> ExceptionMessageBoxSymbol
        Set: Symbol(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ExceptionMessageBox) -> str
        Set: Text(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def UseOwnerFont(self) -> bool:
        """
        Get: UseOwnerFont(self: ExceptionMessageBox) -> bool
        Set: UseOwnerFont(self: ExceptionMessageBox) = value
        """
        ...

    @property
    def YesButtonText(self) -> str:
        """ Get: YesButtonText() -> str """
        ...


    @staticmethod
    def GetMessageText(exception:Exception) -> str:
        """ GetMessageText(exception: Exception) -> str """
        ...

    def SetButtonText(self, button1Text:str, button2Text:str = ..., button3Text:str = ..., button4Text:str = ..., button5Text:str = ...): # -> 
        """ SetButtonText(self: ExceptionMessageBox, button1Text: str, button2Text: str, button3Text: str, button4Text: str, button5Text: str)SetButtonText(self: ExceptionMessageBox, button1Text: str, button2Text: str, button3Text: str, button4Text: str)SetButtonText(self: ExceptionMessageBox, button1Text: str, button2Text: str, button3Text: str)SetButtonText(self: ExceptionMessageBox, button1Text: str, button2Text: str)SetButtonText(self: ExceptionMessageBox, button1Text: str) """
        ...

    def Show(self, *__args): # -> DialogResult # Not found arg types: {'*__args': 'IWin32Window'}
        """
        Show(self: ExceptionMessageBox, hwnd: IntPtr, message: str, source: str, sourceAppName: str, sourceAppVersion: str, sourceModule: str, sourceMessageId: str, sourceLanguage: str) -> DialogResult
        Show(self: ExceptionMessageBox, owner: IWin32Window) -> DialogResult
        """
        ...



class ExceptionMessageBoxButtons(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExceptionMessageBoxButtons, values: AbortRetryIgnore (4), Custom (6), OK (0), OKCancel (1), RetryCancel (5), YesNo (3), YesNoCancel (2) """
    AbortRetryIgnore: ExceptionMessageBoxButtons = ...
    Custom: ExceptionMessageBoxButtons = ...
    OK: ExceptionMessageBoxButtons = ...
    OKCancel: ExceptionMessageBoxButtons = ...
    RetryCancel: ExceptionMessageBoxButtons = ...
    value__ = ...
    YesNo: ExceptionMessageBoxButtons = ...
    YesNoCancel: ExceptionMessageBoxButtons = ...


class ExceptionMessageBoxDefaultButton(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExceptionMessageBoxDefaultButton, values: Button1 (0), Button2 (1), Button3 (2), Button4 (3), Button5 (4) """
    Button1: ExceptionMessageBoxDefaultButton = ...
    Button2: ExceptionMessageBoxDefaultButton = ...
    Button3: ExceptionMessageBoxDefaultButton = ...
    Button4: ExceptionMessageBoxDefaultButton = ...
    Button5: ExceptionMessageBoxDefaultButton = ...
    value__ = ...


class ExceptionMessageBoxDialogResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExceptionMessageBoxDialogResult, values: Button1 (1), Button2 (2), Button3 (3), Button4 (4), Button5 (5), None (0) """
    Button1: ExceptionMessageBoxDialogResult = ...
    Button2: ExceptionMessageBoxDialogResult = ...
    Button3: ExceptionMessageBoxDialogResult = ...
    Button4: ExceptionMessageBoxDialogResult = ...
    Button5: ExceptionMessageBoxDialogResult = ...
    value__ = ...


class ExceptionMessageBoxOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ExceptionMessageBoxOptions, values: None (0), RightAlign (1), RtlReading (2) """
    RightAlign: ExceptionMessageBoxOptions = ...
    RtlReading: ExceptionMessageBoxOptions = ...
    value__ = ...


class ExceptionMessageBoxSymbol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExceptionMessageBoxSymbol, values: Asterisk (5), Error (3), Exclamation (4), Hand (7), Information (2), None (0), Question (6), Stop (3), Warning (1) """
    Asterisk: ExceptionMessageBoxSymbol = ...
    Error: ExceptionMessageBoxSymbol = ...
    Exclamation: ExceptionMessageBoxSymbol = ...
    Hand: ExceptionMessageBoxSymbol = ...
    Information: ExceptionMessageBoxSymbol = ...
    Question: ExceptionMessageBoxSymbol = ...
    Stop: ExceptionMessageBoxSymbol = ...
    value__ = ...
    Warning: ExceptionMessageBoxSymbol = ...


