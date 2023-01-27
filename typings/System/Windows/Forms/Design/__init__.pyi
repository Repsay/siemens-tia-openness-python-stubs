# encoding: utf-8
# module System.Windows.Forms.Design calls itself Design
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, Guid, IServiceProvider, Type

from System.CodeDom import FieldDirection

from System.Collections import ArrayList, IDictionary, IEnumerable, IList

from System.ComponentModel import (ComponentEditor, IComponent, 
    IExtenderProvider, PropertyDescriptor, PropertyDescriptorCollection)

from System.ComponentModel.Design import (CommandID, ComponentDesigner, 
    DesignerOptionService, IDesigner, IRootDesigner, 
    ITypeDescriptorFilterService, StandardCommands)

from System.ComponentModel.Design.Serialization import CodeDomSerializer

from System.Drawing import Bitmap, Icon

from System.Drawing.Design import (IToolboxUser, ImageEditor, ToolboxItem, 
    UITypeEditor)

from System.Globalization import CultureInfo

from System.IO import FileInfo

from System.Messaging import Message

from System.Runtime.InteropServices import TYPELIBATTR, UCOMITypeLib

from System.Web.UI import Control

from System.Windows.Forms import (AccessibleObject, DialogResult, Form, 
    IComponentEditorPageSite, IWin32Window, Menu, MenuItem, MessageBoxButtons, 
    Panel, ScrollableControl)

from System.Windows.Forms.Design.Behavior import (GlyphCollection, 
    GlyphSelectionType)

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point, Size

"""The following names are not found in the module: (BoundEvent, 
    IEventHandlerService, IOleDragClient, ISelectionUIHandler, field#)
"""

# no functions
# classes

class AnchorEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ AnchorEditor() """
    pass

class AxImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ AxImporter(options: Options) """
    @property
    def GeneratedAssemblies(self) -> Array:
        """ Get: GeneratedAssemblies(self: AxImporter) -> Array[str] """
        ...

    @property
    def GeneratedSources(self) -> Array:
        """ Get: GeneratedSources(self: AxImporter) -> Array[str] """
        ...

    @property
    def GeneratedTypeLibAttributes(self) -> Array:
        """ Get: GeneratedTypeLibAttributes(self: AxImporter) -> Array[TYPELIBATTR] """
        ...


    def GenerateFromFile(self, file:FileInfo) -> str:
        """ GenerateFromFile(self: AxImporter, file: FileInfo) -> str """
        ...

    def GenerateFromTypeLibrary(self, typeLib:UCOMITypeLib, clsid:Guid = ...) -> str:
        """
        GenerateFromTypeLibrary(self: AxImporter, typeLib: UCOMITypeLib) -> str
        GenerateFromTypeLibrary(self: AxImporter, typeLib: UCOMITypeLib, clsid: Guid) -> str
        """
        ...

    @staticmethod
    def GetFileOfTypeLib(tlibattr:TYPELIBATTR) -> Tuple_[str, TYPELIBATTR]:
        """ GetFileOfTypeLib(tlibattr: TYPELIBATTR) -> (str, TYPELIBATTR) """
        ...

    def IReferenceResolver(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Options(self, *args): #cannot find CLR method
        """ Options() """
        ...



class AxParameterData: # skipped bases: <type 'object'>, <type 'object'>
    """
    AxParameterData(inname: str, typeName: str)
    AxParameterData(inname: str, type: Type)
    AxParameterData(info: ParameterInfo)
    AxParameterData(info: ParameterInfo, ignoreByRefs: bool)
    """
    @property
    def Direction(self) -> FieldDirection:
        """ Get: Direction(self: AxParameterData) -> FieldDirection """
        ...

    @property
    def IsByRef(self) -> bool:
        """ Get: IsByRef(self: AxParameterData) -> bool """
        ...

    @property
    def IsIn(self) -> bool:
        """ Get: IsIn(self: AxParameterData) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: AxParameterData) -> bool """
        ...

    @property
    def IsOut(self) -> bool:
        """ Get: IsOut(self: AxParameterData) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: AxParameterData) -> str
        Set: Name(self: AxParameterData) = value
        """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: AxParameterData) -> Type """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: AxParameterData) -> str """
        ...


    @staticmethod
    def Convert(infos:Array, ignoreByRefs:bool = ...) -> Array:
        """
        Convert(infos: Array[ParameterInfo]) -> Array[AxParameterData]
        Convert(infos: Array[ParameterInfo], ignoreByRefs: bool) -> Array[AxParameterData]
        """
        ...


class AxWrapperGen: # skipped bases: <type 'object'>, <type 'object'>
    """ AxWrapperGen(axType: Type) """
    GeneratedSources: ArrayList = ...


class BorderSidesEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ BorderSidesEditor() """
    pass

class ComponentDocumentDesigner(ComponentDesigner, IRootDesigner, IToolboxUser, ITypeDescriptorFilterService, IOleDragClient): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ComponentDocumentDesigner() """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: ComponentDocumentDesigner) -> Control """
        ...

    @property
    def TrayAutoArrange(self) -> bool:
        """
        Get: TrayAutoArrange(self: ComponentDocumentDesigner) -> bool
        Set: TrayAutoArrange(self: ComponentDocumentDesigner) = value
        """
        ...

    @property
    def TrayLargeIcon(self) -> bool:
        """
        Get: TrayLargeIcon(self: ComponentDocumentDesigner) -> bool
        Set: TrayLargeIcon(self: ComponentDocumentDesigner) = value
        """
        ...



class ComponentEditorForm(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ComponentEditorForm(component: object, pageTypes: Array[Type]) """
    def OnSelChangeSelector(self, *args): #cannot find CLR method
        """ OnSelChangeSelector(self: ComponentEditorForm, source: object, e: TreeViewEventArgs) """
        ...

    def PreProcessMessage(self, msg:Message) -> Tuple_[bool, Message]:
        """ PreProcessMessage(self: ComponentEditorForm, msg: Message) -> (bool, Message) """
        ...

    def ShowForm(self, *__args:int) -> DialogResult:
        """
        ShowForm(self: ComponentEditorForm) -> DialogResult
        ShowForm(self: ComponentEditorForm, page: int) -> DialogResult
        ShowForm(self: ComponentEditorForm, owner: IWin32Window) -> DialogResult
        ShowForm(self: ComponentEditorForm, owner: IWin32Window, page: int) -> DialogResult
        """
        ...

    def __new__(cls, component:object, pageTypes:Array) -> Self:
        """ __new__(cls: type, component: object, pageTypes: Array[Type]) """
        ...

    AutoSizeChanged = ...


class ComponentEditorPage(Panel): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'object'>
    """ ComponentEditorPage() """
    @property
    def CommitOnDeactivate(self) -> bool:
        """
        Get: CommitOnDeactivate(self: ComponentEditorPage) -> bool
        Set: CommitOnDeactivate(self: ComponentEditorPage) = value
        """
        ...

    @property
    def Component(self):
        ...

    @property
    def FirstActivate(self):
        ...

    @property
    def Icon(self) -> Icon:
        """
        Get: Icon(self: ComponentEditorPage) -> Icon
        Set: Icon(self: ComponentEditorPage) = value
        """
        ...

    @property
    def Loading(self):
        ...

    @property
    def LoadRequired(self):
        ...

    @property
    def PageSite(self):
        ...

    @property
    def Title(self) -> str:
        """ Get: Title(self: ComponentEditorPage) -> str """
        ...


    def Activate(self): # -> 
        """ Activate(self: ComponentEditorPage) """
        ...

    def ApplyChanges(self): # -> 
        """ ApplyChanges(self: ComponentEditorPage) """
        ...

    def Deactivate(self): # -> 
        """ Deactivate(self: ComponentEditorPage) """
        ...

    def EnterLoadingMode(self, *args): #cannot find CLR method
        """ EnterLoadingMode(self: ComponentEditorPage) """
        ...

    def ExitLoadingMode(self, *args): #cannot find CLR method
        """ ExitLoadingMode(self: ComponentEditorPage) """
        ...

    def GetControl(self) -> Control:
        """ GetControl(self: ComponentEditorPage) -> Control """
        ...

    def GetSelectedComponent(self, *args): #cannot find CLR method
        """ GetSelectedComponent(self: ComponentEditorPage) -> IComponent """
        ...

    def IsFirstActivate(self, *args): #cannot find CLR method
        """ IsFirstActivate(self: ComponentEditorPage) -> bool """
        ...

    def IsLoading(self, *args): #cannot find CLR method
        """ IsLoading(self: ComponentEditorPage) -> bool """
        ...

    def IsPageMessage(self, msg:Message) -> Tuple_[bool, Message]:
        """ IsPageMessage(self: ComponentEditorPage, msg: Message) -> (bool, Message) """
        ...

    def LoadComponent(self, *args): #cannot find CLR method
        """ LoadComponent(self: ComponentEditorPage) """
        ...

    def OnApplyComplete(self): # -> 
        """ OnApplyComplete(self: ComponentEditorPage) """
        ...

    def ReloadComponent(self, *args): #cannot find CLR method
        """ ReloadComponent(self: ComponentEditorPage) """
        ...

    def SaveComponent(self, *args): #cannot find CLR method
        """ SaveComponent(self: ComponentEditorPage) """
        ...

    def SetComponent(self, component:IComponent): # -> 
        """ SetComponent(self: ComponentEditorPage, component: IComponent) """
        ...

    def SetDirty(self, *args): #cannot find CLR method
        """ SetDirty(self: ComponentEditorPage) """
        ...

    def SetSite(self, site:IComponentEditorPageSite): # -> 
        """ SetSite(self: ComponentEditorPage, site: IComponentEditorPageSite) """
        ...

    def ShowHelp(self): # -> 
        """ ShowHelp(self: ComponentEditorPage) """
        ...

    def SupportsHelp(self) -> bool:
        """ SupportsHelp(self: ComponentEditorPage) -> bool """
        ...

    AutoSizeChanged = ...


