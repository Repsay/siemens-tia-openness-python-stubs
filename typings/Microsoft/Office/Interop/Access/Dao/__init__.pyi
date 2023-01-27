# encoding: utf-8
# module Microsoft.Office.Interop.Access.Dao calls itself Dao
# from Microsoft.Office.Interop.Access.Dao, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Int16, Single

from System.Collections import IEnumerable

"""The following names are not found in the module: __ComObject, field#
"""

# no functions
# classes

class CollatingOrderEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CollatingOrderEnum, values: dbSortArabic (1025), dbSortChineseSimplified (2052), dbSortChineseTraditional (1028), dbSortCyrillic (1049), dbSortCzech (1029), dbSortDutch (1043), dbSortGeneral (1033), dbSortGreek (1032), dbSortHebrew (1037), dbSortHindi (1081), dbSortHungarian (1038), dbSortIcelandic (1039), dbSortJapanese (1041), dbSortJapaneseRadicalStrokeCount (263185), dbSortKorean (1042), dbSortNeutral (1024), dbSortNorwdan (1030), dbSortPDXIntl (1033), dbSortPDXNor (1030), dbSortPDXSwe (1053), dbSortPolish (1045), dbSortSlovenian (1060), dbSortSpanish (1034), dbSortSwedFin (1053), dbSortThai (1054), dbSortTurkish (1055), dbSortUndefined (-1) """
    dbSortArabic: CollatingOrderEnum = ...
    dbSortChineseSimplified: CollatingOrderEnum = ...
    dbSortChineseTraditional: CollatingOrderEnum = ...
    dbSortCyrillic: CollatingOrderEnum = ...
    dbSortCzech: CollatingOrderEnum = ...
    dbSortDutch: CollatingOrderEnum = ...
    dbSortGeneral: CollatingOrderEnum = ...
    dbSortGreek: CollatingOrderEnum = ...
    dbSortHebrew: CollatingOrderEnum = ...
    dbSortHindi: CollatingOrderEnum = ...
    dbSortHungarian: CollatingOrderEnum = ...
    dbSortIcelandic: CollatingOrderEnum = ...
    dbSortJapanese: CollatingOrderEnum = ...
    dbSortJapaneseRadicalStrokeCount: CollatingOrderEnum = ...
    dbSortKorean: CollatingOrderEnum = ...
    dbSortNeutral: CollatingOrderEnum = ...
    dbSortNorwdan: CollatingOrderEnum = ...
    dbSortPDXIntl: CollatingOrderEnum = ...
    dbSortPDXNor: CollatingOrderEnum = ...
    dbSortPDXSwe: CollatingOrderEnum = ...
    dbSortPolish: CollatingOrderEnum = ...
    dbSortSlovenian: CollatingOrderEnum = ...
    dbSortSpanish: CollatingOrderEnum = ...
    dbSortSwedFin: CollatingOrderEnum = ...
    dbSortThai: CollatingOrderEnum = ...
    dbSortTurkish: CollatingOrderEnum = ...
    dbSortUndefined: CollatingOrderEnum = ...
    value__ = ...


class CommitTransOptionsEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CommitTransOptionsEnum, values: dbForceOSFlush (1) """
    dbForceOSFlush: CommitTransOptionsEnum = ...
    value__ = ...


