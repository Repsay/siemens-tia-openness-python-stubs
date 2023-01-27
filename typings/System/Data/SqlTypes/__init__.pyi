# encoding: utf-8
# module System.Data.SqlTypes calls itself SqlTypes
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Byte, DateTime, Decimal, Enum, Guid, IComparable, 
    Int16, Int64, Single, SystemException, TimeSpan)

from System.Globalization import CompareInfo, CompareOptions, CultureInfo

from System.IO import FileAccess, FileOptions, Stream

from System.Runtime.Serialization import ISerializable

from System.Xml import XmlQualifiedName, XmlReader

from System.Xml.Schema import XmlSchemaSet

from System.Xml.Serialization import IXmlSerializable

from System.Xml.Serialization.Advanced import SchemaImporterExtension

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class INullable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsNull(self) -> bool:
        """ Get: IsNull(self: INullable) -> bool """
        ...



class SqlTypeException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlTypeException()
    SqlTypeException(message: str)
    SqlTypeException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class SqlAlreadyFilledException(SqlTypeException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlAlreadyFilledException()
    SqlAlreadyFilledException(message: str)
    SqlAlreadyFilledException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class SqlBinary(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlBinary(value: Array[Byte]) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: SqlBinary) -> int """
        ...

    @property
    def Value(self) -> Array:
        """ Get: Value(self: SqlBinary) -> Array[Byte] """
        ...


    @staticmethod
    def Add(x:SqlBinary, y:SqlBinary) -> SqlBinary:
        """ Add(x: SqlBinary, y: SqlBinary) -> SqlBinary """
        ...

    @staticmethod
    def Concat(x:SqlBinary, y:SqlBinary) -> SqlBinary:
        """ Concat(x: SqlBinary, y: SqlBinary) -> SqlBinary """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlBinary, y: SqlBinary) -> SqlBoolean
        Equals(self: SqlBinary, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlBinary) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlBinary, y:SqlBinary) -> SqlBoolean:
        """ GreaterThan(x: SqlBinary, y: SqlBinary) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlBinary, y:SqlBinary) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlBinary, y: SqlBinary) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlBinary, y:SqlBinary) -> SqlBoolean:
        """ LessThan(x: SqlBinary, y: SqlBinary) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlBinary, y:SqlBinary) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlBinary, y: SqlBinary) -> SqlBoolean """
        ...

    @staticmethod
    def NotEquals(x:SqlBinary, y:SqlBinary) -> SqlBoolean:
        """ NotEquals(x: SqlBinary, y: SqlBinary) -> SqlBoolean """
        ...

    def ToSqlGuid(self) -> SqlGuid:
        """ ToSqlGuid(self: SqlBinary) -> SqlGuid """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlBinary) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlBinary, y: SqlBinary) -> SqlBinary """
        ...

    Null: SqlBinary = ...


class SqlBoolean(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlBoolean(value: bool)
    SqlBoolean(value: int)
    """
    @property
    def ByteValue(self) -> Byte:
        """ Get: ByteValue(self: SqlBoolean) -> Byte """
        ...

    @property
    def IsFalse(self) -> bool:
        """ Get: IsFalse(self: SqlBoolean) -> bool """
        ...

    @property
    def IsTrue(self) -> bool:
        """ Get: IsTrue(self: SqlBoolean) -> bool """
        ...

    @property
    def Value(self) -> bool:
        """ Get: Value(self: SqlBoolean) -> bool """
        ...


    @staticmethod
    def And(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ And(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean
        Equals(self: SqlBoolean, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlBoolean) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ GreaterThan(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEquals(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ GreaterThanOrEquals(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ LessThan(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEquals(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ LessThanOrEquals(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def NotEquals(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ NotEquals(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def OnesComplement(x:SqlBoolean) -> SqlBoolean:
        """ OnesComplement(x: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def Or(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ Or(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlBoolean:
        """ Parse(s: str) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlBoolean) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlBoolean) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlBoolean) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlBoolean) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlBoolean) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlBoolean) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlBoolean) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlBoolean) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlBoolean) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlBoolean) -> str """
        ...

    @staticmethod
    def Xor(x:SqlBoolean, y:SqlBoolean) -> SqlBoolean:
        """ Xor(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SqlBoolean) -> SqlBoolean """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SqlBoolean, y: SqlBoolean) -> SqlBoolean """
        ...

    Null: SqlBoolean = ...
    One: SqlBoolean = ...
    Zero: SqlBoolean = ...


