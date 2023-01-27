# encoding: utf-8
# module System.ComponentModel.Design.Serialization calls itself Serialization
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Attribute, Enum, EventArgs, IAsyncResult, 
    IDisposable, IServiceProvider, MulticastDelegate, SystemException, Type)

from System.CodeDom import (CodeCompileUnit, CodeExpression, CodeLinePragma, 
    CodeStatement, CodeStatementCollection, CodeTypeDeclaration)

from System.Collections import ICollection, IEnumerable, IList

from System.ComponentModel import (IContainer, MemberDescriptor, 
    PropertyDescriptorCollection)

from System.ComponentModel.Design import IDesignerHost

from System.IO import Stream

from System.Reflection import MemberInfo

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DesignerLoader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Loading(self) -> bool:
        """ Get: Loading(self: DesignerLoader) -> bool """
        ...


    def BeginLoad(self, host:IDesignerLoaderHost): # -> 
        """ BeginLoad(self: DesignerLoader, host: IDesignerLoaderHost) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: DesignerLoader) """
        ...

    def Flush(self): # -> 
        """ Flush(self: DesignerLoader) """
        ...


class IDesignerLoaderService: # skipped bases: <type 'object'>
    """ no doc """
    def AddLoadDependency(self): # -> 
        """ AddLoadDependency(self: IDesignerLoaderService) """
        ...

    def DependentLoadComplete(self, successful:bool, errorCollection:ICollection): # -> 
        """ DependentLoadComplete(self: IDesignerLoaderService, successful: bool, errorCollection: ICollection) """
        ...

    def Reload(self) -> bool:
        """ Reload(self: IDesignerLoaderService) -> bool """
        ...


class BasicDesignerLoader(DesignerLoader, IDesignerLoaderService): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LoaderHost(self):
        ...

    @property
    def Modified(self):
        ...

    @property
    def PropertyProvider(self):
        ...

    @property
    def ReloadPending(self):
        ...


    def EnableComponentNotification(self, *args): #cannot find CLR method
        """ EnableComponentNotification(self: BasicDesignerLoader, enable: bool) -> bool """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: BasicDesignerLoader, serviceType: Type) -> object """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: BasicDesignerLoader) """
        ...

    def IsReloadNeeded(self, *args): #cannot find CLR method
        """ IsReloadNeeded(self: BasicDesignerLoader) -> bool """
        ...

    def OnBeginLoad(self, *args): #cannot find CLR method
        """ OnBeginLoad(self: BasicDesignerLoader) """
        ...

    def OnBeginUnload(self, *args): #cannot find CLR method
        """ OnBeginUnload(self: BasicDesignerLoader) """
        ...

    def OnEndLoad(self, *args): #cannot find CLR method
        """ OnEndLoad(self: BasicDesignerLoader, successful: bool, errors: ICollection) """
        ...

    def OnModifying(self, *args): #cannot find CLR method
        """ OnModifying(self: BasicDesignerLoader) """
        ...

    def PerformFlush(self, *args): #cannot find CLR method
        """ PerformFlush(self: BasicDesignerLoader, serializationManager: IDesignerSerializationManager) """
        ...

    def PerformLoad(self, *args): #cannot find CLR method
        """ PerformLoad(self: BasicDesignerLoader, serializationManager: IDesignerSerializationManager) """
        ...

    def ReloadOptions(self, *args): #cannot find CLR method
        """ enum (flags) ReloadOptions, values: Default (0), Force (2), ModifyOnError (1), NoFlush (4) """
        ...

    def ReportFlushErrors(self, *args): #cannot find CLR method
        """ ReportFlushErrors(self: BasicDesignerLoader, errors: ICollection) """
        ...

    def SetBaseComponentClassName(self, *args): #cannot find CLR method
        """ SetBaseComponentClassName(self: BasicDesignerLoader, name: str) """
        ...



