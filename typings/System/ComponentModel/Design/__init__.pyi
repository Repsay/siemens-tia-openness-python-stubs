# encoding: utf-8
# module System.ComponentModel.Design calls itself Design
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, Guid, 
    IAsyncResult, IDisposable, IServiceProvider, MulticastDelegate, Type)

from System.Collections import (ArrayList, CollectionBase, ICollection, 
    IDictionary, IEnumerator)

from System.ComponentModel import (EventDescriptor, EventDescriptorCollection, 
    IComponent, IContainer, IExtenderProvider, INestedContainer, 
    InheritanceAttribute, LicenseContext, MemberDescriptor, 
    PropertyDescriptor, PropertyDescriptorCollection, TypeDescriptionProvider)

from System.ComponentModel.Design.Serialization import DesignerLoader

from System.Diagnostics import TraceListenerCollection

from System.Drawing.Design import UITypeEditor

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Reflection import Assembly, AssemblyName

from System.Resources import IResourceReader, IResourceWriter

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Versioning import FrameworkName

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    DesignSurface, DesignerActionListCollection, 
    DesignerActionListsChangedType, DesignerActionUIStateChangeType, 
    DesignerOptionCollection, DisplayMode, MenuCommandsChangedType, 
    TableLayoutPanel, field#)
"""

# no functions
# classes

class ActiveDesignerEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActiveDesignerEventArgs(oldDesigner: IDesignerHost, newDesigner: IDesignerHost) """
    @property
    def NewDesigner(self) -> IDesignerHost:
        """ Get: NewDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost """
        ...

    @property
    def OldDesigner(self) -> IDesignerHost:
        """ Get: OldDesigner(self: ActiveDesignerEventArgs) -> IDesignerHost """
        ...


    def __new__(cls, oldDesigner:IDesignerHost, newDesigner:IDesignerHost) -> Self:
        """ __new__(cls: type, oldDesigner: IDesignerHost, newDesigner: IDesignerHost) """
        ...


class ActiveDesignerEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ActiveDesignerEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ActiveDesignerEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ActiveDesignerEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ActiveDesignerEventArgs): # -> 
        """ Invoke(self: ActiveDesignerEventHandler, sender: object, e: ActiveDesignerEventArgs) """
        ...


class ActiveDesignSurfaceChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActiveDesignSurfaceChangedEventArgs(oldSurface: DesignSurface, newSurface: DesignSurface) """
    @property
    def NewSurface(self): # -> DesignSurface
        """ Get: NewSurface(self: ActiveDesignSurfaceChangedEventArgs) -> DesignSurface """
        ...

    @property
    def OldSurface(self): # -> DesignSurface
        """ Get: OldSurface(self: ActiveDesignSurfaceChangedEventArgs) -> DesignSurface """
        ...


    def __new__(cls, oldSurface, newSurface) -> Self: # Not found arg types: {'newSurface': 'DesignSurface', 'oldSurface': 'DesignSurface'}
        """ __new__(cls: type, oldSurface: DesignSurface, newSurface: DesignSurface) """
        ...


class ActiveDesignSurfaceChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ActiveDesignSurfaceChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ActiveDesignSurfaceChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ActiveDesignSurfaceChangedEventHandler, sender: object, e: ActiveDesignSurfaceChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ActiveDesignSurfaceChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ActiveDesignSurfaceChangedEventArgs): # -> 
        """ Invoke(self: ActiveDesignSurfaceChangedEventHandler, sender: object, e: ActiveDesignSurfaceChangedEventArgs) """
        ...


class CollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ CollectionEditor(type: Type) """
    @property
    def CollectionItemType(self):
        ...

    @property
    def CollectionType(self):
        ...

    @property
    def Context(self):
        ...

    @property
    def HelpTopic(self):
        ...

    @property
    def NewItemTypes(self):
        ...


    def CancelChanges(self, *args): #cannot find CLR method
        """ CancelChanges(self: CollectionEditor) """
        ...

    def CanRemoveInstance(self, *args): #cannot find CLR method
        """ CanRemoveInstance(self: CollectionEditor, value: object) -> bool """
        ...

    def CanSelectMultipleInstances(self, *args): #cannot find CLR method
        """ CanSelectMultipleInstances(self: CollectionEditor) -> bool """
        ...

    def CollectionForm(self, *args): #cannot find CLR method
        """ CollectionForm(editor: CollectionEditor) """
        ...

    def CreateCollectionForm(self, *args): #cannot find CLR method
        """ CreateCollectionForm(self: CollectionEditor) -> CollectionForm """
        ...

    def CreateCollectionItemType(self, *args): #cannot find CLR method
        """ CreateCollectionItemType(self: CollectionEditor) -> Type """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: CollectionEditor, itemType: Type) -> object """
        ...

    def CreateNewItemTypes(self, *args): #cannot find CLR method
        """ CreateNewItemTypes(self: CollectionEditor) -> Array[Type] """
        ...

    def DestroyInstance(self, *args): #cannot find CLR method
        """ DestroyInstance(self: CollectionEditor, instance: object) """
        ...

    def GetDisplayText(self, *args): #cannot find CLR method
        """ GetDisplayText(self: CollectionEditor, value: object) -> str """
        ...

    def GetItems(self, *args): #cannot find CLR method
        """ GetItems(self: CollectionEditor, editValue: object) -> Array[object] """
        ...

    def GetObjectsFromInstance(self, *args): #cannot find CLR method
        """ GetObjectsFromInstance(self: CollectionEditor, instance: object) -> IList """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: CollectionEditor, serviceType: Type) -> object """
        ...

    def SetItems(self, *args): #cannot find CLR method
        """ SetItems(self: CollectionEditor, editValue: object, value: Array[object]) -> object """
        ...

    def ShowHelp(self, *args): #cannot find CLR method
        """ ShowHelp(self: CollectionEditor) """
        ...

    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...



class ArrayEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ ArrayEditor(type: Type) """
    pass

class BinaryEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ BinaryEditor() """
    pass

class ByteViewer(TableLayoutPanel): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IExtenderProvider'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ByteViewer() """
    def GetBytes(self) -> Array:
        """ GetBytes(self: ByteViewer) -> Array[Byte] """
        ...

    def GetDisplayMode(self): # -> DisplayMode
        """ GetDisplayMode(self: ByteViewer) -> DisplayMode """
        ...

    def SaveToFile(self, path:str): # -> 
        """ SaveToFile(self: ByteViewer, path: str) """
        ...

    def ScrollChanged(self, *args): #cannot find CLR method
        """ ScrollChanged(self: ByteViewer, source: object, e: EventArgs) """
        ...

    def SetBytes(self, bytes:Array): # -> 
        """ SetBytes(self: ByteViewer, bytes: Array[Byte]) """
        ...

    def SetDisplayMode(self, mode): # ->  # Not found arg types: {'mode': 'DisplayMode'}
        """ SetDisplayMode(self: ByteViewer, mode: DisplayMode) """
        ...

    def SetFile(self, path:str): # -> 
        """ SetFile(self: ByteViewer, path: str) """
        ...

    def SetStartLine(self, line:int): # -> 
        """ SetStartLine(self: ByteViewer, line: int) """
        ...


class CheckoutException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CheckoutException()
    CheckoutException(message: str)
    CheckoutException(message: str, errorCode: int)
    CheckoutException(message: str, innerException: Exception)
    """
    Canceled: CheckoutException = ...
    SerializeObjectState = ...


class CommandID: # skipped bases: <type 'object'>, <type 'object'>
    """ CommandID(menuGroup: Guid, commandID: int) """
    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: CommandID) -> Guid """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: CommandID) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CommandID, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CommandID) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CommandID) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ComponentActionsType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ComponentActionsType, values: All (0), Component (1), Service (2) """
    All: ComponentActionsType = ...
    Component: ComponentActionsType = ...
    Service: ComponentActionsType = ...
    value__ = ...


class ComponentChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ComponentChangedEventArgs(component: object, member: MemberDescriptor, oldValue: object, newValue: object) """
    @property
    def Component(self) -> object:
        """ Get: Component(self: ComponentChangedEventArgs) -> object """
        ...

    @property
    def Member(self) -> MemberDescriptor:
        """ Get: Member(self: ComponentChangedEventArgs) -> MemberDescriptor """
        ...

    @property
    def NewValue(self) -> object:
        """ Get: NewValue(self: ComponentChangedEventArgs) -> object """
        ...

    @property
    def OldValue(self) -> object:
        """ Get: OldValue(self: ComponentChangedEventArgs) -> object """
        ...


    def __new__(cls, component:object, member:MemberDescriptor, oldValue:object, newValue:object) -> Self:
        """ __new__(cls: type, component: object, member: MemberDescriptor, oldValue: object, newValue: object) """
        ...


class ComponentChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ComponentChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ComponentChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ComponentChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ComponentChangedEventArgs): # -> 
        """ Invoke(self: ComponentChangedEventHandler, sender: object, e: ComponentChangedEventArgs) """
        ...


class ComponentChangingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ComponentChangingEventArgs(component: object, member: MemberDescriptor) """
    @property
    def Component(self) -> object:
        """ Get: Component(self: ComponentChangingEventArgs) -> object """
        ...

    @property
    def Member(self) -> MemberDescriptor:
        """ Get: Member(self: ComponentChangingEventArgs) -> MemberDescriptor """
        ...


    def __new__(cls, component:object, member:MemberDescriptor) -> Self:
        """ __new__(cls: type, component: object, member: MemberDescriptor) """
        ...


class ComponentChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ComponentChangingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ComponentChangingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ComponentChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ComponentChangingEventArgs): # -> 
        """ Invoke(self: ComponentChangingEventHandler, sender: object, e: ComponentChangingEventArgs) """
        ...


class IComponentInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def InitializeExistingComponent(self, defaultValues:IDictionary): # -> 
        """ InitializeExistingComponent(self: IComponentInitializer, defaultValues: IDictionary) """
        ...

    def InitializeNewComponent(self, defaultValues:IDictionary): # -> 
        """ InitializeNewComponent(self: IComponentInitializer, defaultValues: IDictionary) """
        ...


class IDesigner(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Component(self) -> IComponent:
        """ Get: Component(self: IDesigner) -> IComponent """
        ...

    @property
    def Verbs(self) -> DesignerVerbCollection:
        """ Get: Verbs(self: IDesigner) -> DesignerVerbCollection """
        ...


    def DoDefaultAction(self): # -> 
        """ DoDefaultAction(self: IDesigner) """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: IDesigner, component: IComponent) """
        ...


class IDesignerFilter: # skipped bases: <type 'object'>
    """ no doc """
    def PostFilterAttributes(self, attributes:IDictionary): # -> 
        """ PostFilterAttributes(self: IDesignerFilter, attributes: IDictionary) """
        ...

    def PostFilterEvents(self, events:IDictionary): # -> 
        """ PostFilterEvents(self: IDesignerFilter, events: IDictionary) """
        ...

    def PostFilterProperties(self, properties:IDictionary): # -> 
        """ PostFilterProperties(self: IDesignerFilter, properties: IDictionary) """
        ...

    def PreFilterAttributes(self, attributes:IDictionary): # -> 
        """ PreFilterAttributes(self: IDesignerFilter, attributes: IDictionary) """
        ...

    def PreFilterEvents(self, events:IDictionary): # -> 
        """ PreFilterEvents(self: IDesignerFilter, events: IDictionary) """
        ...

    def PreFilterProperties(self, properties:IDictionary): # -> 
        """ PreFilterProperties(self: IDesignerFilter, properties: IDictionary) """
        ...


class ITreeDesigner(IDesigner): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> ICollection:
        """ Get: Children(self: ITreeDesigner) -> ICollection """
        ...

    @property
    def Parent(self) -> IDesigner:
        """ Get: Parent(self: ITreeDesigner) -> IDesigner """
        ...



class ComponentDesigner(ITreeDesigner, IComponentInitializer, IDesignerFilter): # skipped bases: <type 'IDisposable'>, <type 'IDesigner'>, <type 'object'>
    """ ComponentDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: ComponentDesigner) -> DesignerActionListCollection """
        ...

    @property
    def AssociatedComponents(self) -> ICollection:
        """ Get: AssociatedComponents(self: ComponentDesigner) -> ICollection """
        ...

    @property
    def Component(self) -> IComponent:
        """ Get: Component(self: ComponentDesigner) -> IComponent """
        ...

    @property
    def InheritanceAttribute(self):
        ...

    @property
    def Inherited(self):
        ...

    @property
    def ParentComponent(self):
        ...

    @property
    def ShadowProperties(self):
        ...

    @property
    def Verbs(self) -> DesignerVerbCollection:
        """ Get: Verbs(self: ComponentDesigner) -> DesignerVerbCollection """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: ComponentDesigner) """
        ...

    def DoDefaultAction(self): # -> 
        """ DoDefaultAction(self: ComponentDesigner) """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: ComponentDesigner, serviceType: Type) -> object """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: ComponentDesigner, component: IComponent) """
        ...

    def InitializeNonDefault(self): # -> 
        """ InitializeNonDefault(self: ComponentDesigner) """
        ...

    def InvokeGetInheritanceAttribute(self, *args): #cannot find CLR method
        """ InvokeGetInheritanceAttribute(self: ComponentDesigner, toInvoke: ComponentDesigner) -> InheritanceAttribute """
        ...

    def OnSetComponentDefaults(self): # -> 
        """ OnSetComponentDefaults(self: ComponentDesigner) """
        ...

    def RaiseComponentChanged(self, *args): #cannot find CLR method
        """ RaiseComponentChanged(self: ComponentDesigner, member: MemberDescriptor, oldValue: object, newValue: object) """
        ...

    def RaiseComponentChanging(self, *args): #cannot find CLR method
        """ RaiseComponentChanging(self: ComponentDesigner, member: MemberDescriptor) """
        ...

    def ShadowPropertyCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class ComponentEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ComponentEventArgs(component: IComponent) """
    @property
    def Component(self) -> IComponent:
        """ Get: Component(self: ComponentEventArgs) -> IComponent """
        ...


    def __new__(cls, component:IComponent) -> Self:
        """ __new__(cls: type, component: IComponent) """
        ...


class ComponentEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ComponentEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ComponentEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ComponentEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ComponentEventArgs): # -> 
        """ Invoke(self: ComponentEventHandler, sender: object, e: ComponentEventArgs) """
        ...


class ComponentRenameEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ComponentRenameEventArgs(component: object, oldName: str, newName: str) """
    @property
    def Component(self) -> object:
        """ Get: Component(self: ComponentRenameEventArgs) -> object """
        ...

    @property
    def NewName(self) -> str:
        """ Get: NewName(self: ComponentRenameEventArgs) -> str """
        ...

    @property
    def OldName(self) -> str:
        """ Get: OldName(self: ComponentRenameEventArgs) -> str """
        ...


    def __new__(cls, component:object, oldName:str, newName:str) -> Self:
        """ __new__(cls: type, component: object, oldName: str, newName: str) """
        ...


class ComponentRenameEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ComponentRenameEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ComponentRenameEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ComponentRenameEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ComponentRenameEventArgs): # -> 
        """ Invoke(self: ComponentRenameEventHandler, sender: object, e: ComponentRenameEventArgs) """
        ...


class DateTimeEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DateTimeEditor() """
    pass

class DesignerActionItem: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerActionItem(displayName: str, category: str, description: str) """
    @property
    def AllowAssociate(self) -> bool:
        """
        Get: AllowAssociate(self: DesignerActionItem) -> bool
        Set: AllowAssociate(self: DesignerActionItem) = value
        """
        ...

    @property
    def Category(self) -> str:
        """ Get: Category(self: DesignerActionItem) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: DesignerActionItem) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: DesignerActionItem) -> str """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: DesignerActionItem) -> IDictionary """
        ...

    @property
    def ShowInSourceView(self) -> bool:
        """
        Get: ShowInSourceView(self: DesignerActionItem) -> bool
        Set: ShowInSourceView(self: DesignerActionItem) = value
        """
        ...



class DesignerActionTextItem(DesignerActionItem): # skipped bases: <type 'object'>
    """ DesignerActionTextItem(displayName: str, category: str) """
    pass

class DesignerActionHeaderItem(DesignerActionTextItem): # skipped bases: <type 'object'>
    """
    DesignerActionHeaderItem(displayName: str)
    DesignerActionHeaderItem(displayName: str, category: str)
    """
    pass

class DesignerActionItemCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DesignerActionItemCollection() """
    def Add(self, value:DesignerActionItem) -> int:
        """ Add(self: DesignerActionItemCollection, value: DesignerActionItem) -> int """
        ...

    def Contains(self, value:DesignerActionItem) -> bool:
        """ Contains(self: DesignerActionItemCollection, value: DesignerActionItem) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DesignerActionItemCollection, array: Array[DesignerActionItem], index: int) """
        ...

    def IndexOf(self, value:DesignerActionItem) -> int:
        """ IndexOf(self: DesignerActionItemCollection, value: DesignerActionItem) -> int """
        ...

    def Insert(self, index:int, value:DesignerActionItem): # -> 
        """ Insert(self: DesignerActionItemCollection, index: int, value: DesignerActionItem) """
        ...

    def Remove(self, value:DesignerActionItem): # -> 
        """ Remove(self: DesignerActionItemCollection, value: DesignerActionItem) """
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


class DesignerActionList: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerActionList(component: IComponent) """
    @property
    def AutoShow(self) -> bool:
        """
        Get: AutoShow(self: DesignerActionList) -> bool
        Set: AutoShow(self: DesignerActionList) = value
        """
        ...

    @property
    def Component(self) -> IComponent:
        """ Get: Component(self: DesignerActionList) -> IComponent """
        ...


    def GetService(self, serviceType:Type) -> object:
        """ GetService(self: DesignerActionList, serviceType: Type) -> object """
        ...

    def GetSortedActionItems(self) -> DesignerActionItemCollection:
        """ GetSortedActionItems(self: DesignerActionList) -> DesignerActionItemCollection """
        ...


class DesignerActionListCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    DesignerActionListCollection()
    DesignerActionListCollection(value: Array[DesignerActionList])
    """
    def Add(self, value:DesignerActionList) -> int:
        """ Add(self: DesignerActionListCollection, value: DesignerActionList) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: DesignerActionListCollection, value: Array[DesignerActionList])AddRange(self: DesignerActionListCollection, value: DesignerActionListCollection) """
        ...

    def Contains(self, value:DesignerActionList) -> bool:
        """ Contains(self: DesignerActionListCollection, value: DesignerActionList) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DesignerActionListCollection, array: Array[DesignerActionList], index: int) """
        ...

    def IndexOf(self, value:DesignerActionList) -> int:
        """ IndexOf(self: DesignerActionListCollection, value: DesignerActionList) -> int """
        ...

    def Insert(self, index:int, value:DesignerActionList): # -> 
        """ Insert(self: DesignerActionListCollection, index: int, value: DesignerActionList) """
        ...

    def Remove(self, value:DesignerActionList): # -> 
        """ Remove(self: DesignerActionListCollection, value: DesignerActionList) """
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


class DesignerActionListsChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignerActionListsChangedEventArgs(relatedObject: object, changeType: DesignerActionListsChangedType, actionLists: DesignerActionListCollection) """
    @property
    def ActionLists(self) -> DesignerActionListCollection:
        """ Get: ActionLists(self: DesignerActionListsChangedEventArgs) -> DesignerActionListCollection """
        ...

    @property
    def ChangeType(self): # -> DesignerActionListsChangedType
        """ Get: ChangeType(self: DesignerActionListsChangedEventArgs) -> DesignerActionListsChangedType """
        ...

    @property
    def RelatedObject(self) -> object:
        """ Get: RelatedObject(self: DesignerActionListsChangedEventArgs) -> object """
        ...


    def __new__(cls, relatedObject:object, changeType, actionLists:DesignerActionListCollection) -> Self: # Not found arg types: {'changeType': 'DesignerActionListsChangedType'}
        """ __new__(cls: type, relatedObject: object, changeType: DesignerActionListsChangedType, actionLists: DesignerActionListCollection) """
        ...


class DesignerActionListsChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DesignerActionListsChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DesignerActionListsChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DesignerActionListsChangedEventHandler, sender: object, e: DesignerActionListsChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DesignerActionListsChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DesignerActionListsChangedEventArgs): # -> 
        """ Invoke(self: DesignerActionListsChangedEventHandler, sender: object, e: DesignerActionListsChangedEventArgs) """
        ...


class DesignerActionListsChangedType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerActionListsChangedType, values: ActionListsAdded (0), ActionListsRemoved (1) """
    ActionListsAdded: DesignerActionListsChangedType = ...
    ActionListsRemoved: DesignerActionListsChangedType = ...
    value__ = ...


class DesignerActionMethodItem(DesignerActionItem): # skipped bases: <type 'object'>
    """
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str, category: str, description: str, includeAsDesignerVerb: bool)
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str)
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str, includeAsDesignerVerb: bool)
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str, category: str)
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str, category: str, includeAsDesignerVerb: bool)
    DesignerActionMethodItem(actionList: DesignerActionList, memberName: str, displayName: str, category: str, description: str)
    """
    @property
    def IncludeAsDesignerVerb(self) -> bool:
        """ Get: IncludeAsDesignerVerb(self: DesignerActionMethodItem) -> bool """
        ...

    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: DesignerActionMethodItem) -> str """
        ...

    @property
    def RelatedComponent(self) -> IComponent:
        """
        Get: RelatedComponent(self: DesignerActionMethodItem) -> IComponent
        Set: RelatedComponent(self: DesignerActionMethodItem) = value
        """
        ...


    def Invoke(self): # -> 
        """ Invoke(self: DesignerActionMethodItem) """
        ...


class DesignerActionPropertyItem(DesignerActionItem): # skipped bases: <type 'object'>
    """
    DesignerActionPropertyItem(memberName: str, displayName: str, category: str, description: str)
    DesignerActionPropertyItem(memberName: str, displayName: str)
    DesignerActionPropertyItem(memberName: str, displayName: str, category: str)
    """
    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: DesignerActionPropertyItem) -> str """
        ...

    @property
    def RelatedComponent(self) -> IComponent:
        """
        Get: RelatedComponent(self: DesignerActionPropertyItem) -> IComponent
        Set: RelatedComponent(self: DesignerActionPropertyItem) = value
        """
        ...



class DesignerActionService(IDisposable): # skipped bases: <type 'object'>
    """ DesignerActionService(serviceProvider: IServiceProvider) """
    def Add(self, comp:IComponent, *__args:DesignerActionListCollection): # -> 
        """ Add(self: DesignerActionService, comp: IComponent, designerActionListCollection: DesignerActionListCollection)Add(self: DesignerActionService, comp: IComponent, actionList: DesignerActionList) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DesignerActionService) """
        ...

    def Contains(self, comp:IComponent) -> bool:
        """ Contains(self: DesignerActionService, comp: IComponent) -> bool """
        ...

    def GetComponentActions(self, component:IComponent, type:ComponentActionsType = ...) -> DesignerActionListCollection:
        """
        GetComponentActions(self: DesignerActionService, component: IComponent) -> DesignerActionListCollection
        GetComponentActions(self: DesignerActionService, component: IComponent, type: ComponentActionsType) -> DesignerActionListCollection
        """
        ...

    def GetComponentDesignerActions(self, *args): #cannot find CLR method
        """ GetComponentDesignerActions(self: DesignerActionService, component: IComponent, actionLists: DesignerActionListCollection) """
        ...

    def GetComponentServiceActions(self, *args): #cannot find CLR method
        """ GetComponentServiceActions(self: DesignerActionService, component: IComponent, actionLists: DesignerActionListCollection) """
        ...

    def Remove(self, *__args:IComponent): # -> 
        """ Remove(self: DesignerActionService, comp: IComponent)Remove(self: DesignerActionService, actionList: DesignerActionList)Remove(self: DesignerActionService, comp: IComponent, actionList: DesignerActionList) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    DesignerActionListsChanged = ...


