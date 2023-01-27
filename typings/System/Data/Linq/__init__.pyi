# encoding: utf-8
# module System.Data.Linq calls itself Linq
# from System.Data.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Enum, IDisposable, IEquatable, 
    InvalidOperationException, Type)

from System.Collections import ICollection, IEnumerable, IEnumerator, IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import IBindingList, IListSource

from System.Data.Common import (DbCommand, DbConnection, DbDataReader, 
    DbTransaction)

from System.Data.Linq.Mapping import MetaModel

from System.IO import TextWriter

from System.Linq import IQueryProvider, IQueryable

from System.Linq.Expressions import Expression, LambdaExpression

from System.Reflection import MemberInfo

"""The following names are not found in the module: (BoundEvent, Func, T, 
    TEntity, field#)
"""

# no functions
# classes

class Binary(IEquatable): # skipped bases: <type 'object'>
    """ Binary(value: Array[Byte]) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: Binary) -> int """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: Binary) -> int """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: Binary) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: Binary) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ChangeAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ChangeAction, values: Delete (1), Insert (2), None (0), Update (3) """
    Delete: ChangeAction = ...
    Insert: ChangeAction = ...
    Update: ChangeAction = ...
    value__ = ...


class ChangeConflictCollection(ICollection): # skipped bases: <type 'IEnumerable[ObjectChangeConflict]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ChangeConflictCollection) -> IEnumerator[ObjectChangeConflict] """
        ...

    def ResolveAll(self, mode:RefreshMode, autoResolveDeletes:bool = ...): # -> 
        """ ResolveAll(self: ChangeConflictCollection, mode: RefreshMode)ResolveAll(self: ChangeConflictCollection, mode: RefreshMode, autoResolveDeletes: bool) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ChangeConflictException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ChangeConflictException()
    ChangeConflictException(message: str)
    ChangeConflictException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ChangeSet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Deletes(self) -> IList:
        """ Get: Deletes(self: ChangeSet) -> IList[object] """
        ...

    @property
    def Inserts(self) -> IList:
        """ Get: Inserts(self: ChangeSet) -> IList[object] """
        ...

    @property
    def Updates(self) -> IList:
        """ Get: Updates(self: ChangeSet) -> IList[object] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ChangeSet) -> str """
        ...


class CompiledQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> LambdaExpression:
        """ Get: Expression(self: CompiledQuery) -> LambdaExpression """
        ...


    @staticmethod
    def Compile(query:Expression): # -> Func
        """
        Compile[(TArg0, TResult)](query: Expression[Func[TArg0, TResult]]) -> Func[TArg0, TResult]
        Compile[(TArg0, TArg1, TResult)](query: Expression[Func[TArg0, TArg1, TResult]]) -> Func[TArg0, TArg1, TResult]
        Compile[(TArg0, TArg1, TArg2, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TResult]]) -> Func[TArg0, TArg1, TArg2, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult]
        """
        ...


class ConflictMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConflictMode, values: ContinueOnConflict (1), FailOnFirstConflict (0) """
    ContinueOnConflict: ConflictMode = ...
    FailOnFirstConflict: ConflictMode = ...
    value__ = ...


