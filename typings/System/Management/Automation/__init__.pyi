# encoding: utf-8
# module System.Management.Automation calls itself Automation
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.ManagementConsole.Internal import Command

from Microsoft.VisualBasic import Collection

from System import (ArgumentException, ArgumentNullException, 
    ArgumentOutOfRangeException, Array, AsyncCallback, Attribute, DateTime, 
    Enum, EventArgs, EventHandler, Guid, IAsyncResult, ICloneable, 
    IComparable, IDisposable, IEquatable, IFormatProvider, IFormattable, 
    Int64, InvalidCastException, InvalidOperationException, MulticastDelegate, 
    NotImplementedException, NotSupportedException, Nullable, 
    ObjectDisposedException, SystemException, Type, UInt32, UInt64, Uri, 
    Version)

from System.Collections import (Hashtable, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList, Stack)

from System.Collections.Generic import Dictionary, HashSet, List

from System.Collections.ObjectModel import (ReadOnlyCollection, 
    ReadOnlyDictionary)

from System.Collections.Specialized import StringDictionary

from System.ComponentModel import (AttributeCollection, CustomTypeDescriptor, 
    PropertyDescriptor, TypeDescriptionProvider)

from System.Configuration.Install import Installer

from System.Diagnostics import SourceSwitch, TraceListenerCollection

from System.Dynamic import IDynamicMetaObjectProvider

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Management.Automation.Host import PSHost

from System.Management.Automation.Internal import (CmdletMetadataAttribute, 
    InternalCommand, ParsingBaseAttribute)

from System.Management.Automation.Language import (Ast, CommandAst, 
    IScriptExtent, ScriptExtent, Token, TypeDefinitionAst)

from System.Management.Automation.Provider import ProviderCapabilities

from System.Management.Automation.Runspaces import (CommandCollection, 
    Runspace, RunspacePool, RunspacePoolState)

from System.Net import NetworkCredential

from System.Reflection import Assembly, MethodInfo, ProcessorArchitecture

from System.Runtime.Serialization import (ISerializable, SerializationInfo, 
    StreamingContext)

from System.Security import SecureString

from System.Security.AccessControl import (AccessControlSections, 
    ObjectSecurity)

from System.Security.Cryptography.X509Certificates import (X509Certificate2, 
    X509Certificate2Collection)

from System.Text import Encoding

from System.Text.RegularExpressions import RegexOptions

from System.Threading import ApartmentState, WaitCallback, WaitHandle

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IHasSessionStateEntryVisibility, IScriptCommandInfo, T, 
    Tuple, IScriptPosition], field#)
"""

# no functions
# classes

class ActionPreference(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActionPreference, values: Continue (2), Ignore (4), Inquire (3), SilentlyContinue (0), Stop (1), Suspend (5) """
    Continue: ActionPreference = ...
    Ignore: ActionPreference = ...
    Inquire: ActionPreference = ...
    SilentlyContinue: ActionPreference = ...
    Stop: ActionPreference = ...
    Suspend: ActionPreference = ...
    value__ = ...


class RuntimeException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuntimeException()
    RuntimeException(message: str)
    RuntimeException(message: str, innerException: Exception)
    RuntimeException(message: str, innerException: Exception, errorRecord: ErrorRecord)
    """
    @property
    def WasThrownFromThrowStatement(self) -> bool:
        """
        Get: WasThrownFromThrowStatement(self: RuntimeException) -> bool
        Set: WasThrownFromThrowStatement(self: RuntimeException) = value
        """
        ...


    SerializeObjectState = ...


class ActionPreferenceStopException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ActionPreferenceStopException()
    ActionPreferenceStopException(message: str)
    ActionPreferenceStopException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AliasAttribute(ParsingBaseAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AliasAttribute(*aliasNames: Array[str]) """
    @property
    def AliasNames(self) -> IList:
        """ Get: AliasNames(self: AliasAttribute) -> IList[str] """
        ...


    def __new__(cls, aliasNames:Array) -> Self:
        """ __new__(cls: type, *aliasNames: Array[str]) """
        ...


class CommandInfo(IHasSessionStateEntryVisibility): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandType(self) -> CommandTypes:
        """ Get: CommandType(self: CommandInfo) -> CommandTypes """
        ...

    @property
    def Definition(self) -> str:
        """ Get: Definition(self: CommandInfo) -> str """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: CommandInfo) -> PSModuleInfo """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: CommandInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CommandInfo) -> str """
        ...

    @property
    def OutputType(self) -> ReadOnlyCollection:
        """ Get: OutputType(self: CommandInfo) -> ReadOnlyCollection[PSTypeName] """
        ...

    @property
    def Parameters(self) -> Dictionary:
        """ Get: Parameters(self: CommandInfo) -> Dictionary[str, ParameterMetadata] """
        ...

    @property
    def ParameterSets(self) -> ReadOnlyCollection:
        """ Get: ParameterSets(self: CommandInfo) -> ReadOnlyCollection[CommandParameterSetInfo] """
        ...

    @property
    def RemotingCapability(self) -> RemotingCapability:
        """ Get: RemotingCapability(self: CommandInfo) -> RemotingCapability """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: CommandInfo) -> str """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: CommandInfo) -> Version """
        ...

    @property
    def Visibility(self) -> SessionStateEntryVisibility:
        """
        Get: Visibility(self: CommandInfo) -> SessionStateEntryVisibility
        Set: Visibility(self: CommandInfo) = value
        """
        ...


    def ResolveParameter(self, name:str) -> ParameterMetadata:
        """ ResolveParameter(self: CommandInfo, name: str) -> ParameterMetadata """
        ...

    def ToString(self) -> str:
        """ ToString(self: CommandInfo) -> str """
        ...


class AliasInfo(CommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: AliasInfo) -> str
        Set: Description(self: AliasInfo) = value
        """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: AliasInfo) -> ScopedItemOptions
        Set: Options(self: AliasInfo) = value
        """
        ...

    @property
    def ReferencedCommand(self) -> CommandInfo:
        """ Get: ReferencedCommand(self: AliasInfo) -> CommandInfo """
        ...

    @property
    def ResolvedCommand(self) -> CommandInfo:
        """ Get: ResolvedCommand(self: AliasInfo) -> CommandInfo """
        ...



class Alignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Alignment, values: Center (2), Left (1), Right (3), Undefined (0) """
    Center: Alignment = ...
    Left: Alignment = ...
    Right: Alignment = ...
    Undefined: Alignment = ...
    value__ = ...


class AllowEmptyCollectionAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AllowEmptyCollectionAttribute() """
    pass

class AllowEmptyStringAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AllowEmptyStringAttribute() """
    pass

class AllowNullAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AllowNullAttribute() """
    pass

class ApplicationFailedException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ApplicationFailedException()
    ApplicationFailedException(message: str)
    ApplicationFailedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ApplicationInfo(CommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    @property
    def Extension(self) -> str:
        """ Get: Extension(self: ApplicationInfo) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ApplicationInfo) -> str """
        ...



class ArgumentCompleterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ArgumentCompleterAttribute(type: Type)
    ArgumentCompleterAttribute(scriptBlock: ScriptBlock)
    """
    @property
    def ScriptBlock(self) -> ScriptBlock:
        """ Get: ScriptBlock(self: ArgumentCompleterAttribute) -> ScriptBlock """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ArgumentCompleterAttribute) -> Type """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, scriptBlock: ScriptBlock)
        """
        ...


class ArgumentTransformationAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def TransformNullOptionalParameters(self) -> bool:
        """ Get: TransformNullOptionalParameters(self: ArgumentTransformationAttribute) -> bool """
        ...


    def Transform(self, engineIntrinsics:EngineIntrinsics, inputData:object) -> object:
        """ Transform(self: ArgumentTransformationAttribute, engineIntrinsics: EngineIntrinsics, inputData: object) -> object """
        ...


class MetadataException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MetadataException()
    MetadataException(message: str)
    MetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ArgumentTransformationMetadataException(MetadataException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ArgumentTransformationMetadataException()
    ArgumentTransformationMetadataException(message: str)
    ArgumentTransformationMetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AuthorizationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthorizationManager(shellId: str) """
    def ShouldRun(self, *args): #cannot find CLR method
        """ ShouldRun(self: AuthorizationManager, commandInfo: CommandInfo, origin: CommandOrigin, host: PSHost) -> (bool, Exception) """
        ...


class BackgroundDispatcher(IBackgroundDispatcher): # skipped bases: <type 'object'>
    """ BackgroundDispatcher(transferProvider: EventProvider, transferEvent: EventDescriptor) """
    pass

class FlowControlException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class LoopFlowException(FlowControlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Label(self) -> str:
        """ Get: Label(self: LoopFlowException) -> str """
        ...


    SerializeObjectState = ...


class BreakException(LoopFlowException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class Breakpoint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> ScriptBlock:
        """ Get: Action(self: Breakpoint) -> ScriptBlock """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: Breakpoint) -> bool """
        ...

    @property
    def HitCount(self) -> int:
        """ Get: HitCount(self: Breakpoint) -> int """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Breakpoint) -> int """
        ...

    @property
    def Script(self) -> str:
        """ Get: Script(self: Breakpoint) -> str """
        ...



class BreakpointUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Breakpoint(self) -> Breakpoint:
        """ Get: Breakpoint(self: BreakpointUpdatedEventArgs) -> Breakpoint """
        ...

    @property
    def BreakpointCount(self) -> int:
        """ Get: BreakpointCount(self: BreakpointUpdatedEventArgs) -> int """
        ...

    @property
    def UpdateType(self) -> BreakpointUpdateType:
        """ Get: UpdateType(self: BreakpointUpdatedEventArgs) -> BreakpointUpdateType """
        ...



class BreakpointUpdateType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BreakpointUpdateType, values: Disabled (3), Enabled (2), Removed (1), Set (0) """
    Disabled: BreakpointUpdateType = ...
    Enabled: BreakpointUpdateType = ...
    Removed: BreakpointUpdateType = ...
    Set: BreakpointUpdateType = ...
    value__ = ...


class CallStackFrame: # skipped bases: <type 'object'>, <type 'object'>
    """ CallStackFrame(invocationInfo: InvocationInfo) """
    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: CallStackFrame) -> str """
        ...

    @property
    def InvocationInfo(self) -> InvocationInfo:
        """ Get: InvocationInfo(self: CallStackFrame) -> InvocationInfo """
        ...

    @property
    def Position(self) -> IScriptExtent:
        """ Get: Position(self: CallStackFrame) -> IScriptExtent """
        ...

    @property
    def ScriptLineNumber(self) -> int:
        """ Get: ScriptLineNumber(self: CallStackFrame) -> int """
        ...

    @property
    def ScriptName(self) -> str:
        """ Get: ScriptName(self: CallStackFrame) -> str """
        ...


    def GetFrameVariables(self) -> Dictionary:
        """ GetFrameVariables(self: CallStackFrame) -> Dictionary[str, PSVariable] """
        ...

    def GetScriptLocation(self) -> str:
        """ GetScriptLocation(self: CallStackFrame) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: CallStackFrame) -> str """
        ...


class CatalogInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ CatalogInformation() """
    @property
    def CatalogItems(self) -> Dictionary:
        """
        Get: CatalogItems(self: CatalogInformation) -> Dictionary[str, str]
        Set: CatalogItems(self: CatalogInformation) = value
        """
        ...

    @property
    def HashAlgorithm(self) -> str:
        """
        Get: HashAlgorithm(self: CatalogInformation) -> str
        Set: HashAlgorithm(self: CatalogInformation) = value
        """
        ...

    @property
    def PathItems(self) -> Dictionary:
        """
        Get: PathItems(self: CatalogInformation) -> Dictionary[str, str]
        Set: PathItems(self: CatalogInformation) = value
        """
        ...

    @property
    def Signature(self) -> Signature:
        """
        Get: Signature(self: CatalogInformation) -> Signature
        Set: Signature(self: CatalogInformation) = value
        """
        ...

    @property
    def Status(self) -> CatalogValidationStatus:
        """
        Get: Status(self: CatalogInformation) -> CatalogValidationStatus
        Set: Status(self: CatalogInformation) = value
        """
        ...



class CatalogValidationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CatalogValidationStatus, values: Valid (0), ValidationFailed (1) """
    Valid: CatalogValidationStatus = ...
    ValidationFailed: CatalogValidationStatus = ...
    value__ = ...


class ChildItemCmdletProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Get(self, path, recurse, *__args) -> Collection:
        """
        Get(self: ChildItemCmdletProviderIntrinsics, path: Array[str], recurse: bool, depth: UInt32, force: bool, literalPath: bool) -> Collection[PSObject]
        Get(self: ChildItemCmdletProviderIntrinsics, path: Array[str], recurse: bool, force: bool, literalPath: bool) -> Collection[PSObject]
        Get(self: ChildItemCmdletProviderIntrinsics, path: str, recurse: bool) -> Collection[PSObject]
        """
        ...

    def GetNames(self, path, returnContainers, recurse, *__args) -> Collection:
        """
        GetNames(self: ChildItemCmdletProviderIntrinsics, path: Array[str], returnContainers: ReturnContainers, recurse: bool, force: bool, literalPath: bool) -> Collection[str]
        GetNames(self: ChildItemCmdletProviderIntrinsics, path: Array[str], returnContainers: ReturnContainers, recurse: bool, depth: UInt32, force: bool, literalPath: bool) -> Collection[str]
        GetNames(self: ChildItemCmdletProviderIntrinsics, path: str, returnContainers: ReturnContainers, recurse: bool) -> Collection[str]
        """
        ...

    def HasChild(self, path:str, force:bool = ..., literalPath:bool = ...) -> bool:
        """
        HasChild(self: ChildItemCmdletProviderIntrinsics, path: str) -> bool
        HasChild(self: ChildItemCmdletProviderIntrinsics, path: str, force: bool, literalPath: bool) -> bool
        """
        ...


class Cmdlet(InternalCommand): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandRuntime(self) -> ICommandRuntime:
        """
        Get: CommandRuntime(self: Cmdlet) -> ICommandRuntime
        Set: CommandRuntime(self: Cmdlet) = value
        """
        ...

    @property
    def CommonParameters(self) -> HashSet:
        """ Get: CommonParameters() -> HashSet[str] """
        ...

    @property
    def CurrentPSTransaction(self) -> PSTransactionContext:
        """ Get: CurrentPSTransaction(self: Cmdlet) -> PSTransactionContext """
        ...

    @property
    def OptionalCommonParameters(self) -> HashSet:
        """ Get: OptionalCommonParameters() -> HashSet[str] """
        ...

    @property
    def Stopping(self) -> bool:
        """ Get: Stopping(self: Cmdlet) -> bool """
        ...


    def BeginProcessing(self, *args): #cannot find CLR method
        """ BeginProcessing(self: Cmdlet) """
        ...

    def EndProcessing(self, *args): #cannot find CLR method
        """ EndProcessing(self: Cmdlet) """
        ...

    def GetResourceString(self, baseName:str, resourceId:str) -> str:
        """ GetResourceString(self: Cmdlet, baseName: str, resourceId: str) -> str """
        ...

    def Invoke(self) -> IEnumerable:
        """
        Invoke(self: Cmdlet) -> IEnumerable
        Invoke[T](self: Cmdlet) -> IEnumerable[T]
        """
        ...

    def ProcessRecord(self, *args): #cannot find CLR method
        """ ProcessRecord(self: Cmdlet) """
        ...

    def ShouldContinue(self, query, caption, *__args) -> bool:
        """
        ShouldContinue(self: Cmdlet, query: str, caption: str) -> bool
        ShouldContinue(self: Cmdlet, query: str, caption: str, yesToAll: bool, noToAll: bool) -> (bool, bool, bool)
        ShouldContinue(self: Cmdlet, query: str, caption: str, hasSecurityImpact: bool, yesToAll: bool, noToAll: bool) -> (bool, bool, bool)
        """
        ...

    def ShouldProcess(self, *__args:str) -> bool:
        """
        ShouldProcess(self: Cmdlet, target: str) -> bool
        ShouldProcess(self: Cmdlet, target: str, action: str) -> bool
        ShouldProcess(self: Cmdlet, verboseDescription: str, verboseWarning: str, caption: str) -> bool
        ShouldProcess(self: Cmdlet, verboseDescription: str, verboseWarning: str, caption: str) -> (bool, ShouldProcessReason)
        """
        ...

    def StopProcessing(self, *args): #cannot find CLR method
        """ StopProcessing(self: Cmdlet) """
        ...

    def ThrowTerminatingError(self, errorRecord:ErrorRecord): # -> 
        """ ThrowTerminatingError(self: Cmdlet, errorRecord: ErrorRecord) """
        ...

    def TransactionAvailable(self) -> bool:
        """ TransactionAvailable(self: Cmdlet) -> bool """
        ...

    def WriteCommandDetail(self, text:str): # -> 
        """ WriteCommandDetail(self: Cmdlet, text: str) """
        ...

    def WriteDebug(self, text:str): # -> 
        """ WriteDebug(self: Cmdlet, text: str) """
        ...

    def WriteError(self, errorRecord:ErrorRecord): # -> 
        """ WriteError(self: Cmdlet, errorRecord: ErrorRecord) """
        ...

    def WriteInformation(self, *__args:InformationRecord): # -> 
        """ WriteInformation(self: Cmdlet, messageData: object, tags: Array[str])WriteInformation(self: Cmdlet, informationRecord: InformationRecord) """
        ...

    def WriteObject(self, sendToPipeline:object, enumerateCollection:bool = ...): # -> 
        """ WriteObject(self: Cmdlet, sendToPipeline: object)WriteObject(self: Cmdlet, sendToPipeline: object, enumerateCollection: bool) """
        ...

    def WriteProgress(self, progressRecord:ProgressRecord): # -> 
        """ WriteProgress(self: Cmdlet, progressRecord: ProgressRecord) """
        ...

    def WriteVerbose(self, text:str): # -> 
        """ WriteVerbose(self: Cmdlet, text: str) """
        ...

    def WriteWarning(self, text:str): # -> 
        """ WriteWarning(self: Cmdlet, text: str) """
        ...



class CmdletCommonMetadataAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def ConfirmImpact(self) -> ConfirmImpact:
        """
        Get: ConfirmImpact(self: CmdletCommonMetadataAttribute) -> ConfirmImpact
        Set: ConfirmImpact(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def DefaultParameterSetName(self) -> str:
        """
        Get: DefaultParameterSetName(self: CmdletCommonMetadataAttribute) -> str
        Set: DefaultParameterSetName(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def HelpUri(self) -> str:
        """
        Get: HelpUri(self: CmdletCommonMetadataAttribute) -> str
        Set: HelpUri(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def RemotingCapability(self) -> RemotingCapability:
        """
        Get: RemotingCapability(self: CmdletCommonMetadataAttribute) -> RemotingCapability
        Set: RemotingCapability(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def SupportsPaging(self) -> bool:
        """
        Get: SupportsPaging(self: CmdletCommonMetadataAttribute) -> bool
        Set: SupportsPaging(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def SupportsShouldProcess(self) -> bool:
        """
        Get: SupportsShouldProcess(self: CmdletCommonMetadataAttribute) -> bool
        Set: SupportsShouldProcess(self: CmdletCommonMetadataAttribute) = value
        """
        ...

    @property
    def SupportsTransactions(self) -> bool:
        """
        Get: SupportsTransactions(self: CmdletCommonMetadataAttribute) -> bool
        Set: SupportsTransactions(self: CmdletCommonMetadataAttribute) = value
        """
        ...



class CmdletAttribute(CmdletCommonMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CmdletAttribute(verbName: str, nounName: str) """
    @property
    def NounName(self) -> str:
        """ Get: NounName(self: CmdletAttribute) -> str """
        ...

    @property
    def VerbName(self) -> str:
        """ Get: VerbName(self: CmdletAttribute) -> str """
        ...


    def __new__(cls, verbName:str, nounName:str) -> Self:
        """ __new__(cls: type, verbName: str, nounName: str) """
        ...


class CmdletBindingAttribute(CmdletCommonMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CmdletBindingAttribute() """
    @property
    def PositionalBinding(self) -> bool:
        """
        Get: PositionalBinding(self: CmdletBindingAttribute) -> bool
        Set: PositionalBinding(self: CmdletBindingAttribute) = value
        """
        ...



class CmdletInfo(CommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ CmdletInfo(name: str, implementingType: Type) """
    @property
    def DefaultParameterSet(self) -> str:
        """ Get: DefaultParameterSet(self: CmdletInfo) -> str """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: CmdletInfo) -> str """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: CmdletInfo) -> Type """
        ...

    @property
    def Noun(self) -> str:
        """ Get: Noun(self: CmdletInfo) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: CmdletInfo) -> ScopedItemOptions
        Set: Options(self: CmdletInfo) = value
        """
        ...

    @property
    def PSSnapIn(self) -> PSSnapInInfo:
        """ Get: PSSnapIn(self: CmdletInfo) -> PSSnapInInfo """
        ...

    @property
    def Verb(self) -> str:
        """ Get: Verb(self: CmdletInfo) -> str """
        ...


    def __new__(cls, name:str, implementingType:Type) -> Self:
        """ __new__(cls: type, name: str, implementingType: Type) """
        ...


class CmdletInvocationException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CmdletInvocationException()
    CmdletInvocationException(message: str)
    CmdletInvocationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CmdletProviderInvocationException(CmdletInvocationException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CmdletProviderInvocationException()
    CmdletProviderInvocationException(message: str)
    CmdletProviderInvocationException(message: str, innerException: Exception)
    """
    @property
    def ProviderInfo(self) -> ProviderInfo:
        """ Get: ProviderInfo(self: CmdletProviderInvocationException) -> ProviderInfo """
        ...

    @property
    def ProviderInvocationException(self) -> ProviderInvocationException:
        """ Get: ProviderInvocationException(self: CmdletProviderInvocationException) -> ProviderInvocationException """
        ...


    SerializeObjectState = ...


class CmdletProviderManagementIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Get(self, name:str) -> Collection:
        """ Get(self: CmdletProviderManagementIntrinsics, name: str) -> Collection[ProviderInfo] """
        ...

    def GetAll(self) -> IEnumerable:
        """ GetAll(self: CmdletProviderManagementIntrinsics) -> IEnumerable[ProviderInfo] """
        ...

    def GetOne(self, name:str) -> ProviderInfo:
        """ GetOne(self: CmdletProviderManagementIntrinsics, name: str) -> ProviderInfo """
        ...


class CmsMessageRecipient: # skipped bases: <type 'object'>, <type 'object'>
    """
    CmsMessageRecipient(identifier: str)
    CmsMessageRecipient(certificate: X509Certificate2)
    """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: CmsMessageRecipient) -> X509Certificate2Collection """
        ...


    def Resolve(self, sessionState, purpose, error) -> ErrorRecord:
        """ Resolve(self: CmsMessageRecipient, sessionState: SessionState, purpose: ResolutionPurpose) -> ErrorRecord """
        ...


class CommandBreakpoint(Breakpoint): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Command(self) -> str:
        """ Get: Command(self: CommandBreakpoint) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: CommandBreakpoint) -> str """
        ...


class CommandCompletion: # skipped bases: <type 'object'>, <type 'object'>
    """ CommandCompletion(matches: Collection[CompletionResult], currentMatchIndex: int, replacementIndex: int, replacementLength: int) """
    @property
    def CompletionMatches(self) -> Collection:
        """
        Get: CompletionMatches(self: CommandCompletion) -> Collection[CompletionResult]
        Set: CompletionMatches(self: CommandCompletion) = value
        """
        ...

    @property
    def CurrentMatchIndex(self) -> int:
        """
        Get: CurrentMatchIndex(self: CommandCompletion) -> int
        Set: CurrentMatchIndex(self: CommandCompletion) = value
        """
        ...

    @property
    def ReplacementIndex(self) -> int:
        """
        Get: ReplacementIndex(self: CommandCompletion) -> int
        Set: ReplacementIndex(self: CommandCompletion) = value
        """
        ...

    @property
    def ReplacementLength(self) -> int:
        """
        Get: ReplacementLength(self: CommandCompletion) -> int
        Set: ReplacementLength(self: CommandCompletion) = value
        """
        ...


    @staticmethod
    def CompleteInput(*__args) -> CommandCompletion:
        """
        CompleteInput(input: str, cursorIndex: int, options: Hashtable) -> CommandCompletion
        CompleteInput(ast: Ast, tokens: Array[Token], positionOfCursor: IScriptPosition, options: Hashtable) -> CommandCompletion
        CompleteInput(input: str, cursorIndex: int, options: Hashtable, powershell: PowerShell) -> CommandCompletion
        CompleteInput(ast: Ast, tokens: Array[Token], cursorPosition: IScriptPosition, options: Hashtable, powershell: PowerShell) -> CommandCompletion
        """
        ...

    def GetNextResult(self, forward:bool) -> CompletionResult:
        """ GetNextResult(self: CommandCompletion, forward: bool) -> CompletionResult """
        ...

    @staticmethod
    def MapStringInputToParsedInput(input:str, cursorIndex:int): # -> Tuple, IScriptPosition]
        """ MapStringInputToParsedInput(input: str, cursorIndex: int) -> Tuple[Ast, Array[Token], IScriptPosition] """
        ...


class CommandInvocationIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CommandNotFoundAction(self) -> EventHandler:
        """
        Get: CommandNotFoundAction(self: CommandInvocationIntrinsics) -> EventHandler[CommandLookupEventArgs]
        Set: CommandNotFoundAction(self: CommandInvocationIntrinsics) = value
        """
        ...

    @property
    def HasErrors(self) -> bool:
        """
        Get: HasErrors(self: CommandInvocationIntrinsics) -> bool
        Set: HasErrors(self: CommandInvocationIntrinsics) = value
        """
        ...

    @property
    def PostCommandLookupAction(self) -> EventHandler:
        """
        Get: PostCommandLookupAction(self: CommandInvocationIntrinsics) -> EventHandler[CommandLookupEventArgs]
        Set: PostCommandLookupAction(self: CommandInvocationIntrinsics) = value
        """
        ...

    @property
    def PreCommandLookupAction(self) -> EventHandler:
        """
        Get: PreCommandLookupAction(self: CommandInvocationIntrinsics) -> EventHandler[CommandLookupEventArgs]
        Set: PreCommandLookupAction(self: CommandInvocationIntrinsics) = value
        """
        ...


    def ExpandString(self, source:str) -> str:
        """ ExpandString(self: CommandInvocationIntrinsics, source: str) -> str """
        ...

    def GetCmdlet(self, commandName:str) -> CmdletInfo:
        """ GetCmdlet(self: CommandInvocationIntrinsics, commandName: str) -> CmdletInfo """
        ...

    def GetCmdletByTypeName(self, cmdletTypeName:str) -> CmdletInfo:
        """ GetCmdletByTypeName(self: CommandInvocationIntrinsics, cmdletTypeName: str) -> CmdletInfo """
        ...

    def GetCmdlets(self, pattern:str = ...) -> List:
        """
        GetCmdlets(self: CommandInvocationIntrinsics, pattern: str) -> List[CmdletInfo]
        GetCmdlets(self: CommandInvocationIntrinsics) -> List[CmdletInfo]
        """
        ...

    def GetCommand(self, commandName:str, type:CommandTypes, arguments:Array = ...) -> CommandInfo:
        """
        GetCommand(self: CommandInvocationIntrinsics, commandName: str, type: CommandTypes) -> CommandInfo
        GetCommand(self: CommandInvocationIntrinsics, commandName: str, type: CommandTypes, arguments: Array[object]) -> CommandInfo
        """
        ...

    def GetCommandName(self, name:str, nameIsPattern:bool, returnFullName:bool) -> List:
        """ GetCommandName(self: CommandInvocationIntrinsics, name: str, nameIsPattern: bool, returnFullName: bool) -> List[str] """
        ...

    def GetCommands(self, name:str, commandTypes:CommandTypes, nameIsPattern:bool) -> IEnumerable:
        """ GetCommands(self: CommandInvocationIntrinsics, name: str, commandTypes: CommandTypes, nameIsPattern: bool) -> IEnumerable[CommandInfo] """
        ...

    def InvokeScript(self, *__args:str) -> Collection:
        """
        InvokeScript(self: CommandInvocationIntrinsics, sessionState: SessionState, scriptBlock: ScriptBlock, *args: Array[object]) -> Collection[PSObject]
        InvokeScript(self: CommandInvocationIntrinsics, useLocalScope: bool, scriptBlock: ScriptBlock, input: IList, *args: Array[object]) -> Collection[PSObject]
        InvokeScript(self: CommandInvocationIntrinsics, script: str, useNewScope: bool, writeToPipeline: PipelineResultTypes, input: IList, *args: Array[object]) -> Collection[PSObject]
        InvokeScript(self: CommandInvocationIntrinsics, script: str) -> Collection[PSObject]
        InvokeScript(self: CommandInvocationIntrinsics, script: str, *args: Array[object]) -> Collection[PSObject]
        """
        ...

    def NewScriptBlock(self, scriptText:str) -> ScriptBlock:
        """ NewScriptBlock(self: CommandInvocationIntrinsics, scriptText: str) -> ScriptBlock """
        ...


class CommandLookupEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Command(self) -> CommandInfo:
        """
        Get: Command(self: CommandLookupEventArgs) -> CommandInfo
        Set: Command(self: CommandLookupEventArgs) = value
        """
        ...

    @property
    def CommandName(self) -> str:
        """ Get: CommandName(self: CommandLookupEventArgs) -> str """
        ...

    @property
    def CommandOrigin(self) -> CommandOrigin:
        """ Get: CommandOrigin(self: CommandLookupEventArgs) -> CommandOrigin """
        ...

    @property
    def CommandScriptBlock(self) -> ScriptBlock:
        """
        Get: CommandScriptBlock(self: CommandLookupEventArgs) -> ScriptBlock
        Set: CommandScriptBlock(self: CommandLookupEventArgs) = value
        """
        ...

    @property
    def StopSearch(self) -> bool:
        """
        Get: StopSearch(self: CommandLookupEventArgs) -> bool
        Set: StopSearch(self: CommandLookupEventArgs) = value
        """
        ...



class CommandMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """
    CommandMetadata(commandType: Type)
    CommandMetadata(commandInfo: CommandInfo)
    CommandMetadata(commandInfo: CommandInfo, shouldGenerateCommonParameters: bool)
    CommandMetadata(path: str)
    CommandMetadata(other: CommandMetadata)
    """
    @property
    def CommandType(self) -> Type:
        """ Get: CommandType(self: CommandMetadata) -> Type """
        ...

    @property
    def ConfirmImpact(self) -> ConfirmImpact:
        """
        Get: ConfirmImpact(self: CommandMetadata) -> ConfirmImpact
        Set: ConfirmImpact(self: CommandMetadata) = value
        """
        ...

    @property
    def DefaultParameterSetName(self) -> str:
        """
        Get: DefaultParameterSetName(self: CommandMetadata) -> str
        Set: DefaultParameterSetName(self: CommandMetadata) = value
        """
        ...

    @property
    def HelpUri(self) -> str:
        """
        Get: HelpUri(self: CommandMetadata) -> str
        Set: HelpUri(self: CommandMetadata) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CommandMetadata) -> str
        Set: Name(self: CommandMetadata) = value
        """
        ...

    @property
    def Parameters(self) -> Dictionary:
        """ Get: Parameters(self: CommandMetadata) -> Dictionary[str, ParameterMetadata] """
        ...

    @property
    def PositionalBinding(self) -> bool:
        """
        Get: PositionalBinding(self: CommandMetadata) -> bool
        Set: PositionalBinding(self: CommandMetadata) = value
        """
        ...

    @property
    def RemotingCapability(self) -> RemotingCapability:
        """
        Get: RemotingCapability(self: CommandMetadata) -> RemotingCapability
        Set: RemotingCapability(self: CommandMetadata) = value
        """
        ...

    @property
    def SupportsPaging(self) -> bool:
        """
        Get: SupportsPaging(self: CommandMetadata) -> bool
        Set: SupportsPaging(self: CommandMetadata) = value
        """
        ...

    @property
    def SupportsShouldProcess(self) -> bool:
        """
        Get: SupportsShouldProcess(self: CommandMetadata) -> bool
        Set: SupportsShouldProcess(self: CommandMetadata) = value
        """
        ...

    @property
    def SupportsTransactions(self) -> bool:
        """
        Get: SupportsTransactions(self: CommandMetadata) -> bool
        Set: SupportsTransactions(self: CommandMetadata) = value
        """
        ...


    @staticmethod
    def GetRestrictedCommands(sessionCapabilities:SessionCapabilities) -> Dictionary:
        """ GetRestrictedCommands(sessionCapabilities: SessionCapabilities) -> Dictionary[str, CommandMetadata] """
        ...


class CommandNotFoundException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CommandNotFoundException()
    CommandNotFoundException(message: str)
    CommandNotFoundException(message: str, innerException: Exception)
    """
    @property
    def CommandName(self) -> str:
        """
        Get: CommandName(self: CommandNotFoundException) -> str
        Set: CommandName(self: CommandNotFoundException) = value
        """
        ...


    SerializeObjectState = ...


class CommandOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CommandOrigin, values: Internal (1), Runspace (0) """
    Internal: CommandOrigin = ...
    Runspace: CommandOrigin = ...
    value__ = ...


class CommandParameterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Aliases(self) -> ReadOnlyCollection:
        """ Get: Aliases(self: CommandParameterInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: CommandParameterInfo) -> ReadOnlyCollection[Attribute] """
        ...

    @property
    def HelpMessage(self) -> str:
        """ Get: HelpMessage(self: CommandParameterInfo) -> str """
        ...

    @property
    def IsDynamic(self) -> bool:
        """ Get: IsDynamic(self: CommandParameterInfo) -> bool """
        ...

    @property
    def IsMandatory(self) -> bool:
        """ Get: IsMandatory(self: CommandParameterInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CommandParameterInfo) -> str """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: CommandParameterInfo) -> Type """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: CommandParameterInfo) -> int """
        ...

    @property
    def ValueFromPipeline(self) -> bool:
        """ Get: ValueFromPipeline(self: CommandParameterInfo) -> bool """
        ...

    @property
    def ValueFromPipelineByPropertyName(self) -> bool:
        """ Get: ValueFromPipelineByPropertyName(self: CommandParameterInfo) -> bool """
        ...

    @property
    def ValueFromRemainingArguments(self) -> bool:
        """ Get: ValueFromRemainingArguments(self: CommandParameterInfo) -> bool """
        ...



class CommandParameterSetInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: CommandParameterSetInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CommandParameterSetInfo) -> str """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: CommandParameterSetInfo) -> ReadOnlyCollection[CommandParameterInfo] """
        ...


    def ToString(self) -> str:
        """ ToString(self: CommandParameterSetInfo) -> str """
        ...


class CommandTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CommandTypes, values: Alias (1), All (511), Application (32), Cmdlet (8), Configuration (256), ExternalScript (16), Filter (4), Function (2), Script (64), Workflow (128) """
    Alias: CommandTypes = ...
    All: CommandTypes = ...
    Application: CommandTypes = ...
    Cmdlet: CommandTypes = ...
    Configuration: CommandTypes = ...
    ExternalScript: CommandTypes = ...
    Filter: CommandTypes = ...
    Function: CommandTypes = ...
    Script: CommandTypes = ...
    value__ = ...
    Workflow: CommandTypes = ...


class CompletionCompleters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CompleteCommand(commandName:str, moduleName:str = ..., commandTypes:CommandTypes = ...) -> IEnumerable:
        """
        CompleteCommand(commandName: str) -> IEnumerable[CompletionResult]
        CompleteCommand(commandName: str, moduleName: str, commandTypes: CommandTypes) -> IEnumerable[CompletionResult]
        """
        ...

    @staticmethod
    def CompleteFilename(fileName:str) -> IEnumerable:
        """ CompleteFilename(fileName: str) -> IEnumerable[CompletionResult] """
        ...

    @staticmethod
    def CompleteOperator(wordToComplete:str) -> List:
        """ CompleteOperator(wordToComplete: str) -> List[CompletionResult] """
        ...

    @staticmethod
    def CompleteType(typeName:str) -> IEnumerable:
        """ CompleteType(typeName: str) -> IEnumerable[CompletionResult] """
        ...

    @staticmethod
    def CompleteVariable(variableName:str) -> IEnumerable:
        """ CompleteVariable(variableName: str) -> IEnumerable[CompletionResult] """
        ...

    __all__: list = ...


class CompletionResult: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompletionResult(completionText: str, listItemText: str, resultType: CompletionResultType, toolTip: str)
    CompletionResult(completionText: str)
    """
    @property
    def CompletionText(self) -> str:
        """ Get: CompletionText(self: CompletionResult) -> str """
        ...

    @property
    def ListItemText(self) -> str:
        """ Get: ListItemText(self: CompletionResult) -> str """
        ...

    @property
    def ResultType(self) -> CompletionResultType:
        """ Get: ResultType(self: CompletionResult) -> CompletionResultType """
        ...

    @property
    def ToolTip(self) -> str:
        """ Get: ToolTip(self: CompletionResult) -> str """
        ...



class CompletionResultType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompletionResultType, values: Command (2), DynamicKeyword (13), History (1), Keyword (12), Method (6), Namespace (10), ParameterName (7), ParameterValue (8), Property (5), ProviderContainer (4), ProviderItem (3), Text (0), Type (11), Variable (9) """
    Command: CompletionResultType = ...
    DynamicKeyword: CompletionResultType = ...
    History: CompletionResultType = ...
    Keyword: CompletionResultType = ...
    Method: CompletionResultType = ...
    Namespace: CompletionResultType = ...
    ParameterName: CompletionResultType = ...
    ParameterValue: CompletionResultType = ...
    Property: CompletionResultType = ...
    ProviderContainer: CompletionResultType = ...
    ProviderItem: CompletionResultType = ...
    Text: CompletionResultType = ...
    Type: CompletionResultType = ...
    value__ = ...
    Variable: CompletionResultType = ...


class FunctionInfo(CommandInfo, IScriptCommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    @property
    def CmdletBinding(self) -> bool:
        """ Get: CmdletBinding(self: FunctionInfo) -> bool """
        ...

    @property
    def DefaultParameterSet(self) -> str:
        """ Get: DefaultParameterSet(self: FunctionInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: FunctionInfo) -> str
        Set: Description(self: FunctionInfo) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: FunctionInfo) -> str """
        ...

    @property
    def Noun(self) -> str:
        """ Get: Noun(self: FunctionInfo) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: FunctionInfo) -> ScopedItemOptions
        Set: Options(self: FunctionInfo) = value
        """
        ...

    @property
    def ScriptBlock(self) -> ScriptBlock:
        """ Get: ScriptBlock(self: FunctionInfo) -> ScriptBlock """
        ...

    @property
    def Verb(self) -> str:
        """ Get: Verb(self: FunctionInfo) -> str """
        ...


    def Update(self, *args): #cannot find CLR method
        """ Update(self: FunctionInfo, newFunction: FunctionInfo, force: bool, options: ScopedItemOptions, helpFile: str) """
        ...


class ConfigurationInfo(FunctionInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'IScriptCommandInfo'>, <type 'object'>
    """ no doc """
    @property
    def IsMetaConfiguration(self) -> bool:
        """ Get: IsMetaConfiguration(self: ConfigurationInfo) -> bool """
        ...



class ConfirmImpact(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfirmImpact, values: High (3), Low (1), Medium (2), None (0) """
    High: ConfirmImpact = ...
    Low: ConfirmImpact = ...
    Medium: ConfirmImpact = ...
    value__ = ...


