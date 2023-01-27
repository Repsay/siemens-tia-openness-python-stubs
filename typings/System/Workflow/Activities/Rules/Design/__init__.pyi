# encoding: utf-8
# module System.Workflow.Activities.Rules.Design calls itself Design
# from System.Workflow.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.CodeDom import CodeExpression

from System.EnterpriseServices import Activity

from System.Windows.Forms import Form

from System.Workflow.Activities.Rules import RuleSet

from typing import Self


# no functions
# classes

class RuleConditionDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    RuleConditionDialog(activity: Activity, expression: CodeExpression)
    RuleConditionDialog(activityType: Type, typeProvider: ITypeProvider, expression: CodeExpression)
    """
    @property
    def Expression(self) -> CodeExpression:
        """ Get: Expression(self: RuleConditionDialog) -> CodeExpression """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, activity: Activity, expression: CodeExpression)
        __new__(cls: type, activityType: Type, typeProvider: ITypeProvider, expression: CodeExpression)
        """
        ...


class RuleSetDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    RuleSetDialog(activity: Activity, ruleSet: RuleSet)
    RuleSetDialog(activityType: Type, typeProvider: ITypeProvider, ruleSet: RuleSet)
    """
    @property
    def RuleSet(self) -> RuleSet:
        """ Get: RuleSet(self: RuleSetDialog) -> RuleSet """
        ...


    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, activity: Activity, ruleSet: RuleSet)
        __new__(cls: type, activityType: Type, typeProvider: ITypeProvider, ruleSet: RuleSet)
        """
        ...


