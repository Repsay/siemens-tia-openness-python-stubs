# encoding: utf-8
# module System.Activities.XamlIntegration calls itself XamlIntegration
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Action, Type

from System.Activities import (ActivityContext, Location, 
    LocationReferenceEnvironment)

from System.Activities.DynamicUpdate import DynamicUpdateMap

from System.Collections import IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import TypeConverter

from System.EnterpriseServices import Activity

from System.IO import Stream, TextWriter

from System.Linq.Expressions import Expression

from System.Windows.Markup import (IValueSerializerContext, MarkupExtension, 
    ValueSerializer)

from System.Xaml import (XamlDeferringLoader, XamlReader, XamlSchemaContext, 
    XamlWriter)

from System.Xml.Serialization import IXmlSerializable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: Func
"""

# no functions
# classes

class TypeConverterBase(TypeConverter): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ActivityWithResultConverter(TypeConverterBase): # skipped bases: <type 'object'>
    """
    ActivityWithResultConverter()
    ActivityWithResultConverter(type: Type)
    """
    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class ActivityWithResultValueSerializer(ValueSerializer): # skipped bases: <type 'object'>
    """ ActivityWithResultValueSerializer() """
    pass

class ActivityXamlServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateBuilderReader(innerReader:XamlReader, schemaContext:XamlSchemaContext = ...) -> XamlReader:
        """
        CreateBuilderReader(innerReader: XamlReader) -> XamlReader
        CreateBuilderReader(innerReader: XamlReader, schemaContext: XamlSchemaContext) -> XamlReader
        """
        ...

    @staticmethod
    def CreateBuilderWriter(innerWriter:XamlWriter) -> XamlWriter:
        """ CreateBuilderWriter(innerWriter: XamlWriter) -> XamlWriter """
        ...

    @staticmethod
    def CreateFactory(reader:XamlReader, resultType:Type = ...): # -> Func
        """
        CreateFactory(reader: XamlReader, resultType: Type) -> Func[object]
        CreateFactory[T](reader: XamlReader) -> Func[T]
        """
        ...

    @staticmethod
    def CreateReader(*__args:Stream) -> XamlReader:
        """
        CreateReader(stream: Stream) -> XamlReader
        CreateReader(innerReader: XamlReader) -> XamlReader
        CreateReader(innerReader: XamlReader, schemaContext: XamlSchemaContext) -> XamlReader
        """
        ...

    @staticmethod
    def InitializeComponent(componentType:Type, componentInstance:object): # -> 
        """ InitializeComponent(componentType: Type, componentInstance: object) """
        ...

    @staticmethod
    def Load(*__args:Stream) -> Activity:
        """
        Load(stream: Stream) -> Activity
        Load(stream: Stream, settings: ActivityXamlServicesSettings) -> Activity
        Load(fileName: str) -> Activity
        Load(fileName: str, settings: ActivityXamlServicesSettings) -> Activity
        Load(textReader: TextReader) -> Activity
        Load(textReader: TextReader, settings: ActivityXamlServicesSettings) -> Activity
        Load(xamlReader: XamlReader) -> Activity
        Load(xmlReader: XmlReader) -> Activity
        Load(xmlReader: XmlReader, settings: ActivityXamlServicesSettings) -> Activity
        Load(xamlReader: XamlReader, settings: ActivityXamlServicesSettings) -> Activity
        """
        ...

    __all__: list = ...


class ActivityXamlServicesSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ ActivityXamlServicesSettings() """
    @property
    def CompileExpressions(self) -> bool:
        """
        Get: CompileExpressions(self: ActivityXamlServicesSettings) -> bool
        Set: CompileExpressions(self: ActivityXamlServicesSettings) = value
        """
        ...

    @property
    def LocationReferenceEnvironment(self) -> LocationReferenceEnvironment:
        """
        Get: LocationReferenceEnvironment(self: ActivityXamlServicesSettings) -> LocationReferenceEnvironment
        Set: LocationReferenceEnvironment(self: ActivityXamlServicesSettings) = value
        """
        ...



class ArgumentValueSerializer(ValueSerializer): # skipped bases: <type 'object'>
    """ ArgumentValueSerializer() """
    pass

class AssemblyReferenceConverter(TypeConverter): # skipped bases: <type 'object'>
    """ AssemblyReferenceConverter() """
    pass

class CompiledDataContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetCompiledDataContextCache(self, *args): #cannot find CLR method
        """ GetCompiledDataContextCache(dataContextActivities: object, activityContext: ActivityContext, compiledRoot: Activity, forImplementation: bool, compiledDataContextCount: int) -> Array[CompiledDataContext] """
        ...

    def GetDataContextActivities(self, *args): #cannot find CLR method
        """ GetDataContextActivities(compiledRoot: Activity, forImplementation: bool) -> object """
        ...

    def GetLocation(self, getMethod, setMethod:Action, expressionId:int = ..., compiledRootActivity:Activity = ..., activityContext:ActivityContext = ...) -> Location: # Not found arg types: {'getMethod': 'Func'}
        """
        GetLocation[T](self: CompiledDataContext, getMethod: Func[T], setMethod: Action[T], expressionId: int, compiledRootActivity: Activity, activityContext: ActivityContext) -> Location[T]
        GetLocation[T](self: CompiledDataContext, getMethod: Func[T], setMethod: Action[T]) -> Location[T]
        """
        ...

    def GetValueTypeValues(self, *args): #cannot find CLR method
        """ GetValueTypeValues(self: CompiledDataContext) """
        ...

    def GetVariableValue(self, *args): #cannot find CLR method
        """ GetVariableValue(self: CompiledDataContext, index: int) -> object """
        ...

    def RewriteExpressionTree(self, *args): #cannot find CLR method
        """ RewriteExpressionTree(self: CompiledDataContext, originalExpression: Expression) -> Expression """
        ...

    def SetValueTypeValues(self, *args): #cannot find CLR method
        """ SetValueTypeValues(self: CompiledDataContext) """
        ...

    def SetVariableValue(self, *args): #cannot find CLR method
        """ SetVariableValue(self: CompiledDataContext, index: int, value: object) """
        ...


class DynamicUpdateMapConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DynamicUpdateMapConverter() """
    pass

class DynamicUpdateMapExtension(MarkupExtension): # skipped bases: <type 'object'>
    """
    DynamicUpdateMapExtension()
    DynamicUpdateMapExtension(updateMap: DynamicUpdateMap)
    """
    @property
    def UpdateMap(self) -> DynamicUpdateMap:
        """ Get: UpdateMap(self: DynamicUpdateMapExtension) -> DynamicUpdateMap """
        ...

    @property
    def XmlContent(self) -> IXmlSerializable:
        """ Get: XmlContent(self: DynamicUpdateMapExtension) -> IXmlSerializable """
        ...


    def __new__(cls, updateMap:DynamicUpdateMap = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, updateMap: DynamicUpdateMap)
        """
        ...


class DynamicUpdateMapItemConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DynamicUpdateMapItemConverter() """
    pass

class FuncDeferringLoader(XamlDeferringLoader): # skipped bases: <type 'object'>
    """ FuncDeferringLoader() """
    pass

class ICompiledExpressionRoot: # skipped bases: <type 'object'>
    """ no doc """
    def CanExecuteExpression(self, expressionText, isReference, locations, expressionId) -> Tuple_[bool, int]:
        """ CanExecuteExpression(self: ICompiledExpressionRoot, expressionText: str, isReference: bool, locations: IList[LocationReference]) -> (bool, int) """
        ...

    def GetExpressionTreeForExpression(self, expressionId:int, locationReferences:IList) -> Expression:
        """ GetExpressionTreeForExpression(self: ICompiledExpressionRoot, expressionId: int, locationReferences: IList[LocationReference]) -> Expression """
        ...

    def GetLanguage(self) -> str:
        """ GetLanguage(self: ICompiledExpressionRoot) -> str """
        ...

    def GetRequiredLocations(self, expressionId:int) -> IList:
        """ GetRequiredLocations(self: ICompiledExpressionRoot, expressionId: int) -> IList[str] """
        ...

    def InvokeExpression(self, expressionId:int, locations:IList, activityContext:ActivityContext = ...) -> object:
        """
        InvokeExpression(self: ICompiledExpressionRoot, expressionId: int, locations: IList[LocationReference], activityContext: ActivityContext) -> object
        InvokeExpression(self: ICompiledExpressionRoot, expressionId: int, locations: IList[Location]) -> object
        """
        ...


class ImplementationVersionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ImplementationVersionConverter() """
    pass

