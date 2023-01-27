# encoding: utf-8
# module System.DirectoryServices.ActiveDirectory calls itself ActiveDirectory
# from System.DirectoryServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, DayOfWeek, Enum, Guid, 
    IAsyncResult, IDisposable, Int64, MulticastDelegate, Nullable, TimeSpan, 
    Type)

from System.Collections import (CollectionBase, DictionaryBase, 
    ReadOnlyCollectionBase)

from System.Collections.Specialized import StringCollection

from System.DirectoryServices import (ActiveDirectorySecurity, DirectoryEntry, 
    DirectorySearcher)

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    ReplicationNeighborOptions, field#)
"""

# no functions
# classes

class ActiveDirectoryInterSiteTransport(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BridgeAllSiteLinks(self) -> bool:
        """
        Get: BridgeAllSiteLinks(self: ActiveDirectoryInterSiteTransport) -> bool
        Set: BridgeAllSiteLinks(self: ActiveDirectoryInterSiteTransport) = value
        """
        ...

    @property
    def IgnoreReplicationSchedule(self) -> bool:
        """
        Get: IgnoreReplicationSchedule(self: ActiveDirectoryInterSiteTransport) -> bool
        Set: IgnoreReplicationSchedule(self: ActiveDirectoryInterSiteTransport) = value
        """
        ...

    @property
    def SiteLinkBridges(self) -> ReadOnlySiteLinkBridgeCollection:
        """ Get: SiteLinkBridges(self: ActiveDirectoryInterSiteTransport) -> ReadOnlySiteLinkBridgeCollection """
        ...

    @property
    def SiteLinks(self) -> ReadOnlySiteLinkCollection:
        """ Get: SiteLinks(self: ActiveDirectoryInterSiteTransport) -> ReadOnlySiteLinkCollection """
        ...

    @property
    def TransportType(self) -> ActiveDirectoryTransportType:
        """ Get: TransportType(self: ActiveDirectoryInterSiteTransport) -> ActiveDirectoryTransportType """
        ...


    @staticmethod
    def FindByTransportType(context:DirectoryContext, transport:ActiveDirectoryTransportType) -> ActiveDirectoryInterSiteTransport:
        """ FindByTransportType(context: DirectoryContext, transport: ActiveDirectoryTransportType) -> ActiveDirectoryInterSiteTransport """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectoryInterSiteTransport) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectoryInterSiteTransport) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectoryInterSiteTransport) -> str """
        ...


class ActiveDirectoryObjectExistsException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActiveDirectoryObjectExistsException(message: str, inner: Exception)
    ActiveDirectoryObjectExistsException(message: str)
    ActiveDirectoryObjectExistsException()
    """
    SerializeObjectState = ...


class ActiveDirectoryObjectNotFoundException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActiveDirectoryObjectNotFoundException(message: str, type: Type, name: str)
    ActiveDirectoryObjectNotFoundException(message: str, inner: Exception)
    ActiveDirectoryObjectNotFoundException(message: str)
    ActiveDirectoryObjectNotFoundException()
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectoryObjectNotFoundException) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ActiveDirectoryObjectNotFoundException) -> Type """
        ...


    SerializeObjectState = ...


class ActiveDirectoryOperationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActiveDirectoryOperationException(message: str, inner: Exception, errorCode: int)
    ActiveDirectoryOperationException(message: str, errorCode: int)
    ActiveDirectoryOperationException(message: str, inner: Exception)
    ActiveDirectoryOperationException(message: str)
    ActiveDirectoryOperationException()
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: ActiveDirectoryOperationException) -> int """
        ...


    SerializeObjectState = ...


class ActiveDirectoryPartition(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectoryPartition) -> str """
        ...


    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectoryPartition) -> DirectoryEntry """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectoryPartition) -> str """
        ...


class ActiveDirectoryReplicationMetadata(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def AttributeNames(self) -> ReadOnlyStringCollection:
        """ Get: AttributeNames(self: ActiveDirectoryReplicationMetadata) -> ReadOnlyStringCollection """
        ...

    @property
    def Values(self) -> AttributeMetadataCollection:
        """ Get: Values(self: ActiveDirectoryReplicationMetadata) -> AttributeMetadataCollection """
        ...


    def Contains(self, attributeName:str) -> bool:
        """ Contains(self: ActiveDirectoryReplicationMetadata, attributeName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ActiveDirectoryRole(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActiveDirectoryRole, values: InfrastructureRole (4), NamingRole (1), PdcRole (2), RidRole (3), SchemaRole (0) """
    InfrastructureRole: ActiveDirectoryRole = ...
    NamingRole: ActiveDirectoryRole = ...
    PdcRole: ActiveDirectoryRole = ...
    RidRole: ActiveDirectoryRole = ...
    SchemaRole: ActiveDirectoryRole = ...
    value__ = ...


class ActiveDirectoryRoleCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, role:ActiveDirectoryRole) -> bool:
        """ Contains(self: ActiveDirectoryRoleCollection, role: ActiveDirectoryRole) -> bool """
        ...

    def CopyTo(self, roles:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectoryRoleCollection, roles: Array[ActiveDirectoryRole], index: int) """
        ...

    def IndexOf(self, role:ActiveDirectoryRole) -> int:
        """ IndexOf(self: ActiveDirectoryRoleCollection, role: ActiveDirectoryRole) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ActiveDirectorySchedule: # skipped bases: <type 'object'>, <type 'object'>
    """
    ActiveDirectorySchedule()
    ActiveDirectorySchedule(schedule: ActiveDirectorySchedule)
    """
    @property
    def RawSchedule(self) -> Array:
        """
        Get: RawSchedule(self: ActiveDirectorySchedule) -> Array[bool]
        Set: RawSchedule(self: ActiveDirectorySchedule) = value
        """
        ...


    def ResetSchedule(self): # -> 
        """ ResetSchedule(self: ActiveDirectorySchedule) """
        ...

    def SetDailySchedule(self, fromHour:HourOfDay, fromMinute:MinuteOfHour, toHour:HourOfDay, toMinute:MinuteOfHour): # -> 
        """ SetDailySchedule(self: ActiveDirectorySchedule, fromHour: HourOfDay, fromMinute: MinuteOfHour, toHour: HourOfDay, toMinute: MinuteOfHour) """
        ...

    def SetSchedule(self, *__args): # -> 
        """ SetSchedule(self: ActiveDirectorySchedule, day: DayOfWeek, fromHour: HourOfDay, fromMinute: MinuteOfHour, toHour: HourOfDay, toMinute: MinuteOfHour)SetSchedule(self: ActiveDirectorySchedule, days: Array[DayOfWeek], fromHour: HourOfDay, fromMinute: MinuteOfHour, toHour: HourOfDay, toMinute: MinuteOfHour) """
        ...


class ActiveDirectorySchema(ActiveDirectoryPartition): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def SchemaRoleOwner(self) -> DirectoryServer:
        """ Get: SchemaRoleOwner(self: ActiveDirectorySchema) -> DirectoryServer """
        ...


    def FindAllClasses(self, type:SchemaClassType = ...) -> ReadOnlyActiveDirectorySchemaClassCollection:
        """
        FindAllClasses(self: ActiveDirectorySchema) -> ReadOnlyActiveDirectorySchemaClassCollection
        FindAllClasses(self: ActiveDirectorySchema, type: SchemaClassType) -> ReadOnlyActiveDirectorySchemaClassCollection
        """
        ...

    def FindAllDefunctClasses(self) -> ReadOnlyActiveDirectorySchemaClassCollection:
        """ FindAllDefunctClasses(self: ActiveDirectorySchema) -> ReadOnlyActiveDirectorySchemaClassCollection """
        ...

    def FindAllDefunctProperties(self) -> ReadOnlyActiveDirectorySchemaPropertyCollection:
        """ FindAllDefunctProperties(self: ActiveDirectorySchema) -> ReadOnlyActiveDirectorySchemaPropertyCollection """
        ...

    def FindAllProperties(self, type:PropertyTypes = ...) -> ReadOnlyActiveDirectorySchemaPropertyCollection:
        """
        FindAllProperties(self: ActiveDirectorySchema) -> ReadOnlyActiveDirectorySchemaPropertyCollection
        FindAllProperties(self: ActiveDirectorySchema, type: PropertyTypes) -> ReadOnlyActiveDirectorySchemaPropertyCollection
        """
        ...

    def FindClass(self, ldapDisplayName:str) -> ActiveDirectorySchemaClass:
        """ FindClass(self: ActiveDirectorySchema, ldapDisplayName: str) -> ActiveDirectorySchemaClass """
        ...

    def FindDefunctClass(self, commonName:str) -> ActiveDirectorySchemaClass:
        """ FindDefunctClass(self: ActiveDirectorySchema, commonName: str) -> ActiveDirectorySchemaClass """
        ...

    def FindDefunctProperty(self, commonName:str) -> ActiveDirectorySchemaProperty:
        """ FindDefunctProperty(self: ActiveDirectorySchema, commonName: str) -> ActiveDirectorySchemaProperty """
        ...

    def FindProperty(self, ldapDisplayName:str) -> ActiveDirectorySchemaProperty:
        """ FindProperty(self: ActiveDirectorySchema, ldapDisplayName: str) -> ActiveDirectorySchemaProperty """
        ...

    @staticmethod
    def GetCurrentSchema() -> ActiveDirectorySchema:
        """ GetCurrentSchema() -> ActiveDirectorySchema """
        ...

    @staticmethod
    def GetSchema(context:DirectoryContext) -> ActiveDirectorySchema:
        """ GetSchema(context: DirectoryContext) -> ActiveDirectorySchema """
        ...

    def RefreshSchema(self): # -> 
        """ RefreshSchema(self: ActiveDirectorySchema) """
        ...


