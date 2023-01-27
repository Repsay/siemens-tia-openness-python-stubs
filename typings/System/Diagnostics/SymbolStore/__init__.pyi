# encoding: utf-8
# module System.Diagnostics.SymbolStore calls itself SymbolStore
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Guid, IntPtr

from System.Reflection import FieldAttributes, ParameterAttributes

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ISymbolBinder: # skipped bases: <type 'object'>
    """ no doc """
    def GetReader(self, importer:int, filename:str, searchPath:str) -> ISymbolReader:
        """ GetReader(self: ISymbolBinder, importer: int, filename: str, searchPath: str) -> ISymbolReader """
        ...


class ISymbolBinder1: # skipped bases: <type 'object'>
    """ no doc """
    def GetReader(self, importer:IntPtr, filename:str, searchPath:str) -> ISymbolReader:
        """ GetReader(self: ISymbolBinder1, importer: IntPtr, filename: str, searchPath: str) -> ISymbolReader """
        ...


class ISymbolDocument: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CheckSumAlgorithmId(self) -> Guid:
        """ Get: CheckSumAlgorithmId(self: ISymbolDocument) -> Guid """
        ...

    @property
    def DocumentType(self) -> Guid:
        """ Get: DocumentType(self: ISymbolDocument) -> Guid """
        ...

    @property
    def HasEmbeddedSource(self) -> bool:
        """ Get: HasEmbeddedSource(self: ISymbolDocument) -> bool """
        ...

    @property
    def Language(self) -> Guid:
        """ Get: Language(self: ISymbolDocument) -> Guid """
        ...

    @property
    def LanguageVendor(self) -> Guid:
        """ Get: LanguageVendor(self: ISymbolDocument) -> Guid """
        ...

    @property
    def SourceLength(self) -> int:
        """ Get: SourceLength(self: ISymbolDocument) -> int """
        ...

    @property
    def URL(self) -> str:
        """ Get: URL(self: ISymbolDocument) -> str """
        ...


    def FindClosestLine(self, line:int) -> int:
        """ FindClosestLine(self: ISymbolDocument, line: int) -> int """
        ...

    def GetCheckSum(self) -> Array:
        """ GetCheckSum(self: ISymbolDocument) -> Array[Byte] """
        ...

    def GetSourceRange(self, startLine:int, startColumn:int, endLine:int, endColumn:int) -> Array:
        """ GetSourceRange(self: ISymbolDocument, startLine: int, startColumn: int, endLine: int, endColumn: int) -> Array[Byte] """
        ...


class ISymbolDocumentWriter: # skipped bases: <type 'object'>
    """ no doc """
    def SetCheckSum(self, algorithmId:Guid, checkSum:Array): # -> 
        """ SetCheckSum(self: ISymbolDocumentWriter, algorithmId: Guid, checkSum: Array[Byte]) """
        ...

    def SetSource(self, source:Array): # -> 
        """ SetSource(self: ISymbolDocumentWriter, source: Array[Byte]) """
        ...


class ISymbolMethod: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RootScope(self) -> ISymbolScope:
        """ Get: RootScope(self: ISymbolMethod) -> ISymbolScope """
        ...

    @property
    def SequencePointCount(self) -> int:
        """ Get: SequencePointCount(self: ISymbolMethod) -> int """
        ...

    @property
    def Token(self) -> SymbolToken:
        """ Get: Token(self: ISymbolMethod) -> SymbolToken """
        ...


    def GetNamespace(self) -> ISymbolNamespace:
        """ GetNamespace(self: ISymbolMethod) -> ISymbolNamespace """
        ...

    def GetOffset(self, document:ISymbolDocument, line:int, column:int) -> int:
        """ GetOffset(self: ISymbolMethod, document: ISymbolDocument, line: int, column: int) -> int """
        ...

    def GetParameters(self) -> Array:
        """ GetParameters(self: ISymbolMethod) -> Array[ISymbolVariable] """
        ...

    def GetRanges(self, document:ISymbolDocument, line:int, column:int) -> Array:
        """ GetRanges(self: ISymbolMethod, document: ISymbolDocument, line: int, column: int) -> Array[int] """
        ...

    def GetScope(self, offset:int) -> ISymbolScope:
        """ GetScope(self: ISymbolMethod, offset: int) -> ISymbolScope """
        ...

    def GetSequencePoints(self, offsets:Array, documents:Array, lines:Array, columns:Array, endLines:Array, endColumns:Array): # -> 
        """ GetSequencePoints(self: ISymbolMethod, offsets: Array[int], documents: Array[ISymbolDocument], lines: Array[int], columns: Array[int], endLines: Array[int], endColumns: Array[int]) """
        ...

    def GetSourceStartEnd(self, docs:Array, lines:Array, columns:Array) -> bool:
        """ GetSourceStartEnd(self: ISymbolMethod, docs: Array[ISymbolDocument], lines: Array[int], columns: Array[int]) -> bool """
        ...


