# encoding: utf-8
# module Microsoft.Scripting.Utils calls itself Utils
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1, Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, ArgumentNullException, 
    ArgumentOutOfRangeException, Array, Char, Comparison, DateTime, Delegate, 
    Enum, IEquatable, IFormatProvider, Int64, MidpointRounding, Predicate, 
    Random, Type, TypeCode, UInt32, UInt64)

from System.Collections import (ICollection, IComparer, IDictionary, 
    IDictionaryEnumerator, IEnumerable, IEnumerator, IEqualityComparer, IList)

from System.Collections.Generic import Dictionary, KeyValuePair, List

from System.Dynamic import DynamicMetaObject, DynamicMetaObjectBinder

from System.Globalization import CultureInfo, DateTimeStyles, NumberStyles

from System.IO import Stream, TextReader

from System.Linq.Expressions import Expression

from System.Reflection import (Assembly, AssemblyName, BindingFlags, 
    EventInfo, FieldInfo, GenericParameterAttributes, MemberInfo, 
    MethodAttributes, MethodBase, MethodInfo, ParameterInfo, PropertyInfo)

from System.Reflection.Emit import (AssemblyBuilder, AssemblyBuilderAccess, 
    MethodBuilder, TypeBuilder)

from System.Text import Encoding, StringBuilder

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (Array[Type], 
    Array[object], Array[str], Func, RuntimeType, SourceCodeKind, StorageInfo, 
    T, TKey, TValue, complex, field#, long)
"""

# no functions
# classes

class ArrayUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Append(array:Array, item) -> Array: # Not found arg types: {'item': 'T'}
        """ Append[T](array: Array[T], item: T) -> Array[T] """
        ...

    @staticmethod
    def AppendRange(array:Array, items:IList, additionalItemCount:int = ...) -> Array:
        """
        AppendRange[T](array: Array[T], items: IList[T]) -> Array[T]
        AppendRange[T](array: Array[T], items: IList[T], additionalItemCount: int) -> Array[T]
        """
        ...

    @staticmethod
    def Concatenate(array1:Array, array2:Array) -> Array:
        """ Concatenate[T](array1: Array[T], array2: Array[T]) -> Array[T] """
        ...

    @staticmethod
    def ConvertAll(input:Array, conv) -> Array: # Not found arg types: {'conv': 'Func'}
        """ ConvertAll[(TInput, TOutput)](input: Array[TInput], conv: Func[TInput, TOutput]) -> Array[TOutput] """
        ...

    @staticmethod
    def Copy(array:Array) -> Array:
        """ Copy[T](array: Array[T]) -> Array[T] """
        ...

    @staticmethod
    def GetValueHashCode(array:Array, start:int = ..., count:int = ...) -> int:
        """
        GetValueHashCode[T](array: Array[T]) -> int
        GetValueHashCode[T](array: Array[T], start: int, count: int) -> int
        """
        ...

    @staticmethod
    def Insert(*__args) -> Array:
        """
        Insert[T](item: T, list: IList[T]) -> Array[T]
        Insert[T](item1: T, item2: T, list: IList[T]) -> Array[T]
        Insert[T](item: T, array: Array[T]) -> Array[T]
        Insert[T](item1: T, item2: T, array: Array[T]) -> Array[T]
        """
        ...

    @staticmethod
    def InsertAt(*__args) -> Array:
        """
        InsertAt[T](list: IList[T], index: int, *items: Array[T]) -> Array[T]
        InsertAt[T](array: Array[T], index: int, *items: Array[T]) -> Array[T]
        """
        ...

    @staticmethod
    def MakeArray(*__args:ICollection) -> Array:
        """
        MakeArray[T](list: ICollection[T]) -> Array[T]
        MakeArray[T](elements: ICollection[T], reservedSlotsBefore: int, reservedSlotsAfter: int) -> Array[T]
        """
        ...

    @staticmethod
    def PrintTable(output:StringBuilder, table:Array): # -> 
        """ PrintTable(output: StringBuilder, table: Array[str]) """
        ...

    @staticmethod
    def RemoveAt(*__args) -> Array:
        """
        RemoveAt[T](list: IList[T], indexToRemove: int) -> Array[T]
        RemoveAt[T](array: Array[T], indexToRemove: int) -> Array[T]
        """
        ...

    @staticmethod
    def RemoveFirst(*__args:IList) -> Array:
        """
        RemoveFirst[T](list: IList[T]) -> Array[T]
        RemoveFirst[T](array: Array[T]) -> Array[T]
        """
        ...

    @staticmethod
    def RemoveLast(array:Array) -> Array:
        """ RemoveLast[T](array: Array[T]) -> Array[T] """
        ...

    @staticmethod
    def Reverse(array:Array) -> Array:
        """ Reverse[T](array: Array[T]) -> Array[T] """
        ...

    @staticmethod
    def RotateRight(array:Array, count:int) -> Array:
        """ RotateRight[T](array: Array[T], count: int) -> Array[T] """
        ...

    @staticmethod
    def ShiftLeft(array:Array, count:int) -> Array:
        """ ShiftLeft[T](array: Array[T], count: int) -> Array[T] """
        ...

    @staticmethod
    def ShiftRight(array:Array, count:int) -> Array:
        """ ShiftRight[T](array: Array[T], count: int) -> Array[T] """
        ...

    @staticmethod
    def SwapLastTwo(array:Array): # -> 
        """ SwapLastTwo[T](array: Array[T]) """
        ...

    @staticmethod
    def ToArray(list:ICollection, convertor = ...) -> Array: # Not found arg types: {'convertor': 'Func'}
        """
        ToArray[T](list: ICollection[T]) -> Array[T]
        ToArray[(TElement, TResult)](list: ICollection[TElement], convertor: Func[TElement, TResult]) -> Array[TResult]
        """
        ...

    @staticmethod
    def ToComparer(comparison:Comparison) -> IComparer:
        """ ToComparer[T](comparison: Comparison[T]) -> IComparer[T] """
        ...

    @staticmethod
    def ValueEquals(array:Array, other:Array) -> bool:
        """ ValueEquals[T](array: Array[T], other: Array[T]) -> bool """
        ...

    EmptyObjects = ...
    EmptyStrings = ...
    __all__: list = ...


class Assert: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Unreachable(self) -> Exception:
        """ Get: Unreachable() -> Exception """
        ...


    @staticmethod
    def IsTrue(predicate): # ->  # Not found arg types: {'predicate': 'Func'}
        """ IsTrue(predicate: Func[bool]) """
        ...

    @staticmethod
    def NotEmpty(*__args:str): # -> 
        """ NotEmpty(str: str)NotEmpty[T](array: ICollection[T]) """
        ...

    @staticmethod
    def NotNull(*__args:object): # -> 
        """ NotNull(var: object)NotNull(var1: object, var2: object)NotNull(var1: object, var2: object, var3: object)NotNull(var1: object, var2: object, var3: object, var4: object) """
        ...

    @staticmethod
    def NotNullItems(items:IEnumerable): # -> 
        """ NotNullItems[T](items: IEnumerable[T]) """
        ...

    __all__: list = ...


class CacheDict: # skipped bases: <type 'object'>, <type 'object'>
    """ CacheDict[TKey, TValue](maxSize: int) """
    def Add(self, key, value): # ->  # Not found arg types: {'value': 'TValue', 'key': 'TKey'}
        """ Add(self: CacheDict[TKey, TValue], key: TKey, value: TValue) """
        ...

    def TryGetValue(self, key, value): # -> Tuple_[bool, TValue]
        """ TryGetValue(self: CacheDict[TKey, TValue], key: TKey) -> (bool, TValue) """
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


class CheckedDictionaryEnumerator(IEnumerator, IDictionaryEnumerator): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ no doc """
    def Dispose(self): # -> 
        """ Dispose(self: CheckedDictionaryEnumerator) """
        ...

    def DoMoveNext(self, *args): #cannot find CLR method
        """ DoMoveNext(self: CheckedDictionaryEnumerator) -> bool """
        ...

    def DoReset(self, *args): #cannot find CLR method
        """ DoReset(self: CheckedDictionaryEnumerator) """
        ...

    def GetKey(self, *args): #cannot find CLR method
        """ GetKey(self: CheckedDictionaryEnumerator) -> object """
        ...

    def GetValue(self, *args): #cannot find CLR method
        """ GetValue(self: CheckedDictionaryEnumerator) -> object """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: CheckedDictionaryEnumerator) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: CheckedDictionaryEnumerator) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[object, object]](enumerator: IEnumerator[KeyValuePair[object, object]], value: KeyValuePair[object, object]) -> bool """
        ...


class CollectionUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddRange(*__args): # -> 
        """ AddRange[T](collection: ICollection[T], items: IEnumerable[T])AddRange[T](list: IList[T], items: IEnumerable[T]) """
        ...

    @staticmethod
    def Cast(sequence:IEnumerable) -> IEnumerable:
        """ Cast[(S, T)](sequence: IEnumerable[S]) -> IEnumerable[T] """
        ...

    @staticmethod
    def ConvertAll(collection:IList, predicate) -> IList: # Not found arg types: {'predicate': 'Func'}
        """ ConvertAll[(T, TRet)](collection: IList[T], predicate: Func[T, TRet]) -> IList[TRet] """
        ...

    @staticmethod
    def CountOf(list:IList, item) -> int: # Not found arg types: {'item': 'T'}
        """ CountOf[T](list: IList[T], item: T) -> int """
        ...

    @staticmethod
    def CreateSetComparer() -> IEqualityComparer:
        """ CreateSetComparer[T]() -> IEqualityComparer[HashSet[T]] """
        ...

    @staticmethod
    def FindIndex(collection:IList, predicate:Predicate) -> int:
        """ FindIndex[T](collection: IList[T], predicate: Predicate[T]) -> int """
        ...

    @staticmethod
    def GetRange(list:IList, index:int, count:int) -> List:
        """ GetRange[T](list: IList[T], index: int, count: int) -> List[T] """
        ...

    @staticmethod
    def InsertRange(collection:IList, index:int, items:IEnumerable): # -> 
        """ InsertRange[T](collection: IList[T], index: int, items: IEnumerable[T]) """
        ...

    @staticmethod
    def MakeList(item) -> List: # Not found arg types: {'item': 'T'}
        """ MakeList[T](item: T) -> List[T] """
        ...

    @staticmethod
    def Max(values:IEnumerable) -> int:
        """ Max(values: IEnumerable[int]) -> int """
        ...

    @staticmethod
    def RemoveRange(collection:IList, index:int, count:int): # -> 
        """ RemoveRange[T](collection: IList[T], index: int, count: int) """
        ...

    @staticmethod
    def Select(enumerable:IEnumerable, selector) -> IEnumerable: # Not found arg types: {'selector': 'Func'}
        """ Select[TRet](enumerable: IEnumerable, selector: Func[object, TRet]) -> IEnumerable[TRet] """
        ...

    @staticmethod
    def ToCovariant(*__args:IEnumerable) -> IEnumerable:
        """
        ToCovariant[(T, TSuper)](enumerable: IEnumerable[T]) -> IEnumerable[TSuper]
        ToCovariant[(T, TSuper)](enumerator: IEnumerator[T]) -> IEnumerator[TSuper]
        """
        ...

    @staticmethod
    def ToDictionaryEnumerator(enumerator:IEnumerator) -> IDictionaryEnumerator:
        """ ToDictionaryEnumerator(enumerator: IEnumerator[KeyValuePair[object, object]]) -> IDictionaryEnumerator """
        ...

    @staticmethod
    def ToEnumerable(enumerable:IEnumerable) -> IEnumerable:
        """ ToEnumerable[T](enumerable: IEnumerable) -> IEnumerable[T] """
        ...

    @staticmethod
    def ToReverseArray(list:IList) -> Array:
        """ ToReverseArray[T](list: IList[T]) -> Array[T] """
        ...

    @staticmethod
    def ToSortedList(collection:ICollection, comparison:Comparison) -> IList:
        """ ToSortedList[T](collection: ICollection[T], comparison: Comparison[T]) -> IList[T] """
        ...

    @staticmethod
    def TrueForAll(collection:IEnumerable, predicate:Predicate) -> bool:
        """ TrueForAll[T](collection: IEnumerable[T], predicate: Predicate[T]) -> bool """
        ...

    __all__: list = ...


class ConsoleInputStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    Instance: ConsoleInputStream = ...


class ConsoleStreamType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConsoleStreamType, values: ErrorOutput (2), Input (0), Output (1) """
    ErrorOutput: ConsoleStreamType = ...
    Input: ConsoleStreamType = ...
    Output: ConsoleStreamType = ...
    value__ = ...


class ContractUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Assert(precondition:bool): # -> 
        """ Assert(precondition: bool) """
        ...

    @staticmethod
    def Ensures(condition:bool, message:str = ...): # -> 
        """ Ensures(condition: bool)Ensures(condition: bool, message: str) """
        ...

    @staticmethod
    def Invariant(condition:bool, message:str = ...): # -> 
        """ Invariant(condition: bool)Invariant(condition: bool, message: str) """
        ...

    @staticmethod
    def Old(value): # -> T # Not found arg types: {'value': 'T'}
        """ Old[T](value: T) -> T """
        ...

    @staticmethod
    def Parameter(value): # -> Tuple_[T, T]
        """ Parameter[T]() -> (T, T) """
        ...

    @staticmethod
    def Requires(precondition:bool, paramName:str = ..., message:str = ...): # -> 
        """ Requires(precondition: bool)Requires(precondition: bool, paramName: str)Requires(precondition: bool, paramName: str, message: str) """
        ...

    @staticmethod
    def RequiresArrayIndex(*__args): # -> 
        """ RequiresArrayIndex(arraySize: int, index: int, indexName: str)RequiresArrayIndex[T](array: IList[T], index: int, indexName: str) """
        ...

    @staticmethod
    def RequiresArrayInsertIndex(*__args): # -> 
        """ RequiresArrayInsertIndex(arraySize: int, index: int, indexName: str)RequiresArrayInsertIndex[T](array: IList[T], index: int, indexName: str) """
        ...

    @staticmethod
    def RequiresArrayRange(*__args): # -> 
        """ RequiresArrayRange(arraySize: int, offset: int, count: int, offsetName: str, countName: str)RequiresArrayRange(str: str, offset: int, count: int, offsetName: str, countName: str)RequiresArrayRange[T](array: IList[T], offset: int, count: int, offsetName: str, countName: str) """
        ...

    @staticmethod
    def RequiresListRange(array:IList, offset:int, count:int, offsetName:str, countName:str): # -> 
        """ RequiresListRange(array: IList, offset: int, count: int, offsetName: str, countName: str) """
        ...

    @staticmethod
    def RequiresNotEmpty(*__args): # -> 
        """ RequiresNotEmpty(str: str, paramName: str)RequiresNotEmpty[T](collection: ICollection[T], paramName: str) """
        ...

    @staticmethod
    def RequiresNotNull(value:object, paramName:str): # -> 
        """ RequiresNotNull(value: object, paramName: str) """
        ...

    @staticmethod
    def RequiresNotNullItems(*__args): # -> 
        """ RequiresNotNullItems[T](array: IList[T], arrayName: str)RequiresNotNullItems[T](collection: IEnumerable[T], collectionName: str) """
        ...

    @staticmethod
    def Result(): # -> T
        """ Result[T]() -> T """
        ...

    __all__: list = ...


