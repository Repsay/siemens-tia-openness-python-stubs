# encoding: utf-8
# module Microsoft.Vbe.Interop calls itself Interop
# from Microsoft.Vbe.Interop.Forms, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c, Microsoft.Vbe.Interop, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.AnalysisServices.AdomdClient import Property

from Microsoft.Office.Interop.Access import (Properties, References, 
    _References)

from Microsoft.Office.Interop.Graph import Application

from Microsoft.Office.Interop.Publisher import Window

from Microsoft.Office.Interop.Word import AddIn, Windows

from Microsoft.VisualStudio.CommandBars import CommandBars

from System import Enum, Int16, MulticastDelegate

from System.Collections import IEnumerable, IEnumerator

from System.ComponentModel import Component

from System.Windows.Markup import Reference

from typing import Tuple as Tuple_

"""The following names are not found in the module: (Addins, BoundEvent, 
    CodePane, CodePanes, Components, VBComponent, VBComponents, VBE, 
    VBProject, VBProjects, __ComObject, 
    _dispCommandBarControlEvents_ClickEventHandler, 
    _dispReferencesEvents_ItemAddedEventHandler, 
    _dispReferencesEvents_ItemRemovedEventHandler, 
    _dispReferences_Events_ItemAddedEventHandler, 
    _dispReferences_Events_ItemRemovedEventHandler, field#, 
    vbext_CodePaneview, vbext_ComponentType, vbext_RefKind)
"""

# no functions
# classes

class AddIn: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Collection(self): # -> Addins
        """ Get: Collection(self: AddIn) -> Addins """
        ...

    @property
    def Connect(self) -> bool:
        """
        Get: Connect(self: AddIn) -> bool
        Set: Connect(self: AddIn) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: AddIn) -> str
        Set: Description(self: AddIn) = value
        """
        ...

    @property
    def Guid(self) -> str:
        """ Get: Guid(self: AddIn) -> str """
        ...

    @property
    def Object(self) -> object:
        """
        Get: Object(self: AddIn) -> object
        Set: Object(self: AddIn) = value
        """
        ...

    @property
    def ProgId(self) -> str:
        """ Get: ProgId(self: AddIn) -> str """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: AddIn) -> VBE """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class _AddIns(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _AddIns) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _AddIns) -> object """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _AddIns) -> VBE """
        ...


    def Item(self, index:object) -> AddIn:
        """ Item(self: _AddIns, index: object) -> AddIn """
        ...

    def Update(self): # -> 
        """ Update(self: _AddIns) """
        ...


class Addins(_AddIns): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class AddinsClass(Addins, __ComObject): # skipped bases: <type 'IEnumerable'>, <type '_AddIns'>, <type 'object'>
    """ AddinsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: AddinsClass) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AddinsClass) -> object """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: AddinsClass) -> VBE """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: AddinsClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> AddIn:
        """ Item(self: AddinsClass, index: object) -> AddIn """
        ...

    def Update(self): # -> 
        """ Update(self: AddinsClass) """
        ...


class Application: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Version(self) -> str:
        """ Get: Version(self: Application) -> str """
        ...



