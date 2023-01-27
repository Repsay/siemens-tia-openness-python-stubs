# encoding: utf-8
# module Microsoft.Office.Interop.OutlookViewCtl calls itself OutlookViewCtl
# from Microsoft.Office.Interop.OutlookViewCtl, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime, Enum, MulticastDelegate

"""The following names are not found in the module: (BoundEvent, __ComObject, 
    field#)
"""

# no functions
# classes

class IDataCtl: # skipped bases: <type 'object'>
    """ no doc """
    pass

class DataCtl(IDataCtl): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DataCtlClass(__ComObject, DataCtl): # skipped bases: <type 'IDataCtl'>, <type 'object'>
    """ DataCtlClass() """
    pass

class FIELDREGISTRY_REFRESHOPTIONS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FIELDREGISTRY_REFRESHOPTIONS, values: fro_Fields (1), fro_Forms (0), fro_View (2) """
    fro_Fields: FIELDREGISTRY_REFRESHOPTIONS = ...
    fro_Forms: FIELDREGISTRY_REFRESHOPTIONS = ...
    fro_View: FIELDREGISTRY_REFRESHOPTIONS = ...
    value__ = ...


class FR_REFRESHOPTIONS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FR_REFRESHOPTIONS, values: fro_Fields (1), fro_Forms (0), fro_View (2) """
    fro_Fields: FR_REFRESHOPTIONS = ...
    fro_Forms: FR_REFRESHOPTIONS = ...
    fro_View: FR_REFRESHOPTIONS = ...
    value__ = ...


class IObjectModelAccess: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveDesktop(self) -> int:
        """
        Get: ActiveDesktop(self: IObjectModelAccess) -> int
        Set: ActiveDesktop(self: IObjectModelAccess) = value
        """
        ...

    @property
    def OutlookApplication(self) -> object:
        """
        Get: OutlookApplication(self: IObjectModelAccess) -> object
        Set: OutlookApplication(self: IObjectModelAccess) = value
        """
        ...


    def DeletePrefs(self): # -> 
        """ DeletePrefs(self: IObjectModelAccess) """
        ...

    def EnableInProcOptimizations(self): # -> 
        """ EnableInProcOptimizations(self: IObjectModelAccess) """
        ...

    def FindPerson(self, bstrName:str): # -> 
        """ FindPerson(self: IObjectModelAccess, bstrName: str) """
        ...

    def GetDate(self) -> str:
        """ GetDate(self: IObjectModelAccess) -> str """
        ...

    def GetPref(self, szname:str) -> str:
        """ GetPref(self: IObjectModelAccess, szname: str) -> str """
        ...

    def PickEmailFolders(self): # -> 
        """ PickEmailFolders(self: IObjectModelAccess) """
        ...

    def SetPref(self, szname:str, szvalue:str): # -> 
        """ SetPref(self: IObjectModelAccess, szname: str, szvalue: str) """
        ...