class CopyOnWriteList(IList): # skipped bases: <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ CopyOnWriteList[T]() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CopyOnWriteList[T]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: CopyOnWriteList[T]) -> bool """
        ...


    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: CopyOnWriteList[T], item: T) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CopyOnWriteList[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: CopyOnWriteList[T], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: CopyOnWriteList[T], array: Array[T], arrayIndex: int) """
        ...

    def GetCopyForRead(self) -> List:
        """ GetCopyForRead(self: CopyOnWriteList[T]) -> List[T] """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CopyOnWriteList[T]) -> IEnumerator[T] """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Remove(self: CopyOnWriteList[T], item: T) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class DictionaryUnionEnumerator(CheckedDictionaryEnumerator): # skipped bases: <type 'IDictionaryEnumerator'>, <type 'IDisposable'>, <type 'IEnumerator'>, <type 'IEnumerator[KeyValuePair[object, object]]'>, <type 'object'>
    """ DictionaryUnionEnumerator(enums: IList[IDictionaryEnumerator]) """
    def __new__(cls, enums:IList) -> Self:
        """ __new__(cls: type, enums: IList[IDictionaryEnumerator]) """
        ...


class DynamicUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetExpressions(objects:Array) -> Array:
        """ GetExpressions(objects: Array[DynamicMetaObject]) -> Array[Expression] """
        ...

    @staticmethod
    def LightBind(binder:DynamicMetaObjectBinder, args:Array, compilationThreshold:int): # -> T
        """ LightBind[T](binder: DynamicMetaObjectBinder, args: Array[object], compilationThreshold: int) -> T """
        ...

    @staticmethod
    def ObjectToMetaObject(argValue:object, parameterExpression:Expression) -> DynamicMetaObject:
        """ ObjectToMetaObject(argValue: object, parameterExpression: Expression) -> DynamicMetaObject """
        ...

    __all__: list = ...


class EnumBounds: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsValid(value) -> bool: # Not found arg types: {'value': 'SourceCodeKind'}
        """ IsValid(value: SourceCodeKind) -> bool """
        ...

    __all__: list = ...


class EnumerableWrapper(IEnumerable): # skipped bases: <type 'object'>
    """ EnumerableWrapper(o: IEnumerable) """
    pass

class EnumUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BitwiseAnd(self, other:object) -> object:
        """ BitwiseAnd(self: object, other: object) -> object """
        ...

    @staticmethod
    def BitwiseOr(self, other:object) -> object:
        """ BitwiseOr(self: object, other: object) -> object """
        ...

    @staticmethod
    def ExclusiveOr(self, other:object) -> object:
        """ ExclusiveOr(self: object, other: object) -> object """
        ...

    @staticmethod
    def OnesComplement(self) -> object:
        """ OnesComplement(self: object) -> object """
        ...

    __all__: list = ...


class ExceptionUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetData(e:Exception, key:object) -> object:
        """ GetData(e: Exception, key: object) -> object """
        ...

    @staticmethod
    def MakeArgumentItemNullException(index:int, arrayName:str) -> ArgumentNullException:
        """ MakeArgumentItemNullException(index: int, arrayName: str) -> ArgumentNullException """
        ...

    @staticmethod
    def MakeArgumentOutOfRangeException(paramName:str, actualValue:object, message:str) -> ArgumentOutOfRangeException:
        """ MakeArgumentOutOfRangeException(paramName: str, actualValue: object, message: str) -> ArgumentOutOfRangeException """
        ...

    @staticmethod
    def RemoveData(e:Exception, key:object): # -> 
        """ RemoveData(e: Exception, key: object) """
        ...

    @staticmethod
    def SetData(e:Exception, key:object, data:object): # -> 
        """ SetData(e: Exception, key: object, data: object) """
        ...

    __all__: list = ...


