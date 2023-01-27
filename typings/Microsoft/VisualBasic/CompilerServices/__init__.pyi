# encoding: utf-8
# module Microsoft.VisualBasic.CompilerServices calls itself CompilerServices
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import CallType, CompareMethod

from System import (Array, Attribute, Byte, Char, DateTime, Decimal, Int16, 
    Int64, SByte, Single, Type, UInt16, UInt32, UInt64)

from System.Collections import IEnumerator

from System.Collections.Generic import List

from System.Globalization import CultureInfo, NumberFormatInfo

from System.Reflection import MethodBase

from System.Windows.Forms import IWin32Window

from System.Xml.Linq import XAttribute, XName, XNamespace

from typing import Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, T, field#
"""

# no functions
# classes

class BooleanType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> bool:
        """ FromObject(Value: object) -> bool """
        ...

    @staticmethod
    def FromString(Value:str) -> bool:
        """ FromString(Value: str) -> bool """
        ...


class ByteType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> Byte:
        """ FromObject(Value: object) -> Byte """
        ...

    @staticmethod
    def FromString(Value:str) -> Byte:
        """ FromString(Value: str) -> Byte """
        ...


class CharArrayType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> Array:
        """ FromObject(Value: object) -> Array[Char] """
        ...

    @staticmethod
    def FromString(Value:str) -> Array:
        """ FromString(Value: str) -> Array[Char] """
        ...


class CharType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> Char:
        """ FromObject(Value: object) -> Char """
        ...

    @staticmethod
    def FromString(Value:str) -> Char:
        """ FromString(Value: str) -> Char """
        ...


class Conversions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ChangeType(Expression:object, TargetType:Type) -> object:
        """ ChangeType(Expression: object, TargetType: Type) -> object """
        ...

    @staticmethod
    def FallbackUserDefinedConversion(Expression:object, TargetType:Type) -> object:
        """ FallbackUserDefinedConversion(Expression: object, TargetType: Type) -> object """
        ...

    @staticmethod
    def FromCharAndCount(Value:Char, Count:int) -> str:
        """ FromCharAndCount(Value: Char, Count: int) -> str """
        ...

    @staticmethod
    def FromCharArray(Value:Array) -> str:
        """ FromCharArray(Value: Array[Char]) -> str """
        ...

    @staticmethod
    def FromCharArraySubset(Value:Array, StartIndex:int, Length:int) -> str:
        """ FromCharArraySubset(Value: Array[Char], StartIndex: int, Length: int) -> str """
        ...

    @staticmethod
    def ToBoolean(Value:str) -> bool:
        """
        ToBoolean(Value: str) -> bool
        ToBoolean(Value: object) -> bool
        """
        ...

    @staticmethod
    def ToByte(Value:str) -> Byte:
        """
        ToByte(Value: str) -> Byte
        ToByte(Value: object) -> Byte
        """
        ...

    @staticmethod
    def ToChar(Value:str) -> Char:
        """
        ToChar(Value: str) -> Char
        ToChar(Value: object) -> Char
        """
        ...

    @staticmethod
    def ToCharArrayRankOne(Value:str) -> Array:
        """
        ToCharArrayRankOne(Value: str) -> Array[Char]
        ToCharArrayRankOne(Value: object) -> Array[Char]
        """
        ...

    @staticmethod
    def ToDate(Value:str) -> DateTime:
        """
        ToDate(Value: str) -> DateTime
        ToDate(Value: object) -> DateTime
        """
        ...

    @staticmethod
    def ToDecimal(Value:bool) -> Decimal:
        """
        ToDecimal(Value: bool) -> Decimal
        ToDecimal(Value: str) -> Decimal
        ToDecimal(Value: object) -> Decimal
        """
        ...

    @staticmethod
    def ToDouble(Value:str) -> float:
        """
        ToDouble(Value: str) -> float
        ToDouble(Value: object) -> float
        """
        ...

    @staticmethod
    def ToGenericParameter(Value:object): # -> T
        """ ToGenericParameter[T](Value: object) -> T """
        ...

    @staticmethod
    def ToInteger(Value:str) -> int:
        """
        ToInteger(Value: str) -> int
        ToInteger(Value: object) -> int
        """
        ...

    @staticmethod
    def ToLong(Value:str) -> Int64:
        """
        ToLong(Value: str) -> Int64
        ToLong(Value: object) -> Int64
        """
        ...

    @staticmethod
    def ToSByte(Value:str) -> SByte:
        """
        ToSByte(Value: str) -> SByte
        ToSByte(Value: object) -> SByte
        """
        ...

    @staticmethod
    def ToShort(Value:str) -> Int16:
        """
        ToShort(Value: str) -> Int16
        ToShort(Value: object) -> Int16
        """
        ...

    @staticmethod
    def ToSingle(Value:str) -> Single:
        """
        ToSingle(Value: str) -> Single
        ToSingle(Value: object) -> Single
        """
        ...

    @staticmethod
    def ToString(Value:Single = ..., NumberFormat:NumberFormatInfo = ...) -> str:
        """
        ToString(Value: bool) -> str
        ToString(Value: Byte) -> str
        ToString(Value: Char) -> str
        ToString(Value: Int16) -> str
        ToString(Value: int) -> str
        ToString(Value: UInt32) -> str
        ToString(Value: Int64) -> str
        ToString(Value: UInt64) -> str
        ToString(Value: Single) -> str
        ToString(Value: Single, NumberFormat: NumberFormatInfo) -> str
        ToString(Value: float) -> str
        ToString(Value: float, NumberFormat: NumberFormatInfo) -> str
        ToString(Value: DateTime) -> str
        ToString(Value: Decimal) -> str
        ToString(Value: Decimal, NumberFormat: NumberFormatInfo) -> str
        ToString(Value: object) -> str
        """
        ...

    @staticmethod
    def ToUInteger(Value:str) -> UInt32:
        """
        ToUInteger(Value: str) -> UInt32
        ToUInteger(Value: object) -> UInt32
        """
        ...

    @staticmethod
    def ToULong(Value:str) -> UInt64:
        """
        ToULong(Value: str) -> UInt64
        ToULong(Value: object) -> UInt64
        """
        ...

    @staticmethod
    def ToUShort(Value:str) -> UInt16:
        """
        ToUShort(Value: str) -> UInt16
        ToUShort(Value: object) -> UInt16
        """
        ...


class DateType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> DateTime:
        """ FromObject(Value: object) -> DateTime """
        ...

    @staticmethod
    def FromString(Value:str, culture:CultureInfo = ...) -> DateTime:
        """
        FromString(Value: str) -> DateTime
        FromString(Value: str, culture: CultureInfo) -> DateTime
        """
        ...


class DecimalType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromBoolean(Value:bool) -> Decimal:
        """ FromBoolean(Value: bool) -> Decimal """
        ...

    @staticmethod
    def FromObject(Value:object, NumberFormat:NumberFormatInfo = ...) -> Decimal:
        """
        FromObject(Value: object) -> Decimal
        FromObject(Value: object, NumberFormat: NumberFormatInfo) -> Decimal
        """
        ...

    @staticmethod
    def FromString(Value:str, NumberFormat:NumberFormatInfo = ...) -> Decimal:
        """
        FromString(Value: str) -> Decimal
        FromString(Value: str, NumberFormat: NumberFormatInfo) -> Decimal
        """
        ...

    @staticmethod
    def Parse(Value:str, NumberFormat:NumberFormatInfo) -> Decimal:
        """ Parse(Value: str, NumberFormat: NumberFormatInfo) -> Decimal """
        ...


class DesignerGeneratedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DesignerGeneratedAttribute() """
    pass

