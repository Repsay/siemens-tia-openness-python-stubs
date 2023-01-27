# encoding: utf-8
# module System.Xaml.Permissions calls itself Permissions
# from System.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Type

from System.Collections import IList

from System.Reflection import Assembly, AssemblyName

from System.Security import CodeAccessPermission

from System.Security.Permissions import (IUnrestrictedPermission, 
    PermissionState)

from typing import Self


# no functions
# classes

class XamlAccessLevel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AssemblyAccessToAssemblyName(self) -> AssemblyName:
        """ Get: AssemblyAccessToAssemblyName(self: XamlAccessLevel) -> AssemblyName """
        ...

    @property
    def PrivateAccessToTypeName(self) -> str:
        """ Get: PrivateAccessToTypeName(self: XamlAccessLevel) -> str """
        ...


    @staticmethod
    def AssemblyAccessTo(*__args:Assembly) -> XamlAccessLevel:
        """
        AssemblyAccessTo(assembly: Assembly) -> XamlAccessLevel
        AssemblyAccessTo(assemblyName: AssemblyName) -> XamlAccessLevel
        """
        ...

    @staticmethod
    def PrivateAccessTo(*__args:Type) -> XamlAccessLevel:
        """
        PrivateAccessTo(type: Type) -> XamlAccessLevel
        PrivateAccessTo(assemblyQualifiedTypeName: str) -> XamlAccessLevel
        """
        ...


class XamlLoadPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    XamlLoadPermission(state: PermissionState)
    XamlLoadPermission(allowedAccess: XamlAccessLevel)
    XamlLoadPermission(allowedAccess: IEnumerable[XamlAccessLevel])
    """
    @property
    def AllowedAccess(self) -> IList:
        """ Get: AllowedAccess(self: XamlLoadPermission) -> IList[XamlAccessLevel] """
        ...


    def Includes(self, requestedAccess:XamlAccessLevel) -> bool:
        """ Includes(self: XamlLoadPermission, requestedAccess: XamlAccessLevel) -> bool """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, allowedAccess: XamlAccessLevel)
        __new__(cls: type, allowedAccess: IEnumerable[XamlAccessLevel])
        """
        ...


