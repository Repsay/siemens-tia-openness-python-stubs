# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.SqlCodeDom calls itself SqlCodeDom
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Excel import IParameter

from Microsoft.SqlServer.Management.SqlParser.Metadata import (DataTypeSpec, 
    IBuiltInFunction, ICallableModule, ICollation, IColumn, IDataType, 
    IDatabaseRole, IExecutionContext, ILocalVariable, ILogin, 
    IMetadataCollection, IMetadataObject, IMutableRelationalIndex, 
    IRelationalIndex, IScalar, IScalarFunction, ISchema, IStoredProcedure, 
    ISynonym, ITableVariable, ITabular, ITrigger, IUser, IUserDefinedFunction, 
    IUserDefinedType, IView)

from System import Array, Enum, Nullable

from System.Activities import Location

from System.Collections import IEnumerable, IEnumerator, IList

from System.Collections.Generic import List

from System.Data.Linq import ITable

from System.Reflection.Emit import StringToken

from typing import Self

"""The following names are not found in the module: (C, IBindFinalizer, 
    IDropObjectStatement, INullCodeObject, ISqlCodeObjectContextVisitor, 
    ISqlStatementContextVisitor, T, field#)
"""

# no functions
# classes

class CreateIndexKeyList: # skipped bases: <type 'object'>, <type 'object'>
    """ CreateIndexKeyList(indexedColumns: IEnumerable[SqlIndexedColumn], includedColumns: IEnumerable[SqlIdentifier]) """
    @property
    def IncludedColumns(self) -> IEnumerable:
        """
        Get: IncludedColumns(self: CreateIndexKeyList) -> IEnumerable[SqlIdentifier]
        Set: IncludedColumns(self: CreateIndexKeyList) = value
        """
        ...

    @property
    def IndexedColumns(self) -> IEnumerable:
        """
        Get: IndexedColumns(self: CreateIndexKeyList) -> IEnumerable[SqlIndexedColumn]
        Set: IndexedColumns(self: CreateIndexKeyList) = value
        """
        ...



class CreateIndexStart: # skipped bases: <type 'object'>, <type 'object'>
    """ CreateIndexStart(isUnique: bool, clusterOption: SqlClusterOption) """
    @property
    def ClusterOption(self) -> SqlClusterOption:
        """
        Get: ClusterOption(self: CreateIndexStart) -> SqlClusterOption
        Set: ClusterOption(self: CreateIndexStart) = value
        """
        ...

    @property
    def IsUnique(self) -> bool:
        """
        Get: IsUnique(self: CreateIndexStart) -> bool
        Set: IsUnique(self: CreateIndexStart) = value
        """
        ...



class CreateTypeStatementInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    CreateTypeStatementInfo(dataType: SqlDataTypeSpecification, nullState: SqlUserDefinedDataTypeNullState)
    CreateTypeStatementInfo(clrClassSpecifier: SqlClrClassSpecifier)
    CreateTypeStatementInfo(tableDefinition: SqlTableDefinition)
    """
    @property
    def ClrClassSpecifier(self) -> SqlClrClassSpecifier:
        """ Get: ClrClassSpecifier(self: CreateTypeStatementInfo) -> SqlClrClassSpecifier """
        ...

    @property
    def DataType(self) -> SqlDataTypeSpecification:
        """ Get: DataType(self: CreateTypeStatementInfo) -> SqlDataTypeSpecification """
        ...

    @property
    def NullState(self) -> SqlUserDefinedDataTypeNullState:
        """ Get: NullState(self: CreateTypeStatementInfo) -> SqlUserDefinedDataTypeNullState """
        ...

    @property
    def TableDefinition(self) -> SqlTableDefinition:
        """ Get: TableDefinition(self: CreateTypeStatementInfo) -> SqlTableDefinition """
        ...


    def GetSqlCreateTypeStatement(self, name:SqlObjectIdentifier) -> SqlCreateTypeStatement:
        """ GetSqlCreateTypeStatement(self: CreateTypeStatementInfo, name: SqlObjectIdentifier) -> SqlCreateTypeStatement """
        ...


class CreateUserStatementFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Create(self, userName:SqlIdentifier, defaultSchema:SqlIdentifier, defaultLanguage:SqlIdentifier = ..., password:str = ...) -> SqlCreateUserStatement:
        """
        Create(self: CreateUserStatementFactory, userName: SqlIdentifier, defaultSchema: SqlIdentifier) -> SqlCreateUserStatement
        Create(self: CreateUserStatementFactory, userName: SqlIdentifier, defaultSchema: SqlIdentifier, defaultLanguage: SqlIdentifier, password: str) -> SqlCreateUserStatement
        """
        ...

    @staticmethod
    def CreateCreateUserFromAsymKeyStatementFactory(asymKeyName:SqlIdentifier) -> CreateUserStatementFactory:
        """ CreateCreateUserFromAsymKeyStatementFactory(asymKeyName: SqlIdentifier) -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserFromCertificateStatementFactory(certificateName:SqlIdentifier) -> CreateUserStatementFactory:
        """ CreateCreateUserFromCertificateStatementFactory(certificateName: SqlIdentifier) -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserFromExternalProviderStatementFactory() -> CreateUserStatementFactory:
        """ CreateCreateUserFromExternalProviderStatementFactory() -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserFromLoginStatementFactory(loginName:SqlIdentifier) -> CreateUserStatementFactory:
        """ CreateCreateUserFromLoginStatementFactory(loginName: SqlIdentifier) -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserStatementErrorFactory() -> CreateUserStatementFactory:
        """ CreateCreateUserStatementErrorFactory() -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserWithImplicitAuthenticationStatementFactory() -> CreateUserStatementFactory:
        """ CreateCreateUserWithImplicitAuthenticationStatementFactory() -> CreateUserStatementFactory """
        ...

    @staticmethod
    def CreateCreateUserWithoutLoginStatementFactory() -> CreateUserStatementFactory:
        """ CreateCreateUserWithoutLoginStatementFactory() -> CreateUserStatementFactory """
        ...


class CursorDefinitionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ CursorDefinitionInfo(statement: SqlSelectStatement, extendedCursorOptions: List[SqlCursorOption]) """
    @property
    def ExtendedCursorOptions(self) -> List:
        """ Get: ExtendedCursorOptions(self: CursorDefinitionInfo) -> List[SqlCursorOption] """
        ...

    @property
    def SelectStatement(self) -> SqlSelectStatement:
        """ Get: SelectStatement(self: CursorDefinitionInfo) -> SqlSelectStatement """
        ...



class DdlTargetObjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DdlTargetObjectType, values: Aggregate (1), Database (2), Default (3), Function (4), Index (5), Login (6), None (0), Procedure (7), Role (8), Rule (9), Schema (10), SecurityPolicy (11), Sequence (12), Synonym (13), Table (14), Trigger (15), Type (16), User (17), View (18) """
    Aggregate: DdlTargetObjectType = ...
    Database: DdlTargetObjectType = ...
    Default: DdlTargetObjectType = ...
    Function: DdlTargetObjectType = ...
    Index: DdlTargetObjectType = ...
    Login: DdlTargetObjectType = ...
    Procedure: DdlTargetObjectType = ...
    Role: DdlTargetObjectType = ...
    Rule: DdlTargetObjectType = ...
    Schema: DdlTargetObjectType = ...
    SecurityPolicy: DdlTargetObjectType = ...
    Sequence: DdlTargetObjectType = ...
    Synonym: DdlTargetObjectType = ...
    Table: DdlTargetObjectType = ...
    Trigger: DdlTargetObjectType = ...
    Type: DdlTargetObjectType = ...
    User: DdlTargetObjectType = ...
    value__ = ...
    View: DdlTargetObjectType = ...


class DmlTarget: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TableExpression(self) -> SqlTableExpression:
        """ Get: TableExpression(self: DmlTarget) -> SqlTableExpression """
        ...

    @property
    def TargetColumns(self) -> List:
        """ Get: TargetColumns(self: DmlTarget) -> List[SqlColumnRefExpression] """
        ...



class FunctionDefinitionFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Create(self, name:SqlObjectIdentifier, parameters:List) -> SqlFunctionDefinition:
        """ Create(self: FunctionDefinitionFactory, name: SqlObjectIdentifier, parameters: List[SqlParameterDeclaration]) -> SqlFunctionDefinition """
        ...

    @staticmethod
    def CreateScalarFactory(returnType:SqlScalarFunctionReturnType, options:List, bodyDefinition:SqlFunctionBodyDefinition) -> FunctionDefinitionFactory:
        """ CreateScalarFactory(returnType: SqlScalarFunctionReturnType, options: List[SqlModuleOption], bodyDefinition: SqlFunctionBodyDefinition) -> FunctionDefinitionFactory """
        ...

    @staticmethod
    def CreateTableClrFactory(returnType:SqlTableFunctionReturnType, options:List, orderClause:SqlSimpleOrderByClause, bodyDefinition:SqlClrFunctionBodyDefinition) -> FunctionDefinitionFactory:
        """ CreateTableClrFactory(returnType: SqlTableFunctionReturnType, options: List[SqlModuleOption], orderClause: SqlSimpleOrderByClause, bodyDefinition: SqlClrFunctionBodyDefinition) -> FunctionDefinitionFactory """
        ...

    @staticmethod
    def CreateTableRelationalFactory(pair:FunctionVariableNameAndTableReturnTypePair, options:List, bodyDefinition:SqlFunctionBodyDefinition) -> FunctionDefinitionFactory:
        """ CreateTableRelationalFactory(pair: FunctionVariableNameAndTableReturnTypePair, options: List[SqlModuleOption], bodyDefinition: SqlFunctionBodyDefinition) -> FunctionDefinitionFactory """
        ...


class FunctionVariableNameAndTableReturnTypePair: # skipped bases: <type 'object'>, <type 'object'>
    """ FunctionVariableNameAndTableReturnTypePair(variable: SqlLiteralExpression, returnType: SqlTableFunctionReturnType) """
    @property
    def ReturnType(self) -> SqlTableFunctionReturnType:
        """ Get: ReturnType(self: FunctionVariableNameAndTableReturnTypePair) -> SqlTableFunctionReturnType """
        ...

    @property
    def Variable(self) -> SqlLiteralExpression:
        """ Get: Variable(self: FunctionVariableNameAndTableReturnTypePair) -> SqlLiteralExpression """
        ...



class IDdlTriggerDefinitionInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivationType(self) -> SqlTriggerActivationType:
        """ Get: ActivationType(self: IDdlTriggerDefinitionInfo) -> SqlTriggerActivationType """
        ...

    @property
    def Events(self) -> SqlCollection:
        """ Get: Events(self: IDdlTriggerDefinitionInfo) -> SqlCollection[SqlTriggerEvent] """
        ...

    @property
    def TargetType(self) -> SqlDdlTriggerTargetType:
        """ Get: TargetType(self: IDdlTriggerDefinitionInfo) -> SqlDdlTriggerTargetType """
        ...



class IDmlTriggerDefinitionInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Actions(self) -> SqlCollection:
        """ Get: Actions(self: IDmlTriggerDefinitionInfo) -> SqlCollection[SqlTriggerAction] """
        ...

    @property
    def ActivationType(self) -> SqlTriggerActivationType:
        """ Get: ActivationType(self: IDmlTriggerDefinitionInfo) -> SqlTriggerActivationType """
        ...

    @property
    def IsNotForReplication(self) -> bool:
        """ Get: IsNotForReplication(self: IDmlTriggerDefinitionInfo) -> bool """
        ...

    @property
    def IsWithAppend(self) -> bool:
        """ Get: IsWithAppend(self: IDmlTriggerDefinitionInfo) -> bool """
        ...

    @property
    def TargetName(self) -> SqlObjectIdentifier:
        """ Get: TargetName(self: IDmlTriggerDefinitionInfo) -> SqlObjectIdentifier """
        ...



class ISqlCodeCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISqlCodeCollection[T]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ISqlCodeCollection[T]) -> bool """
        ...


    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: ISqlCodeCollection[T], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ISqlCodeCollection[T], array: Array[T], arrayIndex: int) """
        ...

    def IndexOf(self, item) -> int: # Not found arg types: {'item': 'T'}
        """ IndexOf(self: ISqlCodeCollection[T], item: T) -> int """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ISqlCodeObjectVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, codeObject:SqlOutputIntoClause): # -> 
        """ Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOutputIntoClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlExecuteArgument)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlExecuteAsClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlExistsBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFillFactorIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFilterClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForBrowseClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForeignKeyConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlAutoClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlDirective)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlExplicitClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlPathClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlForXmlRawClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFromClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFullTextBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFullTextColumn)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGlobalScalarVariableRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGrandTotalGroupByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGrandTotalGroupingSet)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGroupByClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDropExistingIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDmlTriggerDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDmlSpecificationTableSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDerivedTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlColumnIdentity)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlColumnRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCommonTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlComparisonBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCompressionPartitionRange)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlComputedColumnDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlConditionClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlConvertExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCreateUserOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGroupBySets)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCubeGroupByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCursorVariableAssignment)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCursorVariableRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDataCompressionIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDataType)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDataTypeSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDdlTriggerDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDefaultValuesInsertMergeActionSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDefaultValuesInsertSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDeleteMergeAction)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDeleteSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCursorOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlGroupingSetItemsCollection)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlHavingClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIdentifier)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleExecuteAsOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleNativeCompilationOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleRecompileOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleReturnsNullOnNullInputOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleSchemaBindingOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleViewMetadataOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMultistatementFunctionBodyDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMultistatementTableRelationalFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlNotBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleEncryptionOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlQueryExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlObjectIdentifier)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlObjectReference)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOnlineIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlResumableIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBucketCountIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCompressionDelayIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMaxDurationIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOffsetFetchClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOrderByClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlColumnDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlModuleCalledOnNullInputOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMergeSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIdentityFunctionCallExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIgnoreDupKeyIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInBooleanExpressionCollectionValue)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInBooleanExpressionQueryValue)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIndexedColumn)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIndexHint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInlineIndexConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInlineFunctionBodyDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInsertSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInlineTableRelationalFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInsertMergeAction)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInsertSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIntoClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlIsNullBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlLargeDataStorageInformation)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlLikeBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlLiteralExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlLoginPassword)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMaxDegreeOfParallelismIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlMergeActionClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlInlineTableVariableDeclaration)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOrderByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlDefaultConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCollation)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectSpecificationInsertSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectStarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectVariableAssignmentExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSetClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSimpleCaseExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSimpleGroupByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSimpleOrderByClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSimpleOrderByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSimpleWhenClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSortedDataIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSortedDataReorgIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSortInTempDbIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlStatisticsIncrementalIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlStatisticsNoRecomputeIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlStatisticsOnlyIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableClrFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableConstructorExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableConstructorInsertSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableFunctionReturnType)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableHint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectScalarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectIntoClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSelectClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlPadIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlParameterDeclaration)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlPivotClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlPivotTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlPrimaryKeyConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlStorageSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlProcedureDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlQualifiedJoinTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlQuerySpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlQueryWithClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlRollupGroupByItem)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarClrFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarFunctionReturnType)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarRelationalFunctionDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarSubQueryExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarVariableAssignment)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScalarVariableRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlScript)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSearchedCaseExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlSearchedWhenClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlRowConstructorExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableValuedFunctionRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableVariableRefExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTableUdtInstanceMethodExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAllAnyComparisonBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAllowPageLocksIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAllowRowLocksIndexOption)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAssignment)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAtTimeZoneExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBatch)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBetweenBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBinaryBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBinaryFilterExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBinaryQueryExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlAggregateFunctionCallExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBinaryScalarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBooleanFilterExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBuiltinScalarFunctionCallExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCastExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlChangeTrackingContext)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCheckConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlClrAssemblySpecifier)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlClrClassSpecifier)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlClrFunctionBodyDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlClrMethodSpecifier)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlCollateScalarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlColumnAssignment)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlXmlNamespacesDeclaration)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlViewDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTargetTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTemporalPeriodDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTopSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTriggerAction)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTriggerDefinition)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlTriggerEvent)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUdtInstanceDataMemberExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUdtInstanceMethodExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUdtStaticDataMemberExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUdtStaticMethodExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlWhereClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUnaryScalarExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUnpivotClause)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUnpivotTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUnqualifiedJoinTableExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUpdateBooleanExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUpdateMergeAction)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUpdateSpecification)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUserDefinedScalarFunctionCallExpression)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlValuesInsertMergeActionSource)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlVariableColumnAssignment)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlVariableDeclaration)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlUniqueConstraint)Visit(self: ISqlCodeObjectVisitor, codeObject: SqlOutputClause) """
        ...


class ISqlErrorObject: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISqlStatementVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, statement:SqlAlterFunctionStatement): # -> 
        """ Visit(self: ISqlStatementVisitor, statement: SqlAlterFunctionStatement)Visit(self: ISqlStatementVisitor, statement: SqlExecuteModuleStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropViewStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropUserStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropTypeStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropTriggerStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropTableStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropSynonymStatement)Visit(self: ISqlStatementVisitor, statement: SqlExecuteStringStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropSequenceStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropSchemaStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropRuleStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropProcedureStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropLoginStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropFunctionStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropDefaultStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropDatabaseStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropSecurityPolicyStatement)Visit(self: ISqlStatementVisitor, statement: SqlGrantStatement)Visit(self: ISqlStatementVisitor, statement: SqlIfElseStatement)Visit(self: ISqlStatementVisitor, statement: SqlInlineTableVariableDeclareStatement)Visit(self: ISqlStatementVisitor, statement: SqlUseStatement)Visit(self: ISqlStatementVisitor, statement: SqlUpdateStatement)Visit(self: ISqlStatementVisitor, statement: SqlTryCatchStatement)Visit(self: ISqlStatementVisitor, statement: SqlSetStatement)Visit(self: ISqlStatementVisitor, statement: SqlSetAssignmentStatement)Visit(self: ISqlStatementVisitor, statement: SqlSelectStatement)Visit(self: ISqlStatementVisitor, statement: SqlRevokeStatement)Visit(self: ISqlStatementVisitor, statement: SqlReturnStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreTableStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreServiceMasterKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreMasterKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreLogStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreInformationStatement)Visit(self: ISqlStatementVisitor, statement: SqlRestoreDatabaseStatement)Visit(self: ISqlStatementVisitor, statement: SqlStatement)Visit(self: ISqlStatementVisitor, statement: SqlMergeStatement)Visit(self: ISqlStatementVisitor, statement: SqlInsertStatement)Visit(self: ISqlStatementVisitor, statement: SqlDropAggregateStatement)Visit(self: ISqlStatementVisitor, statement: SqlDenyStatement)Visit(self: ISqlStatementVisitor, statement: SqlDeleteStatement)Visit(self: ISqlStatementVisitor, statement: SqlDBCCStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateLoginFromAsymKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateIndexStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateFunctionStatement)Visit(self: ISqlStatementVisitor, statement: SqlContinueStatement)Visit(self: ISqlStatementVisitor, statement: SqlCompoundStatement)Visit(self: ISqlStatementVisitor, statement: SqlCommentStatement)Visit(self: ISqlStatementVisitor, statement: SqlBreakStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupTableStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupServiceMasterKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupMasterKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupLogStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupDatabaseStatement)Visit(self: ISqlStatementVisitor, statement: SqlBackupCertificateStatement)Visit(self: ISqlStatementVisitor, statement: SqlAlterViewStatement)Visit(self: ISqlStatementVisitor, statement: SqlAlterTriggerStatement)Visit(self: ISqlStatementVisitor, statement: SqlAlterProcedureStatement)Visit(self: ISqlStatementVisitor, statement: SqlAlterLoginStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateLoginFromCertificateStatement)Visit(self: ISqlStatementVisitor, statement: SqlVariableDeclareStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateLoginFromWindowsStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateProcedureStatement)Visit(self: ISqlStatementVisitor, statement: SqlCursorDeclareStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateViewStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserWithoutLoginStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserFromExternalProviderStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserFromLoginStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserWithImplicitAuthenticationStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserFromCertificateStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserFromAsymKeyStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserDefinedTypeStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserDefinedTableTypeStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateUserDefinedDataTypeStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateTriggerStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateTableStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateSynonymStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateSchemaStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateRoleStatement)Visit(self: ISqlStatementVisitor, statement: SqlCreateLoginWithPasswordStatement)Visit(self: ISqlStatementVisitor, statement: SqlWhileStatement) """
        ...


class ISqlTableElement: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsColumnDefinition(self) -> SqlColumnDefinition:
        """ Get: AsColumnDefinition(self: ISqlTableElement) -> SqlColumnDefinition """
        ...

    @property
    def AsConstraint(self) -> SqlConstraint:
        """ Get: AsConstraint(self: ISqlTableElement) -> SqlConstraint """
        ...

    @property
    def AsTemporalPeriodDefinition(self) -> SqlTemporalPeriodDefinition:
        """ Get: AsTemporalPeriodDefinition(self: ISqlTableElement) -> SqlTemporalPeriodDefinition """
        ...

    @property
    def IsColumnDefinition(self) -> bool:
        """ Get: IsColumnDefinition(self: ISqlTableElement) -> bool """
        ...

    @property
    def IsConstraint(self) -> bool:
        """ Get: IsConstraint(self: ISqlTableElement) -> bool """
        ...

    @property
    def IsTemporalPeriodDefinition(self) -> bool:
        """ Get: IsTemporalPeriodDefinition(self: ISqlTableElement) -> bool """
        ...