class DataContext(IDisposable): # skipped bases: <type 'object'>
    """
    DataContext(fileOrServerOrConnection: str)
    DataContext(fileOrServerOrConnection: str, mapping: MappingSource)
    DataContext(connection: IDbConnection)
    DataContext(connection: IDbConnection, mapping: MappingSource)
    """
    @property
    def ChangeConflicts(self) -> ChangeConflictCollection:
        """ Get: ChangeConflicts(self: DataContext) -> ChangeConflictCollection """
        ...

    @property
    def CommandTimeout(self) -> int:
        """
        Get: CommandTimeout(self: DataContext) -> int
        Set: CommandTimeout(self: DataContext) = value
        """
        ...

    @property
    def Connection(self) -> DbConnection:
        """ Get: Connection(self: DataContext) -> DbConnection """
        ...

    @property
    def DeferredLoadingEnabled(self) -> bool:
        """
        Get: DeferredLoadingEnabled(self: DataContext) -> bool
        Set: DeferredLoadingEnabled(self: DataContext) = value
        """
        ...

    @property
    def LoadOptions(self) -> DataLoadOptions:
        """
        Get: LoadOptions(self: DataContext) -> DataLoadOptions
        Set: LoadOptions(self: DataContext) = value
        """
        ...

    @property
    def Log(self) -> TextWriter:
        """
        Get: Log(self: DataContext) -> TextWriter
        Set: Log(self: DataContext) = value
        """
        ...

    @property
    def Mapping(self) -> MetaModel:
        """ Get: Mapping(self: DataContext) -> MetaModel """
        ...

    @property
    def ObjectTrackingEnabled(self) -> bool:
        """
        Get: ObjectTrackingEnabled(self: DataContext) -> bool
        Set: ObjectTrackingEnabled(self: DataContext) = value
        """
        ...

    @property
    def Transaction(self) -> DbTransaction:
        """
        Get: Transaction(self: DataContext) -> DbTransaction
        Set: Transaction(self: DataContext) = value
        """
        ...


    def CreateDatabase(self): # -> 
        """ CreateDatabase(self: DataContext) """
        ...

    def CreateMethodCallQuery(self, *args): #cannot find CLR method
        """ CreateMethodCallQuery[TResult](self: DataContext, instance: object, methodInfo: MethodInfo, *parameters: Array[object]) -> IQueryable[TResult] """
        ...

    def DatabaseExists(self) -> bool:
        """ DatabaseExists(self: DataContext) -> bool """
        ...

    def DeleteDatabase(self): # -> 
        """ DeleteDatabase(self: DataContext) """
        ...

    def ExecuteCommand(self, command:str, parameters:Array) -> int:
        """ ExecuteCommand(self: DataContext, command: str, *parameters: Array[object]) -> int """
        ...

    def ExecuteDynamicDelete(self, *args): #cannot find CLR method
        """ ExecuteDynamicDelete(self: DataContext, entity: object) """
        ...

    def ExecuteDynamicInsert(self, *args): #cannot find CLR method
        """ ExecuteDynamicInsert(self: DataContext, entity: object) """
        ...

    def ExecuteDynamicUpdate(self, *args): #cannot find CLR method
        """ ExecuteDynamicUpdate(self: DataContext, entity: object) """
        ...

    def ExecuteMethodCall(self, *args): #cannot find CLR method
        """ ExecuteMethodCall(self: DataContext, instance: object, methodInfo: MethodInfo, *parameters: Array[object]) -> IExecuteResult """
        ...

    def ExecuteQuery(self, *__args) -> IEnumerable:
        """
        ExecuteQuery[TResult](self: DataContext, query: str, *parameters: Array[object]) -> IEnumerable[TResult]
        ExecuteQuery(self: DataContext, elementType: Type, query: str, *parameters: Array[object]) -> IEnumerable
        """
        ...

    def GetChangeSet(self) -> ChangeSet:
        """ GetChangeSet(self: DataContext) -> ChangeSet """
        ...

    def GetCommand(self, query:IQueryable) -> DbCommand:
        """ GetCommand(self: DataContext, query: IQueryable) -> DbCommand """
        ...

    def GetTable(self, type:Type = ...) -> ITable:
        """
        GetTable(self: DataContext, type: Type) -> ITable
        GetTable[TEntity](self: DataContext) -> Table[TEntity]
        """
        ...

    def Refresh(self, mode:RefreshMode, *__args:object): # -> 
        """ Refresh(self: DataContext, mode: RefreshMode, entity: object)Refresh(self: DataContext, mode: RefreshMode, *entities: Array[object])Refresh(self: DataContext, mode: RefreshMode, entities: IEnumerable) """
        ...

    def SubmitChanges(self, failureMode:ConflictMode = ...): # -> 
        """ SubmitChanges(self: DataContext)SubmitChanges(self: DataContext, failureMode: ConflictMode) """
        ...

    def Translate(self, *__args:DbDataReader) -> IMultipleResults:
        """
        Translate(self: DataContext, elementType: Type, reader: DbDataReader) -> IEnumerable
        Translate(self: DataContext, reader: DbDataReader) -> IMultipleResults
        Translate[TResult](self: DataContext, reader: DbDataReader) -> IEnumerable[TResult]
        """
        ...


class DataLoadOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ DataLoadOptions() """
    def AssociateWith(self, expression:LambdaExpression): # -> 
        """ AssociateWith(self: DataLoadOptions, expression: LambdaExpression)AssociateWith[T](self: DataLoadOptions, expression: Expression[Func[T, object]]) """
        ...

    def LoadWith(self, expression:LambdaExpression): # -> 
        """ LoadWith(self: DataLoadOptions, expression: LambdaExpression)LoadWith[T](self: DataLoadOptions, expression: Expression[Func[T, object]]) """
        ...


class DBConvert: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ChangeType(value:object, type:Type = ...) -> object:
        """
        ChangeType[T](value: object) -> T
        ChangeType(value: object, type: Type) -> object
        """
        ...

    __all__: list = ...


class DuplicateKeyException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DuplicateKeyException(duplicate: object)
    DuplicateKeyException(duplicate: object, message: str)
    DuplicateKeyException(duplicate: object, message: str, innerException: Exception)
    """
    @property
    def Object(self) -> object:
        """ Get: Object(self: DuplicateKeyException) -> object """
        ...


    SerializeObjectState = ...


class EntityRef: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityRef[TEntity](entity: TEntity)
    EntityRef[TEntity](source: IEnumerable[TEntity])
    EntityRef[TEntity](entityRef: EntityRef[TEntity])
    """
    @property
    def Entity(self): # -> TEntity
        """
        Get: Entity(self: EntityRef[TEntity]) -> TEntity
        Set: Entity(self: EntityRef[TEntity]) = value
        """
        ...

    @property
    def HasLoadedOrAssignedValue(self) -> bool:
        """ Get: HasLoadedOrAssignedValue(self: EntityRef[TEntity]) -> bool """
        ...



class EntitySet(IList, IListSource): # skipped bases: <type 'IEnumerable[TEntity]'>, <type 'ICollection[TEntity]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    EntitySet[TEntity]()
    EntitySet[TEntity](onAdd: Action[TEntity], onRemove: Action[TEntity])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: EntitySet[TEntity]) -> int """
        ...

    @property
    def HasLoadedOrAssignedValues(self) -> bool:
        """ Get: HasLoadedOrAssignedValues(self: EntitySet[TEntity]) -> bool """
        ...

    @property
    def IsDeferred(self) -> bool:
        """ Get: IsDeferred(self: EntitySet[TEntity]) -> bool """
        ...


    def AddRange(self, collection:IEnumerable): # -> 
        """ AddRange(self: EntitySet[TEntity], collection: IEnumerable[TEntity]) """
        ...

    def Assign(self, entitySource:IEnumerable): # -> 
        """ Assign(self: EntitySet[TEntity], entitySource: IEnumerable[TEntity]) """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: EntitySet[TEntity], array: Array[TEntity], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: EntitySet[TEntity]) -> IEnumerator[TEntity] """
        ...

    def GetNewBindingList(self) -> IBindingList:
        """ GetNewBindingList(self: EntitySet[TEntity]) -> IBindingList """
        ...

    def Load(self): # -> 
        """ Load(self: EntitySet[TEntity]) """
        ...

    def SetSource(self, entitySource:IEnumerable): # -> 
        """ SetSource(self: EntitySet[TEntity], entitySource: IEnumerable[TEntity]) """
        ...

    ListChanged = ...


class ForeignKeyReferenceAlreadyHasValueException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ForeignKeyReferenceAlreadyHasValueException()
    ForeignKeyReferenceAlreadyHasValueException(message: str)
    ForeignKeyReferenceAlreadyHasValueException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IExecuteResult(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReturnValue(self) -> object:
        """ Get: ReturnValue(self: IExecuteResult) -> object """
        ...


    def GetParameterValue(self, parameterIndex:int) -> object:
        """ GetParameterValue(self: IExecuteResult, parameterIndex: int) -> object """
        ...


class IFunctionResult: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReturnValue(self) -> object:
        """ Get: ReturnValue(self: IFunctionResult) -> object """
        ...



class IMultipleResults(IFunctionResult, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetResult(self) -> IEnumerable:
        """ GetResult[TElement](self: IMultipleResults) -> IEnumerable[TElement] """
        ...


class ISingleResult(IFunctionResult, IDisposable, IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...


class ITable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> DataContext:
        """ Get: Context(self: ITable) -> DataContext """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ITable) -> bool """
        ...


    def Attach(self, entity:object, *__args:bool): # -> 
        """ Attach(self: ITable, entity: object)Attach(self: ITable, entity: object, asModified: bool)Attach(self: ITable, entity: object, original: object) """
        ...

    def AttachAll(self, entities:IEnumerable, asModified:bool = ...): # -> 
        """ AttachAll(self: ITable, entities: IEnumerable)AttachAll(self: ITable, entities: IEnumerable, asModified: bool) """
        ...

    def DeleteAllOnSubmit(self, entities:IEnumerable): # -> 
        """ DeleteAllOnSubmit(self: ITable, entities: IEnumerable) """
        ...

    def DeleteOnSubmit(self, entity:object): # -> 
        """ DeleteOnSubmit(self: ITable, entity: object) """
        ...

    def GetModifiedMembers(self, entity:object) -> Array:
        """ GetModifiedMembers(self: ITable, entity: object) -> Array[ModifiedMemberInfo] """
        ...

    def GetOriginalEntityState(self, entity:object) -> object:
        """ GetOriginalEntityState(self: ITable, entity: object) -> object """
        ...

    def InsertAllOnSubmit(self, entities:IEnumerable): # -> 
        """ InsertAllOnSubmit(self: ITable, entities: IEnumerable) """
        ...

    def InsertOnSubmit(self, entity:object): # -> 
        """ InsertOnSubmit(self: ITable, entity: object) """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class Link: # skipped bases: <type 'object'>, <type 'object'>
    """
    Link[T](value: T)
    Link[T](source: IEnumerable[T])
    Link[T](link: Link[T])
    """
    @property
    def HasLoadedOrAssignedValue(self) -> bool:
        """ Get: HasLoadedOrAssignedValue(self: Link[T]) -> bool """
        ...

    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: Link[T]) -> bool """
        ...

    @property
    def Value(self): # -> T
        """
        Get: Value(self: Link[T]) -> T
        Set: Value(self: Link[T]) = value
        """
        ...



class MemberChangeConflict: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentValue(self) -> object:
        """ Get: CurrentValue(self: MemberChangeConflict) -> object """
        ...

    @property
    def DatabaseValue(self) -> object:
        """ Get: DatabaseValue(self: MemberChangeConflict) -> object """
        ...

    @property
    def IsModified(self) -> bool:
        """ Get: IsModified(self: MemberChangeConflict) -> bool """
        ...

    @property
    def IsResolved(self) -> bool:
        """ Get: IsResolved(self: MemberChangeConflict) -> bool """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: MemberChangeConflict) -> MemberInfo """
        ...

    @property
    def OriginalValue(self) -> object:
        """ Get: OriginalValue(self: MemberChangeConflict) -> object """
        ...


    def Resolve(self, *__args:object): # -> 
        """ Resolve(self: MemberChangeConflict, value: object)Resolve(self: MemberChangeConflict, refreshMode: RefreshMode) """
        ...


class ModifiedMemberInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentValue(self) -> object:
        """ Get: CurrentValue(self: ModifiedMemberInfo) -> object """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: ModifiedMemberInfo) -> MemberInfo """
        ...

    @property
    def OriginalValue(self) -> object:
        """ Get: OriginalValue(self: ModifiedMemberInfo) -> object """
        ...



class ObjectChangeConflict: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsDeleted(self) -> bool:
        """ Get: IsDeleted(self: ObjectChangeConflict) -> bool """
        ...

    @property
    def IsResolved(self) -> bool:
        """ Get: IsResolved(self: ObjectChangeConflict) -> bool """
        ...

    @property
    def MemberConflicts(self) -> ReadOnlyCollection:
        """ Get: MemberConflicts(self: ObjectChangeConflict) -> ReadOnlyCollection[MemberChangeConflict] """
        ...

    @property
    def Object(self) -> object:
        """ Get: Object(self: ObjectChangeConflict) -> object """
        ...


    def Resolve(self, refreshMode:RefreshMode = ..., autoResolveDeletes:bool = ...): # -> 
        """ Resolve(self: ObjectChangeConflict)Resolve(self: ObjectChangeConflict, refreshMode: RefreshMode)Resolve(self: ObjectChangeConflict, refreshMode: RefreshMode, autoResolveDeletes: bool) """
        ...


class RefreshMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RefreshMode, values: KeepChanges (1), KeepCurrentValues (0), OverwriteCurrentValues (2) """
    KeepChanges: RefreshMode = ...
    KeepCurrentValues: RefreshMode = ...
    OverwriteCurrentValues: RefreshMode = ...
    value__ = ...


class Table(IQueryProvider, IListSource, ITable): # skipped bases: <type 'IEnumerable[TEntity]'>, <type 'IEnumerable'>, <type 'IQueryable'>, <type 'IQueryable[TEntity]'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Table[TEntity]) -> IEnumerator[TEntity] """
        ...

    def GetNewBindingList(self) -> IBindingList:
        """ GetNewBindingList(self: Table[TEntity]) -> IBindingList """
        ...

    def ToString(self) -> str:
        """ ToString(self: Table[TEntity]) -> str """
        ...


# variables with complex values

