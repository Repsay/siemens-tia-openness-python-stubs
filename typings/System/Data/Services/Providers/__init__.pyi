# encoding: utf-8
# module System.Data.Services.Providers calls itself Providers
# from System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Nullable, Type, Uri

from System.Collections import IEnumerable, IEnumerator

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Data.Services import DataServiceOperationContext, IUpdatable

from System.Data.Services.Common import EntityPropertyMappingAttribute

from System.IO import Stream

from System.Linq import IQueryable

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class DataServiceProviderMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Compare(left:str, right:str) -> int:
        """
        Compare(left: str, right: str) -> int
        Compare(left: bool, right: bool) -> int
        Compare(left: Nullable[bool], right: Nullable[bool]) -> int
        Compare(left: Guid, right: Guid) -> int
        Compare(left: Nullable[Guid], right: Nullable[Guid]) -> int
        """
        ...

    @staticmethod
    def Convert(value:object, type:ResourceType) -> object:
        """ Convert(value: object, type: ResourceType) -> object """
        ...

    @staticmethod
    def GetSequenceValue(value:object, property:ResourceProperty) -> IEnumerable:
        """ GetSequenceValue[T](value: object, property: ResourceProperty) -> IEnumerable[T] """
        ...

    @staticmethod
    def GetValue(value:object, property:ResourceProperty) -> object:
        """ GetValue(value: object, property: ResourceProperty) -> object """
        ...

    @staticmethod
    def TypeIs(value:object, type:ResourceType) -> bool:
        """ TypeIs(value: object, type: ResourceType) -> bool """
        ...

    __all__: list = ...


class IDataServiceMetadataProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContainerName(self) -> str:
        """ Get: ContainerName(self: IDataServiceMetadataProvider) -> str """
        ...

    @property
    def ContainerNamespace(self) -> str:
        """ Get: ContainerNamespace(self: IDataServiceMetadataProvider) -> str """
        ...

    @property
    def ResourceSets(self) -> IEnumerable:
        """ Get: ResourceSets(self: IDataServiceMetadataProvider) -> IEnumerable[ResourceSet] """
        ...

    @property
    def ServiceOperations(self) -> IEnumerable:
        """ Get: ServiceOperations(self: IDataServiceMetadataProvider) -> IEnumerable[ServiceOperation] """
        ...

    @property
    def Types(self) -> IEnumerable:
        """ Get: Types(self: IDataServiceMetadataProvider) -> IEnumerable[ResourceType] """
        ...


    def GetDerivedTypes(self, resourceType:ResourceType) -> IEnumerable:
        """ GetDerivedTypes(self: IDataServiceMetadataProvider, resourceType: ResourceType) -> IEnumerable[ResourceType] """
        ...

    def GetResourceAssociationSet(self, resourceSet:ResourceSet, resourceType:ResourceType, resourceProperty:ResourceProperty) -> ResourceAssociationSet:
        """ GetResourceAssociationSet(self: IDataServiceMetadataProvider, resourceSet: ResourceSet, resourceType: ResourceType, resourceProperty: ResourceProperty) -> ResourceAssociationSet """
        ...

    def HasDerivedTypes(self, resourceType:ResourceType) -> bool:
        """ HasDerivedTypes(self: IDataServiceMetadataProvider, resourceType: ResourceType) -> bool """
        ...

    def TryResolveResourceSet(self, name, resourceSet) -> Tuple_[bool, ResourceSet]:
        """ TryResolveResourceSet(self: IDataServiceMetadataProvider, name: str) -> (bool, ResourceSet) """
        ...

    def TryResolveResourceType(self, name, resourceType) -> Tuple_[bool, ResourceType]:
        """ TryResolveResourceType(self: IDataServiceMetadataProvider, name: str) -> (bool, ResourceType) """
        ...

    def TryResolveServiceOperation(self, name, serviceOperation) -> Tuple_[bool, ServiceOperation]:
        """ TryResolveServiceOperation(self: IDataServiceMetadataProvider, name: str) -> (bool, ServiceOperation) """
        ...


class IDataServicePagingProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetContinuationToken(self, enumerator:IEnumerator) -> Array:
        """ GetContinuationToken(self: IDataServicePagingProvider, enumerator: IEnumerator) -> Array[object] """
        ...

    def SetContinuationToken(self, query:IQueryable, resourceType:ResourceType, continuationToken:Array): # -> 
        """ SetContinuationToken(self: IDataServicePagingProvider, query: IQueryable, resourceType: ResourceType, continuationToken: Array[object]) """
        ...


class IDataServiceQueryProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentDataSource(self) -> object:
        """
        Get: CurrentDataSource(self: IDataServiceQueryProvider) -> object
        Set: CurrentDataSource(self: IDataServiceQueryProvider) = value
        """
        ...

    @property
    def IsNullPropagationRequired(self) -> bool:
        """ Get: IsNullPropagationRequired(self: IDataServiceQueryProvider) -> bool """
        ...


    def GetOpenPropertyValue(self, target:object, propertyName:str) -> object:
        """ GetOpenPropertyValue(self: IDataServiceQueryProvider, target: object, propertyName: str) -> object """
        ...

    def GetOpenPropertyValues(self, target:object) -> IEnumerable:
        """ GetOpenPropertyValues(self: IDataServiceQueryProvider, target: object) -> IEnumerable[KeyValuePair[str, object]] """
        ...

    def GetPropertyValue(self, target:object, resourceProperty:ResourceProperty) -> object:
        """ GetPropertyValue(self: IDataServiceQueryProvider, target: object, resourceProperty: ResourceProperty) -> object """
        ...

    def GetQueryRootForResourceSet(self, resourceSet:ResourceSet) -> IQueryable:
        """ GetQueryRootForResourceSet(self: IDataServiceQueryProvider, resourceSet: ResourceSet) -> IQueryable """
        ...

    def GetResourceType(self, target:object) -> ResourceType:
        """ GetResourceType(self: IDataServiceQueryProvider, target: object) -> ResourceType """
        ...

    def InvokeServiceOperation(self, serviceOperation:ServiceOperation, parameters:Array) -> object:
        """ InvokeServiceOperation(self: IDataServiceQueryProvider, serviceOperation: ServiceOperation, parameters: Array[object]) -> object """
        ...


class IDataServiceStreamProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def StreamBufferSize(self) -> int:
        """ Get: StreamBufferSize(self: IDataServiceStreamProvider) -> int """
        ...


    def DeleteStream(self, entity:object, operationContext:DataServiceOperationContext): # -> 
        """ DeleteStream(self: IDataServiceStreamProvider, entity: object, operationContext: DataServiceOperationContext) """
        ...

    def GetReadStream(self, entity:object, etag:str, checkETagForEquality:Nullable, operationContext:DataServiceOperationContext) -> Stream:
        """ GetReadStream(self: IDataServiceStreamProvider, entity: object, etag: str, checkETagForEquality: Nullable[bool], operationContext: DataServiceOperationContext) -> Stream """
        ...

    def GetReadStreamUri(self, entity:object, operationContext:DataServiceOperationContext) -> Uri:
        """ GetReadStreamUri(self: IDataServiceStreamProvider, entity: object, operationContext: DataServiceOperationContext) -> Uri """
        ...

    def GetStreamContentType(self, entity:object, operationContext:DataServiceOperationContext) -> str:
        """ GetStreamContentType(self: IDataServiceStreamProvider, entity: object, operationContext: DataServiceOperationContext) -> str """
        ...

    def GetStreamETag(self, entity:object, operationContext:DataServiceOperationContext) -> str:
        """ GetStreamETag(self: IDataServiceStreamProvider, entity: object, operationContext: DataServiceOperationContext) -> str """
        ...

    def GetWriteStream(self, entity:object, etag:str, checkETagForEquality:Nullable, operationContext:DataServiceOperationContext) -> Stream:
        """ GetWriteStream(self: IDataServiceStreamProvider, entity: object, etag: str, checkETagForEquality: Nullable[bool], operationContext: DataServiceOperationContext) -> Stream """
        ...

    def ResolveType(self, entitySetName:str, operationContext:DataServiceOperationContext) -> str:
        """ ResolveType(self: IDataServiceStreamProvider, entitySetName: str, operationContext: DataServiceOperationContext) -> str """
        ...


