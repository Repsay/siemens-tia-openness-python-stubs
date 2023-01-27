# encoding: utf-8
# module System.Workflow.ComponentModel.Serialization calls itself Serialization
# from System.Workflow.ComponentModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, IServiceProvider, Type

from System.ComponentModel.Design.Serialization import (CodeDomSerializer, 
    IDesignerSerializationManager, TypeCodeDomSerializer)

from System.Reflection import Assembly

from System.Runtime.Serialization import SurrogateSelector

from System.Workflow.ComponentModel import DependencyProperty

from System.Xml import XmlQualifiedName, XmlReader, XmlWriter

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ActivityCodeDomSerializationManager(IDesignerSerializationManager): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ ActivityCodeDomSerializationManager(manager: IDesignerSerializationManager) """
    @property
    def SerializationManager(self):
        ...


    def GetService(self, serviceType:Type) -> object:
        """ GetService(self: ActivityCodeDomSerializationManager, serviceType: Type) -> object """
        ...

    ResolveName = ...
    SerializationComplete = ...


class DependencyObjectCodeDomSerializer(CodeDomSerializer): # skipped bases: <type 'object'>
    """ DependencyObjectCodeDomSerializer() """
    pass

class ActivityCodeDomSerializer(DependencyObjectCodeDomSerializer): # skipped bases: <type 'object'>
    """ ActivityCodeDomSerializer() """
    MarkupFileNameProperty: DependencyProperty = ...


class WorkflowMarkupSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowMarkupSerializer() """
    def AddChild(self, *args): #cannot find CLR method
        """ AddChild(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, parentObject: object, childObj: object) """
        ...

    def CanSerializeToString(self, *args): #cannot find CLR method
        """ CanSerializeToString(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, value: object) -> bool """
        ...

    def ClearChildren(self, *args): #cannot find CLR method
        """ ClearChildren(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, type: Type) -> object """
        ...

    def Deserialize(self, *__args:XmlReader) -> object:
        """
        Deserialize(self: WorkflowMarkupSerializer, reader: XmlReader) -> object
        Deserialize(self: WorkflowMarkupSerializer, serializationManager: IDesignerSerializationManager, reader: XmlReader) -> object
        """
        ...

    def DeserializeFromString(self, *args): #cannot find CLR method
        """ DeserializeFromString(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, propertyType: Type, value: str) -> object """
        ...

    def GetChildren(self, *args): #cannot find CLR method
        """ GetChildren(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) -> IList """
        ...

    def GetEvents(self, *args): #cannot find CLR method
        """ GetEvents(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) -> Array[EventInfo] """
        ...

    def GetProperties(self, *args): #cannot find CLR method
        """ GetProperties(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) -> Array[PropertyInfo] """
        ...

    def OnAfterDeserialize(self, *args): #cannot find CLR method
        """ OnAfterDeserialize(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) """
        ...

    def OnAfterSerialize(self, *args): #cannot find CLR method
        """ OnAfterSerialize(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) """
        ...

    def OnBeforeDeserialize(self, *args): #cannot find CLR method
        """ OnBeforeDeserialize(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) """
        ...

    def OnBeforeSerialize(self, *args): #cannot find CLR method
        """ OnBeforeSerialize(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, obj: object) """
        ...

    def Serialize(self, *__args): # -> 
        """ Serialize(self: WorkflowMarkupSerializer, writer: XmlWriter, obj: object)Serialize(self: WorkflowMarkupSerializer, serializationManager: IDesignerSerializationManager, writer: XmlWriter, obj: object) """
        ...

    def SerializeToString(self, *args): #cannot find CLR method
        """ SerializeToString(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, value: object) -> str """
        ...

    def ShouldSerializeValue(self, *args): #cannot find CLR method
        """ ShouldSerializeValue(self: WorkflowMarkupSerializer, serializationManager: WorkflowMarkupSerializationManager, value: object) -> bool """
        ...

    ClrNamespacesProperty: DependencyProperty = ...
    EventsProperty: DependencyProperty = ...
    XClassProperty: DependencyProperty = ...
    XCodeProperty: DependencyProperty = ...


