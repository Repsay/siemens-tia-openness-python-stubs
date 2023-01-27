# encoding: utf-8
# module Microsoft.VisualStudio.CommandBars calls itself CommandBars
# from Microsoft.VisualStudio.CommandBars, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, MulticastDelegate

from System.Collections import IEnumerable, IEnumerator

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, StdPicture, 
    __ComObject, field#)
"""

# no functions
# classes

class IAccessible: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def accChildCount(self) -> int:
        """ Get: accChildCount(self: IAccessible) -> int """
        ...

    @property
    def accFocus(self) -> object:
        """ Get: accFocus(self: IAccessible) -> object """
        ...

    @property
    def accParent(self) -> object:
        """ Get: accParent(self: IAccessible) -> object """
        ...

    @property
    def accSelection(self) -> object:
        """ Get: accSelection(self: IAccessible) -> object """
        ...


    def accDoDefaultAction(self, varChild:object): # -> 
        """ accDoDefaultAction(self: IAccessible, varChild: object) """
        ...

    def accHitTest(self, xLeft:int, yTop:int) -> object:
        """ accHitTest(self: IAccessible, xLeft: int, yTop: int) -> object """
        ...

    def accLocation(self, pxLeft, pyTop, pcxWidth, pcyHeight, varChild) -> Tuple_[int, int, int, int]:
        """ accLocation(self: IAccessible, varChild: object) -> (int, int, int, int) """
        ...

    def accNavigate(self, navDir:int, varStart:object) -> object:
        """ accNavigate(self: IAccessible, navDir: int, varStart: object) -> object """
        ...

    def accSelect(self, flagsSelect:int, varChild:object): # -> 
        """ accSelect(self: IAccessible, flagsSelect: int, varChild: object) """
        ...


class _IVsMsoOleAccDispObj(IAccessible): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: _IVsMsoOleAccDispObj) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: _IVsMsoOleAccDispObj) -> int """
        ...



class CommandBar(_IVsMsoOleAccDispObj): # skipped bases: <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def AdaptiveMenu(self) -> bool:
        """
        Get: AdaptiveMenu(self: CommandBar) -> bool
        Set: AdaptiveMenu(self: CommandBar) = value
        """
        ...

    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: CommandBar) -> bool """
        ...

    @property
    def Context(self) -> str:
        """
        Get: Context(self: CommandBar) -> str
        Set: Context(self: CommandBar) = value
        """
        ...

    @property
    def Controls(self) -> CommandBarControls:
        """ Get: Controls(self: CommandBar) -> CommandBarControls """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CommandBar) -> bool
        Set: Enabled(self: CommandBar) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: CommandBar) -> int
        Set: Height(self: CommandBar) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CommandBar) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: CommandBar) -> int """
        ...

    @property
    def InstanceId(self) -> int:
        """ Get: InstanceId(self: CommandBar) -> int """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: CommandBar) -> int
        Set: Left(self: CommandBar) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CommandBar) -> str
        Set: Name(self: CommandBar) = value
        """
        ...

    @property
    def NameLocal(self) -> str:
        """
        Get: NameLocal(self: CommandBar) -> str
        Set: NameLocal(self: CommandBar) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CommandBar) -> object """
        ...

    @property
    def Position(self) -> MsoBarPosition:
        """
        Get: Position(self: CommandBar) -> MsoBarPosition
        Set: Position(self: CommandBar) = value
        """
        ...

    @property
    def Protection(self) -> MsoBarProtection:
        """
        Get: Protection(self: CommandBar) -> MsoBarProtection
        Set: Protection(self: CommandBar) = value
        """
        ...

    @property
    def RowIndex(self) -> int:
        """
        Get: RowIndex(self: CommandBar) -> int
        Set: RowIndex(self: CommandBar) = value
        """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: CommandBar) -> int
        Set: Top(self: CommandBar) = value
        """
        ...

    @property
    def Type(self) -> MsoBarType:
        """ Get: Type(self: CommandBar) -> MsoBarType """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: CommandBar) -> bool
        Set: Visible(self: CommandBar) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: CommandBar) -> int
        Set: Width(self: CommandBar) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: CommandBar) """
        ...

    def FindControl(self, Type:object, Id:object, Tag:object, Visible:object, Recursive:object) -> CommandBarControl:
        """ FindControl(self: CommandBar, Type: object, Id: object, Tag: object, Visible: object, Recursive: object) -> CommandBarControl """
        ...

    def Reset(self): # -> 
        """ Reset(self: CommandBar) """
        ...

    def ShowPopup(self, x:object, y:object): # -> 
        """ ShowPopup(self: CommandBar, x: object, y: object) """
        ...


class CommandBarControl(_IVsMsoOleAccDispObj): # skipped bases: <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def BeginGroup(self) -> bool:
        """
        Get: BeginGroup(self: CommandBarControl) -> bool
        Set: BeginGroup(self: CommandBarControl) = value
        """
        ...

    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: CommandBarControl) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: CommandBarControl) -> str
        Set: Caption(self: CommandBarControl) = value
        """
        ...

    @property
    def Control(self) -> object:
        """ Get: Control(self: CommandBarControl) -> object """
        ...

    @property
    def DescriptionText(self) -> str:
        """
        Get: DescriptionText(self: CommandBarControl) -> str
        Set: DescriptionText(self: CommandBarControl) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CommandBarControl) -> bool
        Set: Enabled(self: CommandBarControl) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: CommandBarControl) -> int
        Set: Height(self: CommandBarControl) = value
        """
        ...

    @property
    def HelpContextId(self) -> int:
        """
        Get: HelpContextId(self: CommandBarControl) -> int
        Set: HelpContextId(self: CommandBarControl) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: CommandBarControl) -> str
        Set: HelpFile(self: CommandBarControl) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CommandBarControl) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: CommandBarControl) -> int """
        ...

    @property
    def InstanceId(self) -> int:
        """ Get: InstanceId(self: CommandBarControl) -> int """
        ...

    @property
    def IsPriorityDropped(self) -> bool:
        """ Get: IsPriorityDropped(self: CommandBarControl) -> bool """
        ...

    @property
    def Left(self) -> int:
        """ Get: Left(self: CommandBarControl) -> int """
        ...

    @property
    def OLEUsage(self) -> MsoControlOLEUsage:
        """
        Get: OLEUsage(self: CommandBarControl) -> MsoControlOLEUsage
        Set: OLEUsage(self: CommandBarControl) = value
        """
        ...

    @property
    def OnAction(self) -> str:
        """
        Get: OnAction(self: CommandBarControl) -> str
        Set: OnAction(self: CommandBarControl) = value
        """
        ...

    @property
    def Parameter(self) -> str:
        """
        Get: Parameter(self: CommandBarControl) -> str
        Set: Parameter(self: CommandBarControl) = value
        """
        ...

    @property
    def Parent(self) -> CommandBar:
        """ Get: Parent(self: CommandBarControl) -> CommandBar """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: CommandBarControl) -> int
        Set: Priority(self: CommandBarControl) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: CommandBarControl) -> str
        Set: Tag(self: CommandBarControl) = value
        """
        ...

    @property
    def TooltipText(self) -> str:
        """
        Get: TooltipText(self: CommandBarControl) -> str
        Set: TooltipText(self: CommandBarControl) = value
        """
        ...

    @property
    def Top(self) -> int:
        """ Get: Top(self: CommandBarControl) -> int """
        ...

    @property
    def Type(self) -> MsoControlType:
        """ Get: Type(self: CommandBarControl) -> MsoControlType """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: CommandBarControl) -> bool
        Set: Visible(self: CommandBarControl) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: CommandBarControl) -> int
        Set: Width(self: CommandBarControl) = value
        """
        ...


    def Copy(self, Bar:object, Before:object) -> CommandBarControl:
        """ Copy(self: CommandBarControl, Bar: object, Before: object) -> CommandBarControl """
        ...

    def Delete(self, Temporary:object): # -> 
        """ Delete(self: CommandBarControl, Temporary: object) """
        ...

    def Execute(self): # -> 
        """ Execute(self: CommandBarControl) """
        ...

    def Move(self, Bar:object, Before:object) -> CommandBarControl:
        """ Move(self: CommandBarControl, Bar: object, Before: object) -> CommandBarControl """
        ...

    def Reserved1(self): # -> 
        """ Reserved1(self: CommandBarControl) """
        ...

    def Reserved2(self): # -> 
        """ Reserved2(self: CommandBarControl) """
        ...

    def Reserved3(self): # -> 
        """ Reserved3(self: CommandBarControl) """
        ...

    def Reserved4(self): # -> 
        """ Reserved4(self: CommandBarControl) """
        ...

    def Reserved5(self): # -> 
        """ Reserved5(self: CommandBarControl) """
        ...

    def Reserved6(self): # -> 
        """ Reserved6(self: CommandBarControl) """
        ...

    def Reserved7(self): # -> 
        """ Reserved7(self: CommandBarControl) """
        ...

    def Reset(self): # -> 
        """ Reset(self: CommandBarControl) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: CommandBarControl) """
        ...


