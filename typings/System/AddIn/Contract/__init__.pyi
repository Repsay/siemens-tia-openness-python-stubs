# encoding: utf-8
# module System.AddIn.Contract calls itself Contract
# from System.AddIn.Contract, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Byte, Char, DBNull, DateTime, Decimal, Enum, 
    IDisposable, Int16, Int64, IntPtr, SByte, Single, TypeCode, UInt16, 
    UInt32, UInt64)

from System.AddIn.Contract.Collections import (IRemoteArgumentArrayContract, 
    IRemoteArgumentDictionaryContract)

from System.Reflection import Missing

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class IContract: # skipped bases: <type 'object'>
    """ no doc """
    def AcquireLifetimeToken(self) -> int:
        """ AcquireLifetimeToken(self: IContract) -> int """
        ...

    def GetRemoteHashCode(self) -> int:
        """ GetRemoteHashCode(self: IContract) -> int """
        ...

    def QueryContract(self, contractIdentifier:str) -> IContract:
        """ QueryContract(self: IContract, contractIdentifier: str) -> IContract """
        ...

    def RemoteEquals(self, contract:IContract) -> bool:
        """ RemoteEquals(self: IContract, contract: IContract) -> bool """
        ...

    def RemoteToString(self) -> str:
        """ RemoteToString(self: IContract) -> str """
        ...

    def RevokeLifetimeToken(self, token:int): # -> 
        """ RevokeLifetimeToken(self: IContract, token: int) """
        ...


