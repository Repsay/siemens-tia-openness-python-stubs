# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.MetadataProvider calls itself MetadataProvider
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.SqlParser.Metadata import (CollationInfo, 
    DataTypeSpec, DatabasePermissionType, IBuiltInFunction, IClrDataType, 
    IColumn, ICursorDataType, ICursorParameter, ICursorVariable, IDatabase, 
    IDatabasePermission, IDatabasePrincipal, IExecutionContext, 
    IExtendedStoredProcedure, IForeignKeyColumn, ILogin, IMetadataCollection, 
    IMetadataObject, IMetadataOrderedCollection, IMutableApplicationRole, 
    IMutableAsymmetricKey, IMutableCertificate, IMutableCheckConstraint, 
    IMutableColumn, IMutableCredential, IMutableDatabase, 
    IMutableDatabaseDdlTrigger, IMutableDatabaseRole, 
    IMutableDefaultConstraint, IMutableDmlTrigger, 
    IMutableForeignKeyConstraint, IMutableIndexedColumn, IMutableLogin, 
    IMutableMetadataCollection, IMutableMetadataOrderedCollection, 
    IMutablePassword, IMutableRelationalIndex, IMutableScalarValuedFunction, 
    IMutableSchema, IMutableServer, IMutableServerDdlTrigger, 
    IMutableStoredProcedure, IMutableSynonym, IMutableTable, 
    IMutableTableDataType, IMutableTableValuedFunction, IMutableTabular, 
    IMutableUser, IMutableUserDefinedClrType, IMutableUserDefinedDataType, 
    IMutableUserDefinedTableType, IMutableView, IPrimaryKeyConstraint, 
    IRelationalIndex, IResolvedExtendedStoredProcedureSynonym, 
    IResolvedScalarValuedFunctionSynonym, IResolvedStoredProcedureSynonym, 
    IResolvedTableSynonym, IResolvedTableValuedFunctionSynonym, 
    IResolvedUserDefinedAggregateSynonym, IResolvedViewSynonym, IScalar, 
    IScalarDataType, IScalarExpression, IScalarParameter, 
    IScalarValuedFunction, IScalarVariable, ISchema, IServer, 
    IStoredProcedure, ISynonym, ISystemDataType, ITableDataType, 
    ITableParameter, ITableValuedFunction, ITableVariable, ITableViewBase, 
    ITabular, IUniqueConstraint, IUser, IUserDefinedAggregate, IView, 
    IXmlDataType)

from Microsoft.SqlServer.Management.SqlParser.Parser import ParseOptions

from System import (Action, Array, AsyncCallback, Enum, EventArgs, 
    IAsyncResult, MulticastDelegate, Predicate)

from System.Collections import IEnumerable, IEnumerator

from System.Data.Linq import ITable

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class ApplicationRoleCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabasePrincipal]'>, <type 'IEnumerable[IApplicationRole]'>, <type 'IMutableMetadataCollection[IApplicationRole]'>, <type 'IEnumerable[IDatabasePrincipal]'>, <type 'IMetadataCollection[IApplicationRole]'>, <type 'object'>
    """
    ApplicationRoleCollection(collationInfo: CollationInfo)
    ApplicationRoleCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class AsymmetricKeyCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IMetadataCollection[IAsymmetricKey]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IAsymmetricKey]'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IEnumerable[IAsymmetricKey]'>, <type 'object'>
    """
    AsymmetricKeyCollection(collationInfo: CollationInfo)
    AsymmetricKeyCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class BuiltInFunctionCollection(DictionaryCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IBuiltInFunction]'>, <type 'IEnumerable[IBuiltInFunction]'>, <type 'IMetadataCollection[IBuiltInFunction]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    BuiltInFunctionCollection()
    BuiltInFunctionCollection(initialCapacity: int)
    """
    pass

class BuiltInFunctionLookupBase(IBuiltInFunctionLookup): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CasingStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CasingStyle, values: Lowercase (1), None (0), Uppercase (2) """
    Lowercase: CasingStyle = ...
    Uppercase: CasingStyle = ...
    value__ = ...


class CertificateCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[ICertificate]'>, <type 'IEnumerable[ICertificate]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IMutableMetadataCollection[ICertificate]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    CertificateCollection(collationInfo: CollationInfo)
    CertificateCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class CollationLookupBase(ICollationLookup): # skipped bases: <type 'object'>
    """ no doc """
    pass

class Collection: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Empty(self) -> IMetadataCollection:
        """ Get: Empty() -> IMetadataCollection[T] """
        ...

    @property
    def EmptyOrdered(self) -> IMetadataOrderedCollection:
        """ Get: EmptyOrdered() -> IMetadataOrderedCollection[T] """
        ...


    @staticmethod
    def ApplyOnFirstAccess(collection:IMutableMetadataCollection, action:Action, actionCompleted:Predicate) -> IMetadataCollection:
        """ ApplyOnFirstAccess[C](collection: IMutableMetadataCollection[C], action: Action[C], actionCompleted: Predicate[C]) -> IMetadataCollection[T] """
        ...

    @staticmethod
    def Convert(collection:IMetadataCollection) -> IMetadataCollection:
        """ Convert[TDerived](collection: IMetadataCollection[TDerived]) -> IMetadataCollection[T] """
        ...

    @staticmethod
    def CopyToArray(collection:IMetadataCollection) -> Array:
        """ CopyToArray(collection: IMetadataCollection[T]) -> Array[T] """
        ...

    @staticmethod
    def CreateOrderedCollection(collationInfo:CollationInfo, *__args) -> IMetadataOrderedCollection: # Not found arg types: {'*__args': 'T'}
        """
        CreateOrderedCollection(collationInfo: CollationInfo, item: T) -> IMetadataOrderedCollection[T]
        CreateOrderedCollection(collationInfo: CollationInfo, item1: T, item2: T) -> IMetadataOrderedCollection[T]
        CreateOrderedCollection(collationInfo: CollationInfo, *items: Array[T]) -> IMetadataOrderedCollection[T]
        CreateOrderedCollection(collationInfo: CollationInfo, items: Array[T], count: int) -> IMetadataOrderedCollection[T]
        """
        ...

    @staticmethod
    def Filter(collection:IMetadataCollection, match:Predicate) -> IMetadataCollection:
        """ Filter(collection: IMetadataCollection[T], match: Predicate[T]) -> IMetadataCollection[T] """
        ...

    @staticmethod
    def Merge(*__args:Array) -> IMetadataCollection:
        """
        Merge(collection1: IMetadataCollection[T], collection2: IMetadataCollection[T]) -> IMetadataCollection[T]
        Merge(allowDuplicates: bool, collection1: IMetadataCollection[T], collection2: IMetadataCollection[T]) -> IMetadataCollection[T]
        Merge(*collections: Array[IMetadataCollection[T]]) -> IMetadataCollection[T]
        Merge(allowDuplicates: bool, *collections: Array[IMetadataCollection[T]]) -> IMetadataCollection[T]
        """
        ...


class ColumnAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ColumnAttributes, values: Identity (1), InPrimaryKey (2), None (0), Nullable (4) """
    Identity: ColumnAttributes = ...
    InPrimaryKey: ColumnAttributes = ...
    Nullable: ColumnAttributes = ...
    value__ = ...


class ColumnCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IColumn]'>, <type 'IEnumerable[IColumn]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IColumn]'>, <type 'IMetadataCollection[IScalar]'>, <type 'IEnumerable[IScalar]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ColumnCollection(collationInfo: CollationInfo)
    ColumnCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ColumnOrderedCollection(OrderedCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IColumn]'>, <type 'IEnumerable[IColumn]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IColumn]'>, <type 'IMutableMetadataOrderedCollection[IColumn]'>, <type 'IMetadataOrderedCollection[IColumn]'>, <type 'IMetadataOrderedCollection[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ColumnOrderedCollection(collationInfo: CollationInfo)
    ColumnOrderedCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ConstraintCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IConstraint]'>, <type 'IMutableMetadataCollection[IConstraint]'>, <type 'IEnumerable'>, <type 'IEnumerable[IConstraint]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ConstraintCollection(collationInfo: CollationInfo)
    ConstraintCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class CredentialCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IEnumerable[ICredential]'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IMutableMetadataCollection[ICredential]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IMetadataCollection[ICredential]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    CredentialCollection(collationInfo: CollationInfo)
    CredentialCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class CursorVariableCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[ILocalVariable]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[ICursorVariable]'>, <type 'IEnumerable[ILocalVariable]'>, <type 'IEnumerable[ICursorVariable]'>, <type 'IMutableMetadataCollection[ICursorVariable]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    CursorVariableCollection(collationInfo: CollationInfo)
    CursorVariableCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DatabaseCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabase]'>, <type 'IEnumerable[IDatabase]'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IMutableMetadataCollection[IDatabase]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DatabaseCollection(collationInfo: CollationInfo)
    DatabaseCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DatabaseDdlTriggerCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[IDatabaseDdlTrigger]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IDatabaseDdlTrigger]'>, <type 'IMetadataCollection[IDatabaseDdlTrigger]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DatabaseDdlTriggerCollection(collationInfo: CollationInfo)
    DatabaseDdlTriggerCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DatabasePermissionCollection(OrderedCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataOrderedCollection[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataOrderedCollection[IDatabasePermission]'>, <type 'IMutableMetadataCollection[IDatabasePermission]'>, <type 'IEnumerable[IDatabasePermission]'>, <type 'IMetadataCollection[IDatabasePermission]'>, <type 'IMetadataOrderedCollection[IDatabasePermission]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DatabasePermissionCollection(collationInfo: CollationInfo)
    DatabasePermissionCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DatabaseRoleCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMutableMetadataCollection[IDatabaseRole]'>, <type 'IEnumerable[IDatabaseRole]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabasePrincipal]'>, <type 'IMetadataCollection[IDatabaseRole]'>, <type 'IEnumerable[IDatabasePrincipal]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DatabaseRoleCollection(collationInfo: CollationInfo)
    DatabaseRoleCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DatePartCollection(DictionaryCollection): # skipped bases: <type 'IEnumerable[IDatePart]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IMutableMetadataCollection[IDatePart]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatePart]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DatePartCollection()
    DatePartCollection(initialCapacity: int)
    """
    pass

class DictionaryCollection(IMetadataCollection, DictionaryCollectionBase): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[T]'>, <type 'IMetadataCollection[T]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[T]'>, <type 'object'>
    """ DictionaryCollection[T](initialCapacity: int, collationInfo: CollationInfo) """
    pass

class DictionaryCollectionBase(IMutableMetadataCollection): # skipped bases: <type 'IMetadataCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AsMetadataObjectCollection(self) -> IMetadataCollection:
        """ Get: AsMetadataObjectCollection(self: DictionaryCollectionBase[T, U]) -> IMetadataCollection[IMetadataObject] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DictionaryCollectionBase[T, U]) -> int """
        ...


    def Contains(self, *__args:str) -> bool:
        """
        Contains(self: DictionaryCollectionBase[T, U], name: str) -> bool
        Contains(self: DictionaryCollectionBase[T, U], item: T) -> bool
        """
        ...

    def FindAll(self, *__args:Predicate) -> IEnumerable:
        """
        FindAll(self: DictionaryCollectionBase[T, U], match: Predicate[T]) -> IEnumerable[T]
        FindAll(self: DictionaryCollectionBase[T, U], name: str) -> IEnumerable[T]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DictionaryCollectionBase[T, U]) -> IEnumerator[T] """
        ...


class DmlTriggerCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IDmlTrigger]'>, <type 'IMetadataCollection[IDmlTrigger]'>, <type 'IEnumerable[IDmlTrigger]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    DmlTriggerCollection(collationInfo: CollationInfo)
    DmlTriggerCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class DualTypeSortedListCollection(IMetadataCollection, SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable[B]'>, <type 'IMetadataCollection[T]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """ DualTypeSortedListCollection[T, B](initialCapacity: int, collationInfo: CollationInfo) """
    pass

class ExtendedStoredProcedureCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[ICallableModule]'>, <type 'IEnumerable[ICallableModule]'>, <type 'IEnumerable'>, <type 'IEnumerable[IExtendedStoredProcedure]'>, <type 'IMetadataCollection[IExtendedStoredProcedure]'>, <type 'IMutableMetadataCollection[IExtendedStoredProcedure]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ExtendedStoredProcedureCollection(collationInfo: CollationInfo)
    ExtendedStoredProcedureCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ExtensionMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayInfoProvider(self) -> IMetadataDisplayInfoProvider:
        """ Get: DisplayInfoProvider() -> IMetadataDisplayInfoProvider """
        ...


    @staticmethod
    def GetDatabaseQualifiedName(metadataObject:IMetadataObject) -> str:
        """ GetDatabaseQualifiedName(metadataObject: IMetadataObject) -> str """
        ...

    @staticmethod
    def GetDescription(metadataObject:IMetadataObject) -> str:
        """ GetDescription(metadataObject: IMetadataObject) -> str """
        ...

    @staticmethod
    def GetDisplayName(metadataObject:IMetadataObject) -> str:
        """ GetDisplayName(metadataObject: IMetadataObject) -> str """
        ...

    @staticmethod
    def ToString(metadataObject:IMetadataObject = ...) -> str:
        """ ToString(metadataObject: IMetadataObject) -> str """
        ...

    __all__: list = ...


class ForeignKeyColumnCollection(OrderedCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IForeignKeyColumn]'>, <type 'IMutableMetadataOrderedCollection[IForeignKeyColumn]'>, <type 'IEnumerable'>, <type 'IEnumerable[IForeignKeyColumn]'>, <type 'IMutableMetadataCollection[IForeignKeyColumn]'>, <type 'IMetadataOrderedCollection[IForeignKeyColumn]'>, <type 'IMetadataOrderedCollection[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ForeignKeyColumnCollection(collationInfo: CollationInfo)
    ForeignKeyColumnCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class IAsymmetricKeyFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateAsymmetricKey(self, database:IDatabase, name:str) -> IMutableAsymmetricKey:
        """ CreateAsymmetricKey(self: IAsymmetricKeyFactory, database: IDatabase, name: str) -> IMutableAsymmetricKey """
        ...


class IBuiltInFunctionLookup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllBuiltIns(self) -> IMetadataCollection:
        """ Get: AllBuiltIns(self: IBuiltInFunctionLookup) -> IMetadataCollection[IBuiltInFunction] """
        ...

    @property
    def BuiltInFunctions(self) -> IMetadataCollection:
        """ Get: BuiltInFunctions(self: IBuiltInFunctionLookup) -> IMetadataCollection[IBuiltInFunction] """
        ...

    @property
    def DateParts(self) -> IMetadataCollection:
        """ Get: DateParts(self: IBuiltInFunctionLookup) -> IMetadataCollection[IDatePart] """
        ...

    @property
    def GlobalVariables(self) -> IMetadataCollection:
        """ Get: GlobalVariables(self: IBuiltInFunctionLookup) -> IMetadataCollection[IBuiltInFunction] """
        ...


    def GetMultiTypeBuiltInFunction(self, name:str, dataType:ISystemDataType) -> IBuiltInFunction:
        """ GetMultiTypeBuiltInFunction(self: IBuiltInFunctionLookup, name: str, dataType: ISystemDataType) -> IBuiltInFunction """
        ...


class ICertificateFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCertificate(self, database:IDatabase, name:str) -> IMutableCertificate:
        """ CreateCertificate(self: ICertificateFactory, database: IDatabase, name: str) -> IMutableCertificate """
        ...


class ICollationLookup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Collations(self) -> IMetadataCollection:
        """ Get: Collations(self: ICollationLookup) -> IMetadataCollection[ICollation] """
        ...



class IColumnFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Null(self) -> IColumn:
        """ Get: Null(self: IColumnFactory) -> IColumn """
        ...


    def Create(self, parent:ITabular, name:str) -> IMutableColumn:
        """ Create(self: IColumnFactory, parent: ITabular, name: str) -> IMutableColumn """
        ...

    def CreateAnonymousColumn(self, dataType:IScalarDataType, nullable:bool) -> IColumn:
        """ CreateAnonymousColumn(self: IColumnFactory, dataType: IScalarDataType, nullable: bool) -> IColumn """
        ...

    def CreateColumnAlias(self, *__args) -> IColumn:
        """
        CreateColumnAlias(self: IColumnFactory, aliasedColumn: IColumn, alias: str) -> IColumn
        CreateColumnAlias(self: IColumnFactory, parent: ITabular, aliasedColumn: IColumn, alias: str) -> IColumn
        """
        ...

    def CreateScalarAlias(self, *__args) -> IColumn:
        """
        CreateScalarAlias(self: IColumnFactory, aliasedScalar: IScalar, alias: str) -> IColumn
        CreateScalarAlias(self: IColumnFactory, parent: ITabular, aliasedScalar: IScalar, alias: str) -> IColumn
        """
        ...

    def CreateSimpleColumn(self, parent:ITabular, name:str, dataType:IScalarDataType, nullable:bool) -> IColumn:
        """ CreateSimpleColumn(self: IColumnFactory, parent: ITabular, name: str, dataType: IScalarDataType, nullable: bool) -> IColumn """
        ...


class IConstraintFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCheckConstraint(self, parent:ITabular, name:str) -> IMutableCheckConstraint:
        """ CreateCheckConstraint(self: IConstraintFactory, parent: ITabular, name: str) -> IMutableCheckConstraint """
        ...

    def CreateDefaultConstraint(self, parent:IColumn, name:str) -> IMutableDefaultConstraint:
        """ CreateDefaultConstraint(self: IConstraintFactory, parent: IColumn, name: str) -> IMutableDefaultConstraint """
        ...

    def CreateForeignKeyColumn(self, referencingColumn:IColumn, referencedColumn:IColumn) -> IForeignKeyColumn:
        """ CreateForeignKeyColumn(self: IConstraintFactory, referencingColumn: IColumn, referencedColumn: IColumn) -> IForeignKeyColumn """
        ...

    def CreateForeignKeyConstraint(self, parent:ITable, name:str) -> IMutableForeignKeyConstraint:
        """ CreateForeignKeyConstraint(self: IConstraintFactory, parent: ITable, name: str) -> IMutableForeignKeyConstraint """
        ...

    def CreatePrimaryKeyConstraint(self, parent:ITabular, index:IRelationalIndex) -> IPrimaryKeyConstraint:
        """ CreatePrimaryKeyConstraint(self: IConstraintFactory, parent: ITabular, index: IRelationalIndex) -> IPrimaryKeyConstraint """
        ...

    def CreateUniqueConstraint(self, parent:ITabular, index:IRelationalIndex) -> IUniqueConstraint:
        """ CreateUniqueConstraint(self: IConstraintFactory, parent: ITabular, index: IRelationalIndex) -> IUniqueConstraint """
        ...


class ICredentialFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCredential(self, server:IServer, name:str) -> IMutableCredential:
        """ CreateCredential(self: ICredentialFactory, server: IServer, name: str) -> IMutableCredential """
        ...


class IDatabaseFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, *__args:IDatabase) -> IMutableDatabase:
        """
        Create(self: IDatabaseFactory, server: IServer, name: str, collationInfo: CollationInfo) -> IMutableDatabase
        Create(self: IDatabaseFactory, otherDatabase: IDatabase) -> IMutableDatabase
        """
        ...

    def CreateEmptyDatabase(self, server:IServer, name:str, collationInfo:CollationInfo, isSystemObject:bool) -> IDatabase:
        """ CreateEmptyDatabase(self: IDatabaseFactory, server: IServer, name: str, collationInfo: CollationInfo, isSystemObject: bool) -> IDatabase """
        ...


class IDataTypeFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Cursor(self) -> ICursorDataType:
        """ Get: Cursor(self: IDataTypeFactory) -> ICursorDataType """
        ...

    @property
    def UnknownClr(self) -> IClrDataType:
        """ Get: UnknownClr(self: IDataTypeFactory) -> IClrDataType """
        ...

    @property
    def UnknownScalar(self) -> IScalarDataType:
        """ Get: UnknownScalar(self: IDataTypeFactory) -> IScalarDataType """
        ...

    @property
    def UnknownTable(self) -> ITableDataType:
        """ Get: UnknownTable(self: IDataTypeFactory) -> ITableDataType """
        ...

    @property
    def Void(self) -> IScalarDataType:
        """ Get: Void(self: IDataTypeFactory) -> IScalarDataType """
        ...

    @property
    def XmlNode(self) -> IXmlDataType:
        """ Get: XmlNode(self: IDataTypeFactory) -> IXmlDataType """
        ...


    def CreateTableDataType(self, name:str, collationInfo:CollationInfo) -> IMutableTableDataType:
        """ CreateTableDataType(self: IDataTypeFactory, name: str, collationInfo: CollationInfo) -> IMutableTableDataType """
        ...


class IExecutionContextFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateExecuteAsCaller(self) -> IExecutionContext:
        """ CreateExecuteAsCaller(self: IExecutionContextFactory) -> IExecutionContext """
        ...

    def CreateExecuteAsLogin(self, login:ILogin) -> IExecutionContext:
        """ CreateExecuteAsLogin(self: IExecutionContextFactory, login: ILogin) -> IExecutionContext """
        ...

    def CreateExecuteAsOwner(self) -> IExecutionContext:
        """ CreateExecuteAsOwner(self: IExecutionContextFactory) -> IExecutionContext """
        ...

    def CreateExecuteAsSelf(self) -> IExecutionContext:
        """ CreateExecuteAsSelf(self: IExecutionContextFactory) -> IExecutionContext """
        ...

    def CreateExecuteAsUser(self, user:IUser) -> IExecutionContext:
        """ CreateExecuteAsUser(self: IExecutionContextFactory, user: IUser) -> IExecutionContext """
        ...


class IIndexFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateIndexedColumn(self, referencedColumn:IColumn) -> IMutableIndexedColumn:
        """ CreateIndexedColumn(self: IIndexFactory, referencedColumn: IColumn) -> IMutableIndexedColumn """
        ...

    def CreateRelationalIndex(self, parent:ITabular, name:str, collationInfo:CollationInfo) -> IMutableRelationalIndex:
        """ CreateRelationalIndex(self: IIndexFactory, parent: ITabular, name: str, collationInfo: CollationInfo) -> IMutableRelationalIndex """
        ...


class ILiteralScalarFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Binary(self) -> IScalarExpression:
        """ Get: Binary(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Default(self) -> IScalarExpression:
        """ Get: Default(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Identifier(self) -> IScalarExpression:
        """ Get: Identifier(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Image(self) -> IScalarExpression:
        """ Get: Image(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Integer(self) -> IScalarExpression:
        """ Get: Integer(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Money(self) -> IScalarExpression:
        """ Get: Money(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Null(self) -> IScalarExpression:
        """ Get: Null(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Numeric(self) -> IScalarExpression:
        """ Get: Numeric(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def Real(self) -> IScalarExpression:
        """ Get: Real(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def String(self) -> IScalarExpression:
        """ Get: String(self: ILiteralScalarFactory) -> IScalarExpression """
        ...

    @property
    def UnicodeString(self) -> IScalarExpression:
        """ Get: UnicodeString(self: ILiteralScalarFactory) -> IScalarExpression """
        ...



class ILoginFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateAsymmetricKeyLogin(self, server:IServer, name:str) -> IMutableLogin:
        """ CreateAsymmetricKeyLogin(self: ILoginFactory, server: IServer, name: str) -> IMutableLogin """
        ...

    def CreateCertificateLogin(self, server:IServer, name:str) -> IMutableLogin:
        """ CreateCertificateLogin(self: ILoginFactory, server: IServer, name: str) -> IMutableLogin """
        ...

    def CreatePassword(self) -> IMutablePassword:
        """ CreatePassword(self: ILoginFactory) -> IMutablePassword """
        ...

    def CreateSqlLogin(self, server:IServer, name:str) -> IMutableLogin:
        """ CreateSqlLogin(self: ILoginFactory, server: IServer, name: str) -> IMutableLogin """
        ...

    def CreateWindowsLogin(self, server:IServer, name:str) -> IMutableLogin:
        """ CreateWindowsLogin(self: ILoginFactory, server: IServer, name: str) -> IMutableLogin """
        ...


class IMetadataDisplayInfoProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltInCasing(self) -> CasingStyle:
        """
        Get: BuiltInCasing(self: IMetadataDisplayInfoProvider) -> CasingStyle
        Set: BuiltInCasing(self: IMetadataDisplayInfoProvider) = value
        """
        ...


    def CollectionToString(self, metadataCollection:IMetadataCollection, singleLine:bool) -> str:
        """
        CollectionToString[T](self: IMetadataDisplayInfoProvider, metadataCollection: IMetadataCollection[T], singleLine: bool) -> str
        CollectionToString[T](self: IMetadataDisplayInfoProvider, metadataCollection: IMetadataOrderedCollection[T], singleLine: bool) -> str
        """
        ...

    def GetDatabaseQualifiedName(self, metadataObject:IMetadataObject) -> str:
        """ GetDatabaseQualifiedName(self: IMetadataDisplayInfoProvider, metadataObject: IMetadataObject) -> str """
        ...

    def GetDescription(self, metadataObject:IMetadataObject) -> str:
        """ GetDescription(self: IMetadataDisplayInfoProvider, metadataObject: IMetadataObject) -> str """
        ...

    def GetDisplayName(self, metadataObject:IMetadataObject) -> str:
        """ GetDisplayName(self: IMetadataDisplayInfoProvider, metadataObject: IMetadataObject) -> str """
        ...

    def ObjectToString(self, metadataObject:IMetadataObject) -> str:
        """ ObjectToString(self: IMetadataDisplayInfoProvider, metadataObject: IMetadataObject) -> str """
        ...


class IMetadataFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsymmetricKey(self) -> IAsymmetricKeyFactory:
        """ Get: AsymmetricKey(self: IMetadataFactory) -> IAsymmetricKeyFactory """
        ...

    @property
    def Certificate(self) -> ICertificateFactory:
        """ Get: Certificate(self: IMetadataFactory) -> ICertificateFactory """
        ...

    @property
    def Column(self) -> IColumnFactory:
        """ Get: Column(self: IMetadataFactory) -> IColumnFactory """
        ...

    @property
    def Constraint(self) -> IConstraintFactory:
        """ Get: Constraint(self: IMetadataFactory) -> IConstraintFactory """
        ...

    @property
    def Credential(self) -> ICredentialFactory:
        """ Get: Credential(self: IMetadataFactory) -> ICredentialFactory """
        ...

    @property
    def Database(self) -> IDatabaseFactory:
        """ Get: Database(self: IMetadataFactory) -> IDatabaseFactory """
        ...

    @property
    def DataType(self) -> IDataTypeFactory:
        """ Get: DataType(self: IMetadataFactory) -> IDataTypeFactory """
        ...

    @property
    def ExecutionContext(self) -> IExecutionContextFactory:
        """ Get: ExecutionContext(self: IMetadataFactory) -> IExecutionContextFactory """
        ...

    @property
    def Index(self) -> IIndexFactory:
        """ Get: Index(self: IMetadataFactory) -> IIndexFactory """
        ...

    @property
    def Login(self) -> ILoginFactory:
        """ Get: Login(self: IMetadataFactory) -> ILoginFactory """
        ...

    @property
    def Parameter(self) -> IParameterFactory:
        """ Get: Parameter(self: IMetadataFactory) -> IParameterFactory """
        ...

    @property
    def Permission(self) -> IPermissionFactory:
        """ Get: Permission(self: IMetadataFactory) -> IPermissionFactory """
        ...

    @property
    def ResolvedSynonym(self) -> IResolvedSynonymFactory:
        """ Get: ResolvedSynonym(self: IMetadataFactory) -> IResolvedSynonymFactory """
        ...

    @property
    def Role(self) -> IRoleFactory:
        """ Get: Role(self: IMetadataFactory) -> IRoleFactory """
        ...

    @property
    def Scalar(self) -> IScalarFactory:
        """ Get: Scalar(self: IMetadataFactory) -> IScalarFactory """
        ...

    @property
    def Schema(self) -> ISchemaFactory:
        """ Get: Schema(self: IMetadataFactory) -> ISchemaFactory """
        ...

    @property
    def Server(self) -> IServerFactory:
        """ Get: Server(self: IMetadataFactory) -> IServerFactory """
        ...

    @property
    def StoredProcedure(self) -> IStoredProcedureFactory:
        """ Get: StoredProcedure(self: IMetadataFactory) -> IStoredProcedureFactory """
        ...

    @property
    def Synonym(self) -> ISynonymFactory:
        """ Get: Synonym(self: IMetadataFactory) -> ISynonymFactory """
        ...

    @property
    def Tabular(self) -> ITabularFactory:
        """ Get: Tabular(self: IMetadataFactory) -> ITabularFactory """
        ...

    @property
    def Trigger(self) -> ITriggerFactory:
        """ Get: Trigger(self: IMetadataFactory) -> ITriggerFactory """
        ...

    @property
    def User(self) -> IUserFactory:
        """ Get: User(self: IMetadataFactory) -> IUserFactory """
        ...

    @property
    def UserDefinedFunction(self) -> IUserDefinedFunctionFactory:
        """ Get: UserDefinedFunction(self: IMetadataFactory) -> IUserDefinedFunctionFactory """
        ...

    @property
    def UserDefinedType(self) -> IUserDefinedTypeFactory:
        """ Get: UserDefinedType(self: IMetadataFactory) -> IUserDefinedTypeFactory """
        ...

    @property
    def Variable(self) -> IVariableFactory:
        """ Get: Variable(self: IMetadataFactory) -> IVariableFactory """
        ...



class IMetadataProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AfterBindHandler(self) -> MetadataProviderEventHandler:
        """ Get: AfterBindHandler(self: IMetadataProvider) -> MetadataProviderEventHandler """
        ...

    @property
    def BeforeBindHandler(self) -> MetadataProviderEventHandler:
        """ Get: BeforeBindHandler(self: IMetadataProvider) -> MetadataProviderEventHandler """
        ...

    @property
    def BuiltInFunctionLookup(self) -> IBuiltInFunctionLookup:
        """ Get: BuiltInFunctionLookup(self: IMetadataProvider) -> IBuiltInFunctionLookup """
        ...

    @property
    def CollationLookup(self) -> ICollationLookup:
        """ Get: CollationLookup(self: IMetadataProvider) -> ICollationLookup """
        ...

    @property
    def MetadataFactory(self) -> IMetadataFactory:
        """ Get: MetadataFactory(self: IMetadataProvider) -> IMetadataFactory """
        ...

    @property
    def Server(self) -> IServer:
        """ Get: Server(self: IMetadataProvider) -> IServer """
        ...

    @property
    def SystemDataTypeLookup(self) -> ISystemDataTypeLookup:
        """ Get: SystemDataTypeLookup(self: IMetadataProvider) -> ISystemDataTypeLookup """
        ...



class IndexCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IIndex]'>, <type 'IMutableMetadataCollection[IIndex]'>, <type 'IEnumerable[IIndex]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    IndexCollection(collationInfo: CollationInfo)
    IndexCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class IndexedColumnCollection(OrderedCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMutableMetadataOrderedCollection[IIndexedColumn]'>, <type 'IMutableMetadataCollection[IIndexedColumn]'>, <type 'IMetadataCollection[IIndexedColumn]'>, <type 'IEnumerable[IIndexedColumn]'>, <type 'IEnumerable'>, <type 'IMetadataOrderedCollection[IIndexedColumn]'>, <type 'IMetadataOrderedCollection[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    IndexedColumnCollection(collationInfo: CollationInfo)
    IndexedColumnCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class IParameterFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCursorParameter(self, name:str) -> ICursorParameter:
        """ CreateCursorParameter(self: IParameterFactory, name: str) -> ICursorParameter """
        ...

    def CreateScalarParameter(self, name:str, dataType:IScalarDataType, isOutput:bool = ..., defaultValue:str = ...) -> IScalarParameter:
        """
        CreateScalarParameter(self: IParameterFactory, name: str, dataType: IScalarDataType) -> IScalarParameter
        CreateScalarParameter(self: IParameterFactory, name: str, dataType: IScalarDataType, isOutput: bool, defaultValue: str) -> IScalarParameter
        """
        ...

    def CreateTableParameter(self, name:str, dataType:ITableDataType) -> ITableParameter:
        """ CreateTableParameter(self: IParameterFactory, name: str, dataType: ITableDataType) -> ITableParameter """
        ...


class IPermissionFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateDatabasePermission(self, databasePrincipal:IDatabasePrincipal, targetObject:IMetadataObject, permissionType:DatabasePermissionType, grantor:IDatabasePrincipal) -> IDatabasePermission:
        """ CreateDatabasePermission(self: IPermissionFactory, databasePrincipal: IDatabasePrincipal, targetObject: IMetadataObject, permissionType: DatabasePermissionType, grantor: IDatabasePrincipal) -> IDatabasePermission """
        ...


class IResolvedSynonymFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateResolvedExtendedStoredProcedureSynonym(self, synonym:ISynonym, extendedStoredProcedure:IExtendedStoredProcedure) -> IResolvedExtendedStoredProcedureSynonym:
        """ CreateResolvedExtendedStoredProcedureSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, extendedStoredProcedure: IExtendedStoredProcedure) -> IResolvedExtendedStoredProcedureSynonym """
        ...

    def CreateResolvedScalarValuedFunctionSynonym(self, synonym:ISynonym, scalarValuedFunction:IScalarValuedFunction) -> IResolvedScalarValuedFunctionSynonym:
        """ CreateResolvedScalarValuedFunctionSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, scalarValuedFunction: IScalarValuedFunction) -> IResolvedScalarValuedFunctionSynonym """
        ...

    def CreateResolvedStoredProcedureSynonym(self, synonym:ISynonym, storedProcedure:IStoredProcedure) -> IResolvedStoredProcedureSynonym:
        """ CreateResolvedStoredProcedureSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, storedProcedure: IStoredProcedure) -> IResolvedStoredProcedureSynonym """
        ...

    def CreateResolvedTableSynonym(self, synonym:ISynonym, table:ITable) -> IResolvedTableSynonym:
        """ CreateResolvedTableSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, table: ITable) -> IResolvedTableSynonym """
        ...

    def CreateResolvedTableValuedFunctionSynonym(self, synonym:ISynonym, tableValuedFunction:ITableValuedFunction) -> IResolvedTableValuedFunctionSynonym:
        """ CreateResolvedTableValuedFunctionSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, tableValuedFunction: ITableValuedFunction) -> IResolvedTableValuedFunctionSynonym """
        ...

    def CreateResolvedUserDefinedAggregateSynonym(self, synonym:ISynonym, userDefinedAggregate:IUserDefinedAggregate) -> IResolvedUserDefinedAggregateSynonym:
        """ CreateResolvedUserDefinedAggregateSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, userDefinedAggregate: IUserDefinedAggregate) -> IResolvedUserDefinedAggregateSynonym """
        ...

    def CreateResolvedViewSynonym(self, synonym:ISynonym, view:IView) -> IResolvedViewSynonym:
        """ CreateResolvedViewSynonym(self: IResolvedSynonymFactory, synonym: ISynonym, view: IView) -> IResolvedViewSynonym """
        ...


class IRoleFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateApplicationRole(self, database:IDatabase, name:str) -> IMutableApplicationRole:
        """ CreateApplicationRole(self: IRoleFactory, database: IDatabase, name: str) -> IMutableApplicationRole """
        ...

    def CreateDatabaseRole(self, database:IDatabase, name:str) -> IMutableDatabaseRole:
        """ CreateDatabaseRole(self: IRoleFactory, database: IDatabase, name: str) -> IMutableDatabaseRole """
        ...


class IScalarFactory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Literal(self) -> ILiteralScalarFactory:
        """ Get: Literal(self: IScalarFactory) -> ILiteralScalarFactory """
        ...

    @property
    def Null(self) -> IScalar:
        """ Get: Null(self: IScalarFactory) -> IScalar """
        ...


    def CreateScalarExpression(self, dataType:IScalarDataType, nullable:bool) -> IScalarExpression:
        """ CreateScalarExpression(self: IScalarFactory, dataType: IScalarDataType, nullable: bool) -> IScalarExpression """
        ...


class ISchemaFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, *__args:ISchema) -> IMutableSchema:
        """
        Create(self: ISchemaFactory, database: IDatabase, name: str) -> IMutableSchema
        Create(self: ISchemaFactory, otherSchema: ISchema) -> IMutableSchema
        """
        ...

    def CreateEmptySchema(self, database:IDatabase, name:str, isSystemObject:bool) -> ISchema:
        """ CreateEmptySchema(self: ISchemaFactory, database: IDatabase, name: str, isSystemObject: bool) -> ISchema """
        ...


class IServerFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, *__args:IServer) -> IMutableServer:
        """
        Create(self: IServerFactory, name: str, collationInfo: CollationInfo) -> IMutableServer
        Create(self: IServerFactory, otherServer: IServer) -> IMutableServer
        """
        ...


class IStoredProcedureFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, schema:ISchema, name:str) -> IMutableStoredProcedure:
        """ Create(self: IStoredProcedureFactory, schema: ISchema, name: str) -> IMutableStoredProcedure """
        ...


class ISynonymFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateSynonym(self, schema:ISchema, name:str) -> IMutableSynonym:
        """ CreateSynonym(self: ISynonymFactory, schema: ISchema, name: str) -> IMutableSynonym """
        ...


class ISystemDataTypeLookup: # skipped bases: <type 'object'>
    """ no doc """
    def Find(self, typeSpec:DataTypeSpec, *__args:bool) -> ISystemDataType:
        """
        Find(self: ISystemDataTypeLookup, typeSpec: DataTypeSpec, isMaximum: bool) -> ISystemDataType
        Find(self: ISystemDataTypeLookup, typeSpec: DataTypeSpec, precisionOrMaxLength: int) -> ISystemDataType
        Find(self: ISystemDataTypeLookup, typeSpec: DataTypeSpec, precision: int, scale: int) -> ISystemDataType
        """
        ...


class ITabularFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCommonTableExpression(self, name:str, collationInfo:CollationInfo) -> IMutableTabular:
        """ CreateCommonTableExpression(self: ITabularFactory, name: str, collationInfo: CollationInfo) -> IMutableTabular """
        ...

    def CreateDerivedTable(self, name:str, collationInfo:CollationInfo) -> IMutableTabular:
        """ CreateDerivedTable(self: ITabularFactory, name: str, collationInfo: CollationInfo) -> IMutableTabular """
        ...

    def CreateDmlDeletedTable(self, targetTable:ITabular) -> ITabular:
        """ CreateDmlDeletedTable(self: ITabularFactory, targetTable: ITabular) -> ITabular """
        ...

    def CreateDmlInsertedTable(self, targetTable:ITabular) -> ITabular:
        """ CreateDmlInsertedTable(self: ITabularFactory, targetTable: ITabular) -> ITabular """
        ...

    def CreateDmlTableSource(self, name:str, collationInfo:CollationInfo) -> IMutableTabular:
        """ CreateDmlTableSource(self: ITabularFactory, name: str, collationInfo: CollationInfo) -> IMutableTabular """
        ...

    def CreatePivotTable(self, name:str, collationInfo:CollationInfo) -> IMutableTabular:
        """ CreatePivotTable(self: ITabularFactory, name: str, collationInfo: CollationInfo) -> IMutableTabular """
        ...

    def CreateTable(self, *__args:ITable) -> IMutableTable:
        """
        CreateTable(self: ITabularFactory, schema: ISchema, name: str) -> IMutableTable
        CreateTable(self: ITabularFactory, table: ITable) -> IMutableTable
        """
        ...

    def CreateTableAlias(self, aliasedTable:ITabular, alias:str) -> ITabular:
        """ CreateTableAlias(self: ITabularFactory, aliasedTable: ITabular, alias: str) -> ITabular """
        ...

    def CreateUnpivotTable(self, name:str, collationInfo:CollationInfo) -> IMutableTabular:
        """ CreateUnpivotTable(self: ITabularFactory, name: str, collationInfo: CollationInfo) -> IMutableTabular """
        ...

    def CreateView(self, *__args:IView) -> IMutableView:
        """
        CreateView(self: ITabularFactory, schema: ISchema, name: str) -> IMutableView
        CreateView(self: ITabularFactory, view: IView) -> IMutableView
        """
        ...


class ITriggerFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateDatabaseDdlTrigger(self, database:IDatabase, name:str) -> IMutableDatabaseDdlTrigger:
        """ CreateDatabaseDdlTrigger(self: ITriggerFactory, database: IDatabase, name: str) -> IMutableDatabaseDdlTrigger """
        ...

    def CreateDmlTrigger(self, parent:ITableViewBase, name:str) -> IMutableDmlTrigger:
        """ CreateDmlTrigger(self: ITriggerFactory, parent: ITableViewBase, name: str) -> IMutableDmlTrigger """
        ...

    def CreateServerDdlTrigger(self, server:IServer, name:str) -> IMutableServerDdlTrigger:
        """ CreateServerDdlTrigger(self: ITriggerFactory, server: IServer, name: str) -> IMutableServerDdlTrigger """
        ...


class IUserDefinedFunctionFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateScalarValuedFunction(self, schema:ISchema, name:str) -> IMutableScalarValuedFunction:
        """ CreateScalarValuedFunction(self: IUserDefinedFunctionFactory, schema: ISchema, name: str) -> IMutableScalarValuedFunction """
        ...

    def CreateTableValuedFunction(self, schema:ISchema, name:str) -> IMutableTableValuedFunction:
        """ CreateTableValuedFunction(self: IUserDefinedFunctionFactory, schema: ISchema, name: str) -> IMutableTableValuedFunction """
        ...


class IUserDefinedTypeFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateClrType(self, schema:ISchema, name:str) -> IMutableUserDefinedClrType:
        """ CreateClrType(self: IUserDefinedTypeFactory, schema: ISchema, name: str) -> IMutableUserDefinedClrType """
        ...

    def CreateDataType(self, schema:ISchema, name:str) -> IMutableUserDefinedDataType:
        """ CreateDataType(self: IUserDefinedTypeFactory, schema: ISchema, name: str) -> IMutableUserDefinedDataType """
        ...

    def CreateTableType(self, schema:ISchema, name:str) -> IMutableUserDefinedTableType:
        """ CreateTableType(self: IUserDefinedTypeFactory, schema: ISchema, name: str) -> IMutableUserDefinedTableType """
        ...


class IUserFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateAsymmetricKeyUser(self, database:IDatabase, name:str) -> IMutableUser:
        """ CreateAsymmetricKeyUser(self: IUserFactory, database: IDatabase, name: str) -> IMutableUser """
        ...

    def CreateCertificateUser(self, database:IDatabase, name:str) -> IMutableUser:
        """ CreateCertificateUser(self: IUserFactory, database: IDatabase, name: str) -> IMutableUser """
        ...

    def CreateExternalProviderUser(self, database:IDatabase, name:str) -> IMutableUser:
        """ CreateExternalProviderUser(self: IUserFactory, database: IDatabase, name: str) -> IMutableUser """
        ...

    def CreateNoLoginUser(self, database:IDatabase, name:str) -> IMutableUser:
        """ CreateNoLoginUser(self: IUserFactory, database: IDatabase, name: str) -> IMutableUser """
        ...

    def CreateSqlLoginUser(self, database:IDatabase, name:str) -> IMutableUser:
        """ CreateSqlLoginUser(self: IUserFactory, database: IDatabase, name: str) -> IMutableUser """
        ...


class IVariableFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateCursorVariable(self, name:str) -> ICursorVariable:
        """ CreateCursorVariable(self: IVariableFactory, name: str) -> ICursorVariable """
        ...

    def CreateScalarVariable(self, name:str, dataType:IScalarDataType) -> IScalarVariable:
        """ CreateScalarVariable(self: IVariableFactory, name: str, dataType: IScalarDataType) -> IScalarVariable """
        ...

    def CreateTableVariable(self, name:str, dataType:ITableDataType) -> ITableVariable:
        """ CreateTableVariable(self: IVariableFactory, name: str, dataType: ITableDataType) -> ITableVariable """
        ...


class LoginCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IMutableMetadataCollection[ILogin]'>, <type 'IMetadataCollection[ILogin]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IEnumerable[ILogin]'>, <type 'object'>
    """
    LoginCollection(collationInfo: CollationInfo)
    LoginCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class MetadataDisplayInfoProvider(IMetadataDisplayInfoProvider): # skipped bases: <type 'object'>
    """ MetadataDisplayInfoProvider() """
    pass

