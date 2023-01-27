# encoding: utf-8
# module System.Web.UI.MobileControls calls itself MobileControls
# from System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Vbe.Interop import Property

from StdFormat import FirstDayOfWeek

from System import (Array, AsyncCallback, Attribute, Char, DateTime, Enum, 
    EventArgs, IAsyncResult, ICloneable, MulticastDelegate, Type)

from System.Collections import (ArrayList, ICollection, IDictionary, 
    IEnumerator, IList)

from System.Collections.Specialized import NameValueCollection

from System.ComponentModel import ITypeDescriptorContext

from System.Configuration import (ConfigurationConverterBase, 
    ConfigurationElement, ConfigurationElementCollection, 
    ConfigurationSection, IConfigurationSectionHandler)

from System.Drawing import Color

from System.Globalization import CultureInfo

from System.IO import TextWriter

from System.Web import HttpRequest

from System.Web.Mobile import MobileCapabilities

from System.Web.UI import (Control, ControlBuilder, HtmlTextWriter, 
    IAttributeAccessor, INamingContainer, IParserAccessor, 
    IPostBackDataHandler, IPostBackEventHandler, IStateManager, ITemplate, 
    IValidator, Page, StateBag, TemplateBuilder, UserControl)

from System.Web.UI.WebControls import (CalendarSelectionMode, 
    CommandEventArgs, SelectedDatesCollection, ValidationCompareOperator, 
    ValidationDataType, ValidatorDisplay, WebControl)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, IListControl, 
    field#)
"""

# no functions
# classes

class MobileControl(IAttributeAccessor, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> Alignment:
        """
        Get: Alignment(self: MobileControl) -> Alignment
        Set: Alignment(self: MobileControl) = value
        """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: MobileControl) -> Color
        Set: BackColor(self: MobileControl) = value
        """
        ...

    @property
    def BreakAfter(self) -> bool:
        """
        Get: BreakAfter(self: MobileControl) -> bool
        Set: BreakAfter(self: MobileControl) = value
        """
        ...

    @property
    def CustomAttributes(self) -> StateBag:
        """ Get: CustomAttributes(self: MobileControl) -> StateBag """
        ...

    @property
    def DeviceSpecific(self) -> DeviceSpecific:
        """
        Get: DeviceSpecific(self: MobileControl) -> DeviceSpecific
        Set: DeviceSpecific(self: MobileControl) = value
        """
        ...

    @property
    def FirstPage(self) -> int:
        """
        Get: FirstPage(self: MobileControl) -> int
        Set: FirstPage(self: MobileControl) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: MobileControl) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: MobileControl) -> Color
        Set: ForeColor(self: MobileControl) = value
        """
        ...

    @property
    def Form(self) -> Form:
        """ Get: Form(self: MobileControl) -> Form """
        ...

    @property
    def InnerText(self):
        ...

    @property
    def IsTemplated(self) -> bool:
        """ Get: IsTemplated(self: MobileControl) -> bool """
        ...

    @property
    def LastPage(self) -> int:
        """
        Get: LastPage(self: MobileControl) -> int
        Set: LastPage(self: MobileControl) = value
        """
        ...

    @property
    def MobilePage(self) -> MobilePage:
        """ Get: MobilePage(self: MobileControl) -> MobilePage """
        ...

    @property
    def PaginateChildren(self):
        ...

    @property
    def Style(self):
        ...

    @property
    def StyleReference(self) -> str:
        """
        Get: StyleReference(self: MobileControl) -> str
        Set: StyleReference(self: MobileControl) = value
        """
        ...

    @property
    def VisibleWeight(self) -> int:
        """ Get: VisibleWeight(self: MobileControl) -> int """
        ...

    @property
    def Wrapping(self) -> Wrapping:
        """
        Get: Wrapping(self: MobileControl) -> Wrapping
        Set: Wrapping(self: MobileControl) = value
        """
        ...


    def AddLinkedForms(self, linkedForms:IList): # -> 
        """ AddLinkedForms(self: MobileControl, linkedForms: IList) """
        ...

    def CreateDefaultTemplatedUI(self, doDataBind:bool): # -> 
        """ CreateDefaultTemplatedUI(self: MobileControl, doDataBind: bool) """
        ...

    def CreateStyle(self, *args): #cannot find CLR method
        """ CreateStyle(self: MobileControl) -> Style """
        ...

    def CreateTemplatedUI(self, *args): #cannot find CLR method
        """ CreateTemplatedUI(self: MobileControl, doDataBind: bool) """
        ...

    def EnsureTemplatedUI(self): # -> 
        """ EnsureTemplatedUI(self: MobileControl) """
        ...

    def GetTemplate(self, templateName:str) -> ITemplate:
        """ GetTemplate(self: MobileControl, templateName: str) -> ITemplate """
        ...

    def IsFormSubmitControl(self, *args): #cannot find CLR method
        """ IsFormSubmitControl(self: MobileControl) -> bool """
        ...

    def IsVisibleOnPage(self, pageNumber:int) -> bool:
        """ IsVisibleOnPage(self: MobileControl, pageNumber: int) -> bool """
        ...

    def LoadPrivateViewState(self, *args): #cannot find CLR method
        """ LoadPrivateViewState(self: MobileControl, state: object) """
        ...

    def OnPageChange(self, *args): #cannot find CLR method
        """ OnPageChange(self: MobileControl, oldPageIndex: int, newPageIndex: int) """
        ...

    def OnRender(self, *args): #cannot find CLR method
        """ OnRender(self: MobileControl, writer: HtmlTextWriter) """
        ...

    def PaginateRecursive(self, pager:ControlPager): # -> 
        """ PaginateRecursive(self: MobileControl, pager: ControlPager) """
        ...

    def ResolveFormReference(self, formID:str) -> Form:
        """ ResolveFormReference(self: MobileControl, formID: str) -> Form """
        ...

    def SavePrivateViewState(self, *args): #cannot find CLR method
        """ SavePrivateViewState(self: MobileControl) -> object """
        ...


class AdRotator(MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ AdRotator() """
    @property
    def AdvertisementFile(self) -> str:
        """
        Get: AdvertisementFile(self: AdRotator) -> str
        Set: AdvertisementFile(self: AdRotator) = value
        """
        ...

    @property
    def ImageKey(self) -> str:
        """
        Get: ImageKey(self: AdRotator) -> str
        Set: ImageKey(self: AdRotator) = value
        """
        ...

    @property
    def KeywordFilter(self) -> str:
        """
        Get: KeywordFilter(self: AdRotator) -> str
        Set: KeywordFilter(self: AdRotator) = value
        """
        ...

    @property
    def NavigateUrlKey(self) -> str:
        """
        Get: NavigateUrlKey(self: AdRotator) -> str
        Set: NavigateUrlKey(self: AdRotator) = value
        """
        ...


    def CreateWebAdRotator(self, *args): #cannot find CLR method
        """ CreateWebAdRotator(self: AdRotator) -> AdRotator """
        ...

    def OnAdCreated(self, *args): #cannot find CLR method
        """ OnAdCreated(self: AdRotator, e: AdCreatedEventArgs) """
        ...

    AdCreated = ...


class Alignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Alignment, values: Center (2), Left (1), NotSet (0), Right (3) """
    Center: Alignment = ...
    Left: Alignment = ...
    NotSet: Alignment = ...
    Right: Alignment = ...
    value__ = ...


class ArrayListCollectionBase(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ArrayListCollectionBase) -> bool """
        ...

    @property
    def Items(self):
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ArrayListCollectionBase) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class TextControl(MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextControl) -> str
        Set: Text(self: TextControl) = value
        """
        ...



class BaseValidator(TextControl, IValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def ControlToValidate(self) -> str:
        """
        Get: ControlToValidate(self: BaseValidator) -> str
        Set: ControlToValidate(self: BaseValidator) = value
        """
        ...

    @property
    def Display(self) -> ValidatorDisplay:
        """
        Get: Display(self: BaseValidator) -> ValidatorDisplay
        Set: Display(self: BaseValidator) = value
        """
        ...

    @property
    def StyleReference(self) -> str:
        """
        Get: StyleReference(self: BaseValidator) -> str
        Set: StyleReference(self: BaseValidator) = value
        """
        ...

    @property
    def VisibleWeight(self) -> int:
        """ Get: VisibleWeight(self: BaseValidator) -> int """
        ...


    def CheckControlValidationProperty(self, *args): #cannot find CLR method
        """ CheckControlValidationProperty(self: BaseValidator, name: str, propertyName: str) """
        ...

    def ControlPropertiesValid(self, *args): #cannot find CLR method
        """ ControlPropertiesValid(self: BaseValidator) -> bool """
        ...

    def CreateWebValidator(self, *args): #cannot find CLR method
        """ CreateWebValidator(self: BaseValidator) -> BaseValidator """
        ...

    def EvaluateIsValid(self, *args): #cannot find CLR method
        """ EvaluateIsValid(self: BaseValidator) -> bool """
        ...


class BooleanOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BooleanOption, values: False (0), NotSet (-1), True (1) """
    NotSet: BooleanOption = ...
    value__ = ...


class Calendar(IPostBackEventHandler, MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Calendar() """
    @property
    def CalendarEntryText(self) -> str:
        """
        Get: CalendarEntryText(self: Calendar) -> str
        Set: CalendarEntryText(self: Calendar) = value
        """
        ...

    @property
    def FirstDayOfWeek(self) -> FirstDayOfWeek:
        """
        Get: FirstDayOfWeek(self: Calendar) -> FirstDayOfWeek
        Set: FirstDayOfWeek(self: Calendar) = value
        """
        ...

    @property
    def SelectedDate(self) -> DateTime:
        """
        Get: SelectedDate(self: Calendar) -> DateTime
        Set: SelectedDate(self: Calendar) = value
        """
        ...

    @property
    def SelectedDates(self) -> SelectedDatesCollection:
        """ Get: SelectedDates(self: Calendar) -> SelectedDatesCollection """
        ...

    @property
    def SelectionMode(self) -> CalendarSelectionMode:
        """
        Get: SelectionMode(self: Calendar) -> CalendarSelectionMode
        Set: SelectionMode(self: Calendar) = value
        """
        ...

    @property
    def ShowDayHeader(self) -> bool:
        """
        Get: ShowDayHeader(self: Calendar) -> bool
        Set: ShowDayHeader(self: Calendar) = value
        """
        ...

    @property
    def VisibleDate(self) -> DateTime:
        """
        Get: VisibleDate(self: Calendar) -> DateTime
        Set: VisibleDate(self: Calendar) = value
        """
        ...

    @property
    def WebCalendar(self) -> Calendar:
        """ Get: WebCalendar(self: Calendar) -> Calendar """
        ...


    def CreateWebCalendar(self, *args): #cannot find CLR method
        """ CreateWebCalendar(self: Calendar) -> Calendar """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: Calendar) """
        ...

    def RaiseSelectionChangedEvent(self): # -> 
        """ RaiseSelectionChangedEvent(self: Calendar) """
        ...

    SelectionChanged = ...


class Command(IPostBackDataHandler, TextControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Command() """
    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: Command) -> bool
        Set: CausesValidation(self: Command) = value
        """
        ...

    @property
    def CommandArgument(self) -> str:
        """
        Get: CommandArgument(self: Command) -> str
        Set: CommandArgument(self: Command) = value
        """
        ...

    @property
    def CommandName(self) -> str:
        """
        Get: CommandName(self: Command) -> str
        Set: CommandName(self: Command) = value
        """
        ...

    @property
    def Format(self) -> CommandFormat:
        """
        Get: Format(self: Command) -> CommandFormat
        Set: Format(self: Command) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: Command) -> str
        Set: ImageUrl(self: Command) = value
        """
        ...

    @property
    def SoftkeyLabel(self) -> str:
        """
        Get: SoftkeyLabel(self: Command) -> str
        Set: SoftkeyLabel(self: Command) = value
        """
        ...


    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: Command, e: EventArgs) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: Command, e: CommandEventArgs) """
        ...

    Click = ...
    ItemCommand = ...


class CommandFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CommandFormat, values: Button (0), Link (1) """
    Button: CommandFormat = ...
    Link: CommandFormat = ...
    value__ = ...


class CompareValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IValidator'>, <type 'object'>
    """ CompareValidator() """
    @property
    def ControlToCompare(self) -> str:
        """
        Get: ControlToCompare(self: CompareValidator) -> str
        Set: ControlToCompare(self: CompareValidator) = value
        """
        ...

    @property
    def Operator(self) -> ValidationCompareOperator:
        """
        Get: Operator(self: CompareValidator) -> ValidationCompareOperator
        Set: Operator(self: CompareValidator) = value
        """
        ...

    @property
    def Type(self) -> ValidationDataType:
        """
        Get: Type(self: CompareValidator) -> ValidationDataType
        Set: Type(self: CompareValidator) = value
        """
        ...

    @property
    def ValueToCompare(self) -> str:
        """
        Get: ValueToCompare(self: CompareValidator) -> str
        Set: ValueToCompare(self: CompareValidator) = value
        """
        ...



class Constants: # skipped bases: <type 'object'>, <type 'object'>
    """ Constants() """
    AlternatingItemTemplateTag: str = ...
    ContentTemplateTag: str = ...
    DefaultSessionsStateHistorySize: int = ...
    EventArgumentID: str = ...
    EventSourceID: str = ...
    FooterTemplateTag: str = ...
    FormIDPrefix: str = ...
    HeaderTemplateTag: str = ...
    ItemDetailsTemplateTag: str = ...
    ItemTemplateTag: str = ...
    LabelTemplateTag: str = ...
    OptimumPageWeightParameter: str = ...
    PagePrefix: str = ...
    ScreenCharactersHeightParameter: str = ...
    ScriptTemplateTag: str = ...
    SelectionListSpecialCharacter: Char = ...
    SeparatorTemplateTag: str = ...
    SymbolProtocol: str = ...
    UniqueFilePathSuffixVariable: str = ...
    UniqueFilePathSuffixVariableWithoutEqual: str = ...


class ControlElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ControlElement(name: str, adapter: Type) """
    @property
    def Adapter(self) -> Type:
        """
        Get: Adapter(self: ControlElement) -> Type
        Set: Adapter(self: ControlElement) = value
        """
        ...

    @property
    def Control(self) -> Type:
        """
        Get: Control(self: ControlElement) -> Type
        Set: Control(self: ControlElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ControlElement) -> str
        Set: Name(self: ControlElement) = value
        """
        ...


    def __new__(cls, name:str, adapter:Type) -> Self:
        """ __new__(cls: type, name: str, adapter: Type) """
        ...


class ControlElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ControlElementCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: ControlElementCollection) -> Array[object] """
        ...


    def Add(self, controlElement:ControlElement): # -> 
        """ Add(self: ControlElementCollection, controlElement: ControlElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ControlElementCollection) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: ControlElementCollection, name: str)Remove(self: ControlElementCollection, controlElement: ControlElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ControlElementCollection, index: int) """
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


class ControlPager: # skipped bases: <type 'object'>, <type 'object'>
    """ ControlPager(form: Form, pageWeight: int) """
    @property
    def PageCount(self) -> int:
        """
        Get: PageCount(self: ControlPager) -> int
        Set: PageCount(self: ControlPager) = value
        """
        ...

    @property
    def PageWeight(self) -> int:
        """ Get: PageWeight(self: ControlPager) -> int """
        ...

    @property
    def RemainingWeight(self) -> int:
        """
        Get: RemainingWeight(self: ControlPager) -> int
        Set: RemainingWeight(self: ControlPager) = value
        """
        ...


    def GetItemPager(self, control:MobileControl, itemCount:int, itemsPerPage:int, itemWeight:int) -> ItemPager:
        """ GetItemPager(self: ControlPager, control: MobileControl, itemCount: int, itemsPerPage: int, itemWeight: int) -> ItemPager """
        ...

    def GetPage(self, weight:int) -> int:
        """ GetPage(self: ControlPager, weight: int) -> int """
        ...

    DefaultWeight: int = ...
    UseDefaultWeight: int = ...


class CustomValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IValidator'>, <type 'object'>
    """ CustomValidator() """
    def OnServerValidate(self, *args): #cannot find CLR method
        """ OnServerValidate(self: CustomValidator, value: str) -> bool """
        ...

    ServerValidate = ...


class DesignerAdapterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DesignerAdapterAttribute(adapterType: Type)
    DesignerAdapterAttribute(adapterTypeName: str)
    """
    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: DesignerAdapterAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, adapterTypeName: str)
        __new__(cls: type, adapterType: Type)
        """
        ...


class DeviceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    DeviceElement(name: str, inheritsFrom: str)
    DeviceElement(name: str, predicateClass: Type, predicateMethod: str, pageAdapter: Type)
    DeviceElement(name: str, inheritsFrom: str, predicateClass: Type, predicateMethod: str, pageAdapter: Type)
    """
    @property
    def Controls(self) -> ControlElementCollection:
        """ Get: Controls(self: DeviceElement) -> ControlElementCollection """
        ...

    @property
    def InheritsFrom(self) -> str:
        """
        Get: InheritsFrom(self: DeviceElement) -> str
        Set: InheritsFrom(self: DeviceElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DeviceElement) -> str
        Set: Name(self: DeviceElement) = value
        """
        ...

    @property
    def PageAdapter(self) -> Type:
        """
        Get: PageAdapter(self: DeviceElement) -> Type
        Set: PageAdapter(self: DeviceElement) = value
        """
        ...

    @property
    def PredicateClass(self) -> Type:
        """
        Get: PredicateClass(self: DeviceElement) -> Type
        Set: PredicateClass(self: DeviceElement) = value
        """
        ...

    @property
    def PredicateMethod(self) -> str:
        """
        Get: PredicateMethod(self: DeviceElement) -> str
        Set: PredicateMethod(self: DeviceElement) = value
        """
        ...


    def __new__(cls, name:str, *__args:str) -> Self:
        """
        __new__(cls: type, name: str, inheritsFrom: str)
        __new__(cls: type, name: str, predicateClass: Type, predicateMethod: str, pageAdapter: Type)
        __new__(cls: type, name: str, inheritsFrom: str, predicateClass: Type, predicateMethod: str, pageAdapter: Type)
        """
        ...


class DeviceElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DeviceElementCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: DeviceElementCollection) -> Array[object] """
        ...


    def Add(self, deviceElement:DeviceElement): # -> 
        """ Add(self: DeviceElementCollection, deviceElement: DeviceElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DeviceElementCollection) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: DeviceElementCollection, name: str)Remove(self: DeviceElementCollection, deviceElement: DeviceElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DeviceElementCollection, index: int) """
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


class DeviceOverridableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DeviceOverridableAttribute()
    DeviceOverridableAttribute(overridable: bool)
    """
    @property
    def Overridable(self) -> bool:
        """ Get: Overridable(self: DeviceOverridableAttribute) -> bool """
        ...


    def __new__(cls, overridable:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, overridable: bool)
        """
        ...


class DeviceSpecific(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DeviceSpecific() """
    @property
    def Choices(self) -> DeviceSpecificChoiceCollection:
        """ Get: Choices(self: DeviceSpecific) -> DeviceSpecificChoiceCollection """
        ...

    @property
    def HasTemplates(self) -> bool:
        """ Get: HasTemplates(self: DeviceSpecific) -> bool """
        ...

    @property
    def MobilePage(self) -> MobilePage:
        """ Get: MobilePage(self: DeviceSpecific) -> MobilePage """
        ...

    @property
    def Owner(self) -> object:
        """ Get: Owner(self: DeviceSpecific) -> object """
        ...

    @property
    def SelectedChoice(self) -> DeviceSpecificChoice:
        """ Get: SelectedChoice(self: DeviceSpecific) -> DeviceSpecificChoice """
        ...


    def GetTemplate(self, templateName:str) -> ITemplate:
        """ GetTemplate(self: DeviceSpecific, templateName: str) -> ITemplate """
        ...

    DataBinding = ...
    Disposed = ...
    Init = ...
    Load = ...
    PreRender = ...
    Unload = ...


class DeviceSpecificChoice(IAttributeAccessor, IParserAccessor): # skipped bases: <type 'object'>
    """ DeviceSpecificChoice() """
    @property
    def Argument(self) -> str:
        """
        Get: Argument(self: DeviceSpecificChoice) -> str
        Set: Argument(self: DeviceSpecificChoice) = value
        """
        ...

    @property
    def Contents(self) -> IDictionary:
        """ Get: Contents(self: DeviceSpecificChoice) -> IDictionary """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: DeviceSpecificChoice) -> str
        Set: Filter(self: DeviceSpecificChoice) = value
        """
        ...

    @property
    def HasTemplates(self) -> bool:
        """ Get: HasTemplates(self: DeviceSpecificChoice) -> bool """
        ...

    @property
    def Templates(self) -> IDictionary:
        """ Get: Templates(self: DeviceSpecificChoice) -> IDictionary """
        ...

    @property
    def Xmlns(self) -> str:
        """
        Get: Xmlns(self: DeviceSpecificChoice) -> str
        Set: Xmlns(self: DeviceSpecificChoice) = value
        """
        ...



class DeviceSpecificChoiceCollection(ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def All(self) -> ArrayList:
        """ Get: All(self: DeviceSpecificChoiceCollection) -> ArrayList """
        ...


    def Add(self, choice:DeviceSpecificChoice): # -> 
        """ Add(self: DeviceSpecificChoiceCollection, choice: DeviceSpecificChoice) """
        ...

    def AddAt(self, index:int, choice:DeviceSpecificChoice): # -> 
        """ AddAt(self: DeviceSpecificChoiceCollection, index: int, choice: DeviceSpecificChoice) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DeviceSpecificChoiceCollection) """
        ...

    def Remove(self, choice:DeviceSpecificChoice): # -> 
        """ Remove(self: DeviceSpecificChoiceCollection, choice: DeviceSpecificChoice) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DeviceSpecificChoiceCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DeviceSpecificChoiceControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ DeviceSpecificChoiceControlBuilder() """
    pass

class DeviceSpecificChoiceTemplateBuilder(TemplateBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ DeviceSpecificChoiceTemplateBuilder() """
    def AppendLiteralString(self, text:str): # -> 
        """ AppendLiteralString(self: DeviceSpecificChoiceTemplateBuilder, text: str) """
        ...

    def AppendSubBuilder(self, subBuilder:ControlBuilder): # -> 
        """ AppendSubBuilder(self: DeviceSpecificChoiceTemplateBuilder, subBuilder: ControlBuilder) """
        ...


class DeviceSpecificChoiceTemplateContainer: # skipped bases: <type 'object'>, <type 'object'>
    """ DeviceSpecificChoiceTemplateContainer() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: DeviceSpecificChoiceTemplateContainer) -> str
        Set: Name(self: DeviceSpecificChoiceTemplateContainer) = value
        """
        ...

    @property
    def Template(self) -> ITemplate:
        """
        Get: Template(self: DeviceSpecificChoiceTemplateContainer) -> ITemplate
        Set: Template(self: DeviceSpecificChoiceTemplateContainer) = value
        """
        ...



class DeviceSpecificControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ DeviceSpecificControlBuilder() """
    pass

class MobilePage(Page): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IFilterResolutionService'>, <type 'IHttpHandler'>, <type 'object'>
    """ MobilePage() """
    @property
    def AbsoluteFilePath(self) -> str:
        """ Get: AbsoluteFilePath(self: MobilePage) -> str """
        ...

    @property
    def ActiveForm(self) -> Form:
        """
        Get: ActiveForm(self: MobilePage) -> Form
        Set: ActiveForm(self: MobilePage) = value
        """
        ...

    @property
    def AllowCustomAttributes(self) -> bool:
        """
        Get: AllowCustomAttributes(self: MobilePage) -> bool
        Set: AllowCustomAttributes(self: MobilePage) = value
        """
        ...

    @property
    def ClientViewState(self) -> str:
        """ Get: ClientViewState(self: MobilePage) -> str """
        ...

    @property
    def Device(self) -> MobileCapabilities:
        """ Get: Device(self: MobilePage) -> MobileCapabilities """
        ...

    @property
    def EnableTheming(self) -> bool:
        """
        Get: EnableTheming(self: MobilePage) -> bool
        Set: EnableTheming(self: MobilePage) = value
        """
        ...

    @property
    def Forms(self) -> IList:
        """ Get: Forms(self: MobilePage) -> IList """
        ...

    @property
    def HiddenVariables(self) -> IDictionary:
        """ Get: HiddenVariables(self: MobilePage) -> IDictionary """
        ...

    @property
    def QueryStringText(self) -> str:
        """ Get: QueryStringText(self: MobilePage) -> str """
        ...

    @property
    def RelativeFilePath(self) -> str:
        """ Get: RelativeFilePath(self: MobilePage) -> str """
        ...

    @property
    def StyleSheet(self) -> StyleSheet:
        """
        Get: StyleSheet(self: MobilePage) -> StyleSheet
        Set: StyleSheet(self: MobilePage) = value
        """
        ...


    def GetControlAdapter(self, control:MobileControl) -> IControlAdapter:
        """ GetControlAdapter(self: MobilePage, control: MobileControl) -> IControlAdapter """
        ...

    def GetForm(self, id:str) -> Form:
        """ GetForm(self: MobilePage, id: str) -> Form """
        ...

    def GetPrivateViewState(self, ctl:MobileControl) -> object:
        """ GetPrivateViewState(self: MobilePage, ctl: MobileControl) -> object """
        ...

    def HasHiddenVariables(self) -> bool:
        """ HasHiddenVariables(self: MobilePage) -> bool """
        ...

    def MakePathAbsolute(self, virtualPath:str) -> str:
        """ MakePathAbsolute(self: MobilePage, virtualPath: str) -> str """
        ...

    def OnDeviceCustomize(self, *args): #cannot find CLR method
        """ OnDeviceCustomize(self: MobilePage, e: EventArgs) """
        ...

    def OnViewStateExpire(self, *args): #cannot find CLR method
        """ OnViewStateExpire(self: MobilePage, e: EventArgs) """
        ...

    def RedirectToMobilePage(self, url:str, endResponse:bool = ...): # -> 
        """ RedirectToMobilePage(self: MobilePage, url: str)RedirectToMobilePage(self: MobilePage, url: str, endResponse: bool) """
        ...

    HiddenPostEventArgumentId: str = ...
    HiddenPostEventSourceId: str = ...
    HiddenVariablePrefix: str = ...
    PageClientViewStateKey: str = ...
    ViewStateID: str = ...


class ErrorFormatterPage(MobilePage): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IFilterResolutionService'>, <type 'IHttpHandler'>, <type 'object'>
    """ ErrorFormatterPage() """
    @property
    def ErrorInfo(self):
        ...


    def InitContent(self, *args): #cannot find CLR method
        """ InitContent(self: ErrorFormatterPage) """
        ...


class FontInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Bold(self) -> BooleanOption:
        """
        Get: Bold(self: FontInfo) -> BooleanOption
        Set: Bold(self: FontInfo) = value
        """
        ...

    @property
    def Italic(self) -> BooleanOption:
        """
        Get: Italic(self: FontInfo) -> BooleanOption
        Set: Italic(self: FontInfo) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: FontInfo) -> str
        Set: Name(self: FontInfo) = value
        """
        ...

    @property
    def Size(self) -> FontSize:
        """
        Get: Size(self: FontInfo) -> FontSize
        Set: Size(self: FontInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: FontInfo) -> str """
        ...


class FontSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FontSize, values: Large (3), Normal (1), NotSet (0), Small (2) """
    Large: FontSize = ...
    Normal: FontSize = ...
    NotSet: FontSize = ...
    Small: FontSize = ...
    value__ = ...