class _CodeModule: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodePane(self): # -> CodePane
        """ Get: CodePane(self: _CodeModule) -> CodePane """
        ...

    @property
    def CountOfDeclarationLines(self) -> int:
        """ Get: CountOfDeclarationLines(self: _CodeModule) -> int """
        ...

    @property
    def CountOfLines(self) -> int:
        """ Get: CountOfLines(self: _CodeModule) -> int """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _CodeModule) -> str
        Set: Name(self: _CodeModule) = value
        """
        ...

    @property
    def Parent(self): # -> VBComponent
        """ Get: Parent(self: _CodeModule) -> VBComponent """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _CodeModule) -> VBE """
        ...


    def AddFromFile(self, FileName:str): # -> 
        """ AddFromFile(self: _CodeModule, FileName: str) """
        ...

    def AddFromString(self, String:str): # -> 
        """ AddFromString(self: _CodeModule, String: str) """
        ...

    def CreateEventProc(self, EventName:str, ObjectName:str) -> int:
        """ CreateEventProc(self: _CodeModule, EventName: str, ObjectName: str) -> int """
        ...

    def DeleteLines(self, StartLine:int, Count:int): # -> 
        """ DeleteLines(self: _CodeModule, StartLine: int, Count: int) """
        ...

    def Find(self, Target, StartLine, StartColumn, EndLine, EndColumn, WholeWord, MatchCase, PatternSearch) -> Tuple_[bool, int, int, int, int]:
        """ Find(self: _CodeModule, Target: str, WholeWord: bool, MatchCase: bool, PatternSearch: bool) -> (bool, int, int, int, int) """
        ...

    def InsertLines(self, Line:int, String:str): # -> 
        """ InsertLines(self: _CodeModule, Line: int, String: str) """
        ...

    def ReplaceLine(self, Line:int, String:str): # -> 
        """ ReplaceLine(self: _CodeModule, Line: int, String: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CodeModule(_CodeModule): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CodeModuleClass(__ComObject, CodeModule): # skipped bases: <type '_CodeModule'>, <type 'object'>
    """ CodeModuleClass() """
    @property
    def CodePane(self): # -> CodePane
        """ Get: CodePane(self: CodeModuleClass) -> CodePane """
        ...

    @property
    def CountOfDeclarationLines(self) -> int:
        """ Get: CountOfDeclarationLines(self: CodeModuleClass) -> int """
        ...

    @property
    def CountOfLines(self) -> int:
        """ Get: CountOfLines(self: CodeModuleClass) -> int """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CodeModuleClass) -> str
        Set: Name(self: CodeModuleClass) = value
        """
        ...

    @property
    def Parent(self): # -> VBComponent
        """ Get: Parent(self: CodeModuleClass) -> VBComponent """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: CodeModuleClass) -> VBE """
        ...


    def AddFromFile(self, FileName:str): # -> 
        """ AddFromFile(self: CodeModuleClass, FileName: str) """
        ...

    def AddFromString(self, String:str): # -> 
        """ AddFromString(self: CodeModuleClass, String: str) """
        ...

    def CreateEventProc(self, EventName:str, ObjectName:str) -> int:
        """ CreateEventProc(self: CodeModuleClass, EventName: str, ObjectName: str) -> int """
        ...

    def DeleteLines(self, StartLine:int, Count:int): # -> 
        """ DeleteLines(self: CodeModuleClass, StartLine: int, Count: int) """
        ...

    def Find(self, Target, StartLine, StartColumn, EndLine, EndColumn, WholeWord, MatchCase, PatternSearch) -> Tuple_[bool, int, int, int, int]:
        """ Find(self: CodeModuleClass, Target: str, WholeWord: bool, MatchCase: bool, PatternSearch: bool) -> (bool, int, int, int, int) """
        ...

    def InsertLines(self, Line:int, String:str): # -> 
        """ InsertLines(self: CodeModuleClass, Line: int, String: str) """
        ...

    def ReplaceLine(self, Line:int, String:str): # -> 
        """ ReplaceLine(self: CodeModuleClass, Line: int, String: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class _CodePane: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodeModule(self) -> CodeModule:
        """ Get: CodeModule(self: _CodePane) -> CodeModule """
        ...

    @property
    def CodePaneView(self): # -> vbext_CodePaneview
        """ Get: CodePaneView(self: _CodePane) -> vbext_CodePaneview """
        ...

    @property
    def Collection(self): # -> CodePanes
        """ Get: Collection(self: _CodePane) -> CodePanes """
        ...

    @property
    def CountOfVisibleLines(self) -> int:
        """ Get: CountOfVisibleLines(self: _CodePane) -> int """
        ...

    @property
    def TopLine(self) -> int:
        """
        Get: TopLine(self: _CodePane) -> int
        Set: TopLine(self: _CodePane) = value
        """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _CodePane) -> VBE """
        ...

    @property
    def Window(self) -> Window:
        """ Get: Window(self: _CodePane) -> Window """
        ...


    def GetSelection(self, StartLine, StartColumn, EndLine, EndColumn) -> Tuple_[int, int, int, int]:
        """ GetSelection(self: _CodePane) -> (int, int, int, int) """
        ...

    def SetSelection(self, StartLine:int, StartColumn:int, EndLine:int, EndColumn:int): # -> 
        """ SetSelection(self: _CodePane, StartLine: int, StartColumn: int, EndLine: int, EndColumn: int) """
        ...

    def Show(self): # -> 
        """ Show(self: _CodePane) """
        ...


class CodePane(_CodePane): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CodePaneClass(CodePane, __ComObject): # skipped bases: <type '_CodePane'>, <type 'object'>
    """ CodePaneClass() """
    @property
    def CodeModule(self) -> CodeModule:
        """ Get: CodeModule(self: CodePaneClass) -> CodeModule """
        ...

    @property
    def CodePaneView(self): # -> vbext_CodePaneview
        """ Get: CodePaneView(self: CodePaneClass) -> vbext_CodePaneview """
        ...

    @property
    def Collection(self): # -> CodePanes
        """ Get: Collection(self: CodePaneClass) -> CodePanes """
        ...

    @property
    def CountOfVisibleLines(self) -> int:
        """ Get: CountOfVisibleLines(self: CodePaneClass) -> int """
        ...

    @property
    def TopLine(self) -> int:
        """
        Get: TopLine(self: CodePaneClass) -> int
        Set: TopLine(self: CodePaneClass) = value
        """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: CodePaneClass) -> VBE """
        ...

    @property
    def Window(self) -> Window:
        """ Get: Window(self: CodePaneClass) -> Window """
        ...


    def GetSelection(self, StartLine, StartColumn, EndLine, EndColumn) -> Tuple_[int, int, int, int]:
        """ GetSelection(self: CodePaneClass) -> (int, int, int, int) """
        ...

    def SetSelection(self, StartLine:int, StartColumn:int, EndLine:int, EndColumn:int): # -> 
        """ SetSelection(self: CodePaneClass, StartLine: int, StartColumn: int, EndLine: int, EndColumn: int) """
        ...

    def Show(self): # -> 
        """ Show(self: CodePaneClass) """
        ...


class _CodePanes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _CodePanes) -> int """
        ...

    @property
    def Current(self) -> CodePane:
        """
        Get: Current(self: _CodePanes) -> CodePane
        Set: Current(self: _CodePanes) = value
        """
        ...

    @property
    def Parent(self): # -> VBE
        """ Get: Parent(self: _CodePanes) -> VBE """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _CodePanes) -> VBE """
        ...


    def Item(self, index:object) -> CodePane:
        """ Item(self: _CodePanes, index: object) -> CodePane """
        ...


class CodePanes(_CodePanes): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class CodePanesClass(__ComObject, CodePanes): # skipped bases: <type '_CodePanes'>, <type 'IEnumerable'>, <type 'object'>
    """ CodePanesClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CodePanesClass) -> int """
        ...

    @property
    def Current(self) -> CodePane:
        """
        Get: Current(self: CodePanesClass) -> CodePane
        Set: Current(self: CodePanesClass) = value
        """
        ...

    @property
    def Parent(self): # -> VBE
        """ Get: Parent(self: CodePanesClass) -> VBE """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: CodePanesClass) -> VBE """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CodePanesClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> CodePane:
        """ Item(self: CodePanesClass, index: object) -> CodePane """
        ...


class _CommandBarControlEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class _dispCommandBarControlEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Click(self): # -> 
        """ add_Click(self: _dispCommandBarControlEvents_Event, : _dispCommandBarControlEvents_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: _dispCommandBarControlEvents_Event, : _dispCommandBarControlEvents_ClickEventHandler) """
        ...

    Click = ...


class CommandBarEvents(_CommandBarControlEvents, _dispCommandBarControlEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CommandBarEventsClass(CommandBarEvents, __ComObject): # skipped bases: <type '_CommandBarControlEvents'>, <type '_dispCommandBarControlEvents_Event'>, <type 'object'>
    """ CommandBarEventsClass() """
    def add_Click(self): # -> 
        """ add_Click(self: CommandBarEventsClass, : _dispCommandBarControlEvents_ClickEventHandler) """
        ...

    def remove_Click(self): # -> 
        """ remove_Click(self: CommandBarEventsClass, : _dispCommandBarControlEvents_ClickEventHandler) """
        ...

    Click = ...


class _Component: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Component) -> Application """
        ...

    @property
    def IsDirty(self) -> bool:
        """
        Get: IsDirty(self: _Component) -> bool
        Set: IsDirty(self: _Component) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Component) -> str
        Set: Name(self: _Component) = value
        """
        ...

    @property
    def Parent(self): # -> Components
        """ Get: Parent(self: _Component) -> Components """
        ...



class Component(_Component): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ComponentClass(__ComObject, Component): # skipped bases: <type '_Component'>, <type 'object'>
    """ ComponentClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ComponentClass) -> Application """
        ...

    @property
    def IsDirty(self) -> bool:
        """
        Get: IsDirty(self: ComponentClass) -> bool
        Set: IsDirty(self: ComponentClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ComponentClass) -> str
        Set: Name(self: ComponentClass) = value
        """
        ...

    @property
    def Parent(self): # -> Components
        """ Get: Parent(self: ComponentClass) -> Components """
        ...