class IEnumeratorContract(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetCurrent(self): # -> T
        """ GetCurrent(self: IEnumeratorContract[T]) -> T """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: IEnumeratorContract[T]) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: IEnumeratorContract[T]) """
        ...


class IExecutorExtensionContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def AssemblyLoaded(self, assemblyName:str): # -> 
        """ AssemblyLoaded(self: IExecutorExtensionContract, assemblyName: str) """
        ...

    def AssemblyLoadedFrom(self, assemblyFile:str): # -> 
        """ AssemblyLoadedFrom(self: IExecutorExtensionContract, assemblyFile: str) """
        ...

    def AssemblyLoading(self, assemblyName:str): # -> 
        """ AssemblyLoading(self: IExecutorExtensionContract, assemblyName: str) """
        ...

    def AssemblyLoadingFrom(self, assemblyFile:str): # -> 
        """ AssemblyLoadingFrom(self: IExecutorExtensionContract, assemblyFile: str) """
        ...

    def EntryPointStarted(self, entryPoint:IContract): # -> 
        """ EntryPointStarted(self: IExecutorExtensionContract, entryPoint: IContract) """
        ...

    def EntryPointStarting(self, assemblyName:str, startupClass:str, initArgs:IRemoteArgumentArrayContract): # -> 
        """ EntryPointStarting(self: IExecutorExtensionContract, assemblyName: str, startupClass: str, initArgs: IRemoteArgumentArrayContract) """
        ...

    def ExecutorCreated(self): # -> 
        """ ExecutorCreated(self: IExecutorExtensionContract) """
        ...


class IListContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def Add(self, item): # ->  # Not found arg types: {'item': 'T'}
        """ Add(self: IListContract[T], item: T) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IListContract[T]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: IListContract[T], item: T) -> bool """
        ...

    def GetCount(self) -> int:
        """ GetCount(self: IListContract[T]) -> int """
        ...

    def GetEnumeratorContract(self) -> IEnumeratorContract:
        """ GetEnumeratorContract(self: IListContract[T]) -> IEnumeratorContract[T] """
        ...

    def GetIsReadOnly(self) -> bool:
        """ GetIsReadOnly(self: IListContract[T]) -> bool """
        ...

    def GetItem(self, index:int): # -> T
        """ GetItem(self: IListContract[T], index: int) -> T """
        ...

    def IndexOf(self, item) -> int: # Not found arg types: {'item': 'T'}
        """ IndexOf(self: IListContract[T], item: T) -> int """
        ...

    def Insert(self, index:int, item): # ->  # Not found arg types: {'item': 'T'}
        """ Insert(self: IListContract[T], index: int, item: T) """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Remove(self: IListContract[T], item: T) -> bool """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IListContract[T], index: int) """
        ...

    def SetItem(self, index:int, item): # ->  # Not found arg types: {'item': 'T'}
        """ SetItem(self: IListContract[T], index: int, item: T) """
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


class INativeHandleContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetHandle(self) -> IntPtr:
        """ GetHandle(self: INativeHandleContract) -> IntPtr """
        ...


class IProfferServiceContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def ProfferService(self, serviceIdentifier:str, service:IServiceProviderContract): # -> 
        """ ProfferService(self: IProfferServiceContract, serviceIdentifier: str, service: IServiceProviderContract) """
        ...

    def RevokeService(self, serviceIdentifier:str): # -> 
        """ RevokeService(self: IProfferServiceContract, serviceIdentifier: str) """
        ...


class ISerializableObjectContract(IRemoteArgumentDictionaryContract): # skipped bases: <type 'IContract'>, <type 'IRemoteArgumentCollectionContract'>, <type 'IRemoteArgumentEnumerableContract'>, <type 'object'>
    """ no doc """
    def GetCanonicalName(self) -> str:
        """ GetCanonicalName(self: ISerializableObjectContract) -> str """
        ...

    def GetSerializableObjectData(self) -> SerializableObjectData:
        """ GetSerializableObjectData(self: ISerializableObjectContract) -> SerializableObjectData """
        ...


class IServiceProviderContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def QueryService(self, serviceIdentifier:str, serviceContractIdentifier:str) -> IContract:
        """ QueryService(self: IServiceProviderContract, serviceIdentifier: str, serviceContractIdentifier: str) -> IContract """
        ...


class RemoteArgument: # skipped bases: <type 'object'>, <type 'object'>
    """
    RemoteArgument(value: IContract)
    RemoteArgument(value: IContract, isByRef: bool)
    RemoteArgument(remoteArgKind: RemoteArgumentKind, typeCode: TypeCode)
    RemoteArgument(remoteArgKind: RemoteArgumentKind, typeCode: TypeCode, isByRef: bool)
    RemoteArgument(value: bool)
    RemoteArgument(value: bool, isByRef: bool)
    RemoteArgument(value: Byte)
    RemoteArgument(value: Byte, isByRef: bool)
    RemoteArgument(value: Char)
    RemoteArgument(value: Char, isByRef: bool)
    RemoteArgument(value: DateTime)
    RemoteArgument(value: DateTime, isByRef: bool)
    RemoteArgument(value: DBNull)
    RemoteArgument(value: DBNull, isByRef: bool)
    RemoteArgument(value: Decimal)
    RemoteArgument(value: Decimal, isByRef: bool)
    RemoteArgument(value: float)
    RemoteArgument(value: float, isByRef: bool)
    RemoteArgument(value: Int16)
    RemoteArgument(value: Int16, isByRef: bool)
    RemoteArgument(value: int)
    RemoteArgument(value: int, isByRef: bool)
    RemoteArgument(value: Int64)
    RemoteArgument(value: Int64, isByRef: bool)
    RemoteArgument(value: Single)
    RemoteArgument(value: Single, isByRef: bool)
    RemoteArgument(value: str)
    RemoteArgument(value: str, isByRef: bool)
    RemoteArgument(value: SByte)
    RemoteArgument(value: SByte, isByRef: bool)
    RemoteArgument(value: UInt16)
    RemoteArgument(value: UInt16, isByRef: bool)
    RemoteArgument(value: UInt32)
    RemoteArgument(value: UInt32, isByRef: bool)
    RemoteArgument(value: UInt64)
    RemoteArgument(value: UInt64, isByRef: bool)
    RemoteArgument(array: Array)
    RemoteArgument(array: Array, isByRef: bool)
    """
    @property
    def ArrayValue(self) -> Array:
        """
        Get: ArrayValue(self: RemoteArgument) -> Array
        Set: ArrayValue(self: RemoteArgument) = value
        """
        ...

    @property
    def BooleanValue(self) -> bool:
        """
        Get: BooleanValue(self: RemoteArgument) -> bool
        Set: BooleanValue(self: RemoteArgument) = value
        """
        ...

    @property
    def ByteValue(self) -> Byte:
        """
        Get: ByteValue(self: RemoteArgument) -> Byte
        Set: ByteValue(self: RemoteArgument) = value
        """
        ...

    @property
    def CharValue(self) -> Char:
        """
        Get: CharValue(self: RemoteArgument) -> Char
        Set: CharValue(self: RemoteArgument) = value
        """
        ...

    @property
    def ContractValue(self) -> IContract:
        """
        Get: ContractValue(self: RemoteArgument) -> IContract
        Set: ContractValue(self: RemoteArgument) = value
        """
        ...

    @property
    def DateTimeValue(self) -> DateTime:
        """
        Get: DateTimeValue(self: RemoteArgument) -> DateTime
        Set: DateTimeValue(self: RemoteArgument) = value
        """
        ...

    @property
    def DBNullValue(self) -> DBNull:
        """
        Get: DBNullValue(self: RemoteArgument) -> DBNull
        Set: DBNullValue(self: RemoteArgument) = value
        """
        ...

    @property
    def DecimalValue(self) -> Decimal:
        """
        Get: DecimalValue(self: RemoteArgument) -> Decimal
        Set: DecimalValue(self: RemoteArgument) = value
        """
        ...

    @property
    def DoubleValue(self) -> float:
        """
        Get: DoubleValue(self: RemoteArgument) -> float
        Set: DoubleValue(self: RemoteArgument) = value
        """
        ...

    @property
    def Int16Value(self) -> Int16:
        """
        Get: Int16Value(self: RemoteArgument) -> Int16
        Set: Int16Value(self: RemoteArgument) = value
        """
        ...

    @property
    def Int32Value(self) -> int:
        """
        Get: Int32Value(self: RemoteArgument) -> int
        Set: Int32Value(self: RemoteArgument) = value
        """
        ...

    @property
    def Int64Value(self) -> Int64:
        """
        Get: Int64Value(self: RemoteArgument) -> Int64
        Set: Int64Value(self: RemoteArgument) = value
        """
        ...

    @property
    def IsByRef(self) -> bool:
        """
        Get: IsByRef(self: RemoteArgument) -> bool
        Set: IsByRef(self: RemoteArgument) = value
        """
        ...

    @property
    def MissingValue(self) -> Missing:
        """ Get: MissingValue(self: RemoteArgument) -> Missing """
        ...

    @property
    def RemoteArgumentKind(self) -> RemoteArgumentKind:
        """ Get: RemoteArgumentKind(self: RemoteArgument) -> RemoteArgumentKind """
        ...

    @property
    def SByteValue(self) -> SByte:
        """
        Get: SByteValue(self: RemoteArgument) -> SByte
        Set: SByteValue(self: RemoteArgument) = value
        """
        ...

    @property
    def SingleValue(self) -> Single:
        """
        Get: SingleValue(self: RemoteArgument) -> Single
        Set: SingleValue(self: RemoteArgument) = value
        """
        ...

    @property
    def StringValue(self) -> str:
        """
        Get: StringValue(self: RemoteArgument) -> str
        Set: StringValue(self: RemoteArgument) = value
        """
        ...

    @property
    def TypeCode(self) -> TypeCode:
        """ Get: TypeCode(self: RemoteArgument) -> TypeCode """
        ...

    @property
    def UInt16Value(self) -> UInt16:
        """
        Get: UInt16Value(self: RemoteArgument) -> UInt16
        Set: UInt16Value(self: RemoteArgument) = value
        """
        ...

    @property
    def UInt32Value(self) -> UInt32:
        """
        Get: UInt32Value(self: RemoteArgument) -> UInt32
        Set: UInt32Value(self: RemoteArgument) = value
        """
        ...

    @property
    def UInt64Value(self) -> UInt64:
        """
        Get: UInt64Value(self: RemoteArgument) -> UInt64
        Set: UInt64Value(self: RemoteArgument) = value
        """
        ...


    @staticmethod
    def CreateRemoteArgument(value:object, isByRef:bool = ..., typeCodeToUse:TypeCode = ...) -> RemoteArgument:
        """
        CreateRemoteArgument(value: object) -> RemoteArgument
        CreateRemoteArgument(value: object, isByRef: bool) -> RemoteArgument
        CreateRemoteArgument(value: object, isByRef: bool, typeCodeToUse: TypeCode) -> RemoteArgument
        """
        ...


class RemoteArgumentKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RemoteArgumentKind, values: Contract (3), Intrinsic (1), IntrinsicArray (2), Missing (0) """
    Contract: RemoteArgumentKind = ...
    Intrinsic: RemoteArgumentKind = ...
    IntrinsicArray: RemoteArgumentKind = ...
    Missing: RemoteArgumentKind = ...
    value__ = ...


class SerializableObjectData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    DimensionLengths = ...
    DimensionLowerBounds = ...
    ElementIndexes = ...
    IsArray = ...
    IsArrayElement = ...
    MemberName = ...
    ObjectId = ...
    ParentId = ...


# variables with complex values

