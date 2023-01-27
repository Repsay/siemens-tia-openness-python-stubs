# encoding: utf-8
# module Microsoft.CSharp.RuntimeBinder calls itself RuntimeBinder
# from Microsoft.CSharp, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Type

from System.Collections import IEnumerable

from System.Linq.Expressions import ExpressionType

from System.Runtime.CompilerServices import CallSiteBinder

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Binder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BinaryOperation(flags:CSharpBinderFlags, operation:ExpressionType, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ BinaryOperation(flags: CSharpBinderFlags, operation: ExpressionType, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def Convert(flags:CSharpBinderFlags, type:Type, context:Type) -> CallSiteBinder:
        """ Convert(flags: CSharpBinderFlags, type: Type, context: Type) -> CallSiteBinder """
        ...

    @staticmethod
    def GetIndex(flags:CSharpBinderFlags, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ GetIndex(flags: CSharpBinderFlags, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def GetMember(flags:CSharpBinderFlags, name:str, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ GetMember(flags: CSharpBinderFlags, name: str, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def Invoke(flags:CSharpBinderFlags, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ Invoke(flags: CSharpBinderFlags, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def InvokeConstructor(flags:CSharpBinderFlags, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ InvokeConstructor(flags: CSharpBinderFlags, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def InvokeMember(flags:CSharpBinderFlags, name:str, typeArguments:IEnumerable, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ InvokeMember(flags: CSharpBinderFlags, name: str, typeArguments: IEnumerable[Type], context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def IsEvent(flags:CSharpBinderFlags, name:str, context:Type) -> CallSiteBinder:
        """ IsEvent(flags: CSharpBinderFlags, name: str, context: Type) -> CallSiteBinder """
        ...

    @staticmethod
    def SetIndex(flags:CSharpBinderFlags, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ SetIndex(flags: CSharpBinderFlags, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def SetMember(flags:CSharpBinderFlags, name:str, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ SetMember(flags: CSharpBinderFlags, name: str, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    @staticmethod
    def UnaryOperation(flags:CSharpBinderFlags, operation:ExpressionType, context:Type, argumentInfo:IEnumerable) -> CallSiteBinder:
        """ UnaryOperation(flags: CSharpBinderFlags, operation: ExpressionType, context: Type, argumentInfo: IEnumerable[CSharpArgumentInfo]) -> CallSiteBinder """
        ...

    __all__: list = ...


class CSharpArgumentInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(flags:CSharpArgumentInfoFlags, name:str) -> CSharpArgumentInfo:
        """ Create(flags: CSharpArgumentInfoFlags, name: str) -> CSharpArgumentInfo """
        ...


class CSharpArgumentInfoFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CSharpArgumentInfoFlags, values: Constant (2), IsOut (16), IsRef (8), IsStaticType (32), NamedArgument (4), None (0), UseCompileTimeType (1) """
    Constant: CSharpArgumentInfoFlags = ...
    IsOut: CSharpArgumentInfoFlags = ...
    IsRef: CSharpArgumentInfoFlags = ...
    IsStaticType: CSharpArgumentInfoFlags = ...
    NamedArgument: CSharpArgumentInfoFlags = ...
    UseCompileTimeType: CSharpArgumentInfoFlags = ...
    value__ = ...


class CSharpBinderFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CSharpBinderFlags, values: BinaryOperationLogical (8), CheckedContext (1), ConvertArrayIndex (32), ConvertExplicit (16), InvokeSimpleName (2), InvokeSpecialName (4), None (0), ResultDiscarded (256), ResultIndexed (64), ValueFromCompoundAssignment (128) """
    BinaryOperationLogical: CSharpBinderFlags = ...
    CheckedContext: CSharpBinderFlags = ...
    ConvertArrayIndex: CSharpBinderFlags = ...
    ConvertExplicit: CSharpBinderFlags = ...
    InvokeSimpleName: CSharpBinderFlags = ...
    InvokeSpecialName: CSharpBinderFlags = ...
    ResultDiscarded: CSharpBinderFlags = ...
    ResultIndexed: CSharpBinderFlags = ...
    ValueFromCompoundAssignment: CSharpBinderFlags = ...
    value__ = ...


class RuntimeBinderException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuntimeBinderException()
    RuntimeBinderException(message: str)
    RuntimeBinderException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RuntimeBinderInternalCompilerException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RuntimeBinderInternalCompilerException()
    RuntimeBinderInternalCompilerException(message: str)
    RuntimeBinderInternalCompilerException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


