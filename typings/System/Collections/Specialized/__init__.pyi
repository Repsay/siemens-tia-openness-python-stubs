# encoding: utf-8
# module System.Collections.Specialized calls itself Specialized
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting.Hosting.Configuration import Section

from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    Int16, MulticastDelegate)

from System.Collections import (Hashtable, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList, SortedList)

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    KeysCollection, field#)
"""

# no functions
# classes

class BitVector32: # skipped bases: <type 'object'>, <type 'object'>
    """
    BitVector32(data: int)
    BitVector32(value: BitVector32)
    """
    @property
    def Data(self) -> int:
        """ Get: Data(self: BitVector32) -> int """
        ...


    @staticmethod
    def CreateMask(previous=None) -> int:
        """
        CreateMask() -> int
        CreateMask(previous: int) -> int
        """
        ...

    @staticmethod
    def CreateSection(maxValue:Int16, previous:Section = ...) -> Section:
        """
        CreateSection(maxValue: Int16) -> Section
        CreateSection(maxValue: Int16, previous: Section) -> Section
        """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: BitVector32, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: BitVector32) -> int """
        ...

    def Section(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def ToString(self, value=None) -> str:
        """
        ToString(self: BitVector32) -> str
        ToString(value: BitVector32) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...



class CollectionsUtil: # skipped bases: <type 'object'>, <type 'object'>
    """ CollectionsUtil() """
    @staticmethod
    def CreateCaseInsensitiveHashtable(*__args:int) -> Hashtable:
        """
        CreateCaseInsensitiveHashtable(capacity: int) -> Hashtable
        CreateCaseInsensitiveHashtable() -> Hashtable
        CreateCaseInsensitiveHashtable(d: IDictionary) -> Hashtable
        """
        ...

    @staticmethod
    def CreateCaseInsensitiveSortedList() -> SortedList:
        """ CreateCaseInsensitiveSortedList() -> SortedList """
        ...


class HybridDictionary(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    HybridDictionary()
    HybridDictionary(initialSize: int)
    HybridDictionary(caseInsensitive: bool)
    HybridDictionary(initialSize: int, caseInsensitive: bool)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: HybridDictionary) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: HybridDictionary) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: HybridDictionary) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: HybridDictionary, array: Array, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class INotifyCollectionChanged: # skipped bases: <type 'object'>
    """ no doc """
    CollectionChanged = ...


class IOrderedDictionary(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Insert(self, index:int, key:object, value:object): # -> 
        """ Insert(self: IOrderedDictionary, index: int, key: object, value: object) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IOrderedDictionary, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class ListDictionary(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ListDictionary()
    ListDictionary(comparer: IComparer)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ListDictionary) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: ListDictionary) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: ListDictionary) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ListDictionary, array: Array, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class NameObjectCollectionBase(IDeserializationCallback, ISerializable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self):
        ...

    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: NameObjectCollectionBase) -> KeysCollection """
        ...


    def BaseAdd(self, *args): #cannot find CLR method
        """ BaseAdd(self: NameObjectCollectionBase, name: str, value: object) """
        ...

    def BaseClear(self, *args): #cannot find CLR method
        """ BaseClear(self: NameObjectCollectionBase) """
        ...

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: NameObjectCollectionBase, name: str) -> object
        BaseGet(self: NameObjectCollectionBase, index: int) -> object
        """
        ...

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """ BaseGetAllKeys(self: NameObjectCollectionBase) -> Array[str] """
        ...

    def BaseGetAllValues(self, *args): #cannot find CLR method
        """
        BaseGetAllValues(self: NameObjectCollectionBase) -> Array[object]
        BaseGetAllValues(self: NameObjectCollectionBase, type: Type) -> Array[object]
        """
        ...

    def BaseGetKey(self, *args): #cannot find CLR method
        """ BaseGetKey(self: NameObjectCollectionBase, index: int) -> str """
        ...

    def BaseHasKeys(self, *args): #cannot find CLR method
        """ BaseHasKeys(self: NameObjectCollectionBase) -> bool """
        ...

    def BaseRemove(self, *args): #cannot find CLR method
        """ BaseRemove(self: NameObjectCollectionBase, name: str) """
        ...

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """ BaseRemoveAt(self: NameObjectCollectionBase, index: int) """
        ...

    def BaseSet(self, *args): #cannot find CLR method
        """ BaseSet(self: NameObjectCollectionBase, name: str, value: object)BaseSet(self: NameObjectCollectionBase, index: int, value: object) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: NameObjectCollectionBase) -> IEnumerator """
        ...

    def KeysCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class NameValueCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """
    NameValueCollection()
    NameValueCollection(col: NameValueCollection)
    NameValueCollection(hashProvider: IHashCodeProvider, comparer: IComparer)
    NameValueCollection(capacity: int)
    NameValueCollection(equalityComparer: IEqualityComparer)
    NameValueCollection(capacity: int, equalityComparer: IEqualityComparer)
    NameValueCollection(capacity: int, col: NameValueCollection)
    NameValueCollection(capacity: int, hashProvider: IHashCodeProvider, comparer: IComparer)
    """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: NameValueCollection) -> Array[str] """
        ...


    def Add(self, *__args:NameValueCollection): # -> 
        """ Add(self: NameValueCollection, c: NameValueCollection)Add(self: NameValueCollection, name: str, value: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: NameValueCollection) """
        ...

    def CopyTo(self, dest:Array, index:int): # -> 
        """ CopyTo(self: NameValueCollection, dest: Array, index: int) """
        ...

    def Get(self, *__args:str) -> str:
        """
        Get(self: NameValueCollection, name: str) -> str
        Get(self: NameValueCollection, index: int) -> str
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: NameValueCollection, index: int) -> str """
        ...

    def GetValues(self, *__args:str) -> Array:
        """
        GetValues(self: NameValueCollection, name: str) -> Array[str]
        GetValues(self: NameValueCollection, index: int) -> Array[str]
        """
        ...

    def HasKeys(self) -> bool:
        """ HasKeys(self: NameValueCollection) -> bool """
        ...

    def InvalidateCachedArrays(self, *args): #cannot find CLR method
        """ InvalidateCachedArrays(self: NameValueCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: NameValueCollection, name: str) """
        ...

    def Set(self, name:str, value:str): # -> 
        """ Set(self: NameValueCollection, name: str, value: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class NotifyCollectionChangedAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NotifyCollectionChangedAction, values: Add (0), Move (3), Remove (1), Replace (2), Reset (4) """
    Add: NotifyCollectionChangedAction = ...
    Move: NotifyCollectionChangedAction = ...
    Remove: NotifyCollectionChangedAction = ...
    Replace: NotifyCollectionChangedAction = ...
    Reset: NotifyCollectionChangedAction = ...
    value__ = ...


class NotifyCollectionChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object, index: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItem: object, oldItem: object)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int)
    NotifyCollectionChangedEventArgs(action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int)
    """
    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """ Get: Action(self: NotifyCollectionChangedEventArgs) -> NotifyCollectionChangedAction """
        ...

    @property
    def NewItems(self) -> IList:
        """ Get: NewItems(self: NotifyCollectionChangedEventArgs) -> IList """
        ...

    @property
    def NewStartingIndex(self) -> int:
        """ Get: NewStartingIndex(self: NotifyCollectionChangedEventArgs) -> int """
        ...

    @property
    def OldItems(self) -> IList:
        """ Get: OldItems(self: NotifyCollectionChangedEventArgs) -> IList """
        ...

    @property
    def OldStartingIndex(self) -> int:
        """ Get: OldStartingIndex(self: NotifyCollectionChangedEventArgs) -> int """
        ...


    def __new__(cls, action:NotifyCollectionChangedAction, *__args:object) -> Self:
        """
        __new__(cls: type, action: NotifyCollectionChangedAction)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object, index: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItem: object, oldItem: object)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItem: object, oldItem: object, index: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList)
        __new__(cls: type, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItem: object, index: int, oldIndex: int)
        __new__(cls: type, action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int)
        """
        ...


class NotifyCollectionChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ NotifyCollectionChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:NotifyCollectionChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: NotifyCollectionChangedEventHandler, sender: object, e: NotifyCollectionChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: NotifyCollectionChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:NotifyCollectionChangedEventArgs): # -> 
        """ Invoke(self: NotifyCollectionChangedEventHandler, sender: object, e: NotifyCollectionChangedEventArgs) """
        ...