class IViewCtl: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveFolder(self) -> object:
        """ Get: ActiveFolder(self: IViewCtl) -> object """
        ...

    @property
    def DeferUpdate(self) -> bool:
        """
        Get: DeferUpdate(self: IViewCtl) -> bool
        Set: DeferUpdate(self: IViewCtl) = value
        """
        ...

    @property
    def Dirty(self) -> bool:
        """
        Get: Dirty(self: IViewCtl) -> bool
        Set: Dirty(self: IViewCtl) = value
        """
        ...

    @property
    def EnableRowPersistance(self) -> bool:
        """
        Get: EnableRowPersistance(self: IViewCtl) -> bool
        Set: EnableRowPersistance(self: IViewCtl) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: IViewCtl) -> str
        Set: Filter(self: IViewCtl) = value
        """
        ...

    @property
    def FilterAppend(self) -> str:
        """
        Get: FilterAppend(self: IViewCtl) -> str
        Set: FilterAppend(self: IViewCtl) = value
        """
        ...

    @property
    def Folder(self) -> str:
        """
        Get: Folder(self: IViewCtl) -> str
        Set: Folder(self: IViewCtl) = value
        """
        ...

    @property
    def ItemCount(self) -> int:
        """ Get: ItemCount(self: IViewCtl) -> int """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: IViewCtl) -> str
        Set: Namespace(self: IViewCtl) = value
        """
        ...

    @property
    def OutlookApplication(self) -> object:
        """ Get: OutlookApplication(self: IViewCtl) -> object """
        ...

    @property
    def Restriction(self) -> str:
        """
        Get: Restriction(self: IViewCtl) -> str
        Set: Restriction(self: IViewCtl) = value
        """
        ...

    @property
    def SelectedDate(self) -> DateTime:
        """ Get: SelectedDate(self: IViewCtl) -> DateTime """
        ...

    @property
    def Selection(self) -> object:
        """ Get: Selection(self: IViewCtl) -> object """
        ...

    @property
    def View(self) -> str:
        """
        Get: View(self: IViewCtl) -> str
        Set: View(self: IViewCtl) = value
        """
        ...

    @property
    def ViewXML(self) -> str:
        """
        Get: ViewXML(self: IViewCtl) -> str
        Set: ViewXML(self: IViewCtl) = value
        """
        ...


    def AddressBook(self): # -> 
        """ AddressBook(self: IViewCtl) """
        ...

    def AddressMeeting(self, pdispContainer:object): # -> 
        """ AddressMeeting(self: IViewCtl, pdispContainer: object) """
        ...

    def AddressMessage(self, pdispContainer:object): # -> 
        """ AddressMessage(self: IViewCtl, pdispContainer: object) """
        ...

    def AddToPFFavorites(self): # -> 
        """ AddToPFFavorites(self: IViewCtl) """
        ...

    def AdvancedFind(self): # -> 
        """ AdvancedFind(self: IViewCtl) """
        ...

    def Categories(self): # -> 
        """ Categories(self: IViewCtl) """
        ...

    def CollapseAllGroups(self): # -> 
        """ CollapseAllGroups(self: IViewCtl) """
        ...

    def CollapseGroup(self): # -> 
        """ CollapseGroup(self: IViewCtl) """
        ...

    def CustomizeView(self): # -> 
        """ CustomizeView(self: IViewCtl) """
        ...

    def Delete(self): # -> 
        """ Delete(self: IViewCtl) """
        ...

    def ExpandAllGroups(self): # -> 
        """ ExpandAllGroups(self: IViewCtl) """
        ...

    def ExpandGroup(self): # -> 
        """ ExpandGroup(self: IViewCtl) """
        ...

    def ExplorerActivate(self): # -> 
        """ ExplorerActivate(self: IViewCtl) """
        ...

    def ExplorerBeforeViewSwitch(self, bStrNewView:str, pVarCancel:bool) -> bool:
        """ ExplorerBeforeViewSwitch(self: IViewCtl, bStrNewView: str, pVarCancel: bool) -> bool """
        ...

    def ExplorerSelectionChange(self): # -> 
        """ ExplorerSelectionChange(self: IViewCtl) """
        ...

    def ExplorerViewSwitch(self): # -> 
        """ ExplorerViewSwitch(self: IViewCtl) """
        ...

    def FlagItem(self): # -> 
        """ FlagItem(self: IViewCtl) """
        ...

    def ForceUpdate(self): # -> 
        """ ForceUpdate(self: IViewCtl) """
        ...

    def Forward(self): # -> 
        """ Forward(self: IViewCtl) """
        ...

    def GoToDate(self, newDate:str): # -> 
        """ GoToDate(self: IViewCtl, newDate: str) """
        ...

    def GoToToday(self): # -> 
        """ GoToToday(self: IViewCtl) """
        ...

    def GroupBy(self): # -> 
        """ GroupBy(self: IViewCtl) """
        ...

    def MarkAllAsRead(self): # -> 
        """ MarkAllAsRead(self: IViewCtl) """
        ...

    def MarkAsRead(self): # -> 
        """ MarkAsRead(self: IViewCtl) """
        ...

    def MarkAsUnread(self): # -> 
        """ MarkAsUnread(self: IViewCtl) """
        ...

    def MoveItem(self): # -> 
        """ MoveItem(self: IViewCtl) """
        ...

    def NewAppointment(self): # -> 
        """ NewAppointment(self: IViewCtl) """
        ...

    def NewContact(self): # -> 
        """ NewContact(self: IViewCtl) """
        ...

    def NewDefaultItem(self): # -> 
        """ NewDefaultItem(self: IViewCtl) """
        ...

    def NewDistributionList(self): # -> 
        """ NewDistributionList(self: IViewCtl) """
        ...

    def NewForm(self): # -> 
        """ NewForm(self: IViewCtl) """
        ...

    def NewJournalEntry(self): # -> 
        """ NewJournalEntry(self: IViewCtl) """
        ...

    def NewMeetingRequest(self): # -> 
        """ NewMeetingRequest(self: IViewCtl) """
        ...

    def NewMessage(self): # -> 
        """ NewMessage(self: IViewCtl) """
        ...

    def NewNote(self): # -> 
        """ NewNote(self: IViewCtl) """
        ...

    def NewOfficeDocument(self): # -> 
        """ NewOfficeDocument(self: IViewCtl) """
        ...

    def NewPost(self): # -> 
        """ NewPost(self: IViewCtl) """
        ...

    def NewTask(self): # -> 
        """ NewTask(self: IViewCtl) """
        ...

    def NewTaskRequest(self): # -> 
        """ NewTaskRequest(self: IViewCtl) """
        ...

    def Open(self): # -> 
        """ Open(self: IViewCtl) """
        ...

    def OpenSharedDefaultFolder(self, bstrRecipient:str, FolderType:OlxDefaultFolders): # -> 
        """ OpenSharedDefaultFolder(self: IViewCtl, bstrRecipient: str, FolderType: OlxDefaultFolders) """
        ...

    def PrintItem(self): # -> 
        """ PrintItem(self: IViewCtl) """
        ...

    def RefreshFieldRegistry(self, fro:FR_REFRESHOPTIONS): # -> 
        """ RefreshFieldRegistry(self: IViewCtl, fro: FR_REFRESHOPTIONS) """
        ...

    def Reply(self): # -> 
        """ Reply(self: IViewCtl) """
        ...

    def ReplyAll(self): # -> 
        """ ReplyAll(self: IViewCtl) """
        ...

    def ReplyInFolder(self): # -> 
        """ ReplyInFolder(self: IViewCtl) """
        ...

    def SaveAs(self): # -> 
        """ SaveAs(self: IViewCtl) """
        ...

    def SaveView(self, ViewName:str): # -> 
        """ SaveView(self: IViewCtl, ViewName: str) """
        ...

    def SendAndReceive(self): # -> 
        """ SendAndReceive(self: IViewCtl) """
        ...

    def SetDesignMode(self): # -> 
        """ SetDesignMode(self: IViewCtl) """
        ...

    def ShowFields(self): # -> 
        """ ShowFields(self: IViewCtl) """
        ...

    def Sort(self): # -> 
        """ Sort(self: IViewCtl) """
        ...

    def SynchFolder(self): # -> 
        """ SynchFolder(self: IViewCtl) """
        ...


class ObjectModelCtl(IObjectModelAccess): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ObjectModelCtlClass(ObjectModelCtl, __ComObject): # skipped bases: <type 'IObjectModelAccess'>, <type 'object'>
    """ ObjectModelCtlClass() """
    @property
    def ActiveDesktop(self) -> int:
        """
        Get: ActiveDesktop(self: ObjectModelCtlClass) -> int
        Set: ActiveDesktop(self: ObjectModelCtlClass) = value
        """
        ...

    @property
    def OutlookApplication(self) -> object:
        """
        Get: OutlookApplication(self: ObjectModelCtlClass) -> object
        Set: OutlookApplication(self: ObjectModelCtlClass) = value
        """
        ...


    def DeletePrefs(self): # -> 
        """ DeletePrefs(self: ObjectModelCtlClass) """
        ...

    def EnableInProcOptimizations(self): # -> 
        """ EnableInProcOptimizations(self: ObjectModelCtlClass) """
        ...

    def FindPerson(self, bstrName:str): # -> 
        """ FindPerson(self: ObjectModelCtlClass, bstrName: str) """
        ...

    def GetDate(self) -> str:
        """ GetDate(self: ObjectModelCtlClass) -> str """
        ...

    def GetPref(self, szname:str) -> str:
        """ GetPref(self: ObjectModelCtlClass, szname: str) -> str """
        ...

    def PickEmailFolders(self): # -> 
        """ PickEmailFolders(self: ObjectModelCtlClass) """
        ...

    def SetPref(self, szname:str, szvalue:str): # -> 
        """ SetPref(self: ObjectModelCtlClass, szname: str, szvalue: str) """
        ...


class OlxDefaultFolders(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OlxDefaultFolders, values: olxFolderCalendar (9), olxFolderContacts (10), olxFolderDeletedItems (3), olxFolderDrafts (16), olxFolderInbox (6), olxFolderJournal (11), olxFolderNotes (12), olxFolderOutbox (4), olxFolderSentMail (5), olxFolderTasks (13) """
    olxFolderCalendar: OlxDefaultFolders = ...
    olxFolderContacts: OlxDefaultFolders = ...
    olxFolderDeletedItems: OlxDefaultFolders = ...
    olxFolderDrafts: OlxDefaultFolders = ...
    olxFolderInbox: OlxDefaultFolders = ...
    olxFolderJournal: OlxDefaultFolders = ...
    olxFolderNotes: OlxDefaultFolders = ...
    olxFolderOutbox: OlxDefaultFolders = ...
    olxFolderSentMail: OlxDefaultFolders = ...
    olxFolderTasks: OlxDefaultFolders = ...
    value__ = ...


class ViewCtlEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Activate(self): # -> 
        """ add_Activate(self: ViewCtlEvents_Event, : ViewCtlEvents_ActivateEventHandler) """
        ...

    def add_BeforeViewSwitch(self): # -> 
        """ add_BeforeViewSwitch(self: ViewCtlEvents_Event, : ViewCtlEvents_BeforeViewSwitchEventHandler) """
        ...

    def add_SelectionChange(self): # -> 
        """ add_SelectionChange(self: ViewCtlEvents_Event, : ViewCtlEvents_SelectionChangeEventHandler) """
        ...

    def add_ViewSwitch(self): # -> 
        """ add_ViewSwitch(self: ViewCtlEvents_Event, : ViewCtlEvents_ViewSwitchEventHandler) """
        ...

    def remove_Activate(self): # -> 
        """ remove_Activate(self: ViewCtlEvents_Event, : ViewCtlEvents_ActivateEventHandler) """
        ...

    def remove_BeforeViewSwitch(self): # -> 
        """ remove_BeforeViewSwitch(self: ViewCtlEvents_Event, : ViewCtlEvents_BeforeViewSwitchEventHandler) """
        ...

    def remove_SelectionChange(self): # -> 
        """ remove_SelectionChange(self: ViewCtlEvents_Event, : ViewCtlEvents_SelectionChangeEventHandler) """
        ...

    def remove_ViewSwitch(self): # -> 
        """ remove_ViewSwitch(self: ViewCtlEvents_Event, : ViewCtlEvents_ViewSwitchEventHandler) """
        ...

    Activate = ...
    BeforeViewSwitch = ...
    SelectionChange = ...
    ViewSwitch = ...


