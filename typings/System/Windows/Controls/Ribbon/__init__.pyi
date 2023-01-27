# encoding: utf-8
# module System.Windows.Controls.Ribbon calls itself Ribbon
# from System.Windows.Controls.Ribbon, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Excel import Button, Menu, MenuItem, TextBox

from Microsoft.Office.Interop.Word import CheckBox, ContentControl, Style

from Microsoft.Vbe.Interop import Window

from Microsoft.Vbe.Interop.Forms import ToggleButton

from Microsoft.VisualBasic import Collection

from Microsoft.Windows.Input import IPreviewCommandSource

from System import (AsyncCallback, Enum, IAsyncResult, IEquatable, 
    MulticastDelegate, Nullable)

from System.Collections import IEnumerable

from System.Collections.Specialized import StringCollection

from System.ComponentModel import TypeConverter

from System.Drawing import Brush

from System.Web.UI import Control

from System.Windows.Input import ICommand

from System.Workflow.ComponentModel import (DependencyObject, 
    DependencyProperty)

from Windows.UI.Xaml import CornerRadius

"""The following names are not found in the module: (BoundEvent, 
    ContentPresenter, ContextMenu, DataTemplate, DataTemplateSelector, 
    Freezable, FreezableCollection, Geometry, HeaderedItemsControl, 
    ICommandSource, IInputElement, ISyncKeyTipAndContent, IWeakEventListener, 
    ImageSource, ItemsControl, LineStackingStrategy, RadioButton, 
    RoutedCommand, RoutedEvent, RoutedEventArgs, RoutedUICommand, Selector, 
    Separator, StyleSelector, TextAlignment, TextDecorationCollection, 
    TextEffectCollection, TextTrimming, ToolTip, UIElement, Visibility, 
    field#)
"""

# no functions
# classes

class Ribbon(Selector): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ Ribbon() """
    @property
    def ApplicationMenu(self) -> RibbonApplicationMenu:
        """
        Get: ApplicationMenu(self: Ribbon) -> RibbonApplicationMenu
        Set: ApplicationMenu(self: Ribbon) = value
        """
        ...

    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: Ribbon) -> Brush
        Set: CheckedBackground(self: Ribbon) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: Ribbon) -> Brush
        Set: CheckedBorderBrush(self: Ribbon) = value
        """
        ...

    @property
    def ContextualTabGroupHeaderTemplate(self): # -> DataTemplate
        """
        Get: ContextualTabGroupHeaderTemplate(self: Ribbon) -> DataTemplate
        Set: ContextualTabGroupHeaderTemplate(self: Ribbon) = value
        """
        ...

    @property
    def ContextualTabGroups(self) -> Collection:
        """ Get: ContextualTabGroups(self: Ribbon) -> Collection[RibbonContextualTabGroup] """
        ...

    @property
    def ContextualTabGroupsSource(self) -> IEnumerable:
        """
        Get: ContextualTabGroupsSource(self: Ribbon) -> IEnumerable
        Set: ContextualTabGroupsSource(self: Ribbon) = value
        """
        ...

    @property
    def ContextualTabGroupStyle(self) -> Style:
        """
        Get: ContextualTabGroupStyle(self: Ribbon) -> Style
        Set: ContextualTabGroupStyle(self: Ribbon) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: Ribbon) -> Brush
        Set: FocusedBackground(self: Ribbon) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: Ribbon) -> Brush
        Set: FocusedBorderBrush(self: Ribbon) = value
        """
        ...

    @property
    def HelpPaneContent(self) -> object:
        """
        Get: HelpPaneContent(self: Ribbon) -> object
        Set: HelpPaneContent(self: Ribbon) = value
        """
        ...

    @property
    def HelpPaneContentTemplate(self): # -> DataTemplate
        """
        Get: HelpPaneContentTemplate(self: Ribbon) -> DataTemplate
        Set: HelpPaneContentTemplate(self: Ribbon) = value
        """
        ...

    @property
    def IsCollapsed(self) -> bool:
        """
        Get: IsCollapsed(self: Ribbon) -> bool
        Set: IsCollapsed(self: Ribbon) = value
        """
        ...

    @property
    def IsDropDownOpen(self) -> bool:
        """
        Get: IsDropDownOpen(self: Ribbon) -> bool
        Set: IsDropDownOpen(self: Ribbon) = value
        """
        ...

    @property
    def IsHostedInRibbonWindow(self) -> bool:
        """ Get: IsHostedInRibbonWindow(self: Ribbon) -> bool """
        ...

    @property
    def IsMinimized(self) -> bool:
        """
        Get: IsMinimized(self: Ribbon) -> bool
        Set: IsMinimized(self: Ribbon) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: Ribbon) -> Brush
        Set: MouseOverBackground(self: Ribbon) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: Ribbon) -> Brush
        Set: MouseOverBorderBrush(self: Ribbon) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: Ribbon) -> Brush
        Set: PressedBackground(self: Ribbon) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: Ribbon) -> Brush
        Set: PressedBorderBrush(self: Ribbon) = value
        """
        ...

    @property
    def QuickAccessToolBar(self) -> RibbonQuickAccessToolBar:
        """
        Get: QuickAccessToolBar(self: Ribbon) -> RibbonQuickAccessToolBar
        Set: QuickAccessToolBar(self: Ribbon) = value
        """
        ...

    @property
    def ShowQuickAccessToolBarOnTop(self) -> bool:
        """
        Get: ShowQuickAccessToolBarOnTop(self: Ribbon) -> bool
        Set: ShowQuickAccessToolBarOnTop(self: Ribbon) = value
        """
        ...

    @property
    def TabHeaderStyle(self) -> Style:
        """
        Get: TabHeaderStyle(self: Ribbon) -> Style
        Set: TabHeaderStyle(self: Ribbon) = value
        """
        ...

    @property
    def TabHeaderTemplate(self): # -> DataTemplate
        """
        Get: TabHeaderTemplate(self: Ribbon) -> DataTemplate
        Set: TabHeaderTemplate(self: Ribbon) = value
        """
        ...

    @property
    def Title(self) -> object:
        """
        Get: Title(self: Ribbon) -> object
        Set: Title(self: Ribbon) = value
        """
        ...

    @property
    def TitleTemplate(self): # -> DataTemplate
        """
        Get: TitleTemplate(self: Ribbon) -> DataTemplate
        Set: TitleTemplate(self: Ribbon) = value
        """
        ...

    @property
    def WindowIconVisibility(self): # -> Visibility
        """
        Get: WindowIconVisibility(self: Ribbon) -> Visibility
        Set: WindowIconVisibility(self: Ribbon) = value
        """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: Ribbon) """
        ...

    ApplicationMenuProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    Collapsed = ...
    CollapsedEvent = ...
    ContextualTabGroupHeaderTemplateProperty: DependencyProperty = ...
    ContextualTabGroupsSourceProperty: DependencyProperty = ...
    ContextualTabGroupStyleProperty: DependencyProperty = ...
    Expanded = ...
    ExpandedEvent = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    HelpPaneContentProperty: DependencyProperty = ...
    HelpPaneContentTemplateProperty: DependencyProperty = ...
    IsCollapsedProperty: DependencyProperty = ...
    IsDropDownOpenProperty: DependencyProperty = ...
    IsHostedInRibbonWindowProperty: DependencyProperty = ...
    IsMinimizedProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarProperty: DependencyProperty = ...
    ShowQuickAccessToolBarOnTopProperty: DependencyProperty = ...
    TabHeaderStyleProperty: DependencyProperty = ...
    TabHeaderTemplateProperty: DependencyProperty = ...
    TitleProperty: DependencyProperty = ...
    TitleTemplateProperty: DependencyProperty = ...
    WindowIconVisibilityProperty: DependencyProperty = ...


class RibbonMenuButton(Menu): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonMenuButton() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonMenuButton) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonMenuButton) = value
        """
        ...

    @property
    def CanUserResizeHorizontally(self) -> bool:
        """
        Get: CanUserResizeHorizontally(self: RibbonMenuButton) -> bool
        Set: CanUserResizeHorizontally(self: RibbonMenuButton) = value
        """
        ...

    @property
    def CanUserResizeVertically(self) -> bool:
        """
        Get: CanUserResizeVertically(self: RibbonMenuButton) -> bool
        Set: CanUserResizeVertically(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonMenuButton) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonMenuButton) = value
        """
        ...

    @property
    def DropDownHeight(self) -> float:
        """
        Get: DropDownHeight(self: RibbonMenuButton) -> float
        Set: DropDownHeight(self: RibbonMenuButton) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonMenuButton) -> Brush
        Set: FocusedBackground(self: RibbonMenuButton) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonMenuButton) -> Brush
        Set: FocusedBorderBrush(self: RibbonMenuButton) = value
        """
        ...

    @property
    def HasGallery(self) -> bool:
        """ Get: HasGallery(self: RibbonMenuButton) -> bool """
        ...

    @property
    def IsDropDownOpen(self) -> bool:
        """
        Get: IsDropDownOpen(self: RibbonMenuButton) -> bool
        Set: IsDropDownOpen(self: RibbonMenuButton) = value
        """
        ...

    @property
    def IsDropDownPositionedAbove(self) -> bool:
        """ Get: IsDropDownPositionedAbove(self: RibbonMenuButton) -> bool """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonMenuButton) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonMenuButton) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonMenuButton) -> str
        Set: KeyTip(self: RibbonMenuButton) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonMenuButton) -> str
        Set: Label(self: RibbonMenuButton) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonMenuButton) -> ImageSource
        Set: LargeImageSource(self: RibbonMenuButton) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonMenuButton) -> Brush
        Set: MouseOverBackground(self: RibbonMenuButton) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonMenuButton) -> Brush
        Set: MouseOverBorderBrush(self: RibbonMenuButton) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonMenuButton) -> Brush
        Set: PressedBackground(self: RibbonMenuButton) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonMenuButton) -> Brush
        Set: PressedBorderBrush(self: RibbonMenuButton) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonMenuButton) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonMenuButton) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonMenuButton) -> object
        Set: QuickAccessToolBarId(self: RibbonMenuButton) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonMenuButton) -> Ribbon """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonMenuButton) -> ImageSource
        Set: SmallImageSource(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonMenuButton) -> str
        Set: ToolTipDescription(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonMenuButton) -> str
        Set: ToolTipFooterDescription(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonMenuButton) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonMenuButton) -> str
        Set: ToolTipFooterTitle(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonMenuButton) -> ImageSource
        Set: ToolTipImageSource(self: RibbonMenuButton) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonMenuButton) -> str
        Set: ToolTipTitle(self: RibbonMenuButton) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonMenuButton, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonMenuButton) """
        ...

    def OnDismissPopup(self, *args): #cannot find CLR method
        """ OnDismissPopup(self: RibbonMenuButton, e: RibbonDismissPopupEventArgs) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonMenuButton, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CanUserResizeHorizontallyProperty: DependencyProperty = ...
    CanUserResizeVerticallyProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    DropDownClosed = ...
    DropDownHeightProperty: DependencyProperty = ...
    DropDownOpened = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    HasGalleryProperty: DependencyProperty = ...
    IsDropDownOpenProperty: DependencyProperty = ...
    IsDropDownPositionedAboveProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonApplicationMenu(RibbonMenuButton): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonApplicationMenu() """
    @property
    def AuxiliaryPaneContent(self) -> object:
        """
        Get: AuxiliaryPaneContent(self: RibbonApplicationMenu) -> object
        Set: AuxiliaryPaneContent(self: RibbonApplicationMenu) = value
        """
        ...

    @property
    def AuxiliaryPaneContentTemplate(self): # -> DataTemplate
        """
        Get: AuxiliaryPaneContentTemplate(self: RibbonApplicationMenu) -> DataTemplate
        Set: AuxiliaryPaneContentTemplate(self: RibbonApplicationMenu) = value
        """
        ...

    @property
    def AuxiliaryPaneContentTemplateSelector(self): # -> DataTemplateSelector
        """
        Get: AuxiliaryPaneContentTemplateSelector(self: RibbonApplicationMenu) -> DataTemplateSelector
        Set: AuxiliaryPaneContentTemplateSelector(self: RibbonApplicationMenu) = value
        """
        ...

    @property
    def FooterPaneContent(self) -> object:
        """
        Get: FooterPaneContent(self: RibbonApplicationMenu) -> object
        Set: FooterPaneContent(self: RibbonApplicationMenu) = value
        """
        ...

    @property
    def FooterPaneContentTemplate(self): # -> DataTemplate
        """
        Get: FooterPaneContentTemplate(self: RibbonApplicationMenu) -> DataTemplate
        Set: FooterPaneContentTemplate(self: RibbonApplicationMenu) = value
        """
        ...

    @property
    def FooterPaneContentTemplateSelector(self): # -> DataTemplateSelector
        """
        Get: FooterPaneContentTemplateSelector(self: RibbonApplicationMenu) -> DataTemplateSelector
        Set: FooterPaneContentTemplateSelector(self: RibbonApplicationMenu) = value
        """
        ...


    AuxiliaryPaneContentProperty: DependencyProperty = ...
    AuxiliaryPaneContentTemplateProperty: DependencyProperty = ...
    AuxiliaryPaneContentTemplateSelectorProperty: DependencyProperty = ...
    FooterPaneContentProperty: DependencyProperty = ...
    FooterPaneContentTemplateProperty: DependencyProperty = ...
    FooterPaneContentTemplateSelectorProperty: DependencyProperty = ...