class _Components(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Components) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: _Components) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: _Components) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _Components) -> VBE """
        ...


    def Add(self, ComponentType) -> Component: # Not found arg types: {'ComponentType': 'vbext_ComponentType'}
        """ Add(self: _Components, ComponentType: vbext_ComponentType) -> Component """
        ...

    def Import(self, FileName:str) -> Component:
        """ Import(self: _Components, FileName: str) -> Component """
        ...

    def Item(self, index:object) -> Component:
        """ Item(self: _Components, index: object) -> Component """
        ...

    def Remove(self, Component:Component): # -> 
        """ Remove(self: _Components, Component: Component) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class Components(_Components): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class ComponentsClass(Components, __ComObject): # skipped bases: <type 'IEnumerable'>, <type '_Components'>, <type 'object'>
    """ ComponentsClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ComponentsClass) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ComponentsClass) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: ComponentsClass) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: ComponentsClass) -> VBE """
        ...


    def Add(self, ComponentType) -> Component: # Not found arg types: {'ComponentType': 'vbext_ComponentType'}
        """ Add(self: ComponentsClass, ComponentType: vbext_ComponentType) -> Component """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ComponentsClass) -> IEnumerator """
        ...

    def Import(self, FileName:str) -> Component:
        """ Import(self: ComponentsClass, FileName: str) -> Component """
        ...

    def Item(self, index:object) -> Component:
        """ Item(self: ComponentsClass, index: object) -> Component """
        ...

    def Remove(self, Component:Component): # -> 
        """ Remove(self: ComponentsClass, Component: Component) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class Events: # skipped bases: <type 'object'>
    """ no doc """
    pass

class _LinkedWindows(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _LinkedWindows) -> int """
        ...

    @property
    def Parent(self) -> Window:
        """ Get: Parent(self: _LinkedWindows) -> Window """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _LinkedWindows) -> VBE """
        ...


    def Add(self, Window:Window): # -> 
        """ Add(self: _LinkedWindows, Window: Window) """
        ...

    def Item(self, index:object) -> Window:
        """ Item(self: _LinkedWindows, index: object) -> Window """
        ...

    def Remove(self, Window:Window): # -> 
        """ Remove(self: _LinkedWindows, Window: Window) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class LinkedWindows(_LinkedWindows): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class LinkedWindowsClass(LinkedWindows, __ComObject): # skipped bases: <type '_LinkedWindows'>, <type 'IEnumerable'>, <type 'object'>
    """ LinkedWindowsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: LinkedWindowsClass) -> int """
        ...

    @property
    def Parent(self) -> Window:
        """ Get: Parent(self: LinkedWindowsClass) -> Window """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: LinkedWindowsClass) -> VBE """
        ...


    def Add(self, Window:Window): # -> 
        """ Add(self: LinkedWindowsClass, Window: Window) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: LinkedWindowsClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> Window:
        """ Item(self: LinkedWindowsClass, index: object) -> Window """
        ...

    def Remove(self, Window:Window): # -> 
        """ Remove(self: LinkedWindowsClass, Window: Window) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class _ProjectTemplate: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _ProjectTemplate) -> Application """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: _ProjectTemplate) -> Application """
        ...



class ProjectTemplate(_ProjectTemplate): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ProjectTemplateClass(ProjectTemplate, __ComObject): # skipped bases: <type '_ProjectTemplate'>, <type 'object'>
    """ ProjectTemplateClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ProjectTemplateClass) -> Application """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: ProjectTemplateClass) -> Application """
        ...



class _Properties(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Properties) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: _Properties) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Properties) -> object """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _Properties) -> VBE """
        ...


    def Item(self, index:object) -> Property:
        """ Item(self: _Properties, index: object) -> Property """
        ...


class Properties(_Properties): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class PropertiesClass(Properties, __ComObject): # skipped bases: <type '_Properties'>, <type 'IEnumerable'>, <type 'object'>
    """ PropertiesClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PropertiesClass) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: PropertiesClass) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PropertiesClass) -> object """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: PropertiesClass) -> VBE """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PropertiesClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> Property:
        """ Item(self: PropertiesClass, index: object) -> Property """
        ...


class Property: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Property) -> Application """
        ...

    @property
    def Collection(self) -> Properties:
        """ Get: Collection(self: Property) -> Properties """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Property) -> str """
        ...

    @property
    def NumIndices(self) -> Int16:
        """ Get: NumIndices(self: Property) -> Int16 """
        ...

    @property
    def Object(self) -> object:
        """
        Get: Object(self: Property) -> object
        Set: Object(self: Property) = value
        """
        ...

    @property
    def Parent(self) -> Properties:
        """ Get: Parent(self: Property) -> Properties """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: Property) -> object
        Set: Value(self: Property) = value
        """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: Property) -> VBE """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Reference: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BuiltIn(self) -> bool:
        """ Get: BuiltIn(self: Reference) -> bool """
        ...

    @property
    def Collection(self) -> References:
        """ Get: Collection(self: Reference) -> References """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Reference) -> str """
        ...

    @property
    def FullPath(self) -> str:
        """ Get: FullPath(self: Reference) -> str """
        ...

    @property
    def Guid(self) -> str:
        """ Get: Guid(self: Reference) -> str """
        ...

    @property
    def IsBroken(self) -> bool:
        """ Get: IsBroken(self: Reference) -> bool """
        ...

    @property
    def Major(self) -> int:
        """ Get: Major(self: Reference) -> int """
        ...

    @property
    def Minor(self) -> int:
        """ Get: Minor(self: Reference) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Reference) -> str """
        ...

    @property
    def Type(self): # -> vbext_RefKind
        """ Get: Type(self: Reference) -> vbext_RefKind """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: Reference) -> VBE """
        ...



class _dispReferences_Events_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_ItemAdded(self): # -> 
        """ add_ItemAdded(self: _dispReferences_Events_Event, : _dispReferences_Events_ItemAddedEventHandler) """
        ...

    def add_ItemRemoved(self): # -> 
        """ add_ItemRemoved(self: _dispReferences_Events_Event, : _dispReferences_Events_ItemRemovedEventHandler) """
        ...

    def remove_ItemAdded(self): # -> 
        """ remove_ItemAdded(self: _dispReferences_Events_Event, : _dispReferences_Events_ItemAddedEventHandler) """
        ...

    def remove_ItemRemoved(self): # -> 
        """ remove_ItemRemoved(self: _dispReferences_Events_Event, : _dispReferences_Events_ItemRemovedEventHandler) """
        ...

    ItemAdded = ...
    ItemRemoved = ...


