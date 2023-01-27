# encoding: utf-8
# module System.Data.Linq.SqlClient.Implementation calls itself Implementation
# from System.Data.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Type

from System.Collections import IEnumerable

from System.Linq import IGrouping, IOrderedEnumerable

"""The following names are not found in the module: TKey, field#
"""

# no functions
# classes

class ObjectMaterializer: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectMaterializer[TDataReader]() """
    @property
    def CanDeferLoad(self) -> bool:
        """ Get: CanDeferLoad(self: ObjectMaterializer[TDataReader]) -> bool """
        ...


    @staticmethod
    def Convert(source:IEnumerable) -> IEnumerable:
        """ Convert[TOutput](source: IEnumerable) -> IEnumerable[TOutput] """
        ...

    @staticmethod
    def CreateGroup(key, items:IEnumerable) -> IGrouping: # Not found arg types: {'key': 'TKey'}
        """ CreateGroup[(TKey, TElement)](key: TKey, items: IEnumerable[TElement]) -> IGrouping[TKey, TElement] """
        ...

    @staticmethod
    def CreateOrderedEnumerable(items:IEnumerable) -> IOrderedEnumerable:
        """ CreateOrderedEnumerable[TElement](items: IEnumerable[TElement]) -> IOrderedEnumerable[TElement] """
        ...

    @staticmethod
    def ErrorAssignmentToNull(type:Type) -> Exception:
        """ ErrorAssignmentToNull(type: Type) -> Exception """
        ...

    def ExecuteSubQuery(self, iSubQuery:int, args:Array) -> IEnumerable:
        """ ExecuteSubQuery(self: ObjectMaterializer[TDataReader], iSubQuery: int, args: Array[object]) -> IEnumerable """
        ...

    def GetLinkSource(self, globalLink:int, localFactory:int, keyValues:Array) -> IEnumerable:
        """ GetLinkSource[T](self: ObjectMaterializer[TDataReader], globalLink: int, localFactory: int, keyValues: Array[object]) -> IEnumerable[T] """
        ...

    def GetNestedLinkSource(self, globalLink:int, localFactory:int, instance:object) -> IEnumerable:
        """ GetNestedLinkSource[T](self: ObjectMaterializer[TDataReader], globalLink: int, localFactory: int, instance: object) -> IEnumerable[T] """
        ...

    def InsertLookup(self, globalMetaType:int, instance:object) -> object:
        """ InsertLookup(self: ObjectMaterializer[TDataReader], globalMetaType: int, instance: object) -> object """
        ...

    def Read(self) -> bool:
        """ Read(self: ObjectMaterializer[TDataReader]) -> bool """
        ...

    def SendEntityMaterialized(self, globalMetaType:int, instance:object): # -> 
        """ SendEntityMaterialized(self: ObjectMaterializer[TDataReader], globalMetaType: int, instance: object) """
        ...

    Arguments = ...
    BufferReader = ...
    DataReader = ...
    Globals = ...
    Locals = ...
    Ordinals = ...