class IDataServiceUpdateProvider(IUpdatable): # skipped bases: <type 'object'>
    """ no doc """
    def SetConcurrencyValues(self, resourceCookie:object, checkForEquality:Nullable, concurrencyValues:IEnumerable): # -> 
        """ SetConcurrencyValues(self: IDataServiceUpdateProvider, resourceCookie: object, checkForEquality: Nullable[bool], concurrencyValues: IEnumerable[KeyValuePair[str, object]]) """
        ...


class OpenTypeMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Add(left:object, right:object) -> object:
        """ Add(left: object, right: object) -> object """
        ...

    @staticmethod
    def AndAlso(left:object, right:object) -> object:
        """ AndAlso(left: object, right: object) -> object """
        ...

    @staticmethod
    def Ceiling(value:object) -> object:
        """ Ceiling(value: object) -> object """
        ...

    @staticmethod
    def Concat(first:object, second:object) -> object:
        """ Concat(first: object, second: object) -> object """
        ...

    @staticmethod
    def Convert(value:object, type:ResourceType) -> object:
        """ Convert(value: object, type: ResourceType) -> object """
        ...

    @staticmethod
    def Day(dateTime:object) -> object:
        """ Day(dateTime: object) -> object """
        ...

    @staticmethod
    def Divide(left:object, right:object) -> object:
        """ Divide(left: object, right: object) -> object """
        ...

    @staticmethod
    def EndsWith(targetString:object, substring:object) -> object:
        """ EndsWith(targetString: object, substring: object) -> object """
        ...

    @staticmethod
    def Equal(left:object, right:object) -> object:
        """ Equal(left: object, right: object) -> object """
        ...

    @staticmethod
    def Floor(value:object) -> object:
        """ Floor(value: object) -> object """
        ...

    @staticmethod
    def GetValue(value:object, propertyName:str) -> object:
        """ GetValue(value: object, propertyName: str) -> object """
        ...

    @staticmethod
    def GreaterThan(left:object, right:object) -> object:
        """ GreaterThan(left: object, right: object) -> object """
        ...

    @staticmethod
    def GreaterThanOrEqual(left:object, right:object) -> object:
        """ GreaterThanOrEqual(left: object, right: object) -> object """
        ...

    @staticmethod
    def Hour(dateTime:object) -> object:
        """ Hour(dateTime: object) -> object """
        ...

    @staticmethod
    def IndexOf(targetString:object, substring:object) -> object:
        """ IndexOf(targetString: object, substring: object) -> object """
        ...

    @staticmethod
    def Length(value:object) -> object:
        """ Length(value: object) -> object """
        ...

    @staticmethod
    def LessThan(left:object, right:object) -> object:
        """ LessThan(left: object, right: object) -> object """
        ...

    @staticmethod
    def LessThanOrEqual(left:object, right:object) -> object:
        """ LessThanOrEqual(left: object, right: object) -> object """
        ...

    @staticmethod
    def Minute(dateTime:object) -> object:
        """ Minute(dateTime: object) -> object """
        ...

    @staticmethod
    def Modulo(left:object, right:object) -> object:
        """ Modulo(left: object, right: object) -> object """
        ...

    @staticmethod
    def Month(dateTime:object) -> object:
        """ Month(dateTime: object) -> object """
        ...

    @staticmethod
    def Multiply(left:object, right:object) -> object:
        """ Multiply(left: object, right: object) -> object """
        ...

    @staticmethod
    def Negate(value:object) -> object:
        """ Negate(value: object) -> object """
        ...

    @staticmethod
    def Not(value:object) -> object:
        """ Not(value: object) -> object """
        ...

    @staticmethod
    def NotEqual(left:object, right:object) -> object:
        """ NotEqual(left: object, right: object) -> object """
        ...

    @staticmethod
    def OrElse(left:object, right:object) -> object:
        """ OrElse(left: object, right: object) -> object """
        ...

    @staticmethod
    def Replace(targetString:object, substring:object, newString:object) -> object:
        """ Replace(targetString: object, substring: object, newString: object) -> object """
        ...

    @staticmethod
    def Round(value:object) -> object:
        """ Round(value: object) -> object """
        ...

    @staticmethod
    def Second(dateTime:object) -> object:
        """ Second(dateTime: object) -> object """
        ...

    @staticmethod
    def StartsWith(targetString:object, substring:object) -> object:
        """ StartsWith(targetString: object, substring: object) -> object """
        ...

    @staticmethod
    def Substring(targetString:object, startIndex:object, length:object = ...) -> object:
        """
        Substring(targetString: object, startIndex: object) -> object
        Substring(targetString: object, startIndex: object, length: object) -> object
        """
        ...

    @staticmethod
    def SubstringOf(substring:object, targetString:object) -> object:
        """ SubstringOf(substring: object, targetString: object) -> object """
        ...

    @staticmethod
    def Subtract(left:object, right:object) -> object:
        """ Subtract(left: object, right: object) -> object """
        ...

    @staticmethod
    def ToLower(targetString:object) -> object:
        """ ToLower(targetString: object) -> object """
        ...

    @staticmethod
    def ToUpper(targetString:object) -> object:
        """ ToUpper(targetString: object) -> object """
        ...

    @staticmethod
    def Trim(targetString:object) -> object:
        """ Trim(targetString: object) -> object """
        ...

    @staticmethod
    def TypeIs(value:object, type:ResourceType) -> object:
        """ TypeIs(value: object, type: ResourceType) -> object """
        ...

    @staticmethod
    def Year(dateTime:object) -> object:
        """ Year(dateTime: object) -> object """
        ...

    __all__: list = ...


