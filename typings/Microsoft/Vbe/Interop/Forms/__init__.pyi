# encoding: utf-8
# module Microsoft.Vbe.Interop.Forms calls itself Forms
# from Microsoft.Vbe.Interop.Forms, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Decimal, Enum, Int16, MulticastDelegate, Single

from System.Collections import IEnumerable

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, StdPicture, 
    __ComObject, field#)
"""

# no functions
# classes

class IMdcCheckBox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: IMdcCheckBox) -> str
        Set: Accelerator(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Alignment(self) -> fmAlignment:
        """
        Get: Alignment(self: IMdcCheckBox) -> fmAlignment
        Set: Alignment(self: IMdcCheckBox) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: IMdcCheckBox) -> bool
        Set: AutoSize(self: IMdcCheckBox) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IMdcCheckBox) -> int
        Set: BackColor(self: IMdcCheckBox) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: IMdcCheckBox) -> fmBackStyle
        Set: BackStyle(self: IMdcCheckBox) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: IMdcCheckBox) -> bool
        Set: BordersSuppress(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IMdcCheckBox) -> str
        Set: Caption(self: IMdcCheckBox) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: IMdcCheckBox) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IMdcCheckBox) -> bool
        Set: Enabled(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IMdcCheckBox) -> NewFont
        Set: Font(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: IMdcCheckBox) -> bool
        Set: FontBold(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: IMdcCheckBox) -> bool
        Set: FontItalic(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: IMdcCheckBox) -> str
        Set: FontName(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: IMdcCheckBox) -> Decimal
        Set: FontSize(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: IMdcCheckBox) -> bool
        Set: FontStrikethru(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: IMdcCheckBox) -> bool
        Set: FontUnderline(self: IMdcCheckBox) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: IMdcCheckBox) -> Int16
        Set: FontWeight(self: IMdcCheckBox) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IMdcCheckBox) -> int
        Set: ForeColor(self: IMdcCheckBox) = value
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: IMdcCheckBox) -> str
        Set: GroupName(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: IMdcCheckBox) -> bool
        Set: Locked(self: IMdcCheckBox) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IMdcCheckBox) -> StdPicture
        Set: MouseIcon(self: IMdcCheckBox) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IMdcCheckBox) -> fmMousePointer
        Set: MousePointer(self: IMdcCheckBox) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: IMdcCheckBox) -> fmMultiSelect
        Set: MultiSelect(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: IMdcCheckBox) -> StdPicture
        Set: Picture(self: IMdcCheckBox) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: IMdcCheckBox) -> fmPicturePosition
        Set: PicturePosition(self: IMdcCheckBox) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmButtonEffect:
        """
        Get: SpecialEffect(self: IMdcCheckBox) -> fmButtonEffect
        Set: SpecialEffect(self: IMdcCheckBox) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: IMdcCheckBox) -> fmTextAlign
        Set: TextAlign(self: IMdcCheckBox) = value
        """
        ...

    @property
    def TripleState(self) -> bool:
        """
        Get: TripleState(self: IMdcCheckBox) -> bool
        Set: TripleState(self: IMdcCheckBox) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: IMdcCheckBox) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IMdcCheckBox) -> object
        Set: Value(self: IMdcCheckBox) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: IMdcCheckBox) -> bool
        Set: WordWrap(self: IMdcCheckBox) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IMdcCheckBox) = value """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class MdcCheckBoxEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcCheckBoxEvents_Event, : MdcCheckBoxEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class CheckBox(IMdcCheckBox, MdcCheckBoxEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CheckBoxClass(CheckBox, __ComObject): # skipped bases: <type 'IMdcCheckBox'>, <type 'MdcCheckBoxEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: CheckBoxClass) -> str
        Set: Accelerator(self: CheckBoxClass) = value
        """
        ...

    @property
    def Alignment(self) -> fmAlignment:
        """
        Get: Alignment(self: CheckBoxClass) -> fmAlignment
        Set: Alignment(self: CheckBoxClass) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: CheckBoxClass) -> bool
        Set: AutoSize(self: CheckBoxClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: CheckBoxClass) -> int
        Set: BackColor(self: CheckBoxClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: CheckBoxClass) -> fmBackStyle
        Set: BackStyle(self: CheckBoxClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: CheckBoxClass) -> bool
        Set: BordersSuppress(self: CheckBoxClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: CheckBoxClass) -> str
        Set: Caption(self: CheckBoxClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: CheckBoxClass) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CheckBoxClass) -> bool
        Set: Enabled(self: CheckBoxClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: CheckBoxClass) -> NewFont
        Set: Font(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: CheckBoxClass) -> bool
        Set: FontBold(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: CheckBoxClass) -> bool
        Set: FontItalic(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: CheckBoxClass) -> str
        Set: FontName(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: CheckBoxClass) -> Decimal
        Set: FontSize(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: CheckBoxClass) -> bool
        Set: FontStrikethru(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: CheckBoxClass) -> bool
        Set: FontUnderline(self: CheckBoxClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: CheckBoxClass) -> Int16
        Set: FontWeight(self: CheckBoxClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: CheckBoxClass) -> int
        Set: ForeColor(self: CheckBoxClass) = value
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: CheckBoxClass) -> str
        Set: GroupName(self: CheckBoxClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: CheckBoxClass) -> bool
        Set: Locked(self: CheckBoxClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: CheckBoxClass) -> StdPicture
        Set: MouseIcon(self: CheckBoxClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: CheckBoxClass) -> fmMousePointer
        Set: MousePointer(self: CheckBoxClass) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: CheckBoxClass) -> fmMultiSelect
        Set: MultiSelect(self: CheckBoxClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: CheckBoxClass) -> StdPicture
        Set: Picture(self: CheckBoxClass) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: CheckBoxClass) -> fmPicturePosition
        Set: PicturePosition(self: CheckBoxClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmButtonEffect:
        """
        Get: SpecialEffect(self: CheckBoxClass) -> fmButtonEffect
        Set: SpecialEffect(self: CheckBoxClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: CheckBoxClass) -> fmTextAlign
        Set: TextAlign(self: CheckBoxClass) = value
        """
        ...

    @property
    def TripleState(self) -> bool:
        """
        Get: TripleState(self: CheckBoxClass) -> bool
        Set: TripleState(self: CheckBoxClass) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: CheckBoxClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: CheckBoxClass) -> object
        Set: Value(self: CheckBoxClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: CheckBoxClass) -> bool
        Set: WordWrap(self: CheckBoxClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: CheckBoxClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: CheckBoxClass, : MdcCheckBoxEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: CheckBoxClass, : MdcCheckBoxEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: CheckBoxClass, : MdcCheckBoxEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: CheckBoxClass, : MdcCheckBoxEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: CheckBoxClass, : MdcCheckBoxEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: CheckBoxClass, : MdcCheckBoxEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: CheckBoxClass, : MdcCheckBoxEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: CheckBoxClass, : MdcCheckBoxEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: CheckBoxClass, : MdcCheckBoxEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: CheckBoxClass, : MdcCheckBoxEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: CheckBoxClass, : MdcCheckBoxEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: CheckBoxClass, : MdcCheckBoxEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: CheckBoxClass, : MdcCheckBoxEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: CheckBoxClass, : MdcCheckBoxEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: CheckBoxClass, : MdcCheckBoxEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: CheckBoxClass, : MdcCheckBoxEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: CheckBoxClass, : MdcCheckBoxEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: CheckBoxClass, : MdcCheckBoxEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: CheckBoxClass, : MdcCheckBoxEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: CheckBoxClass, : MdcCheckBoxEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: CheckBoxClass, : MdcCheckBoxEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: CheckBoxClass, : MdcCheckBoxEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: CheckBoxClass, : MdcCheckBoxEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: CheckBoxClass, : MdcCheckBoxEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class IMdcCombo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: IMdcCombo) -> bool
        Set: AutoSize(self: IMdcCombo) = value
        """
        ...

    @property
    def AutoTab(self) -> bool:
        """
        Get: AutoTab(self: IMdcCombo) -> bool
        Set: AutoTab(self: IMdcCombo) = value
        """
        ...

    @property
    def AutoWordSelect(self) -> bool:
        """
        Get: AutoWordSelect(self: IMdcCombo) -> bool
        Set: AutoWordSelect(self: IMdcCombo) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IMdcCombo) -> int
        Set: BackColor(self: IMdcCombo) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: IMdcCombo) -> fmBackStyle
        Set: BackStyle(self: IMdcCombo) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: IMdcCombo) -> int
        Set: BorderColor(self: IMdcCombo) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: IMdcCombo) -> bool
        Set: BordersSuppress(self: IMdcCombo) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: IMdcCombo) -> fmBorderStyle
        Set: BorderStyle(self: IMdcCombo) = value
        """
        ...

    @property
    def BoundColumn(self) -> object:
        """
        Get: BoundColumn(self: IMdcCombo) -> object
        Set: BoundColumn(self: IMdcCombo) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: IMdcCombo) -> bool """
        ...

    @property
    def ColumnCount(self) -> int:
        """
        Get: ColumnCount(self: IMdcCombo) -> int
        Set: ColumnCount(self: IMdcCombo) = value
        """
        ...

    @property
    def ColumnHeads(self) -> bool:
        """
        Get: ColumnHeads(self: IMdcCombo) -> bool
        Set: ColumnHeads(self: IMdcCombo) = value
        """
        ...

    @property
    def ColumnWidths(self) -> str:
        """
        Get: ColumnWidths(self: IMdcCombo) -> str
        Set: ColumnWidths(self: IMdcCombo) = value
        """
        ...

    @property
    def CurTargetX(self) -> int:
        """ Get: CurTargetX(self: IMdcCombo) -> int """
        ...

    @property
    def CurTargetY(self) -> int:
        """ Get: CurTargetY(self: IMdcCombo) -> int """
        ...

    @property
    def CurX(self) -> int:
        """
        Get: CurX(self: IMdcCombo) -> int
        Set: CurX(self: IMdcCombo) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: IMdcCombo) -> fmDisplayStyle """
        ...

    @property
    def DragBehavior(self) -> fmDragBehavior:
        """
        Get: DragBehavior(self: IMdcCombo) -> fmDragBehavior
        Set: DragBehavior(self: IMdcCombo) = value
        """
        ...

    @property
    def DropButtonStyle(self) -> fmDropButtonStyle:
        """
        Get: DropButtonStyle(self: IMdcCombo) -> fmDropButtonStyle
        Set: DropButtonStyle(self: IMdcCombo) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IMdcCombo) -> bool
        Set: Enabled(self: IMdcCombo) = value
        """
        ...

    @property
    def EnterFieldBehavior(self) -> fmEnterFieldBehavior:
        """
        Get: EnterFieldBehavior(self: IMdcCombo) -> fmEnterFieldBehavior
        Set: EnterFieldBehavior(self: IMdcCombo) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IMdcCombo) -> NewFont
        Set: Font(self: IMdcCombo) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: IMdcCombo) -> bool
        Set: FontBold(self: IMdcCombo) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: IMdcCombo) -> bool
        Set: FontItalic(self: IMdcCombo) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: IMdcCombo) -> str
        Set: FontName(self: IMdcCombo) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: IMdcCombo) -> Decimal
        Set: FontSize(self: IMdcCombo) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: IMdcCombo) -> bool
        Set: FontStrikethru(self: IMdcCombo) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: IMdcCombo) -> bool
        Set: FontUnderline(self: IMdcCombo) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: IMdcCombo) -> Int16
        Set: FontWeight(self: IMdcCombo) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IMdcCombo) -> int
        Set: ForeColor(self: IMdcCombo) = value
        """
        ...

    @property
    def HideSelection(self) -> bool:
        """
        Get: HideSelection(self: IMdcCombo) -> bool
        Set: HideSelection(self: IMdcCombo) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: IMdcCombo) -> fmIMEMode
        Set: IMEMode(self: IMdcCombo) = value
        """
        ...

    @property
    def LineCount(self) -> int:
        """ Get: LineCount(self: IMdcCombo) -> int """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: IMdcCombo) -> int """
        ...

    @property
    def ListCursor(self) -> object:
        """
        Get: ListCursor(self: IMdcCombo) -> object
        Set: ListCursor(self: IMdcCombo) = value
        """
        ...

    @property
    def ListIndex(self) -> object:
        """
        Get: ListIndex(self: IMdcCombo) -> object
        Set: ListIndex(self: IMdcCombo) = value
        """
        ...

    @property
    def ListRows(self) -> int:
        """
        Get: ListRows(self: IMdcCombo) -> int
        Set: ListRows(self: IMdcCombo) = value
        """
        ...

    @property
    def ListStyle(self) -> fmListStyle:
        """
        Get: ListStyle(self: IMdcCombo) -> fmListStyle
        Set: ListStyle(self: IMdcCombo) = value
        """
        ...

    @property
    def ListWidth(self) -> object:
        """
        Get: ListWidth(self: IMdcCombo) -> object
        Set: ListWidth(self: IMdcCombo) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: IMdcCombo) -> bool
        Set: Locked(self: IMdcCombo) = value
        """
        ...

    @property
    def MatchEntry(self) -> fmMatchEntry:
        """
        Get: MatchEntry(self: IMdcCombo) -> fmMatchEntry
        Set: MatchEntry(self: IMdcCombo) = value
        """
        ...

    @property
    def MatchFound(self) -> bool:
        """ Get: MatchFound(self: IMdcCombo) -> bool """
        ...

    @property
    def MatchRequired(self) -> bool:
        """
        Get: MatchRequired(self: IMdcCombo) -> bool
        Set: MatchRequired(self: IMdcCombo) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: IMdcCombo) -> int
        Set: MaxLength(self: IMdcCombo) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IMdcCombo) -> StdPicture
        Set: MouseIcon(self: IMdcCombo) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IMdcCombo) -> fmMousePointer
        Set: MousePointer(self: IMdcCombo) = value
        """
        ...

    @property
    def SelectionMargin(self) -> bool:
        """
        Get: SelectionMargin(self: IMdcCombo) -> bool
        Set: SelectionMargin(self: IMdcCombo) = value
        """
        ...

    @property
    def SelLength(self) -> int:
        """
        Get: SelLength(self: IMdcCombo) -> int
        Set: SelLength(self: IMdcCombo) = value
        """
        ...

    @property
    def SelStart(self) -> int:
        """
        Get: SelStart(self: IMdcCombo) -> int
        Set: SelStart(self: IMdcCombo) = value
        """
        ...

    @property
    def SelText(self) -> str:
        """
        Get: SelText(self: IMdcCombo) -> str
        Set: SelText(self: IMdcCombo) = value
        """
        ...

    @property
    def ShowDropButtonWhen(self) -> fmShowDropButtonWhen:
        """
        Get: ShowDropButtonWhen(self: IMdcCombo) -> fmShowDropButtonWhen
        Set: ShowDropButtonWhen(self: IMdcCombo) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: IMdcCombo) -> fmSpecialEffect
        Set: SpecialEffect(self: IMdcCombo) = value
        """
        ...

    @property
    def Style(self) -> fmStyle:
        """
        Get: Style(self: IMdcCombo) -> fmStyle
        Set: Style(self: IMdcCombo) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IMdcCombo) -> str
        Set: Text(self: IMdcCombo) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: IMdcCombo) -> fmTextAlign
        Set: TextAlign(self: IMdcCombo) = value
        """
        ...

    @property
    def TextColumn(self) -> object:
        """
        Get: TextColumn(self: IMdcCombo) -> object
        Set: TextColumn(self: IMdcCombo) = value
        """
        ...

    @property
    def TextLength(self) -> int:
        """ Get: TextLength(self: IMdcCombo) -> int """
        ...

    @property
    def TopIndex(self) -> object:
        """
        Get: TopIndex(self: IMdcCombo) -> object
        Set: TopIndex(self: IMdcCombo) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: IMdcCombo) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IMdcCombo) -> object
        Set: Value(self: IMdcCombo) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IMdcCombo) = value """
        ...


    def AddItem(self, pvargItem:object, pvargIndex:object) -> Tuple_[object, object]:
        """ AddItem(self: IMdcCombo, pvargItem: object, pvargIndex: object) -> (object, object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IMdcCombo) """
        ...

    def Copy(self): # -> 
        """ Copy(self: IMdcCombo) """
        ...

    def Cut(self): # -> 
        """ Cut(self: IMdcCombo) """
        ...

    def DropDown(self): # -> 
        """ DropDown(self: IMdcCombo) """
        ...

    def Paste(self): # -> 
        """ Paste(self: IMdcCombo) """
        ...

    def RemoveItem(self, pvargIndex:object) -> object:
        """ RemoveItem(self: IMdcCombo, pvargIndex: object) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class MdcComboEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcComboEvents_Event, : MdcComboEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcComboEvents_Event, : MdcComboEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcComboEvents_Event, : MdcComboEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MdcComboEvents_Event, : MdcComboEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcComboEvents_Event, : MdcComboEvents_DblClickEventHandler) """
        ...

    def add_DropButtonClick(self): # -> 
        """ add_DropButtonClick(self: MdcComboEvents_Event, : MdcComboEvents_DropButtonClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcComboEvents_Event, : MdcComboEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcComboEvents_Event, : MdcComboEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcComboEvents_Event, : MdcComboEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcComboEvents_Event, : MdcComboEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcComboEvents_Event, : MdcComboEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcComboEvents_Event, : MdcComboEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcComboEvents_Event, : MdcComboEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcComboEvents_Event, : MdcComboEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcComboEvents_Event, : MdcComboEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcComboEvents_Event, : MdcComboEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MdcComboEvents_Event, : MdcComboEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcComboEvents_Event, : MdcComboEvents_DblClickEventHandler) """
        ...

    def remove_DropButtonClick(self): # -> 
        """ remove_DropButtonClick(self: MdcComboEvents_Event, : MdcComboEvents_DropButtonClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcComboEvents_Event, : MdcComboEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcComboEvents_Event, : MdcComboEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcComboEvents_Event, : MdcComboEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcComboEvents_Event, : MdcComboEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcComboEvents_Event, : MdcComboEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcComboEvents_Event, : MdcComboEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcComboEvents_Event, : MdcComboEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    DropButtonClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class ComboBox(MdcComboEvents_Event, IMdcCombo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ComboBoxClass(ComboBox, __ComObject): # skipped bases: <type 'MdcComboEvents_Event'>, <type 'IMdcCombo'>, <type 'object'>
    """ no doc """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: ComboBoxClass) -> bool
        Set: AutoSize(self: ComboBoxClass) = value
        """
        ...

    @property
    def AutoTab(self) -> bool:
        """
        Get: AutoTab(self: ComboBoxClass) -> bool
        Set: AutoTab(self: ComboBoxClass) = value
        """
        ...

    @property
    def AutoWordSelect(self) -> bool:
        """
        Get: AutoWordSelect(self: ComboBoxClass) -> bool
        Set: AutoWordSelect(self: ComboBoxClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ComboBoxClass) -> int
        Set: BackColor(self: ComboBoxClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: ComboBoxClass) -> fmBackStyle
        Set: BackStyle(self: ComboBoxClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: ComboBoxClass) -> int
        Set: BorderColor(self: ComboBoxClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: ComboBoxClass) -> bool
        Set: BordersSuppress(self: ComboBoxClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: ComboBoxClass) -> fmBorderStyle
        Set: BorderStyle(self: ComboBoxClass) = value
        """
        ...

    @property
    def BoundColumn(self) -> object:
        """
        Get: BoundColumn(self: ComboBoxClass) -> object
        Set: BoundColumn(self: ComboBoxClass) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: ComboBoxClass) -> bool """
        ...

    @property
    def ColumnCount(self) -> int:
        """
        Get: ColumnCount(self: ComboBoxClass) -> int
        Set: ColumnCount(self: ComboBoxClass) = value
        """
        ...

    @property
    def ColumnHeads(self) -> bool:
        """
        Get: ColumnHeads(self: ComboBoxClass) -> bool
        Set: ColumnHeads(self: ComboBoxClass) = value
        """
        ...

    @property
    def ColumnWidths(self) -> str:
        """
        Get: ColumnWidths(self: ComboBoxClass) -> str
        Set: ColumnWidths(self: ComboBoxClass) = value
        """
        ...

    @property
    def CurTargetX(self) -> int:
        """ Get: CurTargetX(self: ComboBoxClass) -> int """
        ...

    @property
    def CurTargetY(self) -> int:
        """ Get: CurTargetY(self: ComboBoxClass) -> int """
        ...

    @property
    def CurX(self) -> int:
        """
        Get: CurX(self: ComboBoxClass) -> int
        Set: CurX(self: ComboBoxClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: ComboBoxClass) -> fmDisplayStyle """
        ...

    @property
    def DragBehavior(self) -> fmDragBehavior:
        """
        Get: DragBehavior(self: ComboBoxClass) -> fmDragBehavior
        Set: DragBehavior(self: ComboBoxClass) = value
        """
        ...

    @property
    def DropButtonStyle(self) -> fmDropButtonStyle:
        """
        Get: DropButtonStyle(self: ComboBoxClass) -> fmDropButtonStyle
        Set: DropButtonStyle(self: ComboBoxClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ComboBoxClass) -> bool
        Set: Enabled(self: ComboBoxClass) = value
        """
        ...

    @property
    def EnterFieldBehavior(self) -> fmEnterFieldBehavior:
        """
        Get: EnterFieldBehavior(self: ComboBoxClass) -> fmEnterFieldBehavior
        Set: EnterFieldBehavior(self: ComboBoxClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ComboBoxClass) -> NewFont
        Set: Font(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ComboBoxClass) -> bool
        Set: FontBold(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ComboBoxClass) -> bool
        Set: FontItalic(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ComboBoxClass) -> str
        Set: FontName(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ComboBoxClass) -> Decimal
        Set: FontSize(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ComboBoxClass) -> bool
        Set: FontStrikethru(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ComboBoxClass) -> bool
        Set: FontUnderline(self: ComboBoxClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ComboBoxClass) -> Int16
        Set: FontWeight(self: ComboBoxClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ComboBoxClass) -> int
        Set: ForeColor(self: ComboBoxClass) = value
        """
        ...

    @property
    def HideSelection(self) -> bool:
        """
        Get: HideSelection(self: ComboBoxClass) -> bool
        Set: HideSelection(self: ComboBoxClass) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: ComboBoxClass) -> fmIMEMode
        Set: IMEMode(self: ComboBoxClass) = value
        """
        ...

    @property
    def LineCount(self) -> int:
        """ Get: LineCount(self: ComboBoxClass) -> int """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: ComboBoxClass) -> int """
        ...

    @property
    def ListCursor(self) -> object:
        """
        Get: ListCursor(self: ComboBoxClass) -> object
        Set: ListCursor(self: ComboBoxClass) = value
        """
        ...

    @property
    def ListIndex(self) -> object:
        """
        Get: ListIndex(self: ComboBoxClass) -> object
        Set: ListIndex(self: ComboBoxClass) = value
        """
        ...

    @property
    def ListRows(self) -> int:
        """
        Get: ListRows(self: ComboBoxClass) -> int
        Set: ListRows(self: ComboBoxClass) = value
        """
        ...

    @property
    def ListStyle(self) -> fmListStyle:
        """
        Get: ListStyle(self: ComboBoxClass) -> fmListStyle
        Set: ListStyle(self: ComboBoxClass) = value
        """
        ...

    @property
    def ListWidth(self) -> object:
        """
        Get: ListWidth(self: ComboBoxClass) -> object
        Set: ListWidth(self: ComboBoxClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: ComboBoxClass) -> bool
        Set: Locked(self: ComboBoxClass) = value
        """
        ...

    @property
    def MatchEntry(self) -> fmMatchEntry:
        """
        Get: MatchEntry(self: ComboBoxClass) -> fmMatchEntry
        Set: MatchEntry(self: ComboBoxClass) = value
        """
        ...

    @property
    def MatchFound(self) -> bool:
        """ Get: MatchFound(self: ComboBoxClass) -> bool """
        ...

    @property
    def MatchRequired(self) -> bool:
        """
        Get: MatchRequired(self: ComboBoxClass) -> bool
        Set: MatchRequired(self: ComboBoxClass) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: ComboBoxClass) -> int
        Set: MaxLength(self: ComboBoxClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ComboBoxClass) -> StdPicture
        Set: MouseIcon(self: ComboBoxClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ComboBoxClass) -> fmMousePointer
        Set: MousePointer(self: ComboBoxClass) = value
        """
        ...

    @property
    def SelectionMargin(self) -> bool:
        """
        Get: SelectionMargin(self: ComboBoxClass) -> bool
        Set: SelectionMargin(self: ComboBoxClass) = value
        """
        ...

    @property
    def SelLength(self) -> int:
        """
        Get: SelLength(self: ComboBoxClass) -> int
        Set: SelLength(self: ComboBoxClass) = value
        """
        ...

    @property
    def SelStart(self) -> int:
        """
        Get: SelStart(self: ComboBoxClass) -> int
        Set: SelStart(self: ComboBoxClass) = value
        """
        ...

    @property
    def SelText(self) -> str:
        """
        Get: SelText(self: ComboBoxClass) -> str
        Set: SelText(self: ComboBoxClass) = value
        """
        ...

    @property
    def ShowDropButtonWhen(self) -> fmShowDropButtonWhen:
        """
        Get: ShowDropButtonWhen(self: ComboBoxClass) -> fmShowDropButtonWhen
        Set: ShowDropButtonWhen(self: ComboBoxClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: ComboBoxClass) -> fmSpecialEffect
        Set: SpecialEffect(self: ComboBoxClass) = value
        """
        ...

    @property
    def Style(self) -> fmStyle:
        """
        Get: Style(self: ComboBoxClass) -> fmStyle
        Set: Style(self: ComboBoxClass) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ComboBoxClass) -> str
        Set: Text(self: ComboBoxClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: ComboBoxClass) -> fmTextAlign
        Set: TextAlign(self: ComboBoxClass) = value
        """
        ...

    @property
    def TextColumn(self) -> object:
        """
        Get: TextColumn(self: ComboBoxClass) -> object
        Set: TextColumn(self: ComboBoxClass) = value
        """
        ...

    @property
    def TextLength(self) -> int:
        """ Get: TextLength(self: ComboBoxClass) -> int """
        ...

    @property
    def TopIndex(self) -> object:
        """
        Get: TopIndex(self: ComboBoxClass) -> object
        Set: TopIndex(self: ComboBoxClass) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: ComboBoxClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ComboBoxClass) -> object
        Set: Value(self: ComboBoxClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ComboBoxClass) = value """
        ...


    def AddItem(self, pvargItem:object, pvargIndex:object) -> Tuple_[object, object]:
        """ AddItem(self: ComboBoxClass, pvargItem: object, pvargIndex: object) -> (object, object) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ComboBoxClass, : MdcComboEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ComboBoxClass, : MdcComboEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: ComboBoxClass, : MdcComboEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: ComboBoxClass, : MdcComboEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: ComboBoxClass, : MdcComboEvents_DblClickEventHandler) """
        ...

    def add_DropButtonClick(self): # -> 
        """ add_DropButtonClick(self: ComboBoxClass, : MdcComboEvents_DropButtonClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ComboBoxClass, : MdcComboEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: ComboBoxClass, : MdcComboEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: ComboBoxClass, : MdcComboEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: ComboBoxClass, : MdcComboEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: ComboBoxClass, : MdcComboEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: ComboBoxClass, : MdcComboEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: ComboBoxClass, : MdcComboEvents_MouseUpEventHandler) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ComboBoxClass) """
        ...

    def Copy(self): # -> 
        """ Copy(self: ComboBoxClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: ComboBoxClass) """
        ...

    def DropDown(self): # -> 
        """ DropDown(self: ComboBoxClass) """
        ...

    def Paste(self): # -> 
        """ Paste(self: ComboBoxClass) """
        ...

    def RemoveItem(self, pvargIndex:object) -> object:
        """ RemoveItem(self: ComboBoxClass, pvargIndex: object) -> object """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ComboBoxClass, : MdcComboEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ComboBoxClass, : MdcComboEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: ComboBoxClass, : MdcComboEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: ComboBoxClass, : MdcComboEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: ComboBoxClass, : MdcComboEvents_DblClickEventHandler) """
        ...

    def remove_DropButtonClick(self): # -> 
        """ remove_DropButtonClick(self: ComboBoxClass, : MdcComboEvents_DropButtonClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ComboBoxClass, : MdcComboEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: ComboBoxClass, : MdcComboEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: ComboBoxClass, : MdcComboEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: ComboBoxClass, : MdcComboEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: ComboBoxClass, : MdcComboEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: ComboBoxClass, : MdcComboEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: ComboBoxClass, : MdcComboEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    DropButtonClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class CommandButtonEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: CommandButtonEvents_Event, : CommandButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: CommandButtonEvents_Event, : CommandButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: CommandButtonEvents_Event, : CommandButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: CommandButtonEvents_Event, : CommandButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: CommandButtonEvents_Event, : CommandButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: CommandButtonEvents_Event, : CommandButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: CommandButtonEvents_Event, : CommandButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: CommandButtonEvents_Event, : CommandButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: CommandButtonEvents_Event, : CommandButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: CommandButtonEvents_Event, : CommandButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: CommandButtonEvents_Event, : CommandButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: CommandButtonEvents_Event, : CommandButtonEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class ICommandButton: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: ICommandButton) -> str
        Set: Accelerator(self: ICommandButton) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: ICommandButton) -> bool
        Set: AutoSize(self: ICommandButton) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ICommandButton) -> int
        Set: BackColor(self: ICommandButton) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: ICommandButton) -> fmBackStyle
        Set: BackStyle(self: ICommandButton) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ICommandButton) -> str
        Set: Caption(self: ICommandButton) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ICommandButton) -> bool
        Set: Enabled(self: ICommandButton) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ICommandButton) -> NewFont
        Set: Font(self: ICommandButton) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ICommandButton) -> bool
        Set: FontBold(self: ICommandButton) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ICommandButton) -> bool
        Set: FontItalic(self: ICommandButton) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ICommandButton) -> str
        Set: FontName(self: ICommandButton) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ICommandButton) -> Decimal
        Set: FontSize(self: ICommandButton) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ICommandButton) -> bool
        Set: FontStrikethru(self: ICommandButton) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ICommandButton) -> bool
        Set: FontUnderline(self: ICommandButton) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ICommandButton) -> Int16
        Set: FontWeight(self: ICommandButton) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ICommandButton) -> int
        Set: ForeColor(self: ICommandButton) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: ICommandButton) -> bool
        Set: Locked(self: ICommandButton) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ICommandButton) -> StdPicture
        Set: MouseIcon(self: ICommandButton) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ICommandButton) -> fmMousePointer
        Set: MousePointer(self: ICommandButton) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: ICommandButton) -> StdPicture
        Set: Picture(self: ICommandButton) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: ICommandButton) -> fmPicturePosition
        Set: PicturePosition(self: ICommandButton) = value
        """
        ...

    @property
    def TakeFocusOnClick(self) -> bool:
        """
        Get: TakeFocusOnClick(self: ICommandButton) -> bool
        Set: TakeFocusOnClick(self: ICommandButton) = value
        """
        ...

    @property
    def Value(self) -> bool:
        """
        Get: Value(self: ICommandButton) -> bool
        Set: Value(self: ICommandButton) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: ICommandButton) -> bool
        Set: WordWrap(self: ICommandButton) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ICommandButton) = value """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CommandButton(CommandButtonEvents_Event, ICommandButton): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CommandButtonClass(CommandButton, __ComObject): # skipped bases: <type 'ICommandButton'>, <type 'CommandButtonEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: CommandButtonClass) -> str
        Set: Accelerator(self: CommandButtonClass) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: CommandButtonClass) -> bool
        Set: AutoSize(self: CommandButtonClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: CommandButtonClass) -> int
        Set: BackColor(self: CommandButtonClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: CommandButtonClass) -> fmBackStyle
        Set: BackStyle(self: CommandButtonClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: CommandButtonClass) -> str
        Set: Caption(self: CommandButtonClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CommandButtonClass) -> bool
        Set: Enabled(self: CommandButtonClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: CommandButtonClass) -> NewFont
        Set: Font(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: CommandButtonClass) -> bool
        Set: FontBold(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: CommandButtonClass) -> bool
        Set: FontItalic(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: CommandButtonClass) -> str
        Set: FontName(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: CommandButtonClass) -> Decimal
        Set: FontSize(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: CommandButtonClass) -> bool
        Set: FontStrikethru(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: CommandButtonClass) -> bool
        Set: FontUnderline(self: CommandButtonClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: CommandButtonClass) -> Int16
        Set: FontWeight(self: CommandButtonClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: CommandButtonClass) -> int
        Set: ForeColor(self: CommandButtonClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: CommandButtonClass) -> bool
        Set: Locked(self: CommandButtonClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: CommandButtonClass) -> StdPicture
        Set: MouseIcon(self: CommandButtonClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: CommandButtonClass) -> fmMousePointer
        Set: MousePointer(self: CommandButtonClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: CommandButtonClass) -> StdPicture
        Set: Picture(self: CommandButtonClass) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: CommandButtonClass) -> fmPicturePosition
        Set: PicturePosition(self: CommandButtonClass) = value
        """
        ...

    @property
    def TakeFocusOnClick(self) -> bool:
        """
        Get: TakeFocusOnClick(self: CommandButtonClass) -> bool
        Set: TakeFocusOnClick(self: CommandButtonClass) = value
        """
        ...

    @property
    def Value(self) -> bool:
        """
        Get: Value(self: CommandButtonClass) -> bool
        Set: Value(self: CommandButtonClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: CommandButtonClass) -> bool
        Set: WordWrap(self: CommandButtonClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: CommandButtonClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: CommandButtonClass, : CommandButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: CommandButtonClass, : CommandButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: CommandButtonClass, : CommandButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: CommandButtonClass, : CommandButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: CommandButtonClass, : CommandButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: CommandButtonClass, : CommandButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: CommandButtonClass, : CommandButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: CommandButtonClass, : CommandButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: CommandButtonClass, : CommandButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: CommandButtonClass, : CommandButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: CommandButtonClass, : CommandButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: CommandButtonClass, : CommandButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: CommandButtonClass, : CommandButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: CommandButtonClass, : CommandButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: CommandButtonClass, : CommandButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: CommandButtonClass, : CommandButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: CommandButtonClass, : CommandButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: CommandButtonClass, : CommandButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: CommandButtonClass, : CommandButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: CommandButtonClass, : CommandButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: CommandButtonClass, : CommandButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: CommandButtonClass, : CommandButtonEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class CommandButtonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: CommandButtonEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: CommandButtonEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Click(self): # -> 
        """ Click(self: CommandButtonEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: CommandButtonEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: CommandButtonEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: CommandButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: CommandButtonEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: CommandButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: CommandButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: CommandButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: CommandButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class CommandButtonEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: CommandButtonEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class CommandButtonEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: CommandButtonEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class CommandButtonEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: CommandButtonEvents_ClickEventHandler) """
        ...


class CommandButtonEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: CommandButtonEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class CommandButtonEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: CommandButtonEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class CommandButtonEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: CommandButtonEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class CommandButtonEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: CommandButtonEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class CommandButtonEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: CommandButtonEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class CommandButtonEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: CommandButtonEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class CommandButtonEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: CommandButtonEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class CommandButtonEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandButtonEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: CommandButtonEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class CommandButtonEvents_SinkHelper(CommandButtonEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class ControlEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AfterUpdate(self): # -> 
        """ add_AfterUpdate(self: ControlEvents_Event, : ControlEvents_AfterUpdateEventHandler) """
        ...

    def add_BeforeUpdate(self): # -> 
        """ add_BeforeUpdate(self: ControlEvents_Event, : ControlEvents_BeforeUpdateEventHandler) """
        ...

    def add_Enter(self): # -> 
        """ add_Enter(self: ControlEvents_Event, : ControlEvents_EnterEventHandler) """
        ...

    def add_Exit(self): # -> 
        """ add_Exit(self: ControlEvents_Event, : ControlEvents_ExitEventHandler) """
        ...

    def remove_AfterUpdate(self): # -> 
        """ remove_AfterUpdate(self: ControlEvents_Event, : ControlEvents_AfterUpdateEventHandler) """
        ...

    def remove_BeforeUpdate(self): # -> 
        """ remove_BeforeUpdate(self: ControlEvents_Event, : ControlEvents_BeforeUpdateEventHandler) """
        ...

    def remove_Enter(self): # -> 
        """ remove_Enter(self: ControlEvents_Event, : ControlEvents_EnterEventHandler) """
        ...

    def remove_Exit(self): # -> 
        """ remove_Exit(self: ControlEvents_Event, : ControlEvents_ExitEventHandler) """
        ...

    AfterUpdate = ...
    BeforeUpdate = ...
    Enter = ...
    Exit = ...


class IControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BoundValue(self) -> object:
        """
        Get: BoundValue(self: IControl) -> object
        Set: BoundValue(self: IControl) = value
        """
        ...

    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: IControl) -> bool
        Set: Cancel(self: IControl) = value
        """
        ...

    @property
    def ControlSource(self) -> str:
        """
        Get: ControlSource(self: IControl) -> str
        Set: ControlSource(self: IControl) = value
        """
        ...

    @property
    def ControlTipText(self) -> str:
        """
        Get: ControlTipText(self: IControl) -> str
        Set: ControlTipText(self: IControl) = value
        """
        ...

    @property
    def Default(self) -> bool:
        """
        Get: Default(self: IControl) -> bool
        Set: Default(self: IControl) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: IControl) -> Single
        Set: Height(self: IControl) = value
        """
        ...

    @property
    def HelpContextID(self) -> int:
        """
        Get: HelpContextID(self: IControl) -> int
        Set: HelpContextID(self: IControl) = value
        """
        ...

    @property
    def InSelection(self) -> bool:
        """
        Get: InSelection(self: IControl) -> bool
        Set: InSelection(self: IControl) = value
        """
        ...

    @property
    def LayoutEffect(self) -> fmLayoutEffect:
        """ Get: LayoutEffect(self: IControl) -> fmLayoutEffect """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: IControl) -> Single
        Set: Left(self: IControl) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IControl) -> str
        Set: Name(self: IControl) = value
        """
        ...

    @property
    def Object(self) -> object:
        """ Get: Object(self: IControl) -> object """
        ...

    @property
    def OldHeight(self) -> Single:
        """ Get: OldHeight(self: IControl) -> Single """
        ...

    @property
    def OldLeft(self) -> Single:
        """ Get: OldLeft(self: IControl) -> Single """
        ...

    @property
    def OldTop(self) -> Single:
        """ Get: OldTop(self: IControl) -> Single """
        ...

    @property
    def OldWidth(self) -> Single:
        """ Get: OldWidth(self: IControl) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IControl) -> object """
        ...

    @property
    def RowSource(self) -> str:
        """
        Get: RowSource(self: IControl) -> str
        Set: RowSource(self: IControl) = value
        """
        ...

    @property
    def RowSourceType(self) -> Int16:
        """
        Get: RowSourceType(self: IControl) -> Int16
        Set: RowSourceType(self: IControl) = value
        """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: IControl) -> Int16
        Set: TabIndex(self: IControl) = value
        """
        ...

    @property
    def TabStop(self) -> bool:
        """
        Get: TabStop(self: IControl) -> bool
        Set: TabStop(self: IControl) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: IControl) -> str
        Set: Tag(self: IControl) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: IControl) -> Single
        Set: Top(self: IControl) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: IControl) -> bool
        Set: Visible(self: IControl) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: IControl) -> Single
        Set: Width(self: IControl) = value
        """
        ...


    def Move(self, Left:object, Top:object, Width:object, Height:object, Layout:object): # -> 
        """ Move(self: IControl, Left: object, Top: object, Width: object, Height: object, Layout: object) """
        ...

    def Select(self, SelectInGroup:bool): # -> 
        """ Select(self: IControl, SelectInGroup: bool) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: IControl) """
        ...

    def ZOrder(self, zPosition:object): # -> 
        """ ZOrder(self: IControl, zPosition: object) """
        ...

    def _GetHeight(self, Height) -> int:
        """ _GetHeight(self: IControl) -> int """
        ...

    def _GethWnd(self) -> int:
        """ _GethWnd(self: IControl) -> int """
        ...

    def _GetID(self) -> int:
        """ _GetID(self: IControl) -> int """
        ...

    def _GetLeft(self, Left) -> int:
        """ _GetLeft(self: IControl) -> int """
        ...

    def _GetOldHeight(self, OldHeight) -> int:
        """ _GetOldHeight(self: IControl) -> int """
        ...

    def _GetOldLeft(self, OldLeft) -> int:
        """ _GetOldLeft(self: IControl) -> int """
        ...

    def _GetOldTop(self, OldTop) -> int:
        """ _GetOldTop(self: IControl) -> int """
        ...

    def _GetOldWidth(self, OldWidth) -> int:
        """ _GetOldWidth(self: IControl) -> int """
        ...

    def _GetTop(self, Top) -> int:
        """ _GetTop(self: IControl) -> int """
        ...

    def _GetWidth(self, Width) -> int:
        """ _GetWidth(self: IControl) -> int """
        ...

    def _Move(self, Left:int, Top:int, Width:int, Height:int): # -> 
        """ _Move(self: IControl, Left: int, Top: int, Width: int, Height: int) """
        ...

    def _SetHeight(self, Height:int): # -> 
        """ _SetHeight(self: IControl, Height: int) """
        ...

    def _SetLeft(self, Left:int): # -> 
        """ _SetLeft(self: IControl, Left: int) """
        ...

    def _SetTop(self, Top:int): # -> 
        """ _SetTop(self: IControl, Top: int) """
        ...

    def _SetWidth(self, Width:int): # -> 
        """ _SetWidth(self: IControl, Width: int) """
        ...

    def _ZOrder(self, zPosition:fmZOrder): # -> 
        """ _ZOrder(self: IControl, zPosition: fmZOrder) """
        ...


