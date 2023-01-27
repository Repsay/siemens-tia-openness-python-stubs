# encoding: utf-8
# module System.Web.UI.Design calls itself Design
# from System.Web.Extensions.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Word import Style

from Microsoft.SqlServer.Management.Smo import ViewEvent

from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, IDisposable, IServiceProvider, MulticastDelegate, Type)

from System.Collections import (ArrayList, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList, ReadOnlyCollectionBase)

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import (IComponent, IListSource, 
    ITypeDescriptorContext, PropertyDescriptor, PropertyDescriptorCollection, 
    StringConverter, TypeConverter)

from System.ComponentModel.Design import (ComponentChangedEventArgs, 
    ComponentChangingEventArgs, DesignerVerb, IDesigner, IDesignerFilter, 
    IDesignerHost, IRootDesigner)

from System.Configuration import Configuration

from System.Data import DataTable

from System.Drawing import Rectangle

from System.Drawing.Design import ToolboxItem, UITypeEditor

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Reflection import Assembly

from System.Resources import IResourceWriter

from System.Web.UI import (Control, DataBindingCollection, 
    ExpressionBindingCollection, IHierarchicalEnumerable, ITemplate, 
    ScriptManager, ServiceReference)

from System.Windows.Forms.Design import ControlDesigner

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point, Size

"""The following names are not found in the module: (BoundEvent, 
    CollectionEditor, ComponentDesigner, DesignTimeResourceProviderFactory, 
    DesignerActionListCollection, DesignerActionService, DesignerAutoFormat, 
    DesignerAutoFormatCollection, DesignerAutoFormatStyle, 
    DesignerDataSourceView, DesignerRegionCollection, EditableDesignerRegion, 
    ExpressionEditorSheet, IControlDesigner, IDataSourceFieldSchema, 
    IDataSourceSchema, IDataSourceViewSchema, IDesignTimeResourceWriter, 
    IHierarchicalDataSourceDesigner, IHtmlControlDesignerBehavior, 
    IResourceProvider, StandardValuesCollection, TemplateDefinition, 
    TemplateEditingVerb, TemplateGroupCollection, TemplatedControlDesigner, 
    TransactedChangeCallback, UrlBuilderOptions, VerticalAlign, ViewFlags, 
    ViewRendering, field#)
"""

# no functions
# classes

class ExpressionEditor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExpressionPrefix(self) -> str:
        """ Get: ExpressionPrefix(self: ExpressionEditor) -> str """
        ...


    def EvaluateExpression(self, expression:str, parseTimeData:object, propertyType:Type, serviceProvider:IServiceProvider) -> object:
        """ EvaluateExpression(self: ExpressionEditor, expression: str, parseTimeData: object, propertyType: Type, serviceProvider: IServiceProvider) -> object """
        ...

    @staticmethod
    def GetExpressionEditor(*__args) -> ExpressionEditor:
        """
        GetExpressionEditor(expressionPrefix: str, serviceProvider: IServiceProvider) -> ExpressionEditor
        GetExpressionEditor(expressionBuilderType: Type, serviceProvider: IServiceProvider) -> ExpressionEditor
        """
        ...

    def GetExpressionEditorSheet(self, expression:str, serviceProvider:IServiceProvider): # -> ExpressionEditorSheet
        """ GetExpressionEditorSheet(self: ExpressionEditor, expression: str, serviceProvider: IServiceProvider) -> ExpressionEditorSheet """
        ...


class AppSettingsExpressionEditor(ExpressionEditor): # skipped bases: <type 'object'>
    """ AppSettingsExpressionEditor() """
    pass

class AsyncPostBackTriggerControlIDConverter(StringConverter): # skipped bases: <type 'object'>
    """ AsyncPostBackTriggerControlIDConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: AsyncPostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: AsyncPostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: AsyncPostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...


class AsyncPostBackTriggerEventNameConverter(StringConverter): # skipped bases: <type 'object'>
    """ AsyncPostBackTriggerEventNameConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: AsyncPostBackTriggerEventNameConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: AsyncPostBackTriggerEventNameConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: AsyncPostBackTriggerEventNameConverter, context: ITypeDescriptorContext) -> bool """
        ...


class DataBindingHandler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DataBindControl(self, designerHost:IDesignerHost, control:Control): # -> 
        """ DataBindControl(self: DataBindingHandler, designerHost: IDesignerHost, control: Control) """
        ...


class CalendarDataBindingHandler(DataBindingHandler): # skipped bases: <type 'object'>
    """ CalendarDataBindingHandler() """
    pass

class ClientScriptItem: # skipped bases: <type 'object'>, <type 'object'>
    """ ClientScriptItem(text: str, source: str, language: str, type: str, id: str) """
    @property
    def Id(self) -> str:
        """ Get: Id(self: ClientScriptItem) -> str """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: ClientScriptItem) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: ClientScriptItem) -> str """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ClientScriptItem) -> str """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: ClientScriptItem) -> str """
        ...



class ClientScriptItemCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ClientScriptItemCollection(clientScriptItems: Array[ClientScriptItem]) """
    def __new__(cls, clientScriptItems:Array) -> Self:
        """ __new__(cls: type, clientScriptItems: Array[ClientScriptItem]) """
        ...


class CollectionEditorBase(CollectionEditor): # skipped bases: <type 'object'>
    """ CollectionEditorBase(type: Type) """
    pass

class ColorBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BuildColor(component:IComponent, owner:Control, initialColor:str) -> str:
        """ BuildColor(component: IComponent, owner: Control, initialColor: str) -> str """
        ...


class ConnectionStringEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ConnectionStringEditor() """
    def GetProviderName(self, *args): #cannot find CLR method
        """ GetProviderName(self: ConnectionStringEditor, instance: object) -> str """
        ...

    def SetProviderName(self, *args): #cannot find CLR method
        """ SetProviderName(self: ConnectionStringEditor, instance: object, connection: DesignerDataConnection) """
        ...


class ConnectionStringsExpressionEditor(ExpressionEditor): # skipped bases: <type 'object'>
    """ ConnectionStringsExpressionEditor() """
    pass

