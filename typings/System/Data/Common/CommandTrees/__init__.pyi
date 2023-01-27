# encoding: utf-8
# module System.Data.Common.CommandTrees calls itself CommandTrees
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Nullable

from System.Collections import IEnumerable, IList

from System.Collections.Generic import KeyValuePair

from System.Data.Linq import EntitySet

from System.Data.Metadata.Edm import (EdmFunction, EdmMember, EntitySetBase, 
    RelationshipEndMember, RelationshipType, TypeUsage)

from System.Data.Spatial import DbGeography, DbGeometry

"""The following names are not found in the module: TResultType, field#
"""

# no functions
# classes

class DbAggregate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DbAggregate) -> IList[DbExpression] """
        ...

    @property
    def ResultType(self) -> TypeUsage:
        """ Get: ResultType(self: DbAggregate) -> TypeUsage """
        ...



class DbExpression: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExpressionKind(self) -> DbExpressionKind:
        """ Get: ExpressionKind(self: DbExpression) -> DbExpressionKind """
        ...

    @property
    def ResultType(self) -> TypeUsage:
        """ Get: ResultType(self: DbExpression) -> TypeUsage """
        ...


    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: DbExpression, obj: object) -> bool """
        ...

    @staticmethod
    def FromBinary(value:Array) -> DbExpression:
        """ FromBinary(value: Array[Byte]) -> DbExpression """
        ...

    @staticmethod
    def FromBoolean(value:Nullable) -> DbExpression:
        """ FromBoolean(value: Nullable[bool]) -> DbExpression """
        ...

    @staticmethod
    def FromByte(value:Nullable) -> DbExpression:
        """ FromByte(value: Nullable[Byte]) -> DbExpression """
        ...

    @staticmethod
    def FromDateTime(value:Nullable) -> DbExpression:
        """ FromDateTime(value: Nullable[DateTime]) -> DbExpression """
        ...

    @staticmethod
    def FromDateTimeOffset(value:Nullable) -> DbExpression:
        """ FromDateTimeOffset(value: Nullable[DateTimeOffset]) -> DbExpression """
        ...

    @staticmethod
    def FromDecimal(value:Nullable) -> DbExpression:
        """ FromDecimal(value: Nullable[Decimal]) -> DbExpression """
        ...

    @staticmethod
    def FromDouble(value:Nullable) -> DbExpression:
        """ FromDouble(value: Nullable[float]) -> DbExpression """
        ...

    @staticmethod
    def FromGeography(value:DbGeography) -> DbExpression:
        """ FromGeography(value: DbGeography) -> DbExpression """
        ...

    @staticmethod
    def FromGeometry(value:DbGeometry) -> DbExpression:
        """ FromGeometry(value: DbGeometry) -> DbExpression """
        ...

    @staticmethod
    def FromGuid(value:Nullable) -> DbExpression:
        """ FromGuid(value: Nullable[Guid]) -> DbExpression """
        ...

    @staticmethod
    def FromInt16(value:Nullable) -> DbExpression:
        """ FromInt16(value: Nullable[Int16]) -> DbExpression """
        ...

    @staticmethod
    def FromInt32(value:Nullable) -> DbExpression:
        """ FromInt32(value: Nullable[int]) -> DbExpression """
        ...

    @staticmethod
    def FromInt64(value:Nullable) -> DbExpression:
        """ FromInt64(value: Nullable[Int64]) -> DbExpression """
        ...

    @staticmethod
    def FromSingle(value:Nullable) -> DbExpression:
        """ FromSingle(value: Nullable[Single]) -> DbExpression """
        ...

    @staticmethod
    def FromString(value:str) -> DbExpression:
        """ FromString(value: str) -> DbExpression """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DbExpression) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DbBinaryExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Left(self) -> DbExpression:
        """ Get: Left(self: DbBinaryExpression) -> DbExpression """
        ...

    @property
    def Right(self) -> DbExpression:
        """ Get: Right(self: DbBinaryExpression) -> DbExpression """
        ...



class DbAndExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbAndExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbAndExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbApplyExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Apply(self) -> DbExpressionBinding:
        """ Get: Apply(self: DbApplyExpression) -> DbExpressionBinding """
        ...

    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbApplyExpression) -> DbExpressionBinding """
        ...



class DbArithmeticExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DbArithmeticExpression) -> IList[DbExpression] """
        ...



class DbCaseExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Else(self) -> DbExpression:
        """ Get: Else(self: DbCaseExpression) -> DbExpression """
        ...

    @property
    def Then(self) -> IList:
        """ Get: Then(self: DbCaseExpression) -> IList[DbExpression] """
        ...

    @property
    def When(self) -> IList:
        """ Get: When(self: DbCaseExpression) -> IList[DbExpression] """
        ...



class DbUnaryExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Argument(self) -> DbExpression:
        """ Get: Argument(self: DbUnaryExpression) -> DbExpression """
        ...



class DbCastExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbCastExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbCastExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbCommandTree: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Parameters(self) -> IEnumerable:
        """ Get: Parameters(self: DbCommandTree) -> IEnumerable[KeyValuePair[str, TypeUsage]] """
        ...



class DbComparisonExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbComparisonExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbComparisonExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbConstantExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """ Get: Value(self: DbConstantExpression) -> object """
        ...



class DbCrossJoinExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Inputs(self) -> IList:
        """ Get: Inputs(self: DbCrossJoinExpression) -> IList[DbExpressionBinding] """
        ...



class DbModificationCommandTree(DbCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Target(self) -> DbExpressionBinding:
        """ Get: Target(self: DbModificationCommandTree) -> DbExpressionBinding """
        ...



class DbDeleteCommandTree(DbModificationCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Predicate(self) -> DbExpression:
        """ Get: Predicate(self: DbDeleteCommandTree) -> DbExpression """
        ...



class DbDerefExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbDerefExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbDerefExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbDistinctExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbDistinctExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbDistinctExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbElementExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbElementExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbElementExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbEntityRefExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbEntityRefExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbEntityRefExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbExceptExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbExceptExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbExceptExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbExpressionBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> DbExpression:
        """ Get: Expression(self: DbExpressionBinding) -> DbExpression """
        ...

    @property
    def Variable(self) -> DbVariableReferenceExpression:
        """ Get: Variable(self: DbExpressionBinding) -> DbVariableReferenceExpression """
        ...

    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: DbExpressionBinding) -> str """
        ...

    @property
    def VariableType(self) -> TypeUsage:
        """ Get: VariableType(self: DbExpressionBinding) -> TypeUsage """
        ...



class DbExpressionKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DbExpressionKind, values: All (0), And (1), Any (2), Case (3), Cast (4), Constant (5), CrossApply (6), CrossJoin (7), Deref (8), Distinct (9), Divide (10), Element (11), EntityRef (12), Equals (13), Except (14), Filter (15), FullOuterJoin (16), Function (17), GreaterThan (18), GreaterThanOrEquals (19), GroupBy (20), InnerJoin (21), Intersect (22), IsEmpty (23), IsNull (24), IsOf (25), IsOfOnly (26), Lambda (57), LeftOuterJoin (27), LessThan (28), LessThanOrEquals (29), Like (30), Limit (31), Minus (32), Modulo (33), Multiply (34), NewInstance (35), Not (36), NotEquals (37), Null (38), OfType (39), OfTypeOnly (40), Or (41), OuterApply (42), ParameterReference (43), Plus (44), Project (45), Property (46), Ref (47), RefKey (48), RelationshipNavigation (49), Scan (50), Skip (51), Sort (52), Treat (53), UnaryMinus (54), UnionAll (55), VariableReference (56) """
    All: DbExpressionKind = ...
    And: DbExpressionKind = ...
    Any: DbExpressionKind = ...
    Case: DbExpressionKind = ...
    Cast: DbExpressionKind = ...
    Constant: DbExpressionKind = ...
    CrossApply: DbExpressionKind = ...
    CrossJoin: DbExpressionKind = ...
    Deref: DbExpressionKind = ...
    Distinct: DbExpressionKind = ...
    Divide: DbExpressionKind = ...
    Element: DbExpressionKind = ...
    EntityRef: DbExpressionKind = ...
    Equals: DbExpressionKind = ...
    Except: DbExpressionKind = ...
    Filter: DbExpressionKind = ...
    FullOuterJoin: DbExpressionKind = ...
    Function: DbExpressionKind = ...
    GreaterThan: DbExpressionKind = ...
    GreaterThanOrEquals: DbExpressionKind = ...
    GroupBy: DbExpressionKind = ...
    InnerJoin: DbExpressionKind = ...
    Intersect: DbExpressionKind = ...
    IsEmpty: DbExpressionKind = ...
    IsNull: DbExpressionKind = ...
    IsOf: DbExpressionKind = ...
    IsOfOnly: DbExpressionKind = ...
    Lambda: DbExpressionKind = ...
    LeftOuterJoin: DbExpressionKind = ...
    LessThan: DbExpressionKind = ...
    LessThanOrEquals: DbExpressionKind = ...
    Like: DbExpressionKind = ...
    Limit: DbExpressionKind = ...
    Minus: DbExpressionKind = ...
    Modulo: DbExpressionKind = ...
    Multiply: DbExpressionKind = ...
    NewInstance: DbExpressionKind = ...
    Not: DbExpressionKind = ...
    NotEquals: DbExpressionKind = ...
    Null: DbExpressionKind = ...
    OfType: DbExpressionKind = ...
    OfTypeOnly: DbExpressionKind = ...
    Or: DbExpressionKind = ...
    OuterApply: DbExpressionKind = ...
    ParameterReference: DbExpressionKind = ...
    Plus: DbExpressionKind = ...
    Project: DbExpressionKind = ...
    Property: DbExpressionKind = ...
    Ref: DbExpressionKind = ...
    RefKey: DbExpressionKind = ...
    RelationshipNavigation: DbExpressionKind = ...
    Scan: DbExpressionKind = ...
    Skip: DbExpressionKind = ...
    Sort: DbExpressionKind = ...
    Treat: DbExpressionKind = ...
    UnaryMinus: DbExpressionKind = ...
    UnionAll: DbExpressionKind = ...
    value__ = ...
    VariableReference: DbExpressionKind = ...


class DbExpressionVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, expression:DbLambdaExpression): # -> 
        """ Visit(self: DbExpressionVisitor, expression: DbLambdaExpression)Visit(self: DbExpressionVisitor, expression: DbJoinExpression)Visit(self: DbExpressionVisitor, expression: DbLikeExpression)Visit(self: DbExpressionVisitor, expression: DbLimitExpression)Visit(self: DbExpressionVisitor, expression: DbNewInstanceExpression)Visit(self: DbExpressionVisitor, expression: DbNotExpression)Visit(self: DbExpressionVisitor, expression: DbNullExpression)Visit(self: DbExpressionVisitor, expression: DbOfTypeExpression)Visit(self: DbExpressionVisitor, expression: DbOrExpression)Visit(self: DbExpressionVisitor, expression: DbIsOfExpression)Visit(self: DbExpressionVisitor, expression: DbParameterReferenceExpression)Visit(self: DbExpressionVisitor, expression: DbPropertyExpression)Visit(self: DbExpressionVisitor, expression: DbQuantifierExpression)Visit(self: DbExpressionVisitor, expression: DbRefExpression)Visit(self: DbExpressionVisitor, expression: DbRelationshipNavigationExpression)Visit(self: DbExpressionVisitor, expression: DbScanExpression)Visit(self: DbExpressionVisitor, expression: DbSkipExpression)Visit(self: DbExpressionVisitor, expression: DbSortExpression)Visit(self: DbExpressionVisitor, expression: DbTreatExpression)Visit(self: DbExpressionVisitor, expression: DbProjectExpression)Visit(self: DbExpressionVisitor, expression: DbUnionAllExpression)Visit(self: DbExpressionVisitor, expression: DbIsNullExpression)Visit(self: DbExpressionVisitor, expression: DbIntersectExpression)Visit(self: DbExpressionVisitor, expression: DbExpression)Visit(self: DbExpressionVisitor, expression: DbAndExpression)Visit(self: DbExpressionVisitor, expression: DbApplyExpression)Visit(self: DbExpressionVisitor, expression: DbArithmeticExpression)Visit(self: DbExpressionVisitor, expression: DbCaseExpression)Visit(self: DbExpressionVisitor, expression: DbCastExpression)Visit(self: DbExpressionVisitor, expression: DbComparisonExpression)Visit(self: DbExpressionVisitor, expression: DbConstantExpression)Visit(self: DbExpressionVisitor, expression: DbIsEmptyExpression)Visit(self: DbExpressionVisitor, expression: DbCrossJoinExpression)Visit(self: DbExpressionVisitor, expression: DbDistinctExpression)Visit(self: DbExpressionVisitor, expression: DbElementExpression)Visit(self: DbExpressionVisitor, expression: DbExceptExpression)Visit(self: DbExpressionVisitor, expression: DbFilterExpression)Visit(self: DbExpressionVisitor, expression: DbFunctionExpression)Visit(self: DbExpressionVisitor, expression: DbEntityRefExpression)Visit(self: DbExpressionVisitor, expression: DbRefKeyExpression)Visit(self: DbExpressionVisitor, expression: DbGroupByExpression)Visit(self: DbExpressionVisitor, expression: DbDerefExpression)Visit(self: DbExpressionVisitor, expression: DbVariableReferenceExpression) """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class DbFilterExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbFilterExpression) -> DbExpressionBinding """
        ...

    @property
    def Predicate(self) -> DbExpression:
        """ Get: Predicate(self: DbFilterExpression) -> DbExpression """
        ...



class DbFunctionAggregate(DbAggregate): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Distinct(self) -> bool:
        """ Get: Distinct(self: DbFunctionAggregate) -> bool """
        ...

    @property
    def Function(self) -> EdmFunction:
        """ Get: Function(self: DbFunctionAggregate) -> EdmFunction """
        ...



class DbFunctionCommandTree(DbCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EdmFunction(self) -> EdmFunction:
        """ Get: EdmFunction(self: DbFunctionCommandTree) -> EdmFunction """
        ...

    @property
    def ResultType(self) -> TypeUsage:
        """ Get: ResultType(self: DbFunctionCommandTree) -> TypeUsage """
        ...



class DbFunctionExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DbFunctionExpression) -> IList[DbExpression] """
        ...

    @property
    def Function(self) -> EdmFunction:
        """ Get: Function(self: DbFunctionExpression) -> EdmFunction """
        ...



