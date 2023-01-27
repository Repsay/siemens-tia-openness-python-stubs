# encoding: utf-8
# module System.Web.ModelBinding calls itself ModelBinding
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, MulticastDelegate, Type)

from System.Collections import (ICollection, IDictionary, IEnumerable, 
    IEnumerator)

from System.Collections.Generic import Dictionary, KeyValuePair

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import CancelEventArgs

from System.ComponentModel.DataAnnotations import ValidationAttribute

from System.Globalization import CultureInfo

from System.Web import HttpContextBase

from typing import Self

"""The following names are not found in the module: (BoundEvent, Func, 
    TService, field#)
"""

# no functions
# classes

class ArrayModelBinder(CollectionModelBinder): # skipped bases: <type 'IModelBinder'>, <type 'object'>
    """ ArrayModelBinder[TElement]() """
    pass

class ModelBinderProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetBinder(self, modelBindingExecutionContext:ModelBindingExecutionContext, bindingContext:ModelBindingContext) -> IModelBinder:
        """ GetBinder(self: ModelBinderProvider, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) -> IModelBinder """
        ...


class ArrayModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ ArrayModelBinderProvider() """
    pass

class ModelMetadataProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetMetadataForProperties(self, container:object, containerType:Type) -> IEnumerable:
        """ GetMetadataForProperties(self: ModelMetadataProvider, container: object, containerType: Type) -> IEnumerable[ModelMetadata] """
        ...

    def GetMetadataForProperty(self, modelAccessor, containerType:Type, propertyName:str) -> ModelMetadata: # Not found arg types: {'modelAccessor': 'Func'}
        """ GetMetadataForProperty(self: ModelMetadataProvider, modelAccessor: Func[object], containerType: Type, propertyName: str) -> ModelMetadata """
        ...

    def GetMetadataForType(self, modelAccessor, modelType:Type) -> ModelMetadata: # Not found arg types: {'modelAccessor': 'Func'}
        """ GetMetadataForType(self: ModelMetadataProvider, modelAccessor: Func[object], modelType: Type) -> ModelMetadata """
        ...


class AssociatedMetadataProvider(ModelMetadataProvider): # skipped bases: <type 'object'>
    """ no doc """
    def CreateMetadata(self, *args): #cannot find CLR method
        """ CreateMetadata(self: AssociatedMetadataProvider, attributes: IEnumerable[Attribute], containerType: Type, modelAccessor: Func[object], modelType: Type, propertyName: str) -> ModelMetadata """
        ...

    def FilterAttributes(self, *args): #cannot find CLR method
        """ FilterAttributes(self: AssociatedMetadataProvider, containerType: Type, propertyDescriptor: PropertyDescriptor, attributes: IEnumerable[Attribute]) -> IEnumerable[Attribute] """
        ...

    def GetTypeDescriptor(self, *args): #cannot find CLR method
        """ GetTypeDescriptor(self: AssociatedMetadataProvider, type: Type) -> ICustomTypeDescriptor """
        ...


class ModelValidatorProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetValidators(self, metadata:ModelMetadata, context:ModelBindingExecutionContext) -> IEnumerable:
        """ GetValidators(self: ModelValidatorProvider, metadata: ModelMetadata, context: ModelBindingExecutionContext) -> IEnumerable[ModelValidator] """
        ...


class AssociatedValidatorProvider(ModelValidatorProvider): # skipped bases: <type 'object'>
    """ no doc """
    def GetTypeDescriptor(self, *args): #cannot find CLR method
        """ GetTypeDescriptor(self: AssociatedValidatorProvider, type: Type) -> ICustomTypeDescriptor """
        ...


class BinaryDataModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ BinaryDataModelBinderProvider() """
    pass

class BindingBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BindingBehavior, values: Never (1), Optional (0), Required (2) """
    Never: BindingBehavior = ...
    Optional: BindingBehavior = ...
    Required: BindingBehavior = ...
    value__ = ...


class BindingBehaviorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BindingBehaviorAttribute(behavior: BindingBehavior) """
    @property
    def Behavior(self) -> BindingBehavior:
        """ Get: Behavior(self: BindingBehaviorAttribute) -> BindingBehavior """
        ...


    def __new__(cls, behavior:BindingBehavior) -> Self:
        """ __new__(cls: type, behavior: BindingBehavior) """
        ...


