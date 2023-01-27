# encoding: utf-8
# module System.Management.Automation.Remoting calls itself Remoting
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.WSMan.Management import AuthenticationMechanism

from System import (Enum, Guid, IDisposable, IntPtr, Nullable, TimeSpan, 
    TimeZone)

from System.Collections.Generic import List

from System.Globalization import CultureInfo

from System.Management.Automation import (PSCredential, PSPrimitiveDictionary, 
    RuntimeException)

from System.Management.Automation.Runspaces import (InitialSessionState, 
    OutputBufferingMode)

from System.Runtime.Serialization import ISerializable

from System.Security.Principal import IIdentity, IPrincipal, WindowsIdentity

from System.Threading import ManualResetEventSlim

"""The following names are not found in the module: (BoundEvent, Func, T, 
    field#)
"""

# no functions
# classes

class CmdletMethodInvoker: # skipped bases: <type 'object'>, <type 'object'>
    """ CmdletMethodInvoker[T]() """
    @property
    def Action(self): # -> Func
        """
        Get: Action(self: CmdletMethodInvoker[T]) -> Func[Cmdlet, T]
        Set: Action(self: CmdletMethodInvoker[T]) = value
        """
        ...

    @property
    def ExceptionThrownOnCmdletThread(self) -> Exception:
        """
        Get: ExceptionThrownOnCmdletThread(self: CmdletMethodInvoker[T]) -> Exception
        Set: ExceptionThrownOnCmdletThread(self: CmdletMethodInvoker[T]) = value
        """
        ...

    @property
    def Finished(self) -> ManualResetEventSlim:
        """
        Get: Finished(self: CmdletMethodInvoker[T]) -> ManualResetEventSlim
        Set: Finished(self: CmdletMethodInvoker[T]) = value
        """
        ...

    @property
    def MethodResult(self): # -> T
        """
        Get: MethodResult(self: CmdletMethodInvoker[T]) -> T
        Set: MethodResult(self: CmdletMethodInvoker[T]) = value
        """
        ...

    @property
    def SyncObject(self) -> object:
        """
        Get: SyncObject(self: CmdletMethodInvoker[T]) -> object
        Set: SyncObject(self: CmdletMethodInvoker[T]) = value
        """
        ...



class OriginInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    OriginInfo(computerName: str, runspaceID: Guid)
    OriginInfo(computerName: str, runspaceID: Guid, instanceID: Guid)
    """
    @property
    def InstanceID(self) -> Guid:
        """
        Get: InstanceID(self: OriginInfo) -> Guid
        Set: InstanceID(self: OriginInfo) = value
        """
        ...

    @property
    def PSComputerName(self) -> str:
        """ Get: PSComputerName(self: OriginInfo) -> str """
        ...

    @property
    def RunspaceID(self) -> Guid:
        """ Get: RunspaceID(self: OriginInfo) -> Guid """
        ...


    def ToString(self) -> str:
        """ ToString(self: OriginInfo) -> str """
        ...


class ProxyAccessType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProxyAccessType, values: AutoDetect (4), IEConfig (1), None (0), NoProxyServer (8), WinHttpConfig (2) """
    AutoDetect: ProxyAccessType = ...
    IEConfig: ProxyAccessType = ...
    NoProxyServer: ProxyAccessType = ...
    value__ = ...
    WinHttpConfig: ProxyAccessType = ...


class PSCertificateDetails: # skipped bases: <type 'object'>, <type 'object'>
    """ PSCertificateDetails(subject: str, issuerName: str, issuerThumbprint: str) """
    @property
    def IssuerName(self) -> str:
        """ Get: IssuerName(self: PSCertificateDetails) -> str """
        ...

    @property
    def IssuerThumbprint(self) -> str:
        """ Get: IssuerThumbprint(self: PSCertificateDetails) -> str """
        ...

    @property
    def Subject(self) -> str:
        """ Get: Subject(self: PSCertificateDetails) -> str """
        ...



class PSDirectException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ PSDirectException(message: str) """
    SerializeObjectState = ...


class PSIdentity(IIdentity): # skipped bases: <type 'object'>
    """ PSIdentity(authType: str, isAuthenticated: bool, userName: str, cert: PSCertificateDetails) """
    @property
    def CertificateDetails(self) -> PSCertificateDetails:
        """ Get: CertificateDetails(self: PSIdentity) -> PSCertificateDetails """
        ...



class PSPrincipal(IPrincipal): # skipped bases: <type 'object'>
    """ PSPrincipal(identity: PSIdentity, windowsIdentity: WindowsIdentity) """
    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity(self: PSPrincipal) -> WindowsIdentity """
        ...



