# encoding: utf-8
# module System.Web.UI.WebControls.WebParts calls itself WebParts
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Word import Style, TableStyle

from System import (Array, AsyncCallback, Attribute, DateTime, Enum, 
    EventArgs, IAsyncResult, IDisposable, Int16, MulticastDelegate, Type)

from System.Collections import (CollectionBase, ICollection, IDictionary, 
    IEnumerator, ReadOnlyCollectionBase)

from System.Collections.Specialized import NameValueCollection

from System.ComponentModel import (CancelEventArgs, ICustomTypeDescriptor, 
    PropertyDescriptor, PropertyDescriptorCollection)

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.Drawing import Color

from System.Reflection import MethodInfo

from System.Web.UI import (Control, ControlCollection, HtmlTextWriter, 
    INamingContainer, IPostBackDataHandler, IPostBackEventHandler, 
    IStateManager, ITemplate, Page)

from System.Web.UI.MobileControls import FontInfo

from System.Web.UI.WebControls import (ButtonType, CompositeControl, 
    ContentDirection, HorizontalAlign, ICompositeControlDesignerAccessor, 
    TableItemStyle, Unit)

from System.Windows.Forms import BorderStyle, Orientation, Panel, ScrollBars

from System.Xml import XmlReader, XmlWriter

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    BrowseWebPartDisplayMode, CatalogWebPartDisplayMode, 
    ConnectWebPartDisplayMode, DesignWebPartDisplayMode, 
    EditWebPartDisplayMode, IWebPartMenuUser, field#)
"""

# no functions
# classes

class Part(ICompositeControlDesignerAccessor, Panel, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def ChromeState(self) -> PartChromeState:
        """
        Get: ChromeState(self: Part) -> PartChromeState
        Set: ChromeState(self: Part) = value
        """
        ...

    @property
    def ChromeType(self) -> PartChromeType:
        """
        Get: ChromeType(self: Part) -> PartChromeType
        Set: ChromeType(self: Part) = value
        """
        ...

    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: Part) -> ControlCollection """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Part) -> str
        Set: Description(self: Part) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Part) -> str
        Set: Title(self: Part) = value
        """
        ...



class EditorPart(Part): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Display(self) -> bool:
        """ Get: Display(self: EditorPart) -> bool """
        ...

    @property
    def DisplayTitle(self) -> str:
        """ Get: DisplayTitle(self: EditorPart) -> str """
        ...

    @property
    def WebPartManager(self):
        ...

    @property
    def WebPartToEdit(self):
        ...

    @property
    def Zone(self):
        ...


    def ApplyChanges(self) -> bool:
        """ ApplyChanges(self: EditorPart) -> bool """
        ...

    def SyncChanges(self): # -> 
        """ SyncChanges(self: EditorPart) """
        ...


class AppearanceEditorPart(EditorPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ AppearanceEditorPart() """
    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: AppearanceEditorPart) -> str
        Set: DefaultButton(self: AppearanceEditorPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: AppearanceEditorPart) -> str
        Set: Title(self: AppearanceEditorPart) = value
        """
        ...



class BehaviorEditorPart(EditorPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ BehaviorEditorPart() """
    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: BehaviorEditorPart) -> str
        Set: DefaultButton(self: BehaviorEditorPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: BehaviorEditorPart) -> str
        Set: Title(self: BehaviorEditorPart) = value
        """
        ...



class CatalogPart(Part): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def DisplayTitle(self) -> str:
        """ Get: DisplayTitle(self: CatalogPart) -> str """
        ...

    @property
    def WebPartManager(self):
        ...

    @property
    def Zone(self):
        ...


    def GetAvailableWebPartDescriptions(self) -> WebPartDescriptionCollection:
        """ GetAvailableWebPartDescriptions(self: CatalogPart) -> WebPartDescriptionCollection """
        ...

    def GetWebPart(self, description:WebPartDescription) -> WebPart:
        """ GetWebPart(self: CatalogPart, description: WebPartDescription) -> WebPart """
        ...


class CatalogPartChrome: # skipped bases: <type 'object'>, <type 'object'>
    """ CatalogPartChrome(zone: CatalogZoneBase) """
    @property
    def Zone(self):
        ...


    def CreateCatalogPartChromeStyle(self, *args): #cannot find CLR method
        """ CreateCatalogPartChromeStyle(self: CatalogPartChrome, catalogPart: CatalogPart, chromeType: PartChromeType) -> Style """
        ...

    def PerformPreRender(self): # -> 
        """ PerformPreRender(self: CatalogPartChrome) """
        ...

    def RenderCatalogPart(self, writer:HtmlTextWriter, catalogPart:CatalogPart): # -> 
        """ RenderCatalogPart(self: CatalogPartChrome, writer: HtmlTextWriter, catalogPart: CatalogPart) """
        ...

    def RenderPartContents(self, *args): #cannot find CLR method
        """ RenderPartContents(self: CatalogPartChrome, writer: HtmlTextWriter, catalogPart: CatalogPart) """
        ...


class CatalogPartCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    CatalogPartCollection()
    CatalogPartCollection(catalogParts: ICollection)
    CatalogPartCollection(existingCatalogParts: CatalogPartCollection, catalogParts: ICollection)
    """
    def Contains(self, catalogPart:CatalogPart) -> bool:
        """ Contains(self: CatalogPartCollection, catalogPart: CatalogPart) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CatalogPartCollection, array: Array[CatalogPart], index: int) """
        ...

    def IndexOf(self, catalogPart:CatalogPart) -> int:
        """ IndexOf(self: CatalogPartCollection, catalogPart: CatalogPart) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *__args:ICollection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, catalogParts: ICollection)
        __new__(cls: type, existingCatalogParts: CatalogPartCollection, catalogParts: ICollection)
        """
        ...

    Empty: CatalogPartCollection = ...


class WebZone(CompositeControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: WebZone) -> str
        Set: BackImageUrl(self: WebZone) = value
        """
        ...

    @property
    def EmptyZoneText(self) -> str:
        """
        Get: EmptyZoneText(self: WebZone) -> str
        Set: EmptyZoneText(self: WebZone) = value
        """
        ...

    @property
    def EmptyZoneTextStyle(self) -> Style:
        """ Get: EmptyZoneTextStyle(self: WebZone) -> Style """
        ...

    @property
    def ErrorStyle(self) -> Style:
        """ Get: ErrorStyle(self: WebZone) -> Style """
        ...

    @property
    def FooterStyle(self) -> TitleStyle:
        """ Get: FooterStyle(self: WebZone) -> TitleStyle """
        ...

    @property
    def HasFooter(self):
        ...

    @property
    def HasHeader(self):
        ...

    @property
    def HeaderStyle(self) -> TitleStyle:
        """ Get: HeaderStyle(self: WebZone) -> TitleStyle """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: WebZone) -> str
        Set: HeaderText(self: WebZone) = value
        """
        ...

    @property
    def Padding(self) -> int:
        """
        Get: Padding(self: WebZone) -> int
        Set: Padding(self: WebZone) = value
        """
        ...

    @property
    def PartChromePadding(self) -> Unit:
        """
        Get: PartChromePadding(self: WebZone) -> Unit
        Set: PartChromePadding(self: WebZone) = value
        """
        ...

    @property
    def PartChromeStyle(self) -> Style:
        """ Get: PartChromeStyle(self: WebZone) -> Style """
        ...

    @property
    def PartChromeType(self) -> PartChromeType:
        """
        Get: PartChromeType(self: WebZone) -> PartChromeType
        Set: PartChromeType(self: WebZone) = value
        """
        ...

    @property
    def PartStyle(self) -> TableStyle:
        """ Get: PartStyle(self: WebZone) -> TableStyle """
        ...

    @property
    def PartTitleStyle(self) -> TitleStyle:
        """ Get: PartTitleStyle(self: WebZone) -> TitleStyle """
        ...

    @property
    def RenderClientScript(self):
        ...

    @property
    def VerbButtonType(self) -> ButtonType:
        """
        Get: VerbButtonType(self: WebZone) -> ButtonType
        Set: VerbButtonType(self: WebZone) = value
        """
        ...

    @property
    def VerbStyle(self) -> Style:
        """ Get: VerbStyle(self: WebZone) -> Style """
        ...

    @property
    def WebPartManager(self):
        ...


    def GetEffectiveChromeType(self, part:Part) -> PartChromeType:
        """ GetEffectiveChromeType(self: WebZone, part: Part) -> PartChromeType """
        ...

    def RenderBeginTag(self, writer:HtmlTextWriter): # -> 
        """ RenderBeginTag(self: WebZone, writer: HtmlTextWriter) """
        ...

    def RenderBody(self, *args): #cannot find CLR method
        """ RenderBody(self: WebZone, writer: HtmlTextWriter) """
        ...

    def RenderFooter(self, *args): #cannot find CLR method
        """ RenderFooter(self: WebZone, writer: HtmlTextWriter) """
        ...

    def RenderHeader(self, *args): #cannot find CLR method
        """ RenderHeader(self: WebZone, writer: HtmlTextWriter) """
        ...


class ToolZone(IPostBackEventHandler, WebZone): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AssociatedDisplayModes(self) -> WebPartDisplayModeCollection:
        """ Get: AssociatedDisplayModes(self: ToolZone) -> WebPartDisplayModeCollection """
        ...

    @property
    def Display(self):
        ...

    @property
    def EditUIStyle(self) -> Style:
        """ Get: EditUIStyle(self: ToolZone) -> Style """
        ...

    @property
    def HeaderCloseVerb(self) -> WebPartVerb:
        """ Get: HeaderCloseVerb(self: ToolZone) -> WebPartVerb """
        ...

    @property
    def HeaderVerbStyle(self) -> Style:
        """ Get: HeaderVerbStyle(self: ToolZone) -> Style """
        ...

    @property
    def InstructionText(self) -> str:
        """
        Get: InstructionText(self: ToolZone) -> str
        Set: InstructionText(self: ToolZone) = value
        """
        ...

    @property
    def InstructionTextStyle(self) -> Style:
        """ Get: InstructionTextStyle(self: ToolZone) -> Style """
        ...

    @property
    def LabelStyle(self) -> Style:
        """ Get: LabelStyle(self: ToolZone) -> Style """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: ToolZone) -> bool
        Set: Visible(self: ToolZone) = value
        """
        ...


    def Close(self, *args): #cannot find CLR method
        """ Close(self: ToolZone) """
        ...

    def OnDisplayModeChanged(self, *args): #cannot find CLR method
        """ OnDisplayModeChanged(self: ToolZone, sender: object, e: WebPartDisplayModeEventArgs) """
        ...

    def OnSelectedWebPartChanged(self, *args): #cannot find CLR method
        """ OnSelectedWebPartChanged(self: ToolZone, sender: object, e: WebPartEventArgs) """
        ...

    def RenderVerb(self, *args): #cannot find CLR method
        """ RenderVerb(self: ToolZone, writer: HtmlTextWriter, verb: WebPartVerb) """
        ...

    def RenderVerbs(self, *args): #cannot find CLR method
        """ RenderVerbs(self: ToolZone, writer: HtmlTextWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, associatedDisplayModes: ICollection)
        __new__(cls: type, associatedDisplayMode: WebPartDisplayMode)
        """
        ...


class CatalogZoneBase(IPostBackDataHandler, ToolZone): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AddVerb(self) -> WebPartVerb:
        """ Get: AddVerb(self: CatalogZoneBase) -> WebPartVerb """
        ...

    @property
    def CatalogPartChrome(self) -> CatalogPartChrome:
        """ Get: CatalogPartChrome(self: CatalogZoneBase) -> CatalogPartChrome """
        ...

    @property
    def CatalogParts(self) -> CatalogPartCollection:
        """ Get: CatalogParts(self: CatalogZoneBase) -> CatalogPartCollection """
        ...

    @property
    def CloseVerb(self) -> WebPartVerb:
        """ Get: CloseVerb(self: CatalogZoneBase) -> WebPartVerb """
        ...

    @property
    def EmptyZoneText(self) -> str:
        """
        Get: EmptyZoneText(self: CatalogZoneBase) -> str
        Set: EmptyZoneText(self: CatalogZoneBase) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: CatalogZoneBase) -> str
        Set: HeaderText(self: CatalogZoneBase) = value
        """
        ...

    @property
    def PartLinkStyle(self) -> Style:
        """ Get: PartLinkStyle(self: CatalogZoneBase) -> Style """
        ...

    @property
    def SelectedCatalogPartID(self) -> str:
        """
        Get: SelectedCatalogPartID(self: CatalogZoneBase) -> str
        Set: SelectedCatalogPartID(self: CatalogZoneBase) = value
        """
        ...

    @property
    def SelectedPartLinkStyle(self) -> Style:
        """ Get: SelectedPartLinkStyle(self: CatalogZoneBase) -> Style """
        ...

    @property
    def SelectTargetZoneText(self) -> str:
        """
        Get: SelectTargetZoneText(self: CatalogZoneBase) -> str
        Set: SelectTargetZoneText(self: CatalogZoneBase) = value
        """
        ...

    @property
    def ShowCatalogIcons(self) -> bool:
        """
        Get: ShowCatalogIcons(self: CatalogZoneBase) -> bool
        Set: ShowCatalogIcons(self: CatalogZoneBase) = value
        """
        ...


    def CreateCatalogPartChrome(self, *args): #cannot find CLR method
        """ CreateCatalogPartChrome(self: CatalogZoneBase) -> CatalogPartChrome """
        ...

    def CreateCatalogParts(self, *args): #cannot find CLR method
        """ CreateCatalogParts(self: CatalogZoneBase) -> CatalogPartCollection """
        ...

    def InvalidateCatalogParts(self, *args): #cannot find CLR method
        """ InvalidateCatalogParts(self: CatalogZoneBase) """
        ...

    def RenderCatalogPartLinks(self, *args): #cannot find CLR method
        """ RenderCatalogPartLinks(self: CatalogZoneBase, writer: HtmlTextWriter) """
        ...


class CatalogZone(CatalogZoneBase): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IPostBackDataHandler'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ CatalogZone() """
    @property
    def ZoneTemplate(self) -> ITemplate:
        """
        Get: ZoneTemplate(self: CatalogZone) -> ITemplate
        Set: ZoneTemplate(self: CatalogZone) = value
        """
        ...



class ConnectionConsumerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ConnectionConsumerAttribute(displayName: str)
    ConnectionConsumerAttribute(displayName: str, id: str)
    ConnectionConsumerAttribute(displayName: str, connectionPointType: Type)
    ConnectionConsumerAttribute(displayName: str, id: str, connectionPointType: Type)
    """
    @property
    def AllowsMultipleConnections(self) -> bool:
        """
        Get: AllowsMultipleConnections(self: ConnectionConsumerAttribute) -> bool
        Set: AllowsMultipleConnections(self: ConnectionConsumerAttribute) = value
        """
        ...

    @property
    def ConnectionPointType(self) -> Type:
        """ Get: ConnectionPointType(self: ConnectionConsumerAttribute) -> Type """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ConnectionConsumerAttribute) -> str """
        ...

    @property
    def DisplayNameValue(self):
        ...

    @property
    def ID(self) -> str:
        """ Get: ID(self: ConnectionConsumerAttribute) -> str """
        ...


    def __new__(cls, displayName:str, *__args:str) -> Self:
        """
        __new__(cls: type, displayName: str)
        __new__(cls: type, displayName: str, id: str)
        __new__(cls: type, displayName: str, connectionPointType: Type)
        __new__(cls: type, displayName: str, id: str, connectionPointType: Type)
        """
        ...


class ConnectionInterfaceCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ConnectionInterfaceCollection()
    ConnectionInterfaceCollection(connectionInterfaces: ICollection)
    ConnectionInterfaceCollection(existingConnectionInterfaces: ConnectionInterfaceCollection, connectionInterfaces: ICollection)
    """
    def Contains(self, value:Type) -> bool:
        """ Contains(self: ConnectionInterfaceCollection, value: Type) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ConnectionInterfaceCollection, array: Array[Type], index: int) """
        ...

    def IndexOf(self, value:Type) -> int:
        """ IndexOf(self: ConnectionInterfaceCollection, value: Type) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *__args:ICollection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionInterfaces: ICollection)
        __new__(cls: type, existingConnectionInterfaces: ConnectionInterfaceCollection, connectionInterfaces: ICollection)
        """
        ...

    Empty: ConnectionInterfaceCollection = ...


class ConnectionPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowsMultipleConnections(self) -> bool:
        """ Get: AllowsMultipleConnections(self: ConnectionPoint) -> bool """
        ...

    @property
    def ControlType(self) -> Type:
        """ Get: ControlType(self: ConnectionPoint) -> Type """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ConnectionPoint) -> str """
        ...

    @property
    def ID(self) -> str:
        """ Get: ID(self: ConnectionPoint) -> str """
        ...

    @property
    def InterfaceType(self) -> Type:
        """ Get: InterfaceType(self: ConnectionPoint) -> Type """
        ...


    def GetEnabled(self, control:Control) -> bool:
        """ GetEnabled(self: ConnectionPoint, control: Control) -> bool """
        ...

    DefaultID: str = ...


class ConnectionProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ConnectionProviderAttribute(displayName: str)
    ConnectionProviderAttribute(displayName: str, id: str)
    ConnectionProviderAttribute(displayName: str, connectionPointType: Type)
    ConnectionProviderAttribute(displayName: str, id: str, connectionPointType: Type)
    """
    @property
    def AllowsMultipleConnections(self) -> bool:
        """
        Get: AllowsMultipleConnections(self: ConnectionProviderAttribute) -> bool
        Set: AllowsMultipleConnections(self: ConnectionProviderAttribute) = value
        """
        ...

    @property
    def ConnectionPointType(self) -> Type:
        """ Get: ConnectionPointType(self: ConnectionProviderAttribute) -> Type """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ConnectionProviderAttribute) -> str """
        ...

    @property
    def DisplayNameValue(self):
        ...

    @property
    def ID(self) -> str:
        """ Get: ID(self: ConnectionProviderAttribute) -> str """
        ...


    def __new__(cls, displayName:str, *__args:str) -> Self:
        """
        __new__(cls: type, displayName: str)
        __new__(cls: type, displayName: str, id: str)
        __new__(cls: type, displayName: str, connectionPointType: Type)
        __new__(cls: type, displayName: str, id: str, connectionPointType: Type)
        """
        ...


class ConnectionsZone(ToolZone): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ConnectionsZone() """
    @property
    def CancelVerb(self) -> WebPartVerb:
        """ Get: CancelVerb(self: ConnectionsZone) -> WebPartVerb """
        ...

    @property
    def CloseVerb(self) -> WebPartVerb:
        """ Get: CloseVerb(self: ConnectionsZone) -> WebPartVerb """
        ...

    @property
    def ConfigureConnectionTitle(self) -> str:
        """
        Get: ConfigureConnectionTitle(self: ConnectionsZone) -> str
        Set: ConfigureConnectionTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConfigureVerb(self) -> WebPartVerb:
        """ Get: ConfigureVerb(self: ConnectionsZone) -> WebPartVerb """
        ...

    @property
    def ConnectToConsumerInstructionText(self) -> str:
        """
        Get: ConnectToConsumerInstructionText(self: ConnectionsZone) -> str
        Set: ConnectToConsumerInstructionText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectToConsumerText(self) -> str:
        """
        Get: ConnectToConsumerText(self: ConnectionsZone) -> str
        Set: ConnectToConsumerText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectToConsumerTitle(self) -> str:
        """
        Get: ConnectToConsumerTitle(self: ConnectionsZone) -> str
        Set: ConnectToConsumerTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectToProviderInstructionText(self) -> str:
        """
        Get: ConnectToProviderInstructionText(self: ConnectionsZone) -> str
        Set: ConnectToProviderInstructionText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectToProviderText(self) -> str:
        """
        Get: ConnectToProviderText(self: ConnectionsZone) -> str
        Set: ConnectToProviderText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectToProviderTitle(self) -> str:
        """
        Get: ConnectToProviderTitle(self: ConnectionsZone) -> str
        Set: ConnectToProviderTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConnectVerb(self) -> WebPartVerb:
        """ Get: ConnectVerb(self: ConnectionsZone) -> WebPartVerb """
        ...

    @property
    def ConsumersInstructionText(self) -> str:
        """
        Get: ConsumersInstructionText(self: ConnectionsZone) -> str
        Set: ConsumersInstructionText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ConsumersTitle(self) -> str:
        """
        Get: ConsumersTitle(self: ConnectionsZone) -> str
        Set: ConsumersTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def DisconnectVerb(self) -> WebPartVerb:
        """ Get: DisconnectVerb(self: ConnectionsZone) -> WebPartVerb """
        ...

    @property
    def EmptyZoneText(self) -> str:
        """
        Get: EmptyZoneText(self: ConnectionsZone) -> str
        Set: EmptyZoneText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ExistingConnectionErrorMessage(self) -> str:
        """
        Get: ExistingConnectionErrorMessage(self: ConnectionsZone) -> str
        Set: ExistingConnectionErrorMessage(self: ConnectionsZone) = value
        """
        ...

    @property
    def GetFromText(self) -> str:
        """
        Get: GetFromText(self: ConnectionsZone) -> str
        Set: GetFromText(self: ConnectionsZone) = value
        """
        ...

    @property
    def GetText(self) -> str:
        """
        Get: GetText(self: ConnectionsZone) -> str
        Set: GetText(self: ConnectionsZone) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: ConnectionsZone) -> str
        Set: HeaderText(self: ConnectionsZone) = value
        """
        ...

    @property
    def InstructionTitle(self) -> str:
        """
        Get: InstructionTitle(self: ConnectionsZone) -> str
        Set: InstructionTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def NewConnectionErrorMessage(self) -> str:
        """
        Get: NewConnectionErrorMessage(self: ConnectionsZone) -> str
        Set: NewConnectionErrorMessage(self: ConnectionsZone) = value
        """
        ...

    @property
    def NoExistingConnectionInstructionText(self) -> str:
        """
        Get: NoExistingConnectionInstructionText(self: ConnectionsZone) -> str
        Set: NoExistingConnectionInstructionText(self: ConnectionsZone) = value
        """
        ...

    @property
    def NoExistingConnectionTitle(self) -> str:
        """
        Get: NoExistingConnectionTitle(self: ConnectionsZone) -> str
        Set: NoExistingConnectionTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def PartChromeType(self) -> PartChromeType:
        """
        Get: PartChromeType(self: ConnectionsZone) -> PartChromeType
        Set: PartChromeType(self: ConnectionsZone) = value
        """
        ...

    @property
    def ProvidersInstructionText(self) -> str:
        """
        Get: ProvidersInstructionText(self: ConnectionsZone) -> str
        Set: ProvidersInstructionText(self: ConnectionsZone) = value
        """
        ...

    @property
    def ProvidersTitle(self) -> str:
        """
        Get: ProvidersTitle(self: ConnectionsZone) -> str
        Set: ProvidersTitle(self: ConnectionsZone) = value
        """
        ...

    @property
    def SendText(self) -> str:
        """
        Get: SendText(self: ConnectionsZone) -> str
        Set: SendText(self: ConnectionsZone) = value
        """
        ...

    @property
    def SendToText(self) -> str:
        """
        Get: SendToText(self: ConnectionsZone) -> str
        Set: SendToText(self: ConnectionsZone) = value
        """
        ...

    @property
    def WebPartToConnect(self):
        ...



class ConsumerConnectionPoint(ConnectionPoint): # skipped bases: <type 'object'>
    """ ConsumerConnectionPoint(callbackMethod: MethodInfo, interfaceType: Type, controlType: Type, displayName: str, id: str, allowsMultipleConnections: bool) """
    def SetObject(self, control:Control, data:object): # -> 
        """ SetObject(self: ConsumerConnectionPoint, control: Control, data: object) """
        ...

    def SupportsConnection(self, control:Control, secondaryInterfaces:ConnectionInterfaceCollection) -> bool:
        """ SupportsConnection(self: ConsumerConnectionPoint, control: Control, secondaryInterfaces: ConnectionInterfaceCollection) -> bool """
        ...

    def __new__(cls, callbackMethod:MethodInfo, interfaceType:Type, controlType:Type, displayName:str, id:str, allowsMultipleConnections:bool) -> Self:
        """ __new__(cls: type, callbackMethod: MethodInfo, interfaceType: Type, controlType: Type, displayName: str, id: str, allowsMultipleConnections: bool) """
        ...


class ConsumerConnectionPointCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ConsumerConnectionPointCollection()
    ConsumerConnectionPointCollection(connectionPoints: ICollection)
    """
    @property
    def Default(self) -> ConsumerConnectionPoint:
        """ Get: Default(self: ConsumerConnectionPointCollection) -> ConsumerConnectionPoint """
        ...


    def Contains(self, connectionPoint:ConsumerConnectionPoint) -> bool:
        """ Contains(self: ConsumerConnectionPointCollection, connectionPoint: ConsumerConnectionPoint) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ConsumerConnectionPointCollection, array: Array[ConsumerConnectionPoint], index: int) """
        ...

    def IndexOf(self, connectionPoint:ConsumerConnectionPoint) -> int:
        """ IndexOf(self: ConsumerConnectionPointCollection, connectionPoint: ConsumerConnectionPoint) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, connectionPoints:ICollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionPoints: ICollection)
        """
        ...