class BindNeverAttribute(BindingBehaviorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BindNeverAttribute() """
    pass

class BindRequiredAttribute(BindingBehaviorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BindRequiredAttribute() """
    pass

class CollectionModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ CollectionModelBinder[TElement]() """
    def CreateOrReplaceCollection(self, *args): #cannot find CLR method
        """ CreateOrReplaceCollection(self: CollectionModelBinder[TElement], modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext, newCollection: IList[TElement]) -> bool """
        ...


class CollectionModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ CollectionModelBinderProvider() """
    pass

class ComplexModel: # skipped bases: <type 'object'>, <type 'object'>
    """ ComplexModel(modelMetadata: ModelMetadata, propertyMetadata: IEnumerable[ModelMetadata]) """
    @property
    def ModelMetadata(self) -> ModelMetadata:
        """ Get: ModelMetadata(self: ComplexModel) -> ModelMetadata """
        ...

    @property
    def PropertyMetadata(self) -> ReadOnlyCollection:
        """ Get: PropertyMetadata(self: ComplexModel) -> ReadOnlyCollection[ModelMetadata] """
        ...

    @property
    def Results(self) -> IDictionary:
        """ Get: Results(self: ComplexModel) -> IDictionary[ModelMetadata, ComplexModelResult] """
        ...



class ComplexModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ ComplexModelBinder() """
    pass

class ComplexModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ ComplexModelBinderProvider() """
    pass

class ComplexModelResult: # skipped bases: <type 'object'>, <type 'object'>
    """ ComplexModelResult(model: object, validationNode: ModelValidationNode) """
    @property
    def Model(self) -> object:
        """ Get: Model(self: ComplexModelResult) -> object """
        ...

    @property
    def ValidationNode(self) -> ModelValidationNode:
        """ Get: ValidationNode(self: ComplexModelResult) -> ModelValidationNode """
        ...



class IModelNameProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetModelName(self) -> str:
        """ GetModelName(self: IModelNameProvider) -> str """
        ...


class IValueProviderSource: # skipped bases: <type 'object'>
    """ no doc """
    def GetValueProvider(self, modelBindingExecutionContext:ModelBindingExecutionContext) -> IValueProvider:
        """ GetValueProvider(self: IValueProviderSource, modelBindingExecutionContext: ModelBindingExecutionContext) -> IValueProvider """
        ...


class ValueProviderSourceAttribute(Attribute, IModelNameProvider, IValueProviderSource): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class ControlAttribute(ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    ControlAttribute()
    ControlAttribute(controlID: str)
    ControlAttribute(controlID: str, propertyName: str)
    """
    @property
    def ControlID(self) -> str:
        """ Get: ControlID(self: ControlAttribute) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ControlAttribute) -> str """
        ...


    def __new__(cls, controlID:str = ..., propertyName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, controlID: str)
        __new__(cls: type, controlID: str, propertyName: str)
        """
        ...


class SimpleValueProvider(IValueProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ModelBindingExecutionContext(self):
        ...


    def FetchValue(self, *args): #cannot find CLR method
        """ FetchValue(self: SimpleValueProvider, key: str) -> object """
        ...


class ControlValueProvider(SimpleValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ ControlValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext, propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ControlValueProvider) -> str """
        ...



class IUnvalidatedValueProviderSource(IValueProviderSource): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ValidateInput(self) -> bool:
        """
        Get: ValidateInput(self: IUnvalidatedValueProviderSource) -> bool
        Set: ValidateInput(self: IUnvalidatedValueProviderSource) = value
        """
        ...



class CookieAttribute(IUnvalidatedValueProviderSource, ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    CookieAttribute()
    CookieAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CookieAttribute) -> str """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class CookieValueProvider(IUnvalidatedValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ CookieValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    def ContainsPrefix(self, prefix:str) -> bool:
        """ ContainsPrefix(self: CookieValueProvider, prefix: str) -> bool """
        ...


class ModelMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelMetadata(provider: ModelMetadataProvider, containerType: Type, modelAccessor: Func[object], modelType: Type, propertyName: str) """
    @property
    def AdditionalValues(self) -> Dictionary:
        """ Get: AdditionalValues(self: ModelMetadata) -> Dictionary[str, object] """
        ...

    @property
    def ContainerType(self) -> Type:
        """ Get: ContainerType(self: ModelMetadata) -> Type """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: ModelMetadata) -> bool
        Set: ConvertEmptyStringToNull(self: ModelMetadata) = value
        """
        ...

    @property
    def DataTypeName(self) -> str:
        """
        Get: DataTypeName(self: ModelMetadata) -> str
        Set: DataTypeName(self: ModelMetadata) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ModelMetadata) -> str
        Set: Description(self: ModelMetadata) = value
        """
        ...

    @property
    def DisplayFormatString(self) -> str:
        """
        Get: DisplayFormatString(self: ModelMetadata) -> str
        Set: DisplayFormatString(self: ModelMetadata) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ModelMetadata) -> str
        Set: DisplayName(self: ModelMetadata) = value
        """
        ...

    @property
    def EditFormatString(self) -> str:
        """
        Get: EditFormatString(self: ModelMetadata) -> str
        Set: EditFormatString(self: ModelMetadata) = value
        """
        ...

    @property
    def HideSurroundingHtml(self) -> bool:
        """
        Get: HideSurroundingHtml(self: ModelMetadata) -> bool
        Set: HideSurroundingHtml(self: ModelMetadata) = value
        """
        ...

    @property
    def IsComplexType(self) -> bool:
        """ Get: IsComplexType(self: ModelMetadata) -> bool """
        ...

    @property
    def IsNullableValueType(self) -> bool:
        """ Get: IsNullableValueType(self: ModelMetadata) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: ModelMetadata) -> bool
        Set: IsReadOnly(self: ModelMetadata) = value
        """
        ...

    @property
    def IsRequired(self) -> bool:
        """
        Get: IsRequired(self: ModelMetadata) -> bool
        Set: IsRequired(self: ModelMetadata) = value
        """
        ...

    @property
    def Model(self) -> object:
        """
        Get: Model(self: ModelMetadata) -> object
        Set: Model(self: ModelMetadata) = value
        """
        ...

    @property
    def ModelType(self) -> Type:
        """ Get: ModelType(self: ModelMetadata) -> Type """
        ...

    @property
    def NullDisplayText(self) -> str:
        """
        Get: NullDisplayText(self: ModelMetadata) -> str
        Set: NullDisplayText(self: ModelMetadata) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: ModelMetadata) -> int
        Set: Order(self: ModelMetadata) = value
        """
        ...

    @property
    def Properties(self) -> IEnumerable:
        """ Get: Properties(self: ModelMetadata) -> IEnumerable[ModelMetadata] """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ModelMetadata) -> str """
        ...

    @property
    def Provider(self):
        ...

    @property
    def RequestValidationEnabled(self) -> bool:
        """
        Get: RequestValidationEnabled(self: ModelMetadata) -> bool
        Set: RequestValidationEnabled(self: ModelMetadata) = value
        """
        ...

    @property
    def ShortDisplayName(self) -> str:
        """
        Get: ShortDisplayName(self: ModelMetadata) -> str
        Set: ShortDisplayName(self: ModelMetadata) = value
        """
        ...

    @property
    def ShowForDisplay(self) -> bool:
        """
        Get: ShowForDisplay(self: ModelMetadata) -> bool
        Set: ShowForDisplay(self: ModelMetadata) = value
        """
        ...

    @property
    def ShowForEdit(self) -> bool:
        """
        Get: ShowForEdit(self: ModelMetadata) -> bool
        Set: ShowForEdit(self: ModelMetadata) = value
        """
        ...

    @property
    def SimpleDisplayText(self) -> str:
        """
        Get: SimpleDisplayText(self: ModelMetadata) -> str
        Set: SimpleDisplayText(self: ModelMetadata) = value
        """
        ...

    @property
    def TemplateHint(self) -> str:
        """
        Get: TemplateHint(self: ModelMetadata) -> str
        Set: TemplateHint(self: ModelMetadata) = value
        """
        ...

    @property
    def Watermark(self) -> str:
        """
        Get: Watermark(self: ModelMetadata) -> str
        Set: Watermark(self: ModelMetadata) = value
        """
        ...


    def GetDisplayName(self) -> str:
        """ GetDisplayName(self: ModelMetadata) -> str """
        ...

    def GetSimpleDisplayText(self, *args): #cannot find CLR method
        """ GetSimpleDisplayText(self: ModelMetadata) -> str """
        ...

    def GetValidators(self, context:ModelBindingExecutionContext) -> IEnumerable:
        """ GetValidators(self: ModelMetadata, context: ModelBindingExecutionContext) -> IEnumerable[ModelValidator] """
        ...

    DefaultOrder: int = ...


class DataAnnotationsModelMetadata(ModelMetadata): # skipped bases: <type 'object'>
    """ DataAnnotationsModelMetadata(provider: DataAnnotationsModelMetadataProvider, containerType: Type, modelAccessor: Func[object], modelType: Type, propertyName: str, displayColumnAttribute: DisplayColumnAttribute) """
    pass

class DataAnnotationsModelMetadataProvider(AssociatedMetadataProvider): # skipped bases: <type 'object'>
    """ DataAnnotationsModelMetadataProvider() """
    pass

class DataAnnotationsModelValidationFactory(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataAnnotationsModelValidationFactory(object: object, method: IntPtr) """
    def BeginInvoke(self, metadata:ModelMetadata, context:ModelBindingExecutionContext, attribute:ValidationAttribute, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataAnnotationsModelValidationFactory, metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: ValidationAttribute, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> ModelValidator:
        """ EndInvoke(self: DataAnnotationsModelValidationFactory, result: IAsyncResult) -> ModelValidator """
        ...

    def Invoke(self, metadata:ModelMetadata, context:ModelBindingExecutionContext, attribute:ValidationAttribute) -> ModelValidator:
        """ Invoke(self: DataAnnotationsModelValidationFactory, metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: ValidationAttribute) -> ModelValidator """
        ...


class DataAnnotationsModelValidator: # skipped bases: <type 'object'>
    """ DataAnnotationsModelValidator(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: ValidationAttribute) """
    @property
    def Attribute(self):
        ...

    @property
    def ErrorMessage(self):
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: DataAnnotationsModelValidator) -> bool """
        ...

    @property
    def Metadata(self):
        ...

    @property
    def ModelBindingExecutionContext(self):
        ...


    def GetLocalizedErrorMessage(self, *args): #cannot find CLR method
        """ GetLocalizedErrorMessage(self: DataAnnotationsModelValidator, errorMessage: str) -> str """
        ...

    def GetLocalizedString(self, *args): #cannot find CLR method
        """ GetLocalizedString(self: DataAnnotationsModelValidator, name: str, *arguments: Array[object]) -> str """
        ...

    def Validate(self, container:object) -> IEnumerable:
        """ Validate(self: DataAnnotationsModelValidator, container: object) -> IEnumerable[ModelValidationResult] """
        ...

    def __new__(cls, metadata:ModelMetadata, context:ModelBindingExecutionContext, attribute:ValidationAttribute) -> Self:
        """ __new__(cls: type, metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: ValidationAttribute) """
        ...


class DataAnnotationsModelValidatorProvider(AssociatedValidatorProvider): # skipped bases: <type 'object'>
    """ DataAnnotationsModelValidatorProvider() """
    @property
    def AddImplicitRequiredAttributeForValueTypes(self) -> bool:
        """
        Get: AddImplicitRequiredAttributeForValueTypes() -> bool
        Set: AddImplicitRequiredAttributeForValueTypes() = value
        """
        ...


    @staticmethod
    def RegisterAdapter(attributeType:Type, adapterType:Type): # -> 
        """ RegisterAdapter(attributeType: Type, adapterType: Type) """
        ...

    @staticmethod
    def RegisterAdapterFactory(attributeType:Type, factory:DataAnnotationsModelValidationFactory): # -> 
        """ RegisterAdapterFactory(attributeType: Type, factory: DataAnnotationsModelValidationFactory) """
        ...

    @staticmethod
    def RegisterDefaultAdapter(adapterType:Type): # -> 
        """ RegisterDefaultAdapter(adapterType: Type) """
        ...

    @staticmethod
    def RegisterDefaultAdapterFactory(factory:DataAnnotationsModelValidationFactory): # -> 
        """ RegisterDefaultAdapterFactory(factory: DataAnnotationsModelValidationFactory) """
        ...

    @staticmethod
    def RegisterDefaultValidatableObjectAdapter(adapterType:Type): # -> 
        """ RegisterDefaultValidatableObjectAdapter(adapterType: Type) """
        ...

    @staticmethod
    def RegisterDefaultValidatableObjectAdapterFactory(factory:DataAnnotationsValidatableObjectAdapterFactory): # -> 
        """ RegisterDefaultValidatableObjectAdapterFactory(factory: DataAnnotationsValidatableObjectAdapterFactory) """
        ...

    @staticmethod
    def RegisterValidatableObjectAdapter(modelType:Type, adapterType:Type): # -> 
        """ RegisterValidatableObjectAdapter(modelType: Type, adapterType: Type) """
        ...

    @staticmethod
    def RegisterValidatableObjectAdapterFactory(modelType:Type, factory:DataAnnotationsValidatableObjectAdapterFactory): # -> 
        """ RegisterValidatableObjectAdapterFactory(modelType: Type, factory: DataAnnotationsValidatableObjectAdapterFactory) """
        ...



class DataAnnotationsValidatableObjectAdapterFactory(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataAnnotationsValidatableObjectAdapterFactory(object: object, method: IntPtr) """
    def BeginInvoke(self, metadata:ModelMetadata, context:ModelBindingExecutionContext, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataAnnotationsValidatableObjectAdapterFactory, metadata: ModelMetadata, context: ModelBindingExecutionContext, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> ModelValidator:
        """ EndInvoke(self: DataAnnotationsValidatableObjectAdapterFactory, result: IAsyncResult) -> ModelValidator """
        ...

    def Invoke(self, metadata:ModelMetadata, context:ModelBindingExecutionContext) -> ModelValidator:
        """ Invoke(self: DataAnnotationsValidatableObjectAdapterFactory, metadata: ModelMetadata, context: ModelBindingExecutionContext) -> ModelValidator """
        ...


class DefaultModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ DefaultModelBinder() """
    @property
    def Providers(self) -> ModelBinderProviderCollection:
        """ Get: Providers(self: DefaultModelBinder) -> ModelBinderProviderCollection """
        ...



class DictionaryModelBinder(CollectionModelBinder): # skipped bases: <type 'IModelBinder'>, <type 'object'>
    """ DictionaryModelBinder[TKey, TValue]() """
    pass

class DictionaryModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ DictionaryModelBinderProvider() """
    pass

class DictionaryValueProvider(IValueProvider): # skipped bases: <type 'object'>
    """ DictionaryValueProvider[TValue](dictionary: IDictionary[str, TValue], culture: CultureInfo) """
    pass

class EmptyModelMetadataProvider(AssociatedMetadataProvider): # skipped bases: <type 'object'>
    """ EmptyModelMetadataProvider() """
    pass

class ExtensibleModelBinderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExtensibleModelBinderAttribute(binderType: Type) """
    @property
    def BinderType(self) -> Type:
        """ Get: BinderType(self: ExtensibleModelBinderAttribute) -> Type """
        ...

    @property
    def SuppressPrefixCheck(self) -> bool:
        """
        Get: SuppressPrefixCheck(self: ExtensibleModelBinderAttribute) -> bool
        Set: SuppressPrefixCheck(self: ExtensibleModelBinderAttribute) = value
        """
        ...


    def __new__(cls, binderType:Type) -> Self:
        """ __new__(cls: type, binderType: Type) """
        ...


class FormAttribute(IUnvalidatedValueProviderSource, ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    FormAttribute()
    FormAttribute(fieldName: str)
    """
    @property
    def FieldName(self) -> str:
        """ Get: FieldName(self: FormAttribute) -> str """
        ...


    def __new__(cls, fieldName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fieldName: str)
        """
        ...


class NameValueCollectionValueProvider(IUnvalidatedValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """
    NameValueCollectionValueProvider(collection: NameValueCollection, culture: CultureInfo)
    NameValueCollectionValueProvider(collection: NameValueCollection, unvalidatedCollection: NameValueCollection, culture: CultureInfo)
    """
    def ContainsPrefix(self, prefix:str) -> bool:
        """ ContainsPrefix(self: NameValueCollectionValueProvider, prefix: str) -> bool """
        ...


class FormValueProvider(NameValueCollectionValueProvider): # skipped bases: <type 'IUnvalidatedValueProvider'>, <type 'IValueProvider'>, <type 'object'>
    """ FormValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

class GenericModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """
    GenericModelBinderProvider(modelType: Type, modelBinder: IModelBinder)
    GenericModelBinderProvider(modelType: Type, modelBinderType: Type)
    GenericModelBinderProvider(modelType: Type, modelBinderFactory: Func[Array[Type], IModelBinder])
    """
    @property
    def ModelType(self) -> Type:
        """ Get: ModelType(self: GenericModelBinderProvider) -> Type """
        ...

    @property
    def SuppressPrefixCheck(self) -> bool:
        """
        Get: SuppressPrefixCheck(self: GenericModelBinderProvider) -> bool
        Set: SuppressPrefixCheck(self: GenericModelBinderProvider) = value
        """
        ...


    def __new__(cls, modelType:Type, *__args:IModelBinder) -> Self:
        """
        __new__(cls: type, modelType: Type, modelBinder: IModelBinder)
        __new__(cls: type, modelType: Type, modelBinderType: Type)
        __new__(cls: type, modelType: Type, modelBinderFactory: Func[Array[Type], IModelBinder])
        """
        ...


class IMetadataAware: # skipped bases: <type 'object'>
    """ no doc """
    def OnMetadataCreated(self, metadata:ModelMetadata): # -> 
        """ OnMetadataCreated(self: IMetadataAware, metadata: ModelMetadata) """
        ...


class IModelBinder: # skipped bases: <type 'object'>
    """ no doc """
    def BindModel(self, modelBindingExecutionContext:ModelBindingExecutionContext, bindingContext:ModelBindingContext) -> bool:
        """ BindModel(self: IModelBinder, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) -> bool """
        ...


class IValueProvider: # skipped bases: <type 'object'>
    """ no doc """
    def ContainsPrefix(self, prefix:str) -> bool:
        """ ContainsPrefix(self: IValueProvider, prefix: str) -> bool """
        ...

    def GetValue(self, key:str) -> ValueProviderResult:
        """ GetValue(self: IValueProvider, key: str) -> ValueProviderResult """
        ...


class IUnvalidatedValueProvider(IValueProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class KeyValuePairModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ KeyValuePairModelBinder[TKey, TValue]() """
    pass

class KeyValuePairModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ KeyValuePairModelBinderProvider() """
    pass

class ModelValidator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: ModelValidator) -> bool """
        ...

    @property
    def Metadata(self):
        ...

    @property
    def ModelBindingExecutionContext(self):
        ...


    @staticmethod
    def GetModelValidator(metadata:ModelMetadata, context:ModelBindingExecutionContext) -> ModelValidator:
        """ GetModelValidator(metadata: ModelMetadata, context: ModelBindingExecutionContext) -> ModelValidator """
        ...

    def Validate(self, container:object) -> IEnumerable:
        """ Validate(self: ModelValidator, container: object) -> IEnumerable[ModelValidationResult] """
        ...


class MaxLengthAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ MaxLengthAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: MaxLengthAttribute) """
    pass

class MinLengthAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ MinLengthAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: MinLengthAttribute) """
    pass

class ModelBinderDictionary(IDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[Type, IModelBinder]]'>, <type 'IEnumerable'>, <type 'ICollection[KeyValuePair[Type, IModelBinder]]'>, <type 'object'>
    """ ModelBinderDictionary() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ModelBinderDictionary) -> int """
        ...

    @property
    def DefaultBinder(self) -> IModelBinder:
        """
        Get: DefaultBinder(self: ModelBinderDictionary) -> IModelBinder
        Set: DefaultBinder(self: ModelBinderDictionary) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ModelBinderDictionary) -> bool """
        ...


    def Clear(self): # -> 
        """ Clear(self: ModelBinderDictionary) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: ModelBinderDictionary, item: KeyValuePair[Type, IModelBinder]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ModelBinderDictionary, array: Array[KeyValuePair[Type, IModelBinder]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ModelBinderDictionary) -> IEnumerator[KeyValuePair[Type, IModelBinder]] """
        ...


class ModelBinderErrorMessageProvider(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ModelBinderErrorMessageProvider(object: object, method: IntPtr) """
    def BeginInvoke(self, modelBindingExecutionContext:ModelBindingExecutionContext, modelMetadata:ModelMetadata, incomingValue:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ModelBinderErrorMessageProvider, modelBindingExecutionContext: ModelBindingExecutionContext, modelMetadata: ModelMetadata, incomingValue: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> str:
        """ EndInvoke(self: ModelBinderErrorMessageProvider, result: IAsyncResult) -> str """
        ...

    def Invoke(self, modelBindingExecutionContext:ModelBindingExecutionContext, modelMetadata:ModelMetadata, incomingValue:object) -> str:
        """ Invoke(self: ModelBinderErrorMessageProvider, modelBindingExecutionContext: ModelBindingExecutionContext, modelMetadata: ModelMetadata, incomingValue: object) -> str """
        ...


class ModelBinderErrorMessageProviders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TypeConversionErrorMessageProvider(self) -> ModelBinderErrorMessageProvider:
        """
        Get: TypeConversionErrorMessageProvider() -> ModelBinderErrorMessageProvider
        Set: TypeConversionErrorMessageProvider() = value
        """
        ...

    @property
    def ValueRequiredErrorMessageProvider(self) -> ModelBinderErrorMessageProvider:
        """
        Get: ValueRequiredErrorMessageProvider() -> ModelBinderErrorMessageProvider
        Set: ValueRequiredErrorMessageProvider() = value
        """
        ...


    __all__: list = ...


class ModelBinderProviderCollection(Collection): # skipped bases: <type 'ICollection[ModelBinderProvider]'>, <type 'IEnumerable'>, <type 'IEnumerable[ModelBinderProvider]'>, <type 'IList'>, <type 'IList[ModelBinderProvider]'>, <type 'IReadOnlyList[ModelBinderProvider]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[ModelBinderProvider]'>, <type 'object'>
    """
    ModelBinderProviderCollection()
    ModelBinderProviderCollection(list: IList[ModelBinderProvider])
    """
    def GetBinder(self, modelBindingExecutionContext:ModelBindingExecutionContext, bindingContext:ModelBindingContext) -> IModelBinder:
        """ GetBinder(self: ModelBinderProviderCollection, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) -> IModelBinder """
        ...

    def RegisterBinderForGenericType(self, modelType:Type, *__args:IModelBinder): # -> 
        """ RegisterBinderForGenericType(self: ModelBinderProviderCollection, modelType: Type, modelBinder: IModelBinder)RegisterBinderForGenericType(self: ModelBinderProviderCollection, modelType: Type, modelBinderFactory: Func[Array[Type], IModelBinder])RegisterBinderForGenericType(self: ModelBinderProviderCollection, modelType: Type, modelBinderType: Type) """
        ...

    def RegisterBinderForType(self, modelType:Type, *__args:IModelBinder): # -> 
        """ RegisterBinderForType(self: ModelBinderProviderCollection, modelType: Type, modelBinder: IModelBinder)RegisterBinderForType(self: ModelBinderProviderCollection, modelType: Type, modelBinderFactory: Func[IModelBinder]) """
        ...


class ModelBinderProviderOptionsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ModelBinderProviderOptionsAttribute() """
    @property
    def FrontOfList(self) -> bool:
        """
        Get: FrontOfList(self: ModelBinderProviderOptionsAttribute) -> bool
        Set: FrontOfList(self: ModelBinderProviderOptionsAttribute) = value
        """
        ...



class ModelBinderProviders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Providers(self) -> ModelBinderProviderCollection:
        """ Get: Providers() -> ModelBinderProviderCollection """
        ...


    __all__: list = ...


class ModelBinders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Binders(self) -> ModelBinderDictionary:
        """ Get: Binders() -> ModelBinderDictionary """
        ...


    __all__: list = ...


class ModelBindingContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    ModelBindingContext()
    ModelBindingContext(bindingContext: ModelBindingContext)
    """
    @property
    def Model(self) -> object:
        """
        Get: Model(self: ModelBindingContext) -> object
        Set: Model(self: ModelBindingContext) = value
        """
        ...

    @property
    def ModelBinderProviders(self) -> ModelBinderProviderCollection:
        """
        Get: ModelBinderProviders(self: ModelBindingContext) -> ModelBinderProviderCollection
        Set: ModelBinderProviders(self: ModelBindingContext) = value
        """
        ...

    @property
    def ModelMetadata(self) -> ModelMetadata:
        """
        Get: ModelMetadata(self: ModelBindingContext) -> ModelMetadata
        Set: ModelMetadata(self: ModelBindingContext) = value
        """
        ...

    @property
    def ModelName(self) -> str:
        """
        Get: ModelName(self: ModelBindingContext) -> str
        Set: ModelName(self: ModelBindingContext) = value
        """
        ...

    @property
    def ModelState(self) -> ModelStateDictionary:
        """
        Get: ModelState(self: ModelBindingContext) -> ModelStateDictionary
        Set: ModelState(self: ModelBindingContext) = value
        """
        ...

    @property
    def ModelType(self) -> Type:
        """ Get: ModelType(self: ModelBindingContext) -> Type """
        ...

    @property
    def PropertyMetadata(self) -> IDictionary:
        """ Get: PropertyMetadata(self: ModelBindingContext) -> IDictionary[str, ModelMetadata] """
        ...

    @property
    def ValidateRequest(self) -> bool:
        """
        Get: ValidateRequest(self: ModelBindingContext) -> bool
        Set: ValidateRequest(self: ModelBindingContext) = value
        """
        ...

    @property
    def ValidationNode(self) -> ModelValidationNode:
        """
        Get: ValidationNode(self: ModelBindingContext) -> ModelValidationNode
        Set: ValidationNode(self: ModelBindingContext) = value
        """
        ...

    @property
    def ValueProvider(self) -> IValueProvider:
        """
        Get: ValueProvider(self: ModelBindingContext) -> IValueProvider
        Set: ValueProvider(self: ModelBindingContext) = value
        """
        ...



class ModelBindingExecutionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelBindingExecutionContext(httpContext: HttpContextBase, modelState: ModelStateDictionary) """
    @property
    def HttpContext(self) -> HttpContextBase:
        """ Get: HttpContext(self: ModelBindingExecutionContext) -> HttpContextBase """
        ...

    @property
    def ModelState(self) -> ModelStateDictionary:
        """ Get: ModelState(self: ModelBindingExecutionContext) -> ModelStateDictionary """
        ...


    def GetService(self): # -> TService
        """ GetService[TService](self: ModelBindingExecutionContext) -> TService """
        ...

    def PublishService(self, service): # ->  # Not found arg types: {'service': 'TService'}
        """ PublishService[TService](self: ModelBindingExecutionContext, service: TService) """
        ...

    def TryGetService(self): # -> TService
        """ TryGetService[TService](self: ModelBindingExecutionContext) -> TService """
        ...


class ModelError: # skipped bases: <type 'object'>, <type 'object'>
    """
    ModelError(exception: Exception)
    ModelError(exception: Exception, errorMessage: str)
    ModelError(errorMessage: str)
    """
    @property
    def ErrorMessage(self) -> str:
        """ Get: ErrorMessage(self: ModelError) -> str """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ModelError) -> Exception """
        ...



class ModelErrorCollection(Collection): # skipped bases: <type 'IReadOnlyList[ModelError]'>, <type 'IEnumerable'>, <type 'ICollection[ModelError]'>, <type 'IList'>, <type 'IList[ModelError]'>, <type 'IReadOnlyCollection[ModelError]'>, <type 'IEnumerable[ModelError]'>, <type 'ICollection'>, <type 'object'>
    """ ModelErrorCollection() """
    pass

class ModelMetadataProviders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> ModelMetadataProvider:
        """
        Get: Current() -> ModelMetadataProvider
        Set: Current() = value
        """
        ...


    __all__: list = ...


class ModelState: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelState() """
    @property
    def Errors(self) -> ModelErrorCollection:
        """ Get: Errors(self: ModelState) -> ModelErrorCollection """
        ...

    @property
    def Value(self) -> ValueProviderResult:
        """
        Get: Value(self: ModelState) -> ValueProviderResult
        Set: Value(self: ModelState) = value
        """
        ...



class ModelStateDictionary(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[str, ModelState]]'>, <type 'ICollection[KeyValuePair[str, ModelState]]'>, <type 'object'>
    """
    ModelStateDictionary()
    ModelStateDictionary(dictionary: ModelStateDictionary)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ModelStateDictionary) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ModelStateDictionary) -> bool """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: ModelStateDictionary) -> bool """
        ...


    def AddModelError(self, key:str, *__args:Exception): # -> 
        """ AddModelError(self: ModelStateDictionary, key: str, exception: Exception)AddModelError(self: ModelStateDictionary, key: str, errorMessage: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ModelStateDictionary) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: ModelStateDictionary, item: KeyValuePair[str, ModelState]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ModelStateDictionary, array: Array[KeyValuePair[str, ModelState]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ModelStateDictionary) -> IEnumerator[KeyValuePair[str, ModelState]] """
        ...

    def IsValidField(self, key:str) -> bool:
        """ IsValidField(self: ModelStateDictionary, key: str) -> bool """
        ...

    def Merge(self, dictionary:ModelStateDictionary): # -> 
        """ Merge(self: ModelStateDictionary, dictionary: ModelStateDictionary) """
        ...

    def SetModelValue(self, key:str, value:ValueProviderResult): # -> 
        """ SetModelValue(self: ModelStateDictionary, key: str, value: ValueProviderResult) """
        ...


class ModelValidatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ModelValidatedEventArgs(modelBindingExecutionContext: ModelBindingExecutionContext, parentNode: ModelValidationNode) """
    @property
    def ModelBindingExecutionContext(self) -> ModelBindingExecutionContext:
        """ Get: ModelBindingExecutionContext(self: ModelValidatedEventArgs) -> ModelBindingExecutionContext """
        ...

    @property
    def ParentNode(self) -> ModelValidationNode:
        """ Get: ParentNode(self: ModelValidatedEventArgs) -> ModelValidationNode """
        ...


    def __new__(cls, modelBindingExecutionContext:ModelBindingExecutionContext, parentNode:ModelValidationNode) -> Self:
        """ __new__(cls: type, modelBindingExecutionContext: ModelBindingExecutionContext, parentNode: ModelValidationNode) """
        ...


class ModelValidatingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ModelValidatingEventArgs(modelBindingExecutionContext: ModelBindingExecutionContext, parentNode: ModelValidationNode) """
    @property
    def ModelBindingExecutionContext(self) -> ModelBindingExecutionContext:
        """ Get: ModelBindingExecutionContext(self: ModelValidatingEventArgs) -> ModelBindingExecutionContext """
        ...

    @property
    def ParentNode(self) -> ModelValidationNode:
        """ Get: ParentNode(self: ModelValidatingEventArgs) -> ModelValidationNode """
        ...



