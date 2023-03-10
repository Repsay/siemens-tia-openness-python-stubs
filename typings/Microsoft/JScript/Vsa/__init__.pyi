# encoding: utf-8
# module Microsoft.JScript.Vsa calls itself Vsa
# from Microsoft.JScript, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import (ArrayConstructor, GlobalScope, IEngine2, 
    IRedirectOutput, LenientGlobalObject, ObjectConstructor, 
    RegExpConstructor, ScriptObject)

from System import Array, Enum, RuntimeTypeHandle, _AppDomain

from System.CodeDom import CodeObject

from System.Collections import Hashtable, IEnumerable

from System.Reflection import Assembly

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Policy import Evidence

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class BaseVsaEngine(IJSVsaEngine): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AppDomain(self) -> _AppDomain:
        """
        Get: AppDomain(self: BaseVsaEngine) -> _AppDomain
        Set: AppDomain(self: BaseVsaEngine) = value
        """
        ...

    @property
    def ApplicationBase(self) -> str:
        """
        Get: ApplicationBase(self: BaseVsaEngine) -> str
        Set: ApplicationBase(self: BaseVsaEngine) = value
        """
        ...


    def DoClose(self, *args): #cannot find CLR method
        """ DoClose(self: BaseVsaEngine) """
        ...

    def DoCompile(self, *args): #cannot find CLR method
        """ DoCompile(self: BaseVsaEngine) -> bool """
        ...

    def DoLoadSourceState(self, *args): #cannot find CLR method
        """ DoLoadSourceState(self: BaseVsaEngine, site: IJSVsaPersistSite) """
        ...

    def DoSaveCompiledState(self, *args): #cannot find CLR method
        """ DoSaveCompiledState(self: BaseVsaEngine) -> (Array[Byte], Array[Byte]) """
        ...

    def DoSaveSourceState(self, *args): #cannot find CLR method
        """ DoSaveSourceState(self: BaseVsaEngine, site: IJSVsaPersistSite) """
        ...

    def Error(self, *args): #cannot find CLR method
        """ Error(self: BaseVsaEngine, vsaErrorNumber: JSVsaError) -> JSVsaException """
        ...

    def GetCustomOption(self, *args): #cannot find CLR method
        """ GetCustomOption(self: BaseVsaEngine, name: str) -> object """
        ...

    def IsValidNamespaceName(self, *args): #cannot find CLR method
        """ IsValidNamespaceName(self: BaseVsaEngine, name: str) -> bool """
        ...

    def LoadCompiledState(self, *args): #cannot find CLR method
        """ LoadCompiledState(self: BaseVsaEngine) -> Assembly """
        ...

    def Pre(self, *args): #cannot find CLR method
        """ enum (flags) Pre, values: EngineCompiled (4), EngineInitialised (1024), EngineNotClosed (1), EngineNotInitialised (2048), EngineNotRunning (16), EngineRunning (8), None (0), RootMonikerNotSet (64), RootMonikerSet (32), RootNamespaceSet (128), SiteNotSet (512), SiteSet (256), SupportForDebug (2) """
        ...

    def Preconditions(self, *args): #cannot find CLR method
        """ Preconditions(self: BaseVsaEngine, flags: Pre) """
        ...

    def ResetCompiledState(self, *args): #cannot find CLR method
        """ ResetCompiledState(self: BaseVsaEngine) """
        ...

    def SetCustomOption(self, *args): #cannot find CLR method
        """ SetCustomOption(self: BaseVsaEngine, name: str, value: object) """
        ...

    def ValidateRootMoniker(self, *args): #cannot find CLR method
        """ ValidateRootMoniker(self: BaseVsaEngine, rootMoniker: str) """
        ...

    applicationPath = ...
    assemblyVersion = ...
    compiledRootNamespace = ...
    engineMoniker = ...
    engineName = ...
    engineSite = ...
    errorLocale = ...
    executionEvidence = ...
    failedCompilation = ...
    genDebugInfo = ...
    haveCompiledState = ...
    isClosed = ...
    isDebugInfoSupported = ...
    isEngineCompiled = ...
    isEngineDirty = ...
    isEngineInitialized = ...
    isEngineRunning = ...
    loadedAssembly = ...
    nameTable: Hashtable = ...
    rootNamespace = ...
    scriptLanguage = ...
    startupClass = ...
    startupInstance = ...
    vsaItems = ...


