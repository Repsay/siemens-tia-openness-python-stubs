# encoding: utf-8
# module System.Management.Automation.Runspaces calls itself Runspaces
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import ScriptBlock

from Microsoft.PowerShell import ExecutionPolicy

from Microsoft.VisualBasic import Collection

from Microsoft.WSMan.Management import ProxyAccessType

from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, Guid, 
    IAsyncResult, IDisposable, Int64, Nullable, SystemException, TimeSpan, 
    Type, UInt32, Uri, Version)

from System.Collections import IEnumerable

from System.Collections.Generic import Dictionary, HashSet, List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Diagnostics import Debugger, Process

from System.Globalization import CultureInfo

from System.Management.Automation import (AuthorizationManager, 
    CmdletProviderManagementIntrinsics, CommandInvocationIntrinsics, 
    CommandOrigin, CommandTypes, DebugRecord, DriveManagementIntrinsics, 
    ErrorRecord, ExtendedTypeDefinition, IContainsErrorRecord, 
    InformationRecord, JobManager, PSCredential, PSDataCollection, 
    PSEventManager, PSLanguageMode, PSModuleInfo, PSPrimitiveDictionary, 
    PSSnapInInfo, PSVariableIntrinsics, PathIntrinsics, PowerShell, 
    ProgressRecord, ProviderIntrinsics, RollbackSeverity, 
    RunspacePoolStateInfo, RuntimeException, ScopedItemOptions, 
    SessionCapabilities, SessionStateEntryVisibility, VerboseRecord, 
    WarningRecord)

from System.Management.Automation.Host import PSHost

from System.Management.Automation.Remoting import (OriginInfo, 
    PSSessionOption)

from System.Reflection import MethodInfo

from System.Threading import ApartmentState, WaitHandle

from System.Transactions import CommittableTransaction

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, T, 
    field#)
"""

# no functions
# classes

class TypeMemberData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: TypeMemberData) -> str """
        ...



class AliasPropertyData(TypeMemberData): # skipped bases: <type 'object'>
    """
    AliasPropertyData(name: str, referencedMemberName: str)
    AliasPropertyData(name: str, referencedMemberName: str, type: Type)
    """
    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: AliasPropertyData) -> bool
        Set: IsHidden(self: AliasPropertyData) = value
        """
        ...

    @property
    def MemberType(self) -> Type:
        """
        Get: MemberType(self: AliasPropertyData) -> Type
        Set: MemberType(self: AliasPropertyData) = value
        """
        ...

    @property
    def ReferencedMemberName(self) -> str:
        """
        Get: ReferencedMemberName(self: AliasPropertyData) -> str
        Set: ReferencedMemberName(self: AliasPropertyData) = value
        """
        ...


    def __new__(cls, name:str, referencedMemberName:str, type:Type = ...) -> Self:
        """
        __new__(cls: type, name: str, referencedMemberName: str)
        __new__(cls: type, name: str, referencedMemberName: str, type: Type)
        """
        ...


class RunspaceConfigurationEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: RunspaceConfigurationEntry) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RunspaceConfigurationEntry) -> str """
        ...

    @property
    def PSSnapIn(self) -> PSSnapInInfo:
        """ Get: PSSnapIn(self: RunspaceConfigurationEntry) -> PSSnapInInfo """
        ...



class AssemblyConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """ AssemblyConfigurationEntry(name: str, fileName: str) """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: AssemblyConfigurationEntry) -> str """
        ...



class AuthenticationMechanism(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationMechanism, values: Basic (1), Credssp (4), Default (0), Digest (5), Kerberos (6), Negotiate (2), NegotiateWithImplicitCredential (3) """
    Basic: AuthenticationMechanism = ...
    Credssp: AuthenticationMechanism = ...
    Default: AuthenticationMechanism = ...
    Digest: AuthenticationMechanism = ...
    Kerberos: AuthenticationMechanism = ...
    Negotiate: AuthenticationMechanism = ...
    NegotiateWithImplicitCredential: AuthenticationMechanism = ...
    value__ = ...


class CmdletConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """ CmdletConfigurationEntry(name: str, implementingType: Type, helpFileName: str) """
    @property
    def HelpFileName(self) -> str:
        """ Get: HelpFileName(self: CmdletConfigurationEntry) -> str """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: CmdletConfigurationEntry) -> Type """
        ...



class CodeMethodData(TypeMemberData): # skipped bases: <type 'object'>
    """ CodeMethodData(name: str, methodToCall: MethodInfo) """
    @property
    def CodeReference(self) -> MethodInfo:
        """
        Get: CodeReference(self: CodeMethodData) -> MethodInfo
        Set: CodeReference(self: CodeMethodData) = value
        """
        ...


    def __new__(cls, name:str, methodToCall:MethodInfo) -> Self:
        """ __new__(cls: type, name: str, methodToCall: MethodInfo) """
        ...


class CodePropertyData(TypeMemberData): # skipped bases: <type 'object'>
    """
    CodePropertyData(name: str, getMethod: MethodInfo)
    CodePropertyData(name: str, getMethod: MethodInfo, setMethod: MethodInfo)
    """
    @property
    def GetCodeReference(self) -> MethodInfo:
        """
        Get: GetCodeReference(self: CodePropertyData) -> MethodInfo
        Set: GetCodeReference(self: CodePropertyData) = value
        """
        ...

    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: CodePropertyData) -> bool
        Set: IsHidden(self: CodePropertyData) = value
        """
        ...

    @property
    def SetCodeReference(self) -> MethodInfo:
        """
        Get: SetCodeReference(self: CodePropertyData) -> MethodInfo
        Set: SetCodeReference(self: CodePropertyData) = value
        """
        ...


    def __new__(cls, name:str, getMethod:MethodInfo, setMethod:MethodInfo = ...) -> Self:
        """
        __new__(cls: type, name: str, getMethod: MethodInfo)
        __new__(cls: type, name: str, getMethod: MethodInfo, setMethod: MethodInfo)
        """
        ...


class Command: # skipped bases: <type 'object'>, <type 'object'>
    """
    Command(command: str)
    Command(command: str, isScript: bool)
    Command(command: str, isScript: bool, useLocalScope: bool)
    """
    @property
    def CommandOrigin(self) -> CommandOrigin:
        """
        Get: CommandOrigin(self: Command) -> CommandOrigin
        Set: CommandOrigin(self: Command) = value
        """
        ...

    @property
    def CommandText(self) -> str:
        """ Get: CommandText(self: Command) -> str """
        ...

    @property
    def IsEndOfStatement(self) -> bool:
        """ Get: IsEndOfStatement(self: Command) -> bool """
        ...

    @property
    def IsScript(self) -> bool:
        """ Get: IsScript(self: Command) -> bool """
        ...

    @property
    def MergeUnclaimedPreviousCommandResults(self) -> PipelineResultTypes:
        """
        Get: MergeUnclaimedPreviousCommandResults(self: Command) -> PipelineResultTypes
        Set: MergeUnclaimedPreviousCommandResults(self: Command) = value
        """
        ...

    @property
    def Parameters(self) -> CommandParameterCollection:
        """ Get: Parameters(self: Command) -> CommandParameterCollection """
        ...

    @property
    def UseLocalScope(self) -> bool:
        """ Get: UseLocalScope(self: Command) -> bool """
        ...


    def MergeMyResults(self, myResult:PipelineResultTypes, toResult:PipelineResultTypes): # -> 
        """ MergeMyResults(self: Command, myResult: PipelineResultTypes, toResult: PipelineResultTypes) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Command) -> str """
        ...


class CommandCollection(Collection): # skipped bases: <type 'IReadOnlyList[Command]'>, <type 'IEnumerable'>, <type 'ICollection[Command]'>, <type 'IList'>, <type 'IReadOnlyCollection[Command]'>, <type 'IEnumerable[Command]'>, <type 'ICollection'>, <type 'IList[Command]'>, <type 'object'>
    """ no doc """
    def AddScript(self, scriptContents:str, useLocalScope:bool = ...): # -> 
        """ AddScript(self: CommandCollection, scriptContents: str, useLocalScope: bool)AddScript(self: CommandCollection, scriptContents: str) """
        ...


class CommandParameter: # skipped bases: <type 'object'>, <type 'object'>
    """
    CommandParameter(name: str)
    CommandParameter(name: str, value: object)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CommandParameter) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: CommandParameter) -> object """
        ...



class CommandParameterCollection(Collection): # skipped bases: <type 'ICollection[CommandParameter]'>, <type 'IReadOnlyCollection[CommandParameter]'>, <type 'IList[CommandParameter]'>, <type 'IEnumerable'>, <type 'IEnumerable[CommandParameter]'>, <type 'IList'>, <type 'IReadOnlyList[CommandParameter]'>, <type 'ICollection'>, <type 'object'>
    """ CommandParameterCollection() """
    pass

class InitialSessionStateEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: InitialSessionStateEntry) -> PSModuleInfo """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: InitialSessionStateEntry) -> str """
        ...

    @property
    def PSSnapIn(self) -> PSSnapInInfo:
        """ Get: PSSnapIn(self: InitialSessionStateEntry) -> PSSnapInInfo """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: InitialSessionStateEntry) -> InitialSessionStateEntry """
        ...


class ConstrainedSessionStateEntry(InitialSessionStateEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Visibility(self) -> SessionStateEntryVisibility:
        """
        Get: Visibility(self: ConstrainedSessionStateEntry) -> SessionStateEntryVisibility
        Set: Visibility(self: ConstrainedSessionStateEntry) = value
        """
        ...



class RunspaceConnectionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AuthenticationMechanism(self) -> AuthenticationMechanism:
        """
        Get: AuthenticationMechanism(self: RunspaceConnectionInfo) -> AuthenticationMechanism
        Set: AuthenticationMechanism(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def CancelTimeout(self) -> int:
        """
        Get: CancelTimeout(self: RunspaceConnectionInfo) -> int
        Set: CancelTimeout(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: RunspaceConnectionInfo) -> str
        Set: CertificateThumbprint(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: RunspaceConnectionInfo) -> str
        Set: ComputerName(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: RunspaceConnectionInfo) -> PSCredential
        Set: Credential(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: RunspaceConnectionInfo) -> CultureInfo
        Set: Culture(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def IdleTimeout(self) -> int:
        """
        Get: IdleTimeout(self: RunspaceConnectionInfo) -> int
        Set: IdleTimeout(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def MaxIdleTimeout(self) -> int:
        """ Get: MaxIdleTimeout(self: RunspaceConnectionInfo) -> int """
        ...

    @property
    def OpenTimeout(self) -> int:
        """
        Get: OpenTimeout(self: RunspaceConnectionInfo) -> int
        Set: OpenTimeout(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def OperationTimeout(self) -> int:
        """
        Get: OperationTimeout(self: RunspaceConnectionInfo) -> int
        Set: OperationTimeout(self: RunspaceConnectionInfo) = value
        """
        ...

    @property
    def UICulture(self) -> CultureInfo:
        """
        Get: UICulture(self: RunspaceConnectionInfo) -> CultureInfo
        Set: UICulture(self: RunspaceConnectionInfo) = value
        """
        ...


    def SetSessionOptions(self, options:PSSessionOption): # -> 
        """ SetSessionOptions(self: RunspaceConnectionInfo, options: PSSessionOption) """
        ...


class ContainerConnectionInfo(RunspaceConnectionInfo): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateContainerConnectionInfo(containerId:str, runAsAdmin:bool, configurationName:str) -> ContainerConnectionInfo:
        """ CreateContainerConnectionInfo(containerId: str, runAsAdmin: bool, configurationName: str) -> ContainerConnectionInfo """
        ...

    def CreateContainerProcess(self): # -> 
        """ CreateContainerProcess(self: ContainerConnectionInfo) """
        ...

    def TerminateContainerProcess(self) -> bool:
        """ TerminateContainerProcess(self: ContainerConnectionInfo) -> bool """
        ...


class FormatConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """
    FormatConfigurationEntry(name: str, fileName: str)
    FormatConfigurationEntry(fileName: str)
    FormatConfigurationEntry(typeDefinition: ExtendedTypeDefinition)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: FormatConfigurationEntry) -> str """
        ...

    @property
    def FormatData(self) -> ExtendedTypeDefinition:
        """ Get: FormatData(self: FormatConfigurationEntry) -> ExtendedTypeDefinition """
        ...



class FormatTable: # skipped bases: <type 'object'>, <type 'object'>
    """ FormatTable(formatFiles: IEnumerable[str]) """
    def AppendFormatData(self, formatData:IEnumerable): # -> 
        """ AppendFormatData(self: FormatTable, formatData: IEnumerable[ExtendedTypeDefinition]) """
        ...

    @staticmethod
    def LoadDefaultFormatFiles() -> FormatTable:
        """ LoadDefaultFormatFiles() -> FormatTable """
        ...

    def PrependFormatData(self, formatData:IEnumerable): # -> 
        """ PrependFormatData(self: FormatTable, formatData: IEnumerable[ExtendedTypeDefinition]) """
        ...


class FormatTableLoadException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FormatTableLoadException()
    FormatTableLoadException(message: str)
    FormatTableLoadException(message: str, innerException: Exception)
    """
    @property
    def Errors(self) -> Collection:
        """ Get: Errors(self: FormatTableLoadException) -> Collection[str] """
        ...


    def SetDefaultErrorRecord(self, *args): #cannot find CLR method
        """ SetDefaultErrorRecord(self: FormatTableLoadException) """
        ...

    SerializeObjectState = ...


class InitialSessionState: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApartmentState(self) -> ApartmentState:
        """
        Get: ApartmentState(self: InitialSessionState) -> ApartmentState
        Set: ApartmentState(self: InitialSessionState) = value
        """
        ...

    @property
    def Assemblies(self) -> InitialSessionStateEntryCollection:
        """ Get: Assemblies(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateAssemblyEntry] """
        ...

    @property
    def AuthorizationManager(self) -> AuthorizationManager:
        """
        Get: AuthorizationManager(self: InitialSessionState) -> AuthorizationManager
        Set: AuthorizationManager(self: InitialSessionState) = value
        """
        ...

    @property
    def Commands(self) -> InitialSessionStateEntryCollection:
        """ Get: Commands(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateCommandEntry] """
        ...

    @property
    def DisableFormatUpdates(self) -> bool:
        """
        Get: DisableFormatUpdates(self: InitialSessionState) -> bool
        Set: DisableFormatUpdates(self: InitialSessionState) = value
        """
        ...

    @property
    def EnvironmentVariables(self) -> InitialSessionStateEntryCollection:
        """ Get: EnvironmentVariables(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateVariableEntry] """
        ...

    @property
    def ExecutionPolicy(self) -> ExecutionPolicy:
        """
        Get: ExecutionPolicy(self: InitialSessionState) -> ExecutionPolicy
        Set: ExecutionPolicy(self: InitialSessionState) = value
        """
        ...

    @property
    def Formats(self) -> InitialSessionStateEntryCollection:
        """ Get: Formats(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateFormatEntry] """
        ...

    @property
    def LanguageMode(self) -> PSLanguageMode:
        """
        Get: LanguageMode(self: InitialSessionState) -> PSLanguageMode
        Set: LanguageMode(self: InitialSessionState) = value
        """
        ...

    @property
    def Modules(self) -> ReadOnlyCollection:
        """ Get: Modules(self: InitialSessionState) -> ReadOnlyCollection[ModuleSpecification] """
        ...

    @property
    def Providers(self) -> InitialSessionStateEntryCollection:
        """ Get: Providers(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateProviderEntry] """
        ...

    @property
    def StartupScripts(self) -> HashSet:
        """ Get: StartupScripts(self: InitialSessionState) -> HashSet[str] """
        ...

    @property
    def ThreadOptions(self) -> PSThreadOptions:
        """
        Get: ThreadOptions(self: InitialSessionState) -> PSThreadOptions
        Set: ThreadOptions(self: InitialSessionState) = value
        """
        ...

    @property
    def ThrowOnRunspaceOpenError(self) -> bool:
        """
        Get: ThrowOnRunspaceOpenError(self: InitialSessionState) -> bool
        Set: ThrowOnRunspaceOpenError(self: InitialSessionState) = value
        """
        ...

    @property
    def TranscriptDirectory(self) -> str:
        """
        Get: TranscriptDirectory(self: InitialSessionState) -> str
        Set: TranscriptDirectory(self: InitialSessionState) = value
        """
        ...

    @property
    def Types(self) -> InitialSessionStateEntryCollection:
        """ Get: Types(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateTypeEntry] """
        ...

    @property
    def UseFullLanguageModeInDebugger(self) -> bool:
        """
        Get: UseFullLanguageModeInDebugger(self: InitialSessionState) -> bool
        Set: UseFullLanguageModeInDebugger(self: InitialSessionState) = value
        """
        ...

    @property
    def Variables(self) -> InitialSessionStateEntryCollection:
        """ Get: Variables(self: InitialSessionState) -> InitialSessionStateEntryCollection[SessionStateVariableEntry] """
        ...


    def Clone(self) -> InitialSessionState:
        """ Clone(self: InitialSessionState) -> InitialSessionState """
        ...

    @staticmethod
    def Create(*__args) -> InitialSessionState:
        """
        Create() -> InitialSessionState
        Create(snapInName: str) -> InitialSessionState
        Create(snapInNameCollection: Array[str]) -> (InitialSessionState, PSConsoleLoadException)
        """
        ...

    @staticmethod
    def CreateDefault() -> InitialSessionState:
        """ CreateDefault() -> InitialSessionState """
        ...

    @staticmethod
    def CreateDefault2() -> InitialSessionState:
        """ CreateDefault2() -> InitialSessionState """
        ...

    @staticmethod
    def CreateFrom(*__args:str) -> Tuple_[InitialSessionState, PSConsoleLoadException]:
        """
        CreateFrom(snapInPath: str) -> (InitialSessionState, PSConsoleLoadException)
        CreateFrom(snapInPathCollection: Array[str]) -> (InitialSessionState, PSConsoleLoadException)
        """
        ...

    @staticmethod
    def CreateFromSessionConfigurationFile(path:str, roleVerifier = ...) -> InitialSessionState: # Not found arg types: {'roleVerifier': 'Func'}
        """
        CreateFromSessionConfigurationFile(path: str) -> InitialSessionState
        CreateFromSessionConfigurationFile(path: str, roleVerifier: Func[str, bool]) -> InitialSessionState
        """
        ...

    @staticmethod
    def CreateRestricted(sessionCapabilities:SessionCapabilities) -> InitialSessionState:
        """ CreateRestricted(sessionCapabilities: SessionCapabilities) -> InitialSessionState """
        ...

    def ImportPSModule(self, *__args:Array): # -> 
        """ ImportPSModule(self: InitialSessionState, name: Array[str])ImportPSModule(self: InitialSessionState, modules: IEnumerable[ModuleSpecification]) """
        ...

    def ImportPSModulesFromPath(self, path:str): # -> 
        """ ImportPSModulesFromPath(self: InitialSessionState, path: str) """
        ...

    def ImportPSSnapIn(self, name, warning) -> Tuple_[PSSnapInInfo, PSSnapInException]:
        """ ImportPSSnapIn(self: InitialSessionState, name: str) -> (PSSnapInInfo, PSSnapInException) """
        ...


class InitialSessionStateEntryCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    InitialSessionStateEntryCollection[T]()
    InitialSessionStateEntryCollection[T](items: IEnumerable[T])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: InitialSessionStateEntryCollection[T]) -> int """
        ...


    def Add(self, *__args): # ->  # Not found arg types: {'*__args': 'T'}
        """ Add(self: InitialSessionStateEntryCollection[T], item: T)Add(self: InitialSessionStateEntryCollection[T], items: IEnumerable[T]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: InitialSessionStateEntryCollection[T]) """
        ...

    def Clone(self) -> InitialSessionStateEntryCollection:
        """ Clone(self: InitialSessionStateEntryCollection[T]) -> InitialSessionStateEntryCollection[T] """
        ...

    def Remove(self, name:str, type:object): # -> 
        """ Remove(self: InitialSessionStateEntryCollection[T], name: str, type: object) """
        ...

    def RemoveItem(self, index:int, count:int = ...): # -> 
        """ RemoveItem(self: InitialSessionStateEntryCollection[T], index: int)RemoveItem(self: InitialSessionStateEntryCollection[T], index: int, count: int) """
        ...

    def Reset(self): # -> 
        """ Reset(self: InitialSessionStateEntryCollection[T]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class InvalidPipelineStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidPipelineStateException()
    InvalidPipelineStateException(message: str)
    InvalidPipelineStateException(message: str, innerException: Exception)
    """
    @property
    def CurrentState(self) -> PipelineState:
        """ Get: CurrentState(self: InvalidPipelineStateException) -> PipelineState """
        ...

    @property
    def ExpectedState(self) -> PipelineState:
        """ Get: ExpectedState(self: InvalidPipelineStateException) -> PipelineState """
        ...


    SerializeObjectState = ...


class InvalidRunspacePoolStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidRunspacePoolStateException()
    InvalidRunspacePoolStateException(message: str)
    InvalidRunspacePoolStateException(message: str, innerException: Exception)
    """
    @property
    def CurrentState(self) -> RunspacePoolState:
        """ Get: CurrentState(self: InvalidRunspacePoolStateException) -> RunspacePoolState """
        ...

    @property
    def ExpectedState(self) -> RunspacePoolState:
        """ Get: ExpectedState(self: InvalidRunspacePoolStateException) -> RunspacePoolState """
        ...


    SerializeObjectState = ...


class InvalidRunspaceStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidRunspaceStateException()
    InvalidRunspaceStateException(message: str)
    InvalidRunspaceStateException(message: str, innerException: Exception)
    """
    @property
    def CurrentState(self) -> RunspaceState:
        """ Get: CurrentState(self: InvalidRunspaceStateException) -> RunspaceState """
        ...

    @property
    def ExpectedState(self) -> RunspaceState:
        """ Get: ExpectedState(self: InvalidRunspaceStateException) -> RunspaceState """
        ...


    SerializeObjectState = ...


class MemberSetData(TypeMemberData): # skipped bases: <type 'object'>
    """ MemberSetData(name: str, members: Collection[TypeMemberData]) """
    @property
    def InheritMembers(self) -> bool:
        """
        Get: InheritMembers(self: MemberSetData) -> bool
        Set: InheritMembers(self: MemberSetData) = value
        """
        ...

    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: MemberSetData) -> bool
        Set: IsHidden(self: MemberSetData) = value
        """
        ...

    @property
    def Members(self) -> Collection:
        """ Get: Members(self: MemberSetData) -> Collection[TypeMemberData] """
        ...


    def __new__(cls, name:str, members:Collection) -> Self:
        """ __new__(cls: type, name: str, members: Collection[TypeMemberData]) """
        ...


class NamedPipeConnectionInfo(RunspaceConnectionInfo): # skipped bases: <type 'object'>
    """
    NamedPipeConnectionInfo()
    NamedPipeConnectionInfo(processId: int)
    NamedPipeConnectionInfo(processId: int, appDomainName: str)
    NamedPipeConnectionInfo(processId: int, appDomainName: str, openTimeout: int)
    """
    @property
    def AppDomainName(self) -> str:
        """
        Get: AppDomainName(self: NamedPipeConnectionInfo) -> str
        Set: AppDomainName(self: NamedPipeConnectionInfo) = value
        """
        ...

    @property
    def ProcessId(self) -> int:
        """
        Get: ProcessId(self: NamedPipeConnectionInfo) -> int
        Set: ProcessId(self: NamedPipeConnectionInfo) = value
        """
        ...


    def __new__(cls, processId:int = ..., appDomainName:str = ..., openTimeout:int = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, processId: int)
        __new__(cls: type, processId: int, appDomainName: str)
        __new__(cls: type, processId: int, appDomainName: str, openTimeout: int)
        """
        ...


class NotePropertyData(TypeMemberData): # skipped bases: <type 'object'>
    """ NotePropertyData(name: str, value: object) """
    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: NotePropertyData) -> bool
        Set: IsHidden(self: NotePropertyData) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: NotePropertyData) -> object
        Set: Value(self: NotePropertyData) = value
        """
        ...


    def __new__(cls, name:str, value:object) -> Self:
        """ __new__(cls: type, name: str, value: object) """
        ...


class OutputBufferingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OutputBufferingMode, values: Block (2), Drop (1), None (0) """
    Block: OutputBufferingMode = ...
    Drop: OutputBufferingMode = ...
    value__ = ...


class Pipeline(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Commands(self) -> CommandCollection:
        """ Get: Commands(self: Pipeline) -> CommandCollection """
        ...

    @property
    def Error(self) -> PipelineReader:
        """ Get: Error(self: Pipeline) -> PipelineReader[object] """
        ...

    @property
    def HadErrors(self) -> bool:
        """ Get: HadErrors(self: Pipeline) -> bool """
        ...

    @property
    def Input(self) -> PipelineWriter:
        """ Get: Input(self: Pipeline) -> PipelineWriter """
        ...

    @property
    def InstanceId(self) -> Int64:
        """ Get: InstanceId(self: Pipeline) -> Int64 """
        ...

    @property
    def IsNested(self) -> bool:
        """ Get: IsNested(self: Pipeline) -> bool """
        ...

    @property
    def Output(self) -> PipelineReader:
        """ Get: Output(self: Pipeline) -> PipelineReader[PSObject] """
        ...

    @property
    def PipelineStateInfo(self) -> PipelineStateInfo:
        """ Get: PipelineStateInfo(self: Pipeline) -> PipelineStateInfo """
        ...

    @property
    def Runspace(self) -> Runspace:
        """ Get: Runspace(self: Pipeline) -> Runspace """
        ...

    @property
    def SetPipelineSessionState(self) -> bool:
        """
        Get: SetPipelineSessionState(self: Pipeline) -> bool
        Set: SetPipelineSessionState(self: Pipeline) = value
        """
        ...


    def Connect(self) -> Collection:
        """ Connect(self: Pipeline) -> Collection[PSObject] """
        ...

    def ConnectAsync(self): # -> 
        """ ConnectAsync(self: Pipeline) """
        ...

    def Copy(self) -> Pipeline:
        """ Copy(self: Pipeline) -> Pipeline """
        ...

    def Invoke(self, input:IEnumerable = ...) -> Collection:
        """
        Invoke(self: Pipeline) -> Collection[PSObject]
        Invoke(self: Pipeline, input: IEnumerable) -> Collection[PSObject]
        """
        ...

    def InvokeAsync(self): # -> 
        """ InvokeAsync(self: Pipeline) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Pipeline) """
        ...

    def StopAsync(self): # -> 
        """ StopAsync(self: Pipeline) """
        ...

    StateChanged = ...


class PipelineReader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PipelineReader[T]) -> int """
        ...

    @property
    def EndOfPipeline(self) -> bool:
        """ Get: EndOfPipeline(self: PipelineReader[T]) -> bool """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: PipelineReader[T]) -> bool """
        ...

    @property
    def MaxCapacity(self) -> int:
        """ Get: MaxCapacity(self: PipelineReader[T]) -> int """
        ...

    @property
    def WaitHandle(self) -> WaitHandle:
        """ Get: WaitHandle(self: PipelineReader[T]) -> WaitHandle """
        ...


    def Close(self): # -> 
        """ Close(self: PipelineReader[T]) """
        ...

    def NonBlockingRead(self, maxRequested:int = ...) -> Collection:
        """
        NonBlockingRead(self: PipelineReader[T]) -> Collection[T]
        NonBlockingRead(self: PipelineReader[T], maxRequested: int) -> Collection[T]
        """
        ...

    def Peek(self): # -> T
        """ Peek(self: PipelineReader[T]) -> T """
        ...

    def Read(self, count:int = ...) -> Collection:
        """
        Read(self: PipelineReader[T], count: int) -> Collection[T]
        Read(self: PipelineReader[T]) -> T
        """
        ...

    def ReadToEnd(self) -> Collection:
        """ ReadToEnd(self: PipelineReader[T]) -> Collection[T] """
        ...

    DataReady = ...


class PipelineResultTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PipelineResultTypes, values: All (7), Debug (5), Error (2), Information (6), None (0), Null (8), Output (1), Verbose (4), Warning (3) """
    All: PipelineResultTypes = ...
    Debug: PipelineResultTypes = ...
    Error: PipelineResultTypes = ...
    Information: PipelineResultTypes = ...
    Null: PipelineResultTypes = ...
    Output: PipelineResultTypes = ...
    value__ = ...
    Verbose: PipelineResultTypes = ...
    Warning: PipelineResultTypes = ...