class ModelValidationNode: # skipped bases: <type 'object'>, <type 'object'>
    """
    ModelValidationNode(modelMetadata: ModelMetadata, modelStateKey: str)
    ModelValidationNode(modelMetadata: ModelMetadata, modelStateKey: str, childNodes: IEnumerable[ModelValidationNode])
    """
    @property
    def ChildNodes(self) -> ICollection:
        """ Get: ChildNodes(self: ModelValidationNode) -> ICollection[ModelValidationNode] """
        ...

    @property
    def ModelMetadata(self) -> ModelMetadata:
        """ Get: ModelMetadata(self: ModelValidationNode) -> ModelMetadata """
        ...

    @property
    def ModelStateKey(self) -> str:
        """ Get: ModelStateKey(self: ModelValidationNode) -> str """
        ...

    @property
    def SuppressValidation(self) -> bool:
        """
        Get: SuppressValidation(self: ModelValidationNode) -> bool
        Set: SuppressValidation(self: ModelValidationNode) = value
        """
        ...

    @property
    def ValidateAllProperties(self) -> bool:
        """
        Get: ValidateAllProperties(self: ModelValidationNode) -> bool
        Set: ValidateAllProperties(self: ModelValidationNode) = value
        """
        ...


    def CombineWith(self, otherNode:ModelValidationNode): # -> 
        """ CombineWith(self: ModelValidationNode, otherNode: ModelValidationNode) """
        ...

    def Validate(self, modelBindingExecutionContext:ModelBindingExecutionContext, parentNode:ModelValidationNode = ...): # -> 
        """ Validate(self: ModelValidationNode, modelBindingExecutionContext: ModelBindingExecutionContext)Validate(self: ModelValidationNode, modelBindingExecutionContext: ModelBindingExecutionContext, parentNode: ModelValidationNode) """
        ...

    Validated = ...
    Validating = ...


