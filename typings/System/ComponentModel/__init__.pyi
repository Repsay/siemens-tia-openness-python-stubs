# encoding: utf-8
# module System.ComponentModel calls itself ComponentModel
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.ComponentModel.DataAnnotations, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (ArgumentException, Array, AsyncCallback, Attribute, Char, 
    Delegate, Enum, EventArgs, EventHandler, IAsyncResult, ICloneable, 
    IDisposable, IServiceProvider, MarshalByRefObject, MulticastDelegate, 
    SystemException, Type)

from System.Collections import (Hashtable, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList, ReadOnlyCollectionBase)

from System.Collections.ObjectModel import Collection

from System.ComponentModel.Design import IDesigner

from System.Globalization import CultureInfo

from System.Reflection import Assembly

from System.Resources import ResourceManager

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Threading import SendOrPostCallback, SynchronizationContext

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    StandardValuesCollection, field#)
"""

# no functions
# classes

class AddingNewEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    AddingNewEventArgs()
    AddingNewEventArgs(newObject: object)
    """
    @property
    def NewObject(self) -> object:
        """
        Get: NewObject(self: AddingNewEventArgs) -> object
        Set: NewObject(self: AddingNewEventArgs) = value
        """
        ...


    def __new__(cls, newObject:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, newObject: object)
        """
        ...


class AddingNewEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AddingNewEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AddingNewEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AddingNewEventHandler, sender: object, e: AddingNewEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: AddingNewEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AddingNewEventArgs): # -> 
        """ Invoke(self: AddingNewEventHandler, sender: object, e: AddingNewEventArgs) """
        ...


class AmbientValueAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    AmbientValueAttribute(type: Type, value: str)
    AmbientValueAttribute(value: Char)
    AmbientValueAttribute(value: Byte)
    AmbientValueAttribute(value: Int16)
    AmbientValueAttribute(value: int)
    AmbientValueAttribute(value: Int64)
    AmbientValueAttribute(value: Single)
    AmbientValueAttribute(value: float)
    AmbientValueAttribute(value: bool)
    AmbientValueAttribute(value: str)
    AmbientValueAttribute(value: object)
    """
    @property
    def Value(self) -> object:
        """ Get: Value(self: AmbientValueAttribute) -> object """
        ...


    def __new__(cls, *__args:Char) -> Self:
        """
        __new__(cls: type, type: Type, value: str)
        __new__(cls: type, value: Char)
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: Int16)
        __new__(cls: type, value: int)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: Single)
        __new__(cls: type, value: float)
        __new__(cls: type, value: bool)
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        ...


class TypeConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ TypeConverter() """
    def CanConvertFrom(self, *__args:Type) -> bool:
        """
        CanConvertFrom(self: TypeConverter, sourceType: Type) -> bool
        CanConvertFrom(self: TypeConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        """
        ...

    def CanConvertTo(self, *__args:Type) -> bool:
        """
        CanConvertTo(self: TypeConverter, destinationType: Type) -> bool
        CanConvertTo(self: TypeConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        """
        ...

    def ConvertFrom(self, *__args:object) -> object:
        """
        ConvertFrom(self: TypeConverter, value: object) -> object
        ConvertFrom(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        """
        ...

    def ConvertFromInvariantString(self, *__args:str) -> object:
        """
        ConvertFromInvariantString(self: TypeConverter, text: str) -> object
        ConvertFromInvariantString(self: TypeConverter, context: ITypeDescriptorContext, text: str) -> object
        """
        ...

    def ConvertFromString(self, *__args:str) -> object:
        """
        ConvertFromString(self: TypeConverter, text: str) -> object
        ConvertFromString(self: TypeConverter, context: ITypeDescriptorContext, text: str) -> object
        ConvertFromString(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, text: str) -> object
        """
        ...

    def ConvertTo(self, *__args) -> object:
        """
        ConvertTo(self: TypeConverter, value: object, destinationType: Type) -> object
        ConvertTo(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        """
        ...

    def ConvertToInvariantString(self, *__args:object) -> str:
        """
        ConvertToInvariantString(self: TypeConverter, value: object) -> str
        ConvertToInvariantString(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> str
        """
        ...

    def ConvertToString(self, *__args:object) -> str:
        """
        ConvertToString(self: TypeConverter, value: object) -> str
        ConvertToString(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> str
        ConvertToString(self: TypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> str
        """
        ...

    def CreateInstance(self, *__args:IDictionary) -> object:
        """
        CreateInstance(self: TypeConverter, propertyValues: IDictionary) -> object
        CreateInstance(self: TypeConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object
        """
        ...

    def GetConvertFromException(self, *args): #cannot find CLR method
        """ GetConvertFromException(self: TypeConverter, value: object) -> Exception """
        ...

    def GetConvertToException(self, *args): #cannot find CLR method
        """ GetConvertToException(self: TypeConverter, value: object, destinationType: Type) -> Exception """
        ...

    def GetCreateInstanceSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """
        GetCreateInstanceSupported(self: TypeConverter) -> bool
        GetCreateInstanceSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        """
        ...

    def GetProperties(self, *__args:object) -> PropertyDescriptorCollection:
        """
        GetProperties(self: TypeConverter, value: object) -> PropertyDescriptorCollection
        GetProperties(self: TypeConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        GetProperties(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> PropertyDescriptorCollection
        """
        ...

    def GetPropertiesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """
        GetPropertiesSupported(self: TypeConverter) -> bool
        GetPropertiesSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        """
        ...

    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """
        GetStandardValues(self: TypeConverter) -> ICollection
        GetStandardValues(self: TypeConverter, context: ITypeDescriptorContext) -> StandardValuesCollection
        """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """
        GetStandardValuesExclusive(self: TypeConverter) -> bool
        GetStandardValuesExclusive(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """
        GetStandardValuesSupported(self: TypeConverter) -> bool
        GetStandardValuesSupported(self: TypeConverter, context: ITypeDescriptorContext) -> bool
        """
        ...

    def IsValid(self, *__args:object) -> bool:
        """
        IsValid(self: TypeConverter, value: object) -> bool
        IsValid(self: TypeConverter, context: ITypeDescriptorContext, value: object) -> bool
        """
        ...

    def SimplePropertyDescriptor(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def SortProperties(self, *args): #cannot find CLR method
        """ SortProperties(self: TypeConverter, props: PropertyDescriptorCollection, names: Array[str]) -> PropertyDescriptorCollection """
        ...

    def StandardValuesCollection(self, *args): #cannot find CLR method
        """ StandardValuesCollection(values: ICollection) """
        ...



class CollectionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ CollectionConverter() """
    pass

class ArrayConverter(CollectionConverter): # skipped bases: <type 'object'>
    """ ArrayConverter() """
    pass

class AsyncCompletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    AsyncCompletedEventArgs()
    AsyncCompletedEventArgs(error: Exception, cancelled: bool, userState: object)
    """
    @property
    def Cancelled(self) -> bool:
        """ Get: Cancelled(self: AsyncCompletedEventArgs) -> bool """
        ...

    @property
    def Error(self) -> Exception:
        """ Get: Error(self: AsyncCompletedEventArgs) -> Exception """
        ...

    @property
    def UserState(self) -> object:
        """ Get: UserState(self: AsyncCompletedEventArgs) -> object """
        ...


    def RaiseExceptionIfNecessary(self, *args): #cannot find CLR method
        """ RaiseExceptionIfNecessary(self: AsyncCompletedEventArgs) """
        ...

    def __new__(cls, error:Exception = ..., cancelled:bool = ..., userState:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, error: Exception, cancelled: bool, userState: object)
        """
        ...


class AsyncCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AsyncCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AsyncCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AsyncCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: AsyncCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AsyncCompletedEventArgs): # -> 
        """ Invoke(self: AsyncCompletedEventHandler, sender: object, e: AsyncCompletedEventArgs) """
        ...


class AsyncOperation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """ Get: SynchronizationContext(self: AsyncOperation) -> SynchronizationContext """
        ...

    @property
    def UserSuppliedState(self) -> object:
        """ Get: UserSuppliedState(self: AsyncOperation) -> object """
        ...


    def OperationCompleted(self): # -> 
        """ OperationCompleted(self: AsyncOperation) """
        ...

    def Post(self, d:SendOrPostCallback, arg:object): # -> 
        """ Post(self: AsyncOperation, d: SendOrPostCallback, arg: object) """
        ...

    def PostOperationCompleted(self, d:SendOrPostCallback, arg:object): # -> 
        """ PostOperationCompleted(self: AsyncOperation, d: SendOrPostCallback, arg: object) """
        ...


class AsyncOperationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """
        Get: SynchronizationContext() -> SynchronizationContext
        Set: SynchronizationContext() = value
        """
        ...


    @staticmethod
    def CreateOperation(userSuppliedState:object) -> AsyncOperation:
        """ CreateOperation(userSuppliedState: object) -> AsyncOperation """
        ...

    __all__: list = ...


class AttributeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ AttributeCollection(*attributes: Array[Attribute]) """
    @property
    def Attributes(self):
        ...


    def Contains(self, *__args:Attribute) -> bool:
        """
        Contains(self: AttributeCollection, attribute: Attribute) -> bool
        Contains(self: AttributeCollection, attributes: Array[Attribute]) -> bool
        """
        ...

    @staticmethod
    def FromExisting(existing:AttributeCollection, newAttributes:Array) -> AttributeCollection:
        """ FromExisting(existing: AttributeCollection, *newAttributes: Array[Attribute]) -> AttributeCollection """
        ...

    def GetDefaultAttribute(self, *args): #cannot find CLR method
        """ GetDefaultAttribute(self: AttributeCollection, attributeType: Type) -> Attribute """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: AttributeCollection) -> IEnumerator """
        ...

    def Matches(self, *__args:Attribute) -> bool:
        """
        Matches(self: AttributeCollection, attribute: Attribute) -> bool
        Matches(self: AttributeCollection, attributes: Array[Attribute]) -> bool
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    Empty: AttributeCollection = ...


class AttributeProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    AttributeProviderAttribute(typeName: str)
    AttributeProviderAttribute(typeName: str, propertyName: str)
    AttributeProviderAttribute(type: Type)
    """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: AttributeProviderAttribute) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: AttributeProviderAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, typeName: str)
        __new__(cls: type, typeName: str, propertyName: str)
        __new__(cls: type, type: Type)
        """
        ...


class Component(MarshalByRefObject, IComponent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ Component() """
    @property
    def CanRaiseEvents(self):
        ...

    @property
    def Container(self) -> IContainer:
        """ Get: Container(self: Component) -> IContainer """
        ...

    @property
    def DesignMode(self):
        ...

    @property
    def Events(self):
        ...


    def Dispose(self): # -> 
        """ Dispose(self: Component) """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: Component, service: Type) -> object """
        ...

    def ToString(self) -> str:
        """ ToString(self: Component) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    Disposed = ...


class BackgroundWorker(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ BackgroundWorker() """
    @property
    def CancellationPending(self) -> bool:
        """ Get: CancellationPending(self: BackgroundWorker) -> bool """
        ...

    @property
    def IsBusy(self) -> bool:
        """ Get: IsBusy(self: BackgroundWorker) -> bool """
        ...

    @property
    def WorkerReportsProgress(self) -> bool:
        """
        Get: WorkerReportsProgress(self: BackgroundWorker) -> bool
        Set: WorkerReportsProgress(self: BackgroundWorker) = value
        """
        ...

    @property
    def WorkerSupportsCancellation(self) -> bool:
        """
        Get: WorkerSupportsCancellation(self: BackgroundWorker) -> bool
        Set: WorkerSupportsCancellation(self: BackgroundWorker) = value
        """
        ...


    def CancelAsync(self): # -> 
        """ CancelAsync(self: BackgroundWorker) """
        ...

    def OnDoWork(self, *args): #cannot find CLR method
        """ OnDoWork(self: BackgroundWorker, e: DoWorkEventArgs) """
        ...

    def OnProgressChanged(self, *args): #cannot find CLR method
        """ OnProgressChanged(self: BackgroundWorker, e: ProgressChangedEventArgs) """
        ...

    def OnRunWorkerCompleted(self, *args): #cannot find CLR method
        """ OnRunWorkerCompleted(self: BackgroundWorker, e: RunWorkerCompletedEventArgs) """
        ...

    def ReportProgress(self, percentProgress:int, userState:object = ...): # -> 
        """ ReportProgress(self: BackgroundWorker, percentProgress: int)ReportProgress(self: BackgroundWorker, percentProgress: int, userState: object) """
        ...

    def RunWorkerAsync(self, argument:object = ...): # -> 
        """ RunWorkerAsync(self: BackgroundWorker)RunWorkerAsync(self: BackgroundWorker, argument: object) """
        ...

    DoWork = ...
    ProgressChanged = ...
    RunWorkerCompleted = ...


class BaseNumberConverter(TypeConverter): # skipped bases: <type 'object'>
    """ no doc """
    pass

class BindableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    BindableAttribute(bindable: bool)
    BindableAttribute(bindable: bool, direction: BindingDirection)
    BindableAttribute(flags: BindableSupport)
    BindableAttribute(flags: BindableSupport, direction: BindingDirection)
    """
    @property
    def Bindable(self) -> bool:
        """ Get: Bindable(self: BindableAttribute) -> bool """
        ...

    @property
    def Direction(self) -> BindingDirection:
        """ Get: Direction(self: BindableAttribute) -> BindingDirection """
        ...


    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type, bindable: bool)
        __new__(cls: type, bindable: bool, direction: BindingDirection)
        __new__(cls: type, flags: BindableSupport)
        __new__(cls: type, flags: BindableSupport, direction: BindingDirection)
        """
        ...

    Default: BindableAttribute = ...
    No: BindableAttribute = ...
    Yes: BindableAttribute = ...


class BindableSupport(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BindableSupport, values: Default (2), No (0), Yes (1) """
    Default: BindableSupport = ...
    No: BindableSupport = ...
    value__ = ...
    Yes: BindableSupport = ...


class BindingDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BindingDirection, values: OneWay (0), TwoWay (1) """
    OneWay: BindingDirection = ...
    TwoWay: BindingDirection = ...
    value__ = ...


class IBindingList(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def AllowEdit(self) -> bool:
        """ Get: AllowEdit(self: IBindingList) -> bool """
        ...

    @property
    def AllowNew(self) -> bool:
        """ Get: AllowNew(self: IBindingList) -> bool """
        ...

    @property
    def AllowRemove(self) -> bool:
        """ Get: AllowRemove(self: IBindingList) -> bool """
        ...

    @property
    def IsSorted(self) -> bool:
        """ Get: IsSorted(self: IBindingList) -> bool """
        ...

    @property
    def SortDirection(self) -> ListSortDirection:
        """ Get: SortDirection(self: IBindingList) -> ListSortDirection """
        ...

    @property
    def SortProperty(self) -> PropertyDescriptor:
        """ Get: SortProperty(self: IBindingList) -> PropertyDescriptor """
        ...

    @property
    def SupportsChangeNotification(self) -> bool:
        """ Get: SupportsChangeNotification(self: IBindingList) -> bool """
        ...

    @property
    def SupportsSearching(self) -> bool:
        """ Get: SupportsSearching(self: IBindingList) -> bool """
        ...

    @property
    def SupportsSorting(self) -> bool:
        """ Get: SupportsSorting(self: IBindingList) -> bool """
        ...


    def AddIndex(self, property:PropertyDescriptor): # -> 
        """ AddIndex(self: IBindingList, property: PropertyDescriptor) """
        ...

    def AddNew(self) -> object:
        """ AddNew(self: IBindingList) -> object """
        ...

    def ApplySort(self, property:PropertyDescriptor, direction:ListSortDirection): # -> 
        """ ApplySort(self: IBindingList, property: PropertyDescriptor, direction: ListSortDirection) """
        ...

    def Find(self, property:PropertyDescriptor, key:object) -> int:
        """ Find(self: IBindingList, property: PropertyDescriptor, key: object) -> int """
        ...

    def RemoveIndex(self, property:PropertyDescriptor): # -> 
        """ RemoveIndex(self: IBindingList, property: PropertyDescriptor) """
        ...

    def RemoveSort(self): # -> 
        """ RemoveSort(self: IBindingList) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...

    ListChanged = ...


class ICancelAddNew: # skipped bases: <type 'object'>
    """ no doc """
    def CancelNew(self, itemIndex:int): # -> 
        """ CancelNew(self: ICancelAddNew, itemIndex: int) """
        ...

    def EndNew(self, itemIndex:int): # -> 
        """ EndNew(self: ICancelAddNew, itemIndex: int) """
        ...


class IRaiseItemChangedEvents: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RaisesItemChangedEvents(self) -> bool:
        """ Get: RaisesItemChangedEvents(self: IRaiseItemChangedEvents) -> bool """
        ...



class BindingList(ICancelAddNew, IRaiseItemChangedEvents, IBindingList, Collection): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[T]'>, <type 'ICollection'>, <type 'IReadOnlyList[T]'>, <type 'object'>
    """
    BindingList[T]()
    BindingList[T](list: IList[T])
    """
    @property
    def IsSortedCore(self):
        ...

    @property
    def RaiseListChangedEvents(self) -> bool:
        """
        Get: RaiseListChangedEvents(self: BindingList[T]) -> bool
        Set: RaiseListChangedEvents(self: BindingList[T]) = value
        """
        ...

    @property
    def SortDirectionCore(self):
        ...

    @property
    def SortPropertyCore(self):
        ...

    @property
    def SupportsChangeNotificationCore(self):
        ...

    @property
    def SupportsSearchingCore(self):
        ...

    @property
    def SupportsSortingCore(self):
        ...


    def AddNewCore(self, *args): #cannot find CLR method
        """ AddNewCore(self: BindingList[T]) -> object """
        ...

    def ApplySortCore(self, *args): #cannot find CLR method
        """ ApplySortCore(self: BindingList[T], prop: PropertyDescriptor, direction: ListSortDirection) """
        ...

    def FindCore(self, *args): #cannot find CLR method
        """ FindCore(self: BindingList[T], prop: PropertyDescriptor, key: object) -> int """
        ...

    def OnAddingNew(self, *args): #cannot find CLR method
        """ OnAddingNew(self: BindingList[T], e: AddingNewEventArgs) """
        ...

    def OnListChanged(self, *args): #cannot find CLR method
        """ OnListChanged(self: BindingList[T], e: ListChangedEventArgs) """
        ...

    def RemoveSortCore(self, *args): #cannot find CLR method
        """ RemoveSortCore(self: BindingList[T]) """
        ...

    def ResetBindings(self): # -> 
        """ ResetBindings(self: BindingList[T]) """
        ...

    def ResetItem(self, position:int): # -> 
        """ ResetItem(self: BindingList[T], position: int) """
        ...

    AddingNew = ...
    ListChanged = ...


class BooleanConverter(TypeConverter): # skipped bases: <type 'object'>
    """ BooleanConverter() """
    pass

class BrowsableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BrowsableAttribute(browsable: bool) """
    @property
    def Browsable(self) -> bool:
        """ Get: Browsable(self: BrowsableAttribute) -> bool """
        ...


    def __new__(cls, browsable:bool) -> Self:
        """ __new__(cls: type, browsable: bool) """
        ...

    Default: BrowsableAttribute = ...
    No: BrowsableAttribute = ...
    Yes: BrowsableAttribute = ...


class ByteConverter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ ByteConverter() """
    pass

class CancelEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    CancelEventArgs()
    CancelEventArgs(cancel: bool)
    """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: CancelEventArgs) -> bool
        Set: Cancel(self: CancelEventArgs) = value
        """
        ...


    def __new__(cls, cancel:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cancel: bool)
        """
        ...


class CancelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CancelEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelEventArgs): # -> 
        """ Invoke(self: CancelEventHandler, sender: object, e: CancelEventArgs) """
        ...


class CategoryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    CategoryAttribute()
    CategoryAttribute(category: str)
    """
    @property
    def Action(self) -> CategoryAttribute:
        """ Get: Action() -> CategoryAttribute """
        ...

    @property
    def Appearance(self) -> CategoryAttribute:
        """ Get: Appearance() -> CategoryAttribute """
        ...

    @property
    def Asynchronous(self) -> CategoryAttribute:
        """ Get: Asynchronous() -> CategoryAttribute """
        ...

    @property
    def Behavior(self) -> CategoryAttribute:
        """ Get: Behavior() -> CategoryAttribute """
        ...

    @property
    def Category(self) -> str:
        """ Get: Category(self: CategoryAttribute) -> str """
        ...

    @property
    def Data(self) -> CategoryAttribute:
        """ Get: Data() -> CategoryAttribute """
        ...

    @property
    def Default(self) -> CategoryAttribute:
        """ Get: Default() -> CategoryAttribute """
        ...

    @property
    def Design(self) -> CategoryAttribute:
        """ Get: Design() -> CategoryAttribute """
        ...

    @property
    def DragDrop(self) -> CategoryAttribute:
        """ Get: DragDrop() -> CategoryAttribute """
        ...

    @property
    def Focus(self) -> CategoryAttribute:
        """ Get: Focus() -> CategoryAttribute """
        ...

    @property
    def Format(self) -> CategoryAttribute:
        """ Get: Format() -> CategoryAttribute """
        ...

    @property
    def Key(self) -> CategoryAttribute:
        """ Get: Key() -> CategoryAttribute """
        ...

    @property
    def Layout(self) -> CategoryAttribute:
        """ Get: Layout() -> CategoryAttribute """
        ...

    @property
    def Mouse(self) -> CategoryAttribute:
        """ Get: Mouse() -> CategoryAttribute """
        ...

    @property
    def WindowStyle(self) -> CategoryAttribute:
        """ Get: WindowStyle() -> CategoryAttribute """
        ...


    def GetLocalizedString(self, *args): #cannot find CLR method
        """ GetLocalizedString(self: CategoryAttribute, value: str) -> str """
        ...

    def __new__(cls, category:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, category: str)
        """
        ...



class CharConverter(TypeConverter): # skipped bases: <type 'object'>
    """ CharConverter() """
    pass

class CollectionChangeAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CollectionChangeAction, values: Add (1), Refresh (3), Remove (2) """
    Add: CollectionChangeAction = ...
    Refresh: CollectionChangeAction = ...
    Remove: CollectionChangeAction = ...
    value__ = ...


class CollectionChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CollectionChangeEventArgs(action: CollectionChangeAction, element: object) """
    @property
    def Action(self) -> CollectionChangeAction:
        """ Get: Action(self: CollectionChangeEventArgs) -> CollectionChangeAction """
        ...

    @property
    def Element(self) -> object:
        """ Get: Element(self: CollectionChangeEventArgs) -> object """
        ...


    def __new__(cls, action:CollectionChangeAction, element:object) -> Self:
        """ __new__(cls: type, action: CollectionChangeAction, element: object) """
        ...


class CollectionChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CollectionChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CollectionChangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CollectionChangeEventHandler, sender: object, e: CollectionChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CollectionChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CollectionChangeEventArgs): # -> 
        """ Invoke(self: CollectionChangeEventHandler, sender: object, e: CollectionChangeEventArgs) """
        ...


class ComplexBindingPropertiesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ComplexBindingPropertiesAttribute()
    ComplexBindingPropertiesAttribute(dataSource: str)
    ComplexBindingPropertiesAttribute(dataSource: str, dataMember: str)
    """
    @property
    def DataMember(self) -> str:
        """ Get: DataMember(self: ComplexBindingPropertiesAttribute) -> str """
        ...

    @property
    def DataSource(self) -> str:
        """ Get: DataSource(self: ComplexBindingPropertiesAttribute) -> str """
        ...


    def __new__(cls, dataSource:str = ..., dataMember:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dataSource: str)
        __new__(cls: type, dataSource: str, dataMember: str)
        """
        ...

    Default: ComplexBindingPropertiesAttribute = ...


class ComponentCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ComponentCollection(components: Array[IComponent]) """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ComponentCollection, array: Array[IComponent], index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, components:Array) -> Self:
        """ __new__(cls: type, components: Array[IComponent]) """
        ...


class ReferenceConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ReferenceConverter(type: Type) """
    def IsValueAllowed(self, *args): #cannot find CLR method
        """ IsValueAllowed(self: ReferenceConverter, context: ITypeDescriptorContext, value: object) -> bool """
        ...

    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class ComponentConverter(ReferenceConverter): # skipped bases: <type 'object'>
    """ ComponentConverter(type: Type) """
    def GetProperties(self, *__args) -> PropertyDescriptorCollection:
        """ GetProperties(self: ComponentConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection """
        ...

    def GetPropertiesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetPropertiesSupported(self: ComponentConverter, context: ITypeDescriptorContext) -> bool """
        ...


class ComponentEditor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def EditComponent(self, *__args:object) -> bool:
        """
        EditComponent(self: ComponentEditor, component: object) -> bool
        EditComponent(self: ComponentEditor, context: ITypeDescriptorContext, component: object) -> bool
        """
        ...


class ComponentResourceManager(ResourceManager): # skipped bases: <type 'object'>
    """
    ComponentResourceManager()
    ComponentResourceManager(t: Type)
    """
    def ApplyResources(self, value:object, objectName:str, culture:CultureInfo = ...): # -> 
        """ ApplyResources(self: ComponentResourceManager, value: object, objectName: str)ApplyResources(self: ComponentResourceManager, value: object, objectName: str, culture: CultureInfo) """
        ...

    BaseNameField = ...
    MainAssembly = ...
    ResourceSets = ...


class Container(IContainer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ Container() """
    def CreateSite(self, *args): #cannot find CLR method
        """ CreateSite(self: Container, component: IComponent, name: str) -> ISite """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: Container) """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: Container, service: Type) -> object """
        ...

    def RemoveWithoutUnsiting(self, *args): #cannot find CLR method
        """ RemoveWithoutUnsiting(self: Container, component: IComponent) """
        ...

    def ValidateName(self, *args): #cannot find CLR method
        """ ValidateName(self: Container, component: IComponent, name: str) """
        ...


class ContainerFilterService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def FilterComponents(self, components:ComponentCollection) -> ComponentCollection:
        """ FilterComponents(self: ContainerFilterService, components: ComponentCollection) -> ComponentCollection """
        ...


class CultureInfoConverter(TypeConverter): # skipped bases: <type 'object'>
    """ CultureInfoConverter() """
    def GetCultureName(self, *args): #cannot find CLR method
        """ GetCultureName(self: CultureInfoConverter, culture: CultureInfo) -> str """
        ...


class CustomTypeDescriptor(ICustomTypeDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DataErrorsChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataErrorsChangedEventArgs(propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: DataErrorsChangedEventArgs) -> str """
        ...


    def __new__(cls, propertyName:str) -> Self:
        """ __new__(cls: type, propertyName: str) """
        ...


class DataObjectAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataObjectAttribute()
    DataObjectAttribute(isDataObject: bool)
    """
    @property
    def IsDataObject(self) -> bool:
        """ Get: IsDataObject(self: DataObjectAttribute) -> bool """
        ...


    def __new__(cls, isDataObject:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, isDataObject: bool)
        """
        ...

    DataObject: DataObjectAttribute = ...
    Default: DataObjectAttribute = ...
    NonDataObject: DataObjectAttribute = ...


class DataObjectFieldAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataObjectFieldAttribute(primaryKey: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool)
    DataObjectFieldAttribute(primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
    """
    @property
    def IsIdentity(self) -> bool:
        """ Get: IsIdentity(self: DataObjectFieldAttribute) -> bool """
        ...

    @property
    def IsNullable(self) -> bool:
        """ Get: IsNullable(self: DataObjectFieldAttribute) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: DataObjectFieldAttribute) -> int """
        ...

    @property
    def PrimaryKey(self) -> bool:
        """ Get: PrimaryKey(self: DataObjectFieldAttribute) -> bool """
        ...


    def __new__(cls, primaryKey:bool, isIdentity:bool = ..., isNullable:bool = ..., length:int = ...) -> Self:
        """
        __new__(cls: type, primaryKey: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool)
        __new__(cls: type, primaryKey: bool, isIdentity: bool, isNullable: bool, length: int)
        """
        ...


class DataObjectMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataObjectMethodAttribute(methodType: DataObjectMethodType)
    DataObjectMethodAttribute(methodType: DataObjectMethodType, isDefault: bool)
    """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: DataObjectMethodAttribute) -> bool """
        ...

    @property
    def MethodType(self) -> DataObjectMethodType:
        """ Get: MethodType(self: DataObjectMethodAttribute) -> DataObjectMethodType """
        ...


    def __new__(cls, methodType:DataObjectMethodType, isDefault:bool = ...) -> Self:
        """
        __new__(cls: type, methodType: DataObjectMethodType)
        __new__(cls: type, methodType: DataObjectMethodType, isDefault: bool)
        """
        ...


class DataObjectMethodType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataObjectMethodType, values: Delete (4), Fill (0), Insert (3), Select (1), Update (2) """
    Delete: DataObjectMethodType = ...
    Fill: DataObjectMethodType = ...
    Insert: DataObjectMethodType = ...
    Select: DataObjectMethodType = ...
    Update: DataObjectMethodType = ...
    value__ = ...


class DateTimeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DateTimeConverter() """
    pass

class DateTimeOffsetConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DateTimeOffsetConverter() """
    pass

class DecimalConverter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ DecimalConverter() """
    pass

class DefaultBindingPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DefaultBindingPropertyAttribute()
    DefaultBindingPropertyAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DefaultBindingPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...

    Default: DefaultBindingPropertyAttribute = ...


class DefaultEventAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultEventAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DefaultEventAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    Default: DefaultEventAttribute = ...


class DefaultPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DefaultPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    Default: DefaultPropertyAttribute = ...


class DefaultValueAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DefaultValueAttribute(type: Type, value: str)
    DefaultValueAttribute(value: Char)
    DefaultValueAttribute(value: Byte)
    DefaultValueAttribute(value: Int16)
    DefaultValueAttribute(value: int)
    DefaultValueAttribute(value: Int64)
    DefaultValueAttribute(value: Single)
    DefaultValueAttribute(value: float)
    DefaultValueAttribute(value: bool)
    DefaultValueAttribute(value: str)
    DefaultValueAttribute(value: object)
    """
    @property
    def Value(self) -> object:
        """ Get: Value(self: DefaultValueAttribute) -> object """
        ...


    def SetValue(self, *args): #cannot find CLR method
        """ SetValue(self: DefaultValueAttribute, value: object) """
        ...

    def __new__(cls, *__args:Char) -> Self:
        """
        __new__(cls: type, type: Type, value: str)
        __new__(cls: type, value: Char)
        __new__(cls: type, value: Byte)
        __new__(cls: type, value: Int16)
        __new__(cls: type, value: int)
        __new__(cls: type, value: Int64)
        __new__(cls: type, value: Single)
        __new__(cls: type, value: float)
        __new__(cls: type, value: bool)
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        ...


class DescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DescriptionAttribute()
    DescriptionAttribute(description: str)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: DescriptionAttribute) -> str """
        ...

    @property
    def DescriptionValue(self):
        ...


    def __new__(cls, description:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        ...

    Default: DescriptionAttribute = ...


class DesignerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignerAttribute(designerTypeName: str)
    DesignerAttribute(designerType: Type)
    DesignerAttribute(designerTypeName: str, designerBaseTypeName: str)
    DesignerAttribute(designerTypeName: str, designerBaseType: Type)
    DesignerAttribute(designerType: Type, designerBaseType: Type)
    """
    @property
    def DesignerBaseTypeName(self) -> str:
        """ Get: DesignerBaseTypeName(self: DesignerAttribute) -> str """
        ...

    @property
    def DesignerTypeName(self) -> str:
        """ Get: DesignerTypeName(self: DesignerAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, designerTypeName: str)
        __new__(cls: type, designerType: Type)
        __new__(cls: type, designerTypeName: str, designerBaseTypeName: str)
        __new__(cls: type, designerTypeName: str, designerBaseType: Type)
        __new__(cls: type, designerType: Type, designerBaseType: Type)
        """
        ...


class DesignerCategoryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignerCategoryAttribute()
    DesignerCategoryAttribute(category: str)
    """
    @property
    def Category(self) -> str:
        """ Get: Category(self: DesignerCategoryAttribute) -> str """
        ...


    def __new__(cls, category:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, category: str)
        """
        ...

    Component: DesignerCategoryAttribute = ...
    Default: DesignerCategoryAttribute = ...
    Form: DesignerCategoryAttribute = ...
    Generic: DesignerCategoryAttribute = ...


class DesignerSerializationVisibility(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DesignerSerializationVisibility, values: Content (2), Hidden (0), Visible (1) """
    Content: DesignerSerializationVisibility = ...
    Hidden: DesignerSerializationVisibility = ...
    value__ = ...
    Visible: DesignerSerializationVisibility = ...


class DesignerSerializationVisibilityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DesignerSerializationVisibilityAttribute(visibility: DesignerSerializationVisibility) """
    @property
    def Visibility(self) -> DesignerSerializationVisibility:
        """ Get: Visibility(self: DesignerSerializationVisibilityAttribute) -> DesignerSerializationVisibility """
        ...


    def __new__(cls, visibility:DesignerSerializationVisibility) -> Self:
        """ __new__(cls: type, visibility: DesignerSerializationVisibility) """
        ...

    Content: DesignerSerializationVisibilityAttribute = ...
    Default: DesignerSerializationVisibilityAttribute = ...
    Hidden: DesignerSerializationVisibilityAttribute = ...
    Visible: DesignerSerializationVisibilityAttribute = ...


class DesignOnlyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DesignOnlyAttribute(isDesignOnly: bool) """
    @property
    def IsDesignOnly(self) -> bool:
        """ Get: IsDesignOnly(self: DesignOnlyAttribute) -> bool """
        ...


    def __new__(cls, isDesignOnly:bool) -> Self:
        """ __new__(cls: type, isDesignOnly: bool) """
        ...

    Default: DesignOnlyAttribute = ...
    No: DesignOnlyAttribute = ...
    Yes: DesignOnlyAttribute = ...


class DesignTimeVisibleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignTimeVisibleAttribute(visible: bool)
    DesignTimeVisibleAttribute()
    """
    @property
    def Visible(self) -> bool:
        """ Get: Visible(self: DesignTimeVisibleAttribute) -> bool """
        ...


    def __new__(cls, visible:bool = ...) -> Self:
        """
        __new__(cls: type, visible: bool)
        __new__(cls: type)
        """
        ...

    Default: DesignTimeVisibleAttribute = ...
    No: DesignTimeVisibleAttribute = ...
    Yes: DesignTimeVisibleAttribute = ...


class DisplayNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DisplayNameAttribute()
    DisplayNameAttribute(displayName: str)
    """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: DisplayNameAttribute) -> str """
        ...

    @property
    def DisplayNameValue(self):
        ...


    def __new__(cls, displayName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str)
        """
        ...

    Default: DisplayNameAttribute = ...


class DoubleConverter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ DoubleConverter() """
    pass

class DoWorkEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DoWorkEventArgs(argument: object) """
    @property
    def Argument(self) -> object:
        """ Get: Argument(self: DoWorkEventArgs) -> object """
        ...

    @property
    def Result(self) -> object:
        """
        Get: Result(self: DoWorkEventArgs) -> object
        Set: Result(self: DoWorkEventArgs) = value
        """
        ...



class DoWorkEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DoWorkEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DoWorkEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DoWorkEventHandler, sender: object, e: DoWorkEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DoWorkEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DoWorkEventArgs): # -> 
        """ Invoke(self: DoWorkEventHandler, sender: object, e: DoWorkEventArgs) """
        ...


class EditorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EditorAttribute()
    EditorAttribute(typeName: str, baseTypeName: str)
    EditorAttribute(typeName: str, baseType: Type)
    EditorAttribute(type: Type, baseType: Type)
    """
    @property
    def EditorBaseTypeName(self) -> str:
        """ Get: EditorBaseTypeName(self: EditorAttribute) -> str """
        ...

    @property
    def EditorTypeName(self) -> str:
        """ Get: EditorTypeName(self: EditorAttribute) -> str """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str, baseTypeName: str)
        __new__(cls: type, typeName: str, baseType: Type)
        __new__(cls: type, type: Type, baseType: Type)
        """
        ...


class EditorBrowsableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EditorBrowsableAttribute(state: EditorBrowsableState)
    EditorBrowsableAttribute()
    """
    @property
    def State(self) -> EditorBrowsableState:
        """ Get: State(self: EditorBrowsableAttribute) -> EditorBrowsableState """
        ...


    def __new__(cls, state:EditorBrowsableState = ...) -> Self:
        """
        __new__(cls: type, state: EditorBrowsableState)
        __new__(cls: type)
        """
        ...


class EditorBrowsableState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EditorBrowsableState, values: Advanced (2), Always (0), Never (1) """
    Advanced: EditorBrowsableState = ...
    Always: EditorBrowsableState = ...
    Never: EditorBrowsableState = ...
    value__ = ...


class EnumConverter(TypeConverter): # skipped bases: <type 'object'>
    """ EnumConverter(type: Type) """
    @property
    def Comparer(self):
        ...

    @property
    def EnumType(self):
        ...

    @property
    def Values(self):
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class MemberDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AttributeArray(self):
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: MemberDescriptor) -> AttributeCollection """
        ...

    @property
    def Category(self) -> str:
        """ Get: Category(self: MemberDescriptor) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MemberDescriptor) -> str """
        ...

    @property
    def DesignTimeOnly(self) -> bool:
        """ Get: DesignTimeOnly(self: MemberDescriptor) -> bool """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: MemberDescriptor) -> str """
        ...

    @property
    def IsBrowsable(self) -> bool:
        """ Get: IsBrowsable(self: MemberDescriptor) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberDescriptor) -> str """
        ...

    @property
    def NameHashCode(self):
        ...


    def CreateAttributeCollection(self, *args): #cannot find CLR method
        """ CreateAttributeCollection(self: MemberDescriptor) -> AttributeCollection """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: MemberDescriptor, obj: object) -> bool """
        ...

    def FillAttributes(self, *args): #cannot find CLR method
        """ FillAttributes(self: MemberDescriptor, attributeList: IList) """
        ...

    def FindMethod(self, *args): #cannot find CLR method
        """
        FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type) -> MethodInfo
        FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type, publicOnly: bool) -> MethodInfo
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MemberDescriptor) -> int """
        ...

    def GetInvocationTarget(self, *args): #cannot find CLR method
        """ GetInvocationTarget(self: MemberDescriptor, type: Type, instance: object) -> object """
        ...

    def GetInvokee(self, *args): #cannot find CLR method
        """ GetInvokee(componentClass: Type, component: object) -> object """
        ...

    def GetSite(self, *args): #cannot find CLR method
        """ GetSite(component: object) -> ISite """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EventDescriptor(MemberDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ComponentType(self) -> Type:
        """ Get: ComponentType(self: EventDescriptor) -> Type """
        ...

    @property
    def EventType(self) -> Type:
        """ Get: EventType(self: EventDescriptor) -> Type """
        ...

    @property
    def IsMulticast(self) -> bool:
        """ Get: IsMulticast(self: EventDescriptor) -> bool """
        ...


    def AddEventHandler(self, component:object, value:Delegate): # -> 
        """ AddEventHandler(self: EventDescriptor, component: object, value: Delegate) """
        ...

    def RemoveEventHandler(self, component:object, value:Delegate): # -> 
        """ RemoveEventHandler(self: EventDescriptor, component: object, value: Delegate) """
        ...


class EventDescriptorCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    EventDescriptorCollection(events: Array[EventDescriptor])
    EventDescriptorCollection(events: Array[EventDescriptor], readOnly: bool)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: EventDescriptorCollection) -> int """
        ...


    def Find(self, name:str, ignoreCase:bool) -> EventDescriptor:
        """ Find(self: EventDescriptorCollection, name: str, ignoreCase: bool) -> EventDescriptor """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: EventDescriptorCollection) -> IEnumerator """
        ...

    def InternalSort(self, *args): #cannot find CLR method
        """ InternalSort(self: EventDescriptorCollection, names: Array[str])InternalSort(self: EventDescriptorCollection, sorter: IComparer) """
        ...

    def Sort(self, *__args:Array) -> EventDescriptorCollection:
        """
        Sort(self: EventDescriptorCollection) -> EventDescriptorCollection
        Sort(self: EventDescriptorCollection, names: Array[str]) -> EventDescriptorCollection
        Sort(self: EventDescriptorCollection, names: Array[str], comparer: IComparer) -> EventDescriptorCollection
        Sort(self: EventDescriptorCollection, comparer: IComparer) -> EventDescriptorCollection
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...

    Empty: EventDescriptorCollection = ...