class Control(ControlEvents_Event, IControl): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ControlClass(Control, __ComObject): # skipped bases: <type 'ControlEvents_Event'>, <type 'IControl'>, <type 'object'>
    """ ControlClass() """
    @property
    def BoundValue(self) -> object:
        """
        Get: BoundValue(self: ControlClass) -> object
        Set: BoundValue(self: ControlClass) = value
        """
        ...

    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: ControlClass) -> bool
        Set: Cancel(self: ControlClass) = value
        """
        ...

    @property
    def ControlSource(self) -> str:
        """
        Get: ControlSource(self: ControlClass) -> str
        Set: ControlSource(self: ControlClass) = value
        """
        ...

    @property
    def ControlTipText(self) -> str:
        """
        Get: ControlTipText(self: ControlClass) -> str
        Set: ControlTipText(self: ControlClass) = value
        """
        ...

    @property
    def Default(self) -> bool:
        """
        Get: Default(self: ControlClass) -> bool
        Set: Default(self: ControlClass) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: ControlClass) -> Single
        Set: Height(self: ControlClass) = value
        """
        ...

    @property
    def HelpContextID(self) -> int:
        """
        Get: HelpContextID(self: ControlClass) -> int
        Set: HelpContextID(self: ControlClass) = value
        """
        ...

    @property
    def InSelection(self) -> bool:
        """
        Get: InSelection(self: ControlClass) -> bool
        Set: InSelection(self: ControlClass) = value
        """
        ...

    @property
    def LayoutEffect(self) -> fmLayoutEffect:
        """ Get: LayoutEffect(self: ControlClass) -> fmLayoutEffect """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: ControlClass) -> Single
        Set: Left(self: ControlClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ControlClass) -> str
        Set: Name(self: ControlClass) = value
        """
        ...

    @property
    def Object(self) -> object:
        """ Get: Object(self: ControlClass) -> object """
        ...

    @property
    def OldHeight(self) -> Single:
        """ Get: OldHeight(self: ControlClass) -> Single """
        ...

    @property
    def OldLeft(self) -> Single:
        """ Get: OldLeft(self: ControlClass) -> Single """
        ...

    @property
    def OldTop(self) -> Single:
        """ Get: OldTop(self: ControlClass) -> Single """
        ...

    @property
    def OldWidth(self) -> Single:
        """ Get: OldWidth(self: ControlClass) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ControlClass) -> object """
        ...

    @property
    def RowSource(self) -> str:
        """
        Get: RowSource(self: ControlClass) -> str
        Set: RowSource(self: ControlClass) = value
        """
        ...

    @property
    def RowSourceType(self) -> Int16:
        """
        Get: RowSourceType(self: ControlClass) -> Int16
        Set: RowSourceType(self: ControlClass) = value
        """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: ControlClass) -> Int16
        Set: TabIndex(self: ControlClass) = value
        """
        ...

    @property
    def TabStop(self) -> bool:
        """
        Get: TabStop(self: ControlClass) -> bool
        Set: TabStop(self: ControlClass) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: ControlClass) -> str
        Set: Tag(self: ControlClass) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: ControlClass) -> Single
        Set: Top(self: ControlClass) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: ControlClass) -> bool
        Set: Visible(self: ControlClass) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: ControlClass) -> Single
        Set: Width(self: ControlClass) = value
        """
        ...


    def add_AfterUpdate(self): # -> 
        """ add_AfterUpdate(self: ControlClass, : ControlEvents_AfterUpdateEventHandler) """
        ...

    def add_BeforeUpdate(self): # -> 
        """ add_BeforeUpdate(self: ControlClass, : ControlEvents_BeforeUpdateEventHandler) """
        ...

    def add_Enter(self): # -> 
        """ add_Enter(self: ControlClass, : ControlEvents_EnterEventHandler) """
        ...

    def add_Exit(self): # -> 
        """ add_Exit(self: ControlClass, : ControlEvents_ExitEventHandler) """
        ...

    def Move(self, Left:object, Top:object, Width:object, Height:object, Layout:object): # -> 
        """ Move(self: ControlClass, Left: object, Top: object, Width: object, Height: object, Layout: object) """
        ...

    def remove_AfterUpdate(self): # -> 
        """ remove_AfterUpdate(self: ControlClass, : ControlEvents_AfterUpdateEventHandler) """
        ...

    def remove_BeforeUpdate(self): # -> 
        """ remove_BeforeUpdate(self: ControlClass, : ControlEvents_BeforeUpdateEventHandler) """
        ...

    def remove_Enter(self): # -> 
        """ remove_Enter(self: ControlClass, : ControlEvents_EnterEventHandler) """
        ...

    def remove_Exit(self): # -> 
        """ remove_Exit(self: ControlClass, : ControlEvents_ExitEventHandler) """
        ...

    def Select(self, SelectInGroup:bool): # -> 
        """ Select(self: ControlClass, SelectInGroup: bool) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: ControlClass) """
        ...

    def ZOrder(self, zPosition:object): # -> 
        """ ZOrder(self: ControlClass, zPosition: object) """
        ...

    def _GetHeight(self, Height) -> int:
        """ _GetHeight(self: ControlClass) -> int """
        ...

    def _GethWnd(self) -> int:
        """ _GethWnd(self: ControlClass) -> int """
        ...

    def _GetID(self) -> int:
        """ _GetID(self: ControlClass) -> int """
        ...

    def _GetLeft(self, Left) -> int:
        """ _GetLeft(self: ControlClass) -> int """
        ...

    def _GetOldHeight(self, OldHeight) -> int:
        """ _GetOldHeight(self: ControlClass) -> int """
        ...

    def _GetOldLeft(self, OldLeft) -> int:
        """ _GetOldLeft(self: ControlClass) -> int """
        ...

    def _GetOldTop(self, OldTop) -> int:
        """ _GetOldTop(self: ControlClass) -> int """
        ...

    def _GetOldWidth(self, OldWidth) -> int:
        """ _GetOldWidth(self: ControlClass) -> int """
        ...

    def _GetTop(self, Top) -> int:
        """ _GetTop(self: ControlClass) -> int """
        ...

    def _GetWidth(self, Width) -> int:
        """ _GetWidth(self: ControlClass) -> int """
        ...

    def _Move(self, Left:int, Top:int, Width:int, Height:int): # -> 
        """ _Move(self: ControlClass, Left: int, Top: int, Width: int, Height: int) """
        ...

    def _SetHeight(self, Height:int): # -> 
        """ _SetHeight(self: ControlClass, Height: int) """
        ...

    def _SetLeft(self, Left:int): # -> 
        """ _SetLeft(self: ControlClass, Left: int) """
        ...

    def _SetTop(self, Top:int): # -> 
        """ _SetTop(self: ControlClass, Top: int) """
        ...

    def _SetWidth(self, Width:int): # -> 
        """ _SetWidth(self: ControlClass, Width: int) """
        ...

    def _ZOrder(self, zPosition:fmZOrder): # -> 
        """ _ZOrder(self: ControlClass, zPosition: fmZOrder) """
        ...

    AfterUpdate = ...
    BeforeUpdate = ...
    Enter = ...
    Exit = ...


class ControlEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AfterUpdate(self): # -> 
        """ AfterUpdate(self: ControlEvents) """
        ...

    def BeforeUpdate(self, Cancel:ReturnBoolean): # -> 
        """ BeforeUpdate(self: ControlEvents, Cancel: ReturnBoolean) """
        ...

    def Enter(self): # -> 
        """ Enter(self: ControlEvents) """
        ...

    def Exit(self, Cancel:ReturnBoolean): # -> 
        """ Exit(self: ControlEvents, Cancel: ReturnBoolean) """
        ...


class ControlEvents_AfterUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ControlEvents_AfterUpdateEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ControlEvents_AfterUpdateEventHandler) """
        ...


class ControlEvents_BeforeUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ControlEvents_BeforeUpdateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: ControlEvents_BeforeUpdateEventHandler, Cancel: ReturnBoolean) """
        ...


class ControlEvents_EnterEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ControlEvents_EnterEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ControlEvents_EnterEventHandler) """
        ...


class ControlEvents_ExitEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ControlEvents_ExitEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: ControlEvents_ExitEventHandler, Cancel: ReturnBoolean) """
        ...


class ControlEvents_SinkHelper(ControlEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_AfterUpdateDelegate = ...
    m_BeforeUpdateDelegate = ...
    m_dwCookie = ...
    m_EnterDelegate = ...
    m_ExitDelegate = ...


class Controls(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Controls) -> int """
        ...


    def Add(self, bstrProgID:str, Name:object, Visible:object) -> Control:
        """ Add(self: Controls, bstrProgID: str, Name: object, Visible: object) -> Control """
        ...

    def AlignToGrid(self): # -> 
        """ AlignToGrid(self: Controls) """
        ...

    def BringForward(self): # -> 
        """ BringForward(self: Controls) """
        ...

    def BringToFront(self): # -> 
        """ BringToFront(self: Controls) """
        ...

    def Clear(self): # -> 
        """ Clear(self: Controls) """
        ...

    def Copy(self): # -> 
        """ Copy(self: Controls) """
        ...

    def Cut(self): # -> 
        """ Cut(self: Controls) """
        ...

    def Enum(self) -> object:
        """ Enum(self: Controls) -> object """
        ...

    def Item(self, varg:object) -> object:
        """ Item(self: Controls, varg: object) -> object """
        ...

    def Move(self, cx:Single, cy:Single): # -> 
        """ Move(self: Controls, cx: Single, cy: Single) """
        ...

    def Remove(self, varg:object): # -> 
        """ Remove(self: Controls, varg: object) """
        ...

    def SelectAll(self): # -> 
        """ SelectAll(self: Controls) """
        ...

    def SendBackward(self): # -> 
        """ SendBackward(self: Controls) """
        ...

    def SendToBack(self): # -> 
        """ SendToBack(self: Controls) """
        ...

    def _AddByClass(self, clsid:int) -> Tuple_[Control, int]:
        """ _AddByClass(self: Controls, clsid: int) -> (Control, int) """
        ...

    def _GetItemByID(self, ID:int) -> Control:
        """ _GetItemByID(self: Controls, ID: int) -> Control """
        ...

    def _GetItemByIndex(self, lIndex:int) -> Control:
        """ _GetItemByIndex(self: Controls, lIndex: int) -> Control """
        ...

    def _GetItemByName(self, pstr:str) -> Control:
        """ _GetItemByName(self: Controls, pstr: str) -> Control """
        ...

    def _Move(self, cx:int, cy:int): # -> 
        """ _Move(self: Controls, cx: int, cy: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class IDataAutoWrapper: # skipped bases: <type 'object'>
    """ no doc """
    def Clear(self): # -> 
        """ Clear(self: IDataAutoWrapper) """
        ...

    def GetFormat(self, Format:object) -> bool:
        """ GetFormat(self: IDataAutoWrapper, Format: object) -> bool """
        ...

    def GetFromClipboard(self): # -> 
        """ GetFromClipboard(self: IDataAutoWrapper) """
        ...

    def GetText(self, Format:object) -> str:
        """ GetText(self: IDataAutoWrapper, Format: object) -> str """
        ...

    def PutInClipboard(self): # -> 
        """ PutInClipboard(self: IDataAutoWrapper) """
        ...

    def SetText(self, Text:str, Format:object): # -> 
        """ SetText(self: IDataAutoWrapper, Text: str, Format: object) """
        ...

    def StartDrag(self, OKEffect:object) -> fmDropEffect:
        """ StartDrag(self: IDataAutoWrapper, OKEffect: object) -> fmDropEffect """
        ...


class DataObject(IDataAutoWrapper): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DataObjectClass(DataObject, __ComObject): # skipped bases: <type 'IDataAutoWrapper'>, <type 'object'>
    """ DataObjectClass() """
    def Clear(self): # -> 
        """ Clear(self: DataObjectClass) """
        ...

    def GetFormat(self, Format:object) -> bool:
        """ GetFormat(self: DataObjectClass, Format: object) -> bool """
        ...

    def GetFromClipboard(self): # -> 
        """ GetFromClipboard(self: DataObjectClass) """
        ...

    def GetText(self, Format:object) -> str:
        """ GetText(self: DataObjectClass, Format: object) -> str """
        ...

    def PutInClipboard(self): # -> 
        """ PutInClipboard(self: DataObjectClass) """
        ...

    def SetText(self, Text:str, Format:object): # -> 
        """ SetText(self: DataObjectClass, Text: str, Format: object) """
        ...

    def StartDrag(self, OKEffect:object) -> fmDropEffect:
        """ StartDrag(self: DataObjectClass, OKEffect: object) -> fmDropEffect """
        ...


class fmAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmAction, values: fmActionCopy (1), fmActionCut (0), fmActionDragDrop (3), fmActionPaste (2) """
    fmActionCopy: fmAction = ...
    fmActionCut: fmAction = ...
    fmActionDragDrop: fmAction = ...
    fmActionPaste: fmAction = ...
    value__ = ...


class fmAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmAlignment, values: fmAlignmentLeft (0), fmAlignmentRight (1) """
    fmAlignmentLeft: fmAlignment = ...
    fmAlignmentRight: fmAlignment = ...
    value__ = ...


class fmBackStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmBackStyle, values: fmBackStyleOpaque (1), fmBackStyleTransparent (0) """
    fmBackStyleOpaque: fmBackStyle = ...
    fmBackStyleTransparent: fmBackStyle = ...
    value__ = ...


