# encoding: utf-8
# module System.Collections calls itself Collections
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, ICloneable, Type

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)


# no functions
# classes

class ArrayList(ICloneable, IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ArrayList()
    ArrayList(capacity: int)
    ArrayList(c: ICollection)
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: ArrayList) -> int
        Set: Capacity(self: ArrayList) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ArrayList) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: ArrayList) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: ArrayList) -> object """
        ...


    @staticmethod
    def Adapter(list:IList) -> ArrayList:
        """ Adapter(list: IList) -> ArrayList """
        ...

    def AddRange(self, c:ICollection): # -> 
        """ AddRange(self: ArrayList, c: ICollection) """
        ...

    def BinarySearch(self, *__args:object) -> int:
        """
        BinarySearch(self: ArrayList, index: int, count: int, value: object, comparer: IComparer) -> int
        BinarySearch(self: ArrayList, value: object) -> int
        BinarySearch(self: ArrayList, value: object, comparer: IComparer) -> int
        """
        ...

    def CopyTo(self, *__args:Array): # -> 
        """ CopyTo(self: ArrayList, array: Array)CopyTo(self: ArrayList, array: Array, arrayIndex: int)CopyTo(self: ArrayList, index: int, array: Array, arrayIndex: int, count: int) """
        ...

    @staticmethod
    def FixedSize(list:IList) -> IList:
        """
        FixedSize(list: IList) -> IList
        FixedSize(list: ArrayList) -> ArrayList
        """
        ...

    def GetEnumerator(self, index:int = ..., count:int = ...) -> IEnumerator:
        """
        GetEnumerator(self: ArrayList) -> IEnumerator
        GetEnumerator(self: ArrayList, index: int, count: int) -> IEnumerator
        """
        ...

    def GetRange(self, index:int, count:int) -> ArrayList:
        """ GetRange(self: ArrayList, index: int, count: int) -> ArrayList """
        ...

    def InsertRange(self, index:int, c:ICollection): # -> 
        """ InsertRange(self: ArrayList, index: int, c: ICollection) """
        ...

    def LastIndexOf(self, value:object, startIndex:int = ..., count:int = ...) -> int:
        """
        LastIndexOf(self: ArrayList, value: object) -> int
        LastIndexOf(self: ArrayList, value: object, startIndex: int) -> int
        LastIndexOf(self: ArrayList, value: object, startIndex: int, count: int) -> int
        """
        ...

    @staticmethod
    def ReadOnly(list:IList) -> IList:
        """
        ReadOnly(list: IList) -> IList
        ReadOnly(list: ArrayList) -> ArrayList
        """
        ...

    def RemoveRange(self, index:int, count:int): # -> 
        """ RemoveRange(self: ArrayList, index: int, count: int) """
        ...

    @staticmethod
    def Repeat(value:object, count:int) -> ArrayList:
        """ Repeat(value: object, count: int) -> ArrayList """
        ...

    def Reverse(self, index:int = ..., count:int = ...): # -> 
        """ Reverse(self: ArrayList)Reverse(self: ArrayList, index: int, count: int) """
        ...

    def SetRange(self, index:int, c:ICollection): # -> 
        """ SetRange(self: ArrayList, index: int, c: ICollection) """
        ...

    def Sort(self, *__args:IComparer): # -> 
        """ Sort(self: ArrayList)Sort(self: ArrayList, comparer: IComparer)Sort(self: ArrayList, index: int, count: int, comparer: IComparer) """
        ...

    @staticmethod
    def Synchronized(list:IList) -> IList:
        """
        Synchronized(list: IList) -> IList
        Synchronized(list: ArrayList) -> ArrayList
        """
        ...

    def ToArray(self, type:Type = ...) -> Array:
        """
        ToArray(self: ArrayList) -> Array[object]
        ToArray(self: ArrayList, type: Type) -> Array
        """
        ...

    def TrimToSize(self): # -> 
        """ TrimToSize(self: ArrayList) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class BitArray(ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    BitArray(length: int)
    BitArray(length: int, defaultValue: bool)
    BitArray(bytes: Array[Byte])
    BitArray(values: Array[bool])
    BitArray(values: Array[int])
    BitArray(bits: BitArray)
    """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: BitArray) -> bool """
        ...

    @property
    def Length(self) -> int:
        """
        Get: Length(self: BitArray) -> int
        Set: Length(self: BitArray) = value
        """
        ...


    def And(self, value:BitArray) -> BitArray:
        """ And(self: BitArray, value: BitArray) -> BitArray """
        ...

    def Get(self, index:int) -> bool:
        """ Get(self: BitArray, index: int) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: BitArray) -> IEnumerator """
        ...

    def Not(self) -> BitArray:
        """ Not(self: BitArray) -> BitArray """
        ...

    def Or(self, value:BitArray) -> BitArray:
        """ Or(self: BitArray, value: BitArray) -> BitArray """
        ...

    def Set(self, index:int, value:bool): # -> 
        """ Set(self: BitArray, index: int, value: bool) """
        ...

    def SetAll(self, value:bool): # -> 
        """ SetAll(self: BitArray, value: bool) """
        ...

    def Xor(self, value:BitArray) -> BitArray:
        """ Xor(self: BitArray, value: BitArray) -> BitArray """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CaseInsensitiveComparer(IComparer): # skipped bases: <type 'object'>
    """
    CaseInsensitiveComparer()
    CaseInsensitiveComparer(culture: CultureInfo)
    """
    @property
    def Default(self) -> CaseInsensitiveComparer:
        """ Get: Default() -> CaseInsensitiveComparer """
        ...

    @property
    def DefaultInvariant(self) -> CaseInsensitiveComparer:
        """ Get: DefaultInvariant() -> CaseInsensitiveComparer """
        ...




class CaseInsensitiveHashCodeProvider(IHashCodeProvider): # skipped bases: <type 'object'>
    """
    CaseInsensitiveHashCodeProvider()
    CaseInsensitiveHashCodeProvider(culture: CultureInfo)
    """
    @property
    def Default(self) -> CaseInsensitiveHashCodeProvider:
        """ Get: Default() -> CaseInsensitiveHashCodeProvider """
        ...

    @property
    def DefaultInvariant(self) -> CaseInsensitiveHashCodeProvider:
        """ Get: DefaultInvariant() -> CaseInsensitiveHashCodeProvider """
        ...




class IEnumerable: # skipped bases: <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: IEnumerable) -> IEnumerator """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class ICollection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ICollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: ICollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: ICollection) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ICollection, array: Array, index: int) """
        ...


class IList(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: IList) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IList) -> bool """
        ...


    def Add(self, value:object) -> int:
        """ Add(self: IList, value: object) -> int """
        ...

    def Clear(self): # -> 
        """ Clear(self: IList) """
        ...

    def Contains(self, value:object) -> bool:
        """ Contains(self: IList, value: object) -> bool """
        ...

    def IndexOf(self, value:object) -> int:
        """ IndexOf(self: IList, value: object) -> int """
        ...

    def Insert(self, index:int, value:object): # -> 
        """ Insert(self: IList, index: int, value: object) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: IList, value: object) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IList, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CollectionBase(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: CollectionBase) -> int
        Set: Capacity(self: CollectionBase) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CollectionBase) -> int """
        ...

    @property
    def InnerList(self):
        ...

    @property
    def List(self):
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CollectionBase) -> IEnumerator """
        ...

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: CollectionBase) """
        ...

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: CollectionBase) """
        ...

    def OnInsert(self, *args): #cannot find CLR method
        """ OnInsert(self: CollectionBase, index: int, value: object) """
        ...

    def OnInsertComplete(self, *args): #cannot find CLR method
        """ OnInsertComplete(self: CollectionBase, index: int, value: object) """
        ...

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: CollectionBase, index: int, value: object) """
        ...

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: CollectionBase, index: int, value: object) """
        ...

    def OnSet(self, *args): #cannot find CLR method
        """ OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object) """
        ...

    def OnSetComplete(self, *args): #cannot find CLR method
        """ OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object) """
        ...

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: CollectionBase, value: object) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class Comparer(IComparer, ISerializable): # skipped bases: <type 'object'>
    """ Comparer(culture: CultureInfo) """
    Default: Comparer = ...
    DefaultInvariant: Comparer = ...


