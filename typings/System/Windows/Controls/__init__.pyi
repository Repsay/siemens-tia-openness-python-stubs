# encoding: utf-8
# module System.Windows.Controls calls itself Controls
# from System.Windows.Controls.Ribbon, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Word import Style

from System import AsyncCallback, Enum, IAsyncResult, MulticastDelegate

from System.Web.UI import Control

from System.Workflow.ComponentModel import (DependencyObject, 
    DependencyProperty)

"""The following names are not found in the module: (RoutedEvent, 
    RoutedEventArgs, UIElement, Visibility, field#)
"""

# no functions
# classes

class ActivatingKeyTipEventArgs(RoutedEventArgs): # skipped bases: <type 'object'>
    """ ActivatingKeyTipEventArgs() """
    @property
    def KeyTipHorizontalOffset(self) -> float:
        """
        Get: KeyTipHorizontalOffset(self: ActivatingKeyTipEventArgs) -> float
        Set: KeyTipHorizontalOffset(self: ActivatingKeyTipEventArgs) = value
        """
        ...

    @property
    def KeyTipHorizontalPlacement(self) -> KeyTipHorizontalPlacement:
        """
        Get: KeyTipHorizontalPlacement(self: ActivatingKeyTipEventArgs) -> KeyTipHorizontalPlacement
        Set: KeyTipHorizontalPlacement(self: ActivatingKeyTipEventArgs) = value
        """
        ...

    @property
    def KeyTipVerticalOffset(self) -> float:
        """
        Get: KeyTipVerticalOffset(self: ActivatingKeyTipEventArgs) -> float
        Set: KeyTipVerticalOffset(self: ActivatingKeyTipEventArgs) = value
        """
        ...

    @property
    def KeyTipVerticalPlacement(self) -> KeyTipVerticalPlacement:
        """
        Get: KeyTipVerticalPlacement(self: ActivatingKeyTipEventArgs) -> KeyTipVerticalPlacement
        Set: KeyTipVerticalPlacement(self: ActivatingKeyTipEventArgs) = value
        """
        ...

    @property
    def KeyTipVisibility(self): # -> Visibility
        """
        Get: KeyTipVisibility(self: ActivatingKeyTipEventArgs) -> Visibility
        Set: KeyTipVisibility(self: ActivatingKeyTipEventArgs) = value
        """
        ...

    @property
    def PlacementTarget(self): # -> UIElement
        """
        Get: PlacementTarget(self: ActivatingKeyTipEventArgs) -> UIElement
        Set: PlacementTarget(self: ActivatingKeyTipEventArgs) = value
        """
        ...



class ActivatingKeyTipEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ActivatingKeyTipEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ActivatingKeyTipEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ActivatingKeyTipEventHandler, sender: object, e: ActivatingKeyTipEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ActivatingKeyTipEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ActivatingKeyTipEventArgs): # -> 
        """ Invoke(self: ActivatingKeyTipEventHandler, sender: object, e: ActivatingKeyTipEventArgs) """
        ...


class KeyTipAccessedEventArgs(RoutedEventArgs): # skipped bases: <type 'object'>
    """ KeyTipAccessedEventArgs() """
    @property
    def TargetKeyTipScope(self) -> DependencyObject:
        """
        Get: TargetKeyTipScope(self: KeyTipAccessedEventArgs) -> DependencyObject
        Set: TargetKeyTipScope(self: KeyTipAccessedEventArgs) = value
        """
        ...



class KeyTipAccessedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ KeyTipAccessedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:KeyTipAccessedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: KeyTipAccessedEventHandler, sender: object, e: KeyTipAccessedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: KeyTipAccessedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:KeyTipAccessedEventArgs): # -> 
        """ Invoke(self: KeyTipAccessedEventHandler, sender: object, e: KeyTipAccessedEventArgs) """
        ...


class KeyTipControl(Control): # skipped bases: <type 'IFrameworkInputElement'>, <type 'IQueryAmbient'>, <type 'IAnimatable'>, <type 'IInputElement'>, <type 'IHaveResources'>, <type 'IResource'>, <type 'ISupportInitialize'>, <type 'object'>
    """ KeyTipControl() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: KeyTipControl) -> str
        Set: Text(self: KeyTipControl) = value
        """
        ...


    TextProperty: DependencyProperty = ...