class ITemplateable: # skipped bases: <type 'object'>
    """ no doc """
    pass

class Panel(ITemplateable, MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Panel() """
    @property
    def Content(self) -> Panel:
        """ Get: Content(self: Panel) -> Panel """
        ...

    @property
    def Paginate(self) -> bool:
        """
        Get: Paginate(self: Panel) -> bool
        Set: Paginate(self: Panel) = value
        """
        ...



class Form(Panel, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITemplateable'>, <type 'object'>
    """ Form() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: Form) -> str
        Set: Action(self: Form) = value
        """
        ...

    @property
    def ControlToPaginate(self) -> Control:
        """
        Get: ControlToPaginate(self: Form) -> Control
        Set: ControlToPaginate(self: Form) = value
        """
        ...

    @property
    def CurrentPage(self) -> int:
        """
        Get: CurrentPage(self: Form) -> int
        Set: CurrentPage(self: Form) = value
        """
        ...

    @property
    def Footer(self) -> Panel:
        """ Get: Footer(self: Form) -> Panel """
        ...

    @property
    def Header(self) -> Panel:
        """ Get: Header(self: Form) -> Panel """
        ...

    @property
    def Method(self) -> FormMethod:
        """
        Get: Method(self: Form) -> FormMethod
        Set: Method(self: Form) = value
        """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: Form) -> int """
        ...

    @property
    def PagerStyle(self) -> PagerStyle:
        """ Get: PagerStyle(self: Form) -> PagerStyle """
        ...

    @property
    def Script(self) -> Panel:
        """ Get: Script(self: Form) -> Panel """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Form) -> str
        Set: Title(self: Form) = value
        """
        ...


    def GetLinkedForms(self, optimumPageWeight:int) -> IList:
        """ GetLinkedForms(self: Form, optimumPageWeight: int) -> IList """
        ...

    def HasActivateHandler(self) -> bool:
        """ HasActivateHandler(self: Form) -> bool """
        ...

    def HasDeactivateHandler(self) -> bool:
        """ HasDeactivateHandler(self: Form) -> bool """
        ...

    def OnActivate(self, *args): #cannot find CLR method
        """ OnActivate(self: Form, e: EventArgs) """
        ...

    def OnDeactivate(self, *args): #cannot find CLR method
        """ OnDeactivate(self: Form, e: EventArgs) """
        ...

    def OnPaginated(self, *args): #cannot find CLR method
        """ OnPaginated(self: Form, e: EventArgs) """
        ...

    Activate = ...
    Deactivate = ...
    Paginated = ...


class MobileControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ MobileControlBuilder() """
    pass

class LiteralTextContainerControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ no doc """
    def AppendLiteralString(self, text:str): # -> 
        """ AppendLiteralString(self: LiteralTextContainerControlBuilder, text: str) """
        ...

    def AppendSubBuilder(self, subBuilder:ControlBuilder): # -> 
        """ AppendSubBuilder(self: LiteralTextContainerControlBuilder, subBuilder: ControlBuilder) """
        ...


class FormControlBuilder(LiteralTextContainerControlBuilder): # skipped bases: <type 'object'>
    """ FormControlBuilder() """
    pass

class FormMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormMethod, values: Get (0), Post (1) """
    Get: FormMethod = ...
    Post: FormMethod = ...
    value__ = ...


class IControlAdapter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Control(self) -> MobileControl:
        """
        Get: Control(self: IControlAdapter) -> MobileControl
        Set: Control(self: IControlAdapter) = value
        """
        ...

    @property
    def ItemWeight(self) -> int:
        """ Get: ItemWeight(self: IControlAdapter) -> int """
        ...

    @property
    def Page(self) -> MobilePage:
        """ Get: Page(self: IControlAdapter) -> MobilePage """
        ...

    @property
    def VisibleWeight(self) -> int:
        """ Get: VisibleWeight(self: IControlAdapter) -> int """
        ...


    def CreateTemplatedUI(self, doDataBind:bool): # -> 
        """ CreateTemplatedUI(self: IControlAdapter, doDataBind: bool) """
        ...

    def HandlePostBackEvent(self, eventArgument:str) -> bool:
        """ HandlePostBackEvent(self: IControlAdapter, eventArgument: str) -> bool """
        ...

    def LoadAdapterState(self, state:object): # -> 
        """ LoadAdapterState(self: IControlAdapter, state: object) """
        ...

    def LoadPostData(self, postDataKey, postCollection, controlPrivateData, dataChanged) -> Tuple_[bool, bool]:
        """ LoadPostData(self: IControlAdapter, postDataKey: str, postCollection: NameValueCollection, controlPrivateData: object) -> (bool, bool) """
        ...

    def OnInit(self, e:EventArgs): # -> 
        """ OnInit(self: IControlAdapter, e: EventArgs) """
        ...

    def OnLoad(self, e:EventArgs): # -> 
        """ OnLoad(self: IControlAdapter, e: EventArgs) """
        ...

    def OnPreRender(self, e:EventArgs): # -> 
        """ OnPreRender(self: IControlAdapter, e: EventArgs) """
        ...

    def OnUnload(self, e:EventArgs): # -> 
        """ OnUnload(self: IControlAdapter, e: EventArgs) """
        ...

    def Render(self, writer:HtmlTextWriter): # -> 
        """ Render(self: IControlAdapter, writer: HtmlTextWriter) """
        ...

    def SaveAdapterState(self) -> object:
        """ SaveAdapterState(self: IControlAdapter) -> object """
        ...


class Image(IPostBackEventHandler, MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Image() """
    @property
    def AlternateText(self) -> str:
        """
        Get: AlternateText(self: Image) -> str
        Set: AlternateText(self: Image) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: Image) -> str
        Set: ImageUrl(self: Image) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: Image) -> str
        Set: NavigateUrl(self: Image) = value
        """
        ...

    @property
    def SoftkeyLabel(self) -> str:
        """
        Get: SoftkeyLabel(self: Image) -> str
        Set: SoftkeyLabel(self: Image) = value
        """
        ...



class IObjectListFieldCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetAll(self) -> Array:
        """ GetAll(self: IObjectListFieldCollection) -> Array[ObjectListField] """
        ...

    def IndexOf(self, *__args:ObjectListField) -> int:
        """
        IndexOf(self: IObjectListFieldCollection, field: ObjectListField) -> int
        IndexOf(self: IObjectListFieldCollection, fieldIDOrTitle: str) -> int
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IPageAdapter(IControlAdapter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CacheVaryByHeaders(self) -> IList:
        """ Get: CacheVaryByHeaders(self: IPageAdapter) -> IList """
        ...

    @property
    def CookielessDataDictionary(self) -> IDictionary:
        """
        Get: CookielessDataDictionary(self: IPageAdapter) -> IDictionary
        Set: CookielessDataDictionary(self: IPageAdapter) = value
        """
        ...

    @property
    def OptimumPageWeight(self) -> int:
        """ Get: OptimumPageWeight(self: IPageAdapter) -> int """
        ...

    @property
    def PersistCookielessData(self) -> bool:
        """
        Get: PersistCookielessData(self: IPageAdapter) -> bool
        Set: PersistCookielessData(self: IPageAdapter) = value
        """
        ...


    def CreateTextWriter(self, writer:TextWriter) -> HtmlTextWriter:
        """ CreateTextWriter(self: IPageAdapter, writer: TextWriter) -> HtmlTextWriter """
        ...

    def DeterminePostBackMode(self, request:HttpRequest, postEventSourceID:str, postEventArgumentID:str, baseCollection:NameValueCollection) -> NameValueCollection:
        """ DeterminePostBackMode(self: IPageAdapter, request: HttpRequest, postEventSourceID: str, postEventArgumentID: str, baseCollection: NameValueCollection) -> NameValueCollection """
        ...

    def HandleError(self, e:Exception, writer:HtmlTextWriter) -> bool:
        """ HandleError(self: IPageAdapter, e: Exception, writer: HtmlTextWriter) -> bool """
        ...

    def HandlePagePostBackEvent(self, eventSource:str, eventArgument:str) -> bool:
        """ HandlePagePostBackEvent(self: IPageAdapter, eventSource: str, eventArgument: str) -> bool """
        ...


class ItemPager: # skipped bases: <type 'object'>, <type 'object'>
    """
    ItemPager()
    ItemPager(pager: ControlPager, control: MobileControl, itemCount: int, itemsPerPage: int, itemWeight: int)
    """
    @property
    def ItemCount(self) -> int:
        """ Get: ItemCount(self: ItemPager) -> int """
        ...

    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: ItemPager) -> int """
        ...



class Label(TextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Label() """
    pass

