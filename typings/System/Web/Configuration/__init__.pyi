# encoding: utf-8
# module System.Web.Configuration calls itself Configuration
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic.ApplicationServices import (AssemblyInfo, 
    AuthenticationMode)

from System import Array, Enum, Int64, IntPtr, TimeSpan, Type, Version

from System.Collections import ArrayList, ICollection, IDictionary

from System.Collections.Specialized import (NameObjectCollectionBase, 
    NameValueCollection, OrderedDictionary, StringCollection)

from System.ComponentModel import ITypeDescriptorContext, TypeConverter

from System.Configuration import (Configuration, ConfigurationConverterBase, 
    ConfigurationElement, ConfigurationElementCollection, 
    ConfigurationFileMap, ConfigurationSection, ConfigurationSectionGroup, 
    ConnectionStringSettingsCollection, DefaultSection, 
    IConfigurationSectionHandler, ProviderSettings, 
    ProviderSettingsCollection)

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.Globalization import CultureInfo

from System.IO import TextWriter

from System.Security.AccessControl import (AuthorizationRule, 
    AuthorizationRuleCollection)

from System.Text import Encoding

from System.Web import (HttpBrowserCapabilities, HttpCookieMode, HttpRequest, 
    SameSiteMode)

from System.Web.Compilation import BuildProvider, ExpressionBuilder

from System.Web.Services.Configuration import (ProtocolElement, 
    WebServicesSection)

from System.Web.SessionState import SessionStateMode

from System.Web.UI import (ClientIDMode, CompilationMode, HtmlTextWriter, 
    IFilterResolutionService, OutputCacheLocation, ViewStateEncryptionMode)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (AuthorizationRuleAction, 
    BufferModeSettings, CodeSubDirectory, CompilerCollection, 
    CookieProtection, ExpressionBuilderCollection, 
    FolderLevelBuildProviderCollection, FormsAuthPasswordFormat, 
    FormsAuthenticationConfiguration, FormsAuthenticationCredentials, 
    FormsAuthenticationUserCollection, FormsProtectionEnum, 
    FullTrustAssemblyCollection, HttpCapabilitiesProvider, 
    MachineKeyValidation, NamespaceInfo, 
    PartialTrustVisibleAssemblyCollection, PassportAuthentication, 
    ProfileGuidedOptimizationsFlags, ProfilePropertySettingsCollection, 
    ProfileSettingsCollection, RootProfilePropertySettingsCollection, 
    RuleSettingsCollection, SerializationMode, TagMapCollection, TagMapInfo, 
    TagPrefixCollection, TagPrefixInfo, TicketCompatibilityMode, TraceSection, 
    TrustLevelCollection, TrustSection, UrlMappingsSection, 
    WebControlsSection, WebPartsPersonalizationAuthorization, WebPartsSection, 
    XhtmlConformanceSection, field#)
"""

# no functions
# classes

class AdapterDictionary(OrderedDictionary): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'IOrderedDictionary'>, <type 'object'>
    """ AdapterDictionary() """
    pass

class AnonymousIdentificationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ AnonymousIdentificationSection() """
    @property
    def Cookieless(self) -> HttpCookieMode:
        """
        Get: Cookieless(self: AnonymousIdentificationSection) -> HttpCookieMode
        Set: Cookieless(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookieName(self) -> str:
        """
        Get: CookieName(self: AnonymousIdentificationSection) -> str
        Set: CookieName(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookiePath(self) -> str:
        """
        Get: CookiePath(self: AnonymousIdentificationSection) -> str
        Set: CookiePath(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookieProtection(self): # -> CookieProtection
        """
        Get: CookieProtection(self: AnonymousIdentificationSection) -> CookieProtection
        Set: CookieProtection(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookieRequireSSL(self) -> bool:
        """
        Get: CookieRequireSSL(self: AnonymousIdentificationSection) -> bool
        Set: CookieRequireSSL(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookieSlidingExpiration(self) -> bool:
        """
        Get: CookieSlidingExpiration(self: AnonymousIdentificationSection) -> bool
        Set: CookieSlidingExpiration(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def CookieTimeout(self) -> TimeSpan:
        """
        Get: CookieTimeout(self: AnonymousIdentificationSection) -> TimeSpan
        Set: CookieTimeout(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: AnonymousIdentificationSection) -> str
        Set: Domain(self: AnonymousIdentificationSection) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: AnonymousIdentificationSection) -> bool
        Set: Enabled(self: AnonymousIdentificationSection) = value
        """
        ...



class AssemblyCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AssemblyCollection() """
    def Add(self, assemblyInformation:AssemblyInfo): # -> 
        """ Add(self: AssemblyCollection, assemblyInformation: AssemblyInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: AssemblyCollection) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: AssemblyCollection, key: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: AssemblyCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class AssemblyInfo(ConfigurationElement): # skipped bases: <type 'object'>
    """ AssemblyInfo(assemblyName: str) """
    @property
    def Assembly(self) -> str:
        """
        Get: Assembly(self: AssemblyInfo) -> str
        Set: Assembly(self: AssemblyInfo) = value
        """
        ...


    def __new__(cls, assemblyName:str) -> Self:
        """ __new__(cls: type, assemblyName: str) """
        ...


class AsyncPreloadModeFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AsyncPreloadModeFlags, values: All (7), AllFormTypes (3), Form (1), FormMultiPart (2), None (0), NonForm (4) """
    All: AsyncPreloadModeFlags = ...
    AllFormTypes: AsyncPreloadModeFlags = ...
    Form: AsyncPreloadModeFlags = ...
    FormMultiPart: AsyncPreloadModeFlags = ...
    NonForm: AsyncPreloadModeFlags = ...
    value__ = ...


class AuthenticationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationMode, values: Forms (3), None (0), Passport (2), Windows (1) """
    Forms: AuthenticationMode = ...
    Passport: AuthenticationMode = ...
    value__ = ...
    Windows: AuthenticationMode = ...


class AuthenticationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ AuthenticationSection() """
    @property
    def Forms(self): # -> FormsAuthenticationConfiguration
        """ Get: Forms(self: AuthenticationSection) -> FormsAuthenticationConfiguration """
        ...

    @property
    def Mode(self) -> AuthenticationMode:
        """
        Get: Mode(self: AuthenticationSection) -> AuthenticationMode
        Set: Mode(self: AuthenticationSection) = value
        """
        ...

    @property
    def Passport(self): # -> PassportAuthentication
        """ Get: Passport(self: AuthenticationSection) -> PassportAuthentication """
        ...



class AuthorizationRule(ConfigurationElement): # skipped bases: <type 'object'>
    """ AuthorizationRule(action: AuthorizationRuleAction) """
    @property
    def Action(self): # -> AuthorizationRuleAction
        """
        Get: Action(self: AuthorizationRule) -> AuthorizationRuleAction
        Set: Action(self: AuthorizationRule) = value
        """
        ...

    @property
    def Roles(self) -> StringCollection:
        """ Get: Roles(self: AuthorizationRule) -> StringCollection """
        ...

    @property
    def Users(self) -> StringCollection:
        """ Get: Users(self: AuthorizationRule) -> StringCollection """
        ...

    @property
    def Verbs(self) -> StringCollection:
        """ Get: Verbs(self: AuthorizationRule) -> StringCollection """
        ...


    def __new__(cls, action) -> Self: # Not found arg types: {'action': 'AuthorizationRuleAction'}
        """ __new__(cls: type, action: AuthorizationRuleAction) """
        ...


class AuthorizationRuleAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthorizationRuleAction, values: Allow (1), Deny (0) """
    Allow: AuthorizationRuleAction = ...
    Deny: AuthorizationRuleAction = ...
    value__ = ...


class AuthorizationRuleCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AuthorizationRuleCollection() """
    def Add(self, rule:AuthorizationRule): # -> 
        """ Add(self: AuthorizationRuleCollection, rule: AuthorizationRule) """
        ...

    def Clear(self): # -> 
        """ Clear(self: AuthorizationRuleCollection) """
        ...

    def Get(self, index:int) -> AuthorizationRule:
        """ Get(self: AuthorizationRuleCollection, index: int) -> AuthorizationRule """
        ...

    def IndexOf(self, rule:AuthorizationRule) -> int:
        """ IndexOf(self: AuthorizationRuleCollection, rule: AuthorizationRule) -> int """
        ...

    def Remove(self, rule:AuthorizationRule): # -> 
        """ Remove(self: AuthorizationRuleCollection, rule: AuthorizationRule) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: AuthorizationRuleCollection, index: int) """
        ...

    def Set(self, index:int, rule:AuthorizationRule): # -> 
        """ Set(self: AuthorizationRuleCollection, index: int, rule: AuthorizationRule) """
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


class AuthorizationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ AuthorizationSection() """
    @property
    def Rules(self) -> AuthorizationRuleCollection:
        """ Get: Rules(self: AuthorizationSection) -> AuthorizationRuleCollection """
        ...



class BrowserCapabilitiesCodeGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ BrowserCapabilitiesCodeGenerator() """
    def Create(self): # -> 
        """ Create(self: BrowserCapabilitiesCodeGenerator) """
        ...

    def ProcessBrowserFiles(self, *args): #cannot find CLR method
        """ ProcessBrowserFiles(self: BrowserCapabilitiesCodeGenerator, useVirtualPath: bool, virtualDir: str) """
        ...

    def Uninstall(self) -> bool:
        """ Uninstall(self: BrowserCapabilitiesCodeGenerator) -> bool """
        ...


class BrowserCapabilitiesFactoryBase: # skipped bases: <type 'object'>, <type 'object'>
    """ BrowserCapabilitiesFactoryBase() """
    @property
    def BrowserElements(self):
        ...

    @property
    def MatchedHeaders(self):
        ...


    def ConfigureBrowserCapabilities(self, headers:NameValueCollection, browserCaps:HttpBrowserCapabilities): # -> 
        """ ConfigureBrowserCapabilities(self: BrowserCapabilitiesFactoryBase, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def ConfigureCustomCapabilities(self, headers:NameValueCollection, browserCaps:HttpBrowserCapabilities): # -> 
        """ ConfigureCustomCapabilities(self: BrowserCapabilitiesFactoryBase, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IsBrowserUnknown(self, *args): #cannot find CLR method
        """ IsBrowserUnknown(self: BrowserCapabilitiesFactoryBase, browserCaps: HttpCapabilitiesBase) -> bool """
        ...

    def PopulateBrowserElements(self, *args): #cannot find CLR method
        """ PopulateBrowserElements(self: BrowserCapabilitiesFactoryBase, dictionary: IDictionary) """
        ...

    def PopulateMatchedHeaders(self, *args): #cannot find CLR method
        """ PopulateMatchedHeaders(self: BrowserCapabilitiesFactoryBase, dictionary: IDictionary) """
        ...


class BrowserCapabilitiesFactory(BrowserCapabilitiesFactoryBase): # skipped bases: <type 'object'>
    """ BrowserCapabilitiesFactory() """
    def BlackberryProcessBrowsers(self, *args): #cannot find CLR method
        """ BlackberryProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def BlackberryProcessGateways(self, *args): #cannot find CLR method
        """ BlackberryProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def ChromeProcessBrowsers(self, *args): #cannot find CLR method
        """ ChromeProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def ChromeProcessGateways(self, *args): #cannot find CLR method
        """ ChromeProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def CpuProcessBrowsers(self, *args): #cannot find CLR method
        """ CpuProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def CpuProcessGateways(self, *args): #cannot find CLR method
        """ CpuProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def CrawlerProcessBrowsers(self, *args): #cannot find CLR method
        """ CrawlerProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def CrawlerProcessGateways(self, *args): #cannot find CLR method
        """ CrawlerProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def DefaultDefaultProcessBrowsers(self, *args): #cannot find CLR method
        """ DefaultDefaultProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def DefaultProcessBrowsers(self, *args): #cannot find CLR method
        """ DefaultProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def DefaultProcessGateways(self, *args): #cannot find CLR method
        """ DefaultProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def DefaultWmlProcessBrowsers(self, *args): #cannot find CLR method
        """ DefaultWmlProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def DefaultXhtmlmpProcessBrowsers(self, *args): #cannot find CLR method
        """ DefaultXhtmlmpProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox35ProcessBrowsers(self, *args): #cannot find CLR method
        """ Firefox35ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox35ProcessGateways(self, *args): #cannot find CLR method
        """ Firefox35ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox3plusProcessBrowsers(self, *args): #cannot find CLR method
        """ Firefox3plusProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox3plusProcessGateways(self, *args): #cannot find CLR method
        """ Firefox3plusProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox3ProcessBrowsers(self, *args): #cannot find CLR method
        """ Firefox3ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Firefox3ProcessGateways(self, *args): #cannot find CLR method
        """ Firefox3ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def FirefoxProcessBrowsers(self, *args): #cannot find CLR method
        """ FirefoxProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def FirefoxProcessGateways(self, *args): #cannot find CLR method
        """ FirefoxProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def GenericdownlevelProcessBrowsers(self, *args): #cannot find CLR method
        """ GenericdownlevelProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def GenericdownlevelProcessGateways(self, *args): #cannot find CLR method
        """ GenericdownlevelProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie10plusProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie10plusProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie10plusProcessGateways(self, *args): #cannot find CLR method
        """ Ie10plusProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie6plusProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie6plusProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie6plusProcessGateways(self, *args): #cannot find CLR method
        """ Ie6plusProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie6to9ProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie6to9ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie6to9ProcessGateways(self, *args): #cannot find CLR method
        """ Ie6to9ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie7ProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie7ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie7ProcessGateways(self, *args): #cannot find CLR method
        """ Ie7ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie8ProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie8ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie8ProcessGateways(self, *args): #cannot find CLR method
        """ Ie8ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie9ProcessBrowsers(self, *args): #cannot find CLR method
        """ Ie9ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Ie9ProcessGateways(self, *args): #cannot find CLR method
        """ Ie9ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IebetaProcessBrowsers(self, *args): #cannot find CLR method
        """ IebetaProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IebetaProcessGateways(self, *args): #cannot find CLR method
        """ IebetaProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IemobileProcessBrowsers(self, *args): #cannot find CLR method
        """ IemobileProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IemobileProcessGateways(self, *args): #cannot find CLR method
        """ IemobileProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IeProcessBrowsers(self, *args): #cannot find CLR method
        """ IeProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IeProcessGateways(self, *args): #cannot find CLR method
        """ IeProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def InternetexplorerProcessBrowsers(self, *args): #cannot find CLR method
        """ InternetexplorerProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def InternetexplorerProcessGateways(self, *args): #cannot find CLR method
        """ InternetexplorerProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IpadProcessBrowsers(self, *args): #cannot find CLR method
        """ IpadProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IpadProcessGateways(self, *args): #cannot find CLR method
        """ IpadProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IphoneProcessBrowsers(self, *args): #cannot find CLR method
        """ IphoneProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IphoneProcessGateways(self, *args): #cannot find CLR method
        """ IphoneProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IpodProcessBrowsers(self, *args): #cannot find CLR method
        """ IpodProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def IpodProcessGateways(self, *args): #cannot find CLR method
        """ IpodProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def MonoProcessBrowsers(self, *args): #cannot find CLR method
        """ MonoProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def MonoProcessGateways(self, *args): #cannot find CLR method
        """ MonoProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def MozillaProcessBrowsers(self, *args): #cannot find CLR method
        """ MozillaProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def MozillaProcessGateways(self, *args): #cannot find CLR method
        """ MozillaProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera10ProcessBrowsers(self, *args): #cannot find CLR method
        """ Opera10ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera10ProcessGateways(self, *args): #cannot find CLR method
        """ Opera10ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera8plusProcessBrowsers(self, *args): #cannot find CLR method
        """ Opera8plusProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera8plusProcessGateways(self, *args): #cannot find CLR method
        """ Opera8plusProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera8to9ProcessBrowsers(self, *args): #cannot find CLR method
        """ Opera8to9ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Opera8to9ProcessGateways(self, *args): #cannot find CLR method
        """ Opera8to9ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperaminiProcessBrowsers(self, *args): #cannot find CLR method
        """ OperaminiProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperaminiProcessGateways(self, *args): #cannot find CLR method
        """ OperaminiProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperamobileProcessBrowsers(self, *args): #cannot find CLR method
        """ OperamobileProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperamobileProcessGateways(self, *args): #cannot find CLR method
        """ OperamobileProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperaProcessBrowsers(self, *args): #cannot find CLR method
        """ OperaProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OperaProcessGateways(self, *args): #cannot find CLR method
        """ OperaProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OSProcessBrowsers(self, *args): #cannot find CLR method
        """ OSProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def OSProcessGateways(self, *args): #cannot find CLR method
        """ OSProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PixelsProcessBrowsers(self, *args): #cannot find CLR method
        """ PixelsProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PixelsProcessGateways(self, *args): #cannot find CLR method
        """ PixelsProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformmac68kProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformmac68kProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformmac68kProcessGateways(self, *args): #cannot find CLR method
        """ Platformmac68kProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformmacppcProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformmacppcProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformmacppcProcessGateways(self, *args): #cannot find CLR method
        """ PlatformmacppcProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformProcessGateways(self, *args): #cannot find CLR method
        """ PlatformProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformunixProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformunixProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformunixProcessGateways(self, *args): #cannot find CLR method
        """ PlatformunixProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwebtvProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformwebtvProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwebtvProcessGateways(self, *args): #cannot find CLR method
        """ PlatformwebtvProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin16ProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformwin16ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin16ProcessGateways(self, *args): #cannot find CLR method
        """ Platformwin16ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin2000aProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformwin2000aProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin2000aProcessGateways(self, *args): #cannot find CLR method
        """ Platformwin2000aProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin2000bProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformwin2000bProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin2000bProcessGateways(self, *args): #cannot find CLR method
        """ Platformwin2000bProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin95ProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformwin95ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin95ProcessGateways(self, *args): #cannot find CLR method
        """ Platformwin95ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin98ProcessBrowsers(self, *args): #cannot find CLR method
        """ Platformwin98ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Platformwin98ProcessGateways(self, *args): #cannot find CLR method
        """ Platformwin98ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinceProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformwinceProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinceProcessGateways(self, *args): #cannot find CLR method
        """ PlatformwinceProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinntProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformwinntProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinntProcessGateways(self, *args): #cannot find CLR method
        """ PlatformwinntProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinxpProcessBrowsers(self, *args): #cannot find CLR method
        """ PlatformwinxpProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def PlatformwinxpProcessGateways(self, *args): #cannot find CLR method
        """ PlatformwinxpProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari3plusProcessBrowsers(self, *args): #cannot find CLR method
        """ Safari3plusProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari3plusProcessGateways(self, *args): #cannot find CLR method
        """ Safari3plusProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari3to4ProcessBrowsers(self, *args): #cannot find CLR method
        """ Safari3to4ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari3to4ProcessGateways(self, *args): #cannot find CLR method
        """ Safari3to4ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari4ProcessBrowsers(self, *args): #cannot find CLR method
        """ Safari4ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Safari4ProcessGateways(self, *args): #cannot find CLR method
        """ Safari4ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def SafariProcessBrowsers(self, *args): #cannot find CLR method
        """ SafariProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def SafariProcessGateways(self, *args): #cannot find CLR method
        """ SafariProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def UcbrowserProcessBrowsers(self, *args): #cannot find CLR method
        """ UcbrowserProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def UcbrowserProcessGateways(self, *args): #cannot find CLR method
        """ UcbrowserProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def VoiceProcessBrowsers(self, *args): #cannot find CLR method
        """ VoiceProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def VoiceProcessGateways(self, *args): #cannot find CLR method
        """ VoiceProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WebkitmobileProcessBrowsers(self, *args): #cannot find CLR method
        """ WebkitmobileProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WebkitmobileProcessGateways(self, *args): #cannot find CLR method
        """ WebkitmobileProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WebkitProcessBrowsers(self, *args): #cannot find CLR method
        """ WebkitProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WebkitProcessGateways(self, *args): #cannot find CLR method
        """ WebkitProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Win16ProcessBrowsers(self, *args): #cannot find CLR method
        """ Win16ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Win16ProcessGateways(self, *args): #cannot find CLR method
        """ Win16ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Win32ProcessBrowsers(self, *args): #cannot find CLR method
        """ Win32ProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def Win32ProcessGateways(self, *args): #cannot find CLR method
        """ Win32ProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WindowsphoneProcessBrowsers(self, *args): #cannot find CLR method
        """ WindowsphoneProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WindowsphoneProcessGateways(self, *args): #cannot find CLR method
        """ WindowsphoneProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WinProcessBrowsers(self, *args): #cannot find CLR method
        """ WinProcessBrowsers(self: BrowserCapabilitiesFactory, ignoreApplicationBrowsers: bool, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...

    def WinProcessGateways(self, *args): #cannot find CLR method
        """ WinProcessGateways(self: BrowserCapabilitiesFactory, headers: NameValueCollection, browserCaps: HttpBrowserCapabilities) """
        ...


class BufferModesCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BufferModesCollection() """
    def Add(self, bufferModeSettings): # ->  # Not found arg types: {'bufferModeSettings': 'BufferModeSettings'}
        """ Add(self: BufferModesCollection, bufferModeSettings: BufferModeSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: BufferModesCollection) """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: BufferModesCollection, s: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class BufferModeSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """ BufferModeSettings(name: str, maxBufferSize: int, maxFlushSize: int, urgentFlushThreshold: int, regularFlushInterval: TimeSpan, urgentFlushInterval: TimeSpan, maxBufferThreads: int) """
    @property
    def MaxBufferSize(self) -> int:
        """
        Get: MaxBufferSize(self: BufferModeSettings) -> int
        Set: MaxBufferSize(self: BufferModeSettings) = value
        """
        ...

    @property
    def MaxBufferThreads(self) -> int:
        """
        Get: MaxBufferThreads(self: BufferModeSettings) -> int
        Set: MaxBufferThreads(self: BufferModeSettings) = value
        """
        ...

    @property
    def MaxFlushSize(self) -> int:
        """
        Get: MaxFlushSize(self: BufferModeSettings) -> int
        Set: MaxFlushSize(self: BufferModeSettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: BufferModeSettings) -> str
        Set: Name(self: BufferModeSettings) = value
        """
        ...

    @property
    def RegularFlushInterval(self) -> TimeSpan:
        """
        Get: RegularFlushInterval(self: BufferModeSettings) -> TimeSpan
        Set: RegularFlushInterval(self: BufferModeSettings) = value
        """
        ...

    @property
    def UrgentFlushInterval(self) -> TimeSpan:
        """
        Get: UrgentFlushInterval(self: BufferModeSettings) -> TimeSpan
        Set: UrgentFlushInterval(self: BufferModeSettings) = value
        """
        ...

    @property
    def UrgentFlushThreshold(self) -> int:
        """
        Get: UrgentFlushThreshold(self: BufferModeSettings) -> int
        Set: UrgentFlushThreshold(self: BufferModeSettings) = value
        """
        ...


    def __new__(cls, name:str, maxBufferSize:int, maxFlushSize:int, urgentFlushThreshold:int, regularFlushInterval:TimeSpan, urgentFlushInterval:TimeSpan, maxBufferThreads:int) -> Self:
        """ __new__(cls: type, name: str, maxBufferSize: int, maxFlushSize: int, urgentFlushThreshold: int, regularFlushInterval: TimeSpan, urgentFlushInterval: TimeSpan, maxBufferThreads: int) """
        ...


class BuildProvider(ConfigurationElement): # skipped bases: <type 'object'>
    """ BuildProvider(extension: str, type: str) """
    @property
    def Extension(self) -> str:
        """
        Get: Extension(self: BuildProvider) -> str
        Set: Extension(self: BuildProvider) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: BuildProvider) -> str
        Set: Type(self: BuildProvider) = value
        """
        ...


    def __new__(cls, extension:str, type:str) -> Self:
        """ __new__(cls: type, extension: str, type: str) """
        ...


class BuildProviderCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BuildProviderCollection() """
    def Add(self, buildProvider:BuildProvider): # -> 
        """ Add(self: BuildProviderCollection, buildProvider: BuildProvider) """
        ...

    def Clear(self): # -> 
        """ Clear(self: BuildProviderCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: BuildProviderCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: BuildProviderCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CacheSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ CacheSection() """
    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: CacheSection) -> str
        Set: DefaultProvider(self: CacheSection) = value
        """
        ...

    @property
    def DisableExpiration(self) -> bool:
        """
        Get: DisableExpiration(self: CacheSection) -> bool
        Set: DisableExpiration(self: CacheSection) = value
        """
        ...

    @property
    def DisableMemoryCollection(self) -> bool:
        """
        Get: DisableMemoryCollection(self: CacheSection) -> bool
        Set: DisableMemoryCollection(self: CacheSection) = value
        """
        ...

    @property
    def PercentagePhysicalMemoryUsedLimit(self) -> int:
        """
        Get: PercentagePhysicalMemoryUsedLimit(self: CacheSection) -> int
        Set: PercentagePhysicalMemoryUsedLimit(self: CacheSection) = value
        """
        ...

    @property
    def PrivateBytesLimit(self) -> Int64:
        """
        Get: PrivateBytesLimit(self: CacheSection) -> Int64
        Set: PrivateBytesLimit(self: CacheSection) = value
        """
        ...

    @property
    def PrivateBytesPollTime(self) -> TimeSpan:
        """
        Get: PrivateBytesPollTime(self: CacheSection) -> TimeSpan
        Set: PrivateBytesPollTime(self: CacheSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: CacheSection) -> ProviderSettingsCollection """
        ...



class ClientTarget(ConfigurationElement): # skipped bases: <type 'object'>
    """ ClientTarget(alias: str, userAgent: str) """
    @property
    def Alias(self) -> str:
        """ Get: Alias(self: ClientTarget) -> str """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: ClientTarget) -> str """
        ...


    def __new__(cls, alias:str, userAgent:str) -> Self:
        """ __new__(cls: type, alias: str, userAgent: str) """
        ...


class ClientTargetCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ClientTargetCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: ClientTargetCollection) -> Array[str] """
        ...


    def Add(self, clientTarget:ClientTarget): # -> 
        """ Add(self: ClientTargetCollection, clientTarget: ClientTarget) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ClientTargetCollection) """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: ClientTargetCollection, index: int) -> str """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: ClientTargetCollection, name: str)Remove(self: ClientTargetCollection, clientTarget: ClientTarget) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ClientTargetCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ClientTargetSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ClientTargetSection() """
    @property
    def ClientTargets(self) -> ClientTargetCollection:
        """ Get: ClientTargets(self: ClientTargetSection) -> ClientTargetCollection """
        ...



class CodeSubDirectoriesCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CodeSubDirectoriesCollection() """
    def Add(self, codeSubDirectory): # ->  # Not found arg types: {'codeSubDirectory': 'CodeSubDirectory'}
        """ Add(self: CodeSubDirectoriesCollection, codeSubDirectory: CodeSubDirectory) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CodeSubDirectoriesCollection) """
        ...

    def Remove(self, directoryName:str): # -> 
        """ Remove(self: CodeSubDirectoriesCollection, directoryName: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: CodeSubDirectoriesCollection, index: int) """
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


class CodeSubDirectory(ConfigurationElement): # skipped bases: <type 'object'>
    """ CodeSubDirectory(directoryName: str) """
    @property
    def DirectoryName(self) -> str:
        """
        Get: DirectoryName(self: CodeSubDirectory) -> str
        Set: DirectoryName(self: CodeSubDirectory) = value
        """
        ...


    def __new__(cls, directoryName:str) -> Self:
        """ __new__(cls: type, directoryName: str) """
        ...


class CompilationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ CompilationSection() """
    @property
    def Assemblies(self) -> AssemblyCollection:
        """ Get: Assemblies(self: CompilationSection) -> AssemblyCollection """
        ...

    @property
    def AssemblyPostProcessorType(self) -> str:
        """
        Get: AssemblyPostProcessorType(self: CompilationSection) -> str
        Set: AssemblyPostProcessorType(self: CompilationSection) = value
        """
        ...

    @property
    def Batch(self) -> bool:
        """
        Get: Batch(self: CompilationSection) -> bool
        Set: Batch(self: CompilationSection) = value
        """
        ...

    @property
    def BatchTimeout(self) -> TimeSpan:
        """
        Get: BatchTimeout(self: CompilationSection) -> TimeSpan
        Set: BatchTimeout(self: CompilationSection) = value
        """
        ...

    @property
    def BuildProviders(self) -> BuildProviderCollection:
        """ Get: BuildProviders(self: CompilationSection) -> BuildProviderCollection """
        ...

    @property
    def CodeSubDirectories(self) -> CodeSubDirectoriesCollection:
        """ Get: CodeSubDirectories(self: CompilationSection) -> CodeSubDirectoriesCollection """
        ...

    @property
    def Compilers(self): # -> CompilerCollection
        """ Get: Compilers(self: CompilationSection) -> CompilerCollection """
        ...

    @property
    def ControlBuilderInterceptorType(self) -> str:
        """
        Get: ControlBuilderInterceptorType(self: CompilationSection) -> str
        Set: ControlBuilderInterceptorType(self: CompilationSection) = value
        """
        ...

    @property
    def Debug(self) -> bool:
        """
        Get: Debug(self: CompilationSection) -> bool
        Set: Debug(self: CompilationSection) = value
        """
        ...

    @property
    def DefaultLanguage(self) -> str:
        """
        Get: DefaultLanguage(self: CompilationSection) -> str
        Set: DefaultLanguage(self: CompilationSection) = value
        """
        ...

    @property
    def DisableObsoleteWarnings(self) -> bool:
        """
        Get: DisableObsoleteWarnings(self: CompilationSection) -> bool
        Set: DisableObsoleteWarnings(self: CompilationSection) = value
        """
        ...

    @property
    def EnablePrefetchOptimization(self) -> bool:
        """
        Get: EnablePrefetchOptimization(self: CompilationSection) -> bool
        Set: EnablePrefetchOptimization(self: CompilationSection) = value
        """
        ...

    @property
    def Explicit(self) -> bool:
        """
        Get: Explicit(self: CompilationSection) -> bool
        Set: Explicit(self: CompilationSection) = value
        """
        ...

    @property
    def ExpressionBuilders(self): # -> ExpressionBuilderCollection
        """ Get: ExpressionBuilders(self: CompilationSection) -> ExpressionBuilderCollection """
        ...

    @property
    def FolderLevelBuildProviders(self): # -> FolderLevelBuildProviderCollection
        """ Get: FolderLevelBuildProviders(self: CompilationSection) -> FolderLevelBuildProviderCollection """
        ...

    @property
    def MaxBatchGeneratedFileSize(self) -> int:
        """
        Get: MaxBatchGeneratedFileSize(self: CompilationSection) -> int
        Set: MaxBatchGeneratedFileSize(self: CompilationSection) = value
        """
        ...

    @property
    def MaxBatchSize(self) -> int:
        """
        Get: MaxBatchSize(self: CompilationSection) -> int
        Set: MaxBatchSize(self: CompilationSection) = value
        """
        ...

    @property
    def MaxConcurrentCompilations(self) -> int:
        """
        Get: MaxConcurrentCompilations(self: CompilationSection) -> int
        Set: MaxConcurrentCompilations(self: CompilationSection) = value
        """
        ...

    @property
    def NumRecompilesBeforeAppRestart(self) -> int:
        """
        Get: NumRecompilesBeforeAppRestart(self: CompilationSection) -> int
        Set: NumRecompilesBeforeAppRestart(self: CompilationSection) = value
        """
        ...

    @property
    def OptimizeCompilations(self) -> bool:
        """
        Get: OptimizeCompilations(self: CompilationSection) -> bool
        Set: OptimizeCompilations(self: CompilationSection) = value
        """
        ...

    @property
    def ProfileGuidedOptimizations(self): # -> ProfileGuidedOptimizationsFlags
        """
        Get: ProfileGuidedOptimizations(self: CompilationSection) -> ProfileGuidedOptimizationsFlags
        Set: ProfileGuidedOptimizations(self: CompilationSection) = value
        """
        ...

    @property
    def Strict(self) -> bool:
        """
        Get: Strict(self: CompilationSection) -> bool
        Set: Strict(self: CompilationSection) = value
        """
        ...

    @property
    def TargetFramework(self) -> str:
        """
        Get: TargetFramework(self: CompilationSection) -> str
        Set: TargetFramework(self: CompilationSection) = value
        """
        ...

    @property
    def TempDirectory(self) -> str:
        """
        Get: TempDirectory(self: CompilationSection) -> str
        Set: TempDirectory(self: CompilationSection) = value
        """
        ...

    @property
    def UrlLinePragmas(self) -> bool:
        """
        Get: UrlLinePragmas(self: CompilationSection) -> bool
        Set: UrlLinePragmas(self: CompilationSection) = value
        """
        ...



class Compiler(ConfigurationElement): # skipped bases: <type 'object'>
    """ Compiler(compilerOptions: str, extension: str, language: str, type: str, warningLevel: int) """
    @property
    def CompilerOptions(self) -> str:
        """ Get: CompilerOptions(self: Compiler) -> str """
        ...

    @property
    def Extension(self) -> str:
        """ Get: Extension(self: Compiler) -> str """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: Compiler) -> str """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: Compiler) -> str """
        ...

    @property
    def WarningLevel(self) -> int:
        """ Get: WarningLevel(self: Compiler) -> int """
        ...


    def __new__(cls, compilerOptions:str, extension:str, language:str, type:str, warningLevel:int) -> Self:
        """ __new__(cls: type, compilerOptions: str, extension: str, language: str, type: str, warningLevel: int) """
        ...


class CompilerCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CompilerCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: CompilerCollection) -> Array[str] """
        ...


    def Get(self, *__args:int) -> Compiler:
        """
        Get(self: CompilerCollection, index: int) -> Compiler
        Get(self: CompilerCollection, language: str) -> Compiler
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: CompilerCollection, index: int) -> str """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class Converter(ConfigurationElement): # skipped bases: <type 'object'>
    """ Converter() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: Converter) -> str
        Set: Name(self: Converter) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: Converter) -> str
        Set: Type(self: Converter) = value
        """
        ...



class ConvertersCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ConvertersCollection() """
    def Add(self, converter:Converter): # -> 
        """ Add(self: ConvertersCollection, converter: Converter) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConvertersCollection) """
        ...

    def Remove(self, converter:Converter): # -> 
        """ Remove(self: ConvertersCollection, converter: Converter) """
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