class EventHandlerList(IDisposable): # skipped bases: <type 'object'>
    """ EventHandlerList() """
    def AddHandler(self, key:object, value:Delegate): # -> 
        """ AddHandler(self: EventHandlerList, key: object, value: Delegate) """
        ...

    def AddHandlers(self, listToAddFrom:EventHandlerList): # -> 
        """ AddHandlers(self: EventHandlerList, listToAddFrom: EventHandlerList) """
        ...

    def RemoveHandler(self, key:object, value:Delegate): # -> 
        """ RemoveHandler(self: EventHandlerList, key: object, value: Delegate) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ExpandableObjectConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ExpandableObjectConverter() """
    pass

class ExtenderProvidedPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExtenderProvidedPropertyAttribute() """
    @property
    def ExtenderProperty(self) -> PropertyDescriptor:
        """ Get: ExtenderProperty(self: ExtenderProvidedPropertyAttribute) -> PropertyDescriptor """
        ...

    @property
    def Provider(self) -> IExtenderProvider:
        """ Get: Provider(self: ExtenderProvidedPropertyAttribute) -> IExtenderProvider """
        ...

    @property
    def ReceiverType(self) -> Type:
        """ Get: ReceiverType(self: ExtenderProvidedPropertyAttribute) -> Type """
        ...



class GuidConverter(TypeConverter): # skipped bases: <type 'object'>
    """ GuidConverter() """
    pass

class HandledEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    HandledEventArgs()
    HandledEventArgs(defaultHandledValue: bool)
    """
    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: HandledEventArgs) -> bool
        Set: Handled(self: HandledEventArgs) = value
        """
        ...


    def __new__(cls, defaultHandledValue:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, defaultHandledValue: bool)
        """
        ...


class HandledEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HandledEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:HandledEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HandledEventHandler, sender: object, e: HandledEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: HandledEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:HandledEventArgs): # -> 
        """ Invoke(self: HandledEventHandler, sender: object, e: HandledEventArgs) """
        ...


class IBindingListView(IBindingList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: IBindingListView) -> str
        Set: Filter(self: IBindingListView) = value
        """
        ...

    @property
    def SortDescriptions(self) -> ListSortDescriptionCollection:
        """ Get: SortDescriptions(self: IBindingListView) -> ListSortDescriptionCollection """
        ...

    @property
    def SupportsAdvancedSorting(self) -> bool:
        """ Get: SupportsAdvancedSorting(self: IBindingListView) -> bool """
        ...

    @property
    def SupportsFiltering(self) -> bool:
        """ Get: SupportsFiltering(self: IBindingListView) -> bool """
        ...


    def RemoveFilter(self): # -> 
        """ RemoveFilter(self: IBindingListView) """
        ...


class IChangeTracking: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsChanged(self) -> bool:
        """ Get: IsChanged(self: IChangeTracking) -> bool """
        ...


    def AcceptChanges(self): # -> 
        """ AcceptChanges(self: IChangeTracking) """
        ...


class IComNativeDescriptorHandler: # skipped bases: <type 'object'>
    """ no doc """
    def GetAttributes(self, component:object) -> AttributeCollection:
        """ GetAttributes(self: IComNativeDescriptorHandler, component: object) -> AttributeCollection """
        ...

    def GetClassName(self, component:object) -> str:
        """ GetClassName(self: IComNativeDescriptorHandler, component: object) -> str """
        ...

    def GetConverter(self, component:object) -> TypeConverter:
        """ GetConverter(self: IComNativeDescriptorHandler, component: object) -> TypeConverter """
        ...

    def GetDefaultEvent(self, component:object) -> EventDescriptor:
        """ GetDefaultEvent(self: IComNativeDescriptorHandler, component: object) -> EventDescriptor """
        ...

    def GetDefaultProperty(self, component:object) -> PropertyDescriptor:
        """ GetDefaultProperty(self: IComNativeDescriptorHandler, component: object) -> PropertyDescriptor """
        ...

    def GetEditor(self, component:object, baseEditorType:Type) -> object:
        """ GetEditor(self: IComNativeDescriptorHandler, component: object, baseEditorType: Type) -> object """
        ...

    def GetEvents(self, component:object, attributes:Array = ...) -> EventDescriptorCollection:
        """
        GetEvents(self: IComNativeDescriptorHandler, component: object) -> EventDescriptorCollection
        GetEvents(self: IComNativeDescriptorHandler, component: object, attributes: Array[Attribute]) -> EventDescriptorCollection
        """
        ...

    def GetName(self, component:object) -> str:
        """ GetName(self: IComNativeDescriptorHandler, component: object) -> str """
        ...

    def GetProperties(self, component:object, attributes:Array) -> PropertyDescriptorCollection:
        """ GetProperties(self: IComNativeDescriptorHandler, component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection """
        ...

    def GetPropertyValue(self, component, *__args) -> Tuple_[object, bool]:
        """
        GetPropertyValue(self: IComNativeDescriptorHandler, component: object, propertyName: str, success: bool) -> (object, bool)
        GetPropertyValue(self: IComNativeDescriptorHandler, component: object, dispid: int, success: bool) -> (object, bool)
        """
        ...


class IComponent(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Site(self) -> ISite:
        """
        Get: Site(self: IComponent) -> ISite
        Set: Site(self: IComponent) = value
        """
        ...


    Disposed = ...


class IContainer(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Components(self) -> ComponentCollection:
        """ Get: Components(self: IContainer) -> ComponentCollection """
        ...


    def Add(self, component:IComponent, name:str = ...): # -> 
        """ Add(self: IContainer, component: IComponent)Add(self: IContainer, component: IComponent, name: str) """
        ...

    def Remove(self, component:IComponent): # -> 
        """ Remove(self: IContainer, component: IComponent) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class ICustomTypeDescriptor: # skipped bases: <type 'object'>
    """ no doc """
    def GetAttributes(self) -> AttributeCollection:
        """ GetAttributes(self: ICustomTypeDescriptor) -> AttributeCollection """
        ...

    def GetClassName(self) -> str:
        """ GetClassName(self: ICustomTypeDescriptor) -> str """
        ...

    def GetComponentName(self) -> str:
        """ GetComponentName(self: ICustomTypeDescriptor) -> str """
        ...

    def GetConverter(self) -> TypeConverter:
        """ GetConverter(self: ICustomTypeDescriptor) -> TypeConverter """
        ...

    def GetDefaultEvent(self) -> EventDescriptor:
        """ GetDefaultEvent(self: ICustomTypeDescriptor) -> EventDescriptor """
        ...

    def GetDefaultProperty(self) -> PropertyDescriptor:
        """ GetDefaultProperty(self: ICustomTypeDescriptor) -> PropertyDescriptor """
        ...

    def GetEditor(self, editorBaseType:Type) -> object:
        """ GetEditor(self: ICustomTypeDescriptor, editorBaseType: Type) -> object """
        ...

    def GetEvents(self, attributes:Array = ...) -> EventDescriptorCollection:
        """
        GetEvents(self: ICustomTypeDescriptor) -> EventDescriptorCollection
        GetEvents(self: ICustomTypeDescriptor, attributes: Array[Attribute]) -> EventDescriptorCollection
        """
        ...

    def GetProperties(self, attributes:Array = ...) -> PropertyDescriptorCollection:
        """
        GetProperties(self: ICustomTypeDescriptor) -> PropertyDescriptorCollection
        GetProperties(self: ICustomTypeDescriptor, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        """
        ...

    def GetPropertyOwner(self, pd:PropertyDescriptor) -> object:
        """ GetPropertyOwner(self: ICustomTypeDescriptor, pd: PropertyDescriptor) -> object """
        ...


class IDataErrorInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Error(self) -> str:
        """ Get: Error(self: IDataErrorInfo) -> str """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IEditableObject: # skipped bases: <type 'object'>
    """ no doc """
    def BeginEdit(self): # -> 
        """ BeginEdit(self: IEditableObject) """
        ...

    def CancelEdit(self): # -> 
        """ CancelEdit(self: IEditableObject) """
        ...

    def EndEdit(self): # -> 
        """ EndEdit(self: IEditableObject) """
        ...


class IExtenderProvider: # skipped bases: <type 'object'>
    """ no doc """
    def CanExtend(self, extendee:object) -> bool:
        """ CanExtend(self: IExtenderProvider, extendee: object) -> bool """
        ...


class IIntellisenseBuilder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IIntellisenseBuilder) -> str """
        ...


    def Show(self, language:str, value:str, newValue:str) -> Tuple_[bool, str]:
        """ Show(self: IIntellisenseBuilder, language: str, value: str, newValue: str) -> (bool, str) """
        ...


class IListSource: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContainsListCollection(self) -> bool:
        """ Get: ContainsListCollection(self: IListSource) -> bool """
        ...


    def GetList(self) -> IList:
        """ GetList(self: IListSource) -> IList """
        ...


class ImmutableObjectAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ImmutableObjectAttribute(immutable: bool) """
    @property
    def Immutable(self) -> bool:
        """ Get: Immutable(self: ImmutableObjectAttribute) -> bool """
        ...


    def __new__(cls, immutable:bool) -> Self:
        """ __new__(cls: type, immutable: bool) """
        ...

    Default: ImmutableObjectAttribute = ...
    No: ImmutableObjectAttribute = ...
    Yes: ImmutableObjectAttribute = ...


class INestedContainer(IContainer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Owner(self) -> IComponent:
        """ Get: Owner(self: INestedContainer) -> IComponent """
        ...



class ISite(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Component(self) -> IComponent:
        """ Get: Component(self: ISite) -> IComponent """
        ...

    @property
    def Container(self) -> IContainer:
        """ Get: Container(self: ISite) -> IContainer """
        ...

    @property
    def DesignMode(self) -> bool:
        """ Get: DesignMode(self: ISite) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ISite) -> str
        Set: Name(self: ISite) = value
        """
        ...



class INestedSite(ISite): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ no doc """
    @property
    def FullName(self) -> str:
        """ Get: FullName(self: INestedSite) -> str """
        ...



class InheritanceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InheritanceAttribute()
    InheritanceAttribute(inheritanceLevel: InheritanceLevel)
    """
    @property
    def InheritanceLevel(self) -> InheritanceLevel:
        """ Get: InheritanceLevel(self: InheritanceAttribute) -> InheritanceLevel """
        ...


    def ToString(self) -> str:
        """ ToString(self: InheritanceAttribute) -> str """
        ...

    def __new__(cls, inheritanceLevel:InheritanceLevel = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, inheritanceLevel: InheritanceLevel)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    Default: InheritanceAttribute = ...
    Inherited: InheritanceAttribute = ...
    InheritedReadOnly: InheritanceAttribute = ...
    NotInherited: InheritanceAttribute = ...


class InheritanceLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InheritanceLevel, values: Inherited (1), InheritedReadOnly (2), NotInherited (3) """
    Inherited: InheritanceLevel = ...
    InheritedReadOnly: InheritanceLevel = ...
    NotInherited: InheritanceLevel = ...
    value__ = ...


class InitializationEventAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InitializationEventAttribute(eventName: str) """
    @property
    def EventName(self) -> str:
        """ Get: EventName(self: InitializationEventAttribute) -> str """
        ...


    def __new__(cls, eventName:str) -> Self:
        """ __new__(cls: type, eventName: str) """
        ...


class INotifyDataErrorInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: INotifyDataErrorInfo) -> bool """
        ...


    def GetErrors(self, propertyName:str) -> IEnumerable:
        """ GetErrors(self: INotifyDataErrorInfo, propertyName: str) -> IEnumerable """
        ...

    ErrorsChanged = ...


class INotifyPropertyChanged: # skipped bases: <type 'object'>
    """ no doc """
    PropertyChanged = ...


class INotifyPropertyChanging: # skipped bases: <type 'object'>
    """ no doc """
    PropertyChanging = ...


class InstallerTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InstallerTypeAttribute(installerType: Type)
    InstallerTypeAttribute(typeName: str)
    """
    @property
    def InstallerType(self) -> Type:
        """ Get: InstallerType(self: InstallerTypeAttribute) -> Type """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, installerType: Type)
        __new__(cls: type, typeName: str)
        """
        ...


class InstanceCreationEditor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Text(self) -> str:
        """ Get: Text(self: InstanceCreationEditor) -> str """
        ...


    def CreateInstance(self, context:ITypeDescriptorContext, instanceType:Type) -> object:
        """ CreateInstance(self: InstanceCreationEditor, context: ITypeDescriptorContext, instanceType: Type) -> object """
        ...


class Int16Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ Int16Converter() """
    pass

class Int32Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ Int32Converter() """
    pass

class Int64Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ Int64Converter() """
    pass