class _References(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _References) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: _References) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _References) -> VBE """
        ...


    def AddFromFile(self, FileName:str) -> Reference:
        """ AddFromFile(self: _References, FileName: str) -> Reference """
        ...

    def AddFromGuid(self, Guid:str, Major:int, Minor:int) -> Reference:
        """ AddFromGuid(self: _References, Guid: str, Major: int, Minor: int) -> Reference """
        ...

    def Item(self, index:object) -> Reference:
        """ Item(self: _References, index: object) -> Reference """
        ...

    def Remove(self, Reference:Reference): # -> 
        """ Remove(self: _References, Reference: Reference) """
        ...


class References(_dispReferences_Events_Event, _References): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class ReferencesClass(References, __ComObject): # skipped bases: <type '_References'>, <type '_dispReferences_Events_Event'>, <type 'IEnumerable'>, <type 'object'>
    """ ReferencesClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReferencesClass) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: ReferencesClass) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: ReferencesClass) -> VBE """
        ...


    def AddFromFile(self, FileName:str) -> Reference:
        """ AddFromFile(self: ReferencesClass, FileName: str) -> Reference """
        ...

    def AddFromGuid(self, Guid:str, Major:int, Minor:int) -> Reference:
        """ AddFromGuid(self: ReferencesClass, Guid: str, Major: int, Minor: int) -> Reference """
        ...

    def add_ItemAdded(self): # -> 
        """ add_ItemAdded(self: ReferencesClass, : _dispReferences_Events_ItemAddedEventHandler) """
        ...

    def add_ItemRemoved(self): # -> 
        """ add_ItemRemoved(self: ReferencesClass, : _dispReferences_Events_ItemRemovedEventHandler) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReferencesClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> Reference:
        """ Item(self: ReferencesClass, index: object) -> Reference """
        ...

    def Remove(self, Reference:Reference): # -> 
        """ Remove(self: ReferencesClass, Reference: Reference) """
        ...

    def remove_ItemAdded(self): # -> 
        """ remove_ItemAdded(self: ReferencesClass, : _dispReferences_Events_ItemAddedEventHandler) """
        ...

    def remove_ItemRemoved(self): # -> 
        """ remove_ItemRemoved(self: ReferencesClass, : _dispReferences_Events_ItemRemovedEventHandler) """
        ...

    ItemAdded = ...
    ItemRemoved = ...


class _dispReferencesEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_ItemAdded(self): # -> 
        """ add_ItemAdded(self: _dispReferencesEvents_Event, : _dispReferencesEvents_ItemAddedEventHandler) """
        ...

    def add_ItemRemoved(self): # -> 
        """ add_ItemRemoved(self: _dispReferencesEvents_Event, : _dispReferencesEvents_ItemRemovedEventHandler) """
        ...

    def remove_ItemAdded(self): # -> 
        """ remove_ItemAdded(self: _dispReferencesEvents_Event, : _dispReferencesEvents_ItemAddedEventHandler) """
        ...

    def remove_ItemRemoved(self): # -> 
        """ remove_ItemRemoved(self: _dispReferencesEvents_Event, : _dispReferencesEvents_ItemRemovedEventHandler) """
        ...

    ItemAdded = ...
    ItemRemoved = ...


