# encoding: utf-8
# module Microsoft.Scripting.Hosting.Providers calls itself Providers
# from Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting import ScriptCode, SourceUnit

from Microsoft.Scripting.Hosting import (CompiledCode, 
    DocumentationOperations, ScriptEngine, ScriptIO, ScriptRuntime, 
    ScriptScope, ScriptSource)

from Microsoft.Scripting.Runtime import (DocumentationProvider, 
    LanguageContext, ScriptDomainManager, SharedIO)

from System.IdentityModel import Scope

"""The following names are not found in the module: Func, T, TRet
"""

# no functions
# classes

class HostingHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CallEngine(engine:ScriptEngine, f, arg): # -> TRet # Not found arg types: {'arg': 'T', 'f': 'Func'}
        """ CallEngine[(T, TRet)](engine: ScriptEngine, f: Func[LanguageContext, T, TRet], arg: T) -> TRet """
        ...

    @staticmethod
    def CreateDocumentationOperations(provider:DocumentationProvider) -> DocumentationOperations:
        """ CreateDocumentationOperations(provider: DocumentationProvider) -> DocumentationOperations """
        ...

    @staticmethod
    def CreateScriptScope(engine:ScriptEngine, scope:Scope) -> ScriptScope:
        """ CreateScriptScope(engine: ScriptEngine, scope: Scope) -> ScriptScope """
        ...

    @staticmethod
    def GetDomainManager(runtime:ScriptRuntime) -> ScriptDomainManager:
        """ GetDomainManager(runtime: ScriptRuntime) -> ScriptDomainManager """
        ...

    @staticmethod
    def GetLanguageContext(engine:ScriptEngine) -> LanguageContext:
        """ GetLanguageContext(engine: ScriptEngine) -> LanguageContext """
        ...

    @staticmethod
    def GetScope(scriptScope:ScriptScope) -> Scope:
        """ GetScope(scriptScope: ScriptScope) -> Scope """
        ...

    @staticmethod
    def GetScriptCode(compiledCode:CompiledCode) -> ScriptCode:
        """ GetScriptCode(compiledCode: CompiledCode) -> ScriptCode """
        ...

    @staticmethod
    def GetSharedIO(io:ScriptIO) -> SharedIO:
        """ GetSharedIO(io: ScriptIO) -> SharedIO """
        ...

    @staticmethod
    def GetSourceUnit(scriptSource:ScriptSource) -> SourceUnit:
        """ GetSourceUnit(scriptSource: ScriptSource) -> SourceUnit """
        ...

    __all__: list = ...