class ViewCtl(ViewCtlEvents_Event, IViewCtl): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ViewCtlClass(ViewCtl, __ComObject): # skipped bases: <type 'ViewCtlEvents_Event'>, <type 'IViewCtl'>, <type 'object'>
    """ ViewCtlClass() """
    @property
    def ActiveFolder(self) -> object:
        """ Get: ActiveFolder(self: ViewCtlClass) -> object """
        ...

    @property
    def DeferUpdate(self) -> bool:
        """
        Get: DeferUpdate(self: ViewCtlClass) -> bool
        Set: DeferUpdate(self: ViewCtlClass) = value
        """
        ...

    @property
    def Dirty(self) -> bool:
        """
        Get: Dirty(self: ViewCtlClass) -> bool
        Set: Dirty(self: ViewCtlClass) = value
        """
        ...

    @property
    def EnableRowPersistance(self) -> bool:
        """
        Get: EnableRowPersistance(self: ViewCtlClass) -> bool
        Set: EnableRowPersistance(self: ViewCtlClass) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: ViewCtlClass) -> str
        Set: Filter(self: ViewCtlClass) = value
        """
        ...

    @property
    def FilterAppend(self) -> str:
        """
        Get: FilterAppend(self: ViewCtlClass) -> str
        Set: FilterAppend(self: ViewCtlClass) = value
        """
        ...

    @property
    def Folder(self) -> str:
        """
        Get: Folder(self: ViewCtlClass) -> str
        Set: Folder(self: ViewCtlClass) = value
        """
        ...

    @property
    def ItemCount(self) -> int:
        """ Get: ItemCount(self: ViewCtlClass) -> int """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: ViewCtlClass) -> str
        Set: Namespace(self: ViewCtlClass) = value
        """
        ...

    @property
    def OutlookApplication(self) -> object:
        """ Get: OutlookApplication(self: ViewCtlClass) -> object """
        ...

    @property
    def Restriction(self) -> str:
        """
        Get: Restriction(self: ViewCtlClass) -> str
        Set: Restriction(self: ViewCtlClass) = value
        """
        ...

    @property
    def SelectedDate(self) -> DateTime:
        """ Get: SelectedDate(self: ViewCtlClass) -> DateTime """
        ...

    @property
    def Selection(self) -> object:
        """ Get: Selection(self: ViewCtlClass) -> object """
        ...

    @property
    def View(self) -> str:
        """
        Get: View(self: ViewCtlClass) -> str
        Set: View(self: ViewCtlClass) = value
        """
        ...

    @property
    def ViewXML(self) -> str:
        """
        Get: ViewXML(self: ViewCtlClass) -> str
        Set: ViewXML(self: ViewCtlClass) = value
        """
        ...


    def AddressBook(self): # -> 
        """ AddressBook(self: ViewCtlClass) """
        ...

    def AddressMeeting(self, pdispContainer:object): # -> 
        """ AddressMeeting(self: ViewCtlClass, pdispContainer: object) """
        ...

    def AddressMessage(self, pdispContainer:object): # -> 
        """ AddressMessage(self: ViewCtlClass, pdispContainer: object) """
        ...

    def AddToPFFavorites(self): # -> 
        """ AddToPFFavorites(self: ViewCtlClass) """
        ...

    def add_Activate(self): # -> 
        """ add_Activate(self: ViewCtlClass, : ViewCtlEvents_ActivateEventHandler) """
        ...

    def add_BeforeViewSwitch(self): # -> 
        """ add_BeforeViewSwitch(self: ViewCtlClass, : ViewCtlEvents_BeforeViewSwitchEventHandler) """
        ...

    def add_SelectionChange(self): # -> 
        """ add_SelectionChange(self: ViewCtlClass, : ViewCtlEvents_SelectionChangeEventHandler) """
        ...

    def add_ViewSwitch(self): # -> 
        """ add_ViewSwitch(self: ViewCtlClass, : ViewCtlEvents_ViewSwitchEventHandler) """
        ...

    def AdvancedFind(self): # -> 
        """ AdvancedFind(self: ViewCtlClass) """
        ...

    def Categories(self): # -> 
        """ Categories(self: ViewCtlClass) """
        ...

    def CollapseAllGroups(self): # -> 
        """ CollapseAllGroups(self: ViewCtlClass) """
        ...

    def CollapseGroup(self): # -> 
        """ CollapseGroup(self: ViewCtlClass) """
        ...

    def CustomizeView(self): # -> 
        """ CustomizeView(self: ViewCtlClass) """
        ...

    def Delete(self): # -> 
        """ Delete(self: ViewCtlClass) """
        ...

    def ExpandAllGroups(self): # -> 
        """ ExpandAllGroups(self: ViewCtlClass) """
        ...

    def ExpandGroup(self): # -> 
        """ ExpandGroup(self: ViewCtlClass) """
        ...

    def ExplorerActivate(self): # -> 
        """ ExplorerActivate(self: ViewCtlClass) """
        ...

    def ExplorerBeforeViewSwitch(self, bStrNewView:str, pVarCancel:bool) -> bool:
        """ ExplorerBeforeViewSwitch(self: ViewCtlClass, bStrNewView: str, pVarCancel: bool) -> bool """
        ...

    def ExplorerSelectionChange(self): # -> 
        """ ExplorerSelectionChange(self: ViewCtlClass) """
        ...

    def ExplorerViewSwitch(self): # -> 
        """ ExplorerViewSwitch(self: ViewCtlClass) """
        ...

    def FlagItem(self): # -> 
        """ FlagItem(self: ViewCtlClass) """
        ...

    def ForceUpdate(self): # -> 
        """ ForceUpdate(self: ViewCtlClass) """
        ...

    def Forward(self): # -> 
        """ Forward(self: ViewCtlClass) """
        ...

    def GoToDate(self, newDate:str): # -> 
        """ GoToDate(self: ViewCtlClass, newDate: str) """
        ...

    def GoToToday(self): # -> 
        """ GoToToday(self: ViewCtlClass) """
        ...

    def GroupBy(self): # -> 
        """ GroupBy(self: ViewCtlClass) """
        ...

    def MarkAllAsRead(self): # -> 
        """ MarkAllAsRead(self: ViewCtlClass) """
        ...

    def MarkAsRead(self): # -> 
        """ MarkAsRead(self: ViewCtlClass) """
        ...

    def MarkAsUnread(self): # -> 
        """ MarkAsUnread(self: ViewCtlClass) """
        ...

    def MoveItem(self): # -> 
        """ MoveItem(self: ViewCtlClass) """
        ...

    def NewAppointment(self): # -> 
        """ NewAppointment(self: ViewCtlClass) """
        ...

    def NewContact(self): # -> 
        """ NewContact(self: ViewCtlClass) """
        ...

    def NewDefaultItem(self): # -> 
        """ NewDefaultItem(self: ViewCtlClass) """
        ...

    def NewDistributionList(self): # -> 
        """ NewDistributionList(self: ViewCtlClass) """
        ...

    def NewForm(self): # -> 
        """ NewForm(self: ViewCtlClass) """
        ...

    def NewJournalEntry(self): # -> 
        """ NewJournalEntry(self: ViewCtlClass) """
        ...

    def NewMeetingRequest(self): # -> 
        """ NewMeetingRequest(self: ViewCtlClass) """
        ...

    def NewMessage(self): # -> 
        """ NewMessage(self: ViewCtlClass) """
        ...

    def NewNote(self): # -> 
        """ NewNote(self: ViewCtlClass) """
        ...

    def NewOfficeDocument(self): # -> 
        """ NewOfficeDocument(self: ViewCtlClass) """
        ...

    def NewPost(self): # -> 
        """ NewPost(self: ViewCtlClass) """
        ...

    def NewTask(self): # -> 
        """ NewTask(self: ViewCtlClass) """
        ...

    def NewTaskRequest(self): # -> 
        """ NewTaskRequest(self: ViewCtlClass) """
        ...

    def Open(self): # -> 
        """ Open(self: ViewCtlClass) """
        ...

    def OpenSharedDefaultFolder(self, bstrRecipient:str, FolderType:OlxDefaultFolders): # -> 
        """ OpenSharedDefaultFolder(self: ViewCtlClass, bstrRecipient: str, FolderType: OlxDefaultFolders) """
        ...

    def PrintItem(self): # -> 
        """ PrintItem(self: ViewCtlClass) """
        ...

    def RefreshFieldRegistry(self, fro:FR_REFRESHOPTIONS): # -> 
        """ RefreshFieldRegistry(self: ViewCtlClass, fro: FR_REFRESHOPTIONS) """
        ...

    def remove_Activate(self): # -> 
        """ remove_Activate(self: ViewCtlClass, : ViewCtlEvents_ActivateEventHandler) """
        ...

    def remove_BeforeViewSwitch(self): # -> 
        """ remove_BeforeViewSwitch(self: ViewCtlClass, : ViewCtlEvents_BeforeViewSwitchEventHandler) """
        ...

    def remove_SelectionChange(self): # -> 
        """ remove_SelectionChange(self: ViewCtlClass, : ViewCtlEvents_SelectionChangeEventHandler) """
        ...

    def remove_ViewSwitch(self): # -> 
        """ remove_ViewSwitch(self: ViewCtlClass, : ViewCtlEvents_ViewSwitchEventHandler) """
        ...

    def Reply(self): # -> 
        """ Reply(self: ViewCtlClass) """
        ...

    def ReplyAll(self): # -> 
        """ ReplyAll(self: ViewCtlClass) """
        ...

    def ReplyInFolder(self): # -> 
        """ ReplyInFolder(self: ViewCtlClass) """
        ...

    def SaveAs(self): # -> 
        """ SaveAs(self: ViewCtlClass) """
        ...

    def SaveView(self, ViewName:str): # -> 
        """ SaveView(self: ViewCtlClass, ViewName: str) """
        ...

    def SendAndReceive(self): # -> 
        """ SendAndReceive(self: ViewCtlClass) """
        ...

    def SetDesignMode(self): # -> 
        """ SetDesignMode(self: ViewCtlClass) """
        ...

    def ShowFields(self): # -> 
        """ ShowFields(self: ViewCtlClass) """
        ...

    def Sort(self): # -> 
        """ Sort(self: ViewCtlClass) """
        ...

    def SynchFolder(self): # -> 
        """ SynchFolder(self: ViewCtlClass) """
        ...

    Activate = ...
    BeforeViewSwitch = ...
    SelectionChange = ...
    ViewSwitch = ...


class ViewCtlEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Activate(self): # -> 
        """ Activate(self: ViewCtlEvents) """
        ...

    def BeforeViewSwitch(self, newView:str, Cancel:bool) -> bool:
        """ BeforeViewSwitch(self: ViewCtlEvents, newView: str, Cancel: bool) -> bool """
        ...

    def SelectionChange(self): # -> 
        """ SelectionChange(self: ViewCtlEvents) """
        ...

    def ViewSwitch(self): # -> 
        """ ViewSwitch(self: ViewCtlEvents) """
        ...


class ViewCtlEvents_ActivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ViewCtlEvents_ActivateEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ViewCtlEvents_ActivateEventHandler) """
        ...


class ViewCtlEvents_BeforeViewSwitchEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ViewCtlEvents_BeforeViewSwitchEventHandler(: object, : UIntPtr) """
    def Invoke(self, newView:str, Cancel:bool) -> bool:
        """ Invoke(self: ViewCtlEvents_BeforeViewSwitchEventHandler, newView: str, Cancel: bool) -> bool """
        ...


class ViewCtlEvents_SelectionChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ViewCtlEvents_SelectionChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ViewCtlEvents_SelectionChangeEventHandler) """
        ...


class ViewCtlEvents_SinkHelper(ViewCtlEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_ActivateDelegate = ...
    m_BeforeViewSwitchDelegate = ...
    m_dwCookie = ...
    m_SelectionChangeDelegate = ...
    m_ViewSwitchDelegate = ...


class ViewCtlEvents_ViewSwitchEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ViewCtlEvents_ViewSwitchEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ViewCtlEvents_ViewSwitchEventHandler) """
        ...


