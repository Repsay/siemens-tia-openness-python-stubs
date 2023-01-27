# encoding: utf-8
# module Microsoft.Scripting calls itself Scripting
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1, Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import TokenTriggers

from Microsoft.Office.Interop.Word import Categories

from System import (Array, Attribute, Enum, EventArgs, Guid, IEquatable, 
    Nullable, StringComparer, Type, WeakReference)

from System.Activities.Debugger import SourceLocation

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.Generic import Dictionary

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Dynamic import IDynamicMetaObjectProvider

from System.IdentityModel import Scope

from System.IO import (FileAccess, FileMode, FileShare, Stream, TextReader, 
    TextWriter)

from System.Linq.Expressions import Expression, SymbolDocumentInfo

from System.Management.Automation.Language import TokenKind

from System.Reflection import Assembly

from System.Text import Encoding

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IWeakReferencable, LanguageContext, NullErrorSink, 
    ReadOnlyCollection[str], ScopeVariableIgnoreCase, ScriptDomainManager, 
    Severity, SourceSpan, SourceUnit, T, TKey, field#)
"""

# no functions
# classes

class AmbiguousFileNameException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AmbiguousFileNameException(firstPath: str, secondPath: str)
    AmbiguousFileNameException(firstPath: str, secondPath: str, message: str)
    AmbiguousFileNameException(firstPath: str, secondPath: str, message: str, inner: Exception)
    """
    @property
    def FirstPath(self) -> str:
        """ Get: FirstPath(self: AmbiguousFileNameException) -> str """
        ...

    @property
    def SecondPath(self) -> str:
        """ Get: SecondPath(self: AmbiguousFileNameException) -> str """
        ...


    SerializeObjectState = ...


class ArgumentTypeException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ArgumentTypeException()
    ArgumentTypeException(message: str)
    ArgumentTypeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class AssemblyLoadedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ AssemblyLoadedEventArgs(assembly: Assembly) """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: AssemblyLoadedEventArgs) -> Assembly """
        ...


    def __new__(cls, assembly:Assembly) -> Self:
        """ __new__(cls: type, assembly: Assembly) """
        ...


class CompilerOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ CompilerOptions() """
    pass

class ErrorSink: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Add(self, *__args): # -> 
        """ Add(self: ErrorSink, source: SourceUnit, message: str, span: SourceSpan, errorCode: int, severity: Severity)Add(self: ErrorSink, message: str, path: str, code: str, line: str, span: SourceSpan, errorCode: int, severity: Severity) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    Default: ErrorSink = ...
    Null = ...