class SqlByte(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlByte(value: Byte) """
    @property
    def Value(self) -> Byte:
        """ Get: Value(self: SqlByte) -> Byte """
        ...


    @staticmethod
    def Add(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Add(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def BitwiseAnd(x:SqlByte, y:SqlByte) -> SqlByte:
        """ BitwiseAnd(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def BitwiseOr(x:SqlByte, y:SqlByte) -> SqlByte:
        """ BitwiseOr(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def Divide(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Divide(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlByte, y: SqlByte) -> SqlBoolean
        Equals(self: SqlByte, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlByte) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlByte, y:SqlByte) -> SqlBoolean:
        """ GreaterThan(x: SqlByte, y: SqlByte) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlByte, y:SqlByte) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlByte, y: SqlByte) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlByte, y:SqlByte) -> SqlBoolean:
        """ LessThan(x: SqlByte, y: SqlByte) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlByte, y:SqlByte) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlByte, y: SqlByte) -> SqlBoolean """
        ...

    @staticmethod
    def Mod(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Mod(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def Modulus(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Modulus(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def Multiply(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Multiply(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def NotEquals(x:SqlByte, y:SqlByte) -> SqlBoolean:
        """ NotEquals(x: SqlByte, y: SqlByte) -> SqlBoolean """
        ...

    @staticmethod
    def OnesComplement(x:SqlByte) -> SqlByte:
        """ OnesComplement(x: SqlByte) -> SqlByte """
        ...

    @staticmethod
    def Parse(s:str) -> SqlByte:
        """ Parse(s: str) -> SqlByte """
        ...

    @staticmethod
    def Subtract(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Subtract(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlByte) -> SqlBoolean """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlByte) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlByte) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlByte) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlByte) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlByte) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlByte) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlByte) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlByte) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlByte) -> str """
        ...

    @staticmethod
    def Xor(x:SqlByte, y:SqlByte) -> SqlByte:
        """ Xor(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SqlByte) -> SqlByte """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SqlByte, y: SqlByte) -> SqlByte """
        ...

    MaxValue: SqlByte = ...
    MinValue: SqlByte = ...
    Null: SqlByte = ...
    Zero: SqlByte = ...


class SqlBytes(IXmlSerializable, INullable, ISerializable): # skipped bases: <type 'object'>
    """
    SqlBytes()
    SqlBytes(buffer: Array[Byte])
    SqlBytes(value: SqlBinary)
    SqlBytes(s: Stream)
    """
    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: SqlBytes) -> Array[Byte] """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: SqlBytes) -> Int64 """
        ...

    @property
    def MaxLength(self) -> Int64:
        """ Get: MaxLength(self: SqlBytes) -> Int64 """
        ...

    @property
    def Null(self) -> SqlBytes:
        """ Get: Null() -> SqlBytes """
        ...

    @property
    def Storage(self) -> StorageState:
        """ Get: Storage(self: SqlBytes) -> StorageState """
        ...

    @property
    def Stream(self) -> Stream:
        """
        Get: Stream(self: SqlBytes) -> Stream
        Set: Stream(self: SqlBytes) = value
        """
        ...

    @property
    def Value(self) -> Array:
        """ Get: Value(self: SqlBytes) -> Array[Byte] """
        ...


    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    def Read(self, offset:Int64, buffer:Array, offsetInBuffer:int, count:int) -> Int64:
        """ Read(self: SqlBytes, offset: Int64, buffer: Array[Byte], offsetInBuffer: int, count: int) -> Int64 """
        ...

    def SetLength(self, value:Int64): # -> 
        """ SetLength(self: SqlBytes, value: Int64) """
        ...

    def SetNull(self): # -> 
        """ SetNull(self: SqlBytes) """
        ...

    def ToSqlBinary(self) -> SqlBinary:
        """ ToSqlBinary(self: SqlBytes) -> SqlBinary """
        ...

    def Write(self, offset:Int64, buffer:Array, offsetInBuffer:int, count:int): # -> 
        """ Write(self: SqlBytes, offset: Int64, buffer: Array[Byte], offsetInBuffer: int, count: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...



class SqlChars(IXmlSerializable, INullable, ISerializable): # skipped bases: <type 'object'>
    """
    SqlChars()
    SqlChars(buffer: Array[Char])
    SqlChars(value: SqlString)
    """
    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: SqlChars) -> Array[Char] """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: SqlChars) -> Int64 """
        ...

    @property
    def MaxLength(self) -> Int64:
        """ Get: MaxLength(self: SqlChars) -> Int64 """
        ...

    @property
    def Null(self) -> SqlChars:
        """ Get: Null() -> SqlChars """
        ...

    @property
    def Storage(self) -> StorageState:
        """ Get: Storage(self: SqlChars) -> StorageState """
        ...

    @property
    def Value(self) -> Array:
        """ Get: Value(self: SqlChars) -> Array[Char] """
        ...


    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    def Read(self, offset:Int64, buffer:Array, offsetInBuffer:int, count:int) -> Int64:
        """ Read(self: SqlChars, offset: Int64, buffer: Array[Char], offsetInBuffer: int, count: int) -> Int64 """
        ...

    def SetLength(self, value:Int64): # -> 
        """ SetLength(self: SqlChars, value: Int64) """
        ...

    def SetNull(self): # -> 
        """ SetNull(self: SqlChars) """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlChars) -> SqlString """
        ...

    def Write(self, offset:Int64, buffer:Array, offsetInBuffer:int, count:int): # -> 
        """ Write(self: SqlChars, offset: Int64, buffer: Array[Char], offsetInBuffer: int, count: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...



class SqlCompareOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlCompareOptions, values: BinarySort (32768), BinarySort2 (16384), IgnoreCase (1), IgnoreKanaType (8), IgnoreNonSpace (2), IgnoreWidth (16), None (0) """
    BinarySort: SqlCompareOptions = ...
    BinarySort2: SqlCompareOptions = ...
    IgnoreCase: SqlCompareOptions = ...
    IgnoreKanaType: SqlCompareOptions = ...
    IgnoreNonSpace: SqlCompareOptions = ...
    IgnoreWidth: SqlCompareOptions = ...
    value__ = ...


class SqlDateTime(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlDateTime(value: DateTime)
    SqlDateTime(year: int, month: int, day: int)
    SqlDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int)
    SqlDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: float)
    SqlDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, bilisecond: int)
    SqlDateTime(dayTicks: int, timeTicks: int)
    """
    @property
    def DayTicks(self) -> int:
        """ Get: DayTicks(self: SqlDateTime) -> int """
        ...

    @property
    def TimeTicks(self) -> int:
        """ Get: TimeTicks(self: SqlDateTime) -> int """
        ...

    @property
    def Value(self) -> DateTime:
        """ Get: Value(self: SqlDateTime) -> DateTime """
        ...


    @staticmethod
    def Add(x:SqlDateTime, t:TimeSpan) -> SqlDateTime:
        """ Add(x: SqlDateTime, t: TimeSpan) -> SqlDateTime """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean
        Equals(self: SqlDateTime, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlDateTime) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlDateTime, y:SqlDateTime) -> SqlBoolean:
        """ GreaterThan(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlDateTime, y:SqlDateTime) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlDateTime, y:SqlDateTime) -> SqlBoolean:
        """ LessThan(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlDateTime, y:SqlDateTime) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean """
        ...

    @staticmethod
    def NotEquals(x:SqlDateTime, y:SqlDateTime) -> SqlBoolean:
        """ NotEquals(x: SqlDateTime, y: SqlDateTime) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlDateTime:
        """ Parse(s: str) -> SqlDateTime """
        ...

    @staticmethod
    def Subtract(x:SqlDateTime, t:TimeSpan) -> SqlDateTime:
        """ Subtract(x: SqlDateTime, t: TimeSpan) -> SqlDateTime """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlDateTime) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlDateTime) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue: SqlDateTime = ...
    MinValue: SqlDateTime = ...
    Null: SqlDateTime = ...
    SQLTicksPerHour: int = ...
    SQLTicksPerMinute: int = ...
    SQLTicksPerSecond: int = ...


class SqlDecimal(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlDecimal(value: Decimal)
    SqlDecimal(value: int)
    SqlDecimal(value: Int64)
    SqlDecimal(bPrecision: Byte, bScale: Byte, fPositive: bool, bits: Array[int])
    SqlDecimal(bPrecision: Byte, bScale: Byte, fPositive: bool, data1: int, data2: int, data3: int, data4: int)
    SqlDecimal(dVal: float)
    """
    @property
    def BinData(self) -> Array:
        """ Get: BinData(self: SqlDecimal) -> Array[Byte] """
        ...

    @property
    def Data(self) -> Array:
        """ Get: Data(self: SqlDecimal) -> Array[int] """
        ...

    @property
    def IsPositive(self) -> bool:
        """ Get: IsPositive(self: SqlDecimal) -> bool """
        ...

    @property
    def Precision(self) -> Byte:
        """ Get: Precision(self: SqlDecimal) -> Byte """
        ...

    @property
    def Scale(self) -> Byte:
        """ Get: Scale(self: SqlDecimal) -> Byte """
        ...

    @property
    def Value(self) -> Decimal:
        """ Get: Value(self: SqlDecimal) -> Decimal """
        ...


    @staticmethod
    def Abs(n:SqlDecimal) -> SqlDecimal:
        """ Abs(n: SqlDecimal) -> SqlDecimal """
        ...

    @staticmethod
    def Add(x:SqlDecimal, y:SqlDecimal) -> SqlDecimal:
        """ Add(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    @staticmethod
    def AdjustScale(n:SqlDecimal, digits:int, fRound:bool) -> SqlDecimal:
        """ AdjustScale(n: SqlDecimal, digits: int, fRound: bool) -> SqlDecimal """
        ...

    @staticmethod
    def Ceiling(n:SqlDecimal) -> SqlDecimal:
        """ Ceiling(n: SqlDecimal) -> SqlDecimal """
        ...

    @staticmethod
    def ConvertToPrecScale(n:SqlDecimal, precision:int, scale:int) -> SqlDecimal:
        """ ConvertToPrecScale(n: SqlDecimal, precision: int, scale: int) -> SqlDecimal """
        ...

    @staticmethod
    def Divide(x:SqlDecimal, y:SqlDecimal) -> SqlDecimal:
        """ Divide(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean
        Equals(self: SqlDecimal, value: object) -> bool
        """
        ...

    @staticmethod
    def Floor(n:SqlDecimal) -> SqlDecimal:
        """ Floor(n: SqlDecimal) -> SqlDecimal """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlDecimal) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlDecimal, y:SqlDecimal) -> SqlBoolean:
        """ GreaterThan(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlDecimal, y:SqlDecimal) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlDecimal, y:SqlDecimal) -> SqlBoolean:
        """ LessThan(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlDecimal, y:SqlDecimal) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean """
        ...

    @staticmethod
    def Multiply(x:SqlDecimal, y:SqlDecimal) -> SqlDecimal:
        """ Multiply(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    @staticmethod
    def NotEquals(x:SqlDecimal, y:SqlDecimal) -> SqlBoolean:
        """ NotEquals(x: SqlDecimal, y: SqlDecimal) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlDecimal:
        """ Parse(s: str) -> SqlDecimal """
        ...

    @staticmethod
    def Power(n:SqlDecimal, exp:float) -> SqlDecimal:
        """ Power(n: SqlDecimal, exp: float) -> SqlDecimal """
        ...

    @staticmethod
    def Round(n:SqlDecimal, position:int) -> SqlDecimal:
        """ Round(n: SqlDecimal, position: int) -> SqlDecimal """
        ...

    @staticmethod
    def Sign(n:SqlDecimal) -> SqlInt32:
        """ Sign(n: SqlDecimal) -> SqlInt32 """
        ...

    @staticmethod
    def Subtract(x:SqlDecimal, y:SqlDecimal) -> SqlDecimal:
        """ Subtract(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    def ToDouble(self) -> float:
        """ ToDouble(self: SqlDecimal) -> float """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlDecimal) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlDecimal) -> SqlByte """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlDecimal) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlDecimal) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlDecimal) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlDecimal) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlDecimal) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlDecimal) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlDecimal) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlDecimal) -> str """
        ...

    @staticmethod
    def Truncate(n:SqlDecimal, position:int) -> SqlDecimal:
        """ Truncate(n: SqlDecimal, position: int) -> SqlDecimal """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlDecimal, y: SqlDecimal) -> SqlDecimal """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxPrecision: Byte = ...
    MaxScale: Byte = ...
    MaxValue: SqlDecimal = ...
    MinValue: SqlDecimal = ...
    Null: SqlDecimal = ...


class SqlDouble(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlDouble(value: float) """
    @property
    def Value(self) -> float:
        """ Get: Value(self: SqlDouble) -> float """
        ...


    @staticmethod
    def Add(x:SqlDouble, y:SqlDouble) -> SqlDouble:
        """ Add(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    @staticmethod
    def Divide(x:SqlDouble, y:SqlDouble) -> SqlDouble:
        """ Divide(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlDouble, y: SqlDouble) -> SqlBoolean
        Equals(self: SqlDouble, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlDouble) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlDouble, y:SqlDouble) -> SqlBoolean:
        """ GreaterThan(x: SqlDouble, y: SqlDouble) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlDouble, y:SqlDouble) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlDouble, y: SqlDouble) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlDouble, y:SqlDouble) -> SqlBoolean:
        """ LessThan(x: SqlDouble, y: SqlDouble) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlDouble, y:SqlDouble) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlDouble, y: SqlDouble) -> SqlBoolean """
        ...

    @staticmethod
    def Multiply(x:SqlDouble, y:SqlDouble) -> SqlDouble:
        """ Multiply(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    @staticmethod
    def NotEquals(x:SqlDouble, y:SqlDouble) -> SqlBoolean:
        """ NotEquals(x: SqlDouble, y: SqlDouble) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlDouble:
        """ Parse(s: str) -> SqlDouble """
        ...

    @staticmethod
    def Subtract(x:SqlDouble, y:SqlDouble) -> SqlDouble:
        """ Subtract(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlDouble) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlDouble) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlDouble) -> SqlDecimal """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlDouble) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlDouble) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlDouble) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlDouble) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlDouble) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlDouble) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlDouble) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(x: SqlDouble) -> float """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(x: SqlDouble) -> float """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlDouble, y: SqlDouble) -> SqlDouble """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue: SqlDouble = ...
    MinValue: SqlDouble = ...
    Null: SqlDouble = ...
    Zero: SqlDouble = ...


class SqlFileStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    SqlFileStream(path: str, transactionContext: Array[Byte], access: FileAccess)
    SqlFileStream(path: str, transactionContext: Array[Byte], access: FileAccess, options: FileOptions, allocationSize: Int64)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlFileStream) -> str """
        ...

    @property
    def TransactionContext(self) -> Array:
        """ Get: TransactionContext(self: SqlFileStream) -> Array[Byte] """
        ...


    def __new__(cls, path:str, transactionContext:Array, access:FileAccess, options:FileOptions = ..., allocationSize:Int64 = ...) -> Self:
        """
        __new__(cls: type, path: str, transactionContext: Array[Byte], access: FileAccess)
        __new__(cls: type, path: str, transactionContext: Array[Byte], access: FileAccess, options: FileOptions, allocationSize: Int64)
        """
        ...


class SqlGuid(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlGuid(value: Array[Byte])
    SqlGuid(s: str)
    SqlGuid(g: Guid)
    SqlGuid(a: int, b: Int16, c: Int16, d: Byte, e: Byte, f: Byte, g: Byte, h: Byte, i: Byte, j: Byte, k: Byte)
    """
    @property
    def Value(self) -> Guid:
        """ Get: Value(self: SqlGuid) -> Guid """
        ...


    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlGuid, y: SqlGuid) -> SqlBoolean
        Equals(self: SqlGuid, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlGuid) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlGuid, y:SqlGuid) -> SqlBoolean:
        """ GreaterThan(x: SqlGuid, y: SqlGuid) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlGuid, y:SqlGuid) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlGuid, y: SqlGuid) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlGuid, y:SqlGuid) -> SqlBoolean:
        """ LessThan(x: SqlGuid, y: SqlGuid) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlGuid, y:SqlGuid) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlGuid, y: SqlGuid) -> SqlBoolean """
        ...

    @staticmethod
    def NotEquals(x:SqlGuid, y:SqlGuid) -> SqlBoolean:
        """ NotEquals(x: SqlGuid, y: SqlGuid) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlGuid:
        """ Parse(s: str) -> SqlGuid """
        ...

    def ToByteArray(self) -> Array:
        """ ToByteArray(self: SqlGuid) -> Array[Byte] """
        ...

    def ToSqlBinary(self) -> SqlBinary:
        """ ToSqlBinary(self: SqlGuid) -> SqlBinary """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlGuid) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlGuid) -> str """
        ...

    Null: SqlGuid = ...


class SqlInt16(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlInt16(value: Int16) """
    @property
    def Value(self) -> Int16:
        """ Get: Value(self: SqlInt16) -> Int16 """
        ...


    @staticmethod
    def Add(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Add(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def BitwiseAnd(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ BitwiseAnd(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def BitwiseOr(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ BitwiseOr(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def Divide(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Divide(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlInt16, y: SqlInt16) -> SqlBoolean
        Equals(self: SqlInt16, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlInt16) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlInt16, y:SqlInt16) -> SqlBoolean:
        """ GreaterThan(x: SqlInt16, y: SqlInt16) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlInt16, y:SqlInt16) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlInt16, y: SqlInt16) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlInt16, y:SqlInt16) -> SqlBoolean:
        """ LessThan(x: SqlInt16, y: SqlInt16) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlInt16, y:SqlInt16) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlInt16, y: SqlInt16) -> SqlBoolean """
        ...

    @staticmethod
    def Mod(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Mod(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def Modulus(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Modulus(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def Multiply(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Multiply(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def NotEquals(x:SqlInt16, y:SqlInt16) -> SqlBoolean:
        """ NotEquals(x: SqlInt16, y: SqlInt16) -> SqlBoolean """
        ...

    @staticmethod
    def OnesComplement(x:SqlInt16) -> SqlInt16:
        """ OnesComplement(x: SqlInt16) -> SqlInt16 """
        ...

    @staticmethod
    def Parse(s:str) -> SqlInt16:
        """ Parse(s: str) -> SqlInt16 """
        ...

    @staticmethod
    def Subtract(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Subtract(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlInt16) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlInt16) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlInt16) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlInt16) -> SqlDouble """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlInt16) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlInt16) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlInt16) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlInt16) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlInt16) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlInt16) -> str """
        ...

    @staticmethod
    def Xor(x:SqlInt16, y:SqlInt16) -> SqlInt16:
        """ Xor(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SqlInt16) -> SqlInt16 """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SqlInt16, y: SqlInt16) -> SqlInt16 """
        ...

    MaxValue: SqlInt16 = ...
    MinValue: SqlInt16 = ...
    Null: SqlInt16 = ...
    Zero: SqlInt16 = ...