class DesignerActionUIService(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def HideUI(self, component:IComponent): # -> 
        """ HideUI(self: DesignerActionUIService, component: IComponent) """
        ...

    def Refresh(self, component:IComponent): # -> 
        """ Refresh(self: DesignerActionUIService, component: IComponent) """
        ...

    def ShouldAutoShow(self, component:IComponent) -> bool:
        """ ShouldAutoShow(self: DesignerActionUIService, component: IComponent) -> bool """
        ...

    def ShowUI(self, component:IComponent): # -> 
        """ ShowUI(self: DesignerActionUIService, component: IComponent) """
        ...

    DesignerActionUIStateChange = ...


class DesignerActionUIStateChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignerActionUIStateChangeEventArgs(relatedObject: object, changeType: DesignerActionUIStateChangeType) """
    @property
    def ChangeType(self): # -> DesignerActionUIStateChangeType
        """ Get: ChangeType(self: DesignerActionUIStateChangeEventArgs) -> DesignerActionUIStateChangeType """
        ...

    @property
    def RelatedObject(self) -> object:
        """ Get: RelatedObject(self: DesignerActionUIStateChangeEventArgs) -> object """
        ...


    def __new__(cls, relatedObject:object, changeType) -> Self: # Not found arg types: {'changeType': 'DesignerActionUIStateChangeType'}
        """ __new__(cls: type, relatedObject: object, changeType: DesignerActionUIStateChangeType) """
        ...


class DesignerActionUIStateChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DesignerActionUIStateChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DesignerActionUIStateChangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DesignerActionUIStateChangeEventHandler, sender: object, e: DesignerActionUIStateChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DesignerActionUIStateChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DesignerActionUIStateChangeEventArgs): # -> 
        """ Invoke(self: DesignerActionUIStateChangeEventHandler, sender: object, e: DesignerActionUIStateChangeEventArgs) """
        ...


class DesignerActionUIStateChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerActionUIStateChangeType, values: Hide (1), Refresh (2), Show (0) """
    Hide: DesignerActionUIStateChangeType = ...
    Refresh: DesignerActionUIStateChangeType = ...
    Show: DesignerActionUIStateChangeType = ...
    value__ = ...


class DesignerCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    DesignerCollection(designers: Array[IDesignerHost])
    DesignerCollection(designers: IList)
    """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DesignerCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DesignerCommandSet: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerCommandSet() """
    @property
    def ActionLists(self) -> DesignerActionListCollection:
        """ Get: ActionLists(self: DesignerCommandSet) -> DesignerActionListCollection """
        ...

    @property
    def Verbs(self) -> DesignerVerbCollection:
        """ Get: Verbs(self: DesignerCommandSet) -> DesignerVerbCollection """
        ...


    def GetCommands(self, name:str) -> ICollection:
        """ GetCommands(self: DesignerCommandSet, name: str) -> ICollection """
        ...


class DesignerEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignerEventArgs(host: IDesignerHost) """
    @property
    def Designer(self) -> IDesignerHost:
        """ Get: Designer(self: DesignerEventArgs) -> IDesignerHost """
        ...


    def __new__(cls, host:IDesignerHost) -> Self:
        """ __new__(cls: type, host: IDesignerHost) """
        ...


class DesignerEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DesignerEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DesignerEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DesignerEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DesignerEventArgs): # -> 
        """ Invoke(self: DesignerEventHandler, sender: object, e: DesignerEventArgs) """
        ...


class IDesignerOptionService: # skipped bases: <type 'object'>
    """ no doc """
    def GetOptionValue(self, pageName:str, valueName:str) -> object:
        """ GetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str) -> object """
        ...

    def SetOptionValue(self, pageName:str, valueName:str, value:object): # -> 
        """ SetOptionValue(self: IDesignerOptionService, pageName: str, valueName: str, value: object) """
        ...


class DesignerOptionService(IDesignerOptionService): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Options(self): # -> DesignerOptionCollection
        """ Get: Options(self: DesignerOptionService) -> DesignerOptionCollection """
        ...


    def CreateOptionCollection(self, *args): #cannot find CLR method
        """ CreateOptionCollection(self: DesignerOptionService, parent: DesignerOptionCollection, name: str, value: object) -> DesignerOptionCollection """
        ...

    def DesignerOptionCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def PopulateOptionCollection(self, *args): #cannot find CLR method
        """ PopulateOptionCollection(self: DesignerOptionService, options: DesignerOptionCollection) """
        ...

    def ShowDialog(self, *args): #cannot find CLR method
        """ ShowDialog(self: DesignerOptionService, options: DesignerOptionCollection, optionObject: object) -> bool """
        ...



class DesignerTransaction(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Canceled(self) -> bool:
        """ Get: Canceled(self: DesignerTransaction) -> bool """
        ...

    @property
    def Committed(self) -> bool:
        """ Get: Committed(self: DesignerTransaction) -> bool """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: DesignerTransaction) -> str """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: DesignerTransaction) """
        ...

    def Commit(self): # -> 
        """ Commit(self: DesignerTransaction) """
        ...

    def OnCancel(self, *args): #cannot find CLR method
        """ OnCancel(self: DesignerTransaction) """
        ...

    def OnCommit(self, *args): #cannot find CLR method
        """ OnCommit(self: DesignerTransaction) """
        ...


class DesignerTransactionCloseEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    DesignerTransactionCloseEventArgs(commit: bool)
    DesignerTransactionCloseEventArgs(commit: bool, lastTransaction: bool)
    """
    @property
    def LastTransaction(self) -> bool:
        """ Get: LastTransaction(self: DesignerTransactionCloseEventArgs) -> bool """
        ...

    @property
    def TransactionCommitted(self) -> bool:
        """ Get: TransactionCommitted(self: DesignerTransactionCloseEventArgs) -> bool """
        ...


    def __new__(cls, commit:bool, lastTransaction:bool = ...) -> Self:
        """
        __new__(cls: type, commit: bool)
        __new__(cls: type, commit: bool, lastTransaction: bool)
        """
        ...


class DesignerTransactionCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DesignerTransactionCloseEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DesignerTransactionCloseEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DesignerTransactionCloseEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DesignerTransactionCloseEventArgs): # -> 
        """ Invoke(self: DesignerTransactionCloseEventHandler, sender: object, e: DesignerTransactionCloseEventArgs) """
        ...


class MenuCommand: # skipped bases: <type 'object'>, <type 'object'>
    """ MenuCommand(handler: EventHandler, command: CommandID) """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: MenuCommand) -> bool
        Set: Checked(self: MenuCommand) = value
        """
        ...

    @property
    def CommandID(self) -> CommandID:
        """ Get: CommandID(self: MenuCommand) -> CommandID """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: MenuCommand) -> bool
        Set: Enabled(self: MenuCommand) = value
        """
        ...

    @property
    def OleStatus(self) -> int:
        """ Get: OleStatus(self: MenuCommand) -> int """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: MenuCommand) -> IDictionary """
        ...

    @property
    def Supported(self) -> bool:
        """
        Get: Supported(self: MenuCommand) -> bool
        Set: Supported(self: MenuCommand) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: MenuCommand) -> bool
        Set: Visible(self: MenuCommand) = value
        """
        ...


    def Invoke(self, arg:object = ...): # -> 
        """ Invoke(self: MenuCommand)Invoke(self: MenuCommand, arg: object) """
        ...

    def OnCommandChanged(self, *args): #cannot find CLR method
        """ OnCommandChanged(self: MenuCommand, e: EventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: MenuCommand) -> str """
        ...

    CommandChanged = ...


class DesignerVerb(MenuCommand): # skipped bases: <type 'object'>
    """
    DesignerVerb(text: str, handler: EventHandler)
    DesignerVerb(text: str, handler: EventHandler, startCommandID: CommandID)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: DesignerVerb) -> str
        Set: Description(self: DesignerVerb) = value
        """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: DesignerVerb) -> str """
        ...



class DesignerVerbCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    DesignerVerbCollection()
    DesignerVerbCollection(value: Array[DesignerVerb])
    """
    def Add(self, value:DesignerVerb) -> int:
        """ Add(self: DesignerVerbCollection, value: DesignerVerb) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: DesignerVerbCollection, value: Array[DesignerVerb])AddRange(self: DesignerVerbCollection, value: DesignerVerbCollection) """
        ...

    def Contains(self, value:DesignerVerb) -> bool:
        """ Contains(self: DesignerVerbCollection, value: DesignerVerb) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DesignerVerbCollection, array: Array[DesignerVerb], index: int) """
        ...

    def IndexOf(self, value:DesignerVerb) -> int:
        """ IndexOf(self: DesignerVerbCollection, value: DesignerVerb) -> int """
        ...

    def Insert(self, index:int, value:DesignerVerb): # -> 
        """ Insert(self: DesignerVerbCollection, index: int, value: DesignerVerb) """
        ...

    def Remove(self, value:DesignerVerb): # -> 
        """ Remove(self: DesignerVerbCollection, value: DesignerVerb) """
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


class DesignSurface(IDisposable, IServiceProvider): # skipped bases: <type 'object'>
    """
    DesignSurface()
    DesignSurface(parentProvider: IServiceProvider)
    DesignSurface(rootComponentType: Type)
    DesignSurface(parentProvider: IServiceProvider, rootComponentType: Type)
    """
    @property
    def ComponentContainer(self) -> IContainer:
        """ Get: ComponentContainer(self: DesignSurface) -> IContainer """
        ...

    @property
    def DtelLoading(self) -> bool:
        """
        Get: DtelLoading(self: DesignSurface) -> bool
        Set: DtelLoading(self: DesignSurface) = value
        """
        ...

    @property
    def IsLoaded(self) -> bool:
        """ Get: IsLoaded(self: DesignSurface) -> bool """
        ...

    @property
    def LoadErrors(self) -> ICollection:
        """ Get: LoadErrors(self: DesignSurface) -> ICollection """
        ...

    @property
    def ServiceContainer(self):
        ...

    @property
    def View(self) -> object:
        """ Get: View(self: DesignSurface) -> object """
        ...


    def BeginLoad(self, *__args:DesignerLoader): # -> 
        """ BeginLoad(self: DesignSurface, loader: DesignerLoader)BeginLoad(self: DesignSurface, rootComponentType: Type) """
        ...

    def CreateComponent(self, *args): #cannot find CLR method
        """ CreateComponent(self: DesignSurface, componentType: Type) -> IComponent """
        ...

    def CreateDesigner(self, *args): #cannot find CLR method
        """ CreateDesigner(self: DesignSurface, component: IComponent, rootDesigner: bool) -> IDesigner """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: DesignSurface, type: Type) -> object """
        ...

    def CreateNestedContainer(self, owningComponent:IComponent, containerName:str = ...) -> INestedContainer:
        """
        CreateNestedContainer(self: DesignSurface, owningComponent: IComponent) -> INestedContainer
        CreateNestedContainer(self: DesignSurface, owningComponent: IComponent, containerName: str) -> INestedContainer
        """
        ...

    def Flush(self): # -> 
        """ Flush(self: DesignSurface) """
        ...

    def OnLoaded(self, *args): #cannot find CLR method
        """ OnLoaded(self: DesignSurface, e: LoadedEventArgs) """
        ...

    def OnLoading(self, *args): #cannot find CLR method
        """ OnLoading(self: DesignSurface, e: EventArgs) """
        ...

    def OnUnloaded(self, *args): #cannot find CLR method
        """ OnUnloaded(self: DesignSurface, e: EventArgs) """
        ...

    def OnUnloading(self, *args): #cannot find CLR method
        """ OnUnloading(self: DesignSurface, e: EventArgs) """
        ...

    def OnViewActivate(self, *args): #cannot find CLR method
        """ OnViewActivate(self: DesignSurface, e: EventArgs) """
        ...

    Disposed = ...
    Flushed = ...
    Loaded = ...
    Loading = ...
    Unloaded = ...
    Unloading = ...
    ViewActivated = ...


class DesignSurfaceCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DesignSurfaceCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DesignSurfaceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignSurfaceEventArgs(surface: DesignSurface) """
    @property
    def Surface(self) -> DesignSurface:
        """ Get: Surface(self: DesignSurfaceEventArgs) -> DesignSurface """
        ...


    def __new__(cls, surface:DesignSurface) -> Self:
        """ __new__(cls: type, surface: DesignSurface) """
        ...


class DesignSurfaceEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DesignSurfaceEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DesignSurfaceEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DesignSurfaceEventHandler, sender: object, e: DesignSurfaceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DesignSurfaceEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DesignSurfaceEventArgs): # -> 
        """ Invoke(self: DesignSurfaceEventHandler, sender: object, e: DesignSurfaceEventArgs) """
        ...


class DesignSurfaceManager(IServiceProvider, IDisposable): # skipped bases: <type 'object'>
    """
    DesignSurfaceManager()
    DesignSurfaceManager(parentProvider: IServiceProvider)
    """
    @property
    def ActiveDesignSurface(self) -> DesignSurface:
        """
        Get: ActiveDesignSurface(self: DesignSurfaceManager) -> DesignSurface
        Set: ActiveDesignSurface(self: DesignSurfaceManager) = value
        """
        ...

    @property
    def DesignSurfaces(self) -> DesignSurfaceCollection:
        """ Get: DesignSurfaces(self: DesignSurfaceManager) -> DesignSurfaceCollection """
        ...

    @property
    def ServiceContainer(self):
        ...


    def CreateDesignSurface(self, parentProvider:IServiceProvider = ...) -> DesignSurface:
        """
        CreateDesignSurface(self: DesignSurfaceManager) -> DesignSurface
        CreateDesignSurface(self: DesignSurfaceManager, parentProvider: IServiceProvider) -> DesignSurface
        """
        ...

    def CreateDesignSurfaceCore(self, *args): #cannot find CLR method
        """ CreateDesignSurfaceCore(self: DesignSurfaceManager, parentProvider: IServiceProvider) -> DesignSurface """
        ...

    ActiveDesignSurfaceChanged = ...
    DesignSurfaceCreated = ...
    DesignSurfaceDisposed = ...
    SelectionChanged = ...


class DesigntimeLicenseContext(LicenseContext): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ DesigntimeLicenseContext() """
    pass

class DesigntimeLicenseContextSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Serialize(o:Stream, cryptoKey:str, context:DesigntimeLicenseContext): # -> 
        """ Serialize(o: Stream, cryptoKey: str, context: DesigntimeLicenseContext) """
        ...


class DisplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DisplayMode, values: Ansi (2), Auto (4), Hexdump (1), Unicode (3) """
    Ansi: DisplayMode = ...
    Auto: DisplayMode = ...
    Hexdump: DisplayMode = ...
    Unicode: DisplayMode = ...
    value__ = ...


class EventBindingService(IEventBindingService): # skipped bases: <type 'object'>
    """ no doc """
    def FreeMethod(self, *args): #cannot find CLR method
        """ FreeMethod(self: EventBindingService, component: IComponent, e: EventDescriptor, methodName: str) """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: EventBindingService, serviceType: Type) -> object """
        ...

    def UseMethod(self, *args): #cannot find CLR method
        """ UseMethod(self: EventBindingService, component: IComponent, e: EventDescriptor, methodName: str) """
        ...

    def ValidateMethodName(self, *args): #cannot find CLR method
        """ ValidateMethodName(self: EventBindingService, methodName: str) """
        ...


class ExceptionCollection(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ ExceptionCollection(exceptions: ArrayList) """
    @property
    def Exceptions(self) -> ArrayList:
        """ Get: Exceptions(self: ExceptionCollection) -> ArrayList """
        ...


    SerializeObjectState = ...


class HelpContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HelpContextType, values: Ambient (0), Selection (2), ToolWindowSelection (3), Window (1) """
    Ambient: HelpContextType = ...
    Selection: HelpContextType = ...
    ToolWindowSelection: HelpContextType = ...
    value__ = ...
    Window: HelpContextType = ...


class HelpKeywordAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    HelpKeywordAttribute()
    HelpKeywordAttribute(keyword: str)
    HelpKeywordAttribute(t: Type)
    """
    @property
    def HelpKeyword(self) -> str:
        """ Get: HelpKeyword(self: HelpKeywordAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, keyword: str)
        __new__(cls: type, t: Type)
        """
        ...

    Default: HelpKeywordAttribute = ...


class HelpKeywordType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HelpKeywordType, values: F1Keyword (0), FilterKeyword (2), GeneralKeyword (1) """
    F1Keyword: HelpKeywordType = ...
    FilterKeyword: HelpKeywordType = ...
    GeneralKeyword: HelpKeywordType = ...
    value__ = ...


class IComponentChangeService: # skipped bases: <type 'object'>
    """ no doc """
    def OnComponentChanged(self, component:object, member:MemberDescriptor, oldValue:object, newValue:object): # -> 
        """ OnComponentChanged(self: IComponentChangeService, component: object, member: MemberDescriptor, oldValue: object, newValue: object) """
        ...

    def OnComponentChanging(self, component:object, member:MemberDescriptor): # -> 
        """ OnComponentChanging(self: IComponentChangeService, component: object, member: MemberDescriptor) """
        ...

    ComponentAdded = ...
    ComponentAdding = ...
    ComponentChanged = ...
    ComponentChanging = ...
    ComponentRemoved = ...
    ComponentRemoving = ...
    ComponentRename = ...


class IComponentDesignerDebugService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IndentLevel(self) -> int:
        """
        Get: IndentLevel(self: IComponentDesignerDebugService) -> int
        Set: IndentLevel(self: IComponentDesignerDebugService) = value
        """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners(self: IComponentDesignerDebugService) -> TraceListenerCollection """
        ...


    def Assert(self, condition:bool, message:str): # -> 
        """ Assert(self: IComponentDesignerDebugService, condition: bool, message: str) """
        ...

    def Fail(self, message:str): # -> 
        """ Fail(self: IComponentDesignerDebugService, message: str) """
        ...

    def Trace(self, message:str, category:str): # -> 
        """ Trace(self: IComponentDesignerDebugService, message: str, category: str) """
        ...


class IComponentDesignerStateService: # skipped bases: <type 'object'>
    """ no doc """
    def GetState(self, component:IComponent, key:str) -> object:
        """ GetState(self: IComponentDesignerStateService, component: IComponent, key: str) -> object """
        ...

    def SetState(self, component:IComponent, key:str, value:object): # -> 
        """ SetState(self: IComponentDesignerStateService, component: IComponent, key: str, value: object) """
        ...


class IComponentDiscoveryService: # skipped bases: <type 'object'>
    """ no doc """
    def GetComponentTypes(self, designerHost:IDesignerHost, baseType:Type) -> ICollection:
        """ GetComponentTypes(self: IComponentDiscoveryService, designerHost: IDesignerHost, baseType: Type) -> ICollection """
        ...


class IDesignerEventService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveDesigner(self) -> IDesignerHost:
        """ Get: ActiveDesigner(self: IDesignerEventService) -> IDesignerHost """
        ...

    @property
    def Designers(self) -> DesignerCollection:
        """ Get: Designers(self: IDesignerEventService) -> DesignerCollection """
        ...


    ActiveDesignerChanged = ...
    DesignerCreated = ...
    DesignerDisposed = ...
    SelectionChanged = ...


class IServiceContainer(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    def AddService(self, serviceType:Type, *__args:object): # -> 
        """ AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object)AddService(self: IServiceContainer, serviceType: Type, serviceInstance: object, promote: bool)AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback)AddService(self: IServiceContainer, serviceType: Type, callback: ServiceCreatorCallback, promote: bool) """
        ...

    def RemoveService(self, serviceType:Type, promote:bool = ...): # -> 
        """ RemoveService(self: IServiceContainer, serviceType: Type)RemoveService(self: IServiceContainer, serviceType: Type, promote: bool) """
        ...


class IDesignerHost(IServiceContainer): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ no doc """
    @property
    def Container(self) -> IContainer:
        """ Get: Container(self: IDesignerHost) -> IContainer """
        ...

    @property
    def InTransaction(self) -> bool:
        """ Get: InTransaction(self: IDesignerHost) -> bool """
        ...

    @property
    def Loading(self) -> bool:
        """ Get: Loading(self: IDesignerHost) -> bool """
        ...

    @property
    def RootComponent(self) -> IComponent:
        """ Get: RootComponent(self: IDesignerHost) -> IComponent """
        ...

    @property
    def RootComponentClassName(self) -> str:
        """ Get: RootComponentClassName(self: IDesignerHost) -> str """
        ...

    @property
    def TransactionDescription(self) -> str:
        """ Get: TransactionDescription(self: IDesignerHost) -> str """
        ...


    def Activate(self): # -> 
        """ Activate(self: IDesignerHost) """
        ...

    def CreateComponent(self, componentClass:Type, name:str = ...) -> IComponent:
        """
        CreateComponent(self: IDesignerHost, componentClass: Type) -> IComponent
        CreateComponent(self: IDesignerHost, componentClass: Type, name: str) -> IComponent
        """
        ...

    def CreateTransaction(self, description:str = ...) -> DesignerTransaction:
        """
        CreateTransaction(self: IDesignerHost) -> DesignerTransaction
        CreateTransaction(self: IDesignerHost, description: str) -> DesignerTransaction
        """
        ...

    def DestroyComponent(self, component:IComponent): # -> 
        """ DestroyComponent(self: IDesignerHost, component: IComponent) """
        ...

    def GetDesigner(self, component:IComponent) -> IDesigner:
        """ GetDesigner(self: IDesignerHost, component: IComponent) -> IDesigner """
        ...

    def GetType(self, typeName:str) -> Type:
        """ GetType(self: IDesignerHost, typeName: str) -> Type """
        ...

    Activated = ...
    Deactivated = ...
    LoadComplete = ...
    TransactionClosed = ...
    TransactionClosing = ...
    TransactionOpened = ...
    TransactionOpening = ...


