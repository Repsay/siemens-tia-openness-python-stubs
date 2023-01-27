# encoding: utf-8
# module Microsoft.VisualStudio.TextManager.Interop calls itself Interop
# from Microsoft.VisualStudio.TextManager.Interop.8.0, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Guid, Int16, IntPtr, UInt32

from typing import Tuple as Tuple_

"""The following names are not found in the module: __ComObject, field#
"""

# no functions
# classes

class AtomicTextProviderFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AtomicTextProviderFlags, values: atpDefault (0), atpGlyph (1), atpTextAttributes (2) """
    atpDefault: AtomicTextProviderFlags = ...
    atpGlyph: AtomicTextProviderFlags = ...
    atpTextAttributes: AtomicTextProviderFlags = ...
    value__ = ...


class BufferCoordinatorReplicationDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BufferCoordinatorReplicationDirection, values: BCRD_PRIMARY_TO_SECONDARY (1), BCRD_SECONDARY_TO_PRIMARY (2) """
    BCRD_PRIMARY_TO_SECONDARY: BufferCoordinatorReplicationDirection = ...
    BCRD_SECONDARY_TO_PRIMARY: BufferCoordinatorReplicationDirection = ...
    value__ = ...


class ChangeCommitGestureFlags2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ChangeCommitGestureFlags2, values: CCG_REFORMAT (256) """
    CCG_REFORMAT: ChangeCommitGestureFlags2 = ...
    value__ = ...


class CODEMEMBERTYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CODEMEMBERTYPE, values: CODEMEMBERTYPE_EVENT_HANDLERS (2), CODEMEMBERTYPE_EVENTS (1), CODEMEMBERTYPE_USER_FUNCTIONS (4) """
    CODEMEMBERTYPE_EVENTS: CODEMEMBERTYPE = ...
    CODEMEMBERTYPE_EVENT_HANDLERS: CODEMEMBERTYPE = ...
    CODEMEMBERTYPE_USER_FUNCTIONS: CODEMEMBERTYPE = ...
    value__ = ...