class MetadataFactory(IMetadataFactory): # skipped bases: <type 'object'>
    """ MetadataFactory() """
    pass

class MetadataObjectBase(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: MetadataObjectBase) -> str """
        ...

    m_name = ...


class MetadataProviderBase(IMetadataProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class MetadataProviderEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MetadataProviderEventArgs() """
    pass

class MetadataProviderEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MetadataProviderEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MetadataProviderEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MetadataProviderEventHandler, sender: object, e: MetadataProviderEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MetadataProviderEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MetadataProviderEventArgs): # -> 
        """ Invoke(self: MetadataProviderEventHandler, sender: object, e: MetadataProviderEventArgs) """
        ...


class MetadataProviderUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetStoredProcParameters(storedProcText:str, metadataFactory:IMetadataFactory, dataTypeLookup:ISystemDataTypeLookup, collationInfo:CollationInfo, parseOptions:ParseOptions) -> IMetadataOrderedCollection:
        """ GetStoredProcParameters(storedProcText: str, metadataFactory: IMetadataFactory, dataTypeLookup: ISystemDataTypeLookup, collationInfo: CollationInfo, parseOptions: ParseOptions) -> IMetadataOrderedCollection[IParameter] """
        ...

    def Names(self, *args): #cannot find CLR method
        """ no doc """
        ...

    __all__: list = ...