class RibbonMenuItem(ISyncKeyTipAndContent, MenuItem): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ICommandSource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonMenuItem() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonMenuItem) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonMenuItem) = value
        """
        ...

    @property
    def CanUserResizeHorizontally(self) -> bool:
        """
        Get: CanUserResizeHorizontally(self: RibbonMenuItem) -> bool
        Set: CanUserResizeHorizontally(self: RibbonMenuItem) = value
        """
        ...

    @property
    def CanUserResizeVertically(self) -> bool:
        """
        Get: CanUserResizeVertically(self: RibbonMenuItem) -> bool
        Set: CanUserResizeVertically(self: RibbonMenuItem) = value
        """
        ...

    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonMenuItem) -> Brush
        Set: CheckedBackground(self: RibbonMenuItem) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonMenuItem) -> Brush
        Set: CheckedBorderBrush(self: RibbonMenuItem) = value
        """
        ...

    @property
    def DropDownHeight(self) -> float:
        """
        Get: DropDownHeight(self: RibbonMenuItem) -> float
        Set: DropDownHeight(self: RibbonMenuItem) = value
        """
        ...

    @property
    def HasGallery(self) -> bool:
        """ Get: HasGallery(self: RibbonMenuItem) -> bool """
        ...

    @property
    def ImageSource(self): # -> ImageSource
        """
        Get: ImageSource(self: RibbonMenuItem) -> ImageSource
        Set: ImageSource(self: RibbonMenuItem) = value
        """
        ...

    @property
    def IsDropDownPositionedLeft(self) -> bool:
        """ Get: IsDropDownPositionedLeft(self: RibbonMenuItem) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonMenuItem) -> str
        Set: KeyTip(self: RibbonMenuItem) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonMenuItem) -> Brush
        Set: MouseOverBackground(self: RibbonMenuItem) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonMenuItem) -> Brush
        Set: MouseOverBorderBrush(self: RibbonMenuItem) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonMenuItem) -> Brush
        Set: PressedBackground(self: RibbonMenuItem) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonMenuItem) -> Brush
        Set: PressedBorderBrush(self: RibbonMenuItem) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonMenuItem) -> object
        Set: QuickAccessToolBarId(self: RibbonMenuItem) = value
        """
        ...

    @property
    def QuickAccessToolBarImageSource(self): # -> ImageSource
        """
        Get: QuickAccessToolBarImageSource(self: RibbonMenuItem) -> ImageSource
        Set: QuickAccessToolBarImageSource(self: RibbonMenuItem) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonMenuItem) -> Ribbon """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonMenuItem) -> str
        Set: ToolTipDescription(self: RibbonMenuItem) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonMenuItem) -> str
        Set: ToolTipFooterDescription(self: RibbonMenuItem) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonMenuItem) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonMenuItem) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonMenuItem) -> str
        Set: ToolTipFooterTitle(self: RibbonMenuItem) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonMenuItem) -> ImageSource
        Set: ToolTipImageSource(self: RibbonMenuItem) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonMenuItem) -> str
        Set: ToolTipTitle(self: RibbonMenuItem) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonMenuItem, e: ActivatingKeyTipEventArgs) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonMenuItem, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CanUserResizeHorizontallyProperty: DependencyProperty = ...
    CanUserResizeVerticallyProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    DropDownHeightProperty: DependencyProperty = ...
    HasGalleryProperty: DependencyProperty = ...
    ImageSourceProperty: DependencyProperty = ...
    IsDropDownPositionedLeftProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    QuickAccessToolBarImageSourceProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonApplicationMenuItem(RibbonMenuItem): # skipped bases: <type 'IFrameworkInputElement'>, <type 'ISyncKeyTipAndContent'>, <type 'ICommandSource'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonApplicationMenuItem() """
    @property
    def Level(self) -> RibbonApplicationMenuItemLevel:
        """ Get: Level(self: RibbonApplicationMenuItem) -> RibbonApplicationMenuItemLevel """
        ...


    LevelProperty: DependencyProperty = ...


class RibbonApplicationMenuItemLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RibbonApplicationMenuItemLevel, values: Middle (1), Sub (2), Top (0) """
    Middle: RibbonApplicationMenuItemLevel = ...
    Sub: RibbonApplicationMenuItemLevel = ...
    Top: RibbonApplicationMenuItemLevel = ...
    value__ = ...


class RibbonSplitMenuItem(RibbonMenuItem): # skipped bases: <type 'IFrameworkInputElement'>, <type 'ISyncKeyTipAndContent'>, <type 'ICommandSource'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonSplitMenuItem() """
    @property
    def DropDownToolTipDescription(self) -> str:
        """
        Get: DropDownToolTipDescription(self: RibbonSplitMenuItem) -> str
        Set: DropDownToolTipDescription(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def DropDownToolTipFooterDescription(self) -> str:
        """
        Get: DropDownToolTipFooterDescription(self: RibbonSplitMenuItem) -> str
        Set: DropDownToolTipFooterDescription(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def DropDownToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: DropDownToolTipFooterImageSource(self: RibbonSplitMenuItem) -> ImageSource
        Set: DropDownToolTipFooterImageSource(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def DropDownToolTipFooterTitle(self) -> str:
        """
        Get: DropDownToolTipFooterTitle(self: RibbonSplitMenuItem) -> str
        Set: DropDownToolTipFooterTitle(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def DropDownToolTipImageSource(self): # -> ImageSource
        """
        Get: DropDownToolTipImageSource(self: RibbonSplitMenuItem) -> ImageSource
        Set: DropDownToolTipImageSource(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def DropDownToolTipTitle(self) -> str:
        """
        Get: DropDownToolTipTitle(self: RibbonSplitMenuItem) -> str
        Set: DropDownToolTipTitle(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def HeaderKeyTip(self) -> str:
        """
        Get: HeaderKeyTip(self: RibbonSplitMenuItem) -> str
        Set: HeaderKeyTip(self: RibbonSplitMenuItem) = value
        """
        ...

    @property
    def HeaderQuickAccessToolBarId(self) -> object:
        """
        Get: HeaderQuickAccessToolBarId(self: RibbonSplitMenuItem) -> object
        Set: HeaderQuickAccessToolBarId(self: RibbonSplitMenuItem) = value
        """
        ...


    DropDownToolTipDescriptionProperty: DependencyProperty = ...
    DropDownToolTipFooterDescriptionProperty: DependencyProperty = ...
    DropDownToolTipFooterImageSourceProperty: DependencyProperty = ...
    DropDownToolTipFooterTitleProperty: DependencyProperty = ...
    DropDownToolTipImageSourceProperty: DependencyProperty = ...
    DropDownToolTipTitleProperty: DependencyProperty = ...
    HeaderKeyTipProperty: DependencyProperty = ...
    HeaderQuickAccessToolBarIdProperty: DependencyProperty = ...


class RibbonApplicationSplitMenuItem(RibbonSplitMenuItem): # skipped bases: <type 'IFrameworkInputElement'>, <type 'ISyncKeyTipAndContent'>, <type 'ICommandSource'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonApplicationSplitMenuItem() """
    @property
    def Level(self) -> RibbonApplicationMenuItemLevel:
        """ Get: Level(self: RibbonApplicationSplitMenuItem) -> RibbonApplicationMenuItemLevel """
        ...


    LevelProperty: DependencyProperty = ...


class RibbonButton(Button): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'ICommandSource'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonButton() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonButton) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonButton) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonButton) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonButton) = value
        """
        ...

    @property
    def CornerRadius(self) -> CornerRadius:
        """
        Get: CornerRadius(self: RibbonButton) -> CornerRadius
        Set: CornerRadius(self: RibbonButton) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonButton) -> Brush
        Set: FocusedBackground(self: RibbonButton) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonButton) -> Brush
        Set: FocusedBorderBrush(self: RibbonButton) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonButton) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonButton) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonButton) -> str
        Set: KeyTip(self: RibbonButton) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonButton) -> str
        Set: Label(self: RibbonButton) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonButton) -> ImageSource
        Set: LargeImageSource(self: RibbonButton) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonButton) -> Brush
        Set: MouseOverBackground(self: RibbonButton) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonButton) -> Brush
        Set: MouseOverBorderBrush(self: RibbonButton) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonButton) -> Brush
        Set: PressedBackground(self: RibbonButton) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonButton) -> Brush
        Set: PressedBorderBrush(self: RibbonButton) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonButton) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonButton) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonButton) -> object
        Set: QuickAccessToolBarId(self: RibbonButton) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonButton) -> Ribbon """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonButton) -> bool """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonButton) -> ImageSource
        Set: SmallImageSource(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonButton) -> str
        Set: ToolTipDescription(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonButton) -> str
        Set: ToolTipFooterDescription(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonButton) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonButton) -> str
        Set: ToolTipFooterTitle(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonButton) -> ImageSource
        Set: ToolTipImageSource(self: RibbonButton) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonButton) -> str
        Set: ToolTipTitle(self: RibbonButton) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonButton, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonButton) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonButton, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    CornerRadiusProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonCheckBox(CheckBox): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'ICommandSource'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonCheckBox() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonCheckBox) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonCheckBox) = value
        """
        ...

    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonCheckBox) -> Brush
        Set: CheckedBackground(self: RibbonCheckBox) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonCheckBox) -> Brush
        Set: CheckedBorderBrush(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonCheckBox) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonCheckBox) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonCheckBox) -> Brush
        Set: FocusedBackground(self: RibbonCheckBox) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonCheckBox) -> Brush
        Set: FocusedBorderBrush(self: RibbonCheckBox) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonCheckBox) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonCheckBox) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonCheckBox) -> str
        Set: KeyTip(self: RibbonCheckBox) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonCheckBox) -> str
        Set: Label(self: RibbonCheckBox) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonCheckBox) -> ImageSource
        Set: LargeImageSource(self: RibbonCheckBox) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonCheckBox) -> Brush
        Set: MouseOverBackground(self: RibbonCheckBox) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonCheckBox) -> Brush
        Set: MouseOverBorderBrush(self: RibbonCheckBox) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonCheckBox) -> Brush
        Set: PressedBackground(self: RibbonCheckBox) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonCheckBox) -> Brush
        Set: PressedBorderBrush(self: RibbonCheckBox) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonCheckBox) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonCheckBox) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonCheckBox) -> object
        Set: QuickAccessToolBarId(self: RibbonCheckBox) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonCheckBox) -> Ribbon """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonCheckBox) -> bool """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonCheckBox) -> ImageSource
        Set: SmallImageSource(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonCheckBox) -> str
        Set: ToolTipDescription(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonCheckBox) -> str
        Set: ToolTipFooterDescription(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonCheckBox) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonCheckBox) -> str
        Set: ToolTipFooterTitle(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonCheckBox) -> ImageSource
        Set: ToolTipImageSource(self: RibbonCheckBox) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonCheckBox) -> str
        Set: ToolTipTitle(self: RibbonCheckBox) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonCheckBox, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonCheckBox) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonCheckBox, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonComboBox(RibbonMenuButton): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonComboBox() """
    @property
    def IsEditable(self) -> bool:
        """
        Get: IsEditable(self: RibbonComboBox) -> bool
        Set: IsEditable(self: RibbonComboBox) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: RibbonComboBox) -> bool
        Set: IsReadOnly(self: RibbonComboBox) = value
        """
        ...

    @property
    def SelectionBoxItem(self) -> object:
        """ Get: SelectionBoxItem(self: RibbonComboBox) -> object """
        ...

    @property
    def SelectionBoxItemStringFormat(self) -> str:
        """ Get: SelectionBoxItemStringFormat(self: RibbonComboBox) -> str """
        ...

    @property
    def SelectionBoxItemTemplate(self): # -> DataTemplate
        """ Get: SelectionBoxItemTemplate(self: RibbonComboBox) -> DataTemplate """
        ...

    @property
    def SelectionBoxItemTemplateSelector(self): # -> DataTemplateSelector
        """ Get: SelectionBoxItemTemplateSelector(self: RibbonComboBox) -> DataTemplateSelector """
        ...

    @property
    def SelectionBoxWidth(self) -> float:
        """
        Get: SelectionBoxWidth(self: RibbonComboBox) -> float
        Set: SelectionBoxWidth(self: RibbonComboBox) = value
        """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonComboBox) -> bool """
        ...

    @property
    def StaysOpenOnEdit(self) -> bool:
        """
        Get: StaysOpenOnEdit(self: RibbonComboBox) -> bool
        Set: StaysOpenOnEdit(self: RibbonComboBox) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: RibbonComboBox) -> str
        Set: Text(self: RibbonComboBox) = value
        """
        ...


    IsEditableProperty: DependencyProperty = ...
    IsReadOnlyProperty: DependencyProperty = ...
    SelectionBoxItemProperty: DependencyProperty = ...
    SelectionBoxItemStringFormatProperty: DependencyProperty = ...
    SelectionBoxItemTemplateProperty: DependencyProperty = ...
    SelectionBoxItemTemplateSelectorProperty: DependencyProperty = ...
    SelectionBoxWidthProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    StaysOpenOnEditProperty: DependencyProperty = ...
    TextProperty: DependencyProperty = ...


class RibbonCommands: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AddToQuickAccessToolBarCommand(self): # -> RoutedUICommand
        """ Get: AddToQuickAccessToolBarCommand() -> RoutedUICommand """
        ...

    @property
    def MaximizeRibbonCommand(self): # -> RoutedUICommand
        """ Get: MaximizeRibbonCommand() -> RoutedUICommand """
        ...

    @property
    def MinimizeRibbonCommand(self): # -> RoutedUICommand
        """ Get: MinimizeRibbonCommand() -> RoutedUICommand """
        ...

    @property
    def RemoveFromQuickAccessToolBarCommand(self): # -> RoutedUICommand
        """ Get: RemoveFromQuickAccessToolBarCommand() -> RoutedUICommand """
        ...

    @property
    def ShowQuickAccessToolBarAboveRibbonCommand(self): # -> RoutedUICommand
        """ Get: ShowQuickAccessToolBarAboveRibbonCommand() -> RoutedUICommand """
        ...

    @property
    def ShowQuickAccessToolBarBelowRibbonCommand(self): # -> RoutedUICommand
        """ Get: ShowQuickAccessToolBarBelowRibbonCommand() -> RoutedUICommand """
        ...


    __all__: list = ...


class RibbonContentPresenter(ContentPresenter): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonContentPresenter() """
    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonContentPresenter) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonContentPresenter) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonContentPresenter) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonContentPresenter) -> bool """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonContentPresenter) """
        ...

    ControlSizeDefinitionProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...


class RibbonContextMenu(ContextMenu): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonContextMenu() """
    @property
    def HasGallery(self) -> bool:
        """ Get: HasGallery(self: RibbonContextMenu) -> bool """
        ...


    HasGalleryProperty: DependencyProperty = ...


class RibbonContextualTabGroup(Control): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonContextualTabGroup() """
    @property
    def Header(self) -> object:
        """
        Get: Header(self: RibbonContextualTabGroup) -> object
        Set: Header(self: RibbonContextualTabGroup) = value
        """
        ...

    @property
    def HeaderStringFormat(self) -> str:
        """
        Get: HeaderStringFormat(self: RibbonContextualTabGroup) -> str
        Set: HeaderStringFormat(self: RibbonContextualTabGroup) = value
        """
        ...

    @property
    def HeaderTemplate(self): # -> DataTemplate
        """
        Get: HeaderTemplate(self: RibbonContextualTabGroup) -> DataTemplate
        Set: HeaderTemplate(self: RibbonContextualTabGroup) = value
        """
        ...

    @property
    def HeaderTemplateSelector(self): # -> DataTemplateSelector
        """
        Get: HeaderTemplateSelector(self: RibbonContextualTabGroup) -> DataTemplateSelector
        Set: HeaderTemplateSelector(self: RibbonContextualTabGroup) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonContextualTabGroup) -> Ribbon """
        ...


    def OnHeaderChanged(self, *args): #cannot find CLR method
        """ OnHeaderChanged(self: RibbonContextualTabGroup, oldHeader: object, newHeader: object) """
        ...

    HeaderProperty: DependencyProperty = ...
    HeaderStringFormatProperty: DependencyProperty = ...
    HeaderTemplateProperty: DependencyProperty = ...
    HeaderTemplateSelectorProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...


class RibbonContextualTabGroupItemsControl(ItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonContextualTabGroupItemsControl() """
    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonContextualTabGroupItemsControl) -> Ribbon """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonContextualTabGroupItemsControl) """
        ...

    RibbonProperty: DependencyProperty = ...


class RibbonControl(ContentControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonControl() """
    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonControl) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonControl) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonControl) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonControl) -> bool """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonControl) """
        ...

    ControlSizeDefinitionProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...


class RibbonControlGroup(ItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonControlGroup() """
    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonControlGroup) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonControlGroup) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonControlGroup) -> Ribbon """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonControlGroup) """
        ...

    ControlSizeDefinitionProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...


class RibbonControlLength(IEquatable): # skipped bases: <type 'object'>
    """
    RibbonControlLength(pixels: float)
    RibbonControlLength(value: float, type: RibbonControlLengthUnitType)
    """
    @property
    def Auto(self) -> RibbonControlLength:
        """ Get: Auto() -> RibbonControlLength """
        ...

    @property
    def IsAbsolute(self) -> bool:
        """ Get: IsAbsolute(self: RibbonControlLength) -> bool """
        ...

    @property
    def IsAuto(self) -> bool:
        """ Get: IsAuto(self: RibbonControlLength) -> bool """
        ...

    @property
    def IsStar(self) -> bool:
        """ Get: IsStar(self: RibbonControlLength) -> bool """
        ...

    @property
    def RibbonControlLengthUnitType(self) -> RibbonControlLengthUnitType:
        """ Get: RibbonControlLengthUnitType(self: RibbonControlLength) -> RibbonControlLengthUnitType """
        ...

    @property
    def Value(self) -> float:
        """ Get: Value(self: RibbonControlLength) -> float """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: RibbonControlLength) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RibbonControlLength) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RibbonControlLengthConverter(TypeConverter): # skipped bases: <type 'object'>
    """ RibbonControlLengthConverter() """
    pass

class RibbonControlLengthUnitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RibbonControlLengthUnitType, values: Auto (0), Item (2), Pixel (1), Star (3) """
    Auto: RibbonControlLengthUnitType = ...
    Item: RibbonControlLengthUnitType = ...
    Pixel: RibbonControlLengthUnitType = ...
    Star: RibbonControlLengthUnitType = ...
    value__ = ...


