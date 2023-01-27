# encoding: utf-8
# module System.Activities calls itself Activities
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Activities.DurableInstancing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Action, AsyncCallback, Attribute, Enum, EventArgs, Guid, 
    IAsyncResult, IDisposable, IEquatable, IntPtr, MulticastDelegate, 
    SystemException, TimeSpan, Type, Version)

from System.Activities.DynamicUpdate import DynamicUpdateMap

from System.Activities.Hosting import (WorkflowInstance, 
    WorkflowInstanceExtensionManager)

from System.Activities.Tracking import CustomTrackingRecord

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.Generic import List

from System.Collections.ObjectModel import (KeyedCollection, 
    ReadOnlyCollection)

from System.ComponentModel import (AsyncCompletedEventArgs, 
    CustomTypeDescriptor, INotifyPropertyChanged)

from System.Runtime.DurableInstancing import InstanceStore

from System.Transactions import Transaction

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (ActivityFunc, BoundEvent, 
    Func, IActivityReferenceWithEnvironment, T, THandle, field#)
"""

# no functions
# classes

class Activity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheId(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: Activity) -> str
        Set: DisplayName(self: Activity) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: Activity) -> str """
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...


    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: Activity, metadata: ActivityMetadata) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: Activity, metadata: UpdateMapMetadata, originalActivity: Activity) """
        ...

    def ShouldSerializeDisplayName(self) -> bool:
        """ ShouldSerializeDisplayName(self: Activity) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: Activity) -> str """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ActivityAction: # skipped bases: <type 'object'>
    """ ActivityAction() """
    def GetResultArgument(self, *args): #cannot find CLR method
        """ GetResultArgument(self: ActivityDelegate) -> DelegateOutArgument """
        ...

    def OnGetRuntimeDelegateArguments(self, *args): #cannot find CLR method
        """ OnGetRuntimeDelegateArguments(self: ActivityDelegate, runtimeDelegateArguments: IList[RuntimeDelegateArgument]) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ActivityBuilder: # skipped bases: <type 'object'>
    """ ActivityBuilder() """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: ActivityBuilder) -> Collection[Attribute] """
        ...

    @property
    def Constraints(self) -> Collection:
        """ Get: Constraints(self: ActivityBuilder) -> Collection[Constraint] """
        ...

    @property
    def Implementation(self) -> Activity:
        """
        Get: Implementation(self: ActivityBuilder) -> Activity
        Set: Implementation(self: ActivityBuilder) = value
        """
        ...

    @property
    def ImplementationVersion(self) -> Version:
        """
        Get: ImplementationVersion(self: ActivityBuilder) -> Version
        Set: ImplementationVersion(self: ActivityBuilder) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ActivityBuilder) -> str
        Set: Name(self: ActivityBuilder) = value
        """
        ...

    @property
    def Properties(self) -> KeyedCollection:
        """ Get: Properties(self: ActivityBuilder) -> KeyedCollection[str, DynamicActivityProperty] """
        ...


    @staticmethod
    def GetPropertyReference(target:object) -> ActivityPropertyReference:
        """ GetPropertyReference(target: object) -> ActivityPropertyReference """
        ...

    @staticmethod
    def GetPropertyReferences(target:object) -> IList:
        """ GetPropertyReferences(target: object) -> IList[ActivityPropertyReference] """
        ...

    @staticmethod
    def SetPropertyReference(target:object, value:ActivityPropertyReference): # -> 
        """ SetPropertyReference(target: object, value: ActivityPropertyReference) """
        ...

    @staticmethod
    def ShouldSerializePropertyReference(target:object) -> bool:
        """ ShouldSerializePropertyReference(target: object) -> bool """
        ...

    @staticmethod
    def ShouldSerializePropertyReferences(target:object) -> bool:
        """ ShouldSerializePropertyReferences(target: object) -> bool """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class ActivityContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityInstanceId(self) -> str:
        """ Get: ActivityInstanceId(self: ActivityContext) -> str """
        ...

    @property
    def DataContext(self) -> WorkflowDataContext:
        """ Get: DataContext(self: ActivityContext) -> WorkflowDataContext """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId(self: ActivityContext) -> Guid """
        ...


    def GetExtension(self): # -> T
        """ GetExtension[T](self: ActivityContext) -> T """
        ...

    def GetLocation(self, locationReference:LocationReference) -> Location:
        """ GetLocation[T](self: ActivityContext, locationReference: LocationReference) -> Location[T] """
        ...

    def GetValue(self, *__args:LocationReference): # -> T
        """
        GetValue[T](self: ActivityContext, locationReference: LocationReference) -> T
        GetValue[T](self: ActivityContext, argument: OutArgument[T]) -> T
        GetValue[T](self: ActivityContext, argument: InOutArgument[T]) -> T
        GetValue[T](self: ActivityContext, argument: InArgument[T]) -> T
        GetValue(self: ActivityContext, argument: Argument) -> object
        GetValue(self: ActivityContext, runtimeArgument: RuntimeArgument) -> object
        """
        ...

    def SetValue(self, *__args): # -> 
        """ SetValue[T](self: ActivityContext, locationReference: LocationReference, value: T)SetValue[T](self: ActivityContext, argument: OutArgument[T], value: T)SetValue[T](self: ActivityContext, argument: InOutArgument[T], value: T)SetValue[T](self: ActivityContext, argument: InArgument[T], value: T)SetValue(self: ActivityContext, argument: Argument, value: object) """
        ...


class ActivityDelegate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ActivityDelegate) -> str
        Set: DisplayName(self: ActivityDelegate) = value
        """
        ...

    @property
    def Handler(self) -> Activity:
        """
        Get: Handler(self: ActivityDelegate) -> Activity
        Set: Handler(self: ActivityDelegate) = value
        """
        ...


    def GetResultArgument(self, *args): #cannot find CLR method
        """ GetResultArgument(self: ActivityDelegate) -> DelegateOutArgument """
        ...

    def OnGetRuntimeDelegateArguments(self, *args): #cannot find CLR method
        """ OnGetRuntimeDelegateArguments(self: ActivityDelegate, runtimeDelegateArguments: IList[RuntimeDelegateArgument]) """
        ...

    def ShouldSerializeDisplayName(self) -> bool:
        """ ShouldSerializeDisplayName(self: ActivityDelegate) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActivityDelegate) -> str """
        ...


class ActivityInstance(IActivityReferenceWithEnvironment): # skipped bases: <type 'IActivityReference'>, <type 'object'>
    """ no doc """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityInstance) -> Activity """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: ActivityInstance) -> str """
        ...

    @property
    def ImplementationVersion(self) -> Version:
        """ Get: ImplementationVersion(self: ActivityInstance) -> Version """
        ...

    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: ActivityInstance) -> bool """
        ...

    @property
    def State(self) -> ActivityInstanceState:
        """ Get: State(self: ActivityInstance) -> ActivityInstanceState """
        ...



class ActivityInstanceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivityInstanceState, values: Canceled (2), Closed (1), Executing (0), Faulted (3) """
    Canceled: ActivityInstanceState = ...
    Closed: ActivityInstanceState = ...
    Executing: ActivityInstanceState = ...
    Faulted: ActivityInstanceState = ...
    value__ = ...


class ActivityMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Environment(self) -> LocationReferenceEnvironment:
        """ Get: Environment(self: ActivityMetadata) -> LocationReferenceEnvironment """
        ...

    @property
    def HasViolations(self) -> bool:
        """ Get: HasViolations(self: ActivityMetadata) -> bool """
        ...


    def AddArgument(self, argument:RuntimeArgument): # -> 
        """ AddArgument(self: ActivityMetadata, argument: RuntimeArgument) """
        ...

    def AddDefaultExtensionProvider(self, extensionProvider): # ->  # Not found arg types: {'extensionProvider': 'Func'}
        """ AddDefaultExtensionProvider[T](self: ActivityMetadata, extensionProvider: Func[T]) """
        ...

    def AddImportedChild(self, importedChild:Activity, origin:object = ...): # -> 
        """ AddImportedChild(self: ActivityMetadata, importedChild: Activity)AddImportedChild(self: ActivityMetadata, importedChild: Activity, origin: object) """
        ...

    def AddImportedDelegate(self, importedDelegate:ActivityDelegate, origin:object = ...): # -> 
        """ AddImportedDelegate(self: ActivityMetadata, importedDelegate: ActivityDelegate)AddImportedDelegate(self: ActivityMetadata, importedDelegate: ActivityDelegate, origin: object) """
        ...

    def AddValidationError(self, *__args:str): # -> 
        """ AddValidationError(self: ActivityMetadata, validationErrorMessage: str)AddValidationError(self: ActivityMetadata, validationError: ValidationError) """
        ...

    def AddVariable(self, variable:Variable, origin:object = ...): # -> 
        """ AddVariable(self: ActivityMetadata, variable: Variable)AddVariable(self: ActivityMetadata, variable: Variable, origin: object) """
        ...

    def Bind(self, binding:Argument, argument:RuntimeArgument): # -> 
        """ Bind(self: ActivityMetadata, binding: Argument, argument: RuntimeArgument) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ActivityMetadata, obj: object) -> bool """
        ...

    def GetArgumentsWithReflection(self) -> Collection:
        """ GetArgumentsWithReflection(self: ActivityMetadata) -> Collection[RuntimeArgument] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ActivityMetadata) -> int """
        ...

    def GetImportedChildrenWithReflection(self) -> Collection:
        """ GetImportedChildrenWithReflection(self: ActivityMetadata) -> Collection[Activity] """
        ...

    def GetImportedDelegatesWithReflection(self) -> Collection:
        """ GetImportedDelegatesWithReflection(self: ActivityMetadata) -> Collection[ActivityDelegate] """
        ...

    def GetVariablesWithReflection(self) -> Collection:
        """ GetVariablesWithReflection(self: ActivityMetadata) -> Collection[Variable] """
        ...

    def RequireExtension(self, extensionType:Type = ...): # -> 
        """ RequireExtension[T](self: ActivityMetadata)RequireExtension(self: ActivityMetadata, extensionType: Type) """
        ...

    def SetArgumentsCollection(self, arguments:Collection): # -> 
        """ SetArgumentsCollection(self: ActivityMetadata, arguments: Collection[RuntimeArgument]) """
        ...

    def SetImportedChildrenCollection(self, importedChildren:Collection): # -> 
        """ SetImportedChildrenCollection(self: ActivityMetadata, importedChildren: Collection[Activity]) """
        ...

    def SetImportedDelegatesCollection(self, importedDelegates:Collection): # -> 
        """ SetImportedDelegatesCollection(self: ActivityMetadata, importedDelegates: Collection[ActivityDelegate]) """
        ...

    def SetValidationErrorsCollection(self, validationErrors:Collection): # -> 
        """ SetValidationErrorsCollection(self: ActivityMetadata, validationErrors: Collection[ValidationError]) """
        ...

    def SetVariablesCollection(self, variables:Collection): # -> 
        """ SetVariablesCollection(self: ActivityMetadata, variables: Collection[Variable]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ActivityPropertyReference: # skipped bases: <type 'object'>, <type 'object'>
    """ ActivityPropertyReference() """
    @property
    def SourceProperty(self) -> str:
        """
        Get: SourceProperty(self: ActivityPropertyReference) -> str
        Set: SourceProperty(self: ActivityPropertyReference) = value
        """
        ...

    @property
    def TargetProperty(self) -> str:
        """
        Get: TargetProperty(self: ActivityPropertyReference) -> str
        Set: TargetProperty(self: ActivityPropertyReference) = value
        """
        ...



class ActivityWithResult(Activity): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> OutArgument:
        """
        Get: Result(self: ActivityWithResult) -> OutArgument
        Set: Result(self: ActivityWithResult) = value
        """
        ...

    @property
    def ResultType(self) -> Type:
        """ Get: ResultType(self: ActivityWithResult) -> Type """
        ...



class Argument: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ArgumentType(self) -> Type:
        """ Get: ArgumentType(self: Argument) -> Type """
        ...

    @property
    def Direction(self) -> ArgumentDirection:
        """ Get: Direction(self: Argument) -> ArgumentDirection """
        ...

    @property
    def EvaluationOrder(self) -> int:
        """
        Get: EvaluationOrder(self: Argument) -> int
        Set: EvaluationOrder(self: Argument) = value
        """
        ...

    @property
    def Expression(self) -> ActivityWithResult:
        """
        Get: Expression(self: Argument) -> ActivityWithResult
        Set: Expression(self: Argument) = value
        """
        ...


    @staticmethod
    def Create(type:Type, direction:ArgumentDirection) -> Argument:
        """ Create(type: Type, direction: ArgumentDirection) -> Argument """
        ...

    @staticmethod
    def CreateReference(argumentToReference:Argument, referencedArgumentName:str) -> Argument:
        """ CreateReference(argumentToReference: Argument, referencedArgumentName: str) -> Argument """
        ...

    def Get(self, context:ActivityContext) -> object:
        """
        Get(self: Argument, context: ActivityContext) -> object
        Get[T](self: Argument, context: ActivityContext) -> T
        """
        ...

    def GetLocation(self, context:ActivityContext) -> Location:
        """ GetLocation(self: Argument, context: ActivityContext) -> Location """
        ...

    def Set(self, context:ActivityContext, value:object): # -> 
        """ Set(self: Argument, context: ActivityContext, value: object) """
        ...

    ResultValue: str = ...
    UnspecifiedEvaluationOrder: int = ...


class ArgumentDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ArgumentDirection, values: In (0), InOut (2), Out (1) """
    In: ArgumentDirection = ...
    InOut: ArgumentDirection = ...
    Out: ArgumentDirection = ...
    value__ = ...


class AsyncCodeActivity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheId(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...


    def BeginExecute(self, *args): #cannot find CLR method
        """ BeginExecute(self: AsyncCodeActivity, context: AsyncCodeActivityContext, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: AsyncCodeActivity, metadata: CodeActivityMetadata)CacheMetadata(self: AsyncCodeActivity, metadata: ActivityMetadata) """
        ...

    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: AsyncCodeActivity, context: AsyncCodeActivityContext) """
        ...

    def EndExecute(self, *args): #cannot find CLR method
        """ EndExecute(self: AsyncCodeActivity, context: AsyncCodeActivityContext, result: IAsyncResult) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: AsyncCodeActivity, metadata: UpdateMapMetadata, originalActivity: Activity) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class CodeActivityContext(ActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    def GetProperty(self): # -> THandle
        """ GetProperty[THandle](self: CodeActivityContext) -> THandle """
        ...

    def Track(self, record:CustomTrackingRecord): # -> 
        """ Track(self: CodeActivityContext, record: CustomTrackingRecord) """
        ...


class AsyncCodeActivityContext(CodeActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsCancellationRequested(self) -> bool:
        """ Get: IsCancellationRequested(self: AsyncCodeActivityContext) -> bool """
        ...

    @property
    def UserState(self) -> object:
        """
        Get: UserState(self: AsyncCodeActivityContext) -> object
        Set: UserState(self: AsyncCodeActivityContext) = value
        """
        ...


    def MarkCanceled(self): # -> 
        """ MarkCanceled(self: AsyncCodeActivityContext) """
        ...


class Bookmark(IEquatable): # skipped bases: <type 'object'>
    """ Bookmark(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: Bookmark) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: Bookmark) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Bookmark) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class BookmarkCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BookmarkCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, context:NativeActivityContext, bookmark:Bookmark, value:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BookmarkCallback, context: NativeActivityContext, bookmark: Bookmark, value: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: BookmarkCallback, result: IAsyncResult) """
        ...

    def Invoke(self, context:NativeActivityContext, bookmark:Bookmark, value:object): # -> 
        """ Invoke(self: BookmarkCallback, context: NativeActivityContext, bookmark: Bookmark, value: object) """
        ...


class BookmarkOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) BookmarkOptions, values: MultipleResume (1), NonBlocking (2), None (0) """
    MultipleResume: BookmarkOptions = ...
    NonBlocking: BookmarkOptions = ...
    value__ = ...


class BookmarkResumptionResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BookmarkResumptionResult, values: NotFound (1), NotReady (2), Success (0) """
    NotFound: BookmarkResumptionResult = ...
    NotReady: BookmarkResumptionResult = ...
    Success: BookmarkResumptionResult = ...
    value__ = ...


class BookmarkScope(IEquatable): # skipped bases: <type 'object'>
    """ BookmarkScope(id: Guid) """
    @property
    def Default(self) -> BookmarkScope:
        """ Get: Default() -> BookmarkScope """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: BookmarkScope) -> Guid """
        ...

    @property
    def IsInitialized(self) -> bool:
        """ Get: IsInitialized(self: BookmarkScope) -> bool """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: BookmarkScope) -> int """
        ...

    def Initialize(self, context:NativeActivityContext, id:Guid): # -> 
        """ Initialize(self: BookmarkScope, context: NativeActivityContext, id: Guid) """
        ...



class Handle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExecutionPropertyName(self) -> str:
        """ Get: ExecutionPropertyName(self: Handle) -> str """
        ...

    @property
    def Owner(self) -> ActivityInstance:
        """ Get: Owner(self: Handle) -> ActivityInstance """
        ...


    def OnInitialize(self, *args): #cannot find CLR method
        """ OnInitialize(self: Handle, context: HandleInitializationContext) """
        ...

    def OnUninitialize(self, *args): #cannot find CLR method
        """ OnUninitialize(self: Handle, context: HandleInitializationContext) """
        ...

    def ThrowIfUninitialized(self, *args): #cannot find CLR method
        """ ThrowIfUninitialized(self: Handle) """
        ...


class BookmarkScopeHandle(Handle): # skipped bases: <type 'object'>
    """ BookmarkScopeHandle() """
    @property
    def BookmarkScope(self) -> BookmarkScope:
        """ Get: BookmarkScope(self: BookmarkScopeHandle) -> BookmarkScope """
        ...

    @property
    def Default(self) -> BookmarkScopeHandle:
        """ Get: Default() -> BookmarkScopeHandle """
        ...


    def CreateBookmarkScope(self, context:NativeActivityContext, scopeId:Guid = ...): # -> 
        """ CreateBookmarkScope(self: BookmarkScopeHandle, context: NativeActivityContext)CreateBookmarkScope(self: BookmarkScopeHandle, context: NativeActivityContext, scopeId: Guid) """
        ...

    def Initialize(self, context:NativeActivityContext, scope:Guid): # -> 
        """ Initialize(self: BookmarkScopeHandle, context: NativeActivityContext, scope: Guid) """
        ...



class CodeActivity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheId(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...


    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: CodeActivity, metadata: CodeActivityMetadata)CacheMetadata(self: CodeActivity, metadata: ActivityMetadata) """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: CodeActivity, context: CodeActivityContext) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: CodeActivity, metadata: UpdateMapMetadata, originalActivity: Activity) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class CodeActivityMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Environment(self) -> LocationReferenceEnvironment:
        """ Get: Environment(self: CodeActivityMetadata) -> LocationReferenceEnvironment """
        ...

    @property
    def HasViolations(self) -> bool:
        """ Get: HasViolations(self: CodeActivityMetadata) -> bool """
        ...


    def AddArgument(self, argument:RuntimeArgument): # -> 
        """ AddArgument(self: CodeActivityMetadata, argument: RuntimeArgument) """
        ...

    def AddDefaultExtensionProvider(self, extensionProvider): # ->  # Not found arg types: {'extensionProvider': 'Func'}
        """ AddDefaultExtensionProvider[T](self: CodeActivityMetadata, extensionProvider: Func[T]) """
        ...

    def AddValidationError(self, *__args:str): # -> 
        """ AddValidationError(self: CodeActivityMetadata, validationErrorMessage: str)AddValidationError(self: CodeActivityMetadata, validationError: ValidationError) """
        ...

    def Bind(self, binding:Argument, argument:RuntimeArgument): # -> 
        """ Bind(self: CodeActivityMetadata, binding: Argument, argument: RuntimeArgument) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: CodeActivityMetadata, obj: object) -> bool """
        ...

    def GetArgumentsWithReflection(self) -> Collection:
        """ GetArgumentsWithReflection(self: CodeActivityMetadata) -> Collection[RuntimeArgument] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CodeActivityMetadata) -> int """
        ...

    def RequireExtension(self, extensionType:Type = ...): # -> 
        """ RequireExtension[T](self: CodeActivityMetadata)RequireExtension(self: CodeActivityMetadata, extensionType: Type) """
        ...

    def SetArgumentsCollection(self, arguments:Collection): # -> 
        """ SetArgumentsCollection(self: CodeActivityMetadata, arguments: Collection[RuntimeArgument]) """
        ...

    def SetValidationErrorsCollection(self, validationErrors:Collection): # -> 
        """ SetValidationErrorsCollection(self: CodeActivityMetadata, validationErrors: Collection[ValidationError]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CodeActivityPublicEnvironmentAccessor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityMetadata(self) -> CodeActivityMetadata:
        """ Get: ActivityMetadata(self: CodeActivityPublicEnvironmentAccessor) -> CodeActivityMetadata """
        ...


    @staticmethod
    def Create(metadata:CodeActivityMetadata) -> CodeActivityPublicEnvironmentAccessor:
        """ Create(metadata: CodeActivityMetadata) -> CodeActivityPublicEnvironmentAccessor """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: CodeActivityPublicEnvironmentAccessor, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CodeActivityPublicEnvironmentAccessor) -> int """
        ...

    def TryGetAccessToPublicLocation(self, publicLocation, accessDirection, equivalentLocation) -> Tuple_[bool, LocationReference]:
        """ TryGetAccessToPublicLocation(self: CodeActivityPublicEnvironmentAccessor, publicLocation: LocationReference, accessDirection: ArgumentDirection) -> (bool, LocationReference) """
        ...

    def TryGetReferenceToPublicLocation(self, publicReference, equivalentReference) -> Tuple_[bool, LocationReference]:
        """ TryGetReferenceToPublicLocation(self: CodeActivityPublicEnvironmentAccessor, publicReference: LocationReference) -> (bool, LocationReference) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompletionCallback: # skipped bases: <type 'object'>
    """ CompletionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, context:NativeActivityContext, completedInstance:ActivityInstance, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CompletionCallback, context: NativeActivityContext, completedInstance: ActivityInstance, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        ...

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CompletionCallback, result: IAsyncResult) """
        ...

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        ...

    def Invoke(self, context:NativeActivityContext, completedInstance:ActivityInstance): # -> 
        """ Invoke(self: CompletionCallback, context: NativeActivityContext, completedInstance: ActivityInstance) """
        ...

    def RemoveImpl(self, *args): #cannot find CLR method
        """ RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate """
        ...

    def __new__(cls, object:object, method:IntPtr) -> Self:
        """ __new__(cls: type, object: object, method: IntPtr) """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...


class LocationReference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: LocationReference) -> str """
        ...

    @property
    def NameCore(self):
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: LocationReference) -> Type """
        ...

    @property
    def TypeCore(self):
        ...


    def GetLocation(self, context:ActivityContext) -> Location:
        """ GetLocation(self: LocationReference, context: ActivityContext) -> Location """
        ...


class DelegateArgument(LocationReference): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Direction(self) -> ArgumentDirection:
        """ Get: Direction(self: DelegateArgument) -> ArgumentDirection """
        ...


    def Get(self, context:ActivityContext) -> object:
        """ Get(self: DelegateArgument, context: ActivityContext) -> object """
        ...


class DelegateCompletionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateCompletionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, context:NativeActivityContext, completedInstance:ActivityInstance, outArguments:IDictionary, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateCompletionCallback, context: NativeActivityContext, completedInstance: ActivityInstance, outArguments: IDictionary[str, object], callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DelegateCompletionCallback, result: IAsyncResult) """
        ...

    def Invoke(self, context:NativeActivityContext, completedInstance:ActivityInstance, outArguments:IDictionary): # -> 
        """ Invoke(self: DelegateCompletionCallback, context: NativeActivityContext, completedInstance: ActivityInstance, outArguments: IDictionary[str, object]) """
        ...


class DelegateInArgument: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NameCore(self):
        ...

    @property
    def TypeCore(self):
        ...



class DelegateOutArgument: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NameCore(self):
        ...

    @property
    def TypeCore(self):
        ...



class DynamicActivity: # skipped bases: <type 'object'>
    """ DynamicActivity() """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: DynamicActivity) -> Collection[Attribute] """
        ...

    @property
    def CacheId(self):
        ...

    @property
    def Constraints(self) -> Collection:
        """ Get: Constraints(self: DynamicActivity) -> Collection[Constraint] """
        ...

    @property
    def Implementation(self): # -> Func
        """
        Get: Implementation(self: DynamicActivity) -> Func[Activity]
        Set: Implementation(self: DynamicActivity) = value
        """
        ...

    @property
    def ImplementationVersion(self) -> Version:
        """
        Get: ImplementationVersion(self: DynamicActivity) -> Version
        Set: ImplementationVersion(self: DynamicActivity) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DynamicActivity) -> str
        Set: Name(self: DynamicActivity) = value
        """
        ...

    @property
    def Properties(self) -> KeyedCollection:
        """ Get: Properties(self: DynamicActivity) -> KeyedCollection[str, DynamicActivityProperty] """
        ...


    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: Activity, metadata: ActivityMetadata) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: Activity, metadata: UpdateMapMetadata, originalActivity: Activity) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DynamicActivityProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicActivityProperty() """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: DynamicActivityProperty) -> Collection[Attribute] """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DynamicActivityProperty) -> str
        Set: Name(self: DynamicActivityProperty) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: DynamicActivityProperty) -> Type
        Set: Type(self: DynamicActivityProperty) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: DynamicActivityProperty) -> object
        Set: Value(self: DynamicActivityProperty) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: DynamicActivityProperty) -> str """
        ...


class ExceptionPersistenceExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ ExceptionPersistenceExtension() """
    @property
    def PersistExceptions(self) -> bool:
        """
        Get: PersistExceptions(self: ExceptionPersistenceExtension) -> bool
        Set: PersistExceptions(self: ExceptionPersistenceExtension) = value
        """
        ...



class ExclusiveHandle(Handle): # skipped bases: <type 'object'>
    """ ExclusiveHandle() """
    @property
    def RegisteredBookmarkScopes(self) -> ReadOnlyCollection:
        """ Get: RegisteredBookmarkScopes(self: ExclusiveHandle) -> ReadOnlyCollection[BookmarkScopeHandle] """
        ...


    def RegisterBookmarkScope(self, context:NativeActivityContext, bookmarkScopeHandle:BookmarkScopeHandle): # -> 
        """ RegisterBookmarkScope(self: ExclusiveHandle, context: NativeActivityContext, bookmarkScopeHandle: BookmarkScopeHandle) """
        ...

    def Reinitialize(self, context:NativeActivityContext): # -> 
        """ Reinitialize(self: ExclusiveHandle, context: NativeActivityContext) """
        ...


class ExecutionProperties(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: ExecutionProperties) -> bool """
        ...


    def Add(self, name:str, property:object, onlyVisibleToPublicChildren:bool = ...): # -> 
        """ Add(self: ExecutionProperties, name: str, property: object)Add(self: ExecutionProperties, name: str, property: object, onlyVisibleToPublicChildren: bool) """
        ...

    def Find(self, name:str) -> object:
        """ Find(self: ExecutionProperties, name: str) -> object """
        ...

    def Remove(self, name:str) -> bool:
        """ Remove(self: ExecutionProperties, name: str) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, object]](enumerable: IEnumerable[KeyValuePair[str, object]], value: KeyValuePair[str, object]) -> bool """
        ...


class FaultCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FaultCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, faultContext:NativeActivityFaultContext, propagatedException:Exception, propagatedFrom:ActivityInstance, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FaultCallback, faultContext: NativeActivityFaultContext, propagatedException: Exception, propagatedFrom: ActivityInstance, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FaultCallback, result: IAsyncResult) """
        ...

    def Invoke(self, faultContext:NativeActivityFaultContext, propagatedException:Exception, propagatedFrom:ActivityInstance): # -> 
        """ Invoke(self: FaultCallback, faultContext: NativeActivityFaultContext, propagatedException: Exception, propagatedFrom: ActivityInstance) """
        ...


class HandleInitializationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateAndInitializeHandle(self): # -> THandle
        """ CreateAndInitializeHandle[THandle](self: HandleInitializationContext) -> THandle """
        ...

    def GetExtension(self): # -> T
        """ GetExtension[T](self: HandleInitializationContext) -> T """
        ...

    def UninitializeHandle(self, handle:Handle): # -> 
        """ UninitializeHandle(self: HandleInitializationContext, handle: Handle) """
        ...


class IExecutionProperty: # skipped bases: <type 'object'>
    """ no doc """
    def CleanupWorkflowThread(self): # -> 
        """ CleanupWorkflowThread(self: IExecutionProperty) """
        ...

    def SetupWorkflowThread(self): # -> 
        """ SetupWorkflowThread(self: IExecutionProperty) """
        ...


class InArgument: # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateReference(argumentToReference:InArgument, referencedArgumentName:str) -> InArgument:
        """
        CreateReference(argumentToReference: InArgument, referencedArgumentName: str) -> InArgument
        CreateReference(argumentToReference: InOutArgument, referencedArgumentName: str) -> InArgument
        """
        ...


class InOutArgument: # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateReference(argumentToReference:InOutArgument, referencedArgumentName:str) -> InOutArgument:
        """ CreateReference(argumentToReference: InOutArgument, referencedArgumentName: str) -> InOutArgument """
        ...


class InvalidWorkflowException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidWorkflowException()
    InvalidWorkflowException(message: str)
    InvalidWorkflowException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvokeCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Outputs(self) -> IDictionary:
        """ Get: Outputs(self: InvokeCompletedEventArgs) -> IDictionary[str, object] """
        ...



class IPropertyRegistrationCallback: # skipped bases: <type 'object'>
    """ no doc """
    def Register(self, context:RegistrationContext): # -> 
        """ Register(self: IPropertyRegistrationCallback, context: RegistrationContext) """
        ...

    def Unregister(self, context:RegistrationContext): # -> 
        """ Unregister(self: IPropertyRegistrationCallback, context: RegistrationContext) """
        ...


class Location: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocationType(self) -> Type:
        """ Get: LocationType(self: Location) -> Type """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: Location) -> object
        Set: Value(self: Location) = value
        """
        ...

    @property
    def ValueCore(self):
        ...


    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class LocationReferenceEnvironment: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> LocationReferenceEnvironment:
        """ Get: Parent(self: LocationReferenceEnvironment) -> LocationReferenceEnvironment """
        ...

    @property
    def Root(self) -> Activity:
        """ Get: Root(self: LocationReferenceEnvironment) -> Activity """
        ...


    def GetLocationReferences(self) -> IEnumerable:
        """ GetLocationReferences(self: LocationReferenceEnvironment) -> IEnumerable[LocationReference] """
        ...

    def IsVisible(self, locationReference:LocationReference) -> bool:
        """ IsVisible(self: LocationReferenceEnvironment, locationReference: LocationReference) -> bool """
        ...

    def TryGetLocationReference(self, name, result) -> Tuple_[bool, LocationReference]:
        """ TryGetLocationReference(self: LocationReferenceEnvironment, name: str) -> (bool, LocationReference) """
        ...


