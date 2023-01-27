# encoding: utf-8
# module Microsoft.Office.Interop.SmartTag calls itself SmartTag
# from Microsoft.Office.Interop.SmartTag, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class C_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum C_TYPE, values: C_TYPE_ACTIVEX (13), C_TYPE_BUTTON (6), C_TYPE_CHECKBOX (9), C_TYPE_COMBO (12), C_TYPE_DOCUMENTFRAGMENT (14), C_TYPE_DOCUMENTFRAGMENTURL (15), C_TYPE_HELP (3), C_TYPE_HELPURL (4), C_TYPE_IMAGE (8), C_TYPE_LABEL (7), C_TYPE_LINK (2), C_TYPE_LISTBOX (11), C_TYPE_RADIOGROUP (16), C_TYPE_SEPARATOR (5), C_TYPE_TEXTBOX (10) """
    C_TYPE_ACTIVEX: C_TYPE = ...
    C_TYPE_BUTTON: C_TYPE = ...
    C_TYPE_CHECKBOX: C_TYPE = ...
    C_TYPE_COMBO: C_TYPE = ...
    C_TYPE_DOCUMENTFRAGMENT: C_TYPE = ...
    C_TYPE_DOCUMENTFRAGMENTURL: C_TYPE = ...
    C_TYPE_HELP: C_TYPE = ...
    C_TYPE_HELPURL: C_TYPE = ...
    C_TYPE_IMAGE: C_TYPE = ...
    C_TYPE_LABEL: C_TYPE = ...
    C_TYPE_LINK: C_TYPE = ...
    C_TYPE_LISTBOX: C_TYPE = ...
    C_TYPE_RADIOGROUP: C_TYPE = ...
    C_TYPE_SEPARATOR: C_TYPE = ...
    C_TYPE_TEXTBOX: C_TYPE = ...
    value__ = ...


class IF_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IF_TYPE, values: IF_TYPE_CELL (16), IF_TYPE_CHAR (1), IF_TYPE_PARA (8), IF_TYPE_REGEXP (4), IF_TYPE_RUN (32), IF_TYPE_SINGLE_WD (2) """
    IF_TYPE_CELL: IF_TYPE = ...
    IF_TYPE_CHAR: IF_TYPE = ...
    IF_TYPE_PARA: IF_TYPE = ...
    IF_TYPE_REGEXP: IF_TYPE = ...
    IF_TYPE_RUN: IF_TYPE = ...
    IF_TYPE_SINGLE_WD: IF_TYPE = ...
    value__ = ...


class ISmartDocProperties: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISmartDocProperties) -> int """
        ...


    def Write(self, Key:str, Value:str): # -> 
        """ Write(self: ISmartDocProperties, Key: str, Value: str) """
        ...