class InvalidAsynchronousStateException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidAsynchronousStateException()
    InvalidAsynchronousStateException(message: str)
    InvalidAsynchronousStateException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidEnumArgumentException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidEnumArgumentException()
    InvalidEnumArgumentException(message: str)
    InvalidEnumArgumentException(message: str, innerException: Exception)
    InvalidEnumArgumentException(argumentName: str, invalidValue: int, enumClass: Type)
    """
    SerializeObjectState = ...


class IRevertibleChangeTracking(IChangeTracking): # skipped bases: <type 'object'>
    """ no doc """
    def RejectChanges(self): # -> 
        """ RejectChanges(self: IRevertibleChangeTracking) """
        ...


class ISupportInitialize: # skipped bases: <type 'object'>
    """ no doc """
    def BeginInit(self): # -> 
        """ BeginInit(self: ISupportInitialize) """
        ...

    def EndInit(self): # -> 
        """ EndInit(self: ISupportInitialize) """
        ...


class ISupportInitializeNotification(ISupportInitialize): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsInitialized(self) -> bool:
        """ Get: IsInitialized(self: ISupportInitializeNotification) -> bool """
        ...


    Initialized = ...


class ISynchronizeInvoke: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InvokeRequired(self) -> bool:
        """ Get: InvokeRequired(self: ISynchronizeInvoke) -> bool """
        ...


    def BeginInvoke(self, method:Delegate, args:Array) -> IAsyncResult:
        """ BeginInvoke(self: ISynchronizeInvoke, method: Delegate, args: Array[object]) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: ISynchronizeInvoke, result: IAsyncResult) -> object """
        ...

    def Invoke(self, method:Delegate, args:Array) -> object:
        """ Invoke(self: ISynchronizeInvoke, method: Delegate, args: Array[object]) -> object """
        ...


class ITypeDescriptorContext(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Container(self) -> IContainer:
        """ Get: Container(self: ITypeDescriptorContext) -> IContainer """
        ...

    @property
    def Instance(self) -> object:
        """ Get: Instance(self: ITypeDescriptorContext) -> object """
        ...

    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """ Get: PropertyDescriptor(self: ITypeDescriptorContext) -> PropertyDescriptor """
        ...


    def OnComponentChanged(self): # -> 
        """ OnComponentChanged(self: ITypeDescriptorContext) """
        ...

    def OnComponentChanging(self) -> bool:
        """ OnComponentChanging(self: ITypeDescriptorContext) -> bool """
        ...


class ITypedList: # skipped bases: <type 'object'>
    """ no doc """
    def GetItemProperties(self, listAccessors:Array) -> PropertyDescriptorCollection:
        """ GetItemProperties(self: ITypedList, listAccessors: Array[PropertyDescriptor]) -> PropertyDescriptorCollection """
        ...

    def GetListName(self, listAccessors:Array) -> str:
        """ GetListName(self: ITypedList, listAccessors: Array[PropertyDescriptor]) -> str """
        ...


class License(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LicenseKey(self) -> str:
        """ Get: LicenseKey(self: License) -> str """
        ...



class LicenseContext(IServiceProvider): # skipped bases: <type 'object'>
    """ LicenseContext() """
    @property
    def UsageMode(self) -> LicenseUsageMode:
        """ Get: UsageMode(self: LicenseContext) -> LicenseUsageMode """
        ...


    def GetSavedLicenseKey(self, type:Type, resourceAssembly:Assembly) -> str:
        """ GetSavedLicenseKey(self: LicenseContext, type: Type, resourceAssembly: Assembly) -> str """
        ...

    def SetSavedLicenseKey(self, type:Type, key:str): # -> 
        """ SetSavedLicenseKey(self: LicenseContext, type: Type, key: str) """
        ...


class LicenseException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LicenseException(type: Type)
    LicenseException(type: Type, instance: object)
    LicenseException(type: Type, instance: object, message: str)
    LicenseException(type: Type, instance: object, message: str, innerException: Exception)
    """
    @property
    def LicensedType(self) -> Type:
        """ Get: LicensedType(self: LicenseException) -> Type """
        ...


    SerializeObjectState = ...


class LicenseManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentContext(self) -> LicenseContext:
        """
        Get: CurrentContext() -> LicenseContext
        Set: CurrentContext() = value
        """
        ...

    @property
    def UsageMode(self) -> LicenseUsageMode:
        """ Get: UsageMode() -> LicenseUsageMode """
        ...


    @staticmethod
    def CreateWithContext(type:Type, creationContext:LicenseContext, args:Array = ...) -> object:
        """
        CreateWithContext(type: Type, creationContext: LicenseContext, args: Array[object]) -> object
        CreateWithContext(type: Type, creationContext: LicenseContext) -> object
        """
        ...

    @staticmethod
    def IsLicensed(type:Type) -> bool:
        """ IsLicensed(type: Type) -> bool """
        ...

    @staticmethod
    def IsValid(type, instance=None, license=None) -> bool:
        """
        IsValid(type: Type) -> bool
        IsValid(type: Type, instance: object) -> (bool, License)
        """
        ...

    @staticmethod
    def LockContext(contextUser:object): # -> 
        """ LockContext(contextUser: object) """
        ...

    @staticmethod
    def UnlockContext(contextUser:object): # -> 
        """ UnlockContext(contextUser: object) """
        ...

    @staticmethod
    def Validate(type:Type, instance:object = ...) -> License:
        """ Validate(type: Type)Validate(type: Type, instance: object) -> License """
        ...



class LicenseProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetLicense(self, context:LicenseContext, type:Type, instance:object, allowExceptions:bool) -> License:
        """ GetLicense(self: LicenseProvider, context: LicenseContext, type: Type, instance: object, allowExceptions: bool) -> License """
        ...


class LicenseProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    LicenseProviderAttribute()
    LicenseProviderAttribute(typeName: str)
    LicenseProviderAttribute(type: Type)
    """
    @property
    def LicenseProvider(self) -> Type:
        """ Get: LicenseProvider(self: LicenseProviderAttribute) -> Type """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        ...

    Default: LicenseProviderAttribute = ...


class LicenseUsageMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LicenseUsageMode, values: Designtime (1), Runtime (0) """
    Designtime: LicenseUsageMode = ...
    Runtime: LicenseUsageMode = ...
    value__ = ...


class LicFileLicenseProvider(LicenseProvider): # skipped bases: <type 'object'>
    """ LicFileLicenseProvider() """
    def GetKey(self, *args): #cannot find CLR method
        """ GetKey(self: LicFileLicenseProvider, type: Type) -> str """
        ...

    def IsKeyValid(self, *args): #cannot find CLR method
        """ IsKeyValid(self: LicFileLicenseProvider, key: str, type: Type) -> bool """
        ...


class ListBindableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ListBindableAttribute(listBindable: bool)
    ListBindableAttribute(flags: BindableSupport)
    """
    @property
    def ListBindable(self) -> bool:
        """ Get: ListBindable(self: ListBindableAttribute) -> bool """
        ...


    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type, listBindable: bool)
        __new__(cls: type, flags: BindableSupport)
        """
        ...

    Default: ListBindableAttribute = ...
    No: ListBindableAttribute = ...
    Yes: ListBindableAttribute = ...


class ListChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int)
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor)
    ListChangedEventArgs(listChangedType: ListChangedType, propDesc: PropertyDescriptor)
    ListChangedEventArgs(listChangedType: ListChangedType, newIndex: int, oldIndex: int)
    """
    @property
    def ListChangedType(self) -> ListChangedType:
        """ Get: ListChangedType(self: ListChangedEventArgs) -> ListChangedType """
        ...

    @property
    def NewIndex(self) -> int:
        """ Get: NewIndex(self: ListChangedEventArgs) -> int """
        ...

    @property
    def OldIndex(self) -> int:
        """ Get: OldIndex(self: ListChangedEventArgs) -> int """
        ...

    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """ Get: PropertyDescriptor(self: ListChangedEventArgs) -> PropertyDescriptor """
        ...


    def __new__(cls, listChangedType:ListChangedType, *__args:int) -> Self:
        """
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int)
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int, propDesc: PropertyDescriptor)
        __new__(cls: type, listChangedType: ListChangedType, propDesc: PropertyDescriptor)
        __new__(cls: type, listChangedType: ListChangedType, newIndex: int, oldIndex: int)
        """
        ...


class ListChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ListChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ListChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ListChangedEventHandler, sender: object, e: ListChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ListChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ListChangedEventArgs): # -> 
        """ Invoke(self: ListChangedEventHandler, sender: object, e: ListChangedEventArgs) """
        ...


class ListChangedType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListChangedType, values: ItemAdded (1), ItemChanged (4), ItemDeleted (2), ItemMoved (3), PropertyDescriptorAdded (5), PropertyDescriptorChanged (7), PropertyDescriptorDeleted (6), Reset (0) """
    ItemAdded: ListChangedType = ...
    ItemChanged: ListChangedType = ...
    ItemDeleted: ListChangedType = ...
    ItemMoved: ListChangedType = ...
    PropertyDescriptorAdded: ListChangedType = ...
    PropertyDescriptorChanged: ListChangedType = ...
    PropertyDescriptorDeleted: ListChangedType = ...
    Reset: ListChangedType = ...
    value__ = ...


class ListSortDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ ListSortDescription(property: PropertyDescriptor, direction: ListSortDirection) """
    @property
    def PropertyDescriptor(self) -> PropertyDescriptor:
        """
        Get: PropertyDescriptor(self: ListSortDescription) -> PropertyDescriptor
        Set: PropertyDescriptor(self: ListSortDescription) = value
        """
        ...

    @property
    def SortDirection(self) -> ListSortDirection:
        """
        Get: SortDirection(self: ListSortDescription) -> ListSortDirection
        Set: SortDirection(self: ListSortDescription) = value
        """
        ...



class ListSortDescriptionCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ListSortDescriptionCollection()
    ListSortDescriptionCollection(sorts: Array[ListSortDescription])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ListSortDescriptionCollection) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ListSortDescriptionCollection, array: Array, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class ListSortDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListSortDirection, values: Ascending (0), Descending (1) """
    Ascending: ListSortDirection = ...
    Descending: ListSortDirection = ...
    value__ = ...


class LocalizableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ LocalizableAttribute(isLocalizable: bool) """
    @property
    def IsLocalizable(self) -> bool:
        """ Get: IsLocalizable(self: LocalizableAttribute) -> bool """
        ...


    def __new__(cls, isLocalizable:bool) -> Self:
        """ __new__(cls: type, isLocalizable: bool) """
        ...

    Default: LocalizableAttribute = ...
    No: LocalizableAttribute = ...
    Yes: LocalizableAttribute = ...


class LookupBindingPropertiesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    LookupBindingPropertiesAttribute()
    LookupBindingPropertiesAttribute(dataSource: str, displayMember: str, valueMember: str, lookupMember: str)
    """
    @property
    def DataSource(self) -> str:
        """ Get: DataSource(self: LookupBindingPropertiesAttribute) -> str """
        ...

    @property
    def DisplayMember(self) -> str:
        """ Get: DisplayMember(self: LookupBindingPropertiesAttribute) -> str """
        ...

    @property
    def LookupMember(self) -> str:
        """ Get: LookupMember(self: LookupBindingPropertiesAttribute) -> str """
        ...

    @property
    def ValueMember(self) -> str:
        """ Get: ValueMember(self: LookupBindingPropertiesAttribute) -> str """
        ...


    def __new__(cls, dataSource:str = ..., displayMember:str = ..., valueMember:str = ..., lookupMember:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dataSource: str, displayMember: str, valueMember: str, lookupMember: str)
        """
        ...

    Default: LookupBindingPropertiesAttribute = ...


class MarshalByValueComponent(IServiceProvider, IComponent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ MarshalByValueComponent() """
    @property
    def Container(self) -> IContainer:
        """ Get: Container(self: MarshalByValueComponent) -> IContainer """
        ...

    @property
    def DesignMode(self) -> bool:
        """ Get: DesignMode(self: MarshalByValueComponent) -> bool """
        ...

    @property
    def Events(self):
        ...


    def Dispose(self): # -> 
        """ Dispose(self: MarshalByValueComponent) """
        ...

    def ToString(self) -> str:
        """ ToString(self: MarshalByValueComponent) -> str """
        ...

    Disposed = ...