class IVisitableSqlCodeObject: # skipped bases: <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: IVisitableSqlCodeObject, visitor: ISqlCodeObjectVisitor)Accept[T](self: IVisitableSqlCodeObject, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: IVisitableSqlCodeObject, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: IVisitableSqlCodeObject, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class IVisitableSqlStatement(IVisitableSqlCodeObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class LiteralValueType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LiteralValueType, values: Binary (0), Default (1), Identifier (2), Image (4), Integer (3), Money (5), Null (6), Numeric (7), Real (8), String (9), UnicodeString (10) """
    Binary: LiteralValueType = ...
    Default: LiteralValueType = ...
    Identifier: LiteralValueType = ...
    Image: LiteralValueType = ...
    Integer: LiteralValueType = ...
    Money: LiteralValueType = ...
    Null: LiteralValueType = ...
    Numeric: LiteralValueType = ...
    Real: LiteralValueType = ...
    String: LiteralValueType = ...
    UnicodeString: LiteralValueType = ...
    value__ = ...


class LoginOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ LoginOptions(options: List[SqlLoginOption]) """
    @property
    def CheckExpiration(self) -> SqlOnOffValue:
        """ Get: CheckExpiration(self: LoginOptions) -> SqlOnOffValue """
        ...

    @property
    def CheckPolicy(self) -> SqlOnOffValue:
        """ Get: CheckPolicy(self: LoginOptions) -> SqlOnOffValue """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: LoginOptions) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Credential(self) -> SqlIdentifier:
        """ Get: Credential(self: LoginOptions) -> SqlIdentifier """
        ...

    @property
    def DefaultDatabase(self) -> SqlIdentifier:
        """ Get: DefaultDatabase(self: LoginOptions) -> SqlIdentifier """
        ...

    @property
    def DefaultLanguage(self) -> SqlIdentifier:
        """ Get: DefaultLanguage(self: LoginOptions) -> SqlIdentifier """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: LoginOptions) -> SqlIdentifier """
        ...

    @property
    def NoCredential(self) -> bool:
        """ Get: NoCredential(self: LoginOptions) -> bool """
        ...

    @property
    def OldPassword(self) -> SqlLoginPassword:
        """ Get: OldPassword(self: LoginOptions) -> SqlLoginPassword """
        ...

    @property
    def Password(self) -> SqlLoginPassword:
        """ Get: Password(self: LoginOptions) -> SqlLoginPassword """
        ...

    @property
    def Sid(self) -> SqlLiteralExpression:
        """ Get: Sid(self: LoginOptions) -> SqlLiteralExpression """
        ...



class ScalarExpressionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ScalarExpressionType, values: Binary (1), Case (2), Collate (4), ColumnReference (8), Error (33554432), Function (32), GlobalVariableReference (64), Literal (16), Null (16777216), SubQuery (128), Udt (512), Unary (256), Unknown (0), VariableReference (1024) """
    Binary: ScalarExpressionType = ...
    Case: ScalarExpressionType = ...
    Collate: ScalarExpressionType = ...
    ColumnReference: ScalarExpressionType = ...
    Error: ScalarExpressionType = ...
    Function: ScalarExpressionType = ...
    GlobalVariableReference: ScalarExpressionType = ...
    Literal: ScalarExpressionType = ...
    Null: ScalarExpressionType = ...
    SubQuery: ScalarExpressionType = ...
    Udt: ScalarExpressionType = ...
    Unary: ScalarExpressionType = ...
    Unknown: ScalarExpressionType = ...
    value__ = ...
    VariableReference: ScalarExpressionType = ...


class SelectExpressionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SelectExpressionType, values: Error (134217728), Scalar (1), Star (2), Unknown (0), VariableAssignment (4) """
    Error: SelectExpressionType = ...
    Scalar: SelectExpressionType = ...
    Star: SelectExpressionType = ...
    Unknown: SelectExpressionType = ...
    value__ = ...
    VariableAssignment: SelectExpressionType = ...


class SqlCodeObject(IVisitableSqlCodeObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCodeObject) -> IMetadataObject """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCodeObject) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def EndLocation(self) -> Location:
        """ Get: EndLocation(self: SqlCodeObject) -> Location """
        ...

    @property
    def IsSqlCodeSnippet(self) -> bool:
        """ Get: IsSqlCodeSnippet(self: SqlCodeObject) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: SqlCodeObject) -> int """
        ...

    @property
    def Sql(self) -> str:
        """ Get: Sql(self: SqlCodeObject) -> str """
        ...

    @property
    def StartLocation(self) -> Location:
        """ Get: StartLocation(self: SqlCodeObject) -> Location """
        ...

    @property
    def Statement(self) -> SqlStatement:
        """ Get: Statement(self: SqlCodeObject) -> SqlStatement """
        ...

    @property
    def Tokens(self) -> IEnumerable:
        """ Get: Tokens(self: SqlCodeObject) -> IEnumerable[Token] """
        ...

    @property
    def Xml(self) -> str:
        """ Get: Xml(self: SqlCodeObject) -> str """
        ...


    @staticmethod
    def GetSqlSource(*__args:ISqlCodeCollection) -> str:
        """
        GetSqlSource[T](collection: ISqlCodeCollection[T]) -> str
        GetSqlSource(*codeObjects: Array[SqlCodeObject]) -> str
        GetSqlSource(first: SqlCodeObject, last: SqlCodeObject) -> str
        """
        ...


class SqlScalarExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundScalar(self) -> IScalar:
        """ Get: BoundScalar(self: SqlScalarExpression) -> IScalar """
        ...



class SqlScalarFunctionCallExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlScalarFunctionCallExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def BoundFunction(self) -> IScalarFunction:
        """ Get: BoundFunction(self: SqlScalarFunctionCallExpression) -> IScalarFunction """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarFunctionCallExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlBuiltinScalarFunctionCallExpression(SqlScalarFunctionCallExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: SqlBuiltinScalarFunctionCallExpression) -> str """
        ...

    @property
    def IsStar(self) -> bool:
        """ Get: IsStar(self: SqlBuiltinScalarFunctionCallExpression) -> bool """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlBuiltinScalarFunctionCallExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBuiltinScalarFunctionCallExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBuiltinScalarFunctionCallExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBuiltinScalarFunctionCallExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlAggregateFunctionCallExpression(SqlBuiltinScalarFunctionCallExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def SetQuantifier(self) -> SqlSetQuantifier:
        """ Get: SetQuantifier(self: SqlAggregateFunctionCallExpression) -> SqlSetQuantifier """
        ...



class SqlBooleanExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlAllAnyComparisonBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlAllAnyComparisonBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ComparisonOperator(self) -> SqlComparisonBooleanExpressionType:
        """ Get: ComparisonOperator(self: SqlAllAnyComparisonBooleanExpression) -> SqlComparisonBooleanExpressionType """
        ...

    @property
    def ComparisonType(self) -> str:
        """ Get: ComparisonType(self: SqlAllAnyComparisonBooleanExpression) -> str """
        ...

    @property
    def Left(self) -> SqlScalarExpression:
        """ Get: Left(self: SqlAllAnyComparisonBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def Right(self) -> SqlQueryExpression:
        """ Get: Right(self: SqlAllAnyComparisonBooleanExpression) -> SqlQueryExpression """
        ...



class SqlIndexOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlIndexOptionType:
        """ Get: Type(self: SqlIndexOption) -> SqlIndexOptionType """
        ...



class SqlAllowPageLocksIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlAllowPageLocksIndexOption) -> SqlOnOffValue """
        ...



class SqlAllowRowLocksIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlAllowRowLocksIndexOption) -> SqlOnOffValue """
        ...



class SqlStatement(IVisitableSqlStatement, SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlDdlStatement(SqlStatement, IBindFinalizer): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlCreateAlterFunctionStatementBase(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundFunction(self) -> IUserDefinedFunction:
        """ Get: BoundFunction(self: SqlCreateAlterFunctionStatementBase) -> IUserDefinedFunction """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateAlterFunctionStatementBase) -> IMetadataObject """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateAlterFunctionStatementBase) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Definition(self) -> SqlFunctionDefinition:
        """ Get: Definition(self: SqlCreateAlterFunctionStatementBase) -> SqlFunctionDefinition """
        ...



class SqlAlterFunctionStatement(SqlCreateAlterFunctionStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlAlterFunctionStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlAlterFunctionStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlAlterFunctionStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterFunctionStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlAlterFunctionStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlAlterFunctionStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlAlterFunctionStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterFunctionStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlAlterLoginStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlAlterLoginStatement(loginName: SqlIdentifier) """
    @property
    def CheckExpiration(self) -> SqlOnOffValue:
        """ Get: CheckExpiration(self: SqlAlterLoginStatement) -> SqlOnOffValue """
        ...

    @property
    def CheckPolicy(self) -> SqlOnOffValue:
        """ Get: CheckPolicy(self: SqlAlterLoginStatement) -> SqlOnOffValue """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlAlterLoginStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Credential(self) -> SqlIdentifier:
        """ Get: Credential(self: SqlAlterLoginStatement) -> SqlIdentifier """
        ...

    @property
    def DefaultDatabase(self) -> SqlIdentifier:
        """ Get: DefaultDatabase(self: SqlAlterLoginStatement) -> SqlIdentifier """
        ...

    @property
    def DefaultLanguage(self) -> SqlIdentifier:
        """ Get: DefaultLanguage(self: SqlAlterLoginStatement) -> SqlIdentifier """
        ...

    @property
    def LoginName(self) -> SqlIdentifier:
        """ Get: LoginName(self: SqlAlterLoginStatement) -> SqlIdentifier """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlAlterLoginStatement) -> SqlIdentifier """
        ...

    @property
    def NoCredential(self) -> bool:
        """ Get: NoCredential(self: SqlAlterLoginStatement) -> bool """
        ...

    @property
    def OldPassword(self) -> SqlLoginPassword:
        """ Get: OldPassword(self: SqlAlterLoginStatement) -> SqlLoginPassword """
        ...

    @property
    def Password(self) -> SqlLoginPassword:
        """ Get: Password(self: SqlAlterLoginStatement) -> SqlLoginPassword """
        ...


    def __new__(cls, loginName:SqlIdentifier) -> Self:
        """ __new__(cls: type, loginName: SqlIdentifier) """
        ...


class SqlCreateAlterProcedureStatementBase(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateAlterProcedureStatementBase) -> IMetadataObject """
        ...

    @property
    def BoundStoredProc(self) -> IStoredProcedure:
        """ Get: BoundStoredProc(self: SqlCreateAlterProcedureStatementBase) -> IStoredProcedure """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateAlterProcedureStatementBase) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Definition(self) -> SqlProcedureDefinition:
        """ Get: Definition(self: SqlCreateAlterProcedureStatementBase) -> SqlProcedureDefinition """
        ...

    @property
    def Statements(self) -> SqlStatementCollection:
        """ Get: Statements(self: SqlCreateAlterProcedureStatementBase) -> SqlStatementCollection """
        ...



class SqlAlterProcedureStatement(SqlCreateAlterProcedureStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlAlterProcedureStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlAlterProcedureStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlAlterProcedureStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterProcedureStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlAlterProcedureStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlAlterProcedureStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlAlterProcedureStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterProcedureStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateAlterTriggerStatementBase(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateAlterTriggerStatementBase) -> IMetadataObject """
        ...

    @property
    def BoundTrigger(self) -> ITrigger:
        """ Get: BoundTrigger(self: SqlCreateAlterTriggerStatementBase) -> ITrigger """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateAlterTriggerStatementBase) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Definition(self) -> SqlTriggerDefinition:
        """ Get: Definition(self: SqlCreateAlterTriggerStatementBase) -> SqlTriggerDefinition """
        ...

    @property
    def Statements(self) -> SqlStatementCollection:
        """ Get: Statements(self: SqlCreateAlterTriggerStatementBase) -> SqlStatementCollection """
        ...



