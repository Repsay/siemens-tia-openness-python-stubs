# encoding: utf-8
# module System.Runtime.Remoting.Messaging calls itself Messaging
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, IAsyncResult, ICloneable, 
    MulticastDelegate)

from System.Collections import IDictionary

from System.Reflection import MethodBase

from System.Runtime.Remoting.Activation import (IConstructionCallMessage, 
    IConstructionReturnMessage)

from System.Runtime.Serialization import (IFormatter, ISerializable, 
    ISurrogateSelector, SerializationInfo, StreamingContext)

"""The following names are not found in the module: (IInternalMessage, 
    ISerializationRootObject, field#)
"""

# no functions
# classes

class AsyncResult(IMessageSink, IAsyncResult): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsyncDelegate(self) -> object:
        """ Get: AsyncDelegate(self: AsyncResult) -> object """
        ...

    @property
    def EndInvokeCalled(self) -> bool:
        """
        Get: EndInvokeCalled(self: AsyncResult) -> bool
        Set: EndInvokeCalled(self: AsyncResult) = value
        """
        ...


    def GetReplyMessage(self) -> IMessage:
        """ GetReplyMessage(self: AsyncResult) -> IMessage """
        ...

    def SetMessageCtrl(self, mc:IMessageCtrl): # -> 
        """ SetMessageCtrl(self: AsyncResult, mc: IMessageCtrl) """
        ...


class CallContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HostContext(self) -> object:
        """
        Get: HostContext() -> object
        Set: HostContext() = value
        """
        ...


    @staticmethod
    def FreeNamedDataSlot(name:str): # -> 
        """ FreeNamedDataSlot(name: str) """
        ...

    @staticmethod
    def GetData(name:str) -> object:
        """ GetData(name: str) -> object """
        ...

    @staticmethod
    def GetHeaders() -> Array:
        """ GetHeaders() -> Array[Header] """
        ...

    @staticmethod
    def LogicalGetData(name:str) -> object:
        """ LogicalGetData(name: str) -> object """
        ...

    @staticmethod
    def LogicalSetData(name:str, data:object): # -> 
        """ LogicalSetData(name: str, data: object) """
        ...

    @staticmethod
    def SetData(name:str, data:object): # -> 
        """ SetData(name: str, data: object) """
        ...

    @staticmethod
    def SetHeaders(headers:Array): # -> 
        """ SetHeaders(headers: Array[Header]) """
        ...


class IMessage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: IMessage) -> IDictionary """
        ...



class IMethodMessage(IMessage): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: IMethodMessage) -> int """
        ...

    @property
    def Args(self) -> Array:
        """ Get: Args(self: IMethodMessage) -> Array[object] """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: IMethodMessage) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: IMethodMessage) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: IMethodMessage) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: IMethodMessage) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: IMethodMessage) -> object """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: IMethodMessage) -> str """
        ...

    @property
    def Uri(self) -> str:
        """ Get: Uri(self: IMethodMessage) -> str """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: IMethodMessage, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: IMethodMessage, index: int) -> str """
        ...


class IMethodCallMessage(IMethodMessage): # skipped bases: <type 'IMessage'>, <type 'object'>
    """ no doc """
    @property
    def InArgCount(self) -> int:
        """ Get: InArgCount(self: IMethodCallMessage) -> int """
        ...

    @property
    def InArgs(self) -> Array:
        """ Get: InArgs(self: IMethodCallMessage) -> Array[object] """
        ...


    def GetInArg(self, argNum:int) -> object:
        """ GetInArg(self: IMethodCallMessage, argNum: int) -> object """
        ...

    def GetInArgName(self, index:int) -> str:
        """ GetInArgName(self: IMethodCallMessage, index: int) -> str """
        ...


class MethodCall(ISerializationRootObject, IInternalMessage, ISerializable, IMethodCallMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """
    MethodCall(h1: Array[Header])
    MethodCall(msg: IMessage)
    """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: MethodCall) -> int """
        ...

    @property
    def Args(self) -> Array:
        """ Get: Args(self: MethodCall) -> Array[object] """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: MethodCall) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: MethodCall) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: MethodCall) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: MethodCall) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: MethodCall) -> object """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: MethodCall) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MethodCall) -> str """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: MethodCall) -> str
        Set: Uri(self: MethodCall) = value
        """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: MethodCall, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: MethodCall, index: int) -> str """
        ...

    def HeaderHandler(self, h:Array) -> object:
        """ HeaderHandler(self: MethodCall, h: Array[Header]) -> object """
        ...

    def Init(self): # -> 
        """ Init(self: MethodCall) """
        ...

    def ResolveMethod(self): # -> 
        """ ResolveMethod(self: MethodCall) """
        ...

    def RootSetObjectData(self, info:SerializationInfo, ctx:StreamingContext): # -> 
        """ RootSetObjectData(self: MethodCall, info: SerializationInfo, ctx: StreamingContext) """
        ...

    ExternalProperties = ...
    InternalProperties = ...


