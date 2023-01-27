# encoding: utf-8
# module Microsoft_VsaVb
# from Microsoft_VsaVb, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Vsa import (IVsaDTEngine, IVsaEngine, IVsaIDE, IVsaItems, 
    IVsaPersistSite, IVsaSite)

from System import Array

from System.Reflection import Assembly

from System.Security.Policy import Evidence

from typing import Tuple as Tuple_

"""The following names are not found in the module: __ComObject
"""

# no functions
# classes

class VsaDTEngine(IVsaDTEngine): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsaDTEngineClass(VsaDTEngine, __ComObject): # skipped bases: <type 'IVsaDTEngine'>, <type 'object'>
    """ VsaDTEngineClass() """
    @property
    def TargetURL(self) -> str:
        """
        Get: TargetURL(self: VsaDTEngineClass) -> str
        Set: TargetURL(self: VsaDTEngineClass) = value
        """
        ...


    def AttachDebugger(self, isAttach:bool): # -> 
        """ AttachDebugger(self: VsaDTEngineClass, isAttach: bool) """
        ...

    def GetIDE(self) -> IVsaIDE:
        """ GetIDE(self: VsaDTEngineClass) -> IVsaIDE """
        ...

    def InitCompleted(self): # -> 
        """ InitCompleted(self: VsaDTEngineClass) """
        ...


class VsaEngine(IVsaEngine): # skipped bases: <type 'object'>
    """ no doc """
    pass

class VsaEngineClass(VsaEngine, __ComObject): # skipped bases: <type 'IVsaEngine'>, <type 'object'>
    """ VsaEngineClass() """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: VsaEngineClass) -> Assembly """
        ...

    @property
    def Evidence(self) -> Evidence:
        """
        Get: Evidence(self: VsaEngineClass) -> Evidence
        Set: Evidence(self: VsaEngineClass) = value
        """
        ...

    @property
    def GenerateDebugInfo(self) -> bool:
        """
        Get: GenerateDebugInfo(self: VsaEngineClass) -> bool
        Set: GenerateDebugInfo(self: VsaEngineClass) = value
        """
        ...

    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: VsaEngineClass) -> bool """
        ...

    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: VsaEngineClass) -> bool """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: VsaEngineClass) -> bool """
        ...

    @property
    def Items(self) -> IVsaItems:
        """ Get: Items(self: VsaEngineClass) -> IVsaItems """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: VsaEngineClass) -> str """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: VsaEngineClass) -> int
        Set: LCID(self: VsaEngineClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: VsaEngineClass) -> str
        Set: Name(self: VsaEngineClass) = value
        """
        ...

    @property
    def RootMoniker(self) -> str:
        """
        Get: RootMoniker(self: VsaEngineClass) -> str
        Set: RootMoniker(self: VsaEngineClass) = value
        """
        ...

    @property
    def RootNamespace(self) -> str:
        """
        Get: RootNamespace(self: VsaEngineClass) -> str
        Set: RootNamespace(self: VsaEngineClass) = value
        """
        ...

    @property
    def Site(self) -> IVsaSite:
        """
        Get: Site(self: VsaEngineClass) -> IVsaSite
        Set: Site(self: VsaEngineClass) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: VsaEngineClass) -> str """
        ...


    def Close(self): # -> 
        """ Close(self: VsaEngineClass) """
        ...

    def Compile(self) -> bool:
        """ Compile(self: VsaEngineClass) -> bool """
        ...

    def GetOption(self, Name:str) -> object:
        """ GetOption(self: VsaEngineClass, Name: str) -> object """
        ...

    def InitNew(self): # -> 
        """ InitNew(self: VsaEngineClass) """
        ...

    def IsValidIdentifier(self, identifier:str) -> bool:
        """ IsValidIdentifier(self: VsaEngineClass, identifier: str) -> bool """
        ...

    def LoadSourceState(self, Site:IVsaPersistSite): # -> 
        """ LoadSourceState(self: VsaEngineClass, Site: IVsaPersistSite) """
        ...

    def Reset(self): # -> 
        """ Reset(self: VsaEngineClass) """
        ...

    def RevokeCache(self): # -> 
        """ RevokeCache(self: VsaEngineClass) """
        ...

    def Run(self): # -> 
        """ Run(self: VsaEngineClass) """
        ...

    def SaveCompiledState(self, pe, pdb) -> Tuple_[Array, Array]:
        """ SaveCompiledState(self: VsaEngineClass) -> (Array[Byte], Array[Byte]) """
        ...

    def SaveSourceState(self, Site:IVsaPersistSite): # -> 
        """ SaveSourceState(self: VsaEngineClass, Site: IVsaPersistSite) """
        ...

    def SetOption(self, Name:str, value:object): # -> 
        """ SetOption(self: VsaEngineClass, Name: str, value: object) """
        ...


