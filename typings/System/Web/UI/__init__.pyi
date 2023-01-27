# encoding: utf-8
# module System.Web.UI calls itself UI
# from System.Web.Extensions.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Publisher import Page

from Microsoft.Office.Interop.Word import Style

from Microsoft.SqlServer.Diagnostics.STrace import TraceContext

from Microsoft.Vbe.Interop.Forms import Control, IControl

from System import (Array, AsyncCallback, Attribute, Char, DateTime, Enum, 
    EventArgs, EventHandler, IAsyncResult, IServiceProvider, 
    MulticastDelegate, TimeSpan, Type, Version)

from System.CodeDom import (CodeArgumentReferenceExpression, CodeCompileUnit, 
    CodeMemberMethod, CodeStatement, CodeTypeDeclaration)

from System.Collections import (ArrayList, ICollection, IDictionary, 
    IEnumerable, IEnumerator, IList)

from System.Collections.ObjectModel import Collection, ReadOnlyCollection

from System.Collections.Specialized import (IOrderedDictionary, 
    NameValueCollection)

from System.ComponentModel import (AttributeCollection, BindingDirection, 
    IComponent, IListSource, ITypeDescriptorContext, Int32Converter, 
    PropertyDescriptor)

from System.ComponentModel.Design import IDesignerHost

from System.Globalization import CultureInfo

from System.IO import Stream, TextWriter

from System.Reflection import Assembly, MemberInfo, PropertyInfo

from System.Runtime.Serialization import IFormatter

from System.Security.Principal import IPrincipal

from System.Text.RegularExpressions import Match

from System.Web.Caching import Cache, CacheDependency

from System.Web.ModelBinding import (IValueProvider, 
    ModelBindingExecutionContext, ModelStateDictionary)

from System.Web.Routing import RouteData, RouteValueDictionary

from System.Web.SessionState import HttpSessionState

from System.Web.UI.Adapters import PageAdapter

from System.Web.UI.HtmlControls import HtmlForm, HtmlHead

from System.Xml import IXmlNamespaceResolver

from typing import Self

"""The following names are not found in the module: (BeginEventHandler, 
    BoundEvent, ClientIDMode, ControlBuilder, ControlCachePolicy, 
    ControlCollection, CssStyleCollection, DataBindingCollection, 
    DataKeyArray, DataSourceView, DataSourceViewOperationCallback, 
    DataSourceViewSelectCallback, EndEventHandler, 
    ExpressionBindingCollection, ExpressionBuilder, 
    HierarchicalDataSourceView, HtmlTextWriter, HtmlTextWriterTag, 
    HttpApplicationState, HttpCacheVaryByParams, HttpContext, HttpRequest, 
    HttpResponse, HttpServerUtility, IAssemblyDependencyParser, 
    IBindableTemplate, IFilterResolutionService, IHierarchicalEnumerable, 
    IHierarchyData, IHttpHandler, IHttpHandlerFactory2, INamingContainer, 
    INonBindingContainer, IScriptManager, IScriptManagerInternal, 
    IScriptResourceDefinition, IScriptResourceMapping, IStateFormatter2, 
    ITemplate, IThemeResolutionService, IUpdatePanel, ObjectPersistData, 
    PageAsyncTask, PostBackOptions, RegisteredScriptType, RenderMethod, 
    ScriptMode, ScriptReferenceCollection, ScriptResourceMapping, 
    ServiceReferenceCollection, StandardValuesCollection, TExtenderControl, 
    TModel, TScriptControl, TemplateControl, ThemeProvider, TraceMode, 
    UnobtrusiveValidationMode, UpdatePanel, UpdatePanelRenderMode, 
    UpdatePanelTriggerCollection, UpdatePanelUpdateMode, ValidateRequestMode, 
    ValidatorCollection, VerificationConditionalOperator, 
    VerificationReportLevel, VerificationRule, ViewStateEncryptionMode, 
    ViewStateMode, VirtualReferenceType, WebControl, field#)
"""

# no functions
# classes

class AjaxFrameworkMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AjaxFrameworkMode, values: Disabled (1), Enabled (0), Explicit (2) """
    Disabled: AjaxFrameworkMode = ...
    Enabled: AjaxFrameworkMode = ...
    Explicit: AjaxFrameworkMode = ...
    value__ = ...


class AsyncPostBackErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ AsyncPostBackErrorEventArgs(exception: Exception) """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: AsyncPostBackErrorEventArgs) -> Exception """
        ...


    def __new__(cls, exception:Exception) -> Self:
        """ __new__(cls: type, exception: Exception) """
        ...


class UpdatePanelTrigger: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Owner(self): # -> UpdatePanel
        """ Get: Owner(self: UpdatePanelTrigger) -> UpdatePanel """
        ...


    def HasTriggered(self, *args): #cannot find CLR method
        """ HasTriggered(self: UpdatePanelTrigger) -> bool """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UpdatePanelTrigger) """
        ...


class UpdatePanelControlTrigger(UpdatePanelTrigger): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: UpdatePanelControlTrigger) -> str
        Set: ControlID(self: UpdatePanelControlTrigger) = value
        """
        ...


    def FindTargetControl(self, *args): #cannot find CLR method
        """ FindTargetControl(self: UpdatePanelControlTrigger, searchNamingContainers: bool) -> Control """
        ...


class AsyncPostBackTrigger(UpdatePanelControlTrigger): # skipped bases: <type 'object'>
    """ AsyncPostBackTrigger() """
    @property
    def EventName(self) -> str:
        """
        Get: EventName(self: AsyncPostBackTrigger) -> str
        Set: EventName(self: AsyncPostBackTrigger) = value
        """
        ...


    def OnEvent(self, sender:object, e:EventArgs): # -> 
        """ OnEvent(self: AsyncPostBackTrigger, sender: object, e: EventArgs) """
        ...

    def ToString(self) -> str:
        """ ToString(self: AsyncPostBackTrigger) -> str """
        ...


class AttributeCollection: # skipped bases: <type 'object'>, <type 'object'>
    """ AttributeCollection(bag: StateBag) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: AttributeCollection) -> int """
        ...

    @property
    def CssStyle(self): # -> CssStyleCollection
        """ Get: CssStyle(self: AttributeCollection) -> CssStyleCollection """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: AttributeCollection) -> ICollection """
        ...


    def Add(self, key:str, value:str): # -> 
        """ Add(self: AttributeCollection, key: str, value: str) """
        ...

    def AddAttributes(self, writer): # ->  # Not found arg types: {'writer': 'HtmlTextWriter'}
        """ AddAttributes(self: AttributeCollection, writer: HtmlTextWriter) """
        ...

    def Clear(self): # -> 
        """ Clear(self: AttributeCollection) """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: AttributeCollection, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AttributeCollection) -> int """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: AttributeCollection, key: str) """
        ...

    def Render(self, writer): # ->  # Not found arg types: {'writer': 'HtmlTextWriter'}
        """ Render(self: AttributeCollection, writer: HtmlTextWriter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class AuthenticationServiceManager: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthenticationServiceManager() """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: AuthenticationServiceManager) -> str
        Set: Path(self: AuthenticationServiceManager) = value
        """
        ...



class BaseParser: # skipped bases: <type 'object'>, <type 'object'>
    """ BaseParser() """
    pass

class IControlBuilderAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ControlBuilder(self): # -> ControlBuilder
        """ Get: ControlBuilder(self: IControlBuilderAccessor) -> ControlBuilder """
        ...



class IControlDesignerAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: IControlDesignerAccessor) -> IDictionary """
        ...


    def GetDesignModeState(self) -> IDictionary:
        """ GetDesignModeState(self: IControlDesignerAccessor) -> IDictionary """
        ...

    def SetDesignModeState(self, data:IDictionary): # -> 
        """ SetDesignModeState(self: IControlDesignerAccessor, data: IDictionary) """
        ...

    def SetOwnerControl(self, owner:Control): # -> 
        """ SetOwnerControl(self: IControlDesignerAccessor, owner: Control) """
        ...


class IDataBindingsAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataBindings(self): # -> DataBindingCollection
        """ Get: DataBindings(self: IDataBindingsAccessor) -> DataBindingCollection """
        ...

    @property
    def HasDataBindings(self) -> bool:
        """ Get: HasDataBindings(self: IDataBindingsAccessor) -> bool """
        ...



class IExpressionsAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expressions(self): # -> ExpressionBindingCollection
        """ Get: Expressions(self: IExpressionsAccessor) -> ExpressionBindingCollection """
        ...

    @property
    def HasExpressions(self) -> bool:
        """ Get: HasExpressions(self: IExpressionsAccessor) -> bool """
        ...



class IParserAccessor: # skipped bases: <type 'object'>
    """ no doc """
    def AddParsedSubObject(self, obj:object): # -> 
        """ AddParsedSubObject(self: IParserAccessor, obj: object) """
        ...


class IUrlResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    def ResolveClientUrl(self, relativeUrl:str) -> str:
        """ ResolveClientUrl(self: IUrlResolutionService, relativeUrl: str) -> str """
        ...