class fmBorders(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmBorders, values: fmBordersBox (1), fmBordersLeft (2), fmBordersNone (0), fmBordersTop (3) """
    fmBordersBox: fmBorders = ...
    fmBordersLeft: fmBorders = ...
    fmBordersNone: fmBorders = ...
    fmBordersTop: fmBorders = ...
    value__ = ...


class fmBorderStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmBorderStyle, values: fmBorderStyleNone (0), fmBorderStyleSingle (1) """
    fmBorderStyleNone: fmBorderStyle = ...
    fmBorderStyleSingle: fmBorderStyle = ...
    value__ = ...


class fmButtonEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmButtonEffect, values: fmButtonEffectFlat (0), fmButtonEffectSunken (2) """
    fmButtonEffectFlat: fmButtonEffect = ...
    fmButtonEffectSunken: fmButtonEffect = ...
    value__ = ...


class fmButtonStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmButtonStyle, values: fmButtonStylePushButton (0), fmButtonStyleToggleButton (1) """
    fmButtonStylePushButton: fmButtonStyle = ...
    fmButtonStyleToggleButton: fmButtonStyle = ...
    value__ = ...


class fmCycle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmCycle, values: fmCycleAllForms (0), fmCycleCurrentForm (2) """
    fmCycleAllForms: fmCycle = ...
    fmCycleCurrentForm: fmCycle = ...
    value__ = ...


class fmDisplayStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmDisplayStyle, values: fmDisplayStyleCheckBox (4), fmDisplayStyleCombo (3), fmDisplayStyleDropList (7), fmDisplayStyleList (2), fmDisplayStyleOptionButton (5), fmDisplayStyleText (1), fmDisplayStyleToggle (6) """
    fmDisplayStyleCheckBox: fmDisplayStyle = ...
    fmDisplayStyleCombo: fmDisplayStyle = ...
    fmDisplayStyleDropList: fmDisplayStyle = ...
    fmDisplayStyleList: fmDisplayStyle = ...
    fmDisplayStyleOptionButton: fmDisplayStyle = ...
    fmDisplayStyleText: fmDisplayStyle = ...
    fmDisplayStyleToggle: fmDisplayStyle = ...
    value__ = ...


class fmDragBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmDragBehavior, values: fmDragBehaviorDisabled (0), fmDragBehaviorEnabled (1) """
    fmDragBehaviorDisabled: fmDragBehavior = ...
    fmDragBehaviorEnabled: fmDragBehavior = ...
    value__ = ...


class fmDragState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmDragState, values: fmDragStateEnter (0), fmDragStateLeave (1), fmDragStateOver (2) """
    fmDragStateEnter: fmDragState = ...
    fmDragStateLeave: fmDragState = ...
    fmDragStateOver: fmDragState = ...
    value__ = ...


class fmDropButtonStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmDropButtonStyle, values: fmDropButtonStyleArrow (1), fmDropButtonStyleEllipsis (2), fmDropButtonStylePlain (0), fmDropButtonStyleReduce (3) """
    fmDropButtonStyleArrow: fmDropButtonStyle = ...
    fmDropButtonStyleEllipsis: fmDropButtonStyle = ...
    fmDropButtonStylePlain: fmDropButtonStyle = ...
    fmDropButtonStyleReduce: fmDropButtonStyle = ...
    value__ = ...


class fmDropEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmDropEffect, values: fmDropEffectCopy (1), fmDropEffectCopyOrMove (3), fmDropEffectMove (2), fmDropEffectNone (0) """
    fmDropEffectCopy: fmDropEffect = ...
    fmDropEffectCopyOrMove: fmDropEffect = ...
    fmDropEffectMove: fmDropEffect = ...
    fmDropEffectNone: fmDropEffect = ...
    value__ = ...


class fmEnAutoSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmEnAutoSize, values: _fmEnAutoSizeBoth (3), _fmEnAutoSizeHorizontal (1), _fmEnAutoSizeNone (0), _fmEnAutoSizeVertical (2) """
    value__ = ...
    _fmEnAutoSizeBoth: fmEnAutoSize = ...
    _fmEnAutoSizeHorizontal: fmEnAutoSize = ...
    _fmEnAutoSizeNone: fmEnAutoSize = ...
    _fmEnAutoSizeVertical: fmEnAutoSize = ...


class fmEnterFieldBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmEnterFieldBehavior, values: fmEnterFieldBehaviorRecallSelection (1), fmEnterFieldBehaviorSelectAll (0) """
    fmEnterFieldBehaviorRecallSelection: fmEnterFieldBehavior = ...
    fmEnterFieldBehaviorSelectAll: fmEnterFieldBehavior = ...
    value__ = ...


class fmIMEMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmIMEMode, values: fmIMEModeAlpha (8), fmIMEModeAlphaFull (7), fmIMEModeDisable (3), fmIMEModeHangul (10), fmIMEModeHangulFull (9), fmIMEModeHanzi (12), fmIMEModeHanziFull (11), fmIMEModeHiragana (4), fmIMEModeKatakana (5), fmIMEModeKatakanaHalf (6), fmIMEModeNoControl (0), fmIMEModeOff (2), fmIMEModeOn (1) """
    fmIMEModeAlpha: fmIMEMode = ...
    fmIMEModeAlphaFull: fmIMEMode = ...
    fmIMEModeDisable: fmIMEMode = ...
    fmIMEModeHangul: fmIMEMode = ...
    fmIMEModeHangulFull: fmIMEMode = ...
    fmIMEModeHanzi: fmIMEMode = ...
    fmIMEModeHanziFull: fmIMEMode = ...
    fmIMEModeHiragana: fmIMEMode = ...
    fmIMEModeKatakana: fmIMEMode = ...
    fmIMEModeKatakanaHalf: fmIMEMode = ...
    fmIMEModeNoControl: fmIMEMode = ...
    fmIMEModeOff: fmIMEMode = ...
    fmIMEModeOn: fmIMEMode = ...
    value__ = ...


class fmLayoutEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmLayoutEffect, values: _fmLayoutEffectRespond (2), fmLayoutEffectInitiate (1), fmLayoutEffectNone (0) """
    fmLayoutEffectInitiate: fmLayoutEffect = ...
    fmLayoutEffectNone: fmLayoutEffect = ...
    value__ = ...
    _fmLayoutEffectRespond: fmLayoutEffect = ...


class fmListBoxStyles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmListBoxStyles, values: _fmListBoxStylesComboBox (2), _fmListBoxStylesListBox (1), _fmListBoxStylesNone (0) """
    value__ = ...
    _fmListBoxStylesComboBox: fmListBoxStyles = ...
    _fmListBoxStylesListBox: fmListBoxStyles = ...
    _fmListBoxStylesNone: fmListBoxStyles = ...


class fmListStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmListStyle, values: fmListStyleOption (1), fmListStylePlain (0) """
    fmListStyleOption: fmListStyle = ...
    fmListStylePlain: fmListStyle = ...
    value__ = ...


class fmMatchEntry(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmMatchEntry, values: fmMatchEntryComplete (1), fmMatchEntryFirstLetter (0), fmMatchEntryNone (2) """
    fmMatchEntryComplete: fmMatchEntry = ...
    fmMatchEntryFirstLetter: fmMatchEntry = ...
    fmMatchEntryNone: fmMatchEntry = ...
    value__ = ...


class fmMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmMode, values: fmModeInherit (-2), fmModeOff (0), fmModeOn (-1) """
    fmModeInherit: fmMode = ...
    fmModeOff: fmMode = ...
    fmModeOn: fmMode = ...
    value__ = ...


class fmMousePointer(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmMousePointer, values: fmMousePointerAppStarting (13), fmMousePointerArrow (1), fmMousePointerCross (2), fmMousePointerCustom (99), fmMousePointerDefault (0), fmMousePointerHelp (14), fmMousePointerHourGlass (11), fmMousePointerIBeam (3), fmMousePointerNoDrop (12), fmMousePointerSizeAll (15), fmMousePointerSizeNESW (6), fmMousePointerSizeNS (7), fmMousePointerSizeNWSE (8), fmMousePointerSizeWE (9), fmMousePointerUpArrow (10) """
    fmMousePointerAppStarting: fmMousePointer = ...
    fmMousePointerArrow: fmMousePointer = ...
    fmMousePointerCross: fmMousePointer = ...
    fmMousePointerCustom: fmMousePointer = ...
    fmMousePointerDefault: fmMousePointer = ...
    fmMousePointerHelp: fmMousePointer = ...
    fmMousePointerHourGlass: fmMousePointer = ...
    fmMousePointerIBeam: fmMousePointer = ...
    fmMousePointerNoDrop: fmMousePointer = ...
    fmMousePointerSizeAll: fmMousePointer = ...
    fmMousePointerSizeNESW: fmMousePointer = ...
    fmMousePointerSizeNS: fmMousePointer = ...
    fmMousePointerSizeNWSE: fmMousePointer = ...
    fmMousePointerSizeWE: fmMousePointer = ...
    fmMousePointerUpArrow: fmMousePointer = ...
    value__ = ...


class fmMultiSelect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmMultiSelect, values: fmMultiSelectExtended (2), fmMultiSelectMulti (1), fmMultiSelectSingle (0) """
    fmMultiSelectExtended: fmMultiSelect = ...
    fmMultiSelectMulti: fmMultiSelect = ...
    fmMultiSelectSingle: fmMultiSelect = ...
    value__ = ...


class fmOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmOrientation, values: fmOrientationAuto (-1), fmOrientationHorizontal (1), fmOrientationVertical (0) """
    fmOrientationAuto: fmOrientation = ...
    fmOrientationHorizontal: fmOrientation = ...
    fmOrientationVertical: fmOrientation = ...
    value__ = ...


class fmPicPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmPicPosition, values: fmPicPositionBottomCenter (7), fmPicPositionBottomLeft (6), fmPicPositionBottomRight (8), fmPicPositionCenter (0), fmPicPositionCenterLeft (4), fmPicPositionCenterRight (5), fmPicPositionTopCenter (2), fmPicPositionTopLeft (1), fmPicPositionTopRight (3) """
    fmPicPositionBottomCenter: fmPicPosition = ...
    fmPicPositionBottomLeft: fmPicPosition = ...
    fmPicPositionBottomRight: fmPicPosition = ...
    fmPicPositionCenter: fmPicPosition = ...
    fmPicPositionCenterLeft: fmPicPosition = ...
    fmPicPositionCenterRight: fmPicPosition = ...
    fmPicPositionTopCenter: fmPicPosition = ...
    fmPicPositionTopLeft: fmPicPosition = ...
    fmPicPositionTopRight: fmPicPosition = ...
    value__ = ...


class fmPictureAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmPictureAlignment, values: fmPictureAlignmentBottomLeft (3), fmPictureAlignmentBottomRight (4), fmPictureAlignmentCenter (2), fmPictureAlignmentTopLeft (0), fmPictureAlignmentTopRight (1) """
    fmPictureAlignmentBottomLeft: fmPictureAlignment = ...
    fmPictureAlignmentBottomRight: fmPictureAlignment = ...
    fmPictureAlignmentCenter: fmPictureAlignment = ...
    fmPictureAlignmentTopLeft: fmPictureAlignment = ...
    fmPictureAlignmentTopRight: fmPictureAlignment = ...
    value__ = ...


class fmPicturePosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmPicturePosition, values: fmPicturePositionAboveCenter (7), fmPicturePositionAboveLeft (6), fmPicturePositionAboveRight (8), fmPicturePositionBelowCenter (10), fmPicturePositionBelowLeft (9), fmPicturePositionBelowRight (11), fmPicturePositionCenter (12), fmPicturePositionLeftBottom (2), fmPicturePositionLeftCenter (1), fmPicturePositionLeftTop (0), fmPicturePositionRightBottom (5), fmPicturePositionRightCenter (4), fmPicturePositionRightTop (3) """
    fmPicturePositionAboveCenter: fmPicturePosition = ...
    fmPicturePositionAboveLeft: fmPicturePosition = ...
    fmPicturePositionAboveRight: fmPicturePosition = ...
    fmPicturePositionBelowCenter: fmPicturePosition = ...
    fmPicturePositionBelowLeft: fmPicturePosition = ...
    fmPicturePositionBelowRight: fmPicturePosition = ...
    fmPicturePositionCenter: fmPicturePosition = ...
    fmPicturePositionLeftBottom: fmPicturePosition = ...
    fmPicturePositionLeftCenter: fmPicturePosition = ...
    fmPicturePositionLeftTop: fmPicturePosition = ...
    fmPicturePositionRightBottom: fmPicturePosition = ...
    fmPicturePositionRightCenter: fmPicturePosition = ...
    fmPicturePositionRightTop: fmPicturePosition = ...
    value__ = ...


class fmPictureSizeMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmPictureSizeMode, values: fmPictureSizeModeClip (0), fmPictureSizeModeStretch (1), fmPictureSizeModeZoom (3) """
    fmPictureSizeModeClip: fmPictureSizeMode = ...
    fmPictureSizeModeStretch: fmPictureSizeMode = ...
    fmPictureSizeModeZoom: fmPictureSizeMode = ...
    value__ = ...


class fmRepeatDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmRepeatDirection, values: _fmRepeatDirectionHorizontal (0), _fmRepeatDirectionVertical (1) """
    value__ = ...
    _fmRepeatDirectionHorizontal: fmRepeatDirection = ...
    _fmRepeatDirectionVertical: fmRepeatDirection = ...


class fmScrollAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmScrollAction, values: _fmScrollActionAbsoluteChange (7), fmScrollActionBegin (5), fmScrollActionControlRequest (9), fmScrollActionEnd (6), fmScrollActionFocusRequest (10), fmScrollActionLineDown (2), fmScrollActionLineUp (1), fmScrollActionNoChange (0), fmScrollActionPageDown (4), fmScrollActionPageUp (3), fmScrollActionPropertyChange (8) """
    fmScrollActionBegin: fmScrollAction = ...
    fmScrollActionControlRequest: fmScrollAction = ...
    fmScrollActionEnd: fmScrollAction = ...
    fmScrollActionFocusRequest: fmScrollAction = ...
    fmScrollActionLineDown: fmScrollAction = ...
    fmScrollActionLineUp: fmScrollAction = ...
    fmScrollActionNoChange: fmScrollAction = ...
    fmScrollActionPageDown: fmScrollAction = ...
    fmScrollActionPageUp: fmScrollAction = ...
    fmScrollActionPropertyChange: fmScrollAction = ...
    value__ = ...
    _fmScrollActionAbsoluteChange: fmScrollAction = ...


class fmScrollBars(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmScrollBars, values: fmScrollBarsBoth (3), fmScrollBarsHorizontal (1), fmScrollBarsNone (0), fmScrollBarsVertical (2) """
    fmScrollBarsBoth: fmScrollBars = ...
    fmScrollBarsHorizontal: fmScrollBars = ...
    fmScrollBarsNone: fmScrollBars = ...
    fmScrollBarsVertical: fmScrollBars = ...
    value__ = ...


class fmShowDropButtonWhen(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmShowDropButtonWhen, values: fmShowDropButtonWhenAlways (2), fmShowDropButtonWhenFocus (1), fmShowDropButtonWhenNever (0) """
    fmShowDropButtonWhenAlways: fmShowDropButtonWhen = ...
    fmShowDropButtonWhenFocus: fmShowDropButtonWhen = ...
    fmShowDropButtonWhenNever: fmShowDropButtonWhen = ...
    value__ = ...


class fmShowListWhen(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmShowListWhen, values: fmShowListWhenAlways (3), fmShowListWhenButton (1), fmShowListWhenFocus (2), fmShowListWhenNever (0) """
    fmShowListWhenAlways: fmShowListWhen = ...
    fmShowListWhenButton: fmShowListWhen = ...
    fmShowListWhenFocus: fmShowListWhen = ...
    fmShowListWhenNever: fmShowListWhen = ...
    value__ = ...


class fmSnapPoint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmSnapPoint, values: fmSnapPointBottomCenter (7), fmSnapPointBottomLeft (6), fmSnapPointBottomRight (8), fmSnapPointCenter (4), fmSnapPointCenterLeft (3), fmSnapPointCenterRight (5), fmSnapPointTopCenter (1), fmSnapPointTopLeft (0), fmSnapPointTopRight (2) """
    fmSnapPointBottomCenter: fmSnapPoint = ...
    fmSnapPointBottomLeft: fmSnapPoint = ...
    fmSnapPointBottomRight: fmSnapPoint = ...
    fmSnapPointCenter: fmSnapPoint = ...
    fmSnapPointCenterLeft: fmSnapPoint = ...
    fmSnapPointCenterRight: fmSnapPoint = ...
    fmSnapPointTopCenter: fmSnapPoint = ...
    fmSnapPointTopLeft: fmSnapPoint = ...
    fmSnapPointTopRight: fmSnapPoint = ...
    value__ = ...


class fmSpecialEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmSpecialEffect, values: fmSpecialEffectBump (6), fmSpecialEffectEtched (3), fmSpecialEffectFlat (0), fmSpecialEffectRaised (1), fmSpecialEffectSunken (2) """
    fmSpecialEffectBump: fmSpecialEffect = ...
    fmSpecialEffectEtched: fmSpecialEffect = ...
    fmSpecialEffectFlat: fmSpecialEffect = ...
    fmSpecialEffectRaised: fmSpecialEffect = ...
    fmSpecialEffectSunken: fmSpecialEffect = ...
    value__ = ...


class fmStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmStyle, values: fmStyleDropDownCombo (0), fmStyleDropDownList (2) """
    fmStyleDropDownCombo: fmStyle = ...
    fmStyleDropDownList: fmStyle = ...
    value__ = ...


class fmTabOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmTabOrientation, values: fmTabOrientationBottom (1), fmTabOrientationLeft (2), fmTabOrientationRight (3), fmTabOrientationTop (0) """
    fmTabOrientationBottom: fmTabOrientation = ...
    fmTabOrientationLeft: fmTabOrientation = ...
    fmTabOrientationRight: fmTabOrientation = ...
    fmTabOrientationTop: fmTabOrientation = ...
    value__ = ...


class fmTabStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmTabStyle, values: fmTabStyleButtons (1), fmTabStyleNone (2), fmTabStyleTabs (0) """
    fmTabStyleButtons: fmTabStyle = ...
    fmTabStyleNone: fmTabStyle = ...
    fmTabStyleTabs: fmTabStyle = ...
    value__ = ...


class fmTextAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmTextAlign, values: fmTextAlignCenter (2), fmTextAlignLeft (1), fmTextAlignRight (3) """
    fmTextAlignCenter: fmTextAlign = ...
    fmTextAlignLeft: fmTextAlign = ...
    fmTextAlignRight: fmTextAlign = ...
    value__ = ...


class fmTransitionEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmTransitionEffect, values: fmTransitionEffectCoverDown (5), fmTransitionEffectCoverLeft (7), fmTransitionEffectCoverLeftDown (6), fmTransitionEffectCoverLeftUp (8), fmTransitionEffectCoverRight (3), fmTransitionEffectCoverRightDown (4), fmTransitionEffectCoverRightUp (2), fmTransitionEffectCoverUp (1), fmTransitionEffectNone (0), fmTransitionEffectPushDown (11), fmTransitionEffectPushLeft (12), fmTransitionEffectPushRight (10), fmTransitionEffectPushUp (9) """
    fmTransitionEffectCoverDown: fmTransitionEffect = ...
    fmTransitionEffectCoverLeft: fmTransitionEffect = ...
    fmTransitionEffectCoverLeftDown: fmTransitionEffect = ...
    fmTransitionEffectCoverLeftUp: fmTransitionEffect = ...
    fmTransitionEffectCoverRight: fmTransitionEffect = ...
    fmTransitionEffectCoverRightDown: fmTransitionEffect = ...
    fmTransitionEffectCoverRightUp: fmTransitionEffect = ...
    fmTransitionEffectCoverUp: fmTransitionEffect = ...
    fmTransitionEffectNone: fmTransitionEffect = ...
    fmTransitionEffectPushDown: fmTransitionEffect = ...
    fmTransitionEffectPushLeft: fmTransitionEffect = ...
    fmTransitionEffectPushRight: fmTransitionEffect = ...
    fmTransitionEffectPushUp: fmTransitionEffect = ...
    value__ = ...


class fmVerticalScrollBarSide(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmVerticalScrollBarSide, values: fmVerticalScrollBarSideLeft (1), fmVerticalScrollBarSideRight (0) """
    fmVerticalScrollBarSideLeft: fmVerticalScrollBarSide = ...
    fmVerticalScrollBarSideRight: fmVerticalScrollBarSide = ...
    value__ = ...


class fmZOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum fmZOrder, values: fmZOrderBack (1), fmZOrderFront (0) """
    fmZOrderBack: fmZOrder = ...
    fmZOrderFront: fmZOrder = ...
    value__ = ...


class Font: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bold(self) -> bool:
        """
        Get: Bold(self: Font) -> bool
        Set: Bold(self: Font) = value
        """
        ...

    @property
    def Charset(self) -> Int16:
        """
        Get: Charset(self: Font) -> Int16
        Set: Charset(self: Font) = value
        """
        ...

    @property
    def Italic(self) -> bool:
        """
        Get: Italic(self: Font) -> bool
        Set: Italic(self: Font) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Font) -> str
        Set: Name(self: Font) = value
        """
        ...

    @property
    def Size(self) -> Decimal:
        """
        Get: Size(self: Font) -> Decimal
        Set: Size(self: Font) = value
        """
        ...

    @property
    def Strikethrough(self) -> bool:
        """
        Get: Strikethrough(self: Font) -> bool
        Set: Strikethrough(self: Font) = value
        """
        ...

    @property
    def Underline(self) -> bool:
        """
        Get: Underline(self: Font) -> bool
        Set: Underline(self: Font) = value
        """
        ...

    @property
    def Weight(self) -> Int16:
        """
        Get: Weight(self: Font) -> Int16
        Set: Weight(self: Font) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class FormEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AddControl(self, Control:Control): # -> 
        """ AddControl(self: FormEvents, Control: Control) """
        ...

    def BeforeDragOver(self, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: FormEvents, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: FormEvents, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Click(self): # -> 
        """ Click(self: FormEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: FormEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: FormEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: FormEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: FormEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: FormEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def Layout(self): # -> 
        """ Layout(self: FormEvents) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: FormEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: FormEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: FormEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def RemoveControl(self, Control:Control): # -> 
        """ RemoveControl(self: FormEvents, Control: Control) """
        ...

    def Scroll(self, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Scroll(self: FormEvents, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...

    def Zoom(self, Percent) -> Int16:
        """ Zoom(self: FormEvents) -> Int16 """
        ...


class FormEvents_AddControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_AddControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Control:Control): # -> 
        """ Invoke(self: FormEvents_AddControlEventHandler, Control: Control) """
        ...


class FormEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: FormEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class FormEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: FormEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class FormEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: FormEvents_ClickEventHandler) """
        ...


class FormEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: FormEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class FormEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: FormEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class FormEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AddControl(self): # -> 
        """ add_AddControl(self: FormEvents_Event, : FormEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: FormEvents_Event, : FormEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: FormEvents_Event, : FormEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: FormEvents_Event, : FormEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: FormEvents_Event, : FormEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: FormEvents_Event, : FormEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: FormEvents_Event, : FormEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: FormEvents_Event, : FormEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: FormEvents_Event, : FormEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: FormEvents_Event, : FormEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: FormEvents_Event, : FormEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: FormEvents_Event, : FormEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: FormEvents_Event, : FormEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: FormEvents_Event, : FormEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: FormEvents_Event, : FormEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: FormEvents_Event, : FormEvents_ZoomEventHandler) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: FormEvents_Event, : FormEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: FormEvents_Event, : FormEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: FormEvents_Event, : FormEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: FormEvents_Event, : FormEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: FormEvents_Event, : FormEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: FormEvents_Event, : FormEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: FormEvents_Event, : FormEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: FormEvents_Event, : FormEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: FormEvents_Event, : FormEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: FormEvents_Event, : FormEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: FormEvents_Event, : FormEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: FormEvents_Event, : FormEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: FormEvents_Event, : FormEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: FormEvents_Event, : FormEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: FormEvents_Event, : FormEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: FormEvents_Event, : FormEvents_ZoomEventHandler) """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    RemoveControl = ...
    Scroll = ...
    Zoom = ...


class FormEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: FormEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class FormEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: FormEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class FormEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: FormEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class FormEvents_LayoutEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_LayoutEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: FormEvents_LayoutEventHandler) """
        ...


class FormEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: FormEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class FormEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: FormEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class FormEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: FormEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class FormEvents_RemoveControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_RemoveControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Control:Control): # -> 
        """ Invoke(self: FormEvents_RemoveControlEventHandler, Control: Control) """
        ...


class FormEvents_ScrollEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_ScrollEventHandler(: object, : UIntPtr) """
    def Invoke(self, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Invoke(self: FormEvents_ScrollEventHandler, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...


class FormEvents_SinkHelper(FormEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_AddControlDelegate = ...
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_LayoutDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...
    m_RemoveControlDelegate = ...
    m_ScrollDelegate = ...
    m_ZoomDelegate = ...


class FormEvents_ZoomEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormEvents_ZoomEventHandler(: object, : UIntPtr) """
    def Invoke(self, Percent) -> Int16:
        """ Invoke(self: FormEvents_ZoomEventHandler) -> Int16 """
        ...


class IOptionFrame: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveControl(self) -> Control:
        """ Get: ActiveControl(self: IOptionFrame) -> Control """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IOptionFrame) -> int
        Set: BackColor(self: IOptionFrame) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: IOptionFrame) -> int
        Set: BorderColor(self: IOptionFrame) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: IOptionFrame) -> fmBorderStyle
        Set: BorderStyle(self: IOptionFrame) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: IOptionFrame) -> bool """
        ...

    @property
    def CanRedo(self) -> bool:
        """ Get: CanRedo(self: IOptionFrame) -> bool """
        ...

    @property
    def CanUndo(self) -> bool:
        """ Get: CanUndo(self: IOptionFrame) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IOptionFrame) -> str
        Set: Caption(self: IOptionFrame) = value
        """
        ...

    @property
    def Controls(self) -> Controls:
        """ Get: Controls(self: IOptionFrame) -> Controls """
        ...

    @property
    def Cycle(self) -> fmCycle:
        """
        Get: Cycle(self: IOptionFrame) -> fmCycle
        Set: Cycle(self: IOptionFrame) = value
        """
        ...

    @property
    def DesignMode(self) -> fmMode:
        """
        Get: DesignMode(self: IOptionFrame) -> fmMode
        Set: DesignMode(self: IOptionFrame) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IOptionFrame) -> bool
        Set: Enabled(self: IOptionFrame) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IOptionFrame) -> NewFont
        Set: Font(self: IOptionFrame) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IOptionFrame) -> int
        Set: ForeColor(self: IOptionFrame) = value
        """
        ...

    @property
    def GridX(self) -> Single:
        """
        Get: GridX(self: IOptionFrame) -> Single
        Set: GridX(self: IOptionFrame) = value
        """
        ...

    @property
    def GridY(self) -> Single:
        """
        Get: GridY(self: IOptionFrame) -> Single
        Set: GridY(self: IOptionFrame) = value
        """
        ...

    @property
    def InsideHeight(self) -> Single:
        """ Get: InsideHeight(self: IOptionFrame) -> Single """
        ...

    @property
    def InsideWidth(self) -> Single:
        """ Get: InsideWidth(self: IOptionFrame) -> Single """
        ...

    @property
    def KeepScrollBarsVisible(self) -> fmScrollBars:
        """
        Get: KeepScrollBarsVisible(self: IOptionFrame) -> fmScrollBars
        Set: KeepScrollBarsVisible(self: IOptionFrame) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IOptionFrame) -> StdPicture
        Set: MouseIcon(self: IOptionFrame) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IOptionFrame) -> fmMousePointer
        Set: MousePointer(self: IOptionFrame) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: IOptionFrame) -> StdPicture
        Set: Picture(self: IOptionFrame) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: IOptionFrame) -> fmPictureAlignment
        Set: PictureAlignment(self: IOptionFrame) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: IOptionFrame) -> fmPictureSizeMode
        Set: PictureSizeMode(self: IOptionFrame) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: IOptionFrame) -> bool
        Set: PictureTiling(self: IOptionFrame) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: IOptionFrame) -> fmScrollBars
        Set: ScrollBars(self: IOptionFrame) = value
        """
        ...

    @property
    def ScrollHeight(self) -> Single:
        """
        Get: ScrollHeight(self: IOptionFrame) -> Single
        Set: ScrollHeight(self: IOptionFrame) = value
        """
        ...

    @property
    def ScrollLeft(self) -> Single:
        """
        Get: ScrollLeft(self: IOptionFrame) -> Single
        Set: ScrollLeft(self: IOptionFrame) = value
        """
        ...

    @property
    def ScrollTop(self) -> Single:
        """
        Get: ScrollTop(self: IOptionFrame) -> Single
        Set: ScrollTop(self: IOptionFrame) = value
        """
        ...

    @property
    def ScrollWidth(self) -> Single:
        """
        Get: ScrollWidth(self: IOptionFrame) -> Single
        Set: ScrollWidth(self: IOptionFrame) = value
        """
        ...

    @property
    def Selected(self) -> Controls:
        """ Get: Selected(self: IOptionFrame) -> Controls """
        ...

    @property
    def ShowGridDots(self) -> fmMode:
        """
        Get: ShowGridDots(self: IOptionFrame) -> fmMode
        Set: ShowGridDots(self: IOptionFrame) = value
        """
        ...

    @property
    def ShowToolbox(self) -> fmMode:
        """
        Get: ShowToolbox(self: IOptionFrame) -> fmMode
        Set: ShowToolbox(self: IOptionFrame) = value
        """
        ...

    @property
    def SnapToGrid(self) -> fmMode:
        """
        Get: SnapToGrid(self: IOptionFrame) -> fmMode
        Set: SnapToGrid(self: IOptionFrame) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: IOptionFrame) -> fmSpecialEffect
        Set: SpecialEffect(self: IOptionFrame) = value
        """
        ...

    @property
    def VerticalScrollBarSide(self) -> fmVerticalScrollBarSide:
        """
        Get: VerticalScrollBarSide(self: IOptionFrame) -> fmVerticalScrollBarSide
        Set: VerticalScrollBarSide(self: IOptionFrame) = value
        """
        ...

    @property
    def Zoom(self) -> Int16:
        """
        Get: Zoom(self: IOptionFrame) -> Int16
        Set: Zoom(self: IOptionFrame) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IOptionFrame) = value """
        ...


    def Copy(self): # -> 
        """ Copy(self: IOptionFrame) """
        ...

    def Cut(self): # -> 
        """ Cut(self: IOptionFrame) """
        ...

    def Paste(self): # -> 
        """ Paste(self: IOptionFrame) """
        ...

    def RedoAction(self): # -> 
        """ RedoAction(self: IOptionFrame) """
        ...

    def Repaint(self): # -> 
        """ Repaint(self: IOptionFrame) """
        ...

    def Scroll(self, xAction:object, yAction:object): # -> 
        """ Scroll(self: IOptionFrame, xAction: object, yAction: object) """
        ...

    def SetDefaultTabOrder(self): # -> 
        """ SetDefaultTabOrder(self: IOptionFrame) """
        ...

    def UndoAction(self): # -> 
        """ UndoAction(self: IOptionFrame) """
        ...

    def _GetGridX(self, GridX) -> int:
        """ _GetGridX(self: IOptionFrame) -> int """
        ...

    def _GetGridY(self, GridY) -> int:
        """ _GetGridY(self: IOptionFrame) -> int """
        ...

    def _GetInsideHeight(self, InsideHeight) -> int:
        """ _GetInsideHeight(self: IOptionFrame) -> int """
        ...

    def _GetInsideWidth(self, InsideWidth) -> int:
        """ _GetInsideWidth(self: IOptionFrame) -> int """
        ...

    def _GetScrollHeight(self, ScrollHeight) -> int:
        """ _GetScrollHeight(self: IOptionFrame) -> int """
        ...

    def _GetScrollLeft(self, ScrollLeft) -> int:
        """ _GetScrollLeft(self: IOptionFrame) -> int """
        ...

    def _GetScrollTop(self, ScrollTop) -> int:
        """ _GetScrollTop(self: IOptionFrame) -> int """
        ...

    def _GetScrollWidth(self, ScrollWidth) -> int:
        """ _GetScrollWidth(self: IOptionFrame) -> int """
        ...

    def _SetGridX(self, GridX:int): # -> 
        """ _SetGridX(self: IOptionFrame, GridX: int) """
        ...

    def _SetGridY(self, GridY:int): # -> 
        """ _SetGridY(self: IOptionFrame, GridY: int) """
        ...

    def _SetScrollHeight(self, ScrollHeight:int): # -> 
        """ _SetScrollHeight(self: IOptionFrame, ScrollHeight: int) """
        ...

    def _SetScrollLeft(self, ScrollLeft:int): # -> 
        """ _SetScrollLeft(self: IOptionFrame, ScrollLeft: int) """
        ...

    def _SetScrollTop(self, ScrollTop:int): # -> 
        """ _SetScrollTop(self: IOptionFrame, ScrollTop: int) """
        ...

    def _SetScrollWidth(self, ScrollWidth:int): # -> 
        """ _SetScrollWidth(self: IOptionFrame, ScrollWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class OptionFrameEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AddControl(self): # -> 
        """ add_AddControl(self: OptionFrameEvents_Event, : OptionFrameEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: OptionFrameEvents_Event, : OptionFrameEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: OptionFrameEvents_Event, : OptionFrameEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: OptionFrameEvents_Event, : OptionFrameEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: OptionFrameEvents_Event, : OptionFrameEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: OptionFrameEvents_Event, : OptionFrameEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: OptionFrameEvents_Event, : OptionFrameEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: OptionFrameEvents_Event, : OptionFrameEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: OptionFrameEvents_Event, : OptionFrameEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: OptionFrameEvents_Event, : OptionFrameEvents_ZoomEventHandler) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: OptionFrameEvents_Event, : OptionFrameEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: OptionFrameEvents_Event, : OptionFrameEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: OptionFrameEvents_Event, : OptionFrameEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: OptionFrameEvents_Event, : OptionFrameEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: OptionFrameEvents_Event, : OptionFrameEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: OptionFrameEvents_Event, : OptionFrameEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: OptionFrameEvents_Event, : OptionFrameEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: OptionFrameEvents_Event, : OptionFrameEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: OptionFrameEvents_Event, : OptionFrameEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: OptionFrameEvents_Event, : OptionFrameEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: OptionFrameEvents_Event, : OptionFrameEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: OptionFrameEvents_Event, : OptionFrameEvents_ZoomEventHandler) """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    RemoveControl = ...
    Scroll = ...
    Zoom = ...


class Frame(OptionFrameEvents_Event, IOptionFrame): # skipped bases: <type 'object'>
    """ no doc """
    pass

class FrameClass(Frame, __ComObject): # skipped bases: <type 'IOptionFrame'>, <type 'OptionFrameEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def ActiveControl(self) -> Control:
        """ Get: ActiveControl(self: FrameClass) -> Control """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: FrameClass) -> int
        Set: BackColor(self: FrameClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: FrameClass) -> int
        Set: BorderColor(self: FrameClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: FrameClass) -> fmBorderStyle
        Set: BorderStyle(self: FrameClass) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: FrameClass) -> bool """
        ...

    @property
    def CanRedo(self) -> bool:
        """ Get: CanRedo(self: FrameClass) -> bool """
        ...

    @property
    def CanUndo(self) -> bool:
        """ Get: CanUndo(self: FrameClass) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: FrameClass) -> str
        Set: Caption(self: FrameClass) = value
        """
        ...

    @property
    def Controls(self) -> Controls:
        """ Get: Controls(self: FrameClass) -> Controls """
        ...

    @property
    def Cycle(self) -> fmCycle:
        """
        Get: Cycle(self: FrameClass) -> fmCycle
        Set: Cycle(self: FrameClass) = value
        """
        ...

    @property
    def DesignMode(self) -> fmMode:
        """
        Get: DesignMode(self: FrameClass) -> fmMode
        Set: DesignMode(self: FrameClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: FrameClass) -> bool
        Set: Enabled(self: FrameClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: FrameClass) -> NewFont
        Set: Font(self: FrameClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: FrameClass) -> int
        Set: ForeColor(self: FrameClass) = value
        """
        ...

    @property
    def GridX(self) -> Single:
        """
        Get: GridX(self: FrameClass) -> Single
        Set: GridX(self: FrameClass) = value
        """
        ...

    @property
    def GridY(self) -> Single:
        """
        Get: GridY(self: FrameClass) -> Single
        Set: GridY(self: FrameClass) = value
        """
        ...

    @property
    def InsideHeight(self) -> Single:
        """ Get: InsideHeight(self: FrameClass) -> Single """
        ...

    @property
    def InsideWidth(self) -> Single:
        """ Get: InsideWidth(self: FrameClass) -> Single """
        ...

    @property
    def KeepScrollBarsVisible(self) -> fmScrollBars:
        """
        Get: KeepScrollBarsVisible(self: FrameClass) -> fmScrollBars
        Set: KeepScrollBarsVisible(self: FrameClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: FrameClass) -> StdPicture
        Set: MouseIcon(self: FrameClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: FrameClass) -> fmMousePointer
        Set: MousePointer(self: FrameClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: FrameClass) -> StdPicture
        Set: Picture(self: FrameClass) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: FrameClass) -> fmPictureAlignment
        Set: PictureAlignment(self: FrameClass) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: FrameClass) -> fmPictureSizeMode
        Set: PictureSizeMode(self: FrameClass) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: FrameClass) -> bool
        Set: PictureTiling(self: FrameClass) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: FrameClass) -> fmScrollBars
        Set: ScrollBars(self: FrameClass) = value
        """
        ...

    @property
    def ScrollHeight(self) -> Single:
        """
        Get: ScrollHeight(self: FrameClass) -> Single
        Set: ScrollHeight(self: FrameClass) = value
        """
        ...

    @property
    def ScrollLeft(self) -> Single:
        """
        Get: ScrollLeft(self: FrameClass) -> Single
        Set: ScrollLeft(self: FrameClass) = value
        """
        ...

    @property
    def ScrollTop(self) -> Single:
        """
        Get: ScrollTop(self: FrameClass) -> Single
        Set: ScrollTop(self: FrameClass) = value
        """
        ...

    @property
    def ScrollWidth(self) -> Single:
        """
        Get: ScrollWidth(self: FrameClass) -> Single
        Set: ScrollWidth(self: FrameClass) = value
        """
        ...

    @property
    def Selected(self) -> Controls:
        """ Get: Selected(self: FrameClass) -> Controls """
        ...

    @property
    def ShowGridDots(self) -> fmMode:
        """
        Get: ShowGridDots(self: FrameClass) -> fmMode
        Set: ShowGridDots(self: FrameClass) = value
        """
        ...

    @property
    def ShowToolbox(self) -> fmMode:
        """
        Get: ShowToolbox(self: FrameClass) -> fmMode
        Set: ShowToolbox(self: FrameClass) = value
        """
        ...

    @property
    def SnapToGrid(self) -> fmMode:
        """
        Get: SnapToGrid(self: FrameClass) -> fmMode
        Set: SnapToGrid(self: FrameClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: FrameClass) -> fmSpecialEffect
        Set: SpecialEffect(self: FrameClass) = value
        """
        ...

    @property
    def VerticalScrollBarSide(self) -> fmVerticalScrollBarSide:
        """
        Get: VerticalScrollBarSide(self: FrameClass) -> fmVerticalScrollBarSide
        Set: VerticalScrollBarSide(self: FrameClass) = value
        """
        ...

    @property
    def Zoom(self) -> Int16:
        """
        Get: Zoom(self: FrameClass) -> Int16
        Set: Zoom(self: FrameClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: FrameClass) = value """
        ...


    def add_AddControl(self): # -> 
        """ add_AddControl(self: FrameClass, : OptionFrameEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: FrameClass, : OptionFrameEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: FrameClass, : OptionFrameEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: FrameClass, : OptionFrameEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: FrameClass, : OptionFrameEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: FrameClass, : OptionFrameEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: FrameClass, : OptionFrameEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: FrameClass, : OptionFrameEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: FrameClass, : OptionFrameEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: FrameClass, : OptionFrameEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: FrameClass, : OptionFrameEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: FrameClass, : OptionFrameEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: FrameClass, : OptionFrameEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: FrameClass, : OptionFrameEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: FrameClass, : OptionFrameEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: FrameClass, : OptionFrameEvents_ZoomEventHandler) """
        ...

    def Copy(self): # -> 
        """ Copy(self: FrameClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: FrameClass) """
        ...

    def Paste(self): # -> 
        """ Paste(self: FrameClass) """
        ...

    def RedoAction(self): # -> 
        """ RedoAction(self: FrameClass) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: FrameClass, : OptionFrameEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: FrameClass, : OptionFrameEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: FrameClass, : OptionFrameEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: FrameClass, : OptionFrameEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: FrameClass, : OptionFrameEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: FrameClass, : OptionFrameEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: FrameClass, : OptionFrameEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: FrameClass, : OptionFrameEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: FrameClass, : OptionFrameEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: FrameClass, : OptionFrameEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: FrameClass, : OptionFrameEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: FrameClass, : OptionFrameEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: FrameClass, : OptionFrameEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: FrameClass, : OptionFrameEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: FrameClass, : OptionFrameEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: FrameClass, : OptionFrameEvents_ZoomEventHandler) """
        ...

    def Repaint(self): # -> 
        """ Repaint(self: FrameClass) """
        ...

    def Scroll(self, xAction:object, yAction:object): # -> 
        """ Scroll(self: FrameClass, xAction: object, yAction: object) """
        ...

    def SetDefaultTabOrder(self): # -> 
        """ SetDefaultTabOrder(self: FrameClass) """
        ...

    def UndoAction(self): # -> 
        """ UndoAction(self: FrameClass) """
        ...

    def _GetGridX(self, GridX) -> int:
        """ _GetGridX(self: FrameClass) -> int """
        ...

    def _GetGridY(self, GridY) -> int:
        """ _GetGridY(self: FrameClass) -> int """
        ...

    def _GetInsideHeight(self, InsideHeight) -> int:
        """ _GetInsideHeight(self: FrameClass) -> int """
        ...

    def _GetInsideWidth(self, InsideWidth) -> int:
        """ _GetInsideWidth(self: FrameClass) -> int """
        ...

    def _GetScrollHeight(self, ScrollHeight) -> int:
        """ _GetScrollHeight(self: FrameClass) -> int """
        ...

    def _GetScrollLeft(self, ScrollLeft) -> int:
        """ _GetScrollLeft(self: FrameClass) -> int """
        ...

    def _GetScrollTop(self, ScrollTop) -> int:
        """ _GetScrollTop(self: FrameClass) -> int """
        ...

    def _GetScrollWidth(self, ScrollWidth) -> int:
        """ _GetScrollWidth(self: FrameClass) -> int """
        ...

    def _SetGridX(self, GridX:int): # -> 
        """ _SetGridX(self: FrameClass, GridX: int) """
        ...

    def _SetGridY(self, GridY:int): # -> 
        """ _SetGridY(self: FrameClass, GridY: int) """
        ...

    def _SetScrollHeight(self, ScrollHeight:int): # -> 
        """ _SetScrollHeight(self: FrameClass, ScrollHeight: int) """
        ...

    def _SetScrollLeft(self, ScrollLeft:int): # -> 
        """ _SetScrollLeft(self: FrameClass, ScrollLeft: int) """
        ...

    def _SetScrollTop(self, ScrollTop:int): # -> 
        """ _SetScrollTop(self: FrameClass, ScrollTop: int) """
        ...

    def _SetScrollWidth(self, ScrollWidth:int): # -> 
        """ _SetScrollWidth(self: FrameClass, ScrollWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    OptionFrameEvents_Event_Scroll = ...
    OptionFrameEvents_Event_Zoom = ...
    RemoveControl = ...


class IWHTMLCheckbox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: IWHTMLCheckbox) -> bool
        Set: Checked(self: IWHTMLCheckbox) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLCheckbox) -> str
        Set: HTMLName(self: IWHTMLCheckbox) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLCheckbox) -> str
        Set: HTMLType(self: IWHTMLCheckbox) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLCheckbox) -> str
        Set: Value(self: IWHTMLCheckbox) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents3_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents3_Event, : WHTMLControlEvents3_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents3_Event, : WHTMLControlEvents3_ClickEventHandler) """
        ...

    Click = ...


class HTMLCheckbox(WHTMLControlEvents3_Event, IWHTMLCheckbox): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLCheckboxClass(__ComObject, HTMLCheckbox): # skipped bases: <type 'WHTMLControlEvents3_Event'>, <type 'IWHTMLCheckbox'>, <type 'object'>
    """ no doc """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: HTMLCheckboxClass) -> bool
        Set: Checked(self: HTMLCheckboxClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLCheckboxClass) -> str
        Set: HTMLName(self: HTMLCheckboxClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLCheckboxClass) -> str
        Set: HTMLType(self: HTMLCheckboxClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLCheckboxClass) -> str
        Set: Value(self: HTMLCheckboxClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLCheckboxClass, : WHTMLControlEvents3_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLCheckboxClass, : WHTMLControlEvents3_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class IWHTMLHidden: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLHidden) -> str
        Set: HTMLName(self: IWHTMLHidden) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLHidden) -> str
        Set: HTMLType(self: IWHTMLHidden) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLHidden) -> str
        Set: Value(self: IWHTMLHidden) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents6_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents6_Event, : WHTMLControlEvents6_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents6_Event, : WHTMLControlEvents6_ClickEventHandler) """
        ...

    Click = ...


