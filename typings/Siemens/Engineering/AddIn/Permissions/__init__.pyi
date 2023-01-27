# encoding: utf-8
# module Siemens.Engineering.AddIn.Permissions calls itself Permissions
# from Siemens.Engineering.AddIn.Permissions, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self


# no functions
# classes

class ProcessStartPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'ISecurityEncodable'>, <type 'IPermission'>, <type 'IStackWalk'>, <type 'object'>
    """ ProcessStartPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class ProcessStartPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ProcessStartPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: ProcessStartPermissionAttribute) -> IPermission """
        ...