class PSRemotingDataStructureException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSRemotingDataStructureException()
    PSRemotingDataStructureException(message: str)
    PSRemotingDataStructureException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PSRemotingTransportException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSRemotingTransportException()
    PSRemotingTransportException(message: str)
    PSRemotingTransportException(message: str, innerException: Exception)
    """
    @property
    def ErrorCode(self) -> int:
        """
        Get: ErrorCode(self: PSRemotingTransportException) -> int
        Set: ErrorCode(self: PSRemotingTransportException) = value
        """
        ...

    @property
    def TransportMessage(self) -> str:
        """
        Get: TransportMessage(self: PSRemotingTransportException) -> str
        Set: TransportMessage(self: PSRemotingTransportException) = value
        """
        ...


    def SetDefaultErrorRecord(self, *args): #cannot find CLR method
        """ SetDefaultErrorRecord(self: PSRemotingTransportException) """
        ...

    SerializeObjectState = ...


class PSRemotingTransportRedirectException(PSRemotingTransportException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSRemotingTransportRedirectException()
    PSRemotingTransportRedirectException(message: str)
    PSRemotingTransportRedirectException(message: str, innerException: Exception)
    """
    @property
    def RedirectLocation(self) -> str:
        """ Get: RedirectLocation(self: PSRemotingTransportRedirectException) -> str """
        ...


    SerializeObjectState = ...


class PSSenderInfo(ISerializable): # skipped bases: <type 'object'>
    """ PSSenderInfo(userPrincipal: PSPrincipal, httpUrl: str) """
    @property
    def ApplicationArguments(self) -> PSPrimitiveDictionary:
        """ Get: ApplicationArguments(self: PSSenderInfo) -> PSPrimitiveDictionary """
        ...

    @property
    def ClientTimeZone(self) -> TimeZone:
        """ Get: ClientTimeZone(self: PSSenderInfo) -> TimeZone """
        ...

    @property
    def ConfigurationName(self) -> str:
        """ Get: ConfigurationName(self: PSSenderInfo) -> str """
        ...

    @property
    def ConnectionString(self) -> str:
        """ Get: ConnectionString(self: PSSenderInfo) -> str """
        ...

    @property
    def UserInfo(self) -> PSPrincipal:
        """ Get: UserInfo(self: PSSenderInfo) -> PSPrincipal """
        ...



