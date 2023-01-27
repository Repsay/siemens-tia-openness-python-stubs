# encoding: utf-8
# module System.ComponentModel.Design.Data calls itself Data
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum

from System.CodeDom import CodeExpression

from System.Collections import CollectionBase, ICollection

from System.ComponentModel.Design import IDesignerHost

from System.Data import DbType, ParameterDirection

from System.Data.Common import DbConnection

from System.Drawing import Bitmap

from System.Windows.Forms import FormStartPosition, IWin32Window

"""The following names are not found in the module: field#
"""

# no functions
# classes

class DataSourceDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Image(self) -> Bitmap:
        """ Get: Image(self: DataSourceDescriptor) -> Bitmap """
        ...

    @property
    def IsDesignable(self) -> bool:
        """ Get: IsDesignable(self: DataSourceDescriptor) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataSourceDescriptor) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: DataSourceDescriptor) -> str """
        ...



class DataSourceDescriptorCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataSourceDescriptorCollection() """
    def Add(self, value:DataSourceDescriptor) -> int:
        """ Add(self: DataSourceDescriptorCollection, value: DataSourceDescriptor) -> int """
        ...

    def Contains(self, value:DataSourceDescriptor) -> bool:
        """ Contains(self: DataSourceDescriptorCollection, value: DataSourceDescriptor) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DataSourceDescriptorCollection, array: Array[DataSourceDescriptor], index: int) """
        ...

    def IndexOf(self, value:DataSourceDescriptor) -> int:
        """ IndexOf(self: DataSourceDescriptorCollection, value: DataSourceDescriptor) -> int """
        ...

    def Insert(self, index:int, value:DataSourceDescriptor): # -> 
        """ Insert(self: DataSourceDescriptorCollection, index: int, value: DataSourceDescriptor) """
        ...

    def Remove(self, value:DataSourceDescriptor): # -> 
        """ Remove(self: DataSourceDescriptorCollection, value: DataSourceDescriptor) """
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


class DataSourceGroup: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DataSources(self) -> DataSourceDescriptorCollection:
        """ Get: DataSources(self: DataSourceGroup) -> DataSourceDescriptorCollection """
        ...

    @property
    def Image(self) -> Bitmap:
        """ Get: Image(self: DataSourceGroup) -> Bitmap """
        ...

    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: DataSourceGroup) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataSourceGroup) -> str """
        ...



class DataSourceGroupCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataSourceGroupCollection() """
    def Add(self, value:DataSourceGroup) -> int:
        """ Add(self: DataSourceGroupCollection, value: DataSourceGroup) -> int """
        ...

    def Contains(self, value:DataSourceGroup) -> bool:
        """ Contains(self: DataSourceGroupCollection, value: DataSourceGroup) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DataSourceGroupCollection, array: Array[DataSourceGroup], index: int) """
        ...

    def IndexOf(self, value:DataSourceGroup) -> int:
        """ IndexOf(self: DataSourceGroupCollection, value: DataSourceGroup) -> int """
        ...

    def Insert(self, index:int, value:DataSourceGroup): # -> 
        """ Insert(self: DataSourceGroupCollection, index: int, value: DataSourceGroup) """
        ...

    def Remove(self, value:DataSourceGroup): # -> 
        """ Remove(self: DataSourceGroupCollection, value: DataSourceGroup) """
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


class DataSourceProviderService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SupportsAddNewDataSource(self) -> bool:
        """ Get: SupportsAddNewDataSource(self: DataSourceProviderService) -> bool """
        ...

    @property
    def SupportsConfigureDataSource(self) -> bool:
        """ Get: SupportsConfigureDataSource(self: DataSourceProviderService) -> bool """
        ...


    def AddDataSourceInstance(self, host:IDesignerHost, dataSourceDescriptor:DataSourceDescriptor) -> object:
        """ AddDataSourceInstance(self: DataSourceProviderService, host: IDesignerHost, dataSourceDescriptor: DataSourceDescriptor) -> object """
        ...

    def GetDataSources(self) -> DataSourceGroupCollection:
        """ GetDataSources(self: DataSourceProviderService) -> DataSourceGroupCollection """
        ...

    def InvokeAddNewDataSource(self, parentWindow:IWin32Window, startPosition:FormStartPosition) -> DataSourceGroup:
        """ InvokeAddNewDataSource(self: DataSourceProviderService, parentWindow: IWin32Window, startPosition: FormStartPosition) -> DataSourceGroup """
        ...

    def InvokeConfigureDataSource(self, parentWindow:IWin32Window, startPosition:FormStartPosition, dataSourceDescriptor:DataSourceDescriptor) -> bool:
        """ InvokeConfigureDataSource(self: DataSourceProviderService, parentWindow: IWin32Window, startPosition: FormStartPosition, dataSourceDescriptor: DataSourceDescriptor) -> bool """
        ...

    def NotifyDataSourceComponentAdded(self, dsc:object): # -> 
        """ NotifyDataSourceComponentAdded(self: DataSourceProviderService, dsc: object) """
        ...


class DesignerDataColumn: # skipped bases: <type 'object'>, <type 'object'>
    """
    DesignerDataColumn(name: str, dataType: DbType)
    DesignerDataColumn(name: str, dataType: DbType, defaultValue: object)
    DesignerDataColumn(name: str, dataType: DbType, defaultValue: object, identity: bool, nullable: bool, primaryKey: bool, precision: int, scale: int, length: int)
    """
    @property
    def DataType(self) -> DbType:
        """ Get: DataType(self: DesignerDataColumn) -> DbType """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: DesignerDataColumn) -> object """
        ...

    @property
    def Identity(self) -> bool:
        """ Get: Identity(self: DesignerDataColumn) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: DesignerDataColumn) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataColumn) -> str """
        ...

    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: DesignerDataColumn) -> bool """
        ...

    @property
    def Precision(self) -> int:
        """ Get: Precision(self: DesignerDataColumn) -> int """
        ...

    @property
    def PrimaryKey(self) -> bool:
        """ Get: PrimaryKey(self: DesignerDataColumn) -> bool """
        ...

    @property
    def Scale(self) -> int:
        """ Get: Scale(self: DesignerDataColumn) -> int """
        ...



class DesignerDataConnection: # skipped bases: <type 'object'>, <type 'object'>
    """
    DesignerDataConnection(name: str, providerName: str, connectionString: str)
    DesignerDataConnection(name: str, providerName: str, connectionString: str, isConfigured: bool)
    """
    @property
    def ConnectionString(self) -> str:
        """ Get: ConnectionString(self: DesignerDataConnection) -> str """
        ...

    @property
    def IsConfigured(self) -> bool:
        """ Get: IsConfigured(self: DesignerDataConnection) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataConnection) -> str """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: DesignerDataConnection) -> str """
        ...



class DesignerDataParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerDataParameter(name: str, dataType: DbType, direction: ParameterDirection) """
    @property
    def DataType(self) -> DbType:
        """ Get: DataType(self: DesignerDataParameter) -> DbType """
        ...

    @property
    def Direction(self) -> ParameterDirection:
        """ Get: Direction(self: DesignerDataParameter) -> ParameterDirection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataParameter) -> str """
        ...



class DesignerDataRelationship: # skipped bases: <type 'object'>, <type 'object'>
    """ DesignerDataRelationship(name: str, parentColumns: ICollection, childTable: DesignerDataTable, childColumns: ICollection) """
    @property
    def ChildColumns(self) -> ICollection:
        """ Get: ChildColumns(self: DesignerDataRelationship) -> ICollection """
        ...

    @property
    def ChildTable(self) -> DesignerDataTable:
        """ Get: ChildTable(self: DesignerDataRelationship) -> DesignerDataTable """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataRelationship) -> str """
        ...

    @property
    def ParentColumns(self) -> ICollection:
        """ Get: ParentColumns(self: DesignerDataRelationship) -> ICollection """
        ...