class ModelValidationResult: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelValidationResult() """
    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: ModelValidationResult) -> str
        Set: MemberName(self: ModelValidationResult) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: ModelValidationResult) -> str
        Set: Message(self: ModelValidationResult) = value
        """
        ...



class ModelValidatorProviderCollection(Collection): # skipped bases: <type 'IList[ModelValidatorProvider]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[ModelValidatorProvider]'>, <type 'IReadOnlyList[ModelValidatorProvider]'>, <type 'IReadOnlyCollection[ModelValidatorProvider]'>, <type 'ICollection'>, <type 'IEnumerable[ModelValidatorProvider]'>, <type 'object'>
    """
    ModelValidatorProviderCollection()
    ModelValidatorProviderCollection(list: IList[ModelValidatorProvider])
    """
    def GetValidators(self, metadata:ModelMetadata, context:ModelBindingExecutionContext) -> IEnumerable:
        """ GetValidators(self: ModelValidatorProviderCollection, metadata: ModelMetadata, context: ModelBindingExecutionContext) -> IEnumerable[ModelValidator] """
        ...


class ModelValidatorProviders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Providers(self) -> ModelValidatorProviderCollection:
        """ Get: Providers() -> ModelValidatorProviderCollection """
        ...


    __all__: list = ...


class MutableObjectModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ MutableObjectModelBinder() """
    def CanUpdateProperty(self, *args): #cannot find CLR method
        """ CanUpdateProperty(self: MutableObjectModelBinder, propertyMetadata: ModelMetadata) -> bool """
        ...

    def CreateModel(self, *args): #cannot find CLR method
        """ CreateModel(self: MutableObjectModelBinder, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) -> object """
        ...

    def EnsureModel(self, *args): #cannot find CLR method
        """ EnsureModel(self: MutableObjectModelBinder, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) """
        ...

    def GetMetadataForProperties(self, *args): #cannot find CLR method
        """ GetMetadataForProperties(self: MutableObjectModelBinder, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext) -> IEnumerable[ModelMetadata] """
        ...

    def SetProperty(self, *args): #cannot find CLR method
        """ SetProperty(self: MutableObjectModelBinder, modelBindingExecutionContext: ModelBindingExecutionContext, bindingContext: ModelBindingContext, propertyMetadata: ModelMetadata, complexModelResult: ComplexModelResult) """
        ...


class MutableObjectModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ MutableObjectModelBinderProvider() """
    pass

