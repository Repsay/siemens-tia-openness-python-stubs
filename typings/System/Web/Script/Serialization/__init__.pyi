# encoding: utf-8
# module System.Web.Script.Serialization calls itself Serialization
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Type

from System.Collections import IDictionary, IEnumerable

from System.Text import StringBuilder


# no functions
# classes

class JavaScriptConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SupportedTypes(self) -> IEnumerable:
        """ Get: SupportedTypes(self: JavaScriptConverter) -> IEnumerable[Type] """
        ...


    def Deserialize(self, dictionary:IDictionary, type:Type, serializer:JavaScriptSerializer) -> object:
        """ Deserialize(self: JavaScriptConverter, dictionary: IDictionary[str, object], type: Type, serializer: JavaScriptSerializer) -> object """
        ...

    def Serialize(self, obj:object, serializer:JavaScriptSerializer) -> IDictionary:
        """ Serialize(self: JavaScriptConverter, obj: object, serializer: JavaScriptSerializer) -> IDictionary[str, object] """
        ...


class JavaScriptSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """
    JavaScriptSerializer()
    JavaScriptSerializer(resolver: JavaScriptTypeResolver)
    """
    @property
    def MaxJsonLength(self) -> int:
        """
        Get: MaxJsonLength(self: JavaScriptSerializer) -> int
        Set: MaxJsonLength(self: JavaScriptSerializer) = value
        """
        ...

    @property
    def RecursionLimit(self) -> int:
        """
        Get: RecursionLimit(self: JavaScriptSerializer) -> int
        Set: RecursionLimit(self: JavaScriptSerializer) = value
        """
        ...


    def ConvertToType(self, obj:object, targetType:Type = ...) -> object:
        """
        ConvertToType(self: JavaScriptSerializer, obj: object, targetType: Type) -> object
        ConvertToType[T](self: JavaScriptSerializer, obj: object) -> T
        """
        ...

    def Deserialize(self, input:str, targetType:Type = ...) -> object:
        """
        Deserialize(self: JavaScriptSerializer, input: str, targetType: Type) -> object
        Deserialize[T](self: JavaScriptSerializer, input: str) -> T
        """
        ...

    def DeserializeObject(self, input:str) -> object:
        """ DeserializeObject(self: JavaScriptSerializer, input: str) -> object """
        ...

    def RegisterConverters(self, converters:IEnumerable): # -> 
        """ RegisterConverters(self: JavaScriptSerializer, converters: IEnumerable[JavaScriptConverter]) """
        ...

    def Serialize(self, obj:object, output:StringBuilder = ...): # -> 
        """
        Serialize(self: JavaScriptSerializer, obj: object) -> str
        Serialize(self: JavaScriptSerializer, obj: object, output: StringBuilder)
        """
        ...


class JavaScriptTypeResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ResolveType(self, id:str) -> Type:
        """ ResolveType(self: JavaScriptTypeResolver, id: str) -> Type """
        ...

    def ResolveTypeId(self, type:Type) -> str:
        """ ResolveTypeId(self: JavaScriptTypeResolver, type: Type) -> str """
        ...


class ScriptIgnoreAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScriptIgnoreAttribute() """
    @property
    def ApplyToOverrides(self) -> bool:
        """
        Get: ApplyToOverrides(self: ScriptIgnoreAttribute) -> bool
        Set: ApplyToOverrides(self: ScriptIgnoreAttribute) = value
        """
        ...



class SimpleTypeResolver(JavaScriptTypeResolver): # skipped bases: <type 'object'>
    """ SimpleTypeResolver() """
    pass

