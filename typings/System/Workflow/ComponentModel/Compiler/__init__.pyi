# encoding: utf-8
# module System.Workflow.ComponentModel.Compiler calls itself Compiler
# from System.Workflow.ComponentModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, Attribute, Enum, EventHandler, IDisposable, 
    IServiceProvider, Type)

from System.CodeDom import CodeCompileUnit

from System.CodeDom.Compiler import (CompilerError, CompilerParameters, 
    CompilerResults)

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Collections.Specialized import StringCollection

from System.ComponentModel.Design.Serialization import ContextStack

from System.EnterpriseServices import Activity

from System.Reflection import Assembly, EventInfo, PropertyInfo

from System.Text.RegularExpressions import Regex

from System.Threading.Tasks import Task

from System.Workflow.ComponentModel import ActivityChangeAction

from typing import Self

"""The following names are not found in the module: (BoundEvent, Func, 
    IWorkflowCompilerError, field#)
"""

# no functions
# classes

class AccessTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AccessTypes, values: Read (1), ReadWrite (3), Write (2) """
    Read: AccessTypes = ...
    ReadWrite: AccessTypes = ...
    value__ = ...
    Write: AccessTypes = ...


class ActivityCodeGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ ActivityCodeGenerator() """
    def GenerateCode(self, manager:CodeGenerationManager, obj:object): # -> 
        """ GenerateCode(self: ActivityCodeGenerator, manager: CodeGenerationManager, obj: object) """
        ...

    def GetCodeTypeDeclaration(self, *args): #cannot find CLR method
        """ GetCodeTypeDeclaration(self: ActivityCodeGenerator, manager: CodeGenerationManager, fullClassName: str) -> CodeTypeDeclaration """
        ...


class ActivityCodeGeneratorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ActivityCodeGeneratorAttribute(codeGeneratorType: Type)
    ActivityCodeGeneratorAttribute(codeGeneratorTypeName: str)
    """
    @property
    def CodeGeneratorTypeName(self) -> str:
        """ Get: CodeGeneratorTypeName(self: ActivityCodeGeneratorAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, codeGeneratorType: Type)
        __new__(cls: type, codeGeneratorTypeName: str)
        """
        ...


class Validator: # skipped bases: <type 'object'>, <type 'object'>
    """ Validator() """
    def GetFullPropertyName(self, *args): #cannot find CLR method
        """ GetFullPropertyName(self: Validator, manager: ValidationManager) -> str """
        ...

    def Validate(self, manager:ValidationManager, obj:object) -> ValidationErrorCollection:
        """ Validate(self: Validator, manager: ValidationManager, obj: object) -> ValidationErrorCollection """
        ...

    def ValidateActivityChange(self, activity:Activity, action:ActivityChangeAction) -> ValidationError:
        """ ValidateActivityChange(self: Validator, activity: Activity, action: ActivityChangeAction) -> ValidationError """
        ...

    def ValidateProperties(self, manager:ValidationManager, obj:object) -> ValidationErrorCollection:
        """ ValidateProperties(self: Validator, manager: ValidationManager, obj: object) -> ValidationErrorCollection """
        ...

    def ValidateProperty(self, *args): #cannot find CLR method
        """ ValidateProperty(self: Validator, propertyInfo: PropertyInfo, propertyOwner: object, propertyValue: object, manager: ValidationManager) -> ValidationErrorCollection """
        ...


class DependencyObjectValidator(Validator): # skipped bases: <type 'object'>
    """ DependencyObjectValidator() """
    pass

class ActivityValidator(DependencyObjectValidator): # skipped bases: <type 'object'>
    """ ActivityValidator() """
    pass

class ActivityValidatorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ActivityValidatorAttribute(validatorType: Type)
    ActivityValidatorAttribute(validatorTypeName: str)
    """
    @property
    def ValidatorTypeName(self) -> str:
        """ Get: ValidatorTypeName(self: ActivityValidatorAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, validatorType: Type)
        __new__(cls: type, validatorTypeName: str)
        """
        ...


class AttributeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ArgumentValues(self) -> ReadOnlyCollection:
        """ Get: ArgumentValues(self: AttributeInfo) -> ReadOnlyCollection[object] """
        ...

    @property
    def AttributeType(self) -> Type:
        """ Get: AttributeType(self: AttributeInfo) -> Type """
        ...

    @property
    def Creatable(self) -> bool:
        """ Get: Creatable(self: AttributeInfo) -> bool """
        ...


    def CreateAttribute(self) -> Attribute:
        """ CreateAttribute(self: AttributeInfo) -> Attribute """
        ...

    def GetArgumentValueAs(self, serviceProvider:IServiceProvider, argumentIndex:int, requestedType:Type) -> object:
        """ GetArgumentValueAs(self: AttributeInfo, serviceProvider: IServiceProvider, argumentIndex: int, requestedType: Type) -> object """
        ...


class AttributeInfoAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def AttributeInfo(self) -> AttributeInfo:
        """ Get: AttributeInfo(self: AttributeInfoAttribute) -> AttributeInfo """
        ...



class AuthorizedType: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthorizedType() """
    @property
    def Assembly(self) -> str:
        """
        Get: Assembly(self: AuthorizedType) -> str
        Set: Assembly(self: AuthorizedType) = value
        """
        ...

    @property
    def Authorized(self) -> str:
        """
        Get: Authorized(self: AuthorizedType) -> str
        Set: Authorized(self: AuthorizedType) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: AuthorizedType) -> str
        Set: Namespace(self: AuthorizedType) = value
        """
        ...

    @property
    def RegularExpression(self) -> Regex:
        """ Get: RegularExpression(self: AuthorizedType) -> Regex """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: AuthorizedType) -> str
        Set: TypeName(self: AuthorizedType) = value
        """
        ...



class BindValidationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    BindValidationContext(targetType: Type)
    BindValidationContext(targetType: Type, access: AccessTypes)
    """
    @property
    def Access(self) -> AccessTypes:
        """ Get: Access(self: BindValidationContext) -> AccessTypes """
        ...

    @property
    def TargetType(self) -> Type:
        """ Get: TargetType(self: BindValidationContext) -> Type """
        ...



class CodeGenerationManager(IServiceProvider): # skipped bases: <type 'object'>
    """ CodeGenerationManager(serviceProvider: IServiceProvider) """
    @property
    def Context(self) -> ContextStack:
        """ Get: Context(self: CodeGenerationManager) -> ContextStack """
        ...


    def GetCodeGenerators(self, type:Type) -> Array:
        """ GetCodeGenerators(self: CodeGenerationManager, type: Type) -> Array[ActivityCodeGenerator] """
        ...


class CompileWorkflowCleanupTask(Task): # skipped bases: <type 'ITask'>, <type 'object'>
    """ CompileWorkflowCleanupTask() """
    @property
    def TemporaryFiles(self) -> Array:
        """
        Get: TemporaryFiles(self: CompileWorkflowCleanupTask) -> Array[ITaskItem]
        Set: TemporaryFiles(self: CompileWorkflowCleanupTask) = value
        """
        ...



class CompileWorkflowTask(Task): # skipped bases: <type 'ITask'>, <type 'object'>
    """ CompileWorkflowTask() """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: CompileWorkflowTask) -> str
        Set: AssemblyName(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def BuildingProject(self) -> bool:
        """
        Get: BuildingProject(self: CompileWorkflowTask) -> bool
        Set: BuildingProject(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def CompilationOptions(self) -> Array:
        """
        Get: CompilationOptions(self: CompileWorkflowTask) -> Array[ITaskItem]
        Set: CompilationOptions(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def DelaySign(self) -> bool:
        """
        Get: DelaySign(self: CompileWorkflowTask) -> bool
        Set: DelaySign(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def Imports(self) -> str:
        """
        Get: Imports(self: CompileWorkflowTask) -> str
        Set: Imports(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def KeepTemporaryFiles(self) -> str:
        """ Get: KeepTemporaryFiles(self: CompileWorkflowTask) -> str """
        ...

    @property
    def KeyContainer(self) -> str:
        """
        Get: KeyContainer(self: CompileWorkflowTask) -> str
        Set: KeyContainer(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def KeyFile(self) -> str:
        """
        Get: KeyFile(self: CompileWorkflowTask) -> str
        Set: KeyFile(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def OutputFiles(self) -> Array:
        """ Get: OutputFiles(self: CompileWorkflowTask) -> Array[ITaskItem] """
        ...

    @property
    def ProjectDirectory(self) -> str:
        """
        Get: ProjectDirectory(self: CompileWorkflowTask) -> str
        Set: ProjectDirectory(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def ProjectExtension(self) -> str:
        """
        Get: ProjectExtension(self: CompileWorkflowTask) -> str
        Set: ProjectExtension(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def ReferenceFiles(self) -> Array:
        """
        Get: ReferenceFiles(self: CompileWorkflowTask) -> Array[ITaskItem]
        Set: ReferenceFiles(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def ResourceFiles(self) -> Array:
        """
        Get: ResourceFiles(self: CompileWorkflowTask) -> Array[ITaskItem]
        Set: ResourceFiles(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def RootNamespace(self) -> str:
        """
        Get: RootNamespace(self: CompileWorkflowTask) -> str
        Set: RootNamespace(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def SourceCodeFiles(self) -> Array:
        """
        Get: SourceCodeFiles(self: CompileWorkflowTask) -> Array[ITaskItem]
        Set: SourceCodeFiles(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def TargetFramework(self) -> str:
        """
        Get: TargetFramework(self: CompileWorkflowTask) -> str
        Set: TargetFramework(self: CompileWorkflowTask) = value
        """
        ...

    @property
    def TemporaryFiles(self) -> Array:
        """ Get: TemporaryFiles(self: CompileWorkflowTask) -> Array[str] """
        ...

    @property
    def WorkflowMarkupFiles(self) -> Array:
        """
        Get: WorkflowMarkupFiles(self: CompileWorkflowTask) -> Array[ITaskItem]
        Set: WorkflowMarkupFiles(self: CompileWorkflowTask) = value
        """
        ...



class CompositeActivityCodeGenerator(ActivityCodeGenerator): # skipped bases: <type 'object'>
    """ CompositeActivityCodeGenerator() """
    pass

class CompositeActivityValidator(ActivityValidator): # skipped bases: <type 'object'>
    """ CompositeActivityValidator() """
    def ValidateActivityChange(self, activity:Activity, action:ActivityChangeAction) -> ValidationError:
        """ ValidateActivityChange(self: CompositeActivityValidator, activity: Activity, action: ActivityChangeAction) -> ValidationError """
        ...


class ConditionValidator(DependencyObjectValidator): # skipped bases: <type 'object'>
    """ ConditionValidator() """
    pass

class ITypeProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocalAssembly(self) -> Assembly:
        """ Get: LocalAssembly(self: ITypeProvider) -> Assembly """
        ...

    @property
    def ReferencedAssemblies(self) -> ICollection:
        """ Get: ReferencedAssemblies(self: ITypeProvider) -> ICollection[Assembly] """
        ...

    @property
    def TypeLoadErrors(self) -> IDictionary:
        """ Get: TypeLoadErrors(self: ITypeProvider) -> IDictionary[object, Exception] """
        ...


    def GetType(self, name:str, throwOnError:bool = ...) -> Type:
        """
        GetType(self: ITypeProvider, name: str) -> Type
        GetType(self: ITypeProvider, name: str, throwOnError: bool) -> Type
        """
        ...

    def GetTypes(self) -> Array:
        """ GetTypes(self: ITypeProvider) -> Array[Type] """
        ...

    TypeLoadErrorsChanged = ...
    TypesChanged = ...


class IWorkflowCompilerOptionsService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CheckTypes(self) -> bool:
        """ Get: CheckTypes(self: IWorkflowCompilerOptionsService) -> bool """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: IWorkflowCompilerOptionsService) -> str """
        ...

    @property
    def RootNamespace(self) -> str:
        """ Get: RootNamespace(self: IWorkflowCompilerOptionsService) -> str """
        ...



class PropertyValidationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    PropertyValidationContext(propertyOwner: object, propertyInfo: PropertyInfo, propertyName: str)
    PropertyValidationContext(propertyOwner: object, dependencyProperty: DependencyProperty)
    """
    @property
    def Property(self) -> object:
        """ Get: Property(self: PropertyValidationContext) -> object """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PropertyValidationContext) -> str """
        ...

    @property
    def PropertyOwner(self) -> object:
        """ Get: PropertyOwner(self: PropertyValidationContext) -> object """
        ...



class TypeProvider(IServiceProvider, IDisposable, ITypeProvider): # skipped bases: <type 'object'>
    """ TypeProvider(serviceProvider: IServiceProvider) """
    @property
    def AssemblyNameResolver(self): # -> Func
        """
        Get: AssemblyNameResolver(self: TypeProvider) -> Func[Type, str]
        Set: AssemblyNameResolver(self: TypeProvider) = value
        """
        ...

    @property
    def IsSupportedPropertyResolver(self): # -> Func
        """
        Get: IsSupportedPropertyResolver(self: TypeProvider) -> Func[PropertyInfo, object, bool]
        Set: IsSupportedPropertyResolver(self: TypeProvider) = value
        """
        ...


    def AddAssembly(self, assembly:Assembly): # -> 
        """ AddAssembly(self: TypeProvider, assembly: Assembly) """
        ...

    def AddAssemblyReference(self, path:str): # -> 
        """ AddAssemblyReference(self: TypeProvider, path: str) """
        ...

    def AddCodeCompileUnit(self, codeCompileUnit:CodeCompileUnit): # -> 
        """ AddCodeCompileUnit(self: TypeProvider, codeCompileUnit: CodeCompileUnit) """
        ...

    def GetAssemblyName(self, type:Type) -> str:
        """ GetAssemblyName(self: TypeProvider, type: Type) -> str """
        ...

    @staticmethod
    def GetEnumNames(enumType:Type) -> Array:
        """ GetEnumNames(enumType: Type) -> Array[str] """
        ...

    @staticmethod
    def GetEventHandlerType(eventInfo:EventInfo) -> Type:
        """ GetEventHandlerType(eventInfo: EventInfo) -> Type """
        ...

    @staticmethod
    def IsAssignable(toType:Type, fromType:Type) -> bool:
        """ IsAssignable(toType: Type, fromType: Type) -> bool """
        ...

    @staticmethod
    def IsEnum(type:Type) -> bool:
        """ IsEnum(type: Type) -> bool """
        ...

    @staticmethod
    def IsSubclassOf(subclass:Type, superClass:Type) -> bool:
        """ IsSubclassOf(subclass: Type, superClass: Type) -> bool """
        ...

    def IsSupportedProperty(self, property:PropertyInfo, declaringInstance:object) -> bool:
        """ IsSupportedProperty(self: TypeProvider, property: PropertyInfo, declaringInstance: object) -> bool """
        ...

    def RefreshCodeCompileUnit(self, codeCompileUnit:CodeCompileUnit, refresher:EventHandler): # -> 
        """ RefreshCodeCompileUnit(self: TypeProvider, codeCompileUnit: CodeCompileUnit, refresher: EventHandler) """
        ...

    def RemoveAssembly(self, assembly:Assembly): # -> 
        """ RemoveAssembly(self: TypeProvider, assembly: Assembly) """
        ...

    def RemoveAssemblyReference(self, path:str): # -> 
        """ RemoveAssemblyReference(self: TypeProvider, path: str) """
        ...

    def RemoveCodeCompileUnit(self, codeCompileUnit:CodeCompileUnit): # -> 
        """ RemoveCodeCompileUnit(self: TypeProvider, codeCompileUnit: CodeCompileUnit) """
        ...

    def SetLocalAssembly(self, assembly:Assembly): # -> 
        """ SetLocalAssembly(self: TypeProvider, assembly: Assembly) """
        ...

    TypeLoadErrorsChanged = ...
    TypesChanged = ...


class ValidationError: # skipped bases: <type 'object'>, <type 'object'>
    """
    ValidationError(errorText: str, errorNumber: int)
    ValidationError(errorText: str, errorNumber: int, isWarning: bool)
    ValidationError(errorText: str, errorNumber: int, isWarning: bool, propertyName: str)
    """
    @property
    def ErrorNumber(self) -> int:
        """ Get: ErrorNumber(self: ValidationError) -> int """
        ...

    @property
    def ErrorText(self) -> str:
        """ Get: ErrorText(self: ValidationError) -> str """
        ...

    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: ValidationError) -> bool """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ValidationError) -> str
        Set: PropertyName(self: ValidationError) = value
        """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: ValidationError) -> IDictionary """
        ...


    @staticmethod
    def GetNotSetValidationError(propertyName:str) -> ValidationError:
        """ GetNotSetValidationError(propertyName: str) -> ValidationError """
        ...

    def ToString(self) -> str:
        """ ToString(self: ValidationError) -> str """
        ...


class ValidationErrorCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[ValidationError]'>, <type 'ICollection[ValidationError]'>, <type 'IEnumerable'>, <type 'IEnumerable[ValidationError]'>, <type 'IList'>, <type 'IReadOnlyList[ValidationError]'>, <type 'IList[ValidationError]'>, <type 'ICollection'>, <type 'object'>
    """
    ValidationErrorCollection()
    ValidationErrorCollection(value: ValidationErrorCollection)
    ValidationErrorCollection(value: IEnumerable[ValidationError])
    """
    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: ValidationErrorCollection) -> bool """
        ...

    @property
    def HasWarnings(self) -> bool:
        """ Get: HasWarnings(self: ValidationErrorCollection) -> bool """
        ...


    def AddRange(self, value:IEnumerable): # -> 
        """ AddRange(self: ValidationErrorCollection, value: IEnumerable[ValidationError]) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ValidationErrorCollection) -> Array[ValidationError] """
        ...


class ValidationManager(IServiceProvider): # skipped bases: <type 'object'>
    """
    ValidationManager(serviceProvider: IServiceProvider)
    ValidationManager(serviceProvider: IServiceProvider, validateChildActivities: bool)
    """
    @property
    def Context(self) -> ContextStack:
        """ Get: Context(self: ValidationManager) -> ContextStack """
        ...

    @property
    def ValidateChildActivities(self) -> bool:
        """ Get: ValidateChildActivities(self: ValidationManager) -> bool """
        ...


    def GetValidators(self, type:Type) -> Array:
        """ GetValidators(self: ValidationManager, type: Type) -> Array[Validator] """
        ...


class ValidationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidationOption, values: None (0), Optional (1), Required (2) """
    Optional: ValidationOption = ...
    Required: ValidationOption = ...
    value__ = ...


class ValidationOptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidationOptionAttribute(validationOption: ValidationOption) """
    @property
    def ValidationOption(self) -> ValidationOption:
        """ Get: ValidationOption(self: ValidationOptionAttribute) -> ValidationOption """
        ...


    def __new__(cls, validationOption:ValidationOption) -> Self:
        """ __new__(cls: type, validationOption: ValidationOption) """
        ...


class WorkflowCompilationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CheckTypes(self) -> bool:
        """ Get: CheckTypes(self: WorkflowCompilationContext) -> bool """
        ...

    @property
    def Current(self) -> WorkflowCompilationContext:
        """ Get: Current() -> WorkflowCompilationContext """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: WorkflowCompilationContext) -> str """
        ...

    @property
    def RootNamespace(self) -> str:
        """ Get: RootNamespace(self: WorkflowCompilationContext) -> str """
        ...


    @staticmethod
    def CreateScope(serviceProvider:IServiceProvider) -> IDisposable:
        """ CreateScope(serviceProvider: IServiceProvider) -> IDisposable """
        ...

    def GetAuthorizedTypes(self) -> IList:
        """ GetAuthorizedTypes(self: WorkflowCompilationContext) -> IList[AuthorizedType] """
        ...


class WorkflowCompiler: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowCompiler() """
    def Compile(self, parameters:WorkflowCompilerParameters, files:Array) -> WorkflowCompilerResults:
        """ Compile(self: WorkflowCompiler, parameters: WorkflowCompilerParameters, *files: Array[str]) -> WorkflowCompilerResults """
        ...


class WorkflowCompilerError(IWorkflowCompilerError, CompilerError): # skipped bases: <type 'object'>
    """
    WorkflowCompilerError()
    WorkflowCompilerError(fileName: str, line: int, column: int, errorNumber: str, errorText: str)
    WorkflowCompilerError(fileName: str, exception: WorkflowMarkupSerializationException)
    """
    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: WorkflowCompilerError) -> str
        Set: PropertyName(self: WorkflowCompilerError) = value
        """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: WorkflowCompilerError) -> IDictionary """
        ...



class WorkflowCompilerOptionsService(IWorkflowCompilerOptionsService): # skipped bases: <type 'object'>
    """ WorkflowCompilerOptionsService() """
    @property
    def TargetFrameworkMoniker(self) -> str:
        """ Get: TargetFrameworkMoniker(self: WorkflowCompilerOptionsService) -> str """
        ...



class WorkflowCompilerParameters(CompilerParameters): # skipped bases: <type 'object'>
    """
    WorkflowCompilerParameters()
    WorkflowCompilerParameters(assemblyNames: Array[str])
    WorkflowCompilerParameters(assemblyNames: Array[str], outputName: str)
    WorkflowCompilerParameters(assemblyNames: Array[str], outputName: str, includeDebugInformation: bool)
    WorkflowCompilerParameters(parameters: WorkflowCompilerParameters)
    """
    @property
    def GenerateCodeCompileUnitOnly(self) -> bool:
        """
        Get: GenerateCodeCompileUnitOnly(self: WorkflowCompilerParameters) -> bool
        Set: GenerateCodeCompileUnitOnly(self: WorkflowCompilerParameters) = value
        """
        ...

    @property
    def LanguageToUse(self) -> str:
        """
        Get: LanguageToUse(self: WorkflowCompilerParameters) -> str
        Set: LanguageToUse(self: WorkflowCompilerParameters) = value
        """
        ...

    @property
    def LibraryPaths(self) -> StringCollection:
        """ Get: LibraryPaths(self: WorkflowCompilerParameters) -> StringCollection """
        ...

    @property
    def UserCodeCompileUnits(self) -> IList:
        """ Get: UserCodeCompileUnits(self: WorkflowCompilerParameters) -> IList[CodeCompileUnit] """
        ...



class WorkflowCompilerResults(CompilerResults): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CompiledUnit(self) -> CodeCompileUnit:
        """ Get: CompiledUnit(self: WorkflowCompilerResults) -> CodeCompileUnit """
        ...



class WorkflowMarkupSourceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WorkflowMarkupSourceAttribute(fileName: str, md5Digest: str) """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: WorkflowMarkupSourceAttribute) -> str """
        ...

    @property
    def MD5Digest(self) -> str:
        """ Get: MD5Digest(self: WorkflowMarkupSourceAttribute) -> str """
        ...


    def __new__(cls, fileName:str, md5Digest:str) -> Self:
        """ __new__(cls: type, fileName: str, md5Digest: str) """
        ...


class WorkflowValidationFailedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowValidationFailedException()
    WorkflowValidationFailedException(message: str)
    WorkflowValidationFailedException(message: str, innerException: Exception)
    WorkflowValidationFailedException(message: str, errors: ValidationErrorCollection)
    """
    @property
    def Errors(self) -> ValidationErrorCollection:
        """ Get: Errors(self: WorkflowValidationFailedException) -> ValidationErrorCollection """
        ...


    SerializeObjectState = ...


