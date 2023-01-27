# encoding: utf-8
# module System.Workflow.Activities.Rules calls itself Rules
# from System.Workflow.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, Type

from System.CodeDom import (CodeBinaryOperatorType, CodeExpression, 
    CodeStatement)

from System.Collections import ICollection, IList

from System.Collections.ObjectModel import KeyedCollection

from System.EnterpriseServices import Activity

from System.Text import StringBuilder

from System.Workflow.ComponentModel import (ActivityCondition, 
    ActivityExecutionContext, DependencyObject, DependencyProperty, 
    IWorkflowChangeDiff, WorkflowChangeAction)

from System.Workflow.ComponentModel.Compiler import (
    ValidationErrorCollection)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class RuleConditionChangeAction(WorkflowChangeAction): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConditionName(self) -> str:
        """ Get: ConditionName(self: RuleConditionChangeAction) -> str """
        ...



class AddedConditionAction(RuleConditionChangeAction): # skipped bases: <type 'object'>
    """
    AddedConditionAction(addedConditionDefinition: RuleCondition)
    AddedConditionAction()
    """
    @property
    def ConditionDefinition(self) -> RuleCondition:
        """
        Get: ConditionDefinition(self: AddedConditionAction) -> RuleCondition
        Set: ConditionDefinition(self: AddedConditionAction) = value
        """
        ...


    def __new__(cls, addedConditionDefinition:RuleCondition = ...) -> Self:
        """
        __new__(cls: type, addedConditionDefinition: RuleCondition)
        __new__(cls: type)
        """
        ...


class RuleSetChangeAction(WorkflowChangeAction): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RuleSetName(self) -> str:
        """ Get: RuleSetName(self: RuleSetChangeAction) -> str """
        ...



class AddedRuleSetAction(RuleSetChangeAction): # skipped bases: <type 'object'>
    """
    AddedRuleSetAction(addedRuleSetDefinition: RuleSet)
    AddedRuleSetAction()
    """
    @property
    def RuleSetDefinition(self) -> RuleSet:
        """
        Get: RuleSetDefinition(self: AddedRuleSetAction) -> RuleSet
        Set: RuleSetDefinition(self: AddedRuleSetAction) = value
        """
        ...


    def __new__(cls, addedRuleSetDefinition:RuleSet = ...) -> Self:
        """
        __new__(cls: type, addedRuleSetDefinition: RuleSet)
        __new__(cls: type)
        """
        ...


class IRuleExpression: # skipped bases: <type 'object'>
    """ no doc """
    def AnalyzeUsage(self, analysis:RuleAnalysis, isRead:bool, isWritten:bool, qualifier:RulePathQualifier): # -> 
        """ AnalyzeUsage(self: IRuleExpression, analysis: RuleAnalysis, isRead: bool, isWritten: bool, qualifier: RulePathQualifier) """
        ...

    def Clone(self) -> CodeExpression:
        """ Clone(self: IRuleExpression) -> CodeExpression """
        ...

    def Decompile(self, stringBuilder:StringBuilder, parentExpression:CodeExpression): # -> 
        """ Decompile(self: IRuleExpression, stringBuilder: StringBuilder, parentExpression: CodeExpression) """
        ...

    def Evaluate(self, execution:RuleExecution) -> RuleExpressionResult:
        """ Evaluate(self: IRuleExpression, execution: RuleExecution) -> RuleExpressionResult """
        ...

    def Match(self, expression:CodeExpression) -> bool:
        """ Match(self: IRuleExpression, expression: CodeExpression) -> bool """
        ...

    def Validate(self, validation:RuleValidation, isWritten:bool) -> RuleExpressionInfo:
        """ Validate(self: IRuleExpression, validation: RuleValidation, isWritten: bool) -> RuleExpressionInfo """
        ...


class RemovedConditionAction(RuleConditionChangeAction): # skipped bases: <type 'object'>
    """
    RemovedConditionAction(removedConditionDefinition: RuleCondition)
    RemovedConditionAction()
    """
    @property
    def ConditionDefinition(self) -> RuleCondition:
        """
        Get: ConditionDefinition(self: RemovedConditionAction) -> RuleCondition
        Set: ConditionDefinition(self: RemovedConditionAction) = value
        """
        ...


    def __new__(cls, removedConditionDefinition:RuleCondition = ...) -> Self:
        """
        __new__(cls: type, removedConditionDefinition: RuleCondition)
        __new__(cls: type)
        """
        ...


