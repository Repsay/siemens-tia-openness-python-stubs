# encoding: utf-8
# module System.Data.Common.CommandTrees.ExpressionBuilder calls itself ExpressionBuilder
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import IEnumerable

from System.Collections.Generic import KeyValuePair

from System.Data.Common.CommandTrees import (DbAndExpression, 
    DbApplyExpression, DbArithmeticExpression, DbCaseExpression, 
    DbCastExpression, DbComparisonExpression, DbConstantExpression, 
    DbCrossJoinExpression, DbDerefExpression, DbDistinctExpression, 
    DbElementExpression, DbEntityRefExpression, DbExceptExpression, 
    DbExpression, DbExpressionBinding, DbFilterExpression, 
    DbFunctionAggregate, DbFunctionExpression, DbGroupByExpression, 
    DbGroupExpressionBinding, DbIntersectExpression, DbIsEmptyExpression, 
    DbIsNullExpression, DbIsOfExpression, DbJoinExpression, DbLambda, 
    DbLikeExpression, DbLimitExpression, DbNewInstanceExpression, 
    DbNotExpression, DbNullExpression, DbOfTypeExpression, DbOrExpression, 
    DbParameterReferenceExpression, DbProjectExpression, DbPropertyExpression, 
    DbQuantifierExpression, DbRefExpression, DbRefKeyExpression, 
    DbRelationshipNavigationExpression, DbScanExpression, DbSkipExpression, 
    DbSortClause, DbSortExpression, DbTreatExpression, DbUnionAllExpression, 
    DbVariableReferenceExpression)

from System.Data.Linq import EntitySet

from System.Data.Metadata.Edm import (EdmFunction, EntitySetBase, EntityType, 
    RelationshipEndMember, TypeUsage)

"""The following names are not found in the module: Func
"""

# no functions
# classes

class DbExpressionBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def False(self) -> DbConstantExpression:
        """ Get: False() -> DbConstantExpression """
        ...

    @property
    def True(self) -> DbConstantExpression:
        """ Get: True() -> DbConstantExpression """
        ...


    @staticmethod
    def Aggregate(function:EdmFunction, argument:DbExpression) -> DbFunctionAggregate:
        """ Aggregate(function: EdmFunction, argument: DbExpression) -> DbFunctionAggregate """
        ...

    @staticmethod
    def AggregateDistinct(function:EdmFunction, argument:DbExpression) -> DbFunctionAggregate:
        """ AggregateDistinct(function: EdmFunction, argument: DbExpression) -> DbFunctionAggregate """
        ...

    @staticmethod
    def All(*__args) -> DbQuantifierExpression:
        """
        All(input: DbExpressionBinding, predicate: DbExpression) -> DbQuantifierExpression
        All(source: DbExpression, predicate: Func[DbExpression, DbExpression]) -> DbQuantifierExpression
        """
        ...

    @staticmethod
    def And(left:DbExpression, right:DbExpression) -> DbAndExpression:
        """ And(left: DbExpression, right: DbExpression) -> DbAndExpression """
        ...

    @staticmethod
    def Any(*__args:DbExpression) -> DbExpression:
        """
        Any(input: DbExpressionBinding, predicate: DbExpression) -> DbQuantifierExpression
        Any(source: DbExpression) -> DbExpression
        Any(source: DbExpression, predicate: Func[DbExpression, DbExpression]) -> DbQuantifierExpression
        """
        ...

    @staticmethod
    def As(value:DbExpression, alias:str) -> KeyValuePair:
        """
        As(value: DbExpression, alias: str) -> KeyValuePair[str, DbExpression]
        As(value: DbAggregate, alias: str) -> KeyValuePair[str, DbAggregate]
        """
        ...

    @staticmethod
    def Bind(input:DbExpression) -> DbExpressionBinding:
        """ Bind(input: DbExpression) -> DbExpressionBinding """
        ...

    @staticmethod
    def BindAs(input:DbExpression, varName:str) -> DbExpressionBinding:
        """ BindAs(input: DbExpression, varName: str) -> DbExpressionBinding """
        ...

    @staticmethod
    def Case(whenExpressions:IEnumerable, thenExpressions:IEnumerable, elseExpression:DbExpression) -> DbCaseExpression:
        """ Case(whenExpressions: IEnumerable[DbExpression], thenExpressions: IEnumerable[DbExpression], elseExpression: DbExpression) -> DbCaseExpression """
        ...

    @staticmethod
    def CastTo(argument:DbExpression, toType:TypeUsage) -> DbCastExpression:
        """ CastTo(argument: DbExpression, toType: TypeUsage) -> DbCastExpression """
        ...

    @staticmethod
    def Constant(*__args:object) -> DbConstantExpression:
        """
        Constant(value: object) -> DbConstantExpression
        Constant(constantType: TypeUsage, value: object) -> DbConstantExpression
        """
        ...

    @staticmethod
    def CreateRef(entitySet:EntitySet, *__args:IEnumerable) -> DbRefExpression:
        """
        CreateRef(entitySet: EntitySet, keyValues: IEnumerable[DbExpression]) -> DbRefExpression
        CreateRef(entitySet: EntitySet, *keyValues: Array[DbExpression]) -> DbRefExpression
        CreateRef(entitySet: EntitySet, entityType: EntityType, keyValues: IEnumerable[DbExpression]) -> DbRefExpression
        CreateRef(entitySet: EntitySet, entityType: EntityType, *keyValues: Array[DbExpression]) -> DbRefExpression
        """
        ...

    @staticmethod
    def CrossApply(*__args) -> DbApplyExpression:
        """
        CrossApply(input: DbExpressionBinding, apply: DbExpressionBinding) -> DbApplyExpression
        CrossApply(source: DbExpression, apply: Func[DbExpression, KeyValuePair[str, DbExpression]]) -> DbApplyExpression
        """
        ...

    @staticmethod
    def CrossJoin(inputs:IEnumerable) -> DbCrossJoinExpression:
        """ CrossJoin(inputs: IEnumerable[DbExpressionBinding]) -> DbCrossJoinExpression """
        ...

    @staticmethod
    def Deref(argument:DbExpression) -> DbDerefExpression:
        """ Deref(argument: DbExpression) -> DbDerefExpression """
        ...

    @staticmethod
    def Distinct(argument:DbExpression) -> DbDistinctExpression:
        """ Distinct(argument: DbExpression) -> DbDistinctExpression """
        ...

    @staticmethod
    def Divide(left:DbExpression, right:DbExpression) -> DbArithmeticExpression:
        """ Divide(left: DbExpression, right: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Element(argument:DbExpression) -> DbElementExpression:
        """ Element(argument: DbExpression) -> DbElementExpression """
        ...

    @staticmethod
    def Equal(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ Equal(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def Except(left:DbExpression, right:DbExpression) -> DbExceptExpression:
        """ Except(left: DbExpression, right: DbExpression) -> DbExceptExpression """
        ...

    @staticmethod
    def Exists(argument:DbExpression) -> DbExpression:
        """ Exists(argument: DbExpression) -> DbExpression """
        ...

    @staticmethod
    def Filter(input:DbExpressionBinding, predicate:DbExpression) -> DbFilterExpression:
        """ Filter(input: DbExpressionBinding, predicate: DbExpression) -> DbFilterExpression """
        ...

    @staticmethod
    def FullOuterJoin(left:DbExpressionBinding, right:DbExpressionBinding, joinCondition:DbExpression) -> DbJoinExpression:
        """
        FullOuterJoin(left: DbExpressionBinding, right: DbExpressionBinding, joinCondition: DbExpression) -> DbJoinExpression
        FullOuterJoin(left: DbExpression, right: DbExpression, joinCondition: Func[DbExpression, DbExpression, DbExpression]) -> DbJoinExpression
        """
        ...

    @staticmethod
    def GetEntityRef(argument:DbExpression) -> DbEntityRefExpression:
        """ GetEntityRef(argument: DbExpression) -> DbEntityRefExpression """
        ...

    @staticmethod
    def GetRefKey(argument:DbExpression) -> DbRefKeyExpression:
        """ GetRefKey(argument: DbExpression) -> DbRefKeyExpression """
        ...

    @staticmethod
    def GreaterThan(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ GreaterThan(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def GreaterThanOrEqual(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ GreaterThanOrEqual(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def GroupBind(input:DbExpression) -> DbGroupExpressionBinding:
        """ GroupBind(input: DbExpression) -> DbGroupExpressionBinding """
        ...

    @staticmethod
    def GroupBindAs(input:DbExpression, varName:str, groupVarName:str) -> DbGroupExpressionBinding:
        """ GroupBindAs(input: DbExpression, varName: str, groupVarName: str) -> DbGroupExpressionBinding """
        ...

    @staticmethod
    def GroupBy(input:DbGroupExpressionBinding, keys:IEnumerable, aggregates:IEnumerable) -> DbGroupByExpression:
        """ GroupBy(input: DbGroupExpressionBinding, keys: IEnumerable[KeyValuePair[str, DbExpression]], aggregates: IEnumerable[KeyValuePair[str, DbAggregate]]) -> DbGroupByExpression """
        ...

    @staticmethod
    def InnerJoin(left:DbExpression, right:DbExpression, joinCondition) -> DbJoinExpression: # Not found arg types: {'joinCondition': 'Func'}
        """
        InnerJoin(left: DbExpression, right: DbExpression, joinCondition: Func[DbExpression, DbExpression, DbExpression]) -> DbJoinExpression
        InnerJoin(left: DbExpressionBinding, right: DbExpressionBinding, joinCondition: DbExpression) -> DbJoinExpression
        """
        ...

    @staticmethod
    def Intersect(left:DbExpression, right:DbExpression) -> DbIntersectExpression:
        """ Intersect(left: DbExpression, right: DbExpression) -> DbIntersectExpression """
        ...

    @staticmethod
    def Invoke(*__args) -> DbFunctionExpression:
        """
        Invoke(function: EdmFunction, arguments: IEnumerable[DbExpression]) -> DbFunctionExpression
        Invoke(function: EdmFunction, *arguments: Array[DbExpression]) -> DbFunctionExpression
        Invoke(lambda: DbLambda, arguments: IEnumerable[DbExpression]) -> DbLambdaExpression
        Invoke(lambda: DbLambda, *arguments: Array[DbExpression]) -> DbLambdaExpression
        """
        ...

    @staticmethod
    def IsEmpty(argument:DbExpression) -> DbIsEmptyExpression:
        """ IsEmpty(argument: DbExpression) -> DbIsEmptyExpression """
        ...

    @staticmethod
    def IsNull(argument:DbExpression) -> DbIsNullExpression:
        """ IsNull(argument: DbExpression) -> DbIsNullExpression """
        ...

    @staticmethod
    def IsOf(argument:DbExpression, type:TypeUsage) -> DbIsOfExpression:
        """ IsOf(argument: DbExpression, type: TypeUsage) -> DbIsOfExpression """
        ...

    @staticmethod
    def IsOfOnly(argument:DbExpression, type:TypeUsage) -> DbIsOfExpression:
        """ IsOfOnly(argument: DbExpression, type: TypeUsage) -> DbIsOfExpression """
        ...

    @staticmethod
    def Join(outer:DbExpression, inner:DbExpression, outerKey, innerKey, selector = ...) -> DbProjectExpression: # Not found arg types: {'outerKey': 'Func', 'selector': 'Func', 'innerKey': 'Func'}
        """
        Join(outer: DbExpression, inner: DbExpression, outerKey: Func[DbExpression, DbExpression], innerKey: Func[DbExpression, DbExpression]) -> DbJoinExpression
        Join[TSelector](outer: DbExpression, inner: DbExpression, outerKey: Func[DbExpression, DbExpression], innerKey: Func[DbExpression, DbExpression], selector: Func[DbExpression, DbExpression, TSelector]) -> DbProjectExpression
        """
        ...

    @staticmethod
    def Lambda(body:DbExpression, variables:IEnumerable) -> DbLambda:
        """
        Lambda(body: DbExpression, variables: IEnumerable[DbVariableReferenceExpression]) -> DbLambda
        Lambda(body: DbExpression, *variables: Array[DbVariableReferenceExpression]) -> DbLambda
        """
        ...

    @staticmethod
    def LeftOuterJoin(left:DbExpression, right:DbExpression, joinCondition) -> DbJoinExpression: # Not found arg types: {'joinCondition': 'Func'}
        """
        LeftOuterJoin(left: DbExpression, right: DbExpression, joinCondition: Func[DbExpression, DbExpression, DbExpression]) -> DbJoinExpression
        LeftOuterJoin(left: DbExpressionBinding, right: DbExpressionBinding, joinCondition: DbExpression) -> DbJoinExpression
        """
        ...

    @staticmethod
    def LessThan(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ LessThan(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def LessThanOrEqual(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ LessThanOrEqual(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def Like(argument:DbExpression, pattern:DbExpression, escape:DbExpression = ...) -> DbLikeExpression:
        """
        Like(argument: DbExpression, pattern: DbExpression, escape: DbExpression) -> DbLikeExpression
        Like(argument: DbExpression, pattern: DbExpression) -> DbLikeExpression
        """
        ...

    @staticmethod
    def Limit(argument:DbExpression, count:DbExpression) -> DbLimitExpression:
        """ Limit(argument: DbExpression, count: DbExpression) -> DbLimitExpression """
        ...

    @staticmethod
    def Minus(left:DbExpression, right:DbExpression) -> DbArithmeticExpression:
        """ Minus(left: DbExpression, right: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Modulo(left:DbExpression, right:DbExpression) -> DbArithmeticExpression:
        """ Modulo(left: DbExpression, right: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Multiply(left:DbExpression, right:DbExpression) -> DbArithmeticExpression:
        """ Multiply(left: DbExpression, right: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Navigate(*__args) -> DbRelationshipNavigationExpression:
        """
        Navigate(navigateFrom: DbExpression, fromEnd: RelationshipEndMember, toEnd: RelationshipEndMember) -> DbRelationshipNavigationExpression
        Navigate(type: RelationshipType, fromEndName: str, toEndName: str, navigateFrom: DbExpression) -> DbRelationshipNavigationExpression
        """
        ...

    @staticmethod
    def Negate(argument:DbExpression) -> DbArithmeticExpression:
        """ Negate(argument: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def New(instanceType:TypeUsage, arguments:IEnumerable) -> DbNewInstanceExpression:
        """
        New(instanceType: TypeUsage, arguments: IEnumerable[DbExpression]) -> DbNewInstanceExpression
        New(instanceType: TypeUsage, *arguments: Array[DbExpression]) -> DbNewInstanceExpression
        """
        ...

    @staticmethod
    def NewCollection(elements:IEnumerable) -> DbNewInstanceExpression:
        """
        NewCollection(elements: IEnumerable[DbExpression]) -> DbNewInstanceExpression
        NewCollection(*elements: Array[DbExpression]) -> DbNewInstanceExpression
        """
        ...

    @staticmethod
    def NewEmptyCollection(collectionType:TypeUsage) -> DbNewInstanceExpression:
        """ NewEmptyCollection(collectionType: TypeUsage) -> DbNewInstanceExpression """
        ...

    @staticmethod
    def NewRow(columnValues:IEnumerable) -> DbNewInstanceExpression:
        """ NewRow(columnValues: IEnumerable[KeyValuePair[str, DbExpression]]) -> DbNewInstanceExpression """
        ...

    @staticmethod
    def Not(argument:DbExpression) -> DbNotExpression:
        """ Not(argument: DbExpression) -> DbNotExpression """
        ...

    @staticmethod
    def NotEqual(left:DbExpression, right:DbExpression) -> DbComparisonExpression:
        """ NotEqual(left: DbExpression, right: DbExpression) -> DbComparisonExpression """
        ...

    @staticmethod
    def Null(nullType:TypeUsage) -> DbNullExpression:
        """ Null(nullType: TypeUsage) -> DbNullExpression """
        ...

    @staticmethod
    def OfType(argument:DbExpression, type:TypeUsage) -> DbOfTypeExpression:
        """ OfType(argument: DbExpression, type: TypeUsage) -> DbOfTypeExpression """
        ...

    @staticmethod
    def OfTypeOnly(argument:DbExpression, type:TypeUsage) -> DbOfTypeExpression:
        """ OfTypeOnly(argument: DbExpression, type: TypeUsage) -> DbOfTypeExpression """
        ...

    @staticmethod
    def Or(left:DbExpression, right:DbExpression) -> DbOrExpression:
        """ Or(left: DbExpression, right: DbExpression) -> DbOrExpression """
        ...

    @staticmethod
    def OrderBy(source:DbExpression, sortKey, collation:str = ...) -> DbSortExpression: # Not found arg types: {'sortKey': 'Func'}
        """
        OrderBy(source: DbExpression, sortKey: Func[DbExpression, DbExpression]) -> DbSortExpression
        OrderBy(source: DbExpression, sortKey: Func[DbExpression, DbExpression], collation: str) -> DbSortExpression
        """
        ...

    @staticmethod
    def OrderByDescending(source:DbExpression, sortKey, collation:str = ...) -> DbSortExpression: # Not found arg types: {'sortKey': 'Func'}
        """
        OrderByDescending(source: DbExpression, sortKey: Func[DbExpression, DbExpression]) -> DbSortExpression
        OrderByDescending(source: DbExpression, sortKey: Func[DbExpression, DbExpression], collation: str) -> DbSortExpression
        """
        ...

    @staticmethod
    def OuterApply(*__args) -> DbApplyExpression:
        """
        OuterApply(input: DbExpressionBinding, apply: DbExpressionBinding) -> DbApplyExpression
        OuterApply(source: DbExpression, apply: Func[DbExpression, KeyValuePair[str, DbExpression]]) -> DbApplyExpression
        """
        ...

    @staticmethod
    def Parameter(type:TypeUsage, name:str) -> DbParameterReferenceExpression:
        """ Parameter(type: TypeUsage, name: str) -> DbParameterReferenceExpression """
        ...

    @staticmethod
    def Plus(left:DbExpression, right:DbExpression) -> DbArithmeticExpression:
        """ Plus(left: DbExpression, right: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Project(input:DbExpressionBinding, projection:DbExpression) -> DbProjectExpression:
        """ Project(input: DbExpressionBinding, projection: DbExpression) -> DbProjectExpression """
        ...

    @staticmethod
    def Property(instance:DbExpression, *__args:str) -> DbPropertyExpression:
        """
        Property(instance: DbExpression, propertyName: str) -> DbPropertyExpression
        Property(instance: DbExpression, propertyMetadata: EdmProperty) -> DbPropertyExpression
        Property(instance: DbExpression, navigationProperty: NavigationProperty) -> DbPropertyExpression
        Property(instance: DbExpression, relationshipEnd: RelationshipEndMember) -> DbPropertyExpression
        """
        ...

    @staticmethod
    def RefFromKey(entitySet:EntitySet, keyRow:DbExpression, entityType:EntityType = ...) -> DbRefExpression:
        """
        RefFromKey(entitySet: EntitySet, keyRow: DbExpression) -> DbRefExpression
        RefFromKey(entitySet: EntitySet, keyRow: DbExpression, entityType: EntityType) -> DbRefExpression
        """
        ...

    @staticmethod
    def Scan(targetSet:EntitySetBase) -> DbScanExpression:
        """ Scan(targetSet: EntitySetBase) -> DbScanExpression """
        ...

    @staticmethod
    def Select(source:DbExpression, projection) -> DbProjectExpression: # Not found arg types: {'projection': 'Func'}
        """ Select[TProjection](source: DbExpression, projection: Func[DbExpression, TProjection]) -> DbProjectExpression """
        ...

    @staticmethod
    def SelectMany(source:DbExpression, apply, selector = ...) -> DbProjectExpression: # Not found arg types: {'apply': 'Func', 'selector': 'Func'}
        """
        SelectMany(source: DbExpression, apply: Func[DbExpression, DbExpression]) -> DbProjectExpression
        SelectMany[TSelector](source: DbExpression, apply: Func[DbExpression, DbExpression], selector: Func[DbExpression, DbExpression, TSelector]) -> DbProjectExpression
        """
        ...

    @staticmethod
    def Skip(*__args) -> DbSkipExpression:
        """
        Skip(input: DbExpressionBinding, sortOrder: IEnumerable[DbSortClause], count: DbExpression) -> DbSkipExpression
        Skip(argument: DbSortExpression, count: DbExpression) -> DbSkipExpression
        """
        ...

    @staticmethod
    def Sort(input:DbExpressionBinding, sortOrder:IEnumerable) -> DbSortExpression:
        """ Sort(input: DbExpressionBinding, sortOrder: IEnumerable[DbSortClause]) -> DbSortExpression """
        ...

    @staticmethod
    def Take(argument:DbExpression, count:DbExpression) -> DbLimitExpression:
        """ Take(argument: DbExpression, count: DbExpression) -> DbLimitExpression """
        ...

    @staticmethod
    def ThenBy(source:DbSortExpression, sortKey, collation:str = ...) -> DbSortExpression: # Not found arg types: {'sortKey': 'Func'}
        """
        ThenBy(source: DbSortExpression, sortKey: Func[DbExpression, DbExpression]) -> DbSortExpression
        ThenBy(source: DbSortExpression, sortKey: Func[DbExpression, DbExpression], collation: str) -> DbSortExpression
        """
        ...

    @staticmethod
    def ThenByDescending(source:DbSortExpression, sortKey, collation:str = ...) -> DbSortExpression: # Not found arg types: {'sortKey': 'Func'}
        """
        ThenByDescending(source: DbSortExpression, sortKey: Func[DbExpression, DbExpression]) -> DbSortExpression
        ThenByDescending(source: DbSortExpression, sortKey: Func[DbExpression, DbExpression], collation: str) -> DbSortExpression
        """
        ...

    @staticmethod
    def ToSortClause(key:DbExpression, collation:str = ...) -> DbSortClause:
        """
        ToSortClause(key: DbExpression) -> DbSortClause
        ToSortClause(key: DbExpression, collation: str) -> DbSortClause
        """
        ...

    @staticmethod
    def ToSortClauseDescending(key:DbExpression, collation:str = ...) -> DbSortClause:
        """
        ToSortClauseDescending(key: DbExpression) -> DbSortClause
        ToSortClauseDescending(key: DbExpression, collation: str) -> DbSortClause
        """
        ...

    @staticmethod
    def TreatAs(argument:DbExpression, treatType:TypeUsage) -> DbTreatExpression:
        """ TreatAs(argument: DbExpression, treatType: TypeUsage) -> DbTreatExpression """
        ...

    @staticmethod
    def UnaryMinus(argument:DbExpression) -> DbArithmeticExpression:
        """ UnaryMinus(argument: DbExpression) -> DbArithmeticExpression """
        ...

    @staticmethod
    def Union(left:DbExpression, right:DbExpression) -> DbExpression:
        """ Union(left: DbExpression, right: DbExpression) -> DbExpression """
        ...

    @staticmethod
    def UnionAll(left:DbExpression, right:DbExpression) -> DbUnionAllExpression:
        """ UnionAll(left: DbExpression, right: DbExpression) -> DbUnionAllExpression """
        ...

    @staticmethod
    def Variable(type:TypeUsage, name:str) -> DbVariableReferenceExpression:
        """ Variable(type: TypeUsage, name: str) -> DbVariableReferenceExpression """
        ...

    @staticmethod
    def Where(source:DbExpression, predicate) -> DbFilterExpression: # Not found arg types: {'predicate': 'Func'}
        """ Where(source: DbExpression, predicate: Func[DbExpression, DbExpression]) -> DbFilterExpression """
        ...

    __all__: list = ...


class EdmFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Abs(value:DbExpression) -> DbFunctionExpression:
        """ Abs(value: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddDays(dateValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddDays(dateValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddHours(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddHours(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddMicroseconds(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddMicroseconds(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddMilliseconds(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddMilliseconds(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddMinutes(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddMinutes(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddMonths(dateValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddMonths(dateValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddNanoseconds(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddNanoseconds(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddSeconds(timeValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddSeconds(timeValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AddYears(dateValue:DbExpression, addValue:DbExpression) -> DbFunctionExpression:
        """ AddYears(dateValue: DbExpression, addValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Average(collection:DbExpression) -> DbFunctionExpression:
        """ Average(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def BitwiseAnd(value1:DbExpression, value2:DbExpression) -> DbFunctionExpression:
        """ BitwiseAnd(value1: DbExpression, value2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def BitwiseNot(value:DbExpression) -> DbFunctionExpression:
        """ BitwiseNot(value: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def BitwiseOr(value1:DbExpression, value2:DbExpression) -> DbFunctionExpression:
        """ BitwiseOr(value1: DbExpression, value2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def BitwiseXor(value1:DbExpression, value2:DbExpression) -> DbFunctionExpression:
        """ BitwiseXor(value1: DbExpression, value2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Ceiling(value:DbExpression) -> DbFunctionExpression:
        """ Ceiling(value: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Concat(string1:DbExpression, string2:DbExpression) -> DbFunctionExpression:
        """ Concat(string1: DbExpression, string2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Contains(searchedString:DbExpression, searchedForString:DbExpression) -> DbExpression:
        """ Contains(searchedString: DbExpression, searchedForString: DbExpression) -> DbExpression """
        ...

    @staticmethod
    def Count(collection:DbExpression) -> DbFunctionExpression:
        """ Count(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def CreateDateTime(year:DbExpression, month:DbExpression, day:DbExpression, hour:DbExpression, minute:DbExpression, second:DbExpression) -> DbFunctionExpression:
        """ CreateDateTime(year: DbExpression, month: DbExpression, day: DbExpression, hour: DbExpression, minute: DbExpression, second: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def CreateDateTimeOffset(year:DbExpression, month:DbExpression, day:DbExpression, hour:DbExpression, minute:DbExpression, second:DbExpression, timeZoneOffset:DbExpression) -> DbFunctionExpression:
        """ CreateDateTimeOffset(year: DbExpression, month: DbExpression, day: DbExpression, hour: DbExpression, minute: DbExpression, second: DbExpression, timeZoneOffset: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def CreateTime(hour:DbExpression, minute:DbExpression, second:DbExpression) -> DbFunctionExpression:
        """ CreateTime(hour: DbExpression, minute: DbExpression, second: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def CurrentDateTime() -> DbFunctionExpression:
        """ CurrentDateTime() -> DbFunctionExpression """
        ...

    @staticmethod
    def CurrentDateTimeOffset() -> DbFunctionExpression:
        """ CurrentDateTimeOffset() -> DbFunctionExpression """
        ...

    @staticmethod
    def CurrentUtcDateTime() -> DbFunctionExpression:
        """ CurrentUtcDateTime() -> DbFunctionExpression """
        ...

    @staticmethod
    def Day(dateValue:DbExpression) -> DbFunctionExpression:
        """ Day(dateValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DayOfYear(dateValue:DbExpression) -> DbFunctionExpression:
        """ DayOfYear(dateValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffDays(dateValue1:DbExpression, dateValue2:DbExpression) -> DbFunctionExpression:
        """ DiffDays(dateValue1: DbExpression, dateValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffHours(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffHours(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffMicroseconds(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffMicroseconds(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffMilliseconds(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffMilliseconds(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffMinutes(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffMinutes(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffMonths(dateValue1:DbExpression, dateValue2:DbExpression) -> DbFunctionExpression:
        """ DiffMonths(dateValue1: DbExpression, dateValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffNanoseconds(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffNanoseconds(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffSeconds(timeValue1:DbExpression, timeValue2:DbExpression) -> DbFunctionExpression:
        """ DiffSeconds(timeValue1: DbExpression, timeValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def DiffYears(dateValue1:DbExpression, dateValue2:DbExpression) -> DbFunctionExpression:
        """ DiffYears(dateValue1: DbExpression, dateValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def EndsWith(stringArgument:DbExpression, suffix:DbExpression) -> DbFunctionExpression:
        """ EndsWith(stringArgument: DbExpression, suffix: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Floor(value:DbExpression) -> DbFunctionExpression:
        """ Floor(value: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GetTotalOffsetMinutes(dateTimeOffsetArgument:DbExpression) -> DbFunctionExpression:
        """ GetTotalOffsetMinutes(dateTimeOffsetArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Hour(timeValue:DbExpression) -> DbFunctionExpression:
        """ Hour(timeValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IndexOf(searchString:DbExpression, stringToFind:DbExpression) -> DbFunctionExpression:
        """ IndexOf(searchString: DbExpression, stringToFind: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Left(stringArgument:DbExpression, length:DbExpression) -> DbFunctionExpression:
        """ Left(stringArgument: DbExpression, length: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Length(stringArgument:DbExpression) -> DbFunctionExpression:
        """ Length(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def LongCount(collection:DbExpression) -> DbFunctionExpression:
        """ LongCount(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Max(collection:DbExpression) -> DbFunctionExpression:
        """ Max(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Millisecond(timeValue:DbExpression) -> DbFunctionExpression:
        """ Millisecond(timeValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Min(collection:DbExpression) -> DbFunctionExpression:
        """ Min(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Minute(timeValue:DbExpression) -> DbFunctionExpression:
        """ Minute(timeValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Month(dateValue:DbExpression) -> DbFunctionExpression:
        """ Month(dateValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def NewGuid() -> DbFunctionExpression:
        """ NewGuid() -> DbFunctionExpression """
        ...

    @staticmethod
    def Power(baseArgument:DbExpression, exponent:DbExpression) -> DbFunctionExpression:
        """ Power(baseArgument: DbExpression, exponent: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Replace(stringArgument:DbExpression, toReplace:DbExpression, replacement:DbExpression) -> DbFunctionExpression:
        """ Replace(stringArgument: DbExpression, toReplace: DbExpression, replacement: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Reverse(stringArgument:DbExpression) -> DbFunctionExpression:
        """ Reverse(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Right(stringArgument:DbExpression, length:DbExpression) -> DbFunctionExpression:
        """ Right(stringArgument: DbExpression, length: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Round(value:DbExpression, digits:DbExpression = ...) -> DbFunctionExpression:
        """
        Round(value: DbExpression) -> DbFunctionExpression
        Round(value: DbExpression, digits: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def Second(timeValue:DbExpression) -> DbFunctionExpression:
        """ Second(timeValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def StartsWith(stringArgument:DbExpression, prefix:DbExpression) -> DbFunctionExpression:
        """ StartsWith(stringArgument: DbExpression, prefix: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def StDev(collection:DbExpression) -> DbFunctionExpression:
        """ StDev(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def StDevP(collection:DbExpression) -> DbFunctionExpression:
        """ StDevP(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Substring(stringArgument:DbExpression, start:DbExpression, length:DbExpression) -> DbFunctionExpression:
        """ Substring(stringArgument: DbExpression, start: DbExpression, length: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Sum(collection:DbExpression) -> DbFunctionExpression:
        """ Sum(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def ToLower(stringArgument:DbExpression) -> DbFunctionExpression:
        """ ToLower(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def ToUpper(stringArgument:DbExpression) -> DbFunctionExpression:
        """ ToUpper(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Trim(stringArgument:DbExpression) -> DbFunctionExpression:
        """ Trim(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def TrimEnd(stringArgument:DbExpression) -> DbFunctionExpression:
        """ TrimEnd(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def TrimStart(stringArgument:DbExpression) -> DbFunctionExpression:
        """ TrimStart(stringArgument: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Truncate(value:DbExpression, digits:DbExpression) -> DbFunctionExpression:
        """ Truncate(value: DbExpression, digits: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def TruncateTime(dateValue:DbExpression) -> DbFunctionExpression:
        """ TruncateTime(dateValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Var(collection:DbExpression) -> DbFunctionExpression:
        """ Var(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def VarP(collection:DbExpression) -> DbFunctionExpression:
        """ VarP(collection: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Year(dateValue:DbExpression) -> DbFunctionExpression:
        """ Year(dateValue: DbExpression) -> DbFunctionExpression """
        ...

    __all__: list = ...


class Row: # skipped bases: <type 'object'>, <type 'object'>
    """ Row(columnValue: KeyValuePair[str, DbExpression], *columnValues: Array[KeyValuePair[str, DbExpression]]) """
    def ToExpression(self) -> DbNewInstanceExpression:
        """ ToExpression(self: Row) -> DbNewInstanceExpression """
        ...


# variables with complex values