class HtmlControlDesigner(ComponentDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HtmlControlDesigner() """
    @property
    def Behavior(self): # -> IHtmlControlDesignerBehavior
        """
        Get: Behavior(self: HtmlControlDesigner) -> IHtmlControlDesignerBehavior
        Set: Behavior(self: HtmlControlDesigner) = value
        """
        ...

    @property
    def DataBindings(self) -> DataBindingCollection:
        """ Get: DataBindings(self: HtmlControlDesigner) -> DataBindingCollection """
        ...

    @property
    def DesignTimeElement(self):
        ...

    @property
    def Expressions(self) -> ExpressionBindingCollection:
        """ Get: Expressions(self: HtmlControlDesigner) -> ExpressionBindingCollection """
        ...

    @property
    def ShouldCodeSerialize(self) -> bool:
        """
        Get: ShouldCodeSerialize(self: HtmlControlDesigner) -> bool
        Set: ShouldCodeSerialize(self: HtmlControlDesigner) = value
        """
        ...


    def OnBehaviorAttached(self, *args): #cannot find CLR method
        """ OnBehaviorAttached(self: HtmlControlDesigner) """
        ...

    def OnBehaviorDetaching(self, *args): #cannot find CLR method
        """ OnBehaviorDetaching(self: HtmlControlDesigner) """
        ...

    def OnBindingsCollectionChanged(self, *args): #cannot find CLR method
        """ OnBindingsCollectionChanged(self: HtmlControlDesigner, propName: str) """
        ...

    def OnSetParent(self): # -> 
        """ OnSetParent(self: HtmlControlDesigner) """
        ...


class ControlDesigner(HtmlControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ControlDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: ControlDesigner) -> DesignerActionListCollection """
        ...

    @property
    def AllowResize(self) -> bool:
        """ Get: AllowResize(self: ControlDesigner) -> bool """
        ...

    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: ControlDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def DataBindingsEnabled(self):
        ...

    @property
    def DesignerState(self):
        ...

    @property
    def DesignTimeElementView(self):
        ...

    @property
    def DesignTimeHtmlRequiresLoadComplete(self) -> bool:
        """ Get: DesignTimeHtmlRequiresLoadComplete(self: ControlDesigner) -> bool """
        ...

    @property
    def HidePropertiesInTemplateMode(self):
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: ControlDesigner) -> str
        Set: ID(self: ControlDesigner) = value
        """
        ...

    @property
    def InTemplateMode(self):
        ...

    @property
    def IsDirty(self) -> bool:
        """
        Get: IsDirty(self: ControlDesigner) -> bool
        Set: IsDirty(self: ControlDesigner) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: ControlDesigner) -> bool
        Set: ReadOnly(self: ControlDesigner) = value
        """
        ...

    @property
    def RootDesigner(self):
        ...

    @property
    def Tag(self):
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: ControlDesigner) -> TemplateGroupCollection """
        ...

    @property
    def UsePreviewControl(self):
        ...

    @property
    def ViewControl(self) -> Control:
        """
        Get: ViewControl(self: ControlDesigner) -> Control
        Set: ViewControl(self: ControlDesigner) = value
        """
        ...

    @property
    def ViewControlCreated(self) -> bool:
        """
        Get: ViewControlCreated(self: ControlDesigner) -> bool
        Set: ViewControlCreated(self: ControlDesigner) = value
        """
        ...

    @property
    def Visible(self):
        ...


    def CreateErrorDesignTimeHtml(self, *args): #cannot find CLR method
        """
        CreateErrorDesignTimeHtml(self: ControlDesigner, errorMessage: str) -> str
        CreateErrorDesignTimeHtml(self: ControlDesigner, errorMessage: str, e: Exception) -> str
        """
        ...

    def CreatePlaceHolderDesignTimeHtml(self, *args): #cannot find CLR method
        """
        CreatePlaceHolderDesignTimeHtml(self: ControlDesigner) -> str
        CreatePlaceHolderDesignTimeHtml(self: ControlDesigner, instruction: str) -> str
        """
        ...

    def CreateViewControl(self, *args): #cannot find CLR method
        """ CreateViewControl(self: ControlDesigner) -> Control """
        ...

    def GetBounds(self) -> Rectangle:
        """ GetBounds(self: ControlDesigner) -> Rectangle """
        ...

    def GetDesignTimeHtml(self, regions = ...) -> str: # Not found arg types: {'regions': 'DesignerRegionCollection'}
        """
        GetDesignTimeHtml(self: ControlDesigner, regions: DesignerRegionCollection) -> str
        GetDesignTimeHtml(self: ControlDesigner) -> str
        """
        ...

    @staticmethod
    def GetDesignTimeResourceProviderFactory(serviceProvider:IServiceProvider): # -> DesignTimeResourceProviderFactory
        """ GetDesignTimeResourceProviderFactory(serviceProvider: IServiceProvider) -> DesignTimeResourceProviderFactory """
        ...

    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: ControlDesigner, region: EditableDesignerRegion) -> str """
        ...

    def GetEmptyDesignTimeHtml(self, *args): #cannot find CLR method
        """ GetEmptyDesignTimeHtml(self: ControlDesigner) -> str """
        ...

    def GetErrorDesignTimeHtml(self, *args): #cannot find CLR method
        """ GetErrorDesignTimeHtml(self: ControlDesigner, e: Exception) -> str """
        ...

    def GetPersistenceContent(self) -> str:
        """ GetPersistenceContent(self: ControlDesigner) -> str """
        ...

    def GetPersistInnerHtml(self) -> str:
        """ GetPersistInnerHtml(self: ControlDesigner) -> str """
        ...

    @staticmethod
    def GetViewRendering(*__args:ControlDesigner): # -> ViewRendering
        """
        GetViewRendering(designer: ControlDesigner) -> ViewRendering
        GetViewRendering(control: Control) -> ViewRendering
        GetViewRendering(self: ControlDesigner) -> ViewRendering
        """
        ...

    def Invalidate(self, rectangle:Rectangle = ...): # -> 
        """ Invalidate(self: ControlDesigner)Invalidate(self: ControlDesigner, rectangle: Rectangle) """
        ...

    @staticmethod
    def InvokeTransactedChange(*__args): # -> 
        """ InvokeTransactedChange(component: IComponent, callback: TransactedChangeCallback, context: object, description: str)InvokeTransactedChange(component: IComponent, callback: TransactedChangeCallback, context: object, description: str, member: MemberDescriptor)InvokeTransactedChange(serviceProvider: IServiceProvider, component: IComponent, callback: TransactedChangeCallback, context: object, description: str, member: MemberDescriptor) """
        ...

    def IsPropertyBound(self, propName:str) -> bool:
        """ IsPropertyBound(self: ControlDesigner, propName: str) -> bool """
        ...

    def Localize(self, resourceWriter): # ->  # Not found arg types: {'resourceWriter': 'IDesignTimeResourceWriter'}
        """ Localize(self: ControlDesigner, resourceWriter: IDesignTimeResourceWriter) """
        ...

    def OnAutoFormatApplied(self, appliedAutoFormat): # ->  # Not found arg types: {'appliedAutoFormat': 'DesignerAutoFormat'}
        """ OnAutoFormatApplied(self: ControlDesigner, appliedAutoFormat: DesignerAutoFormat) """
        ...

    def OnClick(self, *args): #cannot find CLR method
        """ OnClick(self: ControlDesigner, e: DesignerRegionMouseEventArgs) """
        ...

    def OnComponentChanged(self, sender:object, ce:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: ControlDesigner, sender: object, ce: ComponentChangedEventArgs) """
        ...

    def OnComponentChanging(self, sender:object, ce:ComponentChangingEventArgs): # -> 
        """ OnComponentChanging(self: ControlDesigner, sender: object, ce: ComponentChangingEventArgs) """
        ...

    def OnControlResize(self, *args): #cannot find CLR method
        """ OnControlResize(self: ControlDesigner) """
        ...

    def OnPaint(self, *args): #cannot find CLR method
        """ OnPaint(self: ControlDesigner, e: PaintEventArgs) """
        ...

    def RaiseResizeEvent(self): # -> 
        """ RaiseResizeEvent(self: ControlDesigner) """
        ...

    def RegisterClone(self, original:object, clone:object): # -> 
        """ RegisterClone(self: ControlDesigner, original: object, clone: object) """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: ControlDesigner, region: EditableDesignerRegion, content: str) """
        ...

    def SetRegionContent(self, *args): #cannot find CLR method
        """ SetRegionContent(self: ControlDesigner, region: EditableDesignerRegion, content: str) """
        ...

    def SetViewFlags(self, *args): #cannot find CLR method
        """ SetViewFlags(self: ControlDesigner, viewFlags: ViewFlags, setFlag: bool) """
        ...

    def UpdateDesignTimeHtml(self): # -> 
        """ UpdateDesignTimeHtml(self: ControlDesigner) """
        ...


class ContainerControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ContainerControlDesigner() """
    @property
    def FrameCaption(self) -> str:
        """ Get: FrameCaption(self: ContainerControlDesigner) -> str """
        ...

    @property
    def FrameStyle(self) -> Style:
        """ Get: FrameStyle(self: ContainerControlDesigner) -> Style """
        ...

    @property
    def NoWrap(self):
        ...


    def AddDesignTimeCssAttributes(self, *args): #cannot find CLR method
        """ AddDesignTimeCssAttributes(self: ContainerControlDesigner, styleAttributes: IDictionary) """
        ...

    def GetDesignTimeCssAttributes(self) -> IDictionary:
        """ GetDesignTimeCssAttributes(self: ContainerControlDesigner) -> IDictionary """
        ...


class ContentDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ ContentDefinition(id: str, content: str, designTimeHtml: str) """
    @property
    def ContentPlaceHolderID(self) -> str:
        """ Get: ContentPlaceHolderID(self: ContentDefinition) -> str """
        ...

    @property
    def DefaultContent(self) -> str:
        """ Get: DefaultContent(self: ContentDefinition) -> str """
        ...

    @property
    def DefaultDesignTimeHtml(self) -> str:
        """ Get: DefaultDesignTimeHtml(self: ContentDefinition) -> str """
        ...



class ContentDesignerState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContentDesignerState, values: ShowDefaultContent (0), ShowUserContent (1) """
    ShowDefaultContent: ContentDesignerState = ...
    ShowUserContent: ContentDesignerState = ...
    value__ = ...


class ControlDesignerState: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ControlLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ControlLocation, values: After (1), Before (0), First (2), FirstChild (4), Last (3), LastChild (5) """
    After: ControlLocation = ...
    Before: ControlLocation = ...
    First: ControlLocation = ...
    FirstChild: ControlLocation = ...
    Last: ControlLocation = ...
    LastChild: ControlLocation = ...
    value__ = ...


class ControlParser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ParseControl(designerHost:IDesignerHost, controlText:str, directives:str = ...) -> Control:
        """
        ParseControl(designerHost: IDesignerHost, controlText: str) -> Control
        ParseControl(designerHost: IDesignerHost, controlText: str, directives: str) -> Control
        """
        ...

    @staticmethod
    def ParseControls(designerHost:IDesignerHost, controlText:str) -> Array:
        """ ParseControls(designerHost: IDesignerHost, controlText: str) -> Array[Control] """
        ...

    @staticmethod
    def ParseTemplate(designerHost:IDesignerHost, templateText:str, directives:str = ...) -> ITemplate:
        """
        ParseTemplate(designerHost: IDesignerHost, templateText: str) -> ITemplate
        ParseTemplate(designerHost: IDesignerHost, templateText: str, directives: str) -> ITemplate
        """
        ...


class ControlPersister: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def PersistControl(*__args:Control) -> str:
        """
        PersistControl(control: Control) -> str
        PersistControl(control: Control, host: IDesignerHost) -> str
        PersistControl(sw: TextWriter, control: Control)PersistControl(sw: TextWriter, control: Control, host: IDesignerHost)
        """
        ...

    @staticmethod
    def PersistInnerProperties(*__args) -> str:
        """
        PersistInnerProperties(component: object, host: IDesignerHost) -> str
        PersistInnerProperties(sw: TextWriter, component: object, host: IDesignerHost)
        """
        ...

    @staticmethod
    def PersistTemplate(*__args) -> str:
        """
        PersistTemplate(template: ITemplate, host: IDesignerHost) -> str
        PersistTemplate(writer: TextWriter, template: ITemplate, host: IDesignerHost)
        """
        ...


class DataBindingCollectionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataBindingCollectionConverter() """
    pass

class DataBindingCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DataBindingCollectionEditor() """
    pass

class DataBindingValueUIHandler: # skipped bases: <type 'object'>, <type 'object'>
    """ DataBindingValueUIHandler() """
    def OnGetUIValueItem(self, context:ITypeDescriptorContext, propDesc:PropertyDescriptor, valueUIItemList:ArrayList): # -> 
        """ OnGetUIValueItem(self: DataBindingValueUIHandler, context: ITypeDescriptorContext, propDesc: PropertyDescriptor, valueUIItemList: ArrayList) """
        ...


class DataColumnSelectionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataColumnSelectionConverter() """
    pass

class DataFieldConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataFieldConverter() """
    pass

class DataMemberConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataMemberConverter() """
    pass

class DataSetFieldSchema(IDataSourceFieldSchema): # skipped bases: <type 'object'>
    """ DataSetFieldSchema(column: DataColumn) """
    pass

class DataSetSchema(IDataSourceSchema): # skipped bases: <type 'object'>
    """ DataSetSchema(dataSet: DataSet) """
    pass

class DataSetViewSchema(IDataSourceViewSchema): # skipped bases: <type 'object'>
    """ DataSetViewSchema(dataTable: DataTable) """
    pass

class DataSourceViewSchemaConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataSourceViewSchemaConverter() """
    pass

class DataSourceBooleanViewSchemaConverter(DataSourceViewSchemaConverter): # skipped bases: <type 'object'>
    """ DataSourceBooleanViewSchemaConverter() """
    pass

class DataSourceConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataSourceConverter() """
    def IsValidDataSource(self, *args): #cannot find CLR method
        """ IsValidDataSource(self: DataSourceConverter, component: IComponent) -> bool """
        ...


class IDataSourceDesigner: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanConfigure(self) -> bool:
        """ Get: CanConfigure(self: IDataSourceDesigner) -> bool """
        ...

    @property
    def CanRefreshSchema(self) -> bool:
        """ Get: CanRefreshSchema(self: IDataSourceDesigner) -> bool """
        ...


    def Configure(self): # -> 
        """ Configure(self: IDataSourceDesigner) """
        ...

    def GetView(self, viewName:str): # -> DesignerDataSourceView
        """ GetView(self: IDataSourceDesigner, viewName: str) -> DesignerDataSourceView """
        ...

    def GetViewNames(self) -> Array:
        """ GetViewNames(self: IDataSourceDesigner) -> Array[str] """
        ...

    def RefreshSchema(self, preferSilent:bool): # -> 
        """ RefreshSchema(self: IDataSourceDesigner, preferSilent: bool) """
        ...

    def ResumeDataSourceEvents(self): # -> 
        """ ResumeDataSourceEvents(self: IDataSourceDesigner) """
        ...

    def SuppressDataSourceEvents(self): # -> 
        """ SuppressDataSourceEvents(self: IDataSourceDesigner) """
        ...

    DataSourceChanged = ...
    SchemaRefreshed = ...


class DataSourceDesigner(ControlDesigner, IDataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ DataSourceDesigner() """
    @property
    def SuppressingDataSourceEvents(self):
        ...


    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: DataSourceDesigner, e: EventArgs) """
        ...

    def OnSchemaRefreshed(self, *args): #cannot find CLR method
        """ OnSchemaRefreshed(self: DataSourceDesigner, e: EventArgs) """
        ...

    @staticmethod
    def SchemasEquivalent(schema1, schema2) -> bool: # Not found arg types: {'schema2': 'IDataSourceSchema', 'schema1': 'IDataSourceSchema'}
        """ SchemasEquivalent(schema1: IDataSourceSchema, schema2: IDataSourceSchema) -> bool """
        ...

    @staticmethod
    def ViewSchemasEquivalent(viewSchema1, viewSchema2) -> bool: # Not found arg types: {'viewSchema1': 'IDataSourceViewSchema', 'viewSchema2': 'IDataSourceViewSchema'}
        """ ViewSchemasEquivalent(viewSchema1: IDataSourceViewSchema, viewSchema2: IDataSourceViewSchema) -> bool """
        ...

    DataSourceChanged = ...
    SchemaRefreshed = ...


class DesignerAutoFormat: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerAutoFormat) -> str """
        ...

    @property
    def Style(self): # -> DesignerAutoFormatStyle
        """ Get: Style(self: DesignerAutoFormat) -> DesignerAutoFormatStyle """
        ...


    def Apply(self, control:Control): # -> 
        """ Apply(self: DesignerAutoFormat, control: Control) """
        ...

    def GetPreviewControl(self, runtimeControl:Control) -> Control:
        """ GetPreviewControl(self: DesignerAutoFormat, runtimeControl: Control) -> Control """
        ...

    def ToString(self) -> str:
        """ ToString(self: DesignerAutoFormat) -> str """
        ...


class DesignerAutoFormatCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DesignerAutoFormatCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DesignerAutoFormatCollection) -> int """
        ...

    @property
    def PreviewSize(self) -> Size:
        """ Get: PreviewSize(self: DesignerAutoFormatCollection) -> Size """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: DesignerAutoFormatCollection) -> object """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class DesignerAutoFormatStyle(Style): # skipped bases: <type 'IDisposable'>, <type 'IStateManager'>, <type 'IComponent'>, <type 'object'>
    """ DesignerAutoFormatStyle() """
    @property
    def VerticalAlign(self): # -> VerticalAlign
        """
        Get: VerticalAlign(self: DesignerAutoFormatStyle) -> VerticalAlign
        Set: VerticalAlign(self: DesignerAutoFormatStyle) = value
        """
        ...



class DesignerDataSourceView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanDelete(self) -> bool:
        """ Get: CanDelete(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def CanInsert(self) -> bool:
        """ Get: CanInsert(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def CanPage(self) -> bool:
        """ Get: CanPage(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def CanRetrieveTotalRowCount(self) -> bool:
        """ Get: CanRetrieveTotalRowCount(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def CanSort(self) -> bool:
        """ Get: CanSort(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def CanUpdate(self) -> bool:
        """ Get: CanUpdate(self: DesignerDataSourceView) -> bool """
        ...

    @property
    def DataSourceDesigner(self) -> IDataSourceDesigner:
        """ Get: DataSourceDesigner(self: DesignerDataSourceView) -> IDataSourceDesigner """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerDataSourceView) -> str """
        ...

    @property
    def Schema(self): # -> IDataSourceViewSchema
        """ Get: Schema(self: DesignerDataSourceView) -> IDataSourceViewSchema """
        ...


    def GetDesignTimeData(self, minimumRows, isSampleData) -> Tuple_[IEnumerable, bool]:
        """ GetDesignTimeData(self: DesignerDataSourceView, minimumRows: int) -> (IEnumerable, bool) """
        ...


class DesignerHierarchicalDataSourceView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DataSourceDesigner(self): # -> IHierarchicalDataSourceDesigner
        """ Get: DataSourceDesigner(self: DesignerHierarchicalDataSourceView) -> IHierarchicalDataSourceDesigner """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: DesignerHierarchicalDataSourceView) -> str """
        ...

    @property
    def Schema(self): # -> IDataSourceSchema
        """ Get: Schema(self: DesignerHierarchicalDataSourceView) -> IDataSourceSchema """
        ...


    def GetDesignTimeData(self, isSampleData) -> Tuple_[IHierarchicalEnumerable, bool]:
        """ GetDesignTimeData(self: DesignerHierarchicalDataSourceView) -> (IHierarchicalEnumerable, bool) """
        ...


class DesignerObject(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Designer(self) -> ControlDesigner:
        """ Get: Designer(self: DesignerObject) -> ControlDesigner """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DesignerObject) -> str """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: DesignerObject) -> IDictionary """
        ...



class DesignerRegion(DesignerObject): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """
    DesignerRegion(designer: ControlDesigner, name: str)
    DesignerRegion(designer: ControlDesigner, name: str, selectable: bool)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: DesignerRegion) -> str
        Set: Description(self: DesignerRegion) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: DesignerRegion) -> str
        Set: DisplayName(self: DesignerRegion) = value
        """
        ...

    @property
    def EnsureSize(self) -> bool:
        """
        Get: EnsureSize(self: DesignerRegion) -> bool
        Set: EnsureSize(self: DesignerRegion) = value
        """
        ...

    @property
    def Highlight(self) -> bool:
        """
        Get: Highlight(self: DesignerRegion) -> bool
        Set: Highlight(self: DesignerRegion) = value
        """
        ...

    @property
    def Selectable(self) -> bool:
        """
        Get: Selectable(self: DesignerRegion) -> bool
        Set: Selectable(self: DesignerRegion) = value
        """
        ...

    @property
    def Selected(self) -> bool:
        """
        Get: Selected(self: DesignerRegion) -> bool
        Set: Selected(self: DesignerRegion) = value
        """
        ...

    @property
    def UserData(self) -> object:
        """
        Get: UserData(self: DesignerRegion) -> object
        Set: UserData(self: DesignerRegion) = value
        """
        ...


    def GetBounds(self) -> Rectangle:
        """ GetBounds(self: DesignerRegion) -> Rectangle """
        ...

    DesignerRegionAttributeName: str = ...


class DesignerRegionCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    DesignerRegionCollection()
    DesignerRegionCollection(owner: ControlDesigner)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DesignerRegionCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: DesignerRegionCollection) -> bool """
        ...

    @property
    def Owner(self) -> ControlDesigner:
        """ Get: Owner(self: DesignerRegionCollection) -> ControlDesigner """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: DesignerRegionCollection) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DesignerRegionCollection, array: Array, index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DesignerRegionCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class DesignerRegionMouseEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DesignerRegionMouseEventArgs(region: DesignerRegion, location: Point) """
    @property
    def Location(self) -> Point:
        """ Get: Location(self: DesignerRegionMouseEventArgs) -> Point """
        ...

    @property
    def Region(self) -> DesignerRegion:
        """ Get: Region(self: DesignerRegionMouseEventArgs) -> DesignerRegion """
        ...


    def __new__(cls, region:DesignerRegion, location:Point) -> Self:
        """ __new__(cls: type, region: DesignerRegion, location: Point) """
        ...


class DesignTimeData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateDummyDataBoundDataTable() -> DataTable:
        """ CreateDummyDataBoundDataTable() -> DataTable """
        ...

    @staticmethod
    def CreateDummyDataTable() -> DataTable:
        """ CreateDummyDataTable() -> DataTable """
        ...

    @staticmethod
    def CreateSampleDataTable(referenceData:IEnumerable, useDataBoundData:bool = ...) -> DataTable:
        """
        CreateSampleDataTable(referenceData: IEnumerable) -> DataTable
        CreateSampleDataTable(referenceData: IEnumerable, useDataBoundData: bool) -> DataTable
        """
        ...

    @staticmethod
    def GetDataFields(dataSource:IEnumerable) -> PropertyDescriptorCollection:
        """ GetDataFields(dataSource: IEnumerable) -> PropertyDescriptorCollection """
        ...

    @staticmethod
    def GetDataMember(dataSource:IListSource, dataMember:str) -> IEnumerable:
        """ GetDataMember(dataSource: IListSource, dataMember: str) -> IEnumerable """
        ...

    @staticmethod
    def GetDataMembers(dataSource:object) -> Array:
        """ GetDataMembers(dataSource: object) -> Array[str] """
        ...

    @staticmethod
    def GetDesignTimeDataSource(dataTable:DataTable, minimumRows:int) -> IEnumerable:
        """ GetDesignTimeDataSource(dataTable: DataTable, minimumRows: int) -> IEnumerable """
        ...

    @staticmethod
    def GetSelectedDataSource(component:IComponent, dataSource:str, dataMember:str = ...) -> IEnumerable:
        """
        GetSelectedDataSource(component: IComponent, dataSource: str) -> object
        GetSelectedDataSource(component: IComponent, dataSource: str, dataMember: str) -> IEnumerable
        """
        ...


class DesignTimeResourceProviderFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateDesignTimeGlobalResourceProvider(self, serviceProvider:IServiceProvider, classKey:str): # -> IResourceProvider
        """ CreateDesignTimeGlobalResourceProvider(self: DesignTimeResourceProviderFactory, serviceProvider: IServiceProvider, classKey: str) -> IResourceProvider """
        ...

    def CreateDesignTimeLocalResourceProvider(self, serviceProvider:IServiceProvider): # -> IResourceProvider
        """ CreateDesignTimeLocalResourceProvider(self: DesignTimeResourceProviderFactory, serviceProvider: IServiceProvider) -> IResourceProvider """
        ...

    def CreateDesignTimeLocalResourceWriter(self, serviceProvider:IServiceProvider): # -> IDesignTimeResourceWriter
        """ CreateDesignTimeLocalResourceWriter(self: DesignTimeResourceProviderFactory, serviceProvider: IServiceProvider) -> IDesignTimeResourceWriter """
        ...


class EditableDesignerRegion(DesignerRegion): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """
    EditableDesignerRegion(owner: ControlDesigner, name: str)
    EditableDesignerRegion(owner: ControlDesigner, name: str, serverControlsOnly: bool)
    """
    @property
    def Content(self) -> str:
        """
        Get: Content(self: EditableDesignerRegion) -> str
        Set: Content(self: EditableDesignerRegion) = value
        """
        ...

    @property
    def ServerControlsOnly(self) -> bool:
        """
        Get: ServerControlsOnly(self: EditableDesignerRegion) -> bool
        Set: ServerControlsOnly(self: EditableDesignerRegion) = value
        """
        ...

    @property
    def SupportsDataBinding(self) -> bool:
        """
        Get: SupportsDataBinding(self: EditableDesignerRegion) -> bool
        Set: SupportsDataBinding(self: EditableDesignerRegion) = value
        """
        ...


    def GetChildViewRendering(self, control:Control): # -> ViewRendering
        """ GetChildViewRendering(self: EditableDesignerRegion, control: Control) -> ViewRendering """
        ...


class ExpressionEditorSheet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: ExpressionEditorSheet) -> bool """
        ...

    @property
    def ServiceProvider(self) -> IServiceProvider:
        """ Get: ServiceProvider(self: ExpressionEditorSheet) -> IServiceProvider """
        ...


    def GetExpression(self) -> str:
        """ GetExpression(self: ExpressionEditorSheet) -> str """
        ...


class ExpressionsCollectionConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ExpressionsCollectionConverter() """
    pass

class ExpressionsCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ExpressionsCollectionEditor() """
    pass

class ExtenderControlDesigner(ControlDesigner, IControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ExtenderControlDesigner() """
    pass

class WebControlToolboxItem(ToolboxItem): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """
    WebControlToolboxItem()
    WebControlToolboxItem(type: Type)
    """
    def GetToolAttributeValue(self, host:IDesignerHost, attributeType:Type) -> object:
        """ GetToolAttributeValue(self: WebControlToolboxItem, host: IDesignerHost, attributeType: Type) -> object """
        ...

    def GetToolHtml(self, host:IDesignerHost) -> str:
        """ GetToolHtml(self: WebControlToolboxItem, host: IDesignerHost) -> str """
        ...

    def GetToolType(self, host:IDesignerHost) -> Type:
        """ GetToolType(self: WebControlToolboxItem, host: IDesignerHost) -> Type """
        ...


class ExtenderControlToolboxItem(WebControlToolboxItem): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """
    ExtenderControlToolboxItem()
    ExtenderControlToolboxItem(type: Type)
    """
    def GetTargetControlTypes(self, host:IDesignerHost) -> ReadOnlyCollection:
        """ GetTargetControlTypes(self: ExtenderControlToolboxItem, host: IDesignerHost) -> ReadOnlyCollection[Type] """
        ...


class HierarchicalDataSourceConverter(DataSourceConverter): # skipped bases: <type 'object'>
    """ HierarchicalDataSourceConverter() """
    pass

class IHierarchicalDataSourceDesigner: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanConfigure(self) -> bool:
        """ Get: CanConfigure(self: IHierarchicalDataSourceDesigner) -> bool """
        ...

    @property
    def CanRefreshSchema(self) -> bool:
        """ Get: CanRefreshSchema(self: IHierarchicalDataSourceDesigner) -> bool """
        ...


    def Configure(self): # -> 
        """ Configure(self: IHierarchicalDataSourceDesigner) """
        ...

    def GetView(self, viewPath:str) -> DesignerHierarchicalDataSourceView:
        """ GetView(self: IHierarchicalDataSourceDesigner, viewPath: str) -> DesignerHierarchicalDataSourceView """
        ...

    def RefreshSchema(self, preferSilent:bool): # -> 
        """ RefreshSchema(self: IHierarchicalDataSourceDesigner, preferSilent: bool) """
        ...

    def ResumeDataSourceEvents(self): # -> 
        """ ResumeDataSourceEvents(self: IHierarchicalDataSourceDesigner) """
        ...

    def SuppressDataSourceEvents(self): # -> 
        """ SuppressDataSourceEvents(self: IHierarchicalDataSourceDesigner) """
        ...

    DataSourceChanged = ...
    SchemaRefreshed = ...


