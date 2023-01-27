# encoding: utf-8
# module System.CodeDom calls itself CodeDom
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Guid, Type

from System.Collections import (CollectionBase, IDictionary, IEnumerator, 
    IList)

from System.Collections.Specialized import StringCollection

from System.Reflection import TypeAttributes

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CodeObject: # skipped bases: <type 'object'>, <type 'object'>
    """ CodeObject() """
    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: CodeObject) -> IDictionary """
        ...



class CodeExpression(CodeObject): # skipped bases: <type 'object'>
    """ CodeExpression() """
    pass

class CodeArgumentReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeArgumentReferenceExpression()
    CodeArgumentReferenceExpression(parameterName: str)
    """
    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: CodeArgumentReferenceExpression) -> str
        Set: ParameterName(self: CodeArgumentReferenceExpression) = value
        """
        ...


    def __new__(cls, parameterName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        """
        ...


class CodeArrayCreateExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeArrayCreateExpression()
    CodeArrayCreateExpression(createType: CodeTypeReference, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: str, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: Type, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: CodeTypeReference, size: int)
    CodeArrayCreateExpression(createType: str, size: int)
    CodeArrayCreateExpression(createType: Type, size: int)
    CodeArrayCreateExpression(createType: CodeTypeReference, size: CodeExpression)
    CodeArrayCreateExpression(createType: str, size: CodeExpression)
    CodeArrayCreateExpression(createType: Type, size: CodeExpression)
    """
    @property
    def CreateType(self) -> CodeTypeReference:
        """
        Get: CreateType(self: CodeArrayCreateExpression) -> CodeTypeReference
        Set: CreateType(self: CodeArrayCreateExpression) = value
        """
        ...

    @property
    def Initializers(self) -> CodeExpressionCollection:
        """ Get: Initializers(self: CodeArrayCreateExpression) -> CodeExpressionCollection """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: CodeArrayCreateExpression) -> int
        Set: Size(self: CodeArrayCreateExpression) = value
        """
        ...

    @property
    def SizeExpression(self) -> CodeExpression:
        """
        Get: SizeExpression(self: CodeArrayCreateExpression) -> CodeExpression
        Set: SizeExpression(self: CodeArrayCreateExpression) = value
        """
        ...


    def __new__(cls, createType:CodeTypeReference = ..., *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, createType: CodeTypeReference, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: str, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: Type, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: CodeTypeReference, size: int)
        __new__(cls: type, createType: str, size: int)
        __new__(cls: type, createType: Type, size: int)
        __new__(cls: type, createType: CodeTypeReference, size: CodeExpression)
        __new__(cls: type, createType: str, size: CodeExpression)
        __new__(cls: type, createType: Type, size: CodeExpression)
        """
        ...


class CodeArrayIndexerExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeArrayIndexerExpression()
    CodeArrayIndexerExpression(targetObject: CodeExpression, *indices: Array[CodeExpression])
    """
    @property
    def Indices(self) -> CodeExpressionCollection:
        """ Get: Indices(self: CodeArrayIndexerExpression) -> CodeExpressionCollection """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeArrayIndexerExpression) -> CodeExpression
        Set: TargetObject(self: CodeArrayIndexerExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., indices:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, *indices: Array[CodeExpression])
        """
        ...


class CodeStatement(CodeObject): # skipped bases: <type 'object'>
    """ CodeStatement() """
    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """ Get: EndDirectives(self: CodeStatement) -> CodeDirectiveCollection """
        ...

    @property
    def LinePragma(self) -> CodeLinePragma:
        """
        Get: LinePragma(self: CodeStatement) -> CodeLinePragma
        Set: LinePragma(self: CodeStatement) = value
        """
        ...

    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """ Get: StartDirectives(self: CodeStatement) -> CodeDirectiveCollection """
        ...



class CodeAssignStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeAssignStatement()
    CodeAssignStatement(left: CodeExpression, right: CodeExpression)
    """
    @property
    def Left(self) -> CodeExpression:
        """
        Get: Left(self: CodeAssignStatement) -> CodeExpression
        Set: Left(self: CodeAssignStatement) = value
        """
        ...

    @property
    def Right(self) -> CodeExpression:
        """
        Get: Right(self: CodeAssignStatement) -> CodeExpression
        Set: Right(self: CodeAssignStatement) = value
        """
        ...


    def __new__(cls, left:CodeExpression = ..., right:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, left: CodeExpression, right: CodeExpression)
        """
        ...


class CodeAttachEventStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeAttachEventStatement()
    CodeAttachEventStatement(eventRef: CodeEventReferenceExpression, listener: CodeExpression)
    CodeAttachEventStatement(targetObject: CodeExpression, eventName: str, listener: CodeExpression)
    """
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """
        Get: Event(self: CodeAttachEventStatement) -> CodeEventReferenceExpression
        Set: Event(self: CodeAttachEventStatement) = value
        """
        ...

    @property
    def Listener(self) -> CodeExpression:
        """
        Get: Listener(self: CodeAttachEventStatement) -> CodeExpression
        Set: Listener(self: CodeAttachEventStatement) = value
        """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, eventRef: CodeEventReferenceExpression, listener: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, eventName: str, listener: CodeExpression)
        """
        ...


class CodeAttributeArgument: # skipped bases: <type 'object'>, <type 'object'>
    """
    CodeAttributeArgument()
    CodeAttributeArgument(value: CodeExpression)
    CodeAttributeArgument(name: str, value: CodeExpression)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeAttributeArgument) -> str
        Set: Name(self: CodeAttributeArgument) = value
        """
        ...

    @property
    def Value(self) -> CodeExpression:
        """
        Get: Value(self: CodeAttributeArgument) -> CodeExpression
        Set: Value(self: CodeAttributeArgument) = value
        """
        ...



class CodeAttributeArgumentCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeAttributeArgumentCollection()
    CodeAttributeArgumentCollection(value: CodeAttributeArgumentCollection)
    CodeAttributeArgumentCollection(value: Array[CodeAttributeArgument])
    """
    def Add(self, value:CodeAttributeArgument) -> int:
        """ Add(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeAttributeArgumentCollection, value: Array[CodeAttributeArgument])AddRange(self: CodeAttributeArgumentCollection, value: CodeAttributeArgumentCollection) """
        ...

    def Contains(self, value:CodeAttributeArgument) -> bool:
        """ Contains(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeAttributeArgumentCollection, array: Array[CodeAttributeArgument], index: int) """
        ...

    def IndexOf(self, value:CodeAttributeArgument) -> int:
        """ IndexOf(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> int """
        ...

    def Insert(self, index:int, value:CodeAttributeArgument): # -> 
        """ Insert(self: CodeAttributeArgumentCollection, index: int, value: CodeAttributeArgument) """
        ...

    def Remove(self, value:CodeAttributeArgument): # -> 
        """ Remove(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) """
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


class CodeAttributeDeclaration: # skipped bases: <type 'object'>, <type 'object'>
    """
    CodeAttributeDeclaration()
    CodeAttributeDeclaration(name: str)
    CodeAttributeDeclaration(name: str, *arguments: Array[CodeAttributeArgument])
    CodeAttributeDeclaration(attributeType: CodeTypeReference)
    CodeAttributeDeclaration(attributeType: CodeTypeReference, *arguments: Array[CodeAttributeArgument])
    """
    @property
    def Arguments(self) -> CodeAttributeArgumentCollection:
        """ Get: Arguments(self: CodeAttributeDeclaration) -> CodeAttributeArgumentCollection """
        ...

    @property
    def AttributeType(self) -> CodeTypeReference:
        """ Get: AttributeType(self: CodeAttributeDeclaration) -> CodeTypeReference """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeAttributeDeclaration) -> str
        Set: Name(self: CodeAttributeDeclaration) = value
        """
        ...



class CodeAttributeDeclarationCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeAttributeDeclarationCollection()
    CodeAttributeDeclarationCollection(value: CodeAttributeDeclarationCollection)
    CodeAttributeDeclarationCollection(value: Array[CodeAttributeDeclaration])
    """
    def Add(self, value:CodeAttributeDeclaration) -> int:
        """ Add(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeAttributeDeclarationCollection, value: Array[CodeAttributeDeclaration])AddRange(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclarationCollection) """
        ...

    def Contains(self, value:CodeAttributeDeclaration) -> bool:
        """ Contains(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeAttributeDeclarationCollection, array: Array[CodeAttributeDeclaration], index: int) """
        ...

    def IndexOf(self, value:CodeAttributeDeclaration) -> int:
        """ IndexOf(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> int """
        ...

    def Insert(self, index:int, value:CodeAttributeDeclaration): # -> 
        """ Insert(self: CodeAttributeDeclarationCollection, index: int, value: CodeAttributeDeclaration) """
        ...

    def Remove(self, value:CodeAttributeDeclaration): # -> 
        """ Remove(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) """
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


class CodeBaseReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """ CodeBaseReferenceExpression() """
    pass

class CodeBinaryOperatorExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeBinaryOperatorExpression()
    CodeBinaryOperatorExpression(left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression)
    """
    @property
    def Left(self) -> CodeExpression:
        """
        Get: Left(self: CodeBinaryOperatorExpression) -> CodeExpression
        Set: Left(self: CodeBinaryOperatorExpression) = value
        """
        ...

    @property
    def Operator(self) -> CodeBinaryOperatorType:
        """
        Get: Operator(self: CodeBinaryOperatorExpression) -> CodeBinaryOperatorType
        Set: Operator(self: CodeBinaryOperatorExpression) = value
        """
        ...

    @property
    def Right(self) -> CodeExpression:
        """
        Get: Right(self: CodeBinaryOperatorExpression) -> CodeExpression
        Set: Right(self: CodeBinaryOperatorExpression) = value
        """
        ...


    def __new__(cls, left:CodeExpression = ..., op:CodeBinaryOperatorType = ..., right:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression)
        """
        ...


class CodeBinaryOperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeBinaryOperatorType, values: Add (0), Assign (5), BitwiseAnd (10), BitwiseOr (9), BooleanAnd (12), BooleanOr (11), Divide (3), GreaterThan (15), GreaterThanOrEqual (16), IdentityEquality (7), IdentityInequality (6), LessThan (13), LessThanOrEqual (14), Modulus (4), Multiply (2), Subtract (1), ValueEquality (8) """
    Add: CodeBinaryOperatorType = ...
    Assign: CodeBinaryOperatorType = ...
    BitwiseAnd: CodeBinaryOperatorType = ...
    BitwiseOr: CodeBinaryOperatorType = ...
    BooleanAnd: CodeBinaryOperatorType = ...
    BooleanOr: CodeBinaryOperatorType = ...
    Divide: CodeBinaryOperatorType = ...
    GreaterThan: CodeBinaryOperatorType = ...
    GreaterThanOrEqual: CodeBinaryOperatorType = ...
    IdentityEquality: CodeBinaryOperatorType = ...
    IdentityInequality: CodeBinaryOperatorType = ...
    LessThan: CodeBinaryOperatorType = ...
    LessThanOrEqual: CodeBinaryOperatorType = ...
    Modulus: CodeBinaryOperatorType = ...
    Multiply: CodeBinaryOperatorType = ...
    Subtract: CodeBinaryOperatorType = ...
    ValueEquality: CodeBinaryOperatorType = ...
    value__ = ...


class CodeCastExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeCastExpression()
    CodeCastExpression(targetType: CodeTypeReference, expression: CodeExpression)
    CodeCastExpression(targetType: str, expression: CodeExpression)
    CodeCastExpression(targetType: Type, expression: CodeExpression)
    """
    @property
    def Expression(self) -> CodeExpression:
        """
        Get: Expression(self: CodeCastExpression) -> CodeExpression
        Set: Expression(self: CodeCastExpression) = value
        """
        ...

    @property
    def TargetType(self) -> CodeTypeReference:
        """
        Get: TargetType(self: CodeCastExpression) -> CodeTypeReference
        Set: TargetType(self: CodeCastExpression) = value
        """
        ...


    def __new__(cls, targetType:CodeTypeReference = ..., expression:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetType: CodeTypeReference, expression: CodeExpression)
        __new__(cls: type, targetType: str, expression: CodeExpression)
        __new__(cls: type, targetType: Type, expression: CodeExpression)
        """
        ...


class CodeCatchClause: # skipped bases: <type 'object'>, <type 'object'>
    """
    CodeCatchClause()
    CodeCatchClause(localName: str)
    CodeCatchClause(localName: str, catchExceptionType: CodeTypeReference)
    CodeCatchClause(localName: str, catchExceptionType: CodeTypeReference, *statements: Array[CodeStatement])
    """
    @property
    def CatchExceptionType(self) -> CodeTypeReference:
        """
        Get: CatchExceptionType(self: CodeCatchClause) -> CodeTypeReference
        Set: CatchExceptionType(self: CodeCatchClause) = value
        """
        ...

    @property
    def LocalName(self) -> str:
        """
        Get: LocalName(self: CodeCatchClause) -> str
        Set: LocalName(self: CodeCatchClause) = value
        """
        ...

    @property
    def Statements(self) -> CodeStatementCollection:
        """ Get: Statements(self: CodeCatchClause) -> CodeStatementCollection """
        ...



class CodeCatchClauseCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeCatchClauseCollection()
    CodeCatchClauseCollection(value: CodeCatchClauseCollection)
    CodeCatchClauseCollection(value: Array[CodeCatchClause])
    """
    def Add(self, value:CodeCatchClause) -> int:
        """ Add(self: CodeCatchClauseCollection, value: CodeCatchClause) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeCatchClauseCollection, value: Array[CodeCatchClause])AddRange(self: CodeCatchClauseCollection, value: CodeCatchClauseCollection) """
        ...

    def Contains(self, value:CodeCatchClause) -> bool:
        """ Contains(self: CodeCatchClauseCollection, value: CodeCatchClause) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeCatchClauseCollection, array: Array[CodeCatchClause], index: int) """
        ...

    def IndexOf(self, value:CodeCatchClause) -> int:
        """ IndexOf(self: CodeCatchClauseCollection, value: CodeCatchClause) -> int """
        ...

    def Insert(self, index:int, value:CodeCatchClause): # -> 
        """ Insert(self: CodeCatchClauseCollection, index: int, value: CodeCatchClause) """
        ...

    def Remove(self, value:CodeCatchClause): # -> 
        """ Remove(self: CodeCatchClauseCollection, value: CodeCatchClause) """
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


class CodeDirective(CodeObject): # skipped bases: <type 'object'>
    """ CodeDirective() """
    pass

class CodeChecksumPragma(CodeDirective): # skipped bases: <type 'object'>
    """
    CodeChecksumPragma()
    CodeChecksumPragma(fileName: str, checksumAlgorithmId: Guid, checksumData: Array[Byte])
    """
    @property
    def ChecksumAlgorithmId(self) -> Guid:
        """
        Get: ChecksumAlgorithmId(self: CodeChecksumPragma) -> Guid
        Set: ChecksumAlgorithmId(self: CodeChecksumPragma) = value
        """
        ...

    @property
    def ChecksumData(self) -> Array:
        """
        Get: ChecksumData(self: CodeChecksumPragma) -> Array[Byte]
        Set: ChecksumData(self: CodeChecksumPragma) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: CodeChecksumPragma) -> str
        Set: FileName(self: CodeChecksumPragma) = value
        """
        ...


    def __new__(cls, fileName:str = ..., checksumAlgorithmId:Guid = ..., checksumData:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, checksumAlgorithmId: Guid, checksumData: Array[Byte])
        """
        ...


class CodeComment(CodeObject): # skipped bases: <type 'object'>
    """
    CodeComment()
    CodeComment(text: str)
    CodeComment(text: str, docComment: bool)
    """
    @property
    def DocComment(self) -> bool:
        """
        Get: DocComment(self: CodeComment) -> bool
        Set: DocComment(self: CodeComment) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: CodeComment) -> str
        Set: Text(self: CodeComment) = value
        """
        ...


    def __new__(cls, text:str = ..., docComment:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, docComment: bool)
        """
        ...


class CodeCommentStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeCommentStatement()
    CodeCommentStatement(comment: CodeComment)
    CodeCommentStatement(text: str)
    CodeCommentStatement(text: str, docComment: bool)
    """
    @property
    def Comment(self) -> CodeComment:
        """
        Get: Comment(self: CodeCommentStatement) -> CodeComment
        Set: Comment(self: CodeCommentStatement) = value
        """
        ...


    def __new__(cls, *__args:CodeComment) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, comment: CodeComment)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, docComment: bool)
        """
        ...


class CodeCommentStatementCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeCommentStatementCollection()
    CodeCommentStatementCollection(value: CodeCommentStatementCollection)
    CodeCommentStatementCollection(value: Array[CodeCommentStatement])
    """
    def Add(self, value:CodeCommentStatement) -> int:
        """ Add(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeCommentStatementCollection, value: Array[CodeCommentStatement])AddRange(self: CodeCommentStatementCollection, value: CodeCommentStatementCollection) """
        ...

    def Contains(self, value:CodeCommentStatement) -> bool:
        """ Contains(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeCommentStatementCollection, array: Array[CodeCommentStatement], index: int) """
        ...

    def IndexOf(self, value:CodeCommentStatement) -> int:
        """ IndexOf(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> int """
        ...

    def Insert(self, index:int, value:CodeCommentStatement): # -> 
        """ Insert(self: CodeCommentStatementCollection, index: int, value: CodeCommentStatement) """
        ...

    def Remove(self, value:CodeCommentStatement): # -> 
        """ Remove(self: CodeCommentStatementCollection, value: CodeCommentStatement) """
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


class CodeCompileUnit(CodeObject): # skipped bases: <type 'object'>
    """ CodeCompileUnit() """
    @property
    def AssemblyCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """ Get: AssemblyCustomAttributes(self: CodeCompileUnit) -> CodeAttributeDeclarationCollection """
        ...

    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """ Get: EndDirectives(self: CodeCompileUnit) -> CodeDirectiveCollection """
        ...

    @property
    def Namespaces(self) -> CodeNamespaceCollection:
        """ Get: Namespaces(self: CodeCompileUnit) -> CodeNamespaceCollection """
        ...

    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """ Get: ReferencedAssemblies(self: CodeCompileUnit) -> StringCollection """
        ...

    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """ Get: StartDirectives(self: CodeCompileUnit) -> CodeDirectiveCollection """
        ...



class CodeConditionStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeConditionStatement()
    CodeConditionStatement(condition: CodeExpression, *trueStatements: Array[CodeStatement])
    CodeConditionStatement(condition: CodeExpression, trueStatements: Array[CodeStatement], falseStatements: Array[CodeStatement])
    """
    @property
    def Condition(self) -> CodeExpression:
        """
        Get: Condition(self: CodeConditionStatement) -> CodeExpression
        Set: Condition(self: CodeConditionStatement) = value
        """
        ...

    @property
    def FalseStatements(self) -> CodeStatementCollection:
        """ Get: FalseStatements(self: CodeConditionStatement) -> CodeStatementCollection """
        ...

    @property
    def TrueStatements(self) -> CodeStatementCollection:
        """ Get: TrueStatements(self: CodeConditionStatement) -> CodeStatementCollection """
        ...


    def __new__(cls, condition:CodeExpression = ..., trueStatements:Array = ..., falseStatements:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, condition: CodeExpression, *trueStatements: Array[CodeStatement])
        __new__(cls: type, condition: CodeExpression, trueStatements: Array[CodeStatement], falseStatements: Array[CodeStatement])
        """
        ...


class CodeTypeMember(CodeObject): # skipped bases: <type 'object'>
    """ CodeTypeMember() """
    @property
    def Attributes(self) -> MemberAttributes:
        """
        Get: Attributes(self: CodeTypeMember) -> MemberAttributes
        Set: Attributes(self: CodeTypeMember) = value
        """
        ...

    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """ Get: Comments(self: CodeTypeMember) -> CodeCommentStatementCollection """
        ...

    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """
        Get: CustomAttributes(self: CodeTypeMember) -> CodeAttributeDeclarationCollection
        Set: CustomAttributes(self: CodeTypeMember) = value
        """
        ...

    @property
    def EndDirectives(self) -> CodeDirectiveCollection:
        """ Get: EndDirectives(self: CodeTypeMember) -> CodeDirectiveCollection """
        ...

    @property
    def LinePragma(self) -> CodeLinePragma:
        """
        Get: LinePragma(self: CodeTypeMember) -> CodeLinePragma
        Set: LinePragma(self: CodeTypeMember) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeTypeMember) -> str
        Set: Name(self: CodeTypeMember) = value
        """
        ...

    @property
    def StartDirectives(self) -> CodeDirectiveCollection:
        """ Get: StartDirectives(self: CodeTypeMember) -> CodeDirectiveCollection """
        ...



class CodeMemberMethod(CodeTypeMember): # skipped bases: <type 'object'>
    """ CodeMemberMethod() """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """ Get: ImplementationTypes(self: CodeMemberMethod) -> CodeTypeReferenceCollection """
        ...

    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """ Get: Parameters(self: CodeMemberMethod) -> CodeParameterDeclarationExpressionCollection """
        ...

    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """
        Get: PrivateImplementationType(self: CodeMemberMethod) -> CodeTypeReference
        Set: PrivateImplementationType(self: CodeMemberMethod) = value
        """
        ...

    @property
    def ReturnType(self) -> CodeTypeReference:
        """
        Get: ReturnType(self: CodeMemberMethod) -> CodeTypeReference
        Set: ReturnType(self: CodeMemberMethod) = value
        """
        ...

    @property
    def ReturnTypeCustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """ Get: ReturnTypeCustomAttributes(self: CodeMemberMethod) -> CodeAttributeDeclarationCollection """
        ...

    @property
    def Statements(self) -> CodeStatementCollection:
        """ Get: Statements(self: CodeMemberMethod) -> CodeStatementCollection """
        ...

    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """ Get: TypeParameters(self: CodeMemberMethod) -> CodeTypeParameterCollection """
        ...


    PopulateImplementationTypes = ...
    PopulateParameters = ...
    PopulateStatements = ...


class CodeConstructor(CodeMemberMethod): # skipped bases: <type 'object'>
    """ CodeConstructor() """
    @property
    def BaseConstructorArgs(self) -> CodeExpressionCollection:
        """ Get: BaseConstructorArgs(self: CodeConstructor) -> CodeExpressionCollection """
        ...

    @property
    def ChainedConstructorArgs(self) -> CodeExpressionCollection:
        """ Get: ChainedConstructorArgs(self: CodeConstructor) -> CodeExpressionCollection """
        ...



class CodeDefaultValueExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeDefaultValueExpression()
    CodeDefaultValueExpression(type: CodeTypeReference)
    """
    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeDefaultValueExpression) -> CodeTypeReference
        Set: Type(self: CodeDefaultValueExpression) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        """
        ...


class CodeDelegateCreateExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeDelegateCreateExpression()
    CodeDelegateCreateExpression(delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str)
    """
    @property
    def DelegateType(self) -> CodeTypeReference:
        """
        Get: DelegateType(self: CodeDelegateCreateExpression) -> CodeTypeReference
        Set: DelegateType(self: CodeDelegateCreateExpression) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: CodeDelegateCreateExpression) -> str
        Set: MethodName(self: CodeDelegateCreateExpression) = value
        """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeDelegateCreateExpression) -> CodeExpression
        Set: TargetObject(self: CodeDelegateCreateExpression) = value
        """
        ...


    def __new__(cls, delegateType:CodeTypeReference = ..., targetObject:CodeExpression = ..., methodName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str)
        """
        ...


class CodeDelegateInvokeExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeDelegateInvokeExpression()
    CodeDelegateInvokeExpression(targetObject: CodeExpression)
    CodeDelegateInvokeExpression(targetObject: CodeExpression, *parameters: Array[CodeExpression])
    """
    @property
    def Parameters(self) -> CodeExpressionCollection:
        """ Get: Parameters(self: CodeDelegateInvokeExpression) -> CodeExpressionCollection """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeDelegateInvokeExpression) -> CodeExpression
        Set: TargetObject(self: CodeDelegateInvokeExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., parameters:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, *parameters: Array[CodeExpression])
        """
        ...


class CodeDirectionExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeDirectionExpression()
    CodeDirectionExpression(direction: FieldDirection, expression: CodeExpression)
    """
    @property
    def Direction(self) -> FieldDirection:
        """
        Get: Direction(self: CodeDirectionExpression) -> FieldDirection
        Set: Direction(self: CodeDirectionExpression) = value
        """
        ...

    @property
    def Expression(self) -> CodeExpression:
        """
        Get: Expression(self: CodeDirectionExpression) -> CodeExpression
        Set: Expression(self: CodeDirectionExpression) = value
        """
        ...


    def __new__(cls, direction:FieldDirection = ..., expression:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, direction: FieldDirection, expression: CodeExpression)
        """
        ...


class CodeDirectiveCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeDirectiveCollection()
    CodeDirectiveCollection(value: CodeDirectiveCollection)
    CodeDirectiveCollection(value: Array[CodeDirective])
    """
    def Add(self, value:CodeDirective) -> int:
        """ Add(self: CodeDirectiveCollection, value: CodeDirective) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeDirectiveCollection, value: Array[CodeDirective])AddRange(self: CodeDirectiveCollection, value: CodeDirectiveCollection) """
        ...

    def Contains(self, value:CodeDirective) -> bool:
        """ Contains(self: CodeDirectiveCollection, value: CodeDirective) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeDirectiveCollection, array: Array[CodeDirective], index: int) """
        ...

    def IndexOf(self, value:CodeDirective) -> int:
        """ IndexOf(self: CodeDirectiveCollection, value: CodeDirective) -> int """
        ...

    def Insert(self, index:int, value:CodeDirective): # -> 
        """ Insert(self: CodeDirectiveCollection, index: int, value: CodeDirective) """
        ...

    def Remove(self, value:CodeDirective): # -> 
        """ Remove(self: CodeDirectiveCollection, value: CodeDirective) """
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


class CodeEntryPointMethod(CodeMemberMethod): # skipped bases: <type 'object'>
    """ CodeEntryPointMethod() """
    pass

class CodeEventReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeEventReferenceExpression()
    CodeEventReferenceExpression(targetObject: CodeExpression, eventName: str)
    """
    @property
    def EventName(self) -> str:
        """
        Get: EventName(self: CodeEventReferenceExpression) -> str
        Set: EventName(self: CodeEventReferenceExpression) = value
        """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeEventReferenceExpression) -> CodeExpression
        Set: TargetObject(self: CodeEventReferenceExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., eventName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, eventName: str)
        """
        ...


class CodeExpressionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeExpressionCollection()
    CodeExpressionCollection(value: CodeExpressionCollection)
    CodeExpressionCollection(value: Array[CodeExpression])
    """
    def Add(self, value:CodeExpression) -> int:
        """ Add(self: CodeExpressionCollection, value: CodeExpression) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeExpressionCollection, value: Array[CodeExpression])AddRange(self: CodeExpressionCollection, value: CodeExpressionCollection) """
        ...

    def Contains(self, value:CodeExpression) -> bool:
        """ Contains(self: CodeExpressionCollection, value: CodeExpression) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeExpressionCollection, array: Array[CodeExpression], index: int) """
        ...

    def IndexOf(self, value:CodeExpression) -> int:
        """ IndexOf(self: CodeExpressionCollection, value: CodeExpression) -> int """
        ...

    def Insert(self, index:int, value:CodeExpression): # -> 
        """ Insert(self: CodeExpressionCollection, index: int, value: CodeExpression) """
        ...

    def Remove(self, value:CodeExpression): # -> 
        """ Remove(self: CodeExpressionCollection, value: CodeExpression) """
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


class CodeExpressionStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeExpressionStatement()
    CodeExpressionStatement(expression: CodeExpression)
    """
    @property
    def Expression(self) -> CodeExpression:
        """
        Get: Expression(self: CodeExpressionStatement) -> CodeExpression
        Set: Expression(self: CodeExpressionStatement) = value
        """
        ...


    def __new__(cls, expression:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expression: CodeExpression)
        """
        ...


class CodeFieldReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeFieldReferenceExpression()
    CodeFieldReferenceExpression(targetObject: CodeExpression, fieldName: str)
    """
    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: CodeFieldReferenceExpression) -> str
        Set: FieldName(self: CodeFieldReferenceExpression) = value
        """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeFieldReferenceExpression) -> CodeExpression
        Set: TargetObject(self: CodeFieldReferenceExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., fieldName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, fieldName: str)
        """
        ...


class CodeGotoStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeGotoStatement()
    CodeGotoStatement(label: str)
    """
    @property
    def Label(self) -> str:
        """
        Get: Label(self: CodeGotoStatement) -> str
        Set: Label(self: CodeGotoStatement) = value
        """
        ...


    def __new__(cls, label:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, label: str)
        """
        ...


class CodeIndexerExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeIndexerExpression()
    CodeIndexerExpression(targetObject: CodeExpression, *indices: Array[CodeExpression])
    """
    @property
    def Indices(self) -> CodeExpressionCollection:
        """ Get: Indices(self: CodeIndexerExpression) -> CodeExpressionCollection """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeIndexerExpression) -> CodeExpression
        Set: TargetObject(self: CodeIndexerExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., indices:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, *indices: Array[CodeExpression])
        """
        ...


class CodeIterationStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeIterationStatement()
    CodeIterationStatement(initStatement: CodeStatement, testExpression: CodeExpression, incrementStatement: CodeStatement, *statements: Array[CodeStatement])
    """
    @property
    def IncrementStatement(self) -> CodeStatement:
        """
        Get: IncrementStatement(self: CodeIterationStatement) -> CodeStatement
        Set: IncrementStatement(self: CodeIterationStatement) = value
        """
        ...

    @property
    def InitStatement(self) -> CodeStatement:
        """
        Get: InitStatement(self: CodeIterationStatement) -> CodeStatement
        Set: InitStatement(self: CodeIterationStatement) = value
        """
        ...

    @property
    def Statements(self) -> CodeStatementCollection:
        """ Get: Statements(self: CodeIterationStatement) -> CodeStatementCollection """
        ...

    @property
    def TestExpression(self) -> CodeExpression:
        """
        Get: TestExpression(self: CodeIterationStatement) -> CodeExpression
        Set: TestExpression(self: CodeIterationStatement) = value
        """
        ...


    def __new__(cls, initStatement:CodeStatement = ..., testExpression:CodeExpression = ..., incrementStatement:CodeStatement = ..., statements:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, initStatement: CodeStatement, testExpression: CodeExpression, incrementStatement: CodeStatement, *statements: Array[CodeStatement])
        """
        ...


class CodeLabeledStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeLabeledStatement()
    CodeLabeledStatement(label: str)
    CodeLabeledStatement(label: str, statement: CodeStatement)
    """
    @property
    def Label(self) -> str:
        """
        Get: Label(self: CodeLabeledStatement) -> str
        Set: Label(self: CodeLabeledStatement) = value
        """
        ...

    @property
    def Statement(self) -> CodeStatement:
        """
        Get: Statement(self: CodeLabeledStatement) -> CodeStatement
        Set: Statement(self: CodeLabeledStatement) = value
        """
        ...


    def __new__(cls, label:str = ..., statement:CodeStatement = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, label: str)
        __new__(cls: type, label: str, statement: CodeStatement)
        """
        ...


class CodeLinePragma: # skipped bases: <type 'object'>, <type 'object'>
    """
    CodeLinePragma()
    CodeLinePragma(fileName: str, lineNumber: int)
    """
    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: CodeLinePragma) -> str
        Set: FileName(self: CodeLinePragma) = value
        """
        ...

    @property
    def LineNumber(self) -> int:
        """
        Get: LineNumber(self: CodeLinePragma) -> int
        Set: LineNumber(self: CodeLinePragma) = value
        """
        ...