class RemovedRuleSetAction(RuleSetChangeAction): # skipped bases: <type 'object'>
    """
    RemovedRuleSetAction(removedRuleSetDefinition: RuleSet)
    RemovedRuleSetAction()
    """
    @property
    def RuleSetDefinition(self) -> RuleSet:
        """
        Get: RuleSetDefinition(self: RemovedRuleSetAction) -> RuleSet
        Set: RuleSetDefinition(self: RemovedRuleSetAction) = value
        """
        ...


    def __new__(cls, removedRuleSetDefinition:RuleSet = ...) -> Self:
        """
        __new__(cls: type, removedRuleSetDefinition: RuleSet)
        __new__(cls: type)
        """
        ...


class Rule: # skipped bases: <type 'object'>, <type 'object'>
    """
    Rule()
    Rule(name: str)
    Rule(name: str, condition: RuleCondition, thenActions: IList[RuleAction])
    Rule(name: str, condition: RuleCondition, thenActions: IList[RuleAction], elseActions: IList[RuleAction])
    """
    @property
    def Active(self) -> bool:
        """
        Get: Active(self: Rule) -> bool
        Set: Active(self: Rule) = value
        """
        ...

    @property
    def Condition(self) -> RuleCondition:
        """
        Get: Condition(self: Rule) -> RuleCondition
        Set: Condition(self: Rule) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Rule) -> str
        Set: Description(self: Rule) = value
        """
        ...

    @property
    def ElseActions(self) -> IList:
        """ Get: ElseActions(self: Rule) -> IList[RuleAction] """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Rule) -> str
        Set: Name(self: Rule) = value
        """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: Rule) -> int
        Set: Priority(self: Rule) = value
        """
        ...

    @property
    def ReevaluationBehavior(self) -> RuleReevaluationBehavior:
        """
        Get: ReevaluationBehavior(self: Rule) -> RuleReevaluationBehavior
        Set: ReevaluationBehavior(self: Rule) = value
        """
        ...

    @property
    def ThenActions(self) -> IList:
        """ Get: ThenActions(self: Rule) -> IList[RuleAction] """
        ...


    def Clone(self) -> Rule:
        """ Clone(self: Rule) -> Rule """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Rule, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Rule) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleAction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Clone(self) -> RuleAction:
        """ Clone(self: RuleAction) -> RuleAction """
        ...

    def Execute(self, context:RuleExecution): # -> 
        """ Execute(self: RuleAction, context: RuleExecution) """
        ...

    def GetSideEffects(self, validation:RuleValidation) -> ICollection:
        """ GetSideEffects(self: RuleAction, validation: RuleValidation) -> ICollection[str] """
        ...

    def Validate(self, validator:RuleValidation) -> bool:
        """ Validate(self: RuleAction, validator: RuleValidation) -> bool """
        ...


class RuleActionTrackingEvent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConditionResult(self) -> bool:
        """ Get: ConditionResult(self: RuleActionTrackingEvent) -> bool """
        ...

    @property
    def RuleName(self) -> str:
        """ Get: RuleName(self: RuleActionTrackingEvent) -> str """
        ...



class RuleAnalysis: # skipped bases: <type 'object'>, <type 'object'>
    """ RuleAnalysis(validation: RuleValidation, forWrites: bool) """
    @property
    def ForWrites(self) -> bool:
        """ Get: ForWrites(self: RuleAnalysis) -> bool """
        ...


    def AddSymbol(self, symbol:str): # -> 
        """ AddSymbol(self: RuleAnalysis, symbol: str) """
        ...

    def GetSymbols(self) -> ICollection:
        """ GetSymbols(self: RuleAnalysis) -> ICollection[str] """
        ...


class RuleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class RuleAttributeTarget(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RuleAttributeTarget, values: Parameter (0), This (1) """
    Parameter: RuleAttributeTarget = ...
    This: RuleAttributeTarget = ...
    value__ = ...


class RuleChainingBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RuleChainingBehavior, values: Full (2), None (0), UpdateOnly (1) """
    Full: RuleChainingBehavior = ...
    UpdateOnly: RuleChainingBehavior = ...
    value__ = ...


class RuleCondition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: RuleCondition) -> str
        Set: Name(self: RuleCondition) = value
        """
        ...


    def Clone(self) -> RuleCondition:
        """ Clone(self: RuleCondition) -> RuleCondition """
        ...

    def Evaluate(self, execution:RuleExecution) -> bool:
        """ Evaluate(self: RuleCondition, execution: RuleExecution) -> bool """
        ...

    def GetDependencies(self, validation:RuleValidation) -> ICollection:
        """ GetDependencies(self: RuleCondition, validation: RuleValidation) -> ICollection[str] """
        ...

    def OnRuntimeInitialized(self): # -> 
        """ OnRuntimeInitialized(self: RuleCondition) """
        ...

    def Validate(self, validation:RuleValidation) -> bool:
        """ Validate(self: RuleCondition, validation: RuleValidation) -> bool """
        ...


class RuleConditionCollection(KeyedCollection, IWorkflowChangeDiff): # skipped bases: <type 'IList[RuleCondition]'>, <type 'IEnumerable[RuleCondition]'>, <type 'ICollection[RuleCondition]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[RuleCondition]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[RuleCondition]'>, <type 'object'>
    """ RuleConditionCollection() """
    pass

class RuleConditionReference(ActivityCondition): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ RuleConditionReference() """
    @property
    def ConditionName(self) -> str:
        """
        Get: ConditionName(self: RuleConditionReference) -> str
        Set: ConditionName(self: RuleConditionReference) = value
        """
        ...



class RuleDefinitions(IWorkflowChangeDiff): # skipped bases: <type 'object'>
    """ RuleDefinitions() """
    @property
    def Conditions(self) -> RuleConditionCollection:
        """ Get: Conditions(self: RuleDefinitions) -> RuleConditionCollection """
        ...

    @property
    def RuleSets(self) -> RuleSetCollection:
        """ Get: RuleSets(self: RuleDefinitions) -> RuleSetCollection """
        ...


    RuleDefinitionsProperty: DependencyProperty = ...


class RuleEngine: # skipped bases: <type 'object'>, <type 'object'>
    """
    RuleEngine(ruleSet: RuleSet, validation: RuleValidation)
    RuleEngine(ruleSet: RuleSet, objectType: Type)
    """
    def Execute(self, thisObject:object, executionContext:ActivityExecutionContext = ...): # -> 
        """ Execute(self: RuleEngine, thisObject: object, executionContext: ActivityExecutionContext)Execute(self: RuleEngine, thisObject: object) """
        ...


class RuleException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuleException()
    RuleException(message: str)
    RuleException(message: str, ex: Exception)
    """
    SerializeObjectState = ...


class RuleEvaluationException(RuleException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuleEvaluationException()
    RuleEvaluationException(message: str)
    RuleEvaluationException(message: str, ex: Exception)
    """
    SerializeObjectState = ...


