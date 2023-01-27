# encoding: utf-8
# module System.Runtime.Hosting calls itself Hosting
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ActivationContext, ApplicationIdentity, Array

from System.Runtime.Remoting import ObjectHandle

from System.Security.Policy import EvidenceBase

from typing import Self


# no functions
# classes

class ActivationArguments(EvidenceBase): # skipped bases: <type 'object'>
    """
    ActivationArguments(applicationIdentity: ApplicationIdentity)
    ActivationArguments(applicationIdentity: ApplicationIdentity, activationData: Array[str])
    ActivationArguments(activationData: ActivationContext)
    ActivationArguments(activationContext: ActivationContext, activationData: Array[str])
    """
    @property
    def ActivationContext(self) -> ActivationContext:
        """ Get: ActivationContext(self: ActivationArguments) -> ActivationContext """
        ...

    @property
    def ActivationData(self) -> Array:
        """ Get: ActivationData(self: ActivationArguments) -> Array[str] """
        ...

    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """ Get: ApplicationIdentity(self: ActivationArguments) -> ApplicationIdentity """
        ...


    def __new__(cls, *__args:ApplicationIdentity) -> Self:
        """
        __new__(cls: type, applicationIdentity: ApplicationIdentity)
        __new__(cls: type, applicationIdentity: ApplicationIdentity, activationData: Array[str])
        __new__(cls: type, activationData: ActivationContext)
        __new__(cls: type, activationContext: ActivationContext, activationData: Array[str])
        """
        ...


class ApplicationActivator: # skipped bases: <type 'object'>, <type 'object'>
    """ ApplicationActivator() """
    def CreateInstance(self, activationContext:ActivationContext, activationCustomData:Array = ...) -> ObjectHandle:
        """
        CreateInstance(self: ApplicationActivator, activationContext: ActivationContext) -> ObjectHandle
        CreateInstance(self: ApplicationActivator, activationContext: ActivationContext, activationCustomData: Array[str]) -> ObjectHandle
        """
        ...

    def CreateInstanceHelper(self, *args): #cannot find CLR method
        """ CreateInstanceHelper(adSetup: AppDomainSetup) -> ObjectHandle """
        ...


