# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.MetadataSerialization calls itself MetadataSerialization
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

"""The following names are not found in the module: field#
"""

# no functions
# classes

class XmlNestingType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlNestingType, values: InlineDynamicType (1), InlineStaticType (2), Standalone (0) """
    InlineDynamicType: XmlNestingType = ...
    InlineStaticType: XmlNestingType = ...
    Standalone: XmlNestingType = ...
    value__ = ...


class XmlToken(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlToken, values: ApplicationRole (138), ApplicationRoles (156), AssemblyName (95), AssociatedIndex (139), AsymmetricKey (110), AsymmetricKeys (124), BaseObjectName (125), BaseSystemDataType (175), BaseType (34), BodyText (35), BoundingBoxXMax (140), BoundingBoxXMin (141), BoundingBoxYMax (142), BoundingBoxYMin (143), CellsPerObject (126), Certificate (82), Certificates (96), CheckConstraint (144), ClassName (54), ClrDataType (83), Collation (55), CollationInfo (111), Column (17), Columns (27), CompactLargeObjects (182), CompatibilityLevel (176), ComputedColumnInfo (177), Constraints (84), ContextType (85), Credential (70), Credentials (86), CursorDataType (127), CursorParameter (145), CursorVariable (128), Database (36), DatabaseDdlEvents (166), DatabaseDdlTrigger (178), DatabasePermission (179), DatabasePrincipal (167), DatabaseRole (97), Databases (56), DataMembers (87), DataType (37), DefaultConstraint (168), DefaultDatabase (146), DefaultSchema (112), DefaultSchemaName (169), DefaultValue (98), Delete (18), DeleteAction (99), DeleteActivationOrder (197), DisallowPageLocks (170), DisallowRowLocks (157), DmlTrigger (71), ExecutionContext (158), ExtendedStoredProcedure (205), ExtendedStoredProcedures (206), FileGroup (57), FileGroups (72), FileStreamFileGroup (183), FileStreamPartitionScheme (208), FillFactor (73), FilterDefinition (159), ForeignKeyColumn (160), ForeignKeyConstraint (189), ForReplication (129), Grantor (28), HasCheckOption (130), HasColumnSpecification (203), IdentityColumnInfo (180), IgnoreDuplicateKeys (184), Increment (58), IndexedColumn (113), IndexedColumns (131), Indexes (29), IndexKey (38), InPrimaryKey (100), Insert (19), InsertActivationOrder (198), Instances (59), InsteadOf (60), IsBinaryOrdered (147), IsChecked (61), IsClustered (88), IsColumnSet (89), IsComVisible (101), IsDefault (62), IsDisabled (74), IsEnabled (63), IsEncrypted (90), IsFileStream (102), IsFixedRole (91), IsGeneratedAlwaysAsRowEnd (209), IsGeneratedAlwaysAsRowStart (210), IsIncluded (75), IsInline (39), IsNullable (76), IsOutput (40), IsPersisted (92), IsQuotedIdentifierOn (190), IsReadOnly (77), IsRecompiled (103), IsSchemaBound (114), IsSparse (41), IsSqlClr (42), IsStatic (43), IsSystemNamed (115), IsSystemObject (132), IsUnique (44), IsXmlNode (64), Key (3), Language (45), Length (20), Level1Density (116), Level2Density (117), Level3Density (118), Level4Density (119), Login (11), Logins (21), LoginType (65), MemberOfRoles (120), Methods (30), MM (1), Name (5), NoAutomaticRecomputation (207), None (0), NotForReplication (171), Nullable (46), NumericPrecision (161), NumericScale (104), Owner (12), PadIndex (47), Parameters (78), Parent (22), PartitionScheme (148), Password (48), Permissions (93), PermissionState (149), PermissionType (133), PrimaryKeyConstraint (191), QueryText (66), RE (2), Reference (67), ReferencedColumn (162), ReferencedTable (150), ReferenceKey (105), ReferencingColumn (172), RelationalIndex (151), ReturnsNullOnNullInput (204), ReturnsViewMetadata (185), ReturnType (79), Roles (13), RowGuidCol (80), ScalarDataType (134), ScalarParameter (152), ScalarValuedFunction (192), ScalarValuedFunctions (199), ScalarVariable (135), Schema (23), Schemas (31), Seed (6), Server (24), ServerDdlEvents (153), ServerDdlTrigger (163), Sid (4), SortOrder (68), SpatialIndex (106), Startup (32), Statistics (81), StoredProcedure (154), StoredProcedures (164), Synonym (33), Synonyms (49), SystemClrDataType (173), SystemDataType (136), Table (14), TableDataType (121), TableParameter (137), Tables (25), TableValuedFunction (186), TableValuedFunctions (193), TableVariable (122), TableVariableName (174), TargetObject (107), Text (7), Triggers (50), Type (8), TypeSpec (51), UdtDataMember (123), UdtMethod (69), UniqueConstraint (165), Update (26), UpdateAction (108), UpdateActivationOrder (200), User (9), UserDefinedAggregate (194), UserDefinedAggregates (201), UserDefinedClrType (181), UserDefinedClrTypes (187), UserDefinedDataType (188), UserDefinedDataTypes (195), UserDefinedTableType (196), UserDefinedTableTypes (202), UserDefinedType (155), Users (15), UserType (52), View (10), Views (16), VoidDataType (109), XmlDataType (94), XmlIndex (53) """
    ApplicationRole: XmlToken = ...
    ApplicationRoles: XmlToken = ...
    AssemblyName: XmlToken = ...
    AssociatedIndex: XmlToken = ...
    AsymmetricKey: XmlToken = ...
    AsymmetricKeys: XmlToken = ...
    BaseObjectName: XmlToken = ...
    BaseSystemDataType: XmlToken = ...
    BaseType: XmlToken = ...
    BodyText: XmlToken = ...
    BoundingBoxXMax: XmlToken = ...
    BoundingBoxXMin: XmlToken = ...
    BoundingBoxYMax: XmlToken = ...
    BoundingBoxYMin: XmlToken = ...
    CellsPerObject: XmlToken = ...
    Certificate: XmlToken = ...
    Certificates: XmlToken = ...
    CheckConstraint: XmlToken = ...
    ClassName: XmlToken = ...
    ClrDataType: XmlToken = ...
    Collation: XmlToken = ...
    CollationInfo: XmlToken = ...
    Column: XmlToken = ...
    Columns: XmlToken = ...
    CompactLargeObjects: XmlToken = ...
    CompatibilityLevel: XmlToken = ...
    ComputedColumnInfo: XmlToken = ...
    Constraints: XmlToken = ...
    ContextType: XmlToken = ...
    Credential: XmlToken = ...
    Credentials: XmlToken = ...
    CursorDataType: XmlToken = ...
    CursorParameter: XmlToken = ...
    CursorVariable: XmlToken = ...
    Database: XmlToken = ...
    DatabaseDdlEvents: XmlToken = ...
    DatabaseDdlTrigger: XmlToken = ...
    DatabasePermission: XmlToken = ...
    DatabasePrincipal: XmlToken = ...
    DatabaseRole: XmlToken = ...
    Databases: XmlToken = ...
    DataMembers: XmlToken = ...
    DataType: XmlToken = ...
    DefaultConstraint: XmlToken = ...
    DefaultDatabase: XmlToken = ...
    DefaultSchema: XmlToken = ...
    DefaultSchemaName: XmlToken = ...
    DefaultValue: XmlToken = ...
    Delete: XmlToken = ...
    DeleteAction: XmlToken = ...
    DeleteActivationOrder: XmlToken = ...
    DisallowPageLocks: XmlToken = ...
    DisallowRowLocks: XmlToken = ...
    DmlTrigger: XmlToken = ...
    ExecutionContext: XmlToken = ...
    ExtendedStoredProcedure: XmlToken = ...
    ExtendedStoredProcedures: XmlToken = ...
    FileGroup: XmlToken = ...
    FileGroups: XmlToken = ...
    FileStreamFileGroup: XmlToken = ...
    FileStreamPartitionScheme: XmlToken = ...
    FillFactor: XmlToken = ...
    FilterDefinition: XmlToken = ...
    ForeignKeyColumn: XmlToken = ...
    ForeignKeyConstraint: XmlToken = ...
    ForReplication: XmlToken = ...
    Grantor: XmlToken = ...
    HasCheckOption: XmlToken = ...
    HasColumnSpecification: XmlToken = ...
    IdentityColumnInfo: XmlToken = ...
    IgnoreDuplicateKeys: XmlToken = ...
    Increment: XmlToken = ...
    IndexedColumn: XmlToken = ...
    IndexedColumns: XmlToken = ...
    Indexes: XmlToken = ...
    IndexKey: XmlToken = ...
    InPrimaryKey: XmlToken = ...
    Insert: XmlToken = ...
    InsertActivationOrder: XmlToken = ...
    Instances: XmlToken = ...
    InsteadOf: XmlToken = ...
    IsBinaryOrdered: XmlToken = ...
    IsChecked: XmlToken = ...
    IsClustered: XmlToken = ...
    IsColumnSet: XmlToken = ...
    IsComVisible: XmlToken = ...
    IsDefault: XmlToken = ...
    IsDisabled: XmlToken = ...
    IsEnabled: XmlToken = ...
    IsEncrypted: XmlToken = ...
    IsFileStream: XmlToken = ...
    IsFixedRole: XmlToken = ...
    IsGeneratedAlwaysAsRowEnd: XmlToken = ...
    IsGeneratedAlwaysAsRowStart: XmlToken = ...
    IsIncluded: XmlToken = ...
    IsInline: XmlToken = ...
    IsNullable: XmlToken = ...
    IsOutput: XmlToken = ...
    IsPersisted: XmlToken = ...
    IsQuotedIdentifierOn: XmlToken = ...
    IsReadOnly: XmlToken = ...
    IsRecompiled: XmlToken = ...
    IsSchemaBound: XmlToken = ...
    IsSparse: XmlToken = ...
    IsSqlClr: XmlToken = ...
    IsStatic: XmlToken = ...
    IsSystemNamed: XmlToken = ...
    IsSystemObject: XmlToken = ...
    IsUnique: XmlToken = ...
    IsXmlNode: XmlToken = ...
    Key: XmlToken = ...
    Language: XmlToken = ...
    Length: XmlToken = ...
    Level1Density: XmlToken = ...
    Level2Density: XmlToken = ...
    Level3Density: XmlToken = ...
    Level4Density: XmlToken = ...
    Login: XmlToken = ...
    Logins: XmlToken = ...
    LoginType: XmlToken = ...
    MemberOfRoles: XmlToken = ...
    Methods: XmlToken = ...
    MM: XmlToken = ...
    Name: XmlToken = ...
    NoAutomaticRecomputation: XmlToken = ...
    NotForReplication: XmlToken = ...
    Nullable: XmlToken = ...
    NumericPrecision: XmlToken = ...
    NumericScale: XmlToken = ...
    Owner: XmlToken = ...
    PadIndex: XmlToken = ...
    Parameters: XmlToken = ...
    Parent: XmlToken = ...
    PartitionScheme: XmlToken = ...
    Password: XmlToken = ...
    Permissions: XmlToken = ...
    PermissionState: XmlToken = ...
    PermissionType: XmlToken = ...
    PrimaryKeyConstraint: XmlToken = ...
    QueryText: XmlToken = ...
    RE: XmlToken = ...
    Reference: XmlToken = ...
    ReferencedColumn: XmlToken = ...
    ReferencedTable: XmlToken = ...
    ReferenceKey: XmlToken = ...
    ReferencingColumn: XmlToken = ...
    RelationalIndex: XmlToken = ...
    ReturnsNullOnNullInput: XmlToken = ...
    ReturnsViewMetadata: XmlToken = ...
    ReturnType: XmlToken = ...
    Roles: XmlToken = ...
    RowGuidCol: XmlToken = ...
    ScalarDataType: XmlToken = ...
    ScalarParameter: XmlToken = ...
    ScalarValuedFunction: XmlToken = ...
    ScalarValuedFunctions: XmlToken = ...
    ScalarVariable: XmlToken = ...
    Schema: XmlToken = ...
    Schemas: XmlToken = ...
    Seed: XmlToken = ...
    Server: XmlToken = ...
    ServerDdlEvents: XmlToken = ...
    ServerDdlTrigger: XmlToken = ...
    Sid: XmlToken = ...
    SortOrder: XmlToken = ...
    SpatialIndex: XmlToken = ...
    Startup: XmlToken = ...
    Statistics: XmlToken = ...
    StoredProcedure: XmlToken = ...
    StoredProcedures: XmlToken = ...
    Synonym: XmlToken = ...
    Synonyms: XmlToken = ...
    SystemClrDataType: XmlToken = ...
    SystemDataType: XmlToken = ...
    Table: XmlToken = ...
    TableDataType: XmlToken = ...
    TableParameter: XmlToken = ...
    Tables: XmlToken = ...
    TableValuedFunction: XmlToken = ...
    TableValuedFunctions: XmlToken = ...
    TableVariable: XmlToken = ...
    TableVariableName: XmlToken = ...
    TargetObject: XmlToken = ...
    Text: XmlToken = ...
    Triggers: XmlToken = ...
    Type: XmlToken = ...
    TypeSpec: XmlToken = ...
    UdtDataMember: XmlToken = ...
    UdtMethod: XmlToken = ...
    UniqueConstraint: XmlToken = ...
    Update: XmlToken = ...
    UpdateAction: XmlToken = ...
    UpdateActivationOrder: XmlToken = ...
    User: XmlToken = ...
    UserDefinedAggregate: XmlToken = ...
    UserDefinedAggregates: XmlToken = ...
    UserDefinedClrType: XmlToken = ...
    UserDefinedClrTypes: XmlToken = ...
    UserDefinedDataType: XmlToken = ...
    UserDefinedDataTypes: XmlToken = ...
    UserDefinedTableType: XmlToken = ...
    UserDefinedTableTypes: XmlToken = ...
    UserDefinedType: XmlToken = ...
    Users: XmlToken = ...
    UserType: XmlToken = ...
    value__ = ...
    View: XmlToken = ...
    Views: XmlToken = ...
    VoidDataType: XmlToken = ...
    XmlDataType: XmlToken = ...
    XmlIndex: XmlToken = ...