class COMMONLANGUAGEBLOCK(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum COMMONLANGUAGEBLOCK, values: CLB_EXCEPTION_BLOCK (1), CLB_FINAL_BLOCK (2), CLB_TRY_BLOCK (0) """
    CLB_EXCEPTION_BLOCK: COMMONLANGUAGEBLOCK = ...
    CLB_FINAL_BLOCK: COMMONLANGUAGEBLOCK = ...
    CLB_TRY_BLOCK: COMMONLANGUAGEBLOCK = ...
    value__ = ...


class ContainedLanguageRefreshMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContainedLanguageRefreshMode, values: CLRM_COMPILEFILE (1), CLRM_COMPILEPROJECT (2) """
    CLRM_COMPILEFILE: ContainedLanguageRefreshMode = ...
    CLRM_COMPILEPROJECT: ContainedLanguageRefreshMode = ...
    value__ = ...


class ContainedLanguageRenameType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContainedLanguageRenameType, values: CLRT_CLASS (0), CLRT_CLASSMEMBER (1), CLRT_NAMESPACE (2), CLRT_OTHER (3) """
    CLRT_CLASS: ContainedLanguageRenameType = ...
    CLRT_CLASSMEMBER: ContainedLanguageRenameType = ...
    CLRT_NAMESPACE: ContainedLanguageRenameType = ...
    CLRT_OTHER: ContainedLanguageRenameType = ...
    value__ = ...


class ExternalError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrFileName = ...
    bstrText = ...
    fError = ...
    iCol = ...
    iErrorID = ...
    iLine = ...


class FONTCOLORPREFERENCES2: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    hBoldViewFont = ...
    hRegularViewFont = ...
    pColorTable = ...
    pguidColorCategory = ...
    pguidColorService = ...
    pguidFontCategory = ...


class FRAMEPREFERENCES2: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    fHorzScrollbar = ...
    fVertScrollbar = ...


class GLDE_FLAGS2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) GLDE_FLAGS2, values: gldeUsePaintView (64) """
    gldeUsePaintView: GLDE_FLAGS2 = ...
    value__ = ...


class HIDDEN_REGION_BEHAVIOR2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HIDDEN_REGION_BEHAVIOR2, values: hrbClientDrawn (2), hrbNoUserControls (4) """
    hrbClientDrawn: HIDDEN_REGION_BEHAVIOR2 = ...
    hrbNoUserControls: HIDDEN_REGION_BEHAVIOR2 = ...
    value__ = ...


class IntellisenseHostFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) IntellisenseHostFlags, values: IHF_FORCECOMMITTOCONTEXT (8), IHF_NOSEPARATESUBJECT (2), IHF_OVERTYPE (16), IHF_READONLYCONTEXT (1), IHF_SINGLELINESUBJECT (4) """
    IHF_FORCECOMMITTOCONTEXT: IntellisenseHostFlags = ...
    IHF_NOSEPARATESUBJECT: IntellisenseHostFlags = ...
    IHF_OVERTYPE: IntellisenseHostFlags = ...
    IHF_READONLYCONTEXT: IntellisenseHostFlags = ...
    IHF_SINGLELINESUBJECT: IntellisenseHostFlags = ...
    value__ = ...


class IPersistFileCheckSum: # skipped bases: <type 'object'>
    """ no doc """
    def CalculateCheckSum(self, guidCheckSumAlgorithm, cbBufferSize, pbHash, pcbActualSize) -> Tuple_[int, Guid, Array, UInt32]:
        """ CalculateCheckSum(self: IPersistFileCheckSum, guidCheckSumAlgorithm: Guid, cbBufferSize: UInt32) -> (int, Guid, Array[Byte], UInt32) """
        ...


class IVsAtomicTextProvider: # skipped bases: <type 'object'>
    """ no doc """
    def DrawAtomGlyph(self):
        """ no doc """
        ...

    def GetAtomAttributes(self, dwLength, pColorAttr) -> Tuple_[int, Array]:
        """ GetAtomAttributes(self: IVsAtomicTextProvider, dwLength: UInt32) -> (int, Array[UInt32]) """
        ...

    def GetAtomFlags(self, pdwFlags) -> Tuple_[int, UInt32]:
        """ GetAtomFlags(self: IVsAtomicTextProvider) -> (int, UInt32) """
        ...

    def GetAtomGlyphWidth(self, iPixSpaceWidth, pGlyphPix) -> Tuple_[int, int]:
        """ GetAtomGlyphWidth(self: IVsAtomicTextProvider, iPixSpaceWidth: int) -> (int, int) """
        ...


class IVsAutoOutliningClient: # skipped bases: <type 'object'>
    """ no doc """
    def QueryWaitForAutoOutliningCallback(self, fWait) -> Tuple_[int, int]:
        """ QueryWaitForAutoOutliningCallback(self: IVsAutoOutliningClient) -> (int, int) """
        ...


class IVsBufferExtraFiles: # skipped bases: <type 'object'>
    """ no doc """
    def GetQueryEditFilesDocuments(self):
        """ no doc """
        ...


class IVsCanCoordinatorClipTextSpan: # skipped bases: <type 'object'>
    """ no doc """
    def ShouldClipSpanToValidSpanInSecondaryBuffer(self):
        """ no doc """
        ...


class IVsCodePageSelection: # skipped bases: <type 'object'>
    """ no doc """
    def ShowEncodingDialog(self):
        """ no doc """
        ...


class IVsColorizer2: # skipped bases: <type 'object'>
    """ no doc """
    def BeginColorization(self) -> int:
        """ BeginColorization(self: IVsColorizer2) -> int """
        ...

    def EndColorization(self) -> int:
        """ EndColorization(self: IVsColorizer2) -> int """
        ...


class IVsCommandWindowCompletion: # skipped bases: <type 'object'>
    """ no doc """
    def SetCompletionContext(self):
        """ no doc """
        ...


class IVsCompletionSetBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetBuilderCount(self, piCount:int) -> Tuple_[int, int]:
        """ GetBuilderCount(self: IVsCompletionSetBuilder, piCount: int) -> (int, int) """
        ...

    def GetBuilderDescriptionText(self, iIndex, pbstrDescription) -> Tuple_[int, str]:
        """ GetBuilderDescriptionText(self: IVsCompletionSetBuilder, iIndex: int) -> (int, str) """
        ...

    def GetBuilderDisplayText(self, iIndex, pbstrText, piGlyph) -> Tuple_[int, str, Array]:
        """ GetBuilderDisplayText(self: IVsCompletionSetBuilder, iIndex: int) -> (int, str, Array[int]) """
        ...

    def GetBuilderImageList(self, phImages) -> Tuple_[int, IntPtr]:
        """ GetBuilderImageList(self: IVsCompletionSetBuilder) -> (int, IntPtr) """
        ...

    def GetBuilderItemColor(self, iIndex, dwFGColor, dwBGColor) -> Tuple_[int, UInt32, UInt32]:
        """ GetBuilderItemColor(self: IVsCompletionSetBuilder, iIndex: int) -> (int, UInt32, UInt32) """
        ...

    def OnBuilderCommit(self, iIndex:int) -> int:
        """ OnBuilderCommit(self: IVsCompletionSetBuilder, iIndex: int) -> int """
        ...


class IVsCompletionSetEx: # skipped bases: <type 'object'>
    """ no doc """
    def CompareItems(self, bstrSoFar, bstrOther, lCharactersToCompare, pLResult) -> Tuple_[int, int]:
        """ CompareItems(self: IVsCompletionSetEx, bstrSoFar: str, bstrOther: str, lCharactersToCompare: int) -> (int, int) """
        ...

    def DecreaseFilterLevel(self, iSelectedItem:int) -> int:
        """ DecreaseFilterLevel(self: IVsCompletionSetEx, iSelectedItem: int) -> int """
        ...

    def GetCompletionItemColor(self, iIndex, dwFGColor, dwBGColor) -> Tuple_[int, UInt32, UInt32]:
        """ GetCompletionItemColor(self: IVsCompletionSetEx, iIndex: int) -> (int, UInt32, UInt32) """
        ...

    def GetFilterLevel(self, iFilterLevel) -> Tuple_[int, int]:
        """ GetFilterLevel(self: IVsCompletionSetEx) -> (int, int) """
        ...

    def IncreaseFilterLevel(self, iSelectedItem:int) -> int:
        """ IncreaseFilterLevel(self: IVsCompletionSetEx, iSelectedItem: int) -> int """
        ...

    def OnCommitComplete(self) -> int:
        """ OnCommitComplete(self: IVsCompletionSetEx) -> int """
        ...


class IVsContainedCode: # skipped bases: <type 'object'>
    """ no doc """
    def EnumOriginalCodeBlocks(self, ppEnum) -> Tuple_[int, IVsEnumCodeBlocks]:
        """ EnumOriginalCodeBlocks(self: IVsContainedCode) -> (int, IVsEnumCodeBlocks) """
        ...

    def HostSpansUpdated(self) -> int:
        """ HostSpansUpdated(self: IVsContainedCode) -> int """
        ...


class IVsContainedLanguage: # skipped bases: <type 'object'>
    """ no doc """
    def GetColorizer(self):
        """ no doc """
        ...

    def GetLanguageServiceID(self, pguidLangService) -> Tuple_[int, Guid]:
        """ GetLanguageServiceID(self: IVsContainedLanguage) -> (int, Guid) """
        ...

    def GetTextViewFilter(self):
        """ no doc """
        ...

    def Refresh(self, dwRefreshMode:UInt32) -> int:
        """ Refresh(self: IVsContainedLanguage, dwRefreshMode: UInt32) -> int """
        ...

    def SetBufferCoordinator(self):
        """ no doc """
        ...

    def SetHost(self):
        """ no doc """
        ...

    def WaitForReadyState(self) -> int:
        """ WaitForReadyState(self: IVsContainedLanguage) -> int """
        ...


class IVsContainedLanguageCodeSupport: # skipped bases: <type 'object'>
    """ no doc """
    def CreateUniqueEventName(self, pszClassName, pszObjectName, pszNameOfEvent, pbstrEventHandlerName) -> Tuple_[int, str]:
        """ CreateUniqueEventName(self: IVsContainedLanguageCodeSupport, pszClassName: str, pszObjectName: str, pszNameOfEvent: str) -> (int, str) """
        ...

    def EnsureEventHandler(self):
        """ no doc """
        ...

    def GetBaseClassName(self, pszClassName, pbstrBaseClassName) -> Tuple_[int, str]:
        """ GetBaseClassName(self: IVsContainedLanguageCodeSupport, pszClassName: str) -> (int, str) """
        ...

    def GetCompatibleEventHandlers(self, pszClassName, pszObjectTypeName, pszNameOfEvent, pcMembers, ppbstrEventHandlerNames, ppbstrMemberIDs) -> Tuple_[int, int, IntPtr, IntPtr]:
        """ GetCompatibleEventHandlers(self: IVsContainedLanguageCodeSupport, pszClassName: str, pszObjectTypeName: str, pszNameOfEvent: str) -> (int, int, IntPtr, IntPtr) """
        ...

    def GetEventHandlerMemberID(self, pszClassName, pszObjectTypeName, pszNameOfEvent, pszEventHandlerName, pbstrUniqueMemberID) -> Tuple_[int, str]:
        """ GetEventHandlerMemberID(self: IVsContainedLanguageCodeSupport, pszClassName: str, pszObjectTypeName: str, pszNameOfEvent: str, pszEventHandlerName: str) -> (int, str) """
        ...

    def GetMemberNavigationPoint(self):
        """ no doc """
        ...

    def GetMembers(self, pszClassName, dwFlags, pcMembers, ppbstrDisplayNames, ppbstrMemberIDs) -> Tuple_[int, int, IntPtr, IntPtr]:
        """ GetMembers(self: IVsContainedLanguageCodeSupport, pszClassName: str, dwFlags: UInt32) -> (int, int, IntPtr, IntPtr) """
        ...

    def IsValidID(self, bstrID, pfIsValidID) -> Tuple_[int, bool]:
        """ IsValidID(self: IVsContainedLanguageCodeSupport, bstrID: str) -> (int, bool) """
        ...

    def OnRenamed(self, clrt:ContainedLanguageRenameType, bstrOldID:str, bstrNewID:str) -> int:
        """ OnRenamed(self: IVsContainedLanguageCodeSupport, clrt: ContainedLanguageRenameType, bstrOldID: str, bstrNewID: str) -> int """
        ...


class IVsContainedLanguageColorizer: # skipped bases: <type 'object'>
    """ no doc """
    def ColorizeLineFragment(self, iLine, iIndex, iLength, pszText, iState, pAttributes, piNewState) -> Tuple_[int, UInt32, int]:
        """ ColorizeLineFragment(self: IVsContainedLanguageColorizer, iLine: int, iIndex: int, iLength: int, pszText: str, iState: int) -> (int, UInt32, int) """
        ...


class IVsContainedLanguageFactory: # skipped bases: <type 'object'>
    """ no doc """
    def GetLanguage(self):
        """ no doc """
        ...


class IVsContainedLanguageHostEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnViewChange(self, fTextView:int) -> int:
        """ OnViewChange(self: IVsContainedLanguageHostEvents, fTextView: int) -> int """
        ...


class IVsContainedLanguageProjectNameProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetProjectName(self, itemid, pbstrProjectName) -> Tuple_[int, str]:
        """ GetProjectName(self: IVsContainedLanguageProjectNameProvider, itemid: UInt32) -> (int, str) """
        ...


class IVsContainedLanguageStaticEventBinding: # skipped bases: <type 'object'>
    """ no doc """
    def AddStaticEventBinding(self, pszClassName:str, pszUniqueMemberID:str, pszObjectName:str, pszNameOfEvent:str) -> int:
        """ AddStaticEventBinding(self: IVsContainedLanguageStaticEventBinding, pszClassName: str, pszUniqueMemberID: str, pszObjectName: str, pszNameOfEvent: str) -> int """
        ...

    def EnsureStaticEventHandler(self):
        """ no doc """
        ...

    def GetStaticEventBindingsForObject(self, pszClassName, pszObjectName, pcMembers, ppbstrEventNames, ppbstrDisplayNames, ppbstrMemberIDs) -> Tuple_[int, int, IntPtr, IntPtr, IntPtr]:
        """ GetStaticEventBindingsForObject(self: IVsContainedLanguageStaticEventBinding, pszClassName: str, pszObjectName: str) -> (int, int, IntPtr, IntPtr, IntPtr) """
        ...

    def RemoveStaticEventBinding(self, pszClassName:str, pszUniqueMemberID:str, pszObjectName:str, pszNameOfEvent:str) -> int:
        """ RemoveStaticEventBinding(self: IVsContainedLanguageStaticEventBinding, pszClassName: str, pszUniqueMemberID: str, pszObjectName: str, pszNameOfEvent: str) -> int """
        ...


class IVsDropdownBarClientEx: # skipped bases: <type 'object'>
    """ no doc """
    def GetEntryIndent(self, iCombo, iIndex, pIndent) -> Tuple_[int, UInt32]:
        """ GetEntryIndent(self: IVsDropdownBarClientEx, iCombo: int, iIndex: int) -> (int, UInt32) """
        ...


class IVsEnumBufferCoordinatorSpans: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IVsEnumBufferCoordinatorSpans]:
        """ Clone(self: IVsEnumBufferCoordinatorSpans) -> (int, IVsEnumBufferCoordinatorSpans) """
        ...

    def Next(self):
        """ no doc """
        ...

    def Reset(self) -> int:
        """ Reset(self: IVsEnumBufferCoordinatorSpans) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IVsEnumBufferCoordinatorSpans, celt: UInt32) -> int """
        ...


