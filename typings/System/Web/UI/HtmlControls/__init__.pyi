# encoding: utf-8
# module System.Web.UI.HtmlControls calls itself HtmlControls
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import ICollection, IEnumerator

from System.ComponentModel import AttributeCollection

from System.Web import HttpPostedFile

from System.Web.UI import (Control, ControlBuilder, CssStyleCollection, 
    IAttributeAccessor, IPostBackDataHandler, IPostBackEventHandler, 
    IStyleSheet)

from System.Web.UI.WebControls import ListItemCollection

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class HtmlControl(IAttributeAccessor, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: HtmlControl) -> AttributeCollection """
        ...

    @property
    def Disabled(self) -> bool:
        """
        Get: Disabled(self: HtmlControl) -> bool
        Set: Disabled(self: HtmlControl) = value
        """
        ...

    @property
    def Style(self) -> CssStyleCollection:
        """ Get: Style(self: HtmlControl) -> CssStyleCollection """
        ...

    @property
    def TagName(self) -> str:
        """ Get: TagName(self: HtmlControl) -> str """
        ...


    def RenderAttributes(self, *args): #cannot find CLR method
        """ RenderAttributes(self: HtmlControl, writer: HtmlTextWriter) """
        ...

    def RenderBeginTag(self, *args): #cannot find CLR method
        """ RenderBeginTag(self: HtmlControl, writer: HtmlTextWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, tag: str)
        """
        ...


class HtmlContainerControl(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlContainerControl(tag: str) """
    @property
    def InnerHtml(self) -> str:
        """
        Get: InnerHtml(self: HtmlContainerControl) -> str
        Set: InnerHtml(self: HtmlContainerControl) = value
        """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: HtmlContainerControl) -> str
        Set: InnerText(self: HtmlContainerControl) = value
        """
        ...


    def RenderEndTag(self, *args): #cannot find CLR method
        """ RenderEndTag(self: HtmlContainerControl, writer: HtmlTextWriter) """
        ...


class HtmlAnchor(HtmlContainerControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlAnchor() """
    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: HtmlAnchor) -> bool
        Set: CausesValidation(self: HtmlAnchor) = value
        """
        ...

    @property
    def HRef(self) -> str:
        """
        Get: HRef(self: HtmlAnchor) -> str
        Set: HRef(self: HtmlAnchor) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlAnchor) -> str
        Set: Name(self: HtmlAnchor) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HtmlAnchor) -> str
        Set: Target(self: HtmlAnchor) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: HtmlAnchor) -> str
        Set: Title(self: HtmlAnchor) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: HtmlAnchor) -> str
        Set: ValidationGroup(self: HtmlAnchor) = value
        """
        ...


    def OnServerClick(self, *args): #cannot find CLR method
        """ OnServerClick(self: HtmlAnchor, e: EventArgs) """
        ...

    ServerClick = ...


class HtmlArea(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlArea() """
    @property
    def Href(self) -> str:
        """
        Get: Href(self: HtmlArea) -> str
        Set: Href(self: HtmlArea) = value
        """
        ...



