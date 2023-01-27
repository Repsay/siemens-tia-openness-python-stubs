# encoding: utf-8
# module Microsoft.Scripting.Hosting.Shell calls itself Shell
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting import PlatformAdaptationLayer

from Microsoft.Scripting.Hosting import (CompiledCode, LanguageSetup, 
    ScriptEngine, ScriptRuntime, ScriptRuntimeSetup, ScriptScope)

from System import (Action, Array, ConsoleCancelEventHandler, Enum, 
    IDisposable)

from System.Collections import IList

from System.Collections.Generic import List

from System.IO import TextWriter

from System.Text import StringBuilder

from typing import Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class BasicConsole(IDisposable, IConsole): # skipped bases: <type 'object'>
    """ BasicConsole(colorful: bool) """
    @property
    def ConsoleCancelEventHandler(self) -> ConsoleCancelEventHandler:
        """
        Get: ConsoleCancelEventHandler(self: BasicConsole) -> ConsoleCancelEventHandler
        Set: ConsoleCancelEventHandler(self: BasicConsole) = value
        """
        ...

    @property
    def CreatingThread(self):
        ...

    @property
    def CtrlCEvent(self):
        ...


    def WriteColor(self, *args): #cannot find CLR method
        """ WriteColor(self: BasicConsole, output: TextWriter, str: str, c: ConsoleColor) """
        ...


class CommandLine: # skipped bases: <type 'object'>, <type 'object'>
    """ CommandLine() """
    @property
    def Console(self):
        ...

    @property
    def Engine(self):
        ...

    @property
    def ErrorSink(self):
        ...

    @property
    def ExitCode(self) -> int:
        """ Get: ExitCode(self: CommandLine) -> int """
        ...

    @property
    def Language(self):
        ...

    @property
    def Logo(self):
        ...

    @property
    def Options(self):
        ...

    @property
    def Prompt(self):
        ...

    @property
    def PromptContinuation(self) -> str:
        """ Get: PromptContinuation(self: CommandLine) -> str """
        ...

    @property
    def Scope(self):
        ...

    @property
    def ScriptScope(self) -> ScriptScope:
        """ Get: ScriptScope(self: CommandLine) -> ScriptScope """
        ...


    def CreateCommandDispatcher(self, *args): #cannot find CLR method
        """ CreateCommandDispatcher(self: CommandLine) -> ICommandDispatcher """
        ...

    def CreateScope(self, *args): #cannot find CLR method
        """ CreateScope(self: CommandLine) -> Scope """
        ...

    def ExecuteCommand(self, *args): #cannot find CLR method
        """ ExecuteCommand(self: CommandLine, command: str)ExecuteCommand(self: CommandLine, source: ScriptSource) -> object """
        ...

    def GetCommandProperties(self, *args): #cannot find CLR method
        """ GetCommandProperties(self: CommandLine, code: str) -> ScriptCodeParseResult """
        ...

    def GetGlobals(self, name:str) -> IList:
        """ GetGlobals(self: CommandLine, name: str) -> IList[str] """
        ...

    def GetMemberNames(self, code:str) -> IList:
        """ GetMemberNames(self: CommandLine, code: str) -> IList[str] """
        ...

    def GetNextAutoIndentSize(self, *args): #cannot find CLR method
        """ GetNextAutoIndentSize(self: CommandLine, text: str) -> int """
        ...

    def GetOutputWriter(self, *args): #cannot find CLR method
        """ GetOutputWriter(self: CommandLine, isErrorOutput: bool) -> TextWriter """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: CommandLine) """
        ...

    def PrintLogo(self, *args): #cannot find CLR method
        """ PrintLogo(self: CommandLine) """
        ...

    def ReadLine(self, *args): #cannot find CLR method
        """ ReadLine(self: CommandLine, autoIndentSize: int) -> str """
        ...

    def ReadStatement(self, *args): #cannot find CLR method
        """ ReadStatement(self: CommandLine) -> (str, bool) """
        ...

    def Run(self, engine:ScriptEngine, console:IConsole, options:ConsoleOptions): # -> 
        """ Run(self: CommandLine, engine: ScriptEngine, console: IConsole, options: ConsoleOptions) """
        ...

    def RunCommand(self, *args): #cannot find CLR method
        """ RunCommand(self: CommandLine, command: str) -> int """
        ...

    def RunFile(self, *args): #cannot find CLR method
        """
        RunFile(self: CommandLine, fileName: str) -> int
        RunFile(self: CommandLine, source: ScriptSource) -> int
        """
        ...

    def RunInteractive(self, *args): #cannot find CLR method
        """ RunInteractive(self: CommandLine) -> int """
        ...

    def RunInteractiveLoop(self, *args): #cannot find CLR method
        """ RunInteractiveLoop(self: CommandLine) -> int """
        ...

    def Shutdown(self, *args): #cannot find CLR method
        """ Shutdown(self: CommandLine) """
        ...

    def Terminate(self, exitCode:int): # -> 
        """ Terminate(self: CommandLine, exitCode: int) """
        ...

    def TryInteractiveAction(self, *args): #cannot find CLR method
        """ TryInteractiveAction(self: CommandLine) -> Nullable[int] """
        ...

    def UnhandledException(self, *args): #cannot find CLR method
        """ UnhandledException(self: CommandLine, e: Exception) """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: CommandLine, code: str) -> IList[str] """
        ...


