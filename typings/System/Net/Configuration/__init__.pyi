# encoding: utf-8
# module System.Net.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Int64, TimeSpan, Type, Uri

from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup)

from System.Net.Cache import HttpRequestCacheLevel, RequestCacheLevel

from System.Net.Mail import SmtpDeliveryFormat, SmtpDeliveryMethod

from System.Net.Security import EncryptionPolicy

from System.Net.Sockets import IPProtectionLevel

from typing import Self

"""The following names are not found in the module: (AutoDetectValues, 
    BypassOnLocalValues, UseSystemDefaultValues, field#)
"""

# no functions
# classes

class AuthenticationModuleElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    AuthenticationModuleElement()
    AuthenticationModuleElement(typeName: str)
    """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: AuthenticationModuleElement) -> str
        Set: Type(self: AuthenticationModuleElement) = value
        """
        ...


    def __new__(cls, typeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        """
        ...


class AuthenticationModuleElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AuthenticationModuleElementCollection() """
    def Add(self, element:AuthenticationModuleElement): # -> 
        """ Add(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: AuthenticationModuleElementCollection) """
        ...

    def IndexOf(self, element:AuthenticationModuleElement) -> int:
        """ IndexOf(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement) -> int """
        ...

    def Remove(self, *__args:AuthenticationModuleElement): # -> 
        """ Remove(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement)Remove(self: AuthenticationModuleElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: AuthenticationModuleElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class AuthenticationModulesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ AuthenticationModulesSection() """
    @property
    def AuthenticationModules(self) -> AuthenticationModuleElementCollection:
        """ Get: AuthenticationModules(self: AuthenticationModulesSection) -> AuthenticationModuleElementCollection """
        ...



class BypassElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    BypassElement()
    BypassElement(address: str)
    """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: BypassElement) -> str
        Set: Address(self: BypassElement) = value
        """
        ...


    def __new__(cls, address:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, address: str)
        """
        ...


class BypassElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BypassElementCollection() """
    def Add(self, element:BypassElement): # -> 
        """ Add(self: BypassElementCollection, element: BypassElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: BypassElementCollection) """
        ...

    def IndexOf(self, element:BypassElement) -> int:
        """ IndexOf(self: BypassElementCollection, element: BypassElement) -> int """
        ...

    def Remove(self, *__args:BypassElement): # -> 
        """ Remove(self: BypassElementCollection, element: BypassElement)Remove(self: BypassElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: BypassElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ConnectionManagementElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ConnectionManagementElement()
    ConnectionManagementElement(address: str, maxConnection: int)
    """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: ConnectionManagementElement) -> str
        Set: Address(self: ConnectionManagementElement) = value
        """
        ...

    @property
    def MaxConnection(self) -> int:
        """
        Get: MaxConnection(self: ConnectionManagementElement) -> int
        Set: MaxConnection(self: ConnectionManagementElement) = value
        """
        ...


    def __new__(cls, address:str = ..., maxConnection:int = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, address: str, maxConnection: int)
        """
        ...


class ConnectionManagementElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ConnectionManagementElementCollection() """
    def Add(self, element:ConnectionManagementElement): # -> 
        """ Add(self: ConnectionManagementElementCollection, element: ConnectionManagementElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConnectionManagementElementCollection) """
        ...

    def IndexOf(self, element:ConnectionManagementElement) -> int:
        """ IndexOf(self: ConnectionManagementElementCollection, element: ConnectionManagementElement) -> int """
        ...

    def Remove(self, *__args:ConnectionManagementElement): # -> 
        """ Remove(self: ConnectionManagementElementCollection, element: ConnectionManagementElement)Remove(self: ConnectionManagementElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ConnectionManagementElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ConnectionManagementSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ConnectionManagementSection() """
    @property
    def ConnectionManagement(self) -> ConnectionManagementElementCollection:
        """ Get: ConnectionManagement(self: ConnectionManagementSection) -> ConnectionManagementElementCollection """
        ...



class DefaultProxySection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DefaultProxySection() """
    @property
    def BypassList(self) -> BypassElementCollection:
        """ Get: BypassList(self: DefaultProxySection) -> BypassElementCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: DefaultProxySection) -> bool
        Set: Enabled(self: DefaultProxySection) = value
        """
        ...

    @property
    def Module(self) -> ModuleElement:
        """ Get: Module(self: DefaultProxySection) -> ModuleElement """
        ...

    @property
    def Proxy(self) -> ProxyElement:
        """ Get: Proxy(self: DefaultProxySection) -> ProxyElement """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: DefaultProxySection) -> bool
        Set: UseDefaultCredentials(self: DefaultProxySection) = value
        """
        ...



class FtpCachePolicyElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ FtpCachePolicyElement() """
    @property
    def PolicyLevel(self) -> RequestCacheLevel:
        """
        Get: PolicyLevel(self: FtpCachePolicyElement) -> RequestCacheLevel
        Set: PolicyLevel(self: FtpCachePolicyElement) = value
        """
        ...



class HttpCachePolicyElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpCachePolicyElement() """
    @property
    def MaximumAge(self) -> TimeSpan:
        """
        Get: MaximumAge(self: HttpCachePolicyElement) -> TimeSpan
        Set: MaximumAge(self: HttpCachePolicyElement) = value
        """
        ...

    @property
    def MaximumStale(self) -> TimeSpan:
        """
        Get: MaximumStale(self: HttpCachePolicyElement) -> TimeSpan
        Set: MaximumStale(self: HttpCachePolicyElement) = value
        """
        ...

    @property
    def MinimumFresh(self) -> TimeSpan:
        """
        Get: MinimumFresh(self: HttpCachePolicyElement) -> TimeSpan
        Set: MinimumFresh(self: HttpCachePolicyElement) = value
        """
        ...

    @property
    def PolicyLevel(self) -> HttpRequestCacheLevel:
        """
        Get: PolicyLevel(self: HttpCachePolicyElement) -> HttpRequestCacheLevel
        Set: PolicyLevel(self: HttpCachePolicyElement) = value
        """
        ...



class HttpListenerElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpListenerElement() """
    @property
    def Timeouts(self) -> HttpListenerTimeoutsElement:
        """ Get: Timeouts(self: HttpListenerElement) -> HttpListenerTimeoutsElement """
        ...

    @property
    def UnescapeRequestUrl(self) -> bool:
        """ Get: UnescapeRequestUrl(self: HttpListenerElement) -> bool """
        ...



class HttpListenerTimeoutsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpListenerTimeoutsElement() """
    @property
    def DrainEntityBody(self) -> TimeSpan:
        """ Get: DrainEntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan """
        ...

    @property
    def EntityBody(self) -> TimeSpan:
        """ Get: EntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan """
        ...

    @property
    def HeaderWait(self) -> TimeSpan:
        """ Get: HeaderWait(self: HttpListenerTimeoutsElement) -> TimeSpan """
        ...

    @property
    def IdleConnection(self) -> TimeSpan:
        """ Get: IdleConnection(self: HttpListenerTimeoutsElement) -> TimeSpan """
        ...

    @property
    def MinSendBytesPerSecond(self) -> Int64:
        """ Get: MinSendBytesPerSecond(self: HttpListenerTimeoutsElement) -> Int64 """
        ...

    @property
    def RequestQueue(self) -> TimeSpan:
        """ Get: RequestQueue(self: HttpListenerTimeoutsElement) -> TimeSpan """
        ...



class HttpWebRequestElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpWebRequestElement() """
    @property
    def MaximumErrorResponseLength(self) -> int:
        """
        Get: MaximumErrorResponseLength(self: HttpWebRequestElement) -> int
        Set: MaximumErrorResponseLength(self: HttpWebRequestElement) = value
        """
        ...

    @property
    def MaximumResponseHeadersLength(self) -> int:
        """
        Get: MaximumResponseHeadersLength(self: HttpWebRequestElement) -> int
        Set: MaximumResponseHeadersLength(self: HttpWebRequestElement) = value
        """
        ...

    @property
    def MaximumUnauthorizedUploadLength(self) -> int:
        """
        Get: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) -> int
        Set: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) = value
        """
        ...

    @property
    def UseUnsafeHeaderParsing(self) -> bool:
        """
        Get: UseUnsafeHeaderParsing(self: HttpWebRequestElement) -> bool
        Set: UseUnsafeHeaderParsing(self: HttpWebRequestElement) = value
        """
        ...