class IDictionary(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: IDictionary) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IDictionary) -> bool """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: IDictionary) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: IDictionary) -> ICollection """
        ...


    def Add(self, key:object, value:object): # -> 
        """ Add(self: IDictionary, key: object, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IDictionary) """
        ...

    def Contains(self, key:object) -> bool:
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...

    def GetEnumerator(self) -> IDictionaryEnumerator:
        """ GetEnumerator(self: IDictionary) -> IDictionaryEnumerator """
        ...

    def Remove(self, key:object): # -> 
        """ Remove(self: IDictionary, key: object) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DictionaryBase(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DictionaryBase) -> int """
        ...

    @property
    def Dictionary(self):
        ...

    @property
    def InnerHashtable(self):
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DictionaryBase, array: Array, index: int) """
        ...

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: DictionaryBase) """
        ...

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: DictionaryBase) """
        ...

    def OnGet(self, *args): #cannot find CLR method
        """ OnGet(self: DictionaryBase, key: object, currentValue: object) -> object """
        ...

    def OnInsert(self, *args): #cannot find CLR method
        """ OnInsert(self: DictionaryBase, key: object, value: object) """
        ...

    def OnInsertComplete(self, *args): #cannot find CLR method
        """ OnInsertComplete(self: DictionaryBase, key: object, value: object) """
        ...

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: DictionaryBase, key: object, value: object) """
        ...

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: DictionaryBase, key: object, value: object) """
        ...

    def OnSet(self, *args): #cannot find CLR method
        """ OnSet(self: DictionaryBase, key: object, oldValue: object, newValue: object) """
        ...

    def OnSetComplete(self, *args): #cannot find CLR method
        """ OnSetComplete(self: DictionaryBase, key: object, oldValue: object, newValue: object) """
        ...

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: DictionaryBase, key: object, value: object) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class DictionaryEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ DictionaryEntry(key: object, value: object) """
    @property
    def Key(self) -> object:
        """
        Get: Key(self: DictionaryEntry) -> object
        Set: Key(self: DictionaryEntry) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: DictionaryEntry) -> object
        Set: Value(self: DictionaryEntry) = value
        """
        ...



