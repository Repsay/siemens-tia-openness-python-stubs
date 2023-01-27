# encoding: utf-8
# module Microsoft.VisualC.StlClr.Generic calls itself Generic
# from Microsoft.VisualC.STLCLR, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ICloneable, UInt32

"""The following names are not found in the module: TValue
"""

# no functions
# classes

class ConstContainerBidirectionalIterator(IBidirectionalIterator): # skipped bases: <type 'IInputIterator[TValue]'>, <type 'IForwardIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'ICloneable'>, <type 'IBaseIterator[TValue]'>, <type 'object'>
    """
    ConstContainerBidirectionalIterator[TValue]()
    ConstContainerBidirectionalIterator[TValue](_Right: ConstContainerBidirectionalIterator[TValue])
    ConstContainerBidirectionalIterator[TValue](_Node: INode[TValue])
    ConstContainerBidirectionalIterator[TValue](_Right: ContainerBidirectionalIterator[TValue])
    """
    def Clone(self) -> object:
        """ Clone(self: ConstContainerBidirectionalIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ConstContainerBidirectionalIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ConstContainerBidirectionalIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ConstContainerBidirectionalIterator[TValue], _Right: ConstContainerBidirectionalIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ConstContainerBidirectionalIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ConstContainerBidirectionalIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ConstContainerBidirectionalIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ConstContainerBidirectionalIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ConstContainerBidirectionalIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ConstContainerBidirectionalIterator[TValue]) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConstContainerRandomAccessIterator(IRandomAccessIterator): # skipped bases: <type 'IForwardIterator[TValue]'>, <type 'ICloneable'>, <type 'IBaseIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'IBidirectionalIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'object'>
    """
    ConstContainerRandomAccessIterator[TValue]()
    ConstContainerRandomAccessIterator[TValue](_Right: ConstContainerRandomAccessIterator[TValue])
    ConstContainerRandomAccessIterator[TValue](_Cont: IRandomAccessContainer[TValue], _Offset: int)
    ConstContainerRandomAccessIterator[TValue](_Right: ContainerRandomAccessIterator[TValue])
    """
    def Clone(self) -> object:
        """ Clone(self: ConstContainerRandomAccessIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ConstContainerRandomAccessIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ConstContainerRandomAccessIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ConstContainerRandomAccessIterator[TValue], _Right: ConstContainerRandomAccessIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ConstContainerRandomAccessIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ConstContainerRandomAccessIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ConstContainerRandomAccessIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ConstContainerRandomAccessIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ConstContainerRandomAccessIterator[TValue]) """
        ...

    def prev(self): # -> 
        """ prev(self: ConstContainerRandomAccessIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ConstContainerRandomAccessIterator[TValue]) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(: ConstContainerRandomAccessIterator[TValue], _Left: int, _Right: ConstContainerRandomAccessIterator[TValue]) -> ConstContainerRandomAccessIterator[TValue] """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...


class ConstReverseBidirectionalIterator(IBidirectionalIterator): # skipped bases: <type 'IInputIterator[TValue]'>, <type 'IBaseIterator[TValue]'>, <type 'IForwardIterator[TValue]'>, <type 'ICloneable'>, <type 'IOutputIterator[TValue]'>, <type 'object'>
    """
    ConstReverseBidirectionalIterator[TValue]()
    ConstReverseBidirectionalIterator[TValue](_Right: ConstReverseBidirectionalIterator[TValue])
    ConstReverseBidirectionalIterator[TValue](_Iter: IBidirectionalIterator[TValue])
    ConstReverseBidirectionalIterator[TValue](_Iter: ReverseBidirectionalIterator[TValue])
    """
    def base(self) -> IBidirectionalIterator:
        """ base(self: ConstReverseBidirectionalIterator[TValue]) -> IBidirectionalIterator[TValue] """
        ...

    def Clone(self) -> object:
        """ Clone(self: ConstReverseBidirectionalIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ConstReverseBidirectionalIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ConstReverseBidirectionalIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ConstReverseBidirectionalIterator[TValue], _Right: ConstReverseBidirectionalIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ConstReverseBidirectionalIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ConstReverseBidirectionalIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ConstReverseBidirectionalIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ConstReverseBidirectionalIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ConstReverseBidirectionalIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ConstReverseBidirectionalIterator[TValue]) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConstReverseRandomAccessIterator(IRandomAccessIterator): # skipped bases: <type 'ICloneable'>, <type 'IBaseIterator[TValue]'>, <type 'IForwardIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'IBidirectionalIterator[TValue]'>, <type 'object'>
    """
    ConstReverseRandomAccessIterator[TValue]()
    ConstReverseRandomAccessIterator[TValue](_Right: ConstReverseRandomAccessIterator[TValue])
    ConstReverseRandomAccessIterator[TValue](_Iter: IRandomAccessIterator[TValue])
    ConstReverseRandomAccessIterator[TValue](_Iter: ReverseRandomAccessIterator[TValue])
    """
    def base(self) -> IRandomAccessIterator:
        """ base(self: ConstReverseRandomAccessIterator[TValue]) -> IRandomAccessIterator[TValue] """
        ...

    def Clone(self) -> object:
        """ Clone(self: ConstReverseRandomAccessIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ConstReverseRandomAccessIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ConstReverseRandomAccessIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ConstReverseRandomAccessIterator[TValue], _Right: ConstReverseRandomAccessIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ConstReverseRandomAccessIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ConstReverseRandomAccessIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ConstReverseRandomAccessIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ConstReverseRandomAccessIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ConstReverseRandomAccessIterator[TValue]) """
        ...

    def prev(self): # -> 
        """ prev(self: ConstReverseRandomAccessIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ConstReverseRandomAccessIterator[TValue]) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(: ConstReverseRandomAccessIterator[TValue], _Left: int, _Right: ConstReverseRandomAccessIterator[TValue]) -> ConstReverseRandomAccessIterator[TValue] """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...