class SqlInt32(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlInt32(value: int) """
    @property
    def Value(self) -> int:
        """ Get: Value(self: SqlInt32) -> int """
        ...


    @staticmethod
    def Add(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Add(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def BitwiseAnd(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ BitwiseAnd(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def BitwiseOr(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ BitwiseOr(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def Divide(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Divide(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlInt32, y: SqlInt32) -> SqlBoolean
        Equals(self: SqlInt32, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlInt32) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlInt32, y:SqlInt32) -> SqlBoolean:
        """ GreaterThan(x: SqlInt32, y: SqlInt32) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlInt32, y:SqlInt32) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlInt32, y: SqlInt32) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlInt32, y:SqlInt32) -> SqlBoolean:
        """ LessThan(x: SqlInt32, y: SqlInt32) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlInt32, y:SqlInt32) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlInt32, y: SqlInt32) -> SqlBoolean """
        ...

    @staticmethod
    def Mod(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Mod(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def Modulus(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Modulus(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def Multiply(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Multiply(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def NotEquals(x:SqlInt32, y:SqlInt32) -> SqlBoolean:
        """ NotEquals(x: SqlInt32, y: SqlInt32) -> SqlBoolean """
        ...

    @staticmethod
    def OnesComplement(x:SqlInt32) -> SqlInt32:
        """ OnesComplement(x: SqlInt32) -> SqlInt32 """
        ...

    @staticmethod
    def Parse(s:str) -> SqlInt32:
        """ Parse(s: str) -> SqlInt32 """
        ...

    @staticmethod
    def Subtract(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Subtract(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlInt32) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlInt32) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlInt32) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlInt32) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlInt32) -> SqlInt16 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlInt32) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlInt32) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlInt32) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlInt32) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlInt32) -> str """
        ...

    @staticmethod
    def Xor(x:SqlInt32, y:SqlInt32) -> SqlInt32:
        """ Xor(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: SqlInt32) -> int """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SqlInt32) -> SqlInt32 """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(x: SqlInt32) -> int """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SqlInt32, y: SqlInt32) -> SqlInt32 """
        ...

    MaxValue: SqlInt32 = ...
    MinValue: SqlInt32 = ...
    Null: SqlInt32 = ...
    Zero: SqlInt32 = ...


