# encoding: utf-8
# module System.Data.Entity.Design.PluralizationServices calls itself PluralizationServices
# from System.Data.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Globalization import CultureInfo


# no functions
# classes

class ICustomPluralizationMapping: # skipped bases: <type 'object'>
    """ no doc """
    def AddWord(self, singular:str, plural:str): # -> 
        """ AddWord(self: ICustomPluralizationMapping, singular: str, plural: str) """
        ...


class PluralizationService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: PluralizationService) -> CultureInfo """
        ...


    @staticmethod
    def CreateService(culture:CultureInfo) -> PluralizationService:
        """ CreateService(culture: CultureInfo) -> PluralizationService """
        ...

    def IsPlural(self, word:str) -> bool:
        """ IsPlural(self: PluralizationService, word: str) -> bool """
        ...

    def IsSingular(self, word:str) -> bool:
        """ IsSingular(self: PluralizationService, word: str) -> bool """
        ...

    def Pluralize(self, word:str) -> str:
        """ Pluralize(self: PluralizationService, word: str) -> str """
        ...

    def Singularize(self, word:str) -> str:
        """ Singularize(self: PluralizationService, word: str) -> str """
        ...


