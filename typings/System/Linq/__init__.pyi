# encoding: utf-8
# module System.Linq calls itself Linq
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Action, Array, Decimal, Enum, Int64, Nullable, Type

from System.Collections import (IComparer, IEnumerable, IEnumerator, 
    IEqualityComparer)

from System.Collections.Generic import Dictionary, HashSet, List

from System.Linq.Expressions import Expression

from System.Threading import CancellationToken

"""The following names are not found in the module: (Func, TKey, TResult, 
    TSource, field#)
"""

# no functions
# classes

class Enumerable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Aggregate(source:IEnumerable, *__args): # -> TSource # Not found arg types: {'*__args': 'Func'}
        """
        Aggregate[TSource](source: IEnumerable[TSource], func: Func[TSource, TSource, TSource]) -> TSource
        Aggregate[(TSource, TAccumulate)](source: IEnumerable[TSource], seed: TAccumulate, func: Func[TAccumulate, TSource, TAccumulate]) -> TAccumulate
        Aggregate[(TSource, TAccumulate, TResult)](source: IEnumerable[TSource], seed: TAccumulate, func: Func[TAccumulate, TSource, TAccumulate], resultSelector: Func[TAccumulate, TResult]) -> TResult
        """
        ...

    @staticmethod
    def All(source:IEnumerable, predicate) -> bool: # Not found arg types: {'predicate': 'Func'}
        """ All[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool """
        ...

    @staticmethod
    def Any(source:IEnumerable, predicate = ...) -> bool: # Not found arg types: {'predicate': 'Func'}
        """
        Any[TSource](source: IEnumerable[TSource]) -> bool
        Any[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> bool
        """
        ...

    @staticmethod
    def Append(source:IEnumerable, element) -> IEnumerable: # Not found arg types: {'element': 'TSource'}
        """ Append[TSource](source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def AsEnumerable(source:IEnumerable) -> IEnumerable:
        """ AsEnumerable[TSource](source: IEnumerable[TSource]) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def Average(source:IEnumerable, selector = ...) -> Nullable: # Not found arg types: {'selector': 'Func'}
        """
        Average(source: IEnumerable[int]) -> float
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, float]) -> float
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Single]) -> Single
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[float]
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Int64]) -> float
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[float]
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, int]) -> float
        Average(source: IEnumerable[Nullable[Decimal]]) -> Nullable[Decimal]
        Average(source: IEnumerable[Nullable[float]]) -> Nullable[float]
        Average(source: IEnumerable[Nullable[Single]]) -> Nullable[Single]
        Average(source: IEnumerable[Nullable[Int64]]) -> Nullable[float]
        Average(source: IEnumerable[Nullable[int]]) -> Nullable[float]
        Average(source: IEnumerable[Decimal]) -> Decimal
        Average(source: IEnumerable[float]) -> float
        Average(source: IEnumerable[Single]) -> Single
        Average(source: IEnumerable[Int64]) -> float
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Average[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Cast(source:IEnumerable) -> IEnumerable:
        """ Cast[TResult](source: IEnumerable) -> IEnumerable[TResult] """
        ...

    @staticmethod
    def Concat(first:IEnumerable, second:IEnumerable) -> IEnumerable:
        """ Concat[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource]) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def Contains(source:IEnumerable, value, comparer:IEqualityComparer = ...) -> bool: # Not found arg types: {'value': 'TSource'}
        """
        Contains[TSource](source: IEnumerable[TSource], value: TSource) -> bool
        Contains[TSource](source: IEnumerable[TSource], value: TSource, comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Count(source:IEnumerable, predicate = ...) -> int: # Not found arg types: {'predicate': 'Func'}
        """
        Count[TSource](source: IEnumerable[TSource]) -> int
        Count[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> int
        """
        ...

    @staticmethod
    def DefaultIfEmpty(source:IEnumerable, defaultValue = ...) -> IEnumerable: # Not found arg types: {'defaultValue': 'TSource'}
        """
        DefaultIfEmpty[TSource](source: IEnumerable[TSource]) -> IEnumerable[TSource]
        DefaultIfEmpty[TSource](source: IEnumerable[TSource], defaultValue: TSource) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def Distinct(source:IEnumerable, comparer:IEqualityComparer = ...) -> IEnumerable:
        """
        Distinct[TSource](source: IEnumerable[TSource]) -> IEnumerable[TSource]
        Distinct[TSource](source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def ElementAt(source:IEnumerable, index:int): # -> TSource
        """ ElementAt[TSource](source: IEnumerable[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def ElementAtOrDefault(source:IEnumerable, index:int): # -> TSource
        """ ElementAtOrDefault[TSource](source: IEnumerable[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def Empty() -> IEnumerable:
        """ Empty[TResult]() -> IEnumerable[TResult] """
        ...

    @staticmethod
    def Except(first:IEnumerable, second:IEnumerable, comparer:IEqualityComparer = ...) -> IEnumerable:
        """
        Except[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource]) -> IEnumerable[TSource]
        Except[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def First(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        First[TSource](source: IEnumerable[TSource]) -> TSource
        First[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def FirstOrDefault(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        FirstOrDefault[TSource](source: IEnumerable[TSource]) -> TSource
        FirstOrDefault[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def GroupBy(source:IEnumerable, keySelector, *__args:IEqualityComparer) -> IEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """
        GroupBy[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey]) -> IEnumerable[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> IEnumerable[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> IEnumerable[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> IEnumerable[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey, TResult)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], resultSelector: Func[TKey, IEnumerable[TSource], TResult]) -> IEnumerable[TResult]
        GroupBy[(TSource, TKey, TElement, TResult)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], resultSelector: Func[TKey, IEnumerable[TElement], TResult]) -> IEnumerable[TResult]
        GroupBy[(TSource, TKey, TResult)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], resultSelector: Func[TKey, IEnumerable[TSource], TResult], comparer: IEqualityComparer[TKey]) -> IEnumerable[TResult]
        GroupBy[(TSource, TKey, TElement, TResult)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], resultSelector: Func[TKey, IEnumerable[TElement], TResult], comparer: IEqualityComparer[TKey]) -> IEnumerable[TResult]
        """
        ...

    @staticmethod
    def GroupJoin(outer, inner, outerKeySelector, innerKeySelector, resultSelector, comparer=None) -> IEnumerable:
        """
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: IEnumerable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult]) -> IEnumerable[TResult]
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: IEnumerable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult], comparer: IEqualityComparer[TKey]) -> IEnumerable[TResult]
        """
        ...

    @staticmethod
    def Intersect(first:IEnumerable, second:IEnumerable, comparer:IEqualityComparer = ...) -> IEnumerable:
        """
        Intersect[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource]) -> IEnumerable[TSource]
        Intersect[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def Join(outer:IEnumerable, inner:IEnumerable, outerKeySelector, innerKeySelector, resultSelector, comparer:IEqualityComparer = ...) -> IEnumerable: # Not found arg types: {'resultSelector': 'Func', 'innerKeySelector': 'Func', 'outerKeySelector': 'Func'}
        """
        Join[(TOuter, TInner, TKey, TResult)](outer: IEnumerable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult]) -> IEnumerable[TResult]
        Join[(TOuter, TInner, TKey, TResult)](outer: IEnumerable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult], comparer: IEqualityComparer[TKey]) -> IEnumerable[TResult]
        """
        ...

    @staticmethod
    def Last(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        Last[TSource](source: IEnumerable[TSource]) -> TSource
        Last[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def LastOrDefault(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        LastOrDefault[TSource](source: IEnumerable[TSource]) -> TSource
        LastOrDefault[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def LongCount(source:IEnumerable, predicate = ...) -> Int64: # Not found arg types: {'predicate': 'Func'}
        """
        LongCount[TSource](source: IEnumerable[TSource]) -> Int64
        LongCount[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> Int64
        """
        ...

    @staticmethod
    def Max(source:IEnumerable, selector = ...) -> Decimal: # Not found arg types: {'selector': 'Func'}
        """
        Max(source: IEnumerable[int]) -> int
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, float]) -> float
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Single]) -> Single
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Int64]) -> Int64
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, int]) -> int
        Max[TSource](source: IEnumerable[TSource]) -> TSource
        Max(source: IEnumerable[Nullable[Decimal]]) -> Nullable[Decimal]
        Max(source: IEnumerable[Nullable[Single]]) -> Nullable[Single]
        Max(source: IEnumerable[Nullable[float]]) -> Nullable[float]
        Max(source: IEnumerable[Nullable[Int64]]) -> Nullable[Int64]
        Max(source: IEnumerable[Nullable[int]]) -> Nullable[int]
        Max(source: IEnumerable[Decimal]) -> Decimal
        Max(source: IEnumerable[Single]) -> Single
        Max(source: IEnumerable[float]) -> float
        Max(source: IEnumerable[Int64]) -> Int64
        Max[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        Max[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult
        """
        ...

    @staticmethod
    def Min(source:IEnumerable, selector = ...) -> Decimal: # Not found arg types: {'selector': 'Func'}
        """
        Min(source: IEnumerable[int]) -> int
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, float]) -> float
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Single]) -> Single
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Int64]) -> Int64
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, int]) -> int
        Min[TSource](source: IEnumerable[TSource]) -> TSource
        Min(source: IEnumerable[Nullable[Decimal]]) -> Nullable[Decimal]
        Min(source: IEnumerable[Nullable[float]]) -> Nullable[float]
        Min(source: IEnumerable[Nullable[Single]]) -> Nullable[Single]
        Min(source: IEnumerable[Nullable[Int64]]) -> Nullable[Int64]
        Min(source: IEnumerable[Nullable[int]]) -> Nullable[int]
        Min(source: IEnumerable[Decimal]) -> Decimal
        Min(source: IEnumerable[float]) -> float
        Min(source: IEnumerable[Single]) -> Single
        Min(source: IEnumerable[Int64]) -> Int64
        Min[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        Min[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> TResult
        """
        ...

    @staticmethod
    def OfType(source:IEnumerable) -> IEnumerable:
        """ OfType[TResult](source: IEnumerable) -> IEnumerable[TResult] """
        ...

    @staticmethod
    def OrderBy(source:IEnumerable, keySelector, comparer:IComparer = ...) -> IOrderedEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderBy[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey]) -> IOrderedEnumerable[TSource]
        OrderBy[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> IOrderedEnumerable[TSource]
        """
        ...

    @staticmethod
    def OrderByDescending(source:IEnumerable, keySelector, comparer:IComparer = ...) -> IOrderedEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderByDescending[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey]) -> IOrderedEnumerable[TSource]
        OrderByDescending[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> IOrderedEnumerable[TSource]
        """
        ...

    @staticmethod
    def Prepend(source:IEnumerable, element) -> IEnumerable: # Not found arg types: {'element': 'TSource'}
        """ Prepend[TSource](source: IEnumerable[TSource], element: TSource) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def Range(start:int, count:int) -> IEnumerable:
        """ Range(start: int, count: int) -> IEnumerable[int] """
        ...

    @staticmethod
    def Repeat(element, count:int) -> IEnumerable: # Not found arg types: {'element': 'TResult'}
        """ Repeat[TResult](element: TResult, count: int) -> IEnumerable[TResult] """
        ...

    @staticmethod
    def Reverse(source:IEnumerable) -> IEnumerable:
        """ Reverse[TSource](source: IEnumerable[TSource]) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def Select(source:IEnumerable, selector) -> IEnumerable: # Not found arg types: {'selector': 'Func'}
        """
        Select[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, TResult]) -> IEnumerable[TResult]
        Select[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, int, TResult]) -> IEnumerable[TResult]
        """
        ...

    @staticmethod
    def SelectMany(source:IEnumerable, *__args) -> IEnumerable: # Not found arg types: {'*__args': 'Func'}
        """
        SelectMany[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, IEnumerable[TResult]]) -> IEnumerable[TResult]
        SelectMany[(TSource, TResult)](source: IEnumerable[TSource], selector: Func[TSource, int, IEnumerable[TResult]]) -> IEnumerable[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: IEnumerable[TSource], collectionSelector: Func[TSource, int, IEnumerable[TCollection]], resultSelector: Func[TSource, TCollection, TResult]) -> IEnumerable[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: IEnumerable[TSource], collectionSelector: Func[TSource, IEnumerable[TCollection]], resultSelector: Func[TSource, TCollection, TResult]) -> IEnumerable[TResult]
        """
        ...

    @staticmethod
    def SequenceEqual(first:IEnumerable, second:IEnumerable, comparer:IEqualityComparer = ...) -> bool:
        """
        SequenceEqual[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource]) -> bool
        SequenceEqual[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Single(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        Single[TSource](source: IEnumerable[TSource]) -> TSource
        Single[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def SingleOrDefault(source:IEnumerable, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        SingleOrDefault[TSource](source: IEnumerable[TSource]) -> TSource
        SingleOrDefault[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def Skip(source:IEnumerable, count:int) -> IEnumerable:
        """ Skip[TSource](source: IEnumerable[TSource], count: int) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def SkipWhile(source:IEnumerable, predicate) -> IEnumerable: # Not found arg types: {'predicate': 'Func'}
        """
        SkipWhile[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> IEnumerable[TSource]
        SkipWhile[TSource](source: IEnumerable[TSource], predicate: Func[TSource, int, bool]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def Sum(source:IEnumerable, selector = ...) -> Nullable: # Not found arg types: {'selector': 'Func'}
        """
        Sum(source: IEnumerable[int]) -> int
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, float]) -> float
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Single]) -> Single
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Int64]) -> Int64
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, int]) -> int
        Sum(source: IEnumerable[Nullable[Decimal]]) -> Nullable[Decimal]
        Sum(source: IEnumerable[Nullable[float]]) -> Nullable[float]
        Sum(source: IEnumerable[Nullable[Single]]) -> Nullable[Single]
        Sum(source: IEnumerable[Nullable[Int64]]) -> Nullable[Int64]
        Sum(source: IEnumerable[Nullable[int]]) -> Nullable[int]
        Sum(source: IEnumerable[Decimal]) -> Decimal
        Sum(source: IEnumerable[float]) -> float
        Sum(source: IEnumerable[Single]) -> Single
        Sum(source: IEnumerable[Int64]) -> Int64
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Sum[TSource](source: IEnumerable[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Take(source:IEnumerable, count:int) -> IEnumerable:
        """ Take[TSource](source: IEnumerable[TSource], count: int) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def TakeWhile(source:IEnumerable, predicate) -> IEnumerable: # Not found arg types: {'predicate': 'Func'}
        """
        TakeWhile[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> IEnumerable[TSource]
        TakeWhile[TSource](source: IEnumerable[TSource], predicate: Func[TSource, int, bool]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def ThenBy(source:IOrderedEnumerable, keySelector, comparer:IComparer = ...) -> IOrderedEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """
        ThenBy[(TSource, TKey)](source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]) -> IOrderedEnumerable[TSource]
        ThenBy[(TSource, TKey)](source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> IOrderedEnumerable[TSource]
        """
        ...

    @staticmethod
    def ThenByDescending(source:IOrderedEnumerable, keySelector, comparer:IComparer = ...) -> IOrderedEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """
        ThenByDescending[(TSource, TKey)](source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey]) -> IOrderedEnumerable[TSource]
        ThenByDescending[(TSource, TKey)](source: IOrderedEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> IOrderedEnumerable[TSource]
        """
        ...

    @staticmethod
    def ToArray(source:IEnumerable) -> Array:
        """ ToArray[TSource](source: IEnumerable[TSource]) -> Array[TSource] """
        ...

    @staticmethod
    def ToDictionary(source:IEnumerable, keySelector, *__args:IEqualityComparer) -> Dictionary: # Not found arg types: {'keySelector': 'Func'}
        """
        ToDictionary[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey]) -> Dictionary[TKey, TSource]
        ToDictionary[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, TSource]
        ToDictionary[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> Dictionary[TKey, TElement]
        ToDictionary[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, TElement]
        """
        ...

    @staticmethod
    def ToHashSet(source:IEnumerable, comparer:IEqualityComparer = ...) -> HashSet:
        """
        ToHashSet[TSource](source: IEnumerable[TSource]) -> HashSet[TSource]
        ToHashSet[TSource](source: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> HashSet[TSource]
        """
        ...

    @staticmethod
    def ToList(source:IEnumerable) -> List:
        """ ToList[TSource](source: IEnumerable[TSource]) -> List[TSource] """
        ...

    @staticmethod
    def ToLookup(source:IEnumerable, keySelector, *__args:IEqualityComparer) -> ILookup: # Not found arg types: {'keySelector': 'Func'}
        """
        ToLookup[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey]) -> ILookup[TKey, TSource]
        ToLookup[(TSource, TKey)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> ILookup[TKey, TSource]
        ToLookup[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> ILookup[TKey, TElement]
        ToLookup[(TSource, TKey, TElement)](source: IEnumerable[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> ILookup[TKey, TElement]
        """
        ...

    @staticmethod
    def Union(first:IEnumerable, second:IEnumerable, comparer:IEqualityComparer = ...) -> IEnumerable:
        """
        Union[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource]) -> IEnumerable[TSource]
        Union[TSource](first: IEnumerable[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def Where(source:IEnumerable, predicate) -> IEnumerable: # Not found arg types: {'predicate': 'Func'}
        """
        Where[TSource](source: IEnumerable[TSource], predicate: Func[TSource, bool]) -> IEnumerable[TSource]
        Where[TSource](source: IEnumerable[TSource], predicate: Func[TSource, int, bool]) -> IEnumerable[TSource]
        """
        ...

    @staticmethod
    def Zip(first:IEnumerable, second:IEnumerable, resultSelector) -> IEnumerable: # Not found arg types: {'resultSelector': 'Func'}
        """ Zip[(TFirst, TSecond, TResult)](first: IEnumerable[TFirst], second: IEnumerable[TSecond], resultSelector: Func[TFirst, TSecond, TResult]) -> IEnumerable[TResult] """
        ...

    __all__: list = ...


class EnumerableExecutor: # skipped bases: <type 'object'>
    """ no doc """
    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class EnumerableQuery: # skipped bases: <type 'object'>
    """ no doc """
    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class IGrouping(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Key(self): # -> TKey
        """ Get: Key(self: IGrouping[TKey, TElement]) -> TKey """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TElement](enumerable: IEnumerable[TElement], value: TElement) -> bool """
        ...


class ILookup(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ILookup[TKey, TElement]) -> int """
        ...


    def Contains(self, key) -> bool: # Not found arg types: {'key': 'TKey'}
        """ Contains(self: ILookup[TKey, TElement], key: TKey) -> bool """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IGrouping`2](enumerable: IEnumerable[IGrouping[TKey, TElement]], value: IGrouping[TKey, TElement]) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IOrderedEnumerable(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def CreateOrderedEnumerable(self, keySelector, comparer:IComparer, descending:bool) -> IOrderedEnumerable: # Not found arg types: {'keySelector': 'Func'}
        """ CreateOrderedEnumerable[TKey](self: IOrderedEnumerable[TElement], keySelector: Func[TElement, TKey], comparer: IComparer[TKey], descending: bool) -> IOrderedEnumerable[TElement] """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TElement](enumerable: IEnumerable[TElement], value: TElement) -> bool """
        ...


class IOrderedQueryable: # skipped bases: <type 'object'>
    """ no doc """
    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class IQueryable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementType(self) -> Type:
        """ Get: ElementType(self: IQueryable) -> Type """
        ...

    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: IQueryable) -> Expression """
        ...

    @property
    def Provider(self) -> IQueryProvider:
        """ Get: Provider(self: IQueryable) -> IQueryProvider """
        ...


    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class IQueryProvider: # skipped bases: <type 'object'>
    """ no doc """
    def CreateQuery(self, expression:Expression) -> IQueryable:
        """
        CreateQuery(self: IQueryProvider, expression: Expression) -> IQueryable
        CreateQuery[TElement](self: IQueryProvider, expression: Expression) -> IQueryable[TElement]
        """
        ...

    def Execute(self, expression:Expression) -> object:
        """
        Execute(self: IQueryProvider, expression: Expression) -> object
        Execute[TResult](self: IQueryProvider, expression: Expression) -> TResult
        """
        ...


class Lookup(ILookup): # skipped bases: <type 'IEnumerable[IGrouping[TKey, TElement]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def ApplyResultSelector(self, resultSelector) -> IEnumerable: # Not found arg types: {'resultSelector': 'Func'}
        """ ApplyResultSelector[TResult](self: Lookup[TKey, TElement], resultSelector: Func[TKey, IEnumerable[TElement], TResult]) -> IEnumerable[TResult] """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Lookup[TKey, TElement]) -> IEnumerator[IGrouping[TKey, TElement]] """
        ...


class OrderedParallelQuery(ParallelQuery): # skipped bases: <type 'IEnumerable[TSource]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class ParallelEnumerable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Aggregate(source:ParallelQuery, *__args): # -> TSource # Not found arg types: {'*__args': 'Func'}
        """
        Aggregate[TSource](source: ParallelQuery[TSource], func: Func[TSource, TSource, TSource]) -> TSource
        Aggregate[(TSource, TAccumulate)](source: ParallelQuery[TSource], seed: TAccumulate, func: Func[TAccumulate, TSource, TAccumulate]) -> TAccumulate
        Aggregate[(TSource, TAccumulate, TResult)](source: ParallelQuery[TSource], seed: TAccumulate, func: Func[TAccumulate, TSource, TAccumulate], resultSelector: Func[TAccumulate, TResult]) -> TResult
        Aggregate[(TSource, TAccumulate, TResult)](source: ParallelQuery[TSource], seed: TAccumulate, updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate], combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate], resultSelector: Func[TAccumulate, TResult]) -> TResult
        Aggregate[(TSource, TAccumulate, TResult)](source: ParallelQuery[TSource], seedFactory: Func[TAccumulate], updateAccumulatorFunc: Func[TAccumulate, TSource, TAccumulate], combineAccumulatorsFunc: Func[TAccumulate, TAccumulate, TAccumulate], resultSelector: Func[TAccumulate, TResult]) -> TResult
        """
        ...

    @staticmethod
    def All(source:ParallelQuery, predicate) -> bool: # Not found arg types: {'predicate': 'Func'}
        """ All[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool """
        ...

    @staticmethod
    def Any(source:ParallelQuery, predicate = ...) -> bool: # Not found arg types: {'predicate': 'Func'}
        """
        Any[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> bool
        Any[TSource](source: ParallelQuery[TSource]) -> bool
        """
        ...

    @staticmethod
    def AsEnumerable(source:ParallelQuery) -> IEnumerable:
        """ AsEnumerable[TSource](source: ParallelQuery[TSource]) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def AsOrdered(source:ParallelQuery) -> ParallelQuery:
        """
        AsOrdered[TSource](source: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        AsOrdered(source: ParallelQuery) -> ParallelQuery
        """
        ...

    @staticmethod
    def AsParallel(source:IEnumerable) -> ParallelQuery:
        """
        AsParallel[TSource](source: IEnumerable[TSource]) -> ParallelQuery[TSource]
        AsParallel[TSource](source: Partitioner[TSource]) -> ParallelQuery[TSource]
        AsParallel(source: IEnumerable) -> ParallelQuery
        """
        ...

    @staticmethod
    def AsSequential(source:ParallelQuery) -> IEnumerable:
        """ AsSequential[TSource](source: ParallelQuery[TSource]) -> IEnumerable[TSource] """
        ...

    @staticmethod
    def AsUnordered(source:ParallelQuery) -> ParallelQuery:
        """ AsUnordered[TSource](source: ParallelQuery[TSource]) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def Average(source:ParallelQuery, selector = ...) -> Nullable: # Not found arg types: {'selector': 'Func'}
        """
        Average(source: ParallelQuery[int]) -> float
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Single]) -> Single
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[float]
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Int64]) -> float
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[float]
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, int]) -> float
        Average(source: ParallelQuery[Nullable[Decimal]]) -> Nullable[Decimal]
        Average(source: ParallelQuery[Decimal]) -> Decimal
        Average(source: ParallelQuery[Nullable[float]]) -> Nullable[float]
        Average(source: ParallelQuery[float]) -> float
        Average(source: ParallelQuery[Nullable[Single]]) -> Nullable[Single]
        Average(source: ParallelQuery[Single]) -> Single
        Average(source: ParallelQuery[Nullable[Int64]]) -> Nullable[float]
        Average(source: ParallelQuery[Int64]) -> float
        Average(source: ParallelQuery[Nullable[int]]) -> Nullable[float]
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Average[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Cast(source:ParallelQuery) -> ParallelQuery:
        """ Cast[TResult](source: ParallelQuery) -> ParallelQuery[TResult] """
        ...

    @staticmethod
    def Concat(first:ParallelQuery, second:ParallelQuery) -> ParallelQuery:
        """
        Concat[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        Concat[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Contains(source:ParallelQuery, value, comparer:IEqualityComparer = ...) -> bool: # Not found arg types: {'value': 'TSource'}
        """
        Contains[TSource](source: ParallelQuery[TSource], value: TSource) -> bool
        Contains[TSource](source: ParallelQuery[TSource], value: TSource, comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Count(source:ParallelQuery, predicate = ...) -> int: # Not found arg types: {'predicate': 'Func'}
        """
        Count[TSource](source: ParallelQuery[TSource]) -> int
        Count[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> int
        """
        ...

    @staticmethod
    def DefaultIfEmpty(source:ParallelQuery, defaultValue = ...) -> ParallelQuery: # Not found arg types: {'defaultValue': 'TSource'}
        """
        DefaultIfEmpty[TSource](source: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        DefaultIfEmpty[TSource](source: ParallelQuery[TSource], defaultValue: TSource) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Distinct(source:ParallelQuery, comparer:IEqualityComparer = ...) -> ParallelQuery:
        """
        Distinct[TSource](source: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        Distinct[TSource](source: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def ElementAt(source:ParallelQuery, index:int): # -> TSource
        """ ElementAt[TSource](source: ParallelQuery[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def ElementAtOrDefault(source:ParallelQuery, index:int): # -> TSource
        """ ElementAtOrDefault[TSource](source: ParallelQuery[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def Empty() -> ParallelQuery:
        """ Empty[TResult]() -> ParallelQuery[TResult] """
        ...

    @staticmethod
    def Except(first:ParallelQuery, second:ParallelQuery, comparer:IEqualityComparer = ...) -> ParallelQuery:
        """
        Except[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        Except[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> ParallelQuery[TSource]
        Except[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        Except[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def First(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        First[TSource](source: ParallelQuery[TSource]) -> TSource
        First[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def FirstOrDefault(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        FirstOrDefault[TSource](source: ParallelQuery[TSource]) -> TSource
        FirstOrDefault[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def ForAll(source:ParallelQuery, action:Action): # -> 
        """ ForAll[TSource](source: ParallelQuery[TSource], action: Action[TSource]) """
        ...

    @staticmethod
    def GroupBy(source:ParallelQuery, keySelector, *__args:IEqualityComparer) -> ParallelQuery: # Not found arg types: {'keySelector': 'Func'}
        """
        GroupBy[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> ParallelQuery[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> ParallelQuery[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> ParallelQuery[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> ParallelQuery[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey, TResult)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], resultSelector: Func[TKey, IEnumerable[TSource], TResult]) -> ParallelQuery[TResult]
        GroupBy[(TSource, TKey, TResult)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], resultSelector: Func[TKey, IEnumerable[TSource], TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        GroupBy[(TSource, TKey, TElement, TResult)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], resultSelector: Func[TKey, IEnumerable[TElement], TResult]) -> ParallelQuery[TResult]
        GroupBy[(TSource, TKey, TElement, TResult)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], resultSelector: Func[TKey, IEnumerable[TElement], TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        """
        ...

    @staticmethod
    def GroupJoin(outer, inner, outerKeySelector, innerKeySelector, resultSelector, comparer=None) -> ParallelQuery:
        """
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: ParallelQuery[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult]) -> ParallelQuery[TResult]
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult]) -> ParallelQuery[TResult]
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: ParallelQuery[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, IEnumerable[TInner], TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        """
        ...

    @staticmethod
    def Intersect(first:ParallelQuery, second:ParallelQuery, comparer:IEqualityComparer = ...) -> ParallelQuery:
        """
        Intersect[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        Intersect[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> ParallelQuery[TSource]
        Intersect[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        Intersect[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Join(outer:ParallelQuery, inner:ParallelQuery, outerKeySelector, innerKeySelector, resultSelector, comparer:IEqualityComparer = ...) -> ParallelQuery: # Not found arg types: {'resultSelector': 'Func', 'innerKeySelector': 'Func', 'outerKeySelector': 'Func'}
        """
        Join[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: ParallelQuery[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult]) -> ParallelQuery[TResult]
        Join[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult]) -> ParallelQuery[TResult]
        Join[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: ParallelQuery[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        Join[(TOuter, TInner, TKey, TResult)](outer: ParallelQuery[TOuter], inner: IEnumerable[TInner], outerKeySelector: Func[TOuter, TKey], innerKeySelector: Func[TInner, TKey], resultSelector: Func[TOuter, TInner, TResult], comparer: IEqualityComparer[TKey]) -> ParallelQuery[TResult]
        """
        ...

    @staticmethod
    def Last(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        Last[TSource](source: ParallelQuery[TSource]) -> TSource
        Last[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def LastOrDefault(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        LastOrDefault[TSource](source: ParallelQuery[TSource]) -> TSource
        LastOrDefault[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def LongCount(source:ParallelQuery, predicate = ...) -> Int64: # Not found arg types: {'predicate': 'Func'}
        """
        LongCount[TSource](source: ParallelQuery[TSource]) -> Int64
        LongCount[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> Int64
        """
        ...

    @staticmethod
    def Max(source:ParallelQuery, selector = ...) -> Decimal: # Not found arg types: {'selector': 'Func'}
        """
        Max(source: ParallelQuery[int]) -> int
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Single]) -> Single
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Int64]) -> Int64
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int
        Max[TSource](source: ParallelQuery[TSource]) -> TSource
        Max(source: ParallelQuery[Nullable[Decimal]]) -> Nullable[Decimal]
        Max(source: ParallelQuery[Decimal]) -> Decimal
        Max(source: ParallelQuery[Nullable[float]]) -> Nullable[float]
        Max(source: ParallelQuery[float]) -> float
        Max(source: ParallelQuery[Nullable[Single]]) -> Nullable[Single]
        Max(source: ParallelQuery[Single]) -> Single
        Max(source: ParallelQuery[Nullable[Int64]]) -> Nullable[Int64]
        Max(source: ParallelQuery[Int64]) -> Int64
        Max(source: ParallelQuery[Nullable[int]]) -> Nullable[int]
        Max[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        Max[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult
        """
        ...

    @staticmethod
    def Min(source:ParallelQuery, selector = ...) -> Decimal: # Not found arg types: {'selector': 'Func'}
        """
        Min(source: ParallelQuery[int]) -> int
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Single]) -> Single
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Int64]) -> Int64
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int
        Min[TSource](source: ParallelQuery[TSource]) -> TSource
        Min(source: ParallelQuery[Nullable[Decimal]]) -> Nullable[Decimal]
        Min(source: ParallelQuery[Decimal]) -> Decimal
        Min(source: ParallelQuery[Nullable[float]]) -> Nullable[float]
        Min(source: ParallelQuery[float]) -> float
        Min(source: ParallelQuery[Nullable[Single]]) -> Nullable[Single]
        Min(source: ParallelQuery[Single]) -> Single
        Min(source: ParallelQuery[Nullable[Int64]]) -> Nullable[Int64]
        Min(source: ParallelQuery[Int64]) -> Int64
        Min(source: ParallelQuery[Nullable[int]]) -> Nullable[int]
        Min[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        Min[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> TResult
        """
        ...

    @staticmethod
    def OfType(source:ParallelQuery) -> ParallelQuery:
        """ OfType[TResult](source: ParallelQuery) -> ParallelQuery[TResult] """
        ...

    @staticmethod
    def OrderBy(source:ParallelQuery, keySelector, comparer:IComparer = ...) -> OrderedParallelQuery: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderBy[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> OrderedParallelQuery[TSource]
        OrderBy[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> OrderedParallelQuery[TSource]
        """
        ...

    @staticmethod
    def OrderByDescending(source:ParallelQuery, keySelector, comparer:IComparer = ...) -> OrderedParallelQuery: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderByDescending[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> OrderedParallelQuery[TSource]
        OrderByDescending[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> OrderedParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Range(start:int, count:int) -> ParallelQuery:
        """ Range(start: int, count: int) -> ParallelQuery[int] """
        ...

    @staticmethod
    def Repeat(element, count:int) -> ParallelQuery: # Not found arg types: {'element': 'TResult'}
        """ Repeat[TResult](element: TResult, count: int) -> ParallelQuery[TResult] """
        ...

    @staticmethod
    def Reverse(source:ParallelQuery) -> ParallelQuery:
        """ Reverse[TSource](source: ParallelQuery[TSource]) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def Select(source:ParallelQuery, selector) -> ParallelQuery: # Not found arg types: {'selector': 'Func'}
        """
        Select[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, TResult]) -> ParallelQuery[TResult]
        Select[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, int, TResult]) -> ParallelQuery[TResult]
        """
        ...

    @staticmethod
    def SelectMany(source:ParallelQuery, *__args) -> ParallelQuery: # Not found arg types: {'*__args': 'Func'}
        """
        SelectMany[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, IEnumerable[TResult]]) -> ParallelQuery[TResult]
        SelectMany[(TSource, TResult)](source: ParallelQuery[TSource], selector: Func[TSource, int, IEnumerable[TResult]]) -> ParallelQuery[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: ParallelQuery[TSource], collectionSelector: Func[TSource, IEnumerable[TCollection]], resultSelector: Func[TSource, TCollection, TResult]) -> ParallelQuery[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: ParallelQuery[TSource], collectionSelector: Func[TSource, int, IEnumerable[TCollection]], resultSelector: Func[TSource, TCollection, TResult]) -> ParallelQuery[TResult]
        """
        ...

    @staticmethod
    def SequenceEqual(first:ParallelQuery, second:ParallelQuery, comparer:IEqualityComparer = ...) -> bool:
        """
        SequenceEqual[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> bool
        SequenceEqual[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> bool
        SequenceEqual[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]) -> bool
        SequenceEqual[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Single(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        Single[TSource](source: ParallelQuery[TSource]) -> TSource
        Single[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def SingleOrDefault(source:ParallelQuery, predicate = ...): # -> TSource # Not found arg types: {'predicate': 'Func'}
        """
        SingleOrDefault[TSource](source: ParallelQuery[TSource]) -> TSource
        SingleOrDefault[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> TSource
        """
        ...

    @staticmethod
    def Skip(source:ParallelQuery, count:int) -> ParallelQuery:
        """ Skip[TSource](source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def SkipWhile(source:ParallelQuery, predicate) -> ParallelQuery: # Not found arg types: {'predicate': 'Func'}
        """
        SkipWhile[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> ParallelQuery[TSource]
        SkipWhile[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Sum(source:ParallelQuery, selector = ...) -> Nullable: # Not found arg types: {'selector': 'Func'}
        """
        Sum(source: ParallelQuery[int]) -> int
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[float]]) -> Nullable[float]
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, float]) -> float
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Single]]) -> Nullable[Single]
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Single]) -> Single
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Int64]]) -> Nullable[Int64]
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Int64]) -> Int64
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[int]]) -> Nullable[int]
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, int]) -> int
        Sum(source: ParallelQuery[Nullable[Decimal]]) -> Nullable[Decimal]
        Sum(source: ParallelQuery[Decimal]) -> Decimal
        Sum(source: ParallelQuery[Nullable[float]]) -> Nullable[float]
        Sum(source: ParallelQuery[float]) -> float
        Sum(source: ParallelQuery[Nullable[Single]]) -> Nullable[Single]
        Sum(source: ParallelQuery[Single]) -> Single
        Sum(source: ParallelQuery[Nullable[Int64]]) -> Nullable[Int64]
        Sum(source: ParallelQuery[Int64]) -> Int64
        Sum(source: ParallelQuery[Nullable[int]]) -> Nullable[int]
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Decimal]) -> Decimal
        Sum[TSource](source: ParallelQuery[TSource], selector: Func[TSource, Nullable[Decimal]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Take(source:ParallelQuery, count:int) -> ParallelQuery:
        """ Take[TSource](source: ParallelQuery[TSource], count: int) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def TakeWhile(source:ParallelQuery, predicate) -> ParallelQuery: # Not found arg types: {'predicate': 'Func'}
        """
        TakeWhile[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> ParallelQuery[TSource]
        TakeWhile[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def ThenBy(source:OrderedParallelQuery, keySelector, comparer:IComparer = ...) -> OrderedParallelQuery: # Not found arg types: {'keySelector': 'Func'}
        """
        ThenBy[(TSource, TKey)](source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> OrderedParallelQuery[TSource]
        ThenBy[(TSource, TKey)](source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> OrderedParallelQuery[TSource]
        """
        ...

    @staticmethod
    def ThenByDescending(source:OrderedParallelQuery, keySelector, comparer:IComparer = ...) -> OrderedParallelQuery: # Not found arg types: {'keySelector': 'Func'}
        """
        ThenByDescending[(TSource, TKey)](source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> OrderedParallelQuery[TSource]
        ThenByDescending[(TSource, TKey)](source: OrderedParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IComparer[TKey]) -> OrderedParallelQuery[TSource]
        """
        ...

    @staticmethod
    def ToArray(source:ParallelQuery) -> Array:
        """ ToArray[TSource](source: ParallelQuery[TSource]) -> Array[TSource] """
        ...

    @staticmethod
    def ToDictionary(source:ParallelQuery, keySelector, *__args:IEqualityComparer) -> Dictionary: # Not found arg types: {'keySelector': 'Func'}
        """
        ToDictionary[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> Dictionary[TKey, TSource]
        ToDictionary[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, TSource]
        ToDictionary[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> Dictionary[TKey, TElement]
        ToDictionary[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, TElement]
        """
        ...

    @staticmethod
    def ToList(source:ParallelQuery) -> List:
        """ ToList[TSource](source: ParallelQuery[TSource]) -> List[TSource] """
        ...

    @staticmethod
    def ToLookup(source:ParallelQuery, keySelector, *__args:IEqualityComparer) -> ILookup: # Not found arg types: {'keySelector': 'Func'}
        """
        ToLookup[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey]) -> ILookup[TKey, TSource]
        ToLookup[(TSource, TKey)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], comparer: IEqualityComparer[TKey]) -> ILookup[TKey, TSource]
        ToLookup[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement]) -> ILookup[TKey, TElement]
        ToLookup[(TSource, TKey, TElement)](source: ParallelQuery[TSource], keySelector: Func[TSource, TKey], elementSelector: Func[TSource, TElement], comparer: IEqualityComparer[TKey]) -> ILookup[TKey, TElement]
        """
        ...

    @staticmethod
    def Union(first:ParallelQuery, second:ParallelQuery, comparer:IEqualityComparer = ...) -> ParallelQuery:
        """
        Union[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource]) -> ParallelQuery[TSource]
        Union[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource]) -> ParallelQuery[TSource]
        Union[TSource](first: ParallelQuery[TSource], second: ParallelQuery[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        Union[TSource](first: ParallelQuery[TSource], second: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def Where(source:ParallelQuery, predicate) -> ParallelQuery: # Not found arg types: {'predicate': 'Func'}
        """
        Where[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, bool]) -> ParallelQuery[TSource]
        Where[TSource](source: ParallelQuery[TSource], predicate: Func[TSource, int, bool]) -> ParallelQuery[TSource]
        """
        ...

    @staticmethod
    def WithCancellation(source:ParallelQuery, cancellationToken:CancellationToken) -> ParallelQuery:
        """ WithCancellation[TSource](source: ParallelQuery[TSource], cancellationToken: CancellationToken) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def WithDegreeOfParallelism(source:ParallelQuery, degreeOfParallelism:int) -> ParallelQuery:
        """ WithDegreeOfParallelism[TSource](source: ParallelQuery[TSource], degreeOfParallelism: int) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def WithExecutionMode(source:ParallelQuery, executionMode:ParallelExecutionMode) -> ParallelQuery:
        """ WithExecutionMode[TSource](source: ParallelQuery[TSource], executionMode: ParallelExecutionMode) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def WithMergeOptions(source:ParallelQuery, mergeOptions:ParallelMergeOptions) -> ParallelQuery:
        """ WithMergeOptions[TSource](source: ParallelQuery[TSource], mergeOptions: ParallelMergeOptions) -> ParallelQuery[TSource] """
        ...

    @staticmethod
    def Zip(first:ParallelQuery, second:ParallelQuery, resultSelector) -> ParallelQuery: # Not found arg types: {'resultSelector': 'Func'}
        """
        Zip[(TFirst, TSecond, TResult)](first: ParallelQuery[TFirst], second: ParallelQuery[TSecond], resultSelector: Func[TFirst, TSecond, TResult]) -> ParallelQuery[TResult]
        Zip[(TFirst, TSecond, TResult)](first: ParallelQuery[TFirst], second: IEnumerable[TSecond], resultSelector: Func[TFirst, TSecond, TResult]) -> ParallelQuery[TResult]
        """
        ...

    __all__: list = ...


class ParallelExecutionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParallelExecutionMode, values: Default (0), ForceParallelism (1) """
    Default: ParallelExecutionMode = ...
    ForceParallelism: ParallelExecutionMode = ...
    value__ = ...


class ParallelMergeOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParallelMergeOptions, values: AutoBuffered (2), Default (0), FullyBuffered (3), NotBuffered (1) """
    AutoBuffered: ParallelMergeOptions = ...
    Default: ParallelMergeOptions = ...
    FullyBuffered: ParallelMergeOptions = ...
    NotBuffered: ParallelMergeOptions = ...
    value__ = ...


class ParallelQuery: # skipped bases: <type 'object'>
    """ no doc """
    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class Queryable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Aggregate(source:IQueryable, *__args:Expression): # -> TSource
        """
        Aggregate[TSource](source: IQueryable[TSource], func: Expression[Func[TSource, TSource, TSource]]) -> TSource
        Aggregate[(TSource, TAccumulate)](source: IQueryable[TSource], seed: TAccumulate, func: Expression[Func[TAccumulate, TSource, TAccumulate]]) -> TAccumulate
        Aggregate[(TSource, TAccumulate, TResult)](source: IQueryable[TSource], seed: TAccumulate, func: Expression[Func[TAccumulate, TSource, TAccumulate]], selector: Expression[Func[TAccumulate, TResult]]) -> TResult
        """
        ...

    @staticmethod
    def All(source:IQueryable, predicate:Expression) -> bool:
        """ All[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> bool """
        ...

    @staticmethod
    def Any(source:IQueryable, predicate:Expression = ...) -> bool:
        """
        Any[TSource](source: IQueryable[TSource]) -> bool
        Any[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> bool
        """
        ...

    @staticmethod
    def AsQueryable(source:IEnumerable) -> IQueryable:
        """
        AsQueryable(source: IEnumerable) -> IQueryable
        AsQueryable[TElement](source: IEnumerable[TElement]) -> IQueryable[TElement]
        """
        ...

    @staticmethod
    def Average(source:IQueryable, selector:Expression = ...) -> Nullable:
        """
        Average(source: IQueryable[int]) -> float
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[float]]]) -> Nullable[float]
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, float]]) -> float
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Int64]]]) -> Nullable[float]
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Int64]]) -> float
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Single]]]) -> Nullable[Single]
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Single]]) -> Single
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[int]]]) -> Nullable[float]
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, int]]) -> float
        Average(source: IQueryable[Nullable[Decimal]]) -> Nullable[Decimal]
        Average(source: IQueryable[Decimal]) -> Decimal
        Average(source: IQueryable[Nullable[float]]) -> Nullable[float]
        Average(source: IQueryable[float]) -> float
        Average(source: IQueryable[Nullable[Single]]) -> Nullable[Single]
        Average(source: IQueryable[Single]) -> Single
        Average(source: IQueryable[Nullable[Int64]]) -> Nullable[float]
        Average(source: IQueryable[Int64]) -> float
        Average(source: IQueryable[Nullable[int]]) -> Nullable[float]
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal]]) -> Decimal
        Average[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Decimal]]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Cast(source:IQueryable) -> IQueryable:
        """ Cast[TResult](source: IQueryable) -> IQueryable[TResult] """
        ...

    @staticmethod
    def Concat(source1:IQueryable, source2:IEnumerable) -> IQueryable:
        """ Concat[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> IQueryable[TSource] """
        ...

    @staticmethod
    def Contains(source:IQueryable, item, comparer:IEqualityComparer = ...) -> bool: # Not found arg types: {'item': 'TSource'}
        """
        Contains[TSource](source: IQueryable[TSource], item: TSource) -> bool
        Contains[TSource](source: IQueryable[TSource], item: TSource, comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Count(source:IQueryable, predicate:Expression = ...) -> int:
        """
        Count[TSource](source: IQueryable[TSource]) -> int
        Count[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> int
        """
        ...

    @staticmethod
    def DefaultIfEmpty(source:IQueryable, defaultValue = ...) -> IQueryable: # Not found arg types: {'defaultValue': 'TSource'}
        """
        DefaultIfEmpty[TSource](source: IQueryable[TSource]) -> IQueryable[TSource]
        DefaultIfEmpty[TSource](source: IQueryable[TSource], defaultValue: TSource) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def Distinct(source:IQueryable, comparer:IEqualityComparer = ...) -> IQueryable:
        """
        Distinct[TSource](source: IQueryable[TSource]) -> IQueryable[TSource]
        Distinct[TSource](source: IQueryable[TSource], comparer: IEqualityComparer[TSource]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def ElementAt(source:IQueryable, index:int): # -> TSource
        """ ElementAt[TSource](source: IQueryable[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def ElementAtOrDefault(source:IQueryable, index:int): # -> TSource
        """ ElementAtOrDefault[TSource](source: IQueryable[TSource], index: int) -> TSource """
        ...

    @staticmethod
    def Except(source1:IQueryable, source2:IEnumerable, comparer:IEqualityComparer = ...) -> IQueryable:
        """
        Except[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> IQueryable[TSource]
        Except[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def First(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        First[TSource](source: IQueryable[TSource]) -> TSource
        First[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def FirstOrDefault(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        FirstOrDefault[TSource](source: IQueryable[TSource]) -> TSource
        FirstOrDefault[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def GroupBy(source:IQueryable, keySelector:Expression, *__args:Expression) -> IQueryable:
        """
        GroupBy[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]) -> IQueryable[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey, TElement)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], elementSelector: Expression[Func[TSource, TElement]]) -> IQueryable[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], comparer: IEqualityComparer[TKey]) -> IQueryable[IGrouping[TKey, TSource]]
        GroupBy[(TSource, TKey, TElement)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], elementSelector: Expression[Func[TSource, TElement]], comparer: IEqualityComparer[TKey]) -> IQueryable[IGrouping[TKey, TElement]]
        GroupBy[(TSource, TKey, TElement, TResult)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], elementSelector: Expression[Func[TSource, TElement]], resultSelector: Expression[Func[TKey, IEnumerable[TElement], TResult]]) -> IQueryable[TResult]
        GroupBy[(TSource, TKey, TResult)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], resultSelector: Expression[Func[TKey, IEnumerable[TSource], TResult]]) -> IQueryable[TResult]
        GroupBy[(TSource, TKey, TResult)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], resultSelector: Expression[Func[TKey, IEnumerable[TSource], TResult]], comparer: IEqualityComparer[TKey]) -> IQueryable[TResult]
        GroupBy[(TSource, TKey, TElement, TResult)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], elementSelector: Expression[Func[TSource, TElement]], resultSelector: Expression[Func[TKey, IEnumerable[TElement], TResult]], comparer: IEqualityComparer[TKey]) -> IQueryable[TResult]
        """
        ...

    @staticmethod
    def GroupJoin(outer, inner, outerKeySelector, innerKeySelector, resultSelector, comparer=None) -> IQueryable:
        """
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: IQueryable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Expression[Func[TOuter, TKey]], innerKeySelector: Expression[Func[TInner, TKey]], resultSelector: Expression[Func[TOuter, IEnumerable[TInner], TResult]]) -> IQueryable[TResult]
        GroupJoin[(TOuter, TInner, TKey, TResult)](outer: IQueryable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Expression[Func[TOuter, TKey]], innerKeySelector: Expression[Func[TInner, TKey]], resultSelector: Expression[Func[TOuter, IEnumerable[TInner], TResult]], comparer: IEqualityComparer[TKey]) -> IQueryable[TResult]
        """
        ...

    @staticmethod
    def Intersect(source1:IQueryable, source2:IEnumerable, comparer:IEqualityComparer = ...) -> IQueryable:
        """
        Intersect[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> IQueryable[TSource]
        Intersect[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def Join(outer:IQueryable, inner:IEnumerable, outerKeySelector:Expression, innerKeySelector:Expression, resultSelector:Expression, comparer:IEqualityComparer = ...) -> IQueryable:
        """
        Join[(TOuter, TInner, TKey, TResult)](outer: IQueryable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Expression[Func[TOuter, TKey]], innerKeySelector: Expression[Func[TInner, TKey]], resultSelector: Expression[Func[TOuter, TInner, TResult]]) -> IQueryable[TResult]
        Join[(TOuter, TInner, TKey, TResult)](outer: IQueryable[TOuter], inner: IEnumerable[TInner], outerKeySelector: Expression[Func[TOuter, TKey]], innerKeySelector: Expression[Func[TInner, TKey]], resultSelector: Expression[Func[TOuter, TInner, TResult]], comparer: IEqualityComparer[TKey]) -> IQueryable[TResult]
        """
        ...

    @staticmethod
    def Last(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        Last[TSource](source: IQueryable[TSource]) -> TSource
        Last[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def LastOrDefault(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        LastOrDefault[TSource](source: IQueryable[TSource]) -> TSource
        LastOrDefault[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def LongCount(source:IQueryable, predicate:Expression = ...) -> Int64:
        """
        LongCount[TSource](source: IQueryable[TSource]) -> Int64
        LongCount[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> Int64
        """
        ...

    @staticmethod
    def Max(source:IQueryable, selector:Expression = ...): # -> TResult
        """
        Max[TSource](source: IQueryable[TSource]) -> TSource
        Max[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]) -> TResult
        """
        ...

    @staticmethod
    def Min(source:IQueryable, selector:Expression = ...): # -> TResult
        """
        Min[TSource](source: IQueryable[TSource]) -> TSource
        Min[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]) -> TResult
        """
        ...

    @staticmethod
    def OfType(source:IQueryable) -> IQueryable:
        """ OfType[TResult](source: IQueryable) -> IQueryable[TResult] """
        ...

    @staticmethod
    def OrderBy(source:IQueryable, keySelector:Expression, comparer:IComparer = ...) -> IOrderedQueryable:
        """
        OrderBy[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]) -> IOrderedQueryable[TSource]
        OrderBy[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], comparer: IComparer[TKey]) -> IOrderedQueryable[TSource]
        """
        ...

    @staticmethod
    def OrderByDescending(source:IQueryable, keySelector:Expression, comparer:IComparer = ...) -> IOrderedQueryable:
        """
        OrderByDescending[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]) -> IOrderedQueryable[TSource]
        OrderByDescending[(TSource, TKey)](source: IQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], comparer: IComparer[TKey]) -> IOrderedQueryable[TSource]
        """
        ...

    @staticmethod
    def Reverse(source:IQueryable) -> IQueryable:
        """ Reverse[TSource](source: IQueryable[TSource]) -> IQueryable[TSource] """
        ...

    @staticmethod
    def Select(source:IQueryable, selector:Expression) -> IQueryable:
        """
        Select[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, TResult]]) -> IQueryable[TResult]
        Select[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, int, TResult]]) -> IQueryable[TResult]
        """
        ...

    @staticmethod
    def SelectMany(source:IQueryable, *__args:Expression) -> IQueryable:
        """
        SelectMany[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, IEnumerable[TResult]]]) -> IQueryable[TResult]
        SelectMany[(TSource, TResult)](source: IQueryable[TSource], selector: Expression[Func[TSource, int, IEnumerable[TResult]]]) -> IQueryable[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: IQueryable[TSource], collectionSelector: Expression[Func[TSource, int, IEnumerable[TCollection]]], resultSelector: Expression[Func[TSource, TCollection, TResult]]) -> IQueryable[TResult]
        SelectMany[(TSource, TCollection, TResult)](source: IQueryable[TSource], collectionSelector: Expression[Func[TSource, IEnumerable[TCollection]]], resultSelector: Expression[Func[TSource, TCollection, TResult]]) -> IQueryable[TResult]
        """
        ...

    @staticmethod
    def SequenceEqual(source1:IQueryable, source2:IEnumerable, comparer:IEqualityComparer = ...) -> bool:
        """
        SequenceEqual[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> bool
        SequenceEqual[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> bool
        """
        ...

    @staticmethod
    def Single(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        Single[TSource](source: IQueryable[TSource]) -> TSource
        Single[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def SingleOrDefault(source:IQueryable, predicate:Expression = ...): # -> TSource
        """
        SingleOrDefault[TSource](source: IQueryable[TSource]) -> TSource
        SingleOrDefault[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> TSource
        """
        ...

    @staticmethod
    def Skip(source:IQueryable, count:int) -> IQueryable:
        """ Skip[TSource](source: IQueryable[TSource], count: int) -> IQueryable[TSource] """
        ...

    @staticmethod
    def SkipWhile(source:IQueryable, predicate:Expression) -> IQueryable:
        """
        SkipWhile[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> IQueryable[TSource]
        SkipWhile[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def Sum(source:IQueryable, selector:Expression = ...) -> Nullable:
        """
        Sum(source: IQueryable[int]) -> int
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[float]]]) -> Nullable[float]
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, float]]) -> float
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Single]]]) -> Nullable[Single]
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Single]]) -> Single
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Int64]]]) -> Nullable[Int64]
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Int64]]) -> Int64
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[int]]]) -> Nullable[int]
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, int]]) -> int
        Sum(source: IQueryable[Nullable[Decimal]]) -> Nullable[Decimal]
        Sum(source: IQueryable[Decimal]) -> Decimal
        Sum(source: IQueryable[Nullable[float]]) -> Nullable[float]
        Sum(source: IQueryable[float]) -> float
        Sum(source: IQueryable[Nullable[Single]]) -> Nullable[Single]
        Sum(source: IQueryable[Single]) -> Single
        Sum(source: IQueryable[Nullable[Int64]]) -> Nullable[Int64]
        Sum(source: IQueryable[Int64]) -> Int64
        Sum(source: IQueryable[Nullable[int]]) -> Nullable[int]
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Decimal]]) -> Decimal
        Sum[TSource](source: IQueryable[TSource], selector: Expression[Func[TSource, Nullable[Decimal]]]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def Take(source:IQueryable, count:int) -> IQueryable:
        """ Take[TSource](source: IQueryable[TSource], count: int) -> IQueryable[TSource] """
        ...

    @staticmethod
    def TakeWhile(source:IQueryable, predicate:Expression) -> IQueryable:
        """
        TakeWhile[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> IQueryable[TSource]
        TakeWhile[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def ThenBy(source:IOrderedQueryable, keySelector:Expression, comparer:IComparer = ...) -> IOrderedQueryable:
        """
        ThenBy[(TSource, TKey)](source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]) -> IOrderedQueryable[TSource]
        ThenBy[(TSource, TKey)](source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], comparer: IComparer[TKey]) -> IOrderedQueryable[TSource]
        """
        ...

    @staticmethod
    def ThenByDescending(source:IOrderedQueryable, keySelector:Expression, comparer:IComparer = ...) -> IOrderedQueryable:
        """
        ThenByDescending[(TSource, TKey)](source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]]) -> IOrderedQueryable[TSource]
        ThenByDescending[(TSource, TKey)](source: IOrderedQueryable[TSource], keySelector: Expression[Func[TSource, TKey]], comparer: IComparer[TKey]) -> IOrderedQueryable[TSource]
        """
        ...

    @staticmethod
    def Union(source1:IQueryable, source2:IEnumerable, comparer:IEqualityComparer = ...) -> IQueryable:
        """
        Union[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource]) -> IQueryable[TSource]
        Union[TSource](source1: IQueryable[TSource], source2: IEnumerable[TSource], comparer: IEqualityComparer[TSource]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def Where(source:IQueryable, predicate:Expression) -> IQueryable:
        """
        Where[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, bool]]) -> IQueryable[TSource]
        Where[TSource](source: IQueryable[TSource], predicate: Expression[Func[TSource, int, bool]]) -> IQueryable[TSource]
        """
        ...

    @staticmethod
    def Zip(source1:IQueryable, source2:IEnumerable, resultSelector:Expression) -> IQueryable:
        """ Zip[(TFirst, TSecond, TResult)](source1: IQueryable[TFirst], source2: IEnumerable[TSecond], resultSelector: Expression[Func[TFirst, TSecond, TResult]]) -> IQueryable[TResult] """
        ...

    __all__: list = ...


# variables with complex values