class ResourceAssociationSet: # skipped bases: <type 'object'>, <type 'object'>
    """ ResourceAssociationSet(name: str, end1: ResourceAssociationSetEnd, end2: ResourceAssociationSetEnd) """
    @property
    def End1(self) -> ResourceAssociationSetEnd:
        """ Get: End1(self: ResourceAssociationSet) -> ResourceAssociationSetEnd """
        ...

    @property
    def End2(self) -> ResourceAssociationSetEnd:
        """ Get: End2(self: ResourceAssociationSet) -> ResourceAssociationSetEnd """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ResourceAssociationSet) -> str """
        ...



class ResourceAssociationSetEnd: # skipped bases: <type 'object'>, <type 'object'>
    """ ResourceAssociationSetEnd(resourceSet: ResourceSet, resourceType: ResourceType, resourceProperty: ResourceProperty) """
    @property
    def ResourceProperty(self) -> ResourceProperty:
        """ Get: ResourceProperty(self: ResourceAssociationSetEnd) -> ResourceProperty """
        ...

    @property
    def ResourceSet(self) -> ResourceSet:
        """ Get: ResourceSet(self: ResourceAssociationSetEnd) -> ResourceSet """
        ...

    @property
    def ResourceType(self) -> ResourceType:
        """ Get: ResourceType(self: ResourceAssociationSetEnd) -> ResourceType """
        ...



class ResourceProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ ResourceProperty(name: str, kind: ResourcePropertyKind, propertyResourceType: ResourceType) """
    @property
    def CanReflectOnInstanceTypeProperty(self) -> bool:
        """
        Get: CanReflectOnInstanceTypeProperty(self: ResourceProperty) -> bool
        Set: CanReflectOnInstanceTypeProperty(self: ResourceProperty) = value
        """
        ...

    @property
    def CustomState(self) -> object:
        """
        Get: CustomState(self: ResourceProperty) -> object
        Set: CustomState(self: ResourceProperty) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ResourceProperty) -> bool """
        ...

    @property
    def Kind(self) -> ResourcePropertyKind:
        """ Get: Kind(self: ResourceProperty) -> ResourcePropertyKind """
        ...

    @property
    def MimeType(self) -> str:
        """
        Get: MimeType(self: ResourceProperty) -> str
        Set: MimeType(self: ResourceProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ResourceProperty) -> str """
        ...

    @property
    def ResourceType(self) -> ResourceType:
        """ Get: ResourceType(self: ResourceProperty) -> ResourceType """
        ...


    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ResourceProperty) """
        ...


class ResourcePropertyKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ResourcePropertyKind, values: ComplexType (4), ETag (32), Key (2), Primitive (1), ResourceReference (8), ResourceSetReference (16) """
    ComplexType: ResourcePropertyKind = ...
    ETag: ResourcePropertyKind = ...
    Key: ResourcePropertyKind = ...
    Primitive: ResourcePropertyKind = ...
    ResourceReference: ResourcePropertyKind = ...
    ResourceSetReference: ResourcePropertyKind = ...
    value__ = ...


