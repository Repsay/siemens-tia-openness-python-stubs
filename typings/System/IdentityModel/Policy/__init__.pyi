# encoding: utf-8
# module System.IdentityModel.Policy calls itself Policy
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime

from System.Collections import IDictionary, IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IdentityModel.Claims import ClaimSet

from typing import Tuple as Tuple_


# no functions
# classes

class AuthorizationContext(IAuthorizationComponent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ClaimSets(self) -> ReadOnlyCollection:
        """ Get: ClaimSets(self: AuthorizationContext) -> ReadOnlyCollection[ClaimSet] """
        ...

    @property
    def ExpirationTime(self) -> DateTime:
        """ Get: ExpirationTime(self: AuthorizationContext) -> DateTime """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: AuthorizationContext) -> IDictionary[str, object] """
        ...


    @staticmethod
    def CreateDefaultAuthorizationContext(authorizationPolicies:IList) -> AuthorizationContext:
        """ CreateDefaultAuthorizationContext(authorizationPolicies: IList[IAuthorizationPolicy]) -> AuthorizationContext """
        ...


class EvaluationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClaimSets(self) -> ReadOnlyCollection:
        """ Get: ClaimSets(self: EvaluationContext) -> ReadOnlyCollection[ClaimSet] """
        ...

    @property
    def Generation(self) -> int:
        """ Get: Generation(self: EvaluationContext) -> int """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: EvaluationContext) -> IDictionary[str, object] """
        ...


    def AddClaimSet(self, policy:IAuthorizationPolicy, claimSet:ClaimSet): # -> 
        """ AddClaimSet(self: EvaluationContext, policy: IAuthorizationPolicy, claimSet: ClaimSet) """
        ...

    def RecordExpirationTime(self, expirationTime:DateTime): # -> 
        """ RecordExpirationTime(self: EvaluationContext, expirationTime: DateTime) """
        ...


class IAuthorizationComponent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self) -> str:
        """ Get: Id(self: IAuthorizationComponent) -> str """
        ...



class IAuthorizationPolicy(IAuthorizationComponent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Issuer(self) -> ClaimSet:
        """ Get: Issuer(self: IAuthorizationPolicy) -> ClaimSet """
        ...


    def Evaluate(self, evaluationContext:EvaluationContext, state:object) -> Tuple_[bool, object]:
        """ Evaluate(self: IAuthorizationPolicy, evaluationContext: EvaluationContext, state: object) -> (bool, object) """
        ...


