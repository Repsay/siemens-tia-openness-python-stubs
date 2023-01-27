# encoding: utf-8
# module System.Web.UI.Design.WebControls calls itself WebControls
# from System.Web.Extensions.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, IServiceProvider, Type

from System.Collections import IEnumerable

from System.ComponentModel import (IComponent, ISite, ITypeDescriptorContext, 
    Int32Converter, StringConverter, TypeConverter, TypeDescriptionProvider)

from System.ComponentModel.Design import ComponentChangedEventArgs

from System.Drawing.Design import UITypeEditor

from System.Globalization import Calendar, CultureInfo

from System.Web.UI import DataSourceOperation, UserControl

from System.Web.UI.MobileControls import Form

from System.Windows.Forms.Design import ControlDesigner

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    CollectionEditor, ConnectionStringEditor, ContainerControlDesigner, 
    DataBindingHandler, DataBoundControl, DataControlField, 
    DataSourceDesigner, DesignerActionListCollection, DesignerAutoFormat, 
    DesignerAutoFormatCollection, DesignerDataSourceView, 
    DesignerHierarchicalDataSourceView, DesignerRegionCollection, 
    DialogResult, EditableDesignerRegion, HierarchicalDataSourceDesigner, 
    IDataBindingSchemaProvider, IDataSourceDesigner, IDataSourceFieldSchema, 
    IDataSourceProvider, IHierarchicalDataSourceDesigner, 
    ITemplateEditingFrame, IWizardStepEditableRegion, 
    ReadWriteControlDesigner, StandardValuesCollection, TemplateField, 
    TemplateGroupCollection, TemplatedControlDesigner, 
    TemplatedEditableDesignerRegion, TextControlDesigner, UrlEditor, 
    WindowsFormsComponentEditor, WizardStepBase)