class RuleEvaluationIncompatibleTypesException(RuleException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuleEvaluationIncompatibleTypesException()
    RuleEvaluationIncompatibleTypesException(message: str)
    RuleEvaluationIncompatibleTypesException(message: str, ex: Exception)
    RuleEvaluationIncompatibleTypesException(message: str, left: Type, op: CodeBinaryOperatorType, right: Type)
    RuleEvaluationIncompatibleTypesException(message: str, left: Type, op: CodeBinaryOperatorType, right: Type, ex: Exception)
    """
    @property
    def Left(self) -> Type:
        """
        Get: Left(self: RuleEvaluationIncompatibleTypesException) -> Type
        Set: Left(self: RuleEvaluationIncompatibleTypesException) = value
        """
        ...

    @property
    def Operator(self) -> CodeBinaryOperatorType:
        """
        Get: Operator(self: RuleEvaluationIncompatibleTypesException) -> CodeBinaryOperatorType
        Set: Operator(self: RuleEvaluationIncompatibleTypesException) = value
        """
        ...

    @property
    def Right(self) -> Type:
        """
        Get: Right(self: RuleEvaluationIncompatibleTypesException) -> Type
        Set: Right(self: RuleEvaluationIncompatibleTypesException) = value
        """
        ...


    SerializeObjectState = ...


class RuleExecution: # skipped bases: <type 'object'>, <type 'object'>
    """
    RuleExecution(validation: RuleValidation, thisObject: object)
    RuleExecution(validation: RuleValidation, thisObject: object, activityExecutionContext: ActivityExecutionContext)
    """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: RuleExecution) -> Activity """
        ...

    @property
    def ActivityExecutionContext(self) -> ActivityExecutionContext:
        """ Get: ActivityExecutionContext(self: RuleExecution) -> ActivityExecutionContext """
        ...

    @property
    def Halted(self) -> bool:
        """
        Get: Halted(self: RuleExecution) -> bool
        Set: Halted(self: RuleExecution) = value
        """
        ...

    @property
    def ThisObject(self) -> object:
        """ Get: ThisObject(self: RuleExecution) -> object """
        ...

    @property
    def Validation(self) -> RuleValidation:
        """
        Get: Validation(self: RuleExecution) -> RuleValidation
        Set: Validation(self: RuleExecution) = value
        """
        ...



class RuleExpressionCondition(RuleCondition): # skipped bases: <type 'object'>
    """
    RuleExpressionCondition()
    RuleExpressionCondition(conditionName: str)
    RuleExpressionCondition(conditionName: str, expression: CodeExpression)
    RuleExpressionCondition(expression: CodeExpression)
    """
    @property
    def Expression(self) -> CodeExpression:
        """
        Get: Expression(self: RuleExpressionCondition) -> CodeExpression
        Set: Expression(self: RuleExpressionCondition) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RuleExpressionCondition, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RuleExpressionCondition) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RuleExpressionCondition) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, conditionName: str)
        __new__(cls: type, conditionName: str, expression: CodeExpression)
        __new__(cls: type, expression: CodeExpression)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleExpressionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ RuleExpressionInfo(expressionType: Type) """
    @property
    def ExpressionType(self) -> Type:
        """ Get: ExpressionType(self: RuleExpressionInfo) -> Type """
        ...



class RuleExpressionResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: RuleExpressionResult) -> object
        Set: Value(self: RuleExpressionResult) = value
        """
        ...



class RuleExpressionWalker: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AnalyzeUsage(analysis:RuleAnalysis, expression:CodeExpression, isRead:bool, isWritten:bool, qualifier:RulePathQualifier): # -> 
        """ AnalyzeUsage(analysis: RuleAnalysis, expression: CodeExpression, isRead: bool, isWritten: bool, qualifier: RulePathQualifier) """
        ...

    @staticmethod
    def Clone(originalExpression:CodeExpression) -> CodeExpression:
        """ Clone(originalExpression: CodeExpression) -> CodeExpression """
        ...

    @staticmethod
    def Decompile(stringBuilder:StringBuilder, expression:CodeExpression, parentExpression:CodeExpression): # -> 
        """ Decompile(stringBuilder: StringBuilder, expression: CodeExpression, parentExpression: CodeExpression) """
        ...

    @staticmethod
    def Evaluate(execution:RuleExecution, expression:CodeExpression) -> RuleExpressionResult:
        """ Evaluate(execution: RuleExecution, expression: CodeExpression) -> RuleExpressionResult """
        ...

    @staticmethod
    def Match(firstExpression:CodeExpression, secondExpression:CodeExpression) -> bool:
        """ Match(firstExpression: CodeExpression, secondExpression: CodeExpression) -> bool """
        ...

    @staticmethod
    def Validate(validation:RuleValidation, expression:CodeExpression, isWritten:bool) -> RuleExpressionInfo:
        """ Validate(validation: RuleValidation, expression: CodeExpression, isWritten: bool) -> RuleExpressionInfo """
        ...

    __all__: list = ...


class RuleHaltAction(RuleAction): # skipped bases: <type 'object'>
    """ RuleHaltAction() """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: RuleHaltAction, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RuleHaltAction) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RuleHaltAction) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleInvokeAttribute(RuleAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RuleInvokeAttribute(methodInvoked: str) """
    @property
    def MethodInvoked(self) -> str:
        """ Get: MethodInvoked(self: RuleInvokeAttribute) -> str """
        ...


    def __new__(cls, methodInvoked:str) -> Self:
        """ __new__(cls: type, methodInvoked: str) """
        ...


