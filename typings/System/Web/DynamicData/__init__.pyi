# encoding: utf-8
# module System.Web.DynamicData calls itself DynamicData
# from System.Web.DynamicData.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import Parameter

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    ParameterCollection)

from Microsoft.VisualBasic import Collection

from System import Attribute, Enum, EventArgs, Type, TypeCode

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.Generic import List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import AttributeCollection

from System.ComponentModel.DataAnnotations import DataTypeAttribute

from System.Data.Linq.Mapping import MetaModel, MetaTable

from System.Linq import IQueryable

from System.Management.Automation import ListControl

from System.Reflection import PropertyInfo

from System.Security.Principal import IPrincipal

from System.Web import HttpContext, IHttpHandler

from System.Web.DynamicData.ModelProviders import (ColumnProvider, 
    TableProvider)

from System.Web.Routing import (IRouteHandler, RequestContext, Route, 
    RouteData)

from System.Web.UI import (Control, IAttributeAccessor, IAutoFieldGenerator, 
    IBindableControl, IDataSource, INamingContainer, ITemplate, UserControl)

from System.Web.UI.MobileControls import BaseValidator

from System.Web.UI.WebControls import IQueryableDataSource, LinqDataSource

from System.Web.UI.WebControls.Expressions import DataSourceExpression

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BaseDataBoundControl, 
    BoundEvent, DataBoundControlMode, DataControlField, DataKey, 
    DynamicDataManager, EntityTemplateUserControl, Func, HyperLink, 
    IDynamicDataSource, IFieldTemplateFactory, IMetaChildrenColumn, 
    IMetaColumn, IMetaForeignKeyColumn, IMetaModel, IMetaTable, 
    MetaChildrenColumn, MetaColumn, MetaForeignKeyColumn, 
    QueryableFilterUserControl, Repeater, field#)
"""

# no functions
# classes

class ContainerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContainerType, values: Item (1), List (0) """
    Item: ContainerType = ...
    List: ContainerType = ...
    value__ = ...


class ContextConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ ContextConfiguration() """
    @property
    def MetadataProviderFactory(self): # -> Func
        """
        Get: MetadataProviderFactory(self: ContextConfiguration) -> Func[Type, TypeDescriptionProvider]
        Set: MetadataProviderFactory(self: ContextConfiguration) = value
        """
        ...

    @property
    def ScaffoldAllTables(self) -> bool:
        """
        Get: ScaffoldAllTables(self: ContextConfiguration) -> bool
        Set: ScaffoldAllTables(self: ContextConfiguration) = value
        """
        ...



class ControlFilterExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ ControlFilterExpression() """
    @property
    def Column(self) -> str:
        """
        Get: Column(self: ControlFilterExpression) -> str
        Set: Column(self: ControlFilterExpression) = value
        """
        ...

    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: ControlFilterExpression) -> str
        Set: ControlID(self: ControlFilterExpression) = value
        """
        ...



class DataControlReference: # skipped bases: <type 'object'>, <type 'object'>
    """ DataControlReference() """
    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: DataControlReference) -> str
        Set: ControlID(self: DataControlReference) = value
        """
        ...

    @property
    def Owner(self): # -> DynamicDataManager
        """ Get: Owner(self: DataControlReference) -> DynamicDataManager """
        ...


    def ToString(self) -> str:
        """ ToString(self: DataControlReference) -> str """
        ...


class DataControlReferenceCollection(Collection): # skipped bases: <type 'IEnumerable[DataControlReference]'>, <type 'IReadOnlyCollection[DataControlReference]'>, <type 'IReadOnlyList[DataControlReference]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[DataControlReference]'>, <type 'ICollection'>, <type 'ICollection[DataControlReference]'>, <type 'object'>
    """ DataControlReferenceCollection(owner: DynamicDataManager) """
    @property
    def Owner(self): # -> DynamicDataManager
        """ Get: Owner(self: DataControlReferenceCollection) -> DynamicDataManager """
        ...



class DefaultAutoFieldGenerator(IAutoFieldGenerator): # skipped bases: <type 'object'>
    """ DefaultAutoFieldGenerator(table: MetaTable) """
    def CreateField(self, *args): #cannot find CLR method
        """ CreateField(self: DefaultAutoFieldGenerator, column: MetaColumn, containerType: ContainerType, mode: DataBoundControlMode) -> DynamicField """
        ...


class IFieldFormattingOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplyFormatInEditMode(self) -> bool:
        """ Get: ApplyFormatInEditMode(self: IFieldFormattingOptions) -> bool """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """ Get: ConvertEmptyStringToNull(self: IFieldFormattingOptions) -> bool """
        ...

    @property
    def DataFormatString(self) -> str:
        """ Get: DataFormatString(self: IFieldFormattingOptions) -> str """
        ...

    @property
    def HtmlEncode(self) -> bool:
        """ Get: HtmlEncode(self: IFieldFormattingOptions) -> bool """
        ...

    @property
    def NullDisplayText(self) -> str:
        """ Get: NullDisplayText(self: IFieldFormattingOptions) -> str """
        ...



class IFieldTemplateHost: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Column(self): # -> MetaColumn
        """ Get: Column(self: IFieldTemplateHost) -> MetaColumn """
        ...

    @property
    def FormattingOptions(self) -> IFieldFormattingOptions:
        """ Get: FormattingOptions(self: IFieldTemplateHost) -> IFieldFormattingOptions """
        ...

    @property
    def Mode(self): # -> DataBoundControlMode
        """ Get: Mode(self: IFieldTemplateHost) -> DataBoundControlMode """
        ...

    @property
    def ValidationGroup(self) -> str:
        """ Get: ValidationGroup(self: IFieldTemplateHost) -> str """
        ...



