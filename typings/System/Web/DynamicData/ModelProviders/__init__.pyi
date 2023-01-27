# encoding: utf-8
# module System.Web.DynamicData.ModelProviders calls itself ModelProviders
# from System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Type

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import AttributeCollection, ICustomTypeDescriptor

from System.Linq import IQueryable

from System.Reflection import PropertyInfo

from System.Security.Principal import IPrincipal

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AssociationDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AssociationDirection, values: ManyToMany (3), ManyToOne (2), OneToMany (1), OneToOne (0) """
    ManyToMany: AssociationDirection = ...
    ManyToOne: AssociationDirection = ...
    OneToMany: AssociationDirection = ...
    OneToOne: AssociationDirection = ...
    value__ = ...


class AssociationProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Direction(self) -> AssociationDirection:
        """ Get: Direction(self: AssociationProvider) -> AssociationDirection """
        ...

    @property
    def ForeignKeyNames(self) -> ReadOnlyCollection:
        """ Get: ForeignKeyNames(self: AssociationProvider) -> ReadOnlyCollection[str] """
        ...

    @property
    def FromColumn(self) -> ColumnProvider:
        """ Get: FromColumn(self: AssociationProvider) -> ColumnProvider """
        ...

    @property
    def IsPrimaryKeyInThisTable(self) -> bool:
        """ Get: IsPrimaryKeyInThisTable(self: AssociationProvider) -> bool """
        ...

    @property
    def ToColumn(self) -> ColumnProvider:
        """ Get: ToColumn(self: AssociationProvider) -> ColumnProvider """
        ...

    @property
    def ToTable(self) -> TableProvider:
        """ Get: ToTable(self: AssociationProvider) -> TableProvider """
        ...


    def GetSortExpression(self, sortColumn:ColumnProvider) -> str:
        """ GetSortExpression(self: AssociationProvider, sortColumn: ColumnProvider) -> str """
        ...


class ColumnProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Association(self) -> AssociationProvider:
        """ Get: Association(self: ColumnProvider) -> AssociationProvider """
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: ColumnProvider) -> AttributeCollection """
        ...

    @property
    def ColumnType(self) -> Type:
        """ Get: ColumnType(self: ColumnProvider) -> Type """
        ...

    @property
    def EntityTypeProperty(self) -> PropertyInfo:
        """ Get: EntityTypeProperty(self: ColumnProvider) -> PropertyInfo """
        ...

    @property
    def IsCustomProperty(self) -> bool:
        """ Get: IsCustomProperty(self: ColumnProvider) -> bool """
        ...

    @property
    def IsForeignKeyComponent(self) -> bool:
        """ Get: IsForeignKeyComponent(self: ColumnProvider) -> bool """
        ...

    @property
    def IsGenerated(self) -> bool:
        """ Get: IsGenerated(self: ColumnProvider) -> bool """
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        """ Get: IsPrimaryKey(self: ColumnProvider) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ColumnProvider) -> bool """
        ...

    @property
    def IsSortable(self) -> bool:
        """ Get: IsSortable(self: ColumnProvider) -> bool """
        ...

    @property
    def MaxLength(self) -> int:
        """ Get: MaxLength(self: ColumnProvider) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ColumnProvider) -> str """
        ...

    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: ColumnProvider) -> bool """
        ...

    @property
    def Table(self) -> TableProvider:
        """ Get: Table(self: ColumnProvider) -> TableProvider """
        ...


    def AddDefaultAttributes(self, *args): #cannot find CLR method
        """ AddDefaultAttributes(columnProvider: ColumnProvider, attributes: AttributeCollection) -> AttributeCollection """
        ...

    def ToString(self) -> str:
        """ ToString(self: ColumnProvider) -> str """
        ...


class DataModelProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContextType(self) -> Type:
        """ Get: ContextType(self: DataModelProvider) -> Type """
        ...

    @property
    def Tables(self) -> ReadOnlyCollection:
        """ Get: Tables(self: DataModelProvider) -> ReadOnlyCollection[TableProvider] """
        ...


    def CreateContext(self) -> object:
        """ CreateContext(self: DataModelProvider) -> object """
        ...


class TableProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: TableProvider) -> AttributeCollection """
        ...

    @property
    def Columns(self) -> ReadOnlyCollection:
        """ Get: Columns(self: TableProvider) -> ReadOnlyCollection[ColumnProvider] """
        ...

    @property
    def DataContextPropertyName(self) -> str:
        """ Get: DataContextPropertyName(self: TableProvider) -> str """
        ...

    @property
    def DataModel(self) -> DataModelProvider:
        """ Get: DataModel(self: TableProvider) -> DataModelProvider """
        ...

    @property
    def EntityType(self) -> Type:
        """ Get: EntityType(self: TableProvider) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TableProvider) -> str """
        ...

    @property
    def ParentEntityType(self) -> Type:
        """ Get: ParentEntityType(self: TableProvider) -> Type """
        ...

    @property
    def RootEntityType(self) -> Type:
        """ Get: RootEntityType(self: TableProvider) -> Type """
        ...


    def CanDelete(self, principal:IPrincipal) -> bool:
        """ CanDelete(self: TableProvider, principal: IPrincipal) -> bool """
        ...

    def CanInsert(self, principal:IPrincipal) -> bool:
        """ CanInsert(self: TableProvider, principal: IPrincipal) -> bool """
        ...

    def CanRead(self, principal:IPrincipal) -> bool:
        """ CanRead(self: TableProvider, principal: IPrincipal) -> bool """
        ...

    def CanUpdate(self, principal:IPrincipal) -> bool:
        """ CanUpdate(self: TableProvider, principal: IPrincipal) -> bool """
        ...

    def EvaluateForeignKey(self, row:object, foreignKeyName:str) -> object:
        """ EvaluateForeignKey(self: TableProvider, row: object, foreignKeyName: str) -> object """
        ...

    def GetQuery(self, context:object) -> IQueryable:
        """ GetQuery(self: TableProvider, context: object) -> IQueryable """
        ...

    def GetTypeDescriptor(self) -> ICustomTypeDescriptor:
        """ GetTypeDescriptor(self: TableProvider) -> ICustomTypeDescriptor """
        ...

    def ToString(self) -> str:
        """ ToString(self: TableProvider) -> str """
        ...