class RuleLiteralResult(RuleExpressionResult): # skipped bases: <type 'object'>
    """ RuleLiteralResult(literal: object) """
    def __new__(cls, literal:object) -> Self:
        """ __new__(cls: type, literal: object) """
        ...


class RulePathQualifier: # skipped bases: <type 'object'>, <type 'object'>
    """ RulePathQualifier(name: str, next: RulePathQualifier) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: RulePathQualifier) -> str """
        ...

    @property
    def Next(self) -> RulePathQualifier:
        """ Get: Next(self: RulePathQualifier) -> RulePathQualifier """
        ...



class RuleReadWriteAttribute(RuleAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Path(self) -> str:
        """ Get: Path(self: RuleReadWriteAttribute) -> str """
        ...

    @property
    def Target(self) -> RuleAttributeTarget:
        """ Get: Target(self: RuleReadWriteAttribute) -> RuleAttributeTarget """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, path: str, target: RuleAttributeTarget) """
        ...


class RuleReadAttribute(RuleReadWriteAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    RuleReadAttribute(path: str, target: RuleAttributeTarget)
    RuleReadAttribute(path: str)
    """
    pass

class RuleReevaluationBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RuleReevaluationBehavior, values: Always (1), Never (0) """
    Always: RuleReevaluationBehavior = ...
    Never: RuleReevaluationBehavior = ...
    value__ = ...


class RuleSet: # skipped bases: <type 'object'>, <type 'object'>
    """
    RuleSet()
    RuleSet(name: str)
    RuleSet(name: str, description: str)
    """
    @property
    def ChainingBehavior(self) -> RuleChainingBehavior:
        """
        Get: ChainingBehavior(self: RuleSet) -> RuleChainingBehavior
        Set: ChainingBehavior(self: RuleSet) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: RuleSet) -> str
        Set: Description(self: RuleSet) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RuleSet) -> str
        Set: Name(self: RuleSet) = value
        """
        ...

    @property
    def Rules(self) -> ICollection:
        """ Get: Rules(self: RuleSet) -> ICollection[Rule] """
        ...


    def Clone(self) -> RuleSet:
        """ Clone(self: RuleSet) -> RuleSet """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: RuleSet, obj: object) -> bool """
        ...

    def Execute(self, ruleExecution:RuleExecution): # -> 
        """ Execute(self: RuleSet, ruleExecution: RuleExecution) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RuleSet) -> int """
        ...

    def Validate(self, validation:RuleValidation) -> bool:
        """ Validate(self: RuleSet, validation: RuleValidation) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleSetCollection(KeyedCollection, IWorkflowChangeDiff): # skipped bases: <type 'IEnumerable[RuleSet]'>, <type 'IList[RuleSet]'>, <type 'IEnumerable'>, <type 'ICollection[RuleSet]'>, <type 'IList'>, <type 'IReadOnlyList[RuleSet]'>, <type 'IReadOnlyCollection[RuleSet]'>, <type 'ICollection'>, <type 'object'>
    """ RuleSetCollection() """
    pass

class RuleSetReference(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    RuleSetReference()
    RuleSetReference(ruleSetName: str)
    """
    @property
    def RuleSetName(self) -> str:
        """
        Get: RuleSetName(self: RuleSetReference) -> str
        Set: RuleSetName(self: RuleSetReference) = value
        """
        ...


    def __new__(cls, ruleSetName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, ruleSetName: str)
        """
        ...


class RuleSetValidationException(RuleException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuleSetValidationException()
    RuleSetValidationException(message: str)
    RuleSetValidationException(message: str, ex: Exception)
    RuleSetValidationException(message: str, errors: ValidationErrorCollection)
    """
    @property
    def Errors(self) -> ValidationErrorCollection:
        """ Get: Errors(self: RuleSetValidationException) -> ValidationErrorCollection """
        ...


    SerializeObjectState = ...


