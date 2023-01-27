# encoding: utf-8
# module Microsoft.Scripting.Debugging.CompilerServices calls itself CompilerServices
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import IDictionary, IList

from System.Linq.Expressions import Expression, LambdaExpression


# no functions
# classes

class DebugContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Mode(self) -> int:
        """ Get: Mode(self: DebugContext) -> int """
        ...


    @staticmethod
    def CreateInstance() -> DebugContext:
        """ CreateInstance() -> DebugContext """
        ...

    def ResetSourceFile(self, sourceFileName:str): # -> 
        """ ResetSourceFile(self: DebugContext, sourceFileName: str) """
        ...

    def TransformLambda(self, lambda_:LambdaExpression, lambdaInfo:DebugLambdaInfo = ...) -> LambdaExpression:
        """
        TransformLambda(self: DebugContext, lambda: LambdaExpression, lambdaInfo: DebugLambdaInfo) -> LambdaExpression
        TransformLambda(self: DebugContext, lambda: LambdaExpression) -> LambdaExpression
        """
        ...


class DebugLambdaInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ DebugLambdaInfo(compilerSupport: IDebugCompilerSupport, lambdaAlias: str, optimizeForLeafFrames: bool, hiddenVariables: IList[ParameterExpression], variableAliases: IDictionary[ParameterExpression, str], customPayload: object) """
    @property
    def CompilerSupport(self) -> IDebugCompilerSupport:
        """ Get: CompilerSupport(self: DebugLambdaInfo) -> IDebugCompilerSupport """
        ...

    @property
    def CustomPayload(self) -> object:
        """ Get: CustomPayload(self: DebugLambdaInfo) -> object """
        ...

    @property
    def HiddenVariables(self) -> IList:
        """ Get: HiddenVariables(self: DebugLambdaInfo) -> IList[ParameterExpression] """
        ...

    @property
    def LambdaAlias(self) -> str:
        """ Get: LambdaAlias(self: DebugLambdaInfo) -> str """
        ...

    @property
    def OptimizeForLeafFrames(self) -> bool:
        """ Get: OptimizeForLeafFrames(self: DebugLambdaInfo) -> bool """
        ...

    @property
    def VariableAliases(self) -> IDictionary:
        """ Get: VariableAliases(self: DebugLambdaInfo) -> IDictionary[ParameterExpression, str] """
        ...



class IDebugCompilerSupport: # skipped bases: <type 'object'>
    """ no doc """
    def DoesExpressionNeedReduction(self, expression:Expression) -> bool:
        """ DoesExpressionNeedReduction(self: IDebugCompilerSupport, expression: Expression) -> bool """
        ...

    def IsCallToDebuggableLambda(self, expression:Expression) -> bool:
        """ IsCallToDebuggableLambda(self: IDebugCompilerSupport, expression: Expression) -> bool """
        ...

    def QueueExpressionForReduction(self, expression:Expression) -> Expression:
        """ QueueExpressionForReduction(self: IDebugCompilerSupport, expression: Expression) -> Expression """
        ...