class IDesignerHostTransactionState: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsClosingTransaction(self) -> bool:
        """ Get: IsClosingTransaction(self: IDesignerHostTransactionState) -> bool """
        ...



class IDesignTimeAssemblyLoader: # skipped bases: <type 'object'>
    """ no doc """
    def GetTargetAssemblyPath(self, runtimeOrTargetAssemblyName:AssemblyName, suggestedAssemblyPath:str, targetFramework:FrameworkName) -> str:
        """ GetTargetAssemblyPath(self: IDesignTimeAssemblyLoader, runtimeOrTargetAssemblyName: AssemblyName, suggestedAssemblyPath: str, targetFramework: FrameworkName) -> str """
        ...

    def LoadRuntimeAssembly(self, targetAssemblyName:AssemblyName) -> Assembly:
        """ LoadRuntimeAssembly(self: IDesignTimeAssemblyLoader, targetAssemblyName: AssemblyName) -> Assembly """
        ...


class IDictionaryService: # skipped bases: <type 'object'>
    """ no doc """
    def GetKey(self, value:object) -> object:
        """ GetKey(self: IDictionaryService, value: object) -> object """
        ...

    def GetValue(self, key:object) -> object:
        """ GetValue(self: IDictionaryService, key: object) -> object """
        ...

    def SetValue(self, key:object, value:object): # -> 
        """ SetValue(self: IDictionaryService, key: object, value: object) """
        ...


class IEventBindingService: # skipped bases: <type 'object'>
    """ no doc """
    def CreateUniqueMethodName(self, component:IComponent, e:EventDescriptor) -> str:
        """ CreateUniqueMethodName(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> str """
        ...

    def GetCompatibleMethods(self, e:EventDescriptor) -> ICollection:
        """ GetCompatibleMethods(self: IEventBindingService, e: EventDescriptor) -> ICollection """
        ...

    def GetEvent(self, property:PropertyDescriptor) -> EventDescriptor:
        """ GetEvent(self: IEventBindingService, property: PropertyDescriptor) -> EventDescriptor """
        ...

    def GetEventProperties(self, events:EventDescriptorCollection) -> PropertyDescriptorCollection:
        """ GetEventProperties(self: IEventBindingService, events: EventDescriptorCollection) -> PropertyDescriptorCollection """
        ...

    def GetEventProperty(self, e:EventDescriptor) -> PropertyDescriptor:
        """ GetEventProperty(self: IEventBindingService, e: EventDescriptor) -> PropertyDescriptor """
        ...

    def ShowCode(self, *__args:int) -> bool:
        """
        ShowCode(self: IEventBindingService) -> bool
        ShowCode(self: IEventBindingService, lineNumber: int) -> bool
        ShowCode(self: IEventBindingService, component: IComponent, e: EventDescriptor) -> bool
        """
        ...


class IExtenderListService: # skipped bases: <type 'object'>
    """ no doc """
    def GetExtenderProviders(self) -> Array:
        """ GetExtenderProviders(self: IExtenderListService) -> Array[IExtenderProvider] """
        ...


class IExtenderProviderService: # skipped bases: <type 'object'>
    """ no doc """
    def AddExtenderProvider(self, provider:IExtenderProvider): # -> 
        """ AddExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider) """
        ...

    def RemoveExtenderProvider(self, provider:IExtenderProvider): # -> 
        """ RemoveExtenderProvider(self: IExtenderProviderService, provider: IExtenderProvider) """
        ...


class IHelpService: # skipped bases: <type 'object'>
    """ no doc """
    def AddContextAttribute(self, name:str, value:str, keywordType:HelpKeywordType): # -> 
        """ AddContextAttribute(self: IHelpService, name: str, value: str, keywordType: HelpKeywordType) """
        ...

    def ClearContextAttributes(self): # -> 
        """ ClearContextAttributes(self: IHelpService) """
        ...

    def CreateLocalContext(self, contextType:HelpContextType) -> IHelpService:
        """ CreateLocalContext(self: IHelpService, contextType: HelpContextType) -> IHelpService """
        ...

    def RemoveContextAttribute(self, name:str, value:str): # -> 
        """ RemoveContextAttribute(self: IHelpService, name: str, value: str) """
        ...

    def RemoveLocalContext(self, localContext:IHelpService): # -> 
        """ RemoveLocalContext(self: IHelpService, localContext: IHelpService) """
        ...

    def ShowHelpFromKeyword(self, helpKeyword:str): # -> 
        """ ShowHelpFromKeyword(self: IHelpService, helpKeyword: str) """
        ...

    def ShowHelpFromUrl(self, helpUrl:str): # -> 
        """ ShowHelpFromUrl(self: IHelpService, helpUrl: str) """
        ...


class IInheritanceService: # skipped bases: <type 'object'>
    """ no doc """
    def AddInheritedComponents(self, component:IComponent, container:IContainer): # -> 
        """ AddInheritedComponents(self: IInheritanceService, component: IComponent, container: IContainer) """
        ...

    def GetInheritanceAttribute(self, component:IComponent) -> InheritanceAttribute:
        """ GetInheritanceAttribute(self: IInheritanceService, component: IComponent) -> InheritanceAttribute """
        ...


class IMenuCommandService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Verbs(self) -> DesignerVerbCollection:
        """ Get: Verbs(self: IMenuCommandService) -> DesignerVerbCollection """
        ...


    def AddCommand(self, command:MenuCommand): # -> 
        """ AddCommand(self: IMenuCommandService, command: MenuCommand) """
        ...

    def AddVerb(self, verb:DesignerVerb): # -> 
        """ AddVerb(self: IMenuCommandService, verb: DesignerVerb) """
        ...

    def FindCommand(self, commandID:CommandID) -> MenuCommand:
        """ FindCommand(self: IMenuCommandService, commandID: CommandID) -> MenuCommand """
        ...

    def GlobalInvoke(self, commandID:CommandID) -> bool:
        """ GlobalInvoke(self: IMenuCommandService, commandID: CommandID) -> bool """
        ...

    def RemoveCommand(self, command:MenuCommand): # -> 
        """ RemoveCommand(self: IMenuCommandService, command: MenuCommand) """
        ...

    def RemoveVerb(self, verb:DesignerVerb): # -> 
        """ RemoveVerb(self: IMenuCommandService, verb: DesignerVerb) """
        ...

    def ShowContextMenu(self, menuID:CommandID, x:int, y:int): # -> 
        """ ShowContextMenu(self: IMenuCommandService, menuID: CommandID, x: int, y: int) """
        ...


