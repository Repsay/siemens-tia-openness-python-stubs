# encoding: utf-8
# module Microsoft.Scripting.ComInterop calls itself ComInterop
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Guid, Int16, Type

from System.Collections import IEnumerable

from System.Dynamic import (ConvertBinder, DynamicMetaObject, GetIndexBinder, 
    GetMemberBinder, IDynamicMetaObjectProvider, InvokeBinder, 
    InvokeMemberBinder, SetIndexBinder, SetMemberBinder)

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ComBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CanComBind(value:object) -> bool:
        """ CanComBind(value: object) -> bool """
        ...

    @staticmethod
    def GetDynamicMemberNames(value:object) -> IEnumerable:
        """ GetDynamicMemberNames(value: object) -> IEnumerable[str] """
        ...

    @staticmethod
    def IsComObject(value:object) -> bool:
        """ IsComObject(value: object) -> bool """
        ...

    @staticmethod
    def TryBindGetIndex(binder, instance, args, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryBindGetIndex(binder: GetIndexBinder, instance: DynamicMetaObject, args: Array[DynamicMetaObject]) -> (bool, DynamicMetaObject) """
        ...

    @staticmethod
    def TryBindGetMember(binder, instance, result, delayInvocation=None) -> Tuple_[bool, DynamicMetaObject]:
        """
        TryBindGetMember(binder: GetMemberBinder, instance: DynamicMetaObject, delayInvocation: bool) -> (bool, DynamicMetaObject)
        TryBindGetMember(binder: GetMemberBinder, instance: DynamicMetaObject) -> (bool, DynamicMetaObject)
        """
        ...

    @staticmethod
    def TryBindInvoke(binder, instance, args, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryBindInvoke(binder: InvokeBinder, instance: DynamicMetaObject, args: Array[DynamicMetaObject]) -> (bool, DynamicMetaObject) """
        ...

    @staticmethod
    def TryBindInvokeMember(binder, instance, args, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryBindInvokeMember(binder: InvokeMemberBinder, instance: DynamicMetaObject, args: Array[DynamicMetaObject]) -> (bool, DynamicMetaObject) """
        ...

    @staticmethod
    def TryBindSetIndex(binder, instance, args, value, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryBindSetIndex(binder: SetIndexBinder, instance: DynamicMetaObject, args: Array[DynamicMetaObject], value: DynamicMetaObject) -> (bool, DynamicMetaObject) """
        ...

    @staticmethod
    def TryBindSetMember(binder, instance, value, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryBindSetMember(binder: SetMemberBinder, instance: DynamicMetaObject, value: DynamicMetaObject) -> (bool, DynamicMetaObject) """
        ...

    @staticmethod
    def TryConvert(binder, instance, result) -> Tuple_[bool, DynamicMetaObject]:
        """ TryConvert(binder: ConvertBinder, instance: DynamicMetaObject) -> (bool, DynamicMetaObject) """
        ...

    __all__: list = ...


class ComMethodDesc: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DispId(self) -> int:
        """ Get: DispId(self: ComMethodDesc) -> int """
        ...

    @property
    def IsDataMember(self) -> bool:
        """ Get: IsDataMember(self: ComMethodDesc) -> bool """
        ...

    @property
    def IsPropertyGet(self) -> bool:
        """ Get: IsPropertyGet(self: ComMethodDesc) -> bool """
        ...

    @property
    def IsPropertyPut(self) -> bool:
        """ Get: IsPropertyPut(self: ComMethodDesc) -> bool """
        ...

    @property
    def IsPropertyPutRef(self) -> bool:
        """ Get: IsPropertyPutRef(self: ComMethodDesc) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ComMethodDesc) -> str """
        ...



class ComParamDesc: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ByReference(self) -> bool:
        """ Get: ByReference(self: ComParamDesc) -> bool """
        ...

    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: ComParamDesc) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: ComParamDesc) -> bool """
        ...

    @property
    def IsOut(self) -> bool:
        """ Get: IsOut(self: ComParamDesc) -> bool """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: ComParamDesc) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: ComParamDesc) -> str """
        ...


class ComType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ComType, values: Class (0), Enum (1), Interface (2) """
    Class: ComType = ...
    Enum: ComType = ...
    Interface: ComType = ...
    value__ = ...


class ComTypeLibMemberDesc: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Kind(self) -> ComType:
        """ Get: Kind(self: ComTypeLibMemberDesc) -> ComType """
        ...



class ComTypeDesc(ComTypeLibMemberDesc): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TypeLib(self) -> ComTypeLibDesc:
        """ Get: TypeLib(self: ComTypeDesc) -> ComTypeLibDesc """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ComTypeDesc) -> str """
        ...



class ComTypeClassDesc(IDynamicMetaObjectProvider, ComTypeDesc): # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstance(self) -> object:
        """ CreateInstance(self: ComTypeClassDesc) -> object """
        ...


class ComTypeEnumDesc(IDynamicMetaObjectProvider, ComTypeDesc): # skipped bases: <type 'object'>
    """ no doc """
    def GetMemberNames(self) -> Array:
        """ GetMemberNames(self: ComTypeEnumDesc) -> Array[str] """
        ...

    def GetValue(self, enumValueName:str) -> object:
        """ GetValue(self: ComTypeEnumDesc, enumValueName: str) -> object """
        ...

    def ToString(self) -> str:
        """ ToString(self: ComTypeEnumDesc) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ComTypeLibDesc(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Documentation(self) -> str:
        """ Get: Documentation(self: ComTypeLibDesc) -> str """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: ComTypeLibDesc) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ComTypeLibDesc) -> str """
        ...

    @property
    def VersionMajor(self) -> Int16:
        """ Get: VersionMajor(self: ComTypeLibDesc) -> Int16 """
        ...

    @property
    def VersionMinor(self) -> Int16:
        """ Get: VersionMinor(self: ComTypeLibDesc) -> Int16 """
        ...


    @staticmethod
    def CreateFromGuid(typeLibGuid:Guid) -> ComTypeLibInfo:
        """ CreateFromGuid(typeLibGuid: Guid) -> ComTypeLibInfo """
        ...

    @staticmethod
    def CreateFromObject(rcw:object) -> ComTypeLibInfo:
        """ CreateFromObject(rcw: object) -> ComTypeLibInfo """
        ...

    def GetMemberNames(self) -> Array:
        """ GetMemberNames(self: ComTypeLibDesc) -> Array[str] """
        ...

    def GetTypeLibObjectDesc(self, member:str) -> object:
        """ GetTypeLibObjectDesc(self: ComTypeLibDesc, member: str) -> object """
        ...

    def ToString(self) -> str:
        """ ToString(self: ComTypeLibDesc) -> str """
        ...


class ComTypeLibInfo(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: ComTypeLibInfo) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ComTypeLibInfo) -> str """
        ...

    @property
    def TypeLibDesc(self) -> ComTypeLibDesc:
        """ Get: TypeLibDesc(self: ComTypeLibInfo) -> ComTypeLibDesc """
        ...

    @property
    def VersionMajor(self) -> Int16:
        """ Get: VersionMajor(self: ComTypeLibInfo) -> Int16 """
        ...

    @property
    def VersionMinor(self) -> Int16:
        """ Get: VersionMinor(self: ComTypeLibInfo) -> Int16 """
        ...


    def GetMemberNames(self) -> Array:
        """ GetMemberNames(self: ComTypeLibInfo) -> Array[str] """
        ...


