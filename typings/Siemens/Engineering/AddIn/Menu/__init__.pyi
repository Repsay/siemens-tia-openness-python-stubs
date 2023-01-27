# encoding: utf-8
# module Siemens.Engineering.AddIn.Menu calls itself Menu
# from Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Collections import IEnumerable

"""The following names are not found in the module: (
    IMenuItemContainerPrivate, IMenuItemFactoryPrivate, OnClickDelegate, 
    OnUpdateStatusDelegate, field#)
"""

# no functions
# classes

class ActionItem: # skipped bases: <type 'object'>
    """  """
    @property
    def DefaultLabelText(self) -> str:
        """ Get: DefaultLabelText(self: ActionItem) -> str """
        ...



class ActionItemStyle: # skipped bases: <type 'object'>, <type 'object'>
    """  """
    pass

class CheckBoxActionItemStyle(ActionItemStyle): # skipped bases: <type 'object'>
    """  """
    @property
    def State(self) -> CheckBoxState:
        """
        Get: State(self: CheckBoxActionItemStyle) -> CheckBoxState
        Set: State(self: CheckBoxActionItemStyle) = value
        """
        ...



class CheckBoxState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CheckBoxState, values: Checked (1), Unchecked (0) """
    Checked: CheckBoxState = ...
    Unchecked: CheckBoxState = ...
    value__ = ...


class ChildItemFactory(IMenuItemFactoryPrivate): # skipped bases: <type 'IActionItemFactoryPrivate'>, <type 'ISubmenuFactoryPrivate'>, <type 'object'>
    """  """
    def AddActionItem(self, defaultLabelText:str, clickDelegate, updateStatusDelegate = ...) -> ActionItem: # Not found arg types: {'clickDelegate': 'OnClickDelegate', 'updateStatusDelegate': 'OnUpdateStatusDelegate'}
        """
        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject]
        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject]
        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...

    def AddActionItemWithCheckBox(self, defaultLabelText:str, clickDelegate, updateStatusDelegate) -> ActionItem: # Not found arg types: {'clickDelegate': 'OnClickDelegate', 'updateStatusDelegate': 'OnUpdateStatusDelegate'}
        """
        AddActionItemWithCheckBox[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject]
        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...

    def AddActionItemWithRadioButton(self, defaultLabelText:str, clickDelegate, updateStatusDelegate) -> ActionItem: # Not found arg types: {'clickDelegate': 'OnClickDelegate', 'updateStatusDelegate': 'OnUpdateStatusDelegate'}
        """
        AddActionItemWithRadioButton[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject]
        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        ...

    def AddSubmenu(self, defaultLabelText:str) -> Submenu:
        """ AddSubmenu(self: ChildItemFactory, defaultLabelText: str) -> Submenu """
        ...


class ContextMenuAddIn: # skipped bases: <type 'object'>, <type 'object'>
    """  """
    def BuildContextMenuItems(self, *args): #cannot find CLR method
        """ BuildContextMenuItems(self: ContextMenuAddIn, addInRootSubmenu: ContextMenuAddInRoot) """
        ...


class MenuItem: # skipped bases: <type 'object'>, <type 'object'>
    """  """
    pass

class ContextMenuAddInRoot(IMenuItemContainerPrivate, MenuItem): # skipped bases: <type 'object'>
    """  """
    @property
    def DefaultLabelText(self) -> str:
        """ Get: DefaultLabelText(self: ContextMenuAddInRoot) -> str """
        ...

    @property
    def Items(self) -> ChildItemFactory:
        """ Get: Items(self: ContextMenuAddInRoot) -> ChildItemFactory """
        ...



class MenuSelectionProvider: # skipped bases: <type 'object'>
    """  """
    def GetSelection(self) -> IEnumerable:
        """
        GetSelection(self: MenuSelectionProvider) -> IEnumerable[object]
        GetSelection[TRequestedType](self: MenuSelectionProvider) -> IEnumerable[TRequestedType]
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class MenuStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MenuStatus, values: Disabled (1), Enabled (0), Hidden (2) """
    Disabled: MenuStatus = ...
    Enabled: MenuStatus = ...
    Hidden: MenuStatus = ...
    value__ = ...


class RadioButtonActionItemStyle(ActionItemStyle): # skipped bases: <type 'object'>
    """  """
    @property
    def State(self) -> RadioButtonState:
        """
        Get: State(self: RadioButtonActionItemStyle) -> RadioButtonState
        Set: State(self: RadioButtonActionItemStyle) = value
        """
        ...



class RadioButtonState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RadioButtonState, values: Selected (1), Unselected (0) """
    Selected: RadioButtonState = ...
    Unselected: RadioButtonState = ...
    value__ = ...


class Submenu(IMenuItemContainerPrivate, MenuItem): # skipped bases: <type 'object'>
    """  """
    @property
    def DefaultLabelText(self) -> str:
        """ Get: DefaultLabelText(self: Submenu) -> str """
        ...

    @property
    def Items(self) -> ChildItemFactory:
        """ Get: Items(self: Submenu) -> ChildItemFactory """
        ...



