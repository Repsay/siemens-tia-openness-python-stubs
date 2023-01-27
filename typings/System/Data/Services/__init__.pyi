# encoding: utf-8
# module System.Data.Services calls itself Services
# from System.Data.Services.Client, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Services.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Attribute, Enum, EventArgs, InvalidOperationException, 
    Type, Uri)

from System.Collections import ICollection, IEnumerable

from System.Collections.Generic import List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Data.Services.Common import DataServiceProtocolVersion

from System.Data.Services.Providers import ResourceProperty

from System.IO import Stream

from System.Linq import IQueryable

from System.Linq.Expressions import Expression

from System.Messaging import Message

from System.Net import WebHeaderCollection

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.ServiceModel.Web import WebServiceHost

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    DataServiceProcessingPipeline, IDataService, IDataServiceConfiguration, 
    IDataServiceHost, ServiceHostFactory, ServiceOperationRights, field#)
"""

# no functions
# classes

class ChangeInterceptorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ChangeInterceptorAttribute(entitySetName: str) """
    @property
    def EntitySetName(self) -> str:
        """ Get: EntitySetName(self: ChangeInterceptorAttribute) -> str """
        ...


    def __new__(cls, entitySetName:str) -> Self:
        """ __new__(cls: type, entitySetName: str) """
        ...


class IRequestHandler: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessRequestForMessage(self, messageBody:Stream) -> Message:
        """ ProcessRequestForMessage(self: IRequestHandler, messageBody: Stream) -> Message """
        ...


class DataService(IRequestHandler, IDataService): # skipped bases: <type 'object'>
    """ DataService[T]() """
    @property
    def CurrentDataSource(self):
        ...

    @property
    def ProcessingPipeline(self): # -> DataServiceProcessingPipeline
        """ Get: ProcessingPipeline(self: DataService[T]) -> DataServiceProcessingPipeline """
        ...


    def AttachHost(self, host): # ->  # Not found arg types: {'host': 'IDataServiceHost'}
        """ AttachHost(self: DataService[T], host: IDataServiceHost) """
        ...

    def CreateDataSource(self, *args): #cannot find CLR method
        """ CreateDataSource(self: DataService[T]) -> T """
        ...

    def HandleException(self, *args): #cannot find CLR method
        """ HandleException(self: DataService[T], args: HandleExceptionArgs) """
        ...

    def OnStartProcessingRequest(self, *args): #cannot find CLR method
        """ OnStartProcessingRequest(self: DataService[T], args: ProcessRequestArgs) """
        ...

    def ProcessRequest(self): # -> 
        """ ProcessRequest(self: DataService[T]) """
        ...


class DataServiceBehavior: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AcceptCountRequests(self) -> bool:
        """
        Get: AcceptCountRequests(self: DataServiceBehavior) -> bool
        Set: AcceptCountRequests(self: DataServiceBehavior) = value
        """
        ...

    @property
    def AcceptProjectionRequests(self) -> bool:
        """
        Get: AcceptProjectionRequests(self: DataServiceBehavior) -> bool
        Set: AcceptProjectionRequests(self: DataServiceBehavior) = value
        """
        ...

    @property
    def AcceptReplaceFunctionInQuery(self) -> bool:
        """
        Get: AcceptReplaceFunctionInQuery(self: DataServiceBehavior) -> bool
        Set: AcceptReplaceFunctionInQuery(self: DataServiceBehavior) = value
        """
        ...

    @property
    def InvokeInterceptorsOnLinkDelete(self) -> bool:
        """
        Get: InvokeInterceptorsOnLinkDelete(self: DataServiceBehavior) -> bool
        Set: InvokeInterceptorsOnLinkDelete(self: DataServiceBehavior) = value
        """
        ...

    @property
    def MaxProtocolVersion(self) -> DataServiceProtocolVersion:
        """
        Get: MaxProtocolVersion(self: DataServiceBehavior) -> DataServiceProtocolVersion
        Set: MaxProtocolVersion(self: DataServiceBehavior) = value
        """
        ...