class ActiveDirectorySchemaClass(IDisposable): # skipped bases: <type 'object'>
    """ ActiveDirectorySchemaClass(context: DirectoryContext, ldapDisplayName: str) """
    @property
    def AuxiliaryClasses(self) -> ActiveDirectorySchemaClassCollection:
        """ Get: AuxiliaryClasses(self: ActiveDirectorySchemaClass) -> ActiveDirectorySchemaClassCollection """
        ...

    @property
    def CommonName(self) -> str:
        """
        Get: CommonName(self: ActiveDirectorySchemaClass) -> str
        Set: CommonName(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def DefaultObjectSecurityDescriptor(self) -> ActiveDirectorySecurity:
        """
        Get: DefaultObjectSecurityDescriptor(self: ActiveDirectorySchemaClass) -> ActiveDirectorySecurity
        Set: DefaultObjectSecurityDescriptor(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ActiveDirectorySchemaClass) -> str
        Set: Description(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def IsDefunct(self) -> bool:
        """
        Get: IsDefunct(self: ActiveDirectorySchemaClass) -> bool
        Set: IsDefunct(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def MandatoryProperties(self) -> ActiveDirectorySchemaPropertyCollection:
        """ Get: MandatoryProperties(self: ActiveDirectorySchemaClass) -> ActiveDirectorySchemaPropertyCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySchemaClass) -> str """
        ...

    @property
    def Oid(self) -> str:
        """
        Get: Oid(self: ActiveDirectorySchemaClass) -> str
        Set: Oid(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def OptionalProperties(self) -> ActiveDirectorySchemaPropertyCollection:
        """ Get: OptionalProperties(self: ActiveDirectorySchemaClass) -> ActiveDirectorySchemaPropertyCollection """
        ...

    @property
    def PossibleInferiors(self) -> ReadOnlyActiveDirectorySchemaClassCollection:
        """ Get: PossibleInferiors(self: ActiveDirectorySchemaClass) -> ReadOnlyActiveDirectorySchemaClassCollection """
        ...

    @property
    def PossibleSuperiors(self) -> ActiveDirectorySchemaClassCollection:
        """ Get: PossibleSuperiors(self: ActiveDirectorySchemaClass) -> ActiveDirectorySchemaClassCollection """
        ...

    @property
    def SchemaGuid(self) -> Guid:
        """
        Get: SchemaGuid(self: ActiveDirectorySchemaClass) -> Guid
        Set: SchemaGuid(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def SubClassOf(self) -> ActiveDirectorySchemaClass:
        """
        Get: SubClassOf(self: ActiveDirectorySchemaClass) -> ActiveDirectorySchemaClass
        Set: SubClassOf(self: ActiveDirectorySchemaClass) = value
        """
        ...

    @property
    def Type(self) -> SchemaClassType:
        """
        Get: Type(self: ActiveDirectorySchemaClass) -> SchemaClassType
        Set: Type(self: ActiveDirectorySchemaClass) = value
        """
        ...


    @staticmethod
    def FindByName(context:DirectoryContext, ldapDisplayName:str) -> ActiveDirectorySchemaClass:
        """ FindByName(context: DirectoryContext, ldapDisplayName: str) -> ActiveDirectorySchemaClass """
        ...

    def GetAllProperties(self) -> ReadOnlyActiveDirectorySchemaPropertyCollection:
        """ GetAllProperties(self: ActiveDirectorySchemaClass) -> ReadOnlyActiveDirectorySchemaPropertyCollection """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySchemaClass) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySchemaClass) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySchemaClass) -> str """
        ...


class ActiveDirectorySchemaClassCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, schemaClass:ActiveDirectorySchemaClass) -> int:
        """ Add(self: ActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) -> int """
        ...

    def AddRange(self, schemaClasses:Array): # -> 
        """ AddRange(self: ActiveDirectorySchemaClassCollection, schemaClasses: Array[ActiveDirectorySchemaClass])AddRange(self: ActiveDirectorySchemaClassCollection, schemaClasses: ActiveDirectorySchemaClassCollection)AddRange(self: ActiveDirectorySchemaClassCollection, schemaClasses: ReadOnlyActiveDirectorySchemaClassCollection) """
        ...

    def Contains(self, schemaClass:ActiveDirectorySchemaClass) -> bool:
        """ Contains(self: ActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) -> bool """
        ...

    def CopyTo(self, schemaClasses:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectorySchemaClassCollection, schemaClasses: Array[ActiveDirectorySchemaClass], index: int) """
        ...

    def IndexOf(self, schemaClass:ActiveDirectorySchemaClass) -> int:
        """ IndexOf(self: ActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) -> int """
        ...

    def Insert(self, index:int, schemaClass:ActiveDirectorySchemaClass): # -> 
        """ Insert(self: ActiveDirectorySchemaClassCollection, index: int, schemaClass: ActiveDirectorySchemaClass) """
        ...

    def Remove(self, schemaClass:ActiveDirectorySchemaClass): # -> 
        """ Remove(self: ActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) """
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


class ActiveDirectorySchemaProperty(IDisposable): # skipped bases: <type 'object'>
    """ ActiveDirectorySchemaProperty(context: DirectoryContext, ldapDisplayName: str) """
    @property
    def CommonName(self) -> str:
        """
        Get: CommonName(self: ActiveDirectorySchemaProperty) -> str
        Set: CommonName(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ActiveDirectorySchemaProperty) -> str
        Set: Description(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsDefunct(self) -> bool:
        """
        Get: IsDefunct(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsDefunct(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsInAnr(self) -> bool:
        """
        Get: IsInAnr(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsInAnr(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsIndexed(self) -> bool:
        """
        Get: IsIndexed(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsIndexed(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsIndexedOverContainer(self) -> bool:
        """
        Get: IsIndexedOverContainer(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsIndexedOverContainer(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsInGlobalCatalog(self) -> bool:
        """
        Get: IsInGlobalCatalog(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsInGlobalCatalog(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsOnTombstonedObject(self) -> bool:
        """
        Get: IsOnTombstonedObject(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsOnTombstonedObject(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsSingleValued(self) -> bool:
        """
        Get: IsSingleValued(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsSingleValued(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def IsTupleIndexed(self) -> bool:
        """
        Get: IsTupleIndexed(self: ActiveDirectorySchemaProperty) -> bool
        Set: IsTupleIndexed(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def Link(self) -> ActiveDirectorySchemaProperty:
        """ Get: Link(self: ActiveDirectorySchemaProperty) -> ActiveDirectorySchemaProperty """
        ...

    @property
    def LinkId(self) -> Nullable:
        """
        Get: LinkId(self: ActiveDirectorySchemaProperty) -> Nullable[int]
        Set: LinkId(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySchemaProperty) -> str """
        ...

    @property
    def Oid(self) -> str:
        """
        Get: Oid(self: ActiveDirectorySchemaProperty) -> str
        Set: Oid(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def RangeLower(self) -> Nullable:
        """
        Get: RangeLower(self: ActiveDirectorySchemaProperty) -> Nullable[int]
        Set: RangeLower(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def RangeUpper(self) -> Nullable:
        """
        Get: RangeUpper(self: ActiveDirectorySchemaProperty) -> Nullable[int]
        Set: RangeUpper(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def SchemaGuid(self) -> Guid:
        """
        Get: SchemaGuid(self: ActiveDirectorySchemaProperty) -> Guid
        Set: SchemaGuid(self: ActiveDirectorySchemaProperty) = value
        """
        ...

    @property
    def Syntax(self) -> ActiveDirectorySyntax:
        """
        Get: Syntax(self: ActiveDirectorySchemaProperty) -> ActiveDirectorySyntax
        Set: Syntax(self: ActiveDirectorySchemaProperty) = value
        """
        ...


    @staticmethod
    def FindByName(context:DirectoryContext, ldapDisplayName:str) -> ActiveDirectorySchemaProperty:
        """ FindByName(context: DirectoryContext, ldapDisplayName: str) -> ActiveDirectorySchemaProperty """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySchemaProperty) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySchemaProperty) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySchemaProperty) -> str """
        ...


class ActiveDirectorySchemaPropertyCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, schemaProperty:ActiveDirectorySchemaProperty) -> int:
        """ Add(self: ActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) -> int """
        ...

    def AddRange(self, properties:Array): # -> 
        """ AddRange(self: ActiveDirectorySchemaPropertyCollection, properties: Array[ActiveDirectorySchemaProperty])AddRange(self: ActiveDirectorySchemaPropertyCollection, properties: ActiveDirectorySchemaPropertyCollection)AddRange(self: ActiveDirectorySchemaPropertyCollection, properties: ReadOnlyActiveDirectorySchemaPropertyCollection) """
        ...

    def Contains(self, schemaProperty:ActiveDirectorySchemaProperty) -> bool:
        """ Contains(self: ActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) -> bool """
        ...

    def CopyTo(self, properties:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectorySchemaPropertyCollection, properties: Array[ActiveDirectorySchemaProperty], index: int) """
        ...

    def IndexOf(self, schemaProperty:ActiveDirectorySchemaProperty) -> int:
        """ IndexOf(self: ActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) -> int """
        ...

    def Insert(self, index:int, schemaProperty:ActiveDirectorySchemaProperty): # -> 
        """ Insert(self: ActiveDirectorySchemaPropertyCollection, index: int, schemaProperty: ActiveDirectorySchemaProperty) """
        ...

    def Remove(self, schemaProperty:ActiveDirectorySchemaProperty): # -> 
        """ Remove(self: ActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) """
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


class ActiveDirectoryServerDownException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActiveDirectoryServerDownException(message: str, inner: Exception, errorCode: int, name: str)
    ActiveDirectoryServerDownException(message: str, errorCode: int, name: str)
    ActiveDirectoryServerDownException(message: str, inner: Exception)
    ActiveDirectoryServerDownException(message: str)
    ActiveDirectoryServerDownException()
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: ActiveDirectoryServerDownException) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectoryServerDownException) -> str """
        ...


    SerializeObjectState = ...


class ActiveDirectorySite(IDisposable): # skipped bases: <type 'object'>
    """ ActiveDirectorySite(context: DirectoryContext, siteName: str) """
    @property
    def AdjacentSites(self) -> ReadOnlySiteCollection:
        """ Get: AdjacentSites(self: ActiveDirectorySite) -> ReadOnlySiteCollection """
        ...

    @property
    def BridgeheadServers(self) -> ReadOnlyDirectoryServerCollection:
        """ Get: BridgeheadServers(self: ActiveDirectorySite) -> ReadOnlyDirectoryServerCollection """
        ...

    @property
    def Domains(self) -> DomainCollection:
        """ Get: Domains(self: ActiveDirectorySite) -> DomainCollection """
        ...

    @property
    def InterSiteTopologyGenerator(self) -> DirectoryServer:
        """
        Get: InterSiteTopologyGenerator(self: ActiveDirectorySite) -> DirectoryServer
        Set: InterSiteTopologyGenerator(self: ActiveDirectorySite) = value
        """
        ...

    @property
    def IntraSiteReplicationSchedule(self) -> ActiveDirectorySchedule:
        """
        Get: IntraSiteReplicationSchedule(self: ActiveDirectorySite) -> ActiveDirectorySchedule
        Set: IntraSiteReplicationSchedule(self: ActiveDirectorySite) = value
        """
        ...

    @property
    def Location(self) -> str:
        """
        Get: Location(self: ActiveDirectorySite) -> str
        Set: Location(self: ActiveDirectorySite) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySite) -> str """
        ...

    @property
    def Options(self) -> ActiveDirectorySiteOptions:
        """
        Get: Options(self: ActiveDirectorySite) -> ActiveDirectorySiteOptions
        Set: Options(self: ActiveDirectorySite) = value
        """
        ...

    @property
    def PreferredRpcBridgeheadServers(self) -> DirectoryServerCollection:
        """ Get: PreferredRpcBridgeheadServers(self: ActiveDirectorySite) -> DirectoryServerCollection """
        ...

    @property
    def PreferredSmtpBridgeheadServers(self) -> DirectoryServerCollection:
        """ Get: PreferredSmtpBridgeheadServers(self: ActiveDirectorySite) -> DirectoryServerCollection """
        ...

    @property
    def Servers(self) -> ReadOnlyDirectoryServerCollection:
        """ Get: Servers(self: ActiveDirectorySite) -> ReadOnlyDirectoryServerCollection """
        ...

    @property
    def SiteLinks(self) -> ReadOnlySiteLinkCollection:
        """ Get: SiteLinks(self: ActiveDirectorySite) -> ReadOnlySiteLinkCollection """
        ...

    @property
    def Subnets(self) -> ActiveDirectorySubnetCollection:
        """ Get: Subnets(self: ActiveDirectorySite) -> ActiveDirectorySubnetCollection """
        ...


    def Delete(self): # -> 
        """ Delete(self: ActiveDirectorySite) """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, siteName:str) -> ActiveDirectorySite:
        """ FindByName(context: DirectoryContext, siteName: str) -> ActiveDirectorySite """
        ...

    @staticmethod
    def GetComputerSite() -> ActiveDirectorySite:
        """ GetComputerSite() -> ActiveDirectorySite """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySite) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySite) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySite) -> str """
        ...


class ActiveDirectorySiteCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, site:ActiveDirectorySite) -> int:
        """ Add(self: ActiveDirectorySiteCollection, site: ActiveDirectorySite) -> int """
        ...

    def AddRange(self, sites:Array): # -> 
        """ AddRange(self: ActiveDirectorySiteCollection, sites: Array[ActiveDirectorySite])AddRange(self: ActiveDirectorySiteCollection, sites: ActiveDirectorySiteCollection) """
        ...

    def Contains(self, site:ActiveDirectorySite) -> bool:
        """ Contains(self: ActiveDirectorySiteCollection, site: ActiveDirectorySite) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectorySiteCollection, array: Array[ActiveDirectorySite], index: int) """
        ...

    def IndexOf(self, site:ActiveDirectorySite) -> int:
        """ IndexOf(self: ActiveDirectorySiteCollection, site: ActiveDirectorySite) -> int """
        ...

    def Insert(self, index:int, site:ActiveDirectorySite): # -> 
        """ Insert(self: ActiveDirectorySiteCollection, index: int, site: ActiveDirectorySite) """
        ...

    def Remove(self, site:ActiveDirectorySite): # -> 
        """ Remove(self: ActiveDirectorySiteCollection, site: ActiveDirectorySite) """
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


class ActiveDirectorySiteLink(IDisposable): # skipped bases: <type 'object'>
    """
    ActiveDirectorySiteLink(context: DirectoryContext, siteLinkName: str)
    ActiveDirectorySiteLink(context: DirectoryContext, siteLinkName: str, transport: ActiveDirectoryTransportType)
    ActiveDirectorySiteLink(context: DirectoryContext, siteLinkName: str, transport: ActiveDirectoryTransportType, schedule: ActiveDirectorySchedule)
    """
    @property
    def Cost(self) -> int:
        """
        Get: Cost(self: ActiveDirectorySiteLink) -> int
        Set: Cost(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def DataCompressionEnabled(self) -> bool:
        """
        Get: DataCompressionEnabled(self: ActiveDirectorySiteLink) -> bool
        Set: DataCompressionEnabled(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def InterSiteReplicationSchedule(self) -> ActiveDirectorySchedule:
        """
        Get: InterSiteReplicationSchedule(self: ActiveDirectorySiteLink) -> ActiveDirectorySchedule
        Set: InterSiteReplicationSchedule(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySiteLink) -> str """
        ...

    @property
    def NotificationEnabled(self) -> bool:
        """
        Get: NotificationEnabled(self: ActiveDirectorySiteLink) -> bool
        Set: NotificationEnabled(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def ReciprocalReplicationEnabled(self) -> bool:
        """
        Get: ReciprocalReplicationEnabled(self: ActiveDirectorySiteLink) -> bool
        Set: ReciprocalReplicationEnabled(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def ReplicationInterval(self) -> TimeSpan:
        """
        Get: ReplicationInterval(self: ActiveDirectorySiteLink) -> TimeSpan
        Set: ReplicationInterval(self: ActiveDirectorySiteLink) = value
        """
        ...

    @property
    def Sites(self) -> ActiveDirectorySiteCollection:
        """ Get: Sites(self: ActiveDirectorySiteLink) -> ActiveDirectorySiteCollection """
        ...

    @property
    def TransportType(self) -> ActiveDirectoryTransportType:
        """ Get: TransportType(self: ActiveDirectorySiteLink) -> ActiveDirectoryTransportType """
        ...


    def Delete(self): # -> 
        """ Delete(self: ActiveDirectorySiteLink) """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, siteLinkName:str, transport:ActiveDirectoryTransportType = ...) -> ActiveDirectorySiteLink:
        """
        FindByName(context: DirectoryContext, siteLinkName: str) -> ActiveDirectorySiteLink
        FindByName(context: DirectoryContext, siteLinkName: str, transport: ActiveDirectoryTransportType) -> ActiveDirectorySiteLink
        """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySiteLink) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySiteLink) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySiteLink) -> str """
        ...


class ActiveDirectorySiteLinkBridge(IDisposable): # skipped bases: <type 'object'>
    """
    ActiveDirectorySiteLinkBridge(context: DirectoryContext, bridgeName: str)
    ActiveDirectorySiteLinkBridge(context: DirectoryContext, bridgeName: str, transport: ActiveDirectoryTransportType)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySiteLinkBridge) -> str """
        ...

    @property
    def SiteLinks(self) -> ActiveDirectorySiteLinkCollection:
        """ Get: SiteLinks(self: ActiveDirectorySiteLinkBridge) -> ActiveDirectorySiteLinkCollection """
        ...

    @property
    def TransportType(self) -> ActiveDirectoryTransportType:
        """ Get: TransportType(self: ActiveDirectorySiteLinkBridge) -> ActiveDirectoryTransportType """
        ...


    def Delete(self): # -> 
        """ Delete(self: ActiveDirectorySiteLinkBridge) """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, bridgeName:str, transport:ActiveDirectoryTransportType = ...) -> ActiveDirectorySiteLinkBridge:
        """
        FindByName(context: DirectoryContext, bridgeName: str) -> ActiveDirectorySiteLinkBridge
        FindByName(context: DirectoryContext, bridgeName: str, transport: ActiveDirectoryTransportType) -> ActiveDirectorySiteLinkBridge
        """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySiteLinkBridge) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySiteLinkBridge) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySiteLinkBridge) -> str """
        ...


class ActiveDirectorySiteLinkCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, link:ActiveDirectorySiteLink) -> int:
        """ Add(self: ActiveDirectorySiteLinkCollection, link: ActiveDirectorySiteLink) -> int """
        ...

    def AddRange(self, links:Array): # -> 
        """ AddRange(self: ActiveDirectorySiteLinkCollection, links: Array[ActiveDirectorySiteLink])AddRange(self: ActiveDirectorySiteLinkCollection, links: ActiveDirectorySiteLinkCollection) """
        ...

    def Contains(self, link:ActiveDirectorySiteLink) -> bool:
        """ Contains(self: ActiveDirectorySiteLinkCollection, link: ActiveDirectorySiteLink) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectorySiteLinkCollection, array: Array[ActiveDirectorySiteLink], index: int) """
        ...

    def IndexOf(self, link:ActiveDirectorySiteLink) -> int:
        """ IndexOf(self: ActiveDirectorySiteLinkCollection, link: ActiveDirectorySiteLink) -> int """
        ...

    def Insert(self, index:int, link:ActiveDirectorySiteLink): # -> 
        """ Insert(self: ActiveDirectorySiteLinkCollection, index: int, link: ActiveDirectorySiteLink) """
        ...

    def Remove(self, link:ActiveDirectorySiteLink): # -> 
        """ Remove(self: ActiveDirectorySiteLinkCollection, link: ActiveDirectorySiteLink) """
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


class ActiveDirectorySiteOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ActiveDirectorySiteOptions, values: AutoInterSiteTopologyDisabled (16), AutoMinimumHopDisabled (4), AutoTopologyDisabled (1), ForceKccWindows2003Behavior (64), GroupMembershipCachingEnabled (32), None (0), RandomBridgeHeaderServerSelectionDisabled (256), RedundantServerTopologyEnabled (1024), StaleServerDetectDisabled (8), TopologyCleanupDisabled (2), UseHashingForReplicationSchedule (512), UseWindows2000IstgElection (128) """
    AutoInterSiteTopologyDisabled: ActiveDirectorySiteOptions = ...
    AutoMinimumHopDisabled: ActiveDirectorySiteOptions = ...
    AutoTopologyDisabled: ActiveDirectorySiteOptions = ...
    ForceKccWindows2003Behavior: ActiveDirectorySiteOptions = ...
    GroupMembershipCachingEnabled: ActiveDirectorySiteOptions = ...
    RandomBridgeHeaderServerSelectionDisabled: ActiveDirectorySiteOptions = ...
    RedundantServerTopologyEnabled: ActiveDirectorySiteOptions = ...
    StaleServerDetectDisabled: ActiveDirectorySiteOptions = ...
    TopologyCleanupDisabled: ActiveDirectorySiteOptions = ...
    UseHashingForReplicationSchedule: ActiveDirectorySiteOptions = ...
    UseWindows2000IstgElection: ActiveDirectorySiteOptions = ...
    value__ = ...