class Job(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChildJobs(self) -> IList:
        """ Get: ChildJobs(self: Job) -> IList[Job] """
        ...

    @property
    def Command(self) -> str:
        """ Get: Command(self: Job) -> str """
        ...

    @property
    def Debug(self) -> PSDataCollection:
        """
        Get: Debug(self: Job) -> PSDataCollection[DebugRecord]
        Set: Debug(self: Job) = value
        """
        ...

    @property
    def Error(self) -> PSDataCollection:
        """
        Get: Error(self: Job) -> PSDataCollection[ErrorRecord]
        Set: Error(self: Job) = value
        """
        ...

    @property
    def Finished(self) -> WaitHandle:
        """ Get: Finished(self: Job) -> WaitHandle """
        ...

    @property
    def HasMoreData(self) -> bool:
        """ Get: HasMoreData(self: Job) -> bool """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Job) -> int """
        ...

    @property
    def Information(self) -> PSDataCollection:
        """
        Get: Information(self: Job) -> PSDataCollection[InformationRecord]
        Set: Information(self: Job) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: Job) -> Guid """
        ...

    @property
    def JobStateInfo(self) -> JobStateInfo:
        """ Get: JobStateInfo(self: Job) -> JobStateInfo """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: Job) -> str """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Job) -> str
        Set: Name(self: Job) = value
        """
        ...

    @property
    def Output(self) -> PSDataCollection:
        """
        Get: Output(self: Job) -> PSDataCollection[PSObject]
        Set: Output(self: Job) = value
        """
        ...

    @property
    def Progress(self) -> PSDataCollection:
        """
        Get: Progress(self: Job) -> PSDataCollection[ProgressRecord]
        Set: Progress(self: Job) = value
        """
        ...

    @property
    def PSBeginTime(self) -> Nullable:
        """ Get: PSBeginTime(self: Job) -> Nullable[DateTime] """
        ...

    @property
    def PSEndTime(self) -> Nullable:
        """ Get: PSEndTime(self: Job) -> Nullable[DateTime] """
        ...

    @property
    def PSJobTypeName(self) -> str:
        """ Get: PSJobTypeName(self: Job) -> str """
        ...

    @property
    def StatusMessage(self) -> str:
        """ Get: StatusMessage(self: Job) -> str """
        ...

    @property
    def Verbose(self) -> PSDataCollection:
        """
        Get: Verbose(self: Job) -> PSDataCollection[VerboseRecord]
        Set: Verbose(self: Job) = value
        """
        ...

    @property
    def Warning(self) -> PSDataCollection:
        """
        Get: Warning(self: Job) -> PSDataCollection[WarningRecord]
        Set: Warning(self: Job) = value
        """
        ...


    def AutoGenerateJobName(self, *args): #cannot find CLR method
        """ AutoGenerateJobName(self: Job) -> str """
        ...

    def DoLoadJobStreams(self, *args): #cannot find CLR method
        """ DoLoadJobStreams(self: Job) """
        ...

    def DoUnloadJobStreams(self, *args): #cannot find CLR method
        """ DoUnloadJobStreams(self: Job) """
        ...

    def LoadJobStreams(self): # -> 
        """ LoadJobStreams(self: Job) """
        ...

    def SetJobState(self, *args): #cannot find CLR method
        """ SetJobState(self: Job, state: JobState) """
        ...

    def StopJob(self): # -> 
        """ StopJob(self: Job) """
        ...

    def UnloadJobStreams(self): # -> 
        """ UnloadJobStreams(self: Job) """
        ...

    StateChanged = ...


class Job2(Job): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def StartParameters(self) -> List:
        """
        Get: StartParameters(self: Job2) -> List[CommandParameterCollection]
        Set: StartParameters(self: Job2) = value
        """
        ...

    @property
    def SyncRoot(self):
        ...


    def OnResumeJobCompleted(self, *args): #cannot find CLR method
        """ OnResumeJobCompleted(self: Job2, eventArgs: AsyncCompletedEventArgs) """
        ...

    def OnStartJobCompleted(self, *args): #cannot find CLR method
        """ OnStartJobCompleted(self: Job2, eventArgs: AsyncCompletedEventArgs) """
        ...

    def OnStopJobCompleted(self, *args): #cannot find CLR method
        """ OnStopJobCompleted(self: Job2, eventArgs: AsyncCompletedEventArgs) """
        ...

    def OnSuspendJobCompleted(self, *args): #cannot find CLR method
        """ OnSuspendJobCompleted(self: Job2, eventArgs: AsyncCompletedEventArgs) """
        ...

    def OnUnblockJobCompleted(self, *args): #cannot find CLR method
        """ OnUnblockJobCompleted(self: Job2, eventArgs: AsyncCompletedEventArgs) """
        ...

    def ResumeJob(self): # -> 
        """ ResumeJob(self: Job2) """
        ...

    def ResumeJobAsync(self): # -> 
        """ ResumeJobAsync(self: Job2) """
        ...

    def StartJob(self): # -> 
        """ StartJob(self: Job2) """
        ...

    def StartJobAsync(self): # -> 
        """ StartJobAsync(self: Job2) """
        ...

    def StopJobAsync(self, force:bool = ..., reason:str = ...): # -> 
        """ StopJobAsync(self: Job2)StopJobAsync(self: Job2, force: bool, reason: str) """
        ...

    def SuspendJob(self, force:bool = ..., reason:str = ...): # -> 
        """ SuspendJob(self: Job2)SuspendJob(self: Job2, force: bool, reason: str) """
        ...

    def SuspendJobAsync(self, force:bool = ..., reason:str = ...): # -> 
        """ SuspendJobAsync(self: Job2)SuspendJobAsync(self: Job2, force: bool, reason: str) """
        ...

    def UnblockJob(self): # -> 
        """ UnblockJob(self: Job2) """
        ...

    def UnblockJobAsync(self): # -> 
        """ UnblockJobAsync(self: Job2) """
        ...

    ResumeJobCompleted = ...
    StartJobCompleted = ...
    StopJobCompleted = ...
    SuspendJobCompleted = ...
    UnblockJobCompleted = ...


class ContainerParentJob(Job2): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ContainerParentJob(command: str, name: str)
    ContainerParentJob(command: str)
    ContainerParentJob(command: str, name: str, jobId: JobIdentifier)
    ContainerParentJob(command: str, name: str, instanceId: Guid)
    ContainerParentJob(command: str, name: str, jobId: JobIdentifier, jobType: str)
    ContainerParentJob(command: str, name: str, instanceId: Guid, jobType: str)
    ContainerParentJob(command: str, name: str, jobType: str)
    """
    @property
    def HasMoreData(self) -> bool:
        """ Get: HasMoreData(self: ContainerParentJob) -> bool """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: ContainerParentJob) -> str """
        ...

    @property
    def StatusMessage(self) -> str:
        """ Get: StatusMessage(self: ContainerParentJob) -> str """
        ...


    def AddChildJob(self, childJob:Job2): # -> 
        """ AddChildJob(self: ContainerParentJob, childJob: Job2) """
        ...


class ContentCmdletProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clear(self, path:Array, force:bool = ..., literalPath:bool = ...): # -> 
        """ Clear(self: ContentCmdletProviderIntrinsics, path: Array[str], force: bool, literalPath: bool)Clear(self: ContentCmdletProviderIntrinsics, path: str) """
        ...

    def GetReader(self, path:Array, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        GetReader(self: ContentCmdletProviderIntrinsics, path: Array[str], force: bool, literalPath: bool) -> Collection[IContentReader]
        GetReader(self: ContentCmdletProviderIntrinsics, path: str) -> Collection[IContentReader]
        """
        ...

    def GetWriter(self, path:Array, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        GetWriter(self: ContentCmdletProviderIntrinsics, path: Array[str], force: bool, literalPath: bool) -> Collection[IContentWriter]
        GetWriter(self: ContentCmdletProviderIntrinsics, path: str) -> Collection[IContentWriter]
        """
        ...


class ContinueException(LoopFlowException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class PSTypeConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanConvertFrom(self, sourceValue:PSObject, destinationType:Type) -> bool:
        """
        CanConvertFrom(self: PSTypeConverter, sourceValue: PSObject, destinationType: Type) -> bool
        CanConvertFrom(self: PSTypeConverter, sourceValue: object, destinationType: Type) -> bool
        """
        ...

    def CanConvertTo(self, sourceValue:PSObject, destinationType:Type) -> bool:
        """
        CanConvertTo(self: PSTypeConverter, sourceValue: PSObject, destinationType: Type) -> bool
        CanConvertTo(self: PSTypeConverter, sourceValue: object, destinationType: Type) -> bool
        """
        ...

    def ConvertFrom(self, sourceValue:PSObject, destinationType:Type, formatProvider:IFormatProvider, ignoreCase:bool) -> object:
        """
        ConvertFrom(self: PSTypeConverter, sourceValue: PSObject, destinationType: Type, formatProvider: IFormatProvider, ignoreCase: bool) -> object
        ConvertFrom(self: PSTypeConverter, sourceValue: object, destinationType: Type, formatProvider: IFormatProvider, ignoreCase: bool) -> object
        """
        ...

    def ConvertTo(self, sourceValue:PSObject, destinationType:Type, formatProvider:IFormatProvider, ignoreCase:bool) -> object:
        """
        ConvertTo(self: PSTypeConverter, sourceValue: PSObject, destinationType: Type, formatProvider: IFormatProvider, ignoreCase: bool) -> object
        ConvertTo(self: PSTypeConverter, sourceValue: object, destinationType: Type, formatProvider: IFormatProvider, ignoreCase: bool) -> object
        """
        ...


class ConvertThroughString(PSTypeConverter): # skipped bases: <type 'object'>
    """ ConvertThroughString() """
    pass

class CopyContainers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CopyContainers, values: CopyChildrenOfTargetContainer (1), CopyTargetContainer (0) """
    CopyChildrenOfTargetContainer: CopyContainers = ...
    CopyTargetContainer: CopyContainers = ...
    value__ = ...


class CredentialAttribute(ArgumentTransformationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CredentialAttribute() """
    pass

class PSControl: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def GroupBy(self) -> PSControlGroupBy:
        """
        Get: GroupBy(self: PSControl) -> PSControlGroupBy
        Set: GroupBy(self: PSControl) = value
        """
        ...

    @property
    def OutOfBand(self) -> bool:
        """
        Get: OutOfBand(self: PSControl) -> bool
        Set: OutOfBand(self: PSControl) = value
        """
        ...



class CustomControl(PSControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Entries(self) -> List:
        """
        Get: Entries(self: CustomControl) -> List[CustomControlEntry]
        Set: Entries(self: CustomControl) = value
        """
        ...


    @staticmethod
    def Create(outOfBand:bool) -> CustomControlBuilder:
        """ Create(outOfBand: bool) -> CustomControlBuilder """
        ...


class CustomControlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def EndControl(self) -> CustomControl:
        """ EndControl(self: CustomControlBuilder) -> CustomControl """
        ...

    def GroupByProperty(self, property:str, customControl:CustomControl, label:str) -> CustomControlBuilder:
        """ GroupByProperty(self: CustomControlBuilder, property: str, customControl: CustomControl, label: str) -> CustomControlBuilder """
        ...

    def GroupByScriptBlock(self, scriptBlock:str, customControl:CustomControl, label:str) -> CustomControlBuilder:
        """ GroupByScriptBlock(self: CustomControlBuilder, scriptBlock: str, customControl: CustomControl, label: str) -> CustomControlBuilder """
        ...

    def StartEntry(self, entrySelectedByType:IEnumerable, entrySelectedByCondition:IEnumerable) -> CustomEntryBuilder:
        """ StartEntry(self: CustomControlBuilder, entrySelectedByType: IEnumerable[str], entrySelectedByCondition: IEnumerable[DisplayEntry]) -> CustomEntryBuilder """
        ...


class CustomControlEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CustomItems(self) -> List:
        """
        Get: CustomItems(self: CustomControlEntry) -> List[CustomItemBase]
        Set: CustomItems(self: CustomControlEntry) = value
        """
        ...

    @property
    def SelectedBy(self) -> EntrySelectedBy:
        """
        Get: SelectedBy(self: CustomControlEntry) -> EntrySelectedBy
        Set: SelectedBy(self: CustomControlEntry) = value
        """
        ...



class CustomEntryBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddCustomControlExpressionBinding(self, customControl:CustomControl, enumerateCollection:bool, selectedByType:str, selectedByScript:str) -> CustomEntryBuilder:
        """ AddCustomControlExpressionBinding(self: CustomEntryBuilder, customControl: CustomControl, enumerateCollection: bool, selectedByType: str, selectedByScript: str) -> CustomEntryBuilder """
        ...

    def AddNewline(self, count:int) -> CustomEntryBuilder:
        """ AddNewline(self: CustomEntryBuilder, count: int) -> CustomEntryBuilder """
        ...

    def AddPropertyExpressionBinding(self, property:str, enumerateCollection:bool, selectedByType:str, selectedByScript:str, customControl:CustomControl) -> CustomEntryBuilder:
        """ AddPropertyExpressionBinding(self: CustomEntryBuilder, property: str, enumerateCollection: bool, selectedByType: str, selectedByScript: str, customControl: CustomControl) -> CustomEntryBuilder """
        ...

    def AddScriptBlockExpressionBinding(self, scriptBlock:str, enumerateCollection:bool, selectedByType:str, selectedByScript:str, customControl:CustomControl) -> CustomEntryBuilder:
        """ AddScriptBlockExpressionBinding(self: CustomEntryBuilder, scriptBlock: str, enumerateCollection: bool, selectedByType: str, selectedByScript: str, customControl: CustomControl) -> CustomEntryBuilder """
        ...

    def AddText(self, text:str) -> CustomEntryBuilder:
        """ AddText(self: CustomEntryBuilder, text: str) -> CustomEntryBuilder """
        ...

    def EndEntry(self) -> CustomControlBuilder:
        """ EndEntry(self: CustomEntryBuilder) -> CustomControlBuilder """
        ...

    def EndFrame(self) -> CustomEntryBuilder:
        """ EndFrame(self: CustomEntryBuilder) -> CustomEntryBuilder """
        ...

    def StartFrame(self, leftIndent:UInt32, rightIndent:UInt32, firstLineHanging:UInt32, firstLineIndent:UInt32) -> CustomEntryBuilder:
        """ StartFrame(self: CustomEntryBuilder, leftIndent: UInt32, rightIndent: UInt32, firstLineHanging: UInt32, firstLineIndent: UInt32) -> CustomEntryBuilder """
        ...


class CustomItemBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class CustomItemExpression(CustomItemBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CustomControl(self) -> CustomControl:
        """
        Get: CustomControl(self: CustomItemExpression) -> CustomControl
        Set: CustomControl(self: CustomItemExpression) = value
        """
        ...

    @property
    def EnumerateCollection(self) -> bool:
        """
        Get: EnumerateCollection(self: CustomItemExpression) -> bool
        Set: EnumerateCollection(self: CustomItemExpression) = value
        """
        ...

    @property
    def Expression(self) -> DisplayEntry:
        """
        Get: Expression(self: CustomItemExpression) -> DisplayEntry
        Set: Expression(self: CustomItemExpression) = value
        """
        ...

    @property
    def ItemSelectionCondition(self) -> DisplayEntry:
        """
        Get: ItemSelectionCondition(self: CustomItemExpression) -> DisplayEntry
        Set: ItemSelectionCondition(self: CustomItemExpression) = value
        """
        ...



class CustomItemFrame(CustomItemBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CustomItems(self) -> List:
        """
        Get: CustomItems(self: CustomItemFrame) -> List[CustomItemBase]
        Set: CustomItems(self: CustomItemFrame) = value
        """
        ...

    @property
    def FirstLineHanging(self) -> UInt32:
        """
        Get: FirstLineHanging(self: CustomItemFrame) -> UInt32
        Set: FirstLineHanging(self: CustomItemFrame) = value
        """
        ...

    @property
    def FirstLineIndent(self) -> UInt32:
        """
        Get: FirstLineIndent(self: CustomItemFrame) -> UInt32
        Set: FirstLineIndent(self: CustomItemFrame) = value
        """
        ...

    @property
    def LeftIndent(self) -> UInt32:
        """
        Get: LeftIndent(self: CustomItemFrame) -> UInt32
        Set: LeftIndent(self: CustomItemFrame) = value
        """
        ...

    @property
    def RightIndent(self) -> UInt32:
        """
        Get: RightIndent(self: CustomItemFrame) -> UInt32
        Set: RightIndent(self: CustomItemFrame) = value
        """
        ...



class CustomItemNewline(CustomItemBase): # skipped bases: <type 'object'>
    """ CustomItemNewline() """
    @property
    def Count(self) -> int:
        """
        Get: Count(self: CustomItemNewline) -> int
        Set: Count(self: CustomItemNewline) = value
        """
        ...



class CustomItemText(CustomItemBase): # skipped bases: <type 'object'>
    """ CustomItemText() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: CustomItemText) -> str
        Set: Text(self: CustomItemText) = value
        """
        ...



class PSInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    pass

class PSSnapInInstaller(PSInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: PSSnapInInstaller) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: PSSnapInInstaller) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSSnapInInstaller) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSSnapInInstaller) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: PSSnapInInstaller) -> str """
        ...



class CustomPSSnapIn(PSSnapInInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def Cmdlets(self) -> Collection:
        """ Get: Cmdlets(self: CustomPSSnapIn) -> Collection[CmdletConfigurationEntry] """
        ...

    @property
    def Formats(self) -> Collection:
        """ Get: Formats(self: CustomPSSnapIn) -> Collection[FormatConfigurationEntry] """
        ...

    @property
    def Providers(self) -> Collection:
        """ Get: Providers(self: CustomPSSnapIn) -> Collection[ProviderConfigurationEntry] """
        ...

    @property
    def Types(self) -> Collection:
        """ Get: Types(self: CustomPSSnapIn) -> Collection[TypeConfigurationEntry] """
        ...



class DataAddedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: DataAddedEventArgs) -> int """
        ...

    @property
    def PowerShellInstanceId(self) -> Guid:
        """ Get: PowerShellInstanceId(self: DataAddedEventArgs) -> Guid """
        ...



class DataAddingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ItemAdded(self) -> object:
        """ Get: ItemAdded(self: DataAddingEventArgs) -> object """
        ...

    @property
    def PowerShellInstanceId(self) -> Guid:
        """ Get: PowerShellInstanceId(self: DataAddingEventArgs) -> Guid """
        ...



class Debugger: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DebuggerStopped(self):
        ...

    @property
    def DebugMode(self) -> DebugModes:
        """ Get: DebugMode(self: Debugger) -> DebugModes """
        ...

    @property
    def InBreakpoint(self) -> bool:
        """ Get: InBreakpoint(self: Debugger) -> bool """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: Debugger) -> Guid """
        ...

    @property
    def IsActive(self) -> bool:
        """ Get: IsActive(self: Debugger) -> bool """
        ...


    def GetCallStack(self) -> IEnumerable:
        """ GetCallStack(self: Debugger) -> IEnumerable[CallStackFrame] """
        ...

    def GetDebuggerStopArgs(self) -> DebuggerStopEventArgs:
        """ GetDebuggerStopArgs(self: Debugger) -> DebuggerStopEventArgs """
        ...

    def IsDebuggerBreakpointUpdatedEventSubscribed(self, *args): #cannot find CLR method
        """ IsDebuggerBreakpointUpdatedEventSubscribed(self: Debugger) -> bool """
        ...

    def IsDebuggerStopEventSubscribed(self, *args): #cannot find CLR method
        """ IsDebuggerStopEventSubscribed(self: Debugger) -> bool """
        ...

    def ProcessCommand(self, command:PSCommand, output:PSDataCollection) -> DebuggerCommandResults:
        """ ProcessCommand(self: Debugger, command: PSCommand, output: PSDataCollection[PSObject]) -> DebuggerCommandResults """
        ...

    def RaiseBreakpointUpdatedEvent(self, *args): #cannot find CLR method
        """ RaiseBreakpointUpdatedEvent(self: Debugger, args: BreakpointUpdatedEventArgs) """
        ...

    def RaiseDebuggerStopEvent(self, *args): #cannot find CLR method
        """ RaiseDebuggerStopEvent(self: Debugger, args: DebuggerStopEventArgs) """
        ...

    def ResetCommandProcessorSource(self): # -> 
        """ ResetCommandProcessorSource(self: Debugger) """
        ...

    def SetBreakpoints(self, breakpoints:IEnumerable): # -> 
        """ SetBreakpoints(self: Debugger, breakpoints: IEnumerable[Breakpoint]) """
        ...

    def SetDebuggerAction(self, resumeAction:DebuggerResumeAction): # -> 
        """ SetDebuggerAction(self: Debugger, resumeAction: DebuggerResumeAction) """
        ...

    def SetDebuggerStepMode(self, enabled:bool): # -> 
        """ SetDebuggerStepMode(self: Debugger, enabled: bool) """
        ...

    def SetDebugMode(self, mode:DebugModes): # -> 
        """ SetDebugMode(self: Debugger, mode: DebugModes) """
        ...

    def SetParent(self, parent:Debugger, breakPoints:IEnumerable, startAction:Nullable, host:PSHost, path:PathInfo, functionSourceMap:Dictionary = ...): # -> 
        """ SetParent(self: Debugger, parent: Debugger, breakPoints: IEnumerable[Breakpoint], startAction: Nullable[DebuggerResumeAction], host: PSHost, path: PathInfo)SetParent(self: Debugger, parent: Debugger, breakPoints: IEnumerable[Breakpoint], startAction: Nullable[DebuggerResumeAction], host: PSHost, path: PathInfo, functionSourceMap: Dictionary[str, DebugSource]) """
        ...

    def StopProcessCommand(self): # -> 
        """ StopProcessCommand(self: Debugger) """
        ...

    BreakpointUpdated = ...
    DebuggerStop = ...


class DebuggerCommandResults: # skipped bases: <type 'object'>, <type 'object'>
    """ DebuggerCommandResults(resumeAction: Nullable[DebuggerResumeAction], evaluatedByDebugger: bool) """
    @property
    def EvaluatedByDebugger(self) -> bool:
        """ Get: EvaluatedByDebugger(self: DebuggerCommandResults) -> bool """
        ...

    @property
    def ResumeAction(self) -> Nullable:
        """ Get: ResumeAction(self: DebuggerCommandResults) -> Nullable[DebuggerResumeAction] """
        ...



class DebuggerResumeAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DebuggerResumeAction, values: Continue (0), StepInto (1), StepOut (2), StepOver (3), Stop (4) """
    Continue: DebuggerResumeAction = ...
    StepInto: DebuggerResumeAction = ...
    StepOut: DebuggerResumeAction = ...
    StepOver: DebuggerResumeAction = ...
    Stop: DebuggerResumeAction = ...
    value__ = ...


class DebuggerStopEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DebuggerStopEventArgs(invocationInfo: InvocationInfo, breakpoints: Collection[Breakpoint], resumeAction: DebuggerResumeAction) """
    @property
    def Breakpoints(self) -> ReadOnlyCollection:
        """ Get: Breakpoints(self: DebuggerStopEventArgs) -> ReadOnlyCollection[Breakpoint] """
        ...

    @property
    def InvocationInfo(self) -> InvocationInfo:
        """ Get: InvocationInfo(self: DebuggerStopEventArgs) -> InvocationInfo """
        ...

    @property
    def ResumeAction(self) -> DebuggerResumeAction:
        """
        Get: ResumeAction(self: DebuggerStopEventArgs) -> DebuggerResumeAction
        Set: ResumeAction(self: DebuggerStopEventArgs) = value
        """
        ...


    def __new__(cls, invocationInfo:InvocationInfo, breakpoints:Collection, resumeAction:DebuggerResumeAction) -> Self:
        """ __new__(cls: type, invocationInfo: InvocationInfo, breakpoints: Collection[Breakpoint], resumeAction: DebuggerResumeAction) """
        ...


class DebugModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DebugModes, values: Default (1), LocalScript (2), None (0), RemoteScript (4) """
    Default: DebugModes = ...
    LocalScript: DebugModes = ...
    RemoteScript: DebugModes = ...
    value__ = ...


class InformationalRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InvocationInfo(self) -> InvocationInfo:
        """ Get: InvocationInfo(self: InformationalRecord) -> InvocationInfo """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: InformationalRecord) -> str
        Set: Message(self: InformationalRecord) = value
        """
        ...

    @property
    def PipelineIterationInfo(self) -> ReadOnlyCollection:
        """ Get: PipelineIterationInfo(self: InformationalRecord) -> ReadOnlyCollection[int] """
        ...


    def ToString(self) -> str:
        """ ToString(self: InformationalRecord) -> str """
        ...


class DebugRecord(InformationalRecord): # skipped bases: <type 'object'>
    """
    DebugRecord(message: str)
    DebugRecord(record: PSObject)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, message: str)
        __new__(cls: type, record: PSObject)
        """
        ...


class DebugSource: # skipped bases: <type 'object'>, <type 'object'>
    """ DebugSource(script: str, scriptFile: str, xamlDefinition: str) """
    @property
    def Script(self) -> str:
        """ Get: Script(self: DebugSource) -> str """
        ...

    @property
    def ScriptFile(self) -> str:
        """ Get: ScriptFile(self: DebugSource) -> str """
        ...

    @property
    def XamlDefinition(self) -> str:
        """ Get: XamlDefinition(self: DebugSource) -> str """
        ...



class DefaultParameterDictionary(Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """
    DefaultParameterDictionary()
    DefaultParameterDictionary(dictionary: IDictionary)
    """
    def ChangeSinceLastCheck(self) -> bool:
        """ ChangeSinceLastCheck(self: DefaultParameterDictionary) -> bool """
        ...


class DisplayEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ DisplayEntry(value: str, type: DisplayEntryValueType) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: DisplayEntry) -> str """
        ...

    @property
    def ValueType(self) -> DisplayEntryValueType:
        """ Get: ValueType(self: DisplayEntry) -> DisplayEntryValueType """
        ...


    def ToString(self) -> str:
        """ ToString(self: DisplayEntry) -> str """
        ...


class DisplayEntryValueType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DisplayEntryValueType, values: Property (0), ScriptBlock (1) """
    Property: DisplayEntryValueType = ...
    ScriptBlock: DisplayEntryValueType = ...
    value__ = ...


class DriveManagementIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> PSDriveInfo:
        """ Get: Current(self: DriveManagementIntrinsics) -> PSDriveInfo """
        ...


    def Get(self, driveName:str) -> PSDriveInfo:
        """ Get(self: DriveManagementIntrinsics, driveName: str) -> PSDriveInfo """
        ...

    def GetAll(self) -> Collection:
        """ GetAll(self: DriveManagementIntrinsics) -> Collection[PSDriveInfo] """
        ...

    def GetAllAtScope(self, scope:str) -> Collection:
        """ GetAllAtScope(self: DriveManagementIntrinsics, scope: str) -> Collection[PSDriveInfo] """
        ...

    def GetAllForProvider(self, providerName:str) -> Collection:
        """ GetAllForProvider(self: DriveManagementIntrinsics, providerName: str) -> Collection[PSDriveInfo] """
        ...

    def GetAtScope(self, driveName:str, scope:str) -> PSDriveInfo:
        """ GetAtScope(self: DriveManagementIntrinsics, driveName: str, scope: str) -> PSDriveInfo """
        ...

    def New(self, drive:PSDriveInfo, scope:str) -> PSDriveInfo:
        """ New(self: DriveManagementIntrinsics, drive: PSDriveInfo, scope: str) -> PSDriveInfo """
        ...

    def Remove(self, driveName:str, force:bool, scope:str): # -> 
        """ Remove(self: DriveManagementIntrinsics, driveName: str, force: bool, scope: str) """
        ...


class SessionStateException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SessionStateException()
    SessionStateException(message: str)
    SessionStateException(message: str, innerException: Exception)
    """
    @property
    def ItemName(self) -> str:
        """ Get: ItemName(self: SessionStateException) -> str """
        ...

    @property
    def SessionStateCategory(self) -> SessionStateCategory:
        """ Get: SessionStateCategory(self: SessionStateException) -> SessionStateCategory """
        ...


    SerializeObjectState = ...


class DriveNotFoundException(SessionStateException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DriveNotFoundException()
    DriveNotFoundException(message: str)
    DriveNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DscLocalConfigurationManagerAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DscLocalConfigurationManagerAttribute() """
    pass

class DscPropertyAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DscPropertyAttribute() """
    @property
    def Key(self) -> bool:
        """
        Get: Key(self: DscPropertyAttribute) -> bool
        Set: Key(self: DscPropertyAttribute) = value
        """
        ...

    @property
    def Mandatory(self) -> bool:
        """
        Get: Mandatory(self: DscPropertyAttribute) -> bool
        Set: Mandatory(self: DscPropertyAttribute) = value
        """
        ...

    @property
    def NotConfigurable(self) -> bool:
        """
        Get: NotConfigurable(self: DscPropertyAttribute) -> bool
        Set: NotConfigurable(self: DscPropertyAttribute) = value
        """
        ...



class DscResourceAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DscResourceAttribute() """
    @property
    def RunAsCredential(self) -> DSCResourceRunAsCredential:
        """
        Get: RunAsCredential(self: DscResourceAttribute) -> DSCResourceRunAsCredential
        Set: RunAsCredential(self: DscResourceAttribute) = value
        """
        ...



class DscResourceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CompanyName(self) -> str:
        """
        Get: CompanyName(self: DscResourceInfo) -> str
        Set: CompanyName(self: DscResourceInfo) = value
        """
        ...

    @property
    def FriendlyName(self) -> str:
        """
        Get: FriendlyName(self: DscResourceInfo) -> str
        Set: FriendlyName(self: DscResourceInfo) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: DscResourceInfo) -> str """
        ...

    @property
    def ImplementedAs(self) -> ImplementedAsType:
        """
        Get: ImplementedAs(self: DscResourceInfo) -> ImplementedAsType
        Set: ImplementedAs(self: DscResourceInfo) = value
        """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: DscResourceInfo) -> PSModuleInfo """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DscResourceInfo) -> str """
        ...

    @property
    def ParentPath(self) -> str:
        """
        Get: ParentPath(self: DscResourceInfo) -> str
        Set: ParentPath(self: DscResourceInfo) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: DscResourceInfo) -> str
        Set: Path(self: DscResourceInfo) = value
        """
        ...

    @property
    def Properties(self) -> ReadOnlyCollection:
        """ Get: Properties(self: DscResourceInfo) -> ReadOnlyCollection[DscResourcePropertyInfo] """
        ...

    @property
    def ResourceType(self) -> str:
        """
        Get: ResourceType(self: DscResourceInfo) -> str
        Set: ResourceType(self: DscResourceInfo) = value
        """
        ...


    def UpdateProperties(self, properties:IList): # -> 
        """ UpdateProperties(self: DscResourceInfo, properties: IList[DscResourcePropertyInfo]) """
        ...


class DscResourcePropertyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsMandatory(self) -> bool:
        """
        Get: IsMandatory(self: DscResourcePropertyInfo) -> bool
        Set: IsMandatory(self: DscResourcePropertyInfo) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DscResourcePropertyInfo) -> str
        Set: Name(self: DscResourcePropertyInfo) = value
        """
        ...

    @property
    def PropertyType(self) -> str:
        """
        Get: PropertyType(self: DscResourcePropertyInfo) -> str
        Set: PropertyType(self: DscResourcePropertyInfo) = value
        """
        ...

    @property
    def Values(self) -> ReadOnlyCollection:
        """ Get: Values(self: DscResourcePropertyInfo) -> ReadOnlyCollection[str] """
        ...



class DSCResourceRunAsCredential(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DSCResourceRunAsCredential, values: Default (0), Mandatory (2), NotSupported (1), Optional (0) """
    Default: DSCResourceRunAsCredential = ...
    Mandatory: DSCResourceRunAsCredential = ...
    NotSupported: DSCResourceRunAsCredential = ...
    Optional: DSCResourceRunAsCredential = ...
    value__ = ...


class DynamicClassImplementationAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DynamicClassImplementationAssemblyAttribute() """
    pass

class EngineIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Events(self) -> PSEventManager:
        """ Get: Events(self: EngineIntrinsics) -> PSEventManager """
        ...

    @property
    def Host(self) -> PSHost:
        """ Get: Host(self: EngineIntrinsics) -> PSHost """
        ...

    @property
    def InvokeCommand(self) -> CommandInvocationIntrinsics:
        """ Get: InvokeCommand(self: EngineIntrinsics) -> CommandInvocationIntrinsics """
        ...

    @property
    def InvokeProvider(self) -> ProviderIntrinsics:
        """ Get: InvokeProvider(self: EngineIntrinsics) -> ProviderIntrinsics """
        ...

    @property
    def SessionState(self) -> SessionState:
        """ Get: SessionState(self: EngineIntrinsics) -> SessionState """
        ...



class EntrySelectedBy: # skipped bases: <type 'object'>, <type 'object'>
    """ EntrySelectedBy() """
    @property
    def SelectionCondition(self) -> List:
        """
        Get: SelectionCondition(self: EntrySelectedBy) -> List[DisplayEntry]
        Set: SelectionCondition(self: EntrySelectedBy) = value
        """
        ...

    @property
    def TypeNames(self) -> List:
        """
        Get: TypeNames(self: EntrySelectedBy) -> List[str]
        Set: TypeNames(self: EntrySelectedBy) = value
        """
        ...



class ErrorCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ErrorCategory, values: AuthenticationError (28), CloseError (2), ConnectionError (27), DeadlockDetected (4), DeviceError (3), FromStdErr (24), InvalidArgument (5), InvalidData (6), InvalidOperation (7), InvalidResult (8), InvalidType (9), LimitsExceeded (29), MetadataError (10), NotEnabled (31), NotImplemented (11), NotInstalled (12), NotSpecified (0), ObjectNotFound (13), OpenError (1), OperationStopped (14), OperationTimeout (15), ParserError (17), PermissionDenied (18), ProtocolError (26), QuotaExceeded (30), ReadError (22), ResourceBusy (19), ResourceExists (20), ResourceUnavailable (21), SecurityError (25), SyntaxError (16), WriteError (23) """
    AuthenticationError: ErrorCategory = ...
    CloseError: ErrorCategory = ...
    ConnectionError: ErrorCategory = ...
    DeadlockDetected: ErrorCategory = ...
    DeviceError: ErrorCategory = ...
    FromStdErr: ErrorCategory = ...
    InvalidArgument: ErrorCategory = ...
    InvalidData: ErrorCategory = ...
    InvalidOperation: ErrorCategory = ...
    InvalidResult: ErrorCategory = ...
    InvalidType: ErrorCategory = ...
    LimitsExceeded: ErrorCategory = ...
    MetadataError: ErrorCategory = ...
    NotEnabled: ErrorCategory = ...
    NotImplemented: ErrorCategory = ...
    NotInstalled: ErrorCategory = ...
    NotSpecified: ErrorCategory = ...
    ObjectNotFound: ErrorCategory = ...
    OpenError: ErrorCategory = ...
    OperationStopped: ErrorCategory = ...
    OperationTimeout: ErrorCategory = ...
    ParserError: ErrorCategory = ...
    PermissionDenied: ErrorCategory = ...
    ProtocolError: ErrorCategory = ...
    QuotaExceeded: ErrorCategory = ...
    ReadError: ErrorCategory = ...
    ResourceBusy: ErrorCategory = ...
    ResourceExists: ErrorCategory = ...
    ResourceUnavailable: ErrorCategory = ...
    SecurityError: ErrorCategory = ...
    SyntaxError: ErrorCategory = ...
    value__ = ...
    WriteError: ErrorCategory = ...


class ErrorCategoryInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Activity(self) -> str:
        """
        Get: Activity(self: ErrorCategoryInfo) -> str
        Set: Activity(self: ErrorCategoryInfo) = value
        """
        ...

    @property
    def Category(self) -> ErrorCategory:
        """ Get: Category(self: ErrorCategoryInfo) -> ErrorCategory """
        ...

    @property
    def Reason(self) -> str:
        """
        Get: Reason(self: ErrorCategoryInfo) -> str
        Set: Reason(self: ErrorCategoryInfo) = value
        """
        ...

    @property
    def TargetName(self) -> str:
        """
        Get: TargetName(self: ErrorCategoryInfo) -> str
        Set: TargetName(self: ErrorCategoryInfo) = value
        """
        ...

    @property
    def TargetType(self) -> str:
        """
        Get: TargetType(self: ErrorCategoryInfo) -> str
        Set: TargetType(self: ErrorCategoryInfo) = value
        """
        ...


    def GetMessage(self, uiCultureInfo:CultureInfo = ...) -> str:
        """
        GetMessage(self: ErrorCategoryInfo) -> str
        GetMessage(self: ErrorCategoryInfo, uiCultureInfo: CultureInfo) -> str
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: ErrorCategoryInfo) -> str """
        ...


class ErrorDetails(ISerializable): # skipped bases: <type 'object'>
    """
    ErrorDetails(message: str)
    ErrorDetails(cmdlet: Cmdlet, baseName: str, resourceId: str, *args: Array[object])
    ErrorDetails(resourceSupplier: IResourceSupplier, baseName: str, resourceId: str, *args: Array[object])
    ErrorDetails(assembly: Assembly, baseName: str, resourceId: str, *args: Array[object])
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ErrorDetails) -> str """
        ...

    @property
    def RecommendedAction(self) -> str:
        """
        Get: RecommendedAction(self: ErrorDetails) -> str
        Set: RecommendedAction(self: ErrorDetails) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ErrorDetails) -> str """
        ...


class ErrorRecord(ISerializable): # skipped bases: <type 'object'>
    """
    ErrorRecord(exception: Exception, errorId: str, errorCategory: ErrorCategory, targetObject: object)
    ErrorRecord(errorRecord: ErrorRecord, replaceParentContainsErrorRecordException: Exception)
    """
    @property
    def CategoryInfo(self) -> ErrorCategoryInfo:
        """ Get: CategoryInfo(self: ErrorRecord) -> ErrorCategoryInfo """
        ...

    @property
    def ErrorDetails(self) -> ErrorDetails:
        """
        Get: ErrorDetails(self: ErrorRecord) -> ErrorDetails
        Set: ErrorDetails(self: ErrorRecord) = value
        """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ErrorRecord) -> Exception """
        ...

    @property
    def FullyQualifiedErrorId(self) -> str:
        """ Get: FullyQualifiedErrorId(self: ErrorRecord) -> str """
        ...

    @property
    def InvocationInfo(self) -> InvocationInfo:
        """ Get: InvocationInfo(self: ErrorRecord) -> InvocationInfo """
        ...

    @property
    def PipelineIterationInfo(self) -> ReadOnlyCollection:
        """ Get: PipelineIterationInfo(self: ErrorRecord) -> ReadOnlyCollection[int] """
        ...

    @property
    def ScriptStackTrace(self) -> str:
        """ Get: ScriptStackTrace(self: ErrorRecord) -> str """
        ...

    @property
    def TargetObject(self) -> object:
        """ Get: TargetObject(self: ErrorRecord) -> object """
        ...


    def ToString(self) -> str:
        """ ToString(self: ErrorRecord) -> str """
        ...


class ExitException(FlowControlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Argument(self) -> object:
        """ Get: Argument(self: ExitException) -> object """
        ...


    SerializeObjectState = ...


class ExtendedTypeDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """
    ExtendedTypeDefinition(typeName: str, viewDefinitions: IEnumerable[FormatViewDefinition])
    ExtendedTypeDefinition(typeName: str)
    """
    @property
    def FormatViewDefinition(self) -> List:
        """ Get: FormatViewDefinition(self: ExtendedTypeDefinition) -> List[FormatViewDefinition] """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ExtendedTypeDefinition) -> str """
        ...

    @property
    def TypeNames(self) -> List:
        """ Get: TypeNames(self: ExtendedTypeDefinition) -> List[str] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ExtendedTypeDefinition) -> str """
        ...


class ExtendedTypeSystemException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExtendedTypeSystemException()
    ExtendedTypeSystemException(message: str)
    ExtendedTypeSystemException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ExternalScriptInfo(CommandInfo, IScriptCommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    @property
    def OriginalEncoding(self) -> Encoding:
        """ Get: OriginalEncoding(self: ExternalScriptInfo) -> Encoding """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ExternalScriptInfo) -> str """
        ...

    @property
    def ScriptBlock(self) -> ScriptBlock:
        """ Get: ScriptBlock(self: ExternalScriptInfo) -> ScriptBlock """
        ...

    @property
    def ScriptContents(self) -> str:
        """ Get: ScriptContents(self: ExternalScriptInfo) -> str """
        ...


    def ValidateScriptInfo(self, host:PSHost): # -> 
        """ ValidateScriptInfo(self: ExternalScriptInfo, host: PSHost) """
        ...


