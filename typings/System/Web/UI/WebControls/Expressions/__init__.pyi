# encoding: utf-8
# module System.Web.UI.WebControls.Expressions calls itself Expressions
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    ParameterCollection)

from Microsoft.VisualBasic import Collection

from System import Enum, EventArgs, StringComparison, Type

from System.Collections import IDictionary

from System.DirectoryServices import SortDirection

from System.Linq import IQueryable

from System.Web import HttpContext

from System.Web.UI import Control, IStateManager, StateManagedCollection

from System.Web.UI.WebControls import IQueryableDataSource

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DataSourceExpression(IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self):
        ...

    @property
    def DataSource(self) -> IQueryableDataSource:
        """ Get: DataSource(self: DataSourceExpression) -> IQueryableDataSource """
        ...

    @property
    def Owner(self):
        ...

    @property
    def ViewState(self):
        ...


    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: DataSourceExpression, source: IQueryable) -> IQueryable """
        ...

    def SetContext(self, owner:Control, context:HttpContext, dataSource:IQueryableDataSource): # -> 
        """ SetContext(self: DataSourceExpression, owner: Control, context: HttpContext, dataSource: IQueryableDataSource) """
        ...

    def SetDirty(self): # -> 
        """ SetDirty(self: DataSourceExpression) """
        ...


class ParameterDataSourceExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ no doc """
    @property
    def Parameters(self) -> ParameterCollection:
        """ Get: Parameters(self: ParameterDataSourceExpression) -> ParameterCollection """
        ...



class CustomExpression(ParameterDataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ CustomExpression() """
    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: CustomExpression, source: IQueryable) -> IQueryable """
        ...

    Querying = ...


class CustomExpressionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CustomExpressionEventArgs(source: IQueryable, values: IDictionary[str, object]) """
    @property
    def Query(self) -> IQueryable:
        """
        Get: Query(self: CustomExpressionEventArgs) -> IQueryable
        Set: Query(self: CustomExpressionEventArgs) = value
        """
        ...

    @property
    def Values(self) -> IDictionary:
        """ Get: Values(self: CustomExpressionEventArgs) -> IDictionary[str, object] """
        ...


    def __new__(cls, source:IQueryable, values:IDictionary) -> Self:
        """ __new__(cls: type, source: IQueryable, values: IDictionary[str, object]) """
        ...


class DataSourceExpressionCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataSourceExpressionCollection() """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: DataSourceExpressionCollection) -> HttpContext """
        ...

    @property
    def Owner(self) -> Control:
        """ Get: Owner(self: DataSourceExpressionCollection) -> Control """
        ...


    def Add(self, expression:DataSourceExpression): # -> 
        """ Add(self: DataSourceExpressionCollection, expression: DataSourceExpression) """
        ...

    def Contains(self, expression:DataSourceExpression): # -> 
        """ Contains(self: DataSourceExpressionCollection, expression: DataSourceExpression) """
        ...

    def IndexOf(self, expression:DataSourceExpression) -> int:
        """ IndexOf(self: DataSourceExpressionCollection, expression: DataSourceExpression) -> int """
        ...

    def Insert(self, index:int, expression:DataSourceExpression): # -> 
        """ Insert(self: DataSourceExpressionCollection, index: int, expression: DataSourceExpression) """
        ...

    def Remove(self, expression:DataSourceExpression): # -> 
        """ Remove(self: DataSourceExpressionCollection, expression: DataSourceExpression) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataSourceExpressionCollection, index: int) """
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


class MethodExpression(ParameterDataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ MethodExpression() """
    @property
    def IgnoreIfNotFound(self) -> bool:
        """
        Get: IgnoreIfNotFound(self: MethodExpression) -> bool
        Set: IgnoreIfNotFound(self: MethodExpression) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: MethodExpression) -> str
        Set: MethodName(self: MethodExpression) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: MethodExpression) -> str
        Set: TypeName(self: MethodExpression) = value
        """
        ...


    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: MethodExpression, source: IQueryable) -> IQueryable """
        ...


class OfTypeExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """
    OfTypeExpression()
    OfTypeExpression(type: Type)
    """
    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: OfTypeExpression) -> str
        Set: TypeName(self: OfTypeExpression) = value
        """
        ...


    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class OrderByExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ OrderByExpression() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: OrderByExpression) -> str
        Set: DataField(self: OrderByExpression) = value
        """
        ...

    @property
    def Direction(self) -> SortDirection:
        """
        Get: Direction(self: OrderByExpression) -> SortDirection
        Set: Direction(self: OrderByExpression) = value
        """
        ...

    @property
    def ThenByExpressions(self) -> Collection:
        """ Get: ThenByExpressions(self: OrderByExpression) -> Collection[ThenBy] """
        ...



class PropertyExpression(ParameterDataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ PropertyExpression() """
    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: PropertyExpression, source: IQueryable) -> IQueryable """
        ...


class QueryExpression: # skipped bases: <type 'object'>, <type 'object'>
    """ QueryExpression() """
    @property
    def Expressions(self) -> DataSourceExpressionCollection:
        """ Get: Expressions(self: QueryExpression) -> DataSourceExpressionCollection """
        ...


    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: QueryExpression, source: IQueryable) -> IQueryable """
        ...

    def Initialize(self, owner:Control, context:HttpContext, dataSource:IQueryableDataSource): # -> 
        """ Initialize(self: QueryExpression, owner: Control, context: HttpContext, dataSource: IQueryableDataSource) """
        ...


class RangeExpression(ParameterDataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ RangeExpression() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: RangeExpression) -> str
        Set: DataField(self: RangeExpression) = value
        """
        ...

    @property
    def MaxType(self) -> RangeType:
        """
        Get: MaxType(self: RangeExpression) -> RangeType
        Set: MaxType(self: RangeExpression) = value
        """
        ...

    @property
    def MinType(self) -> RangeType:
        """
        Get: MinType(self: RangeExpression) -> RangeType
        Set: MinType(self: RangeExpression) = value
        """
        ...


    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: RangeExpression, source: IQueryable) -> IQueryable """
        ...


class RangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RangeType, values: Exclusive (1), Inclusive (2), None (0) """
    Exclusive: RangeType = ...
    Inclusive: RangeType = ...
    value__ = ...


class SearchExpression(ParameterDataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ SearchExpression() """
    @property
    def ComparisonType(self) -> StringComparison:
        """
        Get: ComparisonType(self: SearchExpression) -> StringComparison
        Set: ComparisonType(self: SearchExpression) = value
        """
        ...

    @property
    def DataFields(self) -> str:
        """
        Get: DataFields(self: SearchExpression) -> str
        Set: DataFields(self: SearchExpression) = value
        """
        ...

    @property
    def SearchType(self) -> SearchType:
        """
        Get: SearchType(self: SearchExpression) -> SearchType
        Set: SearchType(self: SearchExpression) = value
        """
        ...


    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: SearchExpression, source: IQueryable) -> IQueryable """
        ...


class SearchType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchType, values: Contains (0), EndsWith (2), StartsWith (1) """
    Contains: SearchType = ...
    EndsWith: SearchType = ...
    StartsWith: SearchType = ...
    value__ = ...


class ThenBy: # skipped bases: <type 'object'>, <type 'object'>
    """ ThenBy() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: ThenBy) -> str
        Set: DataField(self: ThenBy) = value
        """
        ...

    @property
    def Direction(self) -> SortDirection:
        """
        Get: Direction(self: ThenBy) -> SortDirection
        Set: Direction(self: ThenBy) = value
        """
        ...