class IVsEnumCodeBlocks: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IVsEnumCodeBlocks]:
        """ Clone(self: IVsEnumCodeBlocks) -> (int, IVsEnumCodeBlocks) """
        ...

    def Next(self):
        """ no doc """
        ...

    def Reset(self) -> int:
        """ Reset(self: IVsEnumCodeBlocks) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IVsEnumCodeBlocks, celt: UInt32) -> int """
        ...


class IVsEnumExternalErrors: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppErrors) -> Tuple_[int, IVsEnumExternalErrors]:
        """ Clone(self: IVsEnumExternalErrors) -> (int, IVsEnumExternalErrors) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IVsEnumExternalErrors, celt: UInt32) -> (int, Array[ExternalError], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IVsEnumExternalErrors) -> int """
        ...

    def Skip(self, celts:UInt32) -> int:
        """ Skip(self: IVsEnumExternalErrors, celts: UInt32) -> int """
        ...


class IVsExpansionClient: # skipped bases: <type 'object'>
    """ no doc """
    def EndExpansion(self) -> int:
        """ EndExpansion(self: IVsExpansionClient) -> int """
        ...

    def FormatSpan(self):
        """ no doc """
        ...

    def GetExpansionFunction(self):
        """ no doc """
        ...

    def IsValidKind(self):
        """ no doc """
        ...

    def IsValidType(self):
        """ no doc """
        ...

    def OnAfterInsertion(self):
        """ no doc """
        ...

    def OnBeforeInsertion(self):
        """ no doc """
        ...

    def OnItemChosen(self, pszTitle:str, pszPath:str) -> int:
        """ OnItemChosen(self: IVsExpansionClient, pszTitle: str, pszPath: str) -> int """
        ...

    def PositionCaretForEditing(self):
        """ no doc """
        ...


class IVsExpansionEnumeration: # skipped bases: <type 'object'>
    """ no doc """
    def GetCount(self, pCount) -> Tuple_[int, UInt32]:
        """ GetCount(self: IVsExpansionEnumeration) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IVsExpansionEnumeration, celt: UInt32) -> (int, Array[IntPtr], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IVsExpansionEnumeration) -> int """
        ...


class IVsExpansionEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnAfterSnippetsKeyBindingChange(self, dwCmdGuid:UInt32, dwCmdId:UInt32, fBound:int) -> int:
        """ OnAfterSnippetsKeyBindingChange(self: IVsExpansionEvents, dwCmdGuid: UInt32, dwCmdId: UInt32, fBound: int) -> int """
        ...

    def OnAfterSnippetsUpdate(self) -> int:
        """ OnAfterSnippetsUpdate(self: IVsExpansionEvents) -> int """
        ...


class IVsExpansionFunction: # skipped bases: <type 'object'>
    """ no doc """
    def FieldChanged(self, bstrField, fRequeryFunction) -> Tuple_[int, int]:
        """ FieldChanged(self: IVsExpansionFunction, bstrField: str) -> (int, int) """
        ...

    def GetCurrentValue(self, bstrValue, fHasCurrentValue) -> Tuple_[int, str, int]:
        """ GetCurrentValue(self: IVsExpansionFunction) -> (int, str, int) """
        ...

    def GetDefaultValue(self, bstrValue, fHasDefaultValue) -> Tuple_[int, str, int]:
        """ GetDefaultValue(self: IVsExpansionFunction) -> (int, str, int) """
        ...

    def GetFunctionType(self, pFuncType) -> Tuple_[int, UInt32]:
        """ GetFunctionType(self: IVsExpansionFunction) -> (int, UInt32) """
        ...

    def GetListCount(self, iCount) -> Tuple_[int, int]:
        """ GetListCount(self: IVsExpansionFunction) -> (int, int) """
        ...

    def GetListText(self, iIndex, pbstrText) -> Tuple_[int, str]:
        """ GetListText(self: IVsExpansionFunction, iIndex: int) -> (int, str) """
        ...

    def ReleaseFunction(self) -> int:
        """ ReleaseFunction(self: IVsExpansionFunction) -> int """
        ...


class IVsExpansionIntellisenseHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetCurrentLevel(self, pLevel) -> Tuple_[int, int]:
        """ GetCurrentLevel(self: IVsExpansionIntellisenseHost) -> (int, int) """
        ...

    def GetSelection(self, iStart, iEnd) -> Tuple_[int, int, int]:
        """ GetSelection(self: IVsExpansionIntellisenseHost) -> (int, int, int) """
        ...

    def GetText(self, bstrText) -> Tuple_[int, str]:
        """ GetText(self: IVsExpansionIntellisenseHost) -> (int, str) """
        ...

    def GetTextLen(self, iLen) -> Tuple_[int, int]:
        """ GetTextLen(self: IVsExpansionIntellisenseHost) -> (int, int) """
        ...

    def SetSelection(self, iStart:int, iEnd:int) -> int:
        """ SetSelection(self: IVsExpansionIntellisenseHost, iStart: int, iEnd: int) -> int """
        ...

    def SetText(self, bstrText:str, fReplaceAll:int) -> int:
        """ SetText(self: IVsExpansionIntellisenseHost, bstrText: str, fReplaceAll: int) -> int """
        ...


class IVsExpansionManager: # skipped bases: <type 'object'>
    """ no doc """
    def EnumerateExpansions(self, guidLang, fShortCutOnly, bstrTypes, iCountTypes, fIncludeNULLType, fIncludeDuplicates, pEnum) -> Tuple_[int, IVsExpansionEnumeration]:
        """ EnumerateExpansions(self: IVsExpansionManager, guidLang: Guid, fShortCutOnly: int, bstrTypes: Array[str], iCountTypes: int, fIncludeNULLType: int, fIncludeDuplicates: int) -> (int, IVsExpansionEnumeration) """
        ...

    def GetExpansionByShortcut(self):
        """ no doc """
        ...

    def GetSnippetShortCutKeybindingState(self, fBound) -> Tuple_[int, int]:
        """ GetSnippetShortCutKeybindingState(self: IVsExpansionManager) -> (int, int) """
        ...

    def GetTokenPath(self, token, pbstrPath) -> Tuple_[int, str]:
        """ GetTokenPath(self: IVsExpansionManager, token: UInt32) -> (int, str) """
        ...

    def InvokeInsertionUI(self):
        """ no doc """
        ...