class DesignerDataSchemaClass: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    StoredProcedures: DesignerDataSchemaClass = ...
    Tables: DesignerDataSchemaClass = ...
    Views: DesignerDataSchemaClass = ...


class DesignerDataStoredProcedure: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataStoredProcedure) -> str """
        ...

    @property
    def Owner(self) -> str:
        """ Get: Owner(self: DesignerDataStoredProcedure) -> str """
        ...

    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: DesignerDataStoredProcedure) -> ICollection """
        ...


    def CreateParameters(self, *args): #cannot find CLR method
        """ CreateParameters(self: DesignerDataStoredProcedure) -> ICollection """
        ...


class DesignerDataTableBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> ICollection:
        """ Get: Columns(self: DesignerDataTableBase) -> ICollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataTableBase) -> str """
        ...

    @property
    def Owner(self) -> str:
        """ Get: Owner(self: DesignerDataTableBase) -> str """
        ...


    def CreateColumns(self, *args): #cannot find CLR method
        """ CreateColumns(self: DesignerDataTableBase) -> ICollection """
        ...


class DesignerDataTable(DesignerDataTableBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Relationships(self) -> ICollection:
        """ Get: Relationships(self: DesignerDataTable) -> ICollection """
        ...


    def CreateRelationships(self, *args): #cannot find CLR method
        """ CreateRelationships(self: DesignerDataTable) -> ICollection """
        ...


class DesignerDataView(DesignerDataTableBase): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDataEnvironment: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connections(self) -> ICollection:
        """ Get: Connections(self: IDataEnvironment) -> ICollection """
        ...


    def BuildConnection(self, owner:IWin32Window, initialConnection:DesignerDataConnection) -> DesignerDataConnection:
        """ BuildConnection(self: IDataEnvironment, owner: IWin32Window, initialConnection: DesignerDataConnection) -> DesignerDataConnection """
        ...

    def BuildQuery(self, owner:IWin32Window, connection:DesignerDataConnection, mode:QueryBuilderMode, initialQueryText:str) -> str:
        """ BuildQuery(self: IDataEnvironment, owner: IWin32Window, connection: DesignerDataConnection, mode: QueryBuilderMode, initialQueryText: str) -> str """
        ...

    def ConfigureConnection(self, owner:IWin32Window, connection:DesignerDataConnection, name:str) -> DesignerDataConnection:
        """ ConfigureConnection(self: IDataEnvironment, owner: IWin32Window, connection: DesignerDataConnection, name: str) -> DesignerDataConnection """
        ...

    def GetCodeExpression(self, connection:DesignerDataConnection) -> CodeExpression:
        """ GetCodeExpression(self: IDataEnvironment, connection: DesignerDataConnection) -> CodeExpression """
        ...

    def GetConnectionSchema(self, connection:DesignerDataConnection) -> IDesignerDataSchema:
        """ GetConnectionSchema(self: IDataEnvironment, connection: DesignerDataConnection) -> IDesignerDataSchema """
        ...

    def GetDesignTimeConnection(self, connection:DesignerDataConnection) -> DbConnection:
        """ GetDesignTimeConnection(self: IDataEnvironment, connection: DesignerDataConnection) -> DbConnection """
        ...


class IDesignerDataSchema: # skipped bases: <type 'object'>
    """ no doc """
    def GetSchemaItems(self, schemaClass:DesignerDataSchemaClass) -> ICollection:
        """ GetSchemaItems(self: IDesignerDataSchema, schemaClass: DesignerDataSchemaClass) -> ICollection """
        ...

    def SupportsSchemaClass(self, schemaClass:DesignerDataSchemaClass) -> bool:
        """ SupportsSchemaClass(self: IDesignerDataSchema, schemaClass: DesignerDataSchemaClass) -> bool """
        ...


class QueryBuilderMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueryBuilderMode, values: Delete (3), Insert (2), Select (0), Update (1) """
    Delete: QueryBuilderMode = ...
    Insert: QueryBuilderMode = ...
    Select: QueryBuilderMode = ...
    Update: QueryBuilderMode = ...
    value__ = ...