class InArgumentConverter(TypeConverterBase): # skipped bases: <type 'object'>
    """
    InArgumentConverter()
    InArgumentConverter(type: Type)
    """
    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class InOutArgumentConverter(TypeConverterBase): # skipped bases: <type 'object'>
    """
    InOutArgumentConverter()
    InOutArgumentConverter(type: Type)
    """
    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class IValueSerializableExpression: # skipped bases: <type 'object'>
    """ no doc """
    def CanConvertToString(self, context:IValueSerializerContext) -> bool:
        """ CanConvertToString(self: IValueSerializableExpression, context: IValueSerializerContext) -> bool """
        ...

    def ConvertToString(self, context:IValueSerializerContext) -> str:
        """ ConvertToString(self: IValueSerializableExpression, context: IValueSerializerContext) -> str """
        ...


class OutArgumentConverter(TypeConverterBase): # skipped bases: <type 'object'>
    """
    OutArgumentConverter()
    OutArgumentConverter(type: Type)
    """
    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class PropertyReferenceExtension(MarkupExtension): # skipped bases: <type 'object'>
    """ PropertyReferenceExtension[T]() """
    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: PropertyReferenceExtension[T]) -> str
        Set: PropertyName(self: PropertyReferenceExtension[T]) = value
        """
        ...



class SerializableFuncDeferringLoader(XamlDeferringLoader): # skipped bases: <type 'object'>
    """ SerializableFuncDeferringLoader() """
    pass

class TextExpressionCompiler: # skipped bases: <type 'object'>, <type 'object'>
    """ TextExpressionCompiler(settings: TextExpressionCompilerSettings) """
    def Compile(self) -> TextExpressionCompilerResults:
        """ Compile(self: TextExpressionCompiler) -> TextExpressionCompilerResults """
        ...

    def GenerateSource(self, textWriter:TextWriter) -> bool:
        """ GenerateSource(self: TextExpressionCompiler, textWriter: TextWriter) -> bool """
        ...


class TextExpressionCompilerError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: TextExpressionCompilerError) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: TextExpressionCompilerError) -> str """
        ...

    @property
    def Number(self) -> str:
        """ Get: Number(self: TextExpressionCompilerError) -> str """
        ...

    @property
    def SourceLineNumber(self) -> int:
        """ Get: SourceLineNumber(self: TextExpressionCompilerError) -> int """
        ...



class TextExpressionCompilerResults: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CompilerMessages(self) -> ReadOnlyCollection:
        """ Get: CompilerMessages(self: TextExpressionCompilerResults) -> ReadOnlyCollection[TextExpressionCompilerError] """
        ...

    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: TextExpressionCompilerResults) -> bool """
        ...

    @property
    def HasSourceInfo(self) -> bool:
        """ Get: HasSourceInfo(self: TextExpressionCompilerResults) -> bool """
        ...

    @property
    def ResultType(self) -> Type:
        """ Get: ResultType(self: TextExpressionCompilerResults) -> Type """
        ...



class TextExpressionCompilerSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ TextExpressionCompilerSettings() """
    @property
    def Activity(self) -> Activity:
        """
        Get: Activity(self: TextExpressionCompilerSettings) -> Activity
        Set: Activity(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: TextExpressionCompilerSettings) -> str
        Set: ActivityName(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def ActivityNamespace(self) -> str:
        """
        Get: ActivityNamespace(self: TextExpressionCompilerSettings) -> str
        Set: ActivityNamespace(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def AlwaysGenerateSource(self) -> bool:
        """
        Get: AlwaysGenerateSource(self: TextExpressionCompilerSettings) -> bool
        Set: AlwaysGenerateSource(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def ForImplementation(self) -> bool:
        """
        Get: ForImplementation(self: TextExpressionCompilerSettings) -> bool
        Set: ForImplementation(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def GenerateAsPartialClass(self) -> bool:
        """
        Get: GenerateAsPartialClass(self: TextExpressionCompilerSettings) -> bool
        Set: GenerateAsPartialClass(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: TextExpressionCompilerSettings) -> str
        Set: Language(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def LogSourceGenerationMessage(self) -> Action:
        """
        Get: LogSourceGenerationMessage(self: TextExpressionCompilerSettings) -> Action[str]
        Set: LogSourceGenerationMessage(self: TextExpressionCompilerSettings) = value
        """
        ...

    @property
    def RootNamespace(self) -> str:
        """
        Get: RootNamespace(self: TextExpressionCompilerSettings) -> str
        Set: RootNamespace(self: TextExpressionCompilerSettings) = value
        """
        ...



class WorkflowIdentityConverter(TypeConverter): # skipped bases: <type 'object'>
    """ WorkflowIdentityConverter() """
    pass