class OrderedCollection(IMetadataOrderedCollection, OrderedCollectionBase): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[T]'>, <type 'IMutableMetadataCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IMutableMetadataOrderedCollection[T]'>, <type 'IMetadataOrderedCollection[T]'>, <type 'object'>
    """
    OrderedCollection[T](collationInfo: CollationInfo)
    OrderedCollection[T](initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class OrderedCollectionBase(IMutableMetadataOrderedCollection): # skipped bases: <type 'IMutableMetadataCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IMetadataOrderedCollection[T]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[T]'>, <type 'object'>
    """ no doc """
    @property
    def AsMetadataObjectCollection(self) -> IMetadataCollection:
        """ Get: AsMetadataObjectCollection(self: OrderedCollectionBase[T]) -> IMetadataCollection[IMetadataObject] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: OrderedCollectionBase[T]) -> int """
        ...


    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: OrderedCollectionBase[T], item: T) """
        ...

    def AddRange(self, items:IEnumerable): # -> 
        """ AddRange(self: OrderedCollectionBase[T], items: IEnumerable[T]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: OrderedCollectionBase[T]) """
        ...

    def Clone(self, copyData:bool = ...) -> IMutableMetadataCollection:
        """
        Clone(self: OrderedCollectionBase[T]) -> IMutableMetadataCollection[T]
        Clone(self: OrderedCollectionBase[T], copyData: bool) -> IMutableMetadataCollection[T]
        """
        ...

    def Contains(self, *__args:str) -> bool:
        """
        Contains(self: OrderedCollectionBase[T], name: str) -> bool
        Contains(self: OrderedCollectionBase[T], item: T) -> bool
        """
        ...

    def FindAll(self, *__args:Predicate) -> IEnumerable:
        """
        FindAll(self: OrderedCollectionBase[T], match: Predicate[T]) -> IEnumerable[T]
        FindAll(self: OrderedCollectionBase[T], name: str) -> IEnumerable[T]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: OrderedCollectionBase[T]) -> IEnumerator[T] """
        ...

    def Remove(self, *__args:str) -> bool:
        """
        Remove(self: OrderedCollectionBase[T], name: str) -> bool
        Remove(self: OrderedCollectionBase[T], item: T) -> bool
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ParameterCollection(OrderedCollection): # skipped bases: <type 'IMetadataCollection[IParameter]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IParameter]'>, <type 'IMetadataOrderedCollection[IParameter]'>, <type 'IEnumerable[IParameter]'>, <type 'IMutableMetadataOrderedCollection[IParameter]'>, <type 'IMetadataOrderedCollection[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ParameterCollection(collationInfo: CollationInfo)
    ParameterCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ScalarValuedFunctionCollection(TriTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[IScalarValuedFunction]'>, <type 'IMetadataCollection[ICallableModule]'>, <type 'IEnumerable[ICallableModule]'>, <type 'IEnumerable[IScalarFunction]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IScalarFunction]'>, <type 'IMutableMetadataCollection[IScalarValuedFunction]'>, <type 'IMetadataCollection[IScalarValuedFunction]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ScalarValuedFunctionCollection(collationInfo: CollationInfo)
    ScalarValuedFunctionCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ScalarVariableCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[ILocalVariable]'>, <type 'IEnumerable'>, <type 'IEnumerable[ILocalVariable]'>, <type 'IMutableMetadataCollection[IScalarVariable]'>, <type 'IMetadataCollection[IScalarVariable]'>, <type 'IEnumerable[IScalarVariable]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ScalarVariableCollection(collationInfo: CollationInfo)
    ScalarVariableCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class SchemaCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable[ISchema]'>, <type 'IMutableMetadataCollection[ISchema]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IDatabaseObject]'>, <type 'IEnumerable[IDatabaseObject]'>, <type 'IMetadataCollection[ISchema]'>, <type 'object'>
    """
    SchemaCollection(collationInfo: CollationInfo)
    SchemaCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ServerDdlTriggerCollection(SortedListCollection): # skipped bases: <type 'IMutableMetadataCollection[IServerDdlTrigger]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IEnumerable[IServerDdlTrigger]'>, <type 'IMetadataCollection[IServerDdlTrigger]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ServerDdlTriggerCollection(collationInfo: CollationInfo)
    ServerDdlTriggerCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class SortedListCollection(IMetadataCollection, DictionaryCollectionBase): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[T]'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'IMutableMetadataCollection[T]'>, <type 'object'>
    """ SortedListCollection[T](initialCapacity: int, collationInfo: CollationInfo) """
    pass

class StatisticsCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IStatistics]'>, <type 'IMutableMetadataCollection[IStatistics]'>, <type 'IEnumerable'>, <type 'IEnumerable[IStatistics]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    StatisticsCollection(collationInfo: CollationInfo)
    StatisticsCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class StoredProcedureCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IStoredProcedure]'>, <type 'IMetadataCollection[ICallableModule]'>, <type 'IEnumerable[ICallableModule]'>, <type 'IEnumerable'>, <type 'IEnumerable[IStoredProcedure]'>, <type 'IMutableMetadataCollection[IStoredProcedure]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    StoredProcedureCollection(collationInfo: CollationInfo)
    StoredProcedureCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class SynonymCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[ISynonym]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[ISynonym]'>, <type 'IMutableMetadataCollection[ISynonym]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    SynonymCollection(collationInfo: CollationInfo)
    SynonymCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class SystemDataTypeLookupBase(ISystemDataTypeLookup): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BigInt(self) -> ISystemDataType:
        """ Get: BigInt(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Bit(self) -> ISystemDataType:
        """ Get: Bit(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Date(self) -> ISystemDataType:
        """ Get: Date(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def DateTime(self) -> ISystemDataType:
        """ Get: DateTime(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Float(self) -> ISystemDataType:
        """ Get: Float(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Geography(self) -> ISystemDataType:
        """ Get: Geography(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Geometry(self) -> ISystemDataType:
        """ Get: Geometry(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def HierarchyId(self) -> ISystemDataType:
        """ Get: HierarchyId(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Image(self) -> ISystemDataType:
        """ Get: Image(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Int(self) -> ISystemDataType:
        """ Get: Int(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Money(self) -> ISystemDataType:
        """ Get: Money(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def NText(self) -> ISystemDataType:
        """ Get: NText(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def NVarCharMax(self) -> ISystemDataType:
        """ Get: NVarCharMax(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Real(self) -> ISystemDataType:
        """ Get: Real(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def SmallDateTime(self) -> ISystemDataType:
        """ Get: SmallDateTime(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def SmallInt(self) -> ISystemDataType:
        """ Get: SmallInt(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def SmallMoney(self) -> ISystemDataType:
        """ Get: SmallMoney(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def SysName(self) -> ISystemDataType:
        """ Get: SysName(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Text(self) -> ISystemDataType:
        """ Get: Text(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Timestamp(self) -> ISystemDataType:
        """ Get: Timestamp(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def TinyInt(self) -> ISystemDataType:
        """ Get: TinyInt(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def UniqueIdentifier(self) -> ISystemDataType:
        """ Get: UniqueIdentifier(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def VarBinaryMax(self) -> ISystemDataType:
        """ Get: VarBinaryMax(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def VarCharMax(self) -> ISystemDataType:
        """ Get: VarCharMax(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...

    @property
    def Variant(self) -> ISystemDataType:
        """ Get: Variant(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...


    def Binary(self, maxLength:int = ...) -> ISystemDataType:
        """
        Binary(self: SystemDataTypeLookupBase) -> ISystemDataType
        Binary(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def Char(self, maxLength:int = ...) -> ISystemDataType:
        """
        Char(self: SystemDataTypeLookupBase) -> ISystemDataType
        Char(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def DateTime2(self, scale:int = ...) -> ISystemDataType:
        """
        DateTime2(self: SystemDataTypeLookupBase) -> ISystemDataType
        DateTime2(self: SystemDataTypeLookupBase, scale: int) -> ISystemDataType
        """
        ...

    def DateTimeOffset(self, scale:int = ...) -> ISystemDataType:
        """
        DateTimeOffset(self: SystemDataTypeLookupBase) -> ISystemDataType
        DateTimeOffset(self: SystemDataTypeLookupBase, scale: int) -> ISystemDataType
        """
        ...

    def Decimal(self, precision:int = ..., scale:int = ...) -> ISystemDataType:
        """
        Decimal(self: SystemDataTypeLookupBase) -> ISystemDataType
        Decimal(self: SystemDataTypeLookupBase, precision: int) -> ISystemDataType
        Decimal(self: SystemDataTypeLookupBase, precision: int, scale: int) -> ISystemDataType
        """
        ...

    def NChar(self, maxLength:int = ...) -> ISystemDataType:
        """
        NChar(self: SystemDataTypeLookupBase) -> ISystemDataType
        NChar(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def Numeric(self, precision:int = ..., scale:int = ...) -> ISystemDataType:
        """
        Numeric(self: SystemDataTypeLookupBase) -> ISystemDataType
        Numeric(self: SystemDataTypeLookupBase, precision: int) -> ISystemDataType
        Numeric(self: SystemDataTypeLookupBase, precision: int, scale: int) -> ISystemDataType
        """
        ...

    def NVarChar(self, maxLength:int = ...) -> ISystemDataType:
        """
        NVarChar(self: SystemDataTypeLookupBase) -> ISystemDataType
        NVarChar(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def Time(self, scale:int = ...) -> ISystemDataType:
        """
        Time(self: SystemDataTypeLookupBase) -> ISystemDataType
        Time(self: SystemDataTypeLookupBase, scale: int) -> ISystemDataType
        """
        ...

    def VarBinary(self, maxLength:int = ...) -> ISystemDataType:
        """
        VarBinary(self: SystemDataTypeLookupBase) -> ISystemDataType
        VarBinary(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def VarChar(self, maxLength:int = ...) -> ISystemDataType:
        """
        VarChar(self: SystemDataTypeLookupBase) -> ISystemDataType
        VarChar(self: SystemDataTypeLookupBase, maxLength: int) -> ISystemDataType
        """
        ...

    def Xml(self) -> ISystemDataType:
        """ Xml(self: SystemDataTypeLookupBase) -> ISystemDataType """
        ...


class TableCollection(TriTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IDatabaseTable]'>, <type 'IMetadataCollection[ITable]'>, <type 'IEnumerable[ITabular]'>, <type 'IEnumerable'>, <type 'IEnumerable[ITable]'>, <type 'IEnumerable[IDatabaseTable]'>, <type 'IMutableMetadataCollection[ITable]'>, <type 'IMetadataCollection[ITabular]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    TableCollection(collationInfo: CollationInfo)
    TableCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class TableValuedFunctionCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[ITableValuedFunction]'>, <type 'IEnumerable[ITabular]'>, <type 'IMutableMetadataCollection[ITableValuedFunction]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[ITableValuedFunction]'>, <type 'IMetadataCollection[ITabular]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    TableValuedFunctionCollection(collationInfo: CollationInfo)
    TableValuedFunctionCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class TableVariableCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[ILocalVariable]'>, <type 'IMutableMetadataCollection[ITableVariable]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[ITableVariable]'>, <type 'IEnumerable[ILocalVariable]'>, <type 'IEnumerable[ITableVariable]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    TableVariableCollection(collationInfo: CollationInfo)
    TableVariableCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class TabularCollection(SortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[ITabular]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[ITabular]'>, <type 'IMetadataCollection[ITabular]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    TabularCollection(collationInfo: CollationInfo)
    TabularCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class TriTypeSortedListCollection(IMetadataCollection, DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[B1]'>, <type 'IMetadataCollection[B1]'>, <type 'IMetadataCollection[T]'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'IMutableMetadataCollection[T]'>, <type 'IEnumerable[B2]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """ TriTypeSortedListCollection[T, B1, B2](initialCapacity: int, collationInfo: CollationInfo) """
    pass

class UdtMemberCollectionBase(DualTypeSortedListCollection): # skipped bases: <type 'IMutableMetadataCollection[T]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IUdtMember]'>, <type 'IMetadataCollection[T]'>, <type 'IEnumerable[T]'>, <type 'IEnumerable[IUdtMember]'>, <type 'object'>
    """ no doc """
    pass

class UdtMethodCollection(UdtMemberCollectionBase): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable[IUdtMember]'>, <type 'IMetadataCollection[IUdtMethod]'>, <type 'IEnumerable'>, <type 'IMetadataCollection[IUdtMember]'>, <type 'IEnumerable[IUdtMethod]'>, <type 'IMutableMetadataCollection[IUdtMethod]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    UdtMethodCollection()
    UdtMethodCollection(initialCapacity: int)
    """
    pass

class UserCollection(DualTypeSortedListCollection): # skipped bases: <type 'IMutableMetadataCollection[IUser]'>, <type 'IMetadataCollection[IUser]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IEnumerable[IUser]'>, <type 'IMetadataCollection[IDatabasePrincipal]'>, <type 'IEnumerable[IDatabasePrincipal]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    UserCollection(collationInfo: CollationInfo)
    UserCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class UserDefinedAggregateCollection(SortedListCollection): # skipped bases: <type 'IMetadataCollection[IUserDefinedAggregate]'>, <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IMutableMetadataCollection[IUserDefinedAggregate]'>, <type 'IEnumerable[IUserDefinedAggregate]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    UserDefinedAggregateCollection(collationInfo: CollationInfo)
    UserDefinedAggregateCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class UserDefinedClrTypeCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'IEnumerable[IUserDefinedClrType]'>, <type 'IEnumerable'>, <type 'IEnumerable[IUserDefinedType]'>, <type 'IMetadataCollection[IUserDefinedClrType]'>, <type 'IMetadataCollection[IUserDefinedType]'>, <type 'IMutableMetadataCollection[IUserDefinedClrType]'>, <type 'object'>
    """
    UserDefinedClrTypeCollection(collationInfo: CollationInfo)
    UserDefinedClrTypeCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class UserDefinedDataTypeCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IEnumerable'>, <type 'IEnumerable[IUserDefinedType]'>, <type 'IMetadataCollection[IUserDefinedDataType]'>, <type 'IEnumerable[IUserDefinedDataType]'>, <type 'IMetadataCollection[IUserDefinedType]'>, <type 'IMutableMetadataCollection[IUserDefinedDataType]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    UserDefinedDataTypeCollection(collationInfo: CollationInfo)
    UserDefinedDataTypeCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class UserDefinedTableTypeCollection(DualTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMutableMetadataCollection[IUserDefinedTableType]'>, <type 'IEnumerable'>, <type 'IEnumerable[IUserDefinedType]'>, <type 'IEnumerable[IUserDefinedTableType]'>, <type 'IMetadataCollection[IUserDefinedTableType]'>, <type 'IMetadataCollection[IUserDefinedType]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    UserDefinedTableTypeCollection(collationInfo: CollationInfo)
    UserDefinedTableTypeCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

class ViewCollection(TriTypeSortedListCollection): # skipped bases: <type 'IEnumerable[IMetadataObject]'>, <type 'IMetadataCollection[IDatabaseTable]'>, <type 'IEnumerable[ITabular]'>, <type 'IEnumerable'>, <type 'IEnumerable[IDatabaseTable]'>, <type 'IMetadataCollection[IView]'>, <type 'IEnumerable[IView]'>, <type 'IMetadataCollection[ITabular]'>, <type 'IMutableMetadataCollection[IView]'>, <type 'IMetadataCollection[IMetadataObject]'>, <type 'object'>
    """
    ViewCollection(collationInfo: CollationInfo)
    ViewCollection(initialCapacity: int, collationInfo: CollationInfo)
    """
    pass