class IVsExternalCompletionSet: # skipped bases: <type 'object'>
    """ no doc """
    def SetIntellisenseHost(self):
        """ no doc """
        ...

    def UpdateCompSet(self) -> int:
        """ UpdateCompSet(self: IVsExternalCompletionSet) -> int """
        ...


class IVsFileExtensionMappingEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnFileExtensionsReset(self) -> int:
        """ OnFileExtensionsReset(self: IVsFileExtensionMappingEvents) -> int """
        ...


class IVsFindCancelDialog: # skipped bases: <type 'object'>
    """ no doc """
    def CloseDialog(self) -> int:
        """ CloseDialog(self: IVsFindCancelDialog) -> int """
        ...

    def LaunchDialog(self) -> int:
        """ LaunchDialog(self: IVsFindCancelDialog) -> int """
        ...

    def QueryDialog(self, pfCancel) -> Tuple_[int, int]:
        """ QueryDialog(self: IVsFindCancelDialog) -> (int, int) """
        ...


class IVsHiColorItem: # skipped bases: <type 'object'>
    """ no doc """
    def GetColorData(self, cdElement, pcrColor) -> Tuple_[int, UInt32]:
        """ GetColorData(self: IVsHiColorItem, cdElement: int) -> (int, UInt32) """
        ...


class IVsHiddenRegionEx: # skipped bases: <type 'object'>
    """ no doc """
    def GetBannerAttr(self, dwLength, pColorAttr) -> Tuple_[int, Array]:
        """ GetBannerAttr(self: IVsHiddenRegionEx, dwLength: UInt32) -> (int, Array[UInt32]) """
        ...

    def SetBannerAttr(self, dwLength:UInt32, pColorAttr:Array) -> int:
        """ SetBannerAttr(self: IVsHiddenRegionEx, dwLength: UInt32, pColorAttr: Array[UInt32]) -> int """
        ...


class IVsHiddenTextClientEx: # skipped bases: <type 'object'>
    """ no doc """
    def DrawBannerGlyph(self):
        """ no doc """
        ...

    def GetBannerGlyphWidth(self, iPixSpaceWidth, pGlyphPix) -> Tuple_[int, int]:
        """ GetBannerGlyphWidth(self: IVsHiddenTextClientEx, iPixSpaceWidth: int) -> (int, int) """
        ...


class IVsHiddenTextSessionEx: # skipped bases: <type 'object'>
    """ no doc """
    def AddHiddenRegionsEx(self):
        """ no doc """
        ...


class IVsImmediateStatementCompletion: # skipped bases: <type 'object'>
    """ no doc """
    def EnableStatementCompletion_Deprecated(self, fEnable:int, iStartIndex:int, iEndIndex:int) -> int:
        """ EnableStatementCompletion_Deprecated(self: IVsImmediateStatementCompletion, fEnable: int, iStartIndex: int, iEndIndex: int) -> int """
        ...

    def InstallStatementCompletion(self):
        """ no doc """
        ...

    def SetCompletionContext_Deprecated(self):
        """ no doc """
        ...


class IVsImmediateStatementCompletion2(IVsImmediateStatementCompletion): # skipped bases: <type 'object'>
    """ no doc """
    def EnableStatementCompletion(self):
        """ no doc """
        ...

    def GetFilter(self):
        """ no doc """
        ...

    def SetCompletionContext(self):
        """ no doc """
        ...


class IVsInsertionUI: # skipped bases: <type 'object'>
    """ no doc """
    def GetWindowHandle(self, hwnd) -> Tuple_[int, IntPtr]:
        """ GetWindowHandle(self: IVsInsertionUI) -> (int, IntPtr) """
        ...

    def Hide(self) -> int:
        """ Hide(self: IVsInsertionUI) -> int """
        ...


class IVsIntellisenseLangTip: # skipped bases: <type 'object'>
    """ no doc """
    def Close(self, fDeleteThis:int) -> int:
        """ Close(self: IVsIntellisenseLangTip, fDeleteThis: int) -> int """
        ...

    def Create(self):
        """ no doc """
        ...

    def GetOverloadCount(self, plOverloadCount) -> Tuple_[int, int]:
        """ GetOverloadCount(self: IVsIntellisenseLangTip) -> (int, int) """
        ...

    def GetSizePreferences(self):
        """ no doc """
        ...

    def GetSizeY(self, pSizeY) -> Tuple_[int, Int16]:
        """ GetSizeY(self: IVsIntellisenseLangTip) -> (int, Int16) """
        ...

    def Initialize(self):
        """ no doc """
        ...

    def IsActive(self, pfIsActive) -> Tuple_[int, int]:
        """ IsActive(self: IVsIntellisenseLangTip) -> (int, int) """
        ...

    def ScrollDown(self) -> int:
        """ ScrollDown(self: IVsIntellisenseLangTip) -> int """
        ...

    def ScrollUp(self) -> int:
        """ ScrollUp(self: IVsIntellisenseLangTip) -> int """
        ...

    def Update(self):
        """ no doc """
        ...

    def UpdatePosition(self) -> int:
        """ UpdatePosition(self: IVsIntellisenseLangTip) -> int """
        ...


class IVsIntellisenseOptions: # skipped bases: <type 'object'>
    """ no doc """
    def GetCompletorSize(self, uSize) -> Tuple_[int, int]:
        """ GetCompletorSize(self: IVsIntellisenseOptions) -> (int, int) """
        ...

    def SetCompletorSize(self, uSize:int) -> int:
        """ SetCompletorSize(self: IVsIntellisenseOptions, uSize: int) -> int """
        ...


class IVsLanguageClipboardOpsEx: # skipped bases: <type 'object'>
    """ no doc """
    def IsTextDataEx(self):
        """ no doc """
        ...


class IVsLanguageDebugInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def QueryCatchLineSpan(self):
        """ no doc """
        ...

    def QueryCommonLanguageBlock(self):
        """ no doc """
        ...

    def ValidateInstructionpointLocation(self):
        """ no doc """
        ...


class IVsLanguageDragDropOps: # skipped bases: <type 'object'>
    """ no doc """
    def DragCleanup(self):
        """ no doc """
        ...

    def DragSetup(self):
        """ no doc """
        ...

    def IsTextDataAtLocation(self):
        """ no doc """
        ...


class IVsLanguageLineIndent: # skipped bases: <type 'object'>
    """ no doc """
    def GetIndentPosition(self):
        """ no doc """
        ...


class IVsMethodDataEx: # skipped bases: <type 'object'>
    """ no doc """
    def GetCopyTipText(self, iMethod, pbstrTipText) -> Tuple_[int, str]:
        """ GetCopyTipText(self: IVsMethodDataEx, iMethod: int) -> (int, str) """
        ...


class IVsMethodTipWindow2: # skipped bases: <type 'object'>
    """ no doc """
    def GetOverloadCount(self, piCount:int) -> Tuple_[int, int]:
        """ GetOverloadCount(self: IVsMethodTipWindow2, piCount: int) -> (int, int) """
        ...

    def NextMethod(self, pfSuccess) -> Tuple_[int, int]:
        """ NextMethod(self: IVsMethodTipWindow2) -> (int, int) """
        ...

    def PrevMethod(self, pfSuccess) -> Tuple_[int, int]:
        """ PrevMethod(self: IVsMethodTipWindow2) -> (int, int) """
        ...


class IVsOverrideTextViewAccessibilityState: # skipped bases: <type 'object'>
    """ no doc """
    def GetOverrides(self, pdwMask, pdwFlags) -> Tuple_[int, UInt32, UInt32]:
        """ GetOverrides(self: IVsOverrideTextViewAccessibilityState) -> (int, UInt32, UInt32) """
        ...


class IVsQueryUndoManager: # skipped bases: <type 'object'>
    """ no doc """
    def IsLinkedTransactionOpen(self, pbTransactionIsOpen) -> Tuple_[int, int]:
        """ IsLinkedTransactionOpen(self: IVsQueryUndoManager) -> (int, int) """
        ...