class ConstructionCall(MethodCall, IConstructionCallMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMethodCallMessage'>, <type 'ISerializationRootObject'>, <type 'IMessage'>, <type 'ISerializable'>, <type 'IInternalMessage'>, <type 'object'>
    """
    ConstructionCall(headers: Array[Header])
    ConstructionCall(m: IMessage)
    """
    ExternalProperties = ...
    InternalProperties = ...


class IMethodReturnMessage(IMethodMessage): # skipped bases: <type 'IMessage'>, <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: IMethodReturnMessage) -> Exception """
        ...

    @property
    def OutArgCount(self) -> int:
        """ Get: OutArgCount(self: IMethodReturnMessage) -> int """
        ...

    @property
    def OutArgs(self) -> Array:
        """ Get: OutArgs(self: IMethodReturnMessage) -> Array[object] """
        ...

    @property
    def ReturnValue(self) -> object:
        """ Get: ReturnValue(self: IMethodReturnMessage) -> object """
        ...


    def GetOutArg(self, argNum:int) -> object:
        """ GetOutArg(self: IMethodReturnMessage, argNum: int) -> object """
        ...

    def GetOutArgName(self, index:int) -> str:
        """ GetOutArgName(self: IMethodReturnMessage, index: int) -> str """
        ...


class MethodResponse(ISerializationRootObject, IInternalMessage, IMethodReturnMessage, ISerializable): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """ MethodResponse(h1: Array[Header], mcm: IMethodCallMessage) """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: MethodResponse) -> int """
        ...

    @property
    def Args(self) -> Array:
        """ Get: Args(self: MethodResponse) -> Array[object] """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: MethodResponse) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: MethodResponse) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: MethodResponse) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: MethodResponse) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: MethodResponse) -> object """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: MethodResponse) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MethodResponse) -> str """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: MethodResponse) -> str
        Set: Uri(self: MethodResponse) = value
        """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: MethodResponse, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: MethodResponse, index: int) -> str """
        ...

    def HeaderHandler(self, h:Array) -> object:
        """ HeaderHandler(self: MethodResponse, h: Array[Header]) -> object """
        ...

    def RootSetObjectData(self, info:SerializationInfo, ctx:StreamingContext): # -> 
        """ RootSetObjectData(self: MethodResponse, info: SerializationInfo, ctx: StreamingContext) """
        ...

    ExternalProperties = ...
    InternalProperties = ...


class ConstructionResponse(MethodResponse, IConstructionReturnMessage): # skipped bases: <type 'IMethodMessage'>, <type 'ISerializationRootObject'>, <type 'IMessage'>, <type 'IMethodReturnMessage'>, <type 'ISerializable'>, <type 'IInternalMessage'>, <type 'object'>
    """ ConstructionResponse(h: Array[Header], mcm: IMethodCallMessage) """
    ExternalProperties = ...
    InternalProperties = ...


class Header: # skipped bases: <type 'object'>, <type 'object'>
    """
    Header(_Name: str, _Value: object)
    Header(_Name: str, _Value: object, _MustUnderstand: bool)
    Header(_Name: str, _Value: object, _MustUnderstand: bool, _HeaderNamespace: str)
    """
    HeaderNamespace = ...
    MustUnderstand = ...
    Name = ...
    Value = ...


class HeaderHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HeaderHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, headers:Array, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HeaderHandler, headers: Array[Header], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: HeaderHandler, result: IAsyncResult) -> object """
        ...

    def Invoke(self, headers:Array) -> object:
        """ Invoke(self: HeaderHandler, headers: Array[Header]) -> object """
        ...


class ILogicalThreadAffinative: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IMessageCtrl: # skipped bases: <type 'object'>
    """ no doc """
    def Cancel(self, msToCancel:int): # -> 
        """ Cancel(self: IMessageCtrl, msToCancel: int) """
        ...


class IMessageSink: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NextSink(self) -> IMessageSink:
        """ Get: NextSink(self: IMessageSink) -> IMessageSink """
        ...


    def AsyncProcessMessage(self, msg:IMessage, replySink:IMessageSink) -> IMessageCtrl:
        """ AsyncProcessMessage(self: IMessageSink, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl """
        ...

    def SyncProcessMessage(self, msg:IMessage) -> IMessage:
        """ SyncProcessMessage(self: IMessageSink, msg: IMessage) -> IMessage """
        ...


class InternalMessageWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ InternalMessageWrapper(msg: IMessage) """
    WrappedMessage = ...


class IRemotingFormatter(IFormatter): # skipped bases: <type 'object'>
    """ no doc """
    pass

class LogicalCallContext(ICloneable, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasInfo(self) -> bool:
        """ Get: HasInfo(self: LogicalCallContext) -> bool """
        ...


    def FreeNamedDataSlot(self, name:str): # -> 
        """ FreeNamedDataSlot(self: LogicalCallContext, name: str) """
        ...

    def GetData(self, name:str) -> object:
        """ GetData(self: LogicalCallContext, name: str) -> object """
        ...

    def SetData(self, name:str, data:object): # -> 
        """ SetData(self: LogicalCallContext, name: str, data: object) """
        ...


class MessageSurrogateFilter(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MessageSurrogateFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, key:str, value:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MessageSurrogateFilter, key: str, value: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: MessageSurrogateFilter, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, key:str, value:object) -> bool:
        """ Invoke(self: MessageSurrogateFilter, key: str, value: object) -> bool """
        ...


class MethodCallMessageWrapper(InternalMessageWrapper, IMethodCallMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """ MethodCallMessageWrapper(msg: IMethodCallMessage) """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: MethodCallMessageWrapper) -> int """
        ...

    @property
    def Args(self) -> Array:
        """
        Get: Args(self: MethodCallMessageWrapper) -> Array[object]
        Set: Args(self: MethodCallMessageWrapper) = value
        """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: MethodCallMessageWrapper) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: MethodCallMessageWrapper) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: MethodCallMessageWrapper) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: MethodCallMessageWrapper) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: MethodCallMessageWrapper) -> object """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: MethodCallMessageWrapper) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MethodCallMessageWrapper) -> str """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: MethodCallMessageWrapper) -> str
        Set: Uri(self: MethodCallMessageWrapper) = value
        """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: MethodCallMessageWrapper, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: MethodCallMessageWrapper, index: int) -> str """
        ...

    WrappedMessage = ...


class MethodReturnMessageWrapper(InternalMessageWrapper, IMethodReturnMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """ MethodReturnMessageWrapper(msg: IMethodReturnMessage) """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: MethodReturnMessageWrapper) -> int """
        ...

    @property
    def Args(self) -> Array:
        """
        Get: Args(self: MethodReturnMessageWrapper) -> Array[object]
        Set: Args(self: MethodReturnMessageWrapper) = value
        """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: MethodReturnMessageWrapper) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: MethodReturnMessageWrapper) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: MethodReturnMessageWrapper) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: MethodReturnMessageWrapper) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: MethodReturnMessageWrapper) -> object """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: MethodReturnMessageWrapper) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MethodReturnMessageWrapper) -> str """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: MethodReturnMessageWrapper) -> str
        Set: Uri(self: MethodReturnMessageWrapper) = value
        """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: MethodReturnMessageWrapper, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: MethodReturnMessageWrapper, index: int) -> str """
        ...

    WrappedMessage = ...


class OneWayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OneWayAttribute() """
    pass

class RemotingSurrogateSelector(ISurrogateSelector): # skipped bases: <type 'object'>
    """ RemotingSurrogateSelector() """
    @property
    def Filter(self) -> MessageSurrogateFilter:
        """
        Get: Filter(self: RemotingSurrogateSelector) -> MessageSurrogateFilter
        Set: Filter(self: RemotingSurrogateSelector) = value
        """
        ...


    def GetRootObject(self) -> object:
        """ GetRootObject(self: RemotingSurrogateSelector) -> object """
        ...

    def SetRootObject(self, obj:object): # -> 
        """ SetRootObject(self: RemotingSurrogateSelector, obj: object) """
        ...

    def UseSoapFormat(self): # -> 
        """ UseSoapFormat(self: RemotingSurrogateSelector) """
        ...


class ReturnMessage(IMethodReturnMessage): # skipped bases: <type 'IMethodMessage'>, <type 'IMessage'>, <type 'object'>
    """
    ReturnMessage(ret: object, outArgs: Array[object], outArgsCount: int, callCtx: LogicalCallContext, mcm: IMethodCallMessage)
    ReturnMessage(e: Exception, mcm: IMethodCallMessage)
    """
    @property
    def ArgCount(self) -> int:
        """ Get: ArgCount(self: ReturnMessage) -> int """
        ...

    @property
    def Args(self) -> Array:
        """ Get: Args(self: ReturnMessage) -> Array[object] """
        ...

    @property
    def HasVarArgs(self) -> bool:
        """ Get: HasVarArgs(self: ReturnMessage) -> bool """
        ...

    @property
    def LogicalCallContext(self) -> LogicalCallContext:
        """ Get: LogicalCallContext(self: ReturnMessage) -> LogicalCallContext """
        ...

    @property
    def MethodBase(self) -> MethodBase:
        """ Get: MethodBase(self: ReturnMessage) -> MethodBase """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: ReturnMessage) -> str """
        ...

    @property
    def MethodSignature(self) -> object:
        """ Get: MethodSignature(self: ReturnMessage) -> object """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: ReturnMessage) -> IDictionary """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ReturnMessage) -> str """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: ReturnMessage) -> str
        Set: Uri(self: ReturnMessage) = value
        """
        ...


    def GetArg(self, argNum:int) -> object:
        """ GetArg(self: ReturnMessage, argNum: int) -> object """
        ...

    def GetArgName(self, index:int) -> str:
        """ GetArgName(self: ReturnMessage, index: int) -> str """
        ...


