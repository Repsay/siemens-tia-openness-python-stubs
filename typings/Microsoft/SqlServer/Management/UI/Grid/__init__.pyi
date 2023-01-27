# encoding: utf-8
# module Microsoft.SqlServer.Management.UI.Grid calls itself Grid
# from Microsoft.SqlServer.GridControl, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Char, Decimal, Enum, EventArgs, 
    IAsyncResult, IDisposable, Int64, IntPtr, MulticastDelegate, Single, 
    UInt32)

from System.Collections import CollectionBase

from System.ComponentModel import ISupportInitialize

from System.Drawing import (Bitmap, Brush, Color, Font, Graphics, Rectangle, 
    SolidBrush, StringFormat)

from System.Drawing.Printing import PrintDocument

from System.Web.UI import Control

from System.Windows.Forms import (AccessibleStates, BorderStyle, ButtonState, 
    ComboBox, ComboBoxStyle, DataObject, HorizontalAlignment, KeyEventArgs, 
    Keys, MouseButtons, NumericUpDown, TextBox, TextFormatFlags)

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point

"""The following names are not found in the module: (BoundEvent, 
    DragOperation, field#)
"""

# no functions
# classes

class BlockOfCells: # skipped bases: <type 'object'>, <type 'object'>
    """ BlockOfCells(nRowIndex: Int64, nColIndex: int) """
    @property
    def Bottom(self) -> Int64:
        """ Get: Bottom(self: BlockOfCells) -> Int64 """
        ...

    @property
    def Height(self) -> Int64:
        """
        Get: Height(self: BlockOfCells) -> Int64
        Set: Height(self: BlockOfCells) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: BlockOfCells) -> bool """
        ...

    @property
    def OriginalX(self) -> int:
        """ Get: OriginalX(self: BlockOfCells) -> int """
        ...

    @property
    def OriginalY(self) -> Int64:
        """ Get: OriginalY(self: BlockOfCells) -> Int64 """
        ...

    @property
    def Right(self) -> int:
        """ Get: Right(self: BlockOfCells) -> int """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: BlockOfCells) -> int
        Set: Width(self: BlockOfCells) = value
        """
        ...

    @property
    def X(self) -> int:
        """
        Get: X(self: BlockOfCells) -> int
        Set: X(self: BlockOfCells) = value
        """
        ...

    @property
    def Y(self) -> Int64:
        """
        Get: Y(self: BlockOfCells) -> Int64
        Set: Y(self: BlockOfCells) = value
        """
        ...


    def Contains(self, nRowIndex:Int64, nColIndex:int) -> bool:
        """ Contains(self: BlockOfCells, nRowIndex: Int64, nColIndex: int) -> bool """
        ...


class BlockOfCellsCollection(IDisposable, CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    BlockOfCellsCollection()
    BlockOfCellsCollection(value: BlockOfCellsCollection)
    BlockOfCellsCollection(value: Array[BlockOfCells])
    """
    def Add(self, node:BlockOfCells) -> int:
        """ Add(self: BlockOfCellsCollection, node: BlockOfCells) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: BlockOfCellsCollection, nodes: Array[BlockOfCells])AddRange(self: BlockOfCellsCollection, value: BlockOfCellsCollection) """
        ...

    def Contains(self, node:BlockOfCells) -> bool:
        """ Contains(self: BlockOfCellsCollection, node: BlockOfCells) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BlockOfCellsCollection, array: Array[BlockOfCells], index: int) """
        ...

    def IndexOf(self, node:BlockOfCells) -> int:
        """ IndexOf(self: BlockOfCellsCollection, node: BlockOfCells) -> int """
        ...

    def Insert(self, index:int, node:BlockOfCells): # -> 
        """ Insert(self: BlockOfCellsCollection, index: int, node: BlockOfCells) """
        ...

    def Remove(self, node:BlockOfCells): # -> 
        """ Remove(self: BlockOfCellsCollection, node: BlockOfCells) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ButtonCellState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ButtonCellState, values: Disabled (2), Empty (3), Normal (1), Pushed (0) """
    Disabled: ButtonCellState = ...
    Empty: ButtonCellState = ...
    Normal: ButtonCellState = ...
    Pushed: ButtonCellState = ...
    value__ = ...


class CaptureTracker: # skipped bases: <type 'object'>, <type 'object'>
    """ CaptureTracker() """
    @property
    def AdjustedCellRect(self) -> Rectangle:
        """
        Get: AdjustedCellRect(self: CaptureTracker) -> Rectangle
        Set: AdjustedCellRect(self: CaptureTracker) = value
        """
        ...

    @property
    def ButtonArea(self) -> GridButtonArea:
        """
        Get: ButtonArea(self: CaptureTracker) -> GridButtonArea
        Set: ButtonArea(self: CaptureTracker) = value
        """
        ...

    @property
    def ButtonWasPushed(self) -> bool:
        """
        Get: ButtonWasPushed(self: CaptureTracker) -> bool
        Set: ButtonWasPushed(self: CaptureTracker) = value
        """
        ...

    @property
    def CaptureHitTest(self) -> HitTestResult:
        """
        Get: CaptureHitTest(self: CaptureTracker) -> HitTestResult
        Set: CaptureHitTest(self: CaptureTracker) = value
        """
        ...

    @property
    def CellRect(self) -> Rectangle:
        """
        Get: CellRect(self: CaptureTracker) -> Rectangle
        Set: CellRect(self: CaptureTracker) = value
        """
        ...

    @property
    def ColIndexToDragColAfter(self) -> int:
        """
        Get: ColIndexToDragColAfter(self: CaptureTracker) -> int
        Set: ColIndexToDragColAfter(self: CaptureTracker) = value
        """
        ...

    @property
    def ColumnIndex(self) -> int:
        """
        Get: ColumnIndex(self: CaptureTracker) -> int
        Set: ColumnIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def DragState(self): # -> DragOperation
        """
        Get: DragState(self: CaptureTracker) -> DragOperation
        Set: DragState(self: CaptureTracker) = value
        """
        ...

    @property
    def HeaderDragY(self) -> int:
        """
        Get: HeaderDragY(self: CaptureTracker) -> int
        Set: HeaderDragY(self: CaptureTracker) = value
        """
        ...

    @property
    def LastColumnIndex(self) -> int:
        """
        Get: LastColumnIndex(self: CaptureTracker) -> int
        Set: LastColumnIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def LastColumnWidth(self) -> int:
        """
        Get: LastColumnWidth(self: CaptureTracker) -> int
        Set: LastColumnWidth(self: CaptureTracker) = value
        """
        ...

    @property
    def LastRowIndex(self) -> Int64:
        """
        Get: LastRowIndex(self: CaptureTracker) -> Int64
        Set: LastRowIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def LeftMostMergedColumnIndex(self) -> int:
        """
        Get: LeftMostMergedColumnIndex(self: CaptureTracker) -> int
        Set: LeftMostMergedColumnIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def MinWidthDuringColResize(self) -> int:
        """
        Get: MinWidthDuringColResize(self: CaptureTracker) -> int
        Set: MinWidthDuringColResize(self: CaptureTracker) = value
        """
        ...

    @property
    def MouseCapturePoint(self) -> Point:
        """
        Get: MouseCapturePoint(self: CaptureTracker) -> Point
        Set: MouseCapturePoint(self: CaptureTracker) = value
        """
        ...

    @property
    def MouseOffsetForColResize(self) -> int:
        """
        Get: MouseOffsetForColResize(self: CaptureTracker) -> int
        Set: MouseOffsetForColResize(self: CaptureTracker) = value
        """
        ...

    @property
    def OrigColumnWidth(self) -> int:
        """
        Get: OrigColumnWidth(self: CaptureTracker) -> int
        Set: OrigColumnWidth(self: CaptureTracker) = value
        """
        ...

    @property
    def RowIndex(self) -> Int64:
        """
        Get: RowIndex(self: CaptureTracker) -> Int64
        Set: RowIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def SelectionBlockIndex(self) -> int:
        """
        Get: SelectionBlockIndex(self: CaptureTracker) -> int
        Set: SelectionBlockIndex(self: CaptureTracker) = value
        """
        ...

    @property
    def TotalGridLineAdjDuringResize(self) -> int:
        """
        Get: TotalGridLineAdjDuringResize(self: CaptureTracker) -> int
        Set: TotalGridLineAdjDuringResize(self: CaptureTracker) = value
        """
        ...

    @property
    def WasOverButton(self) -> bool:
        """
        Get: WasOverButton(self: CaptureTracker) -> bool
        Set: WasOverButton(self: CaptureTracker) = value
        """
        ...


    def DragOperation(self, *args): #cannot find CLR method
        """ enum DragOperation, values: DragReady (1), None (0), StartedDrag (2) """
        ...

    def Reset(self): # -> 
        """ Reset(self: CaptureTracker) """
        ...

    def SetInfoFromHitTest(self, htInfo:HitTestInfo): # -> 
        """ SetInfoFromHitTest(self: CaptureTracker, htInfo: HitTestInfo) """
        ...

    def UpdateAdjustedRectHorizontally(self, x:int, width:int): # -> 
        """ UpdateAdjustedRectHorizontally(self: CaptureTracker, x: int, width: int) """
        ...

    NoColIndexToDragColAfter: int = ...


class ColumnReorderRequestedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ColumnReorderRequestedEventArgs(nColumnIndex: int, reordableByDefault: bool) """
    @property
    def AllowReorder(self) -> bool:
        """
        Get: AllowReorder(self: ColumnReorderRequestedEventArgs) -> bool
        Set: AllowReorder(self: ColumnReorderRequestedEventArgs) = value
        """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: ColumnReorderRequestedEventArgs) -> int """
        ...


    def __new__(cls, nColumnIndex:int, reordableByDefault:bool) -> Self:
        """ __new__(cls: type, nColumnIndex: int, reordableByDefault: bool) """
        ...


class ColumnReorderRequestedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ColumnReorderRequestedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, a:ColumnReorderRequestedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ColumnReorderRequestedEventHandler, sender: object, a: ColumnReorderRequestedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ColumnReorderRequestedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, a:ColumnReorderRequestedEventArgs): # -> 
        """ Invoke(self: ColumnReorderRequestedEventHandler, sender: object, a: ColumnReorderRequestedEventArgs) """
        ...


class ColumnsReorderedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ColumnsReorderedEventArgs(origIndex: int, newIndex: int) """
    @property
    def NewColumnIndex(self) -> int:
        """ Get: NewColumnIndex(self: ColumnsReorderedEventArgs) -> int """
        ...

    @property
    def OriginalColumnIndex(self) -> int:
        """ Get: OriginalColumnIndex(self: ColumnsReorderedEventArgs) -> int """
        ...


    def __new__(cls, origIndex:int, newIndex:int) -> Self:
        """ __new__(cls: type, origIndex: int, newIndex: int) """
        ...


class ColumnsReorderedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ColumnsReorderedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, a:ColumnsReorderedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ColumnsReorderedEventHandler, sender: object, a: ColumnsReorderedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ColumnsReorderedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, a:ColumnsReorderedEventArgs): # -> 
        """ Invoke(self: ColumnsReorderedEventHandler, sender: object, a: ColumnsReorderedEventArgs) """
        ...


class ColumnWidthChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ColumnWidthChangedEventArgs(nColIndex: int, nNewColWidth: int) """
    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: ColumnWidthChangedEventArgs) -> int """
        ...

    @property
    def NewColumnWidth(self) -> int:
        """ Get: NewColumnWidth(self: ColumnWidthChangedEventArgs) -> int """
        ...


    def __new__(cls, nColIndex:int, nNewColWidth:int) -> Self:
        """
        __new__(cls: type, nColIndex: int, nNewColWidth: int)
        __new__(cls: type)
        """
        ...


class ColumnWidthChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ColumnWidthChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:ColumnWidthChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ColumnWidthChangedEventHandler, sender: object, args: ColumnWidthChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ColumnWidthChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:ColumnWidthChangedEventArgs): # -> 
        """ Invoke(self: ColumnWidthChangedEventHandler, sender: object, args: ColumnWidthChangedEventArgs) """
        ...


class ContentsChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ContentsChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ContentsChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ContentsChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArgs): # -> 
        """ Invoke(self: ContentsChangedEventHandler, sender: object, e: EventArgs) """
        ...


class CustomizeCellGDIObjectsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CustomizeCellGDIObjectsEventArgs() """
    @property
    def BKBrush(self) -> SolidBrush:
        """
        Get: BKBrush(self: CustomizeCellGDIObjectsEventArgs) -> SolidBrush
        Set: BKBrush(self: CustomizeCellGDIObjectsEventArgs) = value
        """
        ...

    @property
    def CellFont(self) -> Font:
        """
        Get: CellFont(self: CustomizeCellGDIObjectsEventArgs) -> Font
        Set: CellFont(self: CustomizeCellGDIObjectsEventArgs) = value
        """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: CustomizeCellGDIObjectsEventArgs) -> int """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: CustomizeCellGDIObjectsEventArgs) -> Int64 """
        ...

    @property
    def TextBrush(self) -> SolidBrush:
        """
        Get: TextBrush(self: CustomizeCellGDIObjectsEventArgs) -> SolidBrush
        Set: TextBrush(self: CustomizeCellGDIObjectsEventArgs) = value
        """
        ...



class CustomizeCellGDIObjectsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CustomizeCellGDIObjectsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:CustomizeCellGDIObjectsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CustomizeCellGDIObjectsEventHandler, sender: object, args: CustomizeCellGDIObjectsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CustomizeCellGDIObjectsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:CustomizeCellGDIObjectsEventArgs): # -> 
        """ Invoke(self: CustomizeCellGDIObjectsEventHandler, sender: object, args: CustomizeCellGDIObjectsEventArgs) """
        ...


class EditableCellType: # skipped bases: <type 'object'>, <type 'object'>
    """ EditableCellType() """
    ComboBox: int = ...
    Editor: int = ...
    FirstCustomEditableCellType: int = ...
    ListBox: int = ...
    ReadOnly: int = ...
    SpinBox: int = ...


class IGridEmbeddedControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ColumnIndex(self) -> int:
        """
        Get: ColumnIndex(self: IGridEmbeddedControl) -> int
        Set: ColumnIndex(self: IGridEmbeddedControl) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IGridEmbeddedControl) -> bool
        Set: Enabled(self: IGridEmbeddedControl) = value
        """
        ...

    @property
    def RowIndex(self) -> Int64:
        """
        Get: RowIndex(self: IGridEmbeddedControl) -> Int64
        Set: RowIndex(self: IGridEmbeddedControl) = value
        """
        ...


    def AddDataAsString(self, Item:str) -> int:
        """ AddDataAsString(self: IGridEmbeddedControl, Item: str) -> int """
        ...

    def ClearData(self): # -> 
        """ ClearData(self: IGridEmbeddedControl) """
        ...

    def GetCurSelectionAsString(self) -> str:
        """ GetCurSelectionAsString(self: IGridEmbeddedControl) -> str """
        ...

    def GetCurSelectionIndex(self) -> int:
        """ GetCurSelectionIndex(self: IGridEmbeddedControl) -> int """
        ...

    def SetCurSelectionAsString(self, strNewSel:str) -> int:
        """ SetCurSelectionAsString(self: IGridEmbeddedControl, strNewSel: str) -> int """
        ...

    def SetCurSelectionIndex(self, nIndex:int): # -> 
        """ SetCurSelectionIndex(self: IGridEmbeddedControl, nIndex: int) """
        ...

    ContentsChanged = ...


class IGridEmbeddedControlManagement: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WantMouseClick(self) -> bool:
        """ Get: WantMouseClick(self: IGridEmbeddedControlManagement) -> bool """
        ...


    def SetHorizontalAlignment(self, alignment:HorizontalAlignment): # -> 
        """ SetHorizontalAlignment(self: IGridEmbeddedControlManagement, alignment: HorizontalAlignment) """
        ...


class IGridEmbeddedControlManagement2(IGridEmbeddedControlManagement): # skipped bases: <type 'object'>
    """ no doc """
    def PostProcessFocusFromKeyboard(self, keyStroke:Keys, modifiers:Keys): # -> 
        """ PostProcessFocusFromKeyboard(self: IGridEmbeddedControlManagement2, keyStroke: Keys, modifiers: Keys) """
        ...

    def ReceiveChar(self, c:Char): # -> 
        """ ReceiveChar(self: IGridEmbeddedControlManagement2, c: Char) """
        ...

    def ReceiveKeyboardEvent(self, ke:KeyEventArgs): # -> 
        """ ReceiveKeyboardEvent(self: IGridEmbeddedControlManagement2, ke: KeyEventArgs) """
        ...


class EmbeddedComboBox(IGridEmbeddedControl, ComboBox, IGridEmbeddedControlManagement2): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IGridEmbeddedControlManagement'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'object'>
    """ EmbeddedComboBox(parent: Control, MarginsWidth: int, style: ComboBoxStyle) """
    @property
    def WantMouseClick(self) -> bool:
        """ Get: WantMouseClick(self: EmbeddedComboBox) -> bool """
        ...


    def SetHorizontalAlignment(self, alignment:HorizontalAlignment): # -> 
        """ SetHorizontalAlignment(self: EmbeddedComboBox, alignment: HorizontalAlignment) """
        ...

    def __new__(cls, parent:Control, MarginsWidth:int, style:ComboBoxStyle) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Control, MarginsWidth: int, style: ComboBoxStyle)
        """
        ...

    ContentsChanged = ...
    m_ColumnIndex = ...
    m_MarginsWidth = ...
    m_myStringFormat = ...
    m_RowIndex = ...
    m_TextFormatFlags = ...


class EmbeddedControlContentsChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ EmbeddedControlContentsChangedEventArgs(embCtrl: IGridEmbeddedControl) """
    @property
    def EmbeddedControl(self) -> IGridEmbeddedControl:
        """ Get: EmbeddedControl(self: EmbeddedControlContentsChangedEventArgs) -> IGridEmbeddedControl """
        ...


    def __new__(cls, embCtrl:IGridEmbeddedControl) -> Self:
        """ __new__(cls: type, embCtrl: IGridEmbeddedControl) """
        ...


class EmbeddedControlContentsChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EmbeddedControlContentsChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:EmbeddedControlContentsChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: EmbeddedControlContentsChangedEventHandler, sender: object, args: EmbeddedControlContentsChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: EmbeddedControlContentsChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:EmbeddedControlContentsChangedEventArgs): # -> 
        """ Invoke(self: EmbeddedControlContentsChangedEventHandler, sender: object, args: EmbeddedControlContentsChangedEventArgs) """
        ...


class IGridEmbeddedSpinControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Increment(self) -> Decimal:
        """
        Get: Increment(self: IGridEmbeddedSpinControl) -> Decimal
        Set: Increment(self: IGridEmbeddedSpinControl) = value
        """
        ...

    @property
    def Maximum(self) -> Decimal:
        """
        Get: Maximum(self: IGridEmbeddedSpinControl) -> Decimal
        Set: Maximum(self: IGridEmbeddedSpinControl) = value
        """
        ...

    @property
    def Minimum(self) -> Decimal:
        """
        Get: Minimum(self: IGridEmbeddedSpinControl) -> Decimal
        Set: Minimum(self: IGridEmbeddedSpinControl) = value
        """
        ...



class EmbeddedSpinBox(NumericUpDown, IGridEmbeddedControl, IGridEmbeddedControlManagement2, IGridEmbeddedSpinControl): # skipped bases: <type 'IPersistStreamInit'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleInPlaceObject'>, <type 'IWin32Window'>, <type 'IOleObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'ISupportInitialize'>, <type 'IGridEmbeddedControlManagement'>, <type 'IDisposable'>, <type 'IContainerControl'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'object'>
    """ EmbeddedSpinBox(parent: Control, MarginsWidth: int) """
    @property
    def WantMouseClick(self) -> bool:
        """ Get: WantMouseClick(self: EmbeddedSpinBox) -> bool """
        ...


    def SetHorizontalAlignment(self, alignment:HorizontalAlignment): # -> 
        """ SetHorizontalAlignment(self: EmbeddedSpinBox, alignment: HorizontalAlignment) """
        ...

    def __new__(cls, parent:Control, MarginsWidth:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Control, MarginsWidth: int)
        """
        ...

    ContentsChanged = ...
    m_ColumnIndex = ...
    m_MarginsWidth = ...
    m_myDefWidth = ...
    m_RowIndex = ...


class EmbeddedTextBox(TextBox, IGridEmbeddedControl, IGridEmbeddedControlManagement2): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IGridEmbeddedControlManagement'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'object'>
    """ EmbeddedTextBox(parent: Control, MarginsWidth: int) """
    @property
    def AlwaysShowContextMenu(self) -> bool:
        """
        Get: AlwaysShowContextMenu(self: EmbeddedTextBox) -> bool
        Set: AlwaysShowContextMenu(self: EmbeddedTextBox) = value
        """
        ...

    @property
    def WantMouseClick(self) -> bool:
        """ Get: WantMouseClick(self: EmbeddedTextBox) -> bool """
        ...


    def SetHorizontalAlignment(self, alignment:HorizontalAlignment): # -> 
        """ SetHorizontalAlignment(self: EmbeddedTextBox, alignment: HorizontalAlignment) """
        ...

    def __new__(cls, parent:Control, MarginsWidth:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Control, MarginsWidth: int)
        """
        ...

    ContentsChanged = ...
    m_alwaysShowContextMenu = ...
    m_ColumnIndex = ...
    m_MarginsWidth = ...
    m_RowIndex = ...


class GridColumn(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackgroundBrush(self) -> SolidBrush:
        """
        Get: BackgroundBrush(self: GridColumn) -> SolidBrush
        Set: BackgroundBrush(self: GridColumn) = value
        """
        ...

    @property
    def ColumnIndex(self) -> int:
        """
        Get: ColumnIndex(self: GridColumn) -> int
        Set: ColumnIndex(self: GridColumn) = value
        """
        ...

    @property
    def ColumnType(self) -> int:
        """ Get: ColumnType(self: GridColumn) -> int """
        ...

    @property
    def IsWidthInChars(self) -> bool:
        """ Get: IsWidthInChars(self: GridColumn) -> bool """
        ...

    @property
    def RightGridLine(self) -> bool:
        """ Get: RightGridLine(self: GridColumn) -> bool """
        ...

    @property
    def TextAlign(self) -> HorizontalAlignment:
        """ Get: TextAlign(self: GridColumn) -> HorizontalAlignment """
        ...

    @property
    def TextBitmapLayout(self) -> TextBitmapLayout:
        """ Get: TextBitmapLayout(self: GridColumn) -> TextBitmapLayout """
        ...

    @property
    def TextBrush(self) -> SolidBrush:
        """
        Get: TextBrush(self: GridColumn) -> SolidBrush
        Set: TextBrush(self: GridColumn) = value
        """
        ...

    @property
    def WidthInPixels(self) -> int:
        """
        Get: WidthInPixels(self: GridColumn) -> int
        Set: WidthInPixels(self: GridColumn) = value
        """
        ...

    @property
    def WithSelectionBk(self) -> bool:
        """ Get: WithSelectionBk(self: GridColumn) -> bool """
        ...


    def DrawCell(self, g:Graphics, bkBrush:Brush, textBrush:SolidBrush, textFont:Font, rect:Rectangle, storage:IGridStorage, nRowIndex:Int64): # -> 
        """ DrawCell(self: GridColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64)DrawCell(self: GridColumn, g: Graphics, bkBrush: Brush, textBrush: Brush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64) """
        ...

    def DrawDisabledCell(self, g:Graphics, textFont:Font, rect:Rectangle, storage:IGridStorage, nRowIndex:Int64): # -> 
        """ DrawDisabledCell(self: GridColumn, g: Graphics, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64) """
        ...

    def GetAccessibleState(self, nRowIndex:Int64, storage:IGridStorage) -> AccessibleStates:
        """ GetAccessibleState(self: GridColumn, nRowIndex: Int64, storage: IGridStorage) -> AccessibleStates """
        ...

    def GetAccessibleValue(self, nRowIndex:Int64, storage:IGridStorage) -> str:
        """ GetAccessibleValue(self: GridColumn, nRowIndex: Int64, storage: IGridStorage) -> str """
        ...

    def IsPointOverTextInCell(self, pt:Point, cellRect:Rectangle, storage:IGridStorage, row:Int64, g:Graphics, f:Font) -> bool:
        """ IsPointOverTextInCell(self: GridColumn, pt: Point, cellRect: Rectangle, storage: IGridStorage, row: Int64, g: Graphics, f: Font) -> bool """
        ...

    def PrintCell(self, g:Graphics, bkBrush:Brush, textBrush:Brush, textFont:Font, rect:Rectangle, storage:IGridStorage, nRowIndex:Int64): # -> 
        """ PrintCell(self: GridColumn, g: Graphics, bkBrush: Brush, textBrush: Brush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64)PrintCell(self: GridColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64) """
        ...

    def ProcessNewGridFont(self, newFont:Font): # -> 
        """ ProcessNewGridFont(self: GridColumn, newFont: Font) """
        ...

    @staticmethod
    def SetDisabledColors(bkColor:Color, frColor:Color): # -> 
        """ SetDisabledColors(bkColor: Color, frColor: Color) """
        ...

    def SetRTL(self, bRightToLeft:bool): # -> 
        """ SetRTL(self: GridColumn, bRightToLeft: bool) """
        ...

    CELL_CONTENT_OFFSET: int = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...
    s_defaultRTL: bool = ...
    s_defaultWidthInPixels: int = ...
    s_DisabledCellBKBrush: SolidBrush = ...
    s_DisabledCellForeBrush: SolidBrush = ...


class GridBitmapColumn(GridColumn): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GridBitmapColumn(ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) """
    def DrawBitmap(self, *args): #cannot find CLR method
        """ DrawBitmap(self: GridBitmapColumn, g: Graphics, bkBrush: Brush, rect: Rectangle, myBmp: Bitmap, bEnabled: bool) """
        ...

    m_isRTL = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...