class ExtensionMethodInfo(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExtendedType(self) -> Type:
        """ Get: ExtendedType(self: ExtensionMethodInfo) -> Type """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: ExtensionMethodInfo) -> MethodInfo """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExtensionMethodInfo) -> int """
        ...

    def IsExtensionOf(self, type:Type) -> bool:
        """ IsExtensionOf(self: ExtensionMethodInfo, type: Type) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class HybridMapping: # skipped bases: <type 'object'>, <type 'object'>
    """
    HybridMapping[T]()
    HybridMapping[T](offset: int)
    """
    def GetIdFromObject(self, value) -> int: # Not found arg types: {'value': 'T'}
        """ GetIdFromObject(self: HybridMapping[T], value: T) -> int """
        ...

    def GetObjectFromId(self, id:int): # -> T
        """ GetObjectFromId(self: HybridMapping[T], id: int) -> T """
        ...

    def RemoveOnId(self, id:int): # -> 
        """ RemoveOnId(self: HybridMapping[T], id: int) """
        ...

    def RemoveOnObject(self, value): # ->  # Not found arg types: {'value': 'T'}
        """ RemoveOnObject(self: HybridMapping[T], value: T) """
        ...

    def StrongAdd(self, value, pos:int) -> int: # Not found arg types: {'value': 'T'}
        """ StrongAdd(self: HybridMapping[T], value: T, pos: int) -> int """
        ...

    def WeakAdd(self, value) -> int: # Not found arg types: {'value': 'T'}
        """ WeakAdd(self: HybridMapping[T], value: T) -> int """
        ...

    SIZE: int = ...


class IOUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ReadTo(reader:TextReader, terminator:Char) -> str:
        """ ReadTo(reader: TextReader, terminator: Char) -> str """
        ...

    @staticmethod
    def SeekLine(reader:TextReader, line:int) -> bool:
        """ SeekLine(reader: TextReader, line: int) -> bool """
        ...

    @staticmethod
    def SeekTo(reader:TextReader, c:Char) -> bool:
        """ SeekTo(reader: TextReader, c: Char) -> bool """
        ...

    @staticmethod
    def ToValidFileName(path:str) -> str:
        """ ToValidFileName(path: str) -> str """
        ...

    @staticmethod
    def ToValidPath(path:str, isMask:bool = ...) -> str:
        """
        ToValidPath(path: str) -> str
        ToValidPath(path: str, isMask: bool) -> str
        """
        ...

    __all__: list = ...


class MathUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Abs(self): # -> long
        """
        Abs(self: long) -> long
        Abs(self: complex) -> float
        """
        ...

    @staticmethod
    def AsInt32(self, ret) -> Tuple_[bool, int]:
        """ AsInt32(self: long) -> (bool, int) """
        ...

    @staticmethod
    def AsInt64(self, ret) -> Tuple_[bool, Int64]:
        """ AsInt64(self: long) -> (bool, Int64) """
        ...

    @staticmethod
    def AsUInt32(self, ret) -> Tuple_[bool, UInt32]:
        """ AsUInt32(self: long) -> (bool, UInt32) """
        ...

    @staticmethod
    def AsUInt64(self, ret) -> Tuple_[bool, UInt64]:
        """ AsUInt64(self: long) -> (bool, UInt64) """
        ...

    @staticmethod
    def BitLength(x:Int64) -> int:
        """
        BitLength(x: Int64) -> int
        BitLength(x: int) -> int
        BitLength(x: long) -> int
        """
        ...

    @staticmethod
    def BitLengthUnsigned(x:UInt64) -> int:
        """
        BitLengthUnsigned(x: UInt64) -> int
        BitLengthUnsigned(x: UInt32) -> int
        """
        ...

    @staticmethod
    def Conjugate(self): # -> complex
        """ Conjugate(self: complex) -> complex """
        ...

    @staticmethod
    def Erf(v0:float) -> float:
        """ Erf(v0: float) -> float """
        ...

    @staticmethod
    def ErfComplement(v0:float) -> float:
        """ ErfComplement(v0: float) -> float """
        ...

    @staticmethod
    def FloorDivideUnchecked(x:int, y:int) -> int:
        """
        FloorDivideUnchecked(x: int, y: int) -> int
        FloorDivideUnchecked(x: Int64, y: Int64) -> Int64
        """
        ...

    @staticmethod
    def FloorRemainder(x:int, y:int) -> int:
        """
        FloorRemainder(x: int, y: int) -> int
        FloorRemainder(x: Int64, y: Int64) -> Int64
        """
        ...

    @staticmethod
    def Gamma(v0:float) -> float:
        """ Gamma(v0: float) -> float """
        ...

    @staticmethod
    def GetBitCount(self) -> int:
        """ GetBitCount(self: long) -> int """
        ...

    @staticmethod
    def GetByteCount(self) -> int:
        """ GetByteCount(self: long) -> int """
        ...

    @staticmethod
    def GetRandBits(*__args): # -> long
        """
        GetRandBits(NextBytes: Action[Array[Byte]], bits: int) -> long
        GetRandBits(generator: Random, bits: int) -> long
        """
        ...

    @staticmethod
    def GetWord(self, index:int) -> UInt32:
        """ GetWord(self: long, index: int) -> UInt32 """
        ...

    @staticmethod
    def GetWordCount(self) -> int:
        """ GetWordCount(self: long) -> int """
        ...

    @staticmethod
    def GetWords(self) -> Array:
        """ GetWords(self: long) -> Array[UInt32] """
        ...

    @staticmethod
    def Hypot(x:float, y:float) -> float:
        """ Hypot(x: float, y: float) -> float """
        ...

    @staticmethod
    def Imaginary(self) -> float:
        """ Imaginary(self: complex) -> float """
        ...

    @staticmethod
    def IsNegative(self) -> bool:
        """ IsNegative(self: long) -> bool """
        ...

    @staticmethod
    def IsNegativeZero(self) -> bool:
        """ IsNegativeZero(self: float) -> bool """
        ...

    @staticmethod
    def IsPositive(self) -> bool:
        """ IsPositive(self: long) -> bool """
        ...

    @staticmethod
    def IsZero(self) -> bool:
        """
        IsZero(self: long) -> bool
        IsZero(self: complex) -> bool
        """
        ...

    @staticmethod
    def Log(self, baseValue:float = ...) -> float:
        """
        Log(self: long) -> float
        Log(self: long, baseValue: float) -> float
        """
        ...

    @staticmethod
    def Log10(self) -> float:
        """ Log10(self: long) -> float """
        ...

    @staticmethod
    def LogGamma(v0:float) -> float:
        """ LogGamma(v0: float) -> float """
        ...

    @staticmethod
    def MakeComplex(real:float, imag:float): # -> complex
        """ MakeComplex(real: float, imag: float) -> complex """
        ...

    @staticmethod
    def MakeImaginary(imag:float): # -> complex
        """ MakeImaginary(imag: float) -> complex """
        ...

    @staticmethod
    def MakeReal(real:float): # -> complex
        """ MakeReal(real: float) -> complex """
        ...

    @staticmethod
    def ModPow(self, power:int, mod): # -> long # Not found arg types: {'mod': 'long'}
        """
        ModPow(self: long, power: int, mod: long) -> long
        ModPow(self: long, power: long, mod: long) -> long
        """
        ...

    @staticmethod
    def Pow(self, power): # -> complex # Not found arg types: {'power': 'complex'}
        """ Pow(self: complex, power: complex) -> complex """
        ...

    @staticmethod
    def Power(self, exp:int): # -> long
        """
        Power(self: long, exp: int) -> long
        Power(self: long, exp: Int64) -> long
        """
        ...

    @staticmethod
    def Random(generator:Random, limit): # -> long # Not found arg types: {'limit': 'long'}
        """ Random(generator: Random, limit: long) -> long """
        ...

    @staticmethod
    def Round(value:float, precision:int, mode:MidpointRounding) -> float:
        """ Round(value: float, precision: int, mode: MidpointRounding) -> float """
        ...

    @staticmethod
    def RoundAwayFromZero(value:float, precision:int = ...) -> float:
        """
        RoundAwayFromZero(value: float) -> float
        RoundAwayFromZero(value: float, precision: int) -> float
        """
        ...

    @staticmethod
    def ToFloat64(self) -> float:
        """ ToFloat64(self: long) -> float """
        ...

    @staticmethod
    def ToString(self:long = ..., radix:int = ...) -> str:
        """ ToString(self: long, radix: int) -> str """
        ...

    @staticmethod
    def TryToFloat64(self, result) -> Tuple_[bool, float]:
        """ TryToFloat64(self: long) -> (bool, float) """
        ...

    __all__: list = ...


class MonitorUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Enter(obj:object, lockTaken:bool) -> bool:
        """ Enter(obj: object, lockTaken: bool) -> bool """
        ...

    @staticmethod
    def Exit(obj:object, lockTaken:bool) -> bool:
        """ Exit(obj: object, lockTaken: bool) -> bool """
        ...

    @staticmethod
    def TryEnter(obj:object, lockTaken:bool) -> Tuple_[bool, bool]:
        """ TryEnter(obj: object, lockTaken: bool) -> (bool, bool) """
        ...

    __all__: list = ...


class Publisher: # skipped bases: <type 'object'>, <type 'object'>
    """ Publisher[TKey, TValue]() """
    @property
    def Keys(self) -> IEnumerable:
        """ Get: Keys(self: Publisher[TKey, TValue]) -> IEnumerable[TKey] """
        ...


    def GetOrCreateValue(self, key, create): # -> TValue # Not found arg types: {'key': 'TKey', 'create': 'Func'}
        """ GetOrCreateValue(self: Publisher[TKey, TValue], key: TKey, create: Func[TValue]) -> TValue """
        ...


class ReferenceEqualityComparer(IEqualityComparer): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReflectionUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Ancestors(type:Type) -> IEnumerable:
        """ Ancestors(type: Type) -> IEnumerable[Type] """
        ...

    @staticmethod
    def ContainsGenericParameters(type:Type) -> bool:
        """ ContainsGenericParameters(type: Type) -> bool """
        ...

    @staticmethod
    def CopyMethodSignature(from_:MethodInfo, to:MethodBuilder, substituteDeclaringType:bool): # -> 
        """ CopyMethodSignature(from: MethodInfo, to: MethodBuilder, substituteDeclaringType: bool) """
        ...

    @staticmethod
    def CreateDelegate(methodInfo:MethodInfo, delegateType:Type, target:object = ...) -> Delegate:
        """
        CreateDelegate(methodInfo: MethodInfo, delegateType: Type) -> Delegate
        CreateDelegate(methodInfo: MethodInfo, delegateType: Type, target: object) -> Delegate
        """
        ...

    @staticmethod
    def DefineDynamicAssembly(name:AssemblyName, access:AssemblyBuilderAccess) -> AssemblyBuilder:
        """ DefineDynamicAssembly(name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder """
        ...

    @staticmethod
    def DefineMethodOverride(tb:TypeBuilder, extra:MethodAttributes, decl:MethodInfo) -> MethodBuilder:
        """ DefineMethodOverride(tb: TypeBuilder, extra: MethodAttributes, decl: MethodInfo) -> MethodBuilder """
        ...

    @staticmethod
    def FormatSignature(result:StringBuilder, method:MethodBase, nameDispenser = ...) -> StringBuilder: # Not found arg types: {'nameDispenser': 'Func'}
        """
        FormatSignature(result: StringBuilder, method: MethodBase) -> StringBuilder
        FormatSignature(result: StringBuilder, method: MethodBase, nameDispenser: Func[Type, str]) -> StringBuilder
        """
        ...

    @staticmethod
    def FormatTypeArgs(result:StringBuilder, types:Array, nameDispenser = ...) -> StringBuilder: # Not found arg types: {'nameDispenser': 'Func'}
        """
        FormatTypeArgs(result: StringBuilder, types: Array[Type]) -> StringBuilder
        FormatTypeArgs(result: StringBuilder, types: Array[Type], nameDispenser: Func[Type, str]) -> StringBuilder
        """
        ...

    @staticmethod
    def FormatTypeName(result:StringBuilder, type:Type, nameDispenser = ...) -> StringBuilder: # Not found arg types: {'nameDispenser': 'Func'}
        """
        FormatTypeName(result: StringBuilder, type: Type, nameDispenser: Func[Type, str]) -> StringBuilder
        FormatTypeName(result: StringBuilder, type: Type) -> StringBuilder
        """
        ...

    @staticmethod
    def GetBaseType(type:Type) -> Type:
        """ GetBaseType(type: Type) -> Type """
        ...

    @staticmethod
    def GetCustomAttribute(*__args):
        """ no doc """
        ...

    @staticmethod
    def GetDeclaredConstructors(type:Type) -> IEnumerable:
        """ GetDeclaredConstructors(type: Type) -> IEnumerable[ConstructorInfo] """
        ...

    @staticmethod
    def GetDeclaredEvent(type:Type, name:str) -> EventInfo:
        """ GetDeclaredEvent(type: Type, name: str) -> EventInfo """
        ...

    @staticmethod
    def GetDeclaredEvents(type:Type) -> IEnumerable:
        """ GetDeclaredEvents(type: Type) -> IEnumerable[EventInfo] """
        ...

    @staticmethod
    def GetDeclaredField(type:Type, name:str) -> FieldInfo:
        """ GetDeclaredField(type: Type, name: str) -> FieldInfo """
        ...

    @staticmethod
    def GetDeclaredFields(type:Type) -> IEnumerable:
        """ GetDeclaredFields(type: Type) -> IEnumerable[FieldInfo] """
        ...

    @staticmethod
    def GetDeclaredInterfaces(type:Type) -> List:
        """ GetDeclaredInterfaces(type: Type) -> List[Type] """
        ...

    @staticmethod
    def GetDeclaredMembers(type:Type, name:str) -> IEnumerable:
        """ GetDeclaredMembers(type: Type, name: str) -> IEnumerable[MemberInfo] """
        ...

    @staticmethod
    def GetDeclaredMethods(type:Type, name:str) -> IEnumerable:
        """ GetDeclaredMethods(type: Type, name: str) -> IEnumerable[MethodInfo] """
        ...

    @staticmethod
    def GetDeclaredNestedType(type:Type, name:str) -> Type:
        """ GetDeclaredNestedType(type: Type, name: str) -> Type """
        ...

    @staticmethod
    def GetDeclaredNestedTypes(type:Type) -> IEnumerable:
        """ GetDeclaredNestedTypes(type: Type) -> IEnumerable[Type] """
        ...

    @staticmethod
    def GetDeclaredProperties(type:Type) -> IEnumerable:
        """ GetDeclaredProperties(type: Type) -> IEnumerable[PropertyInfo] """
        ...

    @staticmethod
    def GetDeclaredProperty(type:Type, name:str) -> PropertyInfo:
        """ GetDeclaredProperty(type: Type, name: str) -> PropertyInfo """
        ...

    @staticmethod
    def GetDefaultValue(info:ParameterInfo) -> object:
        """ GetDefaultValue(info: ParameterInfo) -> object """
        ...

    @staticmethod
    def GetDelegateSignature(delegateType, parameterInfos, returnInfo) -> Tuple_[Array, ParameterInfo]:
        """ GetDelegateSignature(delegateType: Type) -> (Array[ParameterInfo], ParameterInfo) """
        ...

    @staticmethod
    def GetGenericParameterAttributes(type:Type) -> GenericParameterAttributes:
        """ GetGenericParameterAttributes(type: Type) -> GenericParameterAttributes """
        ...

    @staticmethod
    def GetGenericTypeArguments(type:Type) -> Array:
        """ GetGenericTypeArguments(type: Type) -> Array[Type] """
        ...

    @staticmethod
    def GetGenericTypeParameters(type:Type) -> Array:
        """ GetGenericTypeParameters(type: Type) -> Array[Type] """
        ...

    @staticmethod
    def GetImplementedInterfaces(type:Type) -> IEnumerable:
        """ GetImplementedInterfaces(type: Type) -> IEnumerable[Type] """
        ...

    @staticmethod
    def GetInheritedEvents(type:Type, name:str, flattenHierarchy:bool) -> IEnumerable:
        """ GetInheritedEvents(type: Type, name: str, flattenHierarchy: bool) -> IEnumerable[EventInfo] """
        ...

    @staticmethod
    def GetInheritedFields(type:Type, name:str, flattenHierarchy:bool) -> IEnumerable:
        """ GetInheritedFields(type: Type, name: str, flattenHierarchy: bool) -> IEnumerable[FieldInfo] """
        ...

    @staticmethod
    def GetInheritedMembers(type:Type, name:str, flattenHierarchy:bool) -> IEnumerable:
        """ GetInheritedMembers(type: Type, name: str, flattenHierarchy: bool) -> IEnumerable[MemberInfo] """
        ...

    @staticmethod
    def GetInheritedMethods(type:Type, name:str, flattenHierarchy:bool) -> IEnumerable:
        """ GetInheritedMethods(type: Type, name: str, flattenHierarchy: bool) -> IEnumerable[MethodInfo] """
        ...

    @staticmethod
    def GetInheritedProperties(type:Type, name:str, flattenHierarchy:bool) -> IEnumerable:
        """ GetInheritedProperties(type: Type, name: str, flattenHierarchy: bool) -> IEnumerable[PropertyInfo] """
        ...

    @staticmethod
    def GetMethod(d:Delegate) -> MethodInfo:
        """ GetMethod(d: Delegate) -> MethodInfo """
        ...

    @staticmethod
    def GetMethodInfos(members:Array) -> Array:
        """ GetMethodInfos(members: Array[MemberInfo]) -> Array[MethodBase] """
        ...

    @staticmethod
    def GetModules(assembly:Assembly) -> IEnumerable:
        """ GetModules(assembly: Assembly) -> IEnumerable[Module] """
        ...

    @staticmethod
    def GetNormalizedTypeName(*__args:Type) -> str:
        """
        GetNormalizedTypeName(type: Type) -> str
        GetNormalizedTypeName(typeName: str) -> str
        """
        ...

    @staticmethod
    def GetObjectCallSiteDelegateType(paramCnt:int) -> Type:
        """ GetObjectCallSiteDelegateType(paramCnt: int) -> Type """
        ...

    @staticmethod
    def GetParameterTypes(parameterInfos:Array) -> Array:
        """
        GetParameterTypes(parameterInfos: Array[ParameterInfo]) -> Array[Type]
        GetParameterTypes(parameterInfos: IList[ParameterInfo]) -> Array[Type]
        """
        ...

    @staticmethod
    def GetRawConstantValue(field:FieldInfo) -> object:
        """ GetRawConstantValue(field: FieldInfo) -> object """
        ...

    @staticmethod
    def GetReturnType(mi:MethodBase) -> Type:
        """ GetReturnType(mi: MethodBase) -> Type """
        ...

    @staticmethod
    def GetTypeCode(type:Type) -> TypeCode:
        """ GetTypeCode(type: Type) -> TypeCode """
        ...

    @staticmethod
    def GetVisibleExtensionMethodGroups(assembly:Assembly, useCache:bool) -> IEnumerable:
        """ GetVisibleExtensionMethodGroups(assembly: Assembly, useCache: bool) -> IEnumerable[KeyValuePair[str, IEnumerable[ExtensionMethodInfo]]] """
        ...

    @staticmethod
    def GetVisibleExtensionMethods(assembly:Assembly) -> IEnumerable:
        """ GetVisibleExtensionMethods(assembly: Assembly) -> IEnumerable[MethodInfo] """
        ...

    @staticmethod
    def GetVisibleExtensionMethodsSlow(assembly:Assembly) -> IEnumerable:
        """ GetVisibleExtensionMethodsSlow(assembly: Assembly) -> IEnumerable[MethodInfo] """
        ...

    @staticmethod
    def HasDefaultValue(pi:ParameterInfo) -> bool:
        """ HasDefaultValue(pi: ParameterInfo) -> bool """
        ...

    @staticmethod
    def IsAbstract(type:Type) -> bool:
        """ IsAbstract(type: Type) -> bool """
        ...

    @staticmethod
    def IsClass(type:Type) -> bool:
        """ IsClass(type: Type) -> bool """
        ...

    @staticmethod
    def IsDefined(assembly:Assembly, attributeType:Type) -> bool:
        """ IsDefined(assembly: Assembly, attributeType: Type) -> bool """
        ...

    @staticmethod
    def IsDynamicMethod(method:MethodBase) -> bool:
        """ IsDynamicMethod(method: MethodBase) -> bool """
        ...

    @staticmethod
    def IsEnum(type:Type) -> bool:
        """ IsEnum(type: Type) -> bool """
        ...

    @staticmethod
    def IsExtension(member:MemberInfo) -> bool:
        """ IsExtension(member: MemberInfo) -> bool """
        ...

    @staticmethod
    def IsGenericType(type:Type) -> bool:
        """ IsGenericType(type: Type) -> bool """
        ...

    @staticmethod
    def IsGenericTypeDefinition(type:Type) -> bool:
        """ IsGenericTypeDefinition(type: Type) -> bool """
        ...

    @staticmethod
    def IsInterface(type:Type) -> bool:
        """ IsInterface(type: Type) -> bool """
        ...

    @staticmethod
    def IsMandatory(pi:ParameterInfo) -> bool:
        """ IsMandatory(pi: ParameterInfo) -> bool """
        ...

    @staticmethod
    def IsOutParameter(pi:ParameterInfo) -> bool:
        """ IsOutParameter(pi: ParameterInfo) -> bool """
        ...

    @staticmethod
    def IsParamArray(parameter:ParameterInfo) -> bool:
        """ IsParamArray(parameter: ParameterInfo) -> bool """
        ...

    @staticmethod
    def IsParamDictionary(parameter:ParameterInfo) -> bool:
        """ IsParamDictionary(parameter: ParameterInfo) -> bool """
        ...

    @staticmethod
    def IsParamsMethod(*__args:MethodBase) -> bool:
        """
        IsParamsMethod(method: MethodBase) -> bool
        IsParamsMethod(pis: Array[ParameterInfo]) -> bool
        """
        ...

    @staticmethod
    def IsPrimitive(type:Type) -> bool:
        """ IsPrimitive(type: Type) -> bool """
        ...

    @staticmethod
    def IsPrivate(*__args:PropertyInfo) -> bool:
        """
        IsPrivate(property: PropertyInfo) -> bool
        IsPrivate(evnt: EventInfo) -> bool
        """
        ...

    @staticmethod
    def IsPublic(*__args:PropertyInfo) -> bool:
        """
        IsPublic(property: PropertyInfo) -> bool
        IsPublic(type: Type) -> bool
        """
        ...

    @staticmethod
    def IsSealed(type:Type) -> bool:
        """ IsSealed(type: Type) -> bool """
        ...

    @staticmethod
    def IsStatic(*__args:PropertyInfo) -> bool:
        """
        IsStatic(property: PropertyInfo) -> bool
        IsStatic(evnt: EventInfo) -> bool
        """
        ...

    @staticmethod
    def IsValueType(type:Type) -> bool:
        """ IsValueType(type: Type) -> bool """
        ...

    @staticmethod
    def IsVisible(type:Type) -> bool:
        """ IsVisible(type: Type) -> bool """
        ...

    @staticmethod
    def ProhibitsNull(parameter:ParameterInfo) -> bool:
        """ ProhibitsNull(parameter: ParameterInfo) -> bool """
        ...

    @staticmethod
    def ProhibitsNullItems(parameter:ParameterInfo) -> bool:
        """ ProhibitsNullItems(parameter: ParameterInfo) -> bool """
        ...

    @staticmethod
    def SignatureEquals(method:MethodInfo, requiredSignature:Array) -> bool:
        """ SignatureEquals(method: MethodInfo, *requiredSignature: Array[Type]) -> bool """
        ...

    @staticmethod
    def UnwrapEnumValue(value:object) -> object:
        """ UnwrapEnumValue(value: object) -> object """
        ...

    @staticmethod
    def WithBindingFlags(*__args) -> MemberInfo:
        """
        WithBindingFlags(member: MemberInfo, flags: BindingFlags) -> MemberInfo
        WithBindingFlags(member: MethodInfo, flags: BindingFlags) -> MethodInfo
        WithBindingFlags(member: ConstructorInfo, flags: BindingFlags) -> ConstructorInfo
        WithBindingFlags(member: FieldInfo, flags: BindingFlags) -> FieldInfo
        WithBindingFlags(member: PropertyInfo, flags: BindingFlags) -> PropertyInfo
        WithBindingFlags(member: EventInfo, flags: BindingFlags) -> EventInfo
        WithBindingFlags(member: Type, flags: BindingFlags) -> Type
        WithBindingFlags(members: IEnumerable[MemberInfo], flags: BindingFlags) -> IEnumerable[MemberInfo]
        WithBindingFlags(members: IEnumerable[MethodInfo], flags: BindingFlags) -> IEnumerable[MethodInfo]
        WithBindingFlags(members: IEnumerable[ConstructorInfo], flags: BindingFlags) -> IEnumerable[ConstructorInfo]
        WithBindingFlags(members: IEnumerable[FieldInfo], flags: BindingFlags) -> IEnumerable[FieldInfo]
        WithBindingFlags(members: IEnumerable[PropertyInfo], flags: BindingFlags) -> IEnumerable[PropertyInfo]
        WithBindingFlags(members: IEnumerable[EventInfo], flags: BindingFlags) -> IEnumerable[EventInfo]
        WithBindingFlags(members: IEnumerable[Type], flags: BindingFlags) -> IEnumerable[Type]
        """
        ...

    @staticmethod
    def WithSignature(members:IEnumerable, parameterTypes:Array) -> IEnumerable:
        """
        WithSignature(members: IEnumerable[MethodInfo], parameterTypes: Array[Type]) -> IEnumerable[MethodInfo]
        WithSignature(members: IEnumerable[ConstructorInfo], parameterTypes: Array[Type]) -> IEnumerable[ConstructorInfo]
        """
        ...

    AllMembers: BindingFlags = ...
    EmptyTypes = ...
    GenericArityDelimiter: Char = ...
    __all__: list = ...


class StringUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultEncoding(self) -> Encoding:
        """ Get: DefaultEncoding() -> Encoding """
        ...


    @staticmethod
    def AddSlashes(str:str) -> str:
        """ AddSlashes(str: str) -> str """
        ...

    @staticmethod
    def CountOf(str:str, c:Char) -> int:
        """ CountOf(str: str, c: Char) -> int """
        ...

    @staticmethod
    def GetCultureInfo(name:str) -> CultureInfo:
        """ GetCultureInfo(name: str) -> CultureInfo """
        ...

    @staticmethod
    def GetLongestPrefix(str:str, separator:Char, includeSeparator:bool) -> str:
        """ GetLongestPrefix(str: str, separator: Char, includeSeparator: bool) -> str """
        ...

    @staticmethod
    def GetSuffix(str:str, separator:Char, includeSeparator:bool) -> str:
        """ GetSuffix(str: str, separator: Char, includeSeparator: bool) -> str """
        ...

    @staticmethod
    def Split(str:str, *__args:str) -> IEnumerable:
        """
        Split(str: str, separators: Array[Char], maxComponents: int, options: StringSplitOptions) -> Array[str]
        Split(str: str, separator: str, maxComponents: int, options: StringSplitOptions) -> Array[str]
        Split(str: str, sep: str) -> IEnumerable[str]
        """
        ...

    @staticmethod
    def SplitWords(text:str, indentFirst:bool, lineWidth:int) -> str:
        """ SplitWords(text: str, indentFirst: bool, lineWidth: int) -> str """
        ...

    @staticmethod
    def TryParseDate(s, provider, style, result) -> Tuple_[bool, DateTime]:
        """ TryParseDate(s: str, provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime) """
        ...

    @staticmethod
    def TryParseDateTimeExact(s, *__args) -> Tuple_[bool, DateTime]:
        """
        TryParseDateTimeExact(s: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)
        TryParseDateTimeExact(s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> (bool, DateTime)
        """
        ...

    @staticmethod
    def TryParseDouble(s, style, provider, result) -> Tuple_[bool, float]:
        """ TryParseDouble(s: str, style: NumberStyles, provider: IFormatProvider) -> (bool, float) """
        ...

    @staticmethod
    def TryParseInt32(s, result) -> Tuple_[bool, int]:
        """ TryParseInt32(s: str) -> (bool, int) """
        ...

    __all__: list = ...


class SynchronizedDictionary(IDictionary): # skipped bases: <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'object'>
    """
    SynchronizedDictionary[TKey, TValue]()
    SynchronizedDictionary[TKey, TValue](dictionary: Dictionary[TKey, TValue])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SynchronizedDictionary[TKey, TValue]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SynchronizedDictionary[TKey, TValue]) -> bool """
        ...

    @property
    def UnderlyingDictionary(self) -> Dictionary:
        """ Get: UnderlyingDictionary(self: SynchronizedDictionary[TKey, TValue]) -> Dictionary[TKey, TValue] """
        ...


    def Clear(self): # -> 
        """ Clear(self: SynchronizedDictionary[TKey, TValue]) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: SynchronizedDictionary[TKey, TValue], item: KeyValuePair[TKey, TValue]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: SynchronizedDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SynchronizedDictionary[TKey, TValue]) -> IEnumerator[KeyValuePair[TKey, TValue]] """
        ...


class ThreadingUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetCurrentThreadId() -> int:
        """ GetCurrentThreadId() -> int """
        ...

    __all__: list = ...


class ThreadLocal: # skipped bases: <type 'object'>, <type 'object'>
    """
    ThreadLocal[T]()
    ThreadLocal[T](refCounted: bool)
    """
    @property
    def Value(self): # -> T
        """
        Get: Value(self: ThreadLocal[T]) -> T
        Set: Value(self: ThreadLocal[T]) = value
        """
        ...


    def GetOrCreate(self, func): # -> T # Not found arg types: {'func': 'Func'}
        """ GetOrCreate(self: ThreadLocal[T], func: Func[T]) -> T """
        ...

    def GetStorageInfo(self): # -> StorageInfo
        """ GetStorageInfo(self: ThreadLocal[T]) -> StorageInfo """
        ...

    def StorageInfo(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Update(self, *__args): # -> T # Not found arg types: {'*__args': 'Func'}
        """
        Update(self: ThreadLocal[T], updater: Func[T, T]) -> T
        Update(self: ThreadLocal[T], newValue: T) -> T
        """
        ...



class TypeMemberCache: # skipped bases: <type 'object'>, <type 'object'>
    """ TypeMemberCache[T](reflector: Func[Type, IEnumerable[T]]) """
    def GetMembers(self, type:Type, name:str, inherited:bool) -> IEnumerable:
        """ GetMembers(self: TypeMemberCache[T], type: Type, name: str, inherited: bool) -> IEnumerable[T] """
        ...


class TypeUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsComObject(obj:object) -> bool:
        """ IsComObject(obj: object) -> bool """
        ...

    @staticmethod
    def IsComObjectType(type:Type) -> bool:
        """ IsComObjectType(type: Type) -> bool """
        ...

    @staticmethod
    def IsNested(t:Type) -> bool:
        """ IsNested(t: Type) -> bool """
        ...

    ComObjectType = ...
    __all__: list = ...


class ValueArray(IEquatable): # skipped bases: <type 'object'>
    """ ValueArray[T](array: Array[T]) """
    def GetHashCode(self) -> int:
        """ GetHashCode(self: ValueArray[T]) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WeakDictionary(IDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[TKey, TValue]]'>, <type 'ICollection[KeyValuePair[TKey, TValue]]'>, <type 'IEnumerable'>, <type 'object'>
    """ WeakDictionary[TKey, TValue]() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: WeakDictionary[TKey, TValue]) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: WeakDictionary[TKey, TValue]) -> bool """
        ...


    def Clear(self): # -> 
        """ Clear(self: WeakDictionary[TKey, TValue]) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: WeakDictionary[TKey, TValue], item: KeyValuePair[TKey, TValue]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: WeakDictionary[TKey, TValue], array: Array[KeyValuePair[TKey, TValue]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: WeakDictionary[TKey, TValue]) -> IEnumerator[KeyValuePair[TKey, TValue]] """
        ...

    def GetOrCreateValue(self, key): # -> TValue # Not found arg types: {'key': 'TKey'}
        """ GetOrCreateValue(self: WeakDictionary[TKey, TValue], key: TKey) -> TValue """
        ...


class WeakHandle: # skipped bases: <type 'object'>, <type 'object'>
    """ WeakHandle(target: object, trackResurrection: bool) """
    @property
    def Target(self) -> object:
        """ Get: Target(self: WeakHandle) -> object """
        ...


    def Free(self): # -> 
        """ Free(self: WeakHandle) """
        ...