class HierarchicalDataSourceDesigner(ControlDesigner, IHierarchicalDataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HierarchicalDataSourceDesigner() """
    @property
    def SuppressingDataSourceEvents(self):
        ...


    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: HierarchicalDataSourceDesigner, e: EventArgs) """
        ...

    def OnSchemaRefreshed(self, *args): #cannot find CLR method
        """ OnSchemaRefreshed(self: HierarchicalDataSourceDesigner, e: EventArgs) """
        ...

    DataSourceChanged = ...
    SchemaRefreshed = ...


class HtmlIntrinsicControlDesigner(HtmlControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HtmlIntrinsicControlDesigner() """
    pass

class HyperLinkDataBindingHandler(DataBindingHandler): # skipped bases: <type 'object'>
    """ HyperLinkDataBindingHandler() """
    pass

class IContentResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentDefinitions(self) -> IDictionary:
        """ Get: ContentDefinitions(self: IContentResolutionService) -> IDictionary """
        ...


    def GetContentDesignerState(self, identifier:str) -> ContentDesignerState:
        """ GetContentDesignerState(self: IContentResolutionService, identifier: str) -> ContentDesignerState """
        ...

    def SetContentDesignerState(self, identifier:str, state:ContentDesignerState): # -> 
        """ SetContentDesignerState(self: IContentResolutionService, identifier: str, state: ContentDesignerState) """
        ...


class IControlDesignerBehavior: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DesignTimeElementView(self) -> object:
        """ Get: DesignTimeElementView(self: IControlDesignerBehavior) -> object """
        ...

    @property
    def DesignTimeHtml(self) -> str:
        """
        Get: DesignTimeHtml(self: IControlDesignerBehavior) -> str
        Set: DesignTimeHtml(self: IControlDesignerBehavior) = value
        """
        ...


    def OnTemplateModeChanged(self): # -> 
        """ OnTemplateModeChanged(self: IControlDesignerBehavior) """
        ...


class IControlDesignerTag: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: IControlDesignerTag) -> bool """
        ...


    def GetAttribute(self, name:str) -> str:
        """ GetAttribute(self: IControlDesignerTag, name: str) -> str """
        ...

    def GetContent(self) -> str:
        """ GetContent(self: IControlDesignerTag) -> str """
        ...

    def GetOuterContent(self) -> str:
        """ GetOuterContent(self: IControlDesignerTag) -> str """
        ...

    def RemoveAttribute(self, name:str): # -> 
        """ RemoveAttribute(self: IControlDesignerTag, name: str) """
        ...

    def SetAttribute(self, name:str, value:str): # -> 
        """ SetAttribute(self: IControlDesignerTag, name: str, value: str) """
        ...

    def SetContent(self, content:str): # -> 
        """ SetContent(self: IControlDesignerTag, content: str) """
        ...

    def SetDirty(self, dirty:bool): # -> 
        """ SetDirty(self: IControlDesignerTag, dirty: bool) """
        ...


class IControlDesignerView: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContainingRegion(self) -> DesignerRegion:
        """ Get: ContainingRegion(self: IControlDesignerView) -> DesignerRegion """
        ...

    @property
    def NamingContainerDesigner(self) -> IDesigner:
        """ Get: NamingContainerDesigner(self: IControlDesignerView) -> IDesigner """
        ...

    @property
    def SupportsRegions(self) -> bool:
        """ Get: SupportsRegions(self: IControlDesignerView) -> bool """
        ...


    def GetBounds(self, region:DesignerRegion) -> Rectangle:
        """ GetBounds(self: IControlDesignerView, region: DesignerRegion) -> Rectangle """
        ...

    def Invalidate(self, rectangle:Rectangle): # -> 
        """ Invalidate(self: IControlDesignerView, rectangle: Rectangle) """
        ...

    def SetFlags(self, viewFlags, setFlag:bool): # ->  # Not found arg types: {'viewFlags': 'ViewFlags'}
        """ SetFlags(self: IControlDesignerView, viewFlags: ViewFlags, setFlag: bool) """
        ...

    def SetRegionContent(self, region:EditableDesignerRegion, content:str): # -> 
        """ SetRegionContent(self: IControlDesignerView, region: EditableDesignerRegion, content: str) """
        ...

    def Update(self): # -> 
        """ Update(self: IControlDesignerView) """
        ...

    ViewEvent = ...


class IDataBindingSchemaProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanRefreshSchema(self) -> bool:
        """ Get: CanRefreshSchema(self: IDataBindingSchemaProvider) -> bool """
        ...

    @property
    def Schema(self): # -> IDataSourceViewSchema
        """ Get: Schema(self: IDataBindingSchemaProvider) -> IDataSourceViewSchema """
        ...


    def RefreshSchema(self, preferSilent:bool): # -> 
        """ RefreshSchema(self: IDataBindingSchemaProvider, preferSilent: bool) """
        ...


class IDataSourceFieldSchema: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataType(self) -> Type:
        """ Get: DataType(self: IDataSourceFieldSchema) -> Type """
        ...

    @property
    def Identity(self) -> bool:
        """ Get: Identity(self: IDataSourceFieldSchema) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: IDataSourceFieldSchema) -> bool """
        ...

    @property
    def IsUnique(self) -> bool:
        """ Get: IsUnique(self: IDataSourceFieldSchema) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: IDataSourceFieldSchema) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDataSourceFieldSchema) -> str """
        ...

    @property
    def Nullable(self) -> bool:
        """ Get: Nullable(self: IDataSourceFieldSchema) -> bool """
        ...

    @property
    def Precision(self) -> int:
        """ Get: Precision(self: IDataSourceFieldSchema) -> int """
        ...

    @property
    def PrimaryKey(self) -> bool:
        """ Get: PrimaryKey(self: IDataSourceFieldSchema) -> bool """
        ...

    @property
    def Scale(self) -> int:
        """ Get: Scale(self: IDataSourceFieldSchema) -> int """
        ...



class IDataSourceProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetResolvedSelectedDataSource(self) -> IEnumerable:
        """ GetResolvedSelectedDataSource(self: IDataSourceProvider) -> IEnumerable """
        ...

    def GetSelectedDataSource(self) -> object:
        """ GetSelectedDataSource(self: IDataSourceProvider) -> object """
        ...


class IDataSourceSchema: # skipped bases: <type 'object'>
    """ no doc """
    def GetViews(self) -> Array:
        """ GetViews(self: IDataSourceSchema) -> Array[IDataSourceViewSchema] """
        ...


class IDataSourceViewSchema: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IDataSourceViewSchema) -> str """
        ...


    def GetChildren(self) -> Array:
        """ GetChildren(self: IDataSourceViewSchema) -> Array[IDataSourceViewSchema] """
        ...

    def GetFields(self) -> Array:
        """ GetFields(self: IDataSourceViewSchema) -> Array[IDataSourceFieldSchema] """
        ...


class IDesignTimeResourceProviderFactoryService: # skipped bases: <type 'object'>
    """ no doc """
    def GetFactory(self) -> DesignTimeResourceProviderFactory:
        """ GetFactory(self: IDesignTimeResourceProviderFactoryService) -> DesignTimeResourceProviderFactory """
        ...


class IDesignTimeResourceWriter(IResourceWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def CreateResourceKey(self, resourceName:str, obj:object) -> str:
        """ CreateResourceKey(self: IDesignTimeResourceWriter, resourceName: str, obj: object) -> str """
        ...


class IDocumentProjectItem: # skipped bases: <type 'object'>
    """ no doc """
    def GetContents(self) -> Stream:
        """ GetContents(self: IDocumentProjectItem) -> Stream """
        ...

    def Open(self): # -> 
        """ Open(self: IDocumentProjectItem) """
        ...


class IFolderProjectItem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Children(self) -> ICollection:
        """ Get: Children(self: IFolderProjectItem) -> ICollection """
        ...


    def AddDocument(self, name:str, content:Array) -> IDocumentProjectItem:
        """ AddDocument(self: IFolderProjectItem, name: str, content: Array[Byte]) -> IDocumentProjectItem """
        ...

    def AddFolder(self, name:str) -> IFolderProjectItem:
        """ AddFolder(self: IFolderProjectItem, name: str) -> IFolderProjectItem """
        ...


class IHtmlControlDesignerBehavior: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Designer(self) -> HtmlControlDesigner:
        """
        Get: Designer(self: IHtmlControlDesignerBehavior) -> HtmlControlDesigner
        Set: Designer(self: IHtmlControlDesignerBehavior) = value
        """
        ...

    @property
    def DesignTimeElement(self) -> object:
        """ Get: DesignTimeElement(self: IHtmlControlDesignerBehavior) -> object """
        ...


    def GetAttribute(self, attribute:str, ignoreCase:bool) -> object:
        """ GetAttribute(self: IHtmlControlDesignerBehavior, attribute: str, ignoreCase: bool) -> object """
        ...

    def GetStyleAttribute(self, attribute:str, designTimeOnly:bool, ignoreCase:bool) -> object:
        """ GetStyleAttribute(self: IHtmlControlDesignerBehavior, attribute: str, designTimeOnly: bool, ignoreCase: bool) -> object """
        ...

    def RemoveAttribute(self, attribute:str, ignoreCase:bool): # -> 
        """ RemoveAttribute(self: IHtmlControlDesignerBehavior, attribute: str, ignoreCase: bool) """
        ...

    def RemoveStyleAttribute(self, attribute:str, designTimeOnly:bool, ignoreCase:bool): # -> 
        """ RemoveStyleAttribute(self: IHtmlControlDesignerBehavior, attribute: str, designTimeOnly: bool, ignoreCase: bool) """
        ...

    def SetAttribute(self, attribute:str, value:object, ignoreCase:bool): # -> 
        """ SetAttribute(self: IHtmlControlDesignerBehavior, attribute: str, value: object, ignoreCase: bool) """
        ...

    def SetStyleAttribute(self, attribute:str, designTimeOnly:bool, value:object, ignoreCase:bool): # -> 
        """ SetStyleAttribute(self: IHtmlControlDesignerBehavior, attribute: str, designTimeOnly: bool, value: object, ignoreCase: bool) """
        ...


class UrlEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ UrlEditor() """
    @property
    def Caption(self):
        ...

    @property
    def Filter(self):
        ...

    @property
    def Options(self):
        ...



class ImageUrlEditor(UrlEditor): # skipped bases: <type 'object'>
    """ ImageUrlEditor() """
    pass

class IProjectItem: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AppRelativeUrl(self) -> str:
        """ Get: AppRelativeUrl(self: IProjectItem) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IProjectItem) -> str """
        ...

    @property
    def Parent(self) -> IProjectItem:
        """ Get: Parent(self: IProjectItem) -> IProjectItem """
        ...

    @property
    def PhysicalPath(self) -> str:
        """ Get: PhysicalPath(self: IProjectItem) -> str """
        ...



class ITemplateEditingFrame(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ControlStyle(self) -> Style:
        """ Get: ControlStyle(self: ITemplateEditingFrame) -> Style """
        ...

    @property
    def InitialHeight(self) -> int:
        """
        Get: InitialHeight(self: ITemplateEditingFrame) -> int
        Set: InitialHeight(self: ITemplateEditingFrame) = value
        """
        ...

    @property
    def InitialWidth(self) -> int:
        """
        Get: InitialWidth(self: ITemplateEditingFrame) -> int
        Set: InitialWidth(self: ITemplateEditingFrame) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ITemplateEditingFrame) -> str """
        ...

    @property
    def TemplateNames(self) -> Array:
        """ Get: TemplateNames(self: ITemplateEditingFrame) -> Array[str] """
        ...

    @property
    def TemplateStyles(self) -> Array:
        """ Get: TemplateStyles(self: ITemplateEditingFrame) -> Array[Style] """
        ...

    @property
    def Verb(self): # -> TemplateEditingVerb
        """
        Get: Verb(self: ITemplateEditingFrame) -> TemplateEditingVerb
        Set: Verb(self: ITemplateEditingFrame) = value
        """
        ...


    def Close(self, saveChanges:bool): # -> 
        """ Close(self: ITemplateEditingFrame, saveChanges: bool) """
        ...

    def Open(self): # -> 
        """ Open(self: ITemplateEditingFrame) """
        ...

    def Resize(self, width:int, height:int): # -> 
        """ Resize(self: ITemplateEditingFrame, width: int, height: int) """
        ...

    def Save(self): # -> 
        """ Save(self: ITemplateEditingFrame) """
        ...

    def UpdateControlName(self, newName:str): # -> 
        """ UpdateControlName(self: ITemplateEditingFrame, newName: str) """
        ...


class ITemplateEditingService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SupportsNestedTemplateEditing(self) -> bool:
        """ Get: SupportsNestedTemplateEditing(self: ITemplateEditingService) -> bool """
        ...


    def CreateFrame(self, designer, frameName:str, templateNames:Array, controlStyle:Style = ..., templateStyles:Array = ...) -> ITemplateEditingFrame: # Not found arg types: {'designer': 'TemplatedControlDesigner'}
        """
        CreateFrame(self: ITemplateEditingService, designer: TemplatedControlDesigner, frameName: str, templateNames: Array[str]) -> ITemplateEditingFrame
        CreateFrame(self: ITemplateEditingService, designer: TemplatedControlDesigner, frameName: str, templateNames: Array[str], controlStyle: Style, templateStyles: Array[Style]) -> ITemplateEditingFrame
        """
        ...

    def GetContainingTemplateName(self, control:Control) -> str:
        """ GetContainingTemplateName(self: ITemplateEditingService, control: Control) -> str """
        ...


class IWebAdministrationService: # skipped bases: <type 'object'>
    """ no doc """
    def Start(self, arguments:IDictionary): # -> 
        """ Start(self: IWebAdministrationService, arguments: IDictionary) """
        ...


class IWebApplication(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RootProjectItem(self) -> IProjectItem:
        """ Get: RootProjectItem(self: IWebApplication) -> IProjectItem """
        ...


    def GetProjectItemFromUrl(self, appRelativeUrl:str) -> IProjectItem:
        """ GetProjectItemFromUrl(self: IWebApplication, appRelativeUrl: str) -> IProjectItem """
        ...

    def OpenWebConfiguration(self, isReadOnly:bool) -> Configuration:
        """ OpenWebConfiguration(self: IWebApplication, isReadOnly: bool) -> Configuration """
        ...


class IWebFormReferenceManager: # skipped bases: <type 'object'>
    """ no doc """
    def GetObjectType(self, tagPrefix:str, typeName:str) -> Type:
        """ GetObjectType(self: IWebFormReferenceManager, tagPrefix: str, typeName: str) -> Type """
        ...

    def GetRegisterDirectives(self) -> str:
        """ GetRegisterDirectives(self: IWebFormReferenceManager) -> str """
        ...

    def GetTagPrefix(self, objectType:Type) -> str:
        """ GetTagPrefix(self: IWebFormReferenceManager, objectType: Type) -> str """
        ...


class IWebFormsBuilderUIService: # skipped bases: <type 'object'>
    """ no doc """
    def BuildColor(self, owner:Control, initialColor:str) -> str:
        """ BuildColor(self: IWebFormsBuilderUIService, owner: Control, initialColor: str) -> str """
        ...

    def BuildUrl(self, owner:Control, initialUrl:str, baseUrl:str, caption:str, filter:str, options) -> str: # Not found arg types: {'options': 'UrlBuilderOptions'}
        """ BuildUrl(self: IWebFormsBuilderUIService, owner: Control, initialUrl: str, baseUrl: str, caption: str, filter: str, options: UrlBuilderOptions) -> str """
        ...


class IWebFormsDocumentService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DocumentUrl(self) -> str:
        """ Get: DocumentUrl(self: IWebFormsDocumentService) -> str """
        ...

    @property
    def IsLoading(self) -> bool:
        """ Get: IsLoading(self: IWebFormsDocumentService) -> bool """
        ...


    def CreateDiscardableUndoUnit(self) -> object:
        """ CreateDiscardableUndoUnit(self: IWebFormsDocumentService) -> object """
        ...

    def DiscardUndoUnit(self, discardableUndoUnit:object): # -> 
        """ DiscardUndoUnit(self: IWebFormsDocumentService, discardableUndoUnit: object) """
        ...

    def EnableUndo(self, enable:bool): # -> 
        """ EnableUndo(self: IWebFormsDocumentService, enable: bool) """
        ...

    def UpdateSelection(self): # -> 
        """ UpdateSelection(self: IWebFormsDocumentService) """
        ...

    LoadComplete = ...


class MailFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ MailFileEditor() """
    pass

class MdbDataFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ MdbDataFileEditor() """
    pass

class PostBackTriggerControlIDConverter(StringConverter): # skipped bases: <type 'object'>
    """ PostBackTriggerControlIDConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: PostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: PostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: PostBackTriggerControlIDConverter, context: ITypeDescriptorContext) -> bool """
        ...


class QueryExtenderDesigner(ControlDesigner, IControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ QueryExtenderDesigner() """
    pass

class ReadWriteControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ReadWriteControlDesigner() """
    def MapPropertyToStyle(self, *args): #cannot find CLR method
        """ MapPropertyToStyle(self: ReadWriteControlDesigner, propName: str, varPropValue: object) """
        ...


class ResourceExpressionEditor(ExpressionEditor): # skipped bases: <type 'object'>
    """ ResourceExpressionEditor() """
    pass

class ResourceExpressionEditorSheet(ExpressionEditorSheet): # skipped bases: <type 'object'>
    """ ResourceExpressionEditorSheet(expression: str, serviceProvider: IServiceProvider) """
    @property
    def ClassKey(self) -> str:
        """
        Get: ClassKey(self: ResourceExpressionEditorSheet) -> str
        Set: ClassKey(self: ResourceExpressionEditorSheet) = value
        """
        ...

    @property
    def ResourceKey(self) -> str:
        """
        Get: ResourceKey(self: ResourceExpressionEditorSheet) -> str
        Set: ResourceKey(self: ResourceExpressionEditorSheet) = value
        """
        ...



class RouteUrlExpressionEditor(ExpressionEditor): # skipped bases: <type 'object'>
    """ RouteUrlExpressionEditor() """
    pass

class RouteUrlExpressionEditorSheet(ExpressionEditorSheet): # skipped bases: <type 'object'>
    """ RouteUrlExpressionEditorSheet(expression: str, serviceProvider: IServiceProvider) """
    @property
    def RouteName(self) -> str:
        """
        Get: RouteName(self: RouteUrlExpressionEditorSheet) -> str
        Set: RouteName(self: RouteUrlExpressionEditorSheet) = value
        """
        ...

    @property
    def RouteValues(self) -> str:
        """
        Get: RouteValues(self: RouteUrlExpressionEditorSheet) -> str
        Set: RouteValues(self: RouteUrlExpressionEditorSheet) = value
        """
        ...



class RouteValueExpressionEditor(ExpressionEditor): # skipped bases: <type 'object'>
    """ RouteValueExpressionEditor() """
    pass

class RouteValueExpressionEditorSheet(ExpressionEditorSheet): # skipped bases: <type 'object'>
    """ RouteValueExpressionEditorSheet(expression: str, serviceProvider: IServiceProvider) """
    @property
    def RouteValue(self) -> str:
        """
        Get: RouteValue(self: RouteValueExpressionEditorSheet) -> str
        Set: RouteValue(self: RouteValueExpressionEditorSheet) = value
        """
        ...



class ScriptManagerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ScriptManagerDesigner() """
    @staticmethod
    def GetApplicationServices(scriptManager:ScriptManager, proxies:IEnumerable) -> str:
        """ GetApplicationServices(scriptManager: ScriptManager, proxies: IEnumerable[ScriptManagerProxy]) -> str """
        ...

    @staticmethod
    def GetProxyScript(scriptManager:ScriptManager, serviceReference:ServiceReference) -> str:
        """ GetProxyScript(scriptManager: ScriptManager, serviceReference: ServiceReference) -> str """
        ...

    @staticmethod
    def GetProxyUrl(scriptManager:ScriptManager, serviceReference:ServiceReference) -> str:
        """ GetProxyUrl(scriptManager: ScriptManager, serviceReference: ServiceReference) -> str """
        ...

    @staticmethod
    def GetScriptFromWebResource(assembly:Assembly, resourceName:str, culture:CultureInfo) -> str:
        """ GetScriptFromWebResource(assembly: Assembly, resourceName: str, culture: CultureInfo) -> str """
        ...

    @staticmethod
    def GetScriptReferences(scriptManager:ScriptManager, proxies:IEnumerable) -> ReadOnlyCollection:
        """ GetScriptReferences(scriptManager: ScriptManager, proxies: IEnumerable[ScriptManagerProxy]) -> ReadOnlyCollection[ScriptReference] """
        ...

    @staticmethod
    def GetServiceReferences(scriptManager:ScriptManager, proxies:IEnumerable) -> ReadOnlyCollection:
        """ GetServiceReferences(scriptManager: ScriptManager, proxies: IEnumerable[ScriptManagerProxy]) -> ReadOnlyCollection[ServiceReference] """
        ...


class ScriptManagerProxyDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ScriptManagerProxyDesigner() """
    pass

class ServiceReferenceCollectionEditor(CollectionEditorBase): # skipped bases: <type 'object'>
    """ ServiceReferenceCollectionEditor(type: Type) """
    pass

class SkinIDTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ SkinIDTypeConverter() """
    pass

class SupportsPreviewControlAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SupportsPreviewControlAttribute(supportsPreviewControl: bool) """
    @property
    def SupportsPreviewControl(self) -> bool:
        """ Get: SupportsPreviewControl(self: SupportsPreviewControlAttribute) -> bool """
        ...


    def __new__(cls, supportsPreviewControl:bool) -> Self:
        """ __new__(cls: type, supportsPreviewControl: bool) """
        ...

    Default: SupportsPreviewControlAttribute = ...


class TemplatedControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ TemplatedControlDesigner() """
    @property
    def ActiveTemplateEditingFrame(self) -> ITemplateEditingFrame:
        """ Get: ActiveTemplateEditingFrame(self: TemplatedControlDesigner) -> ITemplateEditingFrame """
        ...

    @property
    def CanEnterTemplateMode(self) -> bool:
        """ Get: CanEnterTemplateMode(self: TemplatedControlDesigner) -> bool """
        ...


    def CreateTemplateEditingFrame(self, *args): #cannot find CLR method
        """ CreateTemplateEditingFrame(self: TemplatedControlDesigner, verb: TemplateEditingVerb) -> ITemplateEditingFrame """
        ...

    def EnterTemplateMode(self, newTemplateEditingFrame:ITemplateEditingFrame): # -> 
        """ EnterTemplateMode(self: TemplatedControlDesigner, newTemplateEditingFrame: ITemplateEditingFrame) """
        ...

    def ExitTemplateMode(self, fSwitchingTemplates:bool, fNested:bool, fSave:bool): # -> 
        """ ExitTemplateMode(self: TemplatedControlDesigner, fSwitchingTemplates: bool, fNested: bool, fSave: bool) """
        ...

    def GetCachedTemplateEditingVerbs(self, *args): #cannot find CLR method
        """ GetCachedTemplateEditingVerbs(self: TemplatedControlDesigner) -> Array[TemplateEditingVerb] """
        ...

    def GetTemplateContainerDataItemProperty(self, templateName:str) -> str:
        """ GetTemplateContainerDataItemProperty(self: TemplatedControlDesigner, templateName: str) -> str """
        ...

    def GetTemplateContainerDataSource(self, templateName:str) -> IEnumerable:
        """ GetTemplateContainerDataSource(self: TemplatedControlDesigner, templateName: str) -> IEnumerable """
        ...

    def GetTemplateContent(self, editingFrame, templateName, allowEditing) -> Tuple_[str, bool]:
        """ GetTemplateContent(self: TemplatedControlDesigner, editingFrame: ITemplateEditingFrame, templateName: str) -> (str, bool) """
        ...

    def GetTemplateEditingVerbs(self) -> Array:
        """ GetTemplateEditingVerbs(self: TemplatedControlDesigner) -> Array[TemplateEditingVerb] """
        ...

    def GetTemplateFromText(self, *args): #cannot find CLR method
        """ GetTemplateFromText(self: TemplatedControlDesigner, text: str) -> ITemplate """
        ...

    def GetTemplatePropertyParentType(self, templateName:str) -> Type:
        """ GetTemplatePropertyParentType(self: TemplatedControlDesigner, templateName: str) -> Type """
        ...

    def GetTextFromTemplate(self, *args): #cannot find CLR method
        """ GetTextFromTemplate(self: TemplatedControlDesigner, template: ITemplate) -> str """
        ...

    def OnSetParent(self): # -> 
        """ OnSetParent(self: TemplatedControlDesigner) """
        ...

    def OnTemplateModeChanged(self, *args): #cannot find CLR method
        """ OnTemplateModeChanged(self: TemplatedControlDesigner) """
        ...

    def SaveActiveTemplateEditingFrame(self, *args): #cannot find CLR method
        """ SaveActiveTemplateEditingFrame(self: TemplatedControlDesigner) """
        ...

    def SetTemplateContent(self, editingFrame:ITemplateEditingFrame, templateName:str, templateContent:str): # -> 
        """ SetTemplateContent(self: TemplatedControlDesigner, editingFrame: ITemplateEditingFrame, templateName: str, templateContent: str) """
        ...


class TemplatedEditableDesignerRegion(EditableDesignerRegion): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ TemplatedEditableDesignerRegion(templateDefinition: TemplateDefinition) """
    @property
    def IsSingleInstanceTemplate(self) -> bool:
        """
        Get: IsSingleInstanceTemplate(self: TemplatedEditableDesignerRegion) -> bool
        Set: IsSingleInstanceTemplate(self: TemplatedEditableDesignerRegion) = value
        """
        ...

    @property
    def TemplateDefinition(self): # -> TemplateDefinition
        """ Get: TemplateDefinition(self: TemplatedEditableDesignerRegion) -> TemplateDefinition """
        ...



class TemplateDefinition(DesignerObject): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """
    TemplateDefinition(designer: ControlDesigner, name: str, templatedObject: object, templatePropertyName: str)
    TemplateDefinition(designer: ControlDesigner, name: str, templatedObject: object, templatePropertyName: str, style: Style)
    TemplateDefinition(designer: ControlDesigner, name: str, templatedObject: object, templatePropertyName: str, serverControlsOnly: bool)
    TemplateDefinition(designer: ControlDesigner, name: str, templatedObject: object, templatePropertyName: str, style: Style, serverControlsOnly: bool)
    """
    @property
    def AllowEditing(self) -> bool:
        """ Get: AllowEditing(self: TemplateDefinition) -> bool """
        ...

    @property
    def Content(self) -> str:
        """
        Get: Content(self: TemplateDefinition) -> str
        Set: Content(self: TemplateDefinition) = value
        """
        ...

    @property
    def ServerControlsOnly(self) -> bool:
        """ Get: ServerControlsOnly(self: TemplateDefinition) -> bool """
        ...

    @property
    def Style(self) -> Style:
        """ Get: Style(self: TemplateDefinition) -> Style """
        ...

    @property
    def SupportsDataBinding(self) -> bool:
        """
        Get: SupportsDataBinding(self: TemplateDefinition) -> bool
        Set: SupportsDataBinding(self: TemplateDefinition) = value
        """
        ...

    @property
    def TemplatedObject(self) -> object:
        """ Get: TemplatedObject(self: TemplateDefinition) -> object """
        ...

    @property
    def TemplatePropertyName(self) -> str:
        """ Get: TemplatePropertyName(self: TemplateDefinition) -> str """
        ...



class TemplateEditingService(IDisposable, ITemplateEditingService): # skipped bases: <type 'object'>
    """ TemplateEditingService(designerHost: IDesignerHost) """
    pass

class TemplateEditingVerb(IDisposable, DesignerVerb): # skipped bases: <type 'object'>
    """
    TemplateEditingVerb(text: str, index: int, designer: TemplatedControlDesigner)
    TemplateEditingVerb(text: str, index: int)
    """
    @property
    def Index(self) -> int:
        """ Get: Index(self: TemplateEditingVerb) -> int """
        ...



class TemplateGroup: # skipped bases: <type 'object'>, <type 'object'>
    """
    TemplateGroup(groupName: str)
    TemplateGroup(groupName: str, groupStyle: Style)
    """
    @property
    def GroupName(self) -> str:
        """ Get: GroupName(self: TemplateGroup) -> str """
        ...

    @property
    def GroupStyle(self) -> Style:
        """ Get: GroupStyle(self: TemplateGroup) -> Style """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: TemplateGroup) -> bool """
        ...

    @property
    def Templates(self) -> Array:
        """ Get: Templates(self: TemplateGroup) -> Array[TemplateDefinition] """
        ...


    def AddTemplateDefinition(self, templateDefinition:TemplateDefinition): # -> 
        """ AddTemplateDefinition(self: TemplateGroup, templateDefinition: TemplateDefinition) """
        ...


class TemplateGroupCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TemplateGroupCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: TemplateGroupCollection) -> int """
        ...


    def AddRange(self, groups:TemplateGroupCollection): # -> 
        """ AddRange(self: TemplateGroupCollection, groups: TemplateGroupCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TemplateGroupCollection, array: Array[TemplateGroup], index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class TemplateModeChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TemplateModeChangedEventArgs(newTemplateGroup: TemplateGroup) """
    @property
    def NewTemplateGroup(self) -> TemplateGroup:
        """ Get: NewTemplateGroup(self: TemplateModeChangedEventArgs) -> TemplateGroup """
        ...


    def __new__(cls, newTemplateGroup:TemplateGroup) -> Self:
        """ __new__(cls: type, newTemplateGroup: TemplateGroup) """
        ...


class TextControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ TextControlDesigner() """
    pass

class TextDataBindingHandler(DataBindingHandler): # skipped bases: <type 'object'>
    """ TextDataBindingHandler() """
    pass

class TimerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ TimerDesigner() """
    pass

class TransactedChangeCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TransactedChangeCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, context:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TransactedChangeCallback, context: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: TransactedChangeCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, context:object) -> bool:
        """ Invoke(self: TransactedChangeCallback, context: object) -> bool """
        ...


class TypeSchema(IDataSourceSchema): # skipped bases: <type 'object'>
    """ TypeSchema(type: Type) """
    pass

class UpdatePanelDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ UpdatePanelDesigner() """
    pass

class UpdatePanelTriggerCollectionEditor(CollectionEditorBase): # skipped bases: <type 'object'>
    """ UpdatePanelTriggerCollectionEditor(type: Type) """
    def EditValue(self, *__args) -> object:
        """ EditValue(self: UpdatePanelTriggerCollectionEditor, context: ITypeDescriptorContext, provider: IServiceProvider, value: object) -> object """
        ...


class UpdateProgressAssociatedUpdatePanelIDConverter(StringConverter): # skipped bases: <type 'object'>
    """ UpdateProgressAssociatedUpdatePanelIDConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: UpdateProgressAssociatedUpdatePanelIDConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: UpdateProgressAssociatedUpdatePanelIDConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: UpdateProgressAssociatedUpdatePanelIDConverter, context: ITypeDescriptorContext) -> bool """
        ...


class UpdateProgressDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ UpdateProgressDesigner() """
    pass

class UrlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BuildUrl(*__args) -> str:
        """
        BuildUrl(component: IComponent, owner: Control, initialUrl: str, caption: str, filter: str) -> str
        BuildUrl(component: IComponent, owner: Control, initialUrl: str, caption: str, filter: str, options: UrlBuilderOptions) -> str
        BuildUrl(serviceProvider: IServiceProvider, owner: Control, initialUrl: str, caption: str, filter: str, options: UrlBuilderOptions) -> str
        """
        ...


class UrlBuilderOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) UrlBuilderOptions, values: NoAbsolute (1), None (0) """
    NoAbsolute: UrlBuilderOptions = ...
    value__ = ...


class UserControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ UserControlDesigner() """
    pass

class UserControlFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ UserControlFileEditor() """
    pass

class ViewEvent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Click: ViewEvent = ...
    Paint: ViewEvent = ...
    TemplateModeChanged: ViewEvent = ...


class ViewEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ViewEventArgs(eventType: ViewEvent, region: DesignerRegion, eventArgs: EventArgs) """
    @property
    def EventArgs(self) -> EventArgs:
        """ Get: EventArgs(self: ViewEventArgs) -> EventArgs """
        ...

    @property
    def EventType(self) -> ViewEvent:
        """ Get: EventType(self: ViewEventArgs) -> ViewEvent """
        ...

    @property
    def Region(self) -> DesignerRegion:
        """ Get: Region(self: ViewEventArgs) -> DesignerRegion """
        ...


    def __new__(cls, eventType:ViewEvent, region:DesignerRegion, eventArgs:EventArgs) -> Self:
        """ __new__(cls: type, eventType: ViewEvent, region: DesignerRegion, eventArgs: EventArgs) """
        ...


class ViewEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ViewEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ViewEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ViewEventHandler, sender: object, e: ViewEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ViewEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ViewEventArgs): # -> 
        """ Invoke(self: ViewEventHandler, sender: object, e: ViewEventArgs) """
        ...


class ViewFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ViewFlags, values: CustomPaint (1), DesignTimeHtmlRequiresLoadComplete (2), TemplateEditing (4) """
    CustomPaint: ViewFlags = ...
    DesignTimeHtmlRequiresLoadComplete: ViewFlags = ...
    TemplateEditing: ViewFlags = ...
    value__ = ...


class ViewRendering: # skipped bases: <type 'object'>, <type 'object'>
    """
    ViewRendering(content: str, regions: DesignerRegionCollection)
    ViewRendering(content: str, regions: DesignerRegionCollection, visible: bool)
    """
    @property
    def Content(self) -> str:
        """ Get: Content(self: ViewRendering) -> str """
        ...

    @property
    def Regions(self) -> DesignerRegionCollection:
        """ Get: Regions(self: ViewRendering) -> DesignerRegionCollection """
        ...

    @property
    def Visible(self) -> bool:
        """ Get: Visible(self: ViewRendering) -> bool """
        ...



class WebFormsDesignerActionService(DesignerActionService): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ WebFormsDesignerActionService(serviceProvider: IServiceProvider) """
    pass

class WebFormsReferenceManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetRegisterDirectives(self) -> ICollection:
        """ GetRegisterDirectives(self: WebFormsReferenceManager) -> ICollection """
        ...

    def GetTagPrefix(self, objectType:Type) -> str:
        """ GetTagPrefix(self: WebFormsReferenceManager, objectType: Type) -> str """
        ...

    def GetType(self, tagPrefix:str = ..., tagName:str = ...) -> Type:
        """ GetType(self: WebFormsReferenceManager, tagPrefix: str, tagName: str) -> Type """
        ...

    def GetUserControlPath(self, tagPrefix:str, tagName:str) -> str:
        """ GetUserControlPath(self: WebFormsReferenceManager, tagPrefix: str, tagName: str) -> str """
        ...

    def RegisterTagPrefix(self, objectType:Type) -> str:
        """ RegisterTagPrefix(self: WebFormsReferenceManager, objectType: Type) -> str """
        ...


class WebFormsRootDesigner(IRootDesigner, IDesignerFilter): # skipped bases: <type 'IDisposable'>, <type 'IDesigner'>, <type 'object'>
    """ no doc """
    @property
    def Component(self) -> IComponent:
        """
        Get: Component(self: WebFormsRootDesigner) -> IComponent
        Set: Component(self: WebFormsRootDesigner) = value
        """
        ...

    @property
    def CurrentCulture(self) -> CultureInfo:
        """ Get: CurrentCulture(self: WebFormsRootDesigner) -> CultureInfo """
        ...

    @property
    def DocumentUrl(self) -> str:
        """ Get: DocumentUrl(self: WebFormsRootDesigner) -> str """
        ...

    @property
    def IsDesignerViewLocked(self) -> bool:
        """ Get: IsDesignerViewLocked(self: WebFormsRootDesigner) -> bool """
        ...

    @property
    def IsLoading(self) -> bool:
        """ Get: IsLoading(self: WebFormsRootDesigner) -> bool """
        ...

    @property
    def ReferenceManager(self) -> WebFormsReferenceManager:
        """ Get: ReferenceManager(self: WebFormsRootDesigner) -> WebFormsReferenceManager """
        ...

    @property
    def Verbs(self):
        ...


    def AddClientScriptToDocument(self, scriptItem:ClientScriptItem): # -> 
        """ AddClientScriptToDocument(self: WebFormsRootDesigner, scriptItem: ClientScriptItem) """
        ...

    def AddControlToDocument(self, newControl:Control, referenceControl:Control, location:ControlLocation) -> str:
        """ AddControlToDocument(self: WebFormsRootDesigner, newControl: Control, referenceControl: Control, location: ControlLocation) -> str """
        ...

    def CreateDesignerActionService(self, *args): #cannot find CLR method
        """ CreateDesignerActionService(self: WebFormsRootDesigner, serviceProvider: IServiceProvider) -> DesignerActionService """
        ...

    def CreateUrlResolutionService(self, *args): #cannot find CLR method
        """ CreateUrlResolutionService(self: WebFormsRootDesigner) -> IUrlResolutionService """
        ...

    def Dispose(self, *args): #cannot find CLR method
        """ Dispose(self: WebFormsRootDesigner, disposing: bool) """
        ...

    def GenerateEmptyDesignTimeHtml(self, control:Control) -> str:
        """ GenerateEmptyDesignTimeHtml(self: WebFormsRootDesigner, control: Control) -> str """
        ...

    def GenerateErrorDesignTimeHtml(self, control:Control, e:Exception, errorMessage:str) -> str:
        """ GenerateErrorDesignTimeHtml(self: WebFormsRootDesigner, control: Control, e: Exception, errorMessage: str) -> str """
        ...

    def GetClientScriptsInDocument(self) -> ClientScriptItemCollection:
        """ GetClientScriptsInDocument(self: WebFormsRootDesigner) -> ClientScriptItemCollection """
        ...

    def GetControlViewAndTag(self, *args): #cannot find CLR method
        """ GetControlViewAndTag(self: WebFormsRootDesigner, control: Control) -> (IControlDesignerView, IControlDesignerTag) """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: WebFormsRootDesigner, serviceType: Type) -> object """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: WebFormsRootDesigner, component: IComponent) """
        ...

    def OnLoadComplete(self, *args): #cannot find CLR method
        """ OnLoadComplete(self: WebFormsRootDesigner, e: EventArgs) """
        ...

    def RemoveClientScriptFromDocument(self, clientScriptId:str): # -> 
        """ RemoveClientScriptFromDocument(self: WebFormsRootDesigner, clientScriptId: str) """
        ...

    def RemoveControlFromDocument(self, control:Control): # -> 
        """ RemoveControlFromDocument(self: WebFormsRootDesigner, control: Control) """
        ...

    def ResolveUrl(self, relativeUrl:str) -> str:
        """ ResolveUrl(self: WebFormsRootDesigner, relativeUrl: str) -> str """
        ...

    def SetControlID(self, control:Control, id:str): # -> 
        """ SetControlID(self: WebFormsRootDesigner, control: Control, id: str) """
        ...

    LoadComplete = ...


class XmlDataFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ XmlDataFileEditor() """
    pass

class XmlDocumentSchema(IDataSourceSchema): # skipped bases: <type 'object'>
    """ XmlDocumentSchema(xmlDocument: XmlDocument, xPath: str) """
    pass

class XmlFileEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ XmlFileEditor() """
    pass

class XmlUrlEditor(UrlEditor): # skipped bases: <type 'object'>
    """ XmlUrlEditor() """
    pass

class XsdSchemaFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ XsdSchemaFileEditor() """
    pass

class XslTransformFileEditor(UrlEditor): # skipped bases: <type 'object'>
    """ XslTransformFileEditor() """
    pass

class XslUrlEditor(UrlEditor): # skipped bases: <type 'object'>
    """ XslUrlEditor() """
    pass

# variables with complex values