class DynamicControl(IAttributeAccessor, IFieldFormattingOptions, Control, IFieldTemplateHost): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    DynamicControl()
    DynamicControl(mode: DataBoundControlMode)
    """
    @property
    def CssClass(self) -> str:
        """
        Get: CssClass(self: DynamicControl) -> str
        Set: CssClass(self: DynamicControl) = value
        """
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: DynamicControl) -> str
        Set: DataField(self: DynamicControl) = value
        """
        ...

    @property
    def FieldTemplate(self) -> Control:
        """ Get: FieldTemplate(self: DynamicControl) -> Control """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: DynamicControl) -> MetaTable """
        ...

    @property
    def UIHint(self) -> str:
        """
        Get: UIHint(self: DynamicControl) -> str
        Set: UIHint(self: DynamicControl) = value
        """
        ...


    def __new__(cls, mode = ...) -> Self: # Not found arg types: {'mode': 'DataBoundControlMode'}
        """
        __new__(cls: type)
        __new__(cls: type, mode: DataBoundControlMode)
        """
        ...


class IWhereParametersProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetWhereParameters(self, dataSource) -> IEnumerable: # Not found arg types: {'dataSource': 'IDynamicDataSource'}
        """ GetWhereParameters(self: IWhereParametersProvider, dataSource: IDynamicDataSource) -> IEnumerable[Parameter] """
        ...


class DynamicControlParameter(IWhereParametersProvider, Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """
    DynamicControlParameter()
    DynamicControlParameter(controlId: str)
    """
    @property
    def ControlId(self) -> str:
        """
        Get: ControlId(self: DynamicControlParameter) -> str
        Set: ControlId(self: DynamicControlParameter) = value
        """
        ...



class DynamicDataExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ConvertEditedValue(formattingOptions:IFieldFormattingOptions, value:str) -> object:
        """ ConvertEditedValue(formattingOptions: IFieldFormattingOptions, value: str) -> object """
        ...

    @staticmethod
    def EnablePersistedSelection(dataBoundControl): # ->  # Not found arg types: {'dataBoundControl': 'BaseDataBoundControl'}
        """ EnablePersistedSelection(dataBoundControl: BaseDataBoundControl) """
        ...

    @staticmethod
    def ExpandDynamicWhereParameters(dataSource): # ->  # Not found arg types: {'dataSource': 'IDynamicDataSource'}
        """ ExpandDynamicWhereParameters(dataSource: IDynamicDataSource) """
        ...

    @staticmethod
    def FindDataSourceControl(current:Control): # -> IDynamicDataSource
        """ FindDataSourceControl(current: Control) -> IDynamicDataSource """
        ...

    @staticmethod
    def FindFieldTemplate(control:Control, columnName:str) -> Control:
        """ FindFieldTemplate(control: Control, columnName: str) -> Control """
        ...

    @staticmethod
    def FindMetaTable(current:Control) -> MetaTable:
        """ FindMetaTable(current: Control) -> MetaTable """
        ...

    @staticmethod
    def FormatEditValue(formattingOptions:IFieldFormattingOptions, fieldValue:object) -> str:
        """ FormatEditValue(formattingOptions: IFieldFormattingOptions, fieldValue: object) -> str """
        ...

    @staticmethod
    def FormatValue(formattingOptions:IFieldFormattingOptions, fieldValue:object) -> str:
        """ FormatValue(formattingOptions: IFieldFormattingOptions, fieldValue: object) -> str """
        ...

    @staticmethod
    def GetDefaultValues(*__args:IDataSource) -> IDictionary:
        """
        GetDefaultValues(dataSource: IDataSource) -> IDictionary[str, object]
        GetDefaultValues(control: INamingContainer) -> IDictionary[str, object]
        """
        ...

    @staticmethod
    def GetEnumType(column) -> Type: # Not found arg types: {'column': 'MetaColumn'}
        """ GetEnumType(column: MetaColumn) -> Type """
        ...

    @staticmethod
    def GetMetaTable(*__args:IDataSource) -> MetaTable:
        """
        GetMetaTable(dataSource: IDataSource) -> MetaTable
        GetMetaTable(control: INamingContainer) -> MetaTable
        """
        ...

    @staticmethod
    def GetTable(dataSource) -> MetaTable: # Not found arg types: {'dataSource': 'IDynamicDataSource'}
        """ GetTable(dataSource: IDynamicDataSource) -> MetaTable """
        ...

    @staticmethod
    def LoadWith(dataSource:LinqDataSource): # -> 
        """ LoadWith[TEntity](dataSource: LinqDataSource) """
        ...

    @staticmethod
    def LoadWithForeignKeys(dataSource:LinqDataSource, rowType:Type): # -> 
        """ LoadWithForeignKeys(dataSource: LinqDataSource, rowType: Type) """
        ...

    @staticmethod
    def SetMetaTable(control:INamingContainer, table:MetaTable, defaultValues:IDictionary = ...): # -> 
        """ SetMetaTable(control: INamingContainer, table: MetaTable)SetMetaTable(control: INamingContainer, table: MetaTable, defaultValues: IDictionary[str, object])SetMetaTable(control: INamingContainer, table: MetaTable, defaultValues: object) """
        ...

    @staticmethod
    def TryGetMetaTable(*__args:IDataSource) -> Tuple_[bool, MetaTable]:
        """
        TryGetMetaTable(dataSource: IDataSource) -> (bool, MetaTable)
        TryGetMetaTable(control: INamingContainer) -> (bool, MetaTable)
        """
        ...

    __all__: list = ...


class DynamicDataManager(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DynamicDataManager() """
    @property
    def AutoLoadForeignKeys(self) -> bool:
        """
        Get: AutoLoadForeignKeys(self: DynamicDataManager) -> bool
        Set: AutoLoadForeignKeys(self: DynamicDataManager) = value
        """
        ...

    @property
    def DataControls(self) -> DataControlReferenceCollection:
        """ Get: DataControls(self: DynamicDataManager) -> DataControlReferenceCollection """
        ...


    def RegisterControl(self, control:Control, setSelectionFromUrl:bool = ...): # -> 
        """ RegisterControl(self: DynamicDataManager, control: Control)RegisterControl(self: DynamicDataManager, control: Control, setSelectionFromUrl: bool) """
        ...


class DynamicDataRoute(Route): # skipped bases: <type 'object'>
    """ DynamicDataRoute(url: str) """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: DynamicDataRoute) -> str
        Set: Action(self: DynamicDataRoute) = value
        """
        ...

    @property
    def Model(self) -> MetaModel:
        """
        Get: Model(self: DynamicDataRoute) -> MetaModel
        Set: Model(self: DynamicDataRoute) = value
        """
        ...

    @property
    def Table(self) -> str:
        """
        Get: Table(self: DynamicDataRoute) -> str
        Set: Table(self: DynamicDataRoute) = value
        """
        ...

    @property
    def ViewName(self) -> str:
        """
        Get: ViewName(self: DynamicDataRoute) -> str
        Set: ViewName(self: DynamicDataRoute) = value
        """
        ...


    def GetActionFromRouteData(self, routeData:RouteData) -> str:
        """ GetActionFromRouteData(self: DynamicDataRoute, routeData: RouteData) -> str """
        ...

    def GetTableFromRouteData(self, routeData:RouteData) -> MetaTable:
        """ GetTableFromRouteData(self: DynamicDataRoute, routeData: RouteData) -> MetaTable """
        ...


class DynamicDataRouteHandler(IRouteHandler): # skipped bases: <type 'object'>
    """ DynamicDataRouteHandler() """
    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: DynamicDataRouteHandler) -> MetaModel """
        ...


    def CreateHandler(self, route:DynamicDataRoute, table:MetaTable, action:str) -> IHttpHandler:
        """ CreateHandler(self: DynamicDataRouteHandler, route: DynamicDataRoute, table: MetaTable, action: str) -> IHttpHandler """
        ...

    def GetCustomPageVirtualPath(self, *args): #cannot find CLR method
        """ GetCustomPageVirtualPath(self: DynamicDataRouteHandler, table: MetaTable, viewName: str) -> str """
        ...

    @staticmethod
    def GetRequestContext(httpContext:HttpContext) -> RequestContext:
        """ GetRequestContext(httpContext: HttpContext) -> RequestContext """
        ...

    @staticmethod
    def GetRequestMetaTable(httpContext:HttpContext) -> MetaTable:
        """ GetRequestMetaTable(httpContext: HttpContext) -> MetaTable """
        ...

    def GetScaffoldPageVirtualPath(self, *args): #cannot find CLR method
        """ GetScaffoldPageVirtualPath(self: DynamicDataRouteHandler, table: MetaTable, viewName: str) -> str """
        ...

    @staticmethod
    def SetRequestMetaTable(httpContext:HttpContext, table:MetaTable): # -> 
        """ SetRequestMetaTable(httpContext: HttpContext, table: MetaTable) """
        ...


class DynamicDataSourceOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DynamicDataSourceOperation, values: ContextCreate (4), Delete (0), Insert (1), Select (2), Update (3) """
    ContextCreate: DynamicDataSourceOperation = ...
    Delete: DynamicDataSourceOperation = ...
    Insert: DynamicDataSourceOperation = ...
    Select: DynamicDataSourceOperation = ...
    Update: DynamicDataSourceOperation = ...
    value__ = ...


class DynamicEntity(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DynamicEntity() """
    @property
    def Mode(self): # -> DataBoundControlMode
        """
        Get: Mode(self: DynamicEntity) -> DataBoundControlMode
        Set: Mode(self: DynamicEntity) = value
        """
        ...

    @property
    def UIHint(self) -> str:
        """
        Get: UIHint(self: DynamicEntity) -> str
        Set: UIHint(self: DynamicEntity) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: DynamicEntity) -> str
        Set: ValidationGroup(self: DynamicEntity) = value
        """
        ...



class DynamicField(IAttributeAccessor, DataControlField, IFieldFormattingOptions): # skipped bases: <type 'IStateManager'>, <type 'IDataSourceViewSchemaAccessor'>, <type 'object'>
    """ DynamicField() """
    @property
    def Column(self):
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: DynamicField) -> str
        Set: DataField(self: DynamicField) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: DynamicField) -> bool
        Set: ReadOnly(self: DynamicField) = value
        """
        ...

    @property
    def UIHint(self) -> str:
        """
        Get: UIHint(self: DynamicField) -> str
        Set: UIHint(self: DynamicField) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: DynamicField) -> str
        Set: ValidationGroup(self: DynamicField) = value
        """
        ...


    def ConfigureDynamicControl(self, *args): #cannot find CLR method
        """ ConfigureDynamicControl(self: DynamicField, control: DynamicControl) """
        ...

    def CreateDynamicControl(self, *args): #cannot find CLR method
        """ CreateDynamicControl(self: DynamicField) -> DynamicControl """
        ...


class IFilterExpressionProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: IFilterExpressionProvider, source: IQueryable) -> IQueryable """
        ...

    def Initialize(self, dataSource:IQueryableDataSource): # -> 
        """ Initialize(self: IFilterExpressionProvider, dataSource: IQueryableDataSource) """
        ...


class DynamicFilter(IFilterExpressionProvider, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DynamicFilter() """
    @property
    def Column(self):
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: DynamicFilter) -> str
        Set: DataField(self: DynamicFilter) = value
        """
        ...

    @property
    def FilterTemplate(self) -> Control:
        """ Get: FilterTemplate(self: DynamicFilter) -> Control """
        ...

    @property
    def FilterUIHint(self) -> str:
        """
        Get: FilterUIHint(self: DynamicFilter) -> str
        Set: FilterUIHint(self: DynamicFilter) = value
        """
        ...


    FilterChanged = ...


class DynamicFilterExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ DynamicFilterExpression() """
    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: DynamicFilterExpression) -> str
        Set: ControlID(self: DynamicFilterExpression) = value
        """
        ...



class DynamicHyperLink(HyperLink): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DynamicHyperLink() """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: DynamicHyperLink) -> str
        Set: Action(self: DynamicHyperLink) = value
        """
        ...

    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: DynamicHyperLink) -> str
        Set: ContextTypeName(self: DynamicHyperLink) = value
        """
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: DynamicHyperLink) -> str
        Set: DataField(self: DynamicHyperLink) = value
        """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: DynamicHyperLink) -> str
        Set: TableName(self: DynamicHyperLink) = value
        """
        ...



class DynamicQueryStringParameter(IWhereParametersProvider, Parameter): # skipped bases: <type 'IStateManager'>, <type 'ICloneable'>, <type 'object'>
    """ DynamicQueryStringParameter() """
    pass

class DynamicRouteExpression(DataSourceExpression): # skipped bases: <type 'IStateManager'>, <type 'object'>
    """ DynamicRouteExpression() """
    @property
    def ColumnName(self) -> str:
        """
        Get: ColumnName(self: DynamicRouteExpression) -> str
        Set: ColumnName(self: DynamicRouteExpression) = value
        """
        ...



class DynamicValidator(BaseValidator): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'ITextControl'>, <type 'IValidator'>, <type 'object'>
    """ DynamicValidator() """
    @property
    def Column(self): # -> MetaColumn
        """
        Get: Column(self: DynamicValidator) -> MetaColumn
        Set: Column(self: DynamicValidator) = value
        """
        ...

    @property
    def ColumnName(self) -> str:
        """ Get: ColumnName(self: DynamicValidator) -> str """
        ...

    @property
    def ValidationException(self):
        ...


    def ValidateException(self, *args): #cannot find CLR method
        """ ValidateException(self: DynamicValidator, exception: Exception) """
        ...


class DynamicValidatorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DynamicValidatorEventArgs(exception: Exception, operation: DynamicDataSourceOperation) """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: DynamicValidatorEventArgs) -> Exception """
        ...

    @property
    def Operation(self) -> DynamicDataSourceOperation:
        """ Get: Operation(self: DynamicValidatorEventArgs) -> DynamicDataSourceOperation """
        ...


    def __new__(cls, exception:Exception, operation:DynamicDataSourceOperation) -> Self:
        """ __new__(cls: type, exception: Exception, operation: DynamicDataSourceOperation) """
        ...


class EntityTemplate(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ EntityTemplate() """
    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: EntityTemplate) -> ITemplate
        Set: ItemTemplate(self: EntityTemplate) = value
        """
        ...



class EntityTemplateFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ EntityTemplateFactory() """
    def BuildEntityTemplateVirtualPath(self, templateName:str, mode) -> str: # Not found arg types: {'mode': 'DataBoundControlMode'}
        """ BuildEntityTemplateVirtualPath(self: EntityTemplateFactory, templateName: str, mode: DataBoundControlMode) -> str """
        ...

    def CreateEntityTemplate(self, table:MetaTable, mode, uiHint:str): # -> EntityTemplateUserControl # Not found arg types: {'mode': 'DataBoundControlMode'}
        """ CreateEntityTemplate(self: EntityTemplateFactory, table: MetaTable, mode: DataBoundControlMode, uiHint: str) -> EntityTemplateUserControl """
        ...

    def GetEntityTemplateVirtualPath(self, table:MetaTable, mode, uiHint:str) -> str: # Not found arg types: {'mode': 'DataBoundControlMode'}
        """ GetEntityTemplateVirtualPath(self: EntityTemplateFactory, table: MetaTable, mode: DataBoundControlMode, uiHint: str) -> str """
        ...


