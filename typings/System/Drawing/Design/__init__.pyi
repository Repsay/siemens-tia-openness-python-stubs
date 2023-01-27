# encoding: utf-8
# module System.Drawing.Design calls itself Design
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Drawing.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    IServiceProvider, MulticastDelegate, Type)

from System.Collections import (ArrayList, ICollection, IDictionary, 
    ReadOnlyCollectionBase)

from System.ComponentModel import ITypeDescriptorContext, PropertyDescriptor

from System.ComponentModel.Design import (IComponentDiscoveryService, 
    IDesignerHost)

from System.Drawing import Bitmap, Graphics, Image, Rectangle

from System.Reflection import AssemblyName

from System.Runtime.InteropServices.ComTypes import IDataObject

from System.Runtime.Serialization import ISerializable

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class UITypeEditor: # skipped bases: <type 'object'>, <type 'object'>
    """ UITypeEditor() """
    @property
    def IsDropDownResizable(self) -> bool:
        """ Get: IsDropDownResizable(self: UITypeEditor) -> bool """
        ...


    def EditValue(self, *__args) -> object:
        """
        EditValue(self: UITypeEditor, provider: IServiceProvider, value: object) -> object
        EditValue(self: UITypeEditor, context: ITypeDescriptorContext, provider: IServiceProvider, value: object) -> object
        """
        ...

    def GetEditStyle(self, context:ITypeDescriptorContext = ...) -> UITypeEditorEditStyle:
        """
        GetEditStyle(self: UITypeEditor) -> UITypeEditorEditStyle
        GetEditStyle(self: UITypeEditor, context: ITypeDescriptorContext) -> UITypeEditorEditStyle
        """
        ...

    def GetPaintValueSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """
        GetPaintValueSupported(self: UITypeEditor) -> bool
        GetPaintValueSupported(self: UITypeEditor, context: ITypeDescriptorContext) -> bool
        """
        ...

    def PaintValue(self, *__args:PaintValueEventArgs): # -> 
        """ PaintValue(self: UITypeEditor, value: object, canvas: Graphics, rectangle: Rectangle)PaintValue(self: UITypeEditor, e: PaintValueEventArgs) """
        ...


class ImageEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ImageEditor() """
    def CreateExtensionsString(self, *args): #cannot find CLR method
        """ CreateExtensionsString(extensions: Array[str], sep: str) -> str """
        ...

    def CreateFilterEntry(self, *args): #cannot find CLR method
        """ CreateFilterEntry(e: ImageEditor) -> str """
        ...

    def GetExtensions(self, *args): #cannot find CLR method
        """ GetExtensions(self: ImageEditor) -> Array[str] """
        ...

    def GetFileDialogDescription(self, *args): #cannot find CLR method
        """ GetFileDialogDescription(self: ImageEditor) -> str """
        ...

    def GetImageExtenders(self, *args): #cannot find CLR method
        """ GetImageExtenders(self: ImageEditor) -> Array[Type] """
        ...

    def LoadFromStream(self, *args): #cannot find CLR method
        """ LoadFromStream(self: ImageEditor, stream: Stream) -> Image """
        ...


class BitmapEditor(ImageEditor): # skipped bases: <type 'object'>
    """ BitmapEditor() """
    pass

class CategoryNameCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    CategoryNameCollection(value: CategoryNameCollection)
    CategoryNameCollection(value: Array[str])
    """
    def Contains(self, value:str) -> bool:
        """ Contains(self: CategoryNameCollection, value: str) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CategoryNameCollection, array: Array[str], index: int) """
        ...

    def IndexOf(self, value:str) -> int:
        """ IndexOf(self: CategoryNameCollection, value: str) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, value:CategoryNameCollection) -> Self:
        """
        __new__(cls: type, value: CategoryNameCollection)
        __new__(cls: type, value: Array[str])
        """
        ...


class ColorEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ColorEditor() """
    pass

class ContentAlignmentEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ContentAlignmentEditor() """
    pass

class CursorEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ CursorEditor() """
    pass

class FontEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ FontEditor() """
    pass

class FontNameEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ FontNameEditor() """
    pass

class IconEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ IconEditor() """
    def CreateExtensionsString(self, *args): #cannot find CLR method
        """ CreateExtensionsString(extensions: Array[str], sep: str) -> str """
        ...

    def CreateFilterEntry(self, *args): #cannot find CLR method
        """ CreateFilterEntry(e: IconEditor) -> str """
        ...

    def GetExtensions(self, *args): #cannot find CLR method
        """ GetExtensions(self: IconEditor) -> Array[str] """
        ...

    def GetFileDialogDescription(self, *args): #cannot find CLR method
        """ GetFileDialogDescription(self: IconEditor) -> str """
        ...

    def LoadFromStream(self, *args): #cannot find CLR method
        """ LoadFromStream(self: IconEditor, stream: Stream) -> Icon """
        ...


class IPropertyValueUIService: # skipped bases: <type 'object'>
    """ no doc """
    def AddPropertyValueUIHandler(self, newHandler:PropertyValueUIHandler): # -> 
        """ AddPropertyValueUIHandler(self: IPropertyValueUIService, newHandler: PropertyValueUIHandler) """
        ...

    def GetPropertyUIValueItems(self, context:ITypeDescriptorContext, propDesc:PropertyDescriptor) -> Array:
        """ GetPropertyUIValueItems(self: IPropertyValueUIService, context: ITypeDescriptorContext, propDesc: PropertyDescriptor) -> Array[PropertyValueUIItem] """
        ...

    def NotifyPropertyValueUIItemsChanged(self): # -> 
        """ NotifyPropertyValueUIItemsChanged(self: IPropertyValueUIService) """
        ...

    def RemovePropertyValueUIHandler(self, newHandler:PropertyValueUIHandler): # -> 
        """ RemovePropertyValueUIHandler(self: IPropertyValueUIService, newHandler: PropertyValueUIHandler) """
        ...

    PropertyUIValueItemsChanged = ...


class IToolboxItemProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Items(self) -> ToolboxItemCollection:
        """ Get: Items(self: IToolboxItemProvider) -> ToolboxItemCollection """
        ...



class IToolboxService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CategoryNames(self) -> CategoryNameCollection:
        """ Get: CategoryNames(self: IToolboxService) -> CategoryNameCollection """
        ...

    @property
    def SelectedCategory(self) -> str:
        """
        Get: SelectedCategory(self: IToolboxService) -> str
        Set: SelectedCategory(self: IToolboxService) = value
        """
        ...


    def AddCreator(self, creator:ToolboxItemCreatorCallback, format:str, host:IDesignerHost = ...): # -> 
        """ AddCreator(self: IToolboxService, creator: ToolboxItemCreatorCallback, format: str)AddCreator(self: IToolboxService, creator: ToolboxItemCreatorCallback, format: str, host: IDesignerHost) """
        ...

    def AddLinkedToolboxItem(self, toolboxItem:ToolboxItem, *__args:IDesignerHost): # -> 
        """ AddLinkedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, host: IDesignerHost)AddLinkedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str, host: IDesignerHost) """
        ...

    def AddToolboxItem(self, toolboxItem:ToolboxItem, category:str = ...): # -> 
        """ AddToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem)AddToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str) """
        ...

    def DeserializeToolboxItem(self, serializedObject:object, host:IDesignerHost = ...) -> ToolboxItem:
        """
        DeserializeToolboxItem(self: IToolboxService, serializedObject: object) -> ToolboxItem
        DeserializeToolboxItem(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> ToolboxItem
        """
        ...

    def GetSelectedToolboxItem(self, host:IDesignerHost = ...) -> ToolboxItem:
        """
        GetSelectedToolboxItem(self: IToolboxService) -> ToolboxItem
        GetSelectedToolboxItem(self: IToolboxService, host: IDesignerHost) -> ToolboxItem
        """
        ...

    def GetToolboxItems(self, *__args:IDesignerHost) -> ToolboxItemCollection:
        """
        GetToolboxItems(self: IToolboxService) -> ToolboxItemCollection
        GetToolboxItems(self: IToolboxService, host: IDesignerHost) -> ToolboxItemCollection
        GetToolboxItems(self: IToolboxService, category: str) -> ToolboxItemCollection
        GetToolboxItems(self: IToolboxService, category: str, host: IDesignerHost) -> ToolboxItemCollection
        """
        ...

    def IsSupported(self, serializedObject:object, *__args:IDesignerHost) -> bool:
        """
        IsSupported(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> bool
        IsSupported(self: IToolboxService, serializedObject: object, filterAttributes: ICollection) -> bool
        """
        ...

    def IsToolboxItem(self, serializedObject:object, host:IDesignerHost = ...) -> bool:
        """
        IsToolboxItem(self: IToolboxService, serializedObject: object) -> bool
        IsToolboxItem(self: IToolboxService, serializedObject: object, host: IDesignerHost) -> bool
        """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: IToolboxService) """
        ...

    def RemoveCreator(self, format:str, host:IDesignerHost = ...): # -> 
        """ RemoveCreator(self: IToolboxService, format: str)RemoveCreator(self: IToolboxService, format: str, host: IDesignerHost) """
        ...

    def RemoveToolboxItem(self, toolboxItem:ToolboxItem, category:str = ...): # -> 
        """ RemoveToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem)RemoveToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem, category: str) """
        ...

    def SelectedToolboxItemUsed(self): # -> 
        """ SelectedToolboxItemUsed(self: IToolboxService) """
        ...

    def SerializeToolboxItem(self, toolboxItem:ToolboxItem) -> object:
        """ SerializeToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem) -> object """
        ...

    def SetCursor(self) -> bool:
        """ SetCursor(self: IToolboxService) -> bool """
        ...

    def SetSelectedToolboxItem(self, toolboxItem:ToolboxItem): # -> 
        """ SetSelectedToolboxItem(self: IToolboxService, toolboxItem: ToolboxItem) """
        ...


class IToolboxUser: # skipped bases: <type 'object'>
    """ no doc """
    def GetToolSupported(self, tool:ToolboxItem) -> bool:
        """ GetToolSupported(self: IToolboxUser, tool: ToolboxItem) -> bool """
        ...

    def ToolPicked(self, tool:ToolboxItem): # -> 
        """ ToolPicked(self: IToolboxUser, tool: ToolboxItem) """
        ...


class MetafileEditor(ImageEditor): # skipped bases: <type 'object'>
    """ MetafileEditor() """
    pass

class PaintValueEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PaintValueEventArgs(context: ITypeDescriptorContext, value: object, graphics: Graphics, bounds: Rectangle) """
    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: PaintValueEventArgs) -> Rectangle """
        ...

    @property
    def Context(self) -> ITypeDescriptorContext:
        """ Get: Context(self: PaintValueEventArgs) -> ITypeDescriptorContext """
        ...

    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: PaintValueEventArgs) -> Graphics """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: PaintValueEventArgs) -> object """
        ...


    def __new__(cls, context:ITypeDescriptorContext, value:object, graphics:Graphics, bounds:Rectangle) -> Self:
        """ __new__(cls: type, context: ITypeDescriptorContext, value: object, graphics: Graphics, bounds: Rectangle) """
        ...


class PropertyValueUIHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PropertyValueUIHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, context:ITypeDescriptorContext, propDesc:PropertyDescriptor, valueUIItemList:ArrayList, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PropertyValueUIHandler, context: ITypeDescriptorContext, propDesc: PropertyDescriptor, valueUIItemList: ArrayList, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PropertyValueUIHandler, result: IAsyncResult) """
        ...

    def Invoke(self, context:ITypeDescriptorContext, propDesc:PropertyDescriptor, valueUIItemList:ArrayList): # -> 
        """ Invoke(self: PropertyValueUIHandler, context: ITypeDescriptorContext, propDesc: PropertyDescriptor, valueUIItemList: ArrayList) """
        ...


class PropertyValueUIItem: # skipped bases: <type 'object'>, <type 'object'>
    """ PropertyValueUIItem(uiItemImage: Image, handler: PropertyValueUIItemInvokeHandler, tooltip: str) """
    @property
    def Image(self) -> Image:
        """ Get: Image(self: PropertyValueUIItem) -> Image """
        ...

    @property
    def InvokeHandler(self) -> PropertyValueUIItemInvokeHandler:
        """ Get: InvokeHandler(self: PropertyValueUIItem) -> PropertyValueUIItemInvokeHandler """
        ...

    @property
    def ToolTip(self) -> str:
        """ Get: ToolTip(self: PropertyValueUIItem) -> str """
        ...


    def Reset(self): # -> 
        """ Reset(self: PropertyValueUIItem) """
        ...


class PropertyValueUIItemInvokeHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PropertyValueUIItemInvokeHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, context:ITypeDescriptorContext, descriptor:PropertyDescriptor, invokedItem:PropertyValueUIItem, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PropertyValueUIItemInvokeHandler, context: ITypeDescriptorContext, descriptor: PropertyDescriptor, invokedItem: PropertyValueUIItem, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PropertyValueUIItemInvokeHandler, result: IAsyncResult) """
        ...

    def Invoke(self, context:ITypeDescriptorContext, descriptor:PropertyDescriptor, invokedItem:PropertyValueUIItem): # -> 
        """ Invoke(self: PropertyValueUIItemInvokeHandler, context: ITypeDescriptorContext, descriptor: PropertyDescriptor, invokedItem: PropertyValueUIItem) """
        ...


class ToolboxComponentsCreatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ToolboxComponentsCreatedEventArgs(components: Array[IComponent]) """
    @property
    def Components(self) -> Array:
        """ Get: Components(self: ToolboxComponentsCreatedEventArgs) -> Array[IComponent] """
        ...


    def __new__(cls, components:Array) -> Self:
        """ __new__(cls: type, components: Array[IComponent]) """
        ...


class ToolboxComponentsCreatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ToolboxComponentsCreatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ToolboxComponentsCreatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ToolboxComponentsCreatedEventHandler, sender: object, e: ToolboxComponentsCreatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ToolboxComponentsCreatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ToolboxComponentsCreatedEventArgs): # -> 
        """ Invoke(self: ToolboxComponentsCreatedEventHandler, sender: object, e: ToolboxComponentsCreatedEventArgs) """
        ...


class ToolboxComponentsCreatingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ToolboxComponentsCreatingEventArgs(host: IDesignerHost) """
    @property
    def DesignerHost(self) -> IDesignerHost:
        """ Get: DesignerHost(self: ToolboxComponentsCreatingEventArgs) -> IDesignerHost """
        ...


    def __new__(cls, host:IDesignerHost) -> Self:
        """ __new__(cls: type, host: IDesignerHost) """
        ...


class ToolboxComponentsCreatingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ToolboxComponentsCreatingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ToolboxComponentsCreatingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ToolboxComponentsCreatingEventHandler, sender: object, e: ToolboxComponentsCreatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ToolboxComponentsCreatingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ToolboxComponentsCreatingEventArgs): # -> 
        """ Invoke(self: ToolboxComponentsCreatingEventHandler, sender: object, e: ToolboxComponentsCreatingEventArgs) """
        ...