class SqlAlterTriggerStatement(SqlCreateAlterTriggerStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlAlterTriggerStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlAlterTriggerStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlAlterTriggerStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterTriggerStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlAlterTriggerStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlAlterTriggerStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlAlterTriggerStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterTriggerStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateAlterViewStatementBase(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateAlterViewStatementBase) -> IMetadataObject """
        ...

    @property
    def BoundView(self) -> IView:
        """ Get: BoundView(self: SqlCreateAlterViewStatementBase) -> IView """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateAlterViewStatementBase) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Definition(self) -> SqlViewDefinition:
        """ Get: Definition(self: SqlCreateAlterViewStatementBase) -> SqlViewDefinition """
        ...



class SqlAlterViewStatement(SqlCreateAlterViewStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlAlterViewStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlAlterViewStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlAlterViewStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterViewStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlAlterViewStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlAlterViewStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlAlterViewStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlAlterViewStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlAssignment(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlAssignment(operatorType: SqlAssignmentOperatorType) """
    @property
    def Operator(self) -> SqlAssignmentOperatorType:
        """ Get: Operator(self: SqlAssignment) -> SqlAssignmentOperatorType """
        ...


    def __new__(cls, operatorType:SqlAssignmentOperatorType) -> Self:
        """ __new__(cls: type, operatorType: SqlAssignmentOperatorType) """
        ...


class SqlAssignmentCollection(SqlCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[SqlAssignment]'>, <type 'ISqlCodeCollection[SqlAssignment]'>, <type 'object'>
    """ no doc """
    pass

class SqlAssignmentError(ISqlErrorObject, SqlAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlAssignmentError) -> SqlScalarExpression """
        ...



class SqlAssignmentOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlAssignmentOperatorType, values: AdditionAssignment (2), Assignment (1), BitwiseAndAssignment (7), BitwiseOrAssignment (8), BitwiseXorAssignment (9), DivisionAssignment (5), ModulusAssignment (6), MultiplicationAssignment (4), None (0), SubtractionAssignment (3) """
    AdditionAssignment: SqlAssignmentOperatorType = ...
    Assignment: SqlAssignmentOperatorType = ...
    BitwiseAndAssignment: SqlAssignmentOperatorType = ...
    BitwiseOrAssignment: SqlAssignmentOperatorType = ...
    BitwiseXorAssignment: SqlAssignmentOperatorType = ...
    DivisionAssignment: SqlAssignmentOperatorType = ...
    ModulusAssignment: SqlAssignmentOperatorType = ...
    MultiplicationAssignment: SqlAssignmentOperatorType = ...
    SubtractionAssignment: SqlAssignmentOperatorType = ...
    value__ = ...


class SqlAtTimeZoneExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlAtTimeZoneExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DateValue(self) -> SqlScalarExpression:
        """ Get: DateValue(self: SqlAtTimeZoneExpression) -> SqlScalarExpression """
        ...

    @property
    def TimeZone(self) -> SqlScalarExpression:
        """ Get: TimeZone(self: SqlAtTimeZoneExpression) -> SqlScalarExpression """
        ...



class SqlBackupCertificateStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupCertificateStatement() """
    pass

class SqlBackupRestoreStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupRestoreDatabaseStatement(SqlBackupRestoreStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupDatabaseStatement(SqlBackupRestoreDatabaseStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupDatabaseStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlBackupDatabaseStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlBackupDatabaseStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlBackupDatabaseStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupDatabaseStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlBackupDatabaseStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBackupDatabaseStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBackupDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlBackupRestoreLogStatement(SqlBackupRestoreStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupLogStatement(SqlBackupRestoreLogStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupLogStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlBackupLogStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlBackupLogStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlBackupLogStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupLogStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlBackupLogStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBackupLogStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBackupLogStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupLogStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlBackupRestoreKeyStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupRestoreMasterKeyStatement(SqlBackupRestoreKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupMasterKeyStatement(SqlBackupRestoreMasterKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupMasterKeyStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlBackupMasterKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlBackupMasterKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlBackupMasterKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupMasterKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlBackupMasterKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBackupMasterKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBackupMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlBackupRestoreServiceMasterKeyStatement(SqlBackupRestoreKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupRestoreTableStatement(SqlBackupRestoreStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlBackupServiceMasterKeyStatement(SqlBackupRestoreServiceMasterKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupServiceMasterKeyStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlBackupServiceMasterKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlBackupServiceMasterKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupServiceMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlBackupTableStatement(SqlBackupRestoreTableStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBackupTableStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlBackupTableStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlBackupTableStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlBackupTableStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupTableStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlBackupTableStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlBackupTableStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlBackupTableStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlBackupTableStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlBatch(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Statements(self) -> SqlStatementCollection:
        """ Get: Statements(self: SqlBatch) -> SqlStatementCollection """
        ...



class SqlBatchCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlBatch]'>, <type 'ISqlCodeCollection[SqlBatch]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlBetweenBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BeginExpression(self) -> SqlScalarExpression:
        """ Get: BeginExpression(self: SqlBetweenBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBetweenBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def EndExpression(self) -> SqlScalarExpression:
        """ Get: EndExpression(self: SqlBetweenBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def HasNot(self) -> bool:
        """ Get: HasNot(self: SqlBetweenBooleanExpression) -> bool """
        ...

    @property
    def TestExpression(self) -> SqlScalarExpression:
        """ Get: TestExpression(self: SqlBetweenBooleanExpression) -> SqlScalarExpression """
        ...



class SqlBinaryBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBinaryBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Left(self) -> SqlBooleanExpression:
        """ Get: Left(self: SqlBinaryBooleanExpression) -> SqlBooleanExpression """
        ...

    @property
    def Operator(self) -> SqlBooleanOperatorType:
        """ Get: Operator(self: SqlBinaryBooleanExpression) -> SqlBooleanOperatorType """
        ...

    @property
    def Right(self) -> SqlBooleanExpression:
        """ Get: Right(self: SqlBinaryBooleanExpression) -> SqlBooleanExpression """
        ...



class SqlFilterExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlBinaryFilterExpression(SqlFilterExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBinaryFilterExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Left(self) -> SqlFilterExpression:
        """ Get: Left(self: SqlBinaryFilterExpression) -> SqlFilterExpression """
        ...

    @property
    def Right(self) -> SqlFilterExpression:
        """ Get: Right(self: SqlBinaryFilterExpression) -> SqlFilterExpression """
        ...



class SqlQueryExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlBinaryQueryExpression(SqlQueryExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBinaryQueryExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Left(self) -> SqlQueryExpression:
        """ Get: Left(self: SqlBinaryQueryExpression) -> SqlQueryExpression """
        ...

    @property
    def Operator(self) -> SqlBinaryQueryOperatorType:
        """ Get: Operator(self: SqlBinaryQueryExpression) -> SqlBinaryQueryOperatorType """
        ...

    @property
    def Right(self) -> SqlQueryExpression:
        """ Get: Right(self: SqlBinaryQueryExpression) -> SqlQueryExpression """
        ...



class SqlBinaryQueryOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlBinaryQueryOperatorType, values: Except (3), Intersect (2), Union (0), UnionAll (1) """
    Except: SqlBinaryQueryOperatorType = ...
    Intersect: SqlBinaryQueryOperatorType = ...
    Union: SqlBinaryQueryOperatorType = ...
    UnionAll: SqlBinaryQueryOperatorType = ...
    value__ = ...


class SqlBinaryScalarExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBinaryScalarExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Left(self) -> SqlScalarExpression:
        """ Get: Left(self: SqlBinaryScalarExpression) -> SqlScalarExpression """
        ...

    @property
    def Operator(self) -> SqlBinaryScalarOperatorType:
        """ Get: Operator(self: SqlBinaryScalarExpression) -> SqlBinaryScalarOperatorType """
        ...

    @property
    def Right(self) -> SqlScalarExpression:
        """ Get: Right(self: SqlBinaryScalarExpression) -> SqlScalarExpression """
        ...



class SqlBinaryScalarOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlBinaryScalarOperatorType, values: Add (1), Assign (2), BitwiseAnd (3), BitwiseOr (4), BitwiseXor (5), Divide (6), Equals (7), GreaterThan (8), GreaterThanOrEqual (9), LessThan (10), LessThanOrEqual (11), Modulus (12), Multiply (13), None (0), NotEqualTo (15), NotGreaterThan (16), NotLessThan (17), Subtract (14) """
    Add: SqlBinaryScalarOperatorType = ...
    Assign: SqlBinaryScalarOperatorType = ...
    BitwiseAnd: SqlBinaryScalarOperatorType = ...
    BitwiseOr: SqlBinaryScalarOperatorType = ...
    BitwiseXor: SqlBinaryScalarOperatorType = ...
    Divide: SqlBinaryScalarOperatorType = ...
    Equals: SqlBinaryScalarOperatorType = ...
    GreaterThan: SqlBinaryScalarOperatorType = ...
    GreaterThanOrEqual: SqlBinaryScalarOperatorType = ...
    LessThan: SqlBinaryScalarOperatorType = ...
    LessThanOrEqual: SqlBinaryScalarOperatorType = ...
    Modulus: SqlBinaryScalarOperatorType = ...
    Multiply: SqlBinaryScalarOperatorType = ...
    NotEqualTo: SqlBinaryScalarOperatorType = ...
    NotGreaterThan: SqlBinaryScalarOperatorType = ...
    NotLessThan: SqlBinaryScalarOperatorType = ...
    Subtract: SqlBinaryScalarOperatorType = ...
    value__ = ...


class SqlBooleanExpressionError(SqlBooleanExpression, ISqlErrorObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBooleanExpressionError) -> IEnumerable[SqlCodeObject] """
        ...



class SqlBooleanFilterExpression(SqlFilterExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlBooleanFilterExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlBooleanExpression:
        """ Get: Expression(self: SqlBooleanFilterExpression) -> SqlBooleanExpression """
        ...



class SqlBooleanOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlBooleanOperatorType, values: And (0), Or (1) """
    And: SqlBooleanOperatorType = ...
    Or: SqlBooleanOperatorType = ...
    value__ = ...


class SqlBreakStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlBreakStatement() """
    pass

class SqlBucketCountIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BucketCount(self) -> int:
        """ Get: BucketCount(self: SqlBucketCountIndexOption) -> int """
        ...



class SqlCaseExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ElseExpression(self) -> SqlScalarExpression:
        """ Get: ElseExpression(self: SqlCaseExpression) -> SqlScalarExpression """
        ...


    elseExpression = ...


class SqlCastExpression(SqlBuiltinScalarFunctionCallExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCastExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DataType(self) -> SqlDataTypeSpecification:
        """ Get: DataType(self: SqlCastExpression) -> SqlDataTypeSpecification """
        ...



class SqlChangeTrackingContext(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlChangeTrackingContext() """
    pass

class SqlConstraint(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlConstraint) -> SqlIdentifier """
        ...

    @property
    def Type(self) -> SqlConstraintType:
        """ Get: Type(self: SqlConstraint) -> SqlConstraintType """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlConstraint) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlCheckConstraint(SqlConstraint, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCheckConstraint) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlBooleanExpression:
        """ Get: Expression(self: SqlCheckConstraint) -> SqlBooleanExpression """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: SqlCheckConstraint) -> bool """
        ...



class SqlClrAssemblySpecifier(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> SqlIdentifier:
        """ Get: AssemblyName(self: SqlClrAssemblySpecifier) -> SqlIdentifier """
        ...



class SqlClrClassSpecifier(SqlClrAssemblySpecifier): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ClassName(self) -> SqlIdentifier:
        """ Get: ClassName(self: SqlClrClassSpecifier) -> SqlIdentifier """
        ...



class SqlFunctionBodyDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlClrFunctionBodyDefinition(SqlFunctionBodyDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlClrFunctionBodyDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ClrMethodSpecifier(self) -> SqlClrMethodSpecifier:
        """ Get: ClrMethodSpecifier(self: SqlClrFunctionBodyDefinition) -> SqlClrMethodSpecifier """
        ...



class SqlClrMethodSpecifier(SqlClrClassSpecifier): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def MethodName(self) -> SqlIdentifier:
        """ Get: MethodName(self: SqlClrMethodSpecifier) -> SqlIdentifier """
        ...



class SqlClusterOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlClusterOption, values: Clustered (1), ClusteredColumnstore (5), Default (0), Hash (4), NonClustered (2), NonClusteredColumnstore (6), NonClusteredHash (3) """
    Clustered: SqlClusterOption = ...
    ClusteredColumnstore: SqlClusterOption = ...
    Default: SqlClusterOption = ...
    Hash: SqlClusterOption = ...
    NonClustered: SqlClusterOption = ...
    NonClusteredColumnstore: SqlClusterOption = ...
    NonClusteredHash: SqlClusterOption = ...
    value__ = ...


class SqlCodeObjectRecursiveVisitor: # skipped bases: <type 'object'>
    """ SqlCodeObjectRecursiveVisitor() """
    def Visit(self, codeObject:SqlDropProcedureStatement): # -> 
        """ Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropProcedureStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSimpleCaseExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSetClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectVariableAssignmentExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectStarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectSpecificationInsertSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSimpleGroupByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectScalarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSearchedWhenClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSearchedCaseExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScript)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarVariableRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarVariableAssignment)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectIntoClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarSubQueryExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSimpleOrderByClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSimpleWhenClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableValuedFunctionRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableHint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableFunctionReturnType)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableConstructorInsertSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSimpleOrderByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableConstructorExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlStatisticsOnlyIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlStatisticsNoRecomputeIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlStatisticsIncrementalIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSortInTempDbIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSortedDataReorgIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSortedDataIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableClrFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableVariableRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarRelationalFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarFunctionReturnType)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMaxDurationIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCompressionDelayIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBucketCountIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlResumableIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOnlineIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlObjectReference)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOffsetFetchClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlObjectIdentifier)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlQueryExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlNotBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMultistatementTableRelationalFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMultistatementFunctionBodyDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleViewMetadataOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOrderByClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOutputClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlScalarClrFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRowConstructorExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRollupGroupByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlQueryWithClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlQuerySpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlQualifiedJoinTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOrderByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlProcedureDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlPrimaryKeyConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlPivotTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlPivotClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlParameterDeclaration)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlPadIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlOutputIntoClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlStorageSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleSchemaBindingOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTableUdtInstanceMethodExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTemporalPeriodDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateTriggerStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateTableStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateSynonymStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateSchemaStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateRoleStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateProcedureStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserDefinedDataTypeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateLoginWithPasswordStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateLoginFromCertificateStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateLoginFromAsymKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateIndexStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateFunctionStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlContinueStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCompoundStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateLoginFromWindowsStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCommentStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserDefinedTableTypeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserFromAsymKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropDefaultStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropDatabaseStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropAggregateStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDenyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDeleteStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDBCCStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserDefinedTypeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCursorDeclareStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserWithoutLoginStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserFromExternalProviderStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserFromLoginStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserWithImplicitAuthenticationStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserFromCertificateStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateViewStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTargetTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBreakStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupServiceMasterKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUpdateBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUnqualifiedJoinTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUnpivotTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUnpivotClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUniqueConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUnaryScalarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUpdateMergeAction)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUdtStaticMethodExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUdtInstanceMethodExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUdtInstanceDataMemberExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTriggerEvent)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTriggerDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTriggerAction)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTopSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUdtStaticDataMemberExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupTableStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUpdateSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlValuesInsertMergeActionSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupMasterKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupLogStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupDatabaseStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBackupCertificateStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAlterViewStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAlterTriggerStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUserDefinedScalarFunctionCallExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAlterProcedureStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAlterFunctionStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlXmlNamespacesDeclaration)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlWhereClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlViewDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlVariableDeclaration)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlVariableColumnAssignment)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAlterLoginStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropFunctionStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleReturnsNullOnNullInputOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCastExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBuiltinScalarFunctionCallExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBooleanFilterExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBinaryScalarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBinaryQueryExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlChangeTrackingContext)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBinaryFilterExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBetweenBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBatch)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAtTimeZoneExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAssignment)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAllowRowLocksIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAllowPageLocksIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlBinaryBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAllAnyComparisonBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCheckConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlClrClassSpecifier)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlConditionClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlComputedColumnDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCompressionPartitionRange)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlComparisonBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCommonTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlColumnRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlClrAssemblySpecifier)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlColumnIdentity)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDefaultConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlColumnAssignment)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCollation)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCollateScalarExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlClrMethodSpecifier)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlClrFunctionBodyDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlColumnDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlAggregateFunctionCallExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlVariableDeclareStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIfElseStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGrantStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlExecuteStringStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlExecuteModuleStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropViewStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropUserStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInlineTableVariableDeclareStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropTypeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropTableStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropSynonymStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropSequenceStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropSecurityPolicyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropSchemaStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropRuleStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropTriggerStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlWhileStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInsertStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUseStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlUpdateStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlTryCatchStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSetStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSetAssignmentStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlSelectStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMergeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRevokeStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreTableStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreServiceMasterKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreMasterKeyStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreLogStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreInformationStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlRestoreDatabaseStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlReturnStatement)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleRecompileOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlConvertExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCubeGroupByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInlineFunctionBodyDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInlineIndexConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIndexHint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIndexedColumn)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInBooleanExpressionQueryValue)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInlineTableRelationalFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInBooleanExpressionCollectionValue)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIgnoreDupKeyIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIdentityFunctionCallExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIdentifier)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlHavingClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGroupingSetItemsCollection)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGroupBySets)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGroupByClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInlineTableVariableDeclaration)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInsertSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleNativeCompilationOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleExecuteAsOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleEncryptionOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlModuleCalledOnNullInputOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInsertSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMergeSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlInsertMergeAction)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMergeActionClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlLoginPassword)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlLiteralExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlLikeBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlLargeDataStorageInformation)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIsNullBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlIntoClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlMaxDegreeOfParallelismIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCreateUserOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGrandTotalGroupingSet)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGlobalScalarVariableRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDmlTriggerDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDmlSpecificationTableSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDerivedTableExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDeleteSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDeleteMergeAction)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDefaultValuesInsertSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropExistingIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDefaultValuesInsertMergeActionSource)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDataTypeSpecification)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDataType)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDataCompressionIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCursorVariableRefExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCursorVariableAssignment)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlCursorOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDdlTriggerDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlGrandTotalGroupByItem)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlExecuteArgument)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlExistsBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFunctionDefinition)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFullTextColumn)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFullTextBooleanExpression)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFromClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlRawClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlPathClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlExecuteAsClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlExplicitClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlAutoClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForeignKeyConstraint)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForBrowseClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFilterClause)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlFillFactorIndexOption)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlForXmlDirective)Visit(self: SqlCodeObjectRecursiveVisitor, codeObject: SqlDropLoginStatement) """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class SqlCollateScalarExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCollateScalarExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Collation(self) -> SqlCollation:
        """ Get: Collation(self: SqlCollateScalarExpression) -> SqlCollation """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlCollateScalarExpression) -> SqlScalarExpression """
        ...



class SqlCollation(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundCollation(self) -> ICollation:
        """ Get: BoundCollation(self: SqlCollation) -> ICollation """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCollation) -> SqlIdentifier """
        ...



class SqlCollection(ISqlCodeCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SqlCollection[T]) -> IEnumerator[T] """
        ...


class SqlColumnAssignment(SqlAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlColumnAssignment) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Column(self) -> SqlScalarRefExpression:
        """ Get: Column(self: SqlColumnAssignment) -> SqlScalarRefExpression """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlColumnAssignment) -> SqlScalarExpression """
        ...



class SqlColumnDefinition(SqlCodeObject, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundColumn(self) -> IColumn:
        """ Get: BoundColumn(self: SqlColumnDefinition) -> IColumn """
        ...

    @property
    def Collation(self) -> SqlCollation:
        """ Get: Collation(self: SqlColumnDefinition) -> SqlCollation """
        ...

    @property
    def Constraints(self) -> SqlConstraintCollection:
        """ Get: Constraints(self: SqlColumnDefinition) -> SqlConstraintCollection """
        ...

    @property
    def DataType(self) -> SqlDataTypeSpecification:
        """ Get: DataType(self: SqlColumnDefinition) -> SqlDataTypeSpecification """
        ...

    @property
    def GeneratedAlwaysType(self) -> SqlGeneratedAlwaysType:
        """ Get: GeneratedAlwaysType(self: SqlColumnDefinition) -> SqlGeneratedAlwaysType """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlColumnDefinition) -> SqlIdentifier """
        ...

    @property
    def SparseOption(self) -> SqlSparseOption:
        """ Get: SparseOption(self: SqlColumnDefinition) -> SqlSparseOption """
        ...



class SqlColumnDefinitionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlColumnDefinition]'>, <type 'ISqlCodeCollection[SqlColumnDefinition]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlColumnIdentity(SqlConstraint): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlColumnIdentity) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Increment(self) -> Nullable:
        """ Get: Increment(self: SqlColumnIdentity) -> Nullable[int] """
        ...

    @property
    def NotForReplicationClause(self) -> bool:
        """ Get: NotForReplicationClause(self: SqlColumnIdentity) -> bool """
        ...

    @property
    def Seed(self) -> Nullable:
        """ Get: Seed(self: SqlColumnIdentity) -> Nullable[int] """
        ...



class SqlScalarRefExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarRefExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def MultipartIdentifier(self) -> SqlMultipartIdentifier:
        """ Get: MultipartIdentifier(self: SqlScalarRefExpression) -> SqlMultipartIdentifier """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlScalarRefExpression) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlColumnRefExpression(SqlScalarRefExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundColumn(self) -> IColumn:
        """ Get: BoundColumn(self: SqlColumnRefExpression) -> IColumn """
        ...

    @property
    def ColumnName(self) -> SqlIdentifier:
        """ Get: ColumnName(self: SqlColumnRefExpression) -> SqlIdentifier """
        ...



class SqlColumnRefExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlColumnRefExpression]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlColumnRefExpression]'>, <type 'object'>
    """ no doc """
    pass

class SqlCommentStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlTableExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundTable(self) -> ITabular:
        """ Get: BoundTable(self: SqlTableExpression) -> ITabular """
        ...



class SqlCommonTableExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCommonTableExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlCommonTableExpression) -> SqlIdentifierCollection """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCommonTableExpression) -> SqlIdentifier """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlCommonTableExpression) -> SqlQueryExpression """
        ...



class SqlCommonTableExpressionCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlCommonTableExpression]'>, <type 'IEnumerable[SqlCommonTableExpression]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlComparisonBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlComparisonBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ComparisonOperator(self) -> SqlComparisonBooleanExpressionType:
        """ Get: ComparisonOperator(self: SqlComparisonBooleanExpression) -> SqlComparisonBooleanExpressionType """
        ...

    @property
    def Left(self) -> SqlScalarExpression:
        """ Get: Left(self: SqlComparisonBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def Right(self) -> SqlScalarExpression:
        """ Get: Right(self: SqlComparisonBooleanExpression) -> SqlScalarExpression """
        ...



class SqlComparisonBooleanExpressionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlComparisonBooleanExpressionType, values: Equals (0), GreaterThan (4), GreaterThanOrEqual (5), LeftStarEqualJoin (11), LessOrGreaterThan (6), LessThan (1), LessThanOrEqual (7), NotEqual (3), NotGreaterThan (9), NotLessThan (8), RightStarEqualJoin (10), ValueEqual (2) """
    Equals: SqlComparisonBooleanExpressionType = ...
    GreaterThan: SqlComparisonBooleanExpressionType = ...
    GreaterThanOrEqual: SqlComparisonBooleanExpressionType = ...
    LeftStarEqualJoin: SqlComparisonBooleanExpressionType = ...
    LessOrGreaterThan: SqlComparisonBooleanExpressionType = ...
    LessThan: SqlComparisonBooleanExpressionType = ...
    LessThanOrEqual: SqlComparisonBooleanExpressionType = ...
    NotEqual: SqlComparisonBooleanExpressionType = ...
    NotGreaterThan: SqlComparisonBooleanExpressionType = ...
    NotLessThan: SqlComparisonBooleanExpressionType = ...
    RightStarEqualJoin: SqlComparisonBooleanExpressionType = ...
    ValueEqual: SqlComparisonBooleanExpressionType = ...
    value__ = ...


class SqlCompoundStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCompoundStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Statements(self) -> SqlStatementCollection:
        """ Get: Statements(self: SqlCompoundStatement) -> SqlStatementCollection """
        ...



class SqlCompressionDelayIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def CompressionDelay(self) -> int:
        """ Get: CompressionDelay(self: SqlCompressionDelayIndexOption) -> int """
        ...



class SqlCompressionPartitionRange(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def From(self) -> SqlScalarExpression:
        """ Get: From(self: SqlCompressionPartitionRange) -> SqlScalarExpression """
        ...

    @property
    def To(self) -> SqlScalarExpression:
        """ Get: To(self: SqlCompressionPartitionRange) -> SqlScalarExpression """
        ...



class SqlCompressionPartitionRangeCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlCompressionPartitionRange]'>, <type 'ISqlCodeCollection[SqlCompressionPartitionRange]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlComputedColumnDefinition(SqlColumnDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'ISqlTableElement'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlComputedColumnDefinition) -> SqlScalarExpression """
        ...

    @property
    def IsPersisted(self) -> bool:
        """ Get: IsPersisted(self: SqlComputedColumnDefinition) -> bool """
        ...



class SqlConditionalStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Condition(self) -> SqlBooleanExpression:
        """ Get: Condition(self: SqlConditionalStatement) -> SqlBooleanExpression """
        ...

    @property
    def TrueStatement(self) -> SqlStatement:
        """ Get: TrueStatement(self: SqlConditionalStatement) -> SqlStatement """
        ...



class SqlConditionClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> SqlBooleanExpression:
        """ Get: Expression(self: SqlConditionClause) -> SqlBooleanExpression """
        ...



class SqlConstraintCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlConstraint]'>, <type 'IEnumerable[SqlConstraint]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlConstraintType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlConstraintType, values: Check (6), Default (5), ForeignKey (7), Identity (4), NotNull (1), Null (0), PrimaryKey (2), RowGuidCol (8), Unique (3) """
    Check: SqlConstraintType = ...
    Default: SqlConstraintType = ...
    ForeignKey: SqlConstraintType = ...
    Identity: SqlConstraintType = ...
    NotNull: SqlConstraintType = ...
    Null: SqlConstraintType = ...
    PrimaryKey: SqlConstraintType = ...
    RowGuidCol: SqlConstraintType = ...
    Unique: SqlConstraintType = ...
    value__ = ...


class SqlContinueStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlContinueStatement() """
    pass

class SqlConvertExpression(SqlCastExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlCreateFunctionStatement(SqlCreateAlterFunctionStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateFunctionStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateFunctionStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateFunctionStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateFunctionStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateFunctionStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateFunctionStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateFunctionStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateFunctionStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateIndexStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundIndex(self) -> IRelationalIndex:
        """ Get: BoundIndex(self: SqlCreateIndexStatement) -> IRelationalIndex """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateIndexStatement) -> IMetadataObject """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateIndexStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ClusterOption(self) -> SqlClusterOption:
        """ Get: ClusterOption(self: SqlCreateIndexStatement) -> SqlClusterOption """
        ...

    @property
    def FileStream(self) -> SqlStorageSpecification:
        """ Get: FileStream(self: SqlCreateIndexStatement) -> SqlStorageSpecification """
        ...

    @property
    def FilterClause(self) -> SqlFilterClause:
        """ Get: FilterClause(self: SqlCreateIndexStatement) -> SqlFilterClause """
        ...

    @property
    def IncludedColumns(self) -> SqlIdentifierCollection:
        """ Get: IncludedColumns(self: SqlCreateIndexStatement) -> SqlIdentifierCollection """
        ...

    @property
    def IndexedColunms(self) -> SqlIndexedColumnCollection:
        """ Get: IndexedColunms(self: SqlCreateIndexStatement) -> SqlIndexedColumnCollection """
        ...

    @property
    def IsUnique(self) -> bool:
        """ Get: IsUnique(self: SqlCreateIndexStatement) -> bool """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCreateIndexStatement) -> SqlIdentifier """
        ...

    @property
    def Options(self) -> SqlIndexOptionCollection:
        """ Get: Options(self: SqlCreateIndexStatement) -> SqlIndexOptionCollection """
        ...

    @property
    def StorageSpecification(self) -> SqlStorageSpecification:
        """ Get: StorageSpecification(self: SqlCreateIndexStatement) -> SqlStorageSpecification """
        ...

    @property
    def TargetObject(self) -> SqlObjectIdentifier:
        """ Get: TargetObject(self: SqlCreateIndexStatement) -> SqlObjectIdentifier """
        ...


    @staticmethod
    def BindIndexOptions(options, boundIndex, mustBeOnline) -> bool:
        """ BindIndexOptions(options: SqlIndexOptionCollection, boundIndex: IMutableRelationalIndex) -> bool """
        ...


class SqlCreateLoginStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundLogin(self) -> ILogin:
        """ Get: BoundLogin(self: SqlCreateLoginStatement) -> ILogin """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateLoginStatement) -> IMetadataObject """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCreateLoginStatement) -> SqlIdentifier """
        ...



class SqlCreateLoginFromAsymKeyStatement(SqlCreateLoginStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def AsymKeyName(self) -> SqlIdentifier:
        """ Get: AsymKeyName(self: SqlCreateLoginFromAsymKeyStatement) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateLoginFromAsymKeyStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Credential(self) -> SqlIdentifier:
        """ Get: Credential(self: SqlCreateLoginFromAsymKeyStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromAsymKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateLoginFromCertificateStatement(SqlCreateLoginStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def CertificateName(self) -> SqlIdentifier:
        """ Get: CertificateName(self: SqlCreateLoginFromCertificateStatement) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateLoginFromCertificateStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Credential(self) -> SqlIdentifier:
        """ Get: Credential(self: SqlCreateLoginFromCertificateStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateLoginFromCertificateStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateLoginFromCertificateStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromCertificateStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateLoginFromWindowsStatement(SqlCreateLoginStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateLoginFromWindowsStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DefaultDatabase(self) -> SqlIdentifier:
        """ Get: DefaultDatabase(self: SqlCreateLoginFromWindowsStatement) -> SqlIdentifier """
        ...

    @property
    def DefaultLanguage(self) -> SqlIdentifier:
        """ Get: DefaultLanguage(self: SqlCreateLoginFromWindowsStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateLoginFromWindowsStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateLoginFromWindowsStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginFromWindowsStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateLoginWithPasswordStatement(SqlCreateLoginStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def CheckExpiration(self) -> SqlOnOffValue:
        """ Get: CheckExpiration(self: SqlCreateLoginWithPasswordStatement) -> SqlOnOffValue """
        ...

    @property
    def CheckPolicy(self) -> SqlOnOffValue:
        """ Get: CheckPolicy(self: SqlCreateLoginWithPasswordStatement) -> SqlOnOffValue """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateLoginWithPasswordStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Credential(self) -> SqlIdentifier:
        """ Get: Credential(self: SqlCreateLoginWithPasswordStatement) -> SqlIdentifier """
        ...

    @property
    def DefaultDatabase(self) -> SqlIdentifier:
        """ Get: DefaultDatabase(self: SqlCreateLoginWithPasswordStatement) -> SqlIdentifier """
        ...

    @property
    def DefaultLanguage(self) -> SqlIdentifier:
        """ Get: DefaultLanguage(self: SqlCreateLoginWithPasswordStatement) -> SqlIdentifier """
        ...

    @property
    def Sid(self) -> SqlLiteralExpression:
        """ Get: Sid(self: SqlCreateLoginWithPasswordStatement) -> SqlLiteralExpression """
        ...

    @property
    def SqlPassword(self) -> SqlLoginPassword:
        """ Get: SqlPassword(self: SqlCreateLoginWithPasswordStatement) -> SqlLoginPassword """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateLoginWithPasswordStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateLoginWithPasswordStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateLoginWithPasswordStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateProcedureStatement(SqlCreateAlterProcedureStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateProcedureStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateProcedureStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateProcedureStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateProcedureStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateProcedureStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateProcedureStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateProcedureStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateProcedureStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateRoleStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateRoleStatement) -> IMetadataObject """
        ...

    @property
    def BoundRole(self) -> IDatabaseRole:
        """ Get: BoundRole(self: SqlCreateRoleStatement) -> IDatabaseRole """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateRoleStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCreateRoleStatement) -> SqlIdentifier """
        ...

    @property
    def Owner(self) -> SqlIdentifier:
        """ Get: Owner(self: SqlCreateRoleStatement) -> SqlIdentifier """
        ...



class SqlCreateSchemaStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateSchemaStatement) -> IMetadataObject """
        ...

    @property
    def BoundSchema(self) -> ISchema:
        """ Get: BoundSchema(self: SqlCreateSchemaStatement) -> ISchema """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateSchemaStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCreateSchemaStatement) -> SqlIdentifier """
        ...

    @property
    def Owner(self) -> SqlIdentifier:
        """ Get: Owner(self: SqlCreateSchemaStatement) -> SqlIdentifier """
        ...

    @property
    def SchemaElements(self) -> SqlSchemaElementCollection:
        """ Get: SchemaElements(self: SqlCreateSchemaStatement) -> SqlSchemaElementCollection """
        ...



class SqlCreateSynonymStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BaseObjectName(self) -> SqlObjectIdentifier:
        """ Get: BaseObjectName(self: SqlCreateSynonymStatement) -> SqlObjectIdentifier """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateSynonymStatement) -> IMetadataObject """
        ...

    @property
    def BoundSynonym(self) -> ISynonym:
        """ Get: BoundSynonym(self: SqlCreateSynonymStatement) -> ISynonym """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateSynonymStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlCreateSynonymStatement) -> SqlObjectIdentifier """
        ...



class SqlCreateTableStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateTableStatement) -> IMetadataObject """
        ...

    @property
    def BoundTable(self) -> ITabular:
        """ Get: BoundTable(self: SqlCreateTableStatement) -> ITabular """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateTableStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Definition(self) -> SqlTableDefinition:
        """ Get: Definition(self: SqlCreateTableStatement) -> SqlTableDefinition """
        ...

    @property
    def LargeDataStorageInformation(self) -> SqlLargeDataStorageInformation:
        """ Get: LargeDataStorageInformation(self: SqlCreateTableStatement) -> SqlLargeDataStorageInformation """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlCreateTableStatement) -> SqlObjectIdentifier """
        ...

    @property
    def StorageSpecification(self) -> SqlStorageSpecification:
        """ Get: StorageSpecification(self: SqlCreateTableStatement) -> SqlStorageSpecification """
        ...



class SqlCreateTriggerStatement(SqlCreateAlterTriggerStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateTriggerStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateTriggerStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateTriggerStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateTriggerStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateTriggerStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateTriggerStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateTriggerStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateTriggerStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateTypeStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundDataType(self) -> IUserDefinedType:
        """ Get: BoundDataType(self: SqlCreateTypeStatement) -> IUserDefinedType """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateTypeStatement) -> IMetadataObject """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlCreateTypeStatement) -> SqlObjectIdentifier """
        ...



