# encoding: utf-8
# module System.Data.Linq.Mapping calls itself Mapping
# from System.Data.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, Type

from System.Collections import IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IO import Stream

from System.Reflection import MemberInfo, MethodInfo, ParameterInfo

from System.Xml import XmlReader

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class DataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: DataAttribute) -> str
        Set: Name(self: DataAttribute) = value
        """
        ...

    @property
    def Storage(self) -> str:
        """
        Get: Storage(self: DataAttribute) -> str
        Set: Storage(self: DataAttribute) = value
        """
        ...



class AssociationAttribute(DataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssociationAttribute() """
    @property
    def DeleteOnNull(self) -> bool:
        """
        Get: DeleteOnNull(self: AssociationAttribute) -> bool
        Set: DeleteOnNull(self: AssociationAttribute) = value
        """
        ...

    @property
    def DeleteRule(self) -> str:
        """
        Get: DeleteRule(self: AssociationAttribute) -> str
        Set: DeleteRule(self: AssociationAttribute) = value
        """
        ...

    @property
    def IsForeignKey(self) -> bool:
        """
        Get: IsForeignKey(self: AssociationAttribute) -> bool
        Set: IsForeignKey(self: AssociationAttribute) = value
        """
        ...

    @property
    def IsUnique(self) -> bool:
        """
        Get: IsUnique(self: AssociationAttribute) -> bool
        Set: IsUnique(self: AssociationAttribute) = value
        """
        ...

    @property
    def OtherKey(self) -> str:
        """
        Get: OtherKey(self: AssociationAttribute) -> str
        Set: OtherKey(self: AssociationAttribute) = value
        """
        ...

    @property
    def ThisKey(self) -> str:
        """
        Get: ThisKey(self: AssociationAttribute) -> str
        Set: ThisKey(self: AssociationAttribute) = value
        """
        ...



class MappingSource: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateModel(self, *args): #cannot find CLR method
        """ CreateModel(self: MappingSource, dataContextType: Type) -> MetaModel """
        ...

    def GetModel(self, dataContextType:Type) -> MetaModel:
        """ GetModel(self: MappingSource, dataContextType: Type) -> MetaModel """
        ...


class AttributeMappingSource(MappingSource): # skipped bases: <type 'object'>
    """ AttributeMappingSource() """
    pass

class AutoSync(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AutoSync, values: Always (1), Default (0), Never (2), OnInsert (3), OnUpdate (4) """
    Always: AutoSync = ...
    Default: AutoSync = ...
    Never: AutoSync = ...
    OnInsert: AutoSync = ...
    OnUpdate: AutoSync = ...
    value__ = ...


class ColumnAttribute(DataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ColumnAttribute() """
    @property
    def AutoSync(self) -> AutoSync:
        """
        Get: AutoSync(self: ColumnAttribute) -> AutoSync
        Set: AutoSync(self: ColumnAttribute) = value
        """
        ...

    @property
    def CanBeNull(self) -> bool:
        """
        Get: CanBeNull(self: ColumnAttribute) -> bool
        Set: CanBeNull(self: ColumnAttribute) = value
        """
        ...

    @property
    def DbType(self) -> str:
        """
        Get: DbType(self: ColumnAttribute) -> str
        Set: DbType(self: ColumnAttribute) = value
        """
        ...

    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: ColumnAttribute) -> str
        Set: Expression(self: ColumnAttribute) = value
        """
        ...

    @property
    def IsDbGenerated(self) -> bool:
        """
        Get: IsDbGenerated(self: ColumnAttribute) -> bool
        Set: IsDbGenerated(self: ColumnAttribute) = value
        """
        ...

    @property
    def IsDiscriminator(self) -> bool:
        """
        Get: IsDiscriminator(self: ColumnAttribute) -> bool
        Set: IsDiscriminator(self: ColumnAttribute) = value
        """
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        """
        Get: IsPrimaryKey(self: ColumnAttribute) -> bool
        Set: IsPrimaryKey(self: ColumnAttribute) = value
        """
        ...

    @property
    def IsVersion(self) -> bool:
        """
        Get: IsVersion(self: ColumnAttribute) -> bool
        Set: IsVersion(self: ColumnAttribute) = value
        """
        ...

    @property
    def UpdateCheck(self) -> UpdateCheck:
        """
        Get: UpdateCheck(self: ColumnAttribute) -> UpdateCheck
        Set: UpdateCheck(self: ColumnAttribute) = value
        """
        ...



class DatabaseAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DatabaseAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: DatabaseAttribute) -> str
        Set: Name(self: DatabaseAttribute) = value
        """
        ...



class FunctionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FunctionAttribute() """
    @property
    def IsComposable(self) -> bool:
        """
        Get: IsComposable(self: FunctionAttribute) -> bool
        Set: IsComposable(self: FunctionAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FunctionAttribute) -> str
        Set: Name(self: FunctionAttribute) = value
        """
        ...



class InheritanceMappingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InheritanceMappingAttribute() """
    @property
    def Code(self) -> object:
        """
        Get: Code(self: InheritanceMappingAttribute) -> object
        Set: Code(self: InheritanceMappingAttribute) = value
        """
        ...

    @property
    def IsDefault(self) -> bool:
        """
        Get: IsDefault(self: InheritanceMappingAttribute) -> bool
        Set: IsDefault(self: InheritanceMappingAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: InheritanceMappingAttribute) -> Type
        Set: Type(self: InheritanceMappingAttribute) = value
        """
        ...



class MetaAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: MetaAccessor) -> Type """
        ...


    def GetBoxedValue(self, instance:object) -> object:
        """ GetBoxedValue(self: MetaAccessor, instance: object) -> object """
        ...

    def HasAssignedValue(self, instance:object) -> bool:
        """ HasAssignedValue(self: MetaAccessor, instance: object) -> bool """
        ...

    def HasLoadedValue(self, instance:object) -> bool:
        """ HasLoadedValue(self: MetaAccessor, instance: object) -> bool """
        ...

    def HasValue(self, instance:object) -> bool:
        """ HasValue(self: MetaAccessor, instance: object) -> bool """
        ...

    def SetBoxedValue(self, instance:object, value:object) -> object:
        """ SetBoxedValue(self: MetaAccessor, instance: object, value: object) -> object """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class MetaAssociation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DeleteOnNull(self) -> bool:
        """ Get: DeleteOnNull(self: MetaAssociation) -> bool """
        ...

    @property
    def DeleteRule(self) -> str:
        """ Get: DeleteRule(self: MetaAssociation) -> str """
        ...

    @property
    def IsForeignKey(self) -> bool:
        """ Get: IsForeignKey(self: MetaAssociation) -> bool """
        ...

    @property
    def IsMany(self) -> bool:
        """ Get: IsMany(self: MetaAssociation) -> bool """
        ...

    @property
    def IsNullable(self) -> bool:
        """ Get: IsNullable(self: MetaAssociation) -> bool """
        ...

    @property
    def IsUnique(self) -> bool:
        """ Get: IsUnique(self: MetaAssociation) -> bool """
        ...

    @property
    def OtherKey(self) -> ReadOnlyCollection:
        """ Get: OtherKey(self: MetaAssociation) -> ReadOnlyCollection[MetaDataMember] """
        ...

    @property
    def OtherKeyIsPrimaryKey(self) -> bool:
        """ Get: OtherKeyIsPrimaryKey(self: MetaAssociation) -> bool """
        ...

    @property
    def OtherMember(self) -> MetaDataMember:
        """ Get: OtherMember(self: MetaAssociation) -> MetaDataMember """
        ...

    @property
    def OtherType(self) -> MetaType:
        """ Get: OtherType(self: MetaAssociation) -> MetaType """
        ...

    @property
    def ThisKey(self) -> ReadOnlyCollection:
        """ Get: ThisKey(self: MetaAssociation) -> ReadOnlyCollection[MetaDataMember] """
        ...

    @property
    def ThisKeyIsPrimaryKey(self) -> bool:
        """ Get: ThisKeyIsPrimaryKey(self: MetaAssociation) -> bool """
        ...

    @property
    def ThisMember(self) -> MetaDataMember:
        """ Get: ThisMember(self: MetaAssociation) -> MetaDataMember """
        ...



class MetaDataMember: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Association(self) -> MetaAssociation:
        """ Get: Association(self: MetaDataMember) -> MetaAssociation """
        ...

    @property
    def AutoSync(self) -> AutoSync:
        """ Get: AutoSync(self: MetaDataMember) -> AutoSync """
        ...

    @property
    def CanBeNull(self) -> bool:
        """ Get: CanBeNull(self: MetaDataMember) -> bool """
        ...

    @property
    def DbType(self) -> str:
        """ Get: DbType(self: MetaDataMember) -> str """
        ...

    @property
    def DeclaringType(self) -> MetaType:
        """ Get: DeclaringType(self: MetaDataMember) -> MetaType """
        ...

    @property
    def DeferredSourceAccessor(self) -> MetaAccessor:
        """ Get: DeferredSourceAccessor(self: MetaDataMember) -> MetaAccessor """
        ...

    @property
    def DeferredValueAccessor(self) -> MetaAccessor:
        """ Get: DeferredValueAccessor(self: MetaDataMember) -> MetaAccessor """
        ...

    @property
    def Expression(self) -> str:
        """ Get: Expression(self: MetaDataMember) -> str """
        ...

    @property
    def IsAssociation(self) -> bool:
        """ Get: IsAssociation(self: MetaDataMember) -> bool """
        ...

    @property
    def IsDbGenerated(self) -> bool:
        """ Get: IsDbGenerated(self: MetaDataMember) -> bool """
        ...

    @property
    def IsDeferred(self) -> bool:
        """ Get: IsDeferred(self: MetaDataMember) -> bool """
        ...

    @property
    def IsDiscriminator(self) -> bool:
        """ Get: IsDiscriminator(self: MetaDataMember) -> bool """
        ...

    @property
    def IsPersistent(self) -> bool:
        """ Get: IsPersistent(self: MetaDataMember) -> bool """
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        """ Get: IsPrimaryKey(self: MetaDataMember) -> bool """
        ...

    @property
    def IsVersion(self) -> bool:
        """ Get: IsVersion(self: MetaDataMember) -> bool """
        ...

    @property
    def LoadMethod(self) -> MethodInfo:
        """ Get: LoadMethod(self: MetaDataMember) -> MethodInfo """
        ...

    @property
    def MappedName(self) -> str:
        """ Get: MappedName(self: MetaDataMember) -> str """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: MetaDataMember) -> MemberInfo """
        ...

    @property
    def MemberAccessor(self) -> MetaAccessor:
        """ Get: MemberAccessor(self: MetaDataMember) -> MetaAccessor """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaDataMember) -> str """
        ...

    @property
    def Ordinal(self) -> int:
        """ Get: Ordinal(self: MetaDataMember) -> int """
        ...

    @property
    def StorageAccessor(self) -> MetaAccessor:
        """ Get: StorageAccessor(self: MetaDataMember) -> MetaAccessor """
        ...

    @property
    def StorageMember(self) -> MemberInfo:
        """ Get: StorageMember(self: MetaDataMember) -> MemberInfo """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: MetaDataMember) -> Type """
        ...

    @property
    def UpdateCheck(self) -> UpdateCheck:
        """ Get: UpdateCheck(self: MetaDataMember) -> UpdateCheck """
        ...


    def IsDeclaredBy(self, type:MetaType) -> bool:
        """ IsDeclaredBy(self: MetaDataMember, type: MetaType) -> bool """
        ...