class ToolboxItem(ISerializable): # skipped bases: <type 'object'>
    """
    ToolboxItem()
    ToolboxItem(toolType: Type)
    """
    @property
    def AssemblyName(self) -> AssemblyName:
        """
        Get: AssemblyName(self: ToolboxItem) -> AssemblyName
        Set: AssemblyName(self: ToolboxItem) = value
        """
        ...

    @property
    def Bitmap(self) -> Bitmap:
        """
        Get: Bitmap(self: ToolboxItem) -> Bitmap
        Set: Bitmap(self: ToolboxItem) = value
        """
        ...

    @property
    def Company(self) -> str:
        """
        Get: Company(self: ToolboxItem) -> str
        Set: Company(self: ToolboxItem) = value
        """
        ...

    @property
    def ComponentType(self) -> str:
        """ Get: ComponentType(self: ToolboxItem) -> str """
        ...

    @property
    def DependentAssemblies(self) -> Array:
        """
        Get: DependentAssemblies(self: ToolboxItem) -> Array[AssemblyName]
        Set: DependentAssemblies(self: ToolboxItem) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ToolboxItem) -> str
        Set: Description(self: ToolboxItem) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ToolboxItem) -> str
        Set: DisplayName(self: ToolboxItem) = value
        """
        ...

    @property
    def Filter(self) -> ICollection:
        """
        Get: Filter(self: ToolboxItem) -> ICollection
        Set: Filter(self: ToolboxItem) = value
        """
        ...

    @property
    def IsTransient(self) -> bool:
        """
        Get: IsTransient(self: ToolboxItem) -> bool
        Set: IsTransient(self: ToolboxItem) = value
        """
        ...

    @property
    def Locked(self) -> bool:
        """ Get: Locked(self: ToolboxItem) -> bool """
        ...

    @property
    def OriginalBitmap(self) -> Bitmap:
        """
        Get: OriginalBitmap(self: ToolboxItem) -> Bitmap
        Set: OriginalBitmap(self: ToolboxItem) = value
        """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: ToolboxItem) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ToolboxItem) -> str
        Set: TypeName(self: ToolboxItem) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ToolboxItem) -> str """
        ...


    def CheckUnlocked(self, *args): #cannot find CLR method
        """ CheckUnlocked(self: ToolboxItem) """
        ...

    def CreateComponents(self, host:IDesignerHost = ..., defaultValues:IDictionary = ...) -> Array:
        """
        CreateComponents(self: ToolboxItem) -> Array[IComponent]
        CreateComponents(self: ToolboxItem, host: IDesignerHost) -> Array[IComponent]
        CreateComponents(self: ToolboxItem, host: IDesignerHost, defaultValues: IDictionary) -> Array[IComponent]
        """
        ...

    def CreateComponentsCore(self, *args): #cannot find CLR method
        """
        CreateComponentsCore(self: ToolboxItem, host: IDesignerHost, defaultValues: IDictionary) -> Array[IComponent]
        CreateComponentsCore(self: ToolboxItem, host: IDesignerHost) -> Array[IComponent]
        """
        ...

    def Deserialize(self, *args): #cannot find CLR method
        """ Deserialize(self: ToolboxItem, info: SerializationInfo, context: StreamingContext) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ToolboxItem, obj: object) -> bool """
        ...

    def FilterPropertyValue(self, *args): #cannot find CLR method
        """ FilterPropertyValue(self: ToolboxItem, propertyName: str, value: object) -> object """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ToolboxItem) -> int """
        ...

    def GetType(self, host:IDesignerHost = ...) -> Type:
        """ GetType(self: ToolboxItem, host: IDesignerHost) -> Type """
        ...

    def Initialize(self, type:Type): # -> 
        """ Initialize(self: ToolboxItem, type: Type) """
        ...

    def Lock(self): # -> 
        """ Lock(self: ToolboxItem) """
        ...

    def OnComponentsCreated(self, *args): #cannot find CLR method
        """ OnComponentsCreated(self: ToolboxItem, args: ToolboxComponentsCreatedEventArgs) """
        ...

    def OnComponentsCreating(self, *args): #cannot find CLR method
        """ OnComponentsCreating(self: ToolboxItem, args: ToolboxComponentsCreatingEventArgs) """
        ...

    def Serialize(self, *args): #cannot find CLR method
        """ Serialize(self: ToolboxItem, info: SerializationInfo, context: StreamingContext) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ToolboxItem) -> str """
        ...

    def ValidatePropertyType(self, *args): #cannot find CLR method
        """ ValidatePropertyType(self: ToolboxItem, propertyName: str, value: object, expectedType: Type, allowNull: bool) """
        ...

    def ValidatePropertyValue(self, *args): #cannot find CLR method
        """ ValidatePropertyValue(self: ToolboxItem, propertyName: str, value: object) -> object """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    ComponentsCreated = ...
    ComponentsCreating = ...


class ToolboxItemCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ToolboxItemCollection(value: ToolboxItemCollection)
    ToolboxItemCollection(value: Array[ToolboxItem])
    """
    def Contains(self, value:ToolboxItem) -> bool:
        """ Contains(self: ToolboxItemCollection, value: ToolboxItem) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ToolboxItemCollection, array: Array[ToolboxItem], index: int) """
        ...

    def IndexOf(self, value:ToolboxItem) -> int:
        """ IndexOf(self: ToolboxItemCollection, value: ToolboxItem) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, value:ToolboxItemCollection) -> Self:
        """
        __new__(cls: type, value: ToolboxItemCollection)
        __new__(cls: type, value: Array[ToolboxItem])
        """
        ...


class ToolboxItemContainer(ISerializable): # skipped bases: <type 'object'>
    """
    ToolboxItemContainer(item: ToolboxItem)
    ToolboxItemContainer(data: IDataObject)
    """
    @property
    def IsCreated(self) -> bool:
        """ Get: IsCreated(self: ToolboxItemContainer) -> bool """
        ...

    @property
    def IsTransient(self) -> bool:
        """ Get: IsTransient(self: ToolboxItemContainer) -> bool """
        ...

    @property
    def ToolboxData(self) -> IDataObject:
        """ Get: ToolboxData(self: ToolboxItemContainer) -> IDataObject """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ToolboxItemContainer, obj: object) -> bool """
        ...

    def GetFilter(self, creators:ICollection) -> ICollection:
        """ GetFilter(self: ToolboxItemContainer, creators: ICollection) -> ICollection """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ToolboxItemContainer) -> int """
        ...

    def GetToolboxItem(self, creators:ICollection) -> ToolboxItem:
        """ GetToolboxItem(self: ToolboxItemContainer, creators: ICollection) -> ToolboxItem """
        ...

    def UpdateFilter(self, item:ToolboxItem): # -> 
        """ UpdateFilter(self: ToolboxItemContainer, item: ToolboxItem) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ToolboxItemCreator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Format(self) -> str:
        """ Get: Format(self: ToolboxItemCreator) -> str """
        ...


    def Create(self, data:IDataObject) -> ToolboxItem:
        """ Create(self: ToolboxItemCreator, data: IDataObject) -> ToolboxItem """
        ...


class ToolboxItemCreatorCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ToolboxItemCreatorCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, serializedObject:object, format:str, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ToolboxItemCreatorCallback, serializedObject: object, format: str, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> ToolboxItem:
        """ EndInvoke(self: ToolboxItemCreatorCallback, result: IAsyncResult) -> ToolboxItem """
        ...

    def Invoke(self, serializedObject:object, format:str) -> ToolboxItem:
        """ Invoke(self: ToolboxItemCreatorCallback, serializedObject: object, format: str) -> ToolboxItem """
        ...


class ToolboxService(IToolboxService, IComponentDiscoveryService): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SelectedItemContainer(self):
        ...


    def CreateItemContainer(self, *args): #cannot find CLR method
        """
        CreateItemContainer(self: ToolboxService, item: ToolboxItem, link: IDesignerHost) -> ToolboxItemContainer
        CreateItemContainer(self: ToolboxService, dataObject: IDataObject) -> ToolboxItemContainer
        """
        ...

    def FilterChanged(self, *args): #cannot find CLR method
        """ FilterChanged(self: ToolboxService) """
        ...

    def GetItemContainers(self, *args): #cannot find CLR method
        """
        GetItemContainers(self: ToolboxService) -> IList
        GetItemContainers(self: ToolboxService, categoryName: str) -> IList
        """
        ...

    @staticmethod
    def GetToolboxItem(toolType:Type, nonPublic:bool = ...) -> ToolboxItem:
        """
        GetToolboxItem(toolType: Type) -> ToolboxItem
        GetToolboxItem(toolType: Type, nonPublic: bool) -> ToolboxItem
        """
        ...

    def IsItemContainer(self, *args): #cannot find CLR method
        """ IsItemContainer(self: ToolboxService, dataObject: IDataObject, host: IDesignerHost) -> bool """
        ...

    def IsItemContainerSupported(self, *args): #cannot find CLR method
        """ IsItemContainerSupported(self: ToolboxService, container: ToolboxItemContainer, host: IDesignerHost) -> bool """
        ...

    def SelectedItemContainerUsed(self, *args): #cannot find CLR method
        """ SelectedItemContainerUsed(self: ToolboxService) """
        ...

    @staticmethod
    def UnloadToolboxItems(): # -> 
        """ UnloadToolboxItems() """
        ...


class UITypeEditorEditStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UITypeEditorEditStyle, values: DropDown (3), Modal (2), None (1) """
    DropDown: UITypeEditorEditStyle = ...
    Modal: UITypeEditorEditStyle = ...
    value__ = ...