class ComponentTray(IExtenderProvider, ScrollableControl, ISelectionUIHandler, IOleDragClient): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IViewObject2'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'object'>
    """ ComponentTray(mainDesigner: IDesigner, serviceProvider: IServiceProvider) """
    @property
    def AutoArrange(self) -> bool:
        """
        Get: AutoArrange(self: ComponentTray) -> bool
        Set: AutoArrange(self: ComponentTray) = value
        """
        ...

    @property
    def ComponentCount(self) -> int:
        """ Get: ComponentCount(self: ComponentTray) -> int """
        ...

    @property
    def ShowLargeIcons(self) -> bool:
        """
        Get: ShowLargeIcons(self: ComponentTray) -> bool
        Set: ShowLargeIcons(self: ComponentTray) = value
        """
        ...


    def AddComponent(self, component:IComponent): # -> 
        """ AddComponent(self: ComponentTray, component: IComponent) """
        ...

    def CanCreateComponentFromTool(self, *args): #cannot find CLR method
        """ CanCreateComponentFromTool(self: ComponentTray, tool: ToolboxItem) -> bool """
        ...

    def CanDisplayComponent(self, *args): #cannot find CLR method
        """ CanDisplayComponent(self: ComponentTray, component: IComponent) -> bool """
        ...

    def CreateComponentFromTool(self, tool:ToolboxItem): # -> 
        """ CreateComponentFromTool(self: ComponentTray, tool: ToolboxItem) """
        ...

    def DisplayError(self, *args): #cannot find CLR method
        """ DisplayError(self: ComponentTray, e: Exception) """
        ...

    def GetLocation(self, receiver:IComponent) -> Point:
        """ GetLocation(self: ComponentTray, receiver: IComponent) -> Point """
        ...

    def GetNextComponent(self, component:IComponent, forward:bool) -> IComponent:
        """ GetNextComponent(self: ComponentTray, component: IComponent, forward: bool) -> IComponent """
        ...

    def GetTrayLocation(self, receiver:IComponent) -> Point:
        """ GetTrayLocation(self: ComponentTray, receiver: IComponent) -> Point """
        ...

    def IsTrayComponent(self, comp:IComponent) -> bool:
        """ IsTrayComponent(self: ComponentTray, comp: IComponent) -> bool """
        ...

    def OnLostCapture(self, *args): #cannot find CLR method
        """ OnLostCapture(self: ComponentTray) """
        ...

    def OnSetCursor(self, *args): #cannot find CLR method
        """ OnSetCursor(self: ComponentTray) """
        ...

    def RemoveComponent(self, component:IComponent): # -> 
        """ RemoveComponent(self: ComponentTray, component: IComponent) """
        ...

    def SetLocation(self, receiver:IComponent, location:Point): # -> 
        """ SetLocation(self: ComponentTray, receiver: IComponent, location: Point) """
        ...

    def SetTrayLocation(self, receiver:IComponent, location:Point): # -> 
        """ SetTrayLocation(self: ComponentTray, receiver: IComponent, location: Point) """
        ...

    def __new__(cls, mainDesigner:IDesigner, serviceProvider:IServiceProvider) -> Self:
        """ __new__(cls: type, mainDesigner: IDesigner, serviceProvider: IServiceProvider) """
        ...