class SqlInt64(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """ SqlInt64(value: Int64) """
    @property
    def Value(self) -> Int64:
        """ Get: Value(self: SqlInt64) -> Int64 """
        ...


    @staticmethod
    def Add(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Add(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def BitwiseAnd(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ BitwiseAnd(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def BitwiseOr(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ BitwiseOr(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def Divide(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Divide(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlInt64, y: SqlInt64) -> SqlBoolean
        Equals(self: SqlInt64, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlInt64) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlInt64, y:SqlInt64) -> SqlBoolean:
        """ GreaterThan(x: SqlInt64, y: SqlInt64) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlInt64, y:SqlInt64) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlInt64, y: SqlInt64) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlInt64, y:SqlInt64) -> SqlBoolean:
        """ LessThan(x: SqlInt64, y: SqlInt64) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlInt64, y:SqlInt64) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlInt64, y: SqlInt64) -> SqlBoolean """
        ...

    @staticmethod
    def Mod(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Mod(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def Modulus(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Modulus(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def Multiply(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Multiply(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def NotEquals(x:SqlInt64, y:SqlInt64) -> SqlBoolean:
        """ NotEquals(x: SqlInt64, y: SqlInt64) -> SqlBoolean """
        ...

    @staticmethod
    def OnesComplement(x:SqlInt64) -> SqlInt64:
        """ OnesComplement(x: SqlInt64) -> SqlInt64 """
        ...

    @staticmethod
    def Parse(s:str) -> SqlInt64:
        """ Parse(s: str) -> SqlInt64 """
        ...

    @staticmethod
    def Subtract(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Subtract(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlInt64) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlInt64) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlInt64) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlInt64) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlInt64) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlInt64) -> SqlInt32 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlInt64) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlInt64) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlInt64) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlInt64) -> str """
        ...

    @staticmethod
    def Xor(x:SqlInt64, y:SqlInt64) -> SqlInt64:
        """ Xor(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: SqlInt64) -> SqlInt64 """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: SqlInt64, y: SqlInt64) -> SqlInt64 """
        ...

    MaxValue: SqlInt64 = ...
    MinValue: SqlInt64 = ...
    Null: SqlInt64 = ...
    Zero: SqlInt64 = ...


class SqlMoney(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlMoney(value: int)
    SqlMoney(value: Int64)
    SqlMoney(value: Decimal)
    SqlMoney(value: float)
    """
    @property
    def Value(self) -> Decimal:
        """ Get: Value(self: SqlMoney) -> Decimal """
        ...


    @staticmethod
    def Add(x:SqlMoney, y:SqlMoney) -> SqlMoney:
        """ Add(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    @staticmethod
    def Divide(x:SqlMoney, y:SqlMoney) -> SqlMoney:
        """ Divide(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlMoney, y: SqlMoney) -> SqlBoolean
        Equals(self: SqlMoney, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlMoney) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlMoney, y:SqlMoney) -> SqlBoolean:
        """ GreaterThan(x: SqlMoney, y: SqlMoney) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlMoney, y:SqlMoney) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlMoney, y: SqlMoney) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlMoney, y:SqlMoney) -> SqlBoolean:
        """ LessThan(x: SqlMoney, y: SqlMoney) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlMoney, y:SqlMoney) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlMoney, y: SqlMoney) -> SqlBoolean """
        ...

    @staticmethod
    def Multiply(x:SqlMoney, y:SqlMoney) -> SqlMoney:
        """ Multiply(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    @staticmethod
    def NotEquals(x:SqlMoney, y:SqlMoney) -> SqlBoolean:
        """ NotEquals(x: SqlMoney, y: SqlMoney) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlMoney:
        """ Parse(s: str) -> SqlMoney """
        ...

    @staticmethod
    def Subtract(x:SqlMoney, y:SqlMoney) -> SqlMoney:
        """ Subtract(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    def ToDecimal(self) -> Decimal:
        """ ToDecimal(self: SqlMoney) -> Decimal """
        ...

    def ToDouble(self) -> float:
        """ ToDouble(self: SqlMoney) -> float """
        ...

    def ToInt32(self) -> int:
        """ ToInt32(self: SqlMoney) -> int """
        ...

    def ToInt64(self) -> Int64:
        """ ToInt64(self: SqlMoney) -> Int64 """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlMoney) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlMoney) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlMoney) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlMoney) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlMoney) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlMoney) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlMoney) -> SqlInt64 """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlMoney) -> SqlSingle """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlMoney) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlMoney) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlMoney, y: SqlMoney) -> SqlMoney """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue: SqlMoney = ...
    MinValue: SqlMoney = ...
    Null: SqlMoney = ...
    Zero: SqlMoney = ...


class SqlNotFilledException(SqlTypeException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlNotFilledException()
    SqlNotFilledException(message: str)
    SqlNotFilledException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class SqlNullValueException(SqlTypeException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlNullValueException()
    SqlNullValueException(message: str)
    SqlNullValueException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class SqlSingle(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlSingle(value: Single)
    SqlSingle(value: float)
    """
    @property
    def Value(self) -> Single:
        """ Get: Value(self: SqlSingle) -> Single """
        ...


    @staticmethod
    def Add(x:SqlSingle, y:SqlSingle) -> SqlSingle:
        """ Add(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    @staticmethod
    def Divide(x:SqlSingle, y:SqlSingle) -> SqlSingle:
        """ Divide(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlSingle, y: SqlSingle) -> SqlBoolean
        Equals(self: SqlSingle, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlSingle) -> int """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlSingle, y:SqlSingle) -> SqlBoolean:
        """ GreaterThan(x: SqlSingle, y: SqlSingle) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlSingle, y:SqlSingle) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlSingle, y: SqlSingle) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlSingle, y:SqlSingle) -> SqlBoolean:
        """ LessThan(x: SqlSingle, y: SqlSingle) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlSingle, y:SqlSingle) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlSingle, y: SqlSingle) -> SqlBoolean """
        ...

    @staticmethod
    def Multiply(x:SqlSingle, y:SqlSingle) -> SqlSingle:
        """ Multiply(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    @staticmethod
    def NotEquals(x:SqlSingle, y:SqlSingle) -> SqlBoolean:
        """ NotEquals(x: SqlSingle, y: SqlSingle) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> SqlSingle:
        """ Parse(s: str) -> SqlSingle """
        ...

    @staticmethod
    def Subtract(x:SqlSingle, y:SqlSingle) -> SqlSingle:
        """ Subtract(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlSingle) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlSingle) -> SqlByte """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlSingle) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlSingle) -> SqlDouble """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlSingle) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlSingle) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlSingle) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlSingle) -> SqlMoney """
        ...

    def ToSqlString(self) -> SqlString:
        """ ToSqlString(self: SqlSingle) -> SqlString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlSingle) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: SqlSingle, y: SqlSingle) -> SqlSingle """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    MaxValue: SqlSingle = ...
    MinValue: SqlSingle = ...
    Null: SqlSingle = ...
    Zero: SqlSingle = ...


