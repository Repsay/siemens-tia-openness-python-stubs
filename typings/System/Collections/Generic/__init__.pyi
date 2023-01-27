# encoding: utf-8
# module System.Collections.Generic calls itself Generic
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import Enumerator

from Microsoft.VisualBasic import Collection

from System import (Action, Array, Comparison, Converter, IDisposable, 
    Predicate, SystemException)

from System.Collections.ObjectModel import (KeyedCollection, 
    ReadOnlyCollection)

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, T, TKey, 
    TValue)
"""

# no functions
# classes

class Comparer(IComparer): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Default(self) -> Comparer:
        """ Get: Default() -> Comparer[T] """
        ...


    @staticmethod
    def Create(comparison:Comparison) -> Comparer:
        """ Create(comparison: Comparison[T]) -> Comparer[T] """
        ...


class Dictionary(IDictionary, IReadOnlyDictionary, IDeserializationCallback, ISerializable): # skipped bases: <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'object'>
    """
    Dictionary[TKey, TValue]()
    Dictionary[TKey, TValue](capacity: int)
    Dictionary[TKey, TValue](comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](capacity: int, comparer: IEqualityComparer[TKey])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    Dictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey])
    """
    @property
    def Comparer(self) -> IEqualityComparer:
        """ Get: Comparer(self: Dictionary[TKey, TValue]) -> IEqualityComparer[TKey] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Dictionary[TKey, TValue]) -> int """
        ...


    def ContainsValue(self, value) -> bool: # Not found arg types: {'value': 'TValue'}
        """ ContainsValue(self: Dictionary[TKey, TValue], value: TValue) -> bool """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def KeyCollection(self, *args): #cannot find CLR method
        """ KeyCollection(dictionary: Dictionary[TKey, TValue]) """
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        """ ValueCollection(dictionary: Dictionary[TKey, TValue]) """
        ...



class EqualityComparer(IEqualityComparer): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Default(self) -> EqualityComparer:
        """ Get: Default() -> EqualityComparer[T] """
        ...



class HashSet(IReadOnlyCollection, IDeserializationCallback, ISet, ISerializable): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'object'>
    """
    HashSet[T]()
    HashSet[T](capacity: int)
    HashSet[T](comparer: IEqualityComparer[T])
    HashSet[T](collection: IEnumerable[T])
    HashSet[T](collection: IEnumerable[T], comparer: IEqualityComparer[T])
    HashSet[T](capacity: int, comparer: IEqualityComparer[T])
    """
    @property
    def Comparer(self) -> IEqualityComparer:
        """ Get: Comparer(self: HashSet[T]) -> IEqualityComparer[T] """
        ...


    def Clear(self): # -> 
        """ Clear(self: HashSet[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: HashSet[T], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int = ..., count:int = ...): # -> 
        """ CopyTo(self: HashSet[T], array: Array[T], arrayIndex: int)CopyTo(self: HashSet[T], array: Array[T])CopyTo(self: HashSet[T], array: Array[T], arrayIndex: int, count: int) """
        ...

    @staticmethod
    def CreateSetComparer() -> IEqualityComparer:
        """ CreateSetComparer() -> IEqualityComparer[HashSet[T]] """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: HashSet[T]) -> Enumerator """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Remove(self: HashSet[T], item: T) -> bool """
        ...

    def RemoveWhere(self, match:Predicate) -> int:
        """ RemoveWhere(self: HashSet[T], match: Predicate[T]) -> int """
        ...

    def TrimExcess(self): # -> 
        """ TrimExcess(self: HashSet[T]) """
        ...

    def TryGetValue(self, equalValue, actualValue): # -> Tuple_[bool, T]
        """ TryGetValue(self: HashSet[T], equalValue: T) -> (bool, T) """
        ...



class ICollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ICollection[T]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ICollection[T]) -> bool """
        ...


    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: ICollection[T], item: T) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ICollection[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: ICollection[T], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ICollection[T], array: Array[T], arrayIndex: int) """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Remove(self: ICollection[T], item: T) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...