class _CommandBarButton(CommandBarControl): # skipped bases: <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def BuiltInFace(self) -> bool:
        """
        Get: BuiltInFace(self: _CommandBarButton) -> bool
        Set: BuiltInFace(self: _CommandBarButton) = value
        """
        ...

    @property
    def FaceId(self) -> int:
        """
        Get: FaceId(self: _CommandBarButton) -> int
        Set: FaceId(self: _CommandBarButton) = value
        """
        ...

    @property
    def HyperlinkType(self) -> MsoCommandBarButtonHyperlinkType:
        """
        Get: HyperlinkType(self: _CommandBarButton) -> MsoCommandBarButtonHyperlinkType
        Set: HyperlinkType(self: _CommandBarButton) = value
        """
        ...

    @property
    def Mask(self): # -> StdPicture
        """
        Get: Mask(self: _CommandBarButton) -> StdPicture
        Set: Mask(self: _CommandBarButton) = value
        """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: _CommandBarButton) -> StdPicture
        Set: Picture(self: _CommandBarButton) = value
        """
        ...

    @property
    def ShortcutText(self) -> str:
        """
        Get: ShortcutText(self: _CommandBarButton) -> str
        Set: ShortcutText(self: _CommandBarButton) = value
        """
        ...

    @property
    def State(self) -> MsoButtonState:
        """
        Get: State(self: _CommandBarButton) -> MsoButtonState
        Set: State(self: _CommandBarButton) = value
        """
        ...

    @property
    def Style(self) -> MsoButtonStyle:
        """
        Get: Style(self: _CommandBarButton) -> MsoButtonStyle
        Set: Style(self: _CommandBarButton) = value
        """
        ...


    def CopyFace(self): # -> 
        """ CopyFace(self: _CommandBarButton) """
        ...

    def PasteFace(self): # -> 
        """ PasteFace(self: _CommandBarButton) """
        ...


class _CommandBarButtonEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self, A_1:_CommandBarButtonEvents_ClickEventHandler): # -> 
        """ add_Click(self: _CommandBarButtonEvents_Event, A_1: _CommandBarButtonEvents_ClickEventHandler) """
        ...

    def remove_Click(self, A_1:_CommandBarButtonEvents_ClickEventHandler): # -> 
        """ remove_Click(self: _CommandBarButtonEvents_Event, A_1: _CommandBarButtonEvents_ClickEventHandler) """
        ...

    Click = ...


class CommandBarButton(_CommandBarButtonEvents_Event, _CommandBarButton): # skipped bases: <type 'CommandBarControl'>, <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    pass

class CommandBarButtonClass(CommandBarButton, __ComObject): # skipped bases: <type '_CommandBarButtonEvents_Event'>, <type 'CommandBarControl'>, <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type '_CommandBarButton'>, <type 'object'>
    """ no doc """
    @property
    def accChildCount(self) -> int:
        """ Get: accChildCount(self: CommandBarButtonClass) -> int """
        ...

    @property
    def accFocus(self) -> object:
        """ Get: accFocus(self: CommandBarButtonClass) -> object """
        ...

    @property
    def accParent(self) -> object:
        """ Get: accParent(self: CommandBarButtonClass) -> object """
        ...

    @property
    def accSelection(self) -> object:
        """ Get: accSelection(self: CommandBarButtonClass) -> object """
        ...

    @property
    def Application(self) -> object:
        """ Get: Application(self: CommandBarButtonClass) -> object """
        ...

    @property
    def BeginGroup(self) -> bool:
        """
        Get: BeginGroup(self: CommandBarButtonClass) -> bool
        Set: BeginGroup(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: CommandBarButtonClass) -> bool """
        ...

    @property
    def BuiltInFace(self) -> bool:
        """
        Get: BuiltInFace(self: CommandBarButtonClass) -> bool
        Set: BuiltInFace(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: CommandBarButtonClass) -> str
        Set: Caption(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Control(self) -> object:
        """ Get: Control(self: CommandBarButtonClass) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: CommandBarButtonClass) -> int """
        ...

    @property
    def DescriptionText(self) -> str:
        """
        Get: DescriptionText(self: CommandBarButtonClass) -> str
        Set: DescriptionText(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CommandBarButtonClass) -> bool
        Set: Enabled(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def FaceId(self) -> int:
        """
        Get: FaceId(self: CommandBarButtonClass) -> int
        Set: FaceId(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: CommandBarButtonClass) -> int
        Set: Height(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def HelpContextId(self) -> int:
        """
        Get: HelpContextId(self: CommandBarButtonClass) -> int
        Set: HelpContextId(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: CommandBarButtonClass) -> str
        Set: HelpFile(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def HyperlinkType(self) -> MsoCommandBarButtonHyperlinkType:
        """
        Get: HyperlinkType(self: CommandBarButtonClass) -> MsoCommandBarButtonHyperlinkType
        Set: HyperlinkType(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CommandBarButtonClass) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: CommandBarButtonClass) -> int """
        ...

    @property
    def InstanceId(self) -> int:
        """ Get: InstanceId(self: CommandBarButtonClass) -> int """
        ...

    @property
    def IsPriorityDropped(self) -> bool:
        """ Get: IsPriorityDropped(self: CommandBarButtonClass) -> bool """
        ...

    @property
    def Left(self) -> int:
        """ Get: Left(self: CommandBarButtonClass) -> int """
        ...

    @property
    def Mask(self): # -> StdPicture
        """
        Get: Mask(self: CommandBarButtonClass) -> StdPicture
        Set: Mask(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def OLEUsage(self) -> MsoControlOLEUsage:
        """
        Get: OLEUsage(self: CommandBarButtonClass) -> MsoControlOLEUsage
        Set: OLEUsage(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def OnAction(self) -> str:
        """
        Get: OnAction(self: CommandBarButtonClass) -> str
        Set: OnAction(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Parameter(self) -> str:
        """
        Get: Parameter(self: CommandBarButtonClass) -> str
        Set: Parameter(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Parent(self) -> CommandBar:
        """ Get: Parent(self: CommandBarButtonClass) -> CommandBar """
        ...

    @property
    def Picture(self): # -> StdPicture
        """
        Get: Picture(self: CommandBarButtonClass) -> StdPicture
        Set: Picture(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: CommandBarButtonClass) -> int
        Set: Priority(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def ShortcutText(self) -> str:
        """
        Get: ShortcutText(self: CommandBarButtonClass) -> str
        Set: ShortcutText(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def State(self) -> MsoButtonState:
        """
        Get: State(self: CommandBarButtonClass) -> MsoButtonState
        Set: State(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Style(self) -> MsoButtonStyle:
        """
        Get: Style(self: CommandBarButtonClass) -> MsoButtonStyle
        Set: Style(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: CommandBarButtonClass) -> str
        Set: Tag(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def TooltipText(self) -> str:
        """
        Get: TooltipText(self: CommandBarButtonClass) -> str
        Set: TooltipText(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Top(self) -> int:
        """ Get: Top(self: CommandBarButtonClass) -> int """
        ...

    @property
    def Type(self) -> MsoControlType:
        """ Get: Type(self: CommandBarButtonClass) -> MsoControlType """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: CommandBarButtonClass) -> bool
        Set: Visible(self: CommandBarButtonClass) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: CommandBarButtonClass) -> int
        Set: Width(self: CommandBarButtonClass) = value
        """
        ...


    def accDoDefaultAction(self, varChild:object): # -> 
        """ accDoDefaultAction(self: CommandBarButtonClass, varChild: object) """
        ...

    def accHitTest(self, xLeft:int, yTop:int) -> object:
        """ accHitTest(self: CommandBarButtonClass, xLeft: int, yTop: int) -> object """
        ...

    def accLocation(self, pxLeft, pyTop, pcxWidth, pcyHeight, varChild) -> Tuple_[int, int, int, int]:
        """ accLocation(self: CommandBarButtonClass, varChild: object) -> (int, int, int, int) """
        ...

    def accNavigate(self, navDir:int, varStart:object) -> object:
        """ accNavigate(self: CommandBarButtonClass, navDir: int, varStart: object) -> object """
        ...

    def accSelect(self, flagsSelect:int, varChild:object): # -> 
        """ accSelect(self: CommandBarButtonClass, flagsSelect: int, varChild: object) """
        ...

    def add_Click(self, A_1:_CommandBarButtonEvents_ClickEventHandler): # -> 
        """ add_Click(self: CommandBarButtonClass, A_1: _CommandBarButtonEvents_ClickEventHandler) """
        ...

    def Copy(self, Bar:object, Before:object) -> CommandBarControl:
        """ Copy(self: CommandBarButtonClass, Bar: object, Before: object) -> CommandBarControl """
        ...

    def CopyFace(self): # -> 
        """ CopyFace(self: CommandBarButtonClass) """
        ...

    def Delete(self, Temporary:object): # -> 
        """ Delete(self: CommandBarButtonClass, Temporary: object) """
        ...

    def Execute(self): # -> 
        """ Execute(self: CommandBarButtonClass) """
        ...

    def Move(self, Bar:object, Before:object) -> CommandBarControl:
        """ Move(self: CommandBarButtonClass, Bar: object, Before: object) -> CommandBarControl """
        ...

    def PasteFace(self): # -> 
        """ PasteFace(self: CommandBarButtonClass) """
        ...

    def remove_Click(self, A_1:_CommandBarButtonEvents_ClickEventHandler): # -> 
        """ remove_Click(self: CommandBarButtonClass, A_1: _CommandBarButtonEvents_ClickEventHandler) """
        ...

    def Reserved1(self): # -> 
        """ Reserved1(self: CommandBarButtonClass) """
        ...

    def Reserved2(self): # -> 
        """ Reserved2(self: CommandBarButtonClass) """
        ...

    def Reserved3(self): # -> 
        """ Reserved3(self: CommandBarButtonClass) """
        ...

    def Reserved4(self): # -> 
        """ Reserved4(self: CommandBarButtonClass) """
        ...

    def Reserved5(self): # -> 
        """ Reserved5(self: CommandBarButtonClass) """
        ...

    def Reserved6(self): # -> 
        """ Reserved6(self: CommandBarButtonClass) """
        ...

    def Reserved7(self): # -> 
        """ Reserved7(self: CommandBarButtonClass) """
        ...

    def Reset(self): # -> 
        """ Reset(self: CommandBarButtonClass) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: CommandBarButtonClass) """
        ...

    Click = ...


class _CommandBarComboBox(CommandBarControl): # skipped bases: <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def DropDownLines(self) -> int:
        """
        Get: DropDownLines(self: _CommandBarComboBox) -> int
        Set: DropDownLines(self: _CommandBarComboBox) = value
        """
        ...

    @property
    def DropDownWidth(self) -> int:
        """
        Get: DropDownWidth(self: _CommandBarComboBox) -> int
        Set: DropDownWidth(self: _CommandBarComboBox) = value
        """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: _CommandBarComboBox) -> int """
        ...

    @property
    def ListHeaderCount(self) -> int:
        """
        Get: ListHeaderCount(self: _CommandBarComboBox) -> int
        Set: ListHeaderCount(self: _CommandBarComboBox) = value
        """
        ...

    @property
    def ListIndex(self) -> int:
        """
        Get: ListIndex(self: _CommandBarComboBox) -> int
        Set: ListIndex(self: _CommandBarComboBox) = value
        """
        ...

    @property
    def Style(self) -> MsoComboStyle:
        """
        Get: Style(self: _CommandBarComboBox) -> MsoComboStyle
        Set: Style(self: _CommandBarComboBox) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: _CommandBarComboBox) -> str
        Set: Text(self: _CommandBarComboBox) = value
        """
        ...


    def AddItem(self, Text:str, Index:object): # -> 
        """ AddItem(self: _CommandBarComboBox, Text: str, Index: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: _CommandBarComboBox) """
        ...

    def RemoveItem(self, Index:int): # -> 
        """ RemoveItem(self: _CommandBarComboBox, Index: int) """
        ...


class _CommandBarComboBoxEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Change(self, A_1:_CommandBarComboBoxEvents_ChangeEventHandler): # -> 
        """ add_Change(self: _CommandBarComboBoxEvents_Event, A_1: _CommandBarComboBoxEvents_ChangeEventHandler) """
        ...

    def remove_Change(self, A_1:_CommandBarComboBoxEvents_ChangeEventHandler): # -> 
        """ remove_Change(self: _CommandBarComboBoxEvents_Event, A_1: _CommandBarComboBoxEvents_ChangeEventHandler) """
        ...

    Change = ...


class CommandBarComboBox(_CommandBarComboBoxEvents_Event, _CommandBarComboBox): # skipped bases: <type 'CommandBarControl'>, <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    pass

class CommandBarComboBoxClass(__ComObject, CommandBarComboBox): # skipped bases: <type '_CommandBarComboBoxEvents_Event'>, <type 'CommandBarControl'>, <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type '_CommandBarComboBox'>, <type 'object'>
    """ no doc """
    @property
    def accChildCount(self) -> int:
        """ Get: accChildCount(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def accFocus(self) -> object:
        """ Get: accFocus(self: CommandBarComboBoxClass) -> object """
        ...

    @property
    def accParent(self) -> object:
        """ Get: accParent(self: CommandBarComboBoxClass) -> object """
        ...

    @property
    def accSelection(self) -> object:
        """ Get: accSelection(self: CommandBarComboBoxClass) -> object """
        ...

    @property
    def Application(self) -> object:
        """ Get: Application(self: CommandBarComboBoxClass) -> object """
        ...

    @property
    def BeginGroup(self) -> bool:
        """
        Get: BeginGroup(self: CommandBarComboBoxClass) -> bool
        Set: BeginGroup(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: CommandBarComboBoxClass) -> bool """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: CommandBarComboBoxClass) -> str
        Set: Caption(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Control(self) -> object:
        """ Get: Control(self: CommandBarComboBoxClass) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def DescriptionText(self) -> str:
        """
        Get: DescriptionText(self: CommandBarComboBoxClass) -> str
        Set: DescriptionText(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def DropDownLines(self) -> int:
        """
        Get: DropDownLines(self: CommandBarComboBoxClass) -> int
        Set: DropDownLines(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def DropDownWidth(self) -> int:
        """
        Get: DropDownWidth(self: CommandBarComboBoxClass) -> int
        Set: DropDownWidth(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: CommandBarComboBoxClass) -> bool
        Set: Enabled(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: CommandBarComboBoxClass) -> int
        Set: Height(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def HelpContextId(self) -> int:
        """
        Get: HelpContextId(self: CommandBarComboBoxClass) -> int
        Set: HelpContextId(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: CommandBarComboBoxClass) -> str
        Set: HelpFile(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def InstanceId(self) -> int:
        """ Get: InstanceId(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def IsPriorityDropped(self) -> bool:
        """ Get: IsPriorityDropped(self: CommandBarComboBoxClass) -> bool """
        ...

    @property
    def Left(self) -> int:
        """ Get: Left(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def ListCount(self) -> int:
        """ Get: ListCount(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def ListHeaderCount(self) -> int:
        """
        Get: ListHeaderCount(self: CommandBarComboBoxClass) -> int
        Set: ListHeaderCount(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def ListIndex(self) -> int:
        """
        Get: ListIndex(self: CommandBarComboBoxClass) -> int
        Set: ListIndex(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def OLEUsage(self) -> MsoControlOLEUsage:
        """
        Get: OLEUsage(self: CommandBarComboBoxClass) -> MsoControlOLEUsage
        Set: OLEUsage(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def OnAction(self) -> str:
        """
        Get: OnAction(self: CommandBarComboBoxClass) -> str
        Set: OnAction(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Parameter(self) -> str:
        """
        Get: Parameter(self: CommandBarComboBoxClass) -> str
        Set: Parameter(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Parent(self) -> CommandBar:
        """ Get: Parent(self: CommandBarComboBoxClass) -> CommandBar """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: CommandBarComboBoxClass) -> int
        Set: Priority(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Style(self) -> MsoComboStyle:
        """
        Get: Style(self: CommandBarComboBoxClass) -> MsoComboStyle
        Set: Style(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: CommandBarComboBoxClass) -> str
        Set: Tag(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: CommandBarComboBoxClass) -> str
        Set: Text(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def TooltipText(self) -> str:
        """
        Get: TooltipText(self: CommandBarComboBoxClass) -> str
        Set: TooltipText(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Top(self) -> int:
        """ Get: Top(self: CommandBarComboBoxClass) -> int """
        ...

    @property
    def Type(self) -> MsoControlType:
        """ Get: Type(self: CommandBarComboBoxClass) -> MsoControlType """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: CommandBarComboBoxClass) -> bool
        Set: Visible(self: CommandBarComboBoxClass) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: CommandBarComboBoxClass) -> int
        Set: Width(self: CommandBarComboBoxClass) = value
        """
        ...


    def accDoDefaultAction(self, varChild:object): # -> 
        """ accDoDefaultAction(self: CommandBarComboBoxClass, varChild: object) """
        ...

    def accHitTest(self, xLeft:int, yTop:int) -> object:
        """ accHitTest(self: CommandBarComboBoxClass, xLeft: int, yTop: int) -> object """
        ...

    def accLocation(self, pxLeft, pyTop, pcxWidth, pcyHeight, varChild) -> Tuple_[int, int, int, int]:
        """ accLocation(self: CommandBarComboBoxClass, varChild: object) -> (int, int, int, int) """
        ...

    def accNavigate(self, navDir:int, varStart:object) -> object:
        """ accNavigate(self: CommandBarComboBoxClass, navDir: int, varStart: object) -> object """
        ...

    def accSelect(self, flagsSelect:int, varChild:object): # -> 
        """ accSelect(self: CommandBarComboBoxClass, flagsSelect: int, varChild: object) """
        ...

    def AddItem(self, Text:str, Index:object): # -> 
        """ AddItem(self: CommandBarComboBoxClass, Text: str, Index: object) """
        ...

    def add_Change(self, A_1:_CommandBarComboBoxEvents_ChangeEventHandler): # -> 
        """ add_Change(self: CommandBarComboBoxClass, A_1: _CommandBarComboBoxEvents_ChangeEventHandler) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CommandBarComboBoxClass) """
        ...

    def Copy(self, Bar:object, Before:object) -> CommandBarControl:
        """ Copy(self: CommandBarComboBoxClass, Bar: object, Before: object) -> CommandBarControl """
        ...

    def Delete(self, Temporary:object): # -> 
        """ Delete(self: CommandBarComboBoxClass, Temporary: object) """
        ...

    def Execute(self): # -> 
        """ Execute(self: CommandBarComboBoxClass) """
        ...

    def Move(self, Bar:object, Before:object) -> CommandBarControl:
        """ Move(self: CommandBarComboBoxClass, Bar: object, Before: object) -> CommandBarControl """
        ...

    def RemoveItem(self, Index:int): # -> 
        """ RemoveItem(self: CommandBarComboBoxClass, Index: int) """
        ...

    def remove_Change(self, A_1:_CommandBarComboBoxEvents_ChangeEventHandler): # -> 
        """ remove_Change(self: CommandBarComboBoxClass, A_1: _CommandBarComboBoxEvents_ChangeEventHandler) """
        ...

    def Reserved1(self): # -> 
        """ Reserved1(self: CommandBarComboBoxClass) """
        ...

    def Reserved2(self): # -> 
        """ Reserved2(self: CommandBarComboBoxClass) """
        ...

    def Reserved3(self): # -> 
        """ Reserved3(self: CommandBarComboBoxClass) """
        ...

    def Reserved4(self): # -> 
        """ Reserved4(self: CommandBarComboBoxClass) """
        ...

    def Reserved5(self): # -> 
        """ Reserved5(self: CommandBarComboBoxClass) """
        ...

    def Reserved6(self): # -> 
        """ Reserved6(self: CommandBarComboBoxClass) """
        ...

    def Reserved7(self): # -> 
        """ Reserved7(self: CommandBarComboBoxClass) """
        ...

    def Reset(self): # -> 
        """ Reset(self: CommandBarComboBoxClass) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: CommandBarComboBoxClass) """
        ...

    Change = ...


class _IVsMsoDispObj: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: _IVsMsoDispObj) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: _IVsMsoDispObj) -> int """
        ...



class CommandBarControls(_IVsMsoDispObj, IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CommandBarControls) -> int """
        ...

    @property
    def Parent(self) -> CommandBar:
        """ Get: Parent(self: CommandBarControls) -> CommandBar """
        ...


    def Add(self, Type:object, Id:object, Parameter:object, Before:object, Temporary:object) -> CommandBarControl:
        """ Add(self: CommandBarControls, Type: object, Id: object, Parameter: object, Before: object, Temporary: object) -> CommandBarControl """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CommandBarPopup(CommandBarControl): # skipped bases: <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def CommandBar(self) -> CommandBar:
        """ Get: CommandBar(self: CommandBarPopup) -> CommandBar """
        ...

    @property
    def Controls(self) -> CommandBarControls:
        """ Get: Controls(self: CommandBarPopup) -> CommandBarControls """
        ...

    @property
    def OLEMenuGroup(self) -> MsoOLEMenuGroup:
        """
        Get: OLEMenuGroup(self: CommandBarPopup) -> MsoOLEMenuGroup
        Set: OLEMenuGroup(self: CommandBarPopup) = value
        """
        ...



class _CommandBars(_IVsMsoDispObj, IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActionControl(self) -> CommandBarControl:
        """ Get: ActionControl(self: _CommandBars) -> CommandBarControl """
        ...

    @property
    def ActiveMenuBar(self) -> CommandBar:
        """ Get: ActiveMenuBar(self: _CommandBars) -> CommandBar """
        ...

    @property
    def AdaptiveMenus(self) -> bool:
        """
        Get: AdaptiveMenus(self: _CommandBars) -> bool
        Set: AdaptiveMenus(self: _CommandBars) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: _CommandBars) -> int """
        ...

    @property
    def DisableAskAQuestionDropdown(self) -> bool:
        """
        Get: DisableAskAQuestionDropdown(self: _CommandBars) -> bool
        Set: DisableAskAQuestionDropdown(self: _CommandBars) = value
        """
        ...

    @property
    def DisableCustomize(self) -> bool:
        """
        Get: DisableCustomize(self: _CommandBars) -> bool
        Set: DisableCustomize(self: _CommandBars) = value
        """
        ...

    @property
    def DisplayFonts(self) -> bool:
        """
        Get: DisplayFonts(self: _CommandBars) -> bool
        Set: DisplayFonts(self: _CommandBars) = value
        """
        ...

    @property
    def DisplayKeysInTooltips(self) -> bool:
        """
        Get: DisplayKeysInTooltips(self: _CommandBars) -> bool
        Set: DisplayKeysInTooltips(self: _CommandBars) = value
        """
        ...

    @property
    def DisplayTooltips(self) -> bool:
        """
        Get: DisplayTooltips(self: _CommandBars) -> bool
        Set: DisplayTooltips(self: _CommandBars) = value
        """
        ...

    @property
    def LargeButtons(self) -> bool:
        """
        Get: LargeButtons(self: _CommandBars) -> bool
        Set: LargeButtons(self: _CommandBars) = value
        """
        ...

    @property
    def MenuAnimationStyle(self) -> MsoMenuAnimation:
        """
        Get: MenuAnimationStyle(self: _CommandBars) -> MsoMenuAnimation
        Set: MenuAnimationStyle(self: _CommandBars) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _CommandBars) -> object """
        ...


    def Add(self, Name:object, Position:object, MenuBar:object, Temporary:object) -> CommandBar:
        """ Add(self: _CommandBars, Name: object, Position: object, MenuBar: object, Temporary: object) -> CommandBar """
        ...

    def AddEx(self, TbidOrName:object, Position:object, MenuBar:object, Temporary:object, TbtrProtection:object) -> CommandBar:
        """ AddEx(self: _CommandBars, TbidOrName: object, Position: object, MenuBar: object, Temporary: object, TbtrProtection: object) -> CommandBar """
        ...

    def FindControl(self, Type:object, Id:object, Tag:object, Visible:object) -> CommandBarControl:
        """ FindControl(self: _CommandBars, Type: object, Id: object, Tag: object, Visible: object) -> CommandBarControl """
        ...

    def FindControls(self, Type:object, Id:object, Tag:object, Visible:object) -> CommandBarControls:
        """ FindControls(self: _CommandBars, Type: object, Id: object, Tag: object, Visible: object) -> CommandBarControls """
        ...

    def ReleaseFocus(self): # -> 
        """ ReleaseFocus(self: _CommandBars) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class _CommandBarsEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_OnUpdate(self, A_1:_CommandBarsEvents_OnUpdateEventHandler): # -> 
        """ add_OnUpdate(self: _CommandBarsEvents_Event, A_1: _CommandBarsEvents_OnUpdateEventHandler) """
        ...

    def remove_OnUpdate(self, A_1:_CommandBarsEvents_OnUpdateEventHandler): # -> 
        """ remove_OnUpdate(self: _CommandBarsEvents_Event, A_1: _CommandBarsEvents_OnUpdateEventHandler) """
        ...

    OnUpdate = ...


class CommandBars(_CommandBars, _CommandBarsEvents_Event): # skipped bases: <type '_IVsMsoDispObj'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class CommandBarsClass(CommandBars, __ComObject): # skipped bases: <type '_IVsMsoDispObj'>, <type 'IEnumerable'>, <type '_CommandBars'>, <type '_CommandBarsEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def ActionControl(self) -> CommandBarControl:
        """ Get: ActionControl(self: CommandBarsClass) -> CommandBarControl """
        ...

    @property
    def ActiveMenuBar(self) -> CommandBar:
        """ Get: ActiveMenuBar(self: CommandBarsClass) -> CommandBar """
        ...

    @property
    def AdaptiveMenus(self) -> bool:
        """
        Get: AdaptiveMenus(self: CommandBarsClass) -> bool
        Set: AdaptiveMenus(self: CommandBarsClass) = value
        """
        ...

    @property
    def Application(self) -> object:
        """ Get: Application(self: CommandBarsClass) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CommandBarsClass) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: CommandBarsClass) -> int """
        ...

    @property
    def DisableAskAQuestionDropdown(self) -> bool:
        """
        Get: DisableAskAQuestionDropdown(self: CommandBarsClass) -> bool
        Set: DisableAskAQuestionDropdown(self: CommandBarsClass) = value
        """
        ...

    @property
    def DisableCustomize(self) -> bool:
        """
        Get: DisableCustomize(self: CommandBarsClass) -> bool
        Set: DisableCustomize(self: CommandBarsClass) = value
        """
        ...

    @property
    def DisplayFonts(self) -> bool:
        """
        Get: DisplayFonts(self: CommandBarsClass) -> bool
        Set: DisplayFonts(self: CommandBarsClass) = value
        """
        ...

    @property
    def DisplayKeysInTooltips(self) -> bool:
        """
        Get: DisplayKeysInTooltips(self: CommandBarsClass) -> bool
        Set: DisplayKeysInTooltips(self: CommandBarsClass) = value
        """
        ...

    @property
    def DisplayTooltips(self) -> bool:
        """
        Get: DisplayTooltips(self: CommandBarsClass) -> bool
        Set: DisplayTooltips(self: CommandBarsClass) = value
        """
        ...

    @property
    def LargeButtons(self) -> bool:
        """
        Get: LargeButtons(self: CommandBarsClass) -> bool
        Set: LargeButtons(self: CommandBarsClass) = value
        """
        ...

    @property
    def MenuAnimationStyle(self) -> MsoMenuAnimation:
        """
        Get: MenuAnimationStyle(self: CommandBarsClass) -> MsoMenuAnimation
        Set: MenuAnimationStyle(self: CommandBarsClass) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CommandBarsClass) -> object """
        ...


    def Add(self, Name:object, Position:object, MenuBar:object, Temporary:object) -> CommandBar:
        """ Add(self: CommandBarsClass, Name: object, Position: object, MenuBar: object, Temporary: object) -> CommandBar """
        ...

    def AddEx(self, TbidOrName:object, Position:object, MenuBar:object, Temporary:object, TbtrProtection:object) -> CommandBar:
        """ AddEx(self: CommandBarsClass, TbidOrName: object, Position: object, MenuBar: object, Temporary: object, TbtrProtection: object) -> CommandBar """
        ...

    def add_OnUpdate(self, A_1:_CommandBarsEvents_OnUpdateEventHandler): # -> 
        """ add_OnUpdate(self: CommandBarsClass, A_1: _CommandBarsEvents_OnUpdateEventHandler) """
        ...

    def FindControl(self, Type:object, Id:object, Tag:object, Visible:object) -> CommandBarControl:
        """ FindControl(self: CommandBarsClass, Type: object, Id: object, Tag: object, Visible: object) -> CommandBarControl """
        ...

    def FindControls(self, Type:object, Id:object, Tag:object, Visible:object) -> CommandBarControls:
        """ FindControls(self: CommandBarsClass, Type: object, Id: object, Tag: object, Visible: object) -> CommandBarControls """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CommandBarsClass) -> IEnumerator """
        ...

    def ReleaseFocus(self): # -> 
        """ ReleaseFocus(self: CommandBarsClass) """
        ...

    def remove_OnUpdate(self, A_1:_CommandBarsEvents_OnUpdateEventHandler): # -> 
        """ remove_OnUpdate(self: CommandBarsClass, A_1: _CommandBarsEvents_OnUpdateEventHandler) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    OnUpdate = ...


class ICommandBarButtonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self, Ctrl, CancelDefault) -> bool:
        """ Click(self: ICommandBarButtonEvents, Ctrl: CommandBarButton) -> bool """
        ...


class ICommandBarComboBoxEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Change(self, Ctrl:CommandBarComboBox): # -> 
        """ Change(self: ICommandBarComboBoxEvents, Ctrl: CommandBarComboBox) """
        ...


class ICommandBarsEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnUpdate(self): # -> 
        """ OnUpdate(self: ICommandBarsEvents) """
        ...


class MsoBarPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoBarPosition, values: msoBarBottom (3), msoBarFloating (4), msoBarLeft (0), msoBarMenuBar (6), msoBarPopup (5), msoBarRight (2), msoBarTop (1) """
    msoBarBottom: MsoBarPosition = ...
    msoBarFloating: MsoBarPosition = ...
    msoBarLeft: MsoBarPosition = ...
    msoBarMenuBar: MsoBarPosition = ...
    msoBarPopup: MsoBarPosition = ...
    msoBarRight: MsoBarPosition = ...
    msoBarTop: MsoBarPosition = ...
    value__ = ...


class MsoBarProtection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoBarProtection, values: msoBarNoChangeDock (16), msoBarNoChangeVisible (8), msoBarNoCustomize (1), msoBarNoHorizontalDock (64), msoBarNoMove (4), msoBarNoProtection (0), msoBarNoResize (2), msoBarNoVerticalDock (32) """
    msoBarNoChangeDock: MsoBarProtection = ...
    msoBarNoChangeVisible: MsoBarProtection = ...
    msoBarNoCustomize: MsoBarProtection = ...
    msoBarNoHorizontalDock: MsoBarProtection = ...
    msoBarNoMove: MsoBarProtection = ...
    msoBarNoProtection: MsoBarProtection = ...
    msoBarNoResize: MsoBarProtection = ...
    msoBarNoVerticalDock: MsoBarProtection = ...
    value__ = ...


class MsoBarRow(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoBarRow, values: msoBarRowFirst (0), msoBarRowLast (-1) """
    msoBarRowFirst: MsoBarRow = ...
    msoBarRowLast: MsoBarRow = ...
    value__ = ...


class MsoBarType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoBarType, values: msoBarTypeMenuBar (1), msoBarTypeNormal (0), msoBarTypePopup (2) """
    msoBarTypeMenuBar: MsoBarType = ...
    msoBarTypeNormal: MsoBarType = ...
    msoBarTypePopup: MsoBarType = ...
    value__ = ...


class MsoButtonState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoButtonState, values: msoButtonDown (-1), msoButtonMixed (2), msoButtonUp (0) """
    msoButtonDown: MsoButtonState = ...
    msoButtonMixed: MsoButtonState = ...
    msoButtonUp: MsoButtonState = ...
    value__ = ...


class MsoButtonStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoButtonStyle, values: msoButtonAutomatic (0), msoButtonCaption (2), msoButtonIcon (1), msoButtonIconAndCaption (3), msoButtonIconAndCaptionBelow (11), msoButtonIconAndWrapCaption (7), msoButtonIconAndWrapCaptionBelow (15), msoButtonWrapCaption (14) """
    msoButtonAutomatic: MsoButtonStyle = ...
    msoButtonCaption: MsoButtonStyle = ...
    msoButtonIcon: MsoButtonStyle = ...
    msoButtonIconAndCaption: MsoButtonStyle = ...
    msoButtonIconAndCaptionBelow: MsoButtonStyle = ...
    msoButtonIconAndWrapCaption: MsoButtonStyle = ...
    msoButtonIconAndWrapCaptionBelow: MsoButtonStyle = ...
    msoButtonWrapCaption: MsoButtonStyle = ...
    value__ = ...


class MsoButtonStyleHidden(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoButtonStyleHidden, values: msoButtonTextBelow (8), msoButtonWrapText (4) """
    msoButtonTextBelow: MsoButtonStyleHidden = ...
    msoButtonWrapText: MsoButtonStyleHidden = ...
    value__ = ...


class MsoComboStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoComboStyle, values: msoComboLabel (1), msoComboNormal (0) """
    msoComboLabel: MsoComboStyle = ...
    msoComboNormal: MsoComboStyle = ...
    value__ = ...


class MsoCommandBarButtonHyperlinkType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoCommandBarButtonHyperlinkType, values: msoCommandBarButtonHyperlinkInsertPicture (2), msoCommandBarButtonHyperlinkNone (0), msoCommandBarButtonHyperlinkOpen (1) """
    msoCommandBarButtonHyperlinkInsertPicture: MsoCommandBarButtonHyperlinkType = ...
    msoCommandBarButtonHyperlinkNone: MsoCommandBarButtonHyperlinkType = ...
    msoCommandBarButtonHyperlinkOpen: MsoCommandBarButtonHyperlinkType = ...
    value__ = ...


class MsoControlOLEUsage(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoControlOLEUsage, values: msoControlOLEUsageBoth (3), msoControlOLEUsageClient (2), msoControlOLEUsageNeither (0), msoControlOLEUsageServer (1) """
    msoControlOLEUsageBoth: MsoControlOLEUsage = ...
    msoControlOLEUsageClient: MsoControlOLEUsage = ...
    msoControlOLEUsageNeither: MsoControlOLEUsage = ...
    msoControlOLEUsageServer: MsoControlOLEUsage = ...
    value__ = ...


class MsoControlType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoControlType, values: msoControlActiveX (22), msoControlAutoCompleteCombo (26), msoControlButton (1), msoControlButtonDropdown (5), msoControlButtonPopup (12), msoControlComboBox (4), msoControlCustom (0), msoControlDropdown (3), msoControlEdit (2), msoControlExpandingGrid (16), msoControlGauge (19), msoControlGenericDropdown (8), msoControlGraphicCombo (20), msoControlGraphicDropdown (9), msoControlGraphicPopup (11), msoControlGrid (18), msoControlLabel (15), msoControlLabelEx (24), msoControlOCXDropdown (7), msoControlPane (21), msoControlPopup (10), msoControlSpinner (23), msoControlSplitButtonMRUPopup (14), msoControlSplitButtonPopup (13), msoControlSplitDropdown (6), msoControlSplitExpandingGrid (17), msoControlWorkPane (25) """
    msoControlActiveX: MsoControlType = ...
    msoControlAutoCompleteCombo: MsoControlType = ...
    msoControlButton: MsoControlType = ...
    msoControlButtonDropdown: MsoControlType = ...
    msoControlButtonPopup: MsoControlType = ...
    msoControlComboBox: MsoControlType = ...
    msoControlCustom: MsoControlType = ...
    msoControlDropdown: MsoControlType = ...
    msoControlEdit: MsoControlType = ...
    msoControlExpandingGrid: MsoControlType = ...
    msoControlGauge: MsoControlType = ...
    msoControlGenericDropdown: MsoControlType = ...
    msoControlGraphicCombo: MsoControlType = ...
    msoControlGraphicDropdown: MsoControlType = ...
    msoControlGraphicPopup: MsoControlType = ...
    msoControlGrid: MsoControlType = ...
    msoControlLabel: MsoControlType = ...
    msoControlLabelEx: MsoControlType = ...
    msoControlOCXDropdown: MsoControlType = ...
    msoControlPane: MsoControlType = ...
    msoControlPopup: MsoControlType = ...
    msoControlSpinner: MsoControlType = ...
    msoControlSplitButtonMRUPopup: MsoControlType = ...
    msoControlSplitButtonPopup: MsoControlType = ...
    msoControlSplitDropdown: MsoControlType = ...
    msoControlSplitExpandingGrid: MsoControlType = ...
    msoControlWorkPane: MsoControlType = ...
    value__ = ...


class MsoMenuAnimation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoMenuAnimation, values: msoMenuAnimationNone (0), msoMenuAnimationRandom (1), msoMenuAnimationSlide (3), msoMenuAnimationUnfold (2) """
    msoMenuAnimationNone: MsoMenuAnimation = ...
    msoMenuAnimationRandom: MsoMenuAnimation = ...
    msoMenuAnimationSlide: MsoMenuAnimation = ...
    msoMenuAnimationUnfold: MsoMenuAnimation = ...
    value__ = ...


class MsoOLEMenuGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoOLEMenuGroup, values: msoOLEMenuGroupContainer (2), msoOLEMenuGroupEdit (1), msoOLEMenuGroupFile (0), msoOLEMenuGroupHelp (5), msoOLEMenuGroupNone (-1), msoOLEMenuGroupObject (3), msoOLEMenuGroupWindow (4) """
    msoOLEMenuGroupContainer: MsoOLEMenuGroup = ...
    msoOLEMenuGroupEdit: MsoOLEMenuGroup = ...
    msoOLEMenuGroupFile: MsoOLEMenuGroup = ...
    msoOLEMenuGroupHelp: MsoOLEMenuGroup = ...
    msoOLEMenuGroupNone: MsoOLEMenuGroup = ...
    msoOLEMenuGroupObject: MsoOLEMenuGroup = ...
    msoOLEMenuGroupWindow: MsoOLEMenuGroup = ...
    value__ = ...


class _CommandBarActiveX(CommandBarControl): # skipped bases: <type '_IVsMsoOleAccDispObj'>, <type 'IAccessible'>, <type 'object'>
    """ no doc """
    @property
    def ControlCLSID(self) -> str:
        """
        Get: ControlCLSID(self: _CommandBarActiveX) -> str
        Set: ControlCLSID(self: _CommandBarActiveX) = value
        """
        ...

    @property
    def InitWith(self): # -> 
        """ Set: InitWith(self: _CommandBarActiveX) = value """
        ...


    def EnsureControl(self): # -> 
        """ EnsureControl(self: _CommandBarActiveX) """
        ...

    def SetInnerObjectFactory(self, pUnk:object): # -> 
        """ SetInnerObjectFactory(self: _CommandBarActiveX, pUnk: object) """
        ...


class _CommandBarButtonEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self, Ctrl, CancelDefault) -> bool:
        """ Click(self: _CommandBarButtonEvents, Ctrl: CommandBarButton) -> bool """
        ...


class _CommandBarButtonEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _CommandBarButtonEvents_ClickEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Ctrl, CancelDefault) -> bool:
        """ Invoke(self: _CommandBarButtonEvents_ClickEventHandler, Ctrl: CommandBarButton) -> bool """
        ...


class _CommandBarButtonEvents_SinkHelper(_CommandBarButtonEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class _CommandBarComboBoxEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Change(self, Ctrl:CommandBarComboBox): # -> 
        """ Change(self: _CommandBarComboBoxEvents, Ctrl: CommandBarComboBox) """
        ...


class _CommandBarComboBoxEvents_ChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _CommandBarComboBoxEvents_ChangeEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Ctrl:CommandBarComboBox): # -> 
        """ Invoke(self: _CommandBarComboBoxEvents_ChangeEventHandler, Ctrl: CommandBarComboBox) """
        ...


class _CommandBarComboBoxEvents_SinkHelper(_CommandBarComboBoxEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_ChangeDelegate = ...
    m_dwCookie = ...


class _CommandBarsEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnUpdate(self): # -> 
        """ OnUpdate(self: _CommandBarsEvents) """
        ...


class _CommandBarsEvents_OnUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _CommandBarsEvents_OnUpdateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: _CommandBarsEvents_OnUpdateEventHandler) """
        ...


class _CommandBarsEvents_SinkHelper(_CommandBarsEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...
    m_OnUpdateDelegate = ...


