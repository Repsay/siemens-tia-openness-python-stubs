# encoding: utf-8
# module System.Management.Automation.Language calls itself Language
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import ScriptBlock

from System import Array, Enum, Tuple, Type, Version

from System.Collections import IDictionary, IEnumerable

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Management.Automation import (ParameterBindingException, 
    ParameterMetadata, VariablePath)

from typing import Tuple as Tuple_

"""The following names are not found in the module: (Func, IAssignableValue, 
    IParameterMetadataProvider, ISupportsAssignment, ISupportsTypeCaching, 
    field#)
"""

# no functions
# classes

class Ast: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Extent(self) -> IScriptExtent:
        """ Get: Extent(self: Ast) -> IScriptExtent """
        ...

    @property
    def Parent(self) -> Ast:
        """ Get: Parent(self: Ast) -> Ast """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: Ast) -> Ast """
        ...

    def Find(self, predicate, searchNestedScriptBlocks:bool) -> Ast: # Not found arg types: {'predicate': 'Func'}
        """ Find(self: Ast, predicate: Func[Ast, bool], searchNestedScriptBlocks: bool) -> Ast """
        ...

    def FindAll(self, predicate, searchNestedScriptBlocks:bool) -> IEnumerable: # Not found arg types: {'predicate': 'Func'}
        """ FindAll(self: Ast, predicate: Func[Ast, bool], searchNestedScriptBlocks: bool) -> IEnumerable[Ast] """
        ...

    def SafeGetValue(self) -> object:
        """ SafeGetValue(self: Ast) -> object """
        ...

    def ToString(self) -> str:
        """ ToString(self: Ast) -> str """
        ...

    def Visit(self, astVisitor:ICustomAstVisitor) -> object:
        """
        Visit(self: Ast, astVisitor: ICustomAstVisitor) -> object
        Visit(self: Ast, astVisitor: AstVisitor)
        """
        ...


class CommandElementAst(Ast): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ExpressionAst(CommandElementAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def StaticType(self) -> Type:
        """ Get: StaticType(self: ExpressionAst) -> Type """
        ...



class ArrayExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ ArrayExpressionAst(extent: IScriptExtent, statementBlock: StatementBlockAst) """
    @property
    def SubExpression(self) -> StatementBlockAst:
        """ Get: SubExpression(self: ArrayExpressionAst) -> StatementBlockAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ArrayExpressionAst) -> Ast """
        ...


class ArrayLiteralAst(ExpressionAst, ISupportsAssignment): # skipped bases: <type 'object'>
    """ ArrayLiteralAst(extent: IScriptExtent, elements: IList[ExpressionAst]) """
    @property
    def Elements(self) -> ReadOnlyCollection:
        """ Get: Elements(self: ArrayLiteralAst) -> ReadOnlyCollection[ExpressionAst] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ArrayLiteralAst) -> Ast """
        ...


class ITypeName: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: ITypeName) -> str """
        ...

    @property
    def Extent(self) -> IScriptExtent:
        """ Get: Extent(self: ITypeName) -> IScriptExtent """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: ITypeName) -> str """
        ...

    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: ITypeName) -> bool """
        ...

    @property
    def IsGeneric(self) -> bool:
        """ Get: IsGeneric(self: ITypeName) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ITypeName) -> str """
        ...


    def GetReflectionAttributeType(self) -> Type:
        """ GetReflectionAttributeType(self: ITypeName) -> Type """
        ...

    def GetReflectionType(self) -> Type:
        """ GetReflectionType(self: ITypeName) -> Type """
        ...


class ArrayTypeName(ITypeName, ISupportsTypeCaching): # skipped bases: <type 'object'>
    """ ArrayTypeName(extent: IScriptExtent, elementType: ITypeName, rank: int) """
    @property
    def ElementType(self) -> ITypeName:
        """ Get: ElementType(self: ArrayTypeName) -> ITypeName """
        ...

    @property
    def Rank(self) -> int:
        """ Get: Rank(self: ArrayTypeName) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ArrayTypeName, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ArrayTypeName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ArrayTypeName) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class StatementAst(Ast): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PipelineBaseAst(StatementAst): # skipped bases: <type 'object'>
    """ no doc """
    def GetPureExpression(self) -> ExpressionAst:
        """ GetPureExpression(self: PipelineBaseAst) -> ExpressionAst """
        ...


class AssignmentStatementAst(PipelineBaseAst): # skipped bases: <type 'object'>
    """ AssignmentStatementAst(extent: IScriptExtent, left: ExpressionAst, operator: TokenKind, right: StatementAst, errorPosition: IScriptExtent) """
    @property
    def ErrorPosition(self) -> IScriptExtent:
        """ Get: ErrorPosition(self: AssignmentStatementAst) -> IScriptExtent """
        ...

    @property
    def Left(self) -> ExpressionAst:
        """ Get: Left(self: AssignmentStatementAst) -> ExpressionAst """
        ...

    @property
    def Operator(self) -> TokenKind:
        """ Get: Operator(self: AssignmentStatementAst) -> TokenKind """
        ...

    @property
    def Right(self) -> StatementAst:
        """ Get: Right(self: AssignmentStatementAst) -> StatementAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: AssignmentStatementAst) -> Ast """
        ...

    def GetAssignmentTargets(self) -> IEnumerable:
        """ GetAssignmentTargets(self: AssignmentStatementAst) -> IEnumerable[ExpressionAst] """
        ...


class AstVisitAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AstVisitAction, values: Continue (0), SkipChildren (1), StopVisit (2) """
    Continue: AstVisitAction = ...
    SkipChildren: AstVisitAction = ...
    StopVisit: AstVisitAction = ...
    value__ = ...


class AstVisitor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def VisitArrayExpression(self, arrayExpressionAst:ArrayExpressionAst) -> AstVisitAction:
        """ VisitArrayExpression(self: AstVisitor, arrayExpressionAst: ArrayExpressionAst) -> AstVisitAction """
        ...

    def VisitArrayLiteral(self, arrayLiteralAst:ArrayLiteralAst) -> AstVisitAction:
        """ VisitArrayLiteral(self: AstVisitor, arrayLiteralAst: ArrayLiteralAst) -> AstVisitAction """
        ...

    def VisitAssignmentStatement(self, assignmentStatementAst:AssignmentStatementAst) -> AstVisitAction:
        """ VisitAssignmentStatement(self: AstVisitor, assignmentStatementAst: AssignmentStatementAst) -> AstVisitAction """
        ...

    def VisitAttribute(self, attributeAst:AttributeAst) -> AstVisitAction:
        """ VisitAttribute(self: AstVisitor, attributeAst: AttributeAst) -> AstVisitAction """
        ...

    def VisitAttributedExpression(self, attributedExpressionAst:AttributedExpressionAst) -> AstVisitAction:
        """ VisitAttributedExpression(self: AstVisitor, attributedExpressionAst: AttributedExpressionAst) -> AstVisitAction """
        ...

    def VisitBinaryExpression(self, binaryExpressionAst:BinaryExpressionAst) -> AstVisitAction:
        """ VisitBinaryExpression(self: AstVisitor, binaryExpressionAst: BinaryExpressionAst) -> AstVisitAction """
        ...

    def VisitBlockStatement(self, blockStatementAst:BlockStatementAst) -> AstVisitAction:
        """ VisitBlockStatement(self: AstVisitor, blockStatementAst: BlockStatementAst) -> AstVisitAction """
        ...

    def VisitBreakStatement(self, breakStatementAst:BreakStatementAst) -> AstVisitAction:
        """ VisitBreakStatement(self: AstVisitor, breakStatementAst: BreakStatementAst) -> AstVisitAction """
        ...

    def VisitCatchClause(self, catchClauseAst:CatchClauseAst) -> AstVisitAction:
        """ VisitCatchClause(self: AstVisitor, catchClauseAst: CatchClauseAst) -> AstVisitAction """
        ...

    def VisitCommand(self, commandAst:CommandAst) -> AstVisitAction:
        """ VisitCommand(self: AstVisitor, commandAst: CommandAst) -> AstVisitAction """
        ...

    def VisitCommandExpression(self, commandExpressionAst:CommandExpressionAst) -> AstVisitAction:
        """ VisitCommandExpression(self: AstVisitor, commandExpressionAst: CommandExpressionAst) -> AstVisitAction """
        ...

    def VisitCommandParameter(self, commandParameterAst:CommandParameterAst) -> AstVisitAction:
        """ VisitCommandParameter(self: AstVisitor, commandParameterAst: CommandParameterAst) -> AstVisitAction """
        ...

    def VisitConstantExpression(self, constantExpressionAst:ConstantExpressionAst) -> AstVisitAction:
        """ VisitConstantExpression(self: AstVisitor, constantExpressionAst: ConstantExpressionAst) -> AstVisitAction """
        ...

    def VisitContinueStatement(self, continueStatementAst:ContinueStatementAst) -> AstVisitAction:
        """ VisitContinueStatement(self: AstVisitor, continueStatementAst: ContinueStatementAst) -> AstVisitAction """
        ...

    def VisitConvertExpression(self, convertExpressionAst:ConvertExpressionAst) -> AstVisitAction:
        """ VisitConvertExpression(self: AstVisitor, convertExpressionAst: ConvertExpressionAst) -> AstVisitAction """
        ...

    def VisitDataStatement(self, dataStatementAst:DataStatementAst) -> AstVisitAction:
        """ VisitDataStatement(self: AstVisitor, dataStatementAst: DataStatementAst) -> AstVisitAction """
        ...

    def VisitDoUntilStatement(self, doUntilStatementAst:DoUntilStatementAst) -> AstVisitAction:
        """ VisitDoUntilStatement(self: AstVisitor, doUntilStatementAst: DoUntilStatementAst) -> AstVisitAction """
        ...

    def VisitDoWhileStatement(self, doWhileStatementAst:DoWhileStatementAst) -> AstVisitAction:
        """ VisitDoWhileStatement(self: AstVisitor, doWhileStatementAst: DoWhileStatementAst) -> AstVisitAction """
        ...

    def VisitErrorExpression(self, errorExpressionAst:ErrorExpressionAst) -> AstVisitAction:
        """ VisitErrorExpression(self: AstVisitor, errorExpressionAst: ErrorExpressionAst) -> AstVisitAction """
        ...

    def VisitErrorStatement(self, errorStatementAst:ErrorStatementAst) -> AstVisitAction:
        """ VisitErrorStatement(self: AstVisitor, errorStatementAst: ErrorStatementAst) -> AstVisitAction """
        ...

    def VisitExitStatement(self, exitStatementAst:ExitStatementAst) -> AstVisitAction:
        """ VisitExitStatement(self: AstVisitor, exitStatementAst: ExitStatementAst) -> AstVisitAction """
        ...

    def VisitExpandableStringExpression(self, expandableStringExpressionAst:ExpandableStringExpressionAst) -> AstVisitAction:
        """ VisitExpandableStringExpression(self: AstVisitor, expandableStringExpressionAst: ExpandableStringExpressionAst) -> AstVisitAction """
        ...

    def VisitFileRedirection(self, redirectionAst:FileRedirectionAst) -> AstVisitAction:
        """ VisitFileRedirection(self: AstVisitor, redirectionAst: FileRedirectionAst) -> AstVisitAction """
        ...

    def VisitForEachStatement(self, forEachStatementAst:ForEachStatementAst) -> AstVisitAction:
        """ VisitForEachStatement(self: AstVisitor, forEachStatementAst: ForEachStatementAst) -> AstVisitAction """
        ...

    def VisitForStatement(self, forStatementAst:ForStatementAst) -> AstVisitAction:
        """ VisitForStatement(self: AstVisitor, forStatementAst: ForStatementAst) -> AstVisitAction """
        ...

    def VisitFunctionDefinition(self, functionDefinitionAst:FunctionDefinitionAst) -> AstVisitAction:
        """ VisitFunctionDefinition(self: AstVisitor, functionDefinitionAst: FunctionDefinitionAst) -> AstVisitAction """
        ...

    def VisitHashtable(self, hashtableAst:HashtableAst) -> AstVisitAction:
        """ VisitHashtable(self: AstVisitor, hashtableAst: HashtableAst) -> AstVisitAction """
        ...

    def VisitIfStatement(self, ifStmtAst:IfStatementAst) -> AstVisitAction:
        """ VisitIfStatement(self: AstVisitor, ifStmtAst: IfStatementAst) -> AstVisitAction """
        ...

    def VisitIndexExpression(self, indexExpressionAst:IndexExpressionAst) -> AstVisitAction:
        """ VisitIndexExpression(self: AstVisitor, indexExpressionAst: IndexExpressionAst) -> AstVisitAction """
        ...

    def VisitInvokeMemberExpression(self, methodCallAst:InvokeMemberExpressionAst) -> AstVisitAction:
        """ VisitInvokeMemberExpression(self: AstVisitor, methodCallAst: InvokeMemberExpressionAst) -> AstVisitAction """
        ...

    def VisitMemberExpression(self, memberExpressionAst:MemberExpressionAst) -> AstVisitAction:
        """ VisitMemberExpression(self: AstVisitor, memberExpressionAst: MemberExpressionAst) -> AstVisitAction """
        ...

    def VisitMergingRedirection(self, redirectionAst:MergingRedirectionAst) -> AstVisitAction:
        """ VisitMergingRedirection(self: AstVisitor, redirectionAst: MergingRedirectionAst) -> AstVisitAction """
        ...

    def VisitNamedAttributeArgument(self, namedAttributeArgumentAst:NamedAttributeArgumentAst) -> AstVisitAction:
        """ VisitNamedAttributeArgument(self: AstVisitor, namedAttributeArgumentAst: NamedAttributeArgumentAst) -> AstVisitAction """
        ...

    def VisitNamedBlock(self, namedBlockAst:NamedBlockAst) -> AstVisitAction:
        """ VisitNamedBlock(self: AstVisitor, namedBlockAst: NamedBlockAst) -> AstVisitAction """
        ...

    def VisitParamBlock(self, paramBlockAst:ParamBlockAst) -> AstVisitAction:
        """ VisitParamBlock(self: AstVisitor, paramBlockAst: ParamBlockAst) -> AstVisitAction """
        ...

    def VisitParameter(self, parameterAst:ParameterAst) -> AstVisitAction:
        """ VisitParameter(self: AstVisitor, parameterAst: ParameterAst) -> AstVisitAction """
        ...

    def VisitParenExpression(self, parenExpressionAst:ParenExpressionAst) -> AstVisitAction:
        """ VisitParenExpression(self: AstVisitor, parenExpressionAst: ParenExpressionAst) -> AstVisitAction """
        ...

    def VisitPipeline(self, pipelineAst:PipelineAst) -> AstVisitAction:
        """ VisitPipeline(self: AstVisitor, pipelineAst: PipelineAst) -> AstVisitAction """
        ...

    def VisitReturnStatement(self, returnStatementAst:ReturnStatementAst) -> AstVisitAction:
        """ VisitReturnStatement(self: AstVisitor, returnStatementAst: ReturnStatementAst) -> AstVisitAction """
        ...

    def VisitScriptBlock(self, scriptBlockAst:ScriptBlockAst) -> AstVisitAction:
        """ VisitScriptBlock(self: AstVisitor, scriptBlockAst: ScriptBlockAst) -> AstVisitAction """
        ...

    def VisitScriptBlockExpression(self, scriptBlockExpressionAst:ScriptBlockExpressionAst) -> AstVisitAction:
        """ VisitScriptBlockExpression(self: AstVisitor, scriptBlockExpressionAst: ScriptBlockExpressionAst) -> AstVisitAction """
        ...

    def VisitStatementBlock(self, statementBlockAst:StatementBlockAst) -> AstVisitAction:
        """ VisitStatementBlock(self: AstVisitor, statementBlockAst: StatementBlockAst) -> AstVisitAction """
        ...

    def VisitStringConstantExpression(self, stringConstantExpressionAst:StringConstantExpressionAst) -> AstVisitAction:
        """ VisitStringConstantExpression(self: AstVisitor, stringConstantExpressionAst: StringConstantExpressionAst) -> AstVisitAction """
        ...

    def VisitSubExpression(self, subExpressionAst:SubExpressionAst) -> AstVisitAction:
        """ VisitSubExpression(self: AstVisitor, subExpressionAst: SubExpressionAst) -> AstVisitAction """
        ...

    def VisitSwitchStatement(self, switchStatementAst:SwitchStatementAst) -> AstVisitAction:
        """ VisitSwitchStatement(self: AstVisitor, switchStatementAst: SwitchStatementAst) -> AstVisitAction """
        ...

    def VisitThrowStatement(self, throwStatementAst:ThrowStatementAst) -> AstVisitAction:
        """ VisitThrowStatement(self: AstVisitor, throwStatementAst: ThrowStatementAst) -> AstVisitAction """
        ...

    def VisitTrap(self, trapStatementAst:TrapStatementAst) -> AstVisitAction:
        """ VisitTrap(self: AstVisitor, trapStatementAst: TrapStatementAst) -> AstVisitAction """
        ...

    def VisitTryStatement(self, tryStatementAst:TryStatementAst) -> AstVisitAction:
        """ VisitTryStatement(self: AstVisitor, tryStatementAst: TryStatementAst) -> AstVisitAction """
        ...

    def VisitTypeConstraint(self, typeConstraintAst:TypeConstraintAst) -> AstVisitAction:
        """ VisitTypeConstraint(self: AstVisitor, typeConstraintAst: TypeConstraintAst) -> AstVisitAction """
        ...

    def VisitTypeExpression(self, typeExpressionAst:TypeExpressionAst) -> AstVisitAction:
        """ VisitTypeExpression(self: AstVisitor, typeExpressionAst: TypeExpressionAst) -> AstVisitAction """
        ...

    def VisitUnaryExpression(self, unaryExpressionAst:UnaryExpressionAst) -> AstVisitAction:
        """ VisitUnaryExpression(self: AstVisitor, unaryExpressionAst: UnaryExpressionAst) -> AstVisitAction """
        ...

    def VisitUsingExpression(self, usingExpressionAst:UsingExpressionAst) -> AstVisitAction:
        """ VisitUsingExpression(self: AstVisitor, usingExpressionAst: UsingExpressionAst) -> AstVisitAction """
        ...

    def VisitVariableExpression(self, variableExpressionAst:VariableExpressionAst) -> AstVisitAction:
        """ VisitVariableExpression(self: AstVisitor, variableExpressionAst: VariableExpressionAst) -> AstVisitAction """
        ...

    def VisitWhileStatement(self, whileStatementAst:WhileStatementAst) -> AstVisitAction:
        """ VisitWhileStatement(self: AstVisitor, whileStatementAst: WhileStatementAst) -> AstVisitAction """
        ...


class AstVisitor2(AstVisitor): # skipped bases: <type 'object'>
    """ no doc """
    def VisitBaseCtorInvokeMemberExpression(self, baseCtorInvokeMemberExpressionAst:BaseCtorInvokeMemberExpressionAst) -> AstVisitAction:
        """ VisitBaseCtorInvokeMemberExpression(self: AstVisitor2, baseCtorInvokeMemberExpressionAst: BaseCtorInvokeMemberExpressionAst) -> AstVisitAction """
        ...

    def VisitConfigurationDefinition(self, configurationDefinitionAst:ConfigurationDefinitionAst) -> AstVisitAction:
        """ VisitConfigurationDefinition(self: AstVisitor2, configurationDefinitionAst: ConfigurationDefinitionAst) -> AstVisitAction """
        ...

    def VisitDynamicKeywordStatement(self, dynamicKeywordStatementAst:DynamicKeywordStatementAst) -> AstVisitAction:
        """ VisitDynamicKeywordStatement(self: AstVisitor2, dynamicKeywordStatementAst: DynamicKeywordStatementAst) -> AstVisitAction """
        ...

    def VisitFunctionMember(self, functionMemberAst:FunctionMemberAst) -> AstVisitAction:
        """ VisitFunctionMember(self: AstVisitor2, functionMemberAst: FunctionMemberAst) -> AstVisitAction """
        ...

    def VisitPropertyMember(self, propertyMemberAst:PropertyMemberAst) -> AstVisitAction:
        """ VisitPropertyMember(self: AstVisitor2, propertyMemberAst: PropertyMemberAst) -> AstVisitAction """
        ...

    def VisitTypeDefinition(self, typeDefinitionAst:TypeDefinitionAst) -> AstVisitAction:
        """ VisitTypeDefinition(self: AstVisitor2, typeDefinitionAst: TypeDefinitionAst) -> AstVisitAction """
        ...

    def VisitUsingStatement(self, usingStatementAst:UsingStatementAst) -> AstVisitAction:
        """ VisitUsingStatement(self: AstVisitor2, usingStatementAst: UsingStatementAst) -> AstVisitAction """
        ...


class AttributeBaseAst(Ast): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TypeName(self) -> ITypeName:
        """ Get: TypeName(self: AttributeBaseAst) -> ITypeName """
        ...



class AttributeAst(AttributeBaseAst): # skipped bases: <type 'object'>
    """ AttributeAst(extent: IScriptExtent, typeName: ITypeName, positionalArguments: IEnumerable[ExpressionAst], namedArguments: IEnumerable[NamedAttributeArgumentAst]) """
    @property
    def NamedArguments(self) -> ReadOnlyCollection:
        """ Get: NamedArguments(self: AttributeAst) -> ReadOnlyCollection[NamedAttributeArgumentAst] """
        ...

    @property
    def PositionalArguments(self) -> ReadOnlyCollection:
        """ Get: PositionalArguments(self: AttributeAst) -> ReadOnlyCollection[ExpressionAst] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: AttributeAst) -> Ast """
        ...


class AttributedExpressionAst(ExpressionAst, ISupportsAssignment, IAssignableValue): # skipped bases: <type 'object'>
    """ AttributedExpressionAst(extent: IScriptExtent, attribute: AttributeBaseAst, child: ExpressionAst) """
    @property
    def Attribute(self) -> AttributeBaseAst:
        """ Get: Attribute(self: AttributedExpressionAst) -> AttributeBaseAst """
        ...

    @property
    def Child(self) -> ExpressionAst:
        """ Get: Child(self: AttributedExpressionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: AttributedExpressionAst) -> Ast """
        ...


class MemberExpressionAst(ExpressionAst, ISupportsAssignment): # skipped bases: <type 'object'>
    """ MemberExpressionAst(extent: IScriptExtent, expression: ExpressionAst, member: CommandElementAst, static: bool) """
    @property
    def Expression(self) -> ExpressionAst:
        """ Get: Expression(self: MemberExpressionAst) -> ExpressionAst """
        ...

    @property
    def Member(self) -> CommandElementAst:
        """ Get: Member(self: MemberExpressionAst) -> CommandElementAst """
        ...

    @property
    def Static(self) -> bool:
        """ Get: Static(self: MemberExpressionAst) -> bool """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: MemberExpressionAst) -> Ast """
        ...


class InvokeMemberExpressionAst(MemberExpressionAst): # skipped bases: <type 'ISupportsAssignment'>, <type 'object'>
    """ InvokeMemberExpressionAst(extent: IScriptExtent, expression: ExpressionAst, method: CommandElementAst, arguments: IEnumerable[ExpressionAst], static: bool) """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: InvokeMemberExpressionAst) -> ReadOnlyCollection[ExpressionAst] """
        ...



class BaseCtorInvokeMemberExpressionAst(InvokeMemberExpressionAst): # skipped bases: <type 'ISupportsAssignment'>, <type 'object'>
    """ BaseCtorInvokeMemberExpressionAst(baseKeywordExtent: IScriptExtent, baseCallExtent: IScriptExtent, arguments: IEnumerable[ExpressionAst]) """
    pass

class BinaryExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ BinaryExpressionAst(extent: IScriptExtent, left: ExpressionAst, operator: TokenKind, right: ExpressionAst, errorPosition: IScriptExtent) """
    @property
    def ErrorPosition(self) -> IScriptExtent:
        """ Get: ErrorPosition(self: BinaryExpressionAst) -> IScriptExtent """
        ...

    @property
    def Left(self) -> ExpressionAst:
        """ Get: Left(self: BinaryExpressionAst) -> ExpressionAst """
        ...

    @property
    def Operator(self) -> TokenKind:
        """ Get: Operator(self: BinaryExpressionAst) -> TokenKind """
        ...

    @property
    def Right(self) -> ExpressionAst:
        """ Get: Right(self: BinaryExpressionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: BinaryExpressionAst) -> Ast """
        ...


class BlockStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ BlockStatementAst(extent: IScriptExtent, kind: Token, body: StatementBlockAst) """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: BlockStatementAst) -> StatementBlockAst """
        ...

    @property
    def Kind(self) -> Token:
        """ Get: Kind(self: BlockStatementAst) -> Token """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: BlockStatementAst) -> Ast """
        ...


class BreakStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ BreakStatementAst(extent: IScriptExtent, label: ExpressionAst) """
    @property
    def Label(self) -> ExpressionAst:
        """ Get: Label(self: BreakStatementAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: BreakStatementAst) -> Ast """
        ...


class CatchClauseAst(Ast): # skipped bases: <type 'object'>
    """ CatchClauseAst(extent: IScriptExtent, catchTypes: IEnumerable[TypeConstraintAst], body: StatementBlockAst) """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: CatchClauseAst) -> StatementBlockAst """
        ...

    @property
    def CatchTypes(self) -> ReadOnlyCollection:
        """ Get: CatchTypes(self: CatchClauseAst) -> ReadOnlyCollection[TypeConstraintAst] """
        ...

    @property
    def IsCatchAll(self) -> bool:
        """ Get: IsCatchAll(self: CatchClauseAst) -> bool """
        ...



class CodeGeneration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EscapeBlockCommentContent(value:str) -> str:
        """ EscapeBlockCommentContent(value: str) -> str """
        ...

    @staticmethod
    def EscapeFormatStringContent(value:str) -> str:
        """ EscapeFormatStringContent(value: str) -> str """
        ...

    @staticmethod
    def EscapeSingleQuotedStringContent(value:str) -> str:
        """ EscapeSingleQuotedStringContent(value: str) -> str """
        ...

    @staticmethod
    def EscapeVariableName(value:str) -> str:
        """ EscapeVariableName(value: str) -> str """
        ...

    __all__: list = ...


class CommandBaseAst(StatementAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Redirections(self) -> ReadOnlyCollection:
        """ Get: Redirections(self: CommandBaseAst) -> ReadOnlyCollection[RedirectionAst] """
        ...



class CommandAst(CommandBaseAst): # skipped bases: <type 'object'>
    """ CommandAst(extent: IScriptExtent, commandElements: IEnumerable[CommandElementAst], invocationOperator: TokenKind, redirections: IEnumerable[RedirectionAst]) """
    @property
    def CommandElements(self) -> ReadOnlyCollection:
        """ Get: CommandElements(self: CommandAst) -> ReadOnlyCollection[CommandElementAst] """
        ...

    @property
    def DefiningKeyword(self) -> DynamicKeyword:
        """
        Get: DefiningKeyword(self: CommandAst) -> DynamicKeyword
        Set: DefiningKeyword(self: CommandAst) = value
        """
        ...

    @property
    def InvocationOperator(self) -> TokenKind:
        """ Get: InvocationOperator(self: CommandAst) -> TokenKind """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: CommandAst) -> Ast """
        ...

    def GetCommandName(self) -> str:
        """ GetCommandName(self: CommandAst) -> str """
        ...