class SqlString(IComparable, IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlString(lcid: int, compareOptions: SqlCompareOptions, data: Array[Byte], index: int, count: int, fUnicode: bool)
    SqlString(lcid: int, compareOptions: SqlCompareOptions, data: Array[Byte], fUnicode: bool)
    SqlString(lcid: int, compareOptions: SqlCompareOptions, data: Array[Byte], index: int, count: int)
    SqlString(lcid: int, compareOptions: SqlCompareOptions, data: Array[Byte])
    SqlString(data: str, lcid: int, compareOptions: SqlCompareOptions)
    SqlString(data: str, lcid: int)
    SqlString(data: str)
    """
    @property
    def CompareInfo(self) -> CompareInfo:
        """ Get: CompareInfo(self: SqlString) -> CompareInfo """
        ...

    @property
    def CultureInfo(self) -> CultureInfo:
        """ Get: CultureInfo(self: SqlString) -> CultureInfo """
        ...

    @property
    def LCID(self) -> int:
        """ Get: LCID(self: SqlString) -> int """
        ...

    @property
    def SqlCompareOptions(self) -> SqlCompareOptions:
        """ Get: SqlCompareOptions(self: SqlString) -> SqlCompareOptions """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: SqlString) -> str """
        ...


    @staticmethod
    def Add(x:SqlString, y:SqlString) -> SqlString:
        """ Add(x: SqlString, y: SqlString) -> SqlString """
        ...

    def Clone(self) -> SqlString:
        """ Clone(self: SqlString) -> SqlString """
        ...

    @staticmethod
    def CompareOptionsFromSqlCompareOptions(compareOptions:SqlCompareOptions) -> CompareOptions:
        """ CompareOptionsFromSqlCompareOptions(compareOptions: SqlCompareOptions) -> CompareOptions """
        ...

    @staticmethod
    def Concat(x:SqlString, y:SqlString) -> SqlString:
        """ Concat(x: SqlString, y: SqlString) -> SqlString """
        ...

    @staticmethod
    def Equals(*__args) -> SqlBoolean:
        """
        Equals(x: SqlString, y: SqlString) -> SqlBoolean
        Equals(self: SqlString, value: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlString) -> int """
        ...

    def GetNonUnicodeBytes(self) -> Array:
        """ GetNonUnicodeBytes(self: SqlString) -> Array[Byte] """
        ...

    def GetUnicodeBytes(self) -> Array:
        """ GetUnicodeBytes(self: SqlString) -> Array[Byte] """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...

    @staticmethod
    def GreaterThan(x:SqlString, y:SqlString) -> SqlBoolean:
        """ GreaterThan(x: SqlString, y: SqlString) -> SqlBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:SqlString, y:SqlString) -> SqlBoolean:
        """ GreaterThanOrEqual(x: SqlString, y: SqlString) -> SqlBoolean """
        ...

    @staticmethod
    def LessThan(x:SqlString, y:SqlString) -> SqlBoolean:
        """ LessThan(x: SqlString, y: SqlString) -> SqlBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:SqlString, y:SqlString) -> SqlBoolean:
        """ LessThanOrEqual(x: SqlString, y: SqlString) -> SqlBoolean """
        ...

    @staticmethod
    def NotEquals(x:SqlString, y:SqlString) -> SqlBoolean:
        """ NotEquals(x: SqlString, y: SqlString) -> SqlBoolean """
        ...

    def ToSqlBoolean(self) -> SqlBoolean:
        """ ToSqlBoolean(self: SqlString) -> SqlBoolean """
        ...

    def ToSqlByte(self) -> SqlByte:
        """ ToSqlByte(self: SqlString) -> SqlByte """
        ...

    def ToSqlDateTime(self) -> SqlDateTime:
        """ ToSqlDateTime(self: SqlString) -> SqlDateTime """
        ...

    def ToSqlDecimal(self) -> SqlDecimal:
        """ ToSqlDecimal(self: SqlString) -> SqlDecimal """
        ...

    def ToSqlDouble(self) -> SqlDouble:
        """ ToSqlDouble(self: SqlString) -> SqlDouble """
        ...

    def ToSqlGuid(self) -> SqlGuid:
        """ ToSqlGuid(self: SqlString) -> SqlGuid """
        ...

    def ToSqlInt16(self) -> SqlInt16:
        """ ToSqlInt16(self: SqlString) -> SqlInt16 """
        ...

    def ToSqlInt32(self) -> SqlInt32:
        """ ToSqlInt32(self: SqlString) -> SqlInt32 """
        ...

    def ToSqlInt64(self) -> SqlInt64:
        """ ToSqlInt64(self: SqlString) -> SqlInt64 """
        ...

    def ToSqlMoney(self) -> SqlMoney:
        """ ToSqlMoney(self: SqlString) -> SqlMoney """
        ...

    def ToSqlSingle(self) -> SqlSingle:
        """ ToSqlSingle(self: SqlString) -> SqlSingle """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlString) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: SqlString, y: SqlString) -> SqlString """
        ...

    BinarySort: int = ...
    BinarySort2: int = ...
    IgnoreCase: int = ...
    IgnoreKanaType: int = ...
    IgnoreNonSpace: int = ...
    IgnoreWidth: int = ...
    Null: SqlString = ...


class SqlTruncateException(SqlTypeException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlTruncateException()
    SqlTruncateException(message: str)
    SqlTruncateException(message: str, e: Exception)
    """
    SerializeObjectState = ...