class OrderedDictionary(IDeserializationCallback, IOrderedDictionary, ISerializable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    OrderedDictionary()
    OrderedDictionary(capacity: int)
    OrderedDictionary(comparer: IEqualityComparer)
    OrderedDictionary(capacity: int, comparer: IEqualityComparer)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: OrderedDictionary) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: OrderedDictionary) -> bool """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: OrderedDictionary) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: OrderedDictionary) -> ICollection """
        ...


    def Add(self, key:object, value:object): # -> 
        """ Add(self: OrderedDictionary, key: object, value: object) """
        ...

    def AsReadOnly(self) -> OrderedDictionary:
        """ AsReadOnly(self: OrderedDictionary) -> OrderedDictionary """
        ...

    def Clear(self): # -> 
        """ Clear(self: OrderedDictionary) """
        ...

    def Contains(self, key:object) -> bool:
        """ Contains(self: OrderedDictionary, key: object) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OrderedDictionary, array: Array, index: int) """
        ...

    def Remove(self, key:object): # -> 
        """ Remove(self: OrderedDictionary, key: object) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class StringCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ StringCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StringCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: StringCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: StringCollection) -> object """
        ...


    def AddRange(self, value:Array): # -> 
        """ AddRange(self: StringCollection, value: Array[str]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: StringCollection, array: Array[str], index: int) """
        ...

    def GetEnumerator(self) -> StringEnumerator:
        """ GetEnumerator(self: StringCollection) -> StringEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class StringDictionary(IEnumerable): # skipped bases: <type 'object'>
    """ StringDictionary() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StringDictionary) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: StringDictionary) -> bool """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: StringDictionary) -> ICollection """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: StringDictionary) -> object """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: StringDictionary) -> ICollection """
        ...


    def Add(self, key:str, value:str): # -> 
        """ Add(self: StringDictionary, key: str, value: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: StringDictionary) """
        ...

    def ContainsKey(self, key:str) -> bool:
        """ ContainsKey(self: StringDictionary, key: str) -> bool """
        ...

    def ContainsValue(self, value:str) -> bool:
        """ ContainsValue(self: StringDictionary, value: str) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: StringDictionary, array: Array, index: int) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: StringDictionary, key: str) """
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


class StringEnumerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> str:
        """ Get: Current(self: StringEnumerator) -> str """
        ...


    def MoveNext(self) -> bool:
        """ MoveNext(self: StringEnumerator) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: StringEnumerator) """
        ...