class ConsoleHost: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CommandLine(self):
        ...

    @property
    def ConsoleHostOptionsParser(self):
        ...

    @property
    def ConsoleIO(self):
        ...

    @property
    def Engine(self) -> ScriptEngine:
        """ Get: Engine(self: ConsoleHost) -> ScriptEngine """
        ...

    @property
    def ExeName(self):
        ...

    @property
    def ExitCode(self):
        ...

    @property
    def Options(self) -> ConsoleHostOptions:
        """ Get: Options(self: ConsoleHost) -> ConsoleHostOptions """
        ...

    @property
    def PlatformAdaptationLayer(self):
        ...

    @property
    def Provider(self):
        ...

    @property
    def Runtime(self) -> ScriptRuntime:
        """ Get: Runtime(self: ConsoleHost) -> ScriptRuntime """
        ...

    @property
    def RuntimeSetup(self) -> ScriptRuntimeSetup:
        """ Get: RuntimeSetup(self: ConsoleHost) -> ScriptRuntimeSetup """
        ...


    def CreateCommandLine(self, *args): #cannot find CLR method
        """ CreateCommandLine(self: ConsoleHost) -> CommandLine """
        ...

    def CreateConsole(self, *args): #cannot find CLR method
        """ CreateConsole(self: ConsoleHost, engine: ScriptEngine, commandLine: CommandLine, options: ConsoleOptions) -> IConsole """
        ...

    def CreateLanguageSetup(self, *args): #cannot find CLR method
        """ CreateLanguageSetup(self: ConsoleHost) -> LanguageSetup """
        ...

    def CreateOptionsParser(self, *args): #cannot find CLR method
        """ CreateOptionsParser(self: ConsoleHost) -> OptionsParser """
        ...

    def CreateRuntimeSetup(self, *args): #cannot find CLR method
        """ CreateRuntimeSetup(self: ConsoleHost) -> ScriptRuntimeSetup """
        ...

    def ExecuteInternal(self, *args): #cannot find CLR method
        """ ExecuteInternal(self: ConsoleHost) """
        ...

    def GetHelp(self, *args): #cannot find CLR method
        """ GetHelp(self: ConsoleHost) -> str """
        ...

    def ParseHostOptions(self, *args): #cannot find CLR method
        """ ParseHostOptions(self: ConsoleHost, args: Array[str]) """
        ...

    def ParseOptions(self, *args): #cannot find CLR method
        """ ParseOptions(self: ConsoleHost, args: Array[str], runtimeSetup: ScriptRuntimeSetup, languageSetup: LanguageSetup) -> ConsoleOptions """
        ...

    def PrintException(self, *args): #cannot find CLR method
        """ PrintException(output: TextWriter, e: Exception) """
        ...

    def PrintHelp(self, *args): #cannot find CLR method
        """ PrintHelp(self: ConsoleHost) """
        ...

    def PrintLanguageHelp(self, output:StringBuilder): # -> 
        """ PrintLanguageHelp(self: ConsoleHost, output: StringBuilder) """
        ...

    def PrintUsage(self, *args): #cannot find CLR method
        """ PrintUsage(self: ConsoleHost) """
        ...

    def PrintVersion(self, *args): #cannot find CLR method
        """ PrintVersion(self: ConsoleHost) """
        ...

    def ReportInvalidOption(self, *args): #cannot find CLR method
        """ ReportInvalidOption(self: ConsoleHost, e: InvalidOptionException) """
        ...

    def Run(self, args:Array) -> int:
        """ Run(self: ConsoleHost, args: Array[str]) -> int """
        ...

    def Terminate(self, exitCode:int): # -> 
        """ Terminate(self: ConsoleHost, exitCode: int) """
        ...

    def UnhandledException(self, *args): #cannot find CLR method
        """ UnhandledException(self: ConsoleHost, engine: ScriptEngine, e: Exception) """
        ...


class ConsoleHostOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ ConsoleHostOptions() """
    @property
    def EnvironmentVars(self) -> List:
        """ Get: EnvironmentVars(self: ConsoleHostOptions) -> List[str] """
        ...

    @property
    def HasLanguageProvider(self) -> bool:
        """
        Get: HasLanguageProvider(self: ConsoleHostOptions) -> bool
        Set: HasLanguageProvider(self: ConsoleHostOptions) = value
        """
        ...

    @property
    def IgnoredArgs(self) -> List:
        """ Get: IgnoredArgs(self: ConsoleHostOptions) -> List[str] """
        ...

    @property
    def LanguageProvider(self) -> str:
        """
        Get: LanguageProvider(self: ConsoleHostOptions) -> str
        Set: LanguageProvider(self: ConsoleHostOptions) = value
        """
        ...

    @property
    def RunAction(self) -> Action:
        """
        Get: RunAction(self: ConsoleHostOptions) -> Action
        Set: RunAction(self: ConsoleHostOptions) = value
        """
        ...

    @property
    def RunFile(self) -> str:
        """
        Get: RunFile(self: ConsoleHostOptions) -> str
        Set: RunFile(self: ConsoleHostOptions) = value
        """
        ...

    @property
    def SourceUnitSearchPaths(self) -> Array:
        """
        Get: SourceUnitSearchPaths(self: ConsoleHostOptions) -> Array[str]
        Set: SourceUnitSearchPaths(self: ConsoleHostOptions) = value
        """
        ...


    def Action(self, *args): #cannot find CLR method
        """ enum Action, values: DisplayHelp (3), None (0), RunConsole (1), RunFile (2) """
        ...

    def GetHelp(self) -> Array:
        """ GetHelp(self: ConsoleHostOptions) -> Array[str] """
        ...



class ConsoleHostOptionsParser: # skipped bases: <type 'object'>, <type 'object'>
    """ ConsoleHostOptionsParser(options: ConsoleHostOptions, runtimeSetup: ScriptRuntimeSetup) """
    @property
    def Options(self) -> ConsoleHostOptions:
        """ Get: Options(self: ConsoleHostOptionsParser) -> ConsoleHostOptions """
        ...

    @property
    def RuntimeSetup(self) -> ScriptRuntimeSetup:
        """ Get: RuntimeSetup(self: ConsoleHostOptionsParser) -> ScriptRuntimeSetup """
        ...


    def OptionValueRequired(self, *args): #cannot find CLR method
        """ OptionValueRequired(self: ConsoleHostOptionsParser, optionName: str, value: str) """
        ...

    def Parse(self, args:Array): # -> 
        """ Parse(self: ConsoleHostOptionsParser, args: Array[str]) """
        ...


class ConsoleOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ ConsoleOptions() """
    @property
    def AutoIndent(self) -> bool:
        """
        Get: AutoIndent(self: ConsoleOptions) -> bool
        Set: AutoIndent(self: ConsoleOptions) = value
        """
        ...

    @property
    def AutoIndentSize(self) -> int:
        """
        Get: AutoIndentSize(self: ConsoleOptions) -> int
        Set: AutoIndentSize(self: ConsoleOptions) = value
        """
        ...

    @property
    def ColorfulConsole(self) -> bool:
        """
        Get: ColorfulConsole(self: ConsoleOptions) -> bool
        Set: ColorfulConsole(self: ConsoleOptions) = value
        """
        ...

    @property
    def Command(self) -> str:
        """
        Get: Command(self: ConsoleOptions) -> str
        Set: Command(self: ConsoleOptions) = value
        """
        ...

    @property
    def Exit(self) -> bool:
        """
        Get: Exit(self: ConsoleOptions) -> bool
        Set: Exit(self: ConsoleOptions) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ConsoleOptions) -> str
        Set: FileName(self: ConsoleOptions) = value
        """
        ...

    @property
    def HandleExceptions(self) -> bool:
        """
        Get: HandleExceptions(self: ConsoleOptions) -> bool
        Set: HandleExceptions(self: ConsoleOptions) = value
        """
        ...

    @property
    def Introspection(self) -> bool:
        """
        Get: Introspection(self: ConsoleOptions) -> bool
        Set: Introspection(self: ConsoleOptions) = value
        """
        ...

    @property
    def IsMta(self) -> bool:
        """
        Get: IsMta(self: ConsoleOptions) -> bool
        Set: IsMta(self: ConsoleOptions) = value
        """
        ...

    @property
    def PrintUsage(self) -> bool:
        """
        Get: PrintUsage(self: ConsoleOptions) -> bool
        Set: PrintUsage(self: ConsoleOptions) = value
        """
        ...

    @property
    def PrintVersion(self) -> bool:
        """
        Get: PrintVersion(self: ConsoleOptions) -> bool
        Set: PrintVersion(self: ConsoleOptions) = value
        """
        ...

    @property
    def RemainingArgs(self) -> Array:
        """
        Get: RemainingArgs(self: ConsoleOptions) -> Array[str]
        Set: RemainingArgs(self: ConsoleOptions) = value
        """
        ...

    @property
    def RemoteRuntimeChannel(self) -> str:
        """
        Get: RemoteRuntimeChannel(self: ConsoleOptions) -> str
        Set: RemoteRuntimeChannel(self: ConsoleOptions) = value
        """
        ...

    @property
    def TabCompletion(self) -> bool:
        """
        Get: TabCompletion(self: ConsoleOptions) -> bool
        Set: TabCompletion(self: ConsoleOptions) = value
        """
        ...