class ProfileAttribute(ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    ProfileAttribute()
    ProfileAttribute(key: str)
    """
    @property
    def Key(self) -> str:
        """ Get: Key(self: ProfileAttribute) -> str """
        ...


    def __new__(cls, key:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        ...


class ProfileValueProvider(SimpleValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ ProfileValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

class QueryStringAttribute(IUnvalidatedValueProviderSource, ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    QueryStringAttribute()
    QueryStringAttribute(key: str)
    """
    @property
    def Key(self) -> str:
        """ Get: Key(self: QueryStringAttribute) -> str """
        ...


    def __new__(cls, key:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        ...


class QueryStringValueProvider(NameValueCollectionValueProvider): # skipped bases: <type 'IUnvalidatedValueProvider'>, <type 'IValueProvider'>, <type 'object'>
    """ QueryStringValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

class RangeAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ RangeAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: RangeAttribute) """
    pass

class RegularExpressionAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ RegularExpressionAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: RegularExpressionAttribute) """
    pass

class RequiredAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ RequiredAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: RequiredAttribute) """
    pass

class RouteDataAttribute(ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    RouteDataAttribute()
    RouteDataAttribute(key: str)
    """
    @property
    def Key(self) -> str:
        """ Get: Key(self: RouteDataAttribute) -> str """
        ...


    def __new__(cls, key:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        ...


class RouteDataValueProvider(DictionaryValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ RouteDataValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

class SessionAttribute(ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    SessionAttribute()
    SessionAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SessionAttribute) -> str """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class SimpleModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """
    SimpleModelBinderProvider(modelType: Type, modelBinder: IModelBinder)
    SimpleModelBinderProvider(modelType: Type, modelBinderFactory: Func[IModelBinder])
    """
    @property
    def ModelType(self) -> Type:
        """ Get: ModelType(self: SimpleModelBinderProvider) -> Type """
        ...

    @property
    def SuppressPrefixCheck(self) -> bool:
        """
        Get: SuppressPrefixCheck(self: SimpleModelBinderProvider) -> bool
        Set: SuppressPrefixCheck(self: SimpleModelBinderProvider) = value
        """
        ...


    def __new__(cls, modelType:Type, *__args:IModelBinder) -> Self:
        """
        __new__(cls: type, modelType: Type, modelBinder: IModelBinder)
        __new__(cls: type, modelType: Type, modelBinderFactory: Func[IModelBinder])
        """
        ...


class StringLengthAttributeAdapter(DataAnnotationsModelValidator): # skipped bases: <type 'object'>
    """ StringLengthAttributeAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext, attribute: StringLengthAttribute) """
    pass

class TypeConverterModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ TypeConverterModelBinder() """
    pass

class TypeConverterModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ TypeConverterModelBinderProvider() """
    pass

class TypeMatchModelBinder(IModelBinder): # skipped bases: <type 'object'>
    """ TypeMatchModelBinder() """
    pass

class TypeMatchModelBinderProvider(ModelBinderProvider): # skipped bases: <type 'object'>
    """ TypeMatchModelBinderProvider() """
    pass

class UserProfileAttribute(Attribute, IValueProviderSource): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UserProfileAttribute() """
    pass

class UserProfileValueProvider(SimpleValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ UserProfileValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

class ValidatableObjectAdapter(ModelValidator): # skipped bases: <type 'object'>
    """ ValidatableObjectAdapter(metadata: ModelMetadata, context: ModelBindingExecutionContext) """
    pass

class ValueProviderCollection(IUnvalidatedValueProvider, Collection): # skipped bases: <type 'IReadOnlyCollection[IValueProvider]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[IValueProvider]'>, <type 'ICollection[IValueProvider]'>, <type 'IEnumerable[IValueProvider]'>, <type 'IList[IValueProvider]'>, <type 'ICollection'>, <type 'IValueProvider'>, <type 'object'>
    """
    ValueProviderCollection()
    ValueProviderCollection(list: IList[IValueProvider])
    """
    def ContainsPrefix(self, prefix:str) -> bool:
        """ ContainsPrefix(self: ValueProviderCollection, prefix: str) -> bool """
        ...


class ValueProviderResult: # skipped bases: <type 'object'>, <type 'object'>
    """ ValueProviderResult(rawValue: object, attemptedValue: str, culture: CultureInfo) """
    @property
    def AttemptedValue(self) -> str:
        """ Get: AttemptedValue(self: ValueProviderResult) -> str """
        ...

    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: ValueProviderResult) -> CultureInfo """
        ...

    @property
    def RawValue(self) -> object:
        """ Get: RawValue(self: ValueProviderResult) -> object """
        ...


    def ConvertTo(self, type:Type, culture:CultureInfo = ...) -> object:
        """
        ConvertTo(self: ValueProviderResult, type: Type) -> object
        ConvertTo(self: ValueProviderResult, type: Type, culture: CultureInfo) -> object
        """
        ...


class ViewStateAttribute(ValueProviderSourceAttribute): # skipped bases: <type '_Attribute'>, <type 'IModelNameProvider'>, <type 'IValueProviderSource'>, <type 'object'>
    """
    ViewStateAttribute()
    ViewStateAttribute(key: str)
    """
    @property
    def Key(self) -> str:
        """ Get: Key(self: ViewStateAttribute) -> str """
        ...


    def __new__(cls, key:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        ...


class ViewStateValueProvider(SimpleValueProvider): # skipped bases: <type 'IValueProvider'>, <type 'object'>
    """ ViewStateValueProvider(modelBindingExecutionContext: ModelBindingExecutionContext) """
    pass

