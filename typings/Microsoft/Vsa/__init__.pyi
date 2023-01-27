# encoding: utf-8
# module Microsoft.Vsa calls itself Vsa
# from Microsoft.Vsa, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, Microsoft.Vsa.Vb.CodeDOMProcessor, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum

from System.CodeDom import CodeObject

from System.Collections import IEnumerable

from System.Reflection import Assembly

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Policy import Evidence

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class IVsaItem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IVsaItem) -> bool """
        ...

    @property
    def ItemType(self) -> VsaItemType:
        """ Get: ItemType(self: IVsaItem) -> VsaItemType """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IVsaItem) -> str
        Set: Name(self: IVsaItem) = value
        """
        ...


    def GetOption(self, name:str) -> object:
        """ GetOption(self: IVsaItem, name: str) -> object """
        ...

    def SetOption(self, name:str, value:object): # -> 
        """ SetOption(self: IVsaItem, name: str, value: object) """
        ...


class IVsaCodeItem(IVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodeDOM(self) -> CodeObject:
        """ Get: CodeDOM(self: IVsaCodeItem) -> CodeObject """
        ...

    @property
    def SourceText(self) -> str:
        """
        Get: SourceText(self: IVsaCodeItem) -> str
        Set: SourceText(self: IVsaCodeItem) = value
        """
        ...


    def AddEventSource(self, eventSourceName:str, eventSourceType:str): # -> 
        """ AddEventSource(self: IVsaCodeItem, eventSourceName: str, eventSourceType: str) """
        ...

    def AppendSourceText(self, text:str): # -> 
        """ AppendSourceText(self: IVsaCodeItem, text: str) """
        ...

    def RemoveEventSource(self, eventSourceName:str): # -> 
        """ RemoveEventSource(self: IVsaCodeItem, eventSourceName: str) """
        ...


class IVsaDTCodeItem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanDelete(self) -> bool:
        """
        Get: CanDelete(self: IVsaDTCodeItem) -> bool
        Set: CanDelete(self: IVsaDTCodeItem) = value
        """
        ...

    @property
    def CanMove(self) -> bool:
        """
        Get: CanMove(self: IVsaDTCodeItem) -> bool
        Set: CanMove(self: IVsaDTCodeItem) = value
        """
        ...

    @property
    def CanRename(self) -> bool:
        """
        Get: CanRename(self: IVsaDTCodeItem) -> bool
        Set: CanRename(self: IVsaDTCodeItem) = value
        """
        ...

    @property
    def Hidden(self) -> bool:
        """
        Get: Hidden(self: IVsaDTCodeItem) -> bool
        Set: Hidden(self: IVsaDTCodeItem) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: IVsaDTCodeItem) -> bool
        Set: ReadOnly(self: IVsaDTCodeItem) = value
        """
        ...



class IVsaDTEngine: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TargetURL(self) -> str:
        """
        Get: TargetURL(self: IVsaDTEngine) -> str
        Set: TargetURL(self: IVsaDTEngine) = value
        """
        ...


    def AttachDebugger(self, isAttach:bool): # -> 
        """ AttachDebugger(self: IVsaDTEngine, isAttach: bool) """
        ...

    def GetIDE(self) -> IVsaIDE:
        """ GetIDE(self: IVsaDTEngine) -> IVsaIDE """
        ...

    def InitCompleted(self): # -> 
        """ InitCompleted(self: IVsaDTEngine) """
        ...


class IVsaEngine: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: IVsaEngine) -> Assembly """
        ...

    @property
    def Evidence(self) -> Evidence:
        """
        Get: Evidence(self: IVsaEngine) -> Evidence
        Set: Evidence(self: IVsaEngine) = value
        """
        ...

    @property
    def GenerateDebugInfo(self) -> bool:
        """
        Get: GenerateDebugInfo(self: IVsaEngine) -> bool
        Set: GenerateDebugInfo(self: IVsaEngine) = value
        """
        ...

    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: IVsaEngine) -> bool """
        ...

    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IVsaEngine) -> bool """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: IVsaEngine) -> bool """
        ...

    @property
    def Items(self) -> IVsaItems:
        """ Get: Items(self: IVsaEngine) -> IVsaItems """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: IVsaEngine) -> str """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: IVsaEngine) -> int
        Set: LCID(self: IVsaEngine) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IVsaEngine) -> str
        Set: Name(self: IVsaEngine) = value
        """
        ...

    @property
    def RootMoniker(self) -> str:
        """
        Get: RootMoniker(self: IVsaEngine) -> str
        Set: RootMoniker(self: IVsaEngine) = value
        """
        ...

    @property
    def RootNamespace(self) -> str:
        """
        Get: RootNamespace(self: IVsaEngine) -> str
        Set: RootNamespace(self: IVsaEngine) = value
        """
        ...

    @property
    def Site(self) -> IVsaSite:
        """
        Get: Site(self: IVsaEngine) -> IVsaSite
        Set: Site(self: IVsaEngine) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: IVsaEngine) -> str """
        ...


    def Close(self): # -> 
        """ Close(self: IVsaEngine) """
        ...

    def Compile(self) -> bool:
        """ Compile(self: IVsaEngine) -> bool """
        ...

    def GetOption(self, name:str) -> object:
        """ GetOption(self: IVsaEngine, name: str) -> object """
        ...

    def InitNew(self): # -> 
        """ InitNew(self: IVsaEngine) """
        ...

    def IsValidIdentifier(self, identifier:str) -> bool:
        """ IsValidIdentifier(self: IVsaEngine, identifier: str) -> bool """
        ...

    def LoadSourceState(self, site:IVsaPersistSite): # -> 
        """ LoadSourceState(self: IVsaEngine, site: IVsaPersistSite) """
        ...

    def Reset(self): # -> 
        """ Reset(self: IVsaEngine) """
        ...

    def RevokeCache(self): # -> 
        """ RevokeCache(self: IVsaEngine) """
        ...

    def Run(self): # -> 
        """ Run(self: IVsaEngine) """
        ...

    def SaveCompiledState(self, pe, pdb) -> Tuple_[Array, Array]:
        """ SaveCompiledState(self: IVsaEngine) -> (Array[Byte], Array[Byte]) """
        ...

    def SaveSourceState(self, site:IVsaPersistSite): # -> 
        """ SaveSourceState(self: IVsaEngine, site: IVsaPersistSite) """
        ...

    def SetOption(self, name:str, value:object): # -> 
        """ SetOption(self: IVsaEngine, name: str, value: object) """
        ...


