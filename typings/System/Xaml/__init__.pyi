# encoding: utf-8
# module System.Xaml calls itself Xaml
# from System.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Xaml.Hosting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Enum, EventArgs, EventHandler, IDisposable, 
    IEquatable, IServiceProvider, Type, Uri)

from System.Collections import ICollection, IEnumerable, IList

from System.Collections.Generic import IReadOnlyDictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import DesignerSerializationVisibility

from System.IO import Stream

from System.Reflection import Assembly, MemberInfo

from System.Windows.Markup import INameScope

from System.Xaml.Permissions import XamlAccessLevel

from System.Xaml.Schema import (AllowedMemberLocations, XamlMemberInvoker, 
    XamlTypeInvoker, XamlTypeName, XamlValueConverter)

from System.Xml import XmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, IAddLineInfo, 
    ICheckIfInitialized, T, field#)
"""

# no functions
# classes

class AmbientPropertyValue: # skipped bases: <type 'object'>, <type 'object'>
    """ AmbientPropertyValue(property: XamlMember, value: object) """
    @property
    def RetrievedProperty(self) -> XamlMember:
        """ Get: RetrievedProperty(self: AmbientPropertyValue) -> XamlMember """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: AmbientPropertyValue) -> object """
        ...



class AttachableMemberIdentifier(IEquatable): # skipped bases: <type 'object'>
    """ AttachableMemberIdentifier(declaringType: Type, memberName: str) """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: AttachableMemberIdentifier) -> Type """
        ...

    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: AttachableMemberIdentifier) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: AttachableMemberIdentifier) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: AttachableMemberIdentifier) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AttachablePropertyServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CopyPropertiesTo(instance:object, array:Array, index:int): # -> 
        """ CopyPropertiesTo(instance: object, array: Array[KeyValuePair[AttachableMemberIdentifier, object]], index: int) """
        ...

    @staticmethod
    def GetAttachedPropertyCount(instance:object) -> int:
        """ GetAttachedPropertyCount(instance: object) -> int """
        ...

    @staticmethod
    def RemoveProperty(instance:object, name:AttachableMemberIdentifier) -> bool:
        """ RemoveProperty(instance: object, name: AttachableMemberIdentifier) -> bool """
        ...

    @staticmethod
    def SetProperty(instance:object, name:AttachableMemberIdentifier, value:object): # -> 
        """ SetProperty(instance: object, name: AttachableMemberIdentifier, value: object) """
        ...

    @staticmethod
    def TryGetProperty(instance, name, value): # -> Tuple_[bool, T]
        """
        TryGetProperty[T](instance: object, name: AttachableMemberIdentifier) -> (bool, T)
        TryGetProperty(instance: object, name: AttachableMemberIdentifier) -> (bool, object)
        """
        ...

    __all__: list = ...


class IAmbientProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetAllAmbientValues(self, *__args:Array) -> IEnumerable:
        """
        GetAllAmbientValues(self: IAmbientProvider, ceilingTypes: IEnumerable[XamlType], *properties: Array[XamlMember]) -> IEnumerable[AmbientPropertyValue]
        GetAllAmbientValues(self: IAmbientProvider, *types: Array[XamlType]) -> IEnumerable[object]
        GetAllAmbientValues(self: IAmbientProvider, ceilingTypes: IEnumerable[XamlType], searchLiveStackOnly: bool, types: IEnumerable[XamlType], *properties: Array[XamlMember]) -> IEnumerable[AmbientPropertyValue]
        """
        ...

    def GetFirstAmbientValue(self, *__args:Array) -> object:
        """
        GetFirstAmbientValue(self: IAmbientProvider, ceilingTypes: IEnumerable[XamlType], *properties: Array[XamlMember]) -> AmbientPropertyValue
        GetFirstAmbientValue(self: IAmbientProvider, *types: Array[XamlType]) -> object
        """
        ...


class IAttachedPropertyStore: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PropertyCount(self) -> int:
        """ Get: PropertyCount(self: IAttachedPropertyStore) -> int """
        ...


    def CopyPropertiesTo(self, array:Array, index:int): # -> 
        """ CopyPropertiesTo(self: IAttachedPropertyStore, array: Array[KeyValuePair[AttachableMemberIdentifier, object]], index: int) """
        ...

    def RemoveProperty(self, attachableMemberIdentifier:AttachableMemberIdentifier) -> bool:
        """ RemoveProperty(self: IAttachedPropertyStore, attachableMemberIdentifier: AttachableMemberIdentifier) -> bool """
        ...

    def SetProperty(self, attachableMemberIdentifier:AttachableMemberIdentifier, value:object): # -> 
        """ SetProperty(self: IAttachedPropertyStore, attachableMemberIdentifier: AttachableMemberIdentifier, value: object) """
        ...

    def TryGetProperty(self, attachableMemberIdentifier, value) -> Tuple_[bool, object]:
        """ TryGetProperty(self: IAttachedPropertyStore, attachableMemberIdentifier: AttachableMemberIdentifier) -> (bool, object) """
        ...


class IDestinationTypeProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetDestinationType(self) -> Type:
        """ GetDestinationType(self: IDestinationTypeProvider) -> Type """
        ...


class INamespacePrefixLookup: # skipped bases: <type 'object'>
    """ no doc """
    def LookupPrefix(self, ns:str) -> str:
        """ LookupPrefix(self: INamespacePrefixLookup, ns: str) -> str """
        ...


class IRootObjectProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RootObject(self) -> object:
        """ Get: RootObject(self: IRootObjectProvider) -> object """
        ...



class IXamlIndexingReader: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IXamlIndexingReader) -> int """
        ...

    @property
    def CurrentIndex(self) -> int:
        """
        Get: CurrentIndex(self: IXamlIndexingReader) -> int
        Set: CurrentIndex(self: IXamlIndexingReader) = value
        """
        ...



class IXamlLineInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasLineInfo(self) -> bool:
        """ Get: HasLineInfo(self: IXamlLineInfo) -> bool """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: IXamlLineInfo) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: IXamlLineInfo) -> int """
        ...



class IXamlLineInfoConsumer: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ShouldProvideLineInfo(self) -> bool:
        """ Get: ShouldProvideLineInfo(self: IXamlLineInfoConsumer) -> bool """
        ...


    def SetLineInfo(self, lineNumber:int, linePosition:int): # -> 
        """ SetLineInfo(self: IXamlLineInfoConsumer, lineNumber: int, linePosition: int) """
        ...


class IXamlNameProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetName(self, value:object) -> str:
        """ GetName(self: IXamlNameProvider, value: object) -> str """
        ...


class IXamlNameResolver: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsFixupTokenAvailable(self) -> bool:
        """ Get: IsFixupTokenAvailable(self: IXamlNameResolver) -> bool """
        ...


    def GetAllNamesAndValuesInScope(self) -> IEnumerable:
        """ GetAllNamesAndValuesInScope(self: IXamlNameResolver) -> IEnumerable[KeyValuePair[str, object]] """
        ...

    def GetFixupToken(self, names:IEnumerable, canAssignDirectly:bool = ...) -> object:
        """
        GetFixupToken(self: IXamlNameResolver, names: IEnumerable[str]) -> object
        GetFixupToken(self: IXamlNameResolver, names: IEnumerable[str], canAssignDirectly: bool) -> object
        """
        ...

    def Resolve(self, name, isFullyInitialized=None) -> object:
        """
        Resolve(self: IXamlNameResolver, name: str) -> object
        Resolve(self: IXamlNameResolver, name: str) -> (object, bool)
        """
        ...

    OnNameScopeInitializationComplete = ...


class IXamlNamespaceResolver: # skipped bases: <type 'object'>
    """ no doc """
    def GetNamespace(self, prefix:str) -> str:
        """ GetNamespace(self: IXamlNamespaceResolver, prefix: str) -> str """
        ...

    def GetNamespacePrefixes(self) -> IEnumerable:
        """ GetNamespacePrefixes(self: IXamlNamespaceResolver) -> IEnumerable[NamespaceDeclaration] """
        ...


class IXamlObjectWriterFactory: # skipped bases: <type 'object'>
    """ no doc """
    def GetParentSettings(self) -> XamlObjectWriterSettings:
        """ GetParentSettings(self: IXamlObjectWriterFactory) -> XamlObjectWriterSettings """
        ...

    def GetXamlObjectWriter(self, settings:XamlObjectWriterSettings) -> XamlObjectWriter:
        """ GetXamlObjectWriter(self: IXamlObjectWriterFactory, settings: XamlObjectWriterSettings) -> XamlObjectWriter """
        ...


class IXamlSchemaContextProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SchemaContext(self) -> XamlSchemaContext:
        """ Get: SchemaContext(self: IXamlSchemaContextProvider) -> XamlSchemaContext """
        ...



class NamespaceDeclaration: # skipped bases: <type 'object'>, <type 'object'>
    """ NamespaceDeclaration(ns: str, prefix: str) """
    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: NamespaceDeclaration) -> str """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: NamespaceDeclaration) -> str """
        ...



class XamlReader(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDisposed(self):
        ...

    @property
    def IsEof(self) -> bool:
        """ Get: IsEof(self: XamlReader) -> bool """
        ...

    @property
    def Member(self) -> XamlMember:
        """ Get: Member(self: XamlReader) -> XamlMember """
        ...

    @property
    def Namespace(self) -> NamespaceDeclaration:
        """ Get: Namespace(self: XamlReader) -> NamespaceDeclaration """
        ...

    @property
    def NodeType(self) -> XamlNodeType:
        """ Get: NodeType(self: XamlReader) -> XamlNodeType """
        ...

    @property
    def SchemaContext(self) -> XamlSchemaContext:
        """ Get: SchemaContext(self: XamlReader) -> XamlSchemaContext """
        ...

    @property
    def Type(self) -> XamlType:
        """ Get: Type(self: XamlReader) -> XamlType """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: XamlReader) -> object """
        ...


    def Close(self): # -> 
        """ Close(self: XamlReader) """
        ...

    def Read(self) -> bool:
        """ Read(self: XamlReader) -> bool """
        ...

    def ReadSubtree(self) -> XamlReader:
        """ ReadSubtree(self: XamlReader) -> XamlReader """
        ...

    def Skip(self): # -> 
        """ Skip(self: XamlReader) """
        ...