class Control(IControlBuilderAccessor, IParserAccessor, IDataBindingsAccessor, IUrlResolutionService, IControlDesignerAccessor, IComponent, IExpressionsAccessor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ Control() """
    @property
    def Adapter(self):
        ...

    @property
    def AppRelativeTemplateSourceDirectory(self) -> str:
        """
        Get: AppRelativeTemplateSourceDirectory(self: Control) -> str
        Set: AppRelativeTemplateSourceDirectory(self: Control) = value
        """
        ...

    @property
    def BindingContainer(self) -> Control:
        """ Get: BindingContainer(self: Control) -> Control """
        ...

    @property
    def ChildControlsCreated(self):
        ...

    @property
    def ClientID(self) -> str:
        """ Get: ClientID(self: Control) -> str """
        ...

    @property
    def ClientIDMode(self): # -> ClientIDMode
        """
        Get: ClientIDMode(self: Control) -> ClientIDMode
        Set: ClientIDMode(self: Control) = value
        """
        ...

    @property
    def ClientIDSeparator(self):
        ...

    @property
    def Context(self):
        ...

    @property
    def Controls(self): # -> ControlCollection
        """ Get: Controls(self: Control) -> ControlCollection """
        ...

    @property
    def DataItemContainer(self) -> Control:
        """ Get: DataItemContainer(self: Control) -> Control """
        ...

    @property
    def DataKeysContainer(self) -> Control:
        """ Get: DataKeysContainer(self: Control) -> Control """
        ...

    @property
    def DesignMode(self):
        ...

    @property
    def EnableTheming(self) -> bool:
        """
        Get: EnableTheming(self: Control) -> bool
        Set: EnableTheming(self: Control) = value
        """
        ...

    @property
    def EnableViewState(self) -> bool:
        """
        Get: EnableViewState(self: Control) -> bool
        Set: EnableViewState(self: Control) = value
        """
        ...

    @property
    def Events(self):
        ...

    @property
    def HasChildViewState(self):
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: Control) -> str
        Set: ID(self: Control) = value
        """
        ...

    @property
    def IdSeparator(self):
        ...

    @property
    def IsChildControlStateCleared(self):
        ...

    @property
    def IsTrackingViewState(self):
        ...

    @property
    def IsViewStateEnabled(self):
        ...

    @property
    def LoadViewStateByID(self):
        ...

    @property
    def NamingContainer(self) -> Control:
        """ Get: NamingContainer(self: Control) -> Control """
        ...

    @property
    def Page(self) -> Page:
        """
        Get: Page(self: Control) -> Page
        Set: Page(self: Control) = value
        """
        ...

    @property
    def Parent(self) -> Control:
        """ Get: Parent(self: Control) -> Control """
        ...

    @property
    def RenderingCompatibility(self) -> Version:
        """
        Get: RenderingCompatibility(self: Control) -> Version
        Set: RenderingCompatibility(self: Control) = value
        """
        ...

    @property
    def SkinID(self) -> str:
        """
        Get: SkinID(self: Control) -> str
        Set: SkinID(self: Control) = value
        """
        ...

    @property
    def TemplateControl(self): # -> TemplateControl
        """
        Get: TemplateControl(self: Control) -> TemplateControl
        Set: TemplateControl(self: Control) = value
        """
        ...

    @property
    def TemplateSourceDirectory(self) -> str:
        """ Get: TemplateSourceDirectory(self: Control) -> str """
        ...

    @property
    def UniqueID(self) -> str:
        """ Get: UniqueID(self: Control) -> str """
        ...

    @property
    def ValidateRequestMode(self): # -> ValidateRequestMode
        """
        Get: ValidateRequestMode(self: Control) -> ValidateRequestMode
        Set: ValidateRequestMode(self: Control) = value
        """
        ...

    @property
    def ViewState(self):
        ...

    @property
    def ViewStateIgnoresCase(self):
        ...

    @property
    def ViewStateMode(self): # -> ViewStateMode
        """
        Get: ViewStateMode(self: Control) -> ViewStateMode
        Set: ViewStateMode(self: Control) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Control) -> bool
        Set: Visible(self: Control) = value
        """
        ...


    def AddedControl(self, *args): #cannot find CLR method
        """ AddedControl(self: Control, control: Control, index: int) """
        ...

    def ApplyStyleSheetSkin(self, page:Page): # -> 
        """ ApplyStyleSheetSkin(self: Control, page: Page) """
        ...

    def BeginRenderTracing(self, *args): #cannot find CLR method
        """ BeginRenderTracing(self: Control, writer: TextWriter, traceObject: object) """
        ...

    def BuildProfileTree(self, *args): #cannot find CLR method
        """ BuildProfileTree(self: Control, parentId: str, calcViewState: bool) """
        ...

    def ClearCachedClientID(self, *args): #cannot find CLR method
        """ ClearCachedClientID(self: Control) """
        ...

    def ClearChildControlState(self, *args): #cannot find CLR method
        """ ClearChildControlState(self: Control) """
        ...

    def ClearChildState(self, *args): #cannot find CLR method
        """ ClearChildState(self: Control) """
        ...

    def ClearChildViewState(self, *args): #cannot find CLR method
        """ ClearChildViewState(self: Control) """
        ...

    def ClearEffectiveClientIDMode(self, *args): #cannot find CLR method
        """ ClearEffectiveClientIDMode(self: Control) """
        ...

    def CreateChildControls(self, *args): #cannot find CLR method
        """ CreateChildControls(self: Control) """
        ...

    def CreateControlCollection(self, *args): #cannot find CLR method
        """ CreateControlCollection(self: Control) -> ControlCollection """
        ...

    def DataBind(self): # -> 
        """ DataBind(self: Control) """
        ...

    def DataBindChildren(self, *args): #cannot find CLR method
        """ DataBindChildren(self: Control) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: Control) """
        ...

    def EndRenderTracing(self, *args): #cannot find CLR method
        """ EndRenderTracing(self: Control, writer: TextWriter, traceObject: object) """
        ...

    def EnsureChildControls(self, *args): #cannot find CLR method
        """ EnsureChildControls(self: Control) """
        ...

    def EnsureID(self, *args): #cannot find CLR method
        """ EnsureID(self: Control) """
        ...

    def FindControl(self, id:str) -> Control:
        """ FindControl(self: Control, id: str) -> Control """
        ...

    def Focus(self): # -> 
        """ Focus(self: Control) """
        ...

    def GetRouteUrl(self, *__args:RouteValueDictionary) -> str:
        """
        GetRouteUrl(self: Control, routeParameters: RouteValueDictionary) -> str
        GetRouteUrl(self: Control, routeName: str, routeParameters: RouteValueDictionary) -> str
        GetRouteUrl(self: Control, routeParameters: object) -> str
        GetRouteUrl(self: Control, routeName: str, routeParameters: object) -> str
        """
        ...

    def GetUniqueIDRelativeTo(self, control:Control) -> str:
        """ GetUniqueIDRelativeTo(self: Control, control: Control) -> str """
        ...

    def HasControls(self) -> bool:
        """ HasControls(self: Control) -> bool """
        ...

    def HasEvents(self, *args): #cannot find CLR method
        """ HasEvents(self: Control) -> bool """
        ...

    def IsLiteralContent(self, *args): #cannot find CLR method
        """ IsLiteralContent(self: Control) -> bool """
        ...

    def LoadControlState(self, *args): #cannot find CLR method
        """ LoadControlState(self: Control, savedState: object) """
        ...

    def LoadViewState(self, *args): #cannot find CLR method
        """ LoadViewState(self: Control, savedState: object) """
        ...

    def MapPathSecure(self, *args): #cannot find CLR method
        """ MapPathSecure(self: Control, virtualPath: str) -> str """
        ...

    def OnBubbleEvent(self, *args): #cannot find CLR method
        """ OnBubbleEvent(self: Control, source: object, args: EventArgs) -> bool """
        ...

    def OnDataBinding(self, *args): #cannot find CLR method
        """ OnDataBinding(self: Control, e: EventArgs) """
        ...

    def OnInit(self, *args): #cannot find CLR method
        """ OnInit(self: Control, e: EventArgs) """
        ...

    def OnLoad(self, *args): #cannot find CLR method
        """ OnLoad(self: Control, e: EventArgs) """
        ...

    def OnPreRender(self, *args): #cannot find CLR method
        """ OnPreRender(self: Control, e: EventArgs) """
        ...

    def OnUnload(self, *args): #cannot find CLR method
        """ OnUnload(self: Control, e: EventArgs) """
        ...

    def OpenFile(self, *args): #cannot find CLR method
        """ OpenFile(self: Control, path: str) -> Stream """
        ...

    def RaiseBubbleEvent(self, *args): #cannot find CLR method
        """ RaiseBubbleEvent(self: Control, source: object, args: EventArgs) """
        ...

    def RemovedControl(self, *args): #cannot find CLR method
        """ RemovedControl(self: Control, control: Control) """
        ...

    def Render(self, *args): #cannot find CLR method
        """ Render(self: Control, writer: HtmlTextWriter) """
        ...

    def RenderChildren(self, *args): #cannot find CLR method
        """ RenderChildren(self: Control, writer: HtmlTextWriter) """
        ...

    def RenderControl(self, writer): # ->  # Not found arg types: {'writer': 'HtmlTextWriter'}
        """ RenderControl(self: Control, writer: HtmlTextWriter) """
        ...

    def ResolveAdapter(self, *args): #cannot find CLR method
        """ ResolveAdapter(self: Control) -> ControlAdapter """
        ...

    def ResolveUrl(self, relativeUrl:str) -> str:
        """ ResolveUrl(self: Control, relativeUrl: str) -> str """
        ...

    def SaveControlState(self, *args): #cannot find CLR method
        """ SaveControlState(self: Control) -> object """
        ...

    def SaveViewState(self, *args): #cannot find CLR method
        """ SaveViewState(self: Control) -> object """
        ...

    def SetRenderMethodDelegate(self, renderMethod): # ->  # Not found arg types: {'renderMethod': 'RenderMethod'}
        """ SetRenderMethodDelegate(self: Control, renderMethod: RenderMethod) """
        ...

    def SetTraceData(self, *__args): # -> 
        """ SetTraceData(self: Control, traceDataKey: object, traceDataValue: object)SetTraceData(self: Control, tracedObject: object, traceDataKey: object, traceDataValue: object) """
        ...

    def TrackViewState(self, *args): #cannot find CLR method
        """ TrackViewState(self: Control) """
        ...

    DataBinding = ...
    Disposed = ...
    Init = ...
    Load = ...
    PreRender = ...
    Unload = ...


class BasePartialCachingControl(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def CachePolicy(self): # -> ControlCachePolicy
        """ Get: CachePolicy(self: BasePartialCachingControl) -> ControlCachePolicy """
        ...

    @property
    def Dependency(self) -> CacheDependency:
        """
        Get: Dependency(self: BasePartialCachingControl) -> CacheDependency
        Set: Dependency(self: BasePartialCachingControl) = value
        """
        ...



class TemplateParser(BaseParser, IAssemblyDependencyParser): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Text(self) -> str:
        """ Get: Text(self: TemplateParser) -> str """
        ...


    def ParseFile(self, *args): #cannot find CLR method
        """ ParseFile(self: TemplateParser, physicalPath: str, virtualPath: str) """
        ...

    @staticmethod
    def ParseTemplate(content:str, virtualPath:str, ignoreFilter:bool): # -> ITemplate
        """ ParseTemplate(content: str, virtualPath: str, ignoreFilter: bool) -> ITemplate """
        ...

    def ProcessError(self, *args): #cannot find CLR method
        """ ProcessError(self: TemplateParser, message: str) """
        ...

    def ProcessException(self, *args): #cannot find CLR method
        """ ProcessException(self: TemplateParser, ex: Exception) """
        ...


class BaseTemplateParser(TemplateParser): # skipped bases: <type 'IAssemblyDependencyParser'>, <type 'object'>
    """ no doc """
    def GetReferencedType(self, *args): #cannot find CLR method
        """ GetReferencedType(self: BaseTemplateParser, virtualPath: str) -> Type """
        ...

    def GetUserControlType(self, *args): #cannot find CLR method
        """ GetUserControlType(self: BaseTemplateParser, virtualPath: str) -> Type """
        ...


class ControlBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ ControlBuilder() """
    @property
    def BindingContainerBuilder(self) -> ControlBuilder:
        """ Get: BindingContainerBuilder(self: ControlBuilder) -> ControlBuilder """
        ...

    @property
    def BindingContainerType(self) -> Type:
        """ Get: BindingContainerType(self: ControlBuilder) -> Type """
        ...

    @property
    def ComplexPropertyEntries(self) -> ICollection:
        """ Get: ComplexPropertyEntries(self: ControlBuilder) -> ICollection """
        ...

    @property
    def ControlType(self) -> Type:
        """ Get: ControlType(self: ControlBuilder) -> Type """
        ...

    @property
    def CurrentFilterResolutionService(self): # -> IFilterResolutionService
        """ Get: CurrentFilterResolutionService(self: ControlBuilder) -> IFilterResolutionService """
        ...

    @property
    def DeclareType(self) -> Type:
        """ Get: DeclareType(self: ControlBuilder) -> Type """
        ...

    @property
    def FChildrenAsProperties(self):
        ...

    @property
    def FIsNonParserAccessor(self):
        ...

    @property
    def HasAspCode(self) -> bool:
        """ Get: HasAspCode(self: ControlBuilder) -> bool """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: ControlBuilder) -> str
        Set: ID(self: ControlBuilder) = value
        """
        ...

    @property
    def InDesigner(self):
        ...

    @property
    def InPageTheme(self):
        ...

    @property
    def ItemType(self) -> str:
        """ Get: ItemType(self: ControlBuilder) -> str """
        ...

    @property
    def Localize(self) -> bool:
        """ Get: Localize(self: ControlBuilder) -> bool """
        ...

    @property
    def NamingContainerType(self) -> Type:
        """ Get: NamingContainerType(self: ControlBuilder) -> Type """
        ...

    @property
    def PageVirtualPath(self) -> str:
        """ Get: PageVirtualPath(self: ControlBuilder) -> str """
        ...

    @property
    def Parser(self):
        ...

    @property
    def ServiceProvider(self) -> IServiceProvider:
        """ Get: ServiceProvider(self: ControlBuilder) -> IServiceProvider """
        ...

    @property
    def SubBuilders(self) -> ArrayList:
        """ Get: SubBuilders(self: ControlBuilder) -> ArrayList """
        ...

    @property
    def TagName(self) -> str:
        """ Get: TagName(self: ControlBuilder) -> str """
        ...

    @property
    def TemplatePropertyEntries(self) -> ICollection:
        """ Get: TemplatePropertyEntries(self: ControlBuilder) -> ICollection """
        ...

    @property
    def ThemeResolutionService(self): # -> IThemeResolutionService
        """ Get: ThemeResolutionService(self: ControlBuilder) -> IThemeResolutionService """
        ...


    def AllowWhitespaceLiterals(self) -> bool:
        """ AllowWhitespaceLiterals(self: ControlBuilder) -> bool """
        ...

    def AppendLiteralString(self, s:str): # -> 
        """ AppendLiteralString(self: ControlBuilder, s: str) """
        ...

    def AppendSubBuilder(self, subBuilder:ControlBuilder): # -> 
        """ AppendSubBuilder(self: ControlBuilder, subBuilder: ControlBuilder) """
        ...

    def BuildObject(self) -> object:
        """ BuildObject(self: ControlBuilder) -> object """
        ...

    def CloseControl(self): # -> 
        """ CloseControl(self: ControlBuilder) """
        ...

    @staticmethod
    def CreateBuilderFromType(parser:TemplateParser, parentBuilder:ControlBuilder, type:Type, tagName:str, id:str, attribs:IDictionary, line:int, sourceFileName:str) -> ControlBuilder:
        """ CreateBuilderFromType(parser: TemplateParser, parentBuilder: ControlBuilder, type: Type, tagName: str, id: str, attribs: IDictionary, line: int, sourceFileName: str) -> ControlBuilder """
        ...

    def GetChildControlType(self, tagName:str, attribs:IDictionary) -> Type:
        """ GetChildControlType(self: ControlBuilder, tagName: str, attribs: IDictionary) -> Type """
        ...

    def GetObjectPersistData(self): # -> ObjectPersistData
        """ GetObjectPersistData(self: ControlBuilder) -> ObjectPersistData """
        ...

    def GetResourceKey(self) -> str:
        """ GetResourceKey(self: ControlBuilder) -> str """
        ...

    def HasBody(self) -> bool:
        """ HasBody(self: ControlBuilder) -> bool """
        ...

    def HtmlDecodeLiterals(self) -> bool:
        """ HtmlDecodeLiterals(self: ControlBuilder) -> bool """
        ...

    def Init(self, parser:TemplateParser, parentBuilder:ControlBuilder, type:Type, tagName:str, id:str, attribs:IDictionary): # -> 
        """ Init(self: ControlBuilder, parser: TemplateParser, parentBuilder: ControlBuilder, type: Type, tagName: str, id: str, attribs: IDictionary) """
        ...

    def NeedsTagInnerText(self) -> bool:
        """ NeedsTagInnerText(self: ControlBuilder) -> bool """
        ...

    def OnAppendToParentBuilder(self, parentBuilder:ControlBuilder): # -> 
        """ OnAppendToParentBuilder(self: ControlBuilder, parentBuilder: ControlBuilder) """
        ...

    def ProcessGeneratedCode(self, codeCompileUnit:CodeCompileUnit, baseType:CodeTypeDeclaration, derivedType:CodeTypeDeclaration, buildMethod:CodeMemberMethod, dataBindingMethod:CodeMemberMethod): # -> 
        """ ProcessGeneratedCode(self: ControlBuilder, codeCompileUnit: CodeCompileUnit, baseType: CodeTypeDeclaration, derivedType: CodeTypeDeclaration, buildMethod: CodeMemberMethod, dataBindingMethod: CodeMemberMethod) """
        ...

    def SetResourceKey(self, resourceKey:str): # -> 
        """ SetResourceKey(self: ControlBuilder, resourceKey: str) """
        ...

    def SetServiceProvider(self, serviceProvider:IServiceProvider): # -> 
        """ SetServiceProvider(self: ControlBuilder, serviceProvider: IServiceProvider) """
        ...

    def SetTagInnerText(self, text:str): # -> 
        """ SetTagInnerText(self: ControlBuilder, text: str) """
        ...

    DesignerFilter: str = ...


class TemplateBuilder(ITemplate, ControlBuilder): # skipped bases: <type 'object'>
    """ TemplateBuilder() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: TemplateBuilder) -> str
        Set: Text(self: TemplateBuilder) = value
        """
        ...



class BindableTemplateBuilder(IBindableTemplate, TemplateBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ BindableTemplateBuilder() """
    def OnAppendToParentBuilder(self, parentBuilder:ControlBuilder): # -> 
        """ OnAppendToParentBuilder(self: BindableTemplateBuilder, parentBuilder: ControlBuilder) """
        ...


class PropertyEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: PropertyEntry) -> Type """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: PropertyEntry) -> str
        Set: Filter(self: PropertyEntry) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PropertyEntry) -> str
        Set: Name(self: PropertyEntry) = value
        """
        ...

    @property
    def PropertyInfo(self) -> PropertyInfo:
        """
        Get: PropertyInfo(self: PropertyEntry) -> PropertyInfo
        Set: PropertyInfo(self: PropertyEntry) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: PropertyEntry) -> Type
        Set: Type(self: PropertyEntry) = value
        """
        ...



class BoundPropertyEntry(PropertyEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ControlID(self) -> str:
        """
        Get: ControlID(self: BoundPropertyEntry) -> str
        Set: ControlID(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def ControlType(self) -> Type:
        """
        Get: ControlType(self: BoundPropertyEntry) -> Type
        Set: ControlType(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: BoundPropertyEntry) -> str
        Set: Expression(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def ExpressionBuilder(self): # -> ExpressionBuilder
        """
        Get: ExpressionBuilder(self: BoundPropertyEntry) -> ExpressionBuilder
        Set: ExpressionBuilder(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def ExpressionPrefix(self) -> str:
        """
        Get: ExpressionPrefix(self: BoundPropertyEntry) -> str
        Set: ExpressionPrefix(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: BoundPropertyEntry) -> str
        Set: FieldName(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def FormatString(self) -> str:
        """
        Get: FormatString(self: BoundPropertyEntry) -> str
        Set: FormatString(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def Generated(self) -> bool:
        """
        Get: Generated(self: BoundPropertyEntry) -> bool
        Set: Generated(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def IsEncoded(self) -> bool:
        """
        Get: IsEncoded(self: BoundPropertyEntry) -> bool
        Set: IsEncoded(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def ParsedExpressionData(self) -> object:
        """
        Get: ParsedExpressionData(self: BoundPropertyEntry) -> object
        Set: ParsedExpressionData(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def ReadOnlyProperty(self) -> bool:
        """
        Get: ReadOnlyProperty(self: BoundPropertyEntry) -> bool
        Set: ReadOnlyProperty(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def TwoWayBound(self) -> bool:
        """
        Get: TwoWayBound(self: BoundPropertyEntry) -> bool
        Set: TwoWayBound(self: BoundPropertyEntry) = value
        """
        ...

    @property
    def UseSetAttribute(self) -> bool:
        """
        Get: UseSetAttribute(self: BoundPropertyEntry) -> bool
        Set: UseSetAttribute(self: BoundPropertyEntry) = value
        """
        ...



class BuilderPropertyEntry(PropertyEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Builder(self) -> ControlBuilder:
        """
        Get: Builder(self: BuilderPropertyEntry) -> ControlBuilder
        Set: Builder(self: BuilderPropertyEntry) = value
        """
        ...



class BuildMethod(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BuildMethod(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BuildMethod, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> Control:
        """ EndInvoke(self: BuildMethod, result: IAsyncResult) -> Control """
        ...

    def Invoke(self) -> Control:
        """ Invoke(self: BuildMethod) -> Control """
        ...


class BuildTemplateMethod(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BuildTemplateMethod(object: object, method: IntPtr) """
    def BeginInvoke(self, control:Control, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BuildTemplateMethod, control: Control, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: BuildTemplateMethod, result: IAsyncResult) """
        ...

    def Invoke(self, control:Control): # -> 
        """ Invoke(self: BuildTemplateMethod, control: Control) """
        ...


class HtmlTextWriter(TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    HtmlTextWriter(writer: TextWriter)
    HtmlTextWriter(writer: TextWriter, tabString: str)
    """
    @property
    def Indent(self) -> int:
        """
        Get: Indent(self: HtmlTextWriter) -> int
        Set: Indent(self: HtmlTextWriter) = value
        """
        ...

    @property
    def InnerWriter(self) -> TextWriter:
        """
        Get: InnerWriter(self: HtmlTextWriter) -> TextWriter
        Set: InnerWriter(self: HtmlTextWriter) = value
        """
        ...

    @property
    def TagKey(self):
        ...

    @property
    def TagName(self):
        ...


    def AddAttribute(self, *__args): # -> 
        """ AddAttribute(self: HtmlTextWriter, name: str, value: str)AddAttribute(self: HtmlTextWriter, name: str, value: str, fEndode: bool)AddAttribute(self: HtmlTextWriter, key: HtmlTextWriterAttribute, value: str)AddAttribute(self: HtmlTextWriter, key: HtmlTextWriterAttribute, value: str, fEncode: bool) """
        ...

    def AddStyleAttribute(self, *__args): # -> 
        """ AddStyleAttribute(self: HtmlTextWriter, name: str, value: str)AddStyleAttribute(self: HtmlTextWriter, key: HtmlTextWriterStyle, value: str) """
        ...

    def BeginRender(self): # -> 
        """ BeginRender(self: HtmlTextWriter) """
        ...

    def EncodeAttributeValue(self, *args): #cannot find CLR method
        """
        EncodeAttributeValue(self: HtmlTextWriter, attrKey: HtmlTextWriterAttribute, value: str) -> str
        EncodeAttributeValue(self: HtmlTextWriter, value: str, fEncode: bool) -> str
        """
        ...

    def EncodeUrl(self, *args): #cannot find CLR method
        """ EncodeUrl(self: HtmlTextWriter, url: str) -> str """
        ...

    def EndRender(self): # -> 
        """ EndRender(self: HtmlTextWriter) """
        ...

    def EnterStyle(self, style:Style, tag = ...): # ->  # Not found arg types: {'tag': 'HtmlTextWriterTag'}
        """ EnterStyle(self: HtmlTextWriter, style: Style, tag: HtmlTextWriterTag)EnterStyle(self: HtmlTextWriter, style: Style) """
        ...

    def ExitStyle(self, style:Style, tag = ...): # ->  # Not found arg types: {'tag': 'HtmlTextWriterTag'}
        """ ExitStyle(self: HtmlTextWriter, style: Style, tag: HtmlTextWriterTag)ExitStyle(self: HtmlTextWriter, style: Style) """
        ...

    def FilterAttributes(self, *args): #cannot find CLR method
        """ FilterAttributes(self: HtmlTextWriter) """
        ...

    def GetAttributeKey(self, *args): #cannot find CLR method
        """ GetAttributeKey(self: HtmlTextWriter, attrName: str) -> HtmlTextWriterAttribute """
        ...

    def GetAttributeName(self, *args): #cannot find CLR method
        """ GetAttributeName(self: HtmlTextWriter, attrKey: HtmlTextWriterAttribute) -> str """
        ...

    def GetStyleKey(self, *args): #cannot find CLR method
        """ GetStyleKey(self: HtmlTextWriter, styleName: str) -> HtmlTextWriterStyle """
        ...

    def GetStyleName(self, *args): #cannot find CLR method
        """ GetStyleName(self: HtmlTextWriter, styleKey: HtmlTextWriterStyle) -> str """
        ...

    def GetTagKey(self, *args): #cannot find CLR method
        """ GetTagKey(self: HtmlTextWriter, tagName: str) -> HtmlTextWriterTag """
        ...

    def GetTagName(self, *args): #cannot find CLR method
        """ GetTagName(self: HtmlTextWriter, tagKey: HtmlTextWriterTag) -> str """
        ...

    def IsAttributeDefined(self, *args): #cannot find CLR method
        """
        IsAttributeDefined(self: HtmlTextWriter, key: HtmlTextWriterAttribute) -> bool
        IsAttributeDefined(self: HtmlTextWriter, key: HtmlTextWriterAttribute) -> (bool, str)
        """
        ...

    def IsStyleAttributeDefined(self, *args): #cannot find CLR method
        """
        IsStyleAttributeDefined(self: HtmlTextWriter, key: HtmlTextWriterStyle) -> bool
        IsStyleAttributeDefined(self: HtmlTextWriter, key: HtmlTextWriterStyle) -> (bool, str)
        """
        ...

    def IsValidFormAttribute(self, attribute:str) -> bool:
        """ IsValidFormAttribute(self: HtmlTextWriter, attribute: str) -> bool """
        ...

    def OnAttributeRender(self, *args): #cannot find CLR method
        """ OnAttributeRender(self: HtmlTextWriter, name: str, value: str, key: HtmlTextWriterAttribute) -> bool """
        ...

    def OnStyleAttributeRender(self, *args): #cannot find CLR method
        """ OnStyleAttributeRender(self: HtmlTextWriter, name: str, value: str, key: HtmlTextWriterStyle) -> bool """
        ...

    def OnTagRender(self, *args): #cannot find CLR method
        """ OnTagRender(self: HtmlTextWriter, name: str, key: HtmlTextWriterTag) -> bool """
        ...

    def OutputTabs(self, *args): #cannot find CLR method
        """ OutputTabs(self: HtmlTextWriter) """
        ...

    def PopEndTag(self, *args): #cannot find CLR method
        """ PopEndTag(self: HtmlTextWriter) -> str """
        ...

    def PushEndTag(self, *args): #cannot find CLR method
        """ PushEndTag(self: HtmlTextWriter, endTag: str) """
        ...

    def RegisterAttribute(self, *args): #cannot find CLR method
        """ RegisterAttribute(name: str, key: HtmlTextWriterAttribute) """
        ...

    def RegisterStyle(self, *args): #cannot find CLR method
        """ RegisterStyle(name: str, key: HtmlTextWriterStyle) """
        ...

    def RegisterTag(self, *args): #cannot find CLR method
        """ RegisterTag(name: str, key: HtmlTextWriterTag) """
        ...

    def RenderAfterContent(self, *args): #cannot find CLR method
        """ RenderAfterContent(self: HtmlTextWriter) -> str """
        ...

    def RenderAfterTag(self, *args): #cannot find CLR method
        """ RenderAfterTag(self: HtmlTextWriter) -> str """
        ...

    def RenderBeforeContent(self, *args): #cannot find CLR method
        """ RenderBeforeContent(self: HtmlTextWriter) -> str """
        ...

    def RenderBeforeTag(self, *args): #cannot find CLR method
        """ RenderBeforeTag(self: HtmlTextWriter) -> str """
        ...

    def RenderBeginTag(self, *__args:str): # -> 
        """ RenderBeginTag(self: HtmlTextWriter, tagName: str)RenderBeginTag(self: HtmlTextWriter, tagKey: HtmlTextWriterTag) """
        ...

    def RenderEndTag(self): # -> 
        """ RenderEndTag(self: HtmlTextWriter) """
        ...

    def WriteAttribute(self, name:str, value:str, fEncode:bool = ...): # -> 
        """ WriteAttribute(self: HtmlTextWriter, name: str, value: str)WriteAttribute(self: HtmlTextWriter, name: str, value: str, fEncode: bool) """
        ...

    def WriteBeginTag(self, tagName:str): # -> 
        """ WriteBeginTag(self: HtmlTextWriter, tagName: str) """
        ...

    def WriteBreak(self): # -> 
        """ WriteBreak(self: HtmlTextWriter) """
        ...

    def WriteEncodedText(self, text:str): # -> 
        """ WriteEncodedText(self: HtmlTextWriter, text: str) """
        ...

    def WriteEncodedUrl(self, url:str): # -> 
        """ WriteEncodedUrl(self: HtmlTextWriter, url: str) """
        ...

    def WriteEncodedUrlParameter(self, urlText:str): # -> 
        """ WriteEncodedUrlParameter(self: HtmlTextWriter, urlText: str) """
        ...

    def WriteEndTag(self, tagName:str): # -> 
        """ WriteEndTag(self: HtmlTextWriter, tagName: str) """
        ...

    def WriteFullBeginTag(self, tagName:str): # -> 
        """ WriteFullBeginTag(self: HtmlTextWriter, tagName: str) """
        ...

    def WriteLineNoTabs(self, s:str): # -> 
        """ WriteLineNoTabs(self: HtmlTextWriter, s: str) """
        ...

    def WriteStyleAttribute(self, name:str, value:str, fEncode:bool = ...): # -> 
        """ WriteStyleAttribute(self: HtmlTextWriter, name: str, value: str)WriteStyleAttribute(self: HtmlTextWriter, name: str, value: str, fEncode: bool) """
        ...

    def WriteUrlEncodedString(self, *args): #cannot find CLR method
        """ WriteUrlEncodedString(self: HtmlTextWriter, text: str, argument: bool) """
        ...

    CoreNewLine = ...
    DefaultTabString: str = ...
    DoubleQuoteChar: Char = ...
    EndTagLeftChars: str = ...
    EqualsChar: Char = ...
    EqualsDoubleQuoteString: str = ...
    SelfClosingChars: str = ...
    SelfClosingTagEnd: str = ...
    SemicolonChar: Char = ...
    SingleQuoteChar: Char = ...
    SlashChar: Char = ...
    SpaceChar: Char = ...
    StyleEqualsChar: Char = ...
    TagLeftChar: Char = ...
    TagRightChar: Char = ...


class Html32TextWriter(HtmlTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    Html32TextWriter(writer: TextWriter)
    Html32TextWriter(writer: TextWriter, tabString: str)
    """
    @property
    def FontStack(self):
        ...

    @property
    def ShouldPerformDivTableSubstitution(self) -> bool:
        """
        Get: ShouldPerformDivTableSubstitution(self: Html32TextWriter) -> bool
        Set: ShouldPerformDivTableSubstitution(self: Html32TextWriter) = value
        """
        ...

    @property
    def SupportsBold(self) -> bool:
        """
        Get: SupportsBold(self: Html32TextWriter) -> bool
        Set: SupportsBold(self: Html32TextWriter) = value
        """
        ...

    @property
    def SupportsItalic(self) -> bool:
        """
        Get: SupportsItalic(self: Html32TextWriter) -> bool
        Set: SupportsItalic(self: Html32TextWriter) = value
        """
        ...


    CoreNewLine = ...


class ChtmlTextWriter(Html32TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ChtmlTextWriter(writer: TextWriter)
    ChtmlTextWriter(writer: TextWriter, tabString: str)
    """
    @property
    def GlobalSuppressedAttributes(self):
        ...

    @property
    def RecognizedAttributes(self):
        ...

    @property
    def SuppressedAttributes(self):
        ...


    def AddRecognizedAttribute(self, elementName:str, attributeName:str): # -> 
        """ AddRecognizedAttribute(self: ChtmlTextWriter, elementName: str, attributeName: str) """
        ...

    def RemoveRecognizedAttribute(self, elementName:str, attributeName:str): # -> 
        """ RemoveRecognizedAttribute(self: ChtmlTextWriter, elementName: str, attributeName: str) """
        ...

    def WriteBreak(self): # -> 
        """ WriteBreak(self: ChtmlTextWriter) """
        ...

    def WriteEncodedText(self, text:str): # -> 
        """ WriteEncodedText(self: ChtmlTextWriter, text: str) """
        ...

    CoreNewLine = ...


class ClientIDMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ClientIDMode, values: AutoID (1), Inherit (0), Predictable (2), Static (3) """
    AutoID: ClientIDMode = ...
    Inherit: ClientIDMode = ...
    Predictable: ClientIDMode = ...
    Static: ClientIDMode = ...
    value__ = ...


class ClientScriptManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetCallbackEventReference(self, *__args) -> str:
        """
        GetCallbackEventReference(self: ClientScriptManager, control: Control, argument: str, clientCallback: str, context: str) -> str
        GetCallbackEventReference(self: ClientScriptManager, control: Control, argument: str, clientCallback: str, context: str, useAsync: bool) -> str
        GetCallbackEventReference(self: ClientScriptManager, control: Control, argument: str, clientCallback: str, context: str, clientErrorCallback: str, useAsync: bool) -> str
        GetCallbackEventReference(self: ClientScriptManager, target: str, argument: str, clientCallback: str, context: str, clientErrorCallback: str, useAsync: bool) -> str
        """
        ...

    def GetPostBackClientHyperlink(self, control:Control, argument:str, registerForEventValidation:bool = ...) -> str:
        """
        GetPostBackClientHyperlink(self: ClientScriptManager, control: Control, argument: str) -> str
        GetPostBackClientHyperlink(self: ClientScriptManager, control: Control, argument: str, registerForEventValidation: bool) -> str
        """
        ...

    def GetPostBackEventReference(self, *__args) -> str: # Not found arg types: {'*__args': 'PostBackOptions'}
        """
        GetPostBackEventReference(self: ClientScriptManager, control: Control, argument: str) -> str
        GetPostBackEventReference(self: ClientScriptManager, control: Control, argument: str, registerForEventValidation: bool) -> str
        GetPostBackEventReference(self: ClientScriptManager, options: PostBackOptions) -> str
        GetPostBackEventReference(self: ClientScriptManager, options: PostBackOptions, registerForEventValidation: bool) -> str
        """
        ...

    def GetWebResourceUrl(self, type:Type, resourceName:str) -> str:
        """ GetWebResourceUrl(self: ClientScriptManager, type: Type, resourceName: str) -> str """
        ...

    def IsClientScriptBlockRegistered(self, *__args:str) -> bool:
        """
        IsClientScriptBlockRegistered(self: ClientScriptManager, key: str) -> bool
        IsClientScriptBlockRegistered(self: ClientScriptManager, type: Type, key: str) -> bool
        """
        ...

    def IsClientScriptIncludeRegistered(self, *__args:str) -> bool:
        """
        IsClientScriptIncludeRegistered(self: ClientScriptManager, key: str) -> bool
        IsClientScriptIncludeRegistered(self: ClientScriptManager, type: Type, key: str) -> bool
        """
        ...

    def IsOnSubmitStatementRegistered(self, *__args:str) -> bool:
        """
        IsOnSubmitStatementRegistered(self: ClientScriptManager, key: str) -> bool
        IsOnSubmitStatementRegistered(self: ClientScriptManager, type: Type, key: str) -> bool
        """
        ...

    def IsStartupScriptRegistered(self, *__args:str) -> bool:
        """
        IsStartupScriptRegistered(self: ClientScriptManager, key: str) -> bool
        IsStartupScriptRegistered(self: ClientScriptManager, type: Type, key: str) -> bool
        """
        ...

    def RegisterArrayDeclaration(self, arrayName:str, arrayValue:str): # -> 
        """ RegisterArrayDeclaration(self: ClientScriptManager, arrayName: str, arrayValue: str) """
        ...

    def RegisterClientScriptBlock(self, type:Type, key:str, script:str, addScriptTags:bool = ...): # -> 
        """ RegisterClientScriptBlock(self: ClientScriptManager, type: Type, key: str, script: str)RegisterClientScriptBlock(self: ClientScriptManager, type: Type, key: str, script: str, addScriptTags: bool) """
        ...

    def RegisterClientScriptInclude(self, *__args): # -> 
        """ RegisterClientScriptInclude(self: ClientScriptManager, key: str, url: str)RegisterClientScriptInclude(self: ClientScriptManager, type: Type, key: str, url: str) """
        ...

    def RegisterClientScriptResource(self, type:Type, resourceName:str): # -> 
        """ RegisterClientScriptResource(self: ClientScriptManager, type: Type, resourceName: str) """
        ...

    def RegisterExpandoAttribute(self, controlId:str, attributeName:str, attributeValue:str, encode:bool = ...): # -> 
        """ RegisterExpandoAttribute(self: ClientScriptManager, controlId: str, attributeName: str, attributeValue: str)RegisterExpandoAttribute(self: ClientScriptManager, controlId: str, attributeName: str, attributeValue: str, encode: bool) """
        ...

    def RegisterForEventValidation(self, *__args): # ->  # Not found arg types: {'*__args': 'PostBackOptions'}
        """ RegisterForEventValidation(self: ClientScriptManager, options: PostBackOptions)RegisterForEventValidation(self: ClientScriptManager, uniqueId: str)RegisterForEventValidation(self: ClientScriptManager, uniqueId: str, argument: str) """
        ...

    def RegisterHiddenField(self, hiddenFieldName:str, hiddenFieldInitialValue:str): # -> 
        """ RegisterHiddenField(self: ClientScriptManager, hiddenFieldName: str, hiddenFieldInitialValue: str) """
        ...

    def RegisterOnSubmitStatement(self, type:Type, key:str, script:str): # -> 
        """ RegisterOnSubmitStatement(self: ClientScriptManager, type: Type, key: str, script: str) """
        ...

    def RegisterStartupScript(self, type:Type, key:str, script:str, addScriptTags:bool = ...): # -> 
        """ RegisterStartupScript(self: ClientScriptManager, type: Type, key: str, script: str)RegisterStartupScript(self: ClientScriptManager, type: Type, key: str, script: str, addScriptTags: bool) """
        ...

    def ValidateEvent(self, uniqueId:str, argument:str = ...): # -> 
        """ ValidateEvent(self: ClientScriptManager, uniqueId: str)ValidateEvent(self: ClientScriptManager, uniqueId: str, argument: str) """
        ...


class CodeBlockType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeBlockType, values: Code (0), DataBinding (2), EncodedExpression (3), Expression (1) """
    Code: CodeBlockType = ...
    DataBinding: CodeBlockType = ...
    EncodedExpression: CodeBlockType = ...
    Expression: CodeBlockType = ...
    value__ = ...


class CodeConstructType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeConstructType, values: CodeSnippet (0), DataBindingSnippet (2), EncodedExpressionSnippet (4), ExpressionSnippet (1), ScriptTag (3) """
    CodeSnippet: CodeConstructType = ...
    DataBindingSnippet: CodeConstructType = ...
    EncodedExpressionSnippet: CodeConstructType = ...
    ExpressionSnippet: CodeConstructType = ...
    ScriptTag: CodeConstructType = ...
    value__ = ...


class CodeStatementBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ no doc """
    def BuildStatement(self, writerReferenceExpression:CodeArgumentReferenceExpression) -> CodeStatement:
        """ BuildStatement(self: CodeStatementBuilder, writerReferenceExpression: CodeArgumentReferenceExpression) -> CodeStatement """
        ...


class CompilationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompilationMode, values: Always (2), Auto (0), Never (1) """
    Always: CompilationMode = ...
    Auto: CompilationMode = ...
    Never: CompilationMode = ...
    value__ = ...


class CompiledBindableTemplateBuilder(IBindableTemplate): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ CompiledBindableTemplateBuilder(buildTemplateMethod: BuildTemplateMethod, extractTemplateValuesMethod: ExtractTemplateValuesMethod) """
    def InstantiateIn(self, container:Control): # -> 
        """ InstantiateIn(self: CompiledBindableTemplateBuilder, container: Control) """
        ...


class CompiledTemplateBuilder(ITemplate): # skipped bases: <type 'object'>
    """ CompiledTemplateBuilder(buildTemplateMethod: BuildTemplateMethod) """
    pass

class ComplexPropertyEntry(BuilderPropertyEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsCollectionItem(self) -> bool:
        """ Get: IsCollectionItem(self: ComplexPropertyEntry) -> bool """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: ComplexPropertyEntry) -> bool
        Set: ReadOnly(self: ComplexPropertyEntry) = value
        """
        ...



class ScriptReferenceBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NotifyScriptLoaded(self) -> bool:
        """
        Get: NotifyScriptLoaded(self: ScriptReferenceBase) -> bool
        Set: NotifyScriptLoaded(self: ScriptReferenceBase) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ScriptReferenceBase) -> str
        Set: Path(self: ScriptReferenceBase) = value
        """
        ...

    @property
    def ResourceUICultures(self) -> Array:
        """
        Get: ResourceUICultures(self: ScriptReferenceBase) -> Array[str]
        Set: ResourceUICultures(self: ScriptReferenceBase) = value
        """
        ...

    @property
    def ScriptMode(self): # -> ScriptMode
        """
        Get: ScriptMode(self: ScriptReferenceBase) -> ScriptMode
        Set: ScriptMode(self: ScriptReferenceBase) = value
        """
        ...


    def GetUrl(self, *args): #cannot find CLR method
        """ GetUrl(self: ScriptReferenceBase, scriptManager: ScriptManager, zip: bool) -> str """
        ...

    def IsAjaxFrameworkScript(self, *args): #cannot find CLR method
        """ IsAjaxFrameworkScript(self: ScriptReferenceBase, scriptManager: ScriptManager) -> bool """
        ...

    def IsFromSystemWebExtensions(self, *args): #cannot find CLR method
        """ IsFromSystemWebExtensions(self: ScriptReferenceBase) -> bool """
        ...

    def ReplaceExtension(self, *args): #cannot find CLR method
        """ ReplaceExtension(pathOrName: str) -> str """
        ...


class CompositeScriptReference(ScriptReferenceBase): # skipped bases: <type 'object'>
    """ CompositeScriptReference() """
    @property
    def Scripts(self): # -> ScriptReferenceCollection
        """ Get: Scripts(self: CompositeScriptReference) -> ScriptReferenceCollection """
        ...



class CompositeScriptReferenceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ CompositeScriptReferenceEventArgs(compositeScript: CompositeScriptReference) """
    @property
    def CompositeScript(self) -> CompositeScriptReference:
        """ Get: CompositeScript(self: CompositeScriptReferenceEventArgs) -> CompositeScriptReference """
        ...


    def __new__(cls, compositeScript:CompositeScriptReference) -> Self:
        """ __new__(cls: type, compositeScript: CompositeScriptReference) """
        ...


class ConflictOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConflictOptions, values: CompareAllValues (1), OverwriteChanges (0) """
    CompareAllValues: ConflictOptions = ...
    OverwriteChanges: ConflictOptions = ...
    value__ = ...


class ConstructorNeedsTagAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ConstructorNeedsTagAttribute()
    ConstructorNeedsTagAttribute(needsTag: bool)
    """
    @property
    def NeedsTag(self) -> bool:
        """ Get: NeedsTag(self: ConstructorNeedsTagAttribute) -> bool """
        ...


    def __new__(cls, needsTag:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, needsTag: bool)
        """
        ...


class ControlBuilderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ControlBuilderAttribute(builderType: Type) """
    @property
    def BuilderType(self) -> Type:
        """ Get: BuilderType(self: ControlBuilderAttribute) -> Type """
        ...


    def __new__(cls, builderType:Type) -> Self:
        """ __new__(cls: type, builderType: Type) """
        ...

    Default: ControlBuilderAttribute = ...


class ControlCachePolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cached(self) -> bool:
        """
        Get: Cached(self: ControlCachePolicy) -> bool
        Set: Cached(self: ControlCachePolicy) = value
        """
        ...

    @property
    def Dependency(self) -> CacheDependency:
        """
        Get: Dependency(self: ControlCachePolicy) -> CacheDependency
        Set: Dependency(self: ControlCachePolicy) = value
        """
        ...

    @property
    def Duration(self) -> TimeSpan:
        """
        Get: Duration(self: ControlCachePolicy) -> TimeSpan
        Set: Duration(self: ControlCachePolicy) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: ControlCachePolicy) -> str
        Set: ProviderName(self: ControlCachePolicy) = value
        """
        ...

    @property
    def SupportsCaching(self) -> bool:
        """ Get: SupportsCaching(self: ControlCachePolicy) -> bool """
        ...

    @property
    def VaryByControl(self) -> str:
        """
        Get: VaryByControl(self: ControlCachePolicy) -> str
        Set: VaryByControl(self: ControlCachePolicy) = value
        """
        ...

    @property
    def VaryByParams(self): # -> HttpCacheVaryByParams
        """ Get: VaryByParams(self: ControlCachePolicy) -> HttpCacheVaryByParams """
        ...


    def SetExpires(self, expirationTime:DateTime): # -> 
        """ SetExpires(self: ControlCachePolicy, expirationTime: DateTime) """
        ...

    def SetSlidingExpiration(self, useSlidingExpiration:bool): # -> 
        """ SetSlidingExpiration(self: ControlCachePolicy, useSlidingExpiration: bool) """
        ...

    def SetVaryByCustom(self, varyByCustom:str): # -> 
        """ SetVaryByCustom(self: ControlCachePolicy, varyByCustom: str) """
        ...


class ControlCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ControlCollection(owner: Control) """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ControlCollection) -> bool """
        ...

    @property
    def Owner(self):
        ...


    def Add(self, child:Control): # -> 
        """ Add(self: ControlCollection, child: Control) """
        ...

    def AddAt(self, index:int, child:Control): # -> 
        """ AddAt(self: ControlCollection, index: int, child: Control) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ControlCollection) """
        ...

    def Contains(self, c:Control) -> bool:
        """ Contains(self: ControlCollection, c: Control) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ControlCollection) -> IEnumerator """
        ...

    def IndexOf(self, value:Control) -> int:
        """ IndexOf(self: ControlCollection, value: Control) -> int """
        ...

    def Remove(self, value:Control): # -> 
        """ Remove(self: ControlCollection, value: Control) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ControlCollection, index: int) """
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


class ControlSkin: # skipped bases: <type 'object'>, <type 'object'>
    """ ControlSkin(controlType: Type, themeDelegate: ControlSkinDelegate) """
    @property
    def ControlType(self) -> Type:
        """ Get: ControlType(self: ControlSkin) -> Type """
        ...


    def ApplySkin(self, control:Control): # -> 
        """ ApplySkin(self: ControlSkin, control: Control) """
        ...


class ControlSkinDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ControlSkinDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, control:Control, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ControlSkinDelegate, control: Control, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> Control:
        """ EndInvoke(self: ControlSkinDelegate, result: IAsyncResult) -> Control """
        ...

    def Invoke(self, control:Control) -> Control:
        """ Invoke(self: ControlSkinDelegate, control: Control) -> Control """
        ...


class ControlValuePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ControlValuePropertyAttribute(name: str)
    ControlValuePropertyAttribute(name: str, defaultValue: object)
    ControlValuePropertyAttribute(name: str, type: Type, defaultValue: str)
    """
    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: ControlValuePropertyAttribute) -> object """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ControlValuePropertyAttribute) -> str """
        ...


    def __new__(cls, name:str, *__args:object) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, defaultValue: object)
        __new__(cls: type, name: str, type: Type, defaultValue: str)
        """
        ...


class CssClassPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CssClassPropertyAttribute() """
    pass

class CssStyleCollection: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CssStyleCollection) -> int """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: CssStyleCollection) -> ICollection """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: CssStyleCollection) -> str
        Set: Value(self: CssStyleCollection) = value
        """
        ...


    def Add(self, key:str, value:str): # -> 
        """ Add(self: CssStyleCollection, key: str, value: str)Add(self: CssStyleCollection, key: HtmlTextWriterStyle, value: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CssStyleCollection) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: CssStyleCollection, key: str)Remove(self: CssStyleCollection, key: HtmlTextWriterStyle) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class DataBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ DataBinder() """
    @property
    def EnableCaching(self) -> bool:
        """
        Get: EnableCaching() -> bool
        Set: EnableCaching() = value
        """
        ...


    @staticmethod
    def Eval(container:object, expression:str, format:str = ...) -> str:
        """
        Eval(container: object, expression: str) -> object
        Eval(container: object, expression: str, format: str) -> str
        """
        ...

    @staticmethod
    def GetDataItem(container, foundDataItem=None) -> object:
        """
        GetDataItem(container: object) -> object
        GetDataItem(container: object) -> (object, bool)
        """
        ...

    @staticmethod
    def GetIndexedPropertyValue(container:object, *__args:str) -> object:
        """
        GetIndexedPropertyValue(container: object, propName: str, format: str) -> str
        GetIndexedPropertyValue(container: object, expr: str) -> object
        """
        ...

    @staticmethod
    def GetPropertyValue(container:object, propName:str, format:str = ...) -> str:
        """
        GetPropertyValue(container: object, propName: str, format: str) -> str
        GetPropertyValue(container: object, propName: str) -> object
        """
        ...

    @staticmethod
    def IsBindableType(type:Type) -> bool:
        """ IsBindableType(type: Type) -> bool """
        ...



class DataBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ DataBinding(propertyName: str, propertyType: Type, expression: str) """
    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: DataBinding) -> str
        Set: Expression(self: DataBinding) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: DataBinding) -> str """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: DataBinding) -> Type """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: DataBinding, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DataBinding) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DataBindingCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ DataBindingCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataBindingCollection) -> bool """
        ...

    @property
    def RemovedBindings(self) -> Array:
        """ Get: RemovedBindings(self: DataBindingCollection) -> Array[str] """
        ...


    def Add(self, binding:DataBinding): # -> 
        """ Add(self: DataBindingCollection, binding: DataBinding) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataBindingCollection) """
        ...

    def Contains(self, propertyName:str) -> bool:
        """ Contains(self: DataBindingCollection, propertyName: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataBindingCollection) -> IEnumerator """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: DataBindingCollection, propertyName: str)Remove(self: DataBindingCollection, binding: DataBinding)Remove(self: DataBindingCollection, propertyName: str, addToRemovedList: bool) """
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

    Changed = ...


class DataBindingHandlerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataBindingHandlerAttribute()
    DataBindingHandlerAttribute(type: Type)
    DataBindingHandlerAttribute(typeName: str)
    """
    @property
    def HandlerTypeName(self) -> str:
        """ Get: HandlerTypeName(self: DataBindingHandlerAttribute) -> str """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        ...

    Default: DataBindingHandlerAttribute = ...


class ITextControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: ITextControl) -> str
        Set: Text(self: ITextControl) = value
        """
        ...



class DataBoundLiteralControl(Control, ITextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DataBoundLiteralControl(staticLiteralsCount: int, dataBoundLiteralCount: int) """
    def SetDataBoundString(self, index:int, s:str): # -> 
        """ SetDataBoundString(self: DataBoundLiteralControl, index: int, s: str) """
        ...

    def SetStaticString(self, index:int, s:str): # -> 
        """ SetStaticString(self: DataBoundLiteralControl, index: int, s: str) """
        ...

    def __new__(cls, staticLiteralsCount:int, dataBoundLiteralCount:int) -> Self:
        """ __new__(cls: type, staticLiteralsCount: int, dataBoundLiteralCount: int) """
        ...


class DataControlExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EnableDynamicData(control, entityType:Type, *__args:object): # ->  # Not found arg types: {'control': 'INamingContainer'}
        """ EnableDynamicData(control: INamingContainer, entityType: Type, defaults: object)EnableDynamicData(control: INamingContainer, entityType: Type, defaultValues: IDictionary[str, object])EnableDynamicData(control: INamingContainer, entityType: Type) """
        ...

    __all__: list = ...


class DataKeyPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataKeyPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DataKeyPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class DataSourceCacheDurationConverter(Int32Converter): # skipped bases: <type 'object'>
    """ DataSourceCacheDurationConverter() """
    def CanConvertFrom(self, *__args) -> bool:
        """ CanConvertFrom(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        ...

    def CanConvertTo(self, *__args) -> bool:
        """ CanConvertTo(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        ...

    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        ...

    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: DataSourceCacheDurationConverter, context: ITypeDescriptorContext) -> bool """
        ...


class DataSourceCacheExpiry(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataSourceCacheExpiry, values: Absolute (0), Sliding (1) """
    Absolute: DataSourceCacheExpiry = ...
    Sliding: DataSourceCacheExpiry = ...
    value__ = ...


class DataSourceCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataSourceCapabilities, values: None (0), Page (2), RetrieveTotalRowCount (4), Sort (1) """
    Page: DataSourceCapabilities = ...
    RetrieveTotalRowCount: DataSourceCapabilities = ...
    Sort: DataSourceCapabilities = ...
    value__ = ...


class IDataSource: # skipped bases: <type 'object'>
    """ no doc """
    def GetView(self, viewName:str): # -> DataSourceView
        """ GetView(self: IDataSource, viewName: str) -> DataSourceView """
        ...

    def GetViewNames(self) -> ICollection:
        """ GetViewNames(self: IDataSource) -> ICollection """
        ...

    DataSourceChanged = ...


class DataSourceControl(Control, IDataSource, IListSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    def RaiseDataSourceChangedEvent(self, *args): #cannot find CLR method
        """ RaiseDataSourceChangedEvent(self: DataSourceControl, e: EventArgs) """
        ...


class DataSourceControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ DataSourceControlBuilder() """
    pass

class DataSourceOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataSourceOperation, values: Delete (0), Insert (1), Select (2), SelectCount (4), Update (3) """
    Delete: DataSourceOperation = ...
    Insert: DataSourceOperation = ...
    Select: DataSourceOperation = ...
    SelectCount: DataSourceOperation = ...
    Update: DataSourceOperation = ...
    value__ = ...


class DataSourceSelectArguments: # skipped bases: <type 'object'>, <type 'object'>
    """
    DataSourceSelectArguments()
    DataSourceSelectArguments(sortExpression: str)
    DataSourceSelectArguments(startRowIndex: int, maximumRows: int)
    DataSourceSelectArguments(sortExpression: str, startRowIndex: int, maximumRows: int)
    """
    @property
    def Empty(self) -> DataSourceSelectArguments:
        """ Get: Empty() -> DataSourceSelectArguments """
        ...

    @property
    def MaximumRows(self) -> int:
        """
        Get: MaximumRows(self: DataSourceSelectArguments) -> int
        Set: MaximumRows(self: DataSourceSelectArguments) = value
        """
        ...

    @property
    def RetrieveTotalRowCount(self) -> bool:
        """
        Get: RetrieveTotalRowCount(self: DataSourceSelectArguments) -> bool
        Set: RetrieveTotalRowCount(self: DataSourceSelectArguments) = value
        """
        ...

    @property
    def SortExpression(self) -> str:
        """
        Get: SortExpression(self: DataSourceSelectArguments) -> str
        Set: SortExpression(self: DataSourceSelectArguments) = value
        """
        ...

    @property
    def StartRowIndex(self) -> int:
        """
        Get: StartRowIndex(self: DataSourceSelectArguments) -> int
        Set: StartRowIndex(self: DataSourceSelectArguments) = value
        """
        ...

    @property
    def TotalRowCount(self) -> int:
        """
        Get: TotalRowCount(self: DataSourceSelectArguments) -> int
        Set: TotalRowCount(self: DataSourceSelectArguments) = value
        """
        ...


    def AddSupportedCapabilities(self, capabilities:DataSourceCapabilities): # -> 
        """ AddSupportedCapabilities(self: DataSourceSelectArguments, capabilities: DataSourceCapabilities) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: DataSourceSelectArguments, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DataSourceSelectArguments) -> int """
        ...

    def RaiseUnsupportedCapabilitiesError(self, view): # ->  # Not found arg types: {'view': 'DataSourceView'}
        """ RaiseUnsupportedCapabilitiesError(self: DataSourceSelectArguments, view: DataSourceView) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class DataSourceView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanDelete(self) -> bool:
        """ Get: CanDelete(self: DataSourceView) -> bool """
        ...

    @property
    def CanInsert(self) -> bool:
        """ Get: CanInsert(self: DataSourceView) -> bool """
        ...

    @property
    def CanPage(self) -> bool:
        """ Get: CanPage(self: DataSourceView) -> bool """
        ...

    @property
    def CanRetrieveTotalRowCount(self) -> bool:
        """ Get: CanRetrieveTotalRowCount(self: DataSourceView) -> bool """
        ...

    @property
    def CanSort(self) -> bool:
        """ Get: CanSort(self: DataSourceView) -> bool """
        ...

    @property
    def CanUpdate(self) -> bool:
        """ Get: CanUpdate(self: DataSourceView) -> bool """
        ...

    @property
    def Events(self):
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataSourceView) -> str """
        ...


    def CanExecute(self, commandName:str) -> bool:
        """ CanExecute(self: DataSourceView, commandName: str) -> bool """
        ...

    def Delete(self, keys:IDictionary, oldValues:IDictionary, callback): # ->  # Not found arg types: {'callback': 'DataSourceViewOperationCallback'}
        """ Delete(self: DataSourceView, keys: IDictionary, oldValues: IDictionary, callback: DataSourceViewOperationCallback) """
        ...

    def ExecuteCommand(self, commandName:str, keys:IDictionary, values:IDictionary, callback): # ->  # Not found arg types: {'callback': 'DataSourceViewOperationCallback'}
        """ ExecuteCommand(self: DataSourceView, commandName: str, keys: IDictionary, values: IDictionary, callback: DataSourceViewOperationCallback) """
        ...

    def ExecuteDelete(self, *args): #cannot find CLR method
        """ ExecuteDelete(self: DataSourceView, keys: IDictionary, oldValues: IDictionary) -> int """
        ...

    def ExecuteInsert(self, *args): #cannot find CLR method
        """ ExecuteInsert(self: DataSourceView, values: IDictionary) -> int """
        ...

    def ExecuteSelect(self, *args): #cannot find CLR method
        """ ExecuteSelect(self: DataSourceView, arguments: DataSourceSelectArguments) -> IEnumerable """
        ...

    def ExecuteUpdate(self, *args): #cannot find CLR method
        """ ExecuteUpdate(self: DataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary) -> int """
        ...

    def Insert(self, values:IDictionary, callback): # ->  # Not found arg types: {'callback': 'DataSourceViewOperationCallback'}
        """ Insert(self: DataSourceView, values: IDictionary, callback: DataSourceViewOperationCallback) """
        ...

    def OnDataSourceViewChanged(self, *args): #cannot find CLR method
        """ OnDataSourceViewChanged(self: DataSourceView, e: EventArgs) """
        ...

    def RaiseUnsupportedCapabilityError(self, *args): #cannot find CLR method
        """ RaiseUnsupportedCapabilityError(self: DataSourceView, capability: DataSourceCapabilities) """
        ...

    def Select(self, arguments:DataSourceSelectArguments, callback): # ->  # Not found arg types: {'callback': 'DataSourceViewSelectCallback'}
        """ Select(self: DataSourceView, arguments: DataSourceSelectArguments, callback: DataSourceViewSelectCallback) """
        ...

    def Update(self, keys:IDictionary, values:IDictionary, oldValues:IDictionary, callback): # ->  # Not found arg types: {'callback': 'DataSourceViewOperationCallback'}
        """ Update(self: DataSourceView, keys: IDictionary, values: IDictionary, oldValues: IDictionary, callback: DataSourceViewOperationCallback) """
        ...

    DataSourceViewChanged = ...


class DataSourceViewOperationCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataSourceViewOperationCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, affectedRecords:int, ex:Exception, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataSourceViewOperationCallback, affectedRecords: int, ex: Exception, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DataSourceViewOperationCallback, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, affectedRecords:int, ex:Exception) -> bool:
        """ Invoke(self: DataSourceViewOperationCallback, affectedRecords: int, ex: Exception) -> bool """
        ...


class DataSourceViewSelectCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataSourceViewSelectCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, data:IEnumerable, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataSourceViewSelectCallback, data: IEnumerable, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataSourceViewSelectCallback, result: IAsyncResult) """
        ...

    def Invoke(self, data:IEnumerable): # -> 
        """ Invoke(self: DataSourceViewSelectCallback, data: IEnumerable) """
        ...


class DesignerDataBoundLiteralControl(Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ DesignerDataBoundLiteralControl() """
    @property
    def Text(self) -> str:
        """
        Get: Text(self: DesignerDataBoundLiteralControl) -> str
        Set: Text(self: DesignerDataBoundLiteralControl) = value
        """
        ...



class DesignTimeParseData: # skipped bases: <type 'object'>, <type 'object'>
    """
    DesignTimeParseData(designerHost: IDesignerHost, parseText: str)
    DesignTimeParseData(designerHost: IDesignerHost, parseText: str, filter: str)
    """
    @property
    def DataBindingHandler(self) -> EventHandler:
        """
        Get: DataBindingHandler(self: DesignTimeParseData) -> EventHandler
        Set: DataBindingHandler(self: DesignTimeParseData) = value
        """
        ...

    @property
    def DesignerHost(self) -> IDesignerHost:
        """ Get: DesignerHost(self: DesignTimeParseData) -> IDesignerHost """
        ...

    @property
    def DocumentUrl(self) -> str:
        """
        Get: DocumentUrl(self: DesignTimeParseData) -> str
        Set: DocumentUrl(self: DesignTimeParseData) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """ Get: Filter(self: DesignTimeParseData) -> str """
        ...

    @property
    def ParseText(self) -> str:
        """ Get: ParseText(self: DesignTimeParseData) -> str """
        ...

    @property
    def ShouldApplyTheme(self) -> bool:
        """
        Get: ShouldApplyTheme(self: DesignTimeParseData) -> bool
        Set: ShouldApplyTheme(self: DesignTimeParseData) = value
        """
        ...

    @property
    def UserControlRegisterEntries(self) -> ICollection:
        """ Get: UserControlRegisterEntries(self: DesignTimeParseData) -> ICollection """
        ...



class DesignTimeTemplateParser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ParseControl(data:DesignTimeParseData) -> Control:
        """ ParseControl(data: DesignTimeParseData) -> Control """
        ...

    @staticmethod
    def ParseControls(data:DesignTimeParseData) -> Array:
        """ ParseControls(data: DesignTimeParseData) -> Array[Control] """
        ...

    @staticmethod
    def ParseTemplate(data:DesignTimeParseData): # -> ITemplate
        """ ParseTemplate(data: DesignTimeParseData) -> ITemplate """
        ...

    @staticmethod
    def ParseTheme(host:IDesignerHost, theme:str, themePath:str) -> ControlBuilder:
        """ ParseTheme(host: IDesignerHost, theme: str, themePath: str) -> ControlBuilder """
        ...

    __all__: list = ...


class EmptyControlCollection(ControlCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ EmptyControlCollection(owner: Control) """
    pass

class EventEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ EventEntry() """
    @property
    def HandlerMethodName(self) -> str:
        """
        Get: HandlerMethodName(self: EventEntry) -> str
        Set: HandlerMethodName(self: EventEntry) = value
        """
        ...

    @property
    def HandlerType(self) -> Type:
        """
        Get: HandlerType(self: EventEntry) -> Type
        Set: HandlerType(self: EventEntry) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EventEntry) -> str
        Set: Name(self: EventEntry) = value
        """
        ...



class ExpressionBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ ExpressionBinding(propertyName: str, propertyType: Type, expressionPrefix: str, expression: str) """
    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: ExpressionBinding) -> str
        Set: Expression(self: ExpressionBinding) = value
        """
        ...

    @property
    def ExpressionPrefix(self) -> str:
        """
        Get: ExpressionPrefix(self: ExpressionBinding) -> str
        Set: ExpressionPrefix(self: ExpressionBinding) = value
        """
        ...

    @property
    def Generated(self) -> bool:
        """ Get: Generated(self: ExpressionBinding) -> bool """
        ...

    @property
    def ParsedExpressionData(self) -> object:
        """ Get: ParsedExpressionData(self: ExpressionBinding) -> object """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ExpressionBinding) -> str """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: ExpressionBinding) -> Type """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ExpressionBinding, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExpressionBinding) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ExpressionBindingCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ExpressionBindingCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ExpressionBindingCollection) -> bool """
        ...

    @property
    def RemovedBindings(self) -> ICollection:
        """ Get: RemovedBindings(self: ExpressionBindingCollection) -> ICollection """
        ...


    def Add(self, binding:ExpressionBinding): # -> 
        """ Add(self: ExpressionBindingCollection, binding: ExpressionBinding) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ExpressionBindingCollection) """
        ...

    def Contains(self, propName:str) -> bool:
        """ Contains(self: ExpressionBindingCollection, propName: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ExpressionBindingCollection) -> IEnumerator """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: ExpressionBindingCollection, propertyName: str)Remove(self: ExpressionBindingCollection, binding: ExpressionBinding)Remove(self: ExpressionBindingCollection, propertyName: str, addToRemovedList: bool) """
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

    Changed = ...


class IExtenderControl: # skipped bases: <type 'object'>
    """ no doc """
    def GetScriptDescriptors(self, targetControl:Control) -> IEnumerable:
        """ GetScriptDescriptors(self: IExtenderControl, targetControl: Control) -> IEnumerable[ScriptDescriptor] """
        ...

    def GetScriptReferences(self) -> IEnumerable:
        """ GetScriptReferences(self: IExtenderControl) -> IEnumerable[ScriptReference] """
        ...


class ExtenderControl(Control, IExtenderControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def TargetControlID(self) -> str:
        """
        Get: TargetControlID(self: ExtenderControl) -> str
        Set: TargetControlID(self: ExtenderControl) = value
        """
        ...



class ExtractTemplateValuesMethod(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ExtractTemplateValuesMethod(object: object, method: IntPtr) """
    def BeginInvoke(self, control:Control, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ExtractTemplateValuesMethod, control: Control, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> IOrderedDictionary:
        """ EndInvoke(self: ExtractTemplateValuesMethod, result: IAsyncResult) -> IOrderedDictionary """
        ...

    def Invoke(self, control:Control) -> IOrderedDictionary:
        """ Invoke(self: ExtractTemplateValuesMethod, control: Control) -> IOrderedDictionary """
        ...


class FileLevelControlBuilderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FileLevelControlBuilderAttribute(builderType: Type) """
    @property
    def BuilderType(self) -> Type:
        """ Get: BuilderType(self: FileLevelControlBuilderAttribute) -> Type """
        ...


    def __new__(cls, builderType:Type) -> Self:
        """ __new__(cls: type, builderType: Type) """
        ...

    Default: FileLevelControlBuilderAttribute = ...


class RootBuilder(TemplateBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """
    RootBuilder()
    RootBuilder(parser: TemplateParser)
    """
    @property
    def BuiltObjects(self) -> IDictionary:
        """ Get: BuiltObjects(self: RootBuilder) -> IDictionary """
        ...


    def GetChildControlType(self, tagName:str, attribs:IDictionary) -> Type:
        """ GetChildControlType(self: RootBuilder, tagName: str, attribs: IDictionary) -> Type """
        ...

    def OnCodeGenerationComplete(self, *args): #cannot find CLR method
        """ OnCodeGenerationComplete(self: RootBuilder) """
        ...

    def __new__(cls, parser:TemplateParser = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parser: TemplateParser)
        """
        ...


class FileLevelPageControlBuilder(RootBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ FileLevelPageControlBuilder() """
    def AppendLiteralString(self, text:str): # -> 
        """ AppendLiteralString(self: FileLevelPageControlBuilder, text: str) """
        ...

    def AppendSubBuilder(self, subBuilder:ControlBuilder): # -> 
        """ AppendSubBuilder(self: FileLevelPageControlBuilder, subBuilder: ControlBuilder) """
        ...


class FileLevelMasterPageControlBuilder(FileLevelPageControlBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ FileLevelMasterPageControlBuilder() """
    pass

class FileLevelUserControlBuilder(RootBuilder): # skipped bases: <type 'ITemplate'>, <type 'object'>
    """ FileLevelUserControlBuilder() """
    pass

class FilterableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FilterableAttribute(filterable: bool) """
    @property
    def Filterable(self) -> bool:
        """ Get: Filterable(self: FilterableAttribute) -> bool """
        ...


    @staticmethod
    def IsObjectFilterable(instance:object) -> bool:
        """ IsObjectFilterable(instance: object) -> bool """
        ...

    @staticmethod
    def IsPropertyFilterable(propertyDescriptor:PropertyDescriptor) -> bool:
        """ IsPropertyFilterable(propertyDescriptor: PropertyDescriptor) -> bool """
        ...

    @staticmethod
    def IsTypeFilterable(type:Type) -> bool:
        """ IsTypeFilterable(type: Type) -> bool """
        ...

    def __new__(cls, filterable:bool) -> Self:
        """ __new__(cls: type, filterable: bool) """
        ...

    Default: FilterableAttribute = ...
    No: FilterableAttribute = ...
    Yes: FilterableAttribute = ...


class PageStatePersister: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ControlState(self) -> object:
        """
        Get: ControlState(self: PageStatePersister) -> object
        Set: ControlState(self: PageStatePersister) = value
        """
        ...

    @property
    def Page(self):
        ...

    @property
    def StateFormatter(self):
        ...

    @property
    def ViewState(self) -> object:
        """
        Get: ViewState(self: PageStatePersister) -> object
        Set: ViewState(self: PageStatePersister) = value
        """
        ...


    def Load(self): # -> 
        """ Load(self: PageStatePersister) """
        ...

    def Save(self): # -> 
        """ Save(self: PageStatePersister) """
        ...


class HiddenFieldPageStatePersister(PageStatePersister): # skipped bases: <type 'object'>
    """ HiddenFieldPageStatePersister(page: Page) """
    pass

class IHierarchicalDataSource: # skipped bases: <type 'object'>
    """ no doc """
    def GetHierarchicalView(self, viewPath:str): # -> HierarchicalDataSourceView
        """ GetHierarchicalView(self: IHierarchicalDataSource, viewPath: str) -> HierarchicalDataSourceView """
        ...

    DataSourceChanged = ...


class HierarchicalDataSourceControl(Control, IHierarchicalDataSource): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    def OnDataSourceChanged(self, *args): #cannot find CLR method
        """ OnDataSourceChanged(self: HierarchicalDataSourceControl, e: EventArgs) """
        ...


class HierarchicalDataSourceView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Select(self): # -> IHierarchicalEnumerable
        """ Select(self: HierarchicalDataSourceView) -> IHierarchicalEnumerable """
        ...


class HistoryEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ HistoryEventArgs(state: NameValueCollection) """
    @property
    def State(self) -> NameValueCollection:
        """ Get: State(self: HistoryEventArgs) -> NameValueCollection """
        ...


    def __new__(cls, state:NameValueCollection) -> Self:
        """ __new__(cls: type, state: NameValueCollection) """
        ...


class HtmlTextWriterAttribute(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HtmlTextWriterAttribute, values: Abbr (40), Accesskey (0), Align (1), Alt (2), AutoComplete (41), Axis (42), Background (3), Bgcolor (4), Border (5), Bordercolor (6), Cellpadding (7), Cellspacing (8), Checked (9), Class (10), Cols (11), Colspan (12), Content (43), Coords (44), DesignerRegion (45), Dir (46), Disabled (13), For (14), Headers (47), Height (15), Href (16), Id (17), Longdesc (48), Maxlength (18), Multiple (19), Name (20), Nowrap (21), Onchange (22), Onclick (23), ReadOnly (24), Rel (49), Rows (25), Rowspan (26), Rules (27), Scope (50), Selected (28), Shape (51), Size (29), Src (30), Style (31), Tabindex (32), Target (33), Title (34), Type (35), Usemap (52), Valign (36), Value (37), VCardName (53), Width (38), Wrap (39) """
    Abbr: HtmlTextWriterAttribute = ...
    Accesskey: HtmlTextWriterAttribute = ...
    Align: HtmlTextWriterAttribute = ...
    Alt: HtmlTextWriterAttribute = ...
    AutoComplete: HtmlTextWriterAttribute = ...
    Axis: HtmlTextWriterAttribute = ...
    Background: HtmlTextWriterAttribute = ...
    Bgcolor: HtmlTextWriterAttribute = ...
    Border: HtmlTextWriterAttribute = ...
    Bordercolor: HtmlTextWriterAttribute = ...
    Cellpadding: HtmlTextWriterAttribute = ...
    Cellspacing: HtmlTextWriterAttribute = ...
    Checked: HtmlTextWriterAttribute = ...
    Class: HtmlTextWriterAttribute = ...
    Cols: HtmlTextWriterAttribute = ...
    Colspan: HtmlTextWriterAttribute = ...
    Content: HtmlTextWriterAttribute = ...
    Coords: HtmlTextWriterAttribute = ...
    DesignerRegion: HtmlTextWriterAttribute = ...
    Dir: HtmlTextWriterAttribute = ...
    Disabled: HtmlTextWriterAttribute = ...
    For: HtmlTextWriterAttribute = ...
    Headers: HtmlTextWriterAttribute = ...
    Height: HtmlTextWriterAttribute = ...
    Href: HtmlTextWriterAttribute = ...
    Id: HtmlTextWriterAttribute = ...
    Longdesc: HtmlTextWriterAttribute = ...
    Maxlength: HtmlTextWriterAttribute = ...
    Multiple: HtmlTextWriterAttribute = ...
    Name: HtmlTextWriterAttribute = ...
    Nowrap: HtmlTextWriterAttribute = ...
    Onchange: HtmlTextWriterAttribute = ...
    Onclick: HtmlTextWriterAttribute = ...
    ReadOnly: HtmlTextWriterAttribute = ...
    Rel: HtmlTextWriterAttribute = ...
    Rows: HtmlTextWriterAttribute = ...
    Rowspan: HtmlTextWriterAttribute = ...
    Rules: HtmlTextWriterAttribute = ...
    Scope: HtmlTextWriterAttribute = ...
    Selected: HtmlTextWriterAttribute = ...
    Shape: HtmlTextWriterAttribute = ...
    Size: HtmlTextWriterAttribute = ...
    Src: HtmlTextWriterAttribute = ...
    Style: HtmlTextWriterAttribute = ...
    Tabindex: HtmlTextWriterAttribute = ...
    Target: HtmlTextWriterAttribute = ...
    Title: HtmlTextWriterAttribute = ...
    Type: HtmlTextWriterAttribute = ...
    Usemap: HtmlTextWriterAttribute = ...
    Valign: HtmlTextWriterAttribute = ...
    Value: HtmlTextWriterAttribute = ...
    value__ = ...
    VCardName: HtmlTextWriterAttribute = ...
    Width: HtmlTextWriterAttribute = ...
    Wrap: HtmlTextWriterAttribute = ...


class HtmlTextWriterStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HtmlTextWriterStyle, values: BackgroundColor (0), BackgroundImage (1), BorderCollapse (2), BorderColor (3), BorderStyle (4), BorderWidth (5), Color (6), Cursor (16), Direction (17), Display (18), Filter (19), FontFamily (7), FontSize (8), FontStyle (9), FontVariant (20), FontWeight (10), Height (11), Left (21), ListStyleImage (14), ListStyleType (15), Margin (22), MarginBottom (23), MarginLeft (24), MarginRight (25), MarginTop (26), Overflow (27), OverflowX (28), OverflowY (29), Padding (30), PaddingBottom (31), PaddingLeft (32), PaddingRight (33), PaddingTop (34), Position (35), TextAlign (36), TextDecoration (12), TextOverflow (38), Top (39), VerticalAlign (37), Visibility (40), WhiteSpace (41), Width (13), ZIndex (42) """
    BackgroundColor: HtmlTextWriterStyle = ...
    BackgroundImage: HtmlTextWriterStyle = ...
    BorderCollapse: HtmlTextWriterStyle = ...
    BorderColor: HtmlTextWriterStyle = ...
    BorderStyle: HtmlTextWriterStyle = ...
    BorderWidth: HtmlTextWriterStyle = ...
    Color: HtmlTextWriterStyle = ...
    Cursor: HtmlTextWriterStyle = ...
    Direction: HtmlTextWriterStyle = ...
    Display: HtmlTextWriterStyle = ...
    Filter: HtmlTextWriterStyle = ...
    FontFamily: HtmlTextWriterStyle = ...
    FontSize: HtmlTextWriterStyle = ...
    FontStyle: HtmlTextWriterStyle = ...
    FontVariant: HtmlTextWriterStyle = ...
    FontWeight: HtmlTextWriterStyle = ...
    Height: HtmlTextWriterStyle = ...
    Left: HtmlTextWriterStyle = ...
    ListStyleImage: HtmlTextWriterStyle = ...
    ListStyleType: HtmlTextWriterStyle = ...
    Margin: HtmlTextWriterStyle = ...
    MarginBottom: HtmlTextWriterStyle = ...
    MarginLeft: HtmlTextWriterStyle = ...
    MarginRight: HtmlTextWriterStyle = ...
    MarginTop: HtmlTextWriterStyle = ...
    Overflow: HtmlTextWriterStyle = ...
    OverflowX: HtmlTextWriterStyle = ...
    OverflowY: HtmlTextWriterStyle = ...
    Padding: HtmlTextWriterStyle = ...
    PaddingBottom: HtmlTextWriterStyle = ...
    PaddingLeft: HtmlTextWriterStyle = ...
    PaddingRight: HtmlTextWriterStyle = ...
    PaddingTop: HtmlTextWriterStyle = ...
    Position: HtmlTextWriterStyle = ...
    TextAlign: HtmlTextWriterStyle = ...
    TextDecoration: HtmlTextWriterStyle = ...
    TextOverflow: HtmlTextWriterStyle = ...
    Top: HtmlTextWriterStyle = ...
    value__ = ...
    VerticalAlign: HtmlTextWriterStyle = ...
    Visibility: HtmlTextWriterStyle = ...
    WhiteSpace: HtmlTextWriterStyle = ...
    Width: HtmlTextWriterStyle = ...
    ZIndex: HtmlTextWriterStyle = ...


class HtmlTextWriterTag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HtmlTextWriterTag, values: A (1), Acronym (2), Address (3), Area (4), B (5), Base (6), Basefont (7), Bdo (8), Bgsound (9), Big (10), Blockquote (11), Body (12), Br (13), Button (14), Caption (15), Center (16), Cite (17), Code (18), Col (19), Colgroup (20), Dd (21), Del (22), Dfn (23), Dir (24), Div (25), Dl (26), Dt (27), Em (28), Embed (29), Fieldset (30), Font (31), Form (32), Frame (33), Frameset (34), H1 (35), H2 (36), H3 (37), H4 (38), H5 (39), H6 (40), Head (41), Hr (42), Html (43), I (44), Iframe (45), Img (46), Input (47), Ins (48), Isindex (49), Kbd (50), Label (51), Legend (52), Li (53), Link (54), Map (55), Marquee (56), Menu (57), Meta (58), Nobr (59), Noframes (60), Noscript (61), Object (62), Ol (63), Option (64), P (65), Param (66), Pre (67), Q (68), Rt (69), Ruby (70), S (71), Samp (72), Script (73), Select (74), Small (75), Span (76), Strike (77), Strong (78), Style (79), Sub (80), Sup (81), Table (82), Tbody (83), Td (84), Textarea (85), Tfoot (86), Th (87), Thead (88), Title (89), Tr (90), Tt (91), U (92), Ul (93), Unknown (0), Var (94), Wbr (95), Xml (96) """
    A: HtmlTextWriterTag = ...
    Acronym: HtmlTextWriterTag = ...
    Address: HtmlTextWriterTag = ...
    Area: HtmlTextWriterTag = ...
    B: HtmlTextWriterTag = ...
    Base: HtmlTextWriterTag = ...
    Basefont: HtmlTextWriterTag = ...
    Bdo: HtmlTextWriterTag = ...
    Bgsound: HtmlTextWriterTag = ...
    Big: HtmlTextWriterTag = ...
    Blockquote: HtmlTextWriterTag = ...
    Body: HtmlTextWriterTag = ...
    Br: HtmlTextWriterTag = ...
    Button: HtmlTextWriterTag = ...
    Caption: HtmlTextWriterTag = ...
    Center: HtmlTextWriterTag = ...
    Cite: HtmlTextWriterTag = ...
    Code: HtmlTextWriterTag = ...
    Col: HtmlTextWriterTag = ...
    Colgroup: HtmlTextWriterTag = ...
    Dd: HtmlTextWriterTag = ...
    Del: HtmlTextWriterTag = ...
    Dfn: HtmlTextWriterTag = ...
    Dir: HtmlTextWriterTag = ...
    Div: HtmlTextWriterTag = ...
    Dl: HtmlTextWriterTag = ...
    Dt: HtmlTextWriterTag = ...
    Em: HtmlTextWriterTag = ...
    Embed: HtmlTextWriterTag = ...
    Fieldset: HtmlTextWriterTag = ...
    Font: HtmlTextWriterTag = ...
    Form: HtmlTextWriterTag = ...
    Frame: HtmlTextWriterTag = ...
    Frameset: HtmlTextWriterTag = ...
    H1: HtmlTextWriterTag = ...
    H2: HtmlTextWriterTag = ...
    H3: HtmlTextWriterTag = ...
    H4: HtmlTextWriterTag = ...
    H5: HtmlTextWriterTag = ...
    H6: HtmlTextWriterTag = ...
    Head: HtmlTextWriterTag = ...
    Hr: HtmlTextWriterTag = ...
    Html: HtmlTextWriterTag = ...
    I: HtmlTextWriterTag = ...
    Iframe: HtmlTextWriterTag = ...
    Img: HtmlTextWriterTag = ...
    Input: HtmlTextWriterTag = ...
    Ins: HtmlTextWriterTag = ...
    Isindex: HtmlTextWriterTag = ...
    Kbd: HtmlTextWriterTag = ...
    Label: HtmlTextWriterTag = ...
    Legend: HtmlTextWriterTag = ...
    Li: HtmlTextWriterTag = ...
    Link: HtmlTextWriterTag = ...
    Map: HtmlTextWriterTag = ...
    Marquee: HtmlTextWriterTag = ...
    Menu: HtmlTextWriterTag = ...
    Meta: HtmlTextWriterTag = ...
    Nobr: HtmlTextWriterTag = ...
    Noframes: HtmlTextWriterTag = ...
    Noscript: HtmlTextWriterTag = ...
    Object: HtmlTextWriterTag = ...
    Ol: HtmlTextWriterTag = ...
    Option: HtmlTextWriterTag = ...
    P: HtmlTextWriterTag = ...
    Param: HtmlTextWriterTag = ...
    Pre: HtmlTextWriterTag = ...
    Q: HtmlTextWriterTag = ...
    Rt: HtmlTextWriterTag = ...
    Ruby: HtmlTextWriterTag = ...
    S: HtmlTextWriterTag = ...
    Samp: HtmlTextWriterTag = ...
    Script: HtmlTextWriterTag = ...
    Select: HtmlTextWriterTag = ...
    Small: HtmlTextWriterTag = ...
    Span: HtmlTextWriterTag = ...
    Strike: HtmlTextWriterTag = ...
    Strong: HtmlTextWriterTag = ...
    Style: HtmlTextWriterTag = ...
    Sub: HtmlTextWriterTag = ...
    Sup: HtmlTextWriterTag = ...
    Table: HtmlTextWriterTag = ...
    Tbody: HtmlTextWriterTag = ...
    Td: HtmlTextWriterTag = ...
    Textarea: HtmlTextWriterTag = ...
    Tfoot: HtmlTextWriterTag = ...
    Th: HtmlTextWriterTag = ...
    Thead: HtmlTextWriterTag = ...
    Title: HtmlTextWriterTag = ...
    Tr: HtmlTextWriterTag = ...
    Tt: HtmlTextWriterTag = ...
    U: HtmlTextWriterTag = ...
    Ul: HtmlTextWriterTag = ...
    Unknown: HtmlTextWriterTag = ...
    value__ = ...
    Var: HtmlTextWriterTag = ...
    Wbr: HtmlTextWriterTag = ...
    Xml: HtmlTextWriterTag = ...


class IAttributeAccessor: # skipped bases: <type 'object'>
    """ no doc """
    def GetAttribute(self, key:str) -> str:
        """ GetAttribute(self: IAttributeAccessor, key: str) -> str """
        ...

    def SetAttribute(self, key:str, value:str): # -> 
        """ SetAttribute(self: IAttributeAccessor, key: str, value: str) """
        ...


class IAutoFieldGenerator: # skipped bases: <type 'object'>
    """ no doc """
    def GenerateFields(self, control:Control) -> ICollection:
        """ GenerateFields(self: IAutoFieldGenerator, control: Control) -> ICollection """
        ...


class IBindableControl: # skipped bases: <type 'object'>
    """ no doc """
    def ExtractValues(self, dictionary:IOrderedDictionary): # -> 
        """ ExtractValues(self: IBindableControl, dictionary: IOrderedDictionary) """
        ...


class ITemplate: # skipped bases: <type 'object'>
    """ no doc """
    def InstantiateIn(self, container:Control): # -> 
        """ InstantiateIn(self: ITemplate, container: Control) """
        ...


class IBindableTemplate(ITemplate): # skipped bases: <type 'object'>
    """ no doc """
    def ExtractValues(self, container:Control) -> IOrderedDictionary:
        """ ExtractValues(self: IBindableTemplate, container: Control) -> IOrderedDictionary """
        ...


class ICallbackEventHandler: # skipped bases: <type 'object'>
    """ no doc """
    def GetCallbackResult(self) -> str:
        """ GetCallbackResult(self: ICallbackEventHandler) -> str """
        ...

    def RaiseCallbackEvent(self, eventArgument:str): # -> 
        """ RaiseCallbackEvent(self: ICallbackEventHandler, eventArgument: str) """
        ...


class ICheckBoxControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: ICheckBoxControl) -> bool
        Set: Checked(self: ICheckBoxControl) = value
        """
        ...


    CheckedChanged = ...


class ICodeBlockTypeAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BlockType(self) -> CodeBlockType:
        """ Get: BlockType(self: ICodeBlockTypeAccessor) -> CodeBlockType """
        ...



class INamingContainer: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDataItemContainer(INamingContainer): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataItem(self) -> object:
        """ Get: DataItem(self: IDataItemContainer) -> object """
        ...

    @property
    def DataItemIndex(self) -> int:
        """ Get: DataItemIndex(self: IDataItemContainer) -> int """
        ...

    @property
    def DisplayIndex(self) -> int:
        """ Get: DisplayIndex(self: IDataItemContainer) -> int """
        ...



class IDataKeysControl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ClientIDRowSuffix(self) -> Array:
        """ Get: ClientIDRowSuffix(self: IDataKeysControl) -> Array[str] """
        ...

    @property
    def ClientIDRowSuffixDataKeys(self): # -> DataKeyArray
        """ Get: ClientIDRowSuffixDataKeys(self: IDataKeysControl) -> DataKeyArray """
        ...



class IDataSourceViewSchemaAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataSourceViewSchema(self) -> object:
        """
        Get: DataSourceViewSchema(self: IDataSourceViewSchemaAccessor) -> object
        Set: DataSourceViewSchema(self: IDataSourceViewSchemaAccessor) = value
        """
        ...



class IDReferencePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    IDReferencePropertyAttribute()
    IDReferencePropertyAttribute(referencedControlType: Type)
    """
    @property
    def ReferencedControlType(self) -> Type:
        """ Get: ReferencedControlType(self: IDReferencePropertyAttribute) -> Type """
        ...


    def __new__(cls, referencedControlType:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, referencedControlType: Type)
        """
        ...


class IEditableTextControl(ITextControl): # skipped bases: <type 'object'>
    """ no doc """
    TextChanged = ...


class IFilterResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    def CompareFilters(self, filter1:str, filter2:str) -> int:
        """ CompareFilters(self: IFilterResolutionService, filter1: str, filter2: str) -> int """
        ...

    def EvaluateFilter(self, filterName:str) -> bool:
        """ EvaluateFilter(self: IFilterResolutionService, filterName: str) -> bool """
        ...


class IHierarchicalEnumerable(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    def GetHierarchyData(self, enumeratedItem:object): # -> IHierarchyData
        """ GetHierarchyData(self: IHierarchicalEnumerable, enumeratedItem: object) -> IHierarchyData """
        ...


class IHierarchyData: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasChildren(self) -> bool:
        """ Get: HasChildren(self: IHierarchyData) -> bool """
        ...

    @property
    def Item(self) -> object:
        """ Get: Item(self: IHierarchyData) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: IHierarchyData) -> str """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: IHierarchyData) -> str """
        ...


    def GetChildren(self) -> IHierarchicalEnumerable:
        """ GetChildren(self: IHierarchyData) -> IHierarchicalEnumerable """
        ...

    def GetParent(self) -> IHierarchyData:
        """ GetParent(self: IHierarchyData) -> IHierarchyData """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ImageClickEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ImageClickEventArgs(x: int, y: int)
    ImageClickEventArgs(x: int, y: int, xRaw: float, yRaw: float)
    """
    def __new__(cls, x:int, y:int, xRaw:float = ..., yRaw:float = ...) -> Self:
        """
        __new__(cls: type, x: int, y: int)
        __new__(cls: type, x: int, y: int, xRaw: float, yRaw: float)
        """
        ...

    X = ...
    XRaw = ...
    Y = ...
    YRaw = ...


class ImageClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ImageClickEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ImageClickEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ImageClickEventHandler, sender: object, e: ImageClickEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ImageClickEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ImageClickEventArgs): # -> 
        """ Invoke(self: ImageClickEventHandler, sender: object, e: ImageClickEventArgs) """
        ...


class INavigateUIData: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: INavigateUIData) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: INavigateUIData) -> str """
        ...

    @property
    def NavigateUrl(self) -> str:
        """ Get: NavigateUrl(self: INavigateUIData) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: INavigateUIData) -> str """
        ...



class IndexedString: # skipped bases: <type 'object'>, <type 'object'>
    """ IndexedString(s: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: IndexedString) -> str """
        ...



class IPostBackDataHandler: # skipped bases: <type 'object'>
    """ no doc """
    def LoadPostData(self, postDataKey:str, postCollection:NameValueCollection) -> bool:
        """ LoadPostData(self: IPostBackDataHandler, postDataKey: str, postCollection: NameValueCollection) -> bool """
        ...

    def RaisePostDataChangedEvent(self): # -> 
        """ RaisePostDataChangedEvent(self: IPostBackDataHandler) """
        ...


class IPostBackEventHandler: # skipped bases: <type 'object'>
    """ no doc """
    def RaisePostBackEvent(self, eventArgument:str): # -> 
        """ RaisePostBackEvent(self: IPostBackEventHandler, eventArgument: str) """
        ...


class IResourceUrlGenerator: # skipped bases: <type 'object'>
    """ no doc """
    def GetResourceUrl(self, type:Type, resourceName:str) -> str:
        """ GetResourceUrl(self: IResourceUrlGenerator, type: Type, resourceName: str) -> str """
        ...


class IScriptControl: # skipped bases: <type 'object'>
    """ no doc """
    def GetScriptDescriptors(self) -> IEnumerable:
        """ GetScriptDescriptors(self: IScriptControl) -> IEnumerable[ScriptDescriptor] """
        ...

    def GetScriptReferences(self) -> IEnumerable:
        """ GetScriptReferences(self: IScriptControl) -> IEnumerable[ScriptReference] """
        ...


class IStateFormatter: # skipped bases: <type 'object'>
    """ no doc """
    def Deserialize(self, serializedState:str) -> object:
        """ Deserialize(self: IStateFormatter, serializedState: str) -> object """
        ...

    def Serialize(self, state:object) -> str:
        """ Serialize(self: IStateFormatter, state: object) -> str """
        ...


class IStateManager: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsTrackingViewState(self) -> bool:
        """ Get: IsTrackingViewState(self: IStateManager) -> bool """
        ...


    def LoadViewState(self, state:object): # -> 
        """ LoadViewState(self: IStateManager, state: object) """
        ...

    def SaveViewState(self) -> object:
        """ SaveViewState(self: IStateManager) -> object """
        ...

    def TrackViewState(self): # -> 
        """ TrackViewState(self: IStateManager) """
        ...


class IStyleSheet: # skipped bases: <type 'object'>
    """ no doc """
    def CreateStyleRule(self, style:Style, urlResolver:IUrlResolutionService, selector:str): # -> 
        """ CreateStyleRule(self: IStyleSheet, style: Style, urlResolver: IUrlResolutionService, selector: str) """
        ...

    def RegisterStyle(self, style:Style, urlResolver:IUrlResolutionService): # -> 
        """ RegisterStyle(self: IStyleSheet, style: Style, urlResolver: IUrlResolutionService) """
        ...


class IThemeResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    def GetAllThemeProviders(self) -> Array:
        """ GetAllThemeProviders(self: IThemeResolutionService) -> Array[ThemeProvider] """
        ...

    def GetStylesheetThemeProvider(self): # -> ThemeProvider
        """ GetStylesheetThemeProvider(self: IThemeResolutionService) -> ThemeProvider """
        ...

    def GetThemeProvider(self): # -> ThemeProvider
        """ GetThemeProvider(self: IThemeResolutionService) -> ThemeProvider """
        ...


class IUserControlDesignerAccessor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: IUserControlDesignerAccessor) -> str
        Set: InnerText(self: IUserControlDesignerAccessor) = value
        """
        ...

    @property
    def TagName(self) -> str:
        """
        Get: TagName(self: IUserControlDesignerAccessor) -> str
        Set: TagName(self: IUserControlDesignerAccessor) = value
        """
        ...