class IVsQueryUndoUnit: # skipped bases: <type 'object'>
    """ no doc """
    def ActionWouldBeAborted(self, pbWouldBeAborted) -> Tuple_[int, int]:
        """ ActionWouldBeAborted(self: IVsQueryUndoUnit) -> (int, int) """
        ...


class IVsReadOnlyViewNotification: # skipped bases: <type 'object'>
    """ no doc """
    def OnDisabledEditingCommand(self, pguidCmdGuid:Guid, dwCmdId:UInt32) -> Tuple_[int, Guid]:
        """ OnDisabledEditingCommand(self: IVsReadOnlyViewNotification, pguidCmdGuid: Guid, dwCmdId: UInt32) -> (int, Guid) """
        ...


class IVsReportExternalErrors: # skipped bases: <type 'object'>
    """ no doc """
    def AddNewErrors(self, pErrors:IVsEnumExternalErrors) -> int:
        """ AddNewErrors(self: IVsReportExternalErrors, pErrors: IVsEnumExternalErrors) -> int """
        ...

    def ClearAllErrors(self) -> int:
        """ ClearAllErrors(self: IVsReportExternalErrors) -> int """
        ...

    def GetErrors(self, pErrors) -> Tuple_[int, IVsEnumExternalErrors]:
        """ GetErrors(self: IVsReportExternalErrors) -> (int, IVsEnumExternalErrors) """
        ...


class IVsSetSpanMappingEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnBeginSetSpanMappings(self):
        """ no doc """
        ...

    def OnEndSetSpanMappings(self) -> int:
        """ OnEndSetSpanMappings(self: IVsSetSpanMappingEvents) -> int """
        ...

    def OnMarkerInvalidated(self):
        """ no doc """
        ...


class IVsSmartTagData: # skipped bases: <type 'object'>
    """ no doc """
    def GetContextMenuInfo(self):
        """ no doc """
        ...

    def GetContextStream(self, piPos, piLength) -> Tuple_[int, int, int]:
        """ GetContextStream(self: IVsSmartTagData) -> (int, int, int) """
        ...

    def GetImageIndex(self, piIndex) -> Tuple_[int, int]:
        """ GetImageIndex(self: IVsSmartTagData) -> (int, int) """
        ...

    def GetTimerInterval(self, piTime) -> Tuple_[int, int]:
        """ GetTimerInterval(self: IVsSmartTagData) -> (int, int) """
        ...

    def GetTipText(self, pbstrTipText) -> Tuple_[int, str]:
        """ GetTipText(self: IVsSmartTagData) -> (int, str) """
        ...

    def IsLeftJustified(self, pfIsLeftJustified) -> Tuple_[int, int]:
        """ IsLeftJustified(self: IVsSmartTagData) -> (int, int) """
        ...

    def OnDismiss(self) -> int:
        """ OnDismiss(self: IVsSmartTagData) -> int """
        ...

    def OnInvocation(self) -> int:
        """ OnInvocation(self: IVsSmartTagData) -> int """
        ...

    def UpdateView(self) -> int:
        """ UpdateView(self: IVsSmartTagData) -> int """
        ...


class IVsSmartTagTipWindow: # skipped bases: <type 'object'>
    """ no doc """
    def Dismiss(self) -> int:
        """ Dismiss(self: IVsSmartTagTipWindow) -> int """
        ...

    def GetContextStream(self, piPos, piLength) -> Tuple_[int, int, int]:
        """ GetContextStream(self: IVsSmartTagTipWindow) -> (int, int, int) """
        ...

    def GetSizePreferences(self):
        """ no doc """
        ...

    def Paint(self):
        """ no doc """
        ...

    def SetSmartTagData(self, pSmartTagData:IVsSmartTagData) -> int:
        """ SetSmartTagData(self: IVsSmartTagTipWindow, pSmartTagData: IVsSmartTagData) -> int """
        ...

    def WndProc(self, hwnd:IntPtr, iMsg:UInt32, wParam:IntPtr, lParam:IntPtr, pLResult:int) -> Tuple_[int, int]:
        """ WndProc(self: IVsSmartTagTipWindow, hwnd: IntPtr, iMsg: UInt32, wParam: IntPtr, lParam: IntPtr, pLResult: int) -> (int, int) """
        ...


class IVsTextBufferEx: # skipped bases: <type 'object'>
    """ no doc """
    def GetTrackChanges(self, pfIsTracking) -> Tuple_[int, int]:
        """ GetTrackChanges(self: IVsTextBufferEx) -> (int, int) """
        ...

    def SetTrackChangesSuppression(self, fSupress:int) -> int:
        """ SetTrackChangesSuppression(self: IVsTextBufferEx, fSupress: int) -> int """
        ...


class IVsTextImage2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEolLengthEx(self):
        """ no doc """
        ...

    def GetEolTextEx(self):
        """ no doc """
        ...

    def GetEolTypeEx(self):
        """ no doc """
        ...


class IVsTextLayer2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEolLengthEx(self):
        """ no doc """
        ...

    def GetEolTextEx(self):
        """ no doc """
        ...

    def GetEolTypeEx(self):
        """ no doc """
        ...


class IVsTextLineMarkerEx: # skipped bases: <type 'object'>
    """ no doc """
    def GetClientData(self, pdwData) -> Tuple_[int, UInt32]:
        """ GetClientData(self: IVsTextLineMarkerEx) -> (int, UInt32) """
        ...

    def SetClientData(self, dwData:UInt32) -> int:
        """ SetClientData(self: IVsTextLineMarkerEx, dwData: UInt32) -> int """
        ...


class IVsTextLines2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEolLengthEx(self):
        """ no doc """
        ...

    def GetEolTextEx(self):
        """ no doc """
        ...

    def GetEolTypeEx(self):
        """ no doc """
        ...


class IVsTextManager2: # skipped bases: <type 'object'>
    """ no doc """
    def AttemptToCheckOutBufferFromScc3(self):
        """ no doc """
        ...

    def FireReplaceAllInFilesBegin(self) -> int:
        """ FireReplaceAllInFilesBegin(self: IVsTextManager2) -> int """
        ...

    def FireReplaceAllInFilesEnd(self) -> int:
        """ FireReplaceAllInFilesEnd(self: IVsTextManager2) -> int """
        ...

    def GetActiveView2(self):
        """ no doc """
        ...

    def GetBufferSccStatus3(self):
        """ no doc """
        ...

    def GetExpansionManager(self, pExpansionManager) -> Tuple_[int, IVsExpansionManager]:
        """ GetExpansionManager(self: IVsTextManager2) -> (int, IVsExpansionManager) """
        ...

    def GetUserPreferences2(self):
        """ no doc """
        ...

    def NavigateToLineAndColumn2(self):
        """ no doc """
        ...

    def NavigateToPosition2(self):
        """ no doc """
        ...

    def ResetColorableItems(self, guidLang:Guid) -> int:
        """ ResetColorableItems(self: IVsTextManager2, guidLang: Guid) -> int """
        ...

    def SetUserPreferences2(self):
        """ no doc """
        ...


class IVsTextManagerEvents2: # skipped bases: <type 'object'>
    """ no doc """
    def OnRegisterMarkerType(self, iMarkerType:int) -> int:
        """ OnRegisterMarkerType(self: IVsTextManagerEvents2, iMarkerType: int) -> int """
        ...

    def OnRegisterView(self):
        """ no doc """
        ...

    def OnReplaceAllInFilesBegin(self) -> int:
        """ OnReplaceAllInFilesBegin(self: IVsTextManagerEvents2) -> int """
        ...

    def OnReplaceAllInFilesEnd(self) -> int:
        """ OnReplaceAllInFilesEnd(self: IVsTextManagerEvents2) -> int """
        ...

    def OnUnregisterView(self):
        """ no doc """
        ...

    def OnUserPreferencesChanged2(self):
        """ no doc """
        ...


class IVsTextMarkerClientAdvanced: # skipped bases: <type 'object'>
    """ no doc """
    def OnMarkerTextChanged(self):
        """ no doc """
        ...


