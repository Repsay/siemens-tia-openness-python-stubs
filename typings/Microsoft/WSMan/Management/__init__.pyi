# encoding: utf-8
# module Microsoft.WSMan.Management calls itself Management
# from Microsoft.WSMan.Runtime, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, Microsoft.WSMan.Management, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IDisposable, Nullable, UInt32, Uri

from System.Collections import Hashtable

from System.Management.Automation import (PSCmdlet, PSCredential, PSSnapIn, 
    SwitchParameter)

from System.Management.Automation.Provider import (
    ICmdletProviderSupportsHelp, NavigationCmdletProvider)

from System.Management.Automation.Runspaces import AuthenticationMechanism

from System.Net import NetworkCredential

"""The following names are not found in the module: __ComObject, field#
"""

# no functions
# classes

class AuthenticatingWSManCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ AuthenticatingWSManCommand() """
    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: AuthenticatingWSManCommand) -> AuthenticationMechanism
        Set: Authentication(self: AuthenticatingWSManCommand) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: AuthenticatingWSManCommand) -> str
        Set: CertificateThumbprint(self: AuthenticatingWSManCommand) = value
        """
        ...

    @property
    def Credential(self) -> PSCredential:
        """
        Get: Credential(self: AuthenticatingWSManCommand) -> PSCredential
        Set: Credential(self: AuthenticatingWSManCommand) = value
        """
        ...