class DeclarativeCatalogPart(CatalogPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ DeclarativeCatalogPart() """
    @property
    def AccessKey(self) -> str:
        """
        Get: AccessKey(self: DeclarativeCatalogPart) -> str
        Set: AccessKey(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: DeclarativeCatalogPart) -> Color
        Set: BackColor(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: DeclarativeCatalogPart) -> str
        Set: BackImageUrl(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: DeclarativeCatalogPart) -> Color
        Set: BorderColor(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: DeclarativeCatalogPart) -> BorderStyle
        Set: BorderStyle(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def BorderWidth(self) -> Unit:
        """
        Get: BorderWidth(self: DeclarativeCatalogPart) -> Unit
        Set: BorderWidth(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: DeclarativeCatalogPart) -> str
        Set: CssClass(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: DeclarativeCatalogPart) -> str
        Set: DefaultButton(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Direction(self) -> ContentDirection:
        """
        Get: Direction(self: DeclarativeCatalogPart) -> ContentDirection
        Set: Direction(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: DeclarativeCatalogPart) -> bool
        Set: Enabled(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def EnableTheming(self) -> bool:
        """
        Get: EnableTheming(self: DeclarativeCatalogPart) -> bool
        Set: EnableTheming(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: DeclarativeCatalogPart) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: DeclarativeCatalogPart) -> Color
        Set: ForeColor(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def GroupingText(self) -> str:
        """
        Get: GroupingText(self: DeclarativeCatalogPart) -> str
        Set: GroupingText(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Height(self) -> Unit:
        """
        Get: Height(self: DeclarativeCatalogPart) -> Unit
        Set: Height(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: DeclarativeCatalogPart) -> HorizontalAlign
        Set: HorizontalAlign(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def ScrollBars(self) -> ScrollBars:
        """
        Get: ScrollBars(self: DeclarativeCatalogPart) -> ScrollBars
        Set: ScrollBars(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def SkinID(self) -> str:
        """
        Get: SkinID(self: DeclarativeCatalogPart) -> str
        Set: SkinID(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: DeclarativeCatalogPart) -> Int16
        Set: TabIndex(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: DeclarativeCatalogPart) -> str
        Set: Title(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: DeclarativeCatalogPart) -> str
        Set: ToolTip(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: DeclarativeCatalogPart) -> bool
        Set: Visible(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def WebPartsListUserControlPath(self) -> str:
        """
        Get: WebPartsListUserControlPath(self: DeclarativeCatalogPart) -> str
        Set: WebPartsListUserControlPath(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def WebPartsTemplate(self) -> ITemplate:
        """
        Get: WebPartsTemplate(self: DeclarativeCatalogPart) -> ITemplate
        Set: WebPartsTemplate(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Width(self) -> Unit:
        """
        Get: Width(self: DeclarativeCatalogPart) -> Unit
        Set: Width(self: DeclarativeCatalogPart) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: DeclarativeCatalogPart) -> bool
        Set: Wrap(self: DeclarativeCatalogPart) = value
        """
        ...



class EditorPartChrome: # skipped bases: <type 'object'>, <type 'object'>
    """ EditorPartChrome(zone: EditorZoneBase) """
    @property
    def Zone(self):
        ...


    def CreateEditorPartChromeStyle(self, *args): #cannot find CLR method
        """ CreateEditorPartChromeStyle(self: EditorPartChrome, editorPart: EditorPart, chromeType: PartChromeType) -> Style """
        ...

    def PerformPreRender(self): # -> 
        """ PerformPreRender(self: EditorPartChrome) """
        ...

    def RenderEditorPart(self, writer:HtmlTextWriter, editorPart:EditorPart): # -> 
        """ RenderEditorPart(self: EditorPartChrome, writer: HtmlTextWriter, editorPart: EditorPart) """
        ...

    def RenderPartContents(self, *args): #cannot find CLR method
        """ RenderPartContents(self: EditorPartChrome, writer: HtmlTextWriter, editorPart: EditorPart) """
        ...


class EditorPartCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    EditorPartCollection()
    EditorPartCollection(editorParts: ICollection)
    EditorPartCollection(existingEditorParts: EditorPartCollection, editorParts: ICollection)
    """
    def Contains(self, editorPart:EditorPart) -> bool:
        """ Contains(self: EditorPartCollection, editorPart: EditorPart) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: EditorPartCollection, array: Array[EditorPart], index: int) """
        ...

    def IndexOf(self, editorPart:EditorPart) -> int:
        """ IndexOf(self: EditorPartCollection, editorPart: EditorPart) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *__args:ICollection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, editorParts: ICollection)
        __new__(cls: type, existingEditorParts: EditorPartCollection, editorParts: ICollection)
        """
        ...

    Empty: EditorPartCollection = ...


class EditorZoneBase(ToolZone): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def ApplyVerb(self) -> WebPartVerb:
        """ Get: ApplyVerb(self: EditorZoneBase) -> WebPartVerb """
        ...

    @property
    def CancelVerb(self) -> WebPartVerb:
        """ Get: CancelVerb(self: EditorZoneBase) -> WebPartVerb """
        ...

    @property
    def EditorPartChrome(self) -> EditorPartChrome:
        """ Get: EditorPartChrome(self: EditorZoneBase) -> EditorPartChrome """
        ...

    @property
    def EditorParts(self) -> EditorPartCollection:
        """ Get: EditorParts(self: EditorZoneBase) -> EditorPartCollection """
        ...

    @property
    def EmptyZoneText(self) -> str:
        """
        Get: EmptyZoneText(self: EditorZoneBase) -> str
        Set: EmptyZoneText(self: EditorZoneBase) = value
        """
        ...

    @property
    def ErrorText(self) -> str:
        """
        Get: ErrorText(self: EditorZoneBase) -> str
        Set: ErrorText(self: EditorZoneBase) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: EditorZoneBase) -> str
        Set: HeaderText(self: EditorZoneBase) = value
        """
        ...

    @property
    def OKVerb(self) -> WebPartVerb:
        """ Get: OKVerb(self: EditorZoneBase) -> WebPartVerb """
        ...

    @property
    def WebPartToEdit(self):
        ...


    def CreateEditorPartChrome(self, *args): #cannot find CLR method
        """ CreateEditorPartChrome(self: EditorZoneBase) -> EditorPartChrome """
        ...

    def CreateEditorParts(self, *args): #cannot find CLR method
        """ CreateEditorParts(self: EditorZoneBase) -> EditorPartCollection """
        ...

    def InvalidateEditorParts(self, *args): #cannot find CLR method
        """ InvalidateEditorParts(self: EditorZoneBase) """
        ...


class EditorZone(EditorZoneBase): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ EditorZone() """
    @property
    def ZoneTemplate(self) -> ITemplate:
        """
        Get: ZoneTemplate(self: EditorZone) -> ITemplate
        Set: ZoneTemplate(self: EditorZone) = value
        """
        ...



class ITrackingPersonalizable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TracksChanges(self) -> bool:
        """ Get: TracksChanges(self: ITrackingPersonalizable) -> bool """
        ...


    def BeginLoad(self): # -> 
        """ BeginLoad(self: ITrackingPersonalizable) """
        ...

    def BeginSave(self): # -> 
        """ BeginSave(self: ITrackingPersonalizable) """
        ...

    def EndLoad(self): # -> 
        """ EndLoad(self: ITrackingPersonalizable) """
        ...

    def EndSave(self): # -> 
        """ EndSave(self: ITrackingPersonalizable) """
        ...


class IWebActionable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Verbs(self) -> WebPartVerbCollection:
        """ Get: Verbs(self: IWebActionable) -> WebPartVerbCollection """
        ...



class IWebEditable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WebBrowsableObject(self) -> object:
        """ Get: WebBrowsableObject(self: IWebEditable) -> object """
        ...


    def CreateEditorParts(self) -> EditorPartCollection:
        """ CreateEditorParts(self: IWebEditable) -> EditorPartCollection """
        ...


class IWebPart: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CatalogIconImageUrl(self) -> str:
        """
        Get: CatalogIconImageUrl(self: IWebPart) -> str
        Set: CatalogIconImageUrl(self: IWebPart) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IWebPart) -> str
        Set: Description(self: IWebPart) = value
        """
        ...

    @property
    def Subtitle(self) -> str:
        """ Get: Subtitle(self: IWebPart) -> str """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: IWebPart) -> str
        Set: Title(self: IWebPart) = value
        """
        ...

    @property
    def TitleIconImageUrl(self) -> str:
        """
        Get: TitleIconImageUrl(self: IWebPart) -> str
        Set: TitleIconImageUrl(self: IWebPart) = value
        """
        ...

    @property
    def TitleUrl(self) -> str:
        """
        Get: TitleUrl(self: IWebPart) -> str
        Set: TitleUrl(self: IWebPart) = value
        """
        ...



class WebPart(IWebEditable, IWebPart, IWebActionable, Part): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AllowClose(self) -> bool:
        """
        Get: AllowClose(self: WebPart) -> bool
        Set: AllowClose(self: WebPart) = value
        """
        ...

    @property
    def AllowConnect(self) -> bool:
        """
        Get: AllowConnect(self: WebPart) -> bool
        Set: AllowConnect(self: WebPart) = value
        """
        ...

    @property
    def AllowEdit(self) -> bool:
        """
        Get: AllowEdit(self: WebPart) -> bool
        Set: AllowEdit(self: WebPart) = value
        """
        ...

    @property
    def AllowHide(self) -> bool:
        """
        Get: AllowHide(self: WebPart) -> bool
        Set: AllowHide(self: WebPart) = value
        """
        ...

    @property
    def AllowMinimize(self) -> bool:
        """
        Get: AllowMinimize(self: WebPart) -> bool
        Set: AllowMinimize(self: WebPart) = value
        """
        ...

    @property
    def AllowZoneChange(self) -> bool:
        """
        Get: AllowZoneChange(self: WebPart) -> bool
        Set: AllowZoneChange(self: WebPart) = value
        """
        ...

    @property
    def AuthorizationFilter(self) -> str:
        """
        Get: AuthorizationFilter(self: WebPart) -> str
        Set: AuthorizationFilter(self: WebPart) = value
        """
        ...

    @property
    def ConnectErrorMessage(self) -> str:
        """ Get: ConnectErrorMessage(self: WebPart) -> str """
        ...

    @property
    def Direction(self) -> ContentDirection:
        """
        Get: Direction(self: WebPart) -> ContentDirection
        Set: Direction(self: WebPart) = value
        """
        ...

    @property
    def DisplayTitle(self) -> str:
        """ Get: DisplayTitle(self: WebPart) -> str """
        ...

    @property
    def ExportMode(self) -> WebPartExportMode:
        """
        Get: ExportMode(self: WebPart) -> WebPartExportMode
        Set: ExportMode(self: WebPart) = value
        """
        ...

    @property
    def HasSharedData(self) -> bool:
        """ Get: HasSharedData(self: WebPart) -> bool """
        ...

    @property
    def HasUserData(self) -> bool:
        """ Get: HasUserData(self: WebPart) -> bool """
        ...

    @property
    def Height(self) -> Unit:
        """
        Get: Height(self: WebPart) -> Unit
        Set: Height(self: WebPart) = value
        """
        ...

    @property
    def HelpMode(self) -> WebPartHelpMode:
        """
        Get: HelpMode(self: WebPart) -> WebPartHelpMode
        Set: HelpMode(self: WebPart) = value
        """
        ...

    @property
    def HelpUrl(self) -> str:
        """
        Get: HelpUrl(self: WebPart) -> str
        Set: HelpUrl(self: WebPart) = value
        """
        ...

    @property
    def Hidden(self) -> bool:
        """
        Get: Hidden(self: WebPart) -> bool
        Set: Hidden(self: WebPart) = value
        """
        ...

    @property
    def ImportErrorMessage(self) -> str:
        """
        Get: ImportErrorMessage(self: WebPart) -> str
        Set: ImportErrorMessage(self: WebPart) = value
        """
        ...

    @property
    def IsClosed(self) -> bool:
        """ Get: IsClosed(self: WebPart) -> bool """
        ...

    @property
    def IsShared(self) -> bool:
        """ Get: IsShared(self: WebPart) -> bool """
        ...

    @property
    def IsStandalone(self) -> bool:
        """ Get: IsStandalone(self: WebPart) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: WebPart) -> bool """
        ...

    @property
    def WebPartManager(self):
        ...

    @property
    def Width(self) -> Unit:
        """
        Get: Width(self: WebPart) -> Unit
        Set: Width(self: WebPart) = value
        """
        ...

    @property
    def Zone(self) -> WebPartZoneBase:
        """ Get: Zone(self: WebPart) -> WebPartZoneBase """
        ...

    @property
    def ZoneIndex(self) -> int:
        """ Get: ZoneIndex(self: WebPart) -> int """
        ...


    def OnClosing(self, *args): #cannot find CLR method
        """ OnClosing(self: WebPart, e: EventArgs) """
        ...

    def OnConnectModeChanged(self, *args): #cannot find CLR method
        """ OnConnectModeChanged(self: WebPart, e: EventArgs) """
        ...

    def OnDeleting(self, *args): #cannot find CLR method
        """ OnDeleting(self: WebPart, e: EventArgs) """
        ...

    def OnEditModeChanged(self, *args): #cannot find CLR method
        """ OnEditModeChanged(self: WebPart, e: EventArgs) """
        ...

    @staticmethod
    def SetPersonalizationDirty(control:Control): # -> 
        """ SetPersonalizationDirty(control: Control) """
        ...


class ProxyWebPart(WebPart): # skipped bases: <type 'IWebActionable'>, <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IWebEditable'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'IWebPart'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def GenericWebPartID(self) -> str:
        """ Get: GenericWebPartID(self: ProxyWebPart) -> str """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: ProxyWebPart) -> str
        Set: ID(self: ProxyWebPart) = value
        """
        ...

    @property
    def OriginalID(self) -> str:
        """ Get: OriginalID(self: ProxyWebPart) -> str """
        ...

    @property
    def OriginalPath(self) -> str:
        """ Get: OriginalPath(self: ProxyWebPart) -> str """
        ...

    @property
    def OriginalTypeName(self) -> str:
        """ Get: OriginalTypeName(self: ProxyWebPart) -> str """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, webPart: WebPart)
        __new__(cls: type, originalID: str, originalTypeName: str, originalPath: str, genericWebPartID: str)
        """
        ...


class ErrorWebPart(ITrackingPersonalizable, ProxyWebPart): # skipped bases: <type 'IWebActionable'>, <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IWebEditable'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'IWebPart'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ErrorWebPart(originalID: str, originalTypeName: str, originalPath: str, genericWebPartID: str) """
    @property
    def ErrorMessage(self) -> str:
        """
        Get: ErrorMessage(self: ErrorWebPart) -> str
        Set: ErrorMessage(self: ErrorWebPart) = value
        """
        ...


    def EndLoadPersonalization(self, *args): #cannot find CLR method
        """ EndLoadPersonalization(self: ErrorWebPart) """
        ...


class FieldCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FieldCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, fieldValue:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FieldCallback, fieldValue: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FieldCallback, result: IAsyncResult) """
        ...

    def Invoke(self, fieldValue:object): # -> 
        """ Invoke(self: FieldCallback, fieldValue: object) """
        ...


class GenericWebPart(WebPart): # skipped bases: <type 'IWebActionable'>, <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IWebEditable'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'IWebPart'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def ChildControl(self) -> Control:
        """ Get: ChildControl(self: GenericWebPart) -> Control """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: GenericWebPart) -> str
        Set: ID(self: GenericWebPart) = value
        """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, control: Control) """
        ...


class ImportCatalogPart(CatalogPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ ImportCatalogPart() """
    @property
    def BrowseHelpText(self) -> str:
        """
        Get: BrowseHelpText(self: ImportCatalogPart) -> str
        Set: BrowseHelpText(self: ImportCatalogPart) = value
        """
        ...

    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: ImportCatalogPart) -> str
        Set: DefaultButton(self: ImportCatalogPart) = value
        """
        ...

    @property
    def ImportedPartLabelText(self) -> str:
        """
        Get: ImportedPartLabelText(self: ImportCatalogPart) -> str
        Set: ImportedPartLabelText(self: ImportCatalogPart) = value
        """
        ...

    @property
    def PartImportErrorLabelText(self) -> str:
        """
        Get: PartImportErrorLabelText(self: ImportCatalogPart) -> str
        Set: PartImportErrorLabelText(self: ImportCatalogPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ImportCatalogPart) -> str
        Set: Title(self: ImportCatalogPart) = value
        """
        ...

    @property
    def UploadButtonText(self) -> str:
        """
        Get: UploadButtonText(self: ImportCatalogPart) -> str
        Set: UploadButtonText(self: ImportCatalogPart) = value
        """
        ...

    @property
    def UploadHelpText(self) -> str:
        """
        Get: UploadHelpText(self: ImportCatalogPart) -> str
        Set: UploadHelpText(self: ImportCatalogPart) = value
        """
        ...



class IPersonalizable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IPersonalizable) -> bool """
        ...


    def Load(self, state:PersonalizationDictionary): # -> 
        """ Load(self: IPersonalizable, state: PersonalizationDictionary) """
        ...

    def Save(self, state:PersonalizationDictionary): # -> 
        """ Save(self: IPersonalizable, state: PersonalizationDictionary) """
        ...


class ITransformerConfigurationControl: # skipped bases: <type 'object'>
    """ no doc """
    Cancelled = ...
    Succeeded = ...


class IVersioningPersonalizable: # skipped bases: <type 'object'>
    """ no doc """
    def Load(self, unknownProperties:IDictionary): # -> 
        """ Load(self: IVersioningPersonalizable, unknownProperties: IDictionary) """
        ...


class IWebPartField: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Schema(self) -> PropertyDescriptor:
        """ Get: Schema(self: IWebPartField) -> PropertyDescriptor """
        ...


    def GetFieldValue(self, callback:FieldCallback): # -> 
        """ GetFieldValue(self: IWebPartField, callback: FieldCallback) """
        ...


class IWebPartParameters: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Schema(self) -> PropertyDescriptorCollection:
        """ Get: Schema(self: IWebPartParameters) -> PropertyDescriptorCollection """
        ...


    def GetParametersData(self, callback:ParametersCallback): # -> 
        """ GetParametersData(self: IWebPartParameters, callback: ParametersCallback) """
        ...

    def SetConsumerSchema(self, schema:PropertyDescriptorCollection): # -> 
        """ SetConsumerSchema(self: IWebPartParameters, schema: PropertyDescriptorCollection) """
        ...


class IWebPartRow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Schema(self) -> PropertyDescriptorCollection:
        """ Get: Schema(self: IWebPartRow) -> PropertyDescriptorCollection """
        ...


    def GetRowData(self, callback:RowCallback): # -> 
        """ GetRowData(self: IWebPartRow, callback: RowCallback) """
        ...


class IWebPartTable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Schema(self) -> PropertyDescriptorCollection:
        """ Get: Schema(self: IWebPartTable) -> PropertyDescriptorCollection """
        ...


    def GetTableData(self, callback:TableCallback): # -> 
        """ GetTableData(self: IWebPartTable, callback: TableCallback) """
        ...


class LayoutEditorPart(EditorPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ LayoutEditorPart() """
    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: LayoutEditorPart) -> str
        Set: DefaultButton(self: LayoutEditorPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: LayoutEditorPart) -> str
        Set: Title(self: LayoutEditorPart) = value
        """
        ...



class PageCatalogPart(CatalogPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ PageCatalogPart() """
    @property
    def AccessKey(self) -> str:
        """
        Get: AccessKey(self: PageCatalogPart) -> str
        Set: AccessKey(self: PageCatalogPart) = value
        """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: PageCatalogPart) -> Color
        Set: BackColor(self: PageCatalogPart) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: PageCatalogPart) -> str
        Set: BackImageUrl(self: PageCatalogPart) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: PageCatalogPart) -> Color
        Set: BorderColor(self: PageCatalogPart) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: PageCatalogPart) -> BorderStyle
        Set: BorderStyle(self: PageCatalogPart) = value
        """
        ...

    @property
    def BorderWidth(self) -> Unit:
        """
        Get: BorderWidth(self: PageCatalogPart) -> Unit
        Set: BorderWidth(self: PageCatalogPart) = value
        """
        ...

    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: PageCatalogPart) -> str
        Set: CssClass(self: PageCatalogPart) = value
        """
        ...

    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: PageCatalogPart) -> str
        Set: DefaultButton(self: PageCatalogPart) = value
        """
        ...

    @property
    def Direction(self) -> ContentDirection:
        """
        Get: Direction(self: PageCatalogPart) -> ContentDirection
        Set: Direction(self: PageCatalogPart) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: PageCatalogPart) -> bool
        Set: Enabled(self: PageCatalogPart) = value
        """
        ...

    @property
    def EnableTheming(self) -> bool:
        """
        Get: EnableTheming(self: PageCatalogPart) -> bool
        Set: EnableTheming(self: PageCatalogPart) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: PageCatalogPart) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: PageCatalogPart) -> Color
        Set: ForeColor(self: PageCatalogPart) = value
        """
        ...

    @property
    def GroupingText(self) -> str:
        """
        Get: GroupingText(self: PageCatalogPart) -> str
        Set: GroupingText(self: PageCatalogPart) = value
        """
        ...

    @property
    def Height(self) -> Unit:
        """
        Get: Height(self: PageCatalogPart) -> Unit
        Set: Height(self: PageCatalogPart) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: PageCatalogPart) -> HorizontalAlign
        Set: HorizontalAlign(self: PageCatalogPart) = value
        """
        ...

    @property
    def ScrollBars(self) -> ScrollBars:
        """
        Get: ScrollBars(self: PageCatalogPart) -> ScrollBars
        Set: ScrollBars(self: PageCatalogPart) = value
        """
        ...

    @property
    def SkinID(self) -> str:
        """
        Get: SkinID(self: PageCatalogPart) -> str
        Set: SkinID(self: PageCatalogPart) = value
        """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: PageCatalogPart) -> Int16
        Set: TabIndex(self: PageCatalogPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: PageCatalogPart) -> str
        Set: Title(self: PageCatalogPart) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: PageCatalogPart) -> str
        Set: ToolTip(self: PageCatalogPart) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: PageCatalogPart) -> bool
        Set: Visible(self: PageCatalogPart) = value
        """
        ...

    @property
    def Width(self) -> Unit:
        """
        Get: Width(self: PageCatalogPart) -> Unit
        Set: Width(self: PageCatalogPart) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: PageCatalogPart) -> bool
        Set: Wrap(self: PageCatalogPart) = value
        """
        ...



class ParametersCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ParametersCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, parametersData:IDictionary, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ParametersCallback, parametersData: IDictionary, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ParametersCallback, result: IAsyncResult) """
        ...

    def Invoke(self, parametersData:IDictionary): # -> 
        """ Invoke(self: ParametersCallback, parametersData: IDictionary) """
        ...