class MaskedTextProvider(ICloneable): # skipped bases: <type 'object'>
    """
    MaskedTextProvider(mask: str)
    MaskedTextProvider(mask: str, restrictToAscii: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo)
    MaskedTextProvider(mask: str, culture: CultureInfo, restrictToAscii: bool)
    MaskedTextProvider(mask: str, passwordChar: Char, allowPromptAsInput: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo, passwordChar: Char, allowPromptAsInput: bool)
    MaskedTextProvider(mask: str, culture: CultureInfo, allowPromptAsInput: bool, promptChar: Char, passwordChar: Char, restrictToAscii: bool)
    """
    @property
    def AllowPromptAsInput(self) -> bool:
        """ Get: AllowPromptAsInput(self: MaskedTextProvider) -> bool """
        ...

    @property
    def AsciiOnly(self) -> bool:
        """ Get: AsciiOnly(self: MaskedTextProvider) -> bool """
        ...

    @property
    def AssignedEditPositionCount(self) -> int:
        """ Get: AssignedEditPositionCount(self: MaskedTextProvider) -> int """
        ...

    @property
    def AvailableEditPositionCount(self) -> int:
        """ Get: AvailableEditPositionCount(self: MaskedTextProvider) -> int """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: MaskedTextProvider) -> CultureInfo """
        ...

    @property
    def DefaultPasswordChar(self) -> Char:
        """ Get: DefaultPasswordChar() -> Char """
        ...

    @property
    def EditPositionCount(self) -> int:
        """ Get: EditPositionCount(self: MaskedTextProvider) -> int """
        ...

    @property
    def EditPositions(self) -> IEnumerator:
        """ Get: EditPositions(self: MaskedTextProvider) -> IEnumerator """
        ...

    @property
    def IncludeLiterals(self) -> bool:
        """
        Get: IncludeLiterals(self: MaskedTextProvider) -> bool
        Set: IncludeLiterals(self: MaskedTextProvider) = value
        """
        ...

    @property
    def IncludePrompt(self) -> bool:
        """
        Get: IncludePrompt(self: MaskedTextProvider) -> bool
        Set: IncludePrompt(self: MaskedTextProvider) = value
        """
        ...

    @property
    def InvalidIndex(self) -> int:
        """ Get: InvalidIndex() -> int """
        ...

    @property
    def IsPassword(self) -> bool:
        """
        Get: IsPassword(self: MaskedTextProvider) -> bool
        Set: IsPassword(self: MaskedTextProvider) = value
        """
        ...

    @property
    def LastAssignedPosition(self) -> int:
        """ Get: LastAssignedPosition(self: MaskedTextProvider) -> int """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: MaskedTextProvider) -> int """
        ...

    @property
    def Mask(self) -> str:
        """ Get: Mask(self: MaskedTextProvider) -> str """
        ...

    @property
    def MaskCompleted(self) -> bool:
        """ Get: MaskCompleted(self: MaskedTextProvider) -> bool """
        ...

    @property
    def MaskFull(self) -> bool:
        """ Get: MaskFull(self: MaskedTextProvider) -> bool """
        ...

    @property
    def PasswordChar(self) -> Char:
        """
        Get: PasswordChar(self: MaskedTextProvider) -> Char
        Set: PasswordChar(self: MaskedTextProvider) = value
        """
        ...

    @property
    def PromptChar(self) -> Char:
        """
        Get: PromptChar(self: MaskedTextProvider) -> Char
        Set: PromptChar(self: MaskedTextProvider) = value
        """
        ...

    @property
    def ResetOnPrompt(self) -> bool:
        """
        Get: ResetOnPrompt(self: MaskedTextProvider) -> bool
        Set: ResetOnPrompt(self: MaskedTextProvider) = value
        """
        ...

    @property
    def ResetOnSpace(self) -> bool:
        """
        Get: ResetOnSpace(self: MaskedTextProvider) -> bool
        Set: ResetOnSpace(self: MaskedTextProvider) = value
        """
        ...

    @property
    def SkipLiterals(self) -> bool:
        """
        Get: SkipLiterals(self: MaskedTextProvider) -> bool
        Set: SkipLiterals(self: MaskedTextProvider) = value
        """
        ...


    def Add(self, input, testPosition=None, resultHint=None) -> bool:
        """
        Add(self: MaskedTextProvider, input: Char) -> bool
        Add(self: MaskedTextProvider, input: Char) -> (bool, int, MaskedTextResultHint)
        Add(self: MaskedTextProvider, input: str) -> bool
        Add(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def Clear(self, resultHint=None): # -> 
        """ Clear(self: MaskedTextProvider)Clear(self: MaskedTextProvider) -> MaskedTextResultHint """
        ...

    def FindAssignedEditPositionFrom(self, position:int, direction:bool) -> int:
        """ FindAssignedEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int """
        ...

    def FindAssignedEditPositionInRange(self, startPosition:int, endPosition:int, direction:bool) -> int:
        """ FindAssignedEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int """
        ...

    def FindEditPositionFrom(self, position:int, direction:bool) -> int:
        """ FindEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int """
        ...

    def FindEditPositionInRange(self, startPosition:int, endPosition:int, direction:bool) -> int:
        """ FindEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int """
        ...

    def FindNonEditPositionFrom(self, position:int, direction:bool) -> int:
        """ FindNonEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int """
        ...

    def FindNonEditPositionInRange(self, startPosition:int, endPosition:int, direction:bool) -> int:
        """ FindNonEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int """
        ...

    def FindUnassignedEditPositionFrom(self, position:int, direction:bool) -> int:
        """ FindUnassignedEditPositionFrom(self: MaskedTextProvider, position: int, direction: bool) -> int """
        ...

    def FindUnassignedEditPositionInRange(self, startPosition:int, endPosition:int, direction:bool) -> int:
        """ FindUnassignedEditPositionInRange(self: MaskedTextProvider, startPosition: int, endPosition: int, direction: bool) -> int """
        ...

    @staticmethod
    def GetOperationResultFromHint(hint:MaskedTextResultHint) -> bool:
        """ GetOperationResultFromHint(hint: MaskedTextResultHint) -> bool """
        ...

    def InsertAt(self, input, position, testPosition=None, resultHint=None) -> bool:
        """
        InsertAt(self: MaskedTextProvider, input: Char, position: int) -> bool
        InsertAt(self: MaskedTextProvider, input: Char, position: int) -> (bool, int, MaskedTextResultHint)
        InsertAt(self: MaskedTextProvider, input: str, position: int) -> bool
        InsertAt(self: MaskedTextProvider, input: str, position: int) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def IsAvailablePosition(self, position:int) -> bool:
        """ IsAvailablePosition(self: MaskedTextProvider, position: int) -> bool """
        ...

    def IsEditPosition(self, position:int) -> bool:
        """ IsEditPosition(self: MaskedTextProvider, position: int) -> bool """
        ...

    @staticmethod
    def IsValidInputChar(c:Char) -> bool:
        """ IsValidInputChar(c: Char) -> bool """
        ...

    @staticmethod
    def IsValidMaskChar(c:Char) -> bool:
        """ IsValidMaskChar(c: Char) -> bool """
        ...

    @staticmethod
    def IsValidPasswordChar(c:Char) -> bool:
        """ IsValidPasswordChar(c: Char) -> bool """
        ...

    def Remove(self, testPosition=None, resultHint=None) -> bool:
        """
        Remove(self: MaskedTextProvider) -> bool
        Remove(self: MaskedTextProvider) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def RemoveAt(self, *__args:int) -> bool:
        """
        RemoveAt(self: MaskedTextProvider, position: int) -> bool
        RemoveAt(self: MaskedTextProvider, startPosition: int, endPosition: int) -> bool
        RemoveAt(self: MaskedTextProvider, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def Replace(self, input:Char, *__args:int) -> bool:
        """
        Replace(self: MaskedTextProvider, input: Char, position: int) -> bool
        Replace(self: MaskedTextProvider, input: Char, position: int) -> (bool, int, MaskedTextResultHint)
        Replace(self: MaskedTextProvider, input: Char, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        Replace(self: MaskedTextProvider, input: str, position: int) -> bool
        Replace(self: MaskedTextProvider, input: str, position: int) -> (bool, int, MaskedTextResultHint)
        Replace(self: MaskedTextProvider, input: str, startPosition: int, endPosition: int) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def Set(self, input, testPosition=None, resultHint=None) -> bool:
        """
        Set(self: MaskedTextProvider, input: str) -> bool
        Set(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def ToDisplayString(self) -> str:
        """ ToDisplayString(self: MaskedTextProvider) -> str """
        ...

    def ToString(self, *__args:bool) -> str:
        """
        ToString(self: MaskedTextProvider) -> str
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool) -> str
        ToString(self: MaskedTextProvider, startPosition: int, length: int) -> str
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool, startPosition: int, length: int) -> str
        ToString(self: MaskedTextProvider, includePrompt: bool, includeLiterals: bool) -> str
        ToString(self: MaskedTextProvider, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int) -> str
        ToString(self: MaskedTextProvider, ignorePasswordChar: bool, includePrompt: bool, includeLiterals: bool, startPosition: int, length: int) -> str
        """
        ...

    def VerifyChar(self, input, position, hint) -> Tuple_[bool, MaskedTextResultHint]:
        """ VerifyChar(self: MaskedTextProvider, input: Char, position: int) -> (bool, MaskedTextResultHint) """
        ...

    def VerifyEscapeChar(self, input:Char, position:int) -> bool:
        """ VerifyEscapeChar(self: MaskedTextProvider, input: Char, position: int) -> bool """
        ...

    def VerifyString(self, input, testPosition=None, resultHint=None) -> bool:
        """
        VerifyString(self: MaskedTextProvider, input: str) -> bool
        VerifyString(self: MaskedTextProvider, input: str) -> (bool, int, MaskedTextResultHint)
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...



class MaskedTextResultHint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MaskedTextResultHint, values: AlphanumericCharacterExpected (-2), AsciiCharacterExpected (-1), CharacterEscaped (1), DigitExpected (-3), InvalidInput (-51), LetterExpected (-4), NoEffect (2), NonEditPosition (-54), PositionOutOfRange (-55), PromptCharNotAllowed (-52), SideEffect (3), SignedDigitExpected (-5), Success (4), UnavailableEditPosition (-53), Unknown (0) """
    AlphanumericCharacterExpected: MaskedTextResultHint = ...
    AsciiCharacterExpected: MaskedTextResultHint = ...
    CharacterEscaped: MaskedTextResultHint = ...
    DigitExpected: MaskedTextResultHint = ...
    InvalidInput: MaskedTextResultHint = ...
    LetterExpected: MaskedTextResultHint = ...
    NoEffect: MaskedTextResultHint = ...
    NonEditPosition: MaskedTextResultHint = ...
    PositionOutOfRange: MaskedTextResultHint = ...
    PromptCharNotAllowed: MaskedTextResultHint = ...
    SideEffect: MaskedTextResultHint = ...
    SignedDigitExpected: MaskedTextResultHint = ...
    Success: MaskedTextResultHint = ...
    UnavailableEditPosition: MaskedTextResultHint = ...
    Unknown: MaskedTextResultHint = ...
    value__ = ...


class MergablePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MergablePropertyAttribute(allowMerge: bool) """
    @property
    def AllowMerge(self) -> bool:
        """ Get: AllowMerge(self: MergablePropertyAttribute) -> bool """
        ...


    def __new__(cls, allowMerge:bool) -> Self:
        """ __new__(cls: type, allowMerge: bool) """
        ...

    Default: MergablePropertyAttribute = ...
    No: MergablePropertyAttribute = ...
    Yes: MergablePropertyAttribute = ...


class MultilineStringConverter(TypeConverter): # skipped bases: <type 'object'>
    """ MultilineStringConverter() """
    pass

class NestedContainer(INestedContainer, Container): # skipped bases: <type 'IDisposable'>, <type 'IContainer'>, <type 'object'>
    """ NestedContainer(owner: IComponent) """
    @property
    def OwnerName(self):
        ...


    def __new__(cls, owner:IComponent) -> Self:
        """ __new__(cls: type, owner: IComponent) """
        ...


class NotifyParentPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NotifyParentPropertyAttribute(notifyParent: bool) """
    @property
    def NotifyParent(self) -> bool:
        """ Get: NotifyParent(self: NotifyParentPropertyAttribute) -> bool """
        ...


    def __new__(cls, notifyParent:bool) -> Self:
        """ __new__(cls: type, notifyParent: bool) """
        ...

    Default: NotifyParentPropertyAttribute = ...
    No: NotifyParentPropertyAttribute = ...
    Yes: NotifyParentPropertyAttribute = ...


class NullableConverter(TypeConverter): # skipped bases: <type 'object'>
    """ NullableConverter(type: Type) """
    @property
    def NullableType(self) -> Type:
        """ Get: NullableType(self: NullableConverter) -> Type """
        ...

    @property
    def UnderlyingType(self) -> Type:
        """ Get: UnderlyingType(self: NullableConverter) -> Type """
        ...

    @property
    def UnderlyingTypeConverter(self) -> TypeConverter:
        """ Get: UnderlyingTypeConverter(self: NullableConverter) -> TypeConverter """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class ParenthesizePropertyNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ParenthesizePropertyNameAttribute()
    ParenthesizePropertyNameAttribute(needParenthesis: bool)
    """
    @property
    def NeedParenthesis(self) -> bool:
        """ Get: NeedParenthesis(self: ParenthesizePropertyNameAttribute) -> bool """
        ...


    def __new__(cls, needParenthesis:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, needParenthesis: bool)
        """
        ...

    Default: ParenthesizePropertyNameAttribute = ...


class PasswordPropertyTextAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PasswordPropertyTextAttribute()
    PasswordPropertyTextAttribute(password: bool)
    """
    @property
    def Password(self) -> bool:
        """ Get: Password(self: PasswordPropertyTextAttribute) -> bool """
        ...


    def __new__(cls, password:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, password: bool)
        """
        ...

    Default: PasswordPropertyTextAttribute = ...
    No: PasswordPropertyTextAttribute = ...
    Yes: PasswordPropertyTextAttribute = ...


class ProgressChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ProgressChangedEventArgs(progressPercentage: int, userState: object) """
    @property
    def ProgressPercentage(self) -> int:
        """ Get: ProgressPercentage(self: ProgressChangedEventArgs) -> int """
        ...

    @property
    def UserState(self) -> object:
        """ Get: UserState(self: ProgressChangedEventArgs) -> object """
        ...


    def __new__(cls, progressPercentage:int, userState:object) -> Self:
        """ __new__(cls: type, progressPercentage: int, userState: object) """
        ...


class ProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProgressChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ProgressChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProgressChangedEventHandler, sender: object, e: ProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ProgressChangedEventArgs): # -> 
        """ Invoke(self: ProgressChangedEventHandler, sender: object, e: ProgressChangedEventArgs) """
        ...


class PropertyChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PropertyChangedEventArgs(propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PropertyChangedEventArgs) -> str """
        ...


    def __new__(cls, propertyName:str) -> Self:
        """ __new__(cls: type, propertyName: str) """
        ...


class PropertyChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PropertyChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PropertyChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PropertyChangedEventHandler, sender: object, e: PropertyChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PropertyChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PropertyChangedEventArgs): # -> 
        """ Invoke(self: PropertyChangedEventHandler, sender: object, e: PropertyChangedEventArgs) """
        ...


class PropertyChangingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PropertyChangingEventArgs(propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PropertyChangingEventArgs) -> str """
        ...


    def __new__(cls, propertyName:str) -> Self:
        """ __new__(cls: type, propertyName: str) """
        ...


class PropertyChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PropertyChangingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PropertyChangingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PropertyChangingEventHandler, sender: object, e: PropertyChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PropertyChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PropertyChangingEventArgs): # -> 
        """ Invoke(self: PropertyChangingEventHandler, sender: object, e: PropertyChangingEventArgs) """
        ...


class PropertyDescriptor(MemberDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ComponentType(self) -> Type:
        """ Get: ComponentType(self: PropertyDescriptor) -> Type """
        ...

    @property
    def Converter(self) -> TypeConverter:
        """ Get: Converter(self: PropertyDescriptor) -> TypeConverter """
        ...

    @property
    def IsLocalizable(self) -> bool:
        """ Get: IsLocalizable(self: PropertyDescriptor) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: PropertyDescriptor) -> bool """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: PropertyDescriptor) -> Type """
        ...

    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """ Get: SerializationVisibility(self: PropertyDescriptor) -> DesignerSerializationVisibility """
        ...

    @property
    def SupportsChangeEvents(self) -> bool:
        """ Get: SupportsChangeEvents(self: PropertyDescriptor) -> bool """
        ...


    def AddValueChanged(self, component:object, handler:EventHandler): # -> 
        """ AddValueChanged(self: PropertyDescriptor, component: object, handler: EventHandler) """
        ...

    def CanResetValue(self, component:object) -> bool:
        """ CanResetValue(self: PropertyDescriptor, component: object) -> bool """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: PropertyDescriptor, type: Type) -> object """
        ...

    def GetChildProperties(self, *__args:Array) -> PropertyDescriptorCollection:
        """
        GetChildProperties(self: PropertyDescriptor) -> PropertyDescriptorCollection
        GetChildProperties(self: PropertyDescriptor, filter: Array[Attribute]) -> PropertyDescriptorCollection
        GetChildProperties(self: PropertyDescriptor, instance: object) -> PropertyDescriptorCollection
        GetChildProperties(self: PropertyDescriptor, instance: object, filter: Array[Attribute]) -> PropertyDescriptorCollection
        """
        ...

    def GetEditor(self, editorBaseType:Type) -> object:
        """ GetEditor(self: PropertyDescriptor, editorBaseType: Type) -> object """
        ...

    def GetTypeFromName(self, *args): #cannot find CLR method
        """ GetTypeFromName(self: PropertyDescriptor, typeName: str) -> Type """
        ...

    def GetValue(self, component:object) -> object:
        """ GetValue(self: PropertyDescriptor, component: object) -> object """
        ...

    def GetValueChangedHandler(self, *args): #cannot find CLR method
        """ GetValueChangedHandler(self: PropertyDescriptor, component: object) -> EventHandler """
        ...

    def OnValueChanged(self, *args): #cannot find CLR method
        """ OnValueChanged(self: PropertyDescriptor, component: object, e: EventArgs) """
        ...

    def RemoveValueChanged(self, component:object, handler:EventHandler): # -> 
        """ RemoveValueChanged(self: PropertyDescriptor, component: object, handler: EventHandler) """
        ...

    def ResetValue(self, component:object): # -> 
        """ ResetValue(self: PropertyDescriptor, component: object) """
        ...

    def SetValue(self, component:object, value:object): # -> 
        """ SetValue(self: PropertyDescriptor, component: object, value: object) """
        ...

    def ShouldSerializeValue(self, component:object) -> bool:
        """ ShouldSerializeValue(self: PropertyDescriptor, component: object) -> bool """
        ...


class PropertyDescriptorCollection(IDictionary, IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    PropertyDescriptorCollection(properties: Array[PropertyDescriptor])
    PropertyDescriptorCollection(properties: Array[PropertyDescriptor], readOnly: bool)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PropertyDescriptorCollection) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PropertyDescriptorCollection, array: Array, index: int) """
        ...

    def Find(self, name:str, ignoreCase:bool) -> PropertyDescriptor:
        """ Find(self: PropertyDescriptorCollection, name: str, ignoreCase: bool) -> PropertyDescriptor """
        ...

    def InternalSort(self, *args): #cannot find CLR method
        """ InternalSort(self: PropertyDescriptorCollection, names: Array[str])InternalSort(self: PropertyDescriptorCollection, sorter: IComparer) """
        ...

    def Sort(self, *__args:Array) -> PropertyDescriptorCollection:
        """
        Sort(self: PropertyDescriptorCollection) -> PropertyDescriptorCollection
        Sort(self: PropertyDescriptorCollection, names: Array[str]) -> PropertyDescriptorCollection
        Sort(self: PropertyDescriptorCollection, names: Array[str], comparer: IComparer) -> PropertyDescriptorCollection
        Sort(self: PropertyDescriptorCollection, comparer: IComparer) -> PropertyDescriptorCollection
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...

    Empty: PropertyDescriptorCollection = ...


class PropertyTabAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PropertyTabAttribute()
    PropertyTabAttribute(tabClass: Type)
    PropertyTabAttribute(tabClassName: str)
    PropertyTabAttribute(tabClass: Type, tabScope: PropertyTabScope)
    PropertyTabAttribute(tabClassName: str, tabScope: PropertyTabScope)
    """
    @property
    def TabClasses(self) -> Array:
        """ Get: TabClasses(self: PropertyTabAttribute) -> Array[Type] """
        ...

    @property
    def TabClassNames(self):
        ...

    @property
    def TabScopes(self) -> Array:
        """ Get: TabScopes(self: PropertyTabAttribute) -> Array[PropertyTabScope] """
        ...


    def InitializeArrays(self, *args): #cannot find CLR method
        """ InitializeArrays(self: PropertyTabAttribute, tabClassNames: Array[str], tabScopes: Array[PropertyTabScope])InitializeArrays(self: PropertyTabAttribute, tabClasses: Array[Type], tabScopes: Array[PropertyTabScope]) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, tabClass: Type)
        __new__(cls: type, tabClassName: str)
        __new__(cls: type, tabClass: Type, tabScope: PropertyTabScope)
        __new__(cls: type, tabClassName: str, tabScope: PropertyTabScope)
        """
        ...


class PropertyTabScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyTabScope, values: Component (3), Document (2), Global (1), Static (0) """
    Component: PropertyTabScope = ...
    Document: PropertyTabScope = ...
    Global: PropertyTabScope = ...
    Static: PropertyTabScope = ...
    value__ = ...


class ProvidePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ProvidePropertyAttribute(propertyName: str, receiverType: Type)
    ProvidePropertyAttribute(propertyName: str, receiverTypeName: str)
    """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ProvidePropertyAttribute) -> str """
        ...

    @property
    def ReceiverTypeName(self) -> str:
        """ Get: ReceiverTypeName(self: ProvidePropertyAttribute) -> str """
        ...


    def __new__(cls, propertyName:str, *__args:Type) -> Self:
        """
        __new__(cls: type, propertyName: str, receiverType: Type)
        __new__(cls: type, propertyName: str, receiverTypeName: str)
        """
        ...


class ReadOnlyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReadOnlyAttribute(isReadOnly: bool) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ReadOnlyAttribute) -> bool """
        ...


    def __new__(cls, isReadOnly:bool) -> Self:
        """ __new__(cls: type, isReadOnly: bool) """
        ...

    Default: ReadOnlyAttribute = ...
    No: ReadOnlyAttribute = ...
    Yes: ReadOnlyAttribute = ...


class RecommendedAsConfigurableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RecommendedAsConfigurableAttribute(recommendedAsConfigurable: bool) """
    @property
    def RecommendedAsConfigurable(self) -> bool:
        """ Get: RecommendedAsConfigurable(self: RecommendedAsConfigurableAttribute) -> bool """
        ...


    def __new__(cls, recommendedAsConfigurable:bool) -> Self:
        """ __new__(cls: type, recommendedAsConfigurable: bool) """
        ...

    Default: RecommendedAsConfigurableAttribute = ...
    No: RecommendedAsConfigurableAttribute = ...
    Yes: RecommendedAsConfigurableAttribute = ...


class RefreshEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    RefreshEventArgs(componentChanged: object)
    RefreshEventArgs(typeChanged: Type)
    """
    @property
    def ComponentChanged(self) -> object:
        """ Get: ComponentChanged(self: RefreshEventArgs) -> object """
        ...

    @property
    def TypeChanged(self) -> Type:
        """ Get: TypeChanged(self: RefreshEventArgs) -> Type """
        ...


    def __new__(cls, *__args:object) -> Self:
        """
        __new__(cls: type, componentChanged: object)
        __new__(cls: type, typeChanged: Type)
        """
        ...


class RefreshEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RefreshEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, e:RefreshEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RefreshEventHandler, e: RefreshEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RefreshEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, e:RefreshEventArgs): # -> 
        """ Invoke(self: RefreshEventHandler, e: RefreshEventArgs) """
        ...


class RefreshProperties(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RefreshProperties, values: All (1), None (0), Repaint (2) """
    All: RefreshProperties = ...
    Repaint: RefreshProperties = ...
    value__ = ...


class RefreshPropertiesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RefreshPropertiesAttribute(refresh: RefreshProperties) """
    @property
    def RefreshProperties(self) -> RefreshProperties:
        """ Get: RefreshProperties(self: RefreshPropertiesAttribute) -> RefreshProperties """
        ...


    def __new__(cls, refresh:RefreshProperties) -> Self:
        """ __new__(cls: type, refresh: RefreshProperties) """
        ...

    All: RefreshPropertiesAttribute = ...
    Default: RefreshPropertiesAttribute = ...
    Repaint: RefreshPropertiesAttribute = ...


class RunInstallerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RunInstallerAttribute(runInstaller: bool) """
    @property
    def RunInstaller(self) -> bool:
        """ Get: RunInstaller(self: RunInstallerAttribute) -> bool """
        ...


    def __new__(cls, runInstaller:bool) -> Self:
        """ __new__(cls: type, runInstaller: bool) """
        ...

    Default: RunInstallerAttribute = ...
    No: RunInstallerAttribute = ...
    Yes: RunInstallerAttribute = ...


class RunWorkerCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ RunWorkerCompletedEventArgs(result: object, error: Exception, cancelled: bool) """
    @property
    def Result(self) -> object:
        """ Get: Result(self: RunWorkerCompletedEventArgs) -> object """
        ...



class RunWorkerCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RunWorkerCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RunWorkerCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RunWorkerCompletedEventHandler, sender: object, e: RunWorkerCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RunWorkerCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RunWorkerCompletedEventArgs): # -> 
        """ Invoke(self: RunWorkerCompletedEventHandler, sender: object, e: RunWorkerCompletedEventArgs) """
        ...


class SByteConverter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ SByteConverter() """
    pass

class SettingsBindableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsBindableAttribute(bindable: bool) """
    @property
    def Bindable(self) -> bool:
        """ Get: Bindable(self: SettingsBindableAttribute) -> bool """
        ...


    def __new__(cls, bindable:bool) -> Self:
        """ __new__(cls: type, bindable: bool) """
        ...

    No: SettingsBindableAttribute = ...
    Yes: SettingsBindableAttribute = ...


class SingleConverter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ SingleConverter() """
    pass

class StringConverter(TypeConverter): # skipped bases: <type 'object'>
    """ StringConverter() """
    pass

class SyntaxCheck: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckMachineName(value:str) -> bool:
        """ CheckMachineName(value: str) -> bool """
        ...

    @staticmethod
    def CheckPath(value:str) -> bool:
        """ CheckPath(value: str) -> bool """
        ...

    @staticmethod
    def CheckRootedPath(value:str) -> bool:
        """ CheckRootedPath(value: str) -> bool """
        ...

    __all__: list = ...


class TimeSpanConverter(TypeConverter): # skipped bases: <type 'object'>
    """ TimeSpanConverter() """
    pass

class ToolboxItemAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ToolboxItemAttribute(defaultType: bool)
    ToolboxItemAttribute(toolboxItemTypeName: str)
    ToolboxItemAttribute(toolboxItemType: Type)
    """
    @property
    def ToolboxItemType(self) -> Type:
        """ Get: ToolboxItemType(self: ToolboxItemAttribute) -> Type """
        ...

    @property
    def ToolboxItemTypeName(self) -> str:
        """ Get: ToolboxItemTypeName(self: ToolboxItemAttribute) -> str """
        ...


    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type, defaultType: bool)
        __new__(cls: type, toolboxItemTypeName: str)
        __new__(cls: type, toolboxItemType: Type)
        """
        ...

    Default: ToolboxItemAttribute = ...


class ToolboxItemFilterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ToolboxItemFilterAttribute(filterString: str)
    ToolboxItemFilterAttribute(filterString: str, filterType: ToolboxItemFilterType)
    """
    @property
    def FilterString(self) -> str:
        """ Get: FilterString(self: ToolboxItemFilterAttribute) -> str """
        ...

    @property
    def FilterType(self) -> ToolboxItemFilterType:
        """ Get: FilterType(self: ToolboxItemFilterAttribute) -> ToolboxItemFilterType """
        ...


    def ToString(self) -> str:
        """ ToString(self: ToolboxItemFilterAttribute) -> str """
        ...

    def __new__(cls, filterString:str, filterType:ToolboxItemFilterType = ...) -> Self:
        """
        __new__(cls: type, filterString: str)
        __new__(cls: type, filterString: str, filterType: ToolboxItemFilterType)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ToolboxItemFilterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ToolboxItemFilterType, values: Allow (0), Custom (1), Prevent (2), Require (3) """
    Allow: ToolboxItemFilterType = ...
    Custom: ToolboxItemFilterType = ...
    Prevent: ToolboxItemFilterType = ...
    Require: ToolboxItemFilterType = ...
    value__ = ...


class TypeConverterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeConverterAttribute()
    TypeConverterAttribute(type: Type)
    TypeConverterAttribute(typeName: str)
    """
    @property
    def ConverterTypeName(self) -> str:
        """ Get: ConverterTypeName(self: TypeConverterAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        ...

    Default: TypeConverterAttribute = ...


class TypeDescriptionProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateInstance(self, provider:IServiceProvider, objectType:Type, argTypes:Array, args:Array) -> object:
        """ CreateInstance(self: TypeDescriptionProvider, provider: IServiceProvider, objectType: Type, argTypes: Array[Type], args: Array[object]) -> object """
        ...

    def GetCache(self, instance:object) -> IDictionary:
        """ GetCache(self: TypeDescriptionProvider, instance: object) -> IDictionary """
        ...

    def GetExtendedTypeDescriptor(self, instance:object) -> ICustomTypeDescriptor:
        """ GetExtendedTypeDescriptor(self: TypeDescriptionProvider, instance: object) -> ICustomTypeDescriptor """
        ...

    def GetExtenderProviders(self, *args): #cannot find CLR method
        """ GetExtenderProviders(self: TypeDescriptionProvider, instance: object) -> Array[IExtenderProvider] """
        ...

    def GetFullComponentName(self, component:object) -> str:
        """ GetFullComponentName(self: TypeDescriptionProvider, component: object) -> str """
        ...

    def GetReflectionType(self, *__args:Type) -> Type:
        """
        GetReflectionType(self: TypeDescriptionProvider, objectType: Type) -> Type
        GetReflectionType(self: TypeDescriptionProvider, instance: object) -> Type
        GetReflectionType(self: TypeDescriptionProvider, objectType: Type, instance: object) -> Type
        """
        ...

    def GetRuntimeType(self, reflectionType:Type) -> Type:
        """ GetRuntimeType(self: TypeDescriptionProvider, reflectionType: Type) -> Type """
        ...

    def GetTypeDescriptor(self, *__args:Type) -> ICustomTypeDescriptor:
        """
        GetTypeDescriptor(self: TypeDescriptionProvider, objectType: Type, instance: object) -> ICustomTypeDescriptor
        GetTypeDescriptor(self: TypeDescriptionProvider, objectType: Type) -> ICustomTypeDescriptor
        GetTypeDescriptor(self: TypeDescriptionProvider, instance: object) -> ICustomTypeDescriptor
        """
        ...

    def IsSupportedType(self, type:Type) -> bool:
        """ IsSupportedType(self: TypeDescriptionProvider, type: Type) -> bool """
        ...


class TypeDescriptionProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeDescriptionProviderAttribute(typeName: str)
    TypeDescriptionProviderAttribute(type: Type)
    """
    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: TypeDescriptionProviderAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        ...


class TypeDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ComNativeDescriptorHandler(self) -> IComNativeDescriptorHandler:
        """
        Get: ComNativeDescriptorHandler() -> IComNativeDescriptorHandler
        Set: ComNativeDescriptorHandler() = value
        """
        ...

    @property
    def ComObjectType(self) -> Type:
        """ Get: ComObjectType() -> Type """
        ...

    @property
    def InterfaceType(self) -> Type:
        """ Get: InterfaceType() -> Type """
        ...


    @staticmethod
    def AddAttributes(*__args) -> TypeDescriptionProvider:
        """
        AddAttributes(type: Type, *attributes: Array[Attribute]) -> TypeDescriptionProvider
        AddAttributes(instance: object, *attributes: Array[Attribute]) -> TypeDescriptionProvider
        """
        ...

    @staticmethod
    def AddEditorTable(editorBaseType:Type, table:Hashtable): # -> 
        """ AddEditorTable(editorBaseType: Type, table: Hashtable) """
        ...

    @staticmethod
    def AddProvider(provider:TypeDescriptionProvider, *__args:Type): # -> 
        """ AddProvider(provider: TypeDescriptionProvider, type: Type)AddProvider(provider: TypeDescriptionProvider, instance: object) """
        ...

    @staticmethod
    def AddProviderTransparent(provider:TypeDescriptionProvider, *__args:Type): # -> 
        """ AddProviderTransparent(provider: TypeDescriptionProvider, type: Type)AddProviderTransparent(provider: TypeDescriptionProvider, instance: object) """
        ...

    @staticmethod
    def CreateAssociation(primary:object, secondary:object): # -> 
        """ CreateAssociation(primary: object, secondary: object) """
        ...

    @staticmethod
    def CreateDesigner(component:IComponent, designerBaseType:Type) -> IDesigner:
        """ CreateDesigner(component: IComponent, designerBaseType: Type) -> IDesigner """
        ...

    @staticmethod
    def CreateEvent(componentType, *__args) -> EventDescriptor:
        """
        CreateEvent(componentType: Type, name: str, type: Type, *attributes: Array[Attribute]) -> EventDescriptor
        CreateEvent(componentType: Type, oldEventDescriptor: EventDescriptor, *attributes: Array[Attribute]) -> EventDescriptor
        """
        ...

    @staticmethod
    def CreateInstance(provider:IServiceProvider, objectType:Type, argTypes:Array, args:Array) -> object:
        """ CreateInstance(provider: IServiceProvider, objectType: Type, argTypes: Array[Type], args: Array[object]) -> object """
        ...

    @staticmethod
    def CreateProperty(componentType, *__args) -> PropertyDescriptor:
        """
        CreateProperty(componentType: Type, name: str, type: Type, *attributes: Array[Attribute]) -> PropertyDescriptor
        CreateProperty(componentType: Type, oldPropertyDescriptor: PropertyDescriptor, *attributes: Array[Attribute]) -> PropertyDescriptor
        """
        ...

    @staticmethod
    def GetAssociation(type:Type, primary:object) -> object:
        """ GetAssociation(type: Type, primary: object) -> object """
        ...

    @staticmethod
    def GetAttributes(*__args:object) -> AttributeCollection:
        """
        GetAttributes(component: object) -> AttributeCollection
        GetAttributes(componentType: Type) -> AttributeCollection
        GetAttributes(component: object, noCustomTypeDesc: bool) -> AttributeCollection
        """
        ...

    @staticmethod
    def GetClassName(*__args:object) -> str:
        """
        GetClassName(component: object) -> str
        GetClassName(component: object, noCustomTypeDesc: bool) -> str
        GetClassName(componentType: Type) -> str
        """
        ...

    @staticmethod
    def GetComponentName(component:object, noCustomTypeDesc:bool = ...) -> str:
        """
        GetComponentName(component: object) -> str
        GetComponentName(component: object, noCustomTypeDesc: bool) -> str
        """
        ...

    @staticmethod
    def GetConverter(*__args:object) -> TypeConverter:
        """
        GetConverter(component: object) -> TypeConverter
        GetConverter(component: object, noCustomTypeDesc: bool) -> TypeConverter
        GetConverter(type: Type) -> TypeConverter
        """
        ...

    @staticmethod
    def GetDefaultEvent(*__args:object) -> EventDescriptor:
        """
        GetDefaultEvent(component: object) -> EventDescriptor
        GetDefaultEvent(component: object, noCustomTypeDesc: bool) -> EventDescriptor
        GetDefaultEvent(componentType: Type) -> EventDescriptor
        """
        ...

    @staticmethod
    def GetDefaultProperty(*__args:object) -> PropertyDescriptor:
        """
        GetDefaultProperty(component: object) -> PropertyDescriptor
        GetDefaultProperty(component: object, noCustomTypeDesc: bool) -> PropertyDescriptor
        GetDefaultProperty(componentType: Type) -> PropertyDescriptor
        """
        ...

    @staticmethod
    def GetEditor(*__args) -> object:
        """
        GetEditor(component: object, editorBaseType: Type) -> object
        GetEditor(component: object, editorBaseType: Type, noCustomTypeDesc: bool) -> object
        GetEditor(type: Type, editorBaseType: Type) -> object
        """
        ...

    @staticmethod
    def GetEvents(*__args:object) -> EventDescriptorCollection:
        """
        GetEvents(component: object) -> EventDescriptorCollection
        GetEvents(component: object, noCustomTypeDesc: bool) -> EventDescriptorCollection
        GetEvents(component: object, attributes: Array[Attribute]) -> EventDescriptorCollection
        GetEvents(componentType: Type, attributes: Array[Attribute]) -> EventDescriptorCollection
        GetEvents(component: object, attributes: Array[Attribute], noCustomTypeDesc: bool) -> EventDescriptorCollection
        GetEvents(componentType: Type) -> EventDescriptorCollection
        """
        ...

    @staticmethod
    def GetFullComponentName(component:object) -> str:
        """ GetFullComponentName(component: object) -> str """
        ...

    @staticmethod
    def GetProperties(*__args:object) -> PropertyDescriptorCollection:
        """
        GetProperties(component: object) -> PropertyDescriptorCollection
        GetProperties(component: object, noCustomTypeDesc: bool) -> PropertyDescriptorCollection
        GetProperties(component: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        GetProperties(component: object, attributes: Array[Attribute], noCustomTypeDesc: bool) -> PropertyDescriptorCollection
        GetProperties(componentType: Type, attributes: Array[Attribute]) -> PropertyDescriptorCollection
        GetProperties(componentType: Type) -> PropertyDescriptorCollection
        """
        ...

    @staticmethod
    def GetProvider(*__args:Type) -> TypeDescriptionProvider:
        """
        GetProvider(type: Type) -> TypeDescriptionProvider
        GetProvider(instance: object) -> TypeDescriptionProvider
        """
        ...

    @staticmethod
    def GetReflectionType(*__args:Type) -> Type:
        """
        GetReflectionType(type: Type) -> Type
        GetReflectionType(instance: object) -> Type
        """
        ...

    @staticmethod
    def Refresh(*__args:object): # -> 
        """ Refresh(component: object)Refresh(type: Type)Refresh(module: Module)Refresh(assembly: Assembly) """
        ...

    @staticmethod
    def RemoveAssociation(primary:object, secondary:object): # -> 
        """ RemoveAssociation(primary: object, secondary: object) """
        ...

    @staticmethod
    def RemoveAssociations(primary:object): # -> 
        """ RemoveAssociations(primary: object) """
        ...

    @staticmethod
    def RemoveProvider(provider:TypeDescriptionProvider, *__args:Type): # -> 
        """ RemoveProvider(provider: TypeDescriptionProvider, type: Type)RemoveProvider(provider: TypeDescriptionProvider, instance: object) """
        ...

    @staticmethod
    def RemoveProviderTransparent(provider:TypeDescriptionProvider, *__args:Type): # -> 
        """ RemoveProviderTransparent(provider: TypeDescriptionProvider, type: Type)RemoveProviderTransparent(provider: TypeDescriptionProvider, instance: object) """
        ...

    @staticmethod
    def SortDescriptorArray(infos:IList): # -> 
        """ SortDescriptorArray(infos: IList) """
        ...

    Refreshed = ...


class TypeListConverter(TypeConverter): # skipped bases: <type 'object'>
    """ no doc """
    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, types: Array[Type]) """
        ...


class UInt16Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ UInt16Converter() """
    pass

class UInt32Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ UInt32Converter() """
    pass

class UInt64Converter(BaseNumberConverter): # skipped bases: <type 'object'>
    """ UInt64Converter() """
    pass

class WarningException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WarningException()
    WarningException(message: str)
    WarningException(message: str, helpUrl: str)
    WarningException(message: str, innerException: Exception)
    WarningException(message: str, helpUrl: str, helpTopic: str)
    """
    @property
    def HelpTopic(self) -> str:
        """ Get: HelpTopic(self: WarningException) -> str """
        ...

    @property
    def HelpUrl(self) -> str:
        """ Get: HelpUrl(self: WarningException) -> str """
        ...


    SerializeObjectState = ...


class Win32Exception(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    Win32Exception()
    Win32Exception(error: int)
    Win32Exception(error: int, message: str)
    Win32Exception(message: str)
    Win32Exception(message: str, innerException: Exception)
    """
    @property
    def NativeErrorCode(self) -> int:
        """ Get: NativeErrorCode(self: Win32Exception) -> int """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: Win32Exception, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


# variables with complex values