class PipelineState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PipelineState, values: Completed (4), Disconnected (6), Failed (5), NotStarted (0), Running (1), Stopped (3), Stopping (2) """
    Completed: PipelineState = ...
    Disconnected: PipelineState = ...
    Failed: PipelineState = ...
    NotStarted: PipelineState = ...
    Running: PipelineState = ...
    Stopped: PipelineState = ...
    Stopping: PipelineState = ...
    value__ = ...


class PipelineStateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PipelineStateInfo(self) -> PipelineStateInfo:
        """ Get: PipelineStateInfo(self: PipelineStateEventArgs) -> PipelineStateInfo """
        ...



class PipelineStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: PipelineStateInfo) -> Exception """
        ...

    @property
    def State(self) -> PipelineState:
        """ Get: State(self: PipelineStateInfo) -> PipelineState """
        ...



class PipelineWriter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PipelineWriter) -> int """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: PipelineWriter) -> bool """
        ...

    @property
    def MaxCapacity(self) -> int:
        """ Get: MaxCapacity(self: PipelineWriter) -> int """
        ...

    @property
    def WaitHandle(self) -> WaitHandle:
        """ Get: WaitHandle(self: PipelineWriter) -> WaitHandle """
        ...


    def Close(self): # -> 
        """ Close(self: PipelineWriter) """
        ...

    def Flush(self): # -> 
        """ Flush(self: PipelineWriter) """
        ...

    def Write(self, obj:object, enumerateCollection:bool = ...) -> int:
        """
        Write(self: PipelineWriter, obj: object) -> int
        Write(self: PipelineWriter, obj: object, enumerateCollection: bool) -> int
        """
        ...