class RibbonControlService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddDismissPopupHandler(element:DependencyObject, handler:RibbonDismissPopupEventHandler): # -> 
        """ AddDismissPopupHandler(element: DependencyObject, handler: RibbonDismissPopupEventHandler) """
        ...

    @staticmethod
    def GetCanAddToQuickAccessToolBarDirectly(element:DependencyObject) -> bool:
        """ GetCanAddToQuickAccessToolBarDirectly(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetCheckedBackground(element:DependencyObject) -> Brush:
        """ GetCheckedBackground(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetCheckedBorderBrush(element:DependencyObject) -> Brush:
        """ GetCheckedBorderBrush(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetControlSizeDefinition(element:DependencyObject) -> RibbonControlSizeDefinition:
        """ GetControlSizeDefinition(element: DependencyObject) -> RibbonControlSizeDefinition """
        ...

    @staticmethod
    def GetCornerRadius(element:DependencyObject) -> CornerRadius:
        """ GetCornerRadius(element: DependencyObject) -> CornerRadius """
        ...

    @staticmethod
    def GetDefaultControlSizeDefinition(element:DependencyObject) -> RibbonControlSizeDefinition:
        """ GetDefaultControlSizeDefinition(element: DependencyObject) -> RibbonControlSizeDefinition """
        ...

    @staticmethod
    def GetFocusedBackground(element:DependencyObject) -> Brush:
        """ GetFocusedBackground(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetFocusedBorderBrush(element:DependencyObject) -> Brush:
        """ GetFocusedBorderBrush(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetIsInControlGroup(element:DependencyObject) -> bool:
        """ GetIsInControlGroup(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetIsInQuickAccessToolBar(element:DependencyObject) -> bool:
        """ GetIsInQuickAccessToolBar(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetLabel(element:DependencyObject) -> str:
        """ GetLabel(element: DependencyObject) -> str """
        ...

    @staticmethod
    def GetLargeImageSource(element:DependencyObject): # -> ImageSource
        """ GetLargeImageSource(element: DependencyObject) -> ImageSource """
        ...

    @staticmethod
    def GetMouseOverBackground(element:DependencyObject) -> Brush:
        """ GetMouseOverBackground(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetMouseOverBorderBrush(element:DependencyObject) -> Brush:
        """ GetMouseOverBorderBrush(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetPressedBackground(element:DependencyObject) -> Brush:
        """ GetPressedBackground(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetPressedBorderBrush(element:DependencyObject) -> Brush:
        """ GetPressedBorderBrush(element: DependencyObject) -> Brush """
        ...

    @staticmethod
    def GetQuickAccessToolBarControlSizeDefinition(element:DependencyObject) -> RibbonControlSizeDefinition:
        """ GetQuickAccessToolBarControlSizeDefinition(element: DependencyObject) -> RibbonControlSizeDefinition """
        ...

    @staticmethod
    def GetQuickAccessToolBarId(element:DependencyObject) -> object:
        """ GetQuickAccessToolBarId(element: DependencyObject) -> object """
        ...

    @staticmethod
    def GetRibbon(element:DependencyObject) -> Ribbon:
        """ GetRibbon(element: DependencyObject) -> Ribbon """
        ...

    @staticmethod
    def GetShowKeyboardCues(element:DependencyObject) -> bool:
        """ GetShowKeyboardCues(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetSmallImageSource(element:DependencyObject): # -> ImageSource
        """ GetSmallImageSource(element: DependencyObject) -> ImageSource """
        ...

    @staticmethod
    def GetToolTipDescription(element:DependencyObject) -> str:
        """ GetToolTipDescription(element: DependencyObject) -> str """
        ...

    @staticmethod
    def GetToolTipFooterDescription(element:DependencyObject) -> str:
        """ GetToolTipFooterDescription(element: DependencyObject) -> str """
        ...

    @staticmethod
    def GetToolTipFooterImageSource(element:DependencyObject): # -> ImageSource
        """ GetToolTipFooterImageSource(element: DependencyObject) -> ImageSource """
        ...

    @staticmethod
    def GetToolTipFooterTitle(element:DependencyObject) -> str:
        """ GetToolTipFooterTitle(element: DependencyObject) -> str """
        ...

    @staticmethod
    def GetToolTipImageSource(element:DependencyObject): # -> ImageSource
        """ GetToolTipImageSource(element: DependencyObject) -> ImageSource """
        ...

    @staticmethod
    def GetToolTipTitle(element:DependencyObject) -> str:
        """ GetToolTipTitle(element: DependencyObject) -> str """
        ...

    @staticmethod
    def RemoveDismissPopupHandler(element:DependencyObject, handler:RibbonDismissPopupEventHandler): # -> 
        """ RemoveDismissPopupHandler(element: DependencyObject, handler: RibbonDismissPopupEventHandler) """
        ...

    @staticmethod
    def SetCanAddToQuickAccessToolBarDirectly(element:DependencyObject, value:bool): # -> 
        """ SetCanAddToQuickAccessToolBarDirectly(element: DependencyObject, value: bool) """
        ...

    @staticmethod
    def SetCheckedBackground(element:DependencyObject, value:Brush): # -> 
        """ SetCheckedBackground(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetCheckedBorderBrush(element:DependencyObject, value:Brush): # -> 
        """ SetCheckedBorderBrush(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetControlSizeDefinition(element:DependencyObject, value:RibbonControlSizeDefinition): # -> 
        """ SetControlSizeDefinition(element: DependencyObject, value: RibbonControlSizeDefinition) """
        ...

    @staticmethod
    def SetCornerRadius(element:DependencyObject, value:CornerRadius): # -> 
        """ SetCornerRadius(element: DependencyObject, value: CornerRadius) """
        ...

    @staticmethod
    def SetDefaultControlSizeDefinition(element:DependencyObject, value:RibbonControlSizeDefinition): # -> 
        """ SetDefaultControlSizeDefinition(element: DependencyObject, value: RibbonControlSizeDefinition) """
        ...

    @staticmethod
    def SetFocusedBackground(element:DependencyObject, value:Brush): # -> 
        """ SetFocusedBackground(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetFocusedBorderBrush(element:DependencyObject, value:Brush): # -> 
        """ SetFocusedBorderBrush(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetLabel(element:DependencyObject, value:str): # -> 
        """ SetLabel(element: DependencyObject, value: str) """
        ...

    @staticmethod
    def SetLargeImageSource(element:DependencyObject, value): # ->  # Not found arg types: {'value': 'ImageSource'}
        """ SetLargeImageSource(element: DependencyObject, value: ImageSource) """
        ...

    @staticmethod
    def SetMouseOverBackground(element:DependencyObject, value:Brush): # -> 
        """ SetMouseOverBackground(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetMouseOverBorderBrush(element:DependencyObject, value:Brush): # -> 
        """ SetMouseOverBorderBrush(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetPressedBackground(element:DependencyObject, value:Brush): # -> 
        """ SetPressedBackground(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetPressedBorderBrush(element:DependencyObject, value:Brush): # -> 
        """ SetPressedBorderBrush(element: DependencyObject, value: Brush) """
        ...

    @staticmethod
    def SetQuickAccessToolBarControlSizeDefinition(element:DependencyObject, value:RibbonControlSizeDefinition): # -> 
        """ SetQuickAccessToolBarControlSizeDefinition(element: DependencyObject, value: RibbonControlSizeDefinition) """
        ...

    @staticmethod
    def SetQuickAccessToolBarId(element:DependencyObject, value:object): # -> 
        """ SetQuickAccessToolBarId(element: DependencyObject, value: object) """
        ...

    @staticmethod
    def SetSmallImageSource(element:DependencyObject, value): # ->  # Not found arg types: {'value': 'ImageSource'}
        """ SetSmallImageSource(element: DependencyObject, value: ImageSource) """
        ...

    @staticmethod
    def SetToolTipDescription(element:DependencyObject, value:str): # -> 
        """ SetToolTipDescription(element: DependencyObject, value: str) """
        ...

    @staticmethod
    def SetToolTipFooterDescription(element:DependencyObject, value:str): # -> 
        """ SetToolTipFooterDescription(element: DependencyObject, value: str) """
        ...

    @staticmethod
    def SetToolTipFooterImageSource(element:DependencyObject, value): # ->  # Not found arg types: {'value': 'ImageSource'}
        """ SetToolTipFooterImageSource(element: DependencyObject, value: ImageSource) """
        ...

    @staticmethod
    def SetToolTipFooterTitle(element:DependencyObject, value:str): # -> 
        """ SetToolTipFooterTitle(element: DependencyObject, value: str) """
        ...

    @staticmethod
    def SetToolTipImageSource(element:DependencyObject, value): # ->  # Not found arg types: {'value': 'ImageSource'}
        """ SetToolTipImageSource(element: DependencyObject, value: ImageSource) """
        ...

    @staticmethod
    def SetToolTipTitle(element:DependencyObject, value:str): # -> 
        """ SetToolTipTitle(element: DependencyObject, value: str) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    CornerRadiusProperty: DependencyProperty = ...
    DefaultControlSizeDefinitionProperty: DependencyProperty = ...
    DismissPopupEvent = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...
    __all__: list = ...


class RibbonControlSizeDefinition(Freezable): # skipped bases: <type 'ISealable'>, <type 'object'>
    """ RibbonControlSizeDefinition() """
    @property
    def ImageSize(self) -> RibbonImageSize:
        """
        Get: ImageSize(self: RibbonControlSizeDefinition) -> RibbonImageSize
        Set: ImageSize(self: RibbonControlSizeDefinition) = value
        """
        ...

    @property
    def IsCollapsed(self) -> bool:
        """
        Get: IsCollapsed(self: RibbonControlSizeDefinition) -> bool
        Set: IsCollapsed(self: RibbonControlSizeDefinition) = value
        """
        ...

    @property
    def IsLabelVisible(self) -> bool:
        """
        Get: IsLabelVisible(self: RibbonControlSizeDefinition) -> bool
        Set: IsLabelVisible(self: RibbonControlSizeDefinition) = value
        """
        ...

    @property
    def MaxWidth(self) -> RibbonControlLength:
        """
        Get: MaxWidth(self: RibbonControlSizeDefinition) -> RibbonControlLength
        Set: MaxWidth(self: RibbonControlSizeDefinition) = value
        """
        ...

    @property
    def MinWidth(self) -> RibbonControlLength:
        """
        Get: MinWidth(self: RibbonControlSizeDefinition) -> RibbonControlLength
        Set: MinWidth(self: RibbonControlSizeDefinition) = value
        """
        ...

    @property
    def Width(self) -> RibbonControlLength:
        """
        Get: Width(self: RibbonControlSizeDefinition) -> RibbonControlLength
        Set: Width(self: RibbonControlSizeDefinition) = value
        """
        ...


    ImageSizeProperty: DependencyProperty = ...
    IsCollapsedProperty: DependencyProperty = ...
    IsLabelVisibleProperty: DependencyProperty = ...
    MaxWidthProperty: DependencyProperty = ...
    MinWidthProperty: DependencyProperty = ...
    WidthProperty: DependencyProperty = ...


class RibbonControlSizeDefinitionCollection(FreezableCollection): # skipped bases: <type 'IList[RibbonControlSizeDefinition]'>, <type 'IAnimatable'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IResource'>, <type 'INotifyCollectionChanged'>, <type 'ISealable'>, <type 'IEnumerable[RibbonControlSizeDefinition]'>, <type 'INotifyPropertyChanged'>, <type 'ICollection[RibbonControlSizeDefinition]'>, <type 'ICollection'>, <type 'object'>
    """ RibbonControlSizeDefinitionCollection() """
    pass

class RibbonDismissPopupEventArgs(RoutedEventArgs): # skipped bases: <type 'object'>
    """
    RibbonDismissPopupEventArgs()
    RibbonDismissPopupEventArgs(dismissMode: RibbonDismissPopupMode)
    """
    @property
    def DismissMode(self) -> RibbonDismissPopupMode:
        """ Get: DismissMode(self: RibbonDismissPopupEventArgs) -> RibbonDismissPopupMode """
        ...



class RibbonDismissPopupEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RibbonDismissPopupEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RibbonDismissPopupEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RibbonDismissPopupEventHandler, sender: object, e: RibbonDismissPopupEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RibbonDismissPopupEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RibbonDismissPopupEventArgs): # -> 
        """ Invoke(self: RibbonDismissPopupEventHandler, sender: object, e: RibbonDismissPopupEventArgs) """
        ...


class RibbonDismissPopupMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RibbonDismissPopupMode, values: Always (0), MousePhysicallyNotOver (1) """
    Always: RibbonDismissPopupMode = ...
    MousePhysicallyNotOver: RibbonDismissPopupMode = ...
    value__ = ...


class RibbonFilterMenuButton(RibbonMenuButton): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonFilterMenuButton() """
    pass

class RibbonGallery(ItemsControl, IPreviewCommandSource, IWeakEventListener): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ICommandSource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonGallery() """
    @property
    def AllFilterItem(self) -> object:
        """ Get: AllFilterItem() -> object """
        ...

    @property
    def AllFilterItemContainerStyle(self) -> Style:
        """
        Get: AllFilterItemContainerStyle(self: RibbonGallery) -> Style
        Set: AllFilterItemContainerStyle(self: RibbonGallery) = value
        """
        ...

    @property
    def AllFilterItemTemplate(self): # -> DataTemplate
        """
        Get: AllFilterItemTemplate(self: RibbonGallery) -> DataTemplate
        Set: AllFilterItemTemplate(self: RibbonGallery) = value
        """
        ...

    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonGallery) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonGallery) = value
        """
        ...

    @property
    def CanUserFilter(self) -> bool:
        """
        Get: CanUserFilter(self: RibbonGallery) -> bool
        Set: CanUserFilter(self: RibbonGallery) = value
        """
        ...

    @property
    def CategoryStyle(self) -> Style:
        """
        Get: CategoryStyle(self: RibbonGallery) -> Style
        Set: CategoryStyle(self: RibbonGallery) = value
        """
        ...

    @property
    def CategoryTemplate(self): # -> DataTemplate
        """
        Get: CategoryTemplate(self: RibbonGallery) -> DataTemplate
        Set: CategoryTemplate(self: RibbonGallery) = value
        """
        ...

    @property
    def ColumnsStretchToFill(self) -> bool:
        """
        Get: ColumnsStretchToFill(self: RibbonGallery) -> bool
        Set: ColumnsStretchToFill(self: RibbonGallery) = value
        """
        ...

    @property
    def Command(self) -> ICommand:
        """
        Get: Command(self: RibbonGallery) -> ICommand
        Set: Command(self: RibbonGallery) = value
        """
        ...

    @property
    def CommandParameter(self) -> object:
        """
        Get: CommandParameter(self: RibbonGallery) -> object
        Set: CommandParameter(self: RibbonGallery) = value
        """
        ...

    @property
    def CommandTarget(self): # -> IInputElement
        """
        Get: CommandTarget(self: RibbonGallery) -> IInputElement
        Set: CommandTarget(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterCommand(self): # -> RoutedCommand
        """ Get: FilterCommand() -> RoutedCommand """
        ...

    @property
    def FilterItemContainerStyle(self) -> Style:
        """
        Get: FilterItemContainerStyle(self: RibbonGallery) -> Style
        Set: FilterItemContainerStyle(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterItemContainerStyleSelector(self): # -> StyleSelector
        """
        Get: FilterItemContainerStyleSelector(self: RibbonGallery) -> StyleSelector
        Set: FilterItemContainerStyleSelector(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterItemTemplate(self): # -> DataTemplate
        """
        Get: FilterItemTemplate(self: RibbonGallery) -> DataTemplate
        Set: FilterItemTemplate(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterItemTemplateSelector(self): # -> DataTemplateSelector
        """
        Get: FilterItemTemplateSelector(self: RibbonGallery) -> DataTemplateSelector
        Set: FilterItemTemplateSelector(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterMenuButtonStyle(self) -> Style:
        """
        Get: FilterMenuButtonStyle(self: RibbonGallery) -> Style
        Set: FilterMenuButtonStyle(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterPaneContent(self) -> object:
        """
        Get: FilterPaneContent(self: RibbonGallery) -> object
        Set: FilterPaneContent(self: RibbonGallery) = value
        """
        ...

    @property
    def FilterPaneContentTemplate(self): # -> DataTemplate
        """
        Get: FilterPaneContentTemplate(self: RibbonGallery) -> DataTemplate
        Set: FilterPaneContentTemplate(self: RibbonGallery) = value
        """
        ...

    @property
    def GalleryItemStyle(self) -> Style:
        """
        Get: GalleryItemStyle(self: RibbonGallery) -> Style
        Set: GalleryItemStyle(self: RibbonGallery) = value
        """
        ...

    @property
    def GalleryItemTemplate(self): # -> DataTemplate
        """
        Get: GalleryItemTemplate(self: RibbonGallery) -> DataTemplate
        Set: GalleryItemTemplate(self: RibbonGallery) = value
        """
        ...

    @property
    def HighlightedItem(self) -> object:
        """ Get: HighlightedItem(self: RibbonGallery) -> object """
        ...

    @property
    def IsSharedColumnSizeScope(self) -> bool:
        """
        Get: IsSharedColumnSizeScope(self: RibbonGallery) -> bool
        Set: IsSharedColumnSizeScope(self: RibbonGallery) = value
        """
        ...

    @property
    def IsSynchronizedWithCurrentItem(self) -> Nullable:
        """
        Get: IsSynchronizedWithCurrentItem(self: RibbonGallery) -> Nullable[bool]
        Set: IsSynchronizedWithCurrentItem(self: RibbonGallery) = value
        """
        ...

    @property
    def MaxColumnCount(self) -> int:
        """
        Get: MaxColumnCount(self: RibbonGallery) -> int
        Set: MaxColumnCount(self: RibbonGallery) = value
        """
        ...

    @property
    def MinColumnCount(self) -> int:
        """
        Get: MinColumnCount(self: RibbonGallery) -> int
        Set: MinColumnCount(self: RibbonGallery) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonGallery) -> object
        Set: QuickAccessToolBarId(self: RibbonGallery) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonGallery) -> Ribbon """
        ...

    @property
    def SelectedItem(self) -> object:
        """
        Get: SelectedItem(self: RibbonGallery) -> object
        Set: SelectedItem(self: RibbonGallery) = value
        """
        ...

    @property
    def SelectedValue(self) -> object:
        """
        Get: SelectedValue(self: RibbonGallery) -> object
        Set: SelectedValue(self: RibbonGallery) = value
        """
        ...

    @property
    def SelectedValuePath(self) -> str:
        """
        Get: SelectedValuePath(self: RibbonGallery) -> str
        Set: SelectedValuePath(self: RibbonGallery) = value
        """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonGallery) -> ImageSource
        Set: SmallImageSource(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonGallery) -> str
        Set: ToolTipDescription(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonGallery) -> str
        Set: ToolTipFooterDescription(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonGallery) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonGallery) -> str
        Set: ToolTipFooterTitle(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonGallery) -> ImageSource
        Set: ToolTipImageSource(self: RibbonGallery) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonGallery) -> str
        Set: ToolTipTitle(self: RibbonGallery) = value
        """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonGallery) """
        ...

    def OnHighlightedItemChanged(self, *args): #cannot find CLR method
        """ OnHighlightedItemChanged(self: RibbonGallery, e: DependencyPropertyChangedEventArgs) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: RibbonGallery, e: RoutedPropertyChangedEventArgs[object]) """
        ...

    def ScrollIntoView(self, item:object): # -> 
        """ ScrollIntoView(self: RibbonGallery, item: object) """
        ...

    AllFilterItemContainerStyleProperty: DependencyProperty = ...
    AllFilterItemTemplateProperty: DependencyProperty = ...
    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CanUserFilterProperty: DependencyProperty = ...
    CategoryStyleProperty: DependencyProperty = ...
    CategoryTemplateProperty: DependencyProperty = ...
    ColumnsStretchToFillProperty: DependencyProperty = ...
    CommandParameterProperty: DependencyProperty = ...
    CommandProperty: DependencyProperty = ...
    CommandTargetProperty: DependencyProperty = ...
    FilterItemContainerStyleProperty: DependencyProperty = ...
    FilterItemContainerStyleSelectorProperty: DependencyProperty = ...
    FilterItemTemplateProperty: DependencyProperty = ...
    FilterItemTemplateSelectorProperty: DependencyProperty = ...
    FilterMenuButtonStyleProperty: DependencyProperty = ...
    FilterPaneContentProperty: DependencyProperty = ...
    FilterPaneContentTemplateProperty: DependencyProperty = ...
    GalleryItemStyleProperty: DependencyProperty = ...
    GalleryItemTemplateProperty: DependencyProperty = ...
    HighlightedItemProperty: DependencyProperty = ...
    IsSharedColumnSizeScopeProperty: DependencyProperty = ...
    IsSynchronizedWithCurrentItemProperty: DependencyProperty = ...
    MaxColumnCountProperty: DependencyProperty = ...
    MinColumnCountProperty: DependencyProperty = ...
    PreviewCommandParameterProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    SelectedItemProperty: DependencyProperty = ...
    SelectedValuePathProperty: DependencyProperty = ...
    SelectedValueProperty: DependencyProperty = ...
    SelectionChanged = ...
    SelectionChangedEvent = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonGalleryCategory(IWeakEventListener, HeaderedItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonGalleryCategory() """
    @property
    def ColumnsStretchToFill(self) -> bool:
        """
        Get: ColumnsStretchToFill(self: RibbonGalleryCategory) -> bool
        Set: ColumnsStretchToFill(self: RibbonGalleryCategory) = value
        """
        ...

    @property
    def HeaderVisibility(self): # -> Visibility
        """
        Get: HeaderVisibility(self: RibbonGalleryCategory) -> Visibility
        Set: HeaderVisibility(self: RibbonGalleryCategory) = value
        """
        ...

    @property
    def IsSharedColumnSizeScope(self) -> bool:
        """
        Get: IsSharedColumnSizeScope(self: RibbonGalleryCategory) -> bool
        Set: IsSharedColumnSizeScope(self: RibbonGalleryCategory) = value
        """
        ...

    @property
    def MaxColumnCount(self) -> int:
        """
        Get: MaxColumnCount(self: RibbonGalleryCategory) -> int
        Set: MaxColumnCount(self: RibbonGalleryCategory) = value
        """
        ...

    @property
    def MinColumnCount(self) -> int:
        """
        Get: MinColumnCount(self: RibbonGalleryCategory) -> int
        Set: MinColumnCount(self: RibbonGalleryCategory) = value
        """
        ...


    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonGalleryCategory) """
        ...

    ColumnsStretchToFillProperty: DependencyProperty = ...
    HeaderVisibilityProperty: DependencyProperty = ...
    IsSharedColumnSizeScopeProperty: DependencyProperty = ...
    MaxColumnCountProperty: DependencyProperty = ...
    MinColumnCountProperty: DependencyProperty = ...


class RibbonGalleryItem(ContentControl, ISyncKeyTipAndContent): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonGalleryItem() """
    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonGalleryItem) -> Brush
        Set: CheckedBackground(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonGalleryItem) -> Brush
        Set: CheckedBorderBrush(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def IsHighlighted(self) -> bool:
        """ Get: IsHighlighted(self: RibbonGalleryItem) -> bool """
        ...

    @property
    def IsPressed(self) -> bool:
        """ Get: IsPressed(self: RibbonGalleryItem) -> bool """
        ...

    @property
    def IsSelected(self) -> bool:
        """
        Get: IsSelected(self: RibbonGalleryItem) -> bool
        Set: IsSelected(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonGalleryItem) -> str
        Set: KeyTip(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonGalleryItem) -> Brush
        Set: MouseOverBackground(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonGalleryItem) -> Brush
        Set: MouseOverBorderBrush(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonGalleryItem) -> Brush
        Set: PressedBackground(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonGalleryItem) -> Brush
        Set: PressedBorderBrush(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonGalleryItem) -> Ribbon """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonGalleryItem) -> str
        Set: ToolTipDescription(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonGalleryItem) -> str
        Set: ToolTipFooterDescription(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonGalleryItem) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonGalleryItem) -> str
        Set: ToolTipFooterTitle(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonGalleryItem) -> ImageSource
        Set: ToolTipImageSource(self: RibbonGalleryItem) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonGalleryItem) -> str
        Set: ToolTipTitle(self: RibbonGalleryItem) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonGalleryItem, e: ActivatingKeyTipEventArgs) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonGalleryItem, e: KeyTipAccessedEventArgs) """
        ...

    def OnSelected(self, *args): #cannot find CLR method
        """ OnSelected(self: RibbonGalleryItem, e: RoutedEventArgs) """
        ...

    def OnUnselected(self, *args): #cannot find CLR method
        """ OnUnselected(self: RibbonGalleryItem, e: RoutedEventArgs) """
        ...

    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    IsHighlightedProperty: DependencyProperty = ...
    IsPressedProperty: DependencyProperty = ...
    IsSelectedProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    Selected = ...
    SelectedEvent = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...
    Unselected = ...
    UnselectedEvent = ...


class RibbonGroup(HeaderedItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonGroup() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonGroup) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonGroup) = value
        """
        ...

    @property
    def GroupSizeDefinitions(self) -> RibbonGroupSizeDefinitionBaseCollection:
        """
        Get: GroupSizeDefinitions(self: RibbonGroup) -> RibbonGroupSizeDefinitionBaseCollection
        Set: GroupSizeDefinitions(self: RibbonGroup) = value
        """
        ...

    @property
    def IsCollapsed(self) -> bool:
        """ Get: IsCollapsed(self: RibbonGroup) -> bool """
        ...

    @property
    def IsDropDownOpen(self) -> bool:
        """
        Get: IsDropDownOpen(self: RibbonGroup) -> bool
        Set: IsDropDownOpen(self: RibbonGroup) = value
        """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonGroup) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonGroup) -> str
        Set: KeyTip(self: RibbonGroup) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonGroup) -> ImageSource
        Set: LargeImageSource(self: RibbonGroup) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonGroup) -> Brush
        Set: MouseOverBackground(self: RibbonGroup) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonGroup) -> Brush
        Set: MouseOverBorderBrush(self: RibbonGroup) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonGroup) -> object
        Set: QuickAccessToolBarId(self: RibbonGroup) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonGroup) -> Ribbon """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonGroup) -> ImageSource
        Set: SmallImageSource(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonGroup) -> str
        Set: ToolTipDescription(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonGroup) -> str
        Set: ToolTipFooterDescription(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonGroup) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonGroup) -> str
        Set: ToolTipFooterTitle(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonGroup) -> ImageSource
        Set: ToolTipImageSource(self: RibbonGroup) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonGroup) -> str
        Set: ToolTipTitle(self: RibbonGroup) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonGroup, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonGroup) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonGroup, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    GroupSizeDefinitionsProperty: DependencyProperty = ...
    IsCollapsedProperty: DependencyProperty = ...
    IsDropDownOpenProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonGroupSizeDefinitionBase(Freezable): # skipped bases: <type 'ISealable'>, <type 'object'>
    """ no doc """
    @property
    def IsCollapsed(self) -> bool:
        """
        Get: IsCollapsed(self: RibbonGroupSizeDefinitionBase) -> bool
        Set: IsCollapsed(self: RibbonGroupSizeDefinitionBase) = value
        """
        ...


    IsCollapsedProperty: DependencyProperty = ...


class RibbonGroupSizeDefinition(RibbonGroupSizeDefinitionBase): # skipped bases: <type 'ISealable'>, <type 'object'>
    """ RibbonGroupSizeDefinition() """
    @property
    def ControlSizeDefinitions(self) -> RibbonControlSizeDefinitionCollection:
        """
        Get: ControlSizeDefinitions(self: RibbonGroupSizeDefinition) -> RibbonControlSizeDefinitionCollection
        Set: ControlSizeDefinitions(self: RibbonGroupSizeDefinition) = value
        """
        ...


    ControlSizeDefinitionsProperty: DependencyProperty = ...


class RibbonGroupSizeDefinitionBaseCollection(FreezableCollection): # skipped bases: <type 'IList[RibbonGroupSizeDefinitionBase]'>, <type 'IAnimatable'>, <type 'ICollection[RibbonGroupSizeDefinitionBase]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IResource'>, <type 'INotifyCollectionChanged'>, <type 'ISealable'>, <type 'IEnumerable[RibbonGroupSizeDefinitionBase]'>, <type 'INotifyPropertyChanged'>, <type 'ICollection'>, <type 'object'>
    """ RibbonGroupSizeDefinitionBaseCollection() """
    pass

class RibbonGroupTemplateSizeDefinition(RibbonGroupSizeDefinitionBase): # skipped bases: <type 'ISealable'>, <type 'object'>
    """ RibbonGroupTemplateSizeDefinition() """
    @property
    def ContentTemplate(self): # -> DataTemplate
        """
        Get: ContentTemplate(self: RibbonGroupTemplateSizeDefinition) -> DataTemplate
        Set: ContentTemplate(self: RibbonGroupTemplateSizeDefinition) = value
        """
        ...


    ContentTemplateProperty: DependencyProperty = ...


class RibbonImageSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RibbonImageSize, values: Collapsed (0), Large (2), Small (1) """
    Collapsed: RibbonImageSize = ...
    Large: RibbonImageSize = ...
    Small: RibbonImageSize = ...
    value__ = ...