class ISymbolNamespace: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ISymbolNamespace) -> str """
        ...


    def GetNamespaces(self) -> Array:
        """ GetNamespaces(self: ISymbolNamespace) -> Array[ISymbolNamespace] """
        ...

    def GetVariables(self) -> Array:
        """ GetVariables(self: ISymbolNamespace) -> Array[ISymbolVariable] """
        ...


class ISymbolReader: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def UserEntryPoint(self) -> SymbolToken:
        """ Get: UserEntryPoint(self: ISymbolReader) -> SymbolToken """
        ...


    def GetDocument(self, url:str, language:Guid, languageVendor:Guid, documentType:Guid) -> ISymbolDocument:
        """ GetDocument(self: ISymbolReader, url: str, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocument """
        ...

    def GetDocuments(self) -> Array:
        """ GetDocuments(self: ISymbolReader) -> Array[ISymbolDocument] """
        ...

    def GetGlobalVariables(self) -> Array:
        """ GetGlobalVariables(self: ISymbolReader) -> Array[ISymbolVariable] """
        ...

    def GetMethod(self, method:SymbolToken, version:int = ...) -> ISymbolMethod:
        """
        GetMethod(self: ISymbolReader, method: SymbolToken) -> ISymbolMethod
        GetMethod(self: ISymbolReader, method: SymbolToken, version: int) -> ISymbolMethod
        """
        ...

    def GetMethodFromDocumentPosition(self, document:ISymbolDocument, line:int, column:int) -> ISymbolMethod:
        """ GetMethodFromDocumentPosition(self: ISymbolReader, document: ISymbolDocument, line: int, column: int) -> ISymbolMethod """
        ...

    def GetNamespaces(self) -> Array:
        """ GetNamespaces(self: ISymbolReader) -> Array[ISymbolNamespace] """
        ...

    def GetSymAttribute(self, parent:SymbolToken, name:str) -> Array:
        """ GetSymAttribute(self: ISymbolReader, parent: SymbolToken, name: str) -> Array[Byte] """
        ...

    def GetVariables(self, parent:SymbolToken) -> Array:
        """ GetVariables(self: ISymbolReader, parent: SymbolToken) -> Array[ISymbolVariable] """
        ...


class ISymbolScope: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EndOffset(self) -> int:
        """ Get: EndOffset(self: ISymbolScope) -> int """
        ...

    @property
    def Method(self) -> ISymbolMethod:
        """ Get: Method(self: ISymbolScope) -> ISymbolMethod """
        ...

    @property
    def Parent(self) -> ISymbolScope:
        """ Get: Parent(self: ISymbolScope) -> ISymbolScope """
        ...

    @property
    def StartOffset(self) -> int:
        """ Get: StartOffset(self: ISymbolScope) -> int """
        ...


    def GetChildren(self) -> Array:
        """ GetChildren(self: ISymbolScope) -> Array[ISymbolScope] """
        ...

    def GetLocals(self) -> Array:
        """ GetLocals(self: ISymbolScope) -> Array[ISymbolVariable] """
        ...

    def GetNamespaces(self) -> Array:
        """ GetNamespaces(self: ISymbolScope) -> Array[ISymbolNamespace] """
        ...


class ISymbolVariable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AddressField1(self) -> int:
        """ Get: AddressField1(self: ISymbolVariable) -> int """
        ...

    @property
    def AddressField2(self) -> int:
        """ Get: AddressField2(self: ISymbolVariable) -> int """
        ...

    @property
    def AddressField3(self) -> int:
        """ Get: AddressField3(self: ISymbolVariable) -> int """
        ...

    @property
    def AddressKind(self) -> SymAddressKind:
        """ Get: AddressKind(self: ISymbolVariable) -> SymAddressKind """
        ...

    @property
    def Attributes(self) -> object:
        """ Get: Attributes(self: ISymbolVariable) -> object """
        ...

    @property
    def EndOffset(self) -> int:
        """ Get: EndOffset(self: ISymbolVariable) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ISymbolVariable) -> str """
        ...

    @property
    def StartOffset(self) -> int:
        """ Get: StartOffset(self: ISymbolVariable) -> int """
        ...


    def GetSignature(self) -> Array:
        """ GetSignature(self: ISymbolVariable) -> Array[Byte] """
        ...


class ISymbolWriter: # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: ISymbolWriter) """
        ...

    def CloseMethod(self): # -> 
        """ CloseMethod(self: ISymbolWriter) """
        ...

    def CloseNamespace(self): # -> 
        """ CloseNamespace(self: ISymbolWriter) """
        ...

    def CloseScope(self, endOffset:int): # -> 
        """ CloseScope(self: ISymbolWriter, endOffset: int) """
        ...

    def DefineDocument(self, url:str, language:Guid, languageVendor:Guid, documentType:Guid) -> ISymbolDocumentWriter:
        """ DefineDocument(self: ISymbolWriter, url: str, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocumentWriter """
        ...

    def DefineField(self, parent:SymbolToken, name:str, attributes:FieldAttributes, signature:Array, addrKind:SymAddressKind, addr1:int, addr2:int, addr3:int): # -> 
        """ DefineField(self: ISymbolWriter, parent: SymbolToken, name: str, attributes: FieldAttributes, signature: Array[Byte], addrKind: SymAddressKind, addr1: int, addr2: int, addr3: int) """
        ...

    def DefineGlobalVariable(self, name:str, attributes:FieldAttributes, signature:Array, addrKind:SymAddressKind, addr1:int, addr2:int, addr3:int): # -> 
        """ DefineGlobalVariable(self: ISymbolWriter, name: str, attributes: FieldAttributes, signature: Array[Byte], addrKind: SymAddressKind, addr1: int, addr2: int, addr3: int) """
        ...

    def DefineLocalVariable(self, name:str, attributes:FieldAttributes, signature:Array, addrKind:SymAddressKind, addr1:int, addr2:int, addr3:int, startOffset:int, endOffset:int): # -> 
        """ DefineLocalVariable(self: ISymbolWriter, name: str, attributes: FieldAttributes, signature: Array[Byte], addrKind: SymAddressKind, addr1: int, addr2: int, addr3: int, startOffset: int, endOffset: int) """
        ...

    def DefineParameter(self, name:str, attributes:ParameterAttributes, sequence:int, addrKind:SymAddressKind, addr1:int, addr2:int, addr3:int): # -> 
        """ DefineParameter(self: ISymbolWriter, name: str, attributes: ParameterAttributes, sequence: int, addrKind: SymAddressKind, addr1: int, addr2: int, addr3: int) """
        ...

    def DefineSequencePoints(self, document:ISymbolDocumentWriter, offsets:Array, lines:Array, columns:Array, endLines:Array, endColumns:Array): # -> 
        """ DefineSequencePoints(self: ISymbolWriter, document: ISymbolDocumentWriter, offsets: Array[int], lines: Array[int], columns: Array[int], endLines: Array[int], endColumns: Array[int]) """
        ...

    def Initialize(self, emitter:IntPtr, filename:str, fFullBuild:bool): # -> 
        """ Initialize(self: ISymbolWriter, emitter: IntPtr, filename: str, fFullBuild: bool) """
        ...

    def OpenMethod(self, method:SymbolToken): # -> 
        """ OpenMethod(self: ISymbolWriter, method: SymbolToken) """
        ...

    def OpenNamespace(self, name:str): # -> 
        """ OpenNamespace(self: ISymbolWriter, name: str) """
        ...

    def OpenScope(self, startOffset:int) -> int:
        """ OpenScope(self: ISymbolWriter, startOffset: int) -> int """
        ...

    def SetMethodSourceRange(self, startDoc:ISymbolDocumentWriter, startLine:int, startColumn:int, endDoc:ISymbolDocumentWriter, endLine:int, endColumn:int): # -> 
        """ SetMethodSourceRange(self: ISymbolWriter, startDoc: ISymbolDocumentWriter, startLine: int, startColumn: int, endDoc: ISymbolDocumentWriter, endLine: int, endColumn: int) """
        ...

    def SetScopeRange(self, scopeID:int, startOffset:int, endOffset:int): # -> 
        """ SetScopeRange(self: ISymbolWriter, scopeID: int, startOffset: int, endOffset: int) """
        ...

    def SetSymAttribute(self, parent:SymbolToken, name:str, data:Array): # -> 
        """ SetSymAttribute(self: ISymbolWriter, parent: SymbolToken, name: str, data: Array[Byte]) """
        ...

    def SetUnderlyingWriter(self, underlyingWriter:IntPtr): # -> 
        """ SetUnderlyingWriter(self: ISymbolWriter, underlyingWriter: IntPtr) """
        ...

    def SetUserEntryPoint(self, entryMethod:SymbolToken): # -> 
        """ SetUserEntryPoint(self: ISymbolWriter, entryMethod: SymbolToken) """
        ...

    def UsingNamespace(self, fullName:str): # -> 
        """ UsingNamespace(self: ISymbolWriter, fullName: str) """
        ...


class SymAddressKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SymAddressKind, values: BitField (9), ILOffset (1), NativeOffset (5), NativeRegister (3), NativeRegisterRegister (6), NativeRegisterRelative (4), NativeRegisterStack (7), NativeRVA (2), NativeSectionOffset (10), NativeStackRegister (8) """
    BitField: SymAddressKind = ...
    ILOffset: SymAddressKind = ...
    NativeOffset: SymAddressKind = ...
    NativeRegister: SymAddressKind = ...
    NativeRegisterRegister: SymAddressKind = ...
    NativeRegisterRelative: SymAddressKind = ...
    NativeRegisterStack: SymAddressKind = ...
    NativeRVA: SymAddressKind = ...
    NativeSectionOffset: SymAddressKind = ...
    NativeStackRegister: SymAddressKind = ...
    value__ = ...


class SymbolToken: # skipped bases: <type 'object'>, <type 'object'>
    """ SymbolToken(val: int) """
    def Equals(self, obj:object) -> bool:
        """
        Equals(self: SymbolToken, obj: object) -> bool
        Equals(self: SymbolToken, obj: SymbolToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SymbolToken) -> int """
        ...

    def GetToken(self) -> int:
        """ GetToken(self: SymbolToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SymDocumentType: # skipped bases: <type 'object'>, <type 'object'>
    """ SymDocumentType() """
    Text: Guid = ...


class SymLanguageType: # skipped bases: <type 'object'>, <type 'object'>
    """ SymLanguageType() """
    Basic: Guid = ...
    C: Guid = ...
    Cobol: Guid = ...
    CPlusPlus: Guid = ...
    CSharp: Guid = ...
    ILAssembly: Guid = ...
    Java: Guid = ...
    JScript: Guid = ...
    MCPlusPlus: Guid = ...
    Pascal: Guid = ...
    SMC: Guid = ...


class SymLanguageVendor: # skipped bases: <type 'object'>, <type 'object'>
    """ SymLanguageVendor() """
    Microsoft: Guid = ...