class ContainerBidirectionalIterator(IBidirectionalIterator): # skipped bases: <type 'IForwardIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'IBaseIterator[TValue]'>, <type 'ICloneable'>, <type 'IOutputIterator[TValue]'>, <type 'object'>
    """
    ContainerBidirectionalIterator[TValue]()
    ContainerBidirectionalIterator[TValue](_Right: ContainerBidirectionalIterator[TValue])
    ContainerBidirectionalIterator[TValue](_Node: INode[TValue])
    """
    def Clone(self) -> object:
        """ Clone(self: ContainerBidirectionalIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ContainerBidirectionalIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ContainerBidirectionalIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ContainerBidirectionalIterator[TValue], _Right: ContainerBidirectionalIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ContainerBidirectionalIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ContainerBidirectionalIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ContainerBidirectionalIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ContainerBidirectionalIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ContainerBidirectionalIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ContainerBidirectionalIterator[TValue]) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ContainerRandomAccessIterator(IRandomAccessIterator): # skipped bases: <type 'IInputIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'ICloneable'>, <type 'IBaseIterator[TValue]'>, <type 'IBidirectionalIterator[TValue]'>, <type 'IForwardIterator[TValue]'>, <type 'object'>
    """
    ContainerRandomAccessIterator[TValue]()
    ContainerRandomAccessIterator[TValue](_Right: ContainerRandomAccessIterator[TValue])
    ContainerRandomAccessIterator[TValue](_Cont: IRandomAccessContainer[TValue], _Offset: int)
    """
    def Clone(self) -> object:
        """ Clone(self: ContainerRandomAccessIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ContainerRandomAccessIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ContainerRandomAccessIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ContainerRandomAccessIterator[TValue], _Right: ContainerRandomAccessIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ContainerRandomAccessIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ContainerRandomAccessIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ContainerRandomAccessIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ContainerRandomAccessIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ContainerRandomAccessIterator[TValue]) """
        ...

    def prev(self): # -> 
        """ prev(self: ContainerRandomAccessIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ContainerRandomAccessIterator[TValue]) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(: ContainerRandomAccessIterator[TValue], _Left: int, _Right: ContainerRandomAccessIterator[TValue]) -> ContainerRandomAccessIterator[TValue] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...


class IBaseIterator(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    def container(self) -> object:
        """ container(self: IBaseIterator[TValue]) -> object """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: IBaseIterator[TValue]) -> int """
        ...

    def get_node(self) -> object:
        """ get_node(self: IBaseIterator[TValue]) -> object """
        ...

    def next(self): # -> 
        """ next(self: IBaseIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: IBaseIterator[TValue]) -> bool """
        ...


class IBidirectionalContainer: # skipped bases: <type 'object'>
    """ no doc """
    def get_generation(self) -> UInt32:
        """ get_generation(self: IBidirectionalContainer[TValue]) -> UInt32 """
        ...


class IBidirectionalIterator(IForwardIterator): # skipped bases: <type 'IInputIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'ICloneable'>, <type 'IBaseIterator[TValue]'>, <type 'object'>
    """ no doc """
    def prev(self): # -> 
        """ prev(self: IBidirectionalIterator[TValue]) """
        ...


class IForwardIterator(IOutputIterator, IInputIterator): # skipped bases: <type 'IBaseIterator[TValue]'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    pass

class IInputIterator(IBaseIterator): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ no doc """
    def equal_to(self, A_0:IInputIterator) -> bool:
        """ equal_to(self: IInputIterator[TValue], A_0: IInputIterator[TValue]) -> bool """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: IInputIterator[TValue]) -> TValue """
        ...


class INode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def _Value(self): # -> TValue
        """
        Get: _Value(self: INode[TValue]) -> TValue
        Set: _Value(self: INode[TValue]) = value
        """
        ...


    def container(self) -> IBidirectionalContainer:
        """ container(self: INode[TValue]) -> IBidirectionalContainer[TValue] """
        ...

    def is_head(self) -> bool:
        """ is_head(self: INode[TValue]) -> bool """
        ...

    def next_node(self) -> INode:
        """ next_node(self: INode[TValue]) -> INode[TValue] """
        ...

    def prev_node(self) -> INode:
        """ prev_node(self: INode[TValue]) -> INode[TValue] """
        ...


class IOutputIterator(IBaseIterator): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ no doc """
    def get_ref(self): # -> TValue
        """ get_ref(self: IOutputIterator[TValue]) -> TValue """
        ...