class _ReferencesEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReferencesEvents(_ReferencesEvents, _dispReferencesEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ReferencesEventsClass(ReferencesEvents, __ComObject): # skipped bases: <type '_ReferencesEvents'>, <type '_dispReferencesEvents_Event'>, <type 'object'>
    """ ReferencesEventsClass() """
    def add_ItemAdded(self): # -> 
        """ add_ItemAdded(self: ReferencesEventsClass, : _dispReferencesEvents_ItemAddedEventHandler) """
        ...

    def add_ItemRemoved(self): # -> 
        """ add_ItemRemoved(self: ReferencesEventsClass, : _dispReferencesEvents_ItemRemovedEventHandler) """
        ...

    def remove_ItemAdded(self): # -> 
        """ remove_ItemAdded(self: ReferencesEventsClass, : _dispReferencesEvents_ItemAddedEventHandler) """
        ...

    def remove_ItemRemoved(self): # -> 
        """ remove_ItemRemoved(self: ReferencesEventsClass, : _dispReferencesEvents_ItemRemovedEventHandler) """
        ...

    ItemAdded = ...
    ItemRemoved = ...


class SelectedComponents(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SelectedComponents) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SelectedComponents) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: SelectedComponents) -> VBProject """
        ...


    def Item(self, index:int) -> Component:
        """ Item(self: SelectedComponents, index: int) -> Component """
        ...


class _VBComponent_Old: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodeModule(self) -> CodeModule:
        """ Get: CodeModule(self: _VBComponent_Old) -> CodeModule """
        ...

    @property
    def Collection(self): # -> VBComponents
        """ Get: Collection(self: _VBComponent_Old) -> VBComponents """
        ...

    @property
    def Designer(self) -> object:
        """ Get: Designer(self: _VBComponent_Old) -> object """
        ...

    @property
    def HasOpenDesigner(self) -> bool:
        """ Get: HasOpenDesigner(self: _VBComponent_Old) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _VBComponent_Old) -> str
        Set: Name(self: _VBComponent_Old) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: _VBComponent_Old) -> Properties """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: _VBComponent_Old) -> bool """
        ...

    @property
    def Type(self): # -> vbext_ComponentType
        """ Get: Type(self: _VBComponent_Old) -> vbext_ComponentType """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _VBComponent_Old) -> VBE """
        ...


    def Activate(self): # -> 
        """ Activate(self: _VBComponent_Old) """
        ...

    def DesignerWindow(self) -> Window:
        """ DesignerWindow(self: _VBComponent_Old) -> Window """
        ...

    def Export(self, FileName:str): # -> 
        """ Export(self: _VBComponent_Old, FileName: str) """
        ...


class _VBComponent(_VBComponent_Old): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DesignerID(self) -> str:
        """ Get: DesignerID(self: _VBComponent) -> str """
        ...



class VBComponent(_VBComponent): # skipped bases: <type '_VBComponent_Old'>, <type 'object'>
    """ no doc """
    pass

class VBComponentClass(VBComponent, __ComObject): # skipped bases: <type '_VBComponent_Old'>, <type '_VBComponent'>, <type 'object'>
    """ VBComponentClass() """
    @property
    def CodeModule(self) -> CodeModule:
        """ Get: CodeModule(self: VBComponentClass) -> CodeModule """
        ...

    @property
    def Collection(self): # -> VBComponents
        """ Get: Collection(self: VBComponentClass) -> VBComponents """
        ...

    @property
    def Designer(self) -> object:
        """ Get: Designer(self: VBComponentClass) -> object """
        ...

    @property
    def DesignerID(self) -> str:
        """ Get: DesignerID(self: VBComponentClass) -> str """
        ...

    @property
    def HasOpenDesigner(self) -> bool:
        """ Get: HasOpenDesigner(self: VBComponentClass) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: VBComponentClass) -> str
        Set: Name(self: VBComponentClass) = value
        """
        ...

    @property
    def Properties(self) -> Properties:
        """ Get: Properties(self: VBComponentClass) -> Properties """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: VBComponentClass) -> bool """
        ...

    @property
    def Type(self): # -> vbext_ComponentType
        """ Get: Type(self: VBComponentClass) -> vbext_ComponentType """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: VBComponentClass) -> VBE """
        ...


    def Activate(self): # -> 
        """ Activate(self: VBComponentClass) """
        ...

    def DesignerWindow(self) -> Window:
        """ DesignerWindow(self: VBComponentClass) -> Window """
        ...

    def Export(self, FileName:str): # -> 
        """ Export(self: VBComponentClass, FileName: str) """
        ...


class _VBComponents_Old(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _VBComponents_Old) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: _VBComponents_Old) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _VBComponents_Old) -> VBE """
        ...


    def Add(self, ComponentType) -> VBComponent: # Not found arg types: {'ComponentType': 'vbext_ComponentType'}
        """ Add(self: _VBComponents_Old, ComponentType: vbext_ComponentType) -> VBComponent """
        ...

    def Import(self, FileName:str) -> VBComponent:
        """ Import(self: _VBComponents_Old, FileName: str) -> VBComponent """
        ...

    def Item(self, index:object) -> VBComponent:
        """ Item(self: _VBComponents_Old, index: object) -> VBComponent """
        ...

    def Remove(self, VBComponent:VBComponent): # -> 
        """ Remove(self: _VBComponents_Old, VBComponent: VBComponent) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class _VBComponents(_VBComponents_Old): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def AddCustom(self, ProgId:str) -> VBComponent:
        """ AddCustom(self: _VBComponents, ProgId: str) -> VBComponent """
        ...

    def AddMTDesigner(self, index:int) -> VBComponent:
        """ AddMTDesigner(self: _VBComponents, index: int) -> VBComponent """
        ...


class VBComponents(_VBComponents): # skipped bases: <type 'IEnumerable'>, <type '_VBComponents_Old'>, <type 'object'>
    """ no doc """
    pass

class VBComponentsClass(VBComponents, __ComObject): # skipped bases: <type '_VBComponents'>, <type 'IEnumerable'>, <type '_VBComponents_Old'>, <type 'object'>
    """ VBComponentsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: VBComponentsClass) -> int """
        ...

    @property
    def Parent(self): # -> VBProject
        """ Get: Parent(self: VBComponentsClass) -> VBProject """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: VBComponentsClass) -> VBE """
        ...


    def Add(self, ComponentType) -> VBComponent: # Not found arg types: {'ComponentType': 'vbext_ComponentType'}
        """ Add(self: VBComponentsClass, ComponentType: vbext_ComponentType) -> VBComponent """
        ...

    def AddCustom(self, ProgId:str) -> VBComponent:
        """ AddCustom(self: VBComponentsClass, ProgId: str) -> VBComponent """
        ...

    def AddMTDesigner(self, index:int) -> VBComponent:
        """ AddMTDesigner(self: VBComponentsClass, index: int) -> VBComponent """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: VBComponentsClass) -> IEnumerator """
        ...

    def Import(self, FileName:str) -> VBComponent:
        """ Import(self: VBComponentsClass, FileName: str) -> VBComponent """
        ...

    def Item(self, index:object) -> VBComponent:
        """ Item(self: VBComponentsClass, index: object) -> VBComponent """
        ...

    def Remove(self, VBComponent:VBComponent): # -> 
        """ Remove(self: VBComponentsClass, VBComponent: VBComponent) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class VBE(Application): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveCodePane(self) -> CodePane:
        """
        Get: ActiveCodePane(self: VBE) -> CodePane
        Set: ActiveCodePane(self: VBE) = value
        """
        ...

    @property
    def ActiveVBProject(self): # -> VBProject
        """
        Get: ActiveVBProject(self: VBE) -> VBProject
        Set: ActiveVBProject(self: VBE) = value
        """
        ...

    @property
    def ActiveWindow(self) -> Window:
        """ Get: ActiveWindow(self: VBE) -> Window """
        ...

    @property
    def Addins(self) -> Addins:
        """ Get: Addins(self: VBE) -> Addins """
        ...

    @property
    def CodePanes(self) -> CodePanes:
        """ Get: CodePanes(self: VBE) -> CodePanes """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: VBE) -> CommandBars """
        ...

    @property
    def Events(self) -> Events:
        """ Get: Events(self: VBE) -> Events """
        ...

    @property
    def MainWindow(self) -> Window:
        """ Get: MainWindow(self: VBE) -> Window """
        ...

    @property
    def SelectedVBComponent(self) -> VBComponent:
        """ Get: SelectedVBComponent(self: VBE) -> VBComponent """
        ...

    @property
    def VBProjects(self): # -> VBProjects
        """ Get: VBProjects(self: VBE) -> VBProjects """
        ...

    @property
    def Windows(self) -> Windows:
        """ Get: Windows(self: VBE) -> Windows """
        ...



class vbextFileTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbextFileTypes, values: vbextFileTypeBinary (10), vbextFileTypeClass (2), vbextFileTypeDesigners (12), vbextFileTypeDocObject (9), vbextFileTypeExe (4), vbextFileTypeForm (0), vbextFileTypeFrx (5), vbextFileTypeGroupProject (11), vbextFileTypeModule (1), vbextFileTypeProject (3), vbextFileTypePropertyPage (8), vbextFileTypeRes (6), vbextFileTypeUserControl (7) """
    value__ = ...
    vbextFileTypeBinary: vbextFileTypes = ...
    vbextFileTypeClass: vbextFileTypes = ...
    vbextFileTypeDesigners: vbextFileTypes = ...
    vbextFileTypeDocObject: vbextFileTypes = ...
    vbextFileTypeExe: vbextFileTypes = ...
    vbextFileTypeForm: vbextFileTypes = ...
    vbextFileTypeFrx: vbextFileTypes = ...
    vbextFileTypeGroupProject: vbextFileTypes = ...
    vbextFileTypeModule: vbextFileTypes = ...
    vbextFileTypeProject: vbextFileTypes = ...
    vbextFileTypePropertyPage: vbextFileTypes = ...
    vbextFileTypeRes: vbextFileTypes = ...
    vbextFileTypeUserControl: vbextFileTypes = ...