class Hashtable(IDictionary, ICloneable, IDeserializationCallback, ISerializable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    Hashtable()
    Hashtable(capacity: int)
    Hashtable(capacity: int, loadFactor: Single)
    Hashtable(capacity: int, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, loadFactor: Single, equalityComparer: IEqualityComparer)
    Hashtable(hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(equalityComparer: IEqualityComparer)
    Hashtable(capacity: int, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(capacity: int, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary)
    Hashtable(d: IDictionary, loadFactor: Single)
    Hashtable(d: IDictionary, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, equalityComparer: IEqualityComparer)
    Hashtable(d: IDictionary, loadFactor: Single, hcp: IHashCodeProvider, comparer: IComparer)
    Hashtable(d: IDictionary, loadFactor: Single, equalityComparer: IEqualityComparer)
    """
    @property
    def comparer(self):
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Hashtable) -> int """
        ...

    @property
    def EqualityComparer(self):
        ...

    @property
    def hcp(self):
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: Hashtable) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: Hashtable) -> object """
        ...


    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: Hashtable, key: object) -> bool """
        ...

    def ContainsValue(self, value:object) -> bool:
        """ ContainsValue(self: Hashtable, value: object) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: Hashtable, array: Array, arrayIndex: int) """
        ...

    def GetHash(self, *args): #cannot find CLR method
        """ GetHash(self: Hashtable, key: object) -> int """
        ...

    def KeyEquals(self, *args): #cannot find CLR method
        """ KeyEquals(self: Hashtable, item: object, key: object) -> bool """
        ...

    @staticmethod
    def Synchronized(table:Hashtable) -> Hashtable:
        """ Synchronized(table: Hashtable) -> Hashtable """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class IComparer: # skipped bases: <type 'object'>
    """ no doc """
    def Compare(self, x:object, y:object) -> int:
        """ Compare(self: IComparer, x: object, y: object) -> int """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...


class IEnumerator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Current(self) -> object:
        """ Get: Current(self: IEnumerator) -> object """
        ...


    def MoveNext(self) -> bool:
        """ MoveNext(self: IEnumerator) -> bool """
        ...

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        ...

    def Reset(self): # -> 
        """ Reset(self: IEnumerator) """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        ...


class IDictionaryEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Entry(self) -> DictionaryEntry:
        """ Get: Entry(self: IDictionaryEnumerator) -> DictionaryEntry """
        ...

    @property
    def Key(self) -> object:
        """ Get: Key(self: IDictionaryEnumerator) -> object """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: IDictionaryEnumerator) -> object """
        ...



class IEqualityComparer: # skipped bases: <type 'object'>
    """ no doc """
    def Equals(self, x:object, y:object) -> bool:
        """ Equals(self: IEqualityComparer, x: object, y: object) -> bool """
        ...

    def GetHashCode(self, obj:object) -> int:
        """ GetHashCode(self: IEqualityComparer, obj: object) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class IHashCodeProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetHashCode(self, obj:object) -> int:
        """ GetHashCode(self: IHashCodeProvider, obj: object) -> int """
        ...


