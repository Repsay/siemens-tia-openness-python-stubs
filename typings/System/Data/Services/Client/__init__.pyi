# encoding: utf-8
# module System.Data.Services.Client calls itself Client
# from System.Data.Services.Client, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, IDisposable, Int64, InvalidOperationException, Type, Uri)

from System.Collections import (ICollection, IDictionary, IEnumerable, 
    IEnumerator)

from System.Collections.Generic import Dictionary

from System.Collections.ObjectModel import (ObservableCollection, 
    ReadOnlyCollection)

from System.Collections.Specialized import NotifyCollectionChangedAction

from System.IO import Stream

from System.Linq import IQueryProvider

from System.Linq.Expressions import Expression

from System.Net import ICredentials, WebHeaderCollection, WebRequest

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Xml.Linq import XElement

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, 
    TEntity, field#)
"""

# no functions
# classes

class OperationResponse: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Error(self) -> Exception:
        """
        Get: Error(self: OperationResponse) -> Exception
        Set: Error(self: OperationResponse) = value
        """
        ...

    @property
    def Headers(self) -> IDictionary:
        """ Get: Headers(self: OperationResponse) -> IDictionary[str, str] """
        ...

    @property
    def StatusCode(self) -> int:
        """ Get: StatusCode(self: OperationResponse) -> int """
        ...



class ChangeOperationResponse(OperationResponse): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Descriptor(self) -> Descriptor:
        """ Get: Descriptor(self: ChangeOperationResponse) -> Descriptor """
        ...



class DataServiceClientException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DataServiceClientException()
    DataServiceClientException(message: str)
    DataServiceClientException(message: str, innerException: Exception)
    DataServiceClientException(message: str, statusCode: int)
    DataServiceClientException(message: str, innerException: Exception, statusCode: int)
    """
    @property
    def StatusCode(self) -> int:
        """ Get: StatusCode(self: DataServiceClientException) -> int """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: DataServiceClientException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class DataServiceCollection(ObservableCollection): # skipped bases: <type 'IList[T]'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'IList'>, <type 'IReadOnlyList[T]'>, <type 'IReadOnlyCollection[T]'>, <type 'INotifyCollectionChanged'>, <type 'INotifyPropertyChanged'>, <type 'ICollection'>, <type 'ICollection[T]'>, <type 'object'>
    """
    DataServiceCollection[T]()
    DataServiceCollection[T](items: IEnumerable[T])
    DataServiceCollection[T](items: IEnumerable[T], trackingMode: TrackingMode)
    DataServiceCollection[T](context: DataServiceContext)
    DataServiceCollection[T](context: DataServiceContext, entitySetName: str, entityChangedCallback: Func[EntityChangedParams, bool], collectionChangedCallback: Func[EntityCollectionChangedParams, bool])
    DataServiceCollection[T](items: IEnumerable[T], trackingMode: TrackingMode, entitySetName: str, entityChangedCallback: Func[EntityChangedParams, bool], collectionChangedCallback: Func[EntityCollectionChangedParams, bool])
    DataServiceCollection[T](context: DataServiceContext, items: IEnumerable[T], trackingMode: TrackingMode, entitySetName: str, entityChangedCallback: Func[EntityChangedParams, bool], collectionChangedCallback: Func[EntityCollectionChangedParams, bool])
    """
    @property
    def Continuation(self) -> DataServiceQueryContinuation:
        """
        Get: Continuation(self: DataServiceCollection[T]) -> DataServiceQueryContinuation[T]
        Set: Continuation(self: DataServiceCollection[T]) = value
        """
        ...


    def Detach(self): # -> 
        """ Detach(self: DataServiceCollection[T]) """
        ...

    def Load(self, *__args:IEnumerable): # -> 
        """ Load(self: DataServiceCollection[T], items: IEnumerable[T])Load(self: DataServiceCollection[T], item: T) """
        ...

    PropertyChanged = ...