class PSSessionConfiguration(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetApplicationPrivateData(self, senderInfo:PSSenderInfo) -> PSPrimitiveDictionary:
        """ GetApplicationPrivateData(self: PSSessionConfiguration, senderInfo: PSSenderInfo) -> PSPrimitiveDictionary """
        ...

    def GetInitialSessionState(self, *__args:PSSenderInfo) -> InitialSessionState:
        """
        GetInitialSessionState(self: PSSessionConfiguration, sessionConfigurationData: PSSessionConfigurationData, senderInfo: PSSenderInfo, configProviderId: str) -> InitialSessionState
        GetInitialSessionState(self: PSSessionConfiguration, senderInfo: PSSenderInfo) -> InitialSessionState
        """
        ...

    def GetMaximumReceivedDataSizePerCommand(self, senderInfo:PSSenderInfo) -> Nullable:
        """ GetMaximumReceivedDataSizePerCommand(self: PSSessionConfiguration, senderInfo: PSSenderInfo) -> Nullable[int] """
        ...

    def GetMaximumReceivedObjectSize(self, senderInfo:PSSenderInfo) -> Nullable:
        """ GetMaximumReceivedObjectSize(self: PSSessionConfiguration, senderInfo: PSSenderInfo) -> Nullable[int] """
        ...


class PSSessionConfigurationData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ModulesToImport(self) -> List:
        """ Get: ModulesToImport(self: PSSessionConfigurationData) -> List[str] """
        ...

    @property
    def PrivateData(self) -> str:
        """ Get: PrivateData(self: PSSessionConfigurationData) -> str """
        ...


    IsServerManager: bool = ...


class PSSessionOption: # skipped bases: <type 'object'>, <type 'object'>
    """ PSSessionOption() """
    @property
    def ApplicationArguments(self) -> PSPrimitiveDictionary:
        """
        Get: ApplicationArguments(self: PSSessionOption) -> PSPrimitiveDictionary
        Set: ApplicationArguments(self: PSSessionOption) = value
        """
        ...

    @property
    def CancelTimeout(self) -> TimeSpan:
        """
        Get: CancelTimeout(self: PSSessionOption) -> TimeSpan
        Set: CancelTimeout(self: PSSessionOption) = value
        """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: PSSessionOption) -> CultureInfo
        Set: Culture(self: PSSessionOption) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: PSSessionOption) -> TimeSpan
        Set: IdleTimeout(self: PSSessionOption) = value
        """
        ...

    @property
    def IncludePortInSPN(self) -> bool:
        """
        Get: IncludePortInSPN(self: PSSessionOption) -> bool
        Set: IncludePortInSPN(self: PSSessionOption) = value
        """
        ...

    @property
    def MaxConnectionRetryCount(self) -> int:
        """
        Get: MaxConnectionRetryCount(self: PSSessionOption) -> int
        Set: MaxConnectionRetryCount(self: PSSessionOption) = value
        """
        ...

    @property
    def MaximumConnectionRedirectionCount(self) -> int:
        """
        Get: MaximumConnectionRedirectionCount(self: PSSessionOption) -> int
        Set: MaximumConnectionRedirectionCount(self: PSSessionOption) = value
        """
        ...

    @property
    def MaximumReceivedDataSizePerCommand(self) -> Nullable:
        """
        Get: MaximumReceivedDataSizePerCommand(self: PSSessionOption) -> Nullable[int]
        Set: MaximumReceivedDataSizePerCommand(self: PSSessionOption) = value
        """
        ...

    @property
    def MaximumReceivedObjectSize(self) -> Nullable:
        """
        Get: MaximumReceivedObjectSize(self: PSSessionOption) -> Nullable[int]
        Set: MaximumReceivedObjectSize(self: PSSessionOption) = value
        """
        ...

    @property
    def NoCompression(self) -> bool:
        """
        Get: NoCompression(self: PSSessionOption) -> bool
        Set: NoCompression(self: PSSessionOption) = value
        """
        ...

    @property
    def NoEncryption(self) -> bool:
        """
        Get: NoEncryption(self: PSSessionOption) -> bool
        Set: NoEncryption(self: PSSessionOption) = value
        """
        ...

    @property
    def NoMachineProfile(self) -> bool:
        """
        Get: NoMachineProfile(self: PSSessionOption) -> bool
        Set: NoMachineProfile(self: PSSessionOption) = value
        """
        ...

    @property
    def OpenTimeout(self) -> TimeSpan:
        """
        Get: OpenTimeout(self: PSSessionOption) -> TimeSpan
        Set: OpenTimeout(self: PSSessionOption) = value
        """
        ...

    @property
    def OperationTimeout(self) -> TimeSpan:
        """
        Get: OperationTimeout(self: PSSessionOption) -> TimeSpan
        Set: OperationTimeout(self: PSSessionOption) = value
        """
        ...

    @property
    def OutputBufferingMode(self) -> OutputBufferingMode:
        """
        Get: OutputBufferingMode(self: PSSessionOption) -> OutputBufferingMode
        Set: OutputBufferingMode(self: PSSessionOption) = value
        """
        ...

    @property
    def ProxyAccessType(self) -> ProxyAccessType:
        """
        Get: ProxyAccessType(self: PSSessionOption) -> ProxyAccessType
        Set: ProxyAccessType(self: PSSessionOption) = value
        """
        ...

    @property
    def ProxyAuthentication(self) -> AuthenticationMechanism:
        """
        Get: ProxyAuthentication(self: PSSessionOption) -> AuthenticationMechanism
        Set: ProxyAuthentication(self: PSSessionOption) = value
        """
        ...

    @property
    def ProxyCredential(self) -> PSCredential:
        """
        Get: ProxyCredential(self: PSSessionOption) -> PSCredential
        Set: ProxyCredential(self: PSSessionOption) = value
        """
        ...

    @property
    def SkipCACheck(self) -> bool:
        """
        Get: SkipCACheck(self: PSSessionOption) -> bool
        Set: SkipCACheck(self: PSSessionOption) = value
        """
        ...

    @property
    def SkipCNCheck(self) -> bool:
        """
        Get: SkipCNCheck(self: PSSessionOption) -> bool
        Set: SkipCNCheck(self: PSSessionOption) = value
        """
        ...

    @property
    def SkipRevocationCheck(self) -> bool:
        """
        Get: SkipRevocationCheck(self: PSSessionOption) -> bool
        Set: SkipRevocationCheck(self: PSSessionOption) = value
        """
        ...

    @property
    def UICulture(self) -> CultureInfo:
        """
        Get: UICulture(self: PSSessionOption) -> CultureInfo
        Set: UICulture(self: PSSessionOption) = value
        """
        ...

    @property
    def UseUTF16(self) -> bool:
        """
        Get: UseUTF16(self: PSSessionOption) -> bool
        Set: UseUTF16(self: PSSessionOption) = value
        """
        ...



class SessionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionType, values: Default (2), Empty (0), RestrictedRemoteServer (1) """
    Default: SessionType = ...
    Empty: SessionType = ...
    RestrictedRemoteServer: SessionType = ...
    value__ = ...