class DoubleType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object, NumberFormat:NumberFormatInfo = ...) -> float:
        """
        FromObject(Value: object) -> float
        FromObject(Value: object, NumberFormat: NumberFormatInfo) -> float
        """
        ...

    @staticmethod
    def FromString(Value:str, NumberFormat:NumberFormatInfo = ...) -> float:
        """
        FromString(Value: str) -> float
        FromString(Value: str, NumberFormat: NumberFormatInfo) -> float
        """
        ...

    @staticmethod
    def Parse(Value:str, NumberFormat:NumberFormatInfo = ...) -> float:
        """
        Parse(Value: str) -> float
        Parse(Value: str, NumberFormat: NumberFormatInfo) -> float
        """
        ...


class ExceptionUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class FlowControl: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckForSyncLockOnValueType(obj:object): # -> 
        """ CheckForSyncLockOnValueType(obj: object) """
        ...

    @staticmethod
    def ForEachInArr(ary:Array) -> IEnumerator:
        """ ForEachInArr(ary: Array) -> IEnumerator """
        ...

    @staticmethod
    def ForEachInObj(obj:object) -> IEnumerator:
        """ ForEachInObj(obj: object) -> IEnumerator """
        ...

    @staticmethod
    def ForEachNextObj(obj:object, enumerator:IEnumerator) -> Tuple_[bool, object]:
        """ ForEachNextObj(obj: object, enumerator: IEnumerator) -> (bool, object) """
        ...

    @staticmethod
    def ForLoopInitObj(Counter:object, Start:object, Limit:object, StepValue:object, LoopForResult:object, CounterResult:object) -> Tuple_[bool, object, object]:
        """ ForLoopInitObj(Counter: object, Start: object, Limit: object, StepValue: object, LoopForResult: object, CounterResult: object) -> (bool, object, object) """
        ...

    @staticmethod
    def ForNextCheckDec(count:Decimal, limit:Decimal, StepValue:Decimal) -> bool:
        """ ForNextCheckDec(count: Decimal, limit: Decimal, StepValue: Decimal) -> bool """
        ...

    @staticmethod
    def ForNextCheckObj(Counter:object, LoopObj:object, CounterResult:object) -> Tuple_[bool, object]:
        """ ForNextCheckObj(Counter: object, LoopObj: object, CounterResult: object) -> (bool, object) """
        ...

    @staticmethod
    def ForNextCheckR4(count:Single, limit:Single, StepValue:Single) -> bool:
        """ ForNextCheckR4(count: Single, limit: Single, StepValue: Single) -> bool """
        ...

    @staticmethod
    def ForNextCheckR8(count:float, limit:float, StepValue:float) -> bool:
        """ ForNextCheckR8(count: float, limit: float, StepValue: float) -> bool """
        ...


