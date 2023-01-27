# encoding: utf-8
# module System.Windows.Forms.Design.Behavior calls itself Behavior
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    IDisposable, IntPtr, MulticastDelegate)

from System.Collections import CollectionBase, ICollection, IEnumerator

from System.ComponentModel import IComponent

from System.ComponentModel.Design import CommandID, MenuCommand

from System.Drawing import Graphics, Rectangle

from System.Messaging import Cursor

from System.Web.UI import Control

from typing import Self

from Windows.Foundation import Point

"""The following names are not found in the module: (BoundEvent, 
    DragEventArgs, GiveFeedbackEventArgs, MouseButtons, PaintEventArgs, 
    QueryContinueDragEventArgs, field#)
"""

# no functions
# classes

class Adorner: # skipped bases: <type 'object'>, <type 'object'>
    """ Adorner() """
    @property
    def BehaviorService(self) -> BehaviorService:
        """
        Get: BehaviorService(self: Adorner) -> BehaviorService
        Set: BehaviorService(self: Adorner) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Adorner) -> bool
        Set: Enabled(self: Adorner) = value
        """
        ...

    @property
    def Glyphs(self) -> GlyphCollection:
        """ Get: Glyphs(self: Adorner) -> GlyphCollection """
        ...


    def Invalidate(self, *__args:Rectangle): # -> 
        """ Invalidate(self: Adorner)Invalidate(self: Adorner, rectangle: Rectangle)Invalidate(self: Adorner, region: Region) """
        ...


class Behavior: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: Behavior) -> Cursor """
        ...

    @property
    def DisableAllCommands(self) -> bool:
        """ Get: DisableAllCommands(self: Behavior) -> bool """
        ...


    def FindCommand(self, commandId:CommandID) -> MenuCommand:
        """ FindCommand(self: Behavior, commandId: CommandID) -> MenuCommand """
        ...

    def OnDragDrop(self, g:Glyph, e): # ->  # Not found arg types: {'e': 'DragEventArgs'}
        """ OnDragDrop(self: Behavior, g: Glyph, e: DragEventArgs) """
        ...

    def OnDragEnter(self, g:Glyph, e): # ->  # Not found arg types: {'e': 'DragEventArgs'}
        """ OnDragEnter(self: Behavior, g: Glyph, e: DragEventArgs) """
        ...

    def OnDragLeave(self, g:Glyph, e:EventArgs): # -> 
        """ OnDragLeave(self: Behavior, g: Glyph, e: EventArgs) """
        ...

    def OnDragOver(self, g:Glyph, e): # ->  # Not found arg types: {'e': 'DragEventArgs'}
        """ OnDragOver(self: Behavior, g: Glyph, e: DragEventArgs) """
        ...

    def OnGiveFeedback(self, g:Glyph, e): # ->  # Not found arg types: {'e': 'GiveFeedbackEventArgs'}
        """ OnGiveFeedback(self: Behavior, g: Glyph, e: GiveFeedbackEventArgs) """
        ...

    def OnLoseCapture(self, g:Glyph, e:EventArgs): # -> 
        """ OnLoseCapture(self: Behavior, g: Glyph, e: EventArgs) """
        ...

    def OnMouseDoubleClick(self, g:Glyph, button, mouseLoc:Point) -> bool: # Not found arg types: {'button': 'MouseButtons'}
        """ OnMouseDoubleClick(self: Behavior, g: Glyph, button: MouseButtons, mouseLoc: Point) -> bool """
        ...

    def OnMouseDown(self, g:Glyph, button, mouseLoc:Point) -> bool: # Not found arg types: {'button': 'MouseButtons'}
        """ OnMouseDown(self: Behavior, g: Glyph, button: MouseButtons, mouseLoc: Point) -> bool """
        ...

    def OnMouseEnter(self, g:Glyph) -> bool:
        """ OnMouseEnter(self: Behavior, g: Glyph) -> bool """
        ...

    def OnMouseHover(self, g:Glyph, mouseLoc:Point) -> bool:
        """ OnMouseHover(self: Behavior, g: Glyph, mouseLoc: Point) -> bool """
        ...

    def OnMouseLeave(self, g:Glyph) -> bool:
        """ OnMouseLeave(self: Behavior, g: Glyph) -> bool """
        ...

    def OnMouseMove(self, g:Glyph, button, mouseLoc:Point) -> bool: # Not found arg types: {'button': 'MouseButtons'}
        """ OnMouseMove(self: Behavior, g: Glyph, button: MouseButtons, mouseLoc: Point) -> bool """
        ...

    def OnMouseUp(self, g:Glyph, button) -> bool: # Not found arg types: {'button': 'MouseButtons'}
        """ OnMouseUp(self: Behavior, g: Glyph, button: MouseButtons) -> bool """
        ...

    def OnQueryContinueDrag(self, g:Glyph, e): # ->  # Not found arg types: {'e': 'QueryContinueDragEventArgs'}
        """ OnQueryContinueDrag(self: Behavior, g: Glyph, e: QueryContinueDragEventArgs) """
        ...


class BehaviorDragDropEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ BehaviorDragDropEventArgs(dragComponents: ICollection) """
    @property
    def DragComponents(self) -> ICollection:
        """ Get: DragComponents(self: BehaviorDragDropEventArgs) -> ICollection """
        ...


    def __new__(cls, dragComponents:ICollection) -> Self:
        """ __new__(cls: type, dragComponents: ICollection) """
        ...


class BehaviorDragDropEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BehaviorDragDropEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:BehaviorDragDropEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BehaviorDragDropEventHandler, sender: object, e: BehaviorDragDropEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: BehaviorDragDropEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:BehaviorDragDropEventArgs): # -> 
        """ Invoke(self: BehaviorDragDropEventHandler, sender: object, e: BehaviorDragDropEventArgs) """
        ...


class BehaviorService(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Adorners(self) -> BehaviorServiceAdornerCollection:
        """ Get: Adorners(self: BehaviorService) -> BehaviorServiceAdornerCollection """
        ...

    @property
    def AdornerWindowGraphics(self) -> Graphics:
        """ Get: AdornerWindowGraphics(self: BehaviorService) -> Graphics """
        ...

    @property
    def CurrentBehavior(self) -> Behavior:
        """ Get: CurrentBehavior(self: BehaviorService) -> Behavior """
        ...


    def AdornerWindowPointToScreen(self, p:Point) -> Point:
        """ AdornerWindowPointToScreen(self: BehaviorService, p: Point) -> Point """
        ...

    def AdornerWindowToScreen(self) -> Point:
        """ AdornerWindowToScreen(self: BehaviorService) -> Point """
        ...

    def ControlRectInAdornerWindow(self, c:Control) -> Rectangle:
        """ ControlRectInAdornerWindow(self: BehaviorService, c: Control) -> Rectangle """
        ...

    def ControlToAdornerWindow(self, c:Control) -> Point:
        """ ControlToAdornerWindow(self: BehaviorService, c: Control) -> Point """
        ...

    def GetNextBehavior(self, behavior:Behavior) -> Behavior:
        """ GetNextBehavior(self: BehaviorService, behavior: Behavior) -> Behavior """
        ...

    def Invalidate(self, *__args:Rectangle): # -> 
        """ Invalidate(self: BehaviorService)Invalidate(self: BehaviorService, rect: Rectangle)Invalidate(self: BehaviorService, r: Region) """
        ...

    def MapAdornerWindowPoint(self, handle:IntPtr, pt:Point) -> Point:
        """ MapAdornerWindowPoint(self: BehaviorService, handle: IntPtr, pt: Point) -> Point """
        ...

    def PopBehavior(self, behavior:Behavior) -> Behavior:
        """ PopBehavior(self: BehaviorService, behavior: Behavior) -> Behavior """
        ...

    def PushBehavior(self, behavior:Behavior): # -> 
        """ PushBehavior(self: BehaviorService, behavior: Behavior) """
        ...

    def PushCaptureBehavior(self, behavior:Behavior): # -> 
        """ PushCaptureBehavior(self: BehaviorService, behavior: Behavior) """
        ...

    def ScreenToAdornerWindow(self, p:Point) -> Point:
        """ ScreenToAdornerWindow(self: BehaviorService, p: Point) -> Point """
        ...

    def SyncSelection(self): # -> 
        """ SyncSelection(self: BehaviorService) """
        ...

    BeginDrag = ...
    EndDrag = ...
    Synchronize = ...


class BehaviorServiceAdornerCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    BehaviorServiceAdornerCollection(behaviorService: BehaviorService)
    BehaviorServiceAdornerCollection(value: BehaviorServiceAdornerCollection)
    BehaviorServiceAdornerCollection(value: Array[Adorner])
    """
    def Add(self, value:Adorner) -> int:
        """ Add(self: BehaviorServiceAdornerCollection, value: Adorner) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: BehaviorServiceAdornerCollection, value: Array[Adorner])AddRange(self: BehaviorServiceAdornerCollection, value: BehaviorServiceAdornerCollection) """
        ...

    def Contains(self, value:Adorner) -> bool:
        """ Contains(self: BehaviorServiceAdornerCollection, value: Adorner) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BehaviorServiceAdornerCollection, array: Array[Adorner], index: int) """
        ...

    def IndexOf(self, value:Adorner) -> int:
        """ IndexOf(self: BehaviorServiceAdornerCollection, value: Adorner) -> int """
        ...

    def Insert(self, index:int, value:Adorner): # -> 
        """ Insert(self: BehaviorServiceAdornerCollection, index: int, value: Adorner) """
        ...

    def Remove(self, value:Adorner): # -> 
        """ Remove(self: BehaviorServiceAdornerCollection, value: Adorner) """
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


class BehaviorServiceAdornerCollectionEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ BehaviorServiceAdornerCollectionEnumerator(mappings: BehaviorServiceAdornerCollection) """
    pass