class ComponentSerializationService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateStore(self) -> SerializationStore:
        """ CreateStore(self: ComponentSerializationService) -> SerializationStore """
        ...

    def Deserialize(self, store:SerializationStore, container:IContainer = ...) -> ICollection:
        """
        Deserialize(self: ComponentSerializationService, store: SerializationStore) -> ICollection
        Deserialize(self: ComponentSerializationService, store: SerializationStore, container: IContainer) -> ICollection
        """
        ...

    def DeserializeTo(self, store:SerializationStore, container:IContainer, validateRecycledTypes:bool = ..., applyDefaults:bool = ...): # -> 
        """ DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer)DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer, validateRecycledTypes: bool)DeserializeTo(self: ComponentSerializationService, store: SerializationStore, container: IContainer, validateRecycledTypes: bool, applyDefaults: bool) """
        ...

    def LoadStore(self, stream:Stream) -> SerializationStore:
        """ LoadStore(self: ComponentSerializationService, stream: Stream) -> SerializationStore """
        ...

    def Serialize(self, store:SerializationStore, value:object): # -> 
        """ Serialize(self: ComponentSerializationService, store: SerializationStore, value: object) """
        ...

    def SerializeAbsolute(self, store:SerializationStore, value:object): # -> 
        """ SerializeAbsolute(self: ComponentSerializationService, store: SerializationStore, value: object) """
        ...

    def SerializeMember(self, store:SerializationStore, owningObject:object, member:MemberDescriptor): # -> 
        """ SerializeMember(self: ComponentSerializationService, store: SerializationStore, owningObject: object, member: MemberDescriptor) """
        ...

    def SerializeMemberAbsolute(self, store:SerializationStore, owningObject:object, member:MemberDescriptor): # -> 
        """ SerializeMemberAbsolute(self: ComponentSerializationService, store: SerializationStore, owningObject: object, member: MemberDescriptor) """
        ...


class CodeDomComponentSerializationService(ComponentSerializationService): # skipped bases: <type 'object'>
    """
    CodeDomComponentSerializationService()
    CodeDomComponentSerializationService(provider: IServiceProvider)
    """
    def __new__(cls, provider:IServiceProvider = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, provider: IServiceProvider)
        """
        ...


class IDesignerSerializationService: # skipped bases: <type 'object'>
    """ no doc """
    def Deserialize(self, serializationData:object) -> ICollection:
        """ Deserialize(self: IDesignerSerializationService, serializationData: object) -> ICollection """
        ...

    def Serialize(self, objects:ICollection) -> object:
        """ Serialize(self: IDesignerSerializationService, objects: ICollection) -> object """
        ...


class INameCreationService: # skipped bases: <type 'object'>
    """ no doc """
    def CreateName(self, container:IContainer, dataType:Type) -> str:
        """ CreateName(self: INameCreationService, container: IContainer, dataType: Type) -> str """
        ...

    def IsValidName(self, name:str) -> bool:
        """ IsValidName(self: INameCreationService, name: str) -> bool """
        ...

    def ValidateName(self, name:str): # -> 
        """ ValidateName(self: INameCreationService, name: str) """
        ...


class CodeDomDesignerLoader(INameCreationService, IDesignerSerializationService, BasicDesignerLoader): # skipped bases: <type 'IDesignerLoaderService'>, <type 'object'>
    """ no doc """
    @property
    def CodeDomProvider(self):
        ...

    @property
    def TypeResolutionService(self):
        ...


    def OnComponentRename(self, *args): #cannot find CLR method
        """ OnComponentRename(self: CodeDomDesignerLoader, component: object, oldName: str, newName: str) """
        ...

    def Parse(self, *args): #cannot find CLR method
        """ Parse(self: CodeDomDesignerLoader) -> CodeCompileUnit """
        ...

    def Write(self, *args): #cannot find CLR method
        """ Write(self: CodeDomDesignerLoader, unit: CodeCompileUnit) """
        ...


class CodeDomLocalizationModel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeDomLocalizationModel, values: None (0), PropertyAssignment (1), PropertyReflection (2) """
    PropertyAssignment: CodeDomLocalizationModel = ...
    PropertyReflection: CodeDomLocalizationModel = ...
    value__ = ...


class IDesignerSerializationProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetSerializer(self, manager:IDesignerSerializationManager, currentSerializer:object, objectType:Type, serializerType:Type) -> object:
        """ GetSerializer(self: IDesignerSerializationProvider, manager: IDesignerSerializationManager, currentSerializer: object, objectType: Type, serializerType: Type) -> object """
        ...


class CodeDomLocalizationProvider(IDisposable, IDesignerSerializationProvider): # skipped bases: <type 'object'>
    """
    CodeDomLocalizationProvider(provider: IServiceProvider, model: CodeDomLocalizationModel)
    CodeDomLocalizationProvider(provider: IServiceProvider, model: CodeDomLocalizationModel, supportedCultures: Array[CultureInfo])
    """
    pass

class CodeDomSerializerBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DeserializeExpression(self, *args): #cannot find CLR method
        """ DeserializeExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, name: str, expression: CodeExpression) -> object """
        ...

    def DeserializeInstance(self, *args): #cannot find CLR method
        """ DeserializeInstance(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, type: Type, parameters: Array[object], name: str, addToContainer: bool) -> object """
        ...

    def DeserializePropertiesFromResources(self, *args): #cannot find CLR method
        """ DeserializePropertiesFromResources(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object, filter: Array[Attribute]) """
        ...

    def DeserializeStatement(self, *args): #cannot find CLR method
        """ DeserializeStatement(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statement: CodeStatement) """
        ...

    def GetAttributesFromTypeHelper(self, *args): #cannot find CLR method
        """ GetAttributesFromTypeHelper(manager: IDesignerSerializationManager, type: Type) -> AttributeCollection """
        ...

    def GetAttributesHelper(self, *args): #cannot find CLR method
        """ GetAttributesHelper(manager: IDesignerSerializationManager, instance: object) -> AttributeCollection """
        ...

    def GetEventsHelper(self, *args): #cannot find CLR method
        """ GetEventsHelper(manager: IDesignerSerializationManager, instance: object, attributes: Array[Attribute]) -> EventDescriptorCollection """
        ...

    def GetExpression(self, *args): #cannot find CLR method
        """ GetExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> CodeExpression """
        ...

    def GetPropertiesHelper(self, *args): #cannot find CLR method
        """ GetPropertiesHelper(manager: IDesignerSerializationManager, instance: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection """
        ...

    def GetReflectionTypeFromTypeHelper(self, *args): #cannot find CLR method
        """ GetReflectionTypeFromTypeHelper(manager: IDesignerSerializationManager, type: Type) -> Type """
        ...

    def GetReflectionTypeHelper(self, *args): #cannot find CLR method
        """ GetReflectionTypeHelper(manager: IDesignerSerializationManager, instance: object) -> Type """
        ...

    def GetSerializer(self, *args): #cannot find CLR method
        """
        GetSerializer(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> CodeDomSerializer
        GetSerializer(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, valueType: Type) -> CodeDomSerializer
        """
        ...

    def GetTargetFrameworkProvider(self, *args): #cannot find CLR method
        """ GetTargetFrameworkProvider(provider: IServiceProvider, instance: object) -> TypeDescriptionProvider """
        ...

    def GetUniqueName(self, *args): #cannot find CLR method
        """ GetUniqueName(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> str """
        ...

    def IsSerialized(self, *args): #cannot find CLR method
        """
        IsSerialized(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> bool
        IsSerialized(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object, honorPreset: bool) -> bool
        """
        ...

    def SerializeCreationExpression(self, *args): #cannot find CLR method
        """ SerializeCreationExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> (CodeExpression, bool) """
        ...

    def SerializeEvent(self, *args): #cannot find CLR method
        """ SerializeEvent(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statements: CodeStatementCollection, value: object, descriptor: EventDescriptor) """
        ...

    def SerializeEvents(self, *args): #cannot find CLR method
        """ SerializeEvents(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statements: CodeStatementCollection, value: object, *filter: Array[Attribute]) """
        ...

    def SerializeProperties(self, *args): #cannot find CLR method
        """ SerializeProperties(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statements: CodeStatementCollection, value: object, filter: Array[Attribute]) """
        ...

    def SerializePropertiesToResources(self, *args): #cannot find CLR method
        """ SerializePropertiesToResources(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statements: CodeStatementCollection, value: object, filter: Array[Attribute]) """
        ...

    def SerializeProperty(self, *args): #cannot find CLR method
        """ SerializeProperty(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, statements: CodeStatementCollection, value: object, propertyToSerialize: PropertyDescriptor) """
        ...

    def SerializeResource(self, *args): #cannot find CLR method
        """ SerializeResource(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, resourceName: str, value: object) """
        ...

    def SerializeResourceInvariant(self, *args): #cannot find CLR method
        """ SerializeResourceInvariant(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, resourceName: str, value: object) """
        ...

    def SerializeToExpression(self, *args): #cannot find CLR method
        """ SerializeToExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> CodeExpression """
        ...

    def SerializeToResourceExpression(self, *args): #cannot find CLR method
        """
        SerializeToResourceExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object) -> CodeExpression
        SerializeToResourceExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object, ensureInvariant: bool) -> CodeExpression
        """
        ...

    def SetExpression(self, *args): #cannot find CLR method
        """ SetExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object, expression: CodeExpression)SetExpression(self: CodeDomSerializerBase, manager: IDesignerSerializationManager, value: object, expression: CodeExpression, isPreset: bool) """
        ...