class WSManPluginManagedEntryInstanceWrapper(IDisposable): # skipped bases: <type 'object'>
    """ WSManPluginManagedEntryInstanceWrapper() """
    def GetEntryDelegate(self) -> IntPtr:
        """ GetEntryDelegate(self: WSManPluginManagedEntryInstanceWrapper) -> IntPtr """
        ...


class WSManPluginManagedEntryWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def InitPlugin(wkrPtrs:IntPtr) -> int:
        """ InitPlugin(wkrPtrs: IntPtr) -> int """
        ...

    @staticmethod
    def PSPluginOperationShutdownCallback(operationContext:object, timedOut:bool): # -> 
        """ PSPluginOperationShutdownCallback(operationContext: object, timedOut: bool) """
        ...

    @staticmethod
    def ShutdownPlugin(pluginContext:IntPtr): # -> 
        """ ShutdownPlugin(pluginContext: IntPtr) """
        ...

    @staticmethod
    def WSManPluginCommand(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, shellContext:IntPtr, commandLine:str, arguments:IntPtr): # -> 
        """ WSManPluginCommand(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, shellContext: IntPtr, commandLine: str, arguments: IntPtr) """
        ...

    @staticmethod
    def WSManPluginConnect(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, shellContext:IntPtr, commandContext:IntPtr, inboundConnectInformation:IntPtr): # -> 
        """ WSManPluginConnect(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, shellContext: IntPtr, commandContext: IntPtr, inboundConnectInformation: IntPtr) """
        ...

    @staticmethod
    def WSManPluginReceive(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, shellContext:IntPtr, commandContext:IntPtr, streamSet:IntPtr): # -> 
        """ WSManPluginReceive(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, shellContext: IntPtr, commandContext: IntPtr, streamSet: IntPtr) """
        ...

    @staticmethod
    def WSManPluginReleaseCommandContext(pluginContext:IntPtr, shellContext:IntPtr, commandContext:IntPtr): # -> 
        """ WSManPluginReleaseCommandContext(pluginContext: IntPtr, shellContext: IntPtr, commandContext: IntPtr) """
        ...

    @staticmethod
    def WSManPluginReleaseShellContext(pluginContext:IntPtr, shellContext:IntPtr): # -> 
        """ WSManPluginReleaseShellContext(pluginContext: IntPtr, shellContext: IntPtr) """
        ...

    @staticmethod
    def WSManPluginSend(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, shellContext:IntPtr, commandContext:IntPtr, stream:str, inboundData:IntPtr): # -> 
        """ WSManPluginSend(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, shellContext: IntPtr, commandContext: IntPtr, stream: str, inboundData: IntPtr) """
        ...

    @staticmethod
    def WSManPluginShell(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, extraInfo:str, startupInfo:IntPtr, inboundShellInformation:IntPtr): # -> 
        """ WSManPluginShell(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, extraInfo: str, startupInfo: IntPtr, inboundShellInformation: IntPtr) """
        ...

    @staticmethod
    def WSManPluginSignal(pluginContext:IntPtr, requestDetails:IntPtr, flags:int, shellContext:IntPtr, commandContext:IntPtr, code:str): # -> 
        """ WSManPluginSignal(pluginContext: IntPtr, requestDetails: IntPtr, flags: int, shellContext: IntPtr, commandContext: IntPtr, code: str) """
        ...


# variables with complex values

