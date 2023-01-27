# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.Metadata calls itself Metadata
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.SqlParser.Common import (
    DatabaseCompatibilityLevel)

from System import Array, Byte, Enum, Int64, Predicate

from System.Collections import (IComparer, IEnumerable, IEnumerator, 
    IEqualityComparer)

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class ActivationOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivationOrder, values: First (1), Last (2), None (0) """
    First: ActivationOrder = ...
    Last: ActivationOrder = ...
    value__ = ...


class CallableModuleType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CallableModuleType, values: ExtendedStoredProcedure (0), ScalarFunction (1), StoredProcedure (2) """
    ExtendedStoredProcedure: CallableModuleType = ...
    ScalarFunction: CallableModuleType = ...
    StoredProcedure: CallableModuleType = ...
    value__ = ...


class IMetadataObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IMetadataObject) -> str """
        ...


    def Accept(self, visitor:IMetadataObjectVisitor): # -> T
        """ Accept[T](self: IMetadataObject, visitor: IMetadataObjectVisitor[T]) -> T """
        ...


class ICollation(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CollationInfo(ICollation): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Collations(self) -> IMetadataCollection:
        """ Get: Collations() -> IMetadataCollection[ICollation] """
        ...

    @property
    def Comparer(self) -> IComparer:
        """ Get: Comparer(self: CollationInfo) -> IComparer[str] """
        ...

    @property
    def Default(self) -> CollationInfo:
        """ Get: Default() -> CollationInfo """
        ...

    @property
    def EqualityComparer(self) -> IEqualityComparer:
        """ Get: EqualityComparer(self: CollationInfo) -> IEqualityComparer[str] """
        ...

    @property
    def LCID(self) -> int:
        """ Get: LCID(self: CollationInfo) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CollationInfo) -> str """
        ...

    @property
    def Ordinal(self) -> CollationInfo:
        """ Get: Ordinal() -> CollationInfo """
        ...

    @property
    def OrdinalIgnoreCase(self) -> CollationInfo:
        """ Get: OrdinalIgnoreCase() -> CollationInfo """
        ...


    @staticmethod
    def GetCollationInfo(*__args:str) -> CollationInfo:
        """
        GetCollationInfo(collationName: str) -> CollationInfo
        GetCollationInfo(collation: ICollation) -> CollationInfo
        GetCollationInfo(lcid: int, compareOptions: CompareOptions) -> CollationInfo
        """
        ...

    def IsPrefix(self, source:str, prefix:str) -> bool:
        """ IsPrefix(self: CollationInfo, source: str, prefix: str) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: CollationInfo) -> str """
        ...



class ComputedColumnInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ComputedColumnInfo(text: str, isPersisted: bool) """
    @property
    def IsPersisted(self) -> bool:
        """ Get: IsPersisted(self: ComputedColumnInfo) -> bool """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ComputedColumnInfo) -> str """
        ...



class ConstraintType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConstraintType, values: Check (0), ForeignKey (1), PrimaryKey (2), Unique (3) """
    Check: ConstraintType = ...
    ForeignKey: ConstraintType = ...
    PrimaryKey: ConstraintType = ...
    Unique: ConstraintType = ...
    value__ = ...


class DatabasePermissionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabasePermissionType, values: Alter (0), AlterAnyApplicationRole (1), AlterAnyAssembly (2), AlterAnyAsymmetricKey (3), AlterAnyCertificate (4), AlterAnyContract (5), AlterAnyDatabaseAudit (6), AlterAnyDatabaseDdlTrigger (7), AlterAnyDatabaseEventNotification (8), AlterAnyDataspace (9), AlterAnyFulltextCatalog (10), AlterAnyMask (11), AlterAnyMessageType (12), AlterAnyRemoteServiceBinding (13), AlterAnyRole (14), AlterAnyRoute (15), AlterAnySchema (16), AlterAnyService (17), AlterAnySymmetricKey (18), AlterAnyUser (19), Authenticate (20), BackupDatabase (21), BackupLog (22), Checkpoint (23), Connect (24), ConnectReplication (25), Control (26), CreateAggregate (27), CreateAssembly (28), CreateAsymmetricKey (29), CreateCertificate (30), CreateContract (31), CreateDatabase (32), CreateDatabaseDdlEventNotification (33), CreateDefault (34), CreateFulltextCatalog (35), CreateFunction (36), CreateMessageType (37), CreateProcedure (38), CreateQueue (39), CreateRemoteServiceBinding (40), CreateRole (41), CreateRoute (42), CreateRule (43), CreateSchema (44), CreateService (45), CreateSymmetricKey (46), CreateSynonym (47), CreateTable (48), CreateType (49), CreateView (50), CreateXmlSchemaCollection (51), Delete (52), Execute (53), Impersonate (54), Insert (55), Receive (56), References (57), Select (58), Send (59), Showplan (60), SubscribeQueryNotifications (61), TakeOwnership (62), Unmask (63), Update (64), ViewAnyColumnEncryptionKeyDefinition (65), ViewAnyColumnMasterKeyDefinition (66), ViewChangeTracking (67), ViewDatabaseState (68), ViewDefinition (69) """
    Alter: DatabasePermissionType = ...
    AlterAnyApplicationRole: DatabasePermissionType = ...
    AlterAnyAssembly: DatabasePermissionType = ...
    AlterAnyAsymmetricKey: DatabasePermissionType = ...
    AlterAnyCertificate: DatabasePermissionType = ...
    AlterAnyContract: DatabasePermissionType = ...
    AlterAnyDatabaseAudit: DatabasePermissionType = ...
    AlterAnyDatabaseDdlTrigger: DatabasePermissionType = ...
    AlterAnyDatabaseEventNotification: DatabasePermissionType = ...
    AlterAnyDataspace: DatabasePermissionType = ...
    AlterAnyFulltextCatalog: DatabasePermissionType = ...
    AlterAnyMask: DatabasePermissionType = ...
    AlterAnyMessageType: DatabasePermissionType = ...
    AlterAnyRemoteServiceBinding: DatabasePermissionType = ...
    AlterAnyRole: DatabasePermissionType = ...
    AlterAnyRoute: DatabasePermissionType = ...
    AlterAnySchema: DatabasePermissionType = ...
    AlterAnyService: DatabasePermissionType = ...
    AlterAnySymmetricKey: DatabasePermissionType = ...
    AlterAnyUser: DatabasePermissionType = ...
    Authenticate: DatabasePermissionType = ...
    BackupDatabase: DatabasePermissionType = ...
    BackupLog: DatabasePermissionType = ...
    Checkpoint: DatabasePermissionType = ...
    Connect: DatabasePermissionType = ...
    ConnectReplication: DatabasePermissionType = ...
    Control: DatabasePermissionType = ...
    CreateAggregate: DatabasePermissionType = ...
    CreateAssembly: DatabasePermissionType = ...
    CreateAsymmetricKey: DatabasePermissionType = ...
    CreateCertificate: DatabasePermissionType = ...
    CreateContract: DatabasePermissionType = ...
    CreateDatabase: DatabasePermissionType = ...
    CreateDatabaseDdlEventNotification: DatabasePermissionType = ...
    CreateDefault: DatabasePermissionType = ...
    CreateFulltextCatalog: DatabasePermissionType = ...
    CreateFunction: DatabasePermissionType = ...
    CreateMessageType: DatabasePermissionType = ...
    CreateProcedure: DatabasePermissionType = ...
    CreateQueue: DatabasePermissionType = ...
    CreateRemoteServiceBinding: DatabasePermissionType = ...
    CreateRole: DatabasePermissionType = ...
    CreateRoute: DatabasePermissionType = ...
    CreateRule: DatabasePermissionType = ...
    CreateSchema: DatabasePermissionType = ...
    CreateService: DatabasePermissionType = ...
    CreateSymmetricKey: DatabasePermissionType = ...
    CreateSynonym: DatabasePermissionType = ...
    CreateTable: DatabasePermissionType = ...
    CreateType: DatabasePermissionType = ...
    CreateView: DatabasePermissionType = ...
    CreateXmlSchemaCollection: DatabasePermissionType = ...
    Delete: DatabasePermissionType = ...
    Execute: DatabasePermissionType = ...
    Impersonate: DatabasePermissionType = ...
    Insert: DatabasePermissionType = ...
    Receive: DatabasePermissionType = ...
    References: DatabasePermissionType = ...
    Select: DatabasePermissionType = ...
    Send: DatabasePermissionType = ...
    Showplan: DatabasePermissionType = ...
    SubscribeQueryNotifications: DatabasePermissionType = ...
    TakeOwnership: DatabasePermissionType = ...
    Unmask: DatabasePermissionType = ...
    Update: DatabasePermissionType = ...
    value__ = ...
    ViewAnyColumnEncryptionKeyDefinition: DatabasePermissionType = ...
    ViewAnyColumnMasterKeyDefinition: DatabasePermissionType = ...
    ViewChangeTracking: DatabasePermissionType = ...
    ViewDatabaseState: DatabasePermissionType = ...
    ViewDefinition: DatabasePermissionType = ...


class DataTypeArgSpec: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DoubleByteLength(self) -> DataTypeArgSpec:
        """ Get: DoubleByteLength() -> DataTypeArgSpec """
        ...

    @property
    def NumericPrecision(self) -> DataTypeArgSpec:
        """ Get: NumericPrecision() -> DataTypeArgSpec """
        ...

    @property
    def NumericScale(self) -> DataTypeArgSpec:
        """ Get: NumericScale() -> DataTypeArgSpec """
        ...

    @property
    def SingleByteLength(self) -> DataTypeArgSpec:
        """ Get: SingleByteLength() -> DataTypeArgSpec """
        ...

    @property
    def TimeScale(self) -> DataTypeArgSpec:
        """ Get: TimeScale() -> DataTypeArgSpec """
        ...


    def ToString(self) -> str:
        """ ToString(self: DataTypeArgSpec) -> str """
        ...

    DefaultValue = ...
    MaxValue = ...
    MinValue = ...
    Name = ...


class DataTypeSpec: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllDataTypes(self) -> IEnumerable:
        """ Get: AllDataTypes() -> IEnumerable[DataTypeSpec] """
        ...

    @property
    def ArgIsScale(self) -> bool:
        """ Get: ArgIsScale(self: DataTypeSpec) -> bool """
        ...

    @property
    def ArgSpec1(self) -> DataTypeArgSpec:
        """ Get: ArgSpec1(self: DataTypeSpec) -> DataTypeArgSpec """
        ...

    @property
    def ArgSpec2(self) -> DataTypeArgSpec:
        """ Get: ArgSpec2(self: DataTypeSpec) -> DataTypeArgSpec """
        ...

    @property
    def BigInt(self) -> DataTypeSpec:
        """ Get: BigInt() -> DataTypeSpec """
        ...

    @property
    def Binary(self) -> DataTypeSpec:
        """ Get: Binary() -> DataTypeSpec """
        ...

    @property
    def Bit(self) -> DataTypeSpec:
        """ Get: Bit() -> DataTypeSpec """
        ...

    @property
    def Char(self) -> DataTypeSpec:
        """ Get: Char() -> DataTypeSpec """
        ...

    @property
    def Date(self) -> DataTypeSpec:
        """ Get: Date() -> DataTypeSpec """
        ...

    @property
    def DateTime(self) -> DataTypeSpec:
        """ Get: DateTime() -> DataTypeSpec """
        ...

    @property
    def DateTime2(self) -> DataTypeSpec:
        """ Get: DateTime2() -> DataTypeSpec """
        ...

    @property
    def DateTimeOffset(self) -> DataTypeSpec:
        """ Get: DateTimeOffset() -> DataTypeSpec """
        ...

    @property
    def Decimal(self) -> DataTypeSpec:
        """ Get: Decimal() -> DataTypeSpec """
        ...

    @property
    def Float(self) -> DataTypeSpec:
        """ Get: Float() -> DataTypeSpec """
        ...

    @property
    def Geography(self) -> DataTypeSpec:
        """ Get: Geography() -> DataTypeSpec """
        ...

    @property
    def Geometry(self) -> DataTypeSpec:
        """ Get: Geometry() -> DataTypeSpec """
        ...

    @property
    def HierarchyId(self) -> DataTypeSpec:
        """ Get: HierarchyId() -> DataTypeSpec """
        ...

    @property
    def Image(self) -> DataTypeSpec:
        """ Get: Image() -> DataTypeSpec """
        ...

    @property
    def Int(self) -> DataTypeSpec:
        """ Get: Int() -> DataTypeSpec """
        ...

    @property
    def Money(self) -> DataTypeSpec:
        """ Get: Money() -> DataTypeSpec """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataTypeSpec) -> str """
        ...

    @property
    def NChar(self) -> DataTypeSpec:
        """ Get: NChar() -> DataTypeSpec """
        ...

    @property
    def NText(self) -> DataTypeSpec:
        """ Get: NText() -> DataTypeSpec """
        ...

    @property
    def Numeric(self) -> DataTypeSpec:
        """ Get: Numeric() -> DataTypeSpec """
        ...

    @property
    def NVarChar(self) -> DataTypeSpec:
        """ Get: NVarChar() -> DataTypeSpec """
        ...

    @property
    def NVarCharMax(self) -> DataTypeSpec:
        """ Get: NVarCharMax() -> DataTypeSpec """
        ...

    @property
    def Real(self) -> DataTypeSpec:
        """ Get: Real() -> DataTypeSpec """
        ...

    @property
    def RequireLength(self) -> bool:
        """ Get: RequireLength(self: DataTypeSpec) -> bool """
        ...

    @property
    def SmallDateTime(self) -> DataTypeSpec:
        """ Get: SmallDateTime() -> DataTypeSpec """
        ...

    @property
    def SmallInt(self) -> DataTypeSpec:
        """ Get: SmallInt() -> DataTypeSpec """
        ...

    @property
    def SmallMoney(self) -> DataTypeSpec:
        """ Get: SmallMoney() -> DataTypeSpec """
        ...

    @property
    def SqlDataType(self) -> SqlDataType:
        """ Get: SqlDataType(self: DataTypeSpec) -> SqlDataType """
        ...

    @property
    def SysName(self) -> DataTypeSpec:
        """ Get: SysName() -> DataTypeSpec """
        ...

    @property
    def Text(self) -> DataTypeSpec:
        """ Get: Text() -> DataTypeSpec """
        ...

    @property
    def Time(self) -> DataTypeSpec:
        """ Get: Time() -> DataTypeSpec """
        ...

    @property
    def Timestamp(self) -> DataTypeSpec:
        """ Get: Timestamp() -> DataTypeSpec """
        ...

    @property
    def TinyInt(self) -> DataTypeSpec:
        """ Get: TinyInt() -> DataTypeSpec """
        ...

    @property
    def UniqueIdentifier(self) -> DataTypeSpec:
        """ Get: UniqueIdentifier() -> DataTypeSpec """
        ...

    @property
    def VarBinary(self) -> DataTypeSpec:
        """ Get: VarBinary() -> DataTypeSpec """
        ...

    @property
    def VarBinaryMax(self) -> DataTypeSpec:
        """ Get: VarBinaryMax() -> DataTypeSpec """
        ...

    @property
    def VarChar(self) -> DataTypeSpec:
        """ Get: VarChar() -> DataTypeSpec """
        ...

    @property
    def VarCharMax(self) -> DataTypeSpec:
        """ Get: VarCharMax() -> DataTypeSpec """
        ...

    @property
    def Variant(self) -> DataTypeSpec:
        """ Get: Variant() -> DataTypeSpec """
        ...

    @property
    def Xml(self) -> DataTypeSpec:
        """ Get: Xml() -> DataTypeSpec """
        ...


    @staticmethod
    def GetDataTypeSpec(typeName:str) -> DataTypeSpec:
        """ GetDataTypeSpec(typeName: str) -> DataTypeSpec """
        ...



class ExecutionContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExecutionContextType, values: Caller (0), ExecuteAsLogin (1), ExecuteAsUser (2), Owner (3), Self (4) """
    Caller: ExecutionContextType = ...
    ExecuteAsLogin: ExecutionContextType = ...
    ExecuteAsUser: ExecutionContextType = ...
    Owner: ExecutionContextType = ...
    Self: ExecutionContextType = ...
    value__ = ...


class ForeignKeyAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ForeignKeyAction, values: Cascade (1), NoAction (0), SetDefault (2), SetNull (3) """
    Cascade: ForeignKeyAction = ...
    NoAction: ForeignKeyAction = ...
    SetDefault: ForeignKeyAction = ...
    SetNull: ForeignKeyAction = ...
    value__ = ...


class GridDensity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridDensity, values: High (2), Low (0), Medium (1) """
    High: GridDensity = ...
    Low: GridDensity = ...
    Medium: GridDensity = ...
    value__ = ...


class IDatabaseObject(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: IDatabaseObject) -> bool """
        ...

    @property
    def Parent(self) -> IDatabaseObject:
        """ Get: Parent(self: IDatabaseObject) -> IDatabaseObject """
        ...



class IDatabaseOwnedObject(IDatabaseObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Database(self) -> IDatabase:
        """ Get: Database(self: IDatabaseOwnedObject) -> IDatabase """
        ...



class IDatabasePrincipal(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def MemberOfRoles(self) -> IMetadataCollection:
        """ Get: MemberOfRoles(self: IDatabasePrincipal) -> IMetadataCollection[IDatabaseRole] """
        ...

    @property
    def Permissions(self) -> IMetadataCollection:
        """ Get: Permissions(self: IDatabasePrincipal) -> IMetadataCollection[IDatabasePermission] """
        ...



class IApplicationRole(IDatabasePrincipal): # skipped bases: <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def DefaultSchema(self) -> ISchema:
        """ Get: DefaultSchema(self: IApplicationRole) -> ISchema """
        ...



class IAsymmetricKey(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IFunctionModuleBase(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Parameters(self) -> IMetadataOrderedCollection:
        """ Get: Parameters(self: IFunctionModuleBase) -> IMetadataOrderedCollection[IParameter] """
        ...



class IFunction(IFunctionModuleBase): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IScalar(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataType(self) -> IScalarDataType:
        """ Get: DataType(self: IScalar) -> IScalarDataType """
        ...

    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: IScalar) -> bool """
        ...

    @property
    def ScalarType(self) -> ScalarType:
        """ Get: ScalarType(self: IScalar) -> ScalarType """
        ...



class IScalarFunction(IFunction, IScalar): # skipped bases: <type 'IFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsAggregateFunction(self) -> bool:
        """ Get: IsAggregateFunction(self: IScalarFunction) -> bool """
        ...



class IBuiltInFunction(IScalarFunction): # skipped bases: <type 'IFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsDatePartFunction(self) -> bool:
        """ Get: IsDatePartFunction(self: IBuiltInFunction) -> bool """
        ...

    @property
    def IsGlobalVariable(self) -> bool:
        """ Get: IsGlobalVariable(self: IBuiltInFunction) -> bool """
        ...

    @property
    def IsVarArg(self) -> bool:
        """ Get: IsVarArg(self: IBuiltInFunction) -> bool """
        ...

    @property
    def MaxNumberOfArgs(self) -> int:
        """ Get: MaxNumberOfArgs(self: IBuiltInFunction) -> int """
        ...

    @property
    def MinNumberOfArgs(self) -> int:
        """ Get: MinNumberOfArgs(self: IBuiltInFunction) -> int """
        ...



class ISchemaOwnedObject(IDatabaseObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Schema(self) -> ISchema:
        """ Get: Schema(self: ISchemaOwnedObject) -> ISchema """
        ...



class IUserDefinedFunctionModuleBase(ISchemaOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def ExecutionContext(self) -> IExecutionContext:
        """ Get: ExecutionContext(self: IUserDefinedFunctionModuleBase) -> IExecutionContext """
        ...

    @property
    def IsEncrypted(self) -> bool:
        """ Get: IsEncrypted(self: IUserDefinedFunctionModuleBase) -> bool """
        ...



class ICallableModule(IFunctionModuleBase, IUserDefinedFunctionModuleBase): # skipped bases: <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def ModuleType(self) -> CallableModuleType:
        """ Get: ModuleType(self: ICallableModule) -> CallableModuleType """
        ...

    @property
    def ReturnType(self) -> IScalarDataType:
        """ Get: ReturnType(self: ICallableModule) -> IScalarDataType """
        ...



class ICertificate(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IConstraint(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsSystemNamed(self) -> bool:
        """ Get: IsSystemNamed(self: IConstraint) -> bool """
        ...

    @property
    def Parent(self) -> ITabular:
        """ Get: Parent(self: IConstraint) -> ITabular """
        ...

    @property
    def Type(self) -> ConstraintType:
        """ Get: Type(self: IConstraint) -> ConstraintType """
        ...



class ICheckConstraint(IConstraint): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsChecked(self) -> bool:
        """ Get: IsChecked(self: ICheckConstraint) -> bool """
        ...

    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled(self: ICheckConstraint) -> bool """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: ICheckConstraint) -> bool """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ICheckConstraint) -> str """
        ...



class IDataType(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsCursor(self) -> bool:
        """ Get: IsCursor(self: IDataType) -> bool """
        ...

    @property
    def IsScalar(self) -> bool:
        """ Get: IsScalar(self: IDataType) -> bool """
        ...

    @property
    def IsTable(self) -> bool:
        """ Get: IsTable(self: IDataType) -> bool """
        ...

    @property
    def IsUnknown(self) -> bool:
        """ Get: IsUnknown(self: IDataType) -> bool """
        ...



class IScalarDataType(IDataType): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def BaseSystemDataType(self) -> ISystemDataType:
        """ Get: BaseSystemDataType(self: IScalarDataType) -> ISystemDataType """
        ...

    @property
    def IsClr(self) -> bool:
        """ Get: IsClr(self: IScalarDataType) -> bool """
        ...

    @property
    def IsSystem(self) -> bool:
        """ Get: IsSystem(self: IScalarDataType) -> bool """
        ...

    @property
    def IsVoid(self) -> bool:
        """ Get: IsVoid(self: IScalarDataType) -> bool """
        ...

    @property
    def IsXml(self) -> bool:
        """ Get: IsXml(self: IScalarDataType) -> bool """
        ...



class IClrDataType(IScalarDataType): # skipped bases: <type 'IDataType'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: IClrDataType) -> str """
        ...

    @property
    def ClassName(self) -> str:
        """ Get: ClassName(self: IClrDataType) -> str """
        ...

    @property
    def DataMembers(self) -> IMetadataCollection:
        """ Get: DataMembers(self: IClrDataType) -> IMetadataCollection[IUdtDataMember] """
        ...

    @property
    def IsBinaryOrdered(self) -> bool:
        """ Get: IsBinaryOrdered(self: IClrDataType) -> bool """
        ...

    @property
    def IsComVisible(self) -> bool:
        """ Get: IsComVisible(self: IClrDataType) -> bool """
        ...

    @property
    def IsNullable(self) -> bool:
        """ Get: IsNullable(self: IClrDataType) -> bool """
        ...

    @property
    def Methods(self) -> IMetadataCollection:
        """ Get: Methods(self: IClrDataType) -> IMetadataCollection[IUdtMethod] """
        ...



class IColumn(IScalar): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Collation(self) -> ICollation:
        """ Get: Collation(self: IColumn) -> ICollation """
        ...

    @property
    def ComputedColumnInfo(self) -> ComputedColumnInfo:
        """ Get: ComputedColumnInfo(self: IColumn) -> ComputedColumnInfo """
        ...

    @property
    def DefaultValue(self) -> IDefaultConstraint:
        """ Get: DefaultValue(self: IColumn) -> IDefaultConstraint """
        ...

    @property
    def IdentityColumnInfo(self) -> IdentityColumnInfo:
        """ Get: IdentityColumnInfo(self: IColumn) -> IdentityColumnInfo """
        ...

    @property
    def InPrimaryKey(self) -> bool:
        """ Get: InPrimaryKey(self: IColumn) -> bool """
        ...

    @property
    def IsColumnSet(self) -> bool:
        """ Get: IsColumnSet(self: IColumn) -> bool """
        ...

    @property
    def IsGeneratedAlwaysAsRowEnd(self) -> bool:
        """ Get: IsGeneratedAlwaysAsRowEnd(self: IColumn) -> bool """
        ...

    @property
    def IsGeneratedAlwaysAsRowStart(self) -> bool:
        """ Get: IsGeneratedAlwaysAsRowStart(self: IColumn) -> bool """
        ...

    @property
    def IsSparse(self) -> bool:
        """ Get: IsSparse(self: IColumn) -> bool """
        ...

    @property
    def Parent(self) -> ITabular:
        """ Get: Parent(self: IColumn) -> ITabular """
        ...

    @property
    def RowGuidCol(self) -> bool:
        """ Get: RowGuidCol(self: IColumn) -> bool """
        ...



class IServerOwnedObject(IDatabaseObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Server(self) -> IServer:
        """ Get: Server(self: IServerOwnedObject) -> IServer """
        ...



class ICredential(IServerOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ICursorDataType(IDataType): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ILocalVariable(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataType(self) -> IDataType:
        """ Get: DataType(self: ILocalVariable) -> IDataType """
        ...

    @property
    def IsCursorVariable(self) -> bool:
        """ Get: IsCursorVariable(self: ILocalVariable) -> bool """
        ...

    @property
    def IsParameter(self) -> bool:
        """ Get: IsParameter(self: ILocalVariable) -> bool """
        ...

    @property
    def IsScalarVariable(self) -> bool:
        """ Get: IsScalarVariable(self: ILocalVariable) -> bool """
        ...

    @property
    def IsTableVariable(self) -> bool:
        """ Get: IsTableVariable(self: ILocalVariable) -> bool """
        ...



class ICursorVariable(ILocalVariable): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IParameter(ILocalVariable): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: IParameter) -> str """
        ...

    @property
    def IsOutput(self) -> bool:
        """ Get: IsOutput(self: IParameter) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IParameter) -> bool """
        ...



class ICursorParameter(IParameter, ICursorVariable): # skipped bases: <type 'IMetadataObject'>, <type 'ILocalVariable'>, <type 'object'>
    """ no doc """
    pass

class IDatabase(IServerOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationRoles(self) -> IMetadataCollection:
        """ Get: ApplicationRoles(self: IDatabase) -> IMetadataCollection[IApplicationRole] """
        ...

    @property
    def AsymmetricKeys(self) -> IMetadataCollection:
        """ Get: AsymmetricKeys(self: IDatabase) -> IMetadataCollection[IAsymmetricKey] """
        ...

    @property
    def Certificates(self) -> IMetadataCollection:
        """ Get: Certificates(self: IDatabase) -> IMetadataCollection[ICertificate] """
        ...

    @property
    def CollationInfo(self) -> CollationInfo:
        """ Get: CollationInfo(self: IDatabase) -> CollationInfo """
        ...

    @property
    def CompatibilityLevel(self) -> DatabaseCompatibilityLevel:
        """ Get: CompatibilityLevel(self: IDatabase) -> DatabaseCompatibilityLevel """
        ...

    @property
    def DefaultSchemaName(self) -> str:
        """ Get: DefaultSchemaName(self: IDatabase) -> str """
        ...

    @property
    def Owner(self) -> IUser:
        """ Get: Owner(self: IDatabase) -> IUser """
        ...

    @property
    def Roles(self) -> IMetadataCollection:
        """ Get: Roles(self: IDatabase) -> IMetadataCollection[IDatabaseRole] """
        ...

    @property
    def Schemas(self) -> IMetadataCollection:
        """ Get: Schemas(self: IDatabase) -> IMetadataCollection[ISchema] """
        ...

    @property
    def Triggers(self) -> IMetadataCollection:
        """ Get: Triggers(self: IDatabase) -> IMetadataCollection[IDatabaseDdlTrigger] """
        ...

    @property
    def Users(self) -> IMetadataCollection:
        """ Get: Users(self: IDatabase) -> IMetadataCollection[IUser] """
        ...



class ITrigger(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BodyText(self) -> str:
        """ Get: BodyText(self: ITrigger) -> str """
        ...

    @property
    def ExecutionContext(self) -> IExecutionContext:
        """ Get: ExecutionContext(self: ITrigger) -> IExecutionContext """
        ...

    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled(self: ITrigger) -> bool """
        ...

    @property
    def IsEncrypted(self) -> bool:
        """ Get: IsEncrypted(self: ITrigger) -> bool """
        ...

    @property
    def IsSqlClr(self) -> bool:
        """ Get: IsSqlClr(self: ITrigger) -> bool """
        ...



class IDatabaseDdlTrigger(ITrigger, IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def DatabaseDdlEvents(self) -> ITriggerEventTypeSet:
        """ Get: DatabaseDdlEvents(self: IDatabaseDdlTrigger) -> ITriggerEventTypeSet """
        ...

    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: IDatabaseDdlTrigger) -> bool """
        ...



class IDatabaseObjectVisitor(IDatabaseOwnedObjectVisitor, IServerOwnedObjectVisitor, ISchemaOwnedObjectVisitor): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDatabaseOwnedObjectVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, *__args:IApplicationRole): # -> T
        """
        Visit(self: IDatabaseOwnedObjectVisitor[T], applicationRole: IApplicationRole) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], assymetricKey: IAsymmetricKey) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], certificate: ICertificate) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], databaseDdlTrigger: IDatabaseDdlTrigger) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], databaseRole: IDatabaseRole) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], fileGroup: IFileGroup) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], partitionScheme: IPartitionScheme) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], schema: ISchema) -> T
        Visit(self: IDatabaseOwnedObjectVisitor[T], user: IUser) -> T
        """
        ...


class IDatabasePermission(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DatabasePrincipal(self) -> IDatabasePrincipal:
        """ Get: DatabasePrincipal(self: IDatabasePermission) -> IDatabasePrincipal """
        ...

    @property
    def Grantor(self) -> IDatabasePrincipal:
        """ Get: Grantor(self: IDatabasePermission) -> IDatabasePrincipal """
        ...

    @property
    def PermissionState(self) -> PermissionState:
        """ Get: PermissionState(self: IDatabasePermission) -> PermissionState """
        ...

    @property
    def PermissionType(self) -> DatabasePermissionType:
        """ Get: PermissionType(self: IDatabasePermission) -> DatabasePermissionType """
        ...

    @property
    def TargetObject(self) -> IMetadataObject:
        """ Get: TargetObject(self: IDatabasePermission) -> IMetadataObject """
        ...



class IDatabaseRole(IDatabasePrincipal): # skipped bases: <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsFixedRole(self) -> bool:
        """ Get: IsFixedRole(self: IDatabaseRole) -> bool """
        ...

    @property
    def Owner(self) -> IDatabasePrincipal:
        """ Get: Owner(self: IDatabaseRole) -> IDatabasePrincipal """
        ...



class ITabular(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> IMetadataOrderedCollection:
        """ Get: Columns(self: ITabular) -> IMetadataOrderedCollection[IColumn] """
        ...

    @property
    def TabularType(self) -> TabularType:
        """ Get: TabularType(self: ITabular) -> TabularType """
        ...

    @property
    def Unaliased(self) -> ITabular:
        """ Get: Unaliased(self: ITabular) -> ITabular """
        ...



class IDatabaseTable(ITabular): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def CollationInfo(self) -> CollationInfo:
        """ Get: CollationInfo(self: IDatabaseTable) -> CollationInfo """
        ...

    @property
    def Constraints(self) -> IMetadataCollection:
        """ Get: Constraints(self: IDatabaseTable) -> IMetadataCollection[IConstraint] """
        ...

    @property
    def Indexes(self) -> IMetadataCollection:
        """ Get: Indexes(self: IDatabaseTable) -> IMetadataCollection[IIndex] """
        ...

    @property
    def Statistics(self) -> IMetadataCollection:
        """ Get: Statistics(self: IDatabaseTable) -> IMetadataCollection[IStatistics] """
        ...



class IDatePart(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDefaultConstraint(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsSystemNamed(self) -> bool:
        """ Get: IsSystemNamed(self: IDefaultConstraint) -> bool """
        ...

    @property
    def Parent(self) -> IColumn:
        """ Get: Parent(self: IDefaultConstraint) -> IColumn """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: IDefaultConstraint) -> str """
        ...



class IdentityColumnInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    IdentityColumnInfo(seed: Int64, increment: Int64)
    IdentityColumnInfo(seed: Int64, increment: Int64, notForReplication: bool)
    """
    @property
    def Increment(self) -> Int64:
        """ Get: Increment(self: IdentityColumnInfo) -> Int64 """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: IdentityColumnInfo) -> bool """
        ...

    @property
    def Seed(self) -> Int64:
        """ Get: Seed(self: IdentityColumnInfo) -> Int64 """
        ...



class IDmlTrigger(ITrigger): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Delete(self) -> bool:
        """ Get: Delete(self: IDmlTrigger) -> bool """
        ...

    @property
    def DeleteActivationOrder(self) -> ActivationOrder:
        """ Get: DeleteActivationOrder(self: IDmlTrigger) -> ActivationOrder """
        ...

    @property
    def Insert(self) -> bool:
        """ Get: Insert(self: IDmlTrigger) -> bool """
        ...

    @property
    def InsertActivationOrder(self) -> ActivationOrder:
        """ Get: InsertActivationOrder(self: IDmlTrigger) -> ActivationOrder """
        ...

    @property
    def InsteadOf(self) -> bool:
        """ Get: InsteadOf(self: IDmlTrigger) -> bool """
        ...

    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: IDmlTrigger) -> bool """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: IDmlTrigger) -> bool """
        ...

    @property
    def Parent(self) -> ITableViewBase:
        """ Get: Parent(self: IDmlTrigger) -> ITableViewBase """
        ...

    @property
    def Update(self) -> bool:
        """ Get: Update(self: IDmlTrigger) -> bool """
        ...

    @property
    def UpdateActivationOrder(self) -> ActivationOrder:
        """ Get: UpdateActivationOrder(self: IDmlTrigger) -> ActivationOrder """
        ...



