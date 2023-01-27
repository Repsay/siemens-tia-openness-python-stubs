# encoding: utf-8
# module System.ComponentModel.DataAnnotations calls itself DataAnnotations
# from System.ComponentModel.DataAnnotations, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, IServiceProvider, Nullable, Type

from System.Collections import ICollection, IDictionary, IEnumerable

from System.ComponentModel import TypeDescriptionProvider

from System.ComponentModel.Design import IServiceContainer

from typing import Self

"""The following names are not found in the module: BoundEvent, Func, field#
"""

# no functions
# classes

class AssociatedMetadataTypeTypeDescriptionProvider(TypeDescriptionProvider): # skipped bases: <type 'object'>
    """
    AssociatedMetadataTypeTypeDescriptionProvider(type: Type)
    AssociatedMetadataTypeTypeDescriptionProvider(type: Type, associatedMetadataType: Type)
    """
    pass

class AssociationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssociationAttribute(name: str, thisKey: str, otherKey: str) """
    @property
    def IsForeignKey(self) -> bool:
        """
        Get: IsForeignKey(self: AssociationAttribute) -> bool
        Set: IsForeignKey(self: AssociationAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AssociationAttribute) -> str """
        ...

    @property
    def OtherKey(self) -> str:
        """ Get: OtherKey(self: AssociationAttribute) -> str """
        ...

    @property
    def OtherKeyMembers(self) -> IEnumerable:
        """ Get: OtherKeyMembers(self: AssociationAttribute) -> IEnumerable[str] """
        ...

    @property
    def ThisKey(self) -> str:
        """ Get: ThisKey(self: AssociationAttribute) -> str """
        ...

    @property
    def ThisKeyMembers(self) -> IEnumerable:
        """ Get: ThisKeyMembers(self: AssociationAttribute) -> IEnumerable[str] """
        ...


    def __new__(cls, name:str, thisKey:str, otherKey:str) -> Self:
        """ __new__(cls: type, name: str, thisKey: str, otherKey: str) """
        ...


class BindableTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BindableTypeAttribute() """
    @property
    def IsBindable(self) -> bool:
        """
        Get: IsBindable(self: BindableTypeAttribute) -> bool
        Set: IsBindable(self: BindableTypeAttribute) = value
        """
        ...



class ValidationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def ErrorMessage(self) -> str:
        """
        Get: ErrorMessage(self: ValidationAttribute) -> str
        Set: ErrorMessage(self: ValidationAttribute) = value
        """
        ...

    @property
    def ErrorMessageResourceName(self) -> str:
        """
        Get: ErrorMessageResourceName(self: ValidationAttribute) -> str
        Set: ErrorMessageResourceName(self: ValidationAttribute) = value
        """
        ...

    @property
    def ErrorMessageResourceType(self) -> Type:
        """
        Get: ErrorMessageResourceType(self: ValidationAttribute) -> Type
        Set: ErrorMessageResourceType(self: ValidationAttribute) = value
        """
        ...

    @property
    def ErrorMessageString(self):
        ...

    @property
    def RequiresValidationContext(self) -> bool:
        """ Get: RequiresValidationContext(self: ValidationAttribute) -> bool """
        ...


    def FormatErrorMessage(self, name:str) -> str:
        """ FormatErrorMessage(self: ValidationAttribute, name: str) -> str """
        ...

    def GetValidationResult(self, value:object, validationContext:ValidationContext) -> ValidationResult:
        """ GetValidationResult(self: ValidationAttribute, value: object, validationContext: ValidationContext) -> ValidationResult """
        ...

    def IsValid(self, value:object) -> bool:
        """ IsValid(self: ValidationAttribute, value: object) -> bool """
        ...

    def Validate(self, value:object, *__args:str): # -> 
        """ Validate(self: ValidationAttribute, value: object, name: str)Validate(self: ValidationAttribute, value: object, validationContext: ValidationContext) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, errorMessage: str)
        __new__(cls: type, errorMessageAccessor: Func[str])
        """
        ...


class CompareAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CompareAttribute(otherProperty: str) """
    @property
    def OtherProperty(self) -> str:
        """ Get: OtherProperty(self: CompareAttribute) -> str """
        ...

    @property
    def OtherPropertyDisplayName(self) -> str:
        """ Get: OtherPropertyDisplayName(self: CompareAttribute) -> str """
        ...



class ConcurrencyCheckAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConcurrencyCheckAttribute() """
    pass

class DataTypeAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataTypeAttribute(dataType: DataType)
    DataTypeAttribute(customDataType: str)
    """
    @property
    def CustomDataType(self) -> str:
        """ Get: CustomDataType(self: DataTypeAttribute) -> str """
        ...

    @property
    def DataType(self) -> DataType:
        """ Get: DataType(self: DataTypeAttribute) -> DataType """
        ...

    @property
    def DisplayFormat(self) -> DisplayFormatAttribute:
        """ Get: DisplayFormat(self: DataTypeAttribute) -> DisplayFormatAttribute """
        ...


    def GetDataTypeName(self) -> str:
        """ GetDataTypeName(self: DataTypeAttribute) -> str """
        ...


class CreditCardAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CreditCardAttribute() """
    pass

class CustomValidationAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CustomValidationAttribute(validatorType: Type, method: str) """
    @property
    def Method(self) -> str:
        """ Get: Method(self: CustomValidationAttribute) -> str """
        ...

    @property
    def TypeId(self) -> object:
        """ Get: TypeId(self: CustomValidationAttribute) -> object """
        ...

    @property
    def ValidatorType(self) -> Type:
        """ Get: ValidatorType(self: CustomValidationAttribute) -> Type """
        ...



class DataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataType, values: CreditCard (14), Currency (6), Custom (0), Date (2), DateTime (1), Duration (4), EmailAddress (10), Html (8), ImageUrl (13), MultilineText (9), Password (11), PhoneNumber (5), PostalCode (15), Text (7), Time (3), Upload (16), Url (12) """
    CreditCard: DataType = ...
    Currency: DataType = ...
    Custom: DataType = ...
    Date: DataType = ...
    DateTime: DataType = ...
    Duration: DataType = ...
    EmailAddress: DataType = ...
    Html: DataType = ...
    ImageUrl: DataType = ...
    MultilineText: DataType = ...
    Password: DataType = ...
    PhoneNumber: DataType = ...
    PostalCode: DataType = ...
    Text: DataType = ...
    Time: DataType = ...
    Upload: DataType = ...
    Url: DataType = ...
    value__ = ...


class DisplayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisplayAttribute() """
    @property
    def AutoGenerateField(self) -> bool:
        """
        Get: AutoGenerateField(self: DisplayAttribute) -> bool
        Set: AutoGenerateField(self: DisplayAttribute) = value
        """
        ...

    @property
    def AutoGenerateFilter(self) -> bool:
        """
        Get: AutoGenerateFilter(self: DisplayAttribute) -> bool
        Set: AutoGenerateFilter(self: DisplayAttribute) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: DisplayAttribute) -> str
        Set: Description(self: DisplayAttribute) = value
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: DisplayAttribute) -> str
        Set: GroupName(self: DisplayAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DisplayAttribute) -> str
        Set: Name(self: DisplayAttribute) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: DisplayAttribute) -> int
        Set: Order(self: DisplayAttribute) = value
        """
        ...

    @property
    def Prompt(self) -> str:
        """
        Get: Prompt(self: DisplayAttribute) -> str
        Set: Prompt(self: DisplayAttribute) = value
        """
        ...

    @property
    def ResourceType(self) -> Type:
        """
        Get: ResourceType(self: DisplayAttribute) -> Type
        Set: ResourceType(self: DisplayAttribute) = value
        """
        ...

    @property
    def ShortName(self) -> str:
        """
        Get: ShortName(self: DisplayAttribute) -> str
        Set: ShortName(self: DisplayAttribute) = value
        """
        ...


    def GetAutoGenerateField(self) -> Nullable:
        """ GetAutoGenerateField(self: DisplayAttribute) -> Nullable[bool] """
        ...

    def GetAutoGenerateFilter(self) -> Nullable:
        """ GetAutoGenerateFilter(self: DisplayAttribute) -> Nullable[bool] """
        ...

    def GetDescription(self) -> str:
        """ GetDescription(self: DisplayAttribute) -> str """
        ...

    def GetGroupName(self) -> str:
        """ GetGroupName(self: DisplayAttribute) -> str """
        ...

    def GetName(self) -> str:
        """ GetName(self: DisplayAttribute) -> str """
        ...

    def GetOrder(self) -> Nullable:
        """ GetOrder(self: DisplayAttribute) -> Nullable[int] """
        ...

    def GetPrompt(self) -> str:
        """ GetPrompt(self: DisplayAttribute) -> str """
        ...

    def GetShortName(self) -> str:
        """ GetShortName(self: DisplayAttribute) -> str """
        ...


class DisplayColumnAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DisplayColumnAttribute(displayColumn: str)
    DisplayColumnAttribute(displayColumn: str, sortColumn: str)
    DisplayColumnAttribute(displayColumn: str, sortColumn: str, sortDescending: bool)
    """
    @property
    def DisplayColumn(self) -> str:
        """ Get: DisplayColumn(self: DisplayColumnAttribute) -> str """
        ...

    @property
    def SortColumn(self) -> str:
        """ Get: SortColumn(self: DisplayColumnAttribute) -> str """
        ...

    @property
    def SortDescending(self) -> bool:
        """ Get: SortDescending(self: DisplayColumnAttribute) -> bool """
        ...


    def __new__(cls, displayColumn:str, sortColumn:str = ..., sortDescending:bool = ...) -> Self:
        """
        __new__(cls: type, displayColumn: str)
        __new__(cls: type, displayColumn: str, sortColumn: str)
        __new__(cls: type, displayColumn: str, sortColumn: str, sortDescending: bool)
        """
        ...


class DisplayFormatAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisplayFormatAttribute() """
    @property
    def ApplyFormatInEditMode(self) -> bool:
        """
        Get: ApplyFormatInEditMode(self: DisplayFormatAttribute) -> bool
        Set: ApplyFormatInEditMode(self: DisplayFormatAttribute) = value
        """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: DisplayFormatAttribute) -> bool
        Set: ConvertEmptyStringToNull(self: DisplayFormatAttribute) = value
        """
        ...

    @property
    def DataFormatString(self) -> str:
        """
        Get: DataFormatString(self: DisplayFormatAttribute) -> str
        Set: DataFormatString(self: DisplayFormatAttribute) = value
        """
        ...

    @property
    def HtmlEncode(self) -> bool:
        """
        Get: HtmlEncode(self: DisplayFormatAttribute) -> bool
        Set: HtmlEncode(self: DisplayFormatAttribute) = value
        """
        ...

    @property
    def NullDisplayText(self) -> str:
        """
        Get: NullDisplayText(self: DisplayFormatAttribute) -> str
        Set: NullDisplayText(self: DisplayFormatAttribute) = value
        """
        ...



class EditableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EditableAttribute(allowEdit: bool) """
    @property
    def AllowEdit(self) -> bool:
        """ Get: AllowEdit(self: EditableAttribute) -> bool """
        ...

    @property
    def AllowInitialValue(self) -> bool:
        """
        Get: AllowInitialValue(self: EditableAttribute) -> bool
        Set: AllowInitialValue(self: EditableAttribute) = value
        """
        ...


    def __new__(cls, allowEdit:bool) -> Self:
        """ __new__(cls: type, allowEdit: bool) """
        ...


class EmailAddressAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EmailAddressAttribute() """
    pass

class EnumDataTypeAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EnumDataTypeAttribute(enumType: Type) """
    @property
    def EnumType(self) -> Type:
        """ Get: EnumType(self: EnumDataTypeAttribute) -> Type """
        ...



class FileExtensionsAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FileExtensionsAttribute() """
    @property
    def Extensions(self) -> str:
        """
        Get: Extensions(self: FileExtensionsAttribute) -> str
        Set: Extensions(self: FileExtensionsAttribute) = value
        """
        ...


    def FormatErrorMessage(self, name:str) -> str:
        """ FormatErrorMessage(self: FileExtensionsAttribute, name: str) -> str """
        ...


class FilterUIHintAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    FilterUIHintAttribute(filterUIHint: str)
    FilterUIHintAttribute(filterUIHint: str, presentationLayer: str)
    FilterUIHintAttribute(filterUIHint: str, presentationLayer: str, *controlParameters: Array[object])
    """
    @property
    def ControlParameters(self) -> IDictionary:
        """ Get: ControlParameters(self: FilterUIHintAttribute) -> IDictionary[str, object] """
        ...

    @property
    def FilterUIHint(self) -> str:
        """ Get: FilterUIHint(self: FilterUIHintAttribute) -> str """
        ...

    @property
    def PresentationLayer(self) -> str:
        """ Get: PresentationLayer(self: FilterUIHintAttribute) -> str """
        ...


    def __new__(cls, filterUIHint:str, presentationLayer:str = ..., controlParameters:Array = ...) -> Self:
        """
        __new__(cls: type, filterUIHint: str)
        __new__(cls: type, filterUIHint: str, presentationLayer: str)
        __new__(cls: type, filterUIHint: str, presentationLayer: str, *controlParameters: Array[object])
        """
        ...


class IValidatableObject: # skipped bases: <type 'object'>
    """ no doc """
    def Validate(self, validationContext:ValidationContext) -> IEnumerable:
        """ Validate(self: IValidatableObject, validationContext: ValidationContext) -> IEnumerable[ValidationResult] """
        ...


class KeyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ KeyAttribute() """
    pass

class MaxLengthAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    MaxLengthAttribute(length: int)
    MaxLengthAttribute()
    """
    @property
    def Length(self) -> int:
        """ Get: Length(self: MaxLengthAttribute) -> int """
        ...



class MetadataTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MetadataTypeAttribute(metadataClassType: Type) """
    @property
    def MetadataClassType(self) -> Type:
        """ Get: MetadataClassType(self: MetadataTypeAttribute) -> Type """
        ...


    def __new__(cls, metadataClassType:Type) -> Self:
        """ __new__(cls: type, metadataClassType: Type) """
        ...


class MinLengthAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MinLengthAttribute(length: int) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: MinLengthAttribute) -> int """
        ...



class PhoneAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PhoneAttribute() """
    pass

class RangeAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    RangeAttribute(minimum: int, maximum: int)
    RangeAttribute(minimum: float, maximum: float)
    RangeAttribute(type: Type, minimum: str, maximum: str)
    """
    @property
    def Maximum(self) -> object:
        """ Get: Maximum(self: RangeAttribute) -> object """
        ...

    @property
    def Minimum(self) -> object:
        """ Get: Minimum(self: RangeAttribute) -> object """
        ...

    @property
    def OperandType(self) -> Type:
        """ Get: OperandType(self: RangeAttribute) -> Type """
        ...



class RegularExpressionAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RegularExpressionAttribute(pattern: str) """
    @property
    def MatchTimeoutInMilliseconds(self) -> int:
        """
        Get: MatchTimeoutInMilliseconds(self: RegularExpressionAttribute) -> int
        Set: MatchTimeoutInMilliseconds(self: RegularExpressionAttribute) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """ Get: Pattern(self: RegularExpressionAttribute) -> str """
        ...



class RequiredAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RequiredAttribute() """
    @property
    def AllowEmptyStrings(self) -> bool:
        """
        Get: AllowEmptyStrings(self: RequiredAttribute) -> bool
        Set: AllowEmptyStrings(self: RequiredAttribute) = value
        """
        ...



class ScaffoldColumnAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScaffoldColumnAttribute(scaffold: bool) """
    @property
    def Scaffold(self) -> bool:
        """ Get: Scaffold(self: ScaffoldColumnAttribute) -> bool """
        ...


    def __new__(cls, scaffold:bool) -> Self:
        """ __new__(cls: type, scaffold: bool) """
        ...


class ScaffoldTableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScaffoldTableAttribute(scaffold: bool) """
    @property
    def Scaffold(self) -> bool:
        """ Get: Scaffold(self: ScaffoldTableAttribute) -> bool """
        ...


    def __new__(cls, scaffold:bool) -> Self:
        """ __new__(cls: type, scaffold: bool) """
        ...


class StringLengthAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StringLengthAttribute(maximumLength: int) """
    @property
    def MaximumLength(self) -> int:
        """ Get: MaximumLength(self: StringLengthAttribute) -> int """
        ...

    @property
    def MinimumLength(self) -> int:
        """
        Get: MinimumLength(self: StringLengthAttribute) -> int
        Set: MinimumLength(self: StringLengthAttribute) = value
        """
        ...



class TimestampAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TimestampAttribute() """
    pass

class UIHintAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    UIHintAttribute(uiHint: str)
    UIHintAttribute(uiHint: str, presentationLayer: str)
    UIHintAttribute(uiHint: str, presentationLayer: str, *controlParameters: Array[object])
    """
    @property
    def ControlParameters(self) -> IDictionary:
        """ Get: ControlParameters(self: UIHintAttribute) -> IDictionary[str, object] """
        ...

    @property
    def PresentationLayer(self) -> str:
        """ Get: PresentationLayer(self: UIHintAttribute) -> str """
        ...

    @property
    def UIHint(self) -> str:
        """ Get: UIHint(self: UIHintAttribute) -> str """
        ...


    def __new__(cls, uiHint:str, presentationLayer:str = ..., controlParameters:Array = ...) -> Self:
        """
        __new__(cls: type, uiHint: str)
        __new__(cls: type, uiHint: str, presentationLayer: str)
        __new__(cls: type, uiHint: str, presentationLayer: str, *controlParameters: Array[object])
        """
        ...


class UrlAttribute(DataTypeAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UrlAttribute() """
    pass