class IVsaError: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: IVsaError) -> str """
        ...

    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: IVsaError) -> int """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: IVsaError) -> int """
        ...

    @property
    def LineText(self) -> str:
        """ Get: LineText(self: IVsaError) -> str """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: IVsaError) -> int """
        ...

    @property
    def Severity(self) -> int:
        """ Get: Severity(self: IVsaError) -> int """
        ...

    @property
    def SourceItem(self) -> IVsaItem:
        """ Get: SourceItem(self: IVsaError) -> IVsaItem """
        ...

    @property
    def SourceMoniker(self) -> str:
        """ Get: SourceMoniker(self: IVsaError) -> str """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: IVsaError) -> int """
        ...



class IVsaGlobalItem(IVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExposeMembers(self) -> bool:
        """
        Get: ExposeMembers(self: IVsaGlobalItem) -> bool
        Set: ExposeMembers(self: IVsaGlobalItem) = value
        """
        ...

    @property
    def TypeString(self): # -> 
        """ Set: TypeString(self: IVsaGlobalItem) = value """
        ...



class IVsaIDE: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultSearchPath(self) -> str:
        """
        Get: DefaultSearchPath(self: IVsaIDE) -> str
        Set: DefaultSearchPath(self: IVsaIDE) = value
        """
        ...

    @property
    def ExtensibilityObject(self) -> object:
        """ Get: ExtensibilityObject(self: IVsaIDE) -> object """
        ...

    @property
    def IDEMode(self) -> VsaIDEMode:
        """ Get: IDEMode(self: IVsaIDE) -> VsaIDEMode """
        ...

    @property
    def Site(self) -> IVsaIDESite:
        """
        Get: Site(self: IVsaIDE) -> IVsaIDESite
        Set: Site(self: IVsaIDE) = value
        """
        ...


    def EnableMainWindow(self, isEnable:bool): # -> 
        """ EnableMainWindow(self: IVsaIDE, isEnable: bool) """
        ...

    def ShowIDE(self, showOrHide:bool): # -> 
        """ ShowIDE(self: IVsaIDE, showOrHide: bool) """
        ...


class IVsaIDESite: # skipped bases: <type 'object'>
    """ no doc """
    def Notify(self, notify:str, optional:object): # -> 
        """ Notify(self: IVsaIDESite, notify: str, optional: object) """
        ...


class IVsaItems(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IVsaItems) -> int """
        ...


    def CreateItem(self, name:str, itemType:VsaItemType, itemFlag:VsaItemFlag) -> IVsaItem:
        """ CreateItem(self: IVsaItems, name: str, itemType: VsaItemType, itemFlag: VsaItemFlag) -> IVsaItem """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: IVsaItems, name: str)Remove(self: IVsaItems, index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class IVsaPersistSite: # skipped bases: <type 'object'>
    """ no doc """
    def LoadElement(self, name:str) -> str:
        """ LoadElement(self: IVsaPersistSite, name: str) -> str """
        ...

    def SaveElement(self, name:str, source:str): # -> 
        """ SaveElement(self: IVsaPersistSite, name: str, source: str) """
        ...


class IVsaReferenceItem(IVsaItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: IVsaReferenceItem) -> str
        Set: AssemblyName(self: IVsaReferenceItem) = value
        """
        ...



class IVsaSite: # skipped bases: <type 'object'>
    """ no doc """
    def GetCompiledState(self, pe, debugInfo) -> Tuple_[Array, Array]:
        """ GetCompiledState(self: IVsaSite) -> (Array[Byte], Array[Byte]) """
        ...

    def GetEventSourceInstance(self, itemName:str, eventSourceName:str) -> object:
        """ GetEventSourceInstance(self: IVsaSite, itemName: str, eventSourceName: str) -> object """
        ...

    def GetGlobalInstance(self, name:str) -> object:
        """ GetGlobalInstance(self: IVsaSite, name: str) -> object """
        ...

    def Notify(self, notify:str, info:object): # -> 
        """ Notify(self: IVsaSite, notify: str, info: object) """
        ...

    def OnCompilerError(self, error:IVsaError) -> bool:
        """ OnCompilerError(self: IVsaSite, error: IVsaError) -> bool """
        ...


class VsaError(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VsaError, values: AppDomainCannotBeSet (-2146226176), AppDomainInvalid (-2146226175), ApplicationBaseCannotBeSet (-2146226174), ApplicationBaseInvalid (-2146226173), AssemblyExpected (-2146226172), AssemblyNameInvalid (-2146226171), BadAssembly (-2146226170), BrowserNotExist (-2146226115), CachedAssemblyInvalid (-2146226169), CallbackUnexpected (-2146226168), CannotAttachToWebServer (-2146226100), CodeDOMNotAvailable (-2146226167), CompiledStateNotFound (-2146226166), DebuggeeNotStarted (-2146226114), DebugInfoNotSupported (-2146226165), ElementNameInvalid (-2146226164), ElementNotFound (-2146226163), EngineBusy (-2146226162), EngineCannotClose (-2146226161), EngineCannotReset (-2146226160), EngineClosed (-2146226159), EngineEmpty (-2146226159), EngineInitialized (-2146226157), EngineNameInUse (-2146226156), EngineNameInvalid (-2146226113), EngineNameNotSet (-2146226099), EngineNotCompiled (-2146226155), EngineNotExist (-2146226112), EngineNotInitialized (-2146226154), EngineNotRunning (-2146226153), EngineRunning (-2146226152), EventSourceInvalid (-2146226151), EventSourceNameInUse (-2146226150), EventSourceNameInvalid (-2146226149), EventSourceNotFound (-2146226148), EventSourceTypeInvalid (-2146226147), FileFormatUnsupported (-2146226111), FileTypeUnknown (-2146226110), GetCompiledStateFailed (-2146226146), GlobalInstanceInvalid (-2146226145), GlobalInstanceTypeInvalid (-2146226144), InternalCompilerError (-2146226143), ItemCannotBeRemoved (-2146226142), ItemCannotBeRenamed (-2146226109), ItemFlagNotSupported (-2146226141), ItemNameInUse (-2146226140), ItemNameInvalid (-2146226139), ItemNotFound (-2146226138), ItemTypeNotSupported (-2146226137), LCIDNotSupported (-2146226136), LoadElementFailed (-2146226135), MissingPdb (-2146226102), MissingSource (-2146226108), NameTooLong (-2146226106), NotClientSideAndNoUrl (-2146226101), NotificationInvalid (-2146226134), NotInitCompleted (-2146226107), OptionInvalid (-2146226133), OptionNotSupported (-2146226132), ProcNameInUse (-2146226105), ProcNameInvalid (-2146226104), RevokeFailed (-2146226131), RootMonikerAlreadySet (-2146226130), RootMonikerInUse (-2146226129), RootMonikerInvalid (-2146226128), RootMonikerNotSet (-2146226127), RootMonikerProtocolInvalid (-2146226126), RootNamespaceInvalid (-2146226125), RootNamespaceNotSet (-2146226124), SaveCompiledStateFailed (-2146226123), SaveElementFailed (-2146226122), SiteAlreadySet (-2146226121), SiteInvalid (-2146226120), SiteNotSet (-2146226119), SourceItemNotAvailable (-2146226118), SourceMonikerNotAvailable (-2146226117), UnknownError (-2146225921), URLInvalid (-2146226116), VsaServerDown (-2146226103) """
    AppDomainCannotBeSet: VsaError = ...
    AppDomainInvalid: VsaError = ...
    ApplicationBaseCannotBeSet: VsaError = ...
    ApplicationBaseInvalid: VsaError = ...
    AssemblyExpected: VsaError = ...
    AssemblyNameInvalid: VsaError = ...
    BadAssembly: VsaError = ...
    BrowserNotExist: VsaError = ...
    CachedAssemblyInvalid: VsaError = ...
    CallbackUnexpected: VsaError = ...
    CannotAttachToWebServer: VsaError = ...
    CodeDOMNotAvailable: VsaError = ...
    CompiledStateNotFound: VsaError = ...
    DebuggeeNotStarted: VsaError = ...
    DebugInfoNotSupported: VsaError = ...
    ElementNameInvalid: VsaError = ...
    ElementNotFound: VsaError = ...
    EngineBusy: VsaError = ...
    EngineCannotClose: VsaError = ...
    EngineCannotReset: VsaError = ...
    EngineClosed: VsaError = ...
    EngineEmpty: VsaError = ...
    EngineInitialized: VsaError = ...
    EngineNameInUse: VsaError = ...
    EngineNameInvalid: VsaError = ...
    EngineNameNotSet: VsaError = ...
    EngineNotCompiled: VsaError = ...
    EngineNotExist: VsaError = ...
    EngineNotInitialized: VsaError = ...
    EngineNotRunning: VsaError = ...
    EngineRunning: VsaError = ...
    EventSourceInvalid: VsaError = ...
    EventSourceNameInUse: VsaError = ...
    EventSourceNameInvalid: VsaError = ...
    EventSourceNotFound: VsaError = ...
    EventSourceTypeInvalid: VsaError = ...
    FileFormatUnsupported: VsaError = ...
    FileTypeUnknown: VsaError = ...
    GetCompiledStateFailed: VsaError = ...
    GlobalInstanceInvalid: VsaError = ...
    GlobalInstanceTypeInvalid: VsaError = ...
    InternalCompilerError: VsaError = ...
    ItemCannotBeRemoved: VsaError = ...
    ItemCannotBeRenamed: VsaError = ...
    ItemFlagNotSupported: VsaError = ...
    ItemNameInUse: VsaError = ...
    ItemNameInvalid: VsaError = ...
    ItemNotFound: VsaError = ...
    ItemTypeNotSupported: VsaError = ...
    LCIDNotSupported: VsaError = ...
    LoadElementFailed: VsaError = ...
    MissingPdb: VsaError = ...
    MissingSource: VsaError = ...
    NameTooLong: VsaError = ...
    NotClientSideAndNoUrl: VsaError = ...
    NotificationInvalid: VsaError = ...
    NotInitCompleted: VsaError = ...
    OptionInvalid: VsaError = ...
    OptionNotSupported: VsaError = ...
    ProcNameInUse: VsaError = ...
    ProcNameInvalid: VsaError = ...
    RevokeFailed: VsaError = ...
    RootMonikerAlreadySet: VsaError = ...
    RootMonikerInUse: VsaError = ...
    RootMonikerInvalid: VsaError = ...
    RootMonikerNotSet: VsaError = ...
    RootMonikerProtocolInvalid: VsaError = ...
    RootNamespaceInvalid: VsaError = ...
    RootNamespaceNotSet: VsaError = ...
    SaveCompiledStateFailed: VsaError = ...
    SaveElementFailed: VsaError = ...
    SiteAlreadySet: VsaError = ...
    SiteInvalid: VsaError = ...
    SiteNotSet: VsaError = ...
    SourceItemNotAvailable: VsaError = ...
    SourceMonikerNotAvailable: VsaError = ...
    UnknownError: VsaError = ...
    URLInvalid: VsaError = ...
    value__ = ...
    VsaServerDown: VsaError = ...


class VsaException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    VsaException()
    VsaException(message: str)
    VsaException(message: str, innerException: Exception)
    VsaException(info: SerializationInfo, context: StreamingContext)
    VsaException(error: VsaError)
    VsaException(error: VsaError, message: str)
    VsaException(error: VsaError, message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: VsaException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class VsaIDEMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VsaIDEMode, values: Break (0), Design (1), Run (2) """
    Break: VsaIDEMode = ...
    Design: VsaIDEMode = ...
    Run: VsaIDEMode = ...
    value__ = ...


class VsaItemFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VsaItemFlag, values: Class (2), Module (1), None (0) """
    Class: VsaItemFlag = ...
    Module: VsaItemFlag = ...
    value__ = ...


class VsaItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VsaItemType, values: AppGlobal (1), Code (2), Reference (0) """
    AppGlobal: VsaItemType = ...
    Code: VsaItemType = ...
    Reference: VsaItemType = ...
    value__ = ...


class VsaLoader(IVsaEngine): # skipped bases: <type 'object'>
    """ VsaLoader() """
    pass

class VsaModule(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ VsaModule(bIsVsaModule: bool) """
    @property
    def IsVsaModule(self) -> bool:
        """
        Get: IsVsaModule(self: VsaModule) -> bool
        Set: IsVsaModule(self: VsaModule) = value
        """
        ...


    def __new__(cls, bIsVsaModule:bool) -> Self:
        """ __new__(cls: type, bIsVsaModule: bool) """
        ...


# variables with complex values