class ISmartDocument: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SmartDocXmlTypeCount(self) -> int:
        """ Get: SmartDocXmlTypeCount(self: ISmartDocument) -> int """
        ...


    def ImageClick(self, ControlID:int, ApplicationName:str, Target:object, Text:str, Xml:str, LocaleID:int, XCoordinate:int, YCoordinate:int): # -> 
        """ ImageClick(self: ISmartDocument, ControlID: int, ApplicationName: str, Target: object, Text: str, Xml: str, LocaleID: int, XCoordinate: int, YCoordinate: int) """
        ...

    def InvokeControl(self, ControlID:int, ApplicationName:str, Target:object, Text:str, Xml:str, LocaleID:int): # -> 
        """ InvokeControl(self: ISmartDocument, ControlID: int, ApplicationName: str, Target: object, Text: str, Xml: str, LocaleID: int) """
        ...

    def OnCheckboxChange(self, ControlID:int, Target:object, Checked:bool): # -> 
        """ OnCheckboxChange(self: ISmartDocument, ControlID: int, Target: object, Checked: bool) """
        ...

    def OnListOrComboSelectChange(self, ControlID:int, Target:object, Selected:int, Value:str): # -> 
        """ OnListOrComboSelectChange(self: ISmartDocument, ControlID: int, Target: object, Selected: int, Value: str) """
        ...

    def OnPaneUpdateComplete(self, Document:object): # -> 
        """ OnPaneUpdateComplete(self: ISmartDocument, Document: object) """
        ...

    def OnRadioGroupSelectChange(self, ControlID:int, Target:object, Selected:int, Value:str): # -> 
        """ OnRadioGroupSelectChange(self: ISmartDocument, ControlID: int, Target: object, Selected: int, Value: str) """
        ...

    def OnTextboxContentChange(self, ControlID:int, Target:object, Value:str): # -> 
        """ OnTextboxContentChange(self: ISmartDocument, ControlID: int, Target: object, Value: str) """
        ...

    def PopulateActiveXProps(self, ControlID:int, ApplicationName:str, LocaleID:int, Text:str, Xml:str, Target:object, Props:ISmartDocProperties, ActiveXPropBag:ISmartDocProperties): # -> 
        """ PopulateActiveXProps(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties, ActiveXPropBag: ISmartDocProperties) """
        ...

    def PopulateCheckbox(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, Checked) -> bool:
        """ PopulateCheckbox(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> bool """
        ...

    def PopulateDocumentFragment(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, DocumentFragment) -> str:
        """ PopulateDocumentFragment(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> str """
        ...

    def PopulateHelpContent(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, Content) -> str:
        """ PopulateHelpContent(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> str """
        ...

    def PopulateImage(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, ImageSrc) -> str:
        """ PopulateImage(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> str """
        ...

    def PopulateListOrComboContent(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, List, Count, InitialSelected) -> Tuple_[Array, int, int]:
        """ PopulateListOrComboContent(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> (Array, int, int) """
        ...

    def PopulateOther(self, ControlID:int, ApplicationName:str, LocaleID:int, Text:str, Xml:str, Target:object, Props:ISmartDocProperties): # -> 
        """ PopulateOther(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) """
        ...

    def PopulateRadioGroup(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, List, Count, InitialSelected) -> Tuple_[Array, int, int]:
        """ PopulateRadioGroup(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> (Array, int, int) """
        ...

    def PopulateTextboxContent(self, ControlID, ApplicationName, LocaleID, Text, Xml, Target, Props, Value) -> str:
        """ PopulateTextboxContent(self: ISmartDocument, ControlID: int, ApplicationName: str, LocaleID: int, Text: str, Xml: str, Target: object, Props: ISmartDocProperties) -> str """
        ...

    def SmartDocInitialize(self, ApplicationName:str, Document:object, SolutionPath:str, SolutionRegKeyRoot:str): # -> 
        """ SmartDocInitialize(self: ISmartDocument, ApplicationName: str, Document: object, SolutionPath: str, SolutionRegKeyRoot: str) """
        ...


class ISmartTagAction: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ProgId(self) -> str:
        """ Get: ProgId(self: ISmartTagAction) -> str """
        ...

    @property
    def SmartTagCount(self) -> int:
        """ Get: SmartTagCount(self: ISmartTagAction) -> int """
        ...


    def InvokeVerb(self, VerbID:int, ApplicationName:str, Target:object, Properties:ISmartTagProperties, Text:str, Xml:str): # -> 
        """ InvokeVerb(self: ISmartTagAction, VerbID: int, ApplicationName: str, Target: object, Properties: ISmartTagProperties, Text: str, Xml: str) """
        ...


class ISmartTagAction2: # skipped bases: <type 'object'>
    """ no doc """
    def InvokeVerb2(self, VerbID:int, ApplicationName:str, Target:object, Properties:ISmartTagProperties, Text:str, Xml:str, LocaleID:int): # -> 
        """ InvokeVerb2(self: ISmartTagAction2, VerbID: int, ApplicationName: str, Target: object, Properties: ISmartTagProperties, Text: str, Xml: str, LocaleID: int) """
        ...

    def SmartTagInitialize(self, ApplicationName:str): # -> 
        """ SmartTagInitialize(self: ISmartTagAction2, ApplicationName: str) """
        ...