class KeyTipHorizontalPlacement(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyTipHorizontalPlacement, values: KeyTipCenterAtTargetCenter (4), KeyTipCenterAtTargetLeft (3), KeyTipCenterAtTargetRight (5), KeyTipLeftAtTargetCenter (1), KeyTipLeftAtTargetLeft (0), KeyTipLeftAtTargetRight (2), KeyTipRightAtTargetCenter (7), KeyTipRightAtTargetLeft (6), KeyTipRightAtTargetRight (8) """
    KeyTipCenterAtTargetCenter: KeyTipHorizontalPlacement = ...
    KeyTipCenterAtTargetLeft: KeyTipHorizontalPlacement = ...
    KeyTipCenterAtTargetRight: KeyTipHorizontalPlacement = ...
    KeyTipLeftAtTargetCenter: KeyTipHorizontalPlacement = ...
    KeyTipLeftAtTargetLeft: KeyTipHorizontalPlacement = ...
    KeyTipLeftAtTargetRight: KeyTipHorizontalPlacement = ...
    KeyTipRightAtTargetCenter: KeyTipHorizontalPlacement = ...
    KeyTipRightAtTargetLeft: KeyTipHorizontalPlacement = ...
    KeyTipRightAtTargetRight: KeyTipHorizontalPlacement = ...
    value__ = ...


class KeyTipService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddActivatingKeyTipHandler(element:DependencyObject, handler:ActivatingKeyTipEventHandler): # -> 
        """ AddActivatingKeyTipHandler(element: DependencyObject, handler: ActivatingKeyTipEventHandler) """
        ...

    @staticmethod
    def AddKeyTipAccessedHandler(element:DependencyObject, handler:KeyTipAccessedEventHandler): # -> 
        """ AddKeyTipAccessedHandler(element: DependencyObject, handler: KeyTipAccessedEventHandler) """
        ...

    @staticmethod
    def AddPreviewKeyTipAccessedHandler(element:DependencyObject, handler:KeyTipAccessedEventHandler): # -> 
        """ AddPreviewKeyTipAccessedHandler(element: DependencyObject, handler: KeyTipAccessedEventHandler) """
        ...

    @staticmethod
    def DismissKeyTips(): # -> 
        """ DismissKeyTips() """
        ...

    @staticmethod
    def GetIsKeyTipScope(element:DependencyObject) -> bool:
        """ GetIsKeyTipScope(element: DependencyObject) -> bool """
        ...

    @staticmethod
    def GetKeyTip(element:DependencyObject) -> str:
        """ GetKeyTip(element: DependencyObject) -> str """
        ...

    @staticmethod
    def GetKeyTipStyle(element:DependencyObject) -> Style:
        """ GetKeyTipStyle(element: DependencyObject) -> Style """
        ...

    @staticmethod
    def RemoveActivatingKeyTipHandler(element:DependencyObject, handler:ActivatingKeyTipEventHandler): # -> 
        """ RemoveActivatingKeyTipHandler(element: DependencyObject, handler: ActivatingKeyTipEventHandler) """
        ...

    @staticmethod
    def RemoveKeyTipAccessedHandler(element:DependencyObject, handler:KeyTipAccessedEventHandler): # -> 
        """ RemoveKeyTipAccessedHandler(element: DependencyObject, handler: KeyTipAccessedEventHandler) """
        ...

    @staticmethod
    def RemovePreviewKeyTipAccessedHandler(element:DependencyObject, handler:KeyTipAccessedEventHandler): # -> 
        """ RemovePreviewKeyTipAccessedHandler(element: DependencyObject, handler: KeyTipAccessedEventHandler) """
        ...

    @staticmethod
    def SetIsKeyTipScope(element:DependencyObject, value:bool): # -> 
        """ SetIsKeyTipScope(element: DependencyObject, value: bool) """
        ...

    @staticmethod
    def SetKeyTip(element:DependencyObject, value:str): # -> 
        """ SetKeyTip(element: DependencyObject, value: str) """
        ...

    @staticmethod
    def SetKeyTipStyle(element:DependencyObject, value:Style): # -> 
        """ SetKeyTipStyle(element: DependencyObject, value: Style) """
        ...

    ActivatingKeyTipEvent = ...
    IsKeyTipScopeProperty: DependencyProperty = ...
    KeyTipAccessedEvent = ...
    KeyTipProperty: DependencyProperty = ...
    KeyTipStyleProperty: DependencyProperty = ...
    PreviewKeyTipAccessedEvent = ...


class KeyTipVerticalPlacement(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyTipVerticalPlacement, values: KeyTipBottomAtTargetBottom (8), KeyTipBottomAtTargetCenter (7), KeyTipBottomAtTargetTop (6), KeyTipCenterAtTargetBottom (5), KeyTipCenterAtTargetCenter (4), KeyTipCenterAtTargetTop (3), KeyTipTopAtTargetBottom (2), KeyTipTopAtTargetCenter (1), KeyTipTopAtTargetTop (0) """
    KeyTipBottomAtTargetBottom: KeyTipVerticalPlacement = ...
    KeyTipBottomAtTargetCenter: KeyTipVerticalPlacement = ...
    KeyTipBottomAtTargetTop: KeyTipVerticalPlacement = ...
    KeyTipCenterAtTargetBottom: KeyTipVerticalPlacement = ...
    KeyTipCenterAtTargetCenter: KeyTipVerticalPlacement = ...
    KeyTipCenterAtTargetTop: KeyTipVerticalPlacement = ...
    KeyTipTopAtTargetBottom: KeyTipVerticalPlacement = ...
    KeyTipTopAtTargetCenter: KeyTipVerticalPlacement = ...
    KeyTipTopAtTargetTop: KeyTipVerticalPlacement = ...
    value__ = ...


# variables with complex values

