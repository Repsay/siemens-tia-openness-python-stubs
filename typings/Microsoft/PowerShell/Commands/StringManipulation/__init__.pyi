# encoding: utf-8
# module Microsoft.PowerShell.Commands.StringManipulation calls itself StringManipulation
# from Microsoft.PowerShell.Commands.Utility, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections.Generic import List

from System.Management.Automation import PSCmdlet, SwitchParameter


# no functions
# classes

class ConvertFromStringCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertFromStringCommand() """
    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: ConvertFromStringCommand) -> str
        Set: Delimiter(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def IncludeExtent(self) -> SwitchParameter:
        """
        Get: IncludeExtent(self: ConvertFromStringCommand) -> SwitchParameter
        Set: IncludeExtent(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def InputObject(self) -> str:
        """
        Get: InputObject(self: ConvertFromStringCommand) -> str
        Set: InputObject(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def PropertyNames(self) -> Array:
        """
        Get: PropertyNames(self: ConvertFromStringCommand) -> Array[str]
        Set: PropertyNames(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def TemplateContent(self) -> Array:
        """
        Get: TemplateContent(self: ConvertFromStringCommand) -> Array[str]
        Set: TemplateContent(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def TemplateFile(self) -> Array:
        """
        Get: TemplateFile(self: ConvertFromStringCommand) -> Array[str]
        Set: TemplateFile(self: ConvertFromStringCommand) = value
        """
        ...

    @property
    def UpdateTemplate(self) -> SwitchParameter:
        """
        Get: UpdateTemplate(self: ConvertFromStringCommand) -> SwitchParameter
        Set: UpdateTemplate(self: ConvertFromStringCommand) = value
        """
        ...



class ConvertStringCommand(PSCmdlet): # skipped bases: <type 'object'>
    """ ConvertStringCommand() """
    @property
    def Example(self) -> List:
        """
        Get: Example(self: ConvertStringCommand) -> List[PSObject]
        Set: Example(self: ConvertStringCommand) = value
        """
        ...

    @property
    def InputObject(self) -> str:
        """
        Get: InputObject(self: ConvertStringCommand) -> str
        Set: InputObject(self: ConvertStringCommand) = value
        """
        ...



# variables with complex values

