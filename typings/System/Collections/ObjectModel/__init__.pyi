# encoding: utf-8
# module System.Collections.ObjectModel calls itself ObjectModel
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections import (IDictionary, IEnumerator, IEqualityComparer, 
    IList)

from System.Collections.Generic import IReadOnlyDictionary, IReadOnlyList

from System.Collections.Specialized import INotifyCollectionChanged

from System.ComponentModel import INotifyPropertyChanged

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class Collection(IReadOnlyList, IList): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'ICollection'>, <type 'object'>
    """
    Collection[T]()
    Collection[T](list: IList[T])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Collection[T]) -> int """
        ...

    @property
    def Items(self):
        ...


    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: Collection[T]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: Collection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Collection[T]) -> IEnumerator[T] """
        ...

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: Collection[T], index: int, item: T) """
        ...

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: Collection[T], index: int) """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: Collection[T], index: int, item: T) """
        ...


class KeyedCollection(Collection): # skipped bases: <type 'IReadOnlyList[TItem]'>, <type 'IList[TItem]'>, <type 'IEnumerable'>, <type 'IEnumerable[TItem]'>, <type 'IReadOnlyCollection[TItem]'>, <type 'ICollection[TItem]'>, <type 'IList'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Comparer(self) -> IEqualityComparer:
        """ Get: Comparer(self: KeyedCollection[TKey, TItem]) -> IEqualityComparer[TKey] """
        ...

    @property
    def Dictionary(self):
        ...


    def ChangeItemKey(self, *args): #cannot find CLR method
        """ ChangeItemKey(self: KeyedCollection[TKey, TItem], item: TItem, newKey: TKey) """
        ...

    def GetKeyForItem(self, *args): #cannot find CLR method
        """ GetKeyForItem(self: KeyedCollection[TKey, TItem], item: TItem) -> TKey """
        ...


class ObservableCollection(INotifyCollectionChanged, Collection, INotifyPropertyChanged): # skipped bases: <type 'IReadOnlyList[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable[T]'>, <type 'ICollection'>, <type 'object'>
    """
    ObservableCollection[T]()
    ObservableCollection[T](list: List[T])
    ObservableCollection[T](collection: IEnumerable[T])
    """
    def BlockReentrancy(self, *args): #cannot find CLR method
        """ BlockReentrancy(self: ObservableCollection[T]) -> IDisposable """
        ...

    def CheckReentrancy(self, *args): #cannot find CLR method
        """ CheckReentrancy(self: ObservableCollection[T]) """
        ...

    def Move(self, oldIndex:int, newIndex:int): # -> 
        """ Move(self: ObservableCollection[T], oldIndex: int, newIndex: int) """
        ...

    def MoveItem(self, *args): #cannot find CLR method
        """ MoveItem(self: ObservableCollection[T], oldIndex: int, newIndex: int) """
        ...

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """ OnCollectionChanged(self: ObservableCollection[T], e: NotifyCollectionChangedEventArgs) """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """ OnPropertyChanged(self: ObservableCollection[T], e: PropertyChangedEventArgs) """
        ...

    CollectionChanged = ...
    PropertyChanged = ...


class ReadOnlyCollection(IReadOnlyList, IList): # skipped bases: <type 'ICollection[T]'>, <type 'IEnumerable[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ReadOnlyCollection[T](list: IList[T]) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReadOnlyCollection[T]) -> int """
        ...

    @property
    def Items(self):
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlyCollection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReadOnlyCollection[T]) -> IEnumerator[T] """
        ...


class ReadOnlyDictionary(IDictionary, IReadOnlyDictionary): # skipped bases: <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IReadOnlyCollection[KeyValuePair[TKey, TValue]]'>, <type 'object'>
    """ ReadOnlyDictionary[TKey, TValue](dictionary: IDictionary[TKey, TValue]) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReadOnlyDictionary[TKey, TValue]) -> int """
        ...

    @property
    def Dictionary(self):
        ...


    def KeyCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def ValueCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class ReadOnlyObservableCollection(ReadOnlyCollection, INotifyCollectionChanged, INotifyPropertyChanged): # skipped bases: <type 'IList[T]'>, <type 'ICollection[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[T]'>, <type 'IEnumerable[T]'>, <type 'ICollection'>, <type 'object'>
    """ ReadOnlyObservableCollection[T](list: ObservableCollection[T]) """
    def OnCollectionChanged(self, *args): #cannot find CLR method
        """ OnCollectionChanged(self: ReadOnlyObservableCollection[T], args: NotifyCollectionChangedEventArgs) """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """ OnPropertyChanged(self: ReadOnlyObservableCollection[T], args: PropertyChangedEventArgs) """
        ...

    CollectionChanged = ...
    PropertyChanged = ...


