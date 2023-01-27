# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.Intellisense calls itself Intellisense
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import CodeObjectQuickInfo, MethodNameAndParamLocations

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    IMetadataDisplayInfoProvider)

from Microsoft.SqlServer.Management.SqlParser.Parser import PairMatch

from System import Enum, IComparable

from System.Collections import IEnumerable, IList

from System.Collections.Generic import List

from System.Data.Common.EntitySql import ParseResult

"""The following names are not found in the module: BlockInformation, field#
"""

# no functions
# classes

class Declaration(IComparable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DatabaseQualifiedName(self) -> str:
        """ Get: DatabaseQualifiedName(self: Declaration) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Declaration) -> str """
        ...

    @property
    def Title(self) -> str:
        """ Get: Title(self: Declaration) -> str """
        ...

    @property
    def Type(self) -> DeclarationType:
        """ Get: Type(self: Declaration) -> DeclarationType """
        ...


    def ToString(self) -> str:
        """ ToString(self: Declaration) -> str """
        ...


class DeclarationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeclarationType, values: ApplicationRole (0), AsymmetricKey (1), BuiltInFunction (2), Certificate (3), CheckConstraint (4), Collation (5), Column (6), Credential (7), CursorDataType (8), CursorParameter (9), CursorVariable (10), Database (11), DatabaseDdlTrigger (12), DatabasePermission (13), DatabaseRole (14), DatePart (15), DefaultConstraint (16), DmlTrigger (17), ExecutionContext (18), ExtendedStoredProcedure (19), FileGroup (20), ForeignKeyColumn (21), ForeignKeyConstraint (22), IndexedColumn (23), Login (24), PartitionScheme (25), PrimaryKeyConstraint (26), RelationalIndex (27), ScalarDataType (29), ScalarExpression (28), ScalarParameter (30), ScalarValuedFunction (31), ScalarVariable (32), Schema (33), Server (34), ServerDdlTrigger (35), SpatialIndex (36), Statistics (37), StoredProcedure (38), Synonym (39), SystemDataType (40), Table (41), TableDataType (42), TableParameter (43), TableValuedFunction (44), TableVariable (45), UdtDataMember (47), UdtMethod (48), UniqueConstraint (49), User (46), UserDefinedAggregate (50), UserDefinedClrType (51), UserDefinedDataType (52), UserDefinedTableType (53), View (54), VirtualTable (55), XmlDataTypeMethod (56), XmlIndex (57) """
    ApplicationRole: DeclarationType = ...
    AsymmetricKey: DeclarationType = ...
    BuiltInFunction: DeclarationType = ...
    Certificate: DeclarationType = ...
    CheckConstraint: DeclarationType = ...
    Collation: DeclarationType = ...
    Column: DeclarationType = ...
    Credential: DeclarationType = ...
    CursorDataType: DeclarationType = ...
    CursorParameter: DeclarationType = ...
    CursorVariable: DeclarationType = ...
    Database: DeclarationType = ...
    DatabaseDdlTrigger: DeclarationType = ...
    DatabasePermission: DeclarationType = ...
    DatabaseRole: DeclarationType = ...
    DatePart: DeclarationType = ...
    DefaultConstraint: DeclarationType = ...
    DmlTrigger: DeclarationType = ...
    ExecutionContext: DeclarationType = ...
    ExtendedStoredProcedure: DeclarationType = ...
    FileGroup: DeclarationType = ...
    ForeignKeyColumn: DeclarationType = ...
    ForeignKeyConstraint: DeclarationType = ...
    IndexedColumn: DeclarationType = ...
    Login: DeclarationType = ...
    PartitionScheme: DeclarationType = ...
    PrimaryKeyConstraint: DeclarationType = ...
    RelationalIndex: DeclarationType = ...
    ScalarDataType: DeclarationType = ...
    ScalarExpression: DeclarationType = ...
    ScalarParameter: DeclarationType = ...
    ScalarValuedFunction: DeclarationType = ...
    ScalarVariable: DeclarationType = ...
    Schema: DeclarationType = ...
    Server: DeclarationType = ...
    ServerDdlTrigger: DeclarationType = ...
    SpatialIndex: DeclarationType = ...
    Statistics: DeclarationType = ...
    StoredProcedure: DeclarationType = ...
    Synonym: DeclarationType = ...
    SystemDataType: DeclarationType = ...
    Table: DeclarationType = ...
    TableDataType: DeclarationType = ...
    TableParameter: DeclarationType = ...
    TableValuedFunction: DeclarationType = ...
    TableVariable: DeclarationType = ...
    UdtDataMember: DeclarationType = ...
    UdtMethod: DeclarationType = ...
    UniqueConstraint: DeclarationType = ...
    User: DeclarationType = ...
    UserDefinedAggregate: DeclarationType = ...
    UserDefinedClrType: DeclarationType = ...
    UserDefinedDataType: DeclarationType = ...
    UserDefinedTableType: DeclarationType = ...
    value__ = ...
    View: DeclarationType = ...
    VirtualTable: DeclarationType = ...
    XmlDataTypeMethod: DeclarationType = ...
    XmlIndex: DeclarationType = ...


class Resolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BlockInformation(self, *args): #cannot find CLR method
        """ no doc """
        ...

    @staticmethod
    def FindBreakPointInformation(parseResult:ParseResult, line:int, col:int): # -> BlockInformation
        """ FindBreakPointInformation(parseResult: ParseResult, line: int, col: int) -> BlockInformation """
        ...

    @staticmethod
    def FindCompletions(parseResult:ParseResult, line:int, col:int, displayInfoProvider:IMetadataDisplayInfoProvider) -> IList:
        """ FindCompletions(parseResult: ParseResult, line: int, col: int, displayInfoProvider: IMetadataDisplayInfoProvider) -> IList[Declaration] """
        ...

    @staticmethod
    def FindMethods(parseResult:ParseResult, line:int, col:int, displayInfoProvider:IMetadataDisplayInfoProvider) -> List:
        """ FindMethods(parseResult: ParseResult, line: int, col: int, displayInfoProvider: IMetadataDisplayInfoProvider) -> List[MethodHelpText] """
        ...

    @staticmethod
    def FindPairMatch(parseResult:ParseResult, line:int, col:int) -> PairMatch:
        """ FindPairMatch(parseResult: ParseResult, line: int, col: int) -> PairMatch """
        ...

    @staticmethod
    def FindRegionObjects(parseResult:ParseResult) -> IEnumerable:
        """ FindRegionObjects(parseResult: ParseResult) -> IEnumerable[Region] """
        ...

    @staticmethod
    def GetBlockInformation(parseResult:ParseResult, line:int, col:int): # -> BlockInformation
        """ GetBlockInformation(parseResult: ParseResult, line: int, col: int) -> BlockInformation """
        ...

    @staticmethod
    def GetMethodNameAndParams(parseResult:ParseResult, line:int, column:int, displayInfoProvider:IMetadataDisplayInfoProvider) -> MethodNameAndParamLocations:
        """ GetMethodNameAndParams(parseResult: ParseResult, line: int, column: int, displayInfoProvider: IMetadataDisplayInfoProvider) -> MethodNameAndParamLocations """
        ...

    @staticmethod
    def GetQuickInfo(parseResult:ParseResult, line:int, col:int, displayInfoProvider:IMetadataDisplayInfoProvider) -> CodeObjectQuickInfo:
        """ GetQuickInfo(parseResult: ParseResult, line: int, col: int, displayInfoProvider: IMetadataDisplayInfoProvider) -> CodeObjectQuickInfo """
        ...



