# encoding: utf-8
# module System.Web.SessionState calls itself SessionState
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    IntPtr, MulticastDelegate, TimeSpan)

from System.Collections import ICollection, IEnumerator, IList

from System.Collections.Specialized import NameObjectCollectionBase

from System.Configuration.Provider import ProviderBase

from System.IO import BinaryReader, BinaryWriter

from System.Runtime.Serialization import ISurrogateSelector

from System.Threading.Tasks import Task

from System.Web import (HttpApplication, HttpContext, HttpCookieMode, 
    HttpStaticObjectsCollection, IHttpModule)

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    KeysCollection, field#)
"""

# no functions
# classes

class HttpSessionState(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def CodePage(self) -> int:
        """
        Get: CodePage(self: HttpSessionState) -> int
        Set: CodePage(self: HttpSessionState) = value
        """
        ...

    @property
    def Contents(self) -> HttpSessionState:
        """ Get: Contents(self: HttpSessionState) -> HttpSessionState """
        ...

    @property
    def CookieMode(self) -> HttpCookieMode:
        """ Get: CookieMode(self: HttpSessionState) -> HttpCookieMode """
        ...

    @property
    def IsCookieless(self) -> bool:
        """ Get: IsCookieless(self: HttpSessionState) -> bool """
        ...

    @property
    def IsNewSession(self) -> bool:
        """ Get: IsNewSession(self: HttpSessionState) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HttpSessionState) -> bool """
        ...

    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: HttpSessionState) -> KeysCollection """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: HttpSessionState) -> int
        Set: LCID(self: HttpSessionState) = value
        """
        ...

    @property
    def Mode(self) -> SessionStateMode:
        """ Get: Mode(self: HttpSessionState) -> SessionStateMode """
        ...

    @property
    def SessionID(self) -> str:
        """ Get: SessionID(self: HttpSessionState) -> str """
        ...

    @property
    def StaticObjects(self) -> HttpStaticObjectsCollection:
        """ Get: StaticObjects(self: HttpSessionState) -> HttpStaticObjectsCollection """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: HttpSessionState) -> int
        Set: Timeout(self: HttpSessionState) = value
        """
        ...


    def Abandon(self): # -> 
        """ Abandon(self: HttpSessionState) """
        ...

    def Add(self, name:str, value:object): # -> 
        """ Add(self: HttpSessionState, name: str, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpSessionState) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpSessionState) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: HttpSessionState, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: HttpSessionState) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpSessionState, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpSessionStateContainer(IHttpSessionState): # skipped bases: <type 'object'>
    """ HttpSessionStateContainer(id: str, sessionItems: ISessionStateItemCollection, staticObjects: HttpStaticObjectsCollection, timeout: int, newSession: bool, cookieMode: HttpCookieMode, mode: SessionStateMode, isReadonly: bool) """
    @property
    def IsAbandoned(self) -> bool:
        """ Get: IsAbandoned(self: HttpSessionStateContainer) -> bool """
        ...



class IHttpSessionState: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodePage(self) -> int:
        """
        Get: CodePage(self: IHttpSessionState) -> int
        Set: CodePage(self: IHttpSessionState) = value
        """
        ...

    @property
    def CookieMode(self) -> HttpCookieMode:
        """ Get: CookieMode(self: IHttpSessionState) -> HttpCookieMode """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IHttpSessionState) -> int """
        ...

    @property
    def IsCookieless(self) -> bool:
        """ Get: IsCookieless(self: IHttpSessionState) -> bool """
        ...

    @property
    def IsNewSession(self) -> bool:
        """ Get: IsNewSession(self: IHttpSessionState) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IHttpSessionState) -> bool """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: IHttpSessionState) -> bool """
        ...

    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: IHttpSessionState) -> KeysCollection """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: IHttpSessionState) -> int
        Set: LCID(self: IHttpSessionState) = value
        """
        ...

    @property
    def Mode(self) -> SessionStateMode:
        """ Get: Mode(self: IHttpSessionState) -> SessionStateMode """
        ...

    @property
    def SessionID(self) -> str:
        """ Get: SessionID(self: IHttpSessionState) -> str """
        ...

    @property
    def StaticObjects(self) -> HttpStaticObjectsCollection:
        """ Get: StaticObjects(self: IHttpSessionState) -> HttpStaticObjectsCollection """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: IHttpSessionState) -> object """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: IHttpSessionState) -> int
        Set: Timeout(self: IHttpSessionState) = value
        """
        ...


    def Abandon(self): # -> 
        """ Abandon(self: IHttpSessionState) """
        ...

    def Add(self, name:str, value:object): # -> 
        """ Add(self: IHttpSessionState, name: str, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IHttpSessionState) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: IHttpSessionState, array: Array, index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: IHttpSessionState) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: IHttpSessionState, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: IHttpSessionState) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IHttpSessionState, index: int) """
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


class IPartialSessionState: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PartialSessionStateKeys(self) -> IList:
        """ Get: PartialSessionStateKeys(self: IPartialSessionState) -> IList[str] """
        ...



class IRequiresSessionState: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IReadOnlySessionState(IRequiresSessionState): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISessionIDManager: # skipped bases: <type 'object'>
    """ no doc """
    def CreateSessionID(self, context:HttpContext) -> str:
        """ CreateSessionID(self: ISessionIDManager, context: HttpContext) -> str """
        ...

    def GetSessionID(self, context:HttpContext) -> str:
        """ GetSessionID(self: ISessionIDManager, context: HttpContext) -> str """
        ...

    def Initialize(self): # -> 
        """ Initialize(self: ISessionIDManager) """
        ...

    def InitializeRequest(self, context, suppressAutoDetectRedirect, supportSessionIDReissue) -> Tuple_[bool, bool]:
        """ InitializeRequest(self: ISessionIDManager, context: HttpContext, suppressAutoDetectRedirect: bool) -> (bool, bool) """
        ...

    def RemoveSessionID(self, context:HttpContext): # -> 
        """ RemoveSessionID(self: ISessionIDManager, context: HttpContext) """
        ...

    def SaveSessionID(self, context, id, redirected, cookieAdded) -> Tuple_[bool, bool]:
        """ SaveSessionID(self: ISessionIDManager, context: HttpContext, id: str) -> (bool, bool) """
        ...

    def Validate(self, id:str) -> bool:
        """ Validate(self: ISessionIDManager, id: str) -> bool """
        ...


class ISessionStateItemCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Dirty(self) -> bool:
        """
        Get: Dirty(self: ISessionStateItemCollection) -> bool
        Set: Dirty(self: ISessionStateItemCollection) = value
        """
        ...

    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: ISessionStateItemCollection) -> KeysCollection """
        ...


    def Clear(self): # -> 
        """ Clear(self: ISessionStateItemCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ISessionStateItemCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ISessionStateItemCollection, index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ISessionStateModule(IHttpModule): # skipped bases: <type 'object'>
    """ no doc """
    def ReleaseSessionState(self, context:HttpContext): # -> 
        """ ReleaseSessionState(self: ISessionStateModule, context: HttpContext) """
        ...

    def ReleaseSessionStateAsync(self, context:HttpContext) -> Task:
        """ ReleaseSessionStateAsync(self: ISessionStateModule, context: HttpContext) -> Task """
        ...


class IStateRuntime: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessRequest(self, tracker, verb, uri, exclusive, *__args): # -> 
        """ ProcessRequest(self: IStateRuntime, tracker: IntPtr, verb: int, uri: str, exclusive: int, timeout: int, lockCookieExists: int, lockCookie: int, contentLength: int, content: IntPtr)ProcessRequest(self: IStateRuntime, tracker: IntPtr, verb: int, uri: str, exclusive: int, extraFlags: int, timeout: int, lockCookieExists: int, lockCookie: int, contentLength: int, content: IntPtr) """
        ...

    def StopProcessing(self): # -> 
        """ StopProcessing(self: IStateRuntime) """
        ...


class SessionIDManager(ISessionIDManager): # skipped bases: <type 'object'>
    """ SessionIDManager() """
    @property
    def SessionIDMaxLength(self) -> int:
        """ Get: SessionIDMaxLength() -> int """
        ...


    def Decode(self, id:str) -> str:
        """ Decode(self: SessionIDManager, id: str) -> str """
        ...

    def Encode(self, id:str) -> str:
        """ Encode(self: SessionIDManager, id: str) -> str """
        ...



class SessionStateActions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SessionStateActions, values: InitializeItem (1), None (0) """
    InitializeItem: SessionStateActions = ...
    value__ = ...


class SessionStateBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionStateBehavior, values: Default (0), Disabled (3), ReadOnly (2), Required (1) """
    Default: SessionStateBehavior = ...
    Disabled: SessionStateBehavior = ...
    ReadOnly: SessionStateBehavior = ...
    Required: SessionStateBehavior = ...
    value__ = ...


class SessionStateItemCollection(NameObjectCollectionBase, ISessionStateItemCollection): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ SessionStateItemCollection() """
    @staticmethod
    def Deserialize(reader:BinaryReader) -> SessionStateItemCollection:
        """ Deserialize(reader: BinaryReader) -> SessionStateItemCollection """
        ...

    def Serialize(self, writer:BinaryWriter): # -> 
        """ Serialize(self: SessionStateItemCollection, writer: BinaryWriter) """
        ...


class SessionStateItemExpireCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SessionStateItemExpireCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, id:str, item:SessionStateStoreData, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SessionStateItemExpireCallback, id: str, item: SessionStateStoreData, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SessionStateItemExpireCallback, result: IAsyncResult) """
        ...

    def Invoke(self, id:str, item:SessionStateStoreData): # -> 
        """ Invoke(self: SessionStateItemExpireCallback, id: str, item: SessionStateStoreData) """
        ...


class SessionStateMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionStateMode, values: Custom (4), InProc (1), Off (0), SQLServer (3), StateServer (2) """
    Custom: SessionStateMode = ...
    InProc: SessionStateMode = ...
    Off: SessionStateMode = ...
    SQLServer: SessionStateMode = ...
    StateServer: SessionStateMode = ...
    value__ = ...


