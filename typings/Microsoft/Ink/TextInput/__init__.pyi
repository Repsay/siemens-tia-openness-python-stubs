# encoding: utf-8
# module Microsoft.Ink.TextInput calls itself TextInput
# from Microsoft.Ink, Version=6.1.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Ink import RecognitionResult

from System import Array, Enum, EventArgs, IDisposable, IntPtr

from System.Drawing import Rectangle

from System.Globalization import CultureInfo

from System.Web.UI import Control

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CorrectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CorrectionMode, values: NotVisible (0), PostInsertionCollapsed (2), PostInsertionExpanded (3), PreInsertion (1) """
    NotVisible: CorrectionMode = ...
    PostInsertionCollapsed: CorrectionMode = ...
    PostInsertionExpanded: CorrectionMode = ...
    PreInsertion: CorrectionMode = ...
    value__ = ...


class CorrectionModeChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CorrectionModeChangeEventArgs(oldMode: CorrectionMode, newMode: CorrectionMode) """
    @property
    def NewMode(self) -> CorrectionMode:
        """ Get: NewMode(self: CorrectionModeChangeEventArgs) -> CorrectionMode """
        ...

    @property
    def OldMode(self) -> CorrectionMode:
        """ Get: OldMode(self: CorrectionModeChangeEventArgs) -> CorrectionMode """
        ...


    def __new__(cls, oldMode:CorrectionMode, newMode:CorrectionMode) -> Self:
        """ __new__(cls: type, oldMode: CorrectionMode, newMode: CorrectionMode) """
        ...


class CorrectionPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CorrectionPosition, values: Auto (0), Bottom (1), Top (2) """
    Auto: CorrectionPosition = ...
    Bottom: CorrectionPosition = ...
    Top: CorrectionPosition = ...
    value__ = ...


class HandwrittenTextInsertion: # skipped bases: <type 'object'>, <type 'object'>
    """ HandwrittenTextInsertion() """
    def InsertInkRecognitionResult(self, recognitionResult:RecognitionResult, culture:CultureInfo, alternateContainsAutoSpacingInformation:bool): # -> 
        """ InsertInkRecognitionResult(self: HandwrittenTextInsertion, recognitionResult: RecognitionResult, culture: CultureInfo, alternateContainsAutoSpacingInformation: bool) """
        ...

    def InsertRecognitionResultsArray(self, alternates:Array, culture:CultureInfo, alternateContainsAutoSpacingInformation:bool): # -> 
        """ InsertRecognitionResultsArray(self: HandwrittenTextInsertion, alternates: Array[Array[str]], culture: CultureInfo, alternateContainsAutoSpacingInformation: bool) """
        ...


class InPlaceDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InPlaceDirection, values: Auto (0), Bottom (1), Top (2) """
    Auto: InPlaceDirection = ...
    Bottom: InPlaceDirection = ...
    Top: InPlaceDirection = ...
    value__ = ...


class InPlaceSizeChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InPlaceSizeChangeEventArgs(oldSize: Rectangle, newSize: Rectangle) """
    @property
    def NewSize(self) -> Rectangle:
        """ Get: NewSize(self: InPlaceSizeChangeEventArgs) -> Rectangle """
        ...

    @property
    def OldSize(self) -> Rectangle:
        """ Get: OldSize(self: InPlaceSizeChangeEventArgs) -> Rectangle """
        ...


    def __new__(cls, oldSize:Rectangle, newSize:Rectangle) -> Self:
        """ __new__(cls: type, oldSize: Rectangle, newSize: Rectangle) """
        ...


class InPlaceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InPlaceState, values: Auto (0), Expanded (2), HoverTarget (1) """
    Auto: InPlaceState = ...
    Expanded: InPlaceState = ...
    HoverTarget: InPlaceState = ...
    value__ = ...


class InPlaceStateChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InPlaceStateChangeEventArgs(oldState: InPlaceState, newState: InPlaceState) """
    @property
    def NewState(self) -> InPlaceState:
        """ Get: NewState(self: InPlaceStateChangeEventArgs) -> InPlaceState """
        ...

    @property
    def OldState(self) -> InPlaceState:
        """ Get: OldState(self: InPlaceStateChangeEventArgs) -> InPlaceState """
        ...


    def __new__(cls, oldState:InPlaceState, newState:InPlaceState) -> Self:
        """ __new__(cls: type, oldState: InPlaceState, newState: InPlaceState) """
        ...


class InPlaceVisibilityChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InPlaceVisibilityChangeEventArgs(visible: bool) """
    @property
    def Visible(self) -> bool:
        """ Get: Visible(self: InPlaceVisibilityChangeEventArgs) -> bool """
        ...


    def __new__(cls, visible:bool) -> Self:
        """ __new__(cls: type, visible: bool) """
        ...


class InputAreaChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InputAreaChangeEventArgs(oldArea: PanelInputArea, newArea: PanelInputArea) """
    @property
    def NewArea(self) -> PanelInputArea:
        """ Get: NewArea(self: InputAreaChangeEventArgs) -> PanelInputArea """
        ...

    @property
    def OldArea(self) -> PanelInputArea:
        """ Get: OldArea(self: InputAreaChangeEventArgs) -> PanelInputArea """
        ...


    def __new__(cls, oldArea:PanelInputArea, newArea:PanelInputArea) -> Self:
        """ __new__(cls: type, oldArea: PanelInputArea, newArea: PanelInputArea) """
        ...


class InteractionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InteractionMode, values: DockedBottom (3), DockedTop (2), Floating (1), InPlace (0) """
    DockedBottom: InteractionMode = ...
    DockedTop: InteractionMode = ...
    Floating: InteractionMode = ...
    InPlace: InteractionMode = ...
    value__ = ...