class ControlDesigner(ComponentDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ControlDesigner() """
    @property
    def AccessibilityObject(self) -> AccessibleObject:
        """ Get: AccessibilityObject(self: ControlDesigner) -> AccessibleObject """
        ...

    @property
    def AutoResizeHandles(self) -> bool:
        """
        Get: AutoResizeHandles(self: ControlDesigner) -> bool
        Set: AutoResizeHandles(self: ControlDesigner) = value
        """
        ...

    @property
    def BehaviorService(self):
        ...

    @property
    def Control(self) -> Control:
        """ Get: Control(self: ControlDesigner) -> Control """
        ...

    @property
    def EnableDragRect(self):
        ...

    @property
    def ParticipatesWithSnapLines(self) -> bool:
        """ Get: ParticipatesWithSnapLines(self: ControlDesigner) -> bool """
        ...

    @property
    def SelectionRules(self) -> SelectionRules:
        """ Get: SelectionRules(self: ControlDesigner) -> SelectionRules """
        ...

    @property
    def SnapLines(self) -> IList:
        """ Get: SnapLines(self: ControlDesigner) -> IList """
        ...


    def BaseWndProc(self, *args): #cannot find CLR method
        """ BaseWndProc(self: ControlDesigner, m: Message) -> Message """
        ...

    def CanBeParentedTo(self, parentDesigner:IDesigner) -> bool:
        """ CanBeParentedTo(self: ControlDesigner, parentDesigner: IDesigner) -> bool """
        ...

    def ControlDesignerAccessibleObject(self, *args): #cannot find CLR method
        """ ControlDesignerAccessibleObject(designer: ControlDesigner, control: Control) """
        ...

    def DefWndProc(self, *args): #cannot find CLR method
        """ DefWndProc(self: ControlDesigner, m: Message) -> Message """
        ...

    def DisplayError(self, *args): #cannot find CLR method
        """ DisplayError(self: ControlDesigner, e: Exception) """
        ...

    def EnableDesignMode(self, *args): #cannot find CLR method
        """ EnableDesignMode(self: ControlDesigner, child: Control, name: str) -> bool """
        ...

    def EnableDragDrop(self, *args): #cannot find CLR method
        """ EnableDragDrop(self: ControlDesigner, value: bool) """
        ...

    def GetControlGlyph(self, *args): #cannot find CLR method
        """ GetControlGlyph(self: ControlDesigner, selectionType: GlyphSelectionType) -> ControlBodyGlyph """
        ...

    def GetGlyphs(self, selectionType:GlyphSelectionType) -> GlyphCollection:
        """ GetGlyphs(self: ControlDesigner, selectionType: GlyphSelectionType) -> GlyphCollection """
        ...

    def GetHitTest(self, *args): #cannot find CLR method
        """ GetHitTest(self: ControlDesigner, point: Point) -> bool """
        ...

    def HookChildControls(self, *args): #cannot find CLR method
        """ HookChildControls(self: ControlDesigner, firstChild: Control) """
        ...

    def InternalControlDesigner(self, internalControlIndex:int) -> ControlDesigner:
        """ InternalControlDesigner(self: ControlDesigner, internalControlIndex: int) -> ControlDesigner """
        ...

    def NumberOfInternalControlDesigners(self) -> int:
        """ NumberOfInternalControlDesigners(self: ControlDesigner) -> int """
        ...

    def OnContextMenu(self, *args): #cannot find CLR method
        """ OnContextMenu(self: ControlDesigner, x: int, y: int) """
        ...

    def OnCreateHandle(self, *args): #cannot find CLR method
        """ OnCreateHandle(self: ControlDesigner) """
        ...

    def OnDragComplete(self, *args): #cannot find CLR method
        """ OnDragComplete(self: ControlDesigner, de: DragEventArgs) """
        ...

    def OnDragDrop(self, *args): #cannot find CLR method
        """ OnDragDrop(self: ControlDesigner, de: DragEventArgs) """
        ...

    def OnDragEnter(self, *args): #cannot find CLR method
        """ OnDragEnter(self: ControlDesigner, de: DragEventArgs) """
        ...

    def OnDragLeave(self, *args): #cannot find CLR method
        """ OnDragLeave(self: ControlDesigner, e: EventArgs) """
        ...

    def OnDragOver(self, *args): #cannot find CLR method
        """ OnDragOver(self: ControlDesigner, de: DragEventArgs) """
        ...

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """ OnGiveFeedback(self: ControlDesigner, e: GiveFeedbackEventArgs) """
        ...

    def OnMouseDragBegin(self, *args): #cannot find CLR method
        """ OnMouseDragBegin(self: ControlDesigner, x: int, y: int) """
        ...

    def OnMouseDragEnd(self, *args): #cannot find CLR method
        """ OnMouseDragEnd(self: ControlDesigner, cancel: bool) """
        ...

    def OnMouseDragMove(self, *args): #cannot find CLR method
        """ OnMouseDragMove(self: ControlDesigner, x: int, y: int) """
        ...

    def OnMouseEnter(self, *args): #cannot find CLR method
        """ OnMouseEnter(self: ControlDesigner) """
        ...

    def OnMouseHover(self, *args): #cannot find CLR method
        """ OnMouseHover(self: ControlDesigner) """
        ...

    def OnMouseLeave(self, *args): #cannot find CLR method
        """ OnMouseLeave(self: ControlDesigner) """
        ...

    def OnPaintAdornments(self, *args): #cannot find CLR method
        """ OnPaintAdornments(self: ControlDesigner, pe: PaintEventArgs) """
        ...

    def OnSetCursor(self, *args): #cannot find CLR method
        """ OnSetCursor(self: ControlDesigner) """
        ...

    def UnhookChildControls(self, *args): #cannot find CLR method
        """ UnhookChildControls(self: ControlDesigner, firstChild: Control) """
        ...

    def WndProc(self, *args): #cannot find CLR method
        """ WndProc(self: ControlDesigner, m: Message) -> Message """
        ...

    accessibilityObj = ...
    InvalidPoint: Point = ...


class DesignerOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerOptions() """
    @property
    def EnableInSituEditing(self) -> bool:
        """
        Get: EnableInSituEditing(self: DesignerOptions) -> bool
        Set: EnableInSituEditing(self: DesignerOptions) = value
        """
        ...

    @property
    def GridSize(self) -> Size:
        """
        Get: GridSize(self: DesignerOptions) -> Size
        Set: GridSize(self: DesignerOptions) = value
        """
        ...

    @property
    def ObjectBoundSmartTagAutoShow(self) -> bool:
        """
        Get: ObjectBoundSmartTagAutoShow(self: DesignerOptions) -> bool
        Set: ObjectBoundSmartTagAutoShow(self: DesignerOptions) = value
        """
        ...

    @property
    def ShowGrid(self) -> bool:
        """
        Get: ShowGrid(self: DesignerOptions) -> bool
        Set: ShowGrid(self: DesignerOptions) = value
        """
        ...

    @property
    def SnapToGrid(self) -> bool:
        """
        Get: SnapToGrid(self: DesignerOptions) -> bool
        Set: SnapToGrid(self: DesignerOptions) = value
        """
        ...

    @property
    def UseOptimizedCodeGeneration(self) -> bool:
        """
        Get: UseOptimizedCodeGeneration(self: DesignerOptions) -> bool
        Set: UseOptimizedCodeGeneration(self: DesignerOptions) = value
        """
        ...

    @property
    def UseSmartTags(self) -> bool:
        """
        Get: UseSmartTags(self: DesignerOptions) -> bool
        Set: UseSmartTags(self: DesignerOptions) = value
        """
        ...

    @property
    def UseSnapLines(self) -> bool:
        """
        Get: UseSnapLines(self: DesignerOptions) -> bool
        Set: UseSnapLines(self: DesignerOptions) = value
        """
        ...



class DockEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DockEditor() """
    pass

class ParentControlDesigner(ControlDesigner, IOleDragClient): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ParentControlDesigner() """
    @property
    def AllowControlLasso(self):
        ...

    @property
    def AllowGenericDragBox(self):
        ...

    @property
    def AllowSetChildIndexOnDrop(self):
        ...

    @property
    def DefaultControlLocation(self):
        ...

    @property
    def DrawGrid(self):
        ...

    @property
    def GridSize(self):
        ...

    @property
    def MouseDragTool(self):
        ...


    def AddPaddingSnapLines(self, *args): #cannot find CLR method
        """ AddPaddingSnapLines(self: ParentControlDesigner, snapLines: ArrayList) -> ArrayList """
        ...

    def CanAddComponent(self, *args): #cannot find CLR method
        """ CanAddComponent(self: ParentControlDesigner, component: IComponent) -> bool """
        ...

    def CanParent(self, *__args:ControlDesigner) -> bool:
        """
        CanParent(self: ParentControlDesigner, controlDesigner: ControlDesigner) -> bool
        CanParent(self: ParentControlDesigner, control: Control) -> bool
        """
        ...

    def CreateTool(self, *args): #cannot find CLR method
        """ CreateTool(self: ParentControlDesigner, tool: ToolboxItem)CreateTool(self: ParentControlDesigner, tool: ToolboxItem, location: Point)CreateTool(self: ParentControlDesigner, tool: ToolboxItem, bounds: Rectangle) """
        ...

    def CreateToolCore(self, *args): #cannot find CLR method
        """ CreateToolCore(self: ParentControlDesigner, tool: ToolboxItem, x: int, y: int, width: int, height: int, hasLocation: bool, hasSize: bool) -> Array[IComponent] """
        ...

    def GetControl(self, *args): #cannot find CLR method
        """ GetControl(self: ParentControlDesigner, component: object) -> Control """
        ...

    def GetParentForComponent(self, *args): #cannot find CLR method
        """ GetParentForComponent(self: ParentControlDesigner, component: IComponent) -> Control """
        ...

    def GetUpdatedRect(self, *args): #cannot find CLR method
        """ GetUpdatedRect(self: ParentControlDesigner, originalRect: Rectangle, dragRect: Rectangle, updateSize: bool) -> Rectangle """
        ...

    def InvokeCreateTool(self, *args): #cannot find CLR method
        """ InvokeCreateTool(toInvoke: ParentControlDesigner, tool: ToolboxItem) """
        ...

    accessibilityObj = ...


class ScrollableControlDesigner(ParentControlDesigner): # skipped bases: <type 'IOleDragClient'>, <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'object'>
    """ ScrollableControlDesigner() """
    accessibilityObj = ...


class DocumentDesigner(IRootDesigner, IToolboxUser, ScrollableControlDesigner): # skipped bases: <type 'IOleDragClient'>, <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'object'>
    """ DocumentDesigner() """
    @property
    def SelectionRules(self) -> SelectionRules:
        """ Get: SelectionRules(self: DocumentDesigner) -> SelectionRules """
        ...


    def EnsureMenuEditorService(self, *args): #cannot find CLR method
        """ EnsureMenuEditorService(self: DocumentDesigner, c: IComponent) """
        ...

    def GetGlyphs(self, selectionType:GlyphSelectionType) -> GlyphCollection:
        """ GetGlyphs(self: DocumentDesigner, selectionType: GlyphSelectionType) -> GlyphCollection """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: DocumentDesigner, component: IComponent) """
        ...

    accessibilityObj = ...
    menuEditorService = ...


class EventHandlerService(IEventHandlerService): # skipped bases: <type 'object'>
    """ EventHandlerService(focusWnd: Control) """
    @property
    def FocusWindow(self) -> Control:
        """ Get: FocusWindow(self: EventHandlerService) -> Control """
        ...


    def GetHandler(self, handlerType:Type) -> object:
        """ GetHandler(self: EventHandlerService, handlerType: Type) -> object """
        ...

    def PopHandler(self, handler:object): # -> 
        """ PopHandler(self: EventHandlerService, handler: object) """
        ...

    def PushHandler(self, handler:object): # -> 
        """ PushHandler(self: EventHandlerService, handler: object) """
        ...

    EventHandlerChanged = ...


class PropertyTab(IExtenderProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bitmap(self) -> Bitmap:
        """ Get: Bitmap(self: PropertyTab) -> Bitmap """
        ...

    @property
    def Components(self) -> Array:
        """
        Get: Components(self: PropertyTab) -> Array[object]
        Set: Components(self: PropertyTab) = value
        """
        ...

    @property
    def HelpKeyword(self) -> str:
        """ Get: HelpKeyword(self: PropertyTab) -> str """
        ...

    @property
    def TabName(self) -> str:
        """ Get: TabName(self: PropertyTab) -> str """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: PropertyTab) """
        ...

    def GetDefaultProperty(self, component:object) -> PropertyDescriptor:
        """ GetDefaultProperty(self: PropertyTab, component: object) -> PropertyDescriptor """
        ...

    def GetProperties(self, *__args:object) -> PropertyDescriptorCollection:
        """
        GetProperties(self: PropertyTab, component: object) -> PropertyDescriptorCollection
        GetProperties(self: PropertyTab, context: ITypeDescriptorContext, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        GetProperties(self: PropertyTab, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        """
        ...


