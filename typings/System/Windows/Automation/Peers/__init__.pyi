# encoding: utf-8
# module System.Windows.Automation.Peers calls itself Peers
# from System.Windows.Controls.Ribbon, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Web.ModelBinding import IValueProvider

"""The following names are not found in the module: (ButtonAutomationPeer, 
    CheckBoxAutomationPeer, FrameworkElementAutomationPeer, 
    IExpandCollapseProvider, IInvokeProvider, IScrollItemProvider, 
    ISelectionItemProvider, ISelectionProvider, IToggleProvider, 
    ITransformProvider, ItemAutomationPeer, ItemsControlAutomationPeer, 
    RadioButtonAutomationPeer, SelectorAutomationPeer, 
    SelectorItemAutomationPeer, SeparatorAutomationPeer, 
    TextBoxAutomationPeer, ToggleButtonAutomationPeer, ToolTipAutomationPeer)
"""

# no functions
# classes

class RibbonMenuButtonAutomationPeer(ItemsControlAutomationPeer, IExpandCollapseProvider, ITransformProvider): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonMenuButtonAutomationPeer(owner: RibbonMenuButton) """
    pass

class RibbonApplicationMenuAutomationPeer(RibbonMenuButtonAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'ITransformProvider'>, <type 'IExpandCollapseProvider'>, <type 'object'>
    """ RibbonApplicationMenuAutomationPeer(owner: RibbonApplicationMenu) """
    pass

class RibbonAutomationPeer(SelectorAutomationPeer, IExpandCollapseProvider): # skipped bases: <type 'IItemContainerProvider'>, <type 'ISelectionProvider'>, <type 'object'>
    """ RibbonAutomationPeer(owner: Ribbon) """
    pass

class RibbonButtonAutomationPeer(ButtonAutomationPeer): # skipped bases: <type 'IInvokeProvider'>, <type 'object'>
    """ RibbonButtonAutomationPeer(owner: RibbonButton) """
    pass

class RibbonCheckBoxAutomationPeer(CheckBoxAutomationPeer): # skipped bases: <type 'IToggleProvider'>, <type 'object'>
    """ RibbonCheckBoxAutomationPeer(owner: RibbonCheckBox) """
    pass

class RibbonComboBoxAutomationPeer(RibbonMenuButtonAutomationPeer, IValueProvider): # skipped bases: <type 'IItemContainerProvider'>, <type 'ITransformProvider'>, <type 'IExpandCollapseProvider'>, <type 'object'>
    """ RibbonComboBoxAutomationPeer(owner: RibbonComboBox) """
    pass

class RibbonContextMenuAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonContextMenuAutomationPeer(owner: RibbonContextMenu) """
    pass

class RibbonContextualTabGroupAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonContextualTabGroupAutomationPeer(owner: RibbonContextualTabGroup) """
    pass

class RibbonContextualTabGroupDataAutomationPeer(ItemAutomationPeer, IInvokeProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonContextualTabGroupDataAutomationPeer(item: object, owner: RibbonContextualTabGroupItemsControlAutomationPeer) """
    pass

class RibbonContextualTabGroupItemsControlAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonContextualTabGroupItemsControlAutomationPeer(owner: RibbonContextualTabGroupItemsControl) """
    pass

class RibbonControlAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonControlAutomationPeer(owner: FrameworkElement) """
    pass

class RibbonControlDataAutomationPeer(ItemAutomationPeer): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonControlDataAutomationPeer(item: object, itemsControlPeer: ItemsControlAutomationPeer) """
    pass

class RibbonControlGroupAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonControlGroupAutomationPeer(owner: RibbonControlGroup) """
    pass