class IMultitargetHelperService: # skipped bases: <type 'object'>
    """ no doc """
    def GetAssemblyQualifiedName(self, type:Type) -> str:
        """ GetAssemblyQualifiedName(self: IMultitargetHelperService, type: Type) -> str """
        ...


class InheritanceService(IDisposable, IInheritanceService): # skipped bases: <type 'object'>
    """ InheritanceService() """
    def IgnoreInheritedMember(self, *args): #cannot find CLR method
        """ IgnoreInheritedMember(self: InheritanceService, member: MemberInfo, component: IComponent) -> bool """
        ...


class IReferenceService: # skipped bases: <type 'object'>
    """ no doc """
    def GetComponent(self, reference:object) -> IComponent:
        """ GetComponent(self: IReferenceService, reference: object) -> IComponent """
        ...

    def GetName(self, reference:object) -> str:
        """ GetName(self: IReferenceService, reference: object) -> str """
        ...

    def GetReference(self, name:str) -> object:
        """ GetReference(self: IReferenceService, name: str) -> object """
        ...

    def GetReferences(self, baseType:Type = ...) -> Array:
        """
        GetReferences(self: IReferenceService) -> Array[object]
        GetReferences(self: IReferenceService, baseType: Type) -> Array[object]
        """
        ...


class IResourceService: # skipped bases: <type 'object'>
    """ no doc """
    def GetResourceReader(self, info:CultureInfo) -> IResourceReader:
        """ GetResourceReader(self: IResourceService, info: CultureInfo) -> IResourceReader """
        ...

    def GetResourceWriter(self, info:CultureInfo) -> IResourceWriter:
        """ GetResourceWriter(self: IResourceService, info: CultureInfo) -> IResourceWriter """
        ...


class IRootDesigner(IDesigner): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def SupportedTechnologies(self) -> Array:
        """ Get: SupportedTechnologies(self: IRootDesigner) -> Array[ViewTechnology] """
        ...


    def GetView(self, technology:ViewTechnology) -> object:
        """ GetView(self: IRootDesigner, technology: ViewTechnology) -> object """
        ...


class ISelectionService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PrimarySelection(self) -> object:
        """ Get: PrimarySelection(self: ISelectionService) -> object """
        ...

    @property
    def SelectionCount(self) -> int:
        """ Get: SelectionCount(self: ISelectionService) -> int """
        ...


    def GetComponentSelected(self, component:object) -> bool:
        """ GetComponentSelected(self: ISelectionService, component: object) -> bool """
        ...

    def GetSelectedComponents(self) -> ICollection:
        """ GetSelectedComponents(self: ISelectionService) -> ICollection """
        ...

    def SetSelectedComponents(self, components:ICollection, selectionType:SelectionTypes = ...): # -> 
        """ SetSelectedComponents(self: ISelectionService, components: ICollection)SetSelectedComponents(self: ISelectionService, components: ICollection, selectionType: SelectionTypes) """
        ...

    SelectionChanged = ...
    SelectionChanging = ...


class ITypeDescriptorFilterService: # skipped bases: <type 'object'>
    """ no doc """
    def FilterAttributes(self, component:IComponent, attributes:IDictionary) -> bool:
        """ FilterAttributes(self: ITypeDescriptorFilterService, component: IComponent, attributes: IDictionary) -> bool """
        ...

    def FilterEvents(self, component:IComponent, events:IDictionary) -> bool:
        """ FilterEvents(self: ITypeDescriptorFilterService, component: IComponent, events: IDictionary) -> bool """
        ...

    def FilterProperties(self, component:IComponent, properties:IDictionary) -> bool:
        """ FilterProperties(self: ITypeDescriptorFilterService, component: IComponent, properties: IDictionary) -> bool """
        ...


class ITypeDiscoveryService: # skipped bases: <type 'object'>
    """ no doc """
    def GetTypes(self, baseType:Type, excludeGlobalTypes:bool) -> ICollection:
        """ GetTypes(self: ITypeDiscoveryService, baseType: Type, excludeGlobalTypes: bool) -> ICollection """
        ...


class ITypeResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    def GetAssembly(self, name:AssemblyName, throwOnError:bool = ...) -> Assembly:
        """
        GetAssembly(self: ITypeResolutionService, name: AssemblyName) -> Assembly
        GetAssembly(self: ITypeResolutionService, name: AssemblyName, throwOnError: bool) -> Assembly
        """
        ...

    def GetPathOfAssembly(self, name:AssemblyName) -> str:
        """ GetPathOfAssembly(self: ITypeResolutionService, name: AssemblyName) -> str """
        ...

    def GetType(self, name:str, throwOnError:bool = ..., ignoreCase:bool = ...) -> Type:
        """
        GetType(self: ITypeResolutionService, name: str) -> Type
        GetType(self: ITypeResolutionService, name: str, throwOnError: bool) -> Type
        GetType(self: ITypeResolutionService, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        ...

    def ReferenceAssembly(self, name:AssemblyName): # -> 
        """ ReferenceAssembly(self: ITypeResolutionService, name: AssemblyName) """
        ...


class LoadedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ LoadedEventArgs(succeeded: bool, errors: ICollection) """
    @property
    def Errors(self) -> ICollection:
        """ Get: Errors(self: LoadedEventArgs) -> ICollection """
        ...

    @property
    def HasSucceeded(self) -> bool:
        """ Get: HasSucceeded(self: LoadedEventArgs) -> bool """
        ...


    def __new__(cls, succeeded:bool, errors:ICollection) -> Self:
        """ __new__(cls: type, succeeded: bool, errors: ICollection) """
        ...


class LoadedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LoadedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:LoadedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: LoadedEventHandler, sender: object, e: LoadedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: LoadedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:LoadedEventArgs): # -> 
        """ Invoke(self: LoadedEventHandler, sender: object, e: LoadedEventArgs) """
        ...


class LocalizationExtenderProvider(IExtenderProvider, IDisposable): # skipped bases: <type 'object'>
    """ LocalizationExtenderProvider(serviceProvider: ISite, baseComponent: IComponent) """
    def GetLanguage(self, o:object) -> CultureInfo:
        """ GetLanguage(self: LocalizationExtenderProvider, o: object) -> CultureInfo """
        ...

    def GetLoadLanguage(self, o:object) -> CultureInfo:
        """ GetLoadLanguage(self: LocalizationExtenderProvider, o: object) -> CultureInfo """
        ...

    def GetLocalizable(self, o:object) -> bool:
        """ GetLocalizable(self: LocalizationExtenderProvider, o: object) -> bool """
        ...

    def ResetLanguage(self, o:object): # -> 
        """ ResetLanguage(self: LocalizationExtenderProvider, o: object) """
        ...

    def SetLanguage(self, o:object, language:CultureInfo): # -> 
        """ SetLanguage(self: LocalizationExtenderProvider, o: object, language: CultureInfo) """
        ...

    def SetLocalizable(self, o:object, localizable:bool): # -> 
        """ SetLocalizable(self: LocalizationExtenderProvider, o: object, localizable: bool) """
        ...

    def ShouldSerializeLanguage(self, o:object) -> bool:
        """ ShouldSerializeLanguage(self: LocalizationExtenderProvider, o: object) -> bool """
        ...


class MenuCommandsChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MenuCommandsChangedEventArgs(changeType: MenuCommandsChangedType, command: MenuCommand) """
    @property
    def ChangeType(self): # -> MenuCommandsChangedType
        """ Get: ChangeType(self: MenuCommandsChangedEventArgs) -> MenuCommandsChangedType """
        ...

    @property
    def Command(self) -> MenuCommand:
        """ Get: Command(self: MenuCommandsChangedEventArgs) -> MenuCommand """
        ...


    def __new__(cls, changeType, command:MenuCommand) -> Self: # Not found arg types: {'changeType': 'MenuCommandsChangedType'}
        """ __new__(cls: type, changeType: MenuCommandsChangedType, command: MenuCommand) """
        ...


class MenuCommandsChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MenuCommandsChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MenuCommandsChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MenuCommandsChangedEventHandler, sender: object, e: MenuCommandsChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MenuCommandsChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MenuCommandsChangedEventArgs): # -> 
        """ Invoke(self: MenuCommandsChangedEventHandler, sender: object, e: MenuCommandsChangedEventArgs) """
        ...


class MenuCommandsChangedType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MenuCommandsChangedType, values: CommandAdded (0), CommandChanged (2), CommandRemoved (1) """
    CommandAdded: MenuCommandsChangedType = ...
    CommandChanged: MenuCommandsChangedType = ...
    CommandRemoved: MenuCommandsChangedType = ...
    value__ = ...