class IUserControlTypeResolutionService: # skipped bases: <type 'object'>
    """ no doc """
    def GetType(self, tagPrefix:str, tagName:str) -> Type:
        """ GetType(self: IUserControlTypeResolutionService, tagPrefix: str, tagName: str) -> Type """
        ...


class IValidator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorMessage(self) -> str:
        """
        Get: ErrorMessage(self: IValidator) -> str
        Set: ErrorMessage(self: IValidator) = value
        """
        ...

    @property
    def IsValid(self) -> bool:
        """
        Get: IsValid(self: IValidator) -> bool
        Set: IsValid(self: IValidator) = value
        """
        ...


    def Validate(self): # -> 
        """ Validate(self: IValidator) """
        ...


class ListSourceHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ContainsListCollection(dataSource:IDataSource) -> bool:
        """ ContainsListCollection(dataSource: IDataSource) -> bool """
        ...

    @staticmethod
    def GetList(dataSource:IDataSource) -> IList:
        """ GetList(dataSource: IDataSource) -> IList """
        ...

    __all__: list = ...


class LiteralControl(Control, ITextControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    LiteralControl()
    LiteralControl(text: str)
    """
    def __new__(cls, text:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        """
        ...


class LosFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """
    LosFormatter()
    LosFormatter(enableMac: bool, macKeyModifier: str)
    LosFormatter(enableMac: bool, macKeyModifier: Array[Byte])
    """
    def Deserialize(self, *__args:Stream) -> object:
        """
        Deserialize(self: LosFormatter, stream: Stream) -> object
        Deserialize(self: LosFormatter, input: str) -> object
        Deserialize(self: LosFormatter, input: TextReader) -> object
        """
        ...

    def Serialize(self, *__args): # -> 
        """ Serialize(self: LosFormatter, stream: Stream, value: object)Serialize(self: LosFormatter, output: TextWriter, value: object) """
        ...


class TemplateControl(IFilterResolutionService, Control, INamingContainer): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def AppRelativeVirtualPath(self) -> str:
        """
        Get: AppRelativeVirtualPath(self: TemplateControl) -> str
        Set: AppRelativeVirtualPath(self: TemplateControl) = value
        """
        ...

    @property
    def AutoHandlers(self):
        ...

    @property
    def SupportAutoEvents(self):
        ...


    def Construct(self, *args): #cannot find CLR method
        """ Construct(self: TemplateControl) """
        ...

    def CreateResourceBasedLiteralControl(self, *args): #cannot find CLR method
        """ CreateResourceBasedLiteralControl(self: TemplateControl, offset: int, size: int, fAsciiOnly: bool) -> LiteralControl """
        ...

    def Eval(self, *args): #cannot find CLR method
        """
        Eval(self: TemplateControl, expression: str) -> object
        Eval(self: TemplateControl, expression: str, format: str) -> str
        """
        ...

    def FrameworkInitialize(self, *args): #cannot find CLR method
        """ FrameworkInitialize(self: TemplateControl) """
        ...

    def GetGlobalResourceObject(self, *args): #cannot find CLR method
        """
        GetGlobalResourceObject(self: TemplateControl, className: str, resourceKey: str) -> object
        GetGlobalResourceObject(self: TemplateControl, className: str, resourceKey: str, objType: Type, propName: str) -> object
        """
        ...

    def GetLocalResourceObject(self, *args): #cannot find CLR method
        """
        GetLocalResourceObject(self: TemplateControl, resourceKey: str) -> object
        GetLocalResourceObject(self: TemplateControl, resourceKey: str, objType: Type, propName: str) -> object
        """
        ...

    def LoadControl(self, *__args:str) -> Control:
        """
        LoadControl(self: TemplateControl, virtualPath: str) -> Control
        LoadControl(self: TemplateControl, t: Type, parameters: Array[object]) -> Control
        """
        ...

    def LoadTemplate(self, virtualPath:str) -> ITemplate:
        """ LoadTemplate(self: TemplateControl, virtualPath: str) -> ITemplate """
        ...

    def OnAbortTransaction(self, *args): #cannot find CLR method
        """ OnAbortTransaction(self: TemplateControl, e: EventArgs) """
        ...

    def OnCommitTransaction(self, *args): #cannot find CLR method
        """ OnCommitTransaction(self: TemplateControl, e: EventArgs) """
        ...

    def OnError(self, *args): #cannot find CLR method
        """ OnError(self: TemplateControl, e: EventArgs) """
        ...

    def ParseControl(self, content:str, ignoreParserFilter:bool = ...) -> Control:
        """
        ParseControl(self: TemplateControl, content: str) -> Control
        ParseControl(self: TemplateControl, content: str, ignoreParserFilter: bool) -> Control
        """
        ...

    @staticmethod
    def ReadStringResource(t:Type = ...) -> object:
        """
        ReadStringResource(t: Type) -> object
        ReadStringResource(self: TemplateControl) -> object
        """
        ...

    def SetStringResourcePointer(self, *args): #cannot find CLR method
        """ SetStringResourcePointer(self: TemplateControl, stringResourcePointer: object, maxResourceOffset: int) """
        ...

    def TestDeviceFilter(self, filterName:str) -> bool:
        """ TestDeviceFilter(self: TemplateControl, filterName: str) -> bool """
        ...

    def WriteUTF8ResourceString(self, *args): #cannot find CLR method
        """ WriteUTF8ResourceString(self: TemplateControl, output: HtmlTextWriter, offset: int, size: int, fAsciiOnly: bool) """
        ...

    def XPath(self, *args): #cannot find CLR method
        """
        XPath(self: TemplateControl, xPathExpression: str) -> object
        XPath(self: TemplateControl, xPathExpression: str, resolver: IXmlNamespaceResolver) -> object
        XPath(self: TemplateControl, xPathExpression: str, format: str) -> str
        XPath(self: TemplateControl, xPathExpression: str, format: str, resolver: IXmlNamespaceResolver) -> str
        """
        ...

    def XPathSelect(self, *args): #cannot find CLR method
        """
        XPathSelect(self: TemplateControl, xPathExpression: str) -> IEnumerable
        XPathSelect(self: TemplateControl, xPathExpression: str, resolver: IXmlNamespaceResolver) -> IEnumerable
        """
        ...

    AbortTransaction = ...
    CommitTransaction = ...
    Error = ...


class UserControl(IAttributeAccessor, IUserControlDesignerAccessor, INonBindingContainer, TemplateControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ UserControl() """
    @property
    def Application(self): # -> HttpApplicationState
        """ Get: Application(self: UserControl) -> HttpApplicationState """
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: UserControl) -> AttributeCollection """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache(self: UserControl) -> Cache """
        ...

    @property
    def CachePolicy(self) -> ControlCachePolicy:
        """ Get: CachePolicy(self: UserControl) -> ControlCachePolicy """
        ...

    @property
    def IsPostBack(self) -> bool:
        """ Get: IsPostBack(self: UserControl) -> bool """
        ...

    @property
    def Request(self): # -> HttpRequest
        """ Get: Request(self: UserControl) -> HttpRequest """
        ...

    @property
    def Response(self): # -> HttpResponse
        """ Get: Response(self: UserControl) -> HttpResponse """
        ...

    @property
    def Server(self): # -> HttpServerUtility
        """ Get: Server(self: UserControl) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: UserControl) -> HttpSessionState """
        ...

    @property
    def Trace(self) -> TraceContext:
        """ Get: Trace(self: UserControl) -> TraceContext """
        ...


    def DesignerInitialize(self): # -> 
        """ DesignerInitialize(self: UserControl) """
        ...

    def InitializeAsUserControl(self, page:Page): # -> 
        """ InitializeAsUserControl(self: UserControl, page: Page) """
        ...

    def MapPath(self, virtualPath:str) -> str:
        """ MapPath(self: UserControl, virtualPath: str) -> str """
        ...

    def TryUpdateModel(self, model, valueProvider:IValueProvider = ...) -> bool: # Not found arg types: {'model': 'TModel'}
        """
        TryUpdateModel[TModel](self: UserControl, model: TModel) -> bool
        TryUpdateModel[TModel](self: UserControl, model: TModel, valueProvider: IValueProvider) -> bool
        """
        ...

    def UpdateModel(self, model, valueProvider:IValueProvider = ...): # ->  # Not found arg types: {'model': 'TModel'}
        """ UpdateModel[TModel](self: UserControl, model: TModel)UpdateModel[TModel](self: UserControl, model: TModel, valueProvider: IValueProvider) """
        ...


class MasterPage(UserControl): # skipped bases: <type 'IAttributeAccessor'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IExpressionsAccessor'>, <type 'INonBindingContainer'>, <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IUserControlDesignerAccessor'>, <type 'IComponent'>, <type 'INamingContainer'>, <type 'IParserAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ MasterPage() """
    @property
    def ContentPlaceHolders(self):
        ...

    @property
    def ContentTemplates(self):
        ...

    @property
    def Master(self) -> MasterPage:
        """ Get: Master(self: MasterPage) -> MasterPage """
        ...

    @property
    def MasterPageFile(self) -> str:
        """
        Get: MasterPageFile(self: MasterPage) -> str
        Set: MasterPageFile(self: MasterPage) = value
        """
        ...


    def AddContentTemplate(self, *args): #cannot find CLR method
        """ AddContentTemplate(self: MasterPage, templateName: str, template: ITemplate) """
        ...

    def InstantiateInContentPlaceHolder(self, contentPlaceHolder:Control, template:ITemplate): # -> 
        """ InstantiateInContentPlaceHolder(self: MasterPage, contentPlaceHolder: Control, template: ITemplate) """
        ...


class UserControlControlBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ UserControlControlBuilder() """
    pass

class MasterPageControlBuilder(UserControlControlBuilder): # skipped bases: <type 'object'>
    """ MasterPageControlBuilder() """
    pass

class NonVisualControlAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    NonVisualControlAttribute()
    NonVisualControlAttribute(nonVisual: bool)
    """
    @property
    def IsNonVisual(self) -> bool:
        """ Get: IsNonVisual(self: NonVisualControlAttribute) -> bool """
        ...


    def __new__(cls, nonVisual:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, nonVisual: bool)
        """
        ...

    Default: NonVisualControlAttribute = ...
    NonVisual: NonVisualControlAttribute = ...
    Visual: NonVisualControlAttribute = ...


class ObjectConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectConverter() """
    @staticmethod
    def ConvertValue(value:object, toType:Type, formatString:str) -> object:
        """ ConvertValue(value: object, toType: Type, formatString: str) -> object """
        ...


class ObjectPersistData: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectPersistData(builder: ControlBuilder, builtObjects: IDictionary) """
    @property
    def AllPropertyEntries(self) -> ICollection:
        """ Get: AllPropertyEntries(self: ObjectPersistData) -> ICollection """
        ...

    @property
    def BuiltObjects(self) -> IDictionary:
        """ Get: BuiltObjects(self: ObjectPersistData) -> IDictionary """
        ...

    @property
    def CollectionItems(self) -> ICollection:
        """ Get: CollectionItems(self: ObjectPersistData) -> ICollection """
        ...

    @property
    def EventEntries(self) -> ICollection:
        """ Get: EventEntries(self: ObjectPersistData) -> ICollection """
        ...

    @property
    def IsCollection(self) -> bool:
        """ Get: IsCollection(self: ObjectPersistData) -> bool """
        ...

    @property
    def Localize(self) -> bool:
        """ Get: Localize(self: ObjectPersistData) -> bool """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: ObjectPersistData) -> Type """
        ...

    @property
    def ResourceKey(self) -> str:
        """ Get: ResourceKey(self: ObjectPersistData) -> str """
        ...


    def AddToObjectControlBuilderTable(self, table:IDictionary): # -> 
        """ AddToObjectControlBuilderTable(self: ObjectPersistData, table: IDictionary) """
        ...

    def GetFilteredProperties(self, filter:str) -> IDictionary:
        """ GetFilteredProperties(self: ObjectPersistData, filter: str) -> IDictionary """
        ...

    def GetFilteredProperty(self, filter:str, name:str) -> PropertyEntry:
        """ GetFilteredProperty(self: ObjectPersistData, filter: str, name: str) -> PropertyEntry """
        ...

    def GetPropertyAllFilters(self, name:str) -> ICollection:
        """ GetPropertyAllFilters(self: ObjectPersistData, name: str) -> ICollection """
        ...


class ObjectStateFormatter(IFormatter, IStateFormatter2): # skipped bases: <type 'IStateFormatter'>, <type 'object'>
    """ ObjectStateFormatter() """
    pass

class ObjectTagBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ ObjectTagBuilder() """
    pass

class OutputCacheLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OutputCacheLocation, values: Any (0), Client (1), Downstream (2), None (4), Server (3), ServerAndClient (5) """
    Any: OutputCacheLocation = ...
    Client: OutputCacheLocation = ...
    Downstream: OutputCacheLocation = ...
    Server: OutputCacheLocation = ...
    ServerAndClient: OutputCacheLocation = ...
    value__ = ...


class OutputCacheParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ OutputCacheParameters() """
    @property
    def CacheProfile(self) -> str:
        """
        Get: CacheProfile(self: OutputCacheParameters) -> str
        Set: CacheProfile(self: OutputCacheParameters) = value
        """
        ...

    @property
    def Duration(self) -> int:
        """
        Get: Duration(self: OutputCacheParameters) -> int
        Set: Duration(self: OutputCacheParameters) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: OutputCacheParameters) -> bool
        Set: Enabled(self: OutputCacheParameters) = value
        """
        ...

    @property
    def Location(self) -> OutputCacheLocation:
        """
        Get: Location(self: OutputCacheParameters) -> OutputCacheLocation
        Set: Location(self: OutputCacheParameters) = value
        """
        ...

    @property
    def NoStore(self) -> bool:
        """
        Get: NoStore(self: OutputCacheParameters) -> bool
        Set: NoStore(self: OutputCacheParameters) = value
        """
        ...

    @property
    def SqlDependency(self) -> str:
        """
        Get: SqlDependency(self: OutputCacheParameters) -> str
        Set: SqlDependency(self: OutputCacheParameters) = value
        """
        ...

    @property
    def VaryByContentEncoding(self) -> str:
        """
        Get: VaryByContentEncoding(self: OutputCacheParameters) -> str
        Set: VaryByContentEncoding(self: OutputCacheParameters) = value
        """
        ...

    @property
    def VaryByControl(self) -> str:
        """
        Get: VaryByControl(self: OutputCacheParameters) -> str
        Set: VaryByControl(self: OutputCacheParameters) = value
        """
        ...

    @property
    def VaryByCustom(self) -> str:
        """
        Get: VaryByCustom(self: OutputCacheParameters) -> str
        Set: VaryByCustom(self: OutputCacheParameters) = value
        """
        ...

    @property
    def VaryByHeader(self) -> str:
        """
        Get: VaryByHeader(self: OutputCacheParameters) -> str
        Set: VaryByHeader(self: OutputCacheParameters) = value
        """
        ...

    @property
    def VaryByParam(self) -> str:
        """
        Get: VaryByParam(self: OutputCacheParameters) -> str
        Set: VaryByParam(self: OutputCacheParameters) = value
        """
        ...



class Page(IHttpHandler, TemplateControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'INamingContainer'>, <type 'IFilterResolutionService'>, <type 'object'>
    """ Page() """
    @property
    def Application(self): # -> HttpApplicationState
        """ Get: Application(self: Page) -> HttpApplicationState """
        ...

    @property
    def AspCompatMode(self):
        ...

    @property
    def AsyncMode(self):
        ...

    @property
    def AsyncTimeout(self) -> TimeSpan:
        """
        Get: AsyncTimeout(self: Page) -> TimeSpan
        Set: AsyncTimeout(self: Page) = value
        """
        ...

    @property
    def AutoPostBackControl(self) -> Control:
        """
        Get: AutoPostBackControl(self: Page) -> Control
        Set: AutoPostBackControl(self: Page) = value
        """
        ...

    @property
    def Buffer(self) -> bool:
        """
        Get: Buffer(self: Page) -> bool
        Set: Buffer(self: Page) = value
        """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache(self: Page) -> Cache """
        ...

    @property
    def ClientQueryString(self) -> str:
        """ Get: ClientQueryString(self: Page) -> str """
        ...

    @property
    def ClientScript(self) -> ClientScriptManager:
        """ Get: ClientScript(self: Page) -> ClientScriptManager """
        ...

    @property
    def ClientTarget(self) -> str:
        """
        Get: ClientTarget(self: Page) -> str
        Set: ClientTarget(self: Page) = value
        """
        ...

    @property
    def CodePage(self) -> int:
        """
        Get: CodePage(self: Page) -> int
        Set: CodePage(self: Page) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: Page) -> str
        Set: ContentType(self: Page) = value
        """
        ...

    @property
    def Culture(self) -> str:
        """
        Get: Culture(self: Page) -> str
        Set: Culture(self: Page) = value
        """
        ...

    @property
    def EnableEventValidation(self) -> bool:
        """
        Get: EnableEventValidation(self: Page) -> bool
        Set: EnableEventValidation(self: Page) = value
        """
        ...

    @property
    def EnableViewState(self) -> bool:
        """
        Get: EnableViewState(self: Page) -> bool
        Set: EnableViewState(self: Page) = value
        """
        ...

    @property
    def EnableViewStateMac(self) -> bool:
        """
        Get: EnableViewStateMac(self: Page) -> bool
        Set: EnableViewStateMac(self: Page) = value
        """
        ...

    @property
    def ErrorPage(self) -> str:
        """
        Get: ErrorPage(self: Page) -> str
        Set: ErrorPage(self: Page) = value
        """
        ...

    @property
    def Form(self) -> HtmlForm:
        """ Get: Form(self: Page) -> HtmlForm """
        ...

    @property
    def Header(self) -> HtmlHead:
        """ Get: Header(self: Page) -> HtmlHead """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: Page) -> str
        Set: ID(self: Page) = value
        """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: Page) -> bool """
        ...

    @property
    def IsCallback(self) -> bool:
        """ Get: IsCallback(self: Page) -> bool """
        ...

    @property
    def IsCrossPagePostBack(self) -> bool:
        """ Get: IsCrossPagePostBack(self: Page) -> bool """
        ...

    @property
    def IsPostBack(self) -> bool:
        """ Get: IsPostBack(self: Page) -> bool """
        ...

    @property
    def IsPostBackEventControlRegistered(self) -> bool:
        """ Get: IsPostBackEventControlRegistered(self: Page) -> bool """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: Page) -> bool """
        ...

    @property
    def Items(self) -> IDictionary:
        """ Get: Items(self: Page) -> IDictionary """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: Page) -> int
        Set: LCID(self: Page) = value
        """
        ...

    @property
    def MaintainScrollPositionOnPostBack(self) -> bool:
        """
        Get: MaintainScrollPositionOnPostBack(self: Page) -> bool
        Set: MaintainScrollPositionOnPostBack(self: Page) = value
        """
        ...

    @property
    def Master(self) -> MasterPage:
        """ Get: Master(self: Page) -> MasterPage """
        ...

    @property
    def MasterPageFile(self) -> str:
        """
        Get: MasterPageFile(self: Page) -> str
        Set: MasterPageFile(self: Page) = value
        """
        ...

    @property
    def MaxPageStateFieldLength(self) -> int:
        """
        Get: MaxPageStateFieldLength(self: Page) -> int
        Set: MaxPageStateFieldLength(self: Page) = value
        """
        ...

    @property
    def MetaDescription(self) -> str:
        """
        Get: MetaDescription(self: Page) -> str
        Set: MetaDescription(self: Page) = value
        """
        ...

    @property
    def MetaKeywords(self) -> str:
        """
        Get: MetaKeywords(self: Page) -> str
        Set: MetaKeywords(self: Page) = value
        """
        ...

    @property
    def ModelBindingExecutionContext(self) -> ModelBindingExecutionContext:
        """ Get: ModelBindingExecutionContext(self: Page) -> ModelBindingExecutionContext """
        ...

    @property
    def ModelState(self) -> ModelStateDictionary:
        """ Get: ModelState(self: Page) -> ModelStateDictionary """
        ...

    @property
    def PageAdapter(self) -> PageAdapter:
        """ Get: PageAdapter(self: Page) -> PageAdapter """
        ...

    @property
    def PageStatePersister(self):
        ...

    @property
    def PreviousPage(self) -> Page:
        """ Get: PreviousPage(self: Page) -> Page """
        ...

    @property
    def Request(self): # -> HttpRequest
        """ Get: Request(self: Page) -> HttpRequest """
        ...

    @property
    def Response(self): # -> HttpResponse
        """ Get: Response(self: Page) -> HttpResponse """
        ...

    @property
    def ResponseEncoding(self) -> str:
        """
        Get: ResponseEncoding(self: Page) -> str
        Set: ResponseEncoding(self: Page) = value
        """
        ...

    @property
    def RouteData(self) -> RouteData:
        """ Get: RouteData(self: Page) -> RouteData """
        ...

    @property
    def Server(self): # -> HttpServerUtility
        """ Get: Server(self: Page) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: Page) -> HttpSessionState """
        ...

    @property
    def SkipFormActionValidation(self) -> bool:
        """
        Get: SkipFormActionValidation(self: Page) -> bool
        Set: SkipFormActionValidation(self: Page) = value
        """
        ...

    @property
    def SmartNavigation(self) -> bool:
        """
        Get: SmartNavigation(self: Page) -> bool
        Set: SmartNavigation(self: Page) = value
        """
        ...

    @property
    def StyleSheetTheme(self) -> str:
        """
        Get: StyleSheetTheme(self: Page) -> str
        Set: StyleSheetTheme(self: Page) = value
        """
        ...

    @property
    def Theme(self) -> str:
        """
        Get: Theme(self: Page) -> str
        Set: Theme(self: Page) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Page) -> str
        Set: Title(self: Page) = value
        """
        ...

    @property
    def Trace(self) -> TraceContext:
        """ Get: Trace(self: Page) -> TraceContext """
        ...

    @property
    def TraceEnabled(self) -> bool:
        """
        Get: TraceEnabled(self: Page) -> bool
        Set: TraceEnabled(self: Page) = value
        """
        ...

    @property
    def TraceModeValue(self): # -> TraceMode
        """
        Get: TraceModeValue(self: Page) -> TraceMode
        Set: TraceModeValue(self: Page) = value
        """
        ...

    @property
    def TransactionMode(self):
        ...

    @property
    def UICulture(self) -> str:
        """
        Get: UICulture(self: Page) -> str
        Set: UICulture(self: Page) = value
        """
        ...

    @property
    def UniqueFilePathSuffix(self):
        ...

    @property
    def UnobtrusiveValidationMode(self): # -> UnobtrusiveValidationMode
        """
        Get: UnobtrusiveValidationMode(self: Page) -> UnobtrusiveValidationMode
        Set: UnobtrusiveValidationMode(self: Page) = value
        """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: Page) -> IPrincipal """
        ...

    @property
    def ValidateRequestMode(self): # -> ValidateRequestMode
        """
        Get: ValidateRequestMode(self: Page) -> ValidateRequestMode
        Set: ValidateRequestMode(self: Page) = value
        """
        ...

    @property
    def Validators(self): # -> ValidatorCollection
        """ Get: Validators(self: Page) -> ValidatorCollection """
        ...

    @property
    def ViewStateEncryptionMode(self): # -> ViewStateEncryptionMode
        """
        Get: ViewStateEncryptionMode(self: Page) -> ViewStateEncryptionMode
        Set: ViewStateEncryptionMode(self: Page) = value
        """
        ...

    @property
    def ViewStateUserKey(self) -> str:
        """
        Get: ViewStateUserKey(self: Page) -> str
        Set: ViewStateUserKey(self: Page) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Page) -> bool
        Set: Visible(self: Page) = value
        """
        ...


    def AddContentTemplate(self, *args): #cannot find CLR method
        """ AddContentTemplate(self: Page, templateName: str, template: ITemplate) """
        ...

    def AddOnPreRenderCompleteAsync(self, beginHandler, endHandler, state:object = ...): # ->  # Not found arg types: {'endHandler': 'EndEventHandler', 'beginHandler': 'BeginEventHandler'}
        """ AddOnPreRenderCompleteAsync(self: Page, beginHandler: BeginEventHandler, endHandler: EndEventHandler)AddOnPreRenderCompleteAsync(self: Page, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddWrappedFileDependencies(self, *args): #cannot find CLR method
        """ AddWrappedFileDependencies(self: Page, virtualFileDependencies: object) """
        ...

    def AspCompatBeginProcessRequest(self, *args): #cannot find CLR method
        """ AspCompatBeginProcessRequest(self: Page, context: HttpContext, cb: AsyncCallback, extraData: object) -> IAsyncResult """
        ...

    def AspCompatEndProcessRequest(self, *args): #cannot find CLR method
        """ AspCompatEndProcessRequest(self: Page, result: IAsyncResult) """
        ...

    def AsyncPageBeginProcessRequest(self, *args): #cannot find CLR method
        """ AsyncPageBeginProcessRequest(self: Page, context: HttpContext, callback: AsyncCallback, extraData: object) -> IAsyncResult """
        ...

    def AsyncPageEndProcessRequest(self, *args): #cannot find CLR method
        """ AsyncPageEndProcessRequest(self: Page, result: IAsyncResult) """
        ...

    def CreateHtmlTextWriter(self, *args): #cannot find CLR method
        """ CreateHtmlTextWriter(self: Page, tw: TextWriter) -> HtmlTextWriter """
        ...

    @staticmethod
    def CreateHtmlTextWriterFromType(tw:TextWriter, writerType:Type) -> HtmlTextWriter:
        """ CreateHtmlTextWriterFromType(tw: TextWriter, writerType: Type) -> HtmlTextWriter """
        ...

    def DesignerInitialize(self): # -> 
        """ DesignerInitialize(self: Page) """
        ...

    def DeterminePostBackMode(self, *args): #cannot find CLR method
        """ DeterminePostBackMode(self: Page) -> NameValueCollection """
        ...

    def DeterminePostBackModeUnvalidated(self, *args): #cannot find CLR method
        """ DeterminePostBackModeUnvalidated(self: Page) -> NameValueCollection """
        ...

    def ExecuteRegisteredAsyncTasks(self): # -> 
        """ ExecuteRegisteredAsyncTasks(self: Page) """
        ...

    def GetDataItem(self) -> object:
        """ GetDataItem(self: Page) -> object """
        ...

    def GetPostBackClientEvent(self, control:Control, argument:str) -> str:
        """ GetPostBackClientEvent(self: Page, control: Control, argument: str) -> str """
        ...

    def GetPostBackClientHyperlink(self, control:Control, argument:str) -> str:
        """ GetPostBackClientHyperlink(self: Page, control: Control, argument: str) -> str """
        ...

    def GetPostBackEventReference(self, control:Control, argument:str = ...) -> str:
        """
        GetPostBackEventReference(self: Page, control: Control) -> str
        GetPostBackEventReference(self: Page, control: Control, argument: str) -> str
        """
        ...

    def GetTypeHashCode(self) -> int:
        """ GetTypeHashCode(self: Page) -> int """
        ...

    def GetValidators(self, validationGroup:str): # -> ValidatorCollection
        """ GetValidators(self: Page, validationGroup: str) -> ValidatorCollection """
        ...

    def GetWrappedFileDependencies(self, *args): #cannot find CLR method
        """ GetWrappedFileDependencies(self: Page, virtualFileDependencies: Array[str]) -> object """
        ...

    def InitializeCulture(self, *args): #cannot find CLR method
        """ InitializeCulture(self: Page) """
        ...

    def InitOutputCache(self, *args): #cannot find CLR method
        """ InitOutputCache(self: Page, duration: int, varyByHeader: str, varyByCustom: str, location: OutputCacheLocation, varyByParam: str)InitOutputCache(self: Page, duration: int, varyByContentEncoding: str, varyByHeader: str, varyByCustom: str, location: OutputCacheLocation, varyByParam: str)InitOutputCache(self: Page, cacheSettings: OutputCacheParameters) """
        ...

    def IsClientScriptBlockRegistered(self, key:str) -> bool:
        """ IsClientScriptBlockRegistered(self: Page, key: str) -> bool """
        ...

    def IsStartupScriptRegistered(self, key:str) -> bool:
        """ IsStartupScriptRegistered(self: Page, key: str) -> bool """
        ...

    def LoadPageStateFromPersistenceMedium(self, *args): #cannot find CLR method
        """ LoadPageStateFromPersistenceMedium(self: Page) -> object """
        ...

    def MapPath(self, virtualPath:str) -> str:
        """ MapPath(self: Page, virtualPath: str) -> str """
        ...

    def OnInitComplete(self, *args): #cannot find CLR method
        """ OnInitComplete(self: Page, e: EventArgs) """
        ...

    def OnLoadComplete(self, *args): #cannot find CLR method
        """ OnLoadComplete(self: Page, e: EventArgs) """
        ...

    def OnPreInit(self, *args): #cannot find CLR method
        """ OnPreInit(self: Page, e: EventArgs) """
        ...

    def OnPreLoad(self, *args): #cannot find CLR method
        """ OnPreLoad(self: Page, e: EventArgs) """
        ...

    def OnPreRenderComplete(self, *args): #cannot find CLR method
        """ OnPreRenderComplete(self: Page, e: EventArgs) """
        ...

    def OnSaveStateComplete(self, *args): #cannot find CLR method
        """ OnSaveStateComplete(self: Page, e: EventArgs) """
        ...

    def RaisePostBackEvent(self, *args): #cannot find CLR method
        """ RaisePostBackEvent(self: Page, sourceControl: IPostBackEventHandler, eventArgument: str) """
        ...

    def RegisterArrayDeclaration(self, arrayName:str, arrayValue:str): # -> 
        """ RegisterArrayDeclaration(self: Page, arrayName: str, arrayValue: str) """
        ...

    def RegisterAsyncTask(self, task): # ->  # Not found arg types: {'task': 'PageAsyncTask'}
        """ RegisterAsyncTask(self: Page, task: PageAsyncTask) """
        ...

    def RegisterClientScriptBlock(self, key:str, script:str): # -> 
        """ RegisterClientScriptBlock(self: Page, key: str, script: str) """
        ...

    def RegisterHiddenField(self, hiddenFieldName:str, hiddenFieldInitialValue:str): # -> 
        """ RegisterHiddenField(self: Page, hiddenFieldName: str, hiddenFieldInitialValue: str) """
        ...

    def RegisterOnSubmitStatement(self, key:str, script:str): # -> 
        """ RegisterOnSubmitStatement(self: Page, key: str, script: str) """
        ...

    def RegisterRequiresControlState(self, control:Control): # -> 
        """ RegisterRequiresControlState(self: Page, control: Control) """
        ...

    def RegisterRequiresPostBack(self, control:Control): # -> 
        """ RegisterRequiresPostBack(self: Page, control: Control) """
        ...

    def RegisterRequiresRaiseEvent(self, control:IPostBackEventHandler): # -> 
        """ RegisterRequiresRaiseEvent(self: Page, control: IPostBackEventHandler) """
        ...

    def RegisterRequiresViewStateEncryption(self): # -> 
        """ RegisterRequiresViewStateEncryption(self: Page) """
        ...

    def RegisterStartupScript(self, key:str, script:str): # -> 
        """ RegisterStartupScript(self: Page, key: str, script: str) """
        ...

    def RegisterViewStateHandler(self): # -> 
        """ RegisterViewStateHandler(self: Page) """
        ...

    def RequiresControlState(self, control:Control) -> bool:
        """ RequiresControlState(self: Page, control: Control) -> bool """
        ...

    def SavePageStateToPersistenceMedium(self, *args): #cannot find CLR method
        """ SavePageStateToPersistenceMedium(self: Page, state: object) """
        ...

    def SetFocus(self, *__args:str): # -> 
        """ SetFocus(self: Page, clientID: str)SetFocus(self: Page, control: Control) """
        ...

    def TryUpdateModel(self, model, valueProvider:IValueProvider = ...) -> bool: # Not found arg types: {'model': 'TModel'}
        """
        TryUpdateModel[TModel](self: Page, model: TModel) -> bool
        TryUpdateModel[TModel](self: Page, model: TModel, valueProvider: IValueProvider) -> bool
        """
        ...

    def UnregisterRequiresControlState(self, control:Control): # -> 
        """ UnregisterRequiresControlState(self: Page, control: Control) """
        ...

    def UpdateModel(self, model, valueProvider:IValueProvider = ...): # ->  # Not found arg types: {'model': 'TModel'}
        """ UpdateModel[TModel](self: Page, model: TModel)UpdateModel[TModel](self: Page, model: TModel, valueProvider: IValueProvider) """
        ...

    def Validate(self, validationGroup:str = ...): # -> 
        """ Validate(self: Page)Validate(self: Page, validationGroup: str) """
        ...

    def VerifyRenderingInServerForm(self, control:Control): # -> 
        """ VerifyRenderingInServerForm(self: Page, control: Control) """
        ...

    InitComplete = ...
    LoadComplete = ...
    postEventArgumentID: str = ...
    postEventSourceID: str = ...
    PreInit = ...
    PreLoad = ...
    PreRenderComplete = ...
    SaveStateComplete = ...


class PageAsyncTask: # skipped bases: <type 'object'>, <type 'object'>
    """
    PageAsyncTask(beginHandler: BeginEventHandler, endHandler: EndEventHandler, timeoutHandler: EndEventHandler, state: object)
    PageAsyncTask(beginHandler: BeginEventHandler, endHandler: EndEventHandler, timeoutHandler: EndEventHandler, state: object, executeInParallel: bool)
    PageAsyncTask(handler: Func[Task])
    PageAsyncTask(handler: Func[CancellationToken, Task])
    """
    @property
    def BeginHandler(self): # -> BeginEventHandler
        """ Get: BeginHandler(self: PageAsyncTask) -> BeginEventHandler """
        ...

    @property
    def EndHandler(self): # -> EndEventHandler
        """ Get: EndHandler(self: PageAsyncTask) -> EndEventHandler """
        ...

    @property
    def ExecuteInParallel(self) -> bool:
        """ Get: ExecuteInParallel(self: PageAsyncTask) -> bool """
        ...

    @property
    def State(self) -> object:
        """ Get: State(self: PageAsyncTask) -> object """
        ...

    @property
    def TimeoutHandler(self): # -> EndEventHandler
        """ Get: TimeoutHandler(self: PageAsyncTask) -> EndEventHandler """
        ...



class PageHandlerFactory(IHttpHandlerFactory2): # skipped bases: <type 'IHttpHandlerFactory'>, <type 'object'>
    """ no doc """
    def ReleaseHandler(self, handler): # ->  # Not found arg types: {'handler': 'IHttpHandler'}
        """ ReleaseHandler(self: PageHandlerFactory, handler: IHttpHandler) """
        ...


class TemplateControlParser(BaseTemplateParser): # skipped bases: <type 'IAssemblyDependencyParser'>, <type 'object'>
    """ no doc """
    pass

class PageParser(TemplateControlParser): # skipped bases: <type 'IAssemblyDependencyParser'>, <type 'object'>
    """ PageParser() """
    @property
    def DefaultApplicationBaseType(self) -> Type:
        """
        Get: DefaultApplicationBaseType() -> Type
        Set: DefaultApplicationBaseType() = value
        """
        ...

    @property
    def DefaultPageBaseType(self) -> Type:
        """
        Get: DefaultPageBaseType() -> Type
        Set: DefaultPageBaseType() = value
        """
        ...

    @property
    def DefaultPageParserFilterType(self) -> Type:
        """
        Get: DefaultPageParserFilterType() -> Type
        Set: DefaultPageParserFilterType() = value
        """
        ...

    @property
    def DefaultUserControlBaseType(self) -> Type:
        """
        Get: DefaultUserControlBaseType() -> Type
        Set: DefaultUserControlBaseType() = value
        """
        ...

    @property
    def EnableLongStringsAsResources(self) -> bool:
        """
        Get: EnableLongStringsAsResources() -> bool
        Set: EnableLongStringsAsResources() = value
        """
        ...


    @staticmethod
    def GetCompiledPageInstance(virtualPath:str, inputFile:str, context): # -> IHttpHandler # Not found arg types: {'context': 'HttpContext'}
        """ GetCompiledPageInstance(virtualPath: str, inputFile: str, context: HttpContext) -> IHttpHandler """
        ...



class PageParserFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowCode(self) -> bool:
        """ Get: AllowCode(self: PageParserFilter) -> bool """
        ...

    @property
    def CalledFromParseControl(self):
        ...

    @property
    def Line(self):
        ...

    @property
    def NumberOfControlsAllowed(self) -> int:
        """ Get: NumberOfControlsAllowed(self: PageParserFilter) -> int """
        ...

    @property
    def NumberOfDirectDependenciesAllowed(self) -> int:
        """ Get: NumberOfDirectDependenciesAllowed(self: PageParserFilter) -> int """
        ...

    @property
    def TotalNumberOfDependenciesAllowed(self) -> int:
        """ Get: TotalNumberOfDependenciesAllowed(self: PageParserFilter) -> int """
        ...

    @property
    def VirtualPath(self):
        ...


    def AddControl(self, *args): #cannot find CLR method
        """ AddControl(self: PageParserFilter, type: Type, attributes: IDictionary) """
        ...

    def AllowBaseType(self, baseType:Type) -> bool:
        """ AllowBaseType(self: PageParserFilter, baseType: Type) -> bool """
        ...

    def AllowControl(self, controlType:Type, builder:ControlBuilder) -> bool:
        """ AllowControl(self: PageParserFilter, controlType: Type, builder: ControlBuilder) -> bool """
        ...

    def AllowServerSideInclude(self, includeVirtualPath:str) -> bool:
        """ AllowServerSideInclude(self: PageParserFilter, includeVirtualPath: str) -> bool """
        ...

    def AllowVirtualReference(self, referenceVirtualPath:str, referenceType) -> bool: # Not found arg types: {'referenceType': 'VirtualReferenceType'}
        """ AllowVirtualReference(self: PageParserFilter, referenceVirtualPath: str, referenceType: VirtualReferenceType) -> bool """
        ...

    def GetCompilationMode(self, current:CompilationMode) -> CompilationMode:
        """ GetCompilationMode(self: PageParserFilter, current: CompilationMode) -> CompilationMode """
        ...

    def GetNoCompileUserControlType(self) -> Type:
        """ GetNoCompileUserControlType(self: PageParserFilter) -> Type """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: PageParserFilter) """
        ...

    def ParseComplete(self, rootBuilder:ControlBuilder): # -> 
        """ ParseComplete(self: PageParserFilter, rootBuilder: ControlBuilder) """
        ...

    def PreprocessDirective(self, directiveName:str, attributes:IDictionary): # -> 
        """ PreprocessDirective(self: PageParserFilter, directiveName: str, attributes: IDictionary) """
        ...

    def ProcessCodeConstruct(self, codeType:CodeConstructType, code:str) -> bool:
        """ ProcessCodeConstruct(self: PageParserFilter, codeType: CodeConstructType, code: str) -> bool """
        ...

    def ProcessDataBindingAttribute(self, controlId:str, name:str, value:str) -> bool:
        """ ProcessDataBindingAttribute(self: PageParserFilter, controlId: str, name: str, value: str) -> bool """
        ...

    def ProcessEventHookup(self, controlId:str, eventName:str, handlerName:str) -> bool:
        """ ProcessEventHookup(self: PageParserFilter, controlId: str, eventName: str, handlerName: str) -> bool """
        ...

    def SetPageProperty(self, *args): #cannot find CLR method
        """ SetPageProperty(self: PageParserFilter, filter: str, name: str, value: str) """
        ...


class PageTheme: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppRelativeTemplateSourceDirectory(self):
        ...

    @property
    def ControlSkins(self):
        ...

    @property
    def LinkedStyleSheets(self):
        ...

    @property
    def Page(self):
        ...


    @staticmethod
    def CreateSkinKey(controlType:Type, skinID:str) -> object:
        """ CreateSkinKey(controlType: Type, skinID: str) -> object """
        ...

    def Eval(self, *args): #cannot find CLR method
        """
        Eval(self: PageTheme, expression: str) -> object
        Eval(self: PageTheme, expression: str, format: str) -> str
        """
        ...

    def TestDeviceFilter(self, deviceFilterName:str) -> bool:
        """ TestDeviceFilter(self: PageTheme, deviceFilterName: str) -> bool """
        ...

    def XPath(self, *args): #cannot find CLR method
        """
        XPath(self: PageTheme, xPathExpression: str) -> object
        XPath(self: PageTheme, xPathExpression: str, resolver: IXmlNamespaceResolver) -> object
        XPath(self: PageTheme, xPathExpression: str, format: str) -> str
        XPath(self: PageTheme, xPathExpression: str, format: str, resolver: IXmlNamespaceResolver) -> str
        """
        ...

    def XPathSelect(self, *args): #cannot find CLR method
        """
        XPathSelect(self: PageTheme, xPathExpression: str) -> IEnumerable
        XPathSelect(self: PageTheme, xPathExpression: str, resolver: IXmlNamespaceResolver) -> IEnumerable
        """
        ...


class Pair: # skipped bases: <type 'object'>, <type 'object'>
    """
    Pair()
    Pair(x: object, y: object)
    """
    First = ...
    Second = ...


class ParseChildrenAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ParseChildrenAttribute()
    ParseChildrenAttribute(childrenAsProperties: bool)
    ParseChildrenAttribute(childControlType: Type)
    ParseChildrenAttribute(childrenAsProperties: bool, defaultProperty: str)
    """
    @property
    def ChildControlType(self) -> Type:
        """ Get: ChildControlType(self: ParseChildrenAttribute) -> Type """
        ...

    @property
    def ChildrenAsProperties(self) -> bool:
        """
        Get: ChildrenAsProperties(self: ParseChildrenAttribute) -> bool
        Set: ChildrenAsProperties(self: ParseChildrenAttribute) = value
        """
        ...

    @property
    def DefaultProperty(self) -> str:
        """
        Get: DefaultProperty(self: ParseChildrenAttribute) -> str
        Set: DefaultProperty(self: ParseChildrenAttribute) = value
        """
        ...


    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, childrenAsProperties: bool)
        __new__(cls: type, childControlType: Type)
        __new__(cls: type, childrenAsProperties: bool, defaultProperty: str)
        """
        ...

    Default: ParseChildrenAttribute = ...
    ParseAsChildren: ParseChildrenAttribute = ...
    ParseAsProperties: ParseChildrenAttribute = ...


class ParseRecorder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def RecorderFactories(self) -> IList:
        """ Get: RecorderFactories() -> IList[Func[ParseRecorder]] """
        ...


    def Initialize(self, parser:TemplateParser): # -> 
        """ Initialize(self: ParseRecorder, parser: TemplateParser) """
        ...

    def ParseComplete(self, root:ControlBuilder): # -> 
        """ ParseComplete(self: ParseRecorder, root: ControlBuilder) """
        ...

    def ProcessGeneratedCode(self, builder:ControlBuilder, codeCompileUnit:CodeCompileUnit, baseType:CodeTypeDeclaration, derivedType:CodeTypeDeclaration, buildMethod:CodeMemberMethod, dataBindingMethod:CodeMemberMethod): # -> 
        """ ProcessGeneratedCode(self: ParseRecorder, builder: ControlBuilder, codeCompileUnit: CodeCompileUnit, baseType: CodeTypeDeclaration, derivedType: CodeTypeDeclaration, buildMethod: CodeMemberMethod, dataBindingMethod: CodeMemberMethod) """
        ...

    def RecordBeginTag(self, builder:ControlBuilder, tag:Match): # -> 
        """ RecordBeginTag(self: ParseRecorder, builder: ControlBuilder, tag: Match) """
        ...

    def RecordCodeBlock(self, builder:ControlBuilder, codeBlock:Match): # -> 
        """ RecordCodeBlock(self: ParseRecorder, builder: ControlBuilder, codeBlock: Match) """
        ...

    def RecordEmptyTag(self, builder:ControlBuilder, tag:Match): # -> 
        """ RecordEmptyTag(self: ParseRecorder, builder: ControlBuilder, tag: Match) """
        ...

    def RecordEndTag(self, builder:ControlBuilder, tag:Match): # -> 
        """ RecordEndTag(self: ParseRecorder, builder: ControlBuilder, tag: Match) """
        ...



class PartialCachingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PartialCachingAttribute(duration: int)
    PartialCachingAttribute(duration: int, varyByParams: str, varyByControls: str, varyByCustom: str)
    PartialCachingAttribute(duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, shared: bool)
    PartialCachingAttribute(duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, shared: bool)
    """
    @property
    def Duration(self) -> int:
        """
        Get: Duration(self: PartialCachingAttribute) -> int
        Set: Duration(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: PartialCachingAttribute) -> str
        Set: ProviderName(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def Shared(self) -> bool:
        """
        Get: Shared(self: PartialCachingAttribute) -> bool
        Set: Shared(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def SqlDependency(self) -> str:
        """
        Get: SqlDependency(self: PartialCachingAttribute) -> str
        Set: SqlDependency(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def VaryByControls(self) -> str:
        """
        Get: VaryByControls(self: PartialCachingAttribute) -> str
        Set: VaryByControls(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def VaryByCustom(self) -> str:
        """
        Get: VaryByCustom(self: PartialCachingAttribute) -> str
        Set: VaryByCustom(self: PartialCachingAttribute) = value
        """
        ...

    @property
    def VaryByParams(self) -> str:
        """
        Get: VaryByParams(self: PartialCachingAttribute) -> str
        Set: VaryByParams(self: PartialCachingAttribute) = value
        """
        ...


    def __new__(cls, duration:int, varyByParams:str = ..., varyByControls:str = ..., varyByCustom:str = ..., *__args:bool) -> Self:
        """
        __new__(cls: type, duration: int)
        __new__(cls: type, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str)
        __new__(cls: type, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, shared: bool)
        __new__(cls: type, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, shared: bool)
        """
        ...


class PartialCachingControl(BasePartialCachingControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    @property
    def CachedControl(self) -> Control:
        """ Get: CachedControl(self: PartialCachingControl) -> Control """
        ...



class PersistChildrenAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PersistChildrenAttribute(persist: bool)
    PersistChildrenAttribute(persist: bool, usesCustomPersistence: bool)
    """
    @property
    def Persist(self) -> bool:
        """ Get: Persist(self: PersistChildrenAttribute) -> bool """
        ...

    @property
    def UsesCustomPersistence(self) -> bool:
        """ Get: UsesCustomPersistence(self: PersistChildrenAttribute) -> bool """
        ...


    def __new__(cls, persist:bool, usesCustomPersistence:bool = ...) -> Self:
        """
        __new__(cls: type, persist: bool)
        __new__(cls: type, persist: bool, usesCustomPersistence: bool)
        """
        ...

    Default: PersistChildrenAttribute = ...
    No: PersistChildrenAttribute = ...
    Yes: PersistChildrenAttribute = ...


class PersistenceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PersistenceMode, values: Attribute (0), EncodedInnerDefaultProperty (3), InnerDefaultProperty (2), InnerProperty (1) """
    Attribute: PersistenceMode = ...
    EncodedInnerDefaultProperty: PersistenceMode = ...
    InnerDefaultProperty: PersistenceMode = ...
    InnerProperty: PersistenceMode = ...
    value__ = ...


class PersistenceModeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PersistenceModeAttribute(mode: PersistenceMode) """
    @property
    def Mode(self) -> PersistenceMode:
        """ Get: Mode(self: PersistenceModeAttribute) -> PersistenceMode """
        ...


    def __new__(cls, mode:PersistenceMode) -> Self:
        """ __new__(cls: type, mode: PersistenceMode) """
        ...

    Attribute: PersistenceModeAttribute = ...
    Default: PersistenceModeAttribute = ...
    EncodedInnerDefaultProperty: PersistenceModeAttribute = ...
    InnerDefaultProperty: PersistenceModeAttribute = ...
    InnerProperty: PersistenceModeAttribute = ...


class PostBackOptions: # skipped bases: <type 'object'>, <type 'object'>
    """
    PostBackOptions(targetControl: Control)
    PostBackOptions(targetControl: Control, argument: str)
    PostBackOptions(targetControl: Control, argument: str, actionUrl: str, autoPostBack: bool, requiresJavaScriptProtocol: bool, trackFocus: bool, clientSubmit: bool, performValidation: bool, validationGroup: str)
    """
    @property
    def ActionUrl(self) -> str:
        """
        Get: ActionUrl(self: PostBackOptions) -> str
        Set: ActionUrl(self: PostBackOptions) = value
        """
        ...

    @property
    def Argument(self) -> str:
        """
        Get: Argument(self: PostBackOptions) -> str
        Set: Argument(self: PostBackOptions) = value
        """
        ...

    @property
    def AutoPostBack(self) -> bool:
        """
        Get: AutoPostBack(self: PostBackOptions) -> bool
        Set: AutoPostBack(self: PostBackOptions) = value
        """
        ...

    @property
    def ClientSubmit(self) -> bool:
        """
        Get: ClientSubmit(self: PostBackOptions) -> bool
        Set: ClientSubmit(self: PostBackOptions) = value
        """
        ...

    @property
    def PerformValidation(self) -> bool:
        """
        Get: PerformValidation(self: PostBackOptions) -> bool
        Set: PerformValidation(self: PostBackOptions) = value
        """
        ...

    @property
    def RequiresJavaScriptProtocol(self) -> bool:
        """
        Get: RequiresJavaScriptProtocol(self: PostBackOptions) -> bool
        Set: RequiresJavaScriptProtocol(self: PostBackOptions) = value
        """
        ...

    @property
    def TargetControl(self) -> Control:
        """ Get: TargetControl(self: PostBackOptions) -> Control """
        ...

    @property
    def TrackFocus(self) -> bool:
        """
        Get: TrackFocus(self: PostBackOptions) -> bool
        Set: TrackFocus(self: PostBackOptions) = value
        """
        ...

    @property
    def ValidationGroup(self) -> str:
        """
        Get: ValidationGroup(self: PostBackOptions) -> str
        Set: ValidationGroup(self: PostBackOptions) = value
        """
        ...



class PostBackTrigger(UpdatePanelControlTrigger): # skipped bases: <type 'object'>
    """ PostBackTrigger() """
    def ToString(self) -> str:
        """ ToString(self: PostBackTrigger) -> str """
        ...


class ProfileServiceManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ProfileServiceManager() """
    @property
    def LoadProperties(self) -> Array:
        """
        Get: LoadProperties(self: ProfileServiceManager) -> Array[str]
        Set: LoadProperties(self: ProfileServiceManager) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ProfileServiceManager) -> str
        Set: Path(self: ProfileServiceManager) = value
        """
        ...



class PropertyConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EnumFromString(enumType:Type, value:str) -> object:
        """ EnumFromString(enumType: Type, value: str) -> object """
        ...

    @staticmethod
    def EnumToString(enumType:Type, enumValue:object) -> str:
        """ EnumToString(enumType: Type, enumValue: object) -> str """
        ...

    @staticmethod
    def ObjectFromString(objType:Type, propertyInfo:MemberInfo, value:str) -> object:
        """ ObjectFromString(objType: Type, propertyInfo: MemberInfo, value: str) -> object """
        ...

    __all__: list = ...


class RegisteredArrayDeclaration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: RegisteredArrayDeclaration) -> Control """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegisteredArrayDeclaration) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: RegisteredArrayDeclaration) -> str """
        ...



class RegisteredDisposeScript: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: RegisteredDisposeScript) -> Control """
        ...

    @property
    def Script(self) -> str:
        """ Get: Script(self: RegisteredDisposeScript) -> str """
        ...



class RegisteredExpandoAttribute: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: RegisteredExpandoAttribute) -> Control """
        ...

    @property
    def ControlId(self) -> str:
        """ Get: ControlId(self: RegisteredExpandoAttribute) -> str """
        ...

    @property
    def Encode(self) -> bool:
        """ Get: Encode(self: RegisteredExpandoAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegisteredExpandoAttribute) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: RegisteredExpandoAttribute) -> str """
        ...



class RegisteredHiddenField: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Control(self) -> Control:
        """ Get: Control(self: RegisteredHiddenField) -> Control """
        ...

    @property
    def InitialValue(self) -> str:
        """ Get: InitialValue(self: RegisteredHiddenField) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegisteredHiddenField) -> str """
        ...



class RegisteredScript: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AddScriptTags(self) -> bool:
        """ Get: AddScriptTags(self: RegisteredScript) -> bool """
        ...

    @property
    def Control(self) -> Control:
        """ Get: Control(self: RegisteredScript) -> Control """
        ...

    @property
    def Key(self) -> str:
        """ Get: Key(self: RegisteredScript) -> str """
        ...

    @property
    def Script(self) -> str:
        """ Get: Script(self: RegisteredScript) -> str """
        ...

    @property
    def ScriptType(self): # -> RegisteredScriptType
        """ Get: ScriptType(self: RegisteredScript) -> RegisteredScriptType """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: RegisteredScript) -> Type """
        ...

    @property
    def Url(self) -> str:
        """ Get: Url(self: RegisteredScript) -> str """
        ...



class RegisteredScriptType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegisteredScriptType, values: ClientScriptBlock (1), ClientScriptInclude (0), ClientStartupScript (2), OnSubmitStatement (3) """
    ClientScriptBlock: RegisteredScriptType = ...
    ClientScriptInclude: RegisteredScriptType = ...
    ClientStartupScript: RegisteredScriptType = ...
    OnSubmitStatement: RegisteredScriptType = ...
    value__ = ...