class EntityTemplateUserControl(UserControl): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ EntityTemplateUserControl() """
    @property
    def ContainerType(self) -> ContainerType:
        """ Get: ContainerType(self: EntityTemplateUserControl) -> ContainerType """
        ...

    @property
    def Mode(self): # -> DataBoundControlMode
        """ Get: Mode(self: EntityTemplateUserControl) -> DataBoundControlMode """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: EntityTemplateUserControl) -> MetaTable """
        ...

    @property
    def ValidationGroup(self) -> str:
        """ Get: ValidationGroup(self: EntityTemplateUserControl) -> str """
        ...



class FieldTemplateFactory(IFieldTemplateFactory): # skipped bases: <type 'object'>
    """ FieldTemplateFactory() """
    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: FieldTemplateFactory) -> MetaModel """
        ...

    @property
    def TemplateFolderVirtualPath(self) -> str:
        """
        Get: TemplateFolderVirtualPath(self: FieldTemplateFactory) -> str
        Set: TemplateFolderVirtualPath(self: FieldTemplateFactory) = value
        """
        ...


    def BuildVirtualPath(self, templateName:str, column, mode) -> str: # Not found arg types: {'column': 'MetaColumn', 'mode': 'DataBoundControlMode'}
        """ BuildVirtualPath(self: FieldTemplateFactory, templateName: str, column: MetaColumn, mode: DataBoundControlMode) -> str """
        ...

    def GetFieldTemplateVirtualPath(self, column, mode, uiHint:str) -> str: # Not found arg types: {'column': 'MetaColumn', 'mode': 'DataBoundControlMode'}
        """ GetFieldTemplateVirtualPath(self: FieldTemplateFactory, column: MetaColumn, mode: DataBoundControlMode, uiHint: str) -> str """
        ...

    def PreprocessMode(self, column, mode): # -> DataBoundControlMode # Not found arg types: {'column': 'MetaColumn', 'mode': 'DataBoundControlMode'}
        """ PreprocessMode(self: FieldTemplateFactory, column: MetaColumn, mode: DataBoundControlMode) -> DataBoundControlMode """
        ...


class IFieldTemplate: # skipped bases: <type 'object'>
    """ no doc """
    def SetHost(self, host:IFieldTemplateHost): # -> 
        """ SetHost(self: IFieldTemplate, host: IFieldTemplateHost) """
        ...


class FieldTemplateUserControl(IBindableControl, UserControl, IFieldTemplate): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ FieldTemplateUserControl() """
    @property
    def ChildrenColumn(self): # -> MetaChildrenColumn
        """ Get: ChildrenColumn(self: FieldTemplateUserControl) -> MetaChildrenColumn """
        ...

    @property
    def ChildrenPath(self):
        ...

    @property
    def Column(self): # -> MetaColumn
        """ Get: Column(self: FieldTemplateUserControl) -> MetaColumn """
        ...

    @property
    def ContainerType(self) -> ContainerType:
        """ Get: ContainerType(self: FieldTemplateUserControl) -> ContainerType """
        ...

    @property
    def DataControl(self) -> Control:
        """ Get: DataControl(self: FieldTemplateUserControl) -> Control """
        ...

    @property
    def FieldValue(self) -> object:
        """
        Get: FieldValue(self: FieldTemplateUserControl) -> object
        Set: FieldValue(self: FieldTemplateUserControl) = value
        """
        ...

    @property
    def FieldValueEditString(self) -> str:
        """ Get: FieldValueEditString(self: FieldTemplateUserControl) -> str """
        ...

    @property
    def FieldValueString(self) -> str:
        """ Get: FieldValueString(self: FieldTemplateUserControl) -> str """
        ...

    @property
    def ForeignKeyColumn(self): # -> MetaForeignKeyColumn
        """ Get: ForeignKeyColumn(self: FieldTemplateUserControl) -> MetaForeignKeyColumn """
        ...

    @property
    def ForeignKeyPath(self):
        ...

    @property
    def FormattingOptions(self) -> IFieldFormattingOptions:
        """ Get: FormattingOptions(self: FieldTemplateUserControl) -> IFieldFormattingOptions """
        ...

    @property
    def Host(self) -> IFieldTemplateHost:
        """ Get: Host(self: FieldTemplateUserControl) -> IFieldTemplateHost """
        ...

    @property
    def MetadataAttributes(self) -> AttributeCollection:
        """ Get: MetadataAttributes(self: FieldTemplateUserControl) -> AttributeCollection """
        ...

    @property
    def Mode(self): # -> DataBoundControlMode
        """ Get: Mode(self: FieldTemplateUserControl) -> DataBoundControlMode """
        ...

    @property
    def Row(self) -> object:
        """ Get: Row(self: FieldTemplateUserControl) -> object """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: FieldTemplateUserControl) -> MetaTable """
        ...


    def BuildChildrenPath(self, *args): #cannot find CLR method
        """ BuildChildrenPath(self: FieldTemplateUserControl, path: str) -> str """
        ...

    def BuildForeignKeyPath(self, *args): #cannot find CLR method
        """ BuildForeignKeyPath(self: FieldTemplateUserControl, path: str) -> str """
        ...

    def ConvertEditedValue(self, *args): #cannot find CLR method
        """ ConvertEditedValue(self: FieldTemplateUserControl, value: str) -> object """
        ...

    def ExtractForeignKey(self, *args): #cannot find CLR method
        """ ExtractForeignKey(self: FieldTemplateUserControl, dictionary: IDictionary, selectedValue: str) """
        ...

    def FindOtherFieldTemplate(self, *args): #cannot find CLR method
        """ FindOtherFieldTemplate(self: FieldTemplateUserControl, columnName: str) -> FieldTemplateUserControl """
        ...

    def FormatFieldValue(self, fieldValue:object) -> str:
        """ FormatFieldValue(self: FieldTemplateUserControl, fieldValue: object) -> str """
        ...

    def GetColumnValue(self, *args): #cannot find CLR method
        """ GetColumnValue(self: FieldTemplateUserControl, column: MetaColumn) -> object """
        ...

    def GetSelectedValueString(self, *args): #cannot find CLR method
        """ GetSelectedValueString(self: FieldTemplateUserControl) -> str """
        ...

    def IgnoreModelValidationAttribute(self, *args): #cannot find CLR method
        """ IgnoreModelValidationAttribute(self: FieldTemplateUserControl, attributeType: Type) """
        ...

    def PopulateListControl(self, *args): #cannot find CLR method
        """ PopulateListControl(self: FieldTemplateUserControl, listControl: ListControl) """
        ...

    def SetUpValidator(self, *args): #cannot find CLR method
        """ SetUpValidator(self: FieldTemplateUserControl, validator: BaseValidator)SetUpValidator(self: FieldTemplateUserControl, validator: BaseValidator, column: MetaColumn) """
        ...


class FilterFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ FilterFactory() """
    def CreateFilterControl(self, column, filterUIHint:str): # -> QueryableFilterUserControl # Not found arg types: {'column': 'MetaColumn'}
        """ CreateFilterControl(self: FilterFactory, column: MetaColumn, filterUIHint: str) -> QueryableFilterUserControl """
        ...

    def GetFilterVirtualPath(self, column, filterUIHint:str) -> str: # Not found arg types: {'column': 'MetaColumn'}
        """ GetFilterVirtualPath(self: FilterFactory, column: MetaColumn, filterUIHint: str) -> str """
        ...


