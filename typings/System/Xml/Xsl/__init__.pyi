# encoding: utf-8
# module System.Xml.Xsl calls itself Xsl
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.SqlXml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, EventArgs, IAsyncResult, 
    MulticastDelegate, SystemException)

from System.CodeDom.Compiler import (CompilerErrorCollection, 
    TempFileCollection)

from System.Reflection.Emit import TypeBuilder

from System.Xml import (XmlNamespaceManager, XmlReader, XmlResolver, 
    XmlWriter, XmlWriterSettings)

from System.Xml.XPath import (IXPathNavigable, XPathNavigator, 
    XPathResultType)

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class IXsltContextFunction: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgTypes(self) -> Array:
        """ Get: ArgTypes(self: IXsltContextFunction) -> Array[XPathResultType] """
        ...

    @property
    def Maxargs(self) -> int:
        """ Get: Maxargs(self: IXsltContextFunction) -> int """
        ...

    @property
    def Minargs(self) -> int:
        """ Get: Minargs(self: IXsltContextFunction) -> int """
        ...

    @property
    def ReturnType(self) -> XPathResultType:
        """ Get: ReturnType(self: IXsltContextFunction) -> XPathResultType """
        ...


    def Invoke(self, xsltContext:XsltContext, args:Array, docContext:XPathNavigator) -> object:
        """ Invoke(self: IXsltContextFunction, xsltContext: XsltContext, args: Array[object], docContext: XPathNavigator) -> object """
        ...


class IXsltContextVariable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: IXsltContextVariable) -> bool """
        ...

    @property
    def IsParam(self) -> bool:
        """ Get: IsParam(self: IXsltContextVariable) -> bool """
        ...

    @property
    def VariableType(self) -> XPathResultType:
        """ Get: VariableType(self: IXsltContextVariable) -> XPathResultType """
        ...


    def Evaluate(self, xsltContext:XsltContext) -> object:
        """ Evaluate(self: IXsltContextVariable, xsltContext: XsltContext) -> object """
        ...


class XslCompiledTransform: # skipped bases: <type 'object'>, <type 'object'>
    """
    XslCompiledTransform()
    XslCompiledTransform(enableDebug: bool)
    """
    @property
    def OutputSettings(self) -> XmlWriterSettings:
        """ Get: OutputSettings(self: XslCompiledTransform) -> XmlWriterSettings """
        ...

    @property
    def TemporaryFiles(self) -> TempFileCollection:
        """ Get: TemporaryFiles(self: XslCompiledTransform) -> TempFileCollection """
        ...


    @staticmethod
    def CompileToType(stylesheet:XmlReader, settings:XsltSettings, stylesheetResolver:XmlResolver, debug:bool, typeBuilder:TypeBuilder, scriptAssemblyPath:str) -> CompilerErrorCollection:
        """ CompileToType(stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver, debug: bool, typeBuilder: TypeBuilder, scriptAssemblyPath: str) -> CompilerErrorCollection """
        ...

    def Load(self, *__args:XmlReader): # -> 
        """ Load(self: XslCompiledTransform, stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver)Load(self: XslCompiledTransform, stylesheet: IXPathNavigable, settings: XsltSettings, stylesheetResolver: XmlResolver)Load(self: XslCompiledTransform, stylesheetUri: str, settings: XsltSettings, stylesheetResolver: XmlResolver)Load(self: XslCompiledTransform, stylesheet: XmlReader)Load(self: XslCompiledTransform, stylesheet: IXPathNavigable)Load(self: XslCompiledTransform, stylesheetUri: str)Load(self: XslCompiledTransform, compiledStylesheet: Type)Load(self: XslCompiledTransform, executeMethod: MethodInfo, queryData: Array[Byte], earlyBoundTypes: Array[Type]) """
        ...

    def Transform(self, *__args): # -> 
        """ Transform(self: XslCompiledTransform, input: IXPathNavigable, results: XmlWriter)Transform(self: XslCompiledTransform, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter)Transform(self: XslCompiledTransform, input: IXPathNavigable, arguments: XsltArgumentList, results: TextWriter)Transform(self: XslCompiledTransform, input: IXPathNavigable, arguments: XsltArgumentList, results: Stream)Transform(self: XslCompiledTransform, input: XmlReader, results: XmlWriter)Transform(self: XslCompiledTransform, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter)Transform(self: XslCompiledTransform, input: XmlReader, arguments: XsltArgumentList, results: TextWriter)Transform(self: XslCompiledTransform, input: XmlReader, arguments: XsltArgumentList, results: Stream)Transform(self: XslCompiledTransform, inputUri: str, results: XmlWriter)Transform(self: XslCompiledTransform, inputUri: str, arguments: XsltArgumentList, results: XmlWriter)Transform(self: XslCompiledTransform, inputUri: str, arguments: XsltArgumentList, results: TextWriter)Transform(self: XslCompiledTransform, inputUri: str, arguments: XsltArgumentList, results: Stream)Transform(self: XslCompiledTransform, inputUri: str, resultsFile: str)Transform(self: XslCompiledTransform, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver)Transform(self: XslCompiledTransform, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) """
        ...


class XsltArgumentList: # skipped bases: <type 'object'>, <type 'object'>
    """ XsltArgumentList() """
    def AddExtensionObject(self, namespaceUri:str, extension:object): # -> 
        """ AddExtensionObject(self: XsltArgumentList, namespaceUri: str, extension: object) """
        ...

    def AddParam(self, name:str, namespaceUri:str, parameter:object): # -> 
        """ AddParam(self: XsltArgumentList, name: str, namespaceUri: str, parameter: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: XsltArgumentList) """
        ...

    def GetExtensionObject(self, namespaceUri:str) -> object:
        """ GetExtensionObject(self: XsltArgumentList, namespaceUri: str) -> object """
        ...

    def GetParam(self, name:str, namespaceUri:str) -> object:
        """ GetParam(self: XsltArgumentList, name: str, namespaceUri: str) -> object """
        ...

    def RemoveExtensionObject(self, namespaceUri:str) -> object:
        """ RemoveExtensionObject(self: XsltArgumentList, namespaceUri: str) -> object """
        ...

    def RemoveParam(self, name:str, namespaceUri:str) -> object:
        """ RemoveParam(self: XsltArgumentList, name: str, namespaceUri: str) -> object """
        ...

    XsltMessageEncountered = ...


class XsltException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XsltException()
    XsltException(message: str)
    XsltException(message: str, innerException: Exception)
    """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XsltException) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XsltException) -> int """
        ...

    @property
    def SourceUri(self) -> str:
        """ Get: SourceUri(self: XsltException) -> str """
        ...


    SerializeObjectState = ...


class XsltCompileException(XsltException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XsltCompileException()
    XsltCompileException(message: str)
    XsltCompileException(message: str, innerException: Exception)
    XsltCompileException(inner: Exception, sourceUri: str, lineNumber: int, linePosition: int)
    """
    SerializeObjectState = ...