class XamlBackgroundReader(XamlReader, IXamlLineInfo): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ XamlBackgroundReader(wrappedReader: XamlReader) """
    def StartThread(self, threadName:str = ...): # -> 
        """ StartThread(self: XamlBackgroundReader)StartThread(self: XamlBackgroundReader, threadName: str) """
        ...

    def __new__(cls, wrappedReader:XamlReader) -> Self:
        """ __new__(cls: type, wrappedReader: XamlReader) """
        ...


class XamlDeferringLoader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Load(self, xamlReader:XamlReader, serviceProvider:IServiceProvider) -> object:
        """ Load(self: XamlDeferringLoader, xamlReader: XamlReader, serviceProvider: IServiceProvider) -> object """
        ...

    def Save(self, value:object, serviceProvider:IServiceProvider) -> XamlReader:
        """ Save(self: XamlDeferringLoader, value: object, serviceProvider: IServiceProvider) -> XamlReader """
        ...


class XamlMember(IEquatable): # skipped bases: <type 'object'>
    """
    XamlMember(name: str, declaringType: XamlType, isAttachable: bool)
    XamlMember(propertyInfo: PropertyInfo, schemaContext: XamlSchemaContext)
    XamlMember(propertyInfo: PropertyInfo, schemaContext: XamlSchemaContext, invoker: XamlMemberInvoker)
    XamlMember(eventInfo: EventInfo, schemaContext: XamlSchemaContext)
    XamlMember(eventInfo: EventInfo, schemaContext: XamlSchemaContext, invoker: XamlMemberInvoker)
    XamlMember(attachablePropertyName: str, getter: MethodInfo, setter: MethodInfo, schemaContext: XamlSchemaContext)
    XamlMember(attachablePropertyName: str, getter: MethodInfo, setter: MethodInfo, schemaContext: XamlSchemaContext, invoker: XamlMemberInvoker)
    XamlMember(attachableEventName: str, adder: MethodInfo, schemaContext: XamlSchemaContext)
    XamlMember(attachableEventName: str, adder: MethodInfo, schemaContext: XamlSchemaContext, invoker: XamlMemberInvoker)
    """
    @property
    def DeclaringType(self) -> XamlType:
        """ Get: DeclaringType(self: XamlMember) -> XamlType """
        ...

    @property
    def DeferringLoader(self) -> XamlValueConverter:
        """ Get: DeferringLoader(self: XamlMember) -> XamlValueConverter[XamlDeferringLoader] """
        ...

    @property
    def DependsOn(self) -> IList:
        """ Get: DependsOn(self: XamlMember) -> IList[XamlMember] """
        ...

    @property
    def Invoker(self) -> XamlMemberInvoker:
        """ Get: Invoker(self: XamlMember) -> XamlMemberInvoker """
        ...

    @property
    def IsAmbient(self) -> bool:
        """ Get: IsAmbient(self: XamlMember) -> bool """
        ...

    @property
    def IsAttachable(self) -> bool:
        """ Get: IsAttachable(self: XamlMember) -> bool """
        ...

    @property
    def IsDirective(self) -> bool:
        """ Get: IsDirective(self: XamlMember) -> bool """
        ...

    @property
    def IsEvent(self) -> bool:
        """ Get: IsEvent(self: XamlMember) -> bool """
        ...

    @property
    def IsNameValid(self) -> bool:
        """ Get: IsNameValid(self: XamlMember) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: XamlMember) -> bool """
        ...

    @property
    def IsReadPublic(self) -> bool:
        """ Get: IsReadPublic(self: XamlMember) -> bool """
        ...

    @property
    def IsUnknown(self) -> bool:
        """ Get: IsUnknown(self: XamlMember) -> bool """
        ...

    @property
    def IsWriteOnly(self) -> bool:
        """ Get: IsWriteOnly(self: XamlMember) -> bool """
        ...

    @property
    def IsWritePublic(self) -> bool:
        """ Get: IsWritePublic(self: XamlMember) -> bool """
        ...

    @property
    def MarkupExtensionBracketCharacters(self) -> IReadOnlyDictionary:
        """ Get: MarkupExtensionBracketCharacters(self: XamlMember) -> IReadOnlyDictionary[Char, Char] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XamlMember) -> str """
        ...

    @property
    def PreferredXamlNamespace(self) -> str:
        """ Get: PreferredXamlNamespace(self: XamlMember) -> str """
        ...

    @property
    def SerializationVisibility(self) -> DesignerSerializationVisibility:
        """ Get: SerializationVisibility(self: XamlMember) -> DesignerSerializationVisibility """
        ...

    @property
    def TargetType(self) -> XamlType:
        """ Get: TargetType(self: XamlMember) -> XamlType """
        ...

    @property
    def Type(self) -> XamlType:
        """ Get: Type(self: XamlMember) -> XamlType """
        ...

    @property
    def TypeConverter(self) -> XamlValueConverter:
        """ Get: TypeConverter(self: XamlMember) -> XamlValueConverter[TypeConverter] """
        ...

    @property
    def UnderlyingMember(self) -> MemberInfo:
        """ Get: UnderlyingMember(self: XamlMember) -> MemberInfo """
        ...

    @property
    def ValueSerializer(self) -> XamlValueConverter:
        """ Get: ValueSerializer(self: XamlMember) -> XamlValueConverter[ValueSerializer] """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: XamlMember) -> int """
        ...

    def GetXamlNamespaces(self) -> IList:
        """ GetXamlNamespaces(self: XamlMember) -> IList[str] """
        ...

    def LookupCustomAttributeProvider(self, *args): #cannot find CLR method
        """ LookupCustomAttributeProvider(self: XamlMember) -> ICustomAttributeProvider """
        ...

    def LookupDeferringLoader(self, *args): #cannot find CLR method
        """ LookupDeferringLoader(self: XamlMember) -> XamlValueConverter[XamlDeferringLoader] """
        ...

    def LookupDependsOn(self, *args): #cannot find CLR method
        """ LookupDependsOn(self: XamlMember) -> IList[XamlMember] """
        ...

    def LookupInvoker(self, *args): #cannot find CLR method
        """ LookupInvoker(self: XamlMember) -> XamlMemberInvoker """
        ...

    def LookupIsAmbient(self, *args): #cannot find CLR method
        """ LookupIsAmbient(self: XamlMember) -> bool """
        ...

    def LookupIsEvent(self, *args): #cannot find CLR method
        """ LookupIsEvent(self: XamlMember) -> bool """
        ...

    def LookupIsReadOnly(self, *args): #cannot find CLR method
        """ LookupIsReadOnly(self: XamlMember) -> bool """
        ...

    def LookupIsReadPublic(self, *args): #cannot find CLR method
        """ LookupIsReadPublic(self: XamlMember) -> bool """
        ...

    def LookupIsUnknown(self, *args): #cannot find CLR method
        """ LookupIsUnknown(self: XamlMember) -> bool """
        ...

    def LookupIsWriteOnly(self, *args): #cannot find CLR method
        """ LookupIsWriteOnly(self: XamlMember) -> bool """
        ...

    def LookupIsWritePublic(self, *args): #cannot find CLR method
        """ LookupIsWritePublic(self: XamlMember) -> bool """
        ...

    def LookupMarkupExtensionBracketCharacters(self, *args): #cannot find CLR method
        """ LookupMarkupExtensionBracketCharacters(self: XamlMember) -> IReadOnlyDictionary[Char, Char] """
        ...

    def LookupTargetType(self, *args): #cannot find CLR method
        """ LookupTargetType(self: XamlMember) -> XamlType """
        ...

    def LookupType(self, *args): #cannot find CLR method
        """ LookupType(self: XamlMember) -> XamlType """
        ...

    def LookupTypeConverter(self, *args): #cannot find CLR method
        """ LookupTypeConverter(self: XamlMember) -> XamlValueConverter[TypeConverter] """
        ...

    def LookupUnderlyingGetter(self, *args): #cannot find CLR method
        """ LookupUnderlyingGetter(self: XamlMember) -> MethodInfo """
        ...

    def LookupUnderlyingMember(self, *args): #cannot find CLR method
        """ LookupUnderlyingMember(self: XamlMember) -> MemberInfo """
        ...

    def LookupUnderlyingSetter(self, *args): #cannot find CLR method
        """ LookupUnderlyingSetter(self: XamlMember) -> MethodInfo """
        ...

    def LookupValueSerializer(self, *args): #cannot find CLR method
        """ LookupValueSerializer(self: XamlMember) -> XamlValueConverter[ValueSerializer] """
        ...

    def ToString(self) -> str:
        """ ToString(self: XamlMember) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class XamlDirective(XamlMember): # skipped bases: <type 'IEquatable[XamlMember]'>, <type 'object'>
    """
    XamlDirective(xamlNamespaces: IEnumerable[str], name: str, xamlType: XamlType, typeConverter: XamlValueConverter[TypeConverter], allowedLocation: AllowedMemberLocations)
    XamlDirective(xamlNamespace: str, name: str)
    """
    @property
    def AllowedLocation(self) -> AllowedMemberLocations:
        """ Get: AllowedLocation(self: XamlDirective) -> AllowedMemberLocations """
        ...



class XamlException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlException(message: str, innerException: Exception, lineNumber: int, linePosition: int)
    XamlException(message: str, innerException: Exception)
    XamlException()
    XamlException(message: str)
    """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XamlException) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XamlException) -> int """
        ...


    SerializeObjectState = ...


class XamlDuplicateMemberException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlDuplicateMemberException()
    XamlDuplicateMemberException(member: XamlMember, type: XamlType)
    XamlDuplicateMemberException(message: str)
    XamlDuplicateMemberException(message: str, innerException: Exception)
    """
    @property
    def DuplicateMember(self) -> XamlMember:
        """
        Get: DuplicateMember(self: XamlDuplicateMemberException) -> XamlMember
        Set: DuplicateMember(self: XamlDuplicateMemberException) = value
        """
        ...

    @property
    def ParentType(self) -> XamlType:
        """
        Get: ParentType(self: XamlDuplicateMemberException) -> XamlType
        Set: ParentType(self: XamlDuplicateMemberException) = value
        """
        ...


    SerializeObjectState = ...