class DbGroupAggregate(DbAggregate): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DbGroupByExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Aggregates(self) -> IList:
        """ Get: Aggregates(self: DbGroupByExpression) -> IList[DbAggregate] """
        ...

    @property
    def Input(self) -> DbGroupExpressionBinding:
        """ Get: Input(self: DbGroupByExpression) -> DbGroupExpressionBinding """
        ...

    @property
    def Keys(self) -> IList:
        """ Get: Keys(self: DbGroupByExpression) -> IList[DbExpression] """
        ...



class DbGroupExpressionBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> DbExpression:
        """ Get: Expression(self: DbGroupExpressionBinding) -> DbExpression """
        ...

    @property
    def GroupAggregate(self) -> DbGroupAggregate:
        """ Get: GroupAggregate(self: DbGroupExpressionBinding) -> DbGroupAggregate """
        ...

    @property
    def GroupVariable(self) -> DbVariableReferenceExpression:
        """ Get: GroupVariable(self: DbGroupExpressionBinding) -> DbVariableReferenceExpression """
        ...

    @property
    def GroupVariableName(self) -> str:
        """ Get: GroupVariableName(self: DbGroupExpressionBinding) -> str """
        ...

    @property
    def GroupVariableType(self) -> TypeUsage:
        """ Get: GroupVariableType(self: DbGroupExpressionBinding) -> TypeUsage """
        ...

    @property
    def Variable(self) -> DbVariableReferenceExpression:
        """ Get: Variable(self: DbGroupExpressionBinding) -> DbVariableReferenceExpression """
        ...

    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: DbGroupExpressionBinding) -> str """
        ...

    @property
    def VariableType(self) -> TypeUsage:
        """ Get: VariableType(self: DbGroupExpressionBinding) -> TypeUsage """
        ...



class DbInsertCommandTree(DbModificationCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Returning(self) -> DbExpression:
        """ Get: Returning(self: DbInsertCommandTree) -> DbExpression """
        ...

    @property
    def SetClauses(self) -> IList:
        """ Get: SetClauses(self: DbInsertCommandTree) -> IList[DbModificationClause] """
        ...



class DbIntersectExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbIntersectExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbIntersectExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbIsEmptyExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbIsEmptyExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbIsEmptyExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbIsNullExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbIsNullExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbIsNullExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbIsOfExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OfType(self) -> TypeUsage:
        """ Get: OfType(self: DbIsOfExpression) -> TypeUsage """
        ...


    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbIsOfExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbIsOfExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbJoinExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def JoinCondition(self) -> DbExpression:
        """ Get: JoinCondition(self: DbJoinExpression) -> DbExpression """
        ...

    @property
    def Left(self) -> DbExpressionBinding:
        """ Get: Left(self: DbJoinExpression) -> DbExpressionBinding """
        ...

    @property
    def Right(self) -> DbExpressionBinding:
        """ Get: Right(self: DbJoinExpression) -> DbExpressionBinding """
        ...



class DbLambda: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Body(self) -> DbExpression:
        """ Get: Body(self: DbLambda) -> DbExpression """
        ...

    @property
    def Variables(self) -> IList:
        """ Get: Variables(self: DbLambda) -> IList[DbVariableReferenceExpression] """
        ...


    @staticmethod
    def Create(*__args) -> DbLambda:
        """
        Create(body: DbExpression, variables: IEnumerable[DbVariableReferenceExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, argument12Type: TypeUsage, argument13Type: TypeUsage, argument14Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, argument12Type: TypeUsage, argument13Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, argument12Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression]) -> DbLambda
        Create(body: DbExpression, *variables: Array[DbVariableReferenceExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, argument12Type: TypeUsage, argument13Type: TypeUsage, argument14Type: TypeUsage, argument15Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        Create(argument1Type: TypeUsage, argument2Type: TypeUsage, argument3Type: TypeUsage, argument4Type: TypeUsage, argument5Type: TypeUsage, argument6Type: TypeUsage, argument7Type: TypeUsage, argument8Type: TypeUsage, argument9Type: TypeUsage, argument10Type: TypeUsage, argument11Type: TypeUsage, argument12Type: TypeUsage, argument13Type: TypeUsage, argument14Type: TypeUsage, argument15Type: TypeUsage, argument16Type: TypeUsage, lambdaFunction: Func[DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression, DbExpression]) -> DbLambda
        """
        ...


class DbLambdaExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DbLambdaExpression) -> IList[DbExpression] """
        ...

    @property
    def Lambda(self) -> DbLambda:
        """ Get: Lambda(self: DbLambdaExpression) -> DbLambda """
        ...



class DbLikeExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Argument(self) -> DbExpression:
        """ Get: Argument(self: DbLikeExpression) -> DbExpression """
        ...

    @property
    def Escape(self) -> DbExpression:
        """ Get: Escape(self: DbLikeExpression) -> DbExpression """
        ...

    @property
    def Pattern(self) -> DbExpression:
        """ Get: Pattern(self: DbLikeExpression) -> DbExpression """
        ...



class DbLimitExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Argument(self) -> DbExpression:
        """ Get: Argument(self: DbLimitExpression) -> DbExpression """
        ...

    @property
    def Limit(self) -> DbExpression:
        """ Get: Limit(self: DbLimitExpression) -> DbExpression """
        ...

    @property
    def WithTies(self) -> bool:
        """ Get: WithTies(self: DbLimitExpression) -> bool """
        ...



class DbModificationClause: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DbNewInstanceExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DbNewInstanceExpression) -> IList[DbExpression] """
        ...



class DbNotExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbNotExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbNotExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbNullExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DbOfTypeExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OfType(self) -> TypeUsage:
        """ Get: OfType(self: DbOfTypeExpression) -> TypeUsage """
        ...


    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbOfTypeExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbOfTypeExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbOrExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbOrExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbOrExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbParameterReferenceExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ParameterName(self) -> str:
        """ Get: ParameterName(self: DbParameterReferenceExpression) -> str """
        ...



class DbProjectExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbProjectExpression) -> DbExpressionBinding """
        ...

    @property
    def Projection(self) -> DbExpression:
        """ Get: Projection(self: DbProjectExpression) -> DbExpression """
        ...



class DbPropertyExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Instance(self) -> DbExpression:
        """ Get: Instance(self: DbPropertyExpression) -> DbExpression """
        ...

    @property
    def Property(self) -> EdmMember:
        """ Get: Property(self: DbPropertyExpression) -> EdmMember """
        ...


    def ToKeyValuePair(self) -> KeyValuePair:
        """ ToKeyValuePair(self: DbPropertyExpression) -> KeyValuePair[str, DbExpression] """
        ...


class DbQuantifierExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbQuantifierExpression) -> DbExpressionBinding """
        ...

    @property
    def Predicate(self) -> DbExpression:
        """ Get: Predicate(self: DbQuantifierExpression) -> DbExpression """
        ...



class DbQueryCommandTree(DbCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Query(self) -> DbExpression:
        """ Get: Query(self: DbQueryCommandTree) -> DbExpression """
        ...



class DbRefExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EntitySet(self) -> EntitySet:
        """ Get: EntitySet(self: DbRefExpression) -> EntitySet """
        ...


    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbRefExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbRefExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbRefKeyExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbRefKeyExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbRefKeyExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbRelationshipNavigationExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NavigateFrom(self) -> RelationshipEndMember:
        """ Get: NavigateFrom(self: DbRelationshipNavigationExpression) -> RelationshipEndMember """
        ...

    @property
    def NavigateTo(self) -> RelationshipEndMember:
        """ Get: NavigateTo(self: DbRelationshipNavigationExpression) -> RelationshipEndMember """
        ...

    @property
    def NavigationSource(self) -> DbExpression:
        """ Get: NavigationSource(self: DbRelationshipNavigationExpression) -> DbExpression """
        ...

    @property
    def Relationship(self) -> RelationshipType:
        """ Get: Relationship(self: DbRelationshipNavigationExpression) -> RelationshipType """
        ...



class DbScanExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Target(self) -> EntitySetBase:
        """ Get: Target(self: DbScanExpression) -> EntitySetBase """
        ...



class DbSetClause(DbModificationClause): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Property(self) -> DbExpression:
        """ Get: Property(self: DbSetClause) -> DbExpression """
        ...

    @property
    def Value(self) -> DbExpression:
        """ Get: Value(self: DbSetClause) -> DbExpression """
        ...



class DbSkipExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> DbExpression:
        """ Get: Count(self: DbSkipExpression) -> DbExpression """
        ...

    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbSkipExpression) -> DbExpressionBinding """
        ...

    @property
    def SortOrder(self) -> IList:
        """ Get: SortOrder(self: DbSkipExpression) -> IList[DbSortClause] """
        ...