class IExecutionContext(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContextType(self) -> ExecutionContextType:
        """ Get: ContextType(self: IExecutionContext) -> ExecutionContextType """
        ...

    @property
    def Login(self) -> ILogin:
        """ Get: Login(self: IExecutionContext) -> ILogin """
        ...

    @property
    def User(self) -> IUser:
        """ Get: User(self: IExecutionContext) -> IUser """
        ...



class IExtendedStoredProcedure(ICallableModule): # skipped bases: <type 'IFunctionModuleBase'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IFileGroup(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: IFileGroup) -> bool """
        ...

    @property
    def IsFileStream(self) -> bool:
        """ Get: IsFileStream(self: IFileGroup) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IFileGroup) -> bool """
        ...



class IForeignKeyColumn(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReferencedColumn(self) -> IColumn:
        """ Get: ReferencedColumn(self: IForeignKeyColumn) -> IColumn """
        ...

    @property
    def ReferencingColumn(self) -> IColumn:
        """ Get: ReferencingColumn(self: IForeignKeyColumn) -> IColumn """
        ...



class IForeignKeyConstraint(IConstraint): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> IMetadataOrderedCollection:
        """ Get: Columns(self: IForeignKeyConstraint) -> IMetadataOrderedCollection[IForeignKeyColumn] """
        ...

    @property
    def DeleteAction(self) -> ForeignKeyAction:
        """ Get: DeleteAction(self: IForeignKeyConstraint) -> ForeignKeyAction """
        ...

    @property
    def IsChecked(self) -> bool:
        """ Get: IsChecked(self: IForeignKeyConstraint) -> bool """
        ...

    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled(self: IForeignKeyConstraint) -> bool """
        ...

    @property
    def NotForReplication(self) -> bool:
        """ Get: NotForReplication(self: IForeignKeyConstraint) -> bool """
        ...

    @property
    def ReferencedTable(self) -> ITable:
        """ Get: ReferencedTable(self: IForeignKeyConstraint) -> ITable """
        ...

    @property
    def UpdateAction(self) -> ForeignKeyAction:
        """ Get: UpdateAction(self: IForeignKeyConstraint) -> ForeignKeyAction """
        ...



class IIndex(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisallowPageLocks(self) -> bool:
        """ Get: DisallowPageLocks(self: IIndex) -> bool """
        ...

    @property
    def DisallowRowLocks(self) -> bool:
        """ Get: DisallowRowLocks(self: IIndex) -> bool """
        ...

    @property
    def FillFactor(self) -> Byte:
        """ Get: FillFactor(self: IIndex) -> Byte """
        ...

    @property
    def IgnoreDuplicateKeys(self) -> bool:
        """ Get: IgnoreDuplicateKeys(self: IIndex) -> bool """
        ...

    @property
    def IsDisabled(self) -> bool:
        """ Get: IsDisabled(self: IIndex) -> bool """
        ...

    @property
    def PadIndex(self) -> bool:
        """ Get: PadIndex(self: IIndex) -> bool """
        ...

    @property
    def Parent(self) -> ITabular:
        """ Get: Parent(self: IIndex) -> ITabular """
        ...

    @property
    def Type(self) -> IndexType:
        """ Get: Type(self: IIndex) -> IndexType """
        ...



class IIndexedColumn(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsIncluded(self) -> bool:
        """ Get: IsIncluded(self: IIndexedColumn) -> bool """
        ...

    @property
    def ReferencedColumn(self) -> IColumn:
        """ Get: ReferencedColumn(self: IIndexedColumn) -> IColumn """
        ...

    @property
    def SortOrder(self) -> SortOrder:
        """ Get: SortOrder(self: IIndexedColumn) -> SortOrder """
        ...



class ILogin(IServerOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def AsymmetricKey(self) -> IAsymmetricKey:
        """ Get: AsymmetricKey(self: ILogin) -> IAsymmetricKey """
        ...

    @property
    def Certificate(self) -> ICertificate:
        """ Get: Certificate(self: ILogin) -> ICertificate """
        ...

    @property
    def Credential(self) -> ICredential:
        """ Get: Credential(self: ILogin) -> ICredential """
        ...

    @property
    def DefaultDatabase(self) -> IDatabase:
        """ Get: DefaultDatabase(self: ILogin) -> IDatabase """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: ILogin) -> str """
        ...

    @property
    def LoginType(self) -> LoginType:
        """ Get: LoginType(self: ILogin) -> LoginType """
        ...

    @property
    def Password(self) -> IPassword:
        """ Get: Password(self: ILogin) -> IPassword """
        ...

    @property
    def Sid(self) -> Array:
        """ Get: Sid(self: ILogin) -> Array[Byte] """
        ...



class IMetadataCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AsMetadataObjectCollection(self) -> IMetadataCollection:
        """ Get: AsMetadataObjectCollection(self: IMetadataCollection[T]) -> IMetadataCollection[IMetadataObject] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IMetadataCollection[T]) -> int """
        ...


    def Contains(self, *__args:str) -> bool:
        """
        Contains(self: IMetadataCollection[T], name: str) -> bool
        Contains(self: IMetadataCollection[T], item: T) -> bool
        """
        ...

    def FindAll(self, *__args:Predicate) -> IEnumerable:
        """
        FindAll(self: IMetadataCollection[T], match: Predicate[T]) -> IEnumerable[T]
        FindAll(self: IMetadataCollection[T], name: str) -> IEnumerable[T]
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IMetadataObjectVisitor(IDatabaseObjectVisitor): # skipped bases: <type 'IServerOwnedObjectVisitor[T]'>, <type 'ISchemaOwnedObjectVisitor[T]'>, <type 'IDatabaseOwnedObjectVisitor[T]'>, <type 'object'>
    """ no doc """
    pass

class IMetadataOrderedCollection(IMetadataCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class IMutableMetadataObject(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IMutableDatabaseObject(IDatabaseObject, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabaseOwnedObject(IDatabaseOwnedObject, IMutableDatabaseObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabasePrincipal(IMutableDatabaseOwnedObject, IDatabasePrincipal): # skipped bases: <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableApplicationRole(IMutableDatabasePrincipal, IApplicationRole): # skipped bases: <type 'IMutableDatabaseOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IDatabasePrincipal'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableAsymmetricKey(IMutableDatabaseOwnedObject, IAsymmetricKey): # skipped bases: <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableFunctionModuleBase(IFunctionModuleBase, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableSchemaOwnedObject(ISchemaOwnedObject, IMutableDatabaseObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableUserDefinedFunctionModuleBase(IMutableSchemaOwnedObject, IUserDefinedFunctionModuleBase): # skipped bases: <type 'IMutableDatabaseObject'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableCallableModule(IMutableFunctionModuleBase, IMutableUserDefinedFunctionModuleBase, ICallableModule): # skipped bases: <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IFunctionModuleBase'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableCertificate(IMutableDatabaseOwnedObject, ICertificate): # skipped bases: <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableConstraint(IConstraint, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableCheckConstraint(ICheckConstraint, IMutableConstraint): # skipped bases: <type 'IConstraint'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDataType(IDataType, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableScalarDataType(IMutableDataType, IScalarDataType): # skipped bases: <type 'IDataType'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableClrDataType(IClrDataType, IMutableScalarDataType): # skipped bases: <type 'IScalarDataType'>, <type 'IMutableDataType'>, <type 'IDataType'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableScalar(IMutableMetadataObject, IScalar): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableColumn(IColumn, IMutableScalar): # skipped bases: <type 'IScalar'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableServerOwnedObject(IServerOwnedObject, IMutableDatabaseObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableCredential(ICredential, IMutableServerOwnedObject): # skipped bases: <type 'IMutableMetadataObject'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IServerOwnedObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabase(IDatabase, IMutableServerOwnedObject): # skipped bases: <type 'IMutableMetadataObject'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IServerOwnedObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableTrigger(ITrigger, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabaseDdlTrigger(IDatabaseDdlTrigger, IMutableDatabaseOwnedObject, IMutableTrigger): # skipped bases: <type 'IMutableMetadataObject'>, <type 'ITrigger'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabasePermission(IDatabasePermission): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabaseRole(IMutableDatabasePrincipal, IDatabaseRole): # skipped bases: <type 'IMutableDatabaseOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IDatabasePrincipal'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableTabular(ITabular, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDatabaseTable(IDatabaseTable, IMutableTabular): # skipped bases: <type 'ITabular'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDefaultConstraint(IDefaultConstraint, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableDmlTrigger(IDmlTrigger, IMutableTrigger): # skipped bases: <type 'ITrigger'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableForeignKeyConstraint(IForeignKeyConstraint, IMutableConstraint): # skipped bases: <type 'IConstraint'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableFunction(IMutableFunctionModuleBase, IFunction): # skipped bases: <type 'IFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableIndex(IMutableMetadataObject, IIndex): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableIndexedColumn(IIndexedColumn, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableLogin(ILogin, IMutableServerOwnedObject): # skipped bases: <type 'IMutableMetadataObject'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IServerOwnedObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableMetadataCollection(IMetadataCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: IMutableMetadataCollection[T], item: T) """
        ...

    def AddRange(self, collection:IEnumerable): # -> 
        """ AddRange(self: IMutableMetadataCollection[T], collection: IEnumerable[T]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IMutableMetadataCollection[T]) """
        ...

    def Clone(self, copyData:bool = ...) -> IMutableMetadataCollection:
        """
        Clone(self: IMutableMetadataCollection[T]) -> IMutableMetadataCollection[T]
        Clone(self: IMutableMetadataCollection[T], copyData: bool) -> IMutableMetadataCollection[T]
        """
        ...

    def Remove(self, *__args:str) -> bool:
        """
        Remove(self: IMutableMetadataCollection[T], name: str) -> bool
        Remove(self: IMutableMetadataCollection[T], item: T) -> bool
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IMutableMetadataOrderedCollection(IMetadataOrderedCollection, IMutableMetadataCollection): # skipped bases: <type 'IMetadataCollection[T]'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'object'>
    """ no doc """
    pass

class IPassword: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CheckExpiration(self) -> bool:
        """ Get: CheckExpiration(self: IPassword) -> bool """
        ...

    @property
    def CheckPolicy(self) -> bool:
        """ Get: CheckPolicy(self: IPassword) -> bool """
        ...

    @property
    def IsHashed(self) -> bool:
        """ Get: IsHashed(self: IPassword) -> bool """
        ...

    @property
    def MustChange(self) -> bool:
        """ Get: MustChange(self: IPassword) -> bool """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: IPassword) -> str """
        ...



class IMutablePassword(IPassword): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IRelationalIndex(IIndex): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def CompactLargeObjects(self) -> bool:
        """ Get: CompactLargeObjects(self: IRelationalIndex) -> bool """
        ...

    @property
    def FileGroup(self) -> IFileGroup:
        """ Get: FileGroup(self: IRelationalIndex) -> IFileGroup """
        ...

    @property
    def FileStreamFileGroup(self) -> IFileGroup:
        """ Get: FileStreamFileGroup(self: IRelationalIndex) -> IFileGroup """
        ...

    @property
    def FileStreamPartitionScheme(self) -> IPartitionScheme:
        """ Get: FileStreamPartitionScheme(self: IRelationalIndex) -> IPartitionScheme """
        ...

    @property
    def FilterDefinition(self) -> str:
        """ Get: FilterDefinition(self: IRelationalIndex) -> str """
        ...

    @property
    def IndexedColumns(self) -> IMetadataOrderedCollection:
        """ Get: IndexedColumns(self: IRelationalIndex) -> IMetadataOrderedCollection[IIndexedColumn] """
        ...

    @property
    def IndexKey(self) -> IUniqueConstraintBase:
        """ Get: IndexKey(self: IRelationalIndex) -> IUniqueConstraintBase """
        ...

    @property
    def IsClustered(self) -> bool:
        """ Get: IsClustered(self: IRelationalIndex) -> bool """
        ...

    @property
    def IsSystemNamed(self) -> bool:
        """ Get: IsSystemNamed(self: IRelationalIndex) -> bool """
        ...

    @property
    def IsUnique(self) -> bool:
        """ Get: IsUnique(self: IRelationalIndex) -> bool """
        ...

    @property
    def NoAutomaticRecomputation(self) -> bool:
        """ Get: NoAutomaticRecomputation(self: IRelationalIndex) -> bool """
        ...

    @property
    def PartitionScheme(self) -> IPartitionScheme:
        """ Get: PartitionScheme(self: IRelationalIndex) -> IPartitionScheme """
        ...



class IMutableRelationalIndex(IMutableIndex, IRelationalIndex): # skipped bases: <type 'IIndex'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableScalarFunction(IScalarFunction, IMutableFunction, IMutableScalar): # skipped bases: <type 'IFunction'>, <type 'IMutableMetadataObject'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IMutableFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedFunction(IFunction, IUserDefinedFunctionModuleBase): # skipped bases: <type 'IFunctionModuleBase'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyText(self) -> str:
        """ Get: BodyText(self: IUserDefinedFunction) -> str """
        ...

    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: IUserDefinedFunction) -> bool """
        ...

    @property
    def IsSchemaBound(self) -> bool:
        """ Get: IsSchemaBound(self: IUserDefinedFunction) -> bool """
        ...

    @property
    def IsSqlClr(self) -> bool:
        """ Get: IsSqlClr(self: IUserDefinedFunction) -> bool """
        ...



class IMutableUserDefinedFunction(IMutableFunction, IMutableUserDefinedFunctionModuleBase, IUserDefinedFunction): # skipped bases: <type 'IFunction'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IFunctionModuleBase'>, <type 'IMutableDatabaseObject'>, <type 'IMutableFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IScalarValuedFunction(IScalarFunction, IUserDefinedFunction, ICallableModule): # skipped bases: <type 'IFunction'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def ReturnsNullOnNullInput(self) -> bool:
        """ Get: ReturnsNullOnNullInput(self: IScalarValuedFunction) -> bool """
        ...



class IMutableScalarValuedFunction(IMutableCallableModule, IScalarValuedFunction, IMutableUserDefinedFunction, IMutableScalarFunction): # skipped bases: <type 'IFunction'>, <type 'ICallableModule'>, <type 'ISchemaOwnedObject'>, <type 'IScalarFunction'>, <type 'IMutableMetadataObject'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IMutableFunctionModuleBase'>, <type 'IMutableUserDefinedFunctionModuleBase'>, <type 'IUserDefinedFunction'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableFunction'>, <type 'IMutableScalar'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ISchema(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def ExtendedStoredProcedures(self) -> IMetadataCollection:
        """ Get: ExtendedStoredProcedures(self: ISchema) -> IMetadataCollection[IExtendedStoredProcedure] """
        ...

    @property
    def Owner(self) -> IDatabasePrincipal:
        """ Get: Owner(self: ISchema) -> IDatabasePrincipal """
        ...

    @property
    def ScalarValuedFunctions(self) -> IMetadataCollection:
        """ Get: ScalarValuedFunctions(self: ISchema) -> IMetadataCollection[IScalarValuedFunction] """
        ...

    @property
    def StoredProcedures(self) -> IMetadataCollection:
        """ Get: StoredProcedures(self: ISchema) -> IMetadataCollection[IStoredProcedure] """
        ...

    @property
    def Synonyms(self) -> IMetadataCollection:
        """ Get: Synonyms(self: ISchema) -> IMetadataCollection[ISynonym] """
        ...

    @property
    def Tables(self) -> IMetadataCollection:
        """ Get: Tables(self: ISchema) -> IMetadataCollection[ITable] """
        ...

    @property
    def TableValuedFunctions(self) -> IMetadataCollection:
        """ Get: TableValuedFunctions(self: ISchema) -> IMetadataCollection[ITableValuedFunction] """
        ...

    @property
    def UserDefinedAggregates(self) -> IMetadataCollection:
        """ Get: UserDefinedAggregates(self: ISchema) -> IMetadataCollection[IUserDefinedAggregate] """
        ...

    @property
    def UserDefinedClrTypes(self) -> IMetadataCollection:
        """ Get: UserDefinedClrTypes(self: ISchema) -> IMetadataCollection[IUserDefinedClrType] """
        ...

    @property
    def UserDefinedDataTypes(self) -> IMetadataCollection:
        """ Get: UserDefinedDataTypes(self: ISchema) -> IMetadataCollection[IUserDefinedDataType] """
        ...

    @property
    def UserDefinedTableTypes(self) -> IMetadataCollection:
        """ Get: UserDefinedTableTypes(self: ISchema) -> IMetadataCollection[IUserDefinedTableType] """
        ...

    @property
    def Views(self) -> IMetadataCollection:
        """ Get: Views(self: ISchema) -> IMetadataCollection[IView] """
        ...



class IMutableSchema(ISchema, IMutableDatabaseOwnedObject): # skipped bases: <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IServer(IDatabaseObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def CollationInfo(self) -> CollationInfo:
        """ Get: CollationInfo(self: IServer) -> CollationInfo """
        ...

    @property
    def Credentials(self) -> IMetadataCollection:
        """ Get: Credentials(self: IServer) -> IMetadataCollection[ICredential] """
        ...

    @property
    def Databases(self) -> IMetadataCollection:
        """ Get: Databases(self: IServer) -> IMetadataCollection[IDatabase] """
        ...

    @property
    def Logins(self) -> IMetadataCollection:
        """ Get: Logins(self: IServer) -> IMetadataCollection[ILogin] """
        ...

    @property
    def Triggers(self) -> IMetadataCollection:
        """ Get: Triggers(self: IServer) -> IMetadataCollection[IServerDdlTrigger] """
        ...



class IMutableServer(IServer, IMutableDatabaseObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IServerDdlTrigger(IServerOwnedObject, ITrigger): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: IServerDdlTrigger) -> bool """
        ...

    @property
    def ServerDdlEvents(self) -> ITriggerEventTypeSet:
        """ Get: ServerDdlEvents(self: IServerDdlTrigger) -> ITriggerEventTypeSet """
        ...



class IMutableServerDdlTrigger(IMutableTrigger, IMutableServerOwnedObject, IServerDdlTrigger): # skipped bases: <type 'IMutableMetadataObject'>, <type 'ITrigger'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IServerOwnedObject'>, <type 'object'>
    """ no doc """
    pass

class ISpatialIndex(IIndex): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def BoundingBoxXMax(self) -> float:
        """ Get: BoundingBoxXMax(self: ISpatialIndex) -> float """
        ...

    @property
    def BoundingBoxXMin(self) -> float:
        """ Get: BoundingBoxXMin(self: ISpatialIndex) -> float """
        ...

    @property
    def BoundingBoxYMax(self) -> float:
        """ Get: BoundingBoxYMax(self: ISpatialIndex) -> float """
        ...

    @property
    def BoundingBoxYMin(self) -> float:
        """ Get: BoundingBoxYMin(self: ISpatialIndex) -> float """
        ...

    @property
    def CellsPerObject(self) -> int:
        """ Get: CellsPerObject(self: ISpatialIndex) -> int """
        ...

    @property
    def IndexedColumn(self) -> IColumn:
        """ Get: IndexedColumn(self: ISpatialIndex) -> IColumn """
        ...

    @property
    def Level1Density(self) -> GridDensity:
        """ Get: Level1Density(self: ISpatialIndex) -> GridDensity """
        ...

    @property
    def Level2Density(self) -> GridDensity:
        """ Get: Level2Density(self: ISpatialIndex) -> GridDensity """
        ...

    @property
    def Level3Density(self) -> GridDensity:
        """ Get: Level3Density(self: ISpatialIndex) -> GridDensity """
        ...

    @property
    def Level4Density(self) -> GridDensity:
        """ Get: Level4Density(self: ISpatialIndex) -> GridDensity """
        ...

    @property
    def NoAutomaticRecomputation(self) -> bool:
        """ Get: NoAutomaticRecomputation(self: ISpatialIndex) -> bool """
        ...



class IMutableSpatialIndex(ISpatialIndex, IMutableIndex): # skipped bases: <type 'IIndex'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IStatistics(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> IMetadataOrderedCollection:
        """ Get: Columns(self: IStatistics) -> IMetadataOrderedCollection[IColumn] """
        ...

    @property
    def FilterDefinition(self) -> str:
        """ Get: FilterDefinition(self: IStatistics) -> str """
        ...

    @property
    def NoAutomaticRecomputation(self) -> bool:
        """ Get: NoAutomaticRecomputation(self: IStatistics) -> bool """
        ...

    @property
    def Parent(self) -> ITabular:
        """ Get: Parent(self: IStatistics) -> ITabular """
        ...

    @property
    def Type(self) -> StatisticsType:
        """ Get: Type(self: IStatistics) -> StatisticsType """
        ...



class IMutableStatistics(IStatistics, IMutableMetadataObject): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IStoredProcedure(ICallableModule): # skipped bases: <type 'IFunctionModuleBase'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def BodyText(self) -> str:
        """ Get: BodyText(self: IStoredProcedure) -> str """
        ...

    @property
    def ForReplication(self) -> bool:
        """ Get: ForReplication(self: IStoredProcedure) -> bool """
        ...

    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: IStoredProcedure) -> bool """
        ...

    @property
    def IsRecompiled(self) -> bool:
        """ Get: IsRecompiled(self: IStoredProcedure) -> bool """
        ...

    @property
    def IsSqlClr(self) -> bool:
        """ Get: IsSqlClr(self: IStoredProcedure) -> bool """
        ...

    @property
    def Startup(self) -> bool:
        """ Get: Startup(self: IStoredProcedure) -> bool """
        ...



class IMutableStoredProcedure(IMutableCallableModule, IStoredProcedure): # skipped bases: <type 'ICallableModule'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IFunctionModuleBase'>, <type 'IMutableDatabaseObject'>, <type 'IMutableUserDefinedFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMutableFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ISynonym(ISchemaOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def BaseObjectName(self) -> str:
        """ Get: BaseObjectName(self: ISynonym) -> str """
        ...

    @property
    def BaseType(self) -> SynonymBaseType:
        """ Get: BaseType(self: ISynonym) -> SynonymBaseType """
        ...



class IMutableSynonym(ISynonym): # skipped bases: <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ITableViewBase(IDatabaseTable, ISchemaOwnedObject): # skipped bases: <type 'ITabular'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsQuotedIdentifierOn(self) -> bool:
        """ Get: IsQuotedIdentifierOn(self: ITableViewBase) -> bool """
        ...

    @property
    def Triggers(self) -> IMetadataCollection:
        """ Get: Triggers(self: ITableViewBase) -> IMetadataCollection[IDmlTrigger] """
        ...



class IMutableTableViewBase(IMutableDatabaseTable, IMutableSchemaOwnedObject, ITableViewBase): # skipped bases: <type 'IMutableTabular'>, <type 'ISchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class ITable(ITableViewBase): # skipped bases: <type 'ITabular'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IMutableTable(IMutableTableViewBase, ITable): # skipped bases: <type 'IMutableTabular'>, <type 'IMutableDatabaseTable'>, <type 'ISchemaOwnedObject'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'ITableViewBase'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class ITableDataType(IDatabaseTable, IDataType): # skipped bases: <type 'ITabular'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableTableDataType(IMutableDatabaseTable, IMutableDataType, ITableDataType): # skipped bases: <type 'IDatabaseTable'>, <type 'IDataType'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'IMetadataObject'>, <type 'IMutableTabular'>, <type 'object'>
    """ no doc """
    pass

class ITableValuedFunction(IDatabaseTable, IUserDefinedFunction): # skipped bases: <type 'IFunction'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'ITabular'>, <type 'IFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsInline(self) -> bool:
        """ Get: IsInline(self: ITableValuedFunction) -> bool """
        ...

    @property
    def TableVariableName(self) -> str:
        """ Get: TableVariableName(self: ITableValuedFunction) -> str """
        ...



class IMutableTableValuedFunction(ITableValuedFunction, IMutableDatabaseTable, IMutableUserDefinedFunction): # skipped bases: <type 'IFunction'>, <type 'ISchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'IFunctionModuleBase'>, <type 'IMutableFunctionModuleBase'>, <type 'IMutableUserDefinedFunctionModuleBase'>, <type 'IUserDefinedFunction'>, <type 'IMutableTabular'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableFunction'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class ITriggerEventTypeSet(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, item:str) -> bool:
        """ Contains(self: ITriggerEventTypeSet, item: str) -> bool """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[str](enumerable: IEnumerable[str], value: str) -> bool """
        ...