class XsltContext(XmlNamespaceManager): # skipped bases: <type 'IXmlNamespaceResolver'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Whitespace(self) -> bool:
        """ Get: Whitespace(self: XsltContext) -> bool """
        ...


    def CompareDocument(self, baseUri:str, nextbaseUri:str) -> int:
        """ CompareDocument(self: XsltContext, baseUri: str, nextbaseUri: str) -> int """
        ...

    def PreserveWhitespace(self, node:XPathNavigator) -> bool:
        """ PreserveWhitespace(self: XsltContext, node: XPathNavigator) -> bool """
        ...

    def ResolveFunction(self, prefix:str, name:str, ArgTypes:Array) -> IXsltContextFunction:
        """ ResolveFunction(self: XsltContext, prefix: str, name: str, ArgTypes: Array[XPathResultType]) -> IXsltContextFunction """
        ...

    def ResolveVariable(self, prefix:str, name:str) -> IXsltContextVariable:
        """ ResolveVariable(self: XsltContext, prefix: str, name: str) -> IXsltContextVariable """
        ...


class XsltMessageEncounteredEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: XsltMessageEncounteredEventArgs) -> str """
        ...



class XsltMessageEncounteredEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XsltMessageEncounteredEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:XsltMessageEncounteredEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XsltMessageEncounteredEventHandler, sender: object, e: XsltMessageEncounteredEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XsltMessageEncounteredEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:XsltMessageEncounteredEventArgs): # -> 
        """ Invoke(self: XsltMessageEncounteredEventHandler, sender: object, e: XsltMessageEncounteredEventArgs) """
        ...


class XslTransform: # skipped bases: <type 'object'>, <type 'object'>
    """ XslTransform() """
    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XslTransform) = value """
        ...


    def Load(self, *__args:str): # -> 
        """ Load(self: XslTransform, url: str)Load(self: XslTransform, stylesheet: XmlReader, resolver: XmlResolver)Load(self: XslTransform, stylesheet: IXPathNavigable, resolver: XmlResolver)Load(self: XslTransform, stylesheet: XPathNavigator, resolver: XmlResolver)Load(self: XslTransform, stylesheet: IXPathNavigable, resolver: XmlResolver, evidence: Evidence)Load(self: XslTransform, stylesheet: XmlReader, resolver: XmlResolver, evidence: Evidence)Load(self: XslTransform, stylesheet: XPathNavigator, resolver: XmlResolver, evidence: Evidence)Load(self: XslTransform, stylesheet: XmlReader)Load(self: XslTransform, stylesheet: IXPathNavigable)Load(self: XslTransform, stylesheet: XPathNavigator)Load(self: XslTransform, url: str, resolver: XmlResolver) """
        ...

    def Transform(self, *__args) -> XmlReader:
        """
        Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader
        Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: Stream)Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: TextWriter)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: Stream)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: Stream, resolver: XmlResolver)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver)Transform(self: XslTransform, input: XPathNavigator, args: XsltArgumentList) -> XmlReader
        Transform(self: XslTransform, inputfile: str, outputfile: str, resolver: XmlResolver)Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver)Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: Stream, resolver: XmlResolver)Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver)Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader
        Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList) -> XmlReader
        Transform(self: XslTransform, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter)Transform(self: XslTransform, inputfile: str, outputfile: str)
        """
        ...


class XsltSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    XsltSettings()
    XsltSettings(enableDocumentFunction: bool, enableScript: bool)
    """
    @property
    def Default(self) -> XsltSettings:
        """ Get: Default() -> XsltSettings """
        ...

    @property
    def EnableDocumentFunction(self) -> bool:
        """
        Get: EnableDocumentFunction(self: XsltSettings) -> bool
        Set: EnableDocumentFunction(self: XsltSettings) = value
        """
        ...

    @property
    def EnableScript(self) -> bool:
        """
        Get: EnableScript(self: XsltSettings) -> bool
        Set: EnableScript(self: XsltSettings) = value
        """
        ...

    @property
    def TrustedXslt(self) -> XsltSettings:
        """ Get: TrustedXslt() -> XsltSettings """
        ...




# variables with complex values