class CodeDomSerializer(CodeDomSerializerBase): # skipped bases: <type 'object'>
    """ CodeDomSerializer() """
    def Deserialize(self, manager:IDesignerSerializationManager, codeObject:object) -> object:
        """ Deserialize(self: CodeDomSerializer, manager: IDesignerSerializationManager, codeObject: object) -> object """
        ...

    def DeserializeStatementToInstance(self, *args): #cannot find CLR method
        """ DeserializeStatementToInstance(self: CodeDomSerializer, manager: IDesignerSerializationManager, statement: CodeStatement) -> object """
        ...

    def GetTargetComponentName(self, statement:CodeStatement, expression:CodeExpression, targetType:Type) -> str:
        """ GetTargetComponentName(self: CodeDomSerializer, statement: CodeStatement, expression: CodeExpression, targetType: Type) -> str """
        ...

    def Serialize(self, manager:IDesignerSerializationManager, value:object) -> object:
        """ Serialize(self: CodeDomSerializer, manager: IDesignerSerializationManager, value: object) -> object """
        ...

    def SerializeAbsolute(self, manager:IDesignerSerializationManager, value:object) -> object:
        """ SerializeAbsolute(self: CodeDomSerializer, manager: IDesignerSerializationManager, value: object) -> object """
        ...

    def SerializeMember(self, manager:IDesignerSerializationManager, owningObject:object, member:MemberDescriptor) -> CodeStatementCollection:
        """ SerializeMember(self: CodeDomSerializer, manager: IDesignerSerializationManager, owningObject: object, member: MemberDescriptor) -> CodeStatementCollection """
        ...

    def SerializeMemberAbsolute(self, manager:IDesignerSerializationManager, owningObject:object, member:MemberDescriptor) -> CodeStatementCollection:
        """ SerializeMemberAbsolute(self: CodeDomSerializer, manager: IDesignerSerializationManager, owningObject: object, member: MemberDescriptor) -> CodeStatementCollection """
        ...

    def SerializeToReferenceExpression(self, *args): #cannot find CLR method
        """ SerializeToReferenceExpression(self: CodeDomSerializer, manager: IDesignerSerializationManager, value: object) -> CodeExpression """
        ...