class BaseVsaSite(IJSVsaSite): # skipped bases: <type 'object'>
    """ BaseVsaSite() """
    @property
    def Assembly(self) -> Array:
        """ Get: Assembly(self: BaseVsaSite) -> Array[Byte] """
        ...

    @property
    def DebugInfo(self) -> Array:
        """ Get: DebugInfo(self: BaseVsaSite) -> Array[Byte] """
        ...



class BaseVsaStartup: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def SetSite(self, site:IJSVsaSite): # -> 
        """ SetSite(self: BaseVsaStartup, site: IJSVsaSite) """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: BaseVsaStartup) """
        ...

    def Startup(self): # -> 
        """ Startup(self: BaseVsaStartup) """
        ...

    site = ...


class IJSVsaItem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IJSVsaItem) -> bool """
        ...

    @property
    def ItemType(self) -> JSVsaItemType:
        """ Get: ItemType(self: IJSVsaItem) -> JSVsaItemType """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IJSVsaItem) -> str
        Set: Name(self: IJSVsaItem) = value
        """
        ...


    def GetOption(self, name:str) -> object:
        """ GetOption(self: IJSVsaItem, name: str) -> object """
        ...

    def SetOption(self, name:str, value:object): # -> 
        """ SetOption(self: IJSVsaItem, name: str, value: object) """
        ...


class IJSVsaCodeItem(IJSVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodeDOM(self) -> CodeObject:
        """ Get: CodeDOM(self: IJSVsaCodeItem) -> CodeObject """
        ...

    @property
    def SourceText(self) -> str:
        """
        Get: SourceText(self: IJSVsaCodeItem) -> str
        Set: SourceText(self: IJSVsaCodeItem) = value
        """
        ...


    def AddEventSource(self, eventSourceName:str, eventSourceType:str): # -> 
        """ AddEventSource(self: IJSVsaCodeItem, eventSourceName: str, eventSourceType: str) """
        ...

    def AppendSourceText(self, text:str): # -> 
        """ AppendSourceText(self: IJSVsaCodeItem, text: str) """
        ...

    def RemoveEventSource(self, eventSourceName:str): # -> 
        """ RemoveEventSource(self: IJSVsaCodeItem, eventSourceName: str) """
        ...


class IJSVsaEngine: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: IJSVsaEngine) -> Assembly """
        ...

    @property
    def Evidence(self) -> Evidence:
        """
        Get: Evidence(self: IJSVsaEngine) -> Evidence
        Set: Evidence(self: IJSVsaEngine) = value
        """
        ...

    @property
    def GenerateDebugInfo(self) -> bool:
        """
        Get: GenerateDebugInfo(self: IJSVsaEngine) -> bool
        Set: GenerateDebugInfo(self: IJSVsaEngine) = value
        """
        ...

    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: IJSVsaEngine) -> bool """
        ...

    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IJSVsaEngine) -> bool """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: IJSVsaEngine) -> bool """
        ...

    @property
    def Items(self) -> IJSVsaItems:
        """ Get: Items(self: IJSVsaEngine) -> IJSVsaItems """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: IJSVsaEngine) -> str """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: IJSVsaEngine) -> int
        Set: LCID(self: IJSVsaEngine) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IJSVsaEngine) -> str
        Set: Name(self: IJSVsaEngine) = value
        """
        ...

    @property
    def RootMoniker(self) -> str:
        """
        Get: RootMoniker(self: IJSVsaEngine) -> str
        Set: RootMoniker(self: IJSVsaEngine) = value
        """
        ...

    @property
    def RootNamespace(self) -> str:
        """
        Get: RootNamespace(self: IJSVsaEngine) -> str
        Set: RootNamespace(self: IJSVsaEngine) = value
        """
        ...

    @property
    def Site(self) -> IJSVsaSite:
        """
        Get: Site(self: IJSVsaEngine) -> IJSVsaSite
        Set: Site(self: IJSVsaEngine) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: IJSVsaEngine) -> str """
        ...


    def Close(self): # -> 
        """ Close(self: IJSVsaEngine) """
        ...

    def Compile(self) -> bool:
        """ Compile(self: IJSVsaEngine) -> bool """
        ...

    def GetOption(self, name:str) -> object:
        """ GetOption(self: IJSVsaEngine, name: str) -> object """
        ...

    def InitNew(self): # -> 
        """ InitNew(self: IJSVsaEngine) """
        ...

    def IsValidIdentifier(self, identifier:str) -> bool:
        """ IsValidIdentifier(self: IJSVsaEngine, identifier: str) -> bool """
        ...

    def LoadSourceState(self, site:IJSVsaPersistSite): # -> 
        """ LoadSourceState(self: IJSVsaEngine, site: IJSVsaPersistSite) """
        ...

    def Reset(self): # -> 
        """ Reset(self: IJSVsaEngine) """
        ...

    def RevokeCache(self): # -> 
        """ RevokeCache(self: IJSVsaEngine) """
        ...

    def Run(self): # -> 
        """ Run(self: IJSVsaEngine) """
        ...

    def SaveCompiledState(self, pe, pdb) -> Tuple_[Array, Array]:
        """ SaveCompiledState(self: IJSVsaEngine) -> (Array[Byte], Array[Byte]) """
        ...

    def SaveSourceState(self, site:IJSVsaPersistSite): # -> 
        """ SaveSourceState(self: IJSVsaEngine, site: IJSVsaPersistSite) """
        ...

    def SetOption(self, name:str, value:object): # -> 
        """ SetOption(self: IJSVsaEngine, name: str, value: object) """
        ...


class IJSVsaError: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: IJSVsaError) -> str """
        ...

    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: IJSVsaError) -> int """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: IJSVsaError) -> int """
        ...

    @property
    def LineText(self) -> str:
        """ Get: LineText(self: IJSVsaError) -> str """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: IJSVsaError) -> int """
        ...

    @property
    def Severity(self) -> int:
        """ Get: Severity(self: IJSVsaError) -> int """
        ...

    @property
    def SourceItem(self) -> IJSVsaItem:
        """ Get: SourceItem(self: IJSVsaError) -> IJSVsaItem """
        ...

    @property
    def SourceMoniker(self) -> str:
        """ Get: SourceMoniker(self: IJSVsaError) -> str """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: IJSVsaError) -> int """
        ...