class MenuCommandService(IDisposable, IMenuCommandService): # skipped bases: <type 'object'>
    """ MenuCommandService(serviceProvider: IServiceProvider) """
    def EnsureVerbs(self, *args): #cannot find CLR method
        """ EnsureVerbs(self: MenuCommandService) """
        ...

    def GetCommandList(self, *args): #cannot find CLR method
        """ GetCommandList(self: MenuCommandService, guid: Guid) -> ICollection """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: MenuCommandService, serviceType: Type) -> object """
        ...

    def OnCommandsChanged(self, *args): #cannot find CLR method
        """ OnCommandsChanged(self: MenuCommandService, e: MenuCommandsChangedEventArgs) """
        ...

    MenuCommandsChanged = ...


class MultilineStringEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ MultilineStringEditor() """
    pass

class ObjectSelectorEditor(UITypeEditor): # skipped bases: <type 'object'>
    """
    ObjectSelectorEditor()
    ObjectSelectorEditor(subObjectSelector: bool)
    """
    def EqualsToValue(self, value:object) -> bool:
        """ EqualsToValue(self: ObjectSelectorEditor, value: object) -> bool """
        ...

    def FillTreeWithData(self, *args): #cannot find CLR method
        """ FillTreeWithData(self: ObjectSelectorEditor, selector: Selector, context: ITypeDescriptorContext, provider: IServiceProvider) """
        ...

    def Selector(self, *args): #cannot find CLR method
        """ Selector(editor: ObjectSelectorEditor) """
        ...

    def SelectorNode(self, *args): #cannot find CLR method
        """ SelectorNode(label: str, value: object) """
        ...

    def SetValue(self, value:object): # -> 
        """ SetValue(self: ObjectSelectorEditor, value: object) """
        ...

    def __new__(cls, subObjectSelector:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, subObjectSelector: bool)
        """
        ...

    currValue = ...
    prevValue = ...
    SubObjectSelector = ...


class ProjectTargetFrameworkAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ProjectTargetFrameworkAttribute(targetFrameworkMoniker: str) """
    @property
    def TargetFrameworkMoniker(self) -> str:
        """ Get: TargetFrameworkMoniker(self: ProjectTargetFrameworkAttribute) -> str """
        ...


    def __new__(cls, targetFrameworkMoniker:str) -> Self:
        """ __new__(cls: type, targetFrameworkMoniker: str) """
        ...


class SelectionTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SelectionTypes, values: Add (64), Auto (1), Click (16), MouseDown (4), MouseUp (8), Normal (1), Primary (16), Remove (128), Replace (2), Toggle (32), Valid (31) """
    Add: SelectionTypes = ...
    Auto: SelectionTypes = ...
    Click: SelectionTypes = ...
    MouseDown: SelectionTypes = ...
    MouseUp: SelectionTypes = ...
    Normal: SelectionTypes = ...
    Primary: SelectionTypes = ...
    Remove: SelectionTypes = ...
    Replace: SelectionTypes = ...
    Toggle: SelectionTypes = ...
    Valid: SelectionTypes = ...
    value__ = ...


class ServiceContainer(IDisposable, IServiceContainer): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """
    ServiceContainer()
    ServiceContainer(parentProvider: IServiceProvider)
    """
    @property
    def DefaultServices(self):
        ...


    def GetService(self, serviceType:Type) -> object:
        """ GetService(self: ServiceContainer, serviceType: Type) -> object """
        ...


class ServiceCreatorCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ServiceCreatorCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, container:IServiceContainer, serviceType:Type, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: ServiceCreatorCallback, result: IAsyncResult) -> object """
        ...

    def Invoke(self, container:IServiceContainer, serviceType:Type) -> object:
        """ Invoke(self: ServiceCreatorCallback, container: IServiceContainer, serviceType: Type) -> object """
        ...


class StandardCommands: # skipped bases: <type 'object'>, <type 'object'>
    """ StandardCommands() """
    AlignBottom: CommandID = ...
    AlignHorizontalCenters: CommandID = ...
    AlignLeft: CommandID = ...
    AlignRight: CommandID = ...
    AlignToGrid: CommandID = ...
    AlignTop: CommandID = ...
    AlignVerticalCenters: CommandID = ...
    ArrangeBottom: CommandID = ...
    ArrangeIcons: CommandID = ...
    ArrangeRight: CommandID = ...
    BringForward: CommandID = ...
    BringToFront: CommandID = ...
    CenterHorizontally: CommandID = ...
    CenterVertically: CommandID = ...
    Copy: CommandID = ...
    Cut: CommandID = ...
    Delete: CommandID = ...
    DocumentOutline: CommandID = ...
    F1Help: CommandID = ...
    Group: CommandID = ...
    HorizSpaceConcatenate: CommandID = ...
    HorizSpaceDecrease: CommandID = ...
    HorizSpaceIncrease: CommandID = ...
    HorizSpaceMakeEqual: CommandID = ...
    LineupIcons: CommandID = ...
    LockControls: CommandID = ...
    MultiLevelRedo: CommandID = ...
    MultiLevelUndo: CommandID = ...
    Paste: CommandID = ...
    Properties: CommandID = ...
    PropertiesWindow: CommandID = ...
    Redo: CommandID = ...
    Replace: CommandID = ...
    SelectAll: CommandID = ...
    SendBackward: CommandID = ...
    SendToBack: CommandID = ...
    ShowGrid: CommandID = ...
    ShowLargeIcons: CommandID = ...
    SizeToControl: CommandID = ...
    SizeToControlHeight: CommandID = ...
    SizeToControlWidth: CommandID = ...
    SizeToFit: CommandID = ...
    SizeToGrid: CommandID = ...
    SnapToGrid: CommandID = ...
    TabOrder: CommandID = ...
    Undo: CommandID = ...
    Ungroup: CommandID = ...
    VerbFirst: CommandID = ...
    VerbLast: CommandID = ...
    VertSpaceConcatenate: CommandID = ...
    VertSpaceDecrease: CommandID = ...
    VertSpaceIncrease: CommandID = ...
    VertSpaceMakeEqual: CommandID = ...
    ViewCode: CommandID = ...
    ViewGrid: CommandID = ...


class StandardToolWindows: # skipped bases: <type 'object'>, <type 'object'>
    """ StandardToolWindows() """
    ObjectBrowser: Guid = ...
    OutputWindow: Guid = ...
    ProjectExplorer: Guid = ...
    PropertyBrowser: Guid = ...
    RelatedLinks: Guid = ...
    ServerExplorer: Guid = ...
    TaskList: Guid = ...
    Toolbox: Guid = ...


class TypeDescriptionProviderService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetProvider(self, *__args:object) -> TypeDescriptionProvider:
        """
        GetProvider(self: TypeDescriptionProviderService, instance: object) -> TypeDescriptionProvider
        GetProvider(self: TypeDescriptionProviderService, type: Type) -> TypeDescriptionProvider
        """
        ...


class UndoEngine(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: UndoEngine) -> bool
        Set: Enabled(self: UndoEngine) = value
        """
        ...

    @property
    def UndoInProgress(self) -> bool:
        """ Get: UndoInProgress(self: UndoEngine) -> bool """
        ...


    def AddUndoUnit(self, *args): #cannot find CLR method
        """ AddUndoUnit(self: UndoEngine, unit: UndoUnit) """
        ...

    def CreateUndoUnit(self, *args): #cannot find CLR method
        """ CreateUndoUnit(self: UndoEngine, name: str, primary: bool) -> UndoUnit """
        ...

    def DiscardUndoUnit(self, *args): #cannot find CLR method
        """ DiscardUndoUnit(self: UndoEngine, unit: UndoUnit) """
        ...

    def GetRequiredService(self, *args): #cannot find CLR method
        """ GetRequiredService(self: UndoEngine, serviceType: Type) -> object """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: UndoEngine, serviceType: Type) -> object """
        ...

    def OnUndoing(self, *args): #cannot find CLR method
        """ OnUndoing(self: UndoEngine, e: EventArgs) """
        ...

    def OnUndone(self, *args): #cannot find CLR method
        """ OnUndone(self: UndoEngine, e: EventArgs) """
        ...

    def UndoUnit(self, *args): #cannot find CLR method
        """ UndoUnit(engine: UndoEngine, name: str) """
        ...

    Undoing = ...
    Undone = ...


class ViewTechnology(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ViewTechnology, values: Default (2), Passthrough (0), WindowsForms (1) """
    Default: ViewTechnology = ...
    Passthrough: ViewTechnology = ...
    value__ = ...
    WindowsForms: ViewTechnology = ...


# variables with complex values