class FilterRepeater(Repeater, IWhereParametersProvider): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'object'>
    """ FilterRepeater() """
    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: FilterRepeater) -> str
        Set: ContextTypeName(self: FilterRepeater) = value
        """
        ...

    @property
    def DynamicFilterContainerId(self) -> str:
        """
        Get: DynamicFilterContainerId(self: FilterRepeater) -> str
        Set: DynamicFilterContainerId(self: FilterRepeater) = value
        """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: FilterRepeater) -> MetaTable """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: FilterRepeater) -> str
        Set: TableName(self: FilterRepeater) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: FilterRepeater) -> bool
        Set: Visible(self: FilterRepeater) = value
        """
        ...


    def GetFilteredColumns(self, *args): #cannot find CLR method
        """ GetFilteredColumns(self: FilterRepeater) -> IEnumerable[MetaColumn] """
        ...

    def OnFilterItemCreated(self, *args): #cannot find CLR method
        """ OnFilterItemCreated(self: FilterRepeater, item: RepeaterItem) """
        ...


class IControlParameterTarget: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FilteredColumn(self): # -> MetaColumn
        """ Get: FilteredColumn(self: IControlParameterTarget) -> MetaColumn """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: IControlParameterTarget) -> MetaTable """
        ...


    def GetPropertyNameExpression(self, columnName:str) -> str:
        """ GetPropertyNameExpression(self: IControlParameterTarget, columnName: str) -> str """
        ...


class FilterUserControlBase(IControlParameterTarget, UserControl): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ FilterUserControlBase() """
    @property
    def Column(self): # -> MetaColumn
        """ Get: Column(self: FilterUserControlBase) -> MetaColumn """
        ...

    @property
    def ContextTypeName(self) -> str:
        """
        Get: ContextTypeName(self: FilterUserControlBase) -> str
        Set: ContextTypeName(self: FilterUserControlBase) = value
        """
        ...

    @property
    def DataField(self) -> str:
        """
        Get: DataField(self: FilterUserControlBase) -> str
        Set: DataField(self: FilterUserControlBase) = value
        """
        ...

    @property
    def InitialValue(self) -> str:
        """ Get: InitialValue(self: FilterUserControlBase) -> str """
        ...

    @property
    def SelectedDataKey(self): # -> DataKey
        """ Get: SelectedDataKey(self: FilterUserControlBase) -> DataKey """
        ...

    @property
    def SelectedValue(self) -> str:
        """ Get: SelectedValue(self: FilterUserControlBase) -> str """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: FilterUserControlBase) -> str
        Set: TableName(self: FilterUserControlBase) = value
        """
        ...


    def PopulateListControl(self, listControl:ListControl): # -> 
        """ PopulateListControl(self: FilterUserControlBase, listControl: ListControl) """
        ...


class IDynamicDataSource(IDataSource): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoGenerateWhereClause(self) -> bool:
        """
        Get: AutoGenerateWhereClause(self: IDynamicDataSource) -> bool
        Set: AutoGenerateWhereClause(self: IDynamicDataSource) = value
        """
        ...

    @property
    def ContextType(self) -> Type:
        """
        Get: ContextType(self: IDynamicDataSource) -> Type
        Set: ContextType(self: IDynamicDataSource) = value
        """
        ...

    @property
    def EnableDelete(self) -> bool:
        """
        Get: EnableDelete(self: IDynamicDataSource) -> bool
        Set: EnableDelete(self: IDynamicDataSource) = value
        """
        ...

    @property
    def EnableInsert(self) -> bool:
        """
        Get: EnableInsert(self: IDynamicDataSource) -> bool
        Set: EnableInsert(self: IDynamicDataSource) = value
        """
        ...

    @property
    def EnableUpdate(self) -> bool:
        """
        Get: EnableUpdate(self: IDynamicDataSource) -> bool
        Set: EnableUpdate(self: IDynamicDataSource) = value
        """
        ...

    @property
    def EntitySetName(self) -> str:
        """
        Get: EntitySetName(self: IDynamicDataSource) -> str
        Set: EntitySetName(self: IDynamicDataSource) = value
        """
        ...

    @property
    def Where(self) -> str:
        """
        Get: Where(self: IDynamicDataSource) -> str
        Set: Where(self: IDynamicDataSource) = value
        """
        ...

    @property
    def WhereParameters(self) -> ParameterCollection:
        """ Get: WhereParameters(self: IDynamicDataSource) -> ParameterCollection """
        ...


    Exception = ...


class IDynamicValidatorException: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InnerExceptions(self) -> IDictionary:
        """ Get: InnerExceptions(self: IDynamicValidatorException) -> IDictionary[str, Exception] """
        ...



class IFieldTemplateFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateFieldTemplate(self, column, mode, uiHint:str) -> IFieldTemplate: # Not found arg types: {'column': 'MetaColumn', 'mode': 'DataBoundControlMode'}
        """ CreateFieldTemplate(self: IFieldTemplateFactory, column: MetaColumn, mode: DataBoundControlMode, uiHint: str) -> IFieldTemplate """
        ...

    def Initialize(self, model:MetaModel): # -> 
        """ Initialize(self: IFieldTemplateFactory, model: MetaModel) """
        ...