class GridButton: # skipped bases: <type 'object'>, <type 'object'>
    """ GridButton() """
    @property
    def ButtonAdditionalHeight(self) -> int:
        """ Get: ButtonAdditionalHeight() -> int """
        ...

    @property
    def RTL(self) -> bool:
        """
        Get: RTL(self: GridButton) -> bool
        Set: RTL(self: GridButton) = value
        """
        ...

    @property
    def TextBrush(self) -> Brush:
        """
        Get: TextBrush(self: GridButton) -> Brush
        Set: TextBrush(self: GridButton) = value
        """
        ...

    @property
    def TextFont(self) -> Font:
        """
        Get: TextFont(self: GridButton) -> Font
        Set: TextFont(self: GridButton) = value
        """
        ...


    @staticmethod
    def CalculateInitialContentsRect(g, r, text, bmp, contentsAlignment, textFont, bRtl, sFormat, nStringWidth) -> Tuple_[Rectangle, StringFormat, int]:
        """
        CalculateInitialContentsRect(g: Graphics, r: Rectangle, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, textFont: Font, bRtl: bool, sFormat: StringFormat) -> (Rectangle, StringFormat, int)
        CalculateInitialContentsRect(g: Graphics, r: Rectangle, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, textFont: Font, bRtl: bool, sFormat: TextFormatFlags) -> (Rectangle, TextFormatFlags, int)
        """
        ...

    @staticmethod
    def HitTest(g, *__args) -> GridButtonArea:
        """
        HitTest(g: Graphics, point: Point, buttonRect: Rectangle, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, textFont: Font, textBrush: Brush, sFormat: StringFormat, bRtl: bool) -> GridButtonArea
        HitTest(g: Graphics, point: Point, buttonRect: Rectangle, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, textFont: Font, textBrush: SolidBrush, sFormat: TextFormatFlags, bRtl: bool) -> GridButtonArea
        HitTest(self: GridButton, g: Graphics, p: Point, r: Rectangle, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout) -> GridButtonArea
        """
        ...

    @staticmethod
    def Paint(g:GridButton, r:Graphics, state:Rectangle, text:ButtonState, bmp:str, contentsAlignment:Bitmap, tbLayout:HorizontalAlignment, bEnabled:TextBitmapLayout, *__args:bool): # -> 
        """ Paint(g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool, textFont: Font, textBrush: Brush, sFormat: StringFormat, bRtl: bool)Paint(g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool, textFont: Font, textBrush: Brush, sFormat: StringFormat, bRtl: bool, buttonType: GridButtonType)Paint(g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool, textFont: Font, textBrush: SolidBrush, sFormat: TextFormatFlags, bRtl: bool)Paint(g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool, textFont: Font, textBrush: SolidBrush, sFormat: TextFormatFlags, bRtl: bool, buttonType: GridButtonType)Paint(self: GridButton, g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool)Paint(self: GridButton, g: Graphics, r: Rectangle, state: ButtonState, text: str, bmp: Bitmap, contentsAlignment: HorizontalAlignment, tbLayout: TextBitmapLayout, bEnabled: bool, buttonType: GridButtonType) """
        ...



class GridButtonArea(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridButtonArea, values: Background (3), Image (2), Nothing (0), Text (1) """
    Background: GridButtonArea = ...
    Image: GridButtonArea = ...
    Nothing: GridButtonArea = ...
    Text: GridButtonArea = ...
    value__ = ...


class GridTextColumn(GridColumn): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GridTextColumn(ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) """
    m_bVertical = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myStringFormat = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_textFormat = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...


class GridButtonColumn(GridTextColumn): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GridButtonColumn(ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) """
    @property
    def IsLineIndexButton(self) -> bool:
        """
        Get: IsLineIndexButton(self: GridButtonColumn) -> bool
        Set: IsLineIndexButton(self: GridButtonColumn) = value
        """
        ...


    def DrawButton(self, g:Graphics, bkBrush:Brush, textBrush:SolidBrush, textFont:Font, rect:Rectangle, buttomBmp:Bitmap, buttonLabel:str, btnState:ButtonState, bEnabled:bool, useGdiPlus:bool = ...): # -> 
        """ DrawButton(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, buttomBmp: Bitmap, buttonLabel: str, btnState: ButtonState, bEnabled: bool, useGdiPlus: bool)DrawButton(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, buttomBmp: Bitmap, buttonLabel: str, btnState: ButtonState, bEnabled: bool)DrawButton(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: Brush, textFont: Font, rect: Rectangle, buttomBmp: Bitmap, buttonLabel: str, btnState: ButtonState, bEnabled: bool) """
        ...

    def DrawCellCommon(self, *args): #cannot find CLR method
        """ DrawCellCommon(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: Brush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64, bEnabled: bool)DrawCellCommon(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64, bEnabled: bool)DrawCellCommon(self: GridButtonColumn, g: Graphics, bkBrush: Brush, textBrush: SolidBrush, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64, bEnabled: bool, useGdiPlus: bool) """
        ...

    def DrawDisabledCell(self, g:Graphics, textFont:Font, rect:Rectangle, storage:IGridStorage, nRowIndex:Int64): # -> 
        """ DrawDisabledCell(self: GridButtonColumn, g: Graphics, textFont: Font, rect: Rectangle, storage: IGridStorage, nRowIndex: Int64) """
        ...

    def SetForcedButtonState(self, rowIndex:Int64, state:ButtonState): # -> 
        """ SetForcedButtonState(self: GridButtonColumn, rowIndex: Int64, state: ButtonState) """
        ...

    def SetGridLinesMode(self, withLines:bool): # -> 
        """ SetGridLinesMode(self: GridButtonColumn, withLines: bool) """
        ...

    m_bVertical = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myStringFormat = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_textFormat = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...


class GridButtonType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridButtonType, values: Header (1), LineNumber (2), Normal (0) """
    Header: GridButtonType = ...
    LineNumber: GridButtonType = ...
    Normal: GridButtonType = ...
    value__ = ...


class GridCheckBoxColumn(GridBitmapColumn): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GridCheckBoxColumn(ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) """
    @property
    def CheckBoxHeight(self) -> int:
        """ Get: CheckBoxHeight(self: GridCheckBoxColumn) -> int """
        ...


    def BitmapFromGridCheckBoxState(self, state:GridCheckBoxState) -> Bitmap:
        """ BitmapFromGridCheckBoxState(self: GridCheckBoxColumn, state: GridCheckBoxState) -> Bitmap """
        ...

    def GetAccessibleState(self, nRowIndex:Int64, storage:IGridStorage) -> AccessibleStates:
        """ GetAccessibleState(self: GridCheckBoxColumn, nRowIndex: Int64, storage: IGridStorage) -> AccessibleStates """
        ...

    def GetAccessibleValue(self, nRowIndex:Int64, storage:IGridStorage) -> str:
        """ GetAccessibleValue(self: GridCheckBoxColumn, nRowIndex: Int64, storage: IGridStorage) -> str """
        ...

    def SetCheckboxBitmaps(self, checkedState:Bitmap, uncheckedState:Bitmap, indeterminateState:Bitmap, disabledState:Bitmap): # -> 
        """ SetCheckboxBitmaps(self: GridCheckBoxColumn, checkedState: Bitmap, uncheckedState: Bitmap, indeterminateState: Bitmap, disabledState: Bitmap) """
        ...

    m_CheckedBitmap = ...
    m_CurrentCheckSize = ...
    m_DisabledBitmap = ...
    m_IntermidiateBitmap = ...
    m_isRTL = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_UncheckedBitmap = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...


class GridCheckBoxState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridCheckBoxState, values: Checked (0), Disabled (3), Indeterminate (2), None (4), Unchecked (1) """
    Checked: GridCheckBoxState = ...
    Disabled: GridCheckBoxState = ...
    Indeterminate: GridCheckBoxState = ...
    Unchecked: GridCheckBoxState = ...
    value__ = ...


class GridColumnCollection(IDisposable, CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    GridColumnCollection()
    GridColumnCollection(value: GridColumnCollection)
    GridColumnCollection(value: Array[GridColumn])
    """
    def Add(self, node:GridColumn) -> int:
        """ Add(self: GridColumnCollection, node: GridColumn) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: GridColumnCollection, nodes: Array[GridColumn])AddRange(self: GridColumnCollection, value: GridColumnCollection) """
        ...

    def Contains(self, node:GridColumn) -> bool:
        """ Contains(self: GridColumnCollection, node: GridColumn) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: GridColumnCollection, array: Array[GridColumn], index: int) """
        ...

    def IndexOf(self, node:GridColumn) -> int:
        """ IndexOf(self: GridColumnCollection, node: GridColumn) -> int """
        ...

    def Insert(self, index:int, node:GridColumn): # -> 
        """ Insert(self: GridColumnCollection, index: int, node: GridColumn) """
        ...

    def Move(self, fromIndex:int, toIndex:int): # -> 
        """ Move(self: GridColumnCollection, fromIndex: int, toIndex: int) """
        ...

    def ProcessNewGridFont(self, newFont:Font): # -> 
        """ ProcessNewGridFont(self: GridColumnCollection, newFont: Font) """
        ...

    def Remove(self, node:GridColumn): # -> 
        """ Remove(self: GridColumnCollection, node: GridColumn) """
        ...

    def RemoveAtAndAdjust(self, index:int): # -> 
        """ RemoveAtAndAdjust(self: GridColumnCollection, index: int) """
        ...

    def SetRTL(self, bRightToLeft:bool): # -> 
        """ SetRTL(self: GridColumnCollection, bRightToLeft: bool) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class GridColumnHeaderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridColumnHeaderType, values: Bitmap (1), CheckBox (3), Text (0), TextAndBitmap (2), TextAndCheckBox (4) """
    Bitmap: GridColumnHeaderType = ...
    CheckBox: GridColumnHeaderType = ...
    Text: GridColumnHeaderType = ...
    TextAndBitmap: GridColumnHeaderType = ...
    TextAndCheckBox: GridColumnHeaderType = ...
    value__ = ...


class GridColumnInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ GridColumnInfo() """
    def SetBackgroundColor(self, bkColor:Color): # -> 
        """ SetBackgroundColor(self: GridColumnInfo, bkColor: Color) """
        ...

    def SetTextColor(self, frColor:Color): # -> 
        """ SetTextColor(self: GridColumnInfo, frColor: Color) """
        ...

    BackgroundColor = ...
    ColumnAlignment = ...
    ColumnType = ...
    ColumnWidth = ...
    HeaderAlignment = ...
    HeaderType = ...
    IsHeaderClickable = ...
    IsHeaderMergedWithRight = ...
    IsUserResizable = ...
    IsWithRightGridLine = ...
    IsWithSelectionBackground = ...
    MergedHeaderResizeProportion = ...
    TextBmpCellsLayout = ...
    TextBmpHeaderLayout = ...
    TextColor = ...
    WidthType = ...


class GridColumnInfoCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    GridColumnInfoCollection()
    GridColumnInfoCollection(value: GridColumnInfoCollection)
    GridColumnInfoCollection(value: Array[GridColumnInfo])
    """
    def Add(self, columnInfo:GridColumnInfo) -> int:
        """ Add(self: GridColumnInfoCollection, columnInfo: GridColumnInfo) -> int """
        ...

    def AddRange(self, *__args:Array): # -> 
        """ AddRange(self: GridColumnInfoCollection, columnInfos: Array[GridColumnInfo])AddRange(self: GridColumnInfoCollection, value: GridColumnInfoCollection) """
        ...

    def Contains(self, columnInfo:GridColumnInfo) -> bool:
        """ Contains(self: GridColumnInfoCollection, columnInfo: GridColumnInfo) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: GridColumnInfoCollection, array: Array[GridColumnInfo], index: int) """
        ...

    def IndexOf(self, columnInfo:GridColumnInfo) -> int:
        """ IndexOf(self: GridColumnInfoCollection, columnInfo: GridColumnInfo) -> int """
        ...

    def Insert(self, index:int, columnInfo:GridColumnInfo): # -> 
        """ Insert(self: GridColumnInfoCollection, index: int, columnInfo: GridColumnInfo) """
        ...

    def Remove(self, columnInfo:GridColumnInfo): # -> 
        """ Remove(self: GridColumnInfoCollection, columnInfo: GridColumnInfo) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class GridColumnType: # skipped bases: <type 'object'>, <type 'object'>
    """ GridColumnType() """
    Bitmap: int = ...
    Button: int = ...
    Checkbox: int = ...
    FirstCustomColumnType: int = ...
    Hyperlink: int = ...
    Text: int = ...


