# encoding: utf-8
# module System.Xml.Xsl.Runtime calls itself Runtime
# from System.Data.SqlXml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, DateTime, Decimal, Enum, Int64, Single, TimeSpan, 
    Type)

from System.Collections import IComparer, IEnumerator, IList

from System.Xml import XmlNameTable, XmlQualifiedName, XmlWriter

from System.Xml.Schema import XmlAtomicValue

from System.Xml.XPath import XPathItem, XPathNavigator, XPathNodeType

from typing import Tuple as Tuple_

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class AncestorDocOrderIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: AncestorDocOrderIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter, orSelf:bool): # -> 
        """ Create(self: AncestorDocOrderIterator, context: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: AncestorDocOrderIterator) -> bool """
        ...


class AncestorIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: AncestorIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter, orSelf:bool): # -> 
        """ Create(self: AncestorIterator, context: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: AncestorIterator) -> bool """
        ...


class AttributeContentIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: AttributeContentIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator): # -> 
        """ Create(self: AttributeContentIterator, context: XPathNavigator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: AttributeContentIterator) -> bool """
        ...


class AttributeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: AttributeIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator): # -> 
        """ Create(self: AttributeIterator, context: XPathNavigator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: AttributeIterator) -> bool """
        ...


class ContentIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: ContentIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator): # -> 
        """ Create(self: ContentIterator, context: XPathNavigator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: ContentIterator) -> bool """
        ...


class ContentMergeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: ContentMergeIterator) -> XPathNavigator """
        ...


    def Create(self, filter:XmlNavigatorFilter): # -> 
        """ Create(self: ContentMergeIterator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self, input:XPathNavigator) -> IteratorResult:
        """ MoveNext(self: ContentMergeIterator, input: XPathNavigator) -> IteratorResult """
        ...


class DecimalAggregator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AverageResult(self) -> Decimal:
        """ Get: AverageResult(self: DecimalAggregator) -> Decimal """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: DecimalAggregator) -> bool """
        ...

    @property
    def MaximumResult(self) -> Decimal:
        """ Get: MaximumResult(self: DecimalAggregator) -> Decimal """
        ...

    @property
    def MinimumResult(self) -> Decimal:
        """ Get: MinimumResult(self: DecimalAggregator) -> Decimal """
        ...

    @property
    def SumResult(self) -> Decimal:
        """ Get: SumResult(self: DecimalAggregator) -> Decimal """
        ...


    def Average(self, value:Decimal): # -> 
        """ Average(self: DecimalAggregator, value: Decimal) """
        ...

    def Create(self): # -> 
        """ Create(self: DecimalAggregator) """
        ...

    def Maximum(self, value:Decimal): # -> 
        """ Maximum(self: DecimalAggregator, value: Decimal) """
        ...

    def Minimum(self, value:Decimal): # -> 
        """ Minimum(self: DecimalAggregator, value: Decimal) """
        ...

    def Sum(self, value:Decimal): # -> 
        """ Sum(self: DecimalAggregator, value: Decimal) """
        ...


class DescendantIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: DescendantIterator) -> XPathNavigator """
        ...


    def Create(self, input:XPathNavigator, filter:XmlNavigatorFilter, orSelf:bool): # -> 
        """ Create(self: DescendantIterator, input: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: DescendantIterator) -> bool """
        ...


class DescendantMergeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: DescendantMergeIterator) -> XPathNavigator """
        ...


    def Create(self, filter:XmlNavigatorFilter, orSelf:bool): # -> 
        """ Create(self: DescendantMergeIterator, filter: XmlNavigatorFilter, orSelf: bool) """
        ...

    def MoveNext(self, input:XPathNavigator) -> IteratorResult:
        """ MoveNext(self: DescendantMergeIterator, input: XPathNavigator) -> IteratorResult """
        ...


class DifferenceIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: DifferenceIterator) -> XPathNavigator """
        ...


    def Create(self, runtime:XmlQueryRuntime): # -> 
        """ Create(self: DifferenceIterator, runtime: XmlQueryRuntime) """
        ...

    def MoveNext(self, nestedNavigator:XPathNavigator) -> SetIteratorResult:
        """ MoveNext(self: DifferenceIterator, nestedNavigator: XPathNavigator) -> SetIteratorResult """
        ...


class DodSequenceMerge: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddSequence(self, sequence:IList): # -> 
        """ AddSequence(self: DodSequenceMerge, sequence: IList[XPathNavigator]) """
        ...

    def Create(self, runtime:XmlQueryRuntime): # -> 
        """ Create(self: DodSequenceMerge, runtime: XmlQueryRuntime) """
        ...

    def MergeSequences(self) -> IList:
        """ MergeSequences(self: DodSequenceMerge) -> IList[XPathNavigator] """
        ...


class DoubleAggregator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AverageResult(self) -> float:
        """ Get: AverageResult(self: DoubleAggregator) -> float """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: DoubleAggregator) -> bool """
        ...

    @property
    def MaximumResult(self) -> float:
        """ Get: MaximumResult(self: DoubleAggregator) -> float """
        ...

    @property
    def MinimumResult(self) -> float:
        """ Get: MinimumResult(self: DoubleAggregator) -> float """
        ...

    @property
    def SumResult(self) -> float:
        """ Get: SumResult(self: DoubleAggregator) -> float """
        ...


    def Average(self, value:float): # -> 
        """ Average(self: DoubleAggregator, value: float) """
        ...

    def Create(self): # -> 
        """ Create(self: DoubleAggregator) """
        ...

    def Maximum(self, value:float): # -> 
        """ Maximum(self: DoubleAggregator, value: float) """
        ...

    def Minimum(self, value:float): # -> 
        """ Minimum(self: DoubleAggregator, value: float) """
        ...

    def Sum(self, value:float): # -> 
        """ Sum(self: DoubleAggregator, value: float) """
        ...


class ElementContentIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: ElementContentIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, localName:str, ns:str): # -> 
        """ Create(self: ElementContentIterator, context: XPathNavigator, localName: str, ns: str) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: ElementContentIterator) -> bool """
        ...


class FollowingSiblingIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: FollowingSiblingIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: FollowingSiblingIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: FollowingSiblingIterator) -> bool """
        ...


class FollowingSiblingMergeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: FollowingSiblingMergeIterator) -> XPathNavigator """
        ...


    def Create(self, filter:XmlNavigatorFilter): # -> 
        """ Create(self: FollowingSiblingMergeIterator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self, navigator:XPathNavigator) -> IteratorResult:
        """ MoveNext(self: FollowingSiblingMergeIterator, navigator: XPathNavigator) -> IteratorResult """
        ...


class IdIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: IdIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, value:str): # -> 
        """ Create(self: IdIterator, context: XPathNavigator, value: str) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: IdIterator) -> bool """
        ...


class Int32Aggregator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AverageResult(self) -> int:
        """ Get: AverageResult(self: Int32Aggregator) -> int """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Int32Aggregator) -> bool """
        ...

    @property
    def MaximumResult(self) -> int:
        """ Get: MaximumResult(self: Int32Aggregator) -> int """
        ...

    @property
    def MinimumResult(self) -> int:
        """ Get: MinimumResult(self: Int32Aggregator) -> int """
        ...

    @property
    def SumResult(self) -> int:
        """ Get: SumResult(self: Int32Aggregator) -> int """
        ...


    def Average(self, value:int): # -> 
        """ Average(self: Int32Aggregator, value: int) """
        ...

    def Create(self): # -> 
        """ Create(self: Int32Aggregator) """
        ...

    def Maximum(self, value:int): # -> 
        """ Maximum(self: Int32Aggregator, value: int) """
        ...

    def Minimum(self, value:int): # -> 
        """ Minimum(self: Int32Aggregator, value: int) """
        ...

    def Sum(self, value:int): # -> 
        """ Sum(self: Int32Aggregator, value: int) """
        ...


class Int64Aggregator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AverageResult(self) -> Int64:
        """ Get: AverageResult(self: Int64Aggregator) -> Int64 """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Int64Aggregator) -> bool """
        ...

    @property
    def MaximumResult(self) -> Int64:
        """ Get: MaximumResult(self: Int64Aggregator) -> Int64 """
        ...

    @property
    def MinimumResult(self) -> Int64:
        """ Get: MinimumResult(self: Int64Aggregator) -> Int64 """
        ...

    @property
    def SumResult(self) -> Int64:
        """ Get: SumResult(self: Int64Aggregator) -> Int64 """
        ...


    def Average(self, value:Int64): # -> 
        """ Average(self: Int64Aggregator, value: Int64) """
        ...

    def Create(self): # -> 
        """ Create(self: Int64Aggregator) """
        ...

    def Maximum(self, value:Int64): # -> 
        """ Maximum(self: Int64Aggregator, value: Int64) """
        ...

    def Minimum(self, value:Int64): # -> 
        """ Minimum(self: Int64Aggregator, value: Int64) """
        ...

    def Sum(self, value:Int64): # -> 
        """ Sum(self: Int64Aggregator, value: Int64) """
        ...


class IntersectIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: IntersectIterator) -> XPathNavigator """
        ...


    def Create(self, runtime:XmlQueryRuntime): # -> 
        """ Create(self: IntersectIterator, runtime: XmlQueryRuntime) """
        ...

    def MoveNext(self, nestedNavigator:XPathNavigator) -> SetIteratorResult:
        """ MoveNext(self: IntersectIterator, nestedNavigator: XPathNavigator) -> SetIteratorResult """
        ...


class IteratorResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IteratorResult, values: HaveCurrentNode (2), NeedInputNode (1), NoMoreNodes (0) """
    HaveCurrentNode: IteratorResult = ...
    NeedInputNode: IteratorResult = ...
    NoMoreNodes: IteratorResult = ...
    value__ = ...


class NamespaceIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: NamespaceIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator): # -> 
        """ Create(self: NamespaceIterator, context: XPathNavigator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: NamespaceIterator) -> bool """
        ...


class NodeKindContentIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: NodeKindContentIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, nodeType:XPathNodeType): # -> 
        """ Create(self: NodeKindContentIterator, context: XPathNavigator, nodeType: XPathNodeType) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: NodeKindContentIterator) -> bool """
        ...


class NodeRangeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: NodeRangeIterator) -> XPathNavigator """
        ...


    def Create(self, start:XPathNavigator, filter:XmlNavigatorFilter, end:XPathNavigator): # -> 
        """ Create(self: NodeRangeIterator, start: XPathNavigator, filter: XmlNavigatorFilter, end: XPathNavigator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: NodeRangeIterator) -> bool """
        ...


class ParentIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: ParentIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: ParentIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: ParentIterator) -> bool """
        ...


class PrecedingIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: PrecedingIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: PrecedingIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: PrecedingIterator) -> bool """
        ...


class PrecedingSiblingDocOrderIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: PrecedingSiblingDocOrderIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: PrecedingSiblingDocOrderIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: PrecedingSiblingDocOrderIterator) -> bool """
        ...


class PrecedingSiblingIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: PrecedingSiblingIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: PrecedingSiblingIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: PrecedingSiblingIterator) -> bool """
        ...


class SetIteratorResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SetIteratorResult, values: HaveCurrentNode (4), InitRightIterator (1), NeedLeftNode (2), NeedRightNode (3), NoMoreNodes (0) """
    HaveCurrentNode: SetIteratorResult = ...
    InitRightIterator: SetIteratorResult = ...
    NeedLeftNode: SetIteratorResult = ...
    NeedRightNode: SetIteratorResult = ...
    NoMoreNodes: SetIteratorResult = ...
    value__ = ...


class StringConcat: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: StringConcat) -> str
        Set: Delimiter(self: StringConcat) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: StringConcat) """
        ...

    def Concat(self, value:str): # -> 
        """ Concat(self: StringConcat, value: str) """
        ...

    def GetResult(self) -> str:
        """ GetResult(self: StringConcat) -> str """
        ...


class UnionIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: UnionIterator) -> XPathNavigator """
        ...


    def Create(self, runtime:XmlQueryRuntime): # -> 
        """ Create(self: UnionIterator, runtime: XmlQueryRuntime) """
        ...

    def MoveNext(self, nestedNavigator:XPathNavigator) -> SetIteratorResult:
        """ MoveNext(self: UnionIterator, nestedNavigator: XPathNavigator) -> SetIteratorResult """
        ...


