# encoding: utf-8
# module System.Workflow.ComponentModel.Design calls itself Design
# from System.Workflow.ComponentModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, Guid, 
    IAsyncResult, IDisposable, IServiceProvider, Int64, MulticastDelegate, 
    Single, Type, Uri)

from System.CodeDom import CodeSnippetExpression, MemberAttributes

from System.Collections import ICollection, IDictionary, IList

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import (ISite, ITypeDescriptorContext, 
    MemberDescriptor, TypeConverter)

from System.ComponentModel.Design import (CommandID, DesignerVerb, 
    DesignerVerbCollection, IDesignerFilter, IDesignerHost, IRootDesigner, 
    ITypeResolutionService, StandardCommands)

from System.ComponentModel.Design.Serialization import BasicDesignerLoader

from System.Drawing import (Brush, Color, Font, Graphics, Image, Pen, 
    Rectangle, StringAlignment)

from System.Drawing.Design import IToolboxUser, ToolboxItem, UITypeEditor

from System.Drawing.Drawing2D import (DashStyle, GraphicsPath, 
    LinearGradientMode)

from System.Drawing.Imaging import ImageFormat

from System.Drawing.Printing import PrintDocument

from System.EnterpriseServices import Activity

from System.IO import (BinaryReader, BinaryWriter, Stream, TextReader, 
    TextWriter)

from System.Reflection import Assembly, AssemblyName

from System.Runtime.InteropServices.ComTypes import IDataObject

from System.Web.UI import UserControl

from System.Web.UI.MobileControls import Form

from System.Workflow.ComponentModel import CompositeActivity

from System.Workflow.ComponentModel.Compiler import (ITypeProvider, 
    TypeProvider)

from System.Workflow.ComponentModel.Serialization import (
    WorkflowMarkupSerializer)

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point, Size

"""The following names are not found in the module: (AccessibleNavigation, 
    AccessibleObject, AutoSizeMode, BoundEvent, ButtonState, 
    ControlAccessibleObject, DialogResult, DragEventArgs, HScrollBar, 
    IConnectableDesigner, IMessageFilter, IPropertyValueProvider, 
    IWorkflowDesignerMessageSink, TreeNode, VScrollBar, field#)
"""

# no functions
# classes

class ActivityBindTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ActivityBindTypeConverter() """
    pass

class ActivityChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActivityChangedEventArgs(activity: Activity, member: MemberDescriptor, oldValue: object, newValue: object) """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityChangedEventArgs) -> Activity """
        ...

    @property
    def Member(self) -> MemberDescriptor:
        """ Get: Member(self: ActivityChangedEventArgs) -> MemberDescriptor """
        ...

    @property
    def NewValue(self) -> object:
        """ Get: NewValue(self: ActivityChangedEventArgs) -> object """
        ...

    @property
    def OldValue(self) -> object:
        """ Get: OldValue(self: ActivityChangedEventArgs) -> object """
        ...


    def __new__(cls, activity:Activity, member:MemberDescriptor, oldValue:object, newValue:object) -> Self:
        """ __new__(cls: type, activity: Activity, member: MemberDescriptor, oldValue: object, newValue: object) """
        ...


class IPersistUIState: # skipped bases: <type 'object'>
    """ no doc """
    def LoadViewState(self, reader:BinaryReader): # -> 
        """ LoadViewState(self: IPersistUIState, reader: BinaryReader) """
        ...

    def SaveViewState(self, writer:BinaryWriter): # -> 
        """ SaveViewState(self: IPersistUIState, writer: BinaryWriter) """
        ...


class IWorkflowRootDesigner(IRootDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesigner'>, <type 'object'>
    """ no doc """
    @property
    def InvokingDesigner(self) -> CompositeActivityDesigner:
        """
        Get: InvokingDesigner(self: IWorkflowRootDesigner) -> CompositeActivityDesigner
        Set: InvokingDesigner(self: IWorkflowRootDesigner) = value
        """
        ...

    @property
    def MessageFilters(self) -> ReadOnlyCollection:
        """ Get: MessageFilters(self: IWorkflowRootDesigner) -> ReadOnlyCollection[WorkflowDesignerMessageFilter] """
        ...

    @property
    def SupportsLayoutPersistence(self) -> bool:
        """ Get: SupportsLayoutPersistence(self: IWorkflowRootDesigner) -> bool """
        ...


    def IsSupportedActivityType(self, activityType:Type) -> bool:
        """ IsSupportedActivityType(self: IWorkflowRootDesigner, activityType: Type) -> bool """
        ...


class ActivityDesigner(IWorkflowDesignerMessageSink, IToolboxUser, IPersistUIState, IConnectableDesigner, IWorkflowRootDesigner, IDesignerFilter): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'object'>
    """ ActivityDesigner() """
    @property
    def AccessibilityObject(self): # -> AccessibleObject
        """ Get: AccessibilityObject(self: ActivityDesigner) -> AccessibleObject """
        ...

    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityDesigner) -> Activity """
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: ActivityDesigner) -> Rectangle """
        ...

    @property
    def DesignerActions(self):
        ...

    @property
    def DesignerTheme(self) -> ActivityDesignerTheme:
        """ Get: DesignerTheme(self: ActivityDesigner) -> ActivityDesignerTheme """
        ...

    @property
    def EnableVisualResizing(self):
        ...

    @property
    def Glyphs(self):
        ...

    @property
    def Image(self) -> Image:
        """ Get: Image(self: ActivityDesigner) -> Image """
        ...

    @property
    def ImageRectangle(self):
        ...

    @property
    def IsLocked(self) -> bool:
        """ Get: IsLocked(self: ActivityDesigner) -> bool """
        ...

    @property
    def IsPrimarySelection(self) -> bool:
        """ Get: IsPrimarySelection(self: ActivityDesigner) -> bool """
        ...

    @property
    def IsRootDesigner(self) -> bool:
        """ Get: IsRootDesigner(self: ActivityDesigner) -> bool """
        ...

    @property
    def IsSelected(self) -> bool:
        """ Get: IsSelected(self: ActivityDesigner) -> bool """
        ...

    @property
    def IsVisible(self) -> bool:
        """ Get: IsVisible(self: ActivityDesigner) -> bool """
        ...

    @property
    def Location(self) -> Point:
        """
        Get: Location(self: ActivityDesigner) -> Point
        Set: Location(self: ActivityDesigner) = value
        """
        ...

    @property
    def MinimumSize(self) -> Size:
        """ Get: MinimumSize(self: ActivityDesigner) -> Size """
        ...

    @property
    def ParentDesigner(self) -> CompositeActivityDesigner:
        """ Get: ParentDesigner(self: ActivityDesigner) -> CompositeActivityDesigner """
        ...

    @property
    def ParentView(self):
        ...

    @property
    def ShowSmartTag(self):
        ...

    @property
    def Size(self) -> Size:
        """
        Get: Size(self: ActivityDesigner) -> Size
        Set: Size(self: ActivityDesigner) = value
        """
        ...

    @property
    def SmartTagRectangle(self):
        ...

    @property
    def SmartTagVerbs(self):
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ActivityDesigner) -> str """
        ...

    @property
    def TextRectangle(self):
        ...

    @property
    def Verbs(self):
        ...


    def CanBeParentedTo(self, parentActivityDesigner:CompositeActivityDesigner) -> bool:
        """ CanBeParentedTo(self: ActivityDesigner, parentActivityDesigner: CompositeActivityDesigner) -> bool """
        ...

    def CanConnect(self, *args): #cannot find CLR method
        """ CanConnect(self: ActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) -> bool """
        ...

    def CreateView(self, *args): #cannot find CLR method
        """ CreateView(self: ActivityDesigner, viewTechnology: ViewTechnology) -> WorkflowView """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: ActivityDesigner) """
        ...

    def DoDefaultAction(self, *args): #cannot find CLR method
        """ DoDefaultAction(self: ActivityDesigner) """
        ...

    def EnsureVisible(self): # -> 
        """ EnsureVisible(self: ActivityDesigner) """
        ...

    def GetConnectionPoints(self, edges:DesignerEdges) -> ReadOnlyCollection:
        """ GetConnectionPoints(self: ActivityDesigner, edges: DesignerEdges) -> ReadOnlyCollection[ConnectionPoint] """
        ...

    def GetConnections(self, *args): #cannot find CLR method
        """ GetConnections(self: ActivityDesigner, edges: DesignerEdges) -> ReadOnlyCollection[Point] """
        ...

    def GetPreviewImage(self, compatibleGraphics:Graphics) -> Image:
        """ GetPreviewImage(self: ActivityDesigner, compatibleGraphics: Graphics) -> Image """
        ...

    @staticmethod
    def GetRootDesigner(serviceProvider:IServiceProvider) -> ActivityDesigner:
        """ GetRootDesigner(serviceProvider: IServiceProvider) -> ActivityDesigner """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: ActivityDesigner, serviceType: Type) -> object """
        ...

    def HitTest(self, point:Point) -> HitTestInfo:
        """ HitTest(self: ActivityDesigner, point: Point) -> HitTestInfo """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: ActivityDesigner, activity: Activity) """
        ...

    def Invalidate(self, rectangle:Rectangle = ...): # -> 
        """ Invalidate(self: ActivityDesigner)Invalidate(self: ActivityDesigner, rectangle: Rectangle) """
        ...

    @staticmethod
    def IsCommentedActivity(activity:Activity) -> bool:
        """ IsCommentedActivity(activity: Activity) -> bool """
        ...

    def OnActivityChanged(self, *args): #cannot find CLR method
        """ OnActivityChanged(self: ActivityDesigner, e: ActivityChangedEventArgs) """
        ...

    def OnBeginResizing(self, *args): #cannot find CLR method
        """ OnBeginResizing(self: ActivityDesigner, e: ActivityDesignerResizeEventArgs) """
        ...

    def OnConnected(self, *args): #cannot find CLR method
        """ OnConnected(self: ActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) """
        ...

    def OnDragDrop(self, *args): #cannot find CLR method
        """ OnDragDrop(self: ActivityDesigner, e: ActivityDragEventArgs) """
        ...

    def OnDragEnter(self, *args): #cannot find CLR method
        """ OnDragEnter(self: ActivityDesigner, e: ActivityDragEventArgs) """
        ...

    def OnDragLeave(self, *args): #cannot find CLR method
        """ OnDragLeave(self: ActivityDesigner) """
        ...

    def OnDragOver(self, *args): #cannot find CLR method
        """ OnDragOver(self: ActivityDesigner, e: ActivityDragEventArgs) """
        ...

    def OnEndResizing(self, *args): #cannot find CLR method
        """ OnEndResizing(self: ActivityDesigner) """
        ...

    def OnExecuteDesignerAction(self, *args): #cannot find CLR method
        """ OnExecuteDesignerAction(self: ActivityDesigner, designerAction: DesignerAction) """
        ...

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """ OnGiveFeedback(self: ActivityDesigner, e: GiveFeedbackEventArgs) """
        ...

    def OnKeyDown(self, *args): #cannot find CLR method
        """ OnKeyDown(self: ActivityDesigner, e: KeyEventArgs) """
        ...

    def OnKeyUp(self, *args): #cannot find CLR method
        """ OnKeyUp(self: ActivityDesigner, e: KeyEventArgs) """
        ...

    def OnLayoutPosition(self, *args): #cannot find CLR method
        """ OnLayoutPosition(self: ActivityDesigner, e: ActivityDesignerLayoutEventArgs) """
        ...

    def OnLayoutSize(self, *args): #cannot find CLR method
        """ OnLayoutSize(self: ActivityDesigner, e: ActivityDesignerLayoutEventArgs) -> Size """
        ...

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """ OnMouseCaptureChanged(self: ActivityDesigner) """
        ...

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """ OnMouseDoubleClick(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseDown(self, *args): #cannot find CLR method
        """ OnMouseDown(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseDragBegin(self, *args): #cannot find CLR method
        """ OnMouseDragBegin(self: ActivityDesigner, initialDragPoint: Point, e: MouseEventArgs) """
        ...

    def OnMouseDragEnd(self, *args): #cannot find CLR method
        """ OnMouseDragEnd(self: ActivityDesigner) """
        ...

    def OnMouseDragMove(self, *args): #cannot find CLR method
        """ OnMouseDragMove(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseEnter(self, *args): #cannot find CLR method
        """ OnMouseEnter(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseHover(self, *args): #cannot find CLR method
        """ OnMouseHover(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseLeave(self, *args): #cannot find CLR method
        """ OnMouseLeave(self: ActivityDesigner) """
        ...

    def OnMouseMove(self, *args): #cannot find CLR method
        """ OnMouseMove(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnMouseUp(self, *args): #cannot find CLR method
        """ OnMouseUp(self: ActivityDesigner, e: MouseEventArgs) """
        ...

    def OnPaint(self, *args): #cannot find CLR method
        """ OnPaint(self: ActivityDesigner, e: ActivityDesignerPaintEventArgs) """
        ...

    def OnProcessMessage(self, *args): #cannot find CLR method
        """ OnProcessMessage(self: ActivityDesigner, message: Message) """
        ...

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """ OnQueryContinueDrag(self: ActivityDesigner, e: QueryContinueDragEventArgs) """
        ...

    def OnResizing(self, *args): #cannot find CLR method
        """ OnResizing(self: ActivityDesigner, e: ActivityDesignerResizeEventArgs) """
        ...

    def OnScroll(self, *args): #cannot find CLR method
        """ OnScroll(self: ActivityDesigner, sender: ScrollBar, value: int) """
        ...

    def OnShowSmartTagVerbs(self, *args): #cannot find CLR method
        """ OnShowSmartTagVerbs(self: ActivityDesigner, smartTagPoint: Point) """
        ...

    def OnSmartTagVisibilityChanged(self, *args): #cannot find CLR method
        """ OnSmartTagVisibilityChanged(self: ActivityDesigner, visible: bool) """
        ...

    def OnThemeChange(self, *args): #cannot find CLR method
        """ OnThemeChange(self: ActivityDesigner, newTheme: ActivityDesignerTheme) """
        ...

    def PerformLayout(self, *args): #cannot find CLR method
        """ PerformLayout(self: ActivityDesigner) """
        ...

    def PointToLogical(self, *args): #cannot find CLR method
        """ PointToLogical(self: ActivityDesigner, point: Point) -> Point """
        ...

    def PointToScreen(self, *args): #cannot find CLR method
        """ PointToScreen(self: ActivityDesigner, point: Point) -> Point """
        ...

    def RectangleToLogical(self, *args): #cannot find CLR method
        """ RectangleToLogical(self: ActivityDesigner, rectangle: Rectangle) -> Rectangle """
        ...

    def RectangleToScreen(self, *args): #cannot find CLR method
        """ RectangleToScreen(self: ActivityDesigner, rectangle: Rectangle) -> Rectangle """
        ...

    def RefreshDesignerActions(self, *args): #cannot find CLR method
        """ RefreshDesignerActions(self: ActivityDesigner) """
        ...

    def RefreshDesignerVerbs(self, *args): #cannot find CLR method
        """ RefreshDesignerVerbs(self: ActivityDesigner) """
        ...

    def ShowInfoTip(self, *args): #cannot find CLR method
        """ ShowInfoTip(self: ActivityDesigner, title: str, infoTip: str)ShowInfoTip(self: ActivityDesigner, infoTip: str) """
        ...

    def ShowInPlaceTip(self, *args): #cannot find CLR method
        """ ShowInPlaceTip(self: ActivityDesigner, infoTip: str, rectangle: Rectangle) """
        ...


class ActivityDesignerAccessibleObject(AccessibleObject): # skipped bases: <type 'IInvokeProvider'>, <type 'IValueProvider'>, <type 'IRawElementProviderFragment'>, <type 'IRawElementProviderFragmentRoot'>, <type 'IRawElementProviderSimple'>, <type 'IRangeValueProvider'>, <type 'IOleWindow'>, <type 'IAccessibleEx'>, <type 'IGridProvider'>, <type 'ISelectionItemProvider'>, <type 'IReflect'>, <type 'IMarshal'>, <type 'ISelectionProvider'>, <type 'IServiceProvider'>, <type 'IScrollItemProvider'>, <type 'ITableProvider'>, <type 'IExpandCollapseProvider'>, <type 'IToggleProvider'>, <type 'ILegacyIAccessibleProvider'>, <type 'IGridItemProvider'>, <type 'IEnumVariant'>, <type 'IAccessible'>, <type 'ITableItemProvider'>, <type 'IRawElementProviderHwndOverride'>, <type 'object'>
    """ ActivityDesignerAccessibleObject(activityDesigner: ActivityDesigner) """
    @property
    def ActivityDesigner(self):
        ...


    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: ActivityDesignerAccessibleObject, serviceType: Type) -> object """
        ...

    def __new__(cls, activityDesigner:ActivityDesigner) -> Self:
        """ __new__(cls: type, activityDesigner: ActivityDesigner) """
        ...


class ActivityDesignerGlyphCollection(List): # skipped bases: <type 'IEnumerable[DesignerGlyph]'>, <type 'IReadOnlyCollection[DesignerGlyph]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[DesignerGlyph]'>, <type 'IReadOnlyList[DesignerGlyph]'>, <type 'IList[DesignerGlyph]'>, <type 'ICollection'>, <type 'object'>
    """
    ActivityDesignerGlyphCollection()
    ActivityDesignerGlyphCollection(glyphs: IEnumerable[DesignerGlyph])
    ActivityDesignerGlyphCollection(glyphs: ActivityDesignerGlyphCollection)
    """
    pass

class ActivityDesignerLayoutEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActivityDesignerLayoutEventArgs(graphics: Graphics, designerTheme: ActivityDesignerTheme) """
    @property
    def AmbientTheme(self) -> AmbientTheme:
        """ Get: AmbientTheme(self: ActivityDesignerLayoutEventArgs) -> AmbientTheme """
        ...

    @property
    def DesignerTheme(self) -> ActivityDesignerTheme:
        """ Get: DesignerTheme(self: ActivityDesignerLayoutEventArgs) -> ActivityDesignerTheme """
        ...

    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: ActivityDesignerLayoutEventArgs) -> Graphics """
        ...


    def __new__(cls, graphics:Graphics, designerTheme:ActivityDesignerTheme) -> Self:
        """ __new__(cls: type, graphics: Graphics, designerTheme: ActivityDesignerTheme) """
        ...


class ActivityDesignerLayoutSerializer(WorkflowMarkupSerializer): # skipped bases: <type 'object'>
    """ ActivityDesignerLayoutSerializer() """
    pass

class ActivityDesignerPaint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Draw3DButton(graphics:Graphics, image:Image, bounds:Rectangle, transparency:Single, buttonState): # ->  # Not found arg types: {'buttonState': 'ButtonState'}
        """ Draw3DButton(graphics: Graphics, image: Image, bounds: Rectangle, transparency: Single, buttonState: ButtonState) """
        ...

    @staticmethod
    def DrawExpandButton(graphics:Graphics, boundingRect:Rectangle, drawExpanded:bool, compositeDesignerTheme:CompositeDesignerTheme): # -> 
        """ DrawExpandButton(graphics: Graphics, boundingRect: Rectangle, drawExpanded: bool, compositeDesignerTheme: CompositeDesignerTheme) """
        ...

    @staticmethod
    def DrawImage(graphics:Graphics, image:Image, destination:Rectangle, *__args:DesignerContentAlignment): # -> 
        """ DrawImage(graphics: Graphics, image: Image, destination: Rectangle, alignment: DesignerContentAlignment)DrawImage(graphics: Graphics, image: Image, destination: Rectangle, source: Rectangle, alignment: DesignerContentAlignment, transparency: Single, grayscale: bool) """
        ...

    @staticmethod
    def DrawRoundedRectangle(graphics:Graphics, drawingPen:Pen, rectangle:Rectangle, radius:int): # -> 
        """ DrawRoundedRectangle(graphics: Graphics, drawingPen: Pen, rectangle: Rectangle, radius: int) """
        ...

    @staticmethod
    def DrawText(graphics:Graphics, font:Font, text:str, boundingRect:Rectangle, alignment:StringAlignment, textQuality:TextQuality, textBrush:Brush): # -> 
        """ DrawText(graphics: Graphics, font: Font, text: str, boundingRect: Rectangle, alignment: StringAlignment, textQuality: TextQuality, textBrush: Brush) """
        ...

    @staticmethod
    def GetRoundedRectanglePath(rectangle:Rectangle, radius:int) -> GraphicsPath:
        """ GetRoundedRectanglePath(rectangle: Rectangle, radius: int) -> GraphicsPath """
        ...

    __all__: list = ...


class ActivityDesignerPaintEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActivityDesignerPaintEventArgs(graphics: Graphics, clipRectangle: Rectangle, viewPort: Rectangle, designerTheme: ActivityDesignerTheme) """
    @property
    def AmbientTheme(self) -> AmbientTheme:
        """ Get: AmbientTheme(self: ActivityDesignerPaintEventArgs) -> AmbientTheme """
        ...

    @property
    def ClipRectangle(self) -> Rectangle:
        """ Get: ClipRectangle(self: ActivityDesignerPaintEventArgs) -> Rectangle """
        ...

    @property
    def DesignerTheme(self) -> ActivityDesignerTheme:
        """ Get: DesignerTheme(self: ActivityDesignerPaintEventArgs) -> ActivityDesignerTheme """
        ...

    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: ActivityDesignerPaintEventArgs) -> Graphics """
        ...


    def __new__(cls, graphics:Graphics, clipRectangle:Rectangle, viewPort:Rectangle, designerTheme:ActivityDesignerTheme) -> Self:
        """ __new__(cls: type, graphics: Graphics, clipRectangle: Rectangle, viewPort: Rectangle, designerTheme: ActivityDesignerTheme) """
        ...


class ActivityDesignerResizeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActivityDesignerResizeEventArgs(sizingEdge: DesignerEdges, newBounds: Rectangle) """
    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: ActivityDesignerResizeEventArgs) -> Rectangle """
        ...

    @property
    def SizingEdge(self) -> DesignerEdges:
        """ Get: SizingEdge(self: ActivityDesignerResizeEventArgs) -> DesignerEdges """
        ...


    def __new__(cls, sizingEdge:DesignerEdges, newBounds:Rectangle) -> Self:
        """ __new__(cls: type, sizingEdge: DesignerEdges, newBounds: Rectangle) """
        ...


class DesignerTheme(IPropertyValueProvider, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplyTo(self) -> str:
        """
        Get: ApplyTo(self: DesignerTheme) -> str
        Set: ApplyTo(self: DesignerTheme) = value
        """
        ...

    @property
    def ContainingTheme(self):
        ...

    @property
    def DesignerType(self) -> Type:
        """
        Get: DesignerType(self: DesignerTheme) -> Type
        Set: DesignerType(self: DesignerTheme) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """ Get: ReadOnly(self: DesignerTheme) -> bool """
        ...


    def Initialize(self): # -> 
        """ Initialize(self: DesignerTheme) """
        ...

    def OnAmbientPropertyChanged(self, ambientProperty:AmbientProperty): # -> 
        """ OnAmbientPropertyChanged(self: DesignerTheme, ambientProperty: AmbientProperty) """
        ...


class ActivityDesignerTheme(DesignerTheme): # skipped bases: <type 'IDisposable'>, <type 'IPropertyValueProvider'>, <type 'object'>
    """ ActivityDesignerTheme(theme: WorkflowTheme) """
    @property
    def BackColorEnd(self) -> Color:
        """
        Get: BackColorEnd(self: ActivityDesignerTheme) -> Color
        Set: BackColorEnd(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def BackColorStart(self) -> Color:
        """
        Get: BackColorStart(self: ActivityDesignerTheme) -> Color
        Set: BackColorStart(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def BackgroundStyle(self) -> LinearGradientMode:
        """
        Get: BackgroundStyle(self: ActivityDesignerTheme) -> LinearGradientMode
        Set: BackgroundStyle(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def BoldFont(self) -> Font:
        """ Get: BoldFont(self: ActivityDesignerTheme) -> Font """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: ActivityDesignerTheme) -> Color
        Set: BorderColor(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def BorderPen(self) -> Pen:
        """ Get: BorderPen(self: ActivityDesignerTheme) -> Pen """
        ...

    @property
    def BorderStyle(self) -> DashStyle:
        """
        Get: BorderStyle(self: ActivityDesignerTheme) -> DashStyle
        Set: BorderStyle(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def BorderWidth(self) -> int:
        """ Get: BorderWidth(self: ActivityDesignerTheme) -> int """
        ...

    @property
    def DesignerGeometry(self) -> DesignerGeometry:
        """ Get: DesignerGeometry(self: ActivityDesignerTheme) -> DesignerGeometry """
        ...

    @property
    def DesignerImage(self) -> Image:
        """ Get: DesignerImage(self: ActivityDesignerTheme) -> Image """
        ...

    @property
    def DesignerImagePath(self) -> str:
        """
        Get: DesignerImagePath(self: ActivityDesignerTheme) -> str
        Set: DesignerImagePath(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ActivityDesignerTheme) -> Font """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: ActivityDesignerTheme) -> Color
        Set: ForeColor(self: ActivityDesignerTheme) = value
        """
        ...

    @property
    def ForegroundBrush(self) -> Brush:
        """ Get: ForegroundBrush(self: ActivityDesignerTheme) -> Brush """
        ...

    @property
    def ForegroundPen(self) -> Pen:
        """ Get: ForegroundPen(self: ActivityDesignerTheme) -> Pen """
        ...

    @property
    def ImageSize(self) -> Size:
        """ Get: ImageSize(self: ActivityDesignerTheme) -> Size """
        ...

    @property
    def Size(self) -> Size:
        """ Get: Size(self: ActivityDesignerTheme) -> Size """
        ...


    def GetBackgroundBrush(self, rectangle:Rectangle) -> Brush:
        """ GetBackgroundBrush(self: ActivityDesignerTheme, rectangle: Rectangle) -> Brush """
        ...


class ActivityDesignerThemeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ActivityDesignerThemeAttribute(designerThemeType: Type) """
    @property
    def DesignerThemeType(self) -> Type:
        """ Get: DesignerThemeType(self: ActivityDesignerThemeAttribute) -> Type """
        ...

    @property
    def Xml(self) -> str:
        """
        Get: Xml(self: ActivityDesignerThemeAttribute) -> str
        Set: Xml(self: ActivityDesignerThemeAttribute) = value
        """
        ...


    def __new__(cls, designerThemeType:Type) -> Self:
        """ __new__(cls: type, designerThemeType: Type) """
        ...


class ActivityDesignerVerb(DesignerVerb): # skipped bases: <type 'object'>
    """
    ActivityDesignerVerb(activityDesigner: ActivityDesigner, verbGroup: DesignerVerbGroup, text: str, invokeHandler: EventHandler)
    ActivityDesignerVerb(activityDesigner: ActivityDesigner, verbGroup: DesignerVerbGroup, text: str, invokeHandler: EventHandler, statusHandler: EventHandler)
    """
    @property
    def CommandID(self) -> CommandID:
        """ Get: CommandID(self: ActivityDesignerVerb) -> CommandID """
        ...

    @property
    def Group(self) -> DesignerVerbGroup:
        """ Get: Group(self: ActivityDesignerVerb) -> DesignerVerbGroup """
        ...

    @property
    def OleStatus(self) -> int:
        """ Get: OleStatus(self: ActivityDesignerVerb) -> int """
        ...



class ActivityDesignerVerbCollection(DesignerVerbCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    ActivityDesignerVerbCollection()
    ActivityDesignerVerbCollection(verbs: IEnumerable[ActivityDesignerVerb])
    """
    pass

class ActivityDragEventArgs(DragEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Activities(self) -> ReadOnlyCollection:
        """ Get: Activities(self: ActivityDragEventArgs) -> ReadOnlyCollection[Activity] """
        ...

    @property
    def DragImageSnapPoint(self) -> Point:
        """
        Get: DragImageSnapPoint(self: ActivityDragEventArgs) -> Point
        Set: DragImageSnapPoint(self: ActivityDragEventArgs) = value
        """
        ...

    @property
    def DragInitiationPoint(self) -> Point:
        """ Get: DragInitiationPoint(self: ActivityDragEventArgs) -> Point """
        ...



class CompositeActivityDesigner(ActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ no doc """
    @property
    def CanExpandCollapse(self) -> bool:
        """ Get: CanExpandCollapse(self: CompositeActivityDesigner) -> bool """
        ...

    @property
    def ContainedDesigners(self) -> ReadOnlyCollection:
        """ Get: ContainedDesigners(self: CompositeActivityDesigner) -> ReadOnlyCollection[ActivityDesigner] """
        ...

    @property
    def ExpandButtonRectangle(self):
        ...

    @property
    def Expanded(self) -> bool:
        """
        Get: Expanded(self: CompositeActivityDesigner) -> bool
        Set: Expanded(self: CompositeActivityDesigner) = value
        """
        ...

    @property
    def FirstSelectableObject(self) -> object:
        """ Get: FirstSelectableObject(self: CompositeActivityDesigner) -> object """
        ...

    @property
    def IsEditable(self) -> bool:
        """ Get: IsEditable(self: CompositeActivityDesigner) -> bool """
        ...

    @property
    def LastSelectableObject(self) -> object:
        """ Get: LastSelectableObject(self: CompositeActivityDesigner) -> object """
        ...

    @property
    def TitleHeight(self):
        ...


    def CanInsertActivities(self, insertLocation:HitTestInfo, activitiesToInsert:ReadOnlyCollection) -> bool:
        """ CanInsertActivities(self: CompositeActivityDesigner, insertLocation: HitTestInfo, activitiesToInsert: ReadOnlyCollection[Activity]) -> bool """
        ...

    def CanMoveActivities(self, moveLocation:HitTestInfo, activitiesToMove:ReadOnlyCollection) -> bool:
        """ CanMoveActivities(self: CompositeActivityDesigner, moveLocation: HitTestInfo, activitiesToMove: ReadOnlyCollection[Activity]) -> bool """
        ...

    def CanRemoveActivities(self, activitiesToRemove:ReadOnlyCollection) -> bool:
        """ CanRemoveActivities(self: CompositeActivityDesigner, activitiesToRemove: ReadOnlyCollection[Activity]) -> bool """
        ...

    @staticmethod
    def DeserializeActivitiesFromDataObject(serviceProvider:IServiceProvider, dataObj:IDataObject) -> Array:
        """ DeserializeActivitiesFromDataObject(serviceProvider: IServiceProvider, dataObj: IDataObject) -> Array[Activity] """
        ...

    def EnsureVisibleContainedDesigner(self, containedDesigner:ActivityDesigner): # -> 
        """ EnsureVisibleContainedDesigner(self: CompositeActivityDesigner, containedDesigner: ActivityDesigner) """
        ...

    @staticmethod
    def GetIntersectingDesigners(topLevelDesigner:ActivityDesigner, rectangle:Rectangle) -> Array:
        """ GetIntersectingDesigners(topLevelDesigner: ActivityDesigner, rectangle: Rectangle) -> Array[ActivityDesigner] """
        ...

    def GetNextSelectableObject(self, current:object, direction:DesignerNavigationDirection) -> object:
        """ GetNextSelectableObject(self: CompositeActivityDesigner, current: object, direction: DesignerNavigationDirection) -> object """
        ...

    @staticmethod
    def InsertActivities(*__args): # -> 
        """ InsertActivities(compositeActivityDesigner: CompositeActivityDesigner, insertLocation: HitTestInfo, activitiesToInsert: ReadOnlyCollection[Activity], undoTransactionDescription: str)InsertActivities(self: CompositeActivityDesigner, insertLocation: HitTestInfo, activitiesToInsert: ReadOnlyCollection[Activity]) """
        ...

    def IsContainedDesignerVisible(self, containedDesigner:ActivityDesigner) -> bool:
        """ IsContainedDesignerVisible(self: CompositeActivityDesigner, containedDesigner: ActivityDesigner) -> bool """
        ...

    def MoveActivities(self, moveLocation:HitTestInfo, activitiesToMove:ReadOnlyCollection): # -> 
        """ MoveActivities(self: CompositeActivityDesigner, moveLocation: HitTestInfo, activitiesToMove: ReadOnlyCollection[Activity]) """
        ...

    @staticmethod
    def MoveDesigners(activityDesigner:ActivityDesigner, moveBack:bool): # -> 
        """ MoveDesigners(activityDesigner: ActivityDesigner, moveBack: bool) """
        ...

    def OnContainedActivitiesChanged(self, *args): #cannot find CLR method
        """ OnContainedActivitiesChanged(self: CompositeActivityDesigner, listChangeArgs: ActivityCollectionChangeEventArgs) """
        ...

    def OnContainedActivitiesChanging(self, *args): #cannot find CLR method
        """ OnContainedActivitiesChanging(self: CompositeActivityDesigner, listChangeArgs: ActivityCollectionChangeEventArgs) """
        ...

    def OnContainedActivityChanged(self, *args): #cannot find CLR method
        """ OnContainedActivityChanged(self: CompositeActivityDesigner, e: ActivityChangedEventArgs) """
        ...

    def PaintContainedDesigners(self, *args): #cannot find CLR method
        """ PaintContainedDesigners(self: CompositeActivityDesigner, e: ActivityDesignerPaintEventArgs) """
        ...

    @staticmethod
    def RemoveActivities(*__args): # -> 
        """ RemoveActivities(serviceProvider: IServiceProvider, activitiesToRemove: ReadOnlyCollection[Activity], transactionDescription: str)RemoveActivities(self: CompositeActivityDesigner, activitiesToRemove: ReadOnlyCollection[Activity]) """
        ...

    @staticmethod
    def SerializeActivitiesToDataObject(serviceProvider:IServiceProvider, activities:Array) -> IDataObject:
        """ SerializeActivitiesToDataObject(serviceProvider: IServiceProvider, activities: Array[Activity]) -> IDataObject """
        ...


class StructuredCompositeActivityDesigner(CompositeActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ no doc """
    @property
    def ActiveView(self) -> DesignerView:
        """
        Get: ActiveView(self: StructuredCompositeActivityDesigner) -> DesignerView
        Set: ActiveView(self: StructuredCompositeActivityDesigner) = value
        """
        ...

    @property
    def CurrentDropTarget(self):
        ...

    @property
    def MinimumSize(self) -> Size:
        """ Get: MinimumSize(self: StructuredCompositeActivityDesigner) -> Size """
        ...

    @property
    def Views(self) -> ReadOnlyCollection:
        """ Get: Views(self: StructuredCompositeActivityDesigner) -> ReadOnlyCollection[DesignerView] """
        ...


    def DrawConnectors(self, *args): #cannot find CLR method
        """ DrawConnectors(self: StructuredCompositeActivityDesigner, graphics: Graphics, pen: Pen, points: Array[Point], startCap: LineAnchor, endCap: LineAnchor) """
        ...

    def GetDropTargets(self, *args): #cannot find CLR method
        """ GetDropTargets(self: StructuredCompositeActivityDesigner, dropPoint: Point) -> Array[Rectangle] """
        ...

    def GetInnerConnections(self, *args): #cannot find CLR method
        """ GetInnerConnections(self: StructuredCompositeActivityDesigner, edges: DesignerEdges) -> ReadOnlyCollection[Point] """
        ...

    def OnViewChanged(self, *args): #cannot find CLR method
        """ OnViewChanged(self: StructuredCompositeActivityDesigner, view: DesignerView) """
        ...


class SequentialActivityDesigner(StructuredCompositeActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ SequentialActivityDesigner() """
    @property
    def AccessibilityObject(self): # -> AccessibleObject
        """ Get: AccessibilityObject(self: SequentialActivityDesigner) -> AccessibleObject """
        ...

    @property
    def CanExpandCollapse(self) -> bool:
        """ Get: CanExpandCollapse(self: SequentialActivityDesigner) -> bool """
        ...

    @property
    def Expanded(self) -> bool:
        """
        Get: Expanded(self: SequentialActivityDesigner) -> bool
        Set: Expanded(self: SequentialActivityDesigner) = value
        """
        ...

    @property
    def HelpText(self):
        ...

    @property
    def HelpTextRectangle(self):
        ...

    @property
    def HelpTextSize(self):
        ...


    def GetConnectors(self, *args): #cannot find CLR method
        """ GetConnectors(self: SequentialActivityDesigner) -> Array[Rectangle] """
        ...

    def HitTest(self, point:Point) -> HitTestInfo:
        """ HitTest(self: SequentialActivityDesigner, point: Point) -> HitTestInfo """
        ...


class ActivityPreviewDesigner(SequentialActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ ActivityPreviewDesigner() """
    @property
    def ContainedDesigners(self) -> ReadOnlyCollection:
        """ Get: ContainedDesigners(self: ActivityPreviewDesigner) -> ReadOnlyCollection[ActivityDesigner] """
        ...

    @property
    def Location(self) -> Point:
        """
        Get: Location(self: ActivityPreviewDesigner) -> Point
        Set: Location(self: ActivityPreviewDesigner) = value
        """
        ...

    @property
    def PreviewedDesigner(self) -> ActivityDesigner:
        """ Get: PreviewedDesigner(self: ActivityPreviewDesigner) -> ActivityDesigner """
        ...

    @property
    def ShowPreview(self) -> bool:
        """
        Get: ShowPreview(self: ActivityPreviewDesigner) -> bool
        Set: ShowPreview(self: ActivityPreviewDesigner) = value
        """
        ...


    def EnsureVisibleContainedDesigner(self, containedDesigner:ActivityDesigner): # -> 
        """ EnsureVisibleContainedDesigner(self: ActivityPreviewDesigner, containedDesigner: ActivityDesigner) """
        ...

    def IsContainedDesignerVisible(self, containedDesigner:ActivityDesigner) -> bool:
        """ IsContainedDesignerVisible(self: ActivityPreviewDesigner, containedDesigner: ActivityDesigner) -> bool """
        ...

    def RefreshPreview(self): # -> 
        """ RefreshPreview(self: ActivityPreviewDesigner) """
        ...


class CompositeDesignerTheme(ActivityDesignerTheme): # skipped bases: <type 'IDisposable'>, <type 'IPropertyValueProvider'>, <type 'object'>
    """ CompositeDesignerTheme(theme: WorkflowTheme) """
    @property
    def ConnectorEndCap(self) -> LineAnchor:
        """
        Get: ConnectorEndCap(self: CompositeDesignerTheme) -> LineAnchor
        Set: ConnectorEndCap(self: CompositeDesignerTheme) = value
        """
        ...

    @property
    def ConnectorSize(self) -> Size:
        """ Get: ConnectorSize(self: CompositeDesignerTheme) -> Size """
        ...

    @property
    def ConnectorStartCap(self) -> LineAnchor:
        """
        Get: ConnectorStartCap(self: CompositeDesignerTheme) -> LineAnchor
        Set: ConnectorStartCap(self: CompositeDesignerTheme) = value
        """
        ...

    @property
    def ExpandButtonSize(self) -> Size:
        """ Get: ExpandButtonSize(self: CompositeDesignerTheme) -> Size """
        ...

    @property
    def ShowDropShadow(self) -> bool:
        """
        Get: ShowDropShadow(self: CompositeDesignerTheme) -> bool
        Set: ShowDropShadow(self: CompositeDesignerTheme) = value
        """
        ...

    @property
    def WatermarkAlignment(self) -> DesignerContentAlignment:
        """
        Get: WatermarkAlignment(self: CompositeDesignerTheme) -> DesignerContentAlignment
        Set: WatermarkAlignment(self: CompositeDesignerTheme) = value
        """
        ...

    @property
    def WatermarkImage(self) -> Image:
        """ Get: WatermarkImage(self: CompositeDesignerTheme) -> Image """
        ...

    @property
    def WatermarkImagePath(self) -> str:
        """
        Get: WatermarkImagePath(self: CompositeDesignerTheme) -> str
        Set: WatermarkImagePath(self: CompositeDesignerTheme) = value
        """
        ...


    def GetExpandButtonBackgroundBrush(self, rectangle:Rectangle) -> Brush:
        """ GetExpandButtonBackgroundBrush(self: CompositeDesignerTheme, rectangle: Rectangle) -> Brush """
        ...


class ActivityPreviewDesignerTheme(CompositeDesignerTheme): # skipped bases: <type 'IDisposable'>, <type 'IPropertyValueProvider'>, <type 'object'>
    """ ActivityPreviewDesignerTheme(theme: WorkflowTheme) """
    @property
    def PreviewBackColor(self) -> Color:
        """
        Get: PreviewBackColor(self: ActivityPreviewDesignerTheme) -> Color
        Set: PreviewBackColor(self: ActivityPreviewDesignerTheme) = value
        """
        ...

    @property
    def PreviewBorderColor(self) -> Color:
        """
        Get: PreviewBorderColor(self: ActivityPreviewDesignerTheme) -> Color
        Set: PreviewBorderColor(self: ActivityPreviewDesignerTheme) = value
        """
        ...

    @property
    def PreviewForeColor(self) -> Color:
        """
        Get: PreviewForeColor(self: ActivityPreviewDesignerTheme) -> Color
        Set: PreviewForeColor(self: ActivityPreviewDesignerTheme) = value
        """
        ...



class ActivityToolboxItem(ToolboxItem): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """
    ActivityToolboxItem()
    ActivityToolboxItem(type: Type)
    """
    def CreateComponentsWithUI(self, host:IDesignerHost) -> Array:
        """ CreateComponentsWithUI(self: ActivityToolboxItem, host: IDesignerHost) -> Array[IComponent] """
        ...

    @staticmethod
    def GetToolboxDisplayName(activityType:Type) -> str:
        """ GetToolboxDisplayName(activityType: Type) -> str """
        ...

    @staticmethod
    def GetToolboxImage(activityType:Type) -> Image:
        """ GetToolboxImage(activityType: Type) -> Image """
        ...


class AmbientProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AmbientProperty, values: DesignerSize (0), OperatingSystemSetting (1) """
    DesignerSize: AmbientProperty = ...
    OperatingSystemSetting: AmbientProperty = ...
    value__ = ...


class AmbientTheme(DesignerTheme): # skipped bases: <type 'IDisposable'>, <type 'IPropertyValueProvider'>, <type 'object'>
    """ AmbientTheme(theme: WorkflowTheme) """
    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: AmbientTheme) -> Color
        Set: BackColor(self: AmbientTheme) = value
        """
        ...

    @property
    def BackgroundBrush(self) -> Brush:
        """ Get: BackgroundBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def BoldFont(self) -> Font:
        """ Get: BoldFont(self: AmbientTheme) -> Font """
        ...

    @property
    def BorderWidth(self) -> int:
        """ Get: BorderWidth(self: AmbientTheme) -> int """
        ...

    @property
    def CommentIndicatorBrush(self) -> Brush:
        """ Get: CommentIndicatorBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def CommentIndicatorColor(self) -> Color:
        """
        Get: CommentIndicatorColor(self: AmbientTheme) -> Color
        Set: CommentIndicatorColor(self: AmbientTheme) = value
        """
        ...

    @property
    def CommentIndicatorPen(self) -> Pen:
        """ Get: CommentIndicatorPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def DesignerSize(self) -> DesignerSize:
        """
        Get: DesignerSize(self: AmbientTheme) -> DesignerSize
        Set: DesignerSize(self: AmbientTheme) = value
        """
        ...

    @property
    def DrawGrayscale(self) -> bool:
        """
        Get: DrawGrayscale(self: AmbientTheme) -> bool
        Set: DrawGrayscale(self: AmbientTheme) = value
        """
        ...

    @property
    def DrawRounded(self) -> bool:
        """
        Get: DrawRounded(self: AmbientTheme) -> bool
        Set: DrawRounded(self: AmbientTheme) = value
        """
        ...

    @property
    def DrawShadow(self) -> bool:
        """
        Get: DrawShadow(self: AmbientTheme) -> bool
        Set: DrawShadow(self: AmbientTheme) = value
        """
        ...

    @property
    def DropIndicatorBrush(self) -> Brush:
        """ Get: DropIndicatorBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def DropIndicatorColor(self) -> Color:
        """
        Get: DropIndicatorColor(self: AmbientTheme) -> Color
        Set: DropIndicatorColor(self: AmbientTheme) = value
        """
        ...

    @property
    def DropIndicatorPen(self) -> Pen:
        """ Get: DropIndicatorPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: AmbientTheme) -> Font """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: AmbientTheme) -> str
        Set: FontName(self: AmbientTheme) = value
        """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: AmbientTheme) -> Color
        Set: ForeColor(self: AmbientTheme) = value
        """
        ...

    @property
    def ForegroundBrush(self) -> Brush:
        """ Get: ForegroundBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def ForegroundPen(self) -> Pen:
        """ Get: ForegroundPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def GlyphSize(self) -> Size:
        """ Get: GlyphSize(self: AmbientTheme) -> Size """
        ...

    @property
    def GridColor(self) -> Color:
        """
        Get: GridColor(self: AmbientTheme) -> Color
        Set: GridColor(self: AmbientTheme) = value
        """
        ...

    @property
    def GridSize(self) -> Size:
        """ Get: GridSize(self: AmbientTheme) -> Size """
        ...

    @property
    def GridStyle(self) -> DashStyle:
        """
        Get: GridStyle(self: AmbientTheme) -> DashStyle
        Set: GridStyle(self: AmbientTheme) = value
        """
        ...

    @property
    def MajorGridBrush(self) -> Brush:
        """ Get: MajorGridBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def MajorGridPen(self) -> Pen:
        """ Get: MajorGridPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def Margin(self) -> Size:
        """ Get: Margin(self: AmbientTheme) -> Size """
        ...

    @property
    def MinorGridPen(self) -> Pen:
        """ Get: MinorGridPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def ReadonlyIndicatorBrush(self) -> Brush:
        """ Get: ReadonlyIndicatorBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def ReadonlyIndicatorColor(self) -> Color:
        """
        Get: ReadonlyIndicatorColor(self: AmbientTheme) -> Color
        Set: ReadonlyIndicatorColor(self: AmbientTheme) = value
        """
        ...

    @property
    def SelectionForeColor(self) -> Color:
        """
        Get: SelectionForeColor(self: AmbientTheme) -> Color
        Set: SelectionForeColor(self: AmbientTheme) = value
        """
        ...

    @property
    def SelectionForegroundBrush(self) -> Brush:
        """ Get: SelectionForegroundBrush(self: AmbientTheme) -> Brush """
        ...

    @property
    def SelectionForegroundPen(self) -> Pen:
        """ Get: SelectionForegroundPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def SelectionPatternColor(self) -> Color:
        """
        Get: SelectionPatternColor(self: AmbientTheme) -> Color
        Set: SelectionPatternColor(self: AmbientTheme) = value
        """
        ...

    @property
    def SelectionPatternPen(self) -> Pen:
        """ Get: SelectionPatternPen(self: AmbientTheme) -> Pen """
        ...

    @property
    def SelectionSize(self) -> Size:
        """ Get: SelectionSize(self: AmbientTheme) -> Size """
        ...

    @property
    def ShowConfigErrors(self) -> bool:
        """
        Get: ShowConfigErrors(self: AmbientTheme) -> bool
        Set: ShowConfigErrors(self: AmbientTheme) = value
        """
        ...

    @property
    def ShowDesignerBorder(self) -> bool:
        """
        Get: ShowDesignerBorder(self: AmbientTheme) -> bool
        Set: ShowDesignerBorder(self: AmbientTheme) = value
        """
        ...

    @property
    def ShowGrid(self) -> bool:
        """
        Get: ShowGrid(self: AmbientTheme) -> bool
        Set: ShowGrid(self: AmbientTheme) = value
        """
        ...

    @property
    def TextQuality(self) -> TextQuality:
        """
        Get: TextQuality(self: AmbientTheme) -> TextQuality
        Set: TextQuality(self: AmbientTheme) = value
        """
        ...

    @property
    def UseOperatingSystemSettings(self) -> bool:
        """ Get: UseOperatingSystemSettings(self: AmbientTheme) -> bool """
        ...

    @property
    def WatermarkAlignment(self) -> DesignerContentAlignment:
        """
        Get: WatermarkAlignment(self: AmbientTheme) -> DesignerContentAlignment
        Set: WatermarkAlignment(self: AmbientTheme) = value
        """
        ...

    @property
    def WatermarkImagePath(self) -> str:
        """
        Get: WatermarkImagePath(self: AmbientTheme) -> str
        Set: WatermarkImagePath(self: AmbientTheme) = value
        """
        ...

    @property
    def WorkflowWatermarkImage(self) -> Image:
        """ Get: WorkflowWatermarkImage(self: AmbientTheme) -> Image """
        ...



class BindUITypeEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ BindUITypeEditor() """
    pass

class DesignerGlyph: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanBeActivated(self) -> bool:
        """ Get: CanBeActivated(self: DesignerGlyph) -> bool """
        ...

    @property
    def Priority(self) -> int:
        """ Get: Priority(self: DesignerGlyph) -> int """
        ...


    def GetBounds(self, designer:ActivityDesigner, activated:bool) -> Rectangle:
        """ GetBounds(self: DesignerGlyph, designer: ActivityDesigner, activated: bool) -> Rectangle """
        ...

    def OnActivate(self, *args): #cannot find CLR method
        """ OnActivate(self: DesignerGlyph, designer: ActivityDesigner) """
        ...

    def OnPaint(self, *args): #cannot find CLR method
        """ OnPaint(self: DesignerGlyph, graphics: Graphics, activated: bool, ambientTheme: AmbientTheme, designer: ActivityDesigner) """
        ...

    HighestPriority: int = ...
    LowestPriority: int = ...
    NormalPriority: int = ...


class CommentGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ CommentGlyph() """
    pass

class CompositeActivityDesignerLayoutSerializer(ActivityDesignerLayoutSerializer): # skipped bases: <type 'object'>
    """ CompositeActivityDesignerLayoutSerializer() """
    pass

class CompositeDesignerAccessibleObject(ActivityDesignerAccessibleObject): # skipped bases: <type 'IInvokeProvider'>, <type 'IValueProvider'>, <type 'IRawElementProviderFragment'>, <type 'IRawElementProviderFragmentRoot'>, <type 'IRawElementProviderSimple'>, <type 'IRangeValueProvider'>, <type 'IOleWindow'>, <type 'IAccessibleEx'>, <type 'IGridProvider'>, <type 'ISelectionItemProvider'>, <type 'IServiceProvider'>, <type 'IMarshal'>, <type 'IReflect'>, <type 'ISelectionProvider'>, <type 'IScrollItemProvider'>, <type 'ITableProvider'>, <type 'IExpandCollapseProvider'>, <type 'IToggleProvider'>, <type 'ILegacyIAccessibleProvider'>, <type 'IGridItemProvider'>, <type 'IEnumVariant'>, <type 'IAccessible'>, <type 'ITableItemProvider'>, <type 'IRawElementProviderHwndOverride'>, <type 'object'>
    """ CompositeDesignerAccessibleObject(activityDesigner: CompositeActivityDesigner) """
    def GetChild(self, index:int): # -> AccessibleObject
        """ GetChild(self: CompositeDesignerAccessibleObject, index: int) -> AccessibleObject """
        ...

    def GetChildCount(self) -> int:
        """ GetChildCount(self: CompositeDesignerAccessibleObject) -> int """
        ...


class ConfigErrorGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ ConfigErrorGlyph() """
    pass

class ConnectionPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ ConnectionPoint(associatedDesigner: ActivityDesigner, designerEdge: DesignerEdges, connectionIndex: int) """
    @property
    def AssociatedDesigner(self) -> ActivityDesigner:
        """ Get: AssociatedDesigner(self: ConnectionPoint) -> ActivityDesigner """
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: ConnectionPoint) -> Rectangle """
        ...

    @property
    def ConnectionEdge(self) -> DesignerEdges:
        """ Get: ConnectionEdge(self: ConnectionPoint) -> DesignerEdges """
        ...

    @property
    def ConnectionIndex(self) -> int:
        """ Get: ConnectionIndex(self: ConnectionPoint) -> int """
        ...

    @property
    def Location(self) -> Point:
        """ Get: Location(self: ConnectionPoint) -> Point """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ConnectionPoint, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ConnectionPoint) -> int """
        ...

    def OnPaint(self, e:ActivityDesignerPaintEventArgs, drawHighlighted:bool): # -> 
        """ OnPaint(self: ConnectionPoint, e: ActivityDesignerPaintEventArgs, drawHighlighted: bool) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Connector(IDisposable): # skipped bases: <type 'object'>
    """ Connector(source: ConnectionPoint, target: ConnectionPoint) """
    @property
    def AccessibilityObject(self): # -> AccessibleObject
        """ Get: AccessibilityObject(self: Connector) -> AccessibleObject """
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: Connector) -> Rectangle """
        ...

    @property
    def ConnectorModified(self) -> bool:
        """ Get: ConnectorModified(self: Connector) -> bool """
        ...

    @property
    def ConnectorSegments(self) -> ReadOnlyCollection:
        """ Get: ConnectorSegments(self: Connector) -> ReadOnlyCollection[Point] """
        ...

    @property
    def ExcludedRoutingRectangles(self):
        ...

    @property
    def ParentDesigner(self) -> FreeformActivityDesigner:
        """ Get: ParentDesigner(self: Connector) -> FreeformActivityDesigner """
        ...

    @property
    def ParentView(self):
        ...

    @property
    def Source(self) -> ConnectionPoint:
        """
        Get: Source(self: Connector) -> ConnectionPoint
        Set: Source(self: Connector) = value
        """
        ...

    @property
    def Target(self) -> ConnectionPoint:
        """
        Get: Target(self: Connector) -> ConnectionPoint
        Set: Target(self: Connector) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Connector, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Connector) -> int """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: Connector, serviceType: Type) -> object """
        ...

    def HitTest(self, point:Point) -> bool:
        """ HitTest(self: Connector, point: Point) -> bool """
        ...

    def Invalidate(self): # -> 
        """ Invalidate(self: Connector) """
        ...

    def Offset(self, size:Size): # -> 
        """ Offset(self: Connector, size: Size) """
        ...

    def OnLayout(self, *args): #cannot find CLR method
        """ OnLayout(self: Connector, e: ActivityDesignerLayoutEventArgs) """
        ...

    def OnPaint(self, *args): #cannot find CLR method
        """ OnPaint(self: Connector, e: ActivityDesignerPaintEventArgs) """
        ...

    def OnPaintEdited(self, *args): #cannot find CLR method
        """ OnPaintEdited(self: Connector, e: ActivityDesignerPaintEventArgs, segments: Array[Point], segmentEditPoints: Array[Point]) """
        ...

    def OnPaintSelected(self, *args): #cannot find CLR method
        """ OnPaintSelected(self: Connector, e: ActivityDesignerPaintEventArgs, primarySelection: bool, segmentEditPoints: Array[Point]) """
        ...

    def PerformLayout(self, *args): #cannot find CLR method
        """ PerformLayout(self: Connector) """
        ...

    def SetConnectorSegments(self, *args): #cannot find CLR method
        """ SetConnectorSegments(self: Connector, segments: ICollection[Point]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectorAccessibleObject(AccessibleObject): # skipped bases: <type 'IInvokeProvider'>, <type 'IValueProvider'>, <type 'IRawElementProviderFragment'>, <type 'IRawElementProviderFragmentRoot'>, <type 'IRawElementProviderSimple'>, <type 'IRangeValueProvider'>, <type 'IOleWindow'>, <type 'IAccessibleEx'>, <type 'IGridProvider'>, <type 'ISelectionItemProvider'>, <type 'IReflect'>, <type 'IMarshal'>, <type 'ISelectionProvider'>, <type 'IServiceProvider'>, <type 'IScrollItemProvider'>, <type 'ITableProvider'>, <type 'IExpandCollapseProvider'>, <type 'IToggleProvider'>, <type 'ILegacyIAccessibleProvider'>, <type 'IGridItemProvider'>, <type 'IEnumVariant'>, <type 'IAccessible'>, <type 'ITableItemProvider'>, <type 'IRawElementProviderHwndOverride'>, <type 'object'>
    """ ConnectorAccessibleObject(connector: Connector) """
    def __new__(cls, connector:Connector) -> Self:
        """ __new__(cls: type, connector: Connector) """
        ...


class ConnectorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connector(self) -> Connector:
        """ Get: Connector(self: ConnectorEventArgs) -> Connector """
        ...



class ConnectorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ConnectorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ConnectorEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ConnectorEventHandler, sender: object, e: ConnectorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ConnectorEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ConnectorEventArgs): # -> 
        """ Invoke(self: ConnectorEventHandler, sender: object, e: ConnectorEventArgs) """
        ...


class HitTestInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ HitTestInfo(designer: ActivityDesigner, location: HitTestLocations) """
    @property
    def AssociatedDesigner(self) -> ActivityDesigner:
        """ Get: AssociatedDesigner(self: HitTestInfo) -> ActivityDesigner """
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: HitTestInfo) -> Rectangle """
        ...

    @property
    def HitLocation(self) -> HitTestLocations:
        """ Get: HitLocation(self: HitTestInfo) -> HitTestLocations """
        ...

    @property
    def Nowhere(self) -> HitTestInfo:
        """ Get: Nowhere() -> HitTestInfo """
        ...

    @property
    def SelectableObject(self) -> object:
        """ Get: SelectableObject(self: HitTestInfo) -> object """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: HitTestInfo) -> IDictionary """
        ...


    def MapToIndex(self) -> int:
        """ MapToIndex(self: HitTestInfo) -> int """
        ...



class ConnectorHitTestInfo(HitTestInfo): # skipped bases: <type 'object'>
    """ ConnectorHitTestInfo(compositeActivityDesigner: CompositeActivityDesigner, flags: HitTestLocations, connector: int) """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: ConnectorHitTestInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ConnectorHitTestInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectorLayoutSerializer(WorkflowMarkupSerializer): # skipped bases: <type 'object'>
    """ ConnectorLayoutSerializer() """
    def GetConnectorConstructionArguments(self, *args): #cannot find CLR method
        """ GetConnectorConstructionArguments(self: ConnectorLayoutSerializer, serializationManager: WorkflowMarkupSerializationManager, type: Type) -> Dictionary[str, str] """
        ...


class DesignerAction: # skipped bases: <type 'object'>, <type 'object'>
    """
    DesignerAction(activityDesigner: ActivityDesigner, actionId: int, text: str)
    DesignerAction(activityDesigner: ActivityDesigner, actionId: int, text: str, image: Image)
    """
    @property
    def ActionId(self) -> int:
        """ Get: ActionId(self: DesignerAction) -> int """
        ...

    @property
    def Image(self) -> Image:
        """ Get: Image(self: DesignerAction) -> Image """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: DesignerAction) -> str
        Set: PropertyName(self: DesignerAction) = value
        """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: DesignerAction) -> str """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: DesignerAction) -> IDictionary """
        ...


    def Invoke(self): # -> 
        """ Invoke(self: DesignerAction) """
        ...


class DesignerContentAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerContentAlignment, values: Bottom (8), BottomCenter (24), BottomLeft (9), BottomRight (12), Center (16), CenterLeft (17), CenterRight (20), Fill (32), Left (1), Right (4), Top (2), TopCenter (18), TopLeft (3), TopRight (6) """
    Bottom: DesignerContentAlignment = ...
    BottomCenter: DesignerContentAlignment = ...
    BottomLeft: DesignerContentAlignment = ...
    BottomRight: DesignerContentAlignment = ...
    Center: DesignerContentAlignment = ...
    CenterLeft: DesignerContentAlignment = ...
    CenterRight: DesignerContentAlignment = ...
    Fill: DesignerContentAlignment = ...
    Left: DesignerContentAlignment = ...
    Right: DesignerContentAlignment = ...
    Top: DesignerContentAlignment = ...
    TopCenter: DesignerContentAlignment = ...
    TopLeft: DesignerContentAlignment = ...
    TopRight: DesignerContentAlignment = ...
    value__ = ...


class DesignerEdges(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DesignerEdges, values: All (15), Bottom (8), Left (1), None (0), Right (4), Top (2) """
    All: DesignerEdges = ...
    Bottom: DesignerEdges = ...
    Left: DesignerEdges = ...
    Right: DesignerEdges = ...
    Top: DesignerEdges = ...
    value__ = ...


class DesignerGeometry(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerGeometry, values: Rectangle (0), RoundedRectangle (1) """
    Rectangle: DesignerGeometry = ...
    RoundedRectangle: DesignerGeometry = ...
    value__ = ...


class DesignerNavigationDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerNavigationDirection, values: Down (0), Left (2), Right (3), Up (1) """
    Down: DesignerNavigationDirection = ...
    Left: DesignerNavigationDirection = ...
    Right: DesignerNavigationDirection = ...
    Up: DesignerNavigationDirection = ...
    value__ = ...


class DesignerSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerSize, values: Large (2), Medium (1), Small (0) """
    Large: DesignerSize = ...
    Medium: DesignerSize = ...
    Small: DesignerSize = ...
    value__ = ...


class DesignerVerbGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerVerbGroup, values: Actions (4), Edit (2), General (0), Misc (5), Options (3), View (1) """
    Actions: DesignerVerbGroup = ...
    Edit: DesignerVerbGroup = ...
    General: DesignerVerbGroup = ...
    Misc: DesignerVerbGroup = ...
    Options: DesignerVerbGroup = ...
    value__ = ...
    View: DesignerVerbGroup = ...


class DesignerView: # skipped bases: <type 'object'>, <type 'object'>
    """
    DesignerView(viewId: int, text: str, image: Image)
    DesignerView(viewId: int, text: str, image: Image, associatedDesigner: ActivityDesigner)
    """
    @property
    def AssociatedDesigner(self) -> ActivityDesigner:
        """ Get: AssociatedDesigner(self: DesignerView) -> ActivityDesigner """
        ...

    @property
    def Image(self) -> Image:
        """ Get: Image(self: DesignerView) -> Image """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: DesignerView) -> str """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: DesignerView) -> IDictionary """
        ...

    @property
    def ViewId(self) -> int:
        """ Get: ViewId(self: DesignerView) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: DesignerView, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DesignerView) -> int """
        ...

    def OnActivate(self): # -> 
        """ OnActivate(self: DesignerView) """
        ...

    def OnDeactivate(self): # -> 
        """ OnDeactivate(self: DesignerView) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FreeformActivityDesigner(CompositeActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ FreeformActivityDesigner() """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: FreeformActivityDesigner) -> bool
        Set: AutoSize(self: FreeformActivityDesigner) = value
        """
        ...

    @property
    def AutoSizeMargin(self) -> Size:
        """
        Get: AutoSizeMargin(self: FreeformActivityDesigner) -> Size
        Set: AutoSizeMargin(self: FreeformActivityDesigner) = value
        """
        ...

    @property
    def AutoSizeMode(self): # -> AutoSizeMode
        """
        Get: AutoSizeMode(self: FreeformActivityDesigner) -> AutoSizeMode
        Set: AutoSizeMode(self: FreeformActivityDesigner) = value
        """
        ...

    @property
    def Connectors(self) -> ReadOnlyCollection:
        """ Get: Connectors(self: FreeformActivityDesigner) -> ReadOnlyCollection[Connector] """
        ...

    @property
    def EnableUserDrawnConnectors(self) -> bool:
        """
        Get: EnableUserDrawnConnectors(self: FreeformActivityDesigner) -> bool
        Set: EnableUserDrawnConnectors(self: FreeformActivityDesigner) = value
        """
        ...

    @property
    def MinimumSize(self) -> Size:
        """ Get: MinimumSize(self: FreeformActivityDesigner) -> Size """
        ...

    @property
    def ShowConnectorsInForeground(self):
        ...


    def AddConnector(self, source:ConnectionPoint, target:ConnectionPoint) -> Connector:
        """ AddConnector(self: FreeformActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) -> Connector """
        ...

    def BringToFront(self, containedDesigner:ActivityDesigner): # -> 
        """ BringToFront(self: FreeformActivityDesigner, containedDesigner: ActivityDesigner) """
        ...

    def CanConnectContainedDesigners(self, *args): #cannot find CLR method
        """ CanConnectContainedDesigners(self: FreeformActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) -> bool """
        ...

    def CanResizeContainedDesigner(self, *args): #cannot find CLR method
        """ CanResizeContainedDesigner(self: FreeformActivityDesigner, containedDesigner: ActivityDesigner) -> bool """
        ...

    def CreateConnector(self, *args): #cannot find CLR method
        """ CreateConnector(self: FreeformActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) -> Connector """
        ...

    def MoveContainedDesigner(self, containedDesigner:ActivityDesigner, newLocation:Point): # -> 
        """ MoveContainedDesigner(self: FreeformActivityDesigner, containedDesigner: ActivityDesigner, newLocation: Point) """
        ...

    def OnConnectorAdded(self, *args): #cannot find CLR method
        """ OnConnectorAdded(self: FreeformActivityDesigner, e: ConnectorEventArgs) """
        ...

    def OnConnectorChanged(self, *args): #cannot find CLR method
        """ OnConnectorChanged(self: FreeformActivityDesigner, e: ConnectorEventArgs) """
        ...

    def OnConnectorRemoved(self, *args): #cannot find CLR method
        """ OnConnectorRemoved(self: FreeformActivityDesigner, e: ConnectorEventArgs) """
        ...

    def OnContainedDesignersConnected(self, *args): #cannot find CLR method
        """ OnContainedDesignersConnected(self: FreeformActivityDesigner, source: ConnectionPoint, target: ConnectionPoint) """
        ...

    def RemoveConnector(self, connector:Connector): # -> 
        """ RemoveConnector(self: FreeformActivityDesigner, connector: Connector) """
        ...

    def ResizeContainedDesigner(self, containedDesigner:ActivityDesigner, newSize:Size): # -> 
        """ ResizeContainedDesigner(self: FreeformActivityDesigner, containedDesigner: ActivityDesigner, newSize: Size) """
        ...

    def SendToBack(self, containedDesigner:ActivityDesigner): # -> 
        """ SendToBack(self: FreeformActivityDesigner, containedDesigner: ActivityDesigner) """
        ...

    ConnectorAdded = ...
    ConnectorChanged = ...
    ConnectorRemoved = ...


class FreeformActivityDesignerLayoutSerializer(CompositeActivityDesignerLayoutSerializer): # skipped bases: <type 'object'>
    """ FreeformActivityDesignerLayoutSerializer() """
    pass

class HitTestLocations(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) HitTestLocations, values: ActionArea (2), Bottom (32), Connector (64), Designer (1), Left (4), None (0), Right (16), Top (8) """
    ActionArea: HitTestLocations = ...
    Bottom: HitTestLocations = ...
    Connector: HitTestLocations = ...
    Designer: HitTestLocations = ...
    Left: HitTestLocations = ...
    Right: HitTestLocations = ...
    Top: HitTestLocations = ...
    value__ = ...


class IDesignerGlyphProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetGlyphs(self, activityDesigner:ActivityDesigner) -> ActivityDesignerGlyphCollection:
        """ GetGlyphs(self: IDesignerGlyphProvider, activityDesigner: ActivityDesigner) -> ActivityDesignerGlyphCollection """
        ...


class IDesignerGlyphProviderService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def GlyphProviders(self) -> ReadOnlyCollection:
        """ Get: GlyphProviders(self: IDesignerGlyphProviderService) -> ReadOnlyCollection[IDesignerGlyphProvider] """
        ...


    def AddGlyphProvider(self, glyphProvider:IDesignerGlyphProvider): # -> 
        """ AddGlyphProvider(self: IDesignerGlyphProviderService, glyphProvider: IDesignerGlyphProvider) """
        ...

    def RemoveGlyphProvider(self, glyphProvider:IDesignerGlyphProvider): # -> 
        """ RemoveGlyphProvider(self: IDesignerGlyphProviderService, glyphProvider: IDesignerGlyphProvider) """
        ...


class IDesignerVerbProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetVerbs(self, activityDesigner:ActivityDesigner) -> ActivityDesignerVerbCollection:
        """ GetVerbs(self: IDesignerVerbProvider, activityDesigner: ActivityDesigner) -> ActivityDesignerVerbCollection """
        ...


class IDesignerVerbProviderService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def VerbProviders(self) -> ReadOnlyCollection:
        """ Get: VerbProviders(self: IDesignerVerbProviderService) -> ReadOnlyCollection[IDesignerVerbProvider] """
        ...


    def AddVerbProvider(self, verbProvider:IDesignerVerbProvider): # -> 
        """ AddVerbProvider(self: IDesignerVerbProviderService, verbProvider: IDesignerVerbProvider) """
        ...

    def RemoveVerbProvider(self, verbProvider:IDesignerVerbProvider): # -> 
        """ RemoveVerbProvider(self: IDesignerVerbProviderService, verbProvider: IDesignerVerbProvider) """
        ...


class IExtendedUIService: # skipped bases: <type 'object'>
    """ no doc """
    def AddAssemblyReference(self, assemblyName:AssemblyName): # -> 
        """ AddAssemblyReference(self: IExtendedUIService, assemblyName: AssemblyName) """
        ...

    def AddDesignerActions(self, actions:Array): # -> 
        """ AddDesignerActions(self: IExtendedUIService, actions: Array[DesignerAction]) """
        ...

    def AddWebReference(self, url, proxyClass): # -> Tuple_[DialogResult, Uri, Type]
        """ AddWebReference(self: IExtendedUIService) -> (DialogResult, Uri, Type) """
        ...

    def GetProxyClassForUrl(self, url:Uri) -> Type:
        """ GetProxyClassForUrl(self: IExtendedUIService, url: Uri) -> Type """
        ...

    def GetSelectedPropertyContext(self) -> ITypeDescriptorContext:
        """ GetSelectedPropertyContext(self: IExtendedUIService) -> ITypeDescriptorContext """
        ...

    def GetUrlForProxyClass(self, proxyClass:Type) -> Uri:
        """ GetUrlForProxyClass(self: IExtendedUIService, proxyClass: Type) -> Uri """
        ...

    def GetXsdProjectItemsInfo(self) -> Dictionary:
        """ GetXsdProjectItemsInfo(self: IExtendedUIService) -> Dictionary[str, Type] """
        ...

    def NavigateToProperty(self, propName:str) -> bool:
        """ NavigateToProperty(self: IExtendedUIService, propName: str) -> bool """
        ...

    def RemoveDesignerActions(self): # -> 
        """ RemoveDesignerActions(self: IExtendedUIService) """
        ...

    def ShowToolsOptions(self): # -> 
        """ ShowToolsOptions(self: IExtendedUIService) """
        ...


class IExtendedUIService2: # skipped bases: <type 'object'>
    """ no doc """
    def GetReflectionAssembly(self, assemblyName:AssemblyName) -> Assembly:
        """ GetReflectionAssembly(self: IExtendedUIService2, assemblyName: AssemblyName) -> Assembly """
        ...

    def GetRuntimeType(self, reflectionType:Type) -> Type:
        """ GetRuntimeType(self: IExtendedUIService2, reflectionType: Type) -> Type """
        ...

    def GetTargetFrameworkVersion(self) -> Int64:
        """ GetTargetFrameworkVersion(self: IExtendedUIService2) -> Int64 """
        ...

    def IsSupportedType(self, type:Type) -> bool:
        """ IsSupportedType(self: IExtendedUIService2, type: Type) -> bool """
        ...


class IIdentifierCreationService: # skipped bases: <type 'object'>
    """ no doc """
    def EnsureUniqueIdentifiers(self, parentActivity:CompositeActivity, childActivities:ICollection): # -> 
        """ EnsureUniqueIdentifiers(self: IIdentifierCreationService, parentActivity: CompositeActivity, childActivities: ICollection) """
        ...

    def ValidateIdentifier(self, activity:Activity, identifier:str): # -> 
        """ ValidateIdentifier(self: IIdentifierCreationService, activity: Activity, identifier: str) """
        ...


class IMemberCreationService: # skipped bases: <type 'object'>
    """ no doc """
    def CreateEvent(self, className:str, eventName:str, eventType:Type, attributes:Array, emitDependencyProperty:bool): # -> 
        """ CreateEvent(self: IMemberCreationService, className: str, eventName: str, eventType: Type, attributes: Array[AttributeInfo], emitDependencyProperty: bool) """
        ...

    def CreateField(self, className:str, fieldName:str, fieldType:Type, genericParameterTypes:Array, attributes:MemberAttributes, initializationExpression:CodeSnippetExpression, overwriteExisting:bool): # -> 
        """ CreateField(self: IMemberCreationService, className: str, fieldName: str, fieldType: Type, genericParameterTypes: Array[Type], attributes: MemberAttributes, initializationExpression: CodeSnippetExpression, overwriteExisting: bool) """
        ...

    def CreateProperty(self, className:str, propertyName:str, propertyType:Type, attributes:Array, emitDependencyProperty:bool, isMetaProperty:bool, isAttached:bool, ownerType:Type, isReadOnly:bool): # -> 
        """ CreateProperty(self: IMemberCreationService, className: str, propertyName: str, propertyType: Type, attributes: Array[AttributeInfo], emitDependencyProperty: bool, isMetaProperty: bool, isAttached: bool, ownerType: Type, isReadOnly: bool) """
        ...

    def RemoveEvent(self, className:str, eventName:str, eventType:Type): # -> 
        """ RemoveEvent(self: IMemberCreationService, className: str, eventName: str, eventType: Type) """
        ...

    def RemoveProperty(self, className:str, propertyName:str, propertyType:Type): # -> 
        """ RemoveProperty(self: IMemberCreationService, className: str, propertyName: str, propertyType: Type) """
        ...

    def ShowCode(self, activity:Activity = ..., methodName:str = ..., delegateType:Type = ...): # -> 
        """ ShowCode(self: IMemberCreationService, activity: Activity, methodName: str, delegateType: Type)ShowCode(self: IMemberCreationService) """
        ...

    def UpdateBaseType(self, className:str, baseType:Type): # -> 
        """ UpdateBaseType(self: IMemberCreationService, className: str, baseType: Type) """
        ...

    def UpdateEvent(self, className:str, oldEventName:str, oldEventType:Type, newEventName:str, newEventType:Type, attributes:Array, emitDependencyProperty:bool, isMetaProperty:bool): # -> 
        """ UpdateEvent(self: IMemberCreationService, className: str, oldEventName: str, oldEventType: Type, newEventName: str, newEventType: Type, attributes: Array[AttributeInfo], emitDependencyProperty: bool, isMetaProperty: bool) """
        ...

    def UpdateProperty(self, className:str, oldPropertyName:str, oldPropertyType:Type, newPropertyName:str, newPropertyType:Type, attributes:Array, emitDependencyProperty:bool, isMetaProperty:bool): # -> 
        """ UpdateProperty(self: IMemberCreationService, className: str, oldPropertyName: str, oldPropertyType: Type, newPropertyName: str, newPropertyType: Type, attributes: Array[AttributeInfo], emitDependencyProperty: bool, isMetaProperty: bool) """
        ...

    def UpdateTypeName(self, oldClassName:str, newClassName:str): # -> 
        """ UpdateTypeName(self: IMemberCreationService, oldClassName: str, newClassName: str) """
        ...


class ITypeFilterProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FilterDescription(self) -> str:
        """ Get: FilterDescription(self: ITypeFilterProvider) -> str """
        ...


    def CanFilterType(self, type:Type, throwOnError:bool) -> bool:
        """ CanFilterType(self: ITypeFilterProvider, type: Type, throwOnError: bool) -> bool """
        ...


class ITypeProviderCreator: # skipped bases: <type 'object'>
    """ no doc """
    def GetLocalAssembly(self, obj:object) -> Assembly:
        """ GetLocalAssembly(self: ITypeProviderCreator, obj: object) -> Assembly """
        ...

    def GetTransientAssembly(self, assemblyName:AssemblyName) -> Assembly:
        """ GetTransientAssembly(self: ITypeProviderCreator, assemblyName: AssemblyName) -> Assembly """
        ...

    def GetTypeProvider(self, obj:object) -> ITypeProvider:
        """ GetTypeProvider(self: ITypeProviderCreator, obj: object) -> ITypeProvider """
        ...

    def GetTypeResolutionService(self, obj:object) -> ITypeResolutionService:
        """ GetTypeResolutionService(self: ITypeProviderCreator, obj: object) -> ITypeResolutionService """
        ...


class LineAnchor(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LineAnchor, values: Arrow (1), ArrowAnchor (2), Diamond (3), DiamondAnchor (4), None (0), Rectangle (7), RectangleAnchor (8), Round (5), RoundAnchor (6), RoundedRectangle (9), RoundedRectangleAnchor (10) """
    Arrow: LineAnchor = ...
    ArrowAnchor: LineAnchor = ...
    Diamond: LineAnchor = ...
    DiamondAnchor: LineAnchor = ...
    Rectangle: LineAnchor = ...
    RectangleAnchor: LineAnchor = ...
    Round: LineAnchor = ...
    RoundAnchor: LineAnchor = ...
    RoundedRectangle: LineAnchor = ...
    RoundedRectangleAnchor: LineAnchor = ...
    value__ = ...


class LockedActivityGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ LockedActivityGlyph() """
    pass

class ParallelActivityDesigner(StructuredCompositeActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ ParallelActivityDesigner() """
    def CanMoveActivities(self, moveLocation:HitTestInfo, activitiesToMove:ReadOnlyCollection) -> bool:
        """ CanMoveActivities(self: ParallelActivityDesigner, moveLocation: HitTestInfo, activitiesToMove: ReadOnlyCollection[Activity]) -> bool """
        ...

    def OnCreateNewBranch(self, *args): #cannot find CLR method
        """ OnCreateNewBranch(self: ParallelActivityDesigner) -> CompositeActivity """
        ...


class ReadOnlyActivityGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ ReadOnlyActivityGlyph() """
    pass

class SelectionGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsPrimarySelection(self) -> bool:
        """ Get: IsPrimarySelection(self: SelectionGlyph) -> bool """
        ...


    def GetGrabHandles(self, designer:ActivityDesigner) -> Array:
        """ GetGrabHandles(self: SelectionGlyph, designer: ActivityDesigner) -> Array[Rectangle] """
        ...


class SequenceDesigner(SequentialActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ SequenceDesigner() """
    pass

class SequenceDesignerAccessibleObject(CompositeDesignerAccessibleObject): # skipped bases: <type 'IInvokeProvider'>, <type 'IValueProvider'>, <type 'IRawElementProviderFragment'>, <type 'IRawElementProviderFragmentRoot'>, <type 'IRawElementProviderSimple'>, <type 'IRangeValueProvider'>, <type 'IOleWindow'>, <type 'IAccessibleEx'>, <type 'IGridProvider'>, <type 'ISelectionItemProvider'>, <type 'IMarshal'>, <type 'IServiceProvider'>, <type 'ISelectionProvider'>, <type 'IReflect'>, <type 'IScrollItemProvider'>, <type 'ITableProvider'>, <type 'IExpandCollapseProvider'>, <type 'IToggleProvider'>, <type 'ILegacyIAccessibleProvider'>, <type 'IGridItemProvider'>, <type 'IEnumVariant'>, <type 'IAccessible'>, <type 'ITableItemProvider'>, <type 'IRawElementProviderHwndOverride'>, <type 'object'>
    """ SequenceDesignerAccessibleObject(activityDesigner: SequentialActivityDesigner) """
    def Navigate(self, navdir): # -> AccessibleObject # Not found arg types: {'navdir': 'AccessibleNavigation'}
        """ Navigate(self: SequenceDesignerAccessibleObject, navdir: AccessibleNavigation) -> AccessibleObject """
        ...


class SequentialWorkflowHeaderFooter: # skipped bases: <type 'object'>, <type 'object'>
    """ SequentialWorkflowHeaderFooter(parent: SequentialWorkflowRootDesigner, isHeader: bool) """
    @property
    def AssociatedDesigner(self):
        ...

    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: SequentialWorkflowHeaderFooter) -> Rectangle """
        ...

    @property
    def Image(self) -> Image:
        """
        Get: Image(self: SequentialWorkflowHeaderFooter) -> Image
        Set: Image(self: SequentialWorkflowHeaderFooter) = value
        """
        ...

    @property
    def ImageRectangle(self) -> Rectangle:
        """ Get: ImageRectangle(self: SequentialWorkflowHeaderFooter) -> Rectangle """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: SequentialWorkflowHeaderFooter) -> str
        Set: Text(self: SequentialWorkflowHeaderFooter) = value
        """
        ...

    @property
    def TextRectangle(self) -> Rectangle:
        """ Get: TextRectangle(self: SequentialWorkflowHeaderFooter) -> Rectangle """
        ...


    def OnLayout(self, e:ActivityDesignerLayoutEventArgs): # -> 
        """ OnLayout(self: SequentialWorkflowHeaderFooter, e: ActivityDesignerLayoutEventArgs) """
        ...

    def OnPaint(self, e:ActivityDesignerPaintEventArgs): # -> 
        """ OnPaint(self: SequentialWorkflowHeaderFooter, e: ActivityDesignerPaintEventArgs) """
        ...


class SequentialWorkflowRootDesigner(SequentialActivityDesigner): # skipped bases: <type 'IRootDesigner'>, <type 'IDisposable'>, <type 'IDesigner'>, <type 'IPersistUIState'>, <type 'IWorkflowDesignerMessageSink'>, <type 'IDesignerFilter'>, <type 'IWorkflowRootDesigner'>, <type 'IToolboxUser'>, <type 'IConnectableDesigner'>, <type 'object'>
    """ SequentialWorkflowRootDesigner() """
    @property
    def Footer(self):
        ...

    @property
    def Header(self):
        ...

    @property
    def Image(self) -> Image:
        """ Get: Image(self: SequentialWorkflowRootDesigner) -> Image """
        ...

    @property
    def MinimumSize(self) -> Size:
        """ Get: MinimumSize(self: SequentialWorkflowRootDesigner) -> Size """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: SequentialWorkflowRootDesigner) -> str """
        ...


    def CanBeParentedTo(self, parentActivityDesigner:CompositeActivityDesigner) -> bool:
        """ CanBeParentedTo(self: SequentialWorkflowRootDesigner, parentActivityDesigner: CompositeActivityDesigner) -> bool """
        ...


class ShadowGlyph(DesignerGlyph): # skipped bases: <type 'object'>
    """ ShadowGlyph() """
    pass

class TextQuality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextQuality, values: Aliased (0), AntiAliased (1) """
    Aliased: TextQuality = ...
    AntiAliased: TextQuality = ...
    value__ = ...


class ThemeConfigurationDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    ThemeConfigurationDialog(serviceProvider: IServiceProvider)
    ThemeConfigurationDialog(serviceProvider: IServiceProvider, theme: WorkflowTheme)
    """
    @property
    def ComposedTheme(self) -> WorkflowTheme:
        """ Get: ComposedTheme(self: ThemeConfigurationDialog) -> WorkflowTheme """
        ...


    def __new__(cls, serviceProvider:IServiceProvider, theme:WorkflowTheme = ...) -> Self:
        """
        __new__(cls: type, serviceProvider: IServiceProvider)
        __new__(cls: type, serviceProvider: IServiceProvider, theme: WorkflowTheme)
        """
        ...


class ThemeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThemeType, values: Default (0), System (1), UserDefined (2) """
    Default: ThemeType = ...
    System: ThemeType = ...
    UserDefined: ThemeType = ...
    value__ = ...


class TypeBrowserDialog(ISite, Form): # skipped bases: <type 'IPersistStreamInit'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IServiceProvider'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IViewObject'>, <type 'IWin32Window'>, <type 'IOleInPlaceObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IDisposable'>, <type 'IContainerControl'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'object'>
    """
    TypeBrowserDialog(serviceProvider: IServiceProvider, filterProvider: ITypeFilterProvider, selectedTypeName: str, typeProvider: TypeProvider)
    TypeBrowserDialog(serviceProvider: IServiceProvider, filterProvider: ITypeFilterProvider, selectedTypeName: str)
    """
    @property
    def SelectedType(self) -> Type:
        """ Get: SelectedType(self: TypeBrowserDialog) -> Type """
        ...


    def __new__(cls, serviceProvider:IServiceProvider, filterProvider:ITypeFilterProvider, selectedTypeName:str, typeProvider:TypeProvider = ...) -> Self:
        """
        __new__(cls: type, serviceProvider: IServiceProvider, filterProvider: ITypeFilterProvider, selectedTypeName: str, typeProvider: TypeProvider)
        __new__(cls: type, serviceProvider: IServiceProvider, filterProvider: ITypeFilterProvider, selectedTypeName: str)
        """
        ...


class TypeBrowserEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ TypeBrowserEditor() """
    pass

class TypeFilterProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeFilterProviderAttribute(type: Type)
    TypeFilterProviderAttribute(typeName: str)
    """
    @property
    def TypeFilterProviderTypeName(self) -> str:
        """ Get: TypeFilterProviderTypeName(self: TypeFilterProviderAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        ...


class WorkflowDesignerLoader(BasicDesignerLoader): # skipped bases: <type 'IDesignerLoaderService'>, <type 'object'>
    """ no doc """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: WorkflowDesignerLoader) -> str """
        ...

    @property
    def InDebugMode(self) -> bool:
        """ Get: InDebugMode(self: WorkflowDesignerLoader) -> bool """
        ...

    @property
    def TargetFrameworkTypeDescriptionProvider(self):
        ...


    def AddActivityToDesigner(self, activity:Activity): # -> 
        """ AddActivityToDesigner(self: WorkflowDesignerLoader, activity: Activity) """
        ...

    def ForceReload(self): # -> 
        """ ForceReload(self: WorkflowDesignerLoader) """
        ...

    def GetFileReader(self, filePath:str) -> TextReader:
        """ GetFileReader(self: WorkflowDesignerLoader, filePath: str) -> TextReader """
        ...

    def GetFileWriter(self, filePath:str) -> TextWriter:
        """ GetFileWriter(self: WorkflowDesignerLoader, filePath: str) -> TextWriter """
        ...

    def LoadDesignerLayout(self, *args): #cannot find CLR method
        """ LoadDesignerLayout(self: WorkflowDesignerLoader, layoutReader: XmlReader) -> IList """
        ...

    def LoadDesignerLayoutFromResource(self, *args): #cannot find CLR method
        """ LoadDesignerLayoutFromResource(self: WorkflowDesignerLoader, type: Type, manifestResourceName: str) -> IList """
        ...

    def RemoveActivityFromDesigner(self, activity:Activity): # -> 
        """ RemoveActivityFromDesigner(self: WorkflowDesignerLoader, activity: Activity) """
        ...

    def SaveDesignerLayout(self, *args): #cannot find CLR method
        """ SaveDesignerLayout(self: WorkflowDesignerLoader, layoutWriter: XmlWriter, rootDesigner: ActivityDesigner) -> IList """
        ...