class CommandExpressionAst(CommandBaseAst): # skipped bases: <type 'object'>
    """ CommandExpressionAst(extent: IScriptExtent, expression: ExpressionAst, redirections: IEnumerable[RedirectionAst]) """
    @property
    def Expression(self) -> ExpressionAst:
        """ Get: Expression(self: CommandExpressionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: CommandExpressionAst) -> Ast """
        ...


class CommandParameterAst(CommandElementAst): # skipped bases: <type 'object'>
    """ CommandParameterAst(extent: IScriptExtent, parameterName: str, argument: ExpressionAst, errorPosition: IScriptExtent) """
    @property
    def Argument(self) -> ExpressionAst:
        """ Get: Argument(self: CommandParameterAst) -> ExpressionAst """
        ...

    @property
    def ErrorPosition(self) -> IScriptExtent:
        """ Get: ErrorPosition(self: CommandParameterAst) -> IScriptExtent """
        ...

    @property
    def ParameterName(self) -> str:
        """ Get: ParameterName(self: CommandParameterAst) -> str """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: CommandParameterAst) -> Ast """
        ...


class CommentHelpInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ CommentHelpInfo() """
    @property
    def Component(self) -> str:
        """ Get: Component(self: CommentHelpInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: CommentHelpInfo) -> str """
        ...

    @property
    def Examples(self) -> ReadOnlyCollection:
        """ Get: Examples(self: CommentHelpInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def ForwardHelpCategory(self) -> str:
        """ Get: ForwardHelpCategory(self: CommentHelpInfo) -> str """
        ...

    @property
    def ForwardHelpTargetName(self) -> str:
        """ Get: ForwardHelpTargetName(self: CommentHelpInfo) -> str """
        ...

    @property
    def Functionality(self) -> str:
        """ Get: Functionality(self: CommentHelpInfo) -> str """
        ...

    @property
    def Inputs(self) -> ReadOnlyCollection:
        """ Get: Inputs(self: CommentHelpInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def Links(self) -> ReadOnlyCollection:
        """ Get: Links(self: CommentHelpInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def MamlHelpFile(self) -> str:
        """ Get: MamlHelpFile(self: CommentHelpInfo) -> str """
        ...

    @property
    def Notes(self) -> str:
        """ Get: Notes(self: CommentHelpInfo) -> str """
        ...

    @property
    def Outputs(self) -> ReadOnlyCollection:
        """ Get: Outputs(self: CommentHelpInfo) -> ReadOnlyCollection[str] """
        ...

    @property
    def Parameters(self) -> IDictionary:
        """ Get: Parameters(self: CommentHelpInfo) -> IDictionary[str, str] """
        ...

    @property
    def RemoteHelpRunspace(self) -> str:
        """ Get: RemoteHelpRunspace(self: CommentHelpInfo) -> str """
        ...

    @property
    def Role(self) -> str:
        """ Get: Role(self: CommentHelpInfo) -> str """
        ...

    @property
    def Synopsis(self) -> str:
        """ Get: Synopsis(self: CommentHelpInfo) -> str """
        ...


    def GetCommentBlock(self) -> str:
        """ GetCommentBlock(self: CommentHelpInfo) -> str """
        ...


class ConfigurationDefinitionAst(StatementAst): # skipped bases: <type 'object'>
    """ ConfigurationDefinitionAst(extent: IScriptExtent, body: ScriptBlockExpressionAst, type: ConfigurationType, instanceName: ExpressionAst) """
    @property
    def Body(self) -> ScriptBlockExpressionAst:
        """ Get: Body(self: ConfigurationDefinitionAst) -> ScriptBlockExpressionAst """
        ...

    @property
    def ConfigurationType(self) -> ConfigurationType:
        """ Get: ConfigurationType(self: ConfigurationDefinitionAst) -> ConfigurationType """
        ...

    @property
    def InstanceName(self) -> ExpressionAst:
        """ Get: InstanceName(self: ConfigurationDefinitionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ConfigurationDefinitionAst) -> Ast """
        ...


class ConfigurationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationType, values: Meta (1), Resource (0) """
    Meta: ConfigurationType = ...
    Resource: ConfigurationType = ...
    value__ = ...


class ConstantExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ ConstantExpressionAst(extent: IScriptExtent, value: object) """
    @property
    def Value(self) -> object:
        """ Get: Value(self: ConstantExpressionAst) -> object """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ConstantExpressionAst) -> Ast """
        ...


class ContinueStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ ContinueStatementAst(extent: IScriptExtent, label: ExpressionAst) """
    @property
    def Label(self) -> ExpressionAst:
        """ Get: Label(self: ContinueStatementAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ContinueStatementAst) -> Ast """
        ...


class ConvertExpressionAst(AttributedExpressionAst): # skipped bases: <type 'IAssignableValue'>, <type 'ISupportsAssignment'>, <type 'object'>
    """ ConvertExpressionAst(extent: IScriptExtent, typeConstraint: TypeConstraintAst, child: ExpressionAst) """
    @property
    def StaticType(self) -> Type:
        """ Get: StaticType(self: ConvertExpressionAst) -> Type """
        ...

    @property
    def Type(self) -> TypeConstraintAst:
        """ Get: Type(self: ConvertExpressionAst) -> TypeConstraintAst """
        ...



class DataStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ DataStatementAst(extent: IScriptExtent, variableName: str, commandsAllowed: IEnumerable[ExpressionAst], body: StatementBlockAst) """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: DataStatementAst) -> StatementBlockAst """
        ...

    @property
    def CommandsAllowed(self) -> ReadOnlyCollection:
        """ Get: CommandsAllowed(self: DataStatementAst) -> ReadOnlyCollection[ExpressionAst] """
        ...

    @property
    def Variable(self) -> str:
        """ Get: Variable(self: DataStatementAst) -> str """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: DataStatementAst) -> Ast """
        ...


class DefaultCustomAstVisitor(ICustomAstVisitor): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DefaultCustomAstVisitor2(DefaultCustomAstVisitor, ICustomAstVisitor2): # skipped bases: <type 'ICustomAstVisitor'>, <type 'object'>
    """ no doc """
    pass

class LabeledStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Condition(self) -> PipelineBaseAst:
        """ Get: Condition(self: LabeledStatementAst) -> PipelineBaseAst """
        ...

    @property
    def Label(self) -> str:
        """ Get: Label(self: LabeledStatementAst) -> str """
        ...



class LoopStatementAst(LabeledStatementAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: LoopStatementAst) -> StatementBlockAst """
        ...



class DoUntilStatementAst(LoopStatementAst): # skipped bases: <type 'object'>
    """ DoUntilStatementAst(extent: IScriptExtent, label: str, condition: PipelineBaseAst, body: StatementBlockAst) """
    def Copy(self) -> Ast:
        """ Copy(self: DoUntilStatementAst) -> Ast """
        ...


class DoWhileStatementAst(LoopStatementAst): # skipped bases: <type 'object'>
    """ DoWhileStatementAst(extent: IScriptExtent, label: str, condition: PipelineBaseAst, body: StatementBlockAst) """
    def Copy(self) -> Ast:
        """ Copy(self: DoWhileStatementAst) -> Ast """
        ...


class DynamicKeyword: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicKeyword() """
    @property
    def BodyMode(self) -> DynamicKeywordBodyMode:
        """
        Get: BodyMode(self: DynamicKeyword) -> DynamicKeywordBodyMode
        Set: BodyMode(self: DynamicKeyword) = value
        """
        ...

    @property
    def DirectCall(self) -> bool:
        """
        Get: DirectCall(self: DynamicKeyword) -> bool
        Set: DirectCall(self: DynamicKeyword) = value
        """
        ...

    @property
    def HasReservedProperties(self) -> bool:
        """
        Get: HasReservedProperties(self: DynamicKeyword) -> bool
        Set: HasReservedProperties(self: DynamicKeyword) = value
        """
        ...

    @property
    def ImplementingModule(self) -> str:
        """
        Get: ImplementingModule(self: DynamicKeyword) -> str
        Set: ImplementingModule(self: DynamicKeyword) = value
        """
        ...

    @property
    def ImplementingModuleVersion(self) -> Version:
        """
        Get: ImplementingModuleVersion(self: DynamicKeyword) -> Version
        Set: ImplementingModuleVersion(self: DynamicKeyword) = value
        """
        ...

    @property
    def IsReservedKeyword(self) -> bool:
        """
        Get: IsReservedKeyword(self: DynamicKeyword) -> bool
        Set: IsReservedKeyword(self: DynamicKeyword) = value
        """
        ...

    @property
    def Keyword(self) -> str:
        """
        Get: Keyword(self: DynamicKeyword) -> str
        Set: Keyword(self: DynamicKeyword) = value
        """
        ...

    @property
    def MetaStatement(self) -> bool:
        """
        Get: MetaStatement(self: DynamicKeyword) -> bool
        Set: MetaStatement(self: DynamicKeyword) = value
        """
        ...

    @property
    def NameMode(self) -> DynamicKeywordNameMode:
        """
        Get: NameMode(self: DynamicKeyword) -> DynamicKeywordNameMode
        Set: NameMode(self: DynamicKeyword) = value
        """
        ...

    @property
    def Parameters(self) -> Dictionary:
        """ Get: Parameters(self: DynamicKeyword) -> Dictionary[str, DynamicKeywordParameter] """
        ...

    @property
    def PostParse(self): # -> Func
        """
        Get: PostParse(self: DynamicKeyword) -> Func[DynamicKeywordStatementAst, Array[ParseError]]
        Set: PostParse(self: DynamicKeyword) = value
        """
        ...

    @property
    def PreParse(self): # -> Func
        """
        Get: PreParse(self: DynamicKeyword) -> Func[DynamicKeyword, Array[ParseError]]
        Set: PreParse(self: DynamicKeyword) = value
        """
        ...

    @property
    def Properties(self) -> Dictionary:
        """ Get: Properties(self: DynamicKeyword) -> Dictionary[str, DynamicKeywordProperty] """
        ...

    @property
    def ResourceName(self) -> str:
        """
        Get: ResourceName(self: DynamicKeyword) -> str
        Set: ResourceName(self: DynamicKeyword) = value
        """
        ...

    @property
    def SemanticCheck(self): # -> Func
        """
        Get: SemanticCheck(self: DynamicKeyword) -> Func[DynamicKeywordStatementAst, Array[ParseError]]
        Set: SemanticCheck(self: DynamicKeyword) = value
        """
        ...


    @staticmethod
    def AddKeyword(keywordToAdd:DynamicKeyword): # -> 
        """ AddKeyword(keywordToAdd: DynamicKeyword) """
        ...

    @staticmethod
    def ContainsKeyword(name:str) -> bool:
        """ ContainsKeyword(name: str) -> bool """
        ...

    def Copy(self) -> DynamicKeyword:
        """ Copy(self: DynamicKeyword) -> DynamicKeyword """
        ...

    @staticmethod
    def GetKeyword(name:str = ...) -> DynamicKeyword:
        """
        GetKeyword(name: str) -> DynamicKeyword
        GetKeyword() -> List[DynamicKeyword]
        """
        ...

    @staticmethod
    def Pop(): # -> 
        """ Pop() """
        ...

    @staticmethod
    def Push(): # -> 
        """ Push() """
        ...

    @staticmethod
    def RemoveKeyword(name:str): # -> 
        """ RemoveKeyword(name: str) """
        ...

    @staticmethod
    def Reset(): # -> 
        """ Reset() """
        ...


class DynamicKeywordBodyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DynamicKeywordBodyMode, values: Command (0), Hashtable (2), ScriptBlock (1) """
    Command: DynamicKeywordBodyMode = ...
    Hashtable: DynamicKeywordBodyMode = ...
    ScriptBlock: DynamicKeywordBodyMode = ...
    value__ = ...


class DynamicKeywordNameMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DynamicKeywordNameMode, values: NameRequired (2), NoName (0), OptionalName (4), SimpleNameRequired (1), SimpleOptionalName (3) """
    NameRequired: DynamicKeywordNameMode = ...
    NoName: DynamicKeywordNameMode = ...
    OptionalName: DynamicKeywordNameMode = ...
    SimpleNameRequired: DynamicKeywordNameMode = ...
    SimpleOptionalName: DynamicKeywordNameMode = ...
    value__ = ...


class DynamicKeywordProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicKeywordProperty() """
    @property
    def Attributes(self) -> List:
        """ Get: Attributes(self: DynamicKeywordProperty) -> List[str] """
        ...

    @property
    def IsKey(self) -> bool:
        """
        Get: IsKey(self: DynamicKeywordProperty) -> bool
        Set: IsKey(self: DynamicKeywordProperty) = value
        """
        ...

    @property
    def Mandatory(self) -> bool:
        """
        Get: Mandatory(self: DynamicKeywordProperty) -> bool
        Set: Mandatory(self: DynamicKeywordProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DynamicKeywordProperty) -> str
        Set: Name(self: DynamicKeywordProperty) = value
        """
        ...

    @property
    def Range(self) -> Tuple:
        """
        Get: Range(self: DynamicKeywordProperty) -> Tuple[int, int]
        Set: Range(self: DynamicKeywordProperty) = value
        """
        ...

    @property
    def TypeConstraint(self) -> str:
        """
        Get: TypeConstraint(self: DynamicKeywordProperty) -> str
        Set: TypeConstraint(self: DynamicKeywordProperty) = value
        """
        ...

    @property
    def ValueMap(self) -> Dictionary:
        """ Get: ValueMap(self: DynamicKeywordProperty) -> Dictionary[str, str] """
        ...

    @property
    def Values(self) -> List:
        """ Get: Values(self: DynamicKeywordProperty) -> List[str] """
        ...



class DynamicKeywordParameter(DynamicKeywordProperty): # skipped bases: <type 'object'>
    """ DynamicKeywordParameter() """
    @property
    def Switch(self) -> bool:
        """
        Get: Switch(self: DynamicKeywordParameter) -> bool
        Set: Switch(self: DynamicKeywordParameter) = value
        """
        ...



class DynamicKeywordStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ DynamicKeywordStatementAst(extent: IScriptExtent, commandElements: IEnumerable[CommandElementAst]) """
    @property
    def CommandElements(self) -> ReadOnlyCollection:
        """ Get: CommandElements(self: DynamicKeywordStatementAst) -> ReadOnlyCollection[CommandElementAst] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: DynamicKeywordStatementAst) -> Ast """
        ...


class ErrorExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NestedAst(self) -> ReadOnlyCollection:
        """ Get: NestedAst(self: ErrorExpressionAst) -> ReadOnlyCollection[Ast] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ErrorExpressionAst) -> Ast """
        ...


class ErrorStatementAst(PipelineBaseAst): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bodies(self) -> ReadOnlyCollection:
        """ Get: Bodies(self: ErrorStatementAst) -> ReadOnlyCollection[Ast] """
        ...

    @property
    def Conditions(self) -> ReadOnlyCollection:
        """ Get: Conditions(self: ErrorStatementAst) -> ReadOnlyCollection[Ast] """
        ...

    @property
    def Flags(self) -> Dictionary:
        """ Get: Flags(self: ErrorStatementAst) -> Dictionary[str, Tuple[Token, Ast]] """
        ...

    @property
    def Kind(self) -> Token:
        """ Get: Kind(self: ErrorStatementAst) -> Token """
        ...

    @property
    def NestedAst(self) -> ReadOnlyCollection:
        """ Get: NestedAst(self: ErrorStatementAst) -> ReadOnlyCollection[Ast] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ErrorStatementAst) -> Ast """
        ...


class ExitStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ ExitStatementAst(extent: IScriptExtent, pipeline: PipelineBaseAst) """
    @property
    def Pipeline(self) -> PipelineBaseAst:
        """ Get: Pipeline(self: ExitStatementAst) -> PipelineBaseAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ExitStatementAst) -> Ast """
        ...


class ExpandableStringExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ ExpandableStringExpressionAst(extent: IScriptExtent, value: str, type: StringConstantType) """
    @property
    def NestedExpressions(self) -> ReadOnlyCollection:
        """ Get: NestedExpressions(self: ExpandableStringExpressionAst) -> ReadOnlyCollection[ExpressionAst] """
        ...

    @property
    def StringConstantType(self) -> StringConstantType:
        """ Get: StringConstantType(self: ExpandableStringExpressionAst) -> StringConstantType """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: ExpandableStringExpressionAst) -> str """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ExpandableStringExpressionAst) -> Ast """
        ...


class RedirectionAst(Ast): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FromStream(self) -> RedirectionStream:
        """ Get: FromStream(self: RedirectionAst) -> RedirectionStream """
        ...



class FileRedirectionAst(RedirectionAst): # skipped bases: <type 'object'>
    """ FileRedirectionAst(extent: IScriptExtent, stream: RedirectionStream, file: ExpressionAst, append: bool) """
    @property
    def Append(self) -> bool:
        """ Get: Append(self: FileRedirectionAst) -> bool """
        ...

    @property
    def Location(self) -> ExpressionAst:
        """ Get: Location(self: FileRedirectionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: FileRedirectionAst) -> Ast """
        ...


class Token: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Extent(self) -> IScriptExtent:
        """ Get: Extent(self: Token) -> IScriptExtent """
        ...

    @property
    def HasError(self) -> bool:
        """ Get: HasError(self: Token) -> bool """
        ...

    @property
    def Kind(self) -> TokenKind:
        """ Get: Kind(self: Token) -> TokenKind """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: Token) -> str """
        ...

    @property
    def TokenFlags(self) -> TokenFlags:
        """ Get: TokenFlags(self: Token) -> TokenFlags """
        ...


    def ToString(self) -> str:
        """ ToString(self: Token) -> str """
        ...


class RedirectionToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    pass

class FileRedirectionToken(RedirectionToken): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Append(self) -> bool:
        """ Get: Append(self: FileRedirectionToken) -> bool """
        ...

    @property
    def FromStream(self) -> RedirectionStream:
        """ Get: FromStream(self: FileRedirectionToken) -> RedirectionStream """
        ...



class ForEachFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ForEachFlags, values: None (0), Parallel (1) """
    Parallel: ForEachFlags = ...
    value__ = ...


class ForEachStatementAst(LoopStatementAst): # skipped bases: <type 'object'>
    """
    ForEachStatementAst(extent: IScriptExtent, label: str, flags: ForEachFlags, variable: VariableExpressionAst, expression: PipelineBaseAst, body: StatementBlockAst)
    ForEachStatementAst(extent: IScriptExtent, label: str, flags: ForEachFlags, throttleLimit: ExpressionAst, variable: VariableExpressionAst, expression: PipelineBaseAst, body: StatementBlockAst)
    """
    @property
    def Flags(self) -> ForEachFlags:
        """ Get: Flags(self: ForEachStatementAst) -> ForEachFlags """
        ...

    @property
    def ThrottleLimit(self) -> ExpressionAst:
        """ Get: ThrottleLimit(self: ForEachStatementAst) -> ExpressionAst """
        ...

    @property
    def Variable(self) -> VariableExpressionAst:
        """ Get: Variable(self: ForEachStatementAst) -> VariableExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ForEachStatementAst) -> Ast """
        ...


class ForStatementAst(LoopStatementAst): # skipped bases: <type 'object'>
    """ ForStatementAst(extent: IScriptExtent, label: str, initializer: PipelineBaseAst, condition: PipelineBaseAst, iterator: PipelineBaseAst, body: StatementBlockAst) """
    @property
    def Initializer(self) -> PipelineBaseAst:
        """ Get: Initializer(self: ForStatementAst) -> PipelineBaseAst """
        ...

    @property
    def Iterator(self) -> PipelineBaseAst:
        """ Get: Iterator(self: ForStatementAst) -> PipelineBaseAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ForStatementAst) -> Ast """
        ...


class FunctionDefinitionAst(IParameterMetadataProvider, StatementAst): # skipped bases: <type 'object'>
    """ FunctionDefinitionAst(extent: IScriptExtent, isFilter: bool, isWorkflow: bool, name: str, parameters: IEnumerable[ParameterAst], body: ScriptBlockAst) """
    @property
    def Body(self) -> ScriptBlockAst:
        """ Get: Body(self: FunctionDefinitionAst) -> ScriptBlockAst """
        ...

    @property
    def IsFilter(self) -> bool:
        """ Get: IsFilter(self: FunctionDefinitionAst) -> bool """
        ...

    @property
    def IsWorkflow(self) -> bool:
        """ Get: IsWorkflow(self: FunctionDefinitionAst) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FunctionDefinitionAst) -> str """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: FunctionDefinitionAst) -> ReadOnlyCollection[ParameterAst] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: FunctionDefinitionAst) -> Ast """
        ...

    def GetHelpContent(self, scriptBlockTokenCache:Dictionary = ...) -> CommentHelpInfo:
        """
        GetHelpContent(self: FunctionDefinitionAst, scriptBlockTokenCache: Dictionary[Ast, Array[Token]]) -> CommentHelpInfo
        GetHelpContent(self: FunctionDefinitionAst) -> CommentHelpInfo
        """
        ...


class MemberAst(Ast): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberAst) -> str """
        ...



class FunctionMemberAst(IParameterMetadataProvider, MemberAst): # skipped bases: <type 'object'>
    """ FunctionMemberAst(extent: IScriptExtent, functionDefinitionAst: FunctionDefinitionAst, returnType: TypeConstraintAst, attributes: IEnumerable[AttributeAst], methodAttributes: MethodAttributes) """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: FunctionMemberAst) -> ReadOnlyCollection[AttributeAst] """
        ...

    @property
    def Body(self) -> ScriptBlockAst:
        """ Get: Body(self: FunctionMemberAst) -> ScriptBlockAst """
        ...

    @property
    def IsConstructor(self) -> bool:
        """ Get: IsConstructor(self: FunctionMemberAst) -> bool """
        ...

    @property
    def IsHidden(self) -> bool:
        """ Get: IsHidden(self: FunctionMemberAst) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: FunctionMemberAst) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: FunctionMemberAst) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: FunctionMemberAst) -> bool """
        ...

    @property
    def MethodAttributes(self) -> MethodAttributes:
        """ Get: MethodAttributes(self: FunctionMemberAst) -> MethodAttributes """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: FunctionMemberAst) -> ReadOnlyCollection[ParameterAst] """
        ...

    @property
    def ReturnType(self) -> TypeConstraintAst:
        """ Get: ReturnType(self: FunctionMemberAst) -> TypeConstraintAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: FunctionMemberAst) -> Ast """
        ...


class GenericTypeName(ITypeName, ISupportsTypeCaching): # skipped bases: <type 'object'>
    """ GenericTypeName(extent: IScriptExtent, genericTypeName: ITypeName, genericArguments: IEnumerable[ITypeName]) """
    @property
    def GenericArguments(self) -> ReadOnlyCollection:
        """ Get: GenericArguments(self: GenericTypeName) -> ReadOnlyCollection[ITypeName] """
        ...

    @property
    def TypeName(self) -> ITypeName:
        """ Get: TypeName(self: GenericTypeName) -> ITypeName """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: GenericTypeName, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GenericTypeName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: GenericTypeName) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class HashtableAst(ExpressionAst): # skipped bases: <type 'object'>
    """ HashtableAst(extent: IScriptExtent, keyValuePairs: IEnumerable[Tuple[ExpressionAst, StatementAst]]) """
    @property
    def KeyValuePairs(self) -> ReadOnlyCollection:
        """ Get: KeyValuePairs(self: HashtableAst) -> ReadOnlyCollection[Tuple[ExpressionAst, StatementAst]] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: HashtableAst) -> Ast """
        ...


class IAstPostVisitHandler: # skipped bases: <type 'object'>
    """ no doc """
    def PostVisit(self, ast:Ast): # -> 
        """ PostVisit(self: IAstPostVisitHandler, ast: Ast) """
        ...


