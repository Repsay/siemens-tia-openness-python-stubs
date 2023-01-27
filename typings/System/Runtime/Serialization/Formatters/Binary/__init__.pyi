# encoding: utf-8
# module System.Runtime.Serialization.Formatters.Binary calls itself Binary
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.IO import Stream

from System.Runtime.Remoting.Messaging import (HeaderHandler, 
    IMethodCallMessage, IRemotingFormatter)

from System.Runtime.Serialization import (ISurrogateSelector, 
    SerializationBinder, StreamingContext)

from System.Runtime.Serialization.Formatters import (FormatterAssemblyStyle, 
    FormatterTypeStyle, TypeFilterLevel)


# no functions
# classes

class BinaryFormatter(IRemotingFormatter): # skipped bases: <type 'IFormatter'>, <type 'object'>
    """
    BinaryFormatter()
    BinaryFormatter(selector: ISurrogateSelector, context: StreamingContext)
    """
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle:
        """
        Get: AssemblyFormat(self: BinaryFormatter) -> FormatterAssemblyStyle
        Set: AssemblyFormat(self: BinaryFormatter) = value
        """
        ...

    @property
    def Binder(self) -> SerializationBinder:
        """
        Get: Binder(self: BinaryFormatter) -> SerializationBinder
        Set: Binder(self: BinaryFormatter) = value
        """
        ...

    @property
    def Context(self) -> StreamingContext:
        """
        Get: Context(self: BinaryFormatter) -> StreamingContext
        Set: Context(self: BinaryFormatter) = value
        """
        ...

    @property
    def FilterLevel(self) -> TypeFilterLevel:
        """
        Get: FilterLevel(self: BinaryFormatter) -> TypeFilterLevel
        Set: FilterLevel(self: BinaryFormatter) = value
        """
        ...

    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """
        Get: SurrogateSelector(self: BinaryFormatter) -> ISurrogateSelector
        Set: SurrogateSelector(self: BinaryFormatter) = value
        """
        ...

    @property
    def TypeFormat(self) -> FormatterTypeStyle:
        """
        Get: TypeFormat(self: BinaryFormatter) -> FormatterTypeStyle
        Set: TypeFormat(self: BinaryFormatter) = value
        """
        ...


    def DeserializeMethodResponse(self, serializationStream:Stream, handler:HeaderHandler, methodCallMessage:IMethodCallMessage) -> object:
        """ DeserializeMethodResponse(self: BinaryFormatter, serializationStream: Stream, handler: HeaderHandler, methodCallMessage: IMethodCallMessage) -> object """
        ...

    def UnsafeDeserialize(self, serializationStream:Stream, handler:HeaderHandler) -> object:
        """ UnsafeDeserialize(self: BinaryFormatter, serializationStream: Stream, handler: HeaderHandler) -> object """
        ...

    def UnsafeDeserializeMethodResponse(self, serializationStream:Stream, handler:HeaderHandler, methodCallMessage:IMethodCallMessage) -> object:
        """ UnsafeDeserializeMethodResponse(self: BinaryFormatter, serializationStream: Stream, handler: HeaderHandler, methodCallMessage: IMethodCallMessage) -> object """
        ...