class SqlTypesSchemaImporterExtensionHelper(SchemaImporterExtension): # skipped bases: <type 'object'>
    """
    SqlTypesSchemaImporterExtensionHelper(name: str, targetNamespace: str, references: Array[str], namespaceImports: Array[CodeNamespaceImport], destinationType: str, direct: bool)
    SqlTypesSchemaImporterExtensionHelper(name: str, destinationType: str)
    SqlTypesSchemaImporterExtensionHelper(name: str, destinationType: str, direct: bool)
    """
    def __new__(cls, name:str, *__args:str) -> Self:
        """
        __new__(cls: type, name: str, targetNamespace: str, references: Array[str], namespaceImports: Array[CodeNamespaceImport], destinationType: str, direct: bool)
        __new__(cls: type, name: str, destinationType: str)
        __new__(cls: type, name: str, destinationType: str, direct: bool)
        """
        ...

    SqlTypesNamespace: str = ...


class SqlXml(IXmlSerializable, INullable): # skipped bases: <type 'object'>
    """
    SqlXml()
    SqlXml(value: XmlReader)
    SqlXml(value: Stream)
    """
    @property
    def Null(self) -> SqlXml:
        """ Get: Null() -> SqlXml """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: SqlXml) -> str """
        ...


    def CreateReader(self) -> XmlReader:
        """ CreateReader(self: SqlXml) -> XmlReader """
        ...

    @staticmethod
    def GetXsdType(schemaSet:XmlSchemaSet) -> XmlQualifiedName:
        """ GetXsdType(schemaSet: XmlSchemaSet) -> XmlQualifiedName """
        ...



class StorageState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StorageState, values: Buffer (0), Stream (1), UnmanagedBuffer (2) """
    Buffer: StorageState = ...
    Stream: StorageState = ...
    UnmanagedBuffer: StorageState = ...
    value__ = ...


class TypeBigIntSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeBigIntSchemaImporterExtension() """
    pass

class TypeBinarySchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeBinarySchemaImporterExtension() """
    pass

class TypeBitSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeBitSchemaImporterExtension() """
    pass

class TypeCharSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeCharSchemaImporterExtension() """
    pass

class TypeDateTimeSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeDateTimeSchemaImporterExtension() """
    pass

class TypeDecimalSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeDecimalSchemaImporterExtension() """
    pass

class TypeFloatSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeFloatSchemaImporterExtension() """
    pass

class TypeIntSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeIntSchemaImporterExtension() """
    pass

class TypeMoneySchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeMoneySchemaImporterExtension() """
    pass

class TypeNCharSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeNCharSchemaImporterExtension() """
    pass

class TypeNTextSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeNTextSchemaImporterExtension() """
    pass

class TypeNumericSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeNumericSchemaImporterExtension() """
    pass

class TypeNVarCharSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeNVarCharSchemaImporterExtension() """
    pass

class TypeRealSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeRealSchemaImporterExtension() """
    pass

class TypeSmallDateTimeSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeSmallDateTimeSchemaImporterExtension() """
    pass

class TypeSmallIntSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeSmallIntSchemaImporterExtension() """
    pass

class TypeSmallMoneySchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeSmallMoneySchemaImporterExtension() """
    pass

class TypeTextSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeTextSchemaImporterExtension() """
    pass

class TypeTinyIntSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeTinyIntSchemaImporterExtension() """
    pass

class TypeUniqueIdentifierSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeUniqueIdentifierSchemaImporterExtension() """
    pass

class TypeVarBinarySchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeVarBinarySchemaImporterExtension() """
    pass

class TypeVarCharSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeVarCharSchemaImporterExtension() """
    pass

class TypeVarImageSchemaImporterExtension(SqlTypesSchemaImporterExtensionHelper): # skipped bases: <type 'object'>
    """ TypeVarImageSchemaImporterExtension() """
    pass