class DataServiceConfiguration(IDataServiceConfiguration): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataServiceBehavior(self) -> DataServiceBehavior:
        """ Get: DataServiceBehavior(self: DataServiceConfiguration) -> DataServiceBehavior """
        ...

    @property
    def EnableTypeConversion(self) -> bool:
        """
        Get: EnableTypeConversion(self: DataServiceConfiguration) -> bool
        Set: EnableTypeConversion(self: DataServiceConfiguration) = value
        """
        ...


    def EnableTypeAccess(self, typeName:str): # -> 
        """ EnableTypeAccess(self: DataServiceConfiguration, typeName: str) """
        ...

    def SetEntitySetPageSize(self, name:str, size:int): # -> 
        """ SetEntitySetPageSize(self: DataServiceConfiguration, name: str, size: int) """
        ...


class DataServiceException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DataServiceException()
    DataServiceException(message: str)
    DataServiceException(message: str, innerException: Exception)
    DataServiceException(statusCode: int, message: str)
    DataServiceException(statusCode: int, errorCode: str, message: str, messageXmlLang: str, innerException: Exception)
    """
    @property
    def ErrorCode(self) -> str:
        """ Get: ErrorCode(self: DataServiceException) -> str """
        ...

    @property
    def MessageLanguage(self) -> str:
        """ Get: MessageLanguage(self: DataServiceException) -> str """
        ...

    @property
    def StatusCode(self) -> int:
        """ Get: StatusCode(self: DataServiceException) -> int """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: DataServiceException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class DataServiceHost(WebServiceHost): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """ DataServiceHost(serviceType: Type, baseAddresses: Array[Uri]) """
    pass

class DataServiceHostFactory(ServiceHostFactory): # skipped bases: <type 'object'>
    """ DataServiceHostFactory() """
    pass

class DataServiceOperationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AbsoluteRequestUri(self) -> Uri:
        """ Get: AbsoluteRequestUri(self: DataServiceOperationContext) -> Uri """
        ...

    @property
    def AbsoluteServiceUri(self) -> Uri:
        """ Get: AbsoluteServiceUri(self: DataServiceOperationContext) -> Uri """
        ...

    @property
    def IsBatchRequest(self) -> bool:
        """ Get: IsBatchRequest(self: DataServiceOperationContext) -> bool """
        ...

    @property
    def RequestHeaders(self) -> WebHeaderCollection:
        """ Get: RequestHeaders(self: DataServiceOperationContext) -> WebHeaderCollection """
        ...

    @property
    def RequestMethod(self) -> str:
        """ Get: RequestMethod(self: DataServiceOperationContext) -> str """
        ...

    @property
    def ResponseHeaders(self) -> WebHeaderCollection:
        """ Get: ResponseHeaders(self: DataServiceOperationContext) -> WebHeaderCollection """
        ...

    @property
    def ResponseStatusCode(self) -> int:
        """
        Get: ResponseStatusCode(self: DataServiceOperationContext) -> int
        Set: ResponseStatusCode(self: DataServiceOperationContext) = value
        """
        ...



class DataServiceProcessingPipeline: # skipped bases: <type 'object'>, <type 'object'>
    """ DataServiceProcessingPipeline() """
    ProcessedChangeset = ...
    ProcessedRequest = ...
    ProcessingChangeset = ...
    ProcessingRequest = ...


class DataServiceProcessingPipelineEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OperationContext(self) -> DataServiceOperationContext:
        """ Get: OperationContext(self: DataServiceProcessingPipelineEventArgs) -> DataServiceOperationContext """
        ...



class EntitySetRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EntitySetRights, values: All (63), AllRead (3), AllWrite (60), None (0), ReadMultiple (2), ReadSingle (1), WriteAppend (4), WriteDelete (16), WriteMerge (32), WriteReplace (8) """
    All: EntitySetRights = ...
    AllRead: EntitySetRights = ...
    AllWrite: EntitySetRights = ...
    ReadMultiple: EntitySetRights = ...
    ReadSingle: EntitySetRights = ...
    value__ = ...
    WriteAppend: EntitySetRights = ...
    WriteDelete: EntitySetRights = ...
    WriteMerge: EntitySetRights = ...
    WriteReplace: EntitySetRights = ...


class ETagAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ETagAttribute(propertyName: str)
    ETagAttribute(*propertyNames: Array[str])
    """
    @property
    def PropertyNames(self) -> ReadOnlyCollection:
        """ Get: PropertyNames(self: ETagAttribute) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, propertyName: str)
        __new__(cls: type, *propertyNames: Array[str])
        """
        ...


class ExpandSegment: # skipped bases: <type 'object'>, <type 'object'>
    """ ExpandSegment(name: str, filter: Expression) """
    @property
    def ExpandedProperty(self) -> ResourceProperty:
        """ Get: ExpandedProperty(self: ExpandSegment) -> ResourceProperty """
        ...

    @property
    def Filter(self) -> Expression:
        """ Get: Filter(self: ExpandSegment) -> Expression """
        ...

    @property
    def HasFilter(self) -> bool:
        """ Get: HasFilter(self: ExpandSegment) -> bool """
        ...

    @property
    def MaxResultsExpected(self) -> int:
        """ Get: MaxResultsExpected(self: ExpandSegment) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ExpandSegment) -> str """
        ...


    @staticmethod
    def PathHasFilter(path:IEnumerable) -> bool:
        """ PathHasFilter(path: IEnumerable[ExpandSegment]) -> bool """
        ...


class ExpandSegmentCollection(List): # skipped bases: <type 'IList[ExpandSegment]'>, <type 'IEnumerable[ExpandSegment]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[ExpandSegment]'>, <type 'IReadOnlyList[ExpandSegment]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[ExpandSegment]'>, <type 'object'>
    """
    ExpandSegmentCollection()
    ExpandSegmentCollection(capacity: int)
    """
    @property
    def HasFilter(self) -> bool:
        """ Get: HasFilter(self: ExpandSegmentCollection) -> bool """
        ...



class HandleExceptionArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """
        Get: Exception(self: HandleExceptionArgs) -> Exception
        Set: Exception(self: HandleExceptionArgs) = value
        """
        ...

    @property
    def ResponseContentType(self) -> str:
        """ Get: ResponseContentType(self: HandleExceptionArgs) -> str """
        ...

    @property
    def ResponseStatusCode(self) -> int:
        """ Get: ResponseStatusCode(self: HandleExceptionArgs) -> int """
        ...

    @property
    def ResponseWritten(self) -> bool:
        """ Get: ResponseWritten(self: HandleExceptionArgs) -> bool """
        ...

    @property
    def UseVerboseErrors(self) -> bool:
        """
        Get: UseVerboseErrors(self: HandleExceptionArgs) -> bool
        Set: UseVerboseErrors(self: HandleExceptionArgs) = value
        """
        ...



class IDataServiceConfiguration: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MaxBatchCount(self) -> int:
        """
        Get: MaxBatchCount(self: IDataServiceConfiguration) -> int
        Set: MaxBatchCount(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def MaxChangesetCount(self) -> int:
        """
        Get: MaxChangesetCount(self: IDataServiceConfiguration) -> int
        Set: MaxChangesetCount(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def MaxExpandCount(self) -> int:
        """
        Get: MaxExpandCount(self: IDataServiceConfiguration) -> int
        Set: MaxExpandCount(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def MaxExpandDepth(self) -> int:
        """
        Get: MaxExpandDepth(self: IDataServiceConfiguration) -> int
        Set: MaxExpandDepth(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def MaxObjectCountOnInsert(self) -> int:
        """
        Get: MaxObjectCountOnInsert(self: IDataServiceConfiguration) -> int
        Set: MaxObjectCountOnInsert(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def MaxResultsPerCollection(self) -> int:
        """
        Get: MaxResultsPerCollection(self: IDataServiceConfiguration) -> int
        Set: MaxResultsPerCollection(self: IDataServiceConfiguration) = value
        """
        ...

    @property
    def UseVerboseErrors(self) -> bool:
        """
        Get: UseVerboseErrors(self: IDataServiceConfiguration) -> bool
        Set: UseVerboseErrors(self: IDataServiceConfiguration) = value
        """
        ...


    def RegisterKnownType(self, type:Type): # -> 
        """ RegisterKnownType(self: IDataServiceConfiguration, type: Type) """
        ...

    def SetEntitySetAccessRule(self, name:str, rights:EntitySetRights): # -> 
        """ SetEntitySetAccessRule(self: IDataServiceConfiguration, name: str, rights: EntitySetRights) """
        ...

    def SetServiceOperationAccessRule(self, name:str, rights): # ->  # Not found arg types: {'rights': 'ServiceOperationRights'}
        """ SetServiceOperationAccessRule(self: IDataServiceConfiguration, name: str, rights: ServiceOperationRights) """
        ...


class IDataServiceHost: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AbsoluteRequestUri(self) -> Uri:
        """ Get: AbsoluteRequestUri(self: IDataServiceHost) -> Uri """
        ...

    @property
    def AbsoluteServiceUri(self) -> Uri:
        """ Get: AbsoluteServiceUri(self: IDataServiceHost) -> Uri """
        ...

    @property
    def RequestAccept(self) -> str:
        """ Get: RequestAccept(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestAcceptCharSet(self) -> str:
        """ Get: RequestAcceptCharSet(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestContentType(self) -> str:
        """ Get: RequestContentType(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestHttpMethod(self) -> str:
        """ Get: RequestHttpMethod(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestIfMatch(self) -> str:
        """ Get: RequestIfMatch(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestIfNoneMatch(self) -> str:
        """ Get: RequestIfNoneMatch(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestMaxVersion(self) -> str:
        """ Get: RequestMaxVersion(self: IDataServiceHost) -> str """
        ...

    @property
    def RequestStream(self) -> Stream:
        """ Get: RequestStream(self: IDataServiceHost) -> Stream """
        ...

    @property
    def RequestVersion(self) -> str:
        """ Get: RequestVersion(self: IDataServiceHost) -> str """
        ...

    @property
    def ResponseCacheControl(self) -> str:
        """
        Get: ResponseCacheControl(self: IDataServiceHost) -> str
        Set: ResponseCacheControl(self: IDataServiceHost) = value
        """
        ...

    @property
    def ResponseContentType(self) -> str:
        """
        Get: ResponseContentType(self: IDataServiceHost) -> str
        Set: ResponseContentType(self: IDataServiceHost) = value
        """
        ...

    @property
    def ResponseETag(self) -> str:
        """
        Get: ResponseETag(self: IDataServiceHost) -> str
        Set: ResponseETag(self: IDataServiceHost) = value
        """
        ...

    @property
    def ResponseLocation(self) -> str:
        """
        Get: ResponseLocation(self: IDataServiceHost) -> str
        Set: ResponseLocation(self: IDataServiceHost) = value
        """
        ...

    @property
    def ResponseStatusCode(self) -> int:
        """
        Get: ResponseStatusCode(self: IDataServiceHost) -> int
        Set: ResponseStatusCode(self: IDataServiceHost) = value
        """
        ...

    @property
    def ResponseStream(self) -> Stream:
        """ Get: ResponseStream(self: IDataServiceHost) -> Stream """
        ...

    @property
    def ResponseVersion(self) -> str:
        """
        Get: ResponseVersion(self: IDataServiceHost) -> str
        Set: ResponseVersion(self: IDataServiceHost) = value
        """
        ...


    def GetQueryStringItem(self, item:str) -> str:
        """ GetQueryStringItem(self: IDataServiceHost, item: str) -> str """
        ...

    def ProcessException(self, args:HandleExceptionArgs): # -> 
        """ ProcessException(self: IDataServiceHost, args: HandleExceptionArgs) """
        ...


class IDataServiceHost2(IDataServiceHost): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestHeaders(self) -> WebHeaderCollection:
        """ Get: RequestHeaders(self: IDataServiceHost2) -> WebHeaderCollection """
        ...

    @property
    def ResponseHeaders(self) -> WebHeaderCollection:
        """ Get: ResponseHeaders(self: IDataServiceHost2) -> WebHeaderCollection """
        ...



class IExpandedResult: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExpandedElement(self) -> object:
        """ Get: ExpandedElement(self: IExpandedResult) -> object """
        ...


    def GetExpandedPropertyValue(self, name:str) -> object:
        """ GetExpandedPropertyValue(self: IExpandedResult, name: str) -> object """
        ...


class IExpandProvider: # skipped bases: <type 'object'>
    """ no doc """
    def ApplyExpansions(self, queryable:IQueryable, expandPaths:ICollection) -> IEnumerable:
        """ ApplyExpansions(self: IExpandProvider, queryable: IQueryable, expandPaths: ICollection[ExpandSegmentCollection]) -> IEnumerable """
        ...


class IgnorePropertiesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    IgnorePropertiesAttribute(propertyName: str)
    IgnorePropertiesAttribute(*propertyNames: Array[str])
    """
    @property
    def PropertyNames(self) -> ReadOnlyCollection:
        """ Get: PropertyNames(self: IgnorePropertiesAttribute) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, propertyName: str)
        __new__(cls: type, *propertyNames: Array[str])
        """
        ...


class IUpdatable: # skipped bases: <type 'object'>
    """ no doc """
    def AddReferenceToCollection(self, targetResource:object, propertyName:str, resourceToBeAdded:object): # -> 
        """ AddReferenceToCollection(self: IUpdatable, targetResource: object, propertyName: str, resourceToBeAdded: object) """
        ...

    def ClearChanges(self): # -> 
        """ ClearChanges(self: IUpdatable) """
        ...

    def CreateResource(self, containerName:str, fullTypeName:str) -> object:
        """ CreateResource(self: IUpdatable, containerName: str, fullTypeName: str) -> object """
        ...

    def DeleteResource(self, targetResource:object): # -> 
        """ DeleteResource(self: IUpdatable, targetResource: object) """
        ...

    def GetResource(self, query:IQueryable, fullTypeName:str) -> object:
        """ GetResource(self: IUpdatable, query: IQueryable, fullTypeName: str) -> object """
        ...

    def GetValue(self, targetResource:object, propertyName:str) -> object:
        """ GetValue(self: IUpdatable, targetResource: object, propertyName: str) -> object """
        ...

    def RemoveReferenceFromCollection(self, targetResource:object, propertyName:str, resourceToBeRemoved:object): # -> 
        """ RemoveReferenceFromCollection(self: IUpdatable, targetResource: object, propertyName: str, resourceToBeRemoved: object) """
        ...

    def ResetResource(self, resource:object) -> object:
        """ ResetResource(self: IUpdatable, resource: object) -> object """
        ...

    def ResolveResource(self, resource:object) -> object:
        """ ResolveResource(self: IUpdatable, resource: object) -> object """
        ...

    def SaveChanges(self): # -> 
        """ SaveChanges(self: IUpdatable) """
        ...

    def SetReference(self, targetResource:object, propertyName:str, propertyValue:object): # -> 
        """ SetReference(self: IUpdatable, targetResource: object, propertyName: str, propertyValue: object) """
        ...

    def SetValue(self, targetResource:object, propertyName:str, propertyValue:object): # -> 
        """ SetValue(self: IUpdatable, targetResource: object, propertyName: str, propertyValue: object) """
        ...


class MimeTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MimeTypeAttribute(memberName: str, mimeType: str) """
    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: MimeTypeAttribute) -> str """
        ...

    @property
    def MimeType(self) -> str:
        """ Get: MimeType(self: MimeTypeAttribute) -> str """
        ...


    def __new__(cls, memberName:str, mimeType:str) -> Self:
        """ __new__(cls: type, memberName: str, mimeType: str) """
        ...


class ProcessRequestArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsBatchOperation(self) -> bool:
        """ Get: IsBatchOperation(self: ProcessRequestArgs) -> bool """
        ...

    @property
    def OperationContext(self) -> DataServiceOperationContext:
        """ Get: OperationContext(self: ProcessRequestArgs) -> DataServiceOperationContext """
        ...

    @property
    def RequestUri(self) -> Uri:
        """ Get: RequestUri(self: ProcessRequestArgs) -> Uri """
        ...



class QueryInterceptorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ QueryInterceptorAttribute(entitySetName: str) """
    @property
    def EntitySetName(self) -> str:
        """ Get: EntitySetName(self: QueryInterceptorAttribute) -> str """
        ...


    def __new__(cls, entitySetName:str) -> Self:
        """ __new__(cls: type, entitySetName: str) """
        ...


class ServiceOperationRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServiceOperationRights, values: All (3), AllRead (3), None (0), OverrideEntitySetRights (4), ReadMultiple (2), ReadSingle (1) """
    All: ServiceOperationRights = ...
    AllRead: ServiceOperationRights = ...
    OverrideEntitySetRights: ServiceOperationRights = ...
    ReadMultiple: ServiceOperationRights = ...
    ReadSingle: ServiceOperationRights = ...
    value__ = ...


class SingleResultAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SingleResultAttribute() """
    pass

class UpdateOperations(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) UpdateOperations, values: Add (1), Change (2), Delete (4), None (0) """
    Add: UpdateOperations = ...
    Change: UpdateOperations = ...
    Delete: UpdateOperations = ...
    value__ = ...


# variables with complex values