class FilterInfo(FunctionInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'IScriptCommandInfo'>, <type 'object'>
    """ no doc """
    pass

class FlagsExpression: # skipped bases: <type 'object'>, <type 'object'>
    """
    FlagsExpression[T](expression: str)
    FlagsExpression[T](expression: Array[object])
    """
    def Evaluate(self, value) -> bool: # Not found arg types: {'value': 'T'}
        """ Evaluate(self: FlagsExpression[T], value: T) -> bool """
        ...


class FormatViewDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ FormatViewDefinition(name: str, control: PSControl) """
    @property
    def Control(self) -> PSControl:
        """ Get: Control(self: FormatViewDefinition) -> PSControl """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FormatViewDefinition) -> str """
        ...



class ForwardedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SerializedRemoteEventArgs(self) -> PSObject:
        """ Get: SerializedRemoteEventArgs(self: ForwardedEventArgs) -> PSObject """
        ...



class GetSymmetricEncryptionKey(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GetSymmetricEncryptionKey(object: object, method: IntPtr) """
    def BeginInvoke(self, context, key, iv, callback, object) -> Tuple_[IAsyncResult, Array, Array]:
        """ BeginInvoke(self: GetSymmetricEncryptionKey, context: StreamingContext, callback: AsyncCallback, object: object) -> (IAsyncResult, Array[Byte], Array[Byte]) """
        ...

    def EndInvoke(self, key, iv, result) -> Tuple_[bool, Array, Array]:
        """ EndInvoke(self: GetSymmetricEncryptionKey, result: IAsyncResult) -> (bool, Array[Byte], Array[Byte]) """
        ...

    def Invoke(self, context, key, iv) -> Tuple_[bool, Array, Array]:
        """ Invoke(self: GetSymmetricEncryptionKey, context: StreamingContext) -> (bool, Array[Byte], Array[Byte]) """
        ...


class GettingValueExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: GettingValueExceptionEventArgs) -> Exception """
        ...

    @property
    def ShouldThrow(self) -> bool:
        """
        Get: ShouldThrow(self: GettingValueExceptionEventArgs) -> bool
        Set: ShouldThrow(self: GettingValueExceptionEventArgs) = value
        """
        ...

    @property
    def ValueReplacement(self) -> object:
        """
        Get: ValueReplacement(self: GettingValueExceptionEventArgs) -> object
        Set: ValueReplacement(self: GettingValueExceptionEventArgs) = value
        """
        ...



class GetValueException(ExtendedTypeSystemException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    GetValueException()
    GetValueException(message: str)
    GetValueException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class GetValueInvocationException(GetValueException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    GetValueInvocationException()
    GetValueInvocationException(message: str)
    GetValueInvocationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class HaltCommandException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HaltCommandException()
    HaltCommandException(message: str)
    HaltCommandException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class HiddenAttribute(ParsingBaseAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HiddenAttribute() """
    pass

class HostInformationMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ HostInformationMessage() """
    @property
    def BackgroundColor(self) -> Nullable:
        """
        Get: BackgroundColor(self: HostInformationMessage) -> Nullable[ConsoleColor]
        Set: BackgroundColor(self: HostInformationMessage) = value
        """
        ...

    @property
    def ForegroundColor(self) -> Nullable:
        """
        Get: ForegroundColor(self: HostInformationMessage) -> Nullable[ConsoleColor]
        Set: ForegroundColor(self: HostInformationMessage) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: HostInformationMessage) -> str
        Set: Message(self: HostInformationMessage) = value
        """
        ...

    @property
    def NoNewLine(self) -> Nullable:
        """
        Get: NoNewLine(self: HostInformationMessage) -> Nullable[bool]
        Set: NoNewLine(self: HostInformationMessage) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: HostInformationMessage) -> str """
        ...


class HostUtilities: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    CreatePSEditFunction: str = ...
    PSEditFunction: str = ...
    RemoteSessionOpenFileEvent: str = ...
    RemovePSEditFunction: str = ...
    __all__: list = ...


class IArgumentCompleter: # skipped bases: <type 'object'>
    """ no doc """
    def CompleteArgument(self, commandName:str, parameterName:str, wordToComplete:str, commandAst:CommandAst, fakeBoundParameters:IDictionary) -> IEnumerable:
        """ CompleteArgument(self: IArgumentCompleter, commandName: str, parameterName: str, wordToComplete: str, commandAst: CommandAst, fakeBoundParameters: IDictionary) -> IEnumerable[CompletionResult] """
        ...


class IBackgroundDispatcher: # skipped bases: <type 'object'>
    """ no doc """
    def BeginInvoke(self, callback:WaitCallback, state:object, completionCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: IBackgroundDispatcher, callback: WaitCallback, state: object, completionCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, asyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: IBackgroundDispatcher, asyncResult: IAsyncResult) """
        ...

    def QueueUserWorkItem(self, callback:WaitCallback, state:object = ...) -> bool:
        """
        QueueUserWorkItem(self: IBackgroundDispatcher, callback: WaitCallback) -> bool
        QueueUserWorkItem(self: IBackgroundDispatcher, callback: WaitCallback, state: object) -> bool
        """
        ...


class ICommandRuntime: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentPSTransaction(self) -> PSTransactionContext:
        """ Get: CurrentPSTransaction(self: ICommandRuntime) -> PSTransactionContext """
        ...

    @property
    def Host(self) -> PSHost:
        """ Get: Host(self: ICommandRuntime) -> PSHost """
        ...


    def ShouldContinue(self, query:str, caption:str, yesToAll:bool = ..., noToAll:bool = ...) -> Tuple_[bool, bool, bool]:
        """
        ShouldContinue(self: ICommandRuntime, query: str, caption: str) -> bool
        ShouldContinue(self: ICommandRuntime, query: str, caption: str, yesToAll: bool, noToAll: bool) -> (bool, bool, bool)
        """
        ...

    def ShouldProcess(self, *__args:str) -> bool:
        """
        ShouldProcess(self: ICommandRuntime, target: str) -> bool
        ShouldProcess(self: ICommandRuntime, target: str, action: str) -> bool
        ShouldProcess(self: ICommandRuntime, verboseDescription: str, verboseWarning: str, caption: str) -> bool
        ShouldProcess(self: ICommandRuntime, verboseDescription: str, verboseWarning: str, caption: str) -> (bool, ShouldProcessReason)
        """
        ...

    def ThrowTerminatingError(self, errorRecord:ErrorRecord): # -> 
        """ ThrowTerminatingError(self: ICommandRuntime, errorRecord: ErrorRecord) """
        ...

    def TransactionAvailable(self) -> bool:
        """ TransactionAvailable(self: ICommandRuntime) -> bool """
        ...

    def WriteCommandDetail(self, text:str): # -> 
        """ WriteCommandDetail(self: ICommandRuntime, text: str) """
        ...

    def WriteDebug(self, text:str): # -> 
        """ WriteDebug(self: ICommandRuntime, text: str) """
        ...

    def WriteError(self, errorRecord:ErrorRecord): # -> 
        """ WriteError(self: ICommandRuntime, errorRecord: ErrorRecord) """
        ...

    def WriteObject(self, sendToPipeline:object, enumerateCollection:bool = ...): # -> 
        """ WriteObject(self: ICommandRuntime, sendToPipeline: object)WriteObject(self: ICommandRuntime, sendToPipeline: object, enumerateCollection: bool) """
        ...

    def WriteProgress(self, *__args:ProgressRecord): # -> 
        """ WriteProgress(self: ICommandRuntime, progressRecord: ProgressRecord)WriteProgress(self: ICommandRuntime, sourceId: Int64, progressRecord: ProgressRecord) """
        ...

    def WriteVerbose(self, text:str): # -> 
        """ WriteVerbose(self: ICommandRuntime, text: str) """
        ...

    def WriteWarning(self, text:str): # -> 
        """ WriteWarning(self: ICommandRuntime, text: str) """
        ...


class ICommandRuntime2(ICommandRuntime): # skipped bases: <type 'object'>
    """ no doc """
    def WriteInformation(self, informationRecord:InformationRecord): # -> 
        """ WriteInformation(self: ICommandRuntime2, informationRecord: InformationRecord) """
        ...


class IContainsErrorRecord: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorRecord(self) -> ErrorRecord:
        """ Get: ErrorRecord(self: IContainsErrorRecord) -> ErrorRecord """
        ...



class IDynamicParameters: # skipped bases: <type 'object'>
    """ no doc """
    def GetDynamicParameters(self) -> object:
        """ GetDynamicParameters(self: IDynamicParameters) -> object """
        ...


class IJobDebugger: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Debugger(self) -> Debugger:
        """ Get: Debugger(self: IJobDebugger) -> Debugger """
        ...

    @property
    def IsAsync(self) -> bool:
        """
        Get: IsAsync(self: IJobDebugger) -> bool
        Set: IsAsync(self: IJobDebugger) = value
        """
        ...



class IModuleAssemblyCleanup: # skipped bases: <type 'object'>
    """ no doc """
    def OnRemove(self, psModuleInfo:PSModuleInfo): # -> 
        """ OnRemove(self: IModuleAssemblyCleanup, psModuleInfo: PSModuleInfo) """
        ...


class IModuleAssemblyInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def OnImport(self): # -> 
        """ OnImport(self: IModuleAssemblyInitializer) """
        ...


class ImplementedAsType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImplementedAsType, values: Binary (2), Composite (3), None (0), PowerShell (1) """
    Binary: ImplementedAsType = ...
    Composite: ImplementedAsType = ...
    PowerShell: ImplementedAsType = ...
    value__ = ...


class ParseException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ParseException()
    ParseException(message: str)
    ParseException(message: str, innerException: Exception)
    ParseException(errors: Array[ParseError])
    """
    @property
    def Errors(self) -> Array:
        """ Get: Errors(self: ParseException) -> Array[ParseError] """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ParseException) -> str """
        ...


    SerializeObjectState = ...


class IncompleteParseException(ParseException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    IncompleteParseException()
    IncompleteParseException(message: str)
    IncompleteParseException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InformationRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ InformationRecord(messageData: object, source: str) """
    @property
    def Computer(self) -> str:
        """
        Get: Computer(self: InformationRecord) -> str
        Set: Computer(self: InformationRecord) = value
        """
        ...

    @property
    def ManagedThreadId(self) -> UInt32:
        """
        Get: ManagedThreadId(self: InformationRecord) -> UInt32
        Set: ManagedThreadId(self: InformationRecord) = value
        """
        ...

    @property
    def MessageData(self) -> object:
        """ Get: MessageData(self: InformationRecord) -> object """
        ...

    @property
    def NativeThreadId(self) -> UInt32:
        """
        Get: NativeThreadId(self: InformationRecord) -> UInt32
        Set: NativeThreadId(self: InformationRecord) = value
        """
        ...

    @property
    def ProcessId(self) -> UInt32:
        """
        Get: ProcessId(self: InformationRecord) -> UInt32
        Set: ProcessId(self: InformationRecord) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: InformationRecord) -> str
        Set: Source(self: InformationRecord) = value
        """
        ...

    @property
    def Tags(self) -> List:
        """ Get: Tags(self: InformationRecord) -> List[str] """
        ...

    @property
    def TimeGenerated(self) -> DateTime:
        """
        Get: TimeGenerated(self: InformationRecord) -> DateTime
        Set: TimeGenerated(self: InformationRecord) = value
        """
        ...

    @property
    def User(self) -> str:
        """
        Get: User(self: InformationRecord) -> str
        Set: User(self: InformationRecord) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: InformationRecord) -> str """
        ...


class InvalidJobStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidJobStateException()
    InvalidJobStateException(message: str)
    InvalidJobStateException(message: str, innerException: Exception)
    InvalidJobStateException(currentState: JobState, actionMessage: str)
    """
    @property
    def CurrentState(self) -> JobState:
        """ Get: CurrentState(self: InvalidJobStateException) -> JobState """
        ...


    SerializeObjectState = ...


class InvalidPowerShellStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidPowerShellStateException()
    InvalidPowerShellStateException(message: str)
    InvalidPowerShellStateException(message: str, innerException: Exception)
    """
    @property
    def CurrentState(self) -> PSInvocationState:
        """ Get: CurrentState(self: InvalidPowerShellStateException) -> PSInvocationState """
        ...


    SerializeObjectState = ...


class InvocationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BoundParameters(self) -> Dictionary:
        """ Get: BoundParameters(self: InvocationInfo) -> Dictionary[str, object] """
        ...

    @property
    def CommandOrigin(self) -> CommandOrigin:
        """ Get: CommandOrigin(self: InvocationInfo) -> CommandOrigin """
        ...

    @property
    def DisplayScriptPosition(self) -> IScriptExtent:
        """
        Get: DisplayScriptPosition(self: InvocationInfo) -> IScriptExtent
        Set: DisplayScriptPosition(self: InvocationInfo) = value
        """
        ...

    @property
    def ExpectingInput(self) -> bool:
        """ Get: ExpectingInput(self: InvocationInfo) -> bool """
        ...

    @property
    def HistoryId(self) -> Int64:
        """ Get: HistoryId(self: InvocationInfo) -> Int64 """
        ...

    @property
    def InvocationName(self) -> str:
        """ Get: InvocationName(self: InvocationInfo) -> str """
        ...

    @property
    def Line(self) -> str:
        """ Get: Line(self: InvocationInfo) -> str """
        ...

    @property
    def MyCommand(self) -> CommandInfo:
        """ Get: MyCommand(self: InvocationInfo) -> CommandInfo """
        ...

    @property
    def OffsetInLine(self) -> int:
        """ Get: OffsetInLine(self: InvocationInfo) -> int """
        ...

    @property
    def PipelineLength(self) -> int:
        """ Get: PipelineLength(self: InvocationInfo) -> int """
        ...

    @property
    def PipelinePosition(self) -> int:
        """ Get: PipelinePosition(self: InvocationInfo) -> int """
        ...

    @property
    def PositionMessage(self) -> str:
        """ Get: PositionMessage(self: InvocationInfo) -> str """
        ...

    @property
    def PSCommandPath(self) -> str:
        """ Get: PSCommandPath(self: InvocationInfo) -> str """
        ...

    @property
    def PSScriptRoot(self) -> str:
        """ Get: PSScriptRoot(self: InvocationInfo) -> str """
        ...

    @property
    def ScriptLineNumber(self) -> int:
        """ Get: ScriptLineNumber(self: InvocationInfo) -> int """
        ...

    @property
    def ScriptName(self) -> str:
        """ Get: ScriptName(self: InvocationInfo) -> str """
        ...

    @property
    def UnboundArguments(self) -> List:
        """ Get: UnboundArguments(self: InvocationInfo) -> List[object] """
        ...


    @staticmethod
    def Create(commandInfo:CommandInfo, scriptPosition:IScriptExtent) -> InvocationInfo:
        """ Create(commandInfo: CommandInfo, scriptPosition: IScriptExtent) -> InvocationInfo """
        ...


class IResourceSupplier: # skipped bases: <type 'object'>
    """ no doc """
    def GetResourceString(self, baseName:str, resourceId:str) -> str:
        """ GetResourceString(self: IResourceSupplier, baseName: str, resourceId: str) -> str """
        ...


class ItemCmdletProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clear(self, path:Array, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Clear(self: ItemCmdletProviderIntrinsics, path: Array[str], force: bool, literalPath: bool) -> Collection[PSObject]
        Clear(self: ItemCmdletProviderIntrinsics, path: str) -> Collection[PSObject]
        """
        ...

    def Copy(self, path:Array, destinationPath:str, recurse:bool, copyContainers:CopyContainers, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Copy(self: ItemCmdletProviderIntrinsics, path: Array[str], destinationPath: str, recurse: bool, copyContainers: CopyContainers, force: bool, literalPath: bool) -> Collection[PSObject]
        Copy(self: ItemCmdletProviderIntrinsics, path: str, destinationPath: str, recurse: bool, copyContainers: CopyContainers) -> Collection[PSObject]
        """
        ...

    def Exists(self, path:str, force:bool = ..., literalPath:bool = ...) -> bool:
        """
        Exists(self: ItemCmdletProviderIntrinsics, path: str) -> bool
        Exists(self: ItemCmdletProviderIntrinsics, path: str, force: bool, literalPath: bool) -> bool
        """
        ...

    def Get(self, path:Array, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Get(self: ItemCmdletProviderIntrinsics, path: Array[str], force: bool, literalPath: bool) -> Collection[PSObject]
        Get(self: ItemCmdletProviderIntrinsics, path: str) -> Collection[PSObject]
        """
        ...

    def Invoke(self, path:Array, literalPath:bool = ...): # -> 
        """ Invoke(self: ItemCmdletProviderIntrinsics, path: Array[str], literalPath: bool)Invoke(self: ItemCmdletProviderIntrinsics, path: str) """
        ...

    def IsContainer(self, path:str) -> bool:
        """ IsContainer(self: ItemCmdletProviderIntrinsics, path: str) -> bool """
        ...

    def Move(self, path:Array, destination:str, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Move(self: ItemCmdletProviderIntrinsics, path: Array[str], destination: str, force: bool, literalPath: bool) -> Collection[PSObject]
        Move(self: ItemCmdletProviderIntrinsics, path: str, destination: str) -> Collection[PSObject]
        """
        ...

    def New(self, path:Array, name:str, itemTypeName:str, content:object, force:bool = ...) -> Collection:
        """
        New(self: ItemCmdletProviderIntrinsics, path: Array[str], name: str, itemTypeName: str, content: object, force: bool) -> Collection[PSObject]
        New(self: ItemCmdletProviderIntrinsics, path: str, name: str, itemTypeName: str, content: object) -> Collection[PSObject]
        """
        ...

    def Remove(self, path:Array, recurse:bool, force:bool = ..., literalPath:bool = ...): # -> 
        """ Remove(self: ItemCmdletProviderIntrinsics, path: Array[str], recurse: bool, force: bool, literalPath: bool)Remove(self: ItemCmdletProviderIntrinsics, path: str, recurse: bool) """
        ...

    def Rename(self, path:str, newName:str, force:bool = ...) -> Collection:
        """
        Rename(self: ItemCmdletProviderIntrinsics, path: str, newName: str) -> Collection[PSObject]
        Rename(self: ItemCmdletProviderIntrinsics, path: str, newName: str, force: bool) -> Collection[PSObject]
        """
        ...

    def Set(self, path:Array, value:object, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Set(self: ItemCmdletProviderIntrinsics, path: Array[str], value: object, force: bool, literalPath: bool) -> Collection[PSObject]
        Set(self: ItemCmdletProviderIntrinsics, path: str, value: object) -> Collection[PSObject]
        """
        ...


class ItemNotFoundException(SessionStateException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ItemNotFoundException()
    ItemNotFoundException(message: str)
    ItemNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class JobDataAddedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataType(self) -> PowerShellStreamType:
        """ Get: DataType(self: JobDataAddedEventArgs) -> PowerShellStreamType """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: JobDataAddedEventArgs) -> int """
        ...

    @property
    def SourceJob(self) -> Job:
        """ Get: SourceJob(self: JobDataAddedEventArgs) -> Job """
        ...



class JobDefinition(ISerializable): # skipped bases: <type 'object'>
    """ JobDefinition(jobSourceAdapterType: Type, command: str, name: str) """
    @property
    def Command(self) -> str:
        """ Get: Command(self: JobDefinition) -> str """
        ...

    @property
    def CommandInfo(self) -> CommandInfo:
        """ Get: CommandInfo(self: JobDefinition) -> CommandInfo """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: JobDefinition) -> Guid
        Set: InstanceId(self: JobDefinition) = value
        """
        ...

    @property
    def JobSourceAdapterType(self) -> Type:
        """ Get: JobSourceAdapterType(self: JobDefinition) -> Type """
        ...

    @property
    def JobSourceAdapterTypeName(self) -> str:
        """
        Get: JobSourceAdapterTypeName(self: JobDefinition) -> str
        Set: JobSourceAdapterTypeName(self: JobDefinition) = value
        """
        ...

    @property
    def ModuleName(self) -> str:
        """
        Get: ModuleName(self: JobDefinition) -> str
        Set: ModuleName(self: JobDefinition) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: JobDefinition) -> str
        Set: Name(self: JobDefinition) = value
        """
        ...


    def Load(self, stream:Stream): # -> 
        """ Load(self: JobDefinition, stream: Stream) """
        ...

    def Save(self, stream:Stream): # -> 
        """ Save(self: JobDefinition, stream: Stream) """
        ...


class JobFailedException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    JobFailedException()
    JobFailedException(message: str)
    JobFailedException(message: str, innerException: Exception)
    JobFailedException(innerException: Exception, displayScriptPosition: ScriptExtent)
    """
    @property
    def DisplayScriptPosition(self) -> ScriptExtent:
        """ Get: DisplayScriptPosition(self: JobFailedException) -> ScriptExtent """
        ...

    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: JobFailedException) -> Exception """
        ...


    SerializeObjectState = ...


class JobIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class JobInvocationInfo(ISerializable): # skipped bases: <type 'object'>
    """
    JobInvocationInfo(definition: JobDefinition, parameters: Dictionary[str, object])
    JobInvocationInfo(definition: JobDefinition, parameterCollectionList: IEnumerable[Dictionary[str, object]])
    JobInvocationInfo(definition: JobDefinition, parameters: CommandParameterCollection)
    JobInvocationInfo(definition: JobDefinition, parameters: IEnumerable[CommandParameterCollection])
    """
    @property
    def Command(self) -> str:
        """
        Get: Command(self: JobInvocationInfo) -> str
        Set: Command(self: JobInvocationInfo) = value
        """
        ...

    @property
    def Definition(self) -> JobDefinition:
        """
        Get: Definition(self: JobInvocationInfo) -> JobDefinition
        Set: Definition(self: JobInvocationInfo) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: JobInvocationInfo) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: JobInvocationInfo) -> str
        Set: Name(self: JobInvocationInfo) = value
        """
        ...

    @property
    def Parameters(self) -> List:
        """ Get: Parameters(self: JobInvocationInfo) -> List[CommandParameterCollection] """
        ...


    def Load(self, stream:Stream): # -> 
        """ Load(self: JobInvocationInfo, stream: Stream) """
        ...

    def Save(self, stream:Stream): # -> 
        """ Save(self: JobInvocationInfo, stream: Stream) """
        ...


class JobManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def IsRegistered(self, typeName:str) -> bool:
        """ IsRegistered(self: JobManager, typeName: str) -> bool """
        ...

    def NewJob(self, *__args:JobDefinition) -> Job2:
        """
        NewJob(self: JobManager, definition: JobDefinition) -> Job2
        NewJob(self: JobManager, specification: JobInvocationInfo) -> Job2
        """
        ...

    def PersistJob(self, job:Job2, definition:JobDefinition): # -> 
        """ PersistJob(self: JobManager, job: Job2, definition: JobDefinition) """
        ...


class JobRepository(Repository): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Jobs(self) -> List:
        """ Get: Jobs(self: JobRepository) -> List[Job] """
        ...


    def GetJob(self, instanceId:Guid) -> Job:
        """ GetJob(self: JobRepository, instanceId: Guid) -> Job """
        ...


class JobSourceAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: JobSourceAdapter) -> str
        Set: Name(self: JobSourceAdapter) = value
        """
        ...


    def GetJobByInstanceId(self, instanceId:Guid, recurse:bool) -> Job2:
        """ GetJobByInstanceId(self: JobSourceAdapter, instanceId: Guid, recurse: bool) -> Job2 """
        ...

    def GetJobBySessionId(self, id:int, recurse:bool) -> Job2:
        """ GetJobBySessionId(self: JobSourceAdapter, id: int, recurse: bool) -> Job2 """
        ...

    def GetJobs(self) -> IList:
        """ GetJobs(self: JobSourceAdapter) -> IList[Job2] """
        ...

    def GetJobsByCommand(self, command:str, recurse:bool) -> IList:
        """ GetJobsByCommand(self: JobSourceAdapter, command: str, recurse: bool) -> IList[Job2] """
        ...

    def GetJobsByFilter(self, filter:Dictionary, recurse:bool) -> IList:
        """ GetJobsByFilter(self: JobSourceAdapter, filter: Dictionary[str, object], recurse: bool) -> IList[Job2] """
        ...

    def GetJobsByName(self, name:str, recurse:bool) -> IList:
        """ GetJobsByName(self: JobSourceAdapter, name: str, recurse: bool) -> IList[Job2] """
        ...

    def GetJobsByState(self, state:JobState, recurse:bool) -> IList:
        """ GetJobsByState(self: JobSourceAdapter, state: JobState, recurse: bool) -> IList[Job2] """
        ...

    def NewJob(self, *__args:JobDefinition) -> Job2:
        """
        NewJob(self: JobSourceAdapter, definitionName: str, definitionPath: str) -> Job2
        NewJob(self: JobSourceAdapter, definition: JobDefinition) -> Job2
        NewJob(self: JobSourceAdapter, specification: JobInvocationInfo) -> Job2
        """
        ...

    def PersistJob(self, job:Job2): # -> 
        """ PersistJob(self: JobSourceAdapter, job: Job2) """
        ...

    def RemoveJob(self, job:Job2): # -> 
        """ RemoveJob(self: JobSourceAdapter, job: Job2) """
        ...

    def RetrieveJobIdForReuse(self, *args): #cannot find CLR method
        """ RetrieveJobIdForReuse(self: JobSourceAdapter, instanceId: Guid) -> JobIdentifier """
        ...

    def StoreJobIdForReuse(self, job:Job2, recurse:bool): # -> 
        """ StoreJobIdForReuse(self: JobSourceAdapter, job: Job2, recurse: bool) """
        ...


class JobState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobState, values: AtBreakpoint (10), Blocked (5), Completed (2), Disconnected (7), Failed (3), NotStarted (0), Running (1), Stopped (4), Stopping (9), Suspended (6), Suspending (8) """
    AtBreakpoint: JobState = ...
    Blocked: JobState = ...
    Completed: JobState = ...
    Disconnected: JobState = ...
    Failed: JobState = ...
    NotStarted: JobState = ...
    Running: JobState = ...
    Stopped: JobState = ...
    Stopping: JobState = ...
    Suspended: JobState = ...
    Suspending: JobState = ...
    value__ = ...


class JobStateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    JobStateEventArgs(jobStateInfo: JobStateInfo)
    JobStateEventArgs(jobStateInfo: JobStateInfo, previousJobStateInfo: JobStateInfo)
    """
    @property
    def JobStateInfo(self) -> JobStateInfo:
        """ Get: JobStateInfo(self: JobStateEventArgs) -> JobStateInfo """
        ...

    @property
    def PreviousJobStateInfo(self) -> JobStateInfo:
        """ Get: PreviousJobStateInfo(self: JobStateEventArgs) -> JobStateInfo """
        ...


    def __new__(cls, jobStateInfo:JobStateInfo, previousJobStateInfo:JobStateInfo = ...) -> Self:
        """
        __new__(cls: type, jobStateInfo: JobStateInfo)
        __new__(cls: type, jobStateInfo: JobStateInfo, previousJobStateInfo: JobStateInfo)
        """
        ...


class JobStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    JobStateInfo(state: JobState)
    JobStateInfo(state: JobState, reason: Exception)
    """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: JobStateInfo) -> Exception """
        ...

    @property
    def State(self) -> JobState:
        """ Get: State(self: JobStateInfo) -> JobState """
        ...


    def ToString(self) -> str:
        """ ToString(self: JobStateInfo) -> str """
        ...


class JobThreadOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobThreadOptions, values: Default (0), UseNewThread (2), UseThreadPoolThread (1) """
    Default: JobThreadOptions = ...
    UseNewThread: JobThreadOptions = ...
    UseThreadPoolThread: JobThreadOptions = ...
    value__ = ...


class LanguagePrimitives: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Compare(first:object, second:object, ignoreCase:bool = ..., formatProvider:IFormatProvider = ...) -> int:
        """
        Compare(first: object, second: object) -> int
        Compare(first: object, second: object, ignoreCase: bool) -> int
        Compare(first: object, second: object, ignoreCase: bool, formatProvider: IFormatProvider) -> int
        """
        ...

    @staticmethod
    def ConvertPSObjectToType(valueToConvert:PSObject, resultType:Type, recursion:bool, formatProvider:IFormatProvider, ignoreUnknownMembers:bool) -> object:
        """ ConvertPSObjectToType(valueToConvert: PSObject, resultType: Type, recursion: bool, formatProvider: IFormatProvider, ignoreUnknownMembers: bool) -> object """
        ...

    @staticmethod
    def ConvertTo(valueToConvert:object, resultType:Type = ..., formatProvider:IFormatProvider = ...) -> object:
        """
        ConvertTo(valueToConvert: object, resultType: Type) -> object
        ConvertTo(valueToConvert: object, resultType: Type, formatProvider: IFormatProvider) -> object
        ConvertTo[T](valueToConvert: object) -> T
        """
        ...

    @staticmethod
    def ConvertTypeNameToPSTypeName(typeName:str) -> str:
        """ ConvertTypeNameToPSTypeName(typeName: str) -> str """
        ...

    @staticmethod
    def Equals(*__args) -> bool:
        """
        Equals(first: object, second: object) -> bool
        Equals(first: object, second: object, ignoreCase: bool) -> bool
        Equals(first: object, second: object, ignoreCase: bool, formatProvider: IFormatProvider) -> bool
        """
        ...

    @staticmethod
    def GetEnumerable(obj:object) -> IEnumerable:
        """ GetEnumerable(obj: object) -> IEnumerable """
        ...

    @staticmethod
    def GetEnumerator(obj:object) -> IEnumerator:
        """ GetEnumerator(obj: object) -> IEnumerator """
        ...

    @staticmethod
    def GetPSDataCollection(inputValue:object) -> PSDataCollection:
        """ GetPSDataCollection(inputValue: object) -> PSDataCollection[PSObject] """
        ...

    @staticmethod
    def IsTrue(obj:object) -> bool:
        """ IsTrue(obj: object) -> bool """
        ...

    @staticmethod
    def TryConvertTo(valueToConvert:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryConvertTo(valueToConvert: object, resultType: Type) -> (bool, object)
        TryConvertTo(valueToConvert: object, resultType: Type, formatProvider: IFormatProvider) -> (bool, object)
        TryConvertTo[T](valueToConvert: object) -> (bool, T)
        TryConvertTo[T](valueToConvert: object, formatProvider: IFormatProvider) -> (bool, T)
        """
        ...

    __all__: list = ...


class LineBreakpoint(Breakpoint): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Column(self) -> int:
        """ Get: Column(self: LineBreakpoint) -> int """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: LineBreakpoint) -> int """
        ...


    def ToString(self) -> str:
        """ ToString(self: LineBreakpoint) -> str """
        ...


class ListControl(PSControl): # skipped bases: <type 'object'>
    """
    ListControl()
    ListControl(entries: IEnumerable[ListControlEntry])
    """
    @property
    def Entries(self) -> List:
        """ Get: Entries(self: ListControl) -> List[ListControlEntry] """
        ...


    @staticmethod
    def Create(outOfBand:bool) -> ListControlBuilder:
        """ Create(outOfBand: bool) -> ListControlBuilder """
        ...

    def __new__(cls, entries:IEnumerable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, entries: IEnumerable[ListControlEntry])
        """
        ...


class ListControlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def EndList(self) -> ListControl:
        """ EndList(self: ListControlBuilder) -> ListControl """
        ...

    def GroupByProperty(self, property:str, customControl:CustomControl, label:str) -> ListControlBuilder:
        """ GroupByProperty(self: ListControlBuilder, property: str, customControl: CustomControl, label: str) -> ListControlBuilder """
        ...

    def GroupByScriptBlock(self, scriptBlock:str, customControl:CustomControl, label:str) -> ListControlBuilder:
        """ GroupByScriptBlock(self: ListControlBuilder, scriptBlock: str, customControl: CustomControl, label: str) -> ListControlBuilder """
        ...

    def StartEntry(self, entrySelectedByType:IEnumerable, entrySelectedByCondition:IEnumerable) -> ListEntryBuilder:
        """ StartEntry(self: ListControlBuilder, entrySelectedByType: IEnumerable[str], entrySelectedByCondition: IEnumerable[DisplayEntry]) -> ListEntryBuilder """
        ...


class ListControlEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    ListControlEntry()
    ListControlEntry(listItems: IEnumerable[ListControlEntryItem])
    ListControlEntry(listItems: IEnumerable[ListControlEntryItem], selectedBy: IEnumerable[str])
    """
    @property
    def EntrySelectedBy(self) -> EntrySelectedBy:
        """ Get: EntrySelectedBy(self: ListControlEntry) -> EntrySelectedBy """
        ...

    @property
    def Items(self) -> List:
        """ Get: Items(self: ListControlEntry) -> List[ListControlEntryItem] """
        ...

    @property
    def SelectedBy(self) -> List:
        """ Get: SelectedBy(self: ListControlEntry) -> List[str] """
        ...



class ListControlEntryItem: # skipped bases: <type 'object'>, <type 'object'>
    """ ListControlEntryItem(label: str, entry: DisplayEntry) """
    @property
    def DisplayEntry(self) -> DisplayEntry:
        """ Get: DisplayEntry(self: ListControlEntryItem) -> DisplayEntry """
        ...

    @property
    def FormatString(self) -> str:
        """ Get: FormatString(self: ListControlEntryItem) -> str """
        ...

    @property
    def ItemSelectionCondition(self) -> DisplayEntry:
        """ Get: ItemSelectionCondition(self: ListControlEntryItem) -> DisplayEntry """
        ...

    @property
    def Label(self) -> str:
        """ Get: Label(self: ListControlEntryItem) -> str """
        ...



class ListEntryBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddItemProperty(self, property:str, label:str, format:str) -> ListEntryBuilder:
        """ AddItemProperty(self: ListEntryBuilder, property: str, label: str, format: str) -> ListEntryBuilder """
        ...

    def AddItemScriptBlock(self, scriptBlock:str, label:str, format:str) -> ListEntryBuilder:
        """ AddItemScriptBlock(self: ListEntryBuilder, scriptBlock: str, label: str, format: str) -> ListEntryBuilder """
        ...

    def EndEntry(self) -> ListControlBuilder:
        """ EndEntry(self: ListEntryBuilder) -> ListControlBuilder """
        ...


class MethodException(ExtendedTypeSystemException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MethodException()
    MethodException(message: str)
    MethodException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MethodInvocationException(MethodException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MethodInvocationException()
    MethodInvocationException(message: str)
    MethodInvocationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ModuleAccessMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ModuleAccessMode, values: Constant (2), ReadOnly (1), ReadWrite (0) """
    Constant: ModuleAccessMode = ...
    ReadOnly: ModuleAccessMode = ...
    ReadWrite: ModuleAccessMode = ...
    value__ = ...


class ModuleIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetModulePath(currentProcessModulePath:str, hklmMachineModulePath:str, hkcuUserModulePath:str) -> str:
        """ GetModulePath(currentProcessModulePath: str, hklmMachineModulePath: str, hkcuUserModulePath: str) -> str """
        ...


class ModuleType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ModuleType, values: Binary (1), Cim (3), Manifest (2), Script (0), Workflow (4) """
    Binary: ModuleType = ...
    Cim: ModuleType = ...
    Manifest: ModuleType = ...
    Script: ModuleType = ...
    value__ = ...
    Workflow: ModuleType = ...


class OutputTypeAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    OutputTypeAttribute(*type: Array[Type])
    OutputTypeAttribute(*type: Array[str])
    """
    @property
    def ParameterSetName(self) -> Array:
        """
        Get: ParameterSetName(self: OutputTypeAttribute) -> Array[str]
        Set: ParameterSetName(self: OutputTypeAttribute) = value
        """
        ...

    @property
    def ProviderCmdlet(self) -> str:
        """
        Get: ProviderCmdlet(self: OutputTypeAttribute) -> str
        Set: ProviderCmdlet(self: OutputTypeAttribute) = value
        """
        ...

    @property
    def Type(self) -> Array:
        """ Get: Type(self: OutputTypeAttribute) -> Array[PSTypeName] """
        ...


    def __new__(cls, type:Array) -> Self:
        """
        __new__(cls: type, *type: Array[Type])
        __new__(cls: type, *type: Array[str])
        """
        ...


class PagingParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def First(self) -> UInt64:
        """
        Get: First(self: PagingParameters) -> UInt64
        Set: First(self: PagingParameters) = value
        """
        ...

    @property
    def IncludeTotalCount(self) -> SwitchParameter:
        """
        Get: IncludeTotalCount(self: PagingParameters) -> SwitchParameter
        Set: IncludeTotalCount(self: PagingParameters) = value
        """
        ...

    @property
    def Skip(self) -> UInt64:
        """
        Get: Skip(self: PagingParameters) -> UInt64
        Set: Skip(self: PagingParameters) = value
        """
        ...


    def NewTotalCount(self, totalCount:UInt64, accuracy:float) -> PSObject:
        """ NewTotalCount(self: PagingParameters, totalCount: UInt64, accuracy: float) -> PSObject """
        ...


class ParameterAttribute(ParsingBaseAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ParameterAttribute() """
    @property
    def DontShow(self) -> bool:
        """
        Get: DontShow(self: ParameterAttribute) -> bool
        Set: DontShow(self: ParameterAttribute) = value
        """
        ...

    @property
    def HelpMessage(self) -> str:
        """
        Get: HelpMessage(self: ParameterAttribute) -> str
        Set: HelpMessage(self: ParameterAttribute) = value
        """
        ...

    @property
    def HelpMessageBaseName(self) -> str:
        """
        Get: HelpMessageBaseName(self: ParameterAttribute) -> str
        Set: HelpMessageBaseName(self: ParameterAttribute) = value
        """
        ...

    @property
    def HelpMessageResourceId(self) -> str:
        """
        Get: HelpMessageResourceId(self: ParameterAttribute) -> str
        Set: HelpMessageResourceId(self: ParameterAttribute) = value
        """
        ...

    @property
    def Mandatory(self) -> bool:
        """
        Get: Mandatory(self: ParameterAttribute) -> bool
        Set: Mandatory(self: ParameterAttribute) = value
        """
        ...

    @property
    def ParameterSetName(self) -> str:
        """
        Get: ParameterSetName(self: ParameterAttribute) -> str
        Set: ParameterSetName(self: ParameterAttribute) = value
        """
        ...

    @property
    def Position(self) -> int:
        """
        Get: Position(self: ParameterAttribute) -> int
        Set: Position(self: ParameterAttribute) = value
        """
        ...

    @property
    def ValueFromPipeline(self) -> bool:
        """
        Get: ValueFromPipeline(self: ParameterAttribute) -> bool
        Set: ValueFromPipeline(self: ParameterAttribute) = value
        """
        ...

    @property
    def ValueFromPipelineByPropertyName(self) -> bool:
        """
        Get: ValueFromPipelineByPropertyName(self: ParameterAttribute) -> bool
        Set: ValueFromPipelineByPropertyName(self: ParameterAttribute) = value
        """
        ...

    @property
    def ValueFromRemainingArguments(self) -> bool:
        """
        Get: ValueFromRemainingArguments(self: ParameterAttribute) -> bool
        Set: ValueFromRemainingArguments(self: ParameterAttribute) = value
        """
        ...


    AllParameterSets: str = ...


class ParameterBindingException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ParameterBindingException()
    ParameterBindingException(message: str)
    ParameterBindingException(message: str, innerException: Exception)
    """
    @property
    def CommandInvocation(self) -> InvocationInfo:
        """ Get: CommandInvocation(self: ParameterBindingException) -> InvocationInfo """
        ...

    @property
    def ErrorId(self) -> str:
        """ Get: ErrorId(self: ParameterBindingException) -> str """
        ...

    @property
    def Line(self) -> Int64:
        """ Get: Line(self: ParameterBindingException) -> Int64 """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ParameterBindingException) -> str """
        ...

    @property
    def Offset(self) -> Int64:
        """ Get: Offset(self: ParameterBindingException) -> Int64 """
        ...

    @property
    def ParameterName(self) -> str:
        """ Get: ParameterName(self: ParameterBindingException) -> str """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: ParameterBindingException) -> Type """
        ...

    @property
    def TypeSpecified(self) -> Type:
        """ Get: TypeSpecified(self: ParameterBindingException) -> Type """
        ...


    SerializeObjectState = ...


class ParameterMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """
    ParameterMetadata(name: str)
    ParameterMetadata(name: str, parameterType: Type)
    ParameterMetadata(other: ParameterMetadata)
    """
    @property
    def Aliases(self) -> Collection:
        """ Get: Aliases(self: ParameterMetadata) -> Collection[str] """
        ...

    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: ParameterMetadata) -> Collection[Attribute] """
        ...

    @property
    def IsDynamic(self) -> bool:
        """
        Get: IsDynamic(self: ParameterMetadata) -> bool
        Set: IsDynamic(self: ParameterMetadata) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ParameterMetadata) -> str
        Set: Name(self: ParameterMetadata) = value
        """
        ...

    @property
    def ParameterSets(self) -> Dictionary:
        """ Get: ParameterSets(self: ParameterMetadata) -> Dictionary[str, ParameterSetMetadata] """
        ...

    @property
    def ParameterType(self) -> Type:
        """
        Get: ParameterType(self: ParameterMetadata) -> Type
        Set: ParameterType(self: ParameterMetadata) = value
        """
        ...

    @property
    def SwitchParameter(self) -> bool:
        """ Get: SwitchParameter(self: ParameterMetadata) -> bool """
        ...


    @staticmethod
    def GetParameterMetadata(type:Type) -> Dictionary:
        """ GetParameterMetadata(type: Type) -> Dictionary[str, ParameterMetadata] """
        ...


class ParameterSetMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HelpMessage(self) -> str:
        """
        Get: HelpMessage(self: ParameterSetMetadata) -> str
        Set: HelpMessage(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def HelpMessageBaseName(self) -> str:
        """
        Get: HelpMessageBaseName(self: ParameterSetMetadata) -> str
        Set: HelpMessageBaseName(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def HelpMessageResourceId(self) -> str:
        """
        Get: HelpMessageResourceId(self: ParameterSetMetadata) -> str
        Set: HelpMessageResourceId(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def IsMandatory(self) -> bool:
        """
        Get: IsMandatory(self: ParameterSetMetadata) -> bool
        Set: IsMandatory(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def Position(self) -> int:
        """
        Get: Position(self: ParameterSetMetadata) -> int
        Set: Position(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def ValueFromPipeline(self) -> bool:
        """
        Get: ValueFromPipeline(self: ParameterSetMetadata) -> bool
        Set: ValueFromPipeline(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def ValueFromPipelineByPropertyName(self) -> bool:
        """
        Get: ValueFromPipelineByPropertyName(self: ParameterSetMetadata) -> bool
        Set: ValueFromPipelineByPropertyName(self: ParameterSetMetadata) = value
        """
        ...

    @property
    def ValueFromRemainingArguments(self) -> bool:
        """
        Get: ValueFromRemainingArguments(self: ParameterSetMetadata) -> bool
        Set: ValueFromRemainingArguments(self: ParameterSetMetadata) = value
        """
        ...



class ParentContainsErrorRecordException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ParentContainsErrorRecordException(wrapperException: Exception)
    ParentContainsErrorRecordException(message: str)
    ParentContainsErrorRecordException()
    ParentContainsErrorRecordException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ParsingMetadataException(MetadataException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ParsingMetadataException()
    ParsingMetadataException(message: str)
    ParsingMetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PathInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Drive(self) -> PSDriveInfo:
        """ Get: Drive(self: PathInfo) -> PSDriveInfo """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: PathInfo) -> str """
        ...

    @property
    def Provider(self) -> ProviderInfo:
        """ Get: Provider(self: PathInfo) -> ProviderInfo """
        ...

    @property
    def ProviderPath(self) -> str:
        """ Get: ProviderPath(self: PathInfo) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: PathInfo) -> str """
        ...


class PathInfoStack(Stack): # skipped bases: <type 'IEnumerable[PathInfo]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IReadOnlyCollection[PathInfo]'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PathInfoStack) -> str """
        ...



class PathIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentFileSystemLocation(self) -> PathInfo:
        """ Get: CurrentFileSystemLocation(self: PathIntrinsics) -> PathInfo """
        ...

    @property
    def CurrentLocation(self) -> PathInfo:
        """ Get: CurrentLocation(self: PathIntrinsics) -> PathInfo """
        ...


    def Combine(self, parent:str, child:str) -> str:
        """ Combine(self: PathIntrinsics, parent: str, child: str) -> str """
        ...

    def CurrentProviderLocation(self, providerName:str) -> PathInfo:
        """ CurrentProviderLocation(self: PathIntrinsics, providerName: str) -> PathInfo """
        ...

    def GetResolvedProviderPathFromProviderPath(self, path:str, providerId:str) -> Collection:
        """ GetResolvedProviderPathFromProviderPath(self: PathIntrinsics, path: str, providerId: str) -> Collection[str] """
        ...

    def GetResolvedProviderPathFromPSPath(self, path, provider) -> Tuple_[Collection, ProviderInfo]:
        """ GetResolvedProviderPathFromPSPath(self: PathIntrinsics, path: str) -> (Collection[str], ProviderInfo) """
        ...

    def GetResolvedPSPathFromPSPath(self, path:str) -> Collection:
        """ GetResolvedPSPathFromPSPath(self: PathIntrinsics, path: str) -> Collection[PathInfo] """
        ...

    def GetUnresolvedProviderPathFromPSPath(self, path, provider=None, drive=None) -> str:
        """
        GetUnresolvedProviderPathFromPSPath(self: PathIntrinsics, path: str) -> str
        GetUnresolvedProviderPathFromPSPath(self: PathIntrinsics, path: str) -> (str, ProviderInfo, PSDriveInfo)
        """
        ...

    def IsProviderQualified(self, path:str) -> bool:
        """ IsProviderQualified(self: PathIntrinsics, path: str) -> bool """
        ...

    def IsPSAbsolute(self, path, driveName) -> Tuple_[bool, str]:
        """ IsPSAbsolute(self: PathIntrinsics, path: str) -> (bool, str) """
        ...

    def IsValid(self, path:str) -> bool:
        """ IsValid(self: PathIntrinsics, path: str) -> bool """
        ...

    def LocationStack(self, stackName:str) -> PathInfoStack:
        """ LocationStack(self: PathIntrinsics, stackName: str) -> PathInfoStack """
        ...

    def NormalizeRelativePath(self, path:str, basePath:str) -> str:
        """ NormalizeRelativePath(self: PathIntrinsics, path: str, basePath: str) -> str """
        ...

    def ParseChildName(self, path:str) -> str:
        """ ParseChildName(self: PathIntrinsics, path: str) -> str """
        ...

    def ParseParent(self, path:str, root:str) -> str:
        """ ParseParent(self: PathIntrinsics, path: str, root: str) -> str """
        ...

    def PopLocation(self, stackName:str) -> PathInfo:
        """ PopLocation(self: PathIntrinsics, stackName: str) -> PathInfo """
        ...

    def PushCurrentLocation(self, stackName:str): # -> 
        """ PushCurrentLocation(self: PathIntrinsics, stackName: str) """
        ...

    def SetDefaultLocationStack(self, stackName:str) -> PathInfoStack:
        """ SetDefaultLocationStack(self: PathIntrinsics, stackName: str) -> PathInfoStack """
        ...

    def SetLocation(self, path:str) -> PathInfo:
        """ SetLocation(self: PathIntrinsics, path: str) -> PathInfo """
        ...


class PipelineClosedException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PipelineClosedException()
    PipelineClosedException(message: str)
    PipelineClosedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PipelineDepthException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PipelineDepthException()
    PipelineDepthException(message: str)
    PipelineDepthException(message: str, innerException: Exception)
    """
    @property
    def CallDepth(self) -> int:
        """ Get: CallDepth(self: PipelineDepthException) -> int """
        ...


    SerializeObjectState = ...


class PipelineStoppedException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PipelineStoppedException()
    PipelineStoppedException(message: str)
    PipelineStoppedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PowerShell(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Commands(self) -> PSCommand:
        """
        Get: Commands(self: PowerShell) -> PSCommand
        Set: Commands(self: PowerShell) = value
        """
        ...

    @property
    def HadErrors(self) -> bool:
        """ Get: HadErrors(self: PowerShell) -> bool """
        ...

    @property
    def HistoryString(self) -> str:
        """
        Get: HistoryString(self: PowerShell) -> str
        Set: HistoryString(self: PowerShell) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: PowerShell) -> Guid """
        ...

    @property
    def InvocationStateInfo(self) -> PSInvocationStateInfo:
        """ Get: InvocationStateInfo(self: PowerShell) -> PSInvocationStateInfo """
        ...

    @property
    def IsNested(self) -> bool:
        """ Get: IsNested(self: PowerShell) -> bool """
        ...

    @property
    def IsRunspaceOwner(self) -> bool:
        """ Get: IsRunspaceOwner(self: PowerShell) -> bool """
        ...

    @property
    def Runspace(self) -> Runspace:
        """
        Get: Runspace(self: PowerShell) -> Runspace
        Set: Runspace(self: PowerShell) = value
        """
        ...

    @property
    def RunspacePool(self) -> RunspacePool:
        """
        Get: RunspacePool(self: PowerShell) -> RunspacePool
        Set: RunspacePool(self: PowerShell) = value
        """
        ...

    @property
    def Streams(self) -> PSDataStreams:
        """ Get: Streams(self: PowerShell) -> PSDataStreams """
        ...


    def AddArgument(self, value:object) -> PowerShell:
        """ AddArgument(self: PowerShell, value: object) -> PowerShell """
        ...

    def AddCommand(self, *__args:str) -> PowerShell:
        """
        AddCommand(self: PowerShell, cmdlet: str) -> PowerShell
        AddCommand(self: PowerShell, cmdlet: str, useLocalScope: bool) -> PowerShell
        AddCommand(self: PowerShell, commandInfo: CommandInfo) -> PowerShell
        """
        ...

    def AddParameter(self, parameterName:str, value:object = ...) -> PowerShell:
        """
        AddParameter(self: PowerShell, parameterName: str, value: object) -> PowerShell
        AddParameter(self: PowerShell, parameterName: str) -> PowerShell
        """
        ...

    def AddParameters(self, parameters:IList) -> PowerShell:
        """
        AddParameters(self: PowerShell, parameters: IList) -> PowerShell
        AddParameters(self: PowerShell, parameters: IDictionary) -> PowerShell
        """
        ...

    def AddScript(self, script:str, useLocalScope:bool = ...) -> PowerShell:
        """
        AddScript(self: PowerShell, script: str) -> PowerShell
        AddScript(self: PowerShell, script: str, useLocalScope: bool) -> PowerShell
        """
        ...

    def AddStatement(self) -> PowerShell:
        """ AddStatement(self: PowerShell) -> PowerShell """
        ...

    def AsJobProxy(self) -> PSJobProxy:
        """ AsJobProxy(self: PowerShell) -> PSJobProxy """
        ...

    def BeginInvoke(self, input:PSDataCollection = ..., *__args:PSDataCollection) -> IAsyncResult:
        """
        BeginInvoke(self: PowerShell) -> IAsyncResult
        BeginInvoke[T](self: PowerShell, input: PSDataCollection[T]) -> IAsyncResult
        BeginInvoke[T](self: PowerShell, input: PSDataCollection[T], settings: PSInvocationSettings, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginInvoke[(TInput, TOutput)](self: PowerShell, input: PSDataCollection[TInput], output: PSDataCollection[TOutput]) -> IAsyncResult
        BeginInvoke[(TInput, TOutput)](self: PowerShell, input: PSDataCollection[TInput], output: PSDataCollection[TOutput], settings: PSInvocationSettings, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginStop(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginStop(self: PowerShell, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Connect(self) -> Collection:
        """ Connect(self: PowerShell) -> Collection[PSObject] """
        ...

    def ConnectAsync(self, output:PSDataCollection = ..., invocationCallback:AsyncCallback = ..., state:object = ...) -> IAsyncResult:
        """
        ConnectAsync(self: PowerShell) -> IAsyncResult
        ConnectAsync(self: PowerShell, output: PSDataCollection[PSObject], invocationCallback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def Create(*__args) -> PowerShell:
        """
        Create() -> PowerShell
        Create(runspace: RunspaceMode) -> PowerShell
        Create(initialSessionState: InitialSessionState) -> PowerShell
        """
        ...

    def CreateNestedPowerShell(self) -> PowerShell:
        """ CreateNestedPowerShell(self: PowerShell) -> PowerShell """
        ...

    def EndInvoke(self, asyncResult:IAsyncResult) -> PSDataCollection:
        """ EndInvoke(self: PowerShell, asyncResult: IAsyncResult) -> PSDataCollection[PSObject] """
        ...

    def EndStop(self, asyncResult:IAsyncResult): # -> 
        """ EndStop(self: PowerShell, asyncResult: IAsyncResult) """
        ...

    def Invoke(self, input:IEnumerable = ..., *__args:PSInvocationSettings) -> Collection:
        """
        Invoke(self: PowerShell) -> Collection[PSObject]
        Invoke(self: PowerShell, input: IEnumerable) -> Collection[PSObject]
        Invoke(self: PowerShell, input: IEnumerable, settings: PSInvocationSettings) -> Collection[PSObject]
        Invoke[T](self: PowerShell) -> Collection[T]
        Invoke[T](self: PowerShell, input: IEnumerable) -> Collection[T]
        Invoke[T](self: PowerShell, input: IEnumerable, settings: PSInvocationSettings) -> Collection[T]
        Invoke[T](self: PowerShell, input: IEnumerable, output: IList[T])Invoke[T](self: PowerShell, input: IEnumerable, output: IList[T], settings: PSInvocationSettings)Invoke[(TInput, TOutput)](self: PowerShell, input: PSDataCollection[TInput], output: PSDataCollection[TOutput], settings: PSInvocationSettings)
        """
        ...

    def Stop(self): # -> 
        """ Stop(self: PowerShell) """
        ...

    InvocationStateChanged = ...


class PowerShellStreams(IDisposable): # skipped bases: <type 'object'>
    """
    PowerShellStreams[TInput, TOutput]()
    PowerShellStreams[TInput, TOutput](pipelineInput: PSDataCollection[TInput])
    """
    @property
    def DebugStream(self) -> PSDataCollection:
        """
        Get: DebugStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[DebugRecord]
        Set: DebugStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def ErrorStream(self) -> PSDataCollection:
        """
        Get: ErrorStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[ErrorRecord]
        Set: ErrorStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def InformationStream(self) -> PSDataCollection:
        """
        Get: InformationStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[InformationRecord]
        Set: InformationStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def InputStream(self) -> PSDataCollection:
        """
        Get: InputStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[TInput]
        Set: InputStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def OutputStream(self) -> PSDataCollection:
        """
        Get: OutputStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[TOutput]
        Set: OutputStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def ProgressStream(self) -> PSDataCollection:
        """
        Get: ProgressStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[ProgressRecord]
        Set: ProgressStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def VerboseStream(self) -> PSDataCollection:
        """
        Get: VerboseStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[VerboseRecord]
        Set: VerboseStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...

    @property
    def WarningStream(self) -> PSDataCollection:
        """
        Get: WarningStream(self: PowerShellStreams[TInput, TOutput]) -> PSDataCollection[WarningRecord]
        Set: WarningStream(self: PowerShellStreams[TInput, TOutput]) = value
        """
        ...


    def CloseAll(self): # -> 
        """ CloseAll(self: PowerShellStreams[TInput, TOutput]) """
        ...


class PowerShellStreamType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerShellStreamType, values: Debug (5), Error (2), Information (7), Input (0), Output (1), Progress (6), Verbose (4), Warning (3) """
    Debug: PowerShellStreamType = ...
    Error: PowerShellStreamType = ...
    Information: PowerShellStreamType = ...
    Input: PowerShellStreamType = ...
    Output: PowerShellStreamType = ...
    Progress: PowerShellStreamType = ...
    value__ = ...
    Verbose: PowerShellStreamType = ...
    Warning: PowerShellStreamType = ...


class ProgressRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ ProgressRecord(activityId: int, activity: str, statusDescription: str) """
    @property
    def Activity(self) -> str:
        """
        Get: Activity(self: ProgressRecord) -> str
        Set: Activity(self: ProgressRecord) = value
        """
        ...

    @property
    def ActivityId(self) -> int:
        """ Get: ActivityId(self: ProgressRecord) -> int """
        ...

    @property
    def CurrentOperation(self) -> str:
        """
        Get: CurrentOperation(self: ProgressRecord) -> str
        Set: CurrentOperation(self: ProgressRecord) = value
        """
        ...

    @property
    def ParentActivityId(self) -> int:
        """
        Get: ParentActivityId(self: ProgressRecord) -> int
        Set: ParentActivityId(self: ProgressRecord) = value
        """
        ...

    @property
    def PercentComplete(self) -> int:
        """
        Get: PercentComplete(self: ProgressRecord) -> int
        Set: PercentComplete(self: ProgressRecord) = value
        """
        ...

    @property
    def RecordType(self) -> ProgressRecordType:
        """
        Get: RecordType(self: ProgressRecord) -> ProgressRecordType
        Set: RecordType(self: ProgressRecord) = value
        """
        ...

    @property
    def SecondsRemaining(self) -> int:
        """
        Get: SecondsRemaining(self: ProgressRecord) -> int
        Set: SecondsRemaining(self: ProgressRecord) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: ProgressRecord) -> str
        Set: StatusDescription(self: ProgressRecord) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ProgressRecord) -> str """
        ...


class ProgressRecordType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProgressRecordType, values: Completed (1), Processing (0) """
    Completed: ProgressRecordType = ...
    Processing: ProgressRecordType = ...
    value__ = ...


class PropertyCmdletProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clear(self, path:Array, propertyToClear:Collection, force:bool = ..., literalPath:bool = ...): # -> 
        """ Clear(self: PropertyCmdletProviderIntrinsics, path: Array[str], propertyToClear: Collection[str], force: bool, literalPath: bool)Clear(self: PropertyCmdletProviderIntrinsics, path: str, propertyToClear: Collection[str]) """
        ...

    def Copy(self, sourcePath:Array, sourceProperty:str, destinationPath:str, destinationProperty:str, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Copy(self: PropertyCmdletProviderIntrinsics, sourcePath: Array[str], sourceProperty: str, destinationPath: str, destinationProperty: str, force: bool, literalPath: bool) -> Collection[PSObject]
        Copy(self: PropertyCmdletProviderIntrinsics, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) -> Collection[PSObject]
        """
        ...

    def Get(self, path:Array, providerSpecificPickList:Collection, literalPath:bool = ...) -> Collection:
        """
        Get(self: PropertyCmdletProviderIntrinsics, path: Array[str], providerSpecificPickList: Collection[str], literalPath: bool) -> Collection[PSObject]
        Get(self: PropertyCmdletProviderIntrinsics, path: str, providerSpecificPickList: Collection[str]) -> Collection[PSObject]
        """
        ...

    def Move(self, sourcePath:Array, sourceProperty:str, destinationPath:str, destinationProperty:str, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Move(self: PropertyCmdletProviderIntrinsics, sourcePath: Array[str], sourceProperty: str, destinationPath: str, destinationProperty: str, force: bool, literalPath: bool) -> Collection[PSObject]
        Move(self: PropertyCmdletProviderIntrinsics, sourcePath: str, sourceProperty: str, destinationPath: str, destinationProperty: str) -> Collection[PSObject]
        """
        ...

    def New(self, path:Array, propertyName:str, propertyTypeName:str, value:object, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        New(self: PropertyCmdletProviderIntrinsics, path: Array[str], propertyName: str, propertyTypeName: str, value: object, force: bool, literalPath: bool) -> Collection[PSObject]
        New(self: PropertyCmdletProviderIntrinsics, path: str, propertyName: str, propertyTypeName: str, value: object) -> Collection[PSObject]
        """
        ...

    def Remove(self, path:Array, propertyName:str, force:bool = ..., literalPath:bool = ...): # -> 
        """ Remove(self: PropertyCmdletProviderIntrinsics, path: Array[str], propertyName: str, force: bool, literalPath: bool)Remove(self: PropertyCmdletProviderIntrinsics, path: str, propertyName: str) """
        ...

    def Rename(self, path:Array, sourceProperty:str, destinationProperty:str, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Rename(self: PropertyCmdletProviderIntrinsics, path: Array[str], sourceProperty: str, destinationProperty: str, force: bool, literalPath: bool) -> Collection[PSObject]
        Rename(self: PropertyCmdletProviderIntrinsics, path: str, sourceProperty: str, destinationProperty: str) -> Collection[PSObject]
        """
        ...

    def Set(self, path:Array, propertyValue:PSObject, force:bool = ..., literalPath:bool = ...) -> Collection:
        """
        Set(self: PropertyCmdletProviderIntrinsics, path: Array[str], propertyValue: PSObject, force: bool, literalPath: bool) -> Collection[PSObject]
        Set(self: PropertyCmdletProviderIntrinsics, path: str, propertyValue: PSObject) -> Collection[PSObject]
        """
        ...


class PropertyNotFoundException(ExtendedTypeSystemException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PropertyNotFoundException()
    PropertyNotFoundException(message: str)
    PropertyNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ProviderCmdlet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    AddContent: str = ...
    ClearContent: str = ...
    ClearItem: str = ...
    ClearItemProperty: str = ...
    ConvertPath: str = ...
    CopyItem: str = ...
    CopyItemProperty: str = ...
    GetAcl: str = ...
    GetChildItem: str = ...
    GetContent: str = ...
    GetItem: str = ...
    GetItemProperty: str = ...
    GetLocation: str = ...
    GetPSDrive: str = ...
    GetPSProvider: str = ...
    InvokeItem: str = ...
    JoinPath: str = ...
    MoveItem: str = ...
    MoveItemProperty: str = ...
    NewItem: str = ...
    NewItemProperty: str = ...
    NewPSDrive: str = ...
    PopLocation: str = ...
    PushLocation: str = ...
    RemoveItem: str = ...
    RemoveItemProperty: str = ...
    RemovePSDrive: str = ...
    RenameItem: str = ...
    RenameItemProperty: str = ...
    ResolvePath: str = ...
    SetAcl: str = ...
    SetContent: str = ...
    SetItem: str = ...
    SetItemProperty: str = ...
    SetLocation: str = ...
    SplitPath: str = ...
    TestPath: str = ...
    __all__: list = ...


class ProviderInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> ProviderCapabilities:
        """ Get: Capabilities(self: ProviderInfo) -> ProviderCapabilities """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ProviderInfo) -> str
        Set: Description(self: ProviderInfo) = value
        """
        ...

    @property
    def Drives(self) -> Collection:
        """ Get: Drives(self: ProviderInfo) -> Collection[PSDriveInfo] """
        ...

    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: ProviderInfo) -> str """
        ...

    @property
    def Home(self) -> str:
        """
        Get: Home(self: ProviderInfo) -> str
        Set: Home(self: ProviderInfo) = value
        """
        ...

    @property
    def ImplementingType(self) -> Type:
        """ Get: ImplementingType(self: ProviderInfo) -> Type """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: ProviderInfo) -> PSModuleInfo """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: ProviderInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ProviderInfo) -> str """
        ...

    @property
    def PSSnapIn(self) -> PSSnapInInfo:
        """ Get: PSSnapIn(self: ProviderInfo) -> PSSnapInInfo """
        ...


    def ToString(self) -> str:
        """ ToString(self: ProviderInfo) -> str """
        ...


class ProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ChildItem(self) -> ChildItemCmdletProviderIntrinsics:
        """ Get: ChildItem(self: ProviderIntrinsics) -> ChildItemCmdletProviderIntrinsics """
        ...

    @property
    def Content(self) -> ContentCmdletProviderIntrinsics:
        """ Get: Content(self: ProviderIntrinsics) -> ContentCmdletProviderIntrinsics """
        ...

    @property
    def Item(self) -> ItemCmdletProviderIntrinsics:
        """ Get: Item(self: ProviderIntrinsics) -> ItemCmdletProviderIntrinsics """
        ...

    @property
    def Property(self) -> PropertyCmdletProviderIntrinsics:
        """ Get: Property(self: ProviderIntrinsics) -> PropertyCmdletProviderIntrinsics """
        ...

    @property
    def SecurityDescriptor(self) -> SecurityDescriptorCmdletProviderIntrinsics:
        """ Get: SecurityDescriptor(self: ProviderIntrinsics) -> SecurityDescriptorCmdletProviderIntrinsics """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ProviderInvocationException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProviderInvocationException()
    ProviderInvocationException(message: str)
    ProviderInvocationException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ProviderInvocationException) -> str """
        ...

    @property
    def ProviderInfo(self) -> ProviderInfo:
        """ Get: ProviderInfo(self: ProviderInvocationException) -> ProviderInfo """
        ...


    SerializeObjectState = ...


class ProviderNotFoundException(SessionStateException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProviderNotFoundException()
    ProviderNotFoundException(message: str)
    ProviderNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ProviderNameAmbiguousException(ProviderNotFoundException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProviderNameAmbiguousException()
    ProviderNameAmbiguousException(message: str)
    ProviderNameAmbiguousException(message: str, innerException: Exception)
    """
    @property
    def PossibleMatches(self) -> ReadOnlyCollection:
        """ Get: PossibleMatches(self: ProviderNameAmbiguousException) -> ReadOnlyCollection[ProviderInfo] """
        ...


    SerializeObjectState = ...


class ProxyCommand: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(commandMetadata:CommandMetadata, helpComment:str = ..., generateDynamicParameters:bool = ...) -> str:
        """
        Create(commandMetadata: CommandMetadata) -> str
        Create(commandMetadata: CommandMetadata, helpComment: str) -> str
        Create(commandMetadata: CommandMetadata, helpComment: str, generateDynamicParameters: bool) -> str
        """
        ...

    @staticmethod
    def GetBegin(commandMetadata:CommandMetadata) -> str:
        """ GetBegin(commandMetadata: CommandMetadata) -> str """
        ...

    @staticmethod
    def GetCmdletBindingAttribute(commandMetadata:CommandMetadata) -> str:
        """ GetCmdletBindingAttribute(commandMetadata: CommandMetadata) -> str """
        ...

    @staticmethod
    def GetDynamicParam(commandMetadata:CommandMetadata) -> str:
        """ GetDynamicParam(commandMetadata: CommandMetadata) -> str """
        ...

    @staticmethod
    def GetEnd(commandMetadata:CommandMetadata) -> str:
        """ GetEnd(commandMetadata: CommandMetadata) -> str """
        ...

    @staticmethod
    def GetHelpComments(help:PSObject) -> str:
        """ GetHelpComments(help: PSObject) -> str """
        ...

    @staticmethod
    def GetParamBlock(commandMetadata:CommandMetadata) -> str:
        """ GetParamBlock(commandMetadata: CommandMetadata) -> str """
        ...

    @staticmethod
    def GetProcess(commandMetadata:CommandMetadata) -> str:
        """ GetProcess(commandMetadata: CommandMetadata) -> str """
        ...


class PSMemberInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsInstance(self) -> bool:
        """ Get: IsInstance(self: PSMemberInfo) -> bool """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSMemberInfo) -> PSMemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSMemberInfo) -> str """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSMemberInfo) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSMemberInfo) -> object
        Set: Value(self: PSMemberInfo) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSMemberInfo) -> PSMemberInfo """
        ...

    def SetMemberName(self, *args): #cannot find CLR method
        """ SetMemberName(self: PSMemberInfo, name: str) """
        ...


class PSPropertyInfo(PSMemberInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsGettable(self) -> bool:
        """ Get: IsGettable(self: PSPropertyInfo) -> bool """
        ...

    @property
    def IsSettable(self) -> bool:
        """ Get: IsSettable(self: PSPropertyInfo) -> bool """
        ...



class PSProperty(PSPropertyInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSProperty) -> PSMemberTypes """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSProperty) -> object
        Set: Value(self: PSProperty) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSProperty) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSProperty) -> str """
        ...


class PSAdaptedProperty(PSProperty): # skipped bases: <type 'object'>
    """ PSAdaptedProperty(name: str, tag: object) """
    @property
    def BaseObject(self) -> object:
        """ Get: BaseObject(self: PSAdaptedProperty) -> object """
        ...

    @property
    def Tag(self) -> object:
        """ Get: Tag(self: PSAdaptedProperty) -> object """
        ...


    def __new__(cls, name:str, tag:object) -> Self:
        """ __new__(cls: type, name: str, tag: object) """
        ...


class PSAliasProperty(PSPropertyInfo): # skipped bases: <type 'object'>
    """
    PSAliasProperty(name: str, referencedMemberName: str)
    PSAliasProperty(name: str, referencedMemberName: str, conversionType: Type)
    """
    @property
    def ConversionType(self) -> Type:
        """ Get: ConversionType(self: PSAliasProperty) -> Type """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSAliasProperty) -> PSMemberTypes """
        ...

    @property
    def ReferencedMemberName(self) -> str:
        """ Get: ReferencedMemberName(self: PSAliasProperty) -> str """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSAliasProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSAliasProperty) -> object
        Set: Value(self: PSAliasProperty) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSAliasProperty) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSAliasProperty) -> str """
        ...

    def __new__(cls, name:str, referencedMemberName:str, conversionType:Type = ...) -> Self:
        """
        __new__(cls: type, name: str, referencedMemberName: str)
        __new__(cls: type, name: str, referencedMemberName: str, conversionType: Type)
        """
        ...


class PSArgumentException(ArgumentException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSArgumentException()
    PSArgumentException(message: str)
    PSArgumentException(message: str, paramName: str)
    PSArgumentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PSArgumentNullException(IContainsErrorRecord, ArgumentNullException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSArgumentNullException()
    PSArgumentNullException(paramName: str)
    PSArgumentNullException(message: str, innerException: Exception)
    PSArgumentNullException(paramName: str, message: str)
    """
    SerializeObjectState = ...


class PSArgumentOutOfRangeException(ArgumentOutOfRangeException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSArgumentOutOfRangeException()
    PSArgumentOutOfRangeException(paramName: str)
    PSArgumentOutOfRangeException(paramName: str, actualValue: object, message: str)
    PSArgumentOutOfRangeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PSChildJobProxy(Job2): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def HasMoreData(self) -> bool:
        """ Get: HasMoreData(self: PSChildJobProxy) -> bool """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: PSChildJobProxy) -> str """
        ...

    @property
    def StatusMessage(self) -> str:
        """ Get: StatusMessage(self: PSChildJobProxy) -> str """
        ...


    JobDataAdded = ...


class PSClassInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HelpFile(self) -> str:
        """ Get: HelpFile(self: PSClassInfo) -> str """
        ...

    @property
    def Members(self) -> ReadOnlyCollection:
        """ Get: Members(self: PSClassInfo) -> ReadOnlyCollection[PSClassMemberInfo] """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: PSClassInfo) -> PSModuleInfo """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSClassInfo) -> str """
        ...


    def UpdateMembers(self, members:IList): # -> 
        """ UpdateMembers(self: PSClassInfo, members: IList[PSClassMemberInfo]) """
        ...


class PSClassMemberInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: PSClassMemberInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSClassMemberInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: PSClassMemberInfo) -> str """
        ...



class PSCmdlet(Cmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Events(self) -> PSEventManager:
        """ Get: Events(self: PSCmdlet) -> PSEventManager """
        ...

    @property
    def Host(self) -> PSHost:
        """ Get: Host(self: PSCmdlet) -> PSHost """
        ...

    @property
    def InvokeCommand(self) -> CommandInvocationIntrinsics:
        """ Get: InvokeCommand(self: PSCmdlet) -> CommandInvocationIntrinsics """
        ...

    @property
    def InvokeProvider(self) -> ProviderIntrinsics:
        """ Get: InvokeProvider(self: PSCmdlet) -> ProviderIntrinsics """
        ...

    @property
    def JobManager(self) -> JobManager:
        """ Get: JobManager(self: PSCmdlet) -> JobManager """
        ...

    @property
    def JobRepository(self) -> JobRepository:
        """ Get: JobRepository(self: PSCmdlet) -> JobRepository """
        ...

    @property
    def MyInvocation(self) -> InvocationInfo:
        """ Get: MyInvocation(self: PSCmdlet) -> InvocationInfo """
        ...

    @property
    def PagingParameters(self) -> PagingParameters:
        """ Get: PagingParameters(self: PSCmdlet) -> PagingParameters """
        ...

    @property
    def ParameterSetName(self) -> str:
        """ Get: ParameterSetName(self: PSCmdlet) -> str """
        ...

    @property
    def SessionState(self) -> SessionState:
        """ Get: SessionState(self: PSCmdlet) -> SessionState """
        ...


    def CurrentProviderLocation(self, providerId:str) -> PathInfo:
        """ CurrentProviderLocation(self: PSCmdlet, providerId: str) -> PathInfo """
        ...

    def GetResolvedProviderPathFromPSPath(self, path, provider) -> Tuple_[Collection, ProviderInfo]:
        """ GetResolvedProviderPathFromPSPath(self: PSCmdlet, path: str) -> (Collection[str], ProviderInfo) """
        ...

    def GetUnresolvedProviderPathFromPSPath(self, path:str) -> str:
        """ GetUnresolvedProviderPathFromPSPath(self: PSCmdlet, path: str) -> str """
        ...

    def GetVariableValue(self, name:str, defaultValue:object = ...) -> object:
        """
        GetVariableValue(self: PSCmdlet, name: str) -> object
        GetVariableValue(self: PSCmdlet, name: str, defaultValue: object) -> object
        """
        ...


class PSMethodInfo(PSMemberInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OverloadDefinitions(self) -> Collection:
        """ Get: OverloadDefinitions(self: PSMethodInfo) -> Collection[str] """
        ...


    def Invoke(self, arguments:Array) -> object:
        """ Invoke(self: PSMethodInfo, *arguments: Array[object]) -> object """
        ...


class PSCodeMethod(PSMethodInfo): # skipped bases: <type 'object'>
    """ PSCodeMethod(name: str, codeReference: MethodInfo) """
    @property
    def CodeReference(self) -> MethodInfo:
        """ Get: CodeReference(self: PSCodeMethod) -> MethodInfo """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSCodeMethod) -> PSMemberTypes """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSCodeMethod) -> str """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSCodeMethod) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSCodeMethod) -> str """
        ...

    def __new__(cls, name:str, codeReference:MethodInfo) -> Self:
        """ __new__(cls: type, name: str, codeReference: MethodInfo) """
        ...


class PSCodeProperty(PSPropertyInfo): # skipped bases: <type 'object'>
    """
    PSCodeProperty(name: str, getterCodeReference: MethodInfo)
    PSCodeProperty(name: str, getterCodeReference: MethodInfo, setterCodeReference: MethodInfo)
    """
    @property
    def GetterCodeReference(self) -> MethodInfo:
        """ Get: GetterCodeReference(self: PSCodeProperty) -> MethodInfo """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSCodeProperty) -> PSMemberTypes """
        ...

    @property
    def SetterCodeReference(self) -> MethodInfo:
        """ Get: SetterCodeReference(self: PSCodeProperty) -> MethodInfo """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSCodeProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSCodeProperty) -> object
        Set: Value(self: PSCodeProperty) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSCodeProperty) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSCodeProperty) -> str """
        ...

    def __new__(cls, name:str, getterCodeReference:MethodInfo, setterCodeReference:MethodInfo = ...) -> Self:
        """
        __new__(cls: type, name: str, getterCodeReference: MethodInfo)
        __new__(cls: type, name: str, getterCodeReference: MethodInfo, setterCodeReference: MethodInfo)
        """
        ...


class PSCommand: # skipped bases: <type 'object'>, <type 'object'>
    """ PSCommand() """
    @property
    def Commands(self) -> CommandCollection:
        """ Get: Commands(self: PSCommand) -> CommandCollection """
        ...


    def AddArgument(self, value:object) -> PSCommand:
        """ AddArgument(self: PSCommand, value: object) -> PSCommand """
        ...

    def AddCommand(self, *__args:Command) -> PSCommand:
        """
        AddCommand(self: PSCommand, cmdlet: str, useLocalScope: bool) -> PSCommand
        AddCommand(self: PSCommand, command: Command) -> PSCommand
        AddCommand(self: PSCommand, command: str) -> PSCommand
        """
        ...

    def AddParameter(self, parameterName:str, value:object = ...) -> PSCommand:
        """
        AddParameter(self: PSCommand, parameterName: str, value: object) -> PSCommand
        AddParameter(self: PSCommand, parameterName: str) -> PSCommand
        """
        ...

    def AddScript(self, script:str, useLocalScope:bool = ...) -> PSCommand:
        """
        AddScript(self: PSCommand, script: str, useLocalScope: bool) -> PSCommand
        AddScript(self: PSCommand, script: str) -> PSCommand
        """
        ...

    def AddStatement(self) -> PSCommand:
        """ AddStatement(self: PSCommand) -> PSCommand """
        ...

    def Clear(self): # -> 
        """ Clear(self: PSCommand) """
        ...

    def Clone(self) -> PSCommand:
        """ Clone(self: PSCommand) -> PSCommand """
        ...


class PSControlGroupBy: # skipped bases: <type 'object'>, <type 'object'>
    """ PSControlGroupBy() """
    @property
    def CustomControl(self) -> CustomControl:
        """
        Get: CustomControl(self: PSControlGroupBy) -> CustomControl
        Set: CustomControl(self: PSControlGroupBy) = value
        """
        ...

    @property
    def Expression(self) -> DisplayEntry:
        """
        Get: Expression(self: PSControlGroupBy) -> DisplayEntry
        Set: Expression(self: PSControlGroupBy) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: PSControlGroupBy) -> str
        Set: Label(self: PSControlGroupBy) = value
        """
        ...



class PSCredential(ISerializable): # skipped bases: <type 'object'>
    """
    PSCredential(userName: str, password: SecureString)
    PSCredential(pso: PSObject)
    """
    @property
    def Empty(self) -> PSCredential:
        """ Get: Empty() -> PSCredential """
        ...

    @property
    def GetSymmetricEncryptionKeyDelegate(self) -> GetSymmetricEncryptionKey:
        """
        Get: GetSymmetricEncryptionKeyDelegate() -> GetSymmetricEncryptionKey
        Set: GetSymmetricEncryptionKeyDelegate() = value
        """
        ...

    @property
    def Password(self) -> SecureString:
        """ Get: Password(self: PSCredential) -> SecureString """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: PSCredential) -> str """
        ...


    def GetNetworkCredential(self) -> NetworkCredential:
        """ GetNetworkCredential(self: PSCredential) -> NetworkCredential """
        ...



class PSCredentialTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PSCredentialTypes, values: Default (3), Domain (2), Generic (1) """
    Default: PSCredentialTypes = ...
    Domain: PSCredentialTypes = ...
    Generic: PSCredentialTypes = ...
    value__ = ...


class PSCredentialUIOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PSCredentialUIOptions, values: AlwaysPrompt (2), Default (1), None (0), ReadOnlyUserName (3), ValidateUserNameSyntax (1) """
    AlwaysPrompt: PSCredentialUIOptions = ...
    Default: PSCredentialUIOptions = ...
    ReadOnlyUserName: PSCredentialUIOptions = ...
    ValidateUserNameSyntax: PSCredentialUIOptions = ...
    value__ = ...


class PSCustomObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PSCustomObject) -> str """
        ...


class PSDataCollection(IDisposable, IList, ISerializable): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'object'>
    """
    PSDataCollection[T]()
    PSDataCollection[T](items: IEnumerable[T])
    PSDataCollection[T](capacity: int)
    """
    @property
    def BlockingEnumerator(self) -> bool:
        """
        Get: BlockingEnumerator(self: PSDataCollection[T]) -> bool
        Set: BlockingEnumerator(self: PSDataCollection[T]) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: PSDataCollection[T]) -> int """
        ...

    @property
    def DataAddedCount(self) -> int:
        """
        Get: DataAddedCount(self: PSDataCollection[T]) -> int
        Set: DataAddedCount(self: PSDataCollection[T]) = value
        """
        ...

    @property
    def EnumeratorNeverBlocks(self) -> bool:
        """
        Get: EnumeratorNeverBlocks(self: PSDataCollection[T]) -> bool
        Set: EnumeratorNeverBlocks(self: PSDataCollection[T]) = value
        """
        ...

    @property
    def IsAutoGenerated(self) -> bool:
        """
        Get: IsAutoGenerated(self: PSDataCollection[T]) -> bool
        Set: IsAutoGenerated(self: PSDataCollection[T]) = value
        """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: PSDataCollection[T]) -> bool """
        ...

    @property
    def SerializeInput(self) -> bool:
        """
        Get: SerializeInput(self: PSDataCollection[T]) -> bool
        Set: SerializeInput(self: PSDataCollection[T]) = value
        """
        ...


    def Complete(self): # -> 
        """ Complete(self: PSDataCollection[T]) """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: PSDataCollection[T], array: Array[T], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PSDataCollection[T]) -> IEnumerator[T] """
        ...

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: PSDataCollection[T], psInstanceId: Guid, index: int, item: T) """
        ...

    def ReadAll(self) -> Collection:
        """ ReadAll(self: PSDataCollection[T]) -> Collection[T] """
        ...

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: PSDataCollection[T], index: int) """
        ...

    Completed = ...
    DataAdded = ...
    DataAdding = ...


class PSDataStreams: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Debug(self) -> PSDataCollection:
        """
        Get: Debug(self: PSDataStreams) -> PSDataCollection[DebugRecord]
        Set: Debug(self: PSDataStreams) = value
        """
        ...

    @property
    def Error(self) -> PSDataCollection:
        """
        Get: Error(self: PSDataStreams) -> PSDataCollection[ErrorRecord]
        Set: Error(self: PSDataStreams) = value
        """
        ...

    @property
    def Information(self) -> PSDataCollection:
        """
        Get: Information(self: PSDataStreams) -> PSDataCollection[InformationRecord]
        Set: Information(self: PSDataStreams) = value
        """
        ...

    @property
    def Progress(self) -> PSDataCollection:
        """
        Get: Progress(self: PSDataStreams) -> PSDataCollection[ProgressRecord]
        Set: Progress(self: PSDataStreams) = value
        """
        ...

    @property
    def Verbose(self) -> PSDataCollection:
        """
        Get: Verbose(self: PSDataStreams) -> PSDataCollection[VerboseRecord]
        Set: Verbose(self: PSDataStreams) = value
        """
        ...

    @property
    def Warning(self) -> PSDataCollection:
        """
        Get: Warning(self: PSDataStreams) -> PSDataCollection[WarningRecord]
        Set: Warning(self: PSDataStreams) = value
        """
        ...


    def ClearStreams(self): # -> 
        """ ClearStreams(self: PSDataStreams) """
        ...


class PSDebugContext: # skipped bases: <type 'object'>, <type 'object'>
    """ PSDebugContext(invocationInfo: InvocationInfo, breakpoints: List[Breakpoint]) """
    @property
    def Breakpoints(self) -> Array:
        """ Get: Breakpoints(self: PSDebugContext) -> Array[Breakpoint] """
        ...

    @property
    def InvocationInfo(self) -> InvocationInfo:
        """ Get: InvocationInfo(self: PSDebugContext) -> InvocationInfo """
        ...



class PSDefaultValueAttribute(ParsingBaseAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PSDefaultValueAttribute() """
    @property
    def Help(self) -> str:
        """
        Get: Help(self: PSDefaultValueAttribute) -> str
        Set: Help(self: PSDefaultValueAttribute) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSDefaultValueAttribute) -> object
        Set: Value(self: PSDefaultValueAttribute) = value
        """
        ...