class IVsTextMarkerClientEx: # skipped bases: <type 'object'>
    """ no doc """
    def MarkerInvalidated(self):
        """ no doc """
        ...

    def OnHoverOverMarker(self):
        """ no doc """
        ...


class IVsTextStorage2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEolLengthEx(self):
        """ no doc """
        ...

    def GetEolTextEx(self):
        """ no doc """
        ...

    def GetEolTypeEx(self):
        """ no doc """
        ...

    def GetVersionCookie(self, pdwVersionCookie) -> Tuple_[int, UInt32]:
        """ GetVersionCookie(self: IVsTextStorage2) -> (int, UInt32) """
        ...


class IVsTextViewEx: # skipped bases: <type 'object'>
    """ no doc """
    def AppendViewOnlyMarkerTypes(self, iCountViewMarkerOnly:UInt32, rgViewMarkerOnly:Array) -> int:
        """ AppendViewOnlyMarkerTypes(self: IVsTextViewEx, iCountViewMarkerOnly: UInt32, rgViewMarkerOnly: Array[UInt32]) -> int """
        ...

    def GetClusterRange(self, iLine, iDisplayCol, picCharacter, piStartCol, piEndCol) -> Tuple_[int, int, int, int]:
        """ GetClusterRange(self: IVsTextViewEx, iLine: int, iDisplayCol: int) -> (int, int, int, int) """
        ...

    def GetSmartTagRect(self):
        """ no doc """
        ...

    def GetWindowFrame(self, ppFrame) -> Tuple_[int, object]:
        """ GetWindowFrame(self: IVsTextViewEx) -> (int, object) """
        ...

    def InvokeInsertionUI(self):
        """ no doc """
        ...

    def IsCompletorWindowActive(self) -> int:
        """ IsCompletorWindowActive(self: IVsTextViewEx) -> int """
        ...

    def IsExpansionUIActive(self) -> int:
        """ IsExpansionUIActive(self: IVsTextViewEx) -> int """
        ...

    def IsReadOnly(self) -> int:
        """ IsReadOnly(self: IVsTextViewEx) -> int """
        ...

    def PersistOutliningState(self) -> int:
        """ PersistOutliningState(self: IVsTextViewEx) -> int """
        ...

    def RemoveViewOnlyMarkerTypes(self, iCountViewMarkerOnly:UInt32, rgViewMarkerOnly:Array) -> int:
        """ RemoveViewOnlyMarkerTypes(self: IVsTextViewEx, iCountViewMarkerOnly: UInt32, rgViewMarkerOnly: Array[UInt32]) -> int """
        ...

    def SetBackgroundColorIndex(self, iBackgroundIndex:int) -> int:
        """ SetBackgroundColorIndex(self: IVsTextViewEx, iBackgroundIndex: int) -> int """
        ...

    def SetHoverWaitTimer(self) -> int:
        """ SetHoverWaitTimer(self: IVsTextViewEx) -> int """
        ...

    def SetIgnoreMarkerTypes(self, iCountMarkerTypes:int, rgIgnoreMarkerTypes:Array) -> int:
        """ SetIgnoreMarkerTypes(self: IVsTextViewEx, iCountMarkerTypes: int, rgIgnoreMarkerTypes: Array[UInt32]) -> int """
        ...

    def UpdateSmartTagWindow(self, pSmartTagWnd:IVsSmartTagTipWindow, dwFlags:UInt32) -> int:
        """ UpdateSmartTagWindow(self: IVsTextViewEx, pSmartTagWnd: IVsSmartTagTipWindow, dwFlags: UInt32) -> int """
        ...


class IVsTextViewIntellisenseHostProvider: # skipped bases: <type 'object'>
    """ no doc """
    def CreateIntellisenseHost(self):
        """ no doc """
        ...


class IVsWebFormDesignerSupport: # skipped bases: <type 'object'>
    """ no doc """
    def AddReference(self, pszReference:str) -> int:
        """ AddReference(self: IVsWebFormDesignerSupport, pszReference: str) -> int """
        ...

    def GetCodeDomProvider(self, ppProvider) -> Tuple_[int, object]:
        """ GetCodeDomProvider(self: IVsWebFormDesignerSupport) -> (int, object) """
        ...


class LINESTYLE2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LINESTYLE2, values: LI_SMARTTAGEPHEM (7), LI_SMARTTAGEPHEMSIDE (8), LI_SMARTTAGFACT (5), LI_SMARTTAGFACTSIDE (6) """
    LI_SMARTTAGEPHEM: LINESTYLE2 = ...
    LI_SMARTTAGEPHEMSIDE: LINESTYLE2 = ...
    LI_SMARTTAGFACT: LINESTYLE2 = ...
    LI_SMARTTAGFACTSIDE: LINESTYLE2 = ...
    value__ = ...


class LinkedTransactionFlags2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LinkedTransactionFlags2, values: mdtGlobal (2) """
    mdtGlobal: LinkedTransactionFlags2 = ...
    value__ = ...


class MARKERBEHAVIORFLAGS2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MARKERBEHAVIORFLAGS2, values: MB_DONT_DELETE_IF_ZEROLEN (16), MB_INHERIT_BACKGROUND (64), MB_INHERIT_FOREGROUND (32), MB_VIEW_SPECIFIC (128) """
    MB_DONT_DELETE_IF_ZEROLEN: MARKERBEHAVIORFLAGS2 = ...
    MB_INHERIT_BACKGROUND: MARKERBEHAVIORFLAGS2 = ...
    MB_INHERIT_FOREGROUND: MARKERBEHAVIORFLAGS2 = ...
    MB_VIEW_SPECIFIC: MARKERBEHAVIORFLAGS2 = ...
    value__ = ...


class MarkerCommandValues2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MarkerCommandValues2, values: mcvRightClickCommand (260) """
    mcvRightClickCommand: MarkerCommandValues2 = ...
    value__ = ...


