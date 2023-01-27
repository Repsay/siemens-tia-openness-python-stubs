# encoding: utf-8
# module System.Web.Compilation calls itself Compilation
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, IDisposable, IServiceProvider, MarshalByRefObject, 
    MulticastDelegate, Nullable, Type)

from System.CodeDom import (CodeCompileUnit, CodeExpression, CodeMemberMethod, 
    CodeTypeDeclaration)

from System.CodeDom.Compiler import (CodeDomProvider, CompilerError, 
    CompilerParameters, CompilerResults)

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Collections.Generic import List

from System.ComponentModel import TypeDescriptionProvider

from System.Globalization import CultureInfo

from System.IO import Stream, TextWriter

from System.Reflection import Assembly

from System.Reflection.Emit import AssemblyBuilder

from System.Resources import IResourceReader

from System.Runtime.Versioning import FrameworkName

from System.Web import ApplicationShutdownReason, HttpContext, ParserError

from System.Web.Routing import RouteValueDictionary

from System.Web.UI import (BoundPropertyEntry, Control, ControlBuilder, Page, 
    TemplateControl, TemplateParser)

from System.Web.Util import IWebObjectFactory

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    BuildProvider, BuildProviderResultFlags, ClientBuildManagerCallback, 
    ClientBuildManagerParameter, CompilerType, ExpressionBuilderContext, 
    IRegisteredObject, ImplicitResourceKey, PrecompilationFlags, field#)
