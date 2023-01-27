# encoding: utf-8
# module System.Web.UI.MobileControls.Adapters.XhtmlAdapters calls itself XhtmlAdapters
# from System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Word import Style

from System import Enum, EventArgs

from System.Web import HttpContext, IHttpHandler

from System.Web.Caching import Cache

from System.Web.SessionState import HttpSessionState, IRequiresSessionState

from System.Web.UI.Adapters import ControlAdapter

from System.Web.UI.MobileControls import IPageAdapter

from System.Web.UI.MobileControls.Adapters import MobileTextWriter

"""The following names are not found in the module: field#
"""

# no functions
# classes

class Doctype(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Doctype, values: NotSet (0), Wml20 (3), XhtmlBasic (1), XhtmlMobileProfile (2) """
    NotSet: Doctype = ...
    value__ = ...
    Wml20: Doctype = ...
    XhtmlBasic: Doctype = ...
    XhtmlMobileProfile: Doctype = ...


class StyleSheetLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StyleSheetLocation, values: ApplicationCache (1), Internal (4), None (5), NotSet (0), PhysicalFile (3), SessionState (2) """
    ApplicationCache: StyleSheetLocation = ...
    Internal: StyleSheetLocation = ...
    NotSet: StyleSheetLocation = ...
    PhysicalFile: StyleSheetLocation = ...
    SessionState: StyleSheetLocation = ...
    value__ = ...


class XhtmlControlAdapter(ControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlControlAdapter() """
    @property
    def CssLocation(self):
        ...

    @property
    def DocumentType(self):
        ...

    @property
    def PageAdapter(self):
        ...

    @property
    def SecondaryUIMode(self):
        ...

    @property
    def StyleSheetLocationAttributeValue(self):
        ...

    @property
    def StyleSheetStorageApplicationSetting(self):
        ...


    def ClearPendingBreakIfDeviceBreaksOnBlockLevel(self, *args): #cannot find CLR method
        """ ClearPendingBreakIfDeviceBreaksOnBlockLevel(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalClearCachedEndTag(self, *args): #cannot find CLR method
        """ ConditionalClearCachedEndTag(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, s: str) """
        ...

    def ConditionalClearPendingBreak(self, *args): #cannot find CLR method
        """ ConditionalClearPendingBreak(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalEnterFormat(self, *args): #cannot find CLR method
        """ ConditionalEnterFormat(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style) """
        ...

    def ConditionalEnterLayout(self, *args): #cannot find CLR method
        """ ConditionalEnterLayout(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style) """
        ...

    def ConditionalEnterStyle(self, *args): #cannot find CLR method
        """ ConditionalEnterStyle(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style)ConditionalEnterStyle(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style, tag: str) """
        ...

    def ConditionalExitFormat(self, *args): #cannot find CLR method
        """ ConditionalExitFormat(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style) """
        ...

    def ConditionalExitLayout(self, *args): #cannot find CLR method
        """ ConditionalExitLayout(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style) """
        ...

    def ConditionalExitStyle(self, *args): #cannot find CLR method
        """ ConditionalExitStyle(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, style: Style) """
        ...

    def ConditionalPopPhysicalCssClass(self, *args): #cannot find CLR method
        """ ConditionalPopPhysicalCssClass(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalRenderClassAttribute(self, *args): #cannot find CLR method
        """ ConditionalRenderClassAttribute(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalRenderClosingDivElement(self, *args): #cannot find CLR method
        """ ConditionalRenderClosingDivElement(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalRenderClosingSpanElement(self, *args): #cannot find CLR method
        """ ConditionalRenderClosingSpanElement(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalRenderCustomAttribute(self, *args): #cannot find CLR method
        """ ConditionalRenderCustomAttribute(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, attributeName: str)ConditionalRenderCustomAttribute(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, attributeName: str, markupAttributeName: str) """
        ...

    def ConditionalRenderOpeningDivElement(self, *args): #cannot find CLR method
        """ ConditionalRenderOpeningDivElement(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalRenderOpeningSpanElement(self, *args): #cannot find CLR method
        """ ConditionalRenderOpeningSpanElement(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalSetPendingBreak(self, *args): #cannot find CLR method
        """ ConditionalSetPendingBreak(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ConditionalSetPendingBreakAfterInline(self, *args): #cannot find CLR method
        """ ConditionalSetPendingBreakAfterInline(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def ExitSecondaryUIMode(self, *args): #cannot find CLR method
        """ ExitSecondaryUIMode(self: XhtmlControlAdapter) """
        ...

    def GetCustomAttributeValue(self, *args): #cannot find CLR method
        """
        GetCustomAttributeValue(self: XhtmlControlAdapter, attributeName: str) -> str
        GetCustomAttributeValue(self: XhtmlControlAdapter, control: MobileControl, attributeName: str) -> str
        """
        ...

    def PreprocessQueryString(self, *args): #cannot find CLR method
        """ PreprocessQueryString(self: XhtmlControlAdapter, queryString: str) -> str """
        ...

    def RenderAsHiddenInputField(self, *args): #cannot find CLR method
        """ RenderAsHiddenInputField(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def RenderBeginLink(self, *args): #cannot find CLR method
        """ RenderBeginLink(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, target: str, accessKey: str, style: Style, cssClass: str)RenderBeginLink(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, target: str, accessKey: str, style: Style, cssClass: str, title: str)RenderBeginLink(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, target: str) """
        ...

    def RenderClosingListTag(self, *args): #cannot find CLR method
        """ RenderClosingListTag(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, tagName: str) """
        ...

    def RenderEndLink(self, *args): #cannot find CLR method
        """ RenderEndLink(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def RenderOffPageVariables(self, *args): #cannot find CLR method
        """ RenderOffPageVariables(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, control: Control, page: int) """
        ...

    def RenderOpeningListTag(self, *args): #cannot find CLR method
        """ RenderOpeningListTag(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, tagName: str) """
        ...

    def RenderPostBackEventAsAnchor(self, *args): #cannot find CLR method
        """ RenderPostBackEventAsAnchor(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, argument: str, linkText: str)RenderPostBackEventAsAnchor(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, argument: str, linkText: str, accessKey: str)RenderPostBackEventAsAnchor(self: XhtmlControlAdapter, writer: XhtmlMobileTextWriter, argument: str, linkText: str, accessKey: str, style: Style, cssClass: str) """
        ...

    NotSecondaryUI: int = ...


class XhtmlCalendarAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlCalendarAdapter() """
    pass

class XhtmlCommandAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlCommandAdapter() """
    pass

class XhtmlCssHandler(IRequiresSessionState, IHttpHandler): # skipped bases: <type 'object'>
    """ XhtmlCssHandler() """
    pass

class XhtmlFormAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlFormAdapter() """
    def RenderPager(self, *args): #cannot find CLR method
        """ RenderPager(self: XhtmlFormAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def RenderPagerTag(self, *args): #cannot find CLR method
        """ RenderPagerTag(self: XhtmlFormAdapter, writer: XhtmlMobileTextWriter, pageToNavigate: int, text: str, accessKeyCustomAttribute: str) """
        ...


class XhtmlImageAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlImageAdapter() """
    def RenderImage(self, *args): #cannot find CLR method
        """ RenderImage(self: XhtmlImageAdapter, writer: XhtmlMobileTextWriter) """
        ...


class XhtmlLabelAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlLabelAdapter() """
    pass

class XhtmlLinkAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlLinkAdapter() """
    pass

class XhtmlListAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlListAdapter() """
    def RenderList(self, *args): #cannot find CLR method
        """ RenderList(self: XhtmlListAdapter, writer: XhtmlMobileTextWriter) """
        ...


class XhtmlLiteralTextAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlLiteralTextAdapter() """
    pass

class XhtmlMobileTextWriter(MobileTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ XhtmlMobileTextWriter(writer: TextWriter, device: MobileCapabilities) """
    @property
    def CacheKey(self) -> str:
        """ Get: CacheKey(self: XhtmlMobileTextWriter) -> str """
        ...

    @property
    def CustomBodyStyles(self) -> str:
        """
        Get: CustomBodyStyles(self: XhtmlMobileTextWriter) -> str
        Set: CustomBodyStyles(self: XhtmlMobileTextWriter) = value
        """
        ...

    @property
    def SessionKey(self) -> str:
        """ Get: SessionKey(self: XhtmlMobileTextWriter) -> str """
        ...

    @property
    def SupportsNoWrapStyle(self) -> bool:
        """
        Get: SupportsNoWrapStyle(self: XhtmlMobileTextWriter) -> bool
        Set: SupportsNoWrapStyle(self: XhtmlMobileTextWriter) = value
        """
        ...

    @property
    def SuppressNewLine(self) -> bool:
        """
        Get: SuppressNewLine(self: XhtmlMobileTextWriter) -> bool
        Set: SuppressNewLine(self: XhtmlMobileTextWriter) = value
        """
        ...

    @property
    def UseDivsForBreaks(self) -> bool:
        """
        Get: UseDivsForBreaks(self: XhtmlMobileTextWriter) -> bool
        Set: UseDivsForBreaks(self: XhtmlMobileTextWriter) = value
        """
        ...


    def AddOnEnterForwardSetVar(self, var:str, value:str = ...): # -> 
        """ AddOnEnterForwardSetVar(self: XhtmlMobileTextWriter, var: str)AddOnEnterForwardSetVar(self: XhtmlMobileTextWriter, var: str, value: str) """
        ...

    def BeginCachedRendering(self): # -> 
        """ BeginCachedRendering(self: XhtmlMobileTextWriter) """
        ...

    def ClearPendingBreak(self): # -> 
        """ ClearPendingBreak(self: XhtmlMobileTextWriter) """
        ...

    def EndCachedRendering(self): # -> 
        """ EndCachedRendering(self: XhtmlMobileTextWriter) """
        ...

    def IsStyleSheetEmpty(self) -> bool:
        """ IsStyleSheetEmpty(self: XhtmlMobileTextWriter) -> bool """
        ...

    def MarkWmlOnEventLocation(self): # -> 
        """ MarkWmlOnEventLocation(self: XhtmlMobileTextWriter) """
        ...

    def SetBodyStyle(self, style:Style): # -> 
        """ SetBodyStyle(self: XhtmlMobileTextWriter, style: Style) """
        ...

    def SetCacheKey(self, cache:Cache): # -> 
        """ SetCacheKey(self: XhtmlMobileTextWriter, cache: Cache) """
        ...

    def SetPendingBreak(self): # -> 
        """ SetPendingBreak(self: XhtmlMobileTextWriter) """
        ...

    def SetSessionKey(self, session:HttpSessionState): # -> 
        """ SetSessionKey(self: XhtmlMobileTextWriter, session: HttpSessionState) """
        ...

    def WriteAttribute(self, *__args): # -> 
        """ WriteAttribute(self: XhtmlMobileTextWriter, attribute: str, value: str, encode: bool) """
        ...

    def WriteBeginTag(self, tag:str): # -> 
        """ WriteBeginTag(self: XhtmlMobileTextWriter, tag: str) """
        ...

    def WriteBreak(self): # -> 
        """ WriteBreak(self: XhtmlMobileTextWriter) """
        ...

    def WriteCachedMarkup(self): # -> 
        """ WriteCachedMarkup(self: XhtmlMobileTextWriter) """
        ...

    def WriteDoctypeDeclaration(self, type:Doctype): # -> 
        """ WriteDoctypeDeclaration(self: XhtmlMobileTextWriter, type: Doctype) """
        ...

    def WriteEncodedAttributeValue(self, value:str): # -> 
        """ WriteEncodedAttributeValue(self: XhtmlMobileTextWriter, value: str) """
        ...

    def WriteEndTag(self, tag:str): # -> 
        """ WriteEndTag(self: XhtmlMobileTextWriter, tag: str) """
        ...

    def WriteFullBeginTag(self, tag:str): # -> 
        """ WriteFullBeginTag(self: XhtmlMobileTextWriter, tag: str) """
        ...

    def WriteHiddenField(self, name:str, value:str = ...): # -> 
        """ WriteHiddenField(self: XhtmlMobileTextWriter, name: str, value: str)WriteHiddenField(self: XhtmlMobileTextWriter, name: str) """
        ...

    def WriteLine(self, *__args:object): # -> 
        """ WriteLine(self: XhtmlMobileTextWriter)WriteLine(self: XhtmlMobileTextWriter, format: str, *arg: Array[object])WriteLine(self: XhtmlMobileTextWriter, format: str, arg: object)WriteLine(self: XhtmlMobileTextWriter, format: str, arg0: object, arg1: object)WriteLine(self: XhtmlMobileTextWriter, v: object)WriteLine(self: XhtmlMobileTextWriter, s: str)WriteLine(self: XhtmlMobileTextWriter, v: float)WriteLine(self: XhtmlMobileTextWriter, v: Single)WriteLine(self: XhtmlMobileTextWriter, v: Int64)WriteLine(self: XhtmlMobileTextWriter, v: int)WriteLine(self: XhtmlMobileTextWriter, v: bool)WriteLine(self: XhtmlMobileTextWriter, buffer: Array[Char], index: int, count: int)WriteLine(self: XhtmlMobileTextWriter, v: Array[Char])WriteLine(self: XhtmlMobileTextWriter, v: Char) """
        ...

    def WritePendingBreak(self): # -> 
        """ WritePendingBreak(self: XhtmlMobileTextWriter) """
        ...

    def WriteUrlParameter(self, name:str, value:str): # -> 
        """ WriteUrlParameter(self: XhtmlMobileTextWriter, name: str, value: str) """
        ...

    def WriteXmlDeclaration(self): # -> 
        """ WriteXmlDeclaration(self: XhtmlMobileTextWriter) """
        ...

    CoreNewLine = ...


class XhtmlObjectListAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlObjectListAdapter() """
    def HasCommands(self, *args): #cannot find CLR method
        """ HasCommands(self: XhtmlObjectListAdapter) -> bool """
        ...

    def HasDefaultCommand(self, *args): #cannot find CLR method
        """ HasDefaultCommand(self: XhtmlObjectListAdapter) -> bool """
        ...

    def HasItemDetails(self, *args): #cannot find CLR method
        """ HasItemDetails(self: XhtmlObjectListAdapter) -> bool """
        ...

    def OnlyHasDefaultCommand(self, *args): #cannot find CLR method
        """ OnlyHasDefaultCommand(self: XhtmlObjectListAdapter) -> bool """
        ...

    def RenderItemDetails(self, *args): #cannot find CLR method
        """ RenderItemDetails(self: XhtmlObjectListAdapter, writer: XhtmlMobileTextWriter, item: ObjectListItem) """
        ...

    def RenderItemsList(self, *args): #cannot find CLR method
        """ RenderItemsList(self: XhtmlObjectListAdapter, writer: XhtmlMobileTextWriter) """
        ...

    BackToList: str = ...
    ShowMore: str = ...
    ShowMoreFormat: str = ...


class XhtmlPageAdapter(XhtmlControlAdapter, IPageAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlPageAdapter() """
    @property
    def EventArgumentKey(self) -> str:
        """ Get: EventArgumentKey(self: XhtmlPageAdapter) -> str """
        ...

    @property
    def EventSourceKey(self) -> str:
        """ Get: EventSourceKey(self: XhtmlPageAdapter) -> str """
        ...


    @staticmethod
    def DeviceQualifies(context:HttpContext) -> bool:
        """ DeviceQualifies(context: HttpContext) -> bool """
        ...

    def InitWriterState(self, *args): #cannot find CLR method
        """ InitWriterState(self: XhtmlPageAdapter, writer: XhtmlMobileTextWriter) """
        ...

    def OnPreRender(self, e:EventArgs): # -> 
        """ OnPreRender(self: XhtmlPageAdapter, e: EventArgs) """
        ...

    def RenderUrlPostBackEvent(self, writer:XhtmlMobileTextWriter, target:str, argument:str): # -> 
        """ RenderUrlPostBackEvent(self: XhtmlPageAdapter, writer: XhtmlMobileTextWriter, target: str, argument: str) """
        ...


class XhtmlPanelAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlPanelAdapter() """
    pass

class XhtmlPhoneCallAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlPhoneCallAdapter() """
    pass

class XhtmlSelectionListAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlSelectionListAdapter() """
    pass

class XhtmlTextBoxAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlTextBoxAdapter() """
    pass

class XhtmlTextViewAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlTextViewAdapter() """
    def RenderElement(self, writer:XhtmlMobileTextWriter, index:int, beginSubstring:int, endSubstring:int): # -> 
        """ RenderElement(self: XhtmlTextViewAdapter, writer: XhtmlMobileTextWriter, index: int, beginSubstring: int, endSubstring: int) """
        ...


class XhtmlValidationSummaryAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlValidationSummaryAdapter() """
    pass

class XhtmlValidatorAdapter(XhtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ XhtmlValidatorAdapter() """
    pass