class PartChromeState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PartChromeState, values: Minimized (1), Normal (0) """
    Minimized: PartChromeState = ...
    Normal: PartChromeState = ...
    value__ = ...


class PartChromeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PartChromeType, values: BorderOnly (4), Default (0), None (2), TitleAndBorder (1), TitleOnly (3) """
    BorderOnly: PartChromeType = ...
    Default: PartChromeType = ...
    TitleAndBorder: PartChromeType = ...
    TitleOnly: PartChromeType = ...
    value__ = ...


class PersonalizableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PersonalizableAttribute()
    PersonalizableAttribute(isPersonalizable: bool)
    PersonalizableAttribute(scope: PersonalizationScope)
    PersonalizableAttribute(scope: PersonalizationScope, isSensitive: bool)
    """
    @property
    def IsPersonalizable(self) -> bool:
        """ Get: IsPersonalizable(self: PersonalizableAttribute) -> bool """
        ...

    @property
    def IsSensitive(self) -> bool:
        """ Get: IsSensitive(self: PersonalizableAttribute) -> bool """
        ...

    @property
    def Scope(self) -> PersonalizationScope:
        """ Get: Scope(self: PersonalizableAttribute) -> PersonalizationScope """
        ...


    @staticmethod
    def GetPersonalizableProperties(type:Type) -> ICollection:
        """ GetPersonalizableProperties(type: Type) -> ICollection """
        ...

    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, isPersonalizable: bool)
        __new__(cls: type, scope: PersonalizationScope)
        __new__(cls: type, scope: PersonalizationScope, isSensitive: bool)
        """
        ...

    Default: PersonalizableAttribute = ...
    NotPersonalizable: PersonalizableAttribute = ...
    Personalizable: PersonalizableAttribute = ...
    SharedPersonalizable: PersonalizableAttribute = ...
    UserPersonalizable: PersonalizableAttribute = ...


class PersonalizationAdministration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName() -> str
        Set: ApplicationName() = value
        """
        ...

    @property
    def Provider(self) -> PersonalizationProvider:
        """ Get: Provider() -> PersonalizationProvider """
        ...

    @property
    def Providers(self) -> PersonalizationProviderCollection:
        """ Get: Providers() -> PersonalizationProviderCollection """
        ...


    @staticmethod
    def FindInactiveUserState(pathToMatch, usernameToMatch, userInactiveSinceDate, pageIndex=None, pageSize=None, totalRecords=None) -> PersonalizationStateInfoCollection:
        """
        FindInactiveUserState(pathToMatch: str, usernameToMatch: str, userInactiveSinceDate: DateTime) -> PersonalizationStateInfoCollection
        FindInactiveUserState(pathToMatch: str, usernameToMatch: str, userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int)
        """
        ...

    @staticmethod
    def FindSharedState(pathToMatch, pageIndex=None, pageSize=None, totalRecords=None) -> PersonalizationStateInfoCollection:
        """
        FindSharedState(pathToMatch: str) -> PersonalizationStateInfoCollection
        FindSharedState(pathToMatch: str, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int)
        """
        ...

    @staticmethod
    def FindUserState(pathToMatch, usernameToMatch, pageIndex=None, pageSize=None, totalRecords=None) -> PersonalizationStateInfoCollection:
        """
        FindUserState(pathToMatch: str, usernameToMatch: str) -> PersonalizationStateInfoCollection
        FindUserState(pathToMatch: str, usernameToMatch: str, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int)
        """
        ...

    @staticmethod
    def GetAllInactiveUserState(userInactiveSinceDate, pageIndex=None, pageSize=None, totalRecords=None) -> PersonalizationStateInfoCollection:
        """
        GetAllInactiveUserState(userInactiveSinceDate: DateTime) -> PersonalizationStateInfoCollection
        GetAllInactiveUserState(userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int)
        """
        ...

    @staticmethod
    def GetAllState(scope, pageIndex=None, pageSize=None, totalRecords=None) -> PersonalizationStateInfoCollection:
        """
        GetAllState(scope: PersonalizationScope) -> PersonalizationStateInfoCollection
        GetAllState(scope: PersonalizationScope, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int)
        """
        ...

    @staticmethod
    def GetCountOfInactiveUserState(*__args:DateTime) -> int:
        """
        GetCountOfInactiveUserState(userInactiveSinceDate: DateTime) -> int
        GetCountOfInactiveUserState(pathToMatch: str, userInactiveSinceDate: DateTime) -> int
        """
        ...

    @staticmethod
    def GetCountOfState(scope:PersonalizationScope, pathToMatch:str = ...) -> int:
        """
        GetCountOfState(scope: PersonalizationScope) -> int
        GetCountOfState(scope: PersonalizationScope, pathToMatch: str) -> int
        """
        ...

    @staticmethod
    def GetCountOfUserState(usernameToMatch:str) -> int:
        """ GetCountOfUserState(usernameToMatch: str) -> int """
        ...

    @staticmethod
    def ResetAllState(scope:PersonalizationScope) -> int:
        """ ResetAllState(scope: PersonalizationScope) -> int """
        ...

    @staticmethod
    def ResetInactiveUserState(*__args:DateTime) -> int:
        """
        ResetInactiveUserState(userInactiveSinceDate: DateTime) -> int
        ResetInactiveUserState(path: str, userInactiveSinceDate: DateTime) -> int
        """
        ...

    @staticmethod
    def ResetSharedState(*__args:str) -> bool:
        """
        ResetSharedState(path: str) -> bool
        ResetSharedState(paths: Array[str]) -> int
        """
        ...

    @staticmethod
    def ResetState(data:PersonalizationStateInfoCollection) -> int:
        """ ResetState(data: PersonalizationStateInfoCollection) -> int """
        ...

    @staticmethod
    def ResetUserState(*__args:str) -> int:
        """
        ResetUserState(path: str) -> int
        ResetUserState(usernames: Array[str]) -> int
        ResetUserState(path: str, username: str) -> bool
        ResetUserState(path: str, usernames: Array[str]) -> int
        """
        ...

    __all__: list = ...


class PersonalizationDictionary(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    PersonalizationDictionary()
    PersonalizationDictionary(initialSize: int)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PersonalizationDictionary) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: PersonalizationDictionary) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: PersonalizationDictionary) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PersonalizationDictionary, array: Array[DictionaryEntry], index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class PersonalizationEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    PersonalizationEntry(value: object, scope: PersonalizationScope)
    PersonalizationEntry(value: object, scope: PersonalizationScope, isSensitive: bool)
    """
    @property
    def IsSensitive(self) -> bool:
        """
        Get: IsSensitive(self: PersonalizationEntry) -> bool
        Set: IsSensitive(self: PersonalizationEntry) = value
        """
        ...

    @property
    def Scope(self) -> PersonalizationScope:
        """
        Get: Scope(self: PersonalizationEntry) -> PersonalizationScope
        Set: Scope(self: PersonalizationEntry) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PersonalizationEntry) -> object
        Set: Value(self: PersonalizationEntry) = value
        """
        ...



class PersonalizationProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: PersonalizationProvider) -> str
        Set: ApplicationName(self: PersonalizationProvider) = value
        """
        ...


    def CreateSupportedUserCapabilities(self, *args): #cannot find CLR method
        """ CreateSupportedUserCapabilities(self: PersonalizationProvider) -> IList """
        ...

    def DetermineInitialScope(self, webPartManager:WebPartManager, loadedState:PersonalizationState) -> PersonalizationScope:
        """ DetermineInitialScope(self: PersonalizationProvider, webPartManager: WebPartManager, loadedState: PersonalizationState) -> PersonalizationScope """
        ...

    def DetermineUserCapabilities(self, webPartManager:WebPartManager) -> IDictionary:
        """ DetermineUserCapabilities(self: PersonalizationProvider, webPartManager: WebPartManager) -> IDictionary """
        ...

    def FindState(self, scope, query, pageIndex, pageSize, totalRecords) -> Tuple_[PersonalizationStateInfoCollection, int]:
        """ FindState(self: PersonalizationProvider, scope: PersonalizationScope, query: PersonalizationStateQuery, pageIndex: int, pageSize: int) -> (PersonalizationStateInfoCollection, int) """
        ...

    def GetCountOfState(self, scope:PersonalizationScope, query:PersonalizationStateQuery) -> int:
        """ GetCountOfState(self: PersonalizationProvider, scope: PersonalizationScope, query: PersonalizationStateQuery) -> int """
        ...

    def LoadPersonalizationBlobs(self, *args): #cannot find CLR method
        """ LoadPersonalizationBlobs(self: PersonalizationProvider, webPartManager: WebPartManager, path: str, userName: str, sharedDataBlob: Array[Byte], userDataBlob: Array[Byte]) -> (Array[Byte], Array[Byte]) """
        ...

    def LoadPersonalizationState(self, webPartManager:WebPartManager, ignoreCurrentUser:bool) -> PersonalizationState:
        """ LoadPersonalizationState(self: PersonalizationProvider, webPartManager: WebPartManager, ignoreCurrentUser: bool) -> PersonalizationState """
        ...

    def ResetPersonalizationBlob(self, *args): #cannot find CLR method
        """ ResetPersonalizationBlob(self: PersonalizationProvider, webPartManager: WebPartManager, path: str, userName: str) """
        ...

    def ResetPersonalizationState(self, webPartManager:WebPartManager): # -> 
        """ ResetPersonalizationState(self: PersonalizationProvider, webPartManager: WebPartManager) """
        ...

    def ResetState(self, scope:PersonalizationScope, paths:Array, usernames:Array) -> int:
        """ ResetState(self: PersonalizationProvider, scope: PersonalizationScope, paths: Array[str], usernames: Array[str]) -> int """
        ...

    def ResetUserState(self, path:str, userInactiveSinceDate:DateTime) -> int:
        """ ResetUserState(self: PersonalizationProvider, path: str, userInactiveSinceDate: DateTime) -> int """
        ...

    def SavePersonalizationBlob(self, *args): #cannot find CLR method
        """ SavePersonalizationBlob(self: PersonalizationProvider, webPartManager: WebPartManager, path: str, userName: str, dataBlob: Array[Byte]) """
        ...

    def SavePersonalizationState(self, state:PersonalizationState): # -> 
        """ SavePersonalizationState(self: PersonalizationProvider, state: PersonalizationState) """
        ...


class PersonalizationProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ PersonalizationProviderCollection() """
    pass

class PersonalizationScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PersonalizationScope, values: Shared (1), User (0) """
    Shared: PersonalizationScope = ...
    User: PersonalizationScope = ...
    value__ = ...


class PersonalizationState: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: PersonalizationState) -> bool """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: PersonalizationState) -> bool """
        ...

    @property
    def WebPartManager(self) -> WebPartManager:
        """ Get: WebPartManager(self: PersonalizationState) -> WebPartManager """
        ...


    def ApplyWebPartManagerPersonalization(self): # -> 
        """ ApplyWebPartManagerPersonalization(self: PersonalizationState) """
        ...

    def ApplyWebPartPersonalization(self, webPart:WebPart): # -> 
        """ ApplyWebPartPersonalization(self: PersonalizationState, webPart: WebPart) """
        ...

    def ExtractWebPartManagerPersonalization(self): # -> 
        """ ExtractWebPartManagerPersonalization(self: PersonalizationState) """
        ...

    def ExtractWebPartPersonalization(self, webPart:WebPart): # -> 
        """ ExtractWebPartPersonalization(self: PersonalizationState, webPart: WebPart) """
        ...

    def GetAuthorizationFilter(self, webPartID:str) -> str:
        """ GetAuthorizationFilter(self: PersonalizationState, webPartID: str) -> str """
        ...

    def SetDirty(self, *args): #cannot find CLR method
        """ SetDirty(self: PersonalizationState) """
        ...

    def SetWebPartDirty(self, webPart:WebPart): # -> 
        """ SetWebPartDirty(self: PersonalizationState, webPart: WebPart) """
        ...

    def SetWebPartManagerDirty(self): # -> 
        """ SetWebPartManagerDirty(self: PersonalizationState) """
        ...

    def ValidateWebPart(self, *args): #cannot find CLR method
        """ ValidateWebPart(self: PersonalizationState, webPart: WebPart) """
        ...


class PersonalizationStateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LastUpdatedDate(self) -> DateTime:
        """ Get: LastUpdatedDate(self: PersonalizationStateInfo) -> DateTime """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: PersonalizationStateInfo) -> str """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: PersonalizationStateInfo) -> int """
        ...



class PersonalizationStateInfoCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ PersonalizationStateInfoCollection() """
    def Add(self, data:PersonalizationStateInfo): # -> 
        """ Add(self: PersonalizationStateInfoCollection, data: PersonalizationStateInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: PersonalizationStateInfoCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PersonalizationStateInfoCollection) -> IEnumerator """
        ...

    def Remove(self, path:str, username:str): # -> 
        """ Remove(self: PersonalizationStateInfoCollection, path: str, username: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: PersonalizationStateInfoCollection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class PersonalizationStateQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ PersonalizationStateQuery() """
    @property
    def PathToMatch(self) -> str:
        """
        Get: PathToMatch(self: PersonalizationStateQuery) -> str
        Set: PathToMatch(self: PersonalizationStateQuery) = value
        """
        ...

    @property
    def UserInactiveSinceDate(self) -> DateTime:
        """
        Get: UserInactiveSinceDate(self: PersonalizationStateQuery) -> DateTime
        Set: UserInactiveSinceDate(self: PersonalizationStateQuery) = value
        """
        ...

    @property
    def UsernameToMatch(self) -> str:
        """
        Get: UsernameToMatch(self: PersonalizationStateQuery) -> str
        Set: UsernameToMatch(self: PersonalizationStateQuery) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class PropertyGridEditorPart(EditorPart): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ PropertyGridEditorPart() """
    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: PropertyGridEditorPart) -> str
        Set: DefaultButton(self: PropertyGridEditorPart) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: PropertyGridEditorPart) -> str
        Set: Title(self: PropertyGridEditorPart) = value
        """
        ...



class ProviderConnectionPoint(ConnectionPoint): # skipped bases: <type 'object'>
    """ ProviderConnectionPoint(callbackMethod: MethodInfo, interfaceType: Type, controlType: Type, displayName: str, id: str, allowsMultipleConnections: bool) """
    def GetObject(self, control:Control) -> object:
        """ GetObject(self: ProviderConnectionPoint, control: Control) -> object """
        ...

    def GetSecondaryInterfaces(self, control:Control) -> ConnectionInterfaceCollection:
        """ GetSecondaryInterfaces(self: ProviderConnectionPoint, control: Control) -> ConnectionInterfaceCollection """
        ...

    def __new__(cls, callbackMethod:MethodInfo, interfaceType:Type, controlType:Type, displayName:str, id:str, allowsMultipleConnections:bool) -> Self:
        """ __new__(cls: type, callbackMethod: MethodInfo, interfaceType: Type, controlType: Type, displayName: str, id: str, allowsMultipleConnections: bool) """
        ...


class ProviderConnectionPointCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    ProviderConnectionPointCollection()
    ProviderConnectionPointCollection(connectionPoints: ICollection)
    """
    @property
    def Default(self) -> ProviderConnectionPoint:
        """ Get: Default(self: ProviderConnectionPointCollection) -> ProviderConnectionPoint """
        ...


    def Contains(self, connectionPoint:ProviderConnectionPoint) -> bool:
        """ Contains(self: ProviderConnectionPointCollection, connectionPoint: ProviderConnectionPoint) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ProviderConnectionPointCollection, array: Array[ProviderConnectionPoint], index: int) """
        ...

    def IndexOf(self, connectionPoint:ProviderConnectionPoint) -> int:
        """ IndexOf(self: ProviderConnectionPointCollection, connectionPoint: ProviderConnectionPoint) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, connectionPoints:ICollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionPoints: ICollection)
        """
        ...


class ProxyWebPartConnectionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ProxyWebPartConnectionCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ProxyWebPartConnectionCollection) -> bool """
        ...


    def Add(self, value:WebPartConnection) -> int:
        """ Add(self: ProxyWebPartConnectionCollection, value: WebPartConnection) -> int """
        ...

    def Contains(self, value:WebPartConnection) -> bool:
        """ Contains(self: ProxyWebPartConnectionCollection, value: WebPartConnection) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ProxyWebPartConnectionCollection, array: Array[WebPartConnection], index: int) """
        ...

    def IndexOf(self, value:WebPartConnection) -> int:
        """ IndexOf(self: ProxyWebPartConnectionCollection, value: WebPartConnection) -> int """
        ...

    def Insert(self, index:int, value:WebPartConnection): # -> 
        """ Insert(self: ProxyWebPartConnectionCollection, index: int, value: WebPartConnection) """
        ...

    def Remove(self, value:WebPartConnection): # -> 
        """ Remove(self: ProxyWebPartConnectionCollection, value: WebPartConnection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProxyWebPartManager(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ProxyWebPartManager() """
    @property
    def StaticConnections(self) -> ProxyWebPartConnectionCollection:
        """ Get: StaticConnections(self: ProxyWebPartManager) -> ProxyWebPartConnectionCollection """
        ...



class RowCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RowCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, rowData:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RowCallback, rowData: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RowCallback, result: IAsyncResult) """
        ...

    def Invoke(self, rowData:object): # -> 
        """ Invoke(self: RowCallback, rowData: object) """
        ...


class WebPartTransformer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateConfigurationControl(self) -> Control:
        """ CreateConfigurationControl(self: WebPartTransformer) -> Control """
        ...

    def LoadConfigurationState(self, *args): #cannot find CLR method
        """ LoadConfigurationState(self: WebPartTransformer, savedState: object) """
        ...

    def SaveConfigurationState(self, *args): #cannot find CLR method
        """ SaveConfigurationState(self: WebPartTransformer) -> object """
        ...

    def Transform(self, providerData:object) -> object:
        """ Transform(self: WebPartTransformer, providerData: object) -> object """
        ...


class RowToFieldTransformer(WebPartTransformer, IWebPartField): # skipped bases: <type 'object'>
    """ RowToFieldTransformer() """
    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: RowToFieldTransformer) -> str
        Set: FieldName(self: RowToFieldTransformer) = value
        """
        ...



class RowToParametersTransformer(IWebPartParameters, WebPartTransformer): # skipped bases: <type 'object'>
    """ RowToParametersTransformer() """
    @property
    def ConsumerFieldNames(self) -> Array:
        """
        Get: ConsumerFieldNames(self: RowToParametersTransformer) -> Array[str]
        Set: ConsumerFieldNames(self: RowToParametersTransformer) = value
        """
        ...

    @property
    def ProviderFieldNames(self) -> Array:
        """
        Get: ProviderFieldNames(self: RowToParametersTransformer) -> Array[str]
        Set: ProviderFieldNames(self: RowToParametersTransformer) = value
        """
        ...



class SharedPersonalizationStateInfo(PersonalizationStateInfo): # skipped bases: <type 'object'>
    """ SharedPersonalizationStateInfo(path: str, lastUpdatedDate: DateTime, size: int, sizeOfPersonalizations: int, countOfPersonalizations: int) """
    @property
    def CountOfPersonalizations(self) -> int:
        """ Get: CountOfPersonalizations(self: SharedPersonalizationStateInfo) -> int """
        ...

    @property
    def SizeOfPersonalizations(self) -> int:
        """ Get: SizeOfPersonalizations(self: SharedPersonalizationStateInfo) -> int """
        ...


    def __new__(cls, path:str, lastUpdatedDate:DateTime, size:int, sizeOfPersonalizations:int, countOfPersonalizations:int) -> Self:
        """ __new__(cls: type, path: str, lastUpdatedDate: DateTime, size: int, sizeOfPersonalizations: int, countOfPersonalizations: int) """
        ...


class SqlPersonalizationProvider(PersonalizationProvider): # skipped bases: <type 'object'>
    """ SqlPersonalizationProvider() """
    def Initialize(self, name:str, configSettings:NameValueCollection): # -> 
        """ Initialize(self: SqlPersonalizationProvider, name: str, configSettings: NameValueCollection) """
        ...


class TableCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TableCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, tableData:ICollection, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TableCallback, tableData: ICollection, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TableCallback, result: IAsyncResult) """
        ...

    def Invoke(self, tableData:ICollection): # -> 
        """ Invoke(self: TableCallback, tableData: ICollection) """
        ...


class TitleStyle(TableItemStyle): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """ TitleStyle() """
    pass

class TransformerTypeCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    TransformerTypeCollection()
    TransformerTypeCollection(transformerTypes: ICollection)
    TransformerTypeCollection(existingTransformerTypes: TransformerTypeCollection, transformerTypes: ICollection)
    """
    def Contains(self, value:Type) -> bool:
        """ Contains(self: TransformerTypeCollection, value: Type) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TransformerTypeCollection, array: Array[Type], index: int) """
        ...

    def IndexOf(self, value:Type) -> int:
        """ IndexOf(self: TransformerTypeCollection, value: Type) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *__args:ICollection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, transformerTypes: ICollection)
        __new__(cls: type, existingTransformerTypes: TransformerTypeCollection, transformerTypes: ICollection)
        """
        ...

    Empty: TransformerTypeCollection = ...


class UnauthorizedWebPart(ProxyWebPart): # skipped bases: <type 'IWebActionable'>, <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IWebEditable'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'IWebPart'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    UnauthorizedWebPart(webPart: WebPart)
    UnauthorizedWebPart(originalID: str, originalTypeName: str, originalPath: str, genericWebPartID: str)
    """
    pass

class UserPersonalizationStateInfo(PersonalizationStateInfo): # skipped bases: <type 'object'>
    """ UserPersonalizationStateInfo(path: str, lastUpdatedDate: DateTime, size: int, username: str, lastActivityDate: DateTime) """
    @property
    def LastActivityDate(self) -> DateTime:
        """ Get: LastActivityDate(self: UserPersonalizationStateInfo) -> DateTime """
        ...

    @property
    def Username(self) -> str:
        """ Get: Username(self: UserPersonalizationStateInfo) -> str """
        ...


    def __new__(cls, path:str, lastUpdatedDate:DateTime, size:int, username:str, lastActivityDate:DateTime) -> Self:
        """ __new__(cls: type, path: str, lastUpdatedDate: DateTime, size: int, username: str, lastActivityDate: DateTime) """
        ...


class WebBrowsableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    WebBrowsableAttribute()
    WebBrowsableAttribute(browsable: bool)
    """
    @property
    def Browsable(self) -> bool:
        """ Get: Browsable(self: WebBrowsableAttribute) -> bool """
        ...


    def __new__(cls, browsable:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, browsable: bool)
        """
        ...

    Default: WebBrowsableAttribute = ...
    No: WebBrowsableAttribute = ...
    Yes: WebBrowsableAttribute = ...


class WebDescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    WebDescriptionAttribute()
    WebDescriptionAttribute(description: str)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: WebDescriptionAttribute) -> str """
        ...

    @property
    def DescriptionValue(self):
        ...


    def __new__(cls, description:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        ...

    Default: WebDescriptionAttribute = ...


class WebDisplayNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    WebDisplayNameAttribute()
    WebDisplayNameAttribute(displayName: str)
    """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: WebDisplayNameAttribute) -> str """
        ...

    @property
    def DisplayNameValue(self):
        ...


    def __new__(cls, displayName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, displayName: str)
        """
        ...

    Default: WebDisplayNameAttribute = ...


class WebPartCancelEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ WebPartCancelEventArgs(webPart: WebPart) """
    @property
    def WebPart(self) -> WebPart:
        """
        Get: WebPart(self: WebPartCancelEventArgs) -> WebPart
        Set: WebPart(self: WebPartCancelEventArgs) = value
        """
        ...



class WebPartAddingEventArgs(WebPartCancelEventArgs): # skipped bases: <type 'object'>
    """ WebPartAddingEventArgs(webPart: WebPart, zone: WebPartZoneBase, zoneIndex: int) """
    @property
    def Zone(self) -> WebPartZoneBase:
        """
        Get: Zone(self: WebPartAddingEventArgs) -> WebPartZoneBase
        Set: Zone(self: WebPartAddingEventArgs) = value
        """
        ...

    @property
    def ZoneIndex(self) -> int:
        """
        Get: ZoneIndex(self: WebPartAddingEventArgs) -> int
        Set: ZoneIndex(self: WebPartAddingEventArgs) = value
        """
        ...



class WebPartAddingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartAddingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartAddingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartAddingEventHandler, sender: object, e: WebPartAddingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartAddingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartAddingEventArgs): # -> 
        """ Invoke(self: WebPartAddingEventHandler, sender: object, e: WebPartAddingEventArgs) """
        ...


class WebPartAuthorizationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WebPartAuthorizationEventArgs(type: Type, path: str, authorizationFilter: str, isShared: bool) """
    @property
    def AuthorizationFilter(self) -> str:
        """ Get: AuthorizationFilter(self: WebPartAuthorizationEventArgs) -> str """
        ...

    @property
    def IsAuthorized(self) -> bool:
        """
        Get: IsAuthorized(self: WebPartAuthorizationEventArgs) -> bool
        Set: IsAuthorized(self: WebPartAuthorizationEventArgs) = value
        """
        ...

    @property
    def IsShared(self) -> bool:
        """ Get: IsShared(self: WebPartAuthorizationEventArgs) -> bool """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: WebPartAuthorizationEventArgs) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: WebPartAuthorizationEventArgs) -> Type """
        ...


    def __new__(cls, type:Type, path:str, authorizationFilter:str, isShared:bool) -> Self:
        """ __new__(cls: type, type: Type, path: str, authorizationFilter: str, isShared: bool) """
        ...


class WebPartAuthorizationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartAuthorizationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartAuthorizationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartAuthorizationEventHandler, sender: object, e: WebPartAuthorizationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartAuthorizationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartAuthorizationEventArgs): # -> 
        """ Invoke(self: WebPartAuthorizationEventHandler, sender: object, e: WebPartAuthorizationEventArgs) """
        ...


class WebPartCancelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartCancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartCancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartCancelEventHandler, sender: object, e: WebPartCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartCancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartCancelEventArgs): # -> 
        """ Invoke(self: WebPartCancelEventHandler, sender: object, e: WebPartCancelEventArgs) """
        ...


class WebPartChrome: # skipped bases: <type 'object'>, <type 'object'>
    """ WebPartChrome(zone: WebPartZoneBase, manager: WebPartManager) """
    @property
    def DragDropEnabled(self):
        ...

    @property
    def WebPartManager(self):
        ...

    @property
    def Zone(self):
        ...


    def CreateWebPartChromeStyle(self, *args): #cannot find CLR method
        """ CreateWebPartChromeStyle(self: WebPartChrome, webPart: WebPart, chromeType: PartChromeType) -> Style """
        ...

    def FilterWebPartVerbs(self, *args): #cannot find CLR method
        """ FilterWebPartVerbs(self: WebPartChrome, verbs: WebPartVerbCollection, webPart: WebPart) -> WebPartVerbCollection """
        ...

    def GetWebPartChromeClientID(self, *args): #cannot find CLR method
        """ GetWebPartChromeClientID(self: WebPartChrome, webPart: WebPart) -> str """
        ...

    def GetWebPartTitleClientID(self, *args): #cannot find CLR method
        """ GetWebPartTitleClientID(self: WebPartChrome, webPart: WebPart) -> str """
        ...

    def GetWebPartVerbs(self, *args): #cannot find CLR method
        """ GetWebPartVerbs(self: WebPartChrome, webPart: WebPart) -> WebPartVerbCollection """
        ...

    def PerformPreRender(self): # -> 
        """ PerformPreRender(self: WebPartChrome) """
        ...

    def RenderPartContents(self, *args): #cannot find CLR method
        """ RenderPartContents(self: WebPartChrome, writer: HtmlTextWriter, webPart: WebPart) """
        ...

    def RenderWebPart(self, writer:HtmlTextWriter, webPart:WebPart): # -> 
        """ RenderWebPart(self: WebPartChrome, writer: HtmlTextWriter, webPart: WebPart) """
        ...


class WebPartCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    WebPartCollection()
    WebPartCollection(webParts: ICollection)
    """
    def Contains(self, value:WebPart) -> bool:
        """ Contains(self: WebPartCollection, value: WebPart) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartCollection, array: Array[WebPart], index: int) """
        ...

    def IndexOf(self, value:WebPart) -> int:
        """ IndexOf(self: WebPartCollection, value: WebPart) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, webParts:ICollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, webParts: ICollection)
        """
        ...