class vbext_CodePaneview(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_CodePaneview, values: vbext_cv_FullModuleView (1), vbext_cv_ProcedureView (0) """
    value__ = ...
    vbext_cv_FullModuleView: vbext_CodePaneview = ...
    vbext_cv_ProcedureView: vbext_CodePaneview = ...


class vbext_ComponentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_ComponentType, values: vbext_ct_ActiveXDesigner (11), vbext_ct_ClassModule (2), vbext_ct_Document (100), vbext_ct_MSForm (3), vbext_ct_StdModule (1) """
    value__ = ...
    vbext_ct_ActiveXDesigner: vbext_ComponentType = ...
    vbext_ct_ClassModule: vbext_ComponentType = ...
    vbext_ct_Document: vbext_ComponentType = ...
    vbext_ct_MSForm: vbext_ComponentType = ...
    vbext_ct_StdModule: vbext_ComponentType = ...


class vbext_ProcKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_ProcKind, values: vbext_pk_Get (3), vbext_pk_Let (1), vbext_pk_Proc (0), vbext_pk_Set (2) """
    value__ = ...
    vbext_pk_Get: vbext_ProcKind = ...
    vbext_pk_Let: vbext_ProcKind = ...
    vbext_pk_Proc: vbext_ProcKind = ...
    vbext_pk_Set: vbext_ProcKind = ...


class vbext_ProjectProtection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_ProjectProtection, values: vbext_pp_locked (1), vbext_pp_none (0) """
    value__ = ...
    vbext_pp_locked: vbext_ProjectProtection = ...
    vbext_pp_none: vbext_ProjectProtection = ...


class vbext_ProjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_ProjectType, values: vbext_pt_HostProject (100), vbext_pt_StandAlone (101) """
    value__ = ...
    vbext_pt_HostProject: vbext_ProjectType = ...
    vbext_pt_StandAlone: vbext_ProjectType = ...


class vbext_RefKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_RefKind, values: vbext_rk_Project (1), vbext_rk_TypeLib (0) """
    value__ = ...
    vbext_rk_Project: vbext_RefKind = ...
    vbext_rk_TypeLib: vbext_RefKind = ...


class vbext_VBAMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_VBAMode, values: vbext_vm_Break (1), vbext_vm_Design (2), vbext_vm_Run (0) """
    value__ = ...
    vbext_vm_Break: vbext_VBAMode = ...
    vbext_vm_Design: vbext_VBAMode = ...
    vbext_vm_Run: vbext_VBAMode = ...


class vbext_WindowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_WindowState, values: vbext_ws_Maximize (2), vbext_ws_Minimize (1), vbext_ws_Normal (0) """
    value__ = ...
    vbext_ws_Maximize: vbext_WindowState = ...
    vbext_ws_Minimize: vbext_WindowState = ...
    vbext_ws_Normal: vbext_WindowState = ...


class vbext_WindowType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum vbext_WindowType, values: vbext_wt_Browser (2), vbext_wt_CodeWindow (0), vbext_wt_Designer (1), vbext_wt_Find (8), vbext_wt_FindReplace (9), vbext_wt_Immediate (5), vbext_wt_LinkedWindowFrame (11), vbext_wt_Locals (4), vbext_wt_MainWindow (12), vbext_wt_ProjectWindow (6), vbext_wt_PropertyWindow (7), vbext_wt_Toolbox (10), vbext_wt_ToolWindow (15), vbext_wt_Watch (3) """
    value__ = ...
    vbext_wt_Browser: vbext_WindowType = ...
    vbext_wt_CodeWindow: vbext_WindowType = ...
    vbext_wt_Designer: vbext_WindowType = ...
    vbext_wt_Find: vbext_WindowType = ...
    vbext_wt_FindReplace: vbext_WindowType = ...
    vbext_wt_Immediate: vbext_WindowType = ...
    vbext_wt_LinkedWindowFrame: vbext_WindowType = ...
    vbext_wt_Locals: vbext_WindowType = ...
    vbext_wt_MainWindow: vbext_WindowType = ...
    vbext_wt_ProjectWindow: vbext_WindowType = ...
    vbext_wt_PropertyWindow: vbext_WindowType = ...
    vbext_wt_Toolbox: vbext_WindowType = ...
    vbext_wt_ToolWindow: vbext_WindowType = ...
    vbext_wt_Watch: vbext_WindowType = ...


class _VBProject_Old(_ProjectTemplate): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Collection(self): # -> VBProjects
        """ Get: Collection(self: _VBProject_Old) -> VBProjects """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: _VBProject_Old) -> str
        Set: Description(self: _VBProject_Old) = value
        """
        ...

    @property
    def HelpContextID(self) -> int:
        """
        Get: HelpContextID(self: _VBProject_Old) -> int
        Set: HelpContextID(self: _VBProject_Old) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: _VBProject_Old) -> str
        Set: HelpFile(self: _VBProject_Old) = value
        """
        ...

    @property
    def Mode(self) -> vbext_VBAMode:
        """ Get: Mode(self: _VBProject_Old) -> vbext_VBAMode """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _VBProject_Old) -> str
        Set: Name(self: _VBProject_Old) = value
        """
        ...

    @property
    def Protection(self) -> vbext_ProjectProtection:
        """ Get: Protection(self: _VBProject_Old) -> vbext_ProjectProtection """
        ...

    @property
    def References(self) -> References:
        """ Get: References(self: _VBProject_Old) -> References """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: _VBProject_Old) -> bool """
        ...

    @property
    def VBComponents(self) -> VBComponents:
        """ Get: VBComponents(self: _VBProject_Old) -> VBComponents """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: _VBProject_Old) -> VBE """
        ...



class _VBProject(_VBProject_Old): # skipped bases: <type '_ProjectTemplate'>, <type 'object'>
    """ no doc """
    @property
    def BuildFileName(self) -> str:
        """
        Get: BuildFileName(self: _VBProject) -> str
        Set: BuildFileName(self: _VBProject) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: _VBProject) -> str """
        ...

    @property
    def Type(self) -> vbext_ProjectType:
        """ Get: Type(self: _VBProject) -> vbext_ProjectType """
        ...


    def MakeCompiledFile(self): # -> 
        """ MakeCompiledFile(self: _VBProject) """
        ...

    def SaveAs(self, FileName:str): # -> 
        """ SaveAs(self: _VBProject, FileName: str) """
        ...


class VBProject(_VBProject): # skipped bases: <type '_ProjectTemplate'>, <type '_VBProject_Old'>, <type 'object'>
    """ no doc """
    pass

class VBProjectClass(VBProject, __ComObject): # skipped bases: <type '_VBProject'>, <type '_ProjectTemplate'>, <type '_VBProject_Old'>, <type 'object'>
    """ VBProjectClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: VBProjectClass) -> Application """
        ...

    @property
    def BuildFileName(self) -> str:
        """
        Get: BuildFileName(self: VBProjectClass) -> str
        Set: BuildFileName(self: VBProjectClass) = value
        """
        ...

    @property
    def Collection(self): # -> VBProjects
        """ Get: Collection(self: VBProjectClass) -> VBProjects """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: VBProjectClass) -> str
        Set: Description(self: VBProjectClass) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: VBProjectClass) -> str """
        ...

    @property
    def HelpContextID(self) -> int:
        """
        Get: HelpContextID(self: VBProjectClass) -> int
        Set: HelpContextID(self: VBProjectClass) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: VBProjectClass) -> str
        Set: HelpFile(self: VBProjectClass) = value
        """
        ...

    @property
    def Mode(self) -> vbext_VBAMode:
        """ Get: Mode(self: VBProjectClass) -> vbext_VBAMode """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: VBProjectClass) -> str
        Set: Name(self: VBProjectClass) = value
        """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: VBProjectClass) -> Application """
        ...

    @property
    def Protection(self) -> vbext_ProjectProtection:
        """ Get: Protection(self: VBProjectClass) -> vbext_ProjectProtection """
        ...

    @property
    def References(self) -> References:
        """ Get: References(self: VBProjectClass) -> References """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: VBProjectClass) -> bool """
        ...

    @property
    def Type(self) -> vbext_ProjectType:
        """ Get: Type(self: VBProjectClass) -> vbext_ProjectType """
        ...

    @property
    def VBComponents(self) -> VBComponents:
        """ Get: VBComponents(self: VBProjectClass) -> VBComponents """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: VBProjectClass) -> VBE """
        ...


    def MakeCompiledFile(self): # -> 
        """ MakeCompiledFile(self: VBProjectClass) """
        ...

    def SaveAs(self, FileName:str): # -> 
        """ SaveAs(self: VBProjectClass, FileName: str) """
        ...