class NativeActivity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheId(self):
        ...

    @property
    def CanInduceIdle(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...


    def Abort(self, *args): #cannot find CLR method
        """ Abort(self: NativeActivity, context: NativeActivityAbortContext) """
        ...

    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: NativeActivity, metadata: NativeActivityMetadata)CacheMetadata(self: NativeActivity, metadata: ActivityMetadata) """
        ...

    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: NativeActivity, context: NativeActivityContext) """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: NativeActivity, context: NativeActivityContext) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: NativeActivity, metadata: UpdateMapMetadata, originalActivity: Activity)OnCreateDynamicUpdateMap(self: NativeActivity, metadata: NativeActivityUpdateMapMetadata, originalActivity: Activity) """
        ...

    def UpdateInstance(self, *args): #cannot find CLR method
        """ UpdateInstance(self: NativeActivity, updateContext: NativeActivityUpdateContext) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class NativeActivityAbortContext(ActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: NativeActivityAbortContext) -> Exception """
        ...



class NativeActivityContext(ActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultBookmarkScope(self) -> BookmarkScope:
        """ Get: DefaultBookmarkScope(self: NativeActivityContext) -> BookmarkScope """
        ...

    @property
    def IsCancellationRequested(self) -> bool:
        """ Get: IsCancellationRequested(self: NativeActivityContext) -> bool """
        ...

    @property
    def Properties(self) -> ExecutionProperties:
        """ Get: Properties(self: NativeActivityContext) -> ExecutionProperties """
        ...


    def Abort(self, reason:Exception = ...): # -> 
        """ Abort(self: NativeActivityContext)Abort(self: NativeActivityContext, reason: Exception) """
        ...

    def AbortChildInstance(self, activity:ActivityInstance, reason:Exception = ...): # -> 
        """ AbortChildInstance(self: NativeActivityContext, activity: ActivityInstance)AbortChildInstance(self: NativeActivityContext, activity: ActivityInstance, reason: Exception) """
        ...

    def CancelChild(self, activityInstance:ActivityInstance): # -> 
        """ CancelChild(self: NativeActivityContext, activityInstance: ActivityInstance) """
        ...

    def CancelChildren(self): # -> 
        """ CancelChildren(self: NativeActivityContext) """
        ...

    def CreateBookmark(self, *__args:BookmarkCallback) -> Bookmark:
        """
        CreateBookmark(self: NativeActivityContext, name: str, callback: BookmarkCallback) -> Bookmark
        CreateBookmark(self: NativeActivityContext, name: str, callback: BookmarkCallback, scope: BookmarkScope) -> Bookmark
        CreateBookmark(self: NativeActivityContext) -> Bookmark
        CreateBookmark(self: NativeActivityContext, callback: BookmarkCallback) -> Bookmark
        CreateBookmark(self: NativeActivityContext, name: str, callback: BookmarkCallback, options: BookmarkOptions) -> Bookmark
        CreateBookmark(self: NativeActivityContext, name: str, callback: BookmarkCallback, scope: BookmarkScope, options: BookmarkOptions) -> Bookmark
        CreateBookmark(self: NativeActivityContext, name: str) -> Bookmark
        CreateBookmark(self: NativeActivityContext, callback: BookmarkCallback, options: BookmarkOptions) -> Bookmark
        """
        ...

    def GetChildren(self) -> ReadOnlyCollection:
        """ GetChildren(self: NativeActivityContext) -> ReadOnlyCollection[ActivityInstance] """
        ...

    def MarkCanceled(self): # -> 
        """ MarkCanceled(self: NativeActivityContext) """
        ...

    def RemoveAllBookmarks(self): # -> 
        """ RemoveAllBookmarks(self: NativeActivityContext) """
        ...

    def RemoveBookmark(self, *__args:str) -> bool:
        """
        RemoveBookmark(self: NativeActivityContext, name: str) -> bool
        RemoveBookmark(self: NativeActivityContext, bookmark: Bookmark) -> bool
        RemoveBookmark(self: NativeActivityContext, name: str, scope: BookmarkScope) -> bool
        """
        ...

    def ResumeBookmark(self, bookmark:Bookmark, value:object) -> BookmarkResumptionResult:
        """ ResumeBookmark(self: NativeActivityContext, bookmark: Bookmark, value: object) -> BookmarkResumptionResult """
        ...

    def ScheduleAction(self, activityAction, *__args) -> ActivityInstance:
        """
        ScheduleAction(self: NativeActivityContext, activityAction: ActivityAction, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4], argument1: T1, argument2: T2, argument3: T3, argument4: T4, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3], argument1: T1, argument2: T2, argument3: T3, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2], argument1: T1, argument2: T2, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[T](self: NativeActivityContext, activityAction: ActivityAction[T], argument: T, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](self: NativeActivityContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, argument16: T16, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        """
        ...

    def ScheduleActivity(self, activity:Activity, *__args:CompletionCallback) -> ActivityInstance:
        """
        ScheduleActivity(self: NativeActivityContext, activity: Activity) -> ActivityInstance
        ScheduleActivity(self: NativeActivityContext, activity: Activity, onCompleted: CompletionCallback) -> ActivityInstance
        ScheduleActivity(self: NativeActivityContext, activity: Activity, onFaulted: FaultCallback) -> ActivityInstance
        ScheduleActivity[TResult](self: NativeActivityContext, activity: Activity[TResult], onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleActivity(self: NativeActivityContext, activity: Activity, onCompleted: CompletionCallback, onFaulted: FaultCallback) -> ActivityInstance
        """
        ...

    def ScheduleDelegate(self, activityDelegate:ActivityDelegate, inputParameters:IDictionary, onCompleted:DelegateCompletionCallback, onFaulted:FaultCallback) -> ActivityInstance:
        """ ScheduleDelegate(self: NativeActivityContext, activityDelegate: ActivityDelegate, inputParameters: IDictionary[str, object], onCompleted: DelegateCompletionCallback, onFaulted: FaultCallback) -> ActivityInstance """
        ...

    def ScheduleFunc(self, activityFunc, *__args) -> ActivityInstance:
        """
        ScheduleFunc[TResult](self: NativeActivityContext, activityFunc: ActivityFunc[TResult], onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, TResult], argument1: T1, argument2: T2, argument3: T3, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, TResult], argument1: T1, argument2: T2, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T, TResult], argument: T, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult)](self: NativeActivityContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, argument16: T16, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) -> ActivityInstance
        """
        ...

    def Track(self, record:CustomTrackingRecord): # -> 
        """ Track(self: NativeActivityContext, record: CustomTrackingRecord) """
        ...


class NativeActivityFaultContext(NativeActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    def HandleFault(self): # -> 
        """ HandleFault(self: NativeActivityFaultContext) """
        ...


class NativeActivityMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Environment(self) -> LocationReferenceEnvironment:
        """ Get: Environment(self: NativeActivityMetadata) -> LocationReferenceEnvironment """
        ...

    @property
    def HasViolations(self) -> bool:
        """ Get: HasViolations(self: NativeActivityMetadata) -> bool """
        ...


    def AddArgument(self, argument:RuntimeArgument): # -> 
        """ AddArgument(self: NativeActivityMetadata, argument: RuntimeArgument) """
        ...

    def AddChild(self, child:Activity, origin:object = ...): # -> 
        """ AddChild(self: NativeActivityMetadata, child: Activity)AddChild(self: NativeActivityMetadata, child: Activity, origin: object) """
        ...

    def AddDefaultExtensionProvider(self, extensionProvider): # ->  # Not found arg types: {'extensionProvider': 'Func'}
        """ AddDefaultExtensionProvider[T](self: NativeActivityMetadata, extensionProvider: Func[T]) """
        ...

    def AddDelegate(self, activityDelegate:ActivityDelegate, origin:object = ...): # -> 
        """ AddDelegate(self: NativeActivityMetadata, activityDelegate: ActivityDelegate)AddDelegate(self: NativeActivityMetadata, activityDelegate: ActivityDelegate, origin: object) """
        ...

    def AddImplementationChild(self, implementationChild:Activity): # -> 
        """ AddImplementationChild(self: NativeActivityMetadata, implementationChild: Activity) """
        ...

    def AddImplementationDelegate(self, implementationDelegate:ActivityDelegate): # -> 
        """ AddImplementationDelegate(self: NativeActivityMetadata, implementationDelegate: ActivityDelegate) """
        ...

    def AddImplementationVariable(self, implementationVariable:Variable): # -> 
        """ AddImplementationVariable(self: NativeActivityMetadata, implementationVariable: Variable) """
        ...

    def AddImportedChild(self, importedChild:Activity, origin:object = ...): # -> 
        """ AddImportedChild(self: NativeActivityMetadata, importedChild: Activity)AddImportedChild(self: NativeActivityMetadata, importedChild: Activity, origin: object) """
        ...

    def AddImportedDelegate(self, importedDelegate:ActivityDelegate, origin:object = ...): # -> 
        """ AddImportedDelegate(self: NativeActivityMetadata, importedDelegate: ActivityDelegate)AddImportedDelegate(self: NativeActivityMetadata, importedDelegate: ActivityDelegate, origin: object) """
        ...

    def AddValidationError(self, *__args:str): # -> 
        """ AddValidationError(self: NativeActivityMetadata, validationErrorMessage: str)AddValidationError(self: NativeActivityMetadata, validationError: ValidationError) """
        ...

    def AddVariable(self, variable:Variable, origin:object = ...): # -> 
        """ AddVariable(self: NativeActivityMetadata, variable: Variable)AddVariable(self: NativeActivityMetadata, variable: Variable, origin: object) """
        ...

    def Bind(self, binding:Argument, argument:RuntimeArgument): # -> 
        """ Bind(self: NativeActivityMetadata, binding: Argument, argument: RuntimeArgument) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: NativeActivityMetadata, obj: object) -> bool """
        ...

    def GetArgumentsWithReflection(self) -> Collection:
        """ GetArgumentsWithReflection(self: NativeActivityMetadata) -> Collection[RuntimeArgument] """
        ...

    def GetChildrenWithReflection(self) -> Collection:
        """ GetChildrenWithReflection(self: NativeActivityMetadata) -> Collection[Activity] """
        ...

    def GetDelegatesWithReflection(self) -> Collection:
        """ GetDelegatesWithReflection(self: NativeActivityMetadata) -> Collection[ActivityDelegate] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: NativeActivityMetadata) -> int """
        ...

    def GetVariablesWithReflection(self) -> Collection:
        """ GetVariablesWithReflection(self: NativeActivityMetadata) -> Collection[Variable] """
        ...

    def RequireExtension(self, extensionType:Type = ...): # -> 
        """ RequireExtension[T](self: NativeActivityMetadata)RequireExtension(self: NativeActivityMetadata, extensionType: Type) """
        ...

    def SetArgumentsCollection(self, arguments:Collection): # -> 
        """ SetArgumentsCollection(self: NativeActivityMetadata, arguments: Collection[RuntimeArgument]) """
        ...

    def SetChildrenCollection(self, children:Collection): # -> 
        """ SetChildrenCollection(self: NativeActivityMetadata, children: Collection[Activity]) """
        ...

    def SetDelegatesCollection(self, delegates:Collection): # -> 
        """ SetDelegatesCollection(self: NativeActivityMetadata, delegates: Collection[ActivityDelegate]) """
        ...

    def SetImplementationChildrenCollection(self, implementationChildren:Collection): # -> 
        """ SetImplementationChildrenCollection(self: NativeActivityMetadata, implementationChildren: Collection[Activity]) """
        ...

    def SetImplementationDelegatesCollection(self, implementationDelegates:Collection): # -> 
        """ SetImplementationDelegatesCollection(self: NativeActivityMetadata, implementationDelegates: Collection[ActivityDelegate]) """
        ...

    def SetImplementationVariablesCollection(self, implementationVariables:Collection): # -> 
        """ SetImplementationVariablesCollection(self: NativeActivityMetadata, implementationVariables: Collection[Variable]) """
        ...

    def SetImportedChildrenCollection(self, importedChildren:Collection): # -> 
        """ SetImportedChildrenCollection(self: NativeActivityMetadata, importedChildren: Collection[Activity]) """
        ...

    def SetImportedDelegatesCollection(self, importedDelegates:Collection): # -> 
        """ SetImportedDelegatesCollection(self: NativeActivityMetadata, importedDelegates: Collection[ActivityDelegate]) """
        ...

    def SetValidationErrorsCollection(self, validationErrors:Collection): # -> 
        """ SetValidationErrorsCollection(self: NativeActivityMetadata, validationErrors: Collection[ValidationError]) """
        ...

    def SetVariablesCollection(self, variables:Collection): # -> 
        """ SetVariablesCollection(self: NativeActivityMetadata, variables: Collection[Variable]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NativeActivityTransactionContext(NativeActivityContext): # skipped bases: <type 'object'>
    """ no doc """
    def SetRuntimeTransaction(self, transaction:Transaction): # -> 
        """ SetRuntimeTransaction(self: NativeActivityTransactionContext, transaction: Transaction) """
        ...


class NoPersistHandle(Handle): # skipped bases: <type 'object'>
    """ NoPersistHandle() """
    def Enter(self, context:NativeActivityContext): # -> 
        """ Enter(self: NoPersistHandle, context: NativeActivityContext) """
        ...

    def Exit(self, context:NativeActivityContext): # -> 
        """ Exit(self: NoPersistHandle, context: NativeActivityContext) """
        ...


class OutArgument: # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateReference(argumentToReference:OutArgument, referencedArgumentName:str) -> OutArgument:
        """
        CreateReference(argumentToReference: OutArgument, referencedArgumentName: str) -> OutArgument
        CreateReference(argumentToReference: InOutArgument, referencedArgumentName: str) -> OutArgument
        """
        ...


class OverloadGroupAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    OverloadGroupAttribute()
    OverloadGroupAttribute(groupName: str)
    """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: OverloadGroupAttribute) -> str
        Set: GroupName(self: OverloadGroupAttribute) = value
        """
        ...


    def __new__(cls, groupName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, groupName: str)
        """
        ...


class PersistableIdleAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PersistableIdleAction, values: None (0), Persist (2), Unload (1) """
    Persist: PersistableIdleAction = ...
    Unload: PersistableIdleAction = ...
    value__ = ...


class RegistrationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def FindProperty(self, name:str) -> object:
        """ FindProperty(self: RegistrationContext, name: str) -> object """
        ...


class RequiredArgumentAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RequiredArgumentAttribute() """
    pass

class RuntimeArgument(LocationReference): # skipped bases: <type 'object'>
    """
    RuntimeArgument(name: str, argumentType: Type, direction: ArgumentDirection)
    RuntimeArgument(name: str, argumentType: Type, direction: ArgumentDirection, overloadGroupNames: List[str])
    RuntimeArgument(name: str, argumentType: Type, direction: ArgumentDirection, isRequired: bool)
    RuntimeArgument(name: str, argumentType: Type, direction: ArgumentDirection, isRequired: bool, overloadGroupNames: List[str])
    """
    @property
    def Direction(self) -> ArgumentDirection:
        """ Get: Direction(self: RuntimeArgument) -> ArgumentDirection """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: RuntimeArgument) -> bool """
        ...

    @property
    def OverloadGroupNames(self) -> ReadOnlyCollection:
        """ Get: OverloadGroupNames(self: RuntimeArgument) -> ReadOnlyCollection[str] """
        ...


    def Get(self, context:ActivityContext) -> object:
        """
        Get(self: RuntimeArgument, context: ActivityContext) -> object
        Get[T](self: RuntimeArgument, context: ActivityContext) -> T
        """
        ...

    def Set(self, context:ActivityContext, value:object): # -> 
        """ Set(self: RuntimeArgument, context: ActivityContext, value: object) """
        ...

    def __new__(cls, name:str, argumentType:Type, direction:ArgumentDirection, *__args:List) -> Self:
        """
        __new__(cls: type, name: str, argumentType: Type, direction: ArgumentDirection)
        __new__(cls: type, name: str, argumentType: Type, direction: ArgumentDirection, overloadGroupNames: List[str])
        __new__(cls: type, name: str, argumentType: Type, direction: ArgumentDirection, isRequired: bool)
        __new__(cls: type, name: str, argumentType: Type, direction: ArgumentDirection, isRequired: bool, overloadGroupNames: List[str])
        """
        ...


class RuntimeDelegateArgument: # skipped bases: <type 'object'>, <type 'object'>
    """ RuntimeDelegateArgument(name: str, type: Type, direction: ArgumentDirection, boundArgument: DelegateArgument) """
    @property
    def BoundArgument(self) -> DelegateArgument:
        """ Get: BoundArgument(self: RuntimeDelegateArgument) -> DelegateArgument """
        ...

    @property
    def Direction(self) -> ArgumentDirection:
        """ Get: Direction(self: RuntimeDelegateArgument) -> ArgumentDirection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RuntimeDelegateArgument) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: RuntimeDelegateArgument) -> Type """
        ...



class RuntimeTransactionHandle(Handle, IExecutionProperty, IPropertyRegistrationCallback): # skipped bases: <type 'object'>
    """
    RuntimeTransactionHandle()
    RuntimeTransactionHandle(rootTransaction: Transaction)
    """
    @property
    def AbortInstanceOnTransactionFailure(self) -> bool:
        """
        Get: AbortInstanceOnTransactionFailure(self: RuntimeTransactionHandle) -> bool
        Set: AbortInstanceOnTransactionFailure(self: RuntimeTransactionHandle) = value
        """
        ...

    @property
    def SuppressTransaction(self) -> bool:
        """
        Get: SuppressTransaction(self: RuntimeTransactionHandle) -> bool
        Set: SuppressTransaction(self: RuntimeTransactionHandle) = value
        """
        ...


    def CompleteTransaction(self, context:NativeActivityContext, callback:BookmarkCallback = ...): # -> 
        """ CompleteTransaction(self: RuntimeTransactionHandle, context: NativeActivityContext)CompleteTransaction(self: RuntimeTransactionHandle, context: NativeActivityContext, callback: BookmarkCallback) """
        ...

    def GetCurrentTransaction(self, context:NativeActivityContext) -> Transaction:
        """
        GetCurrentTransaction(self: RuntimeTransactionHandle, context: NativeActivityContext) -> Transaction
        GetCurrentTransaction(self: RuntimeTransactionHandle, context: CodeActivityContext) -> Transaction
        GetCurrentTransaction(self: RuntimeTransactionHandle, context: AsyncCodeActivityContext) -> Transaction
        """
        ...

    def RequestTransactionContext(self, context:NativeActivityContext, callback:Action, state:object): # -> 
        """ RequestTransactionContext(self: RuntimeTransactionHandle, context: NativeActivityContext, callback: Action[NativeActivityTransactionContext, object], state: object) """
        ...

    def RequireTransactionContext(self, context:NativeActivityContext, callback:Action, state:object): # -> 
        """ RequireTransactionContext(self: RuntimeTransactionHandle, context: NativeActivityContext, callback: Action[NativeActivityTransactionContext, object], state: object) """
        ...

    def __new__(cls, rootTransaction:Transaction = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, rootTransaction: Transaction)
        """
        ...


class UnhandledExceptionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnhandledExceptionAction, values: Abort (0), Cancel (1), Terminate (2) """
    Abort: UnhandledExceptionAction = ...
    Cancel: UnhandledExceptionAction = ...
    Terminate: UnhandledExceptionAction = ...
    value__ = ...


class ValidationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ValidationException()
    ValidationException(message: str)
    ValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Variable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Default(self) -> ActivityWithResult:
        """
        Get: Default(self: Variable) -> ActivityWithResult
        Set: Default(self: Variable) = value
        """
        ...

    @property
    def Modifiers(self) -> VariableModifiers:
        """
        Get: Modifiers(self: Variable) -> VariableModifiers
        Set: Modifiers(self: Variable) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Variable) -> str
        Set: Name(self: Variable) = value
        """
        ...

    @property
    def NameCore(self):
        ...

    @property
    def TypeCore(self):
        ...


    @staticmethod
    def Create(name:str, type:Type, modifiers:VariableModifiers) -> Variable:
        """ Create(name: str, type: Type, modifiers: VariableModifiers) -> Variable """
        ...

    def Get(self, context:ActivityContext) -> object:
        """ Get(self: Variable, context: ActivityContext) -> object """
        ...

    def GetLocation(self, context:ActivityContext) -> Location:
        """ GetLocation(self: Variable, context: ActivityContext) -> Location """
        ...

    def Set(self, context:ActivityContext, value:object): # -> 
        """ Set(self: Variable, context: ActivityContext, value: object) """
        ...


class VariableModifiers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) VariableModifiers, values: Mapped (2), None (0), ReadOnly (1) """
    Mapped: VariableModifiers = ...
    ReadOnly: VariableModifiers = ...
    value__ = ...


class VersionMismatchException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    VersionMismatchException()
    VersionMismatchException(message: str)
    VersionMismatchException(message: str, innerException: Exception)
    VersionMismatchException(expectedVersion: WorkflowIdentity, actualVersion: WorkflowIdentity)
    VersionMismatchException(message: str, expectedVersion: WorkflowIdentity, actualVersion: WorkflowIdentity)
    VersionMismatchException(message: str, expectedVersion: WorkflowIdentity, actualVersion: WorkflowIdentity, innerException: Exception)
    """
    @property
    def ActualVersion(self) -> WorkflowIdentity:
        """ Get: ActualVersion(self: VersionMismatchException) -> WorkflowIdentity """
        ...

    @property
    def ExpectedVersion(self) -> WorkflowIdentity:
        """ Get: ExpectedVersion(self: VersionMismatchException) -> WorkflowIdentity """
        ...


    SerializeObjectState = ...