class SqlCreateUserDefinedDataTypeStatement(SqlCreateTypeStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserDefinedDataTypeStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DataType(self) -> SqlDataTypeSpecification:
        """ Get: DataType(self: SqlCreateUserDefinedDataTypeStatement) -> SqlDataTypeSpecification """
        ...

    @property
    def NullState(self) -> SqlUserDefinedDataTypeNullState:
        """ Get: NullState(self: SqlCreateUserDefinedDataTypeStatement) -> SqlUserDefinedDataTypeNullState """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedDataTypeStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserDefinedTableTypeStatement(SqlCreateTypeStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserDefinedTableTypeStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TableDefinition(self) -> SqlTableDefinition:
        """ Get: TableDefinition(self: SqlCreateUserDefinedTableTypeStatement) -> SqlTableDefinition """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedTableTypeStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserDefinedTypeStatement(SqlCreateTypeStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserDefinedTypeStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ClrClassSpecifier(self) -> SqlClrClassSpecifier:
        """ Get: ClrClassSpecifier(self: SqlCreateUserDefinedTypeStatement) -> SqlClrClassSpecifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserDefinedTypeStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserDefinedTypeStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserDefinedTypeStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlCreateUserStatement) -> IMetadataObject """
        ...

    @property
    def BoundUser(self) -> IUser:
        """ Get: BoundUser(self: SqlCreateUserStatement) -> IUser """
        ...

    @property
    def DefaultSchema(self) -> SqlIdentifier:
        """ Get: DefaultSchema(self: SqlCreateUserStatement) -> SqlIdentifier """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCreateUserStatement) -> SqlIdentifier """
        ...



class SqlCreateUserFromAsymKeyStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def AsymKeyName(self) -> SqlIdentifier:
        """ Get: AsymKeyName(self: SqlCreateUserFromAsymKeyStatement) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserFromAsymKeyStatement) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromAsymKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserFromCertificateStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def CertificateName(self) -> SqlIdentifier:
        """ Get: CertificateName(self: SqlCreateUserFromCertificateStatement) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserFromCertificateStatement) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserFromCertificateStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserFromCertificateStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromCertificateStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromCertificateStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserFromCertificateStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserFromCertificateStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromCertificateStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromCertificateStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserFromExternalProviderStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserFromExternalProviderStatement) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromExternalProviderStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserFromLoginStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserFromLoginStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def LoginName(self) -> SqlIdentifier:
        """ Get: LoginName(self: SqlCreateUserFromLoginStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserFromLoginStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserFromLoginStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromLoginStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromLoginStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserFromLoginStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserFromLoginStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserFromLoginStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserFromLoginStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """
    SqlCreateUserOption(stringToken: StringToken, value: SqlIdentifier)
    SqlCreateUserOption(stringToken: StringToken, literalExpression: SqlLiteralExpression)
    """
    @property
    def Type(self) -> SqlCreateUserOptionType:
        """ Get: Type(self: SqlCreateUserOption) -> SqlCreateUserOptionType """
        ...

    @property
    def Value(self) -> SqlIdentifier:
        """ Get: Value(self: SqlCreateUserOption) -> SqlIdentifier """
        ...


    def __new__(cls, stringToken:StringToken, *__args:SqlIdentifier) -> Self:
        """
        __new__(cls: type, stringToken: StringToken, value: SqlIdentifier)
        __new__(cls: type, stringToken: StringToken, literalExpression: SqlLiteralExpression)
        """
        ...


class SqlCreateUserOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlCreateUserOptionType, values: DefaultLanguage (1), DefaultSchema (2), Invalid (0), Password (3) """
    DefaultLanguage: SqlCreateUserOptionType = ...
    DefaultSchema: SqlCreateUserOptionType = ...
    Invalid: SqlCreateUserOptionType = ...
    Password: SqlCreateUserOptionType = ...
    value__ = ...


class SqlCreateUserStatementError(ISqlErrorObject, SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserStatementError) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserStatementError, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserStatementError, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserStatementError, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserStatementError, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserStatementError, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserStatementError, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserStatementError, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserStatementError, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserWithImplicitAuthenticationStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserWithImplicitAuthenticationStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DefaultLanguage(self) -> SqlIdentifier:
        """ Get: DefaultLanguage(self: SqlCreateUserWithImplicitAuthenticationStatement) -> SqlIdentifier """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: SqlCreateUserWithImplicitAuthenticationStatement) -> str """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserWithImplicitAuthenticationStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateUserWithoutLoginStatement(SqlCreateUserStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCreateUserWithoutLoginStatement) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateUserWithoutLoginStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateUserWithoutLoginStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateUserWithoutLoginStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCreateViewStatement(SqlCreateAlterViewStatementBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlCreateViewStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlCreateViewStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlCreateViewStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateViewStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlCreateViewStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCreateViewStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCreateViewStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCreateViewStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlGroupByItem(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlGroupingSetItem(SqlGroupByItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlCubeGroupByItem(SqlGroupingSetItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCubeGroupByItem) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Items(self) -> SqlCubeRollupArgumentCollection:
        """ Get: Items(self: SqlCubeGroupByItem) -> SqlCubeRollupArgumentCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlCubeGroupByItem, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCubeGroupByItem, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCubeGroupByItem, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCubeGroupByItem, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCubeRollupArgumentCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlSimpleGroupByItem]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlSimpleGroupByItem]'>, <type 'object'>
    """ no doc """
    pass

class SqlDeclareStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlCursorDeclareStatement(SqlDeclareStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlCursorDeclareStatement(name: SqlIdentifier, options: List[SqlCursorOption], definitionInfo: CursorDefinitionInfo) """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCursorDeclareStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlCursorDeclareStatement) -> SqlIdentifier """
        ...

    @property
    def Options(self) -> IEnumerable:
        """ Get: Options(self: SqlCursorDeclareStatement) -> IEnumerable[SqlCursorOption] """
        ...

    @property
    def SelectStatement(self) -> SqlSelectStatement:
        """ Get: SelectStatement(self: SqlCursorDeclareStatement) -> SqlSelectStatement """
        ...


    def __new__(cls, name:SqlIdentifier, options:List, definitionInfo:CursorDefinitionInfo) -> Self:
        """ __new__(cls: type, name: SqlIdentifier, options: List[SqlCursorOption], definitionInfo: CursorDefinitionInfo) """
        ...


class SqlCursorOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlCursorOption(token: StringToken) """
    @property
    def Type(self) -> SqlCursorOptionType:
        """ Get: Type(self: SqlCursorOption) -> SqlCursorOptionType """
        ...


    def __new__(cls, token:StringToken) -> Self:
        """ __new__(cls: type, token: StringToken) """
        ...


class SqlCursorOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlCursorOptionType, values: Dynamic (8), FastForward (9), ForwardOnly (5), Global (4), Insensitive (1), Invalid (0), Keyset (7), Local (3), Optimistic (12), ReadOnly (10), Scroll (2), ScrollLocks (11), Static (6), TypeWarning (13) """
    Dynamic: SqlCursorOptionType = ...
    FastForward: SqlCursorOptionType = ...
    ForwardOnly: SqlCursorOptionType = ...
    Global: SqlCursorOptionType = ...
    Insensitive: SqlCursorOptionType = ...
    Invalid: SqlCursorOptionType = ...
    Keyset: SqlCursorOptionType = ...
    Local: SqlCursorOptionType = ...
    Optimistic: SqlCursorOptionType = ...
    ReadOnly: SqlCursorOptionType = ...
    Scroll: SqlCursorOptionType = ...
    ScrollLocks: SqlCursorOptionType = ...
    Static: SqlCursorOptionType = ...
    TypeWarning: SqlCursorOptionType = ...
    value__ = ...


class SqlVariableAssignment(SqlAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlVariableAssignment(operatorType: SqlAssignmentOperatorType) """
    pass

class SqlCursorVariableAssignment(SqlVariableAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlCursorVariableAssignment(variable: SqlCursorVariableRefExpression, definitionInfo: CursorDefinitionInfo) """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlCursorVariableAssignment) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Options(self) -> IEnumerable:
        """ Get: Options(self: SqlCursorVariableAssignment) -> IEnumerable[SqlCursorOption] """
        ...

    @property
    def SelectStatement(self) -> SqlSelectStatement:
        """ Get: SelectStatement(self: SqlCursorVariableAssignment) -> SqlSelectStatement """
        ...

    @property
    def Variable(self) -> SqlCursorVariableRefExpression:
        """ Get: Variable(self: SqlCursorVariableAssignment) -> SqlCursorVariableRefExpression """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlCursorVariableAssignment, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlCursorVariableAssignment, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlCursorVariableAssignment, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlCursorVariableAssignment, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlCursorVariableRefExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: SqlCursorVariableRefExpression) -> str """
        ...


    @staticmethod
    def Create(variableName:str) -> SqlCursorVariableRefExpression:
        """ Create(variableName: str) -> SqlCursorVariableRefExpression """
        ...


class SqlCursorVariableRefExpressionError(ISqlErrorObject, SqlCursorVariableRefExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlDataCompressionIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDataCompressionIndexOption) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def CompressionType(self) -> SqlDataCompressionType:
        """ Get: CompressionType(self: SqlDataCompressionIndexOption) -> SqlDataCompressionType """
        ...



class SqlDataCompressionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDataCompressionType, values: ColumnStore (3), ColumnStoreArchive (4), Invalid (5), None (0), Page (2), Row (1) """
    ColumnStore: SqlDataCompressionType = ...
    ColumnStoreArchive: SqlDataCompressionType = ...
    Invalid: SqlDataCompressionType = ...
    Page: SqlDataCompressionType = ...
    Row: SqlDataCompressionType = ...
    value__ = ...


class SqlDataType(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def National(self) -> bool:
        """ Get: National(self: SqlDataType) -> bool """
        ...

    @property
    def ObjectIdentifier(self) -> SqlObjectIdentifier:
        """ Get: ObjectIdentifier(self: SqlDataType) -> SqlObjectIdentifier """
        ...

    @property
    def Varying(self) -> bool:
        """ Get: Varying(self: SqlDataType) -> bool """
        ...


    def GetTypeSpec(self) -> DataTypeSpec:
        """ GetTypeSpec(self: SqlDataType) -> DataTypeSpec """
        ...


class SqlDataTypeSpecification(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Argument1(self) -> Nullable:
        """ Get: Argument1(self: SqlDataTypeSpecification) -> Nullable[int] """
        ...

    @property
    def Argument2(self) -> Nullable:
        """ Get: Argument2(self: SqlDataTypeSpecification) -> Nullable[int] """
        ...

    @property
    def BoundType(self) -> IDataType:
        """ Get: BoundType(self: SqlDataTypeSpecification) -> IDataType """
        ...

    @property
    def DataType(self) -> SqlDataType:
        """ Get: DataType(self: SqlDataTypeSpecification) -> SqlDataType """
        ...

    @property
    def IsCursor(self) -> bool:
        """ Get: IsCursor(self: SqlDataTypeSpecification) -> bool """
        ...

    @property
    def IsMaximum(self) -> bool:
        """ Get: IsMaximum(self: SqlDataTypeSpecification) -> bool """
        ...

    @property
    def XmlDocumentConstraint(self) -> SqlXmlDocumentConstraint:
        """ Get: XmlDocumentConstraint(self: SqlDataTypeSpecification) -> SqlXmlDocumentConstraint """
        ...

    @property
    def XmlSchemaCollection(self) -> SqlObjectIdentifier:
        """ Get: XmlSchemaCollection(self: SqlDataTypeSpecification) -> SqlObjectIdentifier """
        ...



class SqlDbccCommandType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDbccCommandType, values: DbRepair (2), NewAlloc (1), None (0), RowLock (3), TextAll (4), TextAlloc (5), TraceOn (6) """
    DbRepair: SqlDbccCommandType = ...
    NewAlloc: SqlDbccCommandType = ...
    RowLock: SqlDbccCommandType = ...
    TextAll: SqlDbccCommandType = ...
    TextAlloc: SqlDbccCommandType = ...
    TraceOn: SqlDbccCommandType = ...
    value__ = ...


class SqlDBCCStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def CommandType(self) -> SqlDbccCommandType:
        """ Get: CommandType(self: SqlDBCCStatement) -> SqlDbccCommandType """
        ...



class SqlTriggerDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ActivationType(self) -> SqlTriggerActivationType:
        """ Get: ActivationType(self: SqlTriggerDefinition) -> SqlTriggerActivationType """
        ...

    @property
    def IsOrAlterStatement(self) -> bool:
        """
        Get: IsOrAlterStatement(self: SqlTriggerDefinition) -> bool
        Set: IsOrAlterStatement(self: SqlTriggerDefinition) = value
        """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlTriggerDefinition) -> SqlObjectIdentifier """
        ...

    @property
    def Options(self) -> SqlCollection:
        """ Get: Options(self: SqlTriggerDefinition) -> SqlCollection[SqlModuleOption] """
        ...



class SqlDdlTriggerDefinition(SqlTriggerDefinition, IDdlTriggerDefinitionInfo): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDdlTriggerDefinition) -> IEnumerable[SqlCodeObject] """
        ...



class SqlDdlTriggerTargetType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDdlTriggerTargetType, values: AllServer (1), Database (0) """
    AllServer: SqlDdlTriggerTargetType = ...
    Database: SqlDdlTriggerTargetType = ...
    value__ = ...


class SqlDefaultConstraint(SqlConstraint, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDefaultConstraint) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlDefaultConstraint) -> SqlScalarExpression """
        ...



class SqlInsertMergeActionSource(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlDefaultValuesInsertMergeActionSource(SqlInsertMergeActionSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlDefaultValuesInsertMergeActionSource() """
    pass

class SqlInsertSource(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlDefaultValuesInsertSource(SqlInsertSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlDefaultValuesInsertSource() """
    pass

class SqlMergeAction(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlDeleteMergeAction(SqlMergeAction): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlDeleteMergeAction() """
    pass

class SqlDmlSpecification(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OutputClause(self) -> SqlOutputClause:
        """ Get: OutputClause(self: SqlDmlSpecification) -> SqlOutputClause """
        ...

    @property
    def OutputIntoClause(self) -> SqlOutputIntoClause:
        """ Get: OutputIntoClause(self: SqlDmlSpecification) -> SqlOutputIntoClause """
        ...

    @property
    def Target(self) -> SqlTableExpression:
        """ Get: Target(self: SqlDmlSpecification) -> SqlTableExpression """
        ...

    @property
    def TopSpecification(self) -> SqlTopSpecification:
        """ Get: TopSpecification(self: SqlDmlSpecification) -> SqlTopSpecification """
        ...



class SqlUpdateDeleteSpecificationBase(SqlDmlSpecification): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def FromClause(self) -> SqlFromClause:
        """ Get: FromClause(self: SqlUpdateDeleteSpecificationBase) -> SqlFromClause """
        ...

    @property
    def WhereClause(self) -> SqlWhereClause:
        """ Get: WhereClause(self: SqlUpdateDeleteSpecificationBase) -> SqlWhereClause """
        ...



class SqlDeleteSpecification(SqlUpdateDeleteSpecificationBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDeleteSpecification) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlDeleteSpecification, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDeleteSpecification, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDeleteSpecification, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDeleteSpecification, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDmlStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDmlStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def QueryWithClause(self) -> SqlQueryWithClause:
        """ Get: QueryWithClause(self: SqlDmlStatement) -> SqlQueryWithClause """
        ...



class SqlDeleteStatement(SqlDmlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def DeleteSpecification(self) -> SqlDeleteSpecification:
        """ Get: DeleteSpecification(self: SqlDeleteStatement) -> SqlDeleteSpecification """
        ...



class SqlGdrStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlDenyStatement(SqlGdrStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlDerivedTableExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlDerivedTableExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDerivedTableExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlDerivedTableExpression) -> SqlIdentifierCollection """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlDerivedTableExpression) -> SqlQueryExpression """
        ...



class SqlDmlSpecificationTableSource(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlDmlSpecificationTableSource) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDmlSpecificationTableSource) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlDmlSpecificationTableSource) -> SqlIdentifierCollection """
        ...

    @property
    def DmlSpecification(self) -> SqlDmlSpecification:
        """ Get: DmlSpecification(self: SqlDmlSpecificationTableSource) -> SqlDmlSpecification """
        ...



class SqlDmlTriggerDefinition(SqlTriggerDefinition, IDmlTriggerDefinitionInfo): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDmlTriggerDefinition) -> IEnumerable[SqlCodeObject] """
        ...



class SqlDropStatement(SqlDdlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlDropAggregateStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropAggregateStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropAggregateStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropAggregateStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropAggregateStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropAggregateStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropAggregateStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropAggregateStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropAggregateStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropAggregateStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropAggregateStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropDatabaseStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropDatabaseStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DatabaseNames(self) -> SqlIdentifierCollection:
        """ Get: DatabaseNames(self: SqlDropDatabaseStatement) -> SqlIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropDatabaseStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropDatabaseStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropDatabaseStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropDatabaseStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropDatabaseStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropDatabaseStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropDefaultStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropDefaultStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropDefaultStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropDefaultStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropDefaultStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropDefaultStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropDefaultStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropDefaultStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropDefaultStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropDefaultStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropDefaultStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropExistingIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlDropExistingIndexOption) -> SqlOnOffValue """
        ...



class SqlDropFunctionStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropFunctionStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropFunctionStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropFunctionStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropFunctionStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropFunctionStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropFunctionStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropFunctionStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropFunctionStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropFunctionStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropFunctionStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropLoginStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropLoginStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def LoginName(self) -> SqlIdentifier:
        """ Get: LoginName(self: SqlDropLoginStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropLoginStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropLoginStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropLoginStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropLoginStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropLoginStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropLoginStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropLoginStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropLoginStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropObjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDropObjectType, values: Aggregate (8), Default (6), Function (3), Proc (1), Procedure (2), Rule (5), SecurityPolicy (11), Sequence (10), Synonym (9), Table (0), Trigger (7), View (4) """
    Aggregate: SqlDropObjectType = ...
    Default: SqlDropObjectType = ...
    Function: SqlDropObjectType = ...
    Proc: SqlDropObjectType = ...
    Procedure: SqlDropObjectType = ...
    Rule: SqlDropObjectType = ...
    SecurityPolicy: SqlDropObjectType = ...
    Sequence: SqlDropObjectType = ...
    Synonym: SqlDropObjectType = ...
    Table: SqlDropObjectType = ...
    Trigger: SqlDropObjectType = ...
    value__ = ...
    View: SqlDropObjectType = ...


class SqlDropProcedureStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropProcedureStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropProcedureStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropProcedureStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropProcedureStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropProcedureStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropProcedureStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropProcedureStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropProcedureStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropProcedureStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropProcedureStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropRuleStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropRuleStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropRuleStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropRuleStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropRuleStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropRuleStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropRuleStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropRuleStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropRuleStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropRuleStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropRuleStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropSchemaStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropSchemaStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def SchemaName(self) -> SqlIdentifier:
        """ Get: SchemaName(self: SqlDropSchemaStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropSchemaStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropSchemaStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropSchemaStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSchemaStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropSchemaStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropSchemaStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropSchemaStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSchemaStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropSecurityPolicyStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropSecurityPolicyStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropSecurityPolicyStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropSecurityPolicyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropSecurityPolicyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropSecurityPolicyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSecurityPolicyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropSecurityPolicyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropSecurityPolicyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropSecurityPolicyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSecurityPolicyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropSequenceStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropSequenceStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropSequenceStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropSequenceStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropSequenceStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropSequenceStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSequenceStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropSequenceStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropSequenceStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropSequenceStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSequenceStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropSynonymStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropSynonymStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropSynonymStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropSynonymStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropSynonymStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropSynonymStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSynonymStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropSynonymStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropSynonymStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropSynonymStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropSynonymStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropTableStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropTableStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropTableStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropTableStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropTableStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropTableStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTableStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropTableStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropTableStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropTableStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTableStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropTriggerStatement(SqlDropStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropTriggerStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropTriggerStatement) -> SqlObjectIdentifierCollection """
        ...

    @property
    def TargetScope(self) -> SqlDropTriggerTargetScope:
        """ Get: TargetScope(self: SqlDropTriggerStatement) -> SqlDropTriggerTargetScope """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropTriggerStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropTriggerStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropTriggerStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTriggerStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropTriggerStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropTriggerStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropTriggerStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTriggerStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropTriggerTargetScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDropTriggerTargetScope, values: AllServer (2), Database (1), None (0) """
    AllServer: SqlDropTriggerTargetScope = ...
    Database: SqlDropTriggerTargetScope = ...
    value__ = ...


class SqlDropTypeStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropTypeStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TypeName(self) -> SqlObjectIdentifier:
        """ Get: TypeName(self: SqlDropTypeStatement) -> SqlObjectIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropTypeStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropTypeStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropTypeStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTypeStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropTypeStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropTypeStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropTypeStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropTypeStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropUserStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropUserStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def UserName(self) -> SqlIdentifier:
        """ Get: UserName(self: SqlDropUserStatement) -> SqlIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropUserStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropUserStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropUserStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropUserStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropUserStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropUserStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropUserStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropUserStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlDropViewStatement(SqlDropStatement, IDropObjectStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IBindFinalizer'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlDropViewStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Objects(self) -> SqlObjectIdentifierCollection:
        """ Get: Objects(self: SqlDropViewStatement) -> SqlObjectIdentifierCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlDropViewStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlDropViewStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlDropViewStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropViewStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlDropViewStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlDropViewStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlDropViewStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlDropViewStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlErrorCodeObject(ISqlErrorObject, SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlExecuteArgument(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundParameter(self) -> IParameter:
        """ Get: BoundParameter(self: SqlExecuteArgument) -> IParameter """
        ...

    @property
    def IsOutput(self) -> bool:
        """ Get: IsOutput(self: SqlExecuteArgument) -> bool """
        ...

    @property
    def Parameter(self) -> SqlScalarVariableRefExpression:
        """ Get: Parameter(self: SqlExecuteArgument) -> SqlScalarVariableRefExpression """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlExecuteArgument) -> SqlScalarExpression """
        ...



class SqlExecuteArgumentCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlExecuteArgument]'>, <type 'IEnumerable[SqlExecuteArgument]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlExecuteAsClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundExecutionContext(self) -> IExecutionContext:
        """ Get: BoundExecutionContext(self: SqlExecuteAsClause) -> IExecutionContext """
        ...

    @property
    def Type(self) -> SqlModuleExecutionContextType:
        """ Get: Type(self: SqlExecuteAsClause) -> SqlModuleExecutionContextType """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: SqlExecuteAsClause) -> str """
        ...



class SqlExecuteStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlExecuteModuleStatement(SqlExecuteStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlExecuteArgumentCollection:
        """ Get: Arguments(self: SqlExecuteModuleStatement) -> SqlExecuteArgumentCollection """
        ...

    @property
    def BoundModule(self) -> ICallableModule:
        """ Get: BoundModule(self: SqlExecuteModuleStatement) -> ICallableModule """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlExecuteModuleStatement) -> IMetadataObject """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlExecuteModuleStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Module(self) -> SqlObjectReference:
        """ Get: Module(self: SqlExecuteModuleStatement) -> SqlObjectReference """
        ...

    @property
    def ModuleOption(self) -> SqlModuleOption:
        """ Get: ModuleOption(self: SqlExecuteModuleStatement) -> SqlModuleOption """
        ...

    @property
    def Number(self) -> Nullable:
        """ Get: Number(self: SqlExecuteModuleStatement) -> Nullable[int] """
        ...

    @property
    def ReturnValue(self) -> SqlScalarVariableRefExpression:
        """ Get: ReturnValue(self: SqlExecuteModuleStatement) -> SqlScalarVariableRefExpression """
        ...



class SqlStatementError(ISqlErrorObject, SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlStatementError) -> IEnumerable[SqlCodeObject] """
        ...



class SqlExecuteStatementError(SqlStatementError): # skipped bases: <type 'ISqlErrorObject'>, <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlExecuteStringStatement(SqlExecuteStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlExecuteStringStatement) -> IEnumerable[SqlCodeObject] """
        ...



class SqlExistsBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlExistsBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlExistsBooleanExpression) -> SqlQueryExpression """
        ...



class SqlFillFactorIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def FillFactor(self) -> int:
        """ Get: FillFactor(self: SqlFillFactorIndexOption) -> int """
        ...



class SqlFilterClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def FilterExpression(self) -> SqlFilterExpression:
        """ Get: FilterExpression(self: SqlFilterClause) -> SqlFilterExpression """
        ...



class SqlForClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlForBrowseClause(SqlForClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlForBrowseClause() """
    pass

class SqlForeignKeyAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlForeignKeyAction, values: Cascade (2), NoAction (1), None (0), SetDefault (3), SetNull (4) """
    Cascade: SqlForeignKeyAction = ...
    NoAction: SqlForeignKeyAction = ...
    SetDefault: SqlForeignKeyAction = ...
    SetNull: SqlForeignKeyAction = ...
    value__ = ...


class SqlForeignKeyConstraint(SqlConstraint, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlForeignKeyConstraint) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Columns(self) -> SqlIdentifierCollection:
        """ Get: Columns(self: SqlForeignKeyConstraint) -> SqlIdentifierCollection """
        ...

    @property
    def DeleteAction(self) -> SqlForeignKeyAction:
        """ Get: DeleteAction(self: SqlForeignKeyConstraint) -> SqlForeignKeyAction """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: SqlForeignKeyConstraint) -> bool """
        ...

    @property
    def ReferencedColumns(self) -> SqlIdentifierCollection:
        """ Get: ReferencedColumns(self: SqlForeignKeyConstraint) -> SqlIdentifierCollection """
        ...

    @property
    def ReferencedTable(self) -> SqlObjectIdentifier:
        """ Get: ReferencedTable(self: SqlForeignKeyConstraint) -> SqlObjectIdentifier """
        ...

    @property
    def UpdateAction(self) -> SqlForeignKeyAction:
        """ Get: UpdateAction(self: SqlForeignKeyConstraint) -> SqlForeignKeyAction """
        ...



class SqlForXmlClause(SqlForClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlForXmlClause) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Directives(self) -> SqlForXmlDirectiveCollection:
        """ Get: Directives(self: SqlForXmlClause) -> SqlForXmlDirectiveCollection """
        ...



class SqlForXmlAutoClause(SqlForXmlClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlForXmlAutoClause, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlForXmlAutoClause, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlForXmlAutoClause, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlForXmlAutoClause, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlForXmlDirective(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Argument(self) -> str:
        """ Get: Argument(self: SqlForXmlDirective) -> str """
        ...

    @property
    def Type(self) -> SqlForXmlDirectivesType:
        """ Get: Type(self: SqlForXmlDirective) -> SqlForXmlDirectivesType """
        ...



class SqlForXmlDirectiveCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlForXmlDirective]'>, <type 'IEnumerable'>, <type 'IEnumerable[SqlForXmlDirective]'>, <type 'object'>
    """ no doc """
    pass

class SqlForXmlDirectivesType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlForXmlDirectivesType, values: AutoMode (255), BinaryBase64 (1), CommonDirectives (7), Elements (128), ElementsAbsent (64), ElementsXsiNil (32), ExplicitMode (15), IncludeNullValues (256), JsonMode (772), None (0), PathMode (231), RawMode (255), Root (4), Type (2), WithoutArrayWrapper (512), XmlData (8), XmlSchema (16) """
    AutoMode: SqlForXmlDirectivesType = ...
    BinaryBase64: SqlForXmlDirectivesType = ...
    CommonDirectives: SqlForXmlDirectivesType = ...
    Elements: SqlForXmlDirectivesType = ...
    ElementsAbsent: SqlForXmlDirectivesType = ...
    ElementsXsiNil: SqlForXmlDirectivesType = ...
    ExplicitMode: SqlForXmlDirectivesType = ...
    IncludeNullValues: SqlForXmlDirectivesType = ...
    JsonMode: SqlForXmlDirectivesType = ...
    PathMode: SqlForXmlDirectivesType = ...
    RawMode: SqlForXmlDirectivesType = ...
    Root: SqlForXmlDirectivesType = ...
    Type: SqlForXmlDirectivesType = ...
    value__ = ...
    WithoutArrayWrapper: SqlForXmlDirectivesType = ...
    XmlData: SqlForXmlDirectivesType = ...
    XmlSchema: SqlForXmlDirectivesType = ...


class SqlForXmlExplicitClause(SqlForXmlClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlForXmlExplicitClause, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlForXmlExplicitClause, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlForXmlExplicitClause, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlForXmlExplicitClause, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlForXmlPathClause(SqlForXmlClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ElementName(self) -> str:
        """ Get: ElementName(self: SqlForXmlPathClause) -> str """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlForXmlPathClause, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlForXmlPathClause, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlForXmlPathClause, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlForXmlPathClause, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlForXmlRawClause(SqlForXmlClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ElementName(self) -> str:
        """ Get: ElementName(self: SqlForXmlRawClause) -> str """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlForXmlRawClause, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlForXmlRawClause, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlForXmlRawClause, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlForXmlRawClause, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlForXmlUnknownDirective(SqlForXmlDirective): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlForXmlUnknownDirective(name: str, argument: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlForXmlUnknownDirective) -> str """
        ...


    def __new__(cls, name:str, argument:str) -> Self:
        """ __new__(cls: type, name: str, argument: str) """
        ...


class SqlFromClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def TableExpressions(self) -> SqlTableExpressionCollection:
        """ Get: TableExpressions(self: SqlFromClause) -> SqlTableExpressionCollection """
        ...



class SqlFullTextBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlFullTextBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlFullTextColumnCollection:
        """ Get: ColumnList(self: SqlFullTextBooleanExpression) -> SqlFullTextColumnCollection """
        ...

    @property
    def FunctionName(self) -> SqlFullTextFunctionType:
        """ Get: FunctionName(self: SqlFullTextBooleanExpression) -> SqlFullTextFunctionType """
        ...

    @property
    def LangExpression(self) -> SqlScalarExpression:
        """ Get: LangExpression(self: SqlFullTextBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def SearchString(self) -> SqlScalarExpression:
        """ Get: SearchString(self: SqlFullTextBooleanExpression) -> SqlScalarExpression """
        ...



class SqlFullTextColumn(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ColumnRefExpression(self) -> SqlScalarRefExpression:
        """ Get: ColumnRefExpression(self: SqlFullTextColumn) -> SqlScalarRefExpression """
        ...

    @property
    def SelectStarExpression(self) -> SqlSelectStarExpression:
        """ Get: SelectStarExpression(self: SqlFullTextColumn) -> SqlSelectStarExpression """
        ...



class SqlFullTextColumnCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlFullTextColumn]'>, <type 'ISqlCodeCollection[SqlFullTextColumn]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlFullTextFunctionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlFullTextFunctionType, values: Contains (0), FreeText (1) """
    Contains: SqlFullTextFunctionType = ...
    FreeText: SqlFullTextFunctionType = ...
    value__ = ...


class SqlFunctionDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlFunctionDefinition) -> SqlObjectIdentifier """
        ...

    @property
    def Options(self) -> SqlCollection:
        """ Get: Options(self: SqlFunctionDefinition) -> SqlCollection[SqlModuleOption] """
        ...

    @property
    def Parameters(self) -> SqlParameterDeclarationCollection:
        """ Get: Parameters(self: SqlFunctionDefinition) -> SqlParameterDeclarationCollection """
        ...



class SqlFunctionDefinitionError(ISqlErrorObject, SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlFunctionDefinitionError) -> SqlFunctionBodyDefinition """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlFunctionDefinitionError) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ReturnType(self) -> SqlFunctionReturnType:
        """ Get: ReturnType(self: SqlFunctionDefinitionError) -> SqlFunctionReturnType """
        ...



class SqlFunctionReturnType(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlGdrStatementType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlGdrStatementType, values: SqlDeny (1), SqlGrant (0), SqlRevoke (2) """
    SqlDeny: SqlGdrStatementType = ...
    SqlGrant: SqlGdrStatementType = ...
    SqlRevoke: SqlGdrStatementType = ...
    value__ = ...


class SqlGeneratedAlwaysType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlGeneratedAlwaysType, values: AsRowEnd (2), AsRowStart (1), None (0) """
    AsRowEnd: SqlGeneratedAlwaysType = ...
    AsRowStart: SqlGeneratedAlwaysType = ...
    value__ = ...


class SqlGlobalScalarVariableRefExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundVariable(self) -> IBuiltInFunction:
        """ Get: BoundVariable(self: SqlGlobalScalarVariableRefExpression) -> IBuiltInFunction """
        ...

    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: SqlGlobalScalarVariableRefExpression) -> str """
        ...



class SqlGrandTotalGroupByItem(SqlGroupByItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlGrandTotalGroupByItem() """
    pass

class SqlGroupingSet(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlGrandTotalGroupingSet(SqlGroupingSet): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlGrandTotalGroupingSet) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Item(self) -> SqlGrandTotalGroupByItem:
        """ Get: Item(self: SqlGrandTotalGroupingSet) -> SqlGrandTotalGroupByItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SqlGrantStatement(SqlGdrStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlGroupByClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def HasAll(self) -> bool:
        """ Get: HasAll(self: SqlGroupByClause) -> bool """
        ...

    @property
    def Items(self) -> SqlGroupByItemCollection:
        """ Get: Items(self: SqlGroupByClause) -> SqlGroupByItemCollection """
        ...

    @property
    def Option(self) -> SqlGroupByOptionType:
        """ Get: Option(self: SqlGroupByClause) -> SqlGroupByOptionType """
        ...



class SqlGroupByItemCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlGroupByItem]'>, <type 'IEnumerable'>, <type 'IEnumerable[SqlGroupByItem]'>, <type 'object'>
    """ no doc """
    pass

class SqlGroupByOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlGroupByOptionType, values: Cube (1), None (0), Rollup (2) """
    Cube: SqlGroupByOptionType = ...
    Rollup: SqlGroupByOptionType = ...
    value__ = ...


class SqlGroupBySets(SqlGroupByItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlGroupBySets) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Sets(self) -> SqlGroupingSetsCollection:
        """ Get: Sets(self: SqlGroupBySets) -> SqlGroupingSetsCollection """
        ...



class SqlGroupingSetCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlGroupingSet]'>, <type 'ISqlCodeCollection[SqlGroupingSet]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlGroupingSetItemCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlGroupingSetItem]'>, <type 'ISqlCodeCollection[SqlGroupingSetItem]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlGroupingSetItemsCollection(SqlGroupingSet): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlGroupingSetItemsCollection) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Items(self) -> SqlGroupingSetItemCollection:
        """ Get: Items(self: SqlGroupingSetItemsCollection) -> SqlGroupingSetItemCollection """
        ...



class SqlGroupingSetsCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlGroupingSet]'>, <type 'ISqlCodeCollection[SqlGroupingSet]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlHavingClause(SqlConditionClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlHint(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsIndexHint(self) -> bool:
        """ Get: IsIndexHint(self: SqlHint) -> bool """
        ...

    @property
    def IsTableHint(self) -> bool:
        """ Get: IsTableHint(self: SqlHint) -> bool """
        ...



class SqlHintCollection(SqlCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[SqlHint]'>, <type 'ISqlCodeCollection[SqlHint]'>, <type 'object'>
    """ no doc """
    pass

class SqlIdentifier(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> str:
        """ Get: Value(self: SqlIdentifier) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlIdentifier) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlIdentifierCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlIdentifier]'>, <type 'IEnumerable'>, <type 'IEnumerable[SqlIdentifier]'>, <type 'object'>
    """ no doc """
    pass

class SqlIdentityFunctionCallExpression(SqlBuiltinScalarFunctionCallExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlIdentityFunctionCallExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlIfElseStatement(SqlConditionalStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlIfElseStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def FalseStatement(self) -> SqlStatement:
        """ Get: FalseStatement(self: SqlIfElseStatement) -> SqlStatement """
        ...



class SqlIgnoreDupKeyIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlIgnoreDupKeyIndexOption) -> SqlOnOffValue """
        ...



class SqlInBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ComparisonValue(self) -> SqlInBooleanExpressionValue:
        """ Get: ComparisonValue(self: SqlInBooleanExpression) -> SqlInBooleanExpressionValue """
        ...

    @property
    def HasNot(self) -> bool:
        """ Get: HasNot(self: SqlInBooleanExpression) -> bool """
        ...

    @property
    def InExpression(self) -> SqlScalarExpression:
        """ Get: InExpression(self: SqlInBooleanExpression) -> SqlScalarExpression """
        ...



class SqlInBooleanExpressionValue(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlInBooleanExpressionCollectionValue(SqlInBooleanExpressionValue): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInBooleanExpressionCollectionValue) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Values(self) -> SqlScalarExpressionCollection:
        """ Get: Values(self: SqlInBooleanExpressionCollectionValue) -> SqlScalarExpressionCollection """
        ...



class SqlInBooleanExpressionQueryValue(SqlInBooleanExpressionValue): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInBooleanExpressionQueryValue) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Value(self) -> SqlQueryExpression:
        """ Get: Value(self: SqlInBooleanExpressionQueryValue) -> SqlQueryExpression """
        ...



class SqlIndexedColumn(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundColumn(self) -> IColumn:
        """ Get: BoundColumn(self: SqlIndexedColumn) -> IColumn """
        ...

    @property
    def Name(self) -> SqlIdentifier:
        """ Get: Name(self: SqlIndexedColumn) -> SqlIdentifier """
        ...

    @property
    def SortOrder(self) -> SqlSortOrder:
        """ Get: SortOrder(self: SqlIndexedColumn) -> SqlSortOrder """
        ...



class SqlIndexedColumnCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlIndexedColumn]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlIndexedColumn]'>, <type 'object'>
    """ no doc """
    pass

class SqlIndexHint(SqlHint): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlLiteralExpressionCollection:
        """ Get: Arguments(self: SqlIndexHint) -> SqlLiteralExpressionCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlIndexHint) -> IEnumerable[SqlCodeObject] """
        ...



class SqlIndexOptionCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlIndexOption]'>, <type 'IEnumerable[SqlIndexOption]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlIndexOptionError(ISqlErrorObject, SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlIndexOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlIndexOptionType, values: AllowPageLocks (1), AllowRowLocks (2), BucketCount (16), CompressionDelay (17), DataCompression (3), DropExisting (4), FillFactor (5), IgnoreDupKey (6), Invalid (0), MaxDegreeOfParallelism (7), MaxDuration (19), Online (8), PadIndex (9), Resumable (18), SortedData (10), SortedDataReorg (11), SortInTempDb (13), StatisticsIncremental (12), StatisticsNoRecompute (14), StatisticsOnly (15) """
    AllowPageLocks: SqlIndexOptionType = ...
    AllowRowLocks: SqlIndexOptionType = ...
    BucketCount: SqlIndexOptionType = ...
    CompressionDelay: SqlIndexOptionType = ...
    DataCompression: SqlIndexOptionType = ...
    DropExisting: SqlIndexOptionType = ...
    FillFactor: SqlIndexOptionType = ...
    IgnoreDupKey: SqlIndexOptionType = ...
    Invalid: SqlIndexOptionType = ...
    MaxDegreeOfParallelism: SqlIndexOptionType = ...
    MaxDuration: SqlIndexOptionType = ...
    Online: SqlIndexOptionType = ...
    PadIndex: SqlIndexOptionType = ...
    Resumable: SqlIndexOptionType = ...
    SortedData: SqlIndexOptionType = ...
    SortedDataReorg: SqlIndexOptionType = ...
    SortInTempDb: SqlIndexOptionType = ...
    StatisticsIncremental: SqlIndexOptionType = ...
    StatisticsNoRecompute: SqlIndexOptionType = ...
    StatisticsOnly: SqlIndexOptionType = ...
    value__ = ...


class SqlInlineFunctionBodyDefinition(SqlFunctionBodyDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInlineFunctionBodyDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlInlineFunctionBodyDefinition) -> SqlQueryExpression """
        ...

    @property
    def QueryWithClause(self) -> SqlQueryWithClause:
        """ Get: QueryWithClause(self: SqlInlineFunctionBodyDefinition) -> SqlQueryWithClause """
        ...



class SqlInlineIndexConstraint(SqlConstraint, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInlineIndexConstraint) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Options(self) -> SqlIndexOptionCollection:
        """ Get: Options(self: SqlInlineIndexConstraint) -> SqlIndexOptionCollection """
        ...



class SqlInlineTableRelationalFunctionDefinition(SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlInlineFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlInlineTableRelationalFunctionDefinition) -> SqlInlineFunctionBodyDefinition """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInlineTableRelationalFunctionDefinition) -> IEnumerable[SqlCodeObject] """
        ...



class SqlInlineTableVariableDeclaration(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundTable(self) -> ITableVariable:
        """ Get: BoundTable(self: SqlInlineTableVariableDeclaration) -> ITableVariable """
        ...

    @property
    def Definition(self) -> SqlTableDefinition:
        """ Get: Definition(self: SqlInlineTableVariableDeclaration) -> SqlTableDefinition """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlInlineTableVariableDeclaration) -> str """
        ...



class SqlInlineTableVariableDeclareStatement(SqlDeclareStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInlineTableVariableDeclareStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Declaration(self) -> SqlInlineTableVariableDeclaration:
        """ Get: Declaration(self: SqlInlineTableVariableDeclareStatement) -> SqlInlineTableVariableDeclaration """
        ...



class SqlInsertMergeAction(SqlMergeAction): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInsertMergeAction) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Source(self) -> SqlInsertMergeActionSource:
        """ Get: Source(self: SqlInsertMergeAction) -> SqlInsertMergeActionSource """
        ...

    @property
    def TargetColumns(self) -> SqlColumnRefExpressionCollection:
        """ Get: TargetColumns(self: SqlInsertMergeAction) -> SqlColumnRefExpressionCollection """
        ...



class SqlInsertSpecification(SqlDmlSpecification): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlInsertSpecification) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Source(self) -> SqlInsertSource:
        """ Get: Source(self: SqlInsertSpecification) -> SqlInsertSource """
        ...

    @property
    def TargetColumns(self) -> SqlColumnRefExpressionCollection:
        """ Get: TargetColumns(self: SqlInsertSpecification) -> SqlColumnRefExpressionCollection """
        ...



class SqlInsertStatement(SqlDmlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def InsertSpecification(self) -> SqlInsertSpecification:
        """ Get: InsertSpecification(self: SqlInsertStatement) -> SqlInsertSpecification """
        ...



class SqlIntoClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> SqlColumnRefExpressionCollection:
        """ Get: Columns(self: SqlIntoClause) -> SqlColumnRefExpressionCollection """
        ...

    @property
    def Target(self) -> SqlTableExpression:
        """ Get: Target(self: SqlIntoClause) -> SqlTableExpression """
        ...



class SqlIsNullBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlIsNullBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlIsNullBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def HasNot(self) -> bool:
        """ Get: HasNot(self: SqlIsNullBooleanExpression) -> bool """
        ...



class SqlJoinOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlJoinOperatorType, values: CrossApply (1), CrossJoin (0), FullOuterJoin (6), InnerJoin (3), LeftOuterJoin (4), OuterApply (2), RightOuterJoin (5) """
    CrossApply: SqlJoinOperatorType = ...
    CrossJoin: SqlJoinOperatorType = ...
    FullOuterJoin: SqlJoinOperatorType = ...
    InnerJoin: SqlJoinOperatorType = ...
    LeftOuterJoin: SqlJoinOperatorType = ...
    OuterApply: SqlJoinOperatorType = ...
    RightOuterJoin: SqlJoinOperatorType = ...
    value__ = ...


class SqlJoinTableExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def JoinOperator(self) -> SqlJoinOperatorType:
        """ Get: JoinOperator(self: SqlJoinTableExpression) -> SqlJoinOperatorType """
        ...

    @property
    def Left(self) -> SqlTableExpression:
        """ Get: Left(self: SqlJoinTableExpression) -> SqlTableExpression """
        ...

    @property
    def Right(self) -> SqlTableExpression:
        """ Get: Right(self: SqlJoinTableExpression) -> SqlTableExpression """
        ...



class SqlLargeDataStorageInformation(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def FileStreamStorageSpecification(self) -> SqlStorageSpecification:
        """ Get: FileStreamStorageSpecification(self: SqlLargeDataStorageInformation) -> SqlStorageSpecification """
        ...

    @property
    def TextAndImageStorageSpecification(self) -> SqlStorageSpecification:
        """ Get: TextAndImageStorageSpecification(self: SqlLargeDataStorageInformation) -> SqlStorageSpecification """
        ...



class SqlLikeBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlLikeBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def EscapeClause(self) -> SqlScalarExpression:
        """ Get: EscapeClause(self: SqlLikeBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlLikeBooleanExpression) -> SqlScalarExpression """
        ...

    @property
    def HasNot(self) -> bool:
        """ Get: HasNot(self: SqlLikeBooleanExpression) -> bool """
        ...

    @property
    def LikePattern(self) -> SqlScalarExpression:
        """ Get: LikePattern(self: SqlLikeBooleanExpression) -> SqlScalarExpression """
        ...



class SqlLiteralExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> LiteralValueType:
        """ Get: Type(self: SqlLiteralExpression) -> LiteralValueType """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: SqlLiteralExpression) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlLiteralExpression) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlLiteralExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlLiteralExpression]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlLiteralExpression]'>, <type 'object'>
    """ no doc """
    pass