class _VBProjects_Old(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _VBProjects_Old) -> int """
        ...

    @property
    def Parent(self) -> VBE:
        """ Get: Parent(self: _VBProjects_Old) -> VBE """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: _VBProjects_Old) -> VBE """
        ...


    def Item(self, index:object) -> VBProject:
        """ Item(self: _VBProjects_Old, index: object) -> VBProject """
        ...


class _VBProjects(_VBProjects_Old): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, Type:vbext_ProjectType) -> VBProject:
        """ Add(self: _VBProjects, Type: vbext_ProjectType) -> VBProject """
        ...

    def Open(self, bstrPath:str) -> VBProject:
        """ Open(self: _VBProjects, bstrPath: str) -> VBProject """
        ...

    def Remove(self, lpc:VBProject): # -> 
        """ Remove(self: _VBProjects, lpc: VBProject) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class VBProjects(_VBProjects): # skipped bases: <type '_VBProjects_Old'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class VBProjectsClass(VBProjects, __ComObject): # skipped bases: <type '_VBProjects_Old'>, <type 'IEnumerable'>, <type '_VBProjects'>, <type 'object'>
    """ VBProjectsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: VBProjectsClass) -> int """
        ...

    @property
    def Parent(self) -> VBE:
        """ Get: Parent(self: VBProjectsClass) -> VBE """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: VBProjectsClass) -> VBE """
        ...


    def Add(self, Type:vbext_ProjectType) -> VBProject:
        """ Add(self: VBProjectsClass, Type: vbext_ProjectType) -> VBProject """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: VBProjectsClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> VBProject:
        """ Item(self: VBProjectsClass, index: object) -> VBProject """
        ...

    def Open(self, bstrPath:str) -> VBProject:
        """ Open(self: VBProjectsClass, bstrPath: str) -> VBProject """
        ...

    def Remove(self, lpc:VBProject): # -> 
        """ Remove(self: VBProjectsClass, lpc: VBProject) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class Window: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Window) -> str """
        ...

    @property
    def Collection(self) -> Windows:
        """ Get: Collection(self: Window) -> Windows """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: Window) -> int
        Set: Height(self: Window) = value
        """
        ...

    @property
    def HWnd(self) -> int:
        """ Get: HWnd(self: Window) -> int """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: Window) -> int
        Set: Left(self: Window) = value
        """
        ...

    @property
    def LinkedWindowFrame(self) -> Window:
        """ Get: LinkedWindowFrame(self: Window) -> Window """
        ...

    @property
    def LinkedWindows(self) -> LinkedWindows:
        """ Get: LinkedWindows(self: Window) -> LinkedWindows """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: Window) -> int
        Set: Top(self: Window) = value
        """
        ...

    @property
    def Type(self) -> vbext_WindowType:
        """ Get: Type(self: Window) -> vbext_WindowType """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: Window) -> VBE """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Window) -> bool
        Set: Visible(self: Window) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: Window) -> int
        Set: Width(self: Window) = value
        """
        ...

    @property
    def WindowState(self) -> vbext_WindowState:
        """
        Get: WindowState(self: Window) -> vbext_WindowState
        Set: WindowState(self: Window) = value
        """
        ...


    def Attach(self, lWindowHandle:int): # -> 
        """ Attach(self: Window, lWindowHandle: int) """
        ...

    def Close(self): # -> 
        """ Close(self: Window) """
        ...

    def Detach(self): # -> 
        """ Detach(self: Window) """
        ...

    def SetFocus(self): # -> 
        """ SetFocus(self: Window) """
        ...

    def SetKind(self, eKind:vbext_WindowType): # -> 
        """ SetKind(self: Window, eKind: vbext_WindowType) """
        ...


class _Windows_old(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: _Windows_old) -> int """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: _Windows_old) -> Application """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: _Windows_old) -> VBE """
        ...


    def Item(self, index:object) -> Window:
        """ Item(self: _Windows_old, index: object) -> Window """
        ...