class CodeDomSerializerException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CodeDomSerializerException(message: str, linePragma: CodeLinePragma)
    CodeDomSerializerException(ex: Exception, linePragma: CodeLinePragma)
    CodeDomSerializerException(message: str, manager: IDesignerSerializationManager)
    CodeDomSerializerException(ex: Exception, manager: IDesignerSerializationManager)
    """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """ Get: LinePragma(self: CodeDomSerializerException) -> CodeLinePragma """
        ...


    SerializeObjectState = ...


class CollectionCodeDomSerializer(CodeDomSerializer): # skipped bases: <type 'object'>
    """ CollectionCodeDomSerializer() """
    def MethodSupportsSerialization(self, *args): #cannot find CLR method
        """ MethodSupportsSerialization(self: CollectionCodeDomSerializer, method: MethodInfo) -> bool """
        ...

    def SerializeCollection(self, *args): #cannot find CLR method
        """ SerializeCollection(self: CollectionCodeDomSerializer, manager: IDesignerSerializationManager, targetExpression: CodeExpression, targetType: Type, originalCollection: ICollection, valuesToSerialize: ICollection) -> object """
        ...


class ContextStack: # skipped bases: <type 'object'>, <type 'object'>
    """ ContextStack() """
    @property
    def Current(self) -> object:
        """ Get: Current(self: ContextStack) -> object """
        ...


    def Append(self, context:object): # -> 
        """ Append(self: ContextStack, context: object) """
        ...

    def Pop(self) -> object:
        """ Pop(self: ContextStack) -> object """
        ...

    def Push(self, context:object): # -> 
        """ Push(self: ContextStack, context: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class DefaultSerializationProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DefaultSerializationProviderAttribute(providerType: Type)
    DefaultSerializationProviderAttribute(providerTypeName: str)
    """
    @property
    def ProviderTypeName(self) -> str:
        """ Get: ProviderTypeName(self: DefaultSerializationProviderAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, providerType: Type)
        __new__(cls: type, providerTypeName: str)
        """
        ...


class IDesignerSerializationManager(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ContextStack:
        """ Get: Context(self: IDesignerSerializationManager) -> ContextStack """
        ...

    @property
    def Properties(self) -> PropertyDescriptorCollection:
        """ Get: Properties(self: IDesignerSerializationManager) -> PropertyDescriptorCollection """
        ...


    def AddSerializationProvider(self, provider:IDesignerSerializationProvider): # -> 
        """ AddSerializationProvider(self: IDesignerSerializationManager, provider: IDesignerSerializationProvider) """
        ...

    def CreateInstance(self, type:Type, arguments:ICollection, name:str, addToContainer:bool) -> object:
        """ CreateInstance(self: IDesignerSerializationManager, type: Type, arguments: ICollection, name: str, addToContainer: bool) -> object """
        ...

    def GetInstance(self, name:str) -> object:
        """ GetInstance(self: IDesignerSerializationManager, name: str) -> object """
        ...

    def GetName(self, value:object) -> str:
        """ GetName(self: IDesignerSerializationManager, value: object) -> str """
        ...

    def GetSerializer(self, objectType:Type, serializerType:Type) -> object:
        """ GetSerializer(self: IDesignerSerializationManager, objectType: Type, serializerType: Type) -> object """
        ...

    def GetType(self, typeName:str) -> Type:
        """ GetType(self: IDesignerSerializationManager, typeName: str) -> Type """
        ...

    def RemoveSerializationProvider(self, provider:IDesignerSerializationProvider): # -> 
        """ RemoveSerializationProvider(self: IDesignerSerializationManager, provider: IDesignerSerializationProvider) """
        ...

    def ReportError(self, errorInformation:object): # -> 
        """ ReportError(self: IDesignerSerializationManager, errorInformation: object) """
        ...

    def SetName(self, instance:object, name:str): # -> 
        """ SetName(self: IDesignerSerializationManager, instance: object, name: str) """
        ...

    ResolveName = ...
    SerializationComplete = ...


class DesignerSerializationManager(IDesignerSerializationManager): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """
    DesignerSerializationManager()
    DesignerSerializationManager(provider: IServiceProvider)
    """
    @property
    def Container(self) -> IContainer:
        """
        Get: Container(self: DesignerSerializationManager) -> IContainer
        Set: Container(self: DesignerSerializationManager) = value
        """
        ...

    @property
    def Errors(self) -> IList:
        """ Get: Errors(self: DesignerSerializationManager) -> IList """
        ...

    @property
    def PreserveNames(self) -> bool:
        """
        Get: PreserveNames(self: DesignerSerializationManager) -> bool
        Set: PreserveNames(self: DesignerSerializationManager) = value
        """
        ...

    @property
    def PropertyProvider(self) -> object:
        """
        Get: PropertyProvider(self: DesignerSerializationManager) -> object
        Set: PropertyProvider(self: DesignerSerializationManager) = value
        """
        ...

    @property
    def RecycleInstances(self) -> bool:
        """
        Get: RecycleInstances(self: DesignerSerializationManager) -> bool
        Set: RecycleInstances(self: DesignerSerializationManager) = value
        """
        ...

    @property
    def ValidateRecycledTypes(self) -> bool:
        """
        Get: ValidateRecycledTypes(self: DesignerSerializationManager) -> bool
        Set: ValidateRecycledTypes(self: DesignerSerializationManager) = value
        """
        ...


    def CreateSession(self) -> IDisposable:
        """ CreateSession(self: DesignerSerializationManager) -> IDisposable """
        ...

    def GetRuntimeType(self, typeName:str) -> Type:
        """ GetRuntimeType(self: DesignerSerializationManager, typeName: str) -> Type """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: DesignerSerializationManager, serviceType: Type) -> object """
        ...

    def OnResolveName(self, *args): #cannot find CLR method
        """ OnResolveName(self: DesignerSerializationManager, e: ResolveNameEventArgs) """
        ...

    def OnSessionCreated(self, *args): #cannot find CLR method
        """ OnSessionCreated(self: DesignerSerializationManager, e: EventArgs) """
        ...

    def OnSessionDisposed(self, *args): #cannot find CLR method
        """ OnSessionDisposed(self: DesignerSerializationManager, e: EventArgs) """
        ...

    SessionCreated = ...
    SessionDisposed = ...


class DesignerSerializerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignerSerializerAttribute(serializerType: Type, baseSerializerType: Type)
    DesignerSerializerAttribute(serializerTypeName: str, baseSerializerType: Type)
    DesignerSerializerAttribute(serializerTypeName: str, baseSerializerTypeName: str)
    """
    @property
    def SerializerBaseTypeName(self) -> str:
        """ Get: SerializerBaseTypeName(self: DesignerSerializerAttribute) -> str """
        ...

    @property
    def SerializerTypeName(self) -> str:
        """ Get: SerializerTypeName(self: DesignerSerializerAttribute) -> str """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, serializerType: Type, baseSerializerType: Type)
        __new__(cls: type, serializerTypeName: str, baseSerializerType: Type)
        __new__(cls: type, serializerTypeName: str, baseSerializerTypeName: str)
        """
        ...


class ExpressionContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    ExpressionContext(expression: CodeExpression, expressionType: Type, owner: object, presetValue: object)
    ExpressionContext(expression: CodeExpression, expressionType: Type, owner: object)
    """
    @property
    def Expression(self) -> CodeExpression:
        """ Get: Expression(self: ExpressionContext) -> CodeExpression """
        ...

    @property
    def ExpressionType(self) -> Type:
        """ Get: ExpressionType(self: ExpressionContext) -> Type """
        ...

    @property
    def Owner(self) -> object:
        """ Get: Owner(self: ExpressionContext) -> object """
        ...

    @property
    def PresetValue(self) -> object:
        """ Get: PresetValue(self: ExpressionContext) -> object """
        ...



class ICodeDomDesignerReload: # skipped bases: <type 'object'>
    """ no doc """
    def ShouldReloadDesigner(self, newTree:CodeCompileUnit) -> bool:
        """ ShouldReloadDesigner(self: ICodeDomDesignerReload, newTree: CodeCompileUnit) -> bool """
        ...


class IDesignerLoaderHost(IDesignerHost): # skipped bases: <type 'IServiceProvider'>, <type 'IServiceContainer'>, <type 'object'>
    """ no doc """
    def EndLoad(self, baseClassName:str, successful:bool, errorCollection:ICollection): # -> 
        """ EndLoad(self: IDesignerLoaderHost, baseClassName: str, successful: bool, errorCollection: ICollection) """
        ...

    def Reload(self): # -> 
        """ Reload(self: IDesignerLoaderHost) """
        ...


class IDesignerLoaderHost2(IDesignerLoaderHost): # skipped bases: <type 'IDesignerHost'>, <type 'IServiceProvider'>, <type 'IServiceContainer'>, <type 'object'>
    """ no doc """
    @property
    def CanReloadWithErrors(self) -> bool:
        """
        Get: CanReloadWithErrors(self: IDesignerLoaderHost2) -> bool
        Set: CanReloadWithErrors(self: IDesignerLoaderHost2) = value
        """
        ...

    @property
    def IgnoreErrorsDuringReload(self) -> bool:
        """
        Get: IgnoreErrorsDuringReload(self: IDesignerLoaderHost2) -> bool
        Set: IgnoreErrorsDuringReload(self: IDesignerLoaderHost2) = value
        """
        ...



class InstanceDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """
    InstanceDescriptor(member: MemberInfo, arguments: ICollection)
    InstanceDescriptor(member: MemberInfo, arguments: ICollection, isComplete: bool)
    """
    @property
    def Arguments(self) -> ICollection:
        """ Get: Arguments(self: InstanceDescriptor) -> ICollection """
        ...

    @property
    def IsComplete(self) -> bool:
        """ Get: IsComplete(self: InstanceDescriptor) -> bool """
        ...

    @property
    def MemberInfo(self) -> MemberInfo:
        """ Get: MemberInfo(self: InstanceDescriptor) -> MemberInfo """
        ...


    def Invoke(self) -> object:
        """ Invoke(self: InstanceDescriptor) -> object """
        ...


class MemberCodeDomSerializer(CodeDomSerializerBase): # skipped bases: <type 'object'>
    """ no doc """
    def Serialize(self, manager:IDesignerSerializationManager, value:object, descriptor:MemberDescriptor, statements:CodeStatementCollection): # -> 
        """ Serialize(self: MemberCodeDomSerializer, manager: IDesignerSerializationManager, value: object, descriptor: MemberDescriptor, statements: CodeStatementCollection) """
        ...

    def ShouldSerialize(self, manager:IDesignerSerializationManager, value:object, descriptor:MemberDescriptor) -> bool:
        """ ShouldSerialize(self: MemberCodeDomSerializer, manager: IDesignerSerializationManager, value: object, descriptor: MemberDescriptor) -> bool """
        ...


class MemberRelationship: # skipped bases: <type 'object'>, <type 'object'>
    """ MemberRelationship(owner: object, member: MemberDescriptor) """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: MemberRelationship) -> bool """
        ...

    @property
    def Member(self) -> MemberDescriptor:
        """ Get: Member(self: MemberRelationship) -> MemberDescriptor """
        ...

    @property
    def Owner(self) -> object:
        """ Get: Owner(self: MemberRelationship) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MemberRelationship, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MemberRelationship) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: MemberRelationship = ...


class MemberRelationshipService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetRelationship(self, *args): #cannot find CLR method
        """ GetRelationship(self: MemberRelationshipService, source: MemberRelationship) -> MemberRelationship """
        ...

    def SetRelationship(self, *args): #cannot find CLR method
        """ SetRelationship(self: MemberRelationshipService, source: MemberRelationship, relationship: MemberRelationship) """
        ...

    def SupportsRelationship(self, source:MemberRelationship, relationship:MemberRelationship) -> bool:
        """ SupportsRelationship(self: MemberRelationshipService, source: MemberRelationship, relationship: MemberRelationship) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ObjectStatementCollection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    def ContainsKey(self, statementOwner:object) -> bool:
        """ ContainsKey(self: ObjectStatementCollection, statementOwner: object) -> bool """
        ...

    def Populate(self, *__args:ICollection): # -> 
        """ Populate(self: ObjectStatementCollection, statementOwners: ICollection)Populate(self: ObjectStatementCollection, owner: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ResolveNameEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ResolveNameEventArgs(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ResolveNameEventArgs) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ResolveNameEventArgs) -> object
        Set: Value(self: ResolveNameEventArgs) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ResolveNameEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ResolveNameEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ResolveNameEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ResolveNameEventHandler, sender: object, e: ResolveNameEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ResolveNameEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ResolveNameEventArgs): # -> 
        """ Invoke(self: ResolveNameEventHandler, sender: object, e: ResolveNameEventArgs) """
        ...


class RootContext: # skipped bases: <type 'object'>, <type 'object'>
    """ RootContext(expression: CodeExpression, value: object) """
    @property
    def Expression(self) -> CodeExpression:
        """ Get: Expression(self: RootContext) -> CodeExpression """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: RootContext) -> object """
        ...



class RootDesignerSerializerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    RootDesignerSerializerAttribute(serializerType: Type, baseSerializerType: Type, reloadable: bool)
    RootDesignerSerializerAttribute(serializerTypeName: str, baseSerializerType: Type, reloadable: bool)
    RootDesignerSerializerAttribute(serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool)
    """
    @property
    def Reloadable(self) -> bool:
        """ Get: Reloadable(self: RootDesignerSerializerAttribute) -> bool """
        ...

    @property
    def SerializerBaseTypeName(self) -> str:
        """ Get: SerializerBaseTypeName(self: RootDesignerSerializerAttribute) -> str """
        ...

    @property
    def SerializerTypeName(self) -> str:
        """ Get: SerializerTypeName(self: RootDesignerSerializerAttribute) -> str """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, serializerType: Type, baseSerializerType: Type, reloadable: bool)
        __new__(cls: type, serializerTypeName: str, baseSerializerType: Type, reloadable: bool)
        __new__(cls: type, serializerTypeName: str, baseSerializerTypeName: str, reloadable: bool)
        """
        ...


class SerializationStore(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> ICollection:
        """ Get: Errors(self: SerializationStore) -> ICollection """
        ...


    def Close(self): # -> 
        """ Close(self: SerializationStore) """
        ...

    def Save(self, stream:Stream): # -> 
        """ Save(self: SerializationStore, stream: Stream) """
        ...


class SerializeAbsoluteContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    SerializeAbsoluteContext()
    SerializeAbsoluteContext(member: MemberDescriptor)
    """
    @property
    def Member(self) -> MemberDescriptor:
        """ Get: Member(self: SerializeAbsoluteContext) -> MemberDescriptor """
        ...


    def ShouldSerialize(self, member:MemberDescriptor) -> bool:
        """ ShouldSerialize(self: SerializeAbsoluteContext, member: MemberDescriptor) -> bool """
        ...


class StatementContext: # skipped bases: <type 'object'>, <type 'object'>
    """ StatementContext() """
    @property
    def StatementCollection(self) -> ObjectStatementCollection:
        """ Get: StatementCollection(self: StatementContext) -> ObjectStatementCollection """
        ...



class TypeCodeDomSerializer(CodeDomSerializerBase): # skipped bases: <type 'object'>
    """ TypeCodeDomSerializer() """
    def Deserialize(self, manager:IDesignerSerializationManager, declaration:CodeTypeDeclaration) -> object:
        """ Deserialize(self: TypeCodeDomSerializer, manager: IDesignerSerializationManager, declaration: CodeTypeDeclaration) -> object """
        ...

    def GetInitializeMethod(self, *args): #cannot find CLR method
        """ GetInitializeMethod(self: TypeCodeDomSerializer, manager: IDesignerSerializationManager, declaration: CodeTypeDeclaration, value: object) -> CodeMemberMethod """
        ...

    def GetInitializeMethods(self, *args): #cannot find CLR method
        """ GetInitializeMethods(self: TypeCodeDomSerializer, manager: IDesignerSerializationManager, declaration: CodeTypeDeclaration) -> Array[CodeMemberMethod] """
        ...

    def Serialize(self, manager:IDesignerSerializationManager, root:object, members:ICollection) -> CodeTypeDeclaration:
        """ Serialize(self: TypeCodeDomSerializer, manager: IDesignerSerializationManager, root: object, members: ICollection) -> CodeTypeDeclaration """
        ...


