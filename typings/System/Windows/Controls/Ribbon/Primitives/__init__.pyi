# encoding: utf-8
# module System.Windows.Controls.Ribbon.Primitives calls itself Primitives
# from System.Windows.Controls.Ribbon, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import IEnumerable

from System.Web.UI.MobileControls import Panel

from System.Windows.Controls.Ribbon import Ribbon

from System.Workflow.ComponentModel import (DependencyObject, 
    DependencyProperty)

"""The following names are not found in the module: (
    IContainsStarLayoutManager, IMultiValueConverter, IScrollInfo, 
    IValueConverter, StackPanel, UIElement, VirtualizingPanel, 
    VirtualizingStackPanel)
"""

# no functions
# classes

class IProvideStarLayoutInfoBase: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TargetElement(self): # -> UIElement
        """ Get: TargetElement(self: IProvideStarLayoutInfoBase) -> UIElement """
        ...


    def OnInitializeLayout(self): # -> 
        """ OnInitializeLayout(self: IProvideStarLayoutInfoBase) """
        ...


class IProvideStarLayoutInfo(IProvideStarLayoutInfoBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def StarLayoutCombinations(self) -> IEnumerable:
        """ Get: StarLayoutCombinations(self: IProvideStarLayoutInfo) -> IEnumerable[StarLayoutInfo] """
        ...


    def OnStarSizeAllocationCompleted(self): # -> 
        """ OnStarSizeAllocationCompleted(self: IProvideStarLayoutInfo) """
        ...


class ISupportStarLayout: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsStarLayoutPass(self) -> bool:
        """ Get: IsStarLayoutPass(self: ISupportStarLayout) -> bool """
        ...


    def RegisterStarLayoutProvider(self, starLayoutInfoProvider:IProvideStarLayoutInfoBase): # -> 
        """ RegisterStarLayoutProvider(self: ISupportStarLayout, starLayoutInfoProvider: IProvideStarLayoutInfoBase) """
        ...

    def UnregisterStarLayoutProvider(self, starLayoutInfoProvider:IProvideStarLayoutInfoBase): # -> 
        """ UnregisterStarLayoutProvider(self: ISupportStarLayout, starLayoutInfoProvider: IProvideStarLayoutInfoBase) """
        ...


class RibbonContextualTabGroupsPanel(Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonContextualTabGroupsPanel() """
    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonContextualTabGroupsPanel) -> Ribbon """
        ...


    RibbonProperty: DependencyProperty = ...


class RibbonGalleryCategoriesPanel(IScrollInfo, IProvideStarLayoutInfoBase, Panel, IContainsStarLayoutManager): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonGalleryCategoriesPanel() """
    pass

class RibbonGalleryItemsPanel(Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonGalleryItemsPanel() """
    pass

class RibbonGroupItemsPanel(IProvideStarLayoutInfo, IContainsStarLayoutManager, Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'IProvideStarLayoutInfoBase'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonGroupItemsPanel() """
    @property
    def TargetElement(self): # -> UIElement
        """ Get: TargetElement(self: RibbonGroupItemsPanel) -> UIElement """
        ...


    def OnInitializeLayout(self): # -> 
        """ OnInitializeLayout(self: RibbonGroupItemsPanel) """
        ...


class RibbonGroupsPanel(StackPanel, ISupportStarLayout): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IScrollInfo'>, <type 'IStackMeasure'>, <type 'object'>
    """ RibbonGroupsPanel() """
    IsStarLayoutPassProperty: DependencyProperty = ...


class RibbonMenuItemsPanel(VirtualizingStackPanel, ISupportStarLayout): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IScrollInfo'>, <type 'IStackMeasure'>, <type 'object'>
    """ RibbonMenuItemsPanel() """
    pass

class RibbonQuickAccessToolBarOverflowPanel(Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonQuickAccessToolBarOverflowPanel() """
    pass

class RibbonQuickAccessToolBarPanel(VirtualizingPanel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonQuickAccessToolBarPanel() """
    pass

class RibbonScrollButtonVisibilityConverter(IMultiValueConverter): # skipped bases: <type 'object'>
    """ RibbonScrollButtonVisibilityConverter() """
    pass

class RibbonTabHeadersPanel(IScrollInfo, Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTabHeadersPanel() """
    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonTabHeadersPanel) -> Ribbon """
        ...


    RibbonProperty: DependencyProperty = ...


class RibbonTabsPanel(IScrollInfo, Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTabsPanel() """
    pass

class RibbonTitlePanel(Panel): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTitlePanel() """
    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonTitlePanel) -> Ribbon """
        ...


    RibbonProperty: DependencyProperty = ...


class RibbonWindowSmallIconConverter(IValueConverter): # skipped bases: <type 'object'>
    """ RibbonWindowSmallIconConverter() """
    pass

class StarLayoutInfo(DependencyObject): # skipped bases: <type 'object'>
    """ StarLayoutInfo() """
    @property
    def AllocatedStarWidth(self) -> float:
        """
        Get: AllocatedStarWidth(self: StarLayoutInfo) -> float
        Set: AllocatedStarWidth(self: StarLayoutInfo) = value
        """
        ...

    @property
    def RequestedStarMaxWidth(self) -> float:
        """
        Get: RequestedStarMaxWidth(self: StarLayoutInfo) -> float
        Set: RequestedStarMaxWidth(self: StarLayoutInfo) = value
        """
        ...

    @property
    def RequestedStarMinWidth(self) -> float:
        """
        Get: RequestedStarMinWidth(self: StarLayoutInfo) -> float
        Set: RequestedStarMinWidth(self: StarLayoutInfo) = value
        """
        ...

    @property
    def RequestedStarWeight(self) -> float:
        """
        Get: RequestedStarWeight(self: StarLayoutInfo) -> float
        Set: RequestedStarWeight(self: StarLayoutInfo) = value
        """
        ...


    AllocatedStarWidthProperty: DependencyProperty = ...
    RequestedStarMaxWidthProperty: DependencyProperty = ...
    RequestedStarMinWidthProperty: DependencyProperty = ...
    RequestedStarWeightProperty: DependencyProperty = ...