class RenderMethod(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RenderMethod(object: object, method: IntPtr) """
    def BeginInvoke(self, output:HtmlTextWriter, container:Control, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RenderMethod, output: HtmlTextWriter, container: Control, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RenderMethod, result: IAsyncResult) """
        ...

    def Invoke(self, output:HtmlTextWriter, container:Control): # -> 
        """ Invoke(self: RenderMethod, output: HtmlTextWriter, container: Control) """
        ...


class RenderTraceListener: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ListenerFactories(self) -> IList:
        """ Get: ListenerFactories() -> IList[Func[RenderTraceListener]] """
        ...


    def BeginRendering(self, writer:TextWriter, renderedObject:object): # -> 
        """ BeginRendering(self: RenderTraceListener, writer: TextWriter, renderedObject: object) """
        ...

    def EndRendering(self, writer:TextWriter, renderedObject:object): # -> 
        """ EndRendering(self: RenderTraceListener, writer: TextWriter, renderedObject: object) """
        ...

    def Initialize(self, context): # ->  # Not found arg types: {'context': 'HttpContext'}
        """ Initialize(self: RenderTraceListener, context: HttpContext) """
        ...

    def SetTraceData(self, tracedObject:object, traceDataKey:object, traceDataValue:object): # -> 
        """ SetTraceData(self: RenderTraceListener, tracedObject: object, traceDataKey: object, traceDataValue: object) """
        ...

    def ShareTraceData(self, source:object, destination:object): # -> 
        """ ShareTraceData(self: RenderTraceListener, source: object, destination: object) """
        ...



class RoleServiceManager: # skipped bases: <type 'object'>, <type 'object'>
    """ RoleServiceManager() """
    @property
    def LoadRoles(self) -> bool:
        """
        Get: LoadRoles(self: RoleServiceManager) -> bool
        Set: LoadRoles(self: RoleServiceManager) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: RoleServiceManager) -> str
        Set: Path(self: RoleServiceManager) = value
        """
        ...



class ScriptDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetScript(self, *args): #cannot find CLR method
        """ GetScript(self: ScriptDescriptor) -> str """
        ...


class ScriptComponentDescriptor(ScriptDescriptor): # skipped bases: <type 'object'>
    """ ScriptComponentDescriptor(type: str) """
    @property
    def ClientID(self) -> str:
        """ Get: ClientID(self: ScriptComponentDescriptor) -> str """
        ...

    @property
    def ID(self) -> str:
        """
        Get: ID(self: ScriptComponentDescriptor) -> str
        Set: ID(self: ScriptComponentDescriptor) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ScriptComponentDescriptor) -> str
        Set: Type(self: ScriptComponentDescriptor) = value
        """
        ...


    def AddComponentProperty(self, name:str, componentID:str): # -> 
        """ AddComponentProperty(self: ScriptComponentDescriptor, name: str, componentID: str) """
        ...

    def AddElementProperty(self, name:str, elementID:str): # -> 
        """ AddElementProperty(self: ScriptComponentDescriptor, name: str, elementID: str) """
        ...

    def AddEvent(self, name:str, handler:str): # -> 
        """ AddEvent(self: ScriptComponentDescriptor, name: str, handler: str) """
        ...

    def AddProperty(self, name:str, value:object): # -> 
        """ AddProperty(self: ScriptComponentDescriptor, name: str, value: object) """
        ...

    def AddScriptProperty(self, name:str, script:str): # -> 
        """ AddScriptProperty(self: ScriptComponentDescriptor, name: str, script: str) """
        ...

    def __new__(cls, type:str) -> Self:
        """ __new__(cls: type, type: str) """
        ...


class ScriptBehaviorDescriptor(ScriptComponentDescriptor): # skipped bases: <type 'object'>
    """ ScriptBehaviorDescriptor(type: str, elementID: str) """
    @property
    def ElementID(self) -> str:
        """ Get: ElementID(self: ScriptBehaviorDescriptor) -> str """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ScriptBehaviorDescriptor) -> str
        Set: Name(self: ScriptBehaviorDescriptor) = value
        """
        ...



class ScriptControl(IScriptControl, WebControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IAttributeAccessor'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ no doc """
    pass