class IJSVsaGlobalItem(IJSVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExposeMembers(self) -> bool:
        """
        Get: ExposeMembers(self: IJSVsaGlobalItem) -> bool
        Set: ExposeMembers(self: IJSVsaGlobalItem) = value
        """
        ...

    @property
    def TypeString(self): # -> 
        """ Set: TypeString(self: IJSVsaGlobalItem) = value """
        ...



class IJSVsaItems(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IJSVsaItems) -> int """
        ...


    def CreateItem(self, name:str, itemType:JSVsaItemType, itemFlag:JSVsaItemFlag) -> IJSVsaItem:
        """ CreateItem(self: IJSVsaItems, name: str, itemType: JSVsaItemType, itemFlag: JSVsaItemFlag) -> IJSVsaItem """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: IJSVsaItems, name: str)Remove(self: IJSVsaItems, index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class IJSVsaPersistSite: # skipped bases: <type 'object'>
    """ no doc """
    def LoadElement(self, name:str) -> str:
        """ LoadElement(self: IJSVsaPersistSite, name: str) -> str """
        ...

    def SaveElement(self, name:str, source:str): # -> 
        """ SaveElement(self: IJSVsaPersistSite, name: str, source: str) """
        ...


class IJSVsaReferenceItem(IJSVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: IJSVsaReferenceItem) -> str
        Set: AssemblyName(self: IJSVsaReferenceItem) = value
        """
        ...



class IJSVsaSite: # skipped bases: <type 'object'>
    """ no doc """
    def GetCompiledState(self, pe, debugInfo) -> Tuple_[Array, Array]:
        """ GetCompiledState(self: IJSVsaSite) -> (Array[Byte], Array[Byte]) """
        ...

    def GetEventSourceInstance(self, itemName:str, eventSourceName:str) -> object:
        """ GetEventSourceInstance(self: IJSVsaSite, itemName: str, eventSourceName: str) -> object """
        ...

    def GetGlobalInstance(self, name:str) -> object:
        """ GetGlobalInstance(self: IJSVsaSite, name: str) -> object """
        ...

    def Notify(self, notify:str, info:object): # -> 
        """ Notify(self: IJSVsaSite, notify: str, info: object) """
        ...

    def OnCompilerError(self, error:IJSVsaError) -> bool:
        """ OnCompilerError(self: IJSVsaSite, error: IJSVsaError) -> bool """
        ...


class JSVsaError(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JSVsaError, values: AppDomainCannotBeSet (-2146226176), AppDomainInvalid (-2146226175), ApplicationBaseCannotBeSet (-2146226174), ApplicationBaseInvalid (-2146226173), AssemblyExpected (-2146226172), AssemblyNameInvalid (-2146226171), BadAssembly (-2146226170), BrowserNotExist (-2146226115), CachedAssemblyInvalid (-2146226169), CallbackUnexpected (-2146226168), CannotAttachToWebServer (-2146226100), CodeDOMNotAvailable (-2146226167), CompiledStateNotFound (-2146226166), DebuggeeNotStarted (-2146226114), DebugInfoNotSupported (-2146226165), ElementNameInvalid (-2146226164), ElementNotFound (-2146226163), EngineBusy (-2146226162), EngineCannotClose (-2146226161), EngineCannotReset (-2146226160), EngineClosed (-2146226159), EngineEmpty (-2146226159), EngineInitialized (-2146226157), EngineNameInUse (-2146226156), EngineNameInvalid (-2146226113), EngineNameNotSet (-2146226099), EngineNotCompiled (-2146226155), EngineNotExist (-2146226112), EngineNotInitialized (-2146226154), EngineNotRunning (-2146226153), EngineRunning (-2146226152), EventSourceInvalid (-2146226151), EventSourceNameInUse (-2146226150), EventSourceNameInvalid (-2146226149), EventSourceNotFound (-2146226148), EventSourceTypeInvalid (-2146226147), FileFormatUnsupported (-2146226111), FileTypeUnknown (-2146226110), GetCompiledStateFailed (-2146226146), GlobalInstanceInvalid (-2146226145), GlobalInstanceTypeInvalid (-2146226144), InternalCompilerError (-2146226143), ItemCannotBeRemoved (-2146226142), ItemCannotBeRenamed (-2146226109), ItemFlagNotSupported (-2146226141), ItemNameInUse (-2146226140), ItemNameInvalid (-2146226139), ItemNotFound (-2146226138), ItemTypeNotSupported (-2146226137), LCIDNotSupported (-2146226136), LoadElementFailed (-2146226135), MissingPdb (-2146226102), MissingSource (-2146226108), NameTooLong (-2146226106), NotClientSideAndNoUrl (-2146226101), NotificationInvalid (-2146226134), NotInitCompleted (-2146226107), OptionInvalid (-2146226133), OptionNotSupported (-2146226132), ProcNameInUse (-2146226105), ProcNameInvalid (-2146226104), RevokeFailed (-2146226131), RootMonikerAlreadySet (-2146226130), RootMonikerInUse (-2146226129), RootMonikerInvalid (-2146226128), RootMonikerNotSet (-2146226127), RootMonikerProtocolInvalid (-2146226126), RootNamespaceInvalid (-2146226125), RootNamespaceNotSet (-2146226124), SaveCompiledStateFailed (-2146226123), SaveElementFailed (-2146226122), SiteAlreadySet (-2146226121), SiteInvalid (-2146226120), SiteNotSet (-2146226119), SourceItemNotAvailable (-2146226118), SourceMonikerNotAvailable (-2146226117), UnknownError (-2146225921), URLInvalid (-2146226116), VsaServerDown (-2146226103) """
    AppDomainCannotBeSet: JSVsaError = ...
    AppDomainInvalid: JSVsaError = ...
    ApplicationBaseCannotBeSet: JSVsaError = ...
    ApplicationBaseInvalid: JSVsaError = ...
    AssemblyExpected: JSVsaError = ...
    AssemblyNameInvalid: JSVsaError = ...
    BadAssembly: JSVsaError = ...
    BrowserNotExist: JSVsaError = ...
    CachedAssemblyInvalid: JSVsaError = ...
    CallbackUnexpected: JSVsaError = ...
    CannotAttachToWebServer: JSVsaError = ...
    CodeDOMNotAvailable: JSVsaError = ...
    CompiledStateNotFound: JSVsaError = ...
    DebuggeeNotStarted: JSVsaError = ...
    DebugInfoNotSupported: JSVsaError = ...
    ElementNameInvalid: JSVsaError = ...
    ElementNotFound: JSVsaError = ...
    EngineBusy: JSVsaError = ...
    EngineCannotClose: JSVsaError = ...
    EngineCannotReset: JSVsaError = ...
    EngineClosed: JSVsaError = ...
    EngineEmpty: JSVsaError = ...
    EngineInitialized: JSVsaError = ...
    EngineNameInUse: JSVsaError = ...
    EngineNameInvalid: JSVsaError = ...
    EngineNameNotSet: JSVsaError = ...
    EngineNotCompiled: JSVsaError = ...
    EngineNotExist: JSVsaError = ...
    EngineNotInitialized: JSVsaError = ...
    EngineNotRunning: JSVsaError = ...
    EngineRunning: JSVsaError = ...
    EventSourceInvalid: JSVsaError = ...
    EventSourceNameInUse: JSVsaError = ...
    EventSourceNameInvalid: JSVsaError = ...
    EventSourceNotFound: JSVsaError = ...
    EventSourceTypeInvalid: JSVsaError = ...
    FileFormatUnsupported: JSVsaError = ...
    FileTypeUnknown: JSVsaError = ...
    GetCompiledStateFailed: JSVsaError = ...
    GlobalInstanceInvalid: JSVsaError = ...
    GlobalInstanceTypeInvalid: JSVsaError = ...
    InternalCompilerError: JSVsaError = ...
    ItemCannotBeRemoved: JSVsaError = ...
    ItemCannotBeRenamed: JSVsaError = ...
    ItemFlagNotSupported: JSVsaError = ...
    ItemNameInUse: JSVsaError = ...
    ItemNameInvalid: JSVsaError = ...
    ItemNotFound: JSVsaError = ...
    ItemTypeNotSupported: JSVsaError = ...
    LCIDNotSupported: JSVsaError = ...
    LoadElementFailed: JSVsaError = ...
    MissingPdb: JSVsaError = ...
    MissingSource: JSVsaError = ...
    NameTooLong: JSVsaError = ...
    NotClientSideAndNoUrl: JSVsaError = ...
    NotificationInvalid: JSVsaError = ...
    NotInitCompleted: JSVsaError = ...
    OptionInvalid: JSVsaError = ...
    OptionNotSupported: JSVsaError = ...
    ProcNameInUse: JSVsaError = ...
    ProcNameInvalid: JSVsaError = ...
    RevokeFailed: JSVsaError = ...
    RootMonikerAlreadySet: JSVsaError = ...
    RootMonikerInUse: JSVsaError = ...
    RootMonikerInvalid: JSVsaError = ...
    RootMonikerNotSet: JSVsaError = ...
    RootMonikerProtocolInvalid: JSVsaError = ...
    RootNamespaceInvalid: JSVsaError = ...
    RootNamespaceNotSet: JSVsaError = ...
    SaveCompiledStateFailed: JSVsaError = ...
    SaveElementFailed: JSVsaError = ...
    SiteAlreadySet: JSVsaError = ...
    SiteInvalid: JSVsaError = ...
    SiteNotSet: JSVsaError = ...
    SourceItemNotAvailable: JSVsaError = ...
    SourceMonikerNotAvailable: JSVsaError = ...
    UnknownError: JSVsaError = ...
    URLInvalid: JSVsaError = ...
    value__ = ...
    VsaServerDown: JSVsaError = ...


class JSVsaException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    JSVsaException()
    JSVsaException(message: str)
    JSVsaException(message: str, innerException: Exception)
    JSVsaException(info: SerializationInfo, context: StreamingContext)
    JSVsaException(error: JSVsaError)
    JSVsaException(error: JSVsaError, message: str)
    JSVsaException(error: JSVsaError, message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: JSVsaException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class JSVsaItemFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JSVsaItemFlag, values: Class (2), Module (1), None (0) """
    Class: JSVsaItemFlag = ...
    Module: JSVsaItemFlag = ...
    value__ = ...


class JSVsaItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JSVsaItemType, values: AppGlobal (1), Code (2), Reference (0) """
    AppGlobal: JSVsaItemType = ...
    Code: JSVsaItemType = ...
    Reference: JSVsaItemType = ...
    value__ = ...


class ResInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResInfo(filename: str, name: str, isPublic: bool, isLinked: bool)
    ResInfo(resinfo: str, isLinked: bool)
    """
    filename = ...
    fullpath = ...
    isLinked = ...
    isPublic = ...
    name = ...


class VsaEngine(IRedirectOutput, IEngine2, BaseVsaEngine): # skipped bases: <type 'IJSVsaEngine'>, <type 'object'>
    """
    VsaEngine()
    VsaEngine(fast: bool)
    """
    @property
    def LenientGlobalObject(self) -> LenientGlobalObject:
        """ Get: LenientGlobalObject(self: VsaEngine) -> LenientGlobalObject """
        ...


    @staticmethod
    def CreateEngine() -> VsaEngine:
        """ CreateEngine() -> VsaEngine """
        ...

    @staticmethod
    def CreateEngineAndGetGlobalScope(fast:bool, assemblyNames:Array) -> GlobalScope:
        """ CreateEngineAndGetGlobalScope(fast: bool, assemblyNames: Array[str]) -> GlobalScope """
        ...

    @staticmethod
    def CreateEngineAndGetGlobalScopeWithType(fast:bool, assemblyNames:Array, callingTypeHandle:RuntimeTypeHandle) -> GlobalScope:
        """ CreateEngineAndGetGlobalScopeWithType(fast: bool, assemblyNames: Array[str], callingTypeHandle: RuntimeTypeHandle) -> GlobalScope """
        ...

    @staticmethod
    def CreateEngineAndGetGlobalScopeWithTypeAndRootNamespace(fast:bool, assemblyNames:Array, callingTypeHandle:RuntimeTypeHandle, rootNamespace:str) -> GlobalScope:
        """ CreateEngineAndGetGlobalScopeWithTypeAndRootNamespace(fast: bool, assemblyNames: Array[str], callingTypeHandle: RuntimeTypeHandle, rootNamespace: str) -> GlobalScope """
        ...

    @staticmethod
    def CreateEngineWithType(callingTypeHandle:RuntimeTypeHandle) -> VsaEngine:
        """ CreateEngineWithType(callingTypeHandle: RuntimeTypeHandle) -> VsaEngine """
        ...

    def GetItem(self, itemName:str) -> IJSVsaItem:
        """ GetItem(self: VsaEngine, itemName: str) -> IJSVsaItem """
        ...

    def GetItemAtIndex(self, index:int) -> IJSVsaItem:
        """ GetItemAtIndex(self: VsaEngine, index: int) -> IJSVsaItem """
        ...

    def GetItemCount(self) -> int:
        """ GetItemCount(self: VsaEngine) -> int """
        ...

    def GetMainScope(self) -> GlobalScope:
        """ GetMainScope(self: VsaEngine) -> GlobalScope """
        ...

    def GetOriginalArrayConstructor(self) -> ArrayConstructor:
        """ GetOriginalArrayConstructor(self: VsaEngine) -> ArrayConstructor """
        ...

    def GetOriginalObjectConstructor(self) -> ObjectConstructor:
        """ GetOriginalObjectConstructor(self: VsaEngine) -> ObjectConstructor """
        ...

    def GetOriginalRegExpConstructor(self) -> RegExpConstructor:
        """ GetOriginalRegExpConstructor(self: VsaEngine) -> RegExpConstructor """
        ...

    def PopScriptObject(self) -> ScriptObject:
        """ PopScriptObject(self: VsaEngine) -> ScriptObject """
        ...

    def PushScriptObject(self, obj:ScriptObject): # -> 
        """ PushScriptObject(self: VsaEngine, obj: ScriptObject) """
        ...

    def ScriptObjectStackTop(self) -> ScriptObject:
        """ ScriptObjectStackTop(self: VsaEngine) -> ScriptObject """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, fast:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fast: bool)
        """
        ...

    applicationPath = ...
    assemblyVersion = ...
    compiledRootNamespace = ...
    engineMoniker = ...
    engineName = ...
    engineSite = ...
    errorLocale = ...
    executionEvidence = ...
    failedCompilation = ...
    genDebugInfo = ...
    haveCompiledState = ...
    isClosed = ...
    isDebugInfoSupported = ...
    isEngineCompiled = ...
    isEngineDirty = ...
    isEngineInitialized = ...
    isEngineRunning = ...
    loadedAssembly = ...
    rootNamespace = ...
    scriptLanguage = ...
    startupClass = ...
    startupInstance = ...
    vsaItems = ...


