# encoding: utf-8
# module System.Web.Handlers calls itself Handlers
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Web import IHttpHandler, IHttpModule


# no functions
# classes

class AssemblyResourceLoader(IHttpHandler): # skipped bases: <type 'object'>
    """ AssemblyResourceLoader() """
    pass

class ScriptModule(IHttpModule): # skipped bases: <type 'object'>
    """ ScriptModule() """
    pass

class ScriptResourceHandler(IHttpHandler): # skipped bases: <type 'object'>
    """ ScriptResourceHandler() """
    pass

class TraceHandler(IHttpHandler): # skipped bases: <type 'object'>
    """ TraceHandler() """
    def ShowDetails(self, *args): #cannot find CLR method
        """ ShowDetails(self: TraceHandler, data: DataSet) """
        ...

    def ShowRequests(self, *args): #cannot find CLR method
        """ ShowRequests(self: TraceHandler, data: IList) """
        ...

    def ShowVersionDetails(self, *args): #cannot find CLR method
        """ ShowVersionDetails(self: TraceHandler) """
        ...