class ScriptControlDescriptor(ScriptComponentDescriptor): # skipped bases: <type 'object'>
    """ ScriptControlDescriptor(type: str, elementID: str) """
    @property
    def ElementID(self) -> str:
        """ Get: ElementID(self: ScriptControlDescriptor) -> str """
        ...



class ScriptManager(IScriptManagerInternal, IScriptManager, IControl, IPostBackDataHandler, Control, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IClientUrlResolver'>, <type 'object'>
    """ ScriptManager() """
    @property
    def AjaxFrameworkAssembly(self) -> Assembly:
        """ Get: AjaxFrameworkAssembly(self: ScriptManager) -> Assembly """
        ...

    @property
    def AjaxFrameworkMode(self) -> AjaxFrameworkMode:
        """
        Get: AjaxFrameworkMode(self: ScriptManager) -> AjaxFrameworkMode
        Set: AjaxFrameworkMode(self: ScriptManager) = value
        """
        ...

    @property
    def AllowCustomErrorsRedirect(self) -> bool:
        """
        Get: AllowCustomErrorsRedirect(self: ScriptManager) -> bool
        Set: AllowCustomErrorsRedirect(self: ScriptManager) = value
        """
        ...

    @property
    def AsyncPostBackErrorMessage(self) -> str:
        """
        Get: AsyncPostBackErrorMessage(self: ScriptManager) -> str
        Set: AsyncPostBackErrorMessage(self: ScriptManager) = value
        """
        ...

    @property
    def AsyncPostBackSourceElementID(self) -> str:
        """ Get: AsyncPostBackSourceElementID(self: ScriptManager) -> str """
        ...

    @property
    def AsyncPostBackTimeout(self) -> int:
        """
        Get: AsyncPostBackTimeout(self: ScriptManager) -> int
        Set: AsyncPostBackTimeout(self: ScriptManager) = value
        """
        ...

    @property
    def AuthenticationService(self) -> AuthenticationServiceManager:
        """ Get: AuthenticationService(self: ScriptManager) -> AuthenticationServiceManager """
        ...

    @property
    def ClientNavigateHandler(self) -> str:
        """
        Get: ClientNavigateHandler(self: ScriptManager) -> str
        Set: ClientNavigateHandler(self: ScriptManager) = value
        """
        ...

    @property
    def CompositeScript(self) -> CompositeScriptReference:
        """ Get: CompositeScript(self: ScriptManager) -> CompositeScriptReference """
        ...

    @property
    def EmptyPageUrl(self) -> str:
        """
        Get: EmptyPageUrl(self: ScriptManager) -> str
        Set: EmptyPageUrl(self: ScriptManager) = value
        """
        ...

    @property
    def EnableCdn(self) -> bool:
        """
        Get: EnableCdn(self: ScriptManager) -> bool
        Set: EnableCdn(self: ScriptManager) = value
        """
        ...

    @property
    def EnableCdnFallback(self) -> bool:
        """
        Get: EnableCdnFallback(self: ScriptManager) -> bool
        Set: EnableCdnFallback(self: ScriptManager) = value
        """
        ...

    @property
    def EnableHistory(self) -> bool:
        """
        Get: EnableHistory(self: ScriptManager) -> bool
        Set: EnableHistory(self: ScriptManager) = value
        """
        ...

    @property
    def EnablePageMethods(self) -> bool:
        """
        Get: EnablePageMethods(self: ScriptManager) -> bool
        Set: EnablePageMethods(self: ScriptManager) = value
        """
        ...

    @property
    def EnablePartialRendering(self) -> bool:
        """
        Get: EnablePartialRendering(self: ScriptManager) -> bool
        Set: EnablePartialRendering(self: ScriptManager) = value
        """
        ...

    @property
    def EnableScriptGlobalization(self) -> bool:
        """
        Get: EnableScriptGlobalization(self: ScriptManager) -> bool
        Set: EnableScriptGlobalization(self: ScriptManager) = value
        """
        ...

    @property
    def EnableScriptLocalization(self) -> bool:
        """
        Get: EnableScriptLocalization(self: ScriptManager) -> bool
        Set: EnableScriptLocalization(self: ScriptManager) = value
        """
        ...

    @property
    def EnableSecureHistoryState(self) -> bool:
        """
        Get: EnableSecureHistoryState(self: ScriptManager) -> bool
        Set: EnableSecureHistoryState(self: ScriptManager) = value
        """
        ...

    @property
    def IsDebuggingEnabled(self) -> bool:
        """ Get: IsDebuggingEnabled(self: ScriptManager) -> bool """
        ...

    @property
    def IsInAsyncPostBack(self) -> bool:
        """ Get: IsInAsyncPostBack(self: ScriptManager) -> bool """
        ...

    @property
    def IsNavigating(self) -> bool:
        """ Get: IsNavigating(self: ScriptManager) -> bool """
        ...

    @property
    def LoadScriptsBeforeUI(self) -> bool:
        """
        Get: LoadScriptsBeforeUI(self: ScriptManager) -> bool
        Set: LoadScriptsBeforeUI(self: ScriptManager) = value
        """
        ...

    @property
    def ProfileService(self) -> ProfileServiceManager:
        """ Get: ProfileService(self: ScriptManager) -> ProfileServiceManager """
        ...

    @property
    def RoleService(self) -> RoleServiceManager:
        """ Get: RoleService(self: ScriptManager) -> RoleServiceManager """
        ...

    @property
    def ScriptMode(self): # -> ScriptMode
        """
        Get: ScriptMode(self: ScriptManager) -> ScriptMode
        Set: ScriptMode(self: ScriptManager) = value
        """
        ...

    @property
    def ScriptPath(self) -> str:
        """
        Get: ScriptPath(self: ScriptManager) -> str
        Set: ScriptPath(self: ScriptManager) = value
        """
        ...

    @property
    def ScriptResourceMapping(self): # -> ScriptResourceMapping
        """ Get: ScriptResourceMapping() -> ScriptResourceMapping """
        ...

    @property
    def Scripts(self): # -> ScriptReferenceCollection
        """ Get: Scripts(self: ScriptManager) -> ScriptReferenceCollection """
        ...

    @property
    def Services(self): # -> ServiceReferenceCollection
        """ Get: Services(self: ScriptManager) -> ServiceReferenceCollection """
        ...

    @property
    def SupportsPartialRendering(self) -> bool:
        """
        Get: SupportsPartialRendering(self: ScriptManager) -> bool
        Set: SupportsPartialRendering(self: ScriptManager) = value
        """
        ...


    def AddHistoryPoint(self, *__args): # -> 
        """ AddHistoryPoint(self: ScriptManager, key: str, value: str)AddHistoryPoint(self: ScriptManager, key: str, value: str, title: str)AddHistoryPoint(self: ScriptManager, state: NameValueCollection, title: str) """
        ...

    @staticmethod
    def GetCurrent(page:Page) -> ScriptManager:
        """ GetCurrent(page: Page) -> ScriptManager """
        ...

    def GetRegisteredArrayDeclarations(self) -> ReadOnlyCollection:
        """ GetRegisteredArrayDeclarations(self: ScriptManager) -> ReadOnlyCollection[RegisteredArrayDeclaration] """
        ...

    def GetRegisteredClientScriptBlocks(self) -> ReadOnlyCollection:
        """ GetRegisteredClientScriptBlocks(self: ScriptManager) -> ReadOnlyCollection[RegisteredScript] """
        ...

    def GetRegisteredDisposeScripts(self) -> ReadOnlyCollection:
        """ GetRegisteredDisposeScripts(self: ScriptManager) -> ReadOnlyCollection[RegisteredDisposeScript] """
        ...

    def GetRegisteredExpandoAttributes(self) -> ReadOnlyCollection:
        """ GetRegisteredExpandoAttributes(self: ScriptManager) -> ReadOnlyCollection[RegisteredExpandoAttribute] """
        ...

    def GetRegisteredHiddenFields(self) -> ReadOnlyCollection:
        """ GetRegisteredHiddenFields(self: ScriptManager) -> ReadOnlyCollection[RegisteredHiddenField] """
        ...

    def GetRegisteredOnSubmitStatements(self) -> ReadOnlyCollection:
        """ GetRegisteredOnSubmitStatements(self: ScriptManager) -> ReadOnlyCollection[RegisteredScript] """
        ...

    def GetRegisteredStartupScripts(self) -> ReadOnlyCollection:
        """ GetRegisteredStartupScripts(self: ScriptManager) -> ReadOnlyCollection[RegisteredScript] """
        ...

    def GetStateString(self) -> str:
        """ GetStateString(self: ScriptManager) -> str """
        ...

    def OnAsyncPostBackError(self, *args): #cannot find CLR method
        """ OnAsyncPostBackError(self: ScriptManager, e: AsyncPostBackErrorEventArgs) """
        ...

    def OnResolveCompositeScriptReference(self, *args): #cannot find CLR method
        """ OnResolveCompositeScriptReference(self: ScriptManager, e: CompositeScriptReferenceEventArgs) """
        ...

    def OnResolveScriptReference(self, *args): #cannot find CLR method
        """ OnResolveScriptReference(self: ScriptManager, e: ScriptReferenceEventArgs) """
        ...

    @staticmethod
    def RegisterArrayDeclaration(*__args): # -> 
        """ RegisterArrayDeclaration(page: Page, arrayName: str, arrayValue: str)RegisterArrayDeclaration(control: Control, arrayName: str, arrayValue: str) """
        ...

    def RegisterAsyncPostBackControl(self, control:Control): # -> 
        """ RegisterAsyncPostBackControl(self: ScriptManager, control: Control) """
        ...

    @staticmethod
    def RegisterClientScriptBlock(*__args): # -> 
        """ RegisterClientScriptBlock(page: Page, type: Type, key: str, script: str, addScriptTags: bool)RegisterClientScriptBlock(control: Control, type: Type, key: str, script: str, addScriptTags: bool) """
        ...

    @staticmethod
    def RegisterClientScriptInclude(*__args): # -> 
        """ RegisterClientScriptInclude(page: Page, type: Type, key: str, url: str)RegisterClientScriptInclude(control: Control, type: Type, key: str, url: str) """
        ...

    @staticmethod
    def RegisterClientScriptResource(*__args): # -> 
        """ RegisterClientScriptResource(page: Page, type: Type, resourceName: str)RegisterClientScriptResource(control: Control, type: Type, resourceName: str) """
        ...

    def RegisterDataItem(self, control:Control, dataItem:str, isJsonSerialized:bool = ...): # -> 
        """ RegisterDataItem(self: ScriptManager, control: Control, dataItem: str)RegisterDataItem(self: ScriptManager, control: Control, dataItem: str, isJsonSerialized: bool) """
        ...

    def RegisterDispose(self, control:Control, disposeScript:str): # -> 
        """ RegisterDispose(self: ScriptManager, control: Control, disposeScript: str) """
        ...

    @staticmethod
    def RegisterExpandoAttribute(control:Control, controlId:str, attributeName:str, attributeValue:str, encode:bool): # -> 
        """ RegisterExpandoAttribute(control: Control, controlId: str, attributeName: str, attributeValue: str, encode: bool) """
        ...

    def RegisterExtenderControl(self, extenderControl, targetControl:Control): # ->  # Not found arg types: {'extenderControl': 'TExtenderControl'}
        """ RegisterExtenderControl[TExtenderControl](self: ScriptManager, extenderControl: TExtenderControl, targetControl: Control) """
        ...

    @staticmethod
    def RegisterHiddenField(*__args): # -> 
        """ RegisterHiddenField(page: Page, hiddenFieldName: str, hiddenFieldInitialValue: str)RegisterHiddenField(control: Control, hiddenFieldName: str, hiddenFieldInitialValue: str) """
        ...

    @staticmethod
    def RegisterNamedClientScriptResource(*__args): # -> 
        """ RegisterNamedClientScriptResource(control: Control, resourceName: str)RegisterNamedClientScriptResource(page: Page, resourceName: str) """
        ...

    @staticmethod
    def RegisterOnSubmitStatement(*__args): # -> 
        """ RegisterOnSubmitStatement(page: Page, type: Type, key: str, script: str)RegisterOnSubmitStatement(control: Control, type: Type, key: str, script: str) """
        ...

    def RegisterPostBackControl(self, control:Control): # -> 
        """ RegisterPostBackControl(self: ScriptManager, control: Control) """
        ...

    def RegisterScriptControl(self, scriptControl): # ->  # Not found arg types: {'scriptControl': 'TScriptControl'}
        """ RegisterScriptControl[TScriptControl](self: ScriptManager, scriptControl: TScriptControl) """
        ...

    def RegisterScriptDescriptors(self, *__args:IExtenderControl): # -> 
        """ RegisterScriptDescriptors(self: ScriptManager, extenderControl: IExtenderControl)RegisterScriptDescriptors(self: ScriptManager, scriptControl: IScriptControl) """
        ...

    @staticmethod
    def RegisterStartupScript(*__args): # -> 
        """ RegisterStartupScript(page: Page, type: Type, key: str, script: str, addScriptTags: bool)RegisterStartupScript(control: Control, type: Type, key: str, script: str, addScriptTags: bool) """
        ...

    def SetFocus(self, *__args:Control): # -> 
        """ SetFocus(self: ScriptManager, control: Control)SetFocus(self: ScriptManager, clientID: str) """
        ...

    AsyncPostBackError = ...
    Navigate = ...
    ResolveCompositeScriptReference = ...
    ResolveScriptReference = ...


class ScriptManagerProxy(Control, IControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'IClientUrlResolver'>, <type 'object'>
    """ ScriptManagerProxy() """
    @property
    def AuthenticationService(self) -> AuthenticationServiceManager:
        """ Get: AuthenticationService(self: ScriptManagerProxy) -> AuthenticationServiceManager """
        ...

    @property
    def CompositeScript(self) -> CompositeScriptReference:
        """ Get: CompositeScript(self: ScriptManagerProxy) -> CompositeScriptReference """
        ...

    @property
    def ProfileService(self) -> ProfileServiceManager:
        """ Get: ProfileService(self: ScriptManagerProxy) -> ProfileServiceManager """
        ...

    @property
    def RoleService(self) -> RoleServiceManager:
        """ Get: RoleService(self: ScriptManagerProxy) -> RoleServiceManager """
        ...

    @property
    def Scripts(self): # -> ScriptReferenceCollection
        """ Get: Scripts(self: ScriptManagerProxy) -> ScriptReferenceCollection """
        ...

    @property
    def Services(self): # -> ServiceReferenceCollection
        """ Get: Services(self: ScriptManagerProxy) -> ServiceReferenceCollection """
        ...


    Navigate = ...


class ScriptMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ScriptMode, values: Auto (0), Debug (2), Inherit (1), Release (3) """
    Auto: ScriptMode = ...
    Debug: ScriptMode = ...
    Inherit: ScriptMode = ...
    Release: ScriptMode = ...
    value__ = ...


class ScriptReference(ScriptReferenceBase): # skipped bases: <type 'object'>
    """
    ScriptReference()
    ScriptReference(name: str, assembly: str)
    ScriptReference(path: str)
    """
    @property
    def Assembly(self) -> str:
        """
        Get: Assembly(self: ScriptReference) -> str
        Set: Assembly(self: ScriptReference) = value
        """
        ...

    @property
    def IgnoreScriptPath(self) -> bool:
        """
        Get: IgnoreScriptPath(self: ScriptReference) -> bool
        Set: IgnoreScriptPath(self: ScriptReference) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ScriptReference) -> str
        Set: Name(self: ScriptReference) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ScriptReference) -> str """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, assembly: str)
        __new__(cls: type, path: str)
        """
        ...


class ScriptReferenceCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[ScriptReference]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[ScriptReference]'>, <type 'IEnumerable[ScriptReference]'>, <type 'IList[ScriptReference]'>, <type 'ICollection[ScriptReference]'>, <type 'ICollection'>, <type 'object'>
    """ ScriptReferenceCollection() """
    pass

class ScriptReferenceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ScriptReferenceEventArgs(script: ScriptReference) """
    @property
    def Script(self) -> ScriptReference:
        """ Get: Script(self: ScriptReferenceEventArgs) -> ScriptReference """
        ...


    def __new__(cls, script:ScriptReference) -> Self:
        """ __new__(cls: type, script: ScriptReference) """
        ...


class ScriptResourceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ScriptResourceAttribute(scriptName: str)
    ScriptResourceAttribute(scriptName: str, stringResourceName: str, stringResourceClientTypeName: str)
    """
    @property
    def ScriptName(self) -> str:
        """ Get: ScriptName(self: ScriptResourceAttribute) -> str """
        ...

    @property
    def ScriptResourceName(self) -> str:
        """ Get: ScriptResourceName(self: ScriptResourceAttribute) -> str """
        ...

    @property
    def StringResourceClientTypeName(self) -> str:
        """ Get: StringResourceClientTypeName(self: ScriptResourceAttribute) -> str """
        ...

    @property
    def StringResourceName(self) -> str:
        """ Get: StringResourceName(self: ScriptResourceAttribute) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ScriptResourceAttribute) -> str """
        ...


    def __new__(cls, scriptName:str, stringResourceName:str = ..., stringResourceClientTypeName:str = ...) -> Self:
        """
        __new__(cls: type, scriptName: str)
        __new__(cls: type, scriptName: str, stringResourceName: str, stringResourceClientTypeName: str)
        """
        ...