"""

# no functions
# classes

class SqlDataSourceDesigner(DataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'IDataSourceDesigner'>, <type 'object'>
    """ SqlDataSourceDesigner() """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlDataSourceDesigner) -> str
        Set: ConnectionString(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def DeleteQuery(self) -> DataSourceOperation:
        """
        Get: DeleteQuery(self: SqlDataSourceDesigner) -> DataSourceOperation
        Set: DeleteQuery(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def InsertQuery(self) -> DataSourceOperation:
        """
        Get: InsertQuery(self: SqlDataSourceDesigner) -> DataSourceOperation
        Set: InsertQuery(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: SqlDataSourceDesigner) -> str
        Set: ProviderName(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def SelectCommand(self) -> str:
        """
        Get: SelectCommand(self: SqlDataSourceDesigner) -> str
        Set: SelectCommand(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def SelectQuery(self) -> DataSourceOperation:
        """
        Get: SelectQuery(self: SqlDataSourceDesigner) -> DataSourceOperation
        Set: SelectQuery(self: SqlDataSourceDesigner) = value
        """
        ...

    @property
    def UpdateQuery(self) -> DataSourceOperation:
        """
        Get: UpdateQuery(self: SqlDataSourceDesigner) -> DataSourceOperation
        Set: UpdateQuery(self: SqlDataSourceDesigner) = value
        """
        ...


    def CreateView(self, *args): #cannot find CLR method
        """ CreateView(self: SqlDataSourceDesigner, viewName: str) -> SqlDesignerDataSourceView """
        ...

    def DeriveParameters(self, *args): #cannot find CLR method
        """ DeriveParameters(self: SqlDataSourceDesigner, providerName: str, command: DbCommand) """
        ...

    def GetConnectionString(self, *args): #cannot find CLR method
        """ GetConnectionString(self: SqlDataSourceDesigner) -> str """
        ...

    def InferParameterNames(self, *args): #cannot find CLR method
        """ InferParameterNames(self: SqlDataSourceDesigner, connection: DesignerDataConnection, commandText: str, commandType: SqlDataSourceCommandType) -> Array[Parameter] """
        ...


class AccessDataSourceDesigner(SqlDataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'IDataSourceDesigner'>, <type 'object'>
    """ AccessDataSourceDesigner() """
    @property
    def DataFile(self) -> str:
        """
        Get: DataFile(self: AccessDataSourceDesigner) -> str
        Set: DataFile(self: AccessDataSourceDesigner) = value
        """
        ...



class BaseDataBoundControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ no doc """
    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: BaseDataBoundControlDesigner) -> str
        Set: DataSource(self: BaseDataBoundControlDesigner) = value
        """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: BaseDataBoundControlDesigner) -> str
        Set: DataSourceID(self: BaseDataBoundControlDesigner) = value
        """
        ...


    def ConnectToDataSource(self, *args): #cannot find CLR method
        """ ConnectToDataSource(self: BaseDataBoundControlDesigner) -> bool """
        ...

    def CreateDataSource(self, *args): #cannot find CLR method
        """ CreateDataSource(self: BaseDataBoundControlDesigner) """
        ...

    def DataBind(self, *args): #cannot find CLR method
        """ DataBind(self: BaseDataBoundControlDesigner, dataBoundControl: BaseDataBoundControl) """
        ...

    def DisconnectFromDataSource(self, *args): #cannot find CLR method
        """ DisconnectFromDataSource(self: BaseDataBoundControlDesigner) """
        ...

    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: BaseDataBoundControlDesigner, forceUpdateView: bool) """
        ...

    def OnSchemaRefreshed(self, *args): #cannot find CLR method
        """ OnSchemaRefreshed(self: BaseDataBoundControlDesigner) """
        ...

    @staticmethod
    def ShowCreateDataSourceDialog(controlDesigner, dataSourceType, configure, dataSourceID): # -> Tuple_[DialogResult, str]
        """ ShowCreateDataSourceDialog(controlDesigner: ControlDesigner, dataSourceType: Type, configure: bool) -> (DialogResult, str) """
        ...


class DataBoundControlDesigner(IDataBindingSchemaProvider, BaseDataBoundControlDesigner, IDataSourceProvider): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ DataBoundControlDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: DataBoundControlDesigner) -> DesignerActionListCollection """
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: DataBoundControlDesigner) -> str
        Set: DataMember(self: DataBoundControlDesigner) = value
        """
        ...

    @property
    def DataSourceDesigner(self): # -> IDataSourceDesigner
        """ Get: DataSourceDesigner(self: DataBoundControlDesigner) -> IDataSourceDesigner """
        ...

    @property
    def DesignerView(self): # -> DesignerDataSourceView
        """ Get: DesignerView(self: DataBoundControlDesigner) -> DesignerDataSourceView """
        ...

    @property
    def SampleRowCount(self):
        ...

    @property
    def UseDataSourcePickerActionList(self):
        ...


    def GetDesignTimeDataSource(self, *args): #cannot find CLR method
        """ GetDesignTimeDataSource(self: DataBoundControlDesigner) -> IEnumerable """
        ...

    def GetSampleDataSource(self, *args): #cannot find CLR method
        """ GetSampleDataSource(self: DataBoundControlDesigner) -> IEnumerable """
        ...


class AdRotatorDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ AdRotatorDesigner() """
    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: AdRotatorDesigner) -> str """
        ...


class BaseDataListComponentEditor(WindowsFormsComponentEditor): # skipped bases: <type 'object'>
    """ BaseDataListComponentEditor(initialPage: int) """
    def __new__(cls, initialPage:int) -> Self:
        """ __new__(cls: type, initialPage: int) """
        ...


class BaseDataListDesigner(TemplatedControlDesigner, IDataBindingSchemaProvider, IDataSourceProvider): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ no doc """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: BaseDataListDesigner) -> DesignerActionListCollection """
        ...

    @property
    def DataKeyField(self) -> str:
        """
        Get: DataKeyField(self: BaseDataListDesigner) -> str
        Set: DataKeyField(self: BaseDataListDesigner) = value
        """
        ...

    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: BaseDataListDesigner) -> str
        Set: DataMember(self: BaseDataListDesigner) = value
        """
        ...

    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: BaseDataListDesigner) -> str
        Set: DataSource(self: BaseDataListDesigner) = value
        """
        ...

    @property
    def DataSourceDesigner(self): # -> IDataSourceDesigner
        """ Get: DataSourceDesigner(self: BaseDataListDesigner) -> IDataSourceDesigner """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: BaseDataListDesigner) -> str
        Set: DataSourceID(self: BaseDataListDesigner) = value
        """
        ...

    @property
    def DesignerView(self): # -> DesignerDataSourceView
        """ Get: DesignerView(self: BaseDataListDesigner) -> DesignerDataSourceView """
        ...


    def GetDesignTimeDataSource(self, *args): #cannot find CLR method
        """
        GetDesignTimeDataSource(self: BaseDataListDesigner, minimumRows: int) -> (IEnumerable, bool)
        GetDesignTimeDataSource(self: BaseDataListDesigner, selectedDataSource: IEnumerable, minimumRows: int) -> (IEnumerable, bool)
        """
        ...

    def InvokePropertyBuilder(self, *args): #cannot find CLR method
        """ InvokePropertyBuilder(self: BaseDataListDesigner, initialPage: int) """
        ...

    def OnAutoFormat(self, *args): #cannot find CLR method
        """ OnAutoFormat(self: BaseDataListDesigner, sender: object, e: EventArgs) """
        ...

    def OnAutoFormatApplied(self, appliedAutoFormat): # ->  # Not found arg types: {'appliedAutoFormat': 'DesignerAutoFormat'}
        """ OnAutoFormatApplied(self: BaseDataListDesigner, appliedAutoFormat: DesignerAutoFormat) """
        ...

    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: BaseDataListDesigner) """
        ...

    def OnPropertyBuilder(self, *args): #cannot find CLR method
        """ OnPropertyBuilder(self: BaseDataListDesigner, sender: object, e: EventArgs) """
        ...

    def OnSchemaRefreshed(self, *args): #cannot find CLR method
        """ OnSchemaRefreshed(self: BaseDataListDesigner) """
        ...

    def OnStylesChanged(self, *args): #cannot find CLR method
        """ OnStylesChanged(self: BaseDataListDesigner) """
        ...

    def OnTemplateEditingVerbsChanged(self, *args): #cannot find CLR method
        """ OnTemplateEditingVerbsChanged(self: BaseDataListDesigner) """
        ...


class PreviewControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ PreviewControlDesigner() """
    pass

class BaseValidatorDesigner(PreviewControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ BaseValidatorDesigner() """
    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: BaseValidatorDesigner) -> str """
        ...


class ListControlDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ ListControlDesigner() """
    @property
    def DataTextField(self) -> str:
        """
        Get: DataTextField(self: ListControlDesigner) -> str
        Set: DataTextField(self: ListControlDesigner) = value
        """
        ...

    @property
    def DataValueField(self) -> str:
        """
        Get: DataValueField(self: ListControlDesigner) -> str
        Set: DataValueField(self: ListControlDesigner) = value
        """
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: ListControlDesigner) -> str """
        ...

    def GetResolvedSelectedDataSource(self) -> IEnumerable:
        """ GetResolvedSelectedDataSource(self: ListControlDesigner) -> IEnumerable """
        ...

    def GetSelectedDataSource(self) -> object:
        """ GetSelectedDataSource(self: ListControlDesigner) -> object """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: ListControlDesigner, component: IComponent) """
        ...