class SqlLiteralStringIdentifier(SqlIdentifier): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlLoginOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlLoginOptionType:
        """ Get: Type(self: SqlLoginOption) -> SqlLoginOptionType """
        ...


    def CheckExpirationOption(self, *args): #cannot find CLR method
        """ CheckExpirationOption(value: SqlOnOffValue) """
        ...

    def CheckPolicyOption(self, *args): #cannot find CLR method
        """ CheckPolicyOption(value: SqlOnOffValue) """
        ...

    def CredentialOption(self, *args): #cannot find CLR method
        """ CredentialOption(value: SqlIdentifier, modificationValue: SqlModificationType) """
        ...

    def DefaultDatabaseOption(self, *args): #cannot find CLR method
        """ DefaultDatabaseOption(value: SqlIdentifier) """
        ...

    def DefaultLanguageOption(self, *args): #cannot find CLR method
        """ DefaultLanguageOption(value: SqlIdentifier) """
        ...

    def EmptyOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def HashedOption(self, *args): #cannot find CLR method
        """ HashedOption() """
        ...

    def InvalidEmptyOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def InvalidObjectOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def InvalidOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def InvalidValueOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def MustChangeOption(self, *args): #cannot find CLR method
        """ MustChangeOption() """
        ...

    def NameOption(self, *args): #cannot find CLR method
        """ NameOption(value: SqlIdentifier) """
        ...

    def NoCredentialOption(self, *args): #cannot find CLR method
        """ NoCredentialOption() """
        ...

    def ObjectOption`1(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def OnOffOption(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def PasswordOption(self, *args): #cannot find CLR method
        """ PasswordOption(password: SqlLoginPassword, oldPassword: SqlLoginPassword) """
        ...

    def SidOption(self, *args): #cannot find CLR method
        """ SidOption(value: SqlLiteralExpression) """
        ...



class SqlLoginOptionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetOptionString(type:SqlLoginOptionType) -> str:
        """ GetOptionString(type: SqlLoginOptionType) -> str """
        ...

    def GetOptionStringToken(self, type:SqlLoginOptionType) -> StringToken:
        """ GetOptionStringToken(self: SqlLoginOptionContext, type: SqlLoginOptionType) -> StringToken """
        ...

    def GetOptionType(self, *__args:StringToken) -> SqlLoginOptionType:
        """
        GetOptionType(self: SqlLoginOptionContext, stringToken: StringToken) -> SqlLoginOptionType
        GetOptionType(self: SqlLoginOptionContext, stringValue: str) -> SqlLoginOptionType
        """
        ...


class SqlLoginOptionContextItem: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlLoginOptionContextItem(type: SqlLoginOptionType) """
    CheckExpiration: SqlLoginOptionContextItem = ...
    CheckPolicy: SqlLoginOptionContextItem = ...
    Credential: SqlLoginOptionContextItem = ...
    DefaultDatabase: SqlLoginOptionContextItem = ...
    DefaultLanguage: SqlLoginOptionContextItem = ...
    Hashed: SqlLoginOptionContextItem = ...
    MustChange: SqlLoginOptionContextItem = ...
    Name: SqlLoginOptionContextItem = ...
    Sid: SqlLoginOptionContextItem = ...
    stringToken = ...
    type = ...


class SqlLoginOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlLoginOptionType, values: CheckExpiration (64), CheckPolicy (128), Credential (32), DefaultDatabase (8), DefaultLanguage (16), Hashed (1), Invalid (32768), InvalidValue (32770), MustChange (2), Name (256), NoCredential (1024), None (0), Password (512), Sid (4), Unrecognized (32769) """
    CheckExpiration: SqlLoginOptionType = ...
    CheckPolicy: SqlLoginOptionType = ...
    Credential: SqlLoginOptionType = ...
    DefaultDatabase: SqlLoginOptionType = ...
    DefaultLanguage: SqlLoginOptionType = ...
    Hashed: SqlLoginOptionType = ...
    Invalid: SqlLoginOptionType = ...
    InvalidValue: SqlLoginOptionType = ...
    MustChange: SqlLoginOptionType = ...
    Name: SqlLoginOptionType = ...
    NoCredential: SqlLoginOptionType = ...
    Password: SqlLoginOptionType = ...
    Sid: SqlLoginOptionType = ...
    Unrecognized: SqlLoginOptionType = ...
    value__ = ...


class SqlLoginPassword(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsHashed(self) -> bool:
        """ Get: IsHashed(self: SqlLoginPassword) -> bool """
        ...

    @property
    def MustChange(self) -> bool:
        """ Get: MustChange(self: SqlLoginPassword) -> bool """
        ...

    @property
    def Password(self) -> SqlLiteralExpression:
        """ Get: Password(self: SqlLoginPassword) -> SqlLiteralExpression """
        ...



class SqlMaxDegreeOfParallelismIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def DegreeOfParallelism(self) -> int:
        """ Get: DegreeOfParallelism(self: SqlMaxDegreeOfParallelismIndexOption) -> int """
        ...



class SqlMaxDurationIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def MaxDuration(self) -> int:
        """ Get: MaxDuration(self: SqlMaxDurationIndexOption) -> int """
        ...



class SqlMergeActionClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> SqlMergeAction:
        """ Get: Action(self: SqlMergeActionClause) -> SqlMergeAction """
        ...

    @property
    def MergeConditionType(self) -> SqlMergeConditionType:
        """ Get: MergeConditionType(self: SqlMergeActionClause) -> SqlMergeConditionType """
        ...

    @property
    def SearchCondition(self) -> SqlBooleanExpression:
        """ Get: SearchCondition(self: SqlMergeActionClause) -> SqlBooleanExpression """
        ...



class SqlMergeActionClauseCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlMergeActionClause]'>, <type 'ISqlCodeCollection[SqlMergeActionClause]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlMergeConditionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlMergeConditionType, values: Error (0), Matched (1), SourceNotMatched (2), TargetNotMatched (3) """
    Error: SqlMergeConditionType = ...
    Matched: SqlMergeConditionType = ...
    SourceNotMatched: SqlMergeConditionType = ...
    TargetNotMatched: SqlMergeConditionType = ...
    value__ = ...


class SqlMergeSpecification(SqlDmlSpecification): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ActionClauses(self) -> SqlMergeActionClauseCollection:
        """ Get: ActionClauses(self: SqlMergeSpecification) -> SqlMergeActionClauseCollection """
        ...

    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlMergeSpecification) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlMergeSpecification) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def OnClause(self) -> SqlConditionClause:
        """ Get: OnClause(self: SqlMergeSpecification) -> SqlConditionClause """
        ...

    @property
    def Source(self) -> SqlTableExpression:
        """ Get: Source(self: SqlMergeSpecification) -> SqlTableExpression """
        ...



class SqlMergeStatement(SqlDmlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def MergeSpecification(self) -> SqlMergeSpecification:
        """ Get: MergeSpecification(self: SqlMergeStatement) -> SqlMergeSpecification """
        ...



class SqlMissingInsertSource(SqlInsertSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlMissingInsertSource() """
    pass

class SqlModificationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlModificationType, values: Add (1), Drop (2), Set (0) """
    Add: SqlModificationType = ...
    Drop: SqlModificationType = ...
    Set: SqlModificationType = ...
    value__ = ...


class SqlModuleOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlModuleOptionType:
        """ Get: Type(self: SqlModuleOption) -> SqlModuleOptionType """
        ...



class SqlModuleCalledOnNullInputOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleEncryptionOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleExecuteAsOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlModuleExecuteAsOption) -> IEnumerable[SqlCodeObject] """
        ...



class SqlModuleExecutionContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlModuleExecutionContextType, values: Caller (0), Owner (1), Self (2), User (3) """
    Caller: SqlModuleExecutionContextType = ...
    Owner: SqlModuleExecutionContextType = ...
    Self: SqlModuleExecutionContextType = ...
    User: SqlModuleExecutionContextType = ...
    value__ = ...


class SqlModuleNativeCompilationOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleOptionMask(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlModuleOptionMask, values: CalledOnNullInput (128), CreateProcedure (286), CreateTrigger (12), CreateView (52), Encryption (4), ExecuteAs (8), ExecuteModule (2), Invalid (32768), NativeCompilation (256), None (0), NullInputOptions (192), Recompile (2), ReturnsNullOnNullInput (64), SchemaBinding (16), ViewMetadata (32) """
    CalledOnNullInput: SqlModuleOptionMask = ...
    CreateProcedure: SqlModuleOptionMask = ...
    CreateTrigger: SqlModuleOptionMask = ...
    CreateView: SqlModuleOptionMask = ...
    Encryption: SqlModuleOptionMask = ...
    ExecuteAs: SqlModuleOptionMask = ...
    ExecuteModule: SqlModuleOptionMask = ...
    Invalid: SqlModuleOptionMask = ...
    NativeCompilation: SqlModuleOptionMask = ...
    NullInputOptions: SqlModuleOptionMask = ...
    Recompile: SqlModuleOptionMask = ...
    ReturnsNullOnNullInput: SqlModuleOptionMask = ...
    SchemaBinding: SqlModuleOptionMask = ...
    value__ = ...
    ViewMetadata: SqlModuleOptionMask = ...


class SqlModuleOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlModuleOptionType, values: CalledOnNullInput (7), Encryption (2), ExecuteAs (3), NativeCompilation (8), None (0), Recompile (1), ReturnsNullOnNullInput (6), SchemaBinding (4), ViewMetadata (5) """
    CalledOnNullInput: SqlModuleOptionType = ...
    Encryption: SqlModuleOptionType = ...
    ExecuteAs: SqlModuleOptionType = ...
    NativeCompilation: SqlModuleOptionType = ...
    Recompile: SqlModuleOptionType = ...
    ReturnsNullOnNullInput: SqlModuleOptionType = ...
    SchemaBinding: SqlModuleOptionType = ...
    value__ = ...
    ViewMetadata: SqlModuleOptionType = ...


class SqlModuleRecompileOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleReturnsNullOnNullInputOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleSchemaBindingOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlModuleViewMetadataOption(SqlModuleOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlMultipartIdentifier(IEnumerable, SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SqlMultipartIdentifier) -> int """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SqlIdentifier](enumerable: IEnumerable[SqlIdentifier], value: SqlIdentifier) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SqlMultistatementFunctionBodyDefinition(SqlFunctionBodyDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlMultistatementFunctionBodyDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def CompoundStatement(self) -> SqlCompoundStatement:
        """ Get: CompoundStatement(self: SqlMultistatementFunctionBodyDefinition) -> SqlCompoundStatement """
        ...



class SqlMultistatementTableRelationalFunctionDefinition(SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlMultistatementFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlMultistatementTableRelationalFunctionDefinition) -> SqlMultistatementFunctionBodyDefinition """
        ...

    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlMultistatementTableRelationalFunctionDefinition) -> IMetadataObject """
        ...

    @property
    def BoundTable(self) -> ITableVariable:
        """ Get: BoundTable(self: SqlMultistatementTableRelationalFunctionDefinition) -> ITableVariable """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlMultistatementTableRelationalFunctionDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ReturnType(self) -> SqlTableFunctionReturnType:
        """ Get: ReturnType(self: SqlMultistatementTableRelationalFunctionDefinition) -> SqlTableFunctionReturnType """
        ...

    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: SqlMultistatementTableRelationalFunctionDefinition) -> str """
        ...



class SqlNotBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlNotBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlBooleanExpression:
        """ Get: Expression(self: SqlNotBooleanExpression) -> SqlBooleanExpression """
        ...



class SqlNullAssignment(SqlAssignment, INullCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlNullAssignment) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Value(self) -> SqlNullScalarExpression:
        """ Get: Value(self: SqlNullAssignment) -> SqlNullScalarExpression """
        ...



class SqlNullInsertSource(SqlInsertSource, INullCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlNullInsertSource() """
    pass

class SqlNullQueryExpression(INullCodeObject, SqlQueryExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlNullQueryExpression() """
    pass

class SqlNullScalarExpression(SqlScalarExpression, INullCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlNullScalarExpression() """
    pass

class SqlNullStatement(INullCodeObject, SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlNullStatement() """
    pass

class SqlNullTableExpression(SqlTableExpression, INullCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlNullTableExpression() """
    pass

class SqlObjectIdentifier(SqlMultipartIdentifier): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IEnumerable'>, <type 'IEnumerable[SqlIdentifier]'>, <type 'object'>
    """ no doc """
    @property
    def DatabaseName(self) -> SqlIdentifier:
        """ Get: DatabaseName(self: SqlObjectIdentifier) -> SqlIdentifier """
        ...

    @property
    def IsMultiPartName(self) -> bool:
        """ Get: IsMultiPartName(self: SqlObjectIdentifier) -> bool """
        ...

    @property
    def ObjectName(self) -> SqlIdentifier:
        """ Get: ObjectName(self: SqlObjectIdentifier) -> SqlIdentifier """
        ...

    @property
    def SchemaName(self) -> SqlIdentifier:
        """ Get: SchemaName(self: SqlObjectIdentifier) -> SqlIdentifier """
        ...

    @property
    def ServerName(self) -> SqlIdentifier:
        """ Get: ServerName(self: SqlObjectIdentifier) -> SqlIdentifier """
        ...



class SqlObjectIdentifierCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlObjectIdentifier]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlObjectIdentifier]'>, <type 'object'>
    """ no doc """
    pass

class SqlObjectReference(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ObjectIdentifier(self) -> SqlObjectIdentifier:
        """ Get: ObjectIdentifier(self: SqlObjectReference) -> SqlObjectIdentifier """
        ...

    @property
    def Variable(self) -> SqlScalarVariableRefExpression:
        """ Get: Variable(self: SqlObjectReference) -> SqlScalarVariableRefExpression """
        ...



class SqlOffsetFetchClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlOffsetFetchClause(offset: SqlScalarExpression, fetch: SqlScalarExpression) """
    @property
    def Fetch(self) -> SqlScalarExpression:
        """ Get: Fetch(self: SqlOffsetFetchClause) -> SqlScalarExpression """
        ...

    @property
    def Offset(self) -> SqlScalarExpression:
        """ Get: Offset(self: SqlOffsetFetchClause) -> SqlScalarExpression """
        ...


    def __new__(cls, offset:SqlScalarExpression, fetch:SqlScalarExpression) -> Self:
        """ __new__(cls: type, offset: SqlScalarExpression, fetch: SqlScalarExpression) """
        ...


class SqlOnClauseError(ISqlErrorObject, SqlConditionClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlOnlineIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlOnlineIndexOption) -> SqlOnOffValue """
        ...



class SqlOnOffValue(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlOnOffValue, values: None (0), Off (1), On (2) """
    Off: SqlOnOffValue = ...
    On: SqlOnOffValue = ...
    value__ = ...


class SqlOrderByClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Items(self) -> SqlOrderByItemCollection:
        """ Get: Items(self: SqlOrderByClause) -> SqlOrderByItemCollection """
        ...

    @property
    def OffsetFetchClause(self) -> SqlOffsetFetchClause:
        """ Get: OffsetFetchClause(self: SqlOrderByClause) -> SqlOffsetFetchClause """
        ...



class SqlOrderByItem(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlOrderByItem) -> SqlScalarExpression """
        ...

    @property
    def SortOrder(self) -> SqlSortOrder:
        """ Get: SortOrder(self: SqlOrderByItem) -> SqlSortOrder """
        ...



class SqlOrderByItemCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlOrderByItem]'>, <type 'ISqlCodeCollection[SqlOrderByItem]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlOutputClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OutputExpressions(self) -> SqlSelectExpressionCollection:
        """ Get: OutputExpressions(self: SqlOutputClause) -> SqlSelectExpressionCollection """
        ...



class SqlOutputIntoClause(SqlOutputClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IntoClause(self) -> SqlIntoClause:
        """ Get: IntoClause(self: SqlOutputIntoClause) -> SqlIntoClause """
        ...



class SqlPadIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlPadIndexOption) -> SqlOnOffValue """
        ...



class SqlVariableDeclaration(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundVariable(self) -> ILocalVariable:
        """ Get: BoundVariable(self: SqlVariableDeclaration) -> ILocalVariable """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlVariableDeclaration) -> str """
        ...

    @property
    def Type(self) -> SqlDataTypeSpecification:
        """ Get: Type(self: SqlVariableDeclaration) -> SqlDataTypeSpecification """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlVariableDeclaration) -> SqlScalarExpression """
        ...



class SqlParameterDeclaration(SqlVariableDeclaration): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsOutput(self) -> bool:
        """ Get: IsOutput(self: SqlParameterDeclaration) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SqlParameterDeclaration) -> bool """
        ...



class SqlParameterDeclarationCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlParameterDeclaration]'>, <type 'IEnumerable[SqlParameterDeclaration]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlParameterOption(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Output() -> SqlParameterOption:
        """ Output() -> SqlParameterOption """
        ...

    @staticmethod
    def ReadOnly() -> SqlParameterOption:
        """ ReadOnly() -> SqlParameterOption """
        ...

    Type = ...


class SqlParameterOptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlParameterOptionType, values: FunctionValidOptions (2), Invalid (32768), None (0), Output (1), ProcedureValidOptions (3), ReadOnly (2) """
    FunctionValidOptions: SqlParameterOptionType = ...
    Invalid: SqlParameterOptionType = ...
    Output: SqlParameterOptionType = ...
    ProcedureValidOptions: SqlParameterOptionType = ...
    ReadOnly: SqlParameterOptionType = ...
    value__ = ...


class SqlPivotClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def AggregatedColumns(self) -> SqlColumnRefExpressionCollection:
        """ Get: AggregatedColumns(self: SqlPivotClause) -> SqlColumnRefExpressionCollection """
        ...

    @property
    def AggregateFunctionName(self) -> SqlObjectIdentifier:
        """ Get: AggregateFunctionName(self: SqlPivotClause) -> SqlObjectIdentifier """
        ...

    @property
    def ColumnList(self) -> SqlColumnRefExpressionCollection:
        """ Get: ColumnList(self: SqlPivotClause) -> SqlColumnRefExpressionCollection """
        ...

    @property
    def PivotedColumn(self) -> SqlColumnRefExpression:
        """ Get: PivotedColumn(self: SqlPivotClause) -> SqlColumnRefExpression """
        ...



class SqlPivotTableExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlPivotTableExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlPivotTableExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def PivotClause(self) -> SqlPivotClause:
        """ Get: PivotClause(self: SqlPivotTableExpression) -> SqlPivotClause """
        ...

    @property
    def Source(self) -> SqlTableExpression:
        """ Get: Source(self: SqlPivotTableExpression) -> SqlTableExpression """
        ...



class SqlUniqueConstraintBase(SqlConstraint, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUniqueConstraintBase) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ClusterOption(self) -> SqlClusterOption:
        """ Get: ClusterOption(self: SqlUniqueConstraintBase) -> SqlClusterOption """
        ...

    @property
    def IndexedColumns(self) -> SqlIndexedColumnCollection:
        """ Get: IndexedColumns(self: SqlUniqueConstraintBase) -> SqlIndexedColumnCollection """
        ...

    @property
    def IndexOptions(self) -> SqlIndexOptionCollection:
        """ Get: IndexOptions(self: SqlUniqueConstraintBase) -> SqlIndexOptionCollection """
        ...



class SqlPrimaryKeyConstraint(SqlUniqueConstraintBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'ISqlTableElement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlPrimaryKeyConstraint, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlPrimaryKeyConstraint, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlPrimaryKeyConstraint, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlPrimaryKeyConstraint, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlProcedureDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsForReplication(self) -> bool:
        """ Get: IsForReplication(self: SqlProcedureDefinition) -> bool """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlProcedureDefinition) -> SqlObjectIdentifier """
        ...

    @property
    def Number(self) -> Nullable:
        """ Get: Number(self: SqlProcedureDefinition) -> Nullable[int] """
        ...

    @property
    def Options(self) -> SqlCollection:
        """ Get: Options(self: SqlProcedureDefinition) -> SqlCollection[SqlModuleOption] """
        ...

    @property
    def Parameters(self) -> SqlParameterDeclarationCollection:
        """ Get: Parameters(self: SqlProcedureDefinition) -> SqlParameterDeclarationCollection """
        ...


    isForReplication = ...
    name = ...
    number = ...
    options = ...
    parameters = ...


class SqlProcedureDefinitionForCreate(SqlProcedureDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsOrAlterStatement(self) -> bool:
        """ Get: IsOrAlterStatement(self: SqlProcedureDefinitionForCreate) -> bool """
        ...


    isForReplication = ...
    name = ...
    number = ...
    options = ...
    parameters = ...


class SqlQualifiedJoinTableExpression(SqlJoinTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlQualifiedJoinTableExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def OnClause(self) -> SqlConditionClause:
        """ Get: OnClause(self: SqlQualifiedJoinTableExpression) -> SqlConditionClause """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlQualifiedJoinTableExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlQualifiedJoinTableExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlQualifiedJoinTableExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlQualifiedJoinTableExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlQuerySpecification(SqlQueryExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlQuerySpecification) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ForClause(self) -> SqlForClause:
        """ Get: ForClause(self: SqlQuerySpecification) -> SqlForClause """
        ...

    @property
    def FromClause(self) -> SqlFromClause:
        """ Get: FromClause(self: SqlQuerySpecification) -> SqlFromClause """
        ...

    @property
    def GroupByClause(self) -> SqlGroupByClause:
        """ Get: GroupByClause(self: SqlQuerySpecification) -> SqlGroupByClause """
        ...

    @property
    def HavingClause(self) -> SqlHavingClause:
        """ Get: HavingClause(self: SqlQuerySpecification) -> SqlHavingClause """
        ...

    @property
    def IntoClause(self) -> SqlSelectIntoClause:
        """ Get: IntoClause(self: SqlQuerySpecification) -> SqlSelectIntoClause """
        ...

    @property
    def OrderByClause(self) -> SqlOrderByClause:
        """ Get: OrderByClause(self: SqlQuerySpecification) -> SqlOrderByClause """
        ...

    @property
    def SelectClause(self) -> SqlSelectClause:
        """ Get: SelectClause(self: SqlQuerySpecification) -> SqlSelectClause """
        ...

    @property
    def WhereClause(self) -> SqlWhereClause:
        """ Get: WhereClause(self: SqlQuerySpecification) -> SqlWhereClause """
        ...



class SqlQueryWithClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def CommonTableExpressions(self) -> SqlCommonTableExpressionCollection:
        """ Get: CommonTableExpressions(self: SqlQueryWithClause) -> SqlCommonTableExpressionCollection """
        ...



class SqlRestoreDatabaseStatement(SqlBackupRestoreDatabaseStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreDatabaseStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlRestoreDatabaseStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlRestoreDatabaseStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlRestoreDatabaseStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreDatabaseStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlRestoreDatabaseStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRestoreDatabaseStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRestoreDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreDatabaseStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlRestoreInformationStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreInformationStatement() """
    pass

class SqlRestoreLogStatement(SqlBackupRestoreLogStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreLogStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlRestoreLogStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlRestoreLogStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlRestoreLogStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreLogStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlRestoreLogStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRestoreLogStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRestoreLogStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreLogStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlRestoreMasterKeyStatement(SqlBackupRestoreMasterKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreMasterKeyStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlRestoreMasterKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlRestoreMasterKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlRestoreMasterKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreMasterKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlRestoreMasterKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRestoreMasterKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRestoreMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlRestoreServiceMasterKeyStatement(SqlBackupRestoreServiceMasterKeyStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreServiceMasterKeyStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreServiceMasterKeyStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlRestoreTableStatement(SqlBackupRestoreTableStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlRestoreTableStatement() """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlStatementContextVisitor'}
        """
        Accept(self: SqlRestoreTableStatement, visitor: ISqlStatementVisitor)Accept[T](self: SqlRestoreTableStatement, visitor: ISqlStatementVisitor[T]) -> T
        Accept[C](self: SqlRestoreTableStatement, visitor: ISqlStatementContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreTableStatement, visitor: ISqlStatementContextVisitor[T, C], context: C) -> T
        Accept(self: SqlRestoreTableStatement, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRestoreTableStatement, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRestoreTableStatement, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRestoreTableStatement, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlResumableIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlResumableIndexOption) -> SqlOnOffValue """
        ...



class SqlReturnStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlReturnStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlReturnStatement) -> SqlScalarExpression """
        ...



class SqlRevokeStatement(SqlGdrStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlRollupGroupByItem(SqlGroupingSetItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlRollupGroupByItem) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Items(self) -> SqlCubeRollupArgumentCollection:
        """ Get: Items(self: SqlRollupGroupByItem) -> SqlCubeRollupArgumentCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlRollupGroupByItem, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlRollupGroupByItem, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlRollupGroupByItem, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlRollupGroupByItem, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlRowConstructorExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Values(self) -> SqlScalarExpressionCollection:
        """ Get: Values(self: SqlRowConstructorExpression) -> SqlScalarExpressionCollection """
        ...



class SqlRowConstructorExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlRowConstructorExpression]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlRowConstructorExpression]'>, <type 'object'>
    """ no doc """
    pass

class SqlScalarClrFunctionDefinition(SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlClrFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlScalarClrFunctionDefinition) -> SqlClrFunctionBodyDefinition """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarClrFunctionDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ReturnType(self) -> SqlScalarFunctionReturnType:
        """ Get: ReturnType(self: SqlScalarClrFunctionDefinition) -> SqlScalarFunctionReturnType """
        ...



class SqlScalarExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[SqlScalarExpression]'>, <type 'ISqlCodeCollection[SqlScalarExpression]'>, <type 'object'>
    """ no doc """
    pass

class SqlScalarExpressionError(SqlScalarExpression, ISqlErrorObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarExpressionError) -> IEnumerable[SqlCodeObject] """
        ...



class SqlScalarFunctionReturnType(SqlFunctionReturnType): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarFunctionReturnType) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DataType(self) -> SqlDataTypeSpecification:
        """ Get: DataType(self: SqlScalarFunctionReturnType) -> SqlDataTypeSpecification """
        ...



class SqlScalarRelationalFunctionDefinition(SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlMultistatementFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlScalarRelationalFunctionDefinition) -> SqlMultistatementFunctionBodyDefinition """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarRelationalFunctionDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ReturnType(self) -> SqlScalarFunctionReturnType:
        """ Get: ReturnType(self: SqlScalarRelationalFunctionDefinition) -> SqlScalarFunctionReturnType """
        ...



class SqlScalarSubQueryExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarSubQueryExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlScalarSubQueryExpression) -> SqlQueryExpression """
        ...



class SqlScalarVariableAssignment(SqlVariableAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlScalarVariableAssignment) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlScalarVariableAssignment) -> SqlScalarExpression """
        ...

    @property
    def Variable(self) -> SqlScalarVariableRefExpression:
        """ Get: Variable(self: SqlScalarVariableAssignment) -> SqlScalarVariableRefExpression """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlScalarVariableAssignment, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlScalarVariableAssignment, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlScalarVariableAssignment, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlScalarVariableAssignment, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlScalarVariableRefExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundVariable(self) -> ILocalVariable:
        """ Get: BoundVariable(self: SqlScalarVariableRefExpression) -> ILocalVariable """
        ...

    @property
    def VariableName(self) -> str:
        """ Get: VariableName(self: SqlScalarVariableRefExpression) -> str """
        ...


    @staticmethod
    def Create(variableName:str) -> SqlScalarVariableRefExpression:
        """ Create(variableName: str) -> SqlScalarVariableRefExpression """
        ...


class SqlScalarVariableRefExpressionError(ISqlErrorObject, SqlScalarVariableRefExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlSchemaElementCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlStatement]'>, <type 'IEnumerable[SqlStatement]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlScript(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Batches(self) -> SqlBatchCollection:
        """ Get: Batches(self: SqlScript) -> SqlBatchCollection """
        ...

    @property
    def Errors(self) -> IEnumerable:
        """ Get: Errors(self: SqlScript) -> IEnumerable[Error] """
        ...


    def RetrieveAllIdentifiers(self) -> IList:
        """ RetrieveAllIdentifiers(self: SqlScript) -> IList[SqlIdentifier] """
        ...


class SqlSearchedCaseExpression(SqlCaseExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSearchedCaseExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def WhenClauses(self) -> SqlSearchedWhenClauseCollection:
        """ Get: WhenClauses(self: SqlSearchedCaseExpression) -> SqlSearchedWhenClauseCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlSearchedCaseExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlSearchedCaseExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlSearchedCaseExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlSearchedCaseExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...

    elseExpression = ...


class SqlSearchedWhenClause(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSearchedWhenClause) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ThenExpression(self) -> SqlScalarExpression:
        """ Get: ThenExpression(self: SqlSearchedWhenClause) -> SqlScalarExpression """
        ...

    @property
    def WhenExpression(self) -> SqlBooleanExpression:
        """ Get: WhenExpression(self: SqlSearchedWhenClause) -> SqlBooleanExpression """
        ...



class SqlSearchedWhenClauseCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlSearchedWhenClause]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlSearchedWhenClause]'>, <type 'object'>
    """ no doc """
    pass

class SqlSelectClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsDistinct(self) -> bool:
        """ Get: IsDistinct(self: SqlSelectClause) -> bool """
        ...

    @property
    def SelectExpressions(self) -> SqlSelectExpressionCollection:
        """ Get: SelectExpressions(self: SqlSelectClause) -> SqlSelectExpressionCollection """
        ...

    @property
    def Top(self) -> SqlTopSpecification:
        """ Get: Top(self: SqlSelectClause) -> SqlTopSpecification """
        ...



class SqlSelectExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlSelectExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlSelectExpression]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlSelectExpression]'>, <type 'object'>
    """ no doc """
    pass

class SqlSelectIntoClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IntoTarget(self) -> SqlObjectIdentifier:
        """ Get: IntoTarget(self: SqlSelectIntoClause) -> SqlObjectIdentifier """
        ...



class SqlSelectScalarExpression(SqlSelectExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlSelectScalarExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSelectScalarExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlSelectScalarExpression) -> SqlScalarExpression """
        ...



class SqlSelectSpecification(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ForClause(self) -> SqlForClause:
        """ Get: ForClause(self: SqlSelectSpecification) -> SqlForClause """
        ...

    @property
    def OrderByClause(self) -> SqlOrderByClause:
        """ Get: OrderByClause(self: SqlSelectSpecification) -> SqlOrderByClause """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlSelectSpecification) -> SqlQueryExpression """
        ...



class SqlSelectSpecificationInsertSource(SqlInsertSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSelectSpecificationInsertSource) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def SelectSpecification(self) -> SqlSelectSpecification:
        """ Get: SelectSpecification(self: SqlSelectSpecificationInsertSource) -> SqlSelectSpecification """
        ...



class SqlSelectStarExpression(SqlSelectExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundColumns(self) -> IMetadataCollection:
        """ Get: BoundColumns(self: SqlSelectStarExpression) -> IMetadataCollection[IColumn] """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSelectStarExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Qualifier(self) -> SqlObjectIdentifier:
        """ Get: Qualifier(self: SqlSelectStarExpression) -> SqlObjectIdentifier """
        ...



class SqlSelectStatement(SqlStatement, IBindFinalizer): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlSelectStatement) -> IMetadataObject """
        ...

    @property
    def BoundTable(self) -> ITable:
        """ Get: BoundTable(self: SqlSelectStatement) -> ITable """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSelectStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def QueryWithClause(self) -> SqlQueryWithClause:
        """ Get: QueryWithClause(self: SqlSelectStatement) -> SqlQueryWithClause """
        ...

    @property
    def SelectSpecification(self) -> SqlSelectSpecification:
        """ Get: SelectSpecification(self: SqlSelectStatement) -> SqlSelectSpecification """
        ...



class SqlSelectVariableAssignmentExpression(SqlSelectExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSelectVariableAssignmentExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def VariableAssignment(self) -> SqlScalarVariableAssignment:
        """ Get: VariableAssignment(self: SqlSelectVariableAssignmentExpression) -> SqlScalarVariableAssignment """
        ...



class SqlSetStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    pass

class SqlSetAssignmentStatement(SqlSetStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSetAssignmentStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def VariableAssignment(self) -> SqlVariableAssignment:
        """ Get: VariableAssignment(self: SqlSetAssignmentStatement) -> SqlVariableAssignment """
        ...



class SqlSetClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Assignments(self) -> SqlAssignmentCollection:
        """ Get: Assignments(self: SqlSetClause) -> SqlAssignmentCollection """
        ...



class SqlSetClauseError(ISqlErrorObject, SqlSetClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlSetQuantifier(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlSetQuantifier, values: All (1), Distinct (2), None (0) """
    All: SqlSetQuantifier = ...
    Distinct: SqlSetQuantifier = ...
    value__ = ...


class SqlSetStatementError(SqlSetStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ SqlSetStatementError() """
    pass

class SqlSimpleCaseExpression(SqlCaseExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSimpleCaseExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TestExpression(self) -> SqlScalarExpression:
        """ Get: TestExpression(self: SqlSimpleCaseExpression) -> SqlScalarExpression """
        ...

    @property
    def WhenClauses(self) -> SqlSimpleWhenClauseCollection:
        """ Get: WhenClauses(self: SqlSimpleCaseExpression) -> SqlSimpleWhenClauseCollection """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlSimpleCaseExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlSimpleCaseExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlSimpleCaseExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlSimpleCaseExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...

    elseExpression = ...


class SqlSimpleGroupByItem(SqlGroupingSetItem): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlSimpleGroupByItem) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlSimpleGroupByItem) -> SqlScalarExpression """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlSimpleGroupByItem, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlSimpleGroupByItem, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlSimpleGroupByItem, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlSimpleGroupByItem, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlSimpleOrderByClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Items(self) -> SqlSimpleOrderByItemCollection:
        """ Get: Items(self: SqlSimpleOrderByClause) -> SqlSimpleOrderByItemCollection """
        ...



class SqlSimpleOrderByItem(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ColumnName(self) -> SqlIdentifier:
        """ Get: ColumnName(self: SqlSimpleOrderByItem) -> SqlIdentifier """
        ...

    @property
    def SortOrder(self) -> SqlSortOrder:
        """ Get: SortOrder(self: SqlSimpleOrderByItem) -> SqlSortOrder """
        ...



class SqlSimpleOrderByItemCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlSimpleOrderByItem]'>, <type 'IEnumerable'>, <type 'IEnumerable[SqlSimpleOrderByItem]'>, <type 'object'>
    """ no doc """
    pass

class SqlSimpleWhenClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ThenExpression(self) -> SqlScalarExpression:
        """ Get: ThenExpression(self: SqlSimpleWhenClause) -> SqlScalarExpression """
        ...

    @property
    def WhenExpression(self) -> SqlScalarExpression:
        """ Get: WhenExpression(self: SqlSimpleWhenClause) -> SqlScalarExpression """
        ...



class SqlSimpleWhenClauseCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlSimpleWhenClause]'>, <type 'IEnumerable[SqlSimpleWhenClause]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlSortedDataIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlSortedDataIndexOption) -> SqlOnOffValue """
        ...



class SqlSortedDataReorgIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlSortedDataReorgIndexOption) -> SqlOnOffValue """
        ...



class SqlSortInTempDbIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlSortInTempDbIndexOption) -> SqlOnOffValue """
        ...



class SqlSortOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlSortOrder, values: Ascending (1), Descending (2), None (0) """
    Ascending: SqlSortOrder = ...
    Descending: SqlSortOrder = ...
    value__ = ...


class SqlSparseOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlSparseOption, values: ColumnSet (2), None (0), Sparse (1) """
    ColumnSet: SqlSparseOption = ...
    Sparse: SqlSparseOption = ...
    value__ = ...


class SqlStatementCollection(SqlCollection): # skipped bases: <type 'ISqlCodeCollection[SqlStatement]'>, <type 'IEnumerable[SqlStatement]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlStatementRecursiveVisitor(ISqlStatementVisitor): # skipped bases: <type 'object'>
    """ SqlStatementRecursiveVisitor(visitor: ISqlStatementVisitor) """
    pass

class SqlStatisticsIncrementalIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlStatisticsIncrementalIndexOption) -> SqlOnOffValue """
        ...



class SqlStatisticsNoRecomputeIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlStatisticsNoRecomputeIndexOption) -> SqlOnOffValue """
        ...



class SqlStatisticsOnlyIndexOption(SqlIndexOption): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def OnOffValue(self) -> SqlOnOffValue:
        """ Get: OnOffValue(self: SqlStatisticsOnlyIndexOption) -> SqlOnOffValue """
        ...

    @property
    def Value(self) -> int:
        """ Get: Value(self: SqlStatisticsOnlyIndexOption) -> int """
        ...



class SqlStorageSpecification(INullCodeObject, SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlStorageSpecification() """
    pass

class SqlTableClrFunctionDefinition(SqlFunctionDefinition): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyDefinition(self) -> SqlClrFunctionBodyDefinition:
        """ Get: BodyDefinition(self: SqlTableClrFunctionDefinition) -> SqlClrFunctionBodyDefinition """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableClrFunctionDefinition) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def OrderByClause(self) -> SqlSimpleOrderByClause:
        """ Get: OrderByClause(self: SqlTableClrFunctionDefinition) -> SqlSimpleOrderByClause """
        ...

    @property
    def ReturnType(self) -> SqlTableFunctionReturnType:
        """ Get: ReturnType(self: SqlTableClrFunctionDefinition) -> SqlTableFunctionReturnType """
        ...



class SqlTableConstructorExpression(SqlQueryExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableConstructorExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Rows(self) -> SqlRowConstructorExpressionCollection:
        """ Get: Rows(self: SqlTableConstructorExpression) -> SqlRowConstructorExpressionCollection """
        ...



class SqlTableConstructorInsertSource(SqlInsertSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableConstructorInsertSource) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TableConstructorExpression(self) -> SqlTableConstructorExpression:
        """ Get: TableConstructorExpression(self: SqlTableConstructorInsertSource) -> SqlTableConstructorExpression """
        ...



class SqlTableDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ColumnDefinitions(self) -> IEnumerable:
        """ Get: ColumnDefinitions(self: SqlTableDefinition) -> IEnumerable[SqlColumnDefinition] """
        ...

    @property
    def Constraints(self) -> IEnumerable:
        """ Get: Constraints(self: SqlTableDefinition) -> IEnumerable[SqlConstraint] """
        ...

    @property
    def TemporalPeriodDefinitions(self) -> IEnumerable:
        """ Get: TemporalPeriodDefinitions(self: SqlTableDefinition) -> IEnumerable[SqlTemporalPeriodDefinition] """
        ...



class SqlTableExpressionCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlTableExpression]'>, <type 'ISqlCodeCollection[SqlTableExpression]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class SqlTableExpressionError(SqlTableExpression, ISqlErrorObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableExpressionError) -> IEnumerable[SqlCodeObject] """
        ...



class SqlTableFunctionReturnType(SqlFunctionReturnType): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableFunctionReturnType) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TableDefinition(self) -> SqlTableDefinition:
        """ Get: TableDefinition(self: SqlTableFunctionReturnType) -> SqlTableDefinition """
        ...



class SqlTableHint(SqlHint): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlTableHintType:
        """ Get: Type(self: SqlTableHint) -> SqlTableHintType """
        ...



class SqlTableHintType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlTableHintType, values: FastFirstRow (1), ForceSeek (2), HoldLock (4), KeepDefaults (8), KeepIdentity (16), NoExpand (32), NoLock (64), None (0), NoWait (128), PageLock (256), ReadCommitted (512), ReadCommittedLock (1024), ReadPast (2048), ReadUncommitted (4096), RepeatableRead (8192), Rowlock (16384), Serializable (32768), Snapshot (2097152), SpatialWindowMaxCells (1048576), TabLock (65536), TabLockX (131072), UpdateLock (262144), XLock (524288) """
    FastFirstRow: SqlTableHintType = ...
    ForceSeek: SqlTableHintType = ...
    HoldLock: SqlTableHintType = ...
    KeepDefaults: SqlTableHintType = ...
    KeepIdentity: SqlTableHintType = ...
    NoExpand: SqlTableHintType = ...
    NoLock: SqlTableHintType = ...
    NoWait: SqlTableHintType = ...
    PageLock: SqlTableHintType = ...
    ReadCommitted: SqlTableHintType = ...
    ReadCommittedLock: SqlTableHintType = ...
    ReadPast: SqlTableHintType = ...
    ReadUncommitted: SqlTableHintType = ...
    RepeatableRead: SqlTableHintType = ...
    Rowlock: SqlTableHintType = ...
    Serializable: SqlTableHintType = ...
    Snapshot: SqlTableHintType = ...
    SpatialWindowMaxCells: SqlTableHintType = ...
    TabLock: SqlTableHintType = ...
    TabLockX: SqlTableHintType = ...
    UpdateLock: SqlTableHintType = ...
    value__ = ...
    XLock: SqlTableHintType = ...


class SqlTableRefExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlTableRefExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableRefExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Hints(self) -> SqlHintCollection:
        """ Get: Hints(self: SqlTableRefExpression) -> SqlHintCollection """
        ...

    @property
    def ObjectIdentifier(self) -> SqlObjectIdentifier:
        """ Get: ObjectIdentifier(self: SqlTableRefExpression) -> SqlObjectIdentifier """
        ...



class SqlTableUdtMemberExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def MemberName(self) -> SqlIdentifier:
        """ Get: MemberName(self: SqlTableUdtMemberExpression) -> SqlIdentifier """
        ...



class SqlTableUdtInstanceMemberExpression(SqlTableUdtMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def UdtInstance(self) -> SqlScalarExpression:
        """ Get: UdtInstance(self: SqlTableUdtInstanceMemberExpression) -> SqlScalarExpression """
        ...



class SqlTableUdtInstanceMethodExpression(SqlTableUdtInstanceMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlTableUdtInstanceMethodExpression) -> SqlIdentifier """
        ...

    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlTableUdtInstanceMethodExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableUdtInstanceMethodExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlTableUdtInstanceMethodExpression) -> SqlIdentifierCollection """
        ...



class SqlTableValuedFunctionRefExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlTableValuedFunctionRefExpression) -> SqlIdentifier """
        ...

    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlTableValuedFunctionRefExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableValuedFunctionRefExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlTableValuedFunctionRefExpression) -> SqlIdentifierCollection """
        ...

    @property
    def ObjectIdentifier(self) -> SqlObjectIdentifier:
        """ Get: ObjectIdentifier(self: SqlTableValuedFunctionRefExpression) -> SqlObjectIdentifier """
        ...



class SqlTableVariableRefExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlTableVariableRefExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTableVariableRefExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlTableVariableRefExpression) -> str """
        ...



class SqlTargetTableExpression(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlTargetTableExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlTargetTableExpression) -> SqlObjectIdentifier """
        ...

    @property
    def OpenDataSourceCommandString(self) -> str:
        """ Get: OpenDataSourceCommandString(self: SqlTargetTableExpression) -> str """
        ...

    @property
    def OpenDataSourceObject(self) -> SqlObjectIdentifier:
        """ Get: OpenDataSourceObject(self: SqlTargetTableExpression) -> SqlObjectIdentifier """
        ...

    @property
    def TableHints(self) -> SqlHintCollection:
        """ Get: TableHints(self: SqlTargetTableExpression) -> SqlHintCollection """
        ...

    @property
    def TargetColumnList(self) -> SqlIdentifierCollection:
        """ Get: TargetColumnList(self: SqlTargetTableExpression) -> SqlIdentifierCollection """
        ...



class SqlTemporalPeriodDefinition(SqlCodeObject, ISqlTableElement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlTemporalPeriodDefinition) -> str """
        ...

    @property
    def RowEndColumnName(self) -> SqlIdentifier:
        """ Get: RowEndColumnName(self: SqlTemporalPeriodDefinition) -> SqlIdentifier """
        ...

    @property
    def RowStartColumnName(self) -> SqlIdentifier:
        """ Get: RowStartColumnName(self: SqlTemporalPeriodDefinition) -> SqlIdentifier """
        ...

    @property
    def Type(self) -> TemporalPeriodType:
        """ Get: Type(self: SqlTemporalPeriodDefinition) -> TemporalPeriodType """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlTemporalPeriodDefinition) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlTopSpecification(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def IsPercent(self) -> bool:
        """ Get: IsPercent(self: SqlTopSpecification) -> bool """
        ...

    @property
    def IsWithTies(self) -> bool:
        """ Get: IsWithTies(self: SqlTopSpecification) -> bool """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlTopSpecification) -> SqlScalarExpression """
        ...



class SqlTriggerAction(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlTriggerActionType:
        """ Get: Type(self: SqlTriggerAction) -> SqlTriggerActionType """
        ...



class SqlTriggerActionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlTriggerActionType, values: Delete (0), Insert (1), Update (2) """
    Delete: SqlTriggerActionType = ...
    Insert: SqlTriggerActionType = ...
    Update: SqlTriggerActionType = ...
    value__ = ...


class SqlTriggerActivationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlTriggerActivationType, values: After (0), For (1), InsteadOf (2) """
    After: SqlTriggerActivationType = ...
    For: SqlTriggerActivationType = ...
    InsteadOf: SqlTriggerActivationType = ...
    value__ = ...


class SqlTriggerDefinitionError(ISqlErrorObject, SqlTriggerDefinition, IDdlTriggerDefinitionInfo, IDmlTriggerDefinitionInfo): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTriggerDefinitionError) -> IEnumerable[SqlCodeObject] """
        ...



class SqlTriggerEvent(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlTriggerEvent) -> str """
        ...



class SqlTryCatchStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def CatchBlock(self) -> SqlStatementCollection:
        """ Get: CatchBlock(self: SqlTryCatchStatement) -> SqlStatementCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlTryCatchStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def TryBlock(self) -> SqlStatementCollection:
        """ Get: TryBlock(self: SqlTryCatchStatement) -> SqlStatementCollection """
        ...



class SqlUdtMemberExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def MemberName(self) -> SqlIdentifier:
        """ Get: MemberName(self: SqlUdtMemberExpression) -> SqlIdentifier """
        ...



class SqlUdtInstanceMemberExpression(SqlUdtMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def UdtInstance(self) -> SqlScalarExpression:
        """ Get: UdtInstance(self: SqlUdtInstanceMemberExpression) -> SqlScalarExpression """
        ...



class SqlUdtInstanceDataMemberExpression(SqlUdtInstanceMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUdtInstanceDataMemberExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlUdtInstanceMethodExpression(SqlUdtInstanceMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlUdtInstanceMethodExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUdtInstanceMethodExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlUdtStaticMemberExpression(SqlUdtMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> SqlDataTypeSpecification:
        """ Get: Type(self: SqlUdtStaticMemberExpression) -> SqlDataTypeSpecification """
        ...



class SqlUdtStaticDataMemberExpression(SqlUdtStaticMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUdtStaticDataMemberExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlUdtStaticMethodExpression(SqlUdtStaticMemberExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> SqlScalarExpressionCollection:
        """ Get: Arguments(self: SqlUdtStaticMethodExpression) -> SqlScalarExpressionCollection """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUdtStaticMethodExpression) -> IEnumerable[SqlCodeObject] """
        ...



class SqlUnaryScalarExpression(SqlScalarExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUnaryScalarExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Expression(self) -> SqlScalarExpression:
        """ Get: Expression(self: SqlUnaryScalarExpression) -> SqlScalarExpression """
        ...

    @property
    def Operator(self) -> SqlUnaryScalarOperatorType:
        """ Get: Operator(self: SqlUnaryScalarExpression) -> SqlUnaryScalarOperatorType """
        ...



class SqlUnaryScalarOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlUnaryScalarOperatorType, values: BitwiseNot (3), Negative (2), None (0), Positive (1) """
    BitwiseNot: SqlUnaryScalarOperatorType = ...
    Negative: SqlUnaryScalarOperatorType = ...
    Positive: SqlUnaryScalarOperatorType = ...
    value__ = ...


class SqlUniqueConstraint(SqlUniqueConstraintBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'ISqlTableElement'>, <type 'object'>
    """ no doc """
    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlUniqueConstraint, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlUniqueConstraint, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlUniqueConstraint, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlUniqueConstraint, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlUnpivotClause(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ColumnList(self) -> SqlColumnRefExpressionCollection:
        """ Get: ColumnList(self: SqlUnpivotClause) -> SqlColumnRefExpressionCollection """
        ...

    @property
    def PivotedColumn(self) -> SqlColumnRefExpression:
        """ Get: PivotedColumn(self: SqlUnpivotClause) -> SqlColumnRefExpression """
        ...

    @property
    def ValueColumn(self) -> SqlColumnRefExpression:
        """ Get: ValueColumn(self: SqlUnpivotClause) -> SqlColumnRefExpression """
        ...



class SqlUnpivotTableExpression(SqlTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Alias(self) -> SqlIdentifier:
        """ Get: Alias(self: SqlUnpivotTableExpression) -> SqlIdentifier """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUnpivotTableExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Source(self) -> SqlTableExpression:
        """ Get: Source(self: SqlUnpivotTableExpression) -> SqlTableExpression """
        ...

    @property
    def UnpivotClause(self) -> SqlUnpivotClause:
        """ Get: UnpivotClause(self: SqlUnpivotTableExpression) -> SqlUnpivotClause """
        ...



class SqlUnqualifiedJoinTableExpression(SqlJoinTableExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUnqualifiedJoinTableExpression) -> IEnumerable[SqlCodeObject] """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlUnqualifiedJoinTableExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlUnqualifiedJoinTableExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlUnqualifiedJoinTableExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlUnqualifiedJoinTableExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlUpdateBooleanExpression(SqlBooleanExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUpdateBooleanExpression) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def ColumnName(self) -> SqlIdentifier:
        """ Get: ColumnName(self: SqlUpdateBooleanExpression) -> SqlIdentifier """
        ...



class SqlUpdateMergeAction(SqlMergeAction): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUpdateMergeAction) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def SetClause(self) -> SqlSetClause:
        """ Get: SetClause(self: SqlUpdateMergeAction) -> SqlSetClause """
        ...



class SqlUpdateSpecification(SqlUpdateDeleteSpecificationBase): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUpdateSpecification) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def SetClause(self) -> SqlSetClause:
        """ Get: SetClause(self: SqlUpdateSpecification) -> SqlSetClause """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlUpdateSpecification, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlUpdateSpecification, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlUpdateSpecification, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlUpdateSpecification, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlUpdateStatement(SqlDmlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def UpdateSpecification(self) -> SqlUpdateSpecification:
        """ Get: UpdateSpecification(self: SqlUpdateStatement) -> SqlUpdateSpecification """
        ...



class SqlUserDefinedDataTypeNullState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlUserDefinedDataTypeNullState, values: None (0), NotNull (2), Null (1) """
    NotNull: SqlUserDefinedDataTypeNullState = ...
    Null: SqlUserDefinedDataTypeNullState = ...
    value__ = ...


class SqlUserDefinedScalarFunctionCallExpression(SqlScalarFunctionCallExpression): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ObjectIdentifier(self) -> SqlObjectIdentifier:
        """ Get: ObjectIdentifier(self: SqlUserDefinedScalarFunctionCallExpression) -> SqlObjectIdentifier """
        ...


    def Accept(self, visitor, context = ...): # ->  # Not found arg types: {'context': 'C', 'visitor': 'ISqlCodeObjectContextVisitor'}
        """
        Accept(self: SqlUserDefinedScalarFunctionCallExpression, visitor: ISqlCodeObjectVisitor)Accept[T](self: SqlUserDefinedScalarFunctionCallExpression, visitor: ISqlCodeObjectVisitor[T]) -> T
        Accept[C](self: SqlUserDefinedScalarFunctionCallExpression, visitor: ISqlCodeObjectContextVisitor[C], context: C)Accept[(T, C)](self: SqlUserDefinedScalarFunctionCallExpression, visitor: ISqlCodeObjectContextVisitor[T, C], context: C) -> T
        """
        ...


class SqlUseStatement(SqlStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def BoundObject(self) -> IMetadataObject:
        """ Get: BoundObject(self: SqlUseStatement) -> IMetadataObject """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlUseStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def DatabaseName(self) -> SqlIdentifier:
        """ Get: DatabaseName(self: SqlUseStatement) -> SqlIdentifier """
        ...



class SqlValuesInsertMergeActionSource(SqlInsertMergeActionSource): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlValuesInsertMergeActionSource) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Values(self) -> SqlScalarExpressionCollection:
        """ Get: Values(self: SqlValuesInsertMergeActionSource) -> SqlScalarExpressionCollection """
        ...



class SqlVariableColumnAssignment(SqlAssignment): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlVariableColumnAssignment) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Column(self) -> SqlScalarRefExpression:
        """ Get: Column(self: SqlVariableColumnAssignment) -> SqlScalarRefExpression """
        ...

    @property
    def Value(self) -> SqlScalarExpression:
        """ Get: Value(self: SqlVariableColumnAssignment) -> SqlScalarExpression """
        ...

    @property
    def Variable(self) -> SqlScalarVariableRefExpression:
        """ Get: Variable(self: SqlVariableColumnAssignment) -> SqlScalarVariableRefExpression """
        ...



class SqlVariableDeclarationCollection(SqlCollection): # skipped bases: <type 'IEnumerable[SqlVariableDeclaration]'>, <type 'IEnumerable'>, <type 'ISqlCodeCollection[SqlVariableDeclaration]'>, <type 'object'>
    """ no doc """
    pass

class SqlVariableDeclareStatement(SqlDeclareStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlVariableDeclareStatement) -> IEnumerable[SqlCodeObject] """
        ...

    @property
    def Declarations(self) -> SqlVariableDeclarationCollection:
        """ Get: Declarations(self: SqlVariableDeclareStatement) -> SqlVariableDeclarationCollection """
        ...



class SqlViewDefinition(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    @property
    def ColumnList(self) -> SqlIdentifierCollection:
        """ Get: ColumnList(self: SqlViewDefinition) -> SqlIdentifierCollection """
        ...

    @property
    def HasCheckOption(self) -> bool:
        """ Get: HasCheckOption(self: SqlViewDefinition) -> bool """
        ...

    @property
    def Name(self) -> SqlObjectIdentifier:
        """ Get: Name(self: SqlViewDefinition) -> SqlObjectIdentifier """
        ...

    @property
    def Options(self) -> SqlCollection:
        """ Get: Options(self: SqlViewDefinition) -> SqlCollection[SqlModuleOption] """
        ...

    @property
    def QueryExpression(self) -> SqlQueryExpression:
        """ Get: QueryExpression(self: SqlViewDefinition) -> SqlQueryExpression """
        ...

    @property
    def QueryWithClause(self) -> SqlQueryWithClause:
        """ Get: QueryWithClause(self: SqlViewDefinition) -> SqlQueryWithClause """
        ...



class SqlWhereClause(SqlConditionClause): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ no doc """
    pass

class SqlWhileStatement(SqlConditionalStatement): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'IVisitableSqlStatement'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SqlWhileStatement) -> IEnumerable[SqlCodeObject] """
        ...



class SqlXmlDocumentConstraint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlXmlDocumentConstraint, values: Content (1), Document (2), None (0) """
    Content: SqlXmlDocumentConstraint = ...
    Document: SqlXmlDocumentConstraint = ...
    value__ = ...


class SqlXmlNamespacesDeclaration(SqlCodeObject): # skipped bases: <type 'IVisitableSqlCodeObject'>, <type 'object'>
    """ SqlXmlNamespacesDeclaration() """
    pass

class TemporalPeriodType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TemporalPeriodType, values: AppTime (1), SystemTime (0) """
    AppTime: TemporalPeriodType = ...
    SystemTime: TemporalPeriodType = ...
    value__ = ...


class TriggerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TriggerType, values: DdlTrigger (1), DmlTrigger (0) """
    DdlTrigger: TriggerType = ...
    DmlTrigger: TriggerType = ...
    value__ = ...


class TriggerTypeEx(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TriggerTypeEx, values: DatabaseDdlTrigger (1), DmlTrigger (0), ServerDdlTrigger (2) """
    DatabaseDdlTrigger: TriggerTypeEx = ...
    DmlTrigger: TriggerTypeEx = ...
    ServerDdlTrigger: TriggerTypeEx = ...
    value__ = ...


class ValidateModuleBodyVisitor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def FunctionBinderVisitor(self) -> SqlStatementRecursiveVisitor:
        """ Get: FunctionBinderVisitor() -> SqlStatementRecursiveVisitor """
        ...

    @property
    def ProcedureParserVisitor(self) -> SqlStatementRecursiveVisitor:
        """ Get: ProcedureParserVisitor() -> SqlStatementRecursiveVisitor """
        ...

    @property
    def ScalarFunctionParserVisitor(self) -> SqlStatementRecursiveVisitor:
        """ Get: ScalarFunctionParserVisitor() -> SqlStatementRecursiveVisitor """
        ...

    @property
    def TableFunctionParserVisitor(self) -> SqlStatementRecursiveVisitor:
        """ Get: TableFunctionParserVisitor() -> SqlStatementRecursiveVisitor """
        ...

    @property
    def TriggerParserVisitor(self) -> SqlStatementRecursiveVisitor:
        """ Get: TriggerParserVisitor() -> SqlStatementRecursiveVisitor """
        ...


    __all__: list = ...