class ResourceSet: # skipped bases: <type 'object'>, <type 'object'>
    """ ResourceSet(name: str, elementType: ResourceType) """
    @property
    def CustomState(self) -> object:
        """
        Get: CustomState(self: ResourceSet) -> object
        Set: CustomState(self: ResourceSet) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ResourceSet) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ResourceSet) -> str """
        ...

    @property
    def ResourceType(self) -> ResourceType:
        """ Get: ResourceType(self: ResourceSet) -> ResourceType """
        ...


    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ResourceSet) """
        ...


class ResourceType: # skipped bases: <type 'object'>, <type 'object'>
    """ ResourceType(instanceType: Type, resourceTypeKind: ResourceTypeKind, baseType: ResourceType, namespaceName: str, name: str, isAbstract: bool) """
    @property
    def BaseType(self) -> ResourceType:
        """ Get: BaseType(self: ResourceType) -> ResourceType """
        ...

    @property
    def CanReflectOnInstanceType(self) -> bool:
        """
        Get: CanReflectOnInstanceType(self: ResourceType) -> bool
        Set: CanReflectOnInstanceType(self: ResourceType) = value
        """
        ...

    @property
    def CustomState(self) -> object:
        """
        Get: CustomState(self: ResourceType) -> object
        Set: CustomState(self: ResourceType) = value
        """
        ...

    @property
    def ETagProperties(self) -> ReadOnlyCollection:
        """ Get: ETagProperties(self: ResourceType) -> ReadOnlyCollection[ResourceProperty] """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: ResourceType) -> str """
        ...

    @property
    def InstanceType(self) -> Type:
        """ Get: InstanceType(self: ResourceType) -> Type """
        ...

    @property
    def IsAbstract(self) -> bool:
        """ Get: IsAbstract(self: ResourceType) -> bool """
        ...

    @property
    def IsMediaLinkEntry(self) -> bool:
        """
        Get: IsMediaLinkEntry(self: ResourceType) -> bool
        Set: IsMediaLinkEntry(self: ResourceType) = value
        """
        ...

    @property
    def IsOpenType(self) -> bool:
        """
        Get: IsOpenType(self: ResourceType) -> bool
        Set: IsOpenType(self: ResourceType) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ResourceType) -> bool """
        ...

    @property
    def KeyProperties(self) -> ReadOnlyCollection:
        """ Get: KeyProperties(self: ResourceType) -> ReadOnlyCollection[ResourceProperty] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ResourceType) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: ResourceType) -> str """
        ...

    @property
    def Properties(self) -> ReadOnlyCollection:
        """ Get: Properties(self: ResourceType) -> ReadOnlyCollection[ResourceProperty] """
        ...

    @property
    def PropertiesDeclaredOnThisType(self) -> ReadOnlyCollection:
        """ Get: PropertiesDeclaredOnThisType(self: ResourceType) -> ReadOnlyCollection[ResourceProperty] """
        ...

    @property
    def ResourceTypeKind(self) -> ResourceTypeKind:
        """ Get: ResourceTypeKind(self: ResourceType) -> ResourceTypeKind """
        ...


    def AddEntityPropertyMappingAttribute(self, attribute:EntityPropertyMappingAttribute): # -> 
        """ AddEntityPropertyMappingAttribute(self: ResourceType, attribute: EntityPropertyMappingAttribute) """
        ...

    def AddProperty(self, property:ResourceProperty): # -> 
        """ AddProperty(self: ResourceType, property: ResourceProperty) """
        ...

    @staticmethod
    def GetPrimitiveResourceType(type:Type) -> ResourceType:
        """ GetPrimitiveResourceType(type: Type) -> ResourceType """
        ...

    def LoadPropertiesDeclaredOnThisType(self, *args): #cannot find CLR method
        """ LoadPropertiesDeclaredOnThisType(self: ResourceType) -> IEnumerable[ResourceProperty] """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ResourceType) """
        ...


class ResourceTypeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResourceTypeKind, values: ComplexType (1), EntityType (0), Primitive (2) """
    ComplexType: ResourceTypeKind = ...
    EntityType: ResourceTypeKind = ...
    Primitive: ResourceTypeKind = ...
    value__ = ...