class EventsTab(PropertyTab): # skipped bases: <type 'IExtenderProvider'>, <type 'object'>
    """ EventsTab(sp: IServiceProvider) """
    def __new__(cls, sp:IServiceProvider) -> Self:
        """ __new__(cls: type, sp: IServiceProvider) """
        ...


class FileNameEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ FileNameEditor() """
    def InitializeDialog(self, *args): #cannot find CLR method
        """ InitializeDialog(self: FileNameEditor, openFileDialog: OpenFileDialog) """
        ...


class FolderNameEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ FolderNameEditor() """
    def FolderBrowser(self, *args): #cannot find CLR method
        """ FolderBrowser() """
        ...

    def FolderBrowserFolder(self, *args): #cannot find CLR method
        """ enum FolderBrowserFolder, values: Desktop (0), Favorites (6), MyComputer (17), MyDocuments (5), MyPictures (39), NetAndDialUpConnections (49), NetworkNeighborhood (18), Printers (4), Recent (8), SendTo (9), StartMenu (11), Templates (21) """
        ...

    def FolderBrowserStyles(self, *args): #cannot find CLR method
        """ enum (flags) FolderBrowserStyles, values: BrowseForComputer (4096), BrowseForEverything (16384), BrowseForPrinter (8192), RestrictToDomain (2), RestrictToFilesystem (1), RestrictToSubfolders (8), ShowTextBox (16) """
        ...

    def InitializeDialog(self, *args): #cannot find CLR method
        """ InitializeDialog(self: FolderNameEditor, folderBrowser: FolderBrowser) """
        ...