class ICustomAstVisitor: # skipped bases: <type 'object'>
    """ no doc """
    def VisitArrayExpression(self, arrayExpressionAst:ArrayExpressionAst) -> object:
        """ VisitArrayExpression(self: ICustomAstVisitor, arrayExpressionAst: ArrayExpressionAst) -> object """
        ...

    def VisitArrayLiteral(self, arrayLiteralAst:ArrayLiteralAst) -> object:
        """ VisitArrayLiteral(self: ICustomAstVisitor, arrayLiteralAst: ArrayLiteralAst) -> object """
        ...

    def VisitAssignmentStatement(self, assignmentStatementAst:AssignmentStatementAst) -> object:
        """ VisitAssignmentStatement(self: ICustomAstVisitor, assignmentStatementAst: AssignmentStatementAst) -> object """
        ...

    def VisitAttribute(self, attributeAst:AttributeAst) -> object:
        """ VisitAttribute(self: ICustomAstVisitor, attributeAst: AttributeAst) -> object """
        ...

    def VisitAttributedExpression(self, attributedExpressionAst:AttributedExpressionAst) -> object:
        """ VisitAttributedExpression(self: ICustomAstVisitor, attributedExpressionAst: AttributedExpressionAst) -> object """
        ...

    def VisitBinaryExpression(self, binaryExpressionAst:BinaryExpressionAst) -> object:
        """ VisitBinaryExpression(self: ICustomAstVisitor, binaryExpressionAst: BinaryExpressionAst) -> object """
        ...

    def VisitBlockStatement(self, blockStatementAst:BlockStatementAst) -> object:
        """ VisitBlockStatement(self: ICustomAstVisitor, blockStatementAst: BlockStatementAst) -> object """
        ...

    def VisitBreakStatement(self, breakStatementAst:BreakStatementAst) -> object:
        """ VisitBreakStatement(self: ICustomAstVisitor, breakStatementAst: BreakStatementAst) -> object """
        ...

    def VisitCatchClause(self, catchClauseAst:CatchClauseAst) -> object:
        """ VisitCatchClause(self: ICustomAstVisitor, catchClauseAst: CatchClauseAst) -> object """
        ...

    def VisitCommand(self, commandAst:CommandAst) -> object:
        """ VisitCommand(self: ICustomAstVisitor, commandAst: CommandAst) -> object """
        ...

    def VisitCommandExpression(self, commandExpressionAst:CommandExpressionAst) -> object:
        """ VisitCommandExpression(self: ICustomAstVisitor, commandExpressionAst: CommandExpressionAst) -> object """
        ...

    def VisitCommandParameter(self, commandParameterAst:CommandParameterAst) -> object:
        """ VisitCommandParameter(self: ICustomAstVisitor, commandParameterAst: CommandParameterAst) -> object """
        ...

    def VisitConstantExpression(self, constantExpressionAst:ConstantExpressionAst) -> object:
        """ VisitConstantExpression(self: ICustomAstVisitor, constantExpressionAst: ConstantExpressionAst) -> object """
        ...

    def VisitContinueStatement(self, continueStatementAst:ContinueStatementAst) -> object:
        """ VisitContinueStatement(self: ICustomAstVisitor, continueStatementAst: ContinueStatementAst) -> object """
        ...

    def VisitConvertExpression(self, convertExpressionAst:ConvertExpressionAst) -> object:
        """ VisitConvertExpression(self: ICustomAstVisitor, convertExpressionAst: ConvertExpressionAst) -> object """
        ...

    def VisitDataStatement(self, dataStatementAst:DataStatementAst) -> object:
        """ VisitDataStatement(self: ICustomAstVisitor, dataStatementAst: DataStatementAst) -> object """
        ...

    def VisitDoUntilStatement(self, doUntilStatementAst:DoUntilStatementAst) -> object:
        """ VisitDoUntilStatement(self: ICustomAstVisitor, doUntilStatementAst: DoUntilStatementAst) -> object """
        ...

    def VisitDoWhileStatement(self, doWhileStatementAst:DoWhileStatementAst) -> object:
        """ VisitDoWhileStatement(self: ICustomAstVisitor, doWhileStatementAst: DoWhileStatementAst) -> object """
        ...

    def VisitErrorExpression(self, errorExpressionAst:ErrorExpressionAst) -> object:
        """ VisitErrorExpression(self: ICustomAstVisitor, errorExpressionAst: ErrorExpressionAst) -> object """
        ...

    def VisitErrorStatement(self, errorStatementAst:ErrorStatementAst) -> object:
        """ VisitErrorStatement(self: ICustomAstVisitor, errorStatementAst: ErrorStatementAst) -> object """
        ...

    def VisitExitStatement(self, exitStatementAst:ExitStatementAst) -> object:
        """ VisitExitStatement(self: ICustomAstVisitor, exitStatementAst: ExitStatementAst) -> object """
        ...

    def VisitExpandableStringExpression(self, expandableStringExpressionAst:ExpandableStringExpressionAst) -> object:
        """ VisitExpandableStringExpression(self: ICustomAstVisitor, expandableStringExpressionAst: ExpandableStringExpressionAst) -> object """
        ...

    def VisitFileRedirection(self, fileRedirectionAst:FileRedirectionAst) -> object:
        """ VisitFileRedirection(self: ICustomAstVisitor, fileRedirectionAst: FileRedirectionAst) -> object """
        ...

    def VisitForEachStatement(self, forEachStatementAst:ForEachStatementAst) -> object:
        """ VisitForEachStatement(self: ICustomAstVisitor, forEachStatementAst: ForEachStatementAst) -> object """
        ...

    def VisitForStatement(self, forStatementAst:ForStatementAst) -> object:
        """ VisitForStatement(self: ICustomAstVisitor, forStatementAst: ForStatementAst) -> object """
        ...

    def VisitFunctionDefinition(self, functionDefinitionAst:FunctionDefinitionAst) -> object:
        """ VisitFunctionDefinition(self: ICustomAstVisitor, functionDefinitionAst: FunctionDefinitionAst) -> object """
        ...

    def VisitHashtable(self, hashtableAst:HashtableAst) -> object:
        """ VisitHashtable(self: ICustomAstVisitor, hashtableAst: HashtableAst) -> object """
        ...

    def VisitIfStatement(self, ifStmtAst:IfStatementAst) -> object:
        """ VisitIfStatement(self: ICustomAstVisitor, ifStmtAst: IfStatementAst) -> object """
        ...

    def VisitIndexExpression(self, indexExpressionAst:IndexExpressionAst) -> object:
        """ VisitIndexExpression(self: ICustomAstVisitor, indexExpressionAst: IndexExpressionAst) -> object """
        ...

    def VisitInvokeMemberExpression(self, invokeMemberExpressionAst:InvokeMemberExpressionAst) -> object:
        """ VisitInvokeMemberExpression(self: ICustomAstVisitor, invokeMemberExpressionAst: InvokeMemberExpressionAst) -> object """
        ...

    def VisitMemberExpression(self, memberExpressionAst:MemberExpressionAst) -> object:
        """ VisitMemberExpression(self: ICustomAstVisitor, memberExpressionAst: MemberExpressionAst) -> object """
        ...

    def VisitMergingRedirection(self, mergingRedirectionAst:MergingRedirectionAst) -> object:
        """ VisitMergingRedirection(self: ICustomAstVisitor, mergingRedirectionAst: MergingRedirectionAst) -> object """
        ...

    def VisitNamedAttributeArgument(self, namedAttributeArgumentAst:NamedAttributeArgumentAst) -> object:
        """ VisitNamedAttributeArgument(self: ICustomAstVisitor, namedAttributeArgumentAst: NamedAttributeArgumentAst) -> object """
        ...

    def VisitNamedBlock(self, namedBlockAst:NamedBlockAst) -> object:
        """ VisitNamedBlock(self: ICustomAstVisitor, namedBlockAst: NamedBlockAst) -> object """
        ...

    def VisitParamBlock(self, paramBlockAst:ParamBlockAst) -> object:
        """ VisitParamBlock(self: ICustomAstVisitor, paramBlockAst: ParamBlockAst) -> object """
        ...

    def VisitParameter(self, parameterAst:ParameterAst) -> object:
        """ VisitParameter(self: ICustomAstVisitor, parameterAst: ParameterAst) -> object """
        ...

    def VisitParenExpression(self, parenExpressionAst:ParenExpressionAst) -> object:
        """ VisitParenExpression(self: ICustomAstVisitor, parenExpressionAst: ParenExpressionAst) -> object """
        ...

    def VisitPipeline(self, pipelineAst:PipelineAst) -> object:
        """ VisitPipeline(self: ICustomAstVisitor, pipelineAst: PipelineAst) -> object """
        ...

    def VisitReturnStatement(self, returnStatementAst:ReturnStatementAst) -> object:
        """ VisitReturnStatement(self: ICustomAstVisitor, returnStatementAst: ReturnStatementAst) -> object """
        ...

    def VisitScriptBlock(self, scriptBlockAst:ScriptBlockAst) -> object:
        """ VisitScriptBlock(self: ICustomAstVisitor, scriptBlockAst: ScriptBlockAst) -> object """
        ...

    def VisitScriptBlockExpression(self, scriptBlockExpressionAst:ScriptBlockExpressionAst) -> object:
        """ VisitScriptBlockExpression(self: ICustomAstVisitor, scriptBlockExpressionAst: ScriptBlockExpressionAst) -> object """
        ...

    def VisitStatementBlock(self, statementBlockAst:StatementBlockAst) -> object:
        """ VisitStatementBlock(self: ICustomAstVisitor, statementBlockAst: StatementBlockAst) -> object """
        ...

    def VisitStringConstantExpression(self, stringConstantExpressionAst:StringConstantExpressionAst) -> object:
        """ VisitStringConstantExpression(self: ICustomAstVisitor, stringConstantExpressionAst: StringConstantExpressionAst) -> object """
        ...

    def VisitSubExpression(self, subExpressionAst:SubExpressionAst) -> object:
        """ VisitSubExpression(self: ICustomAstVisitor, subExpressionAst: SubExpressionAst) -> object """
        ...

    def VisitSwitchStatement(self, switchStatementAst:SwitchStatementAst) -> object:
        """ VisitSwitchStatement(self: ICustomAstVisitor, switchStatementAst: SwitchStatementAst) -> object """
        ...

    def VisitThrowStatement(self, throwStatementAst:ThrowStatementAst) -> object:
        """ VisitThrowStatement(self: ICustomAstVisitor, throwStatementAst: ThrowStatementAst) -> object """
        ...

    def VisitTrap(self, trapStatementAst:TrapStatementAst) -> object:
        """ VisitTrap(self: ICustomAstVisitor, trapStatementAst: TrapStatementAst) -> object """
        ...

    def VisitTryStatement(self, tryStatementAst:TryStatementAst) -> object:
        """ VisitTryStatement(self: ICustomAstVisitor, tryStatementAst: TryStatementAst) -> object """
        ...

    def VisitTypeConstraint(self, typeConstraintAst:TypeConstraintAst) -> object:
        """ VisitTypeConstraint(self: ICustomAstVisitor, typeConstraintAst: TypeConstraintAst) -> object """
        ...

    def VisitTypeExpression(self, typeExpressionAst:TypeExpressionAst) -> object:
        """ VisitTypeExpression(self: ICustomAstVisitor, typeExpressionAst: TypeExpressionAst) -> object """
        ...

    def VisitUnaryExpression(self, unaryExpressionAst:UnaryExpressionAst) -> object:
        """ VisitUnaryExpression(self: ICustomAstVisitor, unaryExpressionAst: UnaryExpressionAst) -> object """
        ...

    def VisitUsingExpression(self, usingExpressionAst:UsingExpressionAst) -> object:
        """ VisitUsingExpression(self: ICustomAstVisitor, usingExpressionAst: UsingExpressionAst) -> object """
        ...

    def VisitVariableExpression(self, variableExpressionAst:VariableExpressionAst) -> object:
        """ VisitVariableExpression(self: ICustomAstVisitor, variableExpressionAst: VariableExpressionAst) -> object """
        ...

    def VisitWhileStatement(self, whileStatementAst:WhileStatementAst) -> object:
        """ VisitWhileStatement(self: ICustomAstVisitor, whileStatementAst: WhileStatementAst) -> object """
        ...


class ICustomAstVisitor2(ICustomAstVisitor): # skipped bases: <type 'object'>
    """ no doc """
    def VisitBaseCtorInvokeMemberExpression(self, baseCtorInvokeMemberExpressionAst:BaseCtorInvokeMemberExpressionAst) -> object:
        """ VisitBaseCtorInvokeMemberExpression(self: ICustomAstVisitor2, baseCtorInvokeMemberExpressionAst: BaseCtorInvokeMemberExpressionAst) -> object """
        ...

    def VisitConfigurationDefinition(self, configurationDefinitionAst:ConfigurationDefinitionAst) -> object:
        """ VisitConfigurationDefinition(self: ICustomAstVisitor2, configurationDefinitionAst: ConfigurationDefinitionAst) -> object """
        ...

    def VisitDynamicKeywordStatement(self, dynamicKeywordAst:DynamicKeywordStatementAst) -> object:
        """ VisitDynamicKeywordStatement(self: ICustomAstVisitor2, dynamicKeywordAst: DynamicKeywordStatementAst) -> object """
        ...

    def VisitFunctionMember(self, functionMemberAst:FunctionMemberAst) -> object:
        """ VisitFunctionMember(self: ICustomAstVisitor2, functionMemberAst: FunctionMemberAst) -> object """
        ...

    def VisitPropertyMember(self, propertyMemberAst:PropertyMemberAst) -> object:
        """ VisitPropertyMember(self: ICustomAstVisitor2, propertyMemberAst: PropertyMemberAst) -> object """
        ...

    def VisitTypeDefinition(self, typeDefinitionAst:TypeDefinitionAst) -> object:
        """ VisitTypeDefinition(self: ICustomAstVisitor2, typeDefinitionAst: TypeDefinitionAst) -> object """
        ...

    def VisitUsingStatement(self, usingStatement:UsingStatementAst) -> object:
        """ VisitUsingStatement(self: ICustomAstVisitor2, usingStatement: UsingStatementAst) -> object """
        ...


class IfStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ IfStatementAst(extent: IScriptExtent, clauses: IEnumerable[Tuple[PipelineBaseAst, StatementBlockAst]], elseClause: StatementBlockAst) """
    @property
    def Clauses(self) -> ReadOnlyCollection:
        """ Get: Clauses(self: IfStatementAst) -> ReadOnlyCollection[Tuple[PipelineBaseAst, StatementBlockAst]] """
        ...

    @property
    def ElseClause(self) -> StatementBlockAst:
        """ Get: ElseClause(self: IfStatementAst) -> StatementBlockAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: IfStatementAst) -> Ast """
        ...


class IndexExpressionAst(ExpressionAst, ISupportsAssignment): # skipped bases: <type 'object'>
    """ IndexExpressionAst(extent: IScriptExtent, target: ExpressionAst, index: ExpressionAst) """
    @property
    def Index(self) -> ExpressionAst:
        """ Get: Index(self: IndexExpressionAst) -> ExpressionAst """
        ...

    @property
    def Target(self) -> ExpressionAst:
        """ Get: Target(self: IndexExpressionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: IndexExpressionAst) -> Ast """
        ...


class InputRedirectionToken(RedirectionToken): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IScriptExtent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EndColumnNumber(self) -> int:
        """ Get: EndColumnNumber(self: IScriptExtent) -> int """
        ...

    @property
    def EndLineNumber(self) -> int:
        """ Get: EndLineNumber(self: IScriptExtent) -> int """
        ...

    @property
    def EndOffset(self) -> int:
        """ Get: EndOffset(self: IScriptExtent) -> int """
        ...

    @property
    def EndScriptPosition(self) -> IScriptPosition:
        """ Get: EndScriptPosition(self: IScriptExtent) -> IScriptPosition """
        ...

    @property
    def File(self) -> str:
        """ Get: File(self: IScriptExtent) -> str """
        ...

    @property
    def StartColumnNumber(self) -> int:
        """ Get: StartColumnNumber(self: IScriptExtent) -> int """
        ...

    @property
    def StartLineNumber(self) -> int:
        """ Get: StartLineNumber(self: IScriptExtent) -> int """
        ...

    @property
    def StartOffset(self) -> int:
        """ Get: StartOffset(self: IScriptExtent) -> int """
        ...

    @property
    def StartScriptPosition(self) -> IScriptPosition:
        """ Get: StartScriptPosition(self: IScriptExtent) -> IScriptPosition """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: IScriptExtent) -> str """
        ...