class PanelInputArea(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PanelInputArea, values: Auto (0), CharacterPad (3), Keyboard (1), WritingPad (2) """
    Auto: PanelInputArea = ...
    CharacterPad: PanelInputArea = ...
    Keyboard: PanelInputArea = ...
    value__ = ...
    WritingPad: PanelInputArea = ...


class TextInputPanel(IDisposable): # skipped bases: <type 'object'>
    """
    TextInputPanel()
    TextInputPanel(attachHandle: IntPtr)
    TextInputPanel(attachControl: Control)
    """
    @property
    def AttachedEditControl(self) -> Control:
        """
        Get: AttachedEditControl(self: TextInputPanel) -> Control
        Set: AttachedEditControl(self: TextInputPanel) = value
        """
        ...

    @property
    def AttachedEditWindow(self) -> IntPtr:
        """
        Get: AttachedEditWindow(self: TextInputPanel) -> IntPtr
        Set: AttachedEditWindow(self: TextInputPanel) = value
        """
        ...

    @property
    def CurrentCorrectionMode(self) -> CorrectionMode:
        """ Get: CurrentCorrectionMode(self: TextInputPanel) -> CorrectionMode """
        ...

    @property
    def CurrentInPlaceState(self) -> InPlaceState:
        """ Get: CurrentInPlaceState(self: TextInputPanel) -> InPlaceState """
        ...

    @property
    def CurrentInputArea(self) -> PanelInputArea:
        """ Get: CurrentInputArea(self: TextInputPanel) -> PanelInputArea """
        ...

    @property
    def CurrentInteractionMode(self) -> InteractionMode:
        """ Get: CurrentInteractionMode(self: TextInputPanel) -> InteractionMode """
        ...

    @property
    def DefaultInPlaceState(self) -> InPlaceState:
        """
        Get: DefaultInPlaceState(self: TextInputPanel) -> InPlaceState
        Set: DefaultInPlaceState(self: TextInputPanel) = value
        """
        ...

    @property
    def DefaultInputArea(self) -> PanelInputArea:
        """
        Get: DefaultInputArea(self: TextInputPanel) -> PanelInputArea
        Set: DefaultInputArea(self: TextInputPanel) = value
        """
        ...

    @property
    def ExpandPostInsertionCorrection(self) -> bool:
        """
        Get: ExpandPostInsertionCorrection(self: TextInputPanel) -> bool
        Set: ExpandPostInsertionCorrection(self: TextInputPanel) = value
        """
        ...

    @property
    def InPlaceBoundingRectangle(self) -> Rectangle:
        """ Get: InPlaceBoundingRectangle(self: TextInputPanel) -> Rectangle """
        ...

    @property
    def InPlaceVisibleOnFocus(self) -> bool:
        """
        Get: InPlaceVisibleOnFocus(self: TextInputPanel) -> bool
        Set: InPlaceVisibleOnFocus(self: TextInputPanel) = value
        """
        ...

    @property
    def PopDownCorrectionHeight(self) -> int:
        """ Get: PopDownCorrectionHeight(self: TextInputPanel) -> int """
        ...

    @property
    def PopUpCorrectionHeight(self) -> int:
        """ Get: PopUpCorrectionHeight(self: TextInputPanel) -> int """
        ...

    @property
    def PreferredInPlaceDirection(self) -> InPlaceDirection:
        """
        Get: PreferredInPlaceDirection(self: TextInputPanel) -> InPlaceDirection
        Set: PreferredInPlaceDirection(self: TextInputPanel) = value
        """
        ...


    def CommitPendingInput(self): # -> 
        """ CommitPendingInput(self: TextInputPanel) """
        ...

    def SetInPlaceHoverTargetPosition(self, x:int, y:int): # -> 
        """ SetInPlaceHoverTargetPosition(self: TextInputPanel, x: int, y: int) """
        ...

    def SetInPlacePosition(self, x:int, y:int, position:CorrectionPosition): # -> 
        """ SetInPlacePosition(self: TextInputPanel, x: int, y: int, position: CorrectionPosition) """
        ...

    def SetInPlaceVisibility(self, visible:bool): # -> 
        """ SetInPlaceVisibility(self: TextInputPanel, visible: bool) """
        ...

    CorrectionModeChanged = ...
    CorrectionModeChanging = ...
    InPlaceSizeChanged = ...
    InPlaceSizeChanging = ...
    InPlaceStateChanged = ...
    InPlaceStateChanging = ...
    InPlaceVisibilityChanged = ...
    InPlaceVisibilityChanging = ...
    InputAreaChanged = ...
    InputAreaChanging = ...
    TextInserted = ...
    TextInserting = ...


class TextInsertionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TextInsertionEventArgs(insertionInk: Array[Ink]) """
    def GetInk(self) -> Array:
        """ GetInk(self: TextInsertionEventArgs) -> Array[Ink] """
        ...

    def __new__(cls, insertionInk:Array) -> Self:
        """ __new__(cls: type, insertionInk: Array[Ink]) """
        ...