class ActivityMarkupSerializer(WorkflowMarkupSerializer): # skipped bases: <type 'object'>
    """ ActivityMarkupSerializer() """
    EndColumnProperty: DependencyProperty = ...
    EndLineProperty: DependencyProperty = ...
    StartColumnProperty: DependencyProperty = ...
    StartLineProperty: DependencyProperty = ...


class ActivitySurrogateSelector(SurrogateSelector): # skipped bases: <type 'ISurrogateSelector'>, <type 'object'>
    """ ActivitySurrogateSelector() """
    @property
    def Default(self) -> ActivitySurrogateSelector:
        """ Get: Default() -> ActivitySurrogateSelector """
        ...




class ActivityTypeCodeDomSerializer(TypeCodeDomSerializer): # skipped bases: <type 'object'>
    """ ActivityTypeCodeDomSerializer() """
    pass

class CompositeActivityMarkupSerializer(ActivityMarkupSerializer): # skipped bases: <type 'object'>
    """ CompositeActivityMarkupSerializer() """
    pass

class ConstructorArgumentAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConstructorArgumentAttribute(argumentName: str) """
    @property
    def ArgumentName(self) -> str:
        """ Get: ArgumentName(self: ConstructorArgumentAttribute) -> str """
        ...


    def __new__(cls, argumentName:str) -> Self:
        """ __new__(cls: type, argumentName: str) """
        ...


class ContentPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ContentPropertyAttribute()
    ContentPropertyAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ContentPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class MarkupExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ProvideValue(self, provider:IServiceProvider) -> object:
        """ ProvideValue(self: MarkupExtension, provider: IServiceProvider) -> object """
        ...


class RuntimeNamePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RuntimeNamePropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: RuntimeNamePropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class WorkflowMarkupSerializationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowMarkupSerializationException(message: str, lineNumber: int, columnNumber: int)
    WorkflowMarkupSerializationException(message: str, innerException: Exception, lineNumber: int, columnNumber: int)
    WorkflowMarkupSerializationException(message: str, innerException: Exception)
    WorkflowMarkupSerializationException(message: str)
    WorkflowMarkupSerializationException()
    """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: WorkflowMarkupSerializationException) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: WorkflowMarkupSerializationException) -> int """
        ...


    SerializeObjectState = ...


class WorkflowMarkupSerializationManager(IDesignerSerializationManager): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ WorkflowMarkupSerializationManager(manager: IDesignerSerializationManager) """
    @property
    def LocalAssembly(self) -> Assembly:
        """
        Get: LocalAssembly(self: WorkflowMarkupSerializationManager) -> Assembly
        Set: LocalAssembly(self: WorkflowMarkupSerializationManager) = value
        """
        ...

    @property
    def SerializationManager(self):
        ...


    def GetService(self, serviceType:Type) -> object:
        """ GetService(self: WorkflowMarkupSerializationManager, serviceType: Type) -> object """
        ...

    def GetXmlQualifiedName(self, type, prefix) -> Tuple_[XmlQualifiedName, str]:
        """ GetXmlQualifiedName(self: WorkflowMarkupSerializationManager, type: Type) -> (XmlQualifiedName, str) """
        ...


class XmlnsDefinitionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlnsDefinitionAttribute(xmlNamespace: str, clrNamespace: str) """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: XmlnsDefinitionAttribute) -> str
        Set: AssemblyName(self: XmlnsDefinitionAttribute) = value
        """
        ...

    @property
    def ClrNamespace(self) -> str:
        """ Get: ClrNamespace(self: XmlnsDefinitionAttribute) -> str """
        ...

    @property
    def XmlNamespace(self) -> str:
        """ Get: XmlNamespace(self: XmlnsDefinitionAttribute) -> str """
        ...


    def __new__(cls, xmlNamespace:str, clrNamespace:str) -> Self:
        """ __new__(cls: type, xmlNamespace: str, clrNamespace: str) """
        ...


class XmlnsPrefixAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlnsPrefixAttribute(xmlNamespace: str, prefix: str) """
    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: XmlnsPrefixAttribute) -> str """
        ...

    @property
    def XmlNamespace(self) -> str:
        """ Get: XmlNamespace(self: XmlnsPrefixAttribute) -> str """
        ...


    def __new__(cls, xmlNamespace:str, prefix:str) -> Self:
        """ __new__(cls: type, xmlNamespace: str, prefix: str) """
        ...


