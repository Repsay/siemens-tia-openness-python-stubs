# encoding: utf-8
# module System.Web.Script.Services calls itself Services
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, Type

from System.ServiceModel.Description import ServiceEndpoint

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class GenerateScriptTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ GenerateScriptTypeAttribute(type: Type) """
    @property
    def ScriptTypeId(self) -> str:
        """
        Get: ScriptTypeId(self: GenerateScriptTypeAttribute) -> str
        Set: ScriptTypeId(self: GenerateScriptTypeAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: GenerateScriptTypeAttribute) -> Type """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class ProxyGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetClientProxyScript(type:Type, path:str, debug:bool, serviceEndpoint:ServiceEndpoint = ...) -> str:
        """
        GetClientProxyScript(type: Type, path: str, debug: bool) -> str
        GetClientProxyScript(type: Type, path: str, debug: bool, serviceEndpoint: ServiceEndpoint) -> str
        """
        ...

    __all__: list = ...


class ResponseFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResponseFormat, values: Json (0), Xml (1) """
    Json: ResponseFormat = ...
    value__ = ...
    Xml: ResponseFormat = ...


class ScriptMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScriptMethodAttribute() """
    @property
    def ResponseFormat(self) -> ResponseFormat:
        """
        Get: ResponseFormat(self: ScriptMethodAttribute) -> ResponseFormat
        Set: ResponseFormat(self: ScriptMethodAttribute) = value
        """
        ...

    @property
    def UseHttpGet(self) -> bool:
        """
        Get: UseHttpGet(self: ScriptMethodAttribute) -> bool
        Set: UseHttpGet(self: ScriptMethodAttribute) = value
        """
        ...

    @property
    def XmlSerializeString(self) -> bool:
        """
        Get: XmlSerializeString(self: ScriptMethodAttribute) -> bool
        Set: XmlSerializeString(self: ScriptMethodAttribute) = value
        """
        ...



class ScriptServiceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScriptServiceAttribute() """
    pass