class RibbonQuickAccessToolBar(ItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonQuickAccessToolBar() """
    @property
    def CustomizeMenuButton(self) -> RibbonMenuButton:
        """
        Get: CustomizeMenuButton(self: RibbonQuickAccessToolBar) -> RibbonMenuButton
        Set: CustomizeMenuButton(self: RibbonQuickAccessToolBar) = value
        """
        ...

    @property
    def HasOverflowItems(self) -> bool:
        """ Get: HasOverflowItems(self: RibbonQuickAccessToolBar) -> bool """
        ...

    @property
    def IsOverflowOpen(self) -> bool:
        """
        Get: IsOverflowOpen(self: RibbonQuickAccessToolBar) -> bool
        Set: IsOverflowOpen(self: RibbonQuickAccessToolBar) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonQuickAccessToolBar) -> Ribbon """
        ...


    @staticmethod
    def AddCloneHandler(element:DependencyObject, handler:RibbonQuickAccessToolBarCloneEventHandler): # -> 
        """ AddCloneHandler(element: DependencyObject, handler: RibbonQuickAccessToolBarCloneEventHandler) """
        ...

    @staticmethod
    def GetIsOverflowItem(element:DependencyObject) -> bool:
        """ GetIsOverflowItem(element: DependencyObject) -> bool """
        ...

    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonQuickAccessToolBar, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonQuickAccessToolBar) """
        ...

    def OnPreviewKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnPreviewKeyTipAccessed(self: RibbonQuickAccessToolBar, e: KeyTipAccessedEventArgs) """
        ...

    @staticmethod
    def RemoveCloneHandler(element:DependencyObject, handler:RibbonQuickAccessToolBarCloneEventHandler): # -> 
        """ RemoveCloneHandler(element: DependencyObject, handler: RibbonQuickAccessToolBarCloneEventHandler) """
        ...

    CloneEvent = ...
    CustomizeMenuButtonProperty: DependencyProperty = ...
    HasOverflowItemsProperty: DependencyProperty = ...
    IsOverflowItemProperty: DependencyProperty = ...
    IsOverflowOpenProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...


class RibbonQuickAccessToolBarCloneEventArgs(RoutedEventArgs): # skipped bases: <type 'object'>
    """ RibbonQuickAccessToolBarCloneEventArgs(targetElement: UIElement) """
    @property
    def CloneInstance(self): # -> UIElement
        """
        Get: CloneInstance(self: RibbonQuickAccessToolBarCloneEventArgs) -> UIElement
        Set: CloneInstance(self: RibbonQuickAccessToolBarCloneEventArgs) = value
        """
        ...

    @property
    def InstanceToBeCloned(self): # -> UIElement
        """ Get: InstanceToBeCloned(self: RibbonQuickAccessToolBarCloneEventArgs) -> UIElement """
        ...



class RibbonQuickAccessToolBarCloneEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RibbonQuickAccessToolBarCloneEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RibbonQuickAccessToolBarCloneEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RibbonQuickAccessToolBarCloneEventHandler, sender: object, e: RibbonQuickAccessToolBarCloneEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RibbonQuickAccessToolBarCloneEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RibbonQuickAccessToolBarCloneEventArgs): # -> 
        """ Invoke(self: RibbonQuickAccessToolBarCloneEventHandler, sender: object, e: RibbonQuickAccessToolBarCloneEventArgs) """
        ...


class RibbonRadioButton(RadioButton): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'ICommandSource'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonRadioButton() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonRadioButton) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonRadioButton) = value
        """
        ...

    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonRadioButton) -> Brush
        Set: CheckedBackground(self: RibbonRadioButton) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonRadioButton) -> Brush
        Set: CheckedBorderBrush(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonRadioButton) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonRadioButton) = value
        """
        ...

    @property
    def CornerRadius(self) -> CornerRadius:
        """
        Get: CornerRadius(self: RibbonRadioButton) -> CornerRadius
        Set: CornerRadius(self: RibbonRadioButton) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonRadioButton) -> Brush
        Set: FocusedBackground(self: RibbonRadioButton) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonRadioButton) -> Brush
        Set: FocusedBorderBrush(self: RibbonRadioButton) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonRadioButton) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonRadioButton) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonRadioButton) -> str
        Set: KeyTip(self: RibbonRadioButton) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonRadioButton) -> str
        Set: Label(self: RibbonRadioButton) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonRadioButton) -> ImageSource
        Set: LargeImageSource(self: RibbonRadioButton) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonRadioButton) -> Brush
        Set: MouseOverBackground(self: RibbonRadioButton) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonRadioButton) -> Brush
        Set: MouseOverBorderBrush(self: RibbonRadioButton) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonRadioButton) -> Brush
        Set: PressedBackground(self: RibbonRadioButton) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonRadioButton) -> Brush
        Set: PressedBorderBrush(self: RibbonRadioButton) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonRadioButton) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonRadioButton) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonRadioButton) -> object
        Set: QuickAccessToolBarId(self: RibbonRadioButton) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonRadioButton) -> Ribbon """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonRadioButton) -> bool """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonRadioButton) -> ImageSource
        Set: SmallImageSource(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonRadioButton) -> str
        Set: ToolTipDescription(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonRadioButton) -> str
        Set: ToolTipFooterDescription(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonRadioButton) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonRadioButton) -> str
        Set: ToolTipFooterTitle(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonRadioButton) -> ImageSource
        Set: ToolTipImageSource(self: RibbonRadioButton) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonRadioButton) -> str
        Set: ToolTipTitle(self: RibbonRadioButton) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonRadioButton, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonRadioButton) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonRadioButton, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    CornerRadiusProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonSeparator(Separator): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonSeparator() """
    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonSeparator) -> str
        Set: Label(self: RibbonSeparator) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonSeparator) -> Ribbon """
        ...


    LabelProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...