class DataServiceContext: # skipped bases: <type 'object'>, <type 'object'>
    """ DataServiceContext(serviceRoot: Uri) """
    @property
    def ApplyingChanges(self) -> bool:
        """ Get: ApplyingChanges(self: DataServiceContext) -> bool """
        ...

    @property
    def BaseUri(self) -> Uri:
        """ Get: BaseUri(self: DataServiceContext) -> Uri """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: DataServiceContext) -> ICredentials
        Set: Credentials(self: DataServiceContext) = value
        """
        ...

    @property
    def DataNamespace(self) -> str:
        """
        Get: DataNamespace(self: DataServiceContext) -> str
        Set: DataNamespace(self: DataServiceContext) = value
        """
        ...

    @property
    def Entities(self) -> ReadOnlyCollection:
        """ Get: Entities(self: DataServiceContext) -> ReadOnlyCollection[EntityDescriptor] """
        ...

    @property
    def IgnoreMissingProperties(self) -> bool:
        """
        Get: IgnoreMissingProperties(self: DataServiceContext) -> bool
        Set: IgnoreMissingProperties(self: DataServiceContext) = value
        """
        ...

    @property
    def IgnoreResourceNotFoundException(self) -> bool:
        """
        Get: IgnoreResourceNotFoundException(self: DataServiceContext) -> bool
        Set: IgnoreResourceNotFoundException(self: DataServiceContext) = value
        """
        ...

    @property
    def Links(self) -> ReadOnlyCollection:
        """ Get: Links(self: DataServiceContext) -> ReadOnlyCollection[LinkDescriptor] """
        ...

    @property
    def MergeOption(self) -> MergeOption:
        """
        Get: MergeOption(self: DataServiceContext) -> MergeOption
        Set: MergeOption(self: DataServiceContext) = value
        """
        ...

    @property
    def ResolveName(self): # -> Func
        """
        Get: ResolveName(self: DataServiceContext) -> Func[Type, str]
        Set: ResolveName(self: DataServiceContext) = value
        """
        ...

    @property
    def ResolveType(self): # -> Func
        """
        Get: ResolveType(self: DataServiceContext) -> Func[str, Type]
        Set: ResolveType(self: DataServiceContext) = value
        """
        ...

    @property
    def SaveChangesDefaultOptions(self) -> SaveChangesOptions:
        """
        Get: SaveChangesDefaultOptions(self: DataServiceContext) -> SaveChangesOptions
        Set: SaveChangesDefaultOptions(self: DataServiceContext) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: DataServiceContext) -> int
        Set: Timeout(self: DataServiceContext) = value
        """
        ...

    @property
    def TypeScheme(self) -> Uri:
        """
        Get: TypeScheme(self: DataServiceContext) -> Uri
        Set: TypeScheme(self: DataServiceContext) = value
        """
        ...

    @property
    def UsePostTunneling(self) -> bool:
        """
        Get: UsePostTunneling(self: DataServiceContext) -> bool
        Set: UsePostTunneling(self: DataServiceContext) = value
        """
        ...


    def AddLink(self, source:object, sourceProperty:str, target:object): # -> 
        """ AddLink(self: DataServiceContext, source: object, sourceProperty: str, target: object) """
        ...

    def AddObject(self, entitySetName:str, entity:object): # -> 
        """ AddObject(self: DataServiceContext, entitySetName: str, entity: object) """
        ...

    def AddRelatedObject(self, source:object, sourceProperty:str, target:object): # -> 
        """ AddRelatedObject(self: DataServiceContext, source: object, sourceProperty: str, target: object) """
        ...

    def AttachLink(self, source:object, sourceProperty:str, target:object): # -> 
        """ AttachLink(self: DataServiceContext, source: object, sourceProperty: str, target: object) """
        ...

    def AttachTo(self, entitySetName:str, entity:object, etag:str = ...): # -> 
        """ AttachTo(self: DataServiceContext, entitySetName: str, entity: object)AttachTo(self: DataServiceContext, entitySetName: str, entity: object, etag: str) """
        ...

    def BeginExecute(self, *__args) -> IAsyncResult:
        """
        BeginExecute[TElement](self: DataServiceContext, requestUri: Uri, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginExecute[T](self: DataServiceContext, continuation: DataServiceQueryContinuation[T], callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginExecuteBatch(self, callback:AsyncCallback, state:object, queries:Array) -> IAsyncResult:
        """ BeginExecuteBatch(self: DataServiceContext, callback: AsyncCallback, state: object, *queries: Array[DataServiceRequest]) -> IAsyncResult """
        ...

    def BeginGetReadStream(self, entity:object, args:DataServiceRequestArgs, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetReadStream(self: DataServiceContext, entity: object, args: DataServiceRequestArgs, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginLoadProperty(self, entity, propertyName, *__args) -> IAsyncResult:
        """
        BeginLoadProperty(self: DataServiceContext, entity: object, propertyName: str, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoadProperty(self: DataServiceContext, entity: object, propertyName: str, nextLinkUri: Uri, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoadProperty(self: DataServiceContext, entity: object, propertyName: str, continuation: DataServiceQueryContinuation, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginSaveChanges(self, *__args) -> IAsyncResult:
        """
        BeginSaveChanges(self: DataServiceContext, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSaveChanges(self: DataServiceContext, options: SaveChangesOptions, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def CancelRequest(self, asyncResult:IAsyncResult): # -> 
        """ CancelRequest(self: DataServiceContext, asyncResult: IAsyncResult) """
        ...

    def CreateQuery(self, entitySetName:str) -> DataServiceQuery:
        """ CreateQuery[T](self: DataServiceContext, entitySetName: str) -> DataServiceQuery[T] """
        ...

    def DeleteLink(self, source:object, sourceProperty:str, target:object): # -> 
        """ DeleteLink(self: DataServiceContext, source: object, sourceProperty: str, target: object) """
        ...

    def DeleteObject(self, entity:object): # -> 
        """ DeleteObject(self: DataServiceContext, entity: object) """
        ...

    def Detach(self, entity:object) -> bool:
        """ Detach(self: DataServiceContext, entity: object) -> bool """
        ...

    def DetachLink(self, source:object, sourceProperty:str, target:object) -> bool:
        """ DetachLink(self: DataServiceContext, source: object, sourceProperty: str, target: object) -> bool """
        ...

    def EndExecute(self, asyncResult:IAsyncResult) -> IEnumerable:
        """ EndExecute[TElement](self: DataServiceContext, asyncResult: IAsyncResult) -> IEnumerable[TElement] """
        ...

    def EndExecuteBatch(self, asyncResult:IAsyncResult) -> DataServiceResponse:
        """ EndExecuteBatch(self: DataServiceContext, asyncResult: IAsyncResult) -> DataServiceResponse """
        ...

    def EndGetReadStream(self, asyncResult:IAsyncResult) -> DataServiceStreamResponse:
        """ EndGetReadStream(self: DataServiceContext, asyncResult: IAsyncResult) -> DataServiceStreamResponse """
        ...

    def EndLoadProperty(self, asyncResult:IAsyncResult) -> QueryOperationResponse:
        """ EndLoadProperty(self: DataServiceContext, asyncResult: IAsyncResult) -> QueryOperationResponse """
        ...

    def EndSaveChanges(self, asyncResult:IAsyncResult) -> DataServiceResponse:
        """ EndSaveChanges(self: DataServiceContext, asyncResult: IAsyncResult) -> DataServiceResponse """
        ...

    def Execute(self, *__args:Uri) -> IEnumerable:
        """
        Execute[TElement](self: DataServiceContext, requestUri: Uri) -> IEnumerable[TElement]
        Execute[T](self: DataServiceContext, continuation: DataServiceQueryContinuation[T]) -> QueryOperationResponse[T]
        """
        ...

    def ExecuteBatch(self, queries:Array) -> DataServiceResponse:
        """ ExecuteBatch(self: DataServiceContext, *queries: Array[DataServiceRequest]) -> DataServiceResponse """
        ...

    def GetEntityDescriptor(self, entity:object) -> EntityDescriptor:
        """ GetEntityDescriptor(self: DataServiceContext, entity: object) -> EntityDescriptor """
        ...

    def GetLinkDescriptor(self, source:object, sourceProperty:str, target:object) -> LinkDescriptor:
        """ GetLinkDescriptor(self: DataServiceContext, source: object, sourceProperty: str, target: object) -> LinkDescriptor """
        ...

    def GetMetadataUri(self) -> Uri:
        """ GetMetadataUri(self: DataServiceContext) -> Uri """
        ...

    def GetReadStream(self, entity:object, *__args:DataServiceRequestArgs) -> DataServiceStreamResponse:
        """
        GetReadStream(self: DataServiceContext, entity: object) -> DataServiceStreamResponse
        GetReadStream(self: DataServiceContext, entity: object, args: DataServiceRequestArgs) -> DataServiceStreamResponse
        GetReadStream(self: DataServiceContext, entity: object, acceptContentType: str) -> DataServiceStreamResponse
        """
        ...

    def GetReadStreamUri(self, entity:object) -> Uri:
        """ GetReadStreamUri(self: DataServiceContext, entity: object) -> Uri """
        ...

    def LoadProperty(self, entity:object, propertyName:str, *__args:Uri) -> QueryOperationResponse:
        """
        LoadProperty(self: DataServiceContext, entity: object, propertyName: str) -> QueryOperationResponse
        LoadProperty(self: DataServiceContext, entity: object, propertyName: str, nextLinkUri: Uri) -> QueryOperationResponse
        LoadProperty(self: DataServiceContext, entity: object, propertyName: str, continuation: DataServiceQueryContinuation) -> QueryOperationResponse
        LoadProperty[T](self: DataServiceContext, entity: object, propertyName: str, continuation: DataServiceQueryContinuation[T]) -> QueryOperationResponse[T]
        """
        ...

    def SaveChanges(self, options:SaveChangesOptions = ...) -> DataServiceResponse:
        """
        SaveChanges(self: DataServiceContext) -> DataServiceResponse
        SaveChanges(self: DataServiceContext, options: SaveChangesOptions) -> DataServiceResponse
        """
        ...

    def SetLink(self, source:object, sourceProperty:str, target:object): # -> 
        """ SetLink(self: DataServiceContext, source: object, sourceProperty: str, target: object) """
        ...

    def SetSaveStream(self, entity:object, stream:Stream, closeStream:bool, *__args:DataServiceRequestArgs): # -> 
        """ SetSaveStream(self: DataServiceContext, entity: object, stream: Stream, closeStream: bool, contentType: str, slug: str)SetSaveStream(self: DataServiceContext, entity: object, stream: Stream, closeStream: bool, args: DataServiceRequestArgs) """
        ...

    def TryGetEntity(self, identity, entity): # -> Tuple_[bool, TEntity]
        """ TryGetEntity[TEntity](self: DataServiceContext, identity: Uri) -> (bool, TEntity) """
        ...

    def TryGetUri(self, entity, identity) -> Tuple_[bool, Uri]:
        """ TryGetUri(self: DataServiceContext, entity: object) -> (bool, Uri) """
        ...

    def UpdateObject(self, entity:object): # -> 
        """ UpdateObject(self: DataServiceContext, entity: object) """
        ...

    ReadingEntity = ...
    SendingRequest = ...
    WritingEntity = ...


class DataServiceQuery: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: DataServiceQuery) -> Expression """
        ...

    @property
    def Provider(self) -> IQueryProvider:
        """ Get: Provider(self: DataServiceQuery) -> IQueryProvider """
        ...


    def BeginExecute(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginExecute(self: DataServiceQuery, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndExecute(self, asyncResult:IAsyncResult) -> IEnumerable:
        """ EndExecute(self: DataServiceQuery, asyncResult: IAsyncResult) -> IEnumerable """
        ...

    def Execute(self) -> IEnumerable:
        """ Execute(self: DataServiceQuery) -> IEnumerable """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DataServiceQueryContinuation: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NextLinkUri(self) -> Uri:
        """ Get: NextLinkUri(self: DataServiceQueryContinuation) -> Uri """
        ...


    def ToString(self) -> str:
        """ ToString(self: DataServiceQueryContinuation) -> str """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DataServiceQueryException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DataServiceQueryException()
    DataServiceQueryException(message: str)
    DataServiceQueryException(message: str, innerException: Exception)
    DataServiceQueryException(message: str, innerException: Exception, response: QueryOperationResponse)
    """
    @property
    def Response(self) -> QueryOperationResponse:
        """ Get: Response(self: DataServiceQueryException) -> QueryOperationResponse """
        ...


    SerializeObjectState = ...


class DataServiceRequest: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementType(self) -> Type:
        """ Get: ElementType(self: DataServiceRequest) -> Type """
        ...

    @property
    def RequestUri(self) -> Uri:
        """ Get: RequestUri(self: DataServiceRequest) -> Uri """
        ...


    def ToString(self) -> str:
        """ ToString(self: DataServiceRequest) -> str """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DataServiceRequestArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ DataServiceRequestArgs() """
    @property
    def AcceptContentType(self) -> str:
        """
        Get: AcceptContentType(self: DataServiceRequestArgs) -> str
        Set: AcceptContentType(self: DataServiceRequestArgs) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: DataServiceRequestArgs) -> str
        Set: ContentType(self: DataServiceRequestArgs) = value
        """
        ...

    @property
    def Headers(self) -> Dictionary:
        """ Get: Headers(self: DataServiceRequestArgs) -> Dictionary[str, str] """
        ...

    @property
    def Slug(self) -> str:
        """
        Get: Slug(self: DataServiceRequestArgs) -> str
        Set: Slug(self: DataServiceRequestArgs) = value
        """
        ...



class DataServiceRequestException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DataServiceRequestException()
    DataServiceRequestException(message: str)
    DataServiceRequestException(message: str, innerException: Exception)
    DataServiceRequestException(message: str, innerException: Exception, response: DataServiceResponse)
    """
    @property
    def Response(self) -> DataServiceResponse:
        """ Get: Response(self: DataServiceRequestException) -> DataServiceResponse """
        ...


    SerializeObjectState = ...


class DataServiceResponse(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def BatchHeaders(self) -> IDictionary:
        """ Get: BatchHeaders(self: DataServiceResponse) -> IDictionary[str, str] """
        ...

    @property
    def BatchStatusCode(self) -> int:
        """ Get: BatchStatusCode(self: DataServiceResponse) -> int """
        ...

    @property
    def IsBatchResponse(self) -> bool:
        """ Get: IsBatchResponse(self: DataServiceResponse) -> bool """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[OperationResponse](enumerable: IEnumerable[OperationResponse], value: OperationResponse) -> bool """
        ...


class DataServiceStreamResponse(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentDisposition(self) -> str:
        """ Get: ContentDisposition(self: DataServiceStreamResponse) -> str """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: DataServiceStreamResponse) -> str """
        ...

    @property
    def Headers(self) -> Dictionary:
        """ Get: Headers(self: DataServiceStreamResponse) -> Dictionary[str, str] """
        ...

    @property
    def Stream(self) -> Stream:
        """ Get: Stream(self: DataServiceStreamResponse) -> Stream """
        ...



class Descriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def State(self) -> EntityStates:
        """ Get: State(self: Descriptor) -> EntityStates """
        ...



class EntityChangedParams: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Context(self) -> DataServiceContext:
        """ Get: Context(self: EntityChangedParams) -> DataServiceContext """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: EntityChangedParams) -> object """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: EntityChangedParams) -> str """
        ...

    @property
    def PropertyValue(self) -> object:
        """ Get: PropertyValue(self: EntityChangedParams) -> object """
        ...

    @property
    def SourceEntitySet(self) -> str:
        """ Get: SourceEntitySet(self: EntityChangedParams) -> str """
        ...

    @property
    def TargetEntitySet(self) -> str:
        """ Get: TargetEntitySet(self: EntityChangedParams) -> str """
        ...



class EntityCollectionChangedParams: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> NotifyCollectionChangedAction:
        """ Get: Action(self: EntityCollectionChangedParams) -> NotifyCollectionChangedAction """
        ...

    @property
    def Collection(self) -> ICollection:
        """ Get: Collection(self: EntityCollectionChangedParams) -> ICollection """
        ...

    @property
    def Context(self) -> DataServiceContext:
        """ Get: Context(self: EntityCollectionChangedParams) -> DataServiceContext """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: EntityCollectionChangedParams) -> str """
        ...

    @property
    def SourceEntity(self) -> object:
        """ Get: SourceEntity(self: EntityCollectionChangedParams) -> object """
        ...

    @property
    def SourceEntitySet(self) -> str:
        """ Get: SourceEntitySet(self: EntityCollectionChangedParams) -> str """
        ...

    @property
    def TargetEntity(self) -> object:
        """ Get: TargetEntity(self: EntityCollectionChangedParams) -> object """
        ...

    @property
    def TargetEntitySet(self) -> str:
        """ Get: TargetEntitySet(self: EntityCollectionChangedParams) -> str """
        ...



class EntityDescriptor(Descriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EditLink(self) -> Uri:
        """ Get: EditLink(self: EntityDescriptor) -> Uri """
        ...

    @property
    def EditStreamUri(self) -> Uri:
        """ Get: EditStreamUri(self: EntityDescriptor) -> Uri """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: EntityDescriptor) -> object """
        ...

    @property
    def ETag(self) -> str:
        """ Get: ETag(self: EntityDescriptor) -> str """
        ...

    @property
    def Identity(self) -> str:
        """ Get: Identity(self: EntityDescriptor) -> str """
        ...

    @property
    def ParentForInsert(self) -> EntityDescriptor:
        """ Get: ParentForInsert(self: EntityDescriptor) -> EntityDescriptor """
        ...

    @property
    def ParentPropertyForInsert(self) -> str:
        """ Get: ParentPropertyForInsert(self: EntityDescriptor) -> str """
        ...

    @property
    def ReadStreamUri(self) -> Uri:
        """ Get: ReadStreamUri(self: EntityDescriptor) -> Uri """
        ...

    @property
    def SelfLink(self) -> Uri:
        """ Get: SelfLink(self: EntityDescriptor) -> Uri """
        ...

    @property
    def ServerTypeName(self) -> str:
        """ Get: ServerTypeName(self: EntityDescriptor) -> str """
        ...

    @property
    def StreamETag(self) -> str:
        """ Get: StreamETag(self: EntityDescriptor) -> str """
        ...



class EntityStates(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EntityStates, values: Added (4), Deleted (8), Detached (1), Modified (16), Unchanged (2) """
    Added: EntityStates = ...
    Deleted: EntityStates = ...
    Detached: EntityStates = ...
    Modified: EntityStates = ...
    Unchanged: EntityStates = ...
    value__ = ...


class LinkDescriptor(Descriptor): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Source(self) -> object:
        """ Get: Source(self: LinkDescriptor) -> object """
        ...

    @property
    def SourceProperty(self) -> str:
        """ Get: SourceProperty(self: LinkDescriptor) -> str """
        ...

    @property
    def Target(self) -> object:
        """ Get: Target(self: LinkDescriptor) -> object """
        ...



class MediaEntryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MediaEntryAttribute(mediaMemberName: str) """
    @property
    def MediaMemberName(self) -> str:
        """ Get: MediaMemberName(self: MediaEntryAttribute) -> str """
        ...


    def __new__(cls, mediaMemberName:str) -> Self:
        """ __new__(cls: type, mediaMemberName: str) """
        ...


class MergeOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MergeOption, values: AppendOnly (0), NoTracking (3), OverwriteChanges (1), PreserveChanges (2) """
    AppendOnly: MergeOption = ...
    NoTracking: MergeOption = ...
    OverwriteChanges: MergeOption = ...
    PreserveChanges: MergeOption = ...
    value__ = ...


class MimeTypePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MimeTypePropertyAttribute(dataPropertyName: str, mimeTypePropertyName: str) """
    @property
    def DataPropertyName(self) -> str:
        """ Get: DataPropertyName(self: MimeTypePropertyAttribute) -> str """
        ...

    @property
    def MimeTypePropertyName(self) -> str:
        """ Get: MimeTypePropertyName(self: MimeTypePropertyAttribute) -> str """
        ...


    def __new__(cls, dataPropertyName:str, mimeTypePropertyName:str) -> Self:
        """ __new__(cls: type, dataPropertyName: str, mimeTypePropertyName: str) """
        ...


class QueryOperationResponse: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Query(self) -> DataServiceRequest:
        """ Get: Query(self: QueryOperationResponse) -> DataServiceRequest """
        ...

    @property
    def TotalCount(self) -> Int64:
        """ Get: TotalCount(self: QueryOperationResponse) -> Int64 """
        ...


    def GetContinuation(self, collection:IEnumerable = ...) -> DataServiceQueryContinuation:
        """
        GetContinuation(self: QueryOperationResponse) -> DataServiceQueryContinuation
        GetContinuation(self: QueryOperationResponse, collection: IEnumerable) -> DataServiceQueryContinuation
        GetContinuation[T](self: QueryOperationResponse, collection: IEnumerable[T]) -> DataServiceQueryContinuation[T]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: QueryOperationResponse) -> IEnumerator """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class ReadingWritingEntityEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Data(self) -> XElement:
        """ Get: Data(self: ReadingWritingEntityEventArgs) -> XElement """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: ReadingWritingEntityEventArgs) -> object """
        ...



class SaveChangesOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SaveChangesOptions, values: Batch (1), ContinueOnError (2), None (0), ReplaceOnUpdate (4) """
    Batch: SaveChangesOptions = ...
    ContinueOnError: SaveChangesOptions = ...
    ReplaceOnUpdate: SaveChangesOptions = ...
    value__ = ...


class SendingRequestEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Request(self) -> WebRequest:
        """
        Get: Request(self: SendingRequestEventArgs) -> WebRequest
        Set: Request(self: SendingRequestEventArgs) = value
        """
        ...

    @property
    def RequestHeaders(self) -> WebHeaderCollection:
        """ Get: RequestHeaders(self: SendingRequestEventArgs) -> WebHeaderCollection """
        ...



class TrackingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrackingMode, values: AutoChangeTracking (1), None (0) """
    AutoChangeTracking: TrackingMode = ...
    value__ = ...