class GridColumnWidthType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridColumnWidthType, values: InAverageFontChar (1), InPixels (0) """
    InAverageFontChar: GridColumnWidthType = ...
    InPixels: GridColumnWidthType = ...
    value__ = ...


class GridConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ GridConstants() """
    @property
    def ActualCheckBoxSize(self) -> int:
        """ Get: ActualCheckBoxSize() -> int """
        ...

    @property
    def CheckedCheckBoxBitmap(self) -> Bitmap:
        """ Get: CheckedCheckBoxBitmap() -> Bitmap """
        ...

    @property
    def DefaultTextFormatFlags(self) -> TextFormatFlags:
        """ Get: DefaultTextFormatFlags() -> TextFormatFlags """
        ...

    @property
    def DisabledCheckBoxBitmap(self) -> Bitmap:
        """ Get: DisabledCheckBoxBitmap() -> Bitmap """
        ...

    @property
    def IntermidiateCheckBoxBitmap(self) -> Bitmap:
        """ Get: IntermidiateCheckBoxBitmap() -> Bitmap """
        ...

    @property
    def ScaleFactor(self) -> Single:
        """
        Get: ScaleFactor() -> Single
        Set: ScaleFactor() = value
        """
        ...

    @property
    def UncheckedCheckBoxBitmap(self) -> Bitmap:
        """ Get: UncheckedCheckBoxBitmap() -> Bitmap """
        ...


    StandardCheckBoxSize: int = ...
    TName: str = ...
    trERR: UInt32 = ...
    trL1: UInt32 = ...
    trL2: UInt32 = ...
    trL3: UInt32 = ...
    trL4: UInt32 = ...
    trWARN: UInt32 = ...


class IGridControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlwaysHighlightSelection(self) -> bool:
        """
        Get: AlwaysHighlightSelection(self: IGridControl) -> bool
        Set: AlwaysHighlightSelection(self: IGridControl) = value
        """
        ...

    @property
    def AutoScrollInterval(self) -> int:
        """
        Get: AutoScrollInterval(self: IGridControl) -> int
        Set: AutoScrollInterval(self: IGridControl) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: IGridControl) -> BorderStyle
        Set: BorderStyle(self: IGridControl) = value
        """
        ...

    @property
    def ColumnsNumber(self) -> int:
        """ Get: ColumnsNumber(self: IGridControl) -> int """
        ...

    @property
    def ColumnsReorderableByDefault(self) -> bool:
        """
        Get: ColumnsReorderableByDefault(self: IGridControl) -> bool
        Set: ColumnsReorderableByDefault(self: IGridControl) = value
        """
        ...

    @property
    def FirstScrollableColumn(self) -> int:
        """
        Get: FirstScrollableColumn(self: IGridControl) -> int
        Set: FirstScrollableColumn(self: IGridControl) = value
        """
        ...

    @property
    def FirstScrollableRow(self) -> UInt32:
        """
        Get: FirstScrollableRow(self: IGridControl) -> UInt32
        Set: FirstScrollableRow(self: IGridControl) = value
        """
        ...

    @property
    def FocusEditorOnNavigation(self) -> bool:
        """
        Get: FocusEditorOnNavigation(self: IGridControl) -> bool
        Set: FocusEditorOnNavigation(self: IGridControl) = value
        """
        ...

    @property
    def GridColumnsInfo(self) -> GridColumnInfoCollection:
        """ Get: GridColumnsInfo(self: IGridControl) -> GridColumnInfoCollection """
        ...

    @property
    def GridLineType(self) -> GridLineType:
        """
        Get: GridLineType(self: IGridControl) -> GridLineType
        Set: GridLineType(self: IGridControl) = value
        """
        ...

    @property
    def GridStorage(self) -> IGridStorage:
        """
        Get: GridStorage(self: IGridControl) -> IGridStorage
        Set: GridStorage(self: IGridControl) = value
        """
        ...

    @property
    def HeaderFont(self) -> Font:
        """
        Get: HeaderFont(self: IGridControl) -> Font
        Set: HeaderFont(self: IGridControl) = value
        """
        ...

    @property
    def HeaderHeight(self) -> int:
        """ Get: HeaderHeight(self: IGridControl) -> int """
        ...

    @property
    def HighlightColor(self) -> Color:
        """ Get: HighlightColor(self: IGridControl) -> Color """
        ...

    @property
    def MarginsWidth(self) -> int:
        """ Get: MarginsWidth(self: IGridControl) -> int """
        ...

    @property
    def PrintDocument(self) -> PrintDocument:
        """ Get: PrintDocument(self: IGridControl) -> PrintDocument """
        ...

    @property
    def RowHeight(self) -> int:
        """ Get: RowHeight(self: IGridControl) -> int """
        ...

    @property
    def SelectedCells(self) -> BlockOfCellsCollection:
        """
        Get: SelectedCells(self: IGridControl) -> BlockOfCellsCollection
        Set: SelectedCells(self: IGridControl) = value
        """
        ...

    @property
    def SelectionType(self) -> GridSelectionType:
        """
        Get: SelectionType(self: IGridControl) -> GridSelectionType
        Set: SelectionType(self: IGridControl) = value
        """
        ...

    @property
    def VisibleRowsNum(self) -> int:
        """ Get: VisibleRowsNum(self: IGridControl) -> int """
        ...

    @property
    def WithHeader(self) -> bool:
        """
        Get: WithHeader(self: IGridControl) -> bool
        Set: WithHeader(self: IGridControl) = value
        """
        ...


    def AddColumn(self, ci:GridColumnInfo): # -> 
        """ AddColumn(self: IGridControl, ci: GridColumnInfo) """
        ...

    def DeleteColumn(self, nIndex:int): # -> 
        """ DeleteColumn(self: IGridControl, nIndex: int) """
        ...

    def EnsureCellIsVisible(self, nRowIndex:Int64, nColIndex:int): # -> 
        """ EnsureCellIsVisible(self: IGridControl, nRowIndex: Int64, nColIndex: int) """
        ...

    def GetColumnWidth(self, nColIndex:int) -> int:
        """ GetColumnWidth(self: IGridControl, nColIndex: int) -> int """
        ...

    def GetCurrentCell(self, rowIndex, columnIndex) -> Tuple_[Int64, int]:
        """ GetCurrentCell(self: IGridControl) -> (Int64, int) """
        ...

    def GetDataObject(self, bOnlyCurrentSelBlock:bool) -> DataObject:
        """ GetDataObject(self: IGridControl, bOnlyCurrentSelBlock: bool) -> DataObject """
        ...

    def GetGridColumnInfo(self, columnIndex:int) -> GridColumnInfo:
        """ GetGridColumnInfo(self: IGridControl, columnIndex: int) -> GridColumnInfo """
        ...

    def GetHeaderInfo(self, colIndex, headerText, *__args) -> Tuple_[str, Bitmap]:
        """
        GetHeaderInfo(self: IGridControl, colIndex: int) -> (str, Bitmap)
        GetHeaderInfo(self: IGridControl, colIndex: int) -> (str, GridCheckBoxState)
        """
        ...

    def GetStorageColumnIndexByUIIndex(self, indexInUI:int) -> int:
        """ GetStorageColumnIndexByUIIndex(self: IGridControl, indexInUI: int) -> int """
        ...

    def GetUIColumnIndexByStorageIndex(self, indexInStorage:int) -> int:
        """ GetUIColumnIndexByStorageIndex(self: IGridControl, indexInStorage: int) -> int """
        ...

    def GetVisibleCellRectangle(self, rowIndex:Int64, columnIndex:int) -> Rectangle:
        """ GetVisibleCellRectangle(self: IGridControl, rowIndex: Int64, columnIndex: int) -> Rectangle """
        ...

    def HitTest(self, mouseX:int, mouseY:int) -> HitTestInfo:
        """ HitTest(self: IGridControl, mouseX: int, mouseY: int) -> HitTestInfo """
        ...

    def InsertColumn(self, nIndex:int, ci:GridColumnInfo): # -> 
        """ InsertColumn(self: IGridControl, nIndex: int, ci: GridColumnInfo) """
        ...

    def IsACellBeingEdited(self, nRowNum, nColNum) -> Tuple_[bool, Int64, int]:
        """ IsACellBeingEdited(self: IGridControl) -> (bool, Int64, int) """
        ...

    def RegisterEmbeddedControl(self, editableCellType:int, embeddedControl:Control): # -> 
        """ RegisterEmbeddedControl(self: IGridControl, editableCellType: int, embeddedControl: Control) """
        ...

    def ResetGrid(self): # -> 
        """ ResetGrid(self: IGridControl) """
        ...

    def ResizeColumnToShowAllContents(self, columnIndex:int): # -> 
        """ ResizeColumnToShowAllContents(self: IGridControl, columnIndex: int) """
        ...

    def SetBitmapsForCheckBoxColumn(self, nColIndex:int, checkedState:Bitmap, uncheckedState:Bitmap, indeterminateState:Bitmap, disabledState:Bitmap): # -> 
        """ SetBitmapsForCheckBoxColumn(self: IGridControl, nColIndex: int, checkedState: Bitmap, uncheckedState: Bitmap, indeterminateState: Bitmap, disabledState: Bitmap) """
        ...

    def SetColumnWidth(self, nColIndex:int, widthType:GridColumnWidthType, nWidth:int): # -> 
        """ SetColumnWidth(self: IGridControl, nColIndex: int, widthType: GridColumnWidthType, nWidth: int) """
        ...

    def SetHeaderInfo(self, *__args): # -> 
        """ SetHeaderInfo(self: IGridControl, nColIndex: int, strText: str, bmp: Bitmap)SetHeaderInfo(self: IGridControl, colIndex: int, strText: str, checkboxState: GridCheckBoxState) """
        ...

    def SetMergedHeaderResizeProportion(self, colIndex:int, proportion:Single): # -> 
        """ SetMergedHeaderResizeProportion(self: IGridControl, colIndex: int, proportion: Single) """
        ...

    def StartCellEdit(self, nRowIndex:Int64, nColIndex:int) -> bool:
        """ StartCellEdit(self: IGridControl, nRowIndex: Int64, nColIndex: int) -> bool """
        ...

    def StopCellEdit(self, bCommitIntoStorage:bool) -> bool:
        """ StopCellEdit(self: IGridControl, bCommitIntoStorage: bool) -> bool """
        ...

    def UpdateGrid(self, bRecalcRows:bool = ...): # -> 
        """ UpdateGrid(self: IGridControl)UpdateGrid(self: IGridControl, bRecalcRows: bool) """
        ...

    ColumnReorderRequested = ...
    ColumnsReordered = ...
    ColumnWidthChanged = ...
    CustomizeCellGDIObjects = ...
    EmbeddedControlContentsChanged = ...
    GridSpecialEvent = ...
    HeaderButtonClicked = ...
    KeyPressedOnCell = ...
    MouseButtonClicked = ...
    MouseButtonClicking = ...
    MouseButtonDoubleClicked = ...
    SelectionChanged = ...
    StandardKeyProcessing = ...
    TooltipDataNeeded = ...