class Ipv6Element(ConfigurationElement): # skipped bases: <type 'object'>
    """ Ipv6Element() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Ipv6Element) -> bool
        Set: Enabled(self: Ipv6Element) = value
        """
        ...



class MailSettingsSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ MailSettingsSectionGroup() """
    @property
    def Smtp(self) -> SmtpSection:
        """ Get: Smtp(self: MailSettingsSectionGroup) -> SmtpSection """
        ...



class ModuleElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ModuleElement() """
    @property
    def Type(self) -> str:
        """
        Get: Type(self: ModuleElement) -> str
        Set: Type(self: ModuleElement) = value
        """
        ...



class NetSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ NetSectionGroup() """
    @property
    def AuthenticationModules(self) -> AuthenticationModulesSection:
        """ Get: AuthenticationModules(self: NetSectionGroup) -> AuthenticationModulesSection """
        ...

    @property
    def ConnectionManagement(self) -> ConnectionManagementSection:
        """ Get: ConnectionManagement(self: NetSectionGroup) -> ConnectionManagementSection """
        ...

    @property
    def DefaultProxy(self) -> DefaultProxySection:
        """ Get: DefaultProxy(self: NetSectionGroup) -> DefaultProxySection """
        ...

    @property
    def MailSettings(self) -> MailSettingsSectionGroup:
        """ Get: MailSettings(self: NetSectionGroup) -> MailSettingsSectionGroup """
        ...

    @property
    def RequestCaching(self) -> RequestCachingSection:
        """ Get: RequestCaching(self: NetSectionGroup) -> RequestCachingSection """
        ...

    @property
    def Settings(self) -> SettingsSection:
        """ Get: Settings(self: NetSectionGroup) -> SettingsSection """
        ...

    @property
    def WebRequestModules(self) -> WebRequestModulesSection:
        """ Get: WebRequestModules(self: NetSectionGroup) -> WebRequestModulesSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> NetSectionGroup:
        """ GetSectionGroup(config: Configuration) -> NetSectionGroup """
        ...


class PerformanceCountersElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ PerformanceCountersElement() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: PerformanceCountersElement) -> bool
        Set: Enabled(self: PerformanceCountersElement) = value
        """
        ...



class ProxyElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ProxyElement() """
    @property
    def AutoDetect(self): # -> AutoDetectValues
        """
        Get: AutoDetect(self: ProxyElement) -> AutoDetectValues
        Set: AutoDetect(self: ProxyElement) = value
        """
        ...

    @property
    def BypassOnLocal(self): # -> BypassOnLocalValues
        """
        Get: BypassOnLocal(self: ProxyElement) -> BypassOnLocalValues
        Set: BypassOnLocal(self: ProxyElement) = value
        """
        ...

    @property
    def ProxyAddress(self) -> Uri:
        """
        Get: ProxyAddress(self: ProxyElement) -> Uri
        Set: ProxyAddress(self: ProxyElement) = value
        """
        ...

    @property
    def ScriptLocation(self) -> Uri:
        """
        Get: ScriptLocation(self: ProxyElement) -> Uri
        Set: ScriptLocation(self: ProxyElement) = value
        """
        ...

    @property
    def UseSystemDefault(self): # -> UseSystemDefaultValues
        """
        Get: UseSystemDefault(self: ProxyElement) -> UseSystemDefaultValues
        Set: UseSystemDefault(self: ProxyElement) = value
        """
        ...


    def AutoDetectValues(self, *args): #cannot find CLR method
        """ enum AutoDetectValues, values: False (0), True (1), Unspecified (-1) """
        ...

    def BypassOnLocalValues(self, *args): #cannot find CLR method
        """ enum BypassOnLocalValues, values: False (0), True (1), Unspecified (-1) """
        ...

    def UseSystemDefaultValues(self, *args): #cannot find CLR method
        """ enum UseSystemDefaultValues, values: False (0), True (1), Unspecified (-1) """
        ...



class RequestCachingSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ RequestCachingSection() """
    @property
    def DefaultFtpCachePolicy(self) -> FtpCachePolicyElement:
        """ Get: DefaultFtpCachePolicy(self: RequestCachingSection) -> FtpCachePolicyElement """
        ...

    @property
    def DefaultHttpCachePolicy(self) -> HttpCachePolicyElement:
        """ Get: DefaultHttpCachePolicy(self: RequestCachingSection) -> HttpCachePolicyElement """
        ...

    @property
    def DefaultPolicyLevel(self) -> RequestCacheLevel:
        """
        Get: DefaultPolicyLevel(self: RequestCachingSection) -> RequestCacheLevel
        Set: DefaultPolicyLevel(self: RequestCachingSection) = value
        """
        ...

    @property
    def DisableAllCaching(self) -> bool:
        """
        Get: DisableAllCaching(self: RequestCachingSection) -> bool
        Set: DisableAllCaching(self: RequestCachingSection) = value
        """
        ...

    @property
    def IsPrivateCache(self) -> bool:
        """
        Get: IsPrivateCache(self: RequestCachingSection) -> bool
        Set: IsPrivateCache(self: RequestCachingSection) = value
        """
        ...

    @property
    def UnspecifiedMaximumAge(self) -> TimeSpan:
        """
        Get: UnspecifiedMaximumAge(self: RequestCachingSection) -> TimeSpan
        Set: UnspecifiedMaximumAge(self: RequestCachingSection) = value
        """
        ...



class ServicePointManagerElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ServicePointManagerElement() """
    @property
    def CheckCertificateName(self) -> bool:
        """
        Get: CheckCertificateName(self: ServicePointManagerElement) -> bool
        Set: CheckCertificateName(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def CheckCertificateRevocationList(self) -> bool:
        """
        Get: CheckCertificateRevocationList(self: ServicePointManagerElement) -> bool
        Set: CheckCertificateRevocationList(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def DnsRefreshTimeout(self) -> int:
        """
        Get: DnsRefreshTimeout(self: ServicePointManagerElement) -> int
        Set: DnsRefreshTimeout(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def EnableDnsRoundRobin(self) -> bool:
        """
        Get: EnableDnsRoundRobin(self: ServicePointManagerElement) -> bool
        Set: EnableDnsRoundRobin(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def EncryptionPolicy(self) -> EncryptionPolicy:
        """
        Get: EncryptionPolicy(self: ServicePointManagerElement) -> EncryptionPolicy
        Set: EncryptionPolicy(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def Expect100Continue(self) -> bool:
        """
        Get: Expect100Continue(self: ServicePointManagerElement) -> bool
        Set: Expect100Continue(self: ServicePointManagerElement) = value
        """
        ...

    @property
    def UseNagleAlgorithm(self) -> bool:
        """
        Get: UseNagleAlgorithm(self: ServicePointManagerElement) -> bool
        Set: UseNagleAlgorithm(self: ServicePointManagerElement) = value
        """
        ...



class SettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SettingsSection() """
    @property
    def HttpListener(self) -> HttpListenerElement:
        """ Get: HttpListener(self: SettingsSection) -> HttpListenerElement """
        ...

    @property
    def HttpWebRequest(self) -> HttpWebRequestElement:
        """ Get: HttpWebRequest(self: SettingsSection) -> HttpWebRequestElement """
        ...

    @property
    def Ipv6(self) -> Ipv6Element:
        """ Get: Ipv6(self: SettingsSection) -> Ipv6Element """
        ...

    @property
    def PerformanceCounters(self) -> PerformanceCountersElement:
        """ Get: PerformanceCounters(self: SettingsSection) -> PerformanceCountersElement """
        ...

    @property
    def ServicePointManager(self) -> ServicePointManagerElement:
        """ Get: ServicePointManager(self: SettingsSection) -> ServicePointManagerElement """
        ...

    @property
    def Socket(self) -> SocketElement:
        """ Get: Socket(self: SettingsSection) -> SocketElement """
        ...

    @property
    def WebProxyScript(self) -> WebProxyScriptElement:
        """ Get: WebProxyScript(self: SettingsSection) -> WebProxyScriptElement """
        ...

    @property
    def WebUtility(self) -> WebUtilityElement:
        """ Get: WebUtility(self: SettingsSection) -> WebUtilityElement """
        ...

    @property
    def WindowsAuthentication(self) -> WindowsAuthenticationElement:
        """ Get: WindowsAuthentication(self: SettingsSection) -> WindowsAuthenticationElement """
        ...



class SmtpNetworkElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SmtpNetworkElement() """
    @property
    def ClientDomain(self) -> str:
        """
        Get: ClientDomain(self: SmtpNetworkElement) -> str
        Set: ClientDomain(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def DefaultCredentials(self) -> bool:
        """
        Get: DefaultCredentials(self: SmtpNetworkElement) -> bool
        Set: DefaultCredentials(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def EnableSsl(self) -> bool:
        """
        Get: EnableSsl(self: SmtpNetworkElement) -> bool
        Set: EnableSsl(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def Host(self) -> str:
        """
        Get: Host(self: SmtpNetworkElement) -> str
        Set: Host(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: SmtpNetworkElement) -> str
        Set: Password(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: SmtpNetworkElement) -> int
        Set: Port(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def TargetName(self) -> str:
        """
        Get: TargetName(self: SmtpNetworkElement) -> str
        Set: TargetName(self: SmtpNetworkElement) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: SmtpNetworkElement) -> str
        Set: UserName(self: SmtpNetworkElement) = value
        """
        ...



class SmtpSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SmtpSection() """
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """
        Get: DeliveryFormat(self: SmtpSection) -> SmtpDeliveryFormat
        Set: DeliveryFormat(self: SmtpSection) = value
        """
        ...

    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """
        Get: DeliveryMethod(self: SmtpSection) -> SmtpDeliveryMethod
        Set: DeliveryMethod(self: SmtpSection) = value
        """
        ...

    @property
    def From(self) -> str:
        """
        Get: From(self: SmtpSection) -> str
        Set: From(self: SmtpSection) = value
        """
        ...

    @property
    def Network(self) -> SmtpNetworkElement:
        """ Get: Network(self: SmtpSection) -> SmtpNetworkElement """
        ...

    @property
    def SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement:
        """ Get: SpecifiedPickupDirectory(self: SmtpSection) -> SmtpSpecifiedPickupDirectoryElement """
        ...



class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SmtpSpecifiedPickupDirectoryElement() """
    @property
    def PickupDirectoryLocation(self) -> str:
        """
        Get: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) -> str
        Set: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) = value
        """
        ...



class SocketElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SocketElement() """
    @property
    def AlwaysUseCompletionPortsForAccept(self) -> bool:
        """
        Get: AlwaysUseCompletionPortsForAccept(self: SocketElement) -> bool
        Set: AlwaysUseCompletionPortsForAccept(self: SocketElement) = value
        """
        ...

    @property
    def AlwaysUseCompletionPortsForConnect(self) -> bool:
        """
        Get: AlwaysUseCompletionPortsForConnect(self: SocketElement) -> bool
        Set: AlwaysUseCompletionPortsForConnect(self: SocketElement) = value
        """
        ...

    @property
    def IPProtectionLevel(self) -> IPProtectionLevel:
        """
        Get: IPProtectionLevel(self: SocketElement) -> IPProtectionLevel
        Set: IPProtectionLevel(self: SocketElement) = value
        """
        ...



class UnicodeDecodingConformance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnicodeDecodingConformance, values: Auto (0), Compat (2), Loose (3), Strict (1) """
    Auto: UnicodeDecodingConformance = ...
    Compat: UnicodeDecodingConformance = ...
    Loose: UnicodeDecodingConformance = ...
    Strict: UnicodeDecodingConformance = ...
    value__ = ...


class UnicodeEncodingConformance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnicodeEncodingConformance, values: Auto (0), Compat (2), Strict (1) """
    Auto: UnicodeEncodingConformance = ...
    Compat: UnicodeEncodingConformance = ...
    Strict: UnicodeEncodingConformance = ...
    value__ = ...


class WebProxyScriptElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WebProxyScriptElement() """
    @property
    def AutoConfigUrlRetryInterval(self) -> int:
        """
        Get: AutoConfigUrlRetryInterval(self: WebProxyScriptElement) -> int
        Set: AutoConfigUrlRetryInterval(self: WebProxyScriptElement) = value
        """
        ...

    @property
    def DownloadTimeout(self) -> TimeSpan:
        """
        Get: DownloadTimeout(self: WebProxyScriptElement) -> TimeSpan
        Set: DownloadTimeout(self: WebProxyScriptElement) = value
        """
        ...



class WebRequestModuleElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    WebRequestModuleElement()
    WebRequestModuleElement(prefix: str, type: str)
    WebRequestModuleElement(prefix: str, type: Type)
    """
    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: WebRequestModuleElement) -> str
        Set: Prefix(self: WebRequestModuleElement) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: WebRequestModuleElement) -> Type
        Set: Type(self: WebRequestModuleElement) = value
        """
        ...


    def __new__(cls, prefix:str = ..., type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, prefix: str, type: str)
        __new__(cls: type, prefix: str, type: Type)
        """
        ...


class WebRequestModuleElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WebRequestModuleElementCollection() """
    def Add(self, element:WebRequestModuleElement): # -> 
        """ Add(self: WebRequestModuleElementCollection, element: WebRequestModuleElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: WebRequestModuleElementCollection) """
        ...

    def IndexOf(self, element:WebRequestModuleElement) -> int:
        """ IndexOf(self: WebRequestModuleElementCollection, element: WebRequestModuleElement) -> int """
        ...

    def Remove(self, *__args:WebRequestModuleElement): # -> 
        """ Remove(self: WebRequestModuleElementCollection, element: WebRequestModuleElement)Remove(self: WebRequestModuleElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: WebRequestModuleElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class WebRequestModulesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WebRequestModulesSection() """
    @property
    def WebRequestModules(self) -> WebRequestModuleElementCollection:
        """ Get: WebRequestModules(self: WebRequestModulesSection) -> WebRequestModuleElementCollection """
        ...



class WebUtilityElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WebUtilityElement() """
    @property
    def UnicodeDecodingConformance(self) -> UnicodeDecodingConformance:
        """
        Get: UnicodeDecodingConformance(self: WebUtilityElement) -> UnicodeDecodingConformance
        Set: UnicodeDecodingConformance(self: WebUtilityElement) = value
        """
        ...

    @property
    def UnicodeEncodingConformance(self) -> UnicodeEncodingConformance:
        """
        Get: UnicodeEncodingConformance(self: WebUtilityElement) -> UnicodeEncodingConformance
        Set: UnicodeEncodingConformance(self: WebUtilityElement) = value
        """
        ...



class WindowsAuthenticationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WindowsAuthenticationElement() """
    @property
    def DefaultCredentialsHandleCacheSize(self) -> int:
        """
        Get: DefaultCredentialsHandleCacheSize(self: WindowsAuthenticationElement) -> int
        Set: DefaultCredentialsHandleCacheSize(self: WindowsAuthenticationElement) = value
        """
        ...