class AuthenticationMechanism(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationMechanism, values: Basic (8), ClientCertificate (32), Credssp (128), Default (1), Digest (2), Kerberos (16), Negotiate (4), None (0) """
    Basic: AuthenticationMechanism = ...
    ClientCertificate: AuthenticationMechanism = ...
    Credssp: AuthenticationMechanism = ...
    Default: AuthenticationMechanism = ...
    Digest: AuthenticationMechanism = ...
    Kerberos: AuthenticationMechanism = ...
    Negotiate: AuthenticationMechanism = ...
    value__ = ...


class ConnectWSManCommand(AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ ConnectWSManCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: ConnectWSManCommand) -> str
        Set: ApplicationName(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: ConnectWSManCommand) -> str
        Set: ComputerName(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: ConnectWSManCommand) -> Uri
        Set: ConnectionURI(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: ConnectWSManCommand) -> Hashtable
        Set: OptionSet(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: ConnectWSManCommand) -> int
        Set: Port(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: ConnectWSManCommand) -> SessionOption
        Set: SessionOption(self: ConnectWSManCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: ConnectWSManCommand) -> SwitchParameter
        Set: UseSSL(self: ConnectWSManCommand) = value
        """
        ...



class WSManCredSSPCommandBase(PSCmdlet): # skipped bases: <type 'object'>
    """ WSManCredSSPCommandBase() """
    @property
    def Role(self) -> str:
        """
        Get: Role(self: WSManCredSSPCommandBase) -> str
        Set: Role(self: WSManCredSSPCommandBase) = value
        """
        ...



class DisableWSManCredSSPCommand(IDisposable, WSManCredSSPCommandBase): # skipped bases: <type 'object'>
    """ DisableWSManCredSSPCommand() """
    pass

class DisconnectWSManCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ DisconnectWSManCommand() """
    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: DisconnectWSManCommand) -> str
        Set: ComputerName(self: DisconnectWSManCommand) = value
        """
        ...



class EnableWSManCredSSPCommand(IDisposable, WSManCredSSPCommandBase): # skipped bases: <type 'object'>
    """ EnableWSManCredSSPCommand() """
    @property
    def DelegateComputer(self) -> Array:
        """
        Get: DelegateComputer(self: EnableWSManCredSSPCommand) -> Array[str]
        Set: DelegateComputer(self: EnableWSManCredSSPCommand) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: EnableWSManCredSSPCommand) -> SwitchParameter
        Set: Force(self: EnableWSManCredSSPCommand) = value
        """
        ...



class GetWSManCredSSPCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ GetWSManCredSSPCommand() """
    pass

class GetWSManInstanceCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ GetWSManInstanceCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: GetWSManInstanceCommand) -> str
        Set: ApplicationName(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Associations(self) -> SwitchParameter:
        """
        Get: Associations(self: GetWSManInstanceCommand) -> SwitchParameter
        Set: Associations(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def BasePropertiesOnly(self) -> SwitchParameter:
        """
        Get: BasePropertiesOnly(self: GetWSManInstanceCommand) -> SwitchParameter
        Set: BasePropertiesOnly(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: GetWSManInstanceCommand) -> str
        Set: ComputerName(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: GetWSManInstanceCommand) -> Uri
        Set: ConnectionURI(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Dialect(self) -> Uri:
        """
        Get: Dialect(self: GetWSManInstanceCommand) -> Uri
        Set: Dialect(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Enumerate(self) -> SwitchParameter:
        """
        Get: Enumerate(self: GetWSManInstanceCommand) -> SwitchParameter
        Set: Enumerate(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: GetWSManInstanceCommand) -> str
        Set: Filter(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Fragment(self) -> str:
        """
        Get: Fragment(self: GetWSManInstanceCommand) -> str
        Set: Fragment(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: GetWSManInstanceCommand) -> Hashtable
        Set: OptionSet(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: GetWSManInstanceCommand) -> int
        Set: Port(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def ResourceURI(self) -> Uri:
        """
        Get: ResourceURI(self: GetWSManInstanceCommand) -> Uri
        Set: ResourceURI(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def ReturnType(self) -> str:
        """
        Get: ReturnType(self: GetWSManInstanceCommand) -> str
        Set: ReturnType(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def SelectorSet(self) -> Hashtable:
        """
        Get: SelectorSet(self: GetWSManInstanceCommand) -> Hashtable
        Set: SelectorSet(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: GetWSManInstanceCommand) -> SessionOption
        Set: SessionOption(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def Shallow(self) -> SwitchParameter:
        """
        Get: Shallow(self: GetWSManInstanceCommand) -> SwitchParameter
        Set: Shallow(self: GetWSManInstanceCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: GetWSManInstanceCommand) -> SwitchParameter
        Set: UseSSL(self: GetWSManInstanceCommand) = value
        """
        ...



class GPClass(__ComObject): # skipped bases: <type 'object'>
    """ GPClass() """
    pass

class GpoNativeApi: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class InvokeWSManActionCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ InvokeWSManActionCommand() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: InvokeWSManActionCommand) -> str
        Set: Action(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: InvokeWSManActionCommand) -> str
        Set: ApplicationName(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: InvokeWSManActionCommand) -> str
        Set: ComputerName(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: InvokeWSManActionCommand) -> Uri
        Set: ConnectionURI(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: InvokeWSManActionCommand) -> str
        Set: FilePath(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: InvokeWSManActionCommand) -> Hashtable
        Set: OptionSet(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: InvokeWSManActionCommand) -> int
        Set: Port(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def ResourceURI(self) -> Uri:
        """
        Get: ResourceURI(self: InvokeWSManActionCommand) -> Uri
        Set: ResourceURI(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def SelectorSet(self) -> Hashtable:
        """
        Get: SelectorSet(self: InvokeWSManActionCommand) -> Hashtable
        Set: SelectorSet(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: InvokeWSManActionCommand) -> SessionOption
        Set: SessionOption(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: InvokeWSManActionCommand) -> SwitchParameter
        Set: UseSSL(self: InvokeWSManActionCommand) = value
        """
        ...

    @property
    def ValueSet(self) -> Hashtable:
        """
        Get: ValueSet(self: InvokeWSManActionCommand) -> Hashtable
        Set: ValueSet(self: InvokeWSManActionCommand) = value
        """
        ...



class IWSMan: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandLine(self) -> str:
        """ Get: CommandLine(self: IWSMan) -> str """
        ...

    @property
    def Error(self) -> str:
        """ Get: Error(self: IWSMan) -> str """
        ...


    def CreateConnectionOptions(self) -> object:
        """ CreateConnectionOptions(self: IWSMan) -> object """
        ...

    def CreateSession(self, connection:str, flags:int, connectionOptions:object) -> object:
        """ CreateSession(self: IWSMan, connection: str, flags: int, connectionOptions: object) -> object """
        ...


class IWSManConnectionOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Password(self): # -> 
        """ Set: Password(self: IWSManConnectionOptions) = value """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: IWSManConnectionOptions) -> str
        Set: UserName(self: IWSManConnectionOptions) = value
        """
        ...



class IWSManConnectionOptionsEx(IWSManConnectionOptions): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: IWSManConnectionOptionsEx) -> str
        Set: CertificateThumbprint(self: IWSManConnectionOptionsEx) = value
        """
        ...



class IWSManConnectionOptionsEx2(IWSManConnectionOptionsEx): # skipped bases: <type 'IWSManConnectionOptions'>, <type 'object'>
    """ no doc """
    def ProxyAuthenticationUseBasic(self) -> int:
        """ ProxyAuthenticationUseBasic(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyAuthenticationUseDigest(self) -> int:
        """ ProxyAuthenticationUseDigest(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyAuthenticationUseNegotiate(self) -> int:
        """ ProxyAuthenticationUseNegotiate(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyAutoDetect(self) -> int:
        """ ProxyAutoDetect(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyIEConfig(self) -> int:
        """ ProxyIEConfig(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyNoProxyServer(self) -> int:
        """ ProxyNoProxyServer(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def ProxyWinHttpConfig(self) -> int:
        """ ProxyWinHttpConfig(self: IWSManConnectionOptionsEx2) -> int """
        ...

    def SetProxy(self, accessType:int, authenticationMechanism:int, userName:str, password:str): # -> 
        """ SetProxy(self: IWSManConnectionOptionsEx2, accessType: int, authenticationMechanism: int, userName: str, password: str) """
        ...


class IWSManEnumerator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AtEndOfStream(self) -> bool:
        """ Get: AtEndOfStream(self: IWSManEnumerator) -> bool """
        ...

    @property
    def Error(self) -> str:
        """ Get: Error(self: IWSManEnumerator) -> str """
        ...


    def ReadItem(self) -> str:
        """ ReadItem(self: IWSManEnumerator) -> str """
        ...


class IWSManEx: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandLine(self) -> str:
        """ Get: CommandLine(self: IWSManEx) -> str """
        ...

    @property
    def Error(self) -> str:
        """ Get: Error(self: IWSManEx) -> str """
        ...


    def CreateConnectionOptions(self) -> object:
        """ CreateConnectionOptions(self: IWSManEx) -> object """
        ...

    def CreateResourceLocator(self, strResourceLocator:str) -> object:
        """ CreateResourceLocator(self: IWSManEx, strResourceLocator: str) -> object """
        ...

    def CreateSession(self, connection:str, flags:int, connectionOptions:object) -> object:
        """ CreateSession(self: IWSManEx, connection: str, flags: int, connectionOptions: object) -> object """
        ...

    def EnumerationFlagAssociatedInstance(self) -> int:
        """ EnumerationFlagAssociatedInstance(self: IWSManEx) -> int """
        ...

    def EnumerationFlagAssociationInstance(self) -> int:
        """ EnumerationFlagAssociationInstance(self: IWSManEx) -> int """
        ...

    def EnumerationFlagHierarchyDeep(self) -> int:
        """ EnumerationFlagHierarchyDeep(self: IWSManEx) -> int """
        ...

    def EnumerationFlagHierarchyDeepBasePropsOnly(self) -> int:
        """ EnumerationFlagHierarchyDeepBasePropsOnly(self: IWSManEx) -> int """
        ...

    def EnumerationFlagHierarchyShallow(self) -> int:
        """ EnumerationFlagHierarchyShallow(self: IWSManEx) -> int """
        ...

    def EnumerationFlagNonXmlText(self) -> int:
        """ EnumerationFlagNonXmlText(self: IWSManEx) -> int """
        ...

    def EnumerationFlagReturnEPR(self) -> int:
        """ EnumerationFlagReturnEPR(self: IWSManEx) -> int """
        ...

    def EnumerationFlagReturnObject(self) -> int:
        """ EnumerationFlagReturnObject(self: IWSManEx) -> int """
        ...

    def EnumerationFlagReturnObjectAndEPR(self) -> int:
        """ EnumerationFlagReturnObjectAndEPR(self: IWSManEx) -> int """
        ...

    def GetErrorMessage(self, errorNumber:UInt32) -> str:
        """ GetErrorMessage(self: IWSManEx, errorNumber: UInt32) -> str """
        ...

    def SessionFlagCredUsernamePassword(self) -> int:
        """ SessionFlagCredUsernamePassword(self: IWSManEx) -> int """
        ...

    def SessionFlagEnableSPNServerPort(self) -> int:
        """ SessionFlagEnableSPNServerPort(self: IWSManEx) -> int """
        ...

    def SessionFlagNoEncryption(self) -> int:
        """ SessionFlagNoEncryption(self: IWSManEx) -> int """
        ...

    def SessionFlagSkipCACheck(self) -> int:
        """ SessionFlagSkipCACheck(self: IWSManEx) -> int """
        ...

    def SessionFlagSkipCNCheck(self) -> int:
        """ SessionFlagSkipCNCheck(self: IWSManEx) -> int """
        ...

    def SessionFlagUseBasic(self) -> int:
        """ SessionFlagUseBasic(self: IWSManEx) -> int """
        ...

    def SessionFlagUseDigest(self) -> int:
        """ SessionFlagUseDigest(self: IWSManEx) -> int """
        ...

    def SessionFlagUseKerberos(self) -> int:
        """ SessionFlagUseKerberos(self: IWSManEx) -> int """
        ...

    def SessionFlagUseNegotiate(self) -> int:
        """ SessionFlagUseNegotiate(self: IWSManEx) -> int """
        ...

    def SessionFlagUseNoAuthentication(self) -> int:
        """ SessionFlagUseNoAuthentication(self: IWSManEx) -> int """
        ...

    def SessionFlagUTF8(self) -> int:
        """ SessionFlagUTF8(self: IWSManEx) -> int """
        ...


class IWSManResourceLocator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Error(self) -> str:
        """ Get: Error(self: IWSManResourceLocator) -> str """
        ...

    @property
    def FragmentDialect(self) -> str:
        """
        Get: FragmentDialect(self: IWSManResourceLocator) -> str
        Set: FragmentDialect(self: IWSManResourceLocator) = value
        """
        ...

    @property
    def FragmentPath(self) -> str:
        """
        Get: FragmentPath(self: IWSManResourceLocator) -> str
        Set: FragmentPath(self: IWSManResourceLocator) = value
        """
        ...

    @property
    def MustUnderstandOptions(self) -> int:
        """
        Get: MustUnderstandOptions(self: IWSManResourceLocator) -> int
        Set: MustUnderstandOptions(self: IWSManResourceLocator) = value
        """
        ...

    @property
    def ResourceUri(self) -> str:
        """
        Get: ResourceUri(self: IWSManResourceLocator) -> str
        Set: ResourceUri(self: IWSManResourceLocator) = value
        """
        ...


    def AddOption(self, OptionName:str, OptionValue:object, mustComply:int): # -> 
        """ AddOption(self: IWSManResourceLocator, OptionName: str, OptionValue: object, mustComply: int) """
        ...

    def AddSelector(self, resourceSelName:str, selValue:object): # -> 
        """ AddSelector(self: IWSManResourceLocator, resourceSelName: str, selValue: object) """
        ...

    def ClearOptions(self): # -> 
        """ ClearOptions(self: IWSManResourceLocator) """
        ...

    def ClearSelectors(self): # -> 
        """ ClearSelectors(self: IWSManResourceLocator) """
        ...


class IWSManResourceLocatorInternal: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IWSManSession: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BatchItems(self) -> int:
        """
        Get: BatchItems(self: IWSManSession) -> int
        Set: BatchItems(self: IWSManSession) = value
        """
        ...

    @property
    def Error(self) -> str:
        """ Get: Error(self: IWSManSession) -> str """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: IWSManSession) -> int
        Set: Timeout(self: IWSManSession) = value
        """
        ...


    def Create(self, resourceUri:object, resource:str, flags:int) -> str:
        """ Create(self: IWSManSession, resourceUri: object, resource: str, flags: int) -> str """
        ...

    def Delete(self, resourceUri:object, flags:int): # -> 
        """ Delete(self: IWSManSession, resourceUri: object, flags: int) """
        ...

    def Enumerate(self, resourceUri:object, filter:str, dialect:str, flags:int) -> object:
        """ Enumerate(self: IWSManSession, resourceUri: object, filter: str, dialect: str, flags: int) -> object """
        ...

    def Get(self, resourceUri:object, flags:int) -> str:
        """ Get(self: IWSManSession, resourceUri: object, flags: int) -> str """
        ...

    def Identify(self, flags:int) -> str:
        """ Identify(self: IWSManSession, flags: int) -> str """
        ...

    def Invoke(self, actionURI:str, resourceUri:object, parameters:str, flags:int) -> str:
        """ Invoke(self: IWSManSession, actionURI: str, resourceUri: object, parameters: str, flags: int) -> str """
        ...

    def Put(self, resourceUri:object, resource:str, flags:int) -> str:
        """ Put(self: IWSManSession, resourceUri: object, resource: str, flags: int) -> str """
        ...


class NewWSManInstanceCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ NewWSManInstanceCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: NewWSManInstanceCommand) -> str
        Set: ApplicationName(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: NewWSManInstanceCommand) -> str
        Set: ComputerName(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: NewWSManInstanceCommand) -> Uri
        Set: ConnectionURI(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: NewWSManInstanceCommand) -> str
        Set: FilePath(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: NewWSManInstanceCommand) -> Hashtable
        Set: OptionSet(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: NewWSManInstanceCommand) -> int
        Set: Port(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def ResourceURI(self) -> Uri:
        """
        Get: ResourceURI(self: NewWSManInstanceCommand) -> Uri
        Set: ResourceURI(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def SelectorSet(self) -> Hashtable:
        """
        Get: SelectorSet(self: NewWSManInstanceCommand) -> Hashtable
        Set: SelectorSet(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: NewWSManInstanceCommand) -> SessionOption
        Set: SessionOption(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: NewWSManInstanceCommand) -> SwitchParameter
        Set: UseSSL(self: NewWSManInstanceCommand) = value
        """
        ...

    @property
    def ValueSet(self) -> Hashtable:
        """
        Get: ValueSet(self: NewWSManInstanceCommand) -> Hashtable
        Set: ValueSet(self: NewWSManInstanceCommand) = value
        """
        ...



class NewWSManSessionOptionCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ NewWSManSessionOptionCommand() """
    @property
    def NoEncryption(self) -> SwitchParameter:
        """
        Get: NoEncryption(self: NewWSManSessionOptionCommand) -> SwitchParameter
        Set: NoEncryption(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def OperationTimeout(self) -> int:
        """
        Get: OperationTimeout(self: NewWSManSessionOptionCommand) -> int
        Set: OperationTimeout(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyAccessType(self) -> ProxyAccessType:
        """
        Get: ProxyAccessType(self: NewWSManSessionOptionCommand) -> ProxyAccessType
        Set: ProxyAccessType(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyAuthentication(self) -> ProxyAuthentication:
        """
        Get: ProxyAuthentication(self: NewWSManSessionOptionCommand) -> ProxyAuthentication
        Set: ProxyAuthentication(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def ProxyCredential(self) -> PSCredential:
        """
        Get: ProxyCredential(self: NewWSManSessionOptionCommand) -> PSCredential
        Set: ProxyCredential(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def SkipCACheck(self) -> SwitchParameter:
        """
        Get: SkipCACheck(self: NewWSManSessionOptionCommand) -> SwitchParameter
        Set: SkipCACheck(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def SkipCNCheck(self) -> SwitchParameter:
        """
        Get: SkipCNCheck(self: NewWSManSessionOptionCommand) -> SwitchParameter
        Set: SkipCNCheck(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def SkipRevocationCheck(self) -> SwitchParameter:
        """
        Get: SkipRevocationCheck(self: NewWSManSessionOptionCommand) -> SwitchParameter
        Set: SkipRevocationCheck(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def SPNPort(self) -> int:
        """
        Get: SPNPort(self: NewWSManSessionOptionCommand) -> int
        Set: SPNPort(self: NewWSManSessionOptionCommand) = value
        """
        ...

    @property
    def UseUTF16(self) -> SwitchParameter:
        """
        Get: UseUTF16(self: NewWSManSessionOptionCommand) -> SwitchParameter
        Set: UseUTF16(self: NewWSManSessionOptionCommand) = value
        """
        ...



class ProxyAccessType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProxyAccessType, values: ProxyAutoDetect (2), ProxyIEConfig (0), ProxyNoProxyServer (3), ProxyWinHttpConfig (1) """
    ProxyAutoDetect: ProxyAccessType = ...
    ProxyIEConfig: ProxyAccessType = ...
    ProxyNoProxyServer: ProxyAccessType = ...
    ProxyWinHttpConfig: ProxyAccessType = ...
    value__ = ...


class ProxyAuthentication(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProxyAuthentication, values: Basic (2), Digest (4), Negotiate (1) """
    Basic: ProxyAuthentication = ...
    Digest: ProxyAuthentication = ...
    Negotiate: ProxyAuthentication = ...
    value__ = ...


class RemoveWSManInstanceCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ RemoveWSManInstanceCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: RemoveWSManInstanceCommand) -> str
        Set: ApplicationName(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: RemoveWSManInstanceCommand) -> str
        Set: ComputerName(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: RemoveWSManInstanceCommand) -> Uri
        Set: ConnectionURI(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: RemoveWSManInstanceCommand) -> Hashtable
        Set: OptionSet(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: RemoveWSManInstanceCommand) -> int
        Set: Port(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def ResourceURI(self) -> Uri:
        """
        Get: ResourceURI(self: RemoveWSManInstanceCommand) -> Uri
        Set: ResourceURI(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def SelectorSet(self) -> Hashtable:
        """
        Get: SelectorSet(self: RemoveWSManInstanceCommand) -> Hashtable
        Set: SelectorSet(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: RemoveWSManInstanceCommand) -> SessionOption
        Set: SessionOption(self: RemoveWSManInstanceCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: RemoveWSManInstanceCommand) -> SwitchParameter
        Set: UseSSL(self: RemoveWSManInstanceCommand) = value
        """
        ...



class SessionOption: # skipped bases: <type 'object'>, <type 'object'>
    """ SessionOption() """
    @property
    def OperationTimeout(self) -> int:
        """
        Get: OperationTimeout(self: SessionOption) -> int
        Set: OperationTimeout(self: SessionOption) = value
        """
        ...

    @property
    def ProxyAccessType(self) -> ProxyAccessType:
        """
        Get: ProxyAccessType(self: SessionOption) -> ProxyAccessType
        Set: ProxyAccessType(self: SessionOption) = value
        """
        ...

    @property
    def ProxyAuthentication(self) -> ProxyAuthentication:
        """
        Get: ProxyAuthentication(self: SessionOption) -> ProxyAuthentication
        Set: ProxyAuthentication(self: SessionOption) = value
        """
        ...

    @property
    def ProxyCredential(self) -> NetworkCredential:
        """
        Get: ProxyCredential(self: SessionOption) -> NetworkCredential
        Set: ProxyCredential(self: SessionOption) = value
        """
        ...

    @property
    def SkipCACheck(self) -> bool:
        """
        Get: SkipCACheck(self: SessionOption) -> bool
        Set: SkipCACheck(self: SessionOption) = value
        """
        ...

    @property
    def SkipCNCheck(self) -> bool:
        """
        Get: SkipCNCheck(self: SessionOption) -> bool
        Set: SkipCNCheck(self: SessionOption) = value
        """
        ...

    @property
    def SkipRevocationCheck(self) -> bool:
        """
        Get: SkipRevocationCheck(self: SessionOption) -> bool
        Set: SkipRevocationCheck(self: SessionOption) = value
        """
        ...

    @property
    def SPNPort(self) -> int:
        """
        Get: SPNPort(self: SessionOption) -> int
        Set: SPNPort(self: SessionOption) = value
        """
        ...

    @property
    def UseEncryption(self) -> bool:
        """
        Get: UseEncryption(self: SessionOption) -> bool
        Set: UseEncryption(self: SessionOption) = value
        """
        ...

    @property
    def UseUtf16(self) -> bool:
        """
        Get: UseUtf16(self: SessionOption) -> bool
        Set: UseUtf16(self: SessionOption) = value
        """
        ...



class SetWSManInstanceCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ SetWSManInstanceCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: SetWSManInstanceCommand) -> str
        Set: ApplicationName(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: SetWSManInstanceCommand) -> str
        Set: ComputerName(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: SetWSManInstanceCommand) -> Uri
        Set: ConnectionURI(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def Dialect(self) -> Uri:
        """
        Get: Dialect(self: SetWSManInstanceCommand) -> Uri
        Set: Dialect(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def FilePath(self) -> str:
        """
        Get: FilePath(self: SetWSManInstanceCommand) -> str
        Set: FilePath(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def Fragment(self) -> str:
        """
        Get: Fragment(self: SetWSManInstanceCommand) -> str
        Set: Fragment(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: SetWSManInstanceCommand) -> Hashtable
        Set: OptionSet(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: SetWSManInstanceCommand) -> int
        Set: Port(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def ResourceURI(self) -> Uri:
        """
        Get: ResourceURI(self: SetWSManInstanceCommand) -> Uri
        Set: ResourceURI(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def SelectorSet(self) -> Hashtable:
        """
        Get: SelectorSet(self: SetWSManInstanceCommand) -> Hashtable
        Set: SelectorSet(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: SetWSManInstanceCommand) -> SessionOption
        Set: SessionOption(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: SetWSManInstanceCommand) -> SwitchParameter
        Set: UseSSL(self: SetWSManInstanceCommand) = value
        """
        ...

    @property
    def ValueSet(self) -> Hashtable:
        """
        Get: ValueSet(self: SetWSManInstanceCommand) -> Hashtable
        Set: ValueSet(self: SetWSManInstanceCommand) = value
        """
        ...



class SetWSManQuickConfigCommand(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ SetWSManQuickConfigCommand() """
    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: SetWSManQuickConfigCommand) -> SwitchParameter
        Set: Force(self: SetWSManQuickConfigCommand) = value
        """
        ...

    @property
    def SkipNetworkProfileCheck(self) -> SwitchParameter:
        """
        Get: SkipNetworkProfileCheck(self: SetWSManQuickConfigCommand) -> SwitchParameter
        Set: SkipNetworkProfileCheck(self: SetWSManQuickConfigCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: SetWSManQuickConfigCommand) -> SwitchParameter
        Set: UseSSL(self: SetWSManQuickConfigCommand) = value
        """
        ...



class TestWSManCommand(IDisposable, AuthenticatingWSManCommand): # skipped bases: <type 'object'>
    """ TestWSManCommand() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: TestWSManCommand) -> str
        Set: ApplicationName(self: TestWSManCommand) = value
        """
        ...

    @property
    def ComputerName(self) -> str:
        """
        Get: ComputerName(self: TestWSManCommand) -> str
        Set: ComputerName(self: TestWSManCommand) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: TestWSManCommand) -> int
        Set: Port(self: TestWSManCommand) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: TestWSManCommand) -> SwitchParameter
        Set: UseSSL(self: TestWSManCommand) = value
        """
        ...



class WSManClass(__ComObject): # skipped bases: <type 'object'>
    """ WSManClass() """
    pass

class WSManConfigElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: WSManConfigElement) -> str
        Set: Name(self: WSManConfigElement) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: WSManConfigElement) -> str
        Set: Type(self: WSManConfigElement) = value
        """
        ...

    @property
    def TypeNameOfElement(self) -> str:
        """
        Get: TypeNameOfElement(self: WSManConfigElement) -> str
        Set: TypeNameOfElement(self: WSManConfigElement) = value
        """
        ...



class WSManConfigContainerElement(WSManConfigElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Keys(self) -> Array:
        """
        Get: Keys(self: WSManConfigContainerElement) -> Array[str]
        Set: Keys(self: WSManConfigContainerElement) = value
        """
        ...



class WSManConfigLeafElement(WSManConfigElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SourceOfValue(self) -> object:
        """
        Get: SourceOfValue(self: WSManConfigLeafElement) -> object
        Set: SourceOfValue(self: WSManConfigLeafElement) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: WSManConfigLeafElement) -> object
        Set: Value(self: WSManConfigLeafElement) = value
        """
        ...



class WSManConfigProvider(ICmdletProviderSupportsHelp, NavigationCmdletProvider): # skipped bases: <type 'IResourceSupplier'>, <type 'object'>
    """ WSManConfigProvider() """
    pass

class WSManEnumFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WSManEnumFlags, values: WSManFlagAssociationInstance (128), WSManFlagHierarchyDeep (0), WSManFlagHierarchyDeepBasePropsOnly (64), WSManFlagHierarchyShallow (32), WSManFlagNonXmlText (1), WSManFlagReturnEPR (2), WSManFlagReturnObject (0), WSManFlagReturnObjectAndEPR (4) """
    value__ = ...
    WSManFlagAssociationInstance: WSManEnumFlags = ...
    WSManFlagHierarchyDeep: WSManEnumFlags = ...
    WSManFlagHierarchyDeepBasePropsOnly: WSManEnumFlags = ...
    WSManFlagHierarchyShallow: WSManEnumFlags = ...
    WSManFlagNonXmlText: WSManEnumFlags = ...
    WSManFlagReturnEPR: WSManEnumFlags = ...
    WSManFlagReturnObject: WSManEnumFlags = ...
    WSManFlagReturnObjectAndEPR: WSManEnumFlags = ...


class WSManProviderClientCertificateParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderClientCertificateParameters() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WSManProviderClientCertificateParameters) -> bool
        Set: Enabled(self: WSManProviderClientCertificateParameters) = value
        """
        ...

    @property
    def Issuer(self) -> str:
        """
        Get: Issuer(self: WSManProviderClientCertificateParameters) -> str
        Set: Issuer(self: WSManProviderClientCertificateParameters) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: WSManProviderClientCertificateParameters) -> str
        Set: Subject(self: WSManProviderClientCertificateParameters) = value
        """
        ...

    @property
    def URI(self) -> Uri:
        """
        Get: URI(self: WSManProviderClientCertificateParameters) -> Uri
        Set: URI(self: WSManProviderClientCertificateParameters) = value
        """
        ...



class WSManProviderInitializeParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderInitializeParameters() """
    @property
    def ParamName(self) -> str:
        """
        Get: ParamName(self: WSManProviderInitializeParameters) -> str
        Set: ParamName(self: WSManProviderInitializeParameters) = value
        """
        ...

    @property
    def ParamValue(self) -> str:
        """
        Get: ParamValue(self: WSManProviderInitializeParameters) -> str
        Set: ParamValue(self: WSManProviderInitializeParameters) = value
        """
        ...



class WSManProviderNewItemComputerParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderNewItemComputerParameters() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: WSManProviderNewItemComputerParameters) -> str
        Set: ApplicationName(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationMechanism:
        """
        Get: Authentication(self: WSManProviderNewItemComputerParameters) -> AuthenticationMechanism
        Set: Authentication(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def CertificateThumbprint(self) -> str:
        """
        Get: CertificateThumbprint(self: WSManProviderNewItemComputerParameters) -> str
        Set: CertificateThumbprint(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def ConnectionURI(self) -> Uri:
        """
        Get: ConnectionURI(self: WSManProviderNewItemComputerParameters) -> Uri
        Set: ConnectionURI(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def OptionSet(self) -> Hashtable:
        """
        Get: OptionSet(self: WSManProviderNewItemComputerParameters) -> Hashtable
        Set: OptionSet(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: WSManProviderNewItemComputerParameters) -> int
        Set: Port(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def SessionOption(self) -> SessionOption:
        """
        Get: SessionOption(self: WSManProviderNewItemComputerParameters) -> SessionOption
        Set: SessionOption(self: WSManProviderNewItemComputerParameters) = value
        """
        ...

    @property
    def UseSSL(self) -> SwitchParameter:
        """
        Get: UseSSL(self: WSManProviderNewItemComputerParameters) -> SwitchParameter
        Set: UseSSL(self: WSManProviderNewItemComputerParameters) = value
        """
        ...



class WSManProviderNewItemPluginParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderNewItemPluginParameters() """
    @property
    def AutoRestart(self) -> SwitchParameter:
        """
        Get: AutoRestart(self: WSManProviderNewItemPluginParameters) -> SwitchParameter
        Set: AutoRestart(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def Capability(self) -> Array:
        """
        Get: Capability(self: WSManProviderNewItemPluginParameters) -> Array[object]
        Set: Capability(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def File(self) -> str:
        """
        Get: File(self: WSManProviderNewItemPluginParameters) -> str
        Set: File(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: WSManProviderNewItemPluginParameters) -> str
        Set: FileName(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def Plugin(self) -> str:
        """
        Get: Plugin(self: WSManProviderNewItemPluginParameters) -> str
        Set: Plugin(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def ProcessIdleTimeoutSec(self) -> Nullable:
        """
        Get: ProcessIdleTimeoutSec(self: WSManProviderNewItemPluginParameters) -> Nullable[UInt32]
        Set: ProcessIdleTimeoutSec(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def Resource(self) -> Uri:
        """
        Get: Resource(self: WSManProviderNewItemPluginParameters) -> Uri
        Set: Resource(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def RunAsCredential(self) -> PSCredential:
        """
        Get: RunAsCredential(self: WSManProviderNewItemPluginParameters) -> PSCredential
        Set: RunAsCredential(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def SDKVersion(self) -> str:
        """
        Get: SDKVersion(self: WSManProviderNewItemPluginParameters) -> str
        Set: SDKVersion(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def UseSharedProcess(self) -> SwitchParameter:
        """
        Get: UseSharedProcess(self: WSManProviderNewItemPluginParameters) -> SwitchParameter
        Set: UseSharedProcess(self: WSManProviderNewItemPluginParameters) = value
        """
        ...

    @property
    def XMLRenderingType(self) -> str:
        """
        Get: XMLRenderingType(self: WSManProviderNewItemPluginParameters) -> str
        Set: XMLRenderingType(self: WSManProviderNewItemPluginParameters) = value
        """
        ...



class WSManProviderNewItemResourceParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderNewItemResourceParameters() """
    @property
    def Capability(self) -> Array:
        """
        Get: Capability(self: WSManProviderNewItemResourceParameters) -> Array[object]
        Set: Capability(self: WSManProviderNewItemResourceParameters) = value
        """
        ...

    @property
    def ResourceUri(self) -> Uri:
        """
        Get: ResourceUri(self: WSManProviderNewItemResourceParameters) -> Uri
        Set: ResourceUri(self: WSManProviderNewItemResourceParameters) = value
        """
        ...



class WSManProviderNewItemSecurityParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderNewItemSecurityParameters() """
    @property
    def Sddl(self) -> str:
        """
        Get: Sddl(self: WSManProviderNewItemSecurityParameters) -> str
        Set: Sddl(self: WSManProviderNewItemSecurityParameters) = value
        """
        ...



class WSManProviderSetItemDynamicParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProviderSetItemDynamicParameters() """
    @property
    def Concatenate(self) -> SwitchParameter:
        """
        Get: Concatenate(self: WSManProviderSetItemDynamicParameters) -> SwitchParameter
        Set: Concatenate(self: WSManProviderSetItemDynamicParameters) = value
        """
        ...



class WSManProvidersListenerParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ WSManProvidersListenerParameters() """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: WSManProvidersListenerParameters) -> str
        Set: Address(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def CertificateThumbPrint(self) -> str:
        """
        Get: CertificateThumbPrint(self: WSManProvidersListenerParameters) -> str
        Set: CertificateThumbPrint(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WSManProvidersListenerParameters) -> bool
        Set: Enabled(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def HostName(self) -> str:
        """
        Get: HostName(self: WSManProvidersListenerParameters) -> str
        Set: HostName(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def IsPortSpecified(self) -> bool:
        """
        Get: IsPortSpecified(self: WSManProvidersListenerParameters) -> bool
        Set: IsPortSpecified(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: WSManProvidersListenerParameters) -> int
        Set: Port(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def Transport(self) -> str:
        """
        Get: Transport(self: WSManProvidersListenerParameters) -> str
        Set: Transport(self: WSManProvidersListenerParameters) = value
        """
        ...

    @property
    def URLPrefix(self) -> str:
        """
        Get: URLPrefix(self: WSManProvidersListenerParameters) -> str
        Set: URLPrefix(self: WSManProvidersListenerParameters) = value
        """
        ...



class WSManPSSnapIn(PSSnapIn): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ WSManPSSnapIn() """
    @property
    def Description(self) -> str:
        """ Get: Description(self: WSManPSSnapIn) -> str """
        ...

    @property
    def DescriptionResource(self) -> str:
        """ Get: DescriptionResource(self: WSManPSSnapIn) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: WSManPSSnapIn) -> str """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: WSManPSSnapIn) -> str """
        ...

    @property
    def VendorResource(self) -> str:
        """ Get: VendorResource(self: WSManPSSnapIn) -> str """
        ...



class WSManSessionFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WSManSessionFlags, values: WSManFlagAllowNegotiateImplicitCredentials (67108864), WSManFlagCredUserNamePassword (4096), WSManFlagEnableSpnServerPort (4194304), WSManFlagNoEncryption (1048576), WSManFlagSkipCACheck (8192), WSManFlagSkipCNCheck (16384), WSManFlagSkipRevocationCheck (33554432), WSManFlagUseBasic (262144), WSManFlagUseClientCertificate (2097152), WSManFlagUseCredSsp (16777216), WSManFlagUseDigest (65536), WSManFlagUseKerberos (524288), WSManFlagUseNegotiate (131072), WSManFlagUseNoAuthentication (32768), WSManFlagUseSsl (134217728), WSManFlagUtf16 (8388608), WSManFlagUtf8 (1), WSManNone (0) """
    value__ = ...
    WSManFlagAllowNegotiateImplicitCredentials: WSManSessionFlags = ...
    WSManFlagCredUserNamePassword: WSManSessionFlags = ...
    WSManFlagEnableSpnServerPort: WSManSessionFlags = ...
    WSManFlagNoEncryption: WSManSessionFlags = ...
    WSManFlagSkipCACheck: WSManSessionFlags = ...
    WSManFlagSkipCNCheck: WSManSessionFlags = ...
    WSManFlagSkipRevocationCheck: WSManSessionFlags = ...
    WSManFlagUseBasic: WSManSessionFlags = ...
    WSManFlagUseClientCertificate: WSManSessionFlags = ...
    WSManFlagUseCredSsp: WSManSessionFlags = ...
    WSManFlagUseDigest: WSManSessionFlags = ...
    WSManFlagUseKerberos: WSManSessionFlags = ...
    WSManFlagUseNegotiate: WSManSessionFlags = ...
    WSManFlagUseNoAuthentication: WSManSessionFlags = ...
    WSManFlagUseSsl: WSManSessionFlags = ...
    WSManFlagUtf16: WSManSessionFlags = ...
    WSManFlagUtf8: WSManSessionFlags = ...
    WSManNone: WSManSessionFlags = ...


