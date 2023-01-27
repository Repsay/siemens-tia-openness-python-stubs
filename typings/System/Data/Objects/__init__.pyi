# encoding: utf-8
# module System.Data.Objects calls itself Objects
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, Char, DateTime, Decimal, Enum, 
    EventArgs, Guid, IAsyncResult, IDisposable, Int16, Int64, 
    MulticastDelegate, Nullable, Single, Type)

from System.Collections import ICollection, IEnumerable

from System.Data import (EntityKey, EntityState, IDataRecord, 
    IExtendedDataRecord)

from System.Data.Common import DbConnection, DbDataReader, DbDataRecord

from System.Data.Linq import EntitySet

from System.Data.Metadata.Edm import (EntitySetBase, MetadataWorkspace, 
    TypeUsage)

from System.Data.Objects.DataClasses import (IEntityChangeTracker, 
    IEntityWithKey, RelationshipManager)

from System.Linq import IQueryable

from System.Linq.Expressions import Expression

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    DataContractResolver, Func, IEntityStateEntry, IEntityStateManager, T, 
    TEntity, field#)
"""

# no functions
# classes

class CompiledQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Compile(query:Expression): # -> Func
        """
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TArg15, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TArg14, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TArg13, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TArg12, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TArg11, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TArg10, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TArg9, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TArg8, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TArg7, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TArg6, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TArg5, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TArg4, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TArg4, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TArg4, TResult]
        Compile[(TArg0, TArg1, TArg2, TArg3, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TArg3, TResult]]) -> Func[TArg0, TArg1, TArg2, TArg3, TResult]
        Compile[(TArg0, TArg1, TArg2, TResult)](query: Expression[Func[TArg0, TArg1, TArg2, TResult]]) -> Func[TArg0, TArg1, TArg2, TResult]
        Compile[(TArg0, TArg1, TResult)](query: Expression[Func[TArg0, TArg1, TResult]]) -> Func[TArg0, TArg1, TResult]
        Compile[(TArg0, TResult)](query: Expression[Func[TArg0, TResult]]) -> Func[TArg0, TResult]
        """
        ...


class DbUpdatableDataRecord(IExtendedDataRecord, DbDataRecord): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDataRecord'>, <type 'object'>
    """ no doc """
    def GetRecordValue(self, *args): #cannot find CLR method
        """ GetRecordValue(self: DbUpdatableDataRecord, ordinal: int) -> object """
        ...

    def SetBoolean(self, ordinal:int, value:bool): # -> 
        """ SetBoolean(self: DbUpdatableDataRecord, ordinal: int, value: bool) """
        ...

    def SetByte(self, ordinal:int, value:Byte): # -> 
        """ SetByte(self: DbUpdatableDataRecord, ordinal: int, value: Byte) """
        ...

    def SetChar(self, ordinal:int, value:Char): # -> 
        """ SetChar(self: DbUpdatableDataRecord, ordinal: int, value: Char) """
        ...

    def SetDataRecord(self, ordinal:int, value:IDataRecord): # -> 
        """ SetDataRecord(self: DbUpdatableDataRecord, ordinal: int, value: IDataRecord) """
        ...

    def SetDateTime(self, ordinal:int, value:DateTime): # -> 
        """ SetDateTime(self: DbUpdatableDataRecord, ordinal: int, value: DateTime) """
        ...

    def SetDBNull(self, ordinal:int): # -> 
        """ SetDBNull(self: DbUpdatableDataRecord, ordinal: int) """
        ...

    def SetDecimal(self, ordinal:int, value:Decimal): # -> 
        """ SetDecimal(self: DbUpdatableDataRecord, ordinal: int, value: Decimal) """
        ...

    def SetDouble(self, ordinal:int, value:float): # -> 
        """ SetDouble(self: DbUpdatableDataRecord, ordinal: int, value: float) """
        ...

    def SetFloat(self, ordinal:int, value:Single): # -> 
        """ SetFloat(self: DbUpdatableDataRecord, ordinal: int, value: Single) """
        ...

    def SetGuid(self, ordinal:int, value:Guid): # -> 
        """ SetGuid(self: DbUpdatableDataRecord, ordinal: int, value: Guid) """
        ...

    def SetInt16(self, ordinal:int, value:Int16): # -> 
        """ SetInt16(self: DbUpdatableDataRecord, ordinal: int, value: Int16) """
        ...

    def SetInt32(self, ordinal:int, value:int): # -> 
        """ SetInt32(self: DbUpdatableDataRecord, ordinal: int, value: int) """
        ...

    def SetInt64(self, ordinal:int, value:Int64): # -> 
        """ SetInt64(self: DbUpdatableDataRecord, ordinal: int, value: Int64) """
        ...

    def SetRecordValue(self, *args): #cannot find CLR method
        """ SetRecordValue(self: DbUpdatableDataRecord, ordinal: int, value: object) """
        ...

    def SetString(self, ordinal:int, value:str): # -> 
        """ SetString(self: DbUpdatableDataRecord, ordinal: int, value: str) """
        ...

    def SetValue(self, ordinal:int, value:object): # -> 
        """ SetValue(self: DbUpdatableDataRecord, ordinal: int, value: object) """
        ...

    def SetValues(self, values:Array) -> int:
        """ SetValues(self: DbUpdatableDataRecord, *values: Array[object]) -> int """
        ...


class CurrentValueRecord(DbUpdatableDataRecord): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDataRecord'>, <type 'IExtendedDataRecord'>, <type 'object'>
    """ no doc """
    pass

class EntityFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddDays(dateValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddDays(dateValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddDays(dateValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        """
        ...

    @staticmethod
    def AddHours(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddHours(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddHours(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddHours(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddMicroseconds(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddMicroseconds(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddMicroseconds(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddMicroseconds(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddMilliseconds(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddMilliseconds(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddMilliseconds(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddMilliseconds(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddMinutes(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddMinutes(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddMinutes(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddMinutes(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddMonths(dateValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddMonths(dateValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddMonths(dateValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        """
        ...

    @staticmethod
    def AddNanoseconds(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddNanoseconds(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddNanoseconds(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddNanoseconds(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddSeconds(timeValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddSeconds(timeValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddSeconds(timeValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        AddSeconds(timeValue: Nullable[TimeSpan], addValue: Nullable[int]) -> Nullable[TimeSpan]
        """
        ...

    @staticmethod
    def AddYears(dateValue:Nullable, addValue:Nullable) -> Nullable:
        """
        AddYears(dateValue: Nullable[DateTimeOffset], addValue: Nullable[int]) -> Nullable[DateTimeOffset]
        AddYears(dateValue: Nullable[DateTime], addValue: Nullable[int]) -> Nullable[DateTime]
        """
        ...

    @staticmethod
    def AsNonUnicode(value:str) -> str:
        """ AsNonUnicode(value: str) -> str """
        ...

    @staticmethod
    def AsUnicode(value:str) -> str:
        """ AsUnicode(value: str) -> str """
        ...

    @staticmethod
    def CreateDateTime(year:Nullable, month:Nullable, day:Nullable, hour:Nullable, minute:Nullable, second:Nullable) -> Nullable:
        """ CreateDateTime(year: Nullable[int], month: Nullable[int], day: Nullable[int], hour: Nullable[int], minute: Nullable[int], second: Nullable[float]) -> Nullable[DateTime] """
        ...

    @staticmethod
    def CreateDateTimeOffset(year:Nullable, month:Nullable, day:Nullable, hour:Nullable, minute:Nullable, second:Nullable, timeZoneOffset:Nullable) -> Nullable:
        """ CreateDateTimeOffset(year: Nullable[int], month: Nullable[int], day: Nullable[int], hour: Nullable[int], minute: Nullable[int], second: Nullable[float], timeZoneOffset: Nullable[int]) -> Nullable[DateTimeOffset] """
        ...

    @staticmethod
    def CreateTime(hour:Nullable, minute:Nullable, second:Nullable) -> Nullable:
        """ CreateTime(hour: Nullable[int], minute: Nullable[int], second: Nullable[float]) -> Nullable[TimeSpan] """
        ...

    @staticmethod
    def DiffDays(dateValue1:Nullable, dateValue2:Nullable) -> Nullable:
        """
        DiffDays(dateValue1: Nullable[DateTimeOffset], dateValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffDays(dateValue1: Nullable[DateTime], dateValue2: Nullable[DateTime]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffHours(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffHours(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffHours(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffHours(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffMicroseconds(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffMicroseconds(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffMicroseconds(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffMicroseconds(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffMilliseconds(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffMilliseconds(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffMilliseconds(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffMilliseconds(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffMinutes(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffMinutes(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffMinutes(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffMinutes(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffMonths(dateValue1:Nullable, dateValue2:Nullable) -> Nullable:
        """
        DiffMonths(dateValue1: Nullable[DateTimeOffset], dateValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffMonths(dateValue1: Nullable[DateTime], dateValue2: Nullable[DateTime]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffNanoseconds(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffNanoseconds(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffNanoseconds(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffNanoseconds(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffSeconds(timeValue1:Nullable, timeValue2:Nullable) -> Nullable:
        """
        DiffSeconds(timeValue1: Nullable[DateTimeOffset], timeValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffSeconds(timeValue1: Nullable[DateTime], timeValue2: Nullable[DateTime]) -> Nullable[int]
        DiffSeconds(timeValue1: Nullable[TimeSpan], timeValue2: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DiffYears(dateValue1:Nullable, dateValue2:Nullable) -> Nullable:
        """
        DiffYears(dateValue1: Nullable[DateTimeOffset], dateValue2: Nullable[DateTimeOffset]) -> Nullable[int]
        DiffYears(dateValue1: Nullable[DateTime], dateValue2: Nullable[DateTime]) -> Nullable[int]
        """
        ...

    @staticmethod
    def GetTotalOffsetMinutes(dateTimeOffsetArgument:Nullable) -> Nullable:
        """ GetTotalOffsetMinutes(dateTimeOffsetArgument: Nullable[DateTimeOffset]) -> Nullable[int] """
        ...

    @staticmethod
    def Left(stringArgument:str, length:Nullable) -> str:
        """ Left(stringArgument: str, length: Nullable[Int64]) -> str """
        ...

    @staticmethod
    def Reverse(stringArgument:str) -> str:
        """ Reverse(stringArgument: str) -> str """
        ...

    @staticmethod
    def Right(stringArgument:str, length:Nullable) -> str:
        """ Right(stringArgument: str, length: Nullable[Int64]) -> str """
        ...

    @staticmethod
    def StandardDeviation(collection:IEnumerable) -> Nullable:
        """
        StandardDeviation(collection: IEnumerable[Decimal]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[Nullable[Decimal]]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[float]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[Nullable[float]]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[int]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[Nullable[int]]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[Int64]) -> Nullable[float]
        StandardDeviation(collection: IEnumerable[Nullable[Int64]]) -> Nullable[float]
        """
        ...

    @staticmethod
    def StandardDeviationP(collection:IEnumerable) -> Nullable:
        """
        StandardDeviationP(collection: IEnumerable[Decimal]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[Nullable[Decimal]]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[float]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[Nullable[float]]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[int]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[Nullable[int]]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[Int64]) -> Nullable[float]
        StandardDeviationP(collection: IEnumerable[Nullable[Int64]]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Truncate(value:Nullable, digits:Nullable) -> Nullable:
        """
        Truncate(value: Nullable[float], digits: Nullable[int]) -> Nullable[float]
        Truncate(value: Nullable[Decimal], digits: Nullable[int]) -> Nullable[Decimal]
        """
        ...

    @staticmethod
    def TruncateTime(dateValue:Nullable) -> Nullable:
        """
        TruncateTime(dateValue: Nullable[DateTimeOffset]) -> Nullable[DateTimeOffset]
        TruncateTime(dateValue: Nullable[DateTime]) -> Nullable[DateTime]
        """
        ...

    @staticmethod
    def Var(collection:IEnumerable) -> Nullable:
        """
        Var(collection: IEnumerable[Decimal]) -> Nullable[float]
        Var(collection: IEnumerable[Nullable[Decimal]]) -> Nullable[float]
        Var(collection: IEnumerable[float]) -> Nullable[float]
        Var(collection: IEnumerable[Nullable[float]]) -> Nullable[float]
        Var(collection: IEnumerable[int]) -> Nullable[float]
        Var(collection: IEnumerable[Nullable[int]]) -> Nullable[float]
        Var(collection: IEnumerable[Int64]) -> Nullable[float]
        Var(collection: IEnumerable[Nullable[Int64]]) -> Nullable[float]
        """
        ...

    @staticmethod
    def VarP(collection:IEnumerable) -> Nullable:
        """
        VarP(collection: IEnumerable[Decimal]) -> Nullable[float]
        VarP(collection: IEnumerable[Nullable[Decimal]]) -> Nullable[float]
        VarP(collection: IEnumerable[float]) -> Nullable[float]
        VarP(collection: IEnumerable[Nullable[float]]) -> Nullable[float]
        VarP(collection: IEnumerable[int]) -> Nullable[float]
        VarP(collection: IEnumerable[Nullable[int]]) -> Nullable[float]
        VarP(collection: IEnumerable[Int64]) -> Nullable[float]
        VarP(collection: IEnumerable[Nullable[Int64]]) -> Nullable[float]
        """
        ...

    __all__: list = ...


class IObjectSet(IQueryable): # skipped bases: <type 'IEnumerable[TEntity]'>, <type 'IEnumerable'>, <type 'IQueryable'>, <type 'object'>
    """ no doc """
    def AddObject(self, entity): # ->  # Not found arg types: {'entity': 'TEntity'}
        """ AddObject(self: IObjectSet[TEntity], entity: TEntity) """
        ...

    def Attach(self, entity): # ->  # Not found arg types: {'entity': 'TEntity'}
        """ Attach(self: IObjectSet[TEntity], entity: TEntity) """
        ...

    def DeleteObject(self, entity): # ->  # Not found arg types: {'entity': 'TEntity'}
        """ DeleteObject(self: IObjectSet[TEntity], entity: TEntity) """
        ...

    def Detach(self, entity): # ->  # Not found arg types: {'entity': 'TEntity'}
        """ Detach(self: IObjectSet[TEntity], entity: TEntity) """
        ...


class MergeOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MergeOption, values: AppendOnly (0), NoTracking (3), OverwriteChanges (1), PreserveChanges (2) """
    AppendOnly: MergeOption = ...
    NoTracking: MergeOption = ...
    OverwriteChanges: MergeOption = ...
    PreserveChanges: MergeOption = ...
    value__ = ...


class ObjectContext(IDisposable): # skipped bases: <type 'object'>
    """
    ObjectContext(connection: EntityConnection)
    ObjectContext(connectionString: str)
    """
    @property
    def CommandTimeout(self) -> Nullable:
        """
        Get: CommandTimeout(self: ObjectContext) -> Nullable[int]
        Set: CommandTimeout(self: ObjectContext) = value
        """
        ...

    @property
    def Connection(self) -> DbConnection:
        """ Get: Connection(self: ObjectContext) -> DbConnection """
        ...

    @property
    def ContextOptions(self) -> ObjectContextOptions:
        """ Get: ContextOptions(self: ObjectContext) -> ObjectContextOptions """
        ...

    @property
    def DefaultContainerName(self) -> str:
        """
        Get: DefaultContainerName(self: ObjectContext) -> str
        Set: DefaultContainerName(self: ObjectContext) = value
        """
        ...

    @property
    def MetadataWorkspace(self) -> MetadataWorkspace:
        """ Get: MetadataWorkspace(self: ObjectContext) -> MetadataWorkspace """
        ...

    @property
    def ObjectStateManager(self) -> ObjectStateManager:
        """ Get: ObjectStateManager(self: ObjectContext) -> ObjectStateManager """
        ...

    @property
    def QueryProvider(self):
        ...


    def AcceptAllChanges(self): # -> 
        """ AcceptAllChanges(self: ObjectContext) """
        ...

    def AddObject(self, entitySetName:str, entity:object): # -> 
        """ AddObject(self: ObjectContext, entitySetName: str, entity: object) """
        ...

    def ApplyCurrentValues(self, entitySetName:str, currentEntity): # -> TEntity # Not found arg types: {'currentEntity': 'TEntity'}
        """ ApplyCurrentValues[TEntity](self: ObjectContext, entitySetName: str, currentEntity: TEntity) -> TEntity """
        ...

    def ApplyOriginalValues(self, entitySetName:str, originalEntity): # -> TEntity # Not found arg types: {'originalEntity': 'TEntity'}
        """ ApplyOriginalValues[TEntity](self: ObjectContext, entitySetName: str, originalEntity: TEntity) -> TEntity """
        ...

    def ApplyPropertyChanges(self, entitySetName:str, changed:object): # -> 
        """ ApplyPropertyChanges(self: ObjectContext, entitySetName: str, changed: object) """
        ...

    def Attach(self, entity:IEntityWithKey): # -> 
        """ Attach(self: ObjectContext, entity: IEntityWithKey) """
        ...

    def AttachTo(self, entitySetName:str, entity:object): # -> 
        """ AttachTo(self: ObjectContext, entitySetName: str, entity: object) """
        ...

    def CreateDatabase(self): # -> 
        """ CreateDatabase(self: ObjectContext) """
        ...

    def CreateDatabaseScript(self) -> str:
        """ CreateDatabaseScript(self: ObjectContext) -> str """
        ...

    def CreateEntityKey(self, entitySetName:str, entity:object) -> EntityKey:
        """ CreateEntityKey(self: ObjectContext, entitySetName: str, entity: object) -> EntityKey """
        ...

    def CreateObject(self): # -> T
        """ CreateObject[T](self: ObjectContext) -> T """
        ...

    def CreateObjectSet(self, entitySetName:str = ...) -> ObjectSet:
        """
        CreateObjectSet[TEntity](self: ObjectContext) -> ObjectSet[TEntity]
        CreateObjectSet[TEntity](self: ObjectContext, entitySetName: str) -> ObjectSet[TEntity]
        """
        ...

    def CreateProxyTypes(self, types:IEnumerable): # -> 
        """ CreateProxyTypes(self: ObjectContext, types: IEnumerable[Type]) """
        ...

    def CreateQuery(self, queryString:str, parameters:Array) -> ObjectQuery:
        """ CreateQuery[T](self: ObjectContext, queryString: str, *parameters: Array[ObjectParameter]) -> ObjectQuery[T] """
        ...

    def DatabaseExists(self) -> bool:
        """ DatabaseExists(self: ObjectContext) -> bool """
        ...

    def DeleteDatabase(self): # -> 
        """ DeleteDatabase(self: ObjectContext) """
        ...

    def DeleteObject(self, entity:object): # -> 
        """ DeleteObject(self: ObjectContext, entity: object) """
        ...

    def Detach(self, entity:object): # -> 
        """ Detach(self: ObjectContext, entity: object) """
        ...

    def DetectChanges(self): # -> 
        """ DetectChanges(self: ObjectContext) """
        ...

    def ExecuteFunction(self, functionName:str, *__args:Array) -> ObjectResult:
        """
        ExecuteFunction[TElement](self: ObjectContext, functionName: str, *parameters: Array[ObjectParameter]) -> ObjectResult[TElement]
        ExecuteFunction[TElement](self: ObjectContext, functionName: str, mergeOption: MergeOption, *parameters: Array[ObjectParameter]) -> ObjectResult[TElement]
        ExecuteFunction(self: ObjectContext, functionName: str, *parameters: Array[ObjectParameter]) -> int
        """
        ...

    def ExecuteStoreCommand(self, commandText:str, parameters:Array) -> int:
        """ ExecuteStoreCommand(self: ObjectContext, commandText: str, *parameters: Array[object]) -> int """
        ...

    def ExecuteStoreQuery(self, commandText:str, *__args:Array) -> ObjectResult:
        """
        ExecuteStoreQuery[TElement](self: ObjectContext, commandText: str, *parameters: Array[object]) -> ObjectResult[TElement]
        ExecuteStoreQuery[TEntity](self: ObjectContext, commandText: str, entitySetName: str, mergeOption: MergeOption, *parameters: Array[object]) -> ObjectResult[TEntity]
        """
        ...

    @staticmethod
    def GetKnownProxyTypes() -> IEnumerable:
        """ GetKnownProxyTypes() -> IEnumerable[Type] """
        ...

    def GetObjectByKey(self, key:EntityKey) -> object:
        """ GetObjectByKey(self: ObjectContext, key: EntityKey) -> object """
        ...

    @staticmethod
    def GetObjectType(type:Type) -> Type:
        """ GetObjectType(type: Type) -> Type """
        ...

    def LoadProperty(self, entity:object, *__args:str): # -> 
        """ LoadProperty(self: ObjectContext, entity: object, navigationProperty: str)LoadProperty(self: ObjectContext, entity: object, navigationProperty: str, mergeOption: MergeOption)LoadProperty[TEntity](self: ObjectContext, entity: TEntity, selector: Expression[Func[TEntity, object]])LoadProperty[TEntity](self: ObjectContext, entity: TEntity, selector: Expression[Func[TEntity, object]], mergeOption: MergeOption) """
        ...

    def Refresh(self, refreshMode:RefreshMode, *__args:IEnumerable): # -> 
        """ Refresh(self: ObjectContext, refreshMode: RefreshMode, collection: IEnumerable)Refresh(self: ObjectContext, refreshMode: RefreshMode, entity: object) """
        ...

    def SaveChanges(self, *__args:bool) -> int:
        """
        SaveChanges(self: ObjectContext) -> int
        SaveChanges(self: ObjectContext, acceptChangesDuringSave: bool) -> int
        SaveChanges(self: ObjectContext, options: SaveOptions) -> int
        """
        ...

    def Translate(self, reader:DbDataReader, entitySetName:str = ..., mergeOption:MergeOption = ...) -> ObjectResult:
        """
        Translate[TElement](self: ObjectContext, reader: DbDataReader) -> ObjectResult[TElement]
        Translate[TEntity](self: ObjectContext, reader: DbDataReader, entitySetName: str, mergeOption: MergeOption) -> ObjectResult[TEntity]
        """
        ...

    def TryGetObjectByKey(self, key, value) -> Tuple_[bool, object]:
        """ TryGetObjectByKey(self: ObjectContext, key: EntityKey) -> (bool, object) """
        ...

    ObjectMaterialized = ...
    SavingChanges = ...


class ObjectContextOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LazyLoadingEnabled(self) -> bool:
        """
        Get: LazyLoadingEnabled(self: ObjectContextOptions) -> bool
        Set: LazyLoadingEnabled(self: ObjectContextOptions) = value
        """
        ...

    @property
    def ProxyCreationEnabled(self) -> bool:
        """
        Get: ProxyCreationEnabled(self: ObjectContextOptions) -> bool
        Set: ProxyCreationEnabled(self: ObjectContextOptions) = value
        """
        ...

    @property
    def UseConsistentNullReferenceBehavior(self) -> bool:
        """
        Get: UseConsistentNullReferenceBehavior(self: ObjectContextOptions) -> bool
        Set: UseConsistentNullReferenceBehavior(self: ObjectContextOptions) = value
        """
        ...

    @property
    def UseCSharpNullComparisonBehavior(self) -> bool:
        """
        Get: UseCSharpNullComparisonBehavior(self: ObjectContextOptions) -> bool
        Set: UseCSharpNullComparisonBehavior(self: ObjectContextOptions) = value
        """
        ...

    @property
    def UseLegacyPreserveChangesBehavior(self) -> bool:
        """
        Get: UseLegacyPreserveChangesBehavior(self: ObjectContextOptions) -> bool
        Set: UseLegacyPreserveChangesBehavior(self: ObjectContextOptions) = value
        """
        ...



class ObjectMaterializedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Entity(self) -> object:
        """ Get: Entity(self: ObjectMaterializedEventArgs) -> object """
        ...



class ObjectMaterializedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectMaterializedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectMaterializedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectMaterializedEventHandler, sender: object, e: ObjectMaterializedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectMaterializedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectMaterializedEventArgs): # -> 
        """ Invoke(self: ObjectMaterializedEventHandler, sender: object, e: ObjectMaterializedEventArgs) """
        ...


class ObjectParameter: # skipped bases: <type 'object'>, <type 'object'>
    """
    ObjectParameter(name: str, type: Type)
    ObjectParameter(name: str, value: object)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ObjectParameter) -> str """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: ObjectParameter) -> Type """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ObjectParameter) -> object
        Set: Value(self: ObjectParameter) = value
        """
        ...



class ObjectParameterCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[ObjectParameter]'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ObjectQuery: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandText(self) -> str:
        """ Get: CommandText(self: ObjectQuery) -> str """
        ...

    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: ObjectQuery) -> ObjectContext """
        ...

    @property
    def EnablePlanCaching(self) -> bool:
        """
        Get: EnablePlanCaching(self: ObjectQuery) -> bool
        Set: EnablePlanCaching(self: ObjectQuery) = value
        """
        ...

    @property
    def MergeOption(self) -> MergeOption:
        """
        Get: MergeOption(self: ObjectQuery) -> MergeOption
        Set: MergeOption(self: ObjectQuery) = value
        """
        ...

    @property
    def Parameters(self) -> ObjectParameterCollection:
        """ Get: Parameters(self: ObjectQuery) -> ObjectParameterCollection """
        ...


    def Execute(self, mergeOption:MergeOption) -> ObjectResult:
        """ Execute(self: ObjectQuery, mergeOption: MergeOption) -> ObjectResult """
        ...

    def GetResultType(self) -> TypeUsage:
        """ GetResultType(self: ObjectQuery) -> TypeUsage """
        ...

    def ToTraceString(self) -> str:
        """ ToTraceString(self: ObjectQuery) -> str """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class ObjectResult: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementType(self) -> Type:
        """ Get: ElementType(self: ObjectResult) -> Type """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: ObjectResult) """
        ...

    def GetNextResult(self) -> ObjectResult:
        """ GetNextResult[TElement](self: ObjectResult) -> ObjectResult[TElement] """
        ...

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        ...

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class ObjectSet(ObjectQuery, IObjectSet): # skipped bases: <type 'IOrderedQueryable[TEntity]'>, <type 'IQueryable[TEntity]'>, <type 'IEnumerable'>, <type 'IQueryable'>, <type 'IEnumerable[TEntity]'>, <type 'IOrderedQueryable'>, <type 'IListSource'>, <type 'object'>
    """ no doc """
    @property
    def EntitySet(self) -> EntitySet:
        """ Get: EntitySet(self: ObjectSet[TEntity]) -> EntitySet """
        ...


    def ApplyCurrentValues(self, currentEntity): # -> TEntity # Not found arg types: {'currentEntity': 'TEntity'}
        """ ApplyCurrentValues(self: ObjectSet[TEntity], currentEntity: TEntity) -> TEntity """
        ...

    def ApplyOriginalValues(self, originalEntity): # -> TEntity # Not found arg types: {'originalEntity': 'TEntity'}
        """ ApplyOriginalValues(self: ObjectSet[TEntity], originalEntity: TEntity) -> TEntity """
        ...

    def CreateObject(self): # -> TEntity
        """
        CreateObject(self: ObjectSet[TEntity]) -> TEntity
        CreateObject[T](self: ObjectSet[TEntity]) -> T
        """
        ...


class ObjectStateEntry(IEntityStateEntry, IEntityChangeTracker): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentValues(self) -> CurrentValueRecord:
        """ Get: CurrentValues(self: ObjectStateEntry) -> CurrentValueRecord """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: ObjectStateEntry) -> object """
        ...

    @property
    def EntityKey(self) -> EntityKey:
        """ Get: EntityKey(self: ObjectStateEntry) -> EntityKey """
        ...

    @property
    def EntitySet(self) -> EntitySetBase:
        """ Get: EntitySet(self: ObjectStateEntry) -> EntitySetBase """
        ...

    @property
    def IsRelationship(self) -> bool:
        """ Get: IsRelationship(self: ObjectStateEntry) -> bool """
        ...

    @property
    def ObjectStateManager(self) -> ObjectStateManager:
        """ Get: ObjectStateManager(self: ObjectStateEntry) -> ObjectStateManager """
        ...

    @property
    def OriginalValues(self) -> DbDataRecord:
        """ Get: OriginalValues(self: ObjectStateEntry) -> DbDataRecord """
        ...

    @property
    def RelationshipManager(self) -> RelationshipManager:
        """ Get: RelationshipManager(self: ObjectStateEntry) -> RelationshipManager """
        ...

    @property
    def State(self) -> EntityState:
        """ Get: State(self: ObjectStateEntry) -> EntityState """
        ...


    def AcceptChanges(self): # -> 
        """ AcceptChanges(self: ObjectStateEntry) """
        ...

    def ApplyCurrentValues(self, currentEntity:object): # -> 
        """ ApplyCurrentValues(self: ObjectStateEntry, currentEntity: object) """
        ...

    def ApplyOriginalValues(self, originalEntity:object): # -> 
        """ ApplyOriginalValues(self: ObjectStateEntry, originalEntity: object) """
        ...

    def ChangeState(self, state:EntityState): # -> 
        """ ChangeState(self: ObjectStateEntry, state: EntityState) """
        ...

    def Delete(self): # -> 
        """ Delete(self: ObjectStateEntry) """
        ...

    def GetModifiedProperties(self) -> IEnumerable:
        """ GetModifiedProperties(self: ObjectStateEntry) -> IEnumerable[str] """
        ...

    def GetUpdatableOriginalValues(self) -> OriginalValueRecord:
        """ GetUpdatableOriginalValues(self: ObjectStateEntry) -> OriginalValueRecord """
        ...

    def IsPropertyChanged(self, propertyName:str) -> bool:
        """ IsPropertyChanged(self: ObjectStateEntry, propertyName: str) -> bool """
        ...

    def RejectPropertyChanges(self, propertyName:str): # -> 
        """ RejectPropertyChanges(self: ObjectStateEntry, propertyName: str) """
        ...

    def SetModified(self): # -> 
        """ SetModified(self: ObjectStateEntry) """
        ...

    def SetModifiedProperty(self, propertyName:str): # -> 
        """ SetModifiedProperty(self: ObjectStateEntry, propertyName: str) """
        ...


class ObjectStateManager(IEntityStateManager): # skipped bases: <type 'object'>
    """ ObjectStateManager(metadataWorkspace: MetadataWorkspace) """
    @property
    def MetadataWorkspace(self) -> MetadataWorkspace:
        """ Get: MetadataWorkspace(self: ObjectStateManager) -> MetadataWorkspace """
        ...


    def ChangeObjectState(self, entity:object, entityState:EntityState) -> ObjectStateEntry:
        """ ChangeObjectState(self: ObjectStateManager, entity: object, entityState: EntityState) -> ObjectStateEntry """
        ...

    def ChangeRelationshipState(self, sourceEntity, targetEntity, *__args) -> ObjectStateEntry:
        """
        ChangeRelationshipState(self: ObjectStateManager, sourceEntity: object, targetEntity: object, relationshipName: str, targetRoleName: str, relationshipState: EntityState) -> ObjectStateEntry
        ChangeRelationshipState(self: ObjectStateManager, sourceEntity: object, targetEntity: object, navigationProperty: str, relationshipState: EntityState) -> ObjectStateEntry
        ChangeRelationshipState[TEntity](self: ObjectStateManager, sourceEntity: TEntity, targetEntity: object, navigationPropertySelector: Expression[Func[TEntity, object]], relationshipState: EntityState) -> ObjectStateEntry
        """
        ...

    def GetObjectStateEntries(self, state:EntityState) -> IEnumerable:
        """ GetObjectStateEntries(self: ObjectStateManager, state: EntityState) -> IEnumerable[ObjectStateEntry] """
        ...

    def GetObjectStateEntry(self, *__args:EntityKey) -> ObjectStateEntry:
        """
        GetObjectStateEntry(self: ObjectStateManager, key: EntityKey) -> ObjectStateEntry
        GetObjectStateEntry(self: ObjectStateManager, entity: object) -> ObjectStateEntry
        """
        ...

    def GetRelationshipManager(self, entity:object) -> RelationshipManager:
        """ GetRelationshipManager(self: ObjectStateManager, entity: object) -> RelationshipManager """
        ...

    def TryGetObjectStateEntry(self, *__args:EntityKey) -> Tuple_[bool, ObjectStateEntry]:
        """
        TryGetObjectStateEntry(self: ObjectStateManager, key: EntityKey) -> (bool, ObjectStateEntry)
        TryGetObjectStateEntry(self: ObjectStateManager, entity: object) -> (bool, ObjectStateEntry)
        """
        ...

    def TryGetRelationshipManager(self, entity, relationshipManager) -> Tuple_[bool, RelationshipManager]:
        """ TryGetRelationshipManager(self: ObjectStateManager, entity: object) -> (bool, RelationshipManager) """
        ...

    ObjectStateManagerChanged = ...


class OriginalValueRecord(DbUpdatableDataRecord): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDataRecord'>, <type 'IExtendedDataRecord'>, <type 'object'>
    """ no doc """
    pass

class ProxyDataContractResolver(DataContractResolver): # skipped bases: <type 'object'>
    """ ProxyDataContractResolver() """
    pass

class RefreshMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RefreshMode, values: ClientWins (2), StoreWins (1) """
    ClientWins: RefreshMode = ...
    StoreWins: RefreshMode = ...
    value__ = ...


class SaveOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SaveOptions, values: AcceptAllChangesAfterSave (1), DetectChangesBeforeSave (2), None (0) """
    AcceptAllChangesAfterSave: SaveOptions = ...
    DetectChangesBeforeSave: SaveOptions = ...
    value__ = ...


# variables with complex values

