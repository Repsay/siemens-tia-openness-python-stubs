# encoding: utf-8
# module System.Web.UI.WebControls calls itself WebControls
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import Parameter

from Microsoft.Office.Interop.Publisher import Wizard

from Microsoft.Office.Interop.Word import Style

from Microsoft.SqlServer.Management.Smo import ViewCollection

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    ParameterCollection)

from StdFormat import FirstDayOfWeek

from System import (Array, AsyncCallback, Char, DateTime, Enum, EventArgs, 
    IAsyncResult, ICloneable, IEquatable, Int16, MulticastDelegate, Nullable, 
    Type, TypeCode)

from System.Activities.Expressions import Literal

from System.Collections import (CollectionBase, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList)

from System.Collections.Generic import List

from System.Collections.Specialized import (IOrderedDictionary, 
    OrderedDictionary)

from System.ComponentModel import (AttributeCollection, CancelEventArgs, 
    Component, ICustomTypeDescriptor, IListSource, ITypeDescriptorContext, 
    ITypedList, PropertyDescriptor, StringConverter, TypeConverter)

from System.Data import DataTable, DbType, ParameterDirection

from System.Data.Common import DbCommand

from System.Data.EntityClient import EntityConnection

from System.Data.Objects import ObjectContext

from System.DirectoryServices import SortDirection

from System.Drawing import Color, ColorConverter, Image

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Linq import IQueryable

from System.Management.Automation import ListControl

from System.Net.Mail import MailMessage, MailPriority

from System.Reflection import MethodInfo

from System.Security.Principal import IPrincipal

from System.Web import (HttpContext, HttpPostedFile, SiteMapNode, 
    SiteMapProvider)

from System.Web.DynamicData import (IDynamicDataSource, 
    IDynamicValidatorException)

from System.Web.ModelBinding import IValueProvider, ModelStateDictionary

from System.Web.Security import MembershipCreateStatus

from System.Web.UI import (ConflictOptions, Control, ControlBuilder, 
    ControlCollection, CssStyleCollection, DataSourceCacheExpiry, 
    DataSourceControl, DataSourceOperation, DataSourceSelectArguments, 
    DataSourceView, HierarchicalDataSourceControl, HierarchicalDataSourceView, 
    HtmlTextWriter, HtmlTextWriterTag, IAttributeAccessor, 
    IAutoFieldGenerator, ICallbackEventHandler, ICheckBoxControl, 
    IDataItemContainer, IDataKeysControl, IDataSource, 
    IDataSourceViewSchemaAccessor, IEditableTextControl, INamingContainer, 
    IParserAccessor, IPostBackDataHandler, IPostBackEventHandler, 
    IStateManager, ITemplate, ITextControl, IUrlResolutionService, IValidator, 
    PostBackOptions, StateBag, StateManagedCollection, ValidateRequestMode)

from System.Web.UI.MobileControls import BaseValidator, FontInfo, FontSize

from System.Web.UI.WebControls.Expressions import (
    DataSourceExpressionCollection)

from System.Windows.Forms import (BorderStyle, CheckBox, IButtonControl, 
    Label, MenuItem, Orientation, ScrollBars, TreeNode, TreeNodeCollection, 
    View)

from System.Windows.Forms.VisualStyles import HorizontalAlign

from System.Xml import XmlDocument

from System.Xml.XPath import XPathNavigator

from System.Xml.Xsl import XslTransform, XsltArgumentList

from typing import Self

"""The following names are not found in the module: (BoundEvent, BulletStyle, 
    BulletedListDisplayMode, ButtonColumnType, ButtonType, 
    CalendarSelectionMode, CreateUserWizardStep, DataControlCellType, 
    DataControlFieldCell, DataControlRowState, DataGridColumnCollection, 
    DataGridItem, DataGridItemCollection, DataGridPagerStyle, 
    DataKeyCollection, DataListItem, DataListItemCollection, DayNameFormat, 
    DetailsViewMode, DetailsViewRow, DetailsViewRowCollection, FontUnit, 
    FormViewMode, FormViewRow, GridLines, GridViewRow, GridViewRowCollection, 
    HotSpotMode, IBorderPaddingControl, INonBindingContainer, 
    IRenderOuterTableControl, IWizardSideBarListControl, ImageAlign, ListItem, 
    ListItemCollection, ListItemType, ListSelectionMode, LiteralMode, 
    LoginFailureAction, LoginTextLayout, LogoutAction, MailDefinition, 
    MenuItemCollection, MenuItemStyle, MenuItemStyleCollection, 
    MenuRenderingMode, ModelDataSource, ModelDataSourceView, NextPrevFormat, 
    PagerMode, PagerPosition, PagerSettings, ParsingCulture, RepeatDirection, 
    RepeatInfo, RepeatLayout, RepeaterItem, RepeaterItemCollection, 
    RoleGroupCollection, SelectedDatesCollection, SiteMapNodeItemType, 
    SqlDataSourceCommandType, SqlDataSourceMode, StandardValuesCollection, 
    SubMenuStyle, SubMenuStyleCollection, TModel, TableCaptionAlign, 
    TableCell, TableCellCollection, TableHeaderScope, TableItemStyle, 
    TableRowCollection, TableRowSection, TextAlign, TextBoxMode, TitleFormat, 
    TreeNodeSelectAction, TreeViewImageSet, Unit, UnitType, 
    ValidationCompareOperator, ValidationDataType, 
    ValidationSummaryDisplayMode, ValidatorDisplay, VerticalAlign, 
    WizardStepCollection, WizardStepType, field#)
"""

# no functions
# classes

class SqlDataSource(DataSourceControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """
    SqlDataSource()
    SqlDataSource(connectionString: str, selectCommand: str)
    SqlDataSource(providerName: str, connectionString: str, selectCommand: str)
    """
    @property
    def CacheDuration(self) -> int:
        """
        Get: CacheDuration(self: SqlDataSource) -> int
        Set: CacheDuration(self: SqlDataSource) = value
        """
        ...

    @property
    def CacheExpirationPolicy(self) -> DataSourceCacheExpiry:
        """
        Get: CacheExpirationPolicy(self: SqlDataSource) -> DataSourceCacheExpiry
        Set: CacheExpirationPolicy(self: SqlDataSource) = value
        """
        ...

    @property
    def CacheKeyDependency(self) -> str:
        """
        Get: CacheKeyDependency(self: SqlDataSource) -> str
        Set: CacheKeyDependency(self: SqlDataSource) = value
        """
        ...

    @property
    def CancelSelectOnNullParameter(self) -> bool:
        """
        Get: CancelSelectOnNullParameter(self: SqlDataSource) -> bool
        Set: CancelSelectOnNullParameter(self: SqlDataSource) = value
        """
        ...

    @property
    def ConflictDetection(self) -> ConflictOptions:
        """
        Get: ConflictDetection(self: SqlDataSource) -> ConflictOptions
        Set: ConflictDetection(self: SqlDataSource) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlDataSource) -> str
        Set: ConnectionString(self: SqlDataSource) = value
        """
        ...

    @property
    def DataSourceMode(self): # -> SqlDataSourceMode
        """
        Get: DataSourceMode(self: SqlDataSource) -> SqlDataSourceMode
        Set: DataSourceMode(self: SqlDataSource) = value
        """
        ...

    @property
    def DeleteCommand(self) -> str:
        """
        Get: DeleteCommand(self: SqlDataSource) -> str
        Set: DeleteCommand(self: SqlDataSource) = value
        """
        ...

    @property
    def DeleteCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: DeleteCommandType(self: SqlDataSource) -> SqlDataSourceCommandType
        Set: DeleteCommandType(self: SqlDataSource) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: SqlDataSource) -> ParameterCollection """
        ...

    @property
    def EnableCaching(self) -> bool:
        """
        Get: EnableCaching(self: SqlDataSource) -> bool
        Set: EnableCaching(self: SqlDataSource) = value
        """
        ...

    @property
    def FilterExpression(self) -> str:
        """
        Get: FilterExpression(self: SqlDataSource) -> str
        Set: FilterExpression(self: SqlDataSource) = value
        """
        ...

    @property
    def FilterParameters(self) -> ParameterCollection:
        """ Get: FilterParameters(self: SqlDataSource) -> ParameterCollection """
        ...

    @property
    def InsertCommand(self) -> str:
        """
        Get: InsertCommand(self: SqlDataSource) -> str
        Set: InsertCommand(self: SqlDataSource) = value
        """
        ...

    @property
    def InsertCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: InsertCommandType(self: SqlDataSource) -> SqlDataSourceCommandType
        Set: InsertCommandType(self: SqlDataSource) = value
        """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: SqlDataSource) -> ParameterCollection """
        ...

    @property
    def OldValuesParameterFormatString(self) -> str:
        """
        Get: OldValuesParameterFormatString(self: SqlDataSource) -> str
        Set: OldValuesParameterFormatString(self: SqlDataSource) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: SqlDataSource) -> str
        Set: ProviderName(self: SqlDataSource) = value
        """
        ...

    @property
    def SelectCommand(self) -> str:
        """
        Get: SelectCommand(self: SqlDataSource) -> str
        Set: SelectCommand(self: SqlDataSource) = value
        """
        ...

    @property
    def SelectCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: SelectCommandType(self: SqlDataSource) -> SqlDataSourceCommandType
        Set: SelectCommandType(self: SqlDataSource) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: SqlDataSource) -> ParameterCollection """
        ...

    @property
    def SortParameterName(self) -> str:
        """
        Get: SortParameterName(self: SqlDataSource) -> str
        Set: SortParameterName(self: SqlDataSource) = value
        """
        ...

    @property
    def SqlCacheDependency(self) -> str:
        """
        Get: SqlCacheDependency(self: SqlDataSource) -> str
        Set: SqlCacheDependency(self: SqlDataSource) = value
        """
        ...

    @property
    def UpdateCommand(self) -> str:
        """
        Get: UpdateCommand(self: SqlDataSource) -> str
        Set: UpdateCommand(self: SqlDataSource) = value
        """
        ...

    @property
    def UpdateCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: UpdateCommandType(self: SqlDataSource) -> SqlDataSourceCommandType
        Set: UpdateCommandType(self: SqlDataSource) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: SqlDataSource) -> ParameterCollection """
        ...


    def CreateDataSourceView(self, *args): #cannot find CLR method
        """ CreateDataSourceView(self: SqlDataSource, viewName: str) -> SqlDataSourceView """
        ...

    def Delete(self) -> int:
        """ Delete(self: SqlDataSource) -> int """
        ...

    def GetDbProviderFactory(self, *args): #cannot find CLR method
        """ GetDbProviderFactory(self: SqlDataSource) -> DbProviderFactory """
        ...

    def Insert(self) -> int:
        """ Insert(self: SqlDataSource) -> int """
        ...

    def Select(self, arguments:DataSourceSelectArguments) -> IEnumerable:
        """ Select(self: SqlDataSource, arguments: DataSourceSelectArguments) -> IEnumerable """
        ...

    def Update(self) -> int:
        """ Update(self: SqlDataSource) -> int """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionString: str, selectCommand: str)
        __new__(cls: type, providerName: str, connectionString: str, selectCommand: str)
        """
        ...

    Deleted = ...
    Deleting = ...
    Filtering = ...
    Inserted = ...
    Inserting = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class AccessDataSource(SqlDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """
    AccessDataSource()
    AccessDataSource(dataFile: str, selectCommand: str)
    """
    @property
    def DataFile(self) -> str:
        """
        Get: DataFile(self: AccessDataSource) -> str
        Set: DataFile(self: AccessDataSource) = value
        """
        ...



class SqlDataSourceView(DataSourceView, IStateManager): # skipped bases: <type 'object'>
    """ SqlDataSourceView(owner: SqlDataSource, name: str, context: HttpContext) """
    @property
    def CancelSelectOnNullParameter(self) -> bool:
        """
        Get: CancelSelectOnNullParameter(self: SqlDataSourceView) -> bool
        Set: CancelSelectOnNullParameter(self: SqlDataSourceView) = value
        """
        ...

    @property
    def ConflictDetection(self) -> ConflictOptions:
        """
        Get: ConflictDetection(self: SqlDataSourceView) -> ConflictOptions
        Set: ConflictDetection(self: SqlDataSourceView) = value
        """
        ...

    @property
    def DeleteCommand(self) -> str:
        """
        Get: DeleteCommand(self: SqlDataSourceView) -> str
        Set: DeleteCommand(self: SqlDataSourceView) = value
        """
        ...

    @property
    def DeleteCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: DeleteCommandType(self: SqlDataSourceView) -> SqlDataSourceCommandType
        Set: DeleteCommandType(self: SqlDataSourceView) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: SqlDataSourceView) -> ParameterCollection """
        ...

    @property
    def FilterExpression(self) -> str:
        """
        Get: FilterExpression(self: SqlDataSourceView) -> str
        Set: FilterExpression(self: SqlDataSourceView) = value
        """
        ...

    @property
    def FilterParameters(self) -> ParameterCollection:
        """ Get: FilterParameters(self: SqlDataSourceView) -> ParameterCollection """
        ...

    @property
    def InsertCommand(self) -> str:
        """
        Get: InsertCommand(self: SqlDataSourceView) -> str
        Set: InsertCommand(self: SqlDataSourceView) = value
        """
        ...

    @property
    def InsertCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: InsertCommandType(self: SqlDataSourceView) -> SqlDataSourceCommandType
        Set: InsertCommandType(self: SqlDataSourceView) = value
        """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: SqlDataSourceView) -> ParameterCollection """
        ...

    @property
    def OldValuesParameterFormatString(self) -> str:
        """
        Get: OldValuesParameterFormatString(self: SqlDataSourceView) -> str
        Set: OldValuesParameterFormatString(self: SqlDataSourceView) = value
        """
        ...

    @property
    def ParameterPrefix(self):
        ...

    @property
    def SelectCommand(self) -> str:
        """
        Get: SelectCommand(self: SqlDataSourceView) -> str
        Set: SelectCommand(self: SqlDataSourceView) = value
        """
        ...

    @property
    def SelectCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: SelectCommandType(self: SqlDataSourceView) -> SqlDataSourceCommandType
        Set: SelectCommandType(self: SqlDataSourceView) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: SqlDataSourceView) -> ParameterCollection """
        ...

    @property
    def SortParameterName(self) -> str:
        """
        Get: SortParameterName(self: SqlDataSourceView) -> str
        Set: SortParameterName(self: SqlDataSourceView) = value
        """
        ...

    @property
    def UpdateCommand(self) -> str:
        """
        Get: UpdateCommand(self: SqlDataSourceView) -> str
        Set: UpdateCommand(self: SqlDataSourceView) = value
        """
        ...

    @property
    def UpdateCommandType(self): # -> SqlDataSourceCommandType
        """
        Get: UpdateCommandType(self: SqlDataSourceView) -> SqlDataSourceCommandType
        Set: UpdateCommandType(self: SqlDataSourceView) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: SqlDataSourceView) -> ParameterCollection """
        ...


    def OnDeleted(self, *args): #cannot find CLR method
        """ OnDeleted(self: SqlDataSourceView, e: SqlDataSourceStatusEventArgs) """
        ...

    def OnDeleting(self, *args): #cannot find CLR method
        """ OnDeleting(self: SqlDataSourceView, e: SqlDataSourceCommandEventArgs) """
        ...

    def OnFiltering(self, *args): #cannot find CLR method
        """ OnFiltering(self: SqlDataSourceView, e: SqlDataSourceFilteringEventArgs) """
        ...

    def OnInserted(self, *args): #cannot find CLR method
        """ OnInserted(self: SqlDataSourceView, e: SqlDataSourceStatusEventArgs) """
        ...

    def OnInserting(self, *args): #cannot find CLR method
        """ OnInserting(self: SqlDataSourceView, e: SqlDataSourceCommandEventArgs) """
        ...

    def OnSelected(self, *args): #cannot find CLR method
        """ OnSelected(self: SqlDataSourceView, e: SqlDataSourceStatusEventArgs) """
        ...

    def OnSelecting(self, *args): #cannot find CLR method
        """ OnSelecting(self: SqlDataSourceView, e: SqlDataSourceSelectingEventArgs) """
        ...

    def OnUpdated(self, *args): #cannot find CLR method
        """ OnUpdated(self: SqlDataSourceView, e: SqlDataSourceStatusEventArgs) """
        ...

    def OnUpdating(self, *args): #cannot find CLR method
        """ OnUpdating(self: SqlDataSourceView, e: SqlDataSourceCommandEventArgs) """
        ...

    Deleted = ...
    Deleting = ...
    Filtering = ...
    Inserted = ...
    Inserting = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class AccessDataSourceView(SqlDataSourceView): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ AccessDataSourceView(owner: AccessDataSource, name: str, context: HttpContext) """
    pass

class AdCreatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ AdCreatedEventArgs(adProperties: IDictionary) """
    @property
    def AdProperties(self) -> IDictionary:
        """ Get: AdProperties(self: AdCreatedEventArgs) -> IDictionary """
        ...

    @property
    def AlternateText(self) -> str:
        """
        Get: AlternateText(self: AdCreatedEventArgs) -> str
        Set: AlternateText(self: AdCreatedEventArgs) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: AdCreatedEventArgs) -> str
        Set: ImageUrl(self: AdCreatedEventArgs) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: AdCreatedEventArgs) -> str
        Set: NavigateUrl(self: AdCreatedEventArgs) = value
        """
        ...


    def __new__(cls, adProperties:IDictionary) -> Self:
        """ __new__(cls: type, adProperties: IDictionary) """
        ...


class AdCreatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AdCreatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AdCreatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AdCreatedEventHandler, sender: object, e: AdCreatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: AdCreatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AdCreatedEventArgs): # -> 
        """ Invoke(self: AdCreatedEventHandler, sender: object, e: AdCreatedEventArgs) """
        ...


class WebControl(IAttributeAccessor, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ WebControl(tag: HtmlTextWriterTag) """
    @property
    def AccessKey(self) -> str:
        """
        Get: AccessKey(self: WebControl) -> str
        Set: AccessKey(self: WebControl) = value
        """
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: WebControl) -> AttributeCollection """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: WebControl) -> Color
        Set: BackColor(self: WebControl) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: WebControl) -> Color
        Set: BorderColor(self: WebControl) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: WebControl) -> BorderStyle
        Set: BorderStyle(self: WebControl) = value
        """
        ...

    @property
    def BorderWidth(self): # -> Unit
        """
        Get: BorderWidth(self: WebControl) -> Unit
        Set: BorderWidth(self: WebControl) = value
        """
        ...

    @property
    def ControlStyle(self) -> Style:
        """ Get: ControlStyle(self: WebControl) -> Style """
        ...

    @property
    def ControlStyleCreated(self) -> bool:
        """ Get: ControlStyleCreated(self: WebControl) -> bool """
        ...

    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: WebControl) -> str
        Set: CssClass(self: WebControl) = value
        """
        ...

    @property
    def DisabledCssClass(self) -> str:
        """
        Get: DisabledCssClass() -> str
        Set: DisabledCssClass() = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WebControl) -> bool
        Set: Enabled(self: WebControl) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: WebControl) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: WebControl) -> Color
        Set: ForeColor(self: WebControl) = value
        """
        ...

    @property
    def HasAttributes(self) -> bool:
        """ Get: HasAttributes(self: WebControl) -> bool """
        ...

    @property
    def Height(self): # -> Unit
        """
        Get: Height(self: WebControl) -> Unit
        Set: Height(self: WebControl) = value
        """
        ...

    @property
    def IsEnabled(self):
        ...

    @property
    def Style(self) -> CssStyleCollection:
        """ Get: Style(self: WebControl) -> CssStyleCollection """
        ...

    @property
    def SupportsDisabledAttribute(self) -> bool:
        """ Get: SupportsDisabledAttribute(self: WebControl) -> bool """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: WebControl) -> Int16
        Set: TabIndex(self: WebControl) = value
        """
        ...

    @property
    def TagKey(self):
        ...

    @property
    def TagName(self):
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: WebControl) -> str
        Set: ToolTip(self: WebControl) = value
        """
        ...

    @property
    def Width(self): # -> Unit
        """
        Get: Width(self: WebControl) -> Unit
        Set: Width(self: WebControl) = value
        """
        ...


    def AddAttributesToRender(self, *args): #cannot find CLR method
        """ AddAttributesToRender(self: WebControl, writer: HtmlTextWriter) """
        ...

    def ApplyStyle(self, s:Style): # -> 
        """ ApplyStyle(self: WebControl, s: Style) """
        ...

    def CopyBaseAttributes(self, controlSrc:WebControl): # -> 
        """ CopyBaseAttributes(self: WebControl, controlSrc: WebControl) """
        ...

    def CreateControlStyle(self, *args): #cannot find CLR method
        """ CreateControlStyle(self: WebControl) -> Style """
        ...

    def MergeStyle(self, s:Style): # -> 
        """ MergeStyle(self: WebControl, s: Style) """
        ...

    def RenderBeginTag(self, writer:HtmlTextWriter): # -> 
        """ RenderBeginTag(self: WebControl, writer: HtmlTextWriter) """
        ...

    def RenderContents(self, *args): #cannot find CLR method
        """ RenderContents(self: WebControl, writer: HtmlTextWriter) """
        ...

    def RenderEndTag(self, writer:HtmlTextWriter): # -> 
        """ RenderEndTag(self: WebControl, writer: HtmlTextWriter) """
        ...

    def __new__(cls, tag:HtmlTextWriterTag) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, tag: HtmlTextWriterTag)
        __new__(cls: type, tag: str)
        """
        ...



class BaseDataBoundControl(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: BaseDataBoundControl) -> object
        Set: DataSource(self: BaseDataBoundControl) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: BaseDataBoundControl) -> str
        Set: DataSourceID(self: BaseDataBoundControl) = value
        """
        ...

    @property
    def Initialized(self):
        ...

    @property
    def IsBoundUsingDataSourceID(self):
        ...

    @property
    def IsDataBindingAutomatic(self):
        ...

    @property
    def IsUsingModelBinders(self):
        ...

    @property
    def RequiresDataBinding(self):
        ...


    def ConfirmInitState(self, *args): #cannot find CLR method
        """ ConfirmInitState(self: BaseDataBoundControl) """
        ...

    def EnsureDataBound(self, *args): #cannot find CLR method
        """ EnsureDataBound(self: BaseDataBoundControl) """
        ...

    def OnDataBound(self, *args): #cannot find CLR method
        """ OnDataBound(self: BaseDataBoundControl, e: EventArgs) """
        ...

    def OnDataPropertyChanged(self, *args): #cannot find CLR method
        """ OnDataPropertyChanged(self: BaseDataBoundControl) """
        ...

    def OnPagePreLoad(self, *args): #cannot find CLR method
        """ OnPagePreLoad(self: BaseDataBoundControl, sender: object, e: EventArgs) """
        ...

    def PerformSelect(self, *args): #cannot find CLR method
        """ PerformSelect(self: BaseDataBoundControl) """
        ...

    def ValidateDataSource(self, *args): #cannot find CLR method
        """ ValidateDataSource(self: BaseDataBoundControl, dataSource: object) """
        ...

    DataBound = ...


class DataBoundControl(BaseDataBoundControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: DataBoundControl) -> str
        Set: DataMember(self: DataBoundControl) = value
        """
        ...

    @property
    def DataSourceObject(self) -> IDataSource:
        """ Get: DataSourceObject(self: DataBoundControl) -> IDataSource """
        ...

    @property
    def ItemType(self) -> str:
        """
        Get: ItemType(self: DataBoundControl) -> str
        Set: ItemType(self: DataBoundControl) = value
        """
        ...

    @property
    def SelectArguments(self):
        ...

    @property
    def SelectMethod(self) -> str:
        """
        Get: SelectMethod(self: DataBoundControl) -> str
        Set: SelectMethod(self: DataBoundControl) = value
        """
        ...


    def CreateDataSourceSelectArguments(self, *args): #cannot find CLR method
        """ CreateDataSourceSelectArguments(self: DataBoundControl) -> DataSourceSelectArguments """
        ...

    def GetData(self, *args): #cannot find CLR method
        """ GetData(self: DataBoundControl) -> DataSourceView """
        ...

    def GetDataSource(self, *args): #cannot find CLR method
        """ GetDataSource(self: DataBoundControl) -> IDataSource """
        ...

    def MarkAsDataBound(self, *args): #cannot find CLR method
        """ MarkAsDataBound(self: DataBoundControl) """
        ...

    def OnCreatingModelDataSource(self, *args): #cannot find CLR method
        """ OnCreatingModelDataSource(self: DataBoundControl, e: CreatingModelDataSourceEventArgs) """
        ...

    def OnDataSourceViewChanged(self, *args): #cannot find CLR method
        """ OnDataSourceViewChanged(self: DataBoundControl, sender: object, e: EventArgs) """
        ...

    def PerformDataBinding(self, *args): #cannot find CLR method
        """ PerformDataBinding(self: DataBoundControl, data: IEnumerable) """
        ...

    CallingDataMethods = ...
    CreatingModelDataSource = ...


class AdRotator(DataBoundControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ AdRotator() """
    @property
    def AdvertisementFile(self) -> str:
        """
        Get: AdvertisementFile(self: AdRotator) -> str
        Set: AdvertisementFile(self: AdRotator) = value
        """
        ...

    @property
    def AlternateTextField(self) -> str:
        """
        Get: AlternateTextField(self: AdRotator) -> str
        Set: AlternateTextField(self: AdRotator) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: AdRotator) -> FontInfo """
        ...

    @property
    def ImageUrlField(self) -> str:
        """
        Get: ImageUrlField(self: AdRotator) -> str
        Set: ImageUrlField(self: AdRotator) = value
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
    def NavigateUrlField(self) -> str:
        """
        Get: NavigateUrlField(self: AdRotator) -> str
        Set: NavigateUrlField(self: AdRotator) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: AdRotator) -> str
        Set: Target(self: AdRotator) = value
        """
        ...

    @property
    def UniqueID(self) -> str:
        """ Get: UniqueID(self: AdRotator) -> str """
        ...


    def OnAdCreated(self, *args): #cannot find CLR method
        """ OnAdCreated(self: AdRotator, e: AdCreatedEventArgs) """
        ...

    AdCreated = ...


class ControlIDConverter(StringConverter): # skipped bases: <type 'object'>
    """ ControlIDConverter() """
    def FilterControl(self, *args): #cannot find CLR method
        """ FilterControl(self: ControlIDConverter, control: Control) -> bool """
        ...

    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: ControlIDConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: ControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: ControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...


class AssociatedControlConverter(ControlIDConverter): # skipped bases: <type 'object'>
    """ AssociatedControlConverter() """
    pass

class AuthenticateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    AuthenticateEventArgs()
    AuthenticateEventArgs(authenticated: bool)
    """
    @property
    def Authenticated(self) -> bool:
        """
        Get: Authenticated(self: AuthenticateEventArgs) -> bool
        Set: Authenticated(self: AuthenticateEventArgs) = value
        """
        ...


    def __new__(cls, authenticated:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, authenticated: bool)
        """
        ...


class AuthenticateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AuthenticateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AuthenticateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AuthenticateEventHandler, sender: object, e: AuthenticateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: AuthenticateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AuthenticateEventArgs): # -> 
        """ Invoke(self: AuthenticateEventHandler, sender: object, e: AuthenticateEventArgs) """
        ...


class AutoCompleteType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AutoCompleteType, values: BusinessCity (23), BusinessCountryRegion (24), BusinessFax (25), BusinessPhone (26), BusinessState (27), BusinessStreetAddress (28), BusinessUrl (29), BusinessZipCode (30), Cellular (2), Company (3), Department (4), Disabled (1), DisplayName (5), Email (6), Enabled (32), FirstName (7), Gender (8), HomeCity (9), HomeCountryRegion (10), HomeFax (11), Homepage (16), HomePhone (12), HomeState (13), HomeStreetAddress (14), HomeZipCode (15), JobTitle (17), LastName (18), MiddleName (19), None (0), Notes (20), Office (21), Pager (22), Search (31) """
    BusinessCity: AutoCompleteType = ...
    BusinessCountryRegion: AutoCompleteType = ...
    BusinessFax: AutoCompleteType = ...
    BusinessPhone: AutoCompleteType = ...
    BusinessState: AutoCompleteType = ...
    BusinessStreetAddress: AutoCompleteType = ...
    BusinessUrl: AutoCompleteType = ...
    BusinessZipCode: AutoCompleteType = ...
    Cellular: AutoCompleteType = ...
    Company: AutoCompleteType = ...
    Department: AutoCompleteType = ...
    Disabled: AutoCompleteType = ...
    DisplayName: AutoCompleteType = ...
    Email: AutoCompleteType = ...
    Enabled: AutoCompleteType = ...
    FirstName: AutoCompleteType = ...
    Gender: AutoCompleteType = ...
    HomeCity: AutoCompleteType = ...
    HomeCountryRegion: AutoCompleteType = ...
    HomeFax: AutoCompleteType = ...
    Homepage: AutoCompleteType = ...
    HomePhone: AutoCompleteType = ...
    HomeState: AutoCompleteType = ...
    HomeStreetAddress: AutoCompleteType = ...
    HomeZipCode: AutoCompleteType = ...
    JobTitle: AutoCompleteType = ...
    LastName: AutoCompleteType = ...
    MiddleName: AutoCompleteType = ...
    Notes: AutoCompleteType = ...
    Office: AutoCompleteType = ...
    Pager: AutoCompleteType = ...
    Search: AutoCompleteType = ...
    value__ = ...


class AutoFieldsGenerator(IAutoFieldGenerator, IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoGeneratedFieldProperties(self):
        ...

    @property
    def AutoGenerateEnumFields(self) -> Nullable:
        """
        Get: AutoGenerateEnumFields(self: AutoFieldsGenerator) -> Nullable[bool]
        Set: AutoGenerateEnumFields(self: AutoFieldsGenerator) = value
        """
        ...


    def CreateAutoGeneratedFieldFromFieldProperties(self, *args): #cannot find CLR method
        """ CreateAutoGeneratedFieldFromFieldProperties(self: AutoFieldsGenerator, fieldProperties: AutoGeneratedFieldProperties) -> AutoGeneratedField """
        ...

    def CreateAutoGeneratedFields(self, dataItem:object, control:Control) -> List:
        """ CreateAutoGeneratedFields(self: AutoFieldsGenerator, dataItem: object, control: Control) -> List[AutoGeneratedField] """
        ...


class DataControlField(IDataSourceViewSchemaAccessor, IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessibleHeaderText(self) -> str:
        """
        Get: AccessibleHeaderText(self: DataControlField) -> str
        Set: AccessibleHeaderText(self: DataControlField) = value
        """
        ...

    @property
    def Control(self):
        ...

    @property
    def ControlStyle(self) -> Style:
        """ Get: ControlStyle(self: DataControlField) -> Style """
        ...

    @property
    def DesignMode(self):
        ...

    @property
    def FooterStyle(self): # -> TableItemStyle
        """ Get: FooterStyle(self: DataControlField) -> TableItemStyle """
        ...

    @property
    def FooterText(self) -> str:
        """
        Get: FooterText(self: DataControlField) -> str
        Set: FooterText(self: DataControlField) = value
        """
        ...

    @property
    def HeaderImageUrl(self) -> str:
        """
        Get: HeaderImageUrl(self: DataControlField) -> str
        Set: HeaderImageUrl(self: DataControlField) = value
        """
        ...

    @property
    def HeaderStyle(self): # -> TableItemStyle
        """ Get: HeaderStyle(self: DataControlField) -> TableItemStyle """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: DataControlField) -> str
        Set: HeaderText(self: DataControlField) = value
        """
        ...

    @property
    def InsertVisible(self) -> bool:
        """
        Get: InsertVisible(self: DataControlField) -> bool
        Set: InsertVisible(self: DataControlField) = value
        """
        ...

    @property
    def ItemStyle(self): # -> TableItemStyle
        """ Get: ItemStyle(self: DataControlField) -> TableItemStyle """
        ...

    @property
    def ShowHeader(self) -> bool:
        """
        Get: ShowHeader(self: DataControlField) -> bool
        Set: ShowHeader(self: DataControlField) = value
        """
        ...

    @property
    def SortExpression(self) -> str:
        """
        Get: SortExpression(self: DataControlField) -> str
        Set: SortExpression(self: DataControlField) = value
        """
        ...

    @property
    def ValidateRequestMode(self):
        ...

    @property
    def ViewState(self):
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: DataControlField) -> bool
        Set: Visible(self: DataControlField) = value
        """
        ...


    def CloneField(self, *args): #cannot find CLR method
        """ CloneField(self: DataControlField) -> DataControlField """
        ...

    def CopyProperties(self, *args): #cannot find CLR method
        """ CopyProperties(self: DataControlField, newField: DataControlField) """
        ...

    def CreateField(self, *args): #cannot find CLR method
        """ CreateField(self: DataControlField) -> DataControlField """
        ...

    def ExtractValuesFromCell(self, dictionary:IOrderedDictionary, cell, rowState, includeReadOnly:bool): # ->  # Not found arg types: {'cell': 'DataControlFieldCell', 'rowState': 'DataControlRowState'}
        """ ExtractValuesFromCell(self: DataControlField, dictionary: IOrderedDictionary, cell: DataControlFieldCell, rowState: DataControlRowState, includeReadOnly: bool) """
        ...

    def Initialize(self, sortingEnabled:bool, control:Control) -> bool:
        """ Initialize(self: DataControlField, sortingEnabled: bool, control: Control) -> bool """
        ...

    def InitializeCell(self, cell, cellType, rowState, rowIndex:int): # ->  # Not found arg types: {'cellType': 'DataControlCellType', 'cell': 'DataControlFieldCell', 'rowState': 'DataControlRowState'}
        """ InitializeCell(self: DataControlField, cell: DataControlFieldCell, cellType: DataControlCellType, rowState: DataControlRowState, rowIndex: int) """
        ...

    def OnFieldChanged(self, *args): #cannot find CLR method
        """ OnFieldChanged(self: DataControlField) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataControlField) -> str """
        ...

    def ValidateSupportsCallback(self): # -> 
        """ ValidateSupportsCallback(self: DataControlField) """
        ...


class BoundField(DataControlField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ BoundField() """
    @property
    def ApplyFormatInEditMode(self) -> bool:
        """
        Get: ApplyFormatInEditMode(self: BoundField) -> bool
        Set: ApplyFormatInEditMode(self: BoundField) = value
        """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: BoundField) -> bool
        Set: ConvertEmptyStringToNull(self: BoundField) = value
        """
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: BoundField) -> str
        Set: DataField(self: BoundField) = value
        """
        ...

    @property
    def DataFormatString(self) -> str:
        """
        Get: DataFormatString(self: BoundField) -> str
        Set: DataFormatString(self: BoundField) = value
        """
        ...

    @property
    def HtmlEncode(self) -> bool:
        """
        Get: HtmlEncode(self: BoundField) -> bool
        Set: HtmlEncode(self: BoundField) = value
        """
        ...

    @property
    def HtmlEncodeFormatString(self) -> bool:
        """
        Get: HtmlEncodeFormatString(self: BoundField) -> bool
        Set: HtmlEncodeFormatString(self: BoundField) = value
        """
        ...

    @property
    def NullDisplayText(self) -> str:
        """
        Get: NullDisplayText(self: BoundField) -> str
        Set: NullDisplayText(self: BoundField) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: BoundField) -> bool
        Set: ReadOnly(self: BoundField) = value
        """
        ...

    @property
    def SupportsHtmlEncode(self):
        ...


    def FormatDataValue(self, *args): #cannot find CLR method
        """ FormatDataValue(self: BoundField, dataValue: object, encode: bool) -> str """
        ...

    def GetDesignTimeValue(self, *args): #cannot find CLR method
        """ GetDesignTimeValue(self: BoundField) -> object """
        ...

    def GetValue(self, *args): #cannot find CLR method
        """ GetValue(self: BoundField, controlContainer: Control) -> object """
        ...

    def InitializeDataCell(self, *args): #cannot find CLR method
        """ InitializeDataCell(self: BoundField, cell: DataControlFieldCell, rowState: DataControlRowState) """
        ...

    def OnDataBindField(self, *args): #cannot find CLR method
        """ OnDataBindField(self: BoundField, sender: object, e: EventArgs) """
        ...

    ThisExpression: str = ...


class AutoGeneratedField(BoundField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ AutoGeneratedField(dataField: str) """
    @property
    def DataType(self) -> Type:
        """
        Get: DataType(self: AutoGeneratedField) -> Type
        Set: DataType(self: AutoGeneratedField) = value
        """
        ...

    @property
    def InsertVisible(self) -> bool:
        """
        Get: InsertVisible(self: AutoGeneratedField) -> bool
        Set: InsertVisible(self: AutoGeneratedField) = value
        """
        ...


    def __new__(cls, dataField:str) -> Self:
        """ __new__(cls: type, dataField: str) """
        ...


class AutoGeneratedFieldProperties(IStateManager): # skipped bases: <type 'object'>
    """ AutoGeneratedFieldProperties() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: AutoGeneratedFieldProperties) -> str
        Set: DataField(self: AutoGeneratedFieldProperties) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: AutoGeneratedFieldProperties) -> bool
        Set: IsReadOnly(self: AutoGeneratedFieldProperties) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: AutoGeneratedFieldProperties) -> str
        Set: Name(self: AutoGeneratedFieldProperties) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: AutoGeneratedFieldProperties) -> Type
        Set: Type(self: AutoGeneratedFieldProperties) = value
        """
        ...



class Label(WebControl, ITextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Label() """
    @property
    def AssociatedControlID(self) -> str:
        """
        Get: AssociatedControlID(self: Label) -> str
        Set: AssociatedControlID(self: Label) = value
        """
        ...



class BaseValidator(IValidator, Label): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'object'>
    """ no doc """
    @property
    def ControlToValidate(self) -> str:
        """
        Get: ControlToValidate(self: BaseValidator) -> str
        Set: ControlToValidate(self: BaseValidator) = value
        """
        ...

    @property
    def Display(self): # -> ValidatorDisplay
        """
        Get: Display(self: BaseValidator) -> ValidatorDisplay
        Set: Display(self: BaseValidator) = value
        """
        ...

    @property
    def EnableClientScript(self) -> bool:
        """
        Get: EnableClientScript(self: BaseValidator) -> bool
        Set: EnableClientScript(self: BaseValidator) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: BaseValidator) -> bool
        Set: Enabled(self: BaseValidator) = value
        """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: BaseValidator) -> Color
        Set: ForeColor(self: BaseValidator) = value
        """
        ...

    @property
    def IsUnobtrusive(self):
        ...

    @property
    def PropertiesValid(self):
        ...

    @property
    def RenderUplevel(self):
        ...

    @property
    def SetFocusOnError(self) -> bool:
        """
        Get: SetFocusOnError(self: BaseValidator) -> bool
        Set: SetFocusOnError(self: BaseValidator) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: BaseValidator) -> str
        Set: ValidationGroup(self: BaseValidator) = value
        """
        ...


    def CheckControlValidationProperty(self, *args): #cannot find CLR method
        """ CheckControlValidationProperty(self: BaseValidator, name: str, propertyName: str) """
        ...

    def ControlPropertiesValid(self, *args): #cannot find CLR method
        """ ControlPropertiesValid(self: BaseValidator) -> bool """
        ...

    def DetermineRenderUplevel(self, *args): #cannot find CLR method
        """ DetermineRenderUplevel(self: BaseValidator) -> bool """
        ...

    def EvaluateIsValid(self, *args): #cannot find CLR method
        """ EvaluateIsValid(self: BaseValidator) -> bool """
        ...

    def GetControlRenderID(self, *args): #cannot find CLR method
        """ GetControlRenderID(self: BaseValidator, name: str) -> str """
        ...

    def GetControlValidationValue(self, *args): #cannot find CLR method
        """ GetControlValidationValue(self: BaseValidator, name: str) -> str """
        ...

    @staticmethod
    def GetValidationProperty(component:object) -> PropertyDescriptor:
        """ GetValidationProperty(component: object) -> PropertyDescriptor """
        ...

    def RegisterValidatorCommonScript(self, *args): #cannot find CLR method
        """ RegisterValidatorCommonScript(self: BaseValidator) """
        ...

    def RegisterValidatorDeclaration(self, *args): #cannot find CLR method
        """ RegisterValidatorDeclaration(self: BaseValidator) """
        ...


class BaseCompareValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ no doc """
    @property
    def CultureInvariantValues(self) -> bool:
        """
        Get: CultureInvariantValues(self: BaseCompareValidator) -> bool
        Set: CultureInvariantValues(self: BaseCompareValidator) = value
        """
        ...

    @property
    def CutoffYear(self):
        ...

    @property
    def Type(self): # -> ValidationDataType
        """
        Get: Type(self: BaseCompareValidator) -> ValidationDataType
        Set: Type(self: BaseCompareValidator) = value
        """
        ...


    @staticmethod
    def CanConvert(text:str, type, cultureInvariant:bool = ...) -> bool: # Not found arg types: {'type': 'ValidationDataType'}
        """
        CanConvert(text: str, type: ValidationDataType) -> bool
        CanConvert(text: str, type: ValidationDataType, cultureInvariant: bool) -> bool
        """
        ...

    def Compare(self, *args): #cannot find CLR method
        """
        Compare(leftText: str, rightText: str, op: ValidationCompareOperator, type: ValidationDataType) -> bool
        Compare(leftText: str, cultureInvariantLeftText: bool, rightText: str, cultureInvariantRightText: bool, op: ValidationCompareOperator, type: ValidationDataType) -> bool
        """
        ...

    def Convert(self, *args): #cannot find CLR method
        """
        Convert(text: str, type: ValidationDataType) -> (bool, object)
        Convert(text: str, type: ValidationDataType, cultureInvariant: bool) -> (bool, object)
        """
        ...

    def GetDateElementOrder(self, *args): #cannot find CLR method
        """ GetDateElementOrder() -> str """
        ...

    def GetFullYear(self, *args): #cannot find CLR method
        """ GetFullYear(shortYear: int) -> int """
        ...


class BaseDataList(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: BaseDataList) -> str
        Set: Caption(self: BaseDataList) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: BaseDataList) -> TableCaptionAlign
        Set: CaptionAlign(self: BaseDataList) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: BaseDataList) -> int
        Set: CellPadding(self: BaseDataList) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: BaseDataList) -> int
        Set: CellSpacing(self: BaseDataList) = value
        """
        ...

    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: BaseDataList) -> ControlCollection """
        ...

    @property
    def DataKeyField(self) -> str:
        """
        Get: DataKeyField(self: BaseDataList) -> str
        Set: DataKeyField(self: BaseDataList) = value
        """
        ...

    @property
    def DataKeys(self): # -> DataKeyCollection
        """ Get: DataKeys(self: BaseDataList) -> DataKeyCollection """
        ...

    @property
    def DataKeysArray(self):
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: BaseDataList) -> str
        Set: DataMember(self: BaseDataList) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: BaseDataList) -> object
        Set: DataSource(self: BaseDataList) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: BaseDataList) -> str
        Set: DataSourceID(self: BaseDataList) = value
        """
        ...

    @property
    def GridLines(self): # -> GridLines
        """
        Get: GridLines(self: BaseDataList) -> GridLines
        Set: GridLines(self: BaseDataList) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: BaseDataList) -> HorizontalAlign
        Set: HorizontalAlign(self: BaseDataList) = value
        """
        ...

    @property
    def Initialized(self):
        ...

    @property
    def IsBoundUsingDataSourceID(self):
        ...

    @property
    def RequiresDataBinding(self):
        ...

    @property
    def SelectArguments(self):
        ...

    @property
    def UseAccessibleHeader(self) -> bool:
        """
        Get: UseAccessibleHeader(self: BaseDataList) -> bool
        Set: UseAccessibleHeader(self: BaseDataList) = value
        """
        ...


    def CreateControlHierarchy(self, *args): #cannot find CLR method
        """ CreateControlHierarchy(self: BaseDataList, useDataSource: bool) """
        ...

    def CreateDataSourceSelectArguments(self, *args): #cannot find CLR method
        """ CreateDataSourceSelectArguments(self: BaseDataList) -> DataSourceSelectArguments """
        ...

    def EnsureDataBound(self, *args): #cannot find CLR method
        """ EnsureDataBound(self: BaseDataList) """
        ...

    def GetData(self, *args): #cannot find CLR method
        """ GetData(self: BaseDataList) -> IEnumerable """
        ...

    @staticmethod
    def IsBindableType(type:Type) -> bool:
        """ IsBindableType(type: Type) -> bool """
        ...

    def OnDataPropertyChanged(self, *args): #cannot find CLR method
        """ OnDataPropertyChanged(self: BaseDataList) """
        ...

    def OnDataSourceViewChanged(self, *args): #cannot find CLR method
        """ OnDataSourceViewChanged(self: BaseDataList, sender: object, e: EventArgs) """
        ...

    def OnSelectedIndexChanged(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanged(self: BaseDataList, e: EventArgs) """
        ...

    def PrepareControlHierarchy(self, *args): #cannot find CLR method
        """ PrepareControlHierarchy(self: BaseDataList) """
        ...

    SelectedIndexChanged = ...


class BorderStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BorderStyle, values: Dashed (3), Dotted (2), Double (5), Groove (6), Inset (8), None (1), NotSet (0), Outset (9), Ridge (7), Solid (4) """
    Dashed: BorderStyle = ...
    Dotted: BorderStyle = ...
    Double: BorderStyle = ...
    Groove: BorderStyle = ...
    Inset: BorderStyle = ...
    NotSet: BorderStyle = ...
    Outset: BorderStyle = ...
    Ridge: BorderStyle = ...
    Solid: BorderStyle = ...
    value__ = ...


class DataGridColumn(IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DesignMode(self):
        ...

    @property
    def FooterStyle(self): # -> TableItemStyle
        """ Get: FooterStyle(self: DataGridColumn) -> TableItemStyle """
        ...

    @property
    def FooterText(self) -> str:
        """
        Get: FooterText(self: DataGridColumn) -> str
        Set: FooterText(self: DataGridColumn) = value
        """
        ...

    @property
    def HeaderImageUrl(self) -> str:
        """
        Get: HeaderImageUrl(self: DataGridColumn) -> str
        Set: HeaderImageUrl(self: DataGridColumn) = value
        """
        ...

    @property
    def HeaderStyle(self): # -> TableItemStyle
        """ Get: HeaderStyle(self: DataGridColumn) -> TableItemStyle """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: DataGridColumn) -> str
        Set: HeaderText(self: DataGridColumn) = value
        """
        ...

    @property
    def ItemStyle(self): # -> TableItemStyle
        """ Get: ItemStyle(self: DataGridColumn) -> TableItemStyle """
        ...

    @property
    def Owner(self):
        ...

    @property
    def SortExpression(self) -> str:
        """
        Get: SortExpression(self: DataGridColumn) -> str
        Set: SortExpression(self: DataGridColumn) = value
        """
        ...

    @property
    def ViewState(self):
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: DataGridColumn) -> bool
        Set: Visible(self: DataGridColumn) = value
        """
        ...


    def Initialize(self): # -> 
        """ Initialize(self: DataGridColumn) """
        ...

    def InitializeCell(self, cell, columnIndex:int, itemType): # ->  # Not found arg types: {'itemType': 'ListItemType', 'cell': 'TableCell'}
        """ InitializeCell(self: DataGridColumn, cell: TableCell, columnIndex: int, itemType: ListItemType) """
        ...

    def OnColumnChanged(self, *args): #cannot find CLR method
        """ OnColumnChanged(self: DataGridColumn) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataGridColumn) -> str """
        ...


class BoundColumn(DataGridColumn): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ BoundColumn() """
    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: BoundColumn) -> str
        Set: DataField(self: BoundColumn) = value
        """
        ...

    @property
    def DataFormatString(self) -> str:
        """
        Get: DataFormatString(self: BoundColumn) -> str
        Set: DataFormatString(self: BoundColumn) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: BoundColumn) -> bool
        Set: ReadOnly(self: BoundColumn) = value
        """
        ...


    def FormatDataValue(self, *args): #cannot find CLR method
        """ FormatDataValue(self: BoundColumn, dataValue: object) -> str """
        ...

    thisExpr: str = ...


class ListControl(DataBoundControl, IEditableTextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'object'>
    """ ListControl() """
    @property
    def AppendDataBoundItems(self) -> bool:
        """
        Get: AppendDataBoundItems(self: ListControl) -> bool
        Set: AppendDataBoundItems(self: ListControl) = value
        """
        ...

    @property
    def AutoPostBack(self) -> bool:
        """
        Get: AutoPostBack(self: ListControl) -> bool
        Set: AutoPostBack(self: ListControl) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: ListControl) -> bool
        Set: CausesValidation(self: ListControl) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: ListControl) -> str
        Set: DataTextField(self: ListControl) = value
        """
        ...

    @property
    def DataTextFormatString(self) -> str:
        """
        Get: DataTextFormatString(self: ListControl) -> str
        Set: DataTextFormatString(self: ListControl) = value
        """
        ...

    @property
    def DataValueField(self) -> str:
        """
        Get: DataValueField(self: ListControl) -> str
        Set: DataValueField(self: ListControl) = value
        """
        ...

    @property
    def Items(self): # -> ListItemCollection
        """ Get: Items(self: ListControl) -> ListItemCollection """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: ListControl) -> int
        Set: SelectedIndex(self: ListControl) = value
        """
        ...

    @property
    def SelectedItem(self): # -> ListItem
        """ Get: SelectedItem(self: ListControl) -> ListItem """
        ...

    @property
    def SelectedValue(self) -> str:
        """
        Get: SelectedValue(self: ListControl) -> str
        Set: SelectedValue(self: ListControl) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ListControl) -> str
        Set: Text(self: ListControl) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: ListControl) -> str
        Set: ValidationGroup(self: ListControl) = value
        """
        ...


    def ClearSelection(self): # -> 
        """ ClearSelection(self: ListControl) """
        ...

    def OnSelectedIndexChanged(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanged(self: ListControl, e: EventArgs) """
        ...

    def OnTextChanged(self, *args): #cannot find CLR method
        """ OnTextChanged(self: ListControl, e: EventArgs) """
        ...

    def SetPostDataSelection(self, *args): #cannot find CLR method
        """ SetPostDataSelection(self: ListControl, selectedIndex: int) """
        ...

    def VerifyMultiSelect(self, *args): #cannot find CLR method
        """ VerifyMultiSelect(self: ListControl) """
        ...

    SelectedIndexChanged = ...
    TextChanged = ...


class BulletedList(IPostBackEventHandler, ListControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IEditableTextControl'>, <type 'object'>
    """ BulletedList() """
    @property
    def BulletImageUrl(self) -> str:
        """
        Get: BulletImageUrl(self: BulletedList) -> str
        Set: BulletImageUrl(self: BulletedList) = value
        """
        ...

    @property
    def BulletStyle(self): # -> BulletStyle
        """
        Get: BulletStyle(self: BulletedList) -> BulletStyle
        Set: BulletStyle(self: BulletedList) = value
        """
        ...

    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: BulletedList) -> ControlCollection """
        ...

    @property
    def DisplayMode(self): # -> BulletedListDisplayMode
        """
        Get: DisplayMode(self: BulletedList) -> BulletedListDisplayMode
        Set: DisplayMode(self: BulletedList) = value
        """
        ...

    @property
    def FirstBulletNumber(self) -> int:
        """
        Get: FirstBulletNumber(self: BulletedList) -> int
        Set: FirstBulletNumber(self: BulletedList) = value
        """
        ...

    @property
    def RenderWhenDataEmpty(self) -> bool:
        """
        Get: RenderWhenDataEmpty(self: BulletedList) -> bool
        Set: RenderWhenDataEmpty(self: BulletedList) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: BulletedList) -> str
        Set: Target(self: BulletedList) = value
        """
        ...


    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: BulletedList, e: BulletedListEventArgs) """
        ...

    def RenderBulletText(self, *args): #cannot find CLR method
        """ RenderBulletText(self: BulletedList, item: ListItem, index: int, writer: HtmlTextWriter) """
        ...

    Click = ...


class BulletedListDisplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BulletedListDisplayMode, values: HyperLink (1), LinkButton (2), Text (0) """
    HyperLink: BulletedListDisplayMode = ...
    LinkButton: BulletedListDisplayMode = ...
    Text: BulletedListDisplayMode = ...
    value__ = ...


class BulletedListEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ BulletedListEventArgs(index: int) """
    @property
    def Index(self) -> int:
        """ Get: Index(self: BulletedListEventArgs) -> int """
        ...


    def __new__(cls, index:int) -> Self:
        """ __new__(cls: type, index: int) """
        ...


class BulletedListEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BulletedListEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:BulletedListEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BulletedListEventHandler, sender: object, e: BulletedListEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: BulletedListEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:BulletedListEventArgs): # -> 
        """ Invoke(self: BulletedListEventHandler, sender: object, e: BulletedListEventArgs) """
        ...


class BulletStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BulletStyle, values: Circle (7), CustomImage (9), Disc (6), LowerAlpha (2), LowerRoman (4), NotSet (0), Numbered (1), Square (8), UpperAlpha (3), UpperRoman (5) """
    Circle: BulletStyle = ...
    CustomImage: BulletStyle = ...
    Disc: BulletStyle = ...
    LowerAlpha: BulletStyle = ...
    LowerRoman: BulletStyle = ...
    NotSet: BulletStyle = ...
    Numbered: BulletStyle = ...
    Square: BulletStyle = ...
    UpperAlpha: BulletStyle = ...
    UpperRoman: BulletStyle = ...
    value__ = ...


class IButtonControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: IButtonControl) -> bool
        Set: CausesValidation(self: IButtonControl) = value
        """
        ...

    @property
    def CommandArgument(self) -> str:
        """
        Get: CommandArgument(self: IButtonControl) -> str
        Set: CommandArgument(self: IButtonControl) = value
        """
        ...

    @property
    def CommandName(self) -> str:
        """
        Get: CommandName(self: IButtonControl) -> str
        Set: CommandName(self: IButtonControl) = value
        """
        ...

    @property
    def PostBackUrl(self) -> str:
        """
        Get: PostBackUrl(self: IButtonControl) -> str
        Set: PostBackUrl(self: IButtonControl) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IButtonControl) -> str
        Set: Text(self: IButtonControl) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: IButtonControl) -> str
        Set: ValidationGroup(self: IButtonControl) = value
        """
        ...


    Click = ...
    Command = ...


class Button(IButtonControl, WebControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Button() """
    @property
    def OnClientClick(self) -> str:
        """
        Get: OnClientClick(self: Button) -> str
        Set: OnClientClick(self: Button) = value
        """
        ...

    @property
    def UseSubmitBehavior(self) -> bool:
        """
        Get: UseSubmitBehavior(self: Button) -> bool
        Set: UseSubmitBehavior(self: Button) = value
        """
        ...


    def GetPostBackOptions(self, *args): #cannot find CLR method
        """ GetPostBackOptions(self: Button) -> PostBackOptions """
        ...

    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: Button, e: EventArgs) """
        ...

    def OnCommand(self, *args): #cannot find CLR method
        """ OnCommand(self: Button, e: CommandEventArgs) """
        ...

    Click = ...
    Command = ...


class ButtonColumn(DataGridColumn): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ ButtonColumn() """
    @property
    def ButtonType(self): # -> ButtonColumnType
        """
        Get: ButtonType(self: ButtonColumn) -> ButtonColumnType
        Set: ButtonType(self: ButtonColumn) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: ButtonColumn) -> bool
        Set: CausesValidation(self: ButtonColumn) = value
        """
        ...

    @property
    def CommandName(self) -> str:
        """
        Get: CommandName(self: ButtonColumn) -> str
        Set: CommandName(self: ButtonColumn) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: ButtonColumn) -> str
        Set: DataTextField(self: ButtonColumn) = value
        """
        ...

    @property
    def DataTextFormatString(self) -> str:
        """
        Get: DataTextFormatString(self: ButtonColumn) -> str
        Set: DataTextFormatString(self: ButtonColumn) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ButtonColumn) -> str
        Set: Text(self: ButtonColumn) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: ButtonColumn) -> str
        Set: ValidationGroup(self: ButtonColumn) = value
        """
        ...


    def FormatDataTextValue(self, *args): #cannot find CLR method
        """ FormatDataTextValue(self: ButtonColumn, dataTextValue: object) -> str """
        ...


class ButtonColumnType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ButtonColumnType, values: LinkButton (0), PushButton (1) """
    LinkButton: ButtonColumnType = ...
    PushButton: ButtonColumnType = ...
    value__ = ...


class ButtonFieldBase(DataControlField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ no doc """
    @property
    def ButtonType(self): # -> ButtonType
        """
        Get: ButtonType(self: ButtonFieldBase) -> ButtonType
        Set: ButtonType(self: ButtonFieldBase) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: ButtonFieldBase) -> bool
        Set: CausesValidation(self: ButtonFieldBase) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: ButtonFieldBase) -> str
        Set: ValidationGroup(self: ButtonFieldBase) = value
        """
        ...



class ButtonField(ButtonFieldBase): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ ButtonField() """
    @property
    def CommandName(self) -> str:
        """
        Get: CommandName(self: ButtonField) -> str
        Set: CommandName(self: ButtonField) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: ButtonField) -> str
        Set: DataTextField(self: ButtonField) = value
        """
        ...

    @property
    def DataTextFormatString(self) -> str:
        """
        Get: DataTextFormatString(self: ButtonField) -> str
        Set: DataTextFormatString(self: ButtonField) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: ButtonField) -> str
        Set: ImageUrl(self: ButtonField) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ButtonField) -> str
        Set: Text(self: ButtonField) = value
        """
        ...


    def FormatDataTextValue(self, *args): #cannot find CLR method
        """ FormatDataTextValue(self: ButtonField, dataTextValue: object) -> str """
        ...

    def Initialize(self, sortingEnabled:bool, control:Control) -> bool:
        """ Initialize(self: ButtonField, sortingEnabled: bool, control: Control) -> bool """
        ...

    def InitializeCell(self, cell, cellType, rowState, rowIndex:int): # ->  # Not found arg types: {'cellType': 'DataControlCellType', 'cell': 'DataControlFieldCell', 'rowState': 'DataControlRowState'}
        """ InitializeCell(self: ButtonField, cell: DataControlFieldCell, cellType: DataControlCellType, rowState: DataControlRowState, rowIndex: int) """
        ...

    def ValidateSupportsCallback(self): # -> 
        """ ValidateSupportsCallback(self: ButtonField) """
        ...


class ButtonType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ButtonType, values: Button (0), Image (1), Link (2) """
    Button: ButtonType = ...
    Image: ButtonType = ...
    Link: ButtonType = ...
    value__ = ...


class Calendar(WebControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Calendar() """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: Calendar) -> str
        Set: Caption(self: Calendar) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: Calendar) -> TableCaptionAlign
        Set: CaptionAlign(self: Calendar) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: Calendar) -> int
        Set: CellPadding(self: Calendar) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: Calendar) -> int
        Set: CellSpacing(self: Calendar) = value
        """
        ...

    @property
    def DayHeaderStyle(self): # -> TableItemStyle
        """ Get: DayHeaderStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def DayNameFormat(self): # -> DayNameFormat
        """
        Get: DayNameFormat(self: Calendar) -> DayNameFormat
        Set: DayNameFormat(self: Calendar) = value
        """
        ...

    @property
    def DayStyle(self): # -> TableItemStyle
        """ Get: DayStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def FirstDayOfWeek(self) -> FirstDayOfWeek:
        """
        Get: FirstDayOfWeek(self: Calendar) -> FirstDayOfWeek
        Set: FirstDayOfWeek(self: Calendar) = value
        """
        ...

    @property
    def NextMonthText(self) -> str:
        """
        Get: NextMonthText(self: Calendar) -> str
        Set: NextMonthText(self: Calendar) = value
        """
        ...

    @property
    def NextPrevFormat(self): # -> NextPrevFormat
        """
        Get: NextPrevFormat(self: Calendar) -> NextPrevFormat
        Set: NextPrevFormat(self: Calendar) = value
        """
        ...

    @property
    def NextPrevStyle(self): # -> TableItemStyle
        """ Get: NextPrevStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def OtherMonthDayStyle(self): # -> TableItemStyle
        """ Get: OtherMonthDayStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def PrevMonthText(self) -> str:
        """
        Get: PrevMonthText(self: Calendar) -> str
        Set: PrevMonthText(self: Calendar) = value
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
    def SelectedDates(self): # -> SelectedDatesCollection
        """ Get: SelectedDates(self: Calendar) -> SelectedDatesCollection """
        ...

    @property
    def SelectedDayStyle(self): # -> TableItemStyle
        """ Get: SelectedDayStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def SelectionMode(self): # -> CalendarSelectionMode
        """
        Get: SelectionMode(self: Calendar) -> CalendarSelectionMode
        Set: SelectionMode(self: Calendar) = value
        """
        ...

    @property
    def SelectMonthText(self) -> str:
        """
        Get: SelectMonthText(self: Calendar) -> str
        Set: SelectMonthText(self: Calendar) = value
        """
        ...

    @property
    def SelectorStyle(self): # -> TableItemStyle
        """ Get: SelectorStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def SelectWeekText(self) -> str:
        """
        Get: SelectWeekText(self: Calendar) -> str
        Set: SelectWeekText(self: Calendar) = value
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
    def ShowGridLines(self) -> bool:
        """
        Get: ShowGridLines(self: Calendar) -> bool
        Set: ShowGridLines(self: Calendar) = value
        """
        ...

    @property
    def ShowNextPrevMonth(self) -> bool:
        """
        Get: ShowNextPrevMonth(self: Calendar) -> bool
        Set: ShowNextPrevMonth(self: Calendar) = value
        """
        ...

    @property
    def ShowTitle(self) -> bool:
        """
        Get: ShowTitle(self: Calendar) -> bool
        Set: ShowTitle(self: Calendar) = value
        """
        ...

    @property
    def TitleFormat(self): # -> TitleFormat
        """
        Get: TitleFormat(self: Calendar) -> TitleFormat
        Set: TitleFormat(self: Calendar) = value
        """
        ...

    @property
    def TitleStyle(self): # -> TableItemStyle
        """ Get: TitleStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def TodayDayStyle(self): # -> TableItemStyle
        """ Get: TodayDayStyle(self: Calendar) -> TableItemStyle """
        ...

    @property
    def TodaysDate(self) -> DateTime:
        """
        Get: TodaysDate(self: Calendar) -> DateTime
        Set: TodaysDate(self: Calendar) = value
        """
        ...

    @property
    def UseAccessibleHeader(self) -> bool:
        """
        Get: UseAccessibleHeader(self: Calendar) -> bool
        Set: UseAccessibleHeader(self: Calendar) = value
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
    def WeekendDayStyle(self): # -> TableItemStyle
        """ Get: WeekendDayStyle(self: Calendar) -> TableItemStyle """
        ...


    def HasWeekSelectors(self, *args): #cannot find CLR method
        """ HasWeekSelectors(self: Calendar, selectionMode: CalendarSelectionMode) -> bool """
        ...

    def OnDayRender(self, *args): #cannot find CLR method
        """ OnDayRender(self: Calendar, cell: TableCell, day: CalendarDay) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: Calendar) """
        ...

    def OnVisibleMonthChanged(self, *args): #cannot find CLR method
        """ OnVisibleMonthChanged(self: Calendar, newDate: DateTime, previousDate: DateTime) """
        ...

    DayRender = ...
    SelectionChanged = ...
    VisibleMonthChanged = ...


class CalendarDay: # skipped bases: <type 'object'>, <type 'object'>
    """ CalendarDay(date: DateTime, isWeekend: bool, isToday: bool, isSelected: bool, isOtherMonth: bool, dayNumberText: str) """
    @property
    def Date(self) -> DateTime:
        """ Get: Date(self: CalendarDay) -> DateTime """
        ...

    @property
    def DayNumberText(self) -> str:
        """ Get: DayNumberText(self: CalendarDay) -> str """
        ...

    @property
    def IsOtherMonth(self) -> bool:
        """ Get: IsOtherMonth(self: CalendarDay) -> bool """
        ...

    @property
    def IsSelectable(self) -> bool:
        """
        Get: IsSelectable(self: CalendarDay) -> bool
        Set: IsSelectable(self: CalendarDay) = value
        """
        ...

    @property
    def IsSelected(self) -> bool:
        """ Get: IsSelected(self: CalendarDay) -> bool """
        ...

    @property
    def IsToday(self) -> bool:
        """ Get: IsToday(self: CalendarDay) -> bool """
        ...

    @property
    def IsWeekend(self) -> bool:
        """ Get: IsWeekend(self: CalendarDay) -> bool """
        ...



class CalendarSelectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CalendarSelectionMode, values: Day (1), DayWeek (2), DayWeekMonth (3), None (0) """
    Day: CalendarSelectionMode = ...
    DayWeek: CalendarSelectionMode = ...
    DayWeekMonth: CalendarSelectionMode = ...
    value__ = ...


class CallingDataMethodsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CallingDataMethodsEventArgs() """
    @property
    def DataMethodsObject(self) -> object:
        """
        Get: DataMethodsObject(self: CallingDataMethodsEventArgs) -> object
        Set: DataMethodsObject(self: CallingDataMethodsEventArgs) = value
        """
        ...

    @property
    def DataMethodsType(self) -> Type:
        """
        Get: DataMethodsType(self: CallingDataMethodsEventArgs) -> Type
        Set: DataMethodsType(self: CallingDataMethodsEventArgs) = value
        """
        ...



class CallingDataMethodsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CallingDataMethodsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CallingDataMethodsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CallingDataMethodsEventHandler, sender: object, e: CallingDataMethodsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CallingDataMethodsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CallingDataMethodsEventArgs): # -> 
        """ Invoke(self: CallingDataMethodsEventHandler, sender: object, e: CallingDataMethodsEventArgs) """
        ...


class ICompositeControlDesignerAccessor: # skipped bases: <type 'object'>
    """ no doc """
    def RecreateChildControls(self): # -> 
        """ RecreateChildControls(self: ICompositeControlDesignerAccessor) """
        ...


class CompositeControl(WebControl, INamingContainer, ICompositeControlDesignerAccessor): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: CompositeControl) -> ControlCollection """
        ...



class ChangePassword(CompositeControl, IBorderPaddingControl, IRenderOuterTableControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ ChangePassword() """
    @property
    def BorderPadding(self) -> int:
        """
        Get: BorderPadding(self: ChangePassword) -> int
        Set: BorderPadding(self: ChangePassword) = value
        """
        ...

    @property
    def CancelButtonImageUrl(self) -> str:
        """
        Get: CancelButtonImageUrl(self: ChangePassword) -> str
        Set: CancelButtonImageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def CancelButtonStyle(self) -> Style:
        """ Get: CancelButtonStyle(self: ChangePassword) -> Style """
        ...

    @property
    def CancelButtonText(self) -> str:
        """
        Get: CancelButtonText(self: ChangePassword) -> str
        Set: CancelButtonText(self: ChangePassword) = value
        """
        ...

    @property
    def CancelButtonType(self) -> ButtonType:
        """
        Get: CancelButtonType(self: ChangePassword) -> ButtonType
        Set: CancelButtonType(self: ChangePassword) = value
        """
        ...

    @property
    def CancelDestinationPageUrl(self) -> str:
        """
        Get: CancelDestinationPageUrl(self: ChangePassword) -> str
        Set: CancelDestinationPageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordButtonImageUrl(self) -> str:
        """
        Get: ChangePasswordButtonImageUrl(self: ChangePassword) -> str
        Set: ChangePasswordButtonImageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordButtonStyle(self) -> Style:
        """ Get: ChangePasswordButtonStyle(self: ChangePassword) -> Style """
        ...

    @property
    def ChangePasswordButtonText(self) -> str:
        """
        Get: ChangePasswordButtonText(self: ChangePassword) -> str
        Set: ChangePasswordButtonText(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordButtonType(self) -> ButtonType:
        """
        Get: ChangePasswordButtonType(self: ChangePassword) -> ButtonType
        Set: ChangePasswordButtonType(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordFailureText(self) -> str:
        """
        Get: ChangePasswordFailureText(self: ChangePassword) -> str
        Set: ChangePasswordFailureText(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordTemplate(self) -> ITemplate:
        """
        Get: ChangePasswordTemplate(self: ChangePassword) -> ITemplate
        Set: ChangePasswordTemplate(self: ChangePassword) = value
        """
        ...

    @property
    def ChangePasswordTemplateContainer(self) -> Control:
        """ Get: ChangePasswordTemplateContainer(self: ChangePassword) -> Control """
        ...

    @property
    def ChangePasswordTitleText(self) -> str:
        """
        Get: ChangePasswordTitleText(self: ChangePassword) -> str
        Set: ChangePasswordTitleText(self: ChangePassword) = value
        """
        ...

    @property
    def ConfirmNewPassword(self) -> str:
        """ Get: ConfirmNewPassword(self: ChangePassword) -> str """
        ...

    @property
    def ConfirmNewPasswordLabelText(self) -> str:
        """
        Get: ConfirmNewPasswordLabelText(self: ChangePassword) -> str
        Set: ConfirmNewPasswordLabelText(self: ChangePassword) = value
        """
        ...

    @property
    def ConfirmPasswordCompareErrorMessage(self) -> str:
        """
        Get: ConfirmPasswordCompareErrorMessage(self: ChangePassword) -> str
        Set: ConfirmPasswordCompareErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def ConfirmPasswordRequiredErrorMessage(self) -> str:
        """
        Get: ConfirmPasswordRequiredErrorMessage(self: ChangePassword) -> str
        Set: ConfirmPasswordRequiredErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def ContinueButtonImageUrl(self) -> str:
        """
        Get: ContinueButtonImageUrl(self: ChangePassword) -> str
        Set: ContinueButtonImageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def ContinueButtonStyle(self) -> Style:
        """ Get: ContinueButtonStyle(self: ChangePassword) -> Style """
        ...

    @property
    def ContinueButtonText(self) -> str:
        """
        Get: ContinueButtonText(self: ChangePassword) -> str
        Set: ContinueButtonText(self: ChangePassword) = value
        """
        ...

    @property
    def ContinueButtonType(self) -> ButtonType:
        """
        Get: ContinueButtonType(self: ChangePassword) -> ButtonType
        Set: ContinueButtonType(self: ChangePassword) = value
        """
        ...

    @property
    def ContinueDestinationPageUrl(self) -> str:
        """
        Get: ContinueDestinationPageUrl(self: ChangePassword) -> str
        Set: ContinueDestinationPageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def CreateUserIconUrl(self) -> str:
        """
        Get: CreateUserIconUrl(self: ChangePassword) -> str
        Set: CreateUserIconUrl(self: ChangePassword) = value
        """
        ...

    @property
    def CreateUserText(self) -> str:
        """
        Get: CreateUserText(self: ChangePassword) -> str
        Set: CreateUserText(self: ChangePassword) = value
        """
        ...

    @property
    def CreateUserUrl(self) -> str:
        """
        Get: CreateUserUrl(self: ChangePassword) -> str
        Set: CreateUserUrl(self: ChangePassword) = value
        """
        ...

    @property
    def CurrentPassword(self) -> str:
        """ Get: CurrentPassword(self: ChangePassword) -> str """
        ...

    @property
    def DisplayUserName(self) -> bool:
        """
        Get: DisplayUserName(self: ChangePassword) -> bool
        Set: DisplayUserName(self: ChangePassword) = value
        """
        ...

    @property
    def EditProfileIconUrl(self) -> str:
        """
        Get: EditProfileIconUrl(self: ChangePassword) -> str
        Set: EditProfileIconUrl(self: ChangePassword) = value
        """
        ...

    @property
    def EditProfileText(self) -> str:
        """
        Get: EditProfileText(self: ChangePassword) -> str
        Set: EditProfileText(self: ChangePassword) = value
        """
        ...

    @property
    def EditProfileUrl(self) -> str:
        """
        Get: EditProfileUrl(self: ChangePassword) -> str
        Set: EditProfileUrl(self: ChangePassword) = value
        """
        ...

    @property
    def FailureTextStyle(self): # -> TableItemStyle
        """ Get: FailureTextStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def HelpPageIconUrl(self) -> str:
        """
        Get: HelpPageIconUrl(self: ChangePassword) -> str
        Set: HelpPageIconUrl(self: ChangePassword) = value
        """
        ...

    @property
    def HelpPageText(self) -> str:
        """
        Get: HelpPageText(self: ChangePassword) -> str
        Set: HelpPageText(self: ChangePassword) = value
        """
        ...

    @property
    def HelpPageUrl(self) -> str:
        """
        Get: HelpPageUrl(self: ChangePassword) -> str
        Set: HelpPageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def HyperLinkStyle(self): # -> TableItemStyle
        """ Get: HyperLinkStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def InstructionText(self) -> str:
        """
        Get: InstructionText(self: ChangePassword) -> str
        Set: InstructionText(self: ChangePassword) = value
        """
        ...

    @property
    def InstructionTextStyle(self): # -> TableItemStyle
        """ Get: InstructionTextStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def LabelStyle(self): # -> TableItemStyle
        """ Get: LabelStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def MailDefinition(self): # -> MailDefinition
        """ Get: MailDefinition(self: ChangePassword) -> MailDefinition """
        ...

    @property
    def MembershipProvider(self) -> str:
        """
        Get: MembershipProvider(self: ChangePassword) -> str
        Set: MembershipProvider(self: ChangePassword) = value
        """
        ...

    @property
    def NewPassword(self) -> str:
        """ Get: NewPassword(self: ChangePassword) -> str """
        ...

    @property
    def NewPasswordLabelText(self) -> str:
        """
        Get: NewPasswordLabelText(self: ChangePassword) -> str
        Set: NewPasswordLabelText(self: ChangePassword) = value
        """
        ...

    @property
    def NewPasswordRegularExpression(self) -> str:
        """
        Get: NewPasswordRegularExpression(self: ChangePassword) -> str
        Set: NewPasswordRegularExpression(self: ChangePassword) = value
        """
        ...

    @property
    def NewPasswordRegularExpressionErrorMessage(self) -> str:
        """
        Get: NewPasswordRegularExpressionErrorMessage(self: ChangePassword) -> str
        Set: NewPasswordRegularExpressionErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def NewPasswordRequiredErrorMessage(self) -> str:
        """
        Get: NewPasswordRequiredErrorMessage(self: ChangePassword) -> str
        Set: NewPasswordRequiredErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordHintStyle(self): # -> TableItemStyle
        """ Get: PasswordHintStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def PasswordHintText(self) -> str:
        """
        Get: PasswordHintText(self: ChangePassword) -> str
        Set: PasswordHintText(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordLabelText(self) -> str:
        """
        Get: PasswordLabelText(self: ChangePassword) -> str
        Set: PasswordLabelText(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordRecoveryIconUrl(self) -> str:
        """
        Get: PasswordRecoveryIconUrl(self: ChangePassword) -> str
        Set: PasswordRecoveryIconUrl(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordRecoveryText(self) -> str:
        """
        Get: PasswordRecoveryText(self: ChangePassword) -> str
        Set: PasswordRecoveryText(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordRecoveryUrl(self) -> str:
        """
        Get: PasswordRecoveryUrl(self: ChangePassword) -> str
        Set: PasswordRecoveryUrl(self: ChangePassword) = value
        """
        ...

    @property
    def PasswordRequiredErrorMessage(self) -> str:
        """
        Get: PasswordRequiredErrorMessage(self: ChangePassword) -> str
        Set: PasswordRequiredErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: ChangePassword) -> bool
        Set: RenderOuterTable(self: ChangePassword) = value
        """
        ...

    @property
    def SuccessPageUrl(self) -> str:
        """
        Get: SuccessPageUrl(self: ChangePassword) -> str
        Set: SuccessPageUrl(self: ChangePassword) = value
        """
        ...

    @property
    def SuccessTemplate(self) -> ITemplate:
        """
        Get: SuccessTemplate(self: ChangePassword) -> ITemplate
        Set: SuccessTemplate(self: ChangePassword) = value
        """
        ...

    @property
    def SuccessTemplateContainer(self) -> Control:
        """ Get: SuccessTemplateContainer(self: ChangePassword) -> Control """
        ...

    @property
    def SuccessText(self) -> str:
        """
        Get: SuccessText(self: ChangePassword) -> str
        Set: SuccessText(self: ChangePassword) = value
        """
        ...

    @property
    def SuccessTextStyle(self): # -> TableItemStyle
        """ Get: SuccessTextStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def SuccessTitleText(self) -> str:
        """
        Get: SuccessTitleText(self: ChangePassword) -> str
        Set: SuccessTitleText(self: ChangePassword) = value
        """
        ...

    @property
    def TextBoxStyle(self) -> Style:
        """ Get: TextBoxStyle(self: ChangePassword) -> Style """
        ...

    @property
    def TitleTextStyle(self): # -> TableItemStyle
        """ Get: TitleTextStyle(self: ChangePassword) -> TableItemStyle """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: ChangePassword) -> str
        Set: UserName(self: ChangePassword) = value
        """
        ...

    @property
    def UserNameLabelText(self) -> str:
        """
        Get: UserNameLabelText(self: ChangePassword) -> str
        Set: UserNameLabelText(self: ChangePassword) = value
        """
        ...

    @property
    def UserNameRequiredErrorMessage(self) -> str:
        """
        Get: UserNameRequiredErrorMessage(self: ChangePassword) -> str
        Set: UserNameRequiredErrorMessage(self: ChangePassword) = value
        """
        ...

    @property
    def ValidatorTextStyle(self) -> Style:
        """ Get: ValidatorTextStyle(self: ChangePassword) -> Style """
        ...


    def OnCancelButtonClick(self, *args): #cannot find CLR method
        """ OnCancelButtonClick(self: ChangePassword, e: EventArgs) """
        ...

    def OnChangedPassword(self, *args): #cannot find CLR method
        """ OnChangedPassword(self: ChangePassword, e: EventArgs) """
        ...

    def OnChangePasswordError(self, *args): #cannot find CLR method
        """ OnChangePasswordError(self: ChangePassword, e: EventArgs) """
        ...

    def OnChangingPassword(self, *args): #cannot find CLR method
        """ OnChangingPassword(self: ChangePassword, e: LoginCancelEventArgs) """
        ...

    def OnContinueButtonClick(self, *args): #cannot find CLR method
        """ OnContinueButtonClick(self: ChangePassword, e: EventArgs) """
        ...

    def OnSendingMail(self, *args): #cannot find CLR method
        """ OnSendingMail(self: ChangePassword, e: MailMessageEventArgs) """
        ...

    def OnSendMailError(self, *args): #cannot find CLR method
        """ OnSendMailError(self: ChangePassword, e: SendMailErrorEventArgs) """
        ...

    CancelButtonClick = ...
    CancelButtonCommandName: str = ...
    ChangedPassword = ...
    ChangePasswordButtonCommandName: str = ...
    ChangePasswordError = ...
    ChangingPassword = ...
    ContinueButtonClick = ...
    ContinueButtonCommandName: str = ...
    SendingMail = ...
    SendMailError = ...


class CheckBox(IPostBackDataHandler, WebControl, ICheckBoxControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ CheckBox() """
    @property
    def AutoPostBack(self) -> bool:
        """
        Get: AutoPostBack(self: CheckBox) -> bool
        Set: AutoPostBack(self: CheckBox) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: CheckBox) -> bool
        Set: CausesValidation(self: CheckBox) = value
        """
        ...

    @property
    def InputAttributes(self) -> AttributeCollection:
        """ Get: InputAttributes(self: CheckBox) -> AttributeCollection """
        ...

    @property
    def LabelAttributes(self) -> AttributeCollection:
        """ Get: LabelAttributes(self: CheckBox) -> AttributeCollection """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: CheckBox) -> str
        Set: Text(self: CheckBox) = value
        """
        ...

    @property
    def TextAlign(self): # -> TextAlign
        """
        Get: TextAlign(self: CheckBox) -> TextAlign
        Set: TextAlign(self: CheckBox) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: CheckBox) -> str
        Set: ValidationGroup(self: CheckBox) = value
        """
        ...


    def OnCheckedChanged(self, *args): #cannot find CLR method
        """ OnCheckedChanged(self: CheckBox, e: EventArgs) """
        ...

    CheckedChanged = ...


class CheckBoxField(BoundField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ CheckBoxField() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: CheckBoxField) -> str
        Set: Text(self: CheckBoxField) = value
        """
        ...



class IRepeatInfoUser: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasFooter(self) -> bool:
        """ Get: HasFooter(self: IRepeatInfoUser) -> bool """
        ...

    @property
    def HasHeader(self) -> bool:
        """ Get: HasHeader(self: IRepeatInfoUser) -> bool """
        ...

    @property
    def HasSeparators(self) -> bool:
        """ Get: HasSeparators(self: IRepeatInfoUser) -> bool """
        ...

    @property
    def RepeatedItemCount(self) -> int:
        """ Get: RepeatedItemCount(self: IRepeatInfoUser) -> int """
        ...


    def GetItemStyle(self, itemType, repeatIndex:int) -> Style: # Not found arg types: {'itemType': 'ListItemType'}
        """ GetItemStyle(self: IRepeatInfoUser, itemType: ListItemType, repeatIndex: int) -> Style """
        ...

    def RenderItem(self, itemType, repeatIndex:int, repeatInfo, writer:HtmlTextWriter): # ->  # Not found arg types: {'itemType': 'ListItemType', 'repeatInfo': 'RepeatInfo'}
        """ RenderItem(self: IRepeatInfoUser, itemType: ListItemType, repeatIndex: int, repeatInfo: RepeatInfo, writer: HtmlTextWriter) """
        ...


class CheckBoxList(IPostBackDataHandler, INamingContainer, ListControl, IRepeatInfoUser): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IEditableTextControl'>, <type 'object'>
    """ CheckBoxList() """
    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: CheckBoxList) -> int
        Set: CellPadding(self: CheckBoxList) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: CheckBoxList) -> int
        Set: CellSpacing(self: CheckBoxList) = value
        """
        ...

    @property
    def RenderWhenDataEmpty(self) -> bool:
        """
        Get: RenderWhenDataEmpty(self: CheckBoxList) -> bool
        Set: RenderWhenDataEmpty(self: CheckBoxList) = value
        """
        ...

    @property
    def RepeatColumns(self) -> int:
        """
        Get: RepeatColumns(self: CheckBoxList) -> int
        Set: RepeatColumns(self: CheckBoxList) = value
        """
        ...

    @property
    def RepeatDirection(self): # -> RepeatDirection
        """
        Get: RepeatDirection(self: CheckBoxList) -> RepeatDirection
        Set: RepeatDirection(self: CheckBoxList) = value
        """
        ...

    @property
    def RepeatLayout(self): # -> RepeatLayout
        """
        Get: RepeatLayout(self: CheckBoxList) -> RepeatLayout
        Set: RepeatLayout(self: CheckBoxList) = value
        """
        ...

    @property
    def TextAlign(self): # -> TextAlign
        """
        Get: TextAlign(self: CheckBoxList) -> TextAlign
        Set: TextAlign(self: CheckBoxList) = value
        """
        ...



class HotSpot(IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AccessKey(self) -> str:
        """
        Get: AccessKey(self: HotSpot) -> str
        Set: AccessKey(self: HotSpot) = value
        """
        ...

    @property
    def AlternateText(self) -> str:
        """
        Get: AlternateText(self: HotSpot) -> str
        Set: AlternateText(self: HotSpot) = value
        """
        ...

    @property
    def HotSpotMode(self): # -> HotSpotMode
        """
        Get: HotSpotMode(self: HotSpot) -> HotSpotMode
        Set: HotSpotMode(self: HotSpot) = value
        """
        ...

    @property
    def MarkupName(self):
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: HotSpot) -> str
        Set: NavigateUrl(self: HotSpot) = value
        """
        ...

    @property
    def PostBackValue(self) -> str:
        """
        Get: PostBackValue(self: HotSpot) -> str
        Set: PostBackValue(self: HotSpot) = value
        """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: HotSpot) -> Int16
        Set: TabIndex(self: HotSpot) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HotSpot) -> str
        Set: Target(self: HotSpot) = value
        """
        ...

    @property
    def ViewState(self):
        ...


    def GetCoordinates(self) -> str:
        """ GetCoordinates(self: HotSpot) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: HotSpot) -> str """
        ...


class CircleHotSpot(HotSpot): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ CircleHotSpot() """
    @property
    def Radius(self) -> int:
        """
        Get: Radius(self: CircleHotSpot) -> int
        Set: Radius(self: CircleHotSpot) = value
        """
        ...

    @property
    def X(self) -> int:
        """
        Get: X(self: CircleHotSpot) -> int
        Set: X(self: CircleHotSpot) = value
        """
        ...

    @property
    def Y(self) -> int:
        """
        Get: Y(self: CircleHotSpot) -> int
        Set: Y(self: CircleHotSpot) = value
        """
        ...



class CommandEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    CommandEventArgs(e: CommandEventArgs)
    CommandEventArgs(commandName: str, argument: object)
    """
    @property
    def CommandArgument(self) -> object:
        """ Get: CommandArgument(self: CommandEventArgs) -> object """
        ...

    @property
    def CommandName(self) -> str:
        """ Get: CommandName(self: CommandEventArgs) -> str """
        ...


    def __new__(cls, *__args:CommandEventArgs) -> Self:
        """
        __new__(cls: type, e: CommandEventArgs)
        __new__(cls: type, commandName: str, argument: object)
        """
        ...


class CommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CommandEventHandler, sender: object, e: CommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CommandEventArgs): # -> 
        """ Invoke(self: CommandEventHandler, sender: object, e: CommandEventArgs) """
        ...


class CommandField(ButtonFieldBase): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ CommandField() """
    @property
    def CancelImageUrl(self) -> str:
        """
        Get: CancelImageUrl(self: CommandField) -> str
        Set: CancelImageUrl(self: CommandField) = value
        """
        ...

    @property
    def CancelText(self) -> str:
        """
        Get: CancelText(self: CommandField) -> str
        Set: CancelText(self: CommandField) = value
        """
        ...

    @property
    def DeleteImageUrl(self) -> str:
        """
        Get: DeleteImageUrl(self: CommandField) -> str
        Set: DeleteImageUrl(self: CommandField) = value
        """
        ...

    @property
    def DeleteText(self) -> str:
        """
        Get: DeleteText(self: CommandField) -> str
        Set: DeleteText(self: CommandField) = value
        """
        ...

    @property
    def EditImageUrl(self) -> str:
        """
        Get: EditImageUrl(self: CommandField) -> str
        Set: EditImageUrl(self: CommandField) = value
        """
        ...

    @property
    def EditText(self) -> str:
        """
        Get: EditText(self: CommandField) -> str
        Set: EditText(self: CommandField) = value
        """
        ...

    @property
    def InsertImageUrl(self) -> str:
        """
        Get: InsertImageUrl(self: CommandField) -> str
        Set: InsertImageUrl(self: CommandField) = value
        """
        ...

    @property
    def InsertText(self) -> str:
        """
        Get: InsertText(self: CommandField) -> str
        Set: InsertText(self: CommandField) = value
        """
        ...

    @property
    def NewImageUrl(self) -> str:
        """
        Get: NewImageUrl(self: CommandField) -> str
        Set: NewImageUrl(self: CommandField) = value
        """
        ...

    @property
    def NewText(self) -> str:
        """
        Get: NewText(self: CommandField) -> str
        Set: NewText(self: CommandField) = value
        """
        ...

    @property
    def SelectImageUrl(self) -> str:
        """
        Get: SelectImageUrl(self: CommandField) -> str
        Set: SelectImageUrl(self: CommandField) = value
        """
        ...

    @property
    def SelectText(self) -> str:
        """
        Get: SelectText(self: CommandField) -> str
        Set: SelectText(self: CommandField) = value
        """
        ...

    @property
    def ShowCancelButton(self) -> bool:
        """
        Get: ShowCancelButton(self: CommandField) -> bool
        Set: ShowCancelButton(self: CommandField) = value
        """
        ...

    @property
    def ShowDeleteButton(self) -> bool:
        """
        Get: ShowDeleteButton(self: CommandField) -> bool
        Set: ShowDeleteButton(self: CommandField) = value
        """
        ...

    @property
    def ShowEditButton(self) -> bool:
        """
        Get: ShowEditButton(self: CommandField) -> bool
        Set: ShowEditButton(self: CommandField) = value
        """
        ...

    @property
    def ShowInsertButton(self) -> bool:
        """
        Get: ShowInsertButton(self: CommandField) -> bool
        Set: ShowInsertButton(self: CommandField) = value
        """
        ...

    @property
    def ShowSelectButton(self) -> bool:
        """
        Get: ShowSelectButton(self: CommandField) -> bool
        Set: ShowSelectButton(self: CommandField) = value
        """
        ...

    @property
    def UpdateImageUrl(self) -> str:
        """
        Get: UpdateImageUrl(self: CommandField) -> str
        Set: UpdateImageUrl(self: CommandField) = value
        """
        ...

    @property
    def UpdateText(self) -> str:
        """
        Get: UpdateText(self: CommandField) -> str
        Set: UpdateText(self: CommandField) = value
        """
        ...


    def InitializeCell(self, cell, cellType, rowState, rowIndex:int): # ->  # Not found arg types: {'cellType': 'DataControlCellType', 'cell': 'DataControlFieldCell', 'rowState': 'DataControlRowState'}
        """ InitializeCell(self: CommandField, cell: DataControlFieldCell, cellType: DataControlCellType, rowState: DataControlRowState, rowIndex: int) """
        ...

    def ValidateSupportsCallback(self): # -> 
        """ ValidateSupportsCallback(self: CommandField) """
        ...


class CompareValidator(BaseCompareValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ CompareValidator() """
    @property
    def ControlToCompare(self) -> str:
        """
        Get: ControlToCompare(self: CompareValidator) -> str
        Set: ControlToCompare(self: CompareValidator) = value
        """
        ...

    @property
    def Operator(self): # -> ValidationCompareOperator
        """
        Get: Operator(self: CompareValidator) -> ValidationCompareOperator
        Set: Operator(self: CompareValidator) = value
        """
        ...

    @property
    def ValueToCompare(self) -> str:
        """
        Get: ValueToCompare(self: CompareValidator) -> str
        Set: ValueToCompare(self: CompareValidator) = value
        """
        ...



class View(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ View() """
    def OnActivate(self, *args): #cannot find CLR method
        """ OnActivate(self: View, e: EventArgs) """
        ...

    def OnDeactivate(self, *args): #cannot find CLR method
        """ OnDeactivate(self: View, e: EventArgs) """
        ...

    Activate = ...
    Deactivate = ...


class WizardStepBase(View): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AllowReturn(self) -> bool:
        """
        Get: AllowReturn(self: WizardStepBase) -> bool
        Set: AllowReturn(self: WizardStepBase) = value
        """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: WizardStepBase) -> str
        Set: ID(self: WizardStepBase) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: WizardStepBase) -> str """
        ...

    @property
    def StepType(self): # -> WizardStepType
        """
        Get: StepType(self: WizardStepBase) -> WizardStepType
        Set: StepType(self: WizardStepBase) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: WizardStepBase) -> str
        Set: Title(self: WizardStepBase) = value
        """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: WizardStepBase) -> Wizard """
        ...



class TemplatedWizardStep(WizardStepBase): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TemplatedWizardStep() """
    @property
    def ContentTemplate(self) -> ITemplate:
        """
        Get: ContentTemplate(self: TemplatedWizardStep) -> ITemplate
        Set: ContentTemplate(self: TemplatedWizardStep) = value
        """
        ...

    @property
    def ContentTemplateContainer(self) -> Control:
        """ Get: ContentTemplateContainer(self: TemplatedWizardStep) -> Control """
        ...

    @property
    def CustomNavigationTemplate(self) -> ITemplate:
        """
        Get: CustomNavigationTemplate(self: TemplatedWizardStep) -> ITemplate
        Set: CustomNavigationTemplate(self: TemplatedWizardStep) = value
        """
        ...

    @property
    def CustomNavigationTemplateContainer(self) -> Control:
        """ Get: CustomNavigationTemplateContainer(self: TemplatedWizardStep) -> Control """
        ...

    @property
    def SkinID(self) -> str:
        """
        Get: SkinID(self: TemplatedWizardStep) -> str
        Set: SkinID(self: TemplatedWizardStep) = value
        """
        ...



class CompleteWizardStep(TemplatedWizardStep): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ CompleteWizardStep() """
    @property
    def StepType(self): # -> WizardStepType
        """
        Get: StepType(self: CompleteWizardStep) -> WizardStepType
        Set: StepType(self: CompleteWizardStep) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: CompleteWizardStep) -> str
        Set: Title(self: CompleteWizardStep) = value
        """
        ...



class CompositeDataBoundControl(INamingContainer, DataBoundControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: CompositeDataBoundControl) -> ControlCollection """
        ...

    @property
    def DeleteMethod(self):
        ...

    @property
    def InsertMethod(self):
        ...

    @property
    def UpdateMethod(self):
        ...



class Content(Control, INonBindingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ Content() """
    @property
    def ContentPlaceHolderID(self) -> str:
        """
        Get: ContentPlaceHolderID(self: Content) -> str
        Set: ContentPlaceHolderID(self: Content) = value
        """
        ...


    DataBinding = ...
    Disposed = ...
    Init = ...
    Load = ...
    PreRender = ...
    Unload = ...


class ContentDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContentDirection, values: LeftToRight (1), NotSet (0), RightToLeft (2) """
    LeftToRight: ContentDirection = ...
    NotSet: ContentDirection = ...
    RightToLeft: ContentDirection = ...
    value__ = ...


class ContentPlaceHolder(Control, INonBindingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ ContentPlaceHolder() """
    pass

class IQueryableDataSource(IDataSource): # skipped bases: <type 'object'>
    """ no doc """
    def RaiseViewChanged(self): # -> 
        """ RaiseViewChanged(self: IQueryableDataSource) """
        ...

    QueryCreated = ...


class QueryableDataSource(DataSourceControl, IQueryableDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """ no doc """
    def CreateQueryableView(self, *args): #cannot find CLR method
        """ CreateQueryableView(self: QueryableDataSource) -> QueryableDataSourceView """
        ...

    def UpdateParameterVales(self, *args): #cannot find CLR method
        """ UpdateParameterVales(self: QueryableDataSource) """
        ...

    QueryCreated = ...


class ContextDataSource(QueryableDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IQueryableDataSource'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """ no doc """
    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: ContextDataSource) -> str
        Set: ContextTypeName(self: ContextDataSource) = value
        """
        ...

    @property
    def EntitySetName(self):
        ...

    @property
    def EntityTypeName(self) -> str:
        """
        Get: EntityTypeName(self: ContextDataSource) -> str
        Set: EntityTypeName(self: ContextDataSource) = value
        """
        ...



class ContextDataSourceContextData: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContextDataSourceContextData()
    ContextDataSourceContextData(context: object)
    """
    @property
    def Context(self) -> object:
        """
        Get: Context(self: ContextDataSourceContextData) -> object
        Set: Context(self: ContextDataSourceContextData) = value
        """
        ...

    @property
    def EntitySet(self) -> object:
        """
        Get: EntitySet(self: ContextDataSourceContextData) -> object
        Set: EntitySet(self: ContextDataSourceContextData) = value
        """
        ...



class QueryableDataSourceView(DataSourceView, IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoGenerateOrderByClause(self) -> bool:
        """
        Get: AutoGenerateOrderByClause(self: QueryableDataSourceView) -> bool
        Set: AutoGenerateOrderByClause(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def AutoGenerateWhereClause(self) -> bool:
        """
        Get: AutoGenerateWhereClause(self: QueryableDataSourceView) -> bool
        Set: AutoGenerateWhereClause(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def AutoPage(self) -> bool:
        """
        Get: AutoPage(self: QueryableDataSourceView) -> bool
        Set: AutoPage(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def AutoSort(self) -> bool:
        """
        Get: AutoSort(self: QueryableDataSourceView) -> bool
        Set: AutoSort(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def EntityType(self):
        ...

    @property
    def GroupBy(self) -> str:
        """
        Get: GroupBy(self: QueryableDataSourceView) -> str
        Set: GroupBy(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def GroupByParameters(self) -> ParameterCollection:
        """ Get: GroupByParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def OrderBy(self) -> str:
        """
        Get: OrderBy(self: QueryableDataSourceView) -> str
        Set: OrderBy(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def OrderByParameters(self) -> ParameterCollection:
        """ Get: OrderByParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def OrderGroupsBy(self) -> str:
        """
        Get: OrderGroupsBy(self: QueryableDataSourceView) -> str
        Set: OrderGroupsBy(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def OrderGroupsByParameters(self) -> ParameterCollection:
        """ Get: OrderGroupsByParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def SelectNew(self) -> str:
        """
        Get: SelectNew(self: QueryableDataSourceView) -> str
        Set: SelectNew(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def SelectNewParameters(self) -> ParameterCollection:
        """ Get: SelectNewParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...

    @property
    def Where(self) -> str:
        """
        Get: Where(self: QueryableDataSourceView) -> str
        Set: Where(self: QueryableDataSourceView) = value
        """
        ...

    @property
    def WhereParameters(self) -> ParameterCollection:
        """ Get: WhereParameters(self: QueryableDataSourceView) -> ParameterCollection """
        ...


    def BuildDeleteObject(self, *args): #cannot find CLR method
        """ BuildDeleteObject(self: QueryableDataSourceView, keys: IDictionary, oldValues: IDictionary, validationErrors: IDictionary[str, Exception]) -> QueryableDataSourceEditData """
        ...

    def BuildInsertObject(self, *args): #cannot find CLR method
        """ BuildInsertObject(self: QueryableDataSourceView, values: IDictionary, validationErrors: IDictionary[str, Exception]) -> QueryableDataSourceEditData """
        ...

    def BuildQuery(self, *args): #cannot find CLR method
        """ BuildQuery(self: QueryableDataSourceView, arguments: DataSourceSelectArguments) -> IQueryable """
        ...

    def BuildUpdateObjects(self, *args): #cannot find CLR method
        """ BuildUpdateObjects(self: QueryableDataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary, validationErrors: IDictionary[str, Exception]) -> QueryableDataSourceEditData """
        ...

    def ClearOriginalValues(self, *args): #cannot find CLR method
        """ ClearOriginalValues(self: QueryableDataSourceView) """
        ...

    def CreateQueryContext(self, *args): #cannot find CLR method
        """ CreateQueryContext(self: QueryableDataSourceView, arguments: DataSourceSelectArguments) -> QueryContext """
        ...

    def DeleteObject(self, *args): #cannot find CLR method
        """ DeleteObject(self: QueryableDataSourceView, oldEntity: object) -> int """
        ...

    def ExecutePaging(self, *args): #cannot find CLR method
        """ ExecutePaging(self: QueryableDataSourceView, source: IQueryable, context: QueryContext) -> IQueryable """
        ...

    def ExecuteQuery(self, *args): #cannot find CLR method
        """ ExecuteQuery(self: QueryableDataSourceView, source: IQueryable, context: QueryContext) -> IQueryable """
        ...

    def ExecuteQueryExpressions(self, *args): #cannot find CLR method
        """ ExecuteQueryExpressions(self: QueryableDataSourceView, source: IQueryable, context: QueryContext) -> IQueryable """
        ...

    def ExecuteSorting(self, *args): #cannot find CLR method
        """ ExecuteSorting(self: QueryableDataSourceView, source: IQueryable, context: QueryContext) -> IQueryable """
        ...

    def GetOriginalValues(self, *args): #cannot find CLR method
        """ GetOriginalValues(self: QueryableDataSourceView, keys: IDictionary) -> IDictionary """
        ...

    def GetSource(self, *args): #cannot find CLR method
        """ GetSource(self: QueryableDataSourceView, context: QueryContext) -> object """
        ...

    def HandleValidationErrors(self, *args): #cannot find CLR method
        """ HandleValidationErrors(self: QueryableDataSourceView, errors: IDictionary[str, Exception], operation: DataSourceOperation) """
        ...

    def InsertObject(self, *args): #cannot find CLR method
        """ InsertObject(self: QueryableDataSourceView, newEntity: object) -> int """
        ...

    def OnQueryCreated(self, *args): #cannot find CLR method
        """ OnQueryCreated(self: QueryableDataSourceView, e: QueryCreatedEventArgs) """
        ...

    def OnQueryParametersChanged(self, *args): #cannot find CLR method
        """ OnQueryParametersChanged(self: QueryableDataSourceView, sender: object, e: EventArgs) """
        ...

    def RaiseViewChanged(self): # -> 
        """ RaiseViewChanged(self: QueryableDataSourceView) """
        ...

    def StoreOriginalValues(self, *args): #cannot find CLR method
        """ StoreOriginalValues(self: QueryableDataSourceView, results: IList)StoreOriginalValues(self: QueryableDataSourceView, results: IList, include: Func[PropertyDescriptor, bool]) """
        ...

    def UpdateObject(self, *args): #cannot find CLR method
        """ UpdateObject(self: QueryableDataSourceView, oldEntity: object, newEntity: object) -> int """
        ...

    EventSelected: object = ...
    EventSelecting: object = ...
    QueryCreated = ...


class ContextDataSourceView(QueryableDataSourceView): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ no doc """
    @property
    def Context(self):
        ...

    @property
    def ContextType(self) -> Type:
        """ Get: ContextType(self: ContextDataSourceView) -> Type """
        ...

    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: ContextDataSourceView) -> str
        Set: ContextTypeName(self: ContextDataSourceView) = value
        """
        ...

    @property
    def EntitySet(self):
        ...

    @property
    def EntitySetName(self) -> str:
        """
        Get: EntitySetName(self: ContextDataSourceView) -> str
        Set: EntitySetName(self: ContextDataSourceView) = value
        """
        ...

    @property
    def EntitySetType(self):
        ...

    @property
    def EntityTypeName(self) -> str:
        """
        Get: EntityTypeName(self: ContextDataSourceView) -> str
        Set: EntityTypeName(self: ContextDataSourceView) = value
        """
        ...


    def CreateContext(self, *args): #cannot find CLR method
        """ CreateContext(self: ContextDataSourceView, operation: DataSourceOperation) -> ContextDataSourceContextData """
        ...

    def DisposeContext(self, *args): #cannot find CLR method
        """ DisposeContext(self: ContextDataSourceView, dataContext: object)DisposeContext(self: ContextDataSourceView) """
        ...

    def GetDataObjectType(self, *args): #cannot find CLR method
        """ GetDataObjectType(self: ContextDataSourceView, type: Type) -> Type """
        ...

    def GetEntitySetType(self, *args): #cannot find CLR method
        """ GetEntitySetType(self: ContextDataSourceView) -> Type """
        ...

    EventContextCreated: object = ...
    EventContextCreating: object = ...
    EventContextDisposing: object = ...


class Parameter(ICloneable, IStateManager): # skipped bases: <type 'object'>
    """
    Parameter()
    Parameter(name: str)
    Parameter(name: str, dbType: DbType)
    Parameter(name: str, dbType: DbType, defaultValue: str)
    Parameter(name: str, type: TypeCode)
    Parameter(name: str, type: TypeCode, defaultValue: str)
    """
    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: Parameter) -> bool
        Set: ConvertEmptyStringToNull(self: Parameter) = value
        """
        ...

    @property
    def DbType(self) -> DbType:
        """
        Get: DbType(self: Parameter) -> DbType
        Set: DbType(self: Parameter) = value
        """
        ...

    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: Parameter) -> str
        Set: DefaultValue(self: Parameter) = value
        """
        ...

    @property
    def Direction(self) -> ParameterDirection:
        """
        Get: Direction(self: Parameter) -> ParameterDirection
        Set: Direction(self: Parameter) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Parameter) -> str
        Set: Name(self: Parameter) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: Parameter) -> int
        Set: Size(self: Parameter) = value
        """
        ...

    @property
    def Type(self) -> TypeCode:
        """
        Get: Type(self: Parameter) -> TypeCode
        Set: Type(self: Parameter) = value
        """
        ...

    @property
    def ViewState(self):
        ...


    @staticmethod
    def ConvertDbTypeToTypeCode(dbType:DbType) -> TypeCode:
        """ ConvertDbTypeToTypeCode(dbType: DbType) -> TypeCode """
        ...

    @staticmethod
    def ConvertTypeCodeToDbType(typeCode:TypeCode) -> DbType:
        """ ConvertTypeCodeToDbType(typeCode: TypeCode) -> DbType """
        ...

    def Evaluate(self, *args): #cannot find CLR method
        """ Evaluate(self: Parameter, context: HttpContext, control: Control) -> object """
        ...

    def GetDatabaseType(self) -> DbType:
        """ GetDatabaseType(self: Parameter) -> DbType """
        ...

    def OnParameterChanged(self, *args): #cannot find CLR method
        """ OnParameterChanged(self: Parameter) """
        ...

    def SetDirty(self, *args): #cannot find CLR method
        """ SetDirty(self: Parameter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Parameter) -> str """
        ...


class ControlParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    ControlParameter()
    ControlParameter(name: str, controlID: str)
    ControlParameter(name: str, controlID: str, propertyName: str)
    ControlParameter(name: str, dbType: DbType, controlID: str, propertyName: str)
    ControlParameter(name: str, type: TypeCode, controlID: str, propertyName: str)
    """
    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: ControlParameter) -> str
        Set: ControlID(self: ControlParameter) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ControlParameter) -> str
        Set: PropertyName(self: ControlParameter) = value
        """
        ...



class ControlPropertyNameConverter(StringConverter): # skipped bases: <type 'object'>
    """ ControlPropertyNameConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: ControlPropertyNameConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: ControlPropertyNameConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: ControlPropertyNameConverter, context: ITypeDescriptorContext) -> bool """
        ...


class CookieParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    CookieParameter()
    CookieParameter(name: str, cookieName: str)
    CookieParameter(name: str, dbType: DbType, cookieName: str)
    CookieParameter(name: str, type: TypeCode, cookieName: str)
    """
    @property
    def CookieName(self) -> str:
        """
        Get: CookieName(self: CookieParameter) -> str
        Set: CookieName(self: CookieParameter) = value
        """
        ...

    @property
    def ValidateInput(self) -> bool:
        """
        Get: ValidateInput(self: CookieParameter) -> bool
        Set: ValidateInput(self: CookieParameter) = value
        """
        ...



class CreateUserErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CreateUserErrorEventArgs(s: MembershipCreateStatus) """
    @property
    def CreateUserError(self) -> MembershipCreateStatus:
        """
        Get: CreateUserError(self: CreateUserErrorEventArgs) -> MembershipCreateStatus
        Set: CreateUserError(self: CreateUserErrorEventArgs) = value
        """
        ...


    def __new__(cls, s:MembershipCreateStatus) -> Self:
        """ __new__(cls: type, s: MembershipCreateStatus) """
        ...


class CreateUserErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CreateUserErrorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CreateUserErrorEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CreateUserErrorEventHandler, sender: object, e: CreateUserErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CreateUserErrorEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CreateUserErrorEventArgs): # -> 
        """ Invoke(self: CreateUserErrorEventHandler, sender: object, e: CreateUserErrorEventArgs) """
        ...


class Wizard(CompositeControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ Wizard() """
    @property
    def ActiveStep(self) -> WizardStepBase:
        """ Get: ActiveStep(self: Wizard) -> WizardStepBase """
        ...

    @property
    def ActiveStepIndex(self) -> int:
        """
        Get: ActiveStepIndex(self: Wizard) -> int
        Set: ActiveStepIndex(self: Wizard) = value
        """
        ...

    @property
    def CancelButtonImageUrl(self) -> str:
        """
        Get: CancelButtonImageUrl(self: Wizard) -> str
        Set: CancelButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def CancelButtonStyle(self) -> Style:
        """ Get: CancelButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def CancelButtonText(self) -> str:
        """
        Get: CancelButtonText(self: Wizard) -> str
        Set: CancelButtonText(self: Wizard) = value
        """
        ...

    @property
    def CancelButtonType(self) -> ButtonType:
        """
        Get: CancelButtonType(self: Wizard) -> ButtonType
        Set: CancelButtonType(self: Wizard) = value
        """
        ...

    @property
    def CancelDestinationPageUrl(self) -> str:
        """
        Get: CancelDestinationPageUrl(self: Wizard) -> str
        Set: CancelDestinationPageUrl(self: Wizard) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: Wizard) -> int
        Set: CellPadding(self: Wizard) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: Wizard) -> int
        Set: CellSpacing(self: Wizard) = value
        """
        ...

    @property
    def DisplayCancelButton(self) -> bool:
        """
        Get: DisplayCancelButton(self: Wizard) -> bool
        Set: DisplayCancelButton(self: Wizard) = value
        """
        ...

    @property
    def DisplaySideBar(self) -> bool:
        """
        Get: DisplaySideBar(self: Wizard) -> bool
        Set: DisplaySideBar(self: Wizard) = value
        """
        ...

    @property
    def FinishCompleteButtonImageUrl(self) -> str:
        """
        Get: FinishCompleteButtonImageUrl(self: Wizard) -> str
        Set: FinishCompleteButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def FinishCompleteButtonStyle(self) -> Style:
        """ Get: FinishCompleteButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def FinishCompleteButtonText(self) -> str:
        """
        Get: FinishCompleteButtonText(self: Wizard) -> str
        Set: FinishCompleteButtonText(self: Wizard) = value
        """
        ...

    @property
    def FinishCompleteButtonType(self) -> ButtonType:
        """
        Get: FinishCompleteButtonType(self: Wizard) -> ButtonType
        Set: FinishCompleteButtonType(self: Wizard) = value
        """
        ...

    @property
    def FinishDestinationPageUrl(self) -> str:
        """
        Get: FinishDestinationPageUrl(self: Wizard) -> str
        Set: FinishDestinationPageUrl(self: Wizard) = value
        """
        ...

    @property
    def FinishNavigationTemplate(self) -> ITemplate:
        """
        Get: FinishNavigationTemplate(self: Wizard) -> ITemplate
        Set: FinishNavigationTemplate(self: Wizard) = value
        """
        ...

    @property
    def FinishPreviousButtonImageUrl(self) -> str:
        """
        Get: FinishPreviousButtonImageUrl(self: Wizard) -> str
        Set: FinishPreviousButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def FinishPreviousButtonStyle(self) -> Style:
        """ Get: FinishPreviousButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def FinishPreviousButtonText(self) -> str:
        """
        Get: FinishPreviousButtonText(self: Wizard) -> str
        Set: FinishPreviousButtonText(self: Wizard) = value
        """
        ...

    @property
    def FinishPreviousButtonType(self) -> ButtonType:
        """
        Get: FinishPreviousButtonType(self: Wizard) -> ButtonType
        Set: FinishPreviousButtonType(self: Wizard) = value
        """
        ...

    @property
    def HeaderStyle(self): # -> TableItemStyle
        """ Get: HeaderStyle(self: Wizard) -> TableItemStyle """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: Wizard) -> ITemplate
        Set: HeaderTemplate(self: Wizard) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: Wizard) -> str
        Set: HeaderText(self: Wizard) = value
        """
        ...

    @property
    def LayoutTemplate(self) -> ITemplate:
        """
        Get: LayoutTemplate(self: Wizard) -> ITemplate
        Set: LayoutTemplate(self: Wizard) = value
        """
        ...

    @property
    def NavigationButtonStyle(self) -> Style:
        """ Get: NavigationButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def NavigationStyle(self): # -> TableItemStyle
        """ Get: NavigationStyle(self: Wizard) -> TableItemStyle """
        ...

    @property
    def SideBarButtonStyle(self) -> Style:
        """ Get: SideBarButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def SideBarStyle(self): # -> TableItemStyle
        """ Get: SideBarStyle(self: Wizard) -> TableItemStyle """
        ...

    @property
    def SideBarTemplate(self) -> ITemplate:
        """
        Get: SideBarTemplate(self: Wizard) -> ITemplate
        Set: SideBarTemplate(self: Wizard) = value
        """
        ...

    @property
    def SkipLinkText(self) -> str:
        """
        Get: SkipLinkText(self: Wizard) -> str
        Set: SkipLinkText(self: Wizard) = value
        """
        ...

    @property
    def StartNavigationTemplate(self) -> ITemplate:
        """
        Get: StartNavigationTemplate(self: Wizard) -> ITemplate
        Set: StartNavigationTemplate(self: Wizard) = value
        """
        ...

    @property
    def StartNextButtonImageUrl(self) -> str:
        """
        Get: StartNextButtonImageUrl(self: Wizard) -> str
        Set: StartNextButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def StartNextButtonStyle(self) -> Style:
        """ Get: StartNextButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def StartNextButtonText(self) -> str:
        """
        Get: StartNextButtonText(self: Wizard) -> str
        Set: StartNextButtonText(self: Wizard) = value
        """
        ...

    @property
    def StartNextButtonType(self) -> ButtonType:
        """
        Get: StartNextButtonType(self: Wizard) -> ButtonType
        Set: StartNextButtonType(self: Wizard) = value
        """
        ...

    @property
    def StepNavigationTemplate(self) -> ITemplate:
        """
        Get: StepNavigationTemplate(self: Wizard) -> ITemplate
        Set: StepNavigationTemplate(self: Wizard) = value
        """
        ...

    @property
    def StepNextButtonImageUrl(self) -> str:
        """
        Get: StepNextButtonImageUrl(self: Wizard) -> str
        Set: StepNextButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def StepNextButtonStyle(self) -> Style:
        """ Get: StepNextButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def StepNextButtonText(self) -> str:
        """
        Get: StepNextButtonText(self: Wizard) -> str
        Set: StepNextButtonText(self: Wizard) = value
        """
        ...

    @property
    def StepNextButtonType(self) -> ButtonType:
        """
        Get: StepNextButtonType(self: Wizard) -> ButtonType
        Set: StepNextButtonType(self: Wizard) = value
        """
        ...

    @property
    def StepPreviousButtonImageUrl(self) -> str:
        """
        Get: StepPreviousButtonImageUrl(self: Wizard) -> str
        Set: StepPreviousButtonImageUrl(self: Wizard) = value
        """
        ...

    @property
    def StepPreviousButtonStyle(self) -> Style:
        """ Get: StepPreviousButtonStyle(self: Wizard) -> Style """
        ...

    @property
    def StepPreviousButtonText(self) -> str:
        """
        Get: StepPreviousButtonText(self: Wizard) -> str
        Set: StepPreviousButtonText(self: Wizard) = value
        """
        ...

    @property
    def StepPreviousButtonType(self) -> ButtonType:
        """
        Get: StepPreviousButtonType(self: Wizard) -> ButtonType
        Set: StepPreviousButtonType(self: Wizard) = value
        """
        ...

    @property
    def StepStyle(self): # -> TableItemStyle
        """ Get: StepStyle(self: Wizard) -> TableItemStyle """
        ...

    @property
    def WizardSteps(self): # -> WizardStepCollection
        """ Get: WizardSteps(self: Wizard) -> WizardStepCollection """
        ...


    def AllowNavigationToStep(self, *args): #cannot find CLR method
        """ AllowNavigationToStep(self: Wizard, index: int) -> bool """
        ...

    def CreateControlHierarchy(self, *args): #cannot find CLR method
        """ CreateControlHierarchy(self: Wizard) """
        ...

    def GetHistory(self) -> ICollection:
        """ GetHistory(self: Wizard) -> ICollection """
        ...

    def GetStepType(self, wizardStep:WizardStepBase, index:int): # -> WizardStepType
        """ GetStepType(self: Wizard, wizardStep: WizardStepBase, index: int) -> WizardStepType """
        ...

    def MoveTo(self, wizardStep:WizardStepBase): # -> 
        """ MoveTo(self: Wizard, wizardStep: WizardStepBase) """
        ...

    def OnActiveStepChanged(self, *args): #cannot find CLR method
        """ OnActiveStepChanged(self: Wizard, source: object, e: EventArgs) """
        ...

    def OnCancelButtonClick(self, *args): #cannot find CLR method
        """ OnCancelButtonClick(self: Wizard, e: EventArgs) """
        ...

    def OnFinishButtonClick(self, *args): #cannot find CLR method
        """ OnFinishButtonClick(self: Wizard, e: WizardNavigationEventArgs) """
        ...

    def OnNextButtonClick(self, *args): #cannot find CLR method
        """ OnNextButtonClick(self: Wizard, e: WizardNavigationEventArgs) """
        ...

    def OnPreviousButtonClick(self, *args): #cannot find CLR method
        """ OnPreviousButtonClick(self: Wizard, e: WizardNavigationEventArgs) """
        ...

    def OnSideBarButtonClick(self, *args): #cannot find CLR method
        """ OnSideBarButtonClick(self: Wizard, e: WizardNavigationEventArgs) """
        ...

    def RegisterCommandEvents(self, *args): #cannot find CLR method
        """ RegisterCommandEvents(self: Wizard, button: IButtonControl) """
        ...

    ActiveStepChanged = ...
    CancelButtonClick = ...
    CancelButtonID: str = ...
    CancelCommandName: str = ...
    CustomFinishButtonID: str = ...
    CustomNextButtonID: str = ...
    CustomPreviousButtonID: str = ...
    DataListID: str = ...
    FinishButtonClick = ...
    FinishButtonID: str = ...
    FinishPreviousButtonID: str = ...
    HeaderPlaceholderId: str = ...
    MoveCompleteCommandName: str = ...
    MoveNextCommandName: str = ...
    MovePreviousCommandName: str = ...
    MoveToCommandName: str = ...
    NavigationPlaceholderId: str = ...
    NextButtonClick = ...
    PreviousButtonClick = ...
    SideBarButtonClick = ...
    SideBarButtonID: str = ...
    SideBarPlaceholderId: str = ...
    StartNextButtonID: str = ...
    StepNextButtonID: str = ...
    StepPreviousButtonID: str = ...
    WizardStepPlaceholderId: str = ...


class CreateUserWizard(Wizard): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ CreateUserWizard() """
    @property
    def Answer(self) -> str:
        """
        Get: Answer(self: CreateUserWizard) -> str
        Set: Answer(self: CreateUserWizard) = value
        """
        ...

    @property
    def AnswerLabelText(self) -> str:
        """
        Get: AnswerLabelText(self: CreateUserWizard) -> str
        Set: AnswerLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def AnswerRequiredErrorMessage(self) -> str:
        """
        Get: AnswerRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: AnswerRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def AutoGeneratePassword(self) -> bool:
        """
        Get: AutoGeneratePassword(self: CreateUserWizard) -> bool
        Set: AutoGeneratePassword(self: CreateUserWizard) = value
        """
        ...

    @property
    def CompleteStep(self) -> CompleteWizardStep:
        """ Get: CompleteStep(self: CreateUserWizard) -> CompleteWizardStep """
        ...

    @property
    def CompleteSuccessText(self) -> str:
        """
        Get: CompleteSuccessText(self: CreateUserWizard) -> str
        Set: CompleteSuccessText(self: CreateUserWizard) = value
        """
        ...

    @property
    def CompleteSuccessTextStyle(self): # -> TableItemStyle
        """ Get: CompleteSuccessTextStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def ConfirmPassword(self) -> str:
        """ Get: ConfirmPassword(self: CreateUserWizard) -> str """
        ...

    @property
    def ConfirmPasswordCompareErrorMessage(self) -> str:
        """
        Get: ConfirmPasswordCompareErrorMessage(self: CreateUserWizard) -> str
        Set: ConfirmPasswordCompareErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def ConfirmPasswordLabelText(self) -> str:
        """
        Get: ConfirmPasswordLabelText(self: CreateUserWizard) -> str
        Set: ConfirmPasswordLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def ConfirmPasswordRequiredErrorMessage(self) -> str:
        """
        Get: ConfirmPasswordRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: ConfirmPasswordRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def ContinueButtonImageUrl(self) -> str:
        """
        Get: ContinueButtonImageUrl(self: CreateUserWizard) -> str
        Set: ContinueButtonImageUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def ContinueButtonStyle(self) -> Style:
        """ Get: ContinueButtonStyle(self: CreateUserWizard) -> Style """
        ...

    @property
    def ContinueButtonText(self) -> str:
        """
        Get: ContinueButtonText(self: CreateUserWizard) -> str
        Set: ContinueButtonText(self: CreateUserWizard) = value
        """
        ...

    @property
    def ContinueButtonType(self) -> ButtonType:
        """
        Get: ContinueButtonType(self: CreateUserWizard) -> ButtonType
        Set: ContinueButtonType(self: CreateUserWizard) = value
        """
        ...

    @property
    def ContinueDestinationPageUrl(self) -> str:
        """
        Get: ContinueDestinationPageUrl(self: CreateUserWizard) -> str
        Set: ContinueDestinationPageUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def CreateUserButtonImageUrl(self) -> str:
        """
        Get: CreateUserButtonImageUrl(self: CreateUserWizard) -> str
        Set: CreateUserButtonImageUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def CreateUserButtonStyle(self) -> Style:
        """ Get: CreateUserButtonStyle(self: CreateUserWizard) -> Style """
        ...

    @property
    def CreateUserButtonText(self) -> str:
        """
        Get: CreateUserButtonText(self: CreateUserWizard) -> str
        Set: CreateUserButtonText(self: CreateUserWizard) = value
        """
        ...

    @property
    def CreateUserButtonType(self) -> ButtonType:
        """
        Get: CreateUserButtonType(self: CreateUserWizard) -> ButtonType
        Set: CreateUserButtonType(self: CreateUserWizard) = value
        """
        ...

    @property
    def CreateUserStep(self): # -> CreateUserWizardStep
        """ Get: CreateUserStep(self: CreateUserWizard) -> CreateUserWizardStep """
        ...

    @property
    def DisableCreatedUser(self) -> bool:
        """
        Get: DisableCreatedUser(self: CreateUserWizard) -> bool
        Set: DisableCreatedUser(self: CreateUserWizard) = value
        """
        ...

    @property
    def DuplicateEmailErrorMessage(self) -> str:
        """
        Get: DuplicateEmailErrorMessage(self: CreateUserWizard) -> str
        Set: DuplicateEmailErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def DuplicateUserNameErrorMessage(self) -> str:
        """
        Get: DuplicateUserNameErrorMessage(self: CreateUserWizard) -> str
        Set: DuplicateUserNameErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def EditProfileIconUrl(self) -> str:
        """
        Get: EditProfileIconUrl(self: CreateUserWizard) -> str
        Set: EditProfileIconUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def EditProfileText(self) -> str:
        """
        Get: EditProfileText(self: CreateUserWizard) -> str
        Set: EditProfileText(self: CreateUserWizard) = value
        """
        ...

    @property
    def EditProfileUrl(self) -> str:
        """
        Get: EditProfileUrl(self: CreateUserWizard) -> str
        Set: EditProfileUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def Email(self) -> str:
        """
        Get: Email(self: CreateUserWizard) -> str
        Set: Email(self: CreateUserWizard) = value
        """
        ...

    @property
    def EmailLabelText(self) -> str:
        """
        Get: EmailLabelText(self: CreateUserWizard) -> str
        Set: EmailLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def EmailRegularExpression(self) -> str:
        """
        Get: EmailRegularExpression(self: CreateUserWizard) -> str
        Set: EmailRegularExpression(self: CreateUserWizard) = value
        """
        ...

    @property
    def EmailRegularExpressionErrorMessage(self) -> str:
        """
        Get: EmailRegularExpressionErrorMessage(self: CreateUserWizard) -> str
        Set: EmailRegularExpressionErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def EmailRequiredErrorMessage(self) -> str:
        """
        Get: EmailRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: EmailRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def ErrorMessageStyle(self): # -> TableItemStyle
        """ Get: ErrorMessageStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def HelpPageIconUrl(self) -> str:
        """
        Get: HelpPageIconUrl(self: CreateUserWizard) -> str
        Set: HelpPageIconUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def HelpPageText(self) -> str:
        """
        Get: HelpPageText(self: CreateUserWizard) -> str
        Set: HelpPageText(self: CreateUserWizard) = value
        """
        ...

    @property
    def HelpPageUrl(self) -> str:
        """
        Get: HelpPageUrl(self: CreateUserWizard) -> str
        Set: HelpPageUrl(self: CreateUserWizard) = value
        """
        ...

    @property
    def HyperLinkStyle(self): # -> TableItemStyle
        """ Get: HyperLinkStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def InstructionText(self) -> str:
        """
        Get: InstructionText(self: CreateUserWizard) -> str
        Set: InstructionText(self: CreateUserWizard) = value
        """
        ...

    @property
    def InstructionTextStyle(self): # -> TableItemStyle
        """ Get: InstructionTextStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def InvalidAnswerErrorMessage(self) -> str:
        """
        Get: InvalidAnswerErrorMessage(self: CreateUserWizard) -> str
        Set: InvalidAnswerErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def InvalidEmailErrorMessage(self) -> str:
        """
        Get: InvalidEmailErrorMessage(self: CreateUserWizard) -> str
        Set: InvalidEmailErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def InvalidPasswordErrorMessage(self) -> str:
        """
        Get: InvalidPasswordErrorMessage(self: CreateUserWizard) -> str
        Set: InvalidPasswordErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def InvalidQuestionErrorMessage(self) -> str:
        """
        Get: InvalidQuestionErrorMessage(self: CreateUserWizard) -> str
        Set: InvalidQuestionErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def LabelStyle(self): # -> TableItemStyle
        """ Get: LabelStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def LoginCreatedUser(self) -> bool:
        """
        Get: LoginCreatedUser(self: CreateUserWizard) -> bool
        Set: LoginCreatedUser(self: CreateUserWizard) = value
        """
        ...

    @property
    def MailDefinition(self): # -> MailDefinition
        """ Get: MailDefinition(self: CreateUserWizard) -> MailDefinition """
        ...

    @property
    def MembershipProvider(self) -> str:
        """
        Get: MembershipProvider(self: CreateUserWizard) -> str
        Set: MembershipProvider(self: CreateUserWizard) = value
        """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: CreateUserWizard) -> str """
        ...

    @property
    def PasswordHintStyle(self): # -> TableItemStyle
        """ Get: PasswordHintStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def PasswordHintText(self) -> str:
        """
        Get: PasswordHintText(self: CreateUserWizard) -> str
        Set: PasswordHintText(self: CreateUserWizard) = value
        """
        ...

    @property
    def PasswordLabelText(self) -> str:
        """
        Get: PasswordLabelText(self: CreateUserWizard) -> str
        Set: PasswordLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def PasswordRegularExpression(self) -> str:
        """
        Get: PasswordRegularExpression(self: CreateUserWizard) -> str
        Set: PasswordRegularExpression(self: CreateUserWizard) = value
        """
        ...

    @property
    def PasswordRegularExpressionErrorMessage(self) -> str:
        """
        Get: PasswordRegularExpressionErrorMessage(self: CreateUserWizard) -> str
        Set: PasswordRegularExpressionErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def PasswordRequiredErrorMessage(self) -> str:
        """
        Get: PasswordRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: PasswordRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def Question(self) -> str:
        """
        Get: Question(self: CreateUserWizard) -> str
        Set: Question(self: CreateUserWizard) = value
        """
        ...

    @property
    def QuestionAndAnswerRequired(self):
        ...

    @property
    def QuestionLabelText(self) -> str:
        """
        Get: QuestionLabelText(self: CreateUserWizard) -> str
        Set: QuestionLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def QuestionRequiredErrorMessage(self) -> str:
        """
        Get: QuestionRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: QuestionRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def RequireEmail(self) -> bool:
        """
        Get: RequireEmail(self: CreateUserWizard) -> bool
        Set: RequireEmail(self: CreateUserWizard) = value
        """
        ...

    @property
    def TextBoxStyle(self) -> Style:
        """ Get: TextBoxStyle(self: CreateUserWizard) -> Style """
        ...

    @property
    def TitleTextStyle(self): # -> TableItemStyle
        """ Get: TitleTextStyle(self: CreateUserWizard) -> TableItemStyle """
        ...

    @property
    def UnknownErrorMessage(self) -> str:
        """
        Get: UnknownErrorMessage(self: CreateUserWizard) -> str
        Set: UnknownErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: CreateUserWizard) -> str
        Set: UserName(self: CreateUserWizard) = value
        """
        ...

    @property
    def UserNameLabelText(self) -> str:
        """
        Get: UserNameLabelText(self: CreateUserWizard) -> str
        Set: UserNameLabelText(self: CreateUserWizard) = value
        """
        ...

    @property
    def UserNameRequiredErrorMessage(self) -> str:
        """
        Get: UserNameRequiredErrorMessage(self: CreateUserWizard) -> str
        Set: UserNameRequiredErrorMessage(self: CreateUserWizard) = value
        """
        ...

    @property
    def ValidatorTextStyle(self) -> Style:
        """ Get: ValidatorTextStyle(self: CreateUserWizard) -> Style """
        ...


    def OnContinueButtonClick(self, *args): #cannot find CLR method
        """ OnContinueButtonClick(self: CreateUserWizard, e: EventArgs) """
        ...

    def OnCreatedUser(self, *args): #cannot find CLR method
        """ OnCreatedUser(self: CreateUserWizard, e: EventArgs) """
        ...

    def OnCreateUserError(self, *args): #cannot find CLR method
        """ OnCreateUserError(self: CreateUserWizard, e: CreateUserErrorEventArgs) """
        ...

    def OnCreatingUser(self, *args): #cannot find CLR method
        """ OnCreatingUser(self: CreateUserWizard, e: LoginCancelEventArgs) """
        ...

    def OnSendingMail(self, *args): #cannot find CLR method
        """ OnSendingMail(self: CreateUserWizard, e: MailMessageEventArgs) """
        ...

    def OnSendMailError(self, *args): #cannot find CLR method
        """ OnSendMailError(self: CreateUserWizard, e: SendMailErrorEventArgs) """
        ...

    ContinueButtonClick = ...
    ContinueButtonCommandName: str = ...
    CreatedUser = ...
    CreateUserError = ...
    CreatingUser = ...
    SendingMail = ...
    SendMailError = ...


class CreateUserWizardStep(TemplatedWizardStep): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ CreateUserWizardStep() """
    @property
    def AllowReturn(self) -> bool:
        """
        Get: AllowReturn(self: CreateUserWizardStep) -> bool
        Set: AllowReturn(self: CreateUserWizardStep) = value
        """
        ...

    @property
    def StepType(self): # -> WizardStepType
        """
        Get: StepType(self: CreateUserWizardStep) -> WizardStepType
        Set: StepType(self: CreateUserWizardStep) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: CreateUserWizardStep) -> str
        Set: Title(self: CreateUserWizardStep) = value
        """
        ...



class CreatingModelDataSourceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CreatingModelDataSourceEventArgs() """
    @property
    def ModelDataSource(self): # -> ModelDataSource
        """
        Get: ModelDataSource(self: CreatingModelDataSourceEventArgs) -> ModelDataSource
        Set: ModelDataSource(self: CreatingModelDataSourceEventArgs) = value
        """
        ...



class CreatingModelDataSourceEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CreatingModelDataSourceEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CreatingModelDataSourceEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CreatingModelDataSourceEventHandler, sender: object, e: CreatingModelDataSourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CreatingModelDataSourceEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CreatingModelDataSourceEventArgs): # -> 
        """ Invoke(self: CreatingModelDataSourceEventHandler, sender: object, e: CreatingModelDataSourceEventArgs) """
        ...


class CustomValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ CustomValidator() """
    @property
    def ClientValidationFunction(self) -> str:
        """
        Get: ClientValidationFunction(self: CustomValidator) -> str
        Set: ClientValidationFunction(self: CustomValidator) = value
        """
        ...

    @property
    def ValidateEmptyText(self) -> bool:
        """
        Get: ValidateEmptyText(self: CustomValidator) -> bool
        Set: ValidateEmptyText(self: CustomValidator) = value
        """
        ...


    def OnServerValidate(self, *args): #cannot find CLR method
        """ OnServerValidate(self: CustomValidator, value: str) -> bool """
        ...

    ServerValidate = ...


class DataBoundControlMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataBoundControlMode, values: Edit (1), Insert (2), ReadOnly (0) """
    Edit: DataBoundControlMode = ...
    Insert: DataBoundControlMode = ...
    ReadOnly: DataBoundControlMode = ...
    value__ = ...


class DataControlCellType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataControlCellType, values: DataCell (2), Footer (1), Header (0) """
    DataCell: DataControlCellType = ...
    Footer: DataControlCellType = ...
    Header: DataControlCellType = ...
    value__ = ...


class DataControlCommands: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    CancelCommandName: str = ...
    DeleteCommandName: str = ...
    EditCommandName: str = ...
    FirstPageCommandArgument: str = ...
    InsertCommandName: str = ...
    LastPageCommandArgument: str = ...
    NewCommandName: str = ...
    NextPageCommandArgument: str = ...
    PageCommandName: str = ...
    PreviousPageCommandArgument: str = ...
    SelectCommandName: str = ...
    SortCommandName: str = ...
    UpdateCommandName: str = ...


class TableCell(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TableCell() """
    @property
    def AssociatedHeaderCellID(self) -> Array:
        """
        Get: AssociatedHeaderCellID(self: TableCell) -> Array[str]
        Set: AssociatedHeaderCellID(self: TableCell) = value
        """
        ...

    @property
    def ColumnSpan(self) -> int:
        """
        Get: ColumnSpan(self: TableCell) -> int
        Set: ColumnSpan(self: TableCell) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: TableCell) -> HorizontalAlign
        Set: HorizontalAlign(self: TableCell) = value
        """
        ...

    @property
    def RowSpan(self) -> int:
        """
        Get: RowSpan(self: TableCell) -> int
        Set: RowSpan(self: TableCell) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TableCell) -> str
        Set: Text(self: TableCell) = value
        """
        ...

    @property
    def VerticalAlign(self): # -> VerticalAlign
        """
        Get: VerticalAlign(self: TableCell) -> VerticalAlign
        Set: VerticalAlign(self: TableCell) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: TableCell) -> bool
        Set: Wrap(self: TableCell) = value
        """
        ...



class DataControlFieldCell(TableCell): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataControlFieldCell(containingField: DataControlField) """
    @property
    def ContainingField(self) -> DataControlField:
        """ Get: ContainingField(self: DataControlFieldCell) -> DataControlField """
        ...

    @property
    def ValidateRequestMode(self) -> ValidateRequestMode:
        """
        Get: ValidateRequestMode(self: DataControlFieldCell) -> ValidateRequestMode
        Set: ValidateRequestMode(self: DataControlFieldCell) = value
        """
        ...


    def __new__(cls, containingField:DataControlField) -> Self:
        """
        __new__(cls: type, containingField: DataControlField)
        __new__(cls: type, tagKey: HtmlTextWriterTag, containingField: DataControlField)
        """
        ...


class DataControlFieldCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataControlFieldCollection() """
    def Add(self, field:DataControlField): # -> 
        """ Add(self: DataControlFieldCollection, field: DataControlField) """
        ...

    def CloneFields(self) -> DataControlFieldCollection:
        """ CloneFields(self: DataControlFieldCollection) -> DataControlFieldCollection """
        ...

    def Contains(self, field:DataControlField) -> bool:
        """ Contains(self: DataControlFieldCollection, field: DataControlField) -> bool """
        ...

    def IndexOf(self, field:DataControlField) -> int:
        """ IndexOf(self: DataControlFieldCollection, field: DataControlField) -> int """
        ...

    def Insert(self, index:int, field:DataControlField): # -> 
        """ Insert(self: DataControlFieldCollection, index: int, field: DataControlField) """
        ...

    def Remove(self, field:DataControlField): # -> 
        """ Remove(self: DataControlFieldCollection, field: DataControlField) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataControlFieldCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    FieldsChanged = ...


class DataControlFieldHeaderCell(DataControlFieldCell): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataControlFieldHeaderCell(containingField: DataControlField) """
    @property
    def AbbreviatedText(self) -> str:
        """
        Get: AbbreviatedText(self: DataControlFieldHeaderCell) -> str
        Set: AbbreviatedText(self: DataControlFieldHeaderCell) = value
        """
        ...

    @property
    def Scope(self): # -> TableHeaderScope
        """
        Get: Scope(self: DataControlFieldHeaderCell) -> TableHeaderScope
        Set: Scope(self: DataControlFieldHeaderCell) = value
        """
        ...



class DataControlRowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataControlRowState, values: Alternate (1), Edit (4), Insert (8), Normal (0), Selected (2) """
    Alternate: DataControlRowState = ...
    Edit: DataControlRowState = ...
    Insert: DataControlRowState = ...
    Normal: DataControlRowState = ...
    Selected: DataControlRowState = ...
    value__ = ...


class DataControlRowType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataControlRowType, values: DataRow (2), EmptyDataRow (5), Footer (1), Header (0), Pager (4), Separator (3) """
    DataRow: DataControlRowType = ...
    EmptyDataRow: DataControlRowType = ...
    Footer: DataControlRowType = ...
    Header: DataControlRowType = ...
    Pager: DataControlRowType = ...
    Separator: DataControlRowType = ...
    value__ = ...


class DataGrid(INamingContainer, BaseDataList): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataGrid() """
    @property
    def AllowCustomPaging(self) -> bool:
        """
        Get: AllowCustomPaging(self: DataGrid) -> bool
        Set: AllowCustomPaging(self: DataGrid) = value
        """
        ...

    @property
    def AllowPaging(self) -> bool:
        """
        Get: AllowPaging(self: DataGrid) -> bool
        Set: AllowPaging(self: DataGrid) = value
        """
        ...

    @property
    def AllowSorting(self) -> bool:
        """
        Get: AllowSorting(self: DataGrid) -> bool
        Set: AllowSorting(self: DataGrid) = value
        """
        ...

    @property
    def AlternatingItemStyle(self): # -> TableItemStyle
        """ Get: AlternatingItemStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def AutoGenerateColumns(self) -> bool:
        """
        Get: AutoGenerateColumns(self: DataGrid) -> bool
        Set: AutoGenerateColumns(self: DataGrid) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: DataGrid) -> str
        Set: BackImageUrl(self: DataGrid) = value
        """
        ...

    @property
    def Columns(self): # -> DataGridColumnCollection
        """ Get: Columns(self: DataGrid) -> DataGridColumnCollection """
        ...

    @property
    def CurrentPageIndex(self) -> int:
        """
        Get: CurrentPageIndex(self: DataGrid) -> int
        Set: CurrentPageIndex(self: DataGrid) = value
        """
        ...

    @property
    def EditItemIndex(self) -> int:
        """
        Get: EditItemIndex(self: DataGrid) -> int
        Set: EditItemIndex(self: DataGrid) = value
        """
        ...

    @property
    def EditItemStyle(self): # -> TableItemStyle
        """ Get: EditItemStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def FooterStyle(self): # -> TableItemStyle
        """ Get: FooterStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def HeaderStyle(self): # -> TableItemStyle
        """ Get: HeaderStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def Items(self): # -> DataGridItemCollection
        """ Get: Items(self: DataGrid) -> DataGridItemCollection """
        ...

    @property
    def ItemStyle(self): # -> TableItemStyle
        """ Get: ItemStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: DataGrid) -> int """
        ...

    @property
    def PagerStyle(self): # -> DataGridPagerStyle
        """ Get: PagerStyle(self: DataGrid) -> DataGridPagerStyle """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: DataGrid) -> int
        Set: PageSize(self: DataGrid) = value
        """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: DataGrid) -> int
        Set: SelectedIndex(self: DataGrid) = value
        """
        ...

    @property
    def SelectedItem(self): # -> DataGridItem
        """ Get: SelectedItem(self: DataGrid) -> DataGridItem """
        ...

    @property
    def SelectedItemStyle(self): # -> TableItemStyle
        """ Get: SelectedItemStyle(self: DataGrid) -> TableItemStyle """
        ...

    @property
    def ShowFooter(self) -> bool:
        """
        Get: ShowFooter(self: DataGrid) -> bool
        Set: ShowFooter(self: DataGrid) = value
        """
        ...

    @property
    def ShowHeader(self) -> bool:
        """
        Get: ShowHeader(self: DataGrid) -> bool
        Set: ShowHeader(self: DataGrid) = value
        """
        ...

    @property
    def VirtualItemCount(self) -> int:
        """
        Get: VirtualItemCount(self: DataGrid) -> int
        Set: VirtualItemCount(self: DataGrid) = value
        """
        ...


    def CreateColumnSet(self, *args): #cannot find CLR method
        """ CreateColumnSet(self: DataGrid, dataSource: PagedDataSource, useDataSource: bool) -> ArrayList """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: DataGrid, itemIndex: int, dataSourceIndex: int, itemType: ListItemType) -> DataGridItem """
        ...

    def InitializeItem(self, *args): #cannot find CLR method
        """ InitializeItem(self: DataGrid, item: DataGridItem, columns: Array[DataGridColumn]) """
        ...

    def InitializePager(self, *args): #cannot find CLR method
        """ InitializePager(self: DataGrid, item: DataGridItem, columnSpan: int, pagedDataSource: PagedDataSource) """
        ...

    def OnCancelCommand(self, *args): #cannot find CLR method
        """ OnCancelCommand(self: DataGrid, e: DataGridCommandEventArgs) """
        ...

    def OnDeleteCommand(self, *args): #cannot find CLR method
        """ OnDeleteCommand(self: DataGrid, e: DataGridCommandEventArgs) """
        ...

    def OnEditCommand(self, *args): #cannot find CLR method
        """ OnEditCommand(self: DataGrid, e: DataGridCommandEventArgs) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: DataGrid, e: DataGridCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: DataGrid, e: DataGridItemEventArgs) """
        ...

    def OnItemDataBound(self, *args): #cannot find CLR method
        """ OnItemDataBound(self: DataGrid, e: DataGridItemEventArgs) """
        ...

    def OnPageIndexChanged(self, *args): #cannot find CLR method
        """ OnPageIndexChanged(self: DataGrid, e: DataGridPageChangedEventArgs) """
        ...

    def OnSortCommand(self, *args): #cannot find CLR method
        """ OnSortCommand(self: DataGrid, e: DataGridSortCommandEventArgs) """
        ...

    def OnUpdateCommand(self, *args): #cannot find CLR method
        """ OnUpdateCommand(self: DataGrid, e: DataGridCommandEventArgs) """
        ...

    CancelCommand = ...
    CancelCommandName: str = ...
    DeleteCommand = ...
    DeleteCommandName: str = ...
    EditCommand = ...
    EditCommandName: str = ...
    ItemCommand = ...
    ItemCreated = ...
    ItemDataBound = ...
    NextPageCommandArgument: str = ...
    PageCommandName: str = ...
    PageIndexChanged = ...
    PrevPageCommandArgument: str = ...
    SelectCommandName: str = ...
    SortCommand = ...
    SortCommandName: str = ...
    UpdateCommand = ...
    UpdateCommandName: str = ...


class DataGridColumnCollection(IStateManager, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataGridColumnCollection(owner: DataGrid, columns: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataGridColumnCollection) -> bool """
        ...


    def Add(self, column:DataGridColumn): # -> 
        """ Add(self: DataGridColumnCollection, column: DataGridColumn) """
        ...

    def AddAt(self, index:int, column:DataGridColumn): # -> 
        """ AddAt(self: DataGridColumnCollection, index: int, column: DataGridColumn) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataGridColumnCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataGridColumnCollection) -> IEnumerator """
        ...

    def IndexOf(self, column:DataGridColumn) -> int:
        """ IndexOf(self: DataGridColumnCollection, column: DataGridColumn) -> int """
        ...

    def Remove(self, column:DataGridColumn): # -> 
        """ Remove(self: DataGridColumnCollection, column: DataGridColumn) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataGridColumnCollection, index: int) """
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


class DataGridCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ DataGridCommandEventArgs(item: DataGridItem, commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DataGridCommandEventArgs) -> object """
        ...

    @property
    def Item(self): # -> DataGridItem
        """ Get: Item(self: DataGridCommandEventArgs) -> DataGridItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataGridCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataGridCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:DataGridCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataGridCommandEventHandler, source: object, e: DataGridCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataGridCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:DataGridCommandEventArgs): # -> 
        """ Invoke(self: DataGridCommandEventHandler, source: object, e: DataGridCommandEventArgs) """
        ...


class TableRow(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TableRow() """
    @property
    def Cells(self): # -> TableCellCollection
        """ Get: Cells(self: TableRow) -> TableCellCollection """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: TableRow) -> HorizontalAlign
        Set: HorizontalAlign(self: TableRow) = value
        """
        ...

    @property
    def TableSection(self): # -> TableRowSection
        """
        Get: TableSection(self: TableRow) -> TableRowSection
        Set: TableSection(self: TableRow) = value
        """
        ...

    @property
    def VerticalAlign(self): # -> VerticalAlign
        """
        Get: VerticalAlign(self: TableRow) -> VerticalAlign
        Set: VerticalAlign(self: TableRow) = value
        """
        ...


    def CellControlCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class DataGridItem(TableRow, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ DataGridItem(itemIndex: int, dataSetIndex: int, itemType: ListItemType) """
    @property
    def DataSetIndex(self) -> int:
        """ Get: DataSetIndex(self: DataGridItem) -> int """
        ...

    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: DataGridItem) -> int """
        ...

    @property
    def ItemType(self): # -> ListItemType
        """ Get: ItemType(self: DataGridItem) -> ListItemType """
        ...


    def SetItemType(self, *args): #cannot find CLR method
        """ SetItemType(self: DataGridItem, itemType: ListItemType) """
        ...

    def __new__(cls, itemIndex:int, dataSetIndex:int, itemType) -> Self: # Not found arg types: {'itemType': 'ListItemType'}
        """ __new__(cls: type, itemIndex: int, dataSetIndex: int, itemType: ListItemType) """
        ...


class DataGridItemCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataGridItemCollection(items: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataGridItemCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataGridItemCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DataGridItemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataGridItemEventArgs(item: DataGridItem) """
    @property
    def Item(self) -> DataGridItem:
        """ Get: Item(self: DataGridItemEventArgs) -> DataGridItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, item:DataGridItem) -> Self:
        """ __new__(cls: type, item: DataGridItem) """
        ...


class DataGridItemEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataGridItemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataGridItemEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataGridItemEventHandler, sender: object, e: DataGridItemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataGridItemEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataGridItemEventArgs): # -> 
        """ Invoke(self: DataGridItemEventHandler, sender: object, e: DataGridItemEventArgs) """
        ...


class DataGridPageChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataGridPageChangedEventArgs(commandSource: object, newPageIndex: int) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DataGridPageChangedEventArgs) -> object """
        ...

    @property
    def NewPageIndex(self) -> int:
        """ Get: NewPageIndex(self: DataGridPageChangedEventArgs) -> int """
        ...


    def __new__(cls, commandSource:object, newPageIndex:int) -> Self:
        """ __new__(cls: type, commandSource: object, newPageIndex: int) """
        ...


class DataGridPageChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataGridPageChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:DataGridPageChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataGridPageChangedEventHandler, source: object, e: DataGridPageChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataGridPageChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:DataGridPageChangedEventArgs): # -> 
        """ Invoke(self: DataGridPageChangedEventHandler, source: object, e: DataGridPageChangedEventArgs) """
        ...


class Style(IStateManager, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    Style()
    Style(bag: StateBag)
    """
    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: Style) -> Color
        Set: BackColor(self: Style) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: Style) -> Color
        Set: BorderColor(self: Style) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: Style) -> BorderStyle
        Set: BorderStyle(self: Style) = value
        """
        ...

    @property
    def BorderWidth(self): # -> Unit
        """
        Get: BorderWidth(self: Style) -> Unit
        Set: BorderWidth(self: Style) = value
        """
        ...

    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: Style) -> str
        Set: CssClass(self: Style) = value
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
    def Height(self): # -> Unit
        """
        Get: Height(self: Style) -> Unit
        Set: Height(self: Style) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Style) -> bool """
        ...

    @property
    def RegisteredCssClass(self) -> str:
        """ Get: RegisteredCssClass(self: Style) -> str """
        ...

    @property
    def ViewState(self):
        ...

    @property
    def Width(self): # -> Unit
        """
        Get: Width(self: Style) -> Unit
        Set: Width(self: Style) = value
        """
        ...


    def AddAttributesToRender(self, writer:HtmlTextWriter, owner:WebControl = ...): # -> 
        """ AddAttributesToRender(self: Style, writer: HtmlTextWriter)AddAttributesToRender(self: Style, writer: HtmlTextWriter, owner: WebControl) """
        ...

    def CopyFrom(self, s:Style): # -> 
        """ CopyFrom(self: Style, s: Style) """
        ...

    def FillStyleAttributes(self, *args): #cannot find CLR method
        """ FillStyleAttributes(self: Style, attributes: CssStyleCollection, urlResolver: IUrlResolutionService) """
        ...

    def GetStyleAttributes(self, urlResolver:IUrlResolutionService) -> CssStyleCollection:
        """ GetStyleAttributes(self: Style, urlResolver: IUrlResolutionService) -> CssStyleCollection """
        ...

    def MergeWith(self, s:Style): # -> 
        """ MergeWith(self: Style, s: Style) """
        ...

    def Reset(self): # -> 
        """ Reset(self: Style) """
        ...

    def SetBit(self, *args): #cannot find CLR method
        """ SetBit(self: Style, bit: int) """
        ...

    def SetDirty(self): # -> 
        """ SetDirty(self: Style) """
        ...

    def __new__(cls, bag:StateBag = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, bag: StateBag)
        """
        ...


class TableItemStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    TableItemStyle()
    TableItemStyle(bag: StateBag)
    """
    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: TableItemStyle) -> HorizontalAlign
        Set: HorizontalAlign(self: TableItemStyle) = value
        """
        ...

    @property
    def VerticalAlign(self): # -> VerticalAlign
        """
        Get: VerticalAlign(self: TableItemStyle) -> VerticalAlign
        Set: VerticalAlign(self: TableItemStyle) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: TableItemStyle) -> bool
        Set: Wrap(self: TableItemStyle) = value
        """
        ...



class DataGridPagerStyle(TableItemStyle): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def Mode(self): # -> PagerMode
        """
        Get: Mode(self: DataGridPagerStyle) -> PagerMode
        Set: Mode(self: DataGridPagerStyle) = value
        """
        ...

    @property
    def NextPageText(self) -> str:
        """
        Get: NextPageText(self: DataGridPagerStyle) -> str
        Set: NextPageText(self: DataGridPagerStyle) = value
        """
        ...

    @property
    def PageButtonCount(self) -> int:
        """
        Get: PageButtonCount(self: DataGridPagerStyle) -> int
        Set: PageButtonCount(self: DataGridPagerStyle) = value
        """
        ...

    @property
    def Position(self): # -> PagerPosition
        """
        Get: Position(self: DataGridPagerStyle) -> PagerPosition
        Set: Position(self: DataGridPagerStyle) = value
        """
        ...

    @property
    def PrevPageText(self) -> str:
        """
        Get: PrevPageText(self: DataGridPagerStyle) -> str
        Set: PrevPageText(self: DataGridPagerStyle) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: DataGridPagerStyle) -> bool
        Set: Visible(self: DataGridPagerStyle) = value
        """
        ...



class DataGridSortCommandEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataGridSortCommandEventArgs(commandSource: object, dce: DataGridCommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DataGridSortCommandEventArgs) -> object """
        ...

    @property
    def SortExpression(self) -> str:
        """ Get: SortExpression(self: DataGridSortCommandEventArgs) -> str """
        ...


    def __new__(cls, commandSource:object, dce:DataGridCommandEventArgs) -> Self:
        """ __new__(cls: type, commandSource: object, dce: DataGridCommandEventArgs) """
        ...


class DataGridSortCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataGridSortCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:DataGridSortCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataGridSortCommandEventHandler, source: object, e: DataGridSortCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataGridSortCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:DataGridSortCommandEventArgs): # -> 
        """ Invoke(self: DataGridSortCommandEventHandler, source: object, e: DataGridSortCommandEventArgs) """
        ...


class DataKey(IStateManager, IEquatable): # skipped bases: <type 'object'>
    """
    DataKey(keyTable: IOrderedDictionary)
    DataKey(keyTable: IOrderedDictionary, keyNames: Array[str])
    """
    @property
    def Value(self) -> object:
        """ Get: Value(self: DataKey) -> object """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: DataKey) -> IOrderedDictionary """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class DataKeyArray(IStateManager, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataKeyArray(keys: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataKeyArray) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataKeyArray) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DataKeyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataKeyCollection(keys: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataKeyCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataKeyCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DataList(INamingContainer, IRepeatInfoUser, IWizardSideBarListControl, BaseDataList): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataList() """
    @property
    def AlternatingItemStyle(self) -> TableItemStyle:
        """ Get: AlternatingItemStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def AlternatingItemTemplate(self) -> ITemplate:
        """
        Get: AlternatingItemTemplate(self: DataList) -> ITemplate
        Set: AlternatingItemTemplate(self: DataList) = value
        """
        ...

    @property
    def EditItemIndex(self) -> int:
        """
        Get: EditItemIndex(self: DataList) -> int
        Set: EditItemIndex(self: DataList) = value
        """
        ...

    @property
    def EditItemStyle(self) -> TableItemStyle:
        """ Get: EditItemStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def EditItemTemplate(self) -> ITemplate:
        """
        Get: EditItemTemplate(self: DataList) -> ITemplate
        Set: EditItemTemplate(self: DataList) = value
        """
        ...

    @property
    def ExtractTemplateRows(self) -> bool:
        """
        Get: ExtractTemplateRows(self: DataList) -> bool
        Set: ExtractTemplateRows(self: DataList) = value
        """
        ...

    @property
    def FooterStyle(self) -> TableItemStyle:
        """ Get: FooterStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: DataList) -> ITemplate
        Set: FooterTemplate(self: DataList) = value
        """
        ...

    @property
    def HeaderStyle(self) -> TableItemStyle:
        """ Get: HeaderStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: DataList) -> ITemplate
        Set: HeaderTemplate(self: DataList) = value
        """
        ...

    @property
    def Items(self): # -> DataListItemCollection
        """ Get: Items(self: DataList) -> DataListItemCollection """
        ...

    @property
    def ItemStyle(self) -> TableItemStyle:
        """ Get: ItemStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: DataList) -> ITemplate
        Set: ItemTemplate(self: DataList) = value
        """
        ...

    @property
    def RepeatColumns(self) -> int:
        """
        Get: RepeatColumns(self: DataList) -> int
        Set: RepeatColumns(self: DataList) = value
        """
        ...

    @property
    def RepeatDirection(self): # -> RepeatDirection
        """
        Get: RepeatDirection(self: DataList) -> RepeatDirection
        Set: RepeatDirection(self: DataList) = value
        """
        ...

    @property
    def RepeatLayout(self): # -> RepeatLayout
        """
        Get: RepeatLayout(self: DataList) -> RepeatLayout
        Set: RepeatLayout(self: DataList) = value
        """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: DataList) -> int
        Set: SelectedIndex(self: DataList) = value
        """
        ...

    @property
    def SelectedItem(self): # -> DataListItem
        """ Get: SelectedItem(self: DataList) -> DataListItem """
        ...

    @property
    def SelectedItemStyle(self) -> TableItemStyle:
        """ Get: SelectedItemStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def SelectedItemTemplate(self) -> ITemplate:
        """
        Get: SelectedItemTemplate(self: DataList) -> ITemplate
        Set: SelectedItemTemplate(self: DataList) = value
        """
        ...

    @property
    def SelectedValue(self) -> object:
        """ Get: SelectedValue(self: DataList) -> object """
        ...

    @property
    def SeparatorStyle(self) -> TableItemStyle:
        """ Get: SeparatorStyle(self: DataList) -> TableItemStyle """
        ...

    @property
    def SeparatorTemplate(self) -> ITemplate:
        """
        Get: SeparatorTemplate(self: DataList) -> ITemplate
        Set: SeparatorTemplate(self: DataList) = value
        """
        ...

    @property
    def ShowFooter(self) -> bool:
        """
        Get: ShowFooter(self: DataList) -> bool
        Set: ShowFooter(self: DataList) = value
        """
        ...

    @property
    def ShowHeader(self) -> bool:
        """
        Get: ShowHeader(self: DataList) -> bool
        Set: ShowHeader(self: DataList) = value
        """
        ...


    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: DataList, itemIndex: int, itemType: ListItemType) -> DataListItem """
        ...

    def InitializeItem(self, *args): #cannot find CLR method
        """ InitializeItem(self: DataList, item: DataListItem) """
        ...

    def OnCancelCommand(self, *args): #cannot find CLR method
        """ OnCancelCommand(self: DataList, e: DataListCommandEventArgs) """
        ...

    def OnDeleteCommand(self, *args): #cannot find CLR method
        """ OnDeleteCommand(self: DataList, e: DataListCommandEventArgs) """
        ...

    def OnEditCommand(self, *args): #cannot find CLR method
        """ OnEditCommand(self: DataList, e: DataListCommandEventArgs) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: DataList, e: DataListCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: DataList, e: DataListItemEventArgs) """
        ...

    def OnItemDataBound(self, *args): #cannot find CLR method
        """ OnItemDataBound(self: DataList, e: DataListItemEventArgs) """
        ...

    def OnUpdateCommand(self, *args): #cannot find CLR method
        """ OnUpdateCommand(self: DataList, e: DataListCommandEventArgs) """
        ...

    CancelCommand = ...
    CancelCommandName: str = ...
    DeleteCommand = ...
    DeleteCommandName: str = ...
    EditCommand = ...
    EditCommandName: str = ...
    ItemCommand = ...
    ItemCreated = ...
    ItemDataBound = ...
    SelectCommandName: str = ...
    UpdateCommand = ...
    UpdateCommandName: str = ...


class DataListCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ DataListCommandEventArgs(item: DataListItem, commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DataListCommandEventArgs) -> object """
        ...

    @property
    def Item(self): # -> DataListItem
        """ Get: Item(self: DataListCommandEventArgs) -> DataListItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataListCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataListCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:DataListCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataListCommandEventHandler, source: object, e: DataListCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataListCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:DataListCommandEventArgs): # -> 
        """ Invoke(self: DataListCommandEventHandler, source: object, e: DataListCommandEventArgs) """
        ...


class DataListItem(WebControl, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ DataListItem(itemIndex: int, itemType: ListItemType) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: DataListItem) -> int """
        ...

    @property
    def ItemType(self): # -> ListItemType
        """ Get: ItemType(self: DataListItem) -> ListItemType """
        ...


    def RenderItem(self, writer:HtmlTextWriter, extractRows:bool, tableLayout:bool): # -> 
        """ RenderItem(self: DataListItem, writer: HtmlTextWriter, extractRows: bool, tableLayout: bool) """
        ...

    def SetItemType(self, *args): #cannot find CLR method
        """ SetItemType(self: DataListItem, itemType: ListItemType) """
        ...


class DataListItemCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataListItemCollection(items: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataListItemCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataListItemCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DataListItemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataListItemEventArgs(item: DataListItem) """
    @property
    def Item(self) -> DataListItem:
        """ Get: Item(self: DataListItemEventArgs) -> DataListItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, item:DataListItem) -> Self:
        """ __new__(cls: type, item: DataListItem) """
        ...


class DataListItemEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataListItemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataListItemEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataListItemEventHandler, sender: object, e: DataListItemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataListItemEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataListItemEventArgs): # -> 
        """ Invoke(self: DataListItemEventHandler, sender: object, e: DataListItemEventArgs) """
        ...


class DataPager(IAttributeAccessor, Control, INamingContainer, ICompositeControlDesignerAccessor): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataPager() """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: DataPager) -> AttributeCollection """
        ...

    @property
    def Fields(self) -> DataPagerFieldCollection:
        """ Get: Fields(self: DataPager) -> DataPagerFieldCollection """
        ...

    @property
    def MaximumRows(self) -> int:
        """ Get: MaximumRows(self: DataPager) -> int """
        ...

    @property
    def PagedControlID(self) -> str:
        """
        Get: PagedControlID(self: DataPager) -> str
        Set: PagedControlID(self: DataPager) = value
        """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: DataPager) -> int
        Set: PageSize(self: DataPager) = value
        """
        ...

    @property
    def QueryStringField(self) -> str:
        """
        Get: QueryStringField(self: DataPager) -> str
        Set: QueryStringField(self: DataPager) = value
        """
        ...

    @property
    def StartRowIndex(self) -> int:
        """ Get: StartRowIndex(self: DataPager) -> int """
        ...

    @property
    def TagKey(self):
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: DataPager) -> int """
        ...


    def AddAttributesToRender(self, *args): #cannot find CLR method
        """ AddAttributesToRender(self: DataPager, writer: HtmlTextWriter) """
        ...

    def ConnectToEvents(self, *args): #cannot find CLR method
        """ ConnectToEvents(self: DataPager, container: IPageableItemContainer) """
        ...

    def CreatePagerFields(self, *args): #cannot find CLR method
        """ CreatePagerFields(self: DataPager) """
        ...

    def FindPageableItemContainer(self, *args): #cannot find CLR method
        """ FindPageableItemContainer(self: DataPager) -> IPageableItemContainer """
        ...

    def OnTotalRowCountAvailable(self, *args): #cannot find CLR method
        """ OnTotalRowCountAvailable(self: DataPager, sender: object, e: PageEventArgs) """
        ...

    def RenderBeginTag(self, writer:HtmlTextWriter): # -> 
        """ RenderBeginTag(self: DataPager, writer: HtmlTextWriter) """
        ...

    def RenderContents(self, *args): #cannot find CLR method
        """ RenderContents(self: DataPager, writer: HtmlTextWriter) """
        ...

    def SetPageProperties(self, startRowIndex:int, maximumRows:int, databind:bool): # -> 
        """ SetPageProperties(self: DataPager, startRowIndex: int, maximumRows: int, databind: bool) """
        ...


class DataPagerCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ DataPagerCommandEventArgs(pagerField: DataPagerField, totalRowCount: int, originalArgs: CommandEventArgs, item: DataPagerFieldItem) """
    @property
    def Item(self) -> DataPagerFieldItem:
        """ Get: Item(self: DataPagerCommandEventArgs) -> DataPagerFieldItem """
        ...

    @property
    def NewMaximumRows(self) -> int:
        """
        Get: NewMaximumRows(self: DataPagerCommandEventArgs) -> int
        Set: NewMaximumRows(self: DataPagerCommandEventArgs) = value
        """
        ...

    @property
    def NewStartRowIndex(self) -> int:
        """
        Get: NewStartRowIndex(self: DataPagerCommandEventArgs) -> int
        Set: NewStartRowIndex(self: DataPagerCommandEventArgs) = value
        """
        ...

    @property
    def PagerField(self) -> DataPagerField:
        """ Get: PagerField(self: DataPagerCommandEventArgs) -> DataPagerField """
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: DataPagerCommandEventArgs) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataPagerField(IStateManager): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataPager(self):
        ...

    @property
    def QueryStringHandled(self):
        ...

    @property
    def QueryStringValue(self):
        ...

    @property
    def ViewState(self):
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: DataPagerField) -> bool
        Set: Visible(self: DataPagerField) = value
        """
        ...


    def CloneField(self, *args): #cannot find CLR method
        """ CloneField(self: DataPagerField) -> DataPagerField """
        ...

    def CopyProperties(self, *args): #cannot find CLR method
        """ CopyProperties(self: DataPagerField, newField: DataPagerField) """
        ...

    def CreateDataPagers(self, container:DataPagerFieldItem, startRowIndex:int, maximumRows:int, totalRowCount:int, fieldIndex:int): # -> 
        """ CreateDataPagers(self: DataPagerField, container: DataPagerFieldItem, startRowIndex: int, maximumRows: int, totalRowCount: int, fieldIndex: int) """
        ...

    def CreateField(self, *args): #cannot find CLR method
        """ CreateField(self: DataPagerField) -> DataPagerField """
        ...

    def GetQueryStringNavigateUrl(self, *args): #cannot find CLR method
        """ GetQueryStringNavigateUrl(self: DataPagerField, pageNumber: int) -> str """
        ...

    def HandleEvent(self, e:CommandEventArgs): # -> 
        """ HandleEvent(self: DataPagerField, e: CommandEventArgs) """
        ...

    def OnFieldChanged(self, *args): #cannot find CLR method
        """ OnFieldChanged(self: DataPagerField) """
        ...


class DataPagerFieldCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataPagerFieldCollection(dataPager: DataPager) """
    def Add(self, field:DataPagerField): # -> 
        """ Add(self: DataPagerFieldCollection, field: DataPagerField) """
        ...

    def CloneFields(self, pager:DataPager) -> DataPagerFieldCollection:
        """ CloneFields(self: DataPagerFieldCollection, pager: DataPager) -> DataPagerFieldCollection """
        ...

    def Contains(self, field:DataPagerField) -> bool:
        """ Contains(self: DataPagerFieldCollection, field: DataPagerField) -> bool """
        ...

    def IndexOf(self, field:DataPagerField) -> int:
        """ IndexOf(self: DataPagerFieldCollection, field: DataPagerField) -> int """
        ...

    def Insert(self, index:int, field:DataPagerField): # -> 
        """ Insert(self: DataPagerFieldCollection, index: int, field: DataPagerField) """
        ...

    def Remove(self, field:DataPagerField): # -> 
        """ Remove(self: DataPagerFieldCollection, field: DataPagerField) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataPagerFieldCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, dataPager:DataPager) -> Self:
        """ __new__(cls: type, dataPager: DataPager) """
        ...

    FieldsChanged = ...


class DataPagerFieldCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ DataPagerFieldCommandEventArgs(item: DataPagerFieldItem, commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DataPagerFieldCommandEventArgs) -> object """
        ...

    @property
    def Item(self) -> DataPagerFieldItem:
        """ Get: Item(self: DataPagerFieldCommandEventArgs) -> DataPagerFieldItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataPagerFieldItem(Control, INonBindingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ DataPagerFieldItem(field: DataPagerField, pager: DataPager) """
    @property
    def Pager(self) -> DataPager:
        """ Get: Pager(self: DataPagerFieldItem) -> DataPager """
        ...

    @property
    def PagerField(self) -> DataPagerField:
        """ Get: PagerField(self: DataPagerFieldItem) -> DataPagerField """
        ...


    def __new__(cls, field:DataPagerField, pager:DataPager) -> Self:
        """ __new__(cls: type, field: DataPagerField, pager: DataPager) """
        ...


class DataSourceSelectResultProcessingOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ DataSourceSelectResultProcessingOptions() """
    @property
    def AutoPage(self) -> bool:
        """
        Get: AutoPage(self: DataSourceSelectResultProcessingOptions) -> bool
        Set: AutoPage(self: DataSourceSelectResultProcessingOptions) = value
        """
        ...

    @property
    def AutoSort(self) -> bool:
        """
        Get: AutoSort(self: DataSourceSelectResultProcessingOptions) -> bool
        Set: AutoSort(self: DataSourceSelectResultProcessingOptions) = value
        """
        ...

    @property
    def ModelType(self) -> Type:
        """
        Get: ModelType(self: DataSourceSelectResultProcessingOptions) -> Type
        Set: ModelType(self: DataSourceSelectResultProcessingOptions) = value
        """
        ...



class DayNameFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DayNameFormat, values: FirstLetter (2), FirstTwoLetters (3), Full (0), Short (1), Shortest (4) """
    FirstLetter: DayNameFormat = ...
    FirstTwoLetters: DayNameFormat = ...
    Full: DayNameFormat = ...
    Short: DayNameFormat = ...
    Shortest: DayNameFormat = ...
    value__ = ...


class DayRenderEventArgs: # skipped bases: <type 'object'>, <type 'object'>
    """
    DayRenderEventArgs(cell: TableCell, day: CalendarDay)
    DayRenderEventArgs(cell: TableCell, day: CalendarDay, selectUrl: str)
    """
    @property
    def Cell(self) -> TableCell:
        """ Get: Cell(self: DayRenderEventArgs) -> TableCell """
        ...

    @property
    def Day(self) -> CalendarDay:
        """ Get: Day(self: DayRenderEventArgs) -> CalendarDay """
        ...

    @property
    def SelectUrl(self) -> str:
        """ Get: SelectUrl(self: DayRenderEventArgs) -> str """
        ...



class DayRenderEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DayRenderEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DayRenderEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DayRenderEventHandler, sender: object, e: DayRenderEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DayRenderEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DayRenderEventArgs): # -> 
        """ Invoke(self: DayRenderEventHandler, sender: object, e: DayRenderEventArgs) """
        ...


class ICallbackContainer: # skipped bases: <type 'object'>
    """ no doc """
    def GetCallbackScript(self, buttonControl:IButtonControl, argument:str) -> str:
        """ GetCallbackScript(self: ICallbackContainer, buttonControl: IButtonControl, argument: str) -> str """
        ...


class IDataBoundControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataKeyNames(self) -> Array:
        """
        Get: DataKeyNames(self: IDataBoundControl) -> Array[str]
        Set: DataKeyNames(self: IDataBoundControl) = value
        """
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: IDataBoundControl) -> str
        Set: DataMember(self: IDataBoundControl) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: IDataBoundControl) -> object
        Set: DataSource(self: IDataBoundControl) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: IDataBoundControl) -> str
        Set: DataSourceID(self: IDataBoundControl) = value
        """
        ...

    @property
    def DataSourceObject(self) -> IDataSource:
        """ Get: DataSourceObject(self: IDataBoundControl) -> IDataSource """
        ...



class IDataBoundItemControl(IDataBoundControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataKey(self) -> DataKey:
        """ Get: DataKey(self: IDataBoundItemControl) -> DataKey """
        ...

    @property
    def Mode(self) -> DataBoundControlMode:
        """ Get: Mode(self: IDataBoundItemControl) -> DataBoundControlMode """
        ...



class IFieldControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FieldsGenerator(self) -> IAutoFieldGenerator:
        """
        Get: FieldsGenerator(self: IFieldControl) -> IAutoFieldGenerator
        Set: FieldsGenerator(self: IFieldControl) = value
        """
        ...



class IPostBackContainer: # skipped bases: <type 'object'>
    """ no doc """
    def GetPostBackOptions(self, buttonControl:IButtonControl) -> PostBackOptions:
        """ GetPostBackOptions(self: IPostBackContainer, buttonControl: IButtonControl) -> PostBackOptions """
        ...


class DetailsView(ICallbackContainer, ICallbackEventHandler, IFieldControl, IDataBoundItemControl, CompositeDataBoundControl, IPostBackContainer, IPostBackEventHandler, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IDataBoundControl'>, <type 'object'>
    """ DetailsView() """
    @property
    def AllowPaging(self) -> bool:
        """
        Get: AllowPaging(self: DetailsView) -> bool
        Set: AllowPaging(self: DetailsView) = value
        """
        ...

    @property
    def AlternatingRowStyle(self) -> TableItemStyle:
        """ Get: AlternatingRowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def AutoGenerateDeleteButton(self) -> bool:
        """
        Get: AutoGenerateDeleteButton(self: DetailsView) -> bool
        Set: AutoGenerateDeleteButton(self: DetailsView) = value
        """
        ...

    @property
    def AutoGenerateEditButton(self) -> bool:
        """
        Get: AutoGenerateEditButton(self: DetailsView) -> bool
        Set: AutoGenerateEditButton(self: DetailsView) = value
        """
        ...

    @property
    def AutoGenerateInsertButton(self) -> bool:
        """
        Get: AutoGenerateInsertButton(self: DetailsView) -> bool
        Set: AutoGenerateInsertButton(self: DetailsView) = value
        """
        ...

    @property
    def AutoGenerateRows(self) -> bool:
        """
        Get: AutoGenerateRows(self: DetailsView) -> bool
        Set: AutoGenerateRows(self: DetailsView) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: DetailsView) -> str
        Set: BackImageUrl(self: DetailsView) = value
        """
        ...

    @property
    def BottomPagerRow(self): # -> DetailsViewRow
        """ Get: BottomPagerRow(self: DetailsView) -> DetailsViewRow """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DetailsView) -> str
        Set: Caption(self: DetailsView) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: DetailsView) -> TableCaptionAlign
        Set: CaptionAlign(self: DetailsView) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: DetailsView) -> int
        Set: CellPadding(self: DetailsView) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: DetailsView) -> int
        Set: CellSpacing(self: DetailsView) = value
        """
        ...

    @property
    def CommandRowStyle(self) -> TableItemStyle:
        """ Get: CommandRowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def CurrentMode(self): # -> DetailsViewMode
        """ Get: CurrentMode(self: DetailsView) -> DetailsViewMode """
        ...

    @property
    def DataItemCount(self) -> int:
        """ Get: DataItemCount(self: DetailsView) -> int """
        ...

    @property
    def DataKeyNames(self) -> Array:
        """
        Get: DataKeyNames(self: DetailsView) -> Array[str]
        Set: DataKeyNames(self: DetailsView) = value
        """
        ...

    @property
    def DefaultMode(self): # -> DetailsViewMode
        """
        Get: DefaultMode(self: DetailsView) -> DetailsViewMode
        Set: DefaultMode(self: DetailsView) = value
        """
        ...

    @property
    def EditRowStyle(self) -> TableItemStyle:
        """ Get: EditRowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def EmptyDataRowStyle(self) -> TableItemStyle:
        """ Get: EmptyDataRowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def EmptyDataTemplate(self) -> ITemplate:
        """
        Get: EmptyDataTemplate(self: DetailsView) -> ITemplate
        Set: EmptyDataTemplate(self: DetailsView) = value
        """
        ...

    @property
    def EmptyDataText(self) -> str:
        """
        Get: EmptyDataText(self: DetailsView) -> str
        Set: EmptyDataText(self: DetailsView) = value
        """
        ...

    @property
    def EnableModelValidation(self) -> bool:
        """
        Get: EnableModelValidation(self: DetailsView) -> bool
        Set: EnableModelValidation(self: DetailsView) = value
        """
        ...

    @property
    def EnablePagingCallbacks(self) -> bool:
        """
        Get: EnablePagingCallbacks(self: DetailsView) -> bool
        Set: EnablePagingCallbacks(self: DetailsView) = value
        """
        ...

    @property
    def FieldHeaderStyle(self) -> TableItemStyle:
        """ Get: FieldHeaderStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def Fields(self) -> DataControlFieldCollection:
        """ Get: Fields(self: DetailsView) -> DataControlFieldCollection """
        ...

    @property
    def FooterRow(self): # -> DetailsViewRow
        """ Get: FooterRow(self: DetailsView) -> DetailsViewRow """
        ...

    @property
    def FooterStyle(self) -> TableItemStyle:
        """ Get: FooterStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: DetailsView) -> ITemplate
        Set: FooterTemplate(self: DetailsView) = value
        """
        ...

    @property
    def FooterText(self) -> str:
        """
        Get: FooterText(self: DetailsView) -> str
        Set: FooterText(self: DetailsView) = value
        """
        ...

    @property
    def GridLines(self): # -> GridLines
        """
        Get: GridLines(self: DetailsView) -> GridLines
        Set: GridLines(self: DetailsView) = value
        """
        ...

    @property
    def HeaderRow(self): # -> DetailsViewRow
        """ Get: HeaderRow(self: DetailsView) -> DetailsViewRow """
        ...

    @property
    def HeaderStyle(self) -> TableItemStyle:
        """ Get: HeaderStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: DetailsView) -> ITemplate
        Set: HeaderTemplate(self: DetailsView) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: DetailsView) -> str
        Set: HeaderText(self: DetailsView) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: DetailsView) -> HorizontalAlign
        Set: HorizontalAlign(self: DetailsView) = value
        """
        ...

    @property
    def InsertRowStyle(self) -> TableItemStyle:
        """ Get: InsertRowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: DetailsView) -> int """
        ...

    @property
    def PageIndex(self) -> int:
        """
        Get: PageIndex(self: DetailsView) -> int
        Set: PageIndex(self: DetailsView) = value
        """
        ...

    @property
    def PagerSettings(self): # -> PagerSettings
        """ Get: PagerSettings(self: DetailsView) -> PagerSettings """
        ...

    @property
    def PagerStyle(self) -> TableItemStyle:
        """ Get: PagerStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def PagerTemplate(self) -> ITemplate:
        """
        Get: PagerTemplate(self: DetailsView) -> ITemplate
        Set: PagerTemplate(self: DetailsView) = value
        """
        ...

    @property
    def Rows(self): # -> DetailsViewRowCollection
        """ Get: Rows(self: DetailsView) -> DetailsViewRowCollection """
        ...

    @property
    def RowsGenerator(self) -> IAutoFieldGenerator:
        """
        Get: RowsGenerator(self: DetailsView) -> IAutoFieldGenerator
        Set: RowsGenerator(self: DetailsView) = value
        """
        ...

    @property
    def RowStyle(self) -> TableItemStyle:
        """ Get: RowStyle(self: DetailsView) -> TableItemStyle """
        ...

    @property
    def SelectedValue(self) -> object:
        """ Get: SelectedValue(self: DetailsView) -> object """
        ...

    @property
    def TopPagerRow(self): # -> DetailsViewRow
        """ Get: TopPagerRow(self: DetailsView) -> DetailsViewRow """
        ...


    def ChangeMode(self, newMode): # ->  # Not found arg types: {'newMode': 'DetailsViewMode'}
        """ ChangeMode(self: DetailsView, newMode: DetailsViewMode) """
        ...

    def CreateAutoGeneratedRow(self, *args): #cannot find CLR method
        """ CreateAutoGeneratedRow(self: DetailsView, fieldProperties: AutoGeneratedFieldProperties) -> AutoGeneratedField """
        ...

    def CreateAutoGeneratedRows(self, *args): #cannot find CLR method
        """ CreateAutoGeneratedRows(self: DetailsView, dataItem: object) -> ICollection """
        ...

    def CreateFieldSet(self, *args): #cannot find CLR method
        """ CreateFieldSet(self: DetailsView, dataItem: object, useDataSource: bool) -> ICollection """
        ...

    def CreateRow(self, *args): #cannot find CLR method
        """ CreateRow(self: DetailsView, rowIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) -> DetailsViewRow """
        ...

    def CreateTable(self, *args): #cannot find CLR method
        """ CreateTable(self: DetailsView) -> Table """
        ...

    def DeleteItem(self): # -> 
        """ DeleteItem(self: DetailsView) """
        ...

    def ExtractRowValues(self, *args): #cannot find CLR method
        """ ExtractRowValues(self: DetailsView, fieldValues: IOrderedDictionary, includeReadOnlyFields: bool, includeKeys: bool) """
        ...

    def InitializePager(self, *args): #cannot find CLR method
        """ InitializePager(self: DetailsView, row: DetailsViewRow, pagedDataSource: PagedDataSource) """
        ...

    def InitializeRow(self, *args): #cannot find CLR method
        """ InitializeRow(self: DetailsView, row: DetailsViewRow, field: DataControlField) """
        ...

    def InsertItem(self, causesValidation:bool): # -> 
        """ InsertItem(self: DetailsView, causesValidation: bool) """
        ...

    def IsBindableType(self, type:Type) -> bool:
        """ IsBindableType(self: DetailsView, type: Type) -> bool """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: DetailsView, e: DetailsViewCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: DetailsView, e: EventArgs) """
        ...

    def OnItemDeleted(self, *args): #cannot find CLR method
        """ OnItemDeleted(self: DetailsView, e: DetailsViewDeletedEventArgs) """
        ...

    def OnItemDeleting(self, *args): #cannot find CLR method
        """ OnItemDeleting(self: DetailsView, e: DetailsViewDeleteEventArgs) """
        ...

    def OnItemInserted(self, *args): #cannot find CLR method
        """ OnItemInserted(self: DetailsView, e: DetailsViewInsertedEventArgs) """
        ...

    def OnItemInserting(self, *args): #cannot find CLR method
        """ OnItemInserting(self: DetailsView, e: DetailsViewInsertEventArgs) """
        ...

    def OnItemUpdated(self, *args): #cannot find CLR method
        """ OnItemUpdated(self: DetailsView, e: DetailsViewUpdatedEventArgs) """
        ...

    def OnItemUpdating(self, *args): #cannot find CLR method
        """ OnItemUpdating(self: DetailsView, e: DetailsViewUpdateEventArgs) """
        ...

    def OnModeChanged(self, *args): #cannot find CLR method
        """ OnModeChanged(self: DetailsView, e: EventArgs) """
        ...

    def OnModeChanging(self, *args): #cannot find CLR method
        """ OnModeChanging(self: DetailsView, e: DetailsViewModeEventArgs) """
        ...

    def OnPageIndexChanged(self, *args): #cannot find CLR method
        """ OnPageIndexChanged(self: DetailsView, e: EventArgs) """
        ...

    def OnPageIndexChanging(self, *args): #cannot find CLR method
        """ OnPageIndexChanging(self: DetailsView, e: DetailsViewPageEventArgs) """
        ...

    def PrepareControlHierarchy(self, *args): #cannot find CLR method
        """ PrepareControlHierarchy(self: DetailsView) """
        ...

    def SetPageIndex(self, index:int): # -> 
        """ SetPageIndex(self: DetailsView, index: int) """
        ...

    def UpdateItem(self, causesValidation:bool): # -> 
        """ UpdateItem(self: DetailsView, causesValidation: bool) """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        ...

    ItemCommand = ...
    ItemCreated = ...
    ItemDeleted = ...
    ItemDeleting = ...
    ItemInserted = ...
    ItemInserting = ...
    ItemUpdated = ...
    ItemUpdating = ...
    ModeChanged = ...
    ModeChanging = ...
    PageIndexChanged = ...
    PageIndexChanging = ...


class DetailsViewCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewCommandEventArgs(commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: DetailsViewCommandEventArgs) -> object """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: DetailsViewCommandEventArgs) -> bool
        Set: Handled(self: DetailsViewCommandEventArgs) = value
        """
        ...



class DetailsViewCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewCommandEventHandler, sender: object, e: DetailsViewCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewCommandEventArgs): # -> 
        """ Invoke(self: DetailsViewCommandEventHandler, sender: object, e: DetailsViewCommandEventArgs) """
        ...


class DetailsViewDeletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DetailsViewDeletedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: DetailsViewDeletedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: DetailsViewDeletedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: DetailsViewDeletedEventArgs) -> bool
        Set: ExceptionHandled(self: DetailsViewDeletedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: DetailsViewDeletedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: DetailsViewDeletedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class DetailsViewDeletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewDeletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewDeletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewDeletedEventHandler, sender: object, e: DetailsViewDeletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewDeletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewDeletedEventArgs): # -> 
        """ Invoke(self: DetailsViewDeletedEventHandler, sender: object, e: DetailsViewDeletedEventArgs) """
        ...


class DetailsViewDeleteEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewDeleteEventArgs(rowIndex: int) """
    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: DetailsViewDeleteEventArgs) -> IOrderedDictionary """
        ...

    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: DetailsViewDeleteEventArgs) -> int """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: DetailsViewDeleteEventArgs) -> IOrderedDictionary """
        ...



class DetailsViewDeleteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewDeleteEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewDeleteEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewDeleteEventHandler, sender: object, e: DetailsViewDeleteEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewDeleteEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewDeleteEventArgs): # -> 
        """ Invoke(self: DetailsViewDeleteEventHandler, sender: object, e: DetailsViewDeleteEventArgs) """
        ...


class DetailsViewInsertedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DetailsViewInsertedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: DetailsViewInsertedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: DetailsViewInsertedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: DetailsViewInsertedEventArgs) -> bool
        Set: ExceptionHandled(self: DetailsViewInsertedEventArgs) = value
        """
        ...

    @property
    def KeepInInsertMode(self) -> bool:
        """
        Get: KeepInInsertMode(self: DetailsViewInsertedEventArgs) -> bool
        Set: KeepInInsertMode(self: DetailsViewInsertedEventArgs) = value
        """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: DetailsViewInsertedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class DetailsViewInsertedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewInsertedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewInsertedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewInsertedEventHandler, sender: object, e: DetailsViewInsertedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewInsertedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewInsertedEventArgs): # -> 
        """ Invoke(self: DetailsViewInsertedEventHandler, sender: object, e: DetailsViewInsertedEventArgs) """
        ...


class DetailsViewInsertEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewInsertEventArgs(commandArgument: object) """
    @property
    def CommandArgument(self) -> object:
        """ Get: CommandArgument(self: DetailsViewInsertEventArgs) -> object """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: DetailsViewInsertEventArgs) -> IOrderedDictionary """
        ...



class DetailsViewInsertEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewInsertEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewInsertEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewInsertEventHandler, sender: object, e: DetailsViewInsertEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewInsertEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewInsertEventArgs): # -> 
        """ Invoke(self: DetailsViewInsertEventHandler, sender: object, e: DetailsViewInsertEventArgs) """
        ...


class DetailsViewMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DetailsViewMode, values: Edit (1), Insert (2), ReadOnly (0) """
    Edit: DetailsViewMode = ...
    Insert: DetailsViewMode = ...
    ReadOnly: DetailsViewMode = ...
    value__ = ...


class DetailsViewModeEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewModeEventArgs(mode: DetailsViewMode, cancelingEdit: bool) """
    @property
    def CancelingEdit(self) -> bool:
        """ Get: CancelingEdit(self: DetailsViewModeEventArgs) -> bool """
        ...

    @property
    def NewMode(self) -> DetailsViewMode:
        """
        Get: NewMode(self: DetailsViewModeEventArgs) -> DetailsViewMode
        Set: NewMode(self: DetailsViewModeEventArgs) = value
        """
        ...



class DetailsViewModeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewModeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewModeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewModeEventHandler, sender: object, e: DetailsViewModeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewModeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewModeEventArgs): # -> 
        """ Invoke(self: DetailsViewModeEventHandler, sender: object, e: DetailsViewModeEventArgs) """
        ...


class DetailsViewPageEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewPageEventArgs(newPageIndex: int) """
    @property
    def NewPageIndex(self) -> int:
        """
        Get: NewPageIndex(self: DetailsViewPageEventArgs) -> int
        Set: NewPageIndex(self: DetailsViewPageEventArgs) = value
        """
        ...



class DetailsViewPageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewPageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewPageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewPageEventHandler, sender: object, e: DetailsViewPageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewPageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewPageEventArgs): # -> 
        """ Invoke(self: DetailsViewPageEventHandler, sender: object, e: DetailsViewPageEventArgs) """
        ...


class DetailsViewRow(TableRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DetailsViewRow(rowIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: DetailsViewRow) -> int """
        ...

    @property
    def RowState(self) -> DataControlRowState:
        """ Get: RowState(self: DetailsViewRow) -> DataControlRowState """
        ...

    @property
    def RowType(self) -> DataControlRowType:
        """ Get: RowType(self: DetailsViewRow) -> DataControlRowType """
        ...


    def __new__(cls, rowIndex:int, rowType:DataControlRowType, rowState:DataControlRowState) -> Self:
        """ __new__(cls: type, rowIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
        ...


class DetailsViewPagerRow(INonBindingContainer, DetailsViewRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ DetailsViewPagerRow(rowIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
    pass

class DetailsViewRowCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DetailsViewRowCollection(rows: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DetailsViewRowCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DetailsViewRowCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class DetailsViewRowsGenerator(AutoFieldsGenerator): # skipped bases: <type 'IStateManager'>, <type 'IAutoFieldGenerator'>, <type 'object'>
    """ DetailsViewRowsGenerator() """
    pass

class DetailsViewUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DetailsViewUpdatedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: DetailsViewUpdatedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: DetailsViewUpdatedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: DetailsViewUpdatedEventArgs) -> bool
        Set: ExceptionHandled(self: DetailsViewUpdatedEventArgs) = value
        """
        ...

    @property
    def KeepInEditMode(self) -> bool:
        """
        Get: KeepInEditMode(self: DetailsViewUpdatedEventArgs) -> bool
        Set: KeepInEditMode(self: DetailsViewUpdatedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: DetailsViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: DetailsViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: DetailsViewUpdatedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class DetailsViewUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewUpdatedEventHandler, sender: object, e: DetailsViewUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewUpdatedEventArgs): # -> 
        """ Invoke(self: DetailsViewUpdatedEventHandler, sender: object, e: DetailsViewUpdatedEventArgs) """
        ...


class DetailsViewUpdateEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ DetailsViewUpdateEventArgs(commandArgument: object) """
    @property
    def CommandArgument(self) -> object:
        """ Get: CommandArgument(self: DetailsViewUpdateEventArgs) -> object """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: DetailsViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: DetailsViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: DetailsViewUpdateEventArgs) -> IOrderedDictionary """
        ...



class DetailsViewUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DetailsViewUpdateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DetailsViewUpdateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DetailsViewUpdateEventHandler, sender: object, e: DetailsViewUpdateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DetailsViewUpdateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DetailsViewUpdateEventArgs): # -> 
        """ Invoke(self: DetailsViewUpdateEventHandler, sender: object, e: DetailsViewUpdateEventArgs) """
        ...


class DropDownList(IPostBackDataHandler, ListControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IEditableTextControl'>, <type 'object'>
    """ DropDownList() """
    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: DropDownList) -> Color
        Set: BorderColor(self: DropDownList) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: DropDownList) -> BorderStyle
        Set: BorderStyle(self: DropDownList) = value
        """
        ...

    @property
    def BorderWidth(self): # -> Unit
        """
        Get: BorderWidth(self: DropDownList) -> Unit
        Set: BorderWidth(self: DropDownList) = value
        """
        ...

    @property
    def SupportsDisabledAttribute(self) -> bool:
        """ Get: SupportsDisabledAttribute(self: DropDownList) -> bool """
        ...



class EditCommandColumn(DataGridColumn): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ EditCommandColumn() """
    @property
    def ButtonType(self) -> ButtonColumnType:
        """
        Get: ButtonType(self: EditCommandColumn) -> ButtonColumnType
        Set: ButtonType(self: EditCommandColumn) = value
        """
        ...

    @property
    def CancelText(self) -> str:
        """
        Get: CancelText(self: EditCommandColumn) -> str
        Set: CancelText(self: EditCommandColumn) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: EditCommandColumn) -> bool
        Set: CausesValidation(self: EditCommandColumn) = value
        """
        ...

    @property
    def EditText(self) -> str:
        """
        Get: EditText(self: EditCommandColumn) -> str
        Set: EditText(self: EditCommandColumn) = value
        """
        ...

    @property
    def UpdateText(self) -> str:
        """
        Get: UpdateText(self: EditCommandColumn) -> str
        Set: UpdateText(self: EditCommandColumn) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: EditCommandColumn) -> str
        Set: ValidationGroup(self: EditCommandColumn) = value
        """
        ...



class EmbeddedMailObject: # skipped bases: <type 'object'>, <type 'object'>
    """
    EmbeddedMailObject()
    EmbeddedMailObject(name: str, path: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: EmbeddedMailObject) -> str
        Set: Name(self: EmbeddedMailObject) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: EmbeddedMailObject) -> str
        Set: Path(self: EmbeddedMailObject) = value
        """
        ...



class EmbeddedMailObjectsCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ EmbeddedMailObjectsCollection() """
    def Add(self, value:EmbeddedMailObject) -> int:
        """ Add(self: EmbeddedMailObjectsCollection, value: EmbeddedMailObject) -> int """
        ...

    def Contains(self, value:EmbeddedMailObject) -> bool:
        """ Contains(self: EmbeddedMailObjectsCollection, value: EmbeddedMailObject) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: EmbeddedMailObjectsCollection, array: Array[EmbeddedMailObject], index: int) """
        ...

    def IndexOf(self, value:EmbeddedMailObject) -> int:
        """ IndexOf(self: EmbeddedMailObjectsCollection, value: EmbeddedMailObject) -> int """
        ...

    def Insert(self, index:int, value:EmbeddedMailObject): # -> 
        """ Insert(self: EmbeddedMailObjectsCollection, index: int, value: EmbeddedMailObject) """
        ...

    def Remove(self, value:EmbeddedMailObject): # -> 
        """ Remove(self: EmbeddedMailObjectsCollection, value: EmbeddedMailObject) """
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


class EntityDataSource(DataSourceControl, IDynamicDataSource, IQueryableDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """
    EntityDataSource()
    EntityDataSource(connection: EntityConnection)
    """
    @property
    def AutoGenerateOrderByClause(self) -> bool:
        """
        Get: AutoGenerateOrderByClause(self: EntityDataSource) -> bool
        Set: AutoGenerateOrderByClause(self: EntityDataSource) = value
        """
        ...

    @property
    def AutoPage(self) -> bool:
        """
        Get: AutoPage(self: EntityDataSource) -> bool
        Set: AutoPage(self: EntityDataSource) = value
        """
        ...

    @property
    def AutoSort(self) -> bool:
        """
        Get: AutoSort(self: EntityDataSource) -> bool
        Set: AutoSort(self: EntityDataSource) = value
        """
        ...

    @property
    def CommandParameters(self) -> ParameterCollection:
        """ Get: CommandParameters(self: EntityDataSource) -> ParameterCollection """
        ...

    @property
    def CommandText(self) -> str:
        """
        Get: CommandText(self: EntityDataSource) -> str
        Set: CommandText(self: EntityDataSource) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: EntityDataSource) -> str
        Set: ConnectionString(self: EntityDataSource) = value
        """
        ...

    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: EntityDataSource) -> str
        Set: ContextTypeName(self: EntityDataSource) = value
        """
        ...

    @property
    def DefaultContainerName(self) -> str:
        """
        Get: DefaultContainerName(self: EntityDataSource) -> str
        Set: DefaultContainerName(self: EntityDataSource) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: EntityDataSource) -> ParameterCollection """
        ...

    @property
    def EnableFlattening(self) -> bool:
        """
        Get: EnableFlattening(self: EntityDataSource) -> bool
        Set: EnableFlattening(self: EntityDataSource) = value
        """
        ...

    @property
    def EntityTypeFilter(self) -> str:
        """
        Get: EntityTypeFilter(self: EntityDataSource) -> str
        Set: EntityTypeFilter(self: EntityDataSource) = value
        """
        ...

    @property
    def GroupBy(self) -> str:
        """
        Get: GroupBy(self: EntityDataSource) -> str
        Set: GroupBy(self: EntityDataSource) = value
        """
        ...

    @property
    def Include(self) -> str:
        """
        Get: Include(self: EntityDataSource) -> str
        Set: Include(self: EntityDataSource) = value
        """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: EntityDataSource) -> ParameterCollection """
        ...

    @property
    def OrderBy(self) -> str:
        """
        Get: OrderBy(self: EntityDataSource) -> str
        Set: OrderBy(self: EntityDataSource) = value
        """
        ...

    @property
    def OrderByParameters(self) -> ParameterCollection:
        """ Get: OrderByParameters(self: EntityDataSource) -> ParameterCollection """
        ...

    @property
    def Select(self) -> str:
        """
        Get: Select(self: EntityDataSource) -> str
        Set: Select(self: EntityDataSource) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: EntityDataSource) -> ParameterCollection """
        ...

    @property
    def StoreOriginalValuesInViewState(self) -> bool:
        """
        Get: StoreOriginalValuesInViewState(self: EntityDataSource) -> bool
        Set: StoreOriginalValuesInViewState(self: EntityDataSource) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: EntityDataSource) -> ParameterCollection """
        ...


    def CreateView(self, *args): #cannot find CLR method
        """ CreateView(self: EntityDataSource) -> EntityDataSourceView """
        ...

    def __new__(cls, connection:EntityConnection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connection: EntityConnection)
        """
        ...

    ContextCreated = ...
    ContextCreating = ...
    ContextDisposing = ...
    Deleted = ...
    Deleting = ...
    Inserted = ...
    Inserting = ...
    QueryCreated = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class EntityDataSourceChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: EntityDataSourceChangedEventArgs) -> ObjectContext """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: EntityDataSourceChangedEventArgs) -> object """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: EntityDataSourceChangedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: EntityDataSourceChangedEventArgs) -> bool
        Set: ExceptionHandled(self: EntityDataSourceChangedEventArgs) = value
        """
        ...



class EntityDataSourceChangingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: EntityDataSourceChangingEventArgs) -> ObjectContext """
        ...

    @property
    def Entity(self) -> object:
        """ Get: Entity(self: EntityDataSourceChangingEventArgs) -> object """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: EntityDataSourceChangingEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: EntityDataSourceChangingEventArgs) -> bool
        Set: ExceptionHandled(self: EntityDataSourceChangingEventArgs) = value
        """
        ...



class EntityDataSourceContextCreatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: EntityDataSourceContextCreatedEventArgs) -> ObjectContext """
        ...



class EntityDataSourceContextCreatingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """
        Get: Context(self: EntityDataSourceContextCreatingEventArgs) -> ObjectContext
        Set: Context(self: EntityDataSourceContextCreatingEventArgs) = value
        """
        ...



class EntityDataSourceContextDisposingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: EntityDataSourceContextDisposingEventArgs) -> ObjectContext """
        ...



class EntityDataSourceSelectedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ObjectContext:
        """ Get: Context(self: EntityDataSourceSelectedEventArgs) -> ObjectContext """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: EntityDataSourceSelectedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: EntityDataSourceSelectedEventArgs) -> bool
        Set: ExceptionHandled(self: EntityDataSourceSelectedEventArgs) = value
        """
        ...

    @property
    def Results(self) -> IEnumerable:
        """ Get: Results(self: EntityDataSourceSelectedEventArgs) -> IEnumerable """
        ...

    @property
    def SelectArguments(self) -> DataSourceSelectArguments:
        """ Get: SelectArguments(self: EntityDataSourceSelectedEventArgs) -> DataSourceSelectArguments """
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: EntityDataSourceSelectedEventArgs) -> int """
        ...



class EntityDataSourceSelectingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataSource(self) -> EntityDataSource:
        """ Get: DataSource(self: EntityDataSourceSelectingEventArgs) -> EntityDataSource """
        ...

    @property
    def SelectArguments(self) -> DataSourceSelectArguments:
        """ Get: SelectArguments(self: EntityDataSourceSelectingEventArgs) -> DataSourceSelectArguments """
        ...



class EntityDataSourceValidationException(IDynamicValidatorException, Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EntityDataSourceValidationException()
    EntityDataSourceValidationException(message: str)
    EntityDataSourceValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EntityDataSourceView(DataSourceView, IStateManager): # skipped bases: <type 'object'>
    """ EntityDataSourceView(owner: EntityDataSource, viewName: str) """
    def GetViewSchema(self) -> DataTable:
        """ GetViewSchema(self: EntityDataSourceView) -> DataTable """
        ...

    ContextCreated = ...
    ContextCreating = ...
    ContextDisposing = ...
    Deleted = ...
    Deleting = ...
    Exception = ...
    Inserted = ...
    Inserting = ...
    QueryCreated = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class FileUpload(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ FileUpload() """
    @property
    def AllowMultiple(self) -> bool:
        """
        Get: AllowMultiple(self: FileUpload) -> bool
        Set: AllowMultiple(self: FileUpload) = value
        """
        ...

    @property
    def FileBytes(self) -> Array:
        """ Get: FileBytes(self: FileUpload) -> Array[Byte] """
        ...

    @property
    def FileContent(self) -> Stream:
        """ Get: FileContent(self: FileUpload) -> Stream """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: FileUpload) -> str """
        ...

    @property
    def HasFile(self) -> bool:
        """ Get: HasFile(self: FileUpload) -> bool """
        ...

    @property
    def HasFiles(self) -> bool:
        """ Get: HasFiles(self: FileUpload) -> bool """
        ...

    @property
    def PostedFile(self) -> HttpPostedFile:
        """ Get: PostedFile(self: FileUpload) -> HttpPostedFile """
        ...

    @property
    def PostedFiles(self) -> IList:
        """ Get: PostedFiles(self: FileUpload) -> IList[HttpPostedFile] """
        ...


    def SaveAs(self, filename:str): # -> 
        """ SaveAs(self: FileUpload, filename: str) """
        ...


class FirstDayOfWeek(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirstDayOfWeek, values: Default (7), Friday (5), Monday (1), Saturday (6), Sunday (0), Thursday (4), Tuesday (2), Wednesday (3) """
    Default: FirstDayOfWeek = ...
    Friday: FirstDayOfWeek = ...
    Monday: FirstDayOfWeek = ...
    Saturday: FirstDayOfWeek = ...
    Sunday: FirstDayOfWeek = ...
    Thursday: FirstDayOfWeek = ...
    Tuesday: FirstDayOfWeek = ...
    value__ = ...
    Wednesday: FirstDayOfWeek = ...


class FontInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Bold(self) -> bool:
        """
        Get: Bold(self: FontInfo) -> bool
        Set: Bold(self: FontInfo) = value
        """
        ...

    @property
    def Italic(self) -> bool:
        """
        Get: Italic(self: FontInfo) -> bool
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
    def Names(self) -> Array:
        """
        Get: Names(self: FontInfo) -> Array[str]
        Set: Names(self: FontInfo) = value
        """
        ...

    @property
    def Overline(self) -> bool:
        """
        Get: Overline(self: FontInfo) -> bool
        Set: Overline(self: FontInfo) = value
        """
        ...

    @property
    def Size(self): # -> FontUnit
        """
        Get: Size(self: FontInfo) -> FontUnit
        Set: Size(self: FontInfo) = value
        """
        ...

    @property
    def Strikeout(self) -> bool:
        """
        Get: Strikeout(self: FontInfo) -> bool
        Set: Strikeout(self: FontInfo) = value
        """
        ...

    @property
    def Underline(self) -> bool:
        """
        Get: Underline(self: FontInfo) -> bool
        Set: Underline(self: FontInfo) = value
        """
        ...


    def ClearDefaults(self): # -> 
        """ ClearDefaults(self: FontInfo) """
        ...

    def CopyFrom(self, f:FontInfo): # -> 
        """ CopyFrom(self: FontInfo, f: FontInfo) """
        ...

    def MergeWith(self, f:FontInfo): # -> 
        """ MergeWith(self: FontInfo, f: FontInfo) """
        ...

    def ShouldSerializeNames(self) -> bool:
        """ ShouldSerializeNames(self: FontInfo) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: FontInfo) -> str """
        ...


class FontNamesConverter(TypeConverter): # skipped bases: <type 'object'>
    """ FontNamesConverter() """
    pass

class FontSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FontSize, values: AsUnit (1), Large (8), Larger (3), Medium (7), NotSet (0), Small (6), Smaller (2), XLarge (9), XSmall (5), XXLarge (10), XXSmall (4) """
    AsUnit: FontSize = ...
    Large: FontSize = ...
    Larger: FontSize = ...
    Medium: FontSize = ...
    NotSet: FontSize = ...
    Small: FontSize = ...
    Smaller: FontSize = ...
    value__ = ...
    XLarge: FontSize = ...
    XSmall: FontSize = ...
    XXLarge: FontSize = ...
    XXSmall: FontSize = ...


class FontUnit: # skipped bases: <type 'object'>, <type 'object'>
    """
    FontUnit(type: FontSize)
    FontUnit(value: Unit)
    FontUnit(value: int)
    FontUnit(value: float)
    FontUnit(value: float, type: UnitType)
    FontUnit(value: str)
    FontUnit(value: str, culture: CultureInfo)
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: FontUnit) -> bool """
        ...

    @property
    def Type(self) -> FontSize:
        """ Get: Type(self: FontUnit) -> FontSize """
        ...

    @property
    def Unit(self): # -> Unit
        """ Get: Unit(self: FontUnit) -> Unit """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: FontUnit, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: FontUnit) -> int """
        ...

    @staticmethod
    def Parse(s:str, culture:CultureInfo = ...) -> FontUnit:
        """
        Parse(s: str) -> FontUnit
        Parse(s: str, culture: CultureInfo) -> FontUnit
        """
        ...

    @staticmethod
    def Point(n:int) -> FontUnit:
        """ Point(n: int) -> FontUnit """
        ...

    def ToString(self, *__args:CultureInfo) -> str:
        """
        ToString(self: FontUnit) -> str
        ToString(self: FontUnit, culture: CultureInfo) -> str
        ToString(self: FontUnit, formatProvider: IFormatProvider) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: FontUnit = ...
    Large: FontUnit = ...
    Larger: FontUnit = ...
    Medium: FontUnit = ...
    Small: FontUnit = ...
    Smaller: FontUnit = ...
    XLarge: FontUnit = ...
    XSmall: FontUnit = ...
    XXLarge: FontUnit = ...
    XXSmall: FontUnit = ...


class FontUnitConverter(TypeConverter): # skipped bases: <type 'object'>
    """ FontUnitConverter() """
    pass

class FormParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    FormParameter()
    FormParameter(name: str, formField: str)
    FormParameter(name: str, dbType: DbType, formField: str)
    FormParameter(name: str, type: TypeCode, formField: str)
    """
    @property
    def FormField(self) -> str:
        """
        Get: FormField(self: FormParameter) -> str
        Set: FormField(self: FormParameter) = value
        """
        ...

    @property
    def ValidateInput(self) -> bool:
        """
        Get: ValidateInput(self: FormParameter) -> bool
        Set: ValidateInput(self: FormParameter) = value
        """
        ...



class FormView(IDataItemContainer, IDataBoundItemControl, CompositeDataBoundControl, IPostBackEventHandler, IPostBackContainer, IRenderOuterTableControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IDataBoundControl'>, <type 'object'>
    """ FormView() """
    @property
    def AllowPaging(self) -> bool:
        """
        Get: AllowPaging(self: FormView) -> bool
        Set: AllowPaging(self: FormView) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: FormView) -> str
        Set: BackImageUrl(self: FormView) = value
        """
        ...

    @property
    def BottomPagerRow(self): # -> FormViewRow
        """ Get: BottomPagerRow(self: FormView) -> FormViewRow """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: FormView) -> str
        Set: Caption(self: FormView) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: FormView) -> TableCaptionAlign
        Set: CaptionAlign(self: FormView) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: FormView) -> int
        Set: CellPadding(self: FormView) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: FormView) -> int
        Set: CellSpacing(self: FormView) = value
        """
        ...

    @property
    def CurrentMode(self): # -> FormViewMode
        """ Get: CurrentMode(self: FormView) -> FormViewMode """
        ...

    @property
    def DataItemCount(self) -> int:
        """ Get: DataItemCount(self: FormView) -> int """
        ...

    @property
    def DataKeyNames(self) -> Array:
        """
        Get: DataKeyNames(self: FormView) -> Array[str]
        Set: DataKeyNames(self: FormView) = value
        """
        ...

    @property
    def DefaultMode(self): # -> FormViewMode
        """
        Get: DefaultMode(self: FormView) -> FormViewMode
        Set: DefaultMode(self: FormView) = value
        """
        ...

    @property
    def EditItemTemplate(self) -> ITemplate:
        """
        Get: EditItemTemplate(self: FormView) -> ITemplate
        Set: EditItemTemplate(self: FormView) = value
        """
        ...

    @property
    def EditRowStyle(self) -> TableItemStyle:
        """ Get: EditRowStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def EmptyDataRowStyle(self) -> TableItemStyle:
        """ Get: EmptyDataRowStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def EmptyDataTemplate(self) -> ITemplate:
        """
        Get: EmptyDataTemplate(self: FormView) -> ITemplate
        Set: EmptyDataTemplate(self: FormView) = value
        """
        ...

    @property
    def EmptyDataText(self) -> str:
        """
        Get: EmptyDataText(self: FormView) -> str
        Set: EmptyDataText(self: FormView) = value
        """
        ...

    @property
    def EnableModelValidation(self) -> bool:
        """
        Get: EnableModelValidation(self: FormView) -> bool
        Set: EnableModelValidation(self: FormView) = value
        """
        ...

    @property
    def FooterRow(self): # -> FormViewRow
        """ Get: FooterRow(self: FormView) -> FormViewRow """
        ...

    @property
    def FooterStyle(self) -> TableItemStyle:
        """ Get: FooterStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: FormView) -> ITemplate
        Set: FooterTemplate(self: FormView) = value
        """
        ...

    @property
    def FooterText(self) -> str:
        """
        Get: FooterText(self: FormView) -> str
        Set: FooterText(self: FormView) = value
        """
        ...

    @property
    def GridLines(self): # -> GridLines
        """
        Get: GridLines(self: FormView) -> GridLines
        Set: GridLines(self: FormView) = value
        """
        ...

    @property
    def HeaderRow(self): # -> FormViewRow
        """ Get: HeaderRow(self: FormView) -> FormViewRow """
        ...

    @property
    def HeaderStyle(self) -> TableItemStyle:
        """ Get: HeaderStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: FormView) -> ITemplate
        Set: HeaderTemplate(self: FormView) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: FormView) -> str
        Set: HeaderText(self: FormView) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: FormView) -> HorizontalAlign
        Set: HorizontalAlign(self: FormView) = value
        """
        ...

    @property
    def InsertItemTemplate(self) -> ITemplate:
        """
        Get: InsertItemTemplate(self: FormView) -> ITemplate
        Set: InsertItemTemplate(self: FormView) = value
        """
        ...

    @property
    def InsertRowStyle(self) -> TableItemStyle:
        """ Get: InsertRowStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: FormView) -> ITemplate
        Set: ItemTemplate(self: FormView) = value
        """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: FormView) -> int """
        ...

    @property
    def PageIndex(self) -> int:
        """
        Get: PageIndex(self: FormView) -> int
        Set: PageIndex(self: FormView) = value
        """
        ...

    @property
    def PagerSettings(self): # -> PagerSettings
        """ Get: PagerSettings(self: FormView) -> PagerSettings """
        ...

    @property
    def PagerStyle(self) -> TableItemStyle:
        """ Get: PagerStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def PagerTemplate(self) -> ITemplate:
        """
        Get: PagerTemplate(self: FormView) -> ITemplate
        Set: PagerTemplate(self: FormView) = value
        """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: FormView) -> bool
        Set: RenderOuterTable(self: FormView) = value
        """
        ...

    @property
    def Row(self): # -> FormViewRow
        """ Get: Row(self: FormView) -> FormViewRow """
        ...

    @property
    def RowStyle(self) -> TableItemStyle:
        """ Get: RowStyle(self: FormView) -> TableItemStyle """
        ...

    @property
    def SelectedValue(self) -> object:
        """ Get: SelectedValue(self: FormView) -> object """
        ...

    @property
    def TopPagerRow(self): # -> FormViewRow
        """ Get: TopPagerRow(self: FormView) -> FormViewRow """
        ...


    def ChangeMode(self, newMode): # ->  # Not found arg types: {'newMode': 'FormViewMode'}
        """ ChangeMode(self: FormView, newMode: FormViewMode) """
        ...

    def CreateRow(self, *args): #cannot find CLR method
        """ CreateRow(self: FormView, itemIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) -> FormViewRow """
        ...

    def CreateTable(self, *args): #cannot find CLR method
        """ CreateTable(self: FormView) -> Table """
        ...

    def DeleteItem(self): # -> 
        """ DeleteItem(self: FormView) """
        ...

    def ExtractRowValues(self, *args): #cannot find CLR method
        """ ExtractRowValues(self: FormView, fieldValues: IOrderedDictionary, includeKeys: bool) """
        ...

    def InitializePager(self, *args): #cannot find CLR method
        """ InitializePager(self: FormView, row: FormViewRow, pagedDataSource: PagedDataSource) """
        ...

    def InitializeRow(self, *args): #cannot find CLR method
        """ InitializeRow(self: FormView, row: FormViewRow) """
        ...

    def InsertItem(self, causesValidation:bool): # -> 
        """ InsertItem(self: FormView, causesValidation: bool) """
        ...

    def IsBindableType(self, type:Type) -> bool:
        """ IsBindableType(self: FormView, type: Type) -> bool """
        ...

    def ModifiedOuterTableStylePropertyName(self, *args): #cannot find CLR method
        """ ModifiedOuterTableStylePropertyName(self: FormView) -> str """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: FormView, e: FormViewCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: FormView, e: EventArgs) """
        ...

    def OnItemDeleted(self, *args): #cannot find CLR method
        """ OnItemDeleted(self: FormView, e: FormViewDeletedEventArgs) """
        ...

    def OnItemDeleting(self, *args): #cannot find CLR method
        """ OnItemDeleting(self: FormView, e: FormViewDeleteEventArgs) """
        ...

    def OnItemInserted(self, *args): #cannot find CLR method
        """ OnItemInserted(self: FormView, e: FormViewInsertedEventArgs) """
        ...

    def OnItemInserting(self, *args): #cannot find CLR method
        """ OnItemInserting(self: FormView, e: FormViewInsertEventArgs) """
        ...

    def OnItemUpdated(self, *args): #cannot find CLR method
        """ OnItemUpdated(self: FormView, e: FormViewUpdatedEventArgs) """
        ...

    def OnItemUpdating(self, *args): #cannot find CLR method
        """ OnItemUpdating(self: FormView, e: FormViewUpdateEventArgs) """
        ...

    def OnModeChanged(self, *args): #cannot find CLR method
        """ OnModeChanged(self: FormView, e: EventArgs) """
        ...

    def OnModeChanging(self, *args): #cannot find CLR method
        """ OnModeChanging(self: FormView, e: FormViewModeEventArgs) """
        ...

    def OnPageIndexChanged(self, *args): #cannot find CLR method
        """ OnPageIndexChanged(self: FormView, e: EventArgs) """
        ...

    def OnPageIndexChanging(self, *args): #cannot find CLR method
        """ OnPageIndexChanging(self: FormView, e: FormViewPageEventArgs) """
        ...

    def PrepareControlHierarchy(self, *args): #cannot find CLR method
        """ PrepareControlHierarchy(self: FormView) """
        ...

    def SetPageIndex(self, index:int): # -> 
        """ SetPageIndex(self: FormView, index: int) """
        ...

    def UpdateItem(self, causesValidation:bool): # -> 
        """ UpdateItem(self: FormView, causesValidation: bool) """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        ...

    ItemCommand = ...
    ItemCreated = ...
    ItemDeleted = ...
    ItemDeleting = ...
    ItemInserted = ...
    ItemInserting = ...
    ItemUpdated = ...
    ItemUpdating = ...
    ModeChanged = ...
    ModeChanging = ...
    PageIndexChanged = ...
    PageIndexChanging = ...


class FormViewCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ FormViewCommandEventArgs(commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: FormViewCommandEventArgs) -> object """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: FormViewCommandEventArgs) -> bool
        Set: Handled(self: FormViewCommandEventArgs) = value
        """
        ...



class FormViewCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewCommandEventHandler, sender: object, e: FormViewCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewCommandEventArgs): # -> 
        """ Invoke(self: FormViewCommandEventHandler, sender: object, e: FormViewCommandEventArgs) """
        ...


class FormViewDeletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FormViewDeletedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: FormViewDeletedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: FormViewDeletedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: FormViewDeletedEventArgs) -> bool
        Set: ExceptionHandled(self: FormViewDeletedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: FormViewDeletedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: FormViewDeletedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class FormViewDeletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewDeletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewDeletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewDeletedEventHandler, sender: object, e: FormViewDeletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewDeletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewDeletedEventArgs): # -> 
        """ Invoke(self: FormViewDeletedEventHandler, sender: object, e: FormViewDeletedEventArgs) """
        ...


class FormViewDeleteEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ FormViewDeleteEventArgs(rowIndex: int) """
    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: FormViewDeleteEventArgs) -> IOrderedDictionary """
        ...

    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: FormViewDeleteEventArgs) -> int """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: FormViewDeleteEventArgs) -> IOrderedDictionary """
        ...



class FormViewDeleteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewDeleteEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewDeleteEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewDeleteEventHandler, sender: object, e: FormViewDeleteEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewDeleteEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewDeleteEventArgs): # -> 
        """ Invoke(self: FormViewDeleteEventHandler, sender: object, e: FormViewDeleteEventArgs) """
        ...


class FormViewInsertedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FormViewInsertedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: FormViewInsertedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: FormViewInsertedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: FormViewInsertedEventArgs) -> bool
        Set: ExceptionHandled(self: FormViewInsertedEventArgs) = value
        """
        ...

    @property
    def KeepInInsertMode(self) -> bool:
        """
        Get: KeepInInsertMode(self: FormViewInsertedEventArgs) -> bool
        Set: KeepInInsertMode(self: FormViewInsertedEventArgs) = value
        """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: FormViewInsertedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class FormViewInsertedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewInsertedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewInsertedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewInsertedEventHandler, sender: object, e: FormViewInsertedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewInsertedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewInsertedEventArgs): # -> 
        """ Invoke(self: FormViewInsertedEventHandler, sender: object, e: FormViewInsertedEventArgs) """
        ...


class FormViewInsertEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ FormViewInsertEventArgs(commandArgument: object) """
    @property
    def CommandArgument(self) -> object:
        """ Get: CommandArgument(self: FormViewInsertEventArgs) -> object """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: FormViewInsertEventArgs) -> IOrderedDictionary """
        ...



class FormViewInsertEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewInsertEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewInsertEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewInsertEventHandler, sender: object, e: FormViewInsertEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewInsertEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewInsertEventArgs): # -> 
        """ Invoke(self: FormViewInsertEventHandler, sender: object, e: FormViewInsertEventArgs) """
        ...


class FormViewMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormViewMode, values: Edit (1), Insert (2), ReadOnly (0) """
    Edit: FormViewMode = ...
    Insert: FormViewMode = ...
    ReadOnly: FormViewMode = ...
    value__ = ...


class FormViewModeEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ FormViewModeEventArgs(mode: FormViewMode, cancelingEdit: bool) """
    @property
    def CancelingEdit(self) -> bool:
        """ Get: CancelingEdit(self: FormViewModeEventArgs) -> bool """
        ...

    @property
    def NewMode(self) -> FormViewMode:
        """
        Get: NewMode(self: FormViewModeEventArgs) -> FormViewMode
        Set: NewMode(self: FormViewModeEventArgs) = value
        """
        ...



class FormViewModeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewModeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewModeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewModeEventHandler, sender: object, e: FormViewModeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewModeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewModeEventArgs): # -> 
        """ Invoke(self: FormViewModeEventHandler, sender: object, e: FormViewModeEventArgs) """
        ...


class FormViewPageEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ FormViewPageEventArgs(newPageIndex: int) """
    @property
    def NewPageIndex(self) -> int:
        """
        Get: NewPageIndex(self: FormViewPageEventArgs) -> int
        Set: NewPageIndex(self: FormViewPageEventArgs) = value
        """
        ...



class FormViewPageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewPageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewPageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewPageEventHandler, sender: object, e: FormViewPageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewPageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewPageEventArgs): # -> 
        """ Invoke(self: FormViewPageEventHandler, sender: object, e: FormViewPageEventArgs) """
        ...


class FormViewRow(TableRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ FormViewRow(itemIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: FormViewRow) -> int """
        ...

    @property
    def RowState(self) -> DataControlRowState:
        """ Get: RowState(self: FormViewRow) -> DataControlRowState """
        ...

    @property
    def RowType(self) -> DataControlRowType:
        """ Get: RowType(self: FormViewRow) -> DataControlRowType """
        ...


    def __new__(cls, itemIndex:int, rowType:DataControlRowType, rowState:DataControlRowState) -> Self:
        """ __new__(cls: type, itemIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
        ...


class FormViewPagerRow(INonBindingContainer, FormViewRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ FormViewPagerRow(rowIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
    pass

class FormViewUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FormViewUpdatedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: FormViewUpdatedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: FormViewUpdatedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: FormViewUpdatedEventArgs) -> bool
        Set: ExceptionHandled(self: FormViewUpdatedEventArgs) = value
        """
        ...

    @property
    def KeepInEditMode(self) -> bool:
        """
        Get: KeepInEditMode(self: FormViewUpdatedEventArgs) -> bool
        Set: KeepInEditMode(self: FormViewUpdatedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: FormViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: FormViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: FormViewUpdatedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class FormViewUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewUpdatedEventHandler, sender: object, e: FormViewUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewUpdatedEventArgs): # -> 
        """ Invoke(self: FormViewUpdatedEventHandler, sender: object, e: FormViewUpdatedEventArgs) """
        ...


class FormViewUpdateEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ FormViewUpdateEventArgs(commandArgument: object) """
    @property
    def CommandArgument(self) -> object:
        """ Get: CommandArgument(self: FormViewUpdateEventArgs) -> object """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: FormViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: FormViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: FormViewUpdateEventArgs) -> IOrderedDictionary """
        ...



class FormViewUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormViewUpdateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormViewUpdateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormViewUpdateEventHandler, sender: object, e: FormViewUpdateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormViewUpdateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormViewUpdateEventArgs): # -> 
        """ Invoke(self: FormViewUpdateEventHandler, sender: object, e: FormViewUpdateEventArgs) """
        ...


class GridLines(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridLines, values: Both (3), Horizontal (1), None (0), Vertical (2) """
    Both: GridLines = ...
    Horizontal: GridLines = ...
    value__ = ...
    Vertical: GridLines = ...


class IDataBoundListControl(IDataBoundControl): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ClientIDRowSuffix(self) -> Array:
        """
        Get: ClientIDRowSuffix(self: IDataBoundListControl) -> Array[str]
        Set: ClientIDRowSuffix(self: IDataBoundListControl) = value
        """
        ...

    @property
    def DataKeys(self) -> DataKeyArray:
        """ Get: DataKeys(self: IDataBoundListControl) -> DataKeyArray """
        ...

    @property
    def EnablePersistedSelection(self) -> bool:
        """
        Get: EnablePersistedSelection(self: IDataBoundListControl) -> bool
        Set: EnablePersistedSelection(self: IDataBoundListControl) = value
        """
        ...

    @property
    def SelectedDataKey(self) -> DataKey:
        """ Get: SelectedDataKey(self: IDataBoundListControl) -> DataKey """
        ...

    @property
    def SelectedIndex(self) -> int:
        """
        Get: SelectedIndex(self: IDataBoundListControl) -> int
        Set: SelectedIndex(self: IDataBoundListControl) = value
        """
        ...



class IPersistedSelector: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataKey(self) -> DataKey:
        """
        Get: DataKey(self: IPersistedSelector) -> DataKey
        Set: DataKey(self: IPersistedSelector) = value
        """
        ...



class GridView(IDataKeysControl, ICallbackContainer, ICallbackEventHandler, IPersistedSelector, IFieldControl, CompositeDataBoundControl, IPostBackContainer, IPostBackEventHandler, IDataBoundListControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IDataBoundControl'>, <type 'object'>
    """ GridView() """
    @property
    def AllowCustomPaging(self) -> bool:
        """
        Get: AllowCustomPaging(self: GridView) -> bool
        Set: AllowCustomPaging(self: GridView) = value
        """
        ...

    @property
    def AllowPaging(self) -> bool:
        """
        Get: AllowPaging(self: GridView) -> bool
        Set: AllowPaging(self: GridView) = value
        """
        ...

    @property
    def AllowSorting(self) -> bool:
        """
        Get: AllowSorting(self: GridView) -> bool
        Set: AllowSorting(self: GridView) = value
        """
        ...

    @property
    def AlternatingRowStyle(self) -> TableItemStyle:
        """ Get: AlternatingRowStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def AutoGenerateColumns(self) -> bool:
        """
        Get: AutoGenerateColumns(self: GridView) -> bool
        Set: AutoGenerateColumns(self: GridView) = value
        """
        ...

    @property
    def AutoGenerateDeleteButton(self) -> bool:
        """
        Get: AutoGenerateDeleteButton(self: GridView) -> bool
        Set: AutoGenerateDeleteButton(self: GridView) = value
        """
        ...

    @property
    def AutoGenerateEditButton(self) -> bool:
        """
        Get: AutoGenerateEditButton(self: GridView) -> bool
        Set: AutoGenerateEditButton(self: GridView) = value
        """
        ...

    @property
    def AutoGenerateSelectButton(self) -> bool:
        """
        Get: AutoGenerateSelectButton(self: GridView) -> bool
        Set: AutoGenerateSelectButton(self: GridView) = value
        """
        ...

    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: GridView) -> str
        Set: BackImageUrl(self: GridView) = value
        """
        ...

    @property
    def BottomPagerRow(self): # -> GridViewRow
        """ Get: BottomPagerRow(self: GridView) -> GridViewRow """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: GridView) -> str
        Set: Caption(self: GridView) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: GridView) -> TableCaptionAlign
        Set: CaptionAlign(self: GridView) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: GridView) -> int
        Set: CellPadding(self: GridView) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: GridView) -> int
        Set: CellSpacing(self: GridView) = value
        """
        ...

    @property
    def Columns(self) -> DataControlFieldCollection:
        """ Get: Columns(self: GridView) -> DataControlFieldCollection """
        ...

    @property
    def ColumnsGenerator(self) -> IAutoFieldGenerator:
        """
        Get: ColumnsGenerator(self: GridView) -> IAutoFieldGenerator
        Set: ColumnsGenerator(self: GridView) = value
        """
        ...

    @property
    def DataKeyNames(self) -> Array:
        """
        Get: DataKeyNames(self: GridView) -> Array[str]
        Set: DataKeyNames(self: GridView) = value
        """
        ...

    @property
    def EditIndex(self) -> int:
        """
        Get: EditIndex(self: GridView) -> int
        Set: EditIndex(self: GridView) = value
        """
        ...

    @property
    def EditRowStyle(self) -> TableItemStyle:
        """ Get: EditRowStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def EmptyDataRowStyle(self) -> TableItemStyle:
        """ Get: EmptyDataRowStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def EmptyDataTemplate(self) -> ITemplate:
        """
        Get: EmptyDataTemplate(self: GridView) -> ITemplate
        Set: EmptyDataTemplate(self: GridView) = value
        """
        ...

    @property
    def EmptyDataText(self) -> str:
        """
        Get: EmptyDataText(self: GridView) -> str
        Set: EmptyDataText(self: GridView) = value
        """
        ...

    @property
    def EnableModelValidation(self) -> bool:
        """
        Get: EnableModelValidation(self: GridView) -> bool
        Set: EnableModelValidation(self: GridView) = value
        """
        ...

    @property
    def EnableSortingAndPagingCallbacks(self) -> bool:
        """
        Get: EnableSortingAndPagingCallbacks(self: GridView) -> bool
        Set: EnableSortingAndPagingCallbacks(self: GridView) = value
        """
        ...

    @property
    def FooterRow(self): # -> GridViewRow
        """ Get: FooterRow(self: GridView) -> GridViewRow """
        ...

    @property
    def FooterStyle(self) -> TableItemStyle:
        """ Get: FooterStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def GridLines(self) -> GridLines:
        """
        Get: GridLines(self: GridView) -> GridLines
        Set: GridLines(self: GridView) = value
        """
        ...

    @property
    def HeaderRow(self): # -> GridViewRow
        """ Get: HeaderRow(self: GridView) -> GridViewRow """
        ...

    @property
    def HeaderStyle(self) -> TableItemStyle:
        """ Get: HeaderStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: GridView) -> HorizontalAlign
        Set: HorizontalAlign(self: GridView) = value
        """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: GridView) -> int """
        ...

    @property
    def PageIndex(self) -> int:
        """
        Get: PageIndex(self: GridView) -> int
        Set: PageIndex(self: GridView) = value
        """
        ...

    @property
    def PagerSettings(self): # -> PagerSettings
        """ Get: PagerSettings(self: GridView) -> PagerSettings """
        ...

    @property
    def PagerStyle(self) -> TableItemStyle:
        """ Get: PagerStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def PagerTemplate(self) -> ITemplate:
        """
        Get: PagerTemplate(self: GridView) -> ITemplate
        Set: PagerTemplate(self: GridView) = value
        """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: GridView) -> int
        Set: PageSize(self: GridView) = value
        """
        ...

    @property
    def RowHeaderColumn(self) -> str:
        """
        Get: RowHeaderColumn(self: GridView) -> str
        Set: RowHeaderColumn(self: GridView) = value
        """
        ...

    @property
    def Rows(self): # -> GridViewRowCollection
        """ Get: Rows(self: GridView) -> GridViewRowCollection """
        ...

    @property
    def RowStyle(self) -> TableItemStyle:
        """ Get: RowStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SelectedPersistedDataKey(self) -> DataKey:
        """
        Get: SelectedPersistedDataKey(self: GridView) -> DataKey
        Set: SelectedPersistedDataKey(self: GridView) = value
        """
        ...

    @property
    def SelectedRow(self): # -> GridViewRow
        """ Get: SelectedRow(self: GridView) -> GridViewRow """
        ...

    @property
    def SelectedRowStyle(self) -> TableItemStyle:
        """ Get: SelectedRowStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SelectedValue(self) -> object:
        """ Get: SelectedValue(self: GridView) -> object """
        ...

    @property
    def ShowFooter(self) -> bool:
        """
        Get: ShowFooter(self: GridView) -> bool
        Set: ShowFooter(self: GridView) = value
        """
        ...

    @property
    def ShowHeader(self) -> bool:
        """
        Get: ShowHeader(self: GridView) -> bool
        Set: ShowHeader(self: GridView) = value
        """
        ...

    @property
    def ShowHeaderWhenEmpty(self) -> bool:
        """
        Get: ShowHeaderWhenEmpty(self: GridView) -> bool
        Set: ShowHeaderWhenEmpty(self: GridView) = value
        """
        ...

    @property
    def SortDirection(self) -> SortDirection:
        """ Get: SortDirection(self: GridView) -> SortDirection """
        ...

    @property
    def SortedAscendingCellStyle(self) -> TableItemStyle:
        """ Get: SortedAscendingCellStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SortedAscendingHeaderStyle(self) -> TableItemStyle:
        """ Get: SortedAscendingHeaderStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SortedDescendingCellStyle(self) -> TableItemStyle:
        """ Get: SortedDescendingCellStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SortedDescendingHeaderStyle(self) -> TableItemStyle:
        """ Get: SortedDescendingHeaderStyle(self: GridView) -> TableItemStyle """
        ...

    @property
    def SortExpression(self) -> str:
        """ Get: SortExpression(self: GridView) -> str """
        ...

    @property
    def TopPagerRow(self): # -> GridViewRow
        """ Get: TopPagerRow(self: GridView) -> GridViewRow """
        ...

    @property
    def UseAccessibleHeader(self) -> bool:
        """
        Get: UseAccessibleHeader(self: GridView) -> bool
        Set: UseAccessibleHeader(self: GridView) = value
        """
        ...

    @property
    def VirtualItemCount(self) -> int:
        """
        Get: VirtualItemCount(self: GridView) -> int
        Set: VirtualItemCount(self: GridView) = value
        """
        ...


    def CreateAutoGeneratedColumn(self, *args): #cannot find CLR method
        """ CreateAutoGeneratedColumn(self: GridView, fieldProperties: AutoGeneratedFieldProperties) -> AutoGeneratedField """
        ...

    def CreateChildTable(self, *args): #cannot find CLR method
        """ CreateChildTable(self: GridView) -> Table """
        ...

    def CreateColumns(self, *args): #cannot find CLR method
        """ CreateColumns(self: GridView, dataSource: PagedDataSource, useDataSource: bool) -> ICollection """
        ...

    def CreateRow(self, *args): #cannot find CLR method
        """ CreateRow(self: GridView, rowIndex: int, dataSourceIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) -> GridViewRow """
        ...

    def DeleteRow(self, rowIndex:int): # -> 
        """ DeleteRow(self: GridView, rowIndex: int) """
        ...

    def ExtractRowValues(self, *args): #cannot find CLR method
        """ ExtractRowValues(self: GridView, fieldValues: IOrderedDictionary, row: GridViewRow, includeReadOnlyFields: bool, includePrimaryKey: bool) """
        ...

    def InitializePager(self, *args): #cannot find CLR method
        """ InitializePager(self: GridView, row: GridViewRow, columnSpan: int, pagedDataSource: PagedDataSource) """
        ...

    def InitializeRow(self, *args): #cannot find CLR method
        """ InitializeRow(self: GridView, row: GridViewRow, fields: Array[DataControlField]) """
        ...

    def IsBindableType(self, type:Type) -> bool:
        """ IsBindableType(self: GridView, type: Type) -> bool """
        ...

    def OnPageIndexChanged(self, *args): #cannot find CLR method
        """ OnPageIndexChanged(self: GridView, e: EventArgs) """
        ...

    def OnPageIndexChanging(self, *args): #cannot find CLR method
        """ OnPageIndexChanging(self: GridView, e: GridViewPageEventArgs) """
        ...

    def OnRowCancelingEdit(self, *args): #cannot find CLR method
        """ OnRowCancelingEdit(self: GridView, e: GridViewCancelEditEventArgs) """
        ...

    def OnRowCommand(self, *args): #cannot find CLR method
        """ OnRowCommand(self: GridView, e: GridViewCommandEventArgs) """
        ...

    def OnRowCreated(self, *args): #cannot find CLR method
        """ OnRowCreated(self: GridView, e: GridViewRowEventArgs) """
        ...

    def OnRowDataBound(self, *args): #cannot find CLR method
        """ OnRowDataBound(self: GridView, e: GridViewRowEventArgs) """
        ...

    def OnRowDeleted(self, *args): #cannot find CLR method
        """ OnRowDeleted(self: GridView, e: GridViewDeletedEventArgs) """
        ...

    def OnRowDeleting(self, *args): #cannot find CLR method
        """ OnRowDeleting(self: GridView, e: GridViewDeleteEventArgs) """
        ...

    def OnRowEditing(self, *args): #cannot find CLR method
        """ OnRowEditing(self: GridView, e: GridViewEditEventArgs) """
        ...

    def OnRowUpdated(self, *args): #cannot find CLR method
        """ OnRowUpdated(self: GridView, e: GridViewUpdatedEventArgs) """
        ...

    def OnRowUpdating(self, *args): #cannot find CLR method
        """ OnRowUpdating(self: GridView, e: GridViewUpdateEventArgs) """
        ...

    def OnSelectedIndexChanged(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanged(self: GridView, e: EventArgs) """
        ...

    def OnSelectedIndexChanging(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanging(self: GridView, e: GridViewSelectEventArgs) """
        ...

    def OnSorted(self, *args): #cannot find CLR method
        """ OnSorted(self: GridView, e: EventArgs) """
        ...

    def OnSorting(self, *args): #cannot find CLR method
        """ OnSorting(self: GridView, e: GridViewSortEventArgs) """
        ...

    def PrepareControlHierarchy(self, *args): #cannot find CLR method
        """ PrepareControlHierarchy(self: GridView) """
        ...

    def SelectRow(self, rowIndex:int): # -> 
        """ SelectRow(self: GridView, rowIndex: int) """
        ...

    def SetEditRow(self, rowIndex:int): # -> 
        """ SetEditRow(self: GridView, rowIndex: int) """
        ...

    def SetPageIndex(self, rowIndex:int): # -> 
        """ SetPageIndex(self: GridView, rowIndex: int) """
        ...

    def Sort(self, sortExpression:str, sortDirection:SortDirection): # -> 
        """ Sort(self: GridView, sortExpression: str, sortDirection: SortDirection) """
        ...

    def UpdateRow(self, rowIndex:int, causesValidation:bool): # -> 
        """ UpdateRow(self: GridView, rowIndex: int, causesValidation: bool) """
        ...

    PageIndexChanged = ...
    PageIndexChanging = ...
    RowCancelingEdit = ...
    RowCommand = ...
    RowCreated = ...
    RowDataBound = ...
    RowDeleted = ...
    RowDeleting = ...
    RowEditing = ...
    RowUpdated = ...
    RowUpdating = ...
    SelectedIndexChanged = ...
    SelectedIndexChanging = ...
    Sorted = ...
    Sorting = ...


class GridViewCancelEditEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewCancelEditEventArgs(rowIndex: int) """
    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: GridViewCancelEditEventArgs) -> int """
        ...



class GridViewCancelEditEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewCancelEditEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewCancelEditEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewCancelEditEventHandler, sender: object, e: GridViewCancelEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewCancelEditEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewCancelEditEventArgs): # -> 
        """ Invoke(self: GridViewCancelEditEventHandler, sender: object, e: GridViewCancelEditEventArgs) """
        ...


class GridViewColumnsGenerator(AutoFieldsGenerator): # skipped bases: <type 'IStateManager'>, <type 'IAutoFieldGenerator'>, <type 'object'>
    """ GridViewColumnsGenerator() """
    pass

class GridViewCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """
    GridViewCommandEventArgs(row: GridViewRow, commandSource: object, originalArgs: CommandEventArgs)
    GridViewCommandEventArgs(commandSource: object, originalArgs: CommandEventArgs)
    """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: GridViewCommandEventArgs) -> object """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: GridViewCommandEventArgs) -> bool
        Set: Handled(self: GridViewCommandEventArgs) = value
        """
        ...



class GridViewCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewCommandEventHandler, sender: object, e: GridViewCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewCommandEventArgs): # -> 
        """ Invoke(self: GridViewCommandEventHandler, sender: object, e: GridViewCommandEventArgs) """
        ...


class GridViewDeletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ GridViewDeletedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: GridViewDeletedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: GridViewDeletedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: GridViewDeletedEventArgs) -> bool
        Set: ExceptionHandled(self: GridViewDeletedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: GridViewDeletedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: GridViewDeletedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class GridViewDeletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewDeletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewDeletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewDeletedEventHandler, sender: object, e: GridViewDeletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewDeletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewDeletedEventArgs): # -> 
        """ Invoke(self: GridViewDeletedEventHandler, sender: object, e: GridViewDeletedEventArgs) """
        ...


class GridViewDeleteEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewDeleteEventArgs(rowIndex: int) """
    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: GridViewDeleteEventArgs) -> IOrderedDictionary """
        ...

    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: GridViewDeleteEventArgs) -> int """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: GridViewDeleteEventArgs) -> IOrderedDictionary """
        ...



class GridViewDeleteEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewDeleteEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewDeleteEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewDeleteEventHandler, sender: object, e: GridViewDeleteEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewDeleteEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewDeleteEventArgs): # -> 
        """ Invoke(self: GridViewDeleteEventHandler, sender: object, e: GridViewDeleteEventArgs) """
        ...


class GridViewEditEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewEditEventArgs(newEditIndex: int) """
    @property
    def NewEditIndex(self) -> int:
        """
        Get: NewEditIndex(self: GridViewEditEventArgs) -> int
        Set: NewEditIndex(self: GridViewEditEventArgs) = value
        """
        ...



class GridViewEditEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewEditEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewEditEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewEditEventHandler, sender: object, e: GridViewEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewEditEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewEditEventArgs): # -> 
        """ Invoke(self: GridViewEditEventHandler, sender: object, e: GridViewEditEventArgs) """
        ...


class GridViewPageEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewPageEventArgs(newPageIndex: int) """
    @property
    def NewPageIndex(self) -> int:
        """
        Get: NewPageIndex(self: GridViewPageEventArgs) -> int
        Set: NewPageIndex(self: GridViewPageEventArgs) = value
        """
        ...



class GridViewPageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewPageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewPageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewPageEventHandler, sender: object, e: GridViewPageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewPageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewPageEventArgs): # -> 
        """ Invoke(self: GridViewPageEventHandler, sender: object, e: GridViewPageEventArgs) """
        ...


class GridViewRow(TableRow, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ GridViewRow(rowIndex: int, dataItemIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: GridViewRow) -> int """
        ...

    @property
    def RowState(self) -> DataControlRowState:
        """
        Get: RowState(self: GridViewRow) -> DataControlRowState
        Set: RowState(self: GridViewRow) = value
        """
        ...

    @property
    def RowType(self) -> DataControlRowType:
        """
        Get: RowType(self: GridViewRow) -> DataControlRowType
        Set: RowType(self: GridViewRow) = value
        """
        ...


    def __new__(cls, rowIndex:int, dataItemIndex:int, rowType:DataControlRowType, rowState:DataControlRowState) -> Self:
        """ __new__(cls: type, rowIndex: int, dataItemIndex: int, rowType: DataControlRowType, rowState: DataControlRowState) """
        ...


class GridViewRowCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ GridViewRowCollection(rows: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: GridViewRowCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: GridViewRowCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class GridViewRowEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ GridViewRowEventArgs(row: GridViewRow) """
    @property
    def Row(self) -> GridViewRow:
        """ Get: Row(self: GridViewRowEventArgs) -> GridViewRow """
        ...


    def __new__(cls, row:GridViewRow) -> Self:
        """ __new__(cls: type, row: GridViewRow) """
        ...


class GridViewRowEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewRowEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewRowEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewRowEventHandler, sender: object, e: GridViewRowEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewRowEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewRowEventArgs): # -> 
        """ Invoke(self: GridViewRowEventHandler, sender: object, e: GridViewRowEventArgs) """
        ...


class GridViewSelectEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewSelectEventArgs(newSelectedIndex: int) """
    @property
    def NewSelectedIndex(self) -> int:
        """
        Get: NewSelectedIndex(self: GridViewSelectEventArgs) -> int
        Set: NewSelectedIndex(self: GridViewSelectEventArgs) = value
        """
        ...



class GridViewSelectEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewSelectEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewSelectEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewSelectEventHandler, sender: object, e: GridViewSelectEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewSelectEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewSelectEventArgs): # -> 
        """ Invoke(self: GridViewSelectEventHandler, sender: object, e: GridViewSelectEventArgs) """
        ...


class GridViewSortEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewSortEventArgs(sortExpression: str, sortDirection: SortDirection) """
    @property
    def SortDirection(self) -> SortDirection:
        """
        Get: SortDirection(self: GridViewSortEventArgs) -> SortDirection
        Set: SortDirection(self: GridViewSortEventArgs) = value
        """
        ...

    @property
    def SortExpression(self) -> str:
        """
        Get: SortExpression(self: GridViewSortEventArgs) -> str
        Set: SortExpression(self: GridViewSortEventArgs) = value
        """
        ...



class GridViewSortEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewSortEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewSortEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewSortEventHandler, sender: object, e: GridViewSortEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewSortEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewSortEventArgs): # -> 
        """ Invoke(self: GridViewSortEventHandler, sender: object, e: GridViewSortEventArgs) """
        ...


class GridViewUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ GridViewUpdatedEventArgs(affectedRows: int, e: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: GridViewUpdatedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: GridViewUpdatedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: GridViewUpdatedEventArgs) -> bool
        Set: ExceptionHandled(self: GridViewUpdatedEventArgs) = value
        """
        ...

    @property
    def KeepInEditMode(self) -> bool:
        """
        Get: KeepInEditMode(self: GridViewUpdatedEventArgs) -> bool
        Set: KeepInEditMode(self: GridViewUpdatedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: GridViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: GridViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: GridViewUpdatedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, e:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, e: Exception) """
        ...


class GridViewUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewUpdatedEventHandler, sender: object, e: GridViewUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewUpdatedEventArgs): # -> 
        """ Invoke(self: GridViewUpdatedEventHandler, sender: object, e: GridViewUpdatedEventArgs) """
        ...


class GridViewUpdateEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ GridViewUpdateEventArgs(rowIndex: int) """
    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: GridViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: GridViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: GridViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def RowIndex(self) -> int:
        """ Get: RowIndex(self: GridViewUpdateEventArgs) -> int """
        ...



class GridViewUpdateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GridViewUpdateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:GridViewUpdateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GridViewUpdateEventHandler, sender: object, e: GridViewUpdateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: GridViewUpdateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:GridViewUpdateEventArgs): # -> 
        """ Invoke(self: GridViewUpdateEventHandler, sender: object, e: GridViewUpdateEventArgs) """
        ...


class HiddenField(IPostBackDataHandler, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HiddenField() """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: HiddenField) -> str
        Set: Value(self: HiddenField) = value
        """
        ...


    def OnValueChanged(self, *args): #cannot find CLR method
        """ OnValueChanged(self: HiddenField, e: EventArgs) """
        ...

    ValueChanged = ...


class HierarchicalDataBoundControl(BaseDataBoundControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    def GetData(self, *args): #cannot find CLR method
        """ GetData(self: HierarchicalDataBoundControl, viewPath: str) -> HierarchicalDataSourceView """
        ...

    def GetDataSource(self, *args): #cannot find CLR method
        """ GetDataSource(self: HierarchicalDataBoundControl) -> IHierarchicalDataSource """
        ...

    def MarkAsDataBound(self, *args): #cannot find CLR method
        """ MarkAsDataBound(self: HierarchicalDataBoundControl) """
        ...

    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: HierarchicalDataBoundControl, sender: object, e: EventArgs) """
        ...

    def PerformDataBinding(self, *args): #cannot find CLR method
        """ PerformDataBinding(self: HierarchicalDataBoundControl) """
        ...


class HorizontalAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HorizontalAlign, values: Center (2), Justify (4), Left (1), NotSet (0), Right (3) """
    Center: HorizontalAlign = ...
    Justify: HorizontalAlign = ...
    Left: HorizontalAlign = ...
    NotSet: HorizontalAlign = ...
    Right: HorizontalAlign = ...
    value__ = ...


class HotSpotCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ HotSpotCollection() """
    def Add(self, spot:HotSpot) -> int:
        """ Add(self: HotSpotCollection, spot: HotSpot) -> int """
        ...

    def Insert(self, index:int, spot:HotSpot): # -> 
        """ Insert(self: HotSpotCollection, index: int, spot: HotSpot) """
        ...

    def Remove(self, spot:HotSpot): # -> 
        """ Remove(self: HotSpotCollection, spot: HotSpot) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HotSpotCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HotSpotMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HotSpotMode, values: Inactive (3), Navigate (1), NotSet (0), PostBack (2) """
    Inactive: HotSpotMode = ...
    Navigate: HotSpotMode = ...
    NotSet: HotSpotMode = ...
    PostBack: HotSpotMode = ...
    value__ = ...


class HyperLink(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ HyperLink() """
    @property
    def ImageHeight(self): # -> Unit
        """
        Get: ImageHeight(self: HyperLink) -> Unit
        Set: ImageHeight(self: HyperLink) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: HyperLink) -> str
        Set: ImageUrl(self: HyperLink) = value
        """
        ...

    @property
    def ImageWidth(self): # -> Unit
        """
        Get: ImageWidth(self: HyperLink) -> Unit
        Set: ImageWidth(self: HyperLink) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: HyperLink) -> str
        Set: NavigateUrl(self: HyperLink) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HyperLink) -> str
        Set: Target(self: HyperLink) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: HyperLink) -> str
        Set: Text(self: HyperLink) = value
        """
        ...



class HyperLinkColumn(DataGridColumn): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ HyperLinkColumn() """
    @property
    def DataNavigateUrlField(self) -> str:
        """
        Get: DataNavigateUrlField(self: HyperLinkColumn) -> str
        Set: DataNavigateUrlField(self: HyperLinkColumn) = value
        """
        ...

    @property
    def DataNavigateUrlFormatString(self) -> str:
        """
        Get: DataNavigateUrlFormatString(self: HyperLinkColumn) -> str
        Set: DataNavigateUrlFormatString(self: HyperLinkColumn) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: HyperLinkColumn) -> str
        Set: DataTextField(self: HyperLinkColumn) = value
        """
        ...

    @property
    def DataTextFormatString(self) -> str:
        """
        Get: DataTextFormatString(self: HyperLinkColumn) -> str
        Set: DataTextFormatString(self: HyperLinkColumn) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: HyperLinkColumn) -> str
        Set: NavigateUrl(self: HyperLinkColumn) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HyperLinkColumn) -> str
        Set: Target(self: HyperLinkColumn) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: HyperLinkColumn) -> str
        Set: Text(self: HyperLinkColumn) = value
        """
        ...


    def FormatDataNavigateUrlValue(self, *args): #cannot find CLR method
        """ FormatDataNavigateUrlValue(self: HyperLinkColumn, dataUrlValue: object) -> str """
        ...

    def FormatDataTextValue(self, *args): #cannot find CLR method
        """ FormatDataTextValue(self: HyperLinkColumn, dataTextValue: object) -> str """
        ...


class HyperLinkControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ HyperLinkControlBuilder() """
    pass

class HyperLinkField(DataControlField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ HyperLinkField() """
    @property
    def DataNavigateUrlFields(self) -> Array:
        """
        Get: DataNavigateUrlFields(self: HyperLinkField) -> Array[str]
        Set: DataNavigateUrlFields(self: HyperLinkField) = value
        """
        ...

    @property
    def DataNavigateUrlFormatString(self) -> str:
        """
        Get: DataNavigateUrlFormatString(self: HyperLinkField) -> str
        Set: DataNavigateUrlFormatString(self: HyperLinkField) = value
        """
        ...

    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: HyperLinkField) -> str
        Set: DataTextField(self: HyperLinkField) = value
        """
        ...

    @property
    def DataTextFormatString(self) -> str:
        """
        Get: DataTextFormatString(self: HyperLinkField) -> str
        Set: DataTextFormatString(self: HyperLinkField) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: HyperLinkField) -> str
        Set: NavigateUrl(self: HyperLinkField) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: HyperLinkField) -> str
        Set: Target(self: HyperLinkField) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: HyperLinkField) -> str
        Set: Text(self: HyperLinkField) = value
        """
        ...


    def FormatDataNavigateUrlValue(self, *args): #cannot find CLR method
        """ FormatDataNavigateUrlValue(self: HyperLinkField, dataUrlValues: Array[object]) -> str """
        ...

    def FormatDataTextValue(self, *args): #cannot find CLR method
        """ FormatDataTextValue(self: HyperLinkField, dataTextValue: object) -> str """
        ...


class Image(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Image() """
    @property
    def AlternateText(self) -> str:
        """
        Get: AlternateText(self: Image) -> str
        Set: AlternateText(self: Image) = value
        """
        ...

    @property
    def DescriptionUrl(self) -> str:
        """
        Get: DescriptionUrl(self: Image) -> str
        Set: DescriptionUrl(self: Image) = value
        """
        ...

    @property
    def GenerateEmptyAlternateText(self) -> bool:
        """
        Get: GenerateEmptyAlternateText(self: Image) -> bool
        Set: GenerateEmptyAlternateText(self: Image) = value
        """
        ...

    @property
    def ImageAlign(self): # -> ImageAlign
        """
        Get: ImageAlign(self: Image) -> ImageAlign
        Set: ImageAlign(self: Image) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: Image) -> str
        Set: ImageUrl(self: Image) = value
        """
        ...



class ImageAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImageAlign, values: AbsBottom (7), AbsMiddle (8), Baseline (3), Bottom (6), Left (1), Middle (5), NotSet (0), Right (2), TextTop (9), Top (4) """
    AbsBottom: ImageAlign = ...
    AbsMiddle: ImageAlign = ...
    Baseline: ImageAlign = ...
    Bottom: ImageAlign = ...
    Left: ImageAlign = ...
    Middle: ImageAlign = ...
    NotSet: ImageAlign = ...
    Right: ImageAlign = ...
    TextTop: ImageAlign = ...
    Top: ImageAlign = ...
    value__ = ...


class ImageButton(IPostBackDataHandler, IButtonControl, Image, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ImageButton() """
    @property
    def OnClientClick(self) -> str:
        """
        Get: OnClientClick(self: ImageButton) -> str
        Set: OnClientClick(self: ImageButton) = value
        """
        ...


    def GetPostBackOptions(self, *args): #cannot find CLR method
        """ GetPostBackOptions(self: ImageButton) -> PostBackOptions """
        ...

    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: ImageButton, e: ImageClickEventArgs) """
        ...

    def OnCommand(self, *args): #cannot find CLR method
        """ OnCommand(self: ImageButton, e: CommandEventArgs) """
        ...

    Click = ...
    Command = ...


class ImageField(DataControlField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ ImageField() """
    @property
    def AlternateText(self) -> str:
        """
        Get: AlternateText(self: ImageField) -> str
        Set: AlternateText(self: ImageField) = value
        """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: ImageField) -> bool
        Set: ConvertEmptyStringToNull(self: ImageField) = value
        """
        ...

    @property
    def DataAlternateTextField(self) -> str:
        """
        Get: DataAlternateTextField(self: ImageField) -> str
        Set: DataAlternateTextField(self: ImageField) = value
        """
        ...

    @property
    def DataAlternateTextFormatString(self) -> str:
        """
        Get: DataAlternateTextFormatString(self: ImageField) -> str
        Set: DataAlternateTextFormatString(self: ImageField) = value
        """
        ...

    @property
    def DataImageUrlField(self) -> str:
        """
        Get: DataImageUrlField(self: ImageField) -> str
        Set: DataImageUrlField(self: ImageField) = value
        """
        ...

    @property
    def DataImageUrlFormatString(self) -> str:
        """
        Get: DataImageUrlFormatString(self: ImageField) -> str
        Set: DataImageUrlFormatString(self: ImageField) = value
        """
        ...

    @property
    def NullDisplayText(self) -> str:
        """
        Get: NullDisplayText(self: ImageField) -> str
        Set: NullDisplayText(self: ImageField) = value
        """
        ...

    @property
    def NullImageUrl(self) -> str:
        """
        Get: NullImageUrl(self: ImageField) -> str
        Set: NullImageUrl(self: ImageField) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: ImageField) -> bool
        Set: ReadOnly(self: ImageField) = value
        """
        ...


    def FormatImageUrlValue(self, *args): #cannot find CLR method
        """ FormatImageUrlValue(self: ImageField, dataValue: object) -> str """
        ...

    def GetDesignTimeValue(self, *args): #cannot find CLR method
        """ GetDesignTimeValue(self: ImageField) -> str """
        ...

    def GetFormattedAlternateText(self, *args): #cannot find CLR method
        """ GetFormattedAlternateText(self: ImageField, controlContainer: Control) -> str """
        ...

    def GetValue(self, *args): #cannot find CLR method
        """ GetValue(self: ImageField, controlContainer: Control, fieldName: str, cachedDescriptor: PropertyDescriptor) -> (object, PropertyDescriptor) """
        ...

    def InitializeDataCell(self, *args): #cannot find CLR method
        """ InitializeDataCell(self: ImageField, cell: DataControlFieldCell, rowState: DataControlRowState) """
        ...

    def OnDataBindField(self, *args): #cannot find CLR method
        """ OnDataBindField(self: ImageField, sender: object, e: EventArgs) """
        ...

    ThisExpression: str = ...


class ImageMap(Image, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ImageMap() """
    @property
    def HotSpotMode(self) -> HotSpotMode:
        """
        Get: HotSpotMode(self: ImageMap) -> HotSpotMode
        Set: HotSpotMode(self: ImageMap) = value
        """
        ...

    @property
    def HotSpots(self) -> HotSpotCollection:
        """ Get: HotSpots(self: ImageMap) -> HotSpotCollection """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: ImageMap) -> str
        Set: Target(self: ImageMap) = value
        """
        ...


    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: ImageMap, e: ImageMapEventArgs) """
        ...

    Click = ...


class ImageMapEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ImageMapEventArgs(value: str) """
    @property
    def PostBackValue(self) -> str:
        """ Get: PostBackValue(self: ImageMapEventArgs) -> str """
        ...


    def __new__(cls, value:str) -> Self:
        """ __new__(cls: type, value: str) """
        ...


class ImageMapEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageMapEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ImageMapEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ImageMapEventHandler, sender: object, e: ImageMapEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ImageMapEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ImageMapEventArgs): # -> 
        """ Invoke(self: ImageMapEventHandler, sender: object, e: ImageMapEventArgs) """
        ...


class InsertItemPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InsertItemPosition, values: FirstItem (1), LastItem (2), None (0) """
    FirstItem: InsertItemPosition = ...
    LastItem: InsertItemPosition = ...
    value__ = ...


class IPageableItemContainer: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MaximumRows(self) -> int:
        """ Get: MaximumRows(self: IPageableItemContainer) -> int """
        ...

    @property
    def StartRowIndex(self) -> int:
        """ Get: StartRowIndex(self: IPageableItemContainer) -> int """
        ...


    def SetPageProperties(self, startRowIndex:int, maximumRows:int, databind:bool): # -> 
        """ SetPageProperties(self: IPageableItemContainer, startRowIndex: int, maximumRows: int, databind: bool) """
        ...

    TotalRowCountAvailable = ...


class LabelControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ LabelControlBuilder() """
    pass

class LinkButton(IButtonControl, WebControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ LinkButton() """
    @property
    def OnClientClick(self) -> str:
        """
        Get: OnClientClick(self: LinkButton) -> str
        Set: OnClientClick(self: LinkButton) = value
        """
        ...


    def GetPostBackOptions(self, *args): #cannot find CLR method
        """ GetPostBackOptions(self: LinkButton) -> PostBackOptions """
        ...

    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: LinkButton, e: EventArgs) """
        ...

    def OnCommand(self, *args): #cannot find CLR method
        """ OnCommand(self: LinkButton, e: CommandEventArgs) """
        ...

    Click = ...
    Command = ...


class LinkButtonControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ LinkButtonControlBuilder() """
    pass

class LinqDataSource(ContextDataSource, IDynamicDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IQueryableDataSource'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """ LinqDataSource() """
    @property
    def AutoGenerateOrderByClause(self) -> bool:
        """
        Get: AutoGenerateOrderByClause(self: LinqDataSource) -> bool
        Set: AutoGenerateOrderByClause(self: LinqDataSource) = value
        """
        ...

    @property
    def AutoPage(self) -> bool:
        """
        Get: AutoPage(self: LinqDataSource) -> bool
        Set: AutoPage(self: LinqDataSource) = value
        """
        ...

    @property
    def AutoSort(self) -> bool:
        """
        Get: AutoSort(self: LinqDataSource) -> bool
        Set: AutoSort(self: LinqDataSource) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def EnableObjectTracking(self) -> bool:
        """
        Get: EnableObjectTracking(self: LinqDataSource) -> bool
        Set: EnableObjectTracking(self: LinqDataSource) = value
        """
        ...

    @property
    def GroupBy(self) -> str:
        """
        Get: GroupBy(self: LinqDataSource) -> str
        Set: GroupBy(self: LinqDataSource) = value
        """
        ...

    @property
    def GroupByParameters(self) -> ParameterCollection:
        """ Get: GroupByParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def OrderBy(self) -> str:
        """
        Get: OrderBy(self: LinqDataSource) -> str
        Set: OrderBy(self: LinqDataSource) = value
        """
        ...

    @property
    def OrderByParameters(self) -> ParameterCollection:
        """ Get: OrderByParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def OrderGroupsBy(self) -> str:
        """
        Get: OrderGroupsBy(self: LinqDataSource) -> str
        Set: OrderGroupsBy(self: LinqDataSource) = value
        """
        ...

    @property
    def OrderGroupsByParameters(self) -> ParameterCollection:
        """ Get: OrderGroupsByParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def Select(self) -> str:
        """
        Get: Select(self: LinqDataSource) -> str
        Set: Select(self: LinqDataSource) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: LinqDataSource) -> ParameterCollection """
        ...

    @property
    def StoreOriginalValuesInViewState(self) -> bool:
        """
        Get: StoreOriginalValuesInViewState(self: LinqDataSource) -> bool
        Set: StoreOriginalValuesInViewState(self: LinqDataSource) = value
        """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: LinqDataSource) -> str
        Set: TableName(self: LinqDataSource) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: LinqDataSource) -> ParameterCollection """
        ...


    def CreateView(self, *args): #cannot find CLR method
        """ CreateView(self: LinqDataSource) -> LinqDataSourceView """
        ...

    def Delete(self, keys:IDictionary, oldValues:IDictionary) -> int:
        """ Delete(self: LinqDataSource, keys: IDictionary, oldValues: IDictionary) -> int """
        ...

    def Insert(self, values:IDictionary) -> int:
        """ Insert(self: LinqDataSource, values: IDictionary) -> int """
        ...

    def Update(self, keys:IDictionary, values:IDictionary, oldValues:IDictionary) -> int:
        """ Update(self: LinqDataSource, keys: IDictionary, values: IDictionary, oldValues: IDictionary) -> int """
        ...

    ContextCreated = ...
    ContextCreating = ...
    ContextDisposing = ...
    Deleted = ...
    Deleting = ...
    Inserted = ...
    Inserting = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class LinqDataSourceContextEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    LinqDataSourceContextEventArgs()
    LinqDataSourceContextEventArgs(operation: DataSourceOperation)
    """
    @property
    def ObjectInstance(self) -> object:
        """
        Get: ObjectInstance(self: LinqDataSourceContextEventArgs) -> object
        Set: ObjectInstance(self: LinqDataSourceContextEventArgs) = value
        """
        ...

    @property
    def Operation(self) -> DataSourceOperation:
        """ Get: Operation(self: LinqDataSourceContextEventArgs) -> DataSourceOperation """
        ...


    def __new__(cls, operation:DataSourceOperation = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, operation: DataSourceOperation)
        """
        ...


class LinqDataSourceDeleteEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """
    LinqDataSourceDeleteEventArgs(originalObject: object)
    LinqDataSourceDeleteEventArgs(exception: LinqDataSourceValidationException)
    """
    @property
    def Exception(self) -> LinqDataSourceValidationException:
        """ Get: Exception(self: LinqDataSourceDeleteEventArgs) -> LinqDataSourceValidationException """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: LinqDataSourceDeleteEventArgs) -> bool
        Set: ExceptionHandled(self: LinqDataSourceDeleteEventArgs) = value
        """
        ...

    @property
    def OriginalObject(self) -> object:
        """ Get: OriginalObject(self: LinqDataSourceDeleteEventArgs) -> object """
        ...



class LinqDataSourceDisposeEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ LinqDataSourceDisposeEventArgs(instance: object) """
    @property
    def ObjectInstance(self) -> object:
        """ Get: ObjectInstance(self: LinqDataSourceDisposeEventArgs) -> object """
        ...



class LinqDataSourceInsertEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """
    LinqDataSourceInsertEventArgs(newObject: object)
    LinqDataSourceInsertEventArgs(exception: LinqDataSourceValidationException)
    """
    @property
    def Exception(self) -> LinqDataSourceValidationException:
        """ Get: Exception(self: LinqDataSourceInsertEventArgs) -> LinqDataSourceValidationException """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: LinqDataSourceInsertEventArgs) -> bool
        Set: ExceptionHandled(self: LinqDataSourceInsertEventArgs) = value
        """
        ...

    @property
    def NewObject(self) -> object:
        """ Get: NewObject(self: LinqDataSourceInsertEventArgs) -> object """
        ...



class LinqDataSourceSelectEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ LinqDataSourceSelectEventArgs(arguments: DataSourceSelectArguments, whereParameters: IDictionary[str, object], orderByParameters: IOrderedDictionary, groupByParameters: IDictionary[str, object], orderGroupsByParameters: IDictionary[str, object], selectParameters: IDictionary[str, object]) """
    @property
    def Arguments(self) -> DataSourceSelectArguments:
        """ Get: Arguments(self: LinqDataSourceSelectEventArgs) -> DataSourceSelectArguments """
        ...

    @property
    def GroupByParameters(self) -> IDictionary:
        """ Get: GroupByParameters(self: LinqDataSourceSelectEventArgs) -> IDictionary[str, object] """
        ...

    @property
    def OrderByParameters(self) -> IOrderedDictionary:
        """ Get: OrderByParameters(self: LinqDataSourceSelectEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OrderGroupsByParameters(self) -> IDictionary:
        """ Get: OrderGroupsByParameters(self: LinqDataSourceSelectEventArgs) -> IDictionary[str, object] """
        ...

    @property
    def Result(self) -> object:
        """
        Get: Result(self: LinqDataSourceSelectEventArgs) -> object
        Set: Result(self: LinqDataSourceSelectEventArgs) = value
        """
        ...

    @property
    def SelectParameters(self) -> IDictionary:
        """ Get: SelectParameters(self: LinqDataSourceSelectEventArgs) -> IDictionary[str, object] """
        ...

    @property
    def WhereParameters(self) -> IDictionary:
        """ Get: WhereParameters(self: LinqDataSourceSelectEventArgs) -> IDictionary[str, object] """
        ...



class LinqDataSourceStatusEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    LinqDataSourceStatusEventArgs(result: object)
    LinqDataSourceStatusEventArgs(result: object, totalRowCount: int)
    LinqDataSourceStatusEventArgs(exception: Exception)
    """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: LinqDataSourceStatusEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: LinqDataSourceStatusEventArgs) -> bool
        Set: ExceptionHandled(self: LinqDataSourceStatusEventArgs) = value
        """
        ...

    @property
    def Result(self) -> object:
        """ Get: Result(self: LinqDataSourceStatusEventArgs) -> object """
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: LinqDataSourceStatusEventArgs) -> int """
        ...


    def __new__(cls, *__args:object) -> Self:
        """
        __new__(cls: type, result: object)
        __new__(cls: type, result: object, totalRowCount: int)
        __new__(cls: type, exception: Exception)
        """
        ...


class LinqDataSourceUpdateEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """
    LinqDataSourceUpdateEventArgs(originalObject: object, newObject: object)
    LinqDataSourceUpdateEventArgs(exception: LinqDataSourceValidationException)
    """
    @property
    def Exception(self) -> LinqDataSourceValidationException:
        """ Get: Exception(self: LinqDataSourceUpdateEventArgs) -> LinqDataSourceValidationException """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: LinqDataSourceUpdateEventArgs) -> bool
        Set: ExceptionHandled(self: LinqDataSourceUpdateEventArgs) = value
        """
        ...

    @property
    def NewObject(self) -> object:
        """ Get: NewObject(self: LinqDataSourceUpdateEventArgs) -> object """
        ...

    @property
    def OriginalObject(self) -> object:
        """ Get: OriginalObject(self: LinqDataSourceUpdateEventArgs) -> object """
        ...



class LinqDataSourceValidationException(IDynamicValidatorException, Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LinqDataSourceValidationException()
    LinqDataSourceValidationException(message: str)
    LinqDataSourceValidationException(message: str, innerException: Exception)
    LinqDataSourceValidationException(message: str, innerExceptions: IDictionary[str, Exception])
    """
    SerializeObjectState = ...


class LinqDataSourceView(ContextDataSourceView): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ LinqDataSourceView(owner: LinqDataSource, name: str, context: HttpContext) """
    @property
    def CanDelete(self) -> bool:
        """ Get: CanDelete(self: LinqDataSourceView) -> bool """
        ...

    @property
    def CanInsert(self) -> bool:
        """ Get: CanInsert(self: LinqDataSourceView) -> bool """
        ...

    @property
    def CanPage(self) -> bool:
        """ Get: CanPage(self: LinqDataSourceView) -> bool """
        ...

    @property
    def CanRetrieveTotalRowCount(self) -> bool:
        """ Get: CanRetrieveTotalRowCount(self: LinqDataSourceView) -> bool """
        ...

    @property
    def CanSort(self) -> bool:
        """ Get: CanSort(self: LinqDataSourceView) -> bool """
        ...

    @property
    def CanUpdate(self) -> bool:
        """ Get: CanUpdate(self: LinqDataSourceView) -> bool """
        ...

    @property
    def EnableDelete(self) -> bool:
        """
        Get: EnableDelete(self: LinqDataSourceView) -> bool
        Set: EnableDelete(self: LinqDataSourceView) = value
        """
        ...

    @property
    def EnableInsert(self) -> bool:
        """
        Get: EnableInsert(self: LinqDataSourceView) -> bool
        Set: EnableInsert(self: LinqDataSourceView) = value
        """
        ...

    @property
    def EnableObjectTracking(self) -> bool:
        """
        Get: EnableObjectTracking(self: LinqDataSourceView) -> bool
        Set: EnableObjectTracking(self: LinqDataSourceView) = value
        """
        ...

    @property
    def EnableUpdate(self) -> bool:
        """
        Get: EnableUpdate(self: LinqDataSourceView) -> bool
        Set: EnableUpdate(self: LinqDataSourceView) = value
        """
        ...

    @property
    def StoreOriginalValuesInViewState(self) -> bool:
        """
        Get: StoreOriginalValuesInViewState(self: LinqDataSourceView) -> bool
        Set: StoreOriginalValuesInViewState(self: LinqDataSourceView) = value
        """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: LinqDataSourceView) -> str
        Set: TableName(self: LinqDataSourceView) = value
        """
        ...


    def DeleteDataObject(self, *args): #cannot find CLR method
        """ DeleteDataObject(self: LinqDataSourceView, dataContext: object, table: object, oldDataObject: object) """
        ...

    def GetTableMemberInfo(self, *args): #cannot find CLR method
        """ GetTableMemberInfo(self: LinqDataSourceView, contextType: Type) -> MemberInfo """
        ...

    def InsertDataObject(self, *args): #cannot find CLR method
        """ InsertDataObject(self: LinqDataSourceView, dataContext: object, table: object, newDataObject: object) """
        ...

    def OnContextCreated(self, *args): #cannot find CLR method
        """ OnContextCreated(self: LinqDataSourceView, e: LinqDataSourceStatusEventArgs) """
        ...

    def OnContextCreating(self, *args): #cannot find CLR method
        """ OnContextCreating(self: LinqDataSourceView, e: LinqDataSourceContextEventArgs) """
        ...

    def OnContextDisposing(self, *args): #cannot find CLR method
        """ OnContextDisposing(self: LinqDataSourceView, e: LinqDataSourceDisposeEventArgs) """
        ...

    def OnDeleted(self, *args): #cannot find CLR method
        """ OnDeleted(self: LinqDataSourceView, e: LinqDataSourceStatusEventArgs) """
        ...

    def OnDeleting(self, *args): #cannot find CLR method
        """ OnDeleting(self: LinqDataSourceView, e: LinqDataSourceDeleteEventArgs) """
        ...

    def OnException(self, *args): #cannot find CLR method
        """ OnException(self: LinqDataSourceView, e: DynamicValidatorEventArgs) """
        ...

    def OnInserted(self, *args): #cannot find CLR method
        """ OnInserted(self: LinqDataSourceView, e: LinqDataSourceStatusEventArgs) """
        ...

    def OnInserting(self, *args): #cannot find CLR method
        """ OnInserting(self: LinqDataSourceView, e: LinqDataSourceInsertEventArgs) """
        ...

    def OnSelected(self, *args): #cannot find CLR method
        """ OnSelected(self: LinqDataSourceView, e: LinqDataSourceStatusEventArgs) """
        ...

    def OnSelecting(self, *args): #cannot find CLR method
        """ OnSelecting(self: LinqDataSourceView, e: LinqDataSourceSelectEventArgs) """
        ...

    def OnUpdated(self, *args): #cannot find CLR method
        """ OnUpdated(self: LinqDataSourceView, e: LinqDataSourceStatusEventArgs) """
        ...

    def OnUpdating(self, *args): #cannot find CLR method
        """ OnUpdating(self: LinqDataSourceView, e: LinqDataSourceUpdateEventArgs) """
        ...

    def ResetDataObject(self, *args): #cannot find CLR method
        """ ResetDataObject(self: LinqDataSourceView, table: object, dataObject: object) """
        ...

    def Select(self, arguments, callback=None) -> IEnumerable:
        """ Select(self: LinqDataSourceView, arguments: DataSourceSelectArguments) -> IEnumerable """
        ...

    def UpdateDataObject(self, *args): #cannot find CLR method
        """ UpdateDataObject(self: LinqDataSourceView, dataContext: object, table: object, oldDataObject: object, newDataObject: object) """
        ...

    def ValidateContextType(self, *args): #cannot find CLR method
        """ ValidateContextType(self: LinqDataSourceView, contextType: Type, selecting: bool) """
        ...

    def ValidateDeleteSupported(self, *args): #cannot find CLR method
        """ ValidateDeleteSupported(self: LinqDataSourceView, keys: IDictionary, oldValues: IDictionary) """
        ...

    def ValidateEditSupported(self, *args): #cannot find CLR method
        """ ValidateEditSupported(self: LinqDataSourceView) """
        ...

    def ValidateInsertSupported(self, *args): #cannot find CLR method
        """ ValidateInsertSupported(self: LinqDataSourceView, values: IDictionary) """
        ...

    def ValidateTableType(self, *args): #cannot find CLR method
        """ ValidateTableType(self: LinqDataSourceView, tableType: Type, selecting: bool) """
        ...

    def ValidateUpdateSupported(self, *args): #cannot find CLR method
        """ ValidateUpdateSupported(self: LinqDataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary) """
        ...

    ContextCreated = ...
    ContextCreating = ...
    ContextDisposing = ...
    Deleted = ...
    Deleting = ...
    Inserted = ...
    Inserting = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class ListBox(IPostBackDataHandler, ListControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IEditableTextControl'>, <type 'object'>
    """ ListBox() """
    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: ListBox) -> Color
        Set: BorderColor(self: ListBox) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: ListBox) -> BorderStyle
        Set: BorderStyle(self: ListBox) = value
        """
        ...

    @property
    def BorderWidth(self): # -> Unit
        """
        Get: BorderWidth(self: ListBox) -> Unit
        Set: BorderWidth(self: ListBox) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: ListBox) -> int
        Set: Rows(self: ListBox) = value
        """
        ...

    @property
    def SelectionMode(self): # -> ListSelectionMode
        """
        Get: SelectionMode(self: ListBox) -> ListSelectionMode
        Set: SelectionMode(self: ListBox) = value
        """
        ...


    def GetSelectedIndices(self) -> Array:
        """ GetSelectedIndices(self: ListBox) -> Array[int] """
        ...


class ListItem(IAttributeAccessor, IStateManager, IParserAccessor): # skipped bases: <type 'object'>
    """
    ListItem()
    ListItem(text: str)
    ListItem(text: str, value: str)
    ListItem(text: str, value: str, enabled: bool)
    """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: ListItem) -> AttributeCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ListItem) -> bool
        Set: Enabled(self: ListItem) = value
        """
        ...

    @property
    def Selected(self) -> bool:
        """
        Get: Selected(self: ListItem) -> bool
        Set: Selected(self: ListItem) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ListItem) -> str
        Set: Text(self: ListItem) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: ListItem) -> str
        Set: Value(self: ListItem) = value
        """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: ListItem, o: object) -> bool """
        ...

    @staticmethod
    def FromString(s:str) -> ListItem:
        """ FromString(s: str) -> ListItem """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ListItem) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: ListItem) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ListItemCollection(IList, IStateManager): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ListItemCollection() """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: ListItemCollection) -> int
        Set: Capacity(self: ListItemCollection) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ListItemCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: ListItemCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: ListItemCollection) -> object """
        ...


    def AddRange(self, items:Array): # -> 
        """ AddRange(self: ListItemCollection, items: Array[ListItem]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ListItemCollection, array: Array, index: int) """
        ...

    def FindByText(self, text:str) -> ListItem:
        """ FindByText(self: ListItemCollection, text: str) -> ListItem """
        ...

    def FindByValue(self, value:str) -> ListItem:
        """ FindByValue(self: ListItemCollection, value: str) -> ListItem """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ListItemCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class ListItemControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ ListItemControlBuilder() """
    pass

class ListItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListItemType, values: AlternatingItem (3), EditItem (5), Footer (1), Header (0), Item (2), Pager (7), SelectedItem (4), Separator (6) """
    AlternatingItem: ListItemType = ...
    EditItem: ListItemType = ...
    Footer: ListItemType = ...
    Header: ListItemType = ...
    Item: ListItemType = ...
    Pager: ListItemType = ...
    SelectedItem: ListItemType = ...
    Separator: ListItemType = ...
    value__ = ...


class ListSelectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListSelectionMode, values: Multiple (1), Single (0) """
    Multiple: ListSelectionMode = ...
    Single: ListSelectionMode = ...
    value__ = ...


class ListView(IPageableItemContainer, IDataKeysControl, DataBoundControl, IWizardSideBarListControl, IPersistedSelector, INamingContainer, IDataBoundListControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataBoundControl'>, <type 'object'>
    """ ListView() """
    @property
    def AccessKey(self) -> str:
        """
        Get: AccessKey(self: ListView) -> str
        Set: AccessKey(self: ListView) = value
        """
        ...

    @property
    def AlternatingItemTemplate(self) -> ITemplate:
        """
        Get: AlternatingItemTemplate(self: ListView) -> ITemplate
        Set: AlternatingItemTemplate(self: ListView) = value
        """
        ...

    @property
    def BackColor(self) -> Color:
        """
        Get: BackColor(self: ListView) -> Color
        Set: BackColor(self: ListView) = value
        """
        ...

    @property
    def BorderColor(self) -> Color:
        """
        Get: BorderColor(self: ListView) -> Color
        Set: BorderColor(self: ListView) = value
        """
        ...

    @property
    def BorderStyle(self) -> BorderStyle:
        """
        Get: BorderStyle(self: ListView) -> BorderStyle
        Set: BorderStyle(self: ListView) = value
        """
        ...

    @property
    def BorderWidth(self): # -> Unit
        """
        Get: BorderWidth(self: ListView) -> Unit
        Set: BorderWidth(self: ListView) = value
        """
        ...

    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: ListView) -> ControlCollection """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: ListView) -> bool
        Set: ConvertEmptyStringToNull(self: ListView) = value
        """
        ...

    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: ListView) -> str
        Set: CssClass(self: ListView) = value
        """
        ...

    @property
    def DataKeyNames(self) -> Array:
        """
        Get: DataKeyNames(self: ListView) -> Array[str]
        Set: DataKeyNames(self: ListView) = value
        """
        ...

    @property
    def DeleteMethod(self) -> str:
        """
        Get: DeleteMethod(self: ListView) -> str
        Set: DeleteMethod(self: ListView) = value
        """
        ...

    @property
    def EditIndex(self) -> int:
        """
        Get: EditIndex(self: ListView) -> int
        Set: EditIndex(self: ListView) = value
        """
        ...

    @property
    def EditItem(self) -> ListViewItem:
        """ Get: EditItem(self: ListView) -> ListViewItem """
        ...

    @property
    def EditItemTemplate(self) -> ITemplate:
        """
        Get: EditItemTemplate(self: ListView) -> ITemplate
        Set: EditItemTemplate(self: ListView) = value
        """
        ...

    @property
    def EmptyDataTemplate(self) -> ITemplate:
        """
        Get: EmptyDataTemplate(self: ListView) -> ITemplate
        Set: EmptyDataTemplate(self: ListView) = value
        """
        ...

    @property
    def EmptyItemTemplate(self) -> ITemplate:
        """
        Get: EmptyItemTemplate(self: ListView) -> ITemplate
        Set: EmptyItemTemplate(self: ListView) = value
        """
        ...

    @property
    def EnableModelValidation(self) -> bool:
        """
        Get: EnableModelValidation(self: ListView) -> bool
        Set: EnableModelValidation(self: ListView) = value
        """
        ...

    @property
    def Font(self) -> FontInfo:
        """ Get: Font(self: ListView) -> FontInfo """
        ...

    @property
    def ForeColor(self) -> Color:
        """
        Get: ForeColor(self: ListView) -> Color
        Set: ForeColor(self: ListView) = value
        """
        ...

    @property
    def GroupItemCount(self) -> int:
        """
        Get: GroupItemCount(self: ListView) -> int
        Set: GroupItemCount(self: ListView) = value
        """
        ...

    @property
    def GroupPlaceholderID(self) -> str:
        """
        Get: GroupPlaceholderID(self: ListView) -> str
        Set: GroupPlaceholderID(self: ListView) = value
        """
        ...

    @property
    def GroupSeparatorTemplate(self) -> ITemplate:
        """
        Get: GroupSeparatorTemplate(self: ListView) -> ITemplate
        Set: GroupSeparatorTemplate(self: ListView) = value
        """
        ...

    @property
    def GroupTemplate(self) -> ITemplate:
        """
        Get: GroupTemplate(self: ListView) -> ITemplate
        Set: GroupTemplate(self: ListView) = value
        """
        ...

    @property
    def Height(self): # -> Unit
        """
        Get: Height(self: ListView) -> Unit
        Set: Height(self: ListView) = value
        """
        ...

    @property
    def InsertItem(self) -> ListViewItem:
        """ Get: InsertItem(self: ListView) -> ListViewItem """
        ...

    @property
    def InsertItemPosition(self) -> InsertItemPosition:
        """
        Get: InsertItemPosition(self: ListView) -> InsertItemPosition
        Set: InsertItemPosition(self: ListView) = value
        """
        ...

    @property
    def InsertItemTemplate(self) -> ITemplate:
        """
        Get: InsertItemTemplate(self: ListView) -> ITemplate
        Set: InsertItemTemplate(self: ListView) = value
        """
        ...

    @property
    def InsertMethod(self) -> str:
        """
        Get: InsertMethod(self: ListView) -> str
        Set: InsertMethod(self: ListView) = value
        """
        ...

    @property
    def ItemPlaceholderID(self) -> str:
        """
        Get: ItemPlaceholderID(self: ListView) -> str
        Set: ItemPlaceholderID(self: ListView) = value
        """
        ...

    @property
    def Items(self) -> IList:
        """ Get: Items(self: ListView) -> IList[ListViewDataItem] """
        ...

    @property
    def ItemSeparatorTemplate(self) -> ITemplate:
        """
        Get: ItemSeparatorTemplate(self: ListView) -> ITemplate
        Set: ItemSeparatorTemplate(self: ListView) = value
        """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: ListView) -> ITemplate
        Set: ItemTemplate(self: ListView) = value
        """
        ...

    @property
    def LayoutTemplate(self) -> ITemplate:
        """
        Get: LayoutTemplate(self: ListView) -> ITemplate
        Set: LayoutTemplate(self: ListView) = value
        """
        ...

    @property
    def SelectedItemTemplate(self) -> ITemplate:
        """
        Get: SelectedItemTemplate(self: ListView) -> ITemplate
        Set: SelectedItemTemplate(self: ListView) = value
        """
        ...

    @property
    def SelectedPersistedDataKey(self) -> DataKey:
        """
        Get: SelectedPersistedDataKey(self: ListView) -> DataKey
        Set: SelectedPersistedDataKey(self: ListView) = value
        """
        ...

    @property
    def SelectedValue(self) -> object:
        """ Get: SelectedValue(self: ListView) -> object """
        ...

    @property
    def SortDirection(self) -> SortDirection:
        """ Get: SortDirection(self: ListView) -> SortDirection """
        ...

    @property
    def SortExpression(self) -> str:
        """ Get: SortExpression(self: ListView) -> str """
        ...

    @property
    def TabIndex(self) -> Int16:
        """
        Get: TabIndex(self: ListView) -> Int16
        Set: TabIndex(self: ListView) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: ListView) -> str
        Set: ToolTip(self: ListView) = value
        """
        ...

    @property
    def UpdateMethod(self) -> str:
        """
        Get: UpdateMethod(self: ListView) -> str
        Set: UpdateMethod(self: ListView) = value
        """
        ...

    @property
    def Width(self): # -> Unit
        """
        Get: Width(self: ListView) -> Unit
        Set: Width(self: ListView) = value
        """
        ...


    def AddControlToContainer(self, *args): #cannot find CLR method
        """ AddControlToContainer(self: ListView, control: Control, container: Control, addLocation: int) """
        ...

    def CreateDataItem(self, *args): #cannot find CLR method
        """ CreateDataItem(self: ListView, dataItemIndex: int, displayIndex: int) -> ListViewDataItem """
        ...

    def CreateEmptyDataItem(self, *args): #cannot find CLR method
        """ CreateEmptyDataItem(self: ListView) """
        ...

    def CreateEmptyItem(self, *args): #cannot find CLR method
        """ CreateEmptyItem(self: ListView) -> ListViewItem """
        ...

    def CreateInsertItem(self, *args): #cannot find CLR method
        """ CreateInsertItem(self: ListView) -> ListViewItem """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: ListView, itemType: ListViewItemType) -> ListViewItem """
        ...

    def CreateItemsInGroups(self, *args): #cannot find CLR method
        """ CreateItemsInGroups(self: ListView, dataSource: ListViewPagedDataSource, dataBinding: bool, insertPosition: InsertItemPosition, keyArray: ArrayList) -> IList[ListViewDataItem] """
        ...

    def CreateItemsWithoutGroups(self, *args): #cannot find CLR method
        """ CreateItemsWithoutGroups(self: ListView, dataSource: ListViewPagedDataSource, dataBinding: bool, insertPosition: InsertItemPosition, keyArray: ArrayList) -> IList[ListViewDataItem] """
        ...

    def CreateLayoutTemplate(self, *args): #cannot find CLR method
        """ CreateLayoutTemplate(self: ListView) """
        ...

    def CreateSuffixArrayList(self, *args): #cannot find CLR method
        """ CreateSuffixArrayList(self: ListView, dataSource: ListViewPagedDataSource, suffixArray: ArrayList) """
        ...

    def DeleteItem(self, itemIndex:int): # -> 
        """ DeleteItem(self: ListView, itemIndex: int) """
        ...

    def EnsureLayoutTemplate(self, *args): #cannot find CLR method
        """ EnsureLayoutTemplate(self: ListView) """
        ...

    def ExtractItemValues(self, itemValues:IOrderedDictionary, item:ListViewItem, includePrimaryKey:bool): # -> 
        """ ExtractItemValues(self: ListView, itemValues: IOrderedDictionary, item: ListViewItem, includePrimaryKey: bool) """
        ...

    def FindPlaceholder(self, *args): #cannot find CLR method
        """ FindPlaceholder(self: ListView, containerID: str, container: Control) -> Control """
        ...

    def InsertNewItem(self, causesValidation:bool): # -> 
        """ InsertNewItem(self: ListView, causesValidation: bool) """
        ...

    def InstantiateEmptyDataTemplate(self, *args): #cannot find CLR method
        """ InstantiateEmptyDataTemplate(self: ListView, container: Control) """
        ...

    def InstantiateEmptyItemTemplate(self, *args): #cannot find CLR method
        """ InstantiateEmptyItemTemplate(self: ListView, container: Control) """
        ...

    def InstantiateGroupSeparatorTemplate(self, *args): #cannot find CLR method
        """ InstantiateGroupSeparatorTemplate(self: ListView, container: Control) """
        ...

    def InstantiateGroupTemplate(self, *args): #cannot find CLR method
        """ InstantiateGroupTemplate(self: ListView, container: Control) """
        ...

    def InstantiateInsertItemTemplate(self, *args): #cannot find CLR method
        """ InstantiateInsertItemTemplate(self: ListView, container: Control) """
        ...

    def InstantiateItemSeparatorTemplate(self, *args): #cannot find CLR method
        """ InstantiateItemSeparatorTemplate(self: ListView, container: Control) """
        ...

    def InstantiateItemTemplate(self, *args): #cannot find CLR method
        """ InstantiateItemTemplate(self: ListView, container: Control, displayIndex: int) """
        ...

    def OnItemCanceling(self, *args): #cannot find CLR method
        """ OnItemCanceling(self: ListView, e: ListViewCancelEventArgs) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: ListView, e: ListViewCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: ListView, e: ListViewItemEventArgs) """
        ...

    def OnItemDataBound(self, *args): #cannot find CLR method
        """ OnItemDataBound(self: ListView, e: ListViewItemEventArgs) """
        ...

    def OnItemDeleted(self, *args): #cannot find CLR method
        """ OnItemDeleted(self: ListView, e: ListViewDeletedEventArgs) """
        ...

    def OnItemDeleting(self, *args): #cannot find CLR method
        """ OnItemDeleting(self: ListView, e: ListViewDeleteEventArgs) """
        ...

    def OnItemEditing(self, *args): #cannot find CLR method
        """ OnItemEditing(self: ListView, e: ListViewEditEventArgs) """
        ...

    def OnItemInserted(self, *args): #cannot find CLR method
        """ OnItemInserted(self: ListView, e: ListViewInsertedEventArgs) """
        ...

    def OnItemInserting(self, *args): #cannot find CLR method
        """ OnItemInserting(self: ListView, e: ListViewInsertEventArgs) """
        ...

    def OnItemUpdated(self, *args): #cannot find CLR method
        """ OnItemUpdated(self: ListView, e: ListViewUpdatedEventArgs) """
        ...

    def OnItemUpdating(self, *args): #cannot find CLR method
        """ OnItemUpdating(self: ListView, e: ListViewUpdateEventArgs) """
        ...

    def OnLayoutCreated(self, *args): #cannot find CLR method
        """ OnLayoutCreated(self: ListView, e: EventArgs) """
        ...

    def OnPagePropertiesChanged(self, *args): #cannot find CLR method
        """ OnPagePropertiesChanged(self: ListView, e: EventArgs) """
        ...

    def OnPagePropertiesChanging(self, *args): #cannot find CLR method
        """ OnPagePropertiesChanging(self: ListView, e: PagePropertiesChangingEventArgs) """
        ...

    def OnSelectedIndexChanged(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanged(self: ListView, e: EventArgs) """
        ...

    def OnSelectedIndexChanging(self, *args): #cannot find CLR method
        """ OnSelectedIndexChanging(self: ListView, e: ListViewSelectEventArgs) """
        ...

    def OnSorted(self, *args): #cannot find CLR method
        """ OnSorted(self: ListView, e: EventArgs) """
        ...

    def OnSorting(self, *args): #cannot find CLR method
        """ OnSorting(self: ListView, e: ListViewSortEventArgs) """
        ...

    def OnTotalRowCountAvailable(self, *args): #cannot find CLR method
        """ OnTotalRowCountAvailable(self: ListView, e: PageEventArgs) """
        ...

    def RemoveItems(self, *args): #cannot find CLR method
        """ RemoveItems(self: ListView) """
        ...

    def SelectItem(self, rowIndex:int): # -> 
        """ SelectItem(self: ListView, rowIndex: int) """
        ...

    def SetEditItem(self, rowIndex:int): # -> 
        """ SetEditItem(self: ListView, rowIndex: int) """
        ...

    def Sort(self, sortExpression:str, sortDirection:SortDirection): # -> 
        """ Sort(self: ListView, sortExpression: str, sortDirection: SortDirection) """
        ...

    def UpdateItem(self, itemIndex:int, causesValidation:bool): # -> 
        """ UpdateItem(self: ListView, itemIndex: int, causesValidation: bool) """
        ...

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        ...

    ItemCanceling = ...
    ItemCommand = ...
    ItemCreated = ...
    ItemDataBound = ...
    ItemDeleted = ...
    ItemDeleting = ...
    ItemEditing = ...
    ItemInserted = ...
    ItemInserting = ...
    ItemUpdated = ...
    ItemUpdating = ...
    LayoutCreated = ...
    PagePropertiesChanged = ...
    PagePropertiesChanging = ...
    SelectedIndexChanged = ...
    SelectedIndexChanging = ...
    Sorted = ...
    Sorting = ...


class ListViewCancelEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewCancelEventArgs(itemIndex: int, cancelMode: ListViewCancelMode) """
    @property
    def CancelMode(self) -> ListViewCancelMode:
        """ Get: CancelMode(self: ListViewCancelEventArgs) -> ListViewCancelMode """
        ...

    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: ListViewCancelEventArgs) -> int """
        ...



class ListViewCancelMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListViewCancelMode, values: CancelingEdit (0), CancelingInsert (1) """
    CancelingEdit: ListViewCancelMode = ...
    CancelingInsert: ListViewCancelMode = ...
    value__ = ...


class ListViewCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ ListViewCommandEventArgs(item: ListViewItem, commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: ListViewCommandEventArgs) -> object """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: ListViewCommandEventArgs) -> bool
        Set: Handled(self: ListViewCommandEventArgs) = value
        """
        ...

    @property
    def Item(self) -> ListViewItem:
        """ Get: Item(self: ListViewCommandEventArgs) -> ListViewItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ListViewItem(Control, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ ListViewItem(itemType: ListViewItemType) """
    @property
    def ItemType(self) -> ListViewItemType:
        """ Get: ItemType(self: ListViewItem) -> ListViewItemType """
        ...


    def __new__(cls, itemType:ListViewItemType) -> Self:
        """ __new__(cls: type, itemType: ListViewItemType) """
        ...


class ListViewDataItem(ListViewItem): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IDataItemContainer'>, <type 'object'>
    """ ListViewDataItem(dataItemIndex: int, displayIndex: int) """
    pass

class ListViewDeletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ListViewDeletedEventArgs(affectedRows: int, exception: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: ListViewDeletedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ListViewDeletedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: ListViewDeletedEventArgs) -> bool
        Set: ExceptionHandled(self: ListViewDeletedEventArgs) = value
        """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: ListViewDeletedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: ListViewDeletedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, exception:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, exception: Exception) """
        ...


class ListViewDeleteEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewDeleteEventArgs(itemIndex: int) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: ListViewDeleteEventArgs) -> int """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: ListViewDeleteEventArgs) -> IOrderedDictionary """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: ListViewDeleteEventArgs) -> IOrderedDictionary """
        ...



class ListViewEditEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewEditEventArgs(newEditIndex: int) """
    @property
    def NewEditIndex(self) -> int:
        """ Get: NewEditIndex(self: ListViewEditEventArgs) -> int """
        ...



class ListViewInsertedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ListViewInsertedEventArgs(affectedRows: int, exception: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: ListViewInsertedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ListViewInsertedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: ListViewInsertedEventArgs) -> bool
        Set: ExceptionHandled(self: ListViewInsertedEventArgs) = value
        """
        ...

    @property
    def KeepInInsertMode(self) -> bool:
        """
        Get: KeepInInsertMode(self: ListViewInsertedEventArgs) -> bool
        Set: KeepInInsertMode(self: ListViewInsertedEventArgs) = value
        """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: ListViewInsertedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, exception:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, exception: Exception) """
        ...


class ListViewInsertEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewInsertEventArgs(item: ListViewItem) """
    @property
    def Item(self) -> ListViewItem:
        """ Get: Item(self: ListViewInsertEventArgs) -> ListViewItem """
        ...

    @property
    def Values(self) -> IOrderedDictionary:
        """ Get: Values(self: ListViewInsertEventArgs) -> IOrderedDictionary """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ListViewItemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ListViewItemEventArgs(item: ListViewItem) """
    @property
    def Item(self) -> ListViewItem:
        """ Get: Item(self: ListViewItemEventArgs) -> ListViewItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, item:ListViewItem) -> Self:
        """ __new__(cls: type, item: ListViewItem) """
        ...


class ListViewItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ListViewItemType, values: DataItem (0), EmptyItem (2), InsertItem (1) """
    DataItem: ListViewItemType = ...
    EmptyItem: ListViewItemType = ...
    InsertItem: ListViewItemType = ...
    value__ = ...


class ListViewPagedDataSource(ITypedList, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ListViewPagedDataSource() """
    @property
    def AllowServerPaging(self) -> bool:
        """
        Get: AllowServerPaging(self: ListViewPagedDataSource) -> bool
        Set: AllowServerPaging(self: ListViewPagedDataSource) = value
        """
        ...

    @property
    def DataSource(self) -> IEnumerable:
        """
        Get: DataSource(self: ListViewPagedDataSource) -> IEnumerable
        Set: DataSource(self: ListViewPagedDataSource) = value
        """
        ...

    @property
    def DataSourceCount(self) -> int:
        """ Get: DataSourceCount(self: ListViewPagedDataSource) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ListViewPagedDataSource) -> bool """
        ...

    @property
    def IsServerPagingEnabled(self) -> bool:
        """ Get: IsServerPagingEnabled(self: ListViewPagedDataSource) -> bool """
        ...

    @property
    def MaximumRows(self) -> int:
        """
        Get: MaximumRows(self: ListViewPagedDataSource) -> int
        Set: MaximumRows(self: ListViewPagedDataSource) = value
        """
        ...

    @property
    def StartRowIndex(self) -> int:
        """
        Get: StartRowIndex(self: ListViewPagedDataSource) -> int
        Set: StartRowIndex(self: ListViewPagedDataSource) = value
        """
        ...

    @property
    def TotalRowCount(self) -> int:
        """
        Get: TotalRowCount(self: ListViewPagedDataSource) -> int
        Set: TotalRowCount(self: ListViewPagedDataSource) = value
        """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ListViewPagedDataSource) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ListViewSelectEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewSelectEventArgs(newSelectedIndex: int) """
    @property
    def NewSelectedIndex(self) -> int:
        """
        Get: NewSelectedIndex(self: ListViewSelectEventArgs) -> int
        Set: NewSelectedIndex(self: ListViewSelectEventArgs) = value
        """
        ...



class ListViewSortEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewSortEventArgs(sortExpression: str, sortDirection: SortDirection) """
    @property
    def SortDirection(self) -> SortDirection:
        """
        Get: SortDirection(self: ListViewSortEventArgs) -> SortDirection
        Set: SortDirection(self: ListViewSortEventArgs) = value
        """
        ...

    @property
    def SortExpression(self) -> str:
        """
        Get: SortExpression(self: ListViewSortEventArgs) -> str
        Set: SortExpression(self: ListViewSortEventArgs) = value
        """
        ...



class ListViewUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ListViewUpdatedEventArgs(affectedRows: int, exception: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: ListViewUpdatedEventArgs) -> int """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ListViewUpdatedEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: ListViewUpdatedEventArgs) -> bool
        Set: ExceptionHandled(self: ListViewUpdatedEventArgs) = value
        """
        ...

    @property
    def KeepInEditMode(self) -> bool:
        """
        Get: KeepInEditMode(self: ListViewUpdatedEventArgs) -> bool
        Set: KeepInEditMode(self: ListViewUpdatedEventArgs) = value
        """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: ListViewUpdatedEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: ListViewUpdatedEventArgs) -> IOrderedDictionary """
        ...


    def __new__(cls, affectedRows:int, exception:Exception) -> Self:
        """ __new__(cls: type, affectedRows: int, exception: Exception) """
        ...


class ListViewUpdateEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ListViewUpdateEventArgs(itemIndex: int) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: ListViewUpdateEventArgs) -> int """
        ...

    @property
    def Keys(self) -> IOrderedDictionary:
        """ Get: Keys(self: ListViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def NewValues(self) -> IOrderedDictionary:
        """ Get: NewValues(self: ListViewUpdateEventArgs) -> IOrderedDictionary """
        ...

    @property
    def OldValues(self) -> IOrderedDictionary:
        """ Get: OldValues(self: ListViewUpdateEventArgs) -> IOrderedDictionary """
        ...



class Literal(Control, ITextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Literal() """
    @property
    def Mode(self): # -> LiteralMode
        """
        Get: Mode(self: Literal) -> LiteralMode
        Set: Mode(self: Literal) = value
        """
        ...



class LiteralControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ LiteralControlBuilder() """
    pass

class LiteralMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LiteralMode, values: Encode (2), PassThrough (1), Transform (0) """
    Encode: LiteralMode = ...
    PassThrough: LiteralMode = ...
    Transform: LiteralMode = ...
    value__ = ...


class Localize(Literal): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'object'>
    """ Localize() """
    pass

class Login(CompositeControl, IBorderPaddingControl, IRenderOuterTableControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ Login() """
    @property
    def BorderPadding(self) -> int:
        """
        Get: BorderPadding(self: Login) -> int
        Set: BorderPadding(self: Login) = value
        """
        ...

    @property
    def CheckBoxStyle(self) -> TableItemStyle:
        """ Get: CheckBoxStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def CreateUserIconUrl(self) -> str:
        """
        Get: CreateUserIconUrl(self: Login) -> str
        Set: CreateUserIconUrl(self: Login) = value
        """
        ...

    @property
    def CreateUserText(self) -> str:
        """
        Get: CreateUserText(self: Login) -> str
        Set: CreateUserText(self: Login) = value
        """
        ...

    @property
    def CreateUserUrl(self) -> str:
        """
        Get: CreateUserUrl(self: Login) -> str
        Set: CreateUserUrl(self: Login) = value
        """
        ...

    @property
    def DestinationPageUrl(self) -> str:
        """
        Get: DestinationPageUrl(self: Login) -> str
        Set: DestinationPageUrl(self: Login) = value
        """
        ...

    @property
    def DisplayRememberMe(self) -> bool:
        """
        Get: DisplayRememberMe(self: Login) -> bool
        Set: DisplayRememberMe(self: Login) = value
        """
        ...

    @property
    def FailureAction(self): # -> LoginFailureAction
        """
        Get: FailureAction(self: Login) -> LoginFailureAction
        Set: FailureAction(self: Login) = value
        """
        ...

    @property
    def FailureText(self) -> str:
        """
        Get: FailureText(self: Login) -> str
        Set: FailureText(self: Login) = value
        """
        ...

    @property
    def FailureTextStyle(self) -> TableItemStyle:
        """ Get: FailureTextStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def HelpPageIconUrl(self) -> str:
        """
        Get: HelpPageIconUrl(self: Login) -> str
        Set: HelpPageIconUrl(self: Login) = value
        """
        ...

    @property
    def HelpPageText(self) -> str:
        """
        Get: HelpPageText(self: Login) -> str
        Set: HelpPageText(self: Login) = value
        """
        ...

    @property
    def HelpPageUrl(self) -> str:
        """
        Get: HelpPageUrl(self: Login) -> str
        Set: HelpPageUrl(self: Login) = value
        """
        ...

    @property
    def HyperLinkStyle(self) -> TableItemStyle:
        """ Get: HyperLinkStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def InstructionText(self) -> str:
        """
        Get: InstructionText(self: Login) -> str
        Set: InstructionText(self: Login) = value
        """
        ...

    @property
    def InstructionTextStyle(self) -> TableItemStyle:
        """ Get: InstructionTextStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def LabelStyle(self) -> TableItemStyle:
        """ Get: LabelStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def LayoutTemplate(self) -> ITemplate:
        """
        Get: LayoutTemplate(self: Login) -> ITemplate
        Set: LayoutTemplate(self: Login) = value
        """
        ...

    @property
    def LoginButtonImageUrl(self) -> str:
        """
        Get: LoginButtonImageUrl(self: Login) -> str
        Set: LoginButtonImageUrl(self: Login) = value
        """
        ...

    @property
    def LoginButtonStyle(self) -> Style:
        """ Get: LoginButtonStyle(self: Login) -> Style """
        ...

    @property
    def LoginButtonText(self) -> str:
        """
        Get: LoginButtonText(self: Login) -> str
        Set: LoginButtonText(self: Login) = value
        """
        ...

    @property
    def LoginButtonType(self) -> ButtonType:
        """
        Get: LoginButtonType(self: Login) -> ButtonType
        Set: LoginButtonType(self: Login) = value
        """
        ...

    @property
    def MembershipProvider(self) -> str:
        """
        Get: MembershipProvider(self: Login) -> str
        Set: MembershipProvider(self: Login) = value
        """
        ...

    @property
    def Orientation(self) -> Orientation:
        """
        Get: Orientation(self: Login) -> Orientation
        Set: Orientation(self: Login) = value
        """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: Login) -> str """
        ...

    @property
    def PasswordLabelText(self) -> str:
        """
        Get: PasswordLabelText(self: Login) -> str
        Set: PasswordLabelText(self: Login) = value
        """
        ...

    @property
    def PasswordRecoveryIconUrl(self) -> str:
        """
        Get: PasswordRecoveryIconUrl(self: Login) -> str
        Set: PasswordRecoveryIconUrl(self: Login) = value
        """
        ...

    @property
    def PasswordRecoveryText(self) -> str:
        """
        Get: PasswordRecoveryText(self: Login) -> str
        Set: PasswordRecoveryText(self: Login) = value
        """
        ...

    @property
    def PasswordRecoveryUrl(self) -> str:
        """
        Get: PasswordRecoveryUrl(self: Login) -> str
        Set: PasswordRecoveryUrl(self: Login) = value
        """
        ...

    @property
    def PasswordRequiredErrorMessage(self) -> str:
        """
        Get: PasswordRequiredErrorMessage(self: Login) -> str
        Set: PasswordRequiredErrorMessage(self: Login) = value
        """
        ...

    @property
    def RememberMeSet(self) -> bool:
        """
        Get: RememberMeSet(self: Login) -> bool
        Set: RememberMeSet(self: Login) = value
        """
        ...

    @property
    def RememberMeText(self) -> str:
        """
        Get: RememberMeText(self: Login) -> str
        Set: RememberMeText(self: Login) = value
        """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: Login) -> bool
        Set: RenderOuterTable(self: Login) = value
        """
        ...

    @property
    def TextBoxStyle(self) -> Style:
        """ Get: TextBoxStyle(self: Login) -> Style """
        ...

    @property
    def TextLayout(self): # -> LoginTextLayout
        """
        Get: TextLayout(self: Login) -> LoginTextLayout
        Set: TextLayout(self: Login) = value
        """
        ...

    @property
    def TitleText(self) -> str:
        """
        Get: TitleText(self: Login) -> str
        Set: TitleText(self: Login) = value
        """
        ...

    @property
    def TitleTextStyle(self) -> TableItemStyle:
        """ Get: TitleTextStyle(self: Login) -> TableItemStyle """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: Login) -> str
        Set: UserName(self: Login) = value
        """
        ...

    @property
    def UserNameLabelText(self) -> str:
        """
        Get: UserNameLabelText(self: Login) -> str
        Set: UserNameLabelText(self: Login) = value
        """
        ...

    @property
    def UserNameRequiredErrorMessage(self) -> str:
        """
        Get: UserNameRequiredErrorMessage(self: Login) -> str
        Set: UserNameRequiredErrorMessage(self: Login) = value
        """
        ...

    @property
    def ValidatorTextStyle(self) -> Style:
        """ Get: ValidatorTextStyle(self: Login) -> Style """
        ...

    @property
    def VisibleWhenLoggedIn(self) -> bool:
        """
        Get: VisibleWhenLoggedIn(self: Login) -> bool
        Set: VisibleWhenLoggedIn(self: Login) = value
        """
        ...


    def OnAuthenticate(self, *args): #cannot find CLR method
        """ OnAuthenticate(self: Login, e: AuthenticateEventArgs) """
        ...

    def OnLoggedIn(self, *args): #cannot find CLR method
        """ OnLoggedIn(self: Login, e: EventArgs) """
        ...

    def OnLoggingIn(self, *args): #cannot find CLR method
        """ OnLoggingIn(self: Login, e: LoginCancelEventArgs) """
        ...

    def OnLoginError(self, *args): #cannot find CLR method
        """ OnLoginError(self: Login, e: EventArgs) """
        ...

    Authenticate = ...
    LoggedIn = ...
    LoggingIn = ...
    LoginButtonCommandName: str = ...
    LoginError = ...


class LoginCancelEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    LoginCancelEventArgs()
    LoginCancelEventArgs(cancel: bool)
    """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: LoginCancelEventArgs) -> bool
        Set: Cancel(self: LoginCancelEventArgs) = value
        """
        ...


    def __new__(cls, cancel:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cancel: bool)
        """
        ...


class LoginCancelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ LoginCancelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:LoginCancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: LoginCancelEventHandler, sender: object, e: LoginCancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: LoginCancelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:LoginCancelEventArgs): # -> 
        """ Invoke(self: LoginCancelEventHandler, sender: object, e: LoginCancelEventArgs) """
        ...


class LoginFailureAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoginFailureAction, values: RedirectToLoginPage (1), Refresh (0) """
    RedirectToLoginPage: LoginFailureAction = ...
    Refresh: LoginFailureAction = ...
    value__ = ...


class LoginName(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ LoginName() """
    @property
    def FormatString(self) -> str:
        """
        Get: FormatString(self: LoginName) -> str
        Set: FormatString(self: LoginName) = value
        """
        ...



class LoginStatus(CompositeControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ LoginStatus() """
    @property
    def LoginImageUrl(self) -> str:
        """
        Get: LoginImageUrl(self: LoginStatus) -> str
        Set: LoginImageUrl(self: LoginStatus) = value
        """
        ...

    @property
    def LoginText(self) -> str:
        """
        Get: LoginText(self: LoginStatus) -> str
        Set: LoginText(self: LoginStatus) = value
        """
        ...

    @property
    def LogoutAction(self): # -> LogoutAction
        """
        Get: LogoutAction(self: LoginStatus) -> LogoutAction
        Set: LogoutAction(self: LoginStatus) = value
        """
        ...

    @property
    def LogoutImageUrl(self) -> str:
        """
        Get: LogoutImageUrl(self: LoginStatus) -> str
        Set: LogoutImageUrl(self: LoginStatus) = value
        """
        ...

    @property
    def LogoutPageUrl(self) -> str:
        """
        Get: LogoutPageUrl(self: LoginStatus) -> str
        Set: LogoutPageUrl(self: LoginStatus) = value
        """
        ...

    @property
    def LogoutText(self) -> str:
        """
        Get: LogoutText(self: LoginStatus) -> str
        Set: LogoutText(self: LoginStatus) = value
        """
        ...


    def OnLoggedOut(self, *args): #cannot find CLR method
        """ OnLoggedOut(self: LoginStatus, e: EventArgs) """
        ...

    def OnLoggingOut(self, *args): #cannot find CLR method
        """ OnLoggingOut(self: LoginStatus, e: LoginCancelEventArgs) """
        ...

    LoggedOut = ...
    LoggingOut = ...


class LoginTextLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoginTextLayout, values: TextOnLeft (0), TextOnTop (1) """
    TextOnLeft: LoginTextLayout = ...
    TextOnTop: LoginTextLayout = ...
    value__ = ...


class LoginView(Control, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ LoginView() """
    @property
    def AnonymousTemplate(self) -> ITemplate:
        """
        Get: AnonymousTemplate(self: LoginView) -> ITemplate
        Set: AnonymousTemplate(self: LoginView) = value
        """
        ...

    @property
    def LoggedInTemplate(self) -> ITemplate:
        """
        Get: LoggedInTemplate(self: LoginView) -> ITemplate
        Set: LoggedInTemplate(self: LoginView) = value
        """
        ...

    @property
    def RoleGroups(self): # -> RoleGroupCollection
        """ Get: RoleGroups(self: LoginView) -> RoleGroupCollection """
        ...


    def OnViewChanged(self, *args): #cannot find CLR method
        """ OnViewChanged(self: LoginView, e: EventArgs) """
        ...

    def OnViewChanging(self, *args): #cannot find CLR method
        """ OnViewChanging(self: LoginView, e: EventArgs) """
        ...

    ViewChanged = ...
    ViewChanging = ...


class LogoutAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogoutAction, values: Redirect (1), RedirectToLoginPage (2), Refresh (0) """
    Redirect: LogoutAction = ...
    RedirectToLoginPage: LogoutAction = ...
    Refresh: LogoutAction = ...
    value__ = ...


class MailDefinition(IStateManager): # skipped bases: <type 'object'>
    """ MailDefinition() """
    @property
    def BodyFileName(self) -> str:
        """
        Get: BodyFileName(self: MailDefinition) -> str
        Set: BodyFileName(self: MailDefinition) = value
        """
        ...

    @property
    def CC(self) -> str:
        """
        Get: CC(self: MailDefinition) -> str
        Set: CC(self: MailDefinition) = value
        """
        ...

    @property
    def EmbeddedObjects(self) -> EmbeddedMailObjectsCollection:
        """ Get: EmbeddedObjects(self: MailDefinition) -> EmbeddedMailObjectsCollection """
        ...

    @property
    def From(self) -> str:
        """
        Get: From(self: MailDefinition) -> str
        Set: From(self: MailDefinition) = value
        """
        ...

    @property
    def IsBodyHtml(self) -> bool:
        """
        Get: IsBodyHtml(self: MailDefinition) -> bool
        Set: IsBodyHtml(self: MailDefinition) = value
        """
        ...

    @property
    def Priority(self) -> MailPriority:
        """
        Get: Priority(self: MailDefinition) -> MailPriority
        Set: Priority(self: MailDefinition) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: MailDefinition) -> str
        Set: Subject(self: MailDefinition) = value
        """
        ...


    def CreateMailMessage(self, recipients:str, replacements:IDictionary, *__args:Control) -> MailMessage:
        """
        CreateMailMessage(self: MailDefinition, recipients: str, replacements: IDictionary, owner: Control) -> MailMessage
        CreateMailMessage(self: MailDefinition, recipients: str, replacements: IDictionary, body: str, owner: Control) -> MailMessage
        """
        ...


class MailMessageEventArgs(LoginCancelEventArgs): # skipped bases: <type 'object'>
    """ MailMessageEventArgs(message: MailMessage) """
    @property
    def Message(self) -> MailMessage:
        """ Get: Message(self: MailMessageEventArgs) -> MailMessage """
        ...



class MailMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MailMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MailMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MailMessageEventHandler, sender: object, e: MailMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MailMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MailMessageEventArgs): # -> 
        """ Invoke(self: MailMessageEventHandler, sender: object, e: MailMessageEventArgs) """
        ...


class Menu(HierarchicalDataBoundControl, IPostBackEventHandler, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Menu() """
    @property
    def Controls(self) -> ControlCollection:
        """ Get: Controls(self: Menu) -> ControlCollection """
        ...

    @property
    def DisappearAfter(self) -> int:
        """
        Get: DisappearAfter(self: Menu) -> int
        Set: DisappearAfter(self: Menu) = value
        """
        ...

    @property
    def DynamicBottomSeparatorImageUrl(self) -> str:
        """
        Get: DynamicBottomSeparatorImageUrl(self: Menu) -> str
        Set: DynamicBottomSeparatorImageUrl(self: Menu) = value
        """
        ...

    @property
    def DynamicEnableDefaultPopOutImage(self) -> bool:
        """
        Get: DynamicEnableDefaultPopOutImage(self: Menu) -> bool
        Set: DynamicEnableDefaultPopOutImage(self: Menu) = value
        """
        ...

    @property
    def DynamicHorizontalOffset(self) -> int:
        """
        Get: DynamicHorizontalOffset(self: Menu) -> int
        Set: DynamicHorizontalOffset(self: Menu) = value
        """
        ...

    @property
    def DynamicHoverStyle(self) -> Style:
        """ Get: DynamicHoverStyle(self: Menu) -> Style """
        ...

    @property
    def DynamicItemFormatString(self) -> str:
        """
        Get: DynamicItemFormatString(self: Menu) -> str
        Set: DynamicItemFormatString(self: Menu) = value
        """
        ...

    @property
    def DynamicItemTemplate(self) -> ITemplate:
        """
        Get: DynamicItemTemplate(self: Menu) -> ITemplate
        Set: DynamicItemTemplate(self: Menu) = value
        """
        ...

    @property
    def DynamicMenuItemStyle(self): # -> MenuItemStyle
        """ Get: DynamicMenuItemStyle(self: Menu) -> MenuItemStyle """
        ...

    @property
    def DynamicMenuStyle(self): # -> SubMenuStyle
        """ Get: DynamicMenuStyle(self: Menu) -> SubMenuStyle """
        ...

    @property
    def DynamicPopOutImageTextFormatString(self) -> str:
        """
        Get: DynamicPopOutImageTextFormatString(self: Menu) -> str
        Set: DynamicPopOutImageTextFormatString(self: Menu) = value
        """
        ...

    @property
    def DynamicPopOutImageUrl(self) -> str:
        """
        Get: DynamicPopOutImageUrl(self: Menu) -> str
        Set: DynamicPopOutImageUrl(self: Menu) = value
        """
        ...

    @property
    def DynamicSelectedStyle(self): # -> MenuItemStyle
        """ Get: DynamicSelectedStyle(self: Menu) -> MenuItemStyle """
        ...

    @property
    def DynamicTopSeparatorImageUrl(self) -> str:
        """
        Get: DynamicTopSeparatorImageUrl(self: Menu) -> str
        Set: DynamicTopSeparatorImageUrl(self: Menu) = value
        """
        ...

    @property
    def DynamicVerticalOffset(self) -> int:
        """
        Get: DynamicVerticalOffset(self: Menu) -> int
        Set: DynamicVerticalOffset(self: Menu) = value
        """
        ...

    @property
    def IncludeStyleBlock(self) -> bool:
        """
        Get: IncludeStyleBlock(self: Menu) -> bool
        Set: IncludeStyleBlock(self: Menu) = value
        """
        ...

    @property
    def Items(self): # -> MenuItemCollection
        """ Get: Items(self: Menu) -> MenuItemCollection """
        ...

    @property
    def ItemWrap(self) -> bool:
        """
        Get: ItemWrap(self: Menu) -> bool
        Set: ItemWrap(self: Menu) = value
        """
        ...

    @property
    def LevelMenuItemStyles(self): # -> MenuItemStyleCollection
        """ Get: LevelMenuItemStyles(self: Menu) -> MenuItemStyleCollection """
        ...

    @property
    def LevelSelectedStyles(self): # -> MenuItemStyleCollection
        """ Get: LevelSelectedStyles(self: Menu) -> MenuItemStyleCollection """
        ...

    @property
    def LevelSubMenuStyles(self): # -> SubMenuStyleCollection
        """ Get: LevelSubMenuStyles(self: Menu) -> SubMenuStyleCollection """
        ...

    @property
    def MaximumDynamicDisplayLevels(self) -> int:
        """
        Get: MaximumDynamicDisplayLevels(self: Menu) -> int
        Set: MaximumDynamicDisplayLevels(self: Menu) = value
        """
        ...

    @property
    def Orientation(self) -> Orientation:
        """
        Get: Orientation(self: Menu) -> Orientation
        Set: Orientation(self: Menu) = value
        """
        ...

    @property
    def PathSeparator(self) -> Char:
        """
        Get: PathSeparator(self: Menu) -> Char
        Set: PathSeparator(self: Menu) = value
        """
        ...

    @property
    def RenderingMode(self): # -> MenuRenderingMode
        """
        Get: RenderingMode(self: Menu) -> MenuRenderingMode
        Set: RenderingMode(self: Menu) = value
        """
        ...

    @property
    def ScrollDownImageUrl(self) -> str:
        """
        Get: ScrollDownImageUrl(self: Menu) -> str
        Set: ScrollDownImageUrl(self: Menu) = value
        """
        ...

    @property
    def ScrollDownText(self) -> str:
        """
        Get: ScrollDownText(self: Menu) -> str
        Set: ScrollDownText(self: Menu) = value
        """
        ...

    @property
    def ScrollUpImageUrl(self) -> str:
        """
        Get: ScrollUpImageUrl(self: Menu) -> str
        Set: ScrollUpImageUrl(self: Menu) = value
        """
        ...

    @property
    def ScrollUpText(self) -> str:
        """
        Get: ScrollUpText(self: Menu) -> str
        Set: ScrollUpText(self: Menu) = value
        """
        ...

    @property
    def SelectedItem(self) -> MenuItem:
        """ Get: SelectedItem(self: Menu) -> MenuItem """
        ...

    @property
    def SelectedValue(self) -> str:
        """ Get: SelectedValue(self: Menu) -> str """
        ...

    @property
    def SkipLinkText(self) -> str:
        """
        Get: SkipLinkText(self: Menu) -> str
        Set: SkipLinkText(self: Menu) = value
        """
        ...

    @property
    def StaticBottomSeparatorImageUrl(self) -> str:
        """
        Get: StaticBottomSeparatorImageUrl(self: Menu) -> str
        Set: StaticBottomSeparatorImageUrl(self: Menu) = value
        """
        ...

    @property
    def StaticDisplayLevels(self) -> int:
        """
        Get: StaticDisplayLevels(self: Menu) -> int
        Set: StaticDisplayLevels(self: Menu) = value
        """
        ...

    @property
    def StaticEnableDefaultPopOutImage(self) -> bool:
        """
        Get: StaticEnableDefaultPopOutImage(self: Menu) -> bool
        Set: StaticEnableDefaultPopOutImage(self: Menu) = value
        """
        ...

    @property
    def StaticHoverStyle(self) -> Style:
        """ Get: StaticHoverStyle(self: Menu) -> Style """
        ...

    @property
    def StaticItemFormatString(self) -> str:
        """
        Get: StaticItemFormatString(self: Menu) -> str
        Set: StaticItemFormatString(self: Menu) = value
        """
        ...

    @property
    def StaticItemTemplate(self) -> ITemplate:
        """
        Get: StaticItemTemplate(self: Menu) -> ITemplate
        Set: StaticItemTemplate(self: Menu) = value
        """
        ...

    @property
    def StaticMenuItemStyle(self): # -> MenuItemStyle
        """ Get: StaticMenuItemStyle(self: Menu) -> MenuItemStyle """
        ...

    @property
    def StaticMenuStyle(self): # -> SubMenuStyle
        """ Get: StaticMenuStyle(self: Menu) -> SubMenuStyle """
        ...

    @property
    def StaticPopOutImageTextFormatString(self) -> str:
        """
        Get: StaticPopOutImageTextFormatString(self: Menu) -> str
        Set: StaticPopOutImageTextFormatString(self: Menu) = value
        """
        ...

    @property
    def StaticPopOutImageUrl(self) -> str:
        """
        Get: StaticPopOutImageUrl(self: Menu) -> str
        Set: StaticPopOutImageUrl(self: Menu) = value
        """
        ...

    @property
    def StaticSelectedStyle(self): # -> MenuItemStyle
        """ Get: StaticSelectedStyle(self: Menu) -> MenuItemStyle """
        ...

    @property
    def StaticSubMenuIndent(self): # -> Unit
        """
        Get: StaticSubMenuIndent(self: Menu) -> Unit
        Set: StaticSubMenuIndent(self: Menu) = value
        """
        ...

    @property
    def StaticTopSeparatorImageUrl(self) -> str:
        """
        Get: StaticTopSeparatorImageUrl(self: Menu) -> str
        Set: StaticTopSeparatorImageUrl(self: Menu) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: Menu) -> str
        Set: Target(self: Menu) = value
        """
        ...


    def FindItem(self, valuePath:str) -> MenuItem:
        """ FindItem(self: Menu, valuePath: str) -> MenuItem """
        ...

    def OnMenuItemClick(self, *args): #cannot find CLR method
        """ OnMenuItemClick(self: Menu, e: MenuEventArgs) """
        ...

    def OnMenuItemDataBound(self, *args): #cannot find CLR method
        """ OnMenuItemDataBound(self: Menu, e: MenuEventArgs) """
        ...

    def RenderBeginTag(self, writer:HtmlTextWriter): # -> 
        """ RenderBeginTag(self: Menu, writer: HtmlTextWriter) """
        ...

    def RenderEndTag(self, writer:HtmlTextWriter): # -> 
        """ RenderEndTag(self: Menu, writer: HtmlTextWriter) """
        ...

    def SetItemDataBound(self, *args): #cannot find CLR method
        """ SetItemDataBound(self: Menu, node: MenuItem, dataBound: bool) """
        ...

    def SetItemDataItem(self, *args): #cannot find CLR method
        """ SetItemDataItem(self: Menu, node: MenuItem, dataItem: object) """
        ...

    def SetItemDataPath(self, *args): #cannot find CLR method
        """ SetItemDataPath(self: Menu, node: MenuItem, dataPath: str) """
        ...

    MenuItemClick = ...
    MenuItemClickCommandName: str = ...
    MenuItemDataBound = ...


class MenuEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """
    MenuEventArgs(item: MenuItem, commandSource: object, originalArgs: CommandEventArgs)
    MenuEventArgs(item: MenuItem)
    """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: MenuEventArgs) -> object """
        ...

    @property
    def Item(self) -> MenuItem:
        """ Get: Item(self: MenuEventArgs) -> MenuItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MenuEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MenuEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MenuEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MenuEventHandler, sender: object, e: MenuEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MenuEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MenuEventArgs): # -> 
        """ Invoke(self: MenuEventHandler, sender: object, e: MenuEventArgs) """
        ...


class MenuItem(ICloneable, IStateManager): # skipped bases: <type 'object'>
    """
    MenuItem()
    MenuItem(text: str)
    MenuItem(text: str, value: str)
    MenuItem(text: str, value: str, imageUrl: str)
    MenuItem(text: str, value: str, imageUrl: str, navigateUrl: str)
    MenuItem(text: str, value: str, imageUrl: str, navigateUrl: str, target: str)
    """
    @property
    def ChildItems(self): # -> MenuItemCollection
        """ Get: ChildItems(self: MenuItem) -> MenuItemCollection """
        ...

    @property
    def DataBound(self) -> bool:
        """ Get: DataBound(self: MenuItem) -> bool """
        ...

    @property
    def DataItem(self) -> object:
        """ Get: DataItem(self: MenuItem) -> object """
        ...

    @property
    def DataPath(self) -> str:
        """ Get: DataPath(self: MenuItem) -> str """
        ...

    @property
    def Depth(self) -> int:
        """ Get: Depth(self: MenuItem) -> int """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: MenuItem) -> bool
        Set: Enabled(self: MenuItem) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: MenuItem) -> str
        Set: ImageUrl(self: MenuItem) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: MenuItem) -> str
        Set: NavigateUrl(self: MenuItem) = value
        """
        ...

    @property
    def Parent(self) -> MenuItem:
        """ Get: Parent(self: MenuItem) -> MenuItem """
        ...

    @property
    def PopOutImageUrl(self) -> str:
        """
        Get: PopOutImageUrl(self: MenuItem) -> str
        Set: PopOutImageUrl(self: MenuItem) = value
        """
        ...

    @property
    def Selectable(self) -> bool:
        """
        Get: Selectable(self: MenuItem) -> bool
        Set: Selectable(self: MenuItem) = value
        """
        ...

    @property
    def Selected(self) -> bool:
        """
        Get: Selected(self: MenuItem) -> bool
        Set: Selected(self: MenuItem) = value
        """
        ...

    @property
    def SeparatorImageUrl(self) -> str:
        """
        Get: SeparatorImageUrl(self: MenuItem) -> str
        Set: SeparatorImageUrl(self: MenuItem) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: MenuItem) -> str
        Set: Target(self: MenuItem) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: MenuItem) -> str
        Set: Text(self: MenuItem) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: MenuItem) -> str
        Set: ToolTip(self: MenuItem) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: MenuItem) -> str
        Set: Value(self: MenuItem) = value
        """
        ...

    @property
    def ValuePath(self) -> str:
        """ Get: ValuePath(self: MenuItem) -> str """
        ...



class MenuItemBinding(IDataSourceViewSchemaAccessor, ICloneable, IStateManager): # skipped bases: <type 'object'>
    """ MenuItemBinding() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: MenuItemBinding) -> str
        Set: DataMember(self: MenuItemBinding) = value
        """
        ...

    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: MenuItemBinding) -> int
        Set: Depth(self: MenuItemBinding) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: MenuItemBinding) -> bool
        Set: Enabled(self: MenuItemBinding) = value
        """
        ...

    @property
    def EnabledField(self) -> str:
        """
        Get: EnabledField(self: MenuItemBinding) -> str
        Set: EnabledField(self: MenuItemBinding) = value
        """
        ...

    @property
    def FormatString(self) -> str:
        """
        Get: FormatString(self: MenuItemBinding) -> str
        Set: FormatString(self: MenuItemBinding) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: MenuItemBinding) -> str
        Set: ImageUrl(self: MenuItemBinding) = value
        """
        ...

    @property
    def ImageUrlField(self) -> str:
        """
        Get: ImageUrlField(self: MenuItemBinding) -> str
        Set: ImageUrlField(self: MenuItemBinding) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: MenuItemBinding) -> str
        Set: NavigateUrl(self: MenuItemBinding) = value
        """
        ...

    @property
    def NavigateUrlField(self) -> str:
        """
        Get: NavigateUrlField(self: MenuItemBinding) -> str
        Set: NavigateUrlField(self: MenuItemBinding) = value
        """
        ...

    @property
    def PopOutImageUrl(self) -> str:
        """
        Get: PopOutImageUrl(self: MenuItemBinding) -> str
        Set: PopOutImageUrl(self: MenuItemBinding) = value
        """
        ...

    @property
    def PopOutImageUrlField(self) -> str:
        """
        Get: PopOutImageUrlField(self: MenuItemBinding) -> str
        Set: PopOutImageUrlField(self: MenuItemBinding) = value
        """
        ...

    @property
    def Selectable(self) -> bool:
        """
        Get: Selectable(self: MenuItemBinding) -> bool
        Set: Selectable(self: MenuItemBinding) = value
        """
        ...

    @property
    def SelectableField(self) -> str:
        """
        Get: SelectableField(self: MenuItemBinding) -> str
        Set: SelectableField(self: MenuItemBinding) = value
        """
        ...

    @property
    def SeparatorImageUrl(self) -> str:
        """
        Get: SeparatorImageUrl(self: MenuItemBinding) -> str
        Set: SeparatorImageUrl(self: MenuItemBinding) = value
        """
        ...

    @property
    def SeparatorImageUrlField(self) -> str:
        """
        Get: SeparatorImageUrlField(self: MenuItemBinding) -> str
        Set: SeparatorImageUrlField(self: MenuItemBinding) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: MenuItemBinding) -> str
        Set: Target(self: MenuItemBinding) = value
        """
        ...

    @property
    def TargetField(self) -> str:
        """
        Get: TargetField(self: MenuItemBinding) -> str
        Set: TargetField(self: MenuItemBinding) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: MenuItemBinding) -> str
        Set: Text(self: MenuItemBinding) = value
        """
        ...

    @property
    def TextField(self) -> str:
        """
        Get: TextField(self: MenuItemBinding) -> str
        Set: TextField(self: MenuItemBinding) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: MenuItemBinding) -> str
        Set: ToolTip(self: MenuItemBinding) = value
        """
        ...

    @property
    def ToolTipField(self) -> str:
        """
        Get: ToolTipField(self: MenuItemBinding) -> str
        Set: ToolTipField(self: MenuItemBinding) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: MenuItemBinding) -> str
        Set: Value(self: MenuItemBinding) = value
        """
        ...

    @property
    def ValueField(self) -> str:
        """
        Get: ValueField(self: MenuItemBinding) -> str
        Set: ValueField(self: MenuItemBinding) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: MenuItemBinding) -> str """
        ...


class MenuItemBindingCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, binding:MenuItemBinding) -> int:
        """ Add(self: MenuItemBindingCollection, binding: MenuItemBinding) -> int """
        ...

    def Contains(self, binding:MenuItemBinding) -> bool:
        """ Contains(self: MenuItemBindingCollection, binding: MenuItemBinding) -> bool """
        ...

    def IndexOf(self, value:MenuItemBinding) -> int:
        """ IndexOf(self: MenuItemBindingCollection, value: MenuItemBinding) -> int """
        ...

    def Insert(self, index:int, binding:MenuItemBinding): # -> 
        """ Insert(self: MenuItemBindingCollection, index: int, binding: MenuItemBinding) """
        ...

    def Remove(self, binding:MenuItemBinding): # -> 
        """ Remove(self: MenuItemBindingCollection, binding: MenuItemBinding) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: MenuItemBindingCollection, index: int) """
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


class MenuItemCollection(IStateManager, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    MenuItemCollection()
    MenuItemCollection(owner: MenuItem)
    """
    def Add(self, child:MenuItem): # -> 
        """ Add(self: MenuItemCollection, child: MenuItem) """
        ...

    def AddAt(self, index:int, child:MenuItem): # -> 
        """ AddAt(self: MenuItemCollection, index: int, child: MenuItem) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MenuItemCollection) """
        ...

    def Contains(self, c:MenuItem) -> bool:
        """ Contains(self: MenuItemCollection, c: MenuItem) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MenuItemCollection) -> IEnumerator """
        ...

    def IndexOf(self, value:MenuItem) -> int:
        """ IndexOf(self: MenuItemCollection, value: MenuItem) -> int """
        ...

    def Remove(self, value:MenuItem): # -> 
        """ Remove(self: MenuItemCollection, value: MenuItem) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: MenuItemCollection, index: int) """
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


class MenuItemStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    MenuItemStyle()
    MenuItemStyle(bag: StateBag)
    """
    @property
    def HorizontalPadding(self): # -> Unit
        """
        Get: HorizontalPadding(self: MenuItemStyle) -> Unit
        Set: HorizontalPadding(self: MenuItemStyle) = value
        """
        ...

    @property
    def ItemSpacing(self): # -> Unit
        """
        Get: ItemSpacing(self: MenuItemStyle) -> Unit
        Set: ItemSpacing(self: MenuItemStyle) = value
        """
        ...

    @property
    def VerticalPadding(self): # -> Unit
        """
        Get: VerticalPadding(self: MenuItemStyle) -> Unit
        Set: VerticalPadding(self: MenuItemStyle) = value
        """
        ...



class MenuItemStyleCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, style:MenuItemStyle) -> int:
        """ Add(self: MenuItemStyleCollection, style: MenuItemStyle) -> int """
        ...

    def Contains(self, style:MenuItemStyle) -> bool:
        """ Contains(self: MenuItemStyleCollection, style: MenuItemStyle) -> bool """
        ...

    def IndexOf(self, style:MenuItemStyle) -> int:
        """ IndexOf(self: MenuItemStyleCollection, style: MenuItemStyle) -> int """
        ...

    def Insert(self, index:int, style:MenuItemStyle): # -> 
        """ Insert(self: MenuItemStyleCollection, index: int, style: MenuItemStyle) """
        ...

    def Remove(self, style:MenuItemStyle): # -> 
        """ Remove(self: MenuItemStyleCollection, style: MenuItemStyle) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: MenuItemStyleCollection, index: int) """
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


class MenuItemTemplateContainer(Control, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ MenuItemTemplateContainer(itemIndex: int, dataItem: MenuItem) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: MenuItemTemplateContainer) -> int """
        ...


    def __new__(cls, itemIndex:int, dataItem:MenuItem) -> Self:
        """ __new__(cls: type, itemIndex: int, dataItem: MenuItem) """
        ...


class MenuRenderingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MenuRenderingMode, values: Default (0), List (2), Table (1) """
    Default: MenuRenderingMode = ...
    List: MenuRenderingMode = ...
    Table: MenuRenderingMode = ...
    value__ = ...


class ModelDataMethodResult: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelDataMethodResult(returnValue: object, outputParameters: OrderedDictionary) """
    @property
    def OutputParameters(self) -> OrderedDictionary:
        """ Get: OutputParameters(self: ModelDataMethodResult) -> OrderedDictionary """
        ...

    @property
    def ReturnValue(self) -> object:
        """ Get: ReturnValue(self: ModelDataMethodResult) -> object """
        ...



class ModelDataSource(IDataSource, IStateManager): # skipped bases: <type 'object'>
    """ ModelDataSource(dataControl: Control) """
    @property
    def DataControl(self) -> Control:
        """ Get: DataControl(self: ModelDataSource) -> Control """
        ...

    @property
    def View(self): # -> ModelDataSourceView
        """ Get: View(self: ModelDataSource) -> ModelDataSourceView """
        ...


    def IsTrackingViewState(self, *args): #cannot find CLR method
        """ IsTrackingViewState(self: ModelDataSource) -> bool """
        ...

    def UpdateProperties(self, modelTypeName:str, selectMethod:str, updateMethod:str = ..., insertMethod:str = ..., deleteMethod:str = ..., dataKeyName:str = ...): # -> 
        """ UpdateProperties(self: ModelDataSource, modelTypeName: str, selectMethod: str)UpdateProperties(self: ModelDataSource, modelTypeName: str, selectMethod: str, updateMethod: str, insertMethod: str, deleteMethod: str, dataKeyName: str) """
        ...

    CallingDataMethods = ...


class ModelDataSourceMethod: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelDataSourceMethod(instance: object, methodInfo: MethodInfo) """
    @property
    def Instance(self) -> object:
        """ Get: Instance(self: ModelDataSourceMethod) -> object """
        ...

    @property
    def MethodInfo(self) -> MethodInfo:
        """ Get: MethodInfo(self: ModelDataSourceMethod) -> MethodInfo """
        ...

    @property
    def Parameters(self) -> OrderedDictionary:
        """ Get: Parameters(self: ModelDataSourceMethod) -> OrderedDictionary """
        ...



class ModelDataSourceView(DataSourceView, IStateManager): # skipped bases: <type 'object'>
    """ ModelDataSourceView(owner: ModelDataSource) """
    @property
    def DataKeyName(self) -> str:
        """ Get: DataKeyName(self: ModelDataSourceView) -> str """
        ...

    @property
    def DeleteMethod(self) -> str:
        """ Get: DeleteMethod(self: ModelDataSourceView) -> str """
        ...

    @property
    def InsertMethod(self) -> str:
        """ Get: InsertMethod(self: ModelDataSourceView) -> str """
        ...

    @property
    def ModelTypeName(self) -> str:
        """ Get: ModelTypeName(self: ModelDataSourceView) -> str """
        ...

    @property
    def SelectMethod(self) -> str:
        """ Get: SelectMethod(self: ModelDataSourceView) -> str """
        ...

    @property
    def UpdateMethod(self) -> str:
        """ Get: UpdateMethod(self: ModelDataSourceView) -> str """
        ...


    def CreateSelectResult(self, *args): #cannot find CLR method
        """ CreateSelectResult(self: ModelDataSourceView, result: object) -> IEnumerable """
        ...

    def EvaluateDeleteMethodParameters(self, *args): #cannot find CLR method
        """ EvaluateDeleteMethodParameters(self: ModelDataSourceView, keys: IDictionary, oldValues: IDictionary) -> ModelDataSourceMethod """
        ...

    def EvaluateInsertMethodParameters(self, *args): #cannot find CLR method
        """ EvaluateInsertMethodParameters(self: ModelDataSourceView, values: IDictionary) -> ModelDataSourceMethod """
        ...

    def EvaluateMethodParameters(self, *args): #cannot find CLR method
        """ EvaluateMethodParameters(self: ModelDataSourceView, dataSourceOperation: DataSourceOperation, modelDataSourceMethod: ModelDataSourceMethod, controlValues: IDictionary)EvaluateMethodParameters(self: ModelDataSourceView, dataSourceOperation: DataSourceOperation, modelDataSourceMethod: ModelDataSourceMethod, controlValues: IDictionary, isPageLoadComplete: bool) """
        ...

    def EvaluateSelectMethodParameters(self, *args): #cannot find CLR method
        """ EvaluateSelectMethodParameters(self: ModelDataSourceView, arguments: DataSourceSelectArguments) -> (ModelDataSourceMethod, DataSourceSelectResultProcessingOptions) """
        ...

    def EvaluateUpdateMethodParameters(self, *args): #cannot find CLR method
        """ EvaluateUpdateMethodParameters(self: ModelDataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary) -> ModelDataSourceMethod """
        ...

    def FindMethod(self, *args): #cannot find CLR method
        """ FindMethod(self: ModelDataSourceView, methodName: str) -> ModelDataSourceMethod """
        ...

    def GetDeleteMethodResult(self, *args): #cannot find CLR method
        """ GetDeleteMethodResult(self: ModelDataSourceView, keys: IDictionary, oldValues: IDictionary) -> object """
        ...

    def GetInsertMethodResult(self, *args): #cannot find CLR method
        """ GetInsertMethodResult(self: ModelDataSourceView, values: IDictionary) -> object """
        ...

    def GetSelectMethodResult(self, *args): #cannot find CLR method
        """ GetSelectMethodResult(self: ModelDataSourceView, arguments: DataSourceSelectArguments) -> object """
        ...

    def GetUpdateMethodResult(self, *args): #cannot find CLR method
        """ GetUpdateMethodResult(self: ModelDataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary) -> object """
        ...

    def InvokeMethod(self, *args): #cannot find CLR method
        """ InvokeMethod(self: ModelDataSourceView, method: ModelDataSourceMethod) -> ModelDataMethodResult """
        ...

    def IsTrackingViewState(self, *args): #cannot find CLR method
        """ IsTrackingViewState(self: ModelDataSourceView) -> bool """
        ...

    def OnCallingDataMethods(self, *args): #cannot find CLR method
        """ OnCallingDataMethods(self: ModelDataSourceView, e: CallingDataMethodsEventArgs) """
        ...

    def ProcessSelectMethodResult(self, *args): #cannot find CLR method
        """ ProcessSelectMethodResult(self: ModelDataSourceView, arguments: DataSourceSelectArguments, selectResultProcessingOptions: DataSourceSelectResultProcessingOptions, result: ModelDataMethodResult) -> object """
        ...

    def UpdateProperties(self, modelTypeName:str, selectMethod:str, updateMethod:str, insertMethod:str, deleteMethod:str, dataKeyName:str): # -> 
        """ UpdateProperties(self: ModelDataSourceView, modelTypeName: str, selectMethod: str, updateMethod: str, insertMethod: str, deleteMethod: str, dataKeyName: str) """
        ...

    CallingDataMethods = ...


class ModelErrorMessage(Label): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'object'>
    """ ModelErrorMessage() """
    @property
    def ModelStateKey(self) -> str:
        """
        Get: ModelStateKey(self: ModelErrorMessage) -> str
        Set: ModelStateKey(self: ModelErrorMessage) = value
        """
        ...

    @property
    def SetFocusOnError(self) -> bool:
        """
        Get: SetFocusOnError(self: ModelErrorMessage) -> bool
        Set: SetFocusOnError(self: ModelErrorMessage) = value
        """
        ...



class ModelMethodContext: # skipped bases: <type 'object'>, <type 'object'>
    """ ModelMethodContext(page: Page) """
    @property
    def Current(self) -> ModelMethodContext:
        """ Get: Current() -> ModelMethodContext """
        ...

    @property
    def ModelState(self) -> ModelStateDictionary:
        """ Get: ModelState(self: ModelMethodContext) -> ModelStateDictionary """
        ...


    def TryUpdateModel(self, model, valueProvider:IValueProvider = ...) -> bool: # Not found arg types: {'model': 'TModel'}
        """
        TryUpdateModel[TModel](self: ModelMethodContext, model: TModel) -> bool
        TryUpdateModel[TModel](self: ModelMethodContext, model: TModel, valueProvider: IValueProvider) -> bool
        """
        ...

    def UpdateModel(self, model, valueProvider:IValueProvider = ...): # ->  # Not found arg types: {'model': 'TModel'}
        """ UpdateModel[TModel](self: ModelMethodContext, model: TModel)UpdateModel[TModel](self: ModelMethodContext, model: TModel, valueProvider: IValueProvider) """
        ...


class MonthChangedEventArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ MonthChangedEventArgs(newDate: DateTime, previousDate: DateTime) """
    @property
    def NewDate(self) -> DateTime:
        """ Get: NewDate(self: MonthChangedEventArgs) -> DateTime """
        ...

    @property
    def PreviousDate(self) -> DateTime:
        """ Get: PreviousDate(self: MonthChangedEventArgs) -> DateTime """
        ...



class MonthChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MonthChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MonthChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MonthChangedEventHandler, sender: object, e: MonthChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MonthChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MonthChangedEventArgs): # -> 
        """ Invoke(self: MonthChangedEventHandler, sender: object, e: MonthChangedEventArgs) """
        ...


class MultiView(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ MultiView() """
    @property
    def ActiveViewIndex(self) -> int:
        """
        Get: ActiveViewIndex(self: MultiView) -> int
        Set: ActiveViewIndex(self: MultiView) = value
        """
        ...

    @property
    def Views(self) -> ViewCollection:
        """ Get: Views(self: MultiView) -> ViewCollection """
        ...


    def GetActiveView(self) -> View:
        """ GetActiveView(self: MultiView) -> View """
        ...

    def OnActiveViewChanged(self, *args): #cannot find CLR method
        """ OnActiveViewChanged(self: MultiView, e: EventArgs) """
        ...

    def SetActiveView(self, view:View): # -> 
        """ SetActiveView(self: MultiView, view: View) """
        ...

    ActiveViewChanged = ...
    NextViewCommandName: str = ...
    PreviousViewCommandName: str = ...
    SwitchViewByIDCommandName: str = ...
    SwitchViewByIndexCommandName: str = ...


class MultiViewControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ MultiViewControlBuilder() """
    pass

class NextPrevFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NextPrevFormat, values: CustomText (0), FullMonth (2), ShortMonth (1) """
    CustomText: NextPrevFormat = ...
    FullMonth: NextPrevFormat = ...
    ShortMonth: NextPrevFormat = ...
    value__ = ...


class NextPreviousPagerField(DataPagerField): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ NextPreviousPagerField() """
    @property
    def ButtonCssClass(self) -> str:
        """
        Get: ButtonCssClass(self: NextPreviousPagerField) -> str
        Set: ButtonCssClass(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def ButtonType(self) -> ButtonType:
        """
        Get: ButtonType(self: NextPreviousPagerField) -> ButtonType
        Set: ButtonType(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def FirstPageImageUrl(self) -> str:
        """
        Get: FirstPageImageUrl(self: NextPreviousPagerField) -> str
        Set: FirstPageImageUrl(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def FirstPageText(self) -> str:
        """
        Get: FirstPageText(self: NextPreviousPagerField) -> str
        Set: FirstPageText(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def LastPageImageUrl(self) -> str:
        """
        Get: LastPageImageUrl(self: NextPreviousPagerField) -> str
        Set: LastPageImageUrl(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def LastPageText(self) -> str:
        """
        Get: LastPageText(self: NextPreviousPagerField) -> str
        Set: LastPageText(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def NextPageImageUrl(self) -> str:
        """
        Get: NextPageImageUrl(self: NextPreviousPagerField) -> str
        Set: NextPageImageUrl(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def NextPageText(self) -> str:
        """
        Get: NextPageText(self: NextPreviousPagerField) -> str
        Set: NextPageText(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def PreviousPageImageUrl(self) -> str:
        """
        Get: PreviousPageImageUrl(self: NextPreviousPagerField) -> str
        Set: PreviousPageImageUrl(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def PreviousPageText(self) -> str:
        """
        Get: PreviousPageText(self: NextPreviousPagerField) -> str
        Set: PreviousPageText(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def RenderDisabledButtonsAsLabels(self) -> bool:
        """
        Get: RenderDisabledButtonsAsLabels(self: NextPreviousPagerField) -> bool
        Set: RenderDisabledButtonsAsLabels(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def RenderNonBreakingSpacesBetweenControls(self) -> bool:
        """
        Get: RenderNonBreakingSpacesBetweenControls(self: NextPreviousPagerField) -> bool
        Set: RenderNonBreakingSpacesBetweenControls(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def ShowFirstPageButton(self) -> bool:
        """
        Get: ShowFirstPageButton(self: NextPreviousPagerField) -> bool
        Set: ShowFirstPageButton(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def ShowLastPageButton(self) -> bool:
        """
        Get: ShowLastPageButton(self: NextPreviousPagerField) -> bool
        Set: ShowLastPageButton(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def ShowNextPageButton(self) -> bool:
        """
        Get: ShowNextPageButton(self: NextPreviousPagerField) -> bool
        Set: ShowNextPageButton(self: NextPreviousPagerField) = value
        """
        ...

    @property
    def ShowPreviousPageButton(self) -> bool:
        """
        Get: ShowPreviousPageButton(self: NextPreviousPagerField) -> bool
        Set: ShowPreviousPageButton(self: NextPreviousPagerField) = value
        """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: NextPreviousPagerField, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: NextPreviousPagerField) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NumericPagerField(DataPagerField): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ NumericPagerField() """
    @property
    def ButtonCount(self) -> int:
        """
        Get: ButtonCount(self: NumericPagerField) -> int
        Set: ButtonCount(self: NumericPagerField) = value
        """
        ...

    @property
    def ButtonType(self) -> ButtonType:
        """
        Get: ButtonType(self: NumericPagerField) -> ButtonType
        Set: ButtonType(self: NumericPagerField) = value
        """
        ...

    @property
    def CurrentPageLabelCssClass(self) -> str:
        """
        Get: CurrentPageLabelCssClass(self: NumericPagerField) -> str
        Set: CurrentPageLabelCssClass(self: NumericPagerField) = value
        """
        ...

    @property
    def NextPageImageUrl(self) -> str:
        """
        Get: NextPageImageUrl(self: NumericPagerField) -> str
        Set: NextPageImageUrl(self: NumericPagerField) = value
        """
        ...

    @property
    def NextPageText(self) -> str:
        """
        Get: NextPageText(self: NumericPagerField) -> str
        Set: NextPageText(self: NumericPagerField) = value
        """
        ...

    @property
    def NextPreviousButtonCssClass(self) -> str:
        """
        Get: NextPreviousButtonCssClass(self: NumericPagerField) -> str
        Set: NextPreviousButtonCssClass(self: NumericPagerField) = value
        """
        ...

    @property
    def NumericButtonCssClass(self) -> str:
        """
        Get: NumericButtonCssClass(self: NumericPagerField) -> str
        Set: NumericButtonCssClass(self: NumericPagerField) = value
        """
        ...

    @property
    def PreviousPageImageUrl(self) -> str:
        """
        Get: PreviousPageImageUrl(self: NumericPagerField) -> str
        Set: PreviousPageImageUrl(self: NumericPagerField) = value
        """
        ...

    @property
    def PreviousPageText(self) -> str:
        """
        Get: PreviousPageText(self: NumericPagerField) -> str
        Set: PreviousPageText(self: NumericPagerField) = value
        """
        ...

    @property
    def RenderNonBreakingSpacesBetweenControls(self) -> bool:
        """
        Get: RenderNonBreakingSpacesBetweenControls(self: NumericPagerField) -> bool
        Set: RenderNonBreakingSpacesBetweenControls(self: NumericPagerField) = value
        """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: NumericPagerField, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: NumericPagerField) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ObjectDataSource(DataSourceControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IDataSource'>, <type 'IListSource'>, <type 'object'>
    """
    ObjectDataSource()
    ObjectDataSource(typeName: str, selectMethod: str)
    """
    @property
    def CacheDuration(self) -> int:
        """
        Get: CacheDuration(self: ObjectDataSource) -> int
        Set: CacheDuration(self: ObjectDataSource) = value
        """
        ...

    @property
    def CacheExpirationPolicy(self) -> DataSourceCacheExpiry:
        """
        Get: CacheExpirationPolicy(self: ObjectDataSource) -> DataSourceCacheExpiry
        Set: CacheExpirationPolicy(self: ObjectDataSource) = value
        """
        ...

    @property
    def CacheKeyDependency(self) -> str:
        """
        Get: CacheKeyDependency(self: ObjectDataSource) -> str
        Set: CacheKeyDependency(self: ObjectDataSource) = value
        """
        ...

    @property
    def ConflictDetection(self) -> ConflictOptions:
        """
        Get: ConflictDetection(self: ObjectDataSource) -> ConflictOptions
        Set: ConflictDetection(self: ObjectDataSource) = value
        """
        ...

    @property
    def ConvertNullToDBNull(self) -> bool:
        """
        Get: ConvertNullToDBNull(self: ObjectDataSource) -> bool
        Set: ConvertNullToDBNull(self: ObjectDataSource) = value
        """
        ...

    @property
    def DataObjectTypeName(self) -> str:
        """
        Get: DataObjectTypeName(self: ObjectDataSource) -> str
        Set: DataObjectTypeName(self: ObjectDataSource) = value
        """
        ...

    @property
    def DeleteMethod(self) -> str:
        """
        Get: DeleteMethod(self: ObjectDataSource) -> str
        Set: DeleteMethod(self: ObjectDataSource) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: ObjectDataSource) -> ParameterCollection """
        ...

    @property
    def EnableCaching(self) -> bool:
        """
        Get: EnableCaching(self: ObjectDataSource) -> bool
        Set: EnableCaching(self: ObjectDataSource) = value
        """
        ...

    @property
    def EnablePaging(self) -> bool:
        """
        Get: EnablePaging(self: ObjectDataSource) -> bool
        Set: EnablePaging(self: ObjectDataSource) = value
        """
        ...

    @property
    def FilterExpression(self) -> str:
        """
        Get: FilterExpression(self: ObjectDataSource) -> str
        Set: FilterExpression(self: ObjectDataSource) = value
        """
        ...

    @property
    def FilterParameters(self) -> ParameterCollection:
        """ Get: FilterParameters(self: ObjectDataSource) -> ParameterCollection """
        ...

    @property
    def InsertMethod(self) -> str:
        """
        Get: InsertMethod(self: ObjectDataSource) -> str
        Set: InsertMethod(self: ObjectDataSource) = value
        """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: ObjectDataSource) -> ParameterCollection """
        ...

    @property
    def MaximumRowsParameterName(self) -> str:
        """
        Get: MaximumRowsParameterName(self: ObjectDataSource) -> str
        Set: MaximumRowsParameterName(self: ObjectDataSource) = value
        """
        ...

    @property
    def OldValuesParameterFormatString(self) -> str:
        """
        Get: OldValuesParameterFormatString(self: ObjectDataSource) -> str
        Set: OldValuesParameterFormatString(self: ObjectDataSource) = value
        """
        ...

    @property
    def ParsingCulture(self): # -> ParsingCulture
        """
        Get: ParsingCulture(self: ObjectDataSource) -> ParsingCulture
        Set: ParsingCulture(self: ObjectDataSource) = value
        """
        ...

    @property
    def SelectCountMethod(self) -> str:
        """
        Get: SelectCountMethod(self: ObjectDataSource) -> str
        Set: SelectCountMethod(self: ObjectDataSource) = value
        """
        ...

    @property
    def SelectMethod(self) -> str:
        """
        Get: SelectMethod(self: ObjectDataSource) -> str
        Set: SelectMethod(self: ObjectDataSource) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: ObjectDataSource) -> ParameterCollection """
        ...

    @property
    def SortParameterName(self) -> str:
        """
        Get: SortParameterName(self: ObjectDataSource) -> str
        Set: SortParameterName(self: ObjectDataSource) = value
        """
        ...

    @property
    def SqlCacheDependency(self) -> str:
        """
        Get: SqlCacheDependency(self: ObjectDataSource) -> str
        Set: SqlCacheDependency(self: ObjectDataSource) = value
        """
        ...

    @property
    def StartRowIndexParameterName(self) -> str:
        """
        Get: StartRowIndexParameterName(self: ObjectDataSource) -> str
        Set: StartRowIndexParameterName(self: ObjectDataSource) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ObjectDataSource) -> str
        Set: TypeName(self: ObjectDataSource) = value
        """
        ...

    @property
    def UpdateMethod(self) -> str:
        """
        Get: UpdateMethod(self: ObjectDataSource) -> str
        Set: UpdateMethod(self: ObjectDataSource) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: ObjectDataSource) -> ParameterCollection """
        ...


    def Delete(self) -> int:
        """ Delete(self: ObjectDataSource) -> int """
        ...

    def Insert(self) -> int:
        """ Insert(self: ObjectDataSource) -> int """
        ...

    def Select(self) -> IEnumerable:
        """ Select(self: ObjectDataSource) -> IEnumerable """
        ...

    def Update(self) -> int:
        """ Update(self: ObjectDataSource) -> int """
        ...

    def __new__(cls, typeName:str = ..., selectMethod:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str, selectMethod: str)
        """
        ...

    Deleted = ...
    Deleting = ...
    Filtering = ...
    Inserted = ...
    Inserting = ...
    ObjectCreated = ...
    ObjectCreating = ...
    ObjectDisposing = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class ObjectDataSourceDisposingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ObjectDataSourceDisposingEventArgs(objectInstance: object) """
    @property
    def ObjectInstance(self) -> object:
        """ Get: ObjectInstance(self: ObjectDataSourceDisposingEventArgs) -> object """
        ...



class ObjectDataSourceDisposingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceDisposingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceDisposingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceDisposingEventHandler, sender: object, e: ObjectDataSourceDisposingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceDisposingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceDisposingEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceDisposingEventHandler, sender: object, e: ObjectDataSourceDisposingEventArgs) """
        ...


class ObjectDataSourceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ObjectDataSourceEventArgs(objectInstance: object) """
    @property
    def ObjectInstance(self) -> object:
        """
        Get: ObjectInstance(self: ObjectDataSourceEventArgs) -> object
        Set: ObjectInstance(self: ObjectDataSourceEventArgs) = value
        """
        ...


    def __new__(cls, objectInstance:object) -> Self:
        """ __new__(cls: type, objectInstance: object) """
        ...


class ObjectDataSourceFilteringEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ObjectDataSourceFilteringEventArgs(parameterValues: IOrderedDictionary) """
    @property
    def ParameterValues(self) -> IOrderedDictionary:
        """ Get: ParameterValues(self: ObjectDataSourceFilteringEventArgs) -> IOrderedDictionary """
        ...



class ObjectDataSourceFilteringEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceFilteringEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceFilteringEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceFilteringEventHandler, sender: object, e: ObjectDataSourceFilteringEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceFilteringEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceFilteringEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceFilteringEventHandler, sender: object, e: ObjectDataSourceFilteringEventArgs) """
        ...


class ObjectDataSourceMethodEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ ObjectDataSourceMethodEventArgs(inputParameters: IOrderedDictionary) """
    @property
    def InputParameters(self) -> IOrderedDictionary:
        """ Get: InputParameters(self: ObjectDataSourceMethodEventArgs) -> IOrderedDictionary """
        ...



class ObjectDataSourceMethodEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceMethodEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceMethodEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceMethodEventHandler, sender: object, e: ObjectDataSourceMethodEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceMethodEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceMethodEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceMethodEventHandler, sender: object, e: ObjectDataSourceMethodEventArgs) """
        ...


class ObjectDataSourceObjectEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceObjectEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceObjectEventHandler, sender: object, e: ObjectDataSourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceObjectEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceObjectEventHandler, sender: object, e: ObjectDataSourceEventArgs) """
        ...


class ObjectDataSourceSelectingEventArgs(ObjectDataSourceMethodEventArgs): # skipped bases: <type 'object'>
    """ ObjectDataSourceSelectingEventArgs(inputParameters: IOrderedDictionary, arguments: DataSourceSelectArguments, executingSelectCount: bool) """
    @property
    def Arguments(self) -> DataSourceSelectArguments:
        """ Get: Arguments(self: ObjectDataSourceSelectingEventArgs) -> DataSourceSelectArguments """
        ...

    @property
    def ExecutingSelectCount(self) -> bool:
        """ Get: ExecutingSelectCount(self: ObjectDataSourceSelectingEventArgs) -> bool """
        ...



class ObjectDataSourceSelectingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceSelectingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceSelectingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceSelectingEventHandler, sender: object, e: ObjectDataSourceSelectingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceSelectingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceSelectingEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceSelectingEventHandler, sender: object, e: ObjectDataSourceSelectingEventArgs) """
        ...


class ObjectDataSourceStatusEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ObjectDataSourceStatusEventArgs(returnValue: object, outputParameters: IDictionary)
    ObjectDataSourceStatusEventArgs(returnValue: object, outputParameters: IDictionary, exception: Exception)
    """
    @property
    def AffectedRows(self) -> int:
        """
        Get: AffectedRows(self: ObjectDataSourceStatusEventArgs) -> int
        Set: AffectedRows(self: ObjectDataSourceStatusEventArgs) = value
        """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ObjectDataSourceStatusEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: ObjectDataSourceStatusEventArgs) -> bool
        Set: ExceptionHandled(self: ObjectDataSourceStatusEventArgs) = value
        """
        ...

    @property
    def OutputParameters(self) -> IDictionary:
        """ Get: OutputParameters(self: ObjectDataSourceStatusEventArgs) -> IDictionary """
        ...

    @property
    def ReturnValue(self) -> object:
        """ Get: ReturnValue(self: ObjectDataSourceStatusEventArgs) -> object """
        ...


    def __new__(cls, returnValue:object, outputParameters:IDictionary, exception:Exception = ...) -> Self:
        """
        __new__(cls: type, returnValue: object, outputParameters: IDictionary)
        __new__(cls: type, returnValue: object, outputParameters: IDictionary, exception: Exception)
        """
        ...


class ObjectDataSourceStatusEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectDataSourceStatusEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectDataSourceStatusEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectDataSourceStatusEventHandler, sender: object, e: ObjectDataSourceStatusEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectDataSourceStatusEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectDataSourceStatusEventArgs): # -> 
        """ Invoke(self: ObjectDataSourceStatusEventHandler, sender: object, e: ObjectDataSourceStatusEventArgs) """
        ...


class ObjectDataSourceView(DataSourceView, IStateManager): # skipped bases: <type 'object'>
    """ ObjectDataSourceView(owner: ObjectDataSource, name: str, context: HttpContext) """
    @property
    def ConflictDetection(self) -> ConflictOptions:
        """
        Get: ConflictDetection(self: ObjectDataSourceView) -> ConflictOptions
        Set: ConflictDetection(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def ConvertNullToDBNull(self) -> bool:
        """
        Get: ConvertNullToDBNull(self: ObjectDataSourceView) -> bool
        Set: ConvertNullToDBNull(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def DataObjectTypeName(self) -> str:
        """
        Get: DataObjectTypeName(self: ObjectDataSourceView) -> str
        Set: DataObjectTypeName(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def DeleteMethod(self) -> str:
        """
        Get: DeleteMethod(self: ObjectDataSourceView) -> str
        Set: DeleteMethod(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def DeleteParameters(self) -> ParameterCollection:
        """ Get: DeleteParameters(self: ObjectDataSourceView) -> ParameterCollection """
        ...

    @property
    def EnablePaging(self) -> bool:
        """
        Get: EnablePaging(self: ObjectDataSourceView) -> bool
        Set: EnablePaging(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def FilterExpression(self) -> str:
        """
        Get: FilterExpression(self: ObjectDataSourceView) -> str
        Set: FilterExpression(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def FilterParameters(self) -> ParameterCollection:
        """ Get: FilterParameters(self: ObjectDataSourceView) -> ParameterCollection """
        ...

    @property
    def InsertMethod(self) -> str:
        """
        Get: InsertMethod(self: ObjectDataSourceView) -> str
        Set: InsertMethod(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def InsertParameters(self) -> ParameterCollection:
        """ Get: InsertParameters(self: ObjectDataSourceView) -> ParameterCollection """
        ...

    @property
    def MaximumRowsParameterName(self) -> str:
        """
        Get: MaximumRowsParameterName(self: ObjectDataSourceView) -> str
        Set: MaximumRowsParameterName(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def OldValuesParameterFormatString(self) -> str:
        """
        Get: OldValuesParameterFormatString(self: ObjectDataSourceView) -> str
        Set: OldValuesParameterFormatString(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def ParsingCulture(self): # -> ParsingCulture
        """
        Get: ParsingCulture(self: ObjectDataSourceView) -> ParsingCulture
        Set: ParsingCulture(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def SelectCountMethod(self) -> str:
        """
        Get: SelectCountMethod(self: ObjectDataSourceView) -> str
        Set: SelectCountMethod(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def SelectMethod(self) -> str:
        """
        Get: SelectMethod(self: ObjectDataSourceView) -> str
        Set: SelectMethod(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def SelectParameters(self) -> ParameterCollection:
        """ Get: SelectParameters(self: ObjectDataSourceView) -> ParameterCollection """
        ...

    @property
    def SortParameterName(self) -> str:
        """
        Get: SortParameterName(self: ObjectDataSourceView) -> str
        Set: SortParameterName(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def StartRowIndexParameterName(self) -> str:
        """
        Get: StartRowIndexParameterName(self: ObjectDataSourceView) -> str
        Set: StartRowIndexParameterName(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ObjectDataSourceView) -> str
        Set: TypeName(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def UpdateMethod(self) -> str:
        """
        Get: UpdateMethod(self: ObjectDataSourceView) -> str
        Set: UpdateMethod(self: ObjectDataSourceView) = value
        """
        ...

    @property
    def UpdateParameters(self) -> ParameterCollection:
        """ Get: UpdateParameters(self: ObjectDataSourceView) -> ParameterCollection """
        ...


    def OnDeleted(self, *args): #cannot find CLR method
        """ OnDeleted(self: ObjectDataSourceView, e: ObjectDataSourceStatusEventArgs) """
        ...

    def OnDeleting(self, *args): #cannot find CLR method
        """ OnDeleting(self: ObjectDataSourceView, e: ObjectDataSourceMethodEventArgs) """
        ...

    def OnFiltering(self, *args): #cannot find CLR method
        """ OnFiltering(self: ObjectDataSourceView, e: ObjectDataSourceFilteringEventArgs) """
        ...

    def OnInserted(self, *args): #cannot find CLR method
        """ OnInserted(self: ObjectDataSourceView, e: ObjectDataSourceStatusEventArgs) """
        ...

    def OnInserting(self, *args): #cannot find CLR method
        """ OnInserting(self: ObjectDataSourceView, e: ObjectDataSourceMethodEventArgs) """
        ...

    def OnObjectCreated(self, *args): #cannot find CLR method
        """ OnObjectCreated(self: ObjectDataSourceView, e: ObjectDataSourceEventArgs) """
        ...

    def OnObjectCreating(self, *args): #cannot find CLR method
        """ OnObjectCreating(self: ObjectDataSourceView, e: ObjectDataSourceEventArgs) """
        ...

    def OnObjectDisposing(self, *args): #cannot find CLR method
        """ OnObjectDisposing(self: ObjectDataSourceView, e: ObjectDataSourceDisposingEventArgs) """
        ...

    def OnSelected(self, *args): #cannot find CLR method
        """ OnSelected(self: ObjectDataSourceView, e: ObjectDataSourceStatusEventArgs) """
        ...

    def OnSelecting(self, *args): #cannot find CLR method
        """ OnSelecting(self: ObjectDataSourceView, e: ObjectDataSourceSelectingEventArgs) """
        ...

    def OnUpdated(self, *args): #cannot find CLR method
        """ OnUpdated(self: ObjectDataSourceView, e: ObjectDataSourceStatusEventArgs) """
        ...

    def OnUpdating(self, *args): #cannot find CLR method
        """ OnUpdating(self: ObjectDataSourceView, e: ObjectDataSourceMethodEventArgs) """
        ...

    Deleted = ...
    Deleting = ...
    Filtering = ...
    Inserted = ...
    Inserting = ...
    ObjectCreated = ...
    ObjectCreating = ...
    ObjectDisposing = ...
    Selected = ...
    Selecting = ...
    Updated = ...
    Updating = ...


class Orientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Orientation, values: Horizontal (0), Vertical (1) """
    Horizontal: Orientation = ...
    value__ = ...
    Vertical: Orientation = ...


class PagedDataSource(ITypedList, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ PagedDataSource() """
    @property
    def AllowCustomPaging(self) -> bool:
        """
        Get: AllowCustomPaging(self: PagedDataSource) -> bool
        Set: AllowCustomPaging(self: PagedDataSource) = value
        """
        ...

    @property
    def AllowPaging(self) -> bool:
        """
        Get: AllowPaging(self: PagedDataSource) -> bool
        Set: AllowPaging(self: PagedDataSource) = value
        """
        ...

    @property
    def AllowServerPaging(self) -> bool:
        """
        Get: AllowServerPaging(self: PagedDataSource) -> bool
        Set: AllowServerPaging(self: PagedDataSource) = value
        """
        ...

    @property
    def CurrentPageIndex(self) -> int:
        """
        Get: CurrentPageIndex(self: PagedDataSource) -> int
        Set: CurrentPageIndex(self: PagedDataSource) = value
        """
        ...

    @property
    def DataSource(self) -> IEnumerable:
        """
        Get: DataSource(self: PagedDataSource) -> IEnumerable
        Set: DataSource(self: PagedDataSource) = value
        """
        ...

    @property
    def DataSourceCount(self) -> int:
        """ Get: DataSourceCount(self: PagedDataSource) -> int """
        ...

    @property
    def FirstIndexInPage(self) -> int:
        """ Get: FirstIndexInPage(self: PagedDataSource) -> int """
        ...

    @property
    def IsCustomPagingEnabled(self) -> bool:
        """ Get: IsCustomPagingEnabled(self: PagedDataSource) -> bool """
        ...

    @property
    def IsFirstPage(self) -> bool:
        """ Get: IsFirstPage(self: PagedDataSource) -> bool """
        ...

    @property
    def IsLastPage(self) -> bool:
        """ Get: IsLastPage(self: PagedDataSource) -> bool """
        ...

    @property
    def IsPagingEnabled(self) -> bool:
        """ Get: IsPagingEnabled(self: PagedDataSource) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: PagedDataSource) -> bool """
        ...

    @property
    def IsServerPagingEnabled(self) -> bool:
        """ Get: IsServerPagingEnabled(self: PagedDataSource) -> bool """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: PagedDataSource) -> int """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: PagedDataSource) -> int
        Set: PageSize(self: PagedDataSource) = value
        """
        ...

    @property
    def VirtualCount(self) -> int:
        """
        Get: VirtualCount(self: PagedDataSource) -> int
        Set: VirtualCount(self: PagedDataSource) = value
        """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PagedDataSource) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class PageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PageEventArgs(startRowIndex: int, maximumRows: int, totalRowCount: int) """
    @property
    def MaximumRows(self) -> int:
        """ Get: MaximumRows(self: PageEventArgs) -> int """
        ...

    @property
    def StartRowIndex(self) -> int:
        """ Get: StartRowIndex(self: PageEventArgs) -> int """
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: PageEventArgs) -> int """
        ...


    def __new__(cls, startRowIndex:int, maximumRows:int, totalRowCount:int) -> Self:
        """ __new__(cls: type, startRowIndex: int, maximumRows: int, totalRowCount: int) """
        ...


class PagePropertiesChangingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PagePropertiesChangingEventArgs(startRowIndex: int, maximumRows: int) """
    @property
    def MaximumRows(self) -> int:
        """ Get: MaximumRows(self: PagePropertiesChangingEventArgs) -> int """
        ...

    @property
    def StartRowIndex(self) -> int:
        """ Get: StartRowIndex(self: PagePropertiesChangingEventArgs) -> int """
        ...


    def __new__(cls, startRowIndex:int, maximumRows:int) -> Self:
        """ __new__(cls: type, startRowIndex: int, maximumRows: int) """
        ...


class PagerButtons(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PagerButtons, values: NextPrevious (0), NextPreviousFirstLast (2), Numeric (1), NumericFirstLast (3) """
    NextPrevious: PagerButtons = ...
    NextPreviousFirstLast: PagerButtons = ...
    Numeric: PagerButtons = ...
    NumericFirstLast: PagerButtons = ...
    value__ = ...


class PagerMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PagerMode, values: NextPrev (0), NumericPages (1) """
    NextPrev: PagerMode = ...
    NumericPages: PagerMode = ...
    value__ = ...


class PagerPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PagerPosition, values: Bottom (0), Top (1), TopAndBottom (2) """
    Bottom: PagerPosition = ...
    Top: PagerPosition = ...
    TopAndBottom: PagerPosition = ...
    value__ = ...


class PagerSettings(IStateManager): # skipped bases: <type 'object'>
    """ PagerSettings() """
    @property
    def FirstPageImageUrl(self) -> str:
        """
        Get: FirstPageImageUrl(self: PagerSettings) -> str
        Set: FirstPageImageUrl(self: PagerSettings) = value
        """
        ...

    @property
    def FirstPageText(self) -> str:
        """
        Get: FirstPageText(self: PagerSettings) -> str
        Set: FirstPageText(self: PagerSettings) = value
        """
        ...

    @property
    def LastPageImageUrl(self) -> str:
        """
        Get: LastPageImageUrl(self: PagerSettings) -> str
        Set: LastPageImageUrl(self: PagerSettings) = value
        """
        ...

    @property
    def LastPageText(self) -> str:
        """
        Get: LastPageText(self: PagerSettings) -> str
        Set: LastPageText(self: PagerSettings) = value
        """
        ...

    @property
    def Mode(self) -> PagerButtons:
        """
        Get: Mode(self: PagerSettings) -> PagerButtons
        Set: Mode(self: PagerSettings) = value
        """
        ...

    @property
    def NextPageImageUrl(self) -> str:
        """
        Get: NextPageImageUrl(self: PagerSettings) -> str
        Set: NextPageImageUrl(self: PagerSettings) = value
        """
        ...

    @property
    def NextPageText(self) -> str:
        """
        Get: NextPageText(self: PagerSettings) -> str
        Set: NextPageText(self: PagerSettings) = value
        """
        ...

    @property
    def PageButtonCount(self) -> int:
        """
        Get: PageButtonCount(self: PagerSettings) -> int
        Set: PageButtonCount(self: PagerSettings) = value
        """
        ...

    @property
    def Position(self) -> PagerPosition:
        """
        Get: Position(self: PagerSettings) -> PagerPosition
        Set: Position(self: PagerSettings) = value
        """
        ...

    @property
    def PreviousPageImageUrl(self) -> str:
        """
        Get: PreviousPageImageUrl(self: PagerSettings) -> str
        Set: PreviousPageImageUrl(self: PagerSettings) = value
        """
        ...

    @property
    def PreviousPageText(self) -> str:
        """
        Get: PreviousPageText(self: PagerSettings) -> str
        Set: PreviousPageText(self: PagerSettings) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: PagerSettings) -> bool
        Set: Visible(self: PagerSettings) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: PagerSettings) -> str """
        ...

    PropertyChanged = ...


class Panel(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Panel() """
    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: Panel) -> str
        Set: BackImageUrl(self: Panel) = value
        """
        ...

    @property
    def DefaultButton(self) -> str:
        """
        Get: DefaultButton(self: Panel) -> str
        Set: DefaultButton(self: Panel) = value
        """
        ...

    @property
    def Direction(self) -> ContentDirection:
        """
        Get: Direction(self: Panel) -> ContentDirection
        Set: Direction(self: Panel) = value
        """
        ...

    @property
    def GroupingText(self) -> str:
        """
        Get: GroupingText(self: Panel) -> str
        Set: GroupingText(self: Panel) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: Panel) -> HorizontalAlign
        Set: HorizontalAlign(self: Panel) = value
        """
        ...

    @property
    def ScrollBars(self) -> ScrollBars:
        """
        Get: ScrollBars(self: Panel) -> ScrollBars
        Set: ScrollBars(self: Panel) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: Panel) -> bool
        Set: Wrap(self: Panel) = value
        """
        ...



class PanelStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """ PanelStyle(bag: StateBag) """
    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: PanelStyle) -> str
        Set: BackImageUrl(self: PanelStyle) = value
        """
        ...

    @property
    def Direction(self) -> ContentDirection:
        """
        Get: Direction(self: PanelStyle) -> ContentDirection
        Set: Direction(self: PanelStyle) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: PanelStyle) -> HorizontalAlign
        Set: HorizontalAlign(self: PanelStyle) = value
        """
        ...

    @property
    def ScrollBars(self) -> ScrollBars:
        """
        Get: ScrollBars(self: PanelStyle) -> ScrollBars
        Set: ScrollBars(self: PanelStyle) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: PanelStyle) -> bool
        Set: Wrap(self: PanelStyle) = value
        """
        ...



class ParameterCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ParameterCollection() """
    def Add(self, *__args:Parameter) -> int:
        """
        Add(self: ParameterCollection, parameter: Parameter) -> int
        Add(self: ParameterCollection, name: str, value: str) -> int
        Add(self: ParameterCollection, name: str, type: TypeCode, value: str) -> int
        Add(self: ParameterCollection, name: str, dbType: DbType, value: str) -> int
        """
        ...

    def Contains(self, parameter:Parameter) -> bool:
        """ Contains(self: ParameterCollection, parameter: Parameter) -> bool """
        ...

    def GetValues(self, context:HttpContext, control:Control) -> IOrderedDictionary:
        """ GetValues(self: ParameterCollection, context: HttpContext, control: Control) -> IOrderedDictionary """
        ...

    def IndexOf(self, parameter:Parameter) -> int:
        """ IndexOf(self: ParameterCollection, parameter: Parameter) -> int """
        ...

    def Insert(self, index:int, parameter:Parameter): # -> 
        """ Insert(self: ParameterCollection, index: int, parameter: Parameter) """
        ...

    def OnParametersChanged(self, *args): #cannot find CLR method
        """ OnParametersChanged(self: ParameterCollection, e: EventArgs) """
        ...

    def Remove(self, parameter:Parameter): # -> 
        """ Remove(self: ParameterCollection, parameter: Parameter) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ParameterCollection, index: int) """
        ...

    def UpdateValues(self, context:HttpContext, control:Control): # -> 
        """ UpdateValues(self: ParameterCollection, context: HttpContext, control: Control) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...

    ParametersChanged = ...


class ParsingCulture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParsingCulture, values: Current (1), Invariant (0) """
    Current: ParsingCulture = ...
    Invariant: ParsingCulture = ...
    value__ = ...


class PasswordRecovery(CompositeControl, IBorderPaddingControl, IRenderOuterTableControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ PasswordRecovery() """
    @property
    def Answer(self) -> str:
        """ Get: Answer(self: PasswordRecovery) -> str """
        ...

    @property
    def AnswerLabelText(self) -> str:
        """
        Get: AnswerLabelText(self: PasswordRecovery) -> str
        Set: AnswerLabelText(self: PasswordRecovery) = value
        """
        ...

    @property
    def AnswerRequiredErrorMessage(self) -> str:
        """
        Get: AnswerRequiredErrorMessage(self: PasswordRecovery) -> str
        Set: AnswerRequiredErrorMessage(self: PasswordRecovery) = value
        """
        ...

    @property
    def BorderPadding(self) -> int:
        """
        Get: BorderPadding(self: PasswordRecovery) -> int
        Set: BorderPadding(self: PasswordRecovery) = value
        """
        ...

    @property
    def FailureTextStyle(self) -> TableItemStyle:
        """ Get: FailureTextStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def GeneralFailureText(self) -> str:
        """
        Get: GeneralFailureText(self: PasswordRecovery) -> str
        Set: GeneralFailureText(self: PasswordRecovery) = value
        """
        ...

    @property
    def HelpPageIconUrl(self) -> str:
        """
        Get: HelpPageIconUrl(self: PasswordRecovery) -> str
        Set: HelpPageIconUrl(self: PasswordRecovery) = value
        """
        ...

    @property
    def HelpPageText(self) -> str:
        """
        Get: HelpPageText(self: PasswordRecovery) -> str
        Set: HelpPageText(self: PasswordRecovery) = value
        """
        ...

    @property
    def HelpPageUrl(self) -> str:
        """
        Get: HelpPageUrl(self: PasswordRecovery) -> str
        Set: HelpPageUrl(self: PasswordRecovery) = value
        """
        ...

    @property
    def HyperLinkStyle(self) -> TableItemStyle:
        """ Get: HyperLinkStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def InstructionTextStyle(self) -> TableItemStyle:
        """ Get: InstructionTextStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def LabelStyle(self) -> TableItemStyle:
        """ Get: LabelStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def MailDefinition(self) -> MailDefinition:
        """ Get: MailDefinition(self: PasswordRecovery) -> MailDefinition """
        ...

    @property
    def MembershipProvider(self) -> str:
        """
        Get: MembershipProvider(self: PasswordRecovery) -> str
        Set: MembershipProvider(self: PasswordRecovery) = value
        """
        ...

    @property
    def Question(self) -> str:
        """ Get: Question(self: PasswordRecovery) -> str """
        ...

    @property
    def QuestionFailureText(self) -> str:
        """
        Get: QuestionFailureText(self: PasswordRecovery) -> str
        Set: QuestionFailureText(self: PasswordRecovery) = value
        """
        ...

    @property
    def QuestionInstructionText(self) -> str:
        """
        Get: QuestionInstructionText(self: PasswordRecovery) -> str
        Set: QuestionInstructionText(self: PasswordRecovery) = value
        """
        ...

    @property
    def QuestionLabelText(self) -> str:
        """
        Get: QuestionLabelText(self: PasswordRecovery) -> str
        Set: QuestionLabelText(self: PasswordRecovery) = value
        """
        ...

    @property
    def QuestionTemplate(self) -> ITemplate:
        """
        Get: QuestionTemplate(self: PasswordRecovery) -> ITemplate
        Set: QuestionTemplate(self: PasswordRecovery) = value
        """
        ...

    @property
    def QuestionTemplateContainer(self) -> Control:
        """ Get: QuestionTemplateContainer(self: PasswordRecovery) -> Control """
        ...

    @property
    def QuestionTitleText(self) -> str:
        """
        Get: QuestionTitleText(self: PasswordRecovery) -> str
        Set: QuestionTitleText(self: PasswordRecovery) = value
        """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: PasswordRecovery) -> bool
        Set: RenderOuterTable(self: PasswordRecovery) = value
        """
        ...

    @property
    def SubmitButtonImageUrl(self) -> str:
        """
        Get: SubmitButtonImageUrl(self: PasswordRecovery) -> str
        Set: SubmitButtonImageUrl(self: PasswordRecovery) = value
        """
        ...

    @property
    def SubmitButtonStyle(self) -> Style:
        """ Get: SubmitButtonStyle(self: PasswordRecovery) -> Style """
        ...

    @property
    def SubmitButtonText(self) -> str:
        """
        Get: SubmitButtonText(self: PasswordRecovery) -> str
        Set: SubmitButtonText(self: PasswordRecovery) = value
        """
        ...

    @property
    def SubmitButtonType(self) -> ButtonType:
        """
        Get: SubmitButtonType(self: PasswordRecovery) -> ButtonType
        Set: SubmitButtonType(self: PasswordRecovery) = value
        """
        ...

    @property
    def SuccessPageUrl(self) -> str:
        """
        Get: SuccessPageUrl(self: PasswordRecovery) -> str
        Set: SuccessPageUrl(self: PasswordRecovery) = value
        """
        ...

    @property
    def SuccessTemplate(self) -> ITemplate:
        """
        Get: SuccessTemplate(self: PasswordRecovery) -> ITemplate
        Set: SuccessTemplate(self: PasswordRecovery) = value
        """
        ...

    @property
    def SuccessTemplateContainer(self) -> Control:
        """ Get: SuccessTemplateContainer(self: PasswordRecovery) -> Control """
        ...

    @property
    def SuccessText(self) -> str:
        """
        Get: SuccessText(self: PasswordRecovery) -> str
        Set: SuccessText(self: PasswordRecovery) = value
        """
        ...

    @property
    def SuccessTextStyle(self) -> TableItemStyle:
        """ Get: SuccessTextStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def TextBoxStyle(self) -> Style:
        """ Get: TextBoxStyle(self: PasswordRecovery) -> Style """
        ...

    @property
    def TextLayout(self) -> LoginTextLayout:
        """
        Get: TextLayout(self: PasswordRecovery) -> LoginTextLayout
        Set: TextLayout(self: PasswordRecovery) = value
        """
        ...

    @property
    def TitleTextStyle(self) -> TableItemStyle:
        """ Get: TitleTextStyle(self: PasswordRecovery) -> TableItemStyle """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: PasswordRecovery) -> str
        Set: UserName(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameFailureText(self) -> str:
        """
        Get: UserNameFailureText(self: PasswordRecovery) -> str
        Set: UserNameFailureText(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameInstructionText(self) -> str:
        """
        Get: UserNameInstructionText(self: PasswordRecovery) -> str
        Set: UserNameInstructionText(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameLabelText(self) -> str:
        """
        Get: UserNameLabelText(self: PasswordRecovery) -> str
        Set: UserNameLabelText(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameRequiredErrorMessage(self) -> str:
        """
        Get: UserNameRequiredErrorMessage(self: PasswordRecovery) -> str
        Set: UserNameRequiredErrorMessage(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameTemplate(self) -> ITemplate:
        """
        Get: UserNameTemplate(self: PasswordRecovery) -> ITemplate
        Set: UserNameTemplate(self: PasswordRecovery) = value
        """
        ...

    @property
    def UserNameTemplateContainer(self) -> Control:
        """ Get: UserNameTemplateContainer(self: PasswordRecovery) -> Control """
        ...

    @property
    def UserNameTitleText(self) -> str:
        """
        Get: UserNameTitleText(self: PasswordRecovery) -> str
        Set: UserNameTitleText(self: PasswordRecovery) = value
        """
        ...

    @property
    def ValidatorTextStyle(self) -> Style:
        """ Get: ValidatorTextStyle(self: PasswordRecovery) -> Style """
        ...


    def OnAnswerLookupError(self, *args): #cannot find CLR method
        """ OnAnswerLookupError(self: PasswordRecovery, e: EventArgs) """
        ...

    def OnSendingMail(self, *args): #cannot find CLR method
        """ OnSendingMail(self: PasswordRecovery, e: MailMessageEventArgs) """
        ...

    def OnSendMailError(self, *args): #cannot find CLR method
        """ OnSendMailError(self: PasswordRecovery, e: SendMailErrorEventArgs) """
        ...

    def OnUserLookupError(self, *args): #cannot find CLR method
        """ OnUserLookupError(self: PasswordRecovery, e: EventArgs) """
        ...

    def OnVerifyingAnswer(self, *args): #cannot find CLR method
        """ OnVerifyingAnswer(self: PasswordRecovery, e: LoginCancelEventArgs) """
        ...

    def OnVerifyingUser(self, *args): #cannot find CLR method
        """ OnVerifyingUser(self: PasswordRecovery, e: LoginCancelEventArgs) """
        ...

    AnswerLookupError = ...
    SendingMail = ...
    SendMailError = ...
    SubmitButtonCommandName: str = ...
    UserLookupError = ...
    VerifyingAnswer = ...
    VerifyingUser = ...


class PathDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PathDirection, values: CurrentToRoot (1), RootToCurrent (0) """
    CurrentToRoot: PathDirection = ...
    RootToCurrent: PathDirection = ...
    value__ = ...


class PlaceHolder(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ PlaceHolder() """
    pass

class PlaceHolderControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ PlaceHolderControlBuilder() """
    pass

class PolygonHotSpot(HotSpot): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ PolygonHotSpot() """
    @property
    def Coordinates(self) -> str:
        """
        Get: Coordinates(self: PolygonHotSpot) -> str
        Set: Coordinates(self: PolygonHotSpot) = value
        """
        ...



class ProfileParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    ProfileParameter()
    ProfileParameter(name: str, propertyName: str)
    ProfileParameter(name: str, type: TypeCode, propertyName: str)
    ProfileParameter(name: str, dbType: DbType, propertyName: str)
    """
    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ProfileParameter) -> str
        Set: PropertyName(self: ProfileParameter) = value
        """
        ...



class QueryableDataSourceEditData: # skipped bases: <type 'object'>, <type 'object'>
    """ QueryableDataSourceEditData() """
    @property
    def NewDataObject(self) -> object:
        """
        Get: NewDataObject(self: QueryableDataSourceEditData) -> object
        Set: NewDataObject(self: QueryableDataSourceEditData) = value
        """
        ...

    @property
    def OriginalDataObject(self) -> object:
        """
        Get: OriginalDataObject(self: QueryableDataSourceEditData) -> object
        Set: OriginalDataObject(self: QueryableDataSourceEditData) = value
        """
        ...



class QueryContext: # skipped bases: <type 'object'>, <type 'object'>
    """ QueryContext(whereParameters: IDictionary[str, object], orderGroupsByParameters: IDictionary[str, object], orderByParameters: IOrderedDictionary, groupByParameters: IDictionary[str, object], selectParameters: IDictionary[str, object], arguments: DataSourceSelectArguments) """
    @property
    def Arguments(self) -> DataSourceSelectArguments:
        """ Get: Arguments(self: QueryContext) -> DataSourceSelectArguments """
        ...

    @property
    def GroupByParameters(self) -> IDictionary:
        """ Get: GroupByParameters(self: QueryContext) -> IDictionary[str, object] """
        ...

    @property
    def OrderByParameters(self) -> IOrderedDictionary:
        """ Get: OrderByParameters(self: QueryContext) -> IOrderedDictionary """
        ...

    @property
    def OrderGroupsByParameters(self) -> IDictionary:
        """ Get: OrderGroupsByParameters(self: QueryContext) -> IDictionary[str, object] """
        ...

    @property
    def SelectParameters(self) -> IDictionary:
        """ Get: SelectParameters(self: QueryContext) -> IDictionary[str, object] """
        ...

    @property
    def WhereParameters(self) -> IDictionary:
        """ Get: WhereParameters(self: QueryContext) -> IDictionary[str, object] """
        ...



class QueryCreatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ QueryCreatedEventArgs(query: IQueryable) """
    @property
    def Query(self) -> IQueryable:
        """
        Get: Query(self: QueryCreatedEventArgs) -> IQueryable
        Set: Query(self: QueryCreatedEventArgs) = value
        """
        ...


    def __new__(cls, query:IQueryable) -> Self:
        """ __new__(cls: type, query: IQueryable) """
        ...


class QueryExtender(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ QueryExtender() """
    @property
    def DataSource(self) -> IQueryableDataSource:
        """ Get: DataSource(self: QueryExtender) -> IQueryableDataSource """
        ...

    @property
    def Expressions(self) -> DataSourceExpressionCollection:
        """ Get: Expressions(self: QueryExtender) -> DataSourceExpressionCollection """
        ...

    @property
    def TargetControlID(self) -> str:
        """
        Get: TargetControlID(self: QueryExtender) -> str
        Set: TargetControlID(self: QueryExtender) = value
        """
        ...



class QueryExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def SortBy(source:IQueryable, sortExpression:str) -> IQueryable:
        """ SortBy[T](source: IQueryable[T], sortExpression: str) -> IQueryable[T] """
        ...

    __all__: list = ...


class QueryStringParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    QueryStringParameter()
    QueryStringParameter(name: str, queryStringField: str)
    QueryStringParameter(name: str, dbType: DbType, queryStringField: str)
    QueryStringParameter(name: str, type: TypeCode, queryStringField: str)
    """
    @property
    def QueryStringField(self) -> str:
        """
        Get: QueryStringField(self: QueryStringParameter) -> str
        Set: QueryStringField(self: QueryStringParameter) = value
        """
        ...

    @property
    def ValidateInput(self) -> bool:
        """
        Get: ValidateInput(self: QueryStringParameter) -> bool
        Set: ValidateInput(self: QueryStringParameter) = value
        """
        ...



class RadioButton(CheckBox): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ICheckBoxControl'>, <type 'IPostBackDataHandler'>, <type 'object'>
    """ RadioButton() """
    @property
    def GroupName(self) -> str:
        """
        Get: GroupName(self: RadioButton) -> str
        Set: GroupName(self: RadioButton) = value
        """
        ...



class RadioButtonList(IPostBackDataHandler, INamingContainer, ListControl, IRepeatInfoUser): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IEditableTextControl'>, <type 'object'>
    """ RadioButtonList() """
    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: RadioButtonList) -> int
        Set: CellPadding(self: RadioButtonList) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: RadioButtonList) -> int
        Set: CellSpacing(self: RadioButtonList) = value
        """
        ...

    @property
    def RenderWhenDataEmpty(self) -> bool:
        """
        Get: RenderWhenDataEmpty(self: RadioButtonList) -> bool
        Set: RenderWhenDataEmpty(self: RadioButtonList) = value
        """
        ...

    @property
    def RepeatColumns(self) -> int:
        """
        Get: RepeatColumns(self: RadioButtonList) -> int
        Set: RepeatColumns(self: RadioButtonList) = value
        """
        ...

    @property
    def RepeatDirection(self): # -> RepeatDirection
        """
        Get: RepeatDirection(self: RadioButtonList) -> RepeatDirection
        Set: RepeatDirection(self: RadioButtonList) = value
        """
        ...

    @property
    def RepeatLayout(self): # -> RepeatLayout
        """
        Get: RepeatLayout(self: RadioButtonList) -> RepeatLayout
        Set: RepeatLayout(self: RadioButtonList) = value
        """
        ...

    @property
    def TextAlign(self): # -> TextAlign
        """
        Get: TextAlign(self: RadioButtonList) -> TextAlign
        Set: TextAlign(self: RadioButtonList) = value
        """
        ...



class RangeValidator(BaseCompareValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
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



class RectangleHotSpot(HotSpot): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ RectangleHotSpot() """
    @property
    def Bottom(self) -> int:
        """
        Get: Bottom(self: RectangleHotSpot) -> int
        Set: Bottom(self: RectangleHotSpot) = value
        """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: RectangleHotSpot) -> int
        Set: Left(self: RectangleHotSpot) = value
        """
        ...

    @property
    def Right(self) -> int:
        """
        Get: Right(self: RectangleHotSpot) -> int
        Set: Right(self: RectangleHotSpot) = value
        """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: RectangleHotSpot) -> int
        Set: Top(self: RectangleHotSpot) = value
        """
        ...



class RegularExpressionValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ RegularExpressionValidator() """
    @property
    def MatchTimeout(self) -> Nullable:
        """
        Get: MatchTimeout(self: RegularExpressionValidator) -> Nullable[int]
        Set: MatchTimeout(self: RegularExpressionValidator) = value
        """
        ...

    @property
    def ValidationExpression(self) -> str:
        """
        Get: ValidationExpression(self: RegularExpressionValidator) -> str
        Set: ValidationExpression(self: RegularExpressionValidator) = value
        """
        ...



class RepeatDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RepeatDirection, values: Horizontal (0), Vertical (1) """
    Horizontal: RepeatDirection = ...
    value__ = ...
    Vertical: RepeatDirection = ...


class Repeater(Control, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Repeater() """
    @property
    def AlternatingItemTemplate(self) -> ITemplate:
        """
        Get: AlternatingItemTemplate(self: Repeater) -> ITemplate
        Set: AlternatingItemTemplate(self: Repeater) = value
        """
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: Repeater) -> str
        Set: DataMember(self: Repeater) = value
        """
        ...

    @property
    def DataSource(self) -> object:
        """
        Get: DataSource(self: Repeater) -> object
        Set: DataSource(self: Repeater) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: Repeater) -> str
        Set: DataSourceID(self: Repeater) = value
        """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: Repeater) -> ITemplate
        Set: FooterTemplate(self: Repeater) = value
        """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: Repeater) -> ITemplate
        Set: HeaderTemplate(self: Repeater) = value
        """
        ...

    @property
    def Initialized(self):
        ...

    @property
    def IsBoundUsingDataSourceID(self):
        ...

    @property
    def IsDataBindingAutomatic(self):
        ...

    @property
    def Items(self): # -> RepeaterItemCollection
        """ Get: Items(self: Repeater) -> RepeaterItemCollection """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: Repeater) -> ITemplate
        Set: ItemTemplate(self: Repeater) = value
        """
        ...

    @property
    def ItemType(self) -> str:
        """
        Get: ItemType(self: Repeater) -> str
        Set: ItemType(self: Repeater) = value
        """
        ...

    @property
    def RequiresDataBinding(self):
        ...

    @property
    def SelectArguments(self):
        ...

    @property
    def SelectMethod(self) -> str:
        """
        Get: SelectMethod(self: Repeater) -> str
        Set: SelectMethod(self: Repeater) = value
        """
        ...

    @property
    def SeparatorTemplate(self) -> ITemplate:
        """
        Get: SeparatorTemplate(self: Repeater) -> ITemplate
        Set: SeparatorTemplate(self: Repeater) = value
        """
        ...


    def CreateControlHierarchy(self, *args): #cannot find CLR method
        """ CreateControlHierarchy(self: Repeater, useDataSource: bool) """
        ...

    def CreateDataSourceSelectArguments(self, *args): #cannot find CLR method
        """ CreateDataSourceSelectArguments(self: Repeater) -> DataSourceSelectArguments """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: Repeater, itemIndex: int, itemType: ListItemType) -> RepeaterItem """
        ...

    def EnsureDataBound(self, *args): #cannot find CLR method
        """ EnsureDataBound(self: Repeater) """
        ...

    def GetData(self, *args): #cannot find CLR method
        """ GetData(self: Repeater) -> IEnumerable """
        ...

    def InitializeItem(self, *args): #cannot find CLR method
        """ InitializeItem(self: Repeater, item: RepeaterItem) """
        ...

    def OnCreatingModelDataSource(self, *args): #cannot find CLR method
        """ OnCreatingModelDataSource(self: Repeater, e: CreatingModelDataSourceEventArgs) """
        ...

    def OnDataPropertyChanged(self, *args): #cannot find CLR method
        """ OnDataPropertyChanged(self: Repeater) """
        ...

    def OnDataSourceViewChanged(self, *args): #cannot find CLR method
        """ OnDataSourceViewChanged(self: Repeater, sender: object, e: EventArgs) """
        ...

    def OnItemCommand(self, *args): #cannot find CLR method
        """ OnItemCommand(self: Repeater, e: RepeaterCommandEventArgs) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: Repeater, e: RepeaterItemEventArgs) """
        ...

    def OnItemDataBound(self, *args): #cannot find CLR method
        """ OnItemDataBound(self: Repeater, e: RepeaterItemEventArgs) """
        ...

    CallingDataMethods = ...
    CreatingModelDataSource = ...
    ItemCommand = ...
    ItemCreated = ...
    ItemDataBound = ...


class RepeaterCommandEventArgs(CommandEventArgs): # skipped bases: <type 'object'>
    """ RepeaterCommandEventArgs(item: RepeaterItem, commandSource: object, originalArgs: CommandEventArgs) """
    @property
    def CommandSource(self) -> object:
        """ Get: CommandSource(self: RepeaterCommandEventArgs) -> object """
        ...

    @property
    def Item(self): # -> RepeaterItem
        """ Get: Item(self: RepeaterCommandEventArgs) -> RepeaterItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RepeaterCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RepeaterCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, e:RepeaterCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RepeaterCommandEventHandler, source: object, e: RepeaterCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RepeaterCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, e:RepeaterCommandEventArgs): # -> 
        """ Invoke(self: RepeaterCommandEventHandler, source: object, e: RepeaterCommandEventArgs) """
        ...


class RepeaterItem(Control, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ RepeaterItem(itemIndex: int, itemType: ListItemType) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: RepeaterItem) -> int """
        ...

    @property
    def ItemType(self) -> ListItemType:
        """ Get: ItemType(self: RepeaterItem) -> ListItemType """
        ...


    def __new__(cls, itemIndex:int, itemType:ListItemType) -> Self:
        """ __new__(cls: type, itemIndex: int, itemType: ListItemType) """
        ...


class RepeaterItemCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ RepeaterItemCollection(items: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: RepeaterItemCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: RepeaterItemCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class RepeaterItemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RepeaterItemEventArgs(item: RepeaterItem) """
    @property
    def Item(self) -> RepeaterItem:
        """ Get: Item(self: RepeaterItemEventArgs) -> RepeaterItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, item:RepeaterItem) -> Self:
        """ __new__(cls: type, item: RepeaterItem) """
        ...


class RepeaterItemEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RepeaterItemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RepeaterItemEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RepeaterItemEventHandler, sender: object, e: RepeaterItemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RepeaterItemEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RepeaterItemEventArgs): # -> 
        """ Invoke(self: RepeaterItemEventHandler, sender: object, e: RepeaterItemEventArgs) """
        ...


class RepeatInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ RepeatInfo() """
    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: RepeatInfo) -> str
        Set: Caption(self: RepeatInfo) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: RepeatInfo) -> TableCaptionAlign
        Set: CaptionAlign(self: RepeatInfo) = value
        """
        ...

    @property
    def OuterTableImplied(self) -> bool:
        """
        Get: OuterTableImplied(self: RepeatInfo) -> bool
        Set: OuterTableImplied(self: RepeatInfo) = value
        """
        ...

    @property
    def RepeatColumns(self) -> int:
        """
        Get: RepeatColumns(self: RepeatInfo) -> int
        Set: RepeatColumns(self: RepeatInfo) = value
        """
        ...

    @property
    def RepeatDirection(self) -> RepeatDirection:
        """
        Get: RepeatDirection(self: RepeatInfo) -> RepeatDirection
        Set: RepeatDirection(self: RepeatInfo) = value
        """
        ...

    @property
    def RepeatLayout(self): # -> RepeatLayout
        """
        Get: RepeatLayout(self: RepeatInfo) -> RepeatLayout
        Set: RepeatLayout(self: RepeatInfo) = value
        """
        ...

    @property
    def UseAccessibleHeader(self) -> bool:
        """
        Get: UseAccessibleHeader(self: RepeatInfo) -> bool
        Set: UseAccessibleHeader(self: RepeatInfo) = value
        """
        ...


    def RenderRepeater(self, writer:HtmlTextWriter, user:IRepeatInfoUser, controlStyle:Style, baseControl:WebControl): # -> 
        """ RenderRepeater(self: RepeatInfo, writer: HtmlTextWriter, user: IRepeatInfoUser, controlStyle: Style, baseControl: WebControl) """
        ...


class RepeatLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RepeatLayout, values: Flow (1), OrderedList (3), Table (0), UnorderedList (2) """
    Flow: RepeatLayout = ...
    OrderedList: RepeatLayout = ...
    Table: RepeatLayout = ...
    UnorderedList: RepeatLayout = ...
    value__ = ...


class RequiredFieldValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ RequiredFieldValidator() """
    @property
    def InitialValue(self) -> str:
        """
        Get: InitialValue(self: RequiredFieldValidator) -> str
        Set: InitialValue(self: RequiredFieldValidator) = value
        """
        ...



class RoleGroup: # skipped bases: <type 'object'>, <type 'object'>
    """ RoleGroup() """
    @property
    def ContentTemplate(self) -> ITemplate:
        """
        Get: ContentTemplate(self: RoleGroup) -> ITemplate
        Set: ContentTemplate(self: RoleGroup) = value
        """
        ...

    @property
    def Roles(self) -> Array:
        """
        Get: Roles(self: RoleGroup) -> Array[str]
        Set: Roles(self: RoleGroup) = value
        """
        ...


    def ContainsUser(self, user:IPrincipal) -> bool:
        """ ContainsUser(self: RoleGroup, user: IPrincipal) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: RoleGroup) -> str """
        ...


class RoleGroupCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ RoleGroupCollection() """
    def Add(self, group:RoleGroup): # -> 
        """ Add(self: RoleGroupCollection, group: RoleGroup) """
        ...

    def Contains(self, group:RoleGroup) -> bool:
        """ Contains(self: RoleGroupCollection, group: RoleGroup) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: RoleGroupCollection, array: Array[RoleGroup], index: int) """
        ...

    def GetMatchingRoleGroup(self, user:IPrincipal) -> RoleGroup:
        """ GetMatchingRoleGroup(self: RoleGroupCollection, user: IPrincipal) -> RoleGroup """
        ...

    def IndexOf(self, group:RoleGroup) -> int:
        """ IndexOf(self: RoleGroupCollection, group: RoleGroup) -> int """
        ...

    def Insert(self, index:int, group:RoleGroup): # -> 
        """ Insert(self: RoleGroupCollection, index: int, group: RoleGroup) """
        ...

    def Remove(self, group:RoleGroup): # -> 
        """ Remove(self: RoleGroupCollection, group: RoleGroup) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RouteParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    RouteParameter()
    RouteParameter(name: str, routeKey: str)
    RouteParameter(name: str, dbType: DbType, routeKey: str)
    RouteParameter(name: str, type: TypeCode, routeKey: str)
    """
    @property
    def RouteKey(self) -> str:
        """
        Get: RouteKey(self: RouteParameter) -> str
        Set: RouteKey(self: RouteParameter) = value
        """
        ...



class ScrollBars(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ScrollBars, values: Auto (4), Both (3), Horizontal (1), None (0), Vertical (2) """
    Auto: ScrollBars = ...
    Both: ScrollBars = ...
    Horizontal: ScrollBars = ...
    value__ = ...
    Vertical: ScrollBars = ...


class SelectedDatesCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ SelectedDatesCollection(dateList: ArrayList) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SelectedDatesCollection) -> bool """
        ...


    def Add(self, date:DateTime): # -> 
        """ Add(self: SelectedDatesCollection, date: DateTime) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SelectedDatesCollection) """
        ...

    def Contains(self, date:DateTime) -> bool:
        """ Contains(self: SelectedDatesCollection, date: DateTime) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SelectedDatesCollection) -> IEnumerator """
        ...

    def Remove(self, date:DateTime): # -> 
        """ Remove(self: SelectedDatesCollection, date: DateTime) """
        ...

    def SelectRange(self, fromDate:DateTime, toDate:DateTime): # -> 
        """ SelectRange(self: SelectedDatesCollection, fromDate: DateTime, toDate: DateTime) """
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


class SelectResult: # skipped bases: <type 'object'>, <type 'object'>
    """ SelectResult(totalRowCount: int, results: IEnumerable) """
    @property
    def Results(self) -> IEnumerable:
        """ Get: Results(self: SelectResult) -> IEnumerable """
        ...

    @property
    def TotalRowCount(self) -> int:
        """ Get: TotalRowCount(self: SelectResult) -> int """
        ...



class SendMailErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SendMailErrorEventArgs(e: Exception) """
    @property
    def Exception(self) -> Exception:
        """
        Get: Exception(self: SendMailErrorEventArgs) -> Exception
        Set: Exception(self: SendMailErrorEventArgs) = value
        """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: SendMailErrorEventArgs) -> bool
        Set: Handled(self: SendMailErrorEventArgs) = value
        """
        ...


    def __new__(cls, e:Exception) -> Self:
        """ __new__(cls: type, e: Exception) """
        ...


class SendMailErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SendMailErrorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SendMailErrorEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SendMailErrorEventHandler, sender: object, e: SendMailErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SendMailErrorEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SendMailErrorEventArgs): # -> 
        """ Invoke(self: SendMailErrorEventHandler, sender: object, e: SendMailErrorEventArgs) """
        ...


class ServerValidateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ServerValidateEventArgs(value: str, isValid: bool) """
    @property
    def IsValid(self) -> bool:
        """
        Get: IsValid(self: ServerValidateEventArgs) -> bool
        Set: IsValid(self: ServerValidateEventArgs) = value
        """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: ServerValidateEventArgs) -> str """
        ...


    def __new__(cls, value:str, isValid:bool) -> Self:
        """ __new__(cls: type, value: str, isValid: bool) """
        ...


class ServerValidateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ServerValidateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, source:object, args:ServerValidateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ServerValidateEventHandler, source: object, args: ServerValidateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ServerValidateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, source:object, args:ServerValidateEventArgs): # -> 
        """ Invoke(self: ServerValidateEventHandler, source: object, args: ServerValidateEventArgs) """
        ...


class SessionParameter(Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    SessionParameter()
    SessionParameter(name: str, sessionField: str)
    SessionParameter(name: str, dbType: DbType, sessionField: str)
    SessionParameter(name: str, type: TypeCode, sessionField: str)
    """
    @property
    def SessionField(self) -> str:
        """
        Get: SessionField(self: SessionParameter) -> str
        Set: SessionField(self: SessionParameter) = value
        """
        ...



class SiteMapDataSource(IDataSource, IListSource, HierarchicalDataSourceControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IHierarchicalDataSource'>, <type 'object'>
    """ SiteMapDataSource() """
    @property
    def Provider(self) -> SiteMapProvider:
        """
        Get: Provider(self: SiteMapDataSource) -> SiteMapProvider
        Set: Provider(self: SiteMapDataSource) = value
        """
        ...

    @property
    def ShowStartingNode(self) -> bool:
        """
        Get: ShowStartingNode(self: SiteMapDataSource) -> bool
        Set: ShowStartingNode(self: SiteMapDataSource) = value
        """
        ...

    @property
    def SiteMapProvider(self) -> str:
        """
        Get: SiteMapProvider(self: SiteMapDataSource) -> str
        Set: SiteMapProvider(self: SiteMapDataSource) = value
        """
        ...

    @property
    def StartFromCurrentNode(self) -> bool:
        """
        Get: StartFromCurrentNode(self: SiteMapDataSource) -> bool
        Set: StartFromCurrentNode(self: SiteMapDataSource) = value
        """
        ...

    @property
    def StartingNodeOffset(self) -> int:
        """
        Get: StartingNodeOffset(self: SiteMapDataSource) -> int
        Set: StartingNodeOffset(self: SiteMapDataSource) = value
        """
        ...

    @property
    def StartingNodeUrl(self) -> str:
        """
        Get: StartingNodeUrl(self: SiteMapDataSource) -> str
        Set: StartingNodeUrl(self: SiteMapDataSource) = value
        """
        ...



class SiteMapDataSourceView(DataSourceView): # skipped bases: <type 'object'>
    """
    SiteMapDataSourceView(owner: SiteMapDataSource, name: str, node: SiteMapNode)
    SiteMapDataSourceView(owner: SiteMapDataSource, name: str, collection: SiteMapNodeCollection)
    """
    pass

class SiteMapHierarchicalDataSourceView(HierarchicalDataSourceView): # skipped bases: <type 'object'>
    """
    SiteMapHierarchicalDataSourceView(node: SiteMapNode)
    SiteMapHierarchicalDataSourceView(collection: SiteMapNodeCollection)
    """
    def __new__(cls, *__args:SiteMapNode) -> Self:
        """
        __new__(cls: type, node: SiteMapNode)
        __new__(cls: type, collection: SiteMapNodeCollection)
        """
        ...


class SiteMapNodeItem(WebControl, IDataItemContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ SiteMapNodeItem(itemIndex: int, itemType: SiteMapNodeItemType) """
    @property
    def ItemIndex(self) -> int:
        """ Get: ItemIndex(self: SiteMapNodeItem) -> int """
        ...

    @property
    def ItemType(self): # -> SiteMapNodeItemType
        """ Get: ItemType(self: SiteMapNodeItem) -> SiteMapNodeItemType """
        ...

    @property
    def SiteMapNode(self) -> SiteMapNode:
        """
        Get: SiteMapNode(self: SiteMapNodeItem) -> SiteMapNode
        Set: SiteMapNode(self: SiteMapNodeItem) = value
        """
        ...


    def SetItemType(self, *args): #cannot find CLR method
        """ SetItemType(self: SiteMapNodeItem, itemType: SiteMapNodeItemType) """
        ...


class SiteMapNodeItemEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SiteMapNodeItemEventArgs(item: SiteMapNodeItem) """
    @property
    def Item(self) -> SiteMapNodeItem:
        """ Get: Item(self: SiteMapNodeItemEventArgs) -> SiteMapNodeItem """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, item:SiteMapNodeItem) -> Self:
        """ __new__(cls: type, item: SiteMapNodeItem) """
        ...


class SiteMapNodeItemEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SiteMapNodeItemEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SiteMapNodeItemEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SiteMapNodeItemEventHandler, sender: object, e: SiteMapNodeItemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SiteMapNodeItemEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SiteMapNodeItemEventArgs): # -> 
        """ Invoke(self: SiteMapNodeItemEventHandler, sender: object, e: SiteMapNodeItemEventArgs) """
        ...


class SiteMapNodeItemType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SiteMapNodeItemType, values: Current (2), Parent (1), PathSeparator (3), Root (0) """
    Current: SiteMapNodeItemType = ...
    Parent: SiteMapNodeItemType = ...
    PathSeparator: SiteMapNodeItemType = ...
    Root: SiteMapNodeItemType = ...
    value__ = ...


class SiteMapPath(CompositeControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'ICompositeControlDesignerAccessor'>, <type 'object'>
    """ SiteMapPath() """
    @property
    def CurrentNodeStyle(self) -> Style:
        """ Get: CurrentNodeStyle(self: SiteMapPath) -> Style """
        ...

    @property
    def CurrentNodeTemplate(self) -> ITemplate:
        """
        Get: CurrentNodeTemplate(self: SiteMapPath) -> ITemplate
        Set: CurrentNodeTemplate(self: SiteMapPath) = value
        """
        ...

    @property
    def NodeStyle(self) -> Style:
        """ Get: NodeStyle(self: SiteMapPath) -> Style """
        ...

    @property
    def NodeTemplate(self) -> ITemplate:
        """
        Get: NodeTemplate(self: SiteMapPath) -> ITemplate
        Set: NodeTemplate(self: SiteMapPath) = value
        """
        ...

    @property
    def ParentLevelsDisplayed(self) -> int:
        """
        Get: ParentLevelsDisplayed(self: SiteMapPath) -> int
        Set: ParentLevelsDisplayed(self: SiteMapPath) = value
        """
        ...

    @property
    def PathDirection(self) -> PathDirection:
        """
        Get: PathDirection(self: SiteMapPath) -> PathDirection
        Set: PathDirection(self: SiteMapPath) = value
        """
        ...

    @property
    def PathSeparator(self) -> str:
        """
        Get: PathSeparator(self: SiteMapPath) -> str
        Set: PathSeparator(self: SiteMapPath) = value
        """
        ...

    @property
    def PathSeparatorStyle(self) -> Style:
        """ Get: PathSeparatorStyle(self: SiteMapPath) -> Style """
        ...

    @property
    def PathSeparatorTemplate(self) -> ITemplate:
        """
        Get: PathSeparatorTemplate(self: SiteMapPath) -> ITemplate
        Set: PathSeparatorTemplate(self: SiteMapPath) = value
        """
        ...

    @property
    def Provider(self) -> SiteMapProvider:
        """
        Get: Provider(self: SiteMapPath) -> SiteMapProvider
        Set: Provider(self: SiteMapPath) = value
        """
        ...

    @property
    def RenderCurrentNodeAsLink(self) -> bool:
        """
        Get: RenderCurrentNodeAsLink(self: SiteMapPath) -> bool
        Set: RenderCurrentNodeAsLink(self: SiteMapPath) = value
        """
        ...

    @property
    def RootNodeStyle(self) -> Style:
        """ Get: RootNodeStyle(self: SiteMapPath) -> Style """
        ...

    @property
    def RootNodeTemplate(self) -> ITemplate:
        """
        Get: RootNodeTemplate(self: SiteMapPath) -> ITemplate
        Set: RootNodeTemplate(self: SiteMapPath) = value
        """
        ...

    @property
    def ShowToolTips(self) -> bool:
        """
        Get: ShowToolTips(self: SiteMapPath) -> bool
        Set: ShowToolTips(self: SiteMapPath) = value
        """
        ...

    @property
    def SiteMapProvider(self) -> str:
        """
        Get: SiteMapProvider(self: SiteMapPath) -> str
        Set: SiteMapProvider(self: SiteMapPath) = value
        """
        ...

    @property
    def SkipLinkText(self) -> str:
        """
        Get: SkipLinkText(self: SiteMapPath) -> str
        Set: SkipLinkText(self: SiteMapPath) = value
        """
        ...


    def CreateControlHierarchy(self, *args): #cannot find CLR method
        """ CreateControlHierarchy(self: SiteMapPath) """
        ...

    def InitializeItem(self, *args): #cannot find CLR method
        """ InitializeItem(self: SiteMapPath, item: SiteMapNodeItem) """
        ...

    def OnItemCreated(self, *args): #cannot find CLR method
        """ OnItemCreated(self: SiteMapPath, e: SiteMapNodeItemEventArgs) """
        ...

    def OnItemDataBound(self, *args): #cannot find CLR method
        """ OnItemDataBound(self: SiteMapPath, e: SiteMapNodeItemEventArgs) """
        ...

    ItemCreated = ...
    ItemDataBound = ...


class SortDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SortDirection, values: Ascending (0), Descending (1) """
    Ascending: SortDirection = ...
    Descending: SortDirection = ...
    value__ = ...


class SqlDataSourceCommandEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ SqlDataSourceCommandEventArgs(command: DbCommand) """
    @property
    def Command(self) -> DbCommand:
        """ Get: Command(self: SqlDataSourceCommandEventArgs) -> DbCommand """
        ...



class SqlDataSourceCommandEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlDataSourceCommandEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlDataSourceCommandEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlDataSourceCommandEventHandler, sender: object, e: SqlDataSourceCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlDataSourceCommandEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlDataSourceCommandEventArgs): # -> 
        """ Invoke(self: SqlDataSourceCommandEventHandler, sender: object, e: SqlDataSourceCommandEventArgs) """
        ...


class SqlDataSourceCommandType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDataSourceCommandType, values: StoredProcedure (1), Text (0) """
    StoredProcedure: SqlDataSourceCommandType = ...
    Text: SqlDataSourceCommandType = ...
    value__ = ...


class SqlDataSourceFilteringEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ SqlDataSourceFilteringEventArgs(parameterValues: IOrderedDictionary) """
    @property
    def ParameterValues(self) -> IOrderedDictionary:
        """ Get: ParameterValues(self: SqlDataSourceFilteringEventArgs) -> IOrderedDictionary """
        ...



class SqlDataSourceFilteringEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlDataSourceFilteringEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlDataSourceFilteringEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlDataSourceFilteringEventHandler, sender: object, e: SqlDataSourceFilteringEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlDataSourceFilteringEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlDataSourceFilteringEventArgs): # -> 
        """ Invoke(self: SqlDataSourceFilteringEventHandler, sender: object, e: SqlDataSourceFilteringEventArgs) """
        ...


class SqlDataSourceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDataSourceMode, values: DataReader (0), DataSet (1) """
    DataReader: SqlDataSourceMode = ...
    DataSet: SqlDataSourceMode = ...
    value__ = ...


class SqlDataSourceSelectingEventArgs(SqlDataSourceCommandEventArgs): # skipped bases: <type 'object'>
    """ SqlDataSourceSelectingEventArgs(command: DbCommand, arguments: DataSourceSelectArguments) """
    @property
    def Arguments(self) -> DataSourceSelectArguments:
        """ Get: Arguments(self: SqlDataSourceSelectingEventArgs) -> DataSourceSelectArguments """
        ...



class SqlDataSourceSelectingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlDataSourceSelectingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlDataSourceSelectingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlDataSourceSelectingEventHandler, sender: object, e: SqlDataSourceSelectingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlDataSourceSelectingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlDataSourceSelectingEventArgs): # -> 
        """ Invoke(self: SqlDataSourceSelectingEventHandler, sender: object, e: SqlDataSourceSelectingEventArgs) """
        ...


class SqlDataSourceStatusEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SqlDataSourceStatusEventArgs(command: DbCommand, affectedRows: int, exception: Exception) """
    @property
    def AffectedRows(self) -> int:
        """ Get: AffectedRows(self: SqlDataSourceStatusEventArgs) -> int """
        ...

    @property
    def Command(self) -> DbCommand:
        """ Get: Command(self: SqlDataSourceStatusEventArgs) -> DbCommand """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: SqlDataSourceStatusEventArgs) -> Exception """
        ...

    @property
    def ExceptionHandled(self) -> bool:
        """
        Get: ExceptionHandled(self: SqlDataSourceStatusEventArgs) -> bool
        Set: ExceptionHandled(self: SqlDataSourceStatusEventArgs) = value
        """
        ...


    def __new__(cls, command:DbCommand, affectedRows:int, exception:Exception) -> Self:
        """ __new__(cls: type, command: DbCommand, affectedRows: int, exception: Exception) """
        ...


class SqlDataSourceStatusEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlDataSourceStatusEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlDataSourceStatusEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlDataSourceStatusEventHandler, sender: object, e: SqlDataSourceStatusEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlDataSourceStatusEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlDataSourceStatusEventArgs): # -> 
        """ Invoke(self: SqlDataSourceStatusEventHandler, sender: object, e: SqlDataSourceStatusEventArgs) """
        ...


class StringArrayConverter(TypeConverter): # skipped bases: <type 'object'>
    """ StringArrayConverter() """
    pass

class StyleCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, style:Style) -> int:
        """ Add(self: StyleCollection, style: Style) -> int """
        ...

    def Contains(self, style:Style) -> bool:
        """ Contains(self: StyleCollection, style: Style) -> bool """
        ...

    def IndexOf(self, style:Style) -> int:
        """ IndexOf(self: StyleCollection, style: Style) -> int """
        ...

    def Insert(self, index:int, style:Style): # -> 
        """ Insert(self: StyleCollection, index: int, style: Style) """
        ...

    def Remove(self, style:Style): # -> 
        """ Remove(self: StyleCollection, style: Style) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: StyleCollection, index: int) """
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


class SubMenuStyle(ICustomTypeDescriptor, Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    SubMenuStyle()
    SubMenuStyle(bag: StateBag)
    """
    @property
    def HorizontalPadding(self): # -> Unit
        """
        Get: HorizontalPadding(self: SubMenuStyle) -> Unit
        Set: HorizontalPadding(self: SubMenuStyle) = value
        """
        ...

    @property
    def VerticalPadding(self): # -> Unit
        """
        Get: VerticalPadding(self: SubMenuStyle) -> Unit
        Set: VerticalPadding(self: SubMenuStyle) = value
        """
        ...



class SubMenuStyleCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, style:SubMenuStyle) -> int:
        """ Add(self: SubMenuStyleCollection, style: SubMenuStyle) -> int """
        ...

    def Contains(self, style:SubMenuStyle) -> bool:
        """ Contains(self: SubMenuStyleCollection, style: SubMenuStyle) -> bool """
        ...

    def IndexOf(self, style:SubMenuStyle) -> int:
        """ IndexOf(self: SubMenuStyleCollection, style: SubMenuStyle) -> int """
        ...

    def Insert(self, index:int, style:SubMenuStyle): # -> 
        """ Insert(self: SubMenuStyleCollection, index: int, style: SubMenuStyle) """
        ...

    def Remove(self, style:SubMenuStyle): # -> 
        """ Remove(self: SubMenuStyleCollection, style: SubMenuStyle) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SubMenuStyleCollection, index: int) """
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


class Substitution(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Substitution() """
    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: Substitution) -> str
        Set: MethodName(self: Substitution) = value
        """
        ...



class Table(WebControl, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Table() """
    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: Table) -> str
        Set: BackImageUrl(self: Table) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: Table) -> str
        Set: Caption(self: Table) = value
        """
        ...

    @property
    def CaptionAlign(self): # -> TableCaptionAlign
        """
        Get: CaptionAlign(self: Table) -> TableCaptionAlign
        Set: CaptionAlign(self: Table) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: Table) -> int
        Set: CellPadding(self: Table) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: Table) -> int
        Set: CellSpacing(self: Table) = value
        """
        ...

    @property
    def GridLines(self) -> GridLines:
        """
        Get: GridLines(self: Table) -> GridLines
        Set: GridLines(self: Table) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: Table) -> HorizontalAlign
        Set: HorizontalAlign(self: Table) = value
        """
        ...

    @property
    def Rows(self): # -> TableRowCollection
        """ Get: Rows(self: Table) -> TableRowCollection """
        ...


    def RowControlCollection(self, *args): #cannot find CLR method
        """ no doc """
        ...



class TableCaptionAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TableCaptionAlign, values: Bottom (2), Left (3), NotSet (0), Right (4), Top (1) """
    Bottom: TableCaptionAlign = ...
    Left: TableCaptionAlign = ...
    NotSet: TableCaptionAlign = ...
    Right: TableCaptionAlign = ...
    Top: TableCaptionAlign = ...
    value__ = ...


class TableCellCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: TableCellCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: TableCellCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: TableCellCollection) -> object """
        ...


    def AddAt(self, index:int, cell:TableCell): # -> 
        """ AddAt(self: TableCellCollection, index: int, cell: TableCell) """
        ...

    def AddRange(self, cells:Array): # -> 
        """ AddRange(self: TableCellCollection, cells: Array[TableCell]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TableCellCollection, array: Array, index: int) """
        ...

    def GetCellIndex(self, cell:TableCell) -> int:
        """ GetCellIndex(self: TableCellCollection, cell: TableCell) -> int """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TableCellCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class TableCellControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ TableCellControlBuilder() """
    pass

class TableFooterRow(TableRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TableFooterRow() """
    pass

class TableHeaderCell(TableCell): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TableHeaderCell() """
    @property
    def AbbreviatedText(self) -> str:
        """
        Get: AbbreviatedText(self: TableHeaderCell) -> str
        Set: AbbreviatedText(self: TableHeaderCell) = value
        """
        ...

    @property
    def CategoryText(self) -> Array:
        """
        Get: CategoryText(self: TableHeaderCell) -> Array[str]
        Set: CategoryText(self: TableHeaderCell) = value
        """
        ...

    @property
    def Scope(self): # -> TableHeaderScope
        """
        Get: Scope(self: TableHeaderCell) -> TableHeaderScope
        Set: Scope(self: TableHeaderCell) = value
        """
        ...



class TableHeaderRow(TableRow): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TableHeaderRow() """
    pass

class TableHeaderScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TableHeaderScope, values: Column (2), NotSet (0), Row (1) """
    Column: TableHeaderScope = ...
    NotSet: TableHeaderScope = ...
    Row: TableHeaderScope = ...
    value__ = ...


class TableRowCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: TableRowCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: TableRowCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: TableRowCollection) -> object """
        ...


    def AddAt(self, index:int, row:TableRow): # -> 
        """ AddAt(self: TableRowCollection, index: int, row: TableRow) """
        ...

    def AddRange(self, rows:Array): # -> 
        """ AddRange(self: TableRowCollection, rows: Array[TableRow]) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TableRowCollection, array: Array, index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TableRowCollection) -> IEnumerator """
        ...

    def GetRowIndex(self, row:TableRow) -> int:
        """ GetRowIndex(self: TableRowCollection, row: TableRow) -> int """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class TableRowSection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TableRowSection, values: TableBody (1), TableFooter (2), TableHeader (0) """
    TableBody: TableRowSection = ...
    TableFooter: TableRowSection = ...
    TableHeader: TableRowSection = ...
    value__ = ...


class TableSectionStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """ TableSectionStyle() """
    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: TableSectionStyle) -> bool
        Set: Visible(self: TableSectionStyle) = value
        """
        ...



class TableStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    TableStyle()
    TableStyle(bag: StateBag)
    """
    @property
    def BackImageUrl(self) -> str:
        """
        Get: BackImageUrl(self: TableStyle) -> str
        Set: BackImageUrl(self: TableStyle) = value
        """
        ...

    @property
    def CellPadding(self) -> int:
        """
        Get: CellPadding(self: TableStyle) -> int
        Set: CellPadding(self: TableStyle) = value
        """
        ...

    @property
    def CellSpacing(self) -> int:
        """
        Get: CellSpacing(self: TableStyle) -> int
        Set: CellSpacing(self: TableStyle) = value
        """
        ...

    @property
    def GridLines(self) -> GridLines:
        """
        Get: GridLines(self: TableStyle) -> GridLines
        Set: GridLines(self: TableStyle) = value
        """
        ...

    @property
    def HorizontalAlign(self) -> HorizontalAlign:
        """
        Get: HorizontalAlign(self: TableStyle) -> HorizontalAlign
        Set: HorizontalAlign(self: TableStyle) = value
        """
        ...



class TargetConverter(StringConverter): # skipped bases: <type 'object'>
    """ TargetConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: TargetConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: TargetConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: TargetConverter, context: ITypeDescriptorContext) -> bool """
        ...


class TemplateColumn(DataGridColumn): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ TemplateColumn() """
    @property
    def EditItemTemplate(self) -> ITemplate:
        """
        Get: EditItemTemplate(self: TemplateColumn) -> ITemplate
        Set: EditItemTemplate(self: TemplateColumn) = value
        """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: TemplateColumn) -> ITemplate
        Set: FooterTemplate(self: TemplateColumn) = value
        """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: TemplateColumn) -> ITemplate
        Set: HeaderTemplate(self: TemplateColumn) = value
        """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: TemplateColumn) -> ITemplate
        Set: ItemTemplate(self: TemplateColumn) = value
        """
        ...



class TemplateField(DataControlField): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ TemplateField() """
    @property
    def AlternatingItemTemplate(self) -> ITemplate:
        """
        Get: AlternatingItemTemplate(self: TemplateField) -> ITemplate
        Set: AlternatingItemTemplate(self: TemplateField) = value
        """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """
        Get: ConvertEmptyStringToNull(self: TemplateField) -> bool
        Set: ConvertEmptyStringToNull(self: TemplateField) = value
        """
        ...

    @property
    def EditItemTemplate(self) -> ITemplate:
        """
        Get: EditItemTemplate(self: TemplateField) -> ITemplate
        Set: EditItemTemplate(self: TemplateField) = value
        """
        ...

    @property
    def FooterTemplate(self) -> ITemplate:
        """
        Get: FooterTemplate(self: TemplateField) -> ITemplate
        Set: FooterTemplate(self: TemplateField) = value
        """
        ...

    @property
    def HeaderTemplate(self) -> ITemplate:
        """
        Get: HeaderTemplate(self: TemplateField) -> ITemplate
        Set: HeaderTemplate(self: TemplateField) = value
        """
        ...

    @property
    def InsertItemTemplate(self) -> ITemplate:
        """
        Get: InsertItemTemplate(self: TemplateField) -> ITemplate
        Set: InsertItemTemplate(self: TemplateField) = value
        """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: TemplateField) -> ITemplate
        Set: ItemTemplate(self: TemplateField) = value
        """
        ...



class TemplatePagerField(DataPagerField): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ TemplatePagerField() """
    @property
    def PagerTemplate(self) -> ITemplate:
        """
        Get: PagerTemplate(self: TemplatePagerField) -> ITemplate
        Set: PagerTemplate(self: TemplatePagerField) = value
        """
        ...


    def OnPagerCommand(self, *args): #cannot find CLR method
        """ OnPagerCommand(self: TemplatePagerField, e: DataPagerCommandEventArgs) """
        ...

    PagerCommand = ...


class TextAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextAlign, values: Left (1), Right (2) """
    Left: TextAlign = ...
    Right: TextAlign = ...
    value__ = ...


class TextBox(IPostBackDataHandler, WebControl, IEditableTextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'object'>
    """ TextBox() """
    @property
    def AutoCompleteType(self) -> AutoCompleteType:
        """
        Get: AutoCompleteType(self: TextBox) -> AutoCompleteType
        Set: AutoCompleteType(self: TextBox) = value
        """
        ...

    @property
    def AutoPostBack(self) -> bool:
        """
        Get: AutoPostBack(self: TextBox) -> bool
        Set: AutoPostBack(self: TextBox) = value
        """
        ...

    @property
    def CausesValidation(self) -> bool:
        """
        Get: CausesValidation(self: TextBox) -> bool
        Set: CausesValidation(self: TextBox) = value
        """
        ...

    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: TextBox) -> int
        Set: Columns(self: TextBox) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: TextBox) -> int
        Set: MaxLength(self: TextBox) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: TextBox) -> bool
        Set: ReadOnly(self: TextBox) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: TextBox) -> int
        Set: Rows(self: TextBox) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextBox) -> str
        Set: Text(self: TextBox) = value
        """
        ...

    @property
    def TextMode(self): # -> TextBoxMode
        """
        Get: TextMode(self: TextBox) -> TextBoxMode
        Set: TextMode(self: TextBox) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: TextBox) -> str
        Set: ValidationGroup(self: TextBox) = value
        """
        ...

    @property
    def Wrap(self) -> bool:
        """
        Get: Wrap(self: TextBox) -> bool
        Set: Wrap(self: TextBox) = value
        """
        ...


    def OnTextChanged(self, *args): #cannot find CLR method
        """ OnTextChanged(self: TextBox, e: EventArgs) """
        ...

    TextChanged = ...


class TextBoxControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ TextBoxControlBuilder() """
    pass

class TextBoxMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextBoxMode, values: Color (3), Date (4), DateTime (5), DateTimeLocal (6), Email (7), Month (8), MultiLine (1), Number (9), Password (2), Phone (12), Range (10), Search (11), SingleLine (0), Time (13), Url (14), Week (15) """
    Color: TextBoxMode = ...
    Date: TextBoxMode = ...
    DateTime: TextBoxMode = ...
    DateTimeLocal: TextBoxMode = ...
    Email: TextBoxMode = ...
    Month: TextBoxMode = ...
    MultiLine: TextBoxMode = ...
    Number: TextBoxMode = ...
    Password: TextBoxMode = ...
    Phone: TextBoxMode = ...
    Range: TextBoxMode = ...
    Search: TextBoxMode = ...
    SingleLine: TextBoxMode = ...
    Time: TextBoxMode = ...
    Url: TextBoxMode = ...
    value__ = ...
    Week: TextBoxMode = ...


class TitleFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TitleFormat, values: Month (0), MonthYear (1) """
    Month: TitleFormat = ...
    MonthYear: TitleFormat = ...
    value__ = ...


class TreeNode(ICloneable, IStateManager): # skipped bases: <type 'object'>
    """
    TreeNode()
    TreeNode(text: str)
    TreeNode(text: str, value: str)
    TreeNode(text: str, value: str, imageUrl: str)
    TreeNode(text: str, value: str, imageUrl: str, navigateUrl: str, target: str)
    """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: TreeNode) -> bool
        Set: Checked(self: TreeNode) = value
        """
        ...

    @property
    def ChildNodes(self) -> TreeNodeCollection:
        """ Get: ChildNodes(self: TreeNode) -> TreeNodeCollection """
        ...

    @property
    def DataBound(self) -> bool:
        """ Get: DataBound(self: TreeNode) -> bool """
        ...

    @property
    def DataItem(self) -> object:
        """ Get: DataItem(self: TreeNode) -> object """
        ...

    @property
    def DataPath(self) -> str:
        """ Get: DataPath(self: TreeNode) -> str """
        ...

    @property
    def Depth(self) -> int:
        """ Get: Depth(self: TreeNode) -> int """
        ...

    @property
    def Expanded(self) -> Nullable:
        """
        Get: Expanded(self: TreeNode) -> Nullable[bool]
        Set: Expanded(self: TreeNode) = value
        """
        ...

    @property
    def ImageToolTip(self) -> str:
        """
        Get: ImageToolTip(self: TreeNode) -> str
        Set: ImageToolTip(self: TreeNode) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: TreeNode) -> str
        Set: ImageUrl(self: TreeNode) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: TreeNode) -> str
        Set: NavigateUrl(self: TreeNode) = value
        """
        ...

    @property
    def Parent(self) -> TreeNode:
        """ Get: Parent(self: TreeNode) -> TreeNode """
        ...

    @property
    def PopulateOnDemand(self) -> bool:
        """
        Get: PopulateOnDemand(self: TreeNode) -> bool
        Set: PopulateOnDemand(self: TreeNode) = value
        """
        ...

    @property
    def SelectAction(self): # -> TreeNodeSelectAction
        """
        Get: SelectAction(self: TreeNode) -> TreeNodeSelectAction
        Set: SelectAction(self: TreeNode) = value
        """
        ...

    @property
    def Selected(self) -> bool:
        """
        Get: Selected(self: TreeNode) -> bool
        Set: Selected(self: TreeNode) = value
        """
        ...

    @property
    def ShowCheckBox(self) -> Nullable:
        """
        Get: ShowCheckBox(self: TreeNode) -> Nullable[bool]
        Set: ShowCheckBox(self: TreeNode) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: TreeNode) -> str
        Set: Target(self: TreeNode) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TreeNode) -> str
        Set: Text(self: TreeNode) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: TreeNode) -> str
        Set: ToolTip(self: TreeNode) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: TreeNode) -> str
        Set: Value(self: TreeNode) = value
        """
        ...

    @property
    def ValuePath(self) -> str:
        """ Get: ValuePath(self: TreeNode) -> str """
        ...


    def Collapse(self): # -> 
        """ Collapse(self: TreeNode) """
        ...

    def CollapseAll(self): # -> 
        """ CollapseAll(self: TreeNode) """
        ...

    def Expand(self): # -> 
        """ Expand(self: TreeNode) """
        ...

    def ExpandAll(self): # -> 
        """ ExpandAll(self: TreeNode) """
        ...

    def RenderPostText(self, *args): #cannot find CLR method
        """ RenderPostText(self: TreeNode, writer: HtmlTextWriter) """
        ...

    def RenderPreText(self, *args): #cannot find CLR method
        """ RenderPreText(self: TreeNode, writer: HtmlTextWriter) """
        ...

    def Select(self): # -> 
        """ Select(self: TreeNode) """
        ...

    def ToggleExpandState(self): # -> 
        """ ToggleExpandState(self: TreeNode) """
        ...


class TreeNodeBinding(IDataSourceViewSchemaAccessor, ICloneable, IStateManager): # skipped bases: <type 'object'>
    """ TreeNodeBinding() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: TreeNodeBinding) -> str
        Set: DataMember(self: TreeNodeBinding) = value
        """
        ...

    @property
    def Depth(self) -> int:
        """
        Get: Depth(self: TreeNodeBinding) -> int
        Set: Depth(self: TreeNodeBinding) = value
        """
        ...

    @property
    def FormatString(self) -> str:
        """
        Get: FormatString(self: TreeNodeBinding) -> str
        Set: FormatString(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ImageToolTip(self) -> str:
        """
        Get: ImageToolTip(self: TreeNodeBinding) -> str
        Set: ImageToolTip(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ImageToolTipField(self) -> str:
        """
        Get: ImageToolTipField(self: TreeNodeBinding) -> str
        Set: ImageToolTipField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: TreeNodeBinding) -> str
        Set: ImageUrl(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ImageUrlField(self) -> str:
        """
        Get: ImageUrlField(self: TreeNodeBinding) -> str
        Set: ImageUrlField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def NavigateUrl(self) -> str:
        """
        Get: NavigateUrl(self: TreeNodeBinding) -> str
        Set: NavigateUrl(self: TreeNodeBinding) = value
        """
        ...

    @property
    def NavigateUrlField(self) -> str:
        """
        Get: NavigateUrlField(self: TreeNodeBinding) -> str
        Set: NavigateUrlField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def PopulateOnDemand(self) -> bool:
        """
        Get: PopulateOnDemand(self: TreeNodeBinding) -> bool
        Set: PopulateOnDemand(self: TreeNodeBinding) = value
        """
        ...

    @property
    def SelectAction(self): # -> TreeNodeSelectAction
        """
        Get: SelectAction(self: TreeNodeBinding) -> TreeNodeSelectAction
        Set: SelectAction(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ShowCheckBox(self) -> Nullable:
        """
        Get: ShowCheckBox(self: TreeNodeBinding) -> Nullable[bool]
        Set: ShowCheckBox(self: TreeNodeBinding) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: TreeNodeBinding) -> str
        Set: Target(self: TreeNodeBinding) = value
        """
        ...

    @property
    def TargetField(self) -> str:
        """
        Get: TargetField(self: TreeNodeBinding) -> str
        Set: TargetField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TreeNodeBinding) -> str
        Set: Text(self: TreeNodeBinding) = value
        """
        ...

    @property
    def TextField(self) -> str:
        """
        Get: TextField(self: TreeNodeBinding) -> str
        Set: TextField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ToolTip(self) -> str:
        """
        Get: ToolTip(self: TreeNodeBinding) -> str
        Set: ToolTip(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ToolTipField(self) -> str:
        """
        Get: ToolTipField(self: TreeNodeBinding) -> str
        Set: ToolTipField(self: TreeNodeBinding) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: TreeNodeBinding) -> str
        Set: Value(self: TreeNodeBinding) = value
        """
        ...

    @property
    def ValueField(self) -> str:
        """
        Get: ValueField(self: TreeNodeBinding) -> str
        Set: ValueField(self: TreeNodeBinding) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: TreeNodeBinding) -> str """
        ...


class TreeNodeBindingCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, binding:TreeNodeBinding) -> int:
        """ Add(self: TreeNodeBindingCollection, binding: TreeNodeBinding) -> int """
        ...

    def Contains(self, binding:TreeNodeBinding) -> bool:
        """ Contains(self: TreeNodeBindingCollection, binding: TreeNodeBinding) -> bool """
        ...

    def IndexOf(self, binding:TreeNodeBinding) -> int:
        """ IndexOf(self: TreeNodeBindingCollection, binding: TreeNodeBinding) -> int """
        ...

    def Insert(self, index:int, binding:TreeNodeBinding): # -> 
        """ Insert(self: TreeNodeBindingCollection, index: int, binding: TreeNodeBinding) """
        ...

    def Remove(self, binding:TreeNodeBinding): # -> 
        """ Remove(self: TreeNodeBindingCollection, binding: TreeNodeBinding) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TreeNodeBindingCollection, index: int) """
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


class TreeNodeCollection(IStateManager, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    TreeNodeCollection()
    TreeNodeCollection(owner: TreeNode)
    """
    def Add(self, child:TreeNode): # -> 
        """ Add(self: TreeNodeCollection, child: TreeNode) """
        ...

    def AddAt(self, index:int, child:TreeNode): # -> 
        """ AddAt(self: TreeNodeCollection, index: int, child: TreeNode) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TreeNodeCollection) """
        ...

    def Contains(self, c:TreeNode) -> bool:
        """ Contains(self: TreeNodeCollection, c: TreeNode) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TreeNodeCollection) -> IEnumerator """
        ...

    def IndexOf(self, value:TreeNode) -> int:
        """ IndexOf(self: TreeNodeCollection, value: TreeNode) -> int """
        ...

    def Remove(self, value:TreeNode): # -> 
        """ Remove(self: TreeNodeCollection, value: TreeNode) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TreeNodeCollection, index: int) """
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


class TreeNodeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TreeNodeEventArgs(node: TreeNode) """
    @property
    def Node(self) -> TreeNode:
        """ Get: Node(self: TreeNodeEventArgs) -> TreeNode """
        ...


    def __new__(cls, node:TreeNode) -> Self:
        """ __new__(cls: type, node: TreeNode) """
        ...


class TreeNodeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TreeNodeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TreeNodeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TreeNodeEventHandler, sender: object, e: TreeNodeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TreeNodeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TreeNodeEventArgs): # -> 
        """ Invoke(self: TreeNodeEventHandler, sender: object, e: TreeNodeEventArgs) """
        ...


class TreeNodeSelectAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TreeNodeSelectAction, values: Expand (1), None (3), Select (0), SelectExpand (2) """
    Expand: TreeNodeSelectAction = ...
    Select: TreeNodeSelectAction = ...
    SelectExpand: TreeNodeSelectAction = ...
    value__ = ...


class TreeNodeStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """
    TreeNodeStyle()
    TreeNodeStyle(bag: StateBag)
    """
    @property
    def ChildNodesPadding(self): # -> Unit
        """
        Get: ChildNodesPadding(self: TreeNodeStyle) -> Unit
        Set: ChildNodesPadding(self: TreeNodeStyle) = value
        """
        ...

    @property
    def HorizontalPadding(self): # -> Unit
        """
        Get: HorizontalPadding(self: TreeNodeStyle) -> Unit
        Set: HorizontalPadding(self: TreeNodeStyle) = value
        """
        ...

    @property
    def ImageUrl(self) -> str:
        """
        Get: ImageUrl(self: TreeNodeStyle) -> str
        Set: ImageUrl(self: TreeNodeStyle) = value
        """
        ...

    @property
    def NodeSpacing(self): # -> Unit
        """
        Get: NodeSpacing(self: TreeNodeStyle) -> Unit
        Set: NodeSpacing(self: TreeNodeStyle) = value
        """
        ...

    @property
    def VerticalPadding(self): # -> Unit
        """
        Get: VerticalPadding(self: TreeNodeStyle) -> Unit
        Set: VerticalPadding(self: TreeNodeStyle) = value
        """
        ...



class TreeNodeStyleCollection(StateManagedCollection): # skipped bases: <type 'IStateManager'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, style:TreeNodeStyle) -> int:
        """ Add(self: TreeNodeStyleCollection, style: TreeNodeStyle) -> int """
        ...

    def Contains(self, style:TreeNodeStyle) -> bool:
        """ Contains(self: TreeNodeStyleCollection, style: TreeNodeStyle) -> bool """
        ...

    def IndexOf(self, style:TreeNodeStyle) -> int:
        """ IndexOf(self: TreeNodeStyleCollection, style: TreeNodeStyle) -> int """
        ...

    def Insert(self, index:int, style:TreeNodeStyle): # -> 
        """ Insert(self: TreeNodeStyleCollection, index: int, style: TreeNodeStyle) """
        ...

    def Remove(self, style:TreeNodeStyle): # -> 
        """ Remove(self: TreeNodeStyleCollection, style: TreeNodeStyle) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TreeNodeStyleCollection, index: int) """
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


class TreeNodeTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TreeNodeTypes, values: All (7), Leaf (4), None (0), Parent (2), Root (1) """
    All: TreeNodeTypes = ...
    Leaf: TreeNodeTypes = ...
    Parent: TreeNodeTypes = ...
    Root: TreeNodeTypes = ...
    value__ = ...


class TreeView(IPostBackDataHandler, HierarchicalDataBoundControl, IPostBackEventHandler, ICallbackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ TreeView() """
    @property
    def AutoGenerateDataBindings(self) -> bool:
        """
        Get: AutoGenerateDataBindings(self: TreeView) -> bool
        Set: AutoGenerateDataBindings(self: TreeView) = value
        """
        ...

    @property
    def CheckedNodes(self) -> TreeNodeCollection:
        """ Get: CheckedNodes(self: TreeView) -> TreeNodeCollection """
        ...

    @property
    def CollapseImageToolTip(self) -> str:
        """
        Get: CollapseImageToolTip(self: TreeView) -> str
        Set: CollapseImageToolTip(self: TreeView) = value
        """
        ...

    @property
    def CollapseImageUrl(self) -> str:
        """
        Get: CollapseImageUrl(self: TreeView) -> str
        Set: CollapseImageUrl(self: TreeView) = value
        """
        ...

    @property
    def EnableClientScript(self) -> bool:
        """
        Get: EnableClientScript(self: TreeView) -> bool
        Set: EnableClientScript(self: TreeView) = value
        """
        ...

    @property
    def ExpandDepth(self) -> int:
        """
        Get: ExpandDepth(self: TreeView) -> int
        Set: ExpandDepth(self: TreeView) = value
        """
        ...

    @property
    def ExpandImageToolTip(self) -> str:
        """
        Get: ExpandImageToolTip(self: TreeView) -> str
        Set: ExpandImageToolTip(self: TreeView) = value
        """
        ...

    @property
    def ExpandImageUrl(self) -> str:
        """
        Get: ExpandImageUrl(self: TreeView) -> str
        Set: ExpandImageUrl(self: TreeView) = value
        """
        ...

    @property
    def HoverNodeStyle(self) -> Style:
        """ Get: HoverNodeStyle(self: TreeView) -> Style """
        ...

    @property
    def ImageSet(self): # -> TreeViewImageSet
        """
        Get: ImageSet(self: TreeView) -> TreeViewImageSet
        Set: ImageSet(self: TreeView) = value
        """
        ...

    @property
    def LeafNodeStyle(self) -> TreeNodeStyle:
        """ Get: LeafNodeStyle(self: TreeView) -> TreeNodeStyle """
        ...

    @property
    def LevelStyles(self) -> TreeNodeStyleCollection:
        """ Get: LevelStyles(self: TreeView) -> TreeNodeStyleCollection """
        ...

    @property
    def LineImagesFolder(self) -> str:
        """
        Get: LineImagesFolder(self: TreeView) -> str
        Set: LineImagesFolder(self: TreeView) = value
        """
        ...

    @property
    def MaxDataBindDepth(self) -> int:
        """
        Get: MaxDataBindDepth(self: TreeView) -> int
        Set: MaxDataBindDepth(self: TreeView) = value
        """
        ...

    @property
    def NodeIndent(self) -> int:
        """
        Get: NodeIndent(self: TreeView) -> int
        Set: NodeIndent(self: TreeView) = value
        """
        ...

    @property
    def Nodes(self) -> TreeNodeCollection:
        """ Get: Nodes(self: TreeView) -> TreeNodeCollection """
        ...

    @property
    def NodeStyle(self) -> TreeNodeStyle:
        """ Get: NodeStyle(self: TreeView) -> TreeNodeStyle """
        ...

    @property
    def NodeWrap(self) -> bool:
        """
        Get: NodeWrap(self: TreeView) -> bool
        Set: NodeWrap(self: TreeView) = value
        """
        ...

    @property
    def NoExpandImageUrl(self) -> str:
        """
        Get: NoExpandImageUrl(self: TreeView) -> str
        Set: NoExpandImageUrl(self: TreeView) = value
        """
        ...

    @property
    def ParentNodeStyle(self) -> TreeNodeStyle:
        """ Get: ParentNodeStyle(self: TreeView) -> TreeNodeStyle """
        ...

    @property
    def PathSeparator(self) -> Char:
        """
        Get: PathSeparator(self: TreeView) -> Char
        Set: PathSeparator(self: TreeView) = value
        """
        ...

    @property
    def PopulateNodesFromClient(self) -> bool:
        """
        Get: PopulateNodesFromClient(self: TreeView) -> bool
        Set: PopulateNodesFromClient(self: TreeView) = value
        """
        ...

    @property
    def RootNodeStyle(self) -> TreeNodeStyle:
        """ Get: RootNodeStyle(self: TreeView) -> TreeNodeStyle """
        ...

    @property
    def SelectedNode(self) -> TreeNode:
        """ Get: SelectedNode(self: TreeView) -> TreeNode """
        ...

    @property
    def SelectedNodeStyle(self) -> TreeNodeStyle:
        """ Get: SelectedNodeStyle(self: TreeView) -> TreeNodeStyle """
        ...

    @property
    def SelectedValue(self) -> str:
        """ Get: SelectedValue(self: TreeView) -> str """
        ...

    @property
    def ShowCheckBoxes(self) -> TreeNodeTypes:
        """
        Get: ShowCheckBoxes(self: TreeView) -> TreeNodeTypes
        Set: ShowCheckBoxes(self: TreeView) = value
        """
        ...

    @property
    def ShowExpandCollapse(self) -> bool:
        """
        Get: ShowExpandCollapse(self: TreeView) -> bool
        Set: ShowExpandCollapse(self: TreeView) = value
        """
        ...

    @property
    def ShowLines(self) -> bool:
        """
        Get: ShowLines(self: TreeView) -> bool
        Set: ShowLines(self: TreeView) = value
        """
        ...

    @property
    def SkipLinkText(self) -> str:
        """
        Get: SkipLinkText(self: TreeView) -> str
        Set: SkipLinkText(self: TreeView) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: TreeView) -> str
        Set: Target(self: TreeView) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: TreeView) -> bool
        Set: Visible(self: TreeView) = value
        """
        ...


    def CollapseAll(self): # -> 
        """ CollapseAll(self: TreeView) """
        ...

    def CreateNode(self, *args): #cannot find CLR method
        """ CreateNode(self: TreeView) -> TreeNode """
        ...

    def ExpandAll(self): # -> 
        """ ExpandAll(self: TreeView) """
        ...

    def FindNode(self, valuePath:str) -> TreeNode:
        """ FindNode(self: TreeView, valuePath: str) -> TreeNode """
        ...

    def OnSelectedNodeChanged(self, *args): #cannot find CLR method
        """ OnSelectedNodeChanged(self: TreeView, e: EventArgs) """
        ...

    def OnTreeNodeCheckChanged(self, *args): #cannot find CLR method
        """ OnTreeNodeCheckChanged(self: TreeView, e: TreeNodeEventArgs) """
        ...

    def OnTreeNodeCollapsed(self, *args): #cannot find CLR method
        """ OnTreeNodeCollapsed(self: TreeView, e: TreeNodeEventArgs) """
        ...

    def OnTreeNodeDataBound(self, *args): #cannot find CLR method
        """ OnTreeNodeDataBound(self: TreeView, e: TreeNodeEventArgs) """
        ...

    def OnTreeNodeExpanded(self, *args): #cannot find CLR method
        """ OnTreeNodeExpanded(self: TreeView, e: TreeNodeEventArgs) """
        ...

    def OnTreeNodePopulate(self, *args): #cannot find CLR method
        """ OnTreeNodePopulate(self: TreeView, e: TreeNodeEventArgs) """
        ...

    def RenderBeginTag(self, writer:HtmlTextWriter): # -> 
        """ RenderBeginTag(self: TreeView, writer: HtmlTextWriter) """
        ...

    def RenderEndTag(self, writer:HtmlTextWriter): # -> 
        """ RenderEndTag(self: TreeView, writer: HtmlTextWriter) """
        ...

    def SetNodeDataBound(self, *args): #cannot find CLR method
        """ SetNodeDataBound(self: TreeView, node: TreeNode, dataBound: bool) """
        ...

    def SetNodeDataItem(self, *args): #cannot find CLR method
        """ SetNodeDataItem(self: TreeView, node: TreeNode, dataItem: object) """
        ...

    def SetNodeDataPath(self, *args): #cannot find CLR method
        """ SetNodeDataPath(self: TreeView, node: TreeNode, dataPath: str) """
        ...

    SelectedNodeChanged = ...
    TreeNodeCheckChanged = ...
    TreeNodeCollapsed = ...
    TreeNodeDataBound = ...
    TreeNodeExpanded = ...
    TreeNodePopulate = ...


class TreeViewImageSet(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TreeViewImageSet, values: Arrows (10), BulletedList (6), BulletedList2 (7), BulletedList3 (8), BulletedList4 (9), Contacts (12), Custom (0), Events (14), Faq (15), Inbox (13), Msdn (2), News (11), Simple (4), Simple2 (5), WindowsHelp (3), XPFileExplorer (1) """
    Arrows: TreeViewImageSet = ...
    BulletedList: TreeViewImageSet = ...
    BulletedList2: TreeViewImageSet = ...
    BulletedList3: TreeViewImageSet = ...
    BulletedList4: TreeViewImageSet = ...
    Contacts: TreeViewImageSet = ...
    Custom: TreeViewImageSet = ...
    Events: TreeViewImageSet = ...
    Faq: TreeViewImageSet = ...
    Inbox: TreeViewImageSet = ...
    Msdn: TreeViewImageSet = ...
    News: TreeViewImageSet = ...
    Simple: TreeViewImageSet = ...
    Simple2: TreeViewImageSet = ...
    value__ = ...
    WindowsHelp: TreeViewImageSet = ...
    XPFileExplorer: TreeViewImageSet = ...


class Unit: # skipped bases: <type 'object'>, <type 'object'>
    """
    Unit(value: int)
    Unit(value: float)
    Unit(value: float, type: UnitType)
    Unit(value: str)
    Unit(value: str, culture: CultureInfo)
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Unit) -> bool """
        ...

    @property
    def Type(self): # -> UnitType
        """ Get: Type(self: Unit) -> UnitType """
        ...

    @property
    def Value(self) -> float:
        """ Get: Value(self: Unit) -> float """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Unit, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Unit) -> int """
        ...

    @staticmethod
    def Parse(s:str, culture:CultureInfo = ...) -> Unit:
        """
        Parse(s: str) -> Unit
        Parse(s: str, culture: CultureInfo) -> Unit
        """
        ...

    @staticmethod
    def Percentage(n:float) -> Unit:
        """ Percentage(n: float) -> Unit """
        ...

    @staticmethod
    def Pixel(n:int) -> Unit:
        """ Pixel(n: int) -> Unit """
        ...

    @staticmethod
    def Point(n:int) -> Unit:
        """ Point(n: int) -> Unit """
        ...

    def ToString(self, *__args:CultureInfo) -> str:
        """
        ToString(self: Unit) -> str
        ToString(self: Unit, culture: CultureInfo) -> str
        ToString(self: Unit, formatProvider: IFormatProvider) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: Unit = ...


class UnitConverter(TypeConverter): # skipped bases: <type 'object'>
    """ UnitConverter() """
    pass

class UnitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnitType, values: Cm (6), Em (8), Ex (9), Inch (4), Mm (5), Percentage (7), Pica (3), Pixel (1), Point (2) """
    Cm: UnitType = ...
    Em: UnitType = ...
    Ex: UnitType = ...
    Inch: UnitType = ...
    Mm: UnitType = ...
    Percentage: UnitType = ...
    Pica: UnitType = ...
    Pixel: UnitType = ...
    Point: UnitType = ...
    value__ = ...


class ValidatedControlConverter(ControlIDConverter): # skipped bases: <type 'object'>
    """ ValidatedControlConverter() """
    pass

class ValidationCompareOperator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidationCompareOperator, values: DataTypeCheck (6), Equal (0), GreaterThan (2), GreaterThanEqual (3), LessThan (4), LessThanEqual (5), NotEqual (1) """
    DataTypeCheck: ValidationCompareOperator = ...
    Equal: ValidationCompareOperator = ...
    GreaterThan: ValidationCompareOperator = ...
    GreaterThanEqual: ValidationCompareOperator = ...
    LessThan: ValidationCompareOperator = ...
    LessThanEqual: ValidationCompareOperator = ...
    NotEqual: ValidationCompareOperator = ...
    value__ = ...


class ValidationDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidationDataType, values: Currency (4), Date (3), Double (2), Integer (1), String (0) """
    Currency: ValidationDataType = ...
    Date: ValidationDataType = ...
    Double: ValidationDataType = ...
    Integer: ValidationDataType = ...
    String: ValidationDataType = ...
    value__ = ...


class ValidationSummary(WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ ValidationSummary() """
    @property
    def DisplayMode(self): # -> ValidationSummaryDisplayMode
        """
        Get: DisplayMode(self: ValidationSummary) -> ValidationSummaryDisplayMode
        Set: DisplayMode(self: ValidationSummary) = value
        """
        ...

    @property
    def EnableClientScript(self) -> bool:
        """
        Get: EnableClientScript(self: ValidationSummary) -> bool
        Set: EnableClientScript(self: ValidationSummary) = value
        """
        ...

    @property
    def HeaderText(self) -> str:
        """
        Get: HeaderText(self: ValidationSummary) -> str
        Set: HeaderText(self: ValidationSummary) = value
        """
        ...

    @property
    def ShowMessageBox(self) -> bool:
        """
        Get: ShowMessageBox(self: ValidationSummary) -> bool
        Set: ShowMessageBox(self: ValidationSummary) = value
        """
        ...

    @property
    def ShowModelStateErrors(self) -> bool:
        """
        Get: ShowModelStateErrors(self: ValidationSummary) -> bool
        Set: ShowModelStateErrors(self: ValidationSummary) = value
        """
        ...

    @property
    def ShowSummary(self) -> bool:
        """
        Get: ShowSummary(self: ValidationSummary) -> bool
        Set: ShowSummary(self: ValidationSummary) = value
        """
        ...

    @property
    def ShowValidationErrors(self) -> bool:
        """
        Get: ShowValidationErrors(self: ValidationSummary) -> bool
        Set: ShowValidationErrors(self: ValidationSummary) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: ValidationSummary) -> str
        Set: ValidationGroup(self: ValidationSummary) = value
        """
        ...



class ValidationSummaryDisplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidationSummaryDisplayMode, values: BulletList (1), List (0), SingleParagraph (2) """
    BulletList: ValidationSummaryDisplayMode = ...
    List: ValidationSummaryDisplayMode = ...
    SingleParagraph: ValidationSummaryDisplayMode = ...
    value__ = ...


class ValidatorDisplay(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidatorDisplay, values: Dynamic (2), None (0), Static (1) """
    Dynamic: ValidatorDisplay = ...
    Static: ValidatorDisplay = ...
    value__ = ...


class VerticalAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VerticalAlign, values: Bottom (3), Middle (2), NotSet (0), Top (1) """
    Bottom: VerticalAlign = ...
    Middle: VerticalAlign = ...
    NotSet: VerticalAlign = ...
    Top: VerticalAlign = ...
    value__ = ...


class ViewCollection(ControlCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ViewCollection(owner: Control) """
    pass

class WebColorConverter(ColorConverter): # skipped bases: <type 'object'>
    """ WebColorConverter() """
    pass

class WizardNavigationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WizardNavigationEventArgs(currentStepIndex: int, nextStepIndex: int) """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: WizardNavigationEventArgs) -> bool
        Set: Cancel(self: WizardNavigationEventArgs) = value
        """
        ...

    @property
    def CurrentStepIndex(self) -> int:
        """ Get: CurrentStepIndex(self: WizardNavigationEventArgs) -> int """
        ...

    @property
    def NextStepIndex(self) -> int:
        """ Get: NextStepIndex(self: WizardNavigationEventArgs) -> int """
        ...


    def __new__(cls, currentStepIndex:int, nextStepIndex:int) -> Self:
        """ __new__(cls: type, currentStepIndex: int, nextStepIndex: int) """
        ...


class WizardNavigationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WizardNavigationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WizardNavigationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WizardNavigationEventHandler, sender: object, e: WizardNavigationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WizardNavigationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WizardNavigationEventArgs): # -> 
        """ Invoke(self: WizardNavigationEventHandler, sender: object, e: WizardNavigationEventArgs) """
        ...


class WizardStep(WizardStepBase): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ WizardStep() """
    pass

class WizardStepCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: WizardStepCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: WizardStepCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: WizardStepCollection) -> object """
        ...


    def AddAt(self, index:int, wizardStep:WizardStepBase): # -> 
        """ AddAt(self: WizardStepCollection, index: int, wizardStep: WizardStepBase) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WizardStepCollection, array: Array[WizardStepBase], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: WizardStepCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class WizardStepControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ WizardStepControlBuilder() """
    pass

class WizardStepType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WizardStepType, values: Auto (0), Complete (1), Finish (2), Start (3), Step (4) """
    Auto: WizardStepType = ...
    Complete: WizardStepType = ...
    Finish: WizardStepType = ...
    Start: WizardStepType = ...
    Step: WizardStepType = ...
    value__ = ...


class Xml(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Xml() """
    @property
    def Document(self) -> XmlDocument:
        """
        Get: Document(self: Xml) -> XmlDocument
        Set: Document(self: Xml) = value
        """
        ...

    @property
    def DocumentContent(self) -> str:
        """
        Get: DocumentContent(self: Xml) -> str
        Set: DocumentContent(self: Xml) = value
        """
        ...

    @property
    def DocumentSource(self) -> str:
        """
        Get: DocumentSource(self: Xml) -> str
        Set: DocumentSource(self: Xml) = value
        """
        ...

    @property
    def Transform(self) -> XslTransform:
        """
        Get: Transform(self: Xml) -> XslTransform
        Set: Transform(self: Xml) = value
        """
        ...

    @property
    def TransformArgumentList(self) -> XsltArgumentList:
        """
        Get: TransformArgumentList(self: Xml) -> XsltArgumentList
        Set: TransformArgumentList(self: Xml) = value
        """
        ...

    @property
    def TransformSource(self) -> str:
        """
        Get: TransformSource(self: Xml) -> str
        Set: TransformSource(self: Xml) = value
        """
        ...

    @property
    def XPathNavigator(self) -> XPathNavigator:
        """
        Get: XPathNavigator(self: Xml) -> XPathNavigator
        Set: XPathNavigator(self: Xml) = value
        """
        ...



class XmlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ XmlBuilder() """
    pass

class XmlDataSource(IDataSource, IListSource, HierarchicalDataSourceControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IHierarchicalDataSource'>, <type 'object'>
    """ XmlDataSource() """
    @property
    def CacheDuration(self) -> int:
        """
        Get: CacheDuration(self: XmlDataSource) -> int
        Set: CacheDuration(self: XmlDataSource) = value
        """
        ...

    @property
    def CacheExpirationPolicy(self) -> DataSourceCacheExpiry:
        """
        Get: CacheExpirationPolicy(self: XmlDataSource) -> DataSourceCacheExpiry
        Set: CacheExpirationPolicy(self: XmlDataSource) = value
        """
        ...

    @property
    def CacheKeyContext(self) -> str:
        """
        Get: CacheKeyContext(self: XmlDataSource) -> str
        Set: CacheKeyContext(self: XmlDataSource) = value
        """
        ...

    @property
    def CacheKeyDependency(self) -> str:
        """
        Get: CacheKeyDependency(self: XmlDataSource) -> str
        Set: CacheKeyDependency(self: XmlDataSource) = value
        """
        ...

    @property
    def Data(self) -> str:
        """
        Get: Data(self: XmlDataSource) -> str
        Set: Data(self: XmlDataSource) = value
        """
        ...

    @property
    def DataFile(self) -> str:
        """
        Get: DataFile(self: XmlDataSource) -> str
        Set: DataFile(self: XmlDataSource) = value
        """
        ...

    @property
    def EnableCaching(self) -> bool:
        """
        Get: EnableCaching(self: XmlDataSource) -> bool
        Set: EnableCaching(self: XmlDataSource) = value
        """
        ...

    @property
    def Transform(self) -> str:
        """
        Get: Transform(self: XmlDataSource) -> str
        Set: Transform(self: XmlDataSource) = value
        """
        ...

    @property
    def TransformArgumentList(self) -> XsltArgumentList:
        """
        Get: TransformArgumentList(self: XmlDataSource) -> XsltArgumentList
        Set: TransformArgumentList(self: XmlDataSource) = value
        """
        ...

    @property
    def TransformFile(self) -> str:
        """
        Get: TransformFile(self: XmlDataSource) -> str
        Set: TransformFile(self: XmlDataSource) = value
        """
        ...

    @property
    def XPath(self) -> str:
        """
        Get: XPath(self: XmlDataSource) -> str
        Set: XPath(self: XmlDataSource) = value
        """
        ...


    def GetXmlDocument(self) -> XmlDocument:
        """ GetXmlDocument(self: XmlDataSource) -> XmlDocument """
        ...

    def OnTransforming(self, *args): #cannot find CLR method
        """ OnTransforming(self: XmlDataSource, e: EventArgs) """
        ...

    def Save(self): # -> 
        """ Save(self: XmlDataSource) """
        ...

    Transforming = ...


class XmlDataSourceView(DataSourceView): # skipped bases: <type 'object'>
    """ XmlDataSourceView(owner: XmlDataSource, name: str) """
    pass

class XmlHierarchicalDataSourceView(HierarchicalDataSourceView): # skipped bases: <type 'object'>
    """ no doc """
    pass

# variables with complex values