class ComplexType: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: ComplexType) -> Fields """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Connection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connect(self) -> str:
        """ Get: Connect(self: Connection) -> str """
        ...

    @property
    def Database(self) -> Database:
        """ Get: Database(self: Connection) -> Database """
        ...

    @property
    def hDbc(self) -> int:
        """ Get: hDbc(self: Connection) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Connection) -> str """
        ...

    @property
    def QueryDefs(self) -> QueryDefs:
        """ Get: QueryDefs(self: Connection) -> QueryDefs """
        ...

    @property
    def QueryTimeout(self) -> Int16:
        """
        Get: QueryTimeout(self: Connection) -> Int16
        Set: QueryTimeout(self: Connection) = value
        """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: Connection) -> int """
        ...

    @property
    def Recordsets(self) -> Recordsets:
        """ Get: Recordsets(self: Connection) -> Recordsets """
        ...

    @property
    def StillExecuting(self) -> bool:
        """ Get: StillExecuting(self: Connection) -> bool """
        ...

    @property
    def Transactions(self) -> bool:
        """ Get: Transactions(self: Connection) -> bool """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: Connection) -> bool """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: Connection) """
        ...

    def Close(self): # -> 
        """ Close(self: Connection) """
        ...

    def CreateQueryDef(self, Name:object, SQLText:object) -> QueryDef:
        """ CreateQueryDef(self: Connection, Name: object, SQLText: object) -> QueryDef """
        ...

    def Execute(self, Query:str, Options:object): # -> 
        """ Execute(self: Connection, Query: str, Options: object) """
        ...

    def OpenRecordset(self, Name:str, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ OpenRecordset(self: Connection, Name: str, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class _Collection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> Int16:
        """ Get: Count(self: _Collection) -> Int16 """
        ...


    def Refresh(self): # -> 
        """ Refresh(self: _Collection) """
        ...


class Connections(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class _DAO: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: _DAO) -> Properties """
        ...



class Container(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllPermissions(self) -> int:
        """ Get: AllPermissions(self: Container) -> int """
        ...

    @property
    def Documents(self) -> Documents:
        """ Get: Documents(self: Container) -> Documents """
        ...

    @property
    def Inherit(self) -> bool:
        """
        Get: Inherit(self: Container) -> bool
        Set: Inherit(self: Container) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Container) -> str """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: Container) -> str
        Set: Owner(self: Container) = value
        """
        ...

    @property
    def Permissions(self) -> int:
        """
        Get: Permissions(self: Container) -> int
        Set: Permissions(self: Container) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: Container) -> str
        Set: UserName(self: Container) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Containers(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CursorDriverEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CursorDriverEnum, values: dbUseClientBatchCursor (3), dbUseDefaultCursor (-1), dbUseNoCursor (4), dbUseODBCCursor (1), dbUseServerCursor (2) """
    dbUseClientBatchCursor: CursorDriverEnum = ...
    dbUseDefaultCursor: CursorDriverEnum = ...
    dbUseNoCursor: CursorDriverEnum = ...
    dbUseODBCCursor: CursorDriverEnum = ...
    dbUseServerCursor: CursorDriverEnum = ...
    value__ = ...


class Database(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CollatingOrder(self) -> int:
        """ Get: CollatingOrder(self: Database) -> int """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: Database) -> str
        Set: Connect(self: Database) = value
        """
        ...

    @property
    def Connection(self) -> Connection:
        """ Get: Connection(self: Database) -> Connection """
        ...

    @property
    def Containers(self) -> Containers:
        """ Get: Containers(self: Database) -> Containers """
        ...

    @property
    def DesignMasterID(self) -> str:
        """
        Get: DesignMasterID(self: Database) -> str
        Set: DesignMasterID(self: Database) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Database) -> str """
        ...

    @property
    def QueryDefs(self) -> QueryDefs:
        """ Get: QueryDefs(self: Database) -> QueryDefs """
        ...

    @property
    def QueryTimeout(self) -> Int16:
        """
        Get: QueryTimeout(self: Database) -> Int16
        Set: QueryTimeout(self: Database) = value
        """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: Database) -> int """
        ...

    @property
    def Recordsets(self) -> Recordsets:
        """ Get: Recordsets(self: Database) -> Recordsets """
        ...

    @property
    def Relations(self) -> Relations:
        """ Get: Relations(self: Database) -> Relations """
        ...

    @property
    def ReplicaID(self) -> str:
        """ Get: ReplicaID(self: Database) -> str """
        ...

    @property
    def TableDefs(self) -> TableDefs:
        """ Get: TableDefs(self: Database) -> TableDefs """
        ...

    @property
    def Transactions(self) -> bool:
        """ Get: Transactions(self: Database) -> bool """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: Database) -> bool """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Database) -> str """
        ...


    def BeginTrans(self): # -> 
        """ BeginTrans(self: Database) """
        ...

    def Close(self): # -> 
        """ Close(self: Database) """
        ...

    def CommitTrans(self, Options:int): # -> 
        """ CommitTrans(self: Database, Options: int) """
        ...

    def CreateDynaset(self, Name:str, Options:object, Inconsistent:object) -> Recordset:
        """ CreateDynaset(self: Database, Name: str, Options: object, Inconsistent: object) -> Recordset """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: Database, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def CreateQueryDef(self, Name:object, SQLText:object) -> QueryDef:
        """ CreateQueryDef(self: Database, Name: object, SQLText: object) -> QueryDef """
        ...

    def CreateRelation(self, Name:object, Table:object, ForeignTable:object, Attributes:object) -> Relation:
        """ CreateRelation(self: Database, Name: object, Table: object, ForeignTable: object, Attributes: object) -> Relation """
        ...

    def CreateSnapshot(self, Source:str, Options:object) -> Recordset:
        """ CreateSnapshot(self: Database, Source: str, Options: object) -> Recordset """
        ...

    def CreateTableDef(self, Name:object, Attributes:object, SourceTableName:object, Connect:object) -> TableDef:
        """ CreateTableDef(self: Database, Name: object, Attributes: object, SourceTableName: object, Connect: object) -> TableDef """
        ...

    def DeleteQueryDef(self, Name:str): # -> 
        """ DeleteQueryDef(self: Database, Name: str) """
        ...

    def Execute(self, Query:str, Options:object): # -> 
        """ Execute(self: Database, Query: str, Options: object) """
        ...

    def ExecuteSQL(self, SQL:str) -> int:
        """ ExecuteSQL(self: Database, SQL: str) -> int """
        ...

    def ListFields(self, Name:str) -> Recordset:
        """ ListFields(self: Database, Name: str) -> Recordset """
        ...

    def ListTables(self) -> Recordset:
        """ ListTables(self: Database) -> Recordset """
        ...

    def MakeReplica(self, PathName:str, Description:str, Options:object): # -> 
        """ MakeReplica(self: Database, PathName: str, Description: str, Options: object) """
        ...

    def NewPassword(self, bstrOld:str, bstrNew:str): # -> 
        """ NewPassword(self: Database, bstrOld: str, bstrNew: str) """
        ...

    def OpenQueryDef(self, Name:str) -> QueryDef:
        """ OpenQueryDef(self: Database, Name: str) -> QueryDef """
        ...

    def OpenRecordset(self, Name:str, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ OpenRecordset(self: Database, Name: str, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def OpenTable(self, Name:str, Options:object) -> Recordset:
        """ OpenTable(self: Database, Name: str, Options: object) -> Recordset """
        ...

    def PopulatePartial(self, DbPathName:str): # -> 
        """ PopulatePartial(self: Database, DbPathName: str) """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: Database) """
        ...

    def Synchronize(self, DbPathName:str, ExchangeType:object): # -> 
        """ Synchronize(self: Database, DbPathName: str, ExchangeType: object) """
        ...

    def _30_OpenRecordset(self, Name:str, Type:object, Options:object) -> Recordset:
        """ _30_OpenRecordset(self: Database, Name: str, Type: object, Options: object) -> Recordset """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Databases(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DatabaseTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseTypeEnum, values: dbDecrypt (4), dbEncrypt (2), dbVersion10 (1), dbVersion11 (8), dbVersion120 (128), dbVersion140 (256), dbVersion150 (512), dbVersion20 (16), dbVersion30 (32), dbVersion40 (64) """
    dbDecrypt: DatabaseTypeEnum = ...
    dbEncrypt: DatabaseTypeEnum = ...
    dbVersion10: DatabaseTypeEnum = ...
    dbVersion11: DatabaseTypeEnum = ...
    dbVersion120: DatabaseTypeEnum = ...
    dbVersion140: DatabaseTypeEnum = ...
    dbVersion150: DatabaseTypeEnum = ...
    dbVersion20: DatabaseTypeEnum = ...
    dbVersion30: DatabaseTypeEnum = ...
    dbVersion40: DatabaseTypeEnum = ...
    value__ = ...


class DataTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataTypeEnum, values: dbAttachment (101), dbBigInt (16), dbBinary (9), dbBoolean (1), dbByte (2), dbChar (18), dbComplexByte (102), dbComplexDecimal (108), dbComplexDouble (106), dbComplexGUID (107), dbComplexInteger (103), dbComplexLong (104), dbComplexSingle (105), dbComplexText (109), dbCurrency (5), dbDate (8), dbDecimal (20), dbDouble (7), dbFloat (21), dbGUID (15), dbInteger (3), dbLong (4), dbLongBinary (11), dbMemo (12), dbNumeric (19), dbSingle (6), dbText (10), dbTime (22), dbTimeStamp (23), dbVarBinary (17) """
    dbAttachment: DataTypeEnum = ...
    dbBigInt: DataTypeEnum = ...
    dbBinary: DataTypeEnum = ...
    dbBoolean: DataTypeEnum = ...
    dbByte: DataTypeEnum = ...
    dbChar: DataTypeEnum = ...
    dbComplexByte: DataTypeEnum = ...
    dbComplexDecimal: DataTypeEnum = ...
    dbComplexDouble: DataTypeEnum = ...
    dbComplexGUID: DataTypeEnum = ...
    dbComplexInteger: DataTypeEnum = ...
    dbComplexLong: DataTypeEnum = ...
    dbComplexSingle: DataTypeEnum = ...
    dbComplexText: DataTypeEnum = ...
    dbCurrency: DataTypeEnum = ...
    dbDate: DataTypeEnum = ...
    dbDecimal: DataTypeEnum = ...
    dbDouble: DataTypeEnum = ...
    dbFloat: DataTypeEnum = ...
    dbGUID: DataTypeEnum = ...
    dbInteger: DataTypeEnum = ...
    dbLong: DataTypeEnum = ...
    dbLongBinary: DataTypeEnum = ...
    dbMemo: DataTypeEnum = ...
    dbNumeric: DataTypeEnum = ...
    dbSingle: DataTypeEnum = ...
    dbText: DataTypeEnum = ...
    dbTime: DataTypeEnum = ...
    dbTimeStamp: DataTypeEnum = ...
    dbVarBinary: DataTypeEnum = ...
    value__ = ...


class _DBEngine(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultPassword(self): # -> 
        """ Set: DefaultPassword(self: _DBEngine) = value """
        ...

    @property
    def DefaultType(self) -> int:
        """
        Get: DefaultType(self: _DBEngine) -> int
        Set: DefaultType(self: _DBEngine) = value
        """
        ...

    @property
    def DefaultUser(self): # -> 
        """ Set: DefaultUser(self: _DBEngine) = value """
        ...

    @property
    def Errors(self) -> Errors:
        """ Get: Errors(self: _DBEngine) -> Errors """
        ...

    @property
    def IniPath(self) -> str:
        """
        Get: IniPath(self: _DBEngine) -> str
        Set: IniPath(self: _DBEngine) = value
        """
        ...

    @property
    def LoginTimeout(self) -> Int16:
        """
        Get: LoginTimeout(self: _DBEngine) -> Int16
        Set: LoginTimeout(self: _DBEngine) = value
        """
        ...

    @property
    def SystemDB(self) -> str:
        """
        Get: SystemDB(self: _DBEngine) -> str
        Set: SystemDB(self: _DBEngine) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: _DBEngine) -> str """
        ...

    @property
    def Workspaces(self) -> Workspaces:
        """ Get: Workspaces(self: _DBEngine) -> Workspaces """
        ...


    def BeginTrans(self): # -> 
        """ BeginTrans(self: _DBEngine) """
        ...

    def CommitTrans(self, Option:int): # -> 
        """ CommitTrans(self: _DBEngine, Option: int) """
        ...

    def CompactDatabase(self, SrcName:str, DstName:str, DstLocale:object, Options:object, SrcLocale:object): # -> 
        """ CompactDatabase(self: _DBEngine, SrcName: str, DstName: str, DstLocale: object, Options: object, SrcLocale: object) """
        ...

    def CreateDatabase(self, Name:str, Locale:str, Option:object) -> Database:
        """ CreateDatabase(self: _DBEngine, Name: str, Locale: str, Option: object) -> Database """
        ...

    def CreateWorkspace(self, Name:str, UserName:str, Password:str, UseType:object) -> Workspace:
        """ CreateWorkspace(self: _DBEngine, Name: str, UserName: str, Password: str, UseType: object) -> Workspace """
        ...

    def FreeLocks(self): # -> 
        """ FreeLocks(self: _DBEngine) """
        ...

    def Idle(self, Action:object): # -> 
        """ Idle(self: _DBEngine, Action: object) """
        ...

    def ISAMStats(self, StatNum:int, Reset:object) -> int:
        """ ISAMStats(self: _DBEngine, StatNum: int, Reset: object) -> int """
        ...

    def OpenConnection(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Connection:
        """ OpenConnection(self: _DBEngine, Name: str, Options: object, ReadOnly: object, Connect: object) -> Connection """
        ...

    def OpenDatabase(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Database:
        """ OpenDatabase(self: _DBEngine, Name: str, Options: object, ReadOnly: object, Connect: object) -> Database """
        ...

    def RegisterDatabase(self, Dsn:str, Driver:str, Silent:bool, Attributes:str): # -> 
        """ RegisterDatabase(self: _DBEngine, Dsn: str, Driver: str, Silent: bool, Attributes: str) """
        ...

    def RepairDatabase(self, Name:str): # -> 
        """ RepairDatabase(self: _DBEngine, Name: str) """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: _DBEngine) """
        ...

    def SetDataAccessOption(self, Option:Int16, Value:object): # -> 
        """ SetDataAccessOption(self: _DBEngine, Option: Int16, Value: object) """
        ...

    def SetDefaultWorkspace(self, Name:str, Password:str): # -> 
        """ SetDefaultWorkspace(self: _DBEngine, Name: str, Password: str) """
        ...

    def SetOption(self, Option:int, Value:object): # -> 
        """ SetOption(self: _DBEngine, Option: int, Value: object) """
        ...

    def _30_CreateWorkspace(self, Name:str, UserName:str, Password:str) -> Workspace:
        """ _30_CreateWorkspace(self: _DBEngine, Name: str, UserName: str, Password: str) -> Workspace """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DBEngine(_DBEngine): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class DBEngineClass(__ComObject, DBEngine): # skipped bases: <type '_DBEngine'>, <type '_DAO'>, <type 'object'>
    """ DBEngineClass() """
    @property
    def DefaultPassword(self): # -> 
        """ Set: DefaultPassword(self: DBEngineClass) = value """
        ...

    @property
    def DefaultType(self) -> int:
        """
        Get: DefaultType(self: DBEngineClass) -> int
        Set: DefaultType(self: DBEngineClass) = value
        """
        ...

    @property
    def DefaultUser(self): # -> 
        """ Set: DefaultUser(self: DBEngineClass) = value """
        ...

    @property
    def Errors(self) -> Errors:
        """ Get: Errors(self: DBEngineClass) -> Errors """
        ...

    @property
    def IniPath(self) -> str:
        """
        Get: IniPath(self: DBEngineClass) -> str
        Set: IniPath(self: DBEngineClass) = value
        """
        ...

    @property
    def LoginTimeout(self) -> Int16:
        """
        Get: LoginTimeout(self: DBEngineClass) -> Int16
        Set: LoginTimeout(self: DBEngineClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: DBEngineClass) -> Properties """
        ...

    @property
    def SystemDB(self) -> str:
        """
        Get: SystemDB(self: DBEngineClass) -> str
        Set: SystemDB(self: DBEngineClass) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: DBEngineClass) -> str """
        ...

    @property
    def Workspaces(self) -> Workspaces:
        """ Get: Workspaces(self: DBEngineClass) -> Workspaces """
        ...


    def BeginTrans(self): # -> 
        """ BeginTrans(self: DBEngineClass) """
        ...

    def CommitTrans(self, Option:int): # -> 
        """ CommitTrans(self: DBEngineClass, Option: int) """
        ...

    def CompactDatabase(self, SrcName:str, DstName:str, DstLocale:object, Options:object, SrcLocale:object): # -> 
        """ CompactDatabase(self: DBEngineClass, SrcName: str, DstName: str, DstLocale: object, Options: object, SrcLocale: object) """
        ...

    def CreateDatabase(self, Name:str, Locale:str, Option:object) -> Database:
        """ CreateDatabase(self: DBEngineClass, Name: str, Locale: str, Option: object) -> Database """
        ...

    def CreateWorkspace(self, Name:str, UserName:str, Password:str, UseType:object) -> Workspace:
        """ CreateWorkspace(self: DBEngineClass, Name: str, UserName: str, Password: str, UseType: object) -> Workspace """
        ...

    def FreeLocks(self): # -> 
        """ FreeLocks(self: DBEngineClass) """
        ...

    def Idle(self, Action:object): # -> 
        """ Idle(self: DBEngineClass, Action: object) """
        ...

    def ISAMStats(self, StatNum:int, Reset:object) -> int:
        """ ISAMStats(self: DBEngineClass, StatNum: int, Reset: object) -> int """
        ...

    def OpenConnection(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Connection:
        """ OpenConnection(self: DBEngineClass, Name: str, Options: object, ReadOnly: object, Connect: object) -> Connection """
        ...

    def OpenDatabase(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Database:
        """ OpenDatabase(self: DBEngineClass, Name: str, Options: object, ReadOnly: object, Connect: object) -> Database """
        ...

    def RegisterDatabase(self, Dsn:str, Driver:str, Silent:bool, Attributes:str): # -> 
        """ RegisterDatabase(self: DBEngineClass, Dsn: str, Driver: str, Silent: bool, Attributes: str) """
        ...

    def RepairDatabase(self, Name:str): # -> 
        """ RepairDatabase(self: DBEngineClass, Name: str) """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: DBEngineClass) """
        ...

    def SetDataAccessOption(self, Option:Int16, Value:object): # -> 
        """ SetDataAccessOption(self: DBEngineClass, Option: Int16, Value: object) """
        ...

    def SetDefaultWorkspace(self, Name:str, Password:str): # -> 
        """ SetDefaultWorkspace(self: DBEngineClass, Name: str, Password: str) """
        ...

    def SetOption(self, Option:int, Value:object): # -> 
        """ SetOption(self: DBEngineClass, Option: int, Value: object) """
        ...

    def _30_CreateWorkspace(self, Name:str, UserName:str, Password:str) -> Workspace:
        """ _30_CreateWorkspace(self: DBEngineClass, Name: str, UserName: str, Password: str) -> Workspace """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Document(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllPermissions(self) -> int:
        """ Get: AllPermissions(self: Document) -> int """
        ...

    @property
    def Container(self) -> str:
        """ Get: Container(self: Document) -> str """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: Document) -> object """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: Document) -> object """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Document) -> str """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: Document) -> str
        Set: Owner(self: Document) = value
        """
        ...

    @property
    def Permissions(self) -> int:
        """
        Get: Permissions(self: Document) -> int
        Set: Permissions(self: Document) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: Document) -> str
        Set: UserName(self: Document) = value
        """
        ...


    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: Document, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...


class Documents(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DriverPromptEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DriverPromptEnum, values: dbDriverComplete (0), dbDriverCompleteRequired (3), dbDriverNoPrompt (1), dbDriverPrompt (2) """
    dbDriverComplete: DriverPromptEnum = ...
    dbDriverCompleteRequired: DriverPromptEnum = ...
    dbDriverNoPrompt: DriverPromptEnum = ...
    dbDriverPrompt: DriverPromptEnum = ...
    value__ = ...


class EditModeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EditModeEnum, values: dbEditAdd (2), dbEditInProgress (1), dbEditNone (0) """
    dbEditAdd: EditModeEnum = ...
    dbEditInProgress: EditModeEnum = ...
    dbEditNone: EditModeEnum = ...
    value__ = ...


class Error: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: Error) -> str """
        ...

    @property
    def HelpContext(self) -> int:
        """ Get: HelpContext(self: Error) -> int """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: Error) -> str """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: Error) -> int """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: Error) -> str """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Errors(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class _Field(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowZeroLength(self) -> bool:
        """
        Get: AllowZeroLength(self: _Field) -> bool
        Set: AllowZeroLength(self: _Field) = value
        """
        ...

    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: _Field) -> int
        Set: Attributes(self: _Field) = value
        """
        ...

    @property
    def CollatingOrder(self) -> int:
        """ Get: CollatingOrder(self: _Field) -> int """
        ...

    @property
    def CollectionIndex(self) -> Int16:
        """ Get: CollectionIndex(self: _Field) -> Int16 """
        ...

    @property
    def DataUpdatable(self) -> bool:
        """ Get: DataUpdatable(self: _Field) -> bool """
        ...

    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: _Field) -> object
        Set: DefaultValue(self: _Field) = value
        """
        ...

    @property
    def FieldSize(self) -> int:
        """ Get: FieldSize(self: _Field) -> int """
        ...

    @property
    def ForeignName(self) -> str:
        """
        Get: ForeignName(self: _Field) -> str
        Set: ForeignName(self: _Field) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Field) -> str
        Set: Name(self: _Field) = value
        """
        ...

    @property
    def OrdinalPosition(self) -> Int16:
        """
        Get: OrdinalPosition(self: _Field) -> Int16
        Set: OrdinalPosition(self: _Field) = value
        """
        ...

    @property
    def OriginalValue(self) -> object:
        """ Get: OriginalValue(self: _Field) -> object """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: _Field) -> bool
        Set: Required(self: _Field) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: _Field) -> int
        Set: Size(self: _Field) = value
        """
        ...

    @property
    def SourceField(self) -> str:
        """ Get: SourceField(self: _Field) -> str """
        ...

    @property
    def SourceTable(self) -> str:
        """ Get: SourceTable(self: _Field) -> str """
        ...

    @property
    def Type(self) -> Int16:
        """
        Get: Type(self: _Field) -> Int16
        Set: Type(self: _Field) = value
        """
        ...

    @property
    def ValidateOnSet(self) -> bool:
        """
        Get: ValidateOnSet(self: _Field) -> bool
        Set: ValidateOnSet(self: _Field) = value
        """
        ...

    @property
    def ValidationRule(self) -> str:
        """
        Get: ValidationRule(self: _Field) -> str
        Set: ValidationRule(self: _Field) = value
        """
        ...

    @property
    def ValidationText(self) -> str:
        """
        Get: ValidationText(self: _Field) -> str
        Set: ValidationText(self: _Field) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: _Field) -> object
        Set: Value(self: _Field) = value
        """
        ...

    @property
    def VisibleValue(self) -> object:
        """ Get: VisibleValue(self: _Field) -> object """
        ...


    def AppendChunk(self, Val:object): # -> 
        """ AppendChunk(self: _Field, Val: object) """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: _Field, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def GetChunk(self, Offset:int, Bytes:int) -> object:
        """ GetChunk(self: _Field, Offset: int, Bytes: int) -> object """
        ...

    def _30_FieldSize(self) -> int:
        """ _30_FieldSize(self: _Field) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Field(_Field): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class Field2(_Field): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    @property
    def AppendOnly(self) -> bool:
        """
        Get: AppendOnly(self: Field2) -> bool
        Set: AppendOnly(self: Field2) = value
        """
        ...

    @property
    def ComplexType(self) -> ComplexType:
        """ Get: ComplexType(self: Field2) -> ComplexType """
        ...

    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: Field2) -> str
        Set: Expression(self: Field2) = value
        """
        ...

    @property
    def IsComplex(self) -> bool:
        """ Get: IsComplex(self: Field2) -> bool """
        ...


    def LoadFromFile(self, FileName:str): # -> 
        """ LoadFromFile(self: Field2, FileName: str) """
        ...

    def SaveToFile(self, FileName:str): # -> 
        """ SaveToFile(self: Field2, FileName: str) """
        ...


class FieldAttributeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FieldAttributeEnum, values: dbAutoIncrField (16), dbDescending (1), dbFixedField (1), dbHyperlinkField (32768), dbSystemField (8192), dbUpdatableField (32), dbVariableField (2) """
    dbAutoIncrField: FieldAttributeEnum = ...
    dbDescending: FieldAttributeEnum = ...
    dbFixedField: FieldAttributeEnum = ...
    dbHyperlinkField: FieldAttributeEnum = ...
    dbSystemField: FieldAttributeEnum = ...
    dbUpdatableField: FieldAttributeEnum = ...
    dbVariableField: FieldAttributeEnum = ...
    value__ = ...


class FieldClass(Field, __ComObject): # skipped bases: <type '_Field'>, <type '_DAO'>, <type 'object'>
    """ FieldClass() """
    @property
    def AllowZeroLength(self) -> bool:
        """
        Get: AllowZeroLength(self: FieldClass) -> bool
        Set: AllowZeroLength(self: FieldClass) = value
        """
        ...

    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: FieldClass) -> int
        Set: Attributes(self: FieldClass) = value
        """
        ...

    @property
    def CollatingOrder(self) -> int:
        """ Get: CollatingOrder(self: FieldClass) -> int """
        ...

    @property
    def CollectionIndex(self) -> Int16:
        """ Get: CollectionIndex(self: FieldClass) -> Int16 """
        ...

    @property
    def DataUpdatable(self) -> bool:
        """ Get: DataUpdatable(self: FieldClass) -> bool """
        ...

    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: FieldClass) -> object
        Set: DefaultValue(self: FieldClass) = value
        """
        ...

    @property
    def FieldSize(self) -> int:
        """ Get: FieldSize(self: FieldClass) -> int """
        ...

    @property
    def ForeignName(self) -> str:
        """
        Get: ForeignName(self: FieldClass) -> str
        Set: ForeignName(self: FieldClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FieldClass) -> str
        Set: Name(self: FieldClass) = value
        """
        ...

    @property
    def OrdinalPosition(self) -> Int16:
        """
        Get: OrdinalPosition(self: FieldClass) -> Int16
        Set: OrdinalPosition(self: FieldClass) = value
        """
        ...

    @property
    def OriginalValue(self) -> object:
        """ Get: OriginalValue(self: FieldClass) -> object """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: FieldClass) -> Properties """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: FieldClass) -> bool
        Set: Required(self: FieldClass) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: FieldClass) -> int
        Set: Size(self: FieldClass) = value
        """
        ...

    @property
    def SourceField(self) -> str:
        """ Get: SourceField(self: FieldClass) -> str """
        ...

    @property
    def SourceTable(self) -> str:
        """ Get: SourceTable(self: FieldClass) -> str """
        ...

    @property
    def Type(self) -> Int16:
        """
        Get: Type(self: FieldClass) -> Int16
        Set: Type(self: FieldClass) = value
        """
        ...

    @property
    def ValidateOnSet(self) -> bool:
        """
        Get: ValidateOnSet(self: FieldClass) -> bool
        Set: ValidateOnSet(self: FieldClass) = value
        """
        ...

    @property
    def ValidationRule(self) -> str:
        """
        Get: ValidationRule(self: FieldClass) -> str
        Set: ValidationRule(self: FieldClass) = value
        """
        ...

    @property
    def ValidationText(self) -> str:
        """
        Get: ValidationText(self: FieldClass) -> str
        Set: ValidationText(self: FieldClass) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: FieldClass) -> object
        Set: Value(self: FieldClass) = value
        """
        ...

    @property
    def VisibleValue(self) -> object:
        """ Get: VisibleValue(self: FieldClass) -> object """
        ...


    def AppendChunk(self, Val:object): # -> 
        """ AppendChunk(self: FieldClass, Val: object) """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: FieldClass, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def GetChunk(self, Offset:int, Bytes:int) -> object:
        """ GetChunk(self: FieldClass, Offset: int, Bytes: int) -> object """
        ...

    def _30_FieldSize(self) -> int:
        """ _30_FieldSize(self: FieldClass) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class _DynaCollection(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Append(self, Object:object): # -> 
        """ Append(self: _DynaCollection, Object: object) """
        ...

    def Delete(self, Name:str): # -> 
        """ Delete(self: _DynaCollection, Name: str) """
        ...


class Fields(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class _Group(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Group) -> str
        Set: Name(self: _Group) = value
        """
        ...

    @property
    def PID(self): # -> 
        """ Set: PID(self: _Group) = value """
        ...

    @property
    def Users(self) -> Users:
        """ Get: Users(self: _Group) -> Users """
        ...


    def CreateUser(self, Name:object, PID:object, Password:object) -> User:
        """ CreateUser(self: _Group, Name: object, PID: object, Password: object) -> User """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Group(_Group): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class GroupClass(__ComObject, Group): # skipped bases: <type '_DAO'>, <type '_Group'>, <type 'object'>
    """ GroupClass() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: GroupClass) -> str
        Set: Name(self: GroupClass) = value
        """
        ...

    @property
    def PID(self): # -> 
        """ Set: PID(self: GroupClass) = value """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: GroupClass) -> Properties """
        ...

    @property
    def Users(self) -> Users:
        """ Get: Users(self: GroupClass) -> Users """
        ...


    def CreateUser(self, Name:object, PID:object, Password:object) -> User:
        """ CreateUser(self: GroupClass, Name: object, PID: object, Password: object) -> User """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Groups(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IdleEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IdleEnum, values: dbFreeLocks (1), dbRefreshCache (8) """
    dbFreeLocks: IdleEnum = ...
    dbRefreshCache: IdleEnum = ...
    value__ = ...


class _Index(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Clustered(self) -> bool:
        """
        Get: Clustered(self: _Index) -> bool
        Set: Clustered(self: _Index) = value
        """
        ...

    @property
    def DistinctCount(self) -> int:
        """ Get: DistinctCount(self: _Index) -> int """
        ...

    @property
    def Fields(self) -> object:
        """
        Get: Fields(self: _Index) -> object
        Set: Fields(self: _Index) = value
        """
        ...

    @property
    def Foreign(self) -> bool:
        """ Get: Foreign(self: _Index) -> bool """
        ...

    @property
    def IgnoreNulls(self) -> bool:
        """
        Get: IgnoreNulls(self: _Index) -> bool
        Set: IgnoreNulls(self: _Index) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Index) -> str
        Set: Name(self: _Index) = value
        """
        ...

    @property
    def Primary(self) -> bool:
        """
        Get: Primary(self: _Index) -> bool
        Set: Primary(self: _Index) = value
        """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: _Index) -> bool
        Set: Required(self: _Index) = value
        """
        ...

    @property
    def Unique(self) -> bool:
        """
        Get: Unique(self: _Index) -> bool
        Set: Unique(self: _Index) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: _Index, Name: object, Type: object, Size: object) -> Field """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: _Index, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...


class Index(_Index): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class IndexClass(__ComObject, Index): # skipped bases: <type '_DAO'>, <type '_Index'>, <type 'object'>
    """ IndexClass() """
    @property
    def Clustered(self) -> bool:
        """
        Get: Clustered(self: IndexClass) -> bool
        Set: Clustered(self: IndexClass) = value
        """
        ...

    @property
    def DistinctCount(self) -> int:
        """ Get: DistinctCount(self: IndexClass) -> int """
        ...

    @property
    def Fields(self) -> object:
        """
        Get: Fields(self: IndexClass) -> object
        Set: Fields(self: IndexClass) = value
        """
        ...

    @property
    def Foreign(self) -> bool:
        """ Get: Foreign(self: IndexClass) -> bool """
        ...

    @property
    def IgnoreNulls(self) -> bool:
        """
        Get: IgnoreNulls(self: IndexClass) -> bool
        Set: IgnoreNulls(self: IndexClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IndexClass) -> str
        Set: Name(self: IndexClass) = value
        """
        ...

    @property
    def Primary(self) -> bool:
        """
        Get: Primary(self: IndexClass) -> bool
        Set: Primary(self: IndexClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: IndexClass) -> Properties """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: IndexClass) -> bool
        Set: Required(self: IndexClass) = value
        """
        ...

    @property
    def Unique(self) -> bool:
        """
        Get: Unique(self: IndexClass) -> bool
        Set: Unique(self: IndexClass) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: IndexClass, Name: object, Type: object, Size: object) -> Field """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: IndexClass, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...


class Indexes(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IndexFields(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class LanguageConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dbLangArabic: str = ...
    dbLangChineseSimplified: str = ...
    dbLangChineseTraditional: str = ...
    dbLangCyrillic: str = ...
    dbLangCzech: str = ...
    dbLangDutch: str = ...
    dbLangGeneral: str = ...
    dbLangGreek: str = ...
    dbLangHebrew: str = ...
    dbLangHindi: str = ...
    dbLangHungarian: str = ...
    dbLangIcelandic: str = ...
    dbLangJapanese: str = ...
    dbLangJapaneseRadicalStrokeCount: str = ...
    dbLangKorean: str = ...
    dbLangNordic: str = ...
    dbLangNorwDan: str = ...
    dbLangPolish: str = ...
    dbLangSlovenian: str = ...
    dbLangSpanish: str = ...
    dbLangSwedFin: str = ...
    dbLangThai: str = ...
    dbLangTurkish: str = ...


class LockTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LockTypeEnum, values: dbOptimistic (3), dbOptimisticBatch (5), dbOptimisticValue (1), dbPessimistic (2) """
    dbOptimistic: LockTypeEnum = ...
    dbOptimisticBatch: LockTypeEnum = ...
    dbOptimisticValue: LockTypeEnum = ...
    dbPessimistic: LockTypeEnum = ...
    value__ = ...


