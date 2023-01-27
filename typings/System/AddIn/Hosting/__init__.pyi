# encoding: utf-8
# module System.AddIn.Hosting calls itself Hosting
# from System.AddIn, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import AppDomain, Array, Enum, TimeSpan, Type

from System.Collections import IDictionary, IEnumerable

from System.Reflection import AssemblyName

"""The following names are not found in the module: BoundEvent, T, field#
"""

# no functions
# classes

class AddInController: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AddInEnvironment(self) -> AddInEnvironment:
        """ Get: AddInEnvironment(self: AddInController) -> AddInEnvironment """
        ...

    @property
    def AppDomain(self) -> AppDomain:
        """ Get: AppDomain(self: AddInController) -> AppDomain """
        ...

    @property
    def Token(self) -> AddInToken:
        """ Get: Token(self: AddInController) -> AddInToken """
        ...


    @staticmethod
    def GetAddInController(addIn:object) -> AddInController:
        """ GetAddInController(addIn: object) -> AddInController """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: AddInController) """
        ...


class AddInEnvironment: # skipped bases: <type 'object'>, <type 'object'>
    """ AddInEnvironment(appDomain: AppDomain) """
    @property
    def Process(self) -> AddInProcess:
        """ Get: Process(self: AddInEnvironment) -> AddInProcess """
        ...



class AddInProcess: # skipped bases: <type 'object'>, <type 'object'>
    """
    AddInProcess()
    AddInProcess(platform: Platform)
    """
    @property
    def IsCurrentProcess(self) -> bool:
        """ Get: IsCurrentProcess(self: AddInProcess) -> bool """
        ...

    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: AddInProcess) -> bool
        Set: KeepAlive(self: AddInProcess) = value
        """
        ...

    @property
    def Platform(self) -> Platform:
        """ Get: Platform(self: AddInProcess) -> Platform """
        ...

    @property
    def ProcessId(self) -> int:
        """ Get: ProcessId(self: AddInProcess) -> int """
        ...

    @property
    def StartupTimeout(self) -> TimeSpan:
        """
        Get: StartupTimeout(self: AddInProcess) -> TimeSpan
        Set: StartupTimeout(self: AddInProcess) = value
        """
        ...


    def Shutdown(self) -> bool:
        """ Shutdown(self: AddInProcess) -> bool """
        ...

    def Start(self) -> bool:
        """ Start(self: AddInProcess) -> bool """
        ...

    ShuttingDown = ...


class AddInSecurityLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AddInSecurityLevel, values: FullTrust (2), Host (3), Internet (0), Intranet (1) """
    FullTrust: AddInSecurityLevel = ...
    Host: AddInSecurityLevel = ...
    Internet: AddInSecurityLevel = ...
    Intranet: AddInSecurityLevel = ...
    value__ = ...


class AddInSegmentDirectoryNotFoundException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AddInSegmentDirectoryNotFoundException(message: str)
    AddInSegmentDirectoryNotFoundException(message: str, innerException: Exception)
    AddInSegmentDirectoryNotFoundException()
    """
    SerializeObjectState = ...


class AddInSegmentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AddInSegmentType, values: AddIn (5), AddInSideAdapter (3), AddInView (4), Contract (2), HostSideAdapter (1), HostViewOfAddIn (0) """
    AddIn: AddInSegmentType = ...
    AddInSideAdapter: AddInSegmentType = ...
    AddInView: AddInSegmentType = ...
    Contract: AddInSegmentType = ...
    HostSideAdapter: AddInSegmentType = ...
    HostViewOfAddIn: AddInSegmentType = ...
    value__ = ...


class AddInStore: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FindAddIn(hostViewOfAddIn:Type, pipelineRootFolderPath:str, addInFilePath:str, addInTypeName:str) -> Collection:
        """ FindAddIn(hostViewOfAddIn: Type, pipelineRootFolderPath: str, addInFilePath: str, addInTypeName: str) -> Collection[AddInToken] """
        ...

    @staticmethod
    def FindAddIns(hostViewOfAddIn:Type, *__args:PipelineStoreLocation) -> Collection:
        """
        FindAddIns(hostViewOfAddIn: Type, location: PipelineStoreLocation) -> Collection[AddInToken]
        FindAddIns(hostViewOfAddIn: Type, location: PipelineStoreLocation, *addInFolderPaths: Array[str]) -> Collection[AddInToken]
        FindAddIns(hostViewOfAddIn: Type, pipelineRootFolderPath: str, *addInFolderPaths: Array[str]) -> Collection[AddInToken]
        """
        ...

    @staticmethod
    def Rebuild(*__args:str) -> Array:
        """
        Rebuild(pipelineRootFolderPath: str) -> Array[str]
        Rebuild(location: PipelineStoreLocation) -> Array[str]
        """
        ...

    @staticmethod
    def RebuildAddIns(addInsFolderPath:str) -> Array:
        """ RebuildAddIns(addInsFolderPath: str) -> Array[str] """
        ...

    @staticmethod
    def Update(*__args:PipelineStoreLocation) -> Array:
        """
        Update(location: PipelineStoreLocation) -> Array[str]
        Update(pipelineRootFolderPath: str) -> Array[str]
        """
        ...

    @staticmethod
    def UpdateAddIns(addInsFolderPath:str) -> Array:
        """ UpdateAddIns(addInsFolderPath: str) -> Array[str] """
        ...

    __all__: list = ...


class AddInToken(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AddInFullName(self) -> str:
        """ Get: AddInFullName(self: AddInToken) -> str """
        ...

    @property
    def AssemblyName(self) -> AssemblyName:
        """ Get: AssemblyName(self: AddInToken) -> AssemblyName """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: AddInToken) -> str """
        ...

    @property
    def EnableDirectConnect(self) -> bool:
        """
        Get: EnableDirectConnect() -> bool
        Set: EnableDirectConnect() = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AddInToken) -> str """
        ...

    @property
    def Publisher(self) -> str:
        """ Get: Publisher(self: AddInToken) -> str """
        ...

    @property
    def QualificationData(self) -> IDictionary:
        """ Get: QualificationData(self: AddInToken) -> IDictionary[AddInSegmentType, IDictionary[str, str]] """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: AddInToken) -> str """
        ...


    def Activate(self, *__args:AddInSecurityLevel): # -> T
        """
        Activate[T](self: AddInToken, trustLevel: AddInSecurityLevel) -> T
        Activate[T](self: AddInToken, trustLevel: AddInSecurityLevel, appDomainName: str) -> T
        Activate[T](self: AddInToken, target: AppDomain) -> T
        Activate[T](self: AddInToken, permissions: PermissionSet) -> T
        Activate[T](self: AddInToken, process: AddInProcess, permissionSet: PermissionSet) -> T
        Activate[T](self: AddInToken, process: AddInProcess, level: AddInSecurityLevel) -> T
        Activate[T](self: AddInToken, environment: AddInEnvironment) -> T
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: AddInToken, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AddInToken) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: AddInToken) -> str """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QualificationDataItem](enumerable: IEnumerable[QualificationDataItem], value: QualificationDataItem) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class InvalidPipelineStoreException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidPipelineStoreException(message: str)
    InvalidPipelineStoreException(message: str, innerException: Exception)
    InvalidPipelineStoreException()
    """
    SerializeObjectState = ...


class PipelineStoreLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PipelineStoreLocation, values: ApplicationBase (0) """
    ApplicationBase: PipelineStoreLocation = ...
    value__ = ...


class Platform(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Platform, values: AnyCpu (1), ARM (4), Host (0), X64 (3), X86 (2) """
    AnyCpu: Platform = ...
    ARM: Platform = ...
    Host: Platform = ...
    value__ = ...
    X64: Platform = ...
    X86: Platform = ...


class QualificationDataItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: QualificationDataItem) -> str """
        ...

    @property
    def Segment(self) -> AddInSegmentType:
        """ Get: Segment(self: QualificationDataItem) -> AddInSegmentType """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: QualificationDataItem) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: QualificationDataItem, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: QualificationDataItem) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