class Link(TextControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Link() """
    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: Link) -> str
        Set: NavigateUrl(self: Link) = value
        """
        ...

    @property
    def SoftkeyLabel(self) -> str:
        """
        Get: SoftkeyLabel(self: Link) -> str
        Set: SoftkeyLabel(self: Link) = value
        """
        ...


    def AddLinkedForms(self, linkedForms:IList): # -> 
        """ AddLinkedForms(self: Link, linkedForms: IList) """
        ...


class PagedControl(MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def FirstVisibleItemIndex(self) -> int:
        """ Get: FirstVisibleItemIndex(self: PagedControl) -> int """
        ...

    @property
    def InternalItemCount(self):
        ...

    @property
    def ItemCount(self) -> int:
        """
        Get: ItemCount(self: PagedControl) -> int
        Set: ItemCount(self: PagedControl) = value
        """
        ...

    @property
    def ItemsPerPage(self) -> int:
        """
        Get: ItemsPerPage(self: PagedControl) -> int
        Set: ItemsPerPage(self: PagedControl) = value
        """
        ...

    @property
    def ItemWeight(self):
        ...

    @property
    def VisibleItemCount(self) -> int:
        """ Get: VisibleItemCount(self: PagedControl) -> int """
        ...


    def OnLoadItems(self, *args): #cannot find CLR method
        """ OnLoadItems(self: PagedControl, e: LoadItemsEventArgs) """
        ...

    LoadItems = ...


class List(IListControl, PagedControl, INamingContainer, IPostBackEventHandler, ITemplateable): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ List() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: List) -> str
        Set: DataMember(self: List) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: List) -> object
        Set: DataSource(self: List) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: List) -> str
        Set: DataTextField(self: List) = value
        """
        ...

    @property
    def DataValueField(self) -> str:
        """
        Get: DataValueField(self: List) -> str
        Set: DataValueField(self: List) = value
        """
        ...

    @property
    def Decoration(self) -> ListDecoration:
        """
        Get: Decoration(self: List) -> ListDecoration
        Set: Decoration(self: List) = value
        """
        ...

    @property
    def HasItemCommandHandler(self) -> bool:
        """ Get: HasItemCommandHandler(self: List) -> bool """
        ...

    @property
    def Items(self) -> MobileListItemCollection:
        """ Get: Items(self: List) -> MobileListItemCollection """
        ...

    @property
    def ItemsAsLinks(self) -> bool:
        """
        Get: ItemsAsLinks(self: List) -> bool
        Set: ItemsAsLinks(self: List) = value
        """
        ...


    def CreateDefaultTemplatedUI(self, doDataBind:bool): # -> 
        """ CreateDefaultTemplatedUI(self: List, doDataBind: bool) """
        ...

    def CreateItems(self, *args): #cannot find CLR method
        """ CreateItems(self: List, dataSource: IEnumerable) """
        ...

    def EnsureTemplatedUI(self): # -> 
        """ EnsureTemplatedUI(self: List) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: List, e: ListCommandEventArgs) """
        ...

    def OnItemDataBind(self, *args): #cannot find CLR method
        """ OnItemDataBind(self: List, e: ListDataBindEventArgs) """
        ...

    ItemCommand = ...
    ItemDataBind = ...


class ListCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """
    ListCommandEventArgs(item: MobileListItem, commandSource: object, originalArgs: CommandEventArgs)
    ListCommandEventArgs(item: MobileListItem, commandSource: object)
    """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: ListCommandEventArgs) -> object """
        ...

    @property
    def ListItem(self) -> MobileListItem:
        """ Get: ListItem(self: ListCommandEventArgs) -> MobileListItem """
        ...


    DefaultCommand: str = ...


class ListCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ListCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ListCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ListCommandEventHandler, sender: object, e: ListCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ListCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ListCommandEventArgs): # -> 
        """ Invoke(self: ListCommandEventHandler, sender: object, e: ListCommandEventArgs) """
        ...


class ListControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ ListControlBuilder() """
    pass

class ListDataBindEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ListDataBindEventArgs(item: MobileListItem, dataItem: object) """
    @property
    def DataItem(self) -> object:
        """ Get: DataItem(self: ListDataBindEventArgs) -> object """
        ...

    @property
    def ListItem(self) -> MobileListItem:
        """ Get: ListItem(self: ListDataBindEventArgs) -> MobileListItem """
        ...


    def __new__(cls, item:MobileListItem, dataItem:object) -> Self:
        """ __new__(cls: type, item: MobileListItem, dataItem: object) """
        ...


class ListDataBindEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ListDataBindEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ListDataBindEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ListDataBindEventHandler, sender: object, e: ListDataBindEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ListDataBindEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ListDataBindEventArgs): # -> 
        """ Invoke(self: ListDataBindEventHandler, sender: object, e: ListDataBindEventArgs) """
        ...


class ListDecoration(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListDecoration, values: Bulleted (1), None (0), Numbered (2) """
    Bulleted: ListDecoration = ...
    Numbered: ListDecoration = ...
    value__ = ...


class ListSelectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListSelectType, values: CheckBox (4), DropDown (0), ListBox (1), MultiSelectListBox (3), Radio (2) """
    CheckBox: ListSelectType = ...
    DropDown: ListSelectType = ...
    ListBox: ListSelectType = ...
    MultiSelectListBox: ListSelectType = ...
    Radio: ListSelectType = ...
    value__ = ...


class LiteralLink(Link): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IPostBackEventHandler'>, <type 'object'>
    """ LiteralLink() """
    pass

class LiteralText(PagedControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ LiteralText() """
    @property
    def PagedText(self) -> str:
        """ Get: PagedText(self: LiteralText) -> str """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: LiteralText) -> str
        Set: Text(self: LiteralText) = value
        """
        ...



class LiteralTextControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ LiteralTextControlBuilder() """
    pass

class LoadItemsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ LoadItemsEventArgs(index: int, count: int) """
    @property
    def ItemCount(self) -> int:
        """ Get: ItemCount(self: LoadItemsEventArgs) -> int """
        ...

    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: LoadItemsEventArgs) -> int """
        ...


    def __new__(cls, index:int, count:int) -> Self:
        """ __new__(cls: type, index: int, count: int) """
        ...


class LoadItemsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LoadItemsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:LoadItemsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: LoadItemsEventHandler, sender: object, e: LoadItemsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: LoadItemsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:LoadItemsEventArgs): # -> 
        """ Invoke(self: LoadItemsEventHandler, sender: object, e: LoadItemsEventArgs) """
        ...


class MobileControlsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ MobileControlsSection() """
    @property
    def AllowCustomAttributes(self) -> bool:
        """
        Get: AllowCustomAttributes(self: MobileControlsSection) -> bool
        Set: AllowCustomAttributes(self: MobileControlsSection) = value
        """
        ...

    @property
    def CookielessDataDictionaryType(self) -> Type:
        """
        Get: CookielessDataDictionaryType(self: MobileControlsSection) -> Type
        Set: CookielessDataDictionaryType(self: MobileControlsSection) = value
        """
        ...

    @property
    def Devices(self) -> DeviceElementCollection:
        """ Get: Devices(self: MobileControlsSection) -> DeviceElementCollection """
        ...

    @property
    def SessionStateHistorySize(self) -> int:
        """
        Get: SessionStateHistorySize(self: MobileControlsSection) -> int
        Set: SessionStateHistorySize(self: MobileControlsSection) = value
        """
        ...



class MobileControlsSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ MobileControlsSectionHandler() """
    pass

class TemplateContainer(Panel, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITemplateable'>, <type 'object'>
    """ TemplateContainer() """
    pass

class MobileListItem(TemplateContainer, IStateManager): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITemplateable'>, <type 'INamingContainer'>, <type 'object'>
    """
    MobileListItem()
    MobileListItem(text: str)
    MobileListItem(text: str, value: str)
    MobileListItem(itemType: MobileListItemType)
    MobileListItem(dataItem: object, text: str, value: str)
    """
    @property
    def DataItem(self) -> object:
        """
        Get: DataItem(self: MobileListItem) -> object
        Set: DataItem(self: MobileListItem) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: MobileListItem) -> int """
        ...

    @property
    def Selected(self) -> bool:
        """
        Get: Selected(self: MobileListItem) -> bool
        Set: Selected(self: MobileListItem) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: MobileListItem) -> str
        Set: Text(self: MobileListItem) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: MobileListItem) -> str
        Set: Value(self: MobileListItem) = value
        """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: MobileListItem, o: object) -> bool """
        ...

    @staticmethod
    def FromString(s:str) -> MobileListItem:
        """ FromString(s: str) -> MobileListItem """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MobileListItem) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MobileListItem) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, value: str)
        __new__(cls: type, itemType: MobileListItemType)
        __new__(cls: type, dataItem: object, text: str, value: str)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class MobileListItemCollection(IStateManager, ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    MobileListItemCollection()
    MobileListItemCollection(items: ArrayList)
    """
    def Add(self, item:MobileListItem): # -> 
        """ Add(self: MobileListItemCollection, item: MobileListItem)Add(self: MobileListItemCollection, item: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MobileListItemCollection) """
        ...

    def Contains(self, item:MobileListItem) -> bool:
        """ Contains(self: MobileListItemCollection, item: MobileListItem) -> bool """
        ...

    def GetAll(self) -> Array:
        """ GetAll(self: MobileListItemCollection) -> Array[MobileListItem] """
        ...

    def IndexOf(self, item:MobileListItem) -> int:
        """ IndexOf(self: MobileListItemCollection, item: MobileListItem) -> int """
        ...

    def Insert(self, index:int, item:str): # -> 
        """ Insert(self: MobileListItemCollection, index: int, item: str)Insert(self: MobileListItemCollection, index: int, item: MobileListItem) """
        ...

    def Remove(self, item:str): # -> 
        """ Remove(self: MobileListItemCollection, item: str)Remove(self: MobileListItemCollection, item: MobileListItem) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: MobileListItemCollection, index: int) """
        ...

    def SetAll(self, value:Array): # -> 
        """ SetAll(self: MobileListItemCollection, value: Array[MobileListItem]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, items:ArrayList = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, items: ArrayList)
        """
        ...


class MobileListItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MobileListItemType, values: FooterItem (2), HeaderItem (0), ListItem (1), SeparatorItem (3) """
    FooterItem: MobileListItemType = ...
    HeaderItem: MobileListItemType = ...
    ListItem: MobileListItemType = ...
    SeparatorItem: MobileListItemType = ...
    value__ = ...


class MobileTypeNameConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ MobileTypeNameConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: MobileTypeNameConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: MobileTypeNameConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, targetType: Type) -> object """
        ...


class MobileUserControl(UserControl): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ MobileUserControl() """
    pass

class ObjectList(PagedControl, INamingContainer, IPostBackEventHandler, ITemplateable): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ObjectList() """
    @property
    def AllFields(self) -> IObjectListFieldCollection:
        """ Get: AllFields(self: ObjectList) -> IObjectListFieldCollection """
        ...

    @property
    def AutoGenerateFields(self) -> bool:
        """
        Get: AutoGenerateFields(self: ObjectList) -> bool
        Set: AutoGenerateFields(self: ObjectList) = value
        """
        ...

    @property
    def BackCommandText(self) -> str:
        """
        Get: BackCommandText(self: ObjectList) -> str
        Set: BackCommandText(self: ObjectList) = value
        """
        ...

    @property
    def Commands(self) -> ObjectListCommandCollection:
        """ Get: Commands(self: ObjectList) -> ObjectListCommandCollection """
        ...

    @property
    def CommandStyle(self) -> Style:
        """
        Get: CommandStyle(self: ObjectList) -> Style
        Set: CommandStyle(self: ObjectList) = value
        """
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: ObjectList) -> str
        Set: DataMember(self: ObjectList) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: ObjectList) -> object
        Set: DataSource(self: ObjectList) = value
        """
        ...

    @property
    def DefaultCommand(self) -> str:
        """
        Get: DefaultCommand(self: ObjectList) -> str
        Set: DefaultCommand(self: ObjectList) = value
        """
        ...

    @property
    def Details(self) -> Panel:
        """ Get: Details(self: ObjectList) -> Panel """
        ...

    @property
    def DetailsCommandText(self) -> str:
        """
        Get: DetailsCommandText(self: ObjectList) -> str
        Set: DetailsCommandText(self: ObjectList) = value
        """
        ...

    @property
    def Fields(self) -> ObjectListFieldCollection:
        """ Get: Fields(self: ObjectList) -> ObjectListFieldCollection """
        ...

    @property
    def HasItemCommandHandler(self) -> bool:
        """ Get: HasItemCommandHandler(self: ObjectList) -> bool """
        ...

    @property
    def Items(self) -> ObjectListItemCollection:
        """ Get: Items(self: ObjectList) -> ObjectListItemCollection """
        ...

    @property
    def LabelField(self) -> str:
        """
        Get: LabelField(self: ObjectList) -> str
        Set: LabelField(self: ObjectList) = value
        """
        ...

    @property
    def LabelFieldIndex(self) -> int:
        """ Get: LabelFieldIndex(self: ObjectList) -> int """
        ...

    @property
    def LabelStyle(self) -> Style:
        """
        Get: LabelStyle(self: ObjectList) -> Style
        Set: LabelStyle(self: ObjectList) = value
        """
        ...

    @property
    def MoreText(self) -> str:
        """
        Get: MoreText(self: ObjectList) -> str
        Set: MoreText(self: ObjectList) = value
        """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: ObjectList) -> int
        Set: SelectedIndex(self: ObjectList) = value
        """
        ...

    @property
    def Selection(self) -> ObjectListItem:
        """ Get: Selection(self: ObjectList) -> ObjectListItem """
        ...

    @property
    def SelectMoreCommand(self) -> str:
        """ Get: SelectMoreCommand() -> str """
        ...

    @property
    def TableFieldIndices(self) -> Array:
        """ Get: TableFieldIndices(self: ObjectList) -> Array[int] """
        ...

    @property
    def TableFields(self) -> str:
        """
        Get: TableFields(self: ObjectList) -> str
        Set: TableFields(self: ObjectList) = value
        """
        ...

    @property
    def ViewMode(self) -> ObjectListViewMode:
        """
        Get: ViewMode(self: ObjectList) -> ObjectListViewMode
        Set: ViewMode(self: ObjectList) = value
        """
        ...


    def CreateAutoGeneratedFields(self, *args): #cannot find CLR method
        """ CreateAutoGeneratedFields(self: ObjectList, dataSource: IEnumerable) """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: ObjectList, dataItem: object) -> ObjectListItem """
        ...

    def CreateItems(self, *args): #cannot find CLR method
        """ CreateItems(self: ObjectList, dataSource: IEnumerable) """
        ...

    def CreateTemplatedItemDetails(self, doDataBind:bool): # -> 
        """ CreateTemplatedItemDetails(self: ObjectList, doDataBind: bool) """
        ...

    def CreateTemplatedItemsList(self, doDataBind:bool): # -> 
        """ CreateTemplatedItemsList(self: ObjectList, doDataBind: bool) """
        ...

    def EnsureTemplatedUI(self): # -> 
        """ EnsureTemplatedUI(self: ObjectList) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: ObjectList, e: ObjectListCommandEventArgs) """
        ...

    def OnItemDataBind(self, *args): #cannot find CLR method
        """ OnItemDataBind(self: ObjectList, e: ObjectListDataBindEventArgs) """
        ...

    def OnItemSelect(self, *args): #cannot find CLR method
        """ OnItemSelect(self: ObjectList, e: ObjectListSelectEventArgs) """
        ...

    def OnShowItemCommands(self, *args): #cannot find CLR method
        """ OnShowItemCommands(self: ObjectList, e: ObjectListShowCommandsEventArgs) """
        ...

    def PreShowItemCommands(self, itemIndex:int): # -> 
        """ PreShowItemCommands(self: ObjectList, itemIndex: int) """
        ...

    def RaiseDefaultItemEvent(self, itemIndex:int): # -> 
        """ RaiseDefaultItemEvent(self: ObjectList, itemIndex: int) """
        ...

    def SelectListItem(self, itemIndex:int, selectMore:bool) -> bool:
        """ SelectListItem(self: ObjectList, itemIndex: int, selectMore: bool) -> bool """
        ...

    ItemCommand = ...
    ItemDataBind = ...
    ItemSelect = ...
    ShowItemCommands = ...


class ObjectListCommand: # skipped bases: <type 'object'>, <type 'object'>
    """
    ObjectListCommand()
    ObjectListCommand(name: str, text: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ObjectListCommand) -> str
        Set: Name(self: ObjectListCommand) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ObjectListCommand) -> str
        Set: Text(self: ObjectListCommand) = value
        """
        ...



class ObjectListCommandCollection(IStateManager, ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, command:ObjectListCommand): # -> 
        """ Add(self: ObjectListCommandCollection, command: ObjectListCommand) """
        ...

    def AddAt(self, index:int, command:ObjectListCommand): # -> 
        """ AddAt(self: ObjectListCommandCollection, index: int, command: ObjectListCommand) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ObjectListCommandCollection) """
        ...

    def IndexOf(self, s:str) -> int:
        """ IndexOf(self: ObjectListCommandCollection, s: str) -> int """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: ObjectListCommandCollection, s: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ObjectListCommandCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ObjectListCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """
    ObjectListCommandEventArgs(item: ObjectListItem, commandSource: object, originalArgs: CommandEventArgs)
    ObjectListCommandEventArgs(item: ObjectListItem, commandName: str)
    """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: ObjectListCommandEventArgs) -> object """
        ...

    @property
    def ListItem(self) -> ObjectListItem:
        """ Get: ListItem(self: ObjectListCommandEventArgs) -> ObjectListItem """
        ...


    DefaultCommand: str = ...


class ObjectListCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectListCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectListCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectListCommandEventHandler, sender: object, e: ObjectListCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectListCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectListCommandEventArgs): # -> 
        """ Invoke(self: ObjectListCommandEventHandler, sender: object, e: ObjectListCommandEventArgs) """
        ...


class ObjectListControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ ObjectListControlBuilder() """
    pass

class ObjectListDataBindEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ObjectListDataBindEventArgs(item: ObjectListItem, dataItem: object) """
    @property
    def DataItem(self) -> object:
        """ Get: DataItem(self: ObjectListDataBindEventArgs) -> object """
        ...

    @property
    def ListItem(self) -> ObjectListItem:
        """ Get: ListItem(self: ObjectListDataBindEventArgs) -> ObjectListItem """
        ...


    def __new__(cls, item:ObjectListItem, dataItem:object) -> Self:
        """ __new__(cls: type, item: ObjectListItem, dataItem: object) """
        ...


class ObjectListDataBindEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectListDataBindEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectListDataBindEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectListDataBindEventHandler, sender: object, e: ObjectListDataBindEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectListDataBindEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectListDataBindEventArgs): # -> 
        """ Invoke(self: ObjectListDataBindEventHandler, sender: object, e: ObjectListDataBindEventArgs) """
        ...


class ObjectListField(IStateManager): # skipped bases: <type 'object'>
    """ ObjectListField() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: ObjectListField) -> str
        Set: DataField(self: ObjectListField) = value
        """
        ...

    @property
    def DataFormatString(self) -> str:
        """
        Get: DataFormatString(self: ObjectListField) -> str
        Set: DataFormatString(self: ObjectListField) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ObjectListField) -> str
        Set: Name(self: ObjectListField) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ObjectListField) -> str
        Set: Title(self: ObjectListField) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: ObjectListField) -> bool
        Set: Visible(self: ObjectListField) = value
        """
        ...


    def DataBindItem(self, fieldIndex:int, item:ObjectListItem): # -> 
        """ DataBindItem(self: ObjectListField, fieldIndex: int, item: ObjectListItem) """
        ...


class ObjectListFieldCollection(IObjectListFieldCollection, IStateManager, ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, field:ObjectListField): # -> 
        """ Add(self: ObjectListFieldCollection, field: ObjectListField) """
        ...

    def AddAt(self, index:int, field:ObjectListField): # -> 
        """ AddAt(self: ObjectListFieldCollection, index: int, field: ObjectListField) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ObjectListFieldCollection) """
        ...

    def Remove(self, field:ObjectListField): # -> 
        """ Remove(self: ObjectListFieldCollection, field: ObjectListField) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ObjectListFieldCollection, index: int) """
        ...

    def SetAll(self, value:Array): # -> 
        """ SetAll(self: ObjectListFieldCollection, value: Array[ObjectListField]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ObjectListItem(MobileListItem): # skipped bases: <type 'ITemplateable'>, <type 'IStateManager'>, <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class ObjectListItemCollection(IStateManager, ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Clear(self): # -> 
        """ Clear(self: ObjectListItemCollection) """
        ...

    def Contains(self, item:ObjectListItem) -> bool:
        """ Contains(self: ObjectListItemCollection, item: ObjectListItem) -> bool """
        ...

    def GetAll(self) -> Array:
        """ GetAll(self: ObjectListItemCollection) -> Array[ObjectListItem] """
        ...

    def IndexOf(self, item:ObjectListItem) -> int:
        """ IndexOf(self: ObjectListItemCollection, item: ObjectListItem) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ObjectListSelectEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ObjectListSelectEventArgs(item: ObjectListItem, selectMore: bool) """
    @property
    def ListItem(self) -> ObjectListItem:
        """ Get: ListItem(self: ObjectListSelectEventArgs) -> ObjectListItem """
        ...

    @property
    def SelectMore(self) -> bool:
        """ Get: SelectMore(self: ObjectListSelectEventArgs) -> bool """
        ...

    @property
    def UseDefaultHandling(self) -> bool:
        """
        Get: UseDefaultHandling(self: ObjectListSelectEventArgs) -> bool
        Set: UseDefaultHandling(self: ObjectListSelectEventArgs) = value
        """
        ...


    def __new__(cls, item:ObjectListItem, selectMore:bool) -> Self:
        """ __new__(cls: type, item: ObjectListItem, selectMore: bool) """
        ...


class ObjectListSelectEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectListSelectEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectListSelectEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectListSelectEventHandler, sender: object, e: ObjectListSelectEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectListSelectEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectListSelectEventArgs): # -> 
        """ Invoke(self: ObjectListSelectEventHandler, sender: object, e: ObjectListSelectEventArgs) """
        ...


class ObjectListShowCommandsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ObjectListShowCommandsEventArgs(item: ObjectListItem, commands: ObjectListCommandCollection) """
    @property
    def Commands(self) -> ObjectListCommandCollection:
        """ Get: Commands(self: ObjectListShowCommandsEventArgs) -> ObjectListCommandCollection """
        ...

    @property
    def ListItem(self) -> ObjectListItem:
        """ Get: ListItem(self: ObjectListShowCommandsEventArgs) -> ObjectListItem """
        ...


    def __new__(cls, item:ObjectListItem, commands:ObjectListCommandCollection) -> Self:
        """ __new__(cls: type, item: ObjectListItem, commands: ObjectListCommandCollection) """
        ...


class ObjectListShowCommandsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectListShowCommandsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectListShowCommandsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectListShowCommandsEventHandler, sender: object, e: ObjectListShowCommandsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectListShowCommandsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectListShowCommandsEventArgs): # -> 
        """ Invoke(self: ObjectListShowCommandsEventHandler, sender: object, e: ObjectListShowCommandsEventArgs) """
        ...


class ObjectListTitleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ObjectListTitleAttribute(title: str) """
    @property
    def Title(self) -> str:
        """ Get: Title(self: ObjectListTitleAttribute) -> str """
        ...


    def __new__(cls, title:str) -> Self:
        """ __new__(cls: type, title: str) """
        ...


class ObjectListViewMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ObjectListViewMode, values: Commands (1), Details (2), List (0) """
    Commands: ObjectListViewMode = ...
    Details: ObjectListViewMode = ...
    List: ObjectListViewMode = ...
    value__ = ...


class Style(ITemplateable, ICloneable, IStateManager, IParserAccessor): # skipped bases: <type 'object'>
    """ Style() """
    @property
    def Alignment(self) -> Alignment:
        """
        Get: Alignment(self: Style) -> Alignment
        Set: Alignment(self: Style) = value
        """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: Style) -> Color
        Set: BackColor(self: Style) = value
        """
        ...

    @property
    def Control(self) -> MobileControl:
        """ Get: Control(self: Style) -> MobileControl """
        ...

    @property
    def DeviceSpecific(self) -> DeviceSpecific:
        """
        Get: DeviceSpecific(self: Style) -> DeviceSpecific
        Set: DeviceSpecific(self: Style) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: Style) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: Style) -> Color
        Set: ForeColor(self: Style) = value
        """
        ...

    @property
    def IsTemplated(self) -> bool:
        """ Get: IsTemplated(self: Style) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Style) -> str
        Set: Name(self: Style) = value
        """
        ...

    @property
    def State(self):
        ...

    @property
    def StyleReference(self) -> str:
        """
        Get: StyleReference(self: Style) -> str
        Set: StyleReference(self: Style) = value
        """
        ...

    @property
    def Wrapping(self) -> Wrapping:
        """
        Get: Wrapping(self: Style) -> Wrapping
        Set: Wrapping(self: Style) = value
        """
        ...


    def ApplyTo(self, control:WebControl): # -> 
        """ ApplyTo(self: Style, control: WebControl) """
        ...

    def GetTemplate(self, templateName:str) -> ITemplate:
        """ GetTemplate(self: Style, templateName: str) -> ITemplate """
        ...

    @staticmethod
    def RegisterStyle(name:str, type:Type, defaultValue:object, inherit:bool) -> object:
        """ RegisterStyle(name: str, type: Type, defaultValue: object, inherit: bool) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    AlignmentKey: Property = ...
    BackColorKey: Property = ...
    BoldKey: Property = ...
    FontNameKey: Property = ...
    FontSizeKey: Property = ...
    ForeColorKey: Property = ...
    ItalicKey: Property = ...
    WrappingKey: Property = ...


class PagerStyle(Style): # skipped bases: <type 'ITemplateable'>, <type 'IStateManager'>, <type 'ICloneable'>, <type 'IParserAccessor'>, <type 'object'>
    """ PagerStyle() """
    @property
    def NextPageText(self) -> str:
        """
        Get: NextPageText(self: PagerStyle) -> str
        Set: NextPageText(self: PagerStyle) = value
        """
        ...

    @property
    def PageLabel(self) -> str:
        """
        Get: PageLabel(self: PagerStyle) -> str
        Set: PageLabel(self: PagerStyle) = value
        """
        ...

    @property
    def PreviousPageText(self) -> str:
        """
        Get: PreviousPageText(self: PagerStyle) -> str
        Set: PreviousPageText(self: PagerStyle) = value
        """
        ...


    def GetNextPageText(self, currentPageIndex:int) -> str:
        """ GetNextPageText(self: PagerStyle, currentPageIndex: int) -> str """
        ...

    def GetPageLabelText(self, currentPageIndex:int, pageCount:int) -> str:
        """ GetPageLabelText(self: PagerStyle, currentPageIndex: int, pageCount: int) -> str """
        ...

    def GetPreviousPageText(self, currentPageIndex:int) -> str:
        """ GetPreviousPageText(self: PagerStyle, currentPageIndex: int) -> str """
        ...

    NextPageTextKey: Property = ...
    PageLabelKey: Property = ...
    PreviousPageTextKey: Property = ...


class PanelControlBuilder(LiteralTextContainerControlBuilder): # skipped bases: <type 'object'>
    """ PanelControlBuilder() """
    pass

class PersistNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PersistNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: PersistNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...

    Default: PersistNameAttribute = ...


class PhoneCall(TextControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ PhoneCall() """
    @property
    def AlternateFormat(self) -> str:
        """
        Get: AlternateFormat(self: PhoneCall) -> str
        Set: AlternateFormat(self: PhoneCall) = value
        """
        ...

    @property
    def AlternateUrl(self) -> str:
        """
        Get: AlternateUrl(self: PhoneCall) -> str
        Set: AlternateUrl(self: PhoneCall) = value
        """
        ...

    @property
    def PhoneNumber(self) -> str:
        """
        Get: PhoneNumber(self: PhoneCall) -> str
        Set: PhoneNumber(self: PhoneCall) = value
        """
        ...

    @property
    def SoftkeyLabel(self) -> str:
        """
        Get: SoftkeyLabel(self: PhoneCall) -> str
        Set: SoftkeyLabel(self: PhoneCall) = value
        """
        ...


    def AddLinkedForms(self, linkedForms:IList): # -> 
        """ AddLinkedForms(self: PhoneCall, linkedForms: IList) """
        ...


class RangeValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IValidator'>, <type 'object'>
    """ RangeValidator() """
    @property
    def MaximumValue(self) -> str:
        """
        Get: MaximumValue(self: RangeValidator) -> str
        Set: MaximumValue(self: RangeValidator) = value
        """
        ...

    @property
    def MinimumValue(self) -> str:
        """
        Get: MinimumValue(self: RangeValidator) -> str
        Set: MinimumValue(self: RangeValidator) = value
        """
        ...

    @property
    def Type(self) -> ValidationDataType:
        """
        Get: Type(self: RangeValidator) -> ValidationDataType
        Set: Type(self: RangeValidator) = value
        """
        ...



class RegularExpressionValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IValidator'>, <type 'object'>
    """ RegularExpressionValidator() """
    @property
    def ValidationExpression(self) -> str:
        """
        Get: ValidationExpression(self: RegularExpressionValidator) -> str
        Set: ValidationExpression(self: RegularExpressionValidator) = value
        """
        ...



class RequiredFieldValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IValidator'>, <type 'object'>
    """ RequiredFieldValidator() """
    @property
    def InitialValue(self) -> str:
        """
        Get: InitialValue(self: RequiredFieldValidator) -> str
        Set: InitialValue(self: RequiredFieldValidator) = value
        """
        ...



class SelectionList(IPostBackDataHandler, IListControl, MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ SelectionList() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: SelectionList) -> str
        Set: DataMember(self: SelectionList) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: SelectionList) -> object
        Set: DataSource(self: SelectionList) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: SelectionList) -> str
        Set: DataTextField(self: SelectionList) = value
        """
        ...

    @property
    def DataValueField(self) -> str:
        """
        Get: DataValueField(self: SelectionList) -> str
        Set: DataValueField(self: SelectionList) = value
        """
        ...

    @property
    def IsMultiSelect(self) -> bool:
        """ Get: IsMultiSelect(self: SelectionList) -> bool """
        ...

    @property
    def Items(self) -> MobileListItemCollection:
        """ Get: Items(self: SelectionList) -> MobileListItemCollection """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: SelectionList) -> int
        Set: Rows(self: SelectionList) = value
        """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: SelectionList) -> int
        Set: SelectedIndex(self: SelectionList) = value
        """
        ...

    @property
    def Selection(self) -> MobileListItem:
        """ Get: Selection(self: SelectionList) -> MobileListItem """
        ...

    @property
    def SelectType(self) -> ListSelectType:
        """
        Get: SelectType(self: SelectionList) -> ListSelectType
        Set: SelectType(self: SelectionList) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: SelectionList) -> str
        Set: Title(self: SelectionList) = value
        """
        ...


    def CreateItems(self, *args): #cannot find CLR method
        """ CreateItems(self: SelectionList, dataSource: IEnumerable) """
        ...

    def OnItemDataBind(self, *args): #cannot find CLR method
        """ OnItemDataBind(self: SelectionList, e: ListDataBindEventArgs) """
        ...

    def OnSelectedIndexChanged(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanged(self: SelectionList, e: EventArgs) """
        ...

    ItemDataBind = ...
    SelectedIndexChanged = ...


class StyleSheet(MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ StyleSheet() """
    @property
    def Default(self) -> StyleSheet:
        """ Get: Default() -> StyleSheet """
        ...

    @property
    def EnableViewState(self) -> bool:
        """
        Get: EnableViewState(self: StyleSheet) -> bool
        Set: EnableViewState(self: StyleSheet) = value
        """
        ...

    @property
    def ReferencePath(self) -> str:
        """
        Get: ReferencePath(self: StyleSheet) -> str
        Set: ReferencePath(self: StyleSheet) = value
        """
        ...

    @property
    def Styles(self) -> ICollection:
        """ Get: Styles(self: StyleSheet) -> ICollection """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: StyleSheet) -> bool
        Set: Visible(self: StyleSheet) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: StyleSheet) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: StyleSheet, name: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...



class StyleSheetControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ StyleSheetControlBuilder() """
    pass

class TextBox(IPostBackDataHandler, TextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TextBox() """
    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: TextBox) -> int
        Set: MaxLength(self: TextBox) = value
        """
        ...

    @property
    def Numeric(self) -> bool:
        """
        Get: Numeric(self: TextBox) -> bool
        Set: Numeric(self: TextBox) = value
        """
        ...

    @property
    def Password(self) -> bool:
        """
        Get: Password(self: TextBox) -> bool
        Set: Password(self: TextBox) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: TextBox) -> int
        Set: Size(self: TextBox) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: TextBox) -> str
        Set: Title(self: TextBox) = value
        """
        ...


    def OnTextChanged(self, *args): #cannot find CLR method
        """ OnTextChanged(self: TextBox, e: EventArgs) """
        ...

    TextChanged = ...


class TextBoxControlBuilder(MobileControlBuilder): # skipped bases: <type 'object'>
    """ TextBoxControlBuilder() """
    pass

class TextView(PagedControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TextView() """
    @property
    def FirstVisibleElementIndex(self) -> int:
        """ Get: FirstVisibleElementIndex(self: TextView) -> int """
        ...

    @property
    def FirstVisibleElementOffset(self) -> int:
        """ Get: FirstVisibleElementOffset(self: TextView) -> int """
        ...

    @property
    def LastVisibleElementIndex(self) -> int:
        """ Get: LastVisibleElementIndex(self: TextView) -> int """
        ...

    @property
    def LastVisibleElementOffset(self) -> int:
        """ Get: LastVisibleElementOffset(self: TextView) -> int """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextView) -> str
        Set: Text(self: TextView) = value
        """
        ...


    def GetElement(self, index:int) -> TextViewElement:
        """ GetElement(self: TextView, index: int) -> TextViewElement """
        ...

    LoadItems = ...


class TextViewElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BreakAfter(self) -> bool:
        """ Get: BreakAfter(self: TextViewElement) -> bool """
        ...

    @property
    def IsBold(self) -> bool:
        """ Get: IsBold(self: TextViewElement) -> bool """
        ...

    @property
    def IsItalic(self) -> bool:
        """ Get: IsItalic(self: TextViewElement) -> bool """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: TextViewElement) -> str """
        ...

    @property
    def Url(self) -> str:
        """ Get: Url(self: TextViewElement) -> str """
        ...



class ValidationSummary(MobileControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ValidationSummary() """
    @property
    def BackLabel(self) -> str:
        """
        Get: BackLabel(self: ValidationSummary) -> str
        Set: BackLabel(self: ValidationSummary) = value
        """
        ...

    @property
    def FormToValidate(self) -> str:
        """
        Get: FormToValidate(self: ValidationSummary) -> str
        Set: FormToValidate(self: ValidationSummary) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: ValidationSummary) -> str
        Set: HeaderText(self: ValidationSummary) = value
        """
        ...


    def GetErrorMessages(self) -> Array:
        """ GetErrorMessages(self: ValidationSummary) -> Array[str] """
        ...


class Wrapping(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Wrapping, values: NotSet (0), NoWrap (2), Wrap (1) """
    NotSet: Wrapping = ...
    NoWrap: Wrapping = ...
    value__ = ...
    Wrap: Wrapping = ...


# variables with complex values

