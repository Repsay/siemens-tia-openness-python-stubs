# encoding: utf-8
# module Microsoft.Office.Interop.OneNote calls itself OneNote
# from Microsoft.Office.Interop.OneNote, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime, Enum, MulticastDelegate, UInt32, UInt64

from System.Collections import IEnumerable

"""The following names are not found in the module: (Application2ClassCOM, 
    ApplicationClassCOM, BoundEvent, field#)
"""

# no functions
# classes

class IApplication: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def COMAddIns(self) -> object:
        """ Get: COMAddIns(self: IApplication) -> object """
        ...

    @property
    def Dummy1(self) -> bool:
        """ Get: Dummy1(self: IApplication) -> bool """
        ...

    @property
    def LanguageSettings(self) -> object:
        """ Get: LanguageSettings(self: IApplication) -> object """
        ...

    @property
    def Windows(self) -> Windows:
        """ Get: Windows(self: IApplication) -> Windows """
        ...


    def CloseNotebook(self, bstrNotebookID:str, force:bool = ...): # -> 
        """ CloseNotebook(self: IApplication, bstrNotebookID: str, force: bool)CloseNotebook(self: IApplication, bstrNotebookID: str) """
        ...

    def CreateNewPage(self, bstrSectionID, pbstrPageID, npsNewPageStyle=None) -> str:
        """
        CreateNewPage(self: IApplication, bstrSectionID: str, npsNewPageStyle: NewPageStyle) -> str
        CreateNewPage(self: IApplication, bstrSectionID: str) -> str
        """
        ...

    def DeleteHierarchy(self, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., deletePermanently:bool = ...): # -> 
        """ DeleteHierarchy(self: IApplication, bstrObjectID: str, dateExpectedLastModified: DateTime, deletePermanently: bool)DeleteHierarchy(self: IApplication, bstrObjectID: str, dateExpectedLastModified: DateTime)DeleteHierarchy(self: IApplication, bstrObjectID: str) """
        ...

    def DeletePageContent(self, bstrPageID:str, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., force:bool = ...): # -> 
        """ DeletePageContent(self: IApplication, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime, force: bool)DeletePageContent(self: IApplication, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime)DeletePageContent(self: IApplication, bstrPageID: str, bstrObjectID: str) """
        ...

    def FindMeta(self, bstrStartNodeID, bstrSearchStringName, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, xsSchema=None) -> str:
        """
        FindMeta(self: IApplication, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool, xsSchema: XMLSchema) -> str
        FindMeta(self: IApplication, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool) -> str
        FindMeta(self: IApplication, bstrStartNodeID: str, bstrSearchStringName: str) -> str
        """
        ...

    def FindPages(self, bstrStartNodeID, bstrSearchString, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, fDisplay=None, xsSchema=None) -> str:
        """
        FindPages(self: IApplication, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool, xsSchema: XMLSchema) -> str
        FindPages(self: IApplication, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool) -> str
        FindPages(self: IApplication, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool) -> str
        FindPages(self: IApplication, bstrStartNodeID: str, bstrSearchString: str) -> str
        """
        ...

    def GetBinaryPageContent(self, bstrPageID, bstrCallbackID, pbstrBinaryObjectB64Out) -> str:
        """ GetBinaryPageContent(self: IApplication, bstrPageID: str, bstrCallbackID: str) -> str """
        ...

    def GetHierarchy(self, bstrStartNodeID, hsScope, pbstrHierarchyXmlOut, xsSchema=None) -> str:
        """
        GetHierarchy(self: IApplication, bstrStartNodeID: str, hsScope: HierarchyScope, xsSchema: XMLSchema) -> str
        GetHierarchy(self: IApplication, bstrStartNodeID: str, hsScope: HierarchyScope) -> str
        """
        ...

    def GetHierarchyParent(self, bstrObjectID, pbstrParentID) -> str:
        """ GetHierarchyParent(self: IApplication, bstrObjectID: str) -> str """
        ...

    def GetHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetHyperlinkToObject(self: IApplication, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def GetPageContent(self, bstrPageID, pbstrPageXmlOut, pageInfoToExport=None, xsSchema=None) -> str:
        """
        GetPageContent(self: IApplication, bstrPageID: str, pageInfoToExport: PageInfo, xsSchema: XMLSchema) -> str
        GetPageContent(self: IApplication, bstrPageID: str, pageInfoToExport: PageInfo) -> str
        GetPageContent(self: IApplication, bstrPageID: str) -> str
        """
        ...

    def GetSpecialLocation(self, slToGet, pbstrSpecialLocationPath) -> str:
        """ GetSpecialLocation(self: IApplication, slToGet: SpecialLocation) -> str """
        ...

    def GetWebHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetWebHyperlinkToObject(self: IApplication, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def MergeFiles(self, bstrBaseFile:str, bstrClientFile:str, bstrServerFile:str, bstrTargetFile:str): # -> 
        """ MergeFiles(self: IApplication, bstrBaseFile: str, bstrClientFile: str, bstrServerFile: str, bstrTargetFile: str) """
        ...

    def MergeSections(self, bstrSectionSourceId:str, bstrSectionDestinationId:str): # -> 
        """ MergeSections(self: IApplication, bstrSectionSourceId: str, bstrSectionDestinationId: str) """
        ...

    def NavigateTo(self, bstrHierarchyObjectID:str, bstrObjectID:str = ..., fNewWindow:bool = ...): # -> 
        """ NavigateTo(self: IApplication, bstrHierarchyObjectID: str, bstrObjectID: str, fNewWindow: bool)NavigateTo(self: IApplication, bstrHierarchyObjectID: str, bstrObjectID: str)NavigateTo(self: IApplication, bstrHierarchyObjectID: str) """
        ...

    def NavigateToUrl(self, bstrUrl:str, fNewWindow:bool = ...): # -> 
        """ NavigateToUrl(self: IApplication, bstrUrl: str, fNewWindow: bool)NavigateToUrl(self: IApplication, bstrUrl: str) """
        ...

    def OpenHierarchy(self, bstrPath, bstrRelativeToObjectID, pbstrObjectID, cftIfNotExist=None) -> str:
        """
        OpenHierarchy(self: IApplication, bstrPath: str, bstrRelativeToObjectID: str, cftIfNotExist: CreateFileType) -> str
        OpenHierarchy(self: IApplication, bstrPath: str, bstrRelativeToObjectID: str) -> str
        """
        ...

    def OpenPackage(self, bstrPathPackage, bstrPathDest, pbstrPathOut) -> str:
        """ OpenPackage(self: IApplication, bstrPathPackage: str, bstrPathDest: str) -> str """
        ...

    def Publish(self, bstrHierarchyID:str, bstrTargetFilePath:str, pfPublishFormat:PublishFormat = ..., bstrCLSIDofExporter:str = ...): # -> 
        """ Publish(self: IApplication, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat, bstrCLSIDofExporter: str)Publish(self: IApplication, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat)Publish(self: IApplication, bstrHierarchyID: str, bstrTargetFilePath: str) """
        ...

    def QuickFiling(self) -> IQuickFilingDialog:
        """ QuickFiling(self: IApplication) -> IQuickFilingDialog """
        ...

    def SetFilingLocation(self, flToSet:FilingLocation, fltToSet:FilingLocationType, bstrFilingSectionID:str): # -> 
        """ SetFilingLocation(self: IApplication, flToSet: FilingLocation, fltToSet: FilingLocationType, bstrFilingSectionID: str) """
        ...

    def SyncHierarchy(self, bstrHierarchyID:str): # -> 
        """ SyncHierarchy(self: IApplication, bstrHierarchyID: str) """
        ...

    def UpdateHierarchy(self, bstrChangesXmlIn:str, xsSchema:XMLSchema = ...): # -> 
        """ UpdateHierarchy(self: IApplication, bstrChangesXmlIn: str, xsSchema: XMLSchema)UpdateHierarchy(self: IApplication, bstrChangesXmlIn: str) """
        ...

    def UpdatePageContent(self, bstrPageChangesXmlIn:str, dateExpectedLastModified:DateTime = ..., xsSchema:XMLSchema = ..., force:bool = ...): # -> 
        """ UpdatePageContent(self: IApplication, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema, force: bool)UpdatePageContent(self: IApplication, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema)UpdatePageContent(self: IApplication, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime)UpdatePageContent(self: IApplication, bstrPageChangesXmlIn: str) """
        ...


class IOneNoteEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_OnHierarchyChange(self, A_1:IOneNoteEvents_OnHierarchyChangeEventHandler): # -> 
        """ add_OnHierarchyChange(self: IOneNoteEvents_Event, A_1: IOneNoteEvents_OnHierarchyChangeEventHandler) """
        ...

    def add_OnNavigate(self, A_1:IOneNoteEvents_OnNavigateEventHandler): # -> 
        """ add_OnNavigate(self: IOneNoteEvents_Event, A_1: IOneNoteEvents_OnNavigateEventHandler) """
        ...

    def remove_OnHierarchyChange(self, A_1:IOneNoteEvents_OnHierarchyChangeEventHandler): # -> 
        """ remove_OnHierarchyChange(self: IOneNoteEvents_Event, A_1: IOneNoteEvents_OnHierarchyChangeEventHandler) """
        ...

    def remove_OnNavigate(self, A_1:IOneNoteEvents_OnNavigateEventHandler): # -> 
        """ remove_OnNavigate(self: IOneNoteEvents_Event, A_1: IOneNoteEvents_OnNavigateEventHandler) """
        ...

    OnHierarchyChange = ...
    OnNavigate = ...


class Application(IOneNoteEvents_Event, IApplication): # skipped bases: <type 'object'>
    """ no doc """
    pass

class Application2(IOneNoteEvents_Event, IApplication): # skipped bases: <type 'object'>
    """ no doc """
    pass

class Application2Class(Application2, Application2ClassCOM): # skipped bases: <type 'IApplicationCOM'>, <type 'IApplication'>, <type 'IOneNoteEvents_Event'>, <type 'object'>
    """ Application2Class() """
    @property
    def COMAddIns(self) -> object:
        """ Get: COMAddIns(self: Application2Class) -> object """
        ...

    @property
    def Dummy1(self) -> bool:
        """ Get: Dummy1(self: Application2Class) -> bool """
        ...

    @property
    def LanguageSettings(self) -> object:
        """ Get: LanguageSettings(self: Application2Class) -> object """
        ...

    @property
    def Windows(self) -> Windows:
        """ Get: Windows(self: Application2Class) -> Windows """
        ...


    def CloseNotebook(self, bstrNotebookID:str, force:bool = ...): # -> 
        """ CloseNotebook(self: Application2Class, bstrNotebookID: str, force: bool)CloseNotebook(self: Application2Class, bstrNotebookID: str) """
        ...

    def CreateNewPage(self, bstrSectionID, pbstrPageID, npsNewPageStyle=None) -> str:
        """
        CreateNewPage(self: Application2Class, bstrSectionID: str, npsNewPageStyle: NewPageStyle) -> str
        CreateNewPage(self: Application2Class, bstrSectionID: str) -> str
        """
        ...

    def DeleteHierarchy(self, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., deletePermanently:bool = ...): # -> 
        """ DeleteHierarchy(self: Application2Class, bstrObjectID: str, dateExpectedLastModified: DateTime, deletePermanently: bool)DeleteHierarchy(self: Application2Class, bstrObjectID: str, dateExpectedLastModified: DateTime)DeleteHierarchy(self: Application2Class, bstrObjectID: str) """
        ...

    def DeletePageContent(self, bstrPageID:str, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., force:bool = ...): # -> 
        """ DeletePageContent(self: Application2Class, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime, force: bool)DeletePageContent(self: Application2Class, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime)DeletePageContent(self: Application2Class, bstrPageID: str, bstrObjectID: str) """
        ...

    def FindMeta(self, bstrStartNodeID, bstrSearchStringName, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, xsSchema=None) -> str:
        """
        FindMeta(self: Application2Class, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool, xsSchema: XMLSchema) -> str
        FindMeta(self: Application2Class, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool) -> str
        FindMeta(self: Application2Class, bstrStartNodeID: str, bstrSearchStringName: str) -> str
        """
        ...

    def FindPages(self, bstrStartNodeID, bstrSearchString, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, fDisplay=None, xsSchema=None) -> str:
        """
        FindPages(self: Application2Class, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool, xsSchema: XMLSchema) -> str
        FindPages(self: Application2Class, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool) -> str
        FindPages(self: Application2Class, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool) -> str
        FindPages(self: Application2Class, bstrStartNodeID: str, bstrSearchString: str) -> str
        """
        ...

    def GetBinaryPageContent(self, bstrPageID, bstrCallbackID, pbstrBinaryObjectB64Out) -> str:
        """ GetBinaryPageContent(self: Application2Class, bstrPageID: str, bstrCallbackID: str) -> str """
        ...

    def GetHierarchy(self, bstrStartNodeID, hsScope, pbstrHierarchyXmlOut, xsSchema=None) -> str:
        """
        GetHierarchy(self: Application2Class, bstrStartNodeID: str, hsScope: HierarchyScope, xsSchema: XMLSchema) -> str
        GetHierarchy(self: Application2Class, bstrStartNodeID: str, hsScope: HierarchyScope) -> str
        """
        ...

    def GetHierarchyParent(self, bstrObjectID, pbstrParentID) -> str:
        """ GetHierarchyParent(self: Application2Class, bstrObjectID: str) -> str """
        ...

    def GetHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetHyperlinkToObject(self: Application2Class, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def GetPageContent(self, bstrPageID, pbstrPageXmlOut, pageInfoToExport=None, xsSchema=None) -> str:
        """
        GetPageContent(self: Application2Class, bstrPageID: str, pageInfoToExport: PageInfo, xsSchema: XMLSchema) -> str
        GetPageContent(self: Application2Class, bstrPageID: str, pageInfoToExport: PageInfo) -> str
        GetPageContent(self: Application2Class, bstrPageID: str) -> str
        """
        ...

    def GetSpecialLocation(self, slToGet, pbstrSpecialLocationPath) -> str:
        """ GetSpecialLocation(self: Application2Class, slToGet: SpecialLocation) -> str """
        ...

    def GetWebHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetWebHyperlinkToObject(self: Application2Class, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def MergeFiles(self, bstrBaseFile:str, bstrClientFile:str, bstrServerFile:str, bstrTargetFile:str): # -> 
        """ MergeFiles(self: Application2Class, bstrBaseFile: str, bstrClientFile: str, bstrServerFile: str, bstrTargetFile: str) """
        ...

    def MergeSections(self, bstrSectionSourceId:str, bstrSectionDestinationId:str): # -> 
        """ MergeSections(self: Application2Class, bstrSectionSourceId: str, bstrSectionDestinationId: str) """
        ...

    def NavigateTo(self, bstrHierarchyObjectID:str, bstrObjectID:str = ..., fNewWindow:bool = ...): # -> 
        """ NavigateTo(self: Application2Class, bstrHierarchyObjectID: str, bstrObjectID: str, fNewWindow: bool)NavigateTo(self: Application2Class, bstrHierarchyObjectID: str, bstrObjectID: str)NavigateTo(self: Application2Class, bstrHierarchyObjectID: str) """
        ...

    def NavigateToUrl(self, bstrUrl:str, fNewWindow:bool = ...): # -> 
        """ NavigateToUrl(self: Application2Class, bstrUrl: str, fNewWindow: bool)NavigateToUrl(self: Application2Class, bstrUrl: str) """
        ...

    def OpenHierarchy(self, bstrPath, bstrRelativeToObjectID, pbstrObjectID, cftIfNotExist=None) -> str:
        """
        OpenHierarchy(self: Application2Class, bstrPath: str, bstrRelativeToObjectID: str, cftIfNotExist: CreateFileType) -> str
        OpenHierarchy(self: Application2Class, bstrPath: str, bstrRelativeToObjectID: str) -> str
        """
        ...

    def OpenPackage(self, bstrPathPackage, bstrPathDest, pbstrPathOut) -> str:
        """ OpenPackage(self: Application2Class, bstrPathPackage: str, bstrPathDest: str) -> str """
        ...

    def Publish(self, bstrHierarchyID:str, bstrTargetFilePath:str, pfPublishFormat:PublishFormat = ..., bstrCLSIDofExporter:str = ...): # -> 
        """ Publish(self: Application2Class, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat, bstrCLSIDofExporter: str)Publish(self: Application2Class, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat)Publish(self: Application2Class, bstrHierarchyID: str, bstrTargetFilePath: str) """
        ...

    def QuickFiling(self) -> IQuickFilingDialog:
        """ QuickFiling(self: Application2Class) -> IQuickFilingDialog """
        ...

    def SetFilingLocation(self, flToSet:FilingLocation, fltToSet:FilingLocationType, bstrFilingSectionID:str): # -> 
        """ SetFilingLocation(self: Application2Class, flToSet: FilingLocation, fltToSet: FilingLocationType, bstrFilingSectionID: str) """
        ...

    def SyncHierarchy(self, bstrHierarchyID:str): # -> 
        """ SyncHierarchy(self: Application2Class, bstrHierarchyID: str) """
        ...

    def UpdateHierarchy(self, bstrChangesXmlIn:str, xsSchema:XMLSchema = ...): # -> 
        """ UpdateHierarchy(self: Application2Class, bstrChangesXmlIn: str, xsSchema: XMLSchema)UpdateHierarchy(self: Application2Class, bstrChangesXmlIn: str) """
        ...

    def UpdatePageContent(self, bstrPageChangesXmlIn:str, dateExpectedLastModified:DateTime = ..., xsSchema:XMLSchema = ..., force:bool = ...): # -> 
        """ UpdatePageContent(self: Application2Class, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema, force: bool)UpdatePageContent(self: Application2Class, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema)UpdatePageContent(self: Application2Class, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime)UpdatePageContent(self: Application2Class, bstrPageChangesXmlIn: str) """
        ...

    OnHierarchyChange = ...
    OnNavigate = ...


class ApplicationClass(Application, ApplicationClassCOM): # skipped bases: <type 'IApplicationCOM'>, <type 'IApplication'>, <type 'IOneNoteEvents_Event'>, <type 'object'>
    """ ApplicationClass() """
    @property
    def COMAddIns(self) -> object:
        """ Get: COMAddIns(self: ApplicationClass) -> object """
        ...

    @property
    def Dummy1(self) -> bool:
        """ Get: Dummy1(self: ApplicationClass) -> bool """
        ...

    @property
    def LanguageSettings(self) -> object:
        """ Get: LanguageSettings(self: ApplicationClass) -> object """
        ...

    @property
    def Windows(self) -> Windows:
        """ Get: Windows(self: ApplicationClass) -> Windows """
        ...


    def CloseNotebook(self, bstrNotebookID:str, force:bool = ...): # -> 
        """ CloseNotebook(self: ApplicationClass, bstrNotebookID: str, force: bool)CloseNotebook(self: ApplicationClass, bstrNotebookID: str) """
        ...

    def CreateNewPage(self, bstrSectionID, pbstrPageID, npsNewPageStyle=None) -> str:
        """
        CreateNewPage(self: ApplicationClass, bstrSectionID: str, npsNewPageStyle: NewPageStyle) -> str
        CreateNewPage(self: ApplicationClass, bstrSectionID: str) -> str
        """
        ...

    def DeleteHierarchy(self, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., deletePermanently:bool = ...): # -> 
        """ DeleteHierarchy(self: ApplicationClass, bstrObjectID: str, dateExpectedLastModified: DateTime, deletePermanently: bool)DeleteHierarchy(self: ApplicationClass, bstrObjectID: str, dateExpectedLastModified: DateTime)DeleteHierarchy(self: ApplicationClass, bstrObjectID: str) """
        ...

    def DeletePageContent(self, bstrPageID:str, bstrObjectID:str, dateExpectedLastModified:DateTime = ..., force:bool = ...): # -> 
        """ DeletePageContent(self: ApplicationClass, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime, force: bool)DeletePageContent(self: ApplicationClass, bstrPageID: str, bstrObjectID: str, dateExpectedLastModified: DateTime)DeletePageContent(self: ApplicationClass, bstrPageID: str, bstrObjectID: str) """
        ...

    def FindMeta(self, bstrStartNodeID, bstrSearchStringName, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, xsSchema=None) -> str:
        """
        FindMeta(self: ApplicationClass, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool, xsSchema: XMLSchema) -> str
        FindMeta(self: ApplicationClass, bstrStartNodeID: str, bstrSearchStringName: str, fIncludeUnindexedPages: bool) -> str
        FindMeta(self: ApplicationClass, bstrStartNodeID: str, bstrSearchStringName: str) -> str
        """
        ...

    def FindPages(self, bstrStartNodeID, bstrSearchString, pbstrHierarchyXmlOut, fIncludeUnindexedPages=None, fDisplay=None, xsSchema=None) -> str:
        """
        FindPages(self: ApplicationClass, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool, xsSchema: XMLSchema) -> str
        FindPages(self: ApplicationClass, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool, fDisplay: bool) -> str
        FindPages(self: ApplicationClass, bstrStartNodeID: str, bstrSearchString: str, fIncludeUnindexedPages: bool) -> str
        FindPages(self: ApplicationClass, bstrStartNodeID: str, bstrSearchString: str) -> str
        """
        ...

    def GetBinaryPageContent(self, bstrPageID, bstrCallbackID, pbstrBinaryObjectB64Out) -> str:
        """ GetBinaryPageContent(self: ApplicationClass, bstrPageID: str, bstrCallbackID: str) -> str """
        ...

    def GetHierarchy(self, bstrStartNodeID, hsScope, pbstrHierarchyXmlOut, xsSchema=None) -> str:
        """
        GetHierarchy(self: ApplicationClass, bstrStartNodeID: str, hsScope: HierarchyScope, xsSchema: XMLSchema) -> str
        GetHierarchy(self: ApplicationClass, bstrStartNodeID: str, hsScope: HierarchyScope) -> str
        """
        ...

    def GetHierarchyParent(self, bstrObjectID, pbstrParentID) -> str:
        """ GetHierarchyParent(self: ApplicationClass, bstrObjectID: str) -> str """
        ...

    def GetHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetHyperlinkToObject(self: ApplicationClass, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def GetPageContent(self, bstrPageID, pbstrPageXmlOut, pageInfoToExport=None, xsSchema=None) -> str:
        """
        GetPageContent(self: ApplicationClass, bstrPageID: str, pageInfoToExport: PageInfo, xsSchema: XMLSchema) -> str
        GetPageContent(self: ApplicationClass, bstrPageID: str, pageInfoToExport: PageInfo) -> str
        GetPageContent(self: ApplicationClass, bstrPageID: str) -> str
        """
        ...

    def GetSpecialLocation(self, slToGet, pbstrSpecialLocationPath) -> str:
        """ GetSpecialLocation(self: ApplicationClass, slToGet: SpecialLocation) -> str """
        ...

    def GetWebHyperlinkToObject(self, bstrHierarchyID, bstrPageContentObjectID, pbstrHyperlinkOut) -> str:
        """ GetWebHyperlinkToObject(self: ApplicationClass, bstrHierarchyID: str, bstrPageContentObjectID: str) -> str """
        ...

    def MergeFiles(self, bstrBaseFile:str, bstrClientFile:str, bstrServerFile:str, bstrTargetFile:str): # -> 
        """ MergeFiles(self: ApplicationClass, bstrBaseFile: str, bstrClientFile: str, bstrServerFile: str, bstrTargetFile: str) """
        ...

    def MergeSections(self, bstrSectionSourceId:str, bstrSectionDestinationId:str): # -> 
        """ MergeSections(self: ApplicationClass, bstrSectionSourceId: str, bstrSectionDestinationId: str) """
        ...

    def NavigateTo(self, bstrHierarchyObjectID:str, bstrObjectID:str = ..., fNewWindow:bool = ...): # -> 
        """ NavigateTo(self: ApplicationClass, bstrHierarchyObjectID: str, bstrObjectID: str, fNewWindow: bool)NavigateTo(self: ApplicationClass, bstrHierarchyObjectID: str, bstrObjectID: str)NavigateTo(self: ApplicationClass, bstrHierarchyObjectID: str) """
        ...

    def NavigateToUrl(self, bstrUrl:str, fNewWindow:bool = ...): # -> 
        """ NavigateToUrl(self: ApplicationClass, bstrUrl: str, fNewWindow: bool)NavigateToUrl(self: ApplicationClass, bstrUrl: str) """
        ...

    def OpenHierarchy(self, bstrPath, bstrRelativeToObjectID, pbstrObjectID, cftIfNotExist=None) -> str:
        """
        OpenHierarchy(self: ApplicationClass, bstrPath: str, bstrRelativeToObjectID: str, cftIfNotExist: CreateFileType) -> str
        OpenHierarchy(self: ApplicationClass, bstrPath: str, bstrRelativeToObjectID: str) -> str
        """
        ...

    def OpenPackage(self, bstrPathPackage, bstrPathDest, pbstrPathOut) -> str:
        """ OpenPackage(self: ApplicationClass, bstrPathPackage: str, bstrPathDest: str) -> str """
        ...

    def Publish(self, bstrHierarchyID:str, bstrTargetFilePath:str, pfPublishFormat:PublishFormat = ..., bstrCLSIDofExporter:str = ...): # -> 
        """ Publish(self: ApplicationClass, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat, bstrCLSIDofExporter: str)Publish(self: ApplicationClass, bstrHierarchyID: str, bstrTargetFilePath: str, pfPublishFormat: PublishFormat)Publish(self: ApplicationClass, bstrHierarchyID: str, bstrTargetFilePath: str) """
        ...

    def QuickFiling(self) -> IQuickFilingDialog:
        """ QuickFiling(self: ApplicationClass) -> IQuickFilingDialog """
        ...

    def SetFilingLocation(self, flToSet:FilingLocation, fltToSet:FilingLocationType, bstrFilingSectionID:str): # -> 
        """ SetFilingLocation(self: ApplicationClass, flToSet: FilingLocation, fltToSet: FilingLocationType, bstrFilingSectionID: str) """
        ...

    def SyncHierarchy(self, bstrHierarchyID:str): # -> 
        """ SyncHierarchy(self: ApplicationClass, bstrHierarchyID: str) """
        ...

    def UpdateHierarchy(self, bstrChangesXmlIn:str, xsSchema:XMLSchema = ...): # -> 
        """ UpdateHierarchy(self: ApplicationClass, bstrChangesXmlIn: str, xsSchema: XMLSchema)UpdateHierarchy(self: ApplicationClass, bstrChangesXmlIn: str) """
        ...

    def UpdatePageContent(self, bstrPageChangesXmlIn:str, dateExpectedLastModified:DateTime = ..., xsSchema:XMLSchema = ..., force:bool = ...): # -> 
        """ UpdatePageContent(self: ApplicationClass, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema, force: bool)UpdatePageContent(self: ApplicationClass, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime, xsSchema: XMLSchema)UpdatePageContent(self: ApplicationClass, bstrPageChangesXmlIn: str, dateExpectedLastModified: DateTime)UpdatePageContent(self: ApplicationClass, bstrPageChangesXmlIn: str) """
        ...

    OnHierarchyChange = ...
    OnNavigate = ...


class CreateFileType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CreateFileType, values: cftFolder (2), cftNone (0), cftNotebook (1), cftSection (3) """
    cftFolder: CreateFileType = ...
    cftNone: CreateFileType = ...
    cftNotebook: CreateFileType = ...
    cftSection: CreateFileType = ...
    value__ = ...


class DockLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DockLocation, values: dlBottom (4), dlDefault (-1), dlLeft (1), dlNone (0), dlRight (2), dlTop (3) """
    dlBottom: DockLocation = ...
    dlDefault: DockLocation = ...
    dlLeft: DockLocation = ...
    dlNone: DockLocation = ...
    dlRight: DockLocation = ...
    dlTop: DockLocation = ...
    value__ = ...


class Error(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Error, values: hrAppInModalUI (-2147213264), hrBinaryObjectDoesNotExist (-2147213297), hrConvertFailed (-2147213267), hrCreatingSection (-2147213310), hrDisabledByPolicy (-2147213284), hrFileAlreadyExists (-2147213286), hrFileDoesNotExist (-2147213306), hrFolderDoesNotExist (-2147213288), hrFutureContentLoss (-2147213278), hrGroupDoesNotExist (-2147213295), hrImportLNTThumbnailFailed (-2147213270), hrInsertingFile (-2147213290), hrInsertingHtml (-2147213303), hrInsertingImage (-2147213305), hrInsertingInk (-2147213304), hrInsertingOutlineText (-2147213299), hrInvalidLinkedNoteThumbnail (-2147213271), hrInvalidLinkedNoteUri (-2147213272), hrInvalidName (-2147213289), hrInvalidQuery (-2147213287), hrInvalidSelection (-2147213268), hrInvalidXML (-2147213311), hrInvalidXMLSchema (-2147213280), hrLastModifiedDateDidNotMatch (-2147213296), hrLegacySection (-2147213282), hrMalformedXML (-2147213312), hrMergeFailed (-2147213281), hrNavigatingToPage (-2147213302), hrNoActiveSelection (-2147213293), hrNoFriendlyNameForLinkedNote (-2147213273), hrNoShortNameForLinkedNote (-2147213274), hrNotebookDoesNotExist (-2147213291), hrNotYetSynchronized (-2147213283), hrObjectDoesNotExist (-2147213292), hrOpeningSection (-2147213309), hrPageDoesNotExist (-2147213307), hrPageDoesNotExistInGroup (-2147213294), hrPageObjectDoesNotExist (-2147213298), hrPageReadOnly (-2147213300), hrRecordingInProgress (-2147213276), hrRecycleBinEditFailed (-2147213266), hrSectionDoesNotExist (-2147213308), hrSectionEncryptedAndLocked (-2147213285), hrSectionReadOnly (-2147213301), hrTimeOut (-2147213277), hrUnknownLinkedNoteState (-2147213275), hrUnreadDisabledForNotebook (-2147213269) """
    hrAppInModalUI: Error = ...
    hrBinaryObjectDoesNotExist: Error = ...
    hrConvertFailed: Error = ...
    hrCreatingSection: Error = ...
    hrDisabledByPolicy: Error = ...
    hrFileAlreadyExists: Error = ...
    hrFileDoesNotExist: Error = ...
    hrFolderDoesNotExist: Error = ...
    hrFutureContentLoss: Error = ...
    hrGroupDoesNotExist: Error = ...
    hrImportLNTThumbnailFailed: Error = ...
    hrInsertingFile: Error = ...
    hrInsertingHtml: Error = ...
    hrInsertingImage: Error = ...
    hrInsertingInk: Error = ...
    hrInsertingOutlineText: Error = ...
    hrInvalidLinkedNoteThumbnail: Error = ...
    hrInvalidLinkedNoteUri: Error = ...
    hrInvalidName: Error = ...
    hrInvalidQuery: Error = ...
    hrInvalidSelection: Error = ...
    hrInvalidXML: Error = ...
    hrInvalidXMLSchema: Error = ...
    hrLastModifiedDateDidNotMatch: Error = ...
    hrLegacySection: Error = ...
    hrMalformedXML: Error = ...
    hrMergeFailed: Error = ...
    hrNavigatingToPage: Error = ...
    hrNoActiveSelection: Error = ...
    hrNoFriendlyNameForLinkedNote: Error = ...
    hrNoShortNameForLinkedNote: Error = ...
    hrNotebookDoesNotExist: Error = ...
    hrNotYetSynchronized: Error = ...
    hrObjectDoesNotExist: Error = ...
    hrOpeningSection: Error = ...
    hrPageDoesNotExist: Error = ...
    hrPageDoesNotExistInGroup: Error = ...
    hrPageObjectDoesNotExist: Error = ...
    hrPageReadOnly: Error = ...
    hrRecordingInProgress: Error = ...
    hrRecycleBinEditFailed: Error = ...
    hrSectionDoesNotExist: Error = ...
    hrSectionEncryptedAndLocked: Error = ...
    hrSectionReadOnly: Error = ...
    hrTimeOut: Error = ...
    hrUnknownLinkedNoteState: Error = ...
    hrUnreadDisabledForNotebook: Error = ...
    value__ = ...


class FilingLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FilingLocation, values: flContacts (1), flEMail (0), flMeetings (3), flPrintOuts (5), flTasks (2), flWebContent (4) """
    flContacts: FilingLocation = ...
    flEMail: FilingLocation = ...
    flMeetings: FilingLocation = ...
    flPrintOuts: FilingLocation = ...
    flTasks: FilingLocation = ...
    flWebContent: FilingLocation = ...
    value__ = ...


class FilingLocationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FilingLocationType, values: fltCurrentPage (2), fltCurrentSectionNewPage (1), fltNamedPage (4), fltNamedSectionNewPage (0) """
    fltCurrentPage: FilingLocationType = ...
    fltCurrentSectionNewPage: FilingLocationType = ...
    fltNamedPage: FilingLocationType = ...
    fltNamedSectionNewPage: FilingLocationType = ...
    value__ = ...


class HierarchyElement(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HierarchyElement, values: heNone (0), heNotebooks (1), hePages (8), heSectionGroups (2), heSections (4) """
    heNone: HierarchyElement = ...
    heNotebooks: HierarchyElement = ...
    hePages: HierarchyElement = ...
    heSectionGroups: HierarchyElement = ...
    heSections: HierarchyElement = ...
    value__ = ...


class HierarchyScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HierarchyScope, values: hsChildren (1), hsNotebooks (2), hsPages (4), hsSections (3), hsSelf (0) """
    hsChildren: HierarchyScope = ...
    hsNotebooks: HierarchyScope = ...
    hsPages: HierarchyScope = ...
    hsSections: HierarchyScope = ...
    hsSelf: HierarchyScope = ...
    value__ = ...


class IOneNoteEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnHierarchyChange(self, bstrActivePageID:str): # -> 
        """ OnHierarchyChange(self: IOneNoteEvents, bstrActivePageID: str) """
        ...

    def OnNavigate(self): # -> 
        """ OnNavigate(self: IOneNoteEvents) """
        ...


class IOneNoteEvents_OnHierarchyChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IOneNoteEvents_OnHierarchyChangeEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, bstrActivePageID:str): # -> 
        """ Invoke(self: IOneNoteEvents_OnHierarchyChangeEventHandler, bstrActivePageID: str) """
        ...


class IOneNoteEvents_OnNavigateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IOneNoteEvents_OnNavigateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: IOneNoteEvents_OnNavigateEventHandler) """
        ...


class IOneNoteEvents_SinkHelper(IOneNoteEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...
    m_OnHierarchyChangeDelegate = ...
    m_OnNavigateDelegate = ...


class IQuickFilingDialog: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CheckboxState(self) -> bool:
        """
        Get: CheckboxState(self: IQuickFilingDialog) -> bool
        Set: CheckboxState(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def CheckboxText(self) -> str:
        """
        Get: CheckboxText(self: IQuickFilingDialog) -> str
        Set: CheckboxText(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IQuickFilingDialog) -> str
        Set: Description(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def NotebookFilterOut(self): # -> 
        """ Set: NotebookFilterOut(self: IQuickFilingDialog) = value """
        ...

    @property
    def ParentWindowHandle(self) -> UInt64:
        """
        Get: ParentWindowHandle(self: IQuickFilingDialog) -> UInt64
        Set: ParentWindowHandle(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def Position(self) -> tagPOINT:
        """
        Get: Position(self: IQuickFilingDialog) -> tagPOINT
        Set: Position(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def PressedButton(self) -> UInt32:
        """ Get: PressedButton(self: IQuickFilingDialog) -> UInt32 """
        ...

    @property
    def SelectedItem(self) -> str:
        """ Get: SelectedItem(self: IQuickFilingDialog) -> str """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: IQuickFilingDialog) -> str
        Set: Title(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def TreeCollapsedState(self): # -> 
        """ Set: TreeCollapsedState(self: IQuickFilingDialog) = value """
        ...

    @property
    def TreeDepth(self) -> HierarchyElement:
        """
        Get: TreeDepth(self: IQuickFilingDialog) -> HierarchyElement
        Set: TreeDepth(self: IQuickFilingDialog) = value
        """
        ...

    @property
    def WindowHandle(self) -> UInt64:
        """ Get: WindowHandle(self: IQuickFilingDialog) -> UInt64 """
        ...


    def AddButton(self, bstrText:str, allowedElements:HierarchyElement, allowedReadOnlyElements:HierarchyElement, fDefault:bool): # -> 
        """ AddButton(self: IQuickFilingDialog, bstrText: str, allowedElements: HierarchyElement, allowedReadOnlyElements: HierarchyElement, fDefault: bool) """
        ...

    def AddInitialEditor(self, initialEditor:str): # -> 
        """ AddInitialEditor(self: IQuickFilingDialog, initialEditor: str) """
        ...

    def ClearInitialEditors(self): # -> 
        """ ClearInitialEditors(self: IQuickFilingDialog) """
        ...

    def Run(self, piCallback:IQuickFilingDialogCallback): # -> 
        """ Run(self: IQuickFilingDialog, piCallback: IQuickFilingDialogCallback) """
        ...

    def SetRecentResults(self, recentResults:RecentResultType, fShowCurrentSection:bool, fShowCurrentPage:bool, fShowUnfiledNotes:bool): # -> 
        """ SetRecentResults(self: IQuickFilingDialog, recentResults: RecentResultType, fShowCurrentSection: bool, fShowCurrentPage: bool, fShowUnfiledNotes: bool) """
        ...

    def ShowCreateNewNotebook(self): # -> 
        """ ShowCreateNewNotebook(self: IQuickFilingDialog) """
        ...

    def ShowSharingHyperlink(self): # -> 
        """ ShowSharingHyperlink(self: IQuickFilingDialog) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IQuickFilingDialogCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnDialogClosed(self, dialog:IQuickFilingDialog): # -> 
        """ OnDialogClosed(self: IQuickFilingDialogCallback, dialog: IQuickFilingDialog) """
        ...


class NewPageStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NewPageStyle, values: npsBlankPageNoTitle (2), npsBlankPageWithTitle (1), npsDefault (0) """
    npsBlankPageNoTitle: NewPageStyle = ...
    npsBlankPageWithTitle: NewPageStyle = ...
    npsDefault: NewPageStyle = ...
    value__ = ...


class NotebookFilterOutType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NotebookFilterOutType, values: nfoLocal (1), nfoNetwork (2), nfoNoWacUrl (8), nfoWeb (4) """
    nfoLocal: NotebookFilterOutType = ...
    nfoNetwork: NotebookFilterOutType = ...
    nfoNoWacUrl: NotebookFilterOutType = ...
    nfoWeb: NotebookFilterOutType = ...
    value__ = ...


class PageInfo(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PageInfo, values: piAll (7), piBasic (0), piBinaryData (1), piBinaryDataFileType (5), piBinaryDataSelection (3), piFileType (4), piSelection (2), piSelectionFileType (6) """
    piAll: PageInfo = ...
    piBasic: PageInfo = ...
    piBinaryData: PageInfo = ...
    piBinaryDataFileType: PageInfo = ...
    piBinaryDataSelection: PageInfo = ...
    piFileType: PageInfo = ...
    piSelection: PageInfo = ...
    piSelectionFileType: PageInfo = ...
    value__ = ...


class PublishFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PublishFormat, values: pfEMF (6), pfHTML (7), pfMHTML (2), pfOneNote (0), pfOneNote2007 (8), pfOneNotePackage (1), pfPDF (3), pfWord (5), pfXPS (4) """
    pfEMF: PublishFormat = ...
    pfHTML: PublishFormat = ...
    pfMHTML: PublishFormat = ...
    pfOneNote: PublishFormat = ...
    pfOneNote2007: PublishFormat = ...
    pfOneNotePackage: PublishFormat = ...
    pfPDF: PublishFormat = ...
    pfWord: PublishFormat = ...
    pfXPS: PublishFormat = ...
    value__ = ...


class RecentResultType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecentResultType, values: rrtFiling (1), rrtLinks (3), rrtNone (0), rrtSearch (2) """
    rrtFiling: RecentResultType = ...
    rrtLinks: RecentResultType = ...
    rrtNone: RecentResultType = ...
    rrtSearch: RecentResultType = ...
    value__ = ...


class SpecialLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SpecialLocation, values: slBackUpFolder (0), slDefaultNotebookFolder (2), slUnfiledNotesSection (1) """
    slBackUpFolder: SpecialLocation = ...
    slDefaultNotebookFolder: SpecialLocation = ...
    slUnfiledNotesSection: SpecialLocation = ...
    value__ = ...


class tagPOINT: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    x = ...
    y = ...


class TreeCollapsedStateType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TreeCollapsedStateType, values: tcsCollapsed (1), tcsExpanded (0) """
    tcsCollapsed: TreeCollapsedStateType = ...
    tcsExpanded: TreeCollapsedStateType = ...
    value__ = ...


class Window: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self) -> bool:
        """
        Get: Active(self: Window) -> bool
        Set: Active(self: Window) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Window) -> Application """
        ...

    @property
    def CurrentNotebookId(self) -> str:
        """ Get: CurrentNotebookId(self: Window) -> str """
        ...

    @property
    def CurrentPageId(self) -> str:
        """ Get: CurrentPageId(self: Window) -> str """
        ...

    @property
    def CurrentSectionGroupId(self) -> str:
        """ Get: CurrentSectionGroupId(self: Window) -> str """
        ...

    @property
    def CurrentSectionId(self) -> str:
        """ Get: CurrentSectionId(self: Window) -> str """
        ...

    @property
    def DockedLocation(self) -> DockLocation:
        """
        Get: DockedLocation(self: Window) -> DockLocation
        Set: DockedLocation(self: Window) = value
        """
        ...

    @property
    def FullPageView(self) -> bool:
        """
        Get: FullPageView(self: Window) -> bool
        Set: FullPageView(self: Window) = value
        """
        ...

    @property
    def SideNote(self) -> bool:
        """ Get: SideNote(self: Window) -> bool """
        ...

    @property
    def WindowHandle(self) -> UInt64:
        """ Get: WindowHandle(self: Window) -> UInt64 """
        ...


    def NavigateTo(self, bstrHierarchyObjectID:str, bstrObjectID:str): # -> 
        """ NavigateTo(self: Window, bstrHierarchyObjectID: str, bstrObjectID: str) """
        ...

    def NavigateToUrl(self, bstrUrl:str): # -> 
        """ NavigateToUrl(self: Window, bstrUrl: str) """
        ...

    def SetDockedLocation(self, DockLocation:DockLocation, ptMonitor:tagPOINT): # -> 
        """ SetDockedLocation(self: Window, DockLocation: DockLocation, ptMonitor: tagPOINT) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Windows(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> UInt32:
        """ Get: Count(self: Windows) -> UInt32 """
        ...

    @property
    def CurrentWindow(self) -> Window:
        """ Get: CurrentWindow(self: Windows) -> Window """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class XMLSchema(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XMLSchema, values: xs2007 (0), xs2010 (1), xs2013 (2), xsCurrent (2) """
    value__ = ...
    xs2007: XMLSchema = ...
    xs2010: XMLSchema = ...
    xs2013: XMLSchema = ...
    xsCurrent: XMLSchema = ...