class GridControl(Control, ISupportInitialize, IGridControl): # skipped bases: <type 'IViewObject'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IWin32Window'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleObject'>, <type 'object'>
    """ GridControl() """
    @property
    def ActAsEnabled(self):
        ...

    @property
    def ColumnsSeparator(self):
        ...

    @property
    def DefaultHeaderFont(self):
        ...

    @property
    def GridButtonHorizOffset(self) -> int:
        """ Get: GridButtonHorizOffset() -> int """
        ...

    @property
    def GridLinesPen(self):
        ...

    @property
    def IsEditing(self):
        ...

    @property
    def IsInitializing(self):
        ...

    @property
    def NeedToHighlightCurrentCell(self):
        ...

    @property
    def NewLineCharacters(self):
        ...

    @property
    def ShouldCommitEmbeddedControlOnLostFocus(self):
        ...

    @property
    def StandardGridCheckBoxSize(self) -> int:
        """ Get: StandardGridCheckBoxSize() -> int """
        ...

    @property
    def StringForBitmapData(self):
        ...

    @property
    def StringForButtonsWithBmpOnly(self):
        ...


    def AddColumnInternal(self, *args): #cannot find CLR method
        """ AddColumnInternal(self: GridControl, ci: GridColumnInfo) """
        ...

    def AdjustColumnIndexesInSelectedCells(self, *args): #cannot find CLR method
        """ AdjustColumnIndexesInSelectedCells(self: GridControl, originalCol: BlockOfCellsCollection, bFromUIToStorage: bool) -> BlockOfCellsCollection """
        ...

    def AdjustEmbeddedEditorBoundsForCustomColumn(self, *args): #cannot find CLR method
        """ AdjustEmbeddedEditorBoundsForCustomColumn(self: GridControl, bounds: Rectangle, uiColumnIndex: int, nRowIndex: Int64) -> Rectangle """
        ...

    def AdjustSelectionForButtonCellMouseClick(self, *args): #cannot find CLR method
        """ AdjustSelectionForButtonCellMouseClick(self: GridControl) -> bool """
        ...

    def AllocateBitmapColumn(self, *args): #cannot find CLR method
        """ AllocateBitmapColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridBitmapColumn """
        ...

    def AllocateButtonColumn(self, *args): #cannot find CLR method
        """ AllocateButtonColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridButtonColumn """
        ...

    def AllocateCheckBoxColumn(self, *args): #cannot find CLR method
        """ AllocateCheckBoxColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridCheckBoxColumn """
        ...

    def AllocateCustomColumn(self, *args): #cannot find CLR method
        """ AllocateCustomColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridColumn """
        ...

    def AllocateGridPrinter(self, *args): #cannot find CLR method
        """ AllocateGridPrinter(self: GridControl) -> GridPrinter """
        ...

    def AllocateHyperlinkColumn(self, *args): #cannot find CLR method
        """ AllocateHyperlinkColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridHyperlinkColumn """
        ...

    def AllocateTextColumn(self, *args): #cannot find CLR method
        """ AllocateTextColumn(self: GridControl, ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) -> GridTextColumn """
        ...

    def AlwaysHighlightSelectionInt(self, *args): #cannot find CLR method
        """ AlwaysHighlightSelectionInt(self: GridControl, bAlwaysHighlight: bool) """
        ...

    def CalculateHeaderHeight(self, *args): #cannot find CLR method
        """ CalculateHeaderHeight(self: GridControl, headerFont: Font) -> int """
        ...

    def CalcValidColWidth(self, *args): #cannot find CLR method
        """ CalcValidColWidth(self: GridControl, X: int) -> int """
        ...

    def CheckAndRePositionEmbeddedControlForSmallSizes(self, *args): #cannot find CLR method
        """ CheckAndRePositionEmbeddedControlForSmallSizes(self: GridControl) """
        ...

    def DeleteColumnInternal(self, *args): #cannot find CLR method
        """ DeleteColumnInternal(self: GridControl, nIndex: int) """
        ...

    def DoCellPainting(self, *args): #cannot find CLR method
        """ DoCellPainting(self: GridControl, g: Graphics, bkBrush: SolidBrush, textBrush: SolidBrush, textFont: Font, cellRect: Rectangle, gridColumn: GridColumn, rowNumber: Int64, enabledState: bool) """
        ...

    def DoCellPrinting(self, *args): #cannot find CLR method
        """ DoCellPrinting(self: GridControl, g: Graphics, bkBrush: SolidBrush, textBrush: SolidBrush, textFont: Font, cellRect: Rectangle, gridColumn: GridColumn, rowNumber: Int64) """
        ...

    def EnsureCellIsVisibleInternal(self, *args): #cannot find CLR method
        """ EnsureCellIsVisibleInternal(self: GridControl, nRowIndex: Int64, nColIndex: int) """
        ...

    def GetButtonCellState(self, *args): #cannot find CLR method
        """ GetButtonCellState(self: GridControl, nRowIndex: Int64, nColIndex: int) -> ButtonCellState """
        ...

    def GetCellFont(self, *args): #cannot find CLR method
        """ GetCellFont(self: GridControl, rowIndex: Int64, gridColumn: GridColumn) -> Font """
        ...

    def GetCellGDIObjects(self, *args): #cannot find CLR method
        """ GetCellGDIObjects(self: GridControl, gridColumn: GridColumn, nRow: Int64, nCol: int, bkBrush: SolidBrush, textBrush: SolidBrush) -> (SolidBrush, SolidBrush) """
        ...

    def GetCellStringForResizeToShowAll(self, *args): #cannot find CLR method
        """
        GetCellStringForResizeToShowAll(self: GridControl, rowIndex: Int64, storageColIndex: int) -> (str, StringFormat)
        GetCellStringForResizeToShowAll(self: GridControl, rowIndex: Int64, storageColIndex: int) -> (str, TextFormatFlags)
        """
        ...

    def GetColumnWidthInternal(self, *args): #cannot find CLR method
        """ GetColumnWidthInternal(self: GridControl, nColIndex: int) -> int """
        ...

    def GetCustomColumnStringForClipboardText(self, *args): #cannot find CLR method
        """ GetCustomColumnStringForClipboardText(self: GridControl, rowIndex: Int64, colIndex: int) -> str """
        ...

    def GetDataObjectInternal(self, *args): #cannot find CLR method
        """ GetDataObjectInternal(self: GridControl, bOnlyCurrentSelBlock: bool) -> DataObject """
        ...

    def GetHeaderInfoInternal(self, *args): #cannot find CLR method
        """ GetHeaderInfoInternal(self: GridControl, colIndex: int) -> (str, Bitmap, GridCheckBoxState) """
        ...

    def GetHeadersText(self) -> str:
        """ GetHeadersText(self: GridControl) -> str """
        ...

    def GetMinWidthOfColumn(self, *args): #cannot find CLR method
        """ GetMinWidthOfColumn(self: GridControl, colIndex: int) -> int """
        ...

    def GetRegisteredEmbeddedControl(self, *args): #cannot find CLR method
        """ GetRegisteredEmbeddedControl(self: GridControl, editableCellType: int) -> Control """
        ...

    def GetTextBasedColumnStringForClipboardText(self, *args): #cannot find CLR method
        """ GetTextBasedColumnStringForClipboardText(self: GridControl, rowIndex: Int64, colIndex: int) -> str """
        ...

    def GraphicsFromHandle(self, *args): #cannot find CLR method
        """ GraphicsFromHandle(self: GridControl) -> Graphics """
        ...

    def GridControlAccessibleObject(self, *args): #cannot find CLR method
        """ GridControlAccessibleObject(owner: GridControl) """
        ...

    def GridPrinter(self, *args): #cannot find CLR method
        """ GridPrinter(grid: GridControl) """
        ...

    def HandleButtonLBtnDown(self, *args): #cannot find CLR method
        """ HandleButtonLBtnDown(self: GridControl) -> bool """
        ...

    def HandleButtonLBtnUp(self, *args): #cannot find CLR method
        """ HandleButtonLBtnUp(self: GridControl, X: int, Y: int) """
        ...

    def HandleButtonMouseMove(self, *args): #cannot find CLR method
        """ HandleButtonMouseMove(self: GridControl, X: int, Y: int) """
        ...

    def HandleButtonMouseMoveWhileDraggingHeader(self, *args): #cannot find CLR method
        """ HandleButtonMouseMoveWhileDraggingHeader(self: GridControl, X: int, Y: int) """
        ...

    def HandleColResizeLBtnDown(self, *args): #cannot find CLR method
        """ HandleColResizeLBtnDown(self: GridControl) """
        ...

    def HandleColResizeLBtnUp(self, *args): #cannot find CLR method
        """ HandleColResizeLBtnUp(self: GridControl, X: int, Y: int) """
        ...

    def HandleColResizeMouseMove(self, *args): #cannot find CLR method
        """ HandleColResizeMouseMove(self: GridControl, X: int, Y: int, bLastUpdate: bool) """
        ...

    def HandleCustomCellDoubleClick(self, *args): #cannot find CLR method
        """ HandleCustomCellDoubleClick(self: GridControl, modKeys: Keys, btn: MouseButtons) """
        ...

    def HandleCustomCellMouseBtnDown(self, *args): #cannot find CLR method
        """ HandleCustomCellMouseBtnDown(self: GridControl, modKeys: Keys, btn: MouseButtons) -> bool """
        ...

    def HandleCustomCellMouseBtnUp(self, *args): #cannot find CLR method
        """ HandleCustomCellMouseBtnUp(self: GridControl, X: int, Y: int, btn: MouseButtons) """
        ...

    def HandleCustomCellMouseMove(self, *args): #cannot find CLR method
        """ HandleCustomCellMouseMove(self: GridControl, X: int, Y: int, btn: MouseButtons) """
        ...

    def HandleHeaderButtonMouseMove(self, *args): #cannot find CLR method
        """ HandleHeaderButtonMouseMove(self: GridControl, X: int, Y: int) -> bool """
        ...

    def HandleKeyboard(self, *args): #cannot find CLR method
        """ HandleKeyboard(self: GridControl, ke: KeyEventArgs) -> bool """
        ...

    def HandleStdCellLBtnDown(self, *args): #cannot find CLR method
        """ HandleStdCellLBtnDown(self: GridControl, modKeys: Keys) -> bool """
        ...

    def HandleStdCellLBtnMouseMove(self, *args): #cannot find CLR method
        """ HandleStdCellLBtnMouseMove(self: GridControl, nCurrentMouseX: int, nCurrentMouseY: int) """
        ...

    def HandleStdCellLBtnUp(self, *args): #cannot find CLR method
        """ HandleStdCellLBtnUp(self: GridControl, nCurrentMouseX: int, nCurrentMouseY: int) """
        ...

    def HandleTabOnLastOrFirstCell(self, *args): #cannot find CLR method
        """ HandleTabOnLastOrFirstCell(self: GridControl, goingLeft: bool) -> bool """
        ...

    def HitTestGridButton(self, *args): #cannot find CLR method
        """ HitTestGridButton(self: GridControl, rowIndex: Int64, colIndex: int, btnRect: Rectangle, ptToHitTest: Point) -> GridButtonArea """
        ...

    def HitTestInternal(self, *args): #cannot find CLR method
        """ HitTestInternal(self: GridControl, nMouseX: int, nMouseY: int) -> HitTestInfo """
        ...

    def InsertColumnInternal(self, *args): #cannot find CLR method
        """ InsertColumnInternal(self: GridControl, nIndex: int, ci: GridColumnInfo) """
        ...

    def IsACellBeingEditedInternal(self, *args): #cannot find CLR method
        """ IsACellBeingEditedInternal(self: GridControl) -> (bool, Int64, int) """
        ...

    def IsCellEditableFromKeyboardNav(self, *args): #cannot find CLR method
        """ IsCellEditableFromKeyboardNav(self: GridControl) -> bool """
        ...

    def IsCellVisible(self, column:int, row:Int64) -> bool:
        """ IsCellVisible(self: GridControl, column: int, row: Int64) -> bool """
        ...

    def IsColumnHeaderDraggable(self, *args): #cannot find CLR method
        """ IsColumnHeaderDraggable(self: GridControl, colIndex: int) -> bool """
        ...

    def MeasureWidthOfCustomColumnRows(self, *args): #cannot find CLR method
        """ MeasureWidthOfCustomColumnRows(self: GridControl, columnIndex: int, columnType: int, nFirstRow: Int64, nLastRow: Int64, g: Graphics) -> int """
        ...

    def MeasureWidthOfRows(self, *args): #cannot find CLR method
        """ MeasureWidthOfRows(self: GridControl, columnIndex: int, columnType: int, nFirstRow: Int64, nLastRow: Int64, g: Graphics) -> int """
        ...

    def NotifyAccAboutNewSelection(self, *args): #cannot find CLR method
        """ NotifyAccAboutNewSelection(self: GridControl, notifySelection: bool, notifyFocus: bool) """
        ...

    def OnBeforeGetClipboardTextForCells(self, *args): #cannot find CLR method
        """ OnBeforeGetClipboardTextForCells(self: GridControl, clipboardText: StringBuilder, nStartRow: Int64, nEndRow: Int64, nStartCol: int, nEndCol: int) -> bool """
        ...

    def OnCanInitiateDragFromCell(self, *args): #cannot find CLR method
        """ OnCanInitiateDragFromCell(self: GridControl, rowIndex: Int64, colIndex: int) -> bool """
        ...

    def OnColumnsReordered(self, *args): #cannot find CLR method
        """ OnColumnsReordered(self: GridControl, oldIndex: int, newIndex: int) """
        ...

    def OnColumnWasReordered(self, *args): #cannot find CLR method
        """ OnColumnWasReordered(self: GridControl, nOldIndex: int, nNewIndex: int) """
        ...

    def OnColumnWidthChanged(self, *args): #cannot find CLR method
        """ OnColumnWidthChanged(self: GridControl, nColIndex: int, nNewColWidth: int) """
        ...

    def OnEmbeddedControlContentsChanged(self, *args): #cannot find CLR method
        """ OnEmbeddedControlContentsChanged(self: GridControl, embeddedControl: IGridEmbeddedControl) """
        ...

    def OnEmbeddedControlLostFocus(self, *args): #cannot find CLR method
        """ OnEmbeddedControlLostFocus(self: GridControl) """
        ...

    def OnGridSpecialEvent(self, *args): #cannot find CLR method
        """ OnGridSpecialEvent(self: GridControl, eventType: int, data: object, htResult: HitTestResult, rowIndex: Int64, colIndex: int, cellRect: Rectangle, mouseState: MouseButtons, headerArea: GridButtonArea) """
        ...

    def OnHeaderButtonClicked(self, *args): #cannot find CLR method
        """ OnHeaderButtonClicked(self: GridControl, nColIndex: int, btn: MouseButtons, headerArea: GridButtonArea) -> bool """
        ...

    def OnKeyPressedOnCell(self, *args): #cannot find CLR method
        """ OnKeyPressedOnCell(self: GridControl, nCurRow: Int64, nCurCol: int, key: Keys, mod: Keys) """
        ...

    def OnMouseButtonClicked(self, *args): #cannot find CLR method
        """ OnMouseButtonClicked(self: GridControl, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons) -> bool """
        ...

    def OnMouseButtonClicking(self, *args): #cannot find CLR method
        """ OnMouseButtonClicking(self: GridControl, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, modKeys: Keys, btn: MouseButtons) -> bool """
        ...

    def OnMouseButtonDoubleClicked(self, *args): #cannot find CLR method
        """ OnMouseButtonDoubleClicked(self: GridControl, htArea: HitTestResult, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons, headerArea: GridButtonArea) """
        ...

    def OnMouseWheelInEmbeddedControl(self, *args): #cannot find CLR method
        """ OnMouseWheelInEmbeddedControl(self: GridControl, e: MouseEventArgs) """
        ...

    def OnResetFirstScrollableColumn(self, *args): #cannot find CLR method
        """ OnResetFirstScrollableColumn(self: GridControl, prevousFirstScrollableColumn: int, newFirstScrollableColumn: int) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: GridControl, selectedCells: BlockOfCellsCollection) """
        ...

    def OnStandardKeyProcessing(self, *args): #cannot find CLR method
        """ OnStandardKeyProcessing(self: GridControl, ke: KeyEventArgs) -> bool """
        ...

    def OnStartCellDragOperation(self, *args): #cannot find CLR method
        """ OnStartCellDragOperation(self: GridControl) """
        ...

    def OnStartedCellEdit(self, *args): #cannot find CLR method
        """ OnStartedCellEdit(self: GridControl) """
        ...

    def OnStoppedCellEdit(self, *args): #cannot find CLR method
        """ OnStoppedCellEdit(self: GridControl) """
        ...

    def OnTooltipDataNeeded(self, *args): #cannot find CLR method
        """ OnTooltipDataNeeded(self: GridControl, ht: HitTestResult, rowNumber: Int64, colNumber: int, toolTipText: str) -> (bool, str) """
        ...

    def PaintCurrentCellRect(self, *args): #cannot find CLR method
        """ PaintCurrentCellRect(self: GridControl, g: Graphics, r: Rectangle) """
        ...

    def PaintEmptyGrid(self, *args): #cannot find CLR method
        """ PaintEmptyGrid(self: GridControl, g: Graphics) """
        ...

    def PaintGrid(self, *args): #cannot find CLR method
        """ PaintGrid(self: GridControl, g: Graphics) """
        ...

    def PaintGridBackground(self, *args): #cannot find CLR method
        """ PaintGridBackground(self: GridControl, g: Graphics) """
        ...

    def PaintHeader(self, *args): #cannot find CLR method
        """ PaintHeader(self: GridControl, g: Graphics) """
        ...

    def PaintHeaderHelper(self, *args): #cannot find CLR method
        """ PaintHeaderHelper(self: GridControl, g: Graphics, nFirstCol: int, nLastCol: int, nFirstColPos: int, nY: int)PaintHeaderHelper(self: GridControl, g: Graphics, nFirstCol: int, nLastCol: int, nFirstColPos: int, nY: int, useGdiPlus: bool) """
        ...

    def PaintHorizGridLines(self, *args): #cannot find CLR method
        """ PaintHorizGridLines(self: GridControl, g: Graphics, rows: Int64, nFirstRowPos: int, nLeftMostPoint: int, nRightMostPoint: int, bAdjust: bool) """
        ...

    def PaintOneCell(self, *args): #cannot find CLR method
        """ PaintOneCell(self: GridControl, g: Graphics, nCol: int, nRow: Int64, nEditedCol: int, nEditedRow: Int64, rCell: Rectangle, rCurrentCellRect: Rectangle, rEditingCellRect: Rectangle) -> (Rectangle, Rectangle, Rectangle) """
        ...

    def PaintVertGridLines(self, *args): #cannot find CLR method
        """ PaintVertGridLines(self: GridControl, g: Graphics, nFirstCol: int, nLastCol: int, nFirstColPos: int, nTopMostPoint: int, nBottomMostPoint: int) """
        ...

    def PositionEmbeddedEditor(self, *args): #cannot find CLR method
        """ PositionEmbeddedEditor(self: GridControl, rEditingCellRect: Rectangle, nEditingCol: int) """
        ...

    def ProcessForTooltip(self, *args): #cannot find CLR method
        """ ProcessForTooltip(self: GridControl, ht: HitTestResult, nRowNumber: Int64, nColNumber: int) """
        ...

    def ProcessHomeEndKeys(self, *args): #cannot find CLR method
        """ ProcessHomeEndKeys(self: GridControl, bHome: bool, mod: Keys) """
        ...

    def ProcessLeftRightKeys(self, *args): #cannot find CLR method
        """ ProcessLeftRightKeys(self: GridControl, bLeft: bool, mod: Keys, bChangeRowIfNeeded: bool) -> bool """
        ...

    def ProcessLeftRightUpDownKeysForBlockSel(self, *args): #cannot find CLR method
        """ ProcessLeftRightUpDownKeysForBlockSel(self: GridControl, key: Keys) """
        ...

    def ProcessPageUpDownKeys(self, *args): #cannot find CLR method
        """ ProcessPageUpDownKeys(self: GridControl, bPageUp: bool, mod: Keys) -> bool """
        ...

    def ProcessUpDownKeys(self, *args): #cannot find CLR method
        """ ProcessUpDownKeys(self: GridControl, bDown: bool, mod: Keys) -> bool """
        ...

    def RegisterEmbeddedControlInternal(self, *args): #cannot find CLR method
        """ RegisterEmbeddedControlInternal(self: GridControl, editableCellType: int, embeddedControl: Control) """
        ...

    def ResetGridInternal(self, *args): #cannot find CLR method
        """ ResetGridInternal(self: GridControl) """
        ...

    def ResetHeaderFont(self): # -> 
        """ ResetHeaderFont(self: GridControl) """
        ...

    def ResizeColumnToShowAllContentsInternal(self, *args): #cannot find CLR method
        """ ResizeColumnToShowAllContentsInternal(self: GridControl, columnIndex: int)ResizeColumnToShowAllContentsInternal(self: GridControl, columnIndex: int, considerAllRows: bool) """
        ...

    def SelectedCellsInternal(self, *args): #cannot find CLR method
        """ SelectedCellsInternal(self: GridControl, col: BlockOfCellsCollection, bSet: bool) """
        ...

    def SendMouseClickToEmbeddedControl(self, *args): #cannot find CLR method
        """ SendMouseClickToEmbeddedControl(self: GridControl) """
        ...

    def SetColumnWidthInternal(self, *args): #cannot find CLR method
        """ SetColumnWidthInternal(self: GridControl, nColIndex: int, widthType: GridColumnWidthType, nWidth: int) """
        ...

    def SetCursorForCustomCell(self, *args): #cannot find CLR method
        """ SetCursorForCustomCell(self: GridControl, nRowIndex: Int64, nColumnIndex: int, r: Rectangle) """
        ...

    def SetCursorFromHitTest(self, *args): #cannot find CLR method
        """ SetCursorFromHitTest(self: GridControl, ht: HitTestResult, nRowIndex: Int64, nColumnIndex: int, cellRect: Rectangle) """
        ...

    def SetHeaderInfoInternal(self, *args): #cannot find CLR method
        """ SetHeaderInfoInternal(self: GridControl, nIndex: int, strText: str, bmp: Bitmap, checkboxState: GridCheckBoxState) """
        ...

    def SetMergedHeaderResizeProportionInternal(self, *args): #cannot find CLR method
        """ SetMergedHeaderResizeProportionInternal(self: GridControl, colIndex: int, proportion: Single) """
        ...

    def ShouldSerializeHeaderFont(self, *args): #cannot find CLR method
        """ ShouldSerializeHeaderFont(self: GridControl) -> bool """
        ...

    def StartCellEditInternal(self, *args): #cannot find CLR method
        """ StartCellEditInternal(self: GridControl, nRowIndex: Int64, nColIndex: int) -> bool """
        ...

    def StopCellEditInternal(self, *args): #cannot find CLR method
        """ StopCellEditInternal(self: GridControl, bCommitIntoStorage: bool) -> bool """
        ...

    def TooltipInfo(self, *args): #cannot find CLR method
        """ TooltipInfo() """
        ...

    def UpdateGridInternal(self, *args): #cannot find CLR method
        """ UpdateGridInternal(self: GridControl, bRecalcRows: bool) """
        ...

    ColumnReorderRequested = ...
    ColumnsReordered = ...
    ColumnWidthChanged = ...
    CustomizeCellGDIObjects = ...
    EmbeddedControlContentsChanged = ...
    GridSpecialEvent = ...
    HeaderButtonClicked = ...
    KeyPressedOnCell = ...
    MaxDisplayableChars: int = ...
    MouseButtonClicked = ...
    MouseButtonClicking = ...
    MouseButtonDoubleClicked = ...
    m_backBrush = ...
    m_captureTracker = ...
    m_Columns = ...
    m_curEmbeddedControl = ...
    m_gridFont = ...
    m_gridHeader = ...
    m_gridLinesPen = ...
    m_gridStorage = ...
    m_gridTooltip = ...
    m_highlightBrush = ...
    m_highlightTextBrush = ...
    m_hooverOverArea = ...
    m_linkFont = ...
    m_scrollableArea = ...
    m_scrollMgr = ...
    m_selMgr = ...
    SelectionChanged = ...
    StandardKeyProcessing = ...
    s_GridEventsCategory: str = ...
    s_GridPropsCategory: str = ...
    TooltipDataNeeded = ...