class RibbonSplitButton(RibbonMenuButton, ICommandSource): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonSplitButton() """
    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonSplitButton) -> Brush
        Set: CheckedBackground(self: RibbonSplitButton) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonSplitButton) -> Brush
        Set: CheckedBorderBrush(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipDescription(self) -> str:
        """
        Get: DropDownToolTipDescription(self: RibbonSplitButton) -> str
        Set: DropDownToolTipDescription(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipFooterDescription(self) -> str:
        """
        Get: DropDownToolTipFooterDescription(self: RibbonSplitButton) -> str
        Set: DropDownToolTipFooterDescription(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: DropDownToolTipFooterImageSource(self: RibbonSplitButton) -> ImageSource
        Set: DropDownToolTipFooterImageSource(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipFooterTitle(self) -> str:
        """
        Get: DropDownToolTipFooterTitle(self: RibbonSplitButton) -> str
        Set: DropDownToolTipFooterTitle(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipImageSource(self): # -> ImageSource
        """
        Get: DropDownToolTipImageSource(self: RibbonSplitButton) -> ImageSource
        Set: DropDownToolTipImageSource(self: RibbonSplitButton) = value
        """
        ...

    @property
    def DropDownToolTipTitle(self) -> str:
        """
        Get: DropDownToolTipTitle(self: RibbonSplitButton) -> str
        Set: DropDownToolTipTitle(self: RibbonSplitButton) = value
        """
        ...

    @property
    def HeaderKeyTip(self) -> str:
        """
        Get: HeaderKeyTip(self: RibbonSplitButton) -> str
        Set: HeaderKeyTip(self: RibbonSplitButton) = value
        """
        ...

    @property
    def HeaderQuickAccessToolBarId(self) -> object:
        """
        Get: HeaderQuickAccessToolBarId(self: RibbonSplitButton) -> object
        Set: HeaderQuickAccessToolBarId(self: RibbonSplitButton) = value
        """
        ...

    @property
    def IsCheckable(self) -> bool:
        """
        Get: IsCheckable(self: RibbonSplitButton) -> bool
        Set: IsCheckable(self: RibbonSplitButton) = value
        """
        ...

    @property
    def IsChecked(self) -> bool:
        """
        Get: IsChecked(self: RibbonSplitButton) -> bool
        Set: IsChecked(self: RibbonSplitButton) = value
        """
        ...

    @property
    def LabelPosition(self) -> RibbonSplitButtonLabelPosition:
        """
        Get: LabelPosition(self: RibbonSplitButton) -> RibbonSplitButtonLabelPosition
        Set: LabelPosition(self: RibbonSplitButton) = value
        """
        ...


    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    Click = ...
    ClickEvent = ...
    CommandParameterProperty: DependencyProperty = ...
    CommandProperty: DependencyProperty = ...
    CommandTargetProperty: DependencyProperty = ...
    DropDownToolTipDescriptionProperty: DependencyProperty = ...
    DropDownToolTipFooterDescriptionProperty: DependencyProperty = ...
    DropDownToolTipFooterImageSourceProperty: DependencyProperty = ...
    DropDownToolTipFooterTitleProperty: DependencyProperty = ...
    DropDownToolTipImageSourceProperty: DependencyProperty = ...
    DropDownToolTipTitleProperty: DependencyProperty = ...
    HeaderKeyTipProperty: DependencyProperty = ...
    HeaderQuickAccessToolBarIdProperty: DependencyProperty = ...
    IsCheckableProperty: DependencyProperty = ...
    IsCheckedProperty: DependencyProperty = ...
    LabelPositionProperty: DependencyProperty = ...


class RibbonSplitButtonLabelPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RibbonSplitButtonLabelPosition, values: DropDown (1), Header (0) """
    DropDown: RibbonSplitButtonLabelPosition = ...
    Header: RibbonSplitButtonLabelPosition = ...
    value__ = ...


class RibbonTab(HeaderedItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonTab() """
    @property
    def ContextualTabGroup(self) -> RibbonContextualTabGroup:
        """ Get: ContextualTabGroup(self: RibbonTab) -> RibbonContextualTabGroup """
        ...

    @property
    def ContextualTabGroupHeader(self) -> object:
        """
        Get: ContextualTabGroupHeader(self: RibbonTab) -> object
        Set: ContextualTabGroupHeader(self: RibbonTab) = value
        """
        ...

    @property
    def GroupSizeReductionOrder(self) -> StringCollection:
        """
        Get: GroupSizeReductionOrder(self: RibbonTab) -> StringCollection
        Set: GroupSizeReductionOrder(self: RibbonTab) = value
        """
        ...

    @property
    def HeaderStyle(self) -> Style:
        """
        Get: HeaderStyle(self: RibbonTab) -> Style
        Set: HeaderStyle(self: RibbonTab) = value
        """
        ...

    @property
    def IsSelected(self) -> bool:
        """
        Get: IsSelected(self: RibbonTab) -> bool
        Set: IsSelected(self: RibbonTab) = value
        """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonTab) -> str
        Set: KeyTip(self: RibbonTab) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonTab) -> Ribbon """
        ...

    @property
    def TabHeaderLeft(self) -> float:
        """ Get: TabHeaderLeft(self: RibbonTab) -> float """
        ...

    @property
    def TabHeaderRight(self) -> float:
        """ Get: TabHeaderRight(self: RibbonTab) -> float """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonTab, e: ActivatingKeyTipEventArgs) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonTab, e: KeyTipAccessedEventArgs) """
        ...

    def OnSelected(self, *args): #cannot find CLR method
        """ OnSelected(self: RibbonTab, e: RoutedEventArgs) """
        ...

    def OnUnselected(self, *args): #cannot find CLR method
        """ OnUnselected(self: RibbonTab, e: RoutedEventArgs) """
        ...

    ContextualTabGroupHeaderProperty: DependencyProperty = ...
    ContextualTabGroupProperty: DependencyProperty = ...
    GroupSizeReductionOrderProperty: DependencyProperty = ...
    HeaderStyleProperty: DependencyProperty = ...
    IsSelectedProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    TabHeaderLeftProperty: DependencyProperty = ...
    TabHeaderRightProperty: DependencyProperty = ...