"""

# no functions
# classes

class ExpressionBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SupportsEvaluate(self) -> bool:
        """ Get: SupportsEvaluate(self: ExpressionBuilder) -> bool """
        ...


    def EvaluateExpression(self, target:object, entry:BoundPropertyEntry, parsedData:object, context) -> object: # Not found arg types: {'context': 'ExpressionBuilderContext'}
        """ EvaluateExpression(self: ExpressionBuilder, target: object, entry: BoundPropertyEntry, parsedData: object, context: ExpressionBuilderContext) -> object """
        ...

    def GetCodeExpression(self, entry:BoundPropertyEntry, parsedData:object, context) -> CodeExpression: # Not found arg types: {'context': 'ExpressionBuilderContext'}
        """ GetCodeExpression(self: ExpressionBuilder, entry: BoundPropertyEntry, parsedData: object, context: ExpressionBuilderContext) -> CodeExpression """
        ...

    def ParseExpression(self, expression:str, propertyType:Type, context) -> object: # Not found arg types: {'context': 'ExpressionBuilderContext'}
        """ ParseExpression(self: ExpressionBuilder, expression: str, propertyType: Type, context: ExpressionBuilderContext) -> object """
        ...


class AppSettingsExpressionBuilder(ExpressionBuilder): # skipped bases: <type 'object'>
    """ AppSettingsExpressionBuilder() """
    @staticmethod
    def GetAppSetting(key:str, targetType:Type = ..., propertyName:str = ...) -> object:
        """
        GetAppSetting(key: str) -> object
        GetAppSetting(key: str, targetType: Type, propertyName: str) -> object
        """
        ...


class AssemblyBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CodeDomProvider(self) -> CodeDomProvider:
        """ Get: CodeDomProvider(self: AssemblyBuilder) -> CodeDomProvider """
        ...


    def AddAssemblyReference(self, a:Assembly): # -> 
        """ AddAssemblyReference(self: AssemblyBuilder, a: Assembly) """
        ...

    def AddCodeCompileUnit(self, buildProvider, compileUnit:CodeCompileUnit): # ->  # Not found arg types: {'buildProvider': 'BuildProvider'}
        """ AddCodeCompileUnit(self: AssemblyBuilder, buildProvider: BuildProvider, compileUnit: CodeCompileUnit) """
        ...

    def CreateCodeFile(self, buildProvider) -> TextWriter: # Not found arg types: {'buildProvider': 'BuildProvider'}
        """ CreateCodeFile(self: AssemblyBuilder, buildProvider: BuildProvider) -> TextWriter """
        ...

    def CreateEmbeddedResource(self, buildProvider, name:str) -> Stream: # Not found arg types: {'buildProvider': 'BuildProvider'}
        """ CreateEmbeddedResource(self: AssemblyBuilder, buildProvider: BuildProvider, name: str) -> Stream """
        ...

    def GenerateTypeFactory(self, typeName:str): # -> 
        """ GenerateTypeFactory(self: AssemblyBuilder, typeName: str) """
        ...

    def GetTempFilePhysicalPath(self, extension:str) -> str:
        """ GetTempFilePhysicalPath(self: AssemblyBuilder, extension: str) -> str """
        ...


class BuildDependencySet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HashCode(self) -> str:
        """ Get: HashCode(self: BuildDependencySet) -> str """
        ...

    @property
    def VirtualPaths(self) -> IEnumerable:
        """ Get: VirtualPaths(self: BuildDependencySet) -> IEnumerable """
        ...



class BuildManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BatchCompilationEnabled(self) -> Nullable:
        """
        Get: BatchCompilationEnabled() -> Nullable[bool]
        Set: BatchCompilationEnabled() = value
        """
        ...

    @property
    def CodeAssemblies(self) -> IList:
        """ Get: CodeAssemblies() -> IList """
        ...

    @property
    def IsPrecompiledApp(self) -> bool:
        """ Get: IsPrecompiledApp() -> bool """
        ...

    @property
    def IsUpdatablePrecompiledApp(self) -> bool:
        """ Get: IsUpdatablePrecompiledApp() -> bool """
        ...

    @property
    def TargetFramework(self) -> FrameworkName:
        """ Get: TargetFramework() -> FrameworkName """
        ...


    @staticmethod
    def AddCompilationDependency(dependency:str): # -> 
        """ AddCompilationDependency(dependency: str) """
        ...

    @staticmethod
    def AddReferencedAssembly(assembly:Assembly): # -> 
        """ AddReferencedAssembly(assembly: Assembly) """
        ...

    @staticmethod
    def CreateCachedFile(fileName:str) -> Stream:
        """ CreateCachedFile(fileName: str) -> Stream """
        ...

    @staticmethod
    def CreateInstanceFromVirtualPath(virtualPath:str, requiredBaseType:Type) -> object:
        """ CreateInstanceFromVirtualPath(virtualPath: str, requiredBaseType: Type) -> object """
        ...

    @staticmethod
    def GetCachedBuildDependencySet(context:HttpContext, virtualPath:str, ensureIsUpToDate:bool = ...) -> BuildDependencySet:
        """
        GetCachedBuildDependencySet(context: HttpContext, virtualPath: str) -> BuildDependencySet
        GetCachedBuildDependencySet(context: HttpContext, virtualPath: str, ensureIsUpToDate: bool) -> BuildDependencySet
        """
        ...

    @staticmethod
    def GetCompiledAssembly(virtualPath:str) -> Assembly:
        """ GetCompiledAssembly(virtualPath: str) -> Assembly """
        ...

    @staticmethod
    def GetCompiledCustomString(virtualPath:str) -> str:
        """ GetCompiledCustomString(virtualPath: str) -> str """
        ...

    @staticmethod
    def GetCompiledType(virtualPath:str) -> Type:
        """ GetCompiledType(virtualPath: str) -> Type """
        ...

    @staticmethod
    def GetGlobalAsaxType() -> Type:
        """ GetGlobalAsaxType() -> Type """
        ...

    @staticmethod
    def GetObjectFactory(virtualPath:str, throwIfNotFound:bool) -> IWebObjectFactory:
        """ GetObjectFactory(virtualPath: str, throwIfNotFound: bool) -> IWebObjectFactory """
        ...

    @staticmethod
    def GetReferencedAssemblies() -> ICollection:
        """ GetReferencedAssemblies() -> ICollection """
        ...

    @staticmethod
    def GetType(typeName:str = ..., throwOnError:bool = ..., ignoreCase:bool = ...) -> Type:
        """
        GetType(typeName: str, throwOnError: bool) -> Type
        GetType(typeName: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        ...

    @staticmethod
    def GetVirtualPathDependencies(virtualPath:str) -> ICollection:
        """ GetVirtualPathDependencies(virtualPath: str) -> ICollection """
        ...

    @staticmethod
    def ReadCachedFile(fileName:str) -> Stream:
        """ ReadCachedFile(fileName: str) -> Stream """
        ...



class BuildManagerHostUnloadEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ BuildManagerHostUnloadEventArgs(reason: ApplicationShutdownReason) """
    @property
    def Reason(self) -> ApplicationShutdownReason:
        """ Get: Reason(self: BuildManagerHostUnloadEventArgs) -> ApplicationShutdownReason """
        ...


    def __new__(cls, reason:ApplicationShutdownReason) -> Self:
        """ __new__(cls: type, reason: ApplicationShutdownReason) """
        ...


class BuildManagerHostUnloadEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BuildManagerHostUnloadEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:BuildManagerHostUnloadEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BuildManagerHostUnloadEventHandler, sender: object, e: BuildManagerHostUnloadEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: BuildManagerHostUnloadEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:BuildManagerHostUnloadEventArgs): # -> 
        """ Invoke(self: BuildManagerHostUnloadEventHandler, sender: object, e: BuildManagerHostUnloadEventArgs) """
        ...


class BuildProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CodeCompilerType(self): # -> CompilerType
        """ Get: CodeCompilerType(self: BuildProvider) -> CompilerType """
        ...

    @property
    def ReferencedAssemblies(self):
        ...

    @property
    def VirtualPath(self):
        ...

    @property
    def VirtualPathDependencies(self) -> ICollection:
        """ Get: VirtualPathDependencies(self: BuildProvider) -> ICollection """
        ...


    def GenerateCode(self, assemblyBuilder:AssemblyBuilder): # -> 
        """ GenerateCode(self: BuildProvider, assemblyBuilder: AssemblyBuilder) """
        ...

    def GetCodeCompileUnit(self, *args): #cannot find CLR method
        """ GetCodeCompileUnit(self: BuildProvider) -> (CodeCompileUnit, IDictionary) """
        ...

    def GetCustomString(self, results:CompilerResults) -> str:
        """ GetCustomString(self: BuildProvider, results: CompilerResults) -> str """
        ...

    def GetDefaultCompilerType(self, *args): #cannot find CLR method
        """ GetDefaultCompilerType(self: BuildProvider) -> CompilerType """
        ...

    def GetDefaultCompilerTypeForLanguage(self, *args): #cannot find CLR method
        """ GetDefaultCompilerTypeForLanguage(self: BuildProvider, language: str) -> CompilerType """
        ...

    def GetGeneratedType(self, results:CompilerResults) -> Type:
        """ GetGeneratedType(self: BuildProvider, results: CompilerResults) -> Type """
        ...

    def GetResultFlags(self, results:CompilerResults): # -> BuildProviderResultFlags
        """ GetResultFlags(self: BuildProvider, results: CompilerResults) -> BuildProviderResultFlags """
        ...

    def OpenReader(self, *args): #cannot find CLR method
        """
        OpenReader(self: BuildProvider) -> TextReader
        OpenReader(self: BuildProvider, virtualPath: str) -> TextReader
        """
        ...

    def OpenStream(self, *args): #cannot find CLR method
        """
        OpenStream(self: BuildProvider) -> Stream
        OpenStream(self: BuildProvider, virtualPath: str) -> Stream
        """
        ...

    def ProcessCompileErrors(self, results:CompilerResults): # -> 
        """ ProcessCompileErrors(self: BuildProvider, results: CompilerResults) """
        ...

    @staticmethod
    def RegisterBuildProvider(extension:str, providerType:Type): # -> 
        """ RegisterBuildProvider(extension: str, providerType: Type) """
        ...


class BuildProviderAppliesTo(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) BuildProviderAppliesTo, values: All (7), Code (2), Resources (4), Web (1) """
    All: BuildProviderAppliesTo = ...
    Code: BuildProviderAppliesTo = ...
    Resources: BuildProviderAppliesTo = ...
    value__ = ...
    Web: BuildProviderAppliesTo = ...


class BuildProviderAppliesToAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BuildProviderAppliesToAttribute(appliesTo: BuildProviderAppliesTo) """
    @property
    def AppliesTo(self) -> BuildProviderAppliesTo:
        """ Get: AppliesTo(self: BuildProviderAppliesToAttribute) -> BuildProviderAppliesTo """
        ...


    def __new__(cls, appliesTo:BuildProviderAppliesTo) -> Self:
        """ __new__(cls: type, appliesTo: BuildProviderAppliesTo) """
        ...


class BuildProviderResultFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) BuildProviderResultFlags, values: Default (0), ShutdownAppDomainOnChange (1) """
    Default: BuildProviderResultFlags = ...
    ShutdownAppDomainOnChange: BuildProviderResultFlags = ...
    value__ = ...


class ClientBuildManager(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    ClientBuildManager(appVirtualDir: str, appPhysicalSourceDir: str)
    ClientBuildManager(appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str)
    ClientBuildManager(appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str, parameter: ClientBuildManagerParameter)
    ClientBuildManager(appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str, parameter: ClientBuildManagerParameter, typeDescriptionProvider: TypeDescriptionProvider)
    """
    @property
    def CodeGenDir(self) -> str:
        """ Get: CodeGenDir(self: ClientBuildManager) -> str """
        ...

    @property
    def IsHostCreated(self) -> bool:
        """ Get: IsHostCreated(self: ClientBuildManager) -> bool """
        ...


    def CompileApplicationDependencies(self): # -> 
        """ CompileApplicationDependencies(self: ClientBuildManager) """
        ...

    def CompileFile(self, virtualPath:str, callback = ...): # ->  # Not found arg types: {'callback': 'ClientBuildManagerCallback'}
        """ CompileFile(self: ClientBuildManager, virtualPath: str)CompileFile(self: ClientBuildManager, virtualPath: str, callback: ClientBuildManagerCallback) """
        ...

    def CreateObject(self, type:Type, failIfExists:bool): # -> IRegisteredObject
        """ CreateObject(self: ClientBuildManager, type: Type, failIfExists: bool) -> IRegisteredObject """
        ...

    def GenerateCode(self, virtualPath, virtualFileString, linePragmasTable) -> Tuple_[str, IDictionary]:
        """ GenerateCode(self: ClientBuildManager, virtualPath: str, virtualFileString: str) -> (str, IDictionary) """
        ...

    def GenerateCodeCompileUnit(self, virtualPath:str, *__args:str) -> Tuple_[CodeCompileUnit, Type, CompilerParameters, IDictionary]:
        """
        GenerateCodeCompileUnit(self: ClientBuildManager, virtualPath: str) -> (CodeCompileUnit, Type, CompilerParameters, IDictionary)
        GenerateCodeCompileUnit(self: ClientBuildManager, virtualPath: str, virtualFileString: str) -> (CodeCompileUnit, Type, CompilerParameters, IDictionary)
        """
        ...

    def GetAppDomainShutdownDirectories(self) -> Array:
        """ GetAppDomainShutdownDirectories(self: ClientBuildManager) -> Array[str] """
        ...

    def GetBrowserDefinitions(self) -> IDictionary:
        """ GetBrowserDefinitions(self: ClientBuildManager) -> IDictionary """
        ...

    def GetCodeDirectoryInformation(self, virtualCodeDir, codeDomProviderType, compilerParameters, generatedFilesDir) -> Tuple_[Type, CompilerParameters, str]:
        """ GetCodeDirectoryInformation(self: ClientBuildManager, virtualCodeDir: str) -> (Type, CompilerParameters, str) """
        ...

    def GetCompiledType(self, virtualPath:str) -> Type:
        """ GetCompiledType(self: ClientBuildManager, virtualPath: str) -> Type """
        ...

    def GetCompilerParameters(self, virtualPath, codeDomProviderType, compilerParameters) -> Tuple_[Type, CompilerParameters]:
        """ GetCompilerParameters(self: ClientBuildManager, virtualPath: str) -> (Type, CompilerParameters) """
        ...

    def GetGeneratedFileVirtualPath(self, filePath:str) -> str:
        """ GetGeneratedFileVirtualPath(self: ClientBuildManager, filePath: str) -> str """
        ...

    def GetGeneratedSourceFile(self, virtualPath:str) -> str:
        """ GetGeneratedSourceFile(self: ClientBuildManager, virtualPath: str) -> str """
        ...

    def GetTopLevelAssemblyReferences(self, virtualPath:str) -> Array:
        """ GetTopLevelAssemblyReferences(self: ClientBuildManager, virtualPath: str) -> Array[str] """
        ...

    def GetVirtualCodeDirectories(self) -> Array:
        """ GetVirtualCodeDirectories(self: ClientBuildManager) -> Array[str] """
        ...

    def IsCodeAssembly(self, assemblyName:str) -> bool:
        """ IsCodeAssembly(self: ClientBuildManager, assemblyName: str) -> bool """
        ...

    def PrecompileApplication(self, callback = ..., forceCleanBuild:bool = ...): # ->  # Not found arg types: {'callback': 'ClientBuildManagerCallback'}
        """ PrecompileApplication(self: ClientBuildManager)PrecompileApplication(self: ClientBuildManager, callback: ClientBuildManagerCallback)PrecompileApplication(self: ClientBuildManager, callback: ClientBuildManagerCallback, forceCleanBuild: bool) """
        ...

    def Unload(self) -> bool:
        """ Unload(self: ClientBuildManager) -> bool """
        ...

    def __new__(cls, appVirtualDir:str, appPhysicalSourceDir:str, appPhysicalTargetDir:str = ..., parameter = ..., typeDescriptionProvider:TypeDescriptionProvider = ...) -> Self: # Not found arg types: {'parameter': 'ClientBuildManagerParameter'}
        """
        __new__(cls: type, appVirtualDir: str, appPhysicalSourceDir: str)
        __new__(cls: type, appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str)
        __new__(cls: type, appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str, parameter: ClientBuildManagerParameter)
        __new__(cls: type, appVirtualDir: str, appPhysicalSourceDir: str, appPhysicalTargetDir: str, parameter: ClientBuildManagerParameter, typeDescriptionProvider: TypeDescriptionProvider)
        """
        ...

    AppDomainShutdown = ...
    AppDomainStarted = ...
    AppDomainUnloaded = ...


class ClientBuildManagerCallback(MarshalByRefObject): # skipped bases: <type 'object'>
    """ ClientBuildManagerCallback() """
    def ReportCompilerError(self, error:CompilerError): # -> 
        """ ReportCompilerError(self: ClientBuildManagerCallback, error: CompilerError) """
        ...

    def ReportParseError(self, error:ParserError): # -> 
        """ ReportParseError(self: ClientBuildManagerCallback, error: ParserError) """
        ...

    def ReportProgress(self, message:str): # -> 
        """ ReportProgress(self: ClientBuildManagerCallback, message: str) """
        ...


class ClientBuildManagerParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ ClientBuildManagerParameter() """
    @property
    def ExcludedVirtualPaths(self) -> List:
        """ Get: ExcludedVirtualPaths(self: ClientBuildManagerParameter) -> List[str] """
        ...

    @property
    def PrecompilationFlags(self): # -> PrecompilationFlags
        """
        Get: PrecompilationFlags(self: ClientBuildManagerParameter) -> PrecompilationFlags
        Set: PrecompilationFlags(self: ClientBuildManagerParameter) = value
        """
        ...

    @property
    def StrongNameKeyContainer(self) -> str:
        """
        Get: StrongNameKeyContainer(self: ClientBuildManagerParameter) -> str
        Set: StrongNameKeyContainer(self: ClientBuildManagerParameter) = value
        """
        ...

    @property
    def StrongNameKeyFile(self) -> str:
        """
        Get: StrongNameKeyFile(self: ClientBuildManagerParameter) -> str
        Set: StrongNameKeyFile(self: ClientBuildManagerParameter) = value
        """
        ...



class CompilerType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CodeDomProviderType(self) -> Type:
        """ Get: CodeDomProviderType(self: CompilerType) -> Type """
        ...

    @property
    def CompilerParameters(self) -> CompilerParameters:
        """ Get: CompilerParameters(self: CompilerType) -> CompilerParameters """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: CompilerType, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CompilerType) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectionStringsExpressionBuilder(ExpressionBuilder): # skipped bases: <type 'object'>
    """ ConnectionStringsExpressionBuilder() """
    @staticmethod
    def GetConnectionString(connectionStringName:str) -> str:
        """ GetConnectionString(connectionStringName: str) -> str """
        ...

    @staticmethod
    def GetConnectionStringProviderName(connectionStringName:str) -> str:
        """ GetConnectionStringProviderName(connectionStringName: str) -> str """
        ...


class ControlBuilderInterceptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def OnProcessGeneratedCode(self, controlBuilder:ControlBuilder, codeCompileUnit:CodeCompileUnit, baseType:CodeTypeDeclaration, derivedType:CodeTypeDeclaration, buildMethod:CodeMemberMethod, dataBindingMethod:CodeMemberMethod, additionalState:IDictionary): # -> 
        """ OnProcessGeneratedCode(self: ControlBuilderInterceptor, controlBuilder: ControlBuilder, codeCompileUnit: CodeCompileUnit, baseType: CodeTypeDeclaration, derivedType: CodeTypeDeclaration, buildMethod: CodeMemberMethod, dataBindingMethod: CodeMemberMethod, additionalState: IDictionary) """
        ...

    def PreControlBuilderInit(self, controlBuilder:ControlBuilder, parser:TemplateParser, parentBuilder:ControlBuilder, type:Type, tagName:str, id:str, attributes:IDictionary, additionalState:IDictionary): # -> 
        """ PreControlBuilderInit(self: ControlBuilderInterceptor, controlBuilder: ControlBuilder, parser: TemplateParser, parentBuilder: ControlBuilder, type: Type, tagName: str, id: str, attributes: IDictionary, additionalState: IDictionary) """
        ...


class DesignTimeResourceProviderFactoryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignTimeResourceProviderFactoryAttribute(factoryType: Type)
    DesignTimeResourceProviderFactoryAttribute(factoryTypeName: str)
    """
    @property
    def FactoryTypeName(self) -> str:
        """ Get: FactoryTypeName(self: DesignTimeResourceProviderFactoryAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, factoryType: Type)
        __new__(cls: type, factoryTypeName: str)
        """
        ...


class ExpressionBuilderContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    ExpressionBuilderContext(virtualPath: str)
    ExpressionBuilderContext(templateControl: TemplateControl)
    """
    @property
    def TemplateControl(self) -> TemplateControl:
        """ Get: TemplateControl(self: ExpressionBuilderContext) -> TemplateControl """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: ExpressionBuilderContext) -> str """
        ...



class ExpressionEditorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ExpressionEditorAttribute(type: Type)
    ExpressionEditorAttribute(typeName: str)
    """
    @property
    def EditorTypeName(self) -> str:
        """ Get: EditorTypeName(self: ExpressionEditorAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        ...


class ExpressionPrefixAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExpressionPrefixAttribute(expressionPrefix: str) """
    @property
    def ExpressionPrefix(self) -> str:
        """ Get: ExpressionPrefix(self: ExpressionPrefixAttribute) -> str """
        ...


    def __new__(cls, expressionPrefix:str) -> Self:
        """ __new__(cls: type, expressionPrefix: str) """
        ...