class ServiceOperation: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceOperation(name: str, resultKind: ServiceOperationResultKind, resultType: ResourceType, resultSet: ResourceSet, method: str, parameters: IEnumerable[ServiceOperationParameter]) """
    @property
    def CustomState(self) -> object:
        """
        Get: CustomState(self: ServiceOperation) -> object
        Set: CustomState(self: ServiceOperation) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ServiceOperation) -> bool """
        ...

    @property
    def Method(self) -> str:
        """ Get: Method(self: ServiceOperation) -> str """
        ...

    @property
    def MimeType(self) -> str:
        """
        Get: MimeType(self: ServiceOperation) -> str
        Set: MimeType(self: ServiceOperation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ServiceOperation) -> str """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: ServiceOperation) -> ReadOnlyCollection[ServiceOperationParameter] """
        ...

    @property
    def ResourceSet(self) -> ResourceSet:
        """ Get: ResourceSet(self: ServiceOperation) -> ResourceSet """
        ...

    @property
    def ResultKind(self) -> ServiceOperationResultKind:
        """ Get: ResultKind(self: ServiceOperation) -> ServiceOperationResultKind """
        ...

    @property
    def ResultType(self) -> ResourceType:
        """ Get: ResultType(self: ServiceOperation) -> ResourceType """
        ...


    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ServiceOperation) """
        ...


class ServiceOperationParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceOperationParameter(name: str, parameterType: ResourceType) """
    @property
    def CustomState(self) -> object:
        """
        Get: CustomState(self: ServiceOperationParameter) -> object
        Set: CustomState(self: ServiceOperationParameter) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ServiceOperationParameter) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ServiceOperationParameter) -> str """
        ...

    @property
    def ParameterType(self) -> ResourceType:
        """ Get: ParameterType(self: ServiceOperationParameter) -> ResourceType """
        ...


    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ServiceOperationParameter) """
        ...


class ServiceOperationResultKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceOperationResultKind, values: DirectValue (0), Enumeration (1), QueryWithMultipleResults (2), QueryWithSingleResult (3), Void (4) """
    DirectValue: ServiceOperationResultKind = ...
    Enumeration: ServiceOperationResultKind = ...
    QueryWithMultipleResults: ServiceOperationResultKind = ...
    QueryWithSingleResult: ServiceOperationResultKind = ...
    value__ = ...
    Void: ServiceOperationResultKind = ...