class ICommandDispatcher: # skipped bases: <type 'object'>
    """ no doc """
    def Execute(self, compiledCode:CompiledCode, scope:ScriptScope) -> object:
        """ Execute(self: ICommandDispatcher, compiledCode: CompiledCode, scope: ScriptScope) -> object """
        ...


class IConsole: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorOutput(self) -> TextWriter:
        """
        Get: ErrorOutput(self: IConsole) -> TextWriter
        Set: ErrorOutput(self: IConsole) = value
        """
        ...

    @property
    def Output(self) -> TextWriter:
        """
        Get: Output(self: IConsole) -> TextWriter
        Set: Output(self: IConsole) = value
        """
        ...


    def ReadLine(self, autoIndentSize:int) -> str:
        """ ReadLine(self: IConsole, autoIndentSize: int) -> str """
        ...

    def Write(self, text:str, style:Style): # -> 
        """ Write(self: IConsole, text: str, style: Style) """
        ...

    def WriteLine(self, text:str = ..., style:Style = ...): # -> 
        """ WriteLine(self: IConsole, text: str, style: Style)WriteLine(self: IConsole) """
        ...


class InvalidOptionException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidOptionException()
    InvalidOptionException(message: str)
    InvalidOptionException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class OptionsParser: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommonConsoleOptions(self) -> ConsoleOptions:
        """ Get: CommonConsoleOptions(self: OptionsParser) -> ConsoleOptions """
        ...

    @property
    def IgnoredArgs(self) -> IList:
        """ Get: IgnoredArgs(self: OptionsParser) -> IList[str] """
        ...

    @property
    def LanguageSetup(self) -> LanguageSetup:
        """ Get: LanguageSetup(self: OptionsParser) -> LanguageSetup """
        ...

    @property
    def Platform(self) -> PlatformAdaptationLayer:
        """ Get: Platform(self: OptionsParser) -> PlatformAdaptationLayer """
        ...

    @property
    def RuntimeSetup(self) -> ScriptRuntimeSetup:
        """ Get: RuntimeSetup(self: OptionsParser) -> ScriptRuntimeSetup """
        ...


    def AfterParse(self, *args): #cannot find CLR method
        """ AfterParse(self: OptionsParser) """
        ...

    def BeforeParse(self, *args): #cannot find CLR method
        """ BeforeParse(self: OptionsParser) """
        ...

    def GetHelp(self, commandLine, options, environmentVariables, comments) -> Tuple_[str, Array, Array, str]:
        """ GetHelp(self: OptionsParser) -> (str, Array[str], Array[str], str) """
        ...

    def IgnoreRemainingArgs(self, *args): #cannot find CLR method
        """ IgnoreRemainingArgs(self: OptionsParser) """
        ...

    def InvalidOptionValue(self, *args): #cannot find CLR method
        """ InvalidOptionValue(option: str, value: str) -> Exception """
        ...

    def Parse(self, args:Array, setup:ScriptRuntimeSetup, languageSetup:LanguageSetup, platform:PlatformAdaptationLayer): # -> 
        """ Parse(self: OptionsParser, args: Array[str], setup: ScriptRuntimeSetup, languageSetup: LanguageSetup, platform: PlatformAdaptationLayer) """
        ...

    def ParseArgument(self, *args): #cannot find CLR method
        """ ParseArgument(self: OptionsParser, arg: str) """
        ...

    def PeekNextArg(self, *args): #cannot find CLR method
        """ PeekNextArg(self: OptionsParser) -> str """
        ...

    def PopNextArg(self, *args): #cannot find CLR method
        """ PopNextArg(self: OptionsParser) -> str """
        ...

    def PopRemainingArgs(self, *args): #cannot find CLR method
        """ PopRemainingArgs(self: OptionsParser) -> Array[str] """
        ...

    def PushArgBack(self, *args): #cannot find CLR method
        """ PushArgBack(self: OptionsParser) """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class Style(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Style, values: Error (2), Out (1), Prompt (0), Warning (3) """
    Error: Style = ...
    Out: Style = ...
    Prompt: Style = ...
    value__ = ...
    Warning: Style = ...


class SuperConsole(BasicConsole): # skipped bases: <type 'IDisposable'>, <type 'IConsole'>, <type 'object'>
    """ SuperConsole(commandLine: CommandLine, colorful: bool) """
    pass

# variables with complex values