class IComparer: # skipped bases: <type 'object'>
    """ no doc """
    def Compare(self, x, y) -> int: # Not found arg types: {'y': 'T', 'x': 'T'}
        """ Compare(self: IComparer[T], x: T, y: T) -> int """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...


class IDictionary(ICollection): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: IDictionary[TKey, TValue]) -> ICollection[TKey] """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: IDictionary[TKey, TValue]) -> ICollection[TValue] """
        ...


    def ContainsKey(self, key) -> bool: # Not found arg types: {'key': 'TKey'}
        """ ContainsKey(self: IDictionary[TKey, TValue], key: TKey) -> bool """
        ...

    def TryGetValue(self, key, value): # -> Tuple_[bool, TValue]
        """ TryGetValue(self: IDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
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


class IEnumerable(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IEnumerator(IDisposable, IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IEqualityComparer: # skipped bases: <type 'object'>
    """ no doc """
    def Equals(self, x, y) -> bool: # Not found arg types: {'y': 'T', 'x': 'T'}
        """ Equals(self: IEqualityComparer[T], x: T, y: T) -> bool """
        ...

    def GetHashCode(self, obj) -> int: # Not found arg types: {'obj': 'T'}
        """ GetHashCode(self: IEqualityComparer[T], obj: T) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class IList(ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def IndexOf(self, item) -> int: # Not found arg types: {'item': 'T'}
        """ IndexOf(self: IList[T], item: T) -> int """
        ...

    def Insert(self, index:int, item): # ->  # Not found arg types: {'item': 'T'}
        """ Insert(self: IList[T], index: int, item: T) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IList[T], index: int) """
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


class IReadOnlyCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IReadOnlyCollection[T]) -> int """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...


class IReadOnlyDictionary(IReadOnlyCollection): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Keys(self) -> IEnumerable:
        """ Get: Keys(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TKey] """
        ...

    @property
    def Values(self) -> IEnumerable:
        """ Get: Values(self: IReadOnlyDictionary[TKey, TValue]) -> IEnumerable[TValue] """
        ...


    def ContainsKey(self, key) -> bool: # Not found arg types: {'key': 'TKey'}
        """ ContainsKey(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> bool """
        ...

    def TryGetValue(self, key, value): # -> Tuple_[bool, TValue]
        """ TryGetValue(self: IReadOnlyDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IReadOnlyList(IReadOnlyCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ISet(ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def ExceptWith(self, other:IEnumerable): # -> 
        """ ExceptWith(self: ISet[T], other: IEnumerable[T]) """
        ...

    def IntersectWith(self, other:IEnumerable): # -> 
        """ IntersectWith(self: ISet[T], other: IEnumerable[T]) """
        ...

    def IsProperSubsetOf(self, other:IEnumerable) -> bool:
        """ IsProperSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def IsProperSupersetOf(self, other:IEnumerable) -> bool:
        """ IsProperSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def IsSubsetOf(self, other:IEnumerable) -> bool:
        """ IsSubsetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def IsSupersetOf(self, other:IEnumerable) -> bool:
        """ IsSupersetOf(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def Overlaps(self, other:IEnumerable) -> bool:
        """ Overlaps(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def SetEquals(self, other:IEnumerable) -> bool:
        """ SetEquals(self: ISet[T], other: IEnumerable[T]) -> bool """
        ...

    def SymmetricExceptWith(self, other:IEnumerable): # -> 
        """ SymmetricExceptWith(self: ISet[T], other: IEnumerable[T]) """
        ...

    def UnionWith(self, other:IEnumerable): # -> 
        """ UnionWith(self: ISet[T], other: IEnumerable[T]) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class KeyedByTypeCollection(KeyedCollection): # skipped bases: <type 'ICollection[TItem]'>, <type 'IReadOnlyCollection[TItem]'>, <type 'IEnumerable'>, <type 'IEnumerable[TItem]'>, <type 'IReadOnlyList[TItem]'>, <type 'IList'>, <type 'IList[TItem]'>, <type 'ICollection'>, <type 'object'>
    """
    KeyedByTypeCollection[TItem]()
    KeyedByTypeCollection[TItem](items: IEnumerable[TItem])
    """
    def Find(self): # -> T
        """ Find[T](self: KeyedByTypeCollection[TItem]) -> T """
        ...

    def FindAll(self) -> Collection:
        """ FindAll[T](self: KeyedByTypeCollection[TItem]) -> Collection[T] """
        ...

    def RemoveAll(self) -> Collection:
        """ RemoveAll[T](self: KeyedByTypeCollection[TItem]) -> Collection[T] """
        ...


class KeyNotFoundException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    KeyNotFoundException()
    KeyNotFoundException(message: str)
    KeyNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class KeyValuePair: # skipped bases: <type 'object'>, <type 'object'>
    """ KeyValuePair[TKey, TValue](key: TKey, value: TValue) """
    @property
    def Key(self): # -> TKey
        """ Get: Key(self: KeyValuePair[TKey, TValue]) -> TKey """
        ...

    @property
    def Value(self): # -> TValue
        """ Get: Value(self: KeyValuePair[TKey, TValue]) -> TValue """
        ...


    def ToString(self) -> str:
        """ ToString(self: KeyValuePair[TKey, TValue]) -> str """
        ...


class LinkedList(IReadOnlyCollection, IDeserializationCallback, ISerializable, ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """
    LinkedList[T]()
    LinkedList[T](collection: IEnumerable[T])
    """
    @property
    def First(self) -> LinkedListNode:
        """ Get: First(self: LinkedList[T]) -> LinkedListNode[T] """
        ...

    @property
    def Last(self) -> LinkedListNode:
        """ Get: Last(self: LinkedList[T]) -> LinkedListNode[T] """
        ...


    def AddAfter(self, node:LinkedListNode, *__args:LinkedListNode): # -> 
        """ AddAfter(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])AddAfter(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T] """
        ...

    def AddBefore(self, node:LinkedListNode, *__args) -> LinkedListNode: # Not found arg types: {'*__args': 'T'}
        """
        AddBefore(self: LinkedList[T], node: LinkedListNode[T], value: T) -> LinkedListNode[T]
        AddBefore(self: LinkedList[T], node: LinkedListNode[T], newNode: LinkedListNode[T])
        """
        ...

    def AddFirst(self, *__args) -> LinkedListNode: # Not found arg types: {'*__args': 'T'}
        """
        AddFirst(self: LinkedList[T], value: T) -> LinkedListNode[T]
        AddFirst(self: LinkedList[T], node: LinkedListNode[T])
        """
        ...

    def AddLast(self, *__args) -> LinkedListNode: # Not found arg types: {'*__args': 'T'}
        """
        AddLast(self: LinkedList[T], value: T) -> LinkedListNode[T]
        AddLast(self: LinkedList[T], node: LinkedListNode[T])
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, value) -> LinkedListNode: # Not found arg types: {'value': 'T'}
        """ Find(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        ...

    def FindLast(self, value) -> LinkedListNode: # Not found arg types: {'value': 'T'}
        """ FindLast(self: LinkedList[T], value: T) -> LinkedListNode[T] """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: LinkedList[T]) -> Enumerator """
        ...

    def RemoveFirst(self): # -> 
        """ RemoveFirst(self: LinkedList[T]) """
        ...

    def RemoveLast(self): # -> 
        """ RemoveLast(self: LinkedList[T]) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class LinkedListNode: # skipped bases: <type 'object'>, <type 'object'>
    """ LinkedListNode[T](value: T) """
    @property
    def List(self) -> LinkedList:
        """ Get: List(self: LinkedListNode[T]) -> LinkedList[T] """
        ...

    @property
    def Next(self) -> LinkedListNode:
        """ Get: Next(self: LinkedListNode[T]) -> LinkedListNode[T] """
        ...

    @property
    def Previous(self) -> LinkedListNode:
        """ Get: Previous(self: LinkedListNode[T]) -> LinkedListNode[T] """
        ...

    @property
    def Value(self): # -> T
        """
        Get: Value(self: LinkedListNode[T]) -> T
        Set: Value(self: LinkedListNode[T]) = value
        """
        ...



class List(IReadOnlyList, IList): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ICollection[T]'>, <type 'object'>
    """
    List[T]()
    List[T](capacity: int)
    List[T](collection: IEnumerable[T])
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: List[T]) -> int
        Set: Capacity(self: List[T]) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: List[T]) -> int """
        ...


    def AddRange(self, collection:IEnumerable): # -> 
        """ AddRange(self: List[T], collection: IEnumerable[T]) """
        ...

    def AsReadOnly(self) -> ReadOnlyCollection:
        """ AsReadOnly(self: List[T]) -> ReadOnlyCollection[T] """
        ...

    def BinarySearch(self, *__args) -> int: # Not found arg types: {'*__args': 'T'}
        """
        BinarySearch(self: List[T], index: int, count: int, item: T, comparer: IComparer[T]) -> int
        BinarySearch(self: List[T], item: T) -> int
        BinarySearch(self: List[T], item: T, comparer: IComparer[T]) -> int
        """
        ...

    def ConvertAll(self, converter:Converter) -> List:
        """ ConvertAll[TOutput](self: List[T], converter: Converter[T, TOutput]) -> List[TOutput] """
        ...

    def CopyTo(self, *__args:Array): # -> 
        """ CopyTo(self: List[T], index: int, array: Array[T], arrayIndex: int, count: int)CopyTo(self: List[T], array: Array[T])CopyTo(self: List[T], array: Array[T], arrayIndex: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Exists(self, match:Predicate) -> bool:
        """ Exists(self: List[T], match: Predicate[T]) -> bool """
        ...

    def Find(self, match:Predicate): # -> T
        """ Find(self: List[T], match: Predicate[T]) -> T """
        ...

    def FindAll(self, match:Predicate) -> List:
        """ FindAll(self: List[T], match: Predicate[T]) -> List[T] """
        ...

    def FindIndex(self, *__args:Predicate) -> int:
        """
        FindIndex(self: List[T], match: Predicate[T]) -> int
        FindIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        FindIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        """
        ...

    def FindLast(self, match:Predicate): # -> T
        """ FindLast(self: List[T], match: Predicate[T]) -> T """
        ...

    def FindLastIndex(self, *__args:Predicate) -> int:
        """
        FindLastIndex(self: List[T], match: Predicate[T]) -> int
        FindLastIndex(self: List[T], startIndex: int, match: Predicate[T]) -> int
        FindLastIndex(self: List[T], startIndex: int, count: int, match: Predicate[T]) -> int
        """
        ...

    def ForEach(self, action:Action): # -> 
        """ ForEach(self: List[T], action: Action[T]) """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: List[T]) -> Enumerator """
        ...

    def GetRange(self, index:int, count:int) -> List:
        """ GetRange(self: List[T], index: int, count: int) -> List[T] """
        ...

    def InsertRange(self, index:int, collection:IEnumerable): # -> 
        """ InsertRange(self: List[T], index: int, collection: IEnumerable[T]) """
        ...

    def LastIndexOf(self, item, index:int = ..., count:int = ...) -> int: # Not found arg types: {'item': 'T'}
        """
        LastIndexOf(self: List[T], item: T) -> int
        LastIndexOf(self: List[T], item: T, index: int) -> int
        LastIndexOf(self: List[T], item: T, index: int, count: int) -> int
        """
        ...

    def RemoveAll(self, match:Predicate) -> int:
        """ RemoveAll(self: List[T], match: Predicate[T]) -> int """
        ...

    def RemoveRange(self, index:int, count:int): # -> 
        """ RemoveRange(self: List[T], index: int, count: int) """
        ...

    def Reverse(self, index:int = ..., count:int = ...): # -> 
        """ Reverse(self: List[T], index: int, count: int)Reverse(self: List[T]) """
        ...

    def Sort(self, *__args:IComparer): # -> 
        """ Sort(self: List[T])Sort(self: List[T], comparer: IComparer[T])Sort(self: List[T], index: int, count: int, comparer: IComparer[T])Sort(self: List[T], comparison: Comparison[T]) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: List[T]) -> Array[T] """
        ...

    def TrimExcess(self): # -> 
        """ TrimExcess(self: List[T]) """
        ...

    def TrueForAll(self, match:Predicate) -> bool:
        """ TrueForAll(self: List[T], match: Predicate[T]) -> bool """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y]x.__delitem__(y) <==> del x[y]x.__delitem__(y) <==> del x[y] """
        ...

    def __getslice__(self, *args): #cannot find CLR method
        """
        __getslice__(self: List[T], x: int, y: int) -> List[T]
        __getslice__(self: List[T], x: int, y: int) -> List[T]
        """
        ...



class Queue(IReadOnlyCollection, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'object'>
    """
    Queue[T]()
    Queue[T](capacity: int)
    Queue[T](collection: IEnumerable[T])
    """
    def Clear(self): # -> 
        """ Clear(self: Queue[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: Queue[T], item: T) -> bool """
        ...

    def Dequeue(self): # -> T
        """ Dequeue(self: Queue[T]) -> T """
        ...

    def Enqueue(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Enqueue(self: Queue[T], item: T) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: Queue[T]) -> Enumerator """
        ...

    def Peek(self): # -> T
        """ Peek(self: Queue[T]) -> T """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: Queue[T]) -> Array[T] """
        ...

    def TrimExcess(self): # -> 
        """ TrimExcess(self: Queue[T]) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class SortedDictionary(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'object'>
    """
    SortedDictionary[TKey, TValue]()
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    SortedDictionary[TKey, TValue](comparer: IComparer[TKey])
    """
    @property
    def Comparer(self) -> IComparer:
        """ Get: Comparer(self: SortedDictionary[TKey, TValue]) -> IComparer[TKey] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SortedDictionary[TKey, TValue]) -> int """
        ...


    def ContainsValue(self, value) -> bool: # Not found arg types: {'value': 'TValue'}
        """ ContainsValue(self: SortedDictionary[TKey, TValue], value: TValue) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SortedDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], index: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def KeyCollection(self, *args): #cannot find CLR method
        """ KeyCollection(dictionary: SortedDictionary[TKey, TValue]) """
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        """ ValueCollection(dictionary: SortedDictionary[TKey, TValue]) """
        ...



class SortedList(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'object'>
    """
    SortedList[TKey, TValue]()
    SortedList[TKey, TValue](capacity: int)
    SortedList[TKey, TValue](comparer: IComparer[TKey])
    SortedList[TKey, TValue](capacity: int, comparer: IComparer[TKey])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue])
    SortedList[TKey, TValue](dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey])
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: SortedList[TKey, TValue]) -> int
        Set: Capacity(self: SortedList[TKey, TValue]) = value
        """
        ...

    @property
    def Comparer(self) -> IComparer:
        """ Get: Comparer(self: SortedList[TKey, TValue]) -> IComparer[TKey] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SortedList[TKey, TValue]) -> int """
        ...


    def ContainsValue(self, value) -> bool: # Not found arg types: {'value': 'TValue'}
        """ ContainsValue(self: SortedList[TKey, TValue], value: TValue) -> bool """
        ...

    def IndexOfKey(self, key) -> int: # Not found arg types: {'key': 'TKey'}
        """ IndexOfKey(self: SortedList[TKey, TValue], key: TKey) -> int """
        ...

    def IndexOfValue(self, value) -> int: # Not found arg types: {'value': 'TValue'}
        """ IndexOfValue(self: SortedList[TKey, TValue], value: TValue) -> int """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SortedList[TKey, TValue], index: int) """
        ...

    def TrimExcess(self): # -> 
        """ TrimExcess(self: SortedList[TKey, TValue]) """
        ...


class SortedSet(IReadOnlyCollection, ISet, IDeserializationCallback, ISerializable, ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'object'>
    """
    SortedSet[T]()
    SortedSet[T](comparer: IComparer[T])
    SortedSet[T](collection: IEnumerable[T])
    SortedSet[T](collection: IEnumerable[T], comparer: IComparer[T])
    """
    @property
    def Comparer(self) -> IComparer:
        """ Get: Comparer(self: SortedSet[T]) -> IComparer[T] """
        ...

    @property
    def Max(self): # -> T
        """ Get: Max(self: SortedSet[T]) -> T """
        ...

    @property
    def Min(self): # -> T
        """ Get: Min(self: SortedSet[T]) -> T """
        ...


    def Clear(self): # -> 
        """ Clear(self: SortedSet[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: SortedSet[T], item: T) -> bool """
        ...

    @staticmethod
    def CreateSetComparer(memberEqualityComparer=None) -> IEqualityComparer:
        """
        CreateSetComparer() -> IEqualityComparer[SortedSet[T]]
        CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]
        """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: SortedSet[T]) -> Enumerator """
        ...

    def GetViewBetween(self, lowerValue, upperValue) -> SortedSet: # Not found arg types: {'upperValue': 'T', 'lowerValue': 'T'}
        """ GetViewBetween(self: SortedSet[T], lowerValue: T, upperValue: T) -> SortedSet[T] """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Remove(self: SortedSet[T], item: T) -> bool """
        ...

    def RemoveWhere(self, match:Predicate) -> int:
        """ RemoveWhere(self: SortedSet[T], match: Predicate[T]) -> int """
        ...

    def Reverse(self) -> IEnumerable:
        """ Reverse(self: SortedSet[T]) -> IEnumerable[T] """
        ...

    def TryGetValue(self, equalValue, actualValue): # -> Tuple_[bool, T]
        """ TryGetValue(self: SortedSet[T], equalValue: T) -> (bool, T) """
        ...



class Stack(IReadOnlyCollection, ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """
    Stack[T]()
    Stack[T](capacity: int)
    Stack[T](collection: IEnumerable[T])
    """
    def Clear(self): # -> 
        """ Clear(self: Stack[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: Stack[T], item: T) -> bool """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: Stack[T]) -> Enumerator """
        ...

    def Peek(self): # -> T
        """ Peek(self: Stack[T]) -> T """
        ...

    def Pop(self): # -> T
        """ Pop(self: Stack[T]) -> T """
        ...

    def Push(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Push(self: Stack[T], item: T) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: Stack[T]) -> Array[T] """
        ...

    def TrimExcess(self): # -> 
        """ TrimExcess(self: Stack[T]) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class SynchronizedCollection(IList): # skipped bases: <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SynchronizedCollection[T]()
    SynchronizedCollection[T](syncRoot: object)
    SynchronizedCollection[T](syncRoot: object, list: IEnumerable[T])
    SynchronizedCollection[T](syncRoot: object, *list: Array[T])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SynchronizedCollection[T]) -> int """
        ...

    @property
    def Items(self):
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: SynchronizedCollection[T]) -> object """
        ...


    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: SynchronizedCollection[T]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SynchronizedCollection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SynchronizedCollection[T]) -> IEnumerator[T] """
        ...

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: SynchronizedCollection[T], index: int, item: T) """
        ...

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: SynchronizedCollection[T], index: int) """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: SynchronizedCollection[T], index: int, item: T) """
        ...


class SynchronizedKeyedCollection(SynchronizedCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IList[T]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[T]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Dictionary(self):
        ...


    def ChangeItemKey(self, *args): #cannot find CLR method
        """ ChangeItemKey(self: SynchronizedKeyedCollection[K, T], item: T, newKey: K) """
        ...

    def GetKeyForItem(self, *args): #cannot find CLR method
        """ GetKeyForItem(self: SynchronizedKeyedCollection[K, T], item: T) -> K """
        ...


class SynchronizedReadOnlyCollection(IList): # skipped bases: <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SynchronizedReadOnlyCollection[T]()
    SynchronizedReadOnlyCollection[T](syncRoot: object)
    SynchronizedReadOnlyCollection[T](syncRoot: object, list: IEnumerable[T])
    SynchronizedReadOnlyCollection[T](syncRoot: object, *list: Array[T])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SynchronizedReadOnlyCollection[T]) -> int """
        ...

    @property
    def Items(self):
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SynchronizedReadOnlyCollection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SynchronizedReadOnlyCollection[T]) -> IEnumerator[T] """
        ...


