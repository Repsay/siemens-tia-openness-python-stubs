# encoding: utf-8
# module System.Windows.Markup calls itself Markup
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Char, EventArgs, IServiceProvider, Type, Uri

from System.Collections import IDictionary, IEnumerable, IList

from System.ComponentModel import ITypeDescriptorContext, TypeConverter

from System.Globalization import CultureInfo

from System.Xaml import XamlMember, XamlType

from typing import Self


# no functions
# classes

class AcceptedMarkupExtensionExpressionTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AcceptedMarkupExtensionExpressionTypeAttribute(type: Type) """
    @property
    def Type(self) -> Type:
        """
        Get: Type(self: AcceptedMarkupExtensionExpressionTypeAttribute) -> Type
        Set: Type(self: AcceptedMarkupExtensionExpressionTypeAttribute) = value
        """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class AmbientAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AmbientAttribute() """
    pass

class MarkupExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ProvideValue(self, serviceProvider:IServiceProvider) -> object:
        """ ProvideValue(self: MarkupExtension, serviceProvider: IServiceProvider) -> object """
        ...


class ArrayExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    ArrayExtension()
    ArrayExtension(arrayType: Type)
    ArrayExtension(elements: Array)
    """
    @property
    def Items(self) -> IList:
        """ Get: Items(self: ArrayExtension) -> IList """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: ArrayExtension) -> Type
        Set: Type(self: ArrayExtension) = value
        """
        ...


    def AddChild(self, value:object): # -> 
        """ AddChild(self: ArrayExtension, value: object) """
        ...

    def AddText(self, text:str): # -> 
        """ AddText(self: ArrayExtension, text: str) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, arrayType: Type)
        __new__(cls: type, elements: Array)
        """
        ...


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


class ContentWrapperAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContentWrapperAttribute(contentWrapper: Type) """
    @property
    def ContentWrapper(self) -> Type:
        """ Get: ContentWrapper(self: ContentWrapperAttribute) -> Type """
        ...


    def __new__(cls, contentWrapper:Type) -> Self:
        """ __new__(cls: type, contentWrapper: Type) """
        ...


class ValueSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanConvertFromString(self, value:str, context:IValueSerializerContext) -> bool:
        """ CanConvertFromString(self: ValueSerializer, value: str, context: IValueSerializerContext) -> bool """
        ...

    def CanConvertToString(self, value:object, context:IValueSerializerContext) -> bool:
        """ CanConvertToString(self: ValueSerializer, value: object, context: IValueSerializerContext) -> bool """
        ...

    def ConvertFromString(self, value:str, context:IValueSerializerContext) -> object:
        """ ConvertFromString(self: ValueSerializer, value: str, context: IValueSerializerContext) -> object """
        ...

    def ConvertToString(self, value:object, context:IValueSerializerContext) -> str:
        """ ConvertToString(self: ValueSerializer, value: object, context: IValueSerializerContext) -> str """
        ...

    def GetConvertFromException(self, *args): #cannot find CLR method
        """ GetConvertFromException(self: ValueSerializer, value: object) -> Exception """
        ...

    def GetConvertToException(self, *args): #cannot find CLR method
        """ GetConvertToException(self: ValueSerializer, value: object, destinationType: Type) -> Exception """
        ...

    @staticmethod
    def GetSerializerFor(*__args:Type) -> ValueSerializer:
        """
        GetSerializerFor(type: Type) -> ValueSerializer
        GetSerializerFor(descriptor: PropertyDescriptor) -> ValueSerializer
        GetSerializerFor(type: Type, context: IValueSerializerContext) -> ValueSerializer
        GetSerializerFor(descriptor: PropertyDescriptor, context: IValueSerializerContext) -> ValueSerializer
        """
        ...

    def TypeReferences(self, value:object, context:IValueSerializerContext) -> IEnumerable:
        """ TypeReferences(self: ValueSerializer, value: object, context: IValueSerializerContext) -> IEnumerable[Type] """
        ...


class DateTimeValueSerializer(ValueSerializer): # skipped bases: <type 'object'>
    """ DateTimeValueSerializer() """
    pass

class DependsOnAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DependsOnAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DependsOnAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class DictionaryKeyPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DictionaryKeyPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DictionaryKeyPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class IComponentConnector: # skipped bases: <type 'object'>
    """ no doc """
    def Connect(self, connectionId:int, target:object): # -> 
        """ Connect(self: IComponentConnector, connectionId: int, target: object) """
        ...

    def InitializeComponent(self): # -> 
        """ InitializeComponent(self: IComponentConnector) """
        ...


class INameScope: # skipped bases: <type 'object'>
    """ no doc """
    def FindName(self, name:str) -> object:
        """ FindName(self: INameScope, name: str) -> object """
        ...

    def RegisterName(self, name:str, scopedElement:object): # -> 
        """ RegisterName(self: INameScope, name: str, scopedElement: object) """
        ...

    def UnregisterName(self, name:str): # -> 
        """ UnregisterName(self: INameScope, name: str) """
        ...


class INameScopeDictionary(IDictionary, INameScope): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'ICollection[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class IProvideValueTarget: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TargetObject(self) -> object:
        """ Get: TargetObject(self: IProvideValueTarget) -> object """
        ...

    @property
    def TargetProperty(self) -> object:
        """ Get: TargetProperty(self: IProvideValueTarget) -> object """
        ...



class IQueryAmbient: # skipped bases: <type 'object'>
    """ no doc """
    def IsAmbientPropertyAvailable(self, propertyName:str) -> bool:
        """ IsAmbientPropertyAvailable(self: IQueryAmbient, propertyName: str) -> bool """
        ...


class IUriContext: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: IUriContext) -> Uri
        Set: BaseUri(self: IUriContext) = value
        """
        ...