class MetaColumn(IFieldFormattingOptions, IMetaColumn): # skipped bases: <type 'object'>
    """ MetaColumn(table: MetaTable, columnProvider: ColumnProvider) """
    @property
    def AllowInitialValue(self) -> bool:
        """ Get: AllowInitialValue(self: MetaColumn) -> bool """
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: MetaColumn) -> AttributeCollection """
        ...

    @property
    def ColumnType(self) -> Type:
        """ Get: ColumnType(self: MetaColumn) -> Type """
        ...

    @property
    def DataTypeAttribute(self) -> DataTypeAttribute:
        """ Get: DataTypeAttribute(self: MetaColumn) -> DataTypeAttribute """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: MetaColumn) -> object """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MetaColumn) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: MetaColumn) -> str """
        ...

    @property
    def EntityTypeProperty(self) -> PropertyInfo:
        """ Get: EntityTypeProperty(self: MetaColumn) -> PropertyInfo """
        ...

    @property
    def FilterUIHint(self) -> str:
        """ Get: FilterUIHint(self: MetaColumn) -> str """
        ...

    @property
    def IsBinaryData(self) -> bool:
        """ Get: IsBinaryData(self: MetaColumn) -> bool """
        ...

    @property
    def IsCustomProperty(self) -> bool:
        """ Get: IsCustomProperty(self: MetaColumn) -> bool """
        ...

    @property
    def IsFloatingPoint(self) -> bool:
        """ Get: IsFloatingPoint(self: MetaColumn) -> bool """
        ...

    @property
    def IsForeignKeyComponent(self) -> bool:
        """ Get: IsForeignKeyComponent(self: MetaColumn) -> bool """
        ...

    @property
    def IsGenerated(self) -> bool:
        """ Get: IsGenerated(self: MetaColumn) -> bool """
        ...

    @property
    def IsInteger(self) -> bool:
        """ Get: IsInteger(self: MetaColumn) -> bool """
        ...

    @property
    def IsLongString(self) -> bool:
        """ Get: IsLongString(self: MetaColumn) -> bool """
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        """ Get: IsPrimaryKey(self: MetaColumn) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MetaColumn) -> bool """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: MetaColumn) -> bool """
        ...

    @property
    def IsString(self) -> bool:
        """ Get: IsString(self: MetaColumn) -> bool """
        ...

    @property
    def MaxLength(self) -> int:
        """ Get: MaxLength(self: MetaColumn) -> int """
        ...

    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: MetaColumn) -> MetaModel """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaColumn) -> str """
        ...

    @property
    def Prompt(self) -> str:
        """ Get: Prompt(self: MetaColumn) -> str """
        ...

    @property
    def Provider(self) -> ColumnProvider:
        """ Get: Provider(self: MetaColumn) -> ColumnProvider """
        ...

    @property
    def RequiredErrorMessage(self) -> str:
        """ Get: RequiredErrorMessage(self: MetaColumn) -> str """
        ...

    @property
    def Scaffold(self) -> bool:
        """
        Get: Scaffold(self: MetaColumn) -> bool
        Set: Scaffold(self: MetaColumn) = value
        """
        ...

    @property
    def ShortDisplayName(self) -> str:
        """ Get: ShortDisplayName(self: MetaColumn) -> str """
        ...

    @property
    def SortExpression(self) -> str:
        """ Get: SortExpression(self: MetaColumn) -> str """
        ...

    @property
    def Table(self) -> MetaTable:
        """ Get: Table(self: MetaColumn) -> MetaTable """
        ...

    @property
    def TypeCode(self) -> TypeCode:
        """ Get: TypeCode(self: MetaColumn) -> TypeCode """
        ...

    @property
    def UIHint(self) -> str:
        """ Get: UIHint(self: MetaColumn) -> str """
        ...


    def BuildAttributeCollection(self, *args): #cannot find CLR method
        """ BuildAttributeCollection(self: MetaColumn) -> AttributeCollection """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: MetaColumn) """
        ...

    def ResetMetadata(self): # -> 
        """ ResetMetadata(self: MetaColumn) """
        ...

    def ToString(self) -> str:
        """ ToString(self: MetaColumn) -> str """
        ...


class MetaChildrenColumn(IMetaChildrenColumn, MetaColumn): # skipped bases: <type 'IFieldFormattingOptions'>, <type 'IMetaColumn'>, <type 'object'>
    """ MetaChildrenColumn(table: MetaTable, entityMember: ColumnProvider) """
    @property
    def ChildTable(self) -> MetaTable:
        """ Get: ChildTable(self: MetaChildrenColumn) -> MetaTable """
        ...

    @property
    def ColumnInOtherTable(self) -> MetaColumn:
        """ Get: ColumnInOtherTable(self: MetaChildrenColumn) -> MetaColumn """
        ...

    @property
    def IsManyToMany(self) -> bool:
        """ Get: IsManyToMany(self: MetaChildrenColumn) -> bool """
        ...


    def GetChildrenListPath(self, row:object) -> str:
        """ GetChildrenListPath(self: MetaChildrenColumn, row: object) -> str """
        ...

    def GetChildrenPath(self, action:str, row:object, path:str = ...) -> str:
        """
        GetChildrenPath(self: MetaChildrenColumn, action: str, row: object) -> str
        GetChildrenPath(self: MetaChildrenColumn, action: str, row: object, path: str) -> str
        """
        ...


class MetaForeignKeyColumn(IMetaForeignKeyColumn, MetaColumn): # skipped bases: <type 'IFieldFormattingOptions'>, <type 'IMetaColumn'>, <type 'object'>
    """ MetaForeignKeyColumn(table: MetaTable, entityMember: ColumnProvider) """
    @property
    def ForeignKeyNames(self) -> ReadOnlyCollection:
        """ Get: ForeignKeyNames(self: MetaForeignKeyColumn) -> ReadOnlyCollection[str] """
        ...

    @property
    def IsPrimaryKeyInThisTable(self) -> bool:
        """ Get: IsPrimaryKeyInThisTable(self: MetaForeignKeyColumn) -> bool """
        ...

    @property
    def ParentTable(self) -> MetaTable:
        """ Get: ParentTable(self: MetaForeignKeyColumn) -> MetaTable """
        ...


    def ExtractForeignKey(self, dictionary:IDictionary, value:str): # -> 
        """ ExtractForeignKey(self: MetaForeignKeyColumn, dictionary: IDictionary, value: str) """
        ...

    def GetFilterExpression(self, foreignKeyName:str) -> str:
        """ GetFilterExpression(self: MetaForeignKeyColumn, foreignKeyName: str) -> str """
        ...

    def GetForeignKeyDetailsPath(self, row:object) -> str:
        """ GetForeignKeyDetailsPath(self: MetaForeignKeyColumn, row: object) -> str """
        ...

    def GetForeignKeyPath(self, action:str, row:object, path:str = ...) -> str:
        """
        GetForeignKeyPath(self: MetaForeignKeyColumn, action: str, row: object) -> str
        GetForeignKeyPath(self: MetaForeignKeyColumn, action: str, row: object, path: str) -> str
        """
        ...

    def GetForeignKeyString(self, row:object) -> str:
        """ GetForeignKeyString(self: MetaForeignKeyColumn, row: object) -> str """
        ...

    def GetForeignKeyValues(self, row:object) -> IList:
        """ GetForeignKeyValues(self: MetaForeignKeyColumn, row: object) -> IList[object] """
        ...


class MetaModel(IMetaModel): # skipped bases: <type 'object'>
    """
    MetaModel()
    MetaModel(registerGlobally: bool)
    """
    @property
    def Default(self) -> MetaModel:
        """ Get: Default() -> MetaModel """
        ...

    @property
    def DynamicDataFolderVirtualPath(self) -> str:
        """
        Get: DynamicDataFolderVirtualPath(self: MetaModel) -> str
        Set: DynamicDataFolderVirtualPath(self: MetaModel) = value
        """
        ...

    @property
    def EntityTemplateFactory(self) -> EntityTemplateFactory:
        """
        Get: EntityTemplateFactory(self: MetaModel) -> EntityTemplateFactory
        Set: EntityTemplateFactory(self: MetaModel) = value
        """
        ...

    @property
    def FieldTemplateFactory(self) -> IFieldTemplateFactory:
        """
        Get: FieldTemplateFactory(self: MetaModel) -> IFieldTemplateFactory
        Set: FieldTemplateFactory(self: MetaModel) = value
        """
        ...

    @property
    def FilterFactory(self) -> FilterFactory:
        """
        Get: FilterFactory(self: MetaModel) -> FilterFactory
        Set: FilterFactory(self: MetaModel) = value
        """
        ...

    @property
    def Tables(self) -> ReadOnlyCollection:
        """ Get: Tables(self: MetaModel) -> ReadOnlyCollection[MetaTable] """
        ...

    @property
    def VisibleTables(self) -> List:
        """ Get: VisibleTables(self: MetaModel) -> List[MetaTable] """
        ...


    def CreateTable(self, *args): #cannot find CLR method
        """ CreateTable(self: MetaModel, provider: TableProvider) -> MetaTable """
        ...

    def GetActionPath(self, tableName:str, action:str, row:object) -> str:
        """ GetActionPath(self: MetaModel, tableName: str, action: str, row: object) -> str """
        ...

    @staticmethod
    def GetModel(contextType:Type) -> MetaModel:
        """ GetModel(contextType: Type) -> MetaModel """
        ...

    def GetTable(self, *__args:Type) -> MetaTable:
        """
        GetTable(self: MetaModel, entityType: Type) -> MetaTable
        GetTable(self: MetaModel, uniqueTableName: str) -> MetaTable
        GetTable(self: MetaModel, tableName: str, contextType: Type) -> MetaTable
        """
        ...

    def RegisterContext(self, *__args:Type): # -> 
        """ RegisterContext(self: MetaModel, contextType: Type)RegisterContext(self: MetaModel, contextType: Type, configuration: ContextConfiguration)RegisterContext(self: MetaModel, contextFactory: Func[object])RegisterContext(self: MetaModel, contextFactory: Func[object], configuration: ContextConfiguration)RegisterContext(self: MetaModel, dataModelProvider: DataModelProvider)RegisterContext(self: MetaModel, dataModelProvider: DataModelProvider, configuration: ContextConfiguration) """
        ...

    @staticmethod
    def ResetRegistrationException(): # -> 
        """ ResetRegistrationException() """
        ...

    def TryGetTable(self, *__args:Type) -> Tuple_[bool, MetaTable]:
        """
        TryGetTable(self: MetaModel, entityType: Type) -> (bool, MetaTable)
        TryGetTable(self: MetaModel, uniqueTableName: str) -> (bool, MetaTable)
        """
        ...


class MetaTable(IMetaTable): # skipped bases: <type 'object'>
    """ MetaTable(metaModel: MetaModel, tableProvider: TableProvider) """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: MetaTable) -> AttributeCollection """
        ...

    @property
    def Columns(self) -> ReadOnlyCollection:
        """ Get: Columns(self: MetaTable) -> ReadOnlyCollection[MetaColumn] """
        ...

    @property
    def DataContextPropertyName(self) -> str:
        """ Get: DataContextPropertyName(self: MetaTable) -> str """
        ...

    @property
    def DataContextType(self) -> Type:
        """ Get: DataContextType(self: MetaTable) -> Type """
        ...

    @property
    def DisplayColumn(self) -> MetaColumn:
        """ Get: DisplayColumn(self: MetaTable) -> MetaColumn """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: MetaTable) -> str """
        ...

    @property
    def EntityType(self) -> Type:
        """ Get: EntityType(self: MetaTable) -> Type """
        ...

    @property
    def ForeignKeyColumnsNames(self) -> str:
        """ Get: ForeignKeyColumnsNames(self: MetaTable) -> str """
        ...

    @property
    def HasPrimaryKey(self) -> bool:
        """ Get: HasPrimaryKey(self: MetaTable) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MetaTable) -> bool """
        ...

    @property
    def ListActionPath(self) -> str:
        """ Get: ListActionPath(self: MetaTable) -> str """
        ...

    @property
    def Model(self) -> MetaModel:
        """ Get: Model(self: MetaTable) -> MetaModel """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MetaTable) -> str """
        ...

    @property
    def PrimaryKeyColumns(self) -> ReadOnlyCollection:
        """ Get: PrimaryKeyColumns(self: MetaTable) -> ReadOnlyCollection[MetaColumn] """
        ...

    @property
    def Provider(self) -> TableProvider:
        """ Get: Provider(self: MetaTable) -> TableProvider """
        ...

    @property
    def RootEntityType(self) -> Type:
        """ Get: RootEntityType(self: MetaTable) -> Type """
        ...

    @property
    def Scaffold(self) -> bool:
        """ Get: Scaffold(self: MetaTable) -> bool """
        ...

    @property
    def SortColumn(self) -> MetaColumn:
        """ Get: SortColumn(self: MetaTable) -> MetaColumn """
        ...

    @property
    def SortDescending(self) -> bool:
        """ Get: SortDescending(self: MetaTable) -> bool """
        ...


    def BuildAttributeCollection(self, *args): #cannot find CLR method
        """ BuildAttributeCollection(self: MetaTable) -> AttributeCollection """
        ...

    def CanDelete(self, principal:IPrincipal) -> bool:
        """ CanDelete(self: MetaTable, principal: IPrincipal) -> bool """
        ...

    def CanInsert(self, principal:IPrincipal) -> bool:
        """ CanInsert(self: MetaTable, principal: IPrincipal) -> bool """
        ...

    def CanRead(self, principal:IPrincipal) -> bool:
        """ CanRead(self: MetaTable, principal: IPrincipal) -> bool """
        ...

    def CanUpdate(self, principal:IPrincipal) -> bool:
        """ CanUpdate(self: MetaTable, principal: IPrincipal) -> bool """
        ...

    def CreateChildrenColumn(self, *args): #cannot find CLR method
        """ CreateChildrenColumn(self: MetaTable, columnProvider: ColumnProvider) -> MetaChildrenColumn """
        ...

    def CreateColumn(self, *args): #cannot find CLR method
        """ CreateColumn(self: MetaTable, columnProvider: ColumnProvider) -> MetaColumn """
        ...

    def CreateContext(self) -> object:
        """ CreateContext(self: MetaTable) -> object """
        ...

    def CreateForeignKeyColumn(self, *args): #cannot find CLR method
        """ CreateForeignKeyColumn(self: MetaTable, columnProvider: ColumnProvider) -> MetaForeignKeyColumn """
        ...

    @staticmethod
    def CreateTable(*__args:Type) -> MetaTable:
        """
        CreateTable(entityType: Type) -> MetaTable
        CreateTable(typeDescriptor: ICustomTypeDescriptor) -> MetaTable
        """
        ...

    def GetActionPath(self, action:str, *__args:object) -> str:
        """
        GetActionPath(self: MetaTable, action: str, row: object) -> str
        GetActionPath(self: MetaTable, action: str, row: object, path: str) -> str
        GetActionPath(self: MetaTable, action: str) -> str
        GetActionPath(self: MetaTable, action: str, routeValues: RouteValueDictionary) -> str
        GetActionPath(self: MetaTable, action: str, primaryKeyValues: IList[object]) -> str
        GetActionPath(self: MetaTable, action: str, primaryKeyValues: IList[object], path: str) -> str
        """
        ...

    def GetColumn(self, columnName:str) -> MetaColumn:
        """ GetColumn(self: MetaTable, columnName: str) -> MetaColumn """
        ...

    def GetColumnValuesFromRoute(self, context:HttpContext) -> IDictionary:
        """ GetColumnValuesFromRoute(self: MetaTable, context: HttpContext) -> IDictionary[str, object] """
        ...

    def GetDataKeyFromRoute(self): # -> DataKey
        """ GetDataKeyFromRoute(self: MetaTable) -> DataKey """
        ...

    def GetDisplayString(self, row:object) -> str:
        """ GetDisplayString(self: MetaTable, row: object) -> str """
        ...

    def GetFilteredColumns(self) -> IEnumerable:
        """ GetFilteredColumns(self: MetaTable) -> IEnumerable[MetaColumn] """
        ...

    def GetPrimaryKeyDictionary(self, row:object) -> IDictionary:
        """ GetPrimaryKeyDictionary(self: MetaTable, row: object) -> IDictionary[str, object] """
        ...

    def GetPrimaryKeyString(self, *__args:object) -> str:
        """
        GetPrimaryKeyString(self: MetaTable, row: object) -> str
        GetPrimaryKeyString(self: MetaTable, primaryKeyValues: IList[object]) -> str
        """
        ...

    def GetPrimaryKeyValues(self, row:object) -> IList:
        """ GetPrimaryKeyValues(self: MetaTable, row: object) -> IList[object] """
        ...

    def GetQuery(self, context:object = ...) -> IQueryable:
        """
        GetQuery(self: MetaTable) -> IQueryable
        GetQuery(self: MetaTable, context: object) -> IQueryable
        """
        ...

    def GetScaffoldColumns(self, mode, containerType:ContainerType) -> IEnumerable: # Not found arg types: {'mode': 'DataBoundControlMode'}
        """ GetScaffoldColumns(self: MetaTable, mode: DataBoundControlMode, containerType: ContainerType) -> IEnumerable[MetaColumn] """
        ...

    @staticmethod
    def GetTable(entityType:Type) -> MetaTable:
        """ GetTable(entityType: Type) -> MetaTable """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: MetaTable) """
        ...

    def ResetMetadata(self): # -> 
        """ ResetMetadata(self: MetaTable) """
        ...

    def ToString(self) -> str:
        """ ToString(self: MetaTable) -> str """
        ...

    def TryGetColumn(self, columnName, column) -> Tuple_[bool, MetaColumn]:
        """ TryGetColumn(self: MetaTable, columnName: str) -> (bool, MetaColumn) """
        ...

    @staticmethod
    def TryGetTable(entityType, table) -> Tuple_[bool, MetaTable]:
        """ TryGetTable(entityType: Type) -> (bool, MetaTable) """
        ...


class PageAction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Details(self) -> str:
        """ Get: Details() -> str """
        ...

    @property
    def Edit(self) -> str:
        """ Get: Edit() -> str """
        ...

    @property
    def Insert(self) -> str:
        """ Get: Insert() -> str """
        ...

    @property
    def List(self) -> str:
        """ Get: List() -> str """
        ...


    __all__: list = ...


class QueryableFilterRepeater(IFilterExpressionProvider, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ QueryableFilterRepeater() """
    @property
    def DynamicFilterContainerId(self) -> str:
        """
        Get: DynamicFilterContainerId(self: QueryableFilterRepeater) -> str
        Set: DynamicFilterContainerId(self: QueryableFilterRepeater) = value
        """
        ...

    @property
    def ItemTemplate(self) -> ITemplate:
        """
        Get: ItemTemplate(self: QueryableFilterRepeater) -> ITemplate
        Set: ItemTemplate(self: QueryableFilterRepeater) = value
        """
        ...