class GridHeader(IDisposable): # skipped bases: <type 'object'>
    """ GridHeader() """
    @property
    def Font(self) -> Font:
        """
        Get: Font(self: GridHeader) -> Font
        Set: Font(self: GridHeader) = value
        """
        ...

    @property
    def HeaderGridButton(self) -> GridButton:
        """ Get: HeaderGridButton(self: GridHeader) -> GridButton """
        ...


    def DeleteItem(self, nIndex:int): # -> 
        """ DeleteItem(self: GridHeader, nIndex: int) """
        ...

    def HeaderItem(self, *args): #cannot find CLR method
        """ HeaderItem(ci: GridColumnInfo) """
        ...

    def HeaderItemCollection(self, *args): #cannot find CLR method
        """
        HeaderItemCollection()
        HeaderItemCollection(value: HeaderItemCollection)
        HeaderItemCollection(value: Array[HeaderItem])
        """
        ...

    def InsertHeaderItem(self, nIndex:int, info:GridColumnInfo): # -> 
        """ InsertHeaderItem(self: GridHeader, nIndex: int, info: GridColumnInfo) """
        ...

    def Move(self, fromIndex:int, toIndex:int): # -> 
        """ Move(self: GridHeader, fromIndex: int, toIndex: int) """
        ...

    def Reset(self): # -> 
        """ Reset(self: GridHeader) """
        ...

    def SetHeaderItemInfo(self, nIndex:int, strText:str, bmp:Bitmap, checkboxState:GridCheckBoxState): # -> 
        """ SetHeaderItemInfo(self: GridHeader, nIndex: int, strText: str, bmp: Bitmap, checkboxState: GridCheckBoxState) """
        ...

    def SetHeaderItemState(self, nIndex:int, bPushed:bool): # -> 
        """ SetHeaderItemState(self: GridHeader, nIndex: int, bPushed: bool) """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...