class PowerShellProcessInstance(IDisposable): # skipped bases: <type 'object'>
    """
    PowerShellProcessInstance(powerShellVersion: Version, credential: PSCredential, initializationScript: ScriptBlock, useWow64: bool)
    PowerShellProcessInstance()
    """
    @property
    def HasExited(self) -> bool:
        """ Get: HasExited(self: PowerShellProcessInstance) -> bool """
        ...

    @property
    def Process(self) -> Process:
        """ Get: Process(self: PowerShellProcessInstance) -> Process """
        ...



class PropertySetData(TypeMemberData): # skipped bases: <type 'object'>
    """ PropertySetData(referencedProperties: IEnumerable[str]) """
    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: PropertySetData) -> bool
        Set: IsHidden(self: PropertySetData) = value
        """
        ...

    @property
    def ReferencedProperties(self) -> Collection:
        """ Get: ReferencedProperties(self: PropertySetData) -> Collection[str] """
        ...


    def __new__(cls, referencedProperties:IEnumerable) -> Self:
        """ __new__(cls: type, referencedProperties: IEnumerable[str]) """
        ...


class ProviderConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """ ProviderConfigurationEntry(name: str, implementingType: Type, helpFileName: str) """
    @property
    def HelpFileName(self) -> str:
        """ Get: HelpFileName(self: ProviderConfigurationEntry) -> str """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: ProviderConfigurationEntry) -> Type """
        ...



class PSConsoleLoadException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSConsoleLoadException()
    PSConsoleLoadException(message: str)
    PSConsoleLoadException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PSSession: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationPrivateData(self) -> PSPrimitiveDictionary:
        """ Get: ApplicationPrivateData(self: PSSession) -> PSPrimitiveDictionary """
        ...

    @property
    def Availability(self) -> RunspaceAvailability:
        """ Get: Availability(self: PSSession) -> RunspaceAvailability """
        ...

    @property
    def ComputerName(self) -> str:
        """ Get: ComputerName(self: PSSession) -> str """
        ...

    @property
    def ComputerType(self) -> TargetMachineType:
        """
        Get: ComputerType(self: PSSession) -> TargetMachineType
        Set: ComputerType(self: PSSession) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """ Get: ConfigurationName(self: PSSession) -> str """
        ...

    @property
    def ContainerId(self) -> str:
        """ Get: ContainerId(self: PSSession) -> str """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: PSSession) -> int """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: PSSession) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PSSession) -> str
        Set: Name(self: PSSession) = value
        """
        ...

    @property
    def Runspace(self) -> Runspace:
        """ Get: Runspace(self: PSSession) -> Runspace """
        ...

    @property
    def VMId(self) -> Nullable:
        """ Get: VMId(self: PSSession) -> Nullable[Guid] """
        ...

    @property
    def VMName(self) -> str:
        """ Get: VMName(self: PSSession) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: PSSession) -> str """
        ...


class PSSessionConfigurationAccessMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSSessionConfigurationAccessMode, values: Disabled (0), Local (1), Remote (2) """
    Disabled: PSSessionConfigurationAccessMode = ...
    Local: PSSessionConfigurationAccessMode = ...
    Remote: PSSessionConfigurationAccessMode = ...
    value__ = ...


class PSSessionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSSessionType, values: DefaultRemoteShell (0), Workflow (1) """
    DefaultRemoteShell: PSSessionType = ...
    value__ = ...
    Workflow: PSSessionType = ...


class PSSnapInException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSSnapInException()
    PSSnapInException(message: str)
    PSSnapInException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: PSSnapInException) -> str """
        ...


    SerializeObjectState = ...


class PSThreadOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSThreadOptions, values: Default (0), ReuseThread (2), UseCurrentThread (3), UseNewThread (1) """
    Default: PSThreadOptions = ...
    ReuseThread: PSThreadOptions = ...
    UseCurrentThread: PSThreadOptions = ...
    UseNewThread: PSThreadOptions = ...
    value__ = ...


class RemotingDebugRecord(DebugRecord): # skipped bases: <type 'object'>
    """ RemotingDebugRecord(message: str, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingDebugRecord) -> OriginInfo """
        ...



class RemotingErrorRecord(ErrorRecord): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ RemotingErrorRecord(errorRecord: ErrorRecord, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingErrorRecord) -> OriginInfo """
        ...



class RemotingInformationRecord(InformationRecord): # skipped bases: <type 'object'>
    """ RemotingInformationRecord(record: InformationRecord, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingInformationRecord) -> OriginInfo """
        ...



class RemotingProgressRecord(ProgressRecord): # skipped bases: <type 'object'>
    """ RemotingProgressRecord(progressRecord: ProgressRecord, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingProgressRecord) -> OriginInfo """
        ...



class RemotingVerboseRecord(VerboseRecord): # skipped bases: <type 'object'>
    """ RemotingVerboseRecord(message: str, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingVerboseRecord) -> OriginInfo """
        ...



class RemotingWarningRecord(WarningRecord): # skipped bases: <type 'object'>
    """ RemotingWarningRecord(message: str, originInfo: OriginInfo) """
    @property
    def OriginInfo(self) -> OriginInfo:
        """ Get: OriginInfo(self: RemotingWarningRecord) -> OriginInfo """
        ...



class Runspace(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApartmentState(self) -> ApartmentState:
        """
        Get: ApartmentState(self: Runspace) -> ApartmentState
        Set: ApartmentState(self: Runspace) = value
        """
        ...

    @property
    def CanUseDefaultRunspace(self) -> bool:
        """ Get: CanUseDefaultRunspace() -> bool """
        ...

    @property
    def ConnectionInfo(self) -> RunspaceConnectionInfo:
        """ Get: ConnectionInfo(self: Runspace) -> RunspaceConnectionInfo """
        ...

    @property
    def Debugger(self) -> Debugger:
        """ Get: Debugger(self: Runspace) -> Debugger """
        ...

    @property
    def DefaultRunspace(self) -> Runspace:
        """
        Get: DefaultRunspace() -> Runspace
        Set: DefaultRunspace() = value
        """
        ...

    @property
    def DisconnectedOn(self) -> Nullable:
        """ Get: DisconnectedOn(self: Runspace) -> Nullable[DateTime] """
        ...

    @property
    def Events(self) -> PSEventManager:
        """ Get: Events(self: Runspace) -> PSEventManager """
        ...

    @property
    def ExpiresOn(self) -> Nullable:
        """ Get: ExpiresOn(self: Runspace) -> Nullable[DateTime] """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Runspace) -> int """
        ...

    @property
    def InitialSessionState(self) -> InitialSessionState:
        """ Get: InitialSessionState(self: Runspace) -> InitialSessionState """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: Runspace) -> Guid """
        ...

    @property
    def JobManager(self) -> JobManager:
        """ Get: JobManager(self: Runspace) -> JobManager """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Runspace) -> str
        Set: Name(self: Runspace) = value
        """
        ...

    @property
    def OriginalConnectionInfo(self) -> RunspaceConnectionInfo:
        """ Get: OriginalConnectionInfo(self: Runspace) -> RunspaceConnectionInfo """
        ...

    @property
    def RunspaceAvailability(self) -> RunspaceAvailability:
        """ Get: RunspaceAvailability(self: Runspace) -> RunspaceAvailability """
        ...

    @property
    def RunspaceConfiguration(self) -> RunspaceConfiguration:
        """ Get: RunspaceConfiguration(self: Runspace) -> RunspaceConfiguration """
        ...

    @property
    def RunspaceIsRemote(self) -> bool:
        """ Get: RunspaceIsRemote(self: Runspace) -> bool """
        ...

    @property
    def RunspaceStateInfo(self) -> RunspaceStateInfo:
        """ Get: RunspaceStateInfo(self: Runspace) -> RunspaceStateInfo """
        ...

    @property
    def SessionStateProxy(self) -> SessionStateProxy:
        """ Get: SessionStateProxy(self: Runspace) -> SessionStateProxy """
        ...

    @property
    def ThreadOptions(self) -> PSThreadOptions:
        """
        Get: ThreadOptions(self: Runspace) -> PSThreadOptions
        Set: ThreadOptions(self: Runspace) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: Runspace) -> Version """
        ...


    def ClearBaseTransaction(self): # -> 
        """ ClearBaseTransaction(self: Runspace) """
        ...

    def Close(self): # -> 
        """ Close(self: Runspace) """
        ...

    def CloseAsync(self): # -> 
        """ CloseAsync(self: Runspace) """
        ...

    def Connect(self): # -> 
        """ Connect(self: Runspace) """
        ...

    def ConnectAsync(self): # -> 
        """ ConnectAsync(self: Runspace) """
        ...

    def CreateDisconnectedPipeline(self) -> Pipeline:
        """ CreateDisconnectedPipeline(self: Runspace) -> Pipeline """
        ...

    def CreateDisconnectedPowerShell(self) -> PowerShell:
        """ CreateDisconnectedPowerShell(self: Runspace) -> PowerShell """
        ...

    def CreateNestedPipeline(self, command:str = ..., addToHistory:bool = ...) -> Pipeline:
        """
        CreateNestedPipeline(self: Runspace) -> Pipeline
        CreateNestedPipeline(self: Runspace, command: str, addToHistory: bool) -> Pipeline
        """
        ...

    def CreatePipeline(self, command:str = ..., addToHistory:bool = ...) -> Pipeline:
        """
        CreatePipeline(self: Runspace) -> Pipeline
        CreatePipeline(self: Runspace, command: str) -> Pipeline
        CreatePipeline(self: Runspace, command: str, addToHistory: bool) -> Pipeline
        """
        ...

    def Disconnect(self): # -> 
        """ Disconnect(self: Runspace) """
        ...

    def DisconnectAsync(self): # -> 
        """ DisconnectAsync(self: Runspace) """
        ...

    def GetApplicationPrivateData(self) -> PSPrimitiveDictionary:
        """ GetApplicationPrivateData(self: Runspace) -> PSPrimitiveDictionary """
        ...

    def GetCapabilities(self) -> RunspaceCapability:
        """ GetCapabilities(self: Runspace) -> RunspaceCapability """
        ...

    @staticmethod
    def GetRunspace(connectionInfo:RunspaceConnectionInfo, sessionId:Guid, commandId:Nullable, host:PSHost, typeTable:TypeTable) -> Runspace:
        """ GetRunspace(connectionInfo: RunspaceConnectionInfo, sessionId: Guid, commandId: Nullable[Guid], host: PSHost, typeTable: TypeTable) -> Runspace """
        ...

    @staticmethod
    def GetRunspaces(connectionInfo:RunspaceConnectionInfo, host:PSHost = ..., typeTable:TypeTable = ...) -> Array:
        """
        GetRunspaces(connectionInfo: RunspaceConnectionInfo) -> Array[Runspace]
        GetRunspaces(connectionInfo: RunspaceConnectionInfo, host: PSHost) -> Array[Runspace]
        GetRunspaces(connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable) -> Array[Runspace]
        """
        ...

    def OnAvailabilityChanged(self, *args): #cannot find CLR method
        """ OnAvailabilityChanged(self: Runspace, e: RunspaceAvailabilityEventArgs) """
        ...

    def Open(self): # -> 
        """ Open(self: Runspace) """
        ...

    def OpenAsync(self): # -> 
        """ OpenAsync(self: Runspace) """
        ...

    def ResetRunspaceState(self): # -> 
        """ ResetRunspaceState(self: Runspace) """
        ...

    def SetBaseTransaction(self, transaction:CommittableTransaction, severity:RollbackSeverity = ...): # -> 
        """ SetBaseTransaction(self: Runspace, transaction: CommittableTransaction)SetBaseTransaction(self: Runspace, transaction: CommittableTransaction, severity: RollbackSeverity) """
        ...

    def UpdateRunspaceAvailability(self, *args): #cannot find CLR method
        """ UpdateRunspaceAvailability(self: Runspace, runspaceState: RunspaceState, raiseEvent: bool) """
        ...

    AvailabilityChanged = ...
    StateChanged = ...


class RunspaceAvailability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspaceAvailability, values: Available (1), AvailableForNestedCommand (2), Busy (3), None (0), RemoteDebug (4) """
    Available: RunspaceAvailability = ...
    AvailableForNestedCommand: RunspaceAvailability = ...
    Busy: RunspaceAvailability = ...
    RemoteDebug: RunspaceAvailability = ...
    value__ = ...


class RunspaceAvailabilityEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RunspaceAvailability(self) -> RunspaceAvailability:
        """ Get: RunspaceAvailability(self: RunspaceAvailabilityEventArgs) -> RunspaceAvailability """
        ...



class RunspaceCapability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspaceCapability, values: Default (0), NamedPipeTransport (2), SupportsDisconnect (1), VMSocketTransport (4) """
    Default: RunspaceCapability = ...
    NamedPipeTransport: RunspaceCapability = ...
    SupportsDisconnect: RunspaceCapability = ...
    value__ = ...
    VMSocketTransport: RunspaceCapability = ...


class RunspaceConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Assemblies(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Assemblies(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[AssemblyConfigurationEntry] """
        ...

    @property
    def AuthorizationManager(self) -> AuthorizationManager:
        """ Get: AuthorizationManager(self: RunspaceConfiguration) -> AuthorizationManager """
        ...

    @property
    def Cmdlets(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Cmdlets(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[CmdletConfigurationEntry] """
        ...

    @property
    def Formats(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Formats(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[FormatConfigurationEntry] """
        ...

    @property
    def InitializationScripts(self) -> RunspaceConfigurationEntryCollection:
        """ Get: InitializationScripts(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[ScriptConfigurationEntry] """
        ...

    @property
    def Providers(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Providers(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[ProviderConfigurationEntry] """
        ...

    @property
    def Scripts(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Scripts(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[ScriptConfigurationEntry] """
        ...

    @property
    def ShellId(self) -> str:
        """ Get: ShellId(self: RunspaceConfiguration) -> str """
        ...

    @property
    def Types(self) -> RunspaceConfigurationEntryCollection:
        """ Get: Types(self: RunspaceConfiguration) -> RunspaceConfigurationEntryCollection[TypeConfigurationEntry] """
        ...


    def AddPSSnapIn(self, name, warning) -> Tuple_[PSSnapInInfo, PSSnapInException]:
        """ AddPSSnapIn(self: RunspaceConfiguration, name: str) -> (PSSnapInInfo, PSSnapInException) """
        ...

    @staticmethod
    def Create(*__args:str) -> RunspaceConfiguration:
        """
        Create(assemblyName: str) -> RunspaceConfiguration
        Create(consoleFilePath: str) -> (RunspaceConfiguration, PSConsoleLoadException)
        Create() -> RunspaceConfiguration
        """
        ...

    def RemovePSSnapIn(self, name, warning) -> Tuple_[PSSnapInInfo, PSSnapInException]:
        """ RemovePSSnapIn(self: RunspaceConfiguration, name: str) -> (PSSnapInInfo, PSSnapInException) """
        ...


class RunspaceConfigurationAttributeException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RunspaceConfigurationAttributeException()
    RunspaceConfigurationAttributeException(message: str)
    RunspaceConfigurationAttributeException(message: str, innerException: Exception)
    """
    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: RunspaceConfigurationAttributeException) -> str """
        ...

    @property
    def Error(self) -> str:
        """ Get: Error(self: RunspaceConfigurationAttributeException) -> str """
        ...


    SerializeObjectState = ...


class RunspaceConfigurationEntryCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    RunspaceConfigurationEntryCollection[T]()
    RunspaceConfigurationEntryCollection[T](items: IEnumerable[T])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: RunspaceConfigurationEntryCollection[T]) -> int """
        ...


    def Append(self, *__args): # ->  # Not found arg types: {'*__args': 'T'}
        """ Append(self: RunspaceConfigurationEntryCollection[T], item: T)Append(self: RunspaceConfigurationEntryCollection[T], items: IEnumerable[T]) """
        ...

    def Prepend(self, *__args): # ->  # Not found arg types: {'*__args': 'T'}
        """ Prepend(self: RunspaceConfigurationEntryCollection[T], item: T)Prepend(self: RunspaceConfigurationEntryCollection[T], items: IEnumerable[T]) """
        ...

    def RemoveItem(self, index:int, count:int = ...): # -> 
        """ RemoveItem(self: RunspaceConfigurationEntryCollection[T], index: int)RemoveItem(self: RunspaceConfigurationEntryCollection[T], index: int, count: int) """
        ...

    def Reset(self): # -> 
        """ Reset(self: RunspaceConfigurationEntryCollection[T]) """
        ...

    def Update(self): # -> 
        """ Update(self: RunspaceConfigurationEntryCollection[T]) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RunspaceConfigurationTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RunspaceConfigurationTypeAttribute(runspaceConfigurationType: str) """
    @property
    def RunspaceConfigurationType(self) -> str:
        """ Get: RunspaceConfigurationType(self: RunspaceConfigurationTypeAttribute) -> str """
        ...


    def __new__(cls, runspaceConfigurationType:str) -> Self:
        """ __new__(cls: type, runspaceConfigurationType: str) """
        ...


class RunspaceConfigurationTypeException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RunspaceConfigurationTypeException()
    RunspaceConfigurationTypeException(message: str)
    RunspaceConfigurationTypeException(message: str, innerException: Exception)
    """
    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: RunspaceConfigurationTypeException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: RunspaceConfigurationTypeException) -> str """
        ...


    SerializeObjectState = ...


class RunspaceFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateOutOfProcessRunspace(typeTable:TypeTable, processInstance:PowerShellProcessInstance = ...) -> Runspace:
        """
        CreateOutOfProcessRunspace(typeTable: TypeTable) -> Runspace
        CreateOutOfProcessRunspace(typeTable: TypeTable, processInstance: PowerShellProcessInstance) -> Runspace
        """
        ...

    @staticmethod
    def CreateRunspace(*__args) -> Runspace:
        """
        CreateRunspace() -> Runspace
        CreateRunspace(host: PSHost) -> Runspace
        CreateRunspace(runspaceConfiguration: RunspaceConfiguration) -> Runspace
        CreateRunspace(host: PSHost, runspaceConfiguration: RunspaceConfiguration) -> Runspace
        CreateRunspace(initialSessionState: InitialSessionState) -> Runspace
        CreateRunspace(host: PSHost, initialSessionState: InitialSessionState) -> Runspace
        CreateRunspace(connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable) -> Runspace
        CreateRunspace(connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable, applicationArguments: PSPrimitiveDictionary) -> Runspace
        CreateRunspace(connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable, applicationArguments: PSPrimitiveDictionary, name: str) -> Runspace
        CreateRunspace(host: PSHost, connectionInfo: RunspaceConnectionInfo) -> Runspace
        CreateRunspace(connectionInfo: RunspaceConnectionInfo) -> Runspace
        """
        ...

    @staticmethod
    def CreateRunspacePool(*__args) -> RunspacePool:
        """
        CreateRunspacePool() -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int) -> RunspacePool
        CreateRunspacePool(initialSessionState: InitialSessionState) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, host: PSHost) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, initialSessionState: InitialSessionState, host: PSHost) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, connectionInfo: RunspaceConnectionInfo) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, connectionInfo: RunspaceConnectionInfo, host: PSHost) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable) -> RunspacePool
        CreateRunspacePool(minRunspaces: int, maxRunspaces: int, connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable, applicationArguments: PSPrimitiveDictionary) -> RunspacePool
        """
        ...

    __all__: list = ...


class RunspaceOpenModuleLoadException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RunspaceOpenModuleLoadException()
    RunspaceOpenModuleLoadException(message: str)
    RunspaceOpenModuleLoadException(message: str, innerException: Exception)
    """
    @property
    def ErrorRecords(self) -> PSDataCollection:
        """ Get: ErrorRecords(self: RunspaceOpenModuleLoadException) -> PSDataCollection[ErrorRecord] """
        ...


    SerializeObjectState = ...