class CodeMemberEvent(CodeTypeMember): # skipped bases: <type 'object'>
    """ CodeMemberEvent() """
    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """ Get: ImplementationTypes(self: CodeMemberEvent) -> CodeTypeReferenceCollection """
        ...

    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """
        Get: PrivateImplementationType(self: CodeMemberEvent) -> CodeTypeReference
        Set: PrivateImplementationType(self: CodeMemberEvent) = value
        """
        ...

    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeMemberEvent) -> CodeTypeReference
        Set: Type(self: CodeMemberEvent) = value
        """
        ...



class CodeMemberField(CodeTypeMember): # skipped bases: <type 'object'>
    """
    CodeMemberField()
    CodeMemberField(type: CodeTypeReference, name: str)
    CodeMemberField(type: str, name: str)
    CodeMemberField(type: Type, name: str)
    """
    @property
    def InitExpression(self) -> CodeExpression:
        """
        Get: InitExpression(self: CodeMemberField) -> CodeExpression
        Set: InitExpression(self: CodeMemberField) = value
        """
        ...

    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeMemberField) -> CodeTypeReference
        Set: Type(self: CodeMemberField) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        """
        ...


class CodeMemberProperty(CodeTypeMember): # skipped bases: <type 'object'>
    """ CodeMemberProperty() """
    @property
    def GetStatements(self) -> CodeStatementCollection:
        """ Get: GetStatements(self: CodeMemberProperty) -> CodeStatementCollection """
        ...

    @property
    def HasGet(self) -> bool:
        """
        Get: HasGet(self: CodeMemberProperty) -> bool
        Set: HasGet(self: CodeMemberProperty) = value
        """
        ...

    @property
    def HasSet(self) -> bool:
        """
        Get: HasSet(self: CodeMemberProperty) -> bool
        Set: HasSet(self: CodeMemberProperty) = value
        """
        ...

    @property
    def ImplementationTypes(self) -> CodeTypeReferenceCollection:
        """ Get: ImplementationTypes(self: CodeMemberProperty) -> CodeTypeReferenceCollection """
        ...

    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """ Get: Parameters(self: CodeMemberProperty) -> CodeParameterDeclarationExpressionCollection """
        ...

    @property
    def PrivateImplementationType(self) -> CodeTypeReference:
        """
        Get: PrivateImplementationType(self: CodeMemberProperty) -> CodeTypeReference
        Set: PrivateImplementationType(self: CodeMemberProperty) = value
        """
        ...

    @property
    def SetStatements(self) -> CodeStatementCollection:
        """ Get: SetStatements(self: CodeMemberProperty) -> CodeStatementCollection """
        ...

    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeMemberProperty) -> CodeTypeReference
        Set: Type(self: CodeMemberProperty) = value
        """
        ...



class CodeMethodInvokeExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeMethodInvokeExpression()
    CodeMethodInvokeExpression(method: CodeMethodReferenceExpression, *parameters: Array[CodeExpression])
    CodeMethodInvokeExpression(targetObject: CodeExpression, methodName: str, *parameters: Array[CodeExpression])
    """
    @property
    def Method(self) -> CodeMethodReferenceExpression:
        """
        Get: Method(self: CodeMethodInvokeExpression) -> CodeMethodReferenceExpression
        Set: Method(self: CodeMethodInvokeExpression) = value
        """
        ...

    @property
    def Parameters(self) -> CodeExpressionCollection:
        """ Get: Parameters(self: CodeMethodInvokeExpression) -> CodeExpressionCollection """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, method: CodeMethodReferenceExpression, *parameters: Array[CodeExpression])
        __new__(cls: type, targetObject: CodeExpression, methodName: str, *parameters: Array[CodeExpression])
        """
        ...


class CodeMethodReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeMethodReferenceExpression()
    CodeMethodReferenceExpression(targetObject: CodeExpression, methodName: str)
    CodeMethodReferenceExpression(targetObject: CodeExpression, methodName: str, *typeParameters: Array[CodeTypeReference])
    """
    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: CodeMethodReferenceExpression) -> str
        Set: MethodName(self: CodeMethodReferenceExpression) = value
        """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodeMethodReferenceExpression) -> CodeExpression
        Set: TargetObject(self: CodeMethodReferenceExpression) = value
        """
        ...

    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """ Get: TypeArguments(self: CodeMethodReferenceExpression) -> CodeTypeReferenceCollection """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., methodName:str = ..., typeParameters:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, methodName: str)
        __new__(cls: type, targetObject: CodeExpression, methodName: str, *typeParameters: Array[CodeTypeReference])
        """
        ...


class CodeMethodReturnStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeMethodReturnStatement()
    CodeMethodReturnStatement(expression: CodeExpression)
    """
    @property
    def Expression(self) -> CodeExpression:
        """
        Get: Expression(self: CodeMethodReturnStatement) -> CodeExpression
        Set: Expression(self: CodeMethodReturnStatement) = value
        """
        ...


    def __new__(cls, expression:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expression: CodeExpression)
        """
        ...


class CodeNamespace(CodeObject): # skipped bases: <type 'object'>
    """
    CodeNamespace()
    CodeNamespace(name: str)
    """
    @property
    def Comments(self) -> CodeCommentStatementCollection:
        """ Get: Comments(self: CodeNamespace) -> CodeCommentStatementCollection """
        ...

    @property
    def Imports(self) -> CodeNamespaceImportCollection:
        """ Get: Imports(self: CodeNamespace) -> CodeNamespaceImportCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeNamespace) -> str
        Set: Name(self: CodeNamespace) = value
        """
        ...

    @property
    def Types(self) -> CodeTypeDeclarationCollection:
        """ Get: Types(self: CodeNamespace) -> CodeTypeDeclarationCollection """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...

    PopulateComments = ...
    PopulateImports = ...
    PopulateTypes = ...


class CodeNamespaceCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeNamespaceCollection()
    CodeNamespaceCollection(value: CodeNamespaceCollection)
    CodeNamespaceCollection(value: Array[CodeNamespace])
    """
    def Add(self, value:CodeNamespace) -> int:
        """ Add(self: CodeNamespaceCollection, value: CodeNamespace) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeNamespaceCollection, value: Array[CodeNamespace])AddRange(self: CodeNamespaceCollection, value: CodeNamespaceCollection) """
        ...

    def Contains(self, value:CodeNamespace) -> bool:
        """ Contains(self: CodeNamespaceCollection, value: CodeNamespace) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeNamespaceCollection, array: Array[CodeNamespace], index: int) """
        ...

    def IndexOf(self, value:CodeNamespace) -> int:
        """ IndexOf(self: CodeNamespaceCollection, value: CodeNamespace) -> int """
        ...

    def Insert(self, index:int, value:CodeNamespace): # -> 
        """ Insert(self: CodeNamespaceCollection, index: int, value: CodeNamespace) """
        ...

    def Remove(self, value:CodeNamespace): # -> 
        """ Remove(self: CodeNamespaceCollection, value: CodeNamespace) """
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


class CodeNamespaceImport(CodeObject): # skipped bases: <type 'object'>
    """
    CodeNamespaceImport()
    CodeNamespaceImport(nameSpace: str)
    """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """
        Get: LinePragma(self: CodeNamespaceImport) -> CodeLinePragma
        Set: LinePragma(self: CodeNamespaceImport) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: CodeNamespaceImport) -> str
        Set: Namespace(self: CodeNamespaceImport) = value
        """
        ...


    def __new__(cls, nameSpace:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, nameSpace: str)
        """
        ...


class CodeNamespaceImportCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CodeNamespaceImportCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CodeNamespaceImportCollection) -> int """
        ...


    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeNamespaceImportCollection, value: Array[CodeNamespaceImport]) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CodeNamespaceImportCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class CodeObjectCreateExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeObjectCreateExpression()
    CodeObjectCreateExpression(createType: CodeTypeReference, *parameters: Array[CodeExpression])
    CodeObjectCreateExpression(createType: str, *parameters: Array[CodeExpression])
    CodeObjectCreateExpression(createType: Type, *parameters: Array[CodeExpression])
    """
    @property
    def CreateType(self) -> CodeTypeReference:
        """
        Get: CreateType(self: CodeObjectCreateExpression) -> CodeTypeReference
        Set: CreateType(self: CodeObjectCreateExpression) = value
        """
        ...

    @property
    def Parameters(self) -> CodeExpressionCollection:
        """ Get: Parameters(self: CodeObjectCreateExpression) -> CodeExpressionCollection """
        ...


    def __new__(cls, createType:CodeTypeReference = ..., parameters:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, createType: CodeTypeReference, *parameters: Array[CodeExpression])
        __new__(cls: type, createType: str, *parameters: Array[CodeExpression])
        __new__(cls: type, createType: Type, *parameters: Array[CodeExpression])
        """
        ...


class CodeParameterDeclarationExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeParameterDeclarationExpression()
    CodeParameterDeclarationExpression(type: CodeTypeReference, name: str)
    CodeParameterDeclarationExpression(type: str, name: str)
    CodeParameterDeclarationExpression(type: Type, name: str)
    """
    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """
        Get: CustomAttributes(self: CodeParameterDeclarationExpression) -> CodeAttributeDeclarationCollection
        Set: CustomAttributes(self: CodeParameterDeclarationExpression) = value
        """
        ...

    @property
    def Direction(self) -> FieldDirection:
        """
        Get: Direction(self: CodeParameterDeclarationExpression) -> FieldDirection
        Set: Direction(self: CodeParameterDeclarationExpression) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeParameterDeclarationExpression) -> str
        Set: Name(self: CodeParameterDeclarationExpression) = value
        """
        ...

    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeParameterDeclarationExpression) -> CodeTypeReference
        Set: Type(self: CodeParameterDeclarationExpression) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        """
        ...


class CodeParameterDeclarationExpressionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeParameterDeclarationExpressionCollection()
    CodeParameterDeclarationExpressionCollection(value: CodeParameterDeclarationExpressionCollection)
    CodeParameterDeclarationExpressionCollection(value: Array[CodeParameterDeclarationExpression])
    """
    def Add(self, value:CodeParameterDeclarationExpression) -> int:
        """ Add(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeParameterDeclarationExpressionCollection, value: Array[CodeParameterDeclarationExpression])AddRange(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpressionCollection) """
        ...

    def Contains(self, value:CodeParameterDeclarationExpression) -> bool:
        """ Contains(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeParameterDeclarationExpressionCollection, array: Array[CodeParameterDeclarationExpression], index: int) """
        ...

    def IndexOf(self, value:CodeParameterDeclarationExpression) -> int:
        """ IndexOf(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> int """
        ...

    def Insert(self, index:int, value:CodeParameterDeclarationExpression): # -> 
        """ Insert(self: CodeParameterDeclarationExpressionCollection, index: int, value: CodeParameterDeclarationExpression) """
        ...

    def Remove(self, value:CodeParameterDeclarationExpression): # -> 
        """ Remove(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) """
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


class CodePrimitiveExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodePrimitiveExpression()
    CodePrimitiveExpression(value: object)
    """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: CodePrimitiveExpression) -> object
        Set: Value(self: CodePrimitiveExpression) = value
        """
        ...


    def __new__(cls, value:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, value: object)
        """
        ...


class CodePropertyReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodePropertyReferenceExpression()
    CodePropertyReferenceExpression(targetObject: CodeExpression, propertyName: str)
    """
    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: CodePropertyReferenceExpression) -> str
        Set: PropertyName(self: CodePropertyReferenceExpression) = value
        """
        ...

    @property
    def TargetObject(self) -> CodeExpression:
        """
        Get: TargetObject(self: CodePropertyReferenceExpression) -> CodeExpression
        Set: TargetObject(self: CodePropertyReferenceExpression) = value
        """
        ...


    def __new__(cls, targetObject:CodeExpression = ..., propertyName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, propertyName: str)
        """
        ...


class CodePropertySetValueReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """ CodePropertySetValueReferenceExpression() """
    pass

class CodeRegionDirective(CodeDirective): # skipped bases: <type 'object'>
    """
    CodeRegionDirective()
    CodeRegionDirective(regionMode: CodeRegionMode, regionText: str)
    """
    @property
    def RegionMode(self) -> CodeRegionMode:
        """
        Get: RegionMode(self: CodeRegionDirective) -> CodeRegionMode
        Set: RegionMode(self: CodeRegionDirective) = value
        """
        ...

    @property
    def RegionText(self) -> str:
        """
        Get: RegionText(self: CodeRegionDirective) -> str
        Set: RegionText(self: CodeRegionDirective) = value
        """
        ...


    def __new__(cls, regionMode:CodeRegionMode = ..., regionText:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, regionMode: CodeRegionMode, regionText: str)
        """
        ...


class CodeRegionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeRegionMode, values: End (2), None (0), Start (1) """
    End: CodeRegionMode = ...
    Start: CodeRegionMode = ...
    value__ = ...


class CodeRemoveEventStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeRemoveEventStatement()
    CodeRemoveEventStatement(eventRef: CodeEventReferenceExpression, listener: CodeExpression)
    CodeRemoveEventStatement(targetObject: CodeExpression, eventName: str, listener: CodeExpression)
    """
    @property
    def Event(self) -> CodeEventReferenceExpression:
        """
        Get: Event(self: CodeRemoveEventStatement) -> CodeEventReferenceExpression
        Set: Event(self: CodeRemoveEventStatement) = value
        """
        ...

    @property
    def Listener(self) -> CodeExpression:
        """
        Get: Listener(self: CodeRemoveEventStatement) -> CodeExpression
        Set: Listener(self: CodeRemoveEventStatement) = value
        """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, eventRef: CodeEventReferenceExpression, listener: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, eventName: str, listener: CodeExpression)
        """
        ...


class CodeSnippetCompileUnit(CodeCompileUnit): # skipped bases: <type 'object'>
    """
    CodeSnippetCompileUnit()
    CodeSnippetCompileUnit(value: str)
    """
    @property
    def LinePragma(self) -> CodeLinePragma:
        """
        Get: LinePragma(self: CodeSnippetCompileUnit) -> CodeLinePragma
        Set: LinePragma(self: CodeSnippetCompileUnit) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: CodeSnippetCompileUnit) -> str
        Set: Value(self: CodeSnippetCompileUnit) = value
        """
        ...


    def __new__(cls, value:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        ...


class CodeSnippetExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeSnippetExpression()
    CodeSnippetExpression(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: CodeSnippetExpression) -> str
        Set: Value(self: CodeSnippetExpression) = value
        """
        ...


    def __new__(cls, value:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        ...


class CodeSnippetStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeSnippetStatement()
    CodeSnippetStatement(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: CodeSnippetStatement) -> str
        Set: Value(self: CodeSnippetStatement) = value
        """
        ...


    def __new__(cls, value:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        ...


class CodeSnippetTypeMember(CodeTypeMember): # skipped bases: <type 'object'>
    """
    CodeSnippetTypeMember()
    CodeSnippetTypeMember(text: str)
    """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: CodeSnippetTypeMember) -> str
        Set: Text(self: CodeSnippetTypeMember) = value
        """
        ...


    def __new__(cls, text:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        """
        ...


class CodeStatementCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeStatementCollection()
    CodeStatementCollection(value: CodeStatementCollection)
    CodeStatementCollection(value: Array[CodeStatement])
    """
    def Add(self, value:CodeStatement) -> int:
        """
        Add(self: CodeStatementCollection, value: CodeStatement) -> int
        Add(self: CodeStatementCollection, value: CodeExpression) -> int
        """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeStatementCollection, value: Array[CodeStatement])AddRange(self: CodeStatementCollection, value: CodeStatementCollection) """
        ...

    def Contains(self, value:CodeStatement) -> bool:
        """ Contains(self: CodeStatementCollection, value: CodeStatement) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeStatementCollection, array: Array[CodeStatement], index: int) """
        ...

    def IndexOf(self, value:CodeStatement) -> int:
        """ IndexOf(self: CodeStatementCollection, value: CodeStatement) -> int """
        ...

    def Insert(self, index:int, value:CodeStatement): # -> 
        """ Insert(self: CodeStatementCollection, index: int, value: CodeStatement) """
        ...

    def Remove(self, value:CodeStatement): # -> 
        """ Remove(self: CodeStatementCollection, value: CodeStatement) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CodeThisReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """ CodeThisReferenceExpression() """
    pass

class CodeThrowExceptionStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeThrowExceptionStatement()
    CodeThrowExceptionStatement(toThrow: CodeExpression)
    """
    @property
    def ToThrow(self) -> CodeExpression:
        """
        Get: ToThrow(self: CodeThrowExceptionStatement) -> CodeExpression
        Set: ToThrow(self: CodeThrowExceptionStatement) = value
        """
        ...


    def __new__(cls, toThrow:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, toThrow: CodeExpression)
        """
        ...


class CodeTryCatchFinallyStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeTryCatchFinallyStatement()
    CodeTryCatchFinallyStatement(tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause])
    CodeTryCatchFinallyStatement(tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause], finallyStatements: Array[CodeStatement])
    """
    @property
    def CatchClauses(self) -> CodeCatchClauseCollection:
        """ Get: CatchClauses(self: CodeTryCatchFinallyStatement) -> CodeCatchClauseCollection """
        ...

    @property
    def FinallyStatements(self) -> CodeStatementCollection:
        """ Get: FinallyStatements(self: CodeTryCatchFinallyStatement) -> CodeStatementCollection """
        ...

    @property
    def TryStatements(self) -> CodeStatementCollection:
        """ Get: TryStatements(self: CodeTryCatchFinallyStatement) -> CodeStatementCollection """
        ...


    def __new__(cls, tryStatements:Array = ..., catchClauses:Array = ..., finallyStatements:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause])
        __new__(cls: type, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause], finallyStatements: Array[CodeStatement])
        """
        ...


class CodeTypeConstructor(CodeMemberMethod): # skipped bases: <type 'object'>
    """ CodeTypeConstructor() """
    pass

class CodeTypeDeclaration(CodeTypeMember): # skipped bases: <type 'object'>
    """
    CodeTypeDeclaration()
    CodeTypeDeclaration(name: str)
    """
    @property
    def BaseTypes(self) -> CodeTypeReferenceCollection:
        """ Get: BaseTypes(self: CodeTypeDeclaration) -> CodeTypeReferenceCollection """
        ...

    @property
    def IsClass(self) -> bool:
        """
        Get: IsClass(self: CodeTypeDeclaration) -> bool
        Set: IsClass(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def IsEnum(self) -> bool:
        """
        Get: IsEnum(self: CodeTypeDeclaration) -> bool
        Set: IsEnum(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def IsInterface(self) -> bool:
        """
        Get: IsInterface(self: CodeTypeDeclaration) -> bool
        Set: IsInterface(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def IsPartial(self) -> bool:
        """
        Get: IsPartial(self: CodeTypeDeclaration) -> bool
        Set: IsPartial(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def IsStruct(self) -> bool:
        """
        Get: IsStruct(self: CodeTypeDeclaration) -> bool
        Set: IsStruct(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def Members(self) -> CodeTypeMemberCollection:
        """ Get: Members(self: CodeTypeDeclaration) -> CodeTypeMemberCollection """
        ...

    @property
    def TypeAttributes(self) -> TypeAttributes:
        """
        Get: TypeAttributes(self: CodeTypeDeclaration) -> TypeAttributes
        Set: TypeAttributes(self: CodeTypeDeclaration) = value
        """
        ...

    @property
    def TypeParameters(self) -> CodeTypeParameterCollection:
        """ Get: TypeParameters(self: CodeTypeDeclaration) -> CodeTypeParameterCollection """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...

    PopulateBaseTypes = ...
    PopulateMembers = ...


class CodeTypeDeclarationCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeTypeDeclarationCollection()
    CodeTypeDeclarationCollection(value: CodeTypeDeclarationCollection)
    CodeTypeDeclarationCollection(value: Array[CodeTypeDeclaration])
    """
    def Add(self, value:CodeTypeDeclaration) -> int:
        """ Add(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeTypeDeclarationCollection, value: Array[CodeTypeDeclaration])AddRange(self: CodeTypeDeclarationCollection, value: CodeTypeDeclarationCollection) """
        ...

    def Contains(self, value:CodeTypeDeclaration) -> bool:
        """ Contains(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeTypeDeclarationCollection, array: Array[CodeTypeDeclaration], index: int) """
        ...

    def IndexOf(self, value:CodeTypeDeclaration) -> int:
        """ IndexOf(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> int """
        ...

    def Insert(self, index:int, value:CodeTypeDeclaration): # -> 
        """ Insert(self: CodeTypeDeclarationCollection, index: int, value: CodeTypeDeclaration) """
        ...

    def Remove(self, value:CodeTypeDeclaration): # -> 
        """ Remove(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) """
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


class CodeTypeDelegate(CodeTypeDeclaration): # skipped bases: <type 'object'>
    """
    CodeTypeDelegate()
    CodeTypeDelegate(name: str)
    """
    @property
    def Parameters(self) -> CodeParameterDeclarationExpressionCollection:
        """ Get: Parameters(self: CodeTypeDelegate) -> CodeParameterDeclarationExpressionCollection """
        ...

    @property
    def ReturnType(self) -> CodeTypeReference:
        """
        Get: ReturnType(self: CodeTypeDelegate) -> CodeTypeReference
        Set: ReturnType(self: CodeTypeDelegate) = value
        """
        ...



class CodeTypeMemberCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeTypeMemberCollection()
    CodeTypeMemberCollection(value: CodeTypeMemberCollection)
    CodeTypeMemberCollection(value: Array[CodeTypeMember])
    """
    def Add(self, value:CodeTypeMember) -> int:
        """ Add(self: CodeTypeMemberCollection, value: CodeTypeMember) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeTypeMemberCollection, value: Array[CodeTypeMember])AddRange(self: CodeTypeMemberCollection, value: CodeTypeMemberCollection) """
        ...

    def Contains(self, value:CodeTypeMember) -> bool:
        """ Contains(self: CodeTypeMemberCollection, value: CodeTypeMember) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeTypeMemberCollection, array: Array[CodeTypeMember], index: int) """
        ...

    def IndexOf(self, value:CodeTypeMember) -> int:
        """ IndexOf(self: CodeTypeMemberCollection, value: CodeTypeMember) -> int """
        ...

    def Insert(self, index:int, value:CodeTypeMember): # -> 
        """ Insert(self: CodeTypeMemberCollection, index: int, value: CodeTypeMember) """
        ...

    def Remove(self, value:CodeTypeMember): # -> 
        """ Remove(self: CodeTypeMemberCollection, value: CodeTypeMember) """
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


class CodeTypeOfExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeTypeOfExpression()
    CodeTypeOfExpression(type: CodeTypeReference)
    CodeTypeOfExpression(type: str)
    CodeTypeOfExpression(type: Type)
    """
    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeTypeOfExpression) -> CodeTypeReference
        Set: Type(self: CodeTypeOfExpression) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        ...