class RibbonTabHeader(ContentControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTabHeader() """
    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonTabHeader) -> Brush
        Set: CheckedBackground(self: RibbonTabHeader) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonTabHeader) -> Brush
        Set: CheckedBorderBrush(self: RibbonTabHeader) = value
        """
        ...

    @property
    def ContextualTabGroup(self) -> RibbonContextualTabGroup:
        """ Get: ContextualTabGroup(self: RibbonTabHeader) -> RibbonContextualTabGroup """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonTabHeader) -> Brush
        Set: FocusedBackground(self: RibbonTabHeader) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonTabHeader) -> Brush
        Set: FocusedBorderBrush(self: RibbonTabHeader) = value
        """
        ...

    @property
    def IsContextualTab(self) -> bool:
        """ Get: IsContextualTab(self: RibbonTabHeader) -> bool """
        ...

    @property
    def IsRibbonTabSelected(self) -> bool:
        """ Get: IsRibbonTabSelected(self: RibbonTabHeader) -> bool """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonTabHeader) -> Brush
        Set: MouseOverBackground(self: RibbonTabHeader) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonTabHeader) -> Brush
        Set: MouseOverBorderBrush(self: RibbonTabHeader) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonTabHeader) -> Ribbon """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonTabHeader, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonTabHeader) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonTabHeader, e: KeyTipAccessedEventArgs) """
        ...

    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    ContextualTabGroupProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsContextualTabProperty: DependencyProperty = ...
    IsRibbonTabSelectedProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...


class RibbonTabHeaderItemsControl(ItemsControl): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IGeneratorHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IContainItemStorage'>, <type 'object'>
    """ RibbonTabHeaderItemsControl() """
    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonTabHeaderItemsControl) """
        ...