class RibbonGalleryAutomationPeer(ISelectionProvider, ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonGalleryAutomationPeer(owner: RibbonGallery) """
    pass

class RibbonGalleryCategoryAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonGalleryCategoryAutomationPeer(owner: RibbonGalleryCategory) """
    pass

class RibbonGalleryCategoryDataAutomationPeer(ItemAutomationPeer, IScrollItemProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonGalleryCategoryDataAutomationPeer(owner: object, itemsControlAutomationPeer: ItemsControlAutomationPeer) """
    pass

class RibbonGalleryItemAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonGalleryItemAutomationPeer(owner: RibbonGalleryItem) """
    pass

class RibbonGalleryItemDataAutomationPeer(ISelectionItemProvider, ItemAutomationPeer, IScrollItemProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonGalleryItemDataAutomationPeer(owner: object, itemsControlAutomationPeer: ItemsControlAutomationPeer, parentCategoryDataAutomationPeer: RibbonGalleryCategoryDataAutomationPeer) """
    @property
    def ParentCategoryDataAutomationPeer(self) -> RibbonGalleryCategoryDataAutomationPeer:
        """ Get: ParentCategoryDataAutomationPeer(self: RibbonGalleryItemDataAutomationPeer) -> RibbonGalleryCategoryDataAutomationPeer """
        ...



class RibbonGroupAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonGroupAutomationPeer(owner: RibbonGroup) """
    pass

class RibbonGroupDataAutomationPeer(ItemAutomationPeer, IScrollItemProvider, IExpandCollapseProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonGroupDataAutomationPeer(item: object, itemsControlPeer: RibbonTabAutomationPeer) """
    pass

class RibbonGroupHeaderAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonGroupHeaderAutomationPeer(owner: FrameworkElement) """
    pass

class RibbonMenuItemAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonMenuItemAutomationPeer(owner: RibbonMenuItem) """
    pass

class RibbonMenuItemDataAutomationPeer(IToggleProvider, ItemAutomationPeer, IInvokeProvider, IExpandCollapseProvider, ITransformProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonMenuItemDataAutomationPeer(item: object, itemsControlPeer: ItemsControlAutomationPeer) """
    pass

class RibbonQuickAccessToolBarAutomationPeer(ItemsControlAutomationPeer, IExpandCollapseProvider): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonQuickAccessToolBarAutomationPeer(owner: RibbonQuickAccessToolBar) """
    pass

class RibbonRadioButtonAutomationPeer(RadioButtonAutomationPeer): # skipped bases: <type 'IToggleProvider'>, <type 'ISelectionItemProvider'>, <type 'object'>
    """ RibbonRadioButtonAutomationPeer(owner: RibbonRadioButton) """
    pass

class RibbonSeparatorAutomationPeer(SeparatorAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonSeparatorAutomationPeer(owner: RibbonSeparator) """
    pass

class RibbonSplitButtonAutomationPeer(IToggleProvider, RibbonMenuButtonAutomationPeer, IInvokeProvider): # skipped bases: <type 'IItemContainerProvider'>, <type 'ITransformProvider'>, <type 'IExpandCollapseProvider'>, <type 'object'>
    """ RibbonSplitButtonAutomationPeer(owner: RibbonSplitButton) """
    pass

class RibbonTabAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonTabAutomationPeer(owner: RibbonTab) """
    pass

class RibbonTabDataAutomationPeer(SelectorItemAutomationPeer, IScrollItemProvider, IExpandCollapseProvider): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'ISelectionItemProvider'>, <type 'object'>
    """ RibbonTabDataAutomationPeer(item: object, itemsControlPeer: RibbonAutomationPeer) """
    pass

class RibbonTabHeaderAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonTabHeaderAutomationPeer(owner: RibbonTabHeader) """
    pass

class RibbonTabHeaderDataAutomationPeer(ItemAutomationPeer): # skipped bases: <type 'IVirtualizedItemProvider'>, <type 'object'>
    """ RibbonTabHeaderDataAutomationPeer(item: object, itemsControlPeer: RibbonTabHeaderItemsControlAutomationPeer) """
    pass

class RibbonTabHeaderItemsControlAutomationPeer(ItemsControlAutomationPeer): # skipped bases: <type 'IItemContainerProvider'>, <type 'object'>
    """ RibbonTabHeaderItemsControlAutomationPeer(owner: RibbonTabHeaderItemsControl) """
    pass

class RibbonTextBoxAutomationPeer(TextBoxAutomationPeer, IInvokeProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ RibbonTextBoxAutomationPeer(owner: RibbonTextBox) """
    pass

class RibbonTitleAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonTitleAutomationPeer(owner: FrameworkElement) """
    pass

class RibbonToggleButtonAutomationPeer(ToggleButtonAutomationPeer): # skipped bases: <type 'IToggleProvider'>, <type 'object'>
    """ RibbonToggleButtonAutomationPeer(owner: RibbonToggleButton) """
    pass

class RibbonToolTipAutomationPeer(ToolTipAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonToolTipAutomationPeer(owner: RibbonToolTip) """
    pass

class RibbonTwoLineTextAutomationPeer(FrameworkElementAutomationPeer): # skipped bases: <type 'object'>
    """ RibbonTwoLineTextAutomationPeer(owner: RibbonTwoLineText) """
    pass