class WorkflowDesignerMessageFilter(IDisposable, IWorkflowDesignerMessageSink): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MessageHitTestContext(self):
        ...

    @property
    def ParentView(self):
        ...


    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: WorkflowDesignerMessageFilter, parentView: WorkflowView) """
        ...

    def OnDragDrop(self, *args): #cannot find CLR method
        """ OnDragDrop(self: WorkflowDesignerMessageFilter, eventArgs: DragEventArgs) -> bool """
        ...

    def OnDragEnter(self, *args): #cannot find CLR method
        """ OnDragEnter(self: WorkflowDesignerMessageFilter, eventArgs: DragEventArgs) -> bool """
        ...

    def OnDragLeave(self, *args): #cannot find CLR method
        """ OnDragLeave(self: WorkflowDesignerMessageFilter) -> bool """
        ...

    def OnDragOver(self, *args): #cannot find CLR method
        """ OnDragOver(self: WorkflowDesignerMessageFilter, eventArgs: DragEventArgs) -> bool """
        ...

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """ OnGiveFeedback(self: WorkflowDesignerMessageFilter, eventArgs: GiveFeedbackEventArgs) -> bool """
        ...

    def OnKeyDown(self, *args): #cannot find CLR method
        """ OnKeyDown(self: WorkflowDesignerMessageFilter, eventArgs: KeyEventArgs) -> bool """
        ...

    def OnKeyUp(self, *args): #cannot find CLR method
        """ OnKeyUp(self: WorkflowDesignerMessageFilter, eventArgs: KeyEventArgs) -> bool """
        ...

    def OnLayout(self, *args): #cannot find CLR method
        """ OnLayout(self: WorkflowDesignerMessageFilter, eventArgs: LayoutEventArgs) """
        ...

    def OnMouseCaptureChanged(self, *args): #cannot find CLR method
        """ OnMouseCaptureChanged(self: WorkflowDesignerMessageFilter) -> bool """
        ...

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """ OnMouseDoubleClick(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseDown(self, *args): #cannot find CLR method
        """ OnMouseDown(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseEnter(self, *args): #cannot find CLR method
        """ OnMouseEnter(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseHover(self, *args): #cannot find CLR method
        """ OnMouseHover(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseLeave(self, *args): #cannot find CLR method
        """ OnMouseLeave(self: WorkflowDesignerMessageFilter) -> bool """
        ...

    def OnMouseMove(self, *args): #cannot find CLR method
        """ OnMouseMove(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseUp(self, *args): #cannot find CLR method
        """ OnMouseUp(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnMouseWheel(self, *args): #cannot find CLR method
        """ OnMouseWheel(self: WorkflowDesignerMessageFilter, eventArgs: MouseEventArgs) -> bool """
        ...

    def OnPaint(self, *args): #cannot find CLR method
        """ OnPaint(self: WorkflowDesignerMessageFilter, eventArgs: PaintEventArgs, viewPort: Rectangle, ambientTheme: AmbientTheme) -> bool """
        ...

    def OnPaintWorkflowAdornments(self, *args): #cannot find CLR method
        """ OnPaintWorkflowAdornments(self: WorkflowDesignerMessageFilter, eventArgs: PaintEventArgs, viewPort: Rectangle, ambientTheme: AmbientTheme) -> bool """
        ...

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """ OnQueryContinueDrag(self: WorkflowDesignerMessageFilter, eventArgs: QueryContinueDragEventArgs) -> bool """
        ...

    def OnScroll(self, *args): #cannot find CLR method
        """ OnScroll(self: WorkflowDesignerMessageFilter, sender: ScrollBar, value: int) -> bool """
        ...

    def OnShowContextMenu(self, *args): #cannot find CLR method
        """ OnShowContextMenu(self: WorkflowDesignerMessageFilter, screenMenuPoint: Point) -> bool """
        ...

    def OnThemeChange(self, *args): #cannot find CLR method
        """ OnThemeChange(self: WorkflowDesignerMessageFilter) """
        ...

    def ProcessMessage(self, *args): #cannot find CLR method
        """ ProcessMessage(self: WorkflowDesignerMessageFilter, message: Message) -> bool """
        ...


class WorkflowMenuCommands(StandardCommands): # skipped bases: <type 'object'>
    """ WorkflowMenuCommands() """
    BreakpointActionMenu: CommandID = ...
    BreakpointConditionMenu: CommandID = ...
    BreakpointConstraintsMenu: CommandID = ...
    BreakpointHitCountMenu: CommandID = ...
    BreakpointLocationMenu: CommandID = ...
    ChangeTheme: CommandID = ...
    ClearBreakpointsMenu: CommandID = ...
    Collapse: CommandID = ...
    CopyToClipboard: CommandID = ...
    CreateTheme: CommandID = ...
    DebugCommandSetId: Guid = ...
    DebugStepBranchMenu: CommandID = ...
    DebugStepInstanceMenu: CommandID = ...
    DebugWorkflowGroupId: Guid = ...
    DefaultFilter: CommandID = ...
    DefaultPage: CommandID = ...
    DesignerActionsMenu: CommandID = ...
    DesignerProperties: CommandID = ...
    Disable: CommandID = ...
    Enable: CommandID = ...
    EnableBreakpointMenu: CommandID = ...
    ExecutionStateMenu: CommandID = ...
    Expand: CommandID = ...
    FirstZoomCommand: int = ...
    GotoDisassemblyMenu: CommandID = ...
    InsertBreakpointMenu: CommandID = ...
    InsertTracePointMenu: CommandID = ...
    LastZoomCommand: int = ...
    MenuGuid: Guid = ...
    NewDataBreakpointMenu: CommandID = ...
    NewFileTracePointMenu: CommandID = ...
    PageDown: CommandID = ...
    PageLayoutMenu: CommandID = ...
    PageSetup: CommandID = ...
    PageUp: CommandID = ...
    Pan: CommandID = ...
    PanMenu: CommandID = ...
    Print: CommandID = ...
    PrintPreview: CommandID = ...
    PrintPreviewPage: CommandID = ...
    RunToCursorMenu: CommandID = ...
    SaveAsImage: CommandID = ...
    SelectionMenu: CommandID = ...
    SetNextStatementMenu: CommandID = ...
    ShowAll: CommandID = ...
    ShowNextStatementMenu: CommandID = ...
    ToggleBreakpointMenu: CommandID = ...
    VerbGroupActions: int = ...
    VerbGroupDesignerActions: int = ...
    VerbGroupEdit: int = ...
    VerbGroupGeneral: int = ...
    VerbGroupMisc: int = ...
    VerbGroupOptions: int = ...
    VerbGroupView: int = ...
    WorkflowCommandSetId: Guid = ...
    WorkflowToolBar: int = ...
    Zoom100Mode: CommandID = ...
    Zoom150Mode: CommandID = ...
    Zoom200Mode: CommandID = ...
    Zoom300Mode: CommandID = ...
    Zoom400Mode: CommandID = ...
    Zoom50Mode: CommandID = ...
    Zoom75Mode: CommandID = ...
    ZoomIn: CommandID = ...
    ZoomLevelCombo: CommandID = ...
    ZoomLevelListHandler: CommandID = ...
    ZoomMenu: CommandID = ...
    ZoomOut: CommandID = ...


class WorkflowOutline(UserControl): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ WorkflowOutline(serviceProvider: IServiceProvider) """
    @property
    def NeedsExpandAll(self):
        ...

    @property
    def RootNode(self):
        ...

    @property
    def TreeView(self):
        ...


    def CreateNewNode(self, *args): #cannot find CLR method
        """ CreateNewNode(self: WorkflowOutline, activity: Activity) -> WorkflowOutlineNode """
        ...

    def GetNode(self, *args): #cannot find CLR method
        """ GetNode(self: WorkflowOutline, activity: Activity) -> WorkflowOutlineNode """
        ...

    def OnBeginUpdate(self, *args): #cannot find CLR method
        """ OnBeginUpdate(self: WorkflowOutline) """
        ...

    def OnEndUpdate(self, *args): #cannot find CLR method
        """ OnEndUpdate(self: WorkflowOutline) """
        ...

    def OnNodeAdded(self, *args): #cannot find CLR method
        """ OnNodeAdded(self: WorkflowOutline, node: WorkflowOutlineNode) """
        ...

    def OnNodeSelected(self, *args): #cannot find CLR method
        """ OnNodeSelected(self: WorkflowOutline, node: WorkflowOutlineNode) """
        ...

    def OnRefreshNode(self, *args): #cannot find CLR method
        """ OnRefreshNode(self: WorkflowOutline, node: WorkflowOutlineNode) """
        ...

    def RefreshNode(self, *args): #cannot find CLR method
        """ RefreshNode(self: WorkflowOutline, nodeToUpdate: WorkflowOutlineNode, refreshChildNodes: bool) """
        ...

    def RefreshWorkflowOutline(self): # -> 
        """ RefreshWorkflowOutline(self: WorkflowOutline) """
        ...

    def ReloadWorkflowOutline(self): # -> 
        """ ReloadWorkflowOutline(self: WorkflowOutline) """
        ...

    def __new__(cls, serviceProvider:IServiceProvider) -> Self:
        """ __new__(cls: type, serviceProvider: IServiceProvider) """
        ...

    Expanding = ...


class WorkflowOutlineNode(TreeNode): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WorkflowOutlineNode(activity: Activity) """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: WorkflowOutlineNode) -> Activity """
        ...


    def OnActivityRename(self, newName:str): # -> 
        """ OnActivityRename(self: WorkflowOutlineNode, newName: str) """
        ...

    def RefreshNode(self): # -> 
        """ RefreshNode(self: WorkflowOutlineNode) """
        ...


class WorkflowPageSetupDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ WorkflowPageSetupDialog(serviceProvider: IServiceProvider) """
    def __new__(cls, serviceProvider:IServiceProvider) -> Self:
        """ __new__(cls: type, serviceProvider: IServiceProvider) """
        ...


class WorkflowTheme(IDisposable): # skipped bases: <type 'object'>
    """ WorkflowTheme() """
    @property
    def AmbientTheme(self) -> AmbientTheme:
        """ Get: AmbientTheme(self: WorkflowTheme) -> AmbientTheme """
        ...

    @property
    def ContainingFileDirectory(self) -> str:
        """ Get: ContainingFileDirectory(self: WorkflowTheme) -> str """
        ...

    @property
    def CurrentTheme(self) -> WorkflowTheme:
        """
        Get: CurrentTheme() -> WorkflowTheme
        Set: CurrentTheme() = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: WorkflowTheme) -> str
        Set: Description(self: WorkflowTheme) = value
        """
        ...

    @property
    def DesignerThemes(self) -> IList:
        """ Get: DesignerThemes(self: WorkflowTheme) -> IList """
        ...

    @property
    def EnableChangeNotification(self) -> bool:
        """
        Get: EnableChangeNotification() -> bool
        Set: EnableChangeNotification() = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: WorkflowTheme) -> str
        Set: FilePath(self: WorkflowTheme) = value
        """
        ...

    @property
    def LookupPath(self) -> str:
        """ Get: LookupPath() -> str """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowTheme) -> str
        Set: Name(self: WorkflowTheme) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: WorkflowTheme) -> bool
        Set: ReadOnly(self: WorkflowTheme) = value
        """
        ...

    @property
    def RegistryKeyPath(self) -> str:
        """ Get: RegistryKeyPath() -> str """
        ...

    @property
    def StandardThemes(self) -> IDictionary:
        """ Get: StandardThemes() -> IDictionary[ThemeType, Array[str]] """
        ...

    @property
    def Type(self) -> ThemeType:
        """ Get: Type(self: WorkflowTheme) -> ThemeType """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: WorkflowTheme) -> str
        Set: Version(self: WorkflowTheme) = value
        """
        ...


    def Clone(self) -> WorkflowTheme:
        """ Clone(self: WorkflowTheme) -> WorkflowTheme """
        ...

    @staticmethod
    def CreateStandardTheme(standardThemeType:ThemeType) -> WorkflowTheme:
        """ CreateStandardTheme(standardThemeType: ThemeType) -> WorkflowTheme """
        ...

    @staticmethod
    def GenerateThemeFilePath() -> str:
        """ GenerateThemeFilePath() -> str """
        ...

    def GetDesignerTheme(self, designer:ActivityDesigner) -> ActivityDesignerTheme:
        """ GetDesignerTheme(self: WorkflowTheme, designer: ActivityDesigner) -> ActivityDesignerTheme """
        ...

    @staticmethod
    def Load(*__args:str) -> WorkflowTheme:
        """
        Load(themeFilePath: str) -> WorkflowTheme
        Load(serializationManager: IDesignerSerializationManager, themeFilePath: str) -> WorkflowTheme
        """
        ...

    @staticmethod
    def LoadThemeSettingFromRegistry() -> WorkflowTheme:
        """ LoadThemeSettingFromRegistry() -> WorkflowTheme """
        ...

    def Save(self, themeFilePath:str): # -> 
        """ Save(self: WorkflowTheme, themeFilePath: str) """
        ...

    @staticmethod
    def SaveThemeSettingToRegistry(): # -> 
        """ SaveThemeSettingToRegistry() """
        ...

    ThemeChanged = ...


class WorkflowView(IServiceProvider, IMessageFilter, UserControl): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    WorkflowView()
    WorkflowView(serviceProvider: IServiceProvider)
    """
    @property
    def EnableFitToScreen(self) -> bool:
        """
        Get: EnableFitToScreen(self: WorkflowView) -> bool
        Set: EnableFitToScreen(self: WorkflowView) = value
        """
        ...

    @property
    def HScrollBar(self): # -> HScrollBar
        """ Get: HScrollBar(self: WorkflowView) -> HScrollBar """
        ...

    @property
    def PrintDocument(self) -> PrintDocument:
        """ Get: PrintDocument(self: WorkflowView) -> PrintDocument """
        ...

    @property
    def PrintPreviewMode(self) -> bool:
        """
        Get: PrintPreviewMode(self: WorkflowView) -> bool
        Set: PrintPreviewMode(self: WorkflowView) = value
        """
        ...

    @property
    def RootDesigner(self) -> ActivityDesigner:
        """
        Get: RootDesigner(self: WorkflowView) -> ActivityDesigner
        Set: RootDesigner(self: WorkflowView) = value
        """
        ...

    @property
    def ScrollPosition(self) -> Point:
        """
        Get: ScrollPosition(self: WorkflowView) -> Point
        Set: ScrollPosition(self: WorkflowView) = value
        """
        ...

    @property
    def ShadowDepth(self) -> int:
        """
        Get: ShadowDepth(self: WorkflowView) -> int
        Set: ShadowDepth(self: WorkflowView) = value
        """
        ...

    @property
    def ViewPortRectangle(self) -> Rectangle:
        """ Get: ViewPortRectangle(self: WorkflowView) -> Rectangle """
        ...

    @property
    def ViewPortSize(self) -> Size:
        """ Get: ViewPortSize(self: WorkflowView) -> Size """
        ...

    @property
    def VScrollBar(self): # -> VScrollBar
        """ Get: VScrollBar(self: WorkflowView) -> VScrollBar """
        ...

    @property
    def Zoom(self) -> int:
        """
        Get: Zoom(self: WorkflowView) -> int
        Set: Zoom(self: WorkflowView) = value
        """
        ...


    def AddDesignerMessageFilter(self, designerMessageFilter:WorkflowDesignerMessageFilter): # -> 
        """ AddDesignerMessageFilter(self: WorkflowView, designerMessageFilter: WorkflowDesignerMessageFilter) """
        ...

    def ClientPointToLogical(self, clientPoint:Point) -> Point:
        """ ClientPointToLogical(self: WorkflowView, clientPoint: Point) -> Point """
        ...

    def ClientRectangleToLogical(self, rectangle:Rectangle) -> Rectangle:
        """ ClientRectangleToLogical(self: WorkflowView, rectangle: Rectangle) -> Rectangle """
        ...

    def ClientSizeToLogical(self, clientSize:Size) -> Size:
        """ ClientSizeToLogical(self: WorkflowView, clientSize: Size) -> Size """
        ...

    def EnsureVisible(self, selectableObject:object): # -> 
        """ EnsureVisible(self: WorkflowView, selectableObject: object) """
        ...

    def FitToScreenSize(self): # -> 
        """ FitToScreenSize(self: WorkflowView) """
        ...

    def FitToWorkflowSize(self): # -> 
        """ FitToWorkflowSize(self: WorkflowView) """
        ...

    def InvalidateClientRectangle(self, clientRectangle:Rectangle): # -> 
        """ InvalidateClientRectangle(self: WorkflowView, clientRectangle: Rectangle) """
        ...

    def InvalidateLogicalRectangle(self, logicalRectangle:Rectangle): # -> 
        """ InvalidateLogicalRectangle(self: WorkflowView, logicalRectangle: Rectangle) """
        ...

    def LoadViewState(self, viewState:Stream): # -> 
        """ LoadViewState(self: WorkflowView, viewState: Stream) """
        ...

    def LogicalPointToClient(self, logicalPoint:Point) -> Point:
        """ LogicalPointToClient(self: WorkflowView, logicalPoint: Point) -> Point """
        ...

    def LogicalPointToScreen(self, logicalPoint:Point) -> Point:
        """ LogicalPointToScreen(self: WorkflowView, logicalPoint: Point) -> Point """
        ...

    def LogicalRectangleToClient(self, rectangle:Rectangle) -> Rectangle:
        """ LogicalRectangleToClient(self: WorkflowView, rectangle: Rectangle) -> Rectangle """
        ...

    def LogicalSizeToClient(self, logicalSize:Size) -> Size:
        """ LogicalSizeToClient(self: WorkflowView, logicalSize: Size) -> Size """
        ...

    def OnRootDesignerChanged(self, *args): #cannot find CLR method
        """ OnRootDesignerChanged(self: WorkflowView) """
        ...

    def OnZoomChanged(self, *args): #cannot find CLR method
        """ OnZoomChanged(self: WorkflowView) """
        ...

    def PerformLayout(self, *__args:bool): # -> 
        """ PerformLayout(self: WorkflowView, immediateUpdate: bool) """
        ...

    def RemoveDesignerMessageFilter(self, designerMessageFilter:WorkflowDesignerMessageFilter): # -> 
        """ RemoveDesignerMessageFilter(self: WorkflowView, designerMessageFilter: WorkflowDesignerMessageFilter) """
        ...

    def SaveViewState(self, viewState:Stream): # -> 
        """ SaveViewState(self: WorkflowView, viewState: Stream) """
        ...

    def SaveWorkflowImage(self, *__args): # -> 
        """ SaveWorkflowImage(self: WorkflowView, imageFile: str, imageFormat: ImageFormat)SaveWorkflowImage(self: WorkflowView, stream: Stream, imageFormat: ImageFormat) """
        ...

    def SaveWorkflowImageToClipboard(self): # -> 
        """ SaveWorkflowImageToClipboard(self: WorkflowView) """
        ...

    def ScreenPointToLogical(self, screenPoint:Point) -> Point:
        """ ScreenPointToLogical(self: WorkflowView, screenPoint: Point) -> Point """
        ...

    def ShowInfoTip(self, *__args:str): # -> 
        """ ShowInfoTip(self: WorkflowView, text: str)ShowInfoTip(self: WorkflowView, title: str, text: str) """
        ...

    def ShowInPlaceToolTip(self, toolTipText:str, toolTipRectangle:Rectangle): # -> 
        """ ShowInPlaceToolTip(self: WorkflowView, toolTipText: str, toolTipRectangle: Rectangle) """
        ...

    def __new__(cls, serviceProvider:IServiceProvider = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, serviceProvider: IServiceProvider)
        """
        ...

    Idle = ...
    RootDesignerChanged = ...
    ZoomChanged = ...


class WorkflowViewAccessibleObject(ControlAccessibleObject): # skipped bases: <type 'IInvokeProvider'>, <type 'IValueProvider'>, <type 'IRawElementProviderFragment'>, <type 'IRawElementProviderFragmentRoot'>, <type 'IRawElementProviderSimple'>, <type 'IRangeValueProvider'>, <type 'IOleWindow'>, <type 'IAccessibleEx'>, <type 'IGridProvider'>, <type 'ISelectionItemProvider'>, <type 'IServiceProvider'>, <type 'IMarshal'>, <type 'IReflect'>, <type 'ISelectionProvider'>, <type 'IScrollItemProvider'>, <type 'ITableProvider'>, <type 'IExpandCollapseProvider'>, <type 'IToggleProvider'>, <type 'ILegacyIAccessibleProvider'>, <type 'IGridItemProvider'>, <type 'IEnumVariant'>, <type 'IAccessible'>, <type 'ITableItemProvider'>, <type 'IRawElementProviderHwndOverride'>, <type 'object'>
    """ WorkflowViewAccessibleObject(workflowView: WorkflowView) """
    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: WorkflowViewAccessibleObject) -> Rectangle """
        ...


    def GetChild(self, index:int): # -> AccessibleObject
        """ GetChild(self: WorkflowViewAccessibleObject, index: int) -> AccessibleObject """
        ...

    def GetChildCount(self) -> int:
        """ GetChildCount(self: WorkflowViewAccessibleObject) -> int """
        ...

    def Navigate(self, navdir): # -> AccessibleObject # Not found arg types: {'navdir': 'AccessibleNavigation'}
        """ Navigate(self: WorkflowViewAccessibleObject, navdir: AccessibleNavigation) -> AccessibleObject """
        ...