class ISmartTagProperties: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISmartTagProperties) -> int """
        ...


    def Write(self, Key:str, Value:str): # -> 
        """ Write(self: ISmartTagProperties, Key: str, Value: str) """
        ...


class ISmartTagRecognizer: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ProgId(self) -> str:
        """ Get: ProgId(self: ISmartTagRecognizer) -> str """
        ...

    @property
    def SmartTagCount(self) -> int:
        """ Get: SmartTagCount(self: ISmartTagRecognizer) -> int """
        ...


    def Recognize(self, Text:str, DataType:IF_TYPE, LocaleID:int, RecognizerSite:ISmartTagRecognizerSite): # -> 
        """ Recognize(self: ISmartTagRecognizer, Text: str, DataType: IF_TYPE, LocaleID: int, RecognizerSite: ISmartTagRecognizerSite) """
        ...


class ISmartTagRecognizer2: # skipped bases: <type 'object'>
    """ no doc """
    def DisplayPropertyPage(self, SmartTagID:int, LocaleID:int): # -> 
        """ DisplayPropertyPage(self: ISmartTagRecognizer2, SmartTagID: int, LocaleID: int) """
        ...

    def Recognize2(self, Text:str, DataType:IF_TYPE, LocaleID:int, RecognizerSite2:ISmartTagRecognizerSite2, ApplicationName:str, TokenList:ISmartTagTokenList): # -> 
        """ Recognize2(self: ISmartTagRecognizer2, Text: str, DataType: IF_TYPE, LocaleID: int, RecognizerSite2: ISmartTagRecognizerSite2, ApplicationName: str, TokenList: ISmartTagTokenList) """
        ...

    def SmartTagInitialize(self, ApplicationName:str): # -> 
        """ SmartTagInitialize(self: ISmartTagRecognizer2, ApplicationName: str) """
        ...


class ISmartTagRecognizerSite: # skipped bases: <type 'object'>
    """ no doc """
    def CommitSmartTag(self, SmartTagName:str, Start:int, Length:int, Properties:ISmartTagProperties): # -> 
        """ CommitSmartTag(self: ISmartTagRecognizerSite, SmartTagName: str, Start: int, Length: int, Properties: ISmartTagProperties) """
        ...

    def GetNewPropertyBag(self) -> ISmartTagProperties:
        """ GetNewPropertyBag(self: ISmartTagRecognizerSite) -> ISmartTagProperties """
        ...


class ISmartTagRecognizerSite2(ISmartTagRecognizerSite): # skipped bases: <type 'object'>
    """ no doc """
    def CommitSmartTag2(self, SmartTagName:str, Start:int, Length:int, Properties:ISmartTagProperties) -> int:
        """ CommitSmartTag2(self: ISmartTagRecognizerSite2, SmartTagName: str, Start: int, Length: int, Properties: ISmartTagProperties) -> int """
        ...


class ISmartTagToken: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Length(self) -> int:
        """ Get: Length(self: ISmartTagToken) -> int """
        ...

    @property
    def Properties(self) -> ISmartTagTokenProperties:
        """ Get: Properties(self: ISmartTagToken) -> ISmartTagTokenProperties """
        ...

    @property
    def Start(self) -> int:
        """ Get: Start(self: ISmartTagToken) -> int """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ISmartTagToken) -> str """
        ...



class ISmartTagTokenList: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISmartTagTokenList) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ISmartTagTokenProperties: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISmartTagTokenProperties) -> int """
        ...



class __MIDL___MIDL_itf_mstag_0000_0000_0001(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __MIDL___MIDL_itf_mstag_0000_0000_0001, values: IF_TYPE_CELL (16), IF_TYPE_CHAR (1), IF_TYPE_PARA (8), IF_TYPE_REGEXP (4), IF_TYPE_RUN (32), IF_TYPE_SINGLE_WD (2) """
    IF_TYPE_CELL: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    IF_TYPE_CHAR: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    IF_TYPE_PARA: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    IF_TYPE_REGEXP: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    IF_TYPE_RUN: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    IF_TYPE_SINGLE_WD: __MIDL___MIDL_itf_mstag_0000_0000_0001 = ...
    value__ = ...


class __MIDL___MIDL_itf_mstag_0000_0000_0002(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum __MIDL___MIDL_itf_mstag_0000_0000_0002, values: C_TYPE_ACTIVEX (13), C_TYPE_BUTTON (6), C_TYPE_CHECKBOX (9), C_TYPE_COMBO (12), C_TYPE_DOCUMENTFRAGMENT (14), C_TYPE_DOCUMENTFRAGMENTURL (15), C_TYPE_HELP (3), C_TYPE_HELPURL (4), C_TYPE_IMAGE (8), C_TYPE_LABEL (7), C_TYPE_LINK (2), C_TYPE_LISTBOX (11), C_TYPE_RADIOGROUP (16), C_TYPE_SEPARATOR (5), C_TYPE_TEXTBOX (10) """
    C_TYPE_ACTIVEX: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_BUTTON: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_CHECKBOX: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_COMBO: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_DOCUMENTFRAGMENT: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_DOCUMENTFRAGMENTURL: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_HELP: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_HELPURL: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_IMAGE: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_LABEL: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_LINK: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_LISTBOX: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_RADIOGROUP: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_SEPARATOR: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    C_TYPE_TEXTBOX: __MIDL___MIDL_itf_mstag_0000_0000_0002 = ...
    value__ = ...