class RuleStatementAction(RuleAction): # skipped bases: <type 'object'>
    """
    RuleStatementAction(codeDomStatement: CodeStatement)
    RuleStatementAction(codeDomExpression: CodeExpression)
    RuleStatementAction()
    """
    @property
    def CodeDomStatement(self) -> CodeStatement:
        """
        Get: CodeDomStatement(self: RuleStatementAction) -> CodeStatement
        Set: CodeDomStatement(self: RuleStatementAction) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RuleStatementAction, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RuleStatementAction) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RuleStatementAction) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:CodeStatement) -> Self:
        """
        __new__(cls: type, codeDomStatement: CodeStatement)
        __new__(cls: type, codeDomExpression: CodeExpression)
        __new__(cls: type)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleUpdateAction(RuleAction): # skipped bases: <type 'object'>
    """
    RuleUpdateAction(path: str)
    RuleUpdateAction()
    """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: RuleUpdateAction) -> str
        Set: Path(self: RuleUpdateAction) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: RuleUpdateAction, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RuleUpdateAction) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RuleUpdateAction) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, path:str = ...) -> Self:
        """
        __new__(cls: type, path: str)
        __new__(cls: type)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RuleValidation: # skipped bases: <type 'object'>, <type 'object'>
    """
    RuleValidation(activity: Activity, typeProvider: ITypeProvider, checkStaticType: bool)
    RuleValidation(thisType: Type, typeProvider: ITypeProvider)
    """
    @property
    def Errors(self) -> ValidationErrorCollection:
        """ Get: Errors(self: RuleValidation) -> ValidationErrorCollection """
        ...

    @property
    def ThisType(self) -> Type:
        """ Get: ThisType(self: RuleValidation) -> Type """
        ...


    def ExpressionInfo(self, expression:CodeExpression) -> RuleExpressionInfo:
        """ ExpressionInfo(self: RuleValidation, expression: CodeExpression) -> RuleExpressionInfo """
        ...

    def PopParentExpression(self): # -> 
        """ PopParentExpression(self: RuleValidation) """
        ...

    def PushParentExpression(self, newParent:CodeExpression) -> bool:
        """ PushParentExpression(self: RuleValidation, newParent: CodeExpression) -> bool """
        ...


class RuleWriteAttribute(RuleReadWriteAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    RuleWriteAttribute(path: str, target: RuleAttributeTarget)
    RuleWriteAttribute(path: str)
    """
    pass

class UpdatedConditionAction(RuleConditionChangeAction): # skipped bases: <type 'object'>
    """
    UpdatedConditionAction(conditionDefinition: RuleCondition, newConditionDefinition: RuleCondition)
    UpdatedConditionAction()
    """
    @property
    def ConditionDefinition(self) -> RuleCondition:
        """
        Get: ConditionDefinition(self: UpdatedConditionAction) -> RuleCondition
        Set: ConditionDefinition(self: UpdatedConditionAction) = value
        """
        ...

    @property
    def NewConditionDefinition(self) -> RuleCondition:
        """
        Get: NewConditionDefinition(self: UpdatedConditionAction) -> RuleCondition
        Set: NewConditionDefinition(self: UpdatedConditionAction) = value
        """
        ...


    def __new__(cls, conditionDefinition:RuleCondition = ..., newConditionDefinition:RuleCondition = ...) -> Self:
        """
        __new__(cls: type, conditionDefinition: RuleCondition, newConditionDefinition: RuleCondition)
        __new__(cls: type)
        """
        ...


class UpdatedRuleSetAction(RuleSetChangeAction): # skipped bases: <type 'object'>
    """
    UpdatedRuleSetAction(originalRuleSetDefinition: RuleSet, updatedRuleSetDefinition: RuleSet)
    UpdatedRuleSetAction()
    """
    @property
    def OriginalRuleSetDefinition(self) -> RuleSet:
        """
        Get: OriginalRuleSetDefinition(self: UpdatedRuleSetAction) -> RuleSet
        Set: OriginalRuleSetDefinition(self: UpdatedRuleSetAction) = value
        """
        ...

    @property
    def UpdatedRuleSetDefinition(self) -> RuleSet:
        """
        Get: UpdatedRuleSetDefinition(self: UpdatedRuleSetAction) -> RuleSet
        Set: UpdatedRuleSetDefinition(self: UpdatedRuleSetAction) = value
        """
        ...


    def __new__(cls, originalRuleSetDefinition:RuleSet = ..., updatedRuleSetDefinition:RuleSet = ...) -> Self:
        """
        __new__(cls: type, originalRuleSetDefinition: RuleSet, updatedRuleSetDefinition: RuleSet)
        __new__(cls: type)
        """
        ...


# variables with complex values