class BulletedListDesigner(ListControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ BulletedListDesigner() """
    pass

class ButtonDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ButtonDesigner() """
    pass

class CalendarAutoFormatDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ CalendarAutoFormatDialog(calendar: Calendar) """
    def DoDelayLoadActions(self, *args): #cannot find CLR method
        """ DoDelayLoadActions(self: CalendarAutoFormatDialog) """
        ...

    def OnOKClicked(self, *args): #cannot find CLR method
        """ OnOKClicked(self: CalendarAutoFormatDialog, source: object, e: EventArgs) """
        ...

    def OnSelChangedScheme(self, *args): #cannot find CLR method
        """ OnSelChangedScheme(self: CalendarAutoFormatDialog, source: object, e: EventArgs) """
        ...

    def SaveComponent(self, *args): #cannot find CLR method
        """ SaveComponent(self: CalendarAutoFormatDialog) """
        ...

    def __new__(cls, calendar:Calendar) -> Self:
        """ __new__(cls: type, calendar: Calendar) """
        ...


class CalendarDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CalendarDesigner() """
    def OnAutoFormat(self, *args): #cannot find CLR method
        """ OnAutoFormat(self: CalendarDesigner, sender: object, e: EventArgs) """
        ...


class ChangePasswordDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ChangePasswordDesigner() """
    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: ChangePasswordDesigner) -> bool
        Set: RenderOuterTable(self: ChangePasswordDesigner) = value
        """
        ...



class CheckBoxDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CheckBoxDesigner() """
    pass

class CompositeControlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CompositeControlDesigner() """
    def CreateChildControls(self, *args): #cannot find CLR method
        """ CreateChildControls(self: CompositeControlDesigner) """
        ...


class ContentDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ContentDesigner() """
    pass

class ContentPlaceHolderDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ContentPlaceHolderDesigner() """
    pass

class WizardDesigner(CompositeControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ WizardDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: WizardDesigner) -> DesignerActionListCollection """
        ...

    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: WizardDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def DisplaySideBar(self):
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: WizardDesigner) -> TemplateGroupCollection """
        ...


    def AddDesignerRegions(self, *args): #cannot find CLR method
        """ AddDesignerRegions(self: WizardDesigner, regions: DesignerRegionCollection) """
        ...

    def ConvertToCustomNavigationTemplate(self, *args): #cannot find CLR method
        """ ConvertToCustomNavigationTemplate(self: WizardDesigner) """
        ...

    def ConvertToTemplate(self, *args): #cannot find CLR method
        """ ConvertToTemplate(self: WizardDesigner, description: str, component: IComponent, templateName: str, keys: Array[str]) """
        ...

    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: WizardDesigner, region: EditableDesignerRegion) -> str """
        ...

    def OnComponentChanged(self, sender:object, ce:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: WizardDesigner, sender: object, ce: ComponentChangedEventArgs) """
        ...

    def ResetTemplate(self, *args): #cannot find CLR method
        """ ResetTemplate(self: WizardDesigner, description: str, component: IComponent, templateName: str) """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: WizardDesigner, region: EditableDesignerRegion, content: str) """
        ...


class CreateUserWizardDesigner(WizardDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ CreateUserWizardDesigner() """
    pass

class WizardStepCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ WizardStepCollectionEditor(type: Type) """
    pass

class CreateUserWizardStepCollectionEditor(WizardStepCollectionEditor): # skipped bases: <type 'object'>
    """ CreateUserWizardStepCollectionEditor(type: Type) """
    pass

class DataControlFieldDesigner: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultNodeText(self) -> str:
        """ Get: DefaultNodeText(self: DataControlFieldDesigner) -> str """
        ...

    @property
    def ServiceProvider(self):
        ...

    @property
    def UsesSchema(self) -> bool:
        """ Get: UsesSchema(self: DataControlFieldDesigner) -> bool """
        ...


    def CreateField(self, fieldSchema = ...): # -> DataControlField # Not found arg types: {'fieldSchema': 'IDataSourceFieldSchema'}
        """
        CreateField(self: DataControlFieldDesigner) -> DataControlField
        CreateField(self: DataControlFieldDesigner, fieldSchema: IDataSourceFieldSchema) -> DataControlField
        """
        ...

    def CreateTemplateField(self, dataControlField, dataBoundControl): # -> TemplateField # Not found arg types: {'dataBoundControl': 'DataBoundControl', 'dataControlField': 'DataControlField'}
        """ CreateTemplateField(self: DataControlFieldDesigner, dataControlField: DataControlField, dataBoundControl: DataBoundControl) -> TemplateField """
        ...

    def GetNewDataSourceName(self, *args): #cannot find CLR method
        """ GetNewDataSourceName(self: DataControlFieldDesigner, controlType: Type, mode: DataBoundControlMode) -> str """
        ...

    def GetNodeText(self, dataControlField) -> str: # Not found arg types: {'dataControlField': 'DataControlField'}
        """ GetNodeText(self: DataControlFieldDesigner, dataControlField: DataControlField) -> str """
        ...

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: DataControlFieldDesigner, serviceType: Type) -> object """
        ...

    def GetTemplate(self, *args): #cannot find CLR method
        """ GetTemplate(self: DataControlFieldDesigner, control: DataBoundControl, templateContent: str) -> ITemplate """
        ...

    def GetTemplateField(self, *args): #cannot find CLR method
        """ GetTemplateField(self: DataControlFieldDesigner, dataControlField: DataControlField, dataBoundControl: DataBoundControl) -> TemplateField """
        ...

    def IsEnabled(self, parent) -> bool: # Not found arg types: {'parent': 'DataBoundControl'}
        """ IsEnabled(self: DataControlFieldDesigner, parent: DataBoundControl) -> bool """
        ...


class DataControlFieldTypeEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DataControlFieldTypeEditor() """
    pass

class DataGridColumnCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DataGridColumnCollectionEditor() """
    pass

class DataGridComponentEditor(BaseDataListComponentEditor): # skipped bases: <type 'object'>
    """
    DataGridComponentEditor()
    DataGridComponentEditor(initialPage: int)
    """
    pass

class DataGridDesigner(BaseDataListDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ DataGridDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: DataGridDesigner) -> DesignerAutoFormatCollection """
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: DataGridDesigner) -> str """
        ...

    def GetTemplateContainerDataItemProperty(self, templateName:str) -> str:
        """ GetTemplateContainerDataItemProperty(self: DataGridDesigner, templateName: str) -> str """
        ...

    def GetTemplateContent(self, editingFrame, templateName, allowEditing) -> Tuple_[str, bool]:
        """ GetTemplateContent(self: DataGridDesigner, editingFrame: ITemplateEditingFrame, templateName: str) -> (str, bool) """
        ...

    def GetTemplatePropertyParentType(self, templateName:str) -> Type:
        """ GetTemplatePropertyParentType(self: DataGridDesigner, templateName: str) -> Type """
        ...

    def OnColumnsChanged(self): # -> 
        """ OnColumnsChanged(self: DataGridDesigner) """
        ...

    def SetTemplateContent(self, editingFrame, templateName:str, templateContent:str): # ->  # Not found arg types: {'editingFrame': 'ITemplateEditingFrame'}
        """ SetTemplateContent(self: DataGridDesigner, editingFrame: ITemplateEditingFrame, templateName: str, templateContent: str) """
        ...


class DataListComponentEditor(BaseDataListComponentEditor): # skipped bases: <type 'object'>
    """
    DataListComponentEditor()
    DataListComponentEditor(initialPage: int)
    """
    pass

class DataListDesigner(BaseDataListDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ DataListDesigner() """
    @property
    def AllowResize(self) -> bool:
        """ Get: AllowResize(self: DataListDesigner) -> bool """
        ...

    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: DataListDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplatesExist(self):
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: DataListDesigner) -> str """
        ...

    def GetTemplateContainerDataItemProperty(self, templateName:str) -> str:
        """ GetTemplateContainerDataItemProperty(self: DataListDesigner, templateName: str) -> str """
        ...

    def GetTemplateContent(self, editingFrame, templateName, allowEditing) -> Tuple_[str, bool]:
        """ GetTemplateContent(self: DataListDesigner, editingFrame: ITemplateEditingFrame, templateName: str) -> (str, bool) """
        ...

    def SetTemplateContent(self, editingFrame, templateName:str, templateContent:str): # ->  # Not found arg types: {'editingFrame': 'ITemplateEditingFrame'}
        """ SetTemplateContent(self: DataListDesigner, editingFrame: ITemplateEditingFrame, templateName: str, templateContent: str) """
        ...


class DataPagerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ DataPagerDesigner() """
    @property
    def PagedControlID(self) -> str:
        """
        Get: PagedControlID(self: DataPagerDesigner) -> str
        Set: PagedControlID(self: DataPagerDesigner) = value
        """
        ...



class DataPagerFieldTypeEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ DataPagerFieldTypeEditor() """
    pass

class DataProviderNameConverter(StringConverter): # skipped bases: <type 'object'>
    """ DataProviderNameConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: DataProviderNameConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: DataProviderNameConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: DataProviderNameConverter, context: ITypeDescriptorContext) -> bool """
        ...


class DataSourceIDConverter(TypeConverter): # skipped bases: <type 'object'>
    """ DataSourceIDConverter() """
    def IsValidDataSource(self, *args): #cannot find CLR method
        """ IsValidDataSource(self: DataSourceIDConverter, component: IComponent) -> bool """
        ...


class DetailsViewDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ DetailsViewDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: DetailsViewDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: DetailsViewDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions = ...) -> str: # Not found arg types: {'regions': 'DesignerRegionCollection'}
        """
        GetDesignTimeHtml(self: DetailsViewDesigner) -> str
        GetDesignTimeHtml(self: DetailsViewDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: DetailsViewDesigner, region: EditableDesignerRegion) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: DetailsViewDesigner, component: IComponent) """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: DetailsViewDesigner, region: EditableDesignerRegion, content: str) """
        ...


class EmbeddedMailObjectCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ EmbeddedMailObjectCollectionEditor(type: Type) """
    pass