class GridHyperlinkColumn(GridTextColumn): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GridHyperlinkColumn(ci: GridColumnInfo, nWidthInPixels: int, colIndex: int) """
    def GetCellStringToMeasure(self, *args): #cannot find CLR method
        """ GetCellStringToMeasure(self: GridHyperlinkColumn, rowIndex: Int64, storage: IGridStorage) -> str """
        ...

    def IsPointOverTextInCell(self, pt:Point, cellRect:Rectangle, storage:IGridStorage, row:Int64, g:Graphics, f:Font) -> bool:
        """ IsPointOverTextInCell(self: GridHyperlinkColumn, pt: Point, cellRect: Rectangle, storage: IGridStorage, row: Int64, g: Graphics, f: Font) -> bool """
        ...

    m_bVertical = ...
    m_myAlign = ...
    m_myBackgroundBrush = ...
    m_myColType = ...
    m_myColumnIndex = ...
    m_myStringFormat = ...
    m_myTextBmpLayout = ...
    m_myTextBrush = ...
    m_myWidthInChars = ...
    m_myWidthInPixels = ...
    m_textFormat = ...
    m_withRightGridLine = ...
    m_withSelectionBk = ...


class GridLineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridLineType, values: None (0), Solid (1) """
    Solid: GridLineType = ...
    value__ = ...


class GridSelectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridSelectionType, values: CellBlocks (4), ColumnBlocks (5), RowBlocks (3), SingleCell (1), SingleColumn (2), SingleRow (0) """
    CellBlocks: GridSelectionType = ...
    ColumnBlocks: GridSelectionType = ...
    RowBlocks: GridSelectionType = ...
    SingleCell: GridSelectionType = ...
    SingleColumn: GridSelectionType = ...
    SingleRow: GridSelectionType = ...
    value__ = ...


class MouseButtonDoubleClickedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MouseButtonDoubleClickedEventArgs(htRes: HitTestResult, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons, headerArea: GridButtonArea) """
    @property
    def Button(self) -> MouseButtons:
        """ Get: Button(self: MouseButtonDoubleClickedEventArgs) -> MouseButtons """
        ...

    @property
    def CellRect(self) -> Rectangle:
        """ Get: CellRect(self: MouseButtonDoubleClickedEventArgs) -> Rectangle """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: MouseButtonDoubleClickedEventArgs) -> int """
        ...

    @property
    def HeaderArea(self) -> GridButtonArea:
        """ Get: HeaderArea(self: MouseButtonDoubleClickedEventArgs) -> GridButtonArea """
        ...

    @property
    def HitTest(self) -> HitTestResult:
        """ Get: HitTest(self: MouseButtonDoubleClickedEventArgs) -> HitTestResult """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: MouseButtonDoubleClickedEventArgs) -> Int64 """
        ...


    def __new__(cls, htRes:HitTestResult, nRowIndex:Int64, nColIndex:int, rCellRect:Rectangle, btn:MouseButtons, headerArea:GridButtonArea) -> Self:
        """
        __new__(cls: type, htRes: HitTestResult, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons, headerArea: GridButtonArea)
        __new__(cls: type)
        """
        ...


class GridSpecialEventArgs(MouseButtonDoubleClickedEventArgs): # skipped bases: <type 'object'>
    """ GridSpecialEventArgs(eventType: int, data: object, htRes: HitTestResult, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons, headerArea: GridButtonArea) """
    @property
    def Data(self) -> object:
        """ Get: Data(self: GridSpecialEventArgs) -> object """
        ...

    @property
    def EventType(self) -> int:
        """ Get: EventType(self: GridSpecialEventArgs) -> int """
        ...


    HyperlinkClick: int = ...


class GridSpecialEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridSpecialEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, sea:GridSpecialEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridSpecialEventHandler, sender: object, sea: GridSpecialEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridSpecialEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, sea:GridSpecialEventArgs): # -> 
        """ Invoke(self: GridSpecialEventHandler, sender: object, sea: GridSpecialEventArgs) """
        ...


class HeaderButtonClickedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ HeaderButtonClickedEventArgs(nColIndex: int, btn: MouseButtons, headerArea: GridButtonArea) """
    @property
    def Button(self) -> MouseButtons:
        """ Get: Button(self: HeaderButtonClickedEventArgs) -> MouseButtons """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: HeaderButtonClickedEventArgs) -> int """
        ...

    @property
    def HeaderArea(self) -> GridButtonArea:
        """ Get: HeaderArea(self: HeaderButtonClickedEventArgs) -> GridButtonArea """
        ...

    @property
    def RepaintWholeGrid(self) -> bool:
        """
        Get: RepaintWholeGrid(self: HeaderButtonClickedEventArgs) -> bool
        Set: RepaintWholeGrid(self: HeaderButtonClickedEventArgs) = value
        """
        ...


    def __new__(cls, nColIndex:int, btn:MouseButtons, headerArea:GridButtonArea) -> Self:
        """
        __new__(cls: type, nColIndex: int, btn: MouseButtons, headerArea: GridButtonArea)
        __new__(cls: type)
        """
        ...


class HeaderButtonClickedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HeaderButtonClickedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:HeaderButtonClickedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HeaderButtonClickedEventHandler, sender: object, args: HeaderButtonClickedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: HeaderButtonClickedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:HeaderButtonClickedEventArgs): # -> 
        """ Invoke(self: HeaderButtonClickedEventHandler, sender: object, args: HeaderButtonClickedEventArgs) """
        ...


class HitTestInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ HitTestInfo(result: HitTestResult, rowIndex: Int64, columnIndex: int, areaRectangle: Rectangle) """
    @property
    def AreaRectangle(self) -> Rectangle:
        """ Get: AreaRectangle(self: HitTestInfo) -> Rectangle """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: HitTestInfo) -> int """
        ...

    @property
    def HitTestResult(self) -> HitTestResult:
        """ Get: HitTestResult(self: HitTestInfo) -> HitTestResult """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: HitTestInfo) -> Int64 """
        ...



class HitTestResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HitTestResult, values: BitmapCell (7), ButtonCell (6), ColumnOnly (1), ColumnResize (3), CustomCell (9), HeaderButton (4), HyperlinkCell (8), Nothing (0), RowOnly (2), TextCell (5) """
    BitmapCell: HitTestResult = ...
    ButtonCell: HitTestResult = ...
    ColumnOnly: HitTestResult = ...
    ColumnResize: HitTestResult = ...
    CustomCell: HitTestResult = ...
    HeaderButton: HitTestResult = ...
    HyperlinkCell: HitTestResult = ...
    Nothing: HitTestResult = ...
    RowOnly: HitTestResult = ...
    TextCell: HitTestResult = ...
    value__ = ...


class IGridStorage: # skipped bases: <type 'object'>
    """ no doc """
    def EnsureRowsInBuf(self, FirstRowIndex:Int64, LastRowIndex:Int64) -> Int64:
        """ EnsureRowsInBuf(self: IGridStorage, FirstRowIndex: Int64, LastRowIndex: Int64) -> Int64 """
        ...

    def FillControlWithData(self, nRowIndex:Int64, nColIndex:int, control:IGridEmbeddedControl): # -> 
        """ FillControlWithData(self: IGridStorage, nRowIndex: Int64, nColIndex: int, control: IGridEmbeddedControl) """
        ...

    def GetCellDataAsBitmap(self, nRowIndex:Int64, nColIndex:int) -> Bitmap:
        """ GetCellDataAsBitmap(self: IGridStorage, nRowIndex: Int64, nColIndex: int) -> Bitmap """
        ...

    def GetCellDataAsString(self, nRowIndex:Int64, nColIndex:int) -> str:
        """ GetCellDataAsString(self: IGridStorage, nRowIndex: Int64, nColIndex: int) -> str """
        ...

    def GetCellDataForButton(self, nRowIndex, nColIndex, state, image, buttonLabel) -> Tuple_[ButtonCellState, Bitmap, str]:
        """ GetCellDataForButton(self: IGridStorage, nRowIndex: Int64, nColIndex: int) -> (ButtonCellState, Bitmap, str) """
        ...

    def GetCellDataForCheckBox(self, nRowIndex:Int64, nColIndex:int) -> GridCheckBoxState:
        """ GetCellDataForCheckBox(self: IGridStorage, nRowIndex: Int64, nColIndex: int) -> GridCheckBoxState """
        ...

    def IsCellEditable(self, nRowIndex:Int64, nColIndex:int) -> int:
        """ IsCellEditable(self: IGridStorage, nRowIndex: Int64, nColIndex: int) -> int """
        ...

    def NumRows(self) -> Int64:
        """ NumRows(self: IGridStorage) -> Int64 """
        ...

    def SetCellDataFromControl(self, nRowIndex:Int64, nColIndex:int, control:IGridEmbeddedControl) -> bool:
        """ SetCellDataFromControl(self: IGridStorage, nRowIndex: Int64, nColIndex: int, control: IGridEmbeddedControl) -> bool """
        ...


class KeyPressedOnCellEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ KeyPressedOnCellEventArgs(nCurRow: Int64, nCurCol: int, k: Keys, m: Keys) """
    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: KeyPressedOnCellEventArgs) -> int """
        ...

    @property
    def Key(self) -> Keys:
        """ Get: Key(self: KeyPressedOnCellEventArgs) -> Keys """
        ...

    @property
    def Modifiers(self) -> Keys:
        """ Get: Modifiers(self: KeyPressedOnCellEventArgs) -> Keys """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: KeyPressedOnCellEventArgs) -> Int64 """
        ...


    def __new__(cls, nCurRow:Int64, nCurCol:int, k:Keys, m:Keys) -> Self:
        """
        __new__(cls: type, nCurRow: Int64, nCurCol: int, k: Keys, m: Keys)
        __new__(cls: type)
        """
        ...


class KeyPressedOnCellEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ KeyPressedOnCellEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:KeyPressedOnCellEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: KeyPressedOnCellEventHandler, sender: object, args: KeyPressedOnCellEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: KeyPressedOnCellEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:KeyPressedOnCellEventArgs): # -> 
        """ Invoke(self: KeyPressedOnCellEventHandler, sender: object, args: KeyPressedOnCellEventArgs) """
        ...


class MouseButtonClickedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MouseButtonClickedEventArgs(nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons) """
    @property
    def Button(self) -> MouseButtons:
        """ Get: Button(self: MouseButtonClickedEventArgs) -> MouseButtons """
        ...

    @property
    def CellRect(self) -> Rectangle:
        """ Get: CellRect(self: MouseButtonClickedEventArgs) -> Rectangle """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: MouseButtonClickedEventArgs) -> int """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: MouseButtonClickedEventArgs) -> Int64 """
        ...

    @property
    def ShouldRedraw(self) -> bool:
        """
        Get: ShouldRedraw(self: MouseButtonClickedEventArgs) -> bool
        Set: ShouldRedraw(self: MouseButtonClickedEventArgs) = value
        """
        ...


    def __new__(cls, nRowIndex:Int64, nColIndex:int, rCellRect:Rectangle, btn:MouseButtons) -> Self:
        """
        __new__(cls: type, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, btn: MouseButtons)
        __new__(cls: type)
        """
        ...


class MouseButtonClickedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MouseButtonClickedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:MouseButtonClickedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MouseButtonClickedEventHandler, sender: object, args: MouseButtonClickedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MouseButtonClickedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:MouseButtonClickedEventArgs): # -> 
        """ Invoke(self: MouseButtonClickedEventHandler, sender: object, args: MouseButtonClickedEventArgs) """
        ...


class MouseButtonClickingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MouseButtonClickingEventArgs(nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, mod: Keys, btn: MouseButtons) """
    @property
    def Button(self) -> MouseButtons:
        """ Get: Button(self: MouseButtonClickingEventArgs) -> MouseButtons """
        ...

    @property
    def CellRect(self) -> Rectangle:
        """ Get: CellRect(self: MouseButtonClickingEventArgs) -> Rectangle """
        ...

    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: MouseButtonClickingEventArgs) -> int """
        ...

    @property
    def Modifiers(self) -> Keys:
        """ Get: Modifiers(self: MouseButtonClickingEventArgs) -> Keys """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: MouseButtonClickingEventArgs) -> Int64 """
        ...

    @property
    def ShouldHandle(self) -> bool:
        """
        Get: ShouldHandle(self: MouseButtonClickingEventArgs) -> bool
        Set: ShouldHandle(self: MouseButtonClickingEventArgs) = value
        """
        ...


    def __new__(cls, nRowIndex:Int64, nColIndex:int, rCellRect:Rectangle, mod:Keys, btn:MouseButtons) -> Self:
        """
        __new__(cls: type, nRowIndex: Int64, nColIndex: int, rCellRect: Rectangle, mod: Keys, btn: MouseButtons)
        __new__(cls: type)
        """
        ...


class MouseButtonClickingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MouseButtonClickingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:MouseButtonClickingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MouseButtonClickingEventHandler, sender: object, args: MouseButtonClickingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MouseButtonClickingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:MouseButtonClickingEventArgs): # -> 
        """ Invoke(self: MouseButtonClickingEventHandler, sender: object, args: MouseButtonClickingEventArgs) """
        ...


class MouseButtonDoubleClickedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MouseButtonDoubleClickedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:MouseButtonDoubleClickedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MouseButtonDoubleClickedEventHandler, sender: object, args: MouseButtonDoubleClickedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MouseButtonDoubleClickedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:MouseButtonDoubleClickedEventArgs): # -> 
        """ Invoke(self: MouseButtonDoubleClickedEventHandler, sender: object, args: MouseButtonDoubleClickedEventArgs) """
        ...


class ScrollManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ScrollManager() """
    @property
    def CellHeight(self) -> int:
        """
        Get: CellHeight(self: ScrollManager) -> int
        Set: CellHeight(self: ScrollManager) = value
        """
        ...

    @property
    def FirstColumnIndex(self) -> int:
        """ Get: FirstColumnIndex(self: ScrollManager) -> int """
        ...

    @property
    def FirstColumnPos(self) -> int:
        """ Get: FirstColumnPos(self: ScrollManager) -> int """
        ...

    @property
    def FirstRowIndex(self) -> Int64:
        """ Get: FirstRowIndex(self: ScrollManager) -> Int64 """
        ...

    @property
    def FirstRowPos(self) -> int:
        """ Get: FirstRowPos(self: ScrollManager) -> int """
        ...

    @property
    def FirstScrollableColumnIndex(self) -> int:
        """
        Get: FirstScrollableColumnIndex(self: ScrollManager) -> int
        Set: FirstScrollableColumnIndex(self: ScrollManager) = value
        """
        ...

    @property
    def FirstScrollableRowIndex(self) -> UInt32:
        """
        Get: FirstScrollableRowIndex(self: ScrollManager) -> UInt32
        Set: FirstScrollableRowIndex(self: ScrollManager) = value
        """
        ...

    @property
    def LastColumnIndex(self) -> int:
        """ Get: LastColumnIndex(self: ScrollManager) -> int """
        ...

    @property
    def LastRowIndex(self) -> Int64:
        """ Get: LastRowIndex(self: ScrollManager) -> Int64 """
        ...

    @property
    def RowsNumber(self) -> Int64:
        """
        Get: RowsNumber(self: ScrollManager) -> Int64
        Set: RowsNumber(self: ScrollManager) = value
        """
        ...


    def EnsureCellIsVisible(self, nRowIndex:Int64, nColIndex:int, bMakeFirstColFullyVisible:bool = ..., bRedraw:bool = ...): # -> 
        """ EnsureCellIsVisible(self: ScrollManager, nRowIndex: Int64, nColIndex: int, bMakeFirstColFullyVisible: bool, bRedraw: bool)EnsureCellIsVisible(self: ScrollManager, nRowIndex: Int64, nColIndex: int) """
        ...

    def EnsureColumnIsVisible(self, nColIndex:int, bMakeFirstFullyVisible:bool, bRedraw:bool): # -> 
        """ EnsureColumnIsVisible(self: ScrollManager, nColIndex: int, bMakeFirstFullyVisible: bool, bRedraw: bool) """
        ...

    def EnsureRowIsVisbleWithoutClientRedraw(self, nRowIndex, bMakeRowTheTopOne, yDelta) -> Tuple_[bool, int]:
        """ EnsureRowIsVisbleWithoutClientRedraw(self: ScrollManager, nRowIndex: Int64, bMakeRowTheTopOne: bool) -> (bool, int) """
        ...

    def EnsureRowIsVisible(self, nRowIndex:Int64, bMakeRowTheTopOne:bool): # -> 
        """ EnsureRowIsVisible(self: ScrollManager, nRowIndex: Int64, bMakeRowTheTopOne: bool) """
        ...

    def GetCellRectangle(self, nRowIndex:Int64, nColIndex:int) -> Rectangle:
        """ GetCellRectangle(self: ScrollManager, nRowIndex: Int64, nColIndex: int) -> Rectangle """
        ...

    def HandleHScroll(self, nScrollRequest:int): # -> 
        """ HandleHScroll(self: ScrollManager, nScrollRequest: int) """
        ...

    def HandleVScroll(self, nScrollRequest:int): # -> 
        """ HandleVScroll(self: ScrollManager, nScrollRequest: int) """
        ...

    def MakeNextColumnVisible(self, bRedraw:bool): # -> 
        """ MakeNextColumnVisible(self: ScrollManager, bRedraw: bool) """
        ...

    def OnSAChange(self, *__args:Rectangle): # -> 
        """ OnSAChange(self: ScrollManager, newSA: Rectangle)OnSAChange(self: ScrollManager, nLeft: int, nRight: int, nTop: int, nBottom: int) """
        ...

    def ProcessDeleteCol(self, nIndex:int, nWidth:int): # -> 
        """ ProcessDeleteCol(self: ScrollManager, nIndex: int, nWidth: int) """
        ...

    def ProcessNewCol(self, nIndex:int): # -> 
        """ ProcessNewCol(self: ScrollManager, nIndex: int) """
        ...

    def RecalcAll(self, scrollableArea:Rectangle): # -> 
        """ RecalcAll(self: ScrollManager, scrollableArea: Rectangle) """
        ...

    def Reset(self): # -> 
        """ Reset(self: ScrollManager) """
        ...

    def SetColumns(self, columns:GridColumnCollection): # -> 
        """ SetColumns(self: ScrollManager, columns: GridColumnCollection) """
        ...

    def SetGridWindowHandle(self, handle:IntPtr): # -> 
        """ SetGridWindowHandle(self: ScrollManager, handle: IntPtr) """
        ...

    def SetHorizontalScrollUnitForArrows(self, numUnits:int): # -> 
        """ SetHorizontalScrollUnitForArrows(self: ScrollManager, numUnits: int) """
        ...

    def UpdateColWidth(self, nIndex:int, nOldWidth:int, nNewWidth:int, bFinalUpdate:bool): # -> 
        """ UpdateColWidth(self: ScrollManager, nIndex: int, nOldWidth: int, nNewWidth: int, bFinalUpdate: bool) """
        ...

    GRID_LINE_WIDTH: int = ...


class SelectionChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SelectionChangedEventArgs(blocks: BlockOfCellsCollection) """
    @property
    def SelectedBlocks(self) -> BlockOfCellsCollection:
        """ Get: SelectedBlocks(self: SelectionChangedEventArgs) -> BlockOfCellsCollection """
        ...


    def __new__(cls, blocks:BlockOfCellsCollection) -> Self:
        """
        __new__(cls: type, blocks: BlockOfCellsCollection)
        __new__(cls: type)
        """
        ...


class SelectionChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SelectionChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:SelectionChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SelectionChangedEventHandler, sender: object, args: SelectionChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SelectionChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:SelectionChangedEventArgs): # -> 
        """ Invoke(self: SelectionChangedEventHandler, sender: object, args: SelectionChangedEventArgs) """
        ...


class SelectionManager: # skipped bases: <type 'object'>, <type 'object'>
    """ SelectionManager() """
    @property
    def CurrentColumn(self) -> int:
        """
        Get: CurrentColumn(self: SelectionManager) -> int
        Set: CurrentColumn(self: SelectionManager) = value
        """
        ...

    @property
    def CurrentRow(self) -> Int64:
        """
        Get: CurrentRow(self: SelectionManager) -> Int64
        Set: CurrentRow(self: SelectionManager) = value
        """
        ...

    @property
    def CurrentSelectionBlockIndex(self) -> int:
        """ Get: CurrentSelectionBlockIndex(self: SelectionManager) -> int """
        ...

    @property
    def LastUpdatedColumn(self) -> int:
        """ Get: LastUpdatedColumn(self: SelectionManager) -> int """
        ...

    @property
    def LastUpdatedRow(self) -> Int64:
        """ Get: LastUpdatedRow(self: SelectionManager) -> Int64 """
        ...

    @property
    def OnlyOneCellSelected(self) -> bool:
        """ Get: OnlyOneCellSelected(self: SelectionManager) -> bool """
        ...

    @property
    def OnlyOneSelItem(self) -> bool:
        """ Get: OnlyOneSelItem(self: SelectionManager) -> bool """
        ...

    @property
    def SelectedBlocks(self) -> BlockOfCellsCollection:
        """ Get: SelectedBlocks(self: SelectionManager) -> BlockOfCellsCollection """
        ...

    @property
    def SelectionType(self) -> GridSelectionType:
        """
        Get: SelectionType(self: SelectionManager) -> GridSelectionType
        Set: SelectionType(self: SelectionManager) = value
        """
        ...


    def Clear(self, bClearCurrentCell:bool = ...): # -> 
        """ Clear(self: SelectionManager)Clear(self: SelectionManager, bClearCurrentCell: bool) """
        ...

    def GetSelecttionBlockNumberForCell(self, nRowIndex:Int64, nColIndex:int) -> int:
        """ GetSelecttionBlockNumberForCell(self: SelectionManager, nRowIndex: Int64, nColIndex: int) -> int """
        ...

    def IsCellSelected(self, nRowIndex:Int64, nColIndex:int) -> bool:
        """ IsCellSelected(self: SelectionManager, nRowIndex: Int64, nColIndex: int) -> bool """
        ...

    def ResetCurrentBlock(self): # -> 
        """ ResetCurrentBlock(self: SelectionManager) """
        ...

    def SetCurrentCell(self, rowIndex:Int64, columnIndex:int) -> bool:
        """ SetCurrentCell(self: SelectionManager, rowIndex: Int64, columnIndex: int) -> bool """
        ...

    def StartNewBlock(self, nRowIndex:Int64, nColIndex:int): # -> 
        """ StartNewBlock(self: SelectionManager, nRowIndex: Int64, nColIndex: int) """
        ...

    def StartNewBlockOrExcludeCell(self, nRowIndex:Int64, nColIndex:int) -> bool:
        """ StartNewBlockOrExcludeCell(self: SelectionManager, nRowIndex: Int64, nColIndex: int) -> bool """
        ...

    def UpdateCurrentBlock(self, nRowIndex:Int64, nColIndex:int): # -> 
        """ UpdateCurrentBlock(self: SelectionManager, nRowIndex: Int64, nColIndex: int) """
        ...


class StandardKeyProcessingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StandardKeyProcessingEventArgs(ke: KeyEventArgs) """
    @property
    def Key(self) -> Keys:
        """ Get: Key(self: StandardKeyProcessingEventArgs) -> Keys """
        ...

    @property
    def Modifiers(self) -> Keys:
        """ Get: Modifiers(self: StandardKeyProcessingEventArgs) -> Keys """
        ...

    @property
    def ShouldHandle(self) -> bool:
        """
        Get: ShouldHandle(self: StandardKeyProcessingEventArgs) -> bool
        Set: ShouldHandle(self: StandardKeyProcessingEventArgs) = value
        """
        ...


    def __new__(cls, ke:KeyEventArgs) -> Self:
        """
        __new__(cls: type, ke: KeyEventArgs)
        __new__(cls: type)
        """
        ...


class StandardKeyProcessingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StandardKeyProcessingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:StandardKeyProcessingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StandardKeyProcessingEventHandler, sender: object, args: StandardKeyProcessingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StandardKeyProcessingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:StandardKeyProcessingEventArgs): # -> 
        """ Invoke(self: StandardKeyProcessingEventHandler, sender: object, args: StandardKeyProcessingEventArgs) """
        ...


class TextBitmapLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextBitmapLayout, values: NotApplicable (0), TextLeftOfBitmap (1), TextRightOfBitmap (2) """
    NotApplicable: TextBitmapLayout = ...
    TextLeftOfBitmap: TextBitmapLayout = ...
    TextRightOfBitmap: TextBitmapLayout = ...
    value__ = ...


class TooltipDataNeededEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TooltipDataNeededEventArgs(ht: HitTestResult, rowIndex: Int64, colIndex: int) """
    @property
    def ColumnIndex(self) -> int:
        """ Get: ColumnIndex(self: TooltipDataNeededEventArgs) -> int """
        ...

    @property
    def HitTest(self) -> HitTestResult:
        """ Get: HitTest(self: TooltipDataNeededEventArgs) -> HitTestResult """
        ...

    @property
    def RowIndex(self) -> Int64:
        """ Get: RowIndex(self: TooltipDataNeededEventArgs) -> Int64 """
        ...

    @property
    def TooltipText(self) -> str:
        """
        Get: TooltipText(self: TooltipDataNeededEventArgs) -> str
        Set: TooltipText(self: TooltipDataNeededEventArgs) = value
        """
        ...


    def __new__(cls, ht:HitTestResult, rowIndex:Int64, colIndex:int) -> Self:
        """ __new__(cls: type, ht: HitTestResult, rowIndex: Int64, colIndex: int) """
        ...


class TooltipDataNeededEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TooltipDataNeededEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, a:TooltipDataNeededEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TooltipDataNeededEventHandler, sender: object, a: TooltipDataNeededEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TooltipDataNeededEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, a:TooltipDataNeededEventArgs): # -> 
        """ Invoke(self: TooltipDataNeededEventHandler, sender: object, a: TooltipDataNeededEventArgs) """
        ...