class HTMLHidden(WHTMLControlEvents6_Event, IWHTMLHidden): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLHiddenClass(__ComObject, HTMLHidden): # skipped bases: <type 'IWHTMLHidden'>, <type 'WHTMLControlEvents6_Event'>, <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLHiddenClass) -> str
        Set: HTMLName(self: HTMLHiddenClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLHiddenClass) -> str
        Set: HTMLType(self: HTMLHiddenClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLHiddenClass) -> str
        Set: Value(self: HTMLHiddenClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLHiddenClass, : WHTMLControlEvents6_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLHiddenClass, : WHTMLControlEvents6_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class IWHTMLImage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: IWHTMLImage) -> str
        Set: Action(self: IWHTMLImage) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: IWHTMLImage) -> str
        Set: Encoding(self: IWHTMLImage) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLImage) -> str
        Set: HTMLName(self: IWHTMLImage) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLImage) -> str
        Set: HTMLType(self: IWHTMLImage) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: IWHTMLImage) -> str
        Set: Method(self: IWHTMLImage) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: IWHTMLImage) -> str
        Set: Source(self: IWHTMLImage) = value
        """
        ...



class WHTMLControlEvents1_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents1_Event, : WHTMLControlEvents1_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents1_Event, : WHTMLControlEvents1_ClickEventHandler) """
        ...

    Click = ...


class HTMLImage(WHTMLControlEvents1_Event, IWHTMLImage): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLImageClass(HTMLImage, __ComObject): # skipped bases: <type 'WHTMLControlEvents1_Event'>, <type 'IWHTMLImage'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: HTMLImageClass) -> str
        Set: Action(self: HTMLImageClass) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: HTMLImageClass) -> str
        Set: Encoding(self: HTMLImageClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLImageClass) -> str
        Set: HTMLName(self: HTMLImageClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLImageClass) -> str
        Set: HTMLType(self: HTMLImageClass) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: HTMLImageClass) -> str
        Set: Method(self: HTMLImageClass) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: HTMLImageClass) -> str
        Set: Source(self: HTMLImageClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLImageClass, : WHTMLControlEvents1_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLImageClass, : WHTMLControlEvents1_ClickEventHandler) """
        ...

    Click = ...


class IWHTMLOption: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: IWHTMLOption) -> bool
        Set: Checked(self: IWHTMLOption) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: IWHTMLOption) -> fmDisplayStyle """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLOption) -> str
        Set: HTMLName(self: IWHTMLOption) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLOption) -> str
        Set: HTMLType(self: IWHTMLOption) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLOption) -> str
        Set: Value(self: IWHTMLOption) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents4_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents4_Event, : WHTMLControlEvents4_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents4_Event, : WHTMLControlEvents4_ClickEventHandler) """
        ...

    Click = ...


class HTMLOption(WHTMLControlEvents4_Event, IWHTMLOption): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLOptionClass(__ComObject, HTMLOption): # skipped bases: <type 'IWHTMLOption'>, <type 'WHTMLControlEvents4_Event'>, <type 'object'>
    """ no doc """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: HTMLOptionClass) -> bool
        Set: Checked(self: HTMLOptionClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: HTMLOptionClass) -> fmDisplayStyle """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLOptionClass) -> str
        Set: HTMLName(self: HTMLOptionClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLOptionClass) -> str
        Set: HTMLType(self: HTMLOptionClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLOptionClass) -> str
        Set: Value(self: HTMLOptionClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLOptionClass, : WHTMLControlEvents4_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLOptionClass, : WHTMLControlEvents4_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class IWHTMLPassword: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLPassword) -> str
        Set: HTMLName(self: IWHTMLPassword) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLPassword) -> str
        Set: HTMLType(self: IWHTMLPassword) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: IWHTMLPassword) -> int
        Set: MaxLength(self: IWHTMLPassword) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLPassword) -> str
        Set: Value(self: IWHTMLPassword) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: IWHTMLPassword) -> int
        Set: Width(self: IWHTMLPassword) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents7_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents7_Event, : WHTMLControlEvents7_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents7_Event, : WHTMLControlEvents7_ClickEventHandler) """
        ...

    Click = ...


class HTMLPassword(WHTMLControlEvents7_Event, IWHTMLPassword): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLPasswordClass(HTMLPassword, __ComObject): # skipped bases: <type 'WHTMLControlEvents7_Event'>, <type 'IWHTMLPassword'>, <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLPasswordClass) -> str
        Set: HTMLName(self: HTMLPasswordClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLPasswordClass) -> str
        Set: HTMLType(self: HTMLPasswordClass) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: HTMLPasswordClass) -> int
        Set: MaxLength(self: HTMLPasswordClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLPasswordClass) -> str
        Set: Value(self: HTMLPasswordClass) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: HTMLPasswordClass) -> int
        Set: Width(self: HTMLPasswordClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLPasswordClass, : WHTMLControlEvents7_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLPasswordClass, : WHTMLControlEvents7_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class IWHTMLReset: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IWHTMLReset) -> str
        Set: Caption(self: IWHTMLReset) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLReset) -> str
        Set: HTMLName(self: IWHTMLReset) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLReset) -> str
        Set: HTMLType(self: IWHTMLReset) = value
        """
        ...



class WHTMLControlEvents2_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents2_Event, : WHTMLControlEvents2_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents2_Event, : WHTMLControlEvents2_ClickEventHandler) """
        ...

    Click = ...


class HTMLReset(IWHTMLReset, WHTMLControlEvents2_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLResetClass(__ComObject, HTMLReset): # skipped bases: <type 'IWHTMLReset'>, <type 'WHTMLControlEvents2_Event'>, <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: HTMLResetClass) -> str
        Set: Caption(self: HTMLResetClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLResetClass) -> str
        Set: HTMLName(self: HTMLResetClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLResetClass) -> str
        Set: HTMLType(self: HTMLResetClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLResetClass, : WHTMLControlEvents2_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLResetClass, : WHTMLControlEvents2_ClickEventHandler) """
        ...

    Click = ...


class IWHTMLSelect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayValues(self) -> object:
        """
        Get: DisplayValues(self: IWHTMLSelect) -> object
        Set: DisplayValues(self: IWHTMLSelect) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLSelect) -> str
        Set: HTMLName(self: IWHTMLSelect) = value
        """
        ...

    @property
    def MultiSelect(self) -> bool:
        """
        Get: MultiSelect(self: IWHTMLSelect) -> bool
        Set: MultiSelect(self: IWHTMLSelect) = value
        """
        ...

    @property
    def Selected(self) -> str:
        """
        Get: Selected(self: IWHTMLSelect) -> str
        Set: Selected(self: IWHTMLSelect) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: IWHTMLSelect) -> int
        Set: Size(self: IWHTMLSelect) = value
        """
        ...

    @property
    def Values(self) -> object:
        """
        Get: Values(self: IWHTMLSelect) -> object
        Set: Values(self: IWHTMLSelect) = value
        """
        ...



class WHTMLControlEvents9_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents9_Event, : WHTMLControlEvents9_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents9_Event, : WHTMLControlEvents9_ClickEventHandler) """
        ...

    Click = ...


class HTMLSelect(WHTMLControlEvents9_Event, IWHTMLSelect): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLSelectClass(HTMLSelect, __ComObject): # skipped bases: <type 'WHTMLControlEvents9_Event'>, <type 'IWHTMLSelect'>, <type 'object'>
    """ no doc """
    @property
    def DisplayValues(self) -> object:
        """
        Get: DisplayValues(self: HTMLSelectClass) -> object
        Set: DisplayValues(self: HTMLSelectClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLSelectClass) -> str
        Set: HTMLName(self: HTMLSelectClass) = value
        """
        ...

    @property
    def MultiSelect(self) -> bool:
        """
        Get: MultiSelect(self: HTMLSelectClass) -> bool
        Set: MultiSelect(self: HTMLSelectClass) = value
        """
        ...

    @property
    def Selected(self) -> str:
        """
        Get: Selected(self: HTMLSelectClass) -> str
        Set: Selected(self: HTMLSelectClass) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: HTMLSelectClass) -> int
        Set: Size(self: HTMLSelectClass) = value
        """
        ...

    @property
    def Values(self) -> object:
        """
        Get: Values(self: HTMLSelectClass) -> object
        Set: Values(self: HTMLSelectClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLSelectClass, : WHTMLControlEvents9_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLSelectClass, : WHTMLControlEvents9_ClickEventHandler) """
        ...

    Click = ...


class IWHTMLSubmitButton: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: IWHTMLSubmitButton) -> str
        Set: Action(self: IWHTMLSubmitButton) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IWHTMLSubmitButton) -> str
        Set: Caption(self: IWHTMLSubmitButton) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: IWHTMLSubmitButton) -> str
        Set: Encoding(self: IWHTMLSubmitButton) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLSubmitButton) -> str
        Set: HTMLName(self: IWHTMLSubmitButton) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLSubmitButton) -> str
        Set: HTMLType(self: IWHTMLSubmitButton) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: IWHTMLSubmitButton) -> str
        Set: Method(self: IWHTMLSubmitButton) = value
        """
        ...



class WHTMLControlEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents_Event, : WHTMLControlEvents_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents_Event, : WHTMLControlEvents_ClickEventHandler) """
        ...

    Click = ...


class HTMLSubmit(WHTMLControlEvents_Event, IWHTMLSubmitButton): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLSubmitClass(HTMLSubmit, __ComObject): # skipped bases: <type 'IWHTMLSubmitButton'>, <type 'WHTMLControlEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: HTMLSubmitClass) -> str
        Set: Action(self: HTMLSubmitClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: HTMLSubmitClass) -> str
        Set: Caption(self: HTMLSubmitClass) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: HTMLSubmitClass) -> str
        Set: Encoding(self: HTMLSubmitClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLSubmitClass) -> str
        Set: HTMLName(self: HTMLSubmitClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLSubmitClass) -> str
        Set: HTMLType(self: HTMLSubmitClass) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: HTMLSubmitClass) -> str
        Set: Method(self: HTMLSubmitClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLSubmitClass, : WHTMLControlEvents_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLSubmitClass, : WHTMLControlEvents_ClickEventHandler) """
        ...

    Click = ...


class IWHTMLText: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLText) -> str
        Set: HTMLName(self: IWHTMLText) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: IWHTMLText) -> str
        Set: HTMLType(self: IWHTMLText) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: IWHTMLText) -> int
        Set: MaxLength(self: IWHTMLText) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLText) -> str
        Set: Value(self: IWHTMLText) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: IWHTMLText) -> int
        Set: Width(self: IWHTMLText) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents5_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents5_Event, : WHTMLControlEvents5_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents5_Event, : WHTMLControlEvents5_ClickEventHandler) """
        ...

    Click = ...


class HTMLText(IWHTMLText, WHTMLControlEvents5_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IWHTMLTextArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: IWHTMLTextArea) -> int
        Set: Columns(self: IWHTMLTextArea) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: IWHTMLTextArea) -> str
        Set: HTMLName(self: IWHTMLTextArea) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: IWHTMLTextArea) -> int
        Set: Rows(self: IWHTMLTextArea) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: IWHTMLTextArea) -> str
        Set: Value(self: IWHTMLTextArea) = value
        """
        ...

    @property
    def WordWrap(self) -> str:
        """
        Get: WordWrap(self: IWHTMLTextArea) -> str
        Set: WordWrap(self: IWHTMLTextArea) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WHTMLControlEvents10_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: WHTMLControlEvents10_Event, : WHTMLControlEvents10_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: WHTMLControlEvents10_Event, : WHTMLControlEvents10_ClickEventHandler) """
        ...

    Click = ...