class ErrorCounter(ErrorSink): # skipped bases: <type 'object'>
    """
    ErrorCounter()
    ErrorCounter(sink: ErrorSink)
    """
    @property
    def AnyError(self) -> bool:
        """ Get: AnyError(self: ErrorCounter) -> bool """
        ...

    @property
    def ErrorCount(self) -> int:
        """ Get: ErrorCount(self: ErrorCounter) -> int """
        ...

    @property
    def FatalErrorCount(self) -> int:
        """ Get: FatalErrorCount(self: ErrorCounter) -> int """
        ...

    @property
    def WarningCount(self) -> int:
        """ Get: WarningCount(self: ErrorCounter) -> int """
        ...


    def ClearCounters(self): # -> 
        """ ClearCounters(self: ErrorCounter) """
        ...

    def CountError(self, *args): #cannot find CLR method
        """ CountError(self: ErrorCounter, severity: Severity) """
        ...

    def __new__(cls, sink:ErrorSink = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sink: ErrorSink)
        """
        ...


class ICustomScriptCodeData: # skipped bases: <type 'object'>
    """ no doc """
    def GetCustomScriptCodeData(self) -> str:
        """ GetCustomScriptCodeData(self: ICustomScriptCodeData) -> str """
        ...


class IndexSpan(IEquatable): # skipped bases: <type 'object'>
    """ IndexSpan(start: int, length: int) """
    @property
    def End(self) -> int:
        """ Get: End(self: IndexSpan) -> int """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: IndexSpan) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: IndexSpan) -> int """
        ...

    @property
    def Start(self) -> int:
        """ Get: Start(self: IndexSpan) -> int """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: IndexSpan) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class InvalidImplementationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidImplementationException()
    InvalidImplementationException(message: str)
    InvalidImplementationException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class IScopeVariable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: IScopeVariable) -> bool """
        ...


    def DeleteValue(self) -> bool:
        """ DeleteValue(self: IScopeVariable) -> bool """
        ...

    def SetValue(self, value:object): # -> 
        """ SetValue(self: IScopeVariable, value: object) """
        ...

    def TryGetValue(self, value) -> Tuple_[bool, object]:
        """ TryGetValue(self: IScopeVariable) -> (bool, object) """
        ...


class KeyboardInterruptException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    KeyboardInterruptException()
    KeyboardInterruptException(msg: str)
    KeyboardInterruptException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class LanguageOptions: # skipped bases: <type 'object'>, <type 'object'>
    """
    LanguageOptions()
    LanguageOptions(options: IDictionary[str, object])
    """
    @property
    def CompilationThreshold(self) -> int:
        """ Get: CompilationThreshold(self: LanguageOptions) -> int """
        ...

    @property
    def ExceptionDetail(self) -> bool:
        """
        Get: ExceptionDetail(self: LanguageOptions) -> bool
        Set: ExceptionDetail(self: LanguageOptions) = value
        """
        ...

    @property
    def InterpretedMode(self) -> bool:
        """
        Get: InterpretedMode(self: LanguageOptions) -> bool
        Set: InterpretedMode(self: LanguageOptions) = value
        """
        ...

    @property
    def NoAdaptiveCompilation(self) -> bool:
        """ Get: NoAdaptiveCompilation(self: LanguageOptions) -> bool """
        ...

    @property
    def PerfStats(self) -> bool:
        """ Get: PerfStats(self: LanguageOptions) -> bool """
        ...

    @property
    def SearchPaths(self) -> ReadOnlyCollection:
        """ Get: SearchPaths(self: LanguageOptions) -> ReadOnlyCollection[str] """
        ...

    @property
    def ShowClrExceptions(self) -> bool:
        """
        Get: ShowClrExceptions(self: LanguageOptions) -> bool
        Set: ShowClrExceptions(self: LanguageOptions) = value
        """
        ...


    @staticmethod
    def GetOption(options:IDictionary, name:str, defaultValue): # -> T # Not found arg types: {'defaultValue': 'T'}
        """ GetOption[T](options: IDictionary[str, object], name: str, defaultValue: T) -> T """
        ...

    @staticmethod
    def GetSearchPathsOption(options:IDictionary) -> ReadOnlyCollection:
        """ GetSearchPathsOption(options: IDictionary[str, object]) -> ReadOnlyCollection[str] """
        ...

    @staticmethod
    def GetStringCollectionOption(options:IDictionary, name:str, separators:Array) -> ReadOnlyCollection:
        """ GetStringCollectionOption(options: IDictionary[str, object], name: str, *separators: Array[Char]) -> ReadOnlyCollection[str] """
        ...

    EmptyStringCollection = ...


class MultiRuntimeAwareAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MultiRuntimeAwareAttribute() """
    pass

class MutableTuple: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Capacity(self) -> int:
        """ Get: Capacity(self: MutableTuple) -> int """
        ...


    @staticmethod
    def Create(values:Array) -> Expression:
        """ Create(*values: Array[Expression]) -> Expression """
        ...

    @staticmethod
    def GetAccessPath(tupleType:Type, *__args:int) -> IEnumerable:
        """
        GetAccessPath(tupleType: Type, index: int) -> IEnumerable[PropertyInfo]
        GetAccessPath(tupleType: Type, size: int, index: int) -> IEnumerable[PropertyInfo]
        """
        ...

    def GetNestedValue(self, size:int, index:int) -> object:
        """ GetNestedValue(self: MutableTuple, size: int, index: int) -> object """
        ...

    @staticmethod
    def GetSize(tupleType:Type) -> int:
        """ GetSize(tupleType: Type) -> int """
        ...

    @staticmethod
    def GetTupleType(size:int) -> Type:
        """ GetTupleType(size: int) -> Type """
        ...

    @staticmethod
    def GetTupleValues(tuple:MutableTuple) -> Array:
        """ GetTupleValues(tuple: MutableTuple) -> Array[object] """
        ...

    def GetValue(self, index:int) -> object:
        """ GetValue(self: MutableTuple, index: int) -> object """
        ...

    @staticmethod
    def MakeTuple(tupleType:Type, args:Array) -> MutableTuple:
        """ MakeTuple(tupleType: Type, *args: Array[object]) -> MutableTuple """
        ...

    @staticmethod
    def MakeTupleType(types:Array) -> Type:
        """ MakeTupleType(*types: Array[Type]) -> Type """
        ...

    def SetNestedValue(self, size:int, index:int, value:object): # -> 
        """ SetNestedValue(self: MutableTuple, size: int, index: int, value: object) """
        ...

    def SetValue(self, index:int, value:object): # -> 
        """ SetValue(self: MutableTuple, index: int, value: object) """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    MaxSize: int = ...


class ParamDictionaryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ParamDictionaryAttribute() """
    pass

class PerfTrack: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddHistograms(result:IDictionary, addend:IDictionary): # -> 
        """ AddHistograms[TKey](result: IDictionary[TKey, int], addend: IDictionary[TKey, int]) """
        ...

    def Categories(self, *args): #cannot find CLR method
        """ enum Categories, values: Binding (13), BindingFast (15), BindingSlow (14), BindingTarget (16), Compiler (6), Count (17), DelegateCreate (7), DictInvoke (8), Exceptions (2), Fields (4), Methods (5), OperatorInvoke (9), OverAllocate (10), Properties (3), ReflectedTypes (1), RuleEvaluation (12), Rules (11), Temporary (0) """
        ...

    @staticmethod
    def DumpHistogram(histogram:IDictionary, output:TextWriter = ...): # -> 
        """ DumpHistogram[TKey](histogram: IDictionary[TKey, int])DumpHistogram[TKey](histogram: IDictionary[TKey, int], output: TextWriter) """
        ...

    @staticmethod
    def DumpStats(output=None): # -> 
        """ DumpStats()DumpStats(output: TextWriter) """
        ...

    @staticmethod
    def IncrementEntry(histogram:IDictionary, key): # ->  # Not found arg types: {'key': 'TKey'}
        """ IncrementEntry[TKey](histogram: IDictionary[TKey, int], key: TKey) """
        ...

    @staticmethod
    def NoteEvent(category:Categories, key:object): # -> 
        """ NoteEvent(category: Categories, key: object) """
        ...

    __all__: list = ...


class PlatformAdaptationLayer: # skipped bases: <type 'object'>, <type 'object'>
    """ PlatformAdaptationLayer() """
    @property
    def CurrentDirectory(self) -> str:
        """
        Get: CurrentDirectory(self: PlatformAdaptationLayer) -> str
        Set: CurrentDirectory(self: PlatformAdaptationLayer) = value
        """
        ...

    @property
    def IsNativeModule(self) -> bool:
        """ Get: IsNativeModule() -> bool """
        ...

    @property
    def IsSingleRootFileSystem(self) -> bool:
        """ Get: IsSingleRootFileSystem(self: PlatformAdaptationLayer) -> bool """
        ...

    @property
    def PathComparer(self) -> StringComparer:
        """ Get: PathComparer(self: PlatformAdaptationLayer) -> StringComparer """
        ...


    def CombinePaths(self, path1:str, path2:str) -> str:
        """ CombinePaths(self: PlatformAdaptationLayer, path1: str, path2: str) -> str """
        ...

    def CreateDirectory(self, path:str): # -> 
        """ CreateDirectory(self: PlatformAdaptationLayer, path: str) """
        ...

    def DeleteDirectory(self, path:str, recursive:bool): # -> 
        """ DeleteDirectory(self: PlatformAdaptationLayer, path: str, recursive: bool) """
        ...

    def DeleteFile(self, path:str, deleteReadOnly:bool): # -> 
        """ DeleteFile(self: PlatformAdaptationLayer, path: str, deleteReadOnly: bool) """
        ...

    def DirectoryExists(self, path:str) -> bool:
        """ DirectoryExists(self: PlatformAdaptationLayer, path: str) -> bool """
        ...

    def FileExists(self, path:str) -> bool:
        """ FileExists(self: PlatformAdaptationLayer, path: str) -> bool """
        ...

    def GetDirectories(self, path:str, searchPattern:str) -> Array:
        """ GetDirectories(self: PlatformAdaptationLayer, path: str, searchPattern: str) -> Array[str] """
        ...

    def GetDirectoryName(self, path:str) -> str:
        """ GetDirectoryName(self: PlatformAdaptationLayer, path: str) -> str """
        ...

    def GetEnvironmentVariable(self, key:str) -> str:
        """ GetEnvironmentVariable(self: PlatformAdaptationLayer, key: str) -> str """
        ...

    def GetEnvironmentVariables(self) -> Dictionary:
        """ GetEnvironmentVariables(self: PlatformAdaptationLayer) -> Dictionary[str, str] """
        ...

    def GetExtension(self, path:str) -> str:
        """ GetExtension(self: PlatformAdaptationLayer, path: str) -> str """
        ...

    def GetFileName(self, path:str) -> str:
        """ GetFileName(self: PlatformAdaptationLayer, path: str) -> str """
        ...

    def GetFileNameWithoutExtension(self, path:str) -> str:
        """ GetFileNameWithoutExtension(self: PlatformAdaptationLayer, path: str) -> str """
        ...

    def GetFiles(self, path:str, searchPattern:str) -> Array:
        """ GetFiles(self: PlatformAdaptationLayer, path: str, searchPattern: str) -> Array[str] """
        ...

    def GetFileSystemEntries(self, path:str, searchPattern:str, includeFiles:bool = ..., includeDirectories:bool = ...) -> Array:
        """
        GetFileSystemEntries(self: PlatformAdaptationLayer, path: str, searchPattern: str) -> Array[str]
        GetFileSystemEntries(self: PlatformAdaptationLayer, path: str, searchPattern: str, includeFiles: bool, includeDirectories: bool) -> Array[str]
        """
        ...

    def GetFullPath(self, path:str) -> str:
        """ GetFullPath(self: PlatformAdaptationLayer, path: str) -> str """
        ...

    def IsAbsolutePath(self, path:str) -> bool:
        """ IsAbsolutePath(self: PlatformAdaptationLayer, path: str) -> bool """
        ...

    def LoadAssembly(self, name:str) -> Assembly:
        """ LoadAssembly(self: PlatformAdaptationLayer, name: str) -> Assembly """
        ...

    def LoadAssemblyFromPath(self, path:str) -> Assembly:
        """ LoadAssemblyFromPath(self: PlatformAdaptationLayer, path: str) -> Assembly """
        ...

    def MoveFileSystemEntry(self, sourcePath:str, destinationPath:str): # -> 
        """ MoveFileSystemEntry(self: PlatformAdaptationLayer, sourcePath: str, destinationPath: str) """
        ...

    def OpenFileStream(self, path:str, mode:FileMode, access:FileAccess, share:FileShare, bufferSize:int) -> Stream:
        """ OpenFileStream(self: PlatformAdaptationLayer, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int) -> Stream """
        ...

    def OpenInputFileStream(self, path:str, mode:FileMode, access:FileAccess, share:FileShare, bufferSize:int) -> Stream:
        """ OpenInputFileStream(self: PlatformAdaptationLayer, path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int) -> Stream """
        ...

    def OpenOutputFileStream(self, path:str) -> Stream:
        """ OpenOutputFileStream(self: PlatformAdaptationLayer, path: str) -> Stream """
        ...

    def SetEnvironmentVariable(self, key:str, value:str): # -> 
        """ SetEnvironmentVariable(self: PlatformAdaptationLayer, key: str, value: str) """
        ...

    def TerminateScriptExecution(self, exitCode:int): # -> 
        """ TerminateScriptExecution(self: PlatformAdaptationLayer, exitCode: int) """
        ...

    Default: PlatformAdaptationLayer = ...
    IsCompactFramework: bool = ...


class ScriptCode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LanguageContext(self): # -> LanguageContext
        """ Get: LanguageContext(self: ScriptCode) -> LanguageContext """
        ...

    @property
    def SourceUnit(self): # -> SourceUnit
        """ Get: SourceUnit(self: ScriptCode) -> SourceUnit """
        ...


    def CreateScope(self) -> Scope:
        """ CreateScope(self: ScriptCode) -> Scope """
        ...

    def Run(self, scope:Scope = ...) -> object:
        """
        Run(self: ScriptCode) -> object
        Run(self: ScriptCode, scope: Scope) -> object
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: ScriptCode) -> str """
        ...


class SavableScriptCode(ScriptCode): # skipped bases: <type 'object'>
    """ no doc """
    def CompileForSave(self, *args): #cannot find CLR method
        """ CompileForSave(self: SavableScriptCode, typeGen: TypeGen) -> KeyValuePair[MethodBuilder, Type] """
        ...

    @staticmethod
    def LoadFromAssembly(runtime, assembly:Assembly) -> Array: # Not found arg types: {'runtime': 'ScriptDomainManager'}
        """ LoadFromAssembly(runtime: ScriptDomainManager, assembly: Assembly) -> Array[ScriptCode] """
        ...

    def RewriteForSave(self, *args): #cannot find CLR method
        """ RewriteForSave(self: SavableScriptCode, typeGen: TypeGen, code: LambdaExpression) -> LambdaExpression """
        ...

    @staticmethod
    def SaveToAssembly(assemblyName:str, *__args:Array): # -> 
        """ SaveToAssembly(assemblyName: str, assemblyAttributes: IDictionary[str, object], *codes: Array[SavableScriptCode])SaveToAssembly(assemblyName: str, *codes: Array[SavableScriptCode]) """
        ...


class ScopeStorage(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ ScopeStorage() """
    def DeleteValue(self, name:str, ignoreCase:bool) -> bool:
        """ DeleteValue(self: ScopeStorage, name: str, ignoreCase: bool) -> bool """
        ...

    def GetItems(self) -> IList:
        """ GetItems(self: ScopeStorage) -> IList[KeyValuePair[str, object]] """
        ...

    def GetMemberNames(self) -> IList:
        """ GetMemberNames(self: ScopeStorage) -> IList[str] """
        ...

    def GetScopeVariable(self, name:str, ignoreCase:bool = ...) -> IScopeVariable:
        """
        GetScopeVariable(self: ScopeStorage, name: str, ignoreCase: bool) -> IScopeVariable
        GetScopeVariable(self: ScopeStorage, name: str) -> ScopeVariable
        """
        ...

    def GetScopeVariableIgnoreCase(self, name:str): # -> ScopeVariableIgnoreCase
        """ GetScopeVariableIgnoreCase(self: ScopeStorage, name: str) -> ScopeVariableIgnoreCase """
        ...

    def GetValue(self, name:str, ignoreCase:bool) -> object:
        """ GetValue(self: ScopeStorage, name: str, ignoreCase: bool) -> object """
        ...

    def HasValue(self, name:str, ignoreCase:bool) -> bool:
        """ HasValue(self: ScopeStorage, name: str, ignoreCase: bool) -> bool """
        ...

    def SetValue(self, name:str, ignoreCase:bool, value:object): # -> 
        """ SetValue(self: ScopeStorage, name: str, ignoreCase: bool, value: object) """
        ...

    def TryGetValue(self, name, ignoreCase, value) -> Tuple_[bool, object]:
        """ TryGetValue(self: ScopeStorage, name: str, ignoreCase: bool) -> (bool, object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ScopeVariable(IWeakReferencable, IScopeVariable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WeakReference(self) -> WeakReference:
        """ Get: WeakReference(self: ScopeVariable) -> WeakReference """
        ...



class ScopeVariableIgnoreCase(IWeakReferencable, IScopeVariable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WeakReference(self) -> WeakReference:
        """ Get: WeakReference(self: ScopeVariableIgnoreCase) -> WeakReference """
        ...



class ScriptCodeParseResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ScriptCodeParseResult, values: Complete (0), Empty (1), IncompleteStatement (4), IncompleteToken (3), Invalid (2) """
    Complete: ScriptCodeParseResult = ...
    Empty: ScriptCodeParseResult = ...
    IncompleteStatement: ScriptCodeParseResult = ...
    IncompleteToken: ScriptCodeParseResult = ...
    Invalid: ScriptCodeParseResult = ...
    value__ = ...