class IMutableTriggerEventTypeSet(ITriggerEventTypeSet): # skipped bases: <type 'IEnumerable[str]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, item:str): # -> 
        """ Add(self: IMutableTriggerEventTypeSet, item: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IMutableTriggerEventTypeSet) """
        ...

    def Remove(self, item:str) -> bool:
        """ Remove(self: IMutableTriggerEventTypeSet, item: str) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class IUser(IDatabasePrincipal): # skipped bases: <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def AsymmetricKey(self) -> IAsymmetricKey:
        """ Get: AsymmetricKey(self: IUser) -> IAsymmetricKey """
        ...

    @property
    def Certificate(self) -> ICertificate:
        """ Get: Certificate(self: IUser) -> ICertificate """
        ...

    @property
    def DefaultSchema(self) -> ISchema:
        """ Get: DefaultSchema(self: IUser) -> ISchema """
        ...

    @property
    def Login(self) -> ILogin:
        """ Get: Login(self: IUser) -> ILogin """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: IUser) -> str """
        ...

    @property
    def UserType(self) -> UserType:
        """ Get: UserType(self: IUser) -> UserType """
        ...



class IMutableUser(IMutableDatabasePrincipal, IUser): # skipped bases: <type 'IMutableDatabaseOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IDatabasePrincipal'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IDatabaseOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedType(ISchemaOwnedObject, IDataType): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableUserDefinedType(IMutableDataType, IMutableSchemaOwnedObject, IUserDefinedType): # skipped bases: <type 'IDataType'>, <type 'ISchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedClrType(IClrDataType, IUserDefinedType): # skipped bases: <type 'IScalarDataType'>, <type 'IDataType'>, <type 'IDatabaseObject'>, <type 'ISchemaOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IMutableUserDefinedClrType(IMutableClrDataType, IUserDefinedClrType, IMutableUserDefinedType): # skipped bases: <type 'IDataType'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedType'>, <type 'IClrDataType'>, <type 'IMutableMetadataObject'>, <type 'IMutableScalarDataType'>, <type 'IMutableDataType'>, <type 'IMutableSchemaOwnedObject'>, <type 'IScalarDataType'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedDataType(IUserDefinedType, IScalarDataType): # skipped bases: <type 'IDataType'>, <type 'IDatabaseObject'>, <type 'ISchemaOwnedObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: IUserDefinedDataType) -> bool """
        ...



