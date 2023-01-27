# encoding: utf-8
# module System.Web.Util calls itself Util
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import AsyncCallback, Enum, IAsyncResult, MulticastDelegate

from System.EnterpriseServices import TransactionOption

from System.Web import HttpContext

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class HttpEncoder: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpEncoder() """
    @property
    def Current(self) -> HttpEncoder:
        """
        Get: Current() -> HttpEncoder
        Set: Current() = value
        """
        ...

    @property
    def Default(self) -> HttpEncoder:
        """ Get: Default() -> HttpEncoder """
        ...


    def HeaderNameValueEncode(self, *args): #cannot find CLR method
        """ HeaderNameValueEncode(self: HttpEncoder, headerName: str, headerValue: str) -> (str, str) """
        ...

    def HtmlAttributeEncode(self, *args): #cannot find CLR method
        """ HtmlAttributeEncode(self: HttpEncoder, value: str, output: TextWriter) """
        ...

    def HtmlDecode(self, *args): #cannot find CLR method
        """ HtmlDecode(self: HttpEncoder, value: str, output: TextWriter) """
        ...

    def HtmlEncode(self, *args): #cannot find CLR method
        """ HtmlEncode(self: HttpEncoder, value: str, output: TextWriter) """
        ...

    def JavaScriptStringEncode(self, *args): #cannot find CLR method
        """ JavaScriptStringEncode(self: HttpEncoder, value: str) -> str """
        ...

    def UrlEncode(self, *args): #cannot find CLR method
        """ UrlEncode(self: HttpEncoder, bytes: Array[Byte], offset: int, count: int) -> Array[Byte] """
        ...

    def UrlPathEncode(self, *args): #cannot find CLR method
        """ UrlPathEncode(self: HttpEncoder, value: str) -> str """
        ...



class IWebObjectFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstance(self) -> object:
        """ CreateInstance(self: IWebObjectFactory) -> object """
        ...


class IWebPropertyAccessor: # skipped bases: <type 'object'>
    """ no doc """
    def GetProperty(self, target:object) -> object:
        """ GetProperty(self: IWebPropertyAccessor, target: object) -> object """
        ...

    def SetProperty(self, target:object, value:object): # -> 
        """ SetProperty(self: IWebPropertyAccessor, target: object, value: object) """
        ...


class RequestValidationSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RequestValidationSource, values: Cookies (2), Files (3), Form (1), Headers (7), Path (5), PathInfo (6), QueryString (0), RawUrl (4) """
    Cookies: RequestValidationSource = ...
    Files: RequestValidationSource = ...
    Form: RequestValidationSource = ...
    Headers: RequestValidationSource = ...
    Path: RequestValidationSource = ...
    PathInfo: RequestValidationSource = ...
    QueryString: RequestValidationSource = ...
    RawUrl: RequestValidationSource = ...
    value__ = ...


class RequestValidator: # skipped bases: <type 'object'>, <type 'object'>
    """ RequestValidator() """
    @property
    def Current(self) -> RequestValidator:
        """
        Get: Current() -> RequestValidator
        Set: Current() = value
        """
        ...


    def InvokeIsValidRequestString(self, context, value, requestValidationSource, collectionKey, validationFailureIndex) -> Tuple_[bool, int]:
        """ InvokeIsValidRequestString(self: RequestValidator, context: HttpContext, value: str, requestValidationSource: RequestValidationSource, collectionKey: str) -> (bool, int) """
        ...

    def IsValidRequestString(self, *args): #cannot find CLR method
        """ IsValidRequestString(self: RequestValidator, context: HttpContext, value: str, requestValidationSource: RequestValidationSource, collectionKey: str) -> (bool, int) """
        ...



class TransactedCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TransactedCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TransactedCallback, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TransactedCallback, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: TransactedCallback) """
        ...


class Transactions: # skipped bases: <type 'object'>, <type 'object'>
    """ Transactions() """
    @staticmethod
    def InvokeTransacted(callback:TransactedCallback, mode:TransactionOption, transactionAborted:bool = ...) -> bool:
        """ InvokeTransacted(callback: TransactedCallback, mode: TransactionOption)InvokeTransacted(callback: TransactedCallback, mode: TransactionOption, transactionAborted: bool) -> bool """
        ...


class WorkItem: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkItem() """
    @staticmethod
    def Post(callback:WorkItemCallback): # -> 
        """ Post(callback: WorkItemCallback) """
        ...


class WorkItemCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WorkItemCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WorkItemCallback, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WorkItemCallback, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: WorkItemCallback) """
        ...