class MetaFunction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HasMultipleResults(self) -> bool:
        """ Get: HasMultipleResults(self: MetaFunction) -> bool """
        ...

    @property
    def IsComposable(self) -> bool:
        """ Get: IsComposable(self: MetaFunction) -> bool """
        ...

    @property
    def MappedName(self) -> str:
        """ Get: MappedName(self: MetaFunction) -> str """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: MetaFunction) -> MethodInfo """
        ...

    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: MetaFunction) -> MetaModel """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaFunction) -> str """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: MetaFunction) -> ReadOnlyCollection[MetaParameter] """
        ...

    @property
    def ResultRowTypes(self) -> ReadOnlyCollection:
        """ Get: ResultRowTypes(self: MetaFunction) -> ReadOnlyCollection[MetaType] """
        ...

    @property
    def ReturnParameter(self) -> MetaParameter:
        """ Get: ReturnParameter(self: MetaFunction) -> MetaParameter """
        ...



class MetaModel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContextType(self) -> Type:
        """ Get: ContextType(self: MetaModel) -> Type """
        ...

    @property
    def DatabaseName(self) -> str:
        """ Get: DatabaseName(self: MetaModel) -> str """
        ...

    @property
    def MappingSource(self) -> MappingSource:
        """ Get: MappingSource(self: MetaModel) -> MappingSource """
        ...

    @property
    def ProviderType(self) -> Type:
        """ Get: ProviderType(self: MetaModel) -> Type """
        ...


    def GetFunction(self, method:MethodInfo) -> MetaFunction:
        """ GetFunction(self: MetaModel, method: MethodInfo) -> MetaFunction """
        ...

    def GetFunctions(self) -> IEnumerable:
        """ GetFunctions(self: MetaModel) -> IEnumerable[MetaFunction] """
        ...

    def GetMetaType(self, type:Type) -> MetaType:
        """ GetMetaType(self: MetaModel, type: Type) -> MetaType """
        ...

    def GetTable(self, rowType:Type) -> MetaTable:
        """ GetTable(self: MetaModel, rowType: Type) -> MetaTable """
        ...

    def GetTables(self) -> IEnumerable:
        """ GetTables(self: MetaModel) -> IEnumerable[MetaTable] """
        ...


class MetaParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DbType(self) -> str:
        """ Get: DbType(self: MetaParameter) -> str """
        ...

    @property
    def MappedName(self) -> str:
        """ Get: MappedName(self: MetaParameter) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaParameter) -> str """
        ...

    @property
    def Parameter(self) -> ParameterInfo:
        """ Get: Parameter(self: MetaParameter) -> ParameterInfo """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: MetaParameter) -> Type """
        ...



class MetaTable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DeleteMethod(self) -> MethodInfo:
        """ Get: DeleteMethod(self: MetaTable) -> MethodInfo """
        ...

    @property
    def InsertMethod(self) -> MethodInfo:
        """ Get: InsertMethod(self: MetaTable) -> MethodInfo """
        ...

    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: MetaTable) -> MetaModel """
        ...

    @property
    def RowType(self) -> MetaType:
        """ Get: RowType(self: MetaTable) -> MetaType """
        ...

    @property
    def TableName(self) -> str:
        """ Get: TableName(self: MetaTable) -> str """
        ...

    @property
    def UpdateMethod(self) -> MethodInfo:
        """ Get: UpdateMethod(self: MetaTable) -> MethodInfo """
        ...



class MetaType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Associations(self) -> ReadOnlyCollection:
        """ Get: Associations(self: MetaType) -> ReadOnlyCollection[MetaAssociation] """
        ...

    @property
    def CanInstantiate(self) -> bool:
        """ Get: CanInstantiate(self: MetaType) -> bool """
        ...

    @property
    def DataMembers(self) -> ReadOnlyCollection:
        """ Get: DataMembers(self: MetaType) -> ReadOnlyCollection[MetaDataMember] """
        ...

    @property
    def DBGeneratedIdentityMember(self) -> MetaDataMember:
        """ Get: DBGeneratedIdentityMember(self: MetaType) -> MetaDataMember """
        ...

    @property
    def DerivedTypes(self) -> ReadOnlyCollection:
        """ Get: DerivedTypes(self: MetaType) -> ReadOnlyCollection[MetaType] """
        ...

    @property
    def Discriminator(self) -> MetaDataMember:
        """ Get: Discriminator(self: MetaType) -> MetaDataMember """
        ...

    @property
    def HasAnyLoadMethod(self) -> bool:
        """ Get: HasAnyLoadMethod(self: MetaType) -> bool """
        ...

    @property
    def HasAnyValidateMethod(self) -> bool:
        """ Get: HasAnyValidateMethod(self: MetaType) -> bool """
        ...

    @property
    def HasInheritance(self) -> bool:
        """ Get: HasInheritance(self: MetaType) -> bool """
        ...

    @property
    def HasInheritanceCode(self) -> bool:
        """ Get: HasInheritanceCode(self: MetaType) -> bool """
        ...

    @property
    def HasUpdateCheck(self) -> bool:
        """ Get: HasUpdateCheck(self: MetaType) -> bool """
        ...

    @property
    def IdentityMembers(self) -> ReadOnlyCollection:
        """ Get: IdentityMembers(self: MetaType) -> ReadOnlyCollection[MetaDataMember] """
        ...

    @property
    def InheritanceBase(self) -> MetaType:
        """ Get: InheritanceBase(self: MetaType) -> MetaType """
        ...

    @property
    def InheritanceCode(self) -> object:
        """ Get: InheritanceCode(self: MetaType) -> object """
        ...

    @property
    def InheritanceDefault(self) -> MetaType:
        """ Get: InheritanceDefault(self: MetaType) -> MetaType """
        ...

    @property
    def InheritanceRoot(self) -> MetaType:
        """ Get: InheritanceRoot(self: MetaType) -> MetaType """
        ...

    @property
    def InheritanceTypes(self) -> ReadOnlyCollection:
        """ Get: InheritanceTypes(self: MetaType) -> ReadOnlyCollection[MetaType] """
        ...

    @property
    def IsEntity(self) -> bool:
        """ Get: IsEntity(self: MetaType) -> bool """
        ...

    @property
    def IsInheritanceDefault(self) -> bool:
        """ Get: IsInheritanceDefault(self: MetaType) -> bool """
        ...

    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: MetaType) -> MetaModel """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaType) -> str """
        ...

    @property
    def OnLoadedMethod(self) -> MethodInfo:
        """ Get: OnLoadedMethod(self: MetaType) -> MethodInfo """
        ...

    @property
    def OnValidateMethod(self) -> MethodInfo:
        """ Get: OnValidateMethod(self: MetaType) -> MethodInfo """
        ...

    @property
    def PersistentDataMembers(self) -> ReadOnlyCollection:
        """ Get: PersistentDataMembers(self: MetaType) -> ReadOnlyCollection[MetaDataMember] """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: MetaType) -> MetaTable """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: MetaType) -> Type """
        ...

    @property
    def VersionMember(self) -> MetaDataMember:
        """ Get: VersionMember(self: MetaType) -> MetaDataMember """
        ...


    def GetDataMember(self, member:MemberInfo) -> MetaDataMember:
        """ GetDataMember(self: MetaType, member: MemberInfo) -> MetaDataMember """
        ...

    def GetInheritanceType(self, type:Type) -> MetaType:
        """ GetInheritanceType(self: MetaType, type: Type) -> MetaType """
        ...

    def GetTypeForInheritanceCode(self, code:object) -> MetaType:
        """ GetTypeForInheritanceCode(self: MetaType, code: object) -> MetaType """
        ...


class ParameterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ParameterAttribute() """
    @property
    def DbType(self) -> str:
        """
        Get: DbType(self: ParameterAttribute) -> str
        Set: DbType(self: ParameterAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ParameterAttribute) -> str
        Set: Name(self: ParameterAttribute) = value
        """
        ...



class ProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ProviderAttribute()
    ProviderAttribute(type: Type)
    """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: ProviderAttribute) -> Type """
        ...


    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class ResultTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ResultTypeAttribute(type: Type) """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: ResultTypeAttribute) -> Type """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class TableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TableAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: TableAttribute) -> str
        Set: Name(self: TableAttribute) = value
        """
        ...



class UpdateCheck(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdateCheck, values: Always (0), Never (1), WhenChanged (2) """
    Always: UpdateCheck = ...
    Never: UpdateCheck = ...
    value__ = ...
    WhenChanged: UpdateCheck = ...


class XmlMappingSource(MappingSource): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def FromReader(reader:XmlReader) -> XmlMappingSource:
        """ FromReader(reader: XmlReader) -> XmlMappingSource """
        ...

    @staticmethod
    def FromStream(stream:Stream) -> XmlMappingSource:
        """ FromStream(stream: Stream) -> XmlMappingSource """
        ...

    @staticmethod
    def FromUrl(url:str) -> XmlMappingSource:
        """ FromUrl(url: str) -> XmlMappingSource """
        ...

    @staticmethod
    def FromXml(xml:str) -> XmlMappingSource:
        """ FromXml(xml: str) -> XmlMappingSource """
        ...


