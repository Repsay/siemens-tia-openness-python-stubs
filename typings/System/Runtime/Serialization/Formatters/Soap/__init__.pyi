# encoding: utf-8
# module System.Runtime.Serialization.Formatters.Soap calls itself Soap
# from System.Runtime.Serialization.Formatters.Soap, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Runtime.Remoting.Messaging import IRemotingFormatter

from System.Runtime.Serialization import (ISurrogateSelector, 
    SerializationBinder, StreamingContext)

from System.Runtime.Serialization.Formatters import (FormatterAssemblyStyle, 
    FormatterTypeStyle, ISoapMessage, TypeFilterLevel)


# no functions
# classes

class SoapFormatter(IRemotingFormatter): # skipped bases: <type 'IFormatter'>, <type 'object'>
    """
    SoapFormatter()
    SoapFormatter(selector: ISurrogateSelector, context: StreamingContext)
    """
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle:
        """
        Get: AssemblyFormat(self: SoapFormatter) -> FormatterAssemblyStyle
        Set: AssemblyFormat(self: SoapFormatter) = value
        """
        ...

    @property
    def Binder(self) -> SerializationBinder:
        """
        Get: Binder(self: SoapFormatter) -> SerializationBinder
        Set: Binder(self: SoapFormatter) = value
        """
        ...

    @property
    def Context(self) -> StreamingContext:
        """
        Get: Context(self: SoapFormatter) -> StreamingContext
        Set: Context(self: SoapFormatter) = value
        """
        ...

    @property
    def FilterLevel(self) -> TypeFilterLevel:
        """
        Get: FilterLevel(self: SoapFormatter) -> TypeFilterLevel
        Set: FilterLevel(self: SoapFormatter) = value
        """
        ...

    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """
        Get: SurrogateSelector(self: SoapFormatter) -> ISurrogateSelector
        Set: SurrogateSelector(self: SoapFormatter) = value
        """
        ...

    @property
    def TopObject(self) -> ISoapMessage:
        """
        Get: TopObject(self: SoapFormatter) -> ISoapMessage
        Set: TopObject(self: SoapFormatter) = value
        """
        ...

    @property
    def TypeFormat(self) -> FormatterTypeStyle:
        """
        Get: TypeFormat(self: SoapFormatter) -> FormatterTypeStyle
        Set: TypeFormat(self: SoapFormatter) = value
        """
        ...