class IStructuralComparable: # skipped bases: <type 'object'>
    """ no doc """
    def CompareTo(self, other:object, comparer:IComparer) -> int:
        """ CompareTo(self: IStructuralComparable, other: object, comparer: IComparer) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IStructuralEquatable: # skipped bases: <type 'object'>
    """ no doc """
    def Equals(self, other:object, comparer:IEqualityComparer) -> bool:
        """ Equals(self: IStructuralEquatable, other: object, comparer: IEqualityComparer) -> bool """
        ...

    def GetHashCode(self, comparer:IEqualityComparer) -> int:
        """ GetHashCode(self: IStructuralEquatable, comparer: IEqualityComparer) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Queue(ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    Queue()
    Queue(capacity: int)
    Queue(capacity: int, growFactor: Single)
    Queue(col: ICollection)
    """
    def Clear(self): # -> 
        """ Clear(self: Queue) """
        ...

    def Contains(self, obj:object) -> bool:
        """ Contains(self: Queue, obj: object) -> bool """
        ...

    def Dequeue(self) -> object:
        """ Dequeue(self: Queue) -> object """
        ...

    def Enqueue(self, obj:object): # -> 
        """ Enqueue(self: Queue, obj: object) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Queue) -> IEnumerator """
        ...

    def Peek(self) -> object:
        """ Peek(self: Queue) -> object """
        ...

    @staticmethod
    def Synchronized(queue:Queue) -> Queue:
        """ Synchronized(queue: Queue) -> Queue """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: Queue) -> Array[object] """
        ...

    def TrimToSize(self): # -> 
        """ TrimToSize(self: Queue) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ReadOnlyCollectionBase(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def InnerList(self):
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReadOnlyCollectionBase) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SortedList(IDictionary, ICloneable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SortedList()
    SortedList(initialCapacity: int)
    SortedList(comparer: IComparer)
    SortedList(comparer: IComparer, capacity: int)
    SortedList(d: IDictionary)
    SortedList(d: IDictionary, comparer: IComparer)
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: SortedList) -> int
        Set: Capacity(self: SortedList) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SortedList) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: SortedList) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: SortedList) -> object """
        ...


    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: SortedList, key: object) -> bool """
        ...

    def ContainsValue(self, value:object) -> bool:
        """ ContainsValue(self: SortedList, value: object) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: SortedList, array: Array, arrayIndex: int) """
        ...

    def GetByIndex(self, index:int) -> object:
        """ GetByIndex(self: SortedList, index: int) -> object """
        ...

    def GetKey(self, index:int) -> object:
        """ GetKey(self: SortedList, index: int) -> object """
        ...

    def GetKeyList(self) -> IList:
        """ GetKeyList(self: SortedList) -> IList """
        ...

    def GetValueList(self) -> IList:
        """ GetValueList(self: SortedList) -> IList """
        ...

    def IndexOfKey(self, key:object) -> int:
        """ IndexOfKey(self: SortedList, key: object) -> int """
        ...

    def IndexOfValue(self, value:object) -> int:
        """ IndexOfValue(self: SortedList, value: object) -> int """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SortedList, index: int) """
        ...

    def SetByIndex(self, index:int, value:object): # -> 
        """ SetByIndex(self: SortedList, index: int, value: object) """
        ...

    @staticmethod
    def Synchronized(list:SortedList) -> SortedList:
        """ Synchronized(list: SortedList) -> SortedList """
        ...

    def TrimToSize(self): # -> 
        """ TrimToSize(self: SortedList) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class Stack(ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    Stack()
    Stack(initialCapacity: int)
    Stack(col: ICollection)
    """
    def Clear(self): # -> 
        """ Clear(self: Stack) """
        ...

    def Contains(self, obj:object) -> bool:
        """ Contains(self: Stack, obj: object) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Stack) -> IEnumerator """
        ...

    def Peek(self) -> object:
        """ Peek(self: Stack) -> object """
        ...

    def Pop(self) -> object:
        """ Pop(self: Stack) -> object """
        ...

    def Push(self, obj:object): # -> 
        """ Push(self: Stack, obj: object) """
        ...

    @staticmethod
    def Synchronized(stack:Stack) -> Stack:
        """ Synchronized(stack: Stack) -> Stack """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: Stack) -> Array[object] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class StructuralComparisons: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def StructuralComparer(self) -> IComparer:
        """ Get: StructuralComparer() -> IComparer """
        ...

    @property
    def StructuralEqualityComparer(self) -> IEqualityComparer:
        """ Get: StructuralEqualityComparer() -> IEqualityComparer """
        ...


    __all__: list = ...


# variables with complex values