class PSDriveInfo(IComparable): # skipped bases: <type 'object'>
    """
    PSDriveInfo(name: str, provider: ProviderInfo, root: str, description: str, credential: PSCredential)
    PSDriveInfo(name: str, provider: ProviderInfo, root: str, description: str, credential: PSCredential, displayRoot: str)
    PSDriveInfo(name: str, provider: ProviderInfo, root: str, description: str, credential: PSCredential, persist: bool)
    """
    @property
    def Credential(self) -> PSCredential:
        """ Get: Credential(self: PSDriveInfo) -> PSCredential """
        ...

    @property
    def CurrentLocation(self) -> str:
        """
        Get: CurrentLocation(self: PSDriveInfo) -> str
        Set: CurrentLocation(self: PSDriveInfo) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PSDriveInfo) -> str
        Set: Description(self: PSDriveInfo) = value
        """
        ...

    @property
    def DisplayRoot(self) -> str:
        """ Get: DisplayRoot(self: PSDriveInfo) -> str """
        ...

    @property
    def MaximumSize(self) -> Nullable:
        """ Get: MaximumSize(self: PSDriveInfo) -> Nullable[Int64] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSDriveInfo) -> str """
        ...

    @property
    def Provider(self) -> ProviderInfo:
        """ Get: Provider(self: PSDriveInfo) -> ProviderInfo """
        ...

    @property
    def Root(self) -> str:
        """ Get: Root(self: PSDriveInfo) -> str """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: PSDriveInfo, obj: object) -> bool
        Equals(self: PSDriveInfo, drive: PSDriveInfo) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PSDriveInfo) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSDriveInfo) -> str """
        ...


class PSDynamicMember(PSMemberInfo): # skipped bases: <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PSDynamicMember) -> str """
        ...


class PSEngineEvent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Exiting: str = ...
    OnIdle: str = ...
    WorkflowJobStartEvent: str = ...


class PSEvent(PSMemberInfo): # skipped bases: <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: PSEvent) -> str """
        ...


class PSEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ComputerName(self) -> str:
        """ Get: ComputerName(self: PSEventArgs) -> str """
        ...

    @property
    def EventIdentifier(self) -> int:
        """ Get: EventIdentifier(self: PSEventArgs) -> int """
        ...

    @property
    def MessageData(self) -> PSObject:
        """ Get: MessageData(self: PSEventArgs) -> PSObject """
        ...

    @property
    def RunspaceId(self) -> Guid:
        """ Get: RunspaceId(self: PSEventArgs) -> Guid """
        ...

    @property
    def Sender(self) -> object:
        """ Get: Sender(self: PSEventArgs) -> object """
        ...

    @property
    def SourceArgs(self) -> Array:
        """ Get: SourceArgs(self: PSEventArgs) -> Array[object] """
        ...

    @property
    def SourceEventArgs(self) -> EventArgs:
        """ Get: SourceEventArgs(self: PSEventArgs) -> EventArgs """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """ Get: SourceIdentifier(self: PSEventArgs) -> str """
        ...

    @property
    def TimeGenerated(self) -> DateTime:
        """ Get: TimeGenerated(self: PSEventArgs) -> DateTime """
        ...



class PSEventArgsCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ PSEventArgsCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PSEventArgsCollection) -> int """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: PSEventArgsCollection) -> object """
        ...


    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: PSEventArgsCollection, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PSEventArgs](enumerable: IEnumerable[PSEventArgs], value: PSEventArgs) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    PSEventReceived = ...


class PSEventHandler: # skipped bases: <type 'object'>, <type 'object'>
    """
    PSEventHandler()
    PSEventHandler(eventManager: PSEventManager, sender: object, sourceIdentifier: str, extraData: PSObject)
    """
    eventManager = ...
    extraData = ...
    sender = ...
    sourceIdentifier = ...


class PSEventJob(Job): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ PSEventJob(eventManager: PSEventManager, subscriber: PSEventSubscriber, action: ScriptBlock, name: str) """
    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: PSEventJob) -> PSModuleInfo """
        ...



class PSEventManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ReceivedEvents(self) -> PSEventArgsCollection:
        """ Get: ReceivedEvents(self: PSEventManager) -> PSEventArgsCollection """
        ...

    @property
    def Subscribers(self) -> List:
        """ Get: Subscribers(self: PSEventManager) -> List[PSEventSubscriber] """
        ...


    def CreateEvent(self, *args): #cannot find CLR method
        """ CreateEvent(self: PSEventManager, sourceIdentifier: str, sender: object, args: Array[object], extraData: PSObject) -> PSEventArgs """
        ...

    def GenerateEvent(self, sourceIdentifier:str, sender:object, args:Array, extraData:PSObject, processInCurrentThread:bool = ..., waitForCompletionInCurrentThread:bool = ...) -> PSEventArgs:
        """
        GenerateEvent(self: PSEventManager, sourceIdentifier: str, sender: object, args: Array[object], extraData: PSObject) -> PSEventArgs
        GenerateEvent(self: PSEventManager, sourceIdentifier: str, sender: object, args: Array[object], extraData: PSObject, processInCurrentThread: bool, waitForCompletionInCurrentThread: bool) -> PSEventArgs
        """
        ...

    def GetEventSubscribers(self, sourceIdentifier:str) -> IEnumerable:
        """ GetEventSubscribers(self: PSEventManager, sourceIdentifier: str) -> IEnumerable[PSEventSubscriber] """
        ...

    def GetNextEventId(self, *args): #cannot find CLR method
        """ GetNextEventId(self: PSEventManager) -> int """
        ...

    def ProcessNewEvent(self, *args): #cannot find CLR method
        """ ProcessNewEvent(self: PSEventManager, newEvent: PSEventArgs, processInCurrentThread: bool, waitForCompletionWhenInCurrentThread: bool)ProcessNewEvent(self: PSEventManager, newEvent: PSEventArgs, processInCurrentThread: bool) """
        ...

    def SubscribeEvent(self, source, eventName, sourceIdentifier, data, *__args) -> PSEventSubscriber:
        """
        SubscribeEvent(self: PSEventManager, source: object, eventName: str, sourceIdentifier: str, data: PSObject, action: ScriptBlock, supportEvent: bool, forwardEvent: bool) -> PSEventSubscriber
        SubscribeEvent(self: PSEventManager, source: object, eventName: str, sourceIdentifier: str, data: PSObject, action: ScriptBlock, supportEvent: bool, forwardEvent: bool, maxTriggerCount: int) -> PSEventSubscriber
        SubscribeEvent(self: PSEventManager, source: object, eventName: str, sourceIdentifier: str, data: PSObject, handlerDelegate: PSEventReceivedEventHandler, supportEvent: bool, forwardEvent: bool) -> PSEventSubscriber
        SubscribeEvent(self: PSEventManager, source: object, eventName: str, sourceIdentifier: str, data: PSObject, handlerDelegate: PSEventReceivedEventHandler, supportEvent: bool, forwardEvent: bool, maxTriggerCount: int) -> PSEventSubscriber
        """
        ...

    def UnsubscribeEvent(self, subscriber:PSEventSubscriber): # -> 
        """ UnsubscribeEvent(self: PSEventManager, subscriber: PSEventSubscriber) """
        ...


class PSEventReceivedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PSEventReceivedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PSEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PSEventReceivedEventHandler, sender: object, e: PSEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PSEventReceivedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PSEventArgs): # -> 
        """ Invoke(self: PSEventReceivedEventHandler, sender: object, e: PSEventArgs) """
        ...


class PSEventSubscriber(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> PSEventJob:
        """ Get: Action(self: PSEventSubscriber) -> PSEventJob """
        ...

    @property
    def EventName(self) -> str:
        """ Get: EventName(self: PSEventSubscriber) -> str """
        ...

    @property
    def ForwardEvent(self) -> bool:
        """ Get: ForwardEvent(self: PSEventSubscriber) -> bool """
        ...

    @property
    def HandlerDelegate(self) -> PSEventReceivedEventHandler:
        """ Get: HandlerDelegate(self: PSEventSubscriber) -> PSEventReceivedEventHandler """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """ Get: SourceIdentifier(self: PSEventSubscriber) -> str """
        ...

    @property
    def SourceObject(self) -> object:
        """ Get: SourceObject(self: PSEventSubscriber) -> object """
        ...

    @property
    def SubscriptionId(self) -> int:
        """
        Get: SubscriptionId(self: PSEventSubscriber) -> int
        Set: SubscriptionId(self: PSEventSubscriber) = value
        """
        ...

    @property
    def SupportEvent(self) -> bool:
        """ Get: SupportEvent(self: PSEventSubscriber) -> bool """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: PSEventSubscriber) -> int """
        ...

    Unsubscribed = ...


class PSEventUnsubscribedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EventSubscriber(self) -> PSEventSubscriber:
        """ Get: EventSubscriber(self: PSEventUnsubscribedEventArgs) -> PSEventSubscriber """
        ...



class PSEventUnsubscribedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PSEventUnsubscribedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PSEventUnsubscribedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PSEventUnsubscribedEventHandler, sender: object, e: PSEventUnsubscribedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PSEventUnsubscribedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PSEventUnsubscribedEventArgs): # -> 
        """ Invoke(self: PSEventUnsubscribedEventHandler, sender: object, e: PSEventUnsubscribedEventArgs) """
        ...


class PSInvalidCastException(InvalidCastException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSInvalidCastException()
    PSInvalidCastException(message: str)
    PSInvalidCastException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PSInvalidCastException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PSInvalidOperationException(IContainsErrorRecord, InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSInvalidOperationException()
    PSInvalidOperationException(message: str)
    PSInvalidOperationException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PSInvalidOperationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PSInvocationSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ PSInvocationSettings() """
    @property
    def AddToHistory(self) -> bool:
        """
        Get: AddToHistory(self: PSInvocationSettings) -> bool
        Set: AddToHistory(self: PSInvocationSettings) = value
        """
        ...

    @property
    def ApartmentState(self) -> ApartmentState:
        """
        Get: ApartmentState(self: PSInvocationSettings) -> ApartmentState
        Set: ApartmentState(self: PSInvocationSettings) = value
        """
        ...

    @property
    def ErrorActionPreference(self) -> Nullable:
        """
        Get: ErrorActionPreference(self: PSInvocationSettings) -> Nullable[ActionPreference]
        Set: ErrorActionPreference(self: PSInvocationSettings) = value
        """
        ...

    @property
    def ExposeFlowControlExceptions(self) -> bool:
        """
        Get: ExposeFlowControlExceptions(self: PSInvocationSettings) -> bool
        Set: ExposeFlowControlExceptions(self: PSInvocationSettings) = value
        """
        ...

    @property
    def FlowImpersonationPolicy(self) -> bool:
        """
        Get: FlowImpersonationPolicy(self: PSInvocationSettings) -> bool
        Set: FlowImpersonationPolicy(self: PSInvocationSettings) = value
        """
        ...

    @property
    def Host(self) -> PSHost:
        """
        Get: Host(self: PSInvocationSettings) -> PSHost
        Set: Host(self: PSInvocationSettings) = value
        """
        ...

    @property
    def RemoteStreamOptions(self) -> RemoteStreamOptions:
        """
        Get: RemoteStreamOptions(self: PSInvocationSettings) -> RemoteStreamOptions
        Set: RemoteStreamOptions(self: PSInvocationSettings) = value
        """
        ...



class PSInvocationState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSInvocationState, values: Completed (4), Disconnected (6), Failed (5), NotStarted (0), Running (1), Stopped (3), Stopping (2) """
    Completed: PSInvocationState = ...
    Disconnected: PSInvocationState = ...
    Failed: PSInvocationState = ...
    NotStarted: PSInvocationState = ...
    Running: PSInvocationState = ...
    Stopped: PSInvocationState = ...
    Stopping: PSInvocationState = ...
    value__ = ...


class PSInvocationStateChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InvocationStateInfo(self) -> PSInvocationStateInfo:
        """ Get: InvocationStateInfo(self: PSInvocationStateChangedEventArgs) -> PSInvocationStateInfo """
        ...



class PSInvocationStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: PSInvocationStateInfo) -> Exception """
        ...

    @property
    def State(self) -> PSInvocationState:
        """ Get: State(self: PSInvocationStateInfo) -> PSInvocationState """
        ...



class PSJobProxy(Job2): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def HasMoreData(self) -> bool:
        """ Get: HasMoreData(self: PSJobProxy) -> bool """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: PSJobProxy) -> str """
        ...

    @property
    def RemoteJobInstanceId(self) -> Guid:
        """ Get: RemoteJobInstanceId(self: PSJobProxy) -> Guid """
        ...

    @property
    def RemoveRemoteJobOnCompletion(self) -> bool:
        """
        Get: RemoveRemoteJobOnCompletion(self: PSJobProxy) -> bool
        Set: RemoveRemoteJobOnCompletion(self: PSJobProxy) = value
        """
        ...

    @property
    def Runspace(self) -> Runspace:
        """
        Get: Runspace(self: PSJobProxy) -> Runspace
        Set: Runspace(self: PSJobProxy) = value
        """
        ...

    @property
    def RunspacePool(self) -> RunspacePool:
        """
        Get: RunspacePool(self: PSJobProxy) -> RunspacePool
        Set: RunspacePool(self: PSJobProxy) = value
        """
        ...

    @property
    def StatusMessage(self) -> str:
        """ Get: StatusMessage(self: PSJobProxy) -> str """
        ...


    @staticmethod
    def Create(*__args:Runspace) -> ICollection:
        """
        Create(runspace: Runspace, filter: Hashtable, dataAdded: EventHandler[JobDataAddedEventArgs], stateChanged: EventHandler[JobStateEventArgs]) -> ICollection[PSJobProxy]
        Create(runspace: Runspace, filter: Hashtable, receiveImmediately: bool) -> ICollection[PSJobProxy]
        Create(runspace: Runspace, filter: Hashtable) -> ICollection[PSJobProxy]
        Create(runspace: Runspace) -> ICollection[PSJobProxy]
        Create(runspacePool: RunspacePool, filter: Hashtable, dataAdded: EventHandler[JobDataAddedEventArgs], stateChanged: EventHandler[JobStateEventArgs]) -> ICollection[PSJobProxy]
        Create(runspacePool: RunspacePool, filter: Hashtable, receiveImmediately: bool) -> ICollection[PSJobProxy]
        Create(runspacePool: RunspacePool, filter: Hashtable) -> ICollection[PSJobProxy]
        Create(runspacePool: RunspacePool) -> ICollection[PSJobProxy]
        """
        ...

    def ReceiveJob(self, dataAdded:EventHandler = ..., stateChanged:EventHandler = ...): # -> 
        """ ReceiveJob(self: PSJobProxy)ReceiveJob(self: PSJobProxy, dataAdded: EventHandler[JobDataAddedEventArgs], stateChanged: EventHandler[JobStateEventArgs]) """
        ...

    def RemoveJob(self, removeRemoteJob:bool, force:bool = ...): # -> 
        """ RemoveJob(self: PSJobProxy, removeRemoteJob: bool, force: bool)RemoveJob(self: PSJobProxy, removeRemoteJob: bool) """
        ...

    def RemoveJobAsync(self, removeRemoteJob:bool, force:bool = ...): # -> 
        """ RemoveJobAsync(self: PSJobProxy, removeRemoteJob: bool)RemoveJobAsync(self: PSJobProxy, removeRemoteJob: bool, force: bool) """
        ...

    RemoveJobCompleted = ...


class PSJobStartEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PSJobStartEventArgs(job: Job, debugger: Debugger, isAsync: bool) """
    @property
    def Debugger(self) -> Debugger:
        """ Get: Debugger(self: PSJobStartEventArgs) -> Debugger """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: PSJobStartEventArgs) -> bool """
        ...

    @property
    def Job(self) -> Job:
        """ Get: Job(self: PSJobStartEventArgs) -> Job """
        ...


    def __new__(cls, job:Job, debugger:Debugger, isAsync:bool) -> Self:
        """ __new__(cls: type, job: Job, debugger: Debugger, isAsync: bool) """
        ...


class PSLanguageMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSLanguageMode, values: ConstrainedLanguage (3), FullLanguage (0), NoLanguage (2), RestrictedLanguage (1) """
    ConstrainedLanguage: PSLanguageMode = ...
    FullLanguage: PSLanguageMode = ...
    NoLanguage: PSLanguageMode = ...
    RestrictedLanguage: PSLanguageMode = ...
    value__ = ...


class PSListModifier: # skipped bases: <type 'object'>
    """
    PSListModifier()
    PSListModifier(removeItems: Collection[object], addItems: Collection[object])
    PSListModifier(replacementItems: object)
    PSListModifier(hash: Hashtable)
    """
    @property
    def Add(self) -> Collection:
        """ Get: Add(self: PSListModifier) -> Collection[object] """
        ...

    @property
    def Remove(self) -> Collection:
        """ Get: Remove(self: PSListModifier) -> Collection[object] """
        ...

    @property
    def Replace(self) -> Collection:
        """ Get: Replace(self: PSListModifier) -> Collection[object] """
        ...


    def ApplyTo(self, collectionToUpdate:IList): # -> 
        """ ApplyTo(self: PSListModifier, collectionToUpdate: IList)ApplyTo(self: PSListModifier, collectionToUpdate: object) """
        ...

    def __new__(cls, *__args:object) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, removeItems: Collection[object], addItems: Collection[object])
        __new__(cls: type, replacementItems: object)
        __new__(cls: type, hash: Hashtable)
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class PSMemberInfoCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, member, preValidated:bool = ...): # ->  # Not found arg types: {'member': 'T'}
        """ Add(self: PSMemberInfoCollection[T], member: T)Add(self: PSMemberInfoCollection[T], member: T, preValidated: bool) """
        ...

    def Match(self, name:str, memberTypes:PSMemberTypes = ...) -> ReadOnlyPSMemberInfoCollection:
        """
        Match(self: PSMemberInfoCollection[T], name: str) -> ReadOnlyPSMemberInfoCollection[T]
        Match(self: PSMemberInfoCollection[T], name: str, memberTypes: PSMemberTypes) -> ReadOnlyPSMemberInfoCollection[T]
        """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: PSMemberInfoCollection[T], name: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PSMemberSet(PSMemberInfo): # skipped bases: <type 'object'>
    """
    PSMemberSet(name: str)
    PSMemberSet(name: str, members: IEnumerable[PSMemberInfo])
    """
    @property
    def InheritMembers(self) -> bool:
        """ Get: InheritMembers(self: PSMemberSet) -> bool """
        ...

    @property
    def Members(self) -> PSMemberInfoCollection:
        """ Get: Members(self: PSMemberSet) -> PSMemberInfoCollection[PSMemberInfo] """
        ...

    @property
    def Methods(self) -> PSMemberInfoCollection:
        """ Get: Methods(self: PSMemberSet) -> PSMemberInfoCollection[PSMethodInfo] """
        ...

    @property
    def Properties(self) -> PSMemberInfoCollection:
        """ Get: Properties(self: PSMemberSet) -> PSMemberInfoCollection[PSPropertyInfo] """
        ...


    def ToString(self) -> str:
        """ ToString(self: PSMemberSet) -> str """
        ...

    def __new__(cls, name:str, members:IEnumerable = ...) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, members: IEnumerable[PSMemberInfo])
        """
        ...


class PSMemberTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PSMemberTypes, values: AliasProperty (1), All (8191), CodeMethod (128), CodeProperty (2), Dynamic (4096), Event (2048), MemberSet (1024), Method (64), Methods (448), NoteProperty (8), ParameterizedProperty (512), Properties (31), Property (4), PropertySet (32), ScriptMethod (256), ScriptProperty (16) """
    AliasProperty: PSMemberTypes = ...
    All: PSMemberTypes = ...
    CodeMethod: PSMemberTypes = ...
    CodeProperty: PSMemberTypes = ...
    Dynamic: PSMemberTypes = ...
    Event: PSMemberTypes = ...
    MemberSet: PSMemberTypes = ...
    Method: PSMemberTypes = ...
    Methods: PSMemberTypes = ...
    NoteProperty: PSMemberTypes = ...
    ParameterizedProperty: PSMemberTypes = ...
    Properties: PSMemberTypes = ...
    Property: PSMemberTypes = ...
    PropertySet: PSMemberTypes = ...
    ScriptMethod: PSMemberTypes = ...
    ScriptProperty: PSMemberTypes = ...
    value__ = ...


class PSMemberViewTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PSMemberViewTypes, values: Adapted (2), All (7), Base (4), Extended (1) """
    Adapted: PSMemberViewTypes = ...
    All: PSMemberViewTypes = ...
    Base: PSMemberViewTypes = ...
    Extended: PSMemberViewTypes = ...
    value__ = ...


class PSMethod(PSMethodInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSMethod) -> PSMemberTypes """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSMethod) -> str """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSMethod) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSMethod) -> str """
        ...


class PSModuleAutoLoadingPreference(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSModuleAutoLoadingPreference, values: All (2), ModuleQualified (1), None (0) """
    All: PSModuleAutoLoadingPreference = ...
    ModuleQualified: PSModuleAutoLoadingPreference = ...
    value__ = ...


class PSModuleInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    PSModuleInfo(linkToGlobal: bool)
    PSModuleInfo(scriptBlock: ScriptBlock)
    """
    @property
    def AccessMode(self) -> ModuleAccessMode:
        """
        Get: AccessMode(self: PSModuleInfo) -> ModuleAccessMode
        Set: AccessMode(self: PSModuleInfo) = value
        """
        ...

    @property
    def Author(self) -> str:
        """ Get: Author(self: PSModuleInfo) -> str """
        ...

    @property
    def ClrVersion(self) -> Version:
        """ Get: ClrVersion(self: PSModuleInfo) -> Version """
        ...

    @property
    def CompanyName(self) -> str:
        """ Get: CompanyName(self: PSModuleInfo) -> str """
        ...

    @property
    def CompatiblePSEditions(self) -> IEnumerable:
        """ Get: CompatiblePSEditions(self: PSModuleInfo) -> IEnumerable[str] """
        ...

    @property
    def Copyright(self) -> str:
        """ Get: Copyright(self: PSModuleInfo) -> str """
        ...

    @property
    def Definition(self) -> str:
        """ Get: Definition(self: PSModuleInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PSModuleInfo) -> str
        Set: Description(self: PSModuleInfo) = value
        """
        ...

    @property
    def DotNetFrameworkVersion(self) -> Version:
        """ Get: DotNetFrameworkVersion(self: PSModuleInfo) -> Version """
        ...

    @property
    def ExportedAliases(self) -> Dictionary:
        """ Get: ExportedAliases(self: PSModuleInfo) -> Dictionary[str, AliasInfo] """
        ...

    @property
    def ExportedCmdlets(self) -> Dictionary:
        """ Get: ExportedCmdlets(self: PSModuleInfo) -> Dictionary[str, CmdletInfo] """
        ...

    @property
    def ExportedCommands(self) -> Dictionary:
        """ Get: ExportedCommands(self: PSModuleInfo) -> Dictionary[str, CommandInfo] """
        ...

    @property
    def ExportedDscResources(self) -> ReadOnlyCollection:
        """ Get: ExportedDscResources(self: PSModuleInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def ExportedFormatFiles(self) -> ReadOnlyCollection:
        """ Get: ExportedFormatFiles(self: PSModuleInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def ExportedFunctions(self) -> Dictionary:
        """ Get: ExportedFunctions(self: PSModuleInfo) -> Dictionary[str, FunctionInfo] """
        ...

    @property
    def ExportedTypeFiles(self) -> ReadOnlyCollection:
        """ Get: ExportedTypeFiles(self: PSModuleInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def ExportedVariables(self) -> Dictionary:
        """ Get: ExportedVariables(self: PSModuleInfo) -> Dictionary[str, PSVariable] """
        ...

    @property
    def ExportedWorkflows(self) -> Dictionary:
        """ Get: ExportedWorkflows(self: PSModuleInfo) -> Dictionary[str, FunctionInfo] """
        ...

    @property
    def FileList(self) -> IEnumerable:
        """ Get: FileList(self: PSModuleInfo) -> IEnumerable[str] """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: PSModuleInfo) -> Guid """
        ...

    @property
    def HelpInfoUri(self) -> str:
        """ Get: HelpInfoUri(self: PSModuleInfo) -> str """
        ...

    @property
    def IconUri(self) -> Uri:
        """ Get: IconUri(self: PSModuleInfo) -> Uri """
        ...

    @property
    def ImplementingAssembly(self) -> Assembly:
        """ Get: ImplementingAssembly(self: PSModuleInfo) -> Assembly """
        ...

    @property
    def LicenseUri(self) -> Uri:
        """ Get: LicenseUri(self: PSModuleInfo) -> Uri """
        ...

    @property
    def LogPipelineExecutionDetails(self) -> bool:
        """
        Get: LogPipelineExecutionDetails(self: PSModuleInfo) -> bool
        Set: LogPipelineExecutionDetails(self: PSModuleInfo) = value
        """
        ...

    @property
    def ModuleBase(self) -> str:
        """ Get: ModuleBase(self: PSModuleInfo) -> str """
        ...

    @property
    def ModuleList(self) -> IEnumerable:
        """ Get: ModuleList(self: PSModuleInfo) -> IEnumerable[object] """
        ...

    @property
    def ModuleType(self) -> ModuleType:
        """ Get: ModuleType(self: PSModuleInfo) -> ModuleType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSModuleInfo) -> str """
        ...

    @property
    def NestedModules(self) -> ReadOnlyCollection:
        """ Get: NestedModules(self: PSModuleInfo) -> ReadOnlyCollection[PSModuleInfo] """
        ...

    @property
    def OnRemove(self) -> ScriptBlock:
        """
        Get: OnRemove(self: PSModuleInfo) -> ScriptBlock
        Set: OnRemove(self: PSModuleInfo) = value
        """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: PSModuleInfo) -> str """
        ...

    @property
    def PowerShellHostName(self) -> str:
        """ Get: PowerShellHostName(self: PSModuleInfo) -> str """
        ...

    @property
    def PowerShellHostVersion(self) -> Version:
        """ Get: PowerShellHostVersion(self: PSModuleInfo) -> Version """
        ...

    @property
    def PowerShellVersion(self) -> Version:
        """ Get: PowerShellVersion(self: PSModuleInfo) -> Version """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: PSModuleInfo) -> str """
        ...

    @property
    def PrivateData(self) -> object:
        """
        Get: PrivateData(self: PSModuleInfo) -> object
        Set: PrivateData(self: PSModuleInfo) = value
        """
        ...

    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """ Get: ProcessorArchitecture(self: PSModuleInfo) -> ProcessorArchitecture """
        ...

    @property
    def ProjectUri(self) -> Uri:
        """ Get: ProjectUri(self: PSModuleInfo) -> Uri """
        ...

    @property
    def ReleaseNotes(self) -> str:
        """ Get: ReleaseNotes(self: PSModuleInfo) -> str """
        ...

    @property
    def RepositorySourceLocation(self) -> Uri:
        """ Get: RepositorySourceLocation(self: PSModuleInfo) -> Uri """
        ...

    @property
    def RequiredAssemblies(self) -> IEnumerable:
        """ Get: RequiredAssemblies(self: PSModuleInfo) -> IEnumerable[str] """
        ...

    @property
    def RequiredModules(self) -> ReadOnlyCollection:
        """ Get: RequiredModules(self: PSModuleInfo) -> ReadOnlyCollection[PSModuleInfo] """
        ...

    @property
    def RootModule(self) -> str:
        """ Get: RootModule(self: PSModuleInfo) -> str """
        ...

    @property
    def Scripts(self) -> IEnumerable:
        """ Get: Scripts(self: PSModuleInfo) -> IEnumerable[str] """
        ...

    @property
    def SessionState(self) -> SessionState:
        """
        Get: SessionState(self: PSModuleInfo) -> SessionState
        Set: SessionState(self: PSModuleInfo) = value
        """
        ...

    @property
    def Tags(self) -> IEnumerable:
        """ Get: Tags(self: PSModuleInfo) -> IEnumerable[str] """
        ...

    @property
    def UseAppDomainLevelModuleCache(self) -> bool:
        """
        Get: UseAppDomainLevelModuleCache() -> bool
        Set: UseAppDomainLevelModuleCache() = value
        """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: PSModuleInfo) -> Version """
        ...


    def AsCustomObject(self) -> PSObject:
        """ AsCustomObject(self: PSModuleInfo) -> PSObject """
        ...

    @staticmethod
    def ClearAppDomainLevelModulePathCache(): # -> 
        """ ClearAppDomainLevelModulePathCache() """
        ...

    def Clone(self) -> PSModuleInfo:
        """ Clone(self: PSModuleInfo) -> PSModuleInfo """
        ...

    def GetExportedTypeDefinitions(self) -> ReadOnlyDictionary:
        """ GetExportedTypeDefinitions(self: PSModuleInfo) -> ReadOnlyDictionary[str, TypeDefinitionAst] """
        ...

    def GetVariableFromCallersModule(self, variableName:str) -> PSVariable:
        """ GetVariableFromCallersModule(self: PSModuleInfo, variableName: str) -> PSVariable """
        ...

    def Invoke(self, sb:ScriptBlock, args:Array) -> object:
        """ Invoke(self: PSModuleInfo, sb: ScriptBlock, *args: Array[object]) -> object """
        ...

    def NewBoundScriptBlock(self, scriptBlockToBind:ScriptBlock) -> ScriptBlock:
        """ NewBoundScriptBlock(self: PSModuleInfo, scriptBlockToBind: ScriptBlock) -> ScriptBlock """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSModuleInfo) -> str """
        ...



class PSNoteProperty(PSPropertyInfo): # skipped bases: <type 'object'>
    """ PSNoteProperty(name: str, value: object) """
    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSNoteProperty) -> PSMemberTypes """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSNoteProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSNoteProperty) -> object
        Set: Value(self: PSNoteProperty) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSNoteProperty) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSNoteProperty) -> str """
        ...

    def __new__(cls, name:str, value:object) -> Self:
        """ __new__(cls: type, name: str, value: object) """
        ...