class CodeTypeParameter(CodeObject): # skipped bases: <type 'object'>
    """
    CodeTypeParameter()
    CodeTypeParameter(name: str)
    """
    @property
    def Constraints(self) -> CodeTypeReferenceCollection:
        """ Get: Constraints(self: CodeTypeParameter) -> CodeTypeReferenceCollection """
        ...

    @property
    def CustomAttributes(self) -> CodeAttributeDeclarationCollection:
        """ Get: CustomAttributes(self: CodeTypeParameter) -> CodeAttributeDeclarationCollection """
        ...

    @property
    def HasConstructorConstraint(self) -> bool:
        """
        Get: HasConstructorConstraint(self: CodeTypeParameter) -> bool
        Set: HasConstructorConstraint(self: CodeTypeParameter) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeTypeParameter) -> str
        Set: Name(self: CodeTypeParameter) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class CodeTypeParameterCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeTypeParameterCollection()
    CodeTypeParameterCollection(value: CodeTypeParameterCollection)
    CodeTypeParameterCollection(value: Array[CodeTypeParameter])
    """
    def Add(self, value:CodeTypeParameter) -> int:
        """
        Add(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> int
        Add(self: CodeTypeParameterCollection, value: str)
        """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeTypeParameterCollection, value: Array[CodeTypeParameter])AddRange(self: CodeTypeParameterCollection, value: CodeTypeParameterCollection) """
        ...

    def Contains(self, value:CodeTypeParameter) -> bool:
        """ Contains(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeTypeParameterCollection, array: Array[CodeTypeParameter], index: int) """
        ...

    def IndexOf(self, value:CodeTypeParameter) -> int:
        """ IndexOf(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> int """
        ...

    def Insert(self, index:int, value:CodeTypeParameter): # -> 
        """ Insert(self: CodeTypeParameterCollection, index: int, value: CodeTypeParameter) """
        ...

    def Remove(self, value:CodeTypeParameter): # -> 
        """ Remove(self: CodeTypeParameterCollection, value: CodeTypeParameter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CodeTypeReference(CodeObject): # skipped bases: <type 'object'>
    """
    CodeTypeReference()
    CodeTypeReference(type: Type)
    CodeTypeReference(type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions)
    CodeTypeReference(typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions)
    CodeTypeReference(typeName: str)
    CodeTypeReference(typeName: str, *typeArguments: Array[CodeTypeReference])
    CodeTypeReference(typeParameter: CodeTypeParameter)
    CodeTypeReference(baseType: str, rank: int)
    CodeTypeReference(arrayType: CodeTypeReference, rank: int)
    """
    @property
    def ArrayElementType(self) -> CodeTypeReference:
        """
        Get: ArrayElementType(self: CodeTypeReference) -> CodeTypeReference
        Set: ArrayElementType(self: CodeTypeReference) = value
        """
        ...

    @property
    def ArrayRank(self) -> int:
        """
        Get: ArrayRank(self: CodeTypeReference) -> int
        Set: ArrayRank(self: CodeTypeReference) = value
        """
        ...

    @property
    def BaseType(self) -> str:
        """
        Get: BaseType(self: CodeTypeReference) -> str
        Set: BaseType(self: CodeTypeReference) = value
        """
        ...

    @property
    def Options(self) -> CodeTypeReferenceOptions:
        """
        Get: Options(self: CodeTypeReference) -> CodeTypeReferenceOptions
        Set: Options(self: CodeTypeReference) = value
        """
        ...

    @property
    def TypeArguments(self) -> CodeTypeReferenceCollection:
        """ Get: TypeArguments(self: CodeTypeReference) -> CodeTypeReferenceCollection """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions)
        __new__(cls: type, typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions)
        __new__(cls: type, typeName: str)
        __new__(cls: type, typeName: str, *typeArguments: Array[CodeTypeReference])
        __new__(cls: type, typeParameter: CodeTypeParameter)
        __new__(cls: type, baseType: str, rank: int)
        __new__(cls: type, arrayType: CodeTypeReference, rank: int)
        """
        ...


class CodeTypeReferenceCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CodeTypeReferenceCollection()
    CodeTypeReferenceCollection(value: CodeTypeReferenceCollection)
    CodeTypeReferenceCollection(value: Array[CodeTypeReference])
    """
    def Add(self, value:CodeTypeReference) -> int:
        """
        Add(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> int
        Add(self: CodeTypeReferenceCollection, value: str)Add(self: CodeTypeReferenceCollection, value: Type)
        """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CodeTypeReferenceCollection, value: Array[CodeTypeReference])AddRange(self: CodeTypeReferenceCollection, value: CodeTypeReferenceCollection) """
        ...

    def Contains(self, value:CodeTypeReference) -> bool:
        """ Contains(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CodeTypeReferenceCollection, array: Array[CodeTypeReference], index: int) """
        ...

    def IndexOf(self, value:CodeTypeReference) -> int:
        """ IndexOf(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> int """
        ...

    def Insert(self, index:int, value:CodeTypeReference): # -> 
        """ Insert(self: CodeTypeReferenceCollection, index: int, value: CodeTypeReference) """
        ...

    def Remove(self, value:CodeTypeReference): # -> 
        """ Remove(self: CodeTypeReferenceCollection, value: CodeTypeReference) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CodeTypeReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeTypeReferenceExpression()
    CodeTypeReferenceExpression(type: CodeTypeReference)
    CodeTypeReferenceExpression(type: str)
    CodeTypeReferenceExpression(type: Type)
    """
    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeTypeReferenceExpression) -> CodeTypeReference
        Set: Type(self: CodeTypeReferenceExpression) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        ...


class CodeTypeReferenceOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CodeTypeReferenceOptions, values: GenericTypeParameter (2), GlobalReference (1) """
    GenericTypeParameter: CodeTypeReferenceOptions = ...
    GlobalReference: CodeTypeReferenceOptions = ...
    value__ = ...


class CodeVariableDeclarationStatement(CodeStatement): # skipped bases: <type 'object'>
    """
    CodeVariableDeclarationStatement()
    CodeVariableDeclarationStatement(type: CodeTypeReference, name: str)
    CodeVariableDeclarationStatement(type: str, name: str)
    CodeVariableDeclarationStatement(type: Type, name: str)
    CodeVariableDeclarationStatement(type: CodeTypeReference, name: str, initExpression: CodeExpression)
    CodeVariableDeclarationStatement(type: str, name: str, initExpression: CodeExpression)
    CodeVariableDeclarationStatement(type: Type, name: str, initExpression: CodeExpression)
    """
    @property
    def InitExpression(self) -> CodeExpression:
        """
        Get: InitExpression(self: CodeVariableDeclarationStatement) -> CodeExpression
        Set: InitExpression(self: CodeVariableDeclarationStatement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeVariableDeclarationStatement) -> str
        Set: Name(self: CodeVariableDeclarationStatement) = value
        """
        ...

    @property
    def Type(self) -> CodeTypeReference:
        """
        Get: Type(self: CodeVariableDeclarationStatement) -> CodeTypeReference
        Set: Type(self: CodeVariableDeclarationStatement) = value
        """
        ...


    def __new__(cls, type:CodeTypeReference = ..., name:str = ..., initExpression:CodeExpression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        __new__(cls: type, type: CodeTypeReference, name: str, initExpression: CodeExpression)
        __new__(cls: type, type: str, name: str, initExpression: CodeExpression)
        __new__(cls: type, type: Type, name: str, initExpression: CodeExpression)
        """
        ...


class CodeVariableReferenceExpression(CodeExpression): # skipped bases: <type 'object'>
    """
    CodeVariableReferenceExpression()
    CodeVariableReferenceExpression(variableName: str)
    """
    @property
    def VariableName(self) -> str:
        """
        Get: VariableName(self: CodeVariableReferenceExpression) -> str
        Set: VariableName(self: CodeVariableReferenceExpression) = value
        """
        ...


    def __new__(cls, variableName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, variableName: str)
        """
        ...


class FieldDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FieldDirection, values: In (0), Out (1), Ref (2) """
    In: FieldDirection = ...
    Out: FieldDirection = ...
    Ref: FieldDirection = ...
    value__ = ...


class MemberAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberAttributes, values: Abstract (1), AccessMask (61440), Assembly (4096), Const (5), Family (12288), FamilyAndAssembly (8192), FamilyOrAssembly (16384), Final (2), New (16), Overloaded (256), Override (4), Private (20480), Public (24576), ScopeMask (15), Static (3), VTableMask (240) """
    Abstract: MemberAttributes = ...
    AccessMask: MemberAttributes = ...
    Assembly: MemberAttributes = ...
    Const: MemberAttributes = ...
    Family: MemberAttributes = ...
    FamilyAndAssembly: MemberAttributes = ...
    FamilyOrAssembly: MemberAttributes = ...
    Final: MemberAttributes = ...
    New: MemberAttributes = ...
    Overloaded: MemberAttributes = ...
    Override: MemberAttributes = ...
    Private: MemberAttributes = ...
    Public: MemberAttributes = ...
    ScopeMask: MemberAttributes = ...
    Static: MemberAttributes = ...
    value__ = ...
    VTableMask: MemberAttributes = ...


# variables with complex values