class HtmlAudio(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlAudio() """
    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlAudio) -> str
        Set: Src(self: HtmlAudio) = value
        """
        ...



class HtmlButton(HtmlContainerControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlButton() """
    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: HtmlButton) -> bool
        Set: CausesValidation(self: HtmlButton) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: HtmlButton) -> str
        Set: ValidationGroup(self: HtmlButton) = value
        """
        ...


    def OnServerClick(self, *args): #cannot find CLR method
        """ OnServerClick(self: HtmlButton, e: EventArgs) """
        ...

    ServerClick = ...


class HtmlElement(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlElement() """
    @property
    def Manifest(self) -> str:
        """
        Get: Manifest(self: HtmlElement) -> str
        Set: Manifest(self: HtmlElement) = value
        """
        ...



class HtmlEmbed(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlEmbed() """
    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlEmbed) -> str
        Set: Src(self: HtmlEmbed) = value
        """
        ...



class HtmlEmptyTagControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ HtmlEmptyTagControlBuilder() """
    pass

class HtmlForm(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlForm() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: HtmlForm) -> str
        Set: Action(self: HtmlForm) = value
        """
        ...

    @property
    def ClientID(self) -> str:
        """ Get: ClientID(self: HtmlForm) -> str """
        ...

    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: HtmlForm) -> str
        Set: DefaultButton(self: HtmlForm) = value
        """
        ...

    @property
    def DefaultFocus(self) -> str:
        """
        Get: DefaultFocus(self: HtmlForm) -> str
        Set: DefaultFocus(self: HtmlForm) = value
        """
        ...

    @property
    def Enctype(self) -> str:
        """
        Get: Enctype(self: HtmlForm) -> str
        Set: Enctype(self: HtmlForm) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: HtmlForm) -> str
        Set: Method(self: HtmlForm) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlForm) -> str
        Set: Name(self: HtmlForm) = value
        """
        ...

    @property
    def SubmitDisabledControls(self) -> bool:
        """
        Get: SubmitDisabledControls(self: HtmlForm) -> bool
        Set: SubmitDisabledControls(self: HtmlForm) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HtmlForm) -> str
        Set: Target(self: HtmlForm) = value
        """
        ...

    @property
    def UniqueID(self) -> str:
        """ Get: UniqueID(self: HtmlForm) -> str """
        ...



class HtmlGenericControl(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlGenericControl()
    HtmlGenericControl(tag: str)
    """
    @property
    def TagName(self) -> str:
        """
        Get: TagName(self: HtmlGenericControl) -> str
        Set: TagName(self: HtmlGenericControl) = value
        """
        ...



class HtmlHead(HtmlGenericControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlHead()
    HtmlHead(tag: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: HtmlHead) -> str
        Set: Description(self: HtmlHead) = value
        """
        ...

    @property
    def Keywords(self) -> str:
        """
        Get: Keywords(self: HtmlHead) -> str
        Set: Keywords(self: HtmlHead) = value
        """
        ...

    @property
    def StyleSheet(self) -> IStyleSheet:
        """ Get: StyleSheet(self: HtmlHead) -> IStyleSheet """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: HtmlHead) -> str
        Set: Title(self: HtmlHead) = value
        """
        ...



class HtmlHeadBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ HtmlHeadBuilder() """
    pass

class HtmlIframe(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlIframe() """
    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlIframe) -> str
        Set: Src(self: HtmlIframe) = value
        """
        ...



class HtmlImage(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlImage() """
    @property
    def Align(self) -> str:
        """
        Get: Align(self: HtmlImage) -> str
        Set: Align(self: HtmlImage) = value
        """
        ...

    @property
    def Alt(self) -> str:
        """
        Get: Alt(self: HtmlImage) -> str
        Set: Alt(self: HtmlImage) = value
        """
        ...

    @property
    def Border(self) -> int:
        """
        Get: Border(self: HtmlImage) -> int
        Set: Border(self: HtmlImage) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: HtmlImage) -> int
        Set: Height(self: HtmlImage) = value
        """
        ...

    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlImage) -> str
        Set: Src(self: HtmlImage) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: HtmlImage) -> int
        Set: Width(self: HtmlImage) = value
        """
        ...



class HtmlInputControl(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlInputControl) -> str
        Set: Name(self: HtmlInputControl) = value
        """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: HtmlInputControl) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HtmlInputControl) -> str
        Set: Value(self: HtmlInputControl) = value
        """
        ...



class HtmlInputButton(HtmlInputControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlInputButton()
    HtmlInputButton(type: str)
    """
    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: HtmlInputButton) -> bool
        Set: CausesValidation(self: HtmlInputButton) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: HtmlInputButton) -> str
        Set: ValidationGroup(self: HtmlInputButton) = value
        """
        ...


    def OnServerClick(self, *args): #cannot find CLR method
        """ OnServerClick(self: HtmlInputButton, e: EventArgs) """
        ...

    ServerClick = ...


class HtmlInputCheckBox(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlInputCheckBox() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: HtmlInputCheckBox) -> bool
        Set: Checked(self: HtmlInputCheckBox) = value
        """
        ...


    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlInputCheckBox, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlInputFile(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlInputFile() """
    @property
    def Accept(self) -> str:
        """
        Get: Accept(self: HtmlInputFile) -> str
        Set: Accept(self: HtmlInputFile) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: HtmlInputFile) -> int
        Set: MaxLength(self: HtmlInputFile) = value
        """
        ...

    @property
    def PostedFile(self) -> HttpPostedFile:
        """ Get: PostedFile(self: HtmlInputFile) -> HttpPostedFile """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: HtmlInputFile) -> int
        Set: Size(self: HtmlInputFile) = value
        """
        ...



class HtmlInputGenericControl(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlInputGenericControl()
    HtmlInputGenericControl(type: str)
    """
    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlInputGenericControl, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlInputHidden(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlInputHidden() """
    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlInputHidden, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlInputImage(IPostBackDataHandler, HtmlInputControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlInputImage() """
    @property
    def Align(self) -> str:
        """
        Get: Align(self: HtmlInputImage) -> str
        Set: Align(self: HtmlInputImage) = value
        """
        ...

    @property
    def Alt(self) -> str:
        """
        Get: Alt(self: HtmlInputImage) -> str
        Set: Alt(self: HtmlInputImage) = value
        """
        ...

    @property
    def Border(self) -> int:
        """
        Get: Border(self: HtmlInputImage) -> int
        Set: Border(self: HtmlInputImage) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: HtmlInputImage) -> bool
        Set: CausesValidation(self: HtmlInputImage) = value
        """
        ...

    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlInputImage) -> str
        Set: Src(self: HtmlInputImage) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: HtmlInputImage) -> str
        Set: ValidationGroup(self: HtmlInputImage) = value
        """
        ...


    def OnServerClick(self, *args): #cannot find CLR method
        """ OnServerClick(self: HtmlInputImage, e: ImageClickEventArgs) """
        ...

    ServerClick = ...


class HtmlInputText(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlInputText()
    HtmlInputText(type: str)
    """
    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: HtmlInputText) -> int
        Set: MaxLength(self: HtmlInputText) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: HtmlInputText) -> int
        Set: Size(self: HtmlInputText) = value
        """
        ...


    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlInputText, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlInputPassword(HtmlInputText): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IPostBackDataHandler'>, <type 'object'>
    """ HtmlInputPassword() """
    pass

class HtmlInputRadioButton(IPostBackDataHandler, HtmlInputControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlInputRadioButton() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: HtmlInputRadioButton) -> bool
        Set: Checked(self: HtmlInputRadioButton) = value
        """
        ...


    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlInputRadioButton, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlInputReset(HtmlInputButton): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IPostBackEventHandler'>, <type 'object'>
    """
    HtmlInputReset()
    HtmlInputReset(type: str)
    """
    ServerClick = ...