class XmlCollation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: XmlCollation, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XmlCollation) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class XmlILIndex: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Add(self, key:str, navigator:XPathNavigator): # -> 
        """ Add(self: XmlILIndex, key: str, navigator: XPathNavigator) """
        ...

    def Lookup(self, key:str) -> XmlQueryNodeSequence:
        """ Lookup(self: XmlILIndex, key: str) -> XmlQueryNodeSequence """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class XmlILStorageConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BooleanToAtomicValue(value:bool, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ BooleanToAtomicValue(value: bool, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def BytesToAtomicValue(value:Array, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ BytesToAtomicValue(value: Array[Byte], index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def DateTimeToAtomicValue(value:DateTime, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ DateTimeToAtomicValue(value: DateTime, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def DecimalToAtomicValue(value:Decimal, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ DecimalToAtomicValue(value: Decimal, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def DoubleToAtomicValue(value:float, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ DoubleToAtomicValue(value: float, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def Int32ToAtomicValue(value:int, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ Int32ToAtomicValue(value: int, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def Int64ToAtomicValue(value:Int64, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ Int64ToAtomicValue(value: Int64, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def ItemsToNavigators(listItems:IList) -> IList:
        """ ItemsToNavigators(listItems: IList[XPathItem]) -> IList[XPathNavigator] """
        ...

    @staticmethod
    def NavigatorsToItems(listNavigators:IList) -> IList:
        """ NavigatorsToItems(listNavigators: IList[XPathNavigator]) -> IList[XPathItem] """
        ...

    @staticmethod
    def SingleToAtomicValue(value:Single, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ SingleToAtomicValue(value: Single, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def StringToAtomicValue(value:str, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ StringToAtomicValue(value: str, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def TimeSpanToAtomicValue(value:TimeSpan, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ TimeSpanToAtomicValue(value: TimeSpan, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    @staticmethod
    def XmlQualifiedNameToAtomicValue(value:XmlQualifiedName, index:int, runtime:XmlQueryRuntime) -> XmlAtomicValue:
        """ XmlQualifiedNameToAtomicValue(value: XmlQualifiedName, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue """
        ...

    __all__: list = ...


class XmlNavigatorFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def IsFiltered(self, navigator:XPathNavigator) -> bool:
        """ IsFiltered(self: XmlNavigatorFilter, navigator: XPathNavigator) -> bool """
        ...

    def MoveToContent(self, navigator:XPathNavigator) -> bool:
        """ MoveToContent(self: XmlNavigatorFilter, navigator: XPathNavigator) -> bool """
        ...

    def MoveToFollowing(self, navigator:XPathNavigator, navigatorEnd:XPathNavigator) -> bool:
        """ MoveToFollowing(self: XmlNavigatorFilter, navigator: XPathNavigator, navigatorEnd: XPathNavigator) -> bool """
        ...

    def MoveToFollowingSibling(self, navigator:XPathNavigator) -> bool:
        """ MoveToFollowingSibling(self: XmlNavigatorFilter, navigator: XPathNavigator) -> bool """
        ...

    def MoveToNextContent(self, navigator:XPathNavigator) -> bool:
        """ MoveToNextContent(self: XmlNavigatorFilter, navigator: XPathNavigator) -> bool """
        ...

    def MoveToPreviousSibling(self, navigator:XPathNavigator) -> bool:
        """ MoveToPreviousSibling(self: XmlNavigatorFilter, navigator: XPathNavigator) -> bool """
        ...


class XmlQueryContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultDataSource(self) -> XPathNavigator:
        """ Get: DefaultDataSource(self: XmlQueryContext) -> XPathNavigator """
        ...

    @property
    def DefaultNameTable(self) -> XmlNameTable:
        """ Get: DefaultNameTable(self: XmlQueryContext) -> XmlNameTable """
        ...

    @property
    def QueryNameTable(self) -> XmlNameTable:
        """ Get: QueryNameTable(self: XmlQueryContext) -> XmlNameTable """
        ...


    def GetDataSource(self, uriRelative:str, uriBase:str) -> XPathNavigator:
        """ GetDataSource(self: XmlQueryContext, uriRelative: str, uriBase: str) -> XPathNavigator """
        ...

    def GetLateBoundObject(self, namespaceUri:str) -> object:
        """ GetLateBoundObject(self: XmlQueryContext, namespaceUri: str) -> object """
        ...

    def GetParameter(self, localName:str, namespaceUri:str) -> object:
        """ GetParameter(self: XmlQueryContext, localName: str, namespaceUri: str) -> object """
        ...

    def InvokeXsltLateBoundFunction(self, name:str, namespaceUri:str, args:Array) -> IList:
        """ InvokeXsltLateBoundFunction(self: XmlQueryContext, name: str, namespaceUri: str, args: Array[IList[XPathItem]]) -> IList[XPathItem] """
        ...

    def LateBoundFunctionExists(self, name:str, namespaceUri:str) -> bool:
        """ LateBoundFunctionExists(self: XmlQueryContext, name: str, namespaceUri: str) -> bool """
        ...

    def OnXsltMessageEncountered(self, message:str): # -> 
        """ OnXsltMessageEncountered(self: XmlQueryContext, message: str) """
        ...


class XmlQueryItemSequence(XmlQuerySequence): # skipped bases: <type 'IEnumerable[XPathItem]'>, <type 'ICollection[XPathItem]'>, <type 'IList[XPathItem]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection'>, <type 'object'>
    """
    XmlQueryItemSequence()
    XmlQueryItemSequence(capacity: int)
    XmlQueryItemSequence(item: XPathItem)
    """
    def AddClone(self, item:XPathItem): # -> 
        """ AddClone(self: XmlQueryItemSequence, item: XPathItem) """
        ...

    Empty: XmlQueryItemSequence = ...


class XmlQueryNodeSequence(XmlQuerySequence, IList): # skipped bases: <type 'IEnumerable[XPathItem]'>, <type 'ICollection[XPathItem]'>, <type 'IEnumerable[XPathNavigator]'>, <type 'IList'>, <type 'IEnumerable'>, <type 'ICollection[XPathNavigator]'>, <type 'IList[XPathNavigator]'>, <type 'ICollection'>, <type 'object'>
    """
    XmlQueryNodeSequence()
    XmlQueryNodeSequence(capacity: int)
    XmlQueryNodeSequence(list: IList[XPathNavigator])
    XmlQueryNodeSequence(array: Array[XPathNavigator], size: int)
    XmlQueryNodeSequence(navigator: XPathNavigator)
    """
    @property
    def IsDocOrderDistinct(self) -> bool:
        """
        Get: IsDocOrderDistinct(self: XmlQueryNodeSequence) -> bool
        Set: IsDocOrderDistinct(self: XmlQueryNodeSequence) = value
        """
        ...


    def AddClone(self, navigator:XPathNavigator): # -> 
        """ AddClone(self: XmlQueryNodeSequence, navigator: XPathNavigator) """
        ...

    def DocOrderDistinct(self, comparer:IComparer) -> XmlQueryNodeSequence:
        """ DocOrderDistinct(self: XmlQueryNodeSequence, comparer: IComparer[XPathNavigator]) -> XmlQueryNodeSequence """
        ...

    Empty: XmlQueryNodeSequence = ...


class XmlQueryOutput(XmlWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def EndCopy(self, navigator:XPathNavigator): # -> 
        """ EndCopy(self: XmlQueryOutput, navigator: XPathNavigator) """
        ...

    def EndTree(self): # -> 
        """ EndTree(self: XmlQueryOutput) """
        ...

    def StartCopy(self, navigator:XPathNavigator) -> bool:
        """ StartCopy(self: XmlQueryOutput, navigator: XPathNavigator) -> bool """
        ...

    def StartElementContentUnchecked(self): # -> 
        """ StartElementContentUnchecked(self: XmlQueryOutput) """
        ...

    def StartTree(self, rootType:XPathNodeType): # -> 
        """ StartTree(self: XmlQueryOutput, rootType: XPathNodeType) """
        ...

    def WriteCommentString(self, text:str): # -> 
        """ WriteCommentString(self: XmlQueryOutput, text: str) """
        ...

    def WriteEndAttributeUnchecked(self): # -> 
        """ WriteEndAttributeUnchecked(self: XmlQueryOutput) """
        ...

    def WriteEndComment(self): # -> 
        """ WriteEndComment(self: XmlQueryOutput) """
        ...

    def WriteEndElementUnchecked(self, *__args:str): # -> 
        """ WriteEndElementUnchecked(self: XmlQueryOutput, prefix: str, localName: str, ns: str)WriteEndElementUnchecked(self: XmlQueryOutput, localName: str) """
        ...

    def WriteEndNamespace(self): # -> 
        """ WriteEndNamespace(self: XmlQueryOutput) """
        ...

    def WriteEndProcessingInstruction(self): # -> 
        """ WriteEndProcessingInstruction(self: XmlQueryOutput) """
        ...

    def WriteEndRoot(self): # -> 
        """ WriteEndRoot(self: XmlQueryOutput) """
        ...

    def WriteItem(self, item:XPathItem): # -> 
        """ WriteItem(self: XmlQueryOutput, item: XPathItem) """
        ...

    def WriteNamespaceDeclaration(self, prefix:str, ns:str): # -> 
        """ WriteNamespaceDeclaration(self: XmlQueryOutput, prefix: str, ns: str) """
        ...

    def WriteNamespaceDeclarationUnchecked(self, prefix:str, ns:str): # -> 
        """ WriteNamespaceDeclarationUnchecked(self: XmlQueryOutput, prefix: str, ns: str) """
        ...

    def WriteNamespaceString(self, text:str): # -> 
        """ WriteNamespaceString(self: XmlQueryOutput, text: str) """
        ...

    def WriteProcessingInstructionString(self, text:str): # -> 
        """ WriteProcessingInstructionString(self: XmlQueryOutput, text: str) """
        ...

    def WriteRawUnchecked(self, text:str): # -> 
        """ WriteRawUnchecked(self: XmlQueryOutput, text: str) """
        ...

    def WriteStartAttributeComputed(self, *__args:XPathNavigator): # -> 
        """ WriteStartAttributeComputed(self: XmlQueryOutput, tagName: str, prefixMappingsIndex: int)WriteStartAttributeComputed(self: XmlQueryOutput, tagName: str, ns: str)WriteStartAttributeComputed(self: XmlQueryOutput, navigator: XPathNavigator)WriteStartAttributeComputed(self: XmlQueryOutput, name: XmlQualifiedName) """
        ...

    def WriteStartAttributeLocalName(self, localName:str): # -> 
        """ WriteStartAttributeLocalName(self: XmlQueryOutput, localName: str) """
        ...

    def WriteStartAttributeUnchecked(self, *__args:str): # -> 
        """ WriteStartAttributeUnchecked(self: XmlQueryOutput, prefix: str, localName: str, ns: str)WriteStartAttributeUnchecked(self: XmlQueryOutput, localName: str) """
        ...

    def WriteStartComment(self): # -> 
        """ WriteStartComment(self: XmlQueryOutput) """
        ...

    def WriteStartElementComputed(self, *__args:XPathNavigator): # -> 
        """ WriteStartElementComputed(self: XmlQueryOutput, tagName: str, prefixMappingsIndex: int)WriteStartElementComputed(self: XmlQueryOutput, tagName: str, ns: str)WriteStartElementComputed(self: XmlQueryOutput, navigator: XPathNavigator)WriteStartElementComputed(self: XmlQueryOutput, name: XmlQualifiedName) """
        ...

    def WriteStartElementLocalName(self, localName:str): # -> 
        """ WriteStartElementLocalName(self: XmlQueryOutput, localName: str) """
        ...

    def WriteStartElementUnchecked(self, *__args:str): # -> 
        """ WriteStartElementUnchecked(self: XmlQueryOutput, prefix: str, localName: str, ns: str)WriteStartElementUnchecked(self: XmlQueryOutput, localName: str) """
        ...

    def WriteStartNamespace(self, prefix:str): # -> 
        """ WriteStartNamespace(self: XmlQueryOutput, prefix: str) """
        ...

    def WriteStartProcessingInstruction(self, target:str): # -> 
        """ WriteStartProcessingInstruction(self: XmlQueryOutput, target: str) """
        ...

    def WriteStartRoot(self): # -> 
        """ WriteStartRoot(self: XmlQueryOutput) """
        ...

    def WriteStringUnchecked(self, text:str): # -> 
        """ WriteStringUnchecked(self: XmlQueryOutput, text: str) """
        ...

    def XsltCopyOf(self, navigator:XPathNavigator): # -> 
        """ XsltCopyOf(self: XmlQueryOutput, navigator: XPathNavigator) """
        ...


class XmlQueryRuntime: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExternalContext(self) -> XmlQueryContext:
        """ Get: ExternalContext(self: XmlQueryRuntime) -> XmlQueryContext """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: XmlQueryRuntime) -> XmlNameTable """
        ...

    @property
    def Output(self) -> XmlQueryOutput:
        """ Get: Output(self: XmlQueryRuntime) -> XmlQueryOutput """
        ...

    @property
    def XsltFunctions(self) -> XsltLibrary:
        """ Get: XsltFunctions(self: XmlQueryRuntime) -> XsltLibrary """
        ...


    def AddNewIndex(self, context:XPathNavigator, indexId:int, index:XmlILIndex): # -> 
        """ AddNewIndex(self: XmlQueryRuntime, context: XPathNavigator, indexId: int, index: XmlILIndex) """
        ...

    def ChangeTypeXsltArgument(self, indexType:int, value:object, destinationType:Type) -> object:
        """ ChangeTypeXsltArgument(self: XmlQueryRuntime, indexType: int, value: object, destinationType: Type) -> object """
        ...

    def ChangeTypeXsltResult(self, indexType:int, value:object) -> object:
        """ ChangeTypeXsltResult(self: XmlQueryRuntime, indexType: int, value: object) -> object """
        ...

    def ComparePosition(self, navigatorThis:XPathNavigator, navigatorThat:XPathNavigator) -> int:
        """ ComparePosition(self: XmlQueryRuntime, navigatorThis: XPathNavigator, navigatorThat: XPathNavigator) -> int """
        ...

    def CreateCollation(self, collation:str) -> XmlCollation:
        """ CreateCollation(self: XmlQueryRuntime, collation: str) -> XmlCollation """
        ...

    def DebugGetGlobalNames(self) -> Array:
        """ DebugGetGlobalNames(self: XmlQueryRuntime) -> Array[str] """
        ...

    def DebugGetGlobalValue(self, name:str) -> IList:
        """ DebugGetGlobalValue(self: XmlQueryRuntime, name: str) -> IList """
        ...

    def DebugGetXsltValue(self, seq:IList) -> object:
        """ DebugGetXsltValue(self: XmlQueryRuntime, seq: IList) -> object """
        ...

    def DebugSetGlobalValue(self, name:str, value:object): # -> 
        """ DebugSetGlobalValue(self: XmlQueryRuntime, name: str, value: object) """
        ...

    def DocOrderDistinct(self, seq:IList) -> IList:
        """ DocOrderDistinct(self: XmlQueryRuntime, seq: IList[XPathNavigator]) -> IList[XPathNavigator] """
        ...

    def EarlyBoundFunctionExists(self, name:str, namespaceUri:str) -> bool:
        """ EarlyBoundFunctionExists(self: XmlQueryRuntime, name: str, namespaceUri: str) -> bool """
        ...

    def EndRtfConstruction(self, output) -> Tuple_[XPathNavigator, XmlQueryOutput]:
        """ EndRtfConstruction(self: XmlQueryRuntime) -> (XPathNavigator, XmlQueryOutput) """
        ...

    def EndSequenceConstruction(self, output) -> Tuple_[IList, XmlQueryOutput]:
        """ EndSequenceConstruction(self: XmlQueryRuntime) -> (IList[XPathItem], XmlQueryOutput) """
        ...

    def FindIndex(self, context, indexId, index) -> Tuple_[bool, XmlILIndex]:
        """ FindIndex(self: XmlQueryRuntime, context: XPathNavigator, indexId: int) -> (bool, XmlILIndex) """
        ...

    def GenerateId(self, navigator:XPathNavigator) -> str:
        """ GenerateId(self: XmlQueryRuntime, navigator: XPathNavigator) -> str """
        ...

    def GetAtomizedName(self, index:int) -> str:
        """ GetAtomizedName(self: XmlQueryRuntime, index: int) -> str """
        ...

    def GetCollation(self, index:int) -> XmlCollation:
        """ GetCollation(self: XmlQueryRuntime, index: int) -> XmlCollation """
        ...

    def GetEarlyBoundObject(self, index:int) -> object:
        """ GetEarlyBoundObject(self: XmlQueryRuntime, index: int) -> object """
        ...

    def GetGlobalValue(self, index:int) -> object:
        """ GetGlobalValue(self: XmlQueryRuntime, index: int) -> object """
        ...

    def GetNameFilter(self, index:int) -> XmlNavigatorFilter:
        """ GetNameFilter(self: XmlQueryRuntime, index: int) -> XmlNavigatorFilter """
        ...

    def GetTypeFilter(self, nodeType:XPathNodeType) -> XmlNavigatorFilter:
        """ GetTypeFilter(self: XmlQueryRuntime, nodeType: XPathNodeType) -> XmlNavigatorFilter """
        ...

    def IsGlobalComputed(self, index:int) -> bool:
        """ IsGlobalComputed(self: XmlQueryRuntime, index: int) -> bool """
        ...

    def IsQNameEqual(self, *__args) -> bool:
        """
        IsQNameEqual(self: XmlQueryRuntime, n1: XPathNavigator, n2: XPathNavigator) -> bool
        IsQNameEqual(self: XmlQueryRuntime, navigator: XPathNavigator, indexLocalName: int, indexNamespaceUri: int) -> bool
        """
        ...

    def MatchesXmlType(self, *__args) -> bool:
        """
        MatchesXmlType(self: XmlQueryRuntime, seq: IList[XPathItem], indexType: int) -> bool
        MatchesXmlType(self: XmlQueryRuntime, item: XPathItem, indexType: int) -> bool
        MatchesXmlType(self: XmlQueryRuntime, seq: IList[XPathItem], code: XmlTypeCode) -> bool
        MatchesXmlType(self: XmlQueryRuntime, item: XPathItem, code: XmlTypeCode) -> bool
        """
        ...

    @staticmethod
    def OnCurrentNodeChanged(currentNode:XPathNavigator) -> int:
        """ OnCurrentNodeChanged(currentNode: XPathNavigator) -> int """
        ...

    def ParseTagName(self, tagName:str, *__args:int) -> XmlQualifiedName:
        """
        ParseTagName(self: XmlQueryRuntime, tagName: str, indexPrefixMappings: int) -> XmlQualifiedName
        ParseTagName(self: XmlQueryRuntime, tagName: str, ns: str) -> XmlQualifiedName
        """
        ...

    def SendMessage(self, message:str): # -> 
        """ SendMessage(self: XmlQueryRuntime, message: str) """
        ...

    def SetGlobalValue(self, index:int, value:object): # -> 
        """ SetGlobalValue(self: XmlQueryRuntime, index: int, value: object) """
        ...

    def StartRtfConstruction(self, baseUri, output) -> XmlQueryOutput:
        """ StartRtfConstruction(self: XmlQueryRuntime, baseUri: str) -> XmlQueryOutput """
        ...

    def StartSequenceConstruction(self, output) -> XmlQueryOutput:
        """ StartSequenceConstruction(self: XmlQueryRuntime) -> XmlQueryOutput """
        ...

    def TextRtfConstruction(self, text:str, baseUri:str) -> XPathNavigator:
        """ TextRtfConstruction(self: XmlQueryRuntime, text: str, baseUri: str) -> XPathNavigator """
        ...

    def ThrowException(self, text:str): # -> 
        """ ThrowException(self: XmlQueryRuntime, text: str) """
        ...


class XmlQuerySequence(IList): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'ICollection'>, <type 'object'>
    """
    XmlQuerySequence[T]()
    XmlQuerySequence[T](capacity: int)
    XmlQuerySequence[T](array: Array[T], size: int)
    XmlQuerySequence[T](value: T)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlQuerySequence[T]) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlQuerySequence[T], array: Array[T], index: int) """
        ...

    @staticmethod
    def CreateOrReuse(seq:XmlQuerySequence, item = ...) -> XmlQuerySequence: # Not found arg types: {'item': 'T'}
        """
        CreateOrReuse(seq: XmlQuerySequence[T]) -> XmlQuerySequence[T]
        CreateOrReuse(seq: XmlQuerySequence[T], item: T) -> XmlQuerySequence[T]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: XmlQuerySequence[T]) -> IEnumerator[T] """
        ...

    def OnItemsChanged(self, *args): #cannot find CLR method
        """ OnItemsChanged(self: XmlQuerySequence[T]) """
        ...

    def SortByKeys(self, keys:Array): # -> 
        """ SortByKeys(self: XmlQuerySequence[T], keys: Array) """
        ...


class XmlSortKeyAccumulator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Keys(self) -> Array:
        """ Get: Keys(self: XmlSortKeyAccumulator) -> Array """
        ...


    def AddDateTimeSortKey(self, collation:XmlCollation, value:DateTime): # -> 
        """ AddDateTimeSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: DateTime) """
        ...

    def AddDecimalSortKey(self, collation:XmlCollation, value:Decimal): # -> 
        """ AddDecimalSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: Decimal) """
        ...

    def AddDoubleSortKey(self, collation:XmlCollation, value:float): # -> 
        """ AddDoubleSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: float) """
        ...

    def AddEmptySortKey(self, collation:XmlCollation): # -> 
        """ AddEmptySortKey(self: XmlSortKeyAccumulator, collation: XmlCollation) """
        ...

    def AddIntegerSortKey(self, collation:XmlCollation, value:Int64): # -> 
        """ AddIntegerSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: Int64) """
        ...

    def AddIntSortKey(self, collation:XmlCollation, value:int): # -> 
        """ AddIntSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: int) """
        ...

    def AddStringSortKey(self, collation:XmlCollation, value:str): # -> 
        """ AddStringSortKey(self: XmlSortKeyAccumulator, collation: XmlCollation, value: str) """
        ...

    def Create(self): # -> 
        """ Create(self: XmlSortKeyAccumulator) """
        ...

    def FinishSortKeys(self): # -> 
        """ FinishSortKeys(self: XmlSortKeyAccumulator) """
        ...


class XPathFollowingIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathFollowingIterator) -> XPathNavigator """
        ...


    def Create(self, input:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: XPathFollowingIterator, input: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: XPathFollowingIterator) -> bool """
        ...


class XPathFollowingMergeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathFollowingMergeIterator) -> XPathNavigator """
        ...


    def Create(self, filter:XmlNavigatorFilter): # -> 
        """ Create(self: XPathFollowingMergeIterator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self, input:XPathNavigator) -> IteratorResult:
        """ MoveNext(self: XPathFollowingMergeIterator, input: XPathNavigator) -> IteratorResult """
        ...


class XPathPrecedingDocOrderIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathPrecedingDocOrderIterator) -> XPathNavigator """
        ...


    def Create(self, input:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: XPathPrecedingDocOrderIterator, input: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: XPathPrecedingDocOrderIterator) -> bool """
        ...


class XPathPrecedingIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathPrecedingIterator) -> XPathNavigator """
        ...


    def Create(self, context:XPathNavigator, filter:XmlNavigatorFilter): # -> 
        """ Create(self: XPathPrecedingIterator, context: XPathNavigator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: XPathPrecedingIterator) -> bool """
        ...


class XPathPrecedingMergeIterator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathPrecedingMergeIterator) -> XPathNavigator """
        ...


    def Create(self, filter:XmlNavigatorFilter): # -> 
        """ Create(self: XPathPrecedingMergeIterator, filter: XmlNavigatorFilter) """
        ...

    def MoveNext(self, input:XPathNavigator) -> IteratorResult:
        """ MoveNext(self: XPathPrecedingMergeIterator, input: XPathNavigator) -> IteratorResult """
        ...


class XsltConvert: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EnsureNodeSet(listItems:IList) -> IList:
        """ EnsureNodeSet(listItems: IList[XPathItem]) -> IList[XPathNavigator] """
        ...

    @staticmethod
    def ToBoolean(*__args:XPathItem) -> bool:
        """
        ToBoolean(item: XPathItem) -> bool
        ToBoolean(listItems: IList[XPathItem]) -> bool
        """
        ...

    @staticmethod
    def ToDateTime(value:str) -> DateTime:
        """ ToDateTime(value: str) -> DateTime """
        ...

    @staticmethod
    def ToDecimal(value:float) -> Decimal:
        """ ToDecimal(value: float) -> Decimal """
        ...

    @staticmethod
    def ToDouble(*__args:str) -> float:
        """
        ToDouble(value: str) -> float
        ToDouble(item: XPathItem) -> float
        ToDouble(listItems: IList[XPathItem]) -> float
        ToDouble(value: Decimal) -> float
        ToDouble(value: int) -> float
        ToDouble(value: Int64) -> float
        """
        ...

    @staticmethod
    def ToInt(value:float) -> int:
        """ ToInt(value: float) -> int """
        ...

    @staticmethod
    def ToLong(value:float) -> Int64:
        """ ToLong(value: float) -> Int64 """
        ...

    @staticmethod
    def ToNode(*__args:XPathItem) -> XPathNavigator:
        """
        ToNode(item: XPathItem) -> XPathNavigator
        ToNode(listItems: IList[XPathItem]) -> XPathNavigator
        """
        ...

    @staticmethod
    def ToNodeSet(*__args:XPathItem) -> IList:
        """
        ToNodeSet(item: XPathItem) -> IList[XPathNavigator]
        ToNodeSet(listItems: IList[XPathItem]) -> IList[XPathNavigator]
        """
        ...

    @staticmethod
    def ToString(*__args:float) -> str:
        """
        ToString(value: float) -> str
        ToString(item: XPathItem) -> str
        ToString(listItems: IList[XPathItem]) -> str
        ToString(value: DateTime) -> str
        """
        ...

    __all__: list = ...


class XsltFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BaseUri(navigator:XPathNavigator) -> str:
        """ BaseUri(navigator: XPathNavigator) -> str """
        ...

    @staticmethod
    def Contains(s1:str, s2:str) -> bool:
        """ Contains(s1: str, s2: str) -> bool """
        ...

    @staticmethod
    def EXslObjectType(value:IList) -> str:
        """ EXslObjectType(value: IList[XPathItem]) -> str """
        ...

    @staticmethod
    def Lang(value:str, context:XPathNavigator) -> bool:
        """ Lang(value: str, context: XPathNavigator) -> bool """
        ...

    @staticmethod
    def MSFormatDateTime(dateTime:str, format:str, lang:str, isDate:bool) -> str:
        """ MSFormatDateTime(dateTime: str, format: str, lang: str, isDate: bool) -> str """
        ...

    @staticmethod
    def MSLocalName(name:str) -> str:
        """ MSLocalName(name: str) -> str """
        ...

    @staticmethod
    def MSNamespaceUri(name:str, currentNode:XPathNavigator) -> str:
        """ MSNamespaceUri(name: str, currentNode: XPathNavigator) -> str """
        ...

    @staticmethod
    def MSNumber(value:IList) -> float:
        """ MSNumber(value: IList[XPathItem]) -> float """
        ...

    @staticmethod
    def MSStringCompare(s1:str, s2:str, lang:str, options:str) -> float:
        """ MSStringCompare(s1: str, s2: str, lang: str, options: str) -> float """
        ...

    @staticmethod
    def MSUtc(dateTime:str) -> str:
        """ MSUtc(dateTime: str) -> str """
        ...

    @staticmethod
    def NormalizeSpace(value:str) -> str:
        """ NormalizeSpace(value: str) -> str """
        ...

    @staticmethod
    def OuterXml(navigator:XPathNavigator) -> str:
        """ OuterXml(navigator: XPathNavigator) -> str """
        ...

    @staticmethod
    def Round(value:float) -> float:
        """ Round(value: float) -> float """
        ...

    @staticmethod
    def StartsWith(s1:str, s2:str) -> bool:
        """ StartsWith(s1: str, s2: str) -> bool """
        ...

    @staticmethod
    def Substring(value:str, startIndex:float, length:float = ...) -> str:
        """
        Substring(value: str, startIndex: float) -> str
        Substring(value: str, startIndex: float, length: float) -> str
        """
        ...

    @staticmethod
    def SubstringAfter(s1:str, s2:str) -> str:
        """ SubstringAfter(s1: str, s2: str) -> str """
        ...

    @staticmethod
    def SubstringBefore(s1:str, s2:str) -> str:
        """ SubstringBefore(s1: str, s2: str) -> str """
        ...

    @staticmethod
    def SystemProperty(name:XmlQualifiedName) -> XPathItem:
        """ SystemProperty(name: XmlQualifiedName) -> XPathItem """
        ...

    @staticmethod
    def Translate(arg:str, mapString:str, transString:str) -> str:
        """ Translate(arg: str, mapString: str, transString: str) -> str """
        ...

    __all__: list = ...


class XsltLibrary: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CheckScriptNamespace(self, nsUri:str) -> int:
        """ CheckScriptNamespace(self: XsltLibrary, nsUri: str) -> int """
        ...

    def ElementAvailable(self, name:XmlQualifiedName) -> bool:
        """ ElementAvailable(self: XsltLibrary, name: XmlQualifiedName) -> bool """
        ...

    def EqualityOperator(self, opCode:float, left:IList, right:IList) -> bool:
        """ EqualityOperator(self: XsltLibrary, opCode: float, left: IList[XPathItem], right: IList[XPathItem]) -> bool """
        ...

    def FormatMessage(self, res:str, args:IList) -> str:
        """ FormatMessage(self: XsltLibrary, res: str, args: IList[str]) -> str """
        ...

    def FormatNumberDynamic(self, value:float, formatPicture:str, decimalFormatName:XmlQualifiedName, errorMessageName:str) -> str:
        """ FormatNumberDynamic(self: XsltLibrary, value: float, formatPicture: str, decimalFormatName: XmlQualifiedName, errorMessageName: str) -> str """
        ...

    def FormatNumberStatic(self, value:float, decimalFormatterIndex:float) -> str:
        """ FormatNumberStatic(self: XsltLibrary, value: float, decimalFormatterIndex: float) -> str """
        ...

    def FunctionAvailable(self, name:XmlQualifiedName) -> bool:
        """ FunctionAvailable(self: XsltLibrary, name: XmlQualifiedName) -> bool """
        ...

    def IsSameNodeSort(self, nav1:XPathNavigator, nav2:XPathNavigator) -> bool:
        """ IsSameNodeSort(self: XsltLibrary, nav1: XPathNavigator, nav2: XPathNavigator) -> bool """
        ...

    def LangToLcid(self, lang:str, forwardCompatibility:bool) -> int:
        """ LangToLcid(self: XsltLibrary, lang: str, forwardCompatibility: bool) -> int """
        ...

    def NumberFormat(self, value:IList, formatString:str, lang:float, letterValue:str, groupingSeparator:str, groupingSize:float) -> str:
        """ NumberFormat(self: XsltLibrary, value: IList[XPathItem], formatString: str, lang: float, letterValue: str, groupingSeparator: str, groupingSize: float) -> str """
        ...

    def RegisterDecimalFormat(self, name:XmlQualifiedName, infinitySymbol:str, nanSymbol:str, characters:str) -> int:
        """ RegisterDecimalFormat(self: XsltLibrary, name: XmlQualifiedName, infinitySymbol: str, nanSymbol: str, characters: str) -> int """
        ...

    def RegisterDecimalFormatter(self, formatPicture:str, infinitySymbol:str, nanSymbol:str, characters:str) -> float:
        """ RegisterDecimalFormatter(self: XsltLibrary, formatPicture: str, infinitySymbol: str, nanSymbol: str, characters: str) -> float """
        ...

    def RelationalOperator(self, opCode:float, left:IList, right:IList) -> bool:
        """ RelationalOperator(self: XsltLibrary, opCode: float, left: IList[XPathItem], right: IList[XPathItem]) -> bool """
        ...