class IContainsThemedScrollbarWindows: # skipped bases: <type 'object'>
    """ no doc """
    def ThemedScrollbarWindows(self) -> IEnumerable:
        """ ThemedScrollbarWindows(self: IContainsThemedScrollbarWindows) -> IEnumerable """
        ...


class ImageListCodeDomSerializer(CodeDomSerializer): # skipped bases: <type 'object'>
    """ ImageListCodeDomSerializer() """
    pass

class ImageListImageEditor(ImageEditor): # skipped bases: <type 'object'>
    """ ImageListImageEditor() """
    pass

class IMenuEditorService: # skipped bases: <type 'object'>
    """ no doc """
    def GetMenu(self) -> Menu:
        """ GetMenu(self: IMenuEditorService) -> Menu """
        ...

    def IsActive(self) -> bool:
        """ IsActive(self: IMenuEditorService) -> bool """
        ...

    def MessageFilter(self, m:Message) -> Tuple_[bool, Message]:
        """ MessageFilter(self: IMenuEditorService, m: Message) -> (bool, Message) """
        ...

    def SetMenu(self, menu:Menu): # -> 
        """ SetMenu(self: IMenuEditorService, menu: Menu) """
        ...

    def SetSelection(self, item:MenuItem): # -> 
        """ SetSelection(self: IMenuEditorService, item: MenuItem) """
        ...