class PSNotImplementedException(NotImplementedException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSNotImplementedException()
    PSNotImplementedException(message: str)
    PSNotImplementedException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PSNotImplementedException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PSNotSupportedException(NotSupportedException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSNotSupportedException()
    PSNotSupportedException(message: str)
    PSNotSupportedException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PSNotSupportedException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PSObject(IComparable, IDynamicMetaObjectProvider, IFormattable, ISerializable): # skipped bases: <type 'object'>
    """
    PSObject()
    PSObject(obj: object)
    """
    @property
    def BaseObject(self) -> object:
        """ Get: BaseObject(self: PSObject) -> object """
        ...

    @property
    def ImmediateBaseObject(self) -> object:
        """ Get: ImmediateBaseObject(self: PSObject) -> object """
        ...

    @property
    def Members(self) -> PSMemberInfoCollection:
        """ Get: Members(self: PSObject) -> PSMemberInfoCollection[PSMemberInfo] """
        ...

    @property
    def Methods(self) -> PSMemberInfoCollection:
        """ Get: Methods(self: PSObject) -> PSMemberInfoCollection[PSMethodInfo] """
        ...

    @property
    def Properties(self) -> PSMemberInfoCollection:
        """ Get: Properties(self: PSObject) -> PSMemberInfoCollection[PSPropertyInfo] """
        ...

    @property
    def TypeNames(self) -> Collection:
        """ Get: TypeNames(self: PSObject) -> Collection[str] """
        ...


    @staticmethod
    def AsPSObject(obj:object) -> PSObject:
        """ AsPSObject(obj: object) -> PSObject """
        ...

    def Copy(self) -> PSObject:
        """ Copy(self: PSObject) -> PSObject """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: PSObject, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PSObject) -> int """
        ...

    AdaptedMemberSetName: str = ...
    BaseObjectMemberSetName: str = ...
    ExtendedMemberSetName: str = ...


class PSObjectDisposedException(ObjectDisposedException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSObjectDisposedException(objectName: str)
    PSObjectDisposedException(objectName: str, message: str)
    PSObjectDisposedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PSObjectPropertyDescriptor(PropertyDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: PSObjectPropertyDescriptor) -> AttributeCollection """
        ...



class PSObjectTypeDescriptionProvider(TypeDescriptionProvider): # skipped bases: <type 'object'>
    """ PSObjectTypeDescriptionProvider() """
    GettingValueException = ...
    SettingValueException = ...


class PSObjectTypeDescriptor(CustomTypeDescriptor): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'object'>
    """ PSObjectTypeDescriptor(instance: PSObject) """
    @property
    def Instance(self) -> PSObject:
        """ Get: Instance(self: PSObjectTypeDescriptor) -> PSObject """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: PSObjectTypeDescriptor, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PSObjectTypeDescriptor) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    GettingValueException = ...
    SettingValueException = ...


class PSParameterizedProperty(PSMethodInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsGettable(self) -> bool:
        """ Get: IsGettable(self: PSParameterizedProperty) -> bool """
        ...

    @property
    def IsSettable(self) -> bool:
        """ Get: IsSettable(self: PSParameterizedProperty) -> bool """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSParameterizedProperty) -> PSMemberTypes """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSParameterizedProperty) -> str """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSParameterizedProperty) -> PSMemberInfo """
        ...

    def InvokeSet(self, valueToSet:object, arguments:Array): # -> 
        """ InvokeSet(self: PSParameterizedProperty, valueToSet: object, *arguments: Array[object]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSParameterizedProperty) -> str """
        ...


class PSParseError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: PSParseError) -> str """
        ...

    @property
    def Token(self) -> PSToken:
        """ Get: Token(self: PSParseError) -> PSToken """
        ...



class PSParser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Tokenize(script, errors) -> Tuple_[Collection, Collection]:
        """
        Tokenize(script: str) -> (Collection[PSToken], Collection[PSParseError])
        Tokenize(script: Array[object]) -> (Collection[PSToken], Collection[PSParseError])
        """
        ...


class PSPrimitiveDictionary(Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """
    PSPrimitiveDictionary()
    PSPrimitiveDictionary(other: Hashtable)
    """
    pass

class PSPropertyAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetProperties(self, baseObject:object) -> Collection:
        """ GetProperties(self: PSPropertyAdapter, baseObject: object) -> Collection[PSAdaptedProperty] """
        ...

    def GetProperty(self, baseObject:object, propertyName:str) -> PSAdaptedProperty:
        """ GetProperty(self: PSPropertyAdapter, baseObject: object, propertyName: str) -> PSAdaptedProperty """
        ...

    def GetPropertyTypeName(self, adaptedProperty:PSAdaptedProperty) -> str:
        """ GetPropertyTypeName(self: PSPropertyAdapter, adaptedProperty: PSAdaptedProperty) -> str """
        ...

    def GetPropertyValue(self, adaptedProperty:PSAdaptedProperty) -> object:
        """ GetPropertyValue(self: PSPropertyAdapter, adaptedProperty: PSAdaptedProperty) -> object """
        ...

    def GetTypeNameHierarchy(self, baseObject:object) -> Collection:
        """ GetTypeNameHierarchy(self: PSPropertyAdapter, baseObject: object) -> Collection[str] """
        ...

    def IsGettable(self, adaptedProperty:PSAdaptedProperty) -> bool:
        """ IsGettable(self: PSPropertyAdapter, adaptedProperty: PSAdaptedProperty) -> bool """
        ...

    def IsSettable(self, adaptedProperty:PSAdaptedProperty) -> bool:
        """ IsSettable(self: PSPropertyAdapter, adaptedProperty: PSAdaptedProperty) -> bool """
        ...

    def SetPropertyValue(self, adaptedProperty:PSAdaptedProperty, value:object): # -> 
        """ SetPropertyValue(self: PSPropertyAdapter, adaptedProperty: PSAdaptedProperty, value: object) """
        ...


class PSPropertySet(PSMemberInfo): # skipped bases: <type 'object'>
    """ PSPropertySet(name: str, referencedPropertyNames: IEnumerable[str]) """
    @property
    def ReferencedPropertyNames(self) -> Collection:
        """ Get: ReferencedPropertyNames(self: PSPropertySet) -> Collection[str] """
        ...


    def ToString(self) -> str:
        """ ToString(self: PSPropertySet) -> str """
        ...

    def __new__(cls, name:str, referencedPropertyNames:IEnumerable) -> Self:
        """ __new__(cls: type, name: str, referencedPropertyNames: IEnumerable[str]) """
        ...


class PSReference: # skipped bases: <type 'object'>, <type 'object'>
    """ PSReference(value: object) """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSReference) -> object
        Set: Value(self: PSReference) = value
        """
        ...



class PSScriptMethod(PSMethodInfo): # skipped bases: <type 'object'>
    """ PSScriptMethod(name: str, script: ScriptBlock) """
    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSScriptMethod) -> PSMemberTypes """
        ...

    @property
    def Script(self) -> ScriptBlock:
        """ Get: Script(self: PSScriptMethod) -> ScriptBlock """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSScriptMethod) -> str """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSScriptMethod) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSScriptMethod) -> str """
        ...

    def __new__(cls, name:str, script:ScriptBlock) -> Self:
        """ __new__(cls: type, name: str, script: ScriptBlock) """
        ...


class PSScriptProperty(PSPropertyInfo): # skipped bases: <type 'object'>
    """
    PSScriptProperty(name: str, getterScript: ScriptBlock)
    PSScriptProperty(name: str, getterScript: ScriptBlock, setterScript: ScriptBlock)
    """
    @property
    def GetterScript(self) -> ScriptBlock:
        """ Get: GetterScript(self: PSScriptProperty) -> ScriptBlock """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: PSScriptProperty) -> PSMemberTypes """
        ...

    @property
    def SetterScript(self) -> ScriptBlock:
        """ Get: SetterScript(self: PSScriptProperty) -> ScriptBlock """
        ...

    @property
    def TypeNameOfValue(self) -> str:
        """ Get: TypeNameOfValue(self: PSScriptProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSScriptProperty) -> object
        Set: Value(self: PSScriptProperty) = value
        """
        ...


    def Copy(self) -> PSMemberInfo:
        """ Copy(self: PSScriptProperty) -> PSMemberInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: PSScriptProperty) -> str """
        ...

    def __new__(cls, name:str, getterScript:ScriptBlock, setterScript:ScriptBlock = ...) -> Self:
        """
        __new__(cls: type, name: str, getterScript: ScriptBlock)
        __new__(cls: type, name: str, getterScript: ScriptBlock, setterScript: ScriptBlock)
        """
        ...


class PSSecurityException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PSSecurityException()
    PSSecurityException(message: str)
    PSSecurityException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: PSSecurityException) -> str """
        ...


    SerializeObjectState = ...


class PSSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Deserialize(source:str) -> object:
        """ Deserialize(source: str) -> object """
        ...

    @staticmethod
    def DeserializeAsList(source:str) -> Array:
        """ DeserializeAsList(source: str) -> Array[object] """
        ...

    @staticmethod
    def Serialize(source:object, depth:int = ...) -> str:
        """
        Serialize(source: object) -> str
        Serialize(source: object, depth: int) -> str
        """
        ...


class PSSessionTypeOption: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ConstructObjectFromPrivateData(self, *args): #cannot find CLR method
        """ ConstructObjectFromPrivateData(self: PSSessionTypeOption, privateData: str) -> PSSessionTypeOption """
        ...

    def ConstructPrivateData(self, *args): #cannot find CLR method
        """ ConstructPrivateData(self: PSSessionTypeOption) -> str """
        ...

    def CopyUpdatedValuesFrom(self, *args): #cannot find CLR method
        """ CopyUpdatedValuesFrom(self: PSSessionTypeOption, updated: PSSessionTypeOption) """
        ...


class PSSnapIn(PSSnapInInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def Formats(self) -> Array:
        """ Get: Formats(self: PSSnapIn) -> Array[str] """
        ...

    @property
    def Types(self) -> Array:
        """ Get: Types(self: PSSnapIn) -> Array[str] """
        ...



class PSSnapInInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationBase(self) -> str:
        """ Get: ApplicationBase(self: PSSnapInInfo) -> str """
        ...

    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: PSSnapInInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: PSSnapInInfo) -> str """
        ...

    @property
    def Formats(self) -> Collection:
        """ Get: Formats(self: PSSnapInInfo) -> Collection[str] """
        ...

    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: PSSnapInInfo) -> bool """
        ...

    @property
    def LogPipelineExecutionDetails(self) -> bool:
        """
        Get: LogPipelineExecutionDetails(self: PSSnapInInfo) -> bool
        Set: LogPipelineExecutionDetails(self: PSSnapInInfo) = value
        """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: PSSnapInInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSSnapInInfo) -> str """
        ...

    @property
    def PSVersion(self) -> Version:
        """ Get: PSVersion(self: PSSnapInInfo) -> Version """
        ...

    @property
    def Types(self) -> Collection:
        """ Get: Types(self: PSSnapInInfo) -> Collection[str] """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: PSSnapInInfo) -> str """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: PSSnapInInfo) -> Version """
        ...


    def ToString(self) -> str:
        """ ToString(self: PSSnapInInfo) -> str """
        ...


class PSSnapInSpecification: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PSSnapInSpecification) -> str """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: PSSnapInSpecification) -> Version """
        ...



class PSToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Content(self) -> str:
        """ Get: Content(self: PSToken) -> str """
        ...

    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: PSToken) -> int """
        ...

    @property
    def EndLine(self) -> int:
        """ Get: EndLine(self: PSToken) -> int """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: PSToken) -> int """
        ...

    @property
    def Start(self) -> int:
        """ Get: Start(self: PSToken) -> int """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: PSToken) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: PSToken) -> int """
        ...

    @property
    def Type(self) -> PSTokenType:
        """ Get: Type(self: PSToken) -> PSTokenType """
        ...


    @staticmethod
    def GetPSTokenType(token:Token) -> PSTokenType:
        """ GetPSTokenType(token: Token) -> PSTokenType """
        ...


class PSTokenType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSTokenType, values: Attribute (9), Command (1), CommandArgument (3), CommandParameter (2), Comment (15), GroupEnd (13), GroupStart (12), Keyword (14), LineContinuation (18), LoopLabel (8), Member (7), NewLine (17), Number (4), Operator (11), Position (19), StatementSeparator (16), String (5), Type (10), Unknown (0), Variable (6) """
    Attribute: PSTokenType = ...
    Command: PSTokenType = ...
    CommandArgument: PSTokenType = ...
    CommandParameter: PSTokenType = ...
    Comment: PSTokenType = ...
    GroupEnd: PSTokenType = ...
    GroupStart: PSTokenType = ...
    Keyword: PSTokenType = ...
    LineContinuation: PSTokenType = ...
    LoopLabel: PSTokenType = ...
    Member: PSTokenType = ...
    NewLine: PSTokenType = ...
    Number: PSTokenType = ...
    Operator: PSTokenType = ...
    Position: PSTokenType = ...
    StatementSeparator: PSTokenType = ...
    String: PSTokenType = ...
    Type: PSTokenType = ...
    Unknown: PSTokenType = ...
    value__ = ...
    Variable: PSTokenType = ...


class PSTraceSource: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> StringDictionary:
        """ Get: Attributes(self: PSTraceSource) -> StringDictionary """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PSTraceSource) -> str
        Set: Description(self: PSTraceSource) = value
        """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners(self: PSTraceSource) -> TraceListenerCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSTraceSource) -> str """
        ...

    @property
    def Options(self) -> PSTraceSourceOptions:
        """
        Get: Options(self: PSTraceSource) -> PSTraceSourceOptions
        Set: Options(self: PSTraceSource) = value
        """
        ...

    @property
    def Switch(self) -> SourceSwitch:
        """
        Get: Switch(self: PSTraceSource) -> SourceSwitch
        Set: Switch(self: PSTraceSource) = value
        """
        ...



class PSTraceSourceOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PSTraceSourceOptions, values: All (32767), Assert (16384), Constructor (1), Data (6167), Delegates (32), Dispose (2), Error (512), Errors (640), Events (64), Exception (128), ExecutionFlow (8303), Finalizer (4), Lock (256), Method (8), None (0), Property (16), Scope (8192), Verbose (2048), Warning (1024), WriteLine (4096) """
    All: PSTraceSourceOptions = ...
    Assert: PSTraceSourceOptions = ...
    Constructor: PSTraceSourceOptions = ...
    Data: PSTraceSourceOptions = ...
    Delegates: PSTraceSourceOptions = ...
    Dispose: PSTraceSourceOptions = ...
    Error: PSTraceSourceOptions = ...
    Errors: PSTraceSourceOptions = ...
    Events: PSTraceSourceOptions = ...
    Exception: PSTraceSourceOptions = ...
    ExecutionFlow: PSTraceSourceOptions = ...
    Finalizer: PSTraceSourceOptions = ...
    Lock: PSTraceSourceOptions = ...
    Method: PSTraceSourceOptions = ...
    Property: PSTraceSourceOptions = ...
    Scope: PSTraceSourceOptions = ...
    value__ = ...
    Verbose: PSTraceSourceOptions = ...
    Warning: PSTraceSourceOptions = ...
    WriteLine: PSTraceSourceOptions = ...


class PSTransaction(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RollbackPreference(self) -> RollbackSeverity:
        """ Get: RollbackPreference(self: PSTransaction) -> RollbackSeverity """
        ...

    @property
    def Status(self) -> PSTransactionStatus:
        """ Get: Status(self: PSTransaction) -> PSTransactionStatus """
        ...

    @property
    def SubscriberCount(self) -> int:
        """
        Get: SubscriberCount(self: PSTransaction) -> int
        Set: SubscriberCount(self: PSTransaction) = value
        """
        ...



class PSTransactionContext(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PSTransactionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSTransactionStatus, values: Active (2), Committed (1), RolledBack (0) """
    Active: PSTransactionStatus = ...
    Committed: PSTransactionStatus = ...
    RolledBack: PSTransactionStatus = ...
    value__ = ...


class PSTransportOption(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    def LoadFromDefaults(self, *args): #cannot find CLR method
        """ LoadFromDefaults(self: PSTransportOption, sessionType: PSSessionType, keepAssigned: bool) """
        ...


class PSTypeName: # skipped bases: <type 'object'>, <type 'object'>
    """
    PSTypeName(type: Type)
    PSTypeName(name: str)
    PSTypeName(typeDefinitionAst: TypeDefinitionAst)
    PSTypeName(typeName: ITypeName)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PSTypeName) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: PSTypeName) -> Type """
        ...

    @property
    def TypeDefinitionAst(self) -> TypeDefinitionAst:
        """ Get: TypeDefinitionAst(self: PSTypeName) -> TypeDefinitionAst """
        ...


    def ToString(self) -> str:
        """ ToString(self: PSTypeName) -> str """
        ...


class PSTypeNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PSTypeNameAttribute(psTypeName: str) """
    @property
    def PSTypeName(self) -> str:
        """ Get: PSTypeName(self: PSTypeNameAttribute) -> str """
        ...


    def __new__(cls, psTypeName:str) -> Self:
        """ __new__(cls: type, psTypeName: str) """
        ...


class PSVariable(IHasSessionStateEntryVisibility): # skipped bases: <type 'object'>
    """
    PSVariable(name: str)
    PSVariable(name: str, value: object)
    PSVariable(name: str, value: object, options: ScopedItemOptions)
    PSVariable(name: str, value: object, options: ScopedItemOptions, attributes: Collection[Attribute])
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: PSVariable) -> Collection[Attribute] """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PSVariable) -> str
        Set: Description(self: PSVariable) = value
        """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: PSVariable) -> PSModuleInfo """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: PSVariable) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSVariable) -> str """
        ...

    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: PSVariable) -> ScopedItemOptions
        Set: Options(self: PSVariable) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PSVariable) -> object
        Set: Value(self: PSVariable) = value
        """
        ...

    @property
    def Visibility(self) -> SessionStateEntryVisibility:
        """
        Get: Visibility(self: PSVariable) -> SessionStateEntryVisibility
        Set: Visibility(self: PSVariable) = value
        """
        ...


    def IsValidValue(self, value:object) -> bool:
        """ IsValidValue(self: PSVariable, value: object) -> bool """
        ...


class PSVariableIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Get(self, name:str) -> PSVariable:
        """ Get(self: PSVariableIntrinsics, name: str) -> PSVariable """
        ...

    def GetValue(self, name:str, defaultValue:object = ...) -> object:
        """
        GetValue(self: PSVariableIntrinsics, name: str) -> object
        GetValue(self: PSVariableIntrinsics, name: str, defaultValue: object) -> object
        """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: PSVariableIntrinsics, name: str)Remove(self: PSVariableIntrinsics, variable: PSVariable) """
        ...

    def Set(self, *__args:PSVariable): # -> 
        """ Set(self: PSVariableIntrinsics, name: str, value: object)Set(self: PSVariableIntrinsics, variable: PSVariable) """
        ...


class PSVariableProperty(PSNoteProperty): # skipped bases: <type 'object'>
    """ PSVariableProperty(variable: PSVariable) """
    pass

class ReadOnlyPSMemberInfoCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReadOnlyPSMemberInfoCollection[T]) -> int """
        ...


    def Match(self, name:str, memberTypes:PSMemberTypes = ...) -> ReadOnlyPSMemberInfoCollection:
        """
        Match(self: ReadOnlyPSMemberInfoCollection[T], name: str) -> ReadOnlyPSMemberInfoCollection[T]
        Match(self: ReadOnlyPSMemberInfoCollection[T], name: str, memberTypes: PSMemberTypes) -> ReadOnlyPSMemberInfoCollection[T]
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class RedirectedException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RedirectedException()
    RedirectedException(message: str)
    RedirectedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RegisterArgumentCompleterCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RegisterArgumentCompleterCommand() """
    @property
    def CommandName(self) -> Array:
        """
        Get: CommandName(self: RegisterArgumentCompleterCommand) -> Array[str]
        Set: CommandName(self: RegisterArgumentCompleterCommand) = value
        """
        ...

    @property
    def Native(self) -> SwitchParameter:
        """
        Get: Native(self: RegisterArgumentCompleterCommand) -> SwitchParameter
        Set: Native(self: RegisterArgumentCompleterCommand) = value
        """
        ...

    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: RegisterArgumentCompleterCommand) -> str
        Set: ParameterName(self: RegisterArgumentCompleterCommand) = value
        """
        ...

    @property
    def ScriptBlock(self) -> ScriptBlock:
        """
        Get: ScriptBlock(self: RegisterArgumentCompleterCommand) -> ScriptBlock
        Set: ScriptBlock(self: RegisterArgumentCompleterCommand) = value
        """
        ...



class RemoteCommandInfo(CommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    pass

class RemoteException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RemoteException()
    RemoteException(message: str)
    RemoteException(message: str, innerException: Exception)
    """
    @property
    def SerializedRemoteException(self) -> PSObject:
        """ Get: SerializedRemoteException(self: RemoteException) -> PSObject """
        ...

    @property
    def SerializedRemoteInvocationInfo(self) -> PSObject:
        """ Get: SerializedRemoteInvocationInfo(self: RemoteException) -> PSObject """
        ...


    SerializeObjectState = ...


class RemoteStreamOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RemoteStreamOptions, values: AddInvocationInfo (15), AddInvocationInfoToDebugRecord (4), AddInvocationInfoToErrorRecord (1), AddInvocationInfoToVerboseRecord (8), AddInvocationInfoToWarningRecord (2) """
    AddInvocationInfo: RemoteStreamOptions = ...
    AddInvocationInfoToDebugRecord: RemoteStreamOptions = ...
    AddInvocationInfoToErrorRecord: RemoteStreamOptions = ...
    AddInvocationInfoToVerboseRecord: RemoteStreamOptions = ...
    AddInvocationInfoToWarningRecord: RemoteStreamOptions = ...
    value__ = ...


class RemotingBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RemotingBehavior, values: Custom (2), None (0), PowerShell (1) """
    Custom: RemotingBehavior = ...
    PowerShell: RemotingBehavior = ...
    value__ = ...


class RemotingCapability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RemotingCapability, values: None (0), OwnedByCommand (3), PowerShell (1), SupportedByCommand (2) """
    OwnedByCommand: RemotingCapability = ...
    PowerShell: RemotingCapability = ...
    SupportedByCommand: RemotingCapability = ...
    value__ = ...


class Repository: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: Repository[T], item: T) """
        ...

    def GetItem(self, instanceId:Guid): # -> T
        """ GetItem(self: Repository[T], instanceId: Guid) -> T """
        ...

    def GetItems(self) -> List:
        """ GetItems(self: Repository[T]) -> List[T] """
        ...

    def GetKey(self, *args): #cannot find CLR method
        """ GetKey(self: Repository[T], item: T) -> Guid """
        ...

    def Remove(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Remove(self: Repository[T], item: T) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ResolutionPurpose(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResolutionPurpose, values: Decryption (1), Encryption (0) """
    Decryption: ResolutionPurpose = ...
    Encryption: ResolutionPurpose = ...
    value__ = ...


class ReturnContainers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReturnContainers, values: ReturnAllContainers (1), ReturnMatchingContainers (0) """
    ReturnAllContainers: ReturnContainers = ...
    ReturnMatchingContainers: ReturnContainers = ...
    value__ = ...


class RollbackSeverity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RollbackSeverity, values: Error (0), Never (2), TerminatingError (1) """
    Error: RollbackSeverity = ...
    Never: RollbackSeverity = ...
    TerminatingError: RollbackSeverity = ...
    value__ = ...


class RunspaceInvoke(IDisposable): # skipped bases: <type 'object'>
    """
    RunspaceInvoke()
    RunspaceInvoke(runspaceConfiguration: RunspaceConfiguration)
    RunspaceInvoke(consoleFilePath: str)
    RunspaceInvoke(runspace: Runspace)
    """
    def Invoke(self, script, input=None, errors=None) -> Collection:
        """
        Invoke(self: RunspaceInvoke, script: str) -> Collection[PSObject]
        Invoke(self: RunspaceInvoke, script: str, input: IEnumerable) -> Collection[PSObject]
        Invoke(self: RunspaceInvoke, script: str, input: IEnumerable) -> (Collection[PSObject], IList)
        """
        ...


class RunspaceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RunspaceMode, values: CurrentRunspace (0), NewRunspace (1) """
    CurrentRunspace: RunspaceMode = ...
    NewRunspace: RunspaceMode = ...
    value__ = ...


class RunspacePoolStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ RunspacePoolStateInfo(state: RunspacePoolState, reason: Exception) """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: RunspacePoolStateInfo) -> Exception """
        ...

    @property
    def State(self) -> RunspacePoolState:
        """ Get: State(self: RunspacePoolStateInfo) -> RunspacePoolState """
        ...



class RunspaceRepository(Repository): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Runspaces(self) -> List:
        """ Get: Runspaces(self: RunspaceRepository) -> List[PSSession] """
        ...



class RuntimeDefinedParameter: # skipped bases: <type 'object'>, <type 'object'>
    """
    RuntimeDefinedParameter()
    RuntimeDefinedParameter(name: str, parameterType: Type, attributes: Collection[Attribute])
    """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: RuntimeDefinedParameter) -> Collection[Attribute] """
        ...

    @property
    def IsSet(self) -> bool:
        """
        Get: IsSet(self: RuntimeDefinedParameter) -> bool
        Set: IsSet(self: RuntimeDefinedParameter) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RuntimeDefinedParameter) -> str
        Set: Name(self: RuntimeDefinedParameter) = value
        """
        ...

    @property
    def ParameterType(self) -> Type:
        """
        Get: ParameterType(self: RuntimeDefinedParameter) -> Type
        Set: ParameterType(self: RuntimeDefinedParameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: RuntimeDefinedParameter) -> object
        Set: Value(self: RuntimeDefinedParameter) = value
        """
        ...



class RuntimeDefinedParameterDictionary(Dictionary): # skipped bases: <type 'IReadOnlyCollection[KeyValuePair[str, RuntimeDefinedParameter]]'>, <type 'IEnumerable[KeyValuePair[str, RuntimeDefinedParameter]]'>, <type 'ICollection[KeyValuePair[str, RuntimeDefinedParameter]]'>, <type 'IEnumerable'>, <type 'IDictionary[str, RuntimeDefinedParameter]'>, <type 'IDictionary'>, <type 'IReadOnlyDictionary[str, RuntimeDefinedParameter]'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """ RuntimeDefinedParameterDictionary() """
    @property
    def Data(self) -> object:
        """
        Get: Data(self: RuntimeDefinedParameterDictionary) -> object
        Set: Data(self: RuntimeDefinedParameterDictionary) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: RuntimeDefinedParameterDictionary) -> str
        Set: HelpFile(self: RuntimeDefinedParameterDictionary) = value
        """
        ...



class ScopedItemOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ScopedItemOptions, values: AllScope (8), Constant (2), None (0), Private (4), ReadOnly (1), Unspecified (16) """
    AllScope: ScopedItemOptions = ...
    Constant: ScopedItemOptions = ...
    Private: ScopedItemOptions = ...
    ReadOnly: ScopedItemOptions = ...
    Unspecified: ScopedItemOptions = ...
    value__ = ...


class ScriptBlock(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Ast(self) -> Ast:
        """ Get: Ast(self: ScriptBlock) -> Ast """
        ...

    @property
    def Attributes(self) -> List:
        """ Get: Attributes(self: ScriptBlock) -> List[Attribute] """
        ...

    @property
    def DebuggerHidden(self) -> bool:
        """
        Get: DebuggerHidden(self: ScriptBlock) -> bool
        Set: DebuggerHidden(self: ScriptBlock) = value
        """
        ...

    @property
    def File(self) -> str:
        """ Get: File(self: ScriptBlock) -> str """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: ScriptBlock) -> Guid """
        ...

    @property
    def IsConfiguration(self) -> bool:
        """
        Get: IsConfiguration(self: ScriptBlock) -> bool
        Set: IsConfiguration(self: ScriptBlock) = value
        """
        ...

    @property
    def IsFilter(self) -> bool:
        """
        Get: IsFilter(self: ScriptBlock) -> bool
        Set: IsFilter(self: ScriptBlock) = value
        """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: ScriptBlock) -> PSModuleInfo """
        ...

    @property
    def StartPosition(self) -> PSToken:
        """ Get: StartPosition(self: ScriptBlock) -> PSToken """
        ...


    def CheckRestrictedLanguage(self, allowedCommands:IEnumerable, allowedVariables:IEnumerable, allowEnvironmentVariables:bool): # -> 
        """ CheckRestrictedLanguage(self: ScriptBlock, allowedCommands: IEnumerable[str], allowedVariables: IEnumerable[str], allowEnvironmentVariables: bool) """
        ...

    @staticmethod
    def Create(script:str) -> ScriptBlock:
        """ Create(script: str) -> ScriptBlock """
        ...

    def GetNewClosure(self) -> ScriptBlock:
        """ GetNewClosure(self: ScriptBlock) -> ScriptBlock """
        ...

    def GetPowerShell(self, *__args:Array) -> PowerShell:
        """
        GetPowerShell(self: ScriptBlock, variables: Dictionary[str, object], *args: Array[object]) -> (PowerShell, Dictionary[str, object])
        GetPowerShell(self: ScriptBlock, *args: Array[object]) -> PowerShell
        GetPowerShell(self: ScriptBlock, isTrustedInput: bool, *args: Array[object]) -> PowerShell
        GetPowerShell(self: ScriptBlock, variables: Dictionary[str, object], *args: Array[object]) -> PowerShell
        GetPowerShell(self: ScriptBlock, variables: Dictionary[str, object], isTrustedInput: bool, *args: Array[object]) -> (PowerShell, Dictionary[str, object])
        """
        ...

    def GetSteppablePipeline(self, commandOrigin:CommandOrigin = ..., args:Array = ...) -> SteppablePipeline:
        """
        GetSteppablePipeline(self: ScriptBlock) -> SteppablePipeline
        GetSteppablePipeline(self: ScriptBlock, commandOrigin: CommandOrigin) -> SteppablePipeline
        GetSteppablePipeline(self: ScriptBlock, commandOrigin: CommandOrigin, args: Array[object]) -> SteppablePipeline
        """
        ...

    def Invoke(self, args:Array) -> Collection:
        """ Invoke(self: ScriptBlock, *args: Array[object]) -> Collection[PSObject] """
        ...

    def InvokeReturnAsIs(self, args:Array) -> object:
        """ InvokeReturnAsIs(self: ScriptBlock, *args: Array[object]) -> object """
        ...

    def InvokeWithContext(self, functionsToDefine:IDictionary, variablesToDefine:List, args:Array) -> Collection:
        """
        InvokeWithContext(self: ScriptBlock, functionsToDefine: IDictionary, variablesToDefine: List[PSVariable], *args: Array[object]) -> Collection[PSObject]
        InvokeWithContext(self: ScriptBlock, functionsToDefine: Dictionary[str, ScriptBlock], variablesToDefine: List[PSVariable], *args: Array[object]) -> Collection[PSObject]
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: ScriptBlock) -> str """
        ...


class ScriptBlockToPowerShellNotSupportedException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ScriptBlockToPowerShellNotSupportedException()
    ScriptBlockToPowerShellNotSupportedException(message: str)
    ScriptBlockToPowerShellNotSupportedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ScriptCallDepthException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ScriptCallDepthException()
    ScriptCallDepthException(message: str)
    ScriptCallDepthException(message: str, innerException: Exception)
    """
    @property
    def CallDepth(self) -> int:
        """ Get: CallDepth(self: ScriptCallDepthException) -> int """
        ...


    SerializeObjectState = ...


class ScriptInfo(CommandInfo, IScriptCommandInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'object'>
    """ no doc """
    @property
    def ScriptBlock(self) -> ScriptBlock:
        """ Get: ScriptBlock(self: ScriptInfo) -> ScriptBlock """
        ...



class ScriptRequiresException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ScriptRequiresException()
    ScriptRequiresException(message: str)
    ScriptRequiresException(message: str, innerException: Exception)
    """
    @property
    def CommandName(self) -> str:
        """ Get: CommandName(self: ScriptRequiresException) -> str """
        ...

    @property
    def MissingPSSnapIns(self) -> ReadOnlyCollection:
        """ Get: MissingPSSnapIns(self: ScriptRequiresException) -> ReadOnlyCollection[str] """
        ...

    @property
    def RequiresPSVersion(self) -> Version:
        """ Get: RequiresPSVersion(self: ScriptRequiresException) -> Version """
        ...

    @property
    def RequiresShellId(self) -> str:
        """ Get: RequiresShellId(self: ScriptRequiresException) -> str """
        ...

    @property
    def RequiresShellPath(self) -> str:
        """ Get: RequiresShellPath(self: ScriptRequiresException) -> str """
        ...


    SerializeObjectState = ...