class Severity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Severity, values: Error (2), FatalError (3), Ignore (0), Warning (1) """
    Error: Severity = ...
    FatalError: Severity = ...
    Ignore: Severity = ...
    value__ = ...
    Warning: Severity = ...


class SourceCodeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SourceCodeKind, values: AutoDetect (6), Expression (1), File (4), InteractiveCode (5), SingleStatement (3), Statements (2), Unspecified (0) """
    AutoDetect: SourceCodeKind = ...
    Expression: SourceCodeKind = ...
    File: SourceCodeKind = ...
    InteractiveCode: SourceCodeKind = ...
    SingleStatement: SourceCodeKind = ...
    Statements: SourceCodeKind = ...
    Unspecified: SourceCodeKind = ...
    value__ = ...


class SourceCodePropertiesUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsCompleteOrInvalid(props:ScriptCodeParseResult, allowIncompleteStatement:bool) -> bool:
        """ IsCompleteOrInvalid(props: ScriptCodeParseResult, allowIncompleteStatement: bool) -> bool """
        ...

    __all__: list = ...


class SourceCodeReader(TextReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SourceCodeReader(textReader: TextReader, encoding: Encoding) """
    @property
    def BaseReader(self) -> TextReader:
        """ Get: BaseReader(self: SourceCodeReader) -> TextReader """
        ...

    @property
    def Encoding(self) -> Encoding:
        """ Get: Encoding(self: SourceCodeReader) -> Encoding """
        ...


    def SeekLine(self, line:int) -> bool:
        """ SeekLine(self: SourceCodeReader, line: int) -> bool """
        ...

    def __new__(cls, textReader:TextReader, encoding:Encoding) -> Self:
        """ __new__(cls: type, textReader: TextReader, encoding: Encoding) """
        ...

    Null: SourceCodeReader = ...


class SourceFileInformation: # skipped bases: <type 'object'>, <type 'object'>
    """
    SourceFileInformation(fileName: str)
    SourceFileInformation(fileName: str, language: Guid)
    SourceFileInformation(fileName: str, language: Guid, vendor: Guid)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SourceFileInformation) -> str """
        ...

    @property
    def LanguageGuid(self) -> Guid:
        """ Get: LanguageGuid(self: SourceFileInformation) -> Guid """
        ...

    @property
    def VendorGuid(self) -> Guid:
        """ Get: VendorGuid(self: SourceFileInformation) -> Guid """
        ...



class SourceLocation(IEquatable): # skipped bases: <type 'object'>
    """ SourceLocation(index: int, line: int, column: int) """
    @property
    def Column(self) -> int:
        """ Get: Column(self: SourceLocation) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: SourceLocation) -> int """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: SourceLocation) -> bool """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: SourceLocation) -> int """
        ...


    @staticmethod
    def Compare(left:SourceLocation, right:SourceLocation) -> int:
        """ Compare(left: SourceLocation, right: SourceLocation) -> int """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SourceLocation) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SourceLocation) -> str """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Invalid: SourceLocation = ...
    MinValue: SourceLocation = ...