class RunspacePool(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApartmentState(self) -> ApartmentState:
        """
        Get: ApartmentState(self: RunspacePool) -> ApartmentState
        Set: ApartmentState(self: RunspacePool) = value
        """
        ...

    @property
    def CleanupInterval(self) -> TimeSpan:
        """
        Get: CleanupInterval(self: RunspacePool) -> TimeSpan
        Set: CleanupInterval(self: RunspacePool) = value
        """
        ...

    @property
    def ConnectionInfo(self) -> RunspaceConnectionInfo:
        """ Get: ConnectionInfo(self: RunspacePool) -> RunspaceConnectionInfo """
        ...

    @property
    def InitialSessionState(self) -> InitialSessionState:
        """ Get: InitialSessionState(self: RunspacePool) -> InitialSessionState """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: RunspacePool) -> Guid """
        ...

    @property
    def IsDisposed(self) -> bool:
        """ Get: IsDisposed(self: RunspacePool) -> bool """
        ...

    @property
    def RunspacePoolAvailability(self) -> RunspacePoolAvailability:
        """ Get: RunspacePoolAvailability(self: RunspacePool) -> RunspacePoolAvailability """
        ...

    @property
    def RunspacePoolStateInfo(self) -> RunspacePoolStateInfo:
        """ Get: RunspacePoolStateInfo(self: RunspacePool) -> RunspacePoolStateInfo """
        ...

    @property
    def ThreadOptions(self) -> PSThreadOptions:
        """
        Get: ThreadOptions(self: RunspacePool) -> PSThreadOptions
        Set: ThreadOptions(self: RunspacePool) = value
        """
        ...


    def BeginClose(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginClose(self: RunspacePool, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginConnect(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginConnect(self: RunspacePool, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginDisconnect(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginDisconnect(self: RunspacePool, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginOpen(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginOpen(self: RunspacePool, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Close(self): # -> 
        """ Close(self: RunspacePool) """
        ...

    def Connect(self): # -> 
        """ Connect(self: RunspacePool) """
        ...

    def CreateDisconnectedPowerShells(self) -> Collection:
        """ CreateDisconnectedPowerShells(self: RunspacePool) -> Collection[PowerShell] """
        ...

    def Disconnect(self): # -> 
        """ Disconnect(self: RunspacePool) """
        ...

    def EndClose(self, asyncResult:IAsyncResult): # -> 
        """ EndClose(self: RunspacePool, asyncResult: IAsyncResult) """
        ...

    def EndConnect(self, asyncResult:IAsyncResult): # -> 
        """ EndConnect(self: RunspacePool, asyncResult: IAsyncResult) """
        ...

    def EndDisconnect(self, asyncResult:IAsyncResult): # -> 
        """ EndDisconnect(self: RunspacePool, asyncResult: IAsyncResult) """
        ...

    def EndOpen(self, asyncResult:IAsyncResult): # -> 
        """ EndOpen(self: RunspacePool, asyncResult: IAsyncResult) """
        ...

    def GetApplicationPrivateData(self) -> PSPrimitiveDictionary:
        """ GetApplicationPrivateData(self: RunspacePool) -> PSPrimitiveDictionary """
        ...

    def GetAvailableRunspaces(self) -> int:
        """ GetAvailableRunspaces(self: RunspacePool) -> int """
        ...

    def GetCapabilities(self) -> RunspacePoolCapability:
        """ GetCapabilities(self: RunspacePool) -> RunspacePoolCapability """
        ...

    def GetMaxRunspaces(self) -> int:
        """ GetMaxRunspaces(self: RunspacePool) -> int """
        ...

    def GetMinRunspaces(self) -> int:
        """ GetMinRunspaces(self: RunspacePool) -> int """
        ...

    @staticmethod
    def GetRunspacePools(connectionInfo:RunspaceConnectionInfo, host:PSHost = ..., typeTable:TypeTable = ...) -> Array:
        """
        GetRunspacePools(connectionInfo: RunspaceConnectionInfo) -> Array[RunspacePool]
        GetRunspacePools(connectionInfo: RunspaceConnectionInfo, host: PSHost) -> Array[RunspacePool]
        GetRunspacePools(connectionInfo: RunspaceConnectionInfo, host: PSHost, typeTable: TypeTable) -> Array[RunspacePool]
        """
        ...

    def Open(self): # -> 
        """ Open(self: RunspacePool) """
        ...

    def SetMaxRunspaces(self, maxRunspaces:int) -> bool:
        """ SetMaxRunspaces(self: RunspacePool, maxRunspaces: int) -> bool """
        ...

    def SetMinRunspaces(self, minRunspaces:int) -> bool:
        """ SetMinRunspaces(self: RunspacePool, minRunspaces: int) -> bool """
        ...

    StateChanged = ...


class RunspacePoolAvailability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspacePoolAvailability, values: Available (1), Busy (2), None (0) """
    Available: RunspacePoolAvailability = ...
    Busy: RunspacePoolAvailability = ...
    value__ = ...


class RunspacePoolCapability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspacePoolCapability, values: Default (0), SupportsDisconnect (1) """
    Default: RunspacePoolCapability = ...
    SupportsDisconnect: RunspacePoolCapability = ...
    value__ = ...


class RunspacePoolState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspacePoolState, values: BeforeOpen (0), Broken (5), Closed (3), Closing (4), Connecting (8), Disconnected (7), Disconnecting (6), Opened (2), Opening (1) """
    BeforeOpen: RunspacePoolState = ...
    Broken: RunspacePoolState = ...
    Closed: RunspacePoolState = ...
    Closing: RunspacePoolState = ...
    Connecting: RunspacePoolState = ...
    Disconnected: RunspacePoolState = ...
    Disconnecting: RunspacePoolState = ...
    Opened: RunspacePoolState = ...
    Opening: RunspacePoolState = ...
    value__ = ...


class RunspacePoolStateChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RunspacePoolStateInfo(self) -> RunspacePoolStateInfo:
        """ Get: RunspacePoolStateInfo(self: RunspacePoolStateChangedEventArgs) -> RunspacePoolStateInfo """
        ...



class RunspaceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspaceState, values: BeforeOpen (0), Broken (5), Closed (3), Closing (4), Connecting (8), Disconnected (7), Disconnecting (6), Opened (2), Opening (1) """
    BeforeOpen: RunspaceState = ...
    Broken: RunspaceState = ...
    Closed: RunspaceState = ...
    Closing: RunspaceState = ...
    Connecting: RunspaceState = ...
    Disconnected: RunspaceState = ...
    Disconnecting: RunspaceState = ...
    Opened: RunspaceState = ...
    Opening: RunspaceState = ...
    value__ = ...


class RunspaceStateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RunspaceStateInfo(self) -> RunspaceStateInfo:
        """ Get: RunspaceStateInfo(self: RunspaceStateEventArgs) -> RunspaceStateInfo """
        ...



class RunspaceStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: RunspaceStateInfo) -> Exception """
        ...

    @property
    def State(self) -> RunspaceState:
        """ Get: State(self: RunspaceStateInfo) -> RunspaceState """
        ...


    def ToString(self) -> str:
        """ ToString(self: RunspaceStateInfo) -> str """
        ...


class ScriptConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """ ScriptConfigurationEntry(name: str, definition: str) """
    @property
    def Definition(self) -> str:
        """ Get: Definition(self: ScriptConfigurationEntry) -> str """
        ...



class ScriptMethodData(TypeMemberData): # skipped bases: <type 'object'>
    """ ScriptMethodData(name: str, scriptToInvoke: ScriptBlock) """
    @property
    def Script(self) -> ScriptBlock:
        """
        Get: Script(self: ScriptMethodData) -> ScriptBlock
        Set: Script(self: ScriptMethodData) = value
        """
        ...


    def __new__(cls, name:str, scriptToInvoke:ScriptBlock) -> Self:
        """ __new__(cls: type, name: str, scriptToInvoke: ScriptBlock) """
        ...


class ScriptPropertyData(TypeMemberData): # skipped bases: <type 'object'>
    """
    ScriptPropertyData(name: str, getScriptBlock: ScriptBlock)
    ScriptPropertyData(name: str, getScriptBlock: ScriptBlock, setScriptBlock: ScriptBlock)
    """
    @property
    def GetScriptBlock(self) -> ScriptBlock:
        """
        Get: GetScriptBlock(self: ScriptPropertyData) -> ScriptBlock
        Set: GetScriptBlock(self: ScriptPropertyData) = value
        """
        ...

    @property
    def IsHidden(self) -> bool:
        """
        Get: IsHidden(self: ScriptPropertyData) -> bool
        Set: IsHidden(self: ScriptPropertyData) = value
        """
        ...

    @property
    def SetScriptBlock(self) -> ScriptBlock:
        """
        Get: SetScriptBlock(self: ScriptPropertyData) -> ScriptBlock
        Set: SetScriptBlock(self: ScriptPropertyData) = value
        """
        ...


    def __new__(cls, name:str, getScriptBlock:ScriptBlock, setScriptBlock:ScriptBlock = ...) -> Self:
        """
        __new__(cls: type, name: str, getScriptBlock: ScriptBlock)
        __new__(cls: type, name: str, getScriptBlock: ScriptBlock, setScriptBlock: ScriptBlock)
        """
        ...


