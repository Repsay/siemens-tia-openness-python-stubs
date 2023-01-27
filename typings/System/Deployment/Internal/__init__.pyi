# encoding: utf-8
# module System.Deployment.Internal calls itself Internal
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Deployment, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ActivationContext, ApplicationIdentity, Array


# no functions
# classes

class InternalActivationContextHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetActivationContextData(appInfo:ActivationContext) -> object:
        """ GetActivationContextData(appInfo: ActivationContext) -> object """
        ...

    @staticmethod
    def GetApplicationComponentManifest(appInfo:ActivationContext) -> object:
        """ GetApplicationComponentManifest(appInfo: ActivationContext) -> object """
        ...

    @staticmethod
    def GetApplicationManifestBytes(appInfo:ActivationContext) -> Array:
        """ GetApplicationManifestBytes(appInfo: ActivationContext) -> Array[Byte] """
        ...

    @staticmethod
    def GetDeploymentComponentManifest(appInfo:ActivationContext) -> object:
        """ GetDeploymentComponentManifest(appInfo: ActivationContext) -> object """
        ...

    @staticmethod
    def GetDeploymentManifestBytes(appInfo:ActivationContext) -> Array:
        """ GetDeploymentManifestBytes(appInfo: ActivationContext) -> Array[Byte] """
        ...

    @staticmethod
    def IsFirstRun(appInfo:ActivationContext) -> bool:
        """ IsFirstRun(appInfo: ActivationContext) -> bool """
        ...

    @staticmethod
    def PrepareForExecution(appInfo:ActivationContext): # -> 
        """ PrepareForExecution(appInfo: ActivationContext) """
        ...

    __all__: list = ...


class InternalApplicationIdentityHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetInternalAppId(id:ApplicationIdentity) -> object:
        """ GetInternalAppId(id: ApplicationIdentity) -> object """
        ...

    __all__: list = ...


# variables with complex values