class Glyph: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Behavior(self) -> Behavior:
        """ Get: Behavior(self: Glyph) -> Behavior """
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: Glyph) -> Rectangle """
        ...


    def GetHitTest(self, p:Point) -> Cursor:
        """ GetHitTest(self: Glyph, p: Point) -> Cursor """
        ...

    def Paint(self, pe): # ->  # Not found arg types: {'pe': 'PaintEventArgs'}
        """ Paint(self: Glyph, pe: PaintEventArgs) """
        ...

    def SetBehavior(self, *args): #cannot find CLR method
        """ SetBehavior(self: Glyph, behavior: Behavior) """
        ...


class ComponentGlyph(Glyph): # skipped bases: <type 'object'>
    """
    ComponentGlyph(relatedComponent: IComponent, behavior: Behavior)
    ComponentGlyph(relatedComponent: IComponent)
    """
    @property
    def RelatedComponent(self) -> IComponent:
        """ Get: RelatedComponent(self: ComponentGlyph) -> IComponent """
        ...



class ControlBodyGlyph(ComponentGlyph): # skipped bases: <type 'object'>
    """
    ControlBodyGlyph(bounds: Rectangle, cursor: Cursor, relatedComponent: IComponent, designer: ControlDesigner)
    ControlBodyGlyph(bounds: Rectangle, cursor: Cursor, relatedComponent: IComponent, behavior: Behavior)
    """
    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: ControlBodyGlyph) -> Rectangle """
        ...



class GlyphCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    GlyphCollection()
    GlyphCollection(value: GlyphCollection)
    GlyphCollection(value: Array[Glyph])
    """
    def Add(self, value:Glyph) -> int:
        """ Add(self: GlyphCollection, value: Glyph) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: GlyphCollection, value: Array[Glyph])AddRange(self: GlyphCollection, value: GlyphCollection) """
        ...

    def Contains(self, value:Glyph) -> bool:
        """ Contains(self: GlyphCollection, value: Glyph) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: GlyphCollection, array: Array[Glyph], index: int) """
        ...

    def IndexOf(self, value:Glyph) -> int:
        """ IndexOf(self: GlyphCollection, value: Glyph) -> int """
        ...

    def Insert(self, index:int, value:Glyph): # -> 
        """ Insert(self: GlyphCollection, index: int, value: Glyph) """
        ...

    def Remove(self, value:Glyph): # -> 
        """ Remove(self: GlyphCollection, value: Glyph) """
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


class GlyphSelectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GlyphSelectionType, values: NotSelected (0), Selected (1), SelectedPrimary (2) """
    NotSelected: GlyphSelectionType = ...
    Selected: GlyphSelectionType = ...
    SelectedPrimary: GlyphSelectionType = ...
    value__ = ...


class SnapLine: # skipped bases: <type 'object'>, <type 'object'>
    """
    SnapLine(type: SnapLineType, offset: int)
    SnapLine(type: SnapLineType, offset: int, filter: str)
    SnapLine(type: SnapLineType, offset: int, priority: SnapLinePriority)
    SnapLine(type: SnapLineType, offset: int, filter: str, priority: SnapLinePriority)
    """
    @property
    def Filter(self) -> str:
        """ Get: Filter(self: SnapLine) -> str """
        ...

    @property
    def IsHorizontal(self) -> bool:
        """ Get: IsHorizontal(self: SnapLine) -> bool """
        ...

    @property
    def IsVertical(self) -> bool:
        """ Get: IsVertical(self: SnapLine) -> bool """
        ...

    @property
    def Offset(self) -> int:
        """ Get: Offset(self: SnapLine) -> int """
        ...

    @property
    def Priority(self) -> SnapLinePriority:
        """ Get: Priority(self: SnapLine) -> SnapLinePriority """
        ...

    @property
    def SnapLineType(self) -> SnapLineType:
        """ Get: SnapLineType(self: SnapLine) -> SnapLineType """
        ...


    def AdjustOffset(self, adjustment:int): # -> 
        """ AdjustOffset(self: SnapLine, adjustment: int) """
        ...

    @staticmethod
    def ShouldSnap(line1:SnapLine, line2:SnapLine) -> bool:
        """ ShouldSnap(line1: SnapLine, line2: SnapLine) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: SnapLine) -> str """
        ...


class SnapLinePriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SnapLinePriority, values: Always (4), High (3), Low (1), Medium (2) """
    Always: SnapLinePriority = ...
    High: SnapLinePriority = ...
    Low: SnapLinePriority = ...
    Medium: SnapLinePriority = ...
    value__ = ...


class SnapLineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SnapLineType, values: Baseline (6), Bottom (1), Horizontal (4), Left (2), Right (3), Top (0), Vertical (5) """
    Baseline: SnapLineType = ...
    Bottom: SnapLineType = ...
    Horizontal: SnapLineType = ...
    Left: SnapLineType = ...
    Right: SnapLineType = ...
    Top: SnapLineType = ...
    value__ = ...
    Vertical: SnapLineType = ...