class SessionStateCommandEntry(ConstrainedSessionStateEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandType(self) -> CommandTypes:
        """ Get: CommandType(self: SessionStateCommandEntry) -> CommandTypes """
        ...



class SessionStateAliasEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """
    SessionStateAliasEntry(name: str, definition: str)
    SessionStateAliasEntry(name: str, definition: str, description: str)
    SessionStateAliasEntry(name: str, definition: str, description: str, options: ScopedItemOptions)
    """
    @property
    def Definition(self) -> str:
        """ Get: Definition(self: SessionStateAliasEntry) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: SessionStateAliasEntry) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """ Get: Options(self: SessionStateAliasEntry) -> ScopedItemOptions """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateAliasEntry) -> InitialSessionStateEntry """
        ...


class SessionStateApplicationEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """ SessionStateApplicationEntry(path: str) """
    @property
    def Path(self) -> str:
        """ Get: Path(self: SessionStateApplicationEntry) -> str """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateApplicationEntry) -> InitialSessionStateEntry """
        ...


class SessionStateAssemblyEntry(InitialSessionStateEntry): # skipped bases: <type 'object'>
    """
    SessionStateAssemblyEntry(name: str, fileName: str)
    SessionStateAssemblyEntry(name: str)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SessionStateAssemblyEntry) -> str """
        ...



class SessionStateCmdletEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """ SessionStateCmdletEntry(name: str, implementingType: Type, helpFileName: str) """
    @property
    def HelpFileName(self) -> str:
        """ Get: HelpFileName(self: SessionStateCmdletEntry) -> str """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: SessionStateCmdletEntry) -> Type """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateCmdletEntry) -> InitialSessionStateEntry """
        ...


class SessionStateFormatEntry(InitialSessionStateEntry): # skipped bases: <type 'object'>
    """
    SessionStateFormatEntry(fileName: str)
    SessionStateFormatEntry(formattable: FormatTable)
    SessionStateFormatEntry(typeDefinition: ExtendedTypeDefinition)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SessionStateFormatEntry) -> str """
        ...

    @property
    def FormatData(self) -> ExtendedTypeDefinition:
        """ Get: FormatData(self: SessionStateFormatEntry) -> ExtendedTypeDefinition """
        ...

    @property
    def Formattable(self) -> FormatTable:
        """ Get: Formattable(self: SessionStateFormatEntry) -> FormatTable """
        ...



class SessionStateFunctionEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """
    SessionStateFunctionEntry(name: str, definition: str, options: ScopedItemOptions, helpFile: str)
    SessionStateFunctionEntry(name: str, definition: str, helpFile: str)
    SessionStateFunctionEntry(name: str, definition: str)
    """
    @property
    def Definition(self) -> str:
        """ Get: Definition(self: SessionStateFunctionEntry) -> str """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: SessionStateFunctionEntry) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """ Get: Options(self: SessionStateFunctionEntry) -> ScopedItemOptions """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateFunctionEntry) -> InitialSessionStateEntry """
        ...


class SessionStateProviderEntry(ConstrainedSessionStateEntry): # skipped bases: <type 'object'>
    """ SessionStateProviderEntry(name: str, implementingType: Type, helpFileName: str) """
    @property
    def HelpFileName(self) -> str:
        """ Get: HelpFileName(self: SessionStateProviderEntry) -> str """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: SessionStateProviderEntry) -> Type """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateProviderEntry) -> InitialSessionStateEntry """
        ...


class SessionStateProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Applications(self) -> List:
        """ Get: Applications(self: SessionStateProxy) -> List[str] """
        ...

    @property
    def Drive(self) -> DriveManagementIntrinsics:
        """ Get: Drive(self: SessionStateProxy) -> DriveManagementIntrinsics """
        ...

    @property
    def InvokeCommand(self) -> CommandInvocationIntrinsics:
        """ Get: InvokeCommand(self: SessionStateProxy) -> CommandInvocationIntrinsics """
        ...

    @property
    def InvokeProvider(self) -> ProviderIntrinsics:
        """ Get: InvokeProvider(self: SessionStateProxy) -> ProviderIntrinsics """
        ...

    @property
    def LanguageMode(self) -> PSLanguageMode:
        """
        Get: LanguageMode(self: SessionStateProxy) -> PSLanguageMode
        Set: LanguageMode(self: SessionStateProxy) = value
        """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: SessionStateProxy) -> PSModuleInfo """
        ...

    @property
    def Path(self) -> PathIntrinsics:
        """ Get: Path(self: SessionStateProxy) -> PathIntrinsics """
        ...

    @property
    def Provider(self) -> CmdletProviderManagementIntrinsics:
        """ Get: Provider(self: SessionStateProxy) -> CmdletProviderManagementIntrinsics """
        ...

    @property
    def PSVariable(self) -> PSVariableIntrinsics:
        """ Get: PSVariable(self: SessionStateProxy) -> PSVariableIntrinsics """
        ...

    @property
    def Scripts(self) -> List:
        """ Get: Scripts(self: SessionStateProxy) -> List[str] """
        ...


    def GetVariable(self, name:str) -> object:
        """ GetVariable(self: SessionStateProxy, name: str) -> object """
        ...

    def SetVariable(self, name:str, value:object): # -> 
        """ SetVariable(self: SessionStateProxy, name: str, value: object) """
        ...


class SessionStateScriptEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """ SessionStateScriptEntry(path: str) """
    @property
    def Path(self) -> str:
        """ Get: Path(self: SessionStateScriptEntry) -> str """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateScriptEntry) -> InitialSessionStateEntry """
        ...


class SessionStateTypeEntry(InitialSessionStateEntry): # skipped bases: <type 'object'>
    """
    SessionStateTypeEntry(fileName: str)
    SessionStateTypeEntry(typeTable: TypeTable)
    SessionStateTypeEntry(typeData: TypeData, isRemove: bool)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SessionStateTypeEntry) -> str """
        ...

    @property
    def IsRemove(self) -> bool:
        """ Get: IsRemove(self: SessionStateTypeEntry) -> bool """
        ...

    @property
    def TypeData(self) -> TypeData:
        """ Get: TypeData(self: SessionStateTypeEntry) -> TypeData """
        ...

    @property
    def TypeTable(self) -> TypeTable:
        """ Get: TypeTable(self: SessionStateTypeEntry) -> TypeTable """
        ...



class SessionStateVariableEntry(ConstrainedSessionStateEntry): # skipped bases: <type 'object'>
    """
    SessionStateVariableEntry(name: str, value: object, description: str)
    SessionStateVariableEntry(name: str, value: object, description: str, options: ScopedItemOptions)
    SessionStateVariableEntry(name: str, value: object, description: str, options: ScopedItemOptions, attributes: Collection[Attribute])
    SessionStateVariableEntry(name: str, value: object, description: str, options: ScopedItemOptions, attribute: Attribute)
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: SessionStateVariableEntry) -> Collection[Attribute] """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: SessionStateVariableEntry) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """ Get: Options(self: SessionStateVariableEntry) -> ScopedItemOptions """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SessionStateVariableEntry) -> object """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateVariableEntry) -> InitialSessionStateEntry """
        ...


class SessionStateWorkflowEntry(SessionStateCommandEntry): # skipped bases: <type 'object'>
    """
    SessionStateWorkflowEntry(name: str, definition: str, options: ScopedItemOptions, helpFile: str)
    SessionStateWorkflowEntry(name: str, definition: str, helpFile: str)
    SessionStateWorkflowEntry(name: str, definition: str)
    """
    @property
    def Definition(self) -> str:
        """ Get: Definition(self: SessionStateWorkflowEntry) -> str """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: SessionStateWorkflowEntry) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """ Get: Options(self: SessionStateWorkflowEntry) -> ScopedItemOptions """
        ...


    def Clone(self) -> InitialSessionStateEntry:
        """ Clone(self: SessionStateWorkflowEntry) -> InitialSessionStateEntry """
        ...


class TargetMachineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TargetMachineType, values: Container (2), RemoteMachine (0), VirtualMachine (1) """
    Container: TargetMachineType = ...
    RemoteMachine: TargetMachineType = ...
    value__ = ...
    VirtualMachine: TargetMachineType = ...


class TypeConfigurationEntry(RunspaceConfigurationEntry): # skipped bases: <type 'object'>
    """
    TypeConfigurationEntry(name: str, fileName: str)
    TypeConfigurationEntry(typeData: TypeData, isRemove: bool)
    TypeConfigurationEntry(fileName: str)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: TypeConfigurationEntry) -> str """
        ...

    @property
    def IsRemove(self) -> bool:
        """ Get: IsRemove(self: TypeConfigurationEntry) -> bool """
        ...

    @property
    def TypeData(self) -> TypeData:
        """ Get: TypeData(self: TypeConfigurationEntry) -> TypeData """
        ...



class TypeData: # skipped bases: <type 'object'>, <type 'object'>
    """
    TypeData(typeName: str)
    TypeData(type: Type)
    """
    @property
    def DefaultDisplayProperty(self) -> str:
        """
        Get: DefaultDisplayProperty(self: TypeData) -> str
        Set: DefaultDisplayProperty(self: TypeData) = value
        """
        ...

    @property
    def DefaultDisplayPropertySet(self) -> PropertySetData:
        """
        Get: DefaultDisplayPropertySet(self: TypeData) -> PropertySetData
        Set: DefaultDisplayPropertySet(self: TypeData) = value
        """
        ...

    @property
    def DefaultKeyPropertySet(self) -> PropertySetData:
        """
        Get: DefaultKeyPropertySet(self: TypeData) -> PropertySetData
        Set: DefaultKeyPropertySet(self: TypeData) = value
        """
        ...

    @property
    def InheritPropertySerializationSet(self) -> bool:
        """
        Get: InheritPropertySerializationSet(self: TypeData) -> bool
        Set: InheritPropertySerializationSet(self: TypeData) = value
        """
        ...

    @property
    def IsOverride(self) -> bool:
        """
        Get: IsOverride(self: TypeData) -> bool
        Set: IsOverride(self: TypeData) = value
        """
        ...

    @property
    def Members(self) -> Dictionary:
        """ Get: Members(self: TypeData) -> Dictionary[str, TypeMemberData] """
        ...

    @property
    def PropertySerializationSet(self) -> PropertySetData:
        """
        Get: PropertySerializationSet(self: TypeData) -> PropertySetData
        Set: PropertySerializationSet(self: TypeData) = value
        """
        ...

    @property
    def SerializationDepth(self) -> UInt32:
        """
        Get: SerializationDepth(self: TypeData) -> UInt32
        Set: SerializationDepth(self: TypeData) = value
        """
        ...

    @property
    def SerializationMethod(self) -> str:
        """
        Get: SerializationMethod(self: TypeData) -> str
        Set: SerializationMethod(self: TypeData) = value
        """
        ...

    @property
    def StringSerializationSource(self) -> str:
        """
        Get: StringSerializationSource(self: TypeData) -> str
        Set: StringSerializationSource(self: TypeData) = value
        """
        ...

    @property
    def StringSerializationSourceProperty(self) -> TypeMemberData:
        """
        Get: StringSerializationSourceProperty(self: TypeData) -> TypeMemberData
        Set: StringSerializationSourceProperty(self: TypeData) = value
        """
        ...

    @property
    def TargetTypeForDeserialization(self) -> Type:
        """
        Get: TargetTypeForDeserialization(self: TypeData) -> Type
        Set: TargetTypeForDeserialization(self: TypeData) = value
        """
        ...

    @property
    def TypeAdapter(self) -> Type:
        """
        Get: TypeAdapter(self: TypeData) -> Type
        Set: TypeAdapter(self: TypeData) = value
        """
        ...

    @property
    def TypeConverter(self) -> Type:
        """
        Get: TypeConverter(self: TypeData) -> Type
        Set: TypeConverter(self: TypeData) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: TypeData) -> str """
        ...


    def Copy(self) -> TypeData:
        """ Copy(self: TypeData) -> TypeData """
        ...


class TypeTable: # skipped bases: <type 'object'>, <type 'object'>
    """ TypeTable(typeFiles: IEnumerable[str]) """
    def AddType(self, typeData:TypeData): # -> 
        """ AddType(self: TypeTable, typeData: TypeData) """
        ...

    def Clone(self, unshared:bool) -> TypeTable:
        """ Clone(self: TypeTable, unshared: bool) -> TypeTable """
        ...

    @staticmethod
    def GetDefaultTypeFiles() -> List:
        """ GetDefaultTypeFiles() -> List[str] """
        ...

    @staticmethod
    def LoadDefaultTypeFiles() -> TypeTable:
        """ LoadDefaultTypeFiles() -> TypeTable """
        ...

    def RemoveType(self, typeName:str): # -> 
        """ RemoveType(self: TypeTable, typeName: str) """
        ...


class TypeTableLoadException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TypeTableLoadException()
    TypeTableLoadException(message: str)
    TypeTableLoadException(message: str, innerException: Exception)
    """
    @property
    def Errors(self) -> Collection:
        """ Get: Errors(self: TypeTableLoadException) -> Collection[str] """
        ...


    def SetDefaultErrorRecord(self, *args): #cannot find CLR method
        """ SetDefaultErrorRecord(self: TypeTableLoadException) """
        ...

    SerializeObjectState = ...


class VMConnectionInfo(RunspaceConnectionInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: VMConnectionInfo) -> str
        Set: ConfigurationName(self: VMConnectionInfo) = value
        """
        ...

    @property
    def VMGuid(self) -> Guid:
        """
        Get: VMGuid(self: VMConnectionInfo) -> Guid
        Set: VMGuid(self: VMConnectionInfo) = value
        """
        ...



class WSManConnectionInfo(RunspaceConnectionInfo): # skipped bases: <type 'object'>
    """
    WSManConnectionInfo(scheme: str, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential, openTimeout: int)
    WSManConnectionInfo(scheme: str, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential)
    WSManConnectionInfo(useSsl: bool, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential)
    WSManConnectionInfo(useSsl: bool, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential, openTimeout: int)
    WSManConnectionInfo()
    WSManConnectionInfo(uri: Uri, shellUri: str, credential: PSCredential)
    WSManConnectionInfo(uri: Uri, shellUri: str, certificateThumbprint: str)
    WSManConnectionInfo(uri: Uri)
    WSManConnectionInfo(configurationType: PSSessionType)
    """
    @property
    def AppName(self) -> str:
        """
        Get: AppName(self: WSManConnectionInfo) -> str
        Set: AppName(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Uri:
        """
        Get: ConnectionUri(self: WSManConnectionInfo) -> Uri
        Set: ConnectionUri(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def EnableNetworkAccess(self) -> bool:
        """
        Get: EnableNetworkAccess(self: WSManConnectionInfo) -> bool
        Set: EnableNetworkAccess(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def IncludePortInSPN(self) -> bool:
        """
        Get: IncludePortInSPN(self: WSManConnectionInfo) -> bool
        Set: IncludePortInSPN(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def MaxConnectionRetryCount(self) -> int:
        """
        Get: MaxConnectionRetryCount(self: WSManConnectionInfo) -> int
        Set: MaxConnectionRetryCount(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def MaximumConnectionRedirectionCount(self) -> int:
        """
        Get: MaximumConnectionRedirectionCount(self: WSManConnectionInfo) -> int
        Set: MaximumConnectionRedirectionCount(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def MaximumReceivedDataSizePerCommand(self) -> Nullable:
        """
        Get: MaximumReceivedDataSizePerCommand(self: WSManConnectionInfo) -> Nullable[int]
        Set: MaximumReceivedDataSizePerCommand(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def MaximumReceivedObjectSize(self) -> Nullable:
        """
        Get: MaximumReceivedObjectSize(self: WSManConnectionInfo) -> Nullable[int]
        Set: MaximumReceivedObjectSize(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def NoEncryption(self) -> bool:
        """
        Get: NoEncryption(self: WSManConnectionInfo) -> bool
        Set: NoEncryption(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def NoMachineProfile(self) -> bool:
        """
        Get: NoMachineProfile(self: WSManConnectionInfo) -> bool
        Set: NoMachineProfile(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def OutputBufferingMode(self) -> OutputBufferingMode:
        """
        Get: OutputBufferingMode(self: WSManConnectionInfo) -> OutputBufferingMode
        Set: OutputBufferingMode(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: WSManConnectionInfo) -> int
        Set: Port(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def ProxyAccessType(self) -> ProxyAccessType:
        """
        Get: ProxyAccessType(self: WSManConnectionInfo) -> ProxyAccessType
        Set: ProxyAccessType(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def ProxyAuthentication(self) -> AuthenticationMechanism:
        """
        Get: ProxyAuthentication(self: WSManConnectionInfo) -> AuthenticationMechanism
        Set: ProxyAuthentication(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def ProxyCredential(self) -> PSCredential:
        """
        Get: ProxyCredential(self: WSManConnectionInfo) -> PSCredential
        Set: ProxyCredential(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: WSManConnectionInfo) -> str
        Set: Scheme(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def ShellUri(self) -> str:
        """
        Get: ShellUri(self: WSManConnectionInfo) -> str
        Set: ShellUri(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def SkipCACheck(self) -> bool:
        """
        Get: SkipCACheck(self: WSManConnectionInfo) -> bool
        Set: SkipCACheck(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def SkipCNCheck(self) -> bool:
        """
        Get: SkipCNCheck(self: WSManConnectionInfo) -> bool
        Set: SkipCNCheck(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def SkipRevocationCheck(self) -> bool:
        """
        Get: SkipRevocationCheck(self: WSManConnectionInfo) -> bool
        Set: SkipRevocationCheck(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def UseCompression(self) -> bool:
        """
        Get: UseCompression(self: WSManConnectionInfo) -> bool
        Set: UseCompression(self: WSManConnectionInfo) = value
        """
        ...

    @property
    def UseUTF16(self) -> bool:
        """
        Get: UseUTF16(self: WSManConnectionInfo) -> bool
        Set: UseUTF16(self: WSManConnectionInfo) = value
        """
        ...


    def Copy(self) -> WSManConnectionInfo:
        """ Copy(self: WSManConnectionInfo) -> WSManConnectionInfo """
        ...

    def __new__(cls, *__args:Uri) -> Self:
        """
        __new__(cls: type, scheme: str, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential, openTimeout: int)
        __new__(cls: type, scheme: str, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential)
        __new__(cls: type, useSsl: bool, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential)
        __new__(cls: type, useSsl: bool, computerName: str, port: int, appName: str, shellUri: str, credential: PSCredential, openTimeout: int)
        __new__(cls: type)
        __new__(cls: type, uri: Uri, shellUri: str, credential: PSCredential)
        __new__(cls: type, uri: Uri, shellUri: str, certificateThumbprint: str)
        __new__(cls: type, uri: Uri)
        __new__(cls: type, configurationType: PSSessionType)
        """
        ...

    HttpScheme: str = ...
    HttpsScheme: str = ...