class IMutableUserDefinedDataType(IMutableUserDefinedType, IUserDefinedDataType, IMutableScalarDataType): # skipped bases: <type 'IMutableDataType'>, <type 'IDataType'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedType'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'IScalarDataType'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedTableType(IUserDefinedType, ITableDataType): # skipped bases: <type 'IDataType'>, <type 'ISchemaOwnedObject'>, <type 'ITabular'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IMutableUserDefinedTableType(IMutableUserDefinedType, IMutableTableDataType, IUserDefinedTableType): # skipped bases: <type 'IDataType'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedType'>, <type 'ITableDataType'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'IMutableTabular'>, <type 'IMutableDatabaseTable'>, <type 'IMutableDataType'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IView(ITableViewBase): # skipped bases: <type 'ITabular'>, <type 'ISchemaOwnedObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    @property
    def HasCheckOption(self) -> bool:
        """ Get: HasCheckOption(self: IView) -> bool """
        ...

    @property
    def HasColumnSpecification(self) -> bool:
        """ Get: HasColumnSpecification(self: IView) -> bool """
        ...

    @property
    def IsEncrypted(self) -> bool:
        """ Get: IsEncrypted(self: IView) -> bool """
        ...

    @property
    def IsSchemaBound(self) -> bool:
        """ Get: IsSchemaBound(self: IView) -> bool """
        ...

    @property
    def QueryText(self) -> str:
        """ Get: QueryText(self: IView) -> str """
        ...

    @property
    def ReturnsViewMetadata(self) -> bool:
        """ Get: ReturnsViewMetadata(self: IView) -> bool """
        ...