class XamlInternalException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlInternalException()
    XamlInternalException(message: str)
    XamlInternalException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlLanguage: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllDirectives(self) -> ReadOnlyCollection:
        """ Get: AllDirectives() -> ReadOnlyCollection[XamlDirective] """
        ...

    @property
    def AllTypes(self) -> ReadOnlyCollection:
        """ Get: AllTypes() -> ReadOnlyCollection[XamlType] """
        ...

    @property
    def Arguments(self) -> XamlDirective:
        """ Get: Arguments() -> XamlDirective """
        ...

    @property
    def Array(self) -> XamlType:
        """ Get: Array() -> XamlType """
        ...

    @property
    def AsyncRecords(self) -> XamlDirective:
        """ Get: AsyncRecords() -> XamlDirective """
        ...

    @property
    def Base(self) -> XamlDirective:
        """ Get: Base() -> XamlDirective """
        ...

    @property
    def Boolean(self) -> XamlType:
        """ Get: Boolean() -> XamlType """
        ...

    @property
    def Byte(self) -> XamlType:
        """ Get: Byte() -> XamlType """
        ...

    @property
    def Char(self) -> XamlType:
        """ Get: Char() -> XamlType """
        ...

    @property
    def Class(self) -> XamlDirective:
        """ Get: Class() -> XamlDirective """
        ...

    @property
    def ClassAttributes(self) -> XamlDirective:
        """ Get: ClassAttributes() -> XamlDirective """
        ...

    @property
    def ClassModifier(self) -> XamlDirective:
        """ Get: ClassModifier() -> XamlDirective """
        ...

    @property
    def Code(self) -> XamlDirective:
        """ Get: Code() -> XamlDirective """
        ...

    @property
    def ConnectionId(self) -> XamlDirective:
        """ Get: ConnectionId() -> XamlDirective """
        ...

    @property
    def Decimal(self) -> XamlType:
        """ Get: Decimal() -> XamlType """
        ...

    @property
    def Double(self) -> XamlType:
        """ Get: Double() -> XamlType """
        ...

    @property
    def FactoryMethod(self) -> XamlDirective:
        """ Get: FactoryMethod() -> XamlDirective """
        ...

    @property
    def FieldModifier(self) -> XamlDirective:
        """ Get: FieldModifier() -> XamlDirective """
        ...

    @property
    def Initialization(self) -> XamlDirective:
        """ Get: Initialization() -> XamlDirective """
        ...

    @property
    def Int16(self) -> XamlType:
        """ Get: Int16() -> XamlType """
        ...

    @property
    def Int32(self) -> XamlType:
        """ Get: Int32() -> XamlType """
        ...

    @property
    def Int64(self) -> XamlType:
        """ Get: Int64() -> XamlType """
        ...

    @property
    def Items(self) -> XamlDirective:
        """ Get: Items() -> XamlDirective """
        ...

    @property
    def Key(self) -> XamlDirective:
        """ Get: Key() -> XamlDirective """
        ...

    @property
    def Lang(self) -> XamlDirective:
        """ Get: Lang() -> XamlDirective """
        ...

    @property
    def Member(self) -> XamlType:
        """ Get: Member() -> XamlType """
        ...

    @property
    def Members(self) -> XamlDirective:
        """ Get: Members() -> XamlDirective """
        ...

    @property
    def Name(self) -> XamlDirective:
        """ Get: Name() -> XamlDirective """
        ...

    @property
    def Null(self) -> XamlType:
        """ Get: Null() -> XamlType """
        ...

    @property
    def Object(self) -> XamlType:
        """ Get: Object() -> XamlType """
        ...

    @property
    def PositionalParameters(self) -> XamlDirective:
        """ Get: PositionalParameters() -> XamlDirective """
        ...

    @property
    def Property(self) -> XamlType:
        """ Get: Property() -> XamlType """
        ...

    @property
    def Reference(self) -> XamlType:
        """ Get: Reference() -> XamlType """
        ...

    @property
    def Shared(self) -> XamlDirective:
        """ Get: Shared() -> XamlDirective """
        ...

    @property
    def Single(self) -> XamlType:
        """ Get: Single() -> XamlType """
        ...

    @property
    def Space(self) -> XamlDirective:
        """ Get: Space() -> XamlDirective """
        ...

    @property
    def Static(self) -> XamlType:
        """ Get: Static() -> XamlType """
        ...

    @property
    def String(self) -> XamlType:
        """ Get: String() -> XamlType """
        ...

    @property
    def Subclass(self) -> XamlDirective:
        """ Get: Subclass() -> XamlDirective """
        ...

    @property
    def SynchronousMode(self) -> XamlDirective:
        """ Get: SynchronousMode() -> XamlDirective """
        ...

    @property
    def TimeSpan(self) -> XamlType:
        """ Get: TimeSpan() -> XamlType """
        ...

    @property
    def Type(self) -> XamlType:
        """ Get: Type() -> XamlType """
        ...

    @property
    def TypeArguments(self) -> XamlDirective:
        """ Get: TypeArguments() -> XamlDirective """
        ...

    @property
    def Uid(self) -> XamlDirective:
        """ Get: Uid() -> XamlDirective """
        ...

    @property
    def UnknownContent(self) -> XamlDirective:
        """ Get: UnknownContent() -> XamlDirective """
        ...

    @property
    def Uri(self) -> XamlType:
        """ Get: Uri() -> XamlType """
        ...

    @property
    def XamlNamespaces(self) -> IList:
        """ Get: XamlNamespaces() -> IList[str] """
        ...

    @property
    def XData(self) -> XamlType:
        """ Get: XData() -> XamlType """
        ...

    @property
    def XmlNamespaces(self) -> IList:
        """ Get: XmlNamespaces() -> IList[str] """
        ...


    Xaml2006Namespace: str = ...
    Xml1998Namespace: str = ...
    __all__: list = ...


class XamlNodeList: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlNodeList(schemaContext: XamlSchemaContext)
    XamlNodeList(schemaContext: XamlSchemaContext, size: int)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XamlNodeList) -> int """
        ...

    @property
    def Writer(self) -> XamlWriter:
        """ Get: Writer(self: XamlNodeList) -> XamlWriter """
        ...


    def Clear(self): # -> 
        """ Clear(self: XamlNodeList) """
        ...

    def GetReader(self) -> XamlReader:
        """ GetReader(self: XamlNodeList) -> XamlReader """
        ...


class XamlNodeQueue: # skipped bases: <type 'object'>, <type 'object'>
    """ XamlNodeQueue(schemaContext: XamlSchemaContext) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XamlNodeQueue) -> int """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: XamlNodeQueue) -> bool """
        ...

    @property
    def Reader(self) -> XamlReader:
        """ Get: Reader(self: XamlNodeQueue) -> XamlReader """
        ...

    @property
    def Writer(self) -> XamlWriter:
        """ Get: Writer(self: XamlNodeQueue) -> XamlWriter """
        ...



class XamlNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XamlNodeType, values: EndMember (5), EndObject (3), GetObject (2), NamespaceDeclaration (7), None (0), StartMember (4), StartObject (1), Value (6) """
    EndMember: XamlNodeType = ...
    EndObject: XamlNodeType = ...
    GetObject: XamlNodeType = ...
    NamespaceDeclaration: XamlNodeType = ...
    StartMember: XamlNodeType = ...
    StartObject: XamlNodeType = ...
    Value: XamlNodeType = ...
    value__ = ...


class XamlObjectEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ XamlObjectEventArgs(instance: object) """
    @property
    def ElementLineNumber(self) -> int:
        """ Get: ElementLineNumber(self: XamlObjectEventArgs) -> int """
        ...

    @property
    def ElementLinePosition(self) -> int:
        """ Get: ElementLinePosition(self: XamlObjectEventArgs) -> int """
        ...

    @property
    def Instance(self) -> object:
        """ Get: Instance(self: XamlObjectEventArgs) -> object """
        ...

    @property
    def SourceBamlUri(self) -> Uri:
        """ Get: SourceBamlUri(self: XamlObjectEventArgs) -> Uri """
        ...


    def __new__(cls, instance:object) -> Self:
        """ __new__(cls: type, instance: object) """
        ...