class ActiveDirectorySubnet(IDisposable): # skipped bases: <type 'object'>
    """
    ActiveDirectorySubnet(context: DirectoryContext, subnetName: str)
    ActiveDirectorySubnet(context: DirectoryContext, subnetName: str, siteName: str)
    """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: ActiveDirectorySubnet) -> str
        Set: Location(self: ActiveDirectorySubnet) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActiveDirectorySubnet) -> str """
        ...

    @property
    def Site(self) -> ActiveDirectorySite:
        """
        Get: Site(self: ActiveDirectorySubnet) -> ActiveDirectorySite
        Set: Site(self: ActiveDirectorySubnet) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: ActiveDirectorySubnet) """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, subnetName:str) -> ActiveDirectorySubnet:
        """ FindByName(context: DirectoryContext, subnetName: str) -> ActiveDirectorySubnet """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ActiveDirectorySubnet) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ActiveDirectorySubnet) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActiveDirectorySubnet) -> str """
        ...


class ActiveDirectorySubnetCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, subnet:ActiveDirectorySubnet) -> int:
        """ Add(self: ActiveDirectorySubnetCollection, subnet: ActiveDirectorySubnet) -> int """
        ...

    def AddRange(self, subnets:Array): # -> 
        """ AddRange(self: ActiveDirectorySubnetCollection, subnets: Array[ActiveDirectorySubnet])AddRange(self: ActiveDirectorySubnetCollection, subnets: ActiveDirectorySubnetCollection) """
        ...

    def Contains(self, subnet:ActiveDirectorySubnet) -> bool:
        """ Contains(self: ActiveDirectorySubnetCollection, subnet: ActiveDirectorySubnet) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ActiveDirectorySubnetCollection, array: Array[ActiveDirectorySubnet], index: int) """
        ...

    def IndexOf(self, subnet:ActiveDirectorySubnet) -> int:
        """ IndexOf(self: ActiveDirectorySubnetCollection, subnet: ActiveDirectorySubnet) -> int """
        ...

    def Insert(self, index:int, subnet:ActiveDirectorySubnet): # -> 
        """ Insert(self: ActiveDirectorySubnetCollection, index: int, subnet: ActiveDirectorySubnet) """
        ...

    def Remove(self, subnet:ActiveDirectorySubnet): # -> 
        """ Remove(self: ActiveDirectorySubnetCollection, subnet: ActiveDirectorySubnet) """
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


