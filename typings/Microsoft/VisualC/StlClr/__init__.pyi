# encoding: utf-8
# module Microsoft.VisualC.StlClr calls itself StlClr
# from Microsoft.VisualC.STLCLR, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualC.StlClr.Generic import (ContainerBidirectionalIterator, 
    ContainerRandomAccessIterator, IBidirectionalContainer, 
    IRandomAccessContainer, ReverseBidirectionalIterator, 
    ReverseRandomAccessIterator)

from System import (AsyncCallback, IAsyncResult, ICloneable, 
    MulticastDelegate, Single, UInt32)

from System.Collections import ICollection, IEnumerable, IEnumerator

"""The following names are not found in the module: (
    GenericPair, ContainerBidirectionalIterator, TArg, TArg1, TArg2, TCont, 
    TKey, TResult, TValue, field#)
"""

# no functions
# classes

class BinaryDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BinaryDelegate[TArg1, TArg2, TResult](A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, __unnamed000, __unnamed001, callback:AsyncCallback, obj:object) -> IAsyncResult: # Not found arg types: {'__unnamed000': 'TArg1', '__unnamed001': 'TArg2'}
        """ BeginInvoke(self: BinaryDelegate[TArg1, TArg2, TResult], __unnamed000: TArg1, __unnamed001: TArg2, callback: AsyncCallback, obj: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> TResult
        """ EndInvoke(self: BinaryDelegate[TArg1, TArg2, TResult], result: IAsyncResult) -> TResult """
        ...

    def Invoke(self, A_0, A_1): # -> TResult # Not found arg types: {'A_0': 'TArg1', 'A_1': 'TArg2'}
        """ Invoke(self: BinaryDelegate[TArg1, TArg2, TResult], A_0: TArg1, A_1: TArg2) -> TResult """
        ...


class DequeEnumerator(DequeEnumeratorBase, IEnumerator): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ DequeEnumerator[TValue](_Cont: IDeque[TValue], _First: int) """
    def Dispose(self): # -> 
        """ Dispose(self: DequeEnumerator[TValue]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TValue](enumerator: IEnumerator[TValue], value: TValue) -> bool """
        ...


class DequeEnumeratorBase(IEnumerator): # skipped bases: <type 'object'>
    """ DequeEnumeratorBase[TValue](_Cont: IDeque[TValue], _First: int) """
    pass

class GenericPair: # skipped bases: <type 'object'>, <type 'object'>
    """
    GenericPair[TValue1, TValue2]()
    GenericPair[TValue1, TValue2](_Right: GenericPair[TValue1, TValue2])
    GenericPair[TValue1, TValue2](_Right: KeyValuePair[TValue1, TValue2]) -> KeyValuePair[TValue1, TValue2]
    GenericPair[TValue1, TValue2](_Val1: TValue1)
    GenericPair[TValue1, TValue2](_Val1: TValue1, _Val2: TValue2)
    """
    def Equals(self, _Right_arg:object) -> bool:
        """ Equals(self: GenericPair[TValue1, TValue2], _Right_arg: object) -> bool """
        ...

    def swap(self, _Right:GenericPair): # -> 
        """ swap(self: GenericPair[TValue1, TValue2], _Right: GenericPair[TValue1, TValue2]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    first = ...
    second = ...


class HashEnumerator(IEnumerator, HashEnumeratorBase): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ HashEnumerator[TKey, TValue](_First: INode[TValue]) """
    def Dispose(self): # -> 
        """ Dispose(self: HashEnumerator[TKey, TValue]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TValue](enumerator: IEnumerator[TValue], value: TValue) -> bool """
        ...


class HashEnumeratorBase(IEnumerator): # skipped bases: <type 'object'>
    """ HashEnumeratorBase[TKey, TValue](_First: INode[TValue]) """
    pass