class QueryableFilterUserControl(UserControl): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ no doc """
    @property
    def Column(self):
        ...

    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: QueryableFilterUserControl) -> str """
        ...

    @property
    def DefaultValues(self) -> IDictionary:
        """ Get: DefaultValues(self: QueryableFilterUserControl) -> IDictionary[str, object] """
        ...

    @property
    def FilterControl(self) -> Control:
        """ Get: FilterControl(self: QueryableFilterUserControl) -> Control """
        ...


    @staticmethod
    def ApplyEqualityFilter(source:IQueryable, propertyName:str, value:object) -> IQueryable:
        """ ApplyEqualityFilter(source: IQueryable, propertyName: str, value: object) -> IQueryable """
        ...

    def GetQueryable(self, source:IQueryable) -> IQueryable:
        """ GetQueryable(self: QueryableFilterUserControl, source: IQueryable) -> IQueryable """
        ...

    def OnFilterChanged(self, *args): #cannot find CLR method
        """ OnFilterChanged(self: QueryableFilterUserControl) """
        ...

    def PopulateListControl(self, listControl:ListControl): # -> 
        """ PopulateListControl(self: QueryableFilterUserControl, listControl: ListControl) """
        ...

    FilterChanged = ...


class TableNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TableNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: TableNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


# variables with complex values