class ActiveDirectorySyntax(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActiveDirectorySyntax, values: AccessPointDN (19), Bool (8), CaseExactString (0), CaseIgnoreString (1), DirectoryString (3), DN (12), DNWithBinary (13), DNWithString (14), Enumeration (15), GeneralizedTime (10), IA5String (16), Int (6), Int64 (7), NumericString (2), OctetString (4), Oid (9), ORName (20), PresentationAddress (21), PrintableString (17), ReplicaLink (22), SecurityDescriptor (5), Sid (18), UtcTime (11) """
    AccessPointDN: ActiveDirectorySyntax = ...
    Bool: ActiveDirectorySyntax = ...
    CaseExactString: ActiveDirectorySyntax = ...
    CaseIgnoreString: ActiveDirectorySyntax = ...
    DirectoryString: ActiveDirectorySyntax = ...
    DN: ActiveDirectorySyntax = ...
    DNWithBinary: ActiveDirectorySyntax = ...
    DNWithString: ActiveDirectorySyntax = ...
    Enumeration: ActiveDirectorySyntax = ...
    GeneralizedTime: ActiveDirectorySyntax = ...
    IA5String: ActiveDirectorySyntax = ...
    Int: ActiveDirectorySyntax = ...
    Int64: ActiveDirectorySyntax = ...
    NumericString: ActiveDirectorySyntax = ...
    OctetString: ActiveDirectorySyntax = ...
    Oid: ActiveDirectorySyntax = ...
    ORName: ActiveDirectorySyntax = ...
    PresentationAddress: ActiveDirectorySyntax = ...
    PrintableString: ActiveDirectorySyntax = ...
    ReplicaLink: ActiveDirectorySyntax = ...
    SecurityDescriptor: ActiveDirectorySyntax = ...
    Sid: ActiveDirectorySyntax = ...
    UtcTime: ActiveDirectorySyntax = ...
    value__ = ...


class ActiveDirectoryTransportType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActiveDirectoryTransportType, values: Rpc (0), Smtp (1) """
    Rpc: ActiveDirectoryTransportType = ...
    Smtp: ActiveDirectoryTransportType = ...
    value__ = ...


class DirectoryServer(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InboundConnections(self) -> ReplicationConnectionCollection:
        """ Get: InboundConnections(self: DirectoryServer) -> ReplicationConnectionCollection """
        ...

    @property
    def IPAddress(self) -> str:
        """ Get: IPAddress(self: DirectoryServer) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DirectoryServer) -> str """
        ...

    @property
    def OutboundConnections(self) -> ReplicationConnectionCollection:
        """ Get: OutboundConnections(self: DirectoryServer) -> ReplicationConnectionCollection """
        ...

    @property
    def Partitions(self) -> ReadOnlyStringCollection:
        """ Get: Partitions(self: DirectoryServer) -> ReadOnlyStringCollection """
        ...

    @property
    def SiteName(self) -> str:
        """ Get: SiteName(self: DirectoryServer) -> str """
        ...

    @property
    def SyncFromAllServersCallback(self) -> SyncUpdateCallback:
        """
        Get: SyncFromAllServersCallback(self: DirectoryServer) -> SyncUpdateCallback
        Set: SyncFromAllServersCallback(self: DirectoryServer) = value
        """
        ...


    def CheckReplicationConsistency(self): # -> 
        """ CheckReplicationConsistency(self: DirectoryServer) """
        ...

    def GetAllReplicationNeighbors(self) -> ReplicationNeighborCollection:
        """ GetAllReplicationNeighbors(self: DirectoryServer) -> ReplicationNeighborCollection """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: DirectoryServer) -> DirectoryEntry """
        ...

    def GetReplicationConnectionFailures(self) -> ReplicationFailureCollection:
        """ GetReplicationConnectionFailures(self: DirectoryServer) -> ReplicationFailureCollection """
        ...

    def GetReplicationCursors(self, partition:str) -> ReplicationCursorCollection:
        """ GetReplicationCursors(self: DirectoryServer, partition: str) -> ReplicationCursorCollection """
        ...

    def GetReplicationMetadata(self, objectPath:str) -> ActiveDirectoryReplicationMetadata:
        """ GetReplicationMetadata(self: DirectoryServer, objectPath: str) -> ActiveDirectoryReplicationMetadata """
        ...

    def GetReplicationNeighbors(self, partition:str) -> ReplicationNeighborCollection:
        """ GetReplicationNeighbors(self: DirectoryServer, partition: str) -> ReplicationNeighborCollection """
        ...

    def GetReplicationOperationInformation(self) -> ReplicationOperationInformation:
        """ GetReplicationOperationInformation(self: DirectoryServer) -> ReplicationOperationInformation """
        ...

    def MoveToAnotherSite(self, siteName:str): # -> 
        """ MoveToAnotherSite(self: DirectoryServer, siteName: str) """
        ...

    def SyncReplicaFromAllServers(self, partition:str, options:SyncFromAllServersOptions): # -> 
        """ SyncReplicaFromAllServers(self: DirectoryServer, partition: str, options: SyncFromAllServersOptions) """
        ...

    def SyncReplicaFromServer(self, partition:str, sourceServer:str): # -> 
        """ SyncReplicaFromServer(self: DirectoryServer, partition: str, sourceServer: str) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DirectoryServer) -> str """
        ...

    def TriggerSyncReplicaFromNeighbors(self, partition:str): # -> 
        """ TriggerSyncReplicaFromNeighbors(self: DirectoryServer, partition: str) """
        ...


class AdamInstance(DirectoryServer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def ConfigurationSet(self) -> ConfigurationSet:
        """ Get: ConfigurationSet(self: AdamInstance) -> ConfigurationSet """
        ...

    @property
    def DefaultPartition(self) -> str:
        """
        Get: DefaultPartition(self: AdamInstance) -> str
        Set: DefaultPartition(self: AdamInstance) = value
        """
        ...

    @property
    def HostName(self) -> str:
        """ Get: HostName(self: AdamInstance) -> str """
        ...

    @property
    def LdapPort(self) -> int:
        """ Get: LdapPort(self: AdamInstance) -> int """
        ...

    @property
    def Roles(self) -> AdamRoleCollection:
        """ Get: Roles(self: AdamInstance) -> AdamRoleCollection """
        ...

    @property
    def SslPort(self) -> int:
        """ Get: SslPort(self: AdamInstance) -> int """
        ...


    @staticmethod
    def FindAll(context:DirectoryContext, partitionName:str) -> AdamInstanceCollection:
        """ FindAll(context: DirectoryContext, partitionName: str) -> AdamInstanceCollection """
        ...

    @staticmethod
    def FindOne(context:DirectoryContext, partitionName:str) -> AdamInstance:
        """ FindOne(context: DirectoryContext, partitionName: str) -> AdamInstance """
        ...

    @staticmethod
    def GetAdamInstance(context:DirectoryContext) -> AdamInstance:
        """ GetAdamInstance(context: DirectoryContext) -> AdamInstance """
        ...

    def Save(self): # -> 
        """ Save(self: AdamInstance) """
        ...

    def SeizeRoleOwnership(self, role:AdamRole): # -> 
        """ SeizeRoleOwnership(self: AdamInstance, role: AdamRole) """
        ...

    def TransferRoleOwnership(self, role:AdamRole): # -> 
        """ TransferRoleOwnership(self: AdamInstance, role: AdamRole) """
        ...


class AdamInstanceCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, adamInstance:AdamInstance) -> bool:
        """ Contains(self: AdamInstanceCollection, adamInstance: AdamInstance) -> bool """
        ...

    def CopyTo(self, adamInstances:Array, index:int): # -> 
        """ CopyTo(self: AdamInstanceCollection, adamInstances: Array[AdamInstance], index: int) """
        ...

    def IndexOf(self, adamInstance:AdamInstance) -> int:
        """ IndexOf(self: AdamInstanceCollection, adamInstance: AdamInstance) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class AdamRole(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AdamRole, values: NamingRole (1), SchemaRole (0) """
    NamingRole: AdamRole = ...
    SchemaRole: AdamRole = ...
    value__ = ...


class AdamRoleCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, role:AdamRole) -> bool:
        """ Contains(self: AdamRoleCollection, role: AdamRole) -> bool """
        ...

    def CopyTo(self, roles:Array, index:int): # -> 
        """ CopyTo(self: AdamRoleCollection, roles: Array[AdamRole], index: int) """
        ...

    def IndexOf(self, role:AdamRole) -> int:
        """ IndexOf(self: AdamRoleCollection, role: AdamRole) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ApplicationPartition(ActiveDirectoryPartition): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ApplicationPartition(context: DirectoryContext, distinguishedName: str)
    ApplicationPartition(context: DirectoryContext, distinguishedName: str, objectClass: str)
    """
    @property
    def DirectoryServers(self) -> DirectoryServerCollection:
        """ Get: DirectoryServers(self: ApplicationPartition) -> DirectoryServerCollection """
        ...

    @property
    def SecurityReferenceDomain(self) -> str:
        """
        Get: SecurityReferenceDomain(self: ApplicationPartition) -> str
        Set: SecurityReferenceDomain(self: ApplicationPartition) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: ApplicationPartition) """
        ...

    def FindAllDirectoryServers(self, siteName:str = ...) -> ReadOnlyDirectoryServerCollection:
        """
        FindAllDirectoryServers(self: ApplicationPartition) -> ReadOnlyDirectoryServerCollection
        FindAllDirectoryServers(self: ApplicationPartition, siteName: str) -> ReadOnlyDirectoryServerCollection
        """
        ...

    def FindAllDiscoverableDirectoryServers(self, siteName:str = ...) -> ReadOnlyDirectoryServerCollection:
        """
        FindAllDiscoverableDirectoryServers(self: ApplicationPartition) -> ReadOnlyDirectoryServerCollection
        FindAllDiscoverableDirectoryServers(self: ApplicationPartition, siteName: str) -> ReadOnlyDirectoryServerCollection
        """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, distinguishedName:str) -> ApplicationPartition:
        """ FindByName(context: DirectoryContext, distinguishedName: str) -> ApplicationPartition """
        ...

    def FindDirectoryServer(self, *__args:str) -> DirectoryServer:
        """
        FindDirectoryServer(self: ApplicationPartition) -> DirectoryServer
        FindDirectoryServer(self: ApplicationPartition, siteName: str) -> DirectoryServer
        FindDirectoryServer(self: ApplicationPartition, forceRediscovery: bool) -> DirectoryServer
        FindDirectoryServer(self: ApplicationPartition, siteName: str, forceRediscovery: bool) -> DirectoryServer
        """
        ...

    @staticmethod
    def GetApplicationPartition(context:DirectoryContext) -> ApplicationPartition:
        """ GetApplicationPartition(context: DirectoryContext) -> ApplicationPartition """
        ...

    def Save(self): # -> 
        """ Save(self: ApplicationPartition) """
        ...

    def __new__(cls, context:DirectoryContext, distinguishedName:str, objectClass:str = ...) -> Self:
        """
        __new__(cls: type, context: DirectoryContext, distinguishedName: str)
        __new__(cls: type, context: DirectoryContext, distinguishedName: str, objectClass: str)
        """
        ...


class ApplicationPartitionCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, applicationPartition:ApplicationPartition) -> bool:
        """ Contains(self: ApplicationPartitionCollection, applicationPartition: ApplicationPartition) -> bool """
        ...

    def CopyTo(self, applicationPartitions:Array, index:int): # -> 
        """ CopyTo(self: ApplicationPartitionCollection, applicationPartitions: Array[ApplicationPartition], index: int) """
        ...

    def IndexOf(self, applicationPartition:ApplicationPartition) -> int:
        """ IndexOf(self: ApplicationPartitionCollection, applicationPartition: ApplicationPartition) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class AttributeMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LastOriginatingChangeTime(self) -> DateTime:
        """ Get: LastOriginatingChangeTime(self: AttributeMetadata) -> DateTime """
        ...

    @property
    def LastOriginatingInvocationId(self) -> Guid:
        """ Get: LastOriginatingInvocationId(self: AttributeMetadata) -> Guid """
        ...

    @property
    def LocalChangeUsn(self) -> Int64:
        """ Get: LocalChangeUsn(self: AttributeMetadata) -> Int64 """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AttributeMetadata) -> str """
        ...

    @property
    def OriginatingChangeUsn(self) -> Int64:
        """ Get: OriginatingChangeUsn(self: AttributeMetadata) -> Int64 """
        ...

    @property
    def OriginatingServer(self) -> str:
        """ Get: OriginatingServer(self: AttributeMetadata) -> str """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: AttributeMetadata) -> int """
        ...



class AttributeMetadataCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, metadata:AttributeMetadata) -> bool:
        """ Contains(self: AttributeMetadataCollection, metadata: AttributeMetadata) -> bool """
        ...

    def CopyTo(self, metadata:Array, index:int): # -> 
        """ CopyTo(self: AttributeMetadataCollection, metadata: Array[AttributeMetadata], index: int) """
        ...

    def IndexOf(self, metadata:AttributeMetadata) -> int:
        """ IndexOf(self: AttributeMetadataCollection, metadata: AttributeMetadata) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ConfigurationSet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AdamInstances(self) -> AdamInstanceCollection:
        """ Get: AdamInstances(self: ConfigurationSet) -> AdamInstanceCollection """
        ...

    @property
    def ApplicationPartitions(self) -> ApplicationPartitionCollection:
        """ Get: ApplicationPartitions(self: ConfigurationSet) -> ApplicationPartitionCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ConfigurationSet) -> str """
        ...

    @property
    def NamingRoleOwner(self) -> AdamInstance:
        """ Get: NamingRoleOwner(self: ConfigurationSet) -> AdamInstance """
        ...

    @property
    def Schema(self) -> ActiveDirectorySchema:
        """ Get: Schema(self: ConfigurationSet) -> ActiveDirectorySchema """
        ...

    @property
    def SchemaRoleOwner(self) -> AdamInstance:
        """ Get: SchemaRoleOwner(self: ConfigurationSet) -> AdamInstance """
        ...

    @property
    def Sites(self) -> ReadOnlySiteCollection:
        """ Get: Sites(self: ConfigurationSet) -> ReadOnlySiteCollection """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: ConfigurationSet) """
        ...

    def FindAdamInstance(self, partitionName:str = ..., siteName:str = ...) -> AdamInstance:
        """
        FindAdamInstance(self: ConfigurationSet) -> AdamInstance
        FindAdamInstance(self: ConfigurationSet, partitionName: str) -> AdamInstance
        FindAdamInstance(self: ConfigurationSet, partitionName: str, siteName: str) -> AdamInstance
        """
        ...

    def FindAllAdamInstances(self, partitionName:str = ..., siteName:str = ...) -> AdamInstanceCollection:
        """
        FindAllAdamInstances(self: ConfigurationSet) -> AdamInstanceCollection
        FindAllAdamInstances(self: ConfigurationSet, partitionName: str) -> AdamInstanceCollection
        FindAllAdamInstances(self: ConfigurationSet, partitionName: str, siteName: str) -> AdamInstanceCollection
        """
        ...

    @staticmethod
    def GetConfigurationSet(context:DirectoryContext) -> ConfigurationSet:
        """ GetConfigurationSet(context: DirectoryContext) -> ConfigurationSet """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ConfigurationSet) -> DirectoryEntry """
        ...

    def GetSecurityLevel(self) -> ReplicationSecurityLevel:
        """ GetSecurityLevel(self: ConfigurationSet) -> ReplicationSecurityLevel """
        ...

    def SetSecurityLevel(self, securityLevel:ReplicationSecurityLevel): # -> 
        """ SetSecurityLevel(self: ConfigurationSet, securityLevel: ReplicationSecurityLevel) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ConfigurationSet) -> str """
        ...


class DirectoryContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    DirectoryContext(contextType: DirectoryContextType)
    DirectoryContext(contextType: DirectoryContextType, name: str)
    DirectoryContext(contextType: DirectoryContextType, username: str, password: str)
    DirectoryContext(contextType: DirectoryContextType, name: str, username: str, password: str)
    """
    @property
    def ContextType(self) -> DirectoryContextType:
        """ Get: ContextType(self: DirectoryContext) -> DirectoryContextType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DirectoryContext) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: DirectoryContext) -> str """
        ...



class DirectoryContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DirectoryContextType, values: ApplicationPartition (4), ConfigurationSet (3), DirectoryServer (2), Domain (0), Forest (1) """
    ApplicationPartition: DirectoryContextType = ...
    ConfigurationSet: DirectoryContextType = ...
    DirectoryServer: DirectoryContextType = ...
    Domain: DirectoryContextType = ...
    Forest: DirectoryContextType = ...
    value__ = ...


class DirectoryServerCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, server:DirectoryServer) -> int:
        """ Add(self: DirectoryServerCollection, server: DirectoryServer) -> int """
        ...

    def AddRange(self, servers:Array): # -> 
        """ AddRange(self: DirectoryServerCollection, servers: Array[DirectoryServer]) """
        ...

    def Contains(self, server:DirectoryServer) -> bool:
        """ Contains(self: DirectoryServerCollection, server: DirectoryServer) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryServerCollection, array: Array[DirectoryServer], index: int) """
        ...

    def IndexOf(self, server:DirectoryServer) -> int:
        """ IndexOf(self: DirectoryServerCollection, server: DirectoryServer) -> int """
        ...

    def Insert(self, index:int, server:DirectoryServer): # -> 
        """ Insert(self: DirectoryServerCollection, index: int, server: DirectoryServer) """
        ...

    def Remove(self, server:DirectoryServer): # -> 
        """ Remove(self: DirectoryServerCollection, server: DirectoryServer) """
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


class Domain(ActiveDirectoryPartition): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Children(self) -> DomainCollection:
        """ Get: Children(self: Domain) -> DomainCollection """
        ...

    @property
    def DomainControllers(self) -> DomainControllerCollection:
        """ Get: DomainControllers(self: Domain) -> DomainControllerCollection """
        ...

    @property
    def DomainMode(self) -> DomainMode:
        """ Get: DomainMode(self: Domain) -> DomainMode """
        ...

    @property
    def DomainModeLevel(self) -> int:
        """ Get: DomainModeLevel(self: Domain) -> int """
        ...

    @property
    def Forest(self) -> Forest:
        """ Get: Forest(self: Domain) -> Forest """
        ...

    @property
    def InfrastructureRoleOwner(self) -> DomainController:
        """ Get: InfrastructureRoleOwner(self: Domain) -> DomainController """
        ...

    @property
    def Parent(self) -> Domain:
        """ Get: Parent(self: Domain) -> Domain """
        ...

    @property
    def PdcRoleOwner(self) -> DomainController:
        """ Get: PdcRoleOwner(self: Domain) -> DomainController """
        ...

    @property
    def RidRoleOwner(self) -> DomainController:
        """ Get: RidRoleOwner(self: Domain) -> DomainController """
        ...


    def CreateLocalSideOfTrustRelationship(self, targetDomainName:str, direction:TrustDirection, trustPassword:str): # -> 
        """ CreateLocalSideOfTrustRelationship(self: Domain, targetDomainName: str, direction: TrustDirection, trustPassword: str) """
        ...

    def CreateTrustRelationship(self, targetDomain:Domain, direction:TrustDirection): # -> 
        """ CreateTrustRelationship(self: Domain, targetDomain: Domain, direction: TrustDirection) """
        ...

    def DeleteLocalSideOfTrustRelationship(self, targetDomainName:str): # -> 
        """ DeleteLocalSideOfTrustRelationship(self: Domain, targetDomainName: str) """
        ...

    def DeleteTrustRelationship(self, targetDomain:Domain): # -> 
        """ DeleteTrustRelationship(self: Domain, targetDomain: Domain) """
        ...

    def FindAllDiscoverableDomainControllers(self, siteName:str = ...) -> DomainControllerCollection:
        """
        FindAllDiscoverableDomainControllers(self: Domain) -> DomainControllerCollection
        FindAllDiscoverableDomainControllers(self: Domain, siteName: str) -> DomainControllerCollection
        """
        ...

    def FindAllDomainControllers(self, siteName:str = ...) -> DomainControllerCollection:
        """
        FindAllDomainControllers(self: Domain) -> DomainControllerCollection
        FindAllDomainControllers(self: Domain, siteName: str) -> DomainControllerCollection
        """
        ...

    def FindDomainController(self, *__args:str) -> DomainController:
        """
        FindDomainController(self: Domain) -> DomainController
        FindDomainController(self: Domain, siteName: str) -> DomainController
        FindDomainController(self: Domain, flag: LocatorOptions) -> DomainController
        FindDomainController(self: Domain, siteName: str, flag: LocatorOptions) -> DomainController
        """
        ...

    def GetAllTrustRelationships(self) -> TrustRelationshipInformationCollection:
        """ GetAllTrustRelationships(self: Domain) -> TrustRelationshipInformationCollection """
        ...

    @staticmethod
    def GetComputerDomain() -> Domain:
        """ GetComputerDomain() -> Domain """
        ...

    @staticmethod
    def GetCurrentDomain() -> Domain:
        """ GetCurrentDomain() -> Domain """
        ...

    @staticmethod
    def GetDomain(context:DirectoryContext) -> Domain:
        """ GetDomain(context: DirectoryContext) -> Domain """
        ...

    def GetSelectiveAuthenticationStatus(self, targetDomainName:str) -> bool:
        """ GetSelectiveAuthenticationStatus(self: Domain, targetDomainName: str) -> bool """
        ...

    def GetSidFilteringStatus(self, targetDomainName:str) -> bool:
        """ GetSidFilteringStatus(self: Domain, targetDomainName: str) -> bool """
        ...

    def GetTrustRelationship(self, targetDomainName:str) -> TrustRelationshipInformation:
        """ GetTrustRelationship(self: Domain, targetDomainName: str) -> TrustRelationshipInformation """
        ...

    def RaiseDomainFunctionality(self, domainMode:DomainMode): # -> 
        """ RaiseDomainFunctionality(self: Domain, domainMode: DomainMode) """
        ...

    def RaiseDomainFunctionalityLevel(self, domainMode:int): # -> 
        """ RaiseDomainFunctionalityLevel(self: Domain, domainMode: int) """
        ...

    def RepairTrustRelationship(self, targetDomain:Domain): # -> 
        """ RepairTrustRelationship(self: Domain, targetDomain: Domain) """
        ...

    def SetSelectiveAuthenticationStatus(self, targetDomainName:str, enable:bool): # -> 
        """ SetSelectiveAuthenticationStatus(self: Domain, targetDomainName: str, enable: bool) """
        ...

    def SetSidFilteringStatus(self, targetDomainName:str, enable:bool): # -> 
        """ SetSidFilteringStatus(self: Domain, targetDomainName: str, enable: bool) """
        ...

    def UpdateLocalSideOfTrustRelationship(self, targetDomainName:str, *__args:str): # -> 
        """ UpdateLocalSideOfTrustRelationship(self: Domain, targetDomainName: str, newTrustPassword: str)UpdateLocalSideOfTrustRelationship(self: Domain, targetDomainName: str, newTrustDirection: TrustDirection, newTrustPassword: str) """
        ...

    def UpdateTrustRelationship(self, targetDomain:Domain, newTrustDirection:TrustDirection): # -> 
        """ UpdateTrustRelationship(self: Domain, targetDomain: Domain, newTrustDirection: TrustDirection) """
        ...

    def VerifyOutboundTrustRelationship(self, targetDomainName:str): # -> 
        """ VerifyOutboundTrustRelationship(self: Domain, targetDomainName: str) """
        ...

    def VerifyTrustRelationship(self, targetDomain:Domain, direction:TrustDirection): # -> 
        """ VerifyTrustRelationship(self: Domain, targetDomain: Domain, direction: TrustDirection) """
        ...


class DomainCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, domain:Domain) -> bool:
        """ Contains(self: DomainCollection, domain: Domain) -> bool """
        ...

    def CopyTo(self, domains:Array, index:int): # -> 
        """ CopyTo(self: DomainCollection, domains: Array[Domain], index: int) """
        ...

    def IndexOf(self, domain:Domain) -> int:
        """ IndexOf(self: DomainCollection, domain: Domain) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DomainCollisionOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DomainCollisionOptions, values: NetBiosNameDisabledByAdmin (4), NetBiosNameDisabledByConflict (8), None (0), SidDisabledByAdmin (1), SidDisabledByConflict (2) """
    NetBiosNameDisabledByAdmin: DomainCollisionOptions = ...
    NetBiosNameDisabledByConflict: DomainCollisionOptions = ...
    SidDisabledByAdmin: DomainCollisionOptions = ...
    SidDisabledByConflict: DomainCollisionOptions = ...
    value__ = ...


class DomainController(DirectoryServer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def CurrentTime(self) -> DateTime:
        """ Get: CurrentTime(self: DomainController) -> DateTime """
        ...

    @property
    def Domain(self) -> Domain:
        """ Get: Domain(self: DomainController) -> Domain """
        ...

    @property
    def Forest(self) -> Forest:
        """ Get: Forest(self: DomainController) -> Forest """
        ...

    @property
    def HighestCommittedUsn(self) -> Int64:
        """ Get: HighestCommittedUsn(self: DomainController) -> Int64 """
        ...

    @property
    def OSVersion(self) -> str:
        """ Get: OSVersion(self: DomainController) -> str """
        ...

    @property
    def Roles(self) -> ActiveDirectoryRoleCollection:
        """ Get: Roles(self: DomainController) -> ActiveDirectoryRoleCollection """
        ...


    def EnableGlobalCatalog(self) -> GlobalCatalog:
        """ EnableGlobalCatalog(self: DomainController) -> GlobalCatalog """
        ...

    @staticmethod
    def FindAll(context:DirectoryContext, siteName:str = ...) -> DomainControllerCollection:
        """
        FindAll(context: DirectoryContext) -> DomainControllerCollection
        FindAll(context: DirectoryContext, siteName: str) -> DomainControllerCollection
        """
        ...

    @staticmethod
    def FindOne(context:DirectoryContext, *__args:str) -> DomainController:
        """
        FindOne(context: DirectoryContext) -> DomainController
        FindOne(context: DirectoryContext, siteName: str) -> DomainController
        FindOne(context: DirectoryContext, flag: LocatorOptions) -> DomainController
        FindOne(context: DirectoryContext, siteName: str, flag: LocatorOptions) -> DomainController
        """
        ...

    def GetDirectorySearcher(self) -> DirectorySearcher:
        """ GetDirectorySearcher(self: DomainController) -> DirectorySearcher """
        ...

    @staticmethod
    def GetDomainController(context:DirectoryContext) -> DomainController:
        """ GetDomainController(context: DirectoryContext) -> DomainController """
        ...

    def IsGlobalCatalog(self) -> bool:
        """ IsGlobalCatalog(self: DomainController) -> bool """
        ...

    def SeizeRoleOwnership(self, role:ActiveDirectoryRole): # -> 
        """ SeizeRoleOwnership(self: DomainController, role: ActiveDirectoryRole) """
        ...

    def TransferRoleOwnership(self, role:ActiveDirectoryRole): # -> 
        """ TransferRoleOwnership(self: DomainController, role: ActiveDirectoryRole) """
        ...


class DomainControllerCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, domainController:DomainController) -> bool:
        """ Contains(self: DomainControllerCollection, domainController: DomainController) -> bool """
        ...

    def CopyTo(self, domainControllers:Array, index:int): # -> 
        """ CopyTo(self: DomainControllerCollection, domainControllers: Array[DomainController], index: int) """
        ...

    def IndexOf(self, domainController:DomainController) -> int:
        """ IndexOf(self: DomainControllerCollection, domainController: DomainController) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DomainMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DomainMode, values: Unknown (-1), Windows2000MixedDomain (0), Windows2000NativeDomain (1), Windows2003Domain (3), Windows2003InterimDomain (2), Windows2008Domain (4), Windows2008R2Domain (5), Windows2012R2Domain (7), Windows8Domain (6) """
    Unknown: DomainMode = ...
    value__ = ...
    Windows2000MixedDomain: DomainMode = ...
    Windows2000NativeDomain: DomainMode = ...
    Windows2003Domain: DomainMode = ...
    Windows2003InterimDomain: DomainMode = ...
    Windows2008Domain: DomainMode = ...
    Windows2008R2Domain: DomainMode = ...
    Windows2012R2Domain: DomainMode = ...
    Windows8Domain: DomainMode = ...


class Forest(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationPartitions(self) -> ApplicationPartitionCollection:
        """ Get: ApplicationPartitions(self: Forest) -> ApplicationPartitionCollection """
        ...

    @property
    def Domains(self) -> DomainCollection:
        """ Get: Domains(self: Forest) -> DomainCollection """
        ...

    @property
    def ForestMode(self) -> ForestMode:
        """ Get: ForestMode(self: Forest) -> ForestMode """
        ...

    @property
    def ForestModeLevel(self) -> int:
        """ Get: ForestModeLevel(self: Forest) -> int """
        ...

    @property
    def GlobalCatalogs(self) -> GlobalCatalogCollection:
        """ Get: GlobalCatalogs(self: Forest) -> GlobalCatalogCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Forest) -> str """
        ...

    @property
    def NamingRoleOwner(self) -> DomainController:
        """ Get: NamingRoleOwner(self: Forest) -> DomainController """
        ...

    @property
    def RootDomain(self) -> Domain:
        """ Get: RootDomain(self: Forest) -> Domain """
        ...

    @property
    def Schema(self) -> ActiveDirectorySchema:
        """ Get: Schema(self: Forest) -> ActiveDirectorySchema """
        ...

    @property
    def SchemaRoleOwner(self) -> DomainController:
        """ Get: SchemaRoleOwner(self: Forest) -> DomainController """
        ...

    @property
    def Sites(self) -> ReadOnlySiteCollection:
        """ Get: Sites(self: Forest) -> ReadOnlySiteCollection """
        ...


    def CreateLocalSideOfTrustRelationship(self, targetForestName:str, direction:TrustDirection, trustPassword:str): # -> 
        """ CreateLocalSideOfTrustRelationship(self: Forest, targetForestName: str, direction: TrustDirection, trustPassword: str) """
        ...

    def CreateTrustRelationship(self, targetForest:Forest, direction:TrustDirection): # -> 
        """ CreateTrustRelationship(self: Forest, targetForest: Forest, direction: TrustDirection) """
        ...

    def DeleteLocalSideOfTrustRelationship(self, targetForestName:str): # -> 
        """ DeleteLocalSideOfTrustRelationship(self: Forest, targetForestName: str) """
        ...

    def DeleteTrustRelationship(self, targetForest:Forest): # -> 
        """ DeleteTrustRelationship(self: Forest, targetForest: Forest) """
        ...

    def FindAllDiscoverableGlobalCatalogs(self, siteName:str = ...) -> GlobalCatalogCollection:
        """
        FindAllDiscoverableGlobalCatalogs(self: Forest) -> GlobalCatalogCollection
        FindAllDiscoverableGlobalCatalogs(self: Forest, siteName: str) -> GlobalCatalogCollection
        """
        ...

    def FindAllGlobalCatalogs(self, siteName:str = ...) -> GlobalCatalogCollection:
        """
        FindAllGlobalCatalogs(self: Forest) -> GlobalCatalogCollection
        FindAllGlobalCatalogs(self: Forest, siteName: str) -> GlobalCatalogCollection
        """
        ...

    def FindGlobalCatalog(self, *__args:str) -> GlobalCatalog:
        """
        FindGlobalCatalog(self: Forest) -> GlobalCatalog
        FindGlobalCatalog(self: Forest, siteName: str) -> GlobalCatalog
        FindGlobalCatalog(self: Forest, flag: LocatorOptions) -> GlobalCatalog
        FindGlobalCatalog(self: Forest, siteName: str, flag: LocatorOptions) -> GlobalCatalog
        """
        ...

    def GetAllTrustRelationships(self) -> TrustRelationshipInformationCollection:
        """ GetAllTrustRelationships(self: Forest) -> TrustRelationshipInformationCollection """
        ...

    @staticmethod
    def GetCurrentForest() -> Forest:
        """ GetCurrentForest() -> Forest """
        ...

    @staticmethod
    def GetForest(context:DirectoryContext) -> Forest:
        """ GetForest(context: DirectoryContext) -> Forest """
        ...

    def GetSelectiveAuthenticationStatus(self, targetForestName:str) -> bool:
        """ GetSelectiveAuthenticationStatus(self: Forest, targetForestName: str) -> bool """
        ...

    def GetSidFilteringStatus(self, targetForestName:str) -> bool:
        """ GetSidFilteringStatus(self: Forest, targetForestName: str) -> bool """
        ...

    def GetTrustRelationship(self, targetForestName:str) -> ForestTrustRelationshipInformation:
        """ GetTrustRelationship(self: Forest, targetForestName: str) -> ForestTrustRelationshipInformation """
        ...

    def RaiseForestFunctionality(self, forestMode:ForestMode): # -> 
        """ RaiseForestFunctionality(self: Forest, forestMode: ForestMode) """
        ...

    def RaiseForestFunctionalityLevel(self, forestMode:int): # -> 
        """ RaiseForestFunctionalityLevel(self: Forest, forestMode: int) """
        ...

    def RepairTrustRelationship(self, targetForest:Forest): # -> 
        """ RepairTrustRelationship(self: Forest, targetForest: Forest) """
        ...

    def SetSelectiveAuthenticationStatus(self, targetForestName:str, enable:bool): # -> 
        """ SetSelectiveAuthenticationStatus(self: Forest, targetForestName: str, enable: bool) """
        ...

    def SetSidFilteringStatus(self, targetForestName:str, enable:bool): # -> 
        """ SetSidFilteringStatus(self: Forest, targetForestName: str, enable: bool) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Forest) -> str """
        ...

    def UpdateLocalSideOfTrustRelationship(self, targetForestName:str, *__args:str): # -> 
        """ UpdateLocalSideOfTrustRelationship(self: Forest, targetForestName: str, newTrustPassword: str)UpdateLocalSideOfTrustRelationship(self: Forest, targetForestName: str, newTrustDirection: TrustDirection, newTrustPassword: str) """
        ...

    def UpdateTrustRelationship(self, targetForest:Forest, newTrustDirection:TrustDirection): # -> 
        """ UpdateTrustRelationship(self: Forest, targetForest: Forest, newTrustDirection: TrustDirection) """
        ...

    def VerifyOutboundTrustRelationship(self, targetForestName:str): # -> 
        """ VerifyOutboundTrustRelationship(self: Forest, targetForestName: str) """
        ...

    def VerifyTrustRelationship(self, targetForest:Forest, direction:TrustDirection): # -> 
        """ VerifyTrustRelationship(self: Forest, targetForest: Forest, direction: TrustDirection) """
        ...


class ForestMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ForestMode, values: Unknown (-1), Windows2000Forest (0), Windows2003Forest (2), Windows2003InterimForest (1), Windows2008Forest (3), Windows2008R2Forest (4), Windows2012R2Forest (6), Windows8Forest (5) """
    Unknown: ForestMode = ...
    value__ = ...
    Windows2000Forest: ForestMode = ...
    Windows2003Forest: ForestMode = ...
    Windows2003InterimForest: ForestMode = ...
    Windows2008Forest: ForestMode = ...
    Windows2008R2Forest: ForestMode = ...
    Windows2012R2Forest: ForestMode = ...
    Windows8Forest: ForestMode = ...


