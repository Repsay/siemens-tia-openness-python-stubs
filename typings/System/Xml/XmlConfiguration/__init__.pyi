# encoding: utf-8
# module System.Xml.XmlConfiguration calls itself XmlConfiguration
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import ConfigurationSection


# no functions
# classes

class XmlReaderSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ XmlReaderSection() """
    @property
    def CollapseWhiteSpaceIntoEmptyStringString(self) -> str:
        """
        Get: CollapseWhiteSpaceIntoEmptyStringString(self: XmlReaderSection) -> str
        Set: CollapseWhiteSpaceIntoEmptyStringString(self: XmlReaderSection) = value
        """
        ...

    @property
    def ProhibitDefaultResolverString(self) -> str:
        """
        Get: ProhibitDefaultResolverString(self: XmlReaderSection) -> str
        Set: ProhibitDefaultResolverString(self: XmlReaderSection) = value
        """
        ...



class XsltConfigSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ XsltConfigSection() """
    @property
    def ProhibitDefaultResolverString(self) -> str:
        """
        Get: ProhibitDefaultResolverString(self: XsltConfigSection) -> str
        Set: ProhibitDefaultResolverString(self: XsltConfigSection) = value
        """
        ...



