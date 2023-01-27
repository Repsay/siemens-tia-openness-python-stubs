# encoding: utf-8
# module System.Web.Configuration.Internal calls itself Internal
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from typing import Tuple as Tuple_


# no functions
# classes

class IInternalConfigWebHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetConfigPathFromSiteIDAndVPath(self, siteID:str, vpath:str) -> str:
        """ GetConfigPathFromSiteIDAndVPath(self: IInternalConfigWebHost, siteID: str, vpath: str) -> str """
        ...

    def GetSiteIDAndVPathFromConfigPath(self, configPath, siteID, vpath) -> Tuple_[str, str]:
        """ GetSiteIDAndVPathFromConfigPath(self: IInternalConfigWebHost, configPath: str) -> (str, str) """
        ...


