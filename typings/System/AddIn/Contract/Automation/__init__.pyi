# encoding: utf-8
# module System.AddIn.Contract.Automation calls itself Automation
# from System.AddIn.Contract, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.AddIn.Contract import IContract, RemoteArgument

from System.AddIn.Contract.Collections import (IArrayContract, 
    IRemoteArgumentArrayContract)

from System.Reflection import BindingFlags, MemberTypes

"""The following names are not found in the module: field#
"""

# no functions
# classes

class IRemoteObjectContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetRemoteType(self) -> IRemoteTypeContract:
        """ GetRemoteType(self: IRemoteObjectContract) -> IRemoteTypeContract """
        ...

    def RemoteCast(self, canonicalName:str) -> RemoteArgument:
        """ RemoteCast(self: IRemoteObjectContract, canonicalName: str) -> RemoteArgument """
        ...


class IRemoteDelegateContract(IRemoteObjectContract): # skipped bases: <type 'IContract'>, <type 'object'>
    """ no doc """
    def InvokeDelegate(self, args:IRemoteArgumentArrayContract) -> RemoteArgument:
        """ InvokeDelegate(self: IRemoteDelegateContract, args: IRemoteArgumentArrayContract) -> RemoteArgument """
        ...


class IRemoteEventInfoContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetAddMethod(self) -> IRemoteMethodInfoContract:
        """ GetAddMethod(self: IRemoteEventInfoContract) -> IRemoteMethodInfoContract """
        ...

    def GetMemberData(self) -> RemoteMemberData:
        """ GetMemberData(self: IRemoteEventInfoContract) -> RemoteMemberData """
        ...

    def GetRemoveMethod(self) -> IRemoteMethodInfoContract:
        """ GetRemoveMethod(self: IRemoteEventInfoContract) -> IRemoteMethodInfoContract """
        ...


class IRemoteFieldInfoContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetFieldData(self) -> RemoteFieldData:
        """ GetFieldData(self: IRemoteFieldInfoContract) -> RemoteFieldData """
        ...

    def GetValue(self, obj:IRemoteObjectContract) -> RemoteArgument:
        """ GetValue(self: IRemoteFieldInfoContract, obj: IRemoteObjectContract) -> RemoteArgument """
        ...

    def SetValue(self, obj:IRemoteObjectContract, value:RemoteArgument, localeId:int): # -> 
        """ SetValue(self: IRemoteFieldInfoContract, obj: IRemoteObjectContract, value: RemoteArgument, localeId: int) """
        ...


class IRemoteMethodInfoContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetMethodData(self) -> RemoteMethodData:
        """ GetMethodData(self: IRemoteMethodInfoContract) -> RemoteMethodData """
        ...

    def Invoke(self, target:IRemoteObjectContract, bindingFlags:BindingFlags, parameters:IRemoteArgumentArrayContract, localeId:int) -> RemoteArgument:
        """ Invoke(self: IRemoteMethodInfoContract, target: IRemoteObjectContract, bindingFlags: BindingFlags, parameters: IRemoteArgumentArrayContract, localeId: int) -> RemoteArgument """
        ...


class IRemotePropertyInfoContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetGetMethod(self) -> IRemoteMethodInfoContract:
        """ GetGetMethod(self: IRemotePropertyInfoContract) -> IRemoteMethodInfoContract """
        ...

    def GetPropertyData(self) -> RemotePropertyData:
        """ GetPropertyData(self: IRemotePropertyInfoContract) -> RemotePropertyData """
        ...

    def GetSetMethod(self) -> IRemoteMethodInfoContract:
        """ GetSetMethod(self: IRemotePropertyInfoContract) -> IRemoteMethodInfoContract """
        ...

    def GetValue(self, obj:IRemoteObjectContract, bindingFlags:BindingFlags, index:IRemoteArgumentArrayContract, localeId:int) -> RemoteArgument:
        """ GetValue(self: IRemotePropertyInfoContract, obj: IRemoteObjectContract, bindingFlags: BindingFlags, index: IRemoteArgumentArrayContract, localeId: int) -> RemoteArgument """
        ...

    def SetValue(self, target:IRemoteObjectContract, value:RemoteArgument, bindingFlags:BindingFlags, index:IRemoteArgumentArrayContract, localeId:int) -> RemoteArgument:
        """ SetValue(self: IRemotePropertyInfoContract, target: IRemoteObjectContract, value: RemoteArgument, bindingFlags: BindingFlags, index: IRemoteArgumentArrayContract, localeId: int) -> RemoteArgument """
        ...


class IRemoteTypeContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetCanonicalName(self) -> str:
        """ GetCanonicalName(self: IRemoteTypeContract) -> str """
        ...

    def GetEvent(self, name:str, bindingFlags:BindingFlags) -> IRemoteEventInfoContract:
        """ GetEvent(self: IRemoteTypeContract, name: str, bindingFlags: BindingFlags) -> IRemoteEventInfoContract """
        ...

    def GetEvents(self, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetEvents(self: IRemoteTypeContract, bindingFlags: BindingFlags) -> IArrayContract[IRemoteEventInfoContract] """
        ...

    def GetField(self, name:str, bindingFlags:BindingFlags) -> IRemoteFieldInfoContract:
        """ GetField(self: IRemoteTypeContract, name: str, bindingFlags: BindingFlags) -> IRemoteFieldInfoContract """
        ...

    def GetFields(self, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetFields(self: IRemoteTypeContract, bindingFlags: BindingFlags) -> IArrayContract[IRemoteFieldInfoContract] """
        ...

    def GetInterface(self, canonicalName:str) -> IRemoteTypeContract:
        """ GetInterface(self: IRemoteTypeContract, canonicalName: str) -> IRemoteTypeContract """
        ...

    def GetInterfaces(self) -> IArrayContract:
        """ GetInterfaces(self: IRemoteTypeContract) -> IArrayContract[IRemoteTypeContract] """
        ...

    def GetMember(self, name:str, memberTypes:MemberTypes, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetMember(self: IRemoteTypeContract, name: str, memberTypes: MemberTypes, bindingFlags: BindingFlags) -> IArrayContract[IContract] """
        ...

    def GetMembers(self, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetMembers(self: IRemoteTypeContract, bindingFlags: BindingFlags) -> IArrayContract[IContract] """
        ...

    def GetMethod(self, name:str, bindingFlags:BindingFlags, remoteTypes:IArrayContract) -> IRemoteMethodInfoContract:
        """ GetMethod(self: IRemoteTypeContract, name: str, bindingFlags: BindingFlags, remoteTypes: IArrayContract[IRemoteTypeContract]) -> IRemoteMethodInfoContract """
        ...

    def GetMethods(self, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetMethods(self: IRemoteTypeContract, bindingFlags: BindingFlags) -> IArrayContract[IRemoteMethodInfoContract] """
        ...

    def GetProperties(self, bindingFlags:BindingFlags) -> IArrayContract:
        """ GetProperties(self: IRemoteTypeContract, bindingFlags: BindingFlags) -> IArrayContract[IRemotePropertyInfoContract] """
        ...

    def GetProperty(self, name:str, bindingFlags:BindingFlags, remoteReturnType:IRemoteTypeContract, remoteTypes:IArrayContract) -> IRemotePropertyInfoContract:
        """ GetProperty(self: IRemoteTypeContract, name: str, bindingFlags: BindingFlags, remoteReturnType: IRemoteTypeContract, remoteTypes: IArrayContract[IRemoteTypeContract]) -> IRemotePropertyInfoContract """
        ...

    def GetTypeData(self) -> RemoteTypeData:
        """ GetTypeData(self: IRemoteTypeContract) -> RemoteTypeData """
        ...

    def InvokeMember(self, name:str, bindingFlags:BindingFlags, target:IRemoteObjectContract, remoteArgs:IRemoteArgumentArrayContract, remoteArgModifiers:Array, localeId:int) -> RemoteArgument:
        """ InvokeMember(self: IRemoteTypeContract, name: str, bindingFlags: BindingFlags, target: IRemoteObjectContract, remoteArgs: IRemoteArgumentArrayContract, remoteArgModifiers: Array[bool], localeId: int) -> RemoteArgument """
        ...


class RemoteFieldData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Attributes = ...
    FieldType = ...
    MemberData = ...


class RemoteMemberData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    DeclaringType = ...
    Name = ...


class RemoteMethodData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Attributes = ...
    MemberData = ...
    Parameters = ...
    ReturnParameter = ...


class RemoteParameterData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Attributes = ...
    DefaultValue = ...
    IsByRef = ...
    IsParameterArray = ...
    Name = ...
    ParameterType = ...
    Position = ...


class RemotePropertyData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Attributes = ...
    CanRead = ...
    CanWrite = ...
    IndexParameters = ...
    MemberData = ...
    PropertyType = ...


class RemoteTypeData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ArrayRank = ...
    AssemblyName = ...
    AssemblyQualifiedName = ...
    Attributes = ...
    BaseType = ...
    ElementType = ...
    FullName = ...
    IsArray = ...
    IsByRef = ...
    MemberData = ...
    TypeCode = ...