class ValidationContext(IServiceProvider): # skipped bases: <type 'object'>
    """
    ValidationContext(instance: object)
    ValidationContext(instance: object, items: dict)
    ValidationContext(instance: object, serviceProvider: IServiceProvider, items: dict)
    """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ValidationContext) -> str
        Set: DisplayName(self: ValidationContext) = value
        """
        ...

    @property
    def Items(self) -> dict:
        """ Get: Items(self: ValidationContext) -> dict """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: ValidationContext) -> str
        Set: MemberName(self: ValidationContext) = value
        """
        ...

    @property
    def ObjectInstance(self) -> object:
        """ Get: ObjectInstance(self: ValidationContext) -> object """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: ValidationContext) -> Type """
        ...

    @property
    def ServiceContainer(self) -> IServiceContainer:
        """ Get: ServiceContainer(self: ValidationContext) -> IServiceContainer """
        ...


    def InitializeServiceProvider(self, serviceProvider): # ->  # Not found arg types: {'serviceProvider': 'Func'}
        """ InitializeServiceProvider(self: ValidationContext, serviceProvider: Func[Type, object]) """
        ...


class ValidationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ValidationException(validationResult: ValidationResult, validatingAttribute: ValidationAttribute, value: object)
    ValidationException(errorMessage: str, validatingAttribute: ValidationAttribute, value: object)
    ValidationException()
    ValidationException(message: str)
    ValidationException(message: str, innerException: Exception)
    """
    @property
    def ValidationAttribute(self) -> ValidationAttribute:
        """ Get: ValidationAttribute(self: ValidationException) -> ValidationAttribute """
        ...

    @property
    def ValidationResult(self) -> ValidationResult:
        """ Get: ValidationResult(self: ValidationException) -> ValidationResult """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: ValidationException) -> object """
        ...


    SerializeObjectState = ...


class ValidationResult: # skipped bases: <type 'object'>, <type 'object'>
    """
    ValidationResult(errorMessage: str)
    ValidationResult(errorMessage: str, memberNames: IEnumerable[str])
    """
    @property
    def ErrorMessage(self) -> str:
        """
        Get: ErrorMessage(self: ValidationResult) -> str
        Set: ErrorMessage(self: ValidationResult) = value
        """
        ...

    @property
    def MemberNames(self) -> IEnumerable:
        """ Get: MemberNames(self: ValidationResult) -> IEnumerable[str] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ValidationResult) -> str """
        ...


class Validator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def TryValidateObject(instance:object, validationContext:ValidationContext, validationResults:ICollection, validateAllProperties:bool = ...) -> bool:
        """
        TryValidateObject(instance: object, validationContext: ValidationContext, validationResults: ICollection[ValidationResult]) -> bool
        TryValidateObject(instance: object, validationContext: ValidationContext, validationResults: ICollection[ValidationResult], validateAllProperties: bool) -> bool
        """
        ...

    @staticmethod
    def TryValidateProperty(value:object, validationContext:ValidationContext, validationResults:ICollection) -> bool:
        """ TryValidateProperty(value: object, validationContext: ValidationContext, validationResults: ICollection[ValidationResult]) -> bool """
        ...

    @staticmethod
    def TryValidateValue(value:object, validationContext:ValidationContext, validationResults:ICollection, validationAttributes:IEnumerable) -> bool:
        """ TryValidateValue(value: object, validationContext: ValidationContext, validationResults: ICollection[ValidationResult], validationAttributes: IEnumerable[ValidationAttribute]) -> bool """
        ...

    @staticmethod
    def ValidateObject(instance:object, validationContext:ValidationContext, validateAllProperties:bool = ...): # -> 
        """ ValidateObject(instance: object, validationContext: ValidationContext)ValidateObject(instance: object, validationContext: ValidationContext, validateAllProperties: bool) """
        ...

    @staticmethod
    def ValidateProperty(value:object, validationContext:ValidationContext): # -> 
        """ ValidateProperty(value: object, validationContext: ValidationContext) """
        ...

    @staticmethod
    def ValidateValue(value:object, validationContext:ValidationContext, validationAttributes:IEnumerable): # -> 
        """ ValidateValue(value: object, validationContext: ValidationContext, validationAttributes: IEnumerable[ValidationAttribute]) """
        ...

    __all__: list = ...


# variables with complex values