class DbSortClause: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Ascending(self) -> bool:
        """ Get: Ascending(self: DbSortClause) -> bool """
        ...

    @property
    def Collation(self) -> str:
        """ Get: Collation(self: DbSortClause) -> str """
        ...

    @property
    def Expression(self) -> DbExpression:
        """ Get: Expression(self: DbSortClause) -> DbExpression """
        ...



class DbSortExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Input(self) -> DbExpressionBinding:
        """ Get: Input(self: DbSortExpression) -> DbExpressionBinding """
        ...

    @property
    def SortOrder(self) -> IList:
        """ Get: SortOrder(self: DbSortExpression) -> IList[DbSortClause] """
        ...



class DbTreatExpression(DbUnaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> TResultType
        """
        Accept[TResultType](self: DbTreatExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType
        Accept(self: DbTreatExpression, visitor: DbExpressionVisitor)
        """
        ...


class DbUnionAllExpression(DbBinaryExpression): # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor:DbExpressionVisitor): # -> 
        """ Accept(self: DbUnionAllExpression, visitor: DbExpressionVisitor)Accept[TResultType](self: DbUnionAllExpression, visitor: DbExpressionVisitor[TResultType]) -> TResultType """
        ...


class DbUpdateCommandTree(DbModificationCommandTree): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Predicate(self) -> DbExpression:
        """ Get: Predicate(self: DbUpdateCommandTree) -> DbExpression """
        ...

    @property
    def Returning(self) -> DbExpression:
        """ Get: Returning(self: DbUpdateCommandTree) -> DbExpression """
        ...

    @property
    def SetClauses(self) -> IList:
        """ Get: SetClauses(self: DbUpdateCommandTree) -> IList[DbModificationClause] """
        ...



class DbVariableReferenceExpression(DbExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: DbVariableReferenceExpression) -> str """
        ...



class DefaultExpressionVisitor(DbExpressionVisitor): # skipped bases: <type 'object'>
    """ no doc """
    def OnEnterScope(self, *args): #cannot find CLR method
        """ OnEnterScope(self: DefaultExpressionVisitor, scopeVariables: IEnumerable[DbVariableReferenceExpression]) """
        ...

    def OnExitScope(self, *args): #cannot find CLR method
        """ OnExitScope(self: DefaultExpressionVisitor) """
        ...

    def OnExpressionReplaced(self, *args): #cannot find CLR method
        """ OnExpressionReplaced(self: DefaultExpressionVisitor, oldExpression: DbExpression, newExpression: DbExpression) """
        ...

    def OnVariableRebound(self, *args): #cannot find CLR method
        """ OnVariableRebound(self: DefaultExpressionVisitor, fromVarRef: DbVariableReferenceExpression, toVarRef: DbVariableReferenceExpression) """
        ...

    def VisitAggregate(self, *args): #cannot find CLR method
        """ VisitAggregate(self: DefaultExpressionVisitor, aggregate: DbAggregate) -> DbAggregate """
        ...

    def VisitEntitySet(self, *args): #cannot find CLR method
        """ VisitEntitySet(self: DefaultExpressionVisitor, entitySet: EntitySetBase) -> EntitySetBase """
        ...

    def VisitExpression(self, *args): #cannot find CLR method
        """ VisitExpression(self: DefaultExpressionVisitor, expression: DbExpression) -> DbExpression """
        ...

    def VisitExpressionBinding(self, *args): #cannot find CLR method
        """ VisitExpressionBinding(self: DefaultExpressionVisitor, binding: DbExpressionBinding) -> DbExpressionBinding """
        ...

    def VisitExpressionBindingList(self, *args): #cannot find CLR method
        """ VisitExpressionBindingList(self: DefaultExpressionVisitor, list: IList[DbExpressionBinding]) -> IList[DbExpressionBinding] """
        ...

    def VisitExpressionList(self, *args): #cannot find CLR method
        """ VisitExpressionList(self: DefaultExpressionVisitor, list: IList[DbExpression]) -> IList[DbExpression] """
        ...

    def VisitFunction(self, *args): #cannot find CLR method
        """ VisitFunction(self: DefaultExpressionVisitor, functionMetadata: EdmFunction) -> EdmFunction """
        ...

    def VisitFunctionAggregate(self, *args): #cannot find CLR method
        """ VisitFunctionAggregate(self: DefaultExpressionVisitor, aggregate: DbFunctionAggregate) -> DbFunctionAggregate """
        ...

    def VisitGroupAggregate(self, *args): #cannot find CLR method
        """ VisitGroupAggregate(self: DefaultExpressionVisitor, aggregate: DbGroupAggregate) -> DbGroupAggregate """
        ...

    def VisitGroupExpressionBinding(self, *args): #cannot find CLR method
        """ VisitGroupExpressionBinding(self: DefaultExpressionVisitor, binding: DbGroupExpressionBinding) -> DbGroupExpressionBinding """
        ...

    def VisitLambda(self, *args): #cannot find CLR method
        """ VisitLambda(self: DefaultExpressionVisitor, lambda: DbLambda) -> DbLambda """
        ...

    def VisitSortClause(self, *args): #cannot find CLR method
        """ VisitSortClause(self: DefaultExpressionVisitor, clause: DbSortClause) -> DbSortClause """
        ...

    def VisitSortOrder(self, *args): #cannot find CLR method
        """ VisitSortOrder(self: DefaultExpressionVisitor, sortOrder: IList[DbSortClause]) -> IList[DbSortClause] """
        ...

    def VisitType(self, *args): #cannot find CLR method
        """ VisitType(self: DefaultExpressionVisitor, type: EdmType) -> EdmType """
        ...

    def VisitTypeUsage(self, *args): #cannot find CLR method
        """ VisitTypeUsage(self: DefaultExpressionVisitor, type: TypeUsage) -> TypeUsage """
        ...


# variables with complex values