class _Windows(_Windows_old): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def CreateToolWindow(self, AddInInst, ProgId, Caption, GuidPosition, DocObj) -> Tuple_[Window, object]:
        """ CreateToolWindow(self: _Windows, AddInInst: AddIn, ProgId: str, Caption: str, GuidPosition: str) -> (Window, object) """
        ...


class Windows(_Windows): # skipped bases: <type 'IEnumerable'>, <type '_Windows_old'>, <type 'object'>
    """ no doc """
    pass

class WindowsClass(Windows, __ComObject): # skipped bases: <type '_Windows'>, <type 'IEnumerable'>, <type '_Windows_old'>, <type 'object'>
    """ WindowsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: WindowsClass) -> int """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: WindowsClass) -> Application """
        ...

    @property
    def VBE(self) -> VBE:
        """ Get: VBE(self: WindowsClass) -> VBE """
        ...


    def CreateToolWindow(self, AddInInst, ProgId, Caption, GuidPosition, DocObj) -> Tuple_[Window, object]:
        """ CreateToolWindow(self: WindowsClass, AddInInst: AddIn, ProgId: str, Caption: str, GuidPosition: str) -> (Window, object) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: WindowsClass) -> IEnumerator """
        ...

    def Item(self, index:object) -> Window:
        """ Item(self: WindowsClass, index: object) -> Window """
        ...


class _dispCommandBarControlEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Click(self, CommandBarControl:object, handled:bool, CancelDefault:bool) -> Tuple_[bool, bool]:
        """ Click(self: _dispCommandBarControlEvents, CommandBarControl: object, handled: bool, CancelDefault: bool) -> (bool, bool) """
        ...


class _dispCommandBarControlEvents_ClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _dispCommandBarControlEvents_ClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, CommandBarControl:object, handled:bool, CancelDefault:bool) -> Tuple_[bool, bool]:
        """ Invoke(self: _dispCommandBarControlEvents_ClickEventHandler, CommandBarControl: object, handled: bool, CancelDefault: bool) -> (bool, bool) """
        ...


class _dispCommandBarControlEvents_SinkHelper(_dispCommandBarControlEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_ClickDelegate = ...
    m_dwCookie = ...


class _dispReferencesEvents: # skipped bases: <type 'object'>
    """ no doc """
    def ItemAdded(self, Reference:Reference): # -> 
        """ ItemAdded(self: _dispReferencesEvents, Reference: Reference) """
        ...

    def ItemRemoved(self, Reference:Reference): # -> 
        """ ItemRemoved(self: _dispReferencesEvents, Reference: Reference) """
        ...


class _dispReferencesEvents_ItemAddedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _dispReferencesEvents_ItemAddedEventHandler(: object, : UIntPtr) """
    def Invoke(self, Reference:Reference): # -> 
        """ Invoke(self: _dispReferencesEvents_ItemAddedEventHandler, Reference: Reference) """
        ...


class _dispReferencesEvents_ItemRemovedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _dispReferencesEvents_ItemRemovedEventHandler(: object, : UIntPtr) """
    def Invoke(self, Reference:Reference): # -> 
        """ Invoke(self: _dispReferencesEvents_ItemRemovedEventHandler, Reference: Reference) """
        ...


class _dispReferencesEvents_SinkHelper(_dispReferencesEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...
    m_ItemAddedDelegate = ...
    m_ItemRemovedDelegate = ...


class _dispReferences_Events: # skipped bases: <type 'object'>
    """ no doc """
    def ItemAdded(self, Reference:Reference): # -> 
        """ ItemAdded(self: _dispReferences_Events, Reference: Reference) """
        ...

    def ItemRemoved(self, Reference:Reference): # -> 
        """ ItemRemoved(self: _dispReferences_Events, Reference: Reference) """
        ...


class _dispReferences_Events_ItemAddedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _dispReferences_Events_ItemAddedEventHandler(: object, : UIntPtr) """
    def Invoke(self, Reference:Reference): # -> 
        """ Invoke(self: _dispReferences_Events_ItemAddedEventHandler, Reference: Reference) """
        ...


class _dispReferences_Events_ItemRemovedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ _dispReferences_Events_ItemRemovedEventHandler(: object, : UIntPtr) """
    def Invoke(self, Reference:Reference): # -> 
        """ Invoke(self: _dispReferences_Events_ItemRemovedEventHandler, Reference: Reference) """
        ...


class _dispReferences_Events_SinkHelper(_dispReferences_Events): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...
    m_ItemAddedDelegate = ...
    m_ItemRemovedDelegate = ...


class _dispVBComponentsEvents: # skipped bases: <type 'object'>
    """ no doc """
    def ItemActivated(self, VBComponent:VBComponent): # -> 
        """ ItemActivated(self: _dispVBComponentsEvents, VBComponent: VBComponent) """
        ...

    def ItemAdded(self, VBComponent:VBComponent): # -> 
        """ ItemAdded(self: _dispVBComponentsEvents, VBComponent: VBComponent) """
        ...

    def ItemReloaded(self, VBComponent:VBComponent): # -> 
        """ ItemReloaded(self: _dispVBComponentsEvents, VBComponent: VBComponent) """
        ...

    def ItemRemoved(self, VBComponent:VBComponent): # -> 
        """ ItemRemoved(self: _dispVBComponentsEvents, VBComponent: VBComponent) """
        ...

    def ItemRenamed(self, VBComponent:VBComponent, OldName:str): # -> 
        """ ItemRenamed(self: _dispVBComponentsEvents, VBComponent: VBComponent, OldName: str) """
        ...

    def ItemSelected(self, VBComponent:VBComponent): # -> 
        """ ItemSelected(self: _dispVBComponentsEvents, VBComponent: VBComponent) """
        ...


class _dispVBProjectsEvents: # skipped bases: <type 'object'>
    """ no doc """
    def ItemActivated(self, VBProject:VBProject): # -> 
        """ ItemActivated(self: _dispVBProjectsEvents, VBProject: VBProject) """
        ...

    def ItemAdded(self, VBProject:VBProject): # -> 
        """ ItemAdded(self: _dispVBProjectsEvents, VBProject: VBProject) """
        ...

    def ItemRemoved(self, VBProject:VBProject): # -> 
        """ ItemRemoved(self: _dispVBProjectsEvents, VBProject: VBProject) """
        ...

    def ItemRenamed(self, VBProject:VBProject, OldName:str): # -> 
        """ ItemRenamed(self: _dispVBProjectsEvents, VBProject: VBProject, OldName: str) """
        ...


class _VBComponentsEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class _VBProjectsEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

# variables with complex values