class IRandomAccessContainer: # skipped bases: <type 'object'>
    """ no doc """
    def at_bias(self, A_0:int): # -> TValue
        """ at_bias(self: IRandomAccessContainer[TValue], A_0: int) -> TValue """
        ...

    def valid_bias(self, A_0:int) -> bool:
        """ valid_bias(self: IRandomAccessContainer[TValue], A_0: int) -> bool """
        ...


class IRandomAccessIterator(IBidirectionalIterator): # skipped bases: <type 'IBaseIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'ICloneable'>, <type 'IForwardIterator[TValue]'>, <type 'object'>
    """ no doc """
    def distance(self, _Right:IRandomAccessIterator) -> int:
        """ distance(self: IRandomAccessIterator[TValue], _Right: IRandomAccessIterator[TValue]) -> int """
        ...

    def less_than(self, _Right:IRandomAccessIterator) -> bool:
        """ less_than(self: IRandomAccessIterator[TValue], _Right: IRandomAccessIterator[TValue]) -> bool """
        ...

    def move(self, _Offset:int) -> int:
        """ move(self: IRandomAccessIterator[TValue], _Offset: int) -> int """
        ...


class ReverseBidirectionalIterator(IBidirectionalIterator): # skipped bases: <type 'IBaseIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'IOutputIterator[TValue]'>, <type 'IForwardIterator[TValue]'>, <type 'ICloneable'>, <type 'object'>
    """
    ReverseBidirectionalIterator[TValue]()
    ReverseBidirectionalIterator[TValue](_Right: ReverseBidirectionalIterator[TValue])
    ReverseBidirectionalIterator[TValue](_Iter: IBidirectionalIterator[TValue])
    """
    def base(self) -> IBidirectionalIterator:
        """ base(self: ReverseBidirectionalIterator[TValue]) -> IBidirectionalIterator[TValue] """
        ...

    def Clone(self) -> object:
        """ Clone(self: ReverseBidirectionalIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ReverseBidirectionalIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ReverseBidirectionalIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ReverseBidirectionalIterator[TValue], _Right: ReverseBidirectionalIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ReverseBidirectionalIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ReverseBidirectionalIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ReverseBidirectionalIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ReverseBidirectionalIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ReverseBidirectionalIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ReverseBidirectionalIterator[TValue]) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReverseRandomAccessIterator(IRandomAccessIterator): # skipped bases: <type 'IOutputIterator[TValue]'>, <type 'ICloneable'>, <type 'IForwardIterator[TValue]'>, <type 'IBaseIterator[TValue]'>, <type 'IInputIterator[TValue]'>, <type 'IBidirectionalIterator[TValue]'>, <type 'object'>
    """
    ReverseRandomAccessIterator[TValue]()
    ReverseRandomAccessIterator[TValue](_Right: ReverseRandomAccessIterator[TValue])
    ReverseRandomAccessIterator[TValue](_Iter: IRandomAccessIterator[TValue])
    """
    def base(self) -> IRandomAccessIterator:
        """ base(self: ReverseRandomAccessIterator[TValue]) -> IRandomAccessIterator[TValue] """
        ...

    def Clone(self) -> object:
        """ Clone(self: ReverseRandomAccessIterator[TValue]) -> object """
        ...

    def container(self) -> object:
        """ container(self: ReverseRandomAccessIterator[TValue]) -> object """
        ...

    def equal_to(self, _Right:IInputIterator) -> bool:
        """
        equal_to(self: ReverseRandomAccessIterator[TValue], _Right: IInputIterator[TValue]) -> bool
        equal_to(self: ReverseRandomAccessIterator[TValue], _Right: ReverseRandomAccessIterator[TValue]) -> bool
        """
        ...

    def get_bias(self) -> int:
        """ get_bias(self: ReverseRandomAccessIterator[TValue]) -> int """
        ...

    def get_cref(self): # -> TValue
        """ get_cref(self: ReverseRandomAccessIterator[TValue]) -> TValue """
        ...

    def get_node(self) -> object:
        """ get_node(self: ReverseRandomAccessIterator[TValue]) -> object """
        ...

    def get_ref(self): # -> TValue
        """ get_ref(self: ReverseRandomAccessIterator[TValue]) -> TValue """
        ...

    def next(self): # -> 
        """ next(self: ReverseRandomAccessIterator[TValue]) """
        ...

    def prev(self): # -> 
        """ prev(self: ReverseRandomAccessIterator[TValue]) """
        ...

    def valid(self) -> bool:
        """ valid(self: ReverseRandomAccessIterator[TValue]) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(: ReverseRandomAccessIterator[TValue], _Left: int, _Right: ReverseRandomAccessIterator[TValue]) -> ReverseRandomAccessIterator[TValue] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...