class ScriptResourceDefinition(IScriptResourceDefinition): # skipped bases: <type 'object'>
    """ ScriptResourceDefinition() """
    @property
    def CdnDebugPath(self) -> str:
        """
        Get: CdnDebugPath(self: ScriptResourceDefinition) -> str
        Set: CdnDebugPath(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def CdnPath(self) -> str:
        """
        Get: CdnPath(self: ScriptResourceDefinition) -> str
        Set: CdnPath(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def CdnSupportsSecureConnection(self) -> bool:
        """
        Get: CdnSupportsSecureConnection(self: ScriptResourceDefinition) -> bool
        Set: CdnSupportsSecureConnection(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def DebugPath(self) -> str:
        """
        Get: DebugPath(self: ScriptResourceDefinition) -> str
        Set: DebugPath(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def LoadSuccessExpression(self) -> str:
        """
        Get: LoadSuccessExpression(self: ScriptResourceDefinition) -> str
        Set: LoadSuccessExpression(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ScriptResourceDefinition) -> str
        Set: Path(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def ResourceAssembly(self) -> Assembly:
        """
        Get: ResourceAssembly(self: ScriptResourceDefinition) -> Assembly
        Set: ResourceAssembly(self: ScriptResourceDefinition) = value
        """
        ...

    @property
    def ResourceName(self) -> str:
        """
        Get: ResourceName(self: ScriptResourceDefinition) -> str
        Set: ResourceName(self: ScriptResourceDefinition) = value
        """
        ...



class ScriptResourceMapping(IScriptResourceMapping): # skipped bases: <type 'object'>
    """ ScriptResourceMapping() """
    def AddDefinition(self, name:str, *__args:ScriptResourceDefinition): # -> 
        """ AddDefinition(self: ScriptResourceMapping, name: str, definition: ScriptResourceDefinition)AddDefinition(self: ScriptResourceMapping, name: str, assembly: Assembly, definition: ScriptResourceDefinition) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ScriptResourceMapping) """
        ...

    def GetDefinition(self, *__args:str) -> ScriptResourceDefinition:
        """
        GetDefinition(self: ScriptResourceMapping, name: str) -> ScriptResourceDefinition
        GetDefinition(self: ScriptResourceMapping, name: str, assembly: Assembly) -> ScriptResourceDefinition
        GetDefinition(self: ScriptResourceMapping, scriptReference: ScriptReference) -> ScriptResourceDefinition
        """
        ...

    def RemoveDefinition(self, name:str, assembly:Assembly = ...) -> ScriptResourceDefinition:
        """
        RemoveDefinition(self: ScriptResourceMapping, name: str) -> ScriptResourceDefinition
        RemoveDefinition(self: ScriptResourceMapping, name: str, assembly: Assembly) -> ScriptResourceDefinition
        """
        ...


class ServiceReference: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceReference()
    ServiceReference(path: str)
    """
    @property
    def InlineScript(self) -> bool:
        """
        Get: InlineScript(self: ServiceReference) -> bool
        Set: InlineScript(self: ServiceReference) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ServiceReference) -> str
        Set: Path(self: ServiceReference) = value
        """
        ...


    def GetProxyScript(self, *args): #cannot find CLR method
        """ GetProxyScript(self: ServiceReference, scriptManager: ScriptManager, containingControl: Control) -> str """
        ...

    def GetProxyUrl(self, *args): #cannot find CLR method
        """ GetProxyUrl(self: ServiceReference, scriptManager: ScriptManager, containingControl: Control) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: ServiceReference) -> str """
        ...


class ServiceReferenceCollection(Collection): # skipped bases: <type 'IReadOnlyList[ServiceReference]'>, <type 'IList[ServiceReference]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[ServiceReference]'>, <type 'IEnumerable[ServiceReference]'>, <type 'ICollection'>, <type 'ICollection[ServiceReference]'>, <type 'object'>
    """ ServiceReferenceCollection() """
    pass

class SessionPageStatePersister(PageStatePersister): # skipped bases: <type 'object'>
    """ SessionPageStatePersister(page: Page) """
    pass

class SimplePropertyEntry(PropertyEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def PersistedValue(self) -> str:
        """
        Get: PersistedValue(self: SimplePropertyEntry) -> str
        Set: PersistedValue(self: SimplePropertyEntry) = value
        """
        ...

    @property
    def UseSetAttribute(self) -> bool:
        """
        Get: UseSetAttribute(self: SimplePropertyEntry) -> bool
        Set: UseSetAttribute(self: SimplePropertyEntry) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: SimplePropertyEntry) -> object
        Set: Value(self: SimplePropertyEntry) = value
        """
        ...



class SimpleWebHandlerParser(IAssemblyDependencyParser): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultDirectiveName(self):
        ...


    def GetCompiledTypeFromCache(self, *args): #cannot find CLR method
        """ GetCompiledTypeFromCache(self: SimpleWebHandlerParser) -> Type """
        ...


class SkinBuilder(ControlBuilder): # skipped bases: <type 'object'>
    """ SkinBuilder(provider: ThemeProvider, control: Control, skinBuilder: ControlBuilder, themePath: str) """
    def ApplyTheme(self) -> Control:
        """ ApplyTheme(self: SkinBuilder) -> Control """
        ...

    def __new__(cls, provider, control:Control, skinBuilder:ControlBuilder, themePath:str) -> Self: # Not found arg types: {'provider': 'ThemeProvider'}
        """ __new__(cls: type, provider: ThemeProvider, control: Control, skinBuilder: ControlBuilder, themePath: str) """
        ...


class StateBag(IDictionary, IStateManager): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    StateBag()
    StateBag(ignoreCase: bool)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StateBag) -> int """
        ...


    def IsItemDirty(self, key:str) -> bool:
        """ IsItemDirty(self: StateBag, key: str) -> bool """
        ...

    def SetDirty(self, dirty:bool): # -> 
        """ SetDirty(self: StateBag, dirty: bool) """
        ...

    def SetItemDirty(self, key:str, dirty:bool): # -> 
        """ SetItemDirty(self: StateBag, key: str, dirty: bool) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class StateItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsDirty(self) -> bool:
        """
        Get: IsDirty(self: StateItem) -> bool
        Set: IsDirty(self: StateItem) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: StateItem) -> object
        Set: Value(self: StateItem) = value
        """
        ...



class StateManagedCollection(IList, IStateManager): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StateManagedCollection) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: StateManagedCollection, array: Array, index: int) """
        ...

    def CreateKnownType(self, *args): #cannot find CLR method
        """ CreateKnownType(self: StateManagedCollection, index: int) -> object """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: StateManagedCollection) -> IEnumerator """
        ...

    def GetKnownTypes(self, *args): #cannot find CLR method
        """ GetKnownTypes(self: StateManagedCollection) -> Array[Type] """
        ...

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: StateManagedCollection) """
        ...

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: StateManagedCollection) """
        ...

    def OnInsert(self, *args): #cannot find CLR method
        """ OnInsert(self: StateManagedCollection, index: int, value: object) """
        ...

    def OnInsertComplete(self, *args): #cannot find CLR method
        """ OnInsertComplete(self: StateManagedCollection, index: int, value: object) """
        ...

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: StateManagedCollection, index: int, value: object) """
        ...

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: StateManagedCollection, index: int, value: object) """
        ...

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: StateManagedCollection, value: object) """
        ...

    def SetDirty(self): # -> 
        """ SetDirty(self: StateManagedCollection) """
        ...

    def SetDirtyObject(self, *args): #cannot find CLR method
        """ SetDirtyObject(self: StateManagedCollection, o: object) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class StaticPartialCachingControl(BasePartialCachingControl): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """
    StaticPartialCachingControl(ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, buildMethod: BuildMethod)
    StaticPartialCachingControl(ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod)
    StaticPartialCachingControl(ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod, providerName: str)
    """
    @staticmethod
    def BuildCachedControl(parent:Control, ctrlID:str, guid:str, duration:int, varyByParams:str, varyByControls:str, varyByCustom:str, *__args:BuildMethod): # -> 
        """ BuildCachedControl(parent: Control, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, buildMethod: BuildMethod)BuildCachedControl(parent: Control, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod)BuildCachedControl(parent: Control, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod, providerName: str) """
        ...

    def __new__(cls, ctrlID:str, guid:str, duration:int, varyByParams:str, varyByControls:str, varyByCustom:str, *__args:BuildMethod) -> Self:
        """
        __new__(cls: type, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, buildMethod: BuildMethod)
        __new__(cls: type, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod)
        __new__(cls: type, ctrlID: str, guid: str, duration: int, varyByParams: str, varyByControls: str, varyByCustom: str, sqlDependency: str, buildMethod: BuildMethod, providerName: str)
        """
        ...


class SupportsEventValidationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SupportsEventValidationAttribute() """
    pass

class TagPrefixAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TagPrefixAttribute(namespaceName: str, tagPrefix: str) """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: TagPrefixAttribute) -> str """
        ...

    @property
    def TagPrefix(self) -> str:
        """ Get: TagPrefix(self: TagPrefixAttribute) -> str """
        ...


    def __new__(cls, namespaceName:str, tagPrefix:str) -> Self:
        """ __new__(cls: type, namespaceName: str, tagPrefix: str) """
        ...


class TargetControlTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TargetControlTypeAttribute(targetControlType: Type) """
    @property
    def TargetControlType(self) -> Type:
        """ Get: TargetControlType(self: TargetControlTypeAttribute) -> Type """
        ...


    def __new__(cls, targetControlType:Type) -> Self:
        """ __new__(cls: type, targetControlType: Type) """
        ...


class TemplateContainerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TemplateContainerAttribute(containerType: Type)
    TemplateContainerAttribute(containerType: Type, bindingDirection: BindingDirection)
    """
    @property
    def BindingDirection(self) -> BindingDirection:
        """ Get: BindingDirection(self: TemplateContainerAttribute) -> BindingDirection """
        ...

    @property
    def ContainerType(self) -> Type:
        """ Get: ContainerType(self: TemplateContainerAttribute) -> Type """
        ...


    def __new__(cls, containerType:Type, bindingDirection:BindingDirection = ...) -> Self:
        """
        __new__(cls: type, containerType: Type)
        __new__(cls: type, containerType: Type, bindingDirection: BindingDirection)
        """
        ...


class TemplateInstance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TemplateInstance, values: Multiple (0), Single (1) """
    Multiple: TemplateInstance = ...
    Single: TemplateInstance = ...
    value__ = ...


class TemplateInstanceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TemplateInstanceAttribute(instances: TemplateInstance) """
    @property
    def Instances(self) -> TemplateInstance:
        """ Get: Instances(self: TemplateInstanceAttribute) -> TemplateInstance """
        ...


    def __new__(cls, instances:TemplateInstance) -> Self:
        """ __new__(cls: type, instances: TemplateInstance) """
        ...

    Default: TemplateInstanceAttribute = ...
    Multiple: TemplateInstanceAttribute = ...
    Single: TemplateInstanceAttribute = ...


class TemplatePropertyEntry(BuilderPropertyEntry): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BindableTemplate(self) -> bool:
        """ Get: BindableTemplate(self: TemplatePropertyEntry) -> bool """
        ...



class ThemeableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ThemeableAttribute(themeable: bool) """
    @property
    def Themeable(self) -> bool:
        """ Get: Themeable(self: ThemeableAttribute) -> bool """
        ...


    @staticmethod
    def IsObjectThemeable(instance:object) -> bool:
        """ IsObjectThemeable(instance: object) -> bool """
        ...

    @staticmethod
    def IsTypeThemeable(type:Type) -> bool:
        """ IsTypeThemeable(type: Type) -> bool """
        ...

    def __new__(cls, themeable:bool) -> Self:
        """ __new__(cls: type, themeable: bool) """
        ...

    Default: ThemeableAttribute = ...
    No: ThemeableAttribute = ...
    Yes: ThemeableAttribute = ...


class ThemeProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ ThemeProvider(host: IDesignerHost, name: str, themeDefinition: str, cssFiles: Array[str], themePath: str) """
    @property
    def ContentHashCode(self) -> int:
        """ Get: ContentHashCode(self: ThemeProvider) -> int """
        ...

    @property
    def CssFiles(self) -> ICollection:
        """ Get: CssFiles(self: ThemeProvider) -> ICollection """
        ...

    @property
    def DesignerHost(self) -> IDesignerHost:
        """ Get: DesignerHost(self: ThemeProvider) -> IDesignerHost """
        ...

    @property
    def ThemeName(self) -> str:
        """ Get: ThemeName(self: ThemeProvider) -> str """
        ...


    def GetSkinBuilder(self, control:Control) -> SkinBuilder:
        """ GetSkinBuilder(self: ThemeProvider, control: Control) -> SkinBuilder """
        ...

    def GetSkinControlBuildersForControlType(self, type:Type) -> IDictionary:
        """ GetSkinControlBuildersForControlType(self: ThemeProvider, type: Type) -> IDictionary """
        ...

    def GetSkinsForControl(self, type:Type) -> ICollection:
        """ GetSkinsForControl(self: ThemeProvider, type: Type) -> ICollection """
        ...


class Timer(IScriptControl, Control, IPostBackEventHandler): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ Timer() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Timer) -> bool
        Set: Enabled(self: Timer) = value
        """
        ...

    @property
    def Interval(self) -> int:
        """
        Get: Interval(self: Timer) -> int
        Set: Interval(self: Timer) = value
        """
        ...


    def OnTick(self, *args): #cannot find CLR method
        """ OnTick(self: Timer, e: EventArgs) """
        ...

    Tick = ...


class ToolboxDataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ToolboxDataAttribute(data: str) """
    @property
    def Data(self) -> str:
        """ Get: Data(self: ToolboxDataAttribute) -> str """
        ...


    def __new__(cls, data:str) -> Self:
        """ __new__(cls: type, data: str) """
        ...

    Default: ToolboxDataAttribute = ...


class Triplet: # skipped bases: <type 'object'>, <type 'object'>
    """
    Triplet()
    Triplet(x: object, y: object)
    Triplet(x: object, y: object, z: object)
    """
    First = ...
    Second = ...
    Third = ...


class UnobtrusiveValidationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnobtrusiveValidationMode, values: None (0), WebForms (1) """
    value__ = ...
    WebForms: UnobtrusiveValidationMode = ...


class UpdatePanel(IAttributeAccessor, Control, IUpdatePanel): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ UpdatePanel() """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: UpdatePanel) -> AttributeCollection """
        ...

    @property
    def ChildrenAsTriggers(self) -> bool:
        """
        Get: ChildrenAsTriggers(self: UpdatePanel) -> bool
        Set: ChildrenAsTriggers(self: UpdatePanel) = value
        """
        ...

    @property
    def ContentTemplate(self) -> ITemplate:
        """
        Get: ContentTemplate(self: UpdatePanel) -> ITemplate
        Set: ContentTemplate(self: UpdatePanel) = value
        """
        ...

    @property
    def ContentTemplateContainer(self) -> Control:
        """ Get: ContentTemplateContainer(self: UpdatePanel) -> Control """
        ...

    @property
    def IsInPartialRendering(self) -> bool:
        """ Get: IsInPartialRendering(self: UpdatePanel) -> bool """
        ...

    @property
    def RenderMode(self): # -> UpdatePanelRenderMode
        """
        Get: RenderMode(self: UpdatePanel) -> UpdatePanelRenderMode
        Set: RenderMode(self: UpdatePanel) = value
        """
        ...

    @property
    def RequiresUpdate(self):
        ...

    @property
    def Triggers(self): # -> UpdatePanelTriggerCollection
        """ Get: Triggers(self: UpdatePanel) -> UpdatePanelTriggerCollection """
        ...

    @property
    def UpdateMode(self): # -> UpdatePanelUpdateMode
        """
        Get: UpdateMode(self: UpdatePanel) -> UpdatePanelUpdateMode
        Set: UpdateMode(self: UpdatePanel) = value
        """
        ...


    def CreateContentTemplateContainer(self, *args): #cannot find CLR method
        """ CreateContentTemplateContainer(self: UpdatePanel) -> Control """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: UpdatePanel) """
        ...

    def Update(self): # -> 
        """ Update(self: UpdatePanel) """
        ...


class UpdatePanelRenderMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdatePanelRenderMode, values: Block (0), Inline (1) """
    Block: UpdatePanelRenderMode = ...
    Inline: UpdatePanelRenderMode = ...
    value__ = ...


class UpdatePanelTriggerCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[UpdatePanelTrigger]'>, <type 'IReadOnlyList[UpdatePanelTrigger]'>, <type 'IEnumerable[UpdatePanelTrigger]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[UpdatePanelTrigger]'>, <type 'IList[UpdatePanelTrigger]'>, <type 'ICollection'>, <type 'object'>
    """ UpdatePanelTriggerCollection(owner: UpdatePanel) """
    @property
    def Owner(self) -> UpdatePanel:
        """ Get: Owner(self: UpdatePanelTriggerCollection) -> UpdatePanel """
        ...



class UpdatePanelUpdateMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdatePanelUpdateMode, values: Always (0), Conditional (1) """
    Always: UpdatePanelUpdateMode = ...
    Conditional: UpdatePanelUpdateMode = ...
    value__ = ...


class UpdateProgress(IAttributeAccessor, IScriptControl, Control): # skipped bases: <type 'IDisposable'>, <type 'IUrlResolutionService'>, <type 'IComponent'>, <type 'IDataBindingsAccessor'>, <type 'IControlBuilderAccessor'>, <type 'IParserAccessor'>, <type 'IExpressionsAccessor'>, <type 'IControlDesignerAccessor'>, <type 'object'>
    """ UpdateProgress() """
    @property
    def AssociatedUpdatePanelID(self) -> str:
        """
        Get: AssociatedUpdatePanelID(self: UpdateProgress) -> str
        Set: AssociatedUpdatePanelID(self: UpdateProgress) = value
        """
        ...

    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: UpdateProgress) -> AttributeCollection """
        ...

    @property
    def DisplayAfter(self) -> int:
        """
        Get: DisplayAfter(self: UpdateProgress) -> int
        Set: DisplayAfter(self: UpdateProgress) = value
        """
        ...

    @property
    def DynamicLayout(self) -> bool:
        """
        Get: DynamicLayout(self: UpdateProgress) -> bool
        Set: DynamicLayout(self: UpdateProgress) = value
        """
        ...

    @property
    def ProgressTemplate(self) -> ITemplate:
        """
        Get: ProgressTemplate(self: UpdateProgress) -> ITemplate
        Set: ProgressTemplate(self: UpdateProgress) = value
        """
        ...



class UrlPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    UrlPropertyAttribute()
    UrlPropertyAttribute(filter: str)
    """
    @property
    def Filter(self) -> str:
        """ Get: Filter(self: UrlPropertyAttribute) -> str """
        ...


    def __new__(cls, filter:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, filter: str)
        """
        ...


class ValidateRequestMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidateRequestMode, values: Disabled (1), Enabled (2), Inherit (0) """
    Disabled: ValidateRequestMode = ...
    Enabled: ValidateRequestMode = ...
    Inherit: ValidateRequestMode = ...
    value__ = ...


class ValidationPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ValidationPropertyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ValidationPropertyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ValidationSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def UnobtrusiveValidationMode(self) -> UnobtrusiveValidationMode:
        """
        Get: UnobtrusiveValidationMode() -> UnobtrusiveValidationMode
        Set: UnobtrusiveValidationMode() = value
        """
        ...


    __all__: list = ...


class ValidatorCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ValidatorCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ValidatorCollection) -> bool """
        ...


    def Add(self, validator:IValidator): # -> 
        """ Add(self: ValidatorCollection, validator: IValidator) """
        ...

    def Contains(self, validator:IValidator) -> bool:
        """ Contains(self: ValidatorCollection, validator: IValidator) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ValidatorCollection) -> IEnumerator """
        ...

    def Remove(self, validator:IValidator): # -> 
        """ Remove(self: ValidatorCollection, validator: IValidator) """
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


class VerificationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    VerificationAttribute(guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str)
    VerificationAttribute(guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str, rule: VerificationRule, conditionalProperty: str)
    VerificationAttribute(guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str, rule: VerificationRule, conditionalProperty: str, conditionalOperator: VerificationConditionalOperator, conditionalValue: str, guidelineUrl: str)
    """
    @property
    def Checkpoint(self) -> str:
        """ Get: Checkpoint(self: VerificationAttribute) -> str """
        ...

    @property
    def ConditionalProperty(self) -> str:
        """ Get: ConditionalProperty(self: VerificationAttribute) -> str """
        ...

    @property
    def ConditionalValue(self) -> str:
        """ Get: ConditionalValue(self: VerificationAttribute) -> str """
        ...

    @property
    def Guideline(self) -> str:
        """ Get: Guideline(self: VerificationAttribute) -> str """
        ...

    @property
    def GuidelineUrl(self) -> str:
        """ Get: GuidelineUrl(self: VerificationAttribute) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: VerificationAttribute) -> str """
        ...

    @property
    def Priority(self) -> int:
        """ Get: Priority(self: VerificationAttribute) -> int """
        ...

    @property
    def VerificationConditionalOperator(self): # -> VerificationConditionalOperator
        """ Get: VerificationConditionalOperator(self: VerificationAttribute) -> VerificationConditionalOperator """
        ...

    @property
    def VerificationReportLevel(self): # -> VerificationReportLevel
        """ Get: VerificationReportLevel(self: VerificationAttribute) -> VerificationReportLevel """
        ...

    @property
    def VerificationRule(self): # -> VerificationRule
        """ Get: VerificationRule(self: VerificationAttribute) -> VerificationRule """
        ...


    def __new__(cls, guideline:str, checkpoint:str, reportLevel, priority:int, message:str, rule = ..., conditionalProperty:str = ..., conditionalOperator = ..., conditionalValue:str = ..., guidelineUrl:str = ...) -> Self: # Not found arg types: {'conditionalOperator': 'VerificationConditionalOperator', 'reportLevel': 'VerificationReportLevel', 'rule': 'VerificationRule'}
        """
        __new__(cls: type, guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str)
        __new__(cls: type, guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str, rule: VerificationRule, conditionalProperty: str)
        __new__(cls: type, guideline: str, checkpoint: str, reportLevel: VerificationReportLevel, priority: int, message: str, rule: VerificationRule, conditionalProperty: str, conditionalOperator: VerificationConditionalOperator, conditionalValue: str, guidelineUrl: str)
        """
        ...


class VerificationConditionalOperator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VerificationConditionalOperator, values: Equals (0), NotEquals (1) """
    Equals: VerificationConditionalOperator = ...
    NotEquals: VerificationConditionalOperator = ...
    value__ = ...


class VerificationReportLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VerificationReportLevel, values: Error (0), Guideline (2), Warning (1) """
    Error: VerificationReportLevel = ...
    Guideline: VerificationReportLevel = ...
    value__ = ...
    Warning: VerificationReportLevel = ...


class VerificationRule(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VerificationRule, values: NotEmptyString (2), Prohibited (1), Required (0) """
    NotEmptyString: VerificationRule = ...
    Prohibited: VerificationRule = ...
    Required: VerificationRule = ...
    value__ = ...


class ViewStateEncryptionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ViewStateEncryptionMode, values: Always (1), Auto (0), Never (2) """
    Always: ViewStateEncryptionMode = ...
    Auto: ViewStateEncryptionMode = ...
    Never: ViewStateEncryptionMode = ...
    value__ = ...


class ViewStateException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ ViewStateException() """
    @property
    def IsConnected(self) -> bool:
        """ Get: IsConnected(self: ViewStateException) -> bool """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ViewStateException) -> str """
        ...

    @property
    def PersistedState(self) -> str:
        """ Get: PersistedState(self: ViewStateException) -> str """
        ...

    @property
    def Referer(self) -> str:
        """ Get: Referer(self: ViewStateException) -> str """
        ...

    @property
    def RemoteAddress(self) -> str:
        """ Get: RemoteAddress(self: ViewStateException) -> str """
        ...

    @property
    def RemotePort(self) -> str:
        """ Get: RemotePort(self: ViewStateException) -> str """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: ViewStateException) -> str """
        ...


    SerializeObjectState = ...


class ViewStateMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ViewStateMode, values: Disabled (2), Enabled (1), Inherit (0) """
    Disabled: ViewStateMode = ...
    Enabled: ViewStateMode = ...
    Inherit: ViewStateMode = ...
    value__ = ...


class ViewStateModeByIdAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ViewStateModeByIdAttribute() """
    pass

class VirtualReferenceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VirtualReferenceType, values: Master (2), Other (4), Page (0), SourceFile (3), UserControl (1) """
    Master: VirtualReferenceType = ...
    Other: VirtualReferenceType = ...
    Page: VirtualReferenceType = ...
    SourceFile: VirtualReferenceType = ...
    UserControl: VirtualReferenceType = ...
    value__ = ...


class WebResourceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebResourceAttribute(webResource: str, contentType: str) """
    @property
    def CdnPath(self) -> str:
        """
        Get: CdnPath(self: WebResourceAttribute) -> str
        Set: CdnPath(self: WebResourceAttribute) = value
        """
        ...

    @property
    def CdnSupportsSecureConnection(self) -> bool:
        """
        Get: CdnSupportsSecureConnection(self: WebResourceAttribute) -> bool
        Set: CdnSupportsSecureConnection(self: WebResourceAttribute) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: WebResourceAttribute) -> str """
        ...

    @property
    def LoadSuccessExpression(self) -> str:
        """
        Get: LoadSuccessExpression(self: WebResourceAttribute) -> str
        Set: LoadSuccessExpression(self: WebResourceAttribute) = value
        """
        ...

    @property
    def PerformSubstitution(self) -> bool:
        """
        Get: PerformSubstitution(self: WebResourceAttribute) -> bool
        Set: PerformSubstitution(self: WebResourceAttribute) = value
        """
        ...

    @property
    def WebResource(self) -> str:
        """ Get: WebResource(self: WebResourceAttribute) -> str """
        ...


    def __new__(cls, webResource:str, contentType:str) -> Self:
        """ __new__(cls: type, webResource: str, contentType: str) """
        ...


class WebServiceParser(SimpleWebHandlerParser): # skipped bases: <type 'IAssemblyDependencyParser'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetCompiledType(inputFile:str, context) -> Type: # Not found arg types: {'context': 'HttpContext'}
        """ GetCompiledType(inputFile: str, context: HttpContext) -> Type """
        ...


class XhtmlMobileDocType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XhtmlMobileDocType, values: Wml20 (2), XhtmlBasic (0), XhtmlMobileProfile (1) """
    value__ = ...
    Wml20: XhtmlMobileDocType = ...
    XhtmlBasic: XhtmlMobileDocType = ...
    XhtmlMobileProfile: XhtmlMobileDocType = ...


class XhtmlTextWriter(HtmlTextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XhtmlTextWriter(writer: TextWriter)
    XhtmlTextWriter(writer: TextWriter, tabString: str)
    """
    @property
    def CommonAttributes(self):
        ...

    @property
    def ElementSpecificAttributes(self):
        ...

    @property
    def SuppressCommonAttributes(self):
        ...


    def AddRecognizedAttribute(self, elementName:str, attributeName:str): # -> 
        """ AddRecognizedAttribute(self: XhtmlTextWriter, elementName: str, attributeName: str) """
        ...

    def RemoveRecognizedAttribute(self, elementName:str, attributeName:str): # -> 
        """ RemoveRecognizedAttribute(self: XhtmlTextWriter, elementName: str, attributeName: str) """
        ...

    def SetDocType(self, docType:XhtmlMobileDocType): # -> 
        """ SetDocType(self: XhtmlTextWriter, docType: XhtmlMobileDocType) """
        ...

    CoreNewLine = ...


class XPathBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Eval(container:object, xPath:str, *__args:str) -> str:
        """
        Eval(container: object, xPath: str) -> object
        Eval(container: object, xPath: str, format: str) -> str
        Eval(container: object, xPath: str, format: str, resolver: IXmlNamespaceResolver) -> str
        Eval(container: object, xPath: str, resolver: IXmlNamespaceResolver) -> object
        """
        ...

    @staticmethod
    def Select(container:object, xPath:str, resolver:IXmlNamespaceResolver = ...) -> IEnumerable:
        """
        Select(container: object, xPath: str) -> IEnumerable
        Select(container: object, xPath: str, resolver: IXmlNamespaceResolver) -> IEnumerable
        """
        ...


# variables with complex values