class WebPartConnection: # skipped bases: <type 'object'>, <type 'object'>
    """ WebPartConnection() """
    @property
    def Consumer(self) -> WebPart:
        """ Get: Consumer(self: WebPartConnection) -> WebPart """
        ...

    @property
    def ConsumerConnectionPoint(self) -> ConsumerConnectionPoint:
        """ Get: ConsumerConnectionPoint(self: WebPartConnection) -> ConsumerConnectionPoint """
        ...

    @property
    def ConsumerConnectionPointID(self) -> str:
        """
        Get: ConsumerConnectionPointID(self: WebPartConnection) -> str
        Set: ConsumerConnectionPointID(self: WebPartConnection) = value
        """
        ...

    @property
    def ConsumerID(self) -> str:
        """
        Get: ConsumerID(self: WebPartConnection) -> str
        Set: ConsumerID(self: WebPartConnection) = value
        """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: WebPartConnection) -> str
        Set: ID(self: WebPartConnection) = value
        """
        ...

    @property
    def IsActive(self) -> bool:
        """ Get: IsActive(self: WebPartConnection) -> bool """
        ...

    @property
    def IsShared(self) -> bool:
        """ Get: IsShared(self: WebPartConnection) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: WebPartConnection) -> bool """
        ...

    @property
    def Provider(self) -> WebPart:
        """ Get: Provider(self: WebPartConnection) -> WebPart """
        ...

    @property
    def ProviderConnectionPoint(self) -> ProviderConnectionPoint:
        """ Get: ProviderConnectionPoint(self: WebPartConnection) -> ProviderConnectionPoint """
        ...

    @property
    def ProviderConnectionPointID(self) -> str:
        """
        Get: ProviderConnectionPointID(self: WebPartConnection) -> str
        Set: ProviderConnectionPointID(self: WebPartConnection) = value
        """
        ...

    @property
    def ProviderID(self) -> str:
        """
        Get: ProviderID(self: WebPartConnection) -> str
        Set: ProviderID(self: WebPartConnection) = value
        """
        ...

    @property
    def Transformer(self) -> WebPartTransformer:
        """ Get: Transformer(self: WebPartConnection) -> WebPartTransformer """
        ...

    @property
    def Transformers(self) -> WebPartTransformerCollection:
        """ Get: Transformers(self: WebPartConnection) -> WebPartTransformerCollection """
        ...


    def ToString(self) -> str:
        """ ToString(self: WebPartConnection) -> str """
        ...


class WebPartConnectionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: WebPartConnectionCollection) -> bool """
        ...


    def Add(self, value:WebPartConnection) -> int:
        """ Add(self: WebPartConnectionCollection, value: WebPartConnection) -> int """
        ...

    def Contains(self, value:WebPartConnection) -> bool:
        """ Contains(self: WebPartConnectionCollection, value: WebPartConnection) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartConnectionCollection, array: Array[WebPartConnection], index: int) """
        ...

    def IndexOf(self, value:WebPartConnection) -> int:
        """ IndexOf(self: WebPartConnectionCollection, value: WebPartConnection) -> int """
        ...

    def Insert(self, index:int, value:WebPartConnection): # -> 
        """ Insert(self: WebPartConnectionCollection, index: int, value: WebPartConnection) """
        ...

    def Remove(self, value:WebPartConnection): # -> 
        """ Remove(self: WebPartConnectionCollection, value: WebPartConnection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WebPartConnectionsCancelEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """
    WebPartConnectionsCancelEventArgs(provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint)
    WebPartConnectionsCancelEventArgs(provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint, connection: WebPartConnection)
    """
    @property
    def Connection(self) -> WebPartConnection:
        """ Get: Connection(self: WebPartConnectionsCancelEventArgs) -> WebPartConnection """
        ...

    @property
    def Consumer(self) -> WebPart:
        """ Get: Consumer(self: WebPartConnectionsCancelEventArgs) -> WebPart """
        ...

    @property
    def ConsumerConnectionPoint(self) -> ConsumerConnectionPoint:
        """ Get: ConsumerConnectionPoint(self: WebPartConnectionsCancelEventArgs) -> ConsumerConnectionPoint """
        ...

    @property
    def Provider(self) -> WebPart:
        """ Get: Provider(self: WebPartConnectionsCancelEventArgs) -> WebPart """
        ...

    @property
    def ProviderConnectionPoint(self) -> ProviderConnectionPoint:
        """ Get: ProviderConnectionPoint(self: WebPartConnectionsCancelEventArgs) -> ProviderConnectionPoint """
        ...



class WebPartConnectionsCancelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartConnectionsCancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartConnectionsCancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartConnectionsCancelEventHandler, sender: object, e: WebPartConnectionsCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartConnectionsCancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartConnectionsCancelEventArgs): # -> 
        """ Invoke(self: WebPartConnectionsCancelEventHandler, sender: object, e: WebPartConnectionsCancelEventArgs) """
        ...


class WebPartConnectionsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    WebPartConnectionsEventArgs(provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint)
    WebPartConnectionsEventArgs(provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint, connection: WebPartConnection)
    """
    @property
    def Connection(self) -> WebPartConnection:
        """ Get: Connection(self: WebPartConnectionsEventArgs) -> WebPartConnection """
        ...

    @property
    def Consumer(self) -> WebPart:
        """ Get: Consumer(self: WebPartConnectionsEventArgs) -> WebPart """
        ...

    @property
    def ConsumerConnectionPoint(self) -> ConsumerConnectionPoint:
        """ Get: ConsumerConnectionPoint(self: WebPartConnectionsEventArgs) -> ConsumerConnectionPoint """
        ...

    @property
    def Provider(self) -> WebPart:
        """ Get: Provider(self: WebPartConnectionsEventArgs) -> WebPart """
        ...

    @property
    def ProviderConnectionPoint(self) -> ProviderConnectionPoint:
        """ Get: ProviderConnectionPoint(self: WebPartConnectionsEventArgs) -> ProviderConnectionPoint """
        ...


    def __new__(cls, provider:WebPart, providerConnectionPoint:ProviderConnectionPoint, consumer:WebPart, consumerConnectionPoint:ConsumerConnectionPoint, connection:WebPartConnection = ...) -> Self:
        """
        __new__(cls: type, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint)
        __new__(cls: type, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint, connection: WebPartConnection)
        """
        ...


class WebPartConnectionsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartConnectionsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartConnectionsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartConnectionsEventHandler, sender: object, e: WebPartConnectionsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartConnectionsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartConnectionsEventArgs): # -> 
        """ Invoke(self: WebPartConnectionsEventHandler, sender: object, e: WebPartConnectionsEventArgs) """
        ...


class WebPartDescription: # skipped bases: <type 'object'>, <type 'object'>
    """
    WebPartDescription(id: str, title: str, description: str, imageUrl: str)
    WebPartDescription(part: WebPart)
    """
    @property
    def CatalogIconImageUrl(self) -> str:
        """ Get: CatalogIconImageUrl(self: WebPartDescription) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: WebPartDescription) -> str """
        ...

    @property
    def ID(self) -> str:
        """ Get: ID(self: WebPartDescription) -> str """
        ...

    @property
    def Title(self) -> str:
        """ Get: Title(self: WebPartDescription) -> str """
        ...



class WebPartDescriptionCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    WebPartDescriptionCollection()
    WebPartDescriptionCollection(webPartDescriptions: ICollection)
    """
    def Contains(self, value:WebPartDescription) -> bool:
        """ Contains(self: WebPartDescriptionCollection, value: WebPartDescription) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartDescriptionCollection, array: Array[WebPartDescription], index: int) """
        ...

    def IndexOf(self, value:WebPartDescription) -> int:
        """ IndexOf(self: WebPartDescriptionCollection, value: WebPartDescription) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, webPartDescriptions:ICollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, webPartDescriptions: ICollection)
        """
        ...


class WebPartDisplayMode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowPageDesign(self) -> bool:
        """ Get: AllowPageDesign(self: WebPartDisplayMode) -> bool """
        ...

    @property
    def AssociatedWithToolZone(self) -> bool:
        """ Get: AssociatedWithToolZone(self: WebPartDisplayMode) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: WebPartDisplayMode) -> str """
        ...

    @property
    def RequiresPersonalization(self) -> bool:
        """ Get: RequiresPersonalization(self: WebPartDisplayMode) -> bool """
        ...

    @property
    def ShowHiddenWebParts(self) -> bool:
        """ Get: ShowHiddenWebParts(self: WebPartDisplayMode) -> bool """
        ...


    def IsEnabled(self, webPartManager:WebPartManager) -> bool:
        """ IsEnabled(self: WebPartDisplayMode, webPartManager: WebPartManager) -> bool """
        ...


class WebPartDisplayModeCancelEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ WebPartDisplayModeCancelEventArgs(newDisplayMode: WebPartDisplayMode) """
    @property
    def NewDisplayMode(self) -> WebPartDisplayMode:
        """
        Get: NewDisplayMode(self: WebPartDisplayModeCancelEventArgs) -> WebPartDisplayMode
        Set: NewDisplayMode(self: WebPartDisplayModeCancelEventArgs) = value
        """
        ...



class WebPartDisplayModeCancelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartDisplayModeCancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartDisplayModeCancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartDisplayModeCancelEventHandler, sender: object, e: WebPartDisplayModeCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartDisplayModeCancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartDisplayModeCancelEventArgs): # -> 
        """ Invoke(self: WebPartDisplayModeCancelEventHandler, sender: object, e: WebPartDisplayModeCancelEventArgs) """
        ...


class WebPartDisplayModeCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: WebPartDisplayModeCollection) -> bool """
        ...


    def Add(self, value:WebPartDisplayMode) -> int:
        """ Add(self: WebPartDisplayModeCollection, value: WebPartDisplayMode) -> int """
        ...

    def Contains(self, value:WebPartDisplayMode) -> bool:
        """ Contains(self: WebPartDisplayModeCollection, value: WebPartDisplayMode) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartDisplayModeCollection, array: Array[WebPartDisplayMode], index: int) """
        ...

    def IndexOf(self, value:WebPartDisplayMode) -> int:
        """ IndexOf(self: WebPartDisplayModeCollection, value: WebPartDisplayMode) -> int """
        ...

    def Insert(self, index:int, value:WebPartDisplayMode): # -> 
        """ Insert(self: WebPartDisplayModeCollection, index: int, value: WebPartDisplayMode) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class WebPartDisplayModeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WebPartDisplayModeEventArgs(oldDisplayMode: WebPartDisplayMode) """
    @property
    def OldDisplayMode(self) -> WebPartDisplayMode:
        """
        Get: OldDisplayMode(self: WebPartDisplayModeEventArgs) -> WebPartDisplayMode
        Set: OldDisplayMode(self: WebPartDisplayModeEventArgs) = value
        """
        ...


    def __new__(cls, oldDisplayMode:WebPartDisplayMode) -> Self:
        """ __new__(cls: type, oldDisplayMode: WebPartDisplayMode) """
        ...


class WebPartDisplayModeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartDisplayModeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartDisplayModeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartDisplayModeEventHandler, sender: object, e: WebPartDisplayModeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartDisplayModeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartDisplayModeEventArgs): # -> 
        """ Invoke(self: WebPartDisplayModeEventHandler, sender: object, e: WebPartDisplayModeEventArgs) """
        ...


class WebPartEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WebPartEventArgs(webPart: WebPart) """
    @property
    def WebPart(self) -> WebPart:
        """ Get: WebPart(self: WebPartEventArgs) -> WebPart """
        ...


    def __new__(cls, webPart:WebPart) -> Self:
        """ __new__(cls: type, webPart: WebPart) """
        ...


class WebPartEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartEventHandler, sender: object, e: WebPartEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartEventArgs): # -> 
        """ Invoke(self: WebPartEventHandler, sender: object, e: WebPartEventArgs) """
        ...


class WebPartExportMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebPartExportMode, values: All (1), None (0), NonSensitiveData (2) """
    All: WebPartExportMode = ...
    NonSensitiveData: WebPartExportMode = ...
    value__ = ...


class WebPartHelpMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebPartHelpMode, values: Modal (0), Modeless (1), Navigate (2) """
    Modal: WebPartHelpMode = ...
    Modeless: WebPartHelpMode = ...
    Navigate: WebPartHelpMode = ...
    value__ = ...


