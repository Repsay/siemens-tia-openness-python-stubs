# encoding: utf-8
# module System.Data.EntityClient calls itself EntityClient
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IServiceProvider

from System.Data import DbType, IExtendedDataRecord

from System.Data.Common import (DbCommand, DbConnection, 
    DbConnectionStringBuilder, DbDataReader, DbParameter, 
    DbParameterCollection, DbProviderFactory, DbTransaction)

from System.Data.Common.CommandTrees import DbCommandTree

from System.Data.Metadata.Edm import EdmType, MetadataWorkspace

from typing import Self


# no functions
# classes

class EntityCommand(DbCommand): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbCommand'>, <type 'object'>
    """
    EntityCommand()
    EntityCommand(statement: str)
    EntityCommand(statement: str, connection: EntityConnection)
    EntityCommand(statement: str, connection: EntityConnection, transaction: EntityTransaction)
    """
    @property
    def CommandTree(self) -> DbCommandTree:
        """
        Get: CommandTree(self: EntityCommand) -> DbCommandTree
        Set: CommandTree(self: EntityCommand) = value
        """
        ...

    @property
    def EnablePlanCaching(self) -> bool:
        """
        Get: EnablePlanCaching(self: EntityCommand) -> bool
        Set: EnablePlanCaching(self: EntityCommand) = value
        """
        ...


    def ToTraceString(self) -> str:
        """ ToTraceString(self: EntityCommand) -> str """
        ...

    def __new__(cls, statement:str = ..., connection:EntityConnection = ..., transaction:EntityTransaction = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, statement: str)
        __new__(cls: type, statement: str, connection: EntityConnection)
        __new__(cls: type, statement: str, connection: EntityConnection, transaction: EntityTransaction)
        """
        ...


class EntityConnection(DbConnection): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbConnection'>, <type 'object'>
    """
    EntityConnection()
    EntityConnection(connectionString: str)
    EntityConnection(workspace: MetadataWorkspace, connection: DbConnection)
    """
    @property
    def StoreConnection(self) -> DbConnection:
        """ Get: StoreConnection(self: EntityConnection) -> DbConnection """
        ...


    def GetMetadataWorkspace(self) -> MetadataWorkspace:
        """ GetMetadataWorkspace(self: EntityConnection) -> MetadataWorkspace """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionString: str)
        __new__(cls: type, workspace: MetadataWorkspace, connection: DbConnection)
        """
        ...


class EntityConnectionStringBuilder(DbConnectionStringBuilder): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    EntityConnectionStringBuilder()
    EntityConnectionStringBuilder(connectionString: str)
    """
    @property
    def Metadata(self) -> str:
        """
        Get: Metadata(self: EntityConnectionStringBuilder) -> str
        Set: Metadata(self: EntityConnectionStringBuilder) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EntityConnectionStringBuilder) -> str
        Set: Name(self: EntityConnectionStringBuilder) = value
        """
        ...

    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: EntityConnectionStringBuilder) -> str
        Set: Provider(self: EntityConnectionStringBuilder) = value
        """
        ...

    @property
    def ProviderConnectionString(self) -> str:
        """
        Get: ProviderConnectionString(self: EntityConnectionStringBuilder) -> str
        Set: ProviderConnectionString(self: EntityConnectionStringBuilder) = value
        """
        ...



class EntityDataReader(DbDataReader, IExtendedDataRecord): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class EntityParameter(DbParameter): # skipped bases: <type 'IDataParameter'>, <type 'IDbDataParameter'>, <type 'object'>
    """
    EntityParameter()
    EntityParameter(parameterName: str, dbType: DbType)
    EntityParameter(parameterName: str, dbType: DbType, size: int)
    EntityParameter(parameterName: str, dbType: DbType, size: int, sourceColumn: str)
    EntityParameter(parameterName: str, dbType: DbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, value: object)
    """
    @property
    def EdmType(self) -> EdmType:
        """
        Get: EdmType(self: EntityParameter) -> EdmType
        Set: EdmType(self: EntityParameter) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: EntityParameter) -> str """
        ...

    def __new__(cls, parameterName:str = ..., dbType:DbType = ..., size:int = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str, dbType: DbType)
        __new__(cls: type, parameterName: str, dbType: DbType, size: int)
        __new__(cls: type, parameterName: str, dbType: DbType, size: int, sourceColumn: str)
        __new__(cls: type, parameterName: str, dbType: DbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, value: object)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class EntityParameterCollection(DbParameterCollection): # skipped bases: <type 'IDataParameterCollection'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def AddWithValue(self, parameterName:str, value:object) -> EntityParameter:
        """ AddWithValue(self: EntityParameterCollection, parameterName: str, value: object) -> EntityParameter """
        ...


class EntityProviderFactory(IServiceProvider, DbProviderFactory): # skipped bases: <type 'object'>
    """ no doc """
    Instance: EntityProviderFactory = ...


class EntityTransaction(DbTransaction): # skipped bases: <type 'IDisposable'>, <type 'IDbTransaction'>, <type 'object'>
    """ no doc """
    pass

