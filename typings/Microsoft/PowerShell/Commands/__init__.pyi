# encoding: utf-8
# module Microsoft.PowerShell.Commands calls itself Commands
# from Microsoft.PowerShell.ConsoleHost, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Management, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Utility, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Security, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.PowerShell.Commands.Diagnostics, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import ScriptBlock

from Microsoft.PowerShell import ExecutionPolicy, ExecutionPolicyScope

from Microsoft.PowerShell.Commands.Internal.Format import (
    FrontEndCommandBase, OuterFormatShapeCommandBase, 
    OuterFormatTableAndListBase, OuterFormatTableBase)

from Microsoft.SqlServer.Management.Smo import Language

from Microsoft.VisualBasic import Collection, OpenMode

from Microsoft.Win32 import RegistryValueKind

from Microsoft.WSMan.Management import (AuthenticationMechanism, 
    ProxyAccessType)

from mshtml import IHTMLDocument2

from System import (ArgumentException, Array, Byte, Char, ConsoleColor, 
    DateTime, Enum, Guid, ICloneable, IDisposable, Int16, Int64, Nullable, 
    SystemException, TimeSpan, TimeZoneInfo, Type, UInt32, Uri, Version)

from System.CodeDom.Compiler import CodeDomProvider, CompilerParameters

from System.Collections import (ArrayList, Hashtable, IDictionary, 
    IEnumerable)

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Diagnostics import (EventLogEntryType, OverflowAction, Process, 
    ProcessWindowStyle, TraceOptions)

from System.Globalization import CultureInfo

from System.IO import MemoryStream

from System.Management import (AuthenticationLevel, ImpersonationLevel, 
    ManagementObject, PutType)

from System.Management.Automation import (Cmdlet, CommandTypes, ErrorCategory, 
    ErrorRecord, IArgumentCompleter, IContainsErrorRecord, IDynamicParameters, 
    Job, JobState, PSCmdlet, PSCredential, PSLanguageMode, PSMemberTypes, 
    PSMemberViewTypes, PSObject, PSPrimitiveDictionary, PSSessionTypeOption, 
    PSSnapIn, PSTraceSourceOptions, PSTransportOption, RollbackSeverity, 
    RuntimeException, ScopedItemOptions, SessionStateEntryVisibility, 
    SwitchParameter, VariableAccessMode)

from System.Management.Automation.Provider import (ContainerCmdletProvider, 
    ICmdletProviderSupportsHelp, IContentCmdletProvider, IContentReader, 
    IContentWriter, IDynamicPropertyCmdletProvider, IPropertyCmdletProvider, 
    ISecurityDescriptorCmdletProvider, NavigationCmdletProvider)

from System.Management.Automation.Remoting import (PSSessionOption, 
    SessionType)

from System.Management.Automation.Runspaces import (OutputBufferingMode, 
    PSSession, PSSessionConfigurationAccessMode, PSSessionType, 
    PSThreadOptions, PipelineState, Runspace, TypeData)

from System.Net import CookieContainer, ICredentials, IWebProxy, WebResponse

from System.Net.Mail import DeliveryNotificationOptions, MailPriority

from System.Reflection import ProcessorArchitecture

from System.Security import SecureString

from System.Security.Cryptography.X509Certificates import (StoreLocation, 
    X509Certificate, X509Certificate2, X509CertificateCollection)

from System.Security.Principal import SecurityIdentifier

from System.ServiceProcess import ServiceStartMode

from System.Text import Encoding

from System.Threading import ApartmentState

from System.Web.Configuration import AuthorizationRuleCollection

from System.Windows.Forms import PowerState, TextDataFormat

from System.Xml import XmlDocument, XmlNode

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, CimSession, 
    ExportAliasFormat, JoinOptions, MatchInfoContext, OutputAssemblyType, 
    OutputModeOption, PSHostProcessInfo, SessionFilterState, TestPathType, 
    WaitForServiceTypes, WebCmdletElementCollection, WebRequestMethod, 
    WebRequestSession, field#)
"""

# no functions
# classes

class AddComputerCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ AddComputerCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: AddComputerCommand) -> Array[str]
        Set: ComputerName(self: AddComputerCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: AddComputerCommand) -> PSCredential
        Set: Credential(self: AddComputerCommand) = value
        """
        ...

    @property
    def DomainName(self) -> str:
        """
        Get: DomainName(self: AddComputerCommand) -> str
        Set: DomainName(self: AddComputerCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: AddComputerCommand) -> SwitchParameter
        Set: Force(self: AddComputerCommand) = value
        """
        ...

    @property
    def LocalCredential(self) -> PSCredential:
        """
        Get: LocalCredential(self: AddComputerCommand) -> PSCredential
        Set: LocalCredential(self: AddComputerCommand) = value
        """
        ...

    @property
    def NewName(self) -> str:
        """
        Get: NewName(self: AddComputerCommand) -> str
        Set: NewName(self: AddComputerCommand) = value
        """
        ...

    @property
    def Options(self): # -> JoinOptions
        """
        Get: Options(self: AddComputerCommand) -> JoinOptions
        Set: Options(self: AddComputerCommand) = value
        """
        ...

    @property
    def OUPath(self) -> str:
        """
        Get: OUPath(self: AddComputerCommand) -> str
        Set: OUPath(self: AddComputerCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: AddComputerCommand) -> SwitchParameter
        Set: PassThru(self: AddComputerCommand) = value
        """
        ...

    @property
    def Restart(self) -> SwitchParameter:
        """
        Get: Restart(self: AddComputerCommand) -> SwitchParameter
        Set: Restart(self: AddComputerCommand) = value
        """
        ...

    @property
    def Server(self) -> str:
        """
        Get: Server(self: AddComputerCommand) -> str
        Set: Server(self: AddComputerCommand) = value
        """
        ...

    @property
    def UnjoinDomainCredential(self) -> PSCredential:
        """
        Get: UnjoinDomainCredential(self: AddComputerCommand) -> PSCredential
        Set: UnjoinDomainCredential(self: AddComputerCommand) = value
        """
        ...

    @property
    def Unsecure(self) -> SwitchParameter:
        """
        Get: Unsecure(self: AddComputerCommand) -> SwitchParameter
        Set: Unsecure(self: AddComputerCommand) = value
        """
        ...

    @property
    def WorkgroupName(self) -> str:
        """
        Get: WorkgroupName(self: AddComputerCommand) -> str
        Set: WorkgroupName(self: AddComputerCommand) = value
        """
        ...



class CoreCommandBase(PSCmdlet, IDynamicParameters): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: CoreCommandBase) -> Array[str]
        Set: Exclude(self: CoreCommandBase) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: CoreCommandBase) -> str
        Set: Filter(self: CoreCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: CoreCommandBase) -> SwitchParameter
        Set: Force(self: CoreCommandBase) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: CoreCommandBase) -> Array[str]
        Set: Include(self: CoreCommandBase) = value
        """
        ...

    @property
    def ProviderSupportsShouldProcess(self):
        ...

    @property
    def RetrievedDynamicParameters(self):
        ...

    @property
    def SupportsShouldProcess(self) -> bool:
        """ Get: SupportsShouldProcess(self: CoreCommandBase) -> bool """
        ...


    def DoesProviderSupportShouldProcess(self, *args): #cannot find CLR method
        """ DoesProviderSupportShouldProcess(self: CoreCommandBase, paths: Array[str]) -> bool """
        ...


class CoreCommandWithCredentialsBase(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ CoreCommandWithCredentialsBase() """
    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: CoreCommandWithCredentialsBase) -> PSCredential
        Set: Credential(self: CoreCommandWithCredentialsBase) = value
        """
        ...



class ContentCommandBase(IDisposable, CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ContentCommandBase() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: ContentCommandBase) -> Array[str]
        Set: Exclude(self: ContentCommandBase) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: ContentCommandBase) -> str
        Set: Filter(self: ContentCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ContentCommandBase) -> SwitchParameter
        Set: Force(self: ContentCommandBase) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: ContentCommandBase) -> Array[str]
        Set: Include(self: ContentCommandBase) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ContentCommandBase) -> Array[str]
        Set: LiteralPath(self: ContentCommandBase) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ContentCommandBase) -> Array[str]
        Set: Path(self: ContentCommandBase) = value
        """
        ...



class PassThroughContentCommandBase(ContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ PassThroughContentCommandBase() """
    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: PassThroughContentCommandBase) -> SwitchParameter
        Set: PassThru(self: PassThroughContentCommandBase) = value
        """
        ...



class WriteContentCommandBase(PassThroughContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ WriteContentCommandBase() """
    @property
    def Value(self) -> Array:
        """
        Get: Value(self: WriteContentCommandBase) -> Array[object]
        Set: Value(self: WriteContentCommandBase) = value
        """
        ...



class AddContentCommand(WriteContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ AddContentCommand() """
    pass

class AddHistoryCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ AddHistoryCommand() """
    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: AddHistoryCommand) -> Array[PSObject]
        Set: InputObject(self: AddHistoryCommand) = value
        """
        ...

    @property
    def Passthru(self) -> SwitchParameter:
        """
        Get: Passthru(self: AddHistoryCommand) -> SwitchParameter
        Set: Passthru(self: AddHistoryCommand) = value
        """
        ...



class AddMemberCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ AddMemberCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: AddMemberCommand) -> SwitchParameter
        Set: Force(self: AddMemberCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: AddMemberCommand) -> PSObject
        Set: InputObject(self: AddMemberCommand) = value
        """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """
        Get: MemberType(self: AddMemberCommand) -> PSMemberTypes
        Set: MemberType(self: AddMemberCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: AddMemberCommand) -> str
        Set: Name(self: AddMemberCommand) = value
        """
        ...

    @property
    def NotePropertyMembers(self) -> IDictionary:
        """
        Get: NotePropertyMembers(self: AddMemberCommand) -> IDictionary
        Set: NotePropertyMembers(self: AddMemberCommand) = value
        """
        ...

    @property
    def NotePropertyName(self) -> str:
        """
        Get: NotePropertyName(self: AddMemberCommand) -> str
        Set: NotePropertyName(self: AddMemberCommand) = value
        """
        ...

    @property
    def NotePropertyValue(self) -> object:
        """
        Get: NotePropertyValue(self: AddMemberCommand) -> object
        Set: NotePropertyValue(self: AddMemberCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: AddMemberCommand) -> SwitchParameter
        Set: PassThru(self: AddMemberCommand) = value
        """
        ...

    @property
    def SecondValue(self) -> object:
        """
        Get: SecondValue(self: AddMemberCommand) -> object
        Set: SecondValue(self: AddMemberCommand) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: AddMemberCommand) -> str
        Set: TypeName(self: AddMemberCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: AddMemberCommand) -> object
        Set: Value(self: AddMemberCommand) = value
        """
        ...



class PSSnapInCommandBase(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ShouldGetAll(self):
        ...


    def GetSnapIns(self, *args): #cannot find CLR method
        """ GetSnapIns(self: PSSnapInCommandBase, pattern: str) -> Collection[PSSnapInInfo] """
        ...


class AddPSSnapinCommand(PSSnapInCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ AddPSSnapinCommand() """
    @property
    def Name(self) -> Array:
        """
        Get: Name(self: AddPSSnapinCommand) -> Array[str]
        Set: Name(self: AddPSSnapinCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: AddPSSnapinCommand) -> SwitchParameter
        Set: PassThru(self: AddPSSnapinCommand) = value
        """
        ...



class AddTypeCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> Array:
        """
        Get: AssemblyName(self: AddTypeCommandBase) -> Array[str]
        Set: AssemblyName(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def IgnoreWarnings(self) -> SwitchParameter:
        """
        Get: IgnoreWarnings(self: AddTypeCommandBase) -> SwitchParameter
        Set: IgnoreWarnings(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def Language(self) -> Language:
        """
        Get: Language(self: AddTypeCommandBase) -> Language
        Set: Language(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: AddTypeCommandBase) -> Array[str]
        Set: LiteralPath(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def MemberDefinition(self) -> Array:
        """
        Get: MemberDefinition(self: AddTypeCommandBase) -> Array[str]
        Set: MemberDefinition(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: AddTypeCommandBase) -> str
        Set: Name(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: AddTypeCommandBase) -> str
        Set: Namespace(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def OutputAssembly(self) -> str:
        """
        Get: OutputAssembly(self: AddTypeCommandBase) -> str
        Set: OutputAssembly(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def OutputType(self): # -> OutputAssemblyType
        """
        Get: OutputType(self: AddTypeCommandBase) -> OutputAssemblyType
        Set: OutputType(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: AddTypeCommandBase) -> SwitchParameter
        Set: PassThru(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: AddTypeCommandBase) -> Array[str]
        Set: Path(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def ReferencedAssemblies(self) -> Array:
        """
        Get: ReferencedAssemblies(self: AddTypeCommandBase) -> Array[str]
        Set: ReferencedAssemblies(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def TypeDefinition(self) -> str:
        """
        Get: TypeDefinition(self: AddTypeCommandBase) -> str
        Set: TypeDefinition(self: AddTypeCommandBase) = value
        """
        ...

    @property
    def UsingNamespace(self) -> Array:
        """
        Get: UsingNamespace(self: AddTypeCommandBase) -> Array[str]
        Set: UsingNamespace(self: AddTypeCommandBase) = value
        """
        ...



class AddTypeCommand(AddTypeCommandBase): # skipped bases: <type 'object'>
    """ AddTypeCommand() """
    @property
    def CodeDomProvider(self) -> CodeDomProvider:
        """
        Get: CodeDomProvider(self: AddTypeCommand) -> CodeDomProvider
        Set: CodeDomProvider(self: AddTypeCommand) = value
        """
        ...

    @property
    def CompilerParameters(self) -> CompilerParameters:
        """
        Get: CompilerParameters(self: AddTypeCommand) -> CompilerParameters
        Set: CompilerParameters(self: AddTypeCommand) = value
        """
        ...



class AddTypeCompilerError: # skipped bases: <type 'object'>, <type 'object'>
    """ AddTypeCompilerError() """
    @property
    def Column(self) -> int:
        """ Get: Column(self: AddTypeCompilerError) -> int """
        ...

    @property
    def ErrorNumber(self) -> str:
        """ Get: ErrorNumber(self: AddTypeCompilerError) -> str """
        ...

    @property
    def ErrorText(self) -> str:
        """ Get: ErrorText(self: AddTypeCompilerError) -> str """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: AddTypeCompilerError) -> str """
        ...

    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: AddTypeCompilerError) -> bool """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: AddTypeCompilerError) -> int """
        ...



class AdminPasswordStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AdminPasswordStatus, values: Disabled (0), Enabled (1), NotImplemented (2), Unknown (3) """
    Disabled: AdminPasswordStatus = ...
    Enabled: AdminPasswordStatus = ...
    NotImplemented: AdminPasswordStatus = ...
    Unknown: AdminPasswordStatus = ...
    value__ = ...


class SessionStateProviderBase(ContainerCmdletProvider, IContentCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ no doc """
    pass

class AliasProvider(SessionStateProviderBase): # skipped bases: <type 'IResourceSupplier'>, <type 'IContentCmdletProvider'>, <type 'object'>
    """ AliasProvider() """
    ProviderName: str = ...


class AliasProviderDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ AliasProviderDynamicParameters() """
    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: AliasProviderDynamicParameters) -> ScopedItemOptions
        Set: Options(self: AliasProviderDynamicParameters) = value
        """
        ...



class BaseCsvWritingCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Delimiter(self) -> Char:
        """
        Get: Delimiter(self: BaseCsvWritingCommand) -> Char
        Set: Delimiter(self: BaseCsvWritingCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: BaseCsvWritingCommand) -> PSObject
        Set: InputObject(self: BaseCsvWritingCommand) = value
        """
        ...

    @property
    def NoTypeInformation(self) -> SwitchParameter:
        """
        Get: NoTypeInformation(self: BaseCsvWritingCommand) -> SwitchParameter
        Set: NoTypeInformation(self: BaseCsvWritingCommand) = value
        """
        ...

    @property
    def UseCulture(self) -> SwitchParameter:
        """
        Get: UseCulture(self: BaseCsvWritingCommand) -> SwitchParameter
        Set: UseCulture(self: BaseCsvWritingCommand) = value
        """
        ...


    def WriteCsvLine(self, line:str): # -> 
        """ WriteCsvLine(self: BaseCsvWritingCommand, line: str) """
        ...


class WebResponseObject: # skipped bases: <type 'object'>, <type 'object'>
    """
    WebResponseObject(response: WebResponse)
    WebResponseObject(response: WebResponse, contentStream: Stream)
    """
    @property
    def BaseResponse(self) -> WebResponse:
        """
        Get: BaseResponse(self: WebResponseObject) -> WebResponse
        Set: BaseResponse(self: WebResponseObject) = value
        """
        ...

    @property
    def Content(self) -> Array:
        """ Get: Content(self: WebResponseObject) -> Array[Byte] """
        ...

    @property
    def Headers(self) -> Dictionary:
        """ Get: Headers(self: WebResponseObject) -> Dictionary[str, str] """
        ...

    @property
    def RawContent(self) -> str:
        """ Get: RawContent(self: WebResponseObject) -> str """
        ...

    @property
    def RawContentLength(self) -> Int64:
        """ Get: RawContentLength(self: WebResponseObject) -> Int64 """
        ...

    @property
    def RawContentStream(self) -> MemoryStream:
        """ Get: RawContentStream(self: WebResponseObject) -> MemoryStream """
        ...

    @property
    def StatusCode(self) -> int:
        """ Get: StatusCode(self: WebResponseObject) -> int """
        ...

    @property
    def StatusDescription(self) -> str:
        """ Get: StatusDescription(self: WebResponseObject) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: WebResponseObject) -> str """
        ...


class BasicHtmlWebResponseObject(WebResponseObject): # skipped bases: <type 'object'>
    """
    BasicHtmlWebResponseObject(response: WebResponse)
    BasicHtmlWebResponseObject(response: WebResponse, contentStream: Stream)
    """
    @property
    def Images(self): # -> WebCmdletElementCollection
        """ Get: Images(self: BasicHtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def InputFields(self): # -> WebCmdletElementCollection
        """ Get: InputFields(self: BasicHtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def Links(self): # -> WebCmdletElementCollection
        """ Get: Links(self: BasicHtmlWebResponseObject) -> WebCmdletElementCollection """
        ...



class BootOptionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BootOptionAction, values: DoNotReboot (3), OperatingSystem (1), SystemUtilities (2) """
    DoNotReboot: BootOptionAction = ...
    OperatingSystem: BootOptionAction = ...
    SystemUtilities: BootOptionAction = ...
    value__ = ...


class BreakpointType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BreakpointType, values: Command (2), Line (0), Variable (1) """
    Command: BreakpointType = ...
    Line: BreakpointType = ...
    value__ = ...
    Variable: BreakpointType = ...


class ByteCollection: # skipped bases: <type 'object'>, <type 'object'>
    """
    ByteCollection(offset: UInt32, value: Array[Byte], path: str)
    ByteCollection(offset: UInt32, value: Array[Byte])
    ByteCollection(value: Array[Byte])
    """
    @property
    def Bytes(self) -> Array:
        """ Get: Bytes(self: ByteCollection) -> Array[Byte] """
        ...

    @property
    def Offset(self) -> UInt32:
        """ Get: Offset(self: ByteCollection) -> UInt32 """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ByteCollection) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: ByteCollection) -> str """
        ...


class CatalogCommandsBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CatalogFilePath(self) -> str:
        """
        Get: CatalogFilePath(self: CatalogCommandsBase) -> str
        Set: CatalogFilePath(self: CatalogCommandsBase) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: CatalogCommandsBase) -> Array[str]
        Set: Path(self: CatalogCommandsBase) = value
        """
        ...


    def PerformAction(self, *args): #cannot find CLR method
        """ PerformAction(self: CatalogCommandsBase, path: Collection[str], catalogFilePath: str) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str) """
        ...


class CertificateProviderItemNotFoundException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CertificateProviderItemNotFoundException()
    CertificateProviderItemNotFoundException(message: str)
    CertificateProviderItemNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CertificateNotFoundException(CertificateProviderItemNotFoundException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CertificateNotFoundException()
    CertificateNotFoundException(message: str)
    CertificateNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CertificateProvider(ICmdletProviderSupportsHelp, NavigationCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ CertificateProvider() """
    pass

class CertificateStoreLocationNotFoundException(CertificateProviderItemNotFoundException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CertificateStoreLocationNotFoundException()
    CertificateStoreLocationNotFoundException(message: str)
    CertificateStoreLocationNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CertificateStoreNotFoundException(CertificateProviderItemNotFoundException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CertificateStoreNotFoundException()
    CertificateStoreNotFoundException(message: str)
    CertificateStoreNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CheckpointComputerCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ CheckpointComputerCommand() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: CheckpointComputerCommand) -> str
        Set: Description(self: CheckpointComputerCommand) = value
        """
        ...

    @property
    def RestorePointType(self) -> str:
        """
        Get: RestorePointType(self: CheckpointComputerCommand) -> str
        Set: RestorePointType(self: CheckpointComputerCommand) = value
        """
        ...



class ClearContentCommand(ContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ ClearContentCommand() """
    pass

class ClearEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ClearEventLogCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: ClearEventLogCommand) -> Array[str]
        Set: ComputerName(self: ClearEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> Array:
        """
        Get: LogName(self: ClearEventLogCommand) -> Array[str]
        Set: LogName(self: ClearEventLogCommand) = value
        """
        ...



class ClearHistoryCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ClearHistoryCommand() """
    @property
    def CommandLine(self) -> Array:
        """
        Get: CommandLine(self: ClearHistoryCommand) -> Array[str]
        Set: CommandLine(self: ClearHistoryCommand) = value
        """
        ...

    @property
    def Count(self) -> int:
        """
        Get: Count(self: ClearHistoryCommand) -> int
        Set: Count(self: ClearHistoryCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: ClearHistoryCommand) -> Array[int]
        Set: Id(self: ClearHistoryCommand) = value
        """
        ...

    @property
    def Newest(self) -> SwitchParameter:
        """
        Get: Newest(self: ClearHistoryCommand) -> SwitchParameter
        Set: Newest(self: ClearHistoryCommand) = value
        """
        ...



class ClearItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ClearItemCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: ClearItemCommand) -> Array[str]
        Set: Exclude(self: ClearItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: ClearItemCommand) -> str
        Set: Filter(self: ClearItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ClearItemCommand) -> SwitchParameter
        Set: Force(self: ClearItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: ClearItemCommand) -> Array[str]
        Set: Include(self: ClearItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ClearItemCommand) -> Array[str]
        Set: LiteralPath(self: ClearItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ClearItemCommand) -> Array[str]
        Set: Path(self: ClearItemCommand) = value
        """
        ...



class ItemPropertyCommandBase(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ItemPropertyCommandBase() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: ItemPropertyCommandBase) -> Array[str]
        Set: Exclude(self: ItemPropertyCommandBase) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: ItemPropertyCommandBase) -> str
        Set: Filter(self: ItemPropertyCommandBase) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: ItemPropertyCommandBase) -> Array[str]
        Set: Include(self: ItemPropertyCommandBase) = value
        """
        ...



class PassThroughItemPropertyCommandBase(ItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ PassThroughItemPropertyCommandBase() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: PassThroughItemPropertyCommandBase) -> SwitchParameter
        Set: Force(self: PassThroughItemPropertyCommandBase) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: PassThroughItemPropertyCommandBase) -> SwitchParameter
        Set: PassThru(self: PassThroughItemPropertyCommandBase) = value
        """
        ...



class ClearItemPropertyCommand(PassThroughItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ClearItemPropertyCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ClearItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: ClearItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ClearItemPropertyCommand) -> str
        Set: Name(self: ClearItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ClearItemPropertyCommand) -> Array[str]
        Set: Path(self: ClearItemPropertyCommand) = value
        """
        ...



class ClearRecycleBinCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ClearRecycleBinCommand() """
    @property
    def DriveLetter(self) -> Array:
        """
        Get: DriveLetter(self: ClearRecycleBinCommand) -> Array[str]
        Set: DriveLetter(self: ClearRecycleBinCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ClearRecycleBinCommand) -> SwitchParameter
        Set: Force(self: ClearRecycleBinCommand) = value
        """
        ...



class VariableCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExcludeFilters(self):
        ...

    @property
    def IncludeFilters(self):
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: VariableCommandBase) -> str
        Set: Scope(self: VariableCommandBase) = value
        """
        ...



class ClearVariableCommand(VariableCommandBase): # skipped bases: <type 'object'>
    """ ClearVariableCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: ClearVariableCommand) -> Array[str]
        Set: Exclude(self: ClearVariableCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ClearVariableCommand) -> SwitchParameter
        Set: Force(self: ClearVariableCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: ClearVariableCommand) -> Array[str]
        Set: Include(self: ClearVariableCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: ClearVariableCommand) -> Array[str]
        Set: Name(self: ClearVariableCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ClearVariableCommand) -> SwitchParameter
        Set: PassThru(self: ClearVariableCommand) = value
        """
        ...



class ClipboardFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ClipboardFormat, values: Audio (3), FileDropList (1), Image (2), Text (0) """
    Audio: ClipboardFormat = ...
    FileDropList: ClipboardFormat = ...
    Image: ClipboardFormat = ...
    Text: ClipboardFormat = ...
    value__ = ...


class CommonRunspaceCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AppDomainName(self) -> Array:
        """
        Get: AppDomainName(self: CommonRunspaceCommandBase) -> Array[str]
        Set: AppDomainName(self: CommonRunspaceCommandBase) = value
        """
        ...

    @property
    def ProcessName(self) -> str:
        """
        Get: ProcessName(self: CommonRunspaceCommandBase) -> str
        Set: ProcessName(self: CommonRunspaceCommandBase) = value
        """
        ...

    @property
    def Runspace(self) -> Array:
        """
        Get: Runspace(self: CommonRunspaceCommandBase) -> Array[Runspace]
        Set: Runspace(self: CommonRunspaceCommandBase) = value
        """
        ...

    @property
    def RunspaceId(self) -> Array:
        """
        Get: RunspaceId(self: CommonRunspaceCommandBase) -> Array[int]
        Set: RunspaceId(self: CommonRunspaceCommandBase) = value
        """
        ...

    @property
    def RunspaceInstanceId(self) -> Array:
        """
        Get: RunspaceInstanceId(self: CommonRunspaceCommandBase) -> Array[Guid]
        Set: RunspaceInstanceId(self: CommonRunspaceCommandBase) = value
        """
        ...

    @property
    def RunspaceName(self) -> Array:
        """
        Get: RunspaceName(self: CommonRunspaceCommandBase) -> Array[str]
        Set: RunspaceName(self: CommonRunspaceCommandBase) = value
        """
        ...


    def GetDebuggerFromRunspace(self, *args): #cannot find CLR method
        """ GetDebuggerFromRunspace(self: CommonRunspaceCommandBase, runspace: Runspace) -> Debugger """
        ...

    def GetRunspaces(self, *args): #cannot find CLR method
        """ GetRunspaces(self: CommonRunspaceCommandBase) -> IReadOnlyList[Runspace] """
        ...

    def SetDebugPreferenceHelper(self, *args): #cannot find CLR method
        """ SetDebugPreferenceHelper(self: CommonRunspaceCommandBase, processName: str, appDomainName: Array[str], enable: bool, fullyQualifiedErrorId: str) """
        ...

    ProcessNameParameterSet: str = ...
    RunspaceIdParameterSet: str = ...
    RunspaceInstanceIdParameterSet: str = ...
    RunspaceNameParameterSet: str = ...
    RunspaceParameterSet: str = ...


class ObjectCmdletBase(PSCmdlet): # skipped bases: <type 'object'>
    """ ObjectCmdletBase() """
    @property
    def CaseSensitive(self) -> SwitchParameter:
        """
        Get: CaseSensitive(self: ObjectCmdletBase) -> SwitchParameter
        Set: CaseSensitive(self: ObjectCmdletBase) = value
        """
        ...

    @property
    def Culture(self) -> str:
        """
        Get: Culture(self: ObjectCmdletBase) -> str
        Set: Culture(self: ObjectCmdletBase) = value
        """
        ...



class CompareObjectCommand(ObjectCmdletBase): # skipped bases: <type 'object'>
    """ CompareObjectCommand() """
    @property
    def DifferenceObject(self) -> Array:
        """
        Get: DifferenceObject(self: CompareObjectCommand) -> Array[PSObject]
        Set: DifferenceObject(self: CompareObjectCommand) = value
        """
        ...

    @property
    def ExcludeDifferent(self) -> SwitchParameter:
        """
        Get: ExcludeDifferent(self: CompareObjectCommand) -> SwitchParameter
        Set: ExcludeDifferent(self: CompareObjectCommand) = value
        """
        ...

    @property
    def IncludeEqual(self) -> SwitchParameter:
        """
        Get: IncludeEqual(self: CompareObjectCommand) -> SwitchParameter
        Set: IncludeEqual(self: CompareObjectCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: CompareObjectCommand) -> SwitchParameter
        Set: PassThru(self: CompareObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: CompareObjectCommand) -> Array[object]
        Set: Property(self: CompareObjectCommand) = value
        """
        ...

    @property
    def ReferenceObject(self) -> Array:
        """
        Get: ReferenceObject(self: CompareObjectCommand) -> Array[PSObject]
        Set: ReferenceObject(self: CompareObjectCommand) = value
        """
        ...

    @property
    def SyncWindow(self) -> int:
        """
        Get: SyncWindow(self: CompareObjectCommand) -> int
        Set: SyncWindow(self: CompareObjectCommand) = value
        """
        ...



class CompleteTransactionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ CompleteTransactionCommand() """
    pass

class ComputerChangeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ComputerChangeInfo() """
    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: ComputerChangeInfo) -> str
        Set: ComputerName(self: ComputerChangeInfo) = value
        """
        ...

    @property
    def HasSucceeded(self) -> bool:
        """
        Get: HasSucceeded(self: ComputerChangeInfo) -> bool
        Set: HasSucceeded(self: ComputerChangeInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ComputerChangeInfo) -> str """
        ...


class ComputerInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ComputerInfo() """
    @property
    def BiosBIOSVersion(self) -> Array:
        """ Get: BiosBIOSVersion(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def BiosBuildNumber(self) -> str:
        """ Get: BiosBuildNumber(self: ComputerInfo) -> str """
        ...

    @property
    def BiosCaption(self) -> str:
        """ Get: BiosCaption(self: ComputerInfo) -> str """
        ...

    @property
    def BiosCharacteristics(self) -> Array:
        """ Get: BiosCharacteristics(self: ComputerInfo) -> Array[UInt16] """
        ...

    @property
    def BiosCodeSet(self) -> str:
        """ Get: BiosCodeSet(self: ComputerInfo) -> str """
        ...

    @property
    def BiosCurrentLanguage(self) -> str:
        """ Get: BiosCurrentLanguage(self: ComputerInfo) -> str """
        ...

    @property
    def BiosDescription(self) -> str:
        """ Get: BiosDescription(self: ComputerInfo) -> str """
        ...

    @property
    def BiosEmbeddedControllerMajorVersion(self) -> Nullable:
        """ Get: BiosEmbeddedControllerMajorVersion(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def BiosEmbeddedControllerMinorVersion(self) -> Nullable:
        """ Get: BiosEmbeddedControllerMinorVersion(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def BiosFirmwareType(self) -> Nullable:
        """ Get: BiosFirmwareType(self: ComputerInfo) -> Nullable[FirmwareType] """
        ...

    @property
    def BiosIdentificationCode(self) -> str:
        """ Get: BiosIdentificationCode(self: ComputerInfo) -> str """
        ...

    @property
    def BiosInstallableLanguages(self) -> Nullable:
        """ Get: BiosInstallableLanguages(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosInstallDate(self) -> Nullable:
        """ Get: BiosInstallDate(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def BiosLanguageEdition(self) -> str:
        """ Get: BiosLanguageEdition(self: ComputerInfo) -> str """
        ...

    @property
    def BiosListOfLanguages(self) -> Array:
        """ Get: BiosListOfLanguages(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def BiosManufacturer(self) -> str:
        """ Get: BiosManufacturer(self: ComputerInfo) -> str """
        ...

    @property
    def BiosName(self) -> str:
        """ Get: BiosName(self: ComputerInfo) -> str """
        ...

    @property
    def BiosOtherTargetOS(self) -> str:
        """ Get: BiosOtherTargetOS(self: ComputerInfo) -> str """
        ...

    @property
    def BiosPrimaryBIOS(self) -> Nullable:
        """ Get: BiosPrimaryBIOS(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def BiosReleaseDate(self) -> Nullable:
        """ Get: BiosReleaseDate(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def BiosSeralNumber(self) -> str:
        """ Get: BiosSeralNumber(self: ComputerInfo) -> str """
        ...

    @property
    def BiosSMBIOSBIOSVersion(self) -> str:
        """ Get: BiosSMBIOSBIOSVersion(self: ComputerInfo) -> str """
        ...

    @property
    def BiosSMBIOSMajorVersion(self) -> Nullable:
        """ Get: BiosSMBIOSMajorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosSMBIOSMinorVersion(self) -> Nullable:
        """ Get: BiosSMBIOSMinorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosSMBIOSPresent(self) -> Nullable:
        """ Get: BiosSMBIOSPresent(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def BiosSoftwareElementState(self) -> Nullable:
        """ Get: BiosSoftwareElementState(self: ComputerInfo) -> Nullable[SoftwareElementState] """
        ...

    @property
    def BiosStatus(self) -> str:
        """ Get: BiosStatus(self: ComputerInfo) -> str """
        ...

    @property
    def BiosSystemBiosMajorVersion(self) -> Nullable:
        """ Get: BiosSystemBiosMajorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosSystemBiosMinorVersion(self) -> Nullable:
        """ Get: BiosSystemBiosMinorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosTargetOperatingSystem(self) -> Nullable:
        """ Get: BiosTargetOperatingSystem(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def BiosVersion(self) -> str:
        """ Get: BiosVersion(self: ComputerInfo) -> str """
        ...

    @property
    def CsAdminPasswordStatus(self) -> Nullable:
        """ Get: CsAdminPasswordStatus(self: ComputerInfo) -> Nullable[HardwareSecurity] """
        ...

    @property
    def CsAutomaticManagedPagefile(self) -> Nullable:
        """ Get: CsAutomaticManagedPagefile(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsAutomaticResetBootOption(self) -> Nullable:
        """ Get: CsAutomaticResetBootOption(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsAutomaticResetCapability(self) -> Nullable:
        """ Get: CsAutomaticResetCapability(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsBootOptionOnLimit(self) -> Nullable:
        """ Get: CsBootOptionOnLimit(self: ComputerInfo) -> Nullable[BootOptionAction] """
        ...

    @property
    def CsBootOptionOnWatchDog(self) -> Nullable:
        """ Get: CsBootOptionOnWatchDog(self: ComputerInfo) -> Nullable[BootOptionAction] """
        ...

    @property
    def CsBootROMSupported(self) -> Nullable:
        """ Get: CsBootROMSupported(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsBootStatus(self) -> Array:
        """ Get: CsBootStatus(self: ComputerInfo) -> Array[UInt16] """
        ...

    @property
    def CsBootupState(self) -> str:
        """ Get: CsBootupState(self: ComputerInfo) -> str """
        ...

    @property
    def CsCaption(self) -> str:
        """ Get: CsCaption(self: ComputerInfo) -> str """
        ...

    @property
    def CsChassisBootupState(self) -> Nullable:
        """ Get: CsChassisBootupState(self: ComputerInfo) -> Nullable[SystemElementState] """
        ...

    @property
    def CsChassisSKUNumber(self) -> str:
        """ Get: CsChassisSKUNumber(self: ComputerInfo) -> str """
        ...

    @property
    def CsCurrentTimeZone(self) -> Nullable:
        """ Get: CsCurrentTimeZone(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def CsDaylightInEffect(self) -> Nullable:
        """ Get: CsDaylightInEffect(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsDescription(self) -> str:
        """ Get: CsDescription(self: ComputerInfo) -> str """
        ...

    @property
    def CsDNSHostName(self) -> str:
        """ Get: CsDNSHostName(self: ComputerInfo) -> str """
        ...

    @property
    def CsDomain(self) -> str:
        """ Get: CsDomain(self: ComputerInfo) -> str """
        ...

    @property
    def CsDomainRole(self) -> Nullable:
        """ Get: CsDomainRole(self: ComputerInfo) -> Nullable[DomainRole] """
        ...

    @property
    def CsEnableDaylightSavingsTime(self) -> Nullable:
        """ Get: CsEnableDaylightSavingsTime(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsFrontPanelResetStatus(self) -> Nullable:
        """ Get: CsFrontPanelResetStatus(self: ComputerInfo) -> Nullable[HardwareSecurity] """
        ...

    @property
    def CsHypervisorPresent(self) -> Nullable:
        """ Get: CsHypervisorPresent(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsInfraredSupported(self) -> Nullable:
        """ Get: CsInfraredSupported(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsInitialLoadInfo(self) -> str:
        """ Get: CsInitialLoadInfo(self: ComputerInfo) -> str """
        ...

    @property
    def CsInstallDate(self) -> Nullable:
        """ Get: CsInstallDate(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def CsKeyboardPasswordStatus(self) -> Nullable:
        """ Get: CsKeyboardPasswordStatus(self: ComputerInfo) -> Nullable[HardwareSecurity] """
        ...

    @property
    def CsLastLoadInfo(self) -> str:
        """ Get: CsLastLoadInfo(self: ComputerInfo) -> str """
        ...

    @property
    def CsManufacturer(self) -> str:
        """ Get: CsManufacturer(self: ComputerInfo) -> str """
        ...

    @property
    def CsModel(self) -> str:
        """ Get: CsModel(self: ComputerInfo) -> str """
        ...

    @property
    def CsName(self) -> str:
        """ Get: CsName(self: ComputerInfo) -> str """
        ...

    @property
    def CsNetworkAdapters(self) -> Array:
        """ Get: CsNetworkAdapters(self: ComputerInfo) -> Array[NetworkAdapter] """
        ...

    @property
    def CsNetworkServerModeEnabled(self) -> Nullable:
        """ Get: CsNetworkServerModeEnabled(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsNumberOfLogicalProcessors(self) -> Nullable:
        """ Get: CsNumberOfLogicalProcessors(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def CsNumberOfProcessors(self) -> Nullable:
        """ Get: CsNumberOfProcessors(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def CsOEMStringArray(self) -> Array:
        """ Get: CsOEMStringArray(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def CsPartOfDomain(self) -> Nullable:
        """ Get: CsPartOfDomain(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsPauseAfterReset(self) -> Nullable:
        """ Get: CsPauseAfterReset(self: ComputerInfo) -> Nullable[Int64] """
        ...

    @property
    def CsPCSystemType(self) -> Nullable:
        """ Get: CsPCSystemType(self: ComputerInfo) -> Nullable[PCSystemType] """
        ...

    @property
    def CsPCSystemTypeEx(self) -> Nullable:
        """ Get: CsPCSystemTypeEx(self: ComputerInfo) -> Nullable[PCSystemTypeEx] """
        ...

    @property
    def CsPhyicallyInstalledMemory(self) -> Nullable:
        """ Get: CsPhyicallyInstalledMemory(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def CsPowerManagementCapabilities(self) -> Array:
        """ Get: CsPowerManagementCapabilities(self: ComputerInfo) -> Array[PowerManagementCapabilities] """
        ...

    @property
    def CsPowerManagementSupported(self) -> Nullable:
        """ Get: CsPowerManagementSupported(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def CsPowerOnPasswordStatus(self) -> Nullable:
        """ Get: CsPowerOnPasswordStatus(self: ComputerInfo) -> Nullable[HardwareSecurity] """
        ...

    @property
    def CsPowerState(self) -> Nullable:
        """ Get: CsPowerState(self: ComputerInfo) -> Nullable[PowerState] """
        ...

    @property
    def CsPowerSupplyState(self) -> Nullable:
        """ Get: CsPowerSupplyState(self: ComputerInfo) -> Nullable[SystemElementState] """
        ...

    @property
    def CsPrimaryOwnerContact(self) -> str:
        """ Get: CsPrimaryOwnerContact(self: ComputerInfo) -> str """
        ...

    @property
    def CsPrimaryOwnerName(self) -> str:
        """ Get: CsPrimaryOwnerName(self: ComputerInfo) -> str """
        ...

    @property
    def CsProcessors(self) -> Array:
        """ Get: CsProcessors(self: ComputerInfo) -> Array[Processor] """
        ...

    @property
    def CsResetCapability(self) -> Nullable:
        """ Get: CsResetCapability(self: ComputerInfo) -> Nullable[ResetCapability] """
        ...

    @property
    def CsResetCount(self) -> Nullable:
        """ Get: CsResetCount(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def CsResetLimit(self) -> Nullable:
        """ Get: CsResetLimit(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def CsRoles(self) -> Array:
        """ Get: CsRoles(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def CsStatus(self) -> str:
        """ Get: CsStatus(self: ComputerInfo) -> str """
        ...

    @property
    def CsSupportContactDescription(self) -> Array:
        """ Get: CsSupportContactDescription(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def CsSystemFamily(self) -> str:
        """ Get: CsSystemFamily(self: ComputerInfo) -> str """
        ...

    @property
    def CsSystemSKUNumber(self) -> str:
        """ Get: CsSystemSKUNumber(self: ComputerInfo) -> str """
        ...

    @property
    def CsSystemType(self) -> str:
        """ Get: CsSystemType(self: ComputerInfo) -> str """
        ...

    @property
    def CsThermalState(self) -> Nullable:
        """ Get: CsThermalState(self: ComputerInfo) -> Nullable[SystemElementState] """
        ...

    @property
    def CsTotalPhysicalMemory(self) -> Nullable:
        """ Get: CsTotalPhysicalMemory(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def CsUserName(self) -> str:
        """ Get: CsUserName(self: ComputerInfo) -> str """
        ...

    @property
    def CsWakeUpType(self) -> Nullable:
        """ Get: CsWakeUpType(self: ComputerInfo) -> Nullable[WakeUpType] """
        ...

    @property
    def CsWorkgroup(self) -> str:
        """ Get: CsWorkgroup(self: ComputerInfo) -> str """
        ...

    @property
    def DeviceGuardAvailableSecurityProperties(self) -> Array:
        """ Get: DeviceGuardAvailableSecurityProperties(self: ComputerInfo) -> Array[DeviceGuardHardwareSecure] """
        ...

    @property
    def DeviceGuardCodeIntegrityPolicyEnforcementStatus(self) -> Nullable:
        """ Get: DeviceGuardCodeIntegrityPolicyEnforcementStatus(self: ComputerInfo) -> Nullable[DeviceGuardConfigCodeIntegrityStatus] """
        ...

    @property
    def DeviceGuardRequiredSecurityProperties(self) -> Array:
        """ Get: DeviceGuardRequiredSecurityProperties(self: ComputerInfo) -> Array[DeviceGuardHardwareSecure] """
        ...

    @property
    def DeviceGuardSecurityServicesConfigured(self) -> Array:
        """ Get: DeviceGuardSecurityServicesConfigured(self: ComputerInfo) -> Array[DeviceGuardSoftwareSecure] """
        ...

    @property
    def DeviceGuardSecurityServicesRunning(self) -> Array:
        """ Get: DeviceGuardSecurityServicesRunning(self: ComputerInfo) -> Array[DeviceGuardSoftwareSecure] """
        ...

    @property
    def DeviceGuardSmartStatus(self) -> Nullable:
        """ Get: DeviceGuardSmartStatus(self: ComputerInfo) -> Nullable[DeviceGuardSmartStatus] """
        ...

    @property
    def DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus(self) -> Nullable:
        """ Get: DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus(self: ComputerInfo) -> Nullable[DeviceGuardConfigCodeIntegrityStatus] """
        ...

    @property
    def HyperVisorPresent(self) -> Nullable:
        """ Get: HyperVisorPresent(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def HyperVRequirementDataExecutionPreventionAvailable(self) -> Nullable:
        """ Get: HyperVRequirementDataExecutionPreventionAvailable(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def HyperVRequirementSecondLevelAddressTranslation(self) -> Nullable:
        """ Get: HyperVRequirementSecondLevelAddressTranslation(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def HyperVRequirementVirtualizationFirmwareEnabled(self) -> Nullable:
        """ Get: HyperVRequirementVirtualizationFirmwareEnabled(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def HyperVRequirementVMMonitorModeExtensions(self) -> Nullable:
        """ Get: HyperVRequirementVMMonitorModeExtensions(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def KeyboardLayout(self) -> str:
        """ Get: KeyboardLayout(self: ComputerInfo) -> str """
        ...

    @property
    def LogonServer(self) -> str:
        """ Get: LogonServer(self: ComputerInfo) -> str """
        ...

    @property
    def OsArchitecture(self) -> str:
        """ Get: OsArchitecture(self: ComputerInfo) -> str """
        ...

    @property
    def OsBootDevice(self) -> str:
        """ Get: OsBootDevice(self: ComputerInfo) -> str """
        ...

    @property
    def OsBuildNumber(self) -> str:
        """ Get: OsBuildNumber(self: ComputerInfo) -> str """
        ...

    @property
    def OsBuildType(self) -> str:
        """ Get: OsBuildType(self: ComputerInfo) -> str """
        ...

    @property
    def OsCodeSet(self) -> str:
        """ Get: OsCodeSet(self: ComputerInfo) -> str """
        ...

    @property
    def OsCountryCode(self) -> str:
        """ Get: OsCountryCode(self: ComputerInfo) -> str """
        ...

    @property
    def OsCSDVersion(self) -> str:
        """ Get: OsCSDVersion(self: ComputerInfo) -> str """
        ...

    @property
    def OsCurrentTimeZone(self) -> Nullable:
        """ Get: OsCurrentTimeZone(self: ComputerInfo) -> Nullable[Int16] """
        ...

    @property
    def OsDataExecutionPrevention32BitApplications(self) -> Nullable:
        """ Get: OsDataExecutionPrevention32BitApplications(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsDataExecutionPreventionAvailable(self) -> Nullable:
        """ Get: OsDataExecutionPreventionAvailable(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsDataExecutionPreventionDrivers(self) -> Nullable:
        """ Get: OsDataExecutionPreventionDrivers(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsDataExecutionPreventionSupportPolicy(self) -> Nullable:
        """ Get: OsDataExecutionPreventionSupportPolicy(self: ComputerInfo) -> Nullable[DataExecutionPreventionSupportPolicy] """
        ...

    @property
    def OsDebug(self) -> Nullable:
        """ Get: OsDebug(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsDistributed(self) -> Nullable:
        """ Get: OsDistributed(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsEncryptionLevel(self) -> Nullable:
        """ Get: OsEncryptionLevel(self: ComputerInfo) -> Nullable[OSEncryptionLevel] """
        ...

    @property
    def OsForegroundApplicationBoost(self) -> Nullable:
        """ Get: OsForegroundApplicationBoost(self: ComputerInfo) -> Nullable[ForegroundApplicationBoost] """
        ...

    @property
    def OsFreePhysicalMemory(self) -> Nullable:
        """ Get: OsFreePhysicalMemory(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsFreeSpaceInPagingFiles(self) -> Nullable:
        """ Get: OsFreeSpaceInPagingFiles(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsFreeVirtualMemory(self) -> Nullable:
        """ Get: OsFreeVirtualMemory(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsHardwareAbstractionLayer(self) -> str:
        """ Get: OsHardwareAbstractionLayer(self: ComputerInfo) -> str """
        ...

    @property
    def OsHotFixes(self) -> Array:
        """ Get: OsHotFixes(self: ComputerInfo) -> Array[HotFix] """
        ...

    @property
    def OsInstallDate(self) -> Nullable:
        """ Get: OsInstallDate(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def OsInUseVirtualMemory(self) -> Nullable:
        """ Get: OsInUseVirtualMemory(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsLanguage(self) -> str:
        """ Get: OsLanguage(self: ComputerInfo) -> str """
        ...

    @property
    def OsLastBootUpTime(self) -> Nullable:
        """ Get: OsLastBootUpTime(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def OsLocalDateTime(self) -> Nullable:
        """ Get: OsLocalDateTime(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def OsLocale(self) -> str:
        """ Get: OsLocale(self: ComputerInfo) -> str """
        ...

    @property
    def OsLocaleID(self) -> str:
        """ Get: OsLocaleID(self: ComputerInfo) -> str """
        ...

    @property
    def OsManufacturer(self) -> str:
        """ Get: OsManufacturer(self: ComputerInfo) -> str """
        ...

    @property
    def OsMaxNumberOfProcesses(self) -> Nullable:
        """ Get: OsMaxNumberOfProcesses(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def OsMaxProcessMemorySize(self) -> Nullable:
        """ Get: OsMaxProcessMemorySize(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsMuiLanguages(self) -> Array:
        """ Get: OsMuiLanguages(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def OsName(self) -> str:
        """ Get: OsName(self: ComputerInfo) -> str """
        ...

    @property
    def OsNumberOfLicensedUsers(self) -> Nullable:
        """ Get: OsNumberOfLicensedUsers(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def OsNumberOfProcesses(self) -> Nullable:
        """ Get: OsNumberOfProcesses(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def OsNumberOfUsers(self) -> Nullable:
        """ Get: OsNumberOfUsers(self: ComputerInfo) -> Nullable[UInt32] """
        ...

    @property
    def OsOperatingSystemSKU(self) -> Nullable:
        """ Get: OsOperatingSystemSKU(self: ComputerInfo) -> Nullable[OperatingSystemSKU] """
        ...

    @property
    def OsOrganization(self) -> str:
        """ Get: OsOrganization(self: ComputerInfo) -> str """
        ...

    @property
    def OsOtherTypeDescription(self) -> str:
        """ Get: OsOtherTypeDescription(self: ComputerInfo) -> str """
        ...

    @property
    def OsPAEEnabled(self) -> Nullable:
        """ Get: OsPAEEnabled(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsPagingFiles(self) -> Array:
        """ Get: OsPagingFiles(self: ComputerInfo) -> Array[str] """
        ...

    @property
    def OsPortableOperatingSystem(self) -> Nullable:
        """ Get: OsPortableOperatingSystem(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsPrimary(self) -> Nullable:
        """ Get: OsPrimary(self: ComputerInfo) -> Nullable[bool] """
        ...

    @property
    def OsProductSuites(self) -> Array:
        """ Get: OsProductSuites(self: ComputerInfo) -> Array[OSProductSuite] """
        ...

    @property
    def OsProductType(self) -> Nullable:
        """ Get: OsProductType(self: ComputerInfo) -> Nullable[ProductType] """
        ...

    @property
    def OsRegisteredUser(self) -> str:
        """ Get: OsRegisteredUser(self: ComputerInfo) -> str """
        ...

    @property
    def OsSerialNumber(self) -> str:
        """ Get: OsSerialNumber(self: ComputerInfo) -> str """
        ...

    @property
    def OsServerLevel(self) -> Nullable:
        """ Get: OsServerLevel(self: ComputerInfo) -> Nullable[ServerLevel] """
        ...

    @property
    def OsServicePackMajorVersion(self) -> Nullable:
        """ Get: OsServicePackMajorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def OsServicePackMinorVersion(self) -> Nullable:
        """ Get: OsServicePackMinorVersion(self: ComputerInfo) -> Nullable[UInt16] """
        ...

    @property
    def OsSizeStoredInPagingFiles(self) -> Nullable:
        """ Get: OsSizeStoredInPagingFiles(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsStatus(self) -> str:
        """ Get: OsStatus(self: ComputerInfo) -> str """
        ...

    @property
    def OsSuites(self) -> Array:
        """ Get: OsSuites(self: ComputerInfo) -> Array[OSProductSuite] """
        ...

    @property
    def OsSystemDevice(self) -> str:
        """ Get: OsSystemDevice(self: ComputerInfo) -> str """
        ...

    @property
    def OsSystemDirectory(self) -> str:
        """ Get: OsSystemDirectory(self: ComputerInfo) -> str """
        ...

    @property
    def OsSystemDrive(self) -> str:
        """ Get: OsSystemDrive(self: ComputerInfo) -> str """
        ...

    @property
    def OsTotalSwapSpaceSize(self) -> Nullable:
        """ Get: OsTotalSwapSpaceSize(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsTotalVirtualMemorySize(self) -> Nullable:
        """ Get: OsTotalVirtualMemorySize(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsTotalVisibleMemorySize(self) -> Nullable:
        """ Get: OsTotalVisibleMemorySize(self: ComputerInfo) -> Nullable[UInt64] """
        ...

    @property
    def OsType(self) -> Nullable:
        """ Get: OsType(self: ComputerInfo) -> Nullable[OSType] """
        ...

    @property
    def OsUptime(self) -> Nullable:
        """ Get: OsUptime(self: ComputerInfo) -> Nullable[TimeSpan] """
        ...

    @property
    def OsVersion(self) -> str:
        """ Get: OsVersion(self: ComputerInfo) -> str """
        ...

    @property
    def OsWindowsDirectory(self) -> str:
        """ Get: OsWindowsDirectory(self: ComputerInfo) -> str """
        ...

    @property
    def PowerPlatformRole(self) -> Nullable:
        """ Get: PowerPlatformRole(self: ComputerInfo) -> Nullable[PowerPlatformRole] """
        ...

    @property
    def TimeZone(self) -> str:
        """ Get: TimeZone(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsBuildLabEx(self) -> str:
        """ Get: WindowsBuildLabEx(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsCurrentVersion(self) -> str:
        """ Get: WindowsCurrentVersion(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsEditionId(self) -> str:
        """ Get: WindowsEditionId(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsInstallationType(self) -> str:
        """ Get: WindowsInstallationType(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsInstallDateFromRegistry(self) -> Nullable:
        """ Get: WindowsInstallDateFromRegistry(self: ComputerInfo) -> Nullable[DateTime] """
        ...

    @property
    def WindowsProductId(self) -> str:
        """ Get: WindowsProductId(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsProductName(self) -> str:
        """ Get: WindowsProductName(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsRegisteredOrganization(self) -> str:
        """ Get: WindowsRegisteredOrganization(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsRegisteredOwner(self) -> str:
        """ Get: WindowsRegisteredOwner(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsSystemRoot(self) -> str:
        """ Get: WindowsSystemRoot(self: ComputerInfo) -> str """
        ...

    @property
    def WindowsVersion(self) -> str:
        """ Get: WindowsVersion(self: ComputerInfo) -> str """
        ...



class PSRemotingCmdlet(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    def ResolveAppName(self, *args): #cannot find CLR method
        """ ResolveAppName(self: PSRemotingCmdlet, appName: str) -> str """
        ...

    def ResolveComputerName(self, *args): #cannot find CLR method
        """ ResolveComputerName(self: PSRemotingCmdlet, computerName: str) -> str """
        ...

    def ResolveComputerNames(self, *args): #cannot find CLR method
        """ ResolveComputerNames(self: PSRemotingCmdlet, computerNames: Array[str]) -> Array[str] """
        ...

    def ResolveShell(self, *args): #cannot find CLR method
        """ ResolveShell(self: PSRemotingCmdlet, shell: str) -> str """
        ...

    ComputerInstanceIdParameterSet: str = ...
    ComputerNameParameterSet: str = ...
    ContainerIdParameterSet: str = ...
    DefaultPowerShellRemoteShellAppName: str = ...
    DefaultPowerShellRemoteShellName: str = ...
    SessionParameterSet: str = ...
    VMIdParameterSet: str = ...
    VMNameParameterSet: str = ...


class PSRunspaceCmdlet(PSRemotingCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: PSRunspaceCmdlet) -> Array[str]
        Set: ComputerName(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def ContainerId(self) -> Array:
        """
        Get: ContainerId(self: PSRunspaceCmdlet) -> Array[str]
        Set: ContainerId(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: PSRunspaceCmdlet) -> Array[int]
        Set: Id(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def InstanceId(self) -> Array:
        """
        Get: InstanceId(self: PSRunspaceCmdlet) -> Array[Guid]
        Set: InstanceId(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: PSRunspaceCmdlet) -> Array[str]
        Set: Name(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def VMId(self) -> Array:
        """
        Get: VMId(self: PSRunspaceCmdlet) -> Array[Guid]
        Set: VMId(self: PSRunspaceCmdlet) = value
        """
        ...

    @property
    def VMName(self) -> Array:
        """
        Get: VMName(self: PSRunspaceCmdlet) -> Array[str]
        Set: VMName(self: PSRunspaceCmdlet) = value
        """
        ...


    def GetMatchingRunspaces(self, *args): #cannot find CLR method
        """
        GetMatchingRunspaces(self: PSRunspaceCmdlet, writeobject: bool, writeErrorOnNoMatch: bool) -> Dictionary[Guid, PSSession]
        GetMatchingRunspaces(self: PSRunspaceCmdlet, writeobject: bool, writeErrorOnNoMatch: bool, filterState: SessionFilterState, configurationName: str) -> Dictionary[Guid, PSSession]
        """
        ...

    def GetMatchingRunspacesByName(self, *args): #cannot find CLR method
        """ GetMatchingRunspacesByName(self: PSRunspaceCmdlet, writeobject: bool, writeErrorOnNoMatch: bool) -> Dictionary[Guid, PSSession] """
        ...

    def GetMatchingRunspacesByRunspaceId(self, *args): #cannot find CLR method
        """ GetMatchingRunspacesByRunspaceId(self: PSRunspaceCmdlet, writeobject: bool, writeErrorOnNoMatch: bool) -> Dictionary[Guid, PSSession] """
        ...

    ContainerIdInstanceIdParameterSet: str = ...
    IdParameterSet: str = ...
    InstanceIdParameterSet: str = ...
    NameParameterSet: str = ...
    VMIdInstanceIdParameterSet: str = ...
    VMNameInstanceIdParameterSet: str = ...


class ConnectPSSessionCommand(IDisposable, PSRunspaceCmdlet): # skipped bases: <type 'object'>
    """ ConnectPSSessionCommand() """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """
        Get: AllowRedirection(self: ConnectPSSessionCommand) -> SwitchParameter
        Set: AllowRedirection(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: ConnectPSSessionCommand) -> str
        Set: ApplicationName(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: ConnectPSSessionCommand) -> AuthenticationMechanism
        Set: Authentication(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: ConnectPSSessionCommand) -> str
        Set: CertificateThumbprint(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ConnectPSSessionCommand) -> str
        Set: ConfigurationName(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Array:
        """
        Get: ConnectionUri(self: ConnectPSSessionCommand) -> Array[Uri]
        Set: ConnectionUri(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: ConnectPSSessionCommand) -> PSCredential
        Set: Credential(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: ConnectPSSessionCommand) -> int
        Set: Port(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def Session(self) -> Array:
        """
        Get: Session(self: ConnectPSSessionCommand) -> Array[PSSession]
        Set: Session(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: ConnectPSSessionCommand) -> PSSessionOption
        Set: SessionOption(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: ConnectPSSessionCommand) -> int
        Set: ThrottleLimit(self: ConnectPSSessionCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: ConnectPSSessionCommand) -> SwitchParameter
        Set: UseSSL(self: ConnectPSSessionCommand) = value
        """
        ...



class ConsoleCmdletsBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ConsoleColorCmdlet(PSCmdlet): # skipped bases: <type 'object'>
    """ ConsoleColorCmdlet() """
    @property
    def BackgroundColor(self) -> ConsoleColor:
        """
        Get: BackgroundColor(self: ConsoleColorCmdlet) -> ConsoleColor
        Set: BackgroundColor(self: ConsoleColorCmdlet) = value
        """
        ...

    @property
    def ForegroundColor(self) -> ConsoleColor:
        """
        Get: ForegroundColor(self: ConsoleColorCmdlet) -> ConsoleColor
        Set: ForegroundColor(self: ConsoleColorCmdlet) = value
        """
        ...



class ControlPanelItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanonicalName(self) -> str:
        """ Get: CanonicalName(self: ControlPanelItem) -> str """
        ...

    @property
    def Category(self) -> Array:
        """ Get: Category(self: ControlPanelItem) -> Array[str] """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: ControlPanelItem) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ControlPanelItem) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: ControlPanelItem) -> str """
        ...


class ControlPanelItemBaseCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ConvertFromCsvCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertFromCsvCommand() """
    @property
    def Delimiter(self) -> Char:
        """
        Get: Delimiter(self: ConvertFromCsvCommand) -> Char
        Set: Delimiter(self: ConvertFromCsvCommand) = value
        """
        ...

    @property
    def Header(self) -> Array:
        """
        Get: Header(self: ConvertFromCsvCommand) -> Array[str]
        Set: Header(self: ConvertFromCsvCommand) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: ConvertFromCsvCommand) -> Array[PSObject]
        Set: InputObject(self: ConvertFromCsvCommand) = value
        """
        ...

    @property
    def UseCulture(self) -> SwitchParameter:
        """
        Get: UseCulture(self: ConvertFromCsvCommand) -> SwitchParameter
        Set: UseCulture(self: ConvertFromCsvCommand) = value
        """
        ...



class ConvertFromJsonCommand(Cmdlet): # skipped bases: <type 'object'>
    """ ConvertFromJsonCommand() """
    @property
    def InputObject(self) -> str:
        """
        Get: InputObject(self: ConvertFromJsonCommand) -> str
        Set: InputObject(self: ConvertFromJsonCommand) = value
        """
        ...



class SecureStringCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SecureStringData(self):
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str) """
        ...


class ConvertFromToSecureStringCommandBase(SecureStringCommandBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Key(self) -> Array:
        """
        Get: Key(self: ConvertFromToSecureStringCommandBase) -> Array[Byte]
        Set: Key(self: ConvertFromToSecureStringCommandBase) = value
        """
        ...

    @property
    def SecureKey(self) -> SecureString:
        """
        Get: SecureKey(self: ConvertFromToSecureStringCommandBase) -> SecureString
        Set: SecureKey(self: ConvertFromToSecureStringCommandBase) = value
        """
        ...



class ConvertFromSecureStringCommand(ConvertFromToSecureStringCommandBase): # skipped bases: <type 'object'>
    """ ConvertFromSecureStringCommand() """
    @property
    def SecureString(self) -> SecureString:
        """
        Get: SecureString(self: ConvertFromSecureStringCommand) -> SecureString
        Set: SecureString(self: ConvertFromSecureStringCommand) = value
        """
        ...



class ConvertFromStringDataCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertFromStringDataCommand() """
    @property
    def StringData(self) -> str:
        """
        Get: StringData(self: ConvertFromStringDataCommand) -> str
        Set: StringData(self: ConvertFromStringDataCommand) = value
        """
        ...



class ConvertPathCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ConvertPathCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ConvertPathCommand) -> Array[str]
        Set: LiteralPath(self: ConvertPathCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ConvertPathCommand) -> Array[str]
        Set: Path(self: ConvertPathCommand) = value
        """
        ...



class ConvertToCsvCommand(BaseCsvWritingCommand): # skipped bases: <type 'object'>
    """ ConvertToCsvCommand() """
    pass

class ConvertToHtmlCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertToHtmlCommand() """
    @property
    def As(self) -> str:
        """
        Get: As(self: ConvertToHtmlCommand) -> str
        Set: As(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def Body(self) -> Array:
        """
        Get: Body(self: ConvertToHtmlCommand) -> Array[str]
        Set: Body(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def CssUri(self) -> Uri:
        """
        Get: CssUri(self: ConvertToHtmlCommand) -> Uri
        Set: CssUri(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def Fragment(self) -> SwitchParameter:
        """
        Get: Fragment(self: ConvertToHtmlCommand) -> SwitchParameter
        Set: Fragment(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def Head(self) -> Array:
        """
        Get: Head(self: ConvertToHtmlCommand) -> Array[str]
        Set: Head(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: ConvertToHtmlCommand) -> PSObject
        Set: InputObject(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def PostContent(self) -> Array:
        """
        Get: PostContent(self: ConvertToHtmlCommand) -> Array[str]
        Set: PostContent(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def PreContent(self) -> Array:
        """
        Get: PreContent(self: ConvertToHtmlCommand) -> Array[str]
        Set: PreContent(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: ConvertToHtmlCommand) -> Array[object]
        Set: Property(self: ConvertToHtmlCommand) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ConvertToHtmlCommand) -> str
        Set: Title(self: ConvertToHtmlCommand) = value
        """
        ...



class ConvertToJsonCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertToJsonCommand() """
    @property
    def Compress(self) -> SwitchParameter:
        """
        Get: Compress(self: ConvertToJsonCommand) -> SwitchParameter
        Set: Compress(self: ConvertToJsonCommand) = value
        """
        ...

    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: ConvertToJsonCommand) -> int
        Set: Depth(self: ConvertToJsonCommand) = value
        """
        ...

    @property
    def InputObject(self) -> object:
        """
        Get: InputObject(self: ConvertToJsonCommand) -> object
        Set: InputObject(self: ConvertToJsonCommand) = value
        """
        ...



class ConvertToSecureStringCommand(ConvertFromToSecureStringCommandBase): # skipped bases: <type 'object'>
    """ ConvertToSecureStringCommand() """
    @property
    def AsPlainText(self) -> SwitchParameter:
        """
        Get: AsPlainText(self: ConvertToSecureStringCommand) -> SwitchParameter
        Set: AsPlainText(self: ConvertToSecureStringCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ConvertToSecureStringCommand) -> SwitchParameter
        Set: Force(self: ConvertToSecureStringCommand) = value
        """
        ...

    @property
    def String(self) -> str:
        """
        Get: String(self: ConvertToSecureStringCommand) -> str
        Set: String(self: ConvertToSecureStringCommand) = value
        """
        ...



class ConvertToXmlCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertToXmlCommand() """
    @property
    def As(self) -> str:
        """
        Get: As(self: ConvertToXmlCommand) -> str
        Set: As(self: ConvertToXmlCommand) = value
        """
        ...

    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: ConvertToXmlCommand) -> int
        Set: Depth(self: ConvertToXmlCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: ConvertToXmlCommand) -> PSObject
        Set: InputObject(self: ConvertToXmlCommand) = value
        """
        ...

    @property
    def NoTypeInformation(self) -> SwitchParameter:
        """
        Get: NoTypeInformation(self: ConvertToXmlCommand) -> SwitchParameter
        Set: NoTypeInformation(self: ConvertToXmlCommand) = value
        """
        ...



class CopyItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ CopyItemCommand() """
    @property
    def Container(self) -> SwitchParameter:
        """
        Get: Container(self: CopyItemCommand) -> SwitchParameter
        Set: Container(self: CopyItemCommand) = value
        """
        ...

    @property
    def Destination(self) -> str:
        """
        Get: Destination(self: CopyItemCommand) -> str
        Set: Destination(self: CopyItemCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: CopyItemCommand) -> Array[str]
        Set: Exclude(self: CopyItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: CopyItemCommand) -> str
        Set: Filter(self: CopyItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: CopyItemCommand) -> SwitchParameter
        Set: Force(self: CopyItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: CopyItemCommand) -> Array[str]
        Set: Include(self: CopyItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: CopyItemCommand) -> Array[str]
        Set: LiteralPath(self: CopyItemCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: CopyItemCommand) -> SwitchParameter
        Set: PassThru(self: CopyItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: CopyItemCommand) -> Array[str]
        Set: Path(self: CopyItemCommand) = value
        """
        ...

    @property
    def Recurse(self) -> SwitchParameter:
        """
        Get: Recurse(self: CopyItemCommand) -> SwitchParameter
        Set: Recurse(self: CopyItemCommand) = value
        """
        ...



class CopyItemPropertyCommand(PassThroughItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ CopyItemPropertyCommand() """
    @property
    def Destination(self) -> str:
        """
        Get: Destination(self: CopyItemPropertyCommand) -> str
        Set: Destination(self: CopyItemPropertyCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: CopyItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: CopyItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CopyItemPropertyCommand) -> str
        Set: Name(self: CopyItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: CopyItemPropertyCommand) -> Array[str]
        Set: Path(self: CopyItemPropertyCommand) = value
        """
        ...



class CpuArchitecture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CpuArchitecture, values: Alpha (2), ARM (5), ia64 (6), MIPs (1), PowerPC (3), x64 (9), x86 (0) """
    Alpha: CpuArchitecture = ...
    ARM: CpuArchitecture = ...
    ia64: CpuArchitecture = ...
    MIPs: CpuArchitecture = ...
    PowerPC: CpuArchitecture = ...
    value__ = ...
    x64: CpuArchitecture = ...
    x86: CpuArchitecture = ...


class CpuAvailability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CpuAvailability, values: Degraded (10), InstallError (12), InTest (5), NotApplicable (6), NotConfigured (20), NotIntalled (11), NotReady (19), OffDuty (9), OffLine (8), Other (1), Paused (18), PowerCycle (16), PowerOff (7), PowerSaveLowPowerMode (14), PowerSaveStandby (15), PowerSaveUnknown (13), PowerSaveWarning (17), Quiesced (21), RunningOrFullPower (3), Unknown (2), Warning (4) """
    Degraded: CpuAvailability = ...
    InstallError: CpuAvailability = ...
    InTest: CpuAvailability = ...
    NotApplicable: CpuAvailability = ...
    NotConfigured: CpuAvailability = ...
    NotIntalled: CpuAvailability = ...
    NotReady: CpuAvailability = ...
    OffDuty: CpuAvailability = ...
    OffLine: CpuAvailability = ...
    Other: CpuAvailability = ...
    Paused: CpuAvailability = ...
    PowerCycle: CpuAvailability = ...
    PowerOff: CpuAvailability = ...
    PowerSaveLowPowerMode: CpuAvailability = ...
    PowerSaveStandby: CpuAvailability = ...
    PowerSaveUnknown: CpuAvailability = ...
    PowerSaveWarning: CpuAvailability = ...
    Quiesced: CpuAvailability = ...
    RunningOrFullPower: CpuAvailability = ...
    Unknown: CpuAvailability = ...
    value__ = ...
    Warning: CpuAvailability = ...


class CpuStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CpuStatus, values: DisabledByBIOS (3), DisabledByUser (2), Enabled (1), Idle (4), Other (7), Unknown (0) """
    DisabledByBIOS: CpuStatus = ...
    DisabledByUser: CpuStatus = ...
    Enabled: CpuStatus = ...
    Idle: CpuStatus = ...
    Other: CpuStatus = ...
    Unknown: CpuStatus = ...
    value__ = ...


class DataExecutionPreventionSupportPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataExecutionPreventionSupportPolicy, values: AlwaysOff (0), AlwaysOn (1), OptIn (2), OptOut (3) """
    AlwaysOff: DataExecutionPreventionSupportPolicy = ...
    AlwaysOn: DataExecutionPreventionSupportPolicy = ...
    OptIn: DataExecutionPreventionSupportPolicy = ...
    OptOut: DataExecutionPreventionSupportPolicy = ...
    value__ = ...


class DebugJobCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ DebugJobCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: DebugJobCommand) -> int
        Set: Id(self: DebugJobCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: DebugJobCommand) -> Guid
        Set: InstanceId(self: DebugJobCommand) = value
        """
        ...

    @property
    def Job(self) -> Job:
        """
        Get: Job(self: DebugJobCommand) -> Job
        Set: Job(self: DebugJobCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DebugJobCommand) -> str
        Set: Name(self: DebugJobCommand) = value
        """
        ...



class ProcessBaseCommand(Cmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: ProcessBaseCommand) -> Array[Process]
        Set: InputObject(self: ProcessBaseCommand) = value
        """
        ...

    @property
    def SuppliedComputerName(self):
        ...



class DebugProcessCommand(ProcessBaseCommand): # skipped bases: <type 'object'>
    """ DebugProcessCommand() """
    @property
    def Id(self) -> Array:
        """
        Get: Id(self: DebugProcessCommand) -> Array[int]
        Set: Id(self: DebugProcessCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: DebugProcessCommand) -> Array[str]
        Set: Name(self: DebugProcessCommand) = value
        """
        ...



class DebugRunspaceCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ DebugRunspaceCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: DebugRunspaceCommand) -> int
        Set: Id(self: DebugRunspaceCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: DebugRunspaceCommand) -> Guid
        Set: InstanceId(self: DebugRunspaceCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DebugRunspaceCommand) -> str
        Set: Name(self: DebugRunspaceCommand) = value
        """
        ...

    @property
    def Runspace(self) -> Runspace:
        """
        Get: Runspace(self: DebugRunspaceCommand) -> Runspace
        Set: Runspace(self: DebugRunspaceCommand) = value
        """
        ...



class DeviceGuard: # skipped bases: <type 'object'>, <type 'object'>
    """ DeviceGuard() """
    @property
    def AvailableSecurityProperties(self) -> Array:
        """ Get: AvailableSecurityProperties(self: DeviceGuard) -> Array[DeviceGuardHardwareSecure] """
        ...

    @property
    def CodeIntegrityPolicyEnforcementStatus(self) -> Nullable:
        """ Get: CodeIntegrityPolicyEnforcementStatus(self: DeviceGuard) -> Nullable[DeviceGuardConfigCodeIntegrityStatus] """
        ...

    @property
    def RequiredSecurityProperties(self) -> Array:
        """ Get: RequiredSecurityProperties(self: DeviceGuard) -> Array[DeviceGuardHardwareSecure] """
        ...

    @property
    def SecurityServicesConfigured(self) -> Array:
        """ Get: SecurityServicesConfigured(self: DeviceGuard) -> Array[DeviceGuardSoftwareSecure] """
        ...

    @property
    def SecurityServicesRunning(self) -> Array:
        """ Get: SecurityServicesRunning(self: DeviceGuard) -> Array[DeviceGuardSoftwareSecure] """
        ...

    @property
    def UserModeCodeIntegrityPolicyEnforcementStatus(self) -> Nullable:
        """ Get: UserModeCodeIntegrityPolicyEnforcementStatus(self: DeviceGuard) -> Nullable[DeviceGuardConfigCodeIntegrityStatus] """
        ...



class DeviceGuardConfigCodeIntegrityStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeviceGuardConfigCodeIntegrityStatus, values: AuditMode (1), EnforcementMode (2), Off (0) """
    AuditMode: DeviceGuardConfigCodeIntegrityStatus = ...
    EnforcementMode: DeviceGuardConfigCodeIntegrityStatus = ...
    Off: DeviceGuardConfigCodeIntegrityStatus = ...
    value__ = ...


class DeviceGuardHardwareSecure(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeviceGuardHardwareSecure, values: BaseVirtualizationSupport (1), DMAProtection (3), SecureBoot (2), SecureMemoryOverwrite (4) """
    BaseVirtualizationSupport: DeviceGuardHardwareSecure = ...
    DMAProtection: DeviceGuardHardwareSecure = ...
    SecureBoot: DeviceGuardHardwareSecure = ...
    SecureMemoryOverwrite: DeviceGuardHardwareSecure = ...
    value__ = ...


class DeviceGuardSmartStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeviceGuardSmartStatus, values: Configured (1), Off (0), Running (2) """
    Configured: DeviceGuardSmartStatus = ...
    Off: DeviceGuardSmartStatus = ...
    Running: DeviceGuardSmartStatus = ...
    value__ = ...


class DeviceGuardSoftwareSecure(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeviceGuardSoftwareSecure, values: CredentialGuard (1), HypervisorEnforcedCodeIntegrity (2) """
    CredentialGuard: DeviceGuardSoftwareSecure = ...
    HypervisorEnforcedCodeIntegrity: DeviceGuardSoftwareSecure = ...
    value__ = ...


class DisableComputerRestoreCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ DisableComputerRestoreCommand() """
    @property
    def Drive(self) -> Array:
        """
        Get: Drive(self: DisableComputerRestoreCommand) -> Array[str]
        Set: Drive(self: DisableComputerRestoreCommand) = value
        """
        ...



class PSBreakpointCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Breakpoint(self) -> Array:
        """
        Get: Breakpoint(self: PSBreakpointCommandBase) -> Array[Breakpoint]
        Set: Breakpoint(self: PSBreakpointCommandBase) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: PSBreakpointCommandBase) -> Array[int]
        Set: Id(self: PSBreakpointCommandBase) = value
        """
        ...


    def ProcessBreakpoint(self, *args): #cannot find CLR method
        """ ProcessBreakpoint(self: PSBreakpointCommandBase, breakpoint: Breakpoint) """
        ...


class DisablePSBreakpointCommand(PSBreakpointCommandBase): # skipped bases: <type 'object'>
    """ DisablePSBreakpointCommand() """
    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: DisablePSBreakpointCommand) -> SwitchParameter
        Set: PassThru(self: DisablePSBreakpointCommand) = value
        """
        ...



class DisablePSRemotingCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ DisablePSRemotingCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: DisablePSRemotingCommand) -> SwitchParameter
        Set: Force(self: DisablePSRemotingCommand) = value
        """
        ...



class DisablePSSessionConfigurationCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ DisablePSSessionConfigurationCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: DisablePSSessionConfigurationCommand) -> SwitchParameter
        Set: Force(self: DisablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: DisablePSSessionConfigurationCommand) -> Array[str]
        Set: Name(self: DisablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def NoServiceRestart(self) -> SwitchParameter:
        """
        Get: NoServiceRestart(self: DisablePSSessionConfigurationCommand) -> SwitchParameter
        Set: NoServiceRestart(self: DisablePSSessionConfigurationCommand) = value
        """
        ...



class DisableRunspaceDebugCommand(CommonRunspaceCommandBase): # skipped bases: <type 'object'>
    """ DisableRunspaceDebugCommand() """
    pass

class DisconnectPSSessionCommand(IDisposable, PSRunspaceCmdlet): # skipped bases: <type 'object'>
    """ DisconnectPSSessionCommand() """
    @property
    def IdleTimeoutSec(self) -> int:
        """
        Get: IdleTimeoutSec(self: DisconnectPSSessionCommand) -> int
        Set: IdleTimeoutSec(self: DisconnectPSSessionCommand) = value
        """
        ...

    @property
    def OutputBufferingMode(self) -> OutputBufferingMode:
        """
        Get: OutputBufferingMode(self: DisconnectPSSessionCommand) -> OutputBufferingMode
        Set: OutputBufferingMode(self: DisconnectPSSessionCommand) = value
        """
        ...

    @property
    def Session(self) -> Array:
        """
        Get: Session(self: DisconnectPSSessionCommand) -> Array[PSSession]
        Set: Session(self: DisconnectPSSessionCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: DisconnectPSSessionCommand) -> int
        Set: ThrottleLimit(self: DisconnectPSSessionCommand) = value
        """
        ...



class DisplayHintType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DisplayHintType, values: Date (0), DateTime (2), Time (1) """
    Date: DisplayHintType = ...
    DateTime: DisplayHintType = ...
    Time: DisplayHintType = ...
    value__ = ...


class DnsNameProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ DnsNameProperty(cert: X509Certificate2) """
    @property
    def DnsNameList(self) -> List:
        """ Get: DnsNameList(self: DnsNameProperty) -> List[DnsNameRepresentation] """
        ...



class DnsNameRepresentation: # skipped bases: <type 'object'>, <type 'object'>
    """
    DnsNameRepresentation(inputDnsName: str)
    DnsNameRepresentation(inputPunycodeName: str, inputUnicodeName: str)
    """
    @property
    def Punycode(self) -> str:
        """ Get: Punycode(self: DnsNameRepresentation) -> str """
        ...

    @property
    def Unicode(self) -> str:
        """ Get: Unicode(self: DnsNameRepresentation) -> str """
        ...


    def Equals(self, *__args:DnsNameRepresentation) -> bool:
        """ Equals(self: DnsNameRepresentation, dnsName: DnsNameRepresentation) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: DnsNameRepresentation) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class DomainRole(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DomainRole, values: BackupDomainController (4), MemberServer (3), MemberWorkstation (1), PrimaryDomainController (5), StandaloneServer (2), StandaloneWorkstation (0) """
    BackupDomainController: DomainRole = ...
    MemberServer: DomainRole = ...
    MemberWorkstation: DomainRole = ...
    PrimaryDomainController: DomainRole = ...
    StandaloneServer: DomainRole = ...
    StandaloneWorkstation: DomainRole = ...
    value__ = ...


class DriveMatchingCoreCommandBase(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ DriveMatchingCoreCommandBase() """
    pass

class EnableComputerRestoreCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ EnableComputerRestoreCommand() """
    @property
    def Drive(self) -> Array:
        """
        Get: Drive(self: EnableComputerRestoreCommand) -> Array[str]
        Set: Drive(self: EnableComputerRestoreCommand) = value
        """
        ...



class EnablePSBreakpointCommand(PSBreakpointCommandBase): # skipped bases: <type 'object'>
    """ EnablePSBreakpointCommand() """
    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: EnablePSBreakpointCommand) -> SwitchParameter
        Set: PassThru(self: EnablePSBreakpointCommand) = value
        """
        ...



class EnablePSRemotingCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ EnablePSRemotingCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: EnablePSRemotingCommand) -> SwitchParameter
        Set: Force(self: EnablePSRemotingCommand) = value
        """
        ...

    @property
    def SkipNetworkProfileCheck(self) -> SwitchParameter:
        """
        Get: SkipNetworkProfileCheck(self: EnablePSRemotingCommand) -> SwitchParameter
        Set: SkipNetworkProfileCheck(self: EnablePSRemotingCommand) = value
        """
        ...



class EnablePSSessionConfigurationCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ EnablePSSessionConfigurationCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: EnablePSSessionConfigurationCommand) -> SwitchParameter
        Set: Force(self: EnablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: EnablePSSessionConfigurationCommand) -> Array[str]
        Set: Name(self: EnablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def NoServiceRestart(self) -> SwitchParameter:
        """
        Get: NoServiceRestart(self: EnablePSSessionConfigurationCommand) -> SwitchParameter
        Set: NoServiceRestart(self: EnablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def SecurityDescriptorSddl(self) -> str:
        """
        Get: SecurityDescriptorSddl(self: EnablePSSessionConfigurationCommand) -> str
        Set: SecurityDescriptorSddl(self: EnablePSSessionConfigurationCommand) = value
        """
        ...

    @property
    def SkipNetworkProfileCheck(self) -> SwitchParameter:
        """
        Get: SkipNetworkProfileCheck(self: EnablePSSessionConfigurationCommand) -> SwitchParameter
        Set: SkipNetworkProfileCheck(self: EnablePSSessionConfigurationCommand) = value
        """
        ...



class EnableRunspaceDebugCommand(CommonRunspaceCommandBase): # skipped bases: <type 'object'>
    """ EnableRunspaceDebugCommand() """
    @property
    def BreakAll(self) -> SwitchParameter:
        """
        Get: BreakAll(self: EnableRunspaceDebugCommand) -> SwitchParameter
        Set: BreakAll(self: EnableRunspaceDebugCommand) = value
        """
        ...



class EnhancedKeyUsageProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ EnhancedKeyUsageProperty(cert: X509Certificate2) """
    @property
    def EnhancedKeyUsageList(self) -> List:
        """ Get: EnhancedKeyUsageList(self: EnhancedKeyUsageProperty) -> List[EnhancedKeyUsageRepresentation] """
        ...



class EnhancedKeyUsageRepresentation: # skipped bases: <type 'object'>, <type 'object'>
    """ EnhancedKeyUsageRepresentation(inputFriendlyName: str, inputOid: str) """
    @property
    def FriendlyName(self) -> str:
        """ Get: FriendlyName(self: EnhancedKeyUsageRepresentation) -> str """
        ...

    @property
    def ObjectId(self) -> str:
        """ Get: ObjectId(self: EnhancedKeyUsageRepresentation) -> str """
        ...


    def Equals(self, *__args:EnhancedKeyUsageRepresentation) -> bool:
        """ Equals(self: EnhancedKeyUsageRepresentation, keyUsage: EnhancedKeyUsageRepresentation) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: EnhancedKeyUsageRepresentation) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class EnterPSHostProcessCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ EnterPSHostProcessCommand() """
    @property
    def AppDomainName(self) -> str:
        """
        Get: AppDomainName(self: EnterPSHostProcessCommand) -> str
        Set: AppDomainName(self: EnterPSHostProcessCommand) = value
        """
        ...

    @property
    def HostProcessInfo(self): # -> PSHostProcessInfo
        """
        Get: HostProcessInfo(self: EnterPSHostProcessCommand) -> PSHostProcessInfo
        Set: HostProcessInfo(self: EnterPSHostProcessCommand) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: EnterPSHostProcessCommand) -> int
        Set: Id(self: EnterPSHostProcessCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EnterPSHostProcessCommand) -> str
        Set: Name(self: EnterPSHostProcessCommand) = value
        """
        ...

    @property
    def Process(self) -> Process:
        """
        Get: Process(self: EnterPSHostProcessCommand) -> Process
        Set: Process(self: EnterPSHostProcessCommand) = value
        """
        ...



class PSRemotingBaseCmdlet(PSRemotingCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """
        Get: AllowRedirection(self: PSRemotingBaseCmdlet) -> SwitchParameter
        Set: AllowRedirection(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: PSRemotingBaseCmdlet) -> str
        Set: ApplicationName(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: PSRemotingBaseCmdlet) -> AuthenticationMechanism
        Set: Authentication(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: PSRemotingBaseCmdlet) -> str
        Set: CertificateThumbprint(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: PSRemotingBaseCmdlet) -> Array[str]
        Set: ComputerName(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Array:
        """
        Get: ConnectionUri(self: PSRemotingBaseCmdlet) -> Array[Uri]
        Set: ConnectionUri(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ContainerId(self) -> Array:
        """
        Get: ContainerId(self: PSRemotingBaseCmdlet) -> Array[str]
        Set: ContainerId(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: PSRemotingBaseCmdlet) -> PSCredential
        Set: Credential(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: PSRemotingBaseCmdlet) -> int
        Set: Port(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ResolvedComputerNames(self):
        ...

    @property
    def RunAsAdministrator(self) -> SwitchParameter:
        """
        Get: RunAsAdministrator(self: PSRemotingBaseCmdlet) -> SwitchParameter
        Set: RunAsAdministrator(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def Session(self) -> Array:
        """
        Get: Session(self: PSRemotingBaseCmdlet) -> Array[PSSession]
        Set: Session(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: PSRemotingBaseCmdlet) -> PSSessionOption
        Set: SessionOption(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: PSRemotingBaseCmdlet) -> int
        Set: ThrottleLimit(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: PSRemotingBaseCmdlet) -> SwitchParameter
        Set: UseSSL(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def VMId(self) -> Array:
        """
        Get: VMId(self: PSRemotingBaseCmdlet) -> Array[Guid]
        Set: VMId(self: PSRemotingBaseCmdlet) = value
        """
        ...

    @property
    def VMName(self) -> Array:
        """
        Get: VMName(self: PSRemotingBaseCmdlet) -> Array[str]
        Set: VMName(self: PSRemotingBaseCmdlet) = value
        """
        ...


    def ValidateComputerName(self, *args): #cannot find CLR method
        """ ValidateComputerName(self: PSRemotingBaseCmdlet, computerNames: Array[str]) """
        ...

    def ValidateRemoteRunspacesSpecified(self, *args): #cannot find CLR method
        """ ValidateRemoteRunspacesSpecified(self: PSRemotingBaseCmdlet) """
        ...

    UriParameterSet: str = ...


class EnterPSSessionCommand(PSRemotingBaseCmdlet): # skipped bases: <type 'object'>
    """ EnterPSSessionCommand() """
    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: EnterPSSessionCommand) -> str
        Set: ConfigurationName(self: EnterPSSessionCommand) = value
        """
        ...

    @property
    def EnableNetworkAccess(self) -> SwitchParameter:
        """
        Get: EnableNetworkAccess(self: EnterPSSessionCommand) -> SwitchParameter
        Set: EnableNetworkAccess(self: EnterPSSessionCommand) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: EnterPSSessionCommand) -> int
        Set: Id(self: EnterPSSessionCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: EnterPSSessionCommand) -> Guid
        Set: InstanceId(self: EnterPSSessionCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EnterPSSessionCommand) -> str
        Set: Name(self: EnterPSSessionCommand) = value
        """
        ...



class EnvironmentProvider(SessionStateProviderBase): # skipped bases: <type 'IResourceSupplier'>, <type 'IContentCmdletProvider'>, <type 'object'>
    """ EnvironmentProvider() """
    ProviderName: str = ...


class ExitPSHostProcessCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ExitPSHostProcessCommand() """
    pass

class ExitPSSessionCommand(PSRemotingCmdlet): # skipped bases: <type 'object'>
    """ ExitPSSessionCommand() """
    pass

class ExportAliasCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ExportAliasCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: ExportAliasCommand) -> SwitchParameter
        Set: Append(self: ExportAliasCommand) = value
        """
        ...

    @property
    def As(self): # -> ExportAliasFormat
        """
        Get: As(self: ExportAliasCommand) -> ExportAliasFormat
        Set: As(self: ExportAliasCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ExportAliasCommand) -> str
        Set: Description(self: ExportAliasCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportAliasCommand) -> SwitchParameter
        Set: Force(self: ExportAliasCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ExportAliasCommand) -> str
        Set: LiteralPath(self: ExportAliasCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: ExportAliasCommand) -> Array[str]
        Set: Name(self: ExportAliasCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ExportAliasCommand) -> SwitchParameter
        Set: NoClobber(self: ExportAliasCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ExportAliasCommand) -> SwitchParameter
        Set: PassThru(self: ExportAliasCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportAliasCommand) -> str
        Set: Path(self: ExportAliasCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: ExportAliasCommand) -> str
        Set: Scope(self: ExportAliasCommand) = value
        """
        ...



class ExportAliasFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExportAliasFormat, values: Csv (0), Script (1) """
    Csv: ExportAliasFormat = ...
    Script: ExportAliasFormat = ...
    value__ = ...


class ExportClixmlCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ ExportClixmlCommand() """
    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: ExportClixmlCommand) -> int
        Set: Depth(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: ExportClixmlCommand) -> str
        Set: Encoding(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportClixmlCommand) -> SwitchParameter
        Set: Force(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: ExportClixmlCommand) -> PSObject
        Set: InputObject(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ExportClixmlCommand) -> str
        Set: LiteralPath(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ExportClixmlCommand) -> SwitchParameter
        Set: NoClobber(self: ExportClixmlCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportClixmlCommand) -> str
        Set: Path(self: ExportClixmlCommand) = value
        """
        ...



class ExportConsoleCommand(ConsoleCmdletsBase): # skipped bases: <type 'object'>
    """ ExportConsoleCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportConsoleCommand) -> SwitchParameter
        Set: Force(self: ExportConsoleCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ExportConsoleCommand) -> SwitchParameter
        Set: NoClobber(self: ExportConsoleCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportConsoleCommand) -> str
        Set: Path(self: ExportConsoleCommand) = value
        """
        ...



class ExportCounterCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ExportCounterCommand() """
    @property
    def Circular(self) -> SwitchParameter:
        """
        Get: Circular(self: ExportCounterCommand) -> SwitchParameter
        Set: Circular(self: ExportCounterCommand) = value
        """
        ...

    @property
    def FileFormat(self) -> str:
        """
        Get: FileFormat(self: ExportCounterCommand) -> str
        Set: FileFormat(self: ExportCounterCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportCounterCommand) -> SwitchParameter
        Set: Force(self: ExportCounterCommand) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: ExportCounterCommand) -> Array[PerformanceCounterSampleSet]
        Set: InputObject(self: ExportCounterCommand) = value
        """
        ...

    @property
    def MaxSize(self) -> UInt32:
        """
        Get: MaxSize(self: ExportCounterCommand) -> UInt32
        Set: MaxSize(self: ExportCounterCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportCounterCommand) -> str
        Set: Path(self: ExportCounterCommand) = value
        """
        ...



class ExportCsvCommand(BaseCsvWritingCommand, IDisposable): # skipped bases: <type 'object'>
    """ ExportCsvCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: ExportCsvCommand) -> SwitchParameter
        Set: Append(self: ExportCsvCommand) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: ExportCsvCommand) -> str
        Set: Encoding(self: ExportCsvCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportCsvCommand) -> SwitchParameter
        Set: Force(self: ExportCsvCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ExportCsvCommand) -> str
        Set: LiteralPath(self: ExportCsvCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ExportCsvCommand) -> SwitchParameter
        Set: NoClobber(self: ExportCsvCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportCsvCommand) -> str
        Set: Path(self: ExportCsvCommand) = value
        """
        ...



class ExportFormatDataCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ExportFormatDataCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportFormatDataCommand) -> SwitchParameter
        Set: Force(self: ExportFormatDataCommand) = value
        """
        ...

    @property
    def IncludeScriptBlock(self) -> SwitchParameter:
        """
        Get: IncludeScriptBlock(self: ExportFormatDataCommand) -> SwitchParameter
        Set: IncludeScriptBlock(self: ExportFormatDataCommand) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: ExportFormatDataCommand) -> Array[ExtendedTypeDefinition]
        Set: InputObject(self: ExportFormatDataCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ExportFormatDataCommand) -> str
        Set: LiteralPath(self: ExportFormatDataCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ExportFormatDataCommand) -> SwitchParameter
        Set: NoClobber(self: ExportFormatDataCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExportFormatDataCommand) -> str
        Set: Path(self: ExportFormatDataCommand) = value
        """
        ...



class ExportModuleMemberCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ExportModuleMemberCommand() """
    @property
    def Alias(self) -> Array:
        """
        Get: Alias(self: ExportModuleMemberCommand) -> Array[str]
        Set: Alias(self: ExportModuleMemberCommand) = value
        """
        ...

    @property
    def Cmdlet(self) -> Array:
        """
        Get: Cmdlet(self: ExportModuleMemberCommand) -> Array[str]
        Set: Cmdlet(self: ExportModuleMemberCommand) = value
        """
        ...

    @property
    def Function(self) -> Array:
        """
        Get: Function(self: ExportModuleMemberCommand) -> Array[str]
        Set: Function(self: ExportModuleMemberCommand) = value
        """
        ...

    @property
    def Variable(self) -> Array:
        """
        Get: Variable(self: ExportModuleMemberCommand) -> Array[str]
        Set: Variable(self: ExportModuleMemberCommand) = value
        """
        ...



class ImplicitRemotingCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowClobber(self) -> SwitchParameter:
        """
        Get: AllowClobber(self: ImplicitRemotingCommandBase) -> SwitchParameter
        Set: AllowClobber(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: ImplicitRemotingCommandBase) -> Array[object]
        Set: ArgumentList(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: ImplicitRemotingCommandBase) -> X509Certificate2
        Set: Certificate(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def CommandName(self) -> Array:
        """
        Get: CommandName(self: ImplicitRemotingCommandBase) -> Array[str]
        Set: CommandName(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def CommandType(self) -> CommandTypes:
        """
        Get: CommandType(self: ImplicitRemotingCommandBase) -> CommandTypes
        Set: CommandType(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def FormatTypeName(self) -> Array:
        """
        Get: FormatTypeName(self: ImplicitRemotingCommandBase) -> Array[str]
        Set: FormatTypeName(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def FullyQualifiedModule(self) -> Array:
        """
        Get: FullyQualifiedModule(self: ImplicitRemotingCommandBase) -> Array[ModuleSpecification]
        Set: FullyQualifiedModule(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def Module(self) -> Array:
        """
        Get: Module(self: ImplicitRemotingCommandBase) -> Array[str]
        Set: Module(self: ImplicitRemotingCommandBase) = value
        """
        ...

    @property
    def Session(self) -> PSSession:
        """
        Get: Session(self: ImplicitRemotingCommandBase) -> PSSession
        Set: Session(self: ImplicitRemotingCommandBase) = value
        """
        ...



class ExportPSSessionCommand(ImplicitRemotingCommandBase): # skipped bases: <type 'object'>
    """ ExportPSSessionCommand() """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: ExportPSSessionCommand) -> str
        Set: Encoding(self: ExportPSSessionCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ExportPSSessionCommand) -> SwitchParameter
        Set: Force(self: ExportPSSessionCommand) = value
        """
        ...

    @property
    def OutputModule(self) -> str:
        """
        Get: OutputModule(self: ExportPSSessionCommand) -> str
        Set: OutputModule(self: ExportPSSessionCommand) = value
        """
        ...

    @property
    def VersionOfScriptGenerator(self) -> Version:
        """ Get: VersionOfScriptGenerator() -> Version """
        ...




class FileSystemClearContentDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystemClearContentDynamicParameters() """
    @property
    def Stream(self) -> str:
        """
        Get: Stream(self: FileSystemClearContentDynamicParameters) -> str
        Set: Stream(self: FileSystemClearContentDynamicParameters) = value
        """
        ...



class FileSystemCmdletProviderEncoding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FileSystemCmdletProviderEncoding, values: Ascii (8), BigEndianUnicode (4), BigEndianUTF32 (11), Byte (3), Default (9), Oem (10), String (1), Unicode (2), Unknown (0), UTF32 (7), UTF7 (6), UTF8 (5) """
    Ascii: FileSystemCmdletProviderEncoding = ...
    BigEndianUnicode: FileSystemCmdletProviderEncoding = ...
    BigEndianUTF32: FileSystemCmdletProviderEncoding = ...
    Byte: FileSystemCmdletProviderEncoding = ...
    Default: FileSystemCmdletProviderEncoding = ...
    Oem: FileSystemCmdletProviderEncoding = ...
    String: FileSystemCmdletProviderEncoding = ...
    Unicode: FileSystemCmdletProviderEncoding = ...
    Unknown: FileSystemCmdletProviderEncoding = ...
    UTF32: FileSystemCmdletProviderEncoding = ...
    UTF7: FileSystemCmdletProviderEncoding = ...
    UTF8: FileSystemCmdletProviderEncoding = ...
    value__ = ...


class FileSystemContentDynamicParametersBase: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystemContentDynamicParametersBase() """
    @property
    def Encoding(self) -> FileSystemCmdletProviderEncoding:
        """
        Get: Encoding(self: FileSystemContentDynamicParametersBase) -> FileSystemCmdletProviderEncoding
        Set: Encoding(self: FileSystemContentDynamicParametersBase) = value
        """
        ...

    @property
    def EncodingType(self) -> Encoding:
        """ Get: EncodingType(self: FileSystemContentDynamicParametersBase) -> Encoding """
        ...

    @property
    def Stream(self) -> str:
        """
        Get: Stream(self: FileSystemContentDynamicParametersBase) -> str
        Set: Stream(self: FileSystemContentDynamicParametersBase) = value
        """
        ...

    @property
    def UsingByteEncoding(self) -> bool:
        """ Get: UsingByteEncoding(self: FileSystemContentDynamicParametersBase) -> bool """
        ...

    @property
    def WasStreamTypeSpecified(self) -> bool:
        """ Get: WasStreamTypeSpecified(self: FileSystemContentDynamicParametersBase) -> bool """
        ...



class FileSystemContentReaderDynamicParameters(FileSystemContentDynamicParametersBase): # skipped bases: <type 'object'>
    """ FileSystemContentReaderDynamicParameters() """
    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: FileSystemContentReaderDynamicParameters) -> str
        Set: Delimiter(self: FileSystemContentReaderDynamicParameters) = value
        """
        ...

    @property
    def DelimiterSpecified(self) -> bool:
        """ Get: DelimiterSpecified(self: FileSystemContentReaderDynamicParameters) -> bool """
        ...

    @property
    def Raw(self) -> SwitchParameter:
        """
        Get: Raw(self: FileSystemContentReaderDynamicParameters) -> SwitchParameter
        Set: Raw(self: FileSystemContentReaderDynamicParameters) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: FileSystemContentReaderDynamicParameters) -> SwitchParameter
        Set: Wait(self: FileSystemContentReaderDynamicParameters) = value
        """
        ...



class FileSystemContentWriterDynamicParameters(FileSystemContentDynamicParametersBase): # skipped bases: <type 'object'>
    """ FileSystemContentWriterDynamicParameters() """
    @property
    def NoNewline(self) -> SwitchParameter:
        """
        Get: NoNewline(self: FileSystemContentWriterDynamicParameters) -> SwitchParameter
        Set: NoNewline(self: FileSystemContentWriterDynamicParameters) = value
        """
        ...



class FileSystemItemProviderDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystemItemProviderDynamicParameters() """
    @property
    def NewerThan(self) -> Nullable:
        """
        Get: NewerThan(self: FileSystemItemProviderDynamicParameters) -> Nullable[DateTime]
        Set: NewerThan(self: FileSystemItemProviderDynamicParameters) = value
        """
        ...

    @property
    def OlderThan(self) -> Nullable:
        """
        Get: OlderThan(self: FileSystemItemProviderDynamicParameters) -> Nullable[DateTime]
        Set: OlderThan(self: FileSystemItemProviderDynamicParameters) = value
        """
        ...



class FileSystemProvider(ISecurityDescriptorCmdletProvider, ICmdletProviderSupportsHelp, NavigationCmdletProvider, IPropertyCmdletProvider, IContentCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ FileSystemProvider() """
    @staticmethod
    def Mode(instance:PSObject) -> str:
        """ Mode(instance: PSObject) -> str """
        ...

    ProviderName: str = ...


class FileSystemProviderGetItemDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystemProviderGetItemDynamicParameters() """
    @property
    def Stream(self) -> Array:
        """
        Get: Stream(self: FileSystemProviderGetItemDynamicParameters) -> Array[str]
        Set: Stream(self: FileSystemProviderGetItemDynamicParameters) = value
        """
        ...



class FileSystemProviderRemoveItemDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ FileSystemProviderRemoveItemDynamicParameters() """
    @property
    def Stream(self) -> Array:
        """
        Get: Stream(self: FileSystemProviderRemoveItemDynamicParameters) -> Array[str]
        Set: Stream(self: FileSystemProviderRemoveItemDynamicParameters) = value
        """
        ...



class FirmwareType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirmwareType, values: Bios (1), Max (3), Uefi (2), Unknown (0) """
    Bios: FirmwareType = ...
    Max: FirmwareType = ...
    Uefi: FirmwareType = ...
    Unknown: FirmwareType = ...
    value__ = ...


class ForEachObjectCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ForEachObjectCommand() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: ForEachObjectCommand) -> Array[object]
        Set: ArgumentList(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def Begin(self) -> ScriptBlock:
        """
        Get: Begin(self: ForEachObjectCommand) -> ScriptBlock
        Set: Begin(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def End(self) -> ScriptBlock:
        """
        Get: End(self: ForEachObjectCommand) -> ScriptBlock
        Set: End(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: ForEachObjectCommand) -> PSObject
        Set: InputObject(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: ForEachObjectCommand) -> str
        Set: MemberName(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def Process(self) -> Array:
        """
        Get: Process(self: ForEachObjectCommand) -> Array[ScriptBlock]
        Set: Process(self: ForEachObjectCommand) = value
        """
        ...

    @property
    def RemainingScripts(self) -> Array:
        """
        Get: RemainingScripts(self: ForEachObjectCommand) -> Array[ScriptBlock]
        Set: RemainingScripts(self: ForEachObjectCommand) = value
        """
        ...



class ForegroundApplicationBoost(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ForegroundApplicationBoost, values: Maximum (2), Minimum (1), None (0) """
    Maximum: ForegroundApplicationBoost = ...
    Minimum: ForegroundApplicationBoost = ...
    value__ = ...


class FormatCustomCommand(OuterFormatShapeCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormatCustomCommand() """
    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: FormatCustomCommand) -> int
        Set: Depth(self: FormatCustomCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: FormatCustomCommand) -> Array[object]
        Set: Property(self: FormatCustomCommand) = value
        """
        ...



class FormatDefaultCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormatDefaultCommand() """
    pass

class FormatListCommand(OuterFormatTableAndListBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormatListCommand() """
    pass

class FormatTableCommand(OuterFormatTableBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormatTableCommand() """
    pass

class FormatWideCommand(OuterFormatShapeCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormatWideCommand() """
    @property
    def AutoSize(self) -> SwitchParameter:
        """
        Get: AutoSize(self: FormatWideCommand) -> SwitchParameter
        Set: AutoSize(self: FormatWideCommand) = value
        """
        ...

    @property
    def Column(self) -> int:
        """
        Get: Column(self: FormatWideCommand) -> int
        Set: Column(self: FormatWideCommand) = value
        """
        ...

    @property
    def Property(self) -> object:
        """
        Get: Property(self: FormatWideCommand) -> object
        Set: Property(self: FormatWideCommand) = value
        """
        ...



class FormObject: # skipped bases: <type 'object'>, <type 'object'>
    """ FormObject(id: str, method: str, action: str) """
    @property
    def Action(self) -> str:
        """ Get: Action(self: FormObject) -> str """
        ...

    @property
    def Fields(self) -> Dictionary:
        """ Get: Fields(self: FormObject) -> Dictionary[str, str] """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: FormObject) -> str """
        ...

    @property
    def Method(self) -> str:
        """ Get: Method(self: FormObject) -> str """
        ...



class FormObjectCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[FormObject]'>, <type 'IEnumerable[FormObject]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[FormObject]'>, <type 'IList[FormObject]'>, <type 'ICollection'>, <type 'IReadOnlyList[FormObject]'>, <type 'object'>
    """ FormObjectCollection() """
    pass

class FrontPanelResetStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FrontPanelResetStatus, values: Disabled (0), Enabled (1), NotImplemented (2), Unknown (3) """
    Disabled: FrontPanelResetStatus = ...
    Enabled: FrontPanelResetStatus = ...
    NotImplemented: FrontPanelResetStatus = ...
    Unknown: FrontPanelResetStatus = ...
    value__ = ...


class FunctionProvider(SessionStateProviderBase): # skipped bases: <type 'IResourceSupplier'>, <type 'IContentCmdletProvider'>, <type 'object'>
    """ FunctionProvider() """
    ProviderName: str = ...


class FunctionProviderDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ FunctionProviderDynamicParameters() """
    @property
    def Options(self) -> ScopedItemOptions:
        """
        Get: Options(self: FunctionProviderDynamicParameters) -> ScopedItemOptions
        Set: Options(self: FunctionProviderDynamicParameters) = value
        """
        ...



class MeasureInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Property(self) -> str:
        """
        Get: Property(self: MeasureInfo) -> str
        Set: Property(self: MeasureInfo) = value
        """
        ...



class GenericMeasureInfo(MeasureInfo): # skipped bases: <type 'object'>
    """ GenericMeasureInfo() """
    @property
    def Average(self) -> Nullable:
        """
        Get: Average(self: GenericMeasureInfo) -> Nullable[float]
        Set: Average(self: GenericMeasureInfo) = value
        """
        ...

    @property
    def Count(self) -> int:
        """
        Get: Count(self: GenericMeasureInfo) -> int
        Set: Count(self: GenericMeasureInfo) = value
        """
        ...

    @property
    def Maximum(self) -> Nullable:
        """
        Get: Maximum(self: GenericMeasureInfo) -> Nullable[float]
        Set: Maximum(self: GenericMeasureInfo) = value
        """
        ...

    @property
    def Minimum(self) -> Nullable:
        """
        Get: Minimum(self: GenericMeasureInfo) -> Nullable[float]
        Set: Minimum(self: GenericMeasureInfo) = value
        """
        ...

    @property
    def Sum(self) -> Nullable:
        """
        Get: Sum(self: GenericMeasureInfo) -> Nullable[float]
        Set: Sum(self: GenericMeasureInfo) = value
        """
        ...



class GenericObjectMeasureInfo(MeasureInfo): # skipped bases: <type 'object'>
    """ GenericObjectMeasureInfo() """
    @property
    def Average(self) -> Nullable:
        """
        Get: Average(self: GenericObjectMeasureInfo) -> Nullable[float]
        Set: Average(self: GenericObjectMeasureInfo) = value
        """
        ...

    @property
    def Count(self) -> int:
        """
        Get: Count(self: GenericObjectMeasureInfo) -> int
        Set: Count(self: GenericObjectMeasureInfo) = value
        """
        ...

    @property
    def Maximum(self) -> object:
        """
        Get: Maximum(self: GenericObjectMeasureInfo) -> object
        Set: Maximum(self: GenericObjectMeasureInfo) = value
        """
        ...

    @property
    def Minimum(self) -> object:
        """
        Get: Minimum(self: GenericObjectMeasureInfo) -> object
        Set: Minimum(self: GenericObjectMeasureInfo) = value
        """
        ...

    @property
    def Sum(self) -> Nullable:
        """
        Get: Sum(self: GenericObjectMeasureInfo) -> Nullable[float]
        Set: Sum(self: GenericObjectMeasureInfo) = value
        """
        ...



class SecurityDescriptorCommandsBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: SecurityDescriptorCommandsBase) -> Array[str]
        Set: Exclude(self: SecurityDescriptorCommandsBase) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: SecurityDescriptorCommandsBase) -> str
        Set: Filter(self: SecurityDescriptorCommandsBase) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: SecurityDescriptorCommandsBase) -> Array[str]
        Set: Include(self: SecurityDescriptorCommandsBase) = value
        """
        ...


    @staticmethod
    def GetAccess(instance:PSObject) -> AuthorizationRuleCollection:
        """ GetAccess(instance: PSObject) -> AuthorizationRuleCollection """
        ...

    @staticmethod
    def GetAllCentralAccessPolicies(instance:PSObject) -> Array:
        """ GetAllCentralAccessPolicies(instance: PSObject) -> Array[str] """
        ...

    @staticmethod
    def GetAudit(instance:PSObject) -> AuthorizationRuleCollection:
        """ GetAudit(instance: PSObject) -> AuthorizationRuleCollection """
        ...

    @staticmethod
    def GetCentralAccessPolicyId(instance:PSObject) -> SecurityIdentifier:
        """ GetCentralAccessPolicyId(instance: PSObject) -> SecurityIdentifier """
        ...

    @staticmethod
    def GetCentralAccessPolicyName(instance:PSObject) -> str:
        """ GetCentralAccessPolicyName(instance: PSObject) -> str """
        ...

    @staticmethod
    def GetGroup(instance:PSObject) -> str:
        """ GetGroup(instance: PSObject) -> str """
        ...

    @staticmethod
    def GetOwner(instance:PSObject) -> str:
        """ GetOwner(instance: PSObject) -> str """
        ...

    @staticmethod
    def GetPath(instance:PSObject) -> str:
        """ GetPath(instance: PSObject) -> str """
        ...

    @staticmethod
    def GetSddl(instance:PSObject) -> str:
        """ GetSddl(instance: PSObject) -> str """
        ...


class GetAclCommand(SecurityDescriptorCommandsBase): # skipped bases: <type 'object'>
    """ GetAclCommand() """
    @property
    def AllCentralAccessPolicies(self) -> SwitchParameter:
        """
        Get: AllCentralAccessPolicies(self: GetAclCommand) -> SwitchParameter
        Set: AllCentralAccessPolicies(self: GetAclCommand) = value
        """
        ...

    @property
    def Audit(self) -> SwitchParameter:
        """
        Get: Audit(self: GetAclCommand) -> SwitchParameter
        Set: Audit(self: GetAclCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: GetAclCommand) -> PSObject
        Set: InputObject(self: GetAclCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetAclCommand) -> Array[str]
        Set: LiteralPath(self: GetAclCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetAclCommand) -> Array[str]
        Set: Path(self: GetAclCommand) = value
        """
        ...



class GetAliasCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetAliasCommand() """
    @property
    def Definition(self) -> Array:
        """
        Get: Definition(self: GetAliasCommand) -> Array[str]
        Set: Definition(self: GetAliasCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: GetAliasCommand) -> Array[str]
        Set: Exclude(self: GetAliasCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetAliasCommand) -> Array[str]
        Set: Name(self: GetAliasCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: GetAliasCommand) -> str
        Set: Scope(self: GetAliasCommand) = value
        """
        ...



class SignatureCommandsBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Content(self) -> Array:
        """
        Get: Content(self: SignatureCommandsBase) -> Array[Byte]
        Set: Content(self: SignatureCommandsBase) = value
        """
        ...

    @property
    def FilePath(self) -> Array:
        """
        Get: FilePath(self: SignatureCommandsBase) -> Array[str]
        Set: FilePath(self: SignatureCommandsBase) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SignatureCommandsBase) -> Array[str]
        Set: LiteralPath(self: SignatureCommandsBase) = value
        """
        ...

    @property
    def Signature(self):
        ...

    @property
    def SourcePathOrExtension(self) -> Array:
        """
        Get: SourcePathOrExtension(self: SignatureCommandsBase) -> Array[str]
        Set: SourcePathOrExtension(self: SignatureCommandsBase) = value
        """
        ...


    def PerformAction(self, *args): #cannot find CLR method
        """
        PerformAction(self: SignatureCommandsBase, filePath: str) -> Signature
        PerformAction(self: SignatureCommandsBase, fileName: str, content: Array[Byte]) -> Signature
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str) """
        ...


class GetAuthenticodeSignatureCommand(SignatureCommandsBase): # skipped bases: <type 'object'>
    """ GetAuthenticodeSignatureCommand() """
    pass

class GetChildItemCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetChildItemCommand() """
    @property
    def Depth(self) -> UInt32:
        """
        Get: Depth(self: GetChildItemCommand) -> UInt32
        Set: Depth(self: GetChildItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetChildItemCommand) -> Array[str]
        Set: LiteralPath(self: GetChildItemCommand) = value
        """
        ...

    @property
    def Name(self) -> SwitchParameter:
        """
        Get: Name(self: GetChildItemCommand) -> SwitchParameter
        Set: Name(self: GetChildItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetChildItemCommand) -> Array[str]
        Set: Path(self: GetChildItemCommand) = value
        """
        ...

    @property
    def Recurse(self) -> SwitchParameter:
        """
        Get: Recurse(self: GetChildItemCommand) -> SwitchParameter
        Set: Recurse(self: GetChildItemCommand) = value
        """
        ...



class GetClipboardCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetClipboardCommand() """
    @property
    def Format(self) -> ClipboardFormat:
        """
        Get: Format(self: GetClipboardCommand) -> ClipboardFormat
        Set: Format(self: GetClipboardCommand) = value
        """
        ...

    @property
    def Raw(self) -> SwitchParameter:
        """
        Get: Raw(self: GetClipboardCommand) -> SwitchParameter
        Set: Raw(self: GetClipboardCommand) = value
        """
        ...

    @property
    def TextFormatType(self) -> TextDataFormat:
        """
        Get: TextFormatType(self: GetClipboardCommand) -> TextDataFormat
        Set: TextFormatType(self: GetClipboardCommand) = value
        """
        ...



class GetCmsMessageCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetCmsMessageCommand() """
    @property
    def Content(self) -> str:
        """
        Get: Content(self: GetCmsMessageCommand) -> str
        Set: Content(self: GetCmsMessageCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: GetCmsMessageCommand) -> str
        Set: LiteralPath(self: GetCmsMessageCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: GetCmsMessageCommand) -> str
        Set: Path(self: GetCmsMessageCommand) = value
        """
        ...



class GetCommandCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetCommandCommand() """
    @property
    def All(self) -> SwitchParameter:
        """
        Get: All(self: GetCommandCommand) -> SwitchParameter
        Set: All(self: GetCommandCommand) = value
        """
        ...

    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: GetCommandCommand) -> Array[object]
        Set: ArgumentList(self: GetCommandCommand) = value
        """
        ...

    @property
    def CommandType(self) -> CommandTypes:
        """
        Get: CommandType(self: GetCommandCommand) -> CommandTypes
        Set: CommandType(self: GetCommandCommand) = value
        """
        ...

    @property
    def FullyQualifiedModule(self) -> Array:
        """
        Get: FullyQualifiedModule(self: GetCommandCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedModule(self: GetCommandCommand) = value
        """
        ...

    @property
    def ListImported(self) -> SwitchParameter:
        """
        Get: ListImported(self: GetCommandCommand) -> SwitchParameter
        Set: ListImported(self: GetCommandCommand) = value
        """
        ...

    @property
    def Module(self) -> Array:
        """
        Get: Module(self: GetCommandCommand) -> Array[str]
        Set: Module(self: GetCommandCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetCommandCommand) -> Array[str]
        Set: Name(self: GetCommandCommand) = value
        """
        ...

    @property
    def Noun(self) -> Array:
        """
        Get: Noun(self: GetCommandCommand) -> Array[str]
        Set: Noun(self: GetCommandCommand) = value
        """
        ...

    @property
    def ParameterName(self) -> Array:
        """
        Get: ParameterName(self: GetCommandCommand) -> Array[str]
        Set: ParameterName(self: GetCommandCommand) = value
        """
        ...

    @property
    def ParameterType(self) -> Array:
        """
        Get: ParameterType(self: GetCommandCommand) -> Array[PSTypeName]
        Set: ParameterType(self: GetCommandCommand) = value
        """
        ...

    @property
    def ShowCommandInfo(self) -> SwitchParameter:
        """
        Get: ShowCommandInfo(self: GetCommandCommand) -> SwitchParameter
        Set: ShowCommandInfo(self: GetCommandCommand) = value
        """
        ...

    @property
    def Syntax(self) -> SwitchParameter:
        """
        Get: Syntax(self: GetCommandCommand) -> SwitchParameter
        Set: Syntax(self: GetCommandCommand) = value
        """
        ...

    @property
    def TotalCount(self) -> int:
        """
        Get: TotalCount(self: GetCommandCommand) -> int
        Set: TotalCount(self: GetCommandCommand) = value
        """
        ...

    @property
    def Verb(self) -> Array:
        """
        Get: Verb(self: GetCommandCommand) -> Array[str]
        Set: Verb(self: GetCommandCommand) = value
        """
        ...



class GetComputerInfoCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetComputerInfoCommand() """
    @property
    def Property(self) -> Array:
        """
        Get: Property(self: GetComputerInfoCommand) -> Array[str]
        Set: Property(self: GetComputerInfoCommand) = value
        """
        ...



class GetComputerRestorePointCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ GetComputerRestorePointCommand() """
    @property
    def LastStatus(self) -> SwitchParameter:
        """
        Get: LastStatus(self: GetComputerRestorePointCommand) -> SwitchParameter
        Set: LastStatus(self: GetComputerRestorePointCommand) = value
        """
        ...

    @property
    def RestorePoint(self) -> Array:
        """
        Get: RestorePoint(self: GetComputerRestorePointCommand) -> Array[int]
        Set: RestorePoint(self: GetComputerRestorePointCommand) = value
        """
        ...



class GetContentCommand(ContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ GetContentCommand() """
    @property
    def ReadCount(self) -> Int64:
        """
        Get: ReadCount(self: GetContentCommand) -> Int64
        Set: ReadCount(self: GetContentCommand) = value
        """
        ...

    @property
    def Tail(self) -> int:
        """
        Get: Tail(self: GetContentCommand) -> int
        Set: Tail(self: GetContentCommand) = value
        """
        ...

    @property
    def TotalCount(self) -> Int64:
        """
        Get: TotalCount(self: GetContentCommand) -> Int64
        Set: TotalCount(self: GetContentCommand) = value
        """
        ...



class GetControlPanelItemCommand(ControlPanelItemBaseCommand): # skipped bases: <type 'object'>
    """ GetControlPanelItemCommand() """
    @property
    def CanonicalName(self) -> Array:
        """
        Get: CanonicalName(self: GetControlPanelItemCommand) -> Array[str]
        Set: CanonicalName(self: GetControlPanelItemCommand) = value
        """
        ...

    @property
    def Category(self) -> Array:
        """
        Get: Category(self: GetControlPanelItemCommand) -> Array[str]
        Set: Category(self: GetControlPanelItemCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetControlPanelItemCommand) -> Array[str]
        Set: Name(self: GetControlPanelItemCommand) = value
        """
        ...



class GetCounterCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetCounterCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: GetCounterCommand) -> Array[str]
        Set: ComputerName(self: GetCounterCommand) = value
        """
        ...

    @property
    def Continuous(self) -> SwitchParameter:
        """
        Get: Continuous(self: GetCounterCommand) -> SwitchParameter
        Set: Continuous(self: GetCounterCommand) = value
        """
        ...

    @property
    def Counter(self) -> Array:
        """
        Get: Counter(self: GetCounterCommand) -> Array[str]
        Set: Counter(self: GetCounterCommand) = value
        """
        ...

    @property
    def ListSet(self) -> Array:
        """
        Get: ListSet(self: GetCounterCommand) -> Array[str]
        Set: ListSet(self: GetCounterCommand) = value
        """
        ...

    @property
    def MaxSamples(self) -> Int64:
        """
        Get: MaxSamples(self: GetCounterCommand) -> Int64
        Set: MaxSamples(self: GetCounterCommand) = value
        """
        ...

    @property
    def SampleInterval(self) -> int:
        """
        Get: SampleInterval(self: GetCounterCommand) -> int
        Set: SampleInterval(self: GetCounterCommand) = value
        """
        ...



class GetCredentialCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetCredentialCommand() """
    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: GetCredentialCommand) -> PSCredential
        Set: Credential(self: GetCredentialCommand) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: GetCredentialCommand) -> str
        Set: Message(self: GetCredentialCommand) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: GetCredentialCommand) -> str
        Set: UserName(self: GetCredentialCommand) = value
        """
        ...



class GetCultureCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetCultureCommand() """
    pass

class GetDateCommand(Cmdlet): # skipped bases: <type 'object'>
    """ GetDateCommand() """
    @property
    def Date(self) -> DateTime:
        """
        Get: Date(self: GetDateCommand) -> DateTime
        Set: Date(self: GetDateCommand) = value
        """
        ...

    @property
    def Day(self) -> int:
        """
        Get: Day(self: GetDateCommand) -> int
        Set: Day(self: GetDateCommand) = value
        """
        ...

    @property
    def DisplayHint(self) -> DisplayHintType:
        """
        Get: DisplayHint(self: GetDateCommand) -> DisplayHintType
        Set: DisplayHint(self: GetDateCommand) = value
        """
        ...

    @property
    def Format(self) -> str:
        """
        Get: Format(self: GetDateCommand) -> str
        Set: Format(self: GetDateCommand) = value
        """
        ...

    @property
    def Hour(self) -> int:
        """
        Get: Hour(self: GetDateCommand) -> int
        Set: Hour(self: GetDateCommand) = value
        """
        ...

    @property
    def Millisecond(self) -> int:
        """
        Get: Millisecond(self: GetDateCommand) -> int
        Set: Millisecond(self: GetDateCommand) = value
        """
        ...

    @property
    def Minute(self) -> int:
        """
        Get: Minute(self: GetDateCommand) -> int
        Set: Minute(self: GetDateCommand) = value
        """
        ...

    @property
    def Month(self) -> int:
        """
        Get: Month(self: GetDateCommand) -> int
        Set: Month(self: GetDateCommand) = value
        """
        ...

    @property
    def Second(self) -> int:
        """
        Get: Second(self: GetDateCommand) -> int
        Set: Second(self: GetDateCommand) = value
        """
        ...

    @property
    def UFormat(self) -> str:
        """
        Get: UFormat(self: GetDateCommand) -> str
        Set: UFormat(self: GetDateCommand) = value
        """
        ...

    @property
    def Year(self) -> int:
        """
        Get: Year(self: GetDateCommand) -> int
        Set: Year(self: GetDateCommand) = value
        """
        ...



class GetEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetEventCommand() """
    @property
    def EventIdentifier(self) -> int:
        """
        Get: EventIdentifier(self: GetEventCommand) -> int
        Set: EventIdentifier(self: GetEventCommand) = value
        """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: GetEventCommand) -> str
        Set: SourceIdentifier(self: GetEventCommand) = value
        """
        ...



class GetEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetEventLogCommand() """
    @property
    def After(self) -> DateTime:
        """
        Get: After(self: GetEventLogCommand) -> DateTime
        Set: After(self: GetEventLogCommand) = value
        """
        ...

    @property
    def AsBaseObject(self) -> SwitchParameter:
        """
        Get: AsBaseObject(self: GetEventLogCommand) -> SwitchParameter
        Set: AsBaseObject(self: GetEventLogCommand) = value
        """
        ...

    @property
    def AsString(self) -> SwitchParameter:
        """
        Get: AsString(self: GetEventLogCommand) -> SwitchParameter
        Set: AsString(self: GetEventLogCommand) = value
        """
        ...

    @property
    def Before(self) -> DateTime:
        """
        Get: Before(self: GetEventLogCommand) -> DateTime
        Set: Before(self: GetEventLogCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: GetEventLogCommand) -> Array[str]
        Set: ComputerName(self: GetEventLogCommand) = value
        """
        ...

    @property
    def EntryType(self) -> Array:
        """
        Get: EntryType(self: GetEventLogCommand) -> Array[str]
        Set: EntryType(self: GetEventLogCommand) = value
        """
        ...

    @property
    def Index(self) -> Array:
        """
        Get: Index(self: GetEventLogCommand) -> Array[int]
        Set: Index(self: GetEventLogCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Array:
        """
        Get: InstanceId(self: GetEventLogCommand) -> Array[Int64]
        Set: InstanceId(self: GetEventLogCommand) = value
        """
        ...

    @property
    def List(self) -> SwitchParameter:
        """
        Get: List(self: GetEventLogCommand) -> SwitchParameter
        Set: List(self: GetEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> str:
        """
        Get: LogName(self: GetEventLogCommand) -> str
        Set: LogName(self: GetEventLogCommand) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: GetEventLogCommand) -> str
        Set: Message(self: GetEventLogCommand) = value
        """
        ...

    @property
    def Newest(self) -> int:
        """
        Get: Newest(self: GetEventLogCommand) -> int
        Set: Newest(self: GetEventLogCommand) = value
        """
        ...

    @property
    def Source(self) -> Array:
        """
        Get: Source(self: GetEventLogCommand) -> Array[str]
        Set: Source(self: GetEventLogCommand) = value
        """
        ...

    @property
    def UserName(self) -> Array:
        """
        Get: UserName(self: GetEventLogCommand) -> Array[str]
        Set: UserName(self: GetEventLogCommand) = value
        """
        ...



class GetEventPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ GetEventPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: GetEventPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: GetEventPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: GetEventPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: GetEventPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: GetEventPSSnapIn) -> str """
        ...



class GetEventSubscriberCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetEventSubscriberCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: GetEventSubscriberCommand) -> SwitchParameter
        Set: Force(self: GetEventSubscriberCommand) = value
        """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: GetEventSubscriberCommand) -> str
        Set: SourceIdentifier(self: GetEventSubscriberCommand) = value
        """
        ...

    @property
    def SubscriptionId(self) -> int:
        """
        Get: SubscriptionId(self: GetEventSubscriberCommand) -> int
        Set: SubscriptionId(self: GetEventSubscriberCommand) = value
        """
        ...



class GetExecutionPolicyCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetExecutionPolicyCommand() """
    @property
    def List(self) -> SwitchParameter:
        """
        Get: List(self: GetExecutionPolicyCommand) -> SwitchParameter
        Set: List(self: GetExecutionPolicyCommand) = value
        """
        ...

    @property
    def Scope(self) -> ExecutionPolicyScope:
        """
        Get: Scope(self: GetExecutionPolicyCommand) -> ExecutionPolicyScope
        Set: Scope(self: GetExecutionPolicyCommand) = value
        """
        ...



class GetFormatDataCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetFormatDataCommand() """
    @property
    def PowerShellVersion(self) -> Version:
        """
        Get: PowerShellVersion(self: GetFormatDataCommand) -> Version
        Set: PowerShellVersion(self: GetFormatDataCommand) = value
        """
        ...

    @property
    def TypeName(self) -> Array:
        """
        Get: TypeName(self: GetFormatDataCommand) -> Array[str]
        Set: TypeName(self: GetFormatDataCommand) = value
        """
        ...



class GetHelpCodeMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetHelpUri(commandInfoPSObject:PSObject) -> str:
        """ GetHelpUri(commandInfoPSObject: PSObject) -> str """
        ...

    __all__: list = ...


class GetHelpCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetHelpCommand() """
    @property
    def Category(self) -> Array:
        """
        Get: Category(self: GetHelpCommand) -> Array[str]
        Set: Category(self: GetHelpCommand) = value
        """
        ...

    @property
    def Component(self) -> Array:
        """
        Get: Component(self: GetHelpCommand) -> Array[str]
        Set: Component(self: GetHelpCommand) = value
        """
        ...

    @property
    def Detailed(self): # -> 
        """ Set: Detailed(self: GetHelpCommand) = value """
        ...

    @property
    def Examples(self): # -> 
        """ Set: Examples(self: GetHelpCommand) = value """
        ...

    @property
    def Full(self): # -> 
        """ Set: Full(self: GetHelpCommand) = value """
        ...

    @property
    def Functionality(self) -> Array:
        """
        Get: Functionality(self: GetHelpCommand) -> Array[str]
        Set: Functionality(self: GetHelpCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: GetHelpCommand) -> str
        Set: Name(self: GetHelpCommand) = value
        """
        ...

    @property
    def Online(self) -> SwitchParameter:
        """
        Get: Online(self: GetHelpCommand) -> SwitchParameter
        Set: Online(self: GetHelpCommand) = value
        """
        ...

    @property
    def Parameter(self) -> str:
        """
        Get: Parameter(self: GetHelpCommand) -> str
        Set: Parameter(self: GetHelpCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: GetHelpCommand) -> str
        Set: Path(self: GetHelpCommand) = value
        """
        ...

    @property
    def Role(self) -> Array:
        """
        Get: Role(self: GetHelpCommand) -> Array[str]
        Set: Role(self: GetHelpCommand) = value
        """
        ...

    @property
    def ShowWindow(self) -> SwitchParameter:
        """
        Get: ShowWindow(self: GetHelpCommand) -> SwitchParameter
        Set: ShowWindow(self: GetHelpCommand) = value
        """
        ...



class GetHistoryCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetHistoryCommand() """
    @property
    def Count(self) -> int:
        """
        Get: Count(self: GetHistoryCommand) -> int
        Set: Count(self: GetHistoryCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetHistoryCommand) -> Array[Int64]
        Set: Id(self: GetHistoryCommand) = value
        """
        ...



class GetHostCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetHostCommand() """
    pass

class GetHotFixCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ GetHotFixCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: GetHotFixCommand) -> Array[str]
        Set: ComputerName(self: GetHotFixCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: GetHotFixCommand) -> PSCredential
        Set: Credential(self: GetHotFixCommand) = value
        """
        ...

    @property
    def Description(self) -> Array:
        """
        Get: Description(self: GetHotFixCommand) -> Array[str]
        Set: Description(self: GetHotFixCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetHotFixCommand) -> Array[str]
        Set: Id(self: GetHotFixCommand) = value
        """
        ...



class GetItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetItemCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: GetItemCommand) -> Array[str]
        Set: Exclude(self: GetItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: GetItemCommand) -> str
        Set: Filter(self: GetItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: GetItemCommand) -> SwitchParameter
        Set: Force(self: GetItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: GetItemCommand) -> Array[str]
        Set: Include(self: GetItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetItemCommand) -> Array[str]
        Set: LiteralPath(self: GetItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetItemCommand) -> Array[str]
        Set: Path(self: GetItemCommand) = value
        """
        ...



class GetItemPropertyCommand(ItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetItemPropertyCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: GetItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetItemPropertyCommand) -> Array[str]
        Set: Name(self: GetItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetItemPropertyCommand) -> Array[str]
        Set: Path(self: GetItemPropertyCommand) = value
        """
        ...



class GetItemPropertyValueCommand(ItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetItemPropertyValueCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetItemPropertyValueCommand) -> Array[str]
        Set: LiteralPath(self: GetItemPropertyValueCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetItemPropertyValueCommand) -> Array[str]
        Set: Name(self: GetItemPropertyValueCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetItemPropertyValueCommand) -> Array[str]
        Set: Path(self: GetItemPropertyValueCommand) = value
        """
        ...



class JobCmdletBase(PSRemotingCmdlet): # skipped bases: <type 'object'>
    """ JobCmdletBase() """
    @property
    def Command(self) -> Array:
        """
        Get: Command(self: JobCmdletBase) -> Array[str]
        Set: Command(self: JobCmdletBase) = value
        """
        ...

    @property
    def Filter(self) -> Hashtable:
        """
        Get: Filter(self: JobCmdletBase) -> Hashtable
        Set: Filter(self: JobCmdletBase) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: JobCmdletBase) -> Array[int]
        Set: Id(self: JobCmdletBase) = value
        """
        ...

    @property
    def InstanceId(self) -> Array:
        """
        Get: InstanceId(self: JobCmdletBase) -> Array[Guid]
        Set: InstanceId(self: JobCmdletBase) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: JobCmdletBase) -> Array[str]
        Set: Name(self: JobCmdletBase) = value
        """
        ...

    @property
    def State(self) -> JobState:
        """
        Get: State(self: JobCmdletBase) -> JobState
        Set: State(self: JobCmdletBase) = value
        """
        ...



class GetJobCommand(JobCmdletBase): # skipped bases: <type 'object'>
    """ GetJobCommand() """
    @property
    def After(self) -> DateTime:
        """
        Get: After(self: GetJobCommand) -> DateTime
        Set: After(self: GetJobCommand) = value
        """
        ...

    @property
    def Before(self) -> DateTime:
        """
        Get: Before(self: GetJobCommand) -> DateTime
        Set: Before(self: GetJobCommand) = value
        """
        ...

    @property
    def ChildJobState(self) -> JobState:
        """
        Get: ChildJobState(self: GetJobCommand) -> JobState
        Set: ChildJobState(self: GetJobCommand) = value
        """
        ...

    @property
    def HasMoreData(self) -> bool:
        """
        Get: HasMoreData(self: GetJobCommand) -> bool
        Set: HasMoreData(self: GetJobCommand) = value
        """
        ...

    @property
    def IncludeChildJob(self) -> SwitchParameter:
        """
        Get: IncludeChildJob(self: GetJobCommand) -> SwitchParameter
        Set: IncludeChildJob(self: GetJobCommand) = value
        """
        ...

    @property
    def Newest(self) -> int:
        """
        Get: Newest(self: GetJobCommand) -> int
        Set: Newest(self: GetJobCommand) = value
        """
        ...


    def FindJobs(self, *args): #cannot find CLR method
        """ FindJobs(self: GetJobCommand) -> List[Job] """
        ...


class GetLocationCommand(DriveMatchingCoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetLocationCommand() """
    @property
    def PSDrive(self) -> Array:
        """
        Get: PSDrive(self: GetLocationCommand) -> Array[str]
        Set: PSDrive(self: GetLocationCommand) = value
        """
        ...

    @property
    def PSProvider(self) -> Array:
        """
        Get: PSProvider(self: GetLocationCommand) -> Array[str]
        Set: PSProvider(self: GetLocationCommand) = value
        """
        ...

    @property
    def Stack(self) -> SwitchParameter:
        """
        Get: Stack(self: GetLocationCommand) -> SwitchParameter
        Set: Stack(self: GetLocationCommand) = value
        """
        ...

    @property
    def StackName(self) -> Array:
        """
        Get: StackName(self: GetLocationCommand) -> Array[str]
        Set: StackName(self: GetLocationCommand) = value
        """
        ...



class GetMemberCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetMemberCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: GetMemberCommand) -> SwitchParameter
        Set: Force(self: GetMemberCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: GetMemberCommand) -> PSObject
        Set: InputObject(self: GetMemberCommand) = value
        """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """
        Get: MemberType(self: GetMemberCommand) -> PSMemberTypes
        Set: MemberType(self: GetMemberCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetMemberCommand) -> Array[str]
        Set: Name(self: GetMemberCommand) = value
        """
        ...

    @property
    def Static(self) -> SwitchParameter:
        """
        Get: Static(self: GetMemberCommand) -> SwitchParameter
        Set: Static(self: GetMemberCommand) = value
        """
        ...

    @property
    def View(self) -> PSMemberViewTypes:
        """
        Get: View(self: GetMemberCommand) -> PSMemberViewTypes
        Set: View(self: GetMemberCommand) = value
        """
        ...



class ModuleCmdletBase(PSCmdlet): # skipped bases: <type 'object'>
    """ ModuleCmdletBase() """
    @property
    def AddToAppDomainLevelCache(self):
        ...

    @property
    def BaseArgumentList(self):
        ...

    @property
    def BaseDisableNameChecking(self):
        ...


    def ImportModuleMembers(self, *args): #cannot find CLR method
        """ ImportModuleMembers(self: ModuleCmdletBase, sourceModule: PSModuleInfo, prefix: str)ImportModuleMembers(self: ModuleCmdletBase, sourceModule: PSModuleInfo, prefix: str, options: ImportModuleOptions) """
        ...

    def ImportModuleOptions(self, *args): #cannot find CLR method
        """ no doc """
        ...



class GetModuleCommand(IDisposable, ModuleCmdletBase): # skipped bases: <type 'object'>
    """ GetModuleCommand() """
    @property
    def All(self) -> SwitchParameter:
        """
        Get: All(self: GetModuleCommand) -> SwitchParameter
        Set: All(self: GetModuleCommand) = value
        """
        ...

    @property
    def CimNamespace(self) -> str:
        """
        Get: CimNamespace(self: GetModuleCommand) -> str
        Set: CimNamespace(self: GetModuleCommand) = value
        """
        ...

    @property
    def CimResourceUri(self) -> Uri:
        """
        Get: CimResourceUri(self: GetModuleCommand) -> Uri
        Set: CimResourceUri(self: GetModuleCommand) = value
        """
        ...

    @property
    def CimSession(self): # -> CimSession
        """
        Get: CimSession(self: GetModuleCommand) -> CimSession
        Set: CimSession(self: GetModuleCommand) = value
        """
        ...

    @property
    def FullyQualifiedName(self) -> Array:
        """
        Get: FullyQualifiedName(self: GetModuleCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedName(self: GetModuleCommand) = value
        """
        ...

    @property
    def ListAvailable(self) -> SwitchParameter:
        """
        Get: ListAvailable(self: GetModuleCommand) -> SwitchParameter
        Set: ListAvailable(self: GetModuleCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetModuleCommand) -> Array[str]
        Set: Name(self: GetModuleCommand) = value
        """
        ...

    @property
    def PSEdition(self) -> str:
        """
        Get: PSEdition(self: GetModuleCommand) -> str
        Set: PSEdition(self: GetModuleCommand) = value
        """
        ...

    @property
    def PSSession(self) -> PSSession:
        """
        Get: PSSession(self: GetModuleCommand) -> PSSession
        Set: PSSession(self: GetModuleCommand) = value
        """
        ...

    @property
    def Refresh(self) -> SwitchParameter:
        """
        Get: Refresh(self: GetModuleCommand) -> SwitchParameter
        Set: Refresh(self: GetModuleCommand) = value
        """
        ...



class GetPfxCertificateCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPfxCertificateCommand() """
    @property
    def FilePath(self) -> Array:
        """
        Get: FilePath(self: GetPfxCertificateCommand) -> Array[str]
        Set: FilePath(self: GetPfxCertificateCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: GetPfxCertificateCommand) -> Array[str]
        Set: LiteralPath(self: GetPfxCertificateCommand) = value
        """
        ...



class GetProcessCommand(ProcessBaseCommand): # skipped bases: <type 'object'>
    """ GetProcessCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: GetProcessCommand) -> Array[str]
        Set: ComputerName(self: GetProcessCommand) = value
        """
        ...

    @property
    def FileVersionInfo(self) -> SwitchParameter:
        """
        Get: FileVersionInfo(self: GetProcessCommand) -> SwitchParameter
        Set: FileVersionInfo(self: GetProcessCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetProcessCommand) -> Array[int]
        Set: Id(self: GetProcessCommand) = value
        """
        ...

    @property
    def IncludeUserName(self) -> SwitchParameter:
        """
        Get: IncludeUserName(self: GetProcessCommand) -> SwitchParameter
        Set: IncludeUserName(self: GetProcessCommand) = value
        """
        ...

    @property
    def Module(self) -> SwitchParameter:
        """
        Get: Module(self: GetProcessCommand) -> SwitchParameter
        Set: Module(self: GetProcessCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetProcessCommand) -> Array[str]
        Set: Name(self: GetProcessCommand) = value
        """
        ...



class GetPSBreakpointCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPSBreakpointCommand() """
    @property
    def Command(self) -> Array:
        """
        Get: Command(self: GetPSBreakpointCommand) -> Array[str]
        Set: Command(self: GetPSBreakpointCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetPSBreakpointCommand) -> Array[int]
        Set: Id(self: GetPSBreakpointCommand) = value
        """
        ...

    @property
    def Script(self) -> Array:
        """
        Get: Script(self: GetPSBreakpointCommand) -> Array[str]
        Set: Script(self: GetPSBreakpointCommand) = value
        """
        ...

    @property
    def Type(self) -> Array:
        """
        Get: Type(self: GetPSBreakpointCommand) -> Array[BreakpointType]
        Set: Type(self: GetPSBreakpointCommand) = value
        """
        ...

    @property
    def Variable(self) -> Array:
        """
        Get: Variable(self: GetPSBreakpointCommand) -> Array[str]
        Set: Variable(self: GetPSBreakpointCommand) = value
        """
        ...



class GetPSCallStackCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPSCallStackCommand() """
    pass

class GetPSDriveCommand(DriveMatchingCoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetPSDriveCommand() """
    @property
    def LiteralName(self) -> Array:
        """
        Get: LiteralName(self: GetPSDriveCommand) -> Array[str]
        Set: LiteralName(self: GetPSDriveCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetPSDriveCommand) -> Array[str]
        Set: Name(self: GetPSDriveCommand) = value
        """
        ...

    @property
    def PSProvider(self) -> Array:
        """
        Get: PSProvider(self: GetPSDriveCommand) -> Array[str]
        Set: PSProvider(self: GetPSDriveCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: GetPSDriveCommand) -> str
        Set: Scope(self: GetPSDriveCommand) = value
        """
        ...



class GetPSHostProcessInfoCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPSHostProcessInfoCommand() """
    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetPSHostProcessInfoCommand) -> Array[int]
        Set: Id(self: GetPSHostProcessInfoCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetPSHostProcessInfoCommand) -> Array[str]
        Set: Name(self: GetPSHostProcessInfoCommand) = value
        """
        ...

    @property
    def Process(self) -> Array:
        """
        Get: Process(self: GetPSHostProcessInfoCommand) -> Array[Process]
        Set: Process(self: GetPSHostProcessInfoCommand) = value
        """
        ...



class GetPSProviderCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ GetPSProviderCommand() """
    @property
    def PSProvider(self) -> Array:
        """
        Get: PSProvider(self: GetPSProviderCommand) -> Array[str]
        Set: PSProvider(self: GetPSProviderCommand) = value
        """
        ...



class GetPSSessionCapabilityCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPSSessionCapabilityCommand() """
    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: GetPSSessionCapabilityCommand) -> str
        Set: ConfigurationName(self: GetPSSessionCapabilityCommand) = value
        """
        ...

    @property
    def Full(self) -> SwitchParameter:
        """
        Get: Full(self: GetPSSessionCapabilityCommand) -> SwitchParameter
        Set: Full(self: GetPSSessionCapabilityCommand) = value
        """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: GetPSSessionCapabilityCommand) -> str
        Set: Username(self: GetPSSessionCapabilityCommand) = value
        """
        ...



class GetPSSessionCommand(IDisposable, PSRunspaceCmdlet): # skipped bases: <type 'object'>
    """ GetPSSessionCommand() """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """
        Get: AllowRedirection(self: GetPSSessionCommand) -> SwitchParameter
        Set: AllowRedirection(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: GetPSSessionCommand) -> str
        Set: ApplicationName(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: GetPSSessionCommand) -> AuthenticationMechanism
        Set: Authentication(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: GetPSSessionCommand) -> str
        Set: CertificateThumbprint(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: GetPSSessionCommand) -> str
        Set: ConfigurationName(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Array:
        """
        Get: ConnectionUri(self: GetPSSessionCommand) -> Array[Uri]
        Set: ConnectionUri(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: GetPSSessionCommand) -> PSCredential
        Set: Credential(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: GetPSSessionCommand) -> int
        Set: Port(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: GetPSSessionCommand) -> PSSessionOption
        Set: SessionOption(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def State(self): # -> SessionFilterState
        """
        Get: State(self: GetPSSessionCommand) -> SessionFilterState
        Set: State(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: GetPSSessionCommand) -> int
        Set: ThrottleLimit(self: GetPSSessionCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: GetPSSessionCommand) -> SwitchParameter
        Set: UseSSL(self: GetPSSessionCommand) = value
        """
        ...



class GetPSSessionConfigurationCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetPSSessionConfigurationCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: GetPSSessionConfigurationCommand) -> SwitchParameter
        Set: Force(self: GetPSSessionConfigurationCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetPSSessionConfigurationCommand) -> Array[str]
        Set: Name(self: GetPSSessionConfigurationCommand) = value
        """
        ...



class GetPSSnapinCommand(PSSnapInCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ GetPSSnapinCommand() """
    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetPSSnapinCommand) -> Array[str]
        Set: Name(self: GetPSSnapinCommand) = value
        """
        ...

    @property
    def Registered(self) -> SwitchParameter:
        """
        Get: Registered(self: GetPSSnapinCommand) -> SwitchParameter
        Set: Registered(self: GetPSSnapinCommand) = value
        """
        ...



class GetRandomCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetRandomCommand() """
    @property
    def Count(self) -> int:
        """
        Get: Count(self: GetRandomCommand) -> int
        Set: Count(self: GetRandomCommand) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: GetRandomCommand) -> Array[object]
        Set: InputObject(self: GetRandomCommand) = value
        """
        ...

    @property
    def Maximum(self) -> object:
        """
        Get: Maximum(self: GetRandomCommand) -> object
        Set: Maximum(self: GetRandomCommand) = value
        """
        ...

    @property
    def Minimum(self) -> object:
        """
        Get: Minimum(self: GetRandomCommand) -> object
        Set: Minimum(self: GetRandomCommand) = value
        """
        ...

    @property
    def SetSeed(self) -> Nullable:
        """
        Get: SetSeed(self: GetRandomCommand) -> Nullable[int]
        Set: SetSeed(self: GetRandomCommand) = value
        """
        ...



class GetRunspaceCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetRunspaceCommand() """
    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetRunspaceCommand) -> Array[int]
        Set: Id(self: GetRunspaceCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Array:
        """
        Get: InstanceId(self: GetRunspaceCommand) -> Array[Guid]
        Set: InstanceId(self: GetRunspaceCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetRunspaceCommand) -> Array[str]
        Set: Name(self: GetRunspaceCommand) = value
        """
        ...



class GetRunspaceDebugCommand(CommonRunspaceCommandBase): # skipped bases: <type 'object'>
    """ GetRunspaceDebugCommand() """
    pass

class ServiceBaseCommand(Cmdlet): # skipped bases: <type 'object'>
    """ no doc """
    def ShouldProcessServiceOperation(self, *args): #cannot find CLR method
        """
        ShouldProcessServiceOperation(self: ServiceBaseCommand, service: ServiceController) -> bool
        ShouldProcessServiceOperation(self: ServiceBaseCommand, displayName: str, serviceName: str) -> bool
        """
        ...


class MultipleServiceCommandBase(ServiceBaseCommand): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> Array:
        """
        Get: DisplayName(self: MultipleServiceCommandBase) -> Array[str]
        Set: DisplayName(self: MultipleServiceCommandBase) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: MultipleServiceCommandBase) -> Array[str]
        Set: Exclude(self: MultipleServiceCommandBase) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: MultipleServiceCommandBase) -> Array[str]
        Set: Include(self: MultipleServiceCommandBase) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: MultipleServiceCommandBase) -> Array[ServiceController]
        Set: InputObject(self: MultipleServiceCommandBase) = value
        """
        ...

    @property
    def SuppliedComputerName(self):
        ...



class GetServiceCommand(MultipleServiceCommandBase): # skipped bases: <type 'object'>
    """ GetServiceCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: GetServiceCommand) -> Array[str]
        Set: ComputerName(self: GetServiceCommand) = value
        """
        ...

    @property
    def DependentServices(self) -> SwitchParameter:
        """
        Get: DependentServices(self: GetServiceCommand) -> SwitchParameter
        Set: DependentServices(self: GetServiceCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetServiceCommand) -> Array[str]
        Set: Name(self: GetServiceCommand) = value
        """
        ...

    @property
    def RequiredServices(self) -> SwitchParameter:
        """
        Get: RequiredServices(self: GetServiceCommand) -> SwitchParameter
        Set: RequiredServices(self: GetServiceCommand) = value
        """
        ...



class GetTimeZoneCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetTimeZoneCommand() """
    @property
    def Id(self) -> Array:
        """
        Get: Id(self: GetTimeZoneCommand) -> Array[str]
        Set: Id(self: GetTimeZoneCommand) = value
        """
        ...

    @property
    def ListAvailable(self) -> SwitchParameter:
        """
        Get: ListAvailable(self: GetTimeZoneCommand) -> SwitchParameter
        Set: ListAvailable(self: GetTimeZoneCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetTimeZoneCommand) -> Array[str]
        Set: Name(self: GetTimeZoneCommand) = value
        """
        ...



class TraceCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ TraceCommandBase() """
    pass

class GetTraceSourceCommand(TraceCommandBase): # skipped bases: <type 'object'>
    """ GetTraceSourceCommand() """
    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetTraceSourceCommand) -> Array[str]
        Set: Name(self: GetTraceSourceCommand) = value
        """
        ...



class GetTransactionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetTransactionCommand() """
    pass

class GetTypeDataCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetTypeDataCommand() """
    @property
    def TypeName(self) -> Array:
        """
        Get: TypeName(self: GetTypeDataCommand) -> Array[str]
        Set: TypeName(self: GetTypeDataCommand) = value
        """
        ...



class GetUICultureCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetUICultureCommand() """
    pass

class GetUniqueCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetUniqueCommand() """
    @property
    def AsString(self) -> SwitchParameter:
        """
        Get: AsString(self: GetUniqueCommand) -> SwitchParameter
        Set: AsString(self: GetUniqueCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: GetUniqueCommand) -> PSObject
        Set: InputObject(self: GetUniqueCommand) = value
        """
        ...

    @property
    def OnType(self) -> SwitchParameter:
        """
        Get: OnType(self: GetUniqueCommand) -> SwitchParameter
        Set: OnType(self: GetUniqueCommand) = value
        """
        ...



class GetVariableCommand(VariableCommandBase): # skipped bases: <type 'object'>
    """ GetVariableCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: GetVariableCommand) -> Array[str]
        Set: Exclude(self: GetVariableCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: GetVariableCommand) -> Array[str]
        Set: Include(self: GetVariableCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: GetVariableCommand) -> Array[str]
        Set: Name(self: GetVariableCommand) = value
        """
        ...

    @property
    def ValueOnly(self) -> SwitchParameter:
        """
        Get: ValueOnly(self: GetVariableCommand) -> SwitchParameter
        Set: ValueOnly(self: GetVariableCommand) = value
        """
        ...



class GetWinEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ GetWinEventCommand() """
    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: GetWinEventCommand) -> str
        Set: ComputerName(self: GetWinEventCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: GetWinEventCommand) -> PSCredential
        Set: Credential(self: GetWinEventCommand) = value
        """
        ...

    @property
    def FilterHashtable(self) -> Array:
        """
        Get: FilterHashtable(self: GetWinEventCommand) -> Array[Hashtable]
        Set: FilterHashtable(self: GetWinEventCommand) = value
        """
        ...

    @property
    def FilterXml(self) -> XmlDocument:
        """
        Get: FilterXml(self: GetWinEventCommand) -> XmlDocument
        Set: FilterXml(self: GetWinEventCommand) = value
        """
        ...

    @property
    def FilterXPath(self) -> str:
        """
        Get: FilterXPath(self: GetWinEventCommand) -> str
        Set: FilterXPath(self: GetWinEventCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: GetWinEventCommand) -> SwitchParameter
        Set: Force(self: GetWinEventCommand) = value
        """
        ...

    @property
    def ListLog(self) -> Array:
        """
        Get: ListLog(self: GetWinEventCommand) -> Array[str]
        Set: ListLog(self: GetWinEventCommand) = value
        """
        ...

    @property
    def ListProvider(self) -> Array:
        """
        Get: ListProvider(self: GetWinEventCommand) -> Array[str]
        Set: ListProvider(self: GetWinEventCommand) = value
        """
        ...

    @property
    def LogName(self) -> Array:
        """
        Get: LogName(self: GetWinEventCommand) -> Array[str]
        Set: LogName(self: GetWinEventCommand) = value
        """
        ...

    @property
    def MaxEvents(self) -> Int64:
        """
        Get: MaxEvents(self: GetWinEventCommand) -> Int64
        Set: MaxEvents(self: GetWinEventCommand) = value
        """
        ...

    @property
    def Oldest(self) -> SwitchParameter:
        """
        Get: Oldest(self: GetWinEventCommand) -> SwitchParameter
        Set: Oldest(self: GetWinEventCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: GetWinEventCommand) -> Array[str]
        Set: Path(self: GetWinEventCommand) = value
        """
        ...

    @property
    def ProviderName(self) -> Array:
        """
        Get: ProviderName(self: GetWinEventCommand) -> Array[str]
        Set: ProviderName(self: GetWinEventCommand) = value
        """
        ...



class WmiBaseCmdlet(Cmdlet): # skipped bases: <type 'object'>
    """ WmiBaseCmdlet() """
    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: WmiBaseCmdlet) -> SwitchParameter
        Set: AsJob(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationLevel:
        """
        Get: Authentication(self: WmiBaseCmdlet) -> AuthenticationLevel
        Set: Authentication(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Authority(self) -> str:
        """
        Get: Authority(self: WmiBaseCmdlet) -> str
        Set: Authority(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: WmiBaseCmdlet) -> Array[str]
        Set: ComputerName(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: WmiBaseCmdlet) -> PSCredential
        Set: Credential(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def EnableAllPrivileges(self) -> SwitchParameter:
        """
        Get: EnableAllPrivileges(self: WmiBaseCmdlet) -> SwitchParameter
        Set: EnableAllPrivileges(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationLevel:
        """
        Get: Impersonation(self: WmiBaseCmdlet) -> ImpersonationLevel
        Set: Impersonation(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Locale(self) -> str:
        """
        Get: Locale(self: WmiBaseCmdlet) -> str
        Set: Locale(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: WmiBaseCmdlet) -> str
        Set: Namespace(self: WmiBaseCmdlet) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: WmiBaseCmdlet) -> int
        Set: ThrottleLimit(self: WmiBaseCmdlet) = value
        """
        ...



class GetWmiObjectCommand(WmiBaseCmdlet): # skipped bases: <type 'object'>
    """ GetWmiObjectCommand() """
    @property
    def Amended(self) -> SwitchParameter:
        """
        Get: Amended(self: GetWmiObjectCommand) -> SwitchParameter
        Set: Amended(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def Class(self) -> str:
        """
        Get: Class(self: GetWmiObjectCommand) -> str
        Set: Class(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def DirectRead(self) -> SwitchParameter:
        """
        Get: DirectRead(self: GetWmiObjectCommand) -> SwitchParameter
        Set: DirectRead(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: GetWmiObjectCommand) -> str
        Set: Filter(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def List(self) -> SwitchParameter:
        """
        Get: List(self: GetWmiObjectCommand) -> SwitchParameter
        Set: List(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: GetWmiObjectCommand) -> Array[str]
        Set: Property(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def Query(self) -> str:
        """
        Get: Query(self: GetWmiObjectCommand) -> str
        Set: Query(self: GetWmiObjectCommand) = value
        """
        ...

    @property
    def Recurse(self) -> SwitchParameter:
        """
        Get: Recurse(self: GetWmiObjectCommand) -> SwitchParameter
        Set: Recurse(self: GetWmiObjectCommand) = value
        """
        ...



class GroupInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: GroupInfo) -> int """
        ...

    @property
    def Group(self) -> Collection:
        """ Get: Group(self: GroupInfo) -> Collection[PSObject] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: GroupInfo) -> str """
        ...

    @property
    def Values(self) -> ArrayList:
        """ Get: Values(self: GroupInfo) -> ArrayList """
        ...



class GroupInfoNoElement(GroupInfo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ObjectBase(ObjectCmdletBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: ObjectBase) -> PSObject
        Set: InputObject(self: ObjectBase) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: ObjectBase) -> Array[object]
        Set: Property(self: ObjectBase) = value
        """
        ...



class GroupObjectCommand(ObjectBase): # skipped bases: <type 'object'>
    """ GroupObjectCommand() """
    @property
    def AsHashTable(self) -> SwitchParameter:
        """
        Get: AsHashTable(self: GroupObjectCommand) -> SwitchParameter
        Set: AsHashTable(self: GroupObjectCommand) = value
        """
        ...

    @property
    def AsString(self) -> SwitchParameter:
        """
        Get: AsString(self: GroupObjectCommand) -> SwitchParameter
        Set: AsString(self: GroupObjectCommand) = value
        """
        ...

    @property
    def NoElement(self) -> SwitchParameter:
        """
        Get: NoElement(self: GroupObjectCommand) -> SwitchParameter
        Set: NoElement(self: GroupObjectCommand) = value
        """
        ...



class HardwareSecurity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HardwareSecurity, values: Disabled (0), Enabled (1), NotImplemented (2), Unknown (3) """
    Disabled: HardwareSecurity = ...
    Enabled: HardwareSecurity = ...
    NotImplemented: HardwareSecurity = ...
    Unknown: HardwareSecurity = ...
    value__ = ...


class HelpCategoryInvalidException(ArgumentException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HelpCategoryInvalidException(helpCategory: str)
    HelpCategoryInvalidException()
    HelpCategoryInvalidException(helpCategory: str, innerException: Exception)
    """
    @property
    def HelpCategory(self) -> str:
        """ Get: HelpCategory(self: HelpCategoryInvalidException) -> str """
        ...


    SerializeObjectState = ...


class HelpNotFoundException(SystemException, IContainsErrorRecord): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HelpNotFoundException(helpTopic: str)
    HelpNotFoundException()
    HelpNotFoundException(helpTopic: str, innerException: Exception)
    """
    @property
    def HelpTopic(self) -> str:
        """ Get: HelpTopic(self: HelpNotFoundException) -> str """
        ...


    SerializeObjectState = ...


class HistoryInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CommandLine(self) -> str:
        """ Get: CommandLine(self: HistoryInfo) -> str """
        ...

    @property
    def EndExecutionTime(self) -> DateTime:
        """ Get: EndExecutionTime(self: HistoryInfo) -> DateTime """
        ...

    @property
    def ExecutionStatus(self) -> PipelineState:
        """ Get: ExecutionStatus(self: HistoryInfo) -> PipelineState """
        ...

    @property
    def Id(self) -> Int64:
        """ Get: Id(self: HistoryInfo) -> Int64 """
        ...

    @property
    def StartExecutionTime(self) -> DateTime:
        """ Get: StartExecutionTime(self: HistoryInfo) -> DateTime """
        ...


    def Clone(self) -> HistoryInfo:
        """ Clone(self: HistoryInfo) -> HistoryInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: HistoryInfo) -> str """
        ...


class HotFix: # skipped bases: <type 'object'>, <type 'object'>
    """ HotFix() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: HotFix) -> str """
        ...

    @property
    def FixComments(self) -> str:
        """ Get: FixComments(self: HotFix) -> str """
        ...

    @property
    def HotFixID(self) -> str:
        """ Get: HotFixID(self: HotFix) -> str """
        ...

    @property
    def InstalledOn(self) -> str:
        """ Get: InstalledOn(self: HotFix) -> str """
        ...



class HtmlWebResponseObject(IDisposable, WebResponseObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllElements(self): # -> WebCmdletElementCollection
        """ Get: AllElements(self: HtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def Forms(self) -> FormObjectCollection:
        """ Get: Forms(self: HtmlWebResponseObject) -> FormObjectCollection """
        ...

    @property
    def Images(self): # -> WebCmdletElementCollection
        """ Get: Images(self: HtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def InputFields(self): # -> WebCmdletElementCollection
        """ Get: InputFields(self: HtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def Links(self): # -> WebCmdletElementCollection
        """ Get: Links(self: HtmlWebResponseObject) -> WebCmdletElementCollection """
        ...

    @property
    def ParsedHtml(self) -> IHTMLDocument2:
        """ Get: ParsedHtml(self: HtmlWebResponseObject) -> IHTMLDocument2 """
        ...

    @property
    def Scripts(self): # -> WebCmdletElementCollection
        """ Get: Scripts(self: HtmlWebResponseObject) -> WebCmdletElementCollection """
        ...



class ImportAliasCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ImportAliasCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ImportAliasCommand) -> SwitchParameter
        Set: Force(self: ImportAliasCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ImportAliasCommand) -> str
        Set: LiteralPath(self: ImportAliasCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ImportAliasCommand) -> SwitchParameter
        Set: PassThru(self: ImportAliasCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ImportAliasCommand) -> str
        Set: Path(self: ImportAliasCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: ImportAliasCommand) -> str
        Set: Scope(self: ImportAliasCommand) = value
        """
        ...



class ImportClixmlCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ ImportClixmlCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ImportClixmlCommand) -> Array[str]
        Set: LiteralPath(self: ImportClixmlCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ImportClixmlCommand) -> Array[str]
        Set: Path(self: ImportClixmlCommand) = value
        """
        ...



class ImportCounterCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ImportCounterCommand() """
    @property
    def Counter(self) -> Array:
        """
        Get: Counter(self: ImportCounterCommand) -> Array[str]
        Set: Counter(self: ImportCounterCommand) = value
        """
        ...

    @property
    def EndTime(self) -> DateTime:
        """
        Get: EndTime(self: ImportCounterCommand) -> DateTime
        Set: EndTime(self: ImportCounterCommand) = value
        """
        ...

    @property
    def ListSet(self) -> Array:
        """
        Get: ListSet(self: ImportCounterCommand) -> Array[str]
        Set: ListSet(self: ImportCounterCommand) = value
        """
        ...

    @property
    def MaxSamples(self) -> Int64:
        """
        Get: MaxSamples(self: ImportCounterCommand) -> Int64
        Set: MaxSamples(self: ImportCounterCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ImportCounterCommand) -> Array[str]
        Set: Path(self: ImportCounterCommand) = value
        """
        ...

    @property
    def StartTime(self) -> DateTime:
        """
        Get: StartTime(self: ImportCounterCommand) -> DateTime
        Set: StartTime(self: ImportCounterCommand) = value
        """
        ...

    @property
    def Summary(self) -> SwitchParameter:
        """
        Get: Summary(self: ImportCounterCommand) -> SwitchParameter
        Set: Summary(self: ImportCounterCommand) = value
        """
        ...



class ImportCsvCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ImportCsvCommand() """
    @property
    def Delimiter(self) -> Char:
        """
        Get: Delimiter(self: ImportCsvCommand) -> Char
        Set: Delimiter(self: ImportCsvCommand) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: ImportCsvCommand) -> str
        Set: Encoding(self: ImportCsvCommand) = value
        """
        ...

    @property
    def Header(self) -> Array:
        """
        Get: Header(self: ImportCsvCommand) -> Array[str]
        Set: Header(self: ImportCsvCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ImportCsvCommand) -> Array[str]
        Set: LiteralPath(self: ImportCsvCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ImportCsvCommand) -> Array[str]
        Set: Path(self: ImportCsvCommand) = value
        """
        ...

    @property
    def UseCulture(self) -> SwitchParameter:
        """
        Get: UseCulture(self: ImportCsvCommand) -> SwitchParameter
        Set: UseCulture(self: ImportCsvCommand) = value
        """
        ...



class ImportLocalizedData(PSCmdlet): # skipped bases: <type 'object'>
    """ ImportLocalizedData() """
    @property
    def BaseDirectory(self) -> str:
        """
        Get: BaseDirectory(self: ImportLocalizedData) -> str
        Set: BaseDirectory(self: ImportLocalizedData) = value
        """
        ...

    @property
    def BindingVariable(self) -> str:
        """
        Get: BindingVariable(self: ImportLocalizedData) -> str
        Set: BindingVariable(self: ImportLocalizedData) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ImportLocalizedData) -> str
        Set: FileName(self: ImportLocalizedData) = value
        """
        ...

    @property
    def SupportedCommand(self) -> Array:
        """
        Get: SupportedCommand(self: ImportLocalizedData) -> Array[str]
        Set: SupportedCommand(self: ImportLocalizedData) = value
        """
        ...

    @property
    def UICulture(self) -> str:
        """
        Get: UICulture(self: ImportLocalizedData) -> str
        Set: UICulture(self: ImportLocalizedData) = value
        """
        ...



class ImportModuleCommand(IDisposable, ModuleCmdletBase): # skipped bases: <type 'object'>
    """ ImportModuleCommand() """
    @property
    def Alias(self) -> Array:
        """
        Get: Alias(self: ImportModuleCommand) -> Array[str]
        Set: Alias(self: ImportModuleCommand) = value
        """
        ...

    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: ImportModuleCommand) -> Array[object]
        Set: ArgumentList(self: ImportModuleCommand) = value
        """
        ...

    @property
    def AsCustomObject(self) -> SwitchParameter:
        """
        Get: AsCustomObject(self: ImportModuleCommand) -> SwitchParameter
        Set: AsCustomObject(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Assembly(self) -> Array:
        """
        Get: Assembly(self: ImportModuleCommand) -> Array[Assembly]
        Set: Assembly(self: ImportModuleCommand) = value
        """
        ...

    @property
    def CimNamespace(self) -> str:
        """
        Get: CimNamespace(self: ImportModuleCommand) -> str
        Set: CimNamespace(self: ImportModuleCommand) = value
        """
        ...

    @property
    def CimResourceUri(self) -> Uri:
        """
        Get: CimResourceUri(self: ImportModuleCommand) -> Uri
        Set: CimResourceUri(self: ImportModuleCommand) = value
        """
        ...

    @property
    def CimSession(self): # -> CimSession
        """
        Get: CimSession(self: ImportModuleCommand) -> CimSession
        Set: CimSession(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Cmdlet(self) -> Array:
        """
        Get: Cmdlet(self: ImportModuleCommand) -> Array[str]
        Set: Cmdlet(self: ImportModuleCommand) = value
        """
        ...

    @property
    def DisableNameChecking(self) -> SwitchParameter:
        """
        Get: DisableNameChecking(self: ImportModuleCommand) -> SwitchParameter
        Set: DisableNameChecking(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ImportModuleCommand) -> SwitchParameter
        Set: Force(self: ImportModuleCommand) = value
        """
        ...

    @property
    def FullyQualifiedName(self) -> Array:
        """
        Get: FullyQualifiedName(self: ImportModuleCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedName(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Function(self) -> Array:
        """
        Get: Function(self: ImportModuleCommand) -> Array[str]
        Set: Function(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Global(self) -> SwitchParameter:
        """
        Get: Global(self: ImportModuleCommand) -> SwitchParameter
        Set: Global(self: ImportModuleCommand) = value
        """
        ...

    @property
    def MaximumVersion(self) -> str:
        """
        Get: MaximumVersion(self: ImportModuleCommand) -> str
        Set: MaximumVersion(self: ImportModuleCommand) = value
        """
        ...

    @property
    def MinimumVersion(self) -> Version:
        """
        Get: MinimumVersion(self: ImportModuleCommand) -> Version
        Set: MinimumVersion(self: ImportModuleCommand) = value
        """
        ...

    @property
    def ModuleInfo(self) -> Array:
        """
        Get: ModuleInfo(self: ImportModuleCommand) -> Array[PSModuleInfo]
        Set: ModuleInfo(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: ImportModuleCommand) -> Array[str]
        Set: Name(self: ImportModuleCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: ImportModuleCommand) -> SwitchParameter
        Set: NoClobber(self: ImportModuleCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ImportModuleCommand) -> SwitchParameter
        Set: PassThru(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: ImportModuleCommand) -> str
        Set: Prefix(self: ImportModuleCommand) = value
        """
        ...

    @property
    def PSSession(self) -> PSSession:
        """
        Get: PSSession(self: ImportModuleCommand) -> PSSession
        Set: PSSession(self: ImportModuleCommand) = value
        """
        ...

    @property
    def RequiredVersion(self) -> Version:
        """
        Get: RequiredVersion(self: ImportModuleCommand) -> Version
        Set: RequiredVersion(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: ImportModuleCommand) -> str
        Set: Scope(self: ImportModuleCommand) = value
        """
        ...

    @property
    def Variable(self) -> Array:
        """
        Get: Variable(self: ImportModuleCommand) -> Array[str]
        Set: Variable(self: ImportModuleCommand) = value
        """
        ...



class ImportPSSessionCommand(ImplicitRemotingCommandBase): # skipped bases: <type 'object'>
    """ ImportPSSessionCommand() """
    @property
    def DisableNameChecking(self) -> SwitchParameter:
        """
        Get: DisableNameChecking(self: ImportPSSessionCommand) -> SwitchParameter
        Set: DisableNameChecking(self: ImportPSSessionCommand) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: ImportPSSessionCommand) -> str
        Set: Prefix(self: ImportPSSessionCommand) = value
        """
        ...



class InternalSymbolicLinkLinkCodeMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetLinkType(instance:PSObject) -> str:
        """ GetLinkType(instance: PSObject) -> str """
        ...

    @staticmethod
    def GetTarget(instance:PSObject) -> IEnumerable:
        """ GetTarget(instance: PSObject) -> IEnumerable[str] """
        ...

    __all__: list = ...


class PSExecutionCmdlet(PSRemotingBaseCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: PSExecutionCmdlet) -> Array[object]
        Set: ArgumentList(self: PSExecutionCmdlet) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: PSExecutionCmdlet) -> str
        Set: ConfigurationName(self: PSExecutionCmdlet) = value
        """
        ...

    @property
    def DisconnectedSessionName(self):
        ...

    @property
    def EnableNetworkAccess(self) -> SwitchParameter:
        """
        Get: EnableNetworkAccess(self: PSExecutionCmdlet) -> SwitchParameter
        Set: EnableNetworkAccess(self: PSExecutionCmdlet) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: PSExecutionCmdlet) -> str
        Set: FilePath(self: PSExecutionCmdlet) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: PSExecutionCmdlet) -> PSObject
        Set: InputObject(self: PSExecutionCmdlet) = value
        """
        ...

    @property
    def InvokeAndDisconnect(self):
        ...

    @property
    def IsLiteralPath(self):
        ...

    @property
    def ScriptBlock(self) -> ScriptBlock:
        """
        Get: ScriptBlock(self: PSExecutionCmdlet) -> ScriptBlock
        Set: ScriptBlock(self: PSExecutionCmdlet) = value
        """
        ...


    def CloseAllInputStreams(self, *args): #cannot find CLR method
        """ CloseAllInputStreams(self: PSExecutionCmdlet) """
        ...

    def CreateHelpersForSpecifiedComputerNames(self, *args): #cannot find CLR method
        """ CreateHelpersForSpecifiedComputerNames(self: PSExecutionCmdlet) """
        ...

    def CreateHelpersForSpecifiedContainerSession(self, *args): #cannot find CLR method
        """ CreateHelpersForSpecifiedContainerSession(self: PSExecutionCmdlet) """
        ...

    def CreateHelpersForSpecifiedRunspaces(self, *args): #cannot find CLR method
        """ CreateHelpersForSpecifiedRunspaces(self: PSExecutionCmdlet) """
        ...

    def CreateHelpersForSpecifiedUris(self, *args): #cannot find CLR method
        """ CreateHelpersForSpecifiedUris(self: PSExecutionCmdlet) """
        ...

    def CreateHelpersForSpecifiedVMSession(self, *args): #cannot find CLR method
        """ CreateHelpersForSpecifiedVMSession(self: PSExecutionCmdlet) """
        ...

    def GetScriptBlockFromFile(self, *args): #cannot find CLR method
        """ GetScriptBlockFromFile(self: PSExecutionCmdlet, filePath: str, isLiteralPath: bool) -> ScriptBlock """
        ...

    FilePathComputerNameParameterSet: str = ...
    FilePathContainerIdParameterSet: str = ...
    FilePathSessionParameterSet: str = ...
    FilePathUriParameterSet: str = ...
    FilePathVMIdParameterSet: str = ...
    FilePathVMNameParameterSet: str = ...
    LiteralFilePathComputerNameParameterSet: str = ...


class InvokeCommandCommand(IDisposable, PSExecutionCmdlet): # skipped bases: <type 'object'>
    """ InvokeCommandCommand() """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """
        Get: AllowRedirection(self: InvokeCommandCommand) -> SwitchParameter
        Set: AllowRedirection(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: InvokeCommandCommand) -> str
        Set: ApplicationName(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: InvokeCommandCommand) -> SwitchParameter
        Set: AsJob(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: InvokeCommandCommand) -> AuthenticationMechanism
        Set: Authentication(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: InvokeCommandCommand) -> Array[str]
        Set: ComputerName(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Array:
        """
        Get: ConnectionUri(self: InvokeCommandCommand) -> Array[Uri]
        Set: ConnectionUri(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: InvokeCommandCommand) -> PSCredential
        Set: Credential(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def HideComputerName(self) -> SwitchParameter:
        """
        Get: HideComputerName(self: InvokeCommandCommand) -> SwitchParameter
        Set: HideComputerName(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def InDisconnectedSession(self) -> SwitchParameter:
        """
        Get: InDisconnectedSession(self: InvokeCommandCommand) -> SwitchParameter
        Set: InDisconnectedSession(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def JobName(self) -> str:
        """
        Get: JobName(self: InvokeCommandCommand) -> str
        Set: JobName(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def NoNewScope(self) -> SwitchParameter:
        """
        Get: NoNewScope(self: InvokeCommandCommand) -> SwitchParameter
        Set: NoNewScope(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: InvokeCommandCommand) -> int
        Set: Port(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def RunAsAdministrator(self) -> SwitchParameter:
        """
        Get: RunAsAdministrator(self: InvokeCommandCommand) -> SwitchParameter
        Set: RunAsAdministrator(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def Session(self) -> Array:
        """
        Get: Session(self: InvokeCommandCommand) -> Array[PSSession]
        Set: Session(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def SessionName(self) -> Array:
        """
        Get: SessionName(self: InvokeCommandCommand) -> Array[str]
        Set: SessionName(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: InvokeCommandCommand) -> PSSessionOption
        Set: SessionOption(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: InvokeCommandCommand) -> int
        Set: ThrottleLimit(self: InvokeCommandCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: InvokeCommandCommand) -> SwitchParameter
        Set: UseSSL(self: InvokeCommandCommand) = value
        """
        ...



class InvokeExpressionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ InvokeExpressionCommand() """
    @property
    def Command(self) -> str:
        """
        Get: Command(self: InvokeExpressionCommand) -> str
        Set: Command(self: InvokeExpressionCommand) = value
        """
        ...



class InvokeHistoryCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ InvokeHistoryCommand() """
    @property
    def Id(self) -> str:
        """
        Get: Id(self: InvokeHistoryCommand) -> str
        Set: Id(self: InvokeHistoryCommand) = value
        """
        ...



class InvokeItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ InvokeItemCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: InvokeItemCommand) -> Array[str]
        Set: Exclude(self: InvokeItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: InvokeItemCommand) -> str
        Set: Filter(self: InvokeItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: InvokeItemCommand) -> Array[str]
        Set: Include(self: InvokeItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: InvokeItemCommand) -> Array[str]
        Set: LiteralPath(self: InvokeItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: InvokeItemCommand) -> Array[str]
        Set: Path(self: InvokeItemCommand) = value
        """
        ...



class WebRequestPSCmdlet(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> object:
        """
        Get: Body(self: WebRequestPSCmdlet) -> object
        Set: Body(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Certificate(self) -> X509Certificate:
        """
        Get: Certificate(self: WebRequestPSCmdlet) -> X509Certificate
        Set: Certificate(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: WebRequestPSCmdlet) -> str
        Set: CertificateThumbprint(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: WebRequestPSCmdlet) -> str
        Set: ContentType(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: WebRequestPSCmdlet) -> PSCredential
        Set: Credential(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def DisableKeepAlive(self) -> SwitchParameter:
        """
        Get: DisableKeepAlive(self: WebRequestPSCmdlet) -> SwitchParameter
        Set: DisableKeepAlive(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Headers(self) -> IDictionary:
        """
        Get: Headers(self: WebRequestPSCmdlet) -> IDictionary
        Set: Headers(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def InFile(self) -> str:
        """
        Get: InFile(self: WebRequestPSCmdlet) -> str
        Set: InFile(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def MaximumRedirection(self) -> int:
        """
        Get: MaximumRedirection(self: WebRequestPSCmdlet) -> int
        Set: MaximumRedirection(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Method(self): # -> WebRequestMethod
        """
        Get: Method(self: WebRequestPSCmdlet) -> WebRequestMethod
        Set: Method(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def OutFile(self) -> str:
        """
        Get: OutFile(self: WebRequestPSCmdlet) -> str
        Set: OutFile(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: WebRequestPSCmdlet) -> SwitchParameter
        Set: PassThru(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Proxy(self) -> Uri:
        """
        Get: Proxy(self: WebRequestPSCmdlet) -> Uri
        Set: Proxy(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def ProxyCredential(self) -> PSCredential:
        """
        Get: ProxyCredential(self: WebRequestPSCmdlet) -> PSCredential
        Set: ProxyCredential(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def ProxyUseDefaultCredentials(self) -> SwitchParameter:
        """
        Get: ProxyUseDefaultCredentials(self: WebRequestPSCmdlet) -> SwitchParameter
        Set: ProxyUseDefaultCredentials(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def SessionVariable(self) -> str:
        """
        Get: SessionVariable(self: WebRequestPSCmdlet) -> str
        Set: SessionVariable(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def TimeoutSec(self) -> int:
        """
        Get: TimeoutSec(self: WebRequestPSCmdlet) -> int
        Set: TimeoutSec(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def TransferEncoding(self) -> str:
        """
        Get: TransferEncoding(self: WebRequestPSCmdlet) -> str
        Set: TransferEncoding(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: WebRequestPSCmdlet) -> Uri
        Set: Uri(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def UseBasicParsing(self) -> SwitchParameter:
        """
        Get: UseBasicParsing(self: WebRequestPSCmdlet) -> SwitchParameter
        Set: UseBasicParsing(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> SwitchParameter:
        """
        Get: UseDefaultCredentials(self: WebRequestPSCmdlet) -> SwitchParameter
        Set: UseDefaultCredentials(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: WebRequestPSCmdlet) -> str
        Set: UserAgent(self: WebRequestPSCmdlet) = value
        """
        ...

    @property
    def WebSession(self): # -> WebRequestSession
        """
        Get: WebSession(self: WebRequestPSCmdlet) -> WebRequestSession
        Set: WebSession(self: WebRequestPSCmdlet) = value
        """
        ...


    def VerifyInternetExplorerAvailable(self, *args): #cannot find CLR method
        """ VerifyInternetExplorerAvailable(self: WebRequestPSCmdlet, checkComObject: bool) -> bool """
        ...


class InvokeRestMethodCommand(WebRequestPSCmdlet): # skipped bases: <type 'object'>
    """ InvokeRestMethodCommand() """
    def RestReturnType(self, *args): #cannot find CLR method
        """ enum RestReturnType, values: Detect (0), Json (1), Xml (2) """
        ...



class InvokeWebRequestCommand(WebRequestPSCmdlet): # skipped bases: <type 'object'>
    """ InvokeWebRequestCommand() """
    pass

class InvokeWmiMethod(WmiBaseCmdlet): # skipped bases: <type 'object'>
    """ InvokeWmiMethod() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: InvokeWmiMethod) -> Array[object]
        Set: ArgumentList(self: InvokeWmiMethod) = value
        """
        ...

    @property
    def Class(self) -> str:
        """
        Get: Class(self: InvokeWmiMethod) -> str
        Set: Class(self: InvokeWmiMethod) = value
        """
        ...

    @property
    def InputObject(self) -> ManagementObject:
        """
        Get: InputObject(self: InvokeWmiMethod) -> ManagementObject
        Set: InputObject(self: InvokeWmiMethod) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: InvokeWmiMethod) -> str
        Set: Name(self: InvokeWmiMethod) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: InvokeWmiMethod) -> str
        Set: Path(self: InvokeWmiMethod) = value
        """
        ...



class JoinOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) JoinOptions, values: AccountCreate (2), DeferSPNSet (256), InstallInvoke (262144), JoinReadOnly (2048), JoinWithNewName (1024), PasswordPass (128), UnsecuredJoin (64), Win9XUpgrade (16) """
    AccountCreate: JoinOptions = ...
    DeferSPNSet: JoinOptions = ...
    InstallInvoke: JoinOptions = ...
    JoinReadOnly: JoinOptions = ...
    JoinWithNewName: JoinOptions = ...
    PasswordPass: JoinOptions = ...
    UnsecuredJoin: JoinOptions = ...
    value__ = ...
    Win9XUpgrade: JoinOptions = ...


class JoinPathCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ JoinPathCommand() """
    @property
    def ChildPath(self) -> str:
        """
        Get: ChildPath(self: JoinPathCommand) -> str
        Set: ChildPath(self: JoinPathCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: JoinPathCommand) -> Array[str]
        Set: Path(self: JoinPathCommand) = value
        """
        ...

    @property
    def Resolve(self) -> SwitchParameter:
        """
        Get: Resolve(self: JoinPathCommand) -> SwitchParameter
        Set: Resolve(self: JoinPathCommand) = value
        """
        ...



class JsonObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ConvertFromJson(input, error) -> Tuple_[object, ErrorRecord]:
        """ ConvertFromJson(input: str) -> (object, ErrorRecord) """
        ...

    __all__: list = ...


class Language(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Language, values: CSharp (0), CSharpVersion2 (2), CSharpVersion3 (1), JScript (4), VisualBasic (3) """
    CSharp: Language = ...
    CSharpVersion2: Language = ...
    CSharpVersion3: Language = ...
    JScript: Language = ...
    value__ = ...
    VisualBasic: Language = ...


class LimitEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ LimitEventLogCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: LimitEventLogCommand) -> Array[str]
        Set: ComputerName(self: LimitEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> Array:
        """
        Get: LogName(self: LimitEventLogCommand) -> Array[str]
        Set: LogName(self: LimitEventLogCommand) = value
        """
        ...

    @property
    def MaximumSize(self) -> Int64:
        """
        Get: MaximumSize(self: LimitEventLogCommand) -> Int64
        Set: MaximumSize(self: LimitEventLogCommand) = value
        """
        ...

    @property
    def OverflowAction(self) -> OverflowAction:
        """
        Get: OverflowAction(self: LimitEventLogCommand) -> OverflowAction
        Set: OverflowAction(self: LimitEventLogCommand) = value
        """
        ...

    @property
    def RetentionDays(self) -> int:
        """
        Get: RetentionDays(self: LimitEventLogCommand) -> int
        Set: RetentionDays(self: LimitEventLogCommand) = value
        """
        ...



class MatchInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ MatchInfo() """
    @property
    def Context(self): # -> MatchInfoContext
        """
        Get: Context(self: MatchInfo) -> MatchInfoContext
        Set: Context(self: MatchInfo) = value
        """
        ...

    @property
    def Filename(self) -> str:
        """ Get: Filename(self: MatchInfo) -> str """
        ...

    @property
    def IgnoreCase(self) -> bool:
        """
        Get: IgnoreCase(self: MatchInfo) -> bool
        Set: IgnoreCase(self: MatchInfo) = value
        """
        ...

    @property
    def Line(self) -> str:
        """
        Get: Line(self: MatchInfo) -> str
        Set: Line(self: MatchInfo) = value
        """
        ...

    @property
    def LineNumber(self) -> int:
        """
        Get: LineNumber(self: MatchInfo) -> int
        Set: LineNumber(self: MatchInfo) = value
        """
        ...

    @property
    def Matches(self) -> Array:
        """
        Get: Matches(self: MatchInfo) -> Array[Match]
        Set: Matches(self: MatchInfo) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: MatchInfo) -> str
        Set: Path(self: MatchInfo) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """
        Get: Pattern(self: MatchInfo) -> str
        Set: Pattern(self: MatchInfo) = value
        """
        ...


    def RelativePath(self, directory:str) -> str:
        """ RelativePath(self: MatchInfo, directory: str) -> str """
        ...

    def ToString(self, directory:str = ...) -> str:
        """
        ToString(self: MatchInfo) -> str
        ToString(self: MatchInfo, directory: str) -> str
        """
        ...


class MatchInfoContext(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayPostContext(self) -> Array:
        """
        Get: DisplayPostContext(self: MatchInfoContext) -> Array[str]
        Set: DisplayPostContext(self: MatchInfoContext) = value
        """
        ...

    @property
    def DisplayPreContext(self) -> Array:
        """
        Get: DisplayPreContext(self: MatchInfoContext) -> Array[str]
        Set: DisplayPreContext(self: MatchInfoContext) = value
        """
        ...

    @property
    def PostContext(self) -> Array:
        """
        Get: PostContext(self: MatchInfoContext) -> Array[str]
        Set: PostContext(self: MatchInfoContext) = value
        """
        ...

    @property
    def PreContext(self) -> Array:
        """
        Get: PreContext(self: MatchInfoContext) -> Array[str]
        Set: PreContext(self: MatchInfoContext) = value
        """
        ...



class MeasureCommandCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ MeasureCommandCommand() """
    @property
    def Expression(self) -> ScriptBlock:
        """
        Get: Expression(self: MeasureCommandCommand) -> ScriptBlock
        Set: Expression(self: MeasureCommandCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: MeasureCommandCommand) -> PSObject
        Set: InputObject(self: MeasureCommandCommand) = value
        """
        ...



class MeasureObjectCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ MeasureObjectCommand() """
    @property
    def Average(self) -> SwitchParameter:
        """
        Get: Average(self: MeasureObjectCommand) -> SwitchParameter
        Set: Average(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Character(self) -> SwitchParameter:
        """
        Get: Character(self: MeasureObjectCommand) -> SwitchParameter
        Set: Character(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def IgnoreWhiteSpace(self) -> SwitchParameter:
        """
        Get: IgnoreWhiteSpace(self: MeasureObjectCommand) -> SwitchParameter
        Set: IgnoreWhiteSpace(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: MeasureObjectCommand) -> PSObject
        Set: InputObject(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Line(self) -> SwitchParameter:
        """
        Get: Line(self: MeasureObjectCommand) -> SwitchParameter
        Set: Line(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Maximum(self) -> SwitchParameter:
        """
        Get: Maximum(self: MeasureObjectCommand) -> SwitchParameter
        Set: Maximum(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Minimum(self) -> SwitchParameter:
        """
        Get: Minimum(self: MeasureObjectCommand) -> SwitchParameter
        Set: Minimum(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: MeasureObjectCommand) -> Array[str]
        Set: Property(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Sum(self) -> SwitchParameter:
        """
        Get: Sum(self: MeasureObjectCommand) -> SwitchParameter
        Set: Sum(self: MeasureObjectCommand) = value
        """
        ...

    @property
    def Word(self) -> SwitchParameter:
        """
        Get: Word(self: MeasureObjectCommand) -> SwitchParameter
        Set: Word(self: MeasureObjectCommand) = value
        """
        ...



class MemberDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ MemberDefinition(typeName: str, name: str, memberType: PSMemberTypes, definition: str) """
    @property
    def Definition(self) -> str:
        """ Get: Definition(self: MemberDefinition) -> str """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """ Get: MemberType(self: MemberDefinition) -> PSMemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberDefinition) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MemberDefinition) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: MemberDefinition) -> str """
        ...


class ModuleSpecification: # skipped bases: <type 'object'>, <type 'object'>
    """
    ModuleSpecification()
    ModuleSpecification(moduleName: str)
    ModuleSpecification(moduleSpecification: Hashtable)
    """
    @property
    def Guid(self) -> Nullable:
        """ Get: Guid(self: ModuleSpecification) -> Nullable[Guid] """
        ...

    @property
    def MaximumVersion(self) -> str:
        """ Get: MaximumVersion(self: ModuleSpecification) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ModuleSpecification) -> str """
        ...

    @property
    def RequiredVersion(self) -> Version:
        """ Get: RequiredVersion(self: ModuleSpecification) -> Version """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: ModuleSpecification) -> Version """
        ...


    def ToString(self) -> str:
        """ ToString(self: ModuleSpecification) -> str """
        ...

    @staticmethod
    def TryParse(input, result) -> Tuple_[bool, ModuleSpecification]:
        """ TryParse(input: str) -> (bool, ModuleSpecification) """
        ...


class MoveItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ MoveItemCommand() """
    @property
    def Destination(self) -> str:
        """
        Get: Destination(self: MoveItemCommand) -> str
        Set: Destination(self: MoveItemCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: MoveItemCommand) -> Array[str]
        Set: Exclude(self: MoveItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: MoveItemCommand) -> str
        Set: Filter(self: MoveItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: MoveItemCommand) -> SwitchParameter
        Set: Force(self: MoveItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: MoveItemCommand) -> Array[str]
        Set: Include(self: MoveItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: MoveItemCommand) -> Array[str]
        Set: LiteralPath(self: MoveItemCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: MoveItemCommand) -> SwitchParameter
        Set: PassThru(self: MoveItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: MoveItemCommand) -> Array[str]
        Set: Path(self: MoveItemCommand) = value
        """
        ...



class MoveItemPropertyCommand(PassThroughItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ MoveItemPropertyCommand() """
    @property
    def Destination(self) -> str:
        """
        Get: Destination(self: MoveItemPropertyCommand) -> str
        Set: Destination(self: MoveItemPropertyCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: MoveItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: MoveItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: MoveItemPropertyCommand) -> Array[str]
        Set: Name(self: MoveItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: MoveItemPropertyCommand) -> Array[str]
        Set: Path(self: MoveItemPropertyCommand) = value
        """
        ...



class NetConnectionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetConnectionStatus, values: Authenticating (8), AuthenticationFailed (10), AuthenticationSucceeded (9), Connected (2), Connecting (1), CredentialsRequired (12), Disconnected (0), Disconnecting (3), HardwareDisabled (5), HardwareMalfunction (6), HardwareNotPresent (4), InvalidAddress (11), MediaDisconnected (7), Other (13) """
    Authenticating: NetConnectionStatus = ...
    AuthenticationFailed: NetConnectionStatus = ...
    AuthenticationSucceeded: NetConnectionStatus = ...
    Connected: NetConnectionStatus = ...
    Connecting: NetConnectionStatus = ...
    CredentialsRequired: NetConnectionStatus = ...
    Disconnected: NetConnectionStatus = ...
    Disconnecting: NetConnectionStatus = ...
    HardwareDisabled: NetConnectionStatus = ...
    HardwareMalfunction: NetConnectionStatus = ...
    HardwareNotPresent: NetConnectionStatus = ...
    InvalidAddress: NetConnectionStatus = ...
    MediaDisconnected: NetConnectionStatus = ...
    Other: NetConnectionStatus = ...
    value__ = ...


class NetworkAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ NetworkAdapter() """
    @property
    def ConnectionID(self) -> str:
        """ Get: ConnectionID(self: NetworkAdapter) -> str """
        ...

    @property
    def ConnectionStatus(self) -> NetConnectionStatus:
        """ Get: ConnectionStatus(self: NetworkAdapter) -> NetConnectionStatus """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: NetworkAdapter) -> str """
        ...

    @property
    def DHCPEnabled(self) -> Nullable:
        """ Get: DHCPEnabled(self: NetworkAdapter) -> Nullable[bool] """
        ...

    @property
    def DHCPServer(self) -> str:
        """ Get: DHCPServer(self: NetworkAdapter) -> str """
        ...

    @property
    def IPAddresses(self) -> Array:
        """ Get: IPAddresses(self: NetworkAdapter) -> Array[str] """
        ...



class WriteAliasCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteAliasCommandBase() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: WriteAliasCommandBase) -> str
        Set: Description(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: WriteAliasCommandBase) -> SwitchParameter
        Set: Force(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WriteAliasCommandBase) -> str
        Set: Name(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def Option(self) -> ScopedItemOptions:
        """
        Get: Option(self: WriteAliasCommandBase) -> ScopedItemOptions
        Set: Option(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: WriteAliasCommandBase) -> SwitchParameter
        Set: PassThru(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: WriteAliasCommandBase) -> str
        Set: Scope(self: WriteAliasCommandBase) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: WriteAliasCommandBase) -> str
        Set: Value(self: WriteAliasCommandBase) = value
        """
        ...



class NewAliasCommand(WriteAliasCommandBase): # skipped bases: <type 'object'>
    """ NewAliasCommand() """
    pass

class NewEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewEventCommand() """
    @property
    def EventArguments(self) -> Array:
        """
        Get: EventArguments(self: NewEventCommand) -> Array[PSObject]
        Set: EventArguments(self: NewEventCommand) = value
        """
        ...

    @property
    def MessageData(self) -> PSObject:
        """
        Get: MessageData(self: NewEventCommand) -> PSObject
        Set: MessageData(self: NewEventCommand) = value
        """
        ...

    @property
    def Sender(self) -> PSObject:
        """
        Get: Sender(self: NewEventCommand) -> PSObject
        Set: Sender(self: NewEventCommand) = value
        """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: NewEventCommand) -> str
        Set: SourceIdentifier(self: NewEventCommand) = value
        """
        ...



class NewEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewEventLogCommand() """
    @property
    def CategoryResourceFile(self) -> str:
        """
        Get: CategoryResourceFile(self: NewEventLogCommand) -> str
        Set: CategoryResourceFile(self: NewEventLogCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: NewEventLogCommand) -> Array[str]
        Set: ComputerName(self: NewEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> str:
        """
        Get: LogName(self: NewEventLogCommand) -> str
        Set: LogName(self: NewEventLogCommand) = value
        """
        ...

    @property
    def MessageResourceFile(self) -> str:
        """
        Get: MessageResourceFile(self: NewEventLogCommand) -> str
        Set: MessageResourceFile(self: NewEventLogCommand) = value
        """
        ...

    @property
    def ParameterResourceFile(self) -> str:
        """
        Get: ParameterResourceFile(self: NewEventLogCommand) -> str
        Set: ParameterResourceFile(self: NewEventLogCommand) = value
        """
        ...

    @property
    def Source(self) -> Array:
        """
        Get: Source(self: NewEventLogCommand) -> Array[str]
        Set: Source(self: NewEventLogCommand) = value
        """
        ...



class NewFileCatalogCommand(CatalogCommandsBase): # skipped bases: <type 'object'>
    """ NewFileCatalogCommand() """
    @property
    def CatalogVersion(self) -> int:
        """
        Get: CatalogVersion(self: NewFileCatalogCommand) -> int
        Set: CatalogVersion(self: NewFileCatalogCommand) = value
        """
        ...



class NewItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ NewItemCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: NewItemCommand) -> SwitchParameter
        Set: Force(self: NewItemCommand) = value
        """
        ...

    @property
    def ItemType(self) -> str:
        """
        Get: ItemType(self: NewItemCommand) -> str
        Set: ItemType(self: NewItemCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewItemCommand) -> str
        Set: Name(self: NewItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: NewItemCommand) -> Array[str]
        Set: Path(self: NewItemCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: NewItemCommand) -> object
        Set: Value(self: NewItemCommand) = value
        """
        ...



class NewItemPropertyCommand(ItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ NewItemPropertyCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: NewItemPropertyCommand) -> SwitchParameter
        Set: Force(self: NewItemPropertyCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: NewItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: NewItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewItemPropertyCommand) -> str
        Set: Name(self: NewItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: NewItemPropertyCommand) -> Array[str]
        Set: Path(self: NewItemPropertyCommand) = value
        """
        ...

    @property
    def PropertyType(self) -> str:
        """
        Get: PropertyType(self: NewItemPropertyCommand) -> str
        Set: PropertyType(self: NewItemPropertyCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: NewItemPropertyCommand) -> object
        Set: Value(self: NewItemPropertyCommand) = value
        """
        ...



class NewModuleCommand(ModuleCmdletBase): # skipped bases: <type 'object'>
    """ NewModuleCommand() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: NewModuleCommand) -> Array[object]
        Set: ArgumentList(self: NewModuleCommand) = value
        """
        ...

    @property
    def AsCustomObject(self) -> SwitchParameter:
        """
        Get: AsCustomObject(self: NewModuleCommand) -> SwitchParameter
        Set: AsCustomObject(self: NewModuleCommand) = value
        """
        ...

    @property
    def Cmdlet(self) -> Array:
        """
        Get: Cmdlet(self: NewModuleCommand) -> Array[str]
        Set: Cmdlet(self: NewModuleCommand) = value
        """
        ...

    @property
    def Function(self) -> Array:
        """
        Get: Function(self: NewModuleCommand) -> Array[str]
        Set: Function(self: NewModuleCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewModuleCommand) -> str
        Set: Name(self: NewModuleCommand) = value
        """
        ...

    @property
    def ReturnResult(self) -> SwitchParameter:
        """
        Get: ReturnResult(self: NewModuleCommand) -> SwitchParameter
        Set: ReturnResult(self: NewModuleCommand) = value
        """
        ...

    @property
    def ScriptBlock(self) -> ScriptBlock:
        """
        Get: ScriptBlock(self: NewModuleCommand) -> ScriptBlock
        Set: ScriptBlock(self: NewModuleCommand) = value
        """
        ...



class NewModuleManifestCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewModuleManifestCommand() """
    @property
    def AliasesToExport(self) -> Array:
        """
        Get: AliasesToExport(self: NewModuleManifestCommand) -> Array[str]
        Set: AliasesToExport(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Author(self) -> str:
        """
        Get: Author(self: NewModuleManifestCommand) -> str
        Set: Author(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ClrVersion(self) -> Version:
        """
        Get: ClrVersion(self: NewModuleManifestCommand) -> Version
        Set: ClrVersion(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def CmdletsToExport(self) -> Array:
        """
        Get: CmdletsToExport(self: NewModuleManifestCommand) -> Array[str]
        Set: CmdletsToExport(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def CompanyName(self) -> str:
        """
        Get: CompanyName(self: NewModuleManifestCommand) -> str
        Set: CompanyName(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def CompatiblePSEditions(self) -> Array:
        """
        Get: CompatiblePSEditions(self: NewModuleManifestCommand) -> Array[str]
        Set: CompatiblePSEditions(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Copyright(self) -> str:
        """
        Get: Copyright(self: NewModuleManifestCommand) -> str
        Set: Copyright(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def DefaultCommandPrefix(self) -> str:
        """
        Get: DefaultCommandPrefix(self: NewModuleManifestCommand) -> str
        Set: DefaultCommandPrefix(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewModuleManifestCommand) -> str
        Set: Description(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def DotNetFrameworkVersion(self) -> Version:
        """
        Get: DotNetFrameworkVersion(self: NewModuleManifestCommand) -> Version
        Set: DotNetFrameworkVersion(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def DscResourcesToExport(self) -> Array:
        """
        Get: DscResourcesToExport(self: NewModuleManifestCommand) -> Array[str]
        Set: DscResourcesToExport(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def FileList(self) -> Array:
        """
        Get: FileList(self: NewModuleManifestCommand) -> Array[str]
        Set: FileList(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def FormatsToProcess(self) -> Array:
        """
        Get: FormatsToProcess(self: NewModuleManifestCommand) -> Array[str]
        Set: FormatsToProcess(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def FunctionsToExport(self) -> Array:
        """
        Get: FunctionsToExport(self: NewModuleManifestCommand) -> Array[str]
        Set: FunctionsToExport(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Get: Guid(self: NewModuleManifestCommand) -> Guid
        Set: Guid(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def HelpInfoUri(self) -> str:
        """
        Get: HelpInfoUri(self: NewModuleManifestCommand) -> str
        Set: HelpInfoUri(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def IconUri(self) -> Uri:
        """
        Get: IconUri(self: NewModuleManifestCommand) -> Uri
        Set: IconUri(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def LicenseUri(self) -> Uri:
        """
        Get: LicenseUri(self: NewModuleManifestCommand) -> Uri
        Set: LicenseUri(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ModuleList(self) -> Array:
        """
        Get: ModuleList(self: NewModuleManifestCommand) -> Array[object]
        Set: ModuleList(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ModuleVersion(self) -> Version:
        """
        Get: ModuleVersion(self: NewModuleManifestCommand) -> Version
        Set: ModuleVersion(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def NestedModules(self) -> Array:
        """
        Get: NestedModules(self: NewModuleManifestCommand) -> Array[object]
        Set: NestedModules(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: NewModuleManifestCommand) -> SwitchParameter
        Set: PassThru(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: NewModuleManifestCommand) -> str
        Set: Path(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def PowerShellHostName(self) -> str:
        """
        Get: PowerShellHostName(self: NewModuleManifestCommand) -> str
        Set: PowerShellHostName(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def PowerShellHostVersion(self) -> Version:
        """
        Get: PowerShellHostVersion(self: NewModuleManifestCommand) -> Version
        Set: PowerShellHostVersion(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def PowerShellVersion(self) -> Version:
        """
        Get: PowerShellVersion(self: NewModuleManifestCommand) -> Version
        Set: PowerShellVersion(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def PrivateData(self) -> object:
        """
        Get: PrivateData(self: NewModuleManifestCommand) -> object
        Set: PrivateData(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """
        Get: ProcessorArchitecture(self: NewModuleManifestCommand) -> ProcessorArchitecture
        Set: ProcessorArchitecture(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ProjectUri(self) -> Uri:
        """
        Get: ProjectUri(self: NewModuleManifestCommand) -> Uri
        Set: ProjectUri(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ReleaseNotes(self) -> str:
        """
        Get: ReleaseNotes(self: NewModuleManifestCommand) -> str
        Set: ReleaseNotes(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def RequiredAssemblies(self) -> Array:
        """
        Get: RequiredAssemblies(self: NewModuleManifestCommand) -> Array[str]
        Set: RequiredAssemblies(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def RequiredModules(self) -> Array:
        """
        Get: RequiredModules(self: NewModuleManifestCommand) -> Array[object]
        Set: RequiredModules(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def RootModule(self) -> str:
        """
        Get: RootModule(self: NewModuleManifestCommand) -> str
        Set: RootModule(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def ScriptsToProcess(self) -> Array:
        """
        Get: ScriptsToProcess(self: NewModuleManifestCommand) -> Array[str]
        Set: ScriptsToProcess(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def Tags(self) -> Array:
        """
        Get: Tags(self: NewModuleManifestCommand) -> Array[str]
        Set: Tags(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def TypesToProcess(self) -> Array:
        """
        Get: TypesToProcess(self: NewModuleManifestCommand) -> Array[str]
        Set: TypesToProcess(self: NewModuleManifestCommand) = value
        """
        ...

    @property
    def VariablesToExport(self) -> Array:
        """
        Get: VariablesToExport(self: NewModuleManifestCommand) -> Array[str]
        Set: VariablesToExport(self: NewModuleManifestCommand) = value
        """
        ...



class NewObjectCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewObjectCommand() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: NewObjectCommand) -> Array[object]
        Set: ArgumentList(self: NewObjectCommand) = value
        """
        ...

    @property
    def ComObject(self) -> str:
        """
        Get: ComObject(self: NewObjectCommand) -> str
        Set: ComObject(self: NewObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> IDictionary:
        """
        Get: Property(self: NewObjectCommand) -> IDictionary
        Set: Property(self: NewObjectCommand) = value
        """
        ...

    @property
    def Strict(self) -> SwitchParameter:
        """
        Get: Strict(self: NewObjectCommand) -> SwitchParameter
        Set: Strict(self: NewObjectCommand) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: NewObjectCommand) -> str
        Set: TypeName(self: NewObjectCommand) = value
        """
        ...



class NewPSDriveCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ NewPSDriveCommand() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewPSDriveCommand) -> str
        Set: Description(self: NewPSDriveCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewPSDriveCommand) -> str
        Set: Name(self: NewPSDriveCommand) = value
        """
        ...

    @property
    def Persist(self) -> SwitchParameter:
        """
        Get: Persist(self: NewPSDriveCommand) -> SwitchParameter
        Set: Persist(self: NewPSDriveCommand) = value
        """
        ...

    @property
    def PSProvider(self) -> str:
        """
        Get: PSProvider(self: NewPSDriveCommand) -> str
        Set: PSProvider(self: NewPSDriveCommand) = value
        """
        ...

    @property
    def Root(self) -> str:
        """
        Get: Root(self: NewPSDriveCommand) -> str
        Set: Root(self: NewPSDriveCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: NewPSDriveCommand) -> str
        Set: Scope(self: NewPSDriveCommand) = value
        """
        ...



class NewPSRoleCapabilityFileCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewPSRoleCapabilityFileCommand() """
    @property
    def AliasDefinitions(self) -> Array:
        """
        Get: AliasDefinitions(self: NewPSRoleCapabilityFileCommand) -> Array[IDictionary]
        Set: AliasDefinitions(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def AssembliesToLoad(self) -> Array:
        """
        Get: AssembliesToLoad(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: AssembliesToLoad(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def Author(self) -> str:
        """
        Get: Author(self: NewPSRoleCapabilityFileCommand) -> str
        Set: Author(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def CompanyName(self) -> str:
        """
        Get: CompanyName(self: NewPSRoleCapabilityFileCommand) -> str
        Set: CompanyName(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def Copyright(self) -> str:
        """
        Get: Copyright(self: NewPSRoleCapabilityFileCommand) -> str
        Set: Copyright(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewPSRoleCapabilityFileCommand) -> str
        Set: Description(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def EnvironmentVariables(self) -> IDictionary:
        """
        Get: EnvironmentVariables(self: NewPSRoleCapabilityFileCommand) -> IDictionary
        Set: EnvironmentVariables(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def FormatsToProcess(self) -> Array:
        """
        Get: FormatsToProcess(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: FormatsToProcess(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def FunctionDefinitions(self) -> Array:
        """
        Get: FunctionDefinitions(self: NewPSRoleCapabilityFileCommand) -> Array[IDictionary]
        Set: FunctionDefinitions(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Get: Guid(self: NewPSRoleCapabilityFileCommand) -> Guid
        Set: Guid(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def ModulesToImport(self) -> Array:
        """
        Get: ModulesToImport(self: NewPSRoleCapabilityFileCommand) -> Array[object]
        Set: ModulesToImport(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: NewPSRoleCapabilityFileCommand) -> str
        Set: Path(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def ScriptsToProcess(self) -> Array:
        """
        Get: ScriptsToProcess(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: ScriptsToProcess(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def TypesToProcess(self) -> Array:
        """
        Get: TypesToProcess(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: TypesToProcess(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VariableDefinitions(self) -> object:
        """
        Get: VariableDefinitions(self: NewPSRoleCapabilityFileCommand) -> object
        Set: VariableDefinitions(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VisibleAliases(self) -> Array:
        """
        Get: VisibleAliases(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: VisibleAliases(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VisibleCmdlets(self) -> Array:
        """
        Get: VisibleCmdlets(self: NewPSRoleCapabilityFileCommand) -> Array[object]
        Set: VisibleCmdlets(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VisibleExternalCommands(self) -> Array:
        """
        Get: VisibleExternalCommands(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: VisibleExternalCommands(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VisibleFunctions(self) -> Array:
        """
        Get: VisibleFunctions(self: NewPSRoleCapabilityFileCommand) -> Array[object]
        Set: VisibleFunctions(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...

    @property
    def VisibleProviders(self) -> Array:
        """
        Get: VisibleProviders(self: NewPSRoleCapabilityFileCommand) -> Array[str]
        Set: VisibleProviders(self: NewPSRoleCapabilityFileCommand) = value
        """
        ...



class NewPSSessionCommand(IDisposable, PSRemotingBaseCmdlet): # skipped bases: <type 'object'>
    """ NewPSSessionCommand() """
    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: NewPSSessionCommand) -> str
        Set: ConfigurationName(self: NewPSSessionCommand) = value
        """
        ...

    @property
    def EnableNetworkAccess(self) -> SwitchParameter:
        """
        Get: EnableNetworkAccess(self: NewPSSessionCommand) -> SwitchParameter
        Set: EnableNetworkAccess(self: NewPSSessionCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: NewPSSessionCommand) -> Array[str]
        Set: Name(self: NewPSSessionCommand) = value
        """
        ...



class NewPSSessionConfigurationFileCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewPSSessionConfigurationFileCommand() """
    @property
    def AliasDefinitions(self) -> Array:
        """
        Get: AliasDefinitions(self: NewPSSessionConfigurationFileCommand) -> Array[IDictionary]
        Set: AliasDefinitions(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def AssembliesToLoad(self) -> Array:
        """
        Get: AssembliesToLoad(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: AssembliesToLoad(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Author(self) -> str:
        """
        Get: Author(self: NewPSSessionConfigurationFileCommand) -> str
        Set: Author(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def CompanyName(self) -> str:
        """
        Get: CompanyName(self: NewPSSessionConfigurationFileCommand) -> str
        Set: CompanyName(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Copyright(self) -> str:
        """
        Get: Copyright(self: NewPSSessionConfigurationFileCommand) -> str
        Set: Copyright(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewPSSessionConfigurationFileCommand) -> str
        Set: Description(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def EnvironmentVariables(self) -> IDictionary:
        """
        Get: EnvironmentVariables(self: NewPSSessionConfigurationFileCommand) -> IDictionary
        Set: EnvironmentVariables(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def ExecutionPolicy(self) -> ExecutionPolicy:
        """
        Get: ExecutionPolicy(self: NewPSSessionConfigurationFileCommand) -> ExecutionPolicy
        Set: ExecutionPolicy(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def FormatsToProcess(self) -> Array:
        """
        Get: FormatsToProcess(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: FormatsToProcess(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Full(self) -> SwitchParameter:
        """
        Get: Full(self: NewPSSessionConfigurationFileCommand) -> SwitchParameter
        Set: Full(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def FunctionDefinitions(self) -> Array:
        """
        Get: FunctionDefinitions(self: NewPSSessionConfigurationFileCommand) -> Array[IDictionary]
        Set: FunctionDefinitions(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def GroupManagedServiceAccount(self) -> str:
        """
        Get: GroupManagedServiceAccount(self: NewPSSessionConfigurationFileCommand) -> str
        Set: GroupManagedServiceAccount(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Get: Guid(self: NewPSSessionConfigurationFileCommand) -> Guid
        Set: Guid(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def LanguageMode(self) -> PSLanguageMode:
        """
        Get: LanguageMode(self: NewPSSessionConfigurationFileCommand) -> PSLanguageMode
        Set: LanguageMode(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def ModulesToImport(self) -> Array:
        """
        Get: ModulesToImport(self: NewPSSessionConfigurationFileCommand) -> Array[object]
        Set: ModulesToImport(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def MountUserDrive(self) -> SwitchParameter:
        """
        Get: MountUserDrive(self: NewPSSessionConfigurationFileCommand) -> SwitchParameter
        Set: MountUserDrive(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: NewPSSessionConfigurationFileCommand) -> str
        Set: Path(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def PowerShellVersion(self) -> Version:
        """
        Get: PowerShellVersion(self: NewPSSessionConfigurationFileCommand) -> Version
        Set: PowerShellVersion(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def RequiredGroups(self) -> IDictionary:
        """
        Get: RequiredGroups(self: NewPSSessionConfigurationFileCommand) -> IDictionary
        Set: RequiredGroups(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def RoleDefinitions(self) -> IDictionary:
        """
        Get: RoleDefinitions(self: NewPSSessionConfigurationFileCommand) -> IDictionary
        Set: RoleDefinitions(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def RunAsVirtualAccount(self) -> SwitchParameter:
        """
        Get: RunAsVirtualAccount(self: NewPSSessionConfigurationFileCommand) -> SwitchParameter
        Set: RunAsVirtualAccount(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def RunAsVirtualAccountGroups(self) -> Array:
        """
        Get: RunAsVirtualAccountGroups(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: RunAsVirtualAccountGroups(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def SchemaVersion(self) -> Version:
        """
        Get: SchemaVersion(self: NewPSSessionConfigurationFileCommand) -> Version
        Set: SchemaVersion(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def ScriptsToProcess(self) -> Array:
        """
        Get: ScriptsToProcess(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: ScriptsToProcess(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def SessionType(self) -> SessionType:
        """
        Get: SessionType(self: NewPSSessionConfigurationFileCommand) -> SessionType
        Set: SessionType(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def TranscriptDirectory(self) -> str:
        """
        Get: TranscriptDirectory(self: NewPSSessionConfigurationFileCommand) -> str
        Set: TranscriptDirectory(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def TypesToProcess(self) -> Array:
        """
        Get: TypesToProcess(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: TypesToProcess(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def UserDriveMaximumSize(self) -> Int64:
        """
        Get: UserDriveMaximumSize(self: NewPSSessionConfigurationFileCommand) -> Int64
        Set: UserDriveMaximumSize(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VariableDefinitions(self) -> object:
        """
        Get: VariableDefinitions(self: NewPSSessionConfigurationFileCommand) -> object
        Set: VariableDefinitions(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VisibleAliases(self) -> Array:
        """
        Get: VisibleAliases(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: VisibleAliases(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VisibleCmdlets(self) -> Array:
        """
        Get: VisibleCmdlets(self: NewPSSessionConfigurationFileCommand) -> Array[object]
        Set: VisibleCmdlets(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VisibleExternalCommands(self) -> Array:
        """
        Get: VisibleExternalCommands(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: VisibleExternalCommands(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VisibleFunctions(self) -> Array:
        """
        Get: VisibleFunctions(self: NewPSSessionConfigurationFileCommand) -> Array[object]
        Set: VisibleFunctions(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...

    @property
    def VisibleProviders(self) -> Array:
        """
        Get: VisibleProviders(self: NewPSSessionConfigurationFileCommand) -> Array[str]
        Set: VisibleProviders(self: NewPSSessionConfigurationFileCommand) = value
        """
        ...



class NewPSSessionOptionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewPSSessionOptionCommand() """
    @property
    def ApplicationArguments(self) -> PSPrimitiveDictionary:
        """
        Get: ApplicationArguments(self: NewPSSessionOptionCommand) -> PSPrimitiveDictionary
        Set: ApplicationArguments(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def CancelTimeout(self) -> int:
        """
        Get: CancelTimeout(self: NewPSSessionOptionCommand) -> int
        Set: CancelTimeout(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """
        Get: Culture(self: NewPSSessionOptionCommand) -> CultureInfo
        Set: Culture(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def IdleTimeout(self) -> int:
        """
        Get: IdleTimeout(self: NewPSSessionOptionCommand) -> int
        Set: IdleTimeout(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def IncludePortInSPN(self) -> SwitchParameter:
        """
        Get: IncludePortInSPN(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: IncludePortInSPN(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def MaxConnectionRetryCount(self) -> int:
        """
        Get: MaxConnectionRetryCount(self: NewPSSessionOptionCommand) -> int
        Set: MaxConnectionRetryCount(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def MaximumReceivedDataSizePerCommand(self) -> int:
        """
        Get: MaximumReceivedDataSizePerCommand(self: NewPSSessionOptionCommand) -> int
        Set: MaximumReceivedDataSizePerCommand(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def MaximumReceivedObjectSize(self) -> int:
        """
        Get: MaximumReceivedObjectSize(self: NewPSSessionOptionCommand) -> int
        Set: MaximumReceivedObjectSize(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def MaximumRedirection(self) -> int:
        """
        Get: MaximumRedirection(self: NewPSSessionOptionCommand) -> int
        Set: MaximumRedirection(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def NoCompression(self) -> SwitchParameter:
        """
        Get: NoCompression(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: NoCompression(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def NoEncryption(self) -> SwitchParameter:
        """
        Get: NoEncryption(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: NoEncryption(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def NoMachineProfile(self) -> SwitchParameter:
        """
        Get: NoMachineProfile(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: NoMachineProfile(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def OpenTimeout(self) -> int:
        """
        Get: OpenTimeout(self: NewPSSessionOptionCommand) -> int
        Set: OpenTimeout(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def OperationTimeout(self) -> int:
        """
        Get: OperationTimeout(self: NewPSSessionOptionCommand) -> int
        Set: OperationTimeout(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def OutputBufferingMode(self) -> OutputBufferingMode:
        """
        Get: OutputBufferingMode(self: NewPSSessionOptionCommand) -> OutputBufferingMode
        Set: OutputBufferingMode(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyAccessType(self) -> ProxyAccessType:
        """
        Get: ProxyAccessType(self: NewPSSessionOptionCommand) -> ProxyAccessType
        Set: ProxyAccessType(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyAuthentication(self) -> AuthenticationMechanism:
        """
        Get: ProxyAuthentication(self: NewPSSessionOptionCommand) -> AuthenticationMechanism
        Set: ProxyAuthentication(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyCredential(self) -> PSCredential:
        """
        Get: ProxyCredential(self: NewPSSessionOptionCommand) -> PSCredential
        Set: ProxyCredential(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def SkipCACheck(self) -> SwitchParameter:
        """
        Get: SkipCACheck(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: SkipCACheck(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def SkipCNCheck(self) -> SwitchParameter:
        """
        Get: SkipCNCheck(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: SkipCNCheck(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def SkipRevocationCheck(self) -> SwitchParameter:
        """
        Get: SkipRevocationCheck(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: SkipRevocationCheck(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def UICulture(self) -> CultureInfo:
        """
        Get: UICulture(self: NewPSSessionOptionCommand) -> CultureInfo
        Set: UICulture(self: NewPSSessionOptionCommand) = value
        """
        ...

    @property
    def UseUTF16(self) -> SwitchParameter:
        """
        Get: UseUTF16(self: NewPSSessionOptionCommand) -> SwitchParameter
        Set: UseUTF16(self: NewPSSessionOptionCommand) = value
        """
        ...



class NewPSTransportOptionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewPSTransportOptionCommand() """
    @property
    def IdleTimeoutSec(self) -> Nullable:
        """
        Get: IdleTimeoutSec(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: IdleTimeoutSec(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxConcurrentCommandsPerSession(self) -> Nullable:
        """
        Get: MaxConcurrentCommandsPerSession(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxConcurrentCommandsPerSession(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxConcurrentUsers(self) -> Nullable:
        """
        Get: MaxConcurrentUsers(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxConcurrentUsers(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxIdleTimeoutSec(self) -> Nullable:
        """
        Get: MaxIdleTimeoutSec(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxIdleTimeoutSec(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxMemoryPerSessionMB(self) -> Nullable:
        """
        Get: MaxMemoryPerSessionMB(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxMemoryPerSessionMB(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxProcessesPerSession(self) -> Nullable:
        """
        Get: MaxProcessesPerSession(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxProcessesPerSession(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxSessions(self) -> Nullable:
        """
        Get: MaxSessions(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxSessions(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def MaxSessionsPerUser(self) -> Nullable:
        """
        Get: MaxSessionsPerUser(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: MaxSessionsPerUser(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def OutputBufferingMode(self) -> Nullable:
        """
        Get: OutputBufferingMode(self: NewPSTransportOptionCommand) -> Nullable[OutputBufferingMode]
        Set: OutputBufferingMode(self: NewPSTransportOptionCommand) = value
        """
        ...

    @property
    def ProcessIdleTimeoutSec(self) -> Nullable:
        """
        Get: ProcessIdleTimeoutSec(self: NewPSTransportOptionCommand) -> Nullable[int]
        Set: ProcessIdleTimeoutSec(self: NewPSTransportOptionCommand) = value
        """
        ...



class NewServiceCommand(ServiceBaseCommand): # skipped bases: <type 'object'>
    """ NewServiceCommand() """
    @property
    def BinaryPathName(self) -> str:
        """
        Get: BinaryPathName(self: NewServiceCommand) -> str
        Set: BinaryPathName(self: NewServiceCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: NewServiceCommand) -> PSCredential
        Set: Credential(self: NewServiceCommand) = value
        """
        ...

    @property
    def DependsOn(self) -> Array:
        """
        Get: DependsOn(self: NewServiceCommand) -> Array[str]
        Set: DependsOn(self: NewServiceCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewServiceCommand) -> str
        Set: Description(self: NewServiceCommand) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: NewServiceCommand) -> str
        Set: DisplayName(self: NewServiceCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewServiceCommand) -> str
        Set: Name(self: NewServiceCommand) = value
        """
        ...

    @property
    def StartupType(self) -> ServiceStartMode:
        """
        Get: StartupType(self: NewServiceCommand) -> ServiceStartMode
        Set: StartupType(self: NewServiceCommand) = value
        """
        ...



class NewTimeSpanCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewTimeSpanCommand() """
    @property
    def Days(self) -> int:
        """
        Get: Days(self: NewTimeSpanCommand) -> int
        Set: Days(self: NewTimeSpanCommand) = value
        """
        ...

    @property
    def End(self) -> DateTime:
        """
        Get: End(self: NewTimeSpanCommand) -> DateTime
        Set: End(self: NewTimeSpanCommand) = value
        """
        ...

    @property
    def Hours(self) -> int:
        """
        Get: Hours(self: NewTimeSpanCommand) -> int
        Set: Hours(self: NewTimeSpanCommand) = value
        """
        ...

    @property
    def Minutes(self) -> int:
        """
        Get: Minutes(self: NewTimeSpanCommand) -> int
        Set: Minutes(self: NewTimeSpanCommand) = value
        """
        ...

    @property
    def Seconds(self) -> int:
        """
        Get: Seconds(self: NewTimeSpanCommand) -> int
        Set: Seconds(self: NewTimeSpanCommand) = value
        """
        ...

    @property
    def Start(self) -> DateTime:
        """
        Get: Start(self: NewTimeSpanCommand) -> DateTime
        Set: Start(self: NewTimeSpanCommand) = value
        """
        ...



class NewVariableCommand(VariableCommandBase): # skipped bases: <type 'object'>
    """ NewVariableCommand() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: NewVariableCommand) -> str
        Set: Description(self: NewVariableCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: NewVariableCommand) -> SwitchParameter
        Set: Force(self: NewVariableCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: NewVariableCommand) -> str
        Set: Name(self: NewVariableCommand) = value
        """
        ...

    @property
    def Option(self) -> ScopedItemOptions:
        """
        Get: Option(self: NewVariableCommand) -> ScopedItemOptions
        Set: Option(self: NewVariableCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: NewVariableCommand) -> SwitchParameter
        Set: PassThru(self: NewVariableCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: NewVariableCommand) -> object
        Set: Value(self: NewVariableCommand) = value
        """
        ...

    @property
    def Visibility(self) -> SessionStateEntryVisibility:
        """
        Get: Visibility(self: NewVariableCommand) -> SessionStateEntryVisibility
        Set: Visibility(self: NewVariableCommand) = value
        """
        ...



class NewWebServiceProxy(PSCmdlet): # skipped bases: <type 'object'>
    """ NewWebServiceProxy() """
    @property
    def Class(self) -> str:
        """
        Get: Class(self: NewWebServiceProxy) -> str
        Set: Class(self: NewWebServiceProxy) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: NewWebServiceProxy) -> PSCredential
        Set: Credential(self: NewWebServiceProxy) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: NewWebServiceProxy) -> str
        Set: Namespace(self: NewWebServiceProxy) = value
        """
        ...

    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: NewWebServiceProxy) -> Uri
        Set: Uri(self: NewWebServiceProxy) = value
        """
        ...

    @property
    def UseDefaultCredential(self) -> SwitchParameter:
        """
        Get: UseDefaultCredential(self: NewWebServiceProxy) -> SwitchParameter
        Set: UseDefaultCredential(self: NewWebServiceProxy) = value
        """
        ...



class NewWinEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewWinEventCommand() """
    @property
    def Id(self) -> int:
        """
        Get: Id(self: NewWinEventCommand) -> int
        Set: Id(self: NewWinEventCommand) = value
        """
        ...

    @property
    def Payload(self) -> Array:
        """
        Get: Payload(self: NewWinEventCommand) -> Array[object]
        Set: Payload(self: NewWinEventCommand) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: NewWinEventCommand) -> str
        Set: ProviderName(self: NewWinEventCommand) = value
        """
        ...

    @property
    def Version(self) -> Byte:
        """
        Get: Version(self: NewWinEventCommand) -> Byte
        Set: Version(self: NewWinEventCommand) = value
        """
        ...



class NounArgumentCompleter(IArgumentCompleter): # skipped bases: <type 'object'>
    """ NounArgumentCompleter() """
    pass

class ObjectEventRegistrationBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> ScriptBlock:
        """
        Get: Action(self: ObjectEventRegistrationBase) -> ScriptBlock
        Set: Action(self: ObjectEventRegistrationBase) = value
        """
        ...

    @property
    def Forward(self) -> SwitchParameter:
        """
        Get: Forward(self: ObjectEventRegistrationBase) -> SwitchParameter
        Set: Forward(self: ObjectEventRegistrationBase) = value
        """
        ...

    @property
    def MaxTriggerCount(self) -> int:
        """
        Get: MaxTriggerCount(self: ObjectEventRegistrationBase) -> int
        Set: MaxTriggerCount(self: ObjectEventRegistrationBase) = value
        """
        ...

    @property
    def MessageData(self) -> PSObject:
        """
        Get: MessageData(self: ObjectEventRegistrationBase) -> PSObject
        Set: MessageData(self: ObjectEventRegistrationBase) = value
        """
        ...

    @property
    def NewSubscriber(self):
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: ObjectEventRegistrationBase) -> str
        Set: SourceIdentifier(self: ObjectEventRegistrationBase) = value
        """
        ...

    @property
    def SupportEvent(self) -> SwitchParameter:
        """
        Get: SupportEvent(self: ObjectEventRegistrationBase) -> SwitchParameter
        Set: SupportEvent(self: ObjectEventRegistrationBase) = value
        """
        ...


    def GetSourceObject(self, *args): #cannot find CLR method
        """ GetSourceObject(self: ObjectEventRegistrationBase) -> object """
        ...

    def GetSourceObjectEventName(self, *args): #cannot find CLR method
        """ GetSourceObjectEventName(self: ObjectEventRegistrationBase) -> str """
        ...


class OpenMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenMode, values: Add (0), New (1), Overwrite (2) """
    Add: OpenMode = ...
    New: OpenMode = ...
    Overwrite: OpenMode = ...
    value__ = ...


class OperatingSystemSKU(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperatingSystemSKU, values: BusinessEdition (6), BusinessNEdition (16), ClusterServerEdition (18), DatacenterServerCoreEdition (12), DatacenterServerEdition (8), EnterpriseEdition (4), EnterpriseServerCoreEdition (14), EnterpriseServerEdition (10), EnterpriseServerIA64Edition (15), HomeBasicEdition (2), HomeBasicNEdition (5), HomePremiumEdition (3), HomeServerEdition (19), MicrosoftHyperVServer (42), ServerForSmallBusinessEdition (24), ServerFoundation (33), SmallBusinessServerEdition (9), SmallBusinessServerPremiumCore (63), SmallBusinessServerPremiumEdition (25), StandardServerCoreEdition (13), StandardServerEdition (7), StarterEdition (11), StorageEnterpriseServerEdition (23), StorageExpressServerEdition (20), StorageServerEnterpriseCore (46), StorageServerExpressCore (43), StorageServerStandardCore (44), StorageServerWorkgroupCore (45), StorageStandardServerEdition (21), StorageWorkgroupServerEdition (22), TBD (26), UltimateEdition (1), Undefined (0), WebServerCore (29), WebServerEdition (17), WindowsEmbeddedHandheld (118), WindowsEmbeddedIndustry (89), WindowsEnterprise (27), WindowsHome (101), WindowsHomeServer (34), WindowsIotCore (123), WindowsMobile (104), WindowsProfessionalWithMediaCenter (103), WindowsRT (97), WindowsServerDatacenterNoHyperVCore (39), WindowsServerDatacenterNoHyperVFull (37), WindowsServerEnterpriseNoHyperVCore (41), WindowsServerEnterpriseNoHyperVFull (38), WindowsServerHyperCoreV (64), WindowsServerStandardNoHyperVCore (40), WindowsServerStandardNoHyperVFull (36), WindowsSmallBusinessServer2011Essentials (50), WindowsThinPC (87), WindowsUltimate (28) """
    BusinessEdition: OperatingSystemSKU = ...
    BusinessNEdition: OperatingSystemSKU = ...
    ClusterServerEdition: OperatingSystemSKU = ...
    DatacenterServerCoreEdition: OperatingSystemSKU = ...
    DatacenterServerEdition: OperatingSystemSKU = ...
    EnterpriseEdition: OperatingSystemSKU = ...
    EnterpriseServerCoreEdition: OperatingSystemSKU = ...
    EnterpriseServerEdition: OperatingSystemSKU = ...
    EnterpriseServerIA64Edition: OperatingSystemSKU = ...
    HomeBasicEdition: OperatingSystemSKU = ...
    HomeBasicNEdition: OperatingSystemSKU = ...
    HomePremiumEdition: OperatingSystemSKU = ...
    HomeServerEdition: OperatingSystemSKU = ...
    MicrosoftHyperVServer: OperatingSystemSKU = ...
    ServerForSmallBusinessEdition: OperatingSystemSKU = ...
    ServerFoundation: OperatingSystemSKU = ...
    SmallBusinessServerEdition: OperatingSystemSKU = ...
    SmallBusinessServerPremiumCore: OperatingSystemSKU = ...
    SmallBusinessServerPremiumEdition: OperatingSystemSKU = ...
    StandardServerCoreEdition: OperatingSystemSKU = ...
    StandardServerEdition: OperatingSystemSKU = ...
    StarterEdition: OperatingSystemSKU = ...
    StorageEnterpriseServerEdition: OperatingSystemSKU = ...
    StorageExpressServerEdition: OperatingSystemSKU = ...
    StorageServerEnterpriseCore: OperatingSystemSKU = ...
    StorageServerExpressCore: OperatingSystemSKU = ...
    StorageServerStandardCore: OperatingSystemSKU = ...
    StorageServerWorkgroupCore: OperatingSystemSKU = ...
    StorageStandardServerEdition: OperatingSystemSKU = ...
    StorageWorkgroupServerEdition: OperatingSystemSKU = ...
    TBD: OperatingSystemSKU = ...
    UltimateEdition: OperatingSystemSKU = ...
    Undefined: OperatingSystemSKU = ...
    value__ = ...
    WebServerCore: OperatingSystemSKU = ...
    WebServerEdition: OperatingSystemSKU = ...
    WindowsEmbeddedHandheld: OperatingSystemSKU = ...
    WindowsEmbeddedIndustry: OperatingSystemSKU = ...
    WindowsEnterprise: OperatingSystemSKU = ...
    WindowsHome: OperatingSystemSKU = ...
    WindowsHomeServer: OperatingSystemSKU = ...
    WindowsIotCore: OperatingSystemSKU = ...
    WindowsMobile: OperatingSystemSKU = ...
    WindowsProfessionalWithMediaCenter: OperatingSystemSKU = ...
    WindowsRT: OperatingSystemSKU = ...
    WindowsServerDatacenterNoHyperVCore: OperatingSystemSKU = ...
    WindowsServerDatacenterNoHyperVFull: OperatingSystemSKU = ...
    WindowsServerEnterpriseNoHyperVCore: OperatingSystemSKU = ...
    WindowsServerEnterpriseNoHyperVFull: OperatingSystemSKU = ...
    WindowsServerHyperCoreV: OperatingSystemSKU = ...
    WindowsServerStandardNoHyperVCore: OperatingSystemSKU = ...
    WindowsServerStandardNoHyperVFull: OperatingSystemSKU = ...
    WindowsSmallBusinessServer2011Essentials: OperatingSystemSKU = ...
    WindowsThinPC: OperatingSystemSKU = ...
    WindowsUltimate: OperatingSystemSKU = ...


class OrderObjectBase(ObjectBase): # skipped bases: <type 'object'>
    """ OrderObjectBase() """
    pass

class OSEncryptionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OSEncryptionLevel, values: Encrypt128Bits (1), Encrypt40Bits (0), EncryptNBits (2) """
    Encrypt128Bits: OSEncryptionLevel = ...
    Encrypt40Bits: OSEncryptionLevel = ...
    EncryptNBits: OSEncryptionLevel = ...
    value__ = ...


class OSProductSuite(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) OSProductSuite, values: BackOfficeComponents (4), CommunicationsServer (8), ComputeClusterEdition (16384), DatacenterEdition (128), HomeEdition (512), Server2008Enterprise (2), SmallBusinessServer (1), SmallBusinessServerRestricted (32), StorageServerEdition (8192), TerminalServices (16), TerminalServicesSingleSession (256), WebServerEdition (1024), WindowsEmbedded (64) """
    BackOfficeComponents: OSProductSuite = ...
    CommunicationsServer: OSProductSuite = ...
    ComputeClusterEdition: OSProductSuite = ...
    DatacenterEdition: OSProductSuite = ...
    HomeEdition: OSProductSuite = ...
    Server2008Enterprise: OSProductSuite = ...
    SmallBusinessServer: OSProductSuite = ...
    SmallBusinessServerRestricted: OSProductSuite = ...
    StorageServerEdition: OSProductSuite = ...
    TerminalServices: OSProductSuite = ...
    TerminalServicesSingleSession: OSProductSuite = ...
    value__ = ...
    WebServerEdition: OSProductSuite = ...
    WindowsEmbedded: OSProductSuite = ...


class OSType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OSType, values: AIX (9), ASERIES (32), ATTUNIX (3), BeOS (53), BS2000 (35), BSDUNIX (41), DC_OS (23), DECNT (5), Dedicated (59), DGUX (4), DigitalUNIX (6), EPOC (49), FreeBSD (42), GNUHurd (44), HP_MPE (54), HPUX (8), Inferno (47), InteractiveUNIX (40), IRIX (28), IxWorks (50), JavaVM (13), LINUX (36), Lynx (37), MACHKernel (46), MACROS (2), MiNT (52), MSDOS (14), MVS (10), NCR3000 (20), NetBSD (43), NetWare (21), NextStep (55), OpenVMS (7), OS_390 (60), OS2 (12), OS400 (11), OS9 (45), OSF (22), Other (1), PalmPilot (56), QNX (48), ReliantUNIX (24), Rhapsody (57), SCOOpenServer (26), SCOUnixWare (25), Sequent (27), Solaris (29), SunOS (30), TandemNSK (33), TandemNT (34), TPF (62), U6000 (31), Unknown (0), VM_ESA (39), VSE (61), VxWorks (51), WIN3x (15), WIN95 (16), WIN98 (17), WINCE (19), Windows2000 (58), WINNT (18), XENIX (38) """
    AIX: OSType = ...
    ASERIES: OSType = ...
    ATTUNIX: OSType = ...
    BeOS: OSType = ...
    BS2000: OSType = ...
    BSDUNIX: OSType = ...
    DC_OS: OSType = ...
    DECNT: OSType = ...
    Dedicated: OSType = ...
    DGUX: OSType = ...
    DigitalUNIX: OSType = ...
    EPOC: OSType = ...
    FreeBSD: OSType = ...
    GNUHurd: OSType = ...
    HPUX: OSType = ...
    HP_MPE: OSType = ...
    Inferno: OSType = ...
    InteractiveUNIX: OSType = ...
    IRIX: OSType = ...
    IxWorks: OSType = ...
    JavaVM: OSType = ...
    LINUX: OSType = ...
    Lynx: OSType = ...
    MACHKernel: OSType = ...
    MACROS: OSType = ...
    MiNT: OSType = ...
    MSDOS: OSType = ...
    MVS: OSType = ...
    NCR3000: OSType = ...
    NetBSD: OSType = ...
    NetWare: OSType = ...
    NextStep: OSType = ...
    OpenVMS: OSType = ...
    OS2: OSType = ...
    OS400: OSType = ...
    OS9: OSType = ...
    OSF: OSType = ...
    OS_390: OSType = ...
    Other: OSType = ...
    PalmPilot: OSType = ...
    QNX: OSType = ...
    ReliantUNIX: OSType = ...
    Rhapsody: OSType = ...
    SCOOpenServer: OSType = ...
    SCOUnixWare: OSType = ...
    Sequent: OSType = ...
    Solaris: OSType = ...
    SunOS: OSType = ...
    TandemNSK: OSType = ...
    TandemNT: OSType = ...
    TPF: OSType = ...
    U6000: OSType = ...
    Unknown: OSType = ...
    value__ = ...
    VM_ESA: OSType = ...
    VSE: OSType = ...
    VxWorks: OSType = ...
    WIN3x: OSType = ...
    WIN95: OSType = ...
    WIN98: OSType = ...
    WINCE: OSType = ...
    Windows2000: OSType = ...
    WINNT: OSType = ...
    XENIX: OSType = ...


class OutDefaultCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutDefaultCommand() """
    @property
    def Transcript(self) -> SwitchParameter:
        """
        Get: Transcript(self: OutDefaultCommand) -> SwitchParameter
        Set: Transcript(self: OutDefaultCommand) = value
        """
        ...



class OutFileCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutFileCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: OutFileCommand) -> SwitchParameter
        Set: Append(self: OutFileCommand) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: OutFileCommand) -> str
        Set: Encoding(self: OutFileCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: OutFileCommand) -> str
        Set: FilePath(self: OutFileCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: OutFileCommand) -> SwitchParameter
        Set: Force(self: OutFileCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: OutFileCommand) -> str
        Set: LiteralPath(self: OutFileCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: OutFileCommand) -> SwitchParameter
        Set: NoClobber(self: OutFileCommand) = value
        """
        ...

    @property
    def NoNewline(self) -> SwitchParameter:
        """
        Get: NoNewline(self: OutFileCommand) -> SwitchParameter
        Set: NoNewline(self: OutFileCommand) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: OutFileCommand) -> int
        Set: Width(self: OutFileCommand) = value
        """
        ...



class OutGridViewCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ OutGridViewCommand() """
    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: OutGridViewCommand) -> PSObject
        Set: InputObject(self: OutGridViewCommand) = value
        """
        ...

    @property
    def OutputMode(self): # -> OutputModeOption
        """
        Get: OutputMode(self: OutGridViewCommand) -> OutputModeOption
        Set: OutputMode(self: OutGridViewCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: OutGridViewCommand) -> SwitchParameter
        Set: PassThru(self: OutGridViewCommand) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: OutGridViewCommand) -> str
        Set: Title(self: OutGridViewCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: OutGridViewCommand) -> SwitchParameter
        Set: Wait(self: OutGridViewCommand) = value
        """
        ...



class OutHostCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutHostCommand() """
    @property
    def Paging(self) -> SwitchParameter:
        """
        Get: Paging(self: OutHostCommand) -> SwitchParameter
        Set: Paging(self: OutHostCommand) = value
        """
        ...



class OutLineOutputCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutLineOutputCommand() """
    @property
    def LineOutput(self) -> object:
        """
        Get: LineOutput(self: OutLineOutputCommand) -> object
        Set: LineOutput(self: OutLineOutputCommand) = value
        """
        ...



class OutNullCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ OutNullCommand() """
    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: OutNullCommand) -> PSObject
        Set: InputObject(self: OutNullCommand) = value
        """
        ...



class OutPrinterCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutPrinterCommand() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: OutPrinterCommand) -> str
        Set: Name(self: OutPrinterCommand) = value
        """
        ...



class OutputAssemblyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OutputAssemblyType, values: ConsoleApplication (1), Library (0), WindowsApplication (2) """
    ConsoleApplication: OutputAssemblyType = ...
    Library: OutputAssemblyType = ...
    value__ = ...
    WindowsApplication: OutputAssemblyType = ...


class OutputModeOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OutputModeOption, values: Multiple (2), None (0), Single (1) """
    Multiple: OutputModeOption = ...
    Single: OutputModeOption = ...
    value__ = ...


class OutStringCommand(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OutStringCommand() """
    @property
    def Stream(self) -> SwitchParameter:
        """
        Get: Stream(self: OutStringCommand) -> SwitchParameter
        Set: Stream(self: OutStringCommand) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: OutStringCommand) -> int
        Set: Width(self: OutStringCommand) = value
        """
        ...



class OutTarget(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OutTarget, values: Default (0), Host (1), Job (2) """
    Default: OutTarget = ...
    Host: OutTarget = ...
    Job: OutTarget = ...
    value__ = ...


class PCSystemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PCSystemType, values: AppliancePC (6), Desktop (1), EnterpriseServer (4), Maximum (8), Mobile (2), PerformanceServer (7), SOHOServer (5), Unspecified (0), Workstation (3) """
    AppliancePC: PCSystemType = ...
    Desktop: PCSystemType = ...
    EnterpriseServer: PCSystemType = ...
    Maximum: PCSystemType = ...
    Mobile: PCSystemType = ...
    PerformanceServer: PCSystemType = ...
    SOHOServer: PCSystemType = ...
    Unspecified: PCSystemType = ...
    value__ = ...
    Workstation: PCSystemType = ...


class PCSystemTypeEx(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PCSystemTypeEx, values: AppliancePC (6), Desktop (1), EnterpriseServer (4), Maximum (9), Mobile (2), PerformanceServer (7), Slate (8), SOHOServer (5), Unspecified (0), Workstation (3) """
    AppliancePC: PCSystemTypeEx = ...
    Desktop: PCSystemTypeEx = ...
    EnterpriseServer: PCSystemTypeEx = ...
    Maximum: PCSystemTypeEx = ...
    Mobile: PCSystemTypeEx = ...
    PerformanceServer: PCSystemTypeEx = ...
    Slate: PCSystemTypeEx = ...
    SOHOServer: PCSystemTypeEx = ...
    Unspecified: PCSystemTypeEx = ...
    value__ = ...
    Workstation: PCSystemTypeEx = ...


class PopLocationCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ PopLocationCommand() """
    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: PopLocationCommand) -> SwitchParameter
        Set: PassThru(self: PopLocationCommand) = value
        """
        ...

    @property
    def StackName(self) -> str:
        """
        Get: StackName(self: PopLocationCommand) -> str
        Set: StackName(self: PopLocationCommand) = value
        """
        ...



class PowerManagementCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerManagementCapabilities, values: Disabled (2), Enabled (3), NotSupported (1), PowerCyclingSupported (6), PowerSavingModesEnteredAutomatically (4), PowerStateSettable (5), TimedPowerOnSupported (7), Unknown (0) """
    Disabled: PowerManagementCapabilities = ...
    Enabled: PowerManagementCapabilities = ...
    NotSupported: PowerManagementCapabilities = ...
    PowerCyclingSupported: PowerManagementCapabilities = ...
    PowerSavingModesEnteredAutomatically: PowerManagementCapabilities = ...
    PowerStateSettable: PowerManagementCapabilities = ...
    TimedPowerOnSupported: PowerManagementCapabilities = ...
    Unknown: PowerManagementCapabilities = ...
    value__ = ...


class PowerPlatformRole(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerPlatformRole, values: AppliancePC (6), Desktop (1), EnterpriseServer (4), MaximumEnumValue (9), Mobile (2), PerformanceServer (7), Slate (8), SOHOServer (5), Unspecified (0), Workstation (3) """
    AppliancePC: PowerPlatformRole = ...
    Desktop: PowerPlatformRole = ...
    EnterpriseServer: PowerPlatformRole = ...
    MaximumEnumValue: PowerPlatformRole = ...
    Mobile: PowerPlatformRole = ...
    PerformanceServer: PowerPlatformRole = ...
    Slate: PowerPlatformRole = ...
    SOHOServer: PowerPlatformRole = ...
    Unspecified: PowerPlatformRole = ...
    value__ = ...
    Workstation: PowerPlatformRole = ...


class PowerState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerState, values: FullPower (1), PowerCycle (5), PowerOff (6), PowerSaveHibernate (8), PowerSaveLowPowerMode (2), PowerSaveSoftOff (9), PowerSaveStandby (3), PowerSaveUnknown (4), PowerSaveWarning (7), Unknown (0) """
    FullPower: PowerState = ...
    PowerCycle: PowerState = ...
    PowerOff: PowerState = ...
    PowerSaveHibernate: PowerState = ...
    PowerSaveLowPowerMode: PowerState = ...
    PowerSaveSoftOff: PowerState = ...
    PowerSaveStandby: PowerState = ...
    PowerSaveUnknown: PowerState = ...
    PowerSaveWarning: PowerState = ...
    Unknown: PowerState = ...
    value__ = ...


class ProcessCommandException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProcessCommandException()
    ProcessCommandException(message: str)
    ProcessCommandException(message: str, innerException: Exception)
    """
    @property
    def ProcessName(self) -> str:
        """
        Get: ProcessName(self: ProcessCommandException) -> str
        Set: ProcessName(self: ProcessCommandException) = value
        """
        ...


    SerializeObjectState = ...


class Processor: # skipped bases: <type 'object'>, <type 'object'>
    """ Processor() """
    @property
    def AddressWidth(self) -> Nullable:
        """ Get: AddressWidth(self: Processor) -> Nullable[UInt16] """
        ...

    @property
    def Architecture(self) -> Nullable:
        """ Get: Architecture(self: Processor) -> Nullable[CpuArchitecture] """
        ...

    @property
    def Availability(self) -> Nullable:
        """ Get: Availability(self: Processor) -> Nullable[CpuAvailability] """
        ...

    @property
    def CpuStatus(self) -> Nullable:
        """ Get: CpuStatus(self: Processor) -> Nullable[CpuStatus] """
        ...

    @property
    def CurrentClockSpeed(self) -> Nullable:
        """ Get: CurrentClockSpeed(self: Processor) -> Nullable[UInt32] """
        ...

    @property
    def DataWidth(self) -> Nullable:
        """ Get: DataWidth(self: Processor) -> Nullable[UInt16] """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Processor) -> str """
        ...

    @property
    def Manufacturer(self) -> str:
        """ Get: Manufacturer(self: Processor) -> str """
        ...

    @property
    def MaxClockSpeed(self) -> Nullable:
        """ Get: MaxClockSpeed(self: Processor) -> Nullable[UInt32] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Processor) -> str """
        ...

    @property
    def NumberOfCores(self) -> Nullable:
        """ Get: NumberOfCores(self: Processor) -> Nullable[UInt32] """
        ...

    @property
    def NumberOfLogicalProcessors(self) -> Nullable:
        """ Get: NumberOfLogicalProcessors(self: Processor) -> Nullable[UInt32] """
        ...

    @property
    def ProcessorID(self) -> str:
        """ Get: ProcessorID(self: Processor) -> str """
        ...

    @property
    def ProcessorType(self) -> Nullable:
        """ Get: ProcessorType(self: Processor) -> Nullable[ProcessorType] """
        ...

    @property
    def Role(self) -> str:
        """ Get: Role(self: Processor) -> str """
        ...

    @property
    def SocketDesignation(self) -> str:
        """ Get: SocketDesignation(self: Processor) -> str """
        ...

    @property
    def Status(self) -> str:
        """ Get: Status(self: Processor) -> str """
        ...



class ProcessorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessorType, values: CentralProcessor (3), DSPProcessor (5), MathProcessor (4), Other (1), Unknown (2), VideoProcessor (6) """
    CentralProcessor: ProcessorType = ...
    DSPProcessor: ProcessorType = ...
    MathProcessor: ProcessorType = ...
    Other: ProcessorType = ...
    Unknown: ProcessorType = ...
    value__ = ...
    VideoProcessor: ProcessorType = ...


class ProductType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProductType, values: DomainController (2), Server (3), Unknown (0), WorkStation (1) """
    DomainController: ProductType = ...
    Server: ProductType = ...
    Unknown: ProductType = ...
    value__ = ...
    WorkStation: ProductType = ...


class ProtectCmsMessageCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ProtectCmsMessageCommand() """
    @property
    def Content(self) -> PSObject:
        """
        Get: Content(self: ProtectCmsMessageCommand) -> PSObject
        Set: Content(self: ProtectCmsMessageCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: ProtectCmsMessageCommand) -> str
        Set: LiteralPath(self: ProtectCmsMessageCommand) = value
        """
        ...

    @property
    def OutFile(self) -> str:
        """
        Get: OutFile(self: ProtectCmsMessageCommand) -> str
        Set: OutFile(self: ProtectCmsMessageCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ProtectCmsMessageCommand) -> str
        Set: Path(self: ProtectCmsMessageCommand) = value
        """
        ...

    @property
    def To(self) -> Array:
        """
        Get: To(self: ProtectCmsMessageCommand) -> Array[CmsMessageRecipient]
        Set: To(self: ProtectCmsMessageCommand) = value
        """
        ...



class PSEditionArgumentCompleter(IArgumentCompleter): # skipped bases: <type 'object'>
    """ PSEditionArgumentCompleter() """
    pass

class PSHostProcessInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppDomainName(self) -> str:
        """ Get: AppDomainName(self: PSHostProcessInfo) -> str """
        ...

    @property
    def MainWindowTitle(self) -> str:
        """ Get: MainWindowTitle(self: PSHostProcessInfo) -> str """
        ...

    @property
    def ProcessId(self) -> int:
        """ Get: ProcessId(self: PSHostProcessInfo) -> int """
        ...

    @property
    def ProcessName(self) -> str:
        """ Get: ProcessName(self: PSHostProcessInfo) -> str """
        ...



class PSRunspaceDebug: # skipped bases: <type 'object'>, <type 'object'>
    """ PSRunspaceDebug(enabled: bool, breakAll: bool, runspaceName: str, runspaceId: int) """
    @property
    def BreakAll(self) -> bool:
        """ Get: BreakAll(self: PSRunspaceDebug) -> bool """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: PSRunspaceDebug) -> bool """
        ...

    @property
    def RunspaceId(self) -> int:
        """ Get: RunspaceId(self: PSRunspaceDebug) -> int """
        ...

    @property
    def RunspaceName(self) -> str:
        """ Get: RunspaceName(self: PSRunspaceDebug) -> str """
        ...



class PSSessionConfigurationCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessMode(self) -> PSSessionConfigurationAccessMode:
        """
        Get: AccessMode(self: PSSessionConfigurationCommandBase) -> PSSessionConfigurationAccessMode
        Set: AccessMode(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ApplicationBase(self) -> str:
        """
        Get: ApplicationBase(self: PSSessionConfigurationCommandBase) -> str
        Set: ApplicationBase(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: PSSessionConfigurationCommandBase) -> str
        Set: AssemblyName(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ConfigurationTypeName(self) -> str:
        """
        Get: ConfigurationTypeName(self: PSSessionConfigurationCommandBase) -> str
        Set: ConfigurationTypeName(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: PSSessionConfigurationCommandBase) -> SwitchParameter
        Set: Force(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def MaximumReceivedDataSizePerCommandMB(self) -> Nullable:
        """
        Get: MaximumReceivedDataSizePerCommandMB(self: PSSessionConfigurationCommandBase) -> Nullable[float]
        Set: MaximumReceivedDataSizePerCommandMB(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def MaximumReceivedObjectSizeMB(self) -> Nullable:
        """
        Get: MaximumReceivedObjectSizeMB(self: PSSessionConfigurationCommandBase) -> Nullable[float]
        Set: MaximumReceivedObjectSizeMB(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ModulesToImport(self) -> Array:
        """
        Get: ModulesToImport(self: PSSessionConfigurationCommandBase) -> Array[object]
        Set: ModulesToImport(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PSSessionConfigurationCommandBase) -> str
        Set: Name(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def NoServiceRestart(self) -> SwitchParameter:
        """
        Get: NoServiceRestart(self: PSSessionConfigurationCommandBase) -> SwitchParameter
        Set: NoServiceRestart(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: PSSessionConfigurationCommandBase) -> str
        Set: Path(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def PSVersion(self) -> Version:
        """
        Get: PSVersion(self: PSSessionConfigurationCommandBase) -> Version
        Set: PSVersion(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def RunAsCredential(self) -> PSCredential:
        """
        Get: RunAsCredential(self: PSSessionConfigurationCommandBase) -> PSCredential
        Set: RunAsCredential(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def RunAsVirtualAccount(self):
        ...

    @property
    def RunAsVirtualAccountGroups(self):
        ...

    @property
    def RunAsVirtualAccountSpecified(self):
        ...

    @property
    def SecurityDescriptorSddl(self) -> str:
        """
        Get: SecurityDescriptorSddl(self: PSSessionConfigurationCommandBase) -> str
        Set: SecurityDescriptorSddl(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def SessionTypeOption(self) -> PSSessionTypeOption:
        """
        Get: SessionTypeOption(self: PSSessionConfigurationCommandBase) -> PSSessionTypeOption
        Set: SessionTypeOption(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ShowSecurityDescriptorUI(self) -> SwitchParameter:
        """
        Get: ShowSecurityDescriptorUI(self: PSSessionConfigurationCommandBase) -> SwitchParameter
        Set: ShowSecurityDescriptorUI(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def StartupScript(self) -> str:
        """
        Get: StartupScript(self: PSSessionConfigurationCommandBase) -> str
        Set: StartupScript(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ThreadApartmentState(self) -> ApartmentState:
        """
        Get: ThreadApartmentState(self: PSSessionConfigurationCommandBase) -> ApartmentState
        Set: ThreadApartmentState(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def ThreadOptions(self) -> PSThreadOptions:
        """
        Get: ThreadOptions(self: PSSessionConfigurationCommandBase) -> PSThreadOptions
        Set: ThreadOptions(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def TransportOption(self) -> PSTransportOption:
        """
        Get: TransportOption(self: PSSessionConfigurationCommandBase) -> PSTransportOption
        Set: TransportOption(self: PSSessionConfigurationCommandBase) = value
        """
        ...

    @property
    def UseSharedProcess(self) -> SwitchParameter:
        """
        Get: UseSharedProcess(self: PSSessionConfigurationCommandBase) -> SwitchParameter
        Set: UseSharedProcess(self: PSSessionConfigurationCommandBase) = value
        """
        ...



class PSUserAgent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Chrome(self) -> str:
        """ Get: Chrome() -> str """
        ...

    @property
    def FireFox(self) -> str:
        """ Get: FireFox() -> str """
        ...

    @property
    def InternetExplorer(self) -> str:
        """ Get: InternetExplorer() -> str """
        ...

    @property
    def Opera(self) -> str:
        """ Get: Opera() -> str """
        ...

    @property
    def Safari(self) -> str:
        """ Get: Safari() -> str """
        ...


    __all__: list = ...


class PushLocationCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ PushLocationCommand() """
    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: PushLocationCommand) -> str
        Set: LiteralPath(self: PushLocationCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: PushLocationCommand) -> SwitchParameter
        Set: PassThru(self: PushLocationCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: PushLocationCommand) -> str
        Set: Path(self: PushLocationCommand) = value
        """
        ...

    @property
    def StackName(self) -> str:
        """
        Get: StackName(self: PushLocationCommand) -> str
        Set: StackName(self: PushLocationCommand) = value
        """
        ...



class ReadHostCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ReadHostCommand() """
    @property
    def AsSecureString(self) -> SwitchParameter:
        """
        Get: AsSecureString(self: ReadHostCommand) -> SwitchParameter
        Set: AsSecureString(self: ReadHostCommand) = value
        """
        ...

    @property
    def Prompt(self) -> object:
        """
        Get: Prompt(self: ReadHostCommand) -> object
        Set: Prompt(self: ReadHostCommand) = value
        """
        ...



class ReceiveJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ ReceiveJobCommand() """
    @property
    def AutoRemoveJob(self) -> SwitchParameter:
        """
        Get: AutoRemoveJob(self: ReceiveJobCommand) -> SwitchParameter
        Set: AutoRemoveJob(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: ReceiveJobCommand) -> Array[str]
        Set: ComputerName(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: ReceiveJobCommand) -> SwitchParameter
        Set: Force(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Job(self) -> Array:
        """
        Get: Job(self: ReceiveJobCommand) -> Array[Job]
        Set: Job(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Keep(self) -> SwitchParameter:
        """
        Get: Keep(self: ReceiveJobCommand) -> SwitchParameter
        Set: Keep(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Location(self) -> Array:
        """
        Get: Location(self: ReceiveJobCommand) -> Array[str]
        Set: Location(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def NoRecurse(self) -> SwitchParameter:
        """
        Get: NoRecurse(self: ReceiveJobCommand) -> SwitchParameter
        Set: NoRecurse(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Session(self) -> Array:
        """
        Get: Session(self: ReceiveJobCommand) -> Array[PSSession]
        Set: Session(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: ReceiveJobCommand) -> SwitchParameter
        Set: Wait(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def WriteEvents(self) -> SwitchParameter:
        """
        Get: WriteEvents(self: ReceiveJobCommand) -> SwitchParameter
        Set: WriteEvents(self: ReceiveJobCommand) = value
        """
        ...

    @property
    def WriteJobInResults(self) -> SwitchParameter:
        """
        Get: WriteJobInResults(self: ReceiveJobCommand) -> SwitchParameter
        Set: WriteJobInResults(self: ReceiveJobCommand) = value
        """
        ...


    LocationParameterSet: str = ...


class ReceivePSSessionCommand(PSRemotingCmdlet): # skipped bases: <type 'object'>
    """ ReceivePSSessionCommand() """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """
        Get: AllowRedirection(self: ReceivePSSessionCommand) -> SwitchParameter
        Set: AllowRedirection(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: ReceivePSSessionCommand) -> str
        Set: ApplicationName(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: ReceivePSSessionCommand) -> AuthenticationMechanism
        Set: Authentication(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: ReceivePSSessionCommand) -> str
        Set: CertificateThumbprint(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: ReceivePSSessionCommand) -> str
        Set: ComputerName(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: ReceivePSSessionCommand) -> str
        Set: ConfigurationName(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def ConnectionUri(self) -> Uri:
        """
        Get: ConnectionUri(self: ReceivePSSessionCommand) -> Uri
        Set: ConnectionUri(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: ReceivePSSessionCommand) -> PSCredential
        Set: Credential(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: ReceivePSSessionCommand) -> int
        Set: Id(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: ReceivePSSessionCommand) -> Guid
        Set: InstanceId(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def JobName(self) -> str:
        """
        Get: JobName(self: ReceivePSSessionCommand) -> str
        Set: JobName(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ReceivePSSessionCommand) -> str
        Set: Name(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def OutTarget(self) -> OutTarget:
        """
        Get: OutTarget(self: ReceivePSSessionCommand) -> OutTarget
        Set: OutTarget(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: ReceivePSSessionCommand) -> int
        Set: Port(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def Session(self) -> PSSession:
        """
        Get: Session(self: ReceivePSSessionCommand) -> PSSession
        Set: Session(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: ReceivePSSessionCommand) -> PSSessionOption
        Set: SessionOption(self: ReceivePSSessionCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: ReceivePSSessionCommand) -> SwitchParameter
        Set: UseSSL(self: ReceivePSSessionCommand) = value
        """
        ...



class RegisterEngineEventCommand(ObjectEventRegistrationBase): # skipped bases: <type 'object'>
    """ RegisterEngineEventCommand() """
    pass

class RegisterObjectEventCommand(ObjectEventRegistrationBase): # skipped bases: <type 'object'>
    """ RegisterObjectEventCommand() """
    @property
    def EventName(self) -> str:
        """
        Get: EventName(self: RegisterObjectEventCommand) -> str
        Set: EventName(self: RegisterObjectEventCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: RegisterObjectEventCommand) -> PSObject
        Set: InputObject(self: RegisterObjectEventCommand) = value
        """
        ...



class RegisterPSSessionConfigurationCommand(PSSessionConfigurationCommandBase): # skipped bases: <type 'object'>
    """ RegisterPSSessionConfigurationCommand() """
    @property
    def ProcessorArchitecture(self) -> str:
        """
        Get: ProcessorArchitecture(self: RegisterPSSessionConfigurationCommand) -> str
        Set: ProcessorArchitecture(self: RegisterPSSessionConfigurationCommand) = value
        """
        ...

    @property
    def SessionType(self) -> PSSessionType:
        """
        Get: SessionType(self: RegisterPSSessionConfigurationCommand) -> PSSessionType
        Set: SessionType(self: RegisterPSSessionConfigurationCommand) = value
        """
        ...



class RegisterWmiEventCommand(ObjectEventRegistrationBase): # skipped bases: <type 'object'>
    """ RegisterWmiEventCommand() """
    @property
    def Class(self) -> str:
        """
        Get: Class(self: RegisterWmiEventCommand) -> str
        Set: Class(self: RegisterWmiEventCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: RegisterWmiEventCommand) -> str
        Set: ComputerName(self: RegisterWmiEventCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: RegisterWmiEventCommand) -> PSCredential
        Set: Credential(self: RegisterWmiEventCommand) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: RegisterWmiEventCommand) -> str
        Set: Namespace(self: RegisterWmiEventCommand) = value
        """
        ...

    @property
    def Query(self) -> str:
        """
        Get: Query(self: RegisterWmiEventCommand) -> str
        Set: Query(self: RegisterWmiEventCommand) = value
        """
        ...

    @property
    def Timeout(self) -> Int64:
        """
        Get: Timeout(self: RegisterWmiEventCommand) -> Int64
        Set: Timeout(self: RegisterWmiEventCommand) = value
        """
        ...



class RegistryProvider(ISecurityDescriptorCmdletProvider, NavigationCmdletProvider, IDynamicPropertyCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'IPropertyCmdletProvider'>, <type 'object'>
    """ RegistryProvider() """
    def ClearProperty(self, path:str, propertyToClear:Collection): # -> 
        """ ClearProperty(self: RegistryProvider, path: str, propertyToClear: Collection[str]) """
        ...

    def ClearPropertyDynamicParameters(self, path:str, propertyToClear:Collection) -> object:
        """ ClearPropertyDynamicParameters(self: RegistryProvider, path: str, propertyToClear: Collection[str]) -> object """
        ...

    def GetProperty(self, path:str, providerSpecificPickList:Collection): # -> 
        """ GetProperty(self: RegistryProvider, path: str, providerSpecificPickList: Collection[str]) """
        ...

    def GetPropertyDynamicParameters(self, path:str, providerSpecificPickList:Collection) -> object:
        """ GetPropertyDynamicParameters(self: RegistryProvider, path: str, providerSpecificPickList: Collection[str]) -> object """
        ...

    def SetProperty(self, path:str, propertyValue:PSObject): # -> 
        """ SetProperty(self: RegistryProvider, path: str, propertyValue: PSObject) """
        ...

    def SetPropertyDynamicParameters(self, path:str, propertyValue:PSObject) -> object:
        """ SetPropertyDynamicParameters(self: RegistryProvider, path: str, propertyValue: PSObject) -> object """
        ...

    ProviderName: str = ...


class RegistryProviderSetItemDynamicParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ RegistryProviderSetItemDynamicParameter() """
    @property
    def Type(self) -> RegistryValueKind:
        """
        Get: Type(self: RegistryProviderSetItemDynamicParameter) -> RegistryValueKind
        Set: Type(self: RegistryProviderSetItemDynamicParameter) = value
        """
        ...



class RemoveComputerCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RemoveComputerCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: RemoveComputerCommand) -> Array[str]
        Set: ComputerName(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveComputerCommand) -> SwitchParameter
        Set: Force(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def LocalCredential(self) -> PSCredential:
        """
        Get: LocalCredential(self: RemoveComputerCommand) -> PSCredential
        Set: LocalCredential(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: RemoveComputerCommand) -> SwitchParameter
        Set: PassThru(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def Restart(self) -> SwitchParameter:
        """
        Get: Restart(self: RemoveComputerCommand) -> SwitchParameter
        Set: Restart(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def UnjoinDomainCredential(self) -> PSCredential:
        """
        Get: UnjoinDomainCredential(self: RemoveComputerCommand) -> PSCredential
        Set: UnjoinDomainCredential(self: RemoveComputerCommand) = value
        """
        ...

    @property
    def WorkgroupName(self) -> str:
        """
        Get: WorkgroupName(self: RemoveComputerCommand) -> str
        Set: WorkgroupName(self: RemoveComputerCommand) = value
        """
        ...



class RemoveEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RemoveEventCommand() """
    @property
    def EventIdentifier(self) -> int:
        """
        Get: EventIdentifier(self: RemoveEventCommand) -> int
        Set: EventIdentifier(self: RemoveEventCommand) = value
        """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: RemoveEventCommand) -> str
        Set: SourceIdentifier(self: RemoveEventCommand) = value
        """
        ...



class RemoveEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RemoveEventLogCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: RemoveEventLogCommand) -> Array[str]
        Set: ComputerName(self: RemoveEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> Array:
        """
        Get: LogName(self: RemoveEventLogCommand) -> Array[str]
        Set: LogName(self: RemoveEventLogCommand) = value
        """
        ...

    @property
    def Source(self) -> Array:
        """
        Get: Source(self: RemoveEventLogCommand) -> Array[str]
        Set: Source(self: RemoveEventLogCommand) = value
        """
        ...



class RemoveItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ RemoveItemCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: RemoveItemCommand) -> Array[str]
        Set: Exclude(self: RemoveItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: RemoveItemCommand) -> str
        Set: Filter(self: RemoveItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveItemCommand) -> SwitchParameter
        Set: Force(self: RemoveItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: RemoveItemCommand) -> Array[str]
        Set: Include(self: RemoveItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: RemoveItemCommand) -> Array[str]
        Set: LiteralPath(self: RemoveItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: RemoveItemCommand) -> Array[str]
        Set: Path(self: RemoveItemCommand) = value
        """
        ...

    @property
    def Recurse(self) -> SwitchParameter:
        """
        Get: Recurse(self: RemoveItemCommand) -> SwitchParameter
        Set: Recurse(self: RemoveItemCommand) = value
        """
        ...



class RemoveItemPropertyCommand(ItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ RemoveItemPropertyCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveItemPropertyCommand) -> SwitchParameter
        Set: Force(self: RemoveItemPropertyCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: RemoveItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: RemoveItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: RemoveItemPropertyCommand) -> Array[str]
        Set: Name(self: RemoveItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: RemoveItemPropertyCommand) -> Array[str]
        Set: Path(self: RemoveItemPropertyCommand) = value
        """
        ...



class RemoveJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ RemoveJobCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveJobCommand) -> SwitchParameter
        Set: Force(self: RemoveJobCommand) = value
        """
        ...

    @property
    def Job(self) -> Array:
        """
        Get: Job(self: RemoveJobCommand) -> Array[Job]
        Set: Job(self: RemoveJobCommand) = value
        """
        ...



class RemoveModuleCommand(ModuleCmdletBase): # skipped bases: <type 'object'>
    """ RemoveModuleCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveModuleCommand) -> SwitchParameter
        Set: Force(self: RemoveModuleCommand) = value
        """
        ...

    @property
    def FullyQualifiedName(self) -> Array:
        """
        Get: FullyQualifiedName(self: RemoveModuleCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedName(self: RemoveModuleCommand) = value
        """
        ...

    @property
    def ModuleInfo(self) -> Array:
        """
        Get: ModuleInfo(self: RemoveModuleCommand) -> Array[PSModuleInfo]
        Set: ModuleInfo(self: RemoveModuleCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: RemoveModuleCommand) -> Array[str]
        Set: Name(self: RemoveModuleCommand) = value
        """
        ...



class RemovePSBreakpointCommand(PSBreakpointCommandBase): # skipped bases: <type 'object'>
    """ RemovePSBreakpointCommand() """
    pass

class RemovePSDriveCommand(DriveMatchingCoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ RemovePSDriveCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemovePSDriveCommand) -> SwitchParameter
        Set: Force(self: RemovePSDriveCommand) = value
        """
        ...

    @property
    def LiteralName(self) -> Array:
        """
        Get: LiteralName(self: RemovePSDriveCommand) -> Array[str]
        Set: LiteralName(self: RemovePSDriveCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: RemovePSDriveCommand) -> Array[str]
        Set: Name(self: RemovePSDriveCommand) = value
        """
        ...

    @property
    def PSProvider(self) -> Array:
        """
        Get: PSProvider(self: RemovePSDriveCommand) -> Array[str]
        Set: PSProvider(self: RemovePSDriveCommand) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: RemovePSDriveCommand) -> str
        Set: Scope(self: RemovePSDriveCommand) = value
        """
        ...



class RemovePSSessionCommand(PSRunspaceCmdlet): # skipped bases: <type 'object'>
    """ RemovePSSessionCommand() """
    @property
    def Session(self) -> Array:
        """
        Get: Session(self: RemovePSSessionCommand) -> Array[PSSession]
        Set: Session(self: RemovePSSessionCommand) = value
        """
        ...



class RemovePSSnapinCommand(PSSnapInCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ RemovePSSnapinCommand() """
    @property
    def Name(self) -> Array:
        """
        Get: Name(self: RemovePSSnapinCommand) -> Array[str]
        Set: Name(self: RemovePSSnapinCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: RemovePSSnapinCommand) -> SwitchParameter
        Set: PassThru(self: RemovePSSnapinCommand) = value
        """
        ...



class RemoveTypeDataCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RemoveTypeDataCommand() """
    @property
    def Path(self) -> Array:
        """
        Get: Path(self: RemoveTypeDataCommand) -> Array[str]
        Set: Path(self: RemoveTypeDataCommand) = value
        """
        ...

    @property
    def TypeData(self) -> TypeData:
        """
        Get: TypeData(self: RemoveTypeDataCommand) -> TypeData
        Set: TypeData(self: RemoveTypeDataCommand) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: RemoveTypeDataCommand) -> str
        Set: TypeName(self: RemoveTypeDataCommand) = value
        """
        ...



class RemoveVariableCommand(VariableCommandBase): # skipped bases: <type 'object'>
    """ RemoveVariableCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: RemoveVariableCommand) -> Array[str]
        Set: Exclude(self: RemoveVariableCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RemoveVariableCommand) -> SwitchParameter
        Set: Force(self: RemoveVariableCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: RemoveVariableCommand) -> Array[str]
        Set: Include(self: RemoveVariableCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: RemoveVariableCommand) -> Array[str]
        Set: Name(self: RemoveVariableCommand) = value
        """
        ...



class RemoveWmiObject(WmiBaseCmdlet): # skipped bases: <type 'object'>
    """ RemoveWmiObject() """
    @property
    def Class(self) -> str:
        """
        Get: Class(self: RemoveWmiObject) -> str
        Set: Class(self: RemoveWmiObject) = value
        """
        ...

    @property
    def InputObject(self) -> ManagementObject:
        """
        Get: InputObject(self: RemoveWmiObject) -> ManagementObject
        Set: InputObject(self: RemoveWmiObject) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: RemoveWmiObject) -> str
        Set: Path(self: RemoveWmiObject) = value
        """
        ...



class RenameComputerChangeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ RenameComputerChangeInfo() """
    @property
    def HasSucceeded(self) -> bool:
        """
        Get: HasSucceeded(self: RenameComputerChangeInfo) -> bool
        Set: HasSucceeded(self: RenameComputerChangeInfo) = value
        """
        ...

    @property
    def NewComputerName(self) -> str:
        """
        Get: NewComputerName(self: RenameComputerChangeInfo) -> str
        Set: NewComputerName(self: RenameComputerChangeInfo) = value
        """
        ...

    @property
    def OldComputerName(self) -> str:
        """
        Get: OldComputerName(self: RenameComputerChangeInfo) -> str
        Set: OldComputerName(self: RenameComputerChangeInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: RenameComputerChangeInfo) -> str """
        ...


class RenameComputerCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ RenameComputerCommand() """
    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: RenameComputerCommand) -> str
        Set: ComputerName(self: RenameComputerCommand) = value
        """
        ...

    @property
    def DomainCredential(self) -> PSCredential:
        """
        Get: DomainCredential(self: RenameComputerCommand) -> PSCredential
        Set: DomainCredential(self: RenameComputerCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RenameComputerCommand) -> SwitchParameter
        Set: Force(self: RenameComputerCommand) = value
        """
        ...

    @property
    def LocalCredential(self) -> PSCredential:
        """
        Get: LocalCredential(self: RenameComputerCommand) -> PSCredential
        Set: LocalCredential(self: RenameComputerCommand) = value
        """
        ...

    @property
    def NewName(self) -> str:
        """
        Get: NewName(self: RenameComputerCommand) -> str
        Set: NewName(self: RenameComputerCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: RenameComputerCommand) -> SwitchParameter
        Set: PassThru(self: RenameComputerCommand) = value
        """
        ...

    @property
    def Protocol(self) -> str:
        """
        Get: Protocol(self: RenameComputerCommand) -> str
        Set: Protocol(self: RenameComputerCommand) = value
        """
        ...

    @property
    def Restart(self) -> SwitchParameter:
        """
        Get: Restart(self: RenameComputerCommand) -> SwitchParameter
        Set: Restart(self: RenameComputerCommand) = value
        """
        ...

    @property
    def WsmanAuthentication(self) -> str:
        """
        Get: WsmanAuthentication(self: RenameComputerCommand) -> str
        Set: WsmanAuthentication(self: RenameComputerCommand) = value
        """
        ...



class RenameItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ RenameItemCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RenameItemCommand) -> SwitchParameter
        Set: Force(self: RenameItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: RenameItemCommand) -> str
        Set: LiteralPath(self: RenameItemCommand) = value
        """
        ...

    @property
    def NewName(self) -> str:
        """
        Get: NewName(self: RenameItemCommand) -> str
        Set: NewName(self: RenameItemCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: RenameItemCommand) -> SwitchParameter
        Set: PassThru(self: RenameItemCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: RenameItemCommand) -> str
        Set: Path(self: RenameItemCommand) = value
        """
        ...



class RenameItemPropertyCommand(PassThroughItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ RenameItemPropertyCommand() """
    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: RenameItemPropertyCommand) -> str
        Set: LiteralPath(self: RenameItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RenameItemPropertyCommand) -> str
        Set: Name(self: RenameItemPropertyCommand) = value
        """
        ...

    @property
    def NewName(self) -> str:
        """
        Get: NewName(self: RenameItemPropertyCommand) -> str
        Set: NewName(self: RenameItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: RenameItemPropertyCommand) -> str
        Set: Path(self: RenameItemPropertyCommand) = value
        """
        ...



class ResetCapability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResetCapability, values: Disabled (3), Enabled (4), NotImplemented (5), Other (1), Unknown (2) """
    Disabled: ResetCapability = ...
    Enabled: ResetCapability = ...
    NotImplemented: ResetCapability = ...
    Other: ResetCapability = ...
    Unknown: ResetCapability = ...
    value__ = ...


class ResetComputerMachinePasswordCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ResetComputerMachinePasswordCommand() """
    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: ResetComputerMachinePasswordCommand) -> PSCredential
        Set: Credential(self: ResetComputerMachinePasswordCommand) = value
        """
        ...

    @property
    def Server(self) -> str:
        """
        Get: Server(self: ResetComputerMachinePasswordCommand) -> str
        Set: Server(self: ResetComputerMachinePasswordCommand) = value
        """
        ...



class ResolvePathCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ ResolvePathCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: ResolvePathCommand) -> Array[str]
        Set: LiteralPath(self: ResolvePathCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: ResolvePathCommand) -> Array[str]
        Set: Path(self: ResolvePathCommand) = value
        """
        ...

    @property
    def Relative(self) -> SwitchParameter:
        """
        Get: Relative(self: ResolvePathCommand) -> SwitchParameter
        Set: Relative(self: ResolvePathCommand) = value
        """
        ...



class RestartComputerCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ RestartComputerCommand() """
    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: RestartComputerCommand) -> SwitchParameter
        Set: AsJob(self: RestartComputerCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: RestartComputerCommand) -> Array[str]
        Set: ComputerName(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: RestartComputerCommand) -> PSCredential
        Set: Credential(self: RestartComputerCommand) = value
        """
        ...

    @property
    def DcomAuthentication(self) -> AuthenticationLevel:
        """
        Get: DcomAuthentication(self: RestartComputerCommand) -> AuthenticationLevel
        Set: DcomAuthentication(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Delay(self) -> Int16:
        """
        Get: Delay(self: RestartComputerCommand) -> Int16
        Set: Delay(self: RestartComputerCommand) = value
        """
        ...

    @property
    def For(self): # -> WaitForServiceTypes
        """
        Get: For(self: RestartComputerCommand) -> WaitForServiceTypes
        Set: For(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RestartComputerCommand) -> SwitchParameter
        Set: Force(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationLevel:
        """
        Get: Impersonation(self: RestartComputerCommand) -> ImpersonationLevel
        Set: Impersonation(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Protocol(self) -> str:
        """
        Get: Protocol(self: RestartComputerCommand) -> str
        Set: Protocol(self: RestartComputerCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: RestartComputerCommand) -> int
        Set: ThrottleLimit(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: RestartComputerCommand) -> int
        Set: Timeout(self: RestartComputerCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: RestartComputerCommand) -> SwitchParameter
        Set: Wait(self: RestartComputerCommand) = value
        """
        ...

    @property
    def WsmanAuthentication(self) -> str:
        """
        Get: WsmanAuthentication(self: RestartComputerCommand) -> str
        Set: WsmanAuthentication(self: RestartComputerCommand) = value
        """
        ...



class RestartComputerTimeoutException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RestartComputerTimeoutException()
    RestartComputerTimeoutException(message: str)
    RestartComputerTimeoutException(message: str, innerException: Exception)
    """
    @property
    def ComputerName(self) -> str:
        """ Get: ComputerName(self: RestartComputerTimeoutException) -> str """
        ...

    @property
    def Timeout(self) -> int:
        """ Get: Timeout(self: RestartComputerTimeoutException) -> int """
        ...


    SerializeObjectState = ...


class ServiceOperationBaseCommand(MultipleServiceCommandBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> Array:
        """
        Get: Name(self: ServiceOperationBaseCommand) -> Array[str]
        Set: Name(self: ServiceOperationBaseCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ServiceOperationBaseCommand) -> SwitchParameter
        Set: PassThru(self: ServiceOperationBaseCommand) = value
        """
        ...



class RestartServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ RestartServiceCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: RestartServiceCommand) -> SwitchParameter
        Set: Force(self: RestartServiceCommand) = value
        """
        ...



class RestoreComputerCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ RestoreComputerCommand() """
    @property
    def RestorePoint(self) -> int:
        """
        Get: RestorePoint(self: RestoreComputerCommand) -> int
        Set: RestorePoint(self: RestoreComputerCommand) = value
        """
        ...



class ResumeJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ ResumeJobCommand() """
    @property
    def Job(self) -> Array:
        """
        Get: Job(self: ResumeJobCommand) -> Array[Job]
        Set: Job(self: ResumeJobCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: ResumeJobCommand) -> SwitchParameter
        Set: Wait(self: ResumeJobCommand) = value
        """
        ...



class ResumeServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ ResumeServiceCommand() """
    pass

class UpdatableHelpCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: UpdatableHelpCommandBase) -> PSCredential
        Set: Credential(self: UpdatableHelpCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: UpdatableHelpCommandBase) -> SwitchParameter
        Set: Force(self: UpdatableHelpCommandBase) = value
        """
        ...

    @property
    def UICulture(self) -> Array:
        """
        Get: UICulture(self: UpdatableHelpCommandBase) -> Array[CultureInfo]
        Set: UICulture(self: UpdatableHelpCommandBase) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> SwitchParameter:
        """
        Get: UseDefaultCredentials(self: UpdatableHelpCommandBase) -> SwitchParameter
        Set: UseDefaultCredentials(self: UpdatableHelpCommandBase) = value
        """
        ...



class SaveHelpCommand(UpdatableHelpCommandBase): # skipped bases: <type 'object'>
    """ SaveHelpCommand() """
    @property
    def DestinationPath(self) -> Array:
        """
        Get: DestinationPath(self: SaveHelpCommand) -> Array[str]
        Set: DestinationPath(self: SaveHelpCommand) = value
        """
        ...

    @property
    def FullyQualifiedModule(self) -> Array:
        """
        Get: FullyQualifiedModule(self: SaveHelpCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedModule(self: SaveHelpCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SaveHelpCommand) -> Array[str]
        Set: LiteralPath(self: SaveHelpCommand) = value
        """
        ...

    @property
    def Module(self) -> Array:
        """
        Get: Module(self: SaveHelpCommand) -> Array[PSModuleInfo]
        Set: Module(self: SaveHelpCommand) = value
        """
        ...



class SelectObjectCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SelectObjectCommand() """
    @property
    def ExcludeProperty(self) -> Array:
        """
        Get: ExcludeProperty(self: SelectObjectCommand) -> Array[str]
        Set: ExcludeProperty(self: SelectObjectCommand) = value
        """
        ...

    @property
    def ExpandProperty(self) -> str:
        """
        Get: ExpandProperty(self: SelectObjectCommand) -> str
        Set: ExpandProperty(self: SelectObjectCommand) = value
        """
        ...

    @property
    def First(self) -> int:
        """
        Get: First(self: SelectObjectCommand) -> int
        Set: First(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Index(self) -> Array:
        """
        Get: Index(self: SelectObjectCommand) -> Array[int]
        Set: Index(self: SelectObjectCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: SelectObjectCommand) -> PSObject
        Set: InputObject(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Last(self) -> int:
        """
        Get: Last(self: SelectObjectCommand) -> int
        Set: Last(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> Array:
        """
        Get: Property(self: SelectObjectCommand) -> Array[object]
        Set: Property(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Skip(self) -> int:
        """
        Get: Skip(self: SelectObjectCommand) -> int
        Set: Skip(self: SelectObjectCommand) = value
        """
        ...

    @property
    def SkipLast(self) -> int:
        """
        Get: SkipLast(self: SelectObjectCommand) -> int
        Set: SkipLast(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Unique(self) -> SwitchParameter:
        """
        Get: Unique(self: SelectObjectCommand) -> SwitchParameter
        Set: Unique(self: SelectObjectCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: SelectObjectCommand) -> SwitchParameter
        Set: Wait(self: SelectObjectCommand) = value
        """
        ...



class SelectStringCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SelectStringCommand() """
    @property
    def AllMatches(self) -> SwitchParameter:
        """
        Get: AllMatches(self: SelectStringCommand) -> SwitchParameter
        Set: AllMatches(self: SelectStringCommand) = value
        """
        ...

    @property
    def CaseSensitive(self) -> SwitchParameter:
        """
        Get: CaseSensitive(self: SelectStringCommand) -> SwitchParameter
        Set: CaseSensitive(self: SelectStringCommand) = value
        """
        ...

    @property
    def Context(self) -> Array:
        """
        Get: Context(self: SelectStringCommand) -> Array[int]
        Set: Context(self: SelectStringCommand) = value
        """
        ...

    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: SelectStringCommand) -> str
        Set: Encoding(self: SelectStringCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: SelectStringCommand) -> Array[str]
        Set: Exclude(self: SelectStringCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: SelectStringCommand) -> Array[str]
        Set: Include(self: SelectStringCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: SelectStringCommand) -> PSObject
        Set: InputObject(self: SelectStringCommand) = value
        """
        ...

    @property
    def List(self) -> SwitchParameter:
        """
        Get: List(self: SelectStringCommand) -> SwitchParameter
        Set: List(self: SelectStringCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SelectStringCommand) -> Array[str]
        Set: LiteralPath(self: SelectStringCommand) = value
        """
        ...

    @property
    def NotMatch(self) -> SwitchParameter:
        """
        Get: NotMatch(self: SelectStringCommand) -> SwitchParameter
        Set: NotMatch(self: SelectStringCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SelectStringCommand) -> Array[str]
        Set: Path(self: SelectStringCommand) = value
        """
        ...

    @property
    def Pattern(self) -> Array:
        """
        Get: Pattern(self: SelectStringCommand) -> Array[str]
        Set: Pattern(self: SelectStringCommand) = value
        """
        ...

    @property
    def Quiet(self) -> SwitchParameter:
        """
        Get: Quiet(self: SelectStringCommand) -> SwitchParameter
        Set: Quiet(self: SelectStringCommand) = value
        """
        ...

    @property
    def SimpleMatch(self) -> SwitchParameter:
        """
        Get: SimpleMatch(self: SelectStringCommand) -> SwitchParameter
        Set: SimpleMatch(self: SelectStringCommand) = value
        """
        ...



class SelectXmlCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SelectXmlCommand() """
    @property
    def Content(self) -> Array:
        """
        Get: Content(self: SelectXmlCommand) -> Array[str]
        Set: Content(self: SelectXmlCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SelectXmlCommand) -> Array[str]
        Set: LiteralPath(self: SelectXmlCommand) = value
        """
        ...

    @property
    def Namespace(self) -> Hashtable:
        """
        Get: Namespace(self: SelectXmlCommand) -> Hashtable
        Set: Namespace(self: SelectXmlCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SelectXmlCommand) -> Array[str]
        Set: Path(self: SelectXmlCommand) = value
        """
        ...

    @property
    def Xml(self) -> Array:
        """
        Get: Xml(self: SelectXmlCommand) -> Array[XmlNode]
        Set: Xml(self: SelectXmlCommand) = value
        """
        ...

    @property
    def XPath(self) -> str:
        """
        Get: XPath(self: SelectXmlCommand) -> str
        Set: XPath(self: SelectXmlCommand) = value
        """
        ...



class SelectXmlInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ SelectXmlInfo() """
    @property
    def Node(self) -> XmlNode:
        """
        Get: Node(self: SelectXmlInfo) -> XmlNode
        Set: Node(self: SelectXmlInfo) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: SelectXmlInfo) -> str
        Set: Path(self: SelectXmlInfo) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """
        Get: Pattern(self: SelectXmlInfo) -> str
        Set: Pattern(self: SelectXmlInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: SelectXmlInfo) -> str """
        ...


class SendAsTrustedIssuerProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ SendAsTrustedIssuerProperty() """
    @staticmethod
    def ReadSendAsTrustedIssuerProperty(cert:X509Certificate2) -> bool:
        """ ReadSendAsTrustedIssuerProperty(cert: X509Certificate2) -> bool """
        ...

    @staticmethod
    def WriteSendAsTrustedIssuerProperty(cert:X509Certificate2, certPath:str, addProperty:bool): # -> 
        """ WriteSendAsTrustedIssuerProperty(cert: X509Certificate2, certPath: str, addProperty: bool) """
        ...


class SendMailMessage(PSCmdlet): # skipped bases: <type 'object'>
    """ SendMailMessage() """
    @property
    def Attachments(self) -> Array:
        """
        Get: Attachments(self: SendMailMessage) -> Array[str]
        Set: Attachments(self: SendMailMessage) = value
        """
        ...

    @property
    def Bcc(self) -> Array:
        """
        Get: Bcc(self: SendMailMessage) -> Array[str]
        Set: Bcc(self: SendMailMessage) = value
        """
        ...

    @property
    def Body(self) -> str:
        """
        Get: Body(self: SendMailMessage) -> str
        Set: Body(self: SendMailMessage) = value
        """
        ...

    @property
    def BodyAsHtml(self) -> SwitchParameter:
        """
        Get: BodyAsHtml(self: SendMailMessage) -> SwitchParameter
        Set: BodyAsHtml(self: SendMailMessage) = value
        """
        ...

    @property
    def Cc(self) -> Array:
        """
        Get: Cc(self: SendMailMessage) -> Array[str]
        Set: Cc(self: SendMailMessage) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: SendMailMessage) -> PSCredential
        Set: Credential(self: SendMailMessage) = value
        """
        ...

    @property
    def DeliveryNotificationOption(self) -> DeliveryNotificationOptions:
        """
        Get: DeliveryNotificationOption(self: SendMailMessage) -> DeliveryNotificationOptions
        Set: DeliveryNotificationOption(self: SendMailMessage) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: SendMailMessage) -> Encoding
        Set: Encoding(self: SendMailMessage) = value
        """
        ...

    @property
    def From(self) -> str:
        """
        Get: From(self: SendMailMessage) -> str
        Set: From(self: SendMailMessage) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: SendMailMessage) -> int
        Set: Port(self: SendMailMessage) = value
        """
        ...

    @property
    def Priority(self) -> MailPriority:
        """
        Get: Priority(self: SendMailMessage) -> MailPriority
        Set: Priority(self: SendMailMessage) = value
        """
        ...

    @property
    def SmtpServer(self) -> str:
        """
        Get: SmtpServer(self: SendMailMessage) -> str
        Set: SmtpServer(self: SendMailMessage) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: SendMailMessage) -> str
        Set: Subject(self: SendMailMessage) = value
        """
        ...

    @property
    def To(self) -> Array:
        """
        Get: To(self: SendMailMessage) -> Array[str]
        Set: To(self: SendMailMessage) = value
        """
        ...

    @property
    def UseSsl(self) -> SwitchParameter:
        """
        Get: UseSsl(self: SendMailMessage) -> SwitchParameter
        Set: UseSsl(self: SendMailMessage) = value
        """
        ...



class ServerLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServerLevel, values: FullServer (4), NanoServer (1), ServerCore (2), ServerCoreWithManagementTools (3), Unknown (0) """
    FullServer: ServerLevel = ...
    NanoServer: ServerLevel = ...
    ServerCore: ServerLevel = ...
    ServerCoreWithManagementTools: ServerLevel = ...
    Unknown: ServerLevel = ...
    value__ = ...


class ServiceCommandException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServiceCommandException()
    ServiceCommandException(message: str)
    ServiceCommandException(message: str, innerException: Exception)
    """
    @property
    def ServiceName(self) -> str:
        """
        Get: ServiceName(self: ServiceCommandException) -> str
        Set: ServiceName(self: ServiceCommandException) = value
        """
        ...


    SerializeObjectState = ...


class SessionFilterState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionFilterState, values: All (0), Broken (4), Closed (3), Disconnected (2), Opened (1) """
    All: SessionFilterState = ...
    Broken: SessionFilterState = ...
    Closed: SessionFilterState = ...
    Disconnected: SessionFilterState = ...
    Opened: SessionFilterState = ...
    value__ = ...


class SessionStateProviderBaseContentReaderWriter(IContentReader, IContentWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def Dispose(self): # -> 
        """ Dispose(self: SessionStateProviderBaseContentReaderWriter) """
        ...


class SetAclCommand(SecurityDescriptorCommandsBase): # skipped bases: <type 'object'>
    """ SetAclCommand() """
    @property
    def AclObject(self) -> object:
        """
        Get: AclObject(self: SetAclCommand) -> object
        Set: AclObject(self: SetAclCommand) = value
        """
        ...

    @property
    def CentralAccessPolicy(self) -> str:
        """
        Get: CentralAccessPolicy(self: SetAclCommand) -> str
        Set: CentralAccessPolicy(self: SetAclCommand) = value
        """
        ...

    @property
    def ClearCentralAccessPolicy(self) -> SwitchParameter:
        """
        Get: ClearCentralAccessPolicy(self: SetAclCommand) -> SwitchParameter
        Set: ClearCentralAccessPolicy(self: SetAclCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: SetAclCommand) -> PSObject
        Set: InputObject(self: SetAclCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SetAclCommand) -> Array[str]
        Set: LiteralPath(self: SetAclCommand) = value
        """
        ...

    @property
    def Passthru(self) -> SwitchParameter:
        """
        Get: Passthru(self: SetAclCommand) -> SwitchParameter
        Set: Passthru(self: SetAclCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SetAclCommand) -> Array[str]
        Set: Path(self: SetAclCommand) = value
        """
        ...



class SetAliasCommand(WriteAliasCommandBase): # skipped bases: <type 'object'>
    """ SetAliasCommand() """
    pass

class SetAuthenticodeSignatureCommand(SignatureCommandsBase): # skipped bases: <type 'object'>
    """ SetAuthenticodeSignatureCommand() """
    @property
    def Certificate(self) -> X509Certificate2:
        """
        Get: Certificate(self: SetAuthenticodeSignatureCommand) -> X509Certificate2
        Set: Certificate(self: SetAuthenticodeSignatureCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetAuthenticodeSignatureCommand) -> SwitchParameter
        Set: Force(self: SetAuthenticodeSignatureCommand) = value
        """
        ...

    @property
    def HashAlgorithm(self) -> str:
        """
        Get: HashAlgorithm(self: SetAuthenticodeSignatureCommand) -> str
        Set: HashAlgorithm(self: SetAuthenticodeSignatureCommand) = value
        """
        ...

    @property
    def IncludeChain(self) -> str:
        """
        Get: IncludeChain(self: SetAuthenticodeSignatureCommand) -> str
        Set: IncludeChain(self: SetAuthenticodeSignatureCommand) = value
        """
        ...

    @property
    def TimestampServer(self) -> str:
        """
        Get: TimestampServer(self: SetAuthenticodeSignatureCommand) -> str
        Set: TimestampServer(self: SetAuthenticodeSignatureCommand) = value
        """
        ...



class SetClipboardCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetClipboardCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: SetClipboardCommand) -> SwitchParameter
        Set: Append(self: SetClipboardCommand) = value
        """
        ...

    @property
    def AsHtml(self) -> SwitchParameter:
        """
        Get: AsHtml(self: SetClipboardCommand) -> SwitchParameter
        Set: AsHtml(self: SetClipboardCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SetClipboardCommand) -> Array[str]
        Set: LiteralPath(self: SetClipboardCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SetClipboardCommand) -> Array[str]
        Set: Path(self: SetClipboardCommand) = value
        """
        ...

    @property
    def Value(self) -> Array:
        """
        Get: Value(self: SetClipboardCommand) -> Array[str]
        Set: Value(self: SetClipboardCommand) = value
        """
        ...



class SetContentCommand(WriteContentCommandBase): # skipped bases: <type 'IDisposable'>, <type 'IDynamicParameters'>, <type 'object'>
    """ SetContentCommand() """
    pass

class SetDateCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetDateCommand() """
    @property
    def Adjust(self) -> TimeSpan:
        """
        Get: Adjust(self: SetDateCommand) -> TimeSpan
        Set: Adjust(self: SetDateCommand) = value
        """
        ...

    @property
    def Date(self) -> DateTime:
        """
        Get: Date(self: SetDateCommand) -> DateTime
        Set: Date(self: SetDateCommand) = value
        """
        ...

    @property
    def DisplayHint(self) -> DisplayHintType:
        """
        Get: DisplayHint(self: SetDateCommand) -> DisplayHintType
        Set: DisplayHint(self: SetDateCommand) = value
        """
        ...



class SetExecutionPolicyCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetExecutionPolicyCommand() """
    @property
    def ExecutionPolicy(self) -> ExecutionPolicy:
        """
        Get: ExecutionPolicy(self: SetExecutionPolicyCommand) -> ExecutionPolicy
        Set: ExecutionPolicy(self: SetExecutionPolicyCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetExecutionPolicyCommand) -> SwitchParameter
        Set: Force(self: SetExecutionPolicyCommand) = value
        """
        ...

    @property
    def Scope(self) -> ExecutionPolicyScope:
        """
        Get: Scope(self: SetExecutionPolicyCommand) -> ExecutionPolicyScope
        Set: Scope(self: SetExecutionPolicyCommand) = value
        """
        ...



class SetItemCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ SetItemCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: SetItemCommand) -> Array[str]
        Set: Exclude(self: SetItemCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: SetItemCommand) -> str
        Set: Filter(self: SetItemCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetItemCommand) -> SwitchParameter
        Set: Force(self: SetItemCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: SetItemCommand) -> Array[str]
        Set: Include(self: SetItemCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SetItemCommand) -> Array[str]
        Set: LiteralPath(self: SetItemCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: SetItemCommand) -> SwitchParameter
        Set: PassThru(self: SetItemCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SetItemCommand) -> Array[str]
        Set: Path(self: SetItemCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: SetItemCommand) -> object
        Set: Value(self: SetItemCommand) = value
        """
        ...



class SetItemPropertyCommand(PassThroughItemPropertyCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ SetItemPropertyCommand() """
    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: SetItemPropertyCommand) -> PSObject
        Set: InputObject(self: SetItemPropertyCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SetItemPropertyCommand) -> Array[str]
        Set: LiteralPath(self: SetItemPropertyCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SetItemPropertyCommand) -> str
        Set: Name(self: SetItemPropertyCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SetItemPropertyCommand) -> Array[str]
        Set: Path(self: SetItemPropertyCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: SetItemPropertyCommand) -> object
        Set: Value(self: SetItemPropertyCommand) = value
        """
        ...



class SetLocationCommand(CoreCommandBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ SetLocationCommand() """
    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: SetLocationCommand) -> str
        Set: LiteralPath(self: SetLocationCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: SetLocationCommand) -> SwitchParameter
        Set: PassThru(self: SetLocationCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: SetLocationCommand) -> str
        Set: Path(self: SetLocationCommand) = value
        """
        ...

    @property
    def StackName(self) -> str:
        """
        Get: StackName(self: SetLocationCommand) -> str
        Set: StackName(self: SetLocationCommand) = value
        """
        ...



class SetPSBreakpointCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetPSBreakpointCommand() """
    @property
    def Action(self) -> ScriptBlock:
        """
        Get: Action(self: SetPSBreakpointCommand) -> ScriptBlock
        Set: Action(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Column(self) -> int:
        """
        Get: Column(self: SetPSBreakpointCommand) -> int
        Set: Column(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Command(self) -> Array:
        """
        Get: Command(self: SetPSBreakpointCommand) -> Array[str]
        Set: Command(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Line(self) -> Array:
        """
        Get: Line(self: SetPSBreakpointCommand) -> Array[int]
        Set: Line(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Mode(self) -> VariableAccessMode:
        """
        Get: Mode(self: SetPSBreakpointCommand) -> VariableAccessMode
        Set: Mode(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Script(self) -> Array:
        """
        Get: Script(self: SetPSBreakpointCommand) -> Array[str]
        Set: Script(self: SetPSBreakpointCommand) = value
        """
        ...

    @property
    def Variable(self) -> Array:
        """
        Get: Variable(self: SetPSBreakpointCommand) -> Array[str]
        Set: Variable(self: SetPSBreakpointCommand) = value
        """
        ...



class SetPSDebugCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetPSDebugCommand() """
    @property
    def Off(self) -> SwitchParameter:
        """
        Get: Off(self: SetPSDebugCommand) -> SwitchParameter
        Set: Off(self: SetPSDebugCommand) = value
        """
        ...

    @property
    def Step(self) -> SwitchParameter:
        """
        Get: Step(self: SetPSDebugCommand) -> SwitchParameter
        Set: Step(self: SetPSDebugCommand) = value
        """
        ...

    @property
    def Strict(self) -> SwitchParameter:
        """
        Get: Strict(self: SetPSDebugCommand) -> SwitchParameter
        Set: Strict(self: SetPSDebugCommand) = value
        """
        ...

    @property
    def Trace(self) -> int:
        """
        Get: Trace(self: SetPSDebugCommand) -> int
        Set: Trace(self: SetPSDebugCommand) = value
        """
        ...



class SetPSSessionConfigurationCommand(PSSessionConfigurationCommandBase): # skipped bases: <type 'object'>
    """ SetPSSessionConfigurationCommand() """
    pass

class SetServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ SetServiceCommand() """
    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: SetServiceCommand) -> Array[str]
        Set: ComputerName(self: SetServiceCommand) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: SetServiceCommand) -> str
        Set: Description(self: SetServiceCommand) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: SetServiceCommand) -> str
        Set: DisplayName(self: SetServiceCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: SetServiceCommand) -> Array[str]
        Set: Exclude(self: SetServiceCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: SetServiceCommand) -> Array[str]
        Set: Include(self: SetServiceCommand) = value
        """
        ...

    @property
    def StartupType(self) -> ServiceStartMode:
        """
        Get: StartupType(self: SetServiceCommand) -> ServiceStartMode
        Set: StartupType(self: SetServiceCommand) = value
        """
        ...

    @property
    def Status(self) -> str:
        """
        Get: Status(self: SetServiceCommand) -> str
        Set: Status(self: SetServiceCommand) = value
        """
        ...



class SetStrictModeCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetStrictModeCommand() """
    @property
    def Off(self) -> SwitchParameter:
        """
        Get: Off(self: SetStrictModeCommand) -> SwitchParameter
        Set: Off(self: SetStrictModeCommand) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: SetStrictModeCommand) -> Version
        Set: Version(self: SetStrictModeCommand) = value
        """
        ...



class SetTimeZoneCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ SetTimeZoneCommand() """
    @property
    def HasAccess(self):
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SetTimeZoneCommand) -> str
        Set: Id(self: SetTimeZoneCommand) = value
        """
        ...

    @property
    def InputObject(self) -> TimeZoneInfo:
        """
        Get: InputObject(self: SetTimeZoneCommand) -> TimeZoneInfo
        Set: InputObject(self: SetTimeZoneCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SetTimeZoneCommand) -> str
        Set: Name(self: SetTimeZoneCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: SetTimeZoneCommand) -> SwitchParameter
        Set: PassThru(self: SetTimeZoneCommand) = value
        """
        ...


    def SetAccessToken(self, *args): #cannot find CLR method
        """ SetAccessToken(self: SetTimeZoneCommand, enable: bool) """
        ...

    def ThrowWin32Error(self, *args): #cannot find CLR method
        """ ThrowWin32Error(self: SetTimeZoneCommand) """
        ...


class TraceListenerCommandBase(TraceCommandBase): # skipped bases: <type 'object'>
    """ TraceListenerCommandBase() """
    @property
    def ForceWrite(self) -> bool:
        """
        Get: ForceWrite(self: TraceListenerCommandBase) -> bool
        Set: ForceWrite(self: TraceListenerCommandBase) = value
        """
        ...


    def ClearStoredState(self, *args): #cannot find CLR method
        """ ClearStoredState(self: TraceListenerCommandBase) """
        ...


class SetTraceSourceCommand(TraceListenerCommandBase): # skipped bases: <type 'object'>
    """ SetTraceSourceCommand() """
    @property
    def Debugger(self) -> SwitchParameter:
        """
        Get: Debugger(self: SetTraceSourceCommand) -> SwitchParameter
        Set: Debugger(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: SetTraceSourceCommand) -> str
        Set: FilePath(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetTraceSourceCommand) -> SwitchParameter
        Set: Force(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def ListenerOption(self) -> TraceOptions:
        """
        Get: ListenerOption(self: SetTraceSourceCommand) -> TraceOptions
        Set: ListenerOption(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: SetTraceSourceCommand) -> Array[str]
        Set: Name(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def Option(self) -> PSTraceSourceOptions:
        """
        Get: Option(self: SetTraceSourceCommand) -> PSTraceSourceOptions
        Set: Option(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: SetTraceSourceCommand) -> SwitchParameter
        Set: PassThru(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def PSHost(self) -> SwitchParameter:
        """
        Get: PSHost(self: SetTraceSourceCommand) -> SwitchParameter
        Set: PSHost(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def RemoveFileListener(self) -> Array:
        """
        Get: RemoveFileListener(self: SetTraceSourceCommand) -> Array[str]
        Set: RemoveFileListener(self: SetTraceSourceCommand) = value
        """
        ...

    @property
    def RemoveListener(self) -> Array:
        """
        Get: RemoveListener(self: SetTraceSourceCommand) -> Array[str]
        Set: RemoveListener(self: SetTraceSourceCommand) = value
        """
        ...



class SetVariableCommand(VariableCommandBase): # skipped bases: <type 'object'>
    """ SetVariableCommand() """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: SetVariableCommand) -> str
        Set: Description(self: SetVariableCommand) = value
        """
        ...

    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: SetVariableCommand) -> Array[str]
        Set: Exclude(self: SetVariableCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetVariableCommand) -> SwitchParameter
        Set: Force(self: SetVariableCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: SetVariableCommand) -> Array[str]
        Set: Include(self: SetVariableCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: SetVariableCommand) -> Array[str]
        Set: Name(self: SetVariableCommand) = value
        """
        ...

    @property
    def Option(self) -> ScopedItemOptions:
        """
        Get: Option(self: SetVariableCommand) -> ScopedItemOptions
        Set: Option(self: SetVariableCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: SetVariableCommand) -> SwitchParameter
        Set: PassThru(self: SetVariableCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: SetVariableCommand) -> object
        Set: Value(self: SetVariableCommand) = value
        """
        ...

    @property
    def Visibility(self) -> SessionStateEntryVisibility:
        """
        Get: Visibility(self: SetVariableCommand) -> SessionStateEntryVisibility
        Set: Visibility(self: SetVariableCommand) = value
        """
        ...



class SetWmiInstance(WmiBaseCmdlet): # skipped bases: <type 'object'>
    """ SetWmiInstance() """
    @property
    def Arguments(self) -> Hashtable:
        """
        Get: Arguments(self: SetWmiInstance) -> Hashtable
        Set: Arguments(self: SetWmiInstance) = value
        """
        ...

    @property
    def Class(self) -> str:
        """
        Get: Class(self: SetWmiInstance) -> str
        Set: Class(self: SetWmiInstance) = value
        """
        ...

    @property
    def InputObject(self) -> ManagementObject:
        """
        Get: InputObject(self: SetWmiInstance) -> ManagementObject
        Set: InputObject(self: SetWmiInstance) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: SetWmiInstance) -> str
        Set: Path(self: SetWmiInstance) = value
        """
        ...

    @property
    def PutType(self) -> PutType:
        """
        Get: PutType(self: SetWmiInstance) -> PutType
        Set: PutType(self: SetWmiInstance) = value
        """
        ...



class ShowCommandCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ ShowCommandCommand() """
    @property
    def ErrorPopup(self) -> SwitchParameter:
        """
        Get: ErrorPopup(self: ShowCommandCommand) -> SwitchParameter
        Set: ErrorPopup(self: ShowCommandCommand) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: ShowCommandCommand) -> float
        Set: Height(self: ShowCommandCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ShowCommandCommand) -> str
        Set: Name(self: ShowCommandCommand) = value
        """
        ...

    @property
    def NoCommonParameter(self) -> SwitchParameter:
        """
        Get: NoCommonParameter(self: ShowCommandCommand) -> SwitchParameter
        Set: NoCommonParameter(self: ShowCommandCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: ShowCommandCommand) -> SwitchParameter
        Set: PassThru(self: ShowCommandCommand) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: ShowCommandCommand) -> float
        Set: Width(self: ShowCommandCommand) = value
        """
        ...


    def RunScript(self, script:str): # -> 
        """ RunScript(self: ShowCommandCommand, script: str) """
        ...


class ShowControlPanelItemCommand(ControlPanelItemBaseCommand): # skipped bases: <type 'object'>
    """ ShowControlPanelItemCommand() """
    @property
    def CanonicalName(self) -> Array:
        """
        Get: CanonicalName(self: ShowControlPanelItemCommand) -> Array[str]
        Set: CanonicalName(self: ShowControlPanelItemCommand) = value
        """
        ...

    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: ShowControlPanelItemCommand) -> Array[ControlPanelItem]
        Set: InputObject(self: ShowControlPanelItemCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: ShowControlPanelItemCommand) -> Array[str]
        Set: Name(self: ShowControlPanelItemCommand) = value
        """
        ...



class ShowEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ShowEventLogCommand() """
    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: ShowEventLogCommand) -> str
        Set: ComputerName(self: ShowEventLogCommand) = value
        """
        ...



class SoftwareElementState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoftwareElementState, values: Deployable (0), Executable (2), Installable (1), Running (3) """
    Deployable: SoftwareElementState = ...
    Executable: SoftwareElementState = ...
    Installable: SoftwareElementState = ...
    Running: SoftwareElementState = ...
    value__ = ...


class SortObjectCommand(OrderObjectBase): # skipped bases: <type 'object'>
    """ SortObjectCommand() """
    @property
    def Descending(self) -> SwitchParameter:
        """
        Get: Descending(self: SortObjectCommand) -> SwitchParameter
        Set: Descending(self: SortObjectCommand) = value
        """
        ...

    @property
    def Unique(self) -> SwitchParameter:
        """
        Get: Unique(self: SortObjectCommand) -> SwitchParameter
        Set: Unique(self: SortObjectCommand) = value
        """
        ...



class SplitPathCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ SplitPathCommand() """
    @property
    def IsAbsolute(self) -> SwitchParameter:
        """
        Get: IsAbsolute(self: SplitPathCommand) -> SwitchParameter
        Set: IsAbsolute(self: SplitPathCommand) = value
        """
        ...

    @property
    def Leaf(self) -> SwitchParameter:
        """
        Get: Leaf(self: SplitPathCommand) -> SwitchParameter
        Set: Leaf(self: SplitPathCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: SplitPathCommand) -> Array[str]
        Set: LiteralPath(self: SplitPathCommand) = value
        """
        ...

    @property
    def NoQualifier(self) -> SwitchParameter:
        """
        Get: NoQualifier(self: SplitPathCommand) -> SwitchParameter
        Set: NoQualifier(self: SplitPathCommand) = value
        """
        ...

    @property
    def Parent(self) -> SwitchParameter:
        """
        Get: Parent(self: SplitPathCommand) -> SwitchParameter
        Set: Parent(self: SplitPathCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: SplitPathCommand) -> Array[str]
        Set: Path(self: SplitPathCommand) = value
        """
        ...

    @property
    def Qualifier(self) -> SwitchParameter:
        """
        Get: Qualifier(self: SplitPathCommand) -> SwitchParameter
        Set: Qualifier(self: SplitPathCommand) = value
        """
        ...

    @property
    def Resolve(self) -> SwitchParameter:
        """
        Get: Resolve(self: SplitPathCommand) -> SwitchParameter
        Set: Resolve(self: SplitPathCommand) = value
        """
        ...



class StartJobCommand(IDisposable, PSExecutionCmdlet): # skipped bases: <type 'object'>
    """ StartJobCommand() """
    @property
    def AllowRedirection(self) -> SwitchParameter:
        """ Get: AllowRedirection(self: StartJobCommand) -> SwitchParameter """
        ...

    @property
    def ApplicationName(self) -> str:
        """ Get: ApplicationName(self: StartJobCommand) -> str """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: StartJobCommand) -> AuthenticationMechanism
        Set: Authentication(self: StartJobCommand) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: StartJobCommand) -> str
        Set: CertificateThumbprint(self: StartJobCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """ Get: ComputerName(self: StartJobCommand) -> Array[str] """
        ...

    @property
    def ConnectionUri(self) -> Array:
        """ Get: ConnectionUri(self: StartJobCommand) -> Array[Uri] """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: StartJobCommand) -> PSCredential
        Set: Credential(self: StartJobCommand) = value
        """
        ...

    @property
    def DefinitionName(self) -> str:
        """
        Get: DefinitionName(self: StartJobCommand) -> str
        Set: DefinitionName(self: StartJobCommand) = value
        """
        ...

    @property
    def DefinitionPath(self) -> str:
        """
        Get: DefinitionPath(self: StartJobCommand) -> str
        Set: DefinitionPath(self: StartJobCommand) = value
        """
        ...

    @property
    def InitializationScript(self) -> ScriptBlock:
        """
        Get: InitializationScript(self: StartJobCommand) -> ScriptBlock
        Set: InitializationScript(self: StartJobCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: StartJobCommand) -> str
        Set: LiteralPath(self: StartJobCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: StartJobCommand) -> str
        Set: Name(self: StartJobCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """ Get: Port(self: StartJobCommand) -> int """
        ...

    @property
    def PSVersion(self) -> Version:
        """
        Get: PSVersion(self: StartJobCommand) -> Version
        Set: PSVersion(self: StartJobCommand) = value
        """
        ...

    @property
    def RunAs32(self) -> SwitchParameter:
        """
        Get: RunAs32(self: StartJobCommand) -> SwitchParameter
        Set: RunAs32(self: StartJobCommand) = value
        """
        ...

    @property
    def RunAsAdministrator(self) -> SwitchParameter:
        """ Get: RunAsAdministrator(self: StartJobCommand) -> SwitchParameter """
        ...

    @property
    def Session(self) -> Array:
        """ Get: Session(self: StartJobCommand) -> Array[PSSession] """
        ...

    @property
    def SessionOption(self) -> PSSessionOption:
        """
        Get: SessionOption(self: StartJobCommand) -> PSSessionOption
        Set: SessionOption(self: StartJobCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """ Get: ThrottleLimit(self: StartJobCommand) -> int """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: StartJobCommand) -> str
        Set: Type(self: StartJobCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """ Get: UseSSL(self: StartJobCommand) -> SwitchParameter """
        ...



class StartProcessCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ StartProcessCommand() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: StartProcessCommand) -> Array[str]
        Set: ArgumentList(self: StartProcessCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: StartProcessCommand) -> PSCredential
        Set: Credential(self: StartProcessCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: StartProcessCommand) -> str
        Set: FilePath(self: StartProcessCommand) = value
        """
        ...

    @property
    def LoadUserProfile(self) -> SwitchParameter:
        """
        Get: LoadUserProfile(self: StartProcessCommand) -> SwitchParameter
        Set: LoadUserProfile(self: StartProcessCommand) = value
        """
        ...

    @property
    def NoNewWindow(self) -> SwitchParameter:
        """
        Get: NoNewWindow(self: StartProcessCommand) -> SwitchParameter
        Set: NoNewWindow(self: StartProcessCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: StartProcessCommand) -> SwitchParameter
        Set: PassThru(self: StartProcessCommand) = value
        """
        ...

    @property
    def RedirectStandardError(self) -> str:
        """
        Get: RedirectStandardError(self: StartProcessCommand) -> str
        Set: RedirectStandardError(self: StartProcessCommand) = value
        """
        ...

    @property
    def RedirectStandardInput(self) -> str:
        """
        Get: RedirectStandardInput(self: StartProcessCommand) -> str
        Set: RedirectStandardInput(self: StartProcessCommand) = value
        """
        ...

    @property
    def RedirectStandardOutput(self) -> str:
        """
        Get: RedirectStandardOutput(self: StartProcessCommand) -> str
        Set: RedirectStandardOutput(self: StartProcessCommand) = value
        """
        ...

    @property
    def UseNewEnvironment(self) -> SwitchParameter:
        """
        Get: UseNewEnvironment(self: StartProcessCommand) -> SwitchParameter
        Set: UseNewEnvironment(self: StartProcessCommand) = value
        """
        ...

    @property
    def Verb(self) -> str:
        """
        Get: Verb(self: StartProcessCommand) -> str
        Set: Verb(self: StartProcessCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: StartProcessCommand) -> SwitchParameter
        Set: Wait(self: StartProcessCommand) = value
        """
        ...

    @property
    def WindowStyle(self) -> ProcessWindowStyle:
        """
        Get: WindowStyle(self: StartProcessCommand) -> ProcessWindowStyle
        Set: WindowStyle(self: StartProcessCommand) = value
        """
        ...

    @property
    def WorkingDirectory(self) -> str:
        """
        Get: WorkingDirectory(self: StartProcessCommand) -> str
        Set: WorkingDirectory(self: StartProcessCommand) = value
        """
        ...



class StartServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ StartServiceCommand() """
    pass

class StartSleepCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ StartSleepCommand() """
    @property
    def Milliseconds(self) -> int:
        """
        Get: Milliseconds(self: StartSleepCommand) -> int
        Set: Milliseconds(self: StartSleepCommand) = value
        """
        ...

    @property
    def Seconds(self) -> int:
        """
        Get: Seconds(self: StartSleepCommand) -> int
        Set: Seconds(self: StartSleepCommand) = value
        """
        ...



class StartTransactionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ StartTransactionCommand() """
    @property
    def Independent(self) -> SwitchParameter:
        """
        Get: Independent(self: StartTransactionCommand) -> SwitchParameter
        Set: Independent(self: StartTransactionCommand) = value
        """
        ...

    @property
    def RollbackPreference(self) -> RollbackSeverity:
        """
        Get: RollbackPreference(self: StartTransactionCommand) -> RollbackSeverity
        Set: RollbackPreference(self: StartTransactionCommand) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: StartTransactionCommand) -> int
        Set: Timeout(self: StartTransactionCommand) = value
        """
        ...



class StartTranscriptCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ StartTranscriptCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: StartTranscriptCommand) -> SwitchParameter
        Set: Append(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: StartTranscriptCommand) -> SwitchParameter
        Set: Force(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def IncludeInvocationHeader(self) -> SwitchParameter:
        """
        Get: IncludeInvocationHeader(self: StartTranscriptCommand) -> SwitchParameter
        Set: IncludeInvocationHeader(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: StartTranscriptCommand) -> str
        Set: LiteralPath(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def NoClobber(self) -> SwitchParameter:
        """
        Get: NoClobber(self: StartTranscriptCommand) -> SwitchParameter
        Set: NoClobber(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def OutputDirectory(self) -> str:
        """
        Get: OutputDirectory(self: StartTranscriptCommand) -> str
        Set: OutputDirectory(self: StartTranscriptCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: StartTranscriptCommand) -> str
        Set: Path(self: StartTranscriptCommand) = value
        """
        ...



class StopComputerCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ StopComputerCommand() """
    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: StopComputerCommand) -> SwitchParameter
        Set: AsJob(self: StopComputerCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: StopComputerCommand) -> Array[str]
        Set: ComputerName(self: StopComputerCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: StopComputerCommand) -> PSCredential
        Set: Credential(self: StopComputerCommand) = value
        """
        ...

    @property
    def DcomAuthentication(self) -> AuthenticationLevel:
        """
        Get: DcomAuthentication(self: StopComputerCommand) -> AuthenticationLevel
        Set: DcomAuthentication(self: StopComputerCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: StopComputerCommand) -> SwitchParameter
        Set: Force(self: StopComputerCommand) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationLevel:
        """
        Get: Impersonation(self: StopComputerCommand) -> ImpersonationLevel
        Set: Impersonation(self: StopComputerCommand) = value
        """
        ...

    @property
    def Protocol(self) -> str:
        """
        Get: Protocol(self: StopComputerCommand) -> str
        Set: Protocol(self: StopComputerCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: StopComputerCommand) -> int
        Set: ThrottleLimit(self: StopComputerCommand) = value
        """
        ...

    @property
    def WsmanAuthentication(self) -> str:
        """
        Get: WsmanAuthentication(self: StopComputerCommand) -> str
        Set: WsmanAuthentication(self: StopComputerCommand) = value
        """
        ...



class StopJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ StopJobCommand() """
    @property
    def Job(self) -> Array:
        """
        Get: Job(self: StopJobCommand) -> Array[Job]
        Set: Job(self: StopJobCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: StopJobCommand) -> SwitchParameter
        Set: PassThru(self: StopJobCommand) = value
        """
        ...



class StopProcessCommand(ProcessBaseCommand): # skipped bases: <type 'object'>
    """ StopProcessCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: StopProcessCommand) -> SwitchParameter
        Set: Force(self: StopProcessCommand) = value
        """
        ...

    @property
    def Id(self) -> Array:
        """
        Get: Id(self: StopProcessCommand) -> Array[int]
        Set: Id(self: StopProcessCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: StopProcessCommand) -> Array[str]
        Set: Name(self: StopProcessCommand) = value
        """
        ...

    @property
    def PassThru(self) -> SwitchParameter:
        """
        Get: PassThru(self: StopProcessCommand) -> SwitchParameter
        Set: PassThru(self: StopProcessCommand) = value
        """
        ...



class StopServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ StopServiceCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: StopServiceCommand) -> SwitchParameter
        Set: Force(self: StopServiceCommand) = value
        """
        ...

    @property
    def NoWait(self) -> SwitchParameter:
        """
        Get: NoWait(self: StopServiceCommand) -> SwitchParameter
        Set: NoWait(self: StopServiceCommand) = value
        """
        ...



class StopTranscriptCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ StopTranscriptCommand() """
    pass

class SuspendJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ SuspendJobCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SuspendJobCommand) -> SwitchParameter
        Set: Force(self: SuspendJobCommand) = value
        """
        ...

    @property
    def Job(self) -> Array:
        """
        Get: Job(self: SuspendJobCommand) -> Array[Job]
        Set: Job(self: SuspendJobCommand) = value
        """
        ...

    @property
    def Wait(self) -> SwitchParameter:
        """
        Get: Wait(self: SuspendJobCommand) -> SwitchParameter
        Set: Wait(self: SuspendJobCommand) = value
        """
        ...



class SuspendServiceCommand(ServiceOperationBaseCommand): # skipped bases: <type 'object'>
    """ SuspendServiceCommand() """
    pass

class SystemElementState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SystemElementState, values: Critical (5), NonRecoverable (6), Other (1), Safe (3), Unknown (2), Warning (4) """
    Critical: SystemElementState = ...
    NonRecoverable: SystemElementState = ...
    Other: SystemElementState = ...
    Safe: SystemElementState = ...
    Unknown: SystemElementState = ...
    value__ = ...
    Warning: SystemElementState = ...


class TeeObjectCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ TeeObjectCommand() """
    @property
    def Append(self) -> SwitchParameter:
        """
        Get: Append(self: TeeObjectCommand) -> SwitchParameter
        Set: Append(self: TeeObjectCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: TeeObjectCommand) -> str
        Set: FilePath(self: TeeObjectCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: TeeObjectCommand) -> PSObject
        Set: InputObject(self: TeeObjectCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: TeeObjectCommand) -> str
        Set: LiteralPath(self: TeeObjectCommand) = value
        """
        ...

    @property
    def Variable(self) -> str:
        """
        Get: Variable(self: TeeObjectCommand) -> str
        Set: Variable(self: TeeObjectCommand) = value
        """
        ...



class TestComputerSecureChannelCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ TestComputerSecureChannelCommand() """
    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: TestComputerSecureChannelCommand) -> PSCredential
        Set: Credential(self: TestComputerSecureChannelCommand) = value
        """
        ...

    @property
    def Repair(self) -> SwitchParameter:
        """
        Get: Repair(self: TestComputerSecureChannelCommand) -> SwitchParameter
        Set: Repair(self: TestComputerSecureChannelCommand) = value
        """
        ...

    @property
    def Server(self) -> str:
        """
        Get: Server(self: TestComputerSecureChannelCommand) -> str
        Set: Server(self: TestComputerSecureChannelCommand) = value
        """
        ...



class TestConnectionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ TestConnectionCommand() """
    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: TestConnectionCommand) -> SwitchParameter
        Set: AsJob(self: TestConnectionCommand) = value
        """
        ...

    @property
    def BufferSize(self) -> int:
        """
        Get: BufferSize(self: TestConnectionCommand) -> int
        Set: BufferSize(self: TestConnectionCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> Array:
        """
        Get: ComputerName(self: TestConnectionCommand) -> Array[str]
        Set: ComputerName(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Count(self) -> int:
        """
        Get: Count(self: TestConnectionCommand) -> int
        Set: Count(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: TestConnectionCommand) -> PSCredential
        Set: Credential(self: TestConnectionCommand) = value
        """
        ...

    @property
    def DcomAuthentication(self) -> AuthenticationLevel:
        """
        Get: DcomAuthentication(self: TestConnectionCommand) -> AuthenticationLevel
        Set: DcomAuthentication(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Delay(self) -> int:
        """
        Get: Delay(self: TestConnectionCommand) -> int
        Set: Delay(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationLevel:
        """
        Get: Impersonation(self: TestConnectionCommand) -> ImpersonationLevel
        Set: Impersonation(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Protocol(self) -> str:
        """
        Get: Protocol(self: TestConnectionCommand) -> str
        Set: Protocol(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Quiet(self) -> SwitchParameter:
        """
        Get: Quiet(self: TestConnectionCommand) -> SwitchParameter
        Set: Quiet(self: TestConnectionCommand) = value
        """
        ...

    @property
    def Source(self) -> Array:
        """
        Get: Source(self: TestConnectionCommand) -> Array[str]
        Set: Source(self: TestConnectionCommand) = value
        """
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: TestConnectionCommand) -> int
        Set: ThrottleLimit(self: TestConnectionCommand) = value
        """
        ...

    @property
    def TimeToLive(self) -> int:
        """
        Get: TimeToLive(self: TestConnectionCommand) -> int
        Set: TimeToLive(self: TestConnectionCommand) = value
        """
        ...

    @property
    def WsmanAuthentication(self) -> str:
        """
        Get: WsmanAuthentication(self: TestConnectionCommand) -> str
        Set: WsmanAuthentication(self: TestConnectionCommand) = value
        """
        ...



class TestFileCatalogCommand(CatalogCommandsBase): # skipped bases: <type 'object'>
    """ TestFileCatalogCommand() """
    @property
    def Detailed(self) -> SwitchParameter:
        """
        Get: Detailed(self: TestFileCatalogCommand) -> SwitchParameter
        Set: Detailed(self: TestFileCatalogCommand) = value
        """
        ...

    @property
    def FilesToSkip(self) -> Array:
        """
        Get: FilesToSkip(self: TestFileCatalogCommand) -> Array[str]
        Set: FilesToSkip(self: TestFileCatalogCommand) = value
        """
        ...



class TestModuleManifestCommand(ModuleCmdletBase): # skipped bases: <type 'object'>
    """ TestModuleManifestCommand() """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: TestModuleManifestCommand) -> str
        Set: Path(self: TestModuleManifestCommand) = value
        """
        ...



class TestPathCommand(CoreCommandWithCredentialsBase): # skipped bases: <type 'IDynamicParameters'>, <type 'object'>
    """ TestPathCommand() """
    @property
    def Exclude(self) -> Array:
        """
        Get: Exclude(self: TestPathCommand) -> Array[str]
        Set: Exclude(self: TestPathCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: TestPathCommand) -> str
        Set: Filter(self: TestPathCommand) = value
        """
        ...

    @property
    def Include(self) -> Array:
        """
        Get: Include(self: TestPathCommand) -> Array[str]
        Set: Include(self: TestPathCommand) = value
        """
        ...

    @property
    def IsValid(self) -> SwitchParameter:
        """
        Get: IsValid(self: TestPathCommand) -> SwitchParameter
        Set: IsValid(self: TestPathCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: TestPathCommand) -> Array[str]
        Set: LiteralPath(self: TestPathCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: TestPathCommand) -> Array[str]
        Set: Path(self: TestPathCommand) = value
        """
        ...

    @property
    def PathType(self): # -> TestPathType
        """
        Get: PathType(self: TestPathCommand) -> TestPathType
        Set: PathType(self: TestPathCommand) = value
        """
        ...



class TestPathType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TestPathType, values: Any (0), Container (1), Leaf (2) """
    Any: TestPathType = ...
    Container: TestPathType = ...
    Leaf: TestPathType = ...
    value__ = ...


class TestPSSessionConfigurationFileCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ TestPSSessionConfigurationFileCommand() """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: TestPSSessionConfigurationFileCommand) -> str
        Set: Path(self: TestPSSessionConfigurationFileCommand) = value
        """
        ...



class TextEncodingType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextEncodingType, values: Ascii (7), BigEndianUnicode (4), Byte (3), String (1), Unicode (2), Unknown (0), Utf7 (6), Utf8 (5) """
    Ascii: TextEncodingType = ...
    BigEndianUnicode: TextEncodingType = ...
    Byte: TextEncodingType = ...
    String: TextEncodingType = ...
    Unicode: TextEncodingType = ...
    Unknown: TextEncodingType = ...
    Utf7: TextEncodingType = ...
    Utf8: TextEncodingType = ...
    value__ = ...


class TextMeasureInfo(MeasureInfo): # skipped bases: <type 'object'>
    """ TextMeasureInfo() """
    @property
    def Characters(self) -> Nullable:
        """
        Get: Characters(self: TextMeasureInfo) -> Nullable[int]
        Set: Characters(self: TextMeasureInfo) = value
        """
        ...

    @property
    def Lines(self) -> Nullable:
        """
        Get: Lines(self: TextMeasureInfo) -> Nullable[int]
        Set: Lines(self: TextMeasureInfo) = value
        """
        ...

    @property
    def Words(self) -> Nullable:
        """
        Get: Words(self: TextMeasureInfo) -> Nullable[int]
        Set: Words(self: TextMeasureInfo) = value
        """
        ...



class TraceCommandCommand(IDisposable, TraceListenerCommandBase): # skipped bases: <type 'object'>
    """ TraceCommandCommand() """
    @property
    def ArgumentList(self) -> Array:
        """
        Get: ArgumentList(self: TraceCommandCommand) -> Array[object]
        Set: ArgumentList(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Command(self) -> str:
        """
        Get: Command(self: TraceCommandCommand) -> str
        Set: Command(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Debugger(self) -> SwitchParameter:
        """
        Get: Debugger(self: TraceCommandCommand) -> SwitchParameter
        Set: Debugger(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Expression(self) -> ScriptBlock:
        """
        Get: Expression(self: TraceCommandCommand) -> ScriptBlock
        Set: Expression(self: TraceCommandCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: TraceCommandCommand) -> str
        Set: FilePath(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: TraceCommandCommand) -> SwitchParameter
        Set: Force(self: TraceCommandCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: TraceCommandCommand) -> PSObject
        Set: InputObject(self: TraceCommandCommand) = value
        """
        ...

    @property
    def ListenerOption(self) -> TraceOptions:
        """
        Get: ListenerOption(self: TraceCommandCommand) -> TraceOptions
        Set: ListenerOption(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: TraceCommandCommand) -> Array[str]
        Set: Name(self: TraceCommandCommand) = value
        """
        ...

    @property
    def Option(self) -> PSTraceSourceOptions:
        """
        Get: Option(self: TraceCommandCommand) -> PSTraceSourceOptions
        Set: Option(self: TraceCommandCommand) = value
        """
        ...

    @property
    def PSHost(self) -> SwitchParameter:
        """
        Get: PSHost(self: TraceCommandCommand) -> SwitchParameter
        Set: PSHost(self: TraceCommandCommand) = value
        """
        ...



class UnblockFileCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UnblockFileCommand() """
    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: UnblockFileCommand) -> Array[str]
        Set: LiteralPath(self: UnblockFileCommand) = value
        """
        ...

    @property
    def Path(self) -> Array:
        """
        Get: Path(self: UnblockFileCommand) -> Array[str]
        Set: Path(self: UnblockFileCommand) = value
        """
        ...



class UndoTransactionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UndoTransactionCommand() """
    pass

class UnprotectCmsMessageCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UnprotectCmsMessageCommand() """
    @property
    def Content(self) -> str:
        """
        Get: Content(self: UnprotectCmsMessageCommand) -> str
        Set: Content(self: UnprotectCmsMessageCommand) = value
        """
        ...

    @property
    def EventLogRecord(self) -> PSObject:
        """
        Get: EventLogRecord(self: UnprotectCmsMessageCommand) -> PSObject
        Set: EventLogRecord(self: UnprotectCmsMessageCommand) = value
        """
        ...

    @property
    def IncludeContext(self) -> SwitchParameter:
        """
        Get: IncludeContext(self: UnprotectCmsMessageCommand) -> SwitchParameter
        Set: IncludeContext(self: UnprotectCmsMessageCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> str:
        """
        Get: LiteralPath(self: UnprotectCmsMessageCommand) -> str
        Set: LiteralPath(self: UnprotectCmsMessageCommand) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: UnprotectCmsMessageCommand) -> str
        Set: Path(self: UnprotectCmsMessageCommand) = value
        """
        ...

    @property
    def To(self) -> Array:
        """
        Get: To(self: UnprotectCmsMessageCommand) -> Array[CmsMessageRecipient]
        Set: To(self: UnprotectCmsMessageCommand) = value
        """
        ...



class UnregisterEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UnregisterEventCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: UnregisterEventCommand) -> SwitchParameter
        Set: Force(self: UnregisterEventCommand) = value
        """
        ...

    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: UnregisterEventCommand) -> str
        Set: SourceIdentifier(self: UnregisterEventCommand) = value
        """
        ...

    @property
    def SubscriptionId(self) -> int:
        """
        Get: SubscriptionId(self: UnregisterEventCommand) -> int
        Set: SubscriptionId(self: UnregisterEventCommand) = value
        """
        ...



class UnregisterPSSessionConfigurationCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UnregisterPSSessionConfigurationCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: UnregisterPSSessionConfigurationCommand) -> SwitchParameter
        Set: Force(self: UnregisterPSSessionConfigurationCommand) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: UnregisterPSSessionConfigurationCommand) -> str
        Set: Name(self: UnregisterPSSessionConfigurationCommand) = value
        """
        ...

    @property
    def NoServiceRestart(self) -> SwitchParameter:
        """
        Get: NoServiceRestart(self: UnregisterPSSessionConfigurationCommand) -> SwitchParameter
        Set: NoServiceRestart(self: UnregisterPSSessionConfigurationCommand) = value
        """
        ...



class UpdateData(PSCmdlet): # skipped bases: <type 'object'>
    """ UpdateData() """
    @property
    def AppendPath(self) -> Array:
        """
        Get: AppendPath(self: UpdateData) -> Array[str]
        Set: AppendPath(self: UpdateData) = value
        """
        ...

    @property
    def PrependPath(self) -> Array:
        """
        Get: PrependPath(self: UpdateData) -> Array[str]
        Set: PrependPath(self: UpdateData) = value
        """
        ...


    FileParameterSet: str = ...


class UpdateFormatDataCommand(UpdateData): # skipped bases: <type 'object'>
    """ UpdateFormatDataCommand() """
    pass

class UpdateHelpCommand(UpdatableHelpCommandBase): # skipped bases: <type 'object'>
    """ UpdateHelpCommand() """
    @property
    def FullyQualifiedModule(self) -> Array:
        """
        Get: FullyQualifiedModule(self: UpdateHelpCommand) -> Array[ModuleSpecification]
        Set: FullyQualifiedModule(self: UpdateHelpCommand) = value
        """
        ...

    @property
    def LiteralPath(self) -> Array:
        """
        Get: LiteralPath(self: UpdateHelpCommand) -> Array[str]
        Set: LiteralPath(self: UpdateHelpCommand) = value
        """
        ...

    @property
    def Module(self) -> Array:
        """
        Get: Module(self: UpdateHelpCommand) -> Array[str]
        Set: Module(self: UpdateHelpCommand) = value
        """
        ...

    @property
    def Recurse(self) -> SwitchParameter:
        """
        Get: Recurse(self: UpdateHelpCommand) -> SwitchParameter
        Set: Recurse(self: UpdateHelpCommand) = value
        """
        ...

    @property
    def SourcePath(self) -> Array:
        """
        Get: SourcePath(self: UpdateHelpCommand) -> Array[str]
        Set: SourcePath(self: UpdateHelpCommand) = value
        """
        ...



class UpdateListCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UpdateListCommand() """
    @property
    def Add(self) -> Array:
        """
        Get: Add(self: UpdateListCommand) -> Array[object]
        Set: Add(self: UpdateListCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: UpdateListCommand) -> PSObject
        Set: InputObject(self: UpdateListCommand) = value
        """
        ...

    @property
    def Property(self) -> str:
        """
        Get: Property(self: UpdateListCommand) -> str
        Set: Property(self: UpdateListCommand) = value
        """
        ...

    @property
    def Remove(self) -> Array:
        """
        Get: Remove(self: UpdateListCommand) -> Array[object]
        Set: Remove(self: UpdateListCommand) = value
        """
        ...

    @property
    def Replace(self) -> Array:
        """
        Get: Replace(self: UpdateListCommand) -> Array[object]
        Set: Replace(self: UpdateListCommand) = value
        """
        ...



class UpdateTypeDataCommand(UpdateData): # skipped bases: <type 'object'>
    """ UpdateTypeDataCommand() """
    @property
    def DefaultDisplayProperty(self) -> str:
        """
        Get: DefaultDisplayProperty(self: UpdateTypeDataCommand) -> str
        Set: DefaultDisplayProperty(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def DefaultDisplayPropertySet(self) -> Array:
        """
        Get: DefaultDisplayPropertySet(self: UpdateTypeDataCommand) -> Array[str]
        Set: DefaultDisplayPropertySet(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def DefaultKeyPropertySet(self) -> Array:
        """
        Get: DefaultKeyPropertySet(self: UpdateTypeDataCommand) -> Array[str]
        Set: DefaultKeyPropertySet(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: UpdateTypeDataCommand) -> SwitchParameter
        Set: Force(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def InheritPropertySerializationSet(self) -> Nullable:
        """
        Get: InheritPropertySerializationSet(self: UpdateTypeDataCommand) -> Nullable[bool]
        Set: InheritPropertySerializationSet(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: UpdateTypeDataCommand) -> str
        Set: MemberName(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def MemberType(self) -> PSMemberTypes:
        """
        Get: MemberType(self: UpdateTypeDataCommand) -> PSMemberTypes
        Set: MemberType(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def PropertySerializationSet(self) -> Array:
        """
        Get: PropertySerializationSet(self: UpdateTypeDataCommand) -> Array[str]
        Set: PropertySerializationSet(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def SecondValue(self) -> object:
        """
        Get: SecondValue(self: UpdateTypeDataCommand) -> object
        Set: SecondValue(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def SerializationDepth(self) -> int:
        """
        Get: SerializationDepth(self: UpdateTypeDataCommand) -> int
        Set: SerializationDepth(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def SerializationMethod(self) -> str:
        """
        Get: SerializationMethod(self: UpdateTypeDataCommand) -> str
        Set: SerializationMethod(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def StringSerializationSource(self) -> str:
        """
        Get: StringSerializationSource(self: UpdateTypeDataCommand) -> str
        Set: StringSerializationSource(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def TargetTypeForDeserialization(self) -> Type:
        """
        Get: TargetTypeForDeserialization(self: UpdateTypeDataCommand) -> Type
        Set: TargetTypeForDeserialization(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def TypeAdapter(self) -> Type:
        """
        Get: TypeAdapter(self: UpdateTypeDataCommand) -> Type
        Set: TypeAdapter(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def TypeConverter(self) -> Type:
        """
        Get: TypeConverter(self: UpdateTypeDataCommand) -> Type
        Set: TypeConverter(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def TypeData(self) -> Array:
        """
        Get: TypeData(self: UpdateTypeDataCommand) -> Array[TypeData]
        Set: TypeData(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: UpdateTypeDataCommand) -> str
        Set: TypeName(self: UpdateTypeDataCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: UpdateTypeDataCommand) -> object
        Set: Value(self: UpdateTypeDataCommand) = value
        """
        ...



class UseTransactionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ UseTransactionCommand() """
    @property
    def TransactedScript(self) -> ScriptBlock:
        """
        Get: TransactedScript(self: UseTransactionCommand) -> ScriptBlock
        Set: TransactedScript(self: UseTransactionCommand) = value
        """
        ...



class UtilityResources: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AlgorithmTypeNotSupported(self) -> str:
        """ Get: AlgorithmTypeNotSupported() -> str """
        ...

    @property
    def CouldNotParseAsPowerShellDataFile(self) -> str:
        """ Get: CouldNotParseAsPowerShellDataFile() -> str """
        ...

    @property
    def FileReadError(self) -> str:
        """ Get: FileReadError() -> str """
        ...

    @property
    def FormatHexPathPrefix(self) -> str:
        """ Get: FormatHexPathPrefix() -> str """
        ...

    @property
    def FormatHexResolvePathError(self) -> str:
        """ Get: FormatHexResolvePathError() -> str """
        ...

    @property
    def FormatHexTypeNotSupported(self) -> str:
        """ Get: FormatHexTypeNotSupported() -> str """
        ...

    @property
    def PathDoesNotExist(self) -> str:
        """ Get: PathDoesNotExist() -> str """
        ...


    __all__: list = ...


class VariableProvider(SessionStateProviderBase): # skipped bases: <type 'IResourceSupplier'>, <type 'IContentCmdletProvider'>, <type 'object'>
    """ VariableProvider() """
    ProviderName: str = ...


class WaitDebuggerCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WaitDebuggerCommand() """
    pass

class WaitEventCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WaitEventCommand() """
    @property
    def SourceIdentifier(self) -> str:
        """
        Get: SourceIdentifier(self: WaitEventCommand) -> str
        Set: SourceIdentifier(self: WaitEventCommand) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: WaitEventCommand) -> int
        Set: Timeout(self: WaitEventCommand) = value
        """
        ...



class WaitForServiceTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WaitForServiceTypes, values: PowerShell (2), WinRM (1), Wmi (0) """
    PowerShell: WaitForServiceTypes = ...
    value__ = ...
    WinRM: WaitForServiceTypes = ...
    Wmi: WaitForServiceTypes = ...


class WaitJobCommand(JobCmdletBase, IDisposable): # skipped bases: <type 'object'>
    """ WaitJobCommand() """
    @property
    def Any(self) -> SwitchParameter:
        """
        Get: Any(self: WaitJobCommand) -> SwitchParameter
        Set: Any(self: WaitJobCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: WaitJobCommand) -> SwitchParameter
        Set: Force(self: WaitJobCommand) = value
        """
        ...

    @property
    def Job(self) -> Array:
        """
        Get: Job(self: WaitJobCommand) -> Array[Job]
        Set: Job(self: WaitJobCommand) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: WaitJobCommand) -> int
        Set: Timeout(self: WaitJobCommand) = value
        """
        ...



class WaitProcessCommand(ProcessBaseCommand): # skipped bases: <type 'object'>
    """ WaitProcessCommand() """
    @property
    def Id(self) -> Array:
        """
        Get: Id(self: WaitProcessCommand) -> Array[int]
        Set: Id(self: WaitProcessCommand) = value
        """
        ...

    @property
    def Name(self) -> Array:
        """
        Get: Name(self: WaitProcessCommand) -> Array[str]
        Set: Name(self: WaitProcessCommand) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: WaitProcessCommand) -> int
        Set: Timeout(self: WaitProcessCommand) = value
        """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: WaitProcessCommand) """
        ...


class WakeUpType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WakeUpType, values: ACPowerRestored (8), APMTimer (3), LANRemote (5), ModemRing (4), Other (1), PCIPME (7), PowerSwitch (6), Unknown (2) """
    ACPowerRestored: WakeUpType = ...
    APMTimer: WakeUpType = ...
    LANRemote: WakeUpType = ...
    ModemRing: WakeUpType = ...
    Other: WakeUpType = ...
    PCIPME: WakeUpType = ...
    PowerSwitch: WakeUpType = ...
    Unknown: WakeUpType = ...
    value__ = ...


class WebCmdletElementCollection(ReadOnlyCollection): # skipped bases: <type 'IList[PSObject]'>, <type 'IReadOnlyList[PSObject]'>, <type 'ICollection[PSObject]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[PSObject]'>, <type 'ICollection'>, <type 'IEnumerable[PSObject]'>, <type 'object'>
    """ no doc """
    def Find(self, nameOrId:str) -> PSObject:
        """ Find(self: WebCmdletElementCollection, nameOrId: str) -> PSObject """
        ...

    def FindById(self, id:str) -> PSObject:
        """ FindById(self: WebCmdletElementCollection, id: str) -> PSObject """
        ...

    def FindByName(self, name:str) -> PSObject:
        """ FindByName(self: WebCmdletElementCollection, name: str) -> PSObject """
        ...


class WebRequestMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebRequestMethod, values: Default (0), Delete (5), Get (1), Head (2), Merge (8), Options (7), Patch (9), Post (3), Put (4), Trace (6) """
    Default: WebRequestMethod = ...
    Delete: WebRequestMethod = ...
    Get: WebRequestMethod = ...
    Head: WebRequestMethod = ...
    Merge: WebRequestMethod = ...
    Options: WebRequestMethod = ...
    Patch: WebRequestMethod = ...
    Post: WebRequestMethod = ...
    Put: WebRequestMethod = ...
    Trace: WebRequestMethod = ...
    value__ = ...


class WebRequestSession: # skipped bases: <type 'object'>, <type 'object'>
    """ WebRequestSession() """
    @property
    def Certificates(self) -> X509CertificateCollection:
        """
        Get: Certificates(self: WebRequestSession) -> X509CertificateCollection
        Set: Certificates(self: WebRequestSession) = value
        """
        ...

    @property
    def Cookies(self) -> CookieContainer:
        """
        Get: Cookies(self: WebRequestSession) -> CookieContainer
        Set: Cookies(self: WebRequestSession) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: WebRequestSession) -> ICredentials
        Set: Credentials(self: WebRequestSession) = value
        """
        ...

    @property
    def Headers(self) -> Dictionary:
        """
        Get: Headers(self: WebRequestSession) -> Dictionary[str, str]
        Set: Headers(self: WebRequestSession) = value
        """
        ...

    @property
    def MaximumRedirection(self) -> int:
        """
        Get: MaximumRedirection(self: WebRequestSession) -> int
        Set: MaximumRedirection(self: WebRequestSession) = value
        """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: WebRequestSession) -> IWebProxy
        Set: Proxy(self: WebRequestSession) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: WebRequestSession) -> bool
        Set: UseDefaultCredentials(self: WebRequestSession) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: WebRequestSession) -> str
        Set: UserAgent(self: WebRequestSession) = value
        """
        ...



class WhereObjectCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WhereObjectCommand() """
    @property
    def CContains(self) -> SwitchParameter:
        """
        Get: CContains(self: WhereObjectCommand) -> SwitchParameter
        Set: CContains(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CEQ(self) -> SwitchParameter:
        """
        Get: CEQ(self: WhereObjectCommand) -> SwitchParameter
        Set: CEQ(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CGE(self) -> SwitchParameter:
        """
        Get: CGE(self: WhereObjectCommand) -> SwitchParameter
        Set: CGE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CGT(self) -> SwitchParameter:
        """
        Get: CGT(self: WhereObjectCommand) -> SwitchParameter
        Set: CGT(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CIn(self) -> SwitchParameter:
        """
        Get: CIn(self: WhereObjectCommand) -> SwitchParameter
        Set: CIn(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CLE(self) -> SwitchParameter:
        """
        Get: CLE(self: WhereObjectCommand) -> SwitchParameter
        Set: CLE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CLike(self) -> SwitchParameter:
        """
        Get: CLike(self: WhereObjectCommand) -> SwitchParameter
        Set: CLike(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CLT(self) -> SwitchParameter:
        """
        Get: CLT(self: WhereObjectCommand) -> SwitchParameter
        Set: CLT(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CMatch(self) -> SwitchParameter:
        """
        Get: CMatch(self: WhereObjectCommand) -> SwitchParameter
        Set: CMatch(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CNE(self) -> SwitchParameter:
        """
        Get: CNE(self: WhereObjectCommand) -> SwitchParameter
        Set: CNE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CNotContains(self) -> SwitchParameter:
        """
        Get: CNotContains(self: WhereObjectCommand) -> SwitchParameter
        Set: CNotContains(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CNotIn(self) -> SwitchParameter:
        """
        Get: CNotIn(self: WhereObjectCommand) -> SwitchParameter
        Set: CNotIn(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CNotLike(self) -> SwitchParameter:
        """
        Get: CNotLike(self: WhereObjectCommand) -> SwitchParameter
        Set: CNotLike(self: WhereObjectCommand) = value
        """
        ...

    @property
    def CNotMatch(self) -> SwitchParameter:
        """
        Get: CNotMatch(self: WhereObjectCommand) -> SwitchParameter
        Set: CNotMatch(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Contains(self) -> SwitchParameter:
        """
        Get: Contains(self: WhereObjectCommand) -> SwitchParameter
        Set: Contains(self: WhereObjectCommand) = value
        """
        ...

    @property
    def EQ(self) -> SwitchParameter:
        """
        Get: EQ(self: WhereObjectCommand) -> SwitchParameter
        Set: EQ(self: WhereObjectCommand) = value
        """
        ...

    @property
    def FilterScript(self) -> ScriptBlock:
        """
        Get: FilterScript(self: WhereObjectCommand) -> ScriptBlock
        Set: FilterScript(self: WhereObjectCommand) = value
        """
        ...

    @property
    def GE(self) -> SwitchParameter:
        """
        Get: GE(self: WhereObjectCommand) -> SwitchParameter
        Set: GE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def GT(self) -> SwitchParameter:
        """
        Get: GT(self: WhereObjectCommand) -> SwitchParameter
        Set: GT(self: WhereObjectCommand) = value
        """
        ...

    @property
    def In(self) -> SwitchParameter:
        """
        Get: In(self: WhereObjectCommand) -> SwitchParameter
        Set: In(self: WhereObjectCommand) = value
        """
        ...

    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: WhereObjectCommand) -> PSObject
        Set: InputObject(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Is(self) -> SwitchParameter:
        """
        Get: Is(self: WhereObjectCommand) -> SwitchParameter
        Set: Is(self: WhereObjectCommand) = value
        """
        ...

    @property
    def IsNot(self) -> SwitchParameter:
        """
        Get: IsNot(self: WhereObjectCommand) -> SwitchParameter
        Set: IsNot(self: WhereObjectCommand) = value
        """
        ...

    @property
    def LE(self) -> SwitchParameter:
        """
        Get: LE(self: WhereObjectCommand) -> SwitchParameter
        Set: LE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Like(self) -> SwitchParameter:
        """
        Get: Like(self: WhereObjectCommand) -> SwitchParameter
        Set: Like(self: WhereObjectCommand) = value
        """
        ...

    @property
    def LT(self) -> SwitchParameter:
        """
        Get: LT(self: WhereObjectCommand) -> SwitchParameter
        Set: LT(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Match(self) -> SwitchParameter:
        """
        Get: Match(self: WhereObjectCommand) -> SwitchParameter
        Set: Match(self: WhereObjectCommand) = value
        """
        ...

    @property
    def NE(self) -> SwitchParameter:
        """
        Get: NE(self: WhereObjectCommand) -> SwitchParameter
        Set: NE(self: WhereObjectCommand) = value
        """
        ...

    @property
    def NotContains(self) -> SwitchParameter:
        """
        Get: NotContains(self: WhereObjectCommand) -> SwitchParameter
        Set: NotContains(self: WhereObjectCommand) = value
        """
        ...

    @property
    def NotIn(self) -> SwitchParameter:
        """
        Get: NotIn(self: WhereObjectCommand) -> SwitchParameter
        Set: NotIn(self: WhereObjectCommand) = value
        """
        ...

    @property
    def NotLike(self) -> SwitchParameter:
        """
        Get: NotLike(self: WhereObjectCommand) -> SwitchParameter
        Set: NotLike(self: WhereObjectCommand) = value
        """
        ...

    @property
    def NotMatch(self) -> SwitchParameter:
        """
        Get: NotMatch(self: WhereObjectCommand) -> SwitchParameter
        Set: NotMatch(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Property(self) -> str:
        """
        Get: Property(self: WhereObjectCommand) -> str
        Set: Property(self: WhereObjectCommand) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: WhereObjectCommand) -> object
        Set: Value(self: WhereObjectCommand) = value
        """
        ...



class WmiState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WmiState, values: Completed (4), Failed (5), NotStarted (0), Running (1), Stopped (3), Stopping (2) """
    Completed: WmiState = ...
    Failed: WmiState = ...
    NotStarted: WmiState = ...
    Running: WmiState = ...
    Stopped: WmiState = ...
    Stopping: WmiState = ...
    value__ = ...


class WriteDebugCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteDebugCommand() """
    @property
    def Message(self) -> str:
        """
        Get: Message(self: WriteDebugCommand) -> str
        Set: Message(self: WriteDebugCommand) = value
        """
        ...



class WriteOrThrowErrorCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteOrThrowErrorCommand() """
    @property
    def Category(self) -> ErrorCategory:
        """
        Get: Category(self: WriteOrThrowErrorCommand) -> ErrorCategory
        Set: Category(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def CategoryActivity(self) -> str:
        """
        Get: CategoryActivity(self: WriteOrThrowErrorCommand) -> str
        Set: CategoryActivity(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def CategoryReason(self) -> str:
        """
        Get: CategoryReason(self: WriteOrThrowErrorCommand) -> str
        Set: CategoryReason(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def CategoryTargetName(self) -> str:
        """
        Get: CategoryTargetName(self: WriteOrThrowErrorCommand) -> str
        Set: CategoryTargetName(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def CategoryTargetType(self) -> str:
        """
        Get: CategoryTargetType(self: WriteOrThrowErrorCommand) -> str
        Set: CategoryTargetType(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def ErrorId(self) -> str:
        """
        Get: ErrorId(self: WriteOrThrowErrorCommand) -> str
        Set: ErrorId(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def ErrorRecord(self) -> ErrorRecord:
        """
        Get: ErrorRecord(self: WriteOrThrowErrorCommand) -> ErrorRecord
        Set: ErrorRecord(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def Exception(self) -> Exception:
        """
        Get: Exception(self: WriteOrThrowErrorCommand) -> Exception
        Set: Exception(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: WriteOrThrowErrorCommand) -> str
        Set: Message(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def RecommendedAction(self) -> str:
        """
        Get: RecommendedAction(self: WriteOrThrowErrorCommand) -> str
        Set: RecommendedAction(self: WriteOrThrowErrorCommand) = value
        """
        ...

    @property
    def TargetObject(self) -> object:
        """
        Get: TargetObject(self: WriteOrThrowErrorCommand) -> object
        Set: TargetObject(self: WriteOrThrowErrorCommand) = value
        """
        ...



class WriteErrorCommand(WriteOrThrowErrorCommand): # skipped bases: <type 'object'>
    """ WriteErrorCommand() """
    pass

class WriteErrorException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WriteErrorException()
    WriteErrorException(message: str)
    WriteErrorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WriteEventLogCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteEventLogCommand() """
    @property
    def Category(self) -> Int16:
        """
        Get: Category(self: WriteEventLogCommand) -> Int16
        Set: Category(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: WriteEventLogCommand) -> str
        Set: ComputerName(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def EntryType(self) -> EventLogEntryType:
        """
        Get: EntryType(self: WriteEventLogCommand) -> EventLogEntryType
        Set: EntryType(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def EventId(self) -> int:
        """
        Get: EventId(self: WriteEventLogCommand) -> int
        Set: EventId(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def LogName(self) -> str:
        """
        Get: LogName(self: WriteEventLogCommand) -> str
        Set: LogName(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: WriteEventLogCommand) -> str
        Set: Message(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def RawData(self) -> Array:
        """
        Get: RawData(self: WriteEventLogCommand) -> Array[Byte]
        Set: RawData(self: WriteEventLogCommand) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: WriteEventLogCommand) -> str
        Set: Source(self: WriteEventLogCommand) = value
        """
        ...



class WriteHostCommand(ConsoleColorCmdlet): # skipped bases: <type 'object'>
    """ WriteHostCommand() """
    @property
    def NoNewline(self) -> SwitchParameter:
        """
        Get: NoNewline(self: WriteHostCommand) -> SwitchParameter
        Set: NoNewline(self: WriteHostCommand) = value
        """
        ...

    @property
    def Object(self) -> object:
        """
        Get: Object(self: WriteHostCommand) -> object
        Set: Object(self: WriteHostCommand) = value
        """
        ...

    @property
    def Separator(self) -> object:
        """
        Get: Separator(self: WriteHostCommand) -> object
        Set: Separator(self: WriteHostCommand) = value
        """
        ...



class WriteInformationCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteInformationCommand() """
    @property
    def MessageData(self) -> object:
        """
        Get: MessageData(self: WriteInformationCommand) -> object
        Set: MessageData(self: WriteInformationCommand) = value
        """
        ...

    @property
    def Tags(self) -> Array:
        """
        Get: Tags(self: WriteInformationCommand) -> Array[str]
        Set: Tags(self: WriteInformationCommand) = value
        """
        ...



class WriteOutputCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteOutputCommand() """
    @property
    def InputObject(self) -> Array:
        """
        Get: InputObject(self: WriteOutputCommand) -> Array[PSObject]
        Set: InputObject(self: WriteOutputCommand) = value
        """
        ...

    @property
    def NoEnumerate(self) -> SwitchParameter:
        """
        Get: NoEnumerate(self: WriteOutputCommand) -> SwitchParameter
        Set: NoEnumerate(self: WriteOutputCommand) = value
        """
        ...



class WriteProgressCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteProgressCommand() """
    @property
    def Activity(self) -> str:
        """
        Get: Activity(self: WriteProgressCommand) -> str
        Set: Activity(self: WriteProgressCommand) = value
        """
        ...

    @property
    def Completed(self) -> SwitchParameter:
        """
        Get: Completed(self: WriteProgressCommand) -> SwitchParameter
        Set: Completed(self: WriteProgressCommand) = value
        """
        ...

    @property
    def CurrentOperation(self) -> str:
        """
        Get: CurrentOperation(self: WriteProgressCommand) -> str
        Set: CurrentOperation(self: WriteProgressCommand) = value
        """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: WriteProgressCommand) -> int
        Set: Id(self: WriteProgressCommand) = value
        """
        ...

    @property
    def ParentId(self) -> int:
        """
        Get: ParentId(self: WriteProgressCommand) -> int
        Set: ParentId(self: WriteProgressCommand) = value
        """
        ...

    @property
    def PercentComplete(self) -> int:
        """
        Get: PercentComplete(self: WriteProgressCommand) -> int
        Set: PercentComplete(self: WriteProgressCommand) = value
        """
        ...

    @property
    def SecondsRemaining(self) -> int:
        """
        Get: SecondsRemaining(self: WriteProgressCommand) -> int
        Set: SecondsRemaining(self: WriteProgressCommand) = value
        """
        ...

    @property
    def SourceId(self) -> int:
        """
        Get: SourceId(self: WriteProgressCommand) -> int
        Set: SourceId(self: WriteProgressCommand) = value
        """
        ...

    @property
    def Status(self) -> str:
        """
        Get: Status(self: WriteProgressCommand) -> str
        Set: Status(self: WriteProgressCommand) = value
        """
        ...



class WriteVerboseCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteVerboseCommand() """
    @property
    def Message(self) -> str:
        """
        Get: Message(self: WriteVerboseCommand) -> str
        Set: Message(self: WriteVerboseCommand) = value
        """
        ...



class WriteWarningCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ WriteWarningCommand() """
    @property
    def Message(self) -> str:
        """
        Get: Message(self: WriteWarningCommand) -> str
        Set: Message(self: WriteWarningCommand) = value
        """
        ...



class WSManConfigurationOption(PSTransportOption): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def IdleTimeoutSec(self) -> Nullable:
        """ Get: IdleTimeoutSec(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxConcurrentCommandsPerSession(self) -> Nullable:
        """ Get: MaxConcurrentCommandsPerSession(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxConcurrentUsers(self) -> Nullable:
        """ Get: MaxConcurrentUsers(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxIdleTimeoutSec(self) -> Nullable:
        """ Get: MaxIdleTimeoutSec(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxMemoryPerSessionMB(self) -> Nullable:
        """ Get: MaxMemoryPerSessionMB(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxProcessesPerSession(self) -> Nullable:
        """ Get: MaxProcessesPerSession(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxSessions(self) -> Nullable:
        """ Get: MaxSessions(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def MaxSessionsPerUser(self) -> Nullable:
        """ Get: MaxSessionsPerUser(self: WSManConfigurationOption) -> Nullable[int] """
        ...

    @property
    def OutputBufferingMode(self) -> Nullable:
        """ Get: OutputBufferingMode(self: WSManConfigurationOption) -> Nullable[OutputBufferingMode] """
        ...

    @property
    def ProcessIdleTimeoutSec(self) -> Nullable:
        """ Get: ProcessIdleTimeoutSec(self: WSManConfigurationOption) -> Nullable[int] """
        ...



class X509StoreLocation: # skipped bases: <type 'object'>, <type 'object'>
    """ X509StoreLocation(location: StoreLocation) """
    @property
    def Location(self) -> StoreLocation:
        """
        Get: Location(self: X509StoreLocation) -> StoreLocation
        Set: Location(self: X509StoreLocation) = value
        """
        ...

    @property
    def LocationName(self) -> str:
        """ Get: LocationName(self: X509StoreLocation) -> str """
        ...

    @property
    def StoreNames(self) -> Hashtable:
        """ Get: StoreNames(self: X509StoreLocation) -> Hashtable """
        ...



# variables with complex values