class MARKERTYPE2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MARKERTYPE2, values: DEF_MARKER_COUNT_NEW (35), MARKER_BOOKMARK_DISABLED (21), MARKER_BRACE_MATCHING (25), MARKER_BRACE_MATCHING_BOLD (30), MARKER_CODEDEFWIN_BACKGROUND (27), MARKER_CODEDEFWIN_SELECTION (28), MARKER_EXSTENCIL (15), MARKER_EXSTENCIL_DEPFIELD (32), MARKER_EXSTENCIL_ENDMARKER (26), MARKER_EXSTENCIL_SELECTED (16), MARKER_HIGHLIGHT_PATH (29), MARKER_REFACTORING_BACKGROUND (31), MARKER_REFACTORING_DEPFIELD (34), MARKER_REFACTORING_FIELD (33), MARKER_REGION_COLLAPSED_NOGLYPH (13), MARKER_REGION_EXPANDED_NOGLYPH (14), MARKER_SMARTTAG_EPHEMERAL (24), MARKER_SMARTTAG_FACTOID (23), MARKER_SMARTTAG_NONVIS (17), MARKER_SMARTTAG_VIS (18), MARKER_SPAN_MAPPING (12), MARKER_TRACK_NONSAVE (19), MARKER_TRACK_PLACEHOLDER (22), MARKER_TRACK_SAVE (20), MARKER_WARNING (11) """
    DEF_MARKER_COUNT_NEW: MARKERTYPE2 = ...
    MARKER_BOOKMARK_DISABLED: MARKERTYPE2 = ...
    MARKER_BRACE_MATCHING: MARKERTYPE2 = ...
    MARKER_BRACE_MATCHING_BOLD: MARKERTYPE2 = ...
    MARKER_CODEDEFWIN_BACKGROUND: MARKERTYPE2 = ...
    MARKER_CODEDEFWIN_SELECTION: MARKERTYPE2 = ...
    MARKER_EXSTENCIL: MARKERTYPE2 = ...
    MARKER_EXSTENCIL_DEPFIELD: MARKERTYPE2 = ...
    MARKER_EXSTENCIL_ENDMARKER: MARKERTYPE2 = ...
    MARKER_EXSTENCIL_SELECTED: MARKERTYPE2 = ...
    MARKER_HIGHLIGHT_PATH: MARKERTYPE2 = ...
    MARKER_REFACTORING_BACKGROUND: MARKERTYPE2 = ...
    MARKER_REFACTORING_DEPFIELD: MARKERTYPE2 = ...
    MARKER_REFACTORING_FIELD: MARKERTYPE2 = ...
    MARKER_REGION_COLLAPSED_NOGLYPH: MARKERTYPE2 = ...
    MARKER_REGION_EXPANDED_NOGLYPH: MARKERTYPE2 = ...
    MARKER_SMARTTAG_EPHEMERAL: MARKERTYPE2 = ...
    MARKER_SMARTTAG_FACTOID: MARKERTYPE2 = ...
    MARKER_SMARTTAG_NONVIS: MARKERTYPE2 = ...
    MARKER_SMARTTAG_VIS: MARKERTYPE2 = ...
    MARKER_SPAN_MAPPING: MARKERTYPE2 = ...
    MARKER_TRACK_NONSAVE: MARKERTYPE2 = ...
    MARKER_TRACK_PLACEHOLDER: MARKERTYPE2 = ...
    MARKER_TRACK_SAVE: MARKERTYPE2 = ...
    MARKER_WARNING: MARKERTYPE2 = ...
    value__ = ...


class MARKERVISUAL2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MARKERVISUAL2, values: MV_BOLDTEXT (131072), MV_DISALLOWBGCHANGE (262144), MV_DISALLOWFGCHANGE (524288), MV_FORCE_CLOSEST_IF_HIDDEN (1048576), MV_ROUNDEDBORDER (65536), MV_SELECT_WHOLE_LINE (2097152), MV_SMARTTAG (16384), MV_TRACK (32768) """
    MV_BOLDTEXT: MARKERVISUAL2 = ...
    MV_DISALLOWBGCHANGE: MARKERVISUAL2 = ...
    MV_DISALLOWFGCHANGE: MARKERVISUAL2 = ...
    MV_FORCE_CLOSEST_IF_HIDDEN: MARKERVISUAL2 = ...
    MV_ROUNDEDBORDER: MARKERVISUAL2 = ...
    MV_SELECT_WHOLE_LINE: MARKERVISUAL2 = ...
    MV_SMARTTAG: MARKERVISUAL2 = ...
    MV_TRACK: MARKERVISUAL2 = ...
    value__ = ...


class ST_IMAGEINDEX(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ST_IMAGEINDEX, values: ST_DEFAULTIMAGE (0), ST_ERROR (1), ST_REFACTOR (2) """
    ST_DEFAULTIMAGE: ST_IMAGEINDEX = ...
    ST_ERROR: ST_IMAGEINDEX = ...
    ST_REFACTOR: ST_IMAGEINDEX = ...
    value__ = ...


class SVsRegisterFindScope: # skipped bases: <type 'object'>
    """ no doc """
    pass

class SVsTextImageUtilities: # skipped bases: <type 'object'>
    """ no doc """
    pass

class SVsTextSpanSet: # skipped bases: <type 'object'>
    """ no doc """
    pass

class TextBufferErrors2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextBufferErrors2, values: BUFFER_E_RELOAD_OCCURRED (-2147217399) """
    BUFFER_E_RELOAD_OCCURRED: TextBufferErrors2 = ...
    value__ = ...


class TextViewInitFlags2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TextViewInitFlags2, values: VIF_ACTIVEINMODALSTATE (1024), VIF_READONLY (512), VIF_SUPPRESS_STATUS_BAR_UPDATE (2048), VIF_SUPPRESSBORDER (8192), VIF_SUPPRESSTRACKCHANGES (4096), VIF_SUPPRESSTRACKGOBACK (16384) """
    value__ = ...
    VIF_ACTIVEINMODALSTATE: TextViewInitFlags2 = ...
    VIF_READONLY: TextViewInitFlags2 = ...
    VIF_SUPPRESSBORDER: TextViewInitFlags2 = ...
    VIF_SUPPRESSTRACKCHANGES: TextViewInitFlags2 = ...
    VIF_SUPPRESSTRACKGOBACK: TextViewInitFlags2 = ...
    VIF_SUPPRESS_STATUS_BAR_UPDATE: TextViewInitFlags2 = ...


class TipSuccesses2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TipSuccesses2, values: TIP_S_NODEFAULTTIP (282625) """
    TIP_S_NODEFAULTTIP: TipSuccesses2 = ...
    value__ = ...


class TipWindowFlags2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TipWindowFlags2, values: UTW_EXPANDED (16), UTW_TIMER (8) """
    UTW_EXPANDED: TipWindowFlags2 = ...
    UTW_TIMER: TipWindowFlags2 = ...
    value__ = ...


class VIEWPREFERENCES2: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    fActiveInModalState = ...
    fAutoDelimiterHighlight = ...
    fClientDragDropFeedback = ...
    fDetectUTF8 = ...
    fDragDropEditing = ...
    fDragDropMove = ...
    fGoToAnchorAfterEscape = ...
    fOvertype = ...
    fReadOnly = ...
    fSelectionMargin = ...
    fTrackChanges = ...
    fUndoCaretMovements = ...
    fVisibleWhitespace = ...
    fWidgetMargin = ...
    lEditorEmulation = ...
    uCompletorSize = ...


class VsExpansion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    description = ...
    path = ...
    shortcut = ...
    title = ...


class VsExpansionManager(IVsExpansionManager): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsExpansionManagerClass(VsExpansionManager, __ComObject): # skipped bases: <type 'IVsExpansionManager'>, <type 'object'>
    """ VsExpansionManagerClass() """
    def EnumerateExpansions(self, guidLang, fShortCutOnly, bstrTypes, iCountTypes, fIncludeNULLType, fIncludeDuplicates, pEnum) -> Tuple_[int, IVsExpansionEnumeration]:
        """ EnumerateExpansions(self: VsExpansionManagerClass, guidLang: Guid, fShortCutOnly: int, bstrTypes: Array[str], iCountTypes: int, fIncludeNULLType: int, fIncludeDuplicates: int) -> (int, IVsExpansionEnumeration) """
        ...

    def GetExpansionByShortcut(self):
        """ no doc """
        ...

    def GetSnippetShortCutKeybindingState(self, fBound) -> Tuple_[int, int]:
        """ GetSnippetShortCutKeybindingState(self: VsExpansionManagerClass) -> (int, int) """
        ...

    def GetTokenPath(self, token, pbstrPath) -> Tuple_[int, str]:
        """ GetTokenPath(self: VsExpansionManagerClass, token: UInt32) -> (int, str) """
        ...

    def InvokeInsertionUI(self):
        """ no doc """
        ...


class VsExpansionPackage(IVsExpansionManager): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsExpansionPackageClass(__ComObject, VsExpansionPackage): # skipped bases: <type 'IVsExpansionManager'>, <type 'object'>
    """ VsExpansionPackageClass() """
    def EnumerateExpansions(self, guidLang, fShortCutOnly, bstrTypes, iCountTypes, fIncludeNULLType, fIncludeDuplicates, pEnum) -> Tuple_[int, IVsExpansionEnumeration]:
        """ EnumerateExpansions(self: VsExpansionPackageClass, guidLang: Guid, fShortCutOnly: int, bstrTypes: Array[str], iCountTypes: int, fIncludeNULLType: int, fIncludeDuplicates: int) -> (int, IVsExpansionEnumeration) """
        ...

    def GetExpansionByShortcut(self):
        """ no doc """
        ...

    def GetSnippetShortCutKeybindingState(self, fBound) -> Tuple_[int, int]:
        """ GetSnippetShortCutKeybindingState(self: VsExpansionPackageClass) -> (int, int) """
        ...

    def GetTokenPath(self, token, pbstrPath) -> Tuple_[int, str]:
        """ GetTokenPath(self: VsExpansionPackageClass, token: UInt32) -> (int, str) """
        ...

    def InvokeInsertionUI(self):
        """ no doc """
        ...


class VSFINDERROR2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VSFINDERROR2, values: VSFE_NoErrorAnsiPattern (1) """
    value__ = ...
    VSFE_NoErrorAnsiPattern: VSFINDERROR2 = ...


class VsIntellisenseLangTip(IVsIntellisenseLangTip): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsIntellisenseLangTipClass(VsIntellisenseLangTip, __ComObject): # skipped bases: <type 'IVsIntellisenseLangTip'>, <type 'object'>
    """ VsIntellisenseLangTipClass() """
    def Close(self, fDeleteThis:int) -> int:
        """ Close(self: VsIntellisenseLangTipClass, fDeleteThis: int) -> int """
        ...

    def Create(self):
        """ no doc """
        ...

    def GetOverloadCount(self, plOverloadCount) -> Tuple_[int, int]:
        """ GetOverloadCount(self: VsIntellisenseLangTipClass) -> (int, int) """
        ...

    def GetSizePreferences(self):
        """ no doc """
        ...

    def GetSizeY(self, pSizeY) -> Tuple_[int, Int16]:
        """ GetSizeY(self: VsIntellisenseLangTipClass) -> (int, Int16) """
        ...

    def Initialize(self):
        """ no doc """
        ...

    def IsActive(self, pfIsActive) -> Tuple_[int, int]:
        """ IsActive(self: VsIntellisenseLangTipClass) -> (int, int) """
        ...

    def ScrollDown(self) -> int:
        """ ScrollDown(self: VsIntellisenseLangTipClass) -> int """
        ...

    def ScrollUp(self) -> int:
        """ ScrollUp(self: VsIntellisenseLangTipClass) -> int """
        ...

    def Update(self):
        """ no doc """
        ...

    def UpdatePosition(self) -> int:
        """ UpdatePosition(self: VsIntellisenseLangTipClass) -> int """
        ...


class VsSmartTagTipWindow(IVsSmartTagTipWindow): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsSmartTagTipWindowClass(VsSmartTagTipWindow, __ComObject): # skipped bases: <type 'IVsSmartTagTipWindow'>, <type 'object'>
    """ VsSmartTagTipWindowClass() """
    def Dismiss(self) -> int:
        """ Dismiss(self: VsSmartTagTipWindowClass) -> int """
        ...

    def GetContextStream(self, piPos, piLength) -> Tuple_[int, int, int]:
        """ GetContextStream(self: VsSmartTagTipWindowClass) -> (int, int, int) """
        ...

    def GetSizePreferences(self):
        """ no doc """
        ...

    def Paint(self):
        """ no doc """
        ...

    def SetSmartTagData(self, pSmartTagData:IVsSmartTagData) -> int:
        """ SetSmartTagData(self: VsSmartTagTipWindowClass, pSmartTagData: IVsSmartTagData) -> int """
        ...

    def WndProc(self, hwnd:IntPtr, iMsg:UInt32, wParam:IntPtr, lParam:IntPtr, pLResult:int) -> Tuple_[int, int]:
        """ WndProc(self: VsSmartTagTipWindowClass, hwnd: IntPtr, iMsg: UInt32, wParam: IntPtr, lParam: IntPtr, pLResult: int) -> (int, int) """
        ...


class VSTFF2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VSTFF2, values: VSTFF_KEEPANSI (536870912), VSTFF_NOUTF8_NOSIG (268435456) """
    value__ = ...
    VSTFF_KEEPANSI: VSTFF2 = ...
    VSTFF_NOUTF8_NOSIG: VSTFF2 = ...


class _BufferCoordinatorMappingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _BufferCoordinatorMappingMode, values: BCMM_ENTIREBUFFER (4), BCMM_EXTENDED (3), BCMM_EXTENDEDLEFT (2), BCMM_EXTENDEDRIGHT (1), BCMM_NORMAL (0) """
    BCMM_ENTIREBUFFER: _BufferCoordinatorMappingMode = ...
    BCMM_EXTENDED: _BufferCoordinatorMappingMode = ...
    BCMM_EXTENDEDLEFT: _BufferCoordinatorMappingMode = ...
    BCMM_EXTENDEDRIGHT: _BufferCoordinatorMappingMode = ...
    BCMM_NORMAL: _BufferCoordinatorMappingMode = ...
    value__ = ...


class _codewindowbehaviorflags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) _codewindowbehaviorflags, values: CWB_DEFAULT (0), CWB_DISABLEDROPDOWNBAR (1), CWB_DISABLESPLITTER (2) """
    CWB_DEFAULT: _codewindowbehaviorflags = ...
    CWB_DISABLEDROPDOWNBAR: _codewindowbehaviorflags = ...
    CWB_DISABLESPLITTER: _codewindowbehaviorflags = ...
    value__ = ...


class _EOLTYPE2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _EOLTYPE2, values: eolUNI_NEL (7), MAX_EOLTYPES2 (8) """
    eolUNI_NEL: _EOLTYPE2 = ...
    MAX_EOLTYPES2: _EOLTYPE2 = ...
    value__ = ...


