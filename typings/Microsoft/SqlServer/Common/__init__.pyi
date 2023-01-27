# encoding: utf-8
# module Microsoft.SqlServer.Common calls itself Common
# from Microsoft.SqlServer.SString, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Char, ICloneable, IComparable, IDisposable, IntPtr

from System.Globalization import CultureInfo

from System.Security import SecureString

from System.Xml.Serialization import IXmlSerializable


# no functions
# classes

class SqlSecureString(IComparable, ICloneable, IDisposable, IXmlSerializable): # skipped bases: <type 'object'>
    """
    SqlSecureString()
    SqlSecureString(str: str)
    SqlSecureString(secureString: SecureString)
    SqlSecureString(bstr: IntPtr, length: int)
    """
    @property
    def Empty(self) -> SqlSecureString:
        """ Get: Empty() -> SqlSecureString """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: SqlSecureString) -> int """
        ...


    @staticmethod
    def Compare(strA:SqlSecureString, *__args:SqlSecureString) -> int:
        """
        Compare(strA: SqlSecureString, strB: SqlSecureString) -> int
        Compare(strA: SqlSecureString, strB: SqlSecureString, ignoreCase: bool) -> int
        Compare(strA: SqlSecureString, strB: SqlSecureString, comparisonType: StringComparison) -> int
        Compare(strA: SqlSecureString, strB: SqlSecureString, ignoreCase: bool, cultureInfo: CultureInfo) -> int
        Compare(strA: SqlSecureString, indexA: int, strB: SqlSecureString, indexB: int, length: int) -> int
        Compare(strA: SqlSecureString, indexA: int, strB: SqlSecureString, indexB: int, length: int, ignoreCase: bool) -> int
        Compare(strA: SqlSecureString, indexA: int, strB: SqlSecureString, indexB: int, length: int, comparisonType: StringComparison) -> int
        Compare(strA: SqlSecureString, indexA: int, strB: SqlSecureString, indexB: int, length: int, ignoreCase: bool, cultureInfo: CultureInfo) -> int
        """
        ...

    @staticmethod
    def CompareOrdinal(strA:SqlSecureString, *__args:SqlSecureString) -> int:
        """
        CompareOrdinal(strA: SqlSecureString, strB: SqlSecureString) -> int
        CompareOrdinal(strA: SqlSecureString, indexA: int, strB: SqlSecureString, indexB: int, length: int) -> int
        """
        ...

    @staticmethod
    def Concat(*__args:object) -> SqlSecureString:
        """
        Concat(obj: object) -> SqlSecureString
        Concat(*args: Array[object]) -> SqlSecureString
        """
        ...

    def Contains(self, value:str) -> bool:
        """
        Contains(self: SqlSecureString, value: str) -> bool
        Contains(self: SqlSecureString, value: SqlSecureString) -> bool
        """
        ...

    def Copy(self) -> SqlSecureString:
        """ Copy(self: SqlSecureString) -> SqlSecureString """
        ...

    def EndsWith(self, value:SqlSecureString, ignoreCase:bool = ..., cultureInfo:CultureInfo = ...) -> bool:
        """
        EndsWith(self: SqlSecureString, value: SqlSecureString) -> bool
        EndsWith(self: SqlSecureString, value: SqlSecureString, ignoreCase: bool, cultureInfo: CultureInfo) -> bool
        """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: SqlSecureString, obj: object) -> bool
        Equals(self: SqlSecureString, other: SqlSecureString) -> bool
        Equals(strA: SqlSecureString, strB: SqlSecureString) -> bool
        Equals(self: SqlSecureString, other: SqlSecureString, comparisonType: StringComparison) -> bool
        Equals(strA: SqlSecureString, strB: SqlSecureString, comparisonType: StringComparison) -> bool
        """
        ...

    @staticmethod
    def Format(*__args) -> SqlSecureString:
        """
        Format(format: str, *arguments: Array[object]) -> SqlSecureString
        Format(formatProvider: IFormatProvider, format: str, *arguments: Array[object]) -> SqlSecureString
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlSecureString) -> int """
        ...

    def IndexOf(self, value:Char, startIndex:int = ..., count:int = ...) -> int:
        """
        IndexOf(self: SqlSecureString, value: Char) -> int
        IndexOf(self: SqlSecureString, value: str) -> int
        IndexOf(self: SqlSecureString, value: Char, startIndex: int) -> int
        IndexOf(self: SqlSecureString, value: str, startIndex: int) -> int
        IndexOf(self: SqlSecureString, value: Char, startIndex: int, count: int) -> int
        IndexOf(self: SqlSecureString, value: str, startIndex: int, count: int) -> int
        """
        ...

    def IndexOfAny(self, anyOf:Array, startIndex:int = ..., count:int = ...) -> int:
        """
        IndexOfAny(self: SqlSecureString, anyOf: Array[Char]) -> int
        IndexOfAny(self: SqlSecureString, anyOf: Array[Char], startIndex: int) -> int
        IndexOfAny(self: SqlSecureString, anyOf: Array[Char], startIndex: int, count: int) -> int
        """
        ...

    def Insert(self, startIndex:int, value:SqlSecureString) -> SqlSecureString:
        """
        Insert(self: SqlSecureString, startIndex: int, value: SqlSecureString) -> SqlSecureString
        Insert(self: SqlSecureString, startIndex: int, value: str) -> SqlSecureString
        """
        ...

    @staticmethod
    def Join(separator:object, value:Array, startIndex:int = ..., count:int = ...) -> SqlSecureString:
        """
        Join(separator: object, value: Array[object]) -> SqlSecureString
        Join(separator: object, value: Array[object], startIndex: int, count: int) -> SqlSecureString
        """
        ...

    def LastIndexOf(self, value:Char, startIndex:int = ..., count:int = ...) -> int:
        """
        LastIndexOf(self: SqlSecureString, value: Char) -> int
        LastIndexOf(self: SqlSecureString, value: str) -> int
        LastIndexOf(self: SqlSecureString, value: Char, startIndex: int) -> int
        LastIndexOf(self: SqlSecureString, value: str, startIndex: int) -> int
        LastIndexOf(self: SqlSecureString, value: Char, startIndex: int, count: int) -> int
        LastIndexOf(self: SqlSecureString, value: str, startIndex: int, count: int) -> int
        """
        ...

    def LastIndexOfAny(self, anyOf:Array, startIndex:int = ..., count:int = ...) -> int:
        """
        LastIndexOfAny(self: SqlSecureString, anyOf: Array[Char]) -> int
        LastIndexOfAny(self: SqlSecureString, anyOf: Array[Char], startIndex: int) -> int
        LastIndexOfAny(self: SqlSecureString, anyOf: Array[Char], startIndex: int, count: int) -> int
        """
        ...

    def PadLeft(self, totalWidth:int, paddingChar:Char = ...) -> SqlSecureString:
        """
        PadLeft(self: SqlSecureString, totalWidth: int) -> SqlSecureString
        PadLeft(self: SqlSecureString, totalWidth: int, paddingChar: Char) -> SqlSecureString
        """
        ...

    def PadRight(self, totalWidth:int, paddingChar:Char = ...) -> SqlSecureString:
        """
        PadRight(self: SqlSecureString, totalWidth: int) -> SqlSecureString
        PadRight(self: SqlSecureString, totalWidth: int, paddingChar: Char) -> SqlSecureString
        """
        ...

    def Remove(self, startIndex:int, count:int = ...) -> SqlSecureString:
        """
        Remove(self: SqlSecureString, startIndex: int) -> SqlSecureString
        Remove(self: SqlSecureString, startIndex: int, count: int) -> SqlSecureString
        """
        ...

    def Replace(self, *__args) -> SqlSecureString:
        """
        Replace(self: SqlSecureString, oldChar: Char, newChar: Char) -> SqlSecureString
        Replace(self: SqlSecureString, oldValue: SqlSecureString, newValue: SqlSecureString) -> SqlSecureString
        """
        ...

    def Split(self, separator:Array, *__args:int) -> Array:
        """
        Split(self: SqlSecureString, separator: Array[Char]) -> Array[SqlSecureString]
        Split(self: SqlSecureString, separator: Array[Char], count: int) -> Array[SqlSecureString]
        Split(self: SqlSecureString, separator: Array[Char], options: StringSplitOptions) -> Array[SqlSecureString]
        Split(self: SqlSecureString, separator: Array[Char], count: int, options: StringSplitOptions) -> Array[SqlSecureString]
        Split(self: SqlSecureString, separator: Array[str], options: StringSplitOptions) -> Array[SqlSecureString]
        Split(self: SqlSecureString, separator: Array[str], count: int, options: StringSplitOptions) -> Array[SqlSecureString]
        """
        ...

    def StartsWith(self, value:SqlSecureString, ignoreCase:bool = ..., culture:CultureInfo = ...) -> bool:
        """
        StartsWith(self: SqlSecureString, value: SqlSecureString) -> bool
        StartsWith(self: SqlSecureString, value: SqlSecureString, ignoreCase: bool, culture: CultureInfo) -> bool
        """
        ...

    @staticmethod
    def StringArrayToSqlSecureStringArray(array:Array) -> Array:
        """ StringArrayToSqlSecureStringArray(array: Array[str]) -> Array[SqlSecureString] """
        ...

    def Substring(self, startIndex:int, length:int = ...) -> SqlSecureString:
        """
        Substring(self: SqlSecureString, startIndex: int) -> SqlSecureString
        Substring(self: SqlSecureString, startIndex: int, length: int) -> SqlSecureString
        """
        ...

    def ToBstr(self) -> IntPtr:
        """ ToBstr(self: SqlSecureString) -> IntPtr """
        ...

    def ToLower(self, culture:CultureInfo = ...) -> SqlSecureString:
        """
        ToLower(self: SqlSecureString) -> SqlSecureString
        ToLower(self: SqlSecureString, culture: CultureInfo) -> SqlSecureString
        """
        ...

    def ToLowerInvariant(self) -> SqlSecureString:
        """ ToLowerInvariant(self: SqlSecureString) -> SqlSecureString """
        ...

    def ToSecureString(self) -> SecureString:
        """ ToSecureString(self: SqlSecureString) -> SecureString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlSecureString) -> str """
        ...

    def ToUpper(self, culture:CultureInfo = ...) -> SqlSecureString:
        """
        ToUpper(self: SqlSecureString) -> SqlSecureString
        ToUpper(self: SqlSecureString, culture: CultureInfo) -> SqlSecureString
        """
        ...

    def ToUpperInvariant(self) -> SqlSecureString:
        """ ToUpperInvariant(self: SqlSecureString) -> SqlSecureString """
        ...

    def Trim(self, trimChars:Array = ...) -> SqlSecureString:
        """
        Trim(self: SqlSecureString) -> SqlSecureString
        Trim(self: SqlSecureString, trimChars: Array[Char]) -> SqlSecureString
        """
        ...

    def TrimEnd(self, trimChars:Array) -> SqlSecureString:
        """ TrimEnd(self: SqlSecureString, trimChars: Array[Char]) -> SqlSecureString """
        ...

    def TrimStart(self, trimChars:Array) -> SqlSecureString:
        """ TrimStart(self: SqlSecureString, trimChars: Array[Char]) -> SqlSecureString """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(strA: SqlSecureString, strB: SqlSecureString) -> SqlSecureString """
        ...



