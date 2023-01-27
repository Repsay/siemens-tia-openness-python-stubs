# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection)

from System.Security.Authentication.ExtendedProtection import (
    ExtendedProtectionPolicy, PolicyEnforcement, ProtectionScenario)


# no functions
# classes

class ExtendedProtectionPolicyElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ExtendedProtectionPolicyElement() """
    @property
    def CustomServiceNames(self) -> ServiceNameElementCollection:
        """ Get: CustomServiceNames(self: ExtendedProtectionPolicyElement) -> ServiceNameElementCollection """
        ...

    @property
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """
        Get: PolicyEnforcement(self: ExtendedProtectionPolicyElement) -> PolicyEnforcement
        Set: PolicyEnforcement(self: ExtendedProtectionPolicyElement) = value
        """
        ...

    @property
    def ProtectionScenario(self) -> ProtectionScenario:
        """
        Get: ProtectionScenario(self: ExtendedProtectionPolicyElement) -> ProtectionScenario
        Set: ProtectionScenario(self: ExtendedProtectionPolicyElement) = value
        """
        ...


    def BuildPolicy(self) -> ExtendedProtectionPolicy:
        """ BuildPolicy(self: ExtendedProtectionPolicyElement) -> ExtendedProtectionPolicy """
        ...


class ServiceNameElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ServiceNameElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ServiceNameElement) -> str
        Set: Name(self: ServiceNameElement) = value
        """
        ...



class ServiceNameElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceNameElementCollection() """
    def Add(self, element:ServiceNameElement): # -> 
        """ Add(self: ServiceNameElementCollection, element: ServiceNameElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ServiceNameElementCollection) """
        ...

    def IndexOf(self, element:ServiceNameElement) -> int:
        """ IndexOf(self: ServiceNameElementCollection, element: ServiceNameElement) -> int """
        ...

    def Remove(self, *__args:ServiceNameElement): # -> 
        """ Remove(self: ServiceNameElementCollection, element: ServiceNameElement)Remove(self: ServiceNameElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ServiceNameElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


