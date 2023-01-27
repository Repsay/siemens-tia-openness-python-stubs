# encoding: utf-8
# module System.Activities.Validation calls itself Validation
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Activities import (CodeActivity, InArgument, 
    LocationReferenceEnvironment, NativeActivity, NativeActivityContext)

from System.Collections import IDictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.EnterpriseServices import Activity

from System.Threading import CancellationToken


# no functions
# classes

class ActivityValidationServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Resolve(root:Activity, id:str) -> Activity:
        """ Resolve(root: Activity, id: str) -> Activity """
        ...

    @staticmethod
    def Validate(toValidate:Activity, settings:ValidationSettings = ...) -> ValidationResults:
        """
        Validate(toValidate: Activity) -> ValidationResults
        Validate(toValidate: Activity, settings: ValidationSettings) -> ValidationResults
        """
        ...

    __all__: list = ...


class AddValidationError(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ AddValidationError() """
    @property
    def IsWarning(self) -> InArgument:
        """
        Get: IsWarning(self: AddValidationError) -> InArgument[bool]
        Set: IsWarning(self: AddValidationError) = value
        """
        ...

    @property
    def Message(self) -> InArgument:
        """
        Get: Message(self: AddValidationError) -> InArgument[str]
        Set: Message(self: AddValidationError) = value
        """
        ...

    @property
    def PropertyName(self) -> InArgument:
        """
        Get: PropertyName(self: AddValidationError) -> InArgument[str]
        Set: PropertyName(self: AddValidationError) = value
        """
        ...



class AssertValidation(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ AssertValidation() """
    @property
    def Assertion(self) -> InArgument:
        """
        Get: Assertion(self: AssertValidation) -> InArgument[bool]
        Set: Assertion(self: AssertValidation) = value
        """
        ...

    @property
    def IsWarning(self) -> InArgument:
        """
        Get: IsWarning(self: AssertValidation) -> InArgument[bool]
        Set: IsWarning(self: AssertValidation) = value
        """
        ...

    @property
    def Message(self) -> InArgument:
        """
        Get: Message(self: AssertValidation) -> InArgument[str]
        Set: Message(self: AssertValidation) = value
        """
        ...

    @property
    def PropertyName(self) -> InArgument:
        """
        Get: PropertyName(self: AssertValidation) -> InArgument[str]
        Set: PropertyName(self: AssertValidation) = value
        """
        ...



class Constraint: # skipped bases: <type 'object'>
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

    @staticmethod
    def AddValidationError(context:NativeActivityContext, error:ValidationError): # -> 
        """ AddValidationError(context: NativeActivityContext, error: ValidationError) """
        ...

    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: Constraint, metadata: NativeActivityMetadata)CacheMetadata(self: NativeActivity, metadata: ActivityMetadata) """
        ...

    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: NativeActivity, context: NativeActivityContext) """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: Constraint, context: NativeActivityContext) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: NativeActivity, metadata: UpdateMapMetadata, originalActivity: Activity)OnCreateDynamicUpdateMap(self: NativeActivity, metadata: NativeActivityUpdateMapMetadata, originalActivity: Activity) """
        ...

    def OnExecute(self, *args): #cannot find CLR method
        """ OnExecute(self: Constraint, context: NativeActivityContext, objectToValidate: object, objectToValidateContext: ValidationContext) """
        ...

    def UpdateInstance(self, *args): #cannot find CLR method
        """ UpdateInstance(self: NativeActivity, updateContext: NativeActivityUpdateContext) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    ValidationErrorListPropertyName: str = ...


class GetChildSubtree(CodeActivity): # skipped bases: <type 'object'>
    """ GetChildSubtree() """
    @property
    def ValidationContext(self) -> InArgument:
        """
        Get: ValidationContext(self: GetChildSubtree) -> InArgument[ValidationContext]
        Set: ValidationContext(self: GetChildSubtree) = value
        """
        ...



class GetParentChain(CodeActivity): # skipped bases: <type 'object'>
    """ GetParentChain() """
    @property
    def ValidationContext(self) -> InArgument:
        """
        Get: ValidationContext(self: GetParentChain) -> InArgument[ValidationContext]
        Set: ValidationContext(self: GetParentChain) = value
        """
        ...



class GetWorkflowTree(CodeActivity): # skipped bases: <type 'object'>
    """ GetWorkflowTree() """
    @property
    def ValidationContext(self) -> InArgument:
        """
        Get: ValidationContext(self: GetWorkflowTree) -> InArgument[ValidationContext]
        Set: ValidationContext(self: GetWorkflowTree) = value
        """
        ...



class ValidationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class ValidationError: # skipped bases: <type 'object'>, <type 'object'>
    """
    ValidationError(message: str)
    ValidationError(message: str, isWarning: bool)
    ValidationError(message: str, isWarning: bool, propertyName: str)
    ValidationError(message: str, isWarning: bool, propertyName: str, sourceDetail: object)
    """
    @property
    def Id(self) -> str:
        """ Get: Id(self: ValidationError) -> str """
        ...

    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: ValidationError) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ValidationError) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ValidationError) -> str """
        ...

    @property
    def Source(self) -> Activity:
        """ Get: Source(self: ValidationError) -> Activity """
        ...

    @property
    def SourceDetail(self) -> object:
        """ Get: SourceDetail(self: ValidationError) -> object """
        ...


    def ToString(self) -> str:
        """ ToString(self: ValidationError) -> str """
        ...


class ValidationResults: # skipped bases: <type 'object'>, <type 'object'>
    """ ValidationResults(allValidationErrors: IList[ValidationError]) """
    @property
    def Errors(self) -> ReadOnlyCollection:
        """ Get: Errors(self: ValidationResults) -> ReadOnlyCollection[ValidationError] """
        ...

    @property
    def Warnings(self) -> ReadOnlyCollection:
        """ Get: Warnings(self: ValidationResults) -> ReadOnlyCollection[ValidationError] """
        ...



class ValidationSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ ValidationSettings() """
    @property
    def AdditionalConstraints(self) -> IDictionary:
        """ Get: AdditionalConstraints(self: ValidationSettings) -> IDictionary[Type, IList[Constraint]] """
        ...

    @property
    def CancellationToken(self) -> CancellationToken:
        """
        Get: CancellationToken(self: ValidationSettings) -> CancellationToken
        Set: CancellationToken(self: ValidationSettings) = value
        """
        ...

    @property
    def Environment(self) -> LocationReferenceEnvironment:
        """
        Get: Environment(self: ValidationSettings) -> LocationReferenceEnvironment
        Set: Environment(self: ValidationSettings) = value
        """
        ...

    @property
    def OnlyUseAdditionalConstraints(self) -> bool:
        """
        Get: OnlyUseAdditionalConstraints(self: ValidationSettings) -> bool
        Set: OnlyUseAdditionalConstraints(self: ValidationSettings) = value
        """
        ...

    @property
    def PrepareForRuntime(self) -> bool:
        """
        Get: PrepareForRuntime(self: ValidationSettings) -> bool
        Set: PrepareForRuntime(self: ValidationSettings) = value
        """
        ...

    @property
    def SingleLevel(self) -> bool:
        """
        Get: SingleLevel(self: ValidationSettings) -> bool
        Set: SingleLevel(self: ValidationSettings) = value
        """
        ...

    @property
    def SkipValidatingRootConfiguration(self) -> bool:
        """
        Get: SkipValidatingRootConfiguration(self: ValidationSettings) -> bool
        Set: SkipValidatingRootConfiguration(self: ValidationSettings) = value
        """
        ...