class HtmlInputSubmit(HtmlInputButton): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IPostBackEventHandler'>, <type 'object'>
    """
    HtmlInputSubmit()
    HtmlInputSubmit(type: str)
    """
    pass

class HtmlLink(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlLink() """
    @property
    def Href(self) -> str:
        """
        Get: Href(self: HtmlLink) -> str
        Set: Href(self: HtmlLink) = value
        """
        ...



class HtmlMeta(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlMeta() """
    @property
    def Content(self) -> str:
        """
        Get: Content(self: HtmlMeta) -> str
        Set: Content(self: HtmlMeta) = value
        """
        ...

    @property
    def HttpEquiv(self) -> str:
        """
        Get: HttpEquiv(self: HtmlMeta) -> str
        Set: HttpEquiv(self: HtmlMeta) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlMeta) -> str
        Set: Name(self: HtmlMeta) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: HtmlMeta) -> str
        Set: Scheme(self: HtmlMeta) = value
        """
        ...



class HtmlSelect(IPostBackDataHandler, HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlSelect() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: HtmlSelect) -> str
        Set: DataMember(self: HtmlSelect) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: HtmlSelect) -> object
        Set: DataSource(self: HtmlSelect) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: HtmlSelect) -> str
        Set: DataSourceID(self: HtmlSelect) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: HtmlSelect) -> str
        Set: DataTextField(self: HtmlSelect) = value
        """
        ...

    @property
    def DataValueField(self) -> str:
        """
        Get: DataValueField(self: HtmlSelect) -> str
        Set: DataValueField(self: HtmlSelect) = value
        """
        ...

    @property
    def IsBoundUsingDataSourceID(self):
        ...

    @property
    def Items(self) -> ListItemCollection:
        """ Get: Items(self: HtmlSelect) -> ListItemCollection """
        ...

    @property
    def Multiple(self) -> bool:
        """
        Get: Multiple(self: HtmlSelect) -> bool
        Set: Multiple(self: HtmlSelect) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlSelect) -> str
        Set: Name(self: HtmlSelect) = value
        """
        ...

    @property
    def RequiresDataBinding(self):
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: HtmlSelect) -> int
        Set: SelectedIndex(self: HtmlSelect) = value
        """
        ...

    @property
    def SelectedIndices(self):
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: HtmlSelect) -> int
        Set: Size(self: HtmlSelect) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HtmlSelect) -> str
        Set: Value(self: HtmlSelect) = value
        """
        ...


    def ClearSelection(self, *args): #cannot find CLR method
        """ ClearSelection(self: HtmlSelect) """
        ...

    def EnsureDataBound(self, *args): #cannot find CLR method
        """ EnsureDataBound(self: HtmlSelect) """
        ...

    def GetData(self, *args): #cannot find CLR method
        """ GetData(self: HtmlSelect) -> IEnumerable """
        ...

    def OnDataPropertyChanged(self, *args): #cannot find CLR method
        """ OnDataPropertyChanged(self: HtmlSelect) """
        ...

    def OnDataSourceViewChanged(self, *args): #cannot find CLR method
        """ OnDataSourceViewChanged(self: HtmlSelect, sender: object, e: EventArgs) """
        ...

    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlSelect, e: EventArgs) """
        ...

    def Select(self, *args): #cannot find CLR method
        """ Select(self: HtmlSelect, selectedIndices: Array[int]) """
        ...

    ServerChange = ...


class HtmlSelectBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ HtmlSelectBuilder() """
    pass

class HtmlSource(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlSource() """
    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlSource) -> str
        Set: Src(self: HtmlSource) = value
        """
        ...



class HtmlTable(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlTable() """
    @property
    def Align(self) -> str:
        """
        Get: Align(self: HtmlTable) -> str
        Set: Align(self: HtmlTable) = value
        """
        ...

    @property
    def BgColor(self) -> str:
        """
        Get: BgColor(self: HtmlTable) -> str
        Set: BgColor(self: HtmlTable) = value
        """
        ...

    @property
    def Border(self) -> int:
        """
        Get: Border(self: HtmlTable) -> int
        Set: Border(self: HtmlTable) = value
        """
        ...

    @property
    def BorderColor(self) -> str:
        """
        Get: BorderColor(self: HtmlTable) -> str
        Set: BorderColor(self: HtmlTable) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: HtmlTable) -> int
        Set: CellPadding(self: HtmlTable) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: HtmlTable) -> int
        Set: CellSpacing(self: HtmlTable) = value
        """
        ...

    @property
    def Height(self) -> str:
        """
        Get: Height(self: HtmlTable) -> str
        Set: Height(self: HtmlTable) = value
        """
        ...

    @property
    def Rows(self) -> HtmlTableRowCollection:
        """ Get: Rows(self: HtmlTable) -> HtmlTableRowCollection """
        ...

    @property
    def Width(self) -> str:
        """
        Get: Width(self: HtmlTable) -> str
        Set: Width(self: HtmlTable) = value
        """
        ...


    def HtmlTableRowControlCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class HtmlTableCell(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    HtmlTableCell()
    HtmlTableCell(tagName: str)
    """
    @property
    def Align(self) -> str:
        """
        Get: Align(self: HtmlTableCell) -> str
        Set: Align(self: HtmlTableCell) = value
        """
        ...

    @property
    def BgColor(self) -> str:
        """
        Get: BgColor(self: HtmlTableCell) -> str
        Set: BgColor(self: HtmlTableCell) = value
        """
        ...

    @property
    def BorderColor(self) -> str:
        """
        Get: BorderColor(self: HtmlTableCell) -> str
        Set: BorderColor(self: HtmlTableCell) = value
        """
        ...

    @property
    def ColSpan(self) -> int:
        """
        Get: ColSpan(self: HtmlTableCell) -> int
        Set: ColSpan(self: HtmlTableCell) = value
        """
        ...

    @property
    def Height(self) -> str:
        """
        Get: Height(self: HtmlTableCell) -> str
        Set: Height(self: HtmlTableCell) = value
        """
        ...

    @property
    def NoWrap(self) -> bool:
        """
        Get: NoWrap(self: HtmlTableCell) -> bool
        Set: NoWrap(self: HtmlTableCell) = value
        """
        ...

    @property
    def RowSpan(self) -> int:
        """
        Get: RowSpan(self: HtmlTableCell) -> int
        Set: RowSpan(self: HtmlTableCell) = value
        """
        ...

    @property
    def VAlign(self) -> str:
        """
        Get: VAlign(self: HtmlTableCell) -> str
        Set: VAlign(self: HtmlTableCell) = value
        """
        ...

    @property
    def Width(self) -> str:
        """
        Get: Width(self: HtmlTableCell) -> str
        Set: Width(self: HtmlTableCell) = value
        """
        ...



class HtmlTableCellCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HtmlTableCellCollection) -> bool """
        ...


    def Add(self, cell:HtmlTableCell): # -> 
        """ Add(self: HtmlTableCellCollection, cell: HtmlTableCell) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HtmlTableCellCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HtmlTableCellCollection) -> IEnumerator """
        ...

    def Insert(self, index:int, cell:HtmlTableCell): # -> 
        """ Insert(self: HtmlTableCellCollection, index: int, cell: HtmlTableCell) """
        ...

    def Remove(self, cell:HtmlTableCell): # -> 
        """ Remove(self: HtmlTableCellCollection, cell: HtmlTableCell) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HtmlTableCellCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HtmlTableRow(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlTableRow() """
    @property
    def Align(self) -> str:
        """
        Get: Align(self: HtmlTableRow) -> str
        Set: Align(self: HtmlTableRow) = value
        """
        ...

    @property
    def BgColor(self) -> str:
        """
        Get: BgColor(self: HtmlTableRow) -> str
        Set: BgColor(self: HtmlTableRow) = value
        """
        ...

    @property
    def BorderColor(self) -> str:
        """
        Get: BorderColor(self: HtmlTableRow) -> str
        Set: BorderColor(self: HtmlTableRow) = value
        """
        ...

    @property
    def Cells(self) -> HtmlTableCellCollection:
        """ Get: Cells(self: HtmlTableRow) -> HtmlTableCellCollection """
        ...

    @property
    def Height(self) -> str:
        """
        Get: Height(self: HtmlTableRow) -> str
        Set: Height(self: HtmlTableRow) = value
        """
        ...

    @property
    def VAlign(self) -> str:
        """
        Get: VAlign(self: HtmlTableRow) -> str
        Set: VAlign(self: HtmlTableRow) = value
        """
        ...


    def HtmlTableCellControlCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class HtmlTableRowCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HtmlTableRowCollection) -> bool """
        ...


    def Add(self, row:HtmlTableRow): # -> 
        """ Add(self: HtmlTableRowCollection, row: HtmlTableRow) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HtmlTableRowCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HtmlTableRowCollection) -> IEnumerator """
        ...

    def Insert(self, index:int, row:HtmlTableRow): # -> 
        """ Insert(self: HtmlTableRowCollection, index: int, row: HtmlTableRow) """
        ...

    def Remove(self, row:HtmlTableRow): # -> 
        """ Remove(self: HtmlTableRowCollection, row: HtmlTableRow) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HtmlTableRowCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HtmlTextArea(IPostBackDataHandler, HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlTextArea() """
    @property
    def Cols(self) -> int:
        """
        Get: Cols(self: HtmlTextArea) -> int
        Set: Cols(self: HtmlTextArea) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HtmlTextArea) -> str
        Set: Name(self: HtmlTextArea) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: HtmlTextArea) -> int
        Set: Rows(self: HtmlTextArea) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HtmlTextArea) -> str
        Set: Value(self: HtmlTextArea) = value
        """
        ...


    def OnServerChange(self, *args): #cannot find CLR method
        """ OnServerChange(self: HtmlTextArea, e: EventArgs) """
        ...

    ServerChange = ...


class HtmlTitle(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlTitle() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: HtmlTitle) -> str
        Set: Text(self: HtmlTitle) = value
        """
        ...



class HtmlTrack(HtmlControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlTrack() """
    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlTrack) -> str
        Set: Src(self: HtmlTrack) = value
        """
        ...



class HtmlVideo(HtmlContainerControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HtmlVideo() """
    @property
    def Poster(self) -> str:
        """
        Get: Poster(self: HtmlVideo) -> str
        Set: Poster(self: HtmlVideo) = value
        """
        ...

    @property
    def Src(self) -> str:
        """
        Get: Src(self: HtmlVideo) -> str
        Set: Src(self: HtmlVideo) = value
        """
        ...