class HTMLTextArea(WHTMLControlEvents10_Event, IWHTMLTextArea): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HTMLTextAreaClass(HTMLTextArea, __ComObject): # skipped bases: <type 'IWHTMLTextArea'>, <type 'WHTMLControlEvents10_Event'>, <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: HTMLTextAreaClass) -> int
        Set: Columns(self: HTMLTextAreaClass) = value
        """
        ...

    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLTextAreaClass) -> str
        Set: HTMLName(self: HTMLTextAreaClass) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: HTMLTextAreaClass) -> int
        Set: Rows(self: HTMLTextAreaClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLTextAreaClass) -> str
        Set: Value(self: HTMLTextAreaClass) = value
        """
        ...

    @property
    def WordWrap(self) -> str:
        """
        Get: WordWrap(self: HTMLTextAreaClass) -> str
        Set: WordWrap(self: HTMLTextAreaClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLTextAreaClass, : WHTMLControlEvents10_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLTextAreaClass, : WHTMLControlEvents10_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class HTMLTextClass(HTMLText, __ComObject): # skipped bases: <type 'WHTMLControlEvents5_Event'>, <type 'IWHTMLText'>, <type 'object'>
    """ no doc """
    @property
    def HTMLName(self) -> str:
        """
        Get: HTMLName(self: HTMLTextClass) -> str
        Set: HTMLName(self: HTMLTextClass) = value
        """
        ...

    @property
    def HTMLType(self) -> str:
        """
        Get: HTMLType(self: HTMLTextClass) -> str
        Set: HTMLType(self: HTMLTextClass) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: HTMLTextClass) -> int
        Set: MaxLength(self: HTMLTextClass) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HTMLTextClass) -> str
        Set: Value(self: HTMLTextClass) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: HTMLTextClass) -> int
        Set: Width(self: HTMLTextClass) = value
        """
        ...


    def add_Click(self): # -> 
        """ add_Click(self: HTMLTextClass, : WHTMLControlEvents5_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: HTMLTextClass, : WHTMLControlEvents5_ClickEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    Click = ...


class IFont: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bold(self) -> bool:
        """
        Get: Bold(self: IFont) -> bool
        Set: Bold(self: IFont) = value
        """
        ...

    @property
    def Charset(self) -> Int16:
        """
        Get: Charset(self: IFont) -> Int16
        Set: Charset(self: IFont) = value
        """
        ...

    @property
    def hFont(self) -> int:
        """ Get: hFont(self: IFont) -> int """
        ...

    @property
    def Italic(self) -> bool:
        """
        Get: Italic(self: IFont) -> bool
        Set: Italic(self: IFont) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IFont) -> str
        Set: Name(self: IFont) = value
        """
        ...

    @property
    def Size(self) -> Decimal:
        """
        Get: Size(self: IFont) -> Decimal
        Set: Size(self: IFont) = value
        """
        ...

    @property
    def Strikethrough(self) -> bool:
        """
        Get: Strikethrough(self: IFont) -> bool
        Set: Strikethrough(self: IFont) = value
        """
        ...

    @property
    def Underline(self) -> bool:
        """
        Get: Underline(self: IFont) -> bool
        Set: Underline(self: IFont) = value
        """
        ...

    @property
    def Weight(self) -> Int16:
        """
        Get: Weight(self: IFont) -> Int16
        Set: Weight(self: IFont) = value
        """
        ...


    def AddRefHfont(self, hFont:int): # -> 
        """ AddRefHfont(self: IFont, hFont: int) """
        ...

    def Clone(self, lplpfont) -> IFont:
        """ Clone(self: IFont) -> IFont """
        ...

    def IsEqual(self, lpFontOther:IFont): # -> 
        """ IsEqual(self: IFont, lpFontOther: IFont) """
        ...

    def ReleaseHfont(self, hFont:int): # -> 
        """ ReleaseHfont(self: IFont, hFont: int) """
        ...

    def SetRatio(self, cyLogical:int, cyHimetric:int): # -> 
        """ SetRatio(self: IFont, cyLogical: int, cyHimetric: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IImage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: IImage) -> bool
        Set: AutoSize(self: IImage) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IImage) -> int
        Set: BackColor(self: IImage) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: IImage) -> fmBackStyle
        Set: BackStyle(self: IImage) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: IImage) -> int
        Set: BorderColor(self: IImage) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: IImage) -> fmBorderStyle
        Set: BorderStyle(self: IImage) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IImage) -> bool
        Set: Enabled(self: IImage) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IImage) -> StdPicture
        Set: MouseIcon(self: IImage) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IImage) -> fmMousePointer
        Set: MousePointer(self: IImage) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: IImage) -> StdPicture
        Set: Picture(self: IImage) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: IImage) -> fmPictureAlignment
        Set: PictureAlignment(self: IImage) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: IImage) -> fmPictureSizeMode
        Set: PictureSizeMode(self: IImage) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: IImage) -> bool
        Set: PictureTiling(self: IImage) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: IImage) -> fmSpecialEffect
        Set: SpecialEffect(self: IImage) = value
        """
        ...



class ILabelControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: ILabelControl) -> str
        Set: Accelerator(self: ILabelControl) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: ILabelControl) -> bool
        Set: AutoSize(self: ILabelControl) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ILabelControl) -> int
        Set: BackColor(self: ILabelControl) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: ILabelControl) -> fmBackStyle
        Set: BackStyle(self: ILabelControl) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: ILabelControl) -> int
        Set: BorderColor(self: ILabelControl) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: ILabelControl) -> fmBorderStyle
        Set: BorderStyle(self: ILabelControl) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ILabelControl) -> str
        Set: Caption(self: ILabelControl) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ILabelControl) -> bool
        Set: Enabled(self: ILabelControl) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ILabelControl) -> NewFont
        Set: Font(self: ILabelControl) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ILabelControl) -> bool
        Set: FontBold(self: ILabelControl) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ILabelControl) -> bool
        Set: FontItalic(self: ILabelControl) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ILabelControl) -> str
        Set: FontName(self: ILabelControl) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ILabelControl) -> Decimal
        Set: FontSize(self: ILabelControl) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ILabelControl) -> bool
        Set: FontStrikethru(self: ILabelControl) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ILabelControl) -> bool
        Set: FontUnderline(self: ILabelControl) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ILabelControl) -> Int16
        Set: FontWeight(self: ILabelControl) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ILabelControl) -> int
        Set: ForeColor(self: ILabelControl) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ILabelControl) -> StdPicture
        Set: MouseIcon(self: ILabelControl) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ILabelControl) -> fmMousePointer
        Set: MousePointer(self: ILabelControl) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: ILabelControl) -> StdPicture
        Set: Picture(self: ILabelControl) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: ILabelControl) -> fmPicturePosition
        Set: PicturePosition(self: ILabelControl) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: ILabelControl) -> fmSpecialEffect
        Set: SpecialEffect(self: ILabelControl) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: ILabelControl) -> fmTextAlign
        Set: TextAlign(self: ILabelControl) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: ILabelControl) -> bool
        Set: WordWrap(self: ILabelControl) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ILabelControl) = value """
        ...

    @property
    def _Value(self) -> str:
        """
        Get: _Value(self: ILabelControl) -> str
        Set: _Value(self: ILabelControl) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ImageEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ImageEvents_Event, : ImageEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ImageEvents_Event, : ImageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: ImageEvents_Event, : ImageEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: ImageEvents_Event, : ImageEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ImageEvents_Event, : ImageEvents_ErrorEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: ImageEvents_Event, : ImageEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: ImageEvents_Event, : ImageEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: ImageEvents_Event, : ImageEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ImageEvents_Event, : ImageEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ImageEvents_Event, : ImageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: ImageEvents_Event, : ImageEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: ImageEvents_Event, : ImageEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ImageEvents_Event, : ImageEvents_ErrorEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: ImageEvents_Event, : ImageEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: ImageEvents_Event, : ImageEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: ImageEvents_Event, : ImageEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class Image(ImageEvents_Event, IImage): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ImageClass(Image, __ComObject): # skipped bases: <type 'ImageEvents_Event'>, <type 'IImage'>, <type 'object'>
    """ ImageClass() """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: ImageClass) -> bool
        Set: AutoSize(self: ImageClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ImageClass) -> int
        Set: BackColor(self: ImageClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: ImageClass) -> fmBackStyle
        Set: BackStyle(self: ImageClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: ImageClass) -> int
        Set: BorderColor(self: ImageClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: ImageClass) -> fmBorderStyle
        Set: BorderStyle(self: ImageClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ImageClass) -> bool
        Set: Enabled(self: ImageClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ImageClass) -> StdPicture
        Set: MouseIcon(self: ImageClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ImageClass) -> fmMousePointer
        Set: MousePointer(self: ImageClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: ImageClass) -> StdPicture
        Set: Picture(self: ImageClass) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: ImageClass) -> fmPictureAlignment
        Set: PictureAlignment(self: ImageClass) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: ImageClass) -> fmPictureSizeMode
        Set: PictureSizeMode(self: ImageClass) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: ImageClass) -> bool
        Set: PictureTiling(self: ImageClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: ImageClass) -> fmSpecialEffect
        Set: SpecialEffect(self: ImageClass) = value
        """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ImageClass, : ImageEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ImageClass, : ImageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: ImageClass, : ImageEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: ImageClass, : ImageEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ImageClass, : ImageEvents_ErrorEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: ImageClass, : ImageEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: ImageClass, : ImageEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: ImageClass, : ImageEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ImageClass, : ImageEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ImageClass, : ImageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: ImageClass, : ImageEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: ImageClass, : ImageEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ImageClass, : ImageEvents_ErrorEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: ImageClass, : ImageEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: ImageClass, : ImageEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: ImageClass, : ImageEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class ImageEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: ImageEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: ImageEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Click(self): # -> 
        """ Click(self: ImageEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: ImageEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: ImageEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: ImageEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: ImageEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: ImageEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class ImageEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: ImageEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class ImageEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: ImageEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class ImageEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ImageEvents_ClickEventHandler) """
        ...


class ImageEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: ImageEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class ImageEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: ImageEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class ImageEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: ImageEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class ImageEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: ImageEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class ImageEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: ImageEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class ImageEvents_SinkHelper(ImageEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class IMdcList: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IMdcList) -> int
        Set: BackColor(self: IMdcList) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: IMdcList) -> int
        Set: BorderColor(self: IMdcList) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: IMdcList) -> bool
        Set: BordersSuppress(self: IMdcList) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: IMdcList) -> fmBorderStyle
        Set: BorderStyle(self: IMdcList) = value
        """
        ...

    @property
    def BoundColumn(self) -> object:
        """
        Get: BoundColumn(self: IMdcList) -> object
        Set: BoundColumn(self: IMdcList) = value
        """
        ...

    @property
    def ColumnCount(self) -> int:
        """
        Get: ColumnCount(self: IMdcList) -> int
        Set: ColumnCount(self: IMdcList) = value
        """
        ...

    @property
    def ColumnHeads(self) -> bool:
        """
        Get: ColumnHeads(self: IMdcList) -> bool
        Set: ColumnHeads(self: IMdcList) = value
        """
        ...

    @property
    def ColumnWidths(self) -> str:
        """
        Get: ColumnWidths(self: IMdcList) -> str
        Set: ColumnWidths(self: IMdcList) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: IMdcList) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IMdcList) -> bool
        Set: Enabled(self: IMdcList) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IMdcList) -> NewFont
        Set: Font(self: IMdcList) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: IMdcList) -> bool
        Set: FontBold(self: IMdcList) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: IMdcList) -> bool
        Set: FontItalic(self: IMdcList) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: IMdcList) -> str
        Set: FontName(self: IMdcList) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: IMdcList) -> Decimal
        Set: FontSize(self: IMdcList) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: IMdcList) -> bool
        Set: FontStrikethru(self: IMdcList) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: IMdcList) -> bool
        Set: FontUnderline(self: IMdcList) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: IMdcList) -> Int16
        Set: FontWeight(self: IMdcList) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IMdcList) -> int
        Set: ForeColor(self: IMdcList) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: IMdcList) -> fmIMEMode
        Set: IMEMode(self: IMdcList) = value
        """
        ...

    @property
    def IntegralHeight(self) -> bool:
        """
        Get: IntegralHeight(self: IMdcList) -> bool
        Set: IntegralHeight(self: IMdcList) = value
        """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: IMdcList) -> int """
        ...

    @property
    def ListCursor(self) -> object:
        """
        Get: ListCursor(self: IMdcList) -> object
        Set: ListCursor(self: IMdcList) = value
        """
        ...

    @property
    def ListIndex(self) -> object:
        """
        Get: ListIndex(self: IMdcList) -> object
        Set: ListIndex(self: IMdcList) = value
        """
        ...

    @property
    def ListStyle(self) -> fmListStyle:
        """
        Get: ListStyle(self: IMdcList) -> fmListStyle
        Set: ListStyle(self: IMdcList) = value
        """
        ...

    @property
    def ListWidth(self) -> object:
        """
        Get: ListWidth(self: IMdcList) -> object
        Set: ListWidth(self: IMdcList) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: IMdcList) -> bool
        Set: Locked(self: IMdcList) = value
        """
        ...

    @property
    def MatchEntry(self) -> fmMatchEntry:
        """
        Get: MatchEntry(self: IMdcList) -> fmMatchEntry
        Set: MatchEntry(self: IMdcList) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IMdcList) -> StdPicture
        Set: MouseIcon(self: IMdcList) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IMdcList) -> fmMousePointer
        Set: MousePointer(self: IMdcList) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: IMdcList) -> fmMultiSelect
        Set: MultiSelect(self: IMdcList) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: IMdcList) -> fmSpecialEffect
        Set: SpecialEffect(self: IMdcList) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IMdcList) -> str
        Set: Text(self: IMdcList) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: IMdcList) -> fmTextAlign
        Set: TextAlign(self: IMdcList) = value
        """
        ...

    @property
    def TextColumn(self) -> object:
        """
        Get: TextColumn(self: IMdcList) -> object
        Set: TextColumn(self: IMdcList) = value
        """
        ...

    @property
    def TopIndex(self) -> object:
        """
        Get: TopIndex(self: IMdcList) -> object
        Set: TopIndex(self: IMdcList) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: IMdcList) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IMdcList) -> object
        Set: Value(self: IMdcList) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IMdcList) = value """
        ...


    def AddItem(self, pvargItem:object, pvargIndex:object) -> Tuple_[object, object]:
        """ AddItem(self: IMdcList, pvargItem: object, pvargIndex: object) -> (object, object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IMdcList) """
        ...

    def RemoveItem(self, pvargIndex:object) -> object:
        """ RemoveItem(self: IMdcList, pvargIndex: object) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IMdcOptionButton(IMdcCheckBox): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IMdcText: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: IMdcText) -> bool
        Set: AutoSize(self: IMdcText) = value
        """
        ...

    @property
    def AutoTab(self) -> bool:
        """
        Get: AutoTab(self: IMdcText) -> bool
        Set: AutoTab(self: IMdcText) = value
        """
        ...

    @property
    def AutoWordSelect(self) -> bool:
        """
        Get: AutoWordSelect(self: IMdcText) -> bool
        Set: AutoWordSelect(self: IMdcText) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IMdcText) -> int
        Set: BackColor(self: IMdcText) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: IMdcText) -> fmBackStyle
        Set: BackStyle(self: IMdcText) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: IMdcText) -> int
        Set: BorderColor(self: IMdcText) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: IMdcText) -> bool
        Set: BordersSuppress(self: IMdcText) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: IMdcText) -> fmBorderStyle
        Set: BorderStyle(self: IMdcText) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: IMdcText) -> bool """
        ...

    @property
    def CurLine(self) -> int:
        """
        Get: CurLine(self: IMdcText) -> int
        Set: CurLine(self: IMdcText) = value
        """
        ...

    @property
    def CurTargetX(self) -> int:
        """ Get: CurTargetX(self: IMdcText) -> int """
        ...

    @property
    def CurTargetY(self) -> int:
        """ Get: CurTargetY(self: IMdcText) -> int """
        ...

    @property
    def CurX(self) -> int:
        """
        Get: CurX(self: IMdcText) -> int
        Set: CurX(self: IMdcText) = value
        """
        ...

    @property
    def CurY(self) -> int:
        """
        Get: CurY(self: IMdcText) -> int
        Set: CurY(self: IMdcText) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: IMdcText) -> fmDisplayStyle """
        ...

    @property
    def DragBehavior(self) -> fmDragBehavior:
        """
        Get: DragBehavior(self: IMdcText) -> fmDragBehavior
        Set: DragBehavior(self: IMdcText) = value
        """
        ...

    @property
    def DropButtonStyle(self) -> fmDropButtonStyle:
        """
        Get: DropButtonStyle(self: IMdcText) -> fmDropButtonStyle
        Set: DropButtonStyle(self: IMdcText) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IMdcText) -> bool
        Set: Enabled(self: IMdcText) = value
        """
        ...

    @property
    def EnterFieldBehavior(self) -> fmEnterFieldBehavior:
        """
        Get: EnterFieldBehavior(self: IMdcText) -> fmEnterFieldBehavior
        Set: EnterFieldBehavior(self: IMdcText) = value
        """
        ...

    @property
    def EnterKeyBehavior(self) -> bool:
        """
        Get: EnterKeyBehavior(self: IMdcText) -> bool
        Set: EnterKeyBehavior(self: IMdcText) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IMdcText) -> NewFont
        Set: Font(self: IMdcText) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: IMdcText) -> bool
        Set: FontBold(self: IMdcText) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: IMdcText) -> bool
        Set: FontItalic(self: IMdcText) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: IMdcText) -> str
        Set: FontName(self: IMdcText) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: IMdcText) -> Decimal
        Set: FontSize(self: IMdcText) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: IMdcText) -> bool
        Set: FontStrikethru(self: IMdcText) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: IMdcText) -> bool
        Set: FontUnderline(self: IMdcText) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: IMdcText) -> Int16
        Set: FontWeight(self: IMdcText) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IMdcText) -> int
        Set: ForeColor(self: IMdcText) = value
        """
        ...

    @property
    def HideSelection(self) -> bool:
        """
        Get: HideSelection(self: IMdcText) -> bool
        Set: HideSelection(self: IMdcText) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: IMdcText) -> fmIMEMode
        Set: IMEMode(self: IMdcText) = value
        """
        ...

    @property
    def IntegralHeight(self) -> bool:
        """
        Get: IntegralHeight(self: IMdcText) -> bool
        Set: IntegralHeight(self: IMdcText) = value
        """
        ...

    @property
    def LineCount(self) -> int:
        """ Get: LineCount(self: IMdcText) -> int """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: IMdcText) -> bool
        Set: Locked(self: IMdcText) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: IMdcText) -> int
        Set: MaxLength(self: IMdcText) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IMdcText) -> StdPicture
        Set: MouseIcon(self: IMdcText) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IMdcText) -> fmMousePointer
        Set: MousePointer(self: IMdcText) = value
        """
        ...

    @property
    def MultiLine(self) -> bool:
        """
        Get: MultiLine(self: IMdcText) -> bool
        Set: MultiLine(self: IMdcText) = value
        """
        ...

    @property
    def PasswordChar(self) -> str:
        """
        Get: PasswordChar(self: IMdcText) -> str
        Set: PasswordChar(self: IMdcText) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: IMdcText) -> fmScrollBars
        Set: ScrollBars(self: IMdcText) = value
        """
        ...

    @property
    def SelectionMargin(self) -> bool:
        """
        Get: SelectionMargin(self: IMdcText) -> bool
        Set: SelectionMargin(self: IMdcText) = value
        """
        ...

    @property
    def SelLength(self) -> int:
        """
        Get: SelLength(self: IMdcText) -> int
        Set: SelLength(self: IMdcText) = value
        """
        ...

    @property
    def SelStart(self) -> int:
        """
        Get: SelStart(self: IMdcText) -> int
        Set: SelStart(self: IMdcText) = value
        """
        ...

    @property
    def SelText(self) -> str:
        """
        Get: SelText(self: IMdcText) -> str
        Set: SelText(self: IMdcText) = value
        """
        ...

    @property
    def ShowDropButtonWhen(self) -> fmShowDropButtonWhen:
        """
        Get: ShowDropButtonWhen(self: IMdcText) -> fmShowDropButtonWhen
        Set: ShowDropButtonWhen(self: IMdcText) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: IMdcText) -> fmSpecialEffect
        Set: SpecialEffect(self: IMdcText) = value
        """
        ...

    @property
    def TabKeyBehavior(self) -> bool:
        """
        Get: TabKeyBehavior(self: IMdcText) -> bool
        Set: TabKeyBehavior(self: IMdcText) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IMdcText) -> str
        Set: Text(self: IMdcText) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: IMdcText) -> fmTextAlign
        Set: TextAlign(self: IMdcText) = value
        """
        ...

    @property
    def TextLength(self) -> int:
        """ Get: TextLength(self: IMdcText) -> int """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: IMdcText) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IMdcText) -> object
        Set: Value(self: IMdcText) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: IMdcText) -> bool
        Set: WordWrap(self: IMdcText) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IMdcText) = value """
        ...


    def Copy(self): # -> 
        """ Copy(self: IMdcText) """
        ...

    def Cut(self): # -> 
        """ Cut(self: IMdcText) """
        ...

    def Paste(self): # -> 
        """ Paste(self: IMdcText) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IMdcToggleButton(IMdcCheckBox): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IMultiPage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IMultiPage) -> int
        Set: BackColor(self: IMultiPage) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IMultiPage) -> bool
        Set: Enabled(self: IMultiPage) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: IMultiPage) -> NewFont
        Set: Font(self: IMultiPage) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: IMultiPage) -> bool
        Set: FontBold(self: IMultiPage) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: IMultiPage) -> bool
        Set: FontItalic(self: IMultiPage) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: IMultiPage) -> str
        Set: FontName(self: IMultiPage) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: IMultiPage) -> Decimal
        Set: FontSize(self: IMultiPage) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: IMultiPage) -> bool
        Set: FontStrikethru(self: IMultiPage) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: IMultiPage) -> bool
        Set: FontUnderline(self: IMultiPage) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: IMultiPage) -> Int16
        Set: FontWeight(self: IMultiPage) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IMultiPage) -> int
        Set: ForeColor(self: IMultiPage) = value
        """
        ...

    @property
    def MultiRow(self) -> bool:
        """
        Get: MultiRow(self: IMultiPage) -> bool
        Set: MultiRow(self: IMultiPage) = value
        """
        ...

    @property
    def Pages(self) -> Pages:
        """ Get: Pages(self: IMultiPage) -> Pages """
        ...

    @property
    def SelectedItem(self) -> Page:
        """ Get: SelectedItem(self: IMultiPage) -> Page """
        ...

    @property
    def Style(self) -> fmTabStyle:
        """
        Get: Style(self: IMultiPage) -> fmTabStyle
        Set: Style(self: IMultiPage) = value
        """
        ...

    @property
    def TabFixedHeight(self) -> Single:
        """
        Get: TabFixedHeight(self: IMultiPage) -> Single
        Set: TabFixedHeight(self: IMultiPage) = value
        """
        ...

    @property
    def TabFixedWidth(self) -> Single:
        """
        Get: TabFixedWidth(self: IMultiPage) -> Single
        Set: TabFixedWidth(self: IMultiPage) = value
        """
        ...

    @property
    def TabOrientation(self) -> fmTabOrientation:
        """
        Get: TabOrientation(self: IMultiPage) -> fmTabOrientation
        Set: TabOrientation(self: IMultiPage) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: IMultiPage) -> int
        Set: Value(self: IMultiPage) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: IMultiPage) = value """
        ...


    def _GetTabFixedHeight(self, Height) -> int:
        """ _GetTabFixedHeight(self: IMultiPage) -> int """
        ...

    def _GetTabFixedWidth(self, Width) -> int:
        """ _GetTabFixedWidth(self: IMultiPage) -> int """
        ...

    def _SetTabFixedHeight(self, Height:int): # -> 
        """ _SetTabFixedHeight(self: IMultiPage, Height: int) """
        ...

    def _SetTabFixedWidth(self, Width:int): # -> 
        """ _SetTabFixedWidth(self: IMultiPage, Width: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IPage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: IPage) -> str
        Set: Accelerator(self: IPage) = value
        """
        ...

    @property
    def ActiveControl(self) -> Control:
        """ Get: ActiveControl(self: IPage) -> Control """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: IPage) -> bool """
        ...

    @property
    def CanRedo(self) -> bool:
        """ Get: CanRedo(self: IPage) -> bool """
        ...

    @property
    def CanUndo(self) -> bool:
        """ Get: CanUndo(self: IPage) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IPage) -> str
        Set: Caption(self: IPage) = value
        """
        ...

    @property
    def Controls(self) -> Controls:
        """ Get: Controls(self: IPage) -> Controls """
        ...

    @property
    def ControlTipText(self) -> str:
        """
        Get: ControlTipText(self: IPage) -> str
        Set: ControlTipText(self: IPage) = value
        """
        ...

    @property
    def Cycle(self) -> fmCycle:
        """
        Get: Cycle(self: IPage) -> fmCycle
        Set: Cycle(self: IPage) = value
        """
        ...

    @property
    def DesignMode(self) -> fmMode:
        """
        Get: DesignMode(self: IPage) -> fmMode
        Set: DesignMode(self: IPage) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IPage) -> bool
        Set: Enabled(self: IPage) = value
        """
        ...

    @property
    def GridX(self) -> Single:
        """
        Get: GridX(self: IPage) -> Single
        Set: GridX(self: IPage) = value
        """
        ...

    @property
    def GridY(self) -> Single:
        """
        Get: GridY(self: IPage) -> Single
        Set: GridY(self: IPage) = value
        """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: IPage) -> int
        Set: Index(self: IPage) = value
        """
        ...

    @property
    def InsideHeight(self) -> Single:
        """ Get: InsideHeight(self: IPage) -> Single """
        ...

    @property
    def InsideWidth(self) -> Single:
        """ Get: InsideWidth(self: IPage) -> Single """
        ...

    @property
    def KeepScrollBarsVisible(self) -> fmScrollBars:
        """
        Get: KeepScrollBarsVisible(self: IPage) -> fmScrollBars
        Set: KeepScrollBarsVisible(self: IPage) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IPage) -> str
        Set: Name(self: IPage) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IPage) -> object """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: IPage) -> StdPicture
        Set: Picture(self: IPage) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: IPage) -> fmPictureAlignment
        Set: PictureAlignment(self: IPage) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: IPage) -> fmPictureSizeMode
        Set: PictureSizeMode(self: IPage) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: IPage) -> bool
        Set: PictureTiling(self: IPage) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: IPage) -> fmScrollBars
        Set: ScrollBars(self: IPage) = value
        """
        ...

    @property
    def ScrollHeight(self) -> Single:
        """
        Get: ScrollHeight(self: IPage) -> Single
        Set: ScrollHeight(self: IPage) = value
        """
        ...

    @property
    def ScrollLeft(self) -> Single:
        """
        Get: ScrollLeft(self: IPage) -> Single
        Set: ScrollLeft(self: IPage) = value
        """
        ...

    @property
    def ScrollTop(self) -> Single:
        """
        Get: ScrollTop(self: IPage) -> Single
        Set: ScrollTop(self: IPage) = value
        """
        ...

    @property
    def ScrollWidth(self) -> Single:
        """
        Get: ScrollWidth(self: IPage) -> Single
        Set: ScrollWidth(self: IPage) = value
        """
        ...

    @property
    def Selected(self) -> Controls:
        """ Get: Selected(self: IPage) -> Controls """
        ...

    @property
    def ShowGridDots(self) -> fmMode:
        """
        Get: ShowGridDots(self: IPage) -> fmMode
        Set: ShowGridDots(self: IPage) = value
        """
        ...

    @property
    def ShowToolbox(self) -> fmMode:
        """
        Get: ShowToolbox(self: IPage) -> fmMode
        Set: ShowToolbox(self: IPage) = value
        """
        ...

    @property
    def SnapToGrid(self) -> fmMode:
        """
        Get: SnapToGrid(self: IPage) -> fmMode
        Set: SnapToGrid(self: IPage) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: IPage) -> str
        Set: Tag(self: IPage) = value
        """
        ...

    @property
    def TransitionEffect(self) -> fmTransitionEffect:
        """
        Get: TransitionEffect(self: IPage) -> fmTransitionEffect
        Set: TransitionEffect(self: IPage) = value
        """
        ...

    @property
    def TransitionPeriod(self) -> int:
        """
        Get: TransitionPeriod(self: IPage) -> int
        Set: TransitionPeriod(self: IPage) = value
        """
        ...

    @property
    def VerticalScrollBarSide(self) -> fmVerticalScrollBarSide:
        """
        Get: VerticalScrollBarSide(self: IPage) -> fmVerticalScrollBarSide
        Set: VerticalScrollBarSide(self: IPage) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: IPage) -> bool
        Set: Visible(self: IPage) = value
        """
        ...

    @property
    def Zoom(self) -> Int16:
        """
        Get: Zoom(self: IPage) -> Int16
        Set: Zoom(self: IPage) = value
        """
        ...


    def Copy(self): # -> 
        """ Copy(self: IPage) """
        ...

    def Cut(self): # -> 
        """ Cut(self: IPage) """
        ...

    def Paste(self): # -> 
        """ Paste(self: IPage) """
        ...

    def RedoAction(self): # -> 
        """ RedoAction(self: IPage) """
        ...

    def Repaint(self): # -> 
        """ Repaint(self: IPage) """
        ...

    def Scroll(self, xAction:object, yAction:object): # -> 
        """ Scroll(self: IPage, xAction: object, yAction: object) """
        ...

    def SetDefaultTabOrder(self): # -> 
        """ SetDefaultTabOrder(self: IPage) """
        ...

    def UndoAction(self): # -> 
        """ UndoAction(self: IPage) """
        ...

    def _GetGridX(self, GridX) -> int:
        """ _GetGridX(self: IPage) -> int """
        ...

    def _GetGridY(self, GridY) -> int:
        """ _GetGridY(self: IPage) -> int """
        ...

    def _GetInsideHeight(self, InsideHeight) -> int:
        """ _GetInsideHeight(self: IPage) -> int """
        ...

    def _GetInsideWidth(self, InsideWidth) -> int:
        """ _GetInsideWidth(self: IPage) -> int """
        ...

    def _GetScrollHeight(self, ScrollHeight) -> int:
        """ _GetScrollHeight(self: IPage) -> int """
        ...

    def _GetScrollLeft(self, ScrollLeft) -> int:
        """ _GetScrollLeft(self: IPage) -> int """
        ...

    def _GetScrollTop(self, ScrollTop) -> int:
        """ _GetScrollTop(self: IPage) -> int """
        ...

    def _GetScrollWidth(self, ScrollWidth) -> int:
        """ _GetScrollWidth(self: IPage) -> int """
        ...

    def _SetGridX(self, GridX:int): # -> 
        """ _SetGridX(self: IPage, GridX: int) """
        ...

    def _SetGridY(self, GridY:int): # -> 
        """ _SetGridY(self: IPage, GridY: int) """
        ...

    def _SetScrollHeight(self, ScrollHeight:int): # -> 
        """ _SetScrollHeight(self: IPage, ScrollHeight: int) """
        ...

    def _SetScrollLeft(self, ScrollLeft:int): # -> 
        """ _SetScrollLeft(self: IPage, ScrollLeft: int) """
        ...

    def _SetScrollTop(self, ScrollTop:int): # -> 
        """ _SetScrollTop(self: IPage, ScrollTop: int) """
        ...

    def _SetScrollWidth(self, ScrollWidth:int): # -> 
        """ _SetScrollWidth(self: IPage, ScrollWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IReturnBoolean: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> bool:
        """
        Get: Value(self: IReturnBoolean) -> bool
        Set: Value(self: IReturnBoolean) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IReturnEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> fmDropEffect:
        """
        Get: Value(self: IReturnEffect) -> fmDropEffect
        Set: Value(self: IReturnEffect) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IReturnInteger: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> int:
        """
        Get: Value(self: IReturnInteger) -> int
        Set: Value(self: IReturnInteger) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IReturnSingle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> Single:
        """
        Get: Value(self: IReturnSingle) -> Single
        Set: Value(self: IReturnSingle) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IReturnString: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: IReturnString) -> str
        Set: Value(self: IReturnString) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IScrollbar: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: IScrollbar) -> int
        Set: BackColor(self: IScrollbar) = value
        """
        ...

    @property
    def Delay(self) -> int:
        """
        Get: Delay(self: IScrollbar) -> int
        Set: Delay(self: IScrollbar) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IScrollbar) -> bool
        Set: Enabled(self: IScrollbar) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: IScrollbar) -> int
        Set: ForeColor(self: IScrollbar) = value
        """
        ...

    @property
    def LargeChange(self) -> int:
        """
        Get: LargeChange(self: IScrollbar) -> int
        Set: LargeChange(self: IScrollbar) = value
        """
        ...

    @property
    def Max(self) -> int:
        """
        Get: Max(self: IScrollbar) -> int
        Set: Max(self: IScrollbar) = value
        """
        ...

    @property
    def Min(self) -> int:
        """
        Get: Min(self: IScrollbar) -> int
        Set: Min(self: IScrollbar) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: IScrollbar) -> StdPicture
        Set: MouseIcon(self: IScrollbar) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: IScrollbar) -> fmMousePointer
        Set: MousePointer(self: IScrollbar) = value
        """
        ...

    @property
    def Orientation(self) -> fmOrientation:
        """
        Get: Orientation(self: IScrollbar) -> fmOrientation
        Set: Orientation(self: IScrollbar) = value
        """
        ...

    @property
    def ProportionalThumb(self) -> bool:
        """
        Get: ProportionalThumb(self: IScrollbar) -> bool
        Set: ProportionalThumb(self: IScrollbar) = value
        """
        ...

    @property
    def SmallChange(self) -> int:
        """
        Get: SmallChange(self: IScrollbar) -> int
        Set: SmallChange(self: IScrollbar) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: IScrollbar) -> int
        Set: Value(self: IScrollbar) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ISpinbutton: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ISpinbutton) -> int
        Set: BackColor(self: ISpinbutton) = value
        """
        ...

    @property
    def Delay(self) -> int:
        """
        Get: Delay(self: ISpinbutton) -> int
        Set: Delay(self: ISpinbutton) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ISpinbutton) -> bool
        Set: Enabled(self: ISpinbutton) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ISpinbutton) -> int
        Set: ForeColor(self: ISpinbutton) = value
        """
        ...

    @property
    def Max(self) -> int:
        """
        Get: Max(self: ISpinbutton) -> int
        Set: Max(self: ISpinbutton) = value
        """
        ...

    @property
    def Min(self) -> int:
        """
        Get: Min(self: ISpinbutton) -> int
        Set: Min(self: ISpinbutton) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ISpinbutton) -> StdPicture
        Set: MouseIcon(self: ISpinbutton) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ISpinbutton) -> fmMousePointer
        Set: MousePointer(self: ISpinbutton) = value
        """
        ...

    @property
    def Orientation(self) -> fmOrientation:
        """
        Get: Orientation(self: ISpinbutton) -> fmOrientation
        Set: Orientation(self: ISpinbutton) = value
        """
        ...

    @property
    def SmallChange(self) -> int:
        """
        Get: SmallChange(self: ISpinbutton) -> int
        Set: SmallChange(self: ISpinbutton) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: ISpinbutton) -> int
        Set: Value(self: ISpinbutton) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ITabStrip: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ITabStrip) -> int
        Set: BackColor(self: ITabStrip) = value
        """
        ...

    @property
    def ClientHeight(self) -> Single:
        """ Get: ClientHeight(self: ITabStrip) -> Single """
        ...

    @property
    def ClientLeft(self) -> Single:
        """ Get: ClientLeft(self: ITabStrip) -> Single """
        ...

    @property
    def ClientTop(self) -> Single:
        """ Get: ClientTop(self: ITabStrip) -> Single """
        ...

    @property
    def ClientWidth(self) -> Single:
        """ Get: ClientWidth(self: ITabStrip) -> Single """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ITabStrip) -> bool
        Set: Enabled(self: ITabStrip) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ITabStrip) -> NewFont
        Set: Font(self: ITabStrip) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ITabStrip) -> bool
        Set: FontBold(self: ITabStrip) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ITabStrip) -> bool
        Set: FontItalic(self: ITabStrip) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ITabStrip) -> str
        Set: FontName(self: ITabStrip) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ITabStrip) -> Decimal
        Set: FontSize(self: ITabStrip) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ITabStrip) -> bool
        Set: FontStrikethru(self: ITabStrip) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ITabStrip) -> bool
        Set: FontUnderline(self: ITabStrip) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ITabStrip) -> Int16
        Set: FontWeight(self: ITabStrip) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ITabStrip) -> int
        Set: ForeColor(self: ITabStrip) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ITabStrip) -> StdPicture
        Set: MouseIcon(self: ITabStrip) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ITabStrip) -> fmMousePointer
        Set: MousePointer(self: ITabStrip) = value
        """
        ...

    @property
    def MultiRow(self) -> bool:
        """
        Get: MultiRow(self: ITabStrip) -> bool
        Set: MultiRow(self: ITabStrip) = value
        """
        ...

    @property
    def SelectedItem(self) -> Tab:
        """ Get: SelectedItem(self: ITabStrip) -> Tab """
        ...

    @property
    def Style(self) -> fmTabStyle:
        """
        Get: Style(self: ITabStrip) -> fmTabStyle
        Set: Style(self: ITabStrip) = value
        """
        ...

    @property
    def TabFixedHeight(self) -> Single:
        """
        Get: TabFixedHeight(self: ITabStrip) -> Single
        Set: TabFixedHeight(self: ITabStrip) = value
        """
        ...

    @property
    def TabFixedWidth(self) -> Single:
        """
        Get: TabFixedWidth(self: ITabStrip) -> Single
        Set: TabFixedWidth(self: ITabStrip) = value
        """
        ...

    @property
    def TabOrientation(self) -> fmTabOrientation:
        """
        Get: TabOrientation(self: ITabStrip) -> fmTabOrientation
        Set: TabOrientation(self: ITabStrip) = value
        """
        ...

    @property
    def Tabs(self) -> Tabs:
        """ Get: Tabs(self: ITabStrip) -> Tabs """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: ITabStrip) -> int
        Set: Value(self: ITabStrip) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ITabStrip) = value """
        ...


    def _GetClientHeight(self, ClientHeight) -> int:
        """ _GetClientHeight(self: ITabStrip) -> int """
        ...

    def _GetClientLeft(self, ClientLeft) -> int:
        """ _GetClientLeft(self: ITabStrip) -> int """
        ...

    def _GetClientTop(self, ClientTop) -> int:
        """ _GetClientTop(self: ITabStrip) -> int """
        ...

    def _GetClientWidth(self, ClientWidth) -> int:
        """ _GetClientWidth(self: ITabStrip) -> int """
        ...

    def _GetTabFixedHeight(self, TabFixedHeight) -> int:
        """ _GetTabFixedHeight(self: ITabStrip) -> int """
        ...

    def _GetTabFixedWidth(self, TabFixedWidth) -> int:
        """ _GetTabFixedWidth(self: ITabStrip) -> int """
        ...

    def _SetTabFixedHeight(self, TabFixedHeight:int): # -> 
        """ _SetTabFixedHeight(self: ITabStrip, TabFixedHeight: int) """
        ...

    def _SetTabFixedWidth(self, TabFixedWidth:int): # -> 
        """ _SetTabFixedWidth(self: ITabStrip, TabFixedWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class LabelControlEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: LabelControlEvents_Event, : LabelControlEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: LabelControlEvents_Event, : LabelControlEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: LabelControlEvents_Event, : LabelControlEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: LabelControlEvents_Event, : LabelControlEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: LabelControlEvents_Event, : LabelControlEvents_ErrorEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: LabelControlEvents_Event, : LabelControlEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: LabelControlEvents_Event, : LabelControlEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: LabelControlEvents_Event, : LabelControlEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: LabelControlEvents_Event, : LabelControlEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: LabelControlEvents_Event, : LabelControlEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: LabelControlEvents_Event, : LabelControlEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: LabelControlEvents_Event, : LabelControlEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: LabelControlEvents_Event, : LabelControlEvents_ErrorEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: LabelControlEvents_Event, : LabelControlEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: LabelControlEvents_Event, : LabelControlEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: LabelControlEvents_Event, : LabelControlEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class Label(LabelControlEvents_Event, ILabelControl): # skipped bases: <type 'object'>
    """ no doc """
    pass

class LabelClass(Label, __ComObject): # skipped bases: <type 'LabelControlEvents_Event'>, <type 'ILabelControl'>, <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: LabelClass) -> str
        Set: Accelerator(self: LabelClass) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: LabelClass) -> bool
        Set: AutoSize(self: LabelClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: LabelClass) -> int
        Set: BackColor(self: LabelClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: LabelClass) -> fmBackStyle
        Set: BackStyle(self: LabelClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: LabelClass) -> int
        Set: BorderColor(self: LabelClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: LabelClass) -> fmBorderStyle
        Set: BorderStyle(self: LabelClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: LabelClass) -> str
        Set: Caption(self: LabelClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: LabelClass) -> bool
        Set: Enabled(self: LabelClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: LabelClass) -> NewFont
        Set: Font(self: LabelClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: LabelClass) -> bool
        Set: FontBold(self: LabelClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: LabelClass) -> bool
        Set: FontItalic(self: LabelClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: LabelClass) -> str
        Set: FontName(self: LabelClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: LabelClass) -> Decimal
        Set: FontSize(self: LabelClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: LabelClass) -> bool
        Set: FontStrikethru(self: LabelClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: LabelClass) -> bool
        Set: FontUnderline(self: LabelClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: LabelClass) -> Int16
        Set: FontWeight(self: LabelClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: LabelClass) -> int
        Set: ForeColor(self: LabelClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: LabelClass) -> StdPicture
        Set: MouseIcon(self: LabelClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: LabelClass) -> fmMousePointer
        Set: MousePointer(self: LabelClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: LabelClass) -> StdPicture
        Set: Picture(self: LabelClass) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: LabelClass) -> fmPicturePosition
        Set: PicturePosition(self: LabelClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: LabelClass) -> fmSpecialEffect
        Set: SpecialEffect(self: LabelClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: LabelClass) -> fmTextAlign
        Set: TextAlign(self: LabelClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: LabelClass) -> bool
        Set: WordWrap(self: LabelClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: LabelClass) = value """
        ...

    @property
    def _Value(self) -> str:
        """
        Get: _Value(self: LabelClass) -> str
        Set: _Value(self: LabelClass) = value
        """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: LabelClass, : LabelControlEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: LabelClass, : LabelControlEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: LabelClass, : LabelControlEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: LabelClass, : LabelControlEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: LabelClass, : LabelControlEvents_ErrorEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: LabelClass, : LabelControlEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: LabelClass, : LabelControlEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: LabelClass, : LabelControlEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: LabelClass, : LabelControlEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: LabelClass, : LabelControlEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: LabelClass, : LabelControlEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: LabelClass, : LabelControlEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: LabelClass, : LabelControlEvents_ErrorEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: LabelClass, : LabelControlEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: LabelClass, : LabelControlEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: LabelClass, : LabelControlEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class LabelControlEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: LabelControlEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: LabelControlEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Click(self): # -> 
        """ Click(self: LabelControlEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: LabelControlEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: LabelControlEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: LabelControlEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: LabelControlEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: LabelControlEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class LabelControlEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: LabelControlEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class LabelControlEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: LabelControlEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class LabelControlEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: LabelControlEvents_ClickEventHandler) """
        ...


class LabelControlEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: LabelControlEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class LabelControlEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: LabelControlEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class LabelControlEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: LabelControlEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class LabelControlEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: LabelControlEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class LabelControlEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LabelControlEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: LabelControlEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class LabelControlEvents_SinkHelper(LabelControlEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcListEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcListEvents_Event, : MdcListEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcListEvents_Event, : MdcListEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcListEvents_Event, : MdcListEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MdcListEvents_Event, : MdcListEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcListEvents_Event, : MdcListEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcListEvents_Event, : MdcListEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcListEvents_Event, : MdcListEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcListEvents_Event, : MdcListEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcListEvents_Event, : MdcListEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcListEvents_Event, : MdcListEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcListEvents_Event, : MdcListEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcListEvents_Event, : MdcListEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcListEvents_Event, : MdcListEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcListEvents_Event, : MdcListEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcListEvents_Event, : MdcListEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MdcListEvents_Event, : MdcListEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcListEvents_Event, : MdcListEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcListEvents_Event, : MdcListEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcListEvents_Event, : MdcListEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcListEvents_Event, : MdcListEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcListEvents_Event, : MdcListEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcListEvents_Event, : MdcListEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcListEvents_Event, : MdcListEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcListEvents_Event, : MdcListEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class ListBox(MdcListEvents_Event, IMdcList): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ListBoxClass(ListBox, __ComObject): # skipped bases: <type 'IMdcList'>, <type 'MdcListEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ListBoxClass) -> int
        Set: BackColor(self: ListBoxClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: ListBoxClass) -> int
        Set: BorderColor(self: ListBoxClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: ListBoxClass) -> bool
        Set: BordersSuppress(self: ListBoxClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: ListBoxClass) -> fmBorderStyle
        Set: BorderStyle(self: ListBoxClass) = value
        """
        ...

    @property
    def BoundColumn(self) -> object:
        """
        Get: BoundColumn(self: ListBoxClass) -> object
        Set: BoundColumn(self: ListBoxClass) = value
        """
        ...

    @property
    def ColumnCount(self) -> int:
        """
        Get: ColumnCount(self: ListBoxClass) -> int
        Set: ColumnCount(self: ListBoxClass) = value
        """
        ...

    @property
    def ColumnHeads(self) -> bool:
        """
        Get: ColumnHeads(self: ListBoxClass) -> bool
        Set: ColumnHeads(self: ListBoxClass) = value
        """
        ...

    @property
    def ColumnWidths(self) -> str:
        """
        Get: ColumnWidths(self: ListBoxClass) -> str
        Set: ColumnWidths(self: ListBoxClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: ListBoxClass) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ListBoxClass) -> bool
        Set: Enabled(self: ListBoxClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ListBoxClass) -> NewFont
        Set: Font(self: ListBoxClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ListBoxClass) -> bool
        Set: FontBold(self: ListBoxClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ListBoxClass) -> bool
        Set: FontItalic(self: ListBoxClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ListBoxClass) -> str
        Set: FontName(self: ListBoxClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ListBoxClass) -> Decimal
        Set: FontSize(self: ListBoxClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ListBoxClass) -> bool
        Set: FontStrikethru(self: ListBoxClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ListBoxClass) -> bool
        Set: FontUnderline(self: ListBoxClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ListBoxClass) -> Int16
        Set: FontWeight(self: ListBoxClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ListBoxClass) -> int
        Set: ForeColor(self: ListBoxClass) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: ListBoxClass) -> fmIMEMode
        Set: IMEMode(self: ListBoxClass) = value
        """
        ...

    @property
    def IntegralHeight(self) -> bool:
        """
        Get: IntegralHeight(self: ListBoxClass) -> bool
        Set: IntegralHeight(self: ListBoxClass) = value
        """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: ListBoxClass) -> int """
        ...

    @property
    def ListCursor(self) -> object:
        """
        Get: ListCursor(self: ListBoxClass) -> object
        Set: ListCursor(self: ListBoxClass) = value
        """
        ...

    @property
    def ListIndex(self) -> object:
        """
        Get: ListIndex(self: ListBoxClass) -> object
        Set: ListIndex(self: ListBoxClass) = value
        """
        ...

    @property
    def ListStyle(self) -> fmListStyle:
        """
        Get: ListStyle(self: ListBoxClass) -> fmListStyle
        Set: ListStyle(self: ListBoxClass) = value
        """
        ...

    @property
    def ListWidth(self) -> object:
        """
        Get: ListWidth(self: ListBoxClass) -> object
        Set: ListWidth(self: ListBoxClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: ListBoxClass) -> bool
        Set: Locked(self: ListBoxClass) = value
        """
        ...

    @property
    def MatchEntry(self) -> fmMatchEntry:
        """
        Get: MatchEntry(self: ListBoxClass) -> fmMatchEntry
        Set: MatchEntry(self: ListBoxClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ListBoxClass) -> StdPicture
        Set: MouseIcon(self: ListBoxClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ListBoxClass) -> fmMousePointer
        Set: MousePointer(self: ListBoxClass) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: ListBoxClass) -> fmMultiSelect
        Set: MultiSelect(self: ListBoxClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: ListBoxClass) -> fmSpecialEffect
        Set: SpecialEffect(self: ListBoxClass) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ListBoxClass) -> str
        Set: Text(self: ListBoxClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: ListBoxClass) -> fmTextAlign
        Set: TextAlign(self: ListBoxClass) = value
        """
        ...

    @property
    def TextColumn(self) -> object:
        """
        Get: TextColumn(self: ListBoxClass) -> object
        Set: TextColumn(self: ListBoxClass) = value
        """
        ...

    @property
    def TopIndex(self) -> object:
        """
        Get: TopIndex(self: ListBoxClass) -> object
        Set: TopIndex(self: ListBoxClass) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: ListBoxClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ListBoxClass) -> object
        Set: Value(self: ListBoxClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ListBoxClass) = value """
        ...


    def AddItem(self, pvargItem:object, pvargIndex:object) -> Tuple_[object, object]:
        """ AddItem(self: ListBoxClass, pvargItem: object, pvargIndex: object) -> (object, object) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ListBoxClass, : MdcListEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ListBoxClass, : MdcListEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: ListBoxClass, : MdcListEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: ListBoxClass, : MdcListEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: ListBoxClass, : MdcListEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ListBoxClass, : MdcListEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: ListBoxClass, : MdcListEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: ListBoxClass, : MdcListEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: ListBoxClass, : MdcListEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: ListBoxClass, : MdcListEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: ListBoxClass, : MdcListEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: ListBoxClass, : MdcListEvents_MouseUpEventHandler) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ListBoxClass) """
        ...

    def RemoveItem(self, pvargIndex:object) -> object:
        """ RemoveItem(self: ListBoxClass, pvargIndex: object) -> object """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ListBoxClass, : MdcListEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ListBoxClass, : MdcListEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: ListBoxClass, : MdcListEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: ListBoxClass, : MdcListEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: ListBoxClass, : MdcListEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ListBoxClass, : MdcListEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: ListBoxClass, : MdcListEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: ListBoxClass, : MdcListEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: ListBoxClass, : MdcListEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: ListBoxClass, : MdcListEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: ListBoxClass, : MdcListEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: ListBoxClass, : MdcListEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class MdcCheckBoxEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcCheckBoxEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcCheckBoxEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcCheckBoxEvents) """
        ...

    def Click(self): # -> 
        """ Click(self: MdcCheckBoxEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcCheckBoxEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcCheckBoxEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcCheckBoxEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcCheckBoxEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcCheckBoxEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcCheckBoxEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcCheckBoxEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcCheckBoxEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcCheckBoxEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcCheckBoxEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcCheckBoxEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcCheckBoxEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcCheckBoxEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcCheckBoxEvents_ChangeEventHandler) """
        ...


class MdcCheckBoxEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcCheckBoxEvents_ClickEventHandler) """
        ...


class MdcCheckBoxEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcCheckBoxEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcCheckBoxEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcCheckBoxEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcCheckBoxEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcCheckBoxEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcCheckBoxEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcCheckBoxEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcCheckBoxEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcCheckBoxEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcCheckBoxEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcCheckBoxEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcCheckBoxEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcCheckBoxEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcCheckBoxEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcCheckBoxEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcCheckBoxEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcCheckBoxEvents_SinkHelper(MdcCheckBoxEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcComboEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcComboEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcComboEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcComboEvents) """
        ...

    def Click(self): # -> 
        """ Click(self: MdcComboEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcComboEvents, Cancel: ReturnBoolean) """
        ...

    def DropButtonClick(self): # -> 
        """ DropButtonClick(self: MdcComboEvents) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcComboEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcComboEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcComboEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcComboEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcComboEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcComboEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcComboEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcComboEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcComboEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcComboEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcComboEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcComboEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcComboEvents_ChangeEventHandler) """
        ...


class MdcComboEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcComboEvents_ClickEventHandler) """
        ...


class MdcComboEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcComboEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcComboEvents_DropButtonClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_DropButtonClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcComboEvents_DropButtonClickEventHandler) """
        ...


class MdcComboEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcComboEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcComboEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcComboEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcComboEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcComboEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcComboEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcComboEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcComboEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcComboEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcComboEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcComboEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcComboEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcComboEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcComboEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcComboEvents_SinkHelper(MdcComboEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_DropButtonClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcListEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcListEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcListEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcListEvents) """
        ...

    def Click(self): # -> 
        """ Click(self: MdcListEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcListEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcListEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcListEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcListEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcListEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcListEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcListEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcListEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcListEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcListEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcListEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcListEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcListEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcListEvents_ChangeEventHandler) """
        ...


class MdcListEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcListEvents_ClickEventHandler) """
        ...


class MdcListEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcListEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcListEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcListEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcListEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcListEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcListEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcListEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcListEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcListEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcListEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcListEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcListEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcListEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcListEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcListEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcListEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcListEvents_SinkHelper(MdcListEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcOptionButtonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcOptionButtonEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcOptionButtonEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcOptionButtonEvents) """
        ...

    def Click(self): # -> 
        """ Click(self: MdcOptionButtonEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcOptionButtonEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcOptionButtonEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcOptionButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcOptionButtonEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcOptionButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcOptionButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcOptionButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcOptionButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcOptionButtonEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcOptionButtonEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcOptionButtonEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcOptionButtonEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcOptionButtonEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcOptionButtonEvents_ChangeEventHandler) """
        ...


class MdcOptionButtonEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcOptionButtonEvents_ClickEventHandler) """
        ...


class MdcOptionButtonEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcOptionButtonEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcOptionButtonEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcOptionButtonEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcOptionButtonEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcOptionButtonEvents_Event, : MdcOptionButtonEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class MdcOptionButtonEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcOptionButtonEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcOptionButtonEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcOptionButtonEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcOptionButtonEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcOptionButtonEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcOptionButtonEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcOptionButtonEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcOptionButtonEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcOptionButtonEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcOptionButtonEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcOptionButtonEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcOptionButtonEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcOptionButtonEvents_SinkHelper(MdcOptionButtonEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcTextEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcTextEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcTextEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcTextEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcTextEvents, Cancel: ReturnBoolean) """
        ...

    def DropButtonClick(self): # -> 
        """ DropButtonClick(self: MdcTextEvents) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcTextEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcTextEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcTextEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcTextEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcTextEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcTextEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcTextEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcTextEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcTextEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcTextEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcTextEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcTextEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcTextEvents_ChangeEventHandler) """
        ...


class MdcTextEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcTextEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcTextEvents_DropButtonClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_DropButtonClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcTextEvents_DropButtonClickEventHandler) """
        ...


class MdcTextEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcTextEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcTextEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcTextEvents_Event, : MdcTextEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcTextEvents_Event, : MdcTextEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcTextEvents_Event, : MdcTextEvents_ChangeEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcTextEvents_Event, : MdcTextEvents_DblClickEventHandler) """
        ...

    def add_DropButtonClick(self): # -> 
        """ add_DropButtonClick(self: MdcTextEvents_Event, : MdcTextEvents_DropButtonClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcTextEvents_Event, : MdcTextEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcTextEvents_Event, : MdcTextEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcTextEvents_Event, : MdcTextEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcTextEvents_Event, : MdcTextEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcTextEvents_Event, : MdcTextEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcTextEvents_Event, : MdcTextEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcTextEvents_Event, : MdcTextEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcTextEvents_Event, : MdcTextEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcTextEvents_Event, : MdcTextEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcTextEvents_Event, : MdcTextEvents_ChangeEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcTextEvents_Event, : MdcTextEvents_DblClickEventHandler) """
        ...

    def remove_DropButtonClick(self): # -> 
        """ remove_DropButtonClick(self: MdcTextEvents_Event, : MdcTextEvents_DropButtonClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcTextEvents_Event, : MdcTextEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcTextEvents_Event, : MdcTextEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcTextEvents_Event, : MdcTextEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcTextEvents_Event, : MdcTextEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcTextEvents_Event, : MdcTextEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcTextEvents_Event, : MdcTextEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcTextEvents_Event, : MdcTextEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    DblClick = ...
    DropButtonClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class MdcTextEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcTextEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcTextEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcTextEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcTextEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcTextEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcTextEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcTextEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcTextEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcTextEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcTextEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcTextEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcTextEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcTextEvents_SinkHelper(MdcTextEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_DblClickDelegate = ...
    m_DropButtonClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MdcToggleButtonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MdcToggleButtonEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MdcToggleButtonEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MdcToggleButtonEvents) """
        ...

    def Click(self): # -> 
        """ Click(self: MdcToggleButtonEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MdcToggleButtonEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MdcToggleButtonEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MdcToggleButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MdcToggleButtonEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MdcToggleButtonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MdcToggleButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MdcToggleButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MdcToggleButtonEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcToggleButtonEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcToggleButtonEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcToggleButtonEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MdcToggleButtonEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MdcToggleButtonEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcToggleButtonEvents_ChangeEventHandler) """
        ...


class MdcToggleButtonEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MdcToggleButtonEvents_ClickEventHandler) """
        ...


class MdcToggleButtonEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MdcToggleButtonEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class MdcToggleButtonEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MdcToggleButtonEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MdcToggleButtonEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MdcToggleButtonEvents_Event, : MdcToggleButtonEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class MdcToggleButtonEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcToggleButtonEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcToggleButtonEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MdcToggleButtonEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MdcToggleButtonEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MdcToggleButtonEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MdcToggleButtonEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcToggleButtonEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcToggleButtonEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcToggleButtonEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcToggleButtonEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MdcToggleButtonEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MdcToggleButtonEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MdcToggleButtonEvents_SinkHelper(MdcToggleButtonEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class MultiPageEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AddControl(self): # -> 
        """ add_AddControl(self: MultiPageEvents_Event, : MultiPageEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MultiPageEvents_Event, : MultiPageEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MultiPageEvents_Event, : MultiPageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MultiPageEvents_Event, : MultiPageEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MultiPageEvents_Event, : MultiPageEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MultiPageEvents_Event, : MultiPageEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MultiPageEvents_Event, : MultiPageEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MultiPageEvents_Event, : MultiPageEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MultiPageEvents_Event, : MultiPageEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MultiPageEvents_Event, : MultiPageEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: MultiPageEvents_Event, : MultiPageEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MultiPageEvents_Event, : MultiPageEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MultiPageEvents_Event, : MultiPageEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MultiPageEvents_Event, : MultiPageEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: MultiPageEvents_Event, : MultiPageEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: MultiPageEvents_Event, : MultiPageEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: MultiPageEvents_Event, : MultiPageEvents_ZoomEventHandler) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: MultiPageEvents_Event, : MultiPageEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MultiPageEvents_Event, : MultiPageEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MultiPageEvents_Event, : MultiPageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MultiPageEvents_Event, : MultiPageEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MultiPageEvents_Event, : MultiPageEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MultiPageEvents_Event, : MultiPageEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MultiPageEvents_Event, : MultiPageEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MultiPageEvents_Event, : MultiPageEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MultiPageEvents_Event, : MultiPageEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MultiPageEvents_Event, : MultiPageEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: MultiPageEvents_Event, : MultiPageEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MultiPageEvents_Event, : MultiPageEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MultiPageEvents_Event, : MultiPageEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MultiPageEvents_Event, : MultiPageEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: MultiPageEvents_Event, : MultiPageEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: MultiPageEvents_Event, : MultiPageEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: MultiPageEvents_Event, : MultiPageEvents_ZoomEventHandler) """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    RemoveControl = ...
    Scroll = ...
    Zoom = ...


class MultiPage(MultiPageEvents_Event, IMultiPage): # skipped bases: <type 'object'>
    """ no doc """
    pass

class MultiPageClass(MultiPage, __ComObject): # skipped bases: <type 'MultiPageEvents_Event'>, <type 'IMultiPage'>, <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: MultiPageClass) -> int
        Set: BackColor(self: MultiPageClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: MultiPageClass) -> bool
        Set: Enabled(self: MultiPageClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: MultiPageClass) -> NewFont
        Set: Font(self: MultiPageClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: MultiPageClass) -> bool
        Set: FontBold(self: MultiPageClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: MultiPageClass) -> bool
        Set: FontItalic(self: MultiPageClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: MultiPageClass) -> str
        Set: FontName(self: MultiPageClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: MultiPageClass) -> Decimal
        Set: FontSize(self: MultiPageClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: MultiPageClass) -> bool
        Set: FontStrikethru(self: MultiPageClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: MultiPageClass) -> bool
        Set: FontUnderline(self: MultiPageClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: MultiPageClass) -> Int16
        Set: FontWeight(self: MultiPageClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: MultiPageClass) -> int
        Set: ForeColor(self: MultiPageClass) = value
        """
        ...

    @property
    def MultiRow(self) -> bool:
        """
        Get: MultiRow(self: MultiPageClass) -> bool
        Set: MultiRow(self: MultiPageClass) = value
        """
        ...

    @property
    def Pages(self) -> Pages:
        """ Get: Pages(self: MultiPageClass) -> Pages """
        ...

    @property
    def SelectedItem(self) -> Page:
        """ Get: SelectedItem(self: MultiPageClass) -> Page """
        ...

    @property
    def Style(self) -> fmTabStyle:
        """
        Get: Style(self: MultiPageClass) -> fmTabStyle
        Set: Style(self: MultiPageClass) = value
        """
        ...

    @property
    def TabFixedHeight(self) -> Single:
        """
        Get: TabFixedHeight(self: MultiPageClass) -> Single
        Set: TabFixedHeight(self: MultiPageClass) = value
        """
        ...

    @property
    def TabFixedWidth(self) -> Single:
        """
        Get: TabFixedWidth(self: MultiPageClass) -> Single
        Set: TabFixedWidth(self: MultiPageClass) = value
        """
        ...

    @property
    def TabOrientation(self) -> fmTabOrientation:
        """
        Get: TabOrientation(self: MultiPageClass) -> fmTabOrientation
        Set: TabOrientation(self: MultiPageClass) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: MultiPageClass) -> int
        Set: Value(self: MultiPageClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: MultiPageClass) = value """
        ...


    def add_AddControl(self): # -> 
        """ add_AddControl(self: MultiPageClass, : MultiPageEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: MultiPageClass, : MultiPageEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: MultiPageClass, : MultiPageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: MultiPageClass, : MultiPageEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: MultiPageClass, : MultiPageEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: MultiPageClass, : MultiPageEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: MultiPageClass, : MultiPageEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: MultiPageClass, : MultiPageEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: MultiPageClass, : MultiPageEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: MultiPageClass, : MultiPageEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: MultiPageClass, : MultiPageEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: MultiPageClass, : MultiPageEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: MultiPageClass, : MultiPageEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: MultiPageClass, : MultiPageEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: MultiPageClass, : MultiPageEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: MultiPageClass, : MultiPageEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: MultiPageClass, : MultiPageEvents_ZoomEventHandler) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: MultiPageClass, : MultiPageEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: MultiPageClass, : MultiPageEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: MultiPageClass, : MultiPageEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: MultiPageClass, : MultiPageEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: MultiPageClass, : MultiPageEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: MultiPageClass, : MultiPageEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: MultiPageClass, : MultiPageEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: MultiPageClass, : MultiPageEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: MultiPageClass, : MultiPageEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: MultiPageClass, : MultiPageEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: MultiPageClass, : MultiPageEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: MultiPageClass, : MultiPageEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: MultiPageClass, : MultiPageEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: MultiPageClass, : MultiPageEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: MultiPageClass, : MultiPageEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: MultiPageClass, : MultiPageEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: MultiPageClass, : MultiPageEvents_ZoomEventHandler) """
        ...

    def _GetTabFixedHeight(self, Height) -> int:
        """ _GetTabFixedHeight(self: MultiPageClass) -> int """
        ...

    def _GetTabFixedWidth(self, Width) -> int:
        """ _GetTabFixedWidth(self: MultiPageClass) -> int """
        ...

    def _SetTabFixedHeight(self, Height:int): # -> 
        """ _SetTabFixedHeight(self: MultiPageClass, Height: int) """
        ...

    def _SetTabFixedWidth(self, Width:int): # -> 
        """ _SetTabFixedWidth(self: MultiPageClass, Width: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    RemoveControl = ...
    Scroll = ...
    Zoom = ...


class MultiPageEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AddControl(self, Index:int, Control:Control): # -> 
        """ AddControl(self: MultiPageEvents, Index: int, Control: Control) """
        ...

    def BeforeDragOver(self, Index:int, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: MultiPageEvents, Index: int, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Index:int, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: MultiPageEvents, Index: int, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: MultiPageEvents) """
        ...

    def Click(self, Index:int): # -> 
        """ Click(self: MultiPageEvents, Index: int) """
        ...

    def DblClick(self, Index:int, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: MultiPageEvents, Index: int, Cancel: ReturnBoolean) """
        ...

    def Error(self, Index:int, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: MultiPageEvents, Index: int, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: MultiPageEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: MultiPageEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: MultiPageEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def Layout(self, Index:int): # -> 
        """ Layout(self: MultiPageEvents, Index: int) """
        ...

    def MouseDown(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: MultiPageEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: MultiPageEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: MultiPageEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def RemoveControl(self, Index:int, Control:Control): # -> 
        """ RemoveControl(self: MultiPageEvents, Index: int, Control: Control) """
        ...

    def Scroll(self, Index:int, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Scroll(self: MultiPageEvents, Index: int, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...

    def Zoom(self, Index, Percent) -> Int16:
        """ Zoom(self: MultiPageEvents, Index: int) -> Int16 """
        ...


class MultiPageEvents_AddControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_AddControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Control:Control): # -> 
        """ Invoke(self: MultiPageEvents_AddControlEventHandler, Index: int, Control: Control) """
        ...


class MultiPageEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MultiPageEvents_BeforeDragOverEventHandler, Index: int, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class MultiPageEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: MultiPageEvents_BeforeDropOrPasteEventHandler, Index: int, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class MultiPageEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: MultiPageEvents_ChangeEventHandler) """
        ...


class MultiPageEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int): # -> 
        """ Invoke(self: MultiPageEvents_ClickEventHandler, Index: int) """
        ...


class MultiPageEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: MultiPageEvents_DblClickEventHandler, Index: int, Cancel: ReturnBoolean) """
        ...


class MultiPageEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: MultiPageEvents_ErrorEventHandler, Index: int, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class MultiPageEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MultiPageEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MultiPageEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: MultiPageEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class MultiPageEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: MultiPageEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class MultiPageEvents_LayoutEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_LayoutEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int): # -> 
        """ Invoke(self: MultiPageEvents_LayoutEventHandler, Index: int) """
        ...


class MultiPageEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MultiPageEvents_MouseDownEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MultiPageEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MultiPageEvents_MouseMoveEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MultiPageEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: MultiPageEvents_MouseUpEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class MultiPageEvents_RemoveControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_RemoveControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Control:Control): # -> 
        """ Invoke(self: MultiPageEvents_RemoveControlEventHandler, Index: int, Control: Control) """
        ...


class MultiPageEvents_ScrollEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_ScrollEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Invoke(self: MultiPageEvents_ScrollEventHandler, Index: int, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...


class MultiPageEvents_SinkHelper(MultiPageEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_AddControlDelegate = ...
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_LayoutDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...
    m_RemoveControlDelegate = ...
    m_ScrollDelegate = ...
    m_ZoomDelegate = ...


class MultiPageEvents_ZoomEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MultiPageEvents_ZoomEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index, Percent) -> Int16:
        """ Invoke(self: MultiPageEvents_ZoomEventHandler, Index: int) -> Int16 """
        ...


class NewFont(Font): # skipped bases: <type 'object'>
    """ no doc """
    pass

class NewFontClass(__ComObject, NewFont): # skipped bases: <type 'Font'>, <type 'object'>
    """ NewFontClass() """
    @property
    def Bold(self) -> bool:
        """
        Get: Bold(self: NewFontClass) -> bool
        Set: Bold(self: NewFontClass) = value
        """
        ...

    @property
    def Charset(self) -> Int16:
        """
        Get: Charset(self: NewFontClass) -> Int16
        Set: Charset(self: NewFontClass) = value
        """
        ...

    @property
    def Italic(self) -> bool:
        """
        Get: Italic(self: NewFontClass) -> bool
        Set: Italic(self: NewFontClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewFontClass) -> str
        Set: Name(self: NewFontClass) = value
        """
        ...

    @property
    def Size(self) -> Decimal:
        """
        Get: Size(self: NewFontClass) -> Decimal
        Set: Size(self: NewFontClass) = value
        """
        ...

    @property
    def Strikethrough(self) -> bool:
        """
        Get: Strikethrough(self: NewFontClass) -> bool
        Set: Strikethrough(self: NewFontClass) = value
        """
        ...

    @property
    def Underline(self) -> bool:
        """
        Get: Underline(self: NewFontClass) -> bool
        Set: Underline(self: NewFontClass) = value
        """
        ...

    @property
    def Weight(self) -> Int16:
        """
        Get: Weight(self: NewFontClass) -> Int16
        Set: Weight(self: NewFontClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class OptionButton(IMdcOptionButton, MdcOptionButtonEvents_Event): # skipped bases: <type 'IMdcCheckBox'>, <type 'object'>
    """ no doc """
    pass

class OptionButtonClass(OptionButton, __ComObject): # skipped bases: <type 'IMdcCheckBox'>, <type 'IMdcOptionButton'>, <type 'MdcOptionButtonEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: OptionButtonClass) -> str
        Set: Accelerator(self: OptionButtonClass) = value
        """
        ...

    @property
    def Alignment(self) -> fmAlignment:
        """
        Get: Alignment(self: OptionButtonClass) -> fmAlignment
        Set: Alignment(self: OptionButtonClass) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: OptionButtonClass) -> bool
        Set: AutoSize(self: OptionButtonClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: OptionButtonClass) -> int
        Set: BackColor(self: OptionButtonClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: OptionButtonClass) -> fmBackStyle
        Set: BackStyle(self: OptionButtonClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: OptionButtonClass) -> bool
        Set: BordersSuppress(self: OptionButtonClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: OptionButtonClass) -> str
        Set: Caption(self: OptionButtonClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: OptionButtonClass) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: OptionButtonClass) -> bool
        Set: Enabled(self: OptionButtonClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: OptionButtonClass) -> NewFont
        Set: Font(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: OptionButtonClass) -> bool
        Set: FontBold(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: OptionButtonClass) -> bool
        Set: FontItalic(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: OptionButtonClass) -> str
        Set: FontName(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: OptionButtonClass) -> Decimal
        Set: FontSize(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: OptionButtonClass) -> bool
        Set: FontStrikethru(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: OptionButtonClass) -> bool
        Set: FontUnderline(self: OptionButtonClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: OptionButtonClass) -> Int16
        Set: FontWeight(self: OptionButtonClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: OptionButtonClass) -> int
        Set: ForeColor(self: OptionButtonClass) = value
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: OptionButtonClass) -> str
        Set: GroupName(self: OptionButtonClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: OptionButtonClass) -> bool
        Set: Locked(self: OptionButtonClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: OptionButtonClass) -> StdPicture
        Set: MouseIcon(self: OptionButtonClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: OptionButtonClass) -> fmMousePointer
        Set: MousePointer(self: OptionButtonClass) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: OptionButtonClass) -> fmMultiSelect
        Set: MultiSelect(self: OptionButtonClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: OptionButtonClass) -> StdPicture
        Set: Picture(self: OptionButtonClass) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: OptionButtonClass) -> fmPicturePosition
        Set: PicturePosition(self: OptionButtonClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmButtonEffect:
        """
        Get: SpecialEffect(self: OptionButtonClass) -> fmButtonEffect
        Set: SpecialEffect(self: OptionButtonClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: OptionButtonClass) -> fmTextAlign
        Set: TextAlign(self: OptionButtonClass) = value
        """
        ...

    @property
    def TripleState(self) -> bool:
        """
        Get: TripleState(self: OptionButtonClass) -> bool
        Set: TripleState(self: OptionButtonClass) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: OptionButtonClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: OptionButtonClass) -> object
        Set: Value(self: OptionButtonClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: OptionButtonClass) -> bool
        Set: WordWrap(self: OptionButtonClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: OptionButtonClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: OptionButtonClass, : MdcOptionButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: OptionButtonClass, : MdcOptionButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: OptionButtonClass, : MdcOptionButtonEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: OptionButtonClass, : MdcOptionButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: OptionButtonClass, : MdcOptionButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: OptionButtonClass, : MdcOptionButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: OptionButtonClass, : MdcOptionButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: OptionButtonClass, : MdcOptionButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: OptionButtonClass, : MdcOptionButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: OptionButtonClass, : MdcOptionButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: OptionButtonClass, : MdcOptionButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: OptionButtonClass, : MdcOptionButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: OptionButtonClass, : MdcOptionButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: OptionButtonClass, : MdcOptionButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: OptionButtonClass, : MdcOptionButtonEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: OptionButtonClass, : MdcOptionButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: OptionButtonClass, : MdcOptionButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: OptionButtonClass, : MdcOptionButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: OptionButtonClass, : MdcOptionButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: OptionButtonClass, : MdcOptionButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: OptionButtonClass, : MdcOptionButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: OptionButtonClass, : MdcOptionButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: OptionButtonClass, : MdcOptionButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: OptionButtonClass, : MdcOptionButtonEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class OptionFrameEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AddControl(self, Control:Control): # -> 
        """ AddControl(self: OptionFrameEvents, Control: Control) """
        ...

    def BeforeDragOver(self, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: OptionFrameEvents, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: OptionFrameEvents, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Click(self): # -> 
        """ Click(self: OptionFrameEvents) """
        ...

    def DblClick(self, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: OptionFrameEvents, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: OptionFrameEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: OptionFrameEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: OptionFrameEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: OptionFrameEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def Layout(self): # -> 
        """ Layout(self: OptionFrameEvents) """
        ...

    def MouseDown(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: OptionFrameEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: OptionFrameEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: OptionFrameEvents, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def RemoveControl(self, Control:Control): # -> 
        """ RemoveControl(self: OptionFrameEvents, Control: Control) """
        ...

    def Scroll(self, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Scroll(self: OptionFrameEvents, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...

    def Zoom(self, Percent) -> Int16:
        """ Zoom(self: OptionFrameEvents) -> Int16 """
        ...


class OptionFrameEvents_AddControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_AddControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Control:Control): # -> 
        """ Invoke(self: OptionFrameEvents_AddControlEventHandler, Control: Control) """
        ...


class OptionFrameEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Control:Control, Data:DataObject, X:Single, Y:Single, State:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: OptionFrameEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Control: Control, Data: DataObject, X: Single, Y: Single, State: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class OptionFrameEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Control:Control, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: OptionFrameEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Control: Control, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class OptionFrameEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: OptionFrameEvents_ClickEventHandler) """
        ...


class OptionFrameEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: OptionFrameEvents_DblClickEventHandler, Cancel: ReturnBoolean) """
        ...


class OptionFrameEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: OptionFrameEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class OptionFrameEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: OptionFrameEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class OptionFrameEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: OptionFrameEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class OptionFrameEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: OptionFrameEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class OptionFrameEvents_LayoutEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_LayoutEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: OptionFrameEvents_LayoutEventHandler) """
        ...


class OptionFrameEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: OptionFrameEvents_MouseDownEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class OptionFrameEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: OptionFrameEvents_MouseMoveEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class OptionFrameEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: OptionFrameEvents_MouseUpEventHandler, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class OptionFrameEvents_RemoveControlEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_RemoveControlEventHandler(: object, : UIntPtr) """
    def Invoke(self, Control:Control): # -> 
        """ Invoke(self: OptionFrameEvents_RemoveControlEventHandler, Control: Control) """
        ...


class OptionFrameEvents_ScrollEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_ScrollEventHandler(: object, : UIntPtr) """
    def Invoke(self, ActionX:fmScrollAction, ActionY:fmScrollAction, RequestDx:Single, RequestDy:Single, ActualDx:ReturnSingle, ActualDy:ReturnSingle): # -> 
        """ Invoke(self: OptionFrameEvents_ScrollEventHandler, ActionX: fmScrollAction, ActionY: fmScrollAction, RequestDx: Single, RequestDy: Single, ActualDx: ReturnSingle, ActualDy: ReturnSingle) """
        ...