class ForestTrustCollisionException(ActiveDirectoryOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ForestTrustCollisionException(message: str, inner: Exception, collisions: ForestTrustRelationshipCollisionCollection)
    ForestTrustCollisionException(message: str, inner: Exception)
    ForestTrustCollisionException(message: str)
    ForestTrustCollisionException()
    """
    @property
    def Collisions(self) -> ForestTrustRelationshipCollisionCollection:
        """ Get: Collisions(self: ForestTrustCollisionException) -> ForestTrustRelationshipCollisionCollection """
        ...


    SerializeObjectState = ...


class ForestTrustCollisionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ForestTrustCollisionType, values: Domain (1), Other (2), TopLevelName (0) """
    Domain: ForestTrustCollisionType = ...
    Other: ForestTrustCollisionType = ...
    TopLevelName: ForestTrustCollisionType = ...
    value__ = ...


class ForestTrustDomainInfoCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, information:ForestTrustDomainInformation) -> bool:
        """ Contains(self: ForestTrustDomainInfoCollection, information: ForestTrustDomainInformation) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ForestTrustDomainInfoCollection, array: Array[ForestTrustDomainInformation], index: int) """
        ...

    def IndexOf(self, information:ForestTrustDomainInformation) -> int:
        """ IndexOf(self: ForestTrustDomainInfoCollection, information: ForestTrustDomainInformation) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ForestTrustDomainInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DnsName(self) -> str:
        """ Get: DnsName(self: ForestTrustDomainInformation) -> str """
        ...

    @property
    def DomainSid(self) -> str:
        """ Get: DomainSid(self: ForestTrustDomainInformation) -> str """
        ...

    @property
    def NetBiosName(self) -> str:
        """ Get: NetBiosName(self: ForestTrustDomainInformation) -> str """
        ...

    @property
    def Status(self) -> ForestTrustDomainStatus:
        """
        Get: Status(self: ForestTrustDomainInformation) -> ForestTrustDomainStatus
        Set: Status(self: ForestTrustDomainInformation) = value
        """
        ...



class ForestTrustDomainStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ForestTrustDomainStatus, values: Enabled (0), NetBiosNameAdminDisabled (4), NetBiosNameConflictDisabled (8), SidAdminDisabled (1), SidConflictDisabled (2) """
    Enabled: ForestTrustDomainStatus = ...
    NetBiosNameAdminDisabled: ForestTrustDomainStatus = ...
    NetBiosNameConflictDisabled: ForestTrustDomainStatus = ...
    SidAdminDisabled: ForestTrustDomainStatus = ...
    SidConflictDisabled: ForestTrustDomainStatus = ...
    value__ = ...


class ForestTrustRelationshipCollision: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CollisionRecord(self) -> str:
        """ Get: CollisionRecord(self: ForestTrustRelationshipCollision) -> str """
        ...

    @property
    def CollisionType(self) -> ForestTrustCollisionType:
        """ Get: CollisionType(self: ForestTrustRelationshipCollision) -> ForestTrustCollisionType """
        ...

    @property
    def DomainCollisionOption(self) -> DomainCollisionOptions:
        """ Get: DomainCollisionOption(self: ForestTrustRelationshipCollision) -> DomainCollisionOptions """
        ...

    @property
    def TopLevelNameCollisionOption(self) -> TopLevelNameCollisionOptions:
        """ Get: TopLevelNameCollisionOption(self: ForestTrustRelationshipCollision) -> TopLevelNameCollisionOptions """
        ...



class ForestTrustRelationshipCollisionCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, collision:ForestTrustRelationshipCollision) -> bool:
        """ Contains(self: ForestTrustRelationshipCollisionCollection, collision: ForestTrustRelationshipCollision) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ForestTrustRelationshipCollisionCollection, array: Array[ForestTrustRelationshipCollision], index: int) """
        ...

    def IndexOf(self, collision:ForestTrustRelationshipCollision) -> int:
        """ IndexOf(self: ForestTrustRelationshipCollisionCollection, collision: ForestTrustRelationshipCollision) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TrustRelationshipInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SourceName(self) -> str:
        """ Get: SourceName(self: TrustRelationshipInformation) -> str """
        ...

    @property
    def TargetName(self) -> str:
        """ Get: TargetName(self: TrustRelationshipInformation) -> str """
        ...

    @property
    def TrustDirection(self) -> TrustDirection:
        """ Get: TrustDirection(self: TrustRelationshipInformation) -> TrustDirection """
        ...

    @property
    def TrustType(self) -> TrustType:
        """ Get: TrustType(self: TrustRelationshipInformation) -> TrustType """
        ...



class ForestTrustRelationshipInformation(TrustRelationshipInformation): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExcludedTopLevelNames(self) -> StringCollection:
        """ Get: ExcludedTopLevelNames(self: ForestTrustRelationshipInformation) -> StringCollection """
        ...

    @property
    def TopLevelNames(self) -> TopLevelNameCollection:
        """ Get: TopLevelNames(self: ForestTrustRelationshipInformation) -> TopLevelNameCollection """
        ...

    @property
    def TrustedDomainInformation(self) -> ForestTrustDomainInfoCollection:
        """ Get: TrustedDomainInformation(self: ForestTrustRelationshipInformation) -> ForestTrustDomainInfoCollection """
        ...


    def Save(self): # -> 
        """ Save(self: ForestTrustRelationshipInformation) """
        ...


class GlobalCatalog(DomainController): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def DisableGlobalCatalog(self) -> DomainController:
        """ DisableGlobalCatalog(self: GlobalCatalog) -> DomainController """
        ...

    def FindAllProperties(self) -> ReadOnlyActiveDirectorySchemaPropertyCollection:
        """ FindAllProperties(self: GlobalCatalog) -> ReadOnlyActiveDirectorySchemaPropertyCollection """
        ...

    @staticmethod
    def GetGlobalCatalog(context:DirectoryContext) -> GlobalCatalog:
        """ GetGlobalCatalog(context: DirectoryContext) -> GlobalCatalog """
        ...


class GlobalCatalogCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, globalCatalog:GlobalCatalog) -> bool:
        """ Contains(self: GlobalCatalogCollection, globalCatalog: GlobalCatalog) -> bool """
        ...

    def CopyTo(self, globalCatalogs:Array, index:int): # -> 
        """ CopyTo(self: GlobalCatalogCollection, globalCatalogs: Array[GlobalCatalog], index: int) """
        ...

    def IndexOf(self, globalCatalog:GlobalCatalog) -> int:
        """ IndexOf(self: GlobalCatalogCollection, globalCatalog: GlobalCatalog) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HourOfDay(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HourOfDay, values: Eight (8), Eighteen (18), Eleven (11), Fifteen (15), Five (5), Four (4), Fourteen (14), Nine (9), Nineteen (19), One (1), Seven (7), Seventeen (17), Six (6), Sixteen (16), Ten (10), Thirteen (13), Three (3), Twelve (12), Twenty (20), TwentyOne (21), TwentyThree (23), TwentyTwo (22), Two (2), Zero (0) """
    Eight: HourOfDay = ...
    Eighteen: HourOfDay = ...
    Eleven: HourOfDay = ...
    Fifteen: HourOfDay = ...
    Five: HourOfDay = ...
    Four: HourOfDay = ...
    Fourteen: HourOfDay = ...
    Nine: HourOfDay = ...
    Nineteen: HourOfDay = ...
    One: HourOfDay = ...
    Seven: HourOfDay = ...
    Seventeen: HourOfDay = ...
    Six: HourOfDay = ...
    Sixteen: HourOfDay = ...
    Ten: HourOfDay = ...
    Thirteen: HourOfDay = ...
    Three: HourOfDay = ...
    Twelve: HourOfDay = ...
    Twenty: HourOfDay = ...
    TwentyOne: HourOfDay = ...
    TwentyThree: HourOfDay = ...
    TwentyTwo: HourOfDay = ...
    Two: HourOfDay = ...
    value__ = ...
    Zero: HourOfDay = ...


class LocatorOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LocatorOptions, values: AvoidSelf (16384), ForceRediscovery (1), KdcRequired (1024), TimeServerRequired (2048), WriteableRequired (4096) """
    AvoidSelf: LocatorOptions = ...
    ForceRediscovery: LocatorOptions = ...
    KdcRequired: LocatorOptions = ...
    TimeServerRequired: LocatorOptions = ...
    value__ = ...
    WriteableRequired: LocatorOptions = ...


class MinuteOfHour(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MinuteOfHour, values: Fifteen (15), FortyFive (45), Thirty (30), Zero (0) """
    Fifteen: MinuteOfHour = ...
    FortyFive: MinuteOfHour = ...
    Thirty: MinuteOfHour = ...
    value__ = ...
    Zero: MinuteOfHour = ...


class NotificationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NotificationStatus, values: IntraSiteOnly (1), NoNotification (0), NotificationAlways (2) """
    IntraSiteOnly: NotificationStatus = ...
    NoNotification: NotificationStatus = ...
    NotificationAlways: NotificationStatus = ...
    value__ = ...


class PropertyTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropertyTypes, values: Indexed (2), InGlobalCatalog (4) """
    Indexed: PropertyTypes = ...
    InGlobalCatalog: PropertyTypes = ...
    value__ = ...


class ReadOnlyActiveDirectorySchemaClassCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, schemaClass:ActiveDirectorySchemaClass) -> bool:
        """ Contains(self: ReadOnlyActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) -> bool """
        ...

    def CopyTo(self, classes:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlyActiveDirectorySchemaClassCollection, classes: Array[ActiveDirectorySchemaClass], index: int) """
        ...

    def IndexOf(self, schemaClass:ActiveDirectorySchemaClass) -> int:
        """ IndexOf(self: ReadOnlyActiveDirectorySchemaClassCollection, schemaClass: ActiveDirectorySchemaClass) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlyActiveDirectorySchemaPropertyCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, schemaProperty:ActiveDirectorySchemaProperty) -> bool:
        """ Contains(self: ReadOnlyActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) -> bool """
        ...

    def CopyTo(self, properties:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlyActiveDirectorySchemaPropertyCollection, properties: Array[ActiveDirectorySchemaProperty], index: int) """
        ...

    def IndexOf(self, schemaProperty:ActiveDirectorySchemaProperty) -> int:
        """ IndexOf(self: ReadOnlyActiveDirectorySchemaPropertyCollection, schemaProperty: ActiveDirectorySchemaProperty) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlyDirectoryServerCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, directoryServer:DirectoryServer) -> bool:
        """ Contains(self: ReadOnlyDirectoryServerCollection, directoryServer: DirectoryServer) -> bool """
        ...

    def CopyTo(self, directoryServers:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlyDirectoryServerCollection, directoryServers: Array[DirectoryServer], index: int) """
        ...

    def IndexOf(self, directoryServer:DirectoryServer) -> int:
        """ IndexOf(self: ReadOnlyDirectoryServerCollection, directoryServer: DirectoryServer) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlySiteCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, site:ActiveDirectorySite) -> bool:
        """ Contains(self: ReadOnlySiteCollection, site: ActiveDirectorySite) -> bool """
        ...

    def CopyTo(self, sites:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlySiteCollection, sites: Array[ActiveDirectorySite], index: int) """
        ...

    def IndexOf(self, site:ActiveDirectorySite) -> int:
        """ IndexOf(self: ReadOnlySiteCollection, site: ActiveDirectorySite) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlySiteLinkBridgeCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, bridge:ActiveDirectorySiteLinkBridge) -> bool:
        """ Contains(self: ReadOnlySiteLinkBridgeCollection, bridge: ActiveDirectorySiteLinkBridge) -> bool """
        ...

    def CopyTo(self, bridges:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlySiteLinkBridgeCollection, bridges: Array[ActiveDirectorySiteLinkBridge], index: int) """
        ...

    def IndexOf(self, bridge:ActiveDirectorySiteLinkBridge) -> int:
        """ IndexOf(self: ReadOnlySiteLinkBridgeCollection, bridge: ActiveDirectorySiteLinkBridge) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlySiteLinkCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, link:ActiveDirectorySiteLink) -> bool:
        """ Contains(self: ReadOnlySiteLinkCollection, link: ActiveDirectorySiteLink) -> bool """
        ...

    def CopyTo(self, links:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlySiteLinkCollection, links: Array[ActiveDirectorySiteLink], index: int) """
        ...

    def IndexOf(self, link:ActiveDirectorySiteLink) -> int:
        """ IndexOf(self: ReadOnlySiteLinkCollection, link: ActiveDirectorySiteLink) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReadOnlyStringCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, value:str) -> bool:
        """ Contains(self: ReadOnlyStringCollection, value: str) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: ReadOnlyStringCollection, values: Array[str], index: int) """
        ...

    def IndexOf(self, value:str) -> int:
        """ IndexOf(self: ReadOnlyStringCollection, value: str) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationConnection(IDisposable): # skipped bases: <type 'object'>
    """
    ReplicationConnection(context: DirectoryContext, name: str, sourceServer: DirectoryServer)
    ReplicationConnection(context: DirectoryContext, name: str, sourceServer: DirectoryServer, schedule: ActiveDirectorySchedule)
    ReplicationConnection(context: DirectoryContext, name: str, sourceServer: DirectoryServer, transport: ActiveDirectoryTransportType)
    ReplicationConnection(context: DirectoryContext, name: str, sourceServer: DirectoryServer, schedule: ActiveDirectorySchedule, transport: ActiveDirectoryTransportType)
    """
    @property
    def ChangeNotificationStatus(self) -> NotificationStatus:
        """
        Get: ChangeNotificationStatus(self: ReplicationConnection) -> NotificationStatus
        Set: ChangeNotificationStatus(self: ReplicationConnection) = value
        """
        ...

    @property
    def DataCompressionEnabled(self) -> bool:
        """
        Get: DataCompressionEnabled(self: ReplicationConnection) -> bool
        Set: DataCompressionEnabled(self: ReplicationConnection) = value
        """
        ...

    @property
    def DestinationServer(self) -> str:
        """ Get: DestinationServer(self: ReplicationConnection) -> str """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ReplicationConnection) -> bool
        Set: Enabled(self: ReplicationConnection) = value
        """
        ...

    @property
    def GeneratedByKcc(self) -> bool:
        """
        Get: GeneratedByKcc(self: ReplicationConnection) -> bool
        Set: GeneratedByKcc(self: ReplicationConnection) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ReplicationConnection) -> str """
        ...

    @property
    def ReciprocalReplicationEnabled(self) -> bool:
        """
        Get: ReciprocalReplicationEnabled(self: ReplicationConnection) -> bool
        Set: ReciprocalReplicationEnabled(self: ReplicationConnection) = value
        """
        ...

    @property
    def ReplicationSchedule(self) -> ActiveDirectorySchedule:
        """
        Get: ReplicationSchedule(self: ReplicationConnection) -> ActiveDirectorySchedule
        Set: ReplicationSchedule(self: ReplicationConnection) = value
        """
        ...

    @property
    def ReplicationScheduleOwnedByUser(self) -> bool:
        """
        Get: ReplicationScheduleOwnedByUser(self: ReplicationConnection) -> bool
        Set: ReplicationScheduleOwnedByUser(self: ReplicationConnection) = value
        """
        ...

    @property
    def ReplicationSpan(self) -> ReplicationSpan:
        """ Get: ReplicationSpan(self: ReplicationConnection) -> ReplicationSpan """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: ReplicationConnection) -> str """
        ...

    @property
    def TransportType(self) -> ActiveDirectoryTransportType:
        """ Get: TransportType(self: ReplicationConnection) -> ActiveDirectoryTransportType """
        ...


    def Delete(self): # -> 
        """ Delete(self: ReplicationConnection) """
        ...

    @staticmethod
    def FindByName(context:DirectoryContext, name:str) -> ReplicationConnection:
        """ FindByName(context: DirectoryContext, name: str) -> ReplicationConnection """
        ...

    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: ReplicationConnection) -> DirectoryEntry """
        ...

    def Save(self): # -> 
        """ Save(self: ReplicationConnection) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ReplicationConnection) -> str """
        ...


class ReplicationConnectionCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, connection:ReplicationConnection) -> bool:
        """ Contains(self: ReplicationConnectionCollection, connection: ReplicationConnection) -> bool """
        ...

    def CopyTo(self, connections:Array, index:int): # -> 
        """ CopyTo(self: ReplicationConnectionCollection, connections: Array[ReplicationConnection], index: int) """
        ...

    def IndexOf(self, connection:ReplicationConnection) -> int:
        """ IndexOf(self: ReplicationConnectionCollection, connection: ReplicationConnection) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationCursor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LastSuccessfulSyncTime(self) -> DateTime:
        """ Get: LastSuccessfulSyncTime(self: ReplicationCursor) -> DateTime """
        ...

    @property
    def PartitionName(self) -> str:
        """ Get: PartitionName(self: ReplicationCursor) -> str """
        ...

    @property
    def SourceInvocationId(self) -> Guid:
        """ Get: SourceInvocationId(self: ReplicationCursor) -> Guid """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: ReplicationCursor) -> str """
        ...

    @property
    def UpToDatenessUsn(self) -> Int64:
        """ Get: UpToDatenessUsn(self: ReplicationCursor) -> Int64 """
        ...



class ReplicationCursorCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, cursor:ReplicationCursor) -> bool:
        """ Contains(self: ReplicationCursorCollection, cursor: ReplicationCursor) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: ReplicationCursorCollection, values: Array[ReplicationCursor], index: int) """
        ...

    def IndexOf(self, cursor:ReplicationCursor) -> int:
        """ IndexOf(self: ReplicationCursorCollection, cursor: ReplicationCursor) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationFailure: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConsecutiveFailureCount(self) -> int:
        """ Get: ConsecutiveFailureCount(self: ReplicationFailure) -> int """
        ...

    @property
    def FirstFailureTime(self) -> DateTime:
        """ Get: FirstFailureTime(self: ReplicationFailure) -> DateTime """
        ...

    @property
    def LastErrorCode(self) -> int:
        """ Get: LastErrorCode(self: ReplicationFailure) -> int """
        ...

    @property
    def LastErrorMessage(self) -> str:
        """ Get: LastErrorMessage(self: ReplicationFailure) -> str """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: ReplicationFailure) -> str """
        ...



class ReplicationFailureCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, failure:ReplicationFailure) -> bool:
        """ Contains(self: ReplicationFailureCollection, failure: ReplicationFailure) -> bool """
        ...

    def CopyTo(self, failures:Array, index:int): # -> 
        """ CopyTo(self: ReplicationFailureCollection, failures: Array[ReplicationFailure], index: int) """
        ...

    def IndexOf(self, failure:ReplicationFailure) -> int:
        """ IndexOf(self: ReplicationFailureCollection, failure: ReplicationFailure) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationNeighbor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConsecutiveFailureCount(self) -> int:
        """ Get: ConsecutiveFailureCount(self: ReplicationNeighbor) -> int """
        ...

    @property
    def LastAttemptedSync(self) -> DateTime:
        """ Get: LastAttemptedSync(self: ReplicationNeighbor) -> DateTime """
        ...

    @property
    def LastSuccessfulSync(self) -> DateTime:
        """ Get: LastSuccessfulSync(self: ReplicationNeighbor) -> DateTime """
        ...

    @property
    def LastSyncMessage(self) -> str:
        """ Get: LastSyncMessage(self: ReplicationNeighbor) -> str """
        ...

    @property
    def LastSyncResult(self) -> int:
        """ Get: LastSyncResult(self: ReplicationNeighbor) -> int """
        ...

    @property
    def PartitionName(self) -> str:
        """ Get: PartitionName(self: ReplicationNeighbor) -> str """
        ...

    @property
    def ReplicationNeighborOption(self): # -> ReplicationNeighborOptions
        """ Get: ReplicationNeighborOption(self: ReplicationNeighbor) -> ReplicationNeighborOptions """
        ...

    @property
    def SourceInvocationId(self) -> Guid:
        """ Get: SourceInvocationId(self: ReplicationNeighbor) -> Guid """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: ReplicationNeighbor) -> str """
        ...

    @property
    def TransportType(self) -> ActiveDirectoryTransportType:
        """ Get: TransportType(self: ReplicationNeighbor) -> ActiveDirectoryTransportType """
        ...

    @property
    def UsnAttributeFilter(self) -> Int64:
        """ Get: UsnAttributeFilter(self: ReplicationNeighbor) -> Int64 """
        ...

    @property
    def UsnLastObjectChangeSynced(self) -> Int64:
        """ Get: UsnLastObjectChangeSynced(self: ReplicationNeighbor) -> Int64 """
        ...


    def ReplicationNeighborOptions(self, *args): #cannot find CLR method
        """ enum (flags) ReplicationNeighborOptions, values: CompressChanges (268435456), DisableScheduledSync (134217728), FullSyncInProgress (65536), FullSyncNextPacket (131072), IgnoreChangeNotifications (67108864), NeverSynced (2097152), NoChangeNotifications (536870912), PartialAttributeSet (1073741824), Preempted (16777216), ReturnObjectParent (2048), ScheduledSync (64), SyncOnStartup (32), TwoWaySync (512), UseInterSiteTransport (128), Writeable (16) """
        ...



class ReplicationNeighborCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, neighbor:ReplicationNeighbor) -> bool:
        """ Contains(self: ReplicationNeighborCollection, neighbor: ReplicationNeighbor) -> bool """
        ...

    def CopyTo(self, neighbors:Array, index:int): # -> 
        """ CopyTo(self: ReplicationNeighborCollection, neighbors: Array[ReplicationNeighbor], index: int) """
        ...

    def IndexOf(self, neighbor:ReplicationNeighbor) -> int:
        """ IndexOf(self: ReplicationNeighborCollection, neighbor: ReplicationNeighbor) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationOperation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def OperationNumber(self) -> int:
        """ Get: OperationNumber(self: ReplicationOperation) -> int """
        ...

    @property
    def OperationType(self) -> ReplicationOperationType:
        """ Get: OperationType(self: ReplicationOperation) -> ReplicationOperationType """
        ...

    @property
    def PartitionName(self) -> str:
        """ Get: PartitionName(self: ReplicationOperation) -> str """
        ...

    @property
    def Priority(self) -> int:
        """ Get: Priority(self: ReplicationOperation) -> int """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: ReplicationOperation) -> str """
        ...

    @property
    def TimeEnqueued(self) -> DateTime:
        """ Get: TimeEnqueued(self: ReplicationOperation) -> DateTime """
        ...



class ReplicationOperationCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, operation:ReplicationOperation) -> bool:
        """ Contains(self: ReplicationOperationCollection, operation: ReplicationOperation) -> bool """
        ...

    def CopyTo(self, operations:Array, index:int): # -> 
        """ CopyTo(self: ReplicationOperationCollection, operations: Array[ReplicationOperation], index: int) """
        ...

    def IndexOf(self, operation:ReplicationOperation) -> int:
        """ IndexOf(self: ReplicationOperationCollection, operation: ReplicationOperation) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReplicationOperationInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ ReplicationOperationInformation() """
    @property
    def CurrentOperation(self) -> ReplicationOperation:
        """ Get: CurrentOperation(self: ReplicationOperationInformation) -> ReplicationOperation """
        ...

    @property
    def OperationStartTime(self) -> DateTime:
        """ Get: OperationStartTime(self: ReplicationOperationInformation) -> DateTime """
        ...

    @property
    def PendingOperations(self) -> ReplicationOperationCollection:
        """ Get: PendingOperations(self: ReplicationOperationInformation) -> ReplicationOperationCollection """
        ...



class ReplicationOperationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReplicationOperationType, values: Add (1), Delete (2), Modify (3), Sync (0), UpdateReference (4) """
    Add: ReplicationOperationType = ...
    Delete: ReplicationOperationType = ...
    Modify: ReplicationOperationType = ...
    Sync: ReplicationOperationType = ...
    UpdateReference: ReplicationOperationType = ...
    value__ = ...


class ReplicationSecurityLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReplicationSecurityLevel, values: MutualAuthentication (2), Negotiate (1), NegotiatePassThrough (0) """
    MutualAuthentication: ReplicationSecurityLevel = ...
    Negotiate: ReplicationSecurityLevel = ...
    NegotiatePassThrough: ReplicationSecurityLevel = ...
    value__ = ...


class ReplicationSpan(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReplicationSpan, values: InterSite (1), IntraSite (0) """
    InterSite: ReplicationSpan = ...
    IntraSite: ReplicationSpan = ...
    value__ = ...


class SchemaClassType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SchemaClassType, values: Abstract (2), Auxiliary (3), Structural (1), Type88 (0) """
    Abstract: SchemaClassType = ...
    Auxiliary: SchemaClassType = ...
    Structural: SchemaClassType = ...
    Type88: SchemaClassType = ...
    value__ = ...


class SyncFromAllServersErrorCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SyncFromAllServersErrorCategory, values: ErrorContactingServer (0), ErrorReplicating (1), ServerUnreachable (2) """
    ErrorContactingServer: SyncFromAllServersErrorCategory = ...
    ErrorReplicating: SyncFromAllServersErrorCategory = ...
    ServerUnreachable: SyncFromAllServersErrorCategory = ...
    value__ = ...


class SyncFromAllServersErrorInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ErrorCategory(self) -> SyncFromAllServersErrorCategory:
        """ Get: ErrorCategory(self: SyncFromAllServersErrorInformation) -> SyncFromAllServersErrorCategory """
        ...

    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: SyncFromAllServersErrorInformation) -> int """
        ...

    @property
    def ErrorMessage(self) -> str:
        """ Get: ErrorMessage(self: SyncFromAllServersErrorInformation) -> str """
        ...

    @property
    def SourceServer(self) -> str:
        """ Get: SourceServer(self: SyncFromAllServersErrorInformation) -> str """
        ...

    @property
    def TargetServer(self) -> str:
        """ Get: TargetServer(self: SyncFromAllServersErrorInformation) -> str """
        ...



class SyncFromAllServersEvent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SyncFromAllServersEvent, values: Error (0), Finished (3), SyncCompleted (2), SyncStarted (1) """
    Error: SyncFromAllServersEvent = ...
    Finished: SyncFromAllServersEvent = ...
    SyncCompleted: SyncFromAllServersEvent = ...
    SyncStarted: SyncFromAllServersEvent = ...
    value__ = ...


class SyncFromAllServersOperationException(ActiveDirectoryOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SyncFromAllServersOperationException(message: str, inner: Exception, errors: Array[SyncFromAllServersErrorInformation])
    SyncFromAllServersOperationException(message: str, inner: Exception)
    SyncFromAllServersOperationException(message: str)
    SyncFromAllServersOperationException()
    """
    @property
    def ErrorInformation(self) -> Array:
        """ Get: ErrorInformation(self: SyncFromAllServersOperationException) -> Array[SyncFromAllServersErrorInformation] """
        ...


    SerializeObjectState = ...


class SyncFromAllServersOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SyncFromAllServersOptions, values: AbortIfServerUnavailable (1), CheckServerAlivenessOnly (8), CrossSite (64), None (0), PushChangeOutward (32), SkipInitialCheck (16), SyncAdjacentServerOnly (2) """
    AbortIfServerUnavailable: SyncFromAllServersOptions = ...
    CheckServerAlivenessOnly: SyncFromAllServersOptions = ...
    CrossSite: SyncFromAllServersOptions = ...
    PushChangeOutward: SyncFromAllServersOptions = ...
    SkipInitialCheck: SyncFromAllServersOptions = ...
    SyncAdjacentServerOnly: SyncFromAllServersOptions = ...
    value__ = ...


class SyncUpdateCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SyncUpdateCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, eventType:SyncFromAllServersEvent, targetServer:str, sourceServer:str, exception:SyncFromAllServersOperationException, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SyncUpdateCallback, eventType: SyncFromAllServersEvent, targetServer: str, sourceServer: str, exception: SyncFromAllServersOperationException, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: SyncUpdateCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, eventType:SyncFromAllServersEvent, targetServer:str, sourceServer:str, exception:SyncFromAllServersOperationException) -> bool:
        """ Invoke(self: SyncUpdateCallback, eventType: SyncFromAllServersEvent, targetServer: str, sourceServer: str, exception: SyncFromAllServersOperationException) -> bool """
        ...


class TopLevelName: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: TopLevelName) -> str """
        ...

    @property
    def Status(self) -> TopLevelNameStatus:
        """
        Get: Status(self: TopLevelName) -> TopLevelNameStatus
        Set: Status(self: TopLevelName) = value
        """
        ...



class TopLevelNameCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, name:TopLevelName) -> bool:
        """ Contains(self: TopLevelNameCollection, name: TopLevelName) -> bool """
        ...

    def CopyTo(self, names:Array, index:int): # -> 
        """ CopyTo(self: TopLevelNameCollection, names: Array[TopLevelName], index: int) """
        ...

    def IndexOf(self, name:TopLevelName) -> int:
        """ IndexOf(self: TopLevelNameCollection, name: TopLevelName) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TopLevelNameCollisionOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TopLevelNameCollisionOptions, values: DisabledByAdmin (2), DisabledByConflict (4), NewlyCreated (1), None (0) """
    DisabledByAdmin: TopLevelNameCollisionOptions = ...
    DisabledByConflict: TopLevelNameCollisionOptions = ...
    NewlyCreated: TopLevelNameCollisionOptions = ...
    value__ = ...


class TopLevelNameStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TopLevelNameStatus, values: AdminDisabled (2), ConflictDisabled (4), Enabled (0), NewlyCreated (1) """
    AdminDisabled: TopLevelNameStatus = ...
    ConflictDisabled: TopLevelNameStatus = ...
    Enabled: TopLevelNameStatus = ...
    NewlyCreated: TopLevelNameStatus = ...
    value__ = ...


class TrustDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrustDirection, values: Bidirectional (3), Inbound (1), Outbound (2) """
    Bidirectional: TrustDirection = ...
    Inbound: TrustDirection = ...
    Outbound: TrustDirection = ...
    value__ = ...


class TrustRelationshipInformationCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, information:TrustRelationshipInformation) -> bool:
        """ Contains(self: TrustRelationshipInformationCollection, information: TrustRelationshipInformation) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TrustRelationshipInformationCollection, array: Array[TrustRelationshipInformation], index: int) """
        ...

    def IndexOf(self, information:TrustRelationshipInformation) -> int:
        """ IndexOf(self: TrustRelationshipInformationCollection, information: TrustRelationshipInformation) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TrustType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrustType, values: CrossLink (2), External (3), Forest (4), Kerberos (5), ParentChild (1), TreeRoot (0), Unknown (6) """
    CrossLink: TrustType = ...
    External: TrustType = ...
    Forest: TrustType = ...
    Kerberos: TrustType = ...
    ParentChild: TrustType = ...
    TreeRoot: TrustType = ...
    Unknown: TrustType = ...
    value__ = ...