class XamlObjectReader(XamlReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XamlObjectReader(instance: object)
    XamlObjectReader(instance: object, settings: XamlObjectReaderSettings)
    XamlObjectReader(instance: object, schemaContext: XamlSchemaContext)
    XamlObjectReader(instance: object, schemaContext: XamlSchemaContext, settings: XamlObjectReaderSettings)
    """
    @property
    def Instance(self) -> object:
        """ Get: Instance(self: XamlObjectReader) -> object """
        ...


    def __new__(cls, instance:object, *__args:XamlObjectReaderSettings) -> Self:
        """
        __new__(cls: type, instance: object)
        __new__(cls: type, instance: object, settings: XamlObjectReaderSettings)
        __new__(cls: type, instance: object, schemaContext: XamlSchemaContext)
        __new__(cls: type, instance: object, schemaContext: XamlSchemaContext, settings: XamlObjectReaderSettings)
        """
        ...


class XamlObjectReaderException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlObjectReaderException()
    XamlObjectReaderException(message: str)
    XamlObjectReaderException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlReaderSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlReaderSettings()
    XamlReaderSettings(settings: XamlReaderSettings)
    """
    @property
    def AllowProtectedMembersOnRoot(self) -> bool:
        """
        Get: AllowProtectedMembersOnRoot(self: XamlReaderSettings) -> bool
        Set: AllowProtectedMembersOnRoot(self: XamlReaderSettings) = value
        """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: XamlReaderSettings) -> Uri
        Set: BaseUri(self: XamlReaderSettings) = value
        """
        ...

    @property
    def IgnoreUidsOnPropertyElements(self) -> bool:
        """
        Get: IgnoreUidsOnPropertyElements(self: XamlReaderSettings) -> bool
        Set: IgnoreUidsOnPropertyElements(self: XamlReaderSettings) = value
        """
        ...

    @property
    def LocalAssembly(self) -> Assembly:
        """
        Get: LocalAssembly(self: XamlReaderSettings) -> Assembly
        Set: LocalAssembly(self: XamlReaderSettings) = value
        """
        ...

    @property
    def ProvideLineInfo(self) -> bool:
        """
        Get: ProvideLineInfo(self: XamlReaderSettings) -> bool
        Set: ProvideLineInfo(self: XamlReaderSettings) = value
        """
        ...

    @property
    def ValuesMustBeString(self) -> bool:
        """
        Get: ValuesMustBeString(self: XamlReaderSettings) -> bool
        Set: ValuesMustBeString(self: XamlReaderSettings) = value
        """
        ...



class XamlObjectReaderSettings(XamlReaderSettings): # skipped bases: <type 'object'>
    """ XamlObjectReaderSettings() """
    @property
    def RequireExplicitContentVisibility(self) -> bool:
        """
        Get: RequireExplicitContentVisibility(self: XamlObjectReaderSettings) -> bool
        Set: RequireExplicitContentVisibility(self: XamlObjectReaderSettings) = value
        """
        ...



class XamlWriter(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDisposed(self):
        ...

    @property
    def SchemaContext(self) -> XamlSchemaContext:
        """ Get: SchemaContext(self: XamlWriter) -> XamlSchemaContext """
        ...


    def Close(self): # -> 
        """ Close(self: XamlWriter) """
        ...

    def WriteEndMember(self): # -> 
        """ WriteEndMember(self: XamlWriter) """
        ...

    def WriteEndObject(self): # -> 
        """ WriteEndObject(self: XamlWriter) """
        ...

    def WriteGetObject(self): # -> 
        """ WriteGetObject(self: XamlWriter) """
        ...

    def WriteNamespace(self, namespaceDeclaration:NamespaceDeclaration): # -> 
        """ WriteNamespace(self: XamlWriter, namespaceDeclaration: NamespaceDeclaration) """
        ...

    def WriteNode(self, reader:XamlReader): # -> 
        """ WriteNode(self: XamlWriter, reader: XamlReader) """
        ...

    def WriteStartMember(self, xamlMember:XamlMember): # -> 
        """ WriteStartMember(self: XamlWriter, xamlMember: XamlMember) """
        ...

    def WriteStartObject(self, type:XamlType): # -> 
        """ WriteStartObject(self: XamlWriter, type: XamlType) """
        ...

    def WriteValue(self, value:object): # -> 
        """ WriteValue(self: XamlWriter, value: object) """
        ...


class XamlObjectWriter(IXamlLineInfoConsumer, ICheckIfInitialized, IAddLineInfo, XamlWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XamlObjectWriter(schemaContext: XamlSchemaContext)
    XamlObjectWriter(schemaContext: XamlSchemaContext, settings: XamlObjectWriterSettings)
    """
    @property
    def Result(self) -> object:
        """ Get: Result(self: XamlObjectWriter) -> object """
        ...

    @property
    def RootNameScope(self) -> INameScope:
        """ Get: RootNameScope(self: XamlObjectWriter) -> INameScope """
        ...


    def Clear(self): # -> 
        """ Clear(self: XamlObjectWriter) """
        ...

    def OnAfterBeginInit(self, *args): #cannot find CLR method
        """ OnAfterBeginInit(self: XamlObjectWriter, value: object) """
        ...

    def OnAfterEndInit(self, *args): #cannot find CLR method
        """ OnAfterEndInit(self: XamlObjectWriter, value: object) """
        ...

    def OnAfterProperties(self, *args): #cannot find CLR method
        """ OnAfterProperties(self: XamlObjectWriter, value: object) """
        ...

    def OnBeforeProperties(self, *args): #cannot find CLR method
        """ OnBeforeProperties(self: XamlObjectWriter, value: object) """
        ...

    def OnSetValue(self, *args): #cannot find CLR method
        """ OnSetValue(self: XamlObjectWriter, eventSender: object, member: XamlMember, value: object) -> bool """
        ...

    def __new__(cls, schemaContext:XamlSchemaContext, settings:XamlObjectWriterSettings = ...) -> Self:
        """
        __new__(cls: type, schemaContext: XamlSchemaContext)
        __new__(cls: type, schemaContext: XamlSchemaContext, settings: XamlObjectWriterSettings)
        """
        ...