class WorkflowApplication(WorkflowInstance): # skipped bases: <type 'object'>
    """
    WorkflowApplication(workflowDefinition: Activity)
    WorkflowApplication(workflowDefinition: Activity, inputs: IDictionary[str, object])
    WorkflowApplication(workflowDefinition: Activity, definitionIdentity: WorkflowIdentity)
    WorkflowApplication(workflowDefinition: Activity, inputs: IDictionary[str, object], definitionIdentity: WorkflowIdentity)
    """
    @property
    def Aborted(self) -> Action:
        """
        Get: Aborted(self: WorkflowApplication) -> Action[WorkflowApplicationAbortedEventArgs]
        Set: Aborted(self: WorkflowApplication) = value
        """
        ...

    @property
    def Completed(self) -> Action:
        """
        Get: Completed(self: WorkflowApplication) -> Action[WorkflowApplicationCompletedEventArgs]
        Set: Completed(self: WorkflowApplication) = value
        """
        ...

    @property
    def Extensions(self) -> WorkflowInstanceExtensionManager:
        """ Get: Extensions(self: WorkflowApplication) -> WorkflowInstanceExtensionManager """
        ...

    @property
    def Idle(self) -> Action:
        """
        Get: Idle(self: WorkflowApplication) -> Action[WorkflowApplicationIdleEventArgs]
        Set: Idle(self: WorkflowApplication) = value
        """
        ...

    @property
    def InstanceStore(self) -> InstanceStore:
        """
        Get: InstanceStore(self: WorkflowApplication) -> InstanceStore
        Set: InstanceStore(self: WorkflowApplication) = value
        """
        ...

    @property
    def OnUnhandledException(self): # -> Func
        """
        Get: OnUnhandledException(self: WorkflowApplication) -> Func[WorkflowApplicationUnhandledExceptionEventArgs, UnhandledExceptionAction]
        Set: OnUnhandledException(self: WorkflowApplication) = value
        """
        ...

    @property
    def PersistableIdle(self): # -> Func
        """
        Get: PersistableIdle(self: WorkflowApplication) -> Func[WorkflowApplicationIdleEventArgs, PersistableIdleAction]
        Set: PersistableIdle(self: WorkflowApplication) = value
        """
        ...

    @property
    def Unloaded(self) -> Action:
        """
        Get: Unloaded(self: WorkflowApplication) -> Action[WorkflowApplicationEventArgs]
        Set: Unloaded(self: WorkflowApplication) = value
        """
        ...


    def Abort(self, reason:str = ...): # -> 
        """ Abort(self: WorkflowApplication)Abort(self: WorkflowApplication, reason: str) """
        ...

    def AddInitialInstanceValues(self, writeOnlyValues:IDictionary): # -> 
        """ AddInitialInstanceValues(self: WorkflowApplication, writeOnlyValues: IDictionary[XName, object]) """
        ...

    def BeginCancel(self, *__args) -> IAsyncResult:
        """
        BeginCancel(self: WorkflowApplication, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginCancel(self: WorkflowApplication, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def BeginCreateDefaultInstanceOwner(instanceStore, definitionIdentity, identityFilter, *__args) -> IAsyncResult:
        """
        BeginCreateDefaultInstanceOwner(instanceStore: InstanceStore, definitionIdentity: WorkflowIdentity, identityFilter: WorkflowIdentityFilter, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginCreateDefaultInstanceOwner(instanceStore: InstanceStore, definitionIdentity: WorkflowIdentity, identityFilter: WorkflowIdentityFilter, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def BeginDeleteDefaultInstanceOwner(instanceStore, *__args) -> IAsyncResult:
        """
        BeginDeleteDefaultInstanceOwner(instanceStore: InstanceStore, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginDeleteDefaultInstanceOwner(instanceStore: InstanceStore, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def BeginGetInstance(instanceId, instanceStore, *__args) -> IAsyncResult:
        """
        BeginGetInstance(instanceId: Guid, instanceStore: InstanceStore, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginGetInstance(instanceId: Guid, instanceStore: InstanceStore, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def BeginGetRunnableInstance(instanceStore, *__args) -> IAsyncResult:
        """
        BeginGetRunnableInstance(instanceStore: InstanceStore, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginGetRunnableInstance(instanceStore: InstanceStore, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginLoad(self, *__args) -> IAsyncResult:
        """
        BeginLoad(self: WorkflowApplication, instanceId: Guid, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoad(self: WorkflowApplication, instance: WorkflowApplicationInstance, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoad(self: WorkflowApplication, instance: WorkflowApplicationInstance, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoad(self: WorkflowApplication, instance: WorkflowApplicationInstance, updateMap: DynamicUpdateMap, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoad(self: WorkflowApplication, instanceId: Guid, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoad(self: WorkflowApplication, instance: WorkflowApplicationInstance, updateMap: DynamicUpdateMap, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginLoadRunnableInstance(self, *__args) -> IAsyncResult:
        """
        BeginLoadRunnableInstance(self: WorkflowApplication, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginLoadRunnableInstance(self: WorkflowApplication, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginPersist(self, *__args) -> IAsyncResult:
        """
        BeginPersist(self: WorkflowApplication, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginPersist(self: WorkflowApplication, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginResumeBookmark(self, *__args) -> IAsyncResult:
        """
        BeginResumeBookmark(self: WorkflowApplication, bookmark: Bookmark, value: object, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginResumeBookmark(self: WorkflowApplication, bookmarkName: str, value: object, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginResumeBookmark(self: WorkflowApplication, bookmarkName: str, value: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginResumeBookmark(self: WorkflowApplication, bookmark: Bookmark, value: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginRun(self, *__args) -> IAsyncResult:
        """
        BeginRun(self: WorkflowApplication, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginRun(self: WorkflowApplication, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginTerminate(self, reason, *__args) -> IAsyncResult:
        """
        BeginTerminate(self: WorkflowApplication, reason: str, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginTerminate(self: WorkflowApplication, reason: Exception, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginTerminate(self: WorkflowApplication, reason: str, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginTerminate(self: WorkflowApplication, reason: Exception, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginUnload(self, *__args) -> IAsyncResult:
        """
        BeginUnload(self: WorkflowApplication, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginUnload(self: WorkflowApplication, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Cancel(self, timeout:TimeSpan = ...): # -> 
        """ Cancel(self: WorkflowApplication)Cancel(self: WorkflowApplication, timeout: TimeSpan) """
        ...

    @staticmethod
    def CreateDefaultInstanceOwner(instanceStore:InstanceStore, definitionIdentity:WorkflowIdentity, identityFilter:WorkflowIdentityFilter, timeout:TimeSpan = ...): # -> 
        """ CreateDefaultInstanceOwner(instanceStore: InstanceStore, definitionIdentity: WorkflowIdentity, identityFilter: WorkflowIdentityFilter)CreateDefaultInstanceOwner(instanceStore: InstanceStore, definitionIdentity: WorkflowIdentity, identityFilter: WorkflowIdentityFilter, timeout: TimeSpan) """
        ...

    @staticmethod
    def DeleteDefaultInstanceOwner(instanceStore:InstanceStore, timeout:TimeSpan = ...): # -> 
        """ DeleteDefaultInstanceOwner(instanceStore: InstanceStore)DeleteDefaultInstanceOwner(instanceStore: InstanceStore, timeout: TimeSpan) """
        ...

    def EndCancel(self, result:IAsyncResult): # -> 
        """ EndCancel(self: WorkflowApplication, result: IAsyncResult) """
        ...

    @staticmethod
    def EndCreateDefaultInstanceOwner(asyncResult:IAsyncResult): # -> 
        """ EndCreateDefaultInstanceOwner(asyncResult: IAsyncResult) """
        ...

    @staticmethod
    def EndDeleteDefaultInstanceOwner(asyncResult:IAsyncResult): # -> 
        """ EndDeleteDefaultInstanceOwner(asyncResult: IAsyncResult) """
        ...

    @staticmethod
    def EndGetInstance(asyncResult:IAsyncResult) -> WorkflowApplicationInstance:
        """ EndGetInstance(asyncResult: IAsyncResult) -> WorkflowApplicationInstance """
        ...

    @staticmethod
    def EndGetRunnableInstance(asyncResult:IAsyncResult) -> WorkflowApplicationInstance:
        """ EndGetRunnableInstance(asyncResult: IAsyncResult) -> WorkflowApplicationInstance """
        ...

    def EndLoad(self, result:IAsyncResult): # -> 
        """ EndLoad(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def EndLoadRunnableInstance(self, result:IAsyncResult): # -> 
        """ EndLoadRunnableInstance(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def EndPersist(self, result:IAsyncResult): # -> 
        """ EndPersist(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def EndResumeBookmark(self, result:IAsyncResult) -> BookmarkResumptionResult:
        """ EndResumeBookmark(self: WorkflowApplication, result: IAsyncResult) -> BookmarkResumptionResult """
        ...

    def EndRun(self, result:IAsyncResult): # -> 
        """ EndRun(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def EndTerminate(self, result:IAsyncResult): # -> 
        """ EndTerminate(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def EndUnload(self, result:IAsyncResult): # -> 
        """ EndUnload(self: WorkflowApplication, result: IAsyncResult) """
        ...

    def GetBookmarks(self, timeout:TimeSpan = ...) -> ReadOnlyCollection:
        """
        GetBookmarks(self: WorkflowApplication) -> ReadOnlyCollection[BookmarkInfo]
        GetBookmarks(self: WorkflowApplication, timeout: TimeSpan) -> ReadOnlyCollection[BookmarkInfo]
        """
        ...

    @staticmethod
    def GetInstance(instanceId:Guid, instanceStore:InstanceStore, timeout:TimeSpan = ...) -> WorkflowApplicationInstance:
        """
        GetInstance(instanceId: Guid, instanceStore: InstanceStore) -> WorkflowApplicationInstance
        GetInstance(instanceId: Guid, instanceStore: InstanceStore, timeout: TimeSpan) -> WorkflowApplicationInstance
        """
        ...

    @staticmethod
    def GetRunnableInstance(instanceStore:InstanceStore, timeout:TimeSpan = ...) -> WorkflowApplicationInstance:
        """
        GetRunnableInstance(instanceStore: InstanceStore) -> WorkflowApplicationInstance
        GetRunnableInstance(instanceStore: InstanceStore, timeout: TimeSpan) -> WorkflowApplicationInstance
        """
        ...

    def Load(self, *__args:WorkflowApplicationInstance): # -> 
        """ Load(self: WorkflowApplication, instance: WorkflowApplicationInstance)Load(self: WorkflowApplication, instance: WorkflowApplicationInstance, timeout: TimeSpan)Load(self: WorkflowApplication, instance: WorkflowApplicationInstance, updateMap: DynamicUpdateMap)Load(self: WorkflowApplication, instanceId: Guid)Load(self: WorkflowApplication, instance: WorkflowApplicationInstance, updateMap: DynamicUpdateMap, timeout: TimeSpan)Load(self: WorkflowApplication, instanceId: Guid, timeout: TimeSpan) """
        ...

    def LoadRunnableInstance(self, timeout:TimeSpan = ...): # -> 
        """ LoadRunnableInstance(self: WorkflowApplication)LoadRunnableInstance(self: WorkflowApplication, timeout: TimeSpan) """
        ...

    def Persist(self, timeout:TimeSpan = ...): # -> 
        """ Persist(self: WorkflowApplication)Persist(self: WorkflowApplication, timeout: TimeSpan) """
        ...

    def ResumeBookmark(self, *__args) -> BookmarkResumptionResult:
        """
        ResumeBookmark(self: WorkflowApplication, bookmark: Bookmark, value: object) -> BookmarkResumptionResult
        ResumeBookmark(self: WorkflowApplication, bookmarkName: str, value: object, timeout: TimeSpan) -> BookmarkResumptionResult
        ResumeBookmark(self: WorkflowApplication, bookmarkName: str, value: object) -> BookmarkResumptionResult
        ResumeBookmark(self: WorkflowApplication, bookmark: Bookmark, value: object, timeout: TimeSpan) -> BookmarkResumptionResult
        """
        ...

    def Run(self, timeout:TimeSpan = ...): # -> 
        """ Run(self: WorkflowApplication, timeout: TimeSpan)Run(self: WorkflowApplication) """
        ...

    def Terminate(self, reason:str, timeout:TimeSpan = ...): # -> 
        """ Terminate(self: WorkflowApplication, reason: str)Terminate(self: WorkflowApplication, reason: Exception)Terminate(self: WorkflowApplication, reason: str, timeout: TimeSpan)Terminate(self: WorkflowApplication, reason: Exception, timeout: TimeSpan) """
        ...

    def Unload(self, timeout:TimeSpan = ...): # -> 
        """ Unload(self: WorkflowApplication)Unload(self: WorkflowApplication, timeout: TimeSpan) """
        ...


class WorkflowApplicationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: WorkflowApplicationEventArgs) -> Guid """
        ...


    def GetInstanceExtensions(self) -> IEnumerable:
        """ GetInstanceExtensions[T](self: WorkflowApplicationEventArgs) -> IEnumerable[T] """
        ...


class WorkflowApplicationAbortedEventArgs(WorkflowApplicationEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> Exception:
        """ Get: Reason(self: WorkflowApplicationAbortedEventArgs) -> Exception """
        ...



class WorkflowApplicationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowApplicationException()
    WorkflowApplicationException(message: str)
    WorkflowApplicationException(message: str, instanceId: Guid)
    WorkflowApplicationException(message: str, innerException: Exception)
    WorkflowApplicationException(message: str, instanceId: Guid, innerException: Exception)
    """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: WorkflowApplicationException) -> Guid """
        ...


    SerializeObjectState = ...


class WorkflowApplicationAbortedException(WorkflowApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowApplicationAbortedException()
    WorkflowApplicationAbortedException(message: str)
    WorkflowApplicationAbortedException(message: str, instanceId: Guid)
    WorkflowApplicationAbortedException(message: str, innerException: Exception)
    WorkflowApplicationAbortedException(message: str, instanceId: Guid, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowApplicationCompletedEventArgs(WorkflowApplicationEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CompletionState(self) -> ActivityInstanceState:
        """ Get: CompletionState(self: WorkflowApplicationCompletedEventArgs) -> ActivityInstanceState """
        ...

    @property
    def Outputs(self) -> IDictionary:
        """ Get: Outputs(self: WorkflowApplicationCompletedEventArgs) -> IDictionary[str, object] """
        ...

    @property
    def TerminationException(self) -> Exception:
        """ Get: TerminationException(self: WorkflowApplicationCompletedEventArgs) -> Exception """
        ...



class WorkflowApplicationCompletedException(WorkflowApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowApplicationCompletedException()
    WorkflowApplicationCompletedException(message: str)
    WorkflowApplicationCompletedException(message: str, instanceId: Guid)
    WorkflowApplicationCompletedException(message: str, innerException: Exception)
    WorkflowApplicationCompletedException(message: str, instanceId: Guid, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowApplicationIdleEventArgs(WorkflowApplicationEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bookmarks(self) -> ReadOnlyCollection:
        """ Get: Bookmarks(self: WorkflowApplicationIdleEventArgs) -> ReadOnlyCollection[BookmarkInfo] """
        ...



class WorkflowApplicationInstance: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefinitionIdentity(self) -> WorkflowIdentity:
        """ Get: DefinitionIdentity(self: WorkflowApplicationInstance) -> WorkflowIdentity """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: WorkflowApplicationInstance) -> Guid """
        ...

    @property
    def InstanceStore(self) -> InstanceStore:
        """ Get: InstanceStore(self: WorkflowApplicationInstance) -> InstanceStore """
        ...


    def Abandon(self, timeout:TimeSpan = ...): # -> 
        """ Abandon(self: WorkflowApplicationInstance)Abandon(self: WorkflowApplicationInstance, timeout: TimeSpan) """
        ...

    def BeginAbandon(self, *__args) -> IAsyncResult:
        """
        BeginAbandon(self: WorkflowApplicationInstance, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAbandon(self: WorkflowApplicationInstance, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def CanApplyUpdate(self, updateMap, activitiesBlockingUpdate) -> Tuple_[bool, IList]:
        """ CanApplyUpdate(self: WorkflowApplicationInstance, updateMap: DynamicUpdateMap) -> (bool, IList[ActivityBlockingUpdate]) """
        ...

    def EndAbandon(self, asyncResult:IAsyncResult): # -> 
        """ EndAbandon(self: WorkflowApplicationInstance, asyncResult: IAsyncResult) """
        ...


class WorkflowApplicationTerminatedException(WorkflowApplicationCompletedException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowApplicationTerminatedException()
    WorkflowApplicationTerminatedException(message: str)
    WorkflowApplicationTerminatedException(message: str, instanceId: Guid)
    WorkflowApplicationTerminatedException(message: str, innerException: Exception)
    WorkflowApplicationTerminatedException(message: str, instanceId: Guid, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowApplicationUnhandledExceptionEventArgs(WorkflowApplicationEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExceptionSource(self) -> Activity:
        """ Get: ExceptionSource(self: WorkflowApplicationUnhandledExceptionEventArgs) -> Activity """
        ...

    @property
    def ExceptionSourceInstanceId(self) -> str:
        """ Get: ExceptionSourceInstanceId(self: WorkflowApplicationUnhandledExceptionEventArgs) -> str """
        ...

    @property
    def UnhandledException(self) -> Exception:
        """ Get: UnhandledException(self: WorkflowApplicationUnhandledExceptionEventArgs) -> Exception """
        ...



class WorkflowApplicationUnloadedException(WorkflowApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowApplicationUnloadedException()
    WorkflowApplicationUnloadedException(message: str)
    WorkflowApplicationUnloadedException(message: str, instanceId: Guid)
    WorkflowApplicationUnloadedException(message: str, innerException: Exception)
    WorkflowApplicationUnloadedException(message: str, instanceId: Guid, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowDataContext(CustomTypeDescriptor, IDisposable, INotifyPropertyChanged): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'object'>
    """ no doc """
    PropertyChanged = ...


class WorkflowIdentity(IEquatable): # skipped bases: <type 'object'>
    """
    WorkflowIdentity()
    WorkflowIdentity(name: str, version: Version, package: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowIdentity) -> str
        Set: Name(self: WorkflowIdentity) = value
        """
        ...

    @property
    def Package(self) -> str:
        """
        Get: Package(self: WorkflowIdentity) -> str
        Set: Package(self: WorkflowIdentity) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: WorkflowIdentity) -> Version
        Set: Version(self: WorkflowIdentity) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: WorkflowIdentity) -> int """
        ...

    @staticmethod
    def Parse(identity:str) -> WorkflowIdentity:
        """ Parse(identity: str) -> WorkflowIdentity """
        ...

    def ToString(self) -> str:
        """ ToString(self: WorkflowIdentity) -> str """
        ...

    @staticmethod
    def TryParse(identity, result) -> Tuple_[bool, WorkflowIdentity]:
        """ TryParse(identity: str) -> (bool, WorkflowIdentity) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkflowIdentityFilter(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowIdentityFilter, values: Any (1), AnyRevision (2), Exact (0) """
    Any: WorkflowIdentityFilter = ...
    AnyRevision: WorkflowIdentityFilter = ...
    Exact: WorkflowIdentityFilter = ...
    value__ = ...


class WorkflowInspectionServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CacheMetadata(rootActivity:Activity, hostEnvironment:LocationReferenceEnvironment = ...): # -> 
        """ CacheMetadata(rootActivity: Activity)CacheMetadata(rootActivity: Activity, hostEnvironment: LocationReferenceEnvironment) """
        ...

    @staticmethod
    def CanInduceIdle(activity:Activity) -> bool:
        """ CanInduceIdle(activity: Activity) -> bool """
        ...

    @staticmethod
    def GetActivities(activity:Activity) -> IEnumerable:
        """ GetActivities(activity: Activity) -> IEnumerable[Activity] """
        ...

    @staticmethod
    def GetImplementationVersion(activity:Activity) -> Version:
        """ GetImplementationVersion(activity: Activity) -> Version """
        ...

    @staticmethod
    def Resolve(root:Activity, id:str) -> Activity:
        """ Resolve(root: Activity, id: str) -> Activity """
        ...

    __all__: list = ...


class WorkflowInvoker: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowInvoker(workflow: Activity) """
    @property
    def Extensions(self) -> WorkflowInstanceExtensionManager:
        """ Get: Extensions(self: WorkflowInvoker) -> WorkflowInstanceExtensionManager """
        ...


    def BeginInvoke(self, *__args) -> IAsyncResult:
        """
        BeginInvoke(self: WorkflowInvoker, inputs: IDictionary[str, object], callback: AsyncCallback, state: object) -> IAsyncResult
        BeginInvoke(self: WorkflowInvoker, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginInvoke(self: WorkflowInvoker, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginInvoke(self: WorkflowInvoker, inputs: IDictionary[str, object], timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def CancelAsync(self, userState:object): # -> 
        """ CancelAsync(self: WorkflowInvoker, userState: object) """
        ...

    def EndInvoke(self, result:IAsyncResult) -> IDictionary:
        """ EndInvoke(self: WorkflowInvoker, result: IAsyncResult) -> IDictionary[str, object] """
        ...

    @staticmethod
    def Invoke(*__args:Activity) -> IDictionary:
        """
        Invoke(workflow: Activity) -> IDictionary[str, object]
        Invoke(workflow: Activity, timeout: TimeSpan) -> IDictionary[str, object]
        Invoke(workflow: Activity, inputs: IDictionary[str, object]) -> IDictionary[str, object]
        Invoke(workflow: Activity, inputs: IDictionary[str, object], timeout: TimeSpan) -> IDictionary[str, object]
        Invoke(self: WorkflowInvoker) -> IDictionary[str, object]
        Invoke(self: WorkflowInvoker, inputs: IDictionary[str, object]) -> IDictionary[str, object]
        Invoke[TResult](workflow: Activity[TResult]) -> TResult
        Invoke[TResult](workflow: Activity[TResult], inputs: IDictionary[str, object]) -> TResult
        Invoke[TResult](workflow: Activity[TResult], inputs: IDictionary[str, object], timeout: TimeSpan) -> TResult
        Invoke[TResult](workflow: Activity[TResult], inputs: IDictionary[str, object], timeout: TimeSpan) -> (TResult, IDictionary[str, object])
        Invoke(self: WorkflowInvoker, timeout: TimeSpan) -> IDictionary[str, object]
        Invoke(self: WorkflowInvoker, inputs: IDictionary[str, object], timeout: TimeSpan) -> IDictionary[str, object]
        """
        ...

    def InvokeAsync(self, *__args:IDictionary): # -> 
        """ InvokeAsync(self: WorkflowInvoker, inputs: IDictionary[str, object])InvokeAsync(self: WorkflowInvoker, inputs: IDictionary[str, object], timeout: TimeSpan)InvokeAsync(self: WorkflowInvoker, inputs: IDictionary[str, object], userState: object)InvokeAsync(self: WorkflowInvoker)InvokeAsync(self: WorkflowInvoker, timeout: TimeSpan)InvokeAsync(self: WorkflowInvoker, userState: object)InvokeAsync(self: WorkflowInvoker, timeout: TimeSpan, userState: object)InvokeAsync(self: WorkflowInvoker, inputs: IDictionary[str, object], timeout: TimeSpan, userState: object) """
        ...

    InvokeCompleted = ...


# variables with complex values