class Parameter(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Direction(self) -> Int16:
        """
        Get: Direction(self: Parameter) -> Int16
        Set: Direction(self: Parameter) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Parameter) -> str """
        ...

    @property
    def Type(self) -> Int16:
        """
        Get: Type(self: Parameter) -> Int16
        Set: Type(self: Parameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: Parameter) -> object
        Set: Value(self: Parameter) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ParameterDirectionEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParameterDirectionEnum, values: dbParamInput (1), dbParamInputOutput (3), dbParamOutput (2), dbParamReturnValue (4) """
    dbParamInput: ParameterDirectionEnum = ...
    dbParamInputOutput: ParameterDirectionEnum = ...
    dbParamOutput: ParameterDirectionEnum = ...
    dbParamReturnValue: ParameterDirectionEnum = ...
    value__ = ...


class Parameters(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PermissionEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PermissionEnum, values: dbSecCreate (1), dbSecDBAdmin (8), dbSecDBCreate (1), dbSecDBExclusive (4), dbSecDBOpen (2), dbSecDelete (65536), dbSecDeleteData (128), dbSecFullAccess (1048575), dbSecInsertData (32), dbSecNoAccess (0), dbSecReadDef (4), dbSecReadSec (131072), dbSecReplaceData (64), dbSecRetrieveData (20), dbSecWriteDef (65548), dbSecWriteOwner (524288), dbSecWriteSec (262144) """
    dbSecCreate: PermissionEnum = ...
    dbSecDBAdmin: PermissionEnum = ...
    dbSecDBCreate: PermissionEnum = ...
    dbSecDBExclusive: PermissionEnum = ...
    dbSecDBOpen: PermissionEnum = ...
    dbSecDelete: PermissionEnum = ...
    dbSecDeleteData: PermissionEnum = ...
    dbSecFullAccess: PermissionEnum = ...
    dbSecInsertData: PermissionEnum = ...
    dbSecNoAccess: PermissionEnum = ...
    dbSecReadDef: PermissionEnum = ...
    dbSecReadSec: PermissionEnum = ...
    dbSecReplaceData: PermissionEnum = ...
    dbSecRetrieveData: PermissionEnum = ...
    dbSecWriteDef: PermissionEnum = ...
    dbSecWriteOwner: PermissionEnum = ...
    dbSecWriteSec: PermissionEnum = ...
    value__ = ...


class PrivDBEngine(_DBEngine): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class PrivDBEngineClass(PrivDBEngine, __ComObject): # skipped bases: <type '_DBEngine'>, <type '_DAO'>, <type 'object'>
    """ PrivDBEngineClass() """
    @property
    def DefaultPassword(self): # -> 
        """ Set: DefaultPassword(self: PrivDBEngineClass) = value """
        ...

    @property
    def DefaultType(self) -> int:
        """
        Get: DefaultType(self: PrivDBEngineClass) -> int
        Set: DefaultType(self: PrivDBEngineClass) = value
        """
        ...

    @property
    def DefaultUser(self): # -> 
        """ Set: DefaultUser(self: PrivDBEngineClass) = value """
        ...

    @property
    def Errors(self) -> Errors:
        """ Get: Errors(self: PrivDBEngineClass) -> Errors """
        ...

    @property
    def IniPath(self) -> str:
        """
        Get: IniPath(self: PrivDBEngineClass) -> str
        Set: IniPath(self: PrivDBEngineClass) = value
        """
        ...

    @property
    def LoginTimeout(self) -> Int16:
        """
        Get: LoginTimeout(self: PrivDBEngineClass) -> Int16
        Set: LoginTimeout(self: PrivDBEngineClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: PrivDBEngineClass) -> Properties """
        ...

    @property
    def SystemDB(self) -> str:
        """
        Get: SystemDB(self: PrivDBEngineClass) -> str
        Set: SystemDB(self: PrivDBEngineClass) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: PrivDBEngineClass) -> str """
        ...

    @property
    def Workspaces(self) -> Workspaces:
        """ Get: Workspaces(self: PrivDBEngineClass) -> Workspaces """
        ...


    def BeginTrans(self): # -> 
        """ BeginTrans(self: PrivDBEngineClass) """
        ...

    def CommitTrans(self, Option:int): # -> 
        """ CommitTrans(self: PrivDBEngineClass, Option: int) """
        ...

    def CompactDatabase(self, SrcName:str, DstName:str, DstLocale:object, Options:object, SrcLocale:object): # -> 
        """ CompactDatabase(self: PrivDBEngineClass, SrcName: str, DstName: str, DstLocale: object, Options: object, SrcLocale: object) """
        ...

    def CreateDatabase(self, Name:str, Locale:str, Option:object) -> Database:
        """ CreateDatabase(self: PrivDBEngineClass, Name: str, Locale: str, Option: object) -> Database """
        ...

    def CreateWorkspace(self, Name:str, UserName:str, Password:str, UseType:object) -> Workspace:
        """ CreateWorkspace(self: PrivDBEngineClass, Name: str, UserName: str, Password: str, UseType: object) -> Workspace """
        ...

    def FreeLocks(self): # -> 
        """ FreeLocks(self: PrivDBEngineClass) """
        ...

    def Idle(self, Action:object): # -> 
        """ Idle(self: PrivDBEngineClass, Action: object) """
        ...

    def ISAMStats(self, StatNum:int, Reset:object) -> int:
        """ ISAMStats(self: PrivDBEngineClass, StatNum: int, Reset: object) -> int """
        ...

    def OpenConnection(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Connection:
        """ OpenConnection(self: PrivDBEngineClass, Name: str, Options: object, ReadOnly: object, Connect: object) -> Connection """
        ...

    def OpenDatabase(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Database:
        """ OpenDatabase(self: PrivDBEngineClass, Name: str, Options: object, ReadOnly: object, Connect: object) -> Database """
        ...

    def RegisterDatabase(self, Dsn:str, Driver:str, Silent:bool, Attributes:str): # -> 
        """ RegisterDatabase(self: PrivDBEngineClass, Dsn: str, Driver: str, Silent: bool, Attributes: str) """
        ...

    def RepairDatabase(self, Name:str): # -> 
        """ RepairDatabase(self: PrivDBEngineClass, Name: str) """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: PrivDBEngineClass) """
        ...

    def SetDataAccessOption(self, Option:Int16, Value:object): # -> 
        """ SetDataAccessOption(self: PrivDBEngineClass, Option: Int16, Value: object) """
        ...

    def SetDefaultWorkspace(self, Name:str, Password:str): # -> 
        """ SetDefaultWorkspace(self: PrivDBEngineClass, Name: str, Password: str) """
        ...

    def SetOption(self, Option:int, Value:object): # -> 
        """ SetOption(self: PrivDBEngineClass, Option: int, Value: object) """
        ...

    def _30_CreateWorkspace(self, Name:str, UserName:str, Password:str) -> Workspace:
        """ _30_CreateWorkspace(self: PrivDBEngineClass, Name: str, UserName: str, Password: str) -> Workspace """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Properties(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Property(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Inherited(self) -> bool:
        """ Get: Inherited(self: Property) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Property) -> str
        Set: Name(self: Property) = value
        """
        ...

    @property
    def Type(self) -> Int16:
        """
        Get: Type(self: Property) -> Int16
        Set: Type(self: Property) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: Property) -> object
        Set: Value(self: Property) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class _QueryDef(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheSize(self) -> int:
        """
        Get: CacheSize(self: _QueryDef) -> int
        Set: CacheSize(self: _QueryDef) = value
        """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: _QueryDef) -> str
        Set: Connect(self: _QueryDef) = value
        """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: _QueryDef) -> object """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: _QueryDef) -> Fields """
        ...

    @property
    def hStmt(self) -> int:
        """ Get: hStmt(self: _QueryDef) -> int """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: _QueryDef) -> object """
        ...

    @property
    def MaxRecords(self) -> int:
        """
        Get: MaxRecords(self: _QueryDef) -> int
        Set: MaxRecords(self: _QueryDef) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _QueryDef) -> str
        Set: Name(self: _QueryDef) = value
        """
        ...

    @property
    def ODBCTimeout(self) -> Int16:
        """
        Get: ODBCTimeout(self: _QueryDef) -> Int16
        Set: ODBCTimeout(self: _QueryDef) = value
        """
        ...

    @property
    def Parameters(self) -> Parameters:
        """ Get: Parameters(self: _QueryDef) -> Parameters """
        ...

    @property
    def Prepare(self) -> object:
        """
        Get: Prepare(self: _QueryDef) -> object
        Set: Prepare(self: _QueryDef) = value
        """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: _QueryDef) -> int """
        ...

    @property
    def ReturnsRecords(self) -> bool:
        """
        Get: ReturnsRecords(self: _QueryDef) -> bool
        Set: ReturnsRecords(self: _QueryDef) = value
        """
        ...

    @property
    def SQL(self) -> str:
        """
        Get: SQL(self: _QueryDef) -> str
        Set: SQL(self: _QueryDef) = value
        """
        ...

    @property
    def StillExecuting(self) -> bool:
        """ Get: StillExecuting(self: _QueryDef) -> bool """
        ...

    @property
    def Type(self) -> Int16:
        """ Get: Type(self: _QueryDef) -> Int16 """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: _QueryDef) -> bool """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: _QueryDef) """
        ...

    def Close(self): # -> 
        """ Close(self: _QueryDef) """
        ...

    def Compare(self, pQdef:QueryDef, lps:Int16) -> Int16:
        """ Compare(self: _QueryDef, pQdef: QueryDef, lps: Int16) -> Int16 """
        ...

    def CreateDynaset(self, Options:object, Inconsistent:object) -> Recordset:
        """ CreateDynaset(self: _QueryDef, Options: object, Inconsistent: object) -> Recordset """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: _QueryDef, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def CreateSnapshot(self, Options:object) -> Recordset:
        """ CreateSnapshot(self: _QueryDef, Options: object) -> Recordset """
        ...

    def Execute(self, Options:object): # -> 
        """ Execute(self: _QueryDef, Options: object) """
        ...

    def ListParameters(self) -> Recordset:
        """ ListParameters(self: _QueryDef) -> Recordset """
        ...

    def OpenRecordset(self, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ OpenRecordset(self: _QueryDef, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def _30_OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ _30_OpenRecordset(self: _QueryDef, Type: object, Options: object) -> Recordset """
        ...

    def _30__OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ _30__OpenRecordset(self: _QueryDef, Type: object, Options: object) -> Recordset """
        ...

    def _Copy(self) -> QueryDef:
        """ _Copy(self: _QueryDef) -> QueryDef """
        ...

    def _OpenRecordset(self, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ _OpenRecordset(self: _QueryDef, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class QueryDef(_QueryDef): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class QueryDefClass(QueryDef, __ComObject): # skipped bases: <type '_QueryDef'>, <type '_DAO'>, <type 'object'>
    """ QueryDefClass() """
    @property
    def CacheSize(self) -> int:
        """
        Get: CacheSize(self: QueryDefClass) -> int
        Set: CacheSize(self: QueryDefClass) = value
        """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: QueryDefClass) -> str
        Set: Connect(self: QueryDefClass) = value
        """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: QueryDefClass) -> object """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: QueryDefClass) -> Fields """
        ...

    @property
    def hStmt(self) -> int:
        """ Get: hStmt(self: QueryDefClass) -> int """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: QueryDefClass) -> object """
        ...

    @property
    def MaxRecords(self) -> int:
        """
        Get: MaxRecords(self: QueryDefClass) -> int
        Set: MaxRecords(self: QueryDefClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: QueryDefClass) -> str
        Set: Name(self: QueryDefClass) = value
        """
        ...

    @property
    def ODBCTimeout(self) -> Int16:
        """
        Get: ODBCTimeout(self: QueryDefClass) -> Int16
        Set: ODBCTimeout(self: QueryDefClass) = value
        """
        ...

    @property
    def Parameters(self) -> Parameters:
        """ Get: Parameters(self: QueryDefClass) -> Parameters """
        ...

    @property
    def Prepare(self) -> object:
        """
        Get: Prepare(self: QueryDefClass) -> object
        Set: Prepare(self: QueryDefClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: QueryDefClass) -> Properties """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: QueryDefClass) -> int """
        ...

    @property
    def ReturnsRecords(self) -> bool:
        """
        Get: ReturnsRecords(self: QueryDefClass) -> bool
        Set: ReturnsRecords(self: QueryDefClass) = value
        """
        ...

    @property
    def SQL(self) -> str:
        """
        Get: SQL(self: QueryDefClass) -> str
        Set: SQL(self: QueryDefClass) = value
        """
        ...

    @property
    def StillExecuting(self) -> bool:
        """ Get: StillExecuting(self: QueryDefClass) -> bool """
        ...

    @property
    def Type(self) -> Int16:
        """ Get: Type(self: QueryDefClass) -> Int16 """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: QueryDefClass) -> bool """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: QueryDefClass) """
        ...

    def Close(self): # -> 
        """ Close(self: QueryDefClass) """
        ...

    def Compare(self, pQdef:QueryDef, lps:Int16) -> Int16:
        """ Compare(self: QueryDefClass, pQdef: QueryDef, lps: Int16) -> Int16 """
        ...

    def CreateDynaset(self, Options:object, Inconsistent:object) -> Recordset:
        """ CreateDynaset(self: QueryDefClass, Options: object, Inconsistent: object) -> Recordset """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: QueryDefClass, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def CreateSnapshot(self, Options:object) -> Recordset:
        """ CreateSnapshot(self: QueryDefClass, Options: object) -> Recordset """
        ...

    def Execute(self, Options:object): # -> 
        """ Execute(self: QueryDefClass, Options: object) """
        ...

    def ListParameters(self) -> Recordset:
        """ ListParameters(self: QueryDefClass) -> Recordset """
        ...

    def OpenRecordset(self, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ OpenRecordset(self: QueryDefClass, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def _30_OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ _30_OpenRecordset(self: QueryDefClass, Type: object, Options: object) -> Recordset """
        ...

    def _30__OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ _30__OpenRecordset(self: QueryDefClass, Type: object, Options: object) -> Recordset """
        ...

    def _Copy(self) -> QueryDef:
        """ _Copy(self: QueryDefClass) -> QueryDef """
        ...

    def _OpenRecordset(self, Type:object, Options:object, LockEdit:object) -> Recordset:
        """ _OpenRecordset(self: QueryDefClass, Type: object, Options: object, LockEdit: object) -> Recordset """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class QueryDefs(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class QueryDefStateEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueryDefStateEnum, values: dbQPrepare (1), dbQUnprepare (2) """
    dbQPrepare: QueryDefStateEnum = ...
    dbQUnprepare: QueryDefStateEnum = ...
    value__ = ...


class QueryDefTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueryDefTypeEnum, values: dbQAction (240), dbQAppend (64), dbQCompound (160), dbQCrosstab (16), dbQDDL (96), dbQDelete (32), dbQMakeTable (80), dbQProcedure (224), dbQSelect (0), dbQSetOperation (128), dbQSPTBulk (144), dbQSQLPassThrough (112), dbQUpdate (48) """
    dbQAction: QueryDefTypeEnum = ...
    dbQAppend: QueryDefTypeEnum = ...
    dbQCompound: QueryDefTypeEnum = ...
    dbQCrosstab: QueryDefTypeEnum = ...
    dbQDDL: QueryDefTypeEnum = ...
    dbQDelete: QueryDefTypeEnum = ...
    dbQMakeTable: QueryDefTypeEnum = ...
    dbQProcedure: QueryDefTypeEnum = ...
    dbQSelect: QueryDefTypeEnum = ...
    dbQSetOperation: QueryDefTypeEnum = ...
    dbQSPTBulk: QueryDefTypeEnum = ...
    dbQSQLPassThrough: QueryDefTypeEnum = ...
    dbQUpdate: QueryDefTypeEnum = ...
    value__ = ...


class Recordset(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AbsolutePosition(self) -> int:
        """
        Get: AbsolutePosition(self: Recordset) -> int
        Set: AbsolutePosition(self: Recordset) = value
        """
        ...

    @property
    def BatchCollisionCount(self) -> int:
        """ Get: BatchCollisionCount(self: Recordset) -> int """
        ...

    @property
    def BatchCollisions(self) -> object:
        """ Get: BatchCollisions(self: Recordset) -> object """
        ...

    @property
    def BatchSize(self) -> int:
        """
        Get: BatchSize(self: Recordset) -> int
        Set: BatchSize(self: Recordset) = value
        """
        ...

    @property
    def BOF(self) -> bool:
        """ Get: BOF(self: Recordset) -> bool """
        ...

    @property
    def Bookmark(self) -> Array:
        """
        Get: Bookmark(self: Recordset) -> Array
        Set: Bookmark(self: Recordset) = value
        """
        ...

    @property
    def Bookmarkable(self) -> bool:
        """ Get: Bookmarkable(self: Recordset) -> bool """
        ...

    @property
    def CacheSize(self) -> int:
        """
        Get: CacheSize(self: Recordset) -> int
        Set: CacheSize(self: Recordset) = value
        """
        ...

    @property
    def CacheStart(self) -> Array:
        """
        Get: CacheStart(self: Recordset) -> Array
        Set: CacheStart(self: Recordset) = value
        """
        ...

    @property
    def Connection(self) -> Connection:
        """
        Get: Connection(self: Recordset) -> Connection
        Set: Connection(self: Recordset) = value
        """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: Recordset) -> object """
        ...

    @property
    def EditMode(self) -> Int16:
        """ Get: EditMode(self: Recordset) -> Int16 """
        ...

    @property
    def EOF(self) -> bool:
        """ Get: EOF(self: Recordset) -> bool """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: Recordset) -> Fields """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: Recordset) -> str
        Set: Filter(self: Recordset) = value
        """
        ...

    @property
    def hStmt(self) -> int:
        """ Get: hStmt(self: Recordset) -> int """
        ...

    @property
    def Index(self) -> str:
        """
        Get: Index(self: Recordset) -> str
        Set: Index(self: Recordset) = value
        """
        ...

    @property
    def Indexes(self) -> Indexes:
        """ Get: Indexes(self: Recordset) -> Indexes """
        ...

    @property
    def LastModified(self) -> Array:
        """ Get: LastModified(self: Recordset) -> Array """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: Recordset) -> object """
        ...

    @property
    def LockEdits(self) -> bool:
        """
        Get: LockEdits(self: Recordset) -> bool
        Set: LockEdits(self: Recordset) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Recordset) -> str """
        ...

    @property
    def NoMatch(self) -> bool:
        """ Get: NoMatch(self: Recordset) -> bool """
        ...

    @property
    def ODBCFetchCount(self) -> int:
        """ Get: ODBCFetchCount(self: Recordset) -> int """
        ...

    @property
    def ODBCFetchDelay(self) -> int:
        """ Get: ODBCFetchDelay(self: Recordset) -> int """
        ...

    @property
    def Parent(self) -> Database:
        """ Get: Parent(self: Recordset) -> Database """
        ...

    @property
    def PercentPosition(self) -> Single:
        """
        Get: PercentPosition(self: Recordset) -> Single
        Set: PercentPosition(self: Recordset) = value
        """
        ...

    @property
    def RecordCount(self) -> int:
        """ Get: RecordCount(self: Recordset) -> int """
        ...

    @property
    def RecordStatus(self) -> Int16:
        """ Get: RecordStatus(self: Recordset) -> Int16 """
        ...

    @property
    def Restartable(self) -> bool:
        """ Get: Restartable(self: Recordset) -> bool """
        ...

    @property
    def Sort(self) -> str:
        """
        Get: Sort(self: Recordset) -> str
        Set: Sort(self: Recordset) = value
        """
        ...

    @property
    def StillExecuting(self) -> bool:
        """ Get: StillExecuting(self: Recordset) -> bool """
        ...

    @property
    def Transactions(self) -> bool:
        """ Get: Transactions(self: Recordset) -> bool """
        ...

    @property
    def Type(self) -> Int16:
        """ Get: Type(self: Recordset) -> Int16 """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: Recordset) -> bool """
        ...

    @property
    def UpdateOptions(self) -> int:
        """
        Get: UpdateOptions(self: Recordset) -> int
        Set: UpdateOptions(self: Recordset) = value
        """
        ...

    @property
    def ValidationRule(self) -> str:
        """ Get: ValidationRule(self: Recordset) -> str """
        ...

    @property
    def ValidationText(self) -> str:
        """ Get: ValidationText(self: Recordset) -> str """
        ...


    def AddNew(self): # -> 
        """ AddNew(self: Recordset) """
        ...

    def Cancel(self): # -> 
        """ Cancel(self: Recordset) """
        ...

    def CancelUpdate(self, UpdateType:int): # -> 
        """ CancelUpdate(self: Recordset, UpdateType: int) """
        ...

    def Clone(self) -> Recordset:
        """ Clone(self: Recordset) -> Recordset """
        ...

    def Close(self): # -> 
        """ Close(self: Recordset) """
        ...

    def CopyQueryDef(self) -> QueryDef:
        """ CopyQueryDef(self: Recordset) -> QueryDef """
        ...

    def CreateDynaset(self, Options:object, Inconsistent:object) -> Recordset:
        """ CreateDynaset(self: Recordset, Options: object, Inconsistent: object) -> Recordset """
        ...

    def CreateSnapshot(self, Options:object) -> Recordset:
        """ CreateSnapshot(self: Recordset, Options: object) -> Recordset """
        ...

    def Delete(self): # -> 
        """ Delete(self: Recordset) """
        ...

    def Edit(self): # -> 
        """ Edit(self: Recordset) """
        ...

    def FillCache(self, Rows:object, StartBookmark:object): # -> 
        """ FillCache(self: Recordset, Rows: object, StartBookmark: object) """
        ...

    def FindFirst(self, Criteria:str): # -> 
        """ FindFirst(self: Recordset, Criteria: str) """
        ...

    def FindLast(self, Criteria:str): # -> 
        """ FindLast(self: Recordset, Criteria: str) """
        ...

    def FindNext(self, Criteria:str): # -> 
        """ FindNext(self: Recordset, Criteria: str) """
        ...

    def FindPrevious(self, Criteria:str): # -> 
        """ FindPrevious(self: Recordset, Criteria: str) """
        ...

    def GetRows(self, NumRows:object) -> object:
        """ GetRows(self: Recordset, NumRows: object) -> object """
        ...

    def ListFields(self) -> Recordset:
        """ ListFields(self: Recordset) -> Recordset """
        ...

    def ListIndexes(self) -> Recordset:
        """ ListIndexes(self: Recordset) -> Recordset """
        ...

    def Move(self, Rows:int, StartBookmark:object): # -> 
        """ Move(self: Recordset, Rows: int, StartBookmark: object) """
        ...

    def MoveFirst(self): # -> 
        """ MoveFirst(self: Recordset) """
        ...

    def MoveLast(self, Options:int): # -> 
        """ MoveLast(self: Recordset, Options: int) """
        ...

    def MoveNext(self): # -> 
        """ MoveNext(self: Recordset) """
        ...

    def MovePrevious(self): # -> 
        """ MovePrevious(self: Recordset) """
        ...

    def NextRecordset(self) -> bool:
        """ NextRecordset(self: Recordset) -> bool """
        ...

    def OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ OpenRecordset(self: Recordset, Type: object, Options: object) -> Recordset """
        ...

    def Requery(self, NewQueryDef:object): # -> 
        """ Requery(self: Recordset, NewQueryDef: object) """
        ...

    def Seek(self, Comparison:str, Key1:object, Key2:object, Key3:object, Key4:object, Key5:object, Key6:object, Key7:object, Key8:object, Key9:object, Key10:object, Key11:object, Key12:object, Key13:object): # -> 
        """ Seek(self: Recordset, Comparison: str, Key1: object, Key2: object, Key3: object, Key4: object, Key5: object, Key6: object, Key7: object, Key8: object, Key9: object, Key10: object, Key11: object, Key12: object, Key13: object) """
        ...

    def Update(self, UpdateType:int, Force:bool): # -> 
        """ Update(self: Recordset, UpdateType: int, Force: bool) """
        ...

    def _30_CancelUpdate(self): # -> 
        """ _30_CancelUpdate(self: Recordset) """
        ...

    def _30_MoveLast(self): # -> 
        """ _30_MoveLast(self: Recordset) """
        ...

    def _30_Update(self): # -> 
        """ _30_Update(self: Recordset) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Recordset2(Recordset): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    @property
    def ParentRecordset(self) -> Recordset:
        """ Get: ParentRecordset(self: Recordset2) -> Recordset """
        ...



class RecordsetOptionEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecordsetOptionEnum, values: dbAppendOnly (8), dbConsistent (32), dbDenyRead (2), dbDenyWrite (1), dbExecDirect (2048), dbFailOnError (128), dbForwardOnly (256), dbInconsistent (16), dbReadOnly (4), dbRunAsync (1024), dbSeeChanges (512), dbSQLPassThrough (64) """
    dbAppendOnly: RecordsetOptionEnum = ...
    dbConsistent: RecordsetOptionEnum = ...
    dbDenyRead: RecordsetOptionEnum = ...
    dbDenyWrite: RecordsetOptionEnum = ...
    dbExecDirect: RecordsetOptionEnum = ...
    dbFailOnError: RecordsetOptionEnum = ...
    dbForwardOnly: RecordsetOptionEnum = ...
    dbInconsistent: RecordsetOptionEnum = ...
    dbReadOnly: RecordsetOptionEnum = ...
    dbRunAsync: RecordsetOptionEnum = ...
    dbSeeChanges: RecordsetOptionEnum = ...
    dbSQLPassThrough: RecordsetOptionEnum = ...
    value__ = ...


class Recordsets(_Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RecordsetTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecordsetTypeEnum, values: dbOpenDynamic (16), dbOpenDynaset (2), dbOpenForwardOnly (8), dbOpenSnapshot (4), dbOpenTable (1) """
    dbOpenDynamic: RecordsetTypeEnum = ...
    dbOpenDynaset: RecordsetTypeEnum = ...
    dbOpenForwardOnly: RecordsetTypeEnum = ...
    dbOpenSnapshot: RecordsetTypeEnum = ...
    dbOpenTable: RecordsetTypeEnum = ...
    value__ = ...


class RecordStatusEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecordStatusEnum, values: dbRecordDBDeleted (4), dbRecordDeleted (3), dbRecordModified (1), dbRecordNew (2), dbRecordUnmodified (0) """
    dbRecordDBDeleted: RecordStatusEnum = ...
    dbRecordDeleted: RecordStatusEnum = ...
    dbRecordModified: RecordStatusEnum = ...
    dbRecordNew: RecordStatusEnum = ...
    dbRecordUnmodified: RecordStatusEnum = ...
    value__ = ...


class _Relation(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: _Relation) -> int
        Set: Attributes(self: _Relation) = value
        """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: _Relation) -> Fields """
        ...

    @property
    def ForeignTable(self) -> str:
        """
        Get: ForeignTable(self: _Relation) -> str
        Set: ForeignTable(self: _Relation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Relation) -> str
        Set: Name(self: _Relation) = value
        """
        ...

    @property
    def PartialReplica(self) -> bool:
        """
        Get: PartialReplica(self: _Relation) -> bool
        Set: PartialReplica(self: _Relation) = value
        """
        ...

    @property
    def Table(self) -> str:
        """
        Get: Table(self: _Relation) -> str
        Set: Table(self: _Relation) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: _Relation, Name: object, Type: object, Size: object) -> Field """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Relation(_Relation): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class RelationAttributeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RelationAttributeEnum, values: dbRelationDeleteCascade (4096), dbRelationDontEnforce (2), dbRelationInherited (4), dbRelationLeft (16777216), dbRelationRight (33554432), dbRelationUnique (1), dbRelationUpdateCascade (256) """
    dbRelationDeleteCascade: RelationAttributeEnum = ...
    dbRelationDontEnforce: RelationAttributeEnum = ...
    dbRelationInherited: RelationAttributeEnum = ...
    dbRelationLeft: RelationAttributeEnum = ...
    dbRelationRight: RelationAttributeEnum = ...
    dbRelationUnique: RelationAttributeEnum = ...
    dbRelationUpdateCascade: RelationAttributeEnum = ...
    value__ = ...


class RelationClass(__ComObject, Relation): # skipped bases: <type '_DAO'>, <type '_Relation'>, <type 'object'>
    """ RelationClass() """
    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: RelationClass) -> int
        Set: Attributes(self: RelationClass) = value
        """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: RelationClass) -> Fields """
        ...

    @property
    def ForeignTable(self) -> str:
        """
        Get: ForeignTable(self: RelationClass) -> str
        Set: ForeignTable(self: RelationClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RelationClass) -> str
        Set: Name(self: RelationClass) = value
        """
        ...

    @property
    def PartialReplica(self) -> bool:
        """
        Get: PartialReplica(self: RelationClass) -> bool
        Set: PartialReplica(self: RelationClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: RelationClass) -> Properties """
        ...

    @property
    def Table(self) -> str:
        """
        Get: Table(self: RelationClass) -> str
        Set: Table(self: RelationClass) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: RelationClass, Name: object, Type: object, Size: object) -> Field """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Relations(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicaTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReplicaTypeEnum, values: dbRepMakePartial (1), dbRepMakeReadOnly (2) """
    dbRepMakePartial: ReplicaTypeEnum = ...
    dbRepMakeReadOnly: ReplicaTypeEnum = ...
    value__ = ...


class SetOptionEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SetOptionEnum, values: dbExclusiveAsyncDelay (60), dbFlushTransactionTimeout (66), dbImplicitCommitSync (59), dbLockDelay (63), dbLockRetry (57), dbMaxBufferSize (8), dbMaxLocksPerFile (62), dbPageTimeout (6), dbPasswordEncryptionAlgorithm (81), dbPasswordEncryptionKeyLength (82), dbPasswordEncryptionProvider (80), dbRecycleLVs (65), dbSharedAsyncDelay (61), dbUserCommitSync (58) """
    dbExclusiveAsyncDelay: SetOptionEnum = ...
    dbFlushTransactionTimeout: SetOptionEnum = ...
    dbImplicitCommitSync: SetOptionEnum = ...
    dbLockDelay: SetOptionEnum = ...
    dbLockRetry: SetOptionEnum = ...
    dbMaxBufferSize: SetOptionEnum = ...
    dbMaxLocksPerFile: SetOptionEnum = ...
    dbPageTimeout: SetOptionEnum = ...
    dbPasswordEncryptionAlgorithm: SetOptionEnum = ...
    dbPasswordEncryptionKeyLength: SetOptionEnum = ...
    dbPasswordEncryptionProvider: SetOptionEnum = ...
    dbRecycleLVs: SetOptionEnum = ...
    dbSharedAsyncDelay: SetOptionEnum = ...
    dbUserCommitSync: SetOptionEnum = ...
    value__ = ...


class SynchronizeTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynchronizeTypeEnum, values: dbRepExportChanges (1), dbRepImpExpChanges (4), dbRepImportChanges (2), dbRepSyncInternet (16) """
    dbRepExportChanges: SynchronizeTypeEnum = ...
    dbRepImpExpChanges: SynchronizeTypeEnum = ...
    dbRepImportChanges: SynchronizeTypeEnum = ...
    dbRepSyncInternet: SynchronizeTypeEnum = ...
    value__ = ...


class _TableDef(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: _TableDef) -> int
        Set: Attributes(self: _TableDef) = value
        """
        ...

    @property
    def ConflictTable(self) -> str:
        """ Get: ConflictTable(self: _TableDef) -> str """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: _TableDef) -> str
        Set: Connect(self: _TableDef) = value
        """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: _TableDef) -> object """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: _TableDef) -> Fields """
        ...

    @property
    def Indexes(self) -> Indexes:
        """ Get: Indexes(self: _TableDef) -> Indexes """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: _TableDef) -> object """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _TableDef) -> str
        Set: Name(self: _TableDef) = value
        """
        ...

    @property
    def RecordCount(self) -> int:
        """ Get: RecordCount(self: _TableDef) -> int """
        ...

    @property
    def ReplicaFilter(self) -> object:
        """
        Get: ReplicaFilter(self: _TableDef) -> object
        Set: ReplicaFilter(self: _TableDef) = value
        """
        ...

    @property
    def SourceTableName(self) -> str:
        """
        Get: SourceTableName(self: _TableDef) -> str
        Set: SourceTableName(self: _TableDef) = value
        """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: _TableDef) -> bool """
        ...

    @property
    def ValidationRule(self) -> str:
        """
        Get: ValidationRule(self: _TableDef) -> str
        Set: ValidationRule(self: _TableDef) = value
        """
        ...

    @property
    def ValidationText(self) -> str:
        """
        Get: ValidationText(self: _TableDef) -> str
        Set: ValidationText(self: _TableDef) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: _TableDef, Name: object, Type: object, Size: object) -> Field """
        ...

    def CreateIndex(self, Name:object) -> Index:
        """ CreateIndex(self: _TableDef, Name: object) -> Index """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: _TableDef, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ OpenRecordset(self: _TableDef, Type: object, Options: object) -> Recordset """
        ...

    def RefreshLink(self): # -> 
        """ RefreshLink(self: _TableDef) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TableDef(_TableDef): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class TableDefAttributeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TableDefAttributeEnum, values: dbAttachedODBC (536870912), dbAttachedTable (1073741824), dbAttachExclusive (65536), dbAttachSavePWD (131072), dbHiddenObject (1), dbSystemObject (-2147483646) """
    dbAttachedODBC: TableDefAttributeEnum = ...
    dbAttachedTable: TableDefAttributeEnum = ...
    dbAttachExclusive: TableDefAttributeEnum = ...
    dbAttachSavePWD: TableDefAttributeEnum = ...
    dbHiddenObject: TableDefAttributeEnum = ...
    dbSystemObject: TableDefAttributeEnum = ...
    value__ = ...


class TableDefClass(TableDef, __ComObject): # skipped bases: <type '_DAO'>, <type '_TableDef'>, <type 'object'>
    """ TableDefClass() """
    @property
    def Attributes(self) -> int:
        """
        Get: Attributes(self: TableDefClass) -> int
        Set: Attributes(self: TableDefClass) = value
        """
        ...

    @property
    def ConflictTable(self) -> str:
        """ Get: ConflictTable(self: TableDefClass) -> str """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: TableDefClass) -> str
        Set: Connect(self: TableDefClass) = value
        """
        ...

    @property
    def DateCreated(self) -> object:
        """ Get: DateCreated(self: TableDefClass) -> object """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: TableDefClass) -> Fields """
        ...

    @property
    def Indexes(self) -> Indexes:
        """ Get: Indexes(self: TableDefClass) -> Indexes """
        ...

    @property
    def LastUpdated(self) -> object:
        """ Get: LastUpdated(self: TableDefClass) -> object """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: TableDefClass) -> str
        Set: Name(self: TableDefClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: TableDefClass) -> Properties """
        ...

    @property
    def RecordCount(self) -> int:
        """ Get: RecordCount(self: TableDefClass) -> int """
        ...

    @property
    def ReplicaFilter(self) -> object:
        """
        Get: ReplicaFilter(self: TableDefClass) -> object
        Set: ReplicaFilter(self: TableDefClass) = value
        """
        ...

    @property
    def SourceTableName(self) -> str:
        """
        Get: SourceTableName(self: TableDefClass) -> str
        Set: SourceTableName(self: TableDefClass) = value
        """
        ...

    @property
    def Updatable(self) -> bool:
        """ Get: Updatable(self: TableDefClass) -> bool """
        ...

    @property
    def ValidationRule(self) -> str:
        """
        Get: ValidationRule(self: TableDefClass) -> str
        Set: ValidationRule(self: TableDefClass) = value
        """
        ...

    @property
    def ValidationText(self) -> str:
        """
        Get: ValidationText(self: TableDefClass) -> str
        Set: ValidationText(self: TableDefClass) = value
        """
        ...


    def CreateField(self, Name:object, Type:object, Size:object) -> Field:
        """ CreateField(self: TableDefClass, Name: object, Type: object, Size: object) -> Field """
        ...

    def CreateIndex(self, Name:object) -> Index:
        """ CreateIndex(self: TableDefClass, Name: object) -> Index """
        ...

    def CreateProperty(self, Name:object, Type:object, Value:object, DDL:object) -> Property:
        """ CreateProperty(self: TableDefClass, Name: object, Type: object, Value: object, DDL: object) -> Property """
        ...

    def OpenRecordset(self, Type:object, Options:object) -> Recordset:
        """ OpenRecordset(self: TableDefClass, Type: object, Options: object) -> Recordset """
        ...

    def RefreshLink(self): # -> 
        """ RefreshLink(self: TableDefClass) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TableDefs(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class UpdateCriteriaEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdateCriteriaEnum, values: dbCriteriaAllCols (4), dbCriteriaDeleteInsert (16), dbCriteriaKey (1), dbCriteriaModValues (2), dbCriteriaTimestamp (8), dbCriteriaUpdate (32) """
    dbCriteriaAllCols: UpdateCriteriaEnum = ...
    dbCriteriaDeleteInsert: UpdateCriteriaEnum = ...
    dbCriteriaKey: UpdateCriteriaEnum = ...
    dbCriteriaModValues: UpdateCriteriaEnum = ...
    dbCriteriaTimestamp: UpdateCriteriaEnum = ...
    dbCriteriaUpdate: UpdateCriteriaEnum = ...
    value__ = ...


class UpdateTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdateTypeEnum, values: dbUpdateBatch (4), dbUpdateCurrentRecord (2), dbUpdateRegular (1) """
    dbUpdateBatch: UpdateTypeEnum = ...
    dbUpdateCurrentRecord: UpdateTypeEnum = ...
    dbUpdateRegular: UpdateTypeEnum = ...
    value__ = ...


class _User(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Groups(self) -> Groups:
        """ Get: Groups(self: _User) -> Groups """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _User) -> str
        Set: Name(self: _User) = value
        """
        ...

    @property
    def Password(self): # -> 
        """ Set: Password(self: _User) = value """
        ...

    @property
    def PID(self): # -> 
        """ Set: PID(self: _User) = value """
        ...


    def CreateGroup(self, Name:object, PID:object) -> Group:
        """ CreateGroup(self: _User, Name: object, PID: object) -> Group """
        ...

    def NewPassword(self, bstrOld:str, bstrNew:str): # -> 
        """ NewPassword(self: _User, bstrOld: str, bstrNew: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class User(_User): # skipped bases: <type '_DAO'>, <type 'object'>
    """ no doc """
    pass

class UserClass(User, __ComObject): # skipped bases: <type '_DAO'>, <type '_User'>, <type 'object'>
    """ UserClass() """
    @property
    def Groups(self) -> Groups:
        """ Get: Groups(self: UserClass) -> Groups """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: UserClass) -> str
        Set: Name(self: UserClass) = value
        """
        ...

    @property
    def Password(self): # -> 
        """ Set: Password(self: UserClass) = value """
        ...

    @property
    def PID(self): # -> 
        """ Set: PID(self: UserClass) = value """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: UserClass) -> Properties """
        ...


    def CreateGroup(self, Name:object, PID:object) -> Group:
        """ CreateGroup(self: UserClass, Name: object, PID: object) -> Group """
        ...

    def NewPassword(self, bstrOld:str, bstrNew:str): # -> 
        """ NewPassword(self: UserClass, bstrOld: str, bstrNew: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Users(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Workspace(_DAO): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connections(self) -> Connections:
        """ Get: Connections(self: Workspace) -> Connections """
        ...

    @property
    def Databases(self) -> Databases:
        """ Get: Databases(self: Workspace) -> Databases """
        ...

    @property
    def DefaultCursorDriver(self) -> int:
        """
        Get: DefaultCursorDriver(self: Workspace) -> int
        Set: DefaultCursorDriver(self: Workspace) = value
        """
        ...

    @property
    def Groups(self) -> Groups:
        """ Get: Groups(self: Workspace) -> Groups """
        ...

    @property
    def hEnv(self) -> int:
        """ Get: hEnv(self: Workspace) -> int """
        ...

    @property
    def IsolateODBCTrans(self) -> Int16:
        """
        Get: IsolateODBCTrans(self: Workspace) -> Int16
        Set: IsolateODBCTrans(self: Workspace) = value
        """
        ...

    @property
    def LoginTimeout(self) -> int:
        """
        Get: LoginTimeout(self: Workspace) -> int
        Set: LoginTimeout(self: Workspace) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Workspace) -> str
        Set: Name(self: Workspace) = value
        """
        ...

    @property
    def Type(self) -> int:
        """ Get: Type(self: Workspace) -> int """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: Workspace) -> str """
        ...

    @property
    def Users(self) -> Users:
        """ Get: Users(self: Workspace) -> Users """
        ...

    @property
    def _30_Password(self): # -> 
        """ Set: _30_Password(self: Workspace) = value """
        ...

    @property
    def _30_UserName(self): # -> 
        """ Set: _30_UserName(self: Workspace) = value """
        ...


    def BeginTrans(self): # -> 
        """ BeginTrans(self: Workspace) """
        ...

    def Close(self): # -> 
        """ Close(self: Workspace) """
        ...

    def CommitTrans(self, Options:int): # -> 
        """ CommitTrans(self: Workspace, Options: int) """
        ...

    def CreateDatabase(self, Name:str, Connect:str, Option:object) -> Database:
        """ CreateDatabase(self: Workspace, Name: str, Connect: str, Option: object) -> Database """
        ...

    def CreateGroup(self, Name:object, PID:object) -> Group:
        """ CreateGroup(self: Workspace, Name: object, PID: object) -> Group """
        ...

    def CreateUser(self, Name:object, PID:object, Password:object) -> User:
        """ CreateUser(self: Workspace, Name: object, PID: object, Password: object) -> User """
        ...

    def OpenConnection(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Connection:
        """ OpenConnection(self: Workspace, Name: str, Options: object, ReadOnly: object, Connect: object) -> Connection """
        ...

    def OpenDatabase(self, Name:str, Options:object, ReadOnly:object, Connect:object) -> Database:
        """ OpenDatabase(self: Workspace, Name: str, Options: object, ReadOnly: object, Connect: object) -> Database """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: Workspace) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Workspaces(_DynaCollection): # skipped bases: <type '_Collection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WorkspaceTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkspaceTypeEnum, values: dbUseJet (2), dbUseODBC (1) """
    dbUseJet: WorkspaceTypeEnum = ...
    dbUseODBC: WorkspaceTypeEnum = ...
    value__ = ...


class _DAOSuppHelp(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum _DAOSuppHelp, values: KeepLocal (0), LogMessages (0), Replicable (0), ReplicableBool (0), V1xNullBehavior (0) """
    KeepLocal: _DAOSuppHelp = ...
    LogMessages: _DAOSuppHelp = ...
    Replicable: _DAOSuppHelp = ...
    ReplicableBool: _DAOSuppHelp = ...
    V1xNullBehavior: _DAOSuppHelp = ...
    value__ = ...