class SessionStateModule(ISessionStateModule): # skipped bases: <type 'IHttpModule'>, <type 'object'>
    """ SessionStateModule() """
    def Dispose(self): # -> 
        """ Dispose(self: SessionStateModule) """
        ...

    def Init(self, app:HttpApplication): # -> 
        """ Init(self: SessionStateModule, app: HttpApplication) """
        ...

    End = ...
    Start = ...


class SessionStateStoreData: # skipped bases: <type 'object'>, <type 'object'>
    """ SessionStateStoreData(sessionItems: ISessionStateItemCollection, staticObjects: HttpStaticObjectsCollection, timeout: int) """
    @property
    def Items(self) -> ISessionStateItemCollection:
        """ Get: Items(self: SessionStateStoreData) -> ISessionStateItemCollection """
        ...

    @property
    def StaticObjects(self) -> HttpStaticObjectsCollection:
        """ Get: StaticObjects(self: SessionStateStoreData) -> HttpStaticObjectsCollection """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: SessionStateStoreData) -> int
        Set: Timeout(self: SessionStateStoreData) = value
        """
        ...



class SessionStateStoreProviderBase(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    def CreateNewStoreData(self, context:HttpContext, timeout:int) -> SessionStateStoreData:
        """ CreateNewStoreData(self: SessionStateStoreProviderBase, context: HttpContext, timeout: int) -> SessionStateStoreData """
        ...

    def CreateUninitializedItem(self, context:HttpContext, id:str, timeout:int): # -> 
        """ CreateUninitializedItem(self: SessionStateStoreProviderBase, context: HttpContext, id: str, timeout: int) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: SessionStateStoreProviderBase) """
        ...

    def EndRequest(self, context:HttpContext): # -> 
        """ EndRequest(self: SessionStateStoreProviderBase, context: HttpContext) """
        ...

    def GetItem(self, context, id, locked, lockAge, lockId, actions) -> Tuple_[SessionStateStoreData, bool, TimeSpan, object, SessionStateActions]:
        """ GetItem(self: SessionStateStoreProviderBase, context: HttpContext, id: str) -> (SessionStateStoreData, bool, TimeSpan, object, SessionStateActions) """
        ...

    def GetItemExclusive(self, context, id, locked, lockAge, lockId, actions) -> Tuple_[SessionStateStoreData, bool, TimeSpan, object, SessionStateActions]:
        """ GetItemExclusive(self: SessionStateStoreProviderBase, context: HttpContext, id: str) -> (SessionStateStoreData, bool, TimeSpan, object, SessionStateActions) """
        ...

    def InitializeRequest(self, context:HttpContext): # -> 
        """ InitializeRequest(self: SessionStateStoreProviderBase, context: HttpContext) """
        ...

    def ReleaseItemExclusive(self, context:HttpContext, id:str, lockId:object): # -> 
        """ ReleaseItemExclusive(self: SessionStateStoreProviderBase, context: HttpContext, id: str, lockId: object) """
        ...

    def RemoveItem(self, context:HttpContext, id:str, lockId:object, item:SessionStateStoreData): # -> 
        """ RemoveItem(self: SessionStateStoreProviderBase, context: HttpContext, id: str, lockId: object, item: SessionStateStoreData) """
        ...

    def ResetItemTimeout(self, context:HttpContext, id:str): # -> 
        """ ResetItemTimeout(self: SessionStateStoreProviderBase, context: HttpContext, id: str) """
        ...

    def SetAndReleaseItemExclusive(self, context:HttpContext, id:str, item:SessionStateStoreData, lockId:object, newItem:bool): # -> 
        """ SetAndReleaseItemExclusive(self: SessionStateStoreProviderBase, context: HttpContext, id: str, item: SessionStateStoreData, lockId: object, newItem: bool) """
        ...

    def SetItemExpireCallback(self, expireCallback:SessionStateItemExpireCallback) -> bool:
        """ SetItemExpireCallback(self: SessionStateStoreProviderBase, expireCallback: SessionStateItemExpireCallback) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SessionStateUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SerializationSurrogateSelector(self) -> ISurrogateSelector:
        """
        Get: SerializationSurrogateSelector() -> ISurrogateSelector
        Set: SerializationSurrogateSelector() = value
        """
        ...


    @staticmethod
    def AddHttpSessionStateToContext(context:HttpContext, container:IHttpSessionState): # -> 
        """ AddHttpSessionStateToContext(context: HttpContext, container: IHttpSessionState) """
        ...

    @staticmethod
    def GetHttpSessionStateFromContext(context:HttpContext) -> IHttpSessionState:
        """ GetHttpSessionStateFromContext(context: HttpContext) -> IHttpSessionState """
        ...

    @staticmethod
    def GetSessionStaticObjects(context:HttpContext) -> HttpStaticObjectsCollection:
        """ GetSessionStaticObjects(context: HttpContext) -> HttpStaticObjectsCollection """
        ...

    @staticmethod
    def IsSessionStateReadOnly(context:HttpContext) -> bool:
        """ IsSessionStateReadOnly(context: HttpContext) -> bool """
        ...

    @staticmethod
    def IsSessionStateRequired(context:HttpContext) -> bool:
        """ IsSessionStateRequired(context: HttpContext) -> bool """
        ...

    @staticmethod
    def RaiseSessionEnd(session:IHttpSessionState, eventSource:object, eventArgs:EventArgs): # -> 
        """ RaiseSessionEnd(session: IHttpSessionState, eventSource: object, eventArgs: EventArgs) """
        ...

    @staticmethod
    def RemoveHttpSessionStateFromContext(context:HttpContext): # -> 
        """ RemoveHttpSessionStateFromContext(context: HttpContext) """
        ...

    __all__: list = ...


class StateRuntime(IStateRuntime): # skipped bases: <type 'object'>
    """ StateRuntime() """
    pass

