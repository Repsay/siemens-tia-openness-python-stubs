# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.Wmi calls itself Wmi
# from Microsoft.SqlServer.SqlWmiManagement, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.WmiEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IAlterable, ICreatable, 
    IDroppable)

from Microsoft.SqlServer.Management.Sdk.Sfc import Urn

from Microsoft.SqlServer.Management.Smo import SmoObjectBase

from Microsoft.Vbe.Interop import Property

from System import DateTime, Enum, TimeSpan

from System.Collections import ICollection, IEnumerator

from System.Collections.Specialized import StringCollection

from System.DirectoryServices import PropertyCollection

from System.Net import IPAddress

from System.ServiceProcess import ServiceStartMode

"""The following names are not found in the module: (BoundEvent, 
    ServiceErrorControl, ServiceState, field#)
"""

# no functions
# classes

class WmiSmoObject(SmoObjectBase): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: WmiSmoObject) -> str
        Set: Name(self: WmiSmoObject) = value
        """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: WmiSmoObject) -> PropertyCollection """
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: WmiSmoObject) -> Urn """
        ...


    def AlterProtocolProperties(self, *args): #cannot find CLR method
        """ AlterProtocolProperties(self: WmiSmoObject, protocolProperties: ProtocolPropertyCollection) """
        ...

    def CheckObjectState(self, *args): #cannot find CLR method
        """ CheckObjectState(self: WmiSmoObject) """
        ...

    def CreateProtocolPropertyCollection(self, *args): #cannot find CLR method
        """ CreateProtocolPropertyCollection(self: WmiSmoObject) -> ProtocolPropertyCollection """
        ...

    def GetPropertyManagementObject(self, *args): #cannot find CLR method
        """ GetPropertyManagementObject(self: WmiSmoObject, pp: ProtocolProperty) -> ManagementObject """
        ...

    def GetPropertyObject(self, *args): #cannot find CLR method
        """ GetPropertyObject(self: WmiSmoObject, properties: PropertyCollection, dr: DataRow, propValue: object) -> ProtocolProperty """
        ...

    def GetProtocolPropertyCollection(self, *args): #cannot find CLR method
        """ GetProtocolPropertyCollection(self: WmiSmoObject) -> ProtocolPropertyCollection """
        ...

    def ImplInitialize(self, *args): #cannot find CLR method
        """ ImplInitialize(self: WmiSmoObject, fields: Array[str], orderby: Array[OrderBy]) -> bool """
        ...

    def Initialize(self) -> bool:
        """ Initialize(self: WmiSmoObject) -> bool """
        ...

    def InvokeMgmtMethod(self, *args): #cannot find CLR method
        """ InvokeMgmtMethod(self: WmiSmoObject, mo: ManagementObject, methodName: str, parameters: Array[object])InvokeMgmtMethod(self: WmiSmoObject, mo: ManagementObject, observer: ManagementOperationObserver, methodName: str, parameters: Array[object]) """
        ...

    def IsObjectInitialized(self, *args): #cannot find CLR method
        """ IsObjectInitialized(self: WmiSmoObject) -> bool """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: WmiSmoObject) """
        ...

    def SetName(self, *args): #cannot find CLR method
        """ SetName(self: WmiSmoObject, name: str) """
        ...

    def SetParentImpl(self, *args): #cannot find CLR method
        """ SetParentImpl(self: WmiSmoObject, newParent: WmiSmoObject) """
        ...

    def Trace(self, *args): #cannot find CLR method
        """ Trace(traceText: str) """
        ...

    def UpdateObjectState(self, *args): #cannot find CLR method
        """ UpdateObjectState(self: WmiSmoObject) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, parentColl: WmiCollectionBase, name: str)
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        ...


class ProtocolBase(IAlterable, WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def ProtocolProperties(self) -> ProtocolPropertyCollection:
        """ Get: ProtocolProperties(self: ProtocolBase) -> ProtocolPropertyCollection """
        ...


    def GetManagementObject(self, *args): #cannot find CLR method
        """ GetManagementObject(self: ProtocolBase) -> ManagementObject """
        ...


class ClientProtocol(ProtocolBase): # skipped bases: <type 'ISfcValidate'>, <type 'IAlterable'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ClientProtocol) -> str """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: ClientProtocol) -> bool
        Set: IsEnabled(self: ClientProtocol) = value
        """
        ...

    @property
    def NetLibInfo(self) -> NetLibInfo:
        """ Get: NetLibInfo(self: ClientProtocol) -> NetLibInfo """
        ...

    @property
    def NetworkLibrary(self) -> str:
        """ Get: NetworkLibrary(self: ClientProtocol) -> str """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: ClientProtocol) -> int
        Set: Order(self: ClientProtocol) = value
        """
        ...

    @property
    def Parent(self) -> ManagedComputer:
        """ Get: Parent(self: ClientProtocol) -> ManagedComputer """
        ...



class WmiCollectionBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: WmiCollectionBase) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: WmiCollectionBase) -> object """
        ...


    def Add(self, *args): #cannot find CLR method
        """ Add(self: WmiCollectionBase, wmiObj: WmiSmoObject) """
        ...

    def Remove(self, *args): #cannot find CLR method
        """ Remove(self: WmiCollectionBase, objname: str) """
        ...

    initialized = ...
    innerColl = ...


class ClientProtocolCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ClientProtocolCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ClientProtocolCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ProtocolProperty(Property): # skipped bases: <type 'ISfcProperty'>, <type 'object'>
    """ no doc """
    pass

class ClientProtocolProperty(ProtocolProperty): # skipped bases: <type 'ISfcProperty'>, <type 'object'>
    """ no doc """
    pass

class ProtocolPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, name:str) -> bool:
        """ Contains(self: ProtocolPropertyCollection, name: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ProtocolPropertyCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ClientProtocolPropertyCollection(ProtocolPropertyCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class IPAddressProperty(ProtocolProperty): # skipped bases: <type 'ISfcProperty'>, <type 'object'>
    """ no doc """
    pass

class IPAddressPropertyCollection(ProtocolPropertyCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ManagedComputer(WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """
    ManagedComputer()
    ManagedComputer(machineName: str)
    ManagedComputer(machineName: str, userName: str, password: str)
    ManagedComputer(machineName: str, userName: str, password: str, providerArchitecture: ProviderArchitecture)
    """
    @property
    def ClientProtocols(self) -> ClientProtocolCollection:
        """ Get: ClientProtocols(self: ManagedComputer) -> ClientProtocolCollection """
        ...

    @property
    def ConnectionSettings(self) -> WmiConnectionInfo:
        """ Get: ConnectionSettings(self: ManagedComputer) -> WmiConnectionInfo """
        ...

    @property
    def ServerAliases(self) -> ServerAliasCollection:
        """ Get: ServerAliases(self: ManagedComputer) -> ServerAliasCollection """
        ...

    @property
    def ServerInstances(self) -> ServerInstanceCollection:
        """ Get: ServerInstances(self: ManagedComputer) -> ServerInstanceCollection """
        ...

    @property
    def Services(self) -> ServiceCollection:
        """ Get: Services(self: ManagedComputer) -> ServiceCollection """
        ...


    def GetSmoObject(self, urn:Urn) -> WmiSmoObject:
        """ GetSmoObject(self: ManagedComputer, urn: Urn) -> WmiSmoObject """
        ...


class ManagedServiceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ManagedServiceType, values: AnalysisServer (5), NotificationServer (8), ReportServer (6), Search (3), SqlAgent (2), SqlBrowser (7), SqlServer (1), SqlServerIntegrationService (4) """
    AnalysisServer: ManagedServiceType = ...
    NotificationServer: ManagedServiceType = ...
    ReportServer: ManagedServiceType = ...
    Search: ManagedServiceType = ...
    SqlAgent: ManagedServiceType = ...
    SqlBrowser: ManagedServiceType = ...
    SqlServer: ManagedServiceType = ...
    SqlServerIntegrationService: ManagedServiceType = ...
    value__ = ...


class NetLibInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Date(self) -> DateTime:
        """ Get: Date(self: NetLibInfo) -> DateTime """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: NetLibInfo) -> str """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: NetLibInfo) -> int """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: NetLibInfo) -> str """
        ...



class PropertyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyType, values: FlagValue (2), NumericValue (1), StringValue (0) """
    FlagValue: PropertyType = ...
    NumericValue: PropertyType = ...
    StringValue: PropertyType = ...
    value__ = ...


class ProviderArchitecture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProviderArchitecture, values: Default (0), Use32bit (32), Use64bit (64) """
    Default: ProviderArchitecture = ...
    Use32bit: ProviderArchitecture = ...
    Use64bit: ProviderArchitecture = ...
    value__ = ...


class ServerAlias(IDroppable, ICreatable, WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """
    ServerAlias(managedComputer: ManagedComputer, name: str)
    ServerAlias()
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: ServerAlias) -> str
        Set: ConnectionString(self: ServerAlias) = value
        """
        ...

    @property
    def Parent(self) -> ManagedComputer:
        """
        Get: Parent(self: ServerAlias) -> ManagedComputer
        Set: Parent(self: ServerAlias) = value
        """
        ...

    @property
    def ProtocolName(self) -> str:
        """
        Get: ProtocolName(self: ServerAlias) -> str
        Set: ProtocolName(self: ServerAlias) = value
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Get: ServerName(self: ServerAlias) -> str
        Set: ServerName(self: ServerAlias) = value
        """
        ...



class ServerAliasCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ServerAliasCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServerAliasCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServerInstance(WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> ManagedComputer:
        """ Get: Parent(self: ServerInstance) -> ManagedComputer """
        ...

    @property
    def ServerProtocols(self) -> ServerProtocolCollection:
        """ Get: ServerProtocols(self: ServerInstance) -> ServerProtocolCollection """
        ...



class ServerInstanceCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ServerInstanceCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServerInstanceCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServerIPAddress(WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def IPAddress(self) -> IPAddress:
        """ Get: IPAddress(self: ServerIPAddress) -> IPAddress """
        ...

    @property
    def IPAddressProperties(self) -> IPAddressPropertyCollection:
        """ Get: IPAddressProperties(self: ServerIPAddress) -> IPAddressPropertyCollection """
        ...

    @property
    def Parent(self) -> ServerProtocol:
        """ Get: Parent(self: ServerIPAddress) -> ServerProtocol """
        ...



class ServerIPAddressCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ServerIPAddressCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServerIPAddressCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServerProtocol(ProtocolBase): # skipped bases: <type 'ISfcValidate'>, <type 'IAlterable'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ServerProtocol) -> str """
        ...

    @property
    def HasMultiIPAddresses(self) -> bool:
        """ Get: HasMultiIPAddresses(self: ServerProtocol) -> bool """
        ...

    @property
    def IPAddresses(self) -> ServerIPAddressCollection:
        """ Get: IPAddresses(self: ServerProtocol) -> ServerIPAddressCollection """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: ServerProtocol) -> bool
        Set: IsEnabled(self: ServerProtocol) = value
        """
        ...

    @property
    def Parent(self) -> ServerInstance:
        """ Get: Parent(self: ServerProtocol) -> ServerInstance """
        ...



class ServerProtocolCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ServerProtocolCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServerProtocolCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServerProtocolProperty(ProtocolProperty): # skipped bases: <type 'ISfcProperty'>, <type 'object'>
    """ no doc """
    pass

class ServerProtocolPropertyCollection(ProtocolPropertyCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class Service(IAlterable, WmiSmoObject): # skipped bases: <type 'ISfcValidate'>, <type 'object'>
    """ no doc """
    @property
    def AcceptsPause(self) -> bool:
        """ Get: AcceptsPause(self: Service) -> bool """
        ...

    @property
    def AcceptsStop(self) -> bool:
        """ Get: AcceptsStop(self: Service) -> bool """
        ...

    @property
    def AdvancedProperties(self) -> PropertyCollection:
        """ Get: AdvancedProperties(self: Service) -> PropertyCollection """
        ...

    @property
    def Dependencies(self) -> StringCollection:
        """ Get: Dependencies(self: Service) -> StringCollection """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Service) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: Service) -> str """
        ...

    @property
    def ErrorControl(self): # -> ServiceErrorControl
        """ Get: ErrorControl(self: Service) -> ServiceErrorControl """
        ...

    @property
    def ExitCode(self) -> int:
        """ Get: ExitCode(self: Service) -> int """
        ...

    @property
    def IsHadrEnabled(self) -> bool:
        """ Get: IsHadrEnabled(self: Service) -> bool """
        ...

    @property
    def Parent(self) -> ManagedComputer:
        """ Get: Parent(self: Service) -> ManagedComputer """
        ...

    @property
    def PathName(self) -> str:
        """ Get: PathName(self: Service) -> str """
        ...

    @property
    def ProcessId(self) -> int:
        """ Get: ProcessId(self: Service) -> int """
        ...

    @property
    def ServiceAccount(self) -> str:
        """ Get: ServiceAccount(self: Service) -> str """
        ...

    @property
    def ServiceState(self): # -> ServiceState
        """ Get: ServiceState(self: Service) -> ServiceState """
        ...

    @property
    def StartMode(self) -> ServiceStartMode:
        """
        Get: StartMode(self: Service) -> ServiceStartMode
        Set: StartMode(self: Service) = value
        """
        ...

    @property
    def StartupParameters(self) -> str:
        """
        Get: StartupParameters(self: Service) -> str
        Set: StartupParameters(self: Service) = value
        """
        ...

    @property
    def Type(self) -> ManagedServiceType:
        """ Get: Type(self: Service) -> ManagedServiceType """
        ...


    def ChangeHadrServiceSetting(self, enable:bool): # -> 
        """ ChangeHadrServiceSetting(self: Service, enable: bool) """
        ...

    def ChangePassword(self, oldPassword:str, newPassword:str): # -> 
        """ ChangePassword(self: Service, oldPassword: str, newPassword: str) """
        ...

    def Pause(self): # -> 
        """ Pause(self: Service) """
        ...

    def Resume(self): # -> 
        """ Resume(self: Service) """
        ...

    def SetServiceAccount(self, userName:str, password:str): # -> 
        """ SetServiceAccount(self: Service, userName: str, password: str) """
        ...

    def Start(self): # -> 
        """ Start(self: Service) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Service) """
        ...

    ManagementStateChange = ...


class ServiceCollection(WmiCollectionBase, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Contains(self, key:str) -> bool:
        """ Contains(self: ServiceCollection, key: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ServiceCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    initialized = ...
    innerColl = ...


class ServiceErrorControl(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceErrorControl, values: Critical (3), Ignore (0), Normal (1), Severe (2), Unknown (4) """
    Critical: ServiceErrorControl = ...
    Ignore: ServiceErrorControl = ...
    Normal: ServiceErrorControl = ...
    Severe: ServiceErrorControl = ...
    Unknown: ServiceErrorControl = ...
    value__ = ...


class ServiceStartMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceStartMode, values: Auto (2), Boot (0), Disabled (4), Manual (3), System (1) """
    Auto: ServiceStartMode = ...
    Boot: ServiceStartMode = ...
    Disabled: ServiceStartMode = ...
    Manual: ServiceStartMode = ...
    System: ServiceStartMode = ...
    value__ = ...


class ServiceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceState, values: ContinuePending (5), Paused (7), PausePending (6), Running (4), StartPending (2), Stopped (1), StopPending (3), Unknown (8) """
    ContinuePending: ServiceState = ...
    Paused: ServiceState = ...
    PausePending: ServiceState = ...
    Running: ServiceState = ...
    StartPending: ServiceState = ...
    Stopped: ServiceState = ...
    StopPending: ServiceState = ...
    Unknown: ServiceState = ...
    value__ = ...


class WmiConnectionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: WmiConnectionInfo) -> str
        Set: MachineName(self: WmiConnectionInfo) = value
        """
        ...

    @property
    def ProviderArchitecture(self) -> ProviderArchitecture:
        """
        Get: ProviderArchitecture(self: WmiConnectionInfo) -> ProviderArchitecture
        Set: ProviderArchitecture(self: WmiConnectionInfo) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: WmiConnectionInfo) -> TimeSpan
        Set: Timeout(self: WmiConnectionInfo) = value
        """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: WmiConnectionInfo) -> str
        Set: Username(self: WmiConnectionInfo) = value
        """
        ...


    def SetPassword(self, password:str): # -> 
        """ SetPassword(self: WmiConnectionInfo, password: str) """
        ...