class HostServices: # skipped bases: <type 'object'>, <type 'object'>
    """ HostServices() """
    @property
    def VBHost(self) -> IVbHost:
        """
        Get: VBHost() -> IVbHost
        Set: VBHost() = value
        """
        ...



class IncompleteInitialization(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    IncompleteInitialization(message: str)
    IncompleteInitialization(message: str, innerException: Exception)
    IncompleteInitialization()
    """
    SerializeObjectState = ...


class IntegerType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> int:
        """ FromObject(Value: object) -> int """
        ...

    @staticmethod
    def FromString(Value:str) -> int:
        """ FromString(Value: str) -> int """
        ...


class InternalErrorException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InternalErrorException(message: str)
    InternalErrorException(message: str, innerException: Exception)
    InternalErrorException()
    """
    SerializeObjectState = ...


class InternalXmlHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateAttribute(name:XName, value:object) -> XAttribute:
        """ CreateAttribute(name: XName, value: object) -> XAttribute """
        ...

    @staticmethod
    def CreateNamespaceAttribute(name:XName, ns:XNamespace) -> XAttribute:
        """ CreateNamespaceAttribute(name: XName, ns: XNamespace) -> XAttribute """
        ...

    @staticmethod
    def RemoveNamespaceAttributes(inScopePrefixes:Array, inScopeNs:Array, attributes:List, *__args:object) -> object:
        """
        RemoveNamespaceAttributes(inScopePrefixes: Array[str], inScopeNs: Array[XNamespace], attributes: List[XAttribute], obj: object) -> object
        RemoveNamespaceAttributes(inScopePrefixes: Array[str], inScopeNs: Array[XNamespace], attributes: List[XAttribute], obj: IEnumerable) -> IEnumerable
        RemoveNamespaceAttributes(inScopePrefixes: Array[str], inScopeNs: Array[XNamespace], attributes: List[XAttribute], e: XElement) -> XElement
        """
        ...


class IVbHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetParentWindow(self) -> IWin32Window:
        """ GetParentWindow(self: IVbHost) -> IWin32Window """
        ...

    def GetWindowTitle(self) -> str:
        """ GetWindowTitle(self: IVbHost) -> str """
        ...


class LateBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def LateCall(o:object, objType:Type, name:str, args:Array, paramnames:Array, CopyBack:Array): # -> 
        """ LateCall(o: object, objType: Type, name: str, args: Array[object], paramnames: Array[str], CopyBack: Array[bool]) """
        ...

    @staticmethod
    def LateGet(o:object, objType:Type, name:str, args:Array, paramnames:Array, CopyBack:Array) -> object:
        """ LateGet(o: object, objType: Type, name: str, args: Array[object], paramnames: Array[str], CopyBack: Array[bool]) -> object """
        ...

    @staticmethod
    def LateIndexGet(o:object, args:Array, paramnames:Array) -> object:
        """ LateIndexGet(o: object, args: Array[object], paramnames: Array[str]) -> object """
        ...

    @staticmethod
    def LateIndexSet(o:object, args:Array, paramnames:Array): # -> 
        """ LateIndexSet(o: object, args: Array[object], paramnames: Array[str]) """
        ...

    @staticmethod
    def LateIndexSetComplex(o:object, args:Array, paramnames:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ LateIndexSetComplex(o: object, args: Array[object], paramnames: Array[str], OptimisticSet: bool, RValueBase: bool) """
        ...

    @staticmethod
    def LateSet(o:object, objType:Type, name:str, args:Array, paramnames:Array): # -> 
        """ LateSet(o: object, objType: Type, name: str, args: Array[object], paramnames: Array[str]) """
        ...

    @staticmethod
    def LateSetComplex(o:object, objType:Type, name:str, args:Array, paramnames:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ LateSetComplex(o: object, objType: Type, name: str, args: Array[object], paramnames: Array[str], OptimisticSet: bool, RValueBase: bool) """
        ...


class LikeOperator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def LikeObject(Source:object, Pattern:object, CompareOption:CompareMethod) -> object:
        """ LikeObject(Source: object, Pattern: object, CompareOption: CompareMethod) -> object """
        ...

    @staticmethod
    def LikeString(Source:str, Pattern:str, CompareOption:CompareMethod) -> bool:
        """ LikeString(Source: str, Pattern: str, CompareOption: CompareMethod) -> bool """
        ...


class LongType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> Int64:
        """ FromObject(Value: object) -> Int64 """
        ...

    @staticmethod
    def FromString(Value:str) -> Int64:
        """ FromString(Value: str) -> Int64 """
        ...


class NewLateBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FallbackCall(Instance:object, MemberName:str, Arguments:Array, ArgumentNames:Array, IgnoreReturn:bool) -> object:
        """ FallbackCall(Instance: object, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], IgnoreReturn: bool) -> object """
        ...

    @staticmethod
    def FallbackGet(Instance:object, MemberName:str, Arguments:Array, ArgumentNames:Array) -> object:
        """ FallbackGet(Instance: object, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str]) -> object """
        ...

    @staticmethod
    def FallbackIndexSet(Instance:object, Arguments:Array, ArgumentNames:Array): # -> 
        """ FallbackIndexSet(Instance: object, Arguments: Array[object], ArgumentNames: Array[str]) """
        ...

    @staticmethod
    def FallbackIndexSetComplex(Instance:object, Arguments:Array, ArgumentNames:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ FallbackIndexSetComplex(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], OptimisticSet: bool, RValueBase: bool) """
        ...

    @staticmethod
    def FallbackInvokeDefault1(Instance:object, Arguments:Array, ArgumentNames:Array, ReportErrors:bool) -> object:
        """ FallbackInvokeDefault1(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], ReportErrors: bool) -> object """
        ...

    @staticmethod
    def FallbackInvokeDefault2(Instance:object, Arguments:Array, ArgumentNames:Array, ReportErrors:bool) -> object:
        """ FallbackInvokeDefault2(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], ReportErrors: bool) -> object """
        ...

    @staticmethod
    def FallbackSet(Instance:object, MemberName:str, Arguments:Array): # -> 
        """ FallbackSet(Instance: object, MemberName: str, Arguments: Array[object]) """
        ...

    @staticmethod
    def FallbackSetComplex(Instance:object, MemberName:str, Arguments:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ FallbackSetComplex(Instance: object, MemberName: str, Arguments: Array[object], OptimisticSet: bool, RValueBase: bool) """
        ...

    @staticmethod
    def LateCall(Instance:object, Type:Type, MemberName:str, Arguments:Array, ArgumentNames:Array, TypeArguments:Array, CopyBack:Array, IgnoreReturn:bool) -> object:
        """ LateCall(Instance: object, Type: Type, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], TypeArguments: Array[Type], CopyBack: Array[bool], IgnoreReturn: bool) -> object """
        ...

    @staticmethod
    def LateCallInvokeDefault(Instance:object, Arguments:Array, ArgumentNames:Array, ReportErrors:bool) -> object:
        """ LateCallInvokeDefault(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], ReportErrors: bool) -> object """
        ...

    @staticmethod
    def LateCanEvaluate(instance:object, type:Type, memberName:str, arguments:Array, allowFunctionEvaluation:bool, allowPropertyEvaluation:bool) -> bool:
        """ LateCanEvaluate(instance: object, type: Type, memberName: str, arguments: Array[object], allowFunctionEvaluation: bool, allowPropertyEvaluation: bool) -> bool """
        ...

    @staticmethod
    def LateGet(Instance:object, Type:Type, MemberName:str, Arguments:Array, ArgumentNames:Array, TypeArguments:Array, CopyBack:Array) -> object:
        """ LateGet(Instance: object, Type: Type, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], TypeArguments: Array[Type], CopyBack: Array[bool]) -> object """
        ...

    @staticmethod
    def LateGetInvokeDefault(Instance:object, Arguments:Array, ArgumentNames:Array, ReportErrors:bool) -> object:
        """ LateGetInvokeDefault(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], ReportErrors: bool) -> object """
        ...

    @staticmethod
    def LateIndexGet(Instance:object, Arguments:Array, ArgumentNames:Array) -> object:
        """ LateIndexGet(Instance: object, Arguments: Array[object], ArgumentNames: Array[str]) -> object """
        ...

    @staticmethod
    def LateIndexSet(Instance:object, Arguments:Array, ArgumentNames:Array): # -> 
        """ LateIndexSet(Instance: object, Arguments: Array[object], ArgumentNames: Array[str]) """
        ...

    @staticmethod
    def LateIndexSetComplex(Instance:object, Arguments:Array, ArgumentNames:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ LateIndexSetComplex(Instance: object, Arguments: Array[object], ArgumentNames: Array[str], OptimisticSet: bool, RValueBase: bool) """
        ...

    @staticmethod
    def LateSet(Instance:object, Type:Type, MemberName:str, Arguments:Array, ArgumentNames:Array, TypeArguments:Array, OptimisticSet:bool = ..., RValueBase:bool = ..., CallType:CallType = ...): # -> 
        """ LateSet(Instance: object, Type: Type, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], TypeArguments: Array[Type])LateSet(Instance: object, Type: Type, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], TypeArguments: Array[Type], OptimisticSet: bool, RValueBase: bool, CallType: CallType) """
        ...

    @staticmethod
    def LateSetComplex(Instance:object, Type:Type, MemberName:str, Arguments:Array, ArgumentNames:Array, TypeArguments:Array, OptimisticSet:bool, RValueBase:bool): # -> 
        """ LateSetComplex(Instance: object, Type: Type, MemberName: str, Arguments: Array[object], ArgumentNames: Array[str], TypeArguments: Array[Type], OptimisticSet: bool, RValueBase: bool) """
        ...


class ObjectFlowControl: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckForSyncLockOnValueType(Expression:object): # -> 
        """ CheckForSyncLockOnValueType(Expression: object) """
        ...

    def ForLoopControl(self, *args): #cannot find CLR method
        """ no doc """
        ...



class ObjectType: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectType() """
    @staticmethod
    def AddObj(o1:object, o2:object) -> object:
        """ AddObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def BitAndObj(obj1:object, obj2:object) -> object:
        """ BitAndObj(obj1: object, obj2: object) -> object """
        ...

    @staticmethod
    def BitOrObj(obj1:object, obj2:object) -> object:
        """ BitOrObj(obj1: object, obj2: object) -> object """
        ...

    @staticmethod
    def BitXorObj(obj1:object, obj2:object) -> object:
        """ BitXorObj(obj1: object, obj2: object) -> object """
        ...

    @staticmethod
    def DivObj(o1:object, o2:object) -> object:
        """ DivObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def GetObjectValuePrimitive(o:object) -> object:
        """ GetObjectValuePrimitive(o: object) -> object """
        ...

    @staticmethod
    def IDivObj(o1:object, o2:object) -> object:
        """ IDivObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def LikeObj(vLeft:object, vRight:object, CompareOption:CompareMethod) -> bool:
        """ LikeObj(vLeft: object, vRight: object, CompareOption: CompareMethod) -> bool """
        ...

    @staticmethod
    def ModObj(o1:object, o2:object) -> object:
        """ ModObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def MulObj(o1:object, o2:object) -> object:
        """ MulObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def NegObj(obj:object) -> object:
        """ NegObj(obj: object) -> object """
        ...

    @staticmethod
    def NotObj(obj:object) -> object:
        """ NotObj(obj: object) -> object """
        ...

    @staticmethod
    def ObjTst(o1:object, o2:object, TextCompare:bool) -> int:
        """ ObjTst(o1: object, o2: object, TextCompare: bool) -> int """
        ...

    @staticmethod
    def PlusObj(obj:object) -> object:
        """ PlusObj(obj: object) -> object """
        ...

    @staticmethod
    def PowObj(obj1:object, obj2:object) -> object:
        """ PowObj(obj1: object, obj2: object) -> object """
        ...

    @staticmethod
    def ShiftLeftObj(o1:object, amount:int) -> object:
        """ ShiftLeftObj(o1: object, amount: int) -> object """
        ...

    @staticmethod
    def ShiftRightObj(o1:object, amount:int) -> object:
        """ ShiftRightObj(o1: object, amount: int) -> object """
        ...

    @staticmethod
    def StrCatObj(vLeft:object, vRight:object) -> object:
        """ StrCatObj(vLeft: object, vRight: object) -> object """
        ...

    @staticmethod
    def SubObj(o1:object, o2:object) -> object:
        """ SubObj(o1: object, o2: object) -> object """
        ...

    @staticmethod
    def XorObj(obj1:object, obj2:object) -> object:
        """ XorObj(obj1: object, obj2: object) -> object """
        ...


class Operators: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddObject(Left:object, Right:object) -> object:
        """ AddObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def AndObject(Left:object, Right:object) -> object:
        """ AndObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def CompareObject(Left:object, Right:object, TextCompare:bool) -> int:
        """ CompareObject(Left: object, Right: object, TextCompare: bool) -> int """
        ...

    @staticmethod
    def CompareObjectEqual(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectEqual(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareObjectGreater(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectGreater(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareObjectGreaterEqual(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectGreaterEqual(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareObjectLess(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectLess(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareObjectLessEqual(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectLessEqual(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareObjectNotEqual(Left:object, Right:object, TextCompare:bool) -> object:
        """ CompareObjectNotEqual(Left: object, Right: object, TextCompare: bool) -> object """
        ...

    @staticmethod
    def CompareString(Left:str, Right:str, TextCompare:bool) -> int:
        """ CompareString(Left: str, Right: str, TextCompare: bool) -> int """
        ...

    @staticmethod
    def ConcatenateObject(Left:object, Right:object) -> object:
        """ ConcatenateObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def ConditionalCompareObjectEqual(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectEqual(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def ConditionalCompareObjectGreater(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectGreater(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def ConditionalCompareObjectGreaterEqual(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectGreaterEqual(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def ConditionalCompareObjectLess(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectLess(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def ConditionalCompareObjectLessEqual(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectLessEqual(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def ConditionalCompareObjectNotEqual(Left:object, Right:object, TextCompare:bool) -> bool:
        """ ConditionalCompareObjectNotEqual(Left: object, Right: object, TextCompare: bool) -> bool """
        ...

    @staticmethod
    def DivideObject(Left:object, Right:object) -> object:
        """ DivideObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def ExponentObject(Left:object, Right:object) -> object:
        """ ExponentObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def FallbackInvokeUserDefinedOperator(vbOp:object, Arguments:Array) -> object:
        """ FallbackInvokeUserDefinedOperator(vbOp: object, Arguments: Array[object]) -> object """
        ...

    @staticmethod
    def IntDivideObject(Left:object, Right:object) -> object:
        """ IntDivideObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def LeftShiftObject(Operand:object, Amount:object) -> object:
        """ LeftShiftObject(Operand: object, Amount: object) -> object """
        ...

    @staticmethod
    def LikeObject(Source:object, Pattern:object, CompareOption:CompareMethod) -> object:
        """ LikeObject(Source: object, Pattern: object, CompareOption: CompareMethod) -> object """
        ...

    @staticmethod
    def LikeString(Source:str, Pattern:str, CompareOption:CompareMethod) -> bool:
        """ LikeString(Source: str, Pattern: str, CompareOption: CompareMethod) -> bool """
        ...

    @staticmethod
    def ModObject(Left:object, Right:object) -> object:
        """ ModObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def MultiplyObject(Left:object, Right:object) -> object:
        """ MultiplyObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def NegateObject(Operand:object) -> object:
        """ NegateObject(Operand: object) -> object """
        ...

    @staticmethod
    def NotObject(Operand:object) -> object:
        """ NotObject(Operand: object) -> object """
        ...

    @staticmethod
    def OrObject(Left:object, Right:object) -> object:
        """ OrObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def PlusObject(Operand:object) -> object:
        """ PlusObject(Operand: object) -> object """
        ...

    @staticmethod
    def RightShiftObject(Operand:object, Amount:object) -> object:
        """ RightShiftObject(Operand: object, Amount: object) -> object """
        ...

    @staticmethod
    def SubtractObject(Left:object, Right:object) -> object:
        """ SubtractObject(Left: object, Right: object) -> object """
        ...

    @staticmethod
    def XorObject(Left:object, Right:object) -> object:
        """ XorObject(Left: object, Right: object) -> object """
        ...


class OptionCompareAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OptionCompareAttribute() """
    pass

class OptionTextAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OptionTextAttribute() """
    pass

class ProjectData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ClearProjectError(): # -> 
        """ ClearProjectError() """
        ...

    @staticmethod
    def CreateProjectError(hr:int) -> Exception:
        """ CreateProjectError(hr: int) -> Exception """
        ...

    @staticmethod
    def EndApp(): # -> 
        """ EndApp() """
        ...

    @staticmethod
    def SetProjectError(ex:Exception, lErl:int = ...): # -> 
        """ SetProjectError(ex: Exception, lErl: int)SetProjectError(ex: Exception) """
        ...


class ShortType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object) -> Int16:
        """ FromObject(Value: object) -> Int16 """
        ...

    @staticmethod
    def FromString(Value:str) -> Int16:
        """ FromString(Value: str) -> Int16 """
        ...


class SingleType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromObject(Value:object, NumberFormat:NumberFormatInfo = ...) -> Single:
        """
        FromObject(Value: object) -> Single
        FromObject(Value: object, NumberFormat: NumberFormatInfo) -> Single
        """
        ...

    @staticmethod
    def FromString(Value:str, NumberFormat:NumberFormatInfo = ...) -> Single:
        """
        FromString(Value: str) -> Single
        FromString(Value: str, NumberFormat: NumberFormatInfo) -> Single
        """
        ...


class StandardModuleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StandardModuleAttribute() """
    pass

class StaticLocalInitFlag: # skipped bases: <type 'object'>, <type 'object'>
    """ StaticLocalInitFlag() """
    State = ...


class StringType: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromBoolean(Value:bool) -> str:
        """ FromBoolean(Value: bool) -> str """
        ...

    @staticmethod
    def FromByte(Value:Byte) -> str:
        """ FromByte(Value: Byte) -> str """
        ...

    @staticmethod
    def FromChar(Value:Char) -> str:
        """ FromChar(Value: Char) -> str """
        ...

    @staticmethod
    def FromDate(Value:DateTime) -> str:
        """ FromDate(Value: DateTime) -> str """
        ...

    @staticmethod
    def FromDecimal(Value:Decimal, NumberFormat:NumberFormatInfo = ...) -> str:
        """
        FromDecimal(Value: Decimal) -> str
        FromDecimal(Value: Decimal, NumberFormat: NumberFormatInfo) -> str
        """
        ...

    @staticmethod
    def FromDouble(Value:float, NumberFormat:NumberFormatInfo = ...) -> str:
        """
        FromDouble(Value: float) -> str
        FromDouble(Value: float, NumberFormat: NumberFormatInfo) -> str
        """
        ...

    @staticmethod
    def FromInteger(Value:int) -> str:
        """ FromInteger(Value: int) -> str """
        ...

    @staticmethod
    def FromLong(Value:Int64) -> str:
        """ FromLong(Value: Int64) -> str """
        ...

    @staticmethod
    def FromObject(Value:object) -> str:
        """ FromObject(Value: object) -> str """
        ...

    @staticmethod
    def FromShort(Value:Int16) -> str:
        """ FromShort(Value: Int16) -> str """
        ...

    @staticmethod
    def FromSingle(Value:Single, NumberFormat:NumberFormatInfo = ...) -> str:
        """
        FromSingle(Value: Single) -> str
        FromSingle(Value: Single, NumberFormat: NumberFormatInfo) -> str
        """
        ...

    @staticmethod
    def MidStmtStr(sDest:str, StartPosition:int, MaxInsertLength:int, sInsert:str) -> str:
        """ MidStmtStr(sDest: str, StartPosition: int, MaxInsertLength: int, sInsert: str) -> str """
        ...

    @staticmethod
    def StrCmp(sLeft:str, sRight:str, TextCompare:bool) -> int:
        """ StrCmp(sLeft: str, sRight: str, TextCompare: bool) -> int """
        ...

    @staticmethod
    def StrLike(Source:str, Pattern:str, CompareOption:CompareMethod) -> bool:
        """ StrLike(Source: str, Pattern: str, CompareOption: CompareMethod) -> bool """
        ...

    @staticmethod
    def StrLikeBinary(Source:str, Pattern:str) -> bool:
        """ StrLikeBinary(Source: str, Pattern: str) -> bool """
        ...

    @staticmethod
    def StrLikeText(Source:str, Pattern:str) -> bool:
        """ StrLikeText(Source: str, Pattern: str) -> bool """
        ...


class Utils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CopyArray(arySrc:Array, aryDest:Array) -> Array:
        """ CopyArray(arySrc: Array, aryDest: Array) -> Array """
        ...

    @staticmethod
    def GetResourceString(ResourceKey:str, Args:Array) -> str:
        """ GetResourceString(ResourceKey: str, *Args: Array[str]) -> str """
        ...

    @staticmethod
    def MethodToString(Method:MethodBase) -> str:
        """ MethodToString(Method: MethodBase) -> str """
        ...

    @staticmethod
    def SetCultureInfo(Culture:CultureInfo) -> object:
        """ SetCultureInfo(Culture: CultureInfo) -> object """
        ...

    @staticmethod
    def ThrowException(hr:int): # -> 
        """ ThrowException(hr: int) """
        ...


class Versioned: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CallByName(Instance:object, MethodName:str, UseCallType:CallType, Arguments:Array) -> object:
        """ CallByName(Instance: object, MethodName: str, UseCallType: CallType, *Arguments: Array[object]) -> object """
        ...

    @staticmethod
    def IsNumeric(Expression:object) -> bool:
        """ IsNumeric(Expression: object) -> bool """
        ...

    @staticmethod
    def SystemTypeName(VbName:str) -> str:
        """ SystemTypeName(VbName: str) -> str """
        ...

    @staticmethod
    def TypeName(Expression:object) -> str:
        """ TypeName(Expression: object) -> str """
        ...

    @staticmethod
    def VbTypeName(SystemName:str) -> str:
        """ VbTypeName(SystemName: str) -> str """
        ...