class WebPartManager(Control, INamingContainer, IPersonalizable): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ WebPartManager() """
    @property
    def AvailableTransformers(self) -> TransformerTypeCollection:
        """ Get: AvailableTransformers(self: WebPartManager) -> TransformerTypeCollection """
        ...

    @property
    def CloseProviderWarning(self) -> str:
        """
        Get: CloseProviderWarning(self: WebPartManager) -> str
        Set: CloseProviderWarning(self: WebPartManager) = value
        """
        ...

    @property
    def Connections(self) -> WebPartConnectionCollection:
        """ Get: Connections(self: WebPartManager) -> WebPartConnectionCollection """
        ...

    @property
    def DeleteWarning(self) -> str:
        """
        Get: DeleteWarning(self: WebPartManager) -> str
        Set: DeleteWarning(self: WebPartManager) = value
        """
        ...

    @property
    def DisplayMode(self) -> WebPartDisplayMode:
        """
        Get: DisplayMode(self: WebPartManager) -> WebPartDisplayMode
        Set: DisplayMode(self: WebPartManager) = value
        """
        ...

    @property
    def DisplayModes(self) -> WebPartDisplayModeCollection:
        """ Get: DisplayModes(self: WebPartManager) -> WebPartDisplayModeCollection """
        ...

    @property
    def DynamicConnections(self):
        ...

    @property
    def EnableClientScript(self) -> bool:
        """
        Get: EnableClientScript(self: WebPartManager) -> bool
        Set: EnableClientScript(self: WebPartManager) = value
        """
        ...

    @property
    def ExportSensitiveDataWarning(self) -> str:
        """
        Get: ExportSensitiveDataWarning(self: WebPartManager) -> str
        Set: ExportSensitiveDataWarning(self: WebPartManager) = value
        """
        ...

    @property
    def Internals(self):
        ...

    @property
    def IsCustomPersonalizationStateDirty(self):
        ...

    @property
    def MediumPermissionSet(self):
        ...

    @property
    def MinimalPermissionSet(self):
        ...

    @property
    def Personalization(self) -> WebPartPersonalization:
        """ Get: Personalization(self: WebPartManager) -> WebPartPersonalization """
        ...

    @property
    def SelectedWebPart(self) -> WebPart:
        """ Get: SelectedWebPart(self: WebPartManager) -> WebPart """
        ...

    @property
    def StaticConnections(self) -> WebPartConnectionCollection:
        """ Get: StaticConnections(self: WebPartManager) -> WebPartConnectionCollection """
        ...

    @property
    def SupportedDisplayModes(self) -> WebPartDisplayModeCollection:
        """ Get: SupportedDisplayModes(self: WebPartManager) -> WebPartDisplayModeCollection """
        ...

    @property
    def WebParts(self) -> WebPartCollection:
        """ Get: WebParts(self: WebPartManager) -> WebPartCollection """
        ...

    @property
    def Zones(self) -> WebPartZoneCollection:
        """ Get: Zones(self: WebPartManager) -> WebPartZoneCollection """
        ...


    def ActivateConnections(self, *args): #cannot find CLR method
        """ ActivateConnections(self: WebPartManager) """
        ...

    def AddWebPart(self, webPart:WebPart, zone:WebPartZoneBase, zoneIndex:int) -> WebPart:
        """ AddWebPart(self: WebPartManager, webPart: WebPart, zone: WebPartZoneBase, zoneIndex: int) -> WebPart """
        ...

    def BeginWebPartConnecting(self, webPart:WebPart): # -> 
        """ BeginWebPartConnecting(self: WebPartManager, webPart: WebPart) """
        ...

    def BeginWebPartEditing(self, webPart:WebPart): # -> 
        """ BeginWebPartEditing(self: WebPartManager, webPart: WebPart) """
        ...

    def CanConnectWebParts(self, provider:WebPart, providerConnectionPoint:ProviderConnectionPoint, consumer:WebPart, consumerConnectionPoint:ConsumerConnectionPoint, transformer:WebPartTransformer = ...) -> bool:
        """
        CanConnectWebParts(self: WebPartManager, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint) -> bool
        CanConnectWebParts(self: WebPartManager, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint, transformer: WebPartTransformer) -> bool
        """
        ...

    def CheckRenderClientScript(self, *args): #cannot find CLR method
        """ CheckRenderClientScript(self: WebPartManager) -> bool """
        ...

    def CloseWebPart(self, webPart:WebPart): # -> 
        """ CloseWebPart(self: WebPartManager, webPart: WebPart) """
        ...

    def ConnectWebParts(self, provider:WebPart, providerConnectionPoint:ProviderConnectionPoint, consumer:WebPart, consumerConnectionPoint:ConsumerConnectionPoint, transformer:WebPartTransformer = ...) -> WebPartConnection:
        """
        ConnectWebParts(self: WebPartManager, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint) -> WebPartConnection
        ConnectWebParts(self: WebPartManager, provider: WebPart, providerConnectionPoint: ProviderConnectionPoint, consumer: WebPart, consumerConnectionPoint: ConsumerConnectionPoint, transformer: WebPartTransformer) -> WebPartConnection
        """
        ...

    def CopyWebPart(self, *args): #cannot find CLR method
        """ CopyWebPart(self: WebPartManager, webPart: WebPart) -> WebPart """
        ...

    def CreateAvailableTransformers(self, *args): #cannot find CLR method
        """ CreateAvailableTransformers(self: WebPartManager) -> TransformerTypeCollection """
        ...

    def CreateDisplayModes(self, *args): #cannot find CLR method
        """ CreateDisplayModes(self: WebPartManager) -> WebPartDisplayModeCollection """
        ...

    def CreateDynamicConnectionID(self, *args): #cannot find CLR method
        """ CreateDynamicConnectionID(self: WebPartManager) -> str """
        ...

    def CreateDynamicWebPartID(self, *args): #cannot find CLR method
        """ CreateDynamicWebPartID(self: WebPartManager, webPartType: Type) -> str """
        ...

    def CreateErrorWebPart(self, *args): #cannot find CLR method
        """ CreateErrorWebPart(self: WebPartManager, originalID: str, originalTypeName: str, originalPath: str, genericWebPartID: str, errorMessage: str) -> ErrorWebPart """
        ...

    def CreatePersonalization(self, *args): #cannot find CLR method
        """ CreatePersonalization(self: WebPartManager) -> WebPartPersonalization """
        ...

    def CreateWebPart(self, control:Control) -> GenericWebPart:
        """ CreateWebPart(self: WebPartManager, control: Control) -> GenericWebPart """
        ...

    def DeleteWebPart(self, webPart:WebPart): # -> 
        """ DeleteWebPart(self: WebPartManager, webPart: WebPart) """
        ...

    def DisconnectWebPart(self, *args): #cannot find CLR method
        """ DisconnectWebPart(self: WebPartManager, webPart: WebPart) """
        ...

    def DisconnectWebParts(self, connection:WebPartConnection): # -> 
        """ DisconnectWebParts(self: WebPartManager, connection: WebPartConnection) """
        ...

    def EndWebPartConnecting(self): # -> 
        """ EndWebPartConnecting(self: WebPartManager) """
        ...

    def EndWebPartEditing(self): # -> 
        """ EndWebPartEditing(self: WebPartManager) """
        ...

    def ExportWebPart(self, webPart:WebPart, writer:XmlWriter): # -> 
        """ ExportWebPart(self: WebPartManager, webPart: WebPart, writer: XmlWriter) """
        ...

    def GetConsumerConnectionPoints(self, webPart:WebPart) -> ConsumerConnectionPointCollection:
        """ GetConsumerConnectionPoints(self: WebPartManager, webPart: WebPart) -> ConsumerConnectionPointCollection """
        ...

    @staticmethod
    def GetCurrentWebPartManager(page:Page) -> WebPartManager:
        """ GetCurrentWebPartManager(page: Page) -> WebPartManager """
        ...

    def GetDisplayTitle(self, *args): #cannot find CLR method
        """ GetDisplayTitle(self: WebPartManager, webPart: WebPart) -> str """
        ...

    def GetExportUrl(self, webPart:WebPart) -> str:
        """ GetExportUrl(self: WebPartManager, webPart: WebPart) -> str """
        ...

    def GetGenericWebPart(self, control:Control) -> GenericWebPart:
        """ GetGenericWebPart(self: WebPartManager, control: Control) -> GenericWebPart """
        ...

    def GetProviderConnectionPoints(self, webPart:WebPart) -> ProviderConnectionPointCollection:
        """ GetProviderConnectionPoints(self: WebPartManager, webPart: WebPart) -> ProviderConnectionPointCollection """
        ...

    def ImportWebPart(self, reader, errorMessage) -> Tuple_[WebPart, str]:
        """ ImportWebPart(self: WebPartManager, reader: XmlReader) -> (WebPart, str) """
        ...

    def IsAuthorized(self, *__args:WebPart) -> bool:
        """
        IsAuthorized(self: WebPartManager, webPart: WebPart) -> bool
        IsAuthorized(self: WebPartManager, type: Type, path: str, authorizationFilter: str, isShared: bool) -> bool
        """
        ...

    def LoadCustomPersonalizationState(self, *args): #cannot find CLR method
        """ LoadCustomPersonalizationState(self: WebPartManager, state: PersonalizationDictionary) """
        ...

    def MoveWebPart(self, webPart:WebPart, zone:WebPartZoneBase, zoneIndex:int): # -> 
        """ MoveWebPart(self: WebPartManager, webPart: WebPart, zone: WebPartZoneBase, zoneIndex: int) """
        ...

    def OnAuthorizeWebPart(self, *args): #cannot find CLR method
        """ OnAuthorizeWebPart(self: WebPartManager, e: WebPartAuthorizationEventArgs) """
        ...

    def OnConnectionsActivated(self, *args): #cannot find CLR method
        """ OnConnectionsActivated(self: WebPartManager, e: EventArgs) """
        ...

    def OnConnectionsActivating(self, *args): #cannot find CLR method
        """ OnConnectionsActivating(self: WebPartManager, e: EventArgs) """
        ...

    def OnDisplayModeChanged(self, *args): #cannot find CLR method
        """ OnDisplayModeChanged(self: WebPartManager, e: WebPartDisplayModeEventArgs) """
        ...

    def OnDisplayModeChanging(self, *args): #cannot find CLR method
        """ OnDisplayModeChanging(self: WebPartManager, e: WebPartDisplayModeCancelEventArgs) """
        ...

    def OnSelectedWebPartChanged(self, *args): #cannot find CLR method
        """ OnSelectedWebPartChanged(self: WebPartManager, e: WebPartEventArgs) """
        ...

    def OnSelectedWebPartChanging(self, *args): #cannot find CLR method
        """ OnSelectedWebPartChanging(self: WebPartManager, e: WebPartCancelEventArgs) """
        ...

    def OnWebPartAdded(self, *args): #cannot find CLR method
        """ OnWebPartAdded(self: WebPartManager, e: WebPartEventArgs) """
        ...

    def OnWebPartAdding(self, *args): #cannot find CLR method
        """ OnWebPartAdding(self: WebPartManager, e: WebPartAddingEventArgs) """
        ...

    def OnWebPartClosed(self, *args): #cannot find CLR method
        """ OnWebPartClosed(self: WebPartManager, e: WebPartEventArgs) """
        ...

    def OnWebPartClosing(self, *args): #cannot find CLR method
        """ OnWebPartClosing(self: WebPartManager, e: WebPartCancelEventArgs) """
        ...

    def OnWebPartDeleted(self, *args): #cannot find CLR method
        """ OnWebPartDeleted(self: WebPartManager, e: WebPartEventArgs) """
        ...

    def OnWebPartDeleting(self, *args): #cannot find CLR method
        """ OnWebPartDeleting(self: WebPartManager, e: WebPartCancelEventArgs) """
        ...

    def OnWebPartMoved(self, *args): #cannot find CLR method
        """ OnWebPartMoved(self: WebPartManager, e: WebPartEventArgs) """
        ...

    def OnWebPartMoving(self, *args): #cannot find CLR method
        """ OnWebPartMoving(self: WebPartManager, e: WebPartMovingEventArgs) """
        ...

    def OnWebPartsConnected(self, *args): #cannot find CLR method
        """ OnWebPartsConnected(self: WebPartManager, e: WebPartConnectionsEventArgs) """
        ...

    def OnWebPartsConnecting(self, *args): #cannot find CLR method
        """ OnWebPartsConnecting(self: WebPartManager, e: WebPartConnectionsCancelEventArgs) """
        ...

    def OnWebPartsDisconnected(self, *args): #cannot find CLR method
        """ OnWebPartsDisconnected(self: WebPartManager, e: WebPartConnectionsEventArgs) """
        ...

    def OnWebPartsDisconnecting(self, *args): #cannot find CLR method
        """ OnWebPartsDisconnecting(self: WebPartManager, e: WebPartConnectionsCancelEventArgs) """
        ...

    def RegisterClientScript(self, *args): #cannot find CLR method
        """ RegisterClientScript(self: WebPartManager) """
        ...

    def SaveCustomPersonalizationState(self, *args): #cannot find CLR method
        """ SaveCustomPersonalizationState(self: WebPartManager, state: PersonalizationDictionary) """
        ...

    def SetPersonalizationDirty(self, *args): #cannot find CLR method
        """ SetPersonalizationDirty(self: WebPartManager) """
        ...

    def SetSelectedWebPart(self, *args): #cannot find CLR method
        """ SetSelectedWebPart(self: WebPartManager, webPart: WebPart) """
        ...

    AuthorizeWebPart = ...
    BrowseDisplayMode = ...
    CatalogDisplayMode = ...
    ConnectDisplayMode = ...
    ConnectionsActivated = ...
    ConnectionsActivating = ...
    DesignDisplayMode = ...
    DisplayModeChanged = ...
    DisplayModeChanging = ...
    EditDisplayMode = ...
    SelectedWebPartChanged = ...
    SelectedWebPartChanging = ...
    WebPartAdded = ...
    WebPartAdding = ...
    WebPartClosed = ...
    WebPartClosing = ...
    WebPartDeleted = ...
    WebPartDeleting = ...
    WebPartMoved = ...
    WebPartMoving = ...
    WebPartsConnected = ...
    WebPartsConnecting = ...
    WebPartsDisconnected = ...
    WebPartsDisconnecting = ...


class WebPartManagerInternals: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddWebPart(self, webPart:WebPart): # -> 
        """ AddWebPart(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def CallOnClosing(self, webPart:WebPart): # -> 
        """ CallOnClosing(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def CallOnConnectModeChanged(self, webPart:WebPart): # -> 
        """ CallOnConnectModeChanged(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def CallOnDeleting(self, webPart:WebPart): # -> 
        """ CallOnDeleting(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def CallOnEditModeChanged(self, webPart:WebPart): # -> 
        """ CallOnEditModeChanged(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def ConnectionDeleted(self, connection:WebPartConnection) -> bool:
        """ ConnectionDeleted(self: WebPartManagerInternals, connection: WebPartConnection) -> bool """
        ...

    def CreateObjectFromType(self, type:Type) -> object:
        """ CreateObjectFromType(self: WebPartManagerInternals, type: Type) -> object """
        ...

    def DeleteConnection(self, connection:WebPartConnection): # -> 
        """ DeleteConnection(self: WebPartManagerInternals, connection: WebPartConnection) """
        ...

    def GetZoneID(self, webPart:WebPart) -> str:
        """ GetZoneID(self: WebPartManagerInternals, webPart: WebPart) -> str """
        ...

    def LoadConfigurationState(self, transformer:WebPartTransformer, savedState:object): # -> 
        """ LoadConfigurationState(self: WebPartManagerInternals, transformer: WebPartTransformer, savedState: object) """
        ...

    def RemoveWebPart(self, webPart:WebPart): # -> 
        """ RemoveWebPart(self: WebPartManagerInternals, webPart: WebPart) """
        ...

    def SaveConfigurationState(self, transformer:WebPartTransformer) -> object:
        """ SaveConfigurationState(self: WebPartManagerInternals, transformer: WebPartTransformer) -> object """
        ...

    def SetConnectErrorMessage(self, webPart:WebPart, connectErrorMessage:str): # -> 
        """ SetConnectErrorMessage(self: WebPartManagerInternals, webPart: WebPart, connectErrorMessage: str) """
        ...

    def SetHasSharedData(self, webPart:WebPart, hasSharedData:bool): # -> 
        """ SetHasSharedData(self: WebPartManagerInternals, webPart: WebPart, hasSharedData: bool) """
        ...

    def SetHasUserData(self, webPart:WebPart, hasUserData:bool): # -> 
        """ SetHasUserData(self: WebPartManagerInternals, webPart: WebPart, hasUserData: bool) """
        ...

    def SetIsClosed(self, webPart:WebPart, isClosed:bool): # -> 
        """ SetIsClosed(self: WebPartManagerInternals, webPart: WebPart, isClosed: bool) """
        ...

    def SetIsShared(self, *__args): # -> 
        """ SetIsShared(self: WebPartManagerInternals, connection: WebPartConnection, isShared: bool)SetIsShared(self: WebPartManagerInternals, webPart: WebPart, isShared: bool) """
        ...

    def SetIsStandalone(self, webPart:WebPart, isStandalone:bool): # -> 
        """ SetIsStandalone(self: WebPartManagerInternals, webPart: WebPart, isStandalone: bool) """
        ...

    def SetIsStatic(self, *__args): # -> 
        """ SetIsStatic(self: WebPartManagerInternals, connection: WebPartConnection, isStatic: bool)SetIsStatic(self: WebPartManagerInternals, webPart: WebPart, isStatic: bool) """
        ...

    def SetTransformer(self, connection:WebPartConnection, transformer:WebPartTransformer): # -> 
        """ SetTransformer(self: WebPartManagerInternals, connection: WebPartConnection, transformer: WebPartTransformer) """
        ...

    def SetZoneID(self, webPart:WebPart, zoneID:str): # -> 
        """ SetZoneID(self: WebPartManagerInternals, webPart: WebPart, zoneID: str) """
        ...

    def SetZoneIndex(self, webPart:WebPart, zoneIndex:int): # -> 
        """ SetZoneIndex(self: WebPartManagerInternals, webPart: WebPart, zoneIndex: int) """
        ...


class WebPartMenuStyle(TableStyle, ICustomTypeDescriptor): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    WebPartMenuStyle()
    WebPartMenuStyle(bag: StateBag)
    """
    @property
    def ShadowColor(self) -> Color:
        """
        Get: ShadowColor(self: WebPartMenuStyle) -> Color
        Set: ShadowColor(self: WebPartMenuStyle) = value
        """
        ...



class WebPartMovingEventArgs(WebPartCancelEventArgs): # skipped bases: <type 'object'>
    """ WebPartMovingEventArgs(webPart: WebPart, zone: WebPartZoneBase, zoneIndex: int) """
    @property
    def Zone(self) -> WebPartZoneBase:
        """
        Get: Zone(self: WebPartMovingEventArgs) -> WebPartZoneBase
        Set: Zone(self: WebPartMovingEventArgs) = value
        """
        ...

    @property
    def ZoneIndex(self) -> int:
        """
        Get: ZoneIndex(self: WebPartMovingEventArgs) -> int
        Set: ZoneIndex(self: WebPartMovingEventArgs) = value
        """
        ...



class WebPartMovingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartMovingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartMovingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartMovingEventHandler, sender: object, e: WebPartMovingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartMovingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartMovingEventArgs): # -> 
        """ Invoke(self: WebPartMovingEventHandler, sender: object, e: WebPartMovingEventArgs) """
        ...


class WebPartPersonalization: # skipped bases: <type 'object'>, <type 'object'>
    """ WebPartPersonalization(owner: WebPartManager) """
    @property
    def CanEnterSharedScope(self) -> bool:
        """ Get: CanEnterSharedScope(self: WebPartPersonalization) -> bool """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WebPartPersonalization) -> bool
        Set: Enabled(self: WebPartPersonalization) = value
        """
        ...

    @property
    def HasPersonalizationState(self) -> bool:
        """ Get: HasPersonalizationState(self: WebPartPersonalization) -> bool """
        ...

    @property
    def InitialScope(self) -> PersonalizationScope:
        """
        Get: InitialScope(self: WebPartPersonalization) -> PersonalizationScope
        Set: InitialScope(self: WebPartPersonalization) = value
        """
        ...

    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled(self: WebPartPersonalization) -> bool """
        ...

    @property
    def IsInitialized(self):
        ...

    @property
    def IsModifiable(self) -> bool:
        """ Get: IsModifiable(self: WebPartPersonalization) -> bool """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: WebPartPersonalization) -> str
        Set: ProviderName(self: WebPartPersonalization) = value
        """
        ...

    @property
    def Scope(self) -> PersonalizationScope:
        """ Get: Scope(self: WebPartPersonalization) -> PersonalizationScope """
        ...

    @property
    def ShouldResetPersonalizationState(self):
        ...

    @property
    def UserCapabilities(self):
        ...

    @property
    def WebPartManager(self):
        ...


    def ApplyPersonalizationState(self, *args): #cannot find CLR method
        """ ApplyPersonalizationState(self: WebPartPersonalization)ApplyPersonalizationState(self: WebPartPersonalization, webPart: WebPart) """
        ...

    def ChangeScope(self, *args): #cannot find CLR method
        """ ChangeScope(self: WebPartPersonalization, scope: PersonalizationScope) """
        ...

    def CopyPersonalizationState(self, *args): #cannot find CLR method
        """ CopyPersonalizationState(self: WebPartPersonalization, webPartA: WebPart, webPartB: WebPart) """
        ...

    def EnsureEnabled(self, ensureModifiable:bool): # -> 
        """ EnsureEnabled(self: WebPartPersonalization, ensureModifiable: bool) """
        ...

    def ExtractPersonalizationState(self, *args): #cannot find CLR method
        """ ExtractPersonalizationState(self: WebPartPersonalization)ExtractPersonalizationState(self: WebPartPersonalization, webPart: WebPart) """
        ...

    def GetAuthorizationFilter(self, *args): #cannot find CLR method
        """ GetAuthorizationFilter(self: WebPartPersonalization, webPartID: str) -> str """
        ...

    def Load(self, *args): #cannot find CLR method
        """ Load(self: WebPartPersonalization) -> PersonalizationScope """
        ...

    def ResetPersonalizationState(self): # -> 
        """ ResetPersonalizationState(self: WebPartPersonalization) """
        ...

    def Save(self, *args): #cannot find CLR method
        """ Save(self: WebPartPersonalization) """
        ...

    def SetDirty(self, *args): #cannot find CLR method
        """ SetDirty(self: WebPartPersonalization)SetDirty(self: WebPartPersonalization, webPart: WebPart) """
        ...

    def ToggleScope(self): # -> 
        """ ToggleScope(self: WebPartPersonalization) """
        ...

    EnterSharedScopeUserCapability: WebPartUserCapability = ...
    ModifyStateUserCapability: WebPartUserCapability = ...


class WebPartTracker(IDisposable): # skipped bases: <type 'object'>
    """ WebPartTracker(webPart: WebPart, providerConnectionPoint: ProviderConnectionPoint) """
    @property
    def IsCircularConnection(self) -> bool:
        """ Get: IsCircularConnection(self: WebPartTracker) -> bool """
        ...



class WebPartTransformerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebPartTransformerAttribute(consumerType: Type, providerType: Type) """
    @property
    def ConsumerType(self) -> Type:
        """ Get: ConsumerType(self: WebPartTransformerAttribute) -> Type """
        ...

    @property
    def ProviderType(self) -> Type:
        """ Get: ProviderType(self: WebPartTransformerAttribute) -> Type """
        ...


    @staticmethod
    def GetConsumerType(transformerType:Type) -> Type:
        """ GetConsumerType(transformerType: Type) -> Type """
        ...

    @staticmethod
    def GetProviderType(transformerType:Type) -> Type:
        """ GetProviderType(transformerType: Type) -> Type """
        ...

    def __new__(cls, consumerType:Type, providerType:Type) -> Self:
        """ __new__(cls: type, consumerType: Type, providerType: Type) """
        ...


class WebPartTransformerCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ WebPartTransformerCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: WebPartTransformerCollection) -> bool """
        ...


    def Add(self, transformer:WebPartTransformer) -> int:
        """ Add(self: WebPartTransformerCollection, transformer: WebPartTransformer) -> int """
        ...

    def Contains(self, transformer:WebPartTransformer) -> bool:
        """ Contains(self: WebPartTransformerCollection, transformer: WebPartTransformer) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartTransformerCollection, array: Array[WebPartTransformer], index: int) """
        ...

    def IndexOf(self, transformer:WebPartTransformer) -> int:
        """ IndexOf(self: WebPartTransformerCollection, transformer: WebPartTransformer) -> int """
        ...

    def Insert(self, index:int, transformer:WebPartTransformer): # -> 
        """ Insert(self: WebPartTransformerCollection, index: int, transformer: WebPartTransformer) """
        ...

    def Remove(self, transformer:WebPartTransformer): # -> 
        """ Remove(self: WebPartTransformerCollection, transformer: WebPartTransformer) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WebPartUserCapability: # skipped bases: <type 'object'>, <type 'object'>
    """ WebPartUserCapability(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: WebPartUserCapability) -> str """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: WebPartUserCapability, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: WebPartUserCapability) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WebPartVerb(IStateManager): # skipped bases: <type 'object'>
    """
    WebPartVerb(id: str, serverClickHandler: WebPartEventHandler)
    WebPartVerb(id: str, clientClickHandler: str)
    WebPartVerb(id: str, serverClickHandler: WebPartEventHandler, clientClickHandler: str)
    """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: WebPartVerb) -> bool
        Set: Checked(self: WebPartVerb) = value
        """
        ...

    @property
    def ClientClickHandler(self) -> str:
        """ Get: ClientClickHandler(self: WebPartVerb) -> str """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: WebPartVerb) -> str
        Set: Description(self: WebPartVerb) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WebPartVerb) -> bool
        Set: Enabled(self: WebPartVerb) = value
        """
        ...

    @property
    def ID(self) -> str:
        """ Get: ID(self: WebPartVerb) -> str """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: WebPartVerb) -> str
        Set: ImageUrl(self: WebPartVerb) = value
        """
        ...

    @property
    def ServerClickHandler(self) -> WebPartEventHandler:
        """ Get: ServerClickHandler(self: WebPartVerb) -> WebPartEventHandler """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: WebPartVerb) -> str
        Set: Text(self: WebPartVerb) = value
        """
        ...

    @property
    def ViewState(self):
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: WebPartVerb) -> bool
        Set: Visible(self: WebPartVerb) = value
        """
        ...



class WebPartVerbCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    WebPartVerbCollection()
    WebPartVerbCollection(verbs: ICollection)
    WebPartVerbCollection(existingVerbs: WebPartVerbCollection, verbs: ICollection)
    """
    def Contains(self, value:WebPartVerb) -> bool:
        """ Contains(self: WebPartVerbCollection, value: WebPartVerb) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartVerbCollection, array: Array[WebPartVerb], index: int) """
        ...

    def IndexOf(self, value:WebPartVerb) -> int:
        """ IndexOf(self: WebPartVerbCollection, value: WebPartVerb) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *__args:ICollection) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, verbs: ICollection)
        __new__(cls: type, existingVerbs: WebPartVerbCollection, verbs: ICollection)
        """
        ...

    Empty: WebPartVerbCollection = ...


class WebPartVerbRenderMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebPartVerbRenderMode, values: Menu (0), TitleBar (1) """
    Menu: WebPartVerbRenderMode = ...
    TitleBar: WebPartVerbRenderMode = ...
    value__ = ...


class WebPartVerbsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    WebPartVerbsEventArgs()
    WebPartVerbsEventArgs(verbs: WebPartVerbCollection)
    """
    @property
    def Verbs(self) -> WebPartVerbCollection:
        """
        Get: Verbs(self: WebPartVerbsEventArgs) -> WebPartVerbCollection
        Set: Verbs(self: WebPartVerbsEventArgs) = value
        """
        ...


    def __new__(cls, verbs:WebPartVerbCollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, verbs: WebPartVerbCollection)
        """
        ...


class WebPartVerbsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WebPartVerbsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WebPartVerbsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WebPartVerbsEventHandler, sender: object, e: WebPartVerbsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WebPartVerbsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WebPartVerbsEventArgs): # -> 
        """ Invoke(self: WebPartVerbsEventHandler, sender: object, e: WebPartVerbsEventArgs) """
        ...


class WebPartZoneBase(IPostBackEventHandler, IWebPartMenuUser, WebZone): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AllowLayoutChange(self) -> bool:
        """
        Get: AllowLayoutChange(self: WebPartZoneBase) -> bool
        Set: AllowLayoutChange(self: WebPartZoneBase) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: WebPartZoneBase) -> Color
        Set: BorderColor(self: WebPartZoneBase) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: WebPartZoneBase) -> BorderStyle
        Set: BorderStyle(self: WebPartZoneBase) = value
        """
        ...

    @property
    def BorderWidth(self) -> Unit:
        """
        Get: BorderWidth(self: WebPartZoneBase) -> Unit
        Set: BorderWidth(self: WebPartZoneBase) = value
        """
        ...

    @property
    def CloseVerb(self) -> WebPartVerb:
        """ Get: CloseVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def ConnectVerb(self) -> WebPartVerb:
        """ Get: ConnectVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def DeleteVerb(self) -> WebPartVerb:
        """ Get: DeleteVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def DisplayTitle(self) -> str:
        """ Get: DisplayTitle(self: WebPartZoneBase) -> str """
        ...

    @property
    def DragDropEnabled(self):
        ...

    @property
    def DragHighlightColor(self) -> Color:
        """
        Get: DragHighlightColor(self: WebPartZoneBase) -> Color
        Set: DragHighlightColor(self: WebPartZoneBase) = value
        """
        ...

    @property
    def EditVerb(self) -> WebPartVerb:
        """ Get: EditVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def ExportVerb(self) -> WebPartVerb:
        """ Get: ExportVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def HelpVerb(self) -> WebPartVerb:
        """ Get: HelpVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def LayoutOrientation(self) -> Orientation:
        """
        Get: LayoutOrientation(self: WebPartZoneBase) -> Orientation
        Set: LayoutOrientation(self: WebPartZoneBase) = value
        """
        ...

    @property
    def MenuCheckImageStyle(self) -> Style:
        """ Get: MenuCheckImageStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def MenuCheckImageUrl(self) -> str:
        """
        Get: MenuCheckImageUrl(self: WebPartZoneBase) -> str
        Set: MenuCheckImageUrl(self: WebPartZoneBase) = value
        """
        ...

    @property
    def MenuLabelHoverStyle(self) -> Style:
        """ Get: MenuLabelHoverStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def MenuLabelStyle(self) -> Style:
        """ Get: MenuLabelStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def MenuLabelText(self) -> str:
        """
        Get: MenuLabelText(self: WebPartZoneBase) -> str
        Set: MenuLabelText(self: WebPartZoneBase) = value
        """
        ...

    @property
    def MenuPopupImageUrl(self) -> str:
        """
        Get: MenuPopupImageUrl(self: WebPartZoneBase) -> str
        Set: MenuPopupImageUrl(self: WebPartZoneBase) = value
        """
        ...

    @property
    def MenuPopupStyle(self) -> WebPartMenuStyle:
        """ Get: MenuPopupStyle(self: WebPartZoneBase) -> WebPartMenuStyle """
        ...

    @property
    def MenuVerbHoverStyle(self) -> Style:
        """ Get: MenuVerbHoverStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def MenuVerbStyle(self) -> Style:
        """ Get: MenuVerbStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def MinimizeVerb(self) -> WebPartVerb:
        """ Get: MinimizeVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def RestoreVerb(self) -> WebPartVerb:
        """ Get: RestoreVerb(self: WebPartZoneBase) -> WebPartVerb """
        ...

    @property
    def SelectedPartChromeStyle(self) -> Style:
        """ Get: SelectedPartChromeStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def ShowTitleIcons(self) -> bool:
        """
        Get: ShowTitleIcons(self: WebPartZoneBase) -> bool
        Set: ShowTitleIcons(self: WebPartZoneBase) = value
        """
        ...

    @property
    def TitleBarVerbButtonType(self) -> ButtonType:
        """
        Get: TitleBarVerbButtonType(self: WebPartZoneBase) -> ButtonType
        Set: TitleBarVerbButtonType(self: WebPartZoneBase) = value
        """
        ...

    @property
    def TitleBarVerbStyle(self) -> Style:
        """ Get: TitleBarVerbStyle(self: WebPartZoneBase) -> Style """
        ...

    @property
    def WebPartChrome(self) -> WebPartChrome:
        """ Get: WebPartChrome(self: WebPartZoneBase) -> WebPartChrome """
        ...

    @property
    def WebParts(self) -> WebPartCollection:
        """ Get: WebParts(self: WebPartZoneBase) -> WebPartCollection """
        ...

    @property
    def WebPartVerbRenderMode(self) -> WebPartVerbRenderMode:
        """
        Get: WebPartVerbRenderMode(self: WebPartZoneBase) -> WebPartVerbRenderMode
        Set: WebPartVerbRenderMode(self: WebPartZoneBase) = value
        """
        ...


    def CloseWebPart(self, *args): #cannot find CLR method
        """ CloseWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    def ConnectWebPart(self, *args): #cannot find CLR method
        """ ConnectWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    def CreateWebPartChrome(self, *args): #cannot find CLR method
        """ CreateWebPartChrome(self: WebPartZoneBase) -> WebPartChrome """
        ...

    def DeleteWebPart(self, *args): #cannot find CLR method
        """ DeleteWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    def EditWebPart(self, *args): #cannot find CLR method
        """ EditWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    def GetInitialWebParts(self, *args): #cannot find CLR method
        """ GetInitialWebParts(self: WebPartZoneBase) -> WebPartCollection """
        ...

    def MinimizeWebPart(self, *args): #cannot find CLR method
        """ MinimizeWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    def OnCreateVerbs(self, *args): #cannot find CLR method
        """ OnCreateVerbs(self: WebPartZoneBase, e: WebPartVerbsEventArgs) """
        ...

    def RenderDropCue(self, *args): #cannot find CLR method
        """ RenderDropCue(self: WebPartZoneBase, writer: HtmlTextWriter) """
        ...

    def RestoreWebPart(self, *args): #cannot find CLR method
        """ RestoreWebPart(self: WebPartZoneBase, webPart: WebPart) """
        ...

    CreateVerbs = ...


class WebPartZone(WebPartZoneBase): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IWebPartMenuUser'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'ICompositeControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IPostBackEventHandler'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ WebPartZone() """
    @property
    def ZoneTemplate(self) -> ITemplate:
        """
        Get: ZoneTemplate(self: WebPartZone) -> ITemplate
        Set: ZoneTemplate(self: WebPartZone) = value
        """
        ...



class WebPartZoneCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    WebPartZoneCollection()
    WebPartZoneCollection(webPartZones: ICollection)
    """
    def Contains(self, value:WebPartZoneBase) -> bool:
        """ Contains(self: WebPartZoneCollection, value: WebPartZoneBase) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebPartZoneCollection, array: Array[WebPartZoneBase], index: int) """
        ...

    def IndexOf(self, value:WebPartZoneBase) -> int:
        """ IndexOf(self: WebPartZoneCollection, value: WebPartZoneBase) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, webPartZones:ICollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, webPartZones: ICollection)
        """
        ...