class OptionFrameEvents_SinkHelper(OptionFrameEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_AddControlDelegate = ...
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_LayoutDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...
    m_RemoveControlDelegate = ...
    m_ScrollDelegate = ...
    m_ZoomDelegate = ...


class OptionFrameEvents_ZoomEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OptionFrameEvents_ZoomEventHandler(: object, : UIntPtr) """
    def Invoke(self, Percent) -> Int16:
        """ Invoke(self: OptionFrameEvents_ZoomEventHandler) -> Int16 """
        ...


class Page(IPage): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PageClass(__ComObject, Page): # skipped bases: <type 'IPage'>, <type 'object'>
    """ PageClass() """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: PageClass) -> str
        Set: Accelerator(self: PageClass) = value
        """
        ...

    @property
    def ActiveControl(self) -> Control:
        """ Get: ActiveControl(self: PageClass) -> Control """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: PageClass) -> bool """
        ...

    @property
    def CanRedo(self) -> bool:
        """ Get: CanRedo(self: PageClass) -> bool """
        ...

    @property
    def CanUndo(self) -> bool:
        """ Get: CanUndo(self: PageClass) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: PageClass) -> str
        Set: Caption(self: PageClass) = value
        """
        ...

    @property
    def Controls(self) -> Controls:
        """ Get: Controls(self: PageClass) -> Controls """
        ...

    @property
    def ControlTipText(self) -> str:
        """
        Get: ControlTipText(self: PageClass) -> str
        Set: ControlTipText(self: PageClass) = value
        """
        ...

    @property
    def Cycle(self) -> fmCycle:
        """
        Get: Cycle(self: PageClass) -> fmCycle
        Set: Cycle(self: PageClass) = value
        """
        ...

    @property
    def DesignMode(self) -> fmMode:
        """
        Get: DesignMode(self: PageClass) -> fmMode
        Set: DesignMode(self: PageClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: PageClass) -> bool
        Set: Enabled(self: PageClass) = value
        """
        ...

    @property
    def GridX(self) -> Single:
        """
        Get: GridX(self: PageClass) -> Single
        Set: GridX(self: PageClass) = value
        """
        ...

    @property
    def GridY(self) -> Single:
        """
        Get: GridY(self: PageClass) -> Single
        Set: GridY(self: PageClass) = value
        """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: PageClass) -> int
        Set: Index(self: PageClass) = value
        """
        ...

    @property
    def InsideHeight(self) -> Single:
        """ Get: InsideHeight(self: PageClass) -> Single """
        ...

    @property
    def InsideWidth(self) -> Single:
        """ Get: InsideWidth(self: PageClass) -> Single """
        ...

    @property
    def KeepScrollBarsVisible(self) -> fmScrollBars:
        """
        Get: KeepScrollBarsVisible(self: PageClass) -> fmScrollBars
        Set: KeepScrollBarsVisible(self: PageClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PageClass) -> str
        Set: Name(self: PageClass) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageClass) -> object """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: PageClass) -> StdPicture
        Set: Picture(self: PageClass) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: PageClass) -> fmPictureAlignment
        Set: PictureAlignment(self: PageClass) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: PageClass) -> fmPictureSizeMode
        Set: PictureSizeMode(self: PageClass) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: PageClass) -> bool
        Set: PictureTiling(self: PageClass) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: PageClass) -> fmScrollBars
        Set: ScrollBars(self: PageClass) = value
        """
        ...

    @property
    def ScrollHeight(self) -> Single:
        """
        Get: ScrollHeight(self: PageClass) -> Single
        Set: ScrollHeight(self: PageClass) = value
        """
        ...

    @property
    def ScrollLeft(self) -> Single:
        """
        Get: ScrollLeft(self: PageClass) -> Single
        Set: ScrollLeft(self: PageClass) = value
        """
        ...

    @property
    def ScrollTop(self) -> Single:
        """
        Get: ScrollTop(self: PageClass) -> Single
        Set: ScrollTop(self: PageClass) = value
        """
        ...

    @property
    def ScrollWidth(self) -> Single:
        """
        Get: ScrollWidth(self: PageClass) -> Single
        Set: ScrollWidth(self: PageClass) = value
        """
        ...

    @property
    def Selected(self) -> Controls:
        """ Get: Selected(self: PageClass) -> Controls """
        ...

    @property
    def ShowGridDots(self) -> fmMode:
        """
        Get: ShowGridDots(self: PageClass) -> fmMode
        Set: ShowGridDots(self: PageClass) = value
        """
        ...

    @property
    def ShowToolbox(self) -> fmMode:
        """
        Get: ShowToolbox(self: PageClass) -> fmMode
        Set: ShowToolbox(self: PageClass) = value
        """
        ...

    @property
    def SnapToGrid(self) -> fmMode:
        """
        Get: SnapToGrid(self: PageClass) -> fmMode
        Set: SnapToGrid(self: PageClass) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: PageClass) -> str
        Set: Tag(self: PageClass) = value
        """
        ...

    @property
    def TransitionEffect(self) -> fmTransitionEffect:
        """
        Get: TransitionEffect(self: PageClass) -> fmTransitionEffect
        Set: TransitionEffect(self: PageClass) = value
        """
        ...

    @property
    def TransitionPeriod(self) -> int:
        """
        Get: TransitionPeriod(self: PageClass) -> int
        Set: TransitionPeriod(self: PageClass) = value
        """
        ...

    @property
    def VerticalScrollBarSide(self) -> fmVerticalScrollBarSide:
        """
        Get: VerticalScrollBarSide(self: PageClass) -> fmVerticalScrollBarSide
        Set: VerticalScrollBarSide(self: PageClass) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: PageClass) -> bool
        Set: Visible(self: PageClass) = value
        """
        ...

    @property
    def Zoom(self) -> Int16:
        """
        Get: Zoom(self: PageClass) -> Int16
        Set: Zoom(self: PageClass) = value
        """
        ...


    def Copy(self): # -> 
        """ Copy(self: PageClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: PageClass) """
        ...

    def Paste(self): # -> 
        """ Paste(self: PageClass) """
        ...

    def RedoAction(self): # -> 
        """ RedoAction(self: PageClass) """
        ...

    def Repaint(self): # -> 
        """ Repaint(self: PageClass) """
        ...

    def Scroll(self, xAction:object, yAction:object): # -> 
        """ Scroll(self: PageClass, xAction: object, yAction: object) """
        ...

    def SetDefaultTabOrder(self): # -> 
        """ SetDefaultTabOrder(self: PageClass) """
        ...

    def UndoAction(self): # -> 
        """ UndoAction(self: PageClass) """
        ...

    def _GetGridX(self, GridX) -> int:
        """ _GetGridX(self: PageClass) -> int """
        ...

    def _GetGridY(self, GridY) -> int:
        """ _GetGridY(self: PageClass) -> int """
        ...

    def _GetInsideHeight(self, InsideHeight) -> int:
        """ _GetInsideHeight(self: PageClass) -> int """
        ...

    def _GetInsideWidth(self, InsideWidth) -> int:
        """ _GetInsideWidth(self: PageClass) -> int """
        ...

    def _GetScrollHeight(self, ScrollHeight) -> int:
        """ _GetScrollHeight(self: PageClass) -> int """
        ...

    def _GetScrollLeft(self, ScrollLeft) -> int:
        """ _GetScrollLeft(self: PageClass) -> int """
        ...

    def _GetScrollTop(self, ScrollTop) -> int:
        """ _GetScrollTop(self: PageClass) -> int """
        ...

    def _GetScrollWidth(self, ScrollWidth) -> int:
        """ _GetScrollWidth(self: PageClass) -> int """
        ...

    def _SetGridX(self, GridX:int): # -> 
        """ _SetGridX(self: PageClass, GridX: int) """
        ...

    def _SetGridY(self, GridY:int): # -> 
        """ _SetGridY(self: PageClass, GridY: int) """
        ...

    def _SetScrollHeight(self, ScrollHeight:int): # -> 
        """ _SetScrollHeight(self: PageClass, ScrollHeight: int) """
        ...

    def _SetScrollLeft(self, ScrollLeft:int): # -> 
        """ _SetScrollLeft(self: PageClass, ScrollLeft: int) """
        ...

    def _SetScrollTop(self, ScrollTop:int): # -> 
        """ _SetScrollTop(self: PageClass, ScrollTop: int) """
        ...

    def _SetScrollWidth(self, ScrollWidth:int): # -> 
        """ _SetScrollWidth(self: PageClass, ScrollWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Pages(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Pages) -> int """
        ...


    def Add(self, bstrName:object, bstrCaption:object, lIndex:object) -> Page:
        """ Add(self: Pages, bstrName: object, bstrCaption: object, lIndex: object) -> Page """
        ...

    def Clear(self): # -> 
        """ Clear(self: Pages) """
        ...

    def Enum(self) -> object:
        """ Enum(self: Pages) -> object """
        ...

    def Item(self, varg:object) -> object:
        """ Item(self: Pages, varg: object) -> object """
        ...

    def Remove(self, varg:object): # -> 
        """ Remove(self: Pages, varg: object) """
        ...

    def _AddCtrl(self, clsid:int, bstrName:str, bstrCaption:str) -> Tuple_[Page, int]:
        """ _AddCtrl(self: Pages, clsid: int, bstrName: str, bstrCaption: str) -> (Page, int) """
        ...

    def _GetItemByIndex(self, lIndex:int) -> Control:
        """ _GetItemByIndex(self: Pages, lIndex: int) -> Control """
        ...

    def _GetItemByName(self, pstrName:str) -> Control:
        """ _GetItemByName(self: Pages, pstrName: str) -> Control """
        ...

    def _InsertCtrl(self, clsid:int, bstrName:str, bstrCaption:str, lIndex:int) -> Tuple_[Page, int]:
        """ _InsertCtrl(self: Pages, clsid: int, bstrName: str, bstrCaption: str, lIndex: int) -> (Page, int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ReturnBoolean(IReturnBoolean): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReturnBooleanClass(ReturnBoolean, __ComObject): # skipped bases: <type 'IReturnBoolean'>, <type 'object'>
    """ ReturnBooleanClass() """
    @property
    def Value(self) -> bool:
        """
        Get: Value(self: ReturnBooleanClass) -> bool
        Set: Value(self: ReturnBooleanClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ReturnEffect(IReturnEffect): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReturnEffectClass(ReturnEffect, __ComObject): # skipped bases: <type 'IReturnEffect'>, <type 'object'>
    """ ReturnEffectClass() """
    @property
    def Value(self) -> fmDropEffect:
        """
        Get: Value(self: ReturnEffectClass) -> fmDropEffect
        Set: Value(self: ReturnEffectClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ReturnInteger(IReturnInteger): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReturnIntegerClass(ReturnInteger, __ComObject): # skipped bases: <type 'IReturnInteger'>, <type 'object'>
    """ ReturnIntegerClass() """
    @property
    def Value(self) -> int:
        """
        Get: Value(self: ReturnIntegerClass) -> int
        Set: Value(self: ReturnIntegerClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ReturnSingle(IReturnSingle): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReturnSingleClass(ReturnSingle, __ComObject): # skipped bases: <type 'IReturnSingle'>, <type 'object'>
    """ ReturnSingleClass() """
    @property
    def Value(self) -> Single:
        """
        Get: Value(self: ReturnSingleClass) -> Single
        Set: Value(self: ReturnSingleClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ReturnString(IReturnString): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReturnStringClass(ReturnString, __ComObject): # skipped bases: <type 'IReturnString'>, <type 'object'>
    """ ReturnStringClass() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: ReturnStringClass) -> str
        Set: Value(self: ReturnStringClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ScrollbarEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ScrollbarEvents_Event, : ScrollbarEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ScrollbarEvents_Event, : ScrollbarEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: ScrollbarEvents_Event, : ScrollbarEvents_ChangeEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ScrollbarEvents_Event, : ScrollbarEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyUpEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: ScrollbarEvents_Event, : ScrollbarEvents_ScrollEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ScrollbarEvents_Event, : ScrollbarEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ScrollbarEvents_Event, : ScrollbarEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: ScrollbarEvents_Event, : ScrollbarEvents_ChangeEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ScrollbarEvents_Event, : ScrollbarEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: ScrollbarEvents_Event, : ScrollbarEvents_KeyUpEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: ScrollbarEvents_Event, : ScrollbarEvents_ScrollEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Scroll = ...


class ScrollBar(ScrollbarEvents_Event, IScrollbar): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ScrollBarClass(ScrollBar, __ComObject): # skipped bases: <type 'IScrollbar'>, <type 'ScrollbarEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ScrollBarClass) -> int
        Set: BackColor(self: ScrollBarClass) = value
        """
        ...

    @property
    def Delay(self) -> int:
        """
        Get: Delay(self: ScrollBarClass) -> int
        Set: Delay(self: ScrollBarClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ScrollBarClass) -> bool
        Set: Enabled(self: ScrollBarClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ScrollBarClass) -> int
        Set: ForeColor(self: ScrollBarClass) = value
        """
        ...

    @property
    def LargeChange(self) -> int:
        """
        Get: LargeChange(self: ScrollBarClass) -> int
        Set: LargeChange(self: ScrollBarClass) = value
        """
        ...

    @property
    def Max(self) -> int:
        """
        Get: Max(self: ScrollBarClass) -> int
        Set: Max(self: ScrollBarClass) = value
        """
        ...

    @property
    def Min(self) -> int:
        """
        Get: Min(self: ScrollBarClass) -> int
        Set: Min(self: ScrollBarClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ScrollBarClass) -> StdPicture
        Set: MouseIcon(self: ScrollBarClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ScrollBarClass) -> fmMousePointer
        Set: MousePointer(self: ScrollBarClass) = value
        """
        ...

    @property
    def Orientation(self) -> fmOrientation:
        """
        Get: Orientation(self: ScrollBarClass) -> fmOrientation
        Set: Orientation(self: ScrollBarClass) = value
        """
        ...

    @property
    def ProportionalThumb(self) -> bool:
        """
        Get: ProportionalThumb(self: ScrollBarClass) -> bool
        Set: ProportionalThumb(self: ScrollBarClass) = value
        """
        ...

    @property
    def SmallChange(self) -> int:
        """
        Get: SmallChange(self: ScrollBarClass) -> int
        Set: SmallChange(self: ScrollBarClass) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: ScrollBarClass) -> int
        Set: Value(self: ScrollBarClass) = value
        """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ScrollBarClass, : ScrollbarEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ScrollBarClass, : ScrollbarEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: ScrollBarClass, : ScrollbarEvents_ChangeEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ScrollBarClass, : ScrollbarEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: ScrollBarClass, : ScrollbarEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: ScrollBarClass, : ScrollbarEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: ScrollBarClass, : ScrollbarEvents_KeyUpEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: ScrollBarClass, : ScrollbarEvents_ScrollEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ScrollBarClass, : ScrollbarEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ScrollBarClass, : ScrollbarEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: ScrollBarClass, : ScrollbarEvents_ChangeEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ScrollBarClass, : ScrollbarEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: ScrollBarClass, : ScrollbarEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: ScrollBarClass, : ScrollbarEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: ScrollBarClass, : ScrollbarEvents_KeyUpEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: ScrollBarClass, : ScrollbarEvents_ScrollEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Scroll = ...


class ScrollbarEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: ScrollbarEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: ScrollbarEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: ScrollbarEvents) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: ScrollbarEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: ScrollbarEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: ScrollbarEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: ScrollbarEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def Scroll(self): # -> 
        """ Scroll(self: ScrollbarEvents) """
        ...


class ScrollbarEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: ScrollbarEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class ScrollbarEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: ScrollbarEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class ScrollbarEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ScrollbarEvents_ChangeEventHandler) """
        ...


class ScrollbarEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: ScrollbarEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class ScrollbarEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: ScrollbarEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class ScrollbarEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: ScrollbarEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class ScrollbarEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: ScrollbarEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class ScrollbarEvents_ScrollEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ScrollbarEvents_ScrollEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ScrollbarEvents_ScrollEventHandler) """
        ...


class ScrollbarEvents_SinkHelper(ScrollbarEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_ScrollDelegate = ...


class SpinbuttonEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: SpinbuttonEvents_Event, : SpinbuttonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: SpinbuttonEvents_Event, : SpinbuttonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: SpinbuttonEvents_Event, : SpinbuttonEvents_ChangeEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: SpinbuttonEvents_Event, : SpinbuttonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyUpEventHandler) """
        ...

    def add_SpinDown(self): # -> 
        """ add_SpinDown(self: SpinbuttonEvents_Event, : SpinbuttonEvents_SpinDownEventHandler) """
        ...

    def add_SpinUp(self): # -> 
        """ add_SpinUp(self: SpinbuttonEvents_Event, : SpinbuttonEvents_SpinUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: SpinbuttonEvents_Event, : SpinbuttonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: SpinbuttonEvents_Event, : SpinbuttonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: SpinbuttonEvents_Event, : SpinbuttonEvents_ChangeEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: SpinbuttonEvents_Event, : SpinbuttonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: SpinbuttonEvents_Event, : SpinbuttonEvents_KeyUpEventHandler) """
        ...

    def remove_SpinDown(self): # -> 
        """ remove_SpinDown(self: SpinbuttonEvents_Event, : SpinbuttonEvents_SpinDownEventHandler) """
        ...

    def remove_SpinUp(self): # -> 
        """ remove_SpinUp(self: SpinbuttonEvents_Event, : SpinbuttonEvents_SpinUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    SpinDown = ...
    SpinUp = ...


class SpinButton(ISpinbutton, SpinbuttonEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SpinButtonClass(SpinButton, __ComObject): # skipped bases: <type 'SpinbuttonEvents_Event'>, <type 'ISpinbutton'>, <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: SpinButtonClass) -> int
        Set: BackColor(self: SpinButtonClass) = value
        """
        ...

    @property
    def Delay(self) -> int:
        """
        Get: Delay(self: SpinButtonClass) -> int
        Set: Delay(self: SpinButtonClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: SpinButtonClass) -> bool
        Set: Enabled(self: SpinButtonClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: SpinButtonClass) -> int
        Set: ForeColor(self: SpinButtonClass) = value
        """
        ...

    @property
    def Max(self) -> int:
        """
        Get: Max(self: SpinButtonClass) -> int
        Set: Max(self: SpinButtonClass) = value
        """
        ...

    @property
    def Min(self) -> int:
        """
        Get: Min(self: SpinButtonClass) -> int
        Set: Min(self: SpinButtonClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: SpinButtonClass) -> StdPicture
        Set: MouseIcon(self: SpinButtonClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: SpinButtonClass) -> fmMousePointer
        Set: MousePointer(self: SpinButtonClass) = value
        """
        ...

    @property
    def Orientation(self) -> fmOrientation:
        """
        Get: Orientation(self: SpinButtonClass) -> fmOrientation
        Set: Orientation(self: SpinButtonClass) = value
        """
        ...

    @property
    def SmallChange(self) -> int:
        """
        Get: SmallChange(self: SpinButtonClass) -> int
        Set: SmallChange(self: SpinButtonClass) = value
        """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: SpinButtonClass) -> int
        Set: Value(self: SpinButtonClass) = value
        """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: SpinButtonClass, : SpinbuttonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: SpinButtonClass, : SpinbuttonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: SpinButtonClass, : SpinbuttonEvents_ChangeEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: SpinButtonClass, : SpinbuttonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: SpinButtonClass, : SpinbuttonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: SpinButtonClass, : SpinbuttonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: SpinButtonClass, : SpinbuttonEvents_KeyUpEventHandler) """
        ...

    def add_SpinDown(self): # -> 
        """ add_SpinDown(self: SpinButtonClass, : SpinbuttonEvents_SpinDownEventHandler) """
        ...

    def add_SpinUp(self): # -> 
        """ add_SpinUp(self: SpinButtonClass, : SpinbuttonEvents_SpinUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: SpinButtonClass, : SpinbuttonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: SpinButtonClass, : SpinbuttonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: SpinButtonClass, : SpinbuttonEvents_ChangeEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: SpinButtonClass, : SpinbuttonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: SpinButtonClass, : SpinbuttonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: SpinButtonClass, : SpinbuttonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: SpinButtonClass, : SpinbuttonEvents_KeyUpEventHandler) """
        ...

    def remove_SpinDown(self): # -> 
        """ remove_SpinDown(self: SpinButtonClass, : SpinbuttonEvents_SpinDownEventHandler) """
        ...

    def remove_SpinUp(self): # -> 
        """ remove_SpinUp(self: SpinButtonClass, : SpinbuttonEvents_SpinUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    SpinDown = ...
    SpinUp = ...


class SpinbuttonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: SpinbuttonEvents, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: SpinbuttonEvents, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: SpinbuttonEvents) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: SpinbuttonEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: SpinbuttonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: SpinbuttonEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: SpinbuttonEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def SpinDown(self): # -> 
        """ SpinDown(self: SpinbuttonEvents) """
        ...

    def SpinUp(self): # -> 
        """ SpinUp(self: SpinbuttonEvents) """
        ...


class SpinbuttonEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: SpinbuttonEvents_BeforeDragOverEventHandler, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class SpinbuttonEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: SpinbuttonEvents_BeforeDropOrPasteEventHandler, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class SpinbuttonEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: SpinbuttonEvents_ChangeEventHandler) """
        ...


class SpinbuttonEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: SpinbuttonEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class SpinbuttonEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: SpinbuttonEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class SpinbuttonEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: SpinbuttonEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class SpinbuttonEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: SpinbuttonEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class SpinbuttonEvents_SinkHelper(SpinbuttonEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_SpinDownDelegate = ...
    m_SpinUpDelegate = ...


class SpinbuttonEvents_SpinDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_SpinDownEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: SpinbuttonEvents_SpinDownEventHandler) """
        ...


class SpinbuttonEvents_SpinUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SpinbuttonEvents_SpinUpEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: SpinbuttonEvents_SpinUpEventHandler) """
        ...


class Tab: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: Tab) -> str
        Set: Accelerator(self: Tab) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: Tab) -> str
        Set: Caption(self: Tab) = value
        """
        ...

    @property
    def ControlTipText(self) -> str:
        """
        Get: ControlTipText(self: Tab) -> str
        Set: ControlTipText(self: Tab) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Tab) -> bool
        Set: Enabled(self: Tab) = value
        """
        ...

    @property
    def Index(self) -> int:
        """
        Get: Index(self: Tab) -> int
        Set: Index(self: Tab) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Tab) -> str
        Set: Name(self: Tab) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: Tab) -> str
        Set: Tag(self: Tab) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Tab) -> bool
        Set: Visible(self: Tab) = value
        """
        ...



class Tabs(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Tabs) -> int """
        ...


    def Add(self, bstrName:object, bstrCaption:object, lIndex:object) -> Tab:
        """ Add(self: Tabs, bstrName: object, bstrCaption: object, lIndex: object) -> Tab """
        ...

    def Clear(self): # -> 
        """ Clear(self: Tabs) """
        ...

    def Enum(self) -> object:
        """ Enum(self: Tabs) -> object """
        ...

    def Item(self, varg:object) -> object:
        """ Item(self: Tabs, varg: object) -> object """
        ...

    def Remove(self, varg:object): # -> 
        """ Remove(self: Tabs, varg: object) """
        ...

    def _Add(self, bstrName:str, bstrCaption:str) -> Tab:
        """ _Add(self: Tabs, bstrName: str, bstrCaption: str) -> Tab """
        ...

    def _GetItemByIndex(self, lIndex:int) -> Tab:
        """ _GetItemByIndex(self: Tabs, lIndex: int) -> Tab """
        ...

    def _GetItemByName(self, bstr:str) -> Tab:
        """ _GetItemByName(self: Tabs, bstr: str) -> Tab """
        ...

    def _Insert(self, bstrName:str, bstrCaption:str, lIndex:int) -> Tab:
        """ _Insert(self: Tabs, bstrName: str, bstrCaption: str, lIndex: int) -> Tab """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class TabStripEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: TabStripEvents_Event, : TabStripEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: TabStripEvents_Event, : TabStripEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: TabStripEvents_Event, : TabStripEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: TabStripEvents_Event, : TabStripEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: TabStripEvents_Event, : TabStripEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: TabStripEvents_Event, : TabStripEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: TabStripEvents_Event, : TabStripEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: TabStripEvents_Event, : TabStripEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: TabStripEvents_Event, : TabStripEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: TabStripEvents_Event, : TabStripEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: TabStripEvents_Event, : TabStripEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: TabStripEvents_Event, : TabStripEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: TabStripEvents_Event, : TabStripEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: TabStripEvents_Event, : TabStripEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: TabStripEvents_Event, : TabStripEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: TabStripEvents_Event, : TabStripEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: TabStripEvents_Event, : TabStripEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: TabStripEvents_Event, : TabStripEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: TabStripEvents_Event, : TabStripEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: TabStripEvents_Event, : TabStripEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: TabStripEvents_Event, : TabStripEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: TabStripEvents_Event, : TabStripEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: TabStripEvents_Event, : TabStripEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: TabStripEvents_Event, : TabStripEvents_MouseUpEventHandler) """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class TabStrip(ITabStrip, TabStripEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class TabStripClass(__ComObject, TabStrip): # skipped bases: <type 'TabStripEvents_Event'>, <type 'ITabStrip'>, <type 'object'>
    """ no doc """
    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: TabStripClass) -> int
        Set: BackColor(self: TabStripClass) = value
        """
        ...

    @property
    def ClientHeight(self) -> Single:
        """ Get: ClientHeight(self: TabStripClass) -> Single """
        ...

    @property
    def ClientLeft(self) -> Single:
        """ Get: ClientLeft(self: TabStripClass) -> Single """
        ...

    @property
    def ClientTop(self) -> Single:
        """ Get: ClientTop(self: TabStripClass) -> Single """
        ...

    @property
    def ClientWidth(self) -> Single:
        """ Get: ClientWidth(self: TabStripClass) -> Single """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: TabStripClass) -> bool
        Set: Enabled(self: TabStripClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: TabStripClass) -> NewFont
        Set: Font(self: TabStripClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: TabStripClass) -> bool
        Set: FontBold(self: TabStripClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: TabStripClass) -> bool
        Set: FontItalic(self: TabStripClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: TabStripClass) -> str
        Set: FontName(self: TabStripClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: TabStripClass) -> Decimal
        Set: FontSize(self: TabStripClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: TabStripClass) -> bool
        Set: FontStrikethru(self: TabStripClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: TabStripClass) -> bool
        Set: FontUnderline(self: TabStripClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: TabStripClass) -> Int16
        Set: FontWeight(self: TabStripClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: TabStripClass) -> int
        Set: ForeColor(self: TabStripClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: TabStripClass) -> StdPicture
        Set: MouseIcon(self: TabStripClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: TabStripClass) -> fmMousePointer
        Set: MousePointer(self: TabStripClass) = value
        """
        ...

    @property
    def MultiRow(self) -> bool:
        """
        Get: MultiRow(self: TabStripClass) -> bool
        Set: MultiRow(self: TabStripClass) = value
        """
        ...

    @property
    def SelectedItem(self) -> Tab:
        """ Get: SelectedItem(self: TabStripClass) -> Tab """
        ...

    @property
    def Style(self) -> fmTabStyle:
        """
        Get: Style(self: TabStripClass) -> fmTabStyle
        Set: Style(self: TabStripClass) = value
        """
        ...

    @property
    def TabFixedHeight(self) -> Single:
        """
        Get: TabFixedHeight(self: TabStripClass) -> Single
        Set: TabFixedHeight(self: TabStripClass) = value
        """
        ...

    @property
    def TabFixedWidth(self) -> Single:
        """
        Get: TabFixedWidth(self: TabStripClass) -> Single
        Set: TabFixedWidth(self: TabStripClass) = value
        """
        ...

    @property
    def TabOrientation(self) -> fmTabOrientation:
        """
        Get: TabOrientation(self: TabStripClass) -> fmTabOrientation
        Set: TabOrientation(self: TabStripClass) = value
        """
        ...

    @property
    def Tabs(self) -> Tabs:
        """ Get: Tabs(self: TabStripClass) -> Tabs """
        ...

    @property
    def Value(self) -> int:
        """
        Get: Value(self: TabStripClass) -> int
        Set: Value(self: TabStripClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: TabStripClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: TabStripClass, : TabStripEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: TabStripClass, : TabStripEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: TabStripClass, : TabStripEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: TabStripClass, : TabStripEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: TabStripClass, : TabStripEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: TabStripClass, : TabStripEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: TabStripClass, : TabStripEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: TabStripClass, : TabStripEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: TabStripClass, : TabStripEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: TabStripClass, : TabStripEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: TabStripClass, : TabStripEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: TabStripClass, : TabStripEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: TabStripClass, : TabStripEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: TabStripClass, : TabStripEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: TabStripClass, : TabStripEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: TabStripClass, : TabStripEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: TabStripClass, : TabStripEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: TabStripClass, : TabStripEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: TabStripClass, : TabStripEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: TabStripClass, : TabStripEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: TabStripClass, : TabStripEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: TabStripClass, : TabStripEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: TabStripClass, : TabStripEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: TabStripClass, : TabStripEvents_MouseUpEventHandler) """
        ...

    def _GetClientHeight(self, ClientHeight) -> int:
        """ _GetClientHeight(self: TabStripClass) -> int """
        ...

    def _GetClientLeft(self, ClientLeft) -> int:
        """ _GetClientLeft(self: TabStripClass) -> int """
        ...

    def _GetClientTop(self, ClientTop) -> int:
        """ _GetClientTop(self: TabStripClass) -> int """
        ...

    def _GetClientWidth(self, ClientWidth) -> int:
        """ _GetClientWidth(self: TabStripClass) -> int """
        ...

    def _GetTabFixedHeight(self, TabFixedHeight) -> int:
        """ _GetTabFixedHeight(self: TabStripClass) -> int """
        ...

    def _GetTabFixedWidth(self, TabFixedWidth) -> int:
        """ _GetTabFixedWidth(self: TabStripClass) -> int """
        ...

    def _SetTabFixedHeight(self, TabFixedHeight:int): # -> 
        """ _SetTabFixedHeight(self: TabStripClass, TabFixedHeight: int) """
        ...

    def _SetTabFixedWidth(self, TabFixedWidth:int): # -> 
        """ _SetTabFixedWidth(self: TabStripClass, TabFixedWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class TabStripEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeDragOver(self, Index:int, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDragOver(self: TabStripEvents, Index: int, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...

    def BeforeDropOrPaste(self, Index:int, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ BeforeDropOrPaste(self: TabStripEvents, Index: int, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...

    def Change(self): # -> 
        """ Change(self: TabStripEvents) """
        ...

    def Click(self, Index:int): # -> 
        """ Click(self: TabStripEvents, Index: int) """
        ...

    def DblClick(self, Index:int, Cancel:ReturnBoolean): # -> 
        """ DblClick(self: TabStripEvents, Index: int, Cancel: ReturnBoolean) """
        ...

    def Error(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Error(self: TabStripEvents, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...

    def KeyDown(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyDown(self: TabStripEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def KeyPress(self, KeyAscii:ReturnInteger): # -> 
        """ KeyPress(self: TabStripEvents, KeyAscii: ReturnInteger) """
        ...

    def KeyUp(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ KeyUp(self: TabStripEvents, KeyCode: ReturnInteger, Shift: Int16) """
        ...

    def MouseDown(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseDown(self: TabStripEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseMove(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseMove(self: TabStripEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...

    def MouseUp(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ MouseUp(self: TabStripEvents, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class TabStripEvents_BeforeDragOverEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_BeforeDragOverEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean, Data:DataObject, X:Single, Y:Single, DragState:fmDragState, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: TabStripEvents_BeforeDragOverEventHandler, Index: int, Cancel: ReturnBoolean, Data: DataObject, X: Single, Y: Single, DragState: fmDragState, Effect: ReturnEffect, Shift: Int16) """
        ...


class TabStripEvents_BeforeDropOrPasteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_BeforeDropOrPasteEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean, Action:fmAction, Data:DataObject, X:Single, Y:Single, Effect:ReturnEffect, Shift:Int16): # -> 
        """ Invoke(self: TabStripEvents_BeforeDropOrPasteEventHandler, Index: int, Cancel: ReturnBoolean, Action: fmAction, Data: DataObject, X: Single, Y: Single, Effect: ReturnEffect, Shift: Int16) """
        ...


class TabStripEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_ChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: TabStripEvents_ChangeEventHandler) """
        ...


class TabStripEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int): # -> 
        """ Invoke(self: TabStripEvents_ClickEventHandler, Index: int) """
        ...


class TabStripEvents_DblClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_DblClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Cancel:ReturnBoolean): # -> 
        """ Invoke(self: TabStripEvents_DblClickEventHandler, Index: int, Cancel: ReturnBoolean) """
        ...


class TabStripEvents_ErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_ErrorEventHandler(: object, : UIntPtr) """
    def Invoke(self, Number:Int16, Description:ReturnString, SCode:int, Source:str, HelpFile:str, HelpContext:int, CancelDisplay:ReturnBoolean): # -> 
        """ Invoke(self: TabStripEvents_ErrorEventHandler, Number: Int16, Description: ReturnString, SCode: int, Source: str, HelpFile: str, HelpContext: int, CancelDisplay: ReturnBoolean) """
        ...


class TabStripEvents_KeyDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_KeyDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: TabStripEvents_KeyDownEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class TabStripEvents_KeyPressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_KeyPressEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyAscii:ReturnInteger): # -> 
        """ Invoke(self: TabStripEvents_KeyPressEventHandler, KeyAscii: ReturnInteger) """
        ...


class TabStripEvents_KeyUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_KeyUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, KeyCode:ReturnInteger, Shift:Int16): # -> 
        """ Invoke(self: TabStripEvents_KeyUpEventHandler, KeyCode: ReturnInteger, Shift: Int16) """
        ...


class TabStripEvents_MouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_MouseDownEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: TabStripEvents_MouseDownEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class TabStripEvents_MouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_MouseMoveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: TabStripEvents_MouseMoveEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class TabStripEvents_MouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TabStripEvents_MouseUpEventHandler(: object, : UIntPtr) """
    def Invoke(self, Index:int, Button:Int16, Shift:Int16, X:Single, Y:Single): # -> 
        """ Invoke(self: TabStripEvents_MouseUpEventHandler, Index: int, Button: Int16, Shift: Int16, X: Single, Y: Single) """
        ...


class TabStripEvents_SinkHelper(TabStripEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeDragOverDelegate = ...
    m_BeforeDropOrPasteDelegate = ...
    m_ChangeDelegate = ...
    m_ClickDelegate = ...
    m_DblClickDelegate = ...
    m_dwCookie = ...
    m_ErrorDelegate = ...
    m_KeyDownDelegate = ...
    m_KeyPressDelegate = ...
    m_KeyUpDelegate = ...
    m_MouseDownDelegate = ...
    m_MouseMoveDelegate = ...
    m_MouseUpDelegate = ...


class TextBox(MdcTextEvents_Event, IMdcText): # skipped bases: <type 'object'>
    """ no doc """
    pass

class TextBoxClass(TextBox, __ComObject): # skipped bases: <type 'IMdcText'>, <type 'MdcTextEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: TextBoxClass) -> bool
        Set: AutoSize(self: TextBoxClass) = value
        """
        ...

    @property
    def AutoTab(self) -> bool:
        """
        Get: AutoTab(self: TextBoxClass) -> bool
        Set: AutoTab(self: TextBoxClass) = value
        """
        ...

    @property
    def AutoWordSelect(self) -> bool:
        """
        Get: AutoWordSelect(self: TextBoxClass) -> bool
        Set: AutoWordSelect(self: TextBoxClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: TextBoxClass) -> int
        Set: BackColor(self: TextBoxClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: TextBoxClass) -> fmBackStyle
        Set: BackStyle(self: TextBoxClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: TextBoxClass) -> int
        Set: BorderColor(self: TextBoxClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: TextBoxClass) -> bool
        Set: BordersSuppress(self: TextBoxClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: TextBoxClass) -> fmBorderStyle
        Set: BorderStyle(self: TextBoxClass) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: TextBoxClass) -> bool """
        ...

    @property
    def CurLine(self) -> int:
        """
        Get: CurLine(self: TextBoxClass) -> int
        Set: CurLine(self: TextBoxClass) = value
        """
        ...

    @property
    def CurTargetX(self) -> int:
        """ Get: CurTargetX(self: TextBoxClass) -> int """
        ...

    @property
    def CurTargetY(self) -> int:
        """ Get: CurTargetY(self: TextBoxClass) -> int """
        ...

    @property
    def CurX(self) -> int:
        """
        Get: CurX(self: TextBoxClass) -> int
        Set: CurX(self: TextBoxClass) = value
        """
        ...

    @property
    def CurY(self) -> int:
        """
        Get: CurY(self: TextBoxClass) -> int
        Set: CurY(self: TextBoxClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: TextBoxClass) -> fmDisplayStyle """
        ...

    @property
    def DragBehavior(self) -> fmDragBehavior:
        """
        Get: DragBehavior(self: TextBoxClass) -> fmDragBehavior
        Set: DragBehavior(self: TextBoxClass) = value
        """
        ...

    @property
    def DropButtonStyle(self) -> fmDropButtonStyle:
        """
        Get: DropButtonStyle(self: TextBoxClass) -> fmDropButtonStyle
        Set: DropButtonStyle(self: TextBoxClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: TextBoxClass) -> bool
        Set: Enabled(self: TextBoxClass) = value
        """
        ...

    @property
    def EnterFieldBehavior(self) -> fmEnterFieldBehavior:
        """
        Get: EnterFieldBehavior(self: TextBoxClass) -> fmEnterFieldBehavior
        Set: EnterFieldBehavior(self: TextBoxClass) = value
        """
        ...

    @property
    def EnterKeyBehavior(self) -> bool:
        """
        Get: EnterKeyBehavior(self: TextBoxClass) -> bool
        Set: EnterKeyBehavior(self: TextBoxClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: TextBoxClass) -> NewFont
        Set: Font(self: TextBoxClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: TextBoxClass) -> bool
        Set: FontBold(self: TextBoxClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: TextBoxClass) -> bool
        Set: FontItalic(self: TextBoxClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: TextBoxClass) -> str
        Set: FontName(self: TextBoxClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: TextBoxClass) -> Decimal
        Set: FontSize(self: TextBoxClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: TextBoxClass) -> bool
        Set: FontStrikethru(self: TextBoxClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: TextBoxClass) -> bool
        Set: FontUnderline(self: TextBoxClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: TextBoxClass) -> Int16
        Set: FontWeight(self: TextBoxClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: TextBoxClass) -> int
        Set: ForeColor(self: TextBoxClass) = value
        """
        ...

    @property
    def HideSelection(self) -> bool:
        """
        Get: HideSelection(self: TextBoxClass) -> bool
        Set: HideSelection(self: TextBoxClass) = value
        """
        ...

    @property
    def IMEMode(self) -> fmIMEMode:
        """
        Get: IMEMode(self: TextBoxClass) -> fmIMEMode
        Set: IMEMode(self: TextBoxClass) = value
        """
        ...

    @property
    def IntegralHeight(self) -> bool:
        """
        Get: IntegralHeight(self: TextBoxClass) -> bool
        Set: IntegralHeight(self: TextBoxClass) = value
        """
        ...

    @property
    def LineCount(self) -> int:
        """ Get: LineCount(self: TextBoxClass) -> int """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: TextBoxClass) -> bool
        Set: Locked(self: TextBoxClass) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: TextBoxClass) -> int
        Set: MaxLength(self: TextBoxClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: TextBoxClass) -> StdPicture
        Set: MouseIcon(self: TextBoxClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: TextBoxClass) -> fmMousePointer
        Set: MousePointer(self: TextBoxClass) = value
        """
        ...

    @property
    def MultiLine(self) -> bool:
        """
        Get: MultiLine(self: TextBoxClass) -> bool
        Set: MultiLine(self: TextBoxClass) = value
        """
        ...

    @property
    def PasswordChar(self) -> str:
        """
        Get: PasswordChar(self: TextBoxClass) -> str
        Set: PasswordChar(self: TextBoxClass) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: TextBoxClass) -> fmScrollBars
        Set: ScrollBars(self: TextBoxClass) = value
        """
        ...

    @property
    def SelectionMargin(self) -> bool:
        """
        Get: SelectionMargin(self: TextBoxClass) -> bool
        Set: SelectionMargin(self: TextBoxClass) = value
        """
        ...

    @property
    def SelLength(self) -> int:
        """
        Get: SelLength(self: TextBoxClass) -> int
        Set: SelLength(self: TextBoxClass) = value
        """
        ...

    @property
    def SelStart(self) -> int:
        """
        Get: SelStart(self: TextBoxClass) -> int
        Set: SelStart(self: TextBoxClass) = value
        """
        ...

    @property
    def SelText(self) -> str:
        """
        Get: SelText(self: TextBoxClass) -> str
        Set: SelText(self: TextBoxClass) = value
        """
        ...

    @property
    def ShowDropButtonWhen(self) -> fmShowDropButtonWhen:
        """
        Get: ShowDropButtonWhen(self: TextBoxClass) -> fmShowDropButtonWhen
        Set: ShowDropButtonWhen(self: TextBoxClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: TextBoxClass) -> fmSpecialEffect
        Set: SpecialEffect(self: TextBoxClass) = value
        """
        ...

    @property
    def TabKeyBehavior(self) -> bool:
        """
        Get: TabKeyBehavior(self: TextBoxClass) -> bool
        Set: TabKeyBehavior(self: TextBoxClass) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextBoxClass) -> str
        Set: Text(self: TextBoxClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: TextBoxClass) -> fmTextAlign
        Set: TextAlign(self: TextBoxClass) = value
        """
        ...

    @property
    def TextLength(self) -> int:
        """ Get: TextLength(self: TextBoxClass) -> int """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: TextBoxClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: TextBoxClass) -> object
        Set: Value(self: TextBoxClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: TextBoxClass) -> bool
        Set: WordWrap(self: TextBoxClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: TextBoxClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: TextBoxClass, : MdcTextEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: TextBoxClass, : MdcTextEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: TextBoxClass, : MdcTextEvents_ChangeEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: TextBoxClass, : MdcTextEvents_DblClickEventHandler) """
        ...

    def add_DropButtonClick(self): # -> 
        """ add_DropButtonClick(self: TextBoxClass, : MdcTextEvents_DropButtonClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: TextBoxClass, : MdcTextEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: TextBoxClass, : MdcTextEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: TextBoxClass, : MdcTextEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: TextBoxClass, : MdcTextEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: TextBoxClass, : MdcTextEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: TextBoxClass, : MdcTextEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: TextBoxClass, : MdcTextEvents_MouseUpEventHandler) """
        ...

    def Copy(self): # -> 
        """ Copy(self: TextBoxClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: TextBoxClass) """
        ...

    def Paste(self): # -> 
        """ Paste(self: TextBoxClass) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: TextBoxClass, : MdcTextEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: TextBoxClass, : MdcTextEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: TextBoxClass, : MdcTextEvents_ChangeEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: TextBoxClass, : MdcTextEvents_DblClickEventHandler) """
        ...

    def remove_DropButtonClick(self): # -> 
        """ remove_DropButtonClick(self: TextBoxClass, : MdcTextEvents_DropButtonClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: TextBoxClass, : MdcTextEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: TextBoxClass, : MdcTextEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: TextBoxClass, : MdcTextEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: TextBoxClass, : MdcTextEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: TextBoxClass, : MdcTextEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: TextBoxClass, : MdcTextEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: TextBoxClass, : MdcTextEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    DblClick = ...
    DropButtonClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class ToggleButton(MdcToggleButtonEvents_Event, IMdcToggleButton): # skipped bases: <type 'IMdcCheckBox'>, <type 'object'>
    """ no doc """
    pass

class ToggleButtonClass(__ComObject, ToggleButton): # skipped bases: <type 'IMdcToggleButton'>, <type 'IMdcCheckBox'>, <type 'MdcToggleButtonEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Accelerator(self) -> str:
        """
        Get: Accelerator(self: ToggleButtonClass) -> str
        Set: Accelerator(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Alignment(self) -> fmAlignment:
        """
        Get: Alignment(self: ToggleButtonClass) -> fmAlignment
        Set: Alignment(self: ToggleButtonClass) = value
        """
        ...

    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: ToggleButtonClass) -> bool
        Set: AutoSize(self: ToggleButtonClass) = value
        """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: ToggleButtonClass) -> int
        Set: BackColor(self: ToggleButtonClass) = value
        """
        ...

    @property
    def BackStyle(self) -> fmBackStyle:
        """
        Get: BackStyle(self: ToggleButtonClass) -> fmBackStyle
        Set: BackStyle(self: ToggleButtonClass) = value
        """
        ...

    @property
    def BordersSuppress(self) -> bool:
        """
        Get: BordersSuppress(self: ToggleButtonClass) -> bool
        Set: BordersSuppress(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ToggleButtonClass) -> str
        Set: Caption(self: ToggleButtonClass) = value
        """
        ...

    @property
    def DisplayStyle(self) -> fmDisplayStyle:
        """ Get: DisplayStyle(self: ToggleButtonClass) -> fmDisplayStyle """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ToggleButtonClass) -> bool
        Set: Enabled(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: ToggleButtonClass) -> NewFont
        Set: Font(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontBold(self) -> bool:
        """
        Get: FontBold(self: ToggleButtonClass) -> bool
        Set: FontBold(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontItalic(self) -> bool:
        """
        Get: FontItalic(self: ToggleButtonClass) -> bool
        Set: FontItalic(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: ToggleButtonClass) -> str
        Set: FontName(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontSize(self) -> Decimal:
        """
        Get: FontSize(self: ToggleButtonClass) -> Decimal
        Set: FontSize(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontStrikethru(self) -> bool:
        """
        Get: FontStrikethru(self: ToggleButtonClass) -> bool
        Set: FontStrikethru(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontUnderline(self) -> bool:
        """
        Get: FontUnderline(self: ToggleButtonClass) -> bool
        Set: FontUnderline(self: ToggleButtonClass) = value
        """
        ...

    @property
    def FontWeight(self) -> Int16:
        """
        Get: FontWeight(self: ToggleButtonClass) -> Int16
        Set: FontWeight(self: ToggleButtonClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: ToggleButtonClass) -> int
        Set: ForeColor(self: ToggleButtonClass) = value
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: ToggleButtonClass) -> str
        Set: GroupName(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """
        Get: Locked(self: ToggleButtonClass) -> bool
        Set: Locked(self: ToggleButtonClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: ToggleButtonClass) -> StdPicture
        Set: MouseIcon(self: ToggleButtonClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: ToggleButtonClass) -> fmMousePointer
        Set: MousePointer(self: ToggleButtonClass) = value
        """
        ...

    @property
    def MultiSelect(self) -> fmMultiSelect:
        """
        Get: MultiSelect(self: ToggleButtonClass) -> fmMultiSelect
        Set: MultiSelect(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: ToggleButtonClass) -> StdPicture
        Set: Picture(self: ToggleButtonClass) = value
        """
        ...

    @property
    def PicturePosition(self) -> fmPicturePosition:
        """
        Get: PicturePosition(self: ToggleButtonClass) -> fmPicturePosition
        Set: PicturePosition(self: ToggleButtonClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmButtonEffect:
        """
        Get: SpecialEffect(self: ToggleButtonClass) -> fmButtonEffect
        Set: SpecialEffect(self: ToggleButtonClass) = value
        """
        ...

    @property
    def TextAlign(self) -> fmTextAlign:
        """
        Get: TextAlign(self: ToggleButtonClass) -> fmTextAlign
        Set: TextAlign(self: ToggleButtonClass) = value
        """
        ...

    @property
    def TripleState(self) -> bool:
        """
        Get: TripleState(self: ToggleButtonClass) -> bool
        Set: TripleState(self: ToggleButtonClass) = value
        """
        ...

    @property
    def Valid(self) -> bool:
        """ Get: Valid(self: ToggleButtonClass) -> bool """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ToggleButtonClass) -> object
        Set: Value(self: ToggleButtonClass) = value
        """
        ...

    @property
    def WordWrap(self) -> bool:
        """
        Get: WordWrap(self: ToggleButtonClass) -> bool
        Set: WordWrap(self: ToggleButtonClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: ToggleButtonClass) = value """
        ...


    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: ToggleButtonClass, : MdcToggleButtonEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: ToggleButtonClass, : MdcToggleButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Change(self): # -> 
        """ add_Change(self: ToggleButtonClass, : MdcToggleButtonEvents_ChangeEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: ToggleButtonClass, : MdcToggleButtonEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: ToggleButtonClass, : MdcToggleButtonEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: ToggleButtonClass, : MdcToggleButtonEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyUpEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseUpEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: ToggleButtonClass, : MdcToggleButtonEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: ToggleButtonClass, : MdcToggleButtonEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Change(self): # -> 
        """ remove_Change(self: ToggleButtonClass, : MdcToggleButtonEvents_ChangeEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: ToggleButtonClass, : MdcToggleButtonEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: ToggleButtonClass, : MdcToggleButtonEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: ToggleButtonClass, : MdcToggleButtonEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: ToggleButtonClass, : MdcToggleButtonEvents_KeyUpEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: ToggleButtonClass, : MdcToggleButtonEvents_MouseUpEventHandler) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Change = ...
    Click = ...
    DblClick = ...
    Error = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...


class _UserForm(IOptionFrame): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DrawBuffer(self) -> int:
        """
        Get: DrawBuffer(self: _UserForm) -> int
        Set: DrawBuffer(self: _UserForm) = value
        """
        ...



class UserForm(FormEvents_Event, _UserForm): # skipped bases: <type 'IOptionFrame'>, <type 'object'>
    """ no doc """
    pass

class UserFormClass(__ComObject, UserForm): # skipped bases: <type '_UserForm'>, <type 'IOptionFrame'>, <type 'FormEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def ActiveControl(self) -> Control:
        """ Get: ActiveControl(self: UserFormClass) -> Control """
        ...

    @property
    def BackColor(self) -> int:
        """
        Get: BackColor(self: UserFormClass) -> int
        Set: BackColor(self: UserFormClass) = value
        """
        ...

    @property
    def BorderColor(self) -> int:
        """
        Get: BorderColor(self: UserFormClass) -> int
        Set: BorderColor(self: UserFormClass) = value
        """
        ...

    @property
    def BorderStyle(self) -> fmBorderStyle:
        """
        Get: BorderStyle(self: UserFormClass) -> fmBorderStyle
        Set: BorderStyle(self: UserFormClass) = value
        """
        ...

    @property
    def CanPaste(self) -> bool:
        """ Get: CanPaste(self: UserFormClass) -> bool """
        ...

    @property
    def CanRedo(self) -> bool:
        """ Get: CanRedo(self: UserFormClass) -> bool """
        ...

    @property
    def CanUndo(self) -> bool:
        """ Get: CanUndo(self: UserFormClass) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: UserFormClass) -> str
        Set: Caption(self: UserFormClass) = value
        """
        ...

    @property
    def Controls(self) -> Controls:
        """ Get: Controls(self: UserFormClass) -> Controls """
        ...

    @property
    def Cycle(self) -> fmCycle:
        """
        Get: Cycle(self: UserFormClass) -> fmCycle
        Set: Cycle(self: UserFormClass) = value
        """
        ...

    @property
    def DesignMode(self) -> fmMode:
        """
        Get: DesignMode(self: UserFormClass) -> fmMode
        Set: DesignMode(self: UserFormClass) = value
        """
        ...

    @property
    def DrawBuffer(self) -> int:
        """
        Get: DrawBuffer(self: UserFormClass) -> int
        Set: DrawBuffer(self: UserFormClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: UserFormClass) -> bool
        Set: Enabled(self: UserFormClass) = value
        """
        ...

    @property
    def Font(self) -> NewFont:
        """
        Get: Font(self: UserFormClass) -> NewFont
        Set: Font(self: UserFormClass) = value
        """
        ...

    @property
    def ForeColor(self) -> int:
        """
        Get: ForeColor(self: UserFormClass) -> int
        Set: ForeColor(self: UserFormClass) = value
        """
        ...

    @property
    def GridX(self) -> Single:
        """
        Get: GridX(self: UserFormClass) -> Single
        Set: GridX(self: UserFormClass) = value
        """
        ...

    @property
    def GridY(self) -> Single:
        """
        Get: GridY(self: UserFormClass) -> Single
        Set: GridY(self: UserFormClass) = value
        """
        ...

    @property
    def InsideHeight(self) -> Single:
        """ Get: InsideHeight(self: UserFormClass) -> Single """
        ...

    @property
    def InsideWidth(self) -> Single:
        """ Get: InsideWidth(self: UserFormClass) -> Single """
        ...

    @property
    def KeepScrollBarsVisible(self) -> fmScrollBars:
        """
        Get: KeepScrollBarsVisible(self: UserFormClass) -> fmScrollBars
        Set: KeepScrollBarsVisible(self: UserFormClass) = value
        """
        ...

    @property
    def MouseIcon(self): # -> StdPicture
        """
        Get: MouseIcon(self: UserFormClass) -> StdPicture
        Set: MouseIcon(self: UserFormClass) = value
        """
        ...

    @property
    def MousePointer(self) -> fmMousePointer:
        """
        Get: MousePointer(self: UserFormClass) -> fmMousePointer
        Set: MousePointer(self: UserFormClass) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: UserFormClass) -> StdPicture
        Set: Picture(self: UserFormClass) = value
        """
        ...

    @property
    def PictureAlignment(self) -> fmPictureAlignment:
        """
        Get: PictureAlignment(self: UserFormClass) -> fmPictureAlignment
        Set: PictureAlignment(self: UserFormClass) = value
        """
        ...

    @property
    def PictureSizeMode(self) -> fmPictureSizeMode:
        """
        Get: PictureSizeMode(self: UserFormClass) -> fmPictureSizeMode
        Set: PictureSizeMode(self: UserFormClass) = value
        """
        ...

    @property
    def PictureTiling(self) -> bool:
        """
        Get: PictureTiling(self: UserFormClass) -> bool
        Set: PictureTiling(self: UserFormClass) = value
        """
        ...

    @property
    def ScrollBars(self) -> fmScrollBars:
        """
        Get: ScrollBars(self: UserFormClass) -> fmScrollBars
        Set: ScrollBars(self: UserFormClass) = value
        """
        ...

    @property
    def ScrollHeight(self) -> Single:
        """
        Get: ScrollHeight(self: UserFormClass) -> Single
        Set: ScrollHeight(self: UserFormClass) = value
        """
        ...

    @property
    def ScrollLeft(self) -> Single:
        """
        Get: ScrollLeft(self: UserFormClass) -> Single
        Set: ScrollLeft(self: UserFormClass) = value
        """
        ...

    @property
    def ScrollTop(self) -> Single:
        """
        Get: ScrollTop(self: UserFormClass) -> Single
        Set: ScrollTop(self: UserFormClass) = value
        """
        ...

    @property
    def ScrollWidth(self) -> Single:
        """
        Get: ScrollWidth(self: UserFormClass) -> Single
        Set: ScrollWidth(self: UserFormClass) = value
        """
        ...

    @property
    def Selected(self) -> Controls:
        """ Get: Selected(self: UserFormClass) -> Controls """
        ...

    @property
    def ShowGridDots(self) -> fmMode:
        """
        Get: ShowGridDots(self: UserFormClass) -> fmMode
        Set: ShowGridDots(self: UserFormClass) = value
        """
        ...

    @property
    def ShowToolbox(self) -> fmMode:
        """
        Get: ShowToolbox(self: UserFormClass) -> fmMode
        Set: ShowToolbox(self: UserFormClass) = value
        """
        ...

    @property
    def SnapToGrid(self) -> fmMode:
        """
        Get: SnapToGrid(self: UserFormClass) -> fmMode
        Set: SnapToGrid(self: UserFormClass) = value
        """
        ...

    @property
    def SpecialEffect(self) -> fmSpecialEffect:
        """
        Get: SpecialEffect(self: UserFormClass) -> fmSpecialEffect
        Set: SpecialEffect(self: UserFormClass) = value
        """
        ...

    @property
    def VerticalScrollBarSide(self) -> fmVerticalScrollBarSide:
        """
        Get: VerticalScrollBarSide(self: UserFormClass) -> fmVerticalScrollBarSide
        Set: VerticalScrollBarSide(self: UserFormClass) = value
        """
        ...

    @property
    def Zoom(self) -> Int16:
        """
        Get: Zoom(self: UserFormClass) -> Int16
        Set: Zoom(self: UserFormClass) = value
        """
        ...

    @property
    def _Font_Reserved(self): # -> 
        """ Set: _Font_Reserved(self: UserFormClass) = value """
        ...


    def add_AddControl(self): # -> 
        """ add_AddControl(self: UserFormClass, : FormEvents_AddControlEventHandler) """
        ...

    def add_BeforeDragOver(self): # -> 
        """ add_BeforeDragOver(self: UserFormClass, : FormEvents_BeforeDragOverEventHandler) """
        ...

    def add_BeforeDropOrPaste(self): # -> 
        """ add_BeforeDropOrPaste(self: UserFormClass, : FormEvents_BeforeDropOrPasteEventHandler) """
        ...

    def add_Click(self): # -> 
        """ add_Click(self: UserFormClass, : FormEvents_ClickEventHandler) """
        ...

    def add_DblClick(self): # -> 
        """ add_DblClick(self: UserFormClass, : FormEvents_DblClickEventHandler) """
        ...

    def add_Error(self): # -> 
        """ add_Error(self: UserFormClass, : FormEvents_ErrorEventHandler) """
        ...

    def add_KeyDown(self): # -> 
        """ add_KeyDown(self: UserFormClass, : FormEvents_KeyDownEventHandler) """
        ...

    def add_KeyPress(self): # -> 
        """ add_KeyPress(self: UserFormClass, : FormEvents_KeyPressEventHandler) """
        ...

    def add_KeyUp(self): # -> 
        """ add_KeyUp(self: UserFormClass, : FormEvents_KeyUpEventHandler) """
        ...

    def add_Layout(self): # -> 
        """ add_Layout(self: UserFormClass, : FormEvents_LayoutEventHandler) """
        ...

    def add_MouseDown(self): # -> 
        """ add_MouseDown(self: UserFormClass, : FormEvents_MouseDownEventHandler) """
        ...

    def add_MouseMove(self): # -> 
        """ add_MouseMove(self: UserFormClass, : FormEvents_MouseMoveEventHandler) """
        ...

    def add_MouseUp(self): # -> 
        """ add_MouseUp(self: UserFormClass, : FormEvents_MouseUpEventHandler) """
        ...

    def add_RemoveControl(self): # -> 
        """ add_RemoveControl(self: UserFormClass, : FormEvents_RemoveControlEventHandler) """
        ...

    def add_Scroll(self): # -> 
        """ add_Scroll(self: UserFormClass, : FormEvents_ScrollEventHandler) """
        ...

    def add_Zoom(self): # -> 
        """ add_Zoom(self: UserFormClass, : FormEvents_ZoomEventHandler) """
        ...

    def Copy(self): # -> 
        """ Copy(self: UserFormClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: UserFormClass) """
        ...

    def Paste(self): # -> 
        """ Paste(self: UserFormClass) """
        ...

    def RedoAction(self): # -> 
        """ RedoAction(self: UserFormClass) """
        ...

    def remove_AddControl(self): # -> 
        """ remove_AddControl(self: UserFormClass, : FormEvents_AddControlEventHandler) """
        ...

    def remove_BeforeDragOver(self): # -> 
        """ remove_BeforeDragOver(self: UserFormClass, : FormEvents_BeforeDragOverEventHandler) """
        ...

    def remove_BeforeDropOrPaste(self): # -> 
        """ remove_BeforeDropOrPaste(self: UserFormClass, : FormEvents_BeforeDropOrPasteEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: UserFormClass, : FormEvents_ClickEventHandler) """
        ...

    def remove_DblClick(self): # -> 
        """ remove_DblClick(self: UserFormClass, : FormEvents_DblClickEventHandler) """
        ...

    def remove_Error(self): # -> 
        """ remove_Error(self: UserFormClass, : FormEvents_ErrorEventHandler) """
        ...

    def remove_KeyDown(self): # -> 
        """ remove_KeyDown(self: UserFormClass, : FormEvents_KeyDownEventHandler) """
        ...

    def remove_KeyPress(self): # -> 
        """ remove_KeyPress(self: UserFormClass, : FormEvents_KeyPressEventHandler) """
        ...

    def remove_KeyUp(self): # -> 
        """ remove_KeyUp(self: UserFormClass, : FormEvents_KeyUpEventHandler) """
        ...

    def remove_Layout(self): # -> 
        """ remove_Layout(self: UserFormClass, : FormEvents_LayoutEventHandler) """
        ...

    def remove_MouseDown(self): # -> 
        """ remove_MouseDown(self: UserFormClass, : FormEvents_MouseDownEventHandler) """
        ...

    def remove_MouseMove(self): # -> 
        """ remove_MouseMove(self: UserFormClass, : FormEvents_MouseMoveEventHandler) """
        ...

    def remove_MouseUp(self): # -> 
        """ remove_MouseUp(self: UserFormClass, : FormEvents_MouseUpEventHandler) """
        ...

    def remove_RemoveControl(self): # -> 
        """ remove_RemoveControl(self: UserFormClass, : FormEvents_RemoveControlEventHandler) """
        ...

    def remove_Scroll(self): # -> 
        """ remove_Scroll(self: UserFormClass, : FormEvents_ScrollEventHandler) """
        ...

    def remove_Zoom(self): # -> 
        """ remove_Zoom(self: UserFormClass, : FormEvents_ZoomEventHandler) """
        ...

    def Repaint(self): # -> 
        """ Repaint(self: UserFormClass) """
        ...

    def Scroll(self, xAction:object, yAction:object): # -> 
        """ Scroll(self: UserFormClass, xAction: object, yAction: object) """
        ...

    def SetDefaultTabOrder(self): # -> 
        """ SetDefaultTabOrder(self: UserFormClass) """
        ...

    def UndoAction(self): # -> 
        """ UndoAction(self: UserFormClass) """
        ...

    def _GetGridX(self, GridX) -> int:
        """ _GetGridX(self: UserFormClass) -> int """
        ...

    def _GetGridY(self, GridY) -> int:
        """ _GetGridY(self: UserFormClass) -> int """
        ...

    def _GetInsideHeight(self, InsideHeight) -> int:
        """ _GetInsideHeight(self: UserFormClass) -> int """
        ...

    def _GetInsideWidth(self, InsideWidth) -> int:
        """ _GetInsideWidth(self: UserFormClass) -> int """
        ...

    def _GetScrollHeight(self, ScrollHeight) -> int:
        """ _GetScrollHeight(self: UserFormClass) -> int """
        ...

    def _GetScrollLeft(self, ScrollLeft) -> int:
        """ _GetScrollLeft(self: UserFormClass) -> int """
        ...

    def _GetScrollTop(self, ScrollTop) -> int:
        """ _GetScrollTop(self: UserFormClass) -> int """
        ...

    def _GetScrollWidth(self, ScrollWidth) -> int:
        """ _GetScrollWidth(self: UserFormClass) -> int """
        ...

    def _SetGridX(self, GridX:int): # -> 
        """ _SetGridX(self: UserFormClass, GridX: int) """
        ...

    def _SetGridY(self, GridY:int): # -> 
        """ _SetGridY(self: UserFormClass, GridY: int) """
        ...

    def _SetScrollHeight(self, ScrollHeight:int): # -> 
        """ _SetScrollHeight(self: UserFormClass, ScrollHeight: int) """
        ...

    def _SetScrollLeft(self, ScrollLeft:int): # -> 
        """ _SetScrollLeft(self: UserFormClass, ScrollLeft: int) """
        ...

    def _SetScrollTop(self, ScrollTop:int): # -> 
        """ _SetScrollTop(self: UserFormClass, ScrollTop: int) """
        ...

    def _SetScrollWidth(self, ScrollWidth:int): # -> 
        """ _SetScrollWidth(self: UserFormClass, ScrollWidth: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    AddControl = ...
    BeforeDragOver = ...
    BeforeDropOrPaste = ...
    Click = ...
    DblClick = ...
    Error = ...
    FormEvents_Event_Scroll = ...
    FormEvents_Event_Zoom = ...
    KeyDown = ...
    KeyPress = ...
    KeyUp = ...
    Layout = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    RemoveControl = ...


class WHTMLControlEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents) """
        ...


class WHTMLControlEvents1: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents1) """
        ...


class WHTMLControlEvents10: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents10) """
        ...


class WHTMLControlEvents10_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents10_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents10_ClickEventHandler) """
        ...


class WHTMLControlEvents10_SinkHelper(WHTMLControlEvents10): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents1_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents1_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents1_ClickEventHandler) """
        ...


class WHTMLControlEvents1_SinkHelper(WHTMLControlEvents1): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents2: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents2) """
        ...


class WHTMLControlEvents2_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents2_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents2_ClickEventHandler) """
        ...


class WHTMLControlEvents2_SinkHelper(WHTMLControlEvents2): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents3: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents3) """
        ...


class WHTMLControlEvents3_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents3_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents3_ClickEventHandler) """
        ...