class IScriptPosition: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ColumnNumber(self) -> int:
        """ Get: ColumnNumber(self: IScriptPosition) -> int """
        ...

    @property
    def File(self) -> str:
        """ Get: File(self: IScriptPosition) -> str """
        ...

    @property
    def Line(self) -> str:
        """ Get: Line(self: IScriptPosition) -> str """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: IScriptPosition) -> int """
        ...

    @property
    def Offset(self) -> int:
        """ Get: Offset(self: IScriptPosition) -> int """
        ...


    def GetFullScript(self) -> str:
        """ GetFullScript(self: IScriptPosition) -> str """
        ...


class LabelToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LabelText(self) -> str:
        """ Get: LabelText(self: LabelToken) -> str """
        ...



class MergingRedirectionAst(RedirectionAst): # skipped bases: <type 'object'>
    """ MergingRedirectionAst(extent: IScriptExtent, from: RedirectionStream, to: RedirectionStream) """
    @property
    def ToStream(self) -> RedirectionStream:
        """ Get: ToStream(self: MergingRedirectionAst) -> RedirectionStream """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: MergingRedirectionAst) -> Ast """
        ...


class MergingRedirectionToken(RedirectionToken): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FromStream(self) -> RedirectionStream:
        """ Get: FromStream(self: MergingRedirectionToken) -> RedirectionStream """
        ...

    @property
    def ToStream(self) -> RedirectionStream:
        """ Get: ToStream(self: MergingRedirectionToken) -> RedirectionStream """
        ...



class MethodAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MethodAttributes, values: Hidden (64), None (0), Private (2), Public (1), Static (16) """
    Hidden: MethodAttributes = ...
    Private: MethodAttributes = ...
    Public: MethodAttributes = ...
    Static: MethodAttributes = ...
    value__ = ...


class NamedAttributeArgumentAst(Ast): # skipped bases: <type 'object'>
    """ NamedAttributeArgumentAst(extent: IScriptExtent, argumentName: str, argument: ExpressionAst, expressionOmitted: bool) """
    @property
    def Argument(self) -> ExpressionAst:
        """ Get: Argument(self: NamedAttributeArgumentAst) -> ExpressionAst """
        ...

    @property
    def ArgumentName(self) -> str:
        """ Get: ArgumentName(self: NamedAttributeArgumentAst) -> str """
        ...

    @property
    def ExpressionOmitted(self) -> bool:
        """ Get: ExpressionOmitted(self: NamedAttributeArgumentAst) -> bool """
        ...



class NamedBlockAst(Ast): # skipped bases: <type 'object'>
    """ NamedBlockAst(extent: IScriptExtent, blockName: TokenKind, statementBlock: StatementBlockAst, unnamed: bool) """
    @property
    def BlockKind(self) -> TokenKind:
        """ Get: BlockKind(self: NamedBlockAst) -> TokenKind """
        ...

    @property
    def Statements(self) -> ReadOnlyCollection:
        """ Get: Statements(self: NamedBlockAst) -> ReadOnlyCollection[StatementAst] """
        ...

    @property
    def Traps(self) -> ReadOnlyCollection:
        """ Get: Traps(self: NamedBlockAst) -> ReadOnlyCollection[TrapStatementAst] """
        ...

    @property
    def Unnamed(self) -> bool:
        """ Get: Unnamed(self: NamedBlockAst) -> bool """
        ...



class NullString: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> NullString:
        """ Get: Value() -> NullString """
        ...


    def ToString(self) -> str:
        """ ToString(self: NullString) -> str """
        ...



class NumberToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """ Get: Value(self: NumberToken) -> object """
        ...



class ParamBlockAst(Ast): # skipped bases: <type 'object'>
    """ ParamBlockAst(extent: IScriptExtent, attributes: IEnumerable[AttributeAst], parameters: IEnumerable[ParameterAst]) """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: ParamBlockAst) -> ReadOnlyCollection[AttributeAst] """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: ParamBlockAst) -> ReadOnlyCollection[ParameterAst] """
        ...



class ParameterAst(Ast): # skipped bases: <type 'object'>
    """ ParameterAst(extent: IScriptExtent, name: VariableExpressionAst, attributes: IEnumerable[AttributeBaseAst], defaultValue: ExpressionAst) """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: ParameterAst) -> ReadOnlyCollection[AttributeBaseAst] """
        ...

    @property
    def DefaultValue(self) -> ExpressionAst:
        """ Get: DefaultValue(self: ParameterAst) -> ExpressionAst """
        ...

    @property
    def Name(self) -> VariableExpressionAst:
        """ Get: Name(self: ParameterAst) -> VariableExpressionAst """
        ...

    @property
    def StaticType(self) -> Type:
        """ Get: StaticType(self: ParameterAst) -> Type """
        ...



class ParameterBindingResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConstantValue(self) -> object:
        """ Get: ConstantValue(self: ParameterBindingResult) -> object """
        ...

    @property
    def Parameter(self) -> ParameterMetadata:
        """ Get: Parameter(self: ParameterBindingResult) -> ParameterMetadata """
        ...

    @property
    def Value(self) -> CommandElementAst:
        """ Get: Value(self: ParameterBindingResult) -> CommandElementAst """
        ...



class ParameterToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ParameterName(self) -> str:
        """ Get: ParameterName(self: ParameterToken) -> str """
        ...

    @property
    def UsedColon(self) -> bool:
        """ Get: UsedColon(self: ParameterToken) -> bool """
        ...



class ParenExpressionAst(ExpressionAst, ISupportsAssignment): # skipped bases: <type 'object'>
    """ ParenExpressionAst(extent: IScriptExtent, pipeline: PipelineBaseAst) """
    @property
    def Pipeline(self) -> PipelineBaseAst:
        """ Get: Pipeline(self: ParenExpressionAst) -> PipelineBaseAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ParenExpressionAst) -> Ast """
        ...


class ParseError: # skipped bases: <type 'object'>, <type 'object'>
    """ ParseError(extent: IScriptExtent, errorId: str, message: str) """
    @property
    def ErrorId(self) -> str:
        """ Get: ErrorId(self: ParseError) -> str """
        ...

    @property
    def Extent(self) -> IScriptExtent:
        """ Get: Extent(self: ParseError) -> IScriptExtent """
        ...

    @property
    def IncompleteInput(self) -> bool:
        """ Get: IncompleteInput(self: ParseError) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ParseError) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: ParseError) -> str """
        ...


class Parser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ParseFile(fileName, tokens, errors) -> Tuple_[ScriptBlockAst, Array, Array]:
        """ ParseFile(fileName: str) -> (ScriptBlockAst, Array[Token], Array[ParseError]) """
        ...

    @staticmethod
    def ParseInput(input:str, *__args:str) -> Tuple_[ScriptBlockAst, Array, Array]:
        """
        ParseInput(input: str) -> (ScriptBlockAst, Array[Token], Array[ParseError])
        ParseInput(input: str, fileName: str) -> (ScriptBlockAst, Array[Token], Array[ParseError])
        """
        ...


class PipelineAst(PipelineBaseAst): # skipped bases: <type 'object'>
    """
    PipelineAst(extent: IScriptExtent, pipelineElements: IEnumerable[CommandBaseAst])
    PipelineAst(extent: IScriptExtent, commandAst: CommandBaseAst)
    """
    @property
    def PipelineElements(self) -> ReadOnlyCollection:
        """ Get: PipelineElements(self: PipelineAst) -> ReadOnlyCollection[CommandBaseAst] """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: PipelineAst) -> Ast """
        ...


class PropertyAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropertyAttributes, values: Hidden (64), Literal (32), None (0), Private (2), Public (1), Static (16) """
    Hidden: PropertyAttributes = ...
    Literal: PropertyAttributes = ...
    Private: PropertyAttributes = ...
    Public: PropertyAttributes = ...
    Static: PropertyAttributes = ...
    value__ = ...


class PropertyMemberAst(MemberAst): # skipped bases: <type 'object'>
    """ PropertyMemberAst(extent: IScriptExtent, name: str, propertyType: TypeConstraintAst, attributes: IEnumerable[AttributeAst], propertyAttributes: PropertyAttributes, initialValue: ExpressionAst) """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: PropertyMemberAst) -> ReadOnlyCollection[AttributeAst] """
        ...

    @property
    def InitialValue(self) -> ExpressionAst:
        """ Get: InitialValue(self: PropertyMemberAst) -> ExpressionAst """
        ...

    @property
    def IsHidden(self) -> bool:
        """ Get: IsHidden(self: PropertyMemberAst) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: PropertyMemberAst) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: PropertyMemberAst) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: PropertyMemberAst) -> bool """
        ...

    @property
    def PropertyAttributes(self) -> PropertyAttributes:
        """ Get: PropertyAttributes(self: PropertyMemberAst) -> PropertyAttributes """
        ...

    @property
    def PropertyType(self) -> TypeConstraintAst:
        """ Get: PropertyType(self: PropertyMemberAst) -> TypeConstraintAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: PropertyMemberAst) -> Ast """
        ...


class RedirectionStream(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RedirectionStream, values: All (0), Debug (5), Error (2), Information (6), Output (1), Verbose (4), Warning (3) """
    All: RedirectionStream = ...
    Debug: RedirectionStream = ...
    Error: RedirectionStream = ...
    Information: RedirectionStream = ...
    Output: RedirectionStream = ...
    value__ = ...
    Verbose: RedirectionStream = ...
    Warning: RedirectionStream = ...


class ReflectionTypeName(ITypeName, ISupportsTypeCaching): # skipped bases: <type 'object'>
    """ ReflectionTypeName(type: Type) """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: ReflectionTypeName, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ReflectionTypeName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ReflectionTypeName) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReturnStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ ReturnStatementAst(extent: IScriptExtent, pipeline: PipelineBaseAst) """
    @property
    def Pipeline(self) -> PipelineBaseAst:
        """ Get: Pipeline(self: ReturnStatementAst) -> PipelineBaseAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ReturnStatementAst) -> Ast """
        ...


class ScriptBlockAst(IParameterMetadataProvider, Ast): # skipped bases: <type 'object'>
    """
    ScriptBlockAst(extent: IScriptExtent, usingStatements: IEnumerable[UsingStatementAst], attributes: IEnumerable[AttributeAst], paramBlock: ParamBlockAst, beginBlock: NamedBlockAst, processBlock: NamedBlockAst, endBlock: NamedBlockAst, dynamicParamBlock: NamedBlockAst)
    ScriptBlockAst(extent: IScriptExtent, usingStatements: IEnumerable[UsingStatementAst], paramBlock: ParamBlockAst, beginBlock: NamedBlockAst, processBlock: NamedBlockAst, endBlock: NamedBlockAst, dynamicParamBlock: NamedBlockAst)
    ScriptBlockAst(extent: IScriptExtent, paramBlock: ParamBlockAst, beginBlock: NamedBlockAst, processBlock: NamedBlockAst, endBlock: NamedBlockAst, dynamicParamBlock: NamedBlockAst)
    ScriptBlockAst(extent: IScriptExtent, usingStatements: List[UsingStatementAst], paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool)
    ScriptBlockAst(extent: IScriptExtent, paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool)
    ScriptBlockAst(extent: IScriptExtent, paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool, isConfiguration: bool)
    ScriptBlockAst(extent: IScriptExtent, usingStatements: IEnumerable[UsingStatementAst], paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool, isConfiguration: bool)
    ScriptBlockAst(extent: IScriptExtent, attributes: IEnumerable[AttributeAst], paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool, isConfiguration: bool)
    ScriptBlockAst(extent: IScriptExtent, usingStatements: IEnumerable[UsingStatementAst], attributes: IEnumerable[AttributeAst], paramBlock: ParamBlockAst, statements: StatementBlockAst, isFilter: bool, isConfiguration: bool)
    """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: ScriptBlockAst) -> ReadOnlyCollection[AttributeAst] """
        ...

    @property
    def BeginBlock(self) -> NamedBlockAst:
        """ Get: BeginBlock(self: ScriptBlockAst) -> NamedBlockAst """
        ...

    @property
    def DynamicParamBlock(self) -> NamedBlockAst:
        """ Get: DynamicParamBlock(self: ScriptBlockAst) -> NamedBlockAst """
        ...

    @property
    def EndBlock(self) -> NamedBlockAst:
        """ Get: EndBlock(self: ScriptBlockAst) -> NamedBlockAst """
        ...

    @property
    def ParamBlock(self) -> ParamBlockAst:
        """ Get: ParamBlock(self: ScriptBlockAst) -> ParamBlockAst """
        ...

    @property
    def ProcessBlock(self) -> NamedBlockAst:
        """ Get: ProcessBlock(self: ScriptBlockAst) -> NamedBlockAst """
        ...

    @property
    def ScriptRequirements(self) -> ScriptRequirements:
        """ Get: ScriptRequirements(self: ScriptBlockAst) -> ScriptRequirements """
        ...

    @property
    def UsingStatements(self) -> ReadOnlyCollection:
        """ Get: UsingStatements(self: ScriptBlockAst) -> ReadOnlyCollection[UsingStatementAst] """
        ...


    def GetHelpContent(self) -> CommentHelpInfo:
        """ GetHelpContent(self: ScriptBlockAst) -> CommentHelpInfo """
        ...

    def GetScriptBlock(self) -> ScriptBlock:
        """ GetScriptBlock(self: ScriptBlockAst) -> ScriptBlock """
        ...


class ScriptBlockExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ ScriptBlockExpressionAst(extent: IScriptExtent, scriptBlock: ScriptBlockAst) """
    @property
    def ScriptBlock(self) -> ScriptBlockAst:
        """ Get: ScriptBlock(self: ScriptBlockExpressionAst) -> ScriptBlockAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ScriptBlockExpressionAst) -> Ast """
        ...


class ScriptExtent(IScriptExtent): # skipped bases: <type 'object'>
    """ ScriptExtent(startPosition: ScriptPosition, endPosition: ScriptPosition) """
    pass

class ScriptPosition(IScriptPosition): # skipped bases: <type 'object'>
    """
    ScriptPosition(scriptName: str, scriptLineNumber: int, offsetInLine: int, line: str)
    ScriptPosition(scriptName: str, scriptLineNumber: int, offsetInLine: int, line: str, fullScript: str)
    """
    pass

class ScriptRequirements: # skipped bases: <type 'object'>, <type 'object'>
    """ ScriptRequirements() """
    @property
    def IsElevationRequired(self) -> bool:
        """ Get: IsElevationRequired(self: ScriptRequirements) -> bool """
        ...

    @property
    def RequiredApplicationId(self) -> str:
        """ Get: RequiredApplicationId(self: ScriptRequirements) -> str """
        ...

    @property
    def RequiredAssemblies(self) -> ReadOnlyCollection:
        """ Get: RequiredAssemblies(self: ScriptRequirements) -> ReadOnlyCollection[str] """
        ...

    @property
    def RequiredModules(self) -> ReadOnlyCollection:
        """ Get: RequiredModules(self: ScriptRequirements) -> ReadOnlyCollection[ModuleSpecification] """
        ...

    @property
    def RequiredPSEditions(self) -> ReadOnlyCollection:
        """ Get: RequiredPSEditions(self: ScriptRequirements) -> ReadOnlyCollection[str] """
        ...

    @property
    def RequiredPSVersion(self) -> Version:
        """ Get: RequiredPSVersion(self: ScriptRequirements) -> Version """
        ...

    @property
    def RequiresPSSnapIns(self) -> ReadOnlyCollection:
        """ Get: RequiresPSSnapIns(self: ScriptRequirements) -> ReadOnlyCollection[PSSnapInSpecification] """
        ...



class StatementBlockAst(Ast): # skipped bases: <type 'object'>
    """ StatementBlockAst(extent: IScriptExtent, statements: IEnumerable[StatementAst], traps: IEnumerable[TrapStatementAst]) """
    @property
    def Statements(self) -> ReadOnlyCollection:
        """ Get: Statements(self: StatementBlockAst) -> ReadOnlyCollection[StatementAst] """
        ...

    @property
    def Traps(self) -> ReadOnlyCollection:
        """ Get: Traps(self: StatementBlockAst) -> ReadOnlyCollection[TrapStatementAst] """
        ...



class StaticBindingError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingException(self) -> ParameterBindingException:
        """ Get: BindingException(self: StaticBindingError) -> ParameterBindingException """
        ...

    @property
    def CommandElement(self) -> CommandElementAst:
        """ Get: CommandElement(self: StaticBindingError) -> CommandElementAst """
        ...



class StaticBindingResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingExceptions(self) -> Dictionary:
        """ Get: BindingExceptions(self: StaticBindingResult) -> Dictionary[str, StaticBindingError] """
        ...

    @property
    def BoundParameters(self) -> Dictionary:
        """ Get: BoundParameters(self: StaticBindingResult) -> Dictionary[str, ParameterBindingResult] """
        ...



class StaticParameterBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BindCommand(commandAst:CommandAst, resolve:bool = ..., desiredParameters:Array = ...) -> StaticBindingResult:
        """
        BindCommand(commandAst: CommandAst) -> StaticBindingResult
        BindCommand(commandAst: CommandAst, resolve: bool) -> StaticBindingResult
        BindCommand(commandAst: CommandAst, resolve: bool, desiredParameters: Array[str]) -> StaticBindingResult
        """
        ...

    __all__: list = ...


class StringConstantExpressionAst(ConstantExpressionAst): # skipped bases: <type 'object'>
    """ StringConstantExpressionAst(extent: IScriptExtent, value: str, stringConstantType: StringConstantType) """
    @property
    def StringConstantType(self) -> StringConstantType:
        """ Get: StringConstantType(self: StringConstantExpressionAst) -> StringConstantType """
        ...



class StringConstantType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StringConstantType, values: BareWord (4), DoubleQuoted (2), DoubleQuotedHereString (3), SingleQuoted (0), SingleQuotedHereString (1) """
    BareWord: StringConstantType = ...
    DoubleQuoted: StringConstantType = ...
    DoubleQuotedHereString: StringConstantType = ...
    SingleQuoted: StringConstantType = ...
    SingleQuotedHereString: StringConstantType = ...
    value__ = ...


class StringToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> str:
        """ Get: Value(self: StringToken) -> str """
        ...



class StringExpandableToken(StringToken): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NestedTokens(self) -> ReadOnlyCollection:
        """ Get: NestedTokens(self: StringExpandableToken) -> ReadOnlyCollection[Token] """
        ...



class StringLiteralToken(StringToken): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SubExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ SubExpressionAst(extent: IScriptExtent, statementBlock: StatementBlockAst) """
    @property
    def SubExpression(self) -> StatementBlockAst:
        """ Get: SubExpression(self: SubExpressionAst) -> StatementBlockAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: SubExpressionAst) -> Ast """
        ...


class SwitchFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SwitchFlags, values: CaseSensitive (16), Exact (8), File (1), None (0), Parallel (32), Regex (2), Wildcard (4) """
    CaseSensitive: SwitchFlags = ...
    Exact: SwitchFlags = ...
    File: SwitchFlags = ...
    Parallel: SwitchFlags = ...
    Regex: SwitchFlags = ...
    value__ = ...
    Wildcard: SwitchFlags = ...


class SwitchStatementAst(LabeledStatementAst): # skipped bases: <type 'object'>
    """ SwitchStatementAst(extent: IScriptExtent, label: str, condition: PipelineBaseAst, flags: SwitchFlags, clauses: IEnumerable[Tuple[ExpressionAst, StatementBlockAst]], default: StatementBlockAst) """
    @property
    def Clauses(self) -> ReadOnlyCollection:
        """ Get: Clauses(self: SwitchStatementAst) -> ReadOnlyCollection[Tuple[ExpressionAst, StatementBlockAst]] """
        ...

    @property
    def Default(self) -> StatementBlockAst:
        """ Get: Default(self: SwitchStatementAst) -> StatementBlockAst """
        ...

    @property
    def Flags(self) -> SwitchFlags:
        """ Get: Flags(self: SwitchStatementAst) -> SwitchFlags """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: SwitchStatementAst) -> Ast """
        ...


class ThrowStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ ThrowStatementAst(extent: IScriptExtent, pipeline: PipelineBaseAst) """
    @property
    def IsRethrow(self) -> bool:
        """ Get: IsRethrow(self: ThrowStatementAst) -> bool """
        ...

    @property
    def Pipeline(self) -> PipelineBaseAst:
        """ Get: Pipeline(self: ThrowStatementAst) -> PipelineBaseAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: ThrowStatementAst) -> Ast """
        ...


class TokenFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TokenFlags, values: AssignmentOperator (8192), AttributeName (4194304), BinaryOperator (256), BinaryPrecedenceAdd (4), BinaryPrecedenceBitwise (2), BinaryPrecedenceComparison (3), BinaryPrecedenceFormat (6), BinaryPrecedenceLogical (1), BinaryPrecedenceMask (7), BinaryPrecedenceMultiply (5), BinaryPrecedenceRange (7), CanConstantFold (8388608), CaseSensitiveOperator (1024), CommandName (524288), DisallowedInRestrictedMode (131072), Keyword (16), MemberName (1048576), None (0), ParseModeInvariant (32768), PrefixOrPostfixOperator (262144), ScriptBlockBlockName (32), SpecialOperator (4096), StatementDoesntSupportAttributes (16777216), TokenInError (65536), TypeName (2097152), UnaryOperator (512) """
    AssignmentOperator: TokenFlags = ...
    AttributeName: TokenFlags = ...
    BinaryOperator: TokenFlags = ...
    BinaryPrecedenceAdd: TokenFlags = ...
    BinaryPrecedenceBitwise: TokenFlags = ...
    BinaryPrecedenceComparison: TokenFlags = ...
    BinaryPrecedenceFormat: TokenFlags = ...
    BinaryPrecedenceLogical: TokenFlags = ...
    BinaryPrecedenceMask: TokenFlags = ...
    BinaryPrecedenceMultiply: TokenFlags = ...
    BinaryPrecedenceRange: TokenFlags = ...
    CanConstantFold: TokenFlags = ...
    CaseSensitiveOperator: TokenFlags = ...
    CommandName: TokenFlags = ...
    DisallowedInRestrictedMode: TokenFlags = ...
    Keyword: TokenFlags = ...
    MemberName: TokenFlags = ...
    ParseModeInvariant: TokenFlags = ...
    PrefixOrPostfixOperator: TokenFlags = ...
    ScriptBlockBlockName: TokenFlags = ...
    SpecialOperator: TokenFlags = ...
    StatementDoesntSupportAttributes: TokenFlags = ...
    TokenInError: TokenFlags = ...
    TypeName: TokenFlags = ...
    UnaryOperator: TokenFlags = ...
    value__ = ...


class TokenKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TokenKind, values: Ampersand (28), And (53), AndAnd (26), As (94), Assembly (165), AtCurly (23), AtParen (22), Band (56), Base (168), Begin (119), Bnot (52), Bor (57), Break (120), Bxor (58), Catch (121), Ccontains (87), Ceq (76), Cge (78), Cgt (79), Cin (89), Class (122), Cle (81), Clike (82), Clt (80), Cmatch (84), Cne (77), Cnotcontains (88), Cnotin (90), Cnotlike (83), Cnotmatch (85), Colon (99), ColonColon (34), Comma (30), Command (166), Comment (10), Configuration (155), Continue (123), Creplace (86), Csplit (91), Data (124), Define (125), Divide (38), DivideEquals (46), Do (126), DollarParen (24), Dot (35), DotDot (33), DynamicKeyword (156), Dynamicparam (127), Else (128), ElseIf (129), End (130), EndOfInput (11), Enum (161), Equals (42), Exclaim (36), Exit (131), Filter (132), Finally (133), For (134), Foreach (135), Format (50), From (136), Function (137), Generic (7), HereStringExpandable (15), HereStringLiteral (14), Hidden (167), Icontains (71), Identifier (6), Ieq (60), If (138), Ige (62), Igt (63), Iin (73), Ile (65), Ilike (66), Ilt (64), Imatch (68), In (139), Ine (61), InlineScript (154), Inotcontains (72), Inotin (74), Inotlike (67), Inotmatch (69), Interface (160), Ireplace (70), Is (92), IsNot (93), Isplit (75), Join (59), Label (5), LBracket (20), LCurly (18), LineContinuation (9), LParen (16), Minus (41), MinusEquals (44), MinusMinus (31), Module (163), Multiply (37), MultiplyEquals (45), Namespace (162), NewLine (8), Not (51), Number (4), Or (54), OrOr (27), Parallel (152), Param (140), Parameter (3), Pipe (29), Plus (40), PlusEquals (43), PlusPlus (32), PostfixMinusMinus (96), PostfixPlusPlus (95), Private (158), Process (141), Public (157), RBracket (21), RCurly (19), RedirectInStd (49), Redirection (48), Rem (39), RemainderEquals (47), Return (142), RParen (17), Semi (25), Sequence (153), Shl (97), Shr (98), SplattedVariable (2), Static (159), StringExpandable (13), StringLiteral (12), Switch (143), Throw (144), Trap (145), Try (146), Type (164), Unknown (0), Until (147), Using (148), Var (149), Variable (1), While (150), Workflow (151), Xor (55) """
    Ampersand: TokenKind = ...
    And: TokenKind = ...
    AndAnd: TokenKind = ...
    As: TokenKind = ...
    Assembly: TokenKind = ...
    AtCurly: TokenKind = ...
    AtParen: TokenKind = ...
    Band: TokenKind = ...
    Base: TokenKind = ...
    Begin: TokenKind = ...
    Bnot: TokenKind = ...
    Bor: TokenKind = ...
    Break: TokenKind = ...
    Bxor: TokenKind = ...
    Catch: TokenKind = ...
    Ccontains: TokenKind = ...
    Ceq: TokenKind = ...
    Cge: TokenKind = ...
    Cgt: TokenKind = ...
    Cin: TokenKind = ...
    Class: TokenKind = ...
    Cle: TokenKind = ...
    Clike: TokenKind = ...
    Clt: TokenKind = ...
    Cmatch: TokenKind = ...
    Cne: TokenKind = ...
    Cnotcontains: TokenKind = ...
    Cnotin: TokenKind = ...
    Cnotlike: TokenKind = ...
    Cnotmatch: TokenKind = ...
    Colon: TokenKind = ...
    ColonColon: TokenKind = ...
    Comma: TokenKind = ...
    Command: TokenKind = ...
    Comment: TokenKind = ...
    Configuration: TokenKind = ...
    Continue: TokenKind = ...
    Creplace: TokenKind = ...
    Csplit: TokenKind = ...
    Data: TokenKind = ...
    Define: TokenKind = ...
    Divide: TokenKind = ...
    DivideEquals: TokenKind = ...
    Do: TokenKind = ...
    DollarParen: TokenKind = ...
    Dot: TokenKind = ...
    DotDot: TokenKind = ...
    DynamicKeyword: TokenKind = ...
    Dynamicparam: TokenKind = ...
    Else: TokenKind = ...
    ElseIf: TokenKind = ...
    End: TokenKind = ...
    EndOfInput: TokenKind = ...
    Enum: TokenKind = ...
    Equals: TokenKind = ...
    Exclaim: TokenKind = ...
    Exit: TokenKind = ...
    Filter: TokenKind = ...
    Finally: TokenKind = ...
    For: TokenKind = ...
    Foreach: TokenKind = ...
    Format: TokenKind = ...
    From: TokenKind = ...
    Function: TokenKind = ...
    Generic: TokenKind = ...
    HereStringExpandable: TokenKind = ...
    HereStringLiteral: TokenKind = ...
    Hidden: TokenKind = ...
    Icontains: TokenKind = ...
    Identifier: TokenKind = ...
    Ieq: TokenKind = ...
    If: TokenKind = ...
    Ige: TokenKind = ...
    Igt: TokenKind = ...
    Iin: TokenKind = ...
    Ile: TokenKind = ...
    Ilike: TokenKind = ...
    Ilt: TokenKind = ...
    Imatch: TokenKind = ...
    In: TokenKind = ...
    Ine: TokenKind = ...
    InlineScript: TokenKind = ...
    Inotcontains: TokenKind = ...
    Inotin: TokenKind = ...
    Inotlike: TokenKind = ...
    Inotmatch: TokenKind = ...
    Interface: TokenKind = ...
    Ireplace: TokenKind = ...
    Is: TokenKind = ...
    IsNot: TokenKind = ...
    Isplit: TokenKind = ...
    Join: TokenKind = ...
    Label: TokenKind = ...
    LBracket: TokenKind = ...
    LCurly: TokenKind = ...
    LineContinuation: TokenKind = ...
    LParen: TokenKind = ...
    Minus: TokenKind = ...
    MinusEquals: TokenKind = ...
    MinusMinus: TokenKind = ...
    Module: TokenKind = ...
    Multiply: TokenKind = ...
    MultiplyEquals: TokenKind = ...
    Namespace: TokenKind = ...
    NewLine: TokenKind = ...
    Not: TokenKind = ...
    Number: TokenKind = ...
    Or: TokenKind = ...
    OrOr: TokenKind = ...
    Parallel: TokenKind = ...
    Param: TokenKind = ...
    Parameter: TokenKind = ...
    Pipe: TokenKind = ...
    Plus: TokenKind = ...
    PlusEquals: TokenKind = ...
    PlusPlus: TokenKind = ...
    PostfixMinusMinus: TokenKind = ...
    PostfixPlusPlus: TokenKind = ...
    Private: TokenKind = ...
    Process: TokenKind = ...
    Public: TokenKind = ...
    RBracket: TokenKind = ...
    RCurly: TokenKind = ...
    RedirectInStd: TokenKind = ...
    Redirection: TokenKind = ...
    Rem: TokenKind = ...
    RemainderEquals: TokenKind = ...
    Return: TokenKind = ...
    RParen: TokenKind = ...
    Semi: TokenKind = ...
    Sequence: TokenKind = ...
    Shl: TokenKind = ...
    Shr: TokenKind = ...
    SplattedVariable: TokenKind = ...
    Static: TokenKind = ...
    StringExpandable: TokenKind = ...
    StringLiteral: TokenKind = ...
    Switch: TokenKind = ...
    Throw: TokenKind = ...
    Trap: TokenKind = ...
    Try: TokenKind = ...
    Type: TokenKind = ...
    Unknown: TokenKind = ...
    Until: TokenKind = ...
    Using: TokenKind = ...
    value__ = ...
    Var: TokenKind = ...
    Variable: TokenKind = ...
    While: TokenKind = ...
    Workflow: TokenKind = ...
    Xor: TokenKind = ...