class CustomError(ConfigurationElement): # skipped bases: <type 'object'>
    """ CustomError(statusCode: int, redirect: str) """
    @property
    def Redirect(self) -> str:
        """
        Get: Redirect(self: CustomError) -> str
        Set: Redirect(self: CustomError) = value
        """
        ...

    @property
    def StatusCode(self) -> int:
        """
        Get: StatusCode(self: CustomError) -> int
        Set: StatusCode(self: CustomError) = value
        """
        ...


    def __new__(cls, statusCode:int, redirect:str) -> Self:
        """ __new__(cls: type, statusCode: int, redirect: str) """
        ...


class CustomErrorCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CustomErrorCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: CustomErrorCollection) -> Array[str] """
        ...


    def Add(self, customError:CustomError): # -> 
        """ Add(self: CustomErrorCollection, customError: CustomError) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CustomErrorCollection) """
        ...

    def Get(self, *__args:int) -> CustomError:
        """
        Get(self: CustomErrorCollection, index: int) -> CustomError
        Get(self: CustomErrorCollection, statusCode: str) -> CustomError
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: CustomErrorCollection, index: int) -> str """
        ...

    def Remove(self, statusCode:str): # -> 
        """ Remove(self: CustomErrorCollection, statusCode: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: CustomErrorCollection, index: int) """
        ...

    def Set(self, customError:CustomError): # -> 
        """ Set(self: CustomErrorCollection, customError: CustomError) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CustomErrorsMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CustomErrorsMode, values: Off (2), On (1), RemoteOnly (0) """
    Off: CustomErrorsMode = ...
    On: CustomErrorsMode = ...
    RemoteOnly: CustomErrorsMode = ...
    value__ = ...


class CustomErrorsRedirectMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CustomErrorsRedirectMode, values: ResponseRedirect (0), ResponseRewrite (1) """
    ResponseRedirect: CustomErrorsRedirectMode = ...
    ResponseRewrite: CustomErrorsRedirectMode = ...
    value__ = ...


class CustomErrorsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ CustomErrorsSection() """
    @property
    def AllowNestedErrors(self) -> bool:
        """
        Get: AllowNestedErrors(self: CustomErrorsSection) -> bool
        Set: AllowNestedErrors(self: CustomErrorsSection) = value
        """
        ...

    @property
    def DefaultRedirect(self) -> str:
        """
        Get: DefaultRedirect(self: CustomErrorsSection) -> str
        Set: DefaultRedirect(self: CustomErrorsSection) = value
        """
        ...

    @property
    def Errors(self) -> CustomErrorCollection:
        """ Get: Errors(self: CustomErrorsSection) -> CustomErrorCollection """
        ...

    @property
    def Mode(self) -> CustomErrorsMode:
        """
        Get: Mode(self: CustomErrorsSection) -> CustomErrorsMode
        Set: Mode(self: CustomErrorsSection) = value
        """
        ...

    @property
    def RedirectMode(self) -> CustomErrorsRedirectMode:
        """
        Get: RedirectMode(self: CustomErrorsSection) -> CustomErrorsRedirectMode
        Set: RedirectMode(self: CustomErrorsSection) = value
        """
        ...



class DeploymentSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DeploymentSection() """
    @property
    def Retail(self) -> bool:
        """
        Get: Retail(self: DeploymentSection) -> bool
        Set: Retail(self: DeploymentSection) = value
        """
        ...



class EventMappingSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    EventMappingSettings(name: str, type: str, startEventCode: int, endEventCode: int)
    EventMappingSettings(name: str, type: str)
    """
    @property
    def EndEventCode(self) -> int:
        """
        Get: EndEventCode(self: EventMappingSettings) -> int
        Set: EndEventCode(self: EventMappingSettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EventMappingSettings) -> str
        Set: Name(self: EventMappingSettings) = value
        """
        ...

    @property
    def StartEventCode(self) -> int:
        """
        Get: StartEventCode(self: EventMappingSettings) -> int
        Set: StartEventCode(self: EventMappingSettings) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: EventMappingSettings) -> str
        Set: Type(self: EventMappingSettings) = value
        """
        ...


    def __new__(cls, name:str, type:str, startEventCode:int = ..., endEventCode:int = ...) -> Self:
        """
        __new__(cls: type, name: str, type: str, startEventCode: int, endEventCode: int)
        __new__(cls: type, name: str, type: str)
        """
        ...


class EventMappingSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ EventMappingSettingsCollection() """
    def Add(self, eventMappingSettings:EventMappingSettings): # -> 
        """ Add(self: EventMappingSettingsCollection, eventMappingSettings: EventMappingSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: EventMappingSettingsCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: EventMappingSettingsCollection, name: str) -> bool """
        ...

    def IndexOf(self, name:str) -> int:
        """ IndexOf(self: EventMappingSettingsCollection, name: str) -> int """
        ...

    def Insert(self, index:int, eventMappingSettings:EventMappingSettings): # -> 
        """ Insert(self: EventMappingSettingsCollection, index: int, eventMappingSettings: EventMappingSettings) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: EventMappingSettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: EventMappingSettingsCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ExpressionBuilder(ConfigurationElement): # skipped bases: <type 'object'>
    """ ExpressionBuilder(expressionPrefix: str, theType: str) """
    @property
    def ExpressionPrefix(self) -> str:
        """
        Get: ExpressionPrefix(self: ExpressionBuilder) -> str
        Set: ExpressionPrefix(self: ExpressionBuilder) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ExpressionBuilder) -> str
        Set: Type(self: ExpressionBuilder) = value
        """
        ...


    def __new__(cls, expressionPrefix:str, theType:str) -> Self:
        """ __new__(cls: type, expressionPrefix: str, theType: str) """
        ...


class ExpressionBuilderCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ExpressionBuilderCollection() """
    def Add(self, buildProvider:ExpressionBuilder): # -> 
        """ Add(self: ExpressionBuilderCollection, buildProvider: ExpressionBuilder) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ExpressionBuilderCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ExpressionBuilderCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ExpressionBuilderCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class FcnMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FcnMode, values: Default (1), Disabled (2), NotSet (0), Single (3) """
    Default: FcnMode = ...
    Disabled: FcnMode = ...
    NotSet: FcnMode = ...
    Single: FcnMode = ...
    value__ = ...


class FolderLevelBuildProvider(ConfigurationElement): # skipped bases: <type 'object'>
    """ FolderLevelBuildProvider(name: str, type: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: FolderLevelBuildProvider) -> str
        Set: Name(self: FolderLevelBuildProvider) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: FolderLevelBuildProvider) -> str
        Set: Type(self: FolderLevelBuildProvider) = value
        """
        ...


    def __new__(cls, name:str, type:str) -> Self:
        """ __new__(cls: type, name: str, type: str) """
        ...


class FolderLevelBuildProviderCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ FolderLevelBuildProviderCollection() """
    def Add(self, buildProvider:FolderLevelBuildProvider): # -> 
        """ Add(self: FolderLevelBuildProviderCollection, buildProvider: FolderLevelBuildProvider) """
        ...

    def Clear(self): # -> 
        """ Clear(self: FolderLevelBuildProviderCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: FolderLevelBuildProviderCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: FolderLevelBuildProviderCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class FormsAuthenticationConfiguration(ConfigurationElement): # skipped bases: <type 'object'>
    """ FormsAuthenticationConfiguration() """
    @property
    def Cookieless(self) -> HttpCookieMode:
        """
        Get: Cookieless(self: FormsAuthenticationConfiguration) -> HttpCookieMode
        Set: Cookieless(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def CookieSameSite(self) -> SameSiteMode:
        """
        Get: CookieSameSite(self: FormsAuthenticationConfiguration) -> SameSiteMode
        Set: CookieSameSite(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Credentials(self): # -> FormsAuthenticationCredentials
        """ Get: Credentials(self: FormsAuthenticationConfiguration) -> FormsAuthenticationCredentials """
        ...

    @property
    def DefaultUrl(self) -> str:
        """
        Get: DefaultUrl(self: FormsAuthenticationConfiguration) -> str
        Set: DefaultUrl(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: FormsAuthenticationConfiguration) -> str
        Set: Domain(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def EnableCrossAppRedirects(self) -> bool:
        """
        Get: EnableCrossAppRedirects(self: FormsAuthenticationConfiguration) -> bool
        Set: EnableCrossAppRedirects(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def LoginUrl(self) -> str:
        """
        Get: LoginUrl(self: FormsAuthenticationConfiguration) -> str
        Set: LoginUrl(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FormsAuthenticationConfiguration) -> str
        Set: Name(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: FormsAuthenticationConfiguration) -> str
        Set: Path(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Protection(self): # -> FormsProtectionEnum
        """
        Get: Protection(self: FormsAuthenticationConfiguration) -> FormsProtectionEnum
        Set: Protection(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def RequireSSL(self) -> bool:
        """
        Get: RequireSSL(self: FormsAuthenticationConfiguration) -> bool
        Set: RequireSSL(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def SlidingExpiration(self) -> bool:
        """
        Get: SlidingExpiration(self: FormsAuthenticationConfiguration) -> bool
        Set: SlidingExpiration(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def TicketCompatibilityMode(self): # -> TicketCompatibilityMode
        """
        Get: TicketCompatibilityMode(self: FormsAuthenticationConfiguration) -> TicketCompatibilityMode
        Set: TicketCompatibilityMode(self: FormsAuthenticationConfiguration) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: FormsAuthenticationConfiguration) -> TimeSpan
        Set: Timeout(self: FormsAuthenticationConfiguration) = value
        """
        ...



class FormsAuthenticationCredentials(ConfigurationElement): # skipped bases: <type 'object'>
    """ FormsAuthenticationCredentials() """
    @property
    def PasswordFormat(self): # -> FormsAuthPasswordFormat
        """
        Get: PasswordFormat(self: FormsAuthenticationCredentials) -> FormsAuthPasswordFormat
        Set: PasswordFormat(self: FormsAuthenticationCredentials) = value
        """
        ...

    @property
    def Users(self): # -> FormsAuthenticationUserCollection
        """ Get: Users(self: FormsAuthenticationCredentials) -> FormsAuthenticationUserCollection """
        ...



class FormsAuthenticationUser(ConfigurationElement): # skipped bases: <type 'object'>
    """ FormsAuthenticationUser(name: str, password: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: FormsAuthenticationUser) -> str
        Set: Name(self: FormsAuthenticationUser) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: FormsAuthenticationUser) -> str
        Set: Password(self: FormsAuthenticationUser) = value
        """
        ...


    def __new__(cls, name:str, password:str) -> Self:
        """ __new__(cls: type, name: str, password: str) """
        ...


class FormsAuthenticationUserCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ FormsAuthenticationUserCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: FormsAuthenticationUserCollection) -> Array[str] """
        ...


    def Add(self, user:FormsAuthenticationUser): # -> 
        """ Add(self: FormsAuthenticationUserCollection, user: FormsAuthenticationUser) """
        ...

    def Clear(self): # -> 
        """ Clear(self: FormsAuthenticationUserCollection) """
        ...

    def Get(self, *__args:int) -> FormsAuthenticationUser:
        """
        Get(self: FormsAuthenticationUserCollection, index: int) -> FormsAuthenticationUser
        Get(self: FormsAuthenticationUserCollection, name: str) -> FormsAuthenticationUser
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: FormsAuthenticationUserCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: FormsAuthenticationUserCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: FormsAuthenticationUserCollection, index: int) """
        ...

    def Set(self, user:FormsAuthenticationUser): # -> 
        """ Set(self: FormsAuthenticationUserCollection, user: FormsAuthenticationUser) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class FormsAuthPasswordFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormsAuthPasswordFormat, values: Clear (0), MD5 (2), SHA1 (1), SHA256 (3), SHA384 (4), SHA512 (5) """
    Clear: FormsAuthPasswordFormat = ...
    MD5: FormsAuthPasswordFormat = ...
    SHA1: FormsAuthPasswordFormat = ...
    SHA256: FormsAuthPasswordFormat = ...
    SHA384: FormsAuthPasswordFormat = ...
    SHA512: FormsAuthPasswordFormat = ...
    value__ = ...


class FormsProtectionEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormsProtectionEnum, values: All (0), Encryption (2), None (1), Validation (3) """
    All: FormsProtectionEnum = ...
    Encryption: FormsProtectionEnum = ...
    Validation: FormsProtectionEnum = ...
    value__ = ...


class FullTrustAssembliesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ FullTrustAssembliesSection() """
    @property
    def FullTrustAssemblies(self): # -> FullTrustAssemblyCollection
        """ Get: FullTrustAssemblies(self: FullTrustAssembliesSection) -> FullTrustAssemblyCollection """
        ...



class FullTrustAssembly(ConfigurationElement): # skipped bases: <type 'object'>
    """ FullTrustAssembly(assemblyName: str, version: str, publicKey: str) """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: FullTrustAssembly) -> str
        Set: AssemblyName(self: FullTrustAssembly) = value
        """
        ...

    @property
    def PublicKey(self) -> str:
        """
        Get: PublicKey(self: FullTrustAssembly) -> str
        Set: PublicKey(self: FullTrustAssembly) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: FullTrustAssembly) -> str
        Set: Version(self: FullTrustAssembly) = value
        """
        ...


    def __new__(cls, assemblyName:str, version:str, publicKey:str) -> Self:
        """ __new__(cls: type, assemblyName: str, version: str, publicKey: str) """
        ...


class FullTrustAssemblyCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ FullTrustAssemblyCollection() """
    def Add(self, fullTrustAssembly:FullTrustAssembly): # -> 
        """ Add(self: FullTrustAssemblyCollection, fullTrustAssembly: FullTrustAssembly) """
        ...

    def Clear(self): # -> 
        """ Clear(self: FullTrustAssemblyCollection) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: FullTrustAssemblyCollection, key: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: FullTrustAssemblyCollection, index: int) """
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


class GlobalizationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ GlobalizationSection() """
    @property
    def Culture(self) -> str:
        """
        Get: Culture(self: GlobalizationSection) -> str
        Set: Culture(self: GlobalizationSection) = value
        """
        ...

    @property
    def EnableBestFitResponseEncoding(self) -> bool:
        """
        Get: EnableBestFitResponseEncoding(self: GlobalizationSection) -> bool
        Set: EnableBestFitResponseEncoding(self: GlobalizationSection) = value
        """
        ...

    @property
    def EnableClientBasedCulture(self) -> bool:
        """
        Get: EnableClientBasedCulture(self: GlobalizationSection) -> bool
        Set: EnableClientBasedCulture(self: GlobalizationSection) = value
        """
        ...

    @property
    def FileEncoding(self) -> Encoding:
        """
        Get: FileEncoding(self: GlobalizationSection) -> Encoding
        Set: FileEncoding(self: GlobalizationSection) = value
        """
        ...

    @property
    def RequestEncoding(self) -> Encoding:
        """
        Get: RequestEncoding(self: GlobalizationSection) -> Encoding
        Set: RequestEncoding(self: GlobalizationSection) = value
        """
        ...

    @property
    def ResourceProviderFactoryType(self) -> str:
        """
        Get: ResourceProviderFactoryType(self: GlobalizationSection) -> str
        Set: ResourceProviderFactoryType(self: GlobalizationSection) = value
        """
        ...

    @property
    def ResponseEncoding(self) -> Encoding:
        """
        Get: ResponseEncoding(self: GlobalizationSection) -> Encoding
        Set: ResponseEncoding(self: GlobalizationSection) = value
        """
        ...

    @property
    def ResponseHeaderEncoding(self) -> Encoding:
        """
        Get: ResponseHeaderEncoding(self: GlobalizationSection) -> Encoding
        Set: ResponseHeaderEncoding(self: GlobalizationSection) = value
        """
        ...

    @property
    def UICulture(self) -> str:
        """
        Get: UICulture(self: GlobalizationSection) -> str
        Set: UICulture(self: GlobalizationSection) = value
        """
        ...



class HealthMonitoringSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HealthMonitoringSection() """
    @property
    def BufferModes(self) -> BufferModesCollection:
        """ Get: BufferModes(self: HealthMonitoringSection) -> BufferModesCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: HealthMonitoringSection) -> bool
        Set: Enabled(self: HealthMonitoringSection) = value
        """
        ...

    @property
    def EventMappings(self) -> EventMappingSettingsCollection:
        """ Get: EventMappings(self: HealthMonitoringSection) -> EventMappingSettingsCollection """
        ...

    @property
    def HeartbeatInterval(self) -> TimeSpan:
        """
        Get: HeartbeatInterval(self: HealthMonitoringSection) -> TimeSpan
        Set: HeartbeatInterval(self: HealthMonitoringSection) = value
        """
        ...

    @property
    def Profiles(self): # -> ProfileSettingsCollection
        """ Get: Profiles(self: HealthMonitoringSection) -> ProfileSettingsCollection """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: HealthMonitoringSection) -> ProviderSettingsCollection """
        ...

    @property
    def Rules(self): # -> RuleSettingsCollection
        """ Get: Rules(self: HealthMonitoringSection) -> RuleSettingsCollection """
        ...



class HostingEnvironmentSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HostingEnvironmentSection() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: HostingEnvironmentSection) -> TimeSpan
        Set: IdleTimeout(self: HostingEnvironmentSection) = value
        """
        ...

    @property
    def ShadowCopyBinAssemblies(self) -> bool:
        """
        Get: ShadowCopyBinAssemblies(self: HostingEnvironmentSection) -> bool
        Set: ShadowCopyBinAssemblies(self: HostingEnvironmentSection) = value
        """
        ...

    @property
    def ShutdownTimeout(self) -> TimeSpan:
        """
        Get: ShutdownTimeout(self: HostingEnvironmentSection) -> TimeSpan
        Set: ShutdownTimeout(self: HostingEnvironmentSection) = value
        """
        ...

    @property
    def UrlMetadataSlidingExpiration(self) -> TimeSpan:
        """
        Get: UrlMetadataSlidingExpiration(self: HostingEnvironmentSection) -> TimeSpan
        Set: UrlMetadataSlidingExpiration(self: HostingEnvironmentSection) = value
        """
        ...



class HttpCapabilitiesBase(IFilterResolutionService): # skipped bases: <type 'object'>
    """ HttpCapabilitiesBase() """
    @property
    def ActiveXControls(self) -> bool:
        """ Get: ActiveXControls(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Adapters(self) -> IDictionary:
        """ Get: Adapters(self: HttpCapabilitiesBase) -> IDictionary """
        ...

    @property
    def AOL(self) -> bool:
        """ Get: AOL(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def BackgroundSounds(self) -> bool:
        """ Get: BackgroundSounds(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Beta(self) -> bool:
        """ Get: Beta(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Browser(self) -> str:
        """ Get: Browser(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def BrowserCapabilitiesProvider(self): # -> HttpCapabilitiesProvider
        """
        Get: BrowserCapabilitiesProvider() -> HttpCapabilitiesProvider
        Set: BrowserCapabilitiesProvider() = value
        """
        ...

    @property
    def Browsers(self) -> ArrayList:
        """ Get: Browsers(self: HttpCapabilitiesBase) -> ArrayList """
        ...

    @property
    def CanCombineFormsInDeck(self) -> bool:
        """ Get: CanCombineFormsInDeck(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanInitiateVoiceCall(self) -> bool:
        """ Get: CanInitiateVoiceCall(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderAfterInputOrSelectElement(self) -> bool:
        """ Get: CanRenderAfterInputOrSelectElement(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderEmptySelects(self) -> bool:
        """ Get: CanRenderEmptySelects(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderInputAndSelectElementsTogether(self) -> bool:
        """ Get: CanRenderInputAndSelectElementsTogether(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderMixedSelects(self) -> bool:
        """ Get: CanRenderMixedSelects(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderOneventAndPrevElementsTogether(self) -> bool:
        """ Get: CanRenderOneventAndPrevElementsTogether(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderPostBackCards(self) -> bool:
        """ Get: CanRenderPostBackCards(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderSetvarZeroWithMultiSelectionList(self) -> bool:
        """ Get: CanRenderSetvarZeroWithMultiSelectionList(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def CanSendMail(self) -> bool:
        """ Get: CanSendMail(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Capabilities(self) -> IDictionary:
        """
        Get: Capabilities(self: HttpCapabilitiesBase) -> IDictionary
        Set: Capabilities(self: HttpCapabilitiesBase) = value
        """
        ...

    @property
    def CDF(self) -> bool:
        """ Get: CDF(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def ClrVersion(self) -> Version:
        """ Get: ClrVersion(self: HttpCapabilitiesBase) -> Version """
        ...

    @property
    def Cookies(self) -> bool:
        """ Get: Cookies(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Crawler(self) -> bool:
        """ Get: Crawler(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def DefaultSubmitButtonLimit(self) -> int:
        """ Get: DefaultSubmitButtonLimit(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def EcmaScriptVersion(self) -> Version:
        """ Get: EcmaScriptVersion(self: HttpCapabilitiesBase) -> Version """
        ...

    @property
    def Frames(self) -> bool:
        """ Get: Frames(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def GatewayMajorVersion(self) -> int:
        """ Get: GatewayMajorVersion(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def GatewayMinorVersion(self) -> float:
        """ Get: GatewayMinorVersion(self: HttpCapabilitiesBase) -> float """
        ...

    @property
    def GatewayVersion(self) -> str:
        """ Get: GatewayVersion(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def HasBackButton(self) -> bool:
        """ Get: HasBackButton(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def HidesRightAlignedMultiselectScrollbars(self) -> bool:
        """ Get: HidesRightAlignedMultiselectScrollbars(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def HtmlTextWriter(self) -> str:
        """
        Get: HtmlTextWriter(self: HttpCapabilitiesBase) -> str
        Set: HtmlTextWriter(self: HttpCapabilitiesBase) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def InputType(self) -> str:
        """ Get: InputType(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def IsColor(self) -> bool:
        """ Get: IsColor(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def IsMobileDevice(self) -> bool:
        """ Get: IsMobileDevice(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def JavaApplets(self) -> bool:
        """ Get: JavaApplets(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def JavaScript(self) -> bool:
        """ Get: JavaScript(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def JScriptVersion(self) -> Version:
        """ Get: JScriptVersion(self: HttpCapabilitiesBase) -> Version """
        ...

    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def MaximumHrefLength(self) -> int:
        """ Get: MaximumHrefLength(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def MaximumRenderedPageSize(self) -> int:
        """ Get: MaximumRenderedPageSize(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def MaximumSoftkeyLabelLength(self) -> int:
        """ Get: MaximumSoftkeyLabelLength(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def MinorVersion(self) -> float:
        """ Get: MinorVersion(self: HttpCapabilitiesBase) -> float """
        ...

    @property
    def MinorVersionString(self) -> str:
        """ Get: MinorVersionString(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def MobileDeviceManufacturer(self) -> str:
        """ Get: MobileDeviceManufacturer(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def MobileDeviceModel(self) -> str:
        """ Get: MobileDeviceModel(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def MSDomVersion(self) -> Version:
        """ Get: MSDomVersion(self: HttpCapabilitiesBase) -> Version """
        ...

    @property
    def NumberOfSoftkeys(self) -> int:
        """ Get: NumberOfSoftkeys(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def Platform(self) -> str:
        """ Get: Platform(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def PreferredImageMime(self) -> str:
        """ Get: PreferredImageMime(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRenderingMime(self) -> str:
        """ Get: PreferredRenderingMime(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRenderingType(self) -> str:
        """ Get: PreferredRenderingType(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRequestEncoding(self) -> str:
        """ Get: PreferredRequestEncoding(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def PreferredResponseEncoding(self) -> str:
        """ Get: PreferredResponseEncoding(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def RendersBreakBeforeWmlSelectAndInput(self) -> bool:
        """ Get: RendersBreakBeforeWmlSelectAndInput(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterHtmlLists(self) -> bool:
        """ Get: RendersBreaksAfterHtmlLists(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterWmlAnchor(self) -> bool:
        """ Get: RendersBreaksAfterWmlAnchor(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterWmlInput(self) -> bool:
        """ Get: RendersBreaksAfterWmlInput(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RendersWmlDoAcceptsInline(self) -> bool:
        """ Get: RendersWmlDoAcceptsInline(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RendersWmlSelectsAsMenuCards(self) -> bool:
        """ Get: RendersWmlSelectsAsMenuCards(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiredMetaTagNameValue(self) -> str:
        """ Get: RequiredMetaTagNameValue(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def RequiresAttributeColonSubstitution(self) -> bool:
        """ Get: RequiresAttributeColonSubstitution(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresContentTypeMetaTag(self) -> bool:
        """ Get: RequiresContentTypeMetaTag(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresControlStateInSession(self) -> bool:
        """ Get: RequiresControlStateInSession(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresDBCSCharacter(self) -> bool:
        """ Get: RequiresDBCSCharacter(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresHtmlAdaptiveErrorReporting(self) -> bool:
        """ Get: RequiresHtmlAdaptiveErrorReporting(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresLeadingPageBreak(self) -> bool:
        """ Get: RequiresLeadingPageBreak(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresNoBreakInFormatting(self) -> bool:
        """ Get: RequiresNoBreakInFormatting(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresOutputOptimization(self) -> bool:
        """ Get: RequiresOutputOptimization(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresPhoneNumbersAsPlainText(self) -> bool:
        """ Get: RequiresPhoneNumbersAsPlainText(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresSpecialViewStateEncoding(self) -> bool:
        """ Get: RequiresSpecialViewStateEncoding(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueFilePathSuffix(self) -> bool:
        """ Get: RequiresUniqueFilePathSuffix(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueHtmlCheckboxNames(self) -> bool:
        """ Get: RequiresUniqueHtmlCheckboxNames(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueHtmlInputNames(self) -> bool:
        """ Get: RequiresUniqueHtmlInputNames(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUrlEncodedPostfieldValues(self) -> bool:
        """ Get: RequiresUrlEncodedPostfieldValues(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def ScreenBitDepth(self) -> int:
        """ Get: ScreenBitDepth(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def ScreenCharactersHeight(self) -> int:
        """ Get: ScreenCharactersHeight(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def ScreenCharactersWidth(self) -> int:
        """ Get: ScreenCharactersWidth(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def ScreenPixelsHeight(self) -> int:
        """ Get: ScreenPixelsHeight(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def ScreenPixelsWidth(self) -> int:
        """ Get: ScreenPixelsWidth(self: HttpCapabilitiesBase) -> int """
        ...

    @property
    def SupportsAccesskeyAttribute(self) -> bool:
        """ Get: SupportsAccesskeyAttribute(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsBodyColor(self) -> bool:
        """ Get: SupportsBodyColor(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsBold(self) -> bool:
        """ Get: SupportsBold(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCacheControlMetaTag(self) -> bool:
        """ Get: SupportsCacheControlMetaTag(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCallback(self) -> bool:
        """ Get: SupportsCallback(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCss(self) -> bool:
        """ Get: SupportsCss(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsDivAlign(self) -> bool:
        """ Get: SupportsDivAlign(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsDivNoWrap(self) -> bool:
        """ Get: SupportsDivNoWrap(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsEmptyStringInCookieValue(self) -> bool:
        """ Get: SupportsEmptyStringInCookieValue(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontColor(self) -> bool:
        """ Get: SupportsFontColor(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontName(self) -> bool:
        """ Get: SupportsFontName(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontSize(self) -> bool:
        """ Get: SupportsFontSize(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsImageSubmit(self) -> bool:
        """ Get: SupportsImageSubmit(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsIModeSymbols(self) -> bool:
        """ Get: SupportsIModeSymbols(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsInputIStyle(self) -> bool:
        """ Get: SupportsInputIStyle(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsInputMode(self) -> bool:
        """ Get: SupportsInputMode(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsItalic(self) -> bool:
        """ Get: SupportsItalic(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsJPhoneMultiMediaAttributes(self) -> bool:
        """ Get: SupportsJPhoneMultiMediaAttributes(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsJPhoneSymbols(self) -> bool:
        """ Get: SupportsJPhoneSymbols(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsQueryStringInFormAction(self) -> bool:
        """ Get: SupportsQueryStringInFormAction(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsRedirectWithCookie(self) -> bool:
        """ Get: SupportsRedirectWithCookie(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsSelectMultiple(self) -> bool:
        """ Get: SupportsSelectMultiple(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsUncheck(self) -> bool:
        """ Get: SupportsUncheck(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsXmlHttp(self) -> bool:
        """ Get: SupportsXmlHttp(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Tables(self) -> bool:
        """ Get: Tables(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def TagWriter(self) -> Type:
        """ Get: TagWriter(self: HttpCapabilitiesBase) -> Type """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def UseOptimizedCacheKey(self) -> bool:
        """ Get: UseOptimizedCacheKey(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def VBScript(self) -> bool:
        """ Get: VBScript(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: HttpCapabilitiesBase) -> str """
        ...

    @property
    def W3CDomVersion(self) -> Version:
        """ Get: W3CDomVersion(self: HttpCapabilitiesBase) -> Version """
        ...

    @property
    def Win16(self) -> bool:
        """ Get: Win16(self: HttpCapabilitiesBase) -> bool """
        ...

    @property
    def Win32(self) -> bool:
        """ Get: Win32(self: HttpCapabilitiesBase) -> bool """
        ...


    def AddBrowser(self, browserName:str): # -> 
        """ AddBrowser(self: HttpCapabilitiesBase, browserName: str) """
        ...

    def CreateHtmlTextWriter(self, w:TextWriter) -> HtmlTextWriter:
        """ CreateHtmlTextWriter(self: HttpCapabilitiesBase, w: TextWriter) -> HtmlTextWriter """
        ...

    def DisableOptimizedCacheKey(self): # -> 
        """ DisableOptimizedCacheKey(self: HttpCapabilitiesBase) """
        ...

    def GetClrVersions(self) -> Array:
        """ GetClrVersions(self: HttpCapabilitiesBase) -> Array[Version] """
        ...

    @staticmethod
    def GetConfigCapabilities(configKey:str, request:HttpRequest) -> HttpCapabilitiesBase:
        """ GetConfigCapabilities(configKey: str, request: HttpRequest) -> HttpCapabilitiesBase """
        ...

    def Init(self, *args): #cannot find CLR method
        """ Init(self: HttpCapabilitiesBase) """
        ...

    def IsBrowser(self, browserName:str) -> bool:
        """ IsBrowser(self: HttpCapabilitiesBase, browserName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HttpCapabilitiesProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetBrowserCapabilities(self, request:HttpRequest) -> HttpBrowserCapabilities:
        """ GetBrowserCapabilities(self: HttpCapabilitiesProvider, request: HttpRequest) -> HttpBrowserCapabilities """
        ...


class HttpCapabilitiesDefaultProvider(HttpCapabilitiesProvider): # skipped bases: <type 'object'>
    """
    HttpCapabilitiesDefaultProvider()
    HttpCapabilitiesDefaultProvider(parent: HttpCapabilitiesDefaultProvider)
    """
    @property
    def CacheTime(self) -> TimeSpan:
        """
        Get: CacheTime(self: HttpCapabilitiesDefaultProvider) -> TimeSpan
        Set: CacheTime(self: HttpCapabilitiesDefaultProvider) = value
        """
        ...

    @property
    def ResultType(self) -> Type:
        """
        Get: ResultType(self: HttpCapabilitiesDefaultProvider) -> Type
        Set: ResultType(self: HttpCapabilitiesDefaultProvider) = value
        """
        ...

    @property
    def UserAgentCacheKeyLength(self) -> int:
        """
        Get: UserAgentCacheKeyLength(self: HttpCapabilitiesDefaultProvider) -> int
        Set: UserAgentCacheKeyLength(self: HttpCapabilitiesDefaultProvider) = value
        """
        ...


    def AddDependency(self, variable:str): # -> 
        """ AddDependency(self: HttpCapabilitiesDefaultProvider, variable: str) """
        ...

    def AddRuleList(self, ruleList:ArrayList): # -> 
        """ AddRuleList(self: HttpCapabilitiesDefaultProvider, ruleList: ArrayList) """
        ...

    def __new__(cls, parent:HttpCapabilitiesDefaultProvider = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: HttpCapabilitiesDefaultProvider)
        """
        ...


class HttpCapabilitiesSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ HttpCapabilitiesSectionHandler() """
    pass

class HttpConfigurationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: HttpConfigurationContext) -> str """
        ...



class HttpCookiesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HttpCookiesSection() """
    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: HttpCookiesSection) -> str
        Set: Domain(self: HttpCookiesSection) = value
        """
        ...

    @property
    def HttpOnlyCookies(self) -> bool:
        """
        Get: HttpOnlyCookies(self: HttpCookiesSection) -> bool
        Set: HttpOnlyCookies(self: HttpCookiesSection) = value
        """
        ...

    @property
    def RequireSSL(self) -> bool:
        """
        Get: RequireSSL(self: HttpCookiesSection) -> bool
        Set: RequireSSL(self: HttpCookiesSection) = value
        """
        ...

    @property
    def SameSite(self) -> SameSiteMode:
        """
        Get: SameSite(self: HttpCookiesSection) -> SameSiteMode
        Set: SameSite(self: HttpCookiesSection) = value
        """
        ...



class HttpHandlerAction(ConfigurationElement): # skipped bases: <type 'object'>
    """
    HttpHandlerAction(path: str, type: str, verb: str)
    HttpHandlerAction(path: str, type: str, verb: str, validate: bool)
    """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: HttpHandlerAction) -> str
        Set: Path(self: HttpHandlerAction) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: HttpHandlerAction) -> str
        Set: Type(self: HttpHandlerAction) = value
        """
        ...

    @property
    def Validate(self) -> bool:
        """
        Get: Validate(self: HttpHandlerAction) -> bool
        Set: Validate(self: HttpHandlerAction) = value
        """
        ...

    @property
    def Verb(self) -> str:
        """
        Get: Verb(self: HttpHandlerAction) -> str
        Set: Verb(self: HttpHandlerAction) = value
        """
        ...


    def __new__(cls, path:str, type:str, verb:str, validate:bool = ...) -> Self:
        """
        __new__(cls: type, path: str, type: str, verb: str)
        __new__(cls: type, path: str, type: str, verb: str, validate: bool)
        """
        ...


class HttpHandlerActionCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ HttpHandlerActionCollection() """
    def Add(self, httpHandlerAction:HttpHandlerAction): # -> 
        """ Add(self: HttpHandlerActionCollection, httpHandlerAction: HttpHandlerAction) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpHandlerActionCollection) """
        ...

    def IndexOf(self, action:HttpHandlerAction) -> int:
        """ IndexOf(self: HttpHandlerActionCollection, action: HttpHandlerAction) -> int """
        ...

    def Remove(self, *__args:HttpHandlerAction): # -> 
        """ Remove(self: HttpHandlerActionCollection, action: HttpHandlerAction)Remove(self: HttpHandlerActionCollection, verb: str, path: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpHandlerActionCollection, index: int) """
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


class HttpHandlersSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HttpHandlersSection() """
    @property
    def Handlers(self) -> HttpHandlerActionCollection:
        """ Get: Handlers(self: HttpHandlersSection) -> HttpHandlerActionCollection """
        ...



class HttpModuleAction(ConfigurationElement): # skipped bases: <type 'object'>
    """ HttpModuleAction(name: str, type: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: HttpModuleAction) -> str
        Set: Name(self: HttpModuleAction) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: HttpModuleAction) -> str
        Set: Type(self: HttpModuleAction) = value
        """
        ...


    def __new__(cls, name:str, type:str) -> Self:
        """ __new__(cls: type, name: str, type: str) """
        ...


class HttpModuleActionCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ HttpModuleActionCollection() """
    def Add(self, httpModule:HttpModuleAction): # -> 
        """ Add(self: HttpModuleActionCollection, httpModule: HttpModuleAction) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpModuleActionCollection) """
        ...

    def IndexOf(self, action:HttpModuleAction) -> int:
        """ IndexOf(self: HttpModuleActionCollection, action: HttpModuleAction) -> int """
        ...

    def Remove(self, *__args:HttpModuleAction): # -> 
        """ Remove(self: HttpModuleActionCollection, action: HttpModuleAction)Remove(self: HttpModuleActionCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpModuleActionCollection, index: int) """
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


class HttpModulesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HttpModulesSection() """
    @property
    def Modules(self) -> HttpModuleActionCollection:
        """ Get: Modules(self: HttpModulesSection) -> HttpModuleActionCollection """
        ...



class HttpRuntimeSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ HttpRuntimeSection() """
    @property
    def AllowDynamicModuleRegistration(self) -> bool:
        """
        Get: AllowDynamicModuleRegistration(self: HttpRuntimeSection) -> bool
        Set: AllowDynamicModuleRegistration(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def ApartmentThreading(self) -> bool:
        """
        Get: ApartmentThreading(self: HttpRuntimeSection) -> bool
        Set: ApartmentThreading(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def AppRequestQueueLimit(self) -> int:
        """
        Get: AppRequestQueueLimit(self: HttpRuntimeSection) -> int
        Set: AppRequestQueueLimit(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def AsyncPreloadMode(self) -> AsyncPreloadModeFlags:
        """
        Get: AsyncPreloadMode(self: HttpRuntimeSection) -> AsyncPreloadModeFlags
        Set: AsyncPreloadMode(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def DefaultRegexMatchTimeout(self) -> TimeSpan:
        """
        Get: DefaultRegexMatchTimeout(self: HttpRuntimeSection) -> TimeSpan
        Set: DefaultRegexMatchTimeout(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def DelayNotificationTimeout(self) -> TimeSpan:
        """
        Get: DelayNotificationTimeout(self: HttpRuntimeSection) -> TimeSpan
        Set: DelayNotificationTimeout(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def Enable(self) -> bool:
        """
        Get: Enable(self: HttpRuntimeSection) -> bool
        Set: Enable(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def EnableHeaderChecking(self) -> bool:
        """
        Get: EnableHeaderChecking(self: HttpRuntimeSection) -> bool
        Set: EnableHeaderChecking(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def EnableKernelOutputCache(self) -> bool:
        """
        Get: EnableKernelOutputCache(self: HttpRuntimeSection) -> bool
        Set: EnableKernelOutputCache(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def EnableVersionHeader(self) -> bool:
        """
        Get: EnableVersionHeader(self: HttpRuntimeSection) -> bool
        Set: EnableVersionHeader(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def EncoderType(self) -> str:
        """
        Get: EncoderType(self: HttpRuntimeSection) -> str
        Set: EncoderType(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def ExecutionTimeout(self) -> TimeSpan:
        """
        Get: ExecutionTimeout(self: HttpRuntimeSection) -> TimeSpan
        Set: ExecutionTimeout(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def FcnMode(self) -> FcnMode:
        """
        Get: FcnMode(self: HttpRuntimeSection) -> FcnMode
        Set: FcnMode(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MaxQueryStringLength(self) -> int:
        """
        Get: MaxQueryStringLength(self: HttpRuntimeSection) -> int
        Set: MaxQueryStringLength(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MaxRequestLength(self) -> int:
        """
        Get: MaxRequestLength(self: HttpRuntimeSection) -> int
        Set: MaxRequestLength(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MaxUrlLength(self) -> int:
        """
        Get: MaxUrlLength(self: HttpRuntimeSection) -> int
        Set: MaxUrlLength(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MaxWaitChangeNotification(self) -> int:
        """
        Get: MaxWaitChangeNotification(self: HttpRuntimeSection) -> int
        Set: MaxWaitChangeNotification(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MinFreeThreads(self) -> int:
        """
        Get: MinFreeThreads(self: HttpRuntimeSection) -> int
        Set: MinFreeThreads(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def MinLocalRequestFreeThreads(self) -> int:
        """
        Get: MinLocalRequestFreeThreads(self: HttpRuntimeSection) -> int
        Set: MinLocalRequestFreeThreads(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RelaxedUrlToFileSystemMapping(self) -> bool:
        """
        Get: RelaxedUrlToFileSystemMapping(self: HttpRuntimeSection) -> bool
        Set: RelaxedUrlToFileSystemMapping(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RequestLengthDiskThreshold(self) -> int:
        """
        Get: RequestLengthDiskThreshold(self: HttpRuntimeSection) -> int
        Set: RequestLengthDiskThreshold(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RequestPathInvalidCharacters(self) -> str:
        """
        Get: RequestPathInvalidCharacters(self: HttpRuntimeSection) -> str
        Set: RequestPathInvalidCharacters(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RequestValidationMode(self) -> Version:
        """
        Get: RequestValidationMode(self: HttpRuntimeSection) -> Version
        Set: RequestValidationMode(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RequestValidationType(self) -> str:
        """
        Get: RequestValidationType(self: HttpRuntimeSection) -> str
        Set: RequestValidationType(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def RequireRootedSaveAsPath(self) -> bool:
        """
        Get: RequireRootedSaveAsPath(self: HttpRuntimeSection) -> bool
        Set: RequireRootedSaveAsPath(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def SendCacheControlHeader(self) -> bool:
        """
        Get: SendCacheControlHeader(self: HttpRuntimeSection) -> bool
        Set: SendCacheControlHeader(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def ShutdownTimeout(self) -> TimeSpan:
        """
        Get: ShutdownTimeout(self: HttpRuntimeSection) -> TimeSpan
        Set: ShutdownTimeout(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def TargetFramework(self) -> str:
        """
        Get: TargetFramework(self: HttpRuntimeSection) -> str
        Set: TargetFramework(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def UseFullyQualifiedRedirectUrl(self) -> bool:
        """
        Get: UseFullyQualifiedRedirectUrl(self: HttpRuntimeSection) -> bool
        Set: UseFullyQualifiedRedirectUrl(self: HttpRuntimeSection) = value
        """
        ...

    @property
    def WaitChangeNotification(self) -> int:
        """
        Get: WaitChangeNotification(self: HttpRuntimeSection) -> int
        Set: WaitChangeNotification(self: HttpRuntimeSection) = value
        """
        ...



class IConfigMapPath: # skipped bases: <type 'object'>
    """ no doc """
    def GetAppPathForPath(self, siteID:str, path:str) -> str:
        """ GetAppPathForPath(self: IConfigMapPath, siteID: str, path: str) -> str """
        ...

    def GetDefaultSiteNameAndID(self, siteName, siteID) -> Tuple_[str, str]:
        """ GetDefaultSiteNameAndID(self: IConfigMapPath) -> (str, str) """
        ...

    def GetMachineConfigFilename(self) -> str:
        """ GetMachineConfigFilename(self: IConfigMapPath) -> str """
        ...

    def GetPathConfigFilename(self, siteID, path, directory, baseName) -> Tuple_[str, str]:
        """ GetPathConfigFilename(self: IConfigMapPath, siteID: str, path: str) -> (str, str) """
        ...

    def GetRootWebConfigFilename(self) -> str:
        """ GetRootWebConfigFilename(self: IConfigMapPath) -> str """
        ...

    def MapPath(self, siteID:str, path:str) -> str:
        """ MapPath(self: IConfigMapPath, siteID: str, path: str) -> str """
        ...

    def ResolveSiteArgument(self, siteArgument, siteName, siteID) -> Tuple_[str, str]:
        """ ResolveSiteArgument(self: IConfigMapPath, siteArgument: str) -> (str, str) """
        ...


class IConfigMapPathFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, virtualPath:str, physicalPath:str) -> IConfigMapPath:
        """ Create(self: IConfigMapPathFactory, virtualPath: str, physicalPath: str) -> IConfigMapPath """
        ...


class IdentitySection(ConfigurationSection): # skipped bases: <type 'object'>
    """ IdentitySection() """
    @property
    def Impersonate(self) -> bool:
        """
        Get: Impersonate(self: IdentitySection) -> bool
        Set: Impersonate(self: IdentitySection) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: IdentitySection) -> str
        Set: Password(self: IdentitySection) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: IdentitySection) -> str
        Set: UserName(self: IdentitySection) = value
        """
        ...



class IgnoreDeviceFilterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IgnoreDeviceFilterElement(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IgnoreDeviceFilterElement) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class IgnoreDeviceFilterElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ IgnoreDeviceFilterElementCollection() """
    def Add(self, deviceFilter:IgnoreDeviceFilterElement): # -> 
        """ Add(self: IgnoreDeviceFilterElementCollection, deviceFilter: IgnoreDeviceFilterElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IgnoreDeviceFilterElementCollection) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: IgnoreDeviceFilterElementCollection, name: str)Remove(self: IgnoreDeviceFilterElementCollection, deviceFilter: IgnoreDeviceFilterElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IgnoreDeviceFilterElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IRemoteWebConfigurationHostServer: # skipped bases: <type 'object'>
    """ no doc """
    def DoEncryptOrDecrypt(self, doEncrypt:bool, xmlString:str, protectionProviderName:str, protectionProviderType:str, parameterKeys:Array, parameterValues:Array) -> str:
        """ DoEncryptOrDecrypt(self: IRemoteWebConfigurationHostServer, doEncrypt: bool, xmlString: str, protectionProviderName: str, protectionProviderType: str, parameterKeys: Array[str], parameterValues: Array[str]) -> str """
        ...

    def GetData(self, fileName, getReadTimeOnly, readTime) -> Tuple_[Array, Int64]:
        """ GetData(self: IRemoteWebConfigurationHostServer, fileName: str, getReadTimeOnly: bool) -> (Array[Byte], Int64) """
        ...

    def GetFileDetails(self, name, exists, size, createDate, lastWriteDate) -> Tuple_[bool, Int64, Int64, Int64]:
        """ GetFileDetails(self: IRemoteWebConfigurationHostServer, name: str) -> (bool, Int64, Int64, Int64) """
        ...

    def GetFilePaths(self, webLevel:int, path:str, site:str, locationSubPath:str) -> str:
        """ GetFilePaths(self: IRemoteWebConfigurationHostServer, webLevel: int, path: str, site: str, locationSubPath: str) -> str """
        ...

    def WriteData(self, fileName:str, templateFileName:str, data:Array, readTime:Int64) -> Int64:
        """ WriteData(self: IRemoteWebConfigurationHostServer, fileName: str, templateFileName: str, data: Array[Byte], readTime: Int64) -> Int64 """
        ...


class LowerCaseStringConverter(TypeConverter): # skipped bases: <type 'object'>
    """ LowerCaseStringConverter() """
    pass

class MachineKeyCompatibilityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MachineKeyCompatibilityMode, values: Framework20SP1 (0), Framework20SP2 (1), Framework45 (2) """
    Framework20SP1: MachineKeyCompatibilityMode = ...
    Framework20SP2: MachineKeyCompatibilityMode = ...
    Framework45: MachineKeyCompatibilityMode = ...
    value__ = ...


class MachineKeySection(ConfigurationSection): # skipped bases: <type 'object'>
    """ MachineKeySection() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: MachineKeySection) -> str
        Set: ApplicationName(self: MachineKeySection) = value
        """
        ...

    @property
    def CompatibilityMode(self) -> MachineKeyCompatibilityMode:
        """
        Get: CompatibilityMode(self: MachineKeySection) -> MachineKeyCompatibilityMode
        Set: CompatibilityMode(self: MachineKeySection) = value
        """
        ...

    @property
    def DataProtectorType(self) -> str:
        """
        Get: DataProtectorType(self: MachineKeySection) -> str
        Set: DataProtectorType(self: MachineKeySection) = value
        """
        ...

    @property
    def Decryption(self) -> str:
        """
        Get: Decryption(self: MachineKeySection) -> str
        Set: Decryption(self: MachineKeySection) = value
        """
        ...

    @property
    def DecryptionKey(self) -> str:
        """
        Get: DecryptionKey(self: MachineKeySection) -> str
        Set: DecryptionKey(self: MachineKeySection) = value
        """
        ...

    @property
    def Validation(self): # -> MachineKeyValidation
        """
        Get: Validation(self: MachineKeySection) -> MachineKeyValidation
        Set: Validation(self: MachineKeySection) = value
        """
        ...

    @property
    def ValidationAlgorithm(self) -> str:
        """
        Get: ValidationAlgorithm(self: MachineKeySection) -> str
        Set: ValidationAlgorithm(self: MachineKeySection) = value
        """
        ...

    @property
    def ValidationKey(self) -> str:
        """
        Get: ValidationKey(self: MachineKeySection) -> str
        Set: ValidationKey(self: MachineKeySection) = value
        """
        ...



class MachineKeyValidation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MachineKeyValidation, values: AES (3), Custom (7), HMACSHA256 (4), HMACSHA384 (5), HMACSHA512 (6), MD5 (0), SHA1 (1), TripleDES (2) """
    AES: MachineKeyValidation = ...
    Custom: MachineKeyValidation = ...
    HMACSHA256: MachineKeyValidation = ...
    HMACSHA384: MachineKeyValidation = ...
    HMACSHA512: MachineKeyValidation = ...
    MD5: MachineKeyValidation = ...
    SHA1: MachineKeyValidation = ...
    TripleDES: MachineKeyValidation = ...
    value__ = ...


class MachineKeyValidationConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ MachineKeyValidationConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: MachineKeyValidationConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: MachineKeyValidationConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class MembershipPasswordCompatibilityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MembershipPasswordCompatibilityMode, values: Framework20 (0), Framework40 (1) """
    Framework20: MembershipPasswordCompatibilityMode = ...
    Framework40: MembershipPasswordCompatibilityMode = ...
    value__ = ...


class MembershipSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ MembershipSection() """
    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: MembershipSection) -> str
        Set: DefaultProvider(self: MembershipSection) = value
        """
        ...

    @property
    def HashAlgorithmType(self) -> str:
        """
        Get: HashAlgorithmType(self: MembershipSection) -> str
        Set: HashAlgorithmType(self: MembershipSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: MembershipSection) -> ProviderSettingsCollection """
        ...

    @property
    def UserIsOnlineTimeWindow(self) -> TimeSpan:
        """
        Get: UserIsOnlineTimeWindow(self: MembershipSection) -> TimeSpan
        Set: UserIsOnlineTimeWindow(self: MembershipSection) = value
        """
        ...



class NamespaceCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ NamespaceCollection() """
    @property
    def AutoImportVBNamespace(self) -> bool:
        """
        Get: AutoImportVBNamespace(self: NamespaceCollection) -> bool
        Set: AutoImportVBNamespace(self: NamespaceCollection) = value
        """
        ...


    def Add(self, namespaceInformation): # ->  # Not found arg types: {'namespaceInformation': 'NamespaceInfo'}
        """ Add(self: NamespaceCollection, namespaceInformation: NamespaceInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: NamespaceCollection) """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: NamespaceCollection, s: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: NamespaceCollection, index: int) """
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


class NamespaceInfo(ConfigurationElement): # skipped bases: <type 'object'>
    """ NamespaceInfo(name: str) """
    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: NamespaceInfo) -> str
        Set: Namespace(self: NamespaceInfo) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class OutputCacheProfile(ConfigurationElement): # skipped bases: <type 'object'>
    """ OutputCacheProfile(name: str) """
    @property
    def Duration(self) -> int:
        """
        Get: Duration(self: OutputCacheProfile) -> int
        Set: Duration(self: OutputCacheProfile) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: OutputCacheProfile) -> bool
        Set: Enabled(self: OutputCacheProfile) = value
        """
        ...

    @property
    def Location(self) -> OutputCacheLocation:
        """
        Get: Location(self: OutputCacheProfile) -> OutputCacheLocation
        Set: Location(self: OutputCacheProfile) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OutputCacheProfile) -> str
        Set: Name(self: OutputCacheProfile) = value
        """
        ...

    @property
    def NoStore(self) -> bool:
        """
        Get: NoStore(self: OutputCacheProfile) -> bool
        Set: NoStore(self: OutputCacheProfile) = value
        """
        ...

    @property
    def SqlDependency(self) -> str:
        """
        Get: SqlDependency(self: OutputCacheProfile) -> str
        Set: SqlDependency(self: OutputCacheProfile) = value
        """
        ...

    @property
    def VaryByContentEncoding(self) -> str:
        """
        Get: VaryByContentEncoding(self: OutputCacheProfile) -> str
        Set: VaryByContentEncoding(self: OutputCacheProfile) = value
        """
        ...

    @property
    def VaryByControl(self) -> str:
        """
        Get: VaryByControl(self: OutputCacheProfile) -> str
        Set: VaryByControl(self: OutputCacheProfile) = value
        """
        ...

    @property
    def VaryByCustom(self) -> str:
        """
        Get: VaryByCustom(self: OutputCacheProfile) -> str
        Set: VaryByCustom(self: OutputCacheProfile) = value
        """
        ...

    @property
    def VaryByHeader(self) -> str:
        """
        Get: VaryByHeader(self: OutputCacheProfile) -> str
        Set: VaryByHeader(self: OutputCacheProfile) = value
        """
        ...

    @property
    def VaryByParam(self) -> str:
        """
        Get: VaryByParam(self: OutputCacheProfile) -> str
        Set: VaryByParam(self: OutputCacheProfile) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class OutputCacheProfileCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ OutputCacheProfileCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: OutputCacheProfileCollection) -> Array[str] """
        ...


    def Add(self, name:OutputCacheProfile): # -> 
        """ Add(self: OutputCacheProfileCollection, name: OutputCacheProfile) """
        ...

    def Clear(self): # -> 
        """ Clear(self: OutputCacheProfileCollection) """
        ...

    def Get(self, *__args:int) -> OutputCacheProfile:
        """
        Get(self: OutputCacheProfileCollection, index: int) -> OutputCacheProfile
        Get(self: OutputCacheProfileCollection, name: str) -> OutputCacheProfile
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: OutputCacheProfileCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: OutputCacheProfileCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: OutputCacheProfileCollection, index: int) """
        ...

    def Set(self, user:OutputCacheProfile): # -> 
        """ Set(self: OutputCacheProfileCollection, user: OutputCacheProfile) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class OutputCacheSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ OutputCacheSection() """
    @property
    def DefaultProviderName(self) -> str:
        """
        Get: DefaultProviderName(self: OutputCacheSection) -> str
        Set: DefaultProviderName(self: OutputCacheSection) = value
        """
        ...

    @property
    def EnableFragmentCache(self) -> bool:
        """
        Get: EnableFragmentCache(self: OutputCacheSection) -> bool
        Set: EnableFragmentCache(self: OutputCacheSection) = value
        """
        ...

    @property
    def EnableKernelCacheForVaryByStar(self) -> bool:
        """
        Get: EnableKernelCacheForVaryByStar(self: OutputCacheSection) -> bool
        Set: EnableKernelCacheForVaryByStar(self: OutputCacheSection) = value
        """
        ...

    @property
    def EnableOutputCache(self) -> bool:
        """
        Get: EnableOutputCache(self: OutputCacheSection) -> bool
        Set: EnableOutputCache(self: OutputCacheSection) = value
        """
        ...

    @property
    def OmitVaryStar(self) -> bool:
        """
        Get: OmitVaryStar(self: OutputCacheSection) -> bool
        Set: OmitVaryStar(self: OutputCacheSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: OutputCacheSection) -> ProviderSettingsCollection """
        ...

    @property
    def SendCacheControlHeader(self) -> bool:
        """
        Get: SendCacheControlHeader(self: OutputCacheSection) -> bool
        Set: SendCacheControlHeader(self: OutputCacheSection) = value
        """
        ...



class OutputCacheSettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ OutputCacheSettingsSection() """
    @property
    def OutputCacheProfiles(self) -> OutputCacheProfileCollection:
        """ Get: OutputCacheProfiles(self: OutputCacheSettingsSection) -> OutputCacheProfileCollection """
        ...



class PagesEnableSessionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PagesEnableSessionState, values: False (0), ReadOnly (1), True (2) """
    ReadOnly: PagesEnableSessionState = ...
    value__ = ...


class PagesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ PagesSection() """
    @property
    def AsyncTimeout(self) -> TimeSpan:
        """
        Get: AsyncTimeout(self: PagesSection) -> TimeSpan
        Set: AsyncTimeout(self: PagesSection) = value
        """
        ...

    @property
    def AutoEventWireup(self) -> bool:
        """
        Get: AutoEventWireup(self: PagesSection) -> bool
        Set: AutoEventWireup(self: PagesSection) = value
        """
        ...

    @property
    def Buffer(self) -> bool:
        """
        Get: Buffer(self: PagesSection) -> bool
        Set: Buffer(self: PagesSection) = value
        """
        ...

    @property
    def ClientIDMode(self) -> ClientIDMode:
        """
        Get: ClientIDMode(self: PagesSection) -> ClientIDMode
        Set: ClientIDMode(self: PagesSection) = value
        """
        ...

    @property
    def CompilationMode(self) -> CompilationMode:
        """
        Get: CompilationMode(self: PagesSection) -> CompilationMode
        Set: CompilationMode(self: PagesSection) = value
        """
        ...

    @property
    def ControlRenderingCompatibilityVersion(self) -> Version:
        """
        Get: ControlRenderingCompatibilityVersion(self: PagesSection) -> Version
        Set: ControlRenderingCompatibilityVersion(self: PagesSection) = value
        """
        ...

    @property
    def Controls(self): # -> TagPrefixCollection
        """ Get: Controls(self: PagesSection) -> TagPrefixCollection """
        ...

    @property
    def EnableEventValidation(self) -> bool:
        """
        Get: EnableEventValidation(self: PagesSection) -> bool
        Set: EnableEventValidation(self: PagesSection) = value
        """
        ...

    @property
    def EnableSessionState(self) -> PagesEnableSessionState:
        """
        Get: EnableSessionState(self: PagesSection) -> PagesEnableSessionState
        Set: EnableSessionState(self: PagesSection) = value
        """
        ...

    @property
    def EnableViewState(self) -> bool:
        """
        Get: EnableViewState(self: PagesSection) -> bool
        Set: EnableViewState(self: PagesSection) = value
        """
        ...

    @property
    def EnableViewStateMac(self) -> bool:
        """
        Get: EnableViewStateMac(self: PagesSection) -> bool
        Set: EnableViewStateMac(self: PagesSection) = value
        """
        ...

    @property
    def IgnoreDeviceFilters(self) -> IgnoreDeviceFilterElementCollection:
        """ Get: IgnoreDeviceFilters(self: PagesSection) -> IgnoreDeviceFilterElementCollection """
        ...

    @property
    def MaintainScrollPositionOnPostBack(self) -> bool:
        """
        Get: MaintainScrollPositionOnPostBack(self: PagesSection) -> bool
        Set: MaintainScrollPositionOnPostBack(self: PagesSection) = value
        """
        ...

    @property
    def MasterPageFile(self) -> str:
        """
        Get: MasterPageFile(self: PagesSection) -> str
        Set: MasterPageFile(self: PagesSection) = value
        """
        ...

    @property
    def MaxPageStateFieldLength(self) -> int:
        """
        Get: MaxPageStateFieldLength(self: PagesSection) -> int
        Set: MaxPageStateFieldLength(self: PagesSection) = value
        """
        ...

    @property
    def Namespaces(self) -> NamespaceCollection:
        """ Get: Namespaces(self: PagesSection) -> NamespaceCollection """
        ...

    @property
    def PageBaseType(self) -> str:
        """
        Get: PageBaseType(self: PagesSection) -> str
        Set: PageBaseType(self: PagesSection) = value
        """
        ...

    @property
    def PageParserFilterType(self) -> str:
        """
        Get: PageParserFilterType(self: PagesSection) -> str
        Set: PageParserFilterType(self: PagesSection) = value
        """
        ...

    @property
    def RenderAllHiddenFieldsAtTopOfForm(self) -> bool:
        """
        Get: RenderAllHiddenFieldsAtTopOfForm(self: PagesSection) -> bool
        Set: RenderAllHiddenFieldsAtTopOfForm(self: PagesSection) = value
        """
        ...

    @property
    def SmartNavigation(self) -> bool:
        """
        Get: SmartNavigation(self: PagesSection) -> bool
        Set: SmartNavigation(self: PagesSection) = value
        """
        ...

    @property
    def StyleSheetTheme(self) -> str:
        """
        Get: StyleSheetTheme(self: PagesSection) -> str
        Set: StyleSheetTheme(self: PagesSection) = value
        """
        ...

    @property
    def TagMapping(self): # -> TagMapCollection
        """ Get: TagMapping(self: PagesSection) -> TagMapCollection """
        ...

    @property
    def Theme(self) -> str:
        """
        Get: Theme(self: PagesSection) -> str
        Set: Theme(self: PagesSection) = value
        """
        ...

    @property
    def UserControlBaseType(self) -> str:
        """
        Get: UserControlBaseType(self: PagesSection) -> str
        Set: UserControlBaseType(self: PagesSection) = value
        """
        ...

    @property
    def ValidateRequest(self) -> bool:
        """
        Get: ValidateRequest(self: PagesSection) -> bool
        Set: ValidateRequest(self: PagesSection) = value
        """
        ...

    @property
    def ViewStateEncryptionMode(self) -> ViewStateEncryptionMode:
        """
        Get: ViewStateEncryptionMode(self: PagesSection) -> ViewStateEncryptionMode
        Set: ViewStateEncryptionMode(self: PagesSection) = value
        """
        ...



class PartialTrustVisibleAssembliesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ PartialTrustVisibleAssembliesSection() """
    @property
    def PartialTrustVisibleAssemblies(self): # -> PartialTrustVisibleAssemblyCollection
        """ Get: PartialTrustVisibleAssemblies(self: PartialTrustVisibleAssembliesSection) -> PartialTrustVisibleAssemblyCollection """
        ...



class PartialTrustVisibleAssembly(ConfigurationElement): # skipped bases: <type 'object'>
    """ PartialTrustVisibleAssembly(assemblyName: str, publicKey: str) """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: PartialTrustVisibleAssembly) -> str
        Set: AssemblyName(self: PartialTrustVisibleAssembly) = value
        """
        ...

    @property
    def PublicKey(self) -> str:
        """
        Get: PublicKey(self: PartialTrustVisibleAssembly) -> str
        Set: PublicKey(self: PartialTrustVisibleAssembly) = value
        """
        ...


    def __new__(cls, assemblyName:str, publicKey:str) -> Self:
        """ __new__(cls: type, assemblyName: str, publicKey: str) """
        ...


class PartialTrustVisibleAssemblyCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ PartialTrustVisibleAssemblyCollection() """
    def Add(self, partialTrustVisibleAssembly:PartialTrustVisibleAssembly): # -> 
        """ Add(self: PartialTrustVisibleAssemblyCollection, partialTrustVisibleAssembly: PartialTrustVisibleAssembly) """
        ...

    def Clear(self): # -> 
        """ Clear(self: PartialTrustVisibleAssemblyCollection) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: PartialTrustVisibleAssemblyCollection, key: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: PartialTrustVisibleAssemblyCollection, index: int) """
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


class PassportAuthentication(ConfigurationElement): # skipped bases: <type 'object'>
    """ PassportAuthentication() """
    @property
    def RedirectUrl(self) -> str:
        """
        Get: RedirectUrl(self: PassportAuthentication) -> str
        Set: RedirectUrl(self: PassportAuthentication) = value
        """
        ...



class ProcessModelComAuthenticationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
    def Call(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def Connect(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def Default(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def None(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def Pkt(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def PktIntegrity(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def PktPrivacy(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    def __call__(self, *args): #cannot find CLR method
        """ enum ProcessModelComAuthenticationLevel, values: Call (1), Connect (2), Default (3), None (0), Pkt (4), PktIntegrity (5), PktPrivacy (6) """
        ...

    value__ = ...


class ProcessModelComImpersonationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessModelComImpersonationLevel, values: Anonymous (1), Default (0), Delegate (2), Identify (3), Impersonate (4) """
    Anonymous: ProcessModelComImpersonationLevel = ...
    Default: ProcessModelComImpersonationLevel = ...
    Delegate: ProcessModelComImpersonationLevel = ...
    Identify: ProcessModelComImpersonationLevel = ...
    Impersonate: ProcessModelComImpersonationLevel = ...
    value__ = ...


class ProcessModelLogLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessModelLogLevel, values: All (1), Errors (2), None (0) """
    All: ProcessModelLogLevel = ...
    Errors: ProcessModelLogLevel = ...
    value__ = ...


class ProcessModelSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ProcessModelSection() """
    @property
    def AutoConfig(self) -> bool:
        """
        Get: AutoConfig(self: ProcessModelSection) -> bool
        Set: AutoConfig(self: ProcessModelSection) = value
        """
        ...

    @property
    def ClientConnectedCheck(self) -> TimeSpan:
        """
        Get: ClientConnectedCheck(self: ProcessModelSection) -> TimeSpan
        Set: ClientConnectedCheck(self: ProcessModelSection) = value
        """
        ...

    @property
    def ComAuthenticationLevel(self) -> ProcessModelComAuthenticationLevel:
        """
        Get: ComAuthenticationLevel(self: ProcessModelSection) -> ProcessModelComAuthenticationLevel
        Set: ComAuthenticationLevel(self: ProcessModelSection) = value
        """
        ...

    @property
    def ComImpersonationLevel(self) -> ProcessModelComImpersonationLevel:
        """
        Get: ComImpersonationLevel(self: ProcessModelSection) -> ProcessModelComImpersonationLevel
        Set: ComImpersonationLevel(self: ProcessModelSection) = value
        """
        ...

    @property
    def CpuMask(self) -> int:
        """
        Get: CpuMask(self: ProcessModelSection) -> int
        Set: CpuMask(self: ProcessModelSection) = value
        """
        ...

    @property
    def Enable(self) -> bool:
        """
        Get: Enable(self: ProcessModelSection) -> bool
        Set: Enable(self: ProcessModelSection) = value
        """
        ...

    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: ProcessModelSection) -> TimeSpan
        Set: IdleTimeout(self: ProcessModelSection) = value
        """
        ...

    @property
    def LogLevel(self) -> ProcessModelLogLevel:
        """
        Get: LogLevel(self: ProcessModelSection) -> ProcessModelLogLevel
        Set: LogLevel(self: ProcessModelSection) = value
        """
        ...

    @property
    def MaxAppDomains(self) -> int:
        """
        Get: MaxAppDomains(self: ProcessModelSection) -> int
        Set: MaxAppDomains(self: ProcessModelSection) = value
        """
        ...

    @property
    def MaxIOThreads(self) -> int:
        """
        Get: MaxIOThreads(self: ProcessModelSection) -> int
        Set: MaxIOThreads(self: ProcessModelSection) = value
        """
        ...

    @property
    def MaxWorkerThreads(self) -> int:
        """
        Get: MaxWorkerThreads(self: ProcessModelSection) -> int
        Set: MaxWorkerThreads(self: ProcessModelSection) = value
        """
        ...

    @property
    def MemoryLimit(self) -> int:
        """
        Get: MemoryLimit(self: ProcessModelSection) -> int
        Set: MemoryLimit(self: ProcessModelSection) = value
        """
        ...

    @property
    def MinIOThreads(self) -> int:
        """
        Get: MinIOThreads(self: ProcessModelSection) -> int
        Set: MinIOThreads(self: ProcessModelSection) = value
        """
        ...

    @property
    def MinWorkerThreads(self) -> int:
        """
        Get: MinWorkerThreads(self: ProcessModelSection) -> int
        Set: MinWorkerThreads(self: ProcessModelSection) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: ProcessModelSection) -> str
        Set: Password(self: ProcessModelSection) = value
        """
        ...

    @property
    def PingFrequency(self) -> TimeSpan:
        """
        Get: PingFrequency(self: ProcessModelSection) -> TimeSpan
        Set: PingFrequency(self: ProcessModelSection) = value
        """
        ...

    @property
    def PingTimeout(self) -> TimeSpan:
        """
        Get: PingTimeout(self: ProcessModelSection) -> TimeSpan
        Set: PingTimeout(self: ProcessModelSection) = value
        """
        ...

    @property
    def RequestLimit(self) -> int:
        """
        Get: RequestLimit(self: ProcessModelSection) -> int
        Set: RequestLimit(self: ProcessModelSection) = value
        """
        ...

    @property
    def RequestQueueLimit(self) -> int:
        """
        Get: RequestQueueLimit(self: ProcessModelSection) -> int
        Set: RequestQueueLimit(self: ProcessModelSection) = value
        """
        ...

    @property
    def ResponseDeadlockInterval(self) -> TimeSpan:
        """
        Get: ResponseDeadlockInterval(self: ProcessModelSection) -> TimeSpan
        Set: ResponseDeadlockInterval(self: ProcessModelSection) = value
        """
        ...

    @property
    def ResponseRestartDeadlockInterval(self) -> TimeSpan:
        """
        Get: ResponseRestartDeadlockInterval(self: ProcessModelSection) -> TimeSpan
        Set: ResponseRestartDeadlockInterval(self: ProcessModelSection) = value
        """
        ...

    @property
    def RestartQueueLimit(self) -> int:
        """
        Get: RestartQueueLimit(self: ProcessModelSection) -> int
        Set: RestartQueueLimit(self: ProcessModelSection) = value
        """
        ...

    @property
    def ServerErrorMessageFile(self) -> str:
        """
        Get: ServerErrorMessageFile(self: ProcessModelSection) -> str
        Set: ServerErrorMessageFile(self: ProcessModelSection) = value
        """
        ...

    @property
    def ShutdownTimeout(self) -> TimeSpan:
        """
        Get: ShutdownTimeout(self: ProcessModelSection) -> TimeSpan
        Set: ShutdownTimeout(self: ProcessModelSection) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: ProcessModelSection) -> TimeSpan
        Set: Timeout(self: ProcessModelSection) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: ProcessModelSection) -> str
        Set: UserName(self: ProcessModelSection) = value
        """
        ...

    @property
    def WebGarden(self) -> bool:
        """
        Get: WebGarden(self: ProcessModelSection) -> bool
        Set: WebGarden(self: ProcessModelSection) = value
        """
        ...



class ProfileGroupSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """ ProfileGroupSettings(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ProfileGroupSettings) -> str """
        ...

    @property
    def PropertySettings(self): # -> ProfilePropertySettingsCollection
        """ Get: PropertySettings(self: ProfileGroupSettings) -> ProfilePropertySettingsCollection """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ProfileGroupSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProfileGroupSettingsCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: ProfileGroupSettingsCollection) -> Array[str] """
        ...


    def Add(self, group:ProfileGroupSettings): # -> 
        """ Add(self: ProfileGroupSettingsCollection, group: ProfileGroupSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProfileGroupSettingsCollection) """
        ...

    def Get(self, *__args:int) -> ProfileGroupSettings:
        """
        Get(self: ProfileGroupSettingsCollection, index: int) -> ProfileGroupSettings
        Get(self: ProfileGroupSettingsCollection, name: str) -> ProfileGroupSettings
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: ProfileGroupSettingsCollection, index: int) -> str """
        ...

    def IndexOf(self, group:ProfileGroupSettings) -> int:
        """ IndexOf(self: ProfileGroupSettingsCollection, group: ProfileGroupSettings) -> int """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProfileGroupSettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ProfileGroupSettingsCollection, index: int) """
        ...

    def Set(self, group:ProfileGroupSettings): # -> 
        """ Set(self: ProfileGroupSettingsCollection, group: ProfileGroupSettings) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProfileGuidedOptimizationsFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ProfileGuidedOptimizationsFlags, values: All (1), None (0) """
    All: ProfileGuidedOptimizationsFlags = ...
    value__ = ...


class ProfilePropertySettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProfilePropertySettings(name: str)
    ProfilePropertySettings(name: str, readOnly: bool, serializeAs: SerializationMode, providerName: str, defaultValue: str, profileType: str, allowAnonymous: bool, customProviderData: str)
    """
    @property
    def AllowAnonymous(self) -> bool:
        """
        Get: AllowAnonymous(self: ProfilePropertySettings) -> bool
        Set: AllowAnonymous(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def CustomProviderData(self) -> str:
        """
        Get: CustomProviderData(self: ProfilePropertySettings) -> str
        Set: CustomProviderData(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: ProfilePropertySettings) -> str
        Set: DefaultValue(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ProfilePropertySettings) -> str
        Set: Name(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: ProfilePropertySettings) -> str
        Set: Provider(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: ProfilePropertySettings) -> bool
        Set: ReadOnly(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def SerializeAs(self): # -> SerializationMode
        """
        Get: SerializeAs(self: ProfilePropertySettings) -> SerializationMode
        Set: SerializeAs(self: ProfilePropertySettings) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ProfilePropertySettings) -> str
        Set: Type(self: ProfilePropertySettings) = value
        """
        ...


    def __new__(cls, name:str, readOnly:bool = ..., serializeAs = ..., providerName:str = ..., defaultValue:str = ..., profileType:str = ..., allowAnonymous:bool = ..., customProviderData:str = ...) -> Self: # Not found arg types: {'serializeAs': 'SerializationMode'}
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, readOnly: bool, serializeAs: SerializationMode, providerName: str, defaultValue: str, profileType: str, allowAnonymous: bool, customProviderData: str)
        """
        ...


class ProfilePropertySettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProfilePropertySettingsCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: ProfilePropertySettingsCollection) -> Array[str] """
        ...

    @property
    def AllowClear(self):
        ...


    def Add(self, propertySettings:ProfilePropertySettings): # -> 
        """ Add(self: ProfilePropertySettingsCollection, propertySettings: ProfilePropertySettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProfilePropertySettingsCollection) """
        ...

    def Get(self, *__args:int) -> ProfilePropertySettings:
        """
        Get(self: ProfilePropertySettingsCollection, index: int) -> ProfilePropertySettings
        Get(self: ProfilePropertySettingsCollection, name: str) -> ProfilePropertySettings
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: ProfilePropertySettingsCollection, index: int) -> str """
        ...

    def IndexOf(self, propertySettings:ProfilePropertySettings) -> int:
        """ IndexOf(self: ProfilePropertySettingsCollection, propertySettings: ProfilePropertySettings) -> int """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProfilePropertySettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ProfilePropertySettingsCollection, index: int) """
        ...

    def Set(self, propertySettings:ProfilePropertySettings): # -> 
        """ Set(self: ProfilePropertySettingsCollection, propertySettings: ProfilePropertySettings) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProfileSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ProfileSection() """
    @property
    def AutomaticSaveEnabled(self) -> bool:
        """
        Get: AutomaticSaveEnabled(self: ProfileSection) -> bool
        Set: AutomaticSaveEnabled(self: ProfileSection) = value
        """
        ...

    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: ProfileSection) -> str
        Set: DefaultProvider(self: ProfileSection) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ProfileSection) -> bool
        Set: Enabled(self: ProfileSection) = value
        """
        ...

    @property
    def Inherits(self) -> str:
        """
        Get: Inherits(self: ProfileSection) -> str
        Set: Inherits(self: ProfileSection) = value
        """
        ...

    @property
    def PropertySettings(self): # -> RootProfilePropertySettingsCollection
        """ Get: PropertySettings(self: ProfileSection) -> RootProfilePropertySettingsCollection """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: ProfileSection) -> ProviderSettingsCollection """
        ...



class ProfileSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProfileSettings(name: str)
    ProfileSettings(name: str, minInstances: int, maxLimit: int, minInterval: TimeSpan)
    ProfileSettings(name: str, minInstances: int, maxLimit: int, minInterval: TimeSpan, custom: str)
    """
    @property
    def Custom(self) -> str:
        """
        Get: Custom(self: ProfileSettings) -> str
        Set: Custom(self: ProfileSettings) = value
        """
        ...

    @property
    def MaxLimit(self) -> int:
        """
        Get: MaxLimit(self: ProfileSettings) -> int
        Set: MaxLimit(self: ProfileSettings) = value
        """
        ...

    @property
    def MinInstances(self) -> int:
        """
        Get: MinInstances(self: ProfileSettings) -> int
        Set: MinInstances(self: ProfileSettings) = value
        """
        ...

    @property
    def MinInterval(self) -> TimeSpan:
        """
        Get: MinInterval(self: ProfileSettings) -> TimeSpan
        Set: MinInterval(self: ProfileSettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ProfileSettings) -> str
        Set: Name(self: ProfileSettings) = value
        """
        ...


    def __new__(cls, name:str, minInstances:int = ..., maxLimit:int = ..., minInterval:TimeSpan = ..., custom:str = ...) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, minInstances: int, maxLimit: int, minInterval: TimeSpan)
        __new__(cls: type, name: str, minInstances: int, maxLimit: int, minInterval: TimeSpan, custom: str)
        """
        ...


class ProfileSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProfileSettingsCollection() """
    def Add(self, profilesSettings:ProfileSettings): # -> 
        """ Add(self: ProfileSettingsCollection, profilesSettings: ProfileSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProfileSettingsCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: ProfileSettingsCollection, name: str) -> bool """
        ...

    def IndexOf(self, name:str) -> int:
        """ IndexOf(self: ProfileSettingsCollection, name: str) -> int """
        ...

    def Insert(self, index:int, authorizationSettings:ProfileSettings): # -> 
        """ Insert(self: ProfileSettingsCollection, index: int, authorizationSettings: ProfileSettings) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProfileSettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ProfileSettingsCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProtocolCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProtocolCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: ProtocolCollection) -> Array[str] """
        ...


    def Add(self, protocolElement:ProtocolElement): # -> 
        """ Add(self: ProtocolCollection, protocolElement: ProtocolElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProtocolCollection) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: ProtocolCollection, name: str)Remove(self: ProtocolCollection, protocolElement: ProtocolElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ProtocolCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProtocolElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProtocolElement(name: str)
    ProtocolElement()
    """
    @property
    def AppDomainHandlerType(self) -> str:
        """
        Get: AppDomainHandlerType(self: ProtocolElement) -> str
        Set: AppDomainHandlerType(self: ProtocolElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ProtocolElement) -> str
        Set: Name(self: ProtocolElement) = value
        """
        ...

    @property
    def ProcessHandlerType(self) -> str:
        """
        Get: ProcessHandlerType(self: ProtocolElement) -> str
        Set: ProcessHandlerType(self: ProtocolElement) = value
        """
        ...

    @property
    def Validate(self) -> bool:
        """
        Get: Validate(self: ProtocolElement) -> bool
        Set: Validate(self: ProtocolElement) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        ...


class ProtocolsConfigurationHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ ProtocolsConfigurationHandler() """
    pass

class ProtocolsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ProtocolsSection() """
    @property
    def Protocols(self) -> ProtocolCollection:
        """ Get: Protocols(self: ProtocolsSection) -> ProtocolCollection """
        ...



class ProvidersHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def InstantiateProvider(providerSettings:ProviderSettings, providerType:Type) -> ProviderBase:
        """ InstantiateProvider(providerSettings: ProviderSettings, providerType: Type) -> ProviderBase """
        ...

    @staticmethod
    def InstantiateProviders(configProviders:ProviderSettingsCollection, providers:ProviderCollection, providerType:Type): # -> 
        """ InstantiateProviders(configProviders: ProviderSettingsCollection, providers: ProviderCollection, providerType: Type) """
        ...

    __all__: list = ...


class RegexWorker: # skipped bases: <type 'object'>, <type 'object'>
    """ RegexWorker(browserCaps: HttpBrowserCapabilities) """
    def ProcessRegex(self, target:str, regexExpression:str) -> bool:
        """ ProcessRegex(self: RegexWorker, target: str, regexExpression: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RemoteWebConfigurationHostServer(IRemoteWebConfigurationHostServer): # skipped bases: <type 'object'>
    """ RemoteWebConfigurationHostServer() """
    pass

class RoleManagerSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ RoleManagerSection() """
    @property
    def CacheRolesInCookie(self) -> bool:
        """
        Get: CacheRolesInCookie(self: RoleManagerSection) -> bool
        Set: CacheRolesInCookie(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookieName(self) -> str:
        """
        Get: CookieName(self: RoleManagerSection) -> str
        Set: CookieName(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookiePath(self) -> str:
        """
        Get: CookiePath(self: RoleManagerSection) -> str
        Set: CookiePath(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookieProtection(self): # -> CookieProtection
        """
        Get: CookieProtection(self: RoleManagerSection) -> CookieProtection
        Set: CookieProtection(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookieRequireSSL(self) -> bool:
        """
        Get: CookieRequireSSL(self: RoleManagerSection) -> bool
        Set: CookieRequireSSL(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookieSlidingExpiration(self) -> bool:
        """
        Get: CookieSlidingExpiration(self: RoleManagerSection) -> bool
        Set: CookieSlidingExpiration(self: RoleManagerSection) = value
        """
        ...

    @property
    def CookieTimeout(self) -> TimeSpan:
        """
        Get: CookieTimeout(self: RoleManagerSection) -> TimeSpan
        Set: CookieTimeout(self: RoleManagerSection) = value
        """
        ...

    @property
    def CreatePersistentCookie(self) -> bool:
        """
        Get: CreatePersistentCookie(self: RoleManagerSection) -> bool
        Set: CreatePersistentCookie(self: RoleManagerSection) = value
        """
        ...

    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: RoleManagerSection) -> str
        Set: DefaultProvider(self: RoleManagerSection) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: RoleManagerSection) -> str
        Set: Domain(self: RoleManagerSection) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: RoleManagerSection) -> bool
        Set: Enabled(self: RoleManagerSection) = value
        """
        ...

    @property
    def MaxCachedResults(self) -> int:
        """
        Get: MaxCachedResults(self: RoleManagerSection) -> int
        Set: MaxCachedResults(self: RoleManagerSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: RoleManagerSection) -> ProviderSettingsCollection """
        ...



class RootProfilePropertySettingsCollection(ProfilePropertySettingsCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ RootProfilePropertySettingsCollection() """
    @property
    def GroupSettings(self) -> ProfileGroupSettingsCollection:
        """ Get: GroupSettings(self: RootProfilePropertySettingsCollection) -> ProfileGroupSettingsCollection """
        ...


    def Equals(self, rootProfilePropertySettingsCollection:object) -> bool:
        """ Equals(self: RootProfilePropertySettingsCollection, rootProfilePropertySettingsCollection: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RootProfilePropertySettingsCollection) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    RuleSettings(name: str, eventName: str, provider: str)
    RuleSettings(name: str, eventName: str, provider: str, profile: str, minInstances: int, maxLimit: int, minInterval: TimeSpan)
    RuleSettings(name: str, eventName: str, provider: str, profile: str, minInstances: int, maxLimit: int, minInterval: TimeSpan, custom: str)
    """
    @property
    def Custom(self) -> str:
        """
        Get: Custom(self: RuleSettings) -> str
        Set: Custom(self: RuleSettings) = value
        """
        ...

    @property
    def EventName(self) -> str:
        """
        Get: EventName(self: RuleSettings) -> str
        Set: EventName(self: RuleSettings) = value
        """
        ...

    @property
    def MaxLimit(self) -> int:
        """
        Get: MaxLimit(self: RuleSettings) -> int
        Set: MaxLimit(self: RuleSettings) = value
        """
        ...

    @property
    def MinInstances(self) -> int:
        """
        Get: MinInstances(self: RuleSettings) -> int
        Set: MinInstances(self: RuleSettings) = value
        """
        ...

    @property
    def MinInterval(self) -> TimeSpan:
        """
        Get: MinInterval(self: RuleSettings) -> TimeSpan
        Set: MinInterval(self: RuleSettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RuleSettings) -> str
        Set: Name(self: RuleSettings) = value
        """
        ...

    @property
    def Profile(self) -> str:
        """
        Get: Profile(self: RuleSettings) -> str
        Set: Profile(self: RuleSettings) = value
        """
        ...

    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: RuleSettings) -> str
        Set: Provider(self: RuleSettings) = value
        """
        ...


    def __new__(cls, name:str, eventName:str, provider:str, profile:str = ..., minInstances:int = ..., maxLimit:int = ..., minInterval:TimeSpan = ..., custom:str = ...) -> Self:
        """
        __new__(cls: type, name: str, eventName: str, provider: str)
        __new__(cls: type, name: str, eventName: str, provider: str, profile: str, minInstances: int, maxLimit: int, minInterval: TimeSpan)
        __new__(cls: type, name: str, eventName: str, provider: str, profile: str, minInstances: int, maxLimit: int, minInterval: TimeSpan, custom: str)
        """
        ...


class RuleSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ RuleSettingsCollection() """
    def Add(self, ruleSettings:RuleSettings): # -> 
        """ Add(self: RuleSettingsCollection, ruleSettings: RuleSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: RuleSettingsCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: RuleSettingsCollection, name: str) -> bool """
        ...

    def IndexOf(self, name:str) -> int:
        """ IndexOf(self: RuleSettingsCollection, name: str) -> int """
        ...

    def Insert(self, index:int, eventSettings:RuleSettings): # -> 
        """ Insert(self: RuleSettingsCollection, index: int, eventSettings: RuleSettings) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: RuleSettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: RuleSettingsCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ScriptingAuthenticationServiceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ScriptingAuthenticationServiceSection() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ScriptingAuthenticationServiceSection) -> bool
        Set: Enabled(self: ScriptingAuthenticationServiceSection) = value
        """
        ...

    @property
    def RequireSSL(self) -> bool:
        """
        Get: RequireSSL(self: ScriptingAuthenticationServiceSection) -> bool
        Set: RequireSSL(self: ScriptingAuthenticationServiceSection) = value
        """
        ...



class ScriptingJsonSerializationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ScriptingJsonSerializationSection() """
    @property
    def Converters(self) -> ConvertersCollection:
        """ Get: Converters(self: ScriptingJsonSerializationSection) -> ConvertersCollection """
        ...

    @property
    def MaxJsonLength(self) -> int:
        """
        Get: MaxJsonLength(self: ScriptingJsonSerializationSection) -> int
        Set: MaxJsonLength(self: ScriptingJsonSerializationSection) = value
        """
        ...

    @property
    def RecursionLimit(self) -> int:
        """
        Get: RecursionLimit(self: ScriptingJsonSerializationSection) -> int
        Set: RecursionLimit(self: ScriptingJsonSerializationSection) = value
        """
        ...



class ScriptingProfileServiceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ScriptingProfileServiceSection() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ScriptingProfileServiceSection) -> bool
        Set: Enabled(self: ScriptingProfileServiceSection) = value
        """
        ...

    @property
    def ReadAccessProperties(self) -> Array:
        """
        Get: ReadAccessProperties(self: ScriptingProfileServiceSection) -> Array[str]
        Set: ReadAccessProperties(self: ScriptingProfileServiceSection) = value
        """
        ...

    @property
    def WriteAccessProperties(self) -> Array:
        """
        Get: WriteAccessProperties(self: ScriptingProfileServiceSection) -> Array[str]
        Set: WriteAccessProperties(self: ScriptingProfileServiceSection) = value
        """
        ...



class ScriptingRoleServiceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ScriptingRoleServiceSection() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ScriptingRoleServiceSection) -> bool
        Set: Enabled(self: ScriptingRoleServiceSection) = value
        """
        ...



class ScriptingScriptResourceHandlerSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ScriptingScriptResourceHandlerSection() """
    @property
    def EnableCaching(self) -> bool:
        """
        Get: EnableCaching(self: ScriptingScriptResourceHandlerSection) -> bool
        Set: EnableCaching(self: ScriptingScriptResourceHandlerSection) = value
        """
        ...

    @property
    def EnableCompression(self) -> bool:
        """
        Get: EnableCompression(self: ScriptingScriptResourceHandlerSection) -> bool
        Set: EnableCompression(self: ScriptingScriptResourceHandlerSection) = value
        """
        ...



class ScriptingSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ScriptingSectionGroup() """
    @property
    def ScriptResourceHandler(self) -> ScriptingScriptResourceHandlerSection:
        """ Get: ScriptResourceHandler(self: ScriptingSectionGroup) -> ScriptingScriptResourceHandlerSection """
        ...

    @property
    def WebServices(self) -> ScriptingWebServicesSectionGroup:
        """ Get: WebServices(self: ScriptingSectionGroup) -> ScriptingWebServicesSectionGroup """
        ...



class ScriptingWebServicesSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ScriptingWebServicesSectionGroup() """
    @property
    def AuthenticationService(self) -> ScriptingAuthenticationServiceSection:
        """ Get: AuthenticationService(self: ScriptingWebServicesSectionGroup) -> ScriptingAuthenticationServiceSection """
        ...

    @property
    def JsonSerialization(self) -> ScriptingJsonSerializationSection:
        """ Get: JsonSerialization(self: ScriptingWebServicesSectionGroup) -> ScriptingJsonSerializationSection """
        ...

    @property
    def ProfileService(self) -> ScriptingProfileServiceSection:
        """ Get: ProfileService(self: ScriptingWebServicesSectionGroup) -> ScriptingProfileServiceSection """
        ...

    @property
    def RoleService(self) -> ScriptingRoleServiceSection:
        """ Get: RoleService(self: ScriptingWebServicesSectionGroup) -> ScriptingRoleServiceSection """
        ...



class SecurityPolicySection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SecurityPolicySection() """
    @property
    def TrustLevels(self): # -> TrustLevelCollection
        """ Get: TrustLevels(self: SecurityPolicySection) -> TrustLevelCollection """
        ...



class SerializationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerializationMode, values: Binary (2), ProviderSpecific (3), String (0), Xml (1) """
    Binary: SerializationMode = ...
    ProviderSpecific: SerializationMode = ...
    String: SerializationMode = ...
    value__ = ...
    Xml: SerializationMode = ...


class SessionPageStateSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SessionPageStateSection() """
    @property
    def HistorySize(self) -> int:
        """
        Get: HistorySize(self: SessionPageStateSection) -> int
        Set: HistorySize(self: SessionPageStateSection) = value
        """
        ...


    DefaultHistorySize: int = ...


class SessionStateSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SessionStateSection() """
    @property
    def AllowCustomSqlDatabase(self) -> bool:
        """
        Get: AllowCustomSqlDatabase(self: SessionStateSection) -> bool
        Set: AllowCustomSqlDatabase(self: SessionStateSection) = value
        """
        ...

    @property
    def CompressionEnabled(self) -> bool:
        """
        Get: CompressionEnabled(self: SessionStateSection) -> bool
        Set: CompressionEnabled(self: SessionStateSection) = value
        """
        ...

    @property
    def Cookieless(self) -> HttpCookieMode:
        """
        Get: Cookieless(self: SessionStateSection) -> HttpCookieMode
        Set: Cookieless(self: SessionStateSection) = value
        """
        ...

    @property
    def CookieName(self) -> str:
        """
        Get: CookieName(self: SessionStateSection) -> str
        Set: CookieName(self: SessionStateSection) = value
        """
        ...

    @property
    def CookieSameSite(self) -> SameSiteMode:
        """
        Get: CookieSameSite(self: SessionStateSection) -> SameSiteMode
        Set: CookieSameSite(self: SessionStateSection) = value
        """
        ...

    @property
    def CustomProvider(self) -> str:
        """
        Get: CustomProvider(self: SessionStateSection) -> str
        Set: CustomProvider(self: SessionStateSection) = value
        """
        ...

    @property
    def Mode(self) -> SessionStateMode:
        """
        Get: Mode(self: SessionStateSection) -> SessionStateMode
        Set: Mode(self: SessionStateSection) = value
        """
        ...

    @property
    def PartitionResolverType(self) -> str:
        """
        Get: PartitionResolverType(self: SessionStateSection) -> str
        Set: PartitionResolverType(self: SessionStateSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: SessionStateSection) -> ProviderSettingsCollection """
        ...

    @property
    def RegenerateExpiredSessionId(self) -> bool:
        """
        Get: RegenerateExpiredSessionId(self: SessionStateSection) -> bool
        Set: RegenerateExpiredSessionId(self: SessionStateSection) = value
        """
        ...

    @property
    def SessionIDManagerType(self) -> str:
        """
        Get: SessionIDManagerType(self: SessionStateSection) -> str
        Set: SessionIDManagerType(self: SessionStateSection) = value
        """
        ...

    @property
    def SqlCommandTimeout(self) -> TimeSpan:
        """
        Get: SqlCommandTimeout(self: SessionStateSection) -> TimeSpan
        Set: SqlCommandTimeout(self: SessionStateSection) = value
        """
        ...

    @property
    def SqlConnectionRetryInterval(self) -> TimeSpan:
        """
        Get: SqlConnectionRetryInterval(self: SessionStateSection) -> TimeSpan
        Set: SqlConnectionRetryInterval(self: SessionStateSection) = value
        """
        ...

    @property
    def SqlConnectionString(self) -> str:
        """
        Get: SqlConnectionString(self: SessionStateSection) -> str
        Set: SqlConnectionString(self: SessionStateSection) = value
        """
        ...

    @property
    def StateConnectionString(self) -> str:
        """
        Get: StateConnectionString(self: SessionStateSection) -> str
        Set: StateConnectionString(self: SessionStateSection) = value
        """
        ...

    @property
    def StateNetworkTimeout(self) -> TimeSpan:
        """
        Get: StateNetworkTimeout(self: SessionStateSection) -> TimeSpan
        Set: StateNetworkTimeout(self: SessionStateSection) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: SessionStateSection) -> TimeSpan
        Set: Timeout(self: SessionStateSection) = value
        """
        ...

    @property
    def UseHostingIdentity(self) -> bool:
        """
        Get: UseHostingIdentity(self: SessionStateSection) -> bool
        Set: UseHostingIdentity(self: SessionStateSection) = value
        """
        ...



class SiteMapSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SiteMapSection() """
    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: SiteMapSection) -> str
        Set: DefaultProvider(self: SiteMapSection) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: SiteMapSection) -> bool
        Set: Enabled(self: SiteMapSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: SiteMapSection) -> ProviderSettingsCollection """
        ...



class SqlCacheDependencyDatabase(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SqlCacheDependencyDatabase(name: str, connectionStringName: str, pollTime: int)
    SqlCacheDependencyDatabase(name: str, connectionStringName: str)
    """
    @property
    def ConnectionStringName(self) -> str:
        """
        Get: ConnectionStringName(self: SqlCacheDependencyDatabase) -> str
        Set: ConnectionStringName(self: SqlCacheDependencyDatabase) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlCacheDependencyDatabase) -> str
        Set: Name(self: SqlCacheDependencyDatabase) = value
        """
        ...

    @property
    def PollTime(self) -> int:
        """
        Get: PollTime(self: SqlCacheDependencyDatabase) -> int
        Set: PollTime(self: SqlCacheDependencyDatabase) = value
        """
        ...


    def __new__(cls, name:str, connectionStringName:str, pollTime:int = ...) -> Self:
        """
        __new__(cls: type, name: str, connectionStringName: str, pollTime: int)
        __new__(cls: type, name: str, connectionStringName: str)
        """
        ...


class SqlCacheDependencyDatabaseCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SqlCacheDependencyDatabaseCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: SqlCacheDependencyDatabaseCollection) -> Array[str] """
        ...


    def Add(self, name:SqlCacheDependencyDatabase): # -> 
        """ Add(self: SqlCacheDependencyDatabaseCollection, name: SqlCacheDependencyDatabase) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SqlCacheDependencyDatabaseCollection) """
        ...

    def Get(self, *__args:int) -> SqlCacheDependencyDatabase:
        """
        Get(self: SqlCacheDependencyDatabaseCollection, index: int) -> SqlCacheDependencyDatabase
        Get(self: SqlCacheDependencyDatabaseCollection, name: str) -> SqlCacheDependencyDatabase
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: SqlCacheDependencyDatabaseCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: SqlCacheDependencyDatabaseCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SqlCacheDependencyDatabaseCollection, index: int) """
        ...

    def Set(self, user:SqlCacheDependencyDatabase): # -> 
        """ Set(self: SqlCacheDependencyDatabaseCollection, user: SqlCacheDependencyDatabase) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class SqlCacheDependencySection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SqlCacheDependencySection() """
    @property
    def Databases(self) -> SqlCacheDependencyDatabaseCollection:
        """ Get: Databases(self: SqlCacheDependencySection) -> SqlCacheDependencyDatabaseCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: SqlCacheDependencySection) -> bool
        Set: Enabled(self: SqlCacheDependencySection) = value
        """
        ...

    @property
    def PollTime(self) -> int:
        """
        Get: PollTime(self: SqlCacheDependencySection) -> int
        Set: PollTime(self: SqlCacheDependencySection) = value
        """
        ...



class SystemWebCachingSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ SystemWebCachingSectionGroup() """
    @property
    def Cache(self) -> CacheSection:
        """ Get: Cache(self: SystemWebCachingSectionGroup) -> CacheSection """
        ...

    @property
    def OutputCache(self) -> OutputCacheSection:
        """ Get: OutputCache(self: SystemWebCachingSectionGroup) -> OutputCacheSection """
        ...

    @property
    def OutputCacheSettings(self) -> OutputCacheSettingsSection:
        """ Get: OutputCacheSettings(self: SystemWebCachingSectionGroup) -> OutputCacheSettingsSection """
        ...

    @property
    def SqlCacheDependency(self) -> SqlCacheDependencySection:
        """ Get: SqlCacheDependency(self: SystemWebCachingSectionGroup) -> SqlCacheDependencySection """
        ...



class SystemWebExtensionsSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ SystemWebExtensionsSectionGroup() """
    @property
    def Scripting(self) -> ScriptingSectionGroup:
        """ Get: Scripting(self: SystemWebExtensionsSectionGroup) -> ScriptingSectionGroup """
        ...



class SystemWebSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ SystemWebSectionGroup() """
    @property
    def AnonymousIdentification(self) -> AnonymousIdentificationSection:
        """ Get: AnonymousIdentification(self: SystemWebSectionGroup) -> AnonymousIdentificationSection """
        ...

    @property
    def Authentication(self) -> AuthenticationSection:
        """ Get: Authentication(self: SystemWebSectionGroup) -> AuthenticationSection """
        ...

    @property
    def Authorization(self) -> AuthorizationSection:
        """ Get: Authorization(self: SystemWebSectionGroup) -> AuthorizationSection """
        ...

    @property
    def BrowserCaps(self) -> DefaultSection:
        """ Get: BrowserCaps(self: SystemWebSectionGroup) -> DefaultSection """
        ...

    @property
    def ClientTarget(self) -> ClientTargetSection:
        """ Get: ClientTarget(self: SystemWebSectionGroup) -> ClientTargetSection """
        ...

    @property
    def Compilation(self) -> CompilationSection:
        """ Get: Compilation(self: SystemWebSectionGroup) -> CompilationSection """
        ...

    @property
    def CustomErrors(self) -> CustomErrorsSection:
        """ Get: CustomErrors(self: SystemWebSectionGroup) -> CustomErrorsSection """
        ...

    @property
    def Deployment(self) -> DeploymentSection:
        """ Get: Deployment(self: SystemWebSectionGroup) -> DeploymentSection """
        ...

    @property
    def DeviceFilters(self) -> DefaultSection:
        """ Get: DeviceFilters(self: SystemWebSectionGroup) -> DefaultSection """
        ...

    @property
    def FullTrustAssemblies(self) -> FullTrustAssembliesSection:
        """ Get: FullTrustAssemblies(self: SystemWebSectionGroup) -> FullTrustAssembliesSection """
        ...

    @property
    def Globalization(self) -> GlobalizationSection:
        """ Get: Globalization(self: SystemWebSectionGroup) -> GlobalizationSection """
        ...

    @property
    def HealthMonitoring(self) -> HealthMonitoringSection:
        """ Get: HealthMonitoring(self: SystemWebSectionGroup) -> HealthMonitoringSection """
        ...

    @property
    def HostingEnvironment(self) -> HostingEnvironmentSection:
        """ Get: HostingEnvironment(self: SystemWebSectionGroup) -> HostingEnvironmentSection """
        ...

    @property
    def HttpCookies(self) -> HttpCookiesSection:
        """ Get: HttpCookies(self: SystemWebSectionGroup) -> HttpCookiesSection """
        ...

    @property
    def HttpHandlers(self) -> HttpHandlersSection:
        """ Get: HttpHandlers(self: SystemWebSectionGroup) -> HttpHandlersSection """
        ...

    @property
    def HttpModules(self) -> HttpModulesSection:
        """ Get: HttpModules(self: SystemWebSectionGroup) -> HttpModulesSection """
        ...

    @property
    def HttpRuntime(self) -> HttpRuntimeSection:
        """ Get: HttpRuntime(self: SystemWebSectionGroup) -> HttpRuntimeSection """
        ...

    @property
    def Identity(self) -> IdentitySection:
        """ Get: Identity(self: SystemWebSectionGroup) -> IdentitySection """
        ...

    @property
    def MachineKey(self) -> MachineKeySection:
        """ Get: MachineKey(self: SystemWebSectionGroup) -> MachineKeySection """
        ...

    @property
    def Membership(self) -> MembershipSection:
        """ Get: Membership(self: SystemWebSectionGroup) -> MembershipSection """
        ...

    @property
    def MobileControls(self) -> ConfigurationSection:
        """ Get: MobileControls(self: SystemWebSectionGroup) -> ConfigurationSection """
        ...

    @property
    def Pages(self) -> PagesSection:
        """ Get: Pages(self: SystemWebSectionGroup) -> PagesSection """
        ...

    @property
    def PartialTrustVisibleAssemblies(self) -> PartialTrustVisibleAssembliesSection:
        """ Get: PartialTrustVisibleAssemblies(self: SystemWebSectionGroup) -> PartialTrustVisibleAssembliesSection """
        ...

    @property
    def ProcessModel(self) -> ProcessModelSection:
        """ Get: ProcessModel(self: SystemWebSectionGroup) -> ProcessModelSection """
        ...

    @property
    def Profile(self) -> ProfileSection:
        """ Get: Profile(self: SystemWebSectionGroup) -> ProfileSection """
        ...

    @property
    def Protocols(self) -> DefaultSection:
        """ Get: Protocols(self: SystemWebSectionGroup) -> DefaultSection """
        ...

    @property
    def RoleManager(self) -> RoleManagerSection:
        """ Get: RoleManager(self: SystemWebSectionGroup) -> RoleManagerSection """
        ...

    @property
    def SecurityPolicy(self) -> SecurityPolicySection:
        """ Get: SecurityPolicy(self: SystemWebSectionGroup) -> SecurityPolicySection """
        ...

    @property
    def SessionState(self) -> SessionStateSection:
        """ Get: SessionState(self: SystemWebSectionGroup) -> SessionStateSection """
        ...

    @property
    def SiteMap(self) -> SiteMapSection:
        """ Get: SiteMap(self: SystemWebSectionGroup) -> SiteMapSection """
        ...

    @property
    def Trace(self): # -> TraceSection
        """ Get: Trace(self: SystemWebSectionGroup) -> TraceSection """
        ...

    @property
    def Trust(self): # -> TrustSection
        """ Get: Trust(self: SystemWebSectionGroup) -> TrustSection """
        ...

    @property
    def UrlMappings(self): # -> UrlMappingsSection
        """ Get: UrlMappings(self: SystemWebSectionGroup) -> UrlMappingsSection """
        ...

    @property
    def WebControls(self): # -> WebControlsSection
        """ Get: WebControls(self: SystemWebSectionGroup) -> WebControlsSection """
        ...

    @property
    def WebParts(self): # -> WebPartsSection
        """ Get: WebParts(self: SystemWebSectionGroup) -> WebPartsSection """
        ...

    @property
    def WebServices(self) -> WebServicesSection:
        """ Get: WebServices(self: SystemWebSectionGroup) -> WebServicesSection """
        ...

    @property
    def XhtmlConformance(self): # -> XhtmlConformanceSection
        """ Get: XhtmlConformance(self: SystemWebSectionGroup) -> XhtmlConformanceSection """
        ...



class TagMapCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TagMapCollection() """
    def Add(self, tagMapInformation): # ->  # Not found arg types: {'tagMapInformation': 'TagMapInfo'}
        """ Add(self: TagMapCollection, tagMapInformation: TagMapInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TagMapCollection) """
        ...

    def Remove(self, tagMapInformation): # ->  # Not found arg types: {'tagMapInformation': 'TagMapInfo'}
        """ Remove(self: TagMapCollection, tagMapInformation: TagMapInfo) """
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


class TagMapInfo(ConfigurationElement): # skipped bases: <type 'object'>
    """ TagMapInfo(tagTypeName: str, mappedTagTypeName: str) """
    @property
    def MappedTagType(self) -> str:
        """
        Get: MappedTagType(self: TagMapInfo) -> str
        Set: MappedTagType(self: TagMapInfo) = value
        """
        ...

    @property
    def TagType(self) -> str:
        """
        Get: TagType(self: TagMapInfo) -> str
        Set: TagType(self: TagMapInfo) = value
        """
        ...


    def __new__(cls, tagTypeName:str, mappedTagTypeName:str) -> Self:
        """ __new__(cls: type, tagTypeName: str, mappedTagTypeName: str) """
        ...


class TagPrefixCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TagPrefixCollection() """
    def Add(self, tagPrefixInformation): # ->  # Not found arg types: {'tagPrefixInformation': 'TagPrefixInfo'}
        """ Add(self: TagPrefixCollection, tagPrefixInformation: TagPrefixInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TagPrefixCollection) """
        ...

    def Remove(self, tagPrefixInformation): # ->  # Not found arg types: {'tagPrefixInformation': 'TagPrefixInfo'}
        """ Remove(self: TagPrefixCollection, tagPrefixInformation: TagPrefixInfo) """
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


class TagPrefixInfo(ConfigurationElement): # skipped bases: <type 'object'>
    """ TagPrefixInfo(tagPrefix: str, nameSpace: str, assembly: str, tagName: str, source: str) """
    @property
    def Assembly(self) -> str:
        """
        Get: Assembly(self: TagPrefixInfo) -> str
        Set: Assembly(self: TagPrefixInfo) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: TagPrefixInfo) -> str
        Set: Namespace(self: TagPrefixInfo) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: TagPrefixInfo) -> str
        Set: Source(self: TagPrefixInfo) = value
        """
        ...

    @property
    def TagName(self) -> str:
        """
        Get: TagName(self: TagPrefixInfo) -> str
        Set: TagName(self: TagPrefixInfo) = value
        """
        ...

    @property
    def TagPrefix(self) -> str:
        """
        Get: TagPrefix(self: TagPrefixInfo) -> str
        Set: TagPrefix(self: TagPrefixInfo) = value
        """
        ...


    def __new__(cls, tagPrefix:str, nameSpace:str, assembly:str, tagName:str, source:str) -> Self:
        """ __new__(cls: type, tagPrefix: str, nameSpace: str, assembly: str, tagName: str, source: str) """
        ...


class TicketCompatibilityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TicketCompatibilityMode, values: Framework20 (0), Framework40 (1) """
    Framework20: TicketCompatibilityMode = ...
    Framework40: TicketCompatibilityMode = ...
    value__ = ...


class TraceDisplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceDisplayMode, values: SortByCategory (2), SortByTime (1) """
    SortByCategory: TraceDisplayMode = ...
    SortByTime: TraceDisplayMode = ...
    value__ = ...


class TraceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ TraceSection() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: TraceSection) -> bool
        Set: Enabled(self: TraceSection) = value
        """
        ...

    @property
    def LocalOnly(self) -> bool:
        """
        Get: LocalOnly(self: TraceSection) -> bool
        Set: LocalOnly(self: TraceSection) = value
        """
        ...

    @property
    def MostRecent(self) -> bool:
        """
        Get: MostRecent(self: TraceSection) -> bool
        Set: MostRecent(self: TraceSection) = value
        """
        ...

    @property
    def PageOutput(self) -> bool:
        """
        Get: PageOutput(self: TraceSection) -> bool
        Set: PageOutput(self: TraceSection) = value
        """
        ...

    @property
    def RequestLimit(self) -> int:
        """
        Get: RequestLimit(self: TraceSection) -> int
        Set: RequestLimit(self: TraceSection) = value
        """
        ...

    @property
    def TraceMode(self) -> TraceDisplayMode:
        """
        Get: TraceMode(self: TraceSection) -> TraceDisplayMode
        Set: TraceMode(self: TraceSection) = value
        """
        ...

    @property
    def WriteToDiagnosticsTrace(self) -> bool:
        """
        Get: WriteToDiagnosticsTrace(self: TraceSection) -> bool
        Set: WriteToDiagnosticsTrace(self: TraceSection) = value
        """
        ...



class TransformerInfo(ConfigurationElement): # skipped bases: <type 'object'>
    """ TransformerInfo(name: str, type: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: TransformerInfo) -> str
        Set: Name(self: TransformerInfo) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: TransformerInfo) -> str
        Set: Type(self: TransformerInfo) = value
        """
        ...


    def __new__(cls, name:str, type:str) -> Self:
        """ __new__(cls: type, name: str, type: str) """
        ...


class TransformerInfoCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TransformerInfoCollection() """
    def Add(self, transformerInfo:TransformerInfo): # -> 
        """ Add(self: TransformerInfoCollection, transformerInfo: TransformerInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TransformerInfoCollection) """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: TransformerInfoCollection, s: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TransformerInfoCollection, index: int) """
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


class TrustLevel(ConfigurationElement): # skipped bases: <type 'object'>
    """ TrustLevel(name: str, policyFile: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: TrustLevel) -> str
        Set: Name(self: TrustLevel) = value
        """
        ...

    @property
    def PolicyFile(self) -> str:
        """
        Get: PolicyFile(self: TrustLevel) -> str
        Set: PolicyFile(self: TrustLevel) = value
        """
        ...


    def __new__(cls, name:str, policyFile:str) -> Self:
        """ __new__(cls: type, name: str, policyFile: str) """
        ...


class TrustLevelCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TrustLevelCollection() """
    def Add(self, trustLevel:TrustLevel): # -> 
        """ Add(self: TrustLevelCollection, trustLevel: TrustLevel) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TrustLevelCollection) """
        ...

    def Get(self, index:int) -> TrustLevel:
        """ Get(self: TrustLevelCollection, index: int) -> TrustLevel """
        ...

    def Remove(self, trustLevel:TrustLevel): # -> 
        """ Remove(self: TrustLevelCollection, trustLevel: TrustLevel) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TrustLevelCollection, index: int) """
        ...

    def Set(self, index:int, trustLevel:TrustLevel): # -> 
        """ Set(self: TrustLevelCollection, index: int, trustLevel: TrustLevel) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class TrustSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ TrustSection() """
    @property
    def HostSecurityPolicyResolverType(self) -> str:
        """
        Get: HostSecurityPolicyResolverType(self: TrustSection) -> str
        Set: HostSecurityPolicyResolverType(self: TrustSection) = value
        """
        ...

    @property
    def LegacyCasModel(self) -> bool:
        """
        Get: LegacyCasModel(self: TrustSection) -> bool
        Set: LegacyCasModel(self: TrustSection) = value
        """
        ...

    @property
    def Level(self) -> str:
        """
        Get: Level(self: TrustSection) -> str
        Set: Level(self: TrustSection) = value
        """
        ...

    @property
    def OriginUrl(self) -> str:
        """
        Get: OriginUrl(self: TrustSection) -> str
        Set: OriginUrl(self: TrustSection) = value
        """
        ...

    @property
    def PermissionSetName(self) -> str:
        """
        Get: PermissionSetName(self: TrustSection) -> str
        Set: PermissionSetName(self: TrustSection) = value
        """
        ...

    @property
    def ProcessRequestInApplicationTrust(self) -> bool:
        """
        Get: ProcessRequestInApplicationTrust(self: TrustSection) -> bool
        Set: ProcessRequestInApplicationTrust(self: TrustSection) = value
        """
        ...



class UrlMapping(ConfigurationElement): # skipped bases: <type 'object'>
    """ UrlMapping(url: str, mappedUrl: str) """
    @property
    def MappedUrl(self) -> str:
        """ Get: MappedUrl(self: UrlMapping) -> str """
        ...

    @property
    def Url(self) -> str:
        """ Get: Url(self: UrlMapping) -> str """
        ...


    def __new__(cls, url:str, mappedUrl:str) -> Self:
        """ __new__(cls: type, url: str, mappedUrl: str) """
        ...


class UrlMappingCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ UrlMappingCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: UrlMappingCollection) -> Array[str] """
        ...


    def Add(self, urlMapping:UrlMapping): # -> 
        """ Add(self: UrlMappingCollection, urlMapping: UrlMapping) """
        ...

    def Clear(self): # -> 
        """ Clear(self: UrlMappingCollection) """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: UrlMappingCollection, index: int) -> str """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: UrlMappingCollection, name: str)Remove(self: UrlMappingCollection, urlMapping: UrlMapping) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: UrlMappingCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class UrlMappingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ UrlMappingsSection() """
    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: UrlMappingsSection) -> bool
        Set: IsEnabled(self: UrlMappingsSection) = value
        """
        ...

    @property
    def UrlMappings(self) -> UrlMappingCollection:
        """ Get: UrlMappings(self: UrlMappingsSection) -> UrlMappingCollection """
        ...



class UserMapPath(IConfigMapPath): # skipped bases: <type 'object'>
    """ UserMapPath(fileMap: ConfigurationFileMap) """
    pass

class VirtualDirectoryMapping: # skipped bases: <type 'object'>, <type 'object'>
    """
    VirtualDirectoryMapping(physicalDirectory: str, isAppRoot: bool)
    VirtualDirectoryMapping(physicalDirectory: str, isAppRoot: bool, configFileBaseName: str)
    """
    @property
    def ConfigFileBaseName(self) -> str:
        """
        Get: ConfigFileBaseName(self: VirtualDirectoryMapping) -> str
        Set: ConfigFileBaseName(self: VirtualDirectoryMapping) = value
        """
        ...

    @property
    def IsAppRoot(self) -> bool:
        """
        Get: IsAppRoot(self: VirtualDirectoryMapping) -> bool
        Set: IsAppRoot(self: VirtualDirectoryMapping) = value
        """
        ...

    @property
    def PhysicalDirectory(self) -> str:
        """
        Get: PhysicalDirectory(self: VirtualDirectoryMapping) -> str
        Set: PhysicalDirectory(self: VirtualDirectoryMapping) = value
        """
        ...

    @property
    def VirtualDirectory(self) -> str:
        """ Get: VirtualDirectory(self: VirtualDirectoryMapping) -> str """
        ...



class VirtualDirectoryMappingCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ VirtualDirectoryMappingCollection() """
    @property
    def AllKeys(self) -> ICollection:
        """ Get: AllKeys(self: VirtualDirectoryMappingCollection) -> ICollection """
        ...


    def Add(self, virtualDirectory:str, mapping:VirtualDirectoryMapping): # -> 
        """ Add(self: VirtualDirectoryMappingCollection, virtualDirectory: str, mapping: VirtualDirectoryMapping) """
        ...

    def Clear(self): # -> 
        """ Clear(self: VirtualDirectoryMappingCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: VirtualDirectoryMappingCollection, array: Array[VirtualDirectoryMapping], index: int) """
        ...

    def Get(self, *__args:int) -> VirtualDirectoryMapping:
        """
        Get(self: VirtualDirectoryMappingCollection, index: int) -> VirtualDirectoryMapping
        Get(self: VirtualDirectoryMappingCollection, virtualDirectory: str) -> VirtualDirectoryMapping
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: VirtualDirectoryMappingCollection, index: int) -> str """
        ...

    def Remove(self, virtualDirectory:str): # -> 
        """ Remove(self: VirtualDirectoryMappingCollection, virtualDirectory: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: VirtualDirectoryMappingCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class WebApplicationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebApplicationLevel, values: AboveApplication (10), AtApplication (20), BelowApplication (30) """
    AboveApplication: WebApplicationLevel = ...
    AtApplication: WebApplicationLevel = ...
    BelowApplication: WebApplicationLevel = ...
    value__ = ...


class WebConfigurationFileMap(ConfigurationFileMap): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    WebConfigurationFileMap()
    WebConfigurationFileMap(machineConfigFileName: str)
    """
    @property
    def VirtualDirectories(self) -> VirtualDirectoryMappingCollection:
        """ Get: VirtualDirectories(self: WebConfigurationFileMap) -> VirtualDirectoryMappingCollection """
        ...



class WebConfigurationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppSettings(self) -> NameValueCollection:
        """ Get: AppSettings() -> NameValueCollection """
        ...

    @property
    def ConnectionStrings(self) -> ConnectionStringSettingsCollection:
        """ Get: ConnectionStrings() -> ConnectionStringSettingsCollection """
        ...


    @staticmethod
    def GetSection(sectionName:str, path:str = ...) -> object:
        """
        GetSection(sectionName: str, path: str) -> object
        GetSection(sectionName: str) -> object
        """
        ...

    @staticmethod
    def GetWebApplicationSection(sectionName:str) -> object:
        """ GetWebApplicationSection(sectionName: str) -> object """
        ...

    @staticmethod
    def OpenMachineConfiguration(locationSubPath:str = ..., server:str = ..., *__args:IntPtr) -> Configuration:
        """
        OpenMachineConfiguration(locationSubPath: str, server: str, userToken: IntPtr) -> Configuration
        OpenMachineConfiguration() -> Configuration
        OpenMachineConfiguration(locationSubPath: str) -> Configuration
        OpenMachineConfiguration(locationSubPath: str, server: str) -> Configuration
        OpenMachineConfiguration(locationSubPath: str, server: str, userName: str, password: str) -> Configuration
        """
        ...

    @staticmethod
    def OpenMappedMachineConfiguration(fileMap:ConfigurationFileMap, locationSubPath:str = ...) -> Configuration:
        """
        OpenMappedMachineConfiguration(fileMap: ConfigurationFileMap) -> Configuration
        OpenMappedMachineConfiguration(fileMap: ConfigurationFileMap, locationSubPath: str) -> Configuration
        """
        ...

    @staticmethod
    def OpenMappedWebConfiguration(fileMap:WebConfigurationFileMap, path:str, site:str = ..., locationSubPath:str = ...) -> Configuration:
        """
        OpenMappedWebConfiguration(fileMap: WebConfigurationFileMap, path: str) -> Configuration
        OpenMappedWebConfiguration(fileMap: WebConfigurationFileMap, path: str, site: str) -> Configuration
        OpenMappedWebConfiguration(fileMap: WebConfigurationFileMap, path: str, site: str, locationSubPath: str) -> Configuration
        """
        ...

    @staticmethod
    def OpenWebConfiguration(path:str, site:str = ..., locationSubPath:str = ..., server:str = ..., *__args:IntPtr) -> Configuration:
        """
        OpenWebConfiguration(path: str, site: str, locationSubPath: str, server: str, userToken: IntPtr) -> Configuration
        OpenWebConfiguration(path: str) -> Configuration
        OpenWebConfiguration(path: str, site: str) -> Configuration
        OpenWebConfiguration(path: str, site: str, locationSubPath: str) -> Configuration
        OpenWebConfiguration(path: str, site: str, locationSubPath: str, server: str) -> Configuration
        OpenWebConfiguration(path: str, site: str, locationSubPath: str, server: str, userName: str, password: str) -> Configuration
        """
        ...

    __all__: list = ...


class WebContext: # skipped bases: <type 'object'>, <type 'object'>
    """ WebContext(pathLevel: WebApplicationLevel, site: str, applicationPath: str, path: str, locationSubPath: str, appConfigPath: str) """
    @property
    def ApplicationLevel(self) -> WebApplicationLevel:
        """ Get: ApplicationLevel(self: WebContext) -> WebApplicationLevel """
        ...

    @property
    def ApplicationPath(self) -> str:
        """ Get: ApplicationPath(self: WebContext) -> str """
        ...

    @property
    def LocationSubPath(self) -> str:
        """ Get: LocationSubPath(self: WebContext) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: WebContext) -> str """
        ...

    @property
    def Site(self) -> str:
        """ Get: Site(self: WebContext) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: WebContext) -> str """
        ...


class WebControlsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WebControlsSection() """
    @property
    def ClientScriptsLocation(self) -> str:
        """ Get: ClientScriptsLocation(self: WebControlsSection) -> str """
        ...



class WebPartsPersonalization(ConfigurationElement): # skipped bases: <type 'object'>
    """ WebPartsPersonalization() """
    @property
    def Authorization(self): # -> WebPartsPersonalizationAuthorization
        """ Get: Authorization(self: WebPartsPersonalization) -> WebPartsPersonalizationAuthorization """
        ...

    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: WebPartsPersonalization) -> str
        Set: DefaultProvider(self: WebPartsPersonalization) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: WebPartsPersonalization) -> ProviderSettingsCollection """
        ...



class WebPartsPersonalizationAuthorization(ConfigurationElement): # skipped bases: <type 'object'>
    """ WebPartsPersonalizationAuthorization() """
    @property
    def Rules(self) -> AuthorizationRuleCollection:
        """ Get: Rules(self: WebPartsPersonalizationAuthorization) -> AuthorizationRuleCollection """
        ...



class WebPartsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WebPartsSection() """
    @property
    def EnableExport(self) -> bool:
        """
        Get: EnableExport(self: WebPartsSection) -> bool
        Set: EnableExport(self: WebPartsSection) = value
        """
        ...

    @property
    def Personalization(self) -> WebPartsPersonalization:
        """ Get: Personalization(self: WebPartsSection) -> WebPartsPersonalization """
        ...

    @property
    def Transformers(self) -> TransformerInfoCollection:
        """ Get: Transformers(self: WebPartsSection) -> TransformerInfoCollection """
        ...



class XhtmlConformanceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XhtmlConformanceMode, values: Legacy (1), Strict (2), Transitional (0) """
    Legacy: XhtmlConformanceMode = ...
    Strict: XhtmlConformanceMode = ...
    Transitional: XhtmlConformanceMode = ...
    value__ = ...


class XhtmlConformanceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ XhtmlConformanceSection() """
    @property
    def Mode(self) -> XhtmlConformanceMode:
        """
        Get: Mode(self: XhtmlConformanceSection) -> XhtmlConformanceMode
        Set: Mode(self: XhtmlConformanceSection) = value
        """
        ...



# variables with complex values

