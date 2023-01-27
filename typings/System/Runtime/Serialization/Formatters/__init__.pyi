# encoding: utf-8
# module System.Runtime.Serialization.Formatters calls itself Formatters
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Serialization.Formatters.Soap, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum

from System.Reflection import Assembly, FieldInfo

from System.Runtime.Serialization import ISerializable

"""The following names are not found in the module: field#
"""

# no functions
# classes

class FormatterAssemblyStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormatterAssemblyStyle, values: Full (1), Simple (0) """
    Full: FormatterAssemblyStyle = ...
    Simple: FormatterAssemblyStyle = ...
    value__ = ...


class FormatterTypeStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormatterTypeStyle, values: TypesAlways (1), TypesWhenNeeded (0), XsdString (2) """
    TypesAlways: FormatterTypeStyle = ...
    TypesWhenNeeded: FormatterTypeStyle = ...
    value__ = ...
    XsdString: FormatterTypeStyle = ...


class IFieldInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FieldNames(self) -> Array:
        """
        Get: FieldNames(self: IFieldInfo) -> Array[str]
        Set: FieldNames(self: IFieldInfo) = value
        """
        ...

    @property
    def FieldTypes(self) -> Array:
        """
        Get: FieldTypes(self: IFieldInfo) -> Array[Type]
        Set: FieldTypes(self: IFieldInfo) = value
        """
        ...



class InternalRM: # skipped bases: <type 'object'>, <type 'object'>
    """ InternalRM() """
    @staticmethod
    def InfoSoap(messages:Array): # -> 
        """ InfoSoap(*messages: Array[object]) """
        ...

    @staticmethod
    def SoapCheckEnabled() -> bool:
        """ SoapCheckEnabled() -> bool """
        ...


class InternalST: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def InfoSoap(messages:Array): # -> 
        """ InfoSoap(*messages: Array[object]) """
        ...

    @staticmethod
    def LoadAssemblyFromString(assemblyString:str) -> Assembly:
        """ LoadAssemblyFromString(assemblyString: str) -> Assembly """
        ...

    @staticmethod
    def SerializationSetValue(fi:FieldInfo, target:object, value:object): # -> 
        """ SerializationSetValue(fi: FieldInfo, target: object, value: object) """
        ...

    @staticmethod
    def Soap(messages:Array): # -> 
        """ Soap(*messages: Array[object]) """
        ...

    @staticmethod
    def SoapAssert(condition:bool, message:str): # -> 
        """ SoapAssert(condition: bool, message: str) """
        ...

    @staticmethod
    def SoapCheckEnabled() -> bool:
        """ SoapCheckEnabled() -> bool """
        ...


class ISoapMessage: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Headers(self) -> Array:
        """
        Get: Headers(self: ISoapMessage) -> Array[Header]
        Set: Headers(self: ISoapMessage) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: ISoapMessage) -> str
        Set: MethodName(self: ISoapMessage) = value
        """
        ...

    @property
    def ParamNames(self) -> Array:
        """
        Get: ParamNames(self: ISoapMessage) -> Array[str]
        Set: ParamNames(self: ISoapMessage) = value
        """
        ...

    @property
    def ParamTypes(self) -> Array:
        """
        Get: ParamTypes(self: ISoapMessage) -> Array[Type]
        Set: ParamTypes(self: ISoapMessage) = value
        """
        ...

    @property
    def ParamValues(self) -> Array:
        """
        Get: ParamValues(self: ISoapMessage) -> Array[object]
        Set: ParamValues(self: ISoapMessage) = value
        """
        ...

    @property
    def XmlNameSpace(self) -> str:
        """
        Get: XmlNameSpace(self: ISoapMessage) -> str
        Set: XmlNameSpace(self: ISoapMessage) = value
        """
        ...



class ServerFault: # skipped bases: <type 'object'>, <type 'object'>
    """ ServerFault(exceptionType: str, message: str, stackTrace: str) """
    @property
    def ExceptionMessage(self) -> str:
        """
        Get: ExceptionMessage(self: ServerFault) -> str
        Set: ExceptionMessage(self: ServerFault) = value
        """
        ...

    @property
    def ExceptionType(self) -> str:
        """
        Get: ExceptionType(self: ServerFault) -> str
        Set: ExceptionType(self: ServerFault) = value
        """
        ...

    @property
    def StackTrace(self) -> str:
        """
        Get: StackTrace(self: ServerFault) -> str
        Set: StackTrace(self: ServerFault) = value
        """
        ...



class SoapFault(ISerializable): # skipped bases: <type 'object'>
    """
    SoapFault()
    SoapFault(faultCode: str, faultString: str, faultActor: str, serverFault: ServerFault)
    """
    @property
    def Detail(self) -> object:
        """
        Get: Detail(self: SoapFault) -> object
        Set: Detail(self: SoapFault) = value
        """
        ...

    @property
    def FaultActor(self) -> str:
        """
        Get: FaultActor(self: SoapFault) -> str
        Set: FaultActor(self: SoapFault) = value
        """
        ...

    @property
    def FaultCode(self) -> str:
        """
        Get: FaultCode(self: SoapFault) -> str
        Set: FaultCode(self: SoapFault) = value
        """
        ...

    @property
    def FaultString(self) -> str:
        """
        Get: FaultString(self: SoapFault) -> str
        Set: FaultString(self: SoapFault) = value
        """
        ...



class SoapMessage(ISoapMessage): # skipped bases: <type 'object'>
    """ SoapMessage() """
    pass

class TypeFilterLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TypeFilterLevel, values: Full (3), Low (2) """
    Full: TypeFilterLevel = ...
    Low: TypeFilterLevel = ...
    value__ = ...


# variables with complex values

