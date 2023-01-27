# encoding: utf-8
# module Microsoft.AnalysisServices.SPClient.Interfaces calls itself Interfaces
# from Microsoft.AnalysisServices.SPClient.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IDisposable

from System.Diagnostics import TraceLevel

from System.IO import Stream

from System.Runtime.InteropServices.ComTypes import IStream

from System.Security.Principal import WindowsIdentity

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ASSPClientProxyFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ ASSPClientProxyFactory() """
    @staticmethod
    def CreateProxy() -> IASSPClientProxy:
        """ CreateProxy() -> IASSPClientProxy """
        ...

    WssRegistryPath: str = ...


class ConnectionStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConnectionStyle, values: Direct (0), ProxyStream (1) """
    Direct: ConnectionStyle = ...
    ProxyStream: ConnectionStyle = ...
    value__ = ...


class ExcelServicesException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExcelServicesException()
    ExcelServicesException(message: str)
    ExcelServicesException(message: str, innerException: Exception)
    ExcelServicesException(name: str, excelStatusMessage: str, severity: str)
    ExcelServicesException(message: str, innerException: Exception, name: str, excelStatusMessage: str, severity: str)
    """
    @property
    def ExcelStatusMessage(self) -> str:
        """ Get: ExcelStatusMessage(self: ExcelServicesException) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ExcelServicesException) -> str """
        ...

    @property
    def Severity(self) -> str:
        """ Get: Severity(self: ExcelServicesException) -> str """
        ...


    SerializeObjectState = ...


class IASSPClientProxy: # skipped bases: <type 'object'>
    """ no doc """
    def GetLinkFile(self, in_bstrLinkFilePath:str) -> ILinkFile:
        """ GetLinkFile(self: IASSPClientProxy, in_bstrLinkFilePath: str) -> ILinkFile """
        ...

    def GetWindowsIdentityFromCurrentPrincipal(self) -> WindowsIdentity:
        """ GetWindowsIdentityFromCurrentPrincipal(self: IASSPClientProxy) -> WindowsIdentity """
        ...

    def IsFarmRunning(self) -> bool:
        """ IsFarmRunning(self: IASSPClientProxy) -> bool """
        ...

    def IsRunningInFarm(self, majorVersion:int) -> bool:
        """ IsRunningInFarm(self: IASSPClientProxy, majorVersion: int) -> bool """
        ...

    def IsWorkbookInFarm(self, in_bstrWorkbookPath:str) -> bool:
        """ IsWorkbookInFarm(self: IASSPClientProxy, in_bstrWorkbookPath: str) -> bool """
        ...

    def Log(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str): # -> 
        """ Log(self: IASSPClientProxy, e_inTraceLevel: TraceLevel, bstr_inMsg: str) """
        ...

    def Log1(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str): # -> 
        """ Log1(self: IASSPClientProxy, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str) """
        ...

    def Log2(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str): # -> 
        """ Log2(self: IASSPClientProxy, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str) """
        ...

    def Log3(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str, bstr_inParam3:str): # -> 
        """ Log3(self: IASSPClientProxy, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str, bstr_inParam3: str) """
        ...

    def Log4(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str, bstr_inParam3:str, bstr_inParam4:str): # -> 
        """ Log4(self: IASSPClientProxy, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str, bstr_inParam3: str, bstr_inParam4: str) """
        ...

    def OpenWorkbookModel(self, in_bstrWorkbookPath:str, in_lifetimePolicy:SessionLifetimePolicy = ...) -> IWorkbookSession:
        """
        OpenWorkbookModel(self: IASSPClientProxy, in_bstrWorkbookPath: str) -> IWorkbookSession
        OpenWorkbookModel(self: IASSPClientProxy, in_bstrWorkbookPath: str, in_lifetimePolicy: SessionLifetimePolicy) -> IWorkbookSession
        """
        ...

    def OpenWorkbookModelForRefresh(self, in_bstrWorkbookPath:str, in_lifetimePolicy:SessionLifetimePolicy = ...) -> IWorkbookSession:
        """
        OpenWorkbookModelForRefresh(self: IASSPClientProxy, in_bstrWorkbookPath: str) -> IWorkbookSession
        OpenWorkbookModelForRefresh(self: IASSPClientProxy, in_bstrWorkbookPath: str, in_lifetimePolicy: SessionLifetimePolicy) -> IWorkbookSession
        """
        ...

    def OpenWorkbookSession(self, in_bstrWorkbookPath:str, in_bstrSessionId:str, in_lifetimePolicy:SessionLifetimePolicy = ...) -> IWorkbookSession:
        """
        OpenWorkbookSession(self: IASSPClientProxy, in_bstrWorkbookPath: str, in_bstrSessionId: str) -> IWorkbookSession
        OpenWorkbookSession(self: IASSPClientProxy, in_bstrWorkbookPath: str, in_bstrSessionId: str, in_lifetimePolicy: SessionLifetimePolicy) -> IWorkbookSession
        """
        ...

    def TraceError(self, message:str, args:Array): # -> 
        """ TraceError(self: IASSPClientProxy, message: str, *args: Array[object]) """
        ...

    def TraceVerbose(self, message:str, args:Array): # -> 
        """ TraceVerbose(self: IASSPClientProxy, message: str, *args: Array[object]) """
        ...

    def TraceWarning(self, message:str, args:Array): # -> 
        """ TraceWarning(self: IASSPClientProxy, message: str, *args: Array[object]) """
        ...


class ILinkFile: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Database(self) -> str:
        """ Get: Database(self: ILinkFile) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: ILinkFile) -> str """
        ...

    @property
    def IsDelegationAllowed(self) -> bool:
        """ Get: IsDelegationAllowed(self: ILinkFile) -> bool """
        ...

    @property
    def IsFileMalformed(self) -> bool:
        """ Get: IsFileMalformed(self: ILinkFile) -> bool """
        ...

    @property
    def IsInFarm(self) -> bool:
        """ Get: IsInFarm(self: ILinkFile) -> bool """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: ILinkFile) -> str """
        ...