class TokenTraits: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetTraits(kind:TokenKind) -> TokenFlags:
        """ GetTraits(kind: TokenKind) -> TokenFlags """
        ...

    @staticmethod
    def HasTrait(kind:TokenKind, flag:TokenFlags) -> bool:
        """ HasTrait(kind: TokenKind, flag: TokenFlags) -> bool """
        ...

    @staticmethod
    def Text(kind:TokenKind) -> str:
        """ Text(kind: TokenKind) -> str """
        ...

    __all__: list = ...


class TrapStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ TrapStatementAst(extent: IScriptExtent, trapType: TypeConstraintAst, body: StatementBlockAst) """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: TrapStatementAst) -> StatementBlockAst """
        ...

    @property
    def TrapType(self) -> TypeConstraintAst:
        """ Get: TrapType(self: TrapStatementAst) -> TypeConstraintAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: TrapStatementAst) -> Ast """
        ...


class TryStatementAst(StatementAst): # skipped bases: <type 'object'>
    """ TryStatementAst(extent: IScriptExtent, body: StatementBlockAst, catchClauses: IEnumerable[CatchClauseAst], finally: StatementBlockAst) """
    @property
    def Body(self) -> StatementBlockAst:
        """ Get: Body(self: TryStatementAst) -> StatementBlockAst """
        ...

    @property
    def CatchClauses(self) -> ReadOnlyCollection:
        """ Get: CatchClauses(self: TryStatementAst) -> ReadOnlyCollection[CatchClauseAst] """
        ...

    @property
    def Finally(self) -> StatementBlockAst:
        """ Get: Finally(self: TryStatementAst) -> StatementBlockAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: TryStatementAst) -> Ast """
        ...


class TypeAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeAttributes, values: Class (1), Enum (4), Interface (2), None (0) """
    Class: TypeAttributes = ...
    Enum: TypeAttributes = ...
    Interface: TypeAttributes = ...
    value__ = ...


class TypeConstraintAst(AttributeBaseAst): # skipped bases: <type 'object'>
    """
    TypeConstraintAst(extent: IScriptExtent, typeName: ITypeName)
    TypeConstraintAst(extent: IScriptExtent, type: Type)
    """
    def Copy(self) -> Ast:
        """ Copy(self: TypeConstraintAst) -> Ast """
        ...


class TypeDefinitionAst(StatementAst): # skipped bases: <type 'object'>
    """ TypeDefinitionAst(extent: IScriptExtent, name: str, attributes: IEnumerable[AttributeAst], members: IEnumerable[MemberAst], typeAttributes: TypeAttributes, baseTypes: IEnumerable[TypeConstraintAst]) """
    @property
    def Attributes(self) -> ReadOnlyCollection:
        """ Get: Attributes(self: TypeDefinitionAst) -> ReadOnlyCollection[AttributeAst] """
        ...

    @property
    def BaseTypes(self) -> ReadOnlyCollection:
        """ Get: BaseTypes(self: TypeDefinitionAst) -> ReadOnlyCollection[TypeConstraintAst] """
        ...

    @property
    def IsClass(self) -> bool:
        """ Get: IsClass(self: TypeDefinitionAst) -> bool """
        ...

    @property
    def IsEnum(self) -> bool:
        """ Get: IsEnum(self: TypeDefinitionAst) -> bool """
        ...

    @property
    def IsInterface(self) -> bool:
        """ Get: IsInterface(self: TypeDefinitionAst) -> bool """
        ...

    @property
    def Members(self) -> ReadOnlyCollection:
        """ Get: Members(self: TypeDefinitionAst) -> ReadOnlyCollection[MemberAst] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TypeDefinitionAst) -> str """
        ...

    @property
    def TypeAttributes(self) -> TypeAttributes:
        """ Get: TypeAttributes(self: TypeDefinitionAst) -> TypeAttributes """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: TypeDefinitionAst) -> Ast """
        ...


class TypeExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ TypeExpressionAst(extent: IScriptExtent, typeName: ITypeName) """
    @property
    def TypeName(self) -> ITypeName:
        """ Get: TypeName(self: TypeExpressionAst) -> ITypeName """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: TypeExpressionAst) -> Ast """
        ...


class TypeName(ITypeName, ISupportsTypeCaching): # skipped bases: <type 'object'>
    """
    TypeName(extent: IScriptExtent, name: str)
    TypeName(extent: IScriptExtent, name: str, assembly: str)
    """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: TypeName, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TypeName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: TypeName) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UnaryExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ UnaryExpressionAst(extent: IScriptExtent, tokenKind: TokenKind, child: ExpressionAst) """
    @property
    def Child(self) -> ExpressionAst:
        """ Get: Child(self: UnaryExpressionAst) -> ExpressionAst """
        ...

    @property
    def TokenKind(self) -> TokenKind:
        """ Get: TokenKind(self: UnaryExpressionAst) -> TokenKind """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: UnaryExpressionAst) -> Ast """
        ...


class UsingExpressionAst(ExpressionAst): # skipped bases: <type 'object'>
    """ UsingExpressionAst(extent: IScriptExtent, expressionAst: ExpressionAst) """
    @property
    def SubExpression(self) -> ExpressionAst:
        """ Get: SubExpression(self: UsingExpressionAst) -> ExpressionAst """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: UsingExpressionAst) -> Ast """
        ...

    @staticmethod
    def ExtractUsingVariable(usingExpressionAst:UsingExpressionAst) -> VariableExpressionAst:
        """ ExtractUsingVariable(usingExpressionAst: UsingExpressionAst) -> VariableExpressionAst """
        ...


class UsingStatementAst(StatementAst): # skipped bases: <type 'object'>
    """
    UsingStatementAst(extent: IScriptExtent, kind: UsingStatementKind, name: StringConstantExpressionAst)
    UsingStatementAst(extent: IScriptExtent, moduleSpecification: HashtableAst)
    UsingStatementAst(extent: IScriptExtent, kind: UsingStatementKind, aliasName: StringConstantExpressionAst, resolvedAliasAst: StringConstantExpressionAst)
    UsingStatementAst(extent: IScriptExtent, aliasName: StringConstantExpressionAst, moduleSpecification: HashtableAst)
    """
    @property
    def Alias(self) -> StringConstantExpressionAst:
        """ Get: Alias(self: UsingStatementAst) -> StringConstantExpressionAst """
        ...

    @property
    def ModuleSpecification(self) -> HashtableAst:
        """ Get: ModuleSpecification(self: UsingStatementAst) -> HashtableAst """
        ...

    @property
    def Name(self) -> StringConstantExpressionAst:
        """ Get: Name(self: UsingStatementAst) -> StringConstantExpressionAst """
        ...

    @property
    def UsingStatementKind(self) -> UsingStatementKind:
        """ Get: UsingStatementKind(self: UsingStatementAst) -> UsingStatementKind """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: UsingStatementAst) -> Ast """
        ...


class UsingStatementKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UsingStatementKind, values: Assembly (0), Command (1), Module (2), Namespace (3), Type (4) """
    Assembly: UsingStatementKind = ...
    Command: UsingStatementKind = ...
    Module: UsingStatementKind = ...
    Namespace: UsingStatementKind = ...
    Type: UsingStatementKind = ...
    value__ = ...


class VariableExpressionAst(ExpressionAst, ISupportsAssignment, IAssignableValue): # skipped bases: <type 'object'>
    """
    VariableExpressionAst(extent: IScriptExtent, variableName: str, splatted: bool)
    VariableExpressionAst(extent: IScriptExtent, variablePath: VariablePath, splatted: bool)
    """
    @property
    def Splatted(self) -> bool:
        """ Get: Splatted(self: VariableExpressionAst) -> bool """
        ...

    @property
    def VariablePath(self) -> VariablePath:
        """ Get: VariablePath(self: VariableExpressionAst) -> VariablePath """
        ...


    def Copy(self) -> Ast:
        """ Copy(self: VariableExpressionAst) -> Ast """
        ...

    def IsConstantVariable(self) -> bool:
        """ IsConstantVariable(self: VariableExpressionAst) -> bool """
        ...


class VariableToken(Token): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: VariableToken) -> str """
        ...

    @property
    def VariablePath(self) -> VariablePath:
        """ Get: VariablePath(self: VariableToken) -> VariablePath """
        ...



class WhileStatementAst(LoopStatementAst): # skipped bases: <type 'object'>
    """ WhileStatementAst(extent: IScriptExtent, label: str, condition: PipelineBaseAst, body: StatementBlockAst) """
    def Copy(self) -> Ast:
        """ Copy(self: WhileStatementAst) -> Ast """
        ...