class SourceSpan(IEquatable): # skipped bases: <type 'object'>
    """ SourceSpan(start: SourceLocation, end: SourceLocation) """
    @property
    def End(self) -> SourceLocation:
        """ Get: End(self: SourceSpan) -> SourceLocation """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: SourceSpan) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: SourceSpan) -> int """
        ...

    @property
    def Start(self) -> SourceLocation:
        """ Get: Start(self: SourceSpan) -> SourceLocation """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: SourceSpan) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SourceSpan) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Invalid: SourceSpan = ...


class SourceUnit: # skipped bases: <type 'object'>, <type 'object'>
    """ SourceUnit(context: LanguageContext, contentProvider: TextContentProvider, path: str, kind: SourceCodeKind) """
    @property
    def CodeProperties(self) -> Nullable:
        """
        Get: CodeProperties(self: SourceUnit) -> Nullable[ScriptCodeParseResult]
        Set: CodeProperties(self: SourceUnit) = value
        """
        ...

    @property
    def Document(self) -> SymbolDocumentInfo:
        """ Get: Document(self: SourceUnit) -> SymbolDocumentInfo """
        ...

    @property
    def EmitDebugSymbols(self) -> bool:
        """ Get: EmitDebugSymbols(self: SourceUnit) -> bool """
        ...

    @property
    def HasLineMapping(self) -> bool:
        """ Get: HasLineMapping(self: SourceUnit) -> bool """
        ...

    @property
    def HasPath(self) -> bool:
        """ Get: HasPath(self: SourceUnit) -> bool """
        ...

    @property
    def Kind(self) -> SourceCodeKind:
        """ Get: Kind(self: SourceUnit) -> SourceCodeKind """
        ...

    @property
    def LanguageContext(self): # -> LanguageContext
        """ Get: LanguageContext(self: SourceUnit) -> LanguageContext """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: SourceUnit) -> str """
        ...


    def Compile(self, *__args:ErrorSink) -> ScriptCode:
        """
        Compile(self: SourceUnit) -> ScriptCode
        Compile(self: SourceUnit, errorSink: ErrorSink) -> ScriptCode
        Compile(self: SourceUnit, options: CompilerOptions, errorSink: ErrorSink) -> ScriptCode
        """
        ...

    def Execute(self, *__args:Scope) -> object:
        """
        Execute(self: SourceUnit, scope: Scope) -> object
        Execute(self: SourceUnit, scope: Scope, errorSink: ErrorSink) -> object
        Execute(self: SourceUnit) -> object
        Execute(self: SourceUnit, errorSink: ErrorSink) -> object
        Execute(self: SourceUnit, options: CompilerOptions, errorSink: ErrorSink) -> object
        """
        ...

    def ExecuteProgram(self) -> int:
        """ ExecuteProgram(self: SourceUnit) -> int """
        ...

    def GetCode(self) -> str:
        """ GetCode(self: SourceUnit) -> str """
        ...

    def GetCodeLine(self, line:int) -> str:
        """ GetCodeLine(self: SourceUnit, line: int) -> str """
        ...

    def GetCodeLines(self, start:int, count:int) -> Array:
        """ GetCodeLines(self: SourceUnit, start: int, count: int) -> Array[str] """
        ...

    def GetCodeProperties(self, options:CompilerOptions = ...) -> ScriptCodeParseResult:
        """
        GetCodeProperties(self: SourceUnit) -> ScriptCodeParseResult
        GetCodeProperties(self: SourceUnit, options: CompilerOptions) -> ScriptCodeParseResult
        """
        ...

    def GetReader(self) -> SourceCodeReader:
        """ GetReader(self: SourceUnit) -> SourceCodeReader """
        ...

    def MakeLocation(self, *__args:SourceLocation) -> SourceLocation:
        """
        MakeLocation(self: SourceUnit, index: int, line: int, column: int) -> SourceLocation
        MakeLocation(self: SourceUnit, loc: SourceLocation) -> SourceLocation
        """
        ...

    def MapLine(self, line:int) -> int:
        """ MapLine(self: SourceUnit, line: int) -> int """
        ...

    def SetLineMapping(self, lineMap:Array): # -> 
        """ SetLineMapping(self: SourceUnit, lineMap: Array[KeyValuePair[int, int]]) """
        ...


class StreamContentProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetStream(self) -> Stream:
        """ GetStream(self: StreamContentProvider) -> Stream """
        ...


class SyntaxErrorException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SyntaxErrorException()
    SyntaxErrorException(message: str)
    SyntaxErrorException(message: str, innerException: Exception)
    SyntaxErrorException(message: str, sourceUnit: SourceUnit, span: SourceSpan, errorCode: int, severity: Severity)
    SyntaxErrorException(message: str, path: str, code: str, line: str, span: SourceSpan, errorCode: int, severity: Severity)
    """
    @property
    def Column(self) -> int:
        """ Get: Column(self: SyntaxErrorException) -> int """
        ...

    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: SyntaxErrorException) -> int """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: SyntaxErrorException) -> int """
        ...

    @property
    def RawSpan(self) -> SourceSpan:
        """ Get: RawSpan(self: SyntaxErrorException) -> SourceSpan """
        ...

    @property
    def Severity(self) -> Severity:
        """ Get: Severity(self: SyntaxErrorException) -> Severity """
        ...

    @property
    def SourceCode(self) -> str:
        """ Get: SourceCode(self: SyntaxErrorException) -> str """
        ...

    @property
    def SourcePath(self) -> str:
        """ Get: SourcePath(self: SyntaxErrorException) -> str """
        ...


    def GetCodeLine(self) -> str:
        """ GetCodeLine(self: SyntaxErrorException) -> str """
        ...

    def GetSymbolDocumentName(self) -> str:
        """ GetSymbolDocumentName(self: SyntaxErrorException) -> str """
        ...

    SerializeObjectState = ...


class TextContentProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetReader(self) -> SourceCodeReader:
        """ GetReader(self: TextContentProvider) -> SourceCodeReader """
        ...


class TokenCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TokenCategory, values: CharacterLiteral (7), Comment (3), Delimiter (13), Directive (11), DocComment (5), EndOfStream (1), Error (16), Grouping (15), Identifier (14), Keyword (10), LanguageDefined (256), LineComment (4), None (0), NumericLiteral (6), Operator (12), RegularExpressionLiteral (9), StringLiteral (8), WhiteSpace (2) """
    CharacterLiteral: TokenCategory = ...
    Comment: TokenCategory = ...
    Delimiter: TokenCategory = ...
    Directive: TokenCategory = ...
    DocComment: TokenCategory = ...
    EndOfStream: TokenCategory = ...
    Error: TokenCategory = ...
    Grouping: TokenCategory = ...
    Identifier: TokenCategory = ...
    Keyword: TokenCategory = ...
    LanguageDefined: TokenCategory = ...
    LineComment: TokenCategory = ...
    NumericLiteral: TokenCategory = ...
    Operator: TokenCategory = ...
    RegularExpressionLiteral: TokenCategory = ...
    StringLiteral: TokenCategory = ...
    value__ = ...
    WhiteSpace: TokenCategory = ...