class RibbonTextBox(TextBox, ICommandSource): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'ITextBoxViewHost'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTextBox() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonTextBox) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonTextBox) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonTextBox) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonTextBox) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonTextBox) -> Brush
        Set: FocusedBackground(self: RibbonTextBox) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonTextBox) -> Brush
        Set: FocusedBorderBrush(self: RibbonTextBox) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonTextBox) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonTextBox) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonTextBox) -> str
        Set: KeyTip(self: RibbonTextBox) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonTextBox) -> str
        Set: Label(self: RibbonTextBox) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonTextBox) -> ImageSource
        Set: LargeImageSource(self: RibbonTextBox) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonTextBox) -> Brush
        Set: MouseOverBackground(self: RibbonTextBox) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonTextBox) -> Brush
        Set: MouseOverBorderBrush(self: RibbonTextBox) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonTextBox) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonTextBox) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonTextBox) -> object
        Set: QuickAccessToolBarId(self: RibbonTextBox) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonTextBox) -> Ribbon """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonTextBox) -> bool """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonTextBox) -> ImageSource
        Set: SmallImageSource(self: RibbonTextBox) = value
        """
        ...

    @property
    def TextBoxWidth(self) -> float:
        """
        Get: TextBoxWidth(self: RibbonTextBox) -> float
        Set: TextBoxWidth(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonTextBox) -> str
        Set: ToolTipDescription(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonTextBox) -> str
        Set: ToolTipFooterDescription(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonTextBox) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonTextBox) -> str
        Set: ToolTipFooterTitle(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonTextBox) -> ImageSource
        Set: ToolTipImageSource(self: RibbonTextBox) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonTextBox) -> str
        Set: ToolTipTitle(self: RibbonTextBox) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonTextBox, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonTextBox) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonTextBox, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CommandParameterProperty: DependencyProperty = ...
    CommandProperty: DependencyProperty = ...
    CommandTargetProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    TextBoxWidthProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonToggleButton(ToggleButton): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'ICommandSource'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonToggleButton() """
    @property
    def CanAddToQuickAccessToolBarDirectly(self) -> bool:
        """
        Get: CanAddToQuickAccessToolBarDirectly(self: RibbonToggleButton) -> bool
        Set: CanAddToQuickAccessToolBarDirectly(self: RibbonToggleButton) = value
        """
        ...

    @property
    def CheckedBackground(self) -> Brush:
        """
        Get: CheckedBackground(self: RibbonToggleButton) -> Brush
        Set: CheckedBackground(self: RibbonToggleButton) = value
        """
        ...

    @property
    def CheckedBorderBrush(self) -> Brush:
        """
        Get: CheckedBorderBrush(self: RibbonToggleButton) -> Brush
        Set: CheckedBorderBrush(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: ControlSizeDefinition(self: RibbonToggleButton) -> RibbonControlSizeDefinition
        Set: ControlSizeDefinition(self: RibbonToggleButton) = value
        """
        ...

    @property
    def CornerRadius(self) -> CornerRadius:
        """
        Get: CornerRadius(self: RibbonToggleButton) -> CornerRadius
        Set: CornerRadius(self: RibbonToggleButton) = value
        """
        ...

    @property
    def FocusedBackground(self) -> Brush:
        """
        Get: FocusedBackground(self: RibbonToggleButton) -> Brush
        Set: FocusedBackground(self: RibbonToggleButton) = value
        """
        ...

    @property
    def FocusedBorderBrush(self) -> Brush:
        """
        Get: FocusedBorderBrush(self: RibbonToggleButton) -> Brush
        Set: FocusedBorderBrush(self: RibbonToggleButton) = value
        """
        ...

    @property
    def IsInControlGroup(self) -> bool:
        """ Get: IsInControlGroup(self: RibbonToggleButton) -> bool """
        ...

    @property
    def IsInQuickAccessToolBar(self) -> bool:
        """ Get: IsInQuickAccessToolBar(self: RibbonToggleButton) -> bool """
        ...

    @property
    def KeyTip(self) -> str:
        """
        Get: KeyTip(self: RibbonToggleButton) -> str
        Set: KeyTip(self: RibbonToggleButton) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: RibbonToggleButton) -> str
        Set: Label(self: RibbonToggleButton) = value
        """
        ...

    @property
    def LargeImageSource(self): # -> ImageSource
        """
        Get: LargeImageSource(self: RibbonToggleButton) -> ImageSource
        Set: LargeImageSource(self: RibbonToggleButton) = value
        """
        ...

    @property
    def MouseOverBackground(self) -> Brush:
        """
        Get: MouseOverBackground(self: RibbonToggleButton) -> Brush
        Set: MouseOverBackground(self: RibbonToggleButton) = value
        """
        ...

    @property
    def MouseOverBorderBrush(self) -> Brush:
        """
        Get: MouseOverBorderBrush(self: RibbonToggleButton) -> Brush
        Set: MouseOverBorderBrush(self: RibbonToggleButton) = value
        """
        ...

    @property
    def PressedBackground(self) -> Brush:
        """
        Get: PressedBackground(self: RibbonToggleButton) -> Brush
        Set: PressedBackground(self: RibbonToggleButton) = value
        """
        ...

    @property
    def PressedBorderBrush(self) -> Brush:
        """
        Get: PressedBorderBrush(self: RibbonToggleButton) -> Brush
        Set: PressedBorderBrush(self: RibbonToggleButton) = value
        """
        ...

    @property
    def QuickAccessToolBarControlSizeDefinition(self) -> RibbonControlSizeDefinition:
        """
        Get: QuickAccessToolBarControlSizeDefinition(self: RibbonToggleButton) -> RibbonControlSizeDefinition
        Set: QuickAccessToolBarControlSizeDefinition(self: RibbonToggleButton) = value
        """
        ...

    @property
    def QuickAccessToolBarId(self) -> object:
        """
        Get: QuickAccessToolBarId(self: RibbonToggleButton) -> object
        Set: QuickAccessToolBarId(self: RibbonToggleButton) = value
        """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonToggleButton) -> Ribbon """
        ...

    @property
    def ShowKeyboardCues(self) -> bool:
        """ Get: ShowKeyboardCues(self: RibbonToggleButton) -> bool """
        ...

    @property
    def SmallImageSource(self): # -> ImageSource
        """
        Get: SmallImageSource(self: RibbonToggleButton) -> ImageSource
        Set: SmallImageSource(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipDescription(self) -> str:
        """
        Get: ToolTipDescription(self: RibbonToggleButton) -> str
        Set: ToolTipDescription(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipFooterDescription(self) -> str:
        """
        Get: ToolTipFooterDescription(self: RibbonToggleButton) -> str
        Set: ToolTipFooterDescription(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipFooterImageSource(self): # -> ImageSource
        """
        Get: ToolTipFooterImageSource(self: RibbonToggleButton) -> ImageSource
        Set: ToolTipFooterImageSource(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipFooterTitle(self) -> str:
        """
        Get: ToolTipFooterTitle(self: RibbonToggleButton) -> str
        Set: ToolTipFooterTitle(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipImageSource(self): # -> ImageSource
        """
        Get: ToolTipImageSource(self: RibbonToggleButton) -> ImageSource
        Set: ToolTipImageSource(self: RibbonToggleButton) = value
        """
        ...

    @property
    def ToolTipTitle(self) -> str:
        """
        Get: ToolTipTitle(self: RibbonToggleButton) -> str
        Set: ToolTipTitle(self: RibbonToggleButton) = value
        """
        ...


    def OnActivatingKeyTip(self, *args): #cannot find CLR method
        """ OnActivatingKeyTip(self: RibbonToggleButton, e: ActivatingKeyTipEventArgs) """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonToggleButton) """
        ...

    def OnKeyTipAccessed(self, *args): #cannot find CLR method
        """ OnKeyTipAccessed(self: RibbonToggleButton, e: KeyTipAccessedEventArgs) """
        ...

    CanAddToQuickAccessToolBarDirectlyProperty: DependencyProperty = ...
    CheckedBackgroundProperty: DependencyProperty = ...
    CheckedBorderBrushProperty: DependencyProperty = ...
    ControlSizeDefinitionProperty: DependencyProperty = ...
    CornerRadiusProperty: DependencyProperty = ...
    FocusedBackgroundProperty: DependencyProperty = ...
    FocusedBorderBrushProperty: DependencyProperty = ...
    IsInControlGroupProperty: DependencyProperty = ...
    IsInQuickAccessToolBarProperty: DependencyProperty = ...
    KeyTipProperty: DependencyProperty = ...
    LabelProperty: DependencyProperty = ...
    LargeImageSourceProperty: DependencyProperty = ...
    MouseOverBackgroundProperty: DependencyProperty = ...
    MouseOverBorderBrushProperty: DependencyProperty = ...
    PressedBackgroundProperty: DependencyProperty = ...
    PressedBorderBrushProperty: DependencyProperty = ...
    QuickAccessToolBarControlSizeDefinitionProperty: DependencyProperty = ...
    QuickAccessToolBarIdProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    ShowKeyboardCuesProperty: DependencyProperty = ...
    SmallImageSourceProperty: DependencyProperty = ...
    ToolTipDescriptionProperty: DependencyProperty = ...
    ToolTipFooterDescriptionProperty: DependencyProperty = ...
    ToolTipFooterImageSourceProperty: DependencyProperty = ...
    ToolTipFooterTitleProperty: DependencyProperty = ...
    ToolTipImageSourceProperty: DependencyProperty = ...
    ToolTipTitleProperty: DependencyProperty = ...


class RibbonToolTip(ToolTip): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonToolTip() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: RibbonToolTip) -> str
        Set: Description(self: RibbonToolTip) = value
        """
        ...

    @property
    def FooterDescription(self) -> str:
        """
        Get: FooterDescription(self: RibbonToolTip) -> str
        Set: FooterDescription(self: RibbonToolTip) = value
        """
        ...

    @property
    def FooterImageSource(self): # -> ImageSource
        """
        Get: FooterImageSource(self: RibbonToolTip) -> ImageSource
        Set: FooterImageSource(self: RibbonToolTip) = value
        """
        ...

    @property
    def FooterTitle(self) -> str:
        """
        Get: FooterTitle(self: RibbonToolTip) -> str
        Set: FooterTitle(self: RibbonToolTip) = value
        """
        ...

    @property
    def HasFooter(self) -> bool:
        """ Get: HasFooter(self: RibbonToolTip) -> bool """
        ...

    @property
    def HasHeader(self) -> bool:
        """ Get: HasHeader(self: RibbonToolTip) -> bool """
        ...

    @property
    def ImageSource(self): # -> ImageSource
        """
        Get: ImageSource(self: RibbonToolTip) -> ImageSource
        Set: ImageSource(self: RibbonToolTip) = value
        """
        ...

    @property
    def IsPlacementTargetInRibbonGroup(self) -> bool:
        """ Get: IsPlacementTargetInRibbonGroup(self: RibbonToolTip) -> bool """
        ...

    @property
    def Ribbon(self) -> Ribbon:
        """ Get: Ribbon(self: RibbonToolTip) -> Ribbon """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: RibbonToolTip) -> str
        Set: Title(self: RibbonToolTip) = value
        """
        ...


    DescriptionProperty: DependencyProperty = ...
    FooterDescriptionProperty: DependencyProperty = ...
    FooterImageSourceProperty: DependencyProperty = ...
    FooterTitleProperty: DependencyProperty = ...
    HasFooterProperty: DependencyProperty = ...
    HasHeaderProperty: DependencyProperty = ...
    ImageSourceProperty: DependencyProperty = ...
    IsPlacementTargetInRibbonGroupProperty: DependencyProperty = ...
    RibbonProperty: DependencyProperty = ...
    TitleProperty: DependencyProperty = ...


class RibbonTwoLineText(Control): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ RibbonTwoLineText() """
    @property
    def BaselineOffset(self) -> float:
        """
        Get: BaselineOffset(self: RibbonTwoLineText) -> float
        Set: BaselineOffset(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def LineHeight(self) -> float:
        """
        Get: LineHeight(self: RibbonTwoLineText) -> float
        Set: LineHeight(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def LineStackingStrategy(self): # -> LineStackingStrategy
        """
        Get: LineStackingStrategy(self: RibbonTwoLineText) -> LineStackingStrategy
        Set: LineStackingStrategy(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def PathFill(self) -> Brush:
        """
        Get: PathFill(self: RibbonTwoLineText) -> Brush
        Set: PathFill(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def PathStroke(self) -> Brush:
        """
        Get: PathStroke(self: RibbonTwoLineText) -> Brush
        Set: PathStroke(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: RibbonTwoLineText) -> str
        Set: Text(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def TextAlignment(self): # -> TextAlignment
        """
        Get: TextAlignment(self: RibbonTwoLineText) -> TextAlignment
        Set: TextAlignment(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def TextDecorations(self): # -> TextDecorationCollection
        """
        Get: TextDecorations(self: RibbonTwoLineText) -> TextDecorationCollection
        Set: TextDecorations(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def TextEffects(self): # -> TextEffectCollection
        """
        Get: TextEffects(self: RibbonTwoLineText) -> TextEffectCollection
        Set: TextEffects(self: RibbonTwoLineText) = value
        """
        ...

    @property
    def TextTrimming(self): # -> TextTrimming
        """
        Get: TextTrimming(self: RibbonTwoLineText) -> TextTrimming
        Set: TextTrimming(self: RibbonTwoLineText) = value
        """
        ...


    @staticmethod
    def GetHasTwoLines(element:DependencyObject) -> bool:
        """ GetHasTwoLines(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetPathData(element:DependencyObject): # -> Geometry
        """ GetPathData(element: DependencyObject) -> Geometry """
        ...

    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonTwoLineText) """
        ...

    @staticmethod
    def SetHasTwoLines(element:DependencyObject, value:bool): # -> 
        """ SetHasTwoLines(element: DependencyObject, value: bool) """
        ...

    @staticmethod
    def SetPathData(element:DependencyObject, value): # ->  # Not found arg types: {'value': 'Geometry'}
        """ SetPathData(element: DependencyObject, value: Geometry) """
        ...

    BaselineOffsetProperty: DependencyProperty = ...
    HasTwoLinesProperty: DependencyProperty = ...
    LineHeightProperty: DependencyProperty = ...
    LineStackingStrategyProperty: DependencyProperty = ...
    PaddingProperty: DependencyProperty = ...
    PathDataProperty: DependencyProperty = ...
    PathFillProperty: DependencyProperty = ...
    PathStrokeProperty: DependencyProperty = ...
    TextAlignmentProperty: DependencyProperty = ...
    TextDecorationsProperty: DependencyProperty = ...
    TextEffectsProperty: DependencyProperty = ...
    TextProperty: DependencyProperty = ...
    TextTrimmingProperty: DependencyProperty = ...


class RibbonWindow(Window): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAddChild'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'IWindowService'>, <type 'object'>
    """ RibbonWindow() """
    def OnApplyTemplate(self): # -> 
        """ OnApplyTemplate(self: RibbonWindow) """
        ...


class StringCollectionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ StringCollectionConverter() """
    pass

# variables with complex values

