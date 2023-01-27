# encoding: utf-8
# module System.Collections.Concurrent calls itself Concurrent
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IDisposable, TimeSpan

from System.Collections import (ICollection, IDictionary, IEnumerable, 
    IEnumerator, IList)

from System.Collections.Generic import (IReadOnlyCollection, 
    IReadOnlyDictionary)

from System.Threading import CancellationToken

from typing import Tuple as Tuple_

"""The following names are not found in the module: (Func, T, TArg, TKey, 
    TValue, field#)
"""

# no functions
# classes

class BlockingCollection(IDisposable, IReadOnlyCollection, ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """
    BlockingCollection[T]()
    BlockingCollection[T](boundedCapacity: int)
    BlockingCollection[T](collection: IProducerConsumerCollection[T], boundedCapacity: int)
    BlockingCollection[T](collection: IProducerConsumerCollection[T])
    """
    @property
    def BoundedCapacity(self) -> int:
        """ Get: BoundedCapacity(self: BlockingCollection[T]) -> int """
        ...

    @property
    def IsAddingCompleted(self) -> bool:
        """ Get: IsAddingCompleted(self: BlockingCollection[T]) -> bool """
        ...

    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: BlockingCollection[T]) -> bool """
        ...


    def Add(self, item, cancellationToken:CancellationToken = ...): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: BlockingCollection[T], item: T)Add(self: BlockingCollection[T], item: T, cancellationToken: CancellationToken) """
        ...

    @staticmethod
    def AddToAny(collections:Array, item, cancellationToken:CancellationToken = ...) -> int: # Not found arg types: {'item': 'T'}
        """
        AddToAny(collections: Array[BlockingCollection[T]], item: T) -> int
        AddToAny(collections: Array[BlockingCollection[T]], item: T, cancellationToken: CancellationToken) -> int
        """
        ...

    def CompleteAdding(self): # -> 
        """ CompleteAdding(self: BlockingCollection[T]) """
        ...

    def GetConsumingEnumerable(self, cancellationToken:CancellationToken = ...) -> IEnumerable:
        """
        GetConsumingEnumerable(self: BlockingCollection[T]) -> IEnumerable[T]
        GetConsumingEnumerable(self: BlockingCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]
        """
        ...

    def Take(self, cancellationToken:CancellationToken = ...): # -> T
        """
        Take(self: BlockingCollection[T]) -> T
        Take(self: BlockingCollection[T], cancellationToken: CancellationToken) -> T
        """
        ...

    @staticmethod
    def TakeFromAny(collections, item, cancellationToken=None): # -> Tuple_[int, T]
        """
        TakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)
        TakeFromAny(collections: Array[BlockingCollection[T]], cancellationToken: CancellationToken) -> (int, T)
        """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: BlockingCollection[T]) -> Array[T] """
        ...

    def TryAdd(self, item, *__args:TimeSpan) -> bool: # Not found arg types: {'item': 'T'}
        """
        TryAdd(self: BlockingCollection[T], item: T) -> bool
        TryAdd(self: BlockingCollection[T], item: T, timeout: TimeSpan) -> bool
        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int) -> bool
        TryAdd(self: BlockingCollection[T], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...

    @staticmethod
    def TryAddToAny(collections:Array, item, *__args:TimeSpan) -> int: # Not found arg types: {'item': 'T'}
        """
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, timeout: TimeSpan) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int) -> int
        TryAddToAny(collections: Array[BlockingCollection[T]], item: T, millisecondsTimeout: int, cancellationToken: CancellationToken) -> int
        """
        ...

    def TryTake(self, item:int, *__args:CancellationToken): # -> Tuple_[bool, T]
        """
        TryTake(self: BlockingCollection[T]) -> (bool, T)
        TryTake(self: BlockingCollection[T], timeout: TimeSpan) -> (bool, T)
        TryTake(self: BlockingCollection[T], millisecondsTimeout: int) -> (bool, T)
        TryTake(self: BlockingCollection[T], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (bool, T)
        """
        ...

    @staticmethod
    def TryTakeFromAny(collections:Array, item:int, *__args:CancellationToken): # -> Tuple_[int, T]
        """
        TryTakeFromAny(collections: Array[BlockingCollection[T]]) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]], timeout: TimeSpan) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int) -> (int, T)
        TryTakeFromAny(collections: Array[BlockingCollection[T]], millisecondsTimeout: int, cancellationToken: CancellationToken) -> (int, T)
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ConcurrentBag(IReadOnlyCollection, IProducerConsumerCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'ICollection'>, <type 'object'>
    """
    ConcurrentBag[T]()
    ConcurrentBag[T](collection: IEnumerable[T])
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: ConcurrentBag[T]) -> bool """
        ...


    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: ConcurrentBag[T], item: T) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConcurrentBag[T]) -> IEnumerator[T] """
        ...

    def TryPeek(self, result): # -> Tuple_[bool, T]
        """ TryPeek(self: ConcurrentBag[T]) -> (bool, T) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ConcurrentDictionary(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'object'>
    """
    ConcurrentDictionary[TKey, TValue]()
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int)
    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]])
    ConcurrentDictionary[TKey, TValue](comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, collection: IEnumerable[KeyValuePair[TKey, TValue]], comparer: IEqualityComparer[TKey])
    ConcurrentDictionary[TKey, TValue](concurrencyLevel: int, capacity: int, comparer: IEqualityComparer[TKey])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ConcurrentDictionary[TKey, TValue]) -> int """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: ConcurrentDictionary[TKey, TValue]) -> bool """
        ...


    def AddOrUpdate(self, key, *__args): # -> TValue
        """
        AddOrUpdate[TArg](self: ConcurrentDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TArg, TValue], updateValueFactory: Func[TKey, TValue, TArg, TValue], factoryArgument: TArg) -> TValue
        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> TValue
        AddOrUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]) -> TValue
        """
        ...

    def GetOrAdd(self, key, *__args): # -> TValue # Not found arg types: {'key': 'TKey', '*__args': 'Func'}
        """
        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> TValue
        GetOrAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> TValue
        GetOrAdd[TArg](self: ConcurrentDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg) -> TValue
        """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ConcurrentDictionary[TKey, TValue]) -> Array[KeyValuePair[TKey, TValue]] """
        ...

    def TryAdd(self, key, value) -> bool: # Not found arg types: {'value': 'TValue', 'key': 'TKey'}
        """ TryAdd(self: ConcurrentDictionary[TKey, TValue], key: TKey, value: TValue) -> bool """
        ...

    def TryRemove(self, key, value): # -> Tuple_[bool, TValue]
        """ TryRemove(self: ConcurrentDictionary[TKey, TValue], key: TKey) -> (bool, TValue) """
        ...

    def TryUpdate(self, key, newValue, comparisonValue) -> bool: # Not found arg types: {'key': 'TKey', 'comparisonValue': 'TValue', 'newValue': 'TValue'}
        """ TryUpdate(self: ConcurrentDictionary[TKey, TValue], key: TKey, newValue: TValue, comparisonValue: TValue) -> bool """
        ...


class ConcurrentQueue(IReadOnlyCollection, IProducerConsumerCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ConcurrentQueue[T]()
    ConcurrentQueue[T](collection: IEnumerable[T])
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: ConcurrentQueue[T]) -> bool """
        ...


    def Enqueue(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Enqueue(self: ConcurrentQueue[T], item: T) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConcurrentQueue[T]) -> IEnumerator[T] """
        ...

    def TryDequeue(self, result): # -> Tuple_[bool, T]
        """ TryDequeue(self: ConcurrentQueue[T]) -> (bool, T) """
        ...

    def TryPeek(self, result): # -> Tuple_[bool, T]
        """ TryPeek(self: ConcurrentQueue[T]) -> (bool, T) """
        ...


class ConcurrentStack(IReadOnlyCollection, IProducerConsumerCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ConcurrentStack[T]()
    ConcurrentStack[T](collection: IEnumerable[T])
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: ConcurrentStack[T]) -> bool """
        ...


    def Clear(self): # -> 
        """ Clear(self: ConcurrentStack[T]) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConcurrentStack[T]) -> IEnumerator[T] """
        ...

    def Push(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Push(self: ConcurrentStack[T], item: T) """
        ...

    def PushRange(self, items:Array, startIndex:int = ..., count:int = ...): # -> 
        """ PushRange(self: ConcurrentStack[T], items: Array[T])PushRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int) """
        ...

    def TryPeek(self, result): # -> Tuple_[bool, T]
        """ TryPeek(self: ConcurrentStack[T]) -> (bool, T) """
        ...

    def TryPop(self, result): # -> Tuple_[bool, T]
        """ TryPop(self: ConcurrentStack[T]) -> (bool, T) """
        ...

    def TryPopRange(self, items:Array, startIndex:int = ..., count:int = ...) -> int:
        """
        TryPopRange(self: ConcurrentStack[T], items: Array[T]) -> int
        TryPopRange(self: ConcurrentStack[T], items: Array[T], startIndex: int, count: int) -> int
        """
        ...


class EnumerablePartitionerOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EnumerablePartitionerOptions, values: NoBuffering (1), None (0) """
    NoBuffering: EnumerablePartitionerOptions = ...
    value__ = ...


