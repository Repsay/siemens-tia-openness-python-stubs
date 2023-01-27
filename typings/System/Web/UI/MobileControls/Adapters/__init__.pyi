# encoding: utf-8
# module System.Web.UI.MobileControls.Adapters calls itself Adapters
# from System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Word import Style

from System import Byte, Char, Enum, Int16, Int64, Single

from System.Collections import IDictionary

from System.Web import HttpContext

from System.Web.Mobile import MobileCapabilities

from System.Web.UI import HtmlTextWriter

from System.Web.UI.MobileControls import IControlAdapter, IPageAdapter

from System.Windows.Forms import Form

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ControlAdapter(IControlAdapter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Device(self) -> MobileCapabilities:
        """ Get: Device(self: ControlAdapter) -> MobileCapabilities """
        ...

    @property
    def Style(self) -> Style:
        """ Get: Style(self: ControlAdapter) -> Style """
        ...


    def CalculateOptimumPageWeight(self, *args): #cannot find CLR method
        """ CalculateOptimumPageWeight(self: ControlAdapter, defaultPageWeight: int) -> int """
        ...

    def GetDefaultLabel(self, *args): #cannot find CLR method
        """ GetDefaultLabel(self: ControlAdapter, labelID: int) -> str """
        ...

    def RenderChildren(self, *args): #cannot find CLR method
        """ RenderChildren(self: ControlAdapter, writer: HtmlTextWriter) """
        ...

    BackLabel: int = ...
    CallLabel: int = ...
    GoLabel: int = ...
    LinkLabel: int = ...
    MoreLabel: int = ...
    NextLabel: int = ...
    OKLabel: int = ...
    OptionsLabel: int = ...
    PreviousLabel: int = ...


class HtmlControlAdapter(ControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlControlAdapter() """
    @property
    def FormAdapter(self):
        ...

    @property
    def PageAdapter(self):
        ...

    @property
    def RequiresFormTag(self) -> bool:
        """ Get: RequiresFormTag(self: HtmlControlAdapter) -> bool """
        ...

    @property
    def SecondaryUIMode(self):
        ...


    def AddAccesskeyAttribute(self, *args): #cannot find CLR method
        """ AddAccesskeyAttribute(self: HtmlControlAdapter, writer: HtmlMobileTextWriter) """
        ...

    def AddAttributes(self, *args): #cannot find CLR method
        """ AddAttributes(self: HtmlControlAdapter, writer: HtmlMobileTextWriter) """
        ...

    def AddJPhoneMultiMediaAttributes(self, *args): #cannot find CLR method
        """ AddJPhoneMultiMediaAttributes(self: HtmlControlAdapter, writer: HtmlMobileTextWriter) """
        ...

    def ExitSecondaryUIMode(self, *args): #cannot find CLR method
        """ ExitSecondaryUIMode(self: HtmlControlAdapter) """
        ...

    def RenderAsHiddenInputField(self, *args): #cannot find CLR method
        """ RenderAsHiddenInputField(self: HtmlControlAdapter, writer: HtmlMobileTextWriter) """
        ...

    def RenderBeginLink(self, *args): #cannot find CLR method
        """ RenderBeginLink(self: HtmlControlAdapter, writer: HtmlMobileTextWriter, target: str) """
        ...

    def RenderEndLink(self, *args): #cannot find CLR method
        """ RenderEndLink(self: HtmlControlAdapter, writer: HtmlMobileTextWriter) """
        ...

    def RenderPostBackEventAsAnchor(self, *args): #cannot find CLR method
        """ RenderPostBackEventAsAnchor(self: HtmlControlAdapter, writer: HtmlMobileTextWriter, argument: str, linkText: str) """
        ...

    def RenderPostBackEventAsAttribute(self, *args): #cannot find CLR method
        """ RenderPostBackEventAsAttribute(self: HtmlControlAdapter, writer: HtmlMobileTextWriter, attributeName: str, argument: str) """
        ...

    def RenderPostBackEventReference(self, *args): #cannot find CLR method
        """ RenderPostBackEventReference(self: HtmlControlAdapter, writer: HtmlMobileTextWriter, argument: str) """
        ...

    NotSecondaryUI: int = ...


class ChtmlCalendarAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlCalendarAdapter() """
    pass

class HtmlCommandAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlCommandAdapter() """
    pass

class ChtmlCommandAdapter(HtmlCommandAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlCommandAdapter() """
    @property
    def RequiresFormTag(self) -> bool:
        """ Get: RequiresFormTag(self: ChtmlCommandAdapter) -> bool """
        ...



class HtmlFormAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlFormAdapter() """
    def DisablePager(self, *args): #cannot find CLR method
        """ DisablePager(self: HtmlFormAdapter) """
        ...

    def RenderBodyTag(self, *args): #cannot find CLR method
        """ RenderBodyTag(self: HtmlFormAdapter, writer: HtmlMobileTextWriter, attributes: IDictionary) """
        ...

    def RenderExtraHeadElements(self, *args): #cannot find CLR method
        """ RenderExtraHeadElements(self: HtmlFormAdapter, writer: HtmlMobileTextWriter) -> bool """
        ...

    def RenderPager(self, *args): #cannot find CLR method
        """ RenderPager(self: HtmlFormAdapter, writer: HtmlMobileTextWriter) """
        ...

    def RenderPagerTag(self, *args): #cannot find CLR method
        """ RenderPagerTag(self: HtmlFormAdapter, writer: HtmlMobileTextWriter, pageToNavigate: int, text: str) """
        ...

    def ShouldRenderFormTag(self, *args): #cannot find CLR method
        """ ShouldRenderFormTag(self: HtmlFormAdapter) -> bool """
        ...


class ChtmlFormAdapter(HtmlFormAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlFormAdapter() """
    pass

class HtmlImageAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlImageAdapter() """
    def RenderImage(self, *args): #cannot find CLR method
        """ RenderImage(self: HtmlImageAdapter, writer: HtmlMobileTextWriter) """
        ...


class ChtmlImageAdapter(HtmlImageAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlImageAdapter() """
    pass

class HtmlLinkAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlLinkAdapter() """
    pass

class ChtmlLinkAdapter(HtmlLinkAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlLinkAdapter() """
    pass

class MultiPartWriter(HtmlTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def SupportsMultiPart(self) -> bool:
        """ Get: SupportsMultiPart(self: MultiPartWriter) -> bool """
        ...


    def AddResource(self, url:str, contentType:str = ...): # -> 
        """ AddResource(self: MultiPartWriter, url: str, contentType: str)AddResource(self: MultiPartWriter, url: str) """
        ...

    def BeginFile(self, url:str, contentType:str, charset:str): # -> 
        """ BeginFile(self: MultiPartWriter, url: str, contentType: str, charset: str) """
        ...

    def BeginResponse(self): # -> 
        """ BeginResponse(self: MultiPartWriter) """
        ...

    def EndFile(self): # -> 
        """ EndFile(self: MultiPartWriter) """
        ...

    def EndResponse(self): # -> 
        """ EndResponse(self: MultiPartWriter) """
        ...

    def NewUrl(self, filetype:str) -> str:
        """ NewUrl(self: MultiPartWriter, filetype: str) -> str """
        ...

    CoreNewLine = ...


class MobileTextWriter(MultiPartWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ MobileTextWriter(writer: TextWriter, device: MobileCapabilities) """
    @property
    def Device(self) -> MobileCapabilities:
        """ Get: Device(self: MobileTextWriter) -> MobileCapabilities """
        ...


    def EnterFormat(self, style:Style): # -> 
        """ EnterFormat(self: MobileTextWriter, style: Style) """
        ...

    def EnterLayout(self, style:Style): # -> 
        """ EnterLayout(self: MobileTextWriter, style: Style) """
        ...

    def EnterStyle(self, style, tag=None): # -> 
        """ EnterStyle(self: MobileTextWriter, style: Style) """
        ...

    def ExitFormat(self, style:Style, breakAfter:bool = ...): # -> 
        """ ExitFormat(self: MobileTextWriter, style: Style)ExitFormat(self: MobileTextWriter, style: Style, breakAfter: bool) """
        ...

    def ExitLayout(self, style:Style, breakAfter:bool = ...): # -> 
        """ ExitLayout(self: MobileTextWriter, style: Style, breakAfter: bool)ExitLayout(self: MobileTextWriter, style: Style) """
        ...

    def ExitStyle(self, style, tag=None): # -> 
        """ ExitStyle(self: MobileTextWriter, style: Style) """
        ...

    CoreNewLine = ...


class HtmlMobileTextWriter(MobileTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ HtmlMobileTextWriter(writer: TextWriter, device: MobileCapabilities) """
    @property
    def RenderBodyColor(self):
        ...

    @property
    def RenderBold(self):
        ...

    @property
    def RenderDivAlign(self):
        ...

    @property
    def RenderDivNoWrap(self):
        ...

    @property
    def RenderFontColor(self):
        ...

    @property
    def RenderFontName(self):
        ...

    @property
    def RenderFontSize(self):
        ...

    @property
    def RenderItalic(self):
        ...

    @property
    def RequiresNoBreakInFormatting(self):
        ...


    def BeginStyleContext(self): # -> 
        """ BeginStyleContext(self: HtmlMobileTextWriter) """
        ...

    def EndStyleContext(self): # -> 
        """ EndStyleContext(self: HtmlMobileTextWriter) """
        ...

    def MarkStyleContext(self, *args): #cannot find CLR method
        """ MarkStyleContext(self: HtmlMobileTextWriter) """
        ...

    def UnMarkStyleContext(self, *args): #cannot find CLR method
        """ UnMarkStyleContext(self: HtmlMobileTextWriter) """
        ...

    def Write(self, *__args:Char): # -> 
        """ Write(self: HtmlMobileTextWriter, c: Char)Write(self: HtmlMobileTextWriter, text: str) """
        ...

    def WriteBeginTag(self, tag:str): # -> 
        """ WriteBeginTag(self: HtmlMobileTextWriter, tag: str) """
        ...

    def WriteBreak(self): # -> 
        """ WriteBreak(self: HtmlMobileTextWriter) """
        ...

    def WriteEncodedText(self, text:str): # -> 
        """ WriteEncodedText(self: HtmlMobileTextWriter, text: str) """
        ...

    def WriteFullBeginTag(self, tag:str): # -> 
        """ WriteFullBeginTag(self: HtmlMobileTextWriter, tag: str) """
        ...

    def WriteHiddenField(self, name:str, value:str): # -> 
        """ WriteHiddenField(self: HtmlMobileTextWriter, name: str, value: str) """
        ...

    def WriteLine(self, *__args:str): # -> 
        """ WriteLine(self: HtmlMobileTextWriter, text: str) """
        ...

    def WriteText(self, text:str, encodeText:bool): # -> 
        """ WriteText(self: HtmlMobileTextWriter, text: str, encodeText: bool) """
        ...

    def WriteUrlParameter(self, name:str, value:str): # -> 
        """ WriteUrlParameter(self: HtmlMobileTextWriter, name: str, value: str) """
        ...

    CoreNewLine = ...


class ChtmlMobileTextWriter(HtmlMobileTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ ChtmlMobileTextWriter(writer: TextWriter, device: MobileCapabilities) """
    CoreNewLine = ...


class HtmlPageAdapter(HtmlControlAdapter, IPageAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlPageAdapter() """
    @property
    def EventArgumentKey(self):
        ...

    @property
    def EventSourceKey(self):
        ...


    @staticmethod
    def DeviceQualifies(context:HttpContext) -> bool:
        """ DeviceQualifies(context: HttpContext) -> bool """
        ...

    def GetFormUrl(self, form:Form) -> str:
        """ GetFormUrl(self: HtmlPageAdapter, form: Form) -> str """
        ...

    def IsFormRendered(self, form:Form) -> bool:
        """ IsFormRendered(self: HtmlPageAdapter, form: Form) -> bool """
        ...

    def RenderForm(self, writer:HtmlMobileTextWriter, form:Form): # -> 
        """ RenderForm(self: HtmlPageAdapter, writer: HtmlMobileTextWriter, form: Form) """
        ...

    def RenderHiddenVariables(self, *args): #cannot find CLR method
        """ RenderHiddenVariables(self: HtmlPageAdapter, writer: HtmlMobileTextWriter) """
        ...

    def RenderPostBackEvent(self, writer:HtmlMobileTextWriter, target:str, argument:str): # -> 
        """ RenderPostBackEvent(self: HtmlPageAdapter, writer: HtmlMobileTextWriter, target: str, argument: str) """
        ...

    def RenderPostBackHeader(self, writer:HtmlMobileTextWriter, form:Form): # -> 
        """ RenderPostBackHeader(self: HtmlPageAdapter, writer: HtmlMobileTextWriter, form: Form) """
        ...

    def RenderUrlPostBackEvent(self, writer:HtmlMobileTextWriter, target:str, argument:str): # -> 
        """ RenderUrlPostBackEvent(self: HtmlPageAdapter, writer: HtmlMobileTextWriter, target: str, argument: str) """
        ...

    def __new__(cls) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, defaultPageWeight: int)
        """
        ...


class ChtmlPageAdapter(HtmlPageAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'IPageAdapter'>, <type 'object'>
    """ ChtmlPageAdapter() """
    pass

class HtmlPhoneCallAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlPhoneCallAdapter() """
    pass

class ChtmlPhoneCallAdapter(HtmlPhoneCallAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlPhoneCallAdapter() """
    pass

class HtmlSelectionListAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlSelectionListAdapter() """
    pass

class ChtmlSelectionListAdapter(HtmlSelectionListAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlSelectionListAdapter() """
    @property
    def RequiresFormTag(self) -> bool:
        """ Get: RequiresFormTag(self: ChtmlSelectionListAdapter) -> bool """
        ...



class HtmlTextBoxAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlTextBoxAdapter() """
    pass

class ChtmlTextBoxAdapter(HtmlTextBoxAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ ChtmlTextBoxAdapter() """
    @property
    def RequiresFormTag(self) -> bool:
        """ Get: RequiresFormTag(self: ChtmlTextBoxAdapter) -> bool """
        ...



class HtmlCalendarAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlCalendarAdapter() """
    pass

class HtmlLabelAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlLabelAdapter() """
    def WhiteSpace(self, *args): #cannot find CLR method
        """ WhiteSpace(self: HtmlLabelAdapter, s: str) -> bool """
        ...


class HtmlListAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlListAdapter() """
    def RenderList(self, *args): #cannot find CLR method
        """ RenderList(self: HtmlListAdapter, writer: HtmlMobileTextWriter) """
        ...


class HtmlLiteralTextAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlLiteralTextAdapter() """
    pass

class HtmlObjectListAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlObjectListAdapter() """
    def HasCommands(self, *args): #cannot find CLR method
        """ HasCommands(self: HtmlObjectListAdapter) -> bool """
        ...

    def HasDefaultCommand(self, *args): #cannot find CLR method
        """ HasDefaultCommand(self: HtmlObjectListAdapter) -> bool """
        ...

    def HasItemDetails(self, *args): #cannot find CLR method
        """ HasItemDetails(self: HtmlObjectListAdapter) -> bool """
        ...

    def OnlyHasDefaultCommand(self, *args): #cannot find CLR method
        """ OnlyHasDefaultCommand(self: HtmlObjectListAdapter) -> bool """
        ...

    def RenderItemDetails(self, *args): #cannot find CLR method
        """ RenderItemDetails(self: HtmlObjectListAdapter, writer: HtmlMobileTextWriter, item: ObjectListItem) """
        ...

    def RenderItemsList(self, *args): #cannot find CLR method
        """ RenderItemsList(self: HtmlObjectListAdapter, writer: HtmlMobileTextWriter) """
        ...

    def ShouldRenderAsTable(self, *args): #cannot find CLR method
        """ ShouldRenderAsTable(self: HtmlObjectListAdapter) -> bool """
        ...

    BackToList: str = ...
    ShowMore: str = ...
    ShowMoreFormat: str = ...


class HtmlPanelAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlPanelAdapter() """
    pass

class HtmlTextViewAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlTextViewAdapter() """
    pass

class HtmlValidationSummaryAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlValidationSummaryAdapter() """
    pass

class HtmlValidatorAdapter(HtmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ HtmlValidatorAdapter() """
    pass

class SR: # skipped bases: <type 'object'>, <type 'object'>
    """ SR() """
    @staticmethod
    def GetBoolean(*__args:str) -> bool:
        """
        GetBoolean(name: str) -> bool
        GetBoolean(culture: CultureInfo, name: str) -> bool
        """
        ...

    @staticmethod
    def GetByte(*__args:str) -> Byte:
        """
        GetByte(name: str) -> Byte
        GetByte(culture: CultureInfo, name: str) -> Byte
        """
        ...

    @staticmethod
    def GetChar(*__args:str) -> Char:
        """
        GetChar(name: str) -> Char
        GetChar(culture: CultureInfo, name: str) -> Char
        """
        ...

    @staticmethod
    def GetDouble(*__args:str) -> float:
        """
        GetDouble(name: str) -> float
        GetDouble(culture: CultureInfo, name: str) -> float
        """
        ...

    @staticmethod
    def GetFloat(*__args:str) -> Single:
        """
        GetFloat(name: str) -> Single
        GetFloat(culture: CultureInfo, name: str) -> Single
        """
        ...

    @staticmethod
    def GetInt(*__args:str) -> int:
        """
        GetInt(name: str) -> int
        GetInt(culture: CultureInfo, name: str) -> int
        """
        ...

    @staticmethod
    def GetLong(*__args:str) -> Int64:
        """
        GetLong(name: str) -> Int64
        GetLong(culture: CultureInfo, name: str) -> Int64
        """
        ...

    @staticmethod
    def GetObject(*__args:str) -> object:
        """
        GetObject(name: str) -> object
        GetObject(culture: CultureInfo, name: str) -> object
        """
        ...

    @staticmethod
    def GetShort(*__args:str) -> Int16:
        """
        GetShort(name: str) -> Int16
        GetShort(culture: CultureInfo, name: str) -> Int16
        """
        ...

    @staticmethod
    def GetString(*__args:str) -> str:
        """
        GetString(name: str, *args: Array[object]) -> str
        GetString(culture: CultureInfo, name: str, *args: Array[object]) -> str
        GetString(name: str) -> str
        GetString(culture: CultureInfo, name: str) -> str
        """
        ...

    CalendarAdapterFirstPrompt: str = ...
    CalendarAdapterOptionChooseDate: str = ...
    CalendarAdapterOptionChooseMonth: str = ...
    CalendarAdapterOptionChooseWeek: str = ...
    CalendarAdapterOptionEra: str = ...
    CalendarAdapterOptionPrompt: str = ...
    CalendarAdapterOptionType: str = ...
    CalendarAdapterTextBoxErrorMessage: str = ...
    ChtmlImageAdapterDecimalCodeExpectedAfterGroupChar: str = ...
    ChtmlPageAdapterRedirectLinkLabel: str = ...
    ChtmlPageAdapterRedirectPageContent: str = ...
    ControlAdapterBasePagePropertyShouldNotBeSet: str = ...
    FormAdapterMultiControlsAttemptSecondaryUI: str = ...
    MobileTextWriterNotMultiPart: str = ...
    ObjectListAdapter_InvalidPostedData: str = ...
    WmlMobileTextWriterBackLabel: str = ...
    WmlMobileTextWriterGoLabel: str = ...
    WmlMobileTextWriterOKLabel: str = ...
    WmlObjectListAdapterDetails: str = ...
    WmlPageAdapterMethod: str = ...
    WmlPageAdapterPartialStackTrace: str = ...
    WmlPageAdapterServerError: str = ...
    WmlPageAdapterStackTrace: str = ...
    XhtmlCssHandler_IdNotPresent: str = ...
    XhtmlCssHandler_StylesheetNotFound: str = ...
    XhtmlMobileTextWriter_CacheKeyNotSet: str = ...
    XhtmlMobileTextWriter_SessionKeyNotSet: str = ...
    XhtmlObjectListAdapter_InvalidPostedData: str = ...


class WmlMobileTextWriter(MobileTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ WmlMobileTextWriter(writer: TextWriter, device: MobileCapabilities, page: MobilePage) """
    @property
    def AnalyzeMode(self) -> bool:
        """
        Get: AnalyzeMode(self: WmlMobileTextWriter) -> bool
        Set: AnalyzeMode(self: WmlMobileTextWriter) = value
        """
        ...

    @property
    def CurrentForm(self):
        ...

    @property
    def DefaultFormat(self):
        ...

    @property
    def DefaultLayout(self):
        ...

    @property
    def NumberOfSoftkeys(self):
        ...

    @property
    def Page(self):
        ...

    @property
    def PendingBreak(self):
        ...


    def AddFormVariable(self, clientID:str, value:str, generateRandomID:bool): # -> 
        """ AddFormVariable(self: WmlMobileTextWriter, clientID: str, value: str, generateRandomID: bool) """
        ...

    def AnalyzePostBack(self, *args): #cannot find CLR method
        """ AnalyzePostBack(self: WmlMobileTextWriter, includeVariables: bool, postBackType: WmlPostFieldType) """
        ...

    def BeginCustomMarkup(self): # -> 
        """ BeginCustomMarkup(self: WmlMobileTextWriter) """
        ...

    def BeginForm(self, form:Form): # -> 
        """ BeginForm(self: WmlMobileTextWriter, form: Form) """
        ...

    def CalculateFormPostBackUrl(self, *args): #cannot find CLR method
        """ CalculateFormPostBackUrl(self: WmlMobileTextWriter, externalSubmit: bool, encode: bool) -> (str, bool) """
        ...

    def CalculateFormQueryString(self, *args): #cannot find CLR method
        """ CalculateFormQueryString(self: WmlMobileTextWriter) -> str """
        ...

    def CloseCharacterFormat(self, *args): #cannot find CLR method
        """ CloseCharacterFormat(self: WmlMobileTextWriter) """
        ...

    def CloseParagraph(self, *args): #cannot find CLR method
        """ CloseParagraph(self: WmlMobileTextWriter) """
        ...

    def EndCustomMarkup(self): # -> 
        """ EndCustomMarkup(self: WmlMobileTextWriter) """
        ...

    def EndForm(self): # -> 
        """ EndForm(self: WmlMobileTextWriter) """
        ...

    def EnsureFormat(self, *args): #cannot find CLR method
        """ EnsureFormat(self: WmlMobileTextWriter) """
        ...

    def EnsureLayout(self, *args): #cannot find CLR method
        """ EnsureLayout(self: WmlMobileTextWriter) """
        ...

    def IsValidSoftkeyLabel(self, label:str) -> bool:
        """ IsValidSoftkeyLabel(self: WmlMobileTextWriter, label: str) -> bool """
        ...

    def MapClientIDToShortName(self, *args): #cannot find CLR method
        """ MapClientIDToShortName(self: WmlMobileTextWriter, clientID: str, generateRandomID: bool) -> str """
        ...

    def OpenCharacterFormat(self, *args): #cannot find CLR method
        """ OpenCharacterFormat(self: WmlMobileTextWriter, format: WmlFormat, writeBold: bool, writeItalic: bool, writeSize: bool) """
        ...

    def OpenParagraph(self, *args): #cannot find CLR method
        """ OpenParagraph(self: WmlMobileTextWriter, layout: WmlLayout, writeAlignment: bool, writeWrapping: bool) """
        ...

    def PostAnalyzeForm(self, *args): #cannot find CLR method
        """ PostAnalyzeForm(self: WmlMobileTextWriter) """
        ...

    def RenderBeginForm(self, *args): #cannot find CLR method
        """ RenderBeginForm(self: WmlMobileTextWriter, form: Form) """
        ...

    def RenderBeginHyperlink(self, targetUrl:str, encodeUrl:bool, softkeyLabel:str, implicitSoftkeyLabel:bool, mapToSoftkey:bool): # -> 
        """ RenderBeginHyperlink(self: WmlMobileTextWriter, targetUrl: str, encodeUrl: bool, softkeyLabel: str, implicitSoftkeyLabel: bool, mapToSoftkey: bool) """
        ...

    def RenderBeginPostBack(self, softkeyLabel:str, implicitSoftkeyLabel:bool, mapToSoftkey:bool): # -> 
        """ RenderBeginPostBack(self: WmlMobileTextWriter, softkeyLabel: str, implicitSoftkeyLabel: bool, mapToSoftkey: bool) """
        ...

    def RenderBeginSelect(self, name:str, iname:str, ivalue:str, title:str, multiSelect:bool): # -> 
        """ RenderBeginSelect(self: WmlMobileTextWriter, name: str, iname: str, ivalue: str, title: str, multiSelect: bool) """
        ...

    def RenderDoEvent(self, *args): #cannot find CLR method
        """ RenderDoEvent(self: WmlMobileTextWriter, doType: str, target: str, arg: str, postBackType: WmlPostFieldType, text: str, includeVariables: bool) """
        ...

    def RenderEndForm(self, *args): #cannot find CLR method
        """ RenderEndForm(self: WmlMobileTextWriter) """
        ...

    def RenderEndHyperlink(self, breakAfter:bool): # -> 
        """ RenderEndHyperlink(self: WmlMobileTextWriter, breakAfter: bool) """
        ...

    def RenderEndPostBack(self, target:str, argument:str, postBackType:WmlPostFieldType, includeVariables:bool, breakAfter:bool): # -> 
        """ RenderEndPostBack(self: WmlMobileTextWriter, target: str, argument: str, postBackType: WmlPostFieldType, includeVariables: bool, breakAfter: bool) """
        ...

    def RenderEndSelect(self, breakAfter:bool): # -> 
        """ RenderEndSelect(self: WmlMobileTextWriter, breakAfter: bool) """
        ...

    def RenderExtraCards(self): # -> 
        """ RenderExtraCards(self: WmlMobileTextWriter) """
        ...

    def RenderFormDoEvent(self, *args): #cannot find CLR method
        """ RenderFormDoEvent(self: WmlMobileTextWriter, doType: str, arg: str, postBackType: WmlPostFieldType, text: str) """
        ...

    def RenderGoAction(self, target:str, argument:str, postBackType:WmlPostFieldType, includeVariables:bool): # -> 
        """ RenderGoAction(self: WmlMobileTextWriter, target: str, argument: str, postBackType: WmlPostFieldType, includeVariables: bool) """
        ...

    def RenderImage(self, source:str, localSource:str, alternateText:str, breakAfter:bool): # -> 
        """ RenderImage(self: WmlMobileTextWriter, source: str, localSource: str, alternateText: str, breakAfter: bool) """
        ...

    def RenderSelectOption(self, text:str, value:str = ...): # -> 
        """ RenderSelectOption(self: WmlMobileTextWriter, text: str)RenderSelectOption(self: WmlMobileTextWriter, text: str, value: str) """
        ...

    def RenderText(self, text:str, breakAfter:bool = ..., encodeText:bool = ...): # -> 
        """ RenderText(self: WmlMobileTextWriter, text: str)RenderText(self: WmlMobileTextWriter, text: str, breakAfter: bool)RenderText(self: WmlMobileTextWriter, text: str, breakAfter: bool, encodeText: bool) """
        ...

    def RenderTextBox(self, id:str, value:str, format:str, title:str, password:bool, size:int, maxLength:int, generateRandomID:bool, breakAfter:bool): # -> 
        """ RenderTextBox(self: WmlMobileTextWriter, id: str, value: str, format: str, title: str, password: bool, size: int, maxLength: int, generateRandomID: bool, breakAfter: bool) """
        ...

    def ResetFormattingState(self): # -> 
        """ ResetFormattingState(self: WmlMobileTextWriter) """
        ...

    def UsePostBackCard(self, *args): #cannot find CLR method
        """ UsePostBackCard(self: WmlMobileTextWriter, includeVariables: bool) -> bool """
        ...

    def WmlFormat(self, *args): #cannot find CLR method
        """
        WmlFormat(style: Style, currentFormat: WmlFormat)
        WmlFormat(bold: bool, italic: bool, size: FontSize)
        """
        ...

    def WmlLayout(self, *args): #cannot find CLR method
        """
        WmlLayout(style: Style, currentLayout: WmlLayout)
        WmlLayout(alignment: Alignment, wrapping: Wrapping)
        """
        ...

    def WriteAttribute(self, *__args): # -> 
        """ WriteAttribute(self: WmlMobileTextWriter, attribute: str, value: str, encode: bool) """
        ...

    def WriteBreak(self): # -> 
        """ WriteBreak(self: WmlMobileTextWriter) """
        ...

    def WriteEncodedText(self, text:str): # -> 
        """ WriteEncodedText(self: WmlMobileTextWriter, text: str) """
        ...

    def WriteEncodedUrl(self, url:str): # -> 
        """ WriteEncodedUrl(self: WmlMobileTextWriter, url: str) """
        ...

    def WritePostField(self, name:str, value:str, type:WmlPostFieldType = ...): # -> 
        """ WritePostField(self: WmlMobileTextWriter, name: str, value: str)WritePostField(self: WmlMobileTextWriter, name: str, value: str, type: WmlPostFieldType) """
        ...

    def WritePostFieldVariable(self, name:str, arg:str): # -> 
        """ WritePostFieldVariable(self: WmlMobileTextWriter, name: str, arg: str) """
        ...

    def WriteText(self, text:str, encodeText:bool): # -> 
        """ WriteText(self: WmlMobileTextWriter, text: str, encodeText: bool) """
        ...

    def WriteTextEncodedAttribute(self, *args): #cannot find CLR method
        """ WriteTextEncodedAttribute(self: WmlMobileTextWriter, attribute: str, value: str) """
        ...

    CoreNewLine = ...


class UpWmlMobileTextWriter(WmlMobileTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ UpWmlMobileTextWriter(writer: TextWriter, device: MobileCapabilities, page: MobilePage) """
    CoreNewLine = ...


class WmlControlAdapter(ControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlControlAdapter() """
    @property
    def FormAdapter(self):
        ...

    @property
    def PageAdapter(self):
        ...

    @property
    def SecondaryUIMode(self):
        ...


    def DeterminePostBack(self, *args): #cannot find CLR method
        """ DeterminePostBack(self: WmlControlAdapter, target: str) -> str """
        ...

    def ExitSecondaryUIMode(self, *args): #cannot find CLR method
        """ ExitSecondaryUIMode(self: WmlControlAdapter) """
        ...

    def GetPostBackValue(self, *args): #cannot find CLR method
        """ GetPostBackValue(self: WmlControlAdapter) -> str """
        ...

    def RenderBeginLink(self, *args): #cannot find CLR method
        """ RenderBeginLink(self: WmlControlAdapter, writer: WmlMobileTextWriter, targetUrl: str, softkeyLabel: str, implicitSoftkeyLabel: bool, mapToSoftkey: bool) """
        ...

    def RenderEndLink(self, *args): #cannot find CLR method
        """ RenderEndLink(self: WmlControlAdapter, writer: WmlMobileTextWriter, targetUrl: str, breakAfter: bool) """
        ...

    def RenderLink(self, *args): #cannot find CLR method
        """ RenderLink(self: WmlControlAdapter, writer: WmlMobileTextWriter, targetUrl: str, softkeyLabel: str, implicitSoftkeyLabel: bool, mapToSoftkey: bool, text: str, breakAfter: bool) """
        ...

    def RenderPostBackEvent(self, *args): #cannot find CLR method
        """ RenderPostBackEvent(self: WmlControlAdapter, writer: WmlMobileTextWriter, argument: str, softkeyLabel: str, mapToSoftkey: bool, text: str, breakAfter: bool)RenderPostBackEvent(self: WmlControlAdapter, writer: WmlMobileTextWriter, argument: str, softkeyLabel: str, mapToSoftkey: bool, text: str, breakAfter: bool, postBackType: WmlPostFieldType) """
        ...

    def RenderSubmitEvent(self, *args): #cannot find CLR method
        """ RenderSubmitEvent(self: WmlControlAdapter, writer: WmlMobileTextWriter, softkeyLabel: str, text: str, breakAfter: bool) """
        ...

    NotSecondaryUI: int = ...


class WmlPageAdapter(IPageAdapter, WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlPageAdapter() """
    @staticmethod
    def DeviceQualifies(context:HttpContext) -> bool:
        """ DeviceQualifies(context: HttpContext) -> bool """
        ...

    def IsFormRendered(self, form:Form) -> bool:
        """ IsFormRendered(self: WmlPageAdapter, form: Form) -> bool """
        ...

    def RenderForm(self, *args): #cannot find CLR method
        """ RenderForm(self: WmlPageAdapter, writer: WmlMobileTextWriter, form: Form) """
        ...

    def RendersMultipleForms(self) -> bool:
        """ RendersMultipleForms(self: WmlPageAdapter) -> bool """
        ...


class UpWmlPageAdapter(WmlPageAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'IPageAdapter'>, <type 'object'>
    """ UpWmlPageAdapter() """
    pass

class WmlCalendarAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlCalendarAdapter() """
    pass

class WmlCommandAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlCommandAdapter() """
    pass

class WmlFormAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlFormAdapter() """
    def CalculatePostBackVariables(self) -> IDictionary:
        """ CalculatePostBackVariables(self: WmlFormAdapter) -> IDictionary """
        ...

    def RenderCardTag(self, *args): #cannot find CLR method
        """ RenderCardTag(self: WmlFormAdapter, writer: WmlMobileTextWriter, attributes: IDictionary) """
        ...

    def RenderExtraCardElements(self, *args): #cannot find CLR method
        """ RenderExtraCardElements(self: WmlFormAdapter, writer: WmlMobileTextWriter) """
        ...

    def RenderPager(self, *args): #cannot find CLR method
        """ RenderPager(self: WmlFormAdapter, writer: WmlMobileTextWriter) """
        ...


class WmlImageAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlImageAdapter() """
    pass

class WmlLabelAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlLabelAdapter() """
    pass

class WmlLinkAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlLinkAdapter() """
    pass

class WmlListAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlListAdapter() """
    pass

class WmlLiteralTextAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlLiteralTextAdapter() """
    pass

class WmlObjectListAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlObjectListAdapter() """
    def HasCommands(self, *args): #cannot find CLR method
        """ HasCommands(self: WmlObjectListAdapter) -> bool """
        ...

    def HasDefaultCommand(self, *args): #cannot find CLR method
        """ HasDefaultCommand(self: WmlObjectListAdapter) -> bool """
        ...

    def HasItemDetails(self, *args): #cannot find CLR method
        """ HasItemDetails(self: WmlObjectListAdapter) -> bool """
        ...

    def OnlyHasDefaultCommand(self, *args): #cannot find CLR method
        """ OnlyHasDefaultCommand(self: WmlObjectListAdapter) -> bool """
        ...

    def RenderItemDetails(self, *args): #cannot find CLR method
        """ RenderItemDetails(self: WmlObjectListAdapter, writer: WmlMobileTextWriter, item: ObjectListItem) """
        ...

    def RenderItemMenu(self, *args): #cannot find CLR method
        """ RenderItemMenu(self: WmlObjectListAdapter, writer: WmlMobileTextWriter, item: ObjectListItem) """
        ...

    def RenderItemsList(self, *args): #cannot find CLR method
        """ RenderItemsList(self: WmlObjectListAdapter, writer: WmlMobileTextWriter) """
        ...

    def ShouldRenderAsTable(self, *args): #cannot find CLR method
        """ ShouldRenderAsTable(self: WmlObjectListAdapter) -> bool """
        ...


class WmlPanelAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlPanelAdapter() """
    pass

class WmlPhoneCallAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlPhoneCallAdapter() """
    pass

class WmlPostFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WmlPostFieldType, values: Normal (0), Raw (3), Submit (1), Variable (2) """
    Normal: WmlPostFieldType = ...
    Raw: WmlPostFieldType = ...
    Submit: WmlPostFieldType = ...
    value__ = ...
    Variable: WmlPostFieldType = ...


class WmlSelectionListAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlSelectionListAdapter() """
    pass

class WmlTextBoxAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlTextBoxAdapter() """
    pass

class WmlTextViewAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlTextViewAdapter() """
    pass

class WmlValidationSummaryAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlValidationSummaryAdapter() """
    pass

class WmlValidatorAdapter(WmlControlAdapter): # skipped bases: <type 'IControlAdapter'>, <type 'object'>
    """ WmlValidatorAdapter() """
    pass

# variables with complex values