class IUIService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Styles(self) -> IDictionary:
        """ Get: Styles(self: IUIService) -> IDictionary """
        ...


    def CanShowComponentEditor(self, component:object) -> bool:
        """ CanShowComponentEditor(self: IUIService, component: object) -> bool """
        ...

    def GetDialogOwnerWindow(self) -> IWin32Window:
        """ GetDialogOwnerWindow(self: IUIService) -> IWin32Window """
        ...

    def SetUIDirty(self): # -> 
        """ SetUIDirty(self: IUIService) """
        ...

    def ShowComponentEditor(self, component:object, parent:IWin32Window) -> bool:
        """ ShowComponentEditor(self: IUIService, component: object, parent: IWin32Window) -> bool """
        ...

    def ShowDialog(self, form:Form) -> DialogResult:
        """ ShowDialog(self: IUIService, form: Form) -> DialogResult """
        ...

    def ShowError(self, *__args:str): # -> 
        """ ShowError(self: IUIService, message: str)ShowError(self: IUIService, ex: Exception)ShowError(self: IUIService, ex: Exception, message: str) """
        ...

    def ShowMessage(self, message:str, caption:str = ..., buttons:MessageBoxButtons = ...) -> DialogResult:
        """ ShowMessage(self: IUIService, message: str)ShowMessage(self: IUIService, message: str, caption: str)ShowMessage(self: IUIService, message: str, caption: str, buttons: MessageBoxButtons) -> DialogResult """
        ...

    def ShowToolWindow(self, toolWindow:Guid) -> bool:
        """ ShowToolWindow(self: IUIService, toolWindow: Guid) -> bool """
        ...


class IWindowsFormsEditorService: # skipped bases: <type 'object'>
    """ no doc """
    def CloseDropDown(self): # -> 
        """ CloseDropDown(self: IWindowsFormsEditorService) """
        ...

    def DropDownControl(self, control:Control): # -> 
        """ DropDownControl(self: IWindowsFormsEditorService, control: Control) """
        ...

    def ShowDialog(self, dialog:Form) -> DialogResult:
        """ ShowDialog(self: IWindowsFormsEditorService, dialog: Form) -> DialogResult """
        ...


class MaskDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: MaskDescriptor) -> CultureInfo """
        ...

    @property
    def Mask(self) -> str:
        """ Get: Mask(self: MaskDescriptor) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MaskDescriptor) -> str """
        ...

    @property
    def Sample(self) -> str:
        """ Get: Sample(self: MaskDescriptor) -> str """
        ...

    @property
    def ValidatingType(self) -> Type:
        """ Get: ValidatingType(self: MaskDescriptor) -> Type """
        ...


    def Equals(self, maskDescriptor:object) -> bool:
        """ Equals(self: MaskDescriptor, maskDescriptor: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MaskDescriptor) -> int """
        ...

    @staticmethod
    def IsValidMaskDescriptor(maskDescriptor, validationErrorDescription=None) -> bool:
        """
        IsValidMaskDescriptor(maskDescriptor: MaskDescriptor) -> bool
        IsValidMaskDescriptor(maskDescriptor: MaskDescriptor) -> (bool, str)
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: MaskDescriptor) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MenuCommands(StandardCommands): # skipped bases: <type 'object'>
    """ MenuCommands() """
    ComponentTrayMenu: CommandID = ...
    ContainerMenu: CommandID = ...
    DesignerProperties: CommandID = ...
    EditLabel: CommandID = ...
    KeyCancel: CommandID = ...
    KeyDefaultAction: CommandID = ...
    KeyEnd: CommandID = ...
    KeyHome: CommandID = ...
    KeyInvokeSmartTag: CommandID = ...
    KeyMoveDown: CommandID = ...
    KeyMoveLeft: CommandID = ...
    KeyMoveRight: CommandID = ...
    KeyMoveUp: CommandID = ...
    KeyNudgeDown: CommandID = ...
    KeyNudgeHeightDecrease: CommandID = ...
    KeyNudgeHeightIncrease: CommandID = ...
    KeyNudgeLeft: CommandID = ...
    KeyNudgeRight: CommandID = ...
    KeyNudgeUp: CommandID = ...
    KeyNudgeWidthDecrease: CommandID = ...
    KeyNudgeWidthIncrease: CommandID = ...
    KeyReverseCancel: CommandID = ...
    KeySelectNext: CommandID = ...
    KeySelectPrevious: CommandID = ...
    KeyShiftEnd: CommandID = ...
    KeyShiftHome: CommandID = ...
    KeySizeHeightDecrease: CommandID = ...
    KeySizeHeightIncrease: CommandID = ...
    KeySizeWidthDecrease: CommandID = ...
    KeySizeWidthIncrease: CommandID = ...
    KeyTabOrderSelect: CommandID = ...
    SelectionMenu: CommandID = ...
    SetStatusRectangle: CommandID = ...
    SetStatusText: CommandID = ...
    TraySelectionMenu: CommandID = ...


class SelectionRules(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SelectionRules, values: AllSizeable (15), BottomSizeable (2), LeftSizeable (4), Locked (-2147483648), Moveable (268435456), None (0), RightSizeable (8), TopSizeable (1), Visible (1073741824) """
    AllSizeable: SelectionRules = ...
    BottomSizeable: SelectionRules = ...
    LeftSizeable: SelectionRules = ...
    Locked: SelectionRules = ...
    Moveable: SelectionRules = ...
    RightSizeable: SelectionRules = ...
    TopSizeable: SelectionRules = ...
    value__ = ...
    Visible: SelectionRules = ...


class ShortcutKeysEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ShortcutKeysEditor() """
    pass

class ThemedScrollbarMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThemedScrollbarMode, values: All (1), None (2), OnlyTopLevel (3) """
    All: ThemedScrollbarMode = ...
    OnlyTopLevel: ThemedScrollbarMode = ...
    value__ = ...


class ThemedScrollbarWindow: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Handle = ...
    Mode = ...


class ToolStripItemDesignerAvailability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ToolStripItemDesignerAvailability, values: All (15), ContextMenuStrip (4), MenuStrip (2), None (0), StatusStrip (8), ToolStrip (1) """
    All: ToolStripItemDesignerAvailability = ...
    ContextMenuStrip: ToolStripItemDesignerAvailability = ...
    MenuStrip: ToolStripItemDesignerAvailability = ...
    StatusStrip: ToolStripItemDesignerAvailability = ...
    ToolStrip: ToolStripItemDesignerAvailability = ...
    value__ = ...


class ToolStripItemDesignerAvailabilityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ToolStripItemDesignerAvailabilityAttribute()
    ToolStripItemDesignerAvailabilityAttribute(visibility: ToolStripItemDesignerAvailability)
    """
    @property
    def ItemAdditionVisibility(self) -> ToolStripItemDesignerAvailability:
        """ Get: ItemAdditionVisibility(self: ToolStripItemDesignerAvailabilityAttribute) -> ToolStripItemDesignerAvailability """
        ...


    def __new__(cls, visibility:ToolStripItemDesignerAvailability = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, visibility: ToolStripItemDesignerAvailability)
        """
        ...

    Default: ToolStripItemDesignerAvailabilityAttribute = ...


class WindowsFormsComponentEditor(ComponentEditor): # skipped bases: <type 'object'>
    """ no doc """
    def GetComponentEditorPages(self, *args): #cannot find CLR method
        """ GetComponentEditorPages(self: WindowsFormsComponentEditor) -> Array[Type] """
        ...

    def GetInitialComponentEditorPageIndex(self, *args): #cannot find CLR method
        """ GetInitialComponentEditorPageIndex(self: WindowsFormsComponentEditor) -> int """
        ...


class WindowsFormsDesignerOptionService(DesignerOptionService): # skipped bases: <type 'IDesignerOptionService'>, <type 'object'>
    """ WindowsFormsDesignerOptionService() """
    @property
    def CompatibilityOptions(self) -> DesignerOptions:
        """ Get: CompatibilityOptions(self: WindowsFormsDesignerOptionService) -> DesignerOptions """
        ...



# variables with complex values

