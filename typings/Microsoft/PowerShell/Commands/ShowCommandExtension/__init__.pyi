# encoding: utf-8
# module Microsoft.PowerShell.Commands.ShowCommandExtension calls itself ShowCommandExtension
# from Microsoft.PowerShell.Commands.Utility, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import ArrayList, ICollection, IList

from System.Management.Automation import CommandTypes


# no functions
# classes

class ShowCommandCommandInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ShowCommandCommandInfo(other: CommandInfo)
    ShowCommandCommandInfo(other: PSObject)
    """
    @property
    def CommandType(self) -> CommandTypes:
        """ Get: CommandType(self: ShowCommandCommandInfo) -> CommandTypes """
        ...

    @property
    def Definition(self) -> str:
        """ Get: Definition(self: ShowCommandCommandInfo) -> str """
        ...

    @property
    def Module(self) -> ShowCommandModuleInfo:
        """ Get: Module(self: ShowCommandCommandInfo) -> ShowCommandModuleInfo """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: ShowCommandCommandInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ShowCommandCommandInfo) -> str """
        ...

    @property
    def ParameterSets(self) -> ICollection:
        """ Get: ParameterSets(self: ShowCommandCommandInfo) -> ICollection[ShowCommandParameterSetInfo] """
        ...



class ShowCommandModuleInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ShowCommandModuleInfo(other: PSModuleInfo)
    ShowCommandModuleInfo(other: PSObject)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ShowCommandModuleInfo) -> str """
        ...



class ShowCommandParameterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ShowCommandParameterInfo(other: CommandParameterInfo)
    ShowCommandParameterInfo(other: PSObject)
    """
    @property
    def HasParameterSet(self) -> bool:
        """ Get: HasParameterSet(self: ShowCommandParameterInfo) -> bool """
        ...

    @property
    def IsMandatory(self) -> bool:
        """ Get: IsMandatory(self: ShowCommandParameterInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ShowCommandParameterInfo) -> str """
        ...

    @property
    def ParameterType(self) -> ShowCommandParameterType:
        """ Get: ParameterType(self: ShowCommandParameterInfo) -> ShowCommandParameterType """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: ShowCommandParameterInfo) -> int """
        ...

    @property
    def ValidParamSetValues(self) -> IList:
        """ Get: ValidParamSetValues(self: ShowCommandParameterInfo) -> IList[str] """
        ...

    @property
    def ValueFromPipeline(self) -> bool:
        """ Get: ValueFromPipeline(self: ShowCommandParameterInfo) -> bool """
        ...



class ShowCommandParameterSetInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ShowCommandParameterSetInfo(other: CommandParameterSetInfo)
    ShowCommandParameterSetInfo(other: PSObject)
    """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: ShowCommandParameterSetInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ShowCommandParameterSetInfo) -> str """
        ...

    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: ShowCommandParameterSetInfo) -> ICollection[ShowCommandParameterInfo] """
        ...



class ShowCommandParameterType: # skipped bases: <type 'object'>, <type 'object'>
    """
    ShowCommandParameterType(other: Type)
    ShowCommandParameterType(other: PSObject)
    """
    @property
    def ElementType(self) -> ShowCommandParameterType:
        """ Get: ElementType(self: ShowCommandParameterType) -> ShowCommandParameterType """
        ...

    @property
    def EnumValues(self) -> ArrayList:
        """ Get: EnumValues(self: ShowCommandParameterType) -> ArrayList """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: ShowCommandParameterType) -> str """
        ...

    @property
    def HasFlagAttribute(self) -> bool:
        """ Get: HasFlagAttribute(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def ImplementsDictionary(self) -> bool:
        """ Get: ImplementsDictionary(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsBoolean(self) -> bool:
        """ Get: IsBoolean(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsEnum(self) -> bool:
        """ Get: IsEnum(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsScriptBlock(self) -> bool:
        """ Get: IsScriptBlock(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsString(self) -> bool:
        """ Get: IsString(self: ShowCommandParameterType) -> bool """
        ...

    @property
    def IsSwitch(self) -> bool:
        """ Get: IsSwitch(self: ShowCommandParameterType) -> bool """
        ...