class IDeque(IRandomAccessContainer, ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def back_item(self): # -> TValue
        """
        Get: back_item(self: IDeque[TValue]) -> TValue
        Set: back_item(self: IDeque[TValue]) = value
        """
        ...

    @property
    def front_item(self): # -> TValue
        """
        Get: front_item(self: IDeque[TValue]) -> TValue
        Set: front_item(self: IDeque[TValue]) = value
        """
        ...


    def assign(self, *__args:IEnumerable): # -> 
        """ assign(self: IDeque[TValue], _Count: int, _Val: TValue)assign(self: IDeque[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])assign(self: IDeque[TValue], _Right: IEnumerable) """
        ...

    def at(self, _Pos:int): # -> TValue
        """ at(self: IDeque[TValue], _Pos: int) -> TValue """
        ...

    def back(self): # -> TValue
        """ back(self: IDeque[TValue]) -> TValue """
        ...

    def begin(self) -> ContainerRandomAccessIterator:
        """ begin(self: IDeque[TValue], : ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue] """
        ...

    def begin_bias(self) -> int:
        """ begin_bias(self: IDeque[TValue]) -> int """
        ...

    def clear(self): # -> 
        """ clear(self: IDeque[TValue]) """
        ...

    def empty(self) -> bool:
        """ empty(self: IDeque[TValue]) -> bool """
        ...

    def end(self) -> ContainerRandomAccessIterator:
        """ end(self: IDeque[TValue], : ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue] """
        ...

    def end_bias(self) -> int:
        """ end_bias(self: IDeque[TValue]) -> int """
        ...

    def erase(self, *__args) -> ContainerRandomAccessIterator:
        """
        erase(self: IDeque[TValue], : ContainerRandomAccessIterator[TValue], _Where: ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue]
        erase(self: IDeque[TValue], : ContainerRandomAccessIterator[TValue], _First_iter: ContainerRandomAccessIterator[TValue], _Last_iter: ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue]
        """
        ...

    def front(self): # -> TValue
        """ front(self: IDeque[TValue]) -> TValue """
        ...

    def get_generation(self) -> UInt32:
        """ get_generation(self: IDeque[TValue]) -> UInt32 """
        ...

    def insert(self, *__args) -> ContainerRandomAccessIterator:
        """
        insert(self: IDeque[TValue], : ContainerRandomAccessIterator[TValue], _Where: ContainerRandomAccessIterator[TValue], _Val: TValue) -> ContainerRandomAccessIterator[TValue]
        insert(self: IDeque[TValue], _Where: ContainerRandomAccessIterator[TValue], _Count: int, _Val: TValue)insert(self: IDeque[TValue], _Where: ContainerRandomAccessIterator[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])insert(self: IDeque[TValue], _Where_iter: ContainerRandomAccessIterator[TValue], _Right: IEnumerable)
        """
        ...

    def pop_back(self): # -> 
        """ pop_back(self: IDeque[TValue]) """
        ...

    def pop_front(self): # -> 
        """ pop_front(self: IDeque[TValue]) """
        ...

    def push_back(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push_back(self: IDeque[TValue], _Val: TValue) """
        ...

    def push_front(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push_front(self: IDeque[TValue], _Val: TValue) """
        ...

    def rbegin(self) -> ReverseRandomAccessIterator:
        """ rbegin(self: IDeque[TValue], : ReverseRandomAccessIterator[TValue]) -> ReverseRandomAccessIterator[TValue] """
        ...

    def rend(self) -> ReverseRandomAccessIterator:
        """ rend(self: IDeque[TValue], : ReverseRandomAccessIterator[TValue]) -> ReverseRandomAccessIterator[TValue] """
        ...

    def resize(self, _Newsize:int, _Val = ...): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ resize(self: IDeque[TValue], _Newsize: int)resize(self: IDeque[TValue], _Newsize: int, _Val: TValue) """
        ...

    def size(self) -> int:
        """ size(self: IDeque[TValue]) -> int """
        ...

    def swap(self, A_0:IDeque): # -> 
        """ swap(self: IDeque[TValue], A_0: IDeque[TValue]) """
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


class IHash(IBidirectionalContainer, ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def begin(self) -> ContainerBidirectionalIterator:
        """ begin(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def bucket_count(self) -> int:
        """ bucket_count(self: IHash[TKey, TValue]) -> int """
        ...

    def clear(self): # -> 
        """ clear(self: IHash[TKey, TValue]) """
        ...

    def count(self, _Keyval) -> int: # Not found arg types: {'_Keyval': 'TKey'}
        """ count(self: IHash[TKey, TValue], _Keyval: TKey) -> int """
        ...

    def empty(self) -> bool:
        """ empty(self: IHash[TKey, TValue]) -> bool """
        ...

    def end(self) -> ContainerBidirectionalIterator:
        """ end(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def equal_range(self, _Keyval): # -> GenericPair, ContainerBidirectionalIterator
        """ equal_range(self: IHash[TKey, TValue], : GenericPair[ContainerBidirectionalIterator[TValue], ContainerBidirectionalIterator[TValue]], _Keyval: TKey) -> GenericPair[ContainerBidirectionalIterator[TValue], ContainerBidirectionalIterator[TValue]] """
        ...

    def erase(self, *__args) -> int: # Not found arg types: {'*__args': 'TKey'}
        """
        erase(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        erase(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _First_iter: ContainerBidirectionalIterator[TValue], _Last_iter: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        erase(self: IHash[TKey, TValue], _Keyval: TKey) -> int
        """
        ...

    def find(self, _Keyval) -> ContainerBidirectionalIterator:
        """ find(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def hash_delegate(self) -> UnaryDelegate:
        """ hash_delegate(self: IHash[TKey, TValue]) -> UnaryDelegate[TKey, int] """
        ...

    def insert(self, *__args:IEnumerable): # -> 
        """
        insert(self: IHash[TKey, TValue], : GenericPair[ContainerBidirectionalIterator[TValue], bool], _Val: TValue) -> GenericPair[ContainerBidirectionalIterator[TValue], bool]
        insert(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue], _Val: TValue) -> ContainerBidirectionalIterator[TValue]
        insert(self: IHash[TKey, TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])insert(self: IHash[TKey, TValue], _Right: IEnumerable)
        """
        ...

    def key_comp(self) -> BinaryDelegate:
        """ key_comp(self: IHash[TKey, TValue]) -> BinaryDelegate[TKey, TKey, bool] """
        ...

    def load_factor(self) -> Single:
        """ load_factor(self: IHash[TKey, TValue]) -> Single """
        ...

    def lower_bound(self, _Keyval) -> ContainerBidirectionalIterator:
        """ lower_bound(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def max_load_factor(self, _Newmax:Single = ...): # -> 
        """
        max_load_factor(self: IHash[TKey, TValue]) -> Single
        max_load_factor(self: IHash[TKey, TValue], _Newmax: Single)
        """
        ...

    def rbegin(self) -> ReverseBidirectionalIterator:
        """ rbegin(self: IHash[TKey, TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def rehash(self, _Buckets:int): # -> 
        """ rehash(self: IHash[TKey, TValue], _Buckets: int) """
        ...

    def rend(self) -> ReverseBidirectionalIterator:
        """ rend(self: IHash[TKey, TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def size(self) -> int:
        """ size(self: IHash[TKey, TValue]) -> int """
        ...

    def swap(self, _Right:IHash): # -> 
        """ swap(self: IHash[TKey, TValue], _Right: IHash[TKey, TValue]) """
        ...

    def upper_bound(self, _Keyval) -> ContainerBidirectionalIterator:
        """ upper_bound(self: IHash[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def value_comp(self) -> BinaryDelegate:
        """ value_comp(self: IHash[TKey, TValue]) -> BinaryDelegate[TValue, TValue, bool] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IList(IBidirectionalContainer, ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def back_item(self): # -> TValue
        """
        Get: back_item(self: IList[TValue]) -> TValue
        Set: back_item(self: IList[TValue]) = value
        """
        ...

    @property
    def front_item(self): # -> TValue
        """
        Get: front_item(self: IList[TValue]) -> TValue
        Set: front_item(self: IList[TValue]) = value
        """
        ...


    def assign(self, *__args:IEnumerable): # -> 
        """ assign(self: IList[TValue], _Count: int, _Val: TValue)assign(self: IList[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])assign(self: IList[TValue], _Right: IEnumerable) """
        ...

    def back(self): # -> TValue
        """ back(self: IList[TValue]) -> TValue """
        ...

    def begin(self) -> ContainerBidirectionalIterator:
        """ begin(self: IList[TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def clear(self): # -> 
        """ clear(self: IList[TValue]) """
        ...

    def empty(self) -> bool:
        """ empty(self: IList[TValue]) -> bool """
        ...

    def end(self) -> ContainerBidirectionalIterator:
        """ end(self: IList[TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def erase(self, *__args) -> ContainerBidirectionalIterator:
        """
        erase(self: IList[TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        erase(self: IList[TValue], : ContainerBidirectionalIterator[TValue], _First_iter: ContainerBidirectionalIterator[TValue], _Last_iter: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        """
        ...

    def front(self): # -> TValue
        """ front(self: IList[TValue]) -> TValue """
        ...

    def insert(self, *__args) -> ContainerBidirectionalIterator:
        """
        insert(self: IList[TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue], _Val: TValue) -> ContainerBidirectionalIterator[TValue]
        insert(self: IList[TValue], _Where: ContainerBidirectionalIterator[TValue], _Count: int, _Val: TValue)insert(self: IList[TValue], _Where: ContainerBidirectionalIterator[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])insert(self: IList[TValue], _Where_iter: ContainerBidirectionalIterator[TValue], _Right: IEnumerable)
        """
        ...

    def merge(self, _Right:IList, _Pred:BinaryDelegate): # -> 
        """ merge(self: IList[TValue], _Right: IList[TValue], _Pred: BinaryDelegate[TValue, TValue, bool]) """
        ...

    def pop_back(self): # -> 
        """ pop_back(self: IList[TValue]) """
        ...

    def pop_front(self): # -> 
        """ pop_front(self: IList[TValue]) """
        ...

    def push_back(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push_back(self: IList[TValue], _Val: TValue) """
        ...

    def push_front(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push_front(self: IList[TValue], _Val: TValue) """
        ...

    def rbegin(self) -> ReverseBidirectionalIterator:
        """ rbegin(self: IList[TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def remove(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ remove(self: IList[TValue], _Val: TValue) """
        ...

    def remove_if(self, _Pred:UnaryDelegate): # -> 
        """ remove_if(self: IList[TValue], _Pred: UnaryDelegate[TValue, bool]) """
        ...

    def rend(self) -> ReverseBidirectionalIterator:
        """ rend(self: IList[TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def resize(self, _Newsize:int, _Val = ...): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ resize(self: IList[TValue], _Newsize: int)resize(self: IList[TValue], _Newsize: int, _Val: TValue) """
        ...

    def reverse(self): # -> 
        """ reverse(self: IList[TValue]) """
        ...

    def size(self) -> int:
        """ size(self: IList[TValue]) -> int """
        ...

    def sort(self, _Pred:BinaryDelegate): # -> 
        """ sort(self: IList[TValue], _Pred: BinaryDelegate[TValue, TValue, bool]) """
        ...

    def splice(self, _Where:ContainerBidirectionalIterator, _Right:IList, _First:ContainerBidirectionalIterator = ..., _Last:ContainerBidirectionalIterator = ...): # -> 
        """ splice(self: IList[TValue], _Where: ContainerBidirectionalIterator[TValue], _Right: IList[TValue])splice(self: IList[TValue], _Where: ContainerBidirectionalIterator[TValue], _Right: IList[TValue], _First: ContainerBidirectionalIterator[TValue])splice(self: IList[TValue], _Where: ContainerBidirectionalIterator[TValue], _Right: IList[TValue], _First: ContainerBidirectionalIterator[TValue], _Last: ContainerBidirectionalIterator[TValue]) """
        ...

    def swap(self, _Right:IList): # -> 
        """ swap(self: IList[TValue], _Right: IList[TValue]) """
        ...

    def unique(self, _Pred:BinaryDelegate): # -> 
        """ unique(self: IList[TValue], _Pred: BinaryDelegate[TValue, TValue, bool]) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IPriorityQueue(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def top_item(self): # -> TValue
        """
        Get: top_item(self: IPriorityQueue[TValue, TCont]) -> TValue
        Set: top_item(self: IPriorityQueue[TValue, TCont]) = value
        """
        ...


    def assign(self, _Right:IPriorityQueue): # -> 
        """ assign(self: IPriorityQueue[TValue, TCont], _Right: IPriorityQueue[TValue, TCont]) """
        ...

    def empty(self) -> bool:
        """ empty(self: IPriorityQueue[TValue, TCont]) -> bool """
        ...

    def get_container(self): # -> TCont
        """ get_container(self: IPriorityQueue[TValue, TCont]) -> TCont """
        ...

    def pop(self): # -> 
        """ pop(self: IPriorityQueue[TValue, TCont]) """
        ...

    def push(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push(self: IPriorityQueue[TValue, TCont], _Val: TValue) """
        ...

    def size(self) -> int:
        """ size(self: IPriorityQueue[TValue, TCont]) -> int """
        ...

    def top(self): # -> TValue
        """ top(self: IPriorityQueue[TValue, TCont]) -> TValue """
        ...

    def value_comp(self) -> BinaryDelegate:
        """ value_comp(self: IPriorityQueue[TValue, TCont]) -> BinaryDelegate[TValue, TValue, bool] """
        ...


class IQueue(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    def assign(self, _Right:IQueue): # -> 
        """ assign(self: IQueue[TValue, TCont], _Right: IQueue[TValue, TCont]) """
        ...

    def back(self): # -> TValue
        """ back(self: IQueue[TValue, TCont]) -> TValue """
        ...

    def empty(self) -> bool:
        """ empty(self: IQueue[TValue, TCont]) -> bool """
        ...

    def front(self): # -> TValue
        """ front(self: IQueue[TValue, TCont]) -> TValue """
        ...

    def get_container(self): # -> TCont
        """ get_container(self: IQueue[TValue, TCont]) -> TCont """
        ...

    def pop(self): # -> 
        """ pop(self: IQueue[TValue, TCont]) """
        ...

    def push(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push(self: IQueue[TValue, TCont], _Val: TValue) """
        ...

    def size(self) -> int:
        """ size(self: IQueue[TValue, TCont]) -> int """
        ...


class IStack(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def top_item(self): # -> TValue
        """
        Get: top_item(self: IStack[TValue, TCont]) -> TValue
        Set: top_item(self: IStack[TValue, TCont]) = value
        """
        ...


    def assign(self, _Right:IStack): # -> 
        """ assign(self: IStack[TValue, TCont], _Right: IStack[TValue, TCont]) """
        ...

    def empty(self) -> bool:
        """ empty(self: IStack[TValue, TCont]) -> bool """
        ...

    def get_container(self): # -> TCont
        """ get_container(self: IStack[TValue, TCont]) -> TCont """
        ...

    def pop(self): # -> 
        """ pop(self: IStack[TValue, TCont]) """
        ...

    def push(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push(self: IStack[TValue, TCont], _Val: TValue) """
        ...

    def size(self) -> int:
        """ size(self: IStack[TValue, TCont]) -> int """
        ...

    def top(self): # -> TValue
        """ top(self: IStack[TValue, TCont]) -> TValue """
        ...


class ITree(IBidirectionalContainer, ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def begin(self) -> ContainerBidirectionalIterator:
        """ begin(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def clear(self): # -> 
        """ clear(self: ITree[TKey, TValue]) """
        ...

    def count(self, _Keyval) -> int: # Not found arg types: {'_Keyval': 'TKey'}
        """ count(self: ITree[TKey, TValue], _Keyval: TKey) -> int """
        ...

    def empty(self) -> bool:
        """ empty(self: ITree[TKey, TValue]) -> bool """
        ...

    def end(self) -> ContainerBidirectionalIterator:
        """ end(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue] """
        ...

    def equal_range(self, _Keyval): # -> GenericPair, ContainerBidirectionalIterator
        """ equal_range(self: ITree[TKey, TValue], : GenericPair[ContainerBidirectionalIterator[TValue], ContainerBidirectionalIterator[TValue]], _Keyval: TKey) -> GenericPair[ContainerBidirectionalIterator[TValue], ContainerBidirectionalIterator[TValue]] """
        ...

    def erase(self, *__args) -> int: # Not found arg types: {'*__args': 'TKey'}
        """
        erase(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        erase(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _First_iter: ContainerBidirectionalIterator[TValue], _Last_iter: ContainerBidirectionalIterator[TValue]) -> ContainerBidirectionalIterator[TValue]
        erase(self: ITree[TKey, TValue], _Keyval: TKey) -> int
        """
        ...

    def find(self, _Keyval) -> ContainerBidirectionalIterator:
        """ find(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def insert(self, *__args:IEnumerable): # -> 
        """
        insert(self: ITree[TKey, TValue], : GenericPair[ContainerBidirectionalIterator[TValue], bool], _Val: TValue) -> GenericPair[ContainerBidirectionalIterator[TValue], bool]
        insert(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Where: ContainerBidirectionalIterator[TValue], _Val: TValue) -> ContainerBidirectionalIterator[TValue]
        insert(self: ITree[TKey, TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])insert(self: ITree[TKey, TValue], _Right: IEnumerable[TValue])
        """
        ...

    def key_comp(self) -> BinaryDelegate:
        """ key_comp(self: ITree[TKey, TValue]) -> BinaryDelegate[TKey, TKey, bool] """
        ...

    def lower_bound(self, _Keyval) -> ContainerBidirectionalIterator:
        """ lower_bound(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def rbegin(self) -> ReverseBidirectionalIterator:
        """ rbegin(self: ITree[TKey, TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def rend(self) -> ReverseBidirectionalIterator:
        """ rend(self: ITree[TKey, TValue], : ReverseBidirectionalIterator[TValue]) -> ReverseBidirectionalIterator[TValue] """
        ...

    def size(self) -> int:
        """ size(self: ITree[TKey, TValue]) -> int """
        ...

    def swap(self, _Right:ITree): # -> 
        """ swap(self: ITree[TKey, TValue], _Right: ITree[TKey, TValue]) """
        ...

    def upper_bound(self, _Keyval) -> ContainerBidirectionalIterator:
        """ upper_bound(self: ITree[TKey, TValue], : ContainerBidirectionalIterator[TValue], _Keyval: TKey) -> ContainerBidirectionalIterator[TValue] """
        ...

    def value_comp(self) -> BinaryDelegate:
        """ value_comp(self: ITree[TKey, TValue]) -> BinaryDelegate[TValue, TValue, bool] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IVector(IRandomAccessContainer, ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def back_item(self): # -> TValue
        """
        Get: back_item(self: IVector[TValue]) -> TValue
        Set: back_item(self: IVector[TValue]) = value
        """
        ...

    @property
    def front_item(self): # -> TValue
        """
        Get: front_item(self: IVector[TValue]) -> TValue
        Set: front_item(self: IVector[TValue]) = value
        """
        ...


    def assign(self, *__args:IEnumerable): # -> 
        """ assign(self: IVector[TValue], _Count: int, _Val: TValue)assign(self: IVector[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])assign(self: IVector[TValue], _Right: IEnumerable) """
        ...

    def at(self, _Pos:int): # -> TValue
        """ at(self: IVector[TValue], _Pos: int) -> TValue """
        ...

    def back(self): # -> TValue
        """ back(self: IVector[TValue]) -> TValue """
        ...

    def begin(self) -> ContainerRandomAccessIterator:
        """ begin(self: IVector[TValue], : ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue] """
        ...

    def capacity(self) -> int:
        """ capacity(self: IVector[TValue]) -> int """
        ...

    def clear(self): # -> 
        """ clear(self: IVector[TValue]) """
        ...

    def empty(self) -> bool:
        """ empty(self: IVector[TValue]) -> bool """
        ...

    def end(self) -> ContainerRandomAccessIterator:
        """ end(self: IVector[TValue], : ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue] """
        ...

    def erase(self, *__args) -> ContainerRandomAccessIterator:
        """
        erase(self: IVector[TValue], : ContainerRandomAccessIterator[TValue], _Where: ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue]
        erase(self: IVector[TValue], : ContainerRandomAccessIterator[TValue], _First_iter: ContainerRandomAccessIterator[TValue], _Last_iter: ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue]
        """
        ...

    def front(self): # -> TValue
        """ front(self: IVector[TValue]) -> TValue """
        ...

    def get_generation(self) -> UInt32:
        """ get_generation(self: IVector[TValue]) -> UInt32 """
        ...

    def insert(self, *__args) -> ContainerRandomAccessIterator:
        """
        insert(self: IVector[TValue], : ContainerRandomAccessIterator[TValue], _Where: ContainerRandomAccessIterator[TValue], _Val: TValue) -> ContainerRandomAccessIterator[TValue]
        insert(self: IVector[TValue], _Where: ContainerRandomAccessIterator[TValue], _Count: int, _Val: TValue)insert(self: IVector[TValue], _Where: ContainerRandomAccessIterator[TValue], _First: IInputIterator[TValue], _Last: IInputIterator[TValue])insert(self: IVector[TValue], _Where_iter: ContainerRandomAccessIterator[TValue], _Right: IEnumerable)
        """
        ...

    def pop_back(self): # -> 
        """ pop_back(self: IVector[TValue]) """
        ...

    def push_back(self, _Val): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ push_back(self: IVector[TValue], _Val: TValue) """
        ...

    def rbegin(self) -> ReverseRandomAccessIterator:
        """ rbegin(self: IVector[TValue], : ReverseRandomAccessIterator[TValue]) -> ReverseRandomAccessIterator[TValue] """
        ...

    def rend(self) -> ReverseRandomAccessIterator:
        """ rend(self: IVector[TValue], : ReverseRandomAccessIterator[TValue]) -> ReverseRandomAccessIterator[TValue] """
        ...

    def reserve(self, _Capacity:int): # -> 
        """ reserve(self: IVector[TValue], _Capacity: int) """
        ...

    def resize(self, _Newsize:int, _Val = ...): # ->  # Not found arg types: {'_Val': 'TValue'}
        """ resize(self: IVector[TValue], _Newsize: int)resize(self: IVector[TValue], _Newsize: int, _Val: TValue) """
        ...

    def size(self) -> int:
        """ size(self: IVector[TValue]) -> int """
        ...

    def swap(self, A_0:IVector): # -> 
        """ swap(self: IVector[TValue], A_0: IVector[TValue]) """
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


class ListEnumerator(IEnumerator, ListEnumeratorBase): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ ListEnumerator[TValue](_First: INode[TValue]) """
    def Dispose(self): # -> 
        """ Dispose(self: ListEnumerator[TValue]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TValue](enumerator: IEnumerator[TValue], value: TValue) -> bool """
        ...


class ListEnumeratorBase(IEnumerator): # skipped bases: <type 'object'>
    """ ListEnumeratorBase[TValue](_First: INode[TValue]) """
    pass

class TreeEnumerator(IEnumerator, TreeEnumeratorBase): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ TreeEnumerator[TKey, TValue](_First: INode[TValue]) """
    def Dispose(self): # -> 
        """ Dispose(self: TreeEnumerator[TKey, TValue]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TValue](enumerator: IEnumerator[TValue], value: TValue) -> bool """
        ...


class TreeEnumeratorBase(IEnumerator): # skipped bases: <type 'object'>
    """ TreeEnumeratorBase[TKey, TValue](_First: INode[TValue]) """
    pass

class UnaryDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UnaryDelegate[TArg, TResult](A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, __unnamed000, callback:AsyncCallback, obj:object) -> IAsyncResult: # Not found arg types: {'__unnamed000': 'TArg'}
        """ BeginInvoke(self: UnaryDelegate[TArg, TResult], __unnamed000: TArg, callback: AsyncCallback, obj: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> TResult
        """ EndInvoke(self: UnaryDelegate[TArg, TResult], result: IAsyncResult) -> TResult """
        ...

    def Invoke(self, A_0): # -> TResult # Not found arg types: {'A_0': 'TArg'}
        """ Invoke(self: UnaryDelegate[TArg, TResult], A_0: TArg) -> TResult """
        ...


class VectorEnumerator(IEnumerator, VectorEnumeratorBase): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ VectorEnumerator[TValue](_Cont: IVector[TValue], _First: int) """
    def Dispose(self): # -> 
        """ Dispose(self: VectorEnumerator[TValue]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TValue](enumerator: IEnumerator[TValue], value: TValue) -> bool """
        ...


class VectorEnumeratorBase(IEnumerator): # skipped bases: <type 'object'>
    """ VectorEnumeratorBase[TValue](_Cont: IVector[TValue], _First: int) """
    pass

# variables with complex values