class IValueSerializerContext(ITypeDescriptorContext): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ no doc """
    def GetValueSerializerFor(self, *__args:Type) -> ValueSerializer:
        """
        GetValueSerializerFor(self: IValueSerializerContext, type: Type) -> ValueSerializer
        GetValueSerializerFor(self: IValueSerializerContext, descriptor: PropertyDescriptor) -> ValueSerializer
        """
        ...


class IXamlTypeResolver: # skipped bases: <type 'object'>
    """ no doc """
    def Resolve(self, qualifiedTypeName:str) -> Type:
        """ Resolve(self: IXamlTypeResolver, qualifiedTypeName: str) -> Type """
        ...


class MarkupExtensionBracketCharactersAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MarkupExtensionBracketCharactersAttribute(openingBracket: Char, closingBracket: Char) """
    @property
    def ClosingBracket(self) -> Char:
        """ Get: ClosingBracket(self: MarkupExtensionBracketCharactersAttribute) -> Char """
        ...

    @property
    def OpeningBracket(self) -> Char:
        """ Get: OpeningBracket(self: MarkupExtensionBracketCharactersAttribute) -> Char """
        ...


    def __new__(cls, openingBracket:Char, closingBracket:Char) -> Self:
        """ __new__(cls: type, openingBracket: Char, closingBracket: Char) """
        ...


class MarkupExtensionReturnTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    MarkupExtensionReturnTypeAttribute(returnType: Type)
    MarkupExtensionReturnTypeAttribute(returnType: Type, expressionType: Type)
    MarkupExtensionReturnTypeAttribute()
    """
    @property
    def ExpressionType(self) -> Type:
        """ Get: ExpressionType(self: MarkupExtensionReturnTypeAttribute) -> Type """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: MarkupExtensionReturnTypeAttribute) -> Type """
        ...


    def __new__(cls, returnType:Type = ..., expressionType:Type = ...) -> Self:
        """
        __new__(cls: type, returnType: Type)
        __new__(cls: type, returnType: Type, expressionType: Type)
        __new__(cls: type)
        """
        ...


class MemberDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: MemberDefinition) -> str
        Set: Name(self: MemberDefinition) = value
        """
        ...



class NameReferenceConverter(TypeConverter): # skipped bases: <type 'object'>
    """ NameReferenceConverter() """
    pass

class NameScopePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    NameScopePropertyAttribute(name: str)
    NameScopePropertyAttribute(name: str, type: Type)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NameScopePropertyAttribute) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: NameScopePropertyAttribute) -> Type """
        ...


    def __new__(cls, name:str, type:Type = ...) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, type: Type)
        """
        ...


class NullExtension(MarkupExtension): # skipped bases: <type 'object'>
    """ NullExtension() """
    pass

class PropertyDefinition(MemberDefinition): # skipped bases: <type 'object'>
    """ PropertyDefinition() """
    @property
    def Attributes(self) -> IList:
        """ Get: Attributes(self: PropertyDefinition) -> IList[Attribute] """
        ...

    @property
    def Modifier(self) -> str:
        """
        Get: Modifier(self: PropertyDefinition) -> str
        Set: Modifier(self: PropertyDefinition) = value
        """
        ...

    @property
    def Type(self) -> XamlType:
        """
        Get: Type(self: PropertyDefinition) -> XamlType
        Set: Type(self: PropertyDefinition) = value
        """
        ...



class Reference(MarkupExtension): # skipped bases: <type 'object'>
    """
    Reference()
    Reference(name: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: Reference) -> str
        Set: Name(self: Reference) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class RootNamespaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RootNamespaceAttribute(nameSpace: str) """
    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: RootNamespaceAttribute) -> str """
        ...


    def __new__(cls, nameSpace:str) -> Self:
        """ __new__(cls: type, nameSpace: str) """
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


class StaticExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    StaticExtension()
    StaticExtension(member: str)
    """
    @property
    def Member(self) -> str:
        """
        Get: Member(self: StaticExtension) -> str
        Set: Member(self: StaticExtension) = value
        """
        ...

    @property
    def MemberType(self) -> Type:
        """
        Get: MemberType(self: StaticExtension) -> Type
        Set: MemberType(self: StaticExtension) = value
        """
        ...


    def __new__(cls, member:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, member: str)
        """
        ...


class TrimSurroundingWhitespaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TrimSurroundingWhitespaceAttribute() """
    pass

class TypeExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    TypeExtension()
    TypeExtension(typeName: str)
    TypeExtension(type: Type)
    """
    @property
    def Type(self) -> Type:
        """
        Get: Type(self: TypeExtension) -> Type
        Set: Type(self: TypeExtension) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: TypeExtension) -> str
        Set: TypeName(self: TypeExtension) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, type: Type)
        """
        ...


class UidPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UidPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: UidPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class UsableDuringInitializationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UsableDuringInitializationAttribute(usable: bool) """
    @property
    def Usable(self) -> bool:
        """ Get: Usable(self: UsableDuringInitializationAttribute) -> bool """
        ...


    def __new__(cls, usable:bool) -> Self:
        """ __new__(cls: type, usable: bool) """
        ...


class ValueSerializerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ValueSerializerAttribute(valueSerializerType: Type)
    ValueSerializerAttribute(valueSerializerTypeName: str)
    """
    @property
    def ValueSerializerType(self) -> Type:
        """ Get: ValueSerializerType(self: ValueSerializerAttribute) -> Type """
        ...

    @property
    def ValueSerializerTypeName(self) -> str:
        """ Get: ValueSerializerTypeName(self: ValueSerializerAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, valueSerializerType: Type)
        __new__(cls: type, valueSerializerTypeName: str)
        """
        ...


class WhitespaceSignificantCollectionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WhitespaceSignificantCollectionAttribute() """
    pass

class XamlDeferLoadAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XamlDeferLoadAttribute(loaderType: Type, contentType: Type)
    XamlDeferLoadAttribute(loaderType: str, contentType: str)
    """
    @property
    def ContentType(self) -> Type:
        """ Get: ContentType(self: XamlDeferLoadAttribute) -> Type """
        ...

    @property
    def ContentTypeName(self) -> str:
        """ Get: ContentTypeName(self: XamlDeferLoadAttribute) -> str """
        ...

    @property
    def LoaderType(self) -> Type:
        """ Get: LoaderType(self: XamlDeferLoadAttribute) -> Type """
        ...

    @property
    def LoaderTypeName(self) -> str:
        """ Get: LoaderTypeName(self: XamlDeferLoadAttribute) -> str """
        ...


    def __new__(cls, loaderType:Type, contentType:Type) -> Self:
        """
        __new__(cls: type, loaderType: Type, contentType: Type)
        __new__(cls: type, loaderType: str, contentType: str)
        """
        ...


class XamlSetMarkupExtensionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XamlSetMarkupExtensionAttribute(xamlSetMarkupExtensionHandler: str) """
    @property
    def XamlSetMarkupExtensionHandler(self) -> str:
        """ Get: XamlSetMarkupExtensionHandler(self: XamlSetMarkupExtensionAttribute) -> str """
        ...


    def __new__(cls, xamlSetMarkupExtensionHandler:str) -> Self:
        """ __new__(cls: type, xamlSetMarkupExtensionHandler: str) """
        ...


class XamlSetValueEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ XamlSetValueEventArgs(member: XamlMember, value: object) """
    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: XamlSetValueEventArgs) -> bool
        Set: Handled(self: XamlSetValueEventArgs) = value
        """
        ...

    @property
    def Member(self) -> XamlMember:
        """ Get: Member(self: XamlSetValueEventArgs) -> XamlMember """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: XamlSetValueEventArgs) -> object """
        ...


    def CallBase(self): # -> 
        """ CallBase(self: XamlSetValueEventArgs) """
        ...

    def __new__(cls, member:XamlMember, value:object) -> Self:
        """ __new__(cls: type, member: XamlMember, value: object) """
        ...


class XamlSetMarkupExtensionEventArgs(XamlSetValueEventArgs): # skipped bases: <type 'object'>
    """ XamlSetMarkupExtensionEventArgs(member: XamlMember, value: MarkupExtension, serviceProvider: IServiceProvider) """
    @property
    def MarkupExtension(self) -> MarkupExtension:
        """ Get: MarkupExtension(self: XamlSetMarkupExtensionEventArgs) -> MarkupExtension """
        ...

    @property
    def ServiceProvider(self) -> IServiceProvider:
        """ Get: ServiceProvider(self: XamlSetMarkupExtensionEventArgs) -> IServiceProvider """
        ...



class XamlSetTypeConverterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XamlSetTypeConverterAttribute(xamlSetTypeConverterHandler: str) """
    @property
    def XamlSetTypeConverterHandler(self) -> str:
        """ Get: XamlSetTypeConverterHandler(self: XamlSetTypeConverterAttribute) -> str """
        ...


    def __new__(cls, xamlSetTypeConverterHandler:str) -> Self:
        """ __new__(cls: type, xamlSetTypeConverterHandler: str) """
        ...


class XamlSetTypeConverterEventArgs(XamlSetValueEventArgs): # skipped bases: <type 'object'>
    """ XamlSetTypeConverterEventArgs(member: XamlMember, typeConverter: TypeConverter, value: object, serviceProvider: ITypeDescriptorContext, cultureInfo: CultureInfo) """
    @property
    def CultureInfo(self) -> CultureInfo:
        """ Get: CultureInfo(self: XamlSetTypeConverterEventArgs) -> CultureInfo """
        ...

    @property
    def ServiceProvider(self) -> ITypeDescriptorContext:
        """ Get: ServiceProvider(self: XamlSetTypeConverterEventArgs) -> ITypeDescriptorContext """
        ...

    @property
    def TypeConverter(self) -> TypeConverter:
        """ Get: TypeConverter(self: XamlSetTypeConverterEventArgs) -> TypeConverter """
        ...



class XData: # skipped bases: <type 'object'>, <type 'object'>
    """ XData() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: XData) -> str
        Set: Text(self: XData) = value
        """
        ...

    @property
    def XmlReader(self) -> object:
        """
        Get: XmlReader(self: XData) -> object
        Set: XmlReader(self: XData) = value
        """
        ...



class XmlLangPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlLangPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlLangPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class XmlnsCompatibleWithAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlnsCompatibleWithAttribute(oldNamespace: str, newNamespace: str) """
    @property
    def NewNamespace(self) -> str:
        """ Get: NewNamespace(self: XmlnsCompatibleWithAttribute) -> str """
        ...

    @property
    def OldNamespace(self) -> str:
        """ Get: OldNamespace(self: XmlnsCompatibleWithAttribute) -> str """
        ...


    def __new__(cls, oldNamespace:str, newNamespace:str) -> Self:
        """ __new__(cls: type, oldNamespace: str, newNamespace: str) """
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