class IMutableView(IView, IMutableTableViewBase): # skipped bases: <type 'IMutableTabular'>, <type 'IMutableDatabaseTable'>, <type 'ISchemaOwnedObject'>, <type 'IMutableSchemaOwnedObject'>, <type 'IMutableMetadataObject'>, <type 'ITabular'>, <type 'ITableViewBase'>, <type 'IMutableDatabaseObject'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IVirtualTable(ITabular): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def TargetTable(self) -> ITabular:
        """ Get: TargetTable(self: IVirtualTable) -> ITabular """
        ...



class IMutableVirtualTable(IMutableTabular, IVirtualTable): # skipped bases: <type 'ITabular'>, <type 'IMetadataObject'>, <type 'IMutableMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IndexType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IndexType, values: Relational (0), Spatial (1), Xml (2) """
    Relational: IndexType = ...
    Spatial: IndexType = ...
    value__ = ...
    Xml: IndexType = ...


class IPartitionScheme(IDatabaseOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def FileGroups(self) -> IMetadataCollection:
        """ Get: FileGroups(self: IPartitionScheme) -> IMetadataCollection[IFileGroup] """
        ...



class IUniqueConstraintBase(IConstraint): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def AssociatedIndex(self) -> IRelationalIndex:
        """ Get: AssociatedIndex(self: IUniqueConstraintBase) -> IRelationalIndex """
        ...



class IPrimaryKeyConstraint(IUniqueConstraintBase): # skipped bases: <type 'IConstraint'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IResolvedSynonym(ISchemaOwnedObject): # skipped bases: <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Synonym(self) -> ISynonym:
        """ Get: Synonym(self: IResolvedSynonym) -> ISynonym """
        ...

    @property
    def TargetObject(self) -> ISchemaOwnedObject:
        """ Get: TargetObject(self: IResolvedSynonym) -> ISchemaOwnedObject """
        ...



class IResolvedExtendedStoredProcedureSynonym(IExtendedStoredProcedure, IResolvedSynonym): # skipped bases: <type 'ICallableModule'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IResolvedScalarValuedFunctionSynonym(IResolvedSynonym, IScalarValuedFunction): # skipped bases: <type 'IFunction'>, <type 'ICallableModule'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IScalarFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IUserDefinedFunction'>, <type 'object'>
    """ no doc """
    pass

class IResolvedStoredProcedureSynonym(IResolvedSynonym, IStoredProcedure): # skipped bases: <type 'ICallableModule'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'IFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IResolvedTableSynonym(IResolvedSynonym, ITable): # skipped bases: <type 'ISchemaOwnedObject'>, <type 'ITabular'>, <type 'ITableViewBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IResolvedTableValuedFunctionSynonym(ITableValuedFunction, IResolvedSynonym): # skipped bases: <type 'IFunction'>, <type 'IUserDefinedFunction'>, <type 'ISchemaOwnedObject'>, <type 'IUserDefinedFunctionModuleBase'>, <type 'ITabular'>, <type 'IFunctionModuleBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IUserDefinedAggregate(ISchemaOwnedObject, IScalarFunction): # skipped bases: <type 'IFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IResolvedUserDefinedAggregateSynonym(IResolvedSynonym, IUserDefinedAggregate): # skipped bases: <type 'IFunction'>, <type 'ISchemaOwnedObject'>, <type 'IScalarFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IResolvedViewSynonym(IView, IResolvedSynonym): # skipped bases: <type 'ISchemaOwnedObject'>, <type 'ITabular'>, <type 'ITableViewBase'>, <type 'IDatabaseObject'>, <type 'IMetadataObject'>, <type 'IDatabaseTable'>, <type 'object'>
    """ no doc """
    pass

class IScalarExpression(IScalar): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IScalarVariable(ILocalVariable, IScalar): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IScalarParameter(IParameter, IScalarVariable): # skipped bases: <type 'IScalar'>, <type 'IMetadataObject'>, <type 'ILocalVariable'>, <type 'object'>
    """ no doc """
    pass

class ISchemaOwnedObjectVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, *__args:IExtendedStoredProcedure): # -> T
        """
        Visit(self: ISchemaOwnedObjectVisitor[T], extendedStoredProcedure: IExtendedStoredProcedure) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], scalarValuedFunction: IScalarValuedFunction) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], storedProcedure: IStoredProcedure) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], synonym: ISynonym) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], table: ITable) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], tableValuedFunction: ITableValuedFunction) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], userDefinedAggregate: IUserDefinedAggregate) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], userDefinedClrType: IUserDefinedClrType) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], userDefinedDataType: IUserDefinedDataType) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], userDefinedTableType: IUserDefinedTableType) -> T
        Visit(self: ISchemaOwnedObjectVisitor[T], view: IView) -> T
        """
        ...


class IServerOwnedObjectVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def Visit(self, *__args:ICredential): # -> T
        """
        Visit(self: IServerOwnedObjectVisitor[T], credential: ICredential) -> T
        Visit(self: IServerOwnedObjectVisitor[T], database: IDatabase) -> T
        Visit(self: IServerOwnedObjectVisitor[T], login: ILogin) -> T
        Visit(self: IServerOwnedObjectVisitor[T], serverDdlTrigger: IServerDdlTrigger) -> T
        """
        ...


class ISystemDataType(IScalarDataType): # skipped bases: <type 'IDataType'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def Length(self) -> int:
        """ Get: Length(self: ISystemDataType) -> int """
        ...

    @property
    def NumericPrecision(self) -> int:
        """ Get: NumericPrecision(self: ISystemDataType) -> int """
        ...

    @property
    def NumericScale(self) -> int:
        """ Get: NumericScale(self: ISystemDataType) -> int """
        ...

    @property
    def TypeSpec(self) -> DataTypeSpec:
        """ Get: TypeSpec(self: ISystemDataType) -> DataTypeSpec """
        ...



class ISystemClrDataType(ISystemDataType, IClrDataType): # skipped bases: <type 'IScalarDataType'>, <type 'IDataType'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ITableVariable(ILocalVariable, ITabular): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class ITableParameter(IParameter, ITableVariable): # skipped bases: <type 'ITabular'>, <type 'IMetadataObject'>, <type 'ILocalVariable'>, <type 'object'>
    """ no doc """
    pass

class IUdtMember(IScalar): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: IUdtMember) -> bool """
        ...

    @property
    def UserDefinedType(self) -> IClrDataType:
        """ Get: UserDefinedType(self: IUdtMember) -> IClrDataType """
        ...



class IUdtDataMember(IUdtMember): # skipped bases: <type 'IScalar'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUdtMethod(IScalarFunction, IUdtMember): # skipped bases: <type 'IFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IUniqueConstraint(IUniqueConstraintBase): # skipped bases: <type 'IConstraint'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IVoidDataType(IScalarDataType): # skipped bases: <type 'IDataType'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IXmlDataType(ISystemDataType): # skipped bases: <type 'IScalarDataType'>, <type 'IDataType'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    @property
    def IsXmlNode(self) -> bool:
        """ Get: IsXmlNode(self: IXmlDataType) -> bool """
        ...

    @property
    def Methods(self) -> IMetadataCollection:
        """ Get: Methods(self: IXmlDataType) -> IMetadataCollection[IXmlDataTypeMethod] """
        ...

    @property
    def TableMethods(self) -> IMetadataCollection:
        """ Get: TableMethods(self: IXmlDataType) -> IMetadataCollection[IXmlDataTypeTableMethod] """
        ...



class IXmlDataTypeMethod(IScalarFunction): # skipped bases: <type 'IFunction'>, <type 'IFunctionModuleBase'>, <type 'IScalar'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IXmlDataTypeTableMethod(IFunction): # skipped bases: <type 'IFunctionModuleBase'>, <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class IXmlIndex(IIndex): # skipped bases: <type 'IMetadataObject'>, <type 'object'>
    """ no doc """
    pass

class LoginType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoginType, values: AsymmetricKey (0), Certificate (1), Sql (2), Windows (3) """
    AsymmetricKey: LoginType = ...
    Certificate: LoginType = ...
    Sql: LoginType = ...
    value__ = ...
    Windows: LoginType = ...


class PermissionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PermissionState, values: Deny (0), Grant (1), GrantWithGrant (2), Revoke (3) """
    Deny: PermissionState = ...
    Grant: PermissionState = ...
    GrantWithGrant: PermissionState = ...
    Revoke: PermissionState = ...
    value__ = ...


class ScalarType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ScalarType, values: Column (0), Expression (1), Literal (2), Null (3), ScalarFunction (4), ScalarVariable (5), UdtMember (6) """
    Column: ScalarType = ...
    Expression: ScalarType = ...
    Literal: ScalarType = ...
    Null: ScalarType = ...
    ScalarFunction: ScalarType = ...
    ScalarVariable: ScalarType = ...
    UdtMember: ScalarType = ...
    value__ = ...


class SortOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SortOrder, values: Ascending (0), Descending (1) """
    Ascending: SortOrder = ...
    Descending: SortOrder = ...
    value__ = ...


class SqlDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDataType, values: BigInt (1), Binary (2), Bit (3), Char (4), Date (5), DateTime (6), DateTime2 (7), DateTimeOffset (8), Decimal (9), Float (10), Geography (11), Geometry (12), HierarchyId (13), Image (14), Int (15), Money (16), NChar (17), None (0), NText (18), Numeric (19), NVarChar (20), NVarCharMax (21), Real (22), SmallDateTime (23), SmallInt (24), SmallMoney (25), SysName (26), Text (27), Time (28), Timestamp (29), TinyInt (30), UniqueIdentifier (31), VarBinary (32), VarBinaryMax (33), VarChar (34), VarCharMax (35), Variant (36), Xml (37), XmlNode (38) """
    BigInt: SqlDataType = ...
    Binary: SqlDataType = ...
    Bit: SqlDataType = ...
    Char: SqlDataType = ...
    Date: SqlDataType = ...
    DateTime: SqlDataType = ...
    DateTime2: SqlDataType = ...
    DateTimeOffset: SqlDataType = ...
    Decimal: SqlDataType = ...
    Float: SqlDataType = ...
    Geography: SqlDataType = ...
    Geometry: SqlDataType = ...
    HierarchyId: SqlDataType = ...
    Image: SqlDataType = ...
    Int: SqlDataType = ...
    Money: SqlDataType = ...
    NChar: SqlDataType = ...
    NText: SqlDataType = ...
    Numeric: SqlDataType = ...
    NVarChar: SqlDataType = ...
    NVarCharMax: SqlDataType = ...
    Real: SqlDataType = ...
    SmallDateTime: SqlDataType = ...
    SmallInt: SqlDataType = ...
    SmallMoney: SqlDataType = ...
    SysName: SqlDataType = ...
    Text: SqlDataType = ...
    Time: SqlDataType = ...
    Timestamp: SqlDataType = ...
    TinyInt: SqlDataType = ...
    UniqueIdentifier: SqlDataType = ...
    value__ = ...
    VarBinary: SqlDataType = ...
    VarBinaryMax: SqlDataType = ...
    VarChar: SqlDataType = ...
    VarCharMax: SqlDataType = ...
    Variant: SqlDataType = ...
    Xml: SqlDataType = ...
    XmlNode: SqlDataType = ...


class StatisticsType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StatisticsType, values: Auto (2), Explicit (0), ImplicitViaIndex (1) """
    Auto: StatisticsType = ...
    Explicit: StatisticsType = ...
    ImplicitViaIndex: StatisticsType = ...
    value__ = ...


class SynonymBaseType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynonymBaseType, values: ClrAggregateFunction (1), ClrScalarFunction (2), ClrStoredProcedure (3), ClrTableValuedFunction (4), ExtendedStoredProcedure (5), None (0), ReplicationFilterProcedure (6), SqlInlineTableValuedFunction (7), SqlScalarFunction (8), SqlStoredProcedure (9), SqlTableValuedFunction (10), Table (11), View (12) """
    ClrAggregateFunction: SynonymBaseType = ...
    ClrScalarFunction: SynonymBaseType = ...
    ClrStoredProcedure: SynonymBaseType = ...
    ClrTableValuedFunction: SynonymBaseType = ...
    ExtendedStoredProcedure: SynonymBaseType = ...
    ReplicationFilterProcedure: SynonymBaseType = ...
    SqlInlineTableValuedFunction: SynonymBaseType = ...
    SqlScalarFunction: SynonymBaseType = ...
    SqlStoredProcedure: SynonymBaseType = ...
    SqlTableValuedFunction: SynonymBaseType = ...
    Table: SynonymBaseType = ...
    value__ = ...
    View: SynonymBaseType = ...


class TabularType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TabularType, values: CommonTableExpression (0), DerivedTable (1), DmlInsertedDeleted (2), DmlTableSource (3), PivotTable (4), Table (5), TableAlias (6), TableDataType (7), TableValuedFunction (8), TableVariable (9), TemporaryTable (10), UnpivotTable (11), View (12) """
    CommonTableExpression: TabularType = ...
    DerivedTable: TabularType = ...
    DmlInsertedDeleted: TabularType = ...
    DmlTableSource: TabularType = ...
    PivotTable: TabularType = ...
    Table: TabularType = ...
    TableAlias: TabularType = ...
    TableDataType: TabularType = ...
    TableValuedFunction: TabularType = ...
    TableVariable: TabularType = ...
    TemporaryTable: TabularType = ...
    UnpivotTable: TabularType = ...
    value__ = ...
    View: TabularType = ...


class TriggerEventTypeSet(IMutableTriggerEventTypeSet): # skipped bases: <type 'IEnumerable[str]'>, <type 'ITriggerEventTypeSet'>, <type 'IEnumerable'>, <type 'object'>
    """ TriggerEventTypeSet() """
    def Contains(self, item:str) -> bool:
        """ Contains(self: TriggerEventTypeSet, item: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TriggerEventTypeSet) -> IEnumerator[str] """
        ...


class UserType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UserType, values: AsymmetricKey (0), Certificate (1), External (5), NoLogin (2), Password (4), SqlLogin (3) """
    AsymmetricKey: UserType = ...
    Certificate: UserType = ...
    External: UserType = ...
    NoLogin: UserType = ...
    Password: UserType = ...
    SqlLogin: UserType = ...
    value__ = ...


