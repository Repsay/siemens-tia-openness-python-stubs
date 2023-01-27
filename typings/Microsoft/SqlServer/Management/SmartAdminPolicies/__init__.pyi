# encoding: utf-8
# module Microsoft.SqlServer.Management.SmartAdminPolicies calls itself SmartAdminPolicies
# from Microsoft.SqlServer.Management.SmartAdminPolicies, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Dmf import Policy

from Microsoft.SqlServer.Management.Smo import SqlSmoObject

from System import Array, Enum, ICloneable, Type

from System.Collections.Generic import Dictionary, List

"""The following names are not found in the module: field#
"""

# no functions
# classes

class EvaluationResult: # skipped bases: <type 'object'>, <type 'object'>
    """ EvaluationResult() """
    @property
    def PolicyEvaluationResults(self) -> Dictionary:
        """
        Get: PolicyEvaluationResults(self: EvaluationResult) -> Dictionary[Policy, EvaluationResultWithUserData]
        Set: PolicyEvaluationResults(self: EvaluationResult) = value
        """
        ...

    @property
    def RollupHealthState(self) -> HealthState:
        """ Get: RollupHealthState(self: EvaluationResult) -> HealthState """
        ...


    def AddResult(self, policy:Policy, result:HealthState, smoObject:SqlSmoObject = ...): # -> 
        """ AddResult(self: EvaluationResult, policy: Policy, result: EvaluationResult)AddResult(self: EvaluationResult, policy: Policy, result: HealthState, smoObject: SqlSmoObject) """
        ...

    def GetPolicyResult(self, policyName:str) -> EvaluationResultWithUserData:
        """ GetPolicyResult(self: EvaluationResult, policyName: str) -> EvaluationResultWithUserData """
        ...


class EvaluationResultWithUserData: # skipped bases: <type 'object'>, <type 'object'>
    """ EvaluationResultWithUserData(state: HealthState, userData: object) """
    @property
    def HealthState(self) -> HealthState:
        """
        Get: HealthState(self: EvaluationResultWithUserData) -> HealthState
        Set: HealthState(self: EvaluationResultWithUserData) = value
        """
        ...

    @property
    def UserData(self) -> object:
        """
        Get: UserData(self: EvaluationResultWithUserData) -> object
        Set: UserData(self: EvaluationResultWithUserData) = value
        """
        ...



class HealthState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HealthState, values: Error (16), Healthy (1), PolicyExecutionFailure (4), Unknown (2), Warning (8) """
    Error: HealthState = ...
    Healthy: HealthState = ...
    PolicyExecutionFailure: HealthState = ...
    Unknown: HealthState = ...
    value__ = ...
    Warning: HealthState = ...


class SmartAdminPolicyCategory(ICloneable): # skipped bases: <type 'object'>
    """ SmartAdminPolicyCategory(categoryName: str, healthState: HealthState, targetType: Type) """
    @property
    def CategoryName(self) -> str:
        """ Get: CategoryName(self: SmartAdminPolicyCategory) -> str """
        ...

    @property
    def HealthStateCategory(self) -> HealthState:
        """ Get: HealthStateCategory(self: SmartAdminPolicyCategory) -> HealthState """
        ...

    @property
    def Policies(self) -> Dictionary:
        """
        Get: Policies(self: SmartAdminPolicyCategory) -> Dictionary[Policy, str]
        Set: Policies(self: SmartAdminPolicyCategory) = value
        """
        ...

    @property
    def TargetType(self) -> Type:
        """ Get: TargetType(self: SmartAdminPolicyCategory) -> Type """
        ...



class SmartAdminPolicyStore: # skipped bases: <type 'object'>, <type 'object'>
    """ SmartAdminPolicyStore(connection: ServerConnection) """
    @property
    def IgnoreUserPolicy(self) -> bool:
        """
        Get: IgnoreUserPolicy(self: SmartAdminPolicyStore) -> bool
        Set: IgnoreUserPolicy(self: SmartAdminPolicyStore) = value
        """
        ...

    @property
    def PolicyCategories(self) -> List:
        """
        Get: PolicyCategories(self: SmartAdminPolicyStore) -> List[SmartAdminPolicyCategory]
        Set: PolicyCategories(self: SmartAdminPolicyStore) = value
        """
        ...


    def Evaluate(self, *__args:Array) -> Array:
        """
        Evaluate(self: SmartAdminPolicyStore, *objects: Array[SqlSmoObject]) -> Array[EvaluationResult]
        Evaluate(self: SmartAdminPolicyStore, policy: Policy, *objects: Array[SqlSmoObject]) -> Array[EvaluationResult]
        Evaluate(self: SmartAdminPolicyStore, policy: KeyValuePair[Policy, str], targetType: Type, *evaluatedObjects: Array[SqlSmoObject]) -> Array[EvaluationResult]
        """
        ...

    def LoadAllSmartAdminPolicies(self): # -> 
        """ LoadAllSmartAdminPolicies(self: SmartAdminPolicyStore) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: SmartAdminPolicyStore) """
        ...

    ErrorCategoryForSmartAdmin: str = ...
    WarningCategoryForSmartAdmin: str = ...