class FolderLevelBuildProviderAppliesTo(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FolderLevelBuildProviderAppliesTo, values: Code (1), GlobalResources (8), LocalResources (4), None (0), WebReferences (2) """
    Code: FolderLevelBuildProviderAppliesTo = ...
    GlobalResources: FolderLevelBuildProviderAppliesTo = ...
    LocalResources: FolderLevelBuildProviderAppliesTo = ...
    value__ = ...
    WebReferences: FolderLevelBuildProviderAppliesTo = ...


class FolderLevelBuildProviderAppliesToAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FolderLevelBuildProviderAppliesToAttribute(appliesTo: FolderLevelBuildProviderAppliesTo) """
    @property
    def AppliesTo(self) -> FolderLevelBuildProviderAppliesTo:
        """ Get: AppliesTo(self: FolderLevelBuildProviderAppliesToAttribute) -> FolderLevelBuildProviderAppliesTo """
        ...


    def __new__(cls, appliesTo:FolderLevelBuildProviderAppliesTo) -> Self:
        """ __new__(cls: type, appliesTo: FolderLevelBuildProviderAppliesTo) """
        ...


class IAssemblyPostProcessor(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def PostProcessAssembly(self, path:str): # -> 
        """ PostProcessAssembly(self: IAssemblyPostProcessor, path: str) """
        ...


class IImplicitResourceProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetImplicitResourceKeys(self, keyPrefix:str) -> ICollection:
        """ GetImplicitResourceKeys(self: IImplicitResourceProvider, keyPrefix: str) -> ICollection """
        ...

    def GetObject(self, key, culture:CultureInfo) -> object: # Not found arg types: {'key': 'ImplicitResourceKey'}
        """ GetObject(self: IImplicitResourceProvider, key: ImplicitResourceKey, culture: CultureInfo) -> object """
        ...


class ImplicitResourceKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    ImplicitResourceKey()
    ImplicitResourceKey(filter: str, keyPrefix: str, property: str)
    """
    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: ImplicitResourceKey) -> str
        Set: Filter(self: ImplicitResourceKey) = value
        """
        ...

    @property
    def KeyPrefix(self) -> str:
        """
        Get: KeyPrefix(self: ImplicitResourceKey) -> str
        Set: KeyPrefix(self: ImplicitResourceKey) = value
        """
        ...

    @property
    def Property(self) -> str:
        """
        Get: Property(self: ImplicitResourceKey) -> str
        Set: Property(self: ImplicitResourceKey) = value
        """
        ...



class IResourceProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ResourceReader(self) -> IResourceReader:
        """ Get: ResourceReader(self: IResourceProvider) -> IResourceReader """
        ...


    def GetObject(self, resourceKey:str, culture:CultureInfo) -> object:
        """ GetObject(self: IResourceProvider, resourceKey: str, culture: CultureInfo) -> object """
        ...


class IWcfReferenceReceiveContextInformation: # skipped bases: <type 'object'>
    """ no doc """
    def ReceiveImportContextInformation(self, serviceReferenceExtensionFileContents:IDictionary, serviceProvider:IServiceProvider): # -> 
        """ ReceiveImportContextInformation(self: IWcfReferenceReceiveContextInformation, serviceReferenceExtensionFileContents: IDictionary[str, Array[Byte]], serviceProvider: IServiceProvider) """
        ...


class LinePragmaCodeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    LinePragmaCodeInfo()
    LinePragmaCodeInfo(startLine: int, startColumn: int, startGeneratedColumn: int, codeLength: int, isCodeNugget: bool)
    """
    @property
    def CodeLength(self) -> int:
        """ Get: CodeLength(self: LinePragmaCodeInfo) -> int """
        ...

    @property
    def IsCodeNugget(self) -> bool:
        """ Get: IsCodeNugget(self: LinePragmaCodeInfo) -> bool """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: LinePragmaCodeInfo) -> int """
        ...

    @property
    def StartGeneratedColumn(self) -> int:
        """ Get: StartGeneratedColumn(self: LinePragmaCodeInfo) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: LinePragmaCodeInfo) -> int """
        ...



class PrecompilationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PrecompilationFlags, values: AllowPartiallyTrustedCallers (32), Clean (8), CodeAnalysis (16), Default (0), DelaySign (64), FixedNames (128), ForceDebug (4), IgnoreBadImageFormatException (256), OverwriteTarget (2), Updatable (1) """
    AllowPartiallyTrustedCallers: PrecompilationFlags = ...
    Clean: PrecompilationFlags = ...
    CodeAnalysis: PrecompilationFlags = ...
    Default: PrecompilationFlags = ...
    DelaySign: PrecompilationFlags = ...
    FixedNames: PrecompilationFlags = ...
    ForceDebug: PrecompilationFlags = ...
    IgnoreBadImageFormatException: PrecompilationFlags = ...
    OverwriteTarget: PrecompilationFlags = ...
    Updatable: PrecompilationFlags = ...
    value__ = ...


class ResourceExpressionBuilder(ExpressionBuilder): # skipped bases: <type 'object'>
    """ ResourceExpressionBuilder() """
    pass

class ResourceExpressionFields: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClassKey(self) -> str:
        """ Get: ClassKey(self: ResourceExpressionFields) -> str """
        ...

    @property
    def ResourceKey(self) -> str:
        """ Get: ResourceKey(self: ResourceExpressionFields) -> str """
        ...



class ResourceProviderFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateGlobalResourceProvider(self, classKey:str) -> IResourceProvider:
        """ CreateGlobalResourceProvider(self: ResourceProviderFactory, classKey: str) -> IResourceProvider """
        ...

    def CreateLocalResourceProvider(self, virtualPath:str) -> IResourceProvider:
        """ CreateLocalResourceProvider(self: ResourceProviderFactory, virtualPath: str) -> IResourceProvider """
        ...


class RouteUrlExpressionBuilder(ExpressionBuilder): # skipped bases: <type 'object'>
    """ RouteUrlExpressionBuilder() """
    @staticmethod
    def GetRouteUrl(control:Control, expression:str) -> str:
        """ GetRouteUrl(control: Control, expression: str) -> str """
        ...

    @staticmethod
    def TryParseRouteExpression(expression, routeValues, routeName) -> Tuple_[bool, str]:
        """ TryParseRouteExpression(expression: str, routeValues: RouteValueDictionary) -> (bool, str) """
        ...


class RouteValueExpressionBuilder(ExpressionBuilder): # skipped bases: <type 'object'>
    """ RouteValueExpressionBuilder() """
    @staticmethod
    def GetRouteValue(page:Page, key:str, controlType:Type, propertyName:str) -> object:
        """ GetRouteValue(page: Page, key: str, controlType: Type, propertyName: str) -> object """
        ...


class WCFBuildProvider(BuildProvider): # skipped bases: <type 'object'>
    """ WCFBuildProvider() """
    pass