class IProducerConsumerCollection(IEnumerable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def ToArray(self) -> Array:
        """ ToArray(self: IProducerConsumerCollection[T]) -> Array[T] """
        ...

    def TryAdd(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ TryAdd(self: IProducerConsumerCollection[T], item: T) -> bool """
        ...

    def TryTake(self, item): # -> Tuple_[bool, T]
        """ TryTake(self: IProducerConsumerCollection[T]) -> (bool, T) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class OrderablePartitioner(Partitioner): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def KeysNormalized(self) -> bool:
        """ Get: KeysNormalized(self: OrderablePartitioner[TSource]) -> bool """
        ...

    @property
    def KeysOrderedAcrossPartitions(self) -> bool:
        """ Get: KeysOrderedAcrossPartitions(self: OrderablePartitioner[TSource]) -> bool """
        ...

    @property
    def KeysOrderedInEachPartition(self) -> bool:
        """ Get: KeysOrderedInEachPartition(self: OrderablePartitioner[TSource]) -> bool """
        ...


    def GetOrderableDynamicPartitions(self) -> IEnumerable:
        """ GetOrderableDynamicPartitions(self: OrderablePartitioner[TSource]) -> IEnumerable[KeyValuePair[Int64, TSource]] """
        ...

    def GetOrderablePartitions(self, partitionCount:int) -> IList:
        """ GetOrderablePartitions(self: OrderablePartitioner[TSource], partitionCount: int) -> IList[IEnumerator[KeyValuePair[Int64, TSource]]] """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, keysOrderedInEachPartition: bool, keysOrderedAcrossPartitions: bool, keysNormalized: bool) """
        ...


class Partitioner: # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Create(*__args:IEnumerable) -> OrderablePartitioner:
        """
        Create(fromInclusive: Int64, toExclusive: Int64) -> OrderablePartitioner[Tuple[Int64, Int64]]
        Create(fromInclusive: Int64, toExclusive: Int64, rangeSize: Int64) -> OrderablePartitioner[Tuple[Int64, Int64]]
        Create(fromInclusive: int, toExclusive: int) -> OrderablePartitioner[Tuple[int, int]]
        Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> OrderablePartitioner[Tuple[int, int]]
        Create[TSource](list: IList[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]
        Create[TSource](array: Array[TSource], loadBalance: bool) -> OrderablePartitioner[TSource]
        Create[TSource](source: IEnumerable[TSource]) -> OrderablePartitioner[TSource]
        Create[TSource](source: IEnumerable[TSource], partitionerOptions: EnumerablePartitionerOptions) -> OrderablePartitioner[TSource]
        """
        ...

    __all__: list = ...