class XamlObjectWriterException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlObjectWriterException()
    XamlObjectWriterException(message: str)
    XamlObjectWriterException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlWriterSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlWriterSettings()
    XamlWriterSettings(settings: XamlWriterSettings)
    """
    pass

class XamlObjectWriterSettings(XamlWriterSettings): # skipped bases: <type 'object'>
    """
    XamlObjectWriterSettings()
    XamlObjectWriterSettings(settings: XamlObjectWriterSettings)
    """
    @property
    def AccessLevel(self) -> XamlAccessLevel:
        """
        Get: AccessLevel(self: XamlObjectWriterSettings) -> XamlAccessLevel
        Set: AccessLevel(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def AfterBeginInitHandler(self) -> EventHandler:
        """
        Get: AfterBeginInitHandler(self: XamlObjectWriterSettings) -> EventHandler[XamlObjectEventArgs]
        Set: AfterBeginInitHandler(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def AfterEndInitHandler(self) -> EventHandler:
        """
        Get: AfterEndInitHandler(self: XamlObjectWriterSettings) -> EventHandler[XamlObjectEventArgs]
        Set: AfterEndInitHandler(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def AfterPropertiesHandler(self) -> EventHandler:
        """
        Get: AfterPropertiesHandler(self: XamlObjectWriterSettings) -> EventHandler[XamlObjectEventArgs]
        Set: AfterPropertiesHandler(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def BeforePropertiesHandler(self) -> EventHandler:
        """
        Get: BeforePropertiesHandler(self: XamlObjectWriterSettings) -> EventHandler[XamlObjectEventArgs]
        Set: BeforePropertiesHandler(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def ExternalNameScope(self) -> INameScope:
        """
        Get: ExternalNameScope(self: XamlObjectWriterSettings) -> INameScope
        Set: ExternalNameScope(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def IgnoreCanConvert(self) -> bool:
        """
        Get: IgnoreCanConvert(self: XamlObjectWriterSettings) -> bool
        Set: IgnoreCanConvert(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def PreferUnconvertedDictionaryKeys(self) -> bool:
        """
        Get: PreferUnconvertedDictionaryKeys(self: XamlObjectWriterSettings) -> bool
        Set: PreferUnconvertedDictionaryKeys(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def RegisterNamesOnExternalNamescope(self) -> bool:
        """
        Get: RegisterNamesOnExternalNamescope(self: XamlObjectWriterSettings) -> bool
        Set: RegisterNamesOnExternalNamescope(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def RootObjectInstance(self) -> object:
        """
        Get: RootObjectInstance(self: XamlObjectWriterSettings) -> object
        Set: RootObjectInstance(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def SkipDuplicatePropertyCheck(self) -> bool:
        """
        Get: SkipDuplicatePropertyCheck(self: XamlObjectWriterSettings) -> bool
        Set: SkipDuplicatePropertyCheck(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def SkipProvideValueOnRoot(self) -> bool:
        """
        Get: SkipProvideValueOnRoot(self: XamlObjectWriterSettings) -> bool
        Set: SkipProvideValueOnRoot(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def SourceBamlUri(self) -> Uri:
        """
        Get: SourceBamlUri(self: XamlObjectWriterSettings) -> Uri
        Set: SourceBamlUri(self: XamlObjectWriterSettings) = value
        """
        ...

    @property
    def XamlSetValueHandler(self) -> EventHandler:
        """
        Get: XamlSetValueHandler(self: XamlObjectWriterSettings) -> EventHandler[XamlSetValueEventArgs]
        Set: XamlSetValueHandler(self: XamlObjectWriterSettings) = value
        """
        ...



class XamlParseException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlParseException()
    XamlParseException(message: str)
    XamlParseException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlSchemaContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlSchemaContext()
    XamlSchemaContext(settings: XamlSchemaContextSettings)
    XamlSchemaContext(referenceAssemblies: IEnumerable[Assembly])
    XamlSchemaContext(referenceAssemblies: IEnumerable[Assembly], settings: XamlSchemaContextSettings)
    """
    @property
    def FullyQualifyAssemblyNamesInClrNamespaces(self) -> bool:
        """ Get: FullyQualifyAssemblyNamesInClrNamespaces(self: XamlSchemaContext) -> bool """
        ...

    @property
    def ReferenceAssemblies(self) -> IList:
        """ Get: ReferenceAssemblies(self: XamlSchemaContext) -> IList[Assembly] """
        ...

    @property
    def SupportMarkupExtensionsWithDuplicateArity(self) -> bool:
        """ Get: SupportMarkupExtensionsWithDuplicateArity(self: XamlSchemaContext) -> bool """
        ...


    def GetAllXamlNamespaces(self) -> IEnumerable:
        """ GetAllXamlNamespaces(self: XamlSchemaContext) -> IEnumerable[str] """
        ...

    def GetAllXamlTypes(self, xamlNamespace:str) -> ICollection:
        """ GetAllXamlTypes(self: XamlSchemaContext, xamlNamespace: str) -> ICollection[XamlType] """
        ...

    def GetPreferredPrefix(self, xmlns:str) -> str:
        """ GetPreferredPrefix(self: XamlSchemaContext, xmlns: str) -> str """
        ...

    def GetValueConverter(self, *args): #cannot find CLR method
        """ GetValueConverter[TConverterBase](self: XamlSchemaContext, converterType: Type, targetType: XamlType) -> XamlValueConverter[TConverterBase] """
        ...

    def GetXamlDirective(self, xamlNamespace:str, name:str) -> XamlDirective:
        """ GetXamlDirective(self: XamlSchemaContext, xamlNamespace: str, name: str) -> XamlDirective """
        ...

    def GetXamlType(self, *__args:XamlTypeName) -> XamlType:
        """
        GetXamlType(self: XamlSchemaContext, xamlTypeName: XamlTypeName) -> XamlType
        GetXamlType(self: XamlSchemaContext, type: Type) -> XamlType
        """
        ...

    def OnAssemblyResolve(self, *args): #cannot find CLR method
        """ OnAssemblyResolve(self: XamlSchemaContext, assemblyName: str) -> Assembly """
        ...

    def TryGetCompatibleXamlNamespace(self, xamlNamespace, compatibleNamespace) -> Tuple_[bool, str]:
        """ TryGetCompatibleXamlNamespace(self: XamlSchemaContext, xamlNamespace: str) -> (bool, str) """
        ...


class XamlSchemaContextSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlSchemaContextSettings()
    XamlSchemaContextSettings(settings: XamlSchemaContextSettings)
    """
    @property
    def FullyQualifyAssemblyNamesInClrNamespaces(self) -> bool:
        """
        Get: FullyQualifyAssemblyNamesInClrNamespaces(self: XamlSchemaContextSettings) -> bool
        Set: FullyQualifyAssemblyNamesInClrNamespaces(self: XamlSchemaContextSettings) = value
        """
        ...

    @property
    def SupportMarkupExtensionsWithDuplicateArity(self) -> bool:
        """
        Get: SupportMarkupExtensionsWithDuplicateArity(self: XamlSchemaContextSettings) -> bool
        Set: SupportMarkupExtensionsWithDuplicateArity(self: XamlSchemaContextSettings) = value
        """
        ...



class XamlSchemaException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlSchemaException()
    XamlSchemaException(message: str)
    XamlSchemaException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Load(*__args:XamlReader) -> object:
        """
        Load(xamlReader: XamlReader) -> object
        Load(xmlReader: XmlReader) -> object
        Load(fileName: str) -> object
        Load(stream: Stream) -> object
        Load(textReader: TextReader) -> object
        """
        ...

    @staticmethod
    def Parse(xaml:str) -> object:
        """ Parse(xaml: str) -> object """
        ...

    @staticmethod
    def Save(*__args:object) -> str:
        """
        Save(writer: XmlWriter, instance: object)Save(writer: XamlWriter, instance: object)Save(instance: object) -> str
        Save(fileName: str, instance: object)Save(stream: Stream, instance: object)Save(writer: TextWriter, instance: object)
        """
        ...

    @staticmethod
    def Transform(xamlReader:XamlReader, xamlWriter:XamlWriter, closeWriter:bool = ...): # -> 
        """ Transform(xamlReader: XamlReader, xamlWriter: XamlWriter)Transform(xamlReader: XamlReader, xamlWriter: XamlWriter, closeWriter: bool) """
        ...

    __all__: list = ...


class XamlType(IEquatable): # skipped bases: <type 'object'>
    """
    XamlType(unknownTypeNamespace: str, unknownTypeName: str, typeArguments: IList[XamlType], schemaContext: XamlSchemaContext)
    XamlType(underlyingType: Type, schemaContext: XamlSchemaContext)
    XamlType(underlyingType: Type, schemaContext: XamlSchemaContext, invoker: XamlTypeInvoker)
    """
    @property
    def AllowedContentTypes(self) -> IList:
        """ Get: AllowedContentTypes(self: XamlType) -> IList[XamlType] """
        ...

    @property
    def BaseType(self) -> XamlType:
        """ Get: BaseType(self: XamlType) -> XamlType """
        ...

    @property
    def ConstructionRequiresArguments(self) -> bool:
        """ Get: ConstructionRequiresArguments(self: XamlType) -> bool """
        ...

    @property
    def ContentProperty(self) -> XamlMember:
        """ Get: ContentProperty(self: XamlType) -> XamlMember """
        ...

    @property
    def ContentWrappers(self) -> IList:
        """ Get: ContentWrappers(self: XamlType) -> IList[XamlType] """
        ...

    @property
    def DeferringLoader(self) -> XamlValueConverter:
        """ Get: DeferringLoader(self: XamlType) -> XamlValueConverter[XamlDeferringLoader] """
        ...

    @property
    def Invoker(self) -> XamlTypeInvoker:
        """ Get: Invoker(self: XamlType) -> XamlTypeInvoker """
        ...

    @property
    def IsAmbient(self) -> bool:
        """ Get: IsAmbient(self: XamlType) -> bool """
        ...

    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: XamlType) -> bool """
        ...

    @property
    def IsCollection(self) -> bool:
        """ Get: IsCollection(self: XamlType) -> bool """
        ...

    @property
    def IsConstructible(self) -> bool:
        """ Get: IsConstructible(self: XamlType) -> bool """
        ...

    @property
    def IsDictionary(self) -> bool:
        """ Get: IsDictionary(self: XamlType) -> bool """
        ...

    @property
    def IsGeneric(self) -> bool:
        """ Get: IsGeneric(self: XamlType) -> bool """
        ...

    @property
    def IsMarkupExtension(self) -> bool:
        """ Get: IsMarkupExtension(self: XamlType) -> bool """
        ...

    @property
    def IsNameScope(self) -> bool:
        """ Get: IsNameScope(self: XamlType) -> bool """
        ...

    @property
    def IsNameValid(self) -> bool:
        """ Get: IsNameValid(self: XamlType) -> bool """
        ...

    @property
    def IsNullable(self) -> bool:
        """ Get: IsNullable(self: XamlType) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: XamlType) -> bool """
        ...

    @property
    def IsUnknown(self) -> bool:
        """ Get: IsUnknown(self: XamlType) -> bool """
        ...

    @property
    def IsUsableDuringInitialization(self) -> bool:
        """ Get: IsUsableDuringInitialization(self: XamlType) -> bool """
        ...

    @property
    def IsWhitespaceSignificantCollection(self) -> bool:
        """ Get: IsWhitespaceSignificantCollection(self: XamlType) -> bool """
        ...

    @property
    def IsXData(self) -> bool:
        """ Get: IsXData(self: XamlType) -> bool """
        ...

    @property
    def ItemType(self) -> XamlType:
        """ Get: ItemType(self: XamlType) -> XamlType """
        ...

    @property
    def KeyType(self) -> XamlType:
        """ Get: KeyType(self: XamlType) -> XamlType """
        ...

    @property
    def MarkupExtensionReturnType(self) -> XamlType:
        """ Get: MarkupExtensionReturnType(self: XamlType) -> XamlType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XamlType) -> str """
        ...

    @property
    def PreferredXamlNamespace(self) -> str:
        """ Get: PreferredXamlNamespace(self: XamlType) -> str """
        ...

    @property
    def SchemaContext(self) -> XamlSchemaContext:
        """ Get: SchemaContext(self: XamlType) -> XamlSchemaContext """
        ...

    @property
    def TrimSurroundingWhitespace(self) -> bool:
        """ Get: TrimSurroundingWhitespace(self: XamlType) -> bool """
        ...

    @property
    def TypeArguments(self) -> IList:
        """ Get: TypeArguments(self: XamlType) -> IList[XamlType] """
        ...

    @property
    def TypeConverter(self) -> XamlValueConverter:
        """ Get: TypeConverter(self: XamlType) -> XamlValueConverter[TypeConverter] """
        ...

    @property
    def UnderlyingType(self) -> Type:
        """ Get: UnderlyingType(self: XamlType) -> Type """
        ...

    @property
    def ValueSerializer(self) -> XamlValueConverter:
        """ Get: ValueSerializer(self: XamlType) -> XamlValueConverter[ValueSerializer] """
        ...


    def CanAssignTo(self, xamlType:XamlType) -> bool:
        """ CanAssignTo(self: XamlType, xamlType: XamlType) -> bool """
        ...

    def GetAliasedProperty(self, directive:XamlDirective) -> XamlMember:
        """ GetAliasedProperty(self: XamlType, directive: XamlDirective) -> XamlMember """
        ...

    def GetAllAttachableMembers(self) -> ICollection:
        """ GetAllAttachableMembers(self: XamlType) -> ICollection[XamlMember] """
        ...

    def GetAllMembers(self) -> ICollection:
        """ GetAllMembers(self: XamlType) -> ICollection[XamlMember] """
        ...

    def GetAttachableMember(self, name:str) -> XamlMember:
        """ GetAttachableMember(self: XamlType, name: str) -> XamlMember """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XamlType) -> int """
        ...

    def GetMember(self, name:str) -> XamlMember:
        """ GetMember(self: XamlType, name: str) -> XamlMember """
        ...

    def GetPositionalParameters(self, parameterCount:int) -> IList:
        """ GetPositionalParameters(self: XamlType, parameterCount: int) -> IList[XamlType] """
        ...

    def GetXamlNamespaces(self) -> IList:
        """ GetXamlNamespaces(self: XamlType) -> IList[str] """
        ...

    def LookupAliasedProperty(self, *args): #cannot find CLR method
        """ LookupAliasedProperty(self: XamlType, directive: XamlDirective) -> XamlMember """
        ...

    def LookupAllAttachableMembers(self, *args): #cannot find CLR method
        """ LookupAllAttachableMembers(self: XamlType) -> IEnumerable[XamlMember] """
        ...

    def LookupAllMembers(self, *args): #cannot find CLR method
        """ LookupAllMembers(self: XamlType) -> IEnumerable[XamlMember] """
        ...

    def LookupAllowedContentTypes(self, *args): #cannot find CLR method
        """ LookupAllowedContentTypes(self: XamlType) -> IList[XamlType] """
        ...

    def LookupAttachableMember(self, *args): #cannot find CLR method
        """ LookupAttachableMember(self: XamlType, name: str) -> XamlMember """
        ...

    def LookupBaseType(self, *args): #cannot find CLR method
        """ LookupBaseType(self: XamlType) -> XamlType """
        ...

    def LookupCollectionKind(self, *args): #cannot find CLR method
        """ LookupCollectionKind(self: XamlType) -> XamlCollectionKind """
        ...

    def LookupConstructionRequiresArguments(self, *args): #cannot find CLR method
        """ LookupConstructionRequiresArguments(self: XamlType) -> bool """
        ...

    def LookupContentProperty(self, *args): #cannot find CLR method
        """ LookupContentProperty(self: XamlType) -> XamlMember """
        ...

    def LookupContentWrappers(self, *args): #cannot find CLR method
        """ LookupContentWrappers(self: XamlType) -> IList[XamlType] """
        ...

    def LookupCustomAttributeProvider(self, *args): #cannot find CLR method
        """ LookupCustomAttributeProvider(self: XamlType) -> ICustomAttributeProvider """
        ...

    def LookupDeferringLoader(self, *args): #cannot find CLR method
        """ LookupDeferringLoader(self: XamlType) -> XamlValueConverter[XamlDeferringLoader] """
        ...

    def LookupInvoker(self, *args): #cannot find CLR method
        """ LookupInvoker(self: XamlType) -> XamlTypeInvoker """
        ...

    def LookupIsAmbient(self, *args): #cannot find CLR method
        """ LookupIsAmbient(self: XamlType) -> bool """
        ...

    def LookupIsConstructible(self, *args): #cannot find CLR method
        """ LookupIsConstructible(self: XamlType) -> bool """
        ...

    def LookupIsMarkupExtension(self, *args): #cannot find CLR method
        """ LookupIsMarkupExtension(self: XamlType) -> bool """
        ...

    def LookupIsNameScope(self, *args): #cannot find CLR method
        """ LookupIsNameScope(self: XamlType) -> bool """
        ...

    def LookupIsNullable(self, *args): #cannot find CLR method
        """ LookupIsNullable(self: XamlType) -> bool """
        ...

    def LookupIsPublic(self, *args): #cannot find CLR method
        """ LookupIsPublic(self: XamlType) -> bool """
        ...

    def LookupIsUnknown(self, *args): #cannot find CLR method
        """ LookupIsUnknown(self: XamlType) -> bool """
        ...

    def LookupIsWhitespaceSignificantCollection(self, *args): #cannot find CLR method
        """ LookupIsWhitespaceSignificantCollection(self: XamlType) -> bool """
        ...

    def LookupIsXData(self, *args): #cannot find CLR method
        """ LookupIsXData(self: XamlType) -> bool """
        ...

    def LookupItemType(self, *args): #cannot find CLR method
        """ LookupItemType(self: XamlType) -> XamlType """
        ...

    def LookupKeyType(self, *args): #cannot find CLR method
        """ LookupKeyType(self: XamlType) -> XamlType """
        ...

    def LookupMarkupExtensionReturnType(self, *args): #cannot find CLR method
        """ LookupMarkupExtensionReturnType(self: XamlType) -> XamlType """
        ...

    def LookupMember(self, *args): #cannot find CLR method
        """ LookupMember(self: XamlType, name: str, skipReadOnlyCheck: bool) -> XamlMember """
        ...

    def LookupPositionalParameters(self, *args): #cannot find CLR method
        """ LookupPositionalParameters(self: XamlType, parameterCount: int) -> IList[XamlType] """
        ...

    def LookupSetMarkupExtensionHandler(self, *args): #cannot find CLR method
        """ LookupSetMarkupExtensionHandler(self: XamlType) -> EventHandler[XamlSetMarkupExtensionEventArgs] """
        ...

    def LookupSetTypeConverterHandler(self, *args): #cannot find CLR method
        """ LookupSetTypeConverterHandler(self: XamlType) -> EventHandler[XamlSetTypeConverterEventArgs] """
        ...

    def LookupTrimSurroundingWhitespace(self, *args): #cannot find CLR method
        """ LookupTrimSurroundingWhitespace(self: XamlType) -> bool """
        ...

    def LookupTypeConverter(self, *args): #cannot find CLR method
        """ LookupTypeConverter(self: XamlType) -> XamlValueConverter[TypeConverter] """
        ...

    def LookupUnderlyingType(self, *args): #cannot find CLR method
        """ LookupUnderlyingType(self: XamlType) -> Type """
        ...

    def LookupUsableDuringInitialization(self, *args): #cannot find CLR method
        """ LookupUsableDuringInitialization(self: XamlType) -> bool """
        ...

    def LookupValueSerializer(self, *args): #cannot find CLR method
        """ LookupValueSerializer(self: XamlType) -> XamlValueConverter[ValueSerializer] """
        ...

    def ToString(self) -> str:
        """ ToString(self: XamlType) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class XamlXmlReader(XamlReader, IXamlLineInfo): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XamlXmlReader(xmlReader: XmlReader)
    XamlXmlReader(xmlReader: XmlReader, settings: XamlXmlReaderSettings)
    XamlXmlReader(xmlReader: XmlReader, schemaContext: XamlSchemaContext)
    XamlXmlReader(xmlReader: XmlReader, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
    XamlXmlReader(fileName: str)
    XamlXmlReader(fileName: str, settings: XamlXmlReaderSettings)
    XamlXmlReader(fileName: str, schemaContext: XamlSchemaContext)
    XamlXmlReader(fileName: str, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
    XamlXmlReader(stream: Stream)
    XamlXmlReader(stream: Stream, settings: XamlXmlReaderSettings)
    XamlXmlReader(stream: Stream, schemaContext: XamlSchemaContext)
    XamlXmlReader(stream: Stream, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
    XamlXmlReader(textReader: TextReader)
    XamlXmlReader(textReader: TextReader, settings: XamlXmlReaderSettings)
    XamlXmlReader(textReader: TextReader, schemaContext: XamlSchemaContext)
    XamlXmlReader(textReader: TextReader, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
    """
    def __new__(cls, *__args:XmlReader) -> Self:
        """
        __new__(cls: type, xmlReader: XmlReader)
        __new__(cls: type, xmlReader: XmlReader, settings: XamlXmlReaderSettings)
        __new__(cls: type, xmlReader: XmlReader, schemaContext: XamlSchemaContext)
        __new__(cls: type, xmlReader: XmlReader, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, settings: XamlXmlReaderSettings)
        __new__(cls: type, fileName: str, schemaContext: XamlSchemaContext)
        __new__(cls: type, fileName: str, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, settings: XamlXmlReaderSettings)
        __new__(cls: type, stream: Stream, schemaContext: XamlSchemaContext)
        __new__(cls: type, stream: Stream, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
        __new__(cls: type, textReader: TextReader)
        __new__(cls: type, textReader: TextReader, settings: XamlXmlReaderSettings)
        __new__(cls: type, textReader: TextReader, schemaContext: XamlSchemaContext)
        __new__(cls: type, textReader: TextReader, schemaContext: XamlSchemaContext, settings: XamlXmlReaderSettings)
        """
        ...


class XamlXmlReaderSettings(XamlReaderSettings): # skipped bases: <type 'object'>
    """
    XamlXmlReaderSettings()
    XamlXmlReaderSettings(settings: XamlXmlReaderSettings)
    """
    @property
    def CloseInput(self) -> bool:
        """
        Get: CloseInput(self: XamlXmlReaderSettings) -> bool
        Set: CloseInput(self: XamlXmlReaderSettings) = value
        """
        ...

    @property
    def SkipXmlCompatibilityProcessing(self) -> bool:
        """
        Get: SkipXmlCompatibilityProcessing(self: XamlXmlReaderSettings) -> bool
        Set: SkipXmlCompatibilityProcessing(self: XamlXmlReaderSettings) = value
        """
        ...

    @property
    def XmlLang(self) -> str:
        """
        Get: XmlLang(self: XamlXmlReaderSettings) -> str
        Set: XmlLang(self: XamlXmlReaderSettings) = value
        """
        ...

    @property
    def XmlSpacePreserve(self) -> bool:
        """
        Get: XmlSpacePreserve(self: XamlXmlReaderSettings) -> bool
        Set: XmlSpacePreserve(self: XamlXmlReaderSettings) = value
        """
        ...



class XamlXmlWriter(XamlWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XamlXmlWriter(stream: Stream, schemaContext: XamlSchemaContext)
    XamlXmlWriter(stream: Stream, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
    XamlXmlWriter(textWriter: TextWriter, schemaContext: XamlSchemaContext)
    XamlXmlWriter(textWriter: TextWriter, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
    XamlXmlWriter(xmlWriter: XmlWriter, schemaContext: XamlSchemaContext)
    XamlXmlWriter(xmlWriter: XmlWriter, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
    """
    @property
    def Settings(self) -> XamlXmlWriterSettings:
        """ Get: Settings(self: XamlXmlWriter) -> XamlXmlWriterSettings """
        ...


    def Flush(self): # -> 
        """ Flush(self: XamlXmlWriter) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, stream: Stream, schemaContext: XamlSchemaContext)
        __new__(cls: type, stream: Stream, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
        __new__(cls: type, textWriter: TextWriter, schemaContext: XamlSchemaContext)
        __new__(cls: type, textWriter: TextWriter, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
        __new__(cls: type, xmlWriter: XmlWriter, schemaContext: XamlSchemaContext)
        __new__(cls: type, xmlWriter: XmlWriter, schemaContext: XamlSchemaContext, settings: XamlXmlWriterSettings)
        """
        ...


class XamlXmlWriterException(XamlException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XamlXmlWriterException()
    XamlXmlWriterException(message: str)
    XamlXmlWriterException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XamlXmlWriterSettings(XamlWriterSettings): # skipped bases: <type 'object'>
    """ XamlXmlWriterSettings() """
    @property
    def AssumeValidInput(self) -> bool:
        """
        Get: AssumeValidInput(self: XamlXmlWriterSettings) -> bool
        Set: AssumeValidInput(self: XamlXmlWriterSettings) = value
        """
        ...

    @property
    def CloseOutput(self) -> bool:
        """
        Get: CloseOutput(self: XamlXmlWriterSettings) -> bool
        Set: CloseOutput(self: XamlXmlWriterSettings) = value
        """
        ...


    def Copy(self) -> XamlXmlWriterSettings:
        """ Copy(self: XamlXmlWriterSettings) -> XamlXmlWriterSettings """
        ...


# variables with complex values

