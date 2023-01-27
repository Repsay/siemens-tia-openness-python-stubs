# encoding: utf-8
# module Microsoft.DataWarehouse.Design calls itself Design
# from Microsoft.DataWarehouse.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

"""The following names are not found in the module: (DialogResult, 
    MessageBoxButtons)
"""

# no functions
# classes

class IErrorReportingService: # skipped bases: <type 'object'>
    """ no doc """
    def ReportError(self, *__args:Exception): # -> 
        """ ReportError(self: IErrorReportingService, description: str, e: Exception, caption: str)ReportError(self: IErrorReportingService, description: str, e: Exception)ReportError(self: IErrorReportingService, e: Exception)ReportError(self: IErrorReportingService, description: str) """
        ...

    def ShowPendingErrors(self): # -> 
        """ ShowPendingErrors(self: IErrorReportingService) """
        ...


class IExceptionContainer: # skipped bases: <type 'object'>
    """ no doc """
    def AddException(self, context:object, *__args:Exception): # -> 
        """ AddException(self: IExceptionContainer, context: object, e: Exception)AddException(self: IExceptionContainer, context: object, errorMessage: str) """
        ...

    def Clear(self, context:object = ...): # -> 
        """ Clear(self: IExceptionContainer, context: object)Clear(self: IExceptionContainer) """
        ...

    def GetExceptions(self, context:object = ...) -> Array:
        """
        GetExceptions(self: IExceptionContainer) -> Array[Exception]
        GetExceptions(self: IExceptionContainer, context: object) -> Array[Exception]
        """
        ...


class IUserPromptService: # skipped bases: <type 'object'>
    """ no doc """
    def ReportError(self, *__args:Exception): # -> 
        """ ReportError(self: IUserPromptService, description: str, e: Exception)ReportError(self: IUserPromptService, e: Exception)ReportError(self: IUserPromptService, description: str) """
        ...

    def ShowMessage(self, message:str, *__args): # -> DialogResult # Not found arg types: {'*__args': 'MessageBoxButtons'}
        """
        ShowMessage(self: IUserPromptService, message: str)ShowMessage(self: IUserPromptService, message: str, caption: str, customButtons: Array[str], defaultButton: int, icon: MessageBoxIcon) -> int
        ShowMessage(self: IUserPromptService, message: str, customButtons: Array[str], defaultButton: int, icon: MessageBoxIcon) -> int
        ShowMessage(self: IUserPromptService, message: str, caption: str, customButtons: Array[str], defaultButton: int) -> int
        ShowMessage(self: IUserPromptService, message: str, customButtons: Array[str], defaultButton: int) -> int
        ShowMessage(self: IUserPromptService, message: str, caption: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, defaultButton: MessageBoxDefaultButton, parent: IWin32Window) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, caption: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, parent: IWin32Window) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, defaultButton: MessageBoxDefaultButton, parent: IWin32Window) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, parent: IWin32Window) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, caption: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, defaultButton: MessageBoxDefaultButton) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, caption: str, buttons: MessageBoxButtons, icon: MessageBoxIcon) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, defaultButton: MessageBoxDefaultButton) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, buttons: MessageBoxButtons, icon: MessageBoxIcon) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, caption: str, buttons: MessageBoxButtons) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, buttons: MessageBoxButtons) -> DialogResult
        ShowMessage(self: IUserPromptService, message: str, caption: str)ShowMessage(self: IUserPromptService, message: str, customButtons: Array[str], defaultButton: int, icon: MessageBoxIcon, parent: IWin32Window) -> int
        ShowMessage(self: IUserPromptService, message: str, caption: str, customButtons: Array[str], defaultButton: int, icon: MessageBoxIcon, parent: IWin32Window) -> int
        """
        ...

    def ShowPendingErrors(self): # -> 
        """ ShowPendingErrors(self: IUserPromptService) """
        ...