class EntityDataSourceDesigner(DataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'IDataSourceDesigner'>, <type 'object'>
    """ EntityDataSourceDesigner() """
    @property
    def CommandText(self) -> str:
        """
        Get: CommandText(self: EntityDataSourceDesigner) -> str
        Set: CommandText(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: EntityDataSourceDesigner) -> str
        Set: ConnectionString(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def DefaultContainerName(self) -> str:
        """
        Get: DefaultContainerName(self: EntityDataSourceDesigner) -> str
        Set: DefaultContainerName(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def EntitySetName(self) -> str:
        """
        Get: EntitySetName(self: EntityDataSourceDesigner) -> str
        Set: EntitySetName(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def EntityTypeFilter(self) -> str:
        """
        Get: EntityTypeFilter(self: EntityDataSourceDesigner) -> str
        Set: EntityTypeFilter(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def OrderBy(self) -> str:
        """
        Get: OrderBy(self: EntityDataSourceDesigner) -> str
        Set: OrderBy(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def Select(self) -> str:
        """
        Get: Select(self: EntityDataSourceDesigner) -> str
        Set: Select(self: EntityDataSourceDesigner) = value
        """
        ...

    @property
    def Where(self) -> str:
        """
        Get: Where(self: EntityDataSourceDesigner) -> str
        Set: Where(self: EntityDataSourceDesigner) = value
        """
        ...


    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: EntityDataSourceDesigner, component: IComponent) """
        ...


class EntityDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ EntityDesignerDataSourceView(owner: EntityDataSourceDesigner) """
    pass

class FormViewDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ FormViewDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: FormViewDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: FormViewDesigner) -> bool
        Set: RenderOuterTable(self: FormViewDesigner) = value
        """
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: FormViewDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: FormViewDesigner) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: FormViewDesigner, component: IComponent) """
        ...


class GridViewDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ GridViewDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: GridViewDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: GridViewDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions = ...) -> str: # Not found arg types: {'regions': 'DesignerRegionCollection'}
        """
        GetDesignTimeHtml(self: GridViewDesigner) -> str
        GetDesignTimeHtml(self: GridViewDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: GridViewDesigner, region: EditableDesignerRegion) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: GridViewDesigner, component: IComponent) """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: GridViewDesigner, region: EditableDesignerRegion, content: str) """
        ...


class HiddenFieldDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HiddenFieldDesigner() """
    pass

class HierarchicalDataBoundControlDesigner(BaseDataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HierarchicalDataBoundControlDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: HierarchicalDataBoundControlDesigner) -> DesignerActionListCollection """
        ...

    @property
    def DataSourceDesigner(self): # -> IHierarchicalDataSourceDesigner
        """ Get: DataSourceDesigner(self: HierarchicalDataBoundControlDesigner) -> IHierarchicalDataSourceDesigner """
        ...

    @property
    def DesignerView(self): # -> DesignerHierarchicalDataSourceView
        """ Get: DesignerView(self: HierarchicalDataBoundControlDesigner) -> DesignerHierarchicalDataSourceView """
        ...

    @property
    def UseDataSourcePickerActionList(self):
        ...


    def GetDesignTimeDataSource(self, *args): #cannot find CLR method
        """ GetDesignTimeDataSource(self: HierarchicalDataBoundControlDesigner) -> IHierarchicalEnumerable """
        ...

    def GetSampleDataSource(self, *args): #cannot find CLR method
        """ GetSampleDataSource(self: HierarchicalDataBoundControlDesigner) -> IHierarchicalEnumerable """
        ...


class HierarchicalDataSourceIDConverter(DataSourceIDConverter): # skipped bases: <type 'object'>
    """ HierarchicalDataSourceIDConverter() """
    pass

class HotSpotCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ HotSpotCollectionEditor(type: Type) """
    pass

class HyperLinkDesigner(TextControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ HyperLinkDesigner() """
    def OnComponentChanged(self, sender:object, ce:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: HyperLinkDesigner, sender: object, ce: ComponentChangedEventArgs) """
        ...


class LabelDesigner(TextControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LabelDesigner() """
    def OnComponentChanged(self, sender:object, ce:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: LabelDesigner, sender: object, ce: ComponentChangedEventArgs) """
        ...


class LinkButtonDesigner(TextControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LinkButtonDesigner() """
    pass