class SecurityDescriptorCmdletProviderIntrinsics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Get(self, path:str, includeSections:AccessControlSections) -> Collection:
        """ Get(self: SecurityDescriptorCmdletProviderIntrinsics, path: str, includeSections: AccessControlSections) -> Collection[PSObject] """
        ...

    def NewFromPath(self, path:str, includeSections:AccessControlSections) -> ObjectSecurity:
        """ NewFromPath(self: SecurityDescriptorCmdletProviderIntrinsics, path: str, includeSections: AccessControlSections) -> ObjectSecurity """
        ...

    def NewOfType(self, providerId:str, type:str, includeSections:AccessControlSections) -> ObjectSecurity:
        """ NewOfType(self: SecurityDescriptorCmdletProviderIntrinsics, providerId: str, type: str, includeSections: AccessControlSections) -> ObjectSecurity """
        ...

    def Set(self, path:str, sd:ObjectSecurity) -> Collection:
        """ Set(self: SecurityDescriptorCmdletProviderIntrinsics, path: str, sd: ObjectSecurity) -> Collection[PSObject] """
        ...


class SessionCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SessionCapabilities, values: Language (4), RemoteServer (1), WorkflowServer (2) """
    Language: SessionCapabilities = ...
    RemoteServer: SessionCapabilities = ...
    value__ = ...
    WorkflowServer: SessionCapabilities = ...


class SessionState: # skipped bases: <type 'object'>, <type 'object'>
    """ SessionState() """
    @property
    def Applications(self) -> List:
        """ Get: Applications(self: SessionState) -> List[str] """
        ...

    @property
    def Drive(self) -> DriveManagementIntrinsics:
        """ Get: Drive(self: SessionState) -> DriveManagementIntrinsics """
        ...

    @property
    def InvokeCommand(self) -> CommandInvocationIntrinsics:
        """ Get: InvokeCommand(self: SessionState) -> CommandInvocationIntrinsics """
        ...

    @property
    def InvokeProvider(self) -> ProviderIntrinsics:
        """ Get: InvokeProvider(self: SessionState) -> ProviderIntrinsics """
        ...

    @property
    def LanguageMode(self) -> PSLanguageMode:
        """
        Get: LanguageMode(self: SessionState) -> PSLanguageMode
        Set: LanguageMode(self: SessionState) = value
        """
        ...

    @property
    def Module(self) -> PSModuleInfo:
        """ Get: Module(self: SessionState) -> PSModuleInfo """
        ...

    @property
    def Path(self) -> PathIntrinsics:
        """ Get: Path(self: SessionState) -> PathIntrinsics """
        ...

    @property
    def Provider(self) -> CmdletProviderManagementIntrinsics:
        """ Get: Provider(self: SessionState) -> CmdletProviderManagementIntrinsics """
        ...

    @property
    def PSVariable(self) -> PSVariableIntrinsics:
        """ Get: PSVariable(self: SessionState) -> PSVariableIntrinsics """
        ...

    @property
    def Scripts(self) -> List:
        """ Get: Scripts(self: SessionState) -> List[str] """
        ...

    @property
    def UseFullLanguageModeInDebugger(self) -> bool:
        """ Get: UseFullLanguageModeInDebugger(self: SessionState) -> bool """
        ...


    @staticmethod
    def IsVisible(origin:CommandOrigin, *__args:object) -> bool:
        """
        IsVisible(origin: CommandOrigin, valueToCheck: object) -> bool
        IsVisible(origin: CommandOrigin, variable: PSVariable) -> bool
        IsVisible(origin: CommandOrigin, commandInfo: CommandInfo) -> bool
        """
        ...

    @staticmethod
    def ThrowIfNotVisible(origin:CommandOrigin, valueToCheck:object): # -> 
        """ ThrowIfNotVisible(origin: CommandOrigin, valueToCheck: object) """
        ...


class SessionStateCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionStateCategory, values: Alias (1), Cmdlet (9), CmdletProvider (5), Command (7), Drive (4), Filter (3), Function (2), Resource (8), Scope (6), Variable (0) """
    Alias: SessionStateCategory = ...
    Cmdlet: SessionStateCategory = ...
    CmdletProvider: SessionStateCategory = ...
    Command: SessionStateCategory = ...
    Drive: SessionStateCategory = ...
    Filter: SessionStateCategory = ...
    Function: SessionStateCategory = ...
    Resource: SessionStateCategory = ...
    Scope: SessionStateCategory = ...
    value__ = ...
    Variable: SessionStateCategory = ...


class SessionStateEntryVisibility(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionStateEntryVisibility, values: Private (1), Public (0) """
    Private: SessionStateEntryVisibility = ...
    Public: SessionStateEntryVisibility = ...
    value__ = ...


class SessionStateOverflowException(SessionStateException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SessionStateOverflowException()
    SessionStateOverflowException(message: str)
    SessionStateOverflowException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SessionStateUnauthorizedAccessException(SessionStateException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SessionStateUnauthorizedAccessException()
    SessionStateUnauthorizedAccessException(message: str)
    SessionStateUnauthorizedAccessException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SettingValueExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: SettingValueExceptionEventArgs) -> Exception """
        ...

    @property
    def ShouldThrow(self) -> bool:
        """
        Get: ShouldThrow(self: SettingValueExceptionEventArgs) -> bool
        Set: ShouldThrow(self: SettingValueExceptionEventArgs) = value
        """
        ...



class SetValueException(ExtendedTypeSystemException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SetValueException()
    SetValueException(message: str)
    SetValueException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SetValueInvocationException(SetValueException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SetValueInvocationException()
    SetValueInvocationException(message: str)
    SetValueInvocationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ShouldProcessReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ShouldProcessReason, values: None (0), WhatIf (1) """
    value__ = ...
    WhatIf: ShouldProcessReason = ...


class Signature: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsOSBinary(self) -> bool:
        """ Get: IsOSBinary(self: Signature) -> bool """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: Signature) -> str """
        ...

    @property
    def SignatureType(self) -> SignatureType:
        """ Get: SignatureType(self: Signature) -> SignatureType """
        ...

    @property
    def SignerCertificate(self) -> X509Certificate2:
        """ Get: SignerCertificate(self: Signature) -> X509Certificate2 """
        ...

    @property
    def Status(self) -> SignatureStatus:
        """ Get: Status(self: Signature) -> SignatureStatus """
        ...

    @property
    def StatusMessage(self) -> str:
        """ Get: StatusMessage(self: Signature) -> str """
        ...

    @property
    def TimeStamperCertificate(self) -> X509Certificate2:
        """ Get: TimeStamperCertificate(self: Signature) -> X509Certificate2 """
        ...



class SignatureStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SignatureStatus, values: HashMismatch (3), Incompatible (6), NotSigned (2), NotSupportedFileFormat (5), NotTrusted (4), UnknownError (1), Valid (0) """
    HashMismatch: SignatureStatus = ...
    Incompatible: SignatureStatus = ...
    NotSigned: SignatureStatus = ...
    NotSupportedFileFormat: SignatureStatus = ...
    NotTrusted: SignatureStatus = ...
    UnknownError: SignatureStatus = ...
    Valid: SignatureStatus = ...
    value__ = ...


class SignatureType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SignatureType, values: Authenticode (1), Catalog (2), None (0) """
    Authenticode: SignatureType = ...
    Catalog: SignatureType = ...
    value__ = ...


class SigningOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SigningOption, values: AddFullCertificateChain (1), AddFullCertificateChainExceptRoot (2), AddOnlyCertificate (0), Default (2) """
    AddFullCertificateChain: SigningOption = ...
    AddFullCertificateChainExceptRoot: SigningOption = ...
    AddOnlyCertificate: SigningOption = ...
    Default: SigningOption = ...
    value__ = ...


class SplitOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SplitOptions, values: CultureInvariant (4), ExplicitCapture (128), IgnoreCase (64), IgnorePatternWhitespace (8), Multiline (16), RegexMatch (2), SimpleMatch (1), Singleline (32) """
    CultureInvariant: SplitOptions = ...
    ExplicitCapture: SplitOptions = ...
    IgnoreCase: SplitOptions = ...
    IgnorePatternWhitespace: SplitOptions = ...
    Multiline: SplitOptions = ...
    RegexMatch: SplitOptions = ...
    SimpleMatch: SplitOptions = ...
    Singleline: SplitOptions = ...
    value__ = ...


class SteppablePipeline(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Begin(self, *__args:bool): # -> 
        """ Begin(self: SteppablePipeline, expectInput: bool)Begin(self: SteppablePipeline, expectInput: bool, contextToRedirectTo: EngineIntrinsics)Begin(self: SteppablePipeline, command: InternalCommand) """
        ...

    def End(self) -> Array:
        """ End(self: SteppablePipeline) -> Array """
        ...

    def Process(self, input:object = ...) -> Array:
        """
        Process(self: SteppablePipeline, input: object) -> Array
        Process(self: SteppablePipeline, input: PSObject) -> Array
        Process(self: SteppablePipeline) -> Array
        """
        ...


class SupportsWildcardsAttribute(ParsingBaseAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SupportsWildcardsAttribute() """
    pass

class SwitchParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ SwitchParameter(isPresent: bool) """
    @property
    def IsPresent(self) -> bool:
        """ Get: IsPresent(self: SwitchParameter) -> bool """
        ...

    @property
    def Present(self) -> SwitchParameter:
        """ Get: Present() -> SwitchParameter """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SwitchParameter, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SwitchParameter) -> int """
        ...

    def ToBool(self) -> bool:
        """ ToBool(self: SwitchParameter) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: SwitchParameter) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class TableControl(PSControl): # skipped bases: <type 'object'>
    """
    TableControl()
    TableControl(tableControlRow: TableControlRow)
    TableControl(tableControlRow: TableControlRow, tableControlColumnHeaders: IEnumerable[TableControlColumnHeader])
    """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: TableControl) -> bool
        Set: AutoSize(self: TableControl) = value
        """
        ...

    @property
    def Headers(self) -> List:
        """
        Get: Headers(self: TableControl) -> List[TableControlColumnHeader]
        Set: Headers(self: TableControl) = value
        """
        ...

    @property
    def HideTableHeaders(self) -> bool:
        """
        Get: HideTableHeaders(self: TableControl) -> bool
        Set: HideTableHeaders(self: TableControl) = value
        """
        ...

    @property
    def Rows(self) -> List:
        """
        Get: Rows(self: TableControl) -> List[TableControlRow]
        Set: Rows(self: TableControl) = value
        """
        ...


    @staticmethod
    def Create(outOfBand:bool, autoSize:bool, hideTableHeaders:bool) -> TableControlBuilder:
        """ Create(outOfBand: bool, autoSize: bool, hideTableHeaders: bool) -> TableControlBuilder """
        ...

    def __new__(cls, tableControlRow:TableControlRow = ..., tableControlColumnHeaders:IEnumerable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, tableControlRow: TableControlRow)
        __new__(cls: type, tableControlRow: TableControlRow, tableControlColumnHeaders: IEnumerable[TableControlColumnHeader])
        """
        ...


class TableControlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddHeader(self, alignment:Alignment, width:int, label:str) -> TableControlBuilder:
        """ AddHeader(self: TableControlBuilder, alignment: Alignment, width: int, label: str) -> TableControlBuilder """
        ...

    def EndTable(self) -> TableControl:
        """ EndTable(self: TableControlBuilder) -> TableControl """
        ...

    def GroupByProperty(self, property:str, customControl:CustomControl, label:str) -> TableControlBuilder:
        """ GroupByProperty(self: TableControlBuilder, property: str, customControl: CustomControl, label: str) -> TableControlBuilder """
        ...

    def GroupByScriptBlock(self, scriptBlock:str, customControl:CustomControl, label:str) -> TableControlBuilder:
        """ GroupByScriptBlock(self: TableControlBuilder, scriptBlock: str, customControl: CustomControl, label: str) -> TableControlBuilder """
        ...

    def StartRowDefinition(self, wrap:bool, entrySelectedByType:IEnumerable, entrySelectedByCondition:IEnumerable) -> TableRowDefinitionBuilder:
        """ StartRowDefinition(self: TableControlBuilder, wrap: bool, entrySelectedByType: IEnumerable[str], entrySelectedByCondition: IEnumerable[DisplayEntry]) -> TableRowDefinitionBuilder """
        ...


class TableControlColumn: # skipped bases: <type 'object'>, <type 'object'>
    """
    TableControlColumn()
    TableControlColumn(alignment: Alignment, entry: DisplayEntry)
    """
    @property
    def Alignment(self) -> Alignment:
        """
        Get: Alignment(self: TableControlColumn) -> Alignment
        Set: Alignment(self: TableControlColumn) = value
        """
        ...

    @property
    def DisplayEntry(self) -> DisplayEntry:
        """
        Get: DisplayEntry(self: TableControlColumn) -> DisplayEntry
        Set: DisplayEntry(self: TableControlColumn) = value
        """
        ...

    @property
    def FormatString(self) -> str:
        """ Get: FormatString(self: TableControlColumn) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: TableControlColumn) -> str """
        ...


class TableControlColumnHeader: # skipped bases: <type 'object'>, <type 'object'>
    """
    TableControlColumnHeader()
    TableControlColumnHeader(label: str, width: int, alignment: Alignment)
    """
    @property
    def Alignment(self) -> Alignment:
        """
        Get: Alignment(self: TableControlColumnHeader) -> Alignment
        Set: Alignment(self: TableControlColumnHeader) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: TableControlColumnHeader) -> str
        Set: Label(self: TableControlColumnHeader) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: TableControlColumnHeader) -> int
        Set: Width(self: TableControlColumnHeader) = value
        """
        ...



class TableControlRow: # skipped bases: <type 'object'>, <type 'object'>
    """
    TableControlRow()
    TableControlRow(columns: IEnumerable[TableControlColumn])
    """
    @property
    def Columns(self) -> List:
        """
        Get: Columns(self: TableControlRow) -> List[TableControlColumn]
        Set: Columns(self: TableControlRow) = value
        """
        ...

    @property
    def SelectedBy(self) -> EntrySelectedBy:
        """ Get: SelectedBy(self: TableControlRow) -> EntrySelectedBy """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: TableControlRow) -> bool
        Set: Wrap(self: TableControlRow) = value
        """
        ...



class TableRowDefinitionBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddPropertyColumn(self, propertyName:str, alignment:Alignment, format:str) -> TableRowDefinitionBuilder:
        """ AddPropertyColumn(self: TableRowDefinitionBuilder, propertyName: str, alignment: Alignment, format: str) -> TableRowDefinitionBuilder """
        ...

    def AddScriptBlockColumn(self, scriptBlock:str, alignment:Alignment, format:str) -> TableRowDefinitionBuilder:
        """ AddScriptBlockColumn(self: TableRowDefinitionBuilder, scriptBlock: str, alignment: Alignment, format: str) -> TableRowDefinitionBuilder """
        ...

    def EndRowDefinition(self) -> TableControlBuilder:
        """ EndRowDefinition(self: TableRowDefinitionBuilder) -> TableControlBuilder """
        ...


class TerminateException(FlowControlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ TerminateException() """
    SerializeObjectState = ...


class ValidateArgumentsAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    def Validate(self, *args): #cannot find CLR method
        """ Validate(self: ValidateArgumentsAttribute, arguments: object, engineIntrinsics: EngineIntrinsics) """
        ...


class ValidateCountAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateCountAttribute(minLength: int, maxLength: int) """
    @property
    def MaxLength(self) -> int:
        """ Get: MaxLength(self: ValidateCountAttribute) -> int """
        ...

    @property
    def MinLength(self) -> int:
        """ Get: MinLength(self: ValidateCountAttribute) -> int """
        ...


    def __new__(cls, minLength:int, maxLength:int) -> Self:
        """ __new__(cls: type, minLength: int, maxLength: int) """
        ...


class ValidateDriveAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateDriveAttribute(*validRootDrives: Array[str]) """
    def __new__(cls, validRootDrives:Array) -> Self:
        """ __new__(cls: type, *validRootDrives: Array[str]) """
        ...


class ValidateEnumeratedArgumentsAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    def ValidateElement(self, *args): #cannot find CLR method
        """ ValidateElement(self: ValidateEnumeratedArgumentsAttribute, element: object) """
        ...


class ValidateLengthAttribute(ValidateEnumeratedArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateLengthAttribute(minLength: int, maxLength: int) """
    @property
    def MaxLength(self) -> int:
        """ Get: MaxLength(self: ValidateLengthAttribute) -> int """
        ...

    @property
    def MinLength(self) -> int:
        """ Get: MinLength(self: ValidateLengthAttribute) -> int """
        ...


    def __new__(cls, minLength:int, maxLength:int) -> Self:
        """ __new__(cls: type, minLength: int, maxLength: int) """
        ...


class ValidateNotNullAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateNotNullAttribute() """
    pass

class ValidateNotNullOrEmptyAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateNotNullOrEmptyAttribute() """
    pass

class ValidatePatternAttribute(ValidateEnumeratedArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidatePatternAttribute(regexPattern: str) """
    @property
    def Options(self) -> RegexOptions:
        """
        Get: Options(self: ValidatePatternAttribute) -> RegexOptions
        Set: Options(self: ValidatePatternAttribute) = value
        """
        ...

    @property
    def RegexPattern(self) -> str:
        """ Get: RegexPattern(self: ValidatePatternAttribute) -> str """
        ...


    def __new__(cls, regexPattern:str) -> Self:
        """ __new__(cls: type, regexPattern: str) """
        ...


class ValidateRangeAttribute(ValidateEnumeratedArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateRangeAttribute(minRange: object, maxRange: object) """
    @property
    def MaxRange(self) -> object:
        """ Get: MaxRange(self: ValidateRangeAttribute) -> object """
        ...

    @property
    def MinRange(self) -> object:
        """ Get: MinRange(self: ValidateRangeAttribute) -> object """
        ...


    def __new__(cls, minRange:object, maxRange:object) -> Self:
        """ __new__(cls: type, minRange: object, maxRange: object) """
        ...


class ValidateScriptAttribute(ValidateEnumeratedArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateScriptAttribute(scriptBlock: ScriptBlock) """
    @property
    def ScriptBlock(self) -> ScriptBlock:
        """ Get: ScriptBlock(self: ValidateScriptAttribute) -> ScriptBlock """
        ...


    def __new__(cls, scriptBlock:ScriptBlock) -> Self:
        """ __new__(cls: type, scriptBlock: ScriptBlock) """
        ...


class ValidateSetAttribute(ValidateEnumeratedArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateSetAttribute(*validValues: Array[str]) """
    @property
    def IgnoreCase(self) -> bool:
        """
        Get: IgnoreCase(self: ValidateSetAttribute) -> bool
        Set: IgnoreCase(self: ValidateSetAttribute) = value
        """
        ...

    @property
    def ValidValues(self) -> IList:
        """ Get: ValidValues(self: ValidateSetAttribute) -> IList[str] """
        ...


    def __new__(cls, validValues:Array) -> Self:
        """ __new__(cls: type, *validValues: Array[str]) """
        ...


class ValidateTrustedDataAttribute(ValidateArgumentsAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateTrustedDataAttribute() """
    pass

class ValidateUserDriveAttribute(ValidateDriveAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidateUserDriveAttribute() """
    pass

class ValidationMetadataException(MetadataException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ValidationMetadataException()
    ValidationMetadataException(message: str)
    ValidationMetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class VariableAccessMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VariableAccessMode, values: Read (0), ReadWrite (2), Write (1) """
    Read: VariableAccessMode = ...
    ReadWrite: VariableAccessMode = ...
    value__ = ...
    Write: VariableAccessMode = ...


class VariableBreakpoint(Breakpoint): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessMode(self) -> VariableAccessMode:
        """ Get: AccessMode(self: VariableBreakpoint) -> VariableAccessMode """
        ...

    @property
    def Variable(self) -> str:
        """ Get: Variable(self: VariableBreakpoint) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: VariableBreakpoint) -> str """
        ...


class VariablePath: # skipped bases: <type 'object'>, <type 'object'>
    """ VariablePath(path: str) """
    @property
    def DriveName(self) -> str:
        """ Get: DriveName(self: VariablePath) -> str """
        ...

    @property
    def IsDriveQualified(self) -> bool:
        """ Get: IsDriveQualified(self: VariablePath) -> bool """
        ...

    @property
    def IsGlobal(self) -> bool:
        """ Get: IsGlobal(self: VariablePath) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: VariablePath) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: VariablePath) -> bool """
        ...

    @property
    def IsScript(self) -> bool:
        """ Get: IsScript(self: VariablePath) -> bool """
        ...

    @property
    def IsUnqualified(self) -> bool:
        """ Get: IsUnqualified(self: VariablePath) -> bool """
        ...

    @property
    def IsUnscopedVariable(self) -> bool:
        """ Get: IsUnscopedVariable(self: VariablePath) -> bool """
        ...

    @property
    def IsVariable(self) -> bool:
        """ Get: IsVariable(self: VariablePath) -> bool """
        ...

    @property
    def UserPath(self) -> str:
        """ Get: UserPath(self: VariablePath) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: VariablePath) -> str """
        ...


class VerboseRecord(InformationalRecord): # skipped bases: <type 'object'>
    """
    VerboseRecord(message: str)
    VerboseRecord(record: PSObject)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, message: str)
        __new__(cls: type, record: PSObject)
        """
        ...


class VerbsCommon: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Add: str = ...
    Clear: str = ...
    Close: str = ...
    Copy: str = ...
    Enter: str = ...
    Exit: str = ...
    Find: str = ...
    Format: str = ...
    Get: str = ...
    Hide: str = ...
    Join: str = ...
    Lock: str = ...
    Move: str = ...
    New: str = ...
    Open: str = ...
    Optimize: str = ...
    Pop: str = ...
    Push: str = ...
    Redo: str = ...
    Remove: str = ...
    Rename: str = ...
    Reset: str = ...
    Resize: str = ...
    Search: str = ...
    Select: str = ...
    Set: str = ...
    Show: str = ...
    Skip: str = ...
    Split: str = ...
    Step: str = ...
    Switch: str = ...
    Undo: str = ...
    Unlock: str = ...
    Watch: str = ...
    __all__: list = ...


class VerbsCommunications: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Connect: str = ...
    Disconnect: str = ...
    Read: str = ...
    Receive: str = ...
    Send: str = ...
    Write: str = ...
    __all__: list = ...


class VerbsData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Backup: str = ...
    Checkpoint: str = ...
    Compare: str = ...
    Compress: str = ...
    Convert: str = ...
    ConvertFrom: str = ...
    ConvertTo: str = ...
    Dismount: str = ...
    Edit: str = ...
    Expand: str = ...
    Export: str = ...
    Group: str = ...
    Import: str = ...
    Initialize: str = ...
    Limit: str = ...
    Merge: str = ...
    Mount: str = ...
    Out: str = ...
    Publish: str = ...
    Restore: str = ...
    Save: str = ...
    Sync: str = ...
    Unpublish: str = ...
    Update: str = ...
    __all__: list = ...


class VerbsDiagnostic: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Debug: str = ...
    Measure: str = ...
    Ping: str = ...
    Repair: str = ...
    Resolve: str = ...
    Test: str = ...
    Trace: str = ...
    __all__: list = ...


class VerbsLifecycle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Approve: str = ...
    Assert: str = ...
    Complete: str = ...
    Confirm: str = ...
    Deny: str = ...
    Disable: str = ...
    Enable: str = ...
    Install: str = ...
    Invoke: str = ...
    Register: str = ...
    Request: str = ...
    Restart: str = ...
    Resume: str = ...
    Start: str = ...
    Stop: str = ...
    Submit: str = ...
    Suspend: str = ...
    Uninstall: str = ...
    Unregister: str = ...
    Wait: str = ...
    __all__: list = ...


class VerbsOther: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Use: str = ...
    __all__: list = ...


class VerbsSecurity: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Block: str = ...
    Grant: str = ...
    Protect: str = ...
    Revoke: str = ...
    Unblock: str = ...
    Unprotect: str = ...
    __all__: list = ...


class WarningRecord(InformationalRecord): # skipped bases: <type 'object'>
    """
    WarningRecord(message: str)
    WarningRecord(record: PSObject)
    WarningRecord(fullyQualifiedWarningId: str, message: str)
    WarningRecord(fullyQualifiedWarningId: str, record: PSObject)
    """
    @property
    def FullyQualifiedWarningId(self) -> str:
        """ Get: FullyQualifiedWarningId(self: WarningRecord) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, message: str)
        __new__(cls: type, record: PSObject)
        __new__(cls: type, fullyQualifiedWarningId: str, message: str)
        __new__(cls: type, fullyQualifiedWarningId: str, record: PSObject)
        """
        ...


class WhereOperatorSelectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WhereOperatorSelectionMode, values: Default (0), First (1), Last (2), SkipUntil (3), Split (5), Until (4) """
    Default: WhereOperatorSelectionMode = ...
    First: WhereOperatorSelectionMode = ...
    Last: WhereOperatorSelectionMode = ...
    SkipUntil: WhereOperatorSelectionMode = ...
    Split: WhereOperatorSelectionMode = ...
    Until: WhereOperatorSelectionMode = ...
    value__ = ...


class WideControl(PSControl): # skipped bases: <type 'object'>
    """
    WideControl()
    WideControl(wideEntries: IEnumerable[WideControlEntryItem])
    WideControl(wideEntries: IEnumerable[WideControlEntryItem], columns: UInt32)
    WideControl(columns: UInt32)
    """
    @property
    def AutoSize(self) -> bool:
        """
        Get: AutoSize(self: WideControl) -> bool
        Set: AutoSize(self: WideControl) = value
        """
        ...

    @property
    def Columns(self) -> UInt32:
        """ Get: Columns(self: WideControl) -> UInt32 """
        ...

    @property
    def Entries(self) -> List:
        """ Get: Entries(self: WideControl) -> List[WideControlEntryItem] """
        ...


    @staticmethod
    def Create(outOfBand:bool, autoSize:bool, columns:UInt32) -> WideControlBuilder:
        """ Create(outOfBand: bool, autoSize: bool, columns: UInt32) -> WideControlBuilder """
        ...

    def __new__(cls, *__args:IEnumerable) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, wideEntries: IEnumerable[WideControlEntryItem])
        __new__(cls: type, wideEntries: IEnumerable[WideControlEntryItem], columns: UInt32)
        __new__(cls: type, columns: UInt32)
        """
        ...


class WideControlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddPropertyEntry(self, propertyName:str, format:str, entrySelectedByType:IEnumerable, entrySelectedByCondition:IEnumerable) -> WideControlBuilder:
        """ AddPropertyEntry(self: WideControlBuilder, propertyName: str, format: str, entrySelectedByType: IEnumerable[str], entrySelectedByCondition: IEnumerable[DisplayEntry]) -> WideControlBuilder """
        ...

    def AddScriptBlockEntry(self, scriptBlock:str, format:str, entrySelectedByType:IEnumerable, entrySelectedByCondition:IEnumerable) -> WideControlBuilder:
        """ AddScriptBlockEntry(self: WideControlBuilder, scriptBlock: str, format: str, entrySelectedByType: IEnumerable[str], entrySelectedByCondition: IEnumerable[DisplayEntry]) -> WideControlBuilder """
        ...

    def EndWideControl(self) -> WideControl:
        """ EndWideControl(self: WideControlBuilder) -> WideControl """
        ...

    def GroupByProperty(self, property:str, customControl:CustomControl, label:str) -> WideControlBuilder:
        """ GroupByProperty(self: WideControlBuilder, property: str, customControl: CustomControl, label: str) -> WideControlBuilder """
        ...

    def GroupByScriptBlock(self, scriptBlock:str, customControl:CustomControl, label:str) -> WideControlBuilder:
        """ GroupByScriptBlock(self: WideControlBuilder, scriptBlock: str, customControl: CustomControl, label: str) -> WideControlBuilder """
        ...


class WideControlEntryItem: # skipped bases: <type 'object'>, <type 'object'>
    """
    WideControlEntryItem(entry: DisplayEntry)
    WideControlEntryItem(entry: DisplayEntry, selectedBy: IEnumerable[str])
    """
    @property
    def DisplayEntry(self) -> DisplayEntry:
        """ Get: DisplayEntry(self: WideControlEntryItem) -> DisplayEntry """
        ...

    @property
    def EntrySelectedBy(self) -> EntrySelectedBy:
        """ Get: EntrySelectedBy(self: WideControlEntryItem) -> EntrySelectedBy """
        ...

    @property
    def FormatString(self) -> str:
        """ Get: FormatString(self: WideControlEntryItem) -> str """
        ...

    @property
    def SelectedBy(self) -> List:
        """ Get: SelectedBy(self: WideControlEntryItem) -> List[str] """
        ...



class WildcardOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WildcardOptions, values: Compiled (1), CultureInvariant (4), IgnoreCase (2), None (0) """
    Compiled: WildcardOptions = ...
    CultureInvariant: WildcardOptions = ...
    IgnoreCase: WildcardOptions = ...
    value__ = ...


class WildcardPattern: # skipped bases: <type 'object'>, <type 'object'>
    """
    WildcardPattern(pattern: str)
    WildcardPattern(pattern: str, options: WildcardOptions)
    """
    @staticmethod
    def ContainsWildcardCharacters(pattern:str) -> bool:
        """ ContainsWildcardCharacters(pattern: str) -> bool """
        ...

    @staticmethod
    def Escape(pattern:str) -> str:
        """ Escape(pattern: str) -> str """
        ...

    @staticmethod
    def Get(pattern:str, options:WildcardOptions) -> WildcardPattern:
        """ Get(pattern: str, options: WildcardOptions) -> WildcardPattern """
        ...

    def IsMatch(self, input:str) -> bool:
        """ IsMatch(self: WildcardPattern, input: str) -> bool """
        ...

    def ToWql(self) -> str:
        """ ToWql(self: WildcardPattern) -> str """
        ...

    @staticmethod
    def Unescape(pattern:str) -> str:
        """ Unescape(pattern: str) -> str """
        ...


class WildcardPatternException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WildcardPatternException()
    WildcardPatternException(message: str)
    WildcardPatternException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowInfo(FunctionInfo): # skipped bases: <type 'IHasSessionStateEntryVisibility'>, <type 'IScriptCommandInfo'>, <type 'object'>
    """
    WorkflowInfo(name: str, definition: str, workflow: ScriptBlock, xamlDefinition: str, workflowsCalled: Array[WorkflowInfo])
    WorkflowInfo(name: str, definition: str, workflow: ScriptBlock, xamlDefinition: str, workflowsCalled: Array[WorkflowInfo], module: PSModuleInfo)
    """
    @property
    def NestedXamlDefinition(self) -> str:
        """
        Get: NestedXamlDefinition(self: WorkflowInfo) -> str
        Set: NestedXamlDefinition(self: WorkflowInfo) = value
        """
        ...

    @property
    def WorkflowsCalled(self) -> ReadOnlyCollection:
        """ Get: WorkflowsCalled(self: WorkflowInfo) -> ReadOnlyCollection[WorkflowInfo] """
        ...

    @property
    def XamlDefinition(self) -> str:
        """ Get: XamlDefinition(self: WorkflowInfo) -> str """
        ...


    def __new__(cls, name:str, definition:str, workflow:ScriptBlock, xamlDefinition:str, workflowsCalled:Array, module:PSModuleInfo = ...) -> Self:
        """
        __new__(cls: type, name: str, definition: str, workflow: ScriptBlock, xamlDefinition: str, workflowsCalled: Array[WorkflowInfo])
        __new__(cls: type, name: str, definition: str, workflow: ScriptBlock, xamlDefinition: str, workflowsCalled: Array[WorkflowInfo], module: PSModuleInfo)
        """
        ...


# variables with complex values