class WHTMLControlEvents3_SinkHelper(WHTMLControlEvents3): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents4: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents4) """
        ...


class WHTMLControlEvents4_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents4_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents4_ClickEventHandler) """
        ...


class WHTMLControlEvents4_SinkHelper(WHTMLControlEvents4): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents5: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents5) """
        ...


class WHTMLControlEvents5_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents5_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents5_ClickEventHandler) """
        ...


class WHTMLControlEvents5_SinkHelper(WHTMLControlEvents5): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents6: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents6) """
        ...


class WHTMLControlEvents6_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents6_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents6_ClickEventHandler) """
        ...


class WHTMLControlEvents6_SinkHelper(WHTMLControlEvents6): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents7: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents7) """
        ...


class WHTMLControlEvents7_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents7_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents7_ClickEventHandler) """
        ...


class WHTMLControlEvents7_SinkHelper(WHTMLControlEvents7): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents9: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self): # -> 
        """ Click(self: WHTMLControlEvents9) """
        ...


class WHTMLControlEvents9_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents9_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents9_ClickEventHandler) """
        ...


class WHTMLControlEvents9_SinkHelper(WHTMLControlEvents9): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class WHTMLControlEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WHTMLControlEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: WHTMLControlEvents_ClickEventHandler) """
        ...


class WHTMLControlEvents_SinkHelper(WHTMLControlEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