class IWorkbookSession(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionStyle(self) -> ConnectionStyle:
        """ Get: ConnectionStyle(self: IWorkbookSession) -> ConnectionStyle """
        ...

    @property
    def Database(self) -> str:
        """ Get: Database(self: IWorkbookSession) -> str """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: IWorkbookSession) -> str """
        ...

    @property
    def SessionId(self) -> str:
        """ Get: SessionId(self: IWorkbookSession) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: IWorkbookSession) -> str """
        ...

    @property
    def WorkbookFormatVersion(self) -> WorkbookFileFormat:
        """ Get: WorkbookFormatVersion(self: IWorkbookSession) -> WorkbookFileFormat """
        ...

    @property
    def WorkbookPath(self) -> str:
        """ Get: WorkbookPath(self: IWorkbookSession) -> str """
        ...


    def BeginActivity(self): # -> 
        """ BeginActivity(self: IWorkbookSession) """
        ...

    def CreateManagedStream(self) -> Stream:
        """ CreateManagedStream(self: IWorkbookSession) -> Stream """
        ...

    def CreateNativeStream(self) -> IStream:
        """ CreateNativeStream(self: IWorkbookSession) -> IStream """
        ...

    def EndActivity(self): # -> 
        """ EndActivity(self: IWorkbookSession) """
        ...

    def EndSession(self): # -> 
        """ EndSession(self: IWorkbookSession) """
        ...

    def EnsureValidSession(self): # -> 
        """ EnsureValidSession(self: IWorkbookSession) """
        ...

    def GetWorkbookConnections(self) -> Array:
        """ GetWorkbookConnections(self: IWorkbookSession) -> Array[str] """
        ...

    def Log(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str): # -> 
        """ Log(self: IWorkbookSession, e_inTraceLevel: TraceLevel, bstr_inMsg: str) """
        ...

    def Log1(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str): # -> 
        """ Log1(self: IWorkbookSession, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str) """
        ...

    def Log2(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str): # -> 
        """ Log2(self: IWorkbookSession, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str) """
        ...

    def Log3(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str, bstr_inParam3:str): # -> 
        """ Log3(self: IWorkbookSession, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str, bstr_inParam3: str) """
        ...

    def Log4(self, e_inTraceLevel:TraceLevel, bstr_inMsg:str, bstr_inParam1:str, bstr_inParam2:str, bstr_inParam3:str, bstr_inParam4:str): # -> 
        """ Log4(self: IWorkbookSession, e_inTraceLevel: TraceLevel, bstr_inMsg: str, bstr_inParam1: str, bstr_inParam2: str, bstr_inParam3: str, bstr_inParam4: str) """
        ...

    def Refresh(self, in_bstrTargetApplicationId:str, in_bstrConnectionName:str): # -> 
        """ Refresh(self: IWorkbookSession, in_bstrTargetApplicationId: str, in_bstrConnectionName: str) """
        ...

    def RefreshEmbeddedModel(self): # -> 
        """ RefreshEmbeddedModel(self: IWorkbookSession) """
        ...

    def ReportQueryExecution(self, elapsedTime:int, in_bstrQuery:str): # -> 
        """ ReportQueryExecution(self: IWorkbookSession, elapsedTime: int, in_bstrQuery: str) """
        ...

    def Save(self): # -> 
        """ Save(self: IWorkbookSession) """
        ...

    def TraceError(self, message:str, args:Array): # -> 
        """ TraceError(self: IWorkbookSession, message: str, *args: Array[object]) """
        ...

    def TraceVerbose(self, message:str, args:Array): # -> 
        """ TraceVerbose(self: IWorkbookSession, message: str, *args: Array[object]) """
        ...

    def TraceWarning(self, message:str, args:Array): # -> 
        """ TraceWarning(self: IWorkbookSession, message: str, *args: Array[object]) """
        ...


class SessionLifetimePolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SessionLifetimePolicy, values: CloseSessionOnDispose (1), KeepActiveSessionAlive (2), None (0), VersionCheckOnSave (4) """
    CloseSessionOnDispose: SessionLifetimePolicy = ...
    KeepActiveSessionAlive: SessionLifetimePolicy = ...
    value__ = ...
    VersionCheckOnSave: SessionLifetimePolicy = ...


class WorkbookFileFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkbookFileFormat, values: Excel2010 (14), Excel2013 (15), Excel2016 (16), Unknown (0) """
    Excel2010: WorkbookFileFormat = ...
    Excel2013: WorkbookFileFormat = ...
    Excel2016: WorkbookFileFormat = ...
    Unknown: WorkbookFileFormat = ...
    value__ = ...


