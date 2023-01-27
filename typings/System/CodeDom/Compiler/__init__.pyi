# encoding: utf-8
# module System.CodeDom.Compiler calls itself Compiler
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, IDisposable, IntPtr, Type

from System.CodeDom import (CodeCompileUnit, CodeExpression, CodeNamespace, 
    CodeObject, CodeStatement, CodeTypeDeclaration, CodeTypeMember, 
    CodeTypeReference)

from System.Collections import (CollectionBase, ICollection, IDictionary, 
    IEnumerator)

from System.Collections.Specialized import StringCollection

from System.ComponentModel import Component, TypeConverter

from System.IO import TextReader, TextWriter

from System.Reflection import Assembly

from System.Security.Policy import Evidence

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ICodeGenerator: # skipped bases: <type 'object'>
    """ no doc """
    def CreateEscapedIdentifier(self, value:str) -> str:
        """ CreateEscapedIdentifier(self: ICodeGenerator, value: str) -> str """
        ...

    def CreateValidIdentifier(self, value:str) -> str:
        """ CreateValidIdentifier(self: ICodeGenerator, value: str) -> str """
        ...

    def GenerateCodeFromCompileUnit(self, e:CodeCompileUnit, w:TextWriter, o:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromCompileUnit(self: ICodeGenerator, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromExpression(self, e:CodeExpression, w:TextWriter, o:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromExpression(self: ICodeGenerator, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromNamespace(self, e:CodeNamespace, w:TextWriter, o:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromNamespace(self: ICodeGenerator, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromStatement(self, e:CodeStatement, w:TextWriter, o:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromStatement(self: ICodeGenerator, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromType(self, e:CodeTypeDeclaration, w:TextWriter, o:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromType(self: ICodeGenerator, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions) """
        ...

    def GetTypeOutput(self, type:CodeTypeReference) -> str:
        """ GetTypeOutput(self: ICodeGenerator, type: CodeTypeReference) -> str """
        ...

    def IsValidIdentifier(self, value:str) -> bool:
        """ IsValidIdentifier(self: ICodeGenerator, value: str) -> bool """
        ...

    def Supports(self, supports:GeneratorSupport) -> bool:
        """ Supports(self: ICodeGenerator, supports: GeneratorSupport) -> bool """
        ...

    def ValidateIdentifier(self, value:str): # -> 
        """ ValidateIdentifier(self: ICodeGenerator, value: str) """
        ...


class CodeGenerator(ICodeGenerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentClass(self):
        ...

    @property
    def CurrentMember(self):
        ...

    @property
    def CurrentMemberName(self):
        ...

    @property
    def CurrentTypeName(self):
        ...

    @property
    def Indent(self):
        ...

    @property
    def IsCurrentClass(self):
        ...

    @property
    def IsCurrentDelegate(self):
        ...

    @property
    def IsCurrentEnum(self):
        ...

    @property
    def IsCurrentInterface(self):
        ...

    @property
    def IsCurrentStruct(self):
        ...

    @property
    def NullToken(self):
        ...

    @property
    def Options(self):
        ...

    @property
    def Output(self):
        ...


    def ContinueOnNewLine(self, *args): #cannot find CLR method
        """ ContinueOnNewLine(self: CodeGenerator, st: str) """
        ...

    def GenerateArgumentReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateArgumentReferenceExpression(self: CodeGenerator, e: CodeArgumentReferenceExpression) """
        ...

    def GenerateArrayCreateExpression(self, *args): #cannot find CLR method
        """ GenerateArrayCreateExpression(self: CodeGenerator, e: CodeArrayCreateExpression) """
        ...

    def GenerateArrayIndexerExpression(self, *args): #cannot find CLR method
        """ GenerateArrayIndexerExpression(self: CodeGenerator, e: CodeArrayIndexerExpression) """
        ...

    def GenerateAssignStatement(self, *args): #cannot find CLR method
        """ GenerateAssignStatement(self: CodeGenerator, e: CodeAssignStatement) """
        ...

    def GenerateAttachEventStatement(self, *args): #cannot find CLR method
        """ GenerateAttachEventStatement(self: CodeGenerator, e: CodeAttachEventStatement) """
        ...

    def GenerateAttributeDeclarationsEnd(self, *args): #cannot find CLR method
        """ GenerateAttributeDeclarationsEnd(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection) """
        ...

    def GenerateAttributeDeclarationsStart(self, *args): #cannot find CLR method
        """ GenerateAttributeDeclarationsStart(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection) """
        ...

    def GenerateBaseReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateBaseReferenceExpression(self: CodeGenerator, e: CodeBaseReferenceExpression) """
        ...

    def GenerateBinaryOperatorExpression(self, *args): #cannot find CLR method
        """ GenerateBinaryOperatorExpression(self: CodeGenerator, e: CodeBinaryOperatorExpression) """
        ...

    def GenerateCastExpression(self, *args): #cannot find CLR method
        """ GenerateCastExpression(self: CodeGenerator, e: CodeCastExpression) """
        ...

    def GenerateCodeFromMember(self, member:CodeTypeMember, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromMember(self: CodeGenerator, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateComment(self, *args): #cannot find CLR method
        """ GenerateComment(self: CodeGenerator, e: CodeComment) """
        ...

    def GenerateCommentStatement(self, *args): #cannot find CLR method
        """ GenerateCommentStatement(self: CodeGenerator, e: CodeCommentStatement) """
        ...

    def GenerateCommentStatements(self, *args): #cannot find CLR method
        """ GenerateCommentStatements(self: CodeGenerator, e: CodeCommentStatementCollection) """
        ...

    def GenerateCompileUnit(self, *args): #cannot find CLR method
        """ GenerateCompileUnit(self: CodeGenerator, e: CodeCompileUnit) """
        ...

    def GenerateCompileUnitEnd(self, *args): #cannot find CLR method
        """ GenerateCompileUnitEnd(self: CodeGenerator, e: CodeCompileUnit) """
        ...

    def GenerateCompileUnitStart(self, *args): #cannot find CLR method
        """ GenerateCompileUnitStart(self: CodeGenerator, e: CodeCompileUnit) """
        ...

    def GenerateConditionStatement(self, *args): #cannot find CLR method
        """ GenerateConditionStatement(self: CodeGenerator, e: CodeConditionStatement) """
        ...

    def GenerateConstructor(self, *args): #cannot find CLR method
        """ GenerateConstructor(self: CodeGenerator, e: CodeConstructor, c: CodeTypeDeclaration) """
        ...

    def GenerateDecimalValue(self, *args): #cannot find CLR method
        """ GenerateDecimalValue(self: CodeGenerator, d: Decimal) """
        ...

    def GenerateDefaultValueExpression(self, *args): #cannot find CLR method
        """ GenerateDefaultValueExpression(self: CodeGenerator, e: CodeDefaultValueExpression) """
        ...

    def GenerateDelegateCreateExpression(self, *args): #cannot find CLR method
        """ GenerateDelegateCreateExpression(self: CodeGenerator, e: CodeDelegateCreateExpression) """
        ...

    def GenerateDelegateInvokeExpression(self, *args): #cannot find CLR method
        """ GenerateDelegateInvokeExpression(self: CodeGenerator, e: CodeDelegateInvokeExpression) """
        ...

    def GenerateDirectionExpression(self, *args): #cannot find CLR method
        """ GenerateDirectionExpression(self: CodeGenerator, e: CodeDirectionExpression) """
        ...

    def GenerateDirectives(self, *args): #cannot find CLR method
        """ GenerateDirectives(self: CodeGenerator, directives: CodeDirectiveCollection) """
        ...

    def GenerateDoubleValue(self, *args): #cannot find CLR method
        """ GenerateDoubleValue(self: CodeGenerator, d: float) """
        ...

    def GenerateEntryPointMethod(self, *args): #cannot find CLR method
        """ GenerateEntryPointMethod(self: CodeGenerator, e: CodeEntryPointMethod, c: CodeTypeDeclaration) """
        ...

    def GenerateEvent(self, *args): #cannot find CLR method
        """ GenerateEvent(self: CodeGenerator, e: CodeMemberEvent, c: CodeTypeDeclaration) """
        ...

    def GenerateEventReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateEventReferenceExpression(self: CodeGenerator, e: CodeEventReferenceExpression) """
        ...

    def GenerateExpression(self, *args): #cannot find CLR method
        """ GenerateExpression(self: CodeGenerator, e: CodeExpression) """
        ...

    def GenerateExpressionStatement(self, *args): #cannot find CLR method
        """ GenerateExpressionStatement(self: CodeGenerator, e: CodeExpressionStatement) """
        ...

    def GenerateField(self, *args): #cannot find CLR method
        """ GenerateField(self: CodeGenerator, e: CodeMemberField) """
        ...

    def GenerateFieldReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateFieldReferenceExpression(self: CodeGenerator, e: CodeFieldReferenceExpression) """
        ...

    def GenerateGotoStatement(self, *args): #cannot find CLR method
        """ GenerateGotoStatement(self: CodeGenerator, e: CodeGotoStatement) """
        ...

    def GenerateIndexerExpression(self, *args): #cannot find CLR method
        """ GenerateIndexerExpression(self: CodeGenerator, e: CodeIndexerExpression) """
        ...

    def GenerateIterationStatement(self, *args): #cannot find CLR method
        """ GenerateIterationStatement(self: CodeGenerator, e: CodeIterationStatement) """
        ...

    def GenerateLabeledStatement(self, *args): #cannot find CLR method
        """ GenerateLabeledStatement(self: CodeGenerator, e: CodeLabeledStatement) """
        ...

    def GenerateLinePragmaEnd(self, *args): #cannot find CLR method
        """ GenerateLinePragmaEnd(self: CodeGenerator, e: CodeLinePragma) """
        ...

    def GenerateLinePragmaStart(self, *args): #cannot find CLR method
        """ GenerateLinePragmaStart(self: CodeGenerator, e: CodeLinePragma) """
        ...

    def GenerateMethod(self, *args): #cannot find CLR method
        """ GenerateMethod(self: CodeGenerator, e: CodeMemberMethod, c: CodeTypeDeclaration) """
        ...

    def GenerateMethodInvokeExpression(self, *args): #cannot find CLR method
        """ GenerateMethodInvokeExpression(self: CodeGenerator, e: CodeMethodInvokeExpression) """
        ...

    def GenerateMethodReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateMethodReferenceExpression(self: CodeGenerator, e: CodeMethodReferenceExpression) """
        ...

    def GenerateMethodReturnStatement(self, *args): #cannot find CLR method
        """ GenerateMethodReturnStatement(self: CodeGenerator, e: CodeMethodReturnStatement) """
        ...

    def GenerateNamespace(self, *args): #cannot find CLR method
        """ GenerateNamespace(self: CodeGenerator, e: CodeNamespace) """
        ...

    def GenerateNamespaceEnd(self, *args): #cannot find CLR method
        """ GenerateNamespaceEnd(self: CodeGenerator, e: CodeNamespace) """
        ...

    def GenerateNamespaceImport(self, *args): #cannot find CLR method
        """ GenerateNamespaceImport(self: CodeGenerator, e: CodeNamespaceImport) """
        ...

    def GenerateNamespaceImports(self, *args): #cannot find CLR method
        """ GenerateNamespaceImports(self: CodeGenerator, e: CodeNamespace) """
        ...

    def GenerateNamespaces(self, *args): #cannot find CLR method
        """ GenerateNamespaces(self: CodeGenerator, e: CodeCompileUnit) """
        ...

    def GenerateNamespaceStart(self, *args): #cannot find CLR method
        """ GenerateNamespaceStart(self: CodeGenerator, e: CodeNamespace) """
        ...

    def GenerateObjectCreateExpression(self, *args): #cannot find CLR method
        """ GenerateObjectCreateExpression(self: CodeGenerator, e: CodeObjectCreateExpression) """
        ...

    def GenerateParameterDeclarationExpression(self, *args): #cannot find CLR method
        """ GenerateParameterDeclarationExpression(self: CodeGenerator, e: CodeParameterDeclarationExpression) """
        ...

    def GeneratePrimitiveExpression(self, *args): #cannot find CLR method
        """ GeneratePrimitiveExpression(self: CodeGenerator, e: CodePrimitiveExpression) """
        ...

    def GenerateProperty(self, *args): #cannot find CLR method
        """ GenerateProperty(self: CodeGenerator, e: CodeMemberProperty, c: CodeTypeDeclaration) """
        ...

    def GeneratePropertyReferenceExpression(self, *args): #cannot find CLR method
        """ GeneratePropertyReferenceExpression(self: CodeGenerator, e: CodePropertyReferenceExpression) """
        ...

    def GeneratePropertySetValueReferenceExpression(self, *args): #cannot find CLR method
        """ GeneratePropertySetValueReferenceExpression(self: CodeGenerator, e: CodePropertySetValueReferenceExpression) """
        ...

    def GenerateRemoveEventStatement(self, *args): #cannot find CLR method
        """ GenerateRemoveEventStatement(self: CodeGenerator, e: CodeRemoveEventStatement) """
        ...

    def GenerateSingleFloatValue(self, *args): #cannot find CLR method
        """ GenerateSingleFloatValue(self: CodeGenerator, s: Single) """
        ...

    def GenerateSnippetCompileUnit(self, *args): #cannot find CLR method
        """ GenerateSnippetCompileUnit(self: CodeGenerator, e: CodeSnippetCompileUnit) """
        ...

    def GenerateSnippetExpression(self, *args): #cannot find CLR method
        """ GenerateSnippetExpression(self: CodeGenerator, e: CodeSnippetExpression) """
        ...

    def GenerateSnippetMember(self, *args): #cannot find CLR method
        """ GenerateSnippetMember(self: CodeGenerator, e: CodeSnippetTypeMember) """
        ...

    def GenerateSnippetStatement(self, *args): #cannot find CLR method
        """ GenerateSnippetStatement(self: CodeGenerator, e: CodeSnippetStatement) """
        ...

    def GenerateStatement(self, *args): #cannot find CLR method
        """ GenerateStatement(self: CodeGenerator, e: CodeStatement) """
        ...

    def GenerateStatements(self, *args): #cannot find CLR method
        """ GenerateStatements(self: CodeGenerator, stms: CodeStatementCollection) """
        ...

    def GenerateThisReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateThisReferenceExpression(self: CodeGenerator, e: CodeThisReferenceExpression) """
        ...

    def GenerateThrowExceptionStatement(self, *args): #cannot find CLR method
        """ GenerateThrowExceptionStatement(self: CodeGenerator, e: CodeThrowExceptionStatement) """
        ...

    def GenerateTryCatchFinallyStatement(self, *args): #cannot find CLR method
        """ GenerateTryCatchFinallyStatement(self: CodeGenerator, e: CodeTryCatchFinallyStatement) """
        ...

    def GenerateTypeConstructor(self, *args): #cannot find CLR method
        """ GenerateTypeConstructor(self: CodeGenerator, e: CodeTypeConstructor) """
        ...

    def GenerateTypeEnd(self, *args): #cannot find CLR method
        """ GenerateTypeEnd(self: CodeGenerator, e: CodeTypeDeclaration) """
        ...

    def GenerateTypeOfExpression(self, *args): #cannot find CLR method
        """ GenerateTypeOfExpression(self: CodeGenerator, e: CodeTypeOfExpression) """
        ...

    def GenerateTypeReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateTypeReferenceExpression(self: CodeGenerator, e: CodeTypeReferenceExpression) """
        ...

    def GenerateTypes(self, *args): #cannot find CLR method
        """ GenerateTypes(self: CodeGenerator, e: CodeNamespace) """
        ...

    def GenerateTypeStart(self, *args): #cannot find CLR method
        """ GenerateTypeStart(self: CodeGenerator, e: CodeTypeDeclaration) """
        ...

    def GenerateVariableDeclarationStatement(self, *args): #cannot find CLR method
        """ GenerateVariableDeclarationStatement(self: CodeGenerator, e: CodeVariableDeclarationStatement) """
        ...

    def GenerateVariableReferenceExpression(self, *args): #cannot find CLR method
        """ GenerateVariableReferenceExpression(self: CodeGenerator, e: CodeVariableReferenceExpression) """
        ...

    @staticmethod
    def IsValidLanguageIndependentIdentifier(value:str) -> bool:
        """ IsValidLanguageIndependentIdentifier(value: str) -> bool """
        ...

    def OutputAttributeArgument(self, *args): #cannot find CLR method
        """ OutputAttributeArgument(self: CodeGenerator, arg: CodeAttributeArgument) """
        ...

    def OutputAttributeDeclarations(self, *args): #cannot find CLR method
        """ OutputAttributeDeclarations(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection) """
        ...

    def OutputDirection(self, *args): #cannot find CLR method
        """ OutputDirection(self: CodeGenerator, dir: FieldDirection) """
        ...

    def OutputExpressionList(self, *args): #cannot find CLR method
        """ OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection)OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection, newlineBetweenItems: bool) """
        ...

    def OutputFieldScopeModifier(self, *args): #cannot find CLR method
        """ OutputFieldScopeModifier(self: CodeGenerator, attributes: MemberAttributes) """
        ...

    def OutputIdentifier(self, *args): #cannot find CLR method
        """ OutputIdentifier(self: CodeGenerator, ident: str) """
        ...

    def OutputMemberAccessModifier(self, *args): #cannot find CLR method
        """ OutputMemberAccessModifier(self: CodeGenerator, attributes: MemberAttributes) """
        ...

    def OutputMemberScopeModifier(self, *args): #cannot find CLR method
        """ OutputMemberScopeModifier(self: CodeGenerator, attributes: MemberAttributes) """
        ...

    def OutputOperator(self, *args): #cannot find CLR method
        """ OutputOperator(self: CodeGenerator, op: CodeBinaryOperatorType) """
        ...

    def OutputParameters(self, *args): #cannot find CLR method
        """ OutputParameters(self: CodeGenerator, parameters: CodeParameterDeclarationExpressionCollection) """
        ...

    def OutputType(self, *args): #cannot find CLR method
        """ OutputType(self: CodeGenerator, typeRef: CodeTypeReference) """
        ...

    def OutputTypeAttributes(self, *args): #cannot find CLR method
        """ OutputTypeAttributes(self: CodeGenerator, attributes: TypeAttributes, isStruct: bool, isEnum: bool) """
        ...

    def OutputTypeNamePair(self, *args): #cannot find CLR method
        """ OutputTypeNamePair(self: CodeGenerator, typeRef: CodeTypeReference, name: str) """
        ...

    def QuoteSnippetString(self, *args): #cannot find CLR method
        """ QuoteSnippetString(self: CodeGenerator, value: str) -> str """
        ...

    @staticmethod
    def ValidateIdentifiers(e:CodeObject): # -> 
        """ ValidateIdentifiers(e: CodeObject) """
        ...


class ICodeCompiler: # skipped bases: <type 'object'>
    """ no doc """
    def CompileAssemblyFromDom(self, options:CompilerParameters, compilationUnit:CodeCompileUnit) -> CompilerResults:
        """ CompileAssemblyFromDom(self: ICodeCompiler, options: CompilerParameters, compilationUnit: CodeCompileUnit) -> CompilerResults """
        ...

    def CompileAssemblyFromDomBatch(self, options:CompilerParameters, compilationUnits:Array) -> CompilerResults:
        """ CompileAssemblyFromDomBatch(self: ICodeCompiler, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]) -> CompilerResults """
        ...

    def CompileAssemblyFromFile(self, options:CompilerParameters, fileName:str) -> CompilerResults:
        """ CompileAssemblyFromFile(self: ICodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults """
        ...

    def CompileAssemblyFromFileBatch(self, options:CompilerParameters, fileNames:Array) -> CompilerResults:
        """ CompileAssemblyFromFileBatch(self: ICodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults """
        ...

    def CompileAssemblyFromSource(self, options:CompilerParameters, source:str) -> CompilerResults:
        """ CompileAssemblyFromSource(self: ICodeCompiler, options: CompilerParameters, source: str) -> CompilerResults """
        ...

    def CompileAssemblyFromSourceBatch(self, options:CompilerParameters, sources:Array) -> CompilerResults:
        """ CompileAssemblyFromSourceBatch(self: ICodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults """
        ...


class CodeCompiler(CodeGenerator, ICodeCompiler): # skipped bases: <type 'ICodeGenerator'>, <type 'object'>
    """ no doc """
    @property
    def CompilerName(self):
        ...

    @property
    def FileExtension(self):
        ...


    def CmdArgsFromParameters(self, *args): #cannot find CLR method
        """ CmdArgsFromParameters(self: CodeCompiler, options: CompilerParameters) -> str """
        ...

    def FromDom(self, *args): #cannot find CLR method
        """ FromDom(self: CodeCompiler, options: CompilerParameters, e: CodeCompileUnit) -> CompilerResults """
        ...

    def FromDomBatch(self, *args): #cannot find CLR method
        """ FromDomBatch(self: CodeCompiler, options: CompilerParameters, ea: Array[CodeCompileUnit]) -> CompilerResults """
        ...

    def FromFile(self, *args): #cannot find CLR method
        """ FromFile(self: CodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults """
        ...

    def FromFileBatch(self, *args): #cannot find CLR method
        """ FromFileBatch(self: CodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults """
        ...

    def FromSource(self, *args): #cannot find CLR method
        """ FromSource(self: CodeCompiler, options: CompilerParameters, source: str) -> CompilerResults """
        ...

    def FromSourceBatch(self, *args): #cannot find CLR method
        """ FromSourceBatch(self: CodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults """
        ...

    def GetResponseFileCmdArgs(self, *args): #cannot find CLR method
        """ GetResponseFileCmdArgs(self: CodeCompiler, options: CompilerParameters, cmdArgs: str) -> str """
        ...

    def JoinStringArray(self, *args): #cannot find CLR method
        """ JoinStringArray(sa: Array[str], separator: str) -> str """
        ...

    def ProcessCompilerOutputLine(self, *args): #cannot find CLR method
        """ ProcessCompilerOutputLine(self: CodeCompiler, results: CompilerResults, line: str) """
        ...


class CodeDomProvider(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def FileExtension(self) -> str:
        """ Get: FileExtension(self: CodeDomProvider) -> str """
        ...

    @property
    def LanguageOptions(self) -> LanguageOptions:
        """ Get: LanguageOptions(self: CodeDomProvider) -> LanguageOptions """
        ...


    def CompileAssemblyFromDom(self, options:CompilerParameters, compilationUnits:Array) -> CompilerResults:
        """ CompileAssemblyFromDom(self: CodeDomProvider, options: CompilerParameters, *compilationUnits: Array[CodeCompileUnit]) -> CompilerResults """
        ...

    def CompileAssemblyFromFile(self, options:CompilerParameters, fileNames:Array) -> CompilerResults:
        """ CompileAssemblyFromFile(self: CodeDomProvider, options: CompilerParameters, *fileNames: Array[str]) -> CompilerResults """
        ...

    def CompileAssemblyFromSource(self, options:CompilerParameters, sources:Array) -> CompilerResults:
        """ CompileAssemblyFromSource(self: CodeDomProvider, options: CompilerParameters, *sources: Array[str]) -> CompilerResults """
        ...

    def CreateCompiler(self) -> ICodeCompiler:
        """ CreateCompiler(self: CodeDomProvider) -> ICodeCompiler """
        ...

    def CreateEscapedIdentifier(self, value:str) -> str:
        """ CreateEscapedIdentifier(self: CodeDomProvider, value: str) -> str """
        ...

    def CreateGenerator(self, *__args:TextWriter) -> ICodeGenerator:
        """
        CreateGenerator(self: CodeDomProvider, output: TextWriter) -> ICodeGenerator
        CreateGenerator(self: CodeDomProvider, fileName: str) -> ICodeGenerator
        CreateGenerator(self: CodeDomProvider) -> ICodeGenerator
        """
        ...

    def CreateParser(self) -> ICodeParser:
        """ CreateParser(self: CodeDomProvider) -> ICodeParser """
        ...

    @staticmethod
    def CreateProvider(language:str, providerOptions:IDictionary = ...) -> CodeDomProvider:
        """
        CreateProvider(language: str, providerOptions: IDictionary[str, str]) -> CodeDomProvider
        CreateProvider(language: str) -> CodeDomProvider
        """
        ...

    def CreateValidIdentifier(self, value:str) -> str:
        """ CreateValidIdentifier(self: CodeDomProvider, value: str) -> str """
        ...

    def GenerateCodeFromCompileUnit(self, compileUnit:CodeCompileUnit, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromCompileUnit(self: CodeDomProvider, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromExpression(self, expression:CodeExpression, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromExpression(self: CodeDomProvider, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromMember(self, member:CodeTypeMember, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromMember(self: CodeDomProvider, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromNamespace(self, codeNamespace:CodeNamespace, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromNamespace(self: CodeDomProvider, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromStatement(self, statement:CodeStatement, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromStatement(self: CodeDomProvider, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    def GenerateCodeFromType(self, codeType:CodeTypeDeclaration, writer:TextWriter, options:CodeGeneratorOptions): # -> 
        """ GenerateCodeFromType(self: CodeDomProvider, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions) """
        ...

    @staticmethod
    def GetAllCompilerInfo() -> Array:
        """ GetAllCompilerInfo() -> Array[CompilerInfo] """
        ...

    @staticmethod
    def GetCompilerInfo(language:str) -> CompilerInfo:
        """ GetCompilerInfo(language: str) -> CompilerInfo """
        ...

    def GetConverter(self, type:Type) -> TypeConverter:
        """ GetConverter(self: CodeDomProvider, type: Type) -> TypeConverter """
        ...

    @staticmethod
    def GetLanguageFromExtension(extension:str) -> str:
        """ GetLanguageFromExtension(extension: str) -> str """
        ...

    def GetTypeOutput(self, type:CodeTypeReference) -> str:
        """ GetTypeOutput(self: CodeDomProvider, type: CodeTypeReference) -> str """
        ...

    @staticmethod
    def IsDefinedExtension(extension:str) -> bool:
        """ IsDefinedExtension(extension: str) -> bool """
        ...

    @staticmethod
    def IsDefinedLanguage(language:str) -> bool:
        """ IsDefinedLanguage(language: str) -> bool """
        ...

    def IsValidIdentifier(self, value:str) -> bool:
        """ IsValidIdentifier(self: CodeDomProvider, value: str) -> bool """
        ...

    def Parse(self, codeStream:TextReader) -> CodeCompileUnit:
        """ Parse(self: CodeDomProvider, codeStream: TextReader) -> CodeCompileUnit """
        ...

    def Supports(self, generatorSupport:GeneratorSupport) -> bool:
        """ Supports(self: CodeDomProvider, generatorSupport: GeneratorSupport) -> bool """
        ...


class CodeGeneratorOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ CodeGeneratorOptions() """
    @property
    def BlankLinesBetweenMembers(self) -> bool:
        """
        Get: BlankLinesBetweenMembers(self: CodeGeneratorOptions) -> bool
        Set: BlankLinesBetweenMembers(self: CodeGeneratorOptions) = value
        """
        ...

    @property
    def BracingStyle(self) -> str:
        """
        Get: BracingStyle(self: CodeGeneratorOptions) -> str
        Set: BracingStyle(self: CodeGeneratorOptions) = value
        """
        ...

    @property
    def ElseOnClosing(self) -> bool:
        """
        Get: ElseOnClosing(self: CodeGeneratorOptions) -> bool
        Set: ElseOnClosing(self: CodeGeneratorOptions) = value
        """
        ...

    @property
    def IndentString(self) -> str:
        """
        Get: IndentString(self: CodeGeneratorOptions) -> str
        Set: IndentString(self: CodeGeneratorOptions) = value
        """
        ...

    @property
    def VerbatimOrder(self) -> bool:
        """
        Get: VerbatimOrder(self: CodeGeneratorOptions) -> bool
        Set: VerbatimOrder(self: CodeGeneratorOptions) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CodeParser(ICodeParser): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CompilerError: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompilerError()
    CompilerError(fileName: str, line: int, column: int, errorNumber: str, errorText: str)
    """
    @property
    def Column(self) -> int:
        """
        Get: Column(self: CompilerError) -> int
        Set: Column(self: CompilerError) = value
        """
        ...

    @property
    def ErrorNumber(self) -> str:
        """
        Get: ErrorNumber(self: CompilerError) -> str
        Set: ErrorNumber(self: CompilerError) = value
        """
        ...

    @property
    def ErrorText(self) -> str:
        """
        Get: ErrorText(self: CompilerError) -> str
        Set: ErrorText(self: CompilerError) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: CompilerError) -> str
        Set: FileName(self: CompilerError) = value
        """
        ...

    @property
    def IsWarning(self) -> bool:
        """
        Get: IsWarning(self: CompilerError) -> bool
        Set: IsWarning(self: CompilerError) = value
        """
        ...

    @property
    def Line(self) -> int:
        """
        Get: Line(self: CompilerError) -> int
        Set: Line(self: CompilerError) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: CompilerError) -> str """
        ...


class CompilerErrorCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CompilerErrorCollection()
    CompilerErrorCollection(value: CompilerErrorCollection)
    CompilerErrorCollection(value: Array[CompilerError])
    """
    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: CompilerErrorCollection) -> bool """
        ...

    @property
    def HasWarnings(self) -> bool:
        """ Get: HasWarnings(self: CompilerErrorCollection) -> bool """
        ...


    def Add(self, value:CompilerError) -> int:
        """ Add(self: CompilerErrorCollection, value: CompilerError) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CompilerErrorCollection, value: Array[CompilerError])AddRange(self: CompilerErrorCollection, value: CompilerErrorCollection) """
        ...

    def Contains(self, value:CompilerError) -> bool:
        """ Contains(self: CompilerErrorCollection, value: CompilerError) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CompilerErrorCollection, array: Array[CompilerError], index: int) """
        ...

    def IndexOf(self, value:CompilerError) -> int:
        """ IndexOf(self: CompilerErrorCollection, value: CompilerError) -> int """
        ...

    def Insert(self, index:int, value:CompilerError): # -> 
        """ Insert(self: CompilerErrorCollection, index: int, value: CompilerError) """
        ...

    def Remove(self, value:CompilerError): # -> 
        """ Remove(self: CompilerErrorCollection, value: CompilerError) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CompilerInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CodeDomProviderType(self) -> Type:
        """ Get: CodeDomProviderType(self: CompilerInfo) -> Type """
        ...

    @property
    def IsCodeDomProviderTypeValid(self) -> bool:
        """ Get: IsCodeDomProviderTypeValid(self: CompilerInfo) -> bool """
        ...


    def CreateDefaultCompilerParameters(self) -> CompilerParameters:
        """ CreateDefaultCompilerParameters(self: CompilerInfo) -> CompilerParameters """
        ...

    def CreateProvider(self, providerOptions:IDictionary = ...) -> CodeDomProvider:
        """
        CreateProvider(self: CompilerInfo, providerOptions: IDictionary[str, str]) -> CodeDomProvider
        CreateProvider(self: CompilerInfo) -> CodeDomProvider
        """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: CompilerInfo, o: object) -> bool """
        ...

    def GetExtensions(self) -> Array:
        """ GetExtensions(self: CompilerInfo) -> Array[str] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CompilerInfo) -> int """
        ...

    def GetLanguages(self) -> Array:
        """ GetLanguages(self: CompilerInfo) -> Array[str] """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompilerParameters: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompilerParameters()
    CompilerParameters(assemblyNames: Array[str])
    CompilerParameters(assemblyNames: Array[str], outputName: str)
    CompilerParameters(assemblyNames: Array[str], outputName: str, includeDebugInformation: bool)
    """
    @property
    def CompilerOptions(self) -> str:
        """
        Get: CompilerOptions(self: CompilerParameters) -> str
        Set: CompilerOptions(self: CompilerParameters) = value
        """
        ...

    @property
    def CoreAssemblyFileName(self) -> str:
        """
        Get: CoreAssemblyFileName(self: CompilerParameters) -> str
        Set: CoreAssemblyFileName(self: CompilerParameters) = value
        """
        ...

    @property
    def EmbeddedResources(self) -> StringCollection:
        """ Get: EmbeddedResources(self: CompilerParameters) -> StringCollection """
        ...

    @property
    def Evidence(self) -> Evidence:
        """
        Get: Evidence(self: CompilerParameters) -> Evidence
        Set: Evidence(self: CompilerParameters) = value
        """
        ...

    @property
    def GenerateExecutable(self) -> bool:
        """
        Get: GenerateExecutable(self: CompilerParameters) -> bool
        Set: GenerateExecutable(self: CompilerParameters) = value
        """
        ...

    @property
    def GenerateInMemory(self) -> bool:
        """
        Get: GenerateInMemory(self: CompilerParameters) -> bool
        Set: GenerateInMemory(self: CompilerParameters) = value
        """
        ...

    @property
    def IncludeDebugInformation(self) -> bool:
        """
        Get: IncludeDebugInformation(self: CompilerParameters) -> bool
        Set: IncludeDebugInformation(self: CompilerParameters) = value
        """
        ...

    @property
    def LinkedResources(self) -> StringCollection:
        """ Get: LinkedResources(self: CompilerParameters) -> StringCollection """
        ...

    @property
    def MainClass(self) -> str:
        """
        Get: MainClass(self: CompilerParameters) -> str
        Set: MainClass(self: CompilerParameters) = value
        """
        ...

    @property
    def OutputAssembly(self) -> str:
        """
        Get: OutputAssembly(self: CompilerParameters) -> str
        Set: OutputAssembly(self: CompilerParameters) = value
        """
        ...

    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """ Get: ReferencedAssemblies(self: CompilerParameters) -> StringCollection """
        ...

    @property
    def TempFiles(self) -> TempFileCollection:
        """
        Get: TempFiles(self: CompilerParameters) -> TempFileCollection
        Set: TempFiles(self: CompilerParameters) = value
        """
        ...

    @property
    def TreatWarningsAsErrors(self) -> bool:
        """
        Get: TreatWarningsAsErrors(self: CompilerParameters) -> bool
        Set: TreatWarningsAsErrors(self: CompilerParameters) = value
        """
        ...

    @property
    def UserToken(self) -> IntPtr:
        """
        Get: UserToken(self: CompilerParameters) -> IntPtr
        Set: UserToken(self: CompilerParameters) = value
        """
        ...

    @property
    def WarningLevel(self) -> int:
        """
        Get: WarningLevel(self: CompilerParameters) -> int
        Set: WarningLevel(self: CompilerParameters) = value
        """
        ...

    @property
    def Win32Resource(self) -> str:
        """
        Get: Win32Resource(self: CompilerParameters) -> str
        Set: Win32Resource(self: CompilerParameters) = value
        """
        ...



class CompilerResults: # skipped bases: <type 'object'>, <type 'object'>
    """ CompilerResults(tempFiles: TempFileCollection) """
    @property
    def CompiledAssembly(self) -> Assembly:
        """
        Get: CompiledAssembly(self: CompilerResults) -> Assembly
        Set: CompiledAssembly(self: CompilerResults) = value
        """
        ...

    @property
    def Errors(self) -> CompilerErrorCollection:
        """ Get: Errors(self: CompilerResults) -> CompilerErrorCollection """
        ...

    @property
    def Evidence(self) -> Evidence:
        """
        Get: Evidence(self: CompilerResults) -> Evidence
        Set: Evidence(self: CompilerResults) = value
        """
        ...

    @property
    def NativeCompilerReturnValue(self) -> int:
        """
        Get: NativeCompilerReturnValue(self: CompilerResults) -> int
        Set: NativeCompilerReturnValue(self: CompilerResults) = value
        """
        ...

    @property
    def Output(self) -> StringCollection:
        """ Get: Output(self: CompilerResults) -> StringCollection """
        ...

    @property
    def PathToAssembly(self) -> str:
        """
        Get: PathToAssembly(self: CompilerResults) -> str
        Set: PathToAssembly(self: CompilerResults) = value
        """
        ...

    @property
    def TempFiles(self) -> TempFileCollection:
        """
        Get: TempFiles(self: CompilerResults) -> TempFileCollection
        Set: TempFiles(self: CompilerResults) = value
        """
        ...



class Executor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ExecWait(cmd:str, tempFiles:TempFileCollection): # -> 
        """ ExecWait(cmd: str, tempFiles: TempFileCollection) """
        ...

    @staticmethod
    def ExecWaitWithCapture(*__args) -> Tuple_[int, str, str]:
        """
        ExecWaitWithCapture(cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        ExecWaitWithCapture(cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        ExecWaitWithCapture(userToken: IntPtr, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        ExecWaitWithCapture(userToken: IntPtr, cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        """
        ...

    __all__: list = ...


class GeneratedCodeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ GeneratedCodeAttribute(tool: str, version: str) """
    @property
    def Tool(self) -> str:
        """ Get: Tool(self: GeneratedCodeAttribute) -> str """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: GeneratedCodeAttribute) -> str """
        ...


    def __new__(cls, tool:str, version:str) -> Self:
        """ __new__(cls: type, tool: str, version: str) """
        ...


class GeneratorSupport(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) GeneratorSupport, values: ArraysOfArrays (1), AssemblyAttributes (4096), ChainedConstructorArguments (32768), ComplexExpressions (524288), DeclareDelegates (512), DeclareEnums (256), DeclareEvents (2048), DeclareIndexerProperties (33554432), DeclareInterfaces (1024), DeclareValueTypes (128), EntryPointMethod (2), GenericTypeDeclaration (16777216), GenericTypeReference (8388608), GotoStatements (4), MultidimensionalArrays (8), MultipleInterfaceMembers (131072), NestedTypes (65536), ParameterAttributes (8192), PartialTypes (4194304), PublicStaticMembers (262144), ReferenceParameters (16384), Resources (2097152), ReturnTypeAttributes (64), StaticConstructors (16), TryCatchStatements (32), Win32Resources (1048576) """
    ArraysOfArrays: GeneratorSupport = ...
    AssemblyAttributes: GeneratorSupport = ...
    ChainedConstructorArguments: GeneratorSupport = ...
    ComplexExpressions: GeneratorSupport = ...
    DeclareDelegates: GeneratorSupport = ...
    DeclareEnums: GeneratorSupport = ...
    DeclareEvents: GeneratorSupport = ...
    DeclareIndexerProperties: GeneratorSupport = ...
    DeclareInterfaces: GeneratorSupport = ...
    DeclareValueTypes: GeneratorSupport = ...
    EntryPointMethod: GeneratorSupport = ...
    GenericTypeDeclaration: GeneratorSupport = ...
    GenericTypeReference: GeneratorSupport = ...
    GotoStatements: GeneratorSupport = ...
    MultidimensionalArrays: GeneratorSupport = ...
    MultipleInterfaceMembers: GeneratorSupport = ...
    NestedTypes: GeneratorSupport = ...
    ParameterAttributes: GeneratorSupport = ...
    PartialTypes: GeneratorSupport = ...
    PublicStaticMembers: GeneratorSupport = ...
    ReferenceParameters: GeneratorSupport = ...
    Resources: GeneratorSupport = ...
    ReturnTypeAttributes: GeneratorSupport = ...
    StaticConstructors: GeneratorSupport = ...
    TryCatchStatements: GeneratorSupport = ...
    value__ = ...
    Win32Resources: GeneratorSupport = ...


class ICodeParser: # skipped bases: <type 'object'>
    """ no doc """
    def Parse(self, codeStream:TextReader) -> CodeCompileUnit:
        """ Parse(self: ICodeParser, codeStream: TextReader) -> CodeCompileUnit """
        ...


class IndentedTextWriter(TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    IndentedTextWriter(writer: TextWriter)
    IndentedTextWriter(writer: TextWriter, tabString: str)
    """
    @property
    def Indent(self) -> int:
        """
        Get: Indent(self: IndentedTextWriter) -> int
        Set: Indent(self: IndentedTextWriter) = value
        """
        ...

    @property
    def InnerWriter(self) -> TextWriter:
        """ Get: InnerWriter(self: IndentedTextWriter) -> TextWriter """
        ...


    def OutputTabs(self, *args): #cannot find CLR method
        """ OutputTabs(self: IndentedTextWriter) """
        ...

    def WriteLineNoTabs(self, s:str): # -> 
        """ WriteLineNoTabs(self: IndentedTextWriter, s: str) """
        ...

    CoreNewLine = ...
    DefaultTabString: str = ...


class LanguageOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LanguageOptions, values: CaseInsensitive (1), None (0) """
    CaseInsensitive: LanguageOptions = ...
    value__ = ...


class TempFileCollection(IDisposable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    TempFileCollection()
    TempFileCollection(tempDir: str)
    TempFileCollection(tempDir: str, keepFiles: bool)
    """
    @property
    def BasePath(self) -> str:
        """ Get: BasePath(self: TempFileCollection) -> str """
        ...

    @property
    def KeepFiles(self) -> bool:
        """
        Get: KeepFiles(self: TempFileCollection) -> bool
        Set: KeepFiles(self: TempFileCollection) = value
        """
        ...

    @property
    def TempDir(self) -> str:
        """ Get: TempDir(self: TempFileCollection) -> str """
        ...


    def AddExtension(self, fileExtension:str, keepFile:bool = ...) -> str:
        """
        AddExtension(self: TempFileCollection, fileExtension: str, keepFile: bool) -> str
        AddExtension(self: TempFileCollection, fileExtension: str) -> str
        """
        ...

    def AddFile(self, fileName:str, keepFile:bool): # -> 
        """ AddFile(self: TempFileCollection, fileName: str, keepFile: bool) """
        ...

    def Delete(self): # -> 
        """ Delete(self: TempFileCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TempFileCollection) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