class TokenInfo(IEquatable): # skipped bases: <type 'object'>
    """ TokenInfo(span: SourceSpan, category: TokenCategory, trigger: TokenTriggers) """
    @property
    def Category(self) -> TokenCategory:
        """
        Get: Category(self: TokenInfo) -> TokenCategory
        Set: Category(self: TokenInfo) = value
        """
        ...

    @property
    def SourceSpan(self) -> SourceSpan:
        """
        Get: SourceSpan(self: TokenInfo) -> SourceSpan
        Set: SourceSpan(self: TokenInfo) = value
        """
        ...

    @property
    def Trigger(self) -> TokenTriggers:
        """
        Get: Trigger(self: TokenInfo) -> TokenTriggers
        Set: Trigger(self: TokenInfo) = value
        """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: TokenInfo) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: TokenInfo) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TokenKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TokenKind, values: Arrow (84), Assign (72), AssignAlias (73), AssignColon (74), At (89), BackQuote (86), Backslash (93), BitwiseAnd (56), BitwiseAndEqual (57), BitwiseOr (58), BitwiseOrEqual (59), BooleanAnd (62), BooleanAndEqual (63), BooleanOr (64), BooleanOrEqual (65), CharacterLiteral (19), Colon (33), Comma (30), CompareEqual (81), Default (0), Directive (12), Div (44), DivEqual (45), Dollar (95), Dot (31), DoubleArrow (85), DoubleAt (90), DoubleBackslash (94), DoubleColon (34), DoubleDollar (96), DoubleDot (87), DoubleQuestion (92), EndOfLine (3), Equal (75), Error (1), FloatLiteral (18), FloorDivide (46), FloorDivideEqual (47), FormattedString (22), FormattedUnicodeString (23), GreaterThan (69), GreaterThanOrEqual (71), Identifier (14), Indentation (5), IntegerLiteral (17), Keyword (13), LanguageDefined (97), LeftBrace (28), LeftBracket (26), LeftParenthesis (24), LeftShift (52), LeftShiftEqual (53), LessThan (68), LessThanOrEqual (70), LineJoin (4), Match (82), Minus (39), MinusEqual (41), MinusMinus (40), Mod (48), ModEqual (49), Mul (42), MulEqual (43), MultiLineComment (7), MultiLineDocComment (11), NestableCommentEnd (9), NestableCommentStart (8), Not (77), NotEqual (78), NotMatch (83), Plus (36), PlusEqual (38), PlusPlus (37), Power (50), PowerEqual (51), Question (91), RightBrace (29), RightBracket (27), RightParenthesis (25), RightShift (54), RightShiftEqual (55), Semicolon (32), SingleLineComment (6), SingleLineDocComment (10), StrictEqual (76), StrictNotEqual (79), String (20), TripleColon (35), TripleDot (88), Twiddle (66), TwiddleEqual (67), Unequal (80), UnicodeString (21), Variable (16), VerbatimIdentifier (15), Whitespace (2), Xor (60), XorEqual (61) """
    Arrow: TokenKind = ...
    Assign: TokenKind = ...
    AssignAlias: TokenKind = ...
    AssignColon: TokenKind = ...
    At: TokenKind = ...
    BackQuote: TokenKind = ...
    Backslash: TokenKind = ...
    BitwiseAnd: TokenKind = ...
    BitwiseAndEqual: TokenKind = ...
    BitwiseOr: TokenKind = ...
    BitwiseOrEqual: TokenKind = ...
    BooleanAnd: TokenKind = ...
    BooleanAndEqual: TokenKind = ...
    BooleanOr: TokenKind = ...
    BooleanOrEqual: TokenKind = ...
    CharacterLiteral: TokenKind = ...
    Colon: TokenKind = ...
    Comma: TokenKind = ...
    CompareEqual: TokenKind = ...
    Default: TokenKind = ...
    Directive: TokenKind = ...
    Div: TokenKind = ...
    DivEqual: TokenKind = ...
    Dollar: TokenKind = ...
    Dot: TokenKind = ...
    DoubleArrow: TokenKind = ...
    DoubleAt: TokenKind = ...
    DoubleBackslash: TokenKind = ...
    DoubleColon: TokenKind = ...
    DoubleDollar: TokenKind = ...
    DoubleDot: TokenKind = ...
    DoubleQuestion: TokenKind = ...
    EndOfLine: TokenKind = ...
    Equal: TokenKind = ...
    Error: TokenKind = ...
    FloatLiteral: TokenKind = ...
    FloorDivide: TokenKind = ...
    FloorDivideEqual: TokenKind = ...
    FormattedString: TokenKind = ...
    FormattedUnicodeString: TokenKind = ...
    GreaterThan: TokenKind = ...
    GreaterThanOrEqual: TokenKind = ...
    Identifier: TokenKind = ...
    Indentation: TokenKind = ...
    IntegerLiteral: TokenKind = ...
    Keyword: TokenKind = ...
    LanguageDefined: TokenKind = ...
    LeftBrace: TokenKind = ...
    LeftBracket: TokenKind = ...
    LeftParenthesis: TokenKind = ...
    LeftShift: TokenKind = ...
    LeftShiftEqual: TokenKind = ...
    LessThan: TokenKind = ...
    LessThanOrEqual: TokenKind = ...
    LineJoin: TokenKind = ...
    Match: TokenKind = ...
    Minus: TokenKind = ...
    MinusEqual: TokenKind = ...
    MinusMinus: TokenKind = ...
    Mod: TokenKind = ...
    ModEqual: TokenKind = ...
    Mul: TokenKind = ...
    MulEqual: TokenKind = ...
    MultiLineComment: TokenKind = ...
    MultiLineDocComment: TokenKind = ...
    NestableCommentEnd: TokenKind = ...
    NestableCommentStart: TokenKind = ...
    Not: TokenKind = ...
    NotEqual: TokenKind = ...
    NotMatch: TokenKind = ...
    Plus: TokenKind = ...
    PlusEqual: TokenKind = ...
    PlusPlus: TokenKind = ...
    Power: TokenKind = ...
    PowerEqual: TokenKind = ...
    Question: TokenKind = ...
    RightBrace: TokenKind = ...
    RightBracket: TokenKind = ...
    RightParenthesis: TokenKind = ...
    RightShift: TokenKind = ...
    RightShiftEqual: TokenKind = ...
    Semicolon: TokenKind = ...
    SingleLineComment: TokenKind = ...
    SingleLineDocComment: TokenKind = ...
    StrictEqual: TokenKind = ...
    StrictNotEqual: TokenKind = ...
    String: TokenKind = ...
    TripleColon: TokenKind = ...
    TripleDot: TokenKind = ...
    Twiddle: TokenKind = ...
    TwiddleEqual: TokenKind = ...
    Unequal: TokenKind = ...
    UnicodeString: TokenKind = ...
    value__ = ...
    Variable: TokenKind = ...
    VerbatimIdentifier: TokenKind = ...
    Whitespace: TokenKind = ...
    Xor: TokenKind = ...
    XorEqual: TokenKind = ...


class TokenTriggers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TokenTriggers, values: MatchBraces (2), MemberSelect (1), MethodTip (240), None (0), Parameter (128), ParameterEnd (64), ParameterNext (32), ParameterStart (16) """
    MatchBraces: TokenTriggers = ...
    MemberSelect: TokenTriggers = ...
    MethodTip: TokenTriggers = ...
    Parameter: TokenTriggers = ...
    ParameterEnd: TokenTriggers = ...
    ParameterNext: TokenTriggers = ...
    ParameterStart: TokenTriggers = ...
    value__ = ...


# variables with complex values