class LinqDataSourceDesigner(DataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'IDataSourceDesigner'>, <type 'object'>
    """ LinqDataSourceDesigner() """
    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: LinqDataSourceDesigner) -> str
        Set: ContextTypeName(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def Delete(self) -> str:
        """
        Get: Delete(self: LinqDataSourceDesigner) -> str
        Set: Delete(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def EnableDelete(self) -> bool:
        """
        Get: EnableDelete(self: LinqDataSourceDesigner) -> bool
        Set: EnableDelete(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def EnableInsert(self) -> bool:
        """
        Get: EnableInsert(self: LinqDataSourceDesigner) -> bool
        Set: EnableInsert(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def EnableUpdate(self) -> bool:
        """
        Get: EnableUpdate(self: LinqDataSourceDesigner) -> bool
        Set: EnableUpdate(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def GroupBy(self) -> str:
        """
        Get: GroupBy(self: LinqDataSourceDesigner) -> str
        Set: GroupBy(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def Insert(self) -> str:
        """
        Get: Insert(self: LinqDataSourceDesigner) -> str
        Set: Insert(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def OrderBy(self) -> str:
        """
        Get: OrderBy(self: LinqDataSourceDesigner) -> str
        Set: OrderBy(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def OrderGroupsBy(self) -> str:
        """
        Get: OrderGroupsBy(self: LinqDataSourceDesigner) -> str
        Set: OrderGroupsBy(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def Select(self) -> str:
        """
        Get: Select(self: LinqDataSourceDesigner) -> str
        Set: Select(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def ServiceProvider(self) -> IServiceProvider:
        """ Get: ServiceProvider(self: LinqDataSourceDesigner) -> IServiceProvider """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: LinqDataSourceDesigner) -> str
        Set: TableName(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def Update(self) -> str:
        """
        Get: Update(self: LinqDataSourceDesigner) -> str
        Set: Update(self: LinqDataSourceDesigner) = value
        """
        ...

    @property
    def Where(self) -> str:
        """
        Get: Where(self: LinqDataSourceDesigner) -> str
        Set: Where(self: LinqDataSourceDesigner) = value
        """
        ...


    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: LinqDataSourceDesigner, component: IComponent) """
        ...


class LinqDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ LinqDesignerDataSourceView(owner: LinqDataSourceDesigner) """
    @property
    def IsDataContext(self) -> bool:
        """ Get: IsDataContext(self: LinqDesignerDataSourceView) -> bool """
        ...

    @property
    def IsTableTypeTable(self) -> bool:
        """ Get: IsTableTypeTable(self: LinqDesignerDataSourceView) -> bool """
        ...



class ListControlDataBindingHandler(DataBindingHandler): # skipped bases: <type 'object'>
    """ ListControlDataBindingHandler() """
    pass

class ListItemsCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ ListItemsCollectionEditor(type: Type) """
    pass

class ListViewDesigner(DataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IDataSourceProvider'>, <type 'ITreeDesigner'>, <type 'IDataBindingSchemaProvider'>, <type 'IDesignerFilter'>, <type 'object'>
    """ ListViewDesigner() """
    def GetDesignTimeHtml(self, regions = ...) -> str: # Not found arg types: {'regions': 'DesignerRegionCollection'}
        """
        GetDesignTimeHtml(self: ListViewDesigner) -> str
        GetDesignTimeHtml(self: ListViewDesigner, regions: DesignerRegionCollection) -> str
        """
        ...

    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: ListViewDesigner, region: EditableDesignerRegion) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: ListViewDesigner, component: IComponent) """
        ...

    def OnComponentChanged(self, sender:object, ce:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: ListViewDesigner, sender: object, ce: ComponentChangedEventArgs) """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: ListViewDesigner, region: EditableDesignerRegion, content: str) """
        ...


class LiteralDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LiteralDesigner() """
    pass

class LoginDesigner(CompositeControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LoginDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: LoginDesigner) -> DesignerActionListCollection """
        ...

    @property
    def AllowResize(self) -> bool:
        """ Get: AllowResize(self: LoginDesigner) -> bool """
        ...

    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: LoginDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: LoginDesigner) -> bool
        Set: RenderOuterTable(self: LoginDesigner) = value
        """
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: LoginDesigner) -> TemplateGroupCollection """
        ...


    def GetEditableDesignerRegionContent(self, region) -> str: # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ GetEditableDesignerRegionContent(self: LoginDesigner, region: EditableDesignerRegion) -> str """
        ...

    def SetEditableDesignerRegionContent(self, region, content:str): # ->  # Not found arg types: {'region': 'EditableDesignerRegion'}
        """ SetEditableDesignerRegionContent(self: LoginDesigner, region: EditableDesignerRegion, content: str) """
        ...


class LoginNameDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LoginNameDesigner() """
    pass

class LoginStatusDesigner(CompositeControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LoginStatusDesigner() """
    @property
    def ActionLists(self): # -> DesignerActionListCollection
        """ Get: ActionLists(self: LoginStatusDesigner) -> DesignerActionListCollection """
        ...



class LoginViewDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ LoginViewDesigner() """
    pass

class MailDefinitionBodyFileNameEditor(UrlEditor): # skipped bases: <type 'object'>
    """ MailDefinitionBodyFileNameEditor() """
    pass

class MenuBindingsEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ MenuBindingsEditor() """
    pass

class MenuDesigner(IDataBindingSchemaProvider, HierarchicalDataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ MenuDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: MenuDesigner) -> DesignerAutoFormatCollection """
        ...

    @property
    def TemplateGroups(self): # -> TemplateGroupCollection
        """ Get: TemplateGroups(self: MenuDesigner) -> TemplateGroupCollection """
        ...


    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: MenuDesigner) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: MenuDesigner, component: IComponent) """
        ...


class MenuItemCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ MenuItemCollectionEditor() """
    pass

class MenuItemStyleCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ MenuItemStyleCollectionEditor(type: Type) """
    pass

class MultiViewDesigner(ContainerControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ MultiViewDesigner() """
    pass

class ObjectDataSourceDesigner(DataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'IDataSourceDesigner'>, <type 'object'>
    """ ObjectDataSourceDesigner() """
    @property
    def SelectMethod(self) -> str:
        """
        Get: SelectMethod(self: ObjectDataSourceDesigner) -> str
        Set: SelectMethod(self: ObjectDataSourceDesigner) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ObjectDataSourceDesigner) -> str
        Set: TypeName(self: ObjectDataSourceDesigner) = value
        """
        ...



class ObjectDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ ObjectDesignerDataSourceView(owner: ObjectDataSourceDesigner, viewName: str) """
    pass

class PanelContainerDesigner(ContainerControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ PanelContainerDesigner() """
    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: PanelContainerDesigner, component: IComponent) """
        ...


class PanelDesigner(ReadWriteControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ PanelDesigner() """
    pass

class ParameterCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ ParameterCollectionEditor() """
    pass

class ParameterEditorUserControl(UserControl): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ParameterEditorUserControl(serviceProvider: IServiceProvider) """
    @property
    def ParametersConfigured(self) -> bool:
        """ Get: ParametersConfigured(self: ParameterEditorUserControl) -> bool """
        ...

    @property
    def TypeDescriptionProvider(self) -> TypeDescriptionProvider:
        """ Get: TypeDescriptionProvider(self: ParameterEditorUserControl) -> TypeDescriptionProvider """
        ...


    def AddParameters(self, parameters:Array): # -> 
        """ AddParameters(self: ParameterEditorUserControl, parameters: Array[Parameter]) """
        ...

    def ClearParameters(self): # -> 
        """ ClearParameters(self: ParameterEditorUserControl) """
        ...

    def GetParameters(self) -> Array:
        """ GetParameters(self: ParameterEditorUserControl) -> Array[Parameter] """
        ...

    def OnParametersChanged(self, *args): #cannot find CLR method
        """ OnParametersChanged(self: ParameterEditorUserControl, sender: object, e: EventArgs) """
        ...

    def SetAllowCollectionChanges(self, allowChanges:bool): # -> 
        """ SetAllowCollectionChanges(self: ParameterEditorUserControl, allowChanges: bool) """
        ...

    def __new__(cls, serviceProvider:IServiceProvider) -> Self:
        """ __new__(cls: type, serviceProvider: IServiceProvider) """
        ...

    ParametersChanged = ...


class PasswordRecoveryDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ PasswordRecoveryDesigner() """
    @property
    def RenderOuterTable(self) -> bool:
        """
        Get: RenderOuterTable(self: PasswordRecoveryDesigner) -> bool
        Set: RenderOuterTable(self: PasswordRecoveryDesigner) = value
        """
        ...



class RegexEditorDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ RegexEditorDialog(site: ISite) """
    @property
    def RegularExpression(self) -> str:
        """
        Get: RegularExpression(self: RegexEditorDialog) -> str
        Set: RegularExpression(self: RegexEditorDialog) = value
        """
        ...


    def cmdHelp_Click(self, *args): #cannot find CLR method
        """ cmdHelp_Click(self: RegexEditorDialog, sender: object, e: EventArgs) """
        ...

    def cmdOK_Click(self, *args): #cannot find CLR method
        """ cmdOK_Click(self: RegexEditorDialog, sender: object, e: EventArgs) """
        ...

    def cmdTestValidate_Click(self, *args): #cannot find CLR method
        """ cmdTestValidate_Click(self: RegexEditorDialog, sender: object, args: EventArgs) """
        ...

    def lstStandardExpressions_SelectedIndexChanged(self, *args): #cannot find CLR method
        """ lstStandardExpressions_SelectedIndexChanged(self: RegexEditorDialog, sender: object, e: EventArgs) """
        ...

    def RegexTypeEditor_Activated(self, *args): #cannot find CLR method
        """ RegexTypeEditor_Activated(self: RegexEditorDialog, sender: object, e: EventArgs) """
        ...

    def txtExpression_TextChanged(self, *args): #cannot find CLR method
        """ txtExpression_TextChanged(self: RegexEditorDialog, sender: object, e: EventArgs) """
        ...

    def __new__(cls, site:ISite) -> Self:
        """ __new__(cls: type, site: ISite) """
        ...


class RegexTypeEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ RegexTypeEditor() """
    pass

class RepeaterDesigner(ControlDesigner, IDataSourceProvider): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ RepeaterDesigner() """
    @property
    def DataMember(self) -> str:
        """
        Get: DataMember(self: RepeaterDesigner) -> str
        Set: DataMember(self: RepeaterDesigner) = value
        """
        ...

    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: RepeaterDesigner) -> str
        Set: DataSource(self: RepeaterDesigner) = value
        """
        ...

    @property
    def DataSourceDesigner(self): # -> IDataSourceDesigner
        """ Get: DataSourceDesigner(self: RepeaterDesigner) -> IDataSourceDesigner """
        ...

    @property
    def DataSourceID(self) -> str:
        """
        Get: DataSourceID(self: RepeaterDesigner) -> str
        Set: DataSourceID(self: RepeaterDesigner) = value
        """
        ...

    @property
    def DesignerView(self): # -> DesignerDataSourceView
        """ Get: DesignerView(self: RepeaterDesigner) -> DesignerDataSourceView """
        ...

    @property
    def TemplatesExist(self):
        ...


    def ExecuteChooseDataSourcePostSteps(self, *args): #cannot find CLR method
        """ ExecuteChooseDataSourcePostSteps(self: RepeaterDesigner) """
        ...

    def GetDesignTimeDataSource(self, *args): #cannot find CLR method
        """
        GetDesignTimeDataSource(self: RepeaterDesigner, minimumRows: int) -> IEnumerable
        GetDesignTimeDataSource(self: RepeaterDesigner, selectedDataSource: IEnumerable, minimumRows: int) -> IEnumerable
        """
        ...

    def OnDataSourceChanged(self): # -> 
        """ OnDataSourceChanged(self: RepeaterDesigner) """
        ...


class RoleGroupCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ RoleGroupCollectionEditor(type: Type) """
    pass

class SiteMapDataSourceDesigner(HierarchicalDataSourceDesigner, IDataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IHierarchicalDataSourceDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'object'>
    """ SiteMapDataSourceDesigner() """
    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: SiteMapDataSourceDesigner, component: IComponent) """
        ...

    def OnComponentChanged(self, sender:object, e:ComponentChangedEventArgs): # -> 
        """ OnComponentChanged(self: SiteMapDataSourceDesigner, sender: object, e: ComponentChangedEventArgs) """
        ...


class SiteMapDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ SiteMapDesignerDataSourceView(owner: SiteMapDataSourceDesigner, viewName: str) """
    pass

class SiteMapDesignerHierarchicalDataSourceView(DesignerHierarchicalDataSourceView): # skipped bases: <type 'object'>
    """ SiteMapDesignerHierarchicalDataSourceView(owner: SiteMapDataSourceDesigner, viewPath: str) """
    pass

class SiteMapPathDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ SiteMapPathDesigner() """
    pass

class SqlDataSourceConnectionStringEditor(ConnectionStringEditor): # skipped bases: <type 'object'>
    """ SqlDataSourceConnectionStringEditor() """
    pass

class SqlDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ SqlDesignerDataSourceView(owner: SqlDataSourceDesigner, viewName: str) """
    pass

class StyleCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ StyleCollectionEditor(type: Type) """
    pass

class SubMenuStyleCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ SubMenuStyleCollectionEditor(type: Type) """
    pass

class SubstitutionDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ SubstitutionDesigner() """
    pass

class TableCellsCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ TableCellsCollectionEditor(type: Type) """
    pass

class TableDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ TableDesigner() """
    pass

class TableRowsCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ TableRowsCollectionEditor(type: Type) """
    pass

class TreeNodeBindingDepthConverter(Int32Converter): # skipped bases: <type 'object'>
    """ TreeNodeBindingDepthConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: TreeNodeBindingDepthConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: TreeNodeBindingDepthConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        ...


class TreeNodeCollectionEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ TreeNodeCollectionEditor() """
    pass

class TreeNodeStyleCollectionEditor(StyleCollectionEditor): # skipped bases: <type 'object'>
    """ TreeNodeStyleCollectionEditor(type: Type) """
    pass

class TreeViewBindingsEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ TreeViewBindingsEditor() """
    pass

class TreeViewDesigner(HierarchicalDataBoundControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ TreeViewDesigner() """
    @property
    def AutoFormats(self): # -> DesignerAutoFormatCollection
        """ Get: AutoFormats(self: TreeViewDesigner) -> DesignerAutoFormatCollection """
        ...


    def CreateLineImages(self, *args): #cannot find CLR method
        """ CreateLineImages(self: TreeViewDesigner) """
        ...

    def EditBindings(self, *args): #cannot find CLR method
        """ EditBindings(self: TreeViewDesigner) """
        ...

    def EditNodes(self, *args): #cannot find CLR method
        """ EditNodes(self: TreeViewDesigner) """
        ...

    def GetDesignTimeHtml(self, regions=None) -> str:
        """ GetDesignTimeHtml(self: TreeViewDesigner) -> str """
        ...

    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: TreeViewDesigner, component: IComponent) """
        ...


class ValidationSummaryDesigner(PreviewControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ValidationSummaryDesigner() """
    pass

class ViewDesigner(ContainerControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ViewDesigner() """
    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: ViewDesigner, component: IComponent) """
        ...


class WizardStepEditableRegion(EditableDesignerRegion, IWizardStepEditableRegion): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ WizardStepEditableRegion(designer: WizardDesigner, wizardStep: WizardStepBase) """
    @property
    def Step(self): # -> WizardStepBase
        """ Get: Step(self: WizardStepEditableRegion) -> WizardStepBase """
        ...



class WizardStepTemplatedEditableRegion(IWizardStepEditableRegion, TemplatedEditableDesignerRegion): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ WizardStepTemplatedEditableRegion(templateDefinition: TemplateDefinition, wizardStep: WizardStepBase) """
    @property
    def Step(self): # -> WizardStepBase
        """ Get: Step(self: WizardStepTemplatedEditableRegion) -> WizardStepBase """
        ...



class XmlDataSourceDesigner(HierarchicalDataSourceDesigner, IDataSourceDesigner): # skipped bases: <type 'IDisposable'>, <type 'IComponentInitializer'>, <type 'IDesigner'>, <type 'IHierarchicalDataSourceDesigner'>, <type 'ITreeDesigner'>, <type 'IDesignerFilter'>, <type 'object'>
    """ XmlDataSourceDesigner() """
    @property
    def Data(self) -> str:
        """
        Get: Data(self: XmlDataSourceDesigner) -> str
        Set: Data(self: XmlDataSourceDesigner) = value
        """
        ...

    @property
    def DataFile(self) -> str:
        """
        Get: DataFile(self: XmlDataSourceDesigner) -> str
        Set: DataFile(self: XmlDataSourceDesigner) = value
        """
        ...

    @property
    def Transform(self) -> str:
        """
        Get: Transform(self: XmlDataSourceDesigner) -> str
        Set: Transform(self: XmlDataSourceDesigner) = value
        """
        ...

    @property
    def TransformFile(self) -> str:
        """
        Get: TransformFile(self: XmlDataSourceDesigner) -> str
        Set: TransformFile(self: XmlDataSourceDesigner) = value
        """
        ...

    @property
    def XPath(self) -> str:
        """
        Get: XPath(self: XmlDataSourceDesigner) -> str
        Set: XPath(self: XmlDataSourceDesigner) = value
        """
        ...


    def Initialize(self, component:IComponent): # -> 
        """ Initialize(self: XmlDataSourceDesigner, component: IComponent) """
        ...


class XmlDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ XmlDesigner() """
    pass

class XmlDesignerDataSourceView(DesignerDataSourceView): # skipped bases: <type 'object'>
    """ XmlDesignerDataSourceView(owner: XmlDataSourceDesigner, viewName: str) """
    pass

class XmlDesignerHierarchicalDataSourceView(DesignerHierarchicalDataSourceView): # skipped bases: <type 'object'>
    """ XmlDesignerHierarchicalDataSourceView(owner: XmlDataSourceDesigner, viewPath: str) """
    pass

# variables with complex values