class _ExpansionFunctionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _ExpansionFunctionType, values: eft_List (0), eft_Value (1) """
    eft_List: _ExpansionFunctionType = ...
    eft_Value: _ExpansionFunctionType = ...
    value__ = ...


class _ExpansionToken(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _ExpansionToken, values: ET_InstallRoot (2), ET_MyDocs (1) """
    ET_InstallRoot: _ExpansionToken = ...
    ET_MyDocs: _ExpansionToken = ...
    value__ = ...


class _HighlightMatchingBraceFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) _HighlightMatchingBraceFlags, values: HMB_SUPPRESS_STATUS_BAR_UPDATE (1), HMB_USERECTANGLEBRACES (2) """
    HMB_SUPPRESS_STATUS_BAR_UPDATE: _HighlightMatchingBraceFlags = ...
    HMB_USERECTANGLEBRACES: _HighlightMatchingBraceFlags = ...
    value__ = ...


class _VIEWFRAMETYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _VIEWFRAMETYPE, values: vftAny (0), vftCodeWindow (1), vftToolWindow (2) """
    value__ = ...
    vftAny: _VIEWFRAMETYPE = ...
    vftCodeWindow: _VIEWFRAMETYPE = ...
    vftToolWindow: _VIEWFRAMETYPE = ...


class __tagVSCOLORDATA(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __tagVSCOLORDATA, values: CD_BACKGROUND (1), CD_FOREGROUND (0), CD_LINECOLOR (2) """
    CD_BACKGROUND: __tagVSCOLORDATA = ...
    CD_FOREGROUND: __tagVSCOLORDATA = ...
    CD_LINECOLOR: __tagVSCOLORDATA = ...
    value__ = ...


class __VSEDITPROPID2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __VSEDITPROPID2, values: VSEDITPROPID_ViewGeneral_AccessibilityStateOverride (-73735) """
    value__ = ...
    VSEDITPROPID_ViewGeneral_AccessibilityStateOverride: __VSEDITPROPID2 = ...


class __VSFINDOPTIONS2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __VSFINDOPTIONS2, values: FR_BlockThread (536870912), FR_DoNotUpdateUI (1073741824), FR_RegExprLineBreaks (16384) """
    FR_BlockThread: __VSFINDOPTIONS2 = ...
    FR_DoNotUpdateUI: __VSFINDOPTIONS2 = ...
    FR_RegExprLineBreaks: __VSFINDOPTIONS2 = ...
    value__ = ...


class __VSFINDRESULT2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __VSFINDRESULT2, values: VSFR_CancelledBeforeReplacementsMade (536870912), VSFR_ReplaceIncompleteEOL (268435456) """
    value__ = ...
    VSFR_CancelledBeforeReplacementsMade: __VSFINDRESULT2 = ...
    VSFR_ReplaceIncompleteEOL: __VSFINDRESULT2 = ...


class __VSFTPROPID2(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __VSFTPROPID2, values: VSFTPROPID_IsFindInFilesForegroundOnly (6) """
    value__ = ...
    VSFTPROPID_IsFindInFilesForegroundOnly: __VSFTPROPID2 = ...


