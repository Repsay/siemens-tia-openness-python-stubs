# encoding: utf-8
# module System.Text.RegularExpressions calls itself RegularExpressions
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, IAsyncResult, 
    MulticastDelegate, TimeSpan, TimeoutException)

from System.Collections import ICollection, IEnumerator

from System.Reflection import AssemblyName

from System.Runtime.Serialization import ISerializable

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Capture: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: Capture) -> int """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: Capture) -> int """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: Capture) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: Capture) -> str """
        ...


class CaptureCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: CaptureCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CaptureCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class Group(Capture): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Captures(self) -> CaptureCollection:
        """ Get: Captures(self: Group) -> CaptureCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Group) -> str """
        ...

    @property
    def Success(self) -> bool:
        """ Get: Success(self: Group) -> bool """
        ...


    @staticmethod
    def Synchronized(inner:Group) -> Group:
        """ Synchronized(inner: Group) -> Group """
        ...


class GroupCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: GroupCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: GroupCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class Match(Group): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Empty(self) -> Match:
        """ Get: Empty() -> Match """
        ...

    @property
    def Groups(self) -> GroupCollection:
        """ Get: Groups(self: Match) -> GroupCollection """
        ...


    def NextMatch(self) -> Match:
        """ NextMatch(self: Match) -> Match """
        ...

    def Result(self, replacement:str) -> str:
        """ Result(self: Match, replacement: str) -> str """
        ...



class MatchCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: MatchCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MatchCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class MatchEvaluator(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MatchEvaluator(object: object, method: IntPtr) """
    def BeginInvoke(self, match:Match, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MatchEvaluator, match: Match, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> str:
        """ EndInvoke(self: MatchEvaluator, result: IAsyncResult) -> str """
        ...

    def Invoke(self, match:Match) -> str:
        """ Invoke(self: MatchEvaluator, match: Match) -> str """
        ...


class Regex(ISerializable): # skipped bases: <type 'object'>
    """
    Regex(pattern: str)
    Regex(pattern: str, options: RegexOptions)
    Regex(pattern: str, options: RegexOptions, matchTimeout: TimeSpan)
    """
    @property
    def CacheSize(self) -> int:
        """
        Get: CacheSize() -> int
        Set: CacheSize() = value
        """
        ...

    @property
    def CapNames(self):
        ...

    @property
    def Caps(self):
        ...

    @property
    def MatchTimeout(self) -> TimeSpan:
        """ Get: MatchTimeout(self: Regex) -> TimeSpan """
        ...

    @property
    def Options(self) -> RegexOptions:
        """ Get: Options(self: Regex) -> RegexOptions """
        ...

    @property
    def RightToLeft(self) -> bool:
        """ Get: RightToLeft(self: Regex) -> bool """
        ...


    @staticmethod
    def CompileToAssembly(regexinfos:Array, assemblyname:AssemblyName, attributes:Array = ..., resourceFile:str = ...): # -> 
        """ CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName)CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder])CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder], resourceFile: str) """
        ...

    @staticmethod
    def Escape(str:str) -> str:
        """ Escape(str: str) -> str """
        ...

    def GetGroupNames(self) -> Array:
        """ GetGroupNames(self: Regex) -> Array[str] """
        ...

    def GetGroupNumbers(self) -> Array:
        """ GetGroupNumbers(self: Regex) -> Array[int] """
        ...

    def GroupNameFromNumber(self, i:int) -> str:
        """ GroupNameFromNumber(self: Regex, i: int) -> str """
        ...

    def GroupNumberFromName(self, name:str) -> int:
        """ GroupNumberFromName(self: Regex, name: str) -> int """
        ...

    def InitializeReferences(self, *args): #cannot find CLR method
        """ InitializeReferences(self: Regex) """
        ...

    @staticmethod
    def IsMatch(input:Regex, *__args:str) -> bool:
        """
        IsMatch(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> bool
        IsMatch(self: Regex, input: str) -> bool
        IsMatch(self: Regex, input: str, startat: int) -> bool
        IsMatch(input: str, pattern: str) -> bool
        IsMatch(input: str, pattern: str, options: RegexOptions) -> bool
        """
        ...

    @staticmethod
    def Match(input:Regex, *__args:str) -> Match:
        """
        Match(input: str, pattern: str, options: RegexOptions) -> Match
        Match(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Match
        Match(self: Regex, input: str) -> Match
        Match(self: Regex, input: str, startat: int) -> Match
        Match(self: Regex, input: str, beginning: int, length: int) -> Match
        Match(input: str, pattern: str) -> Match
        """
        ...

    @staticmethod
    def Matches(input:Regex, *__args:str) -> MatchCollection:
        """
        Matches(input: str, pattern: str, options: RegexOptions) -> MatchCollection
        Matches(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> MatchCollection
        Matches(self: Regex, input: str) -> MatchCollection
        Matches(self: Regex, input: str, startat: int) -> MatchCollection
        Matches(input: str, pattern: str) -> MatchCollection
        """
        ...

    @staticmethod
    def Replace(input, *__args) -> str:
        """
        Replace(input: str, pattern: str, replacement: str) -> str
        Replace(input: str, pattern: str, replacement: str, options: RegexOptions) -> str
        Replace(input: str, pattern: str, replacement: str, options: RegexOptions, matchTimeout: TimeSpan) -> str
        Replace(self: Regex, input: str, replacement: str) -> str
        Replace(self: Regex, input: str, replacement: str, count: int) -> str
        Replace(self: Regex, input: str, replacement: str, count: int, startat: int) -> str
        Replace(input: str, pattern: str, evaluator: MatchEvaluator) -> str
        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions) -> str
        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions, matchTimeout: TimeSpan) -> str
        Replace(self: Regex, input: str, evaluator: MatchEvaluator) -> str
        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int) -> str
        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int, startat: int) -> str
        """
        ...

    @staticmethod
    def Split(input:str, *__args:str) -> Array:
        """
        Split(input: str, pattern: str) -> Array[str]
        Split(input: str, pattern: str, options: RegexOptions) -> Array[str]
        Split(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Array[str]
        Split(self: Regex, input: str) -> Array[str]
        Split(self: Regex, input: str, count: int) -> Array[str]
        Split(self: Regex, input: str, count: int, startat: int) -> Array[str]
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: Regex) -> str """
        ...

    @staticmethod
    def Unescape(str:str) -> str:
        """ Unescape(str: str) -> str """
        ...

    def UseOptionC(self, *args): #cannot find CLR method
        """ UseOptionC(self: Regex) -> bool """
        ...

    def UseOptionR(self, *args): #cannot find CLR method
        """ UseOptionR(self: Regex) -> bool """
        ...

    def ValidateMatchTimeout(self, *args): #cannot find CLR method
        """ ValidateMatchTimeout(matchTimeout: TimeSpan) """
        ...

    capnames = ...
    caps = ...
    capsize = ...
    capslist = ...
    factory = ...
    InfiniteMatchTimeout: TimeSpan = ...
    internalMatchTimeout = ...
    pattern = ...
    roptions = ...


class RegexCompilationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool)
    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool, matchTimeout: TimeSpan)
    """
    @property
    def IsPublic(self) -> bool:
        """
        Get: IsPublic(self: RegexCompilationInfo) -> bool
        Set: IsPublic(self: RegexCompilationInfo) = value
        """
        ...

    @property
    def MatchTimeout(self) -> TimeSpan:
        """
        Get: MatchTimeout(self: RegexCompilationInfo) -> TimeSpan
        Set: MatchTimeout(self: RegexCompilationInfo) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: RegexCompilationInfo) -> str
        Set: Name(self: RegexCompilationInfo) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: RegexCompilationInfo) -> str
        Set: Namespace(self: RegexCompilationInfo) = value
        """
        ...

    @property
    def Options(self) -> RegexOptions:
        """
        Get: Options(self: RegexCompilationInfo) -> RegexOptions
        Set: Options(self: RegexCompilationInfo) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """
        Get: Pattern(self: RegexCompilationInfo) -> str
        Set: Pattern(self: RegexCompilationInfo) = value
        """
        ...



class RegexMatchTimeoutException(TimeoutException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RegexMatchTimeoutException(regexInput: str, regexPattern: str, matchTimeout: TimeSpan)
    RegexMatchTimeoutException()
    RegexMatchTimeoutException(message: str)
    RegexMatchTimeoutException(message: str, inner: Exception)
    """
    @property
    def Input(self) -> str:
        """ Get: Input(self: RegexMatchTimeoutException) -> str """
        ...

    @property
    def MatchTimeout(self) -> TimeSpan:
        """ Get: MatchTimeout(self: RegexMatchTimeoutException) -> TimeSpan """
        ...

    @property
    def Pattern(self) -> str:
        """ Get: Pattern(self: RegexMatchTimeoutException) -> str """
        ...


    SerializeObjectState = ...


class RegexOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegexOptions, values: Compiled (8), CultureInvariant (512), ECMAScript (256), ExplicitCapture (4), IgnoreCase (1), IgnorePatternWhitespace (32), Multiline (2), None (0), RightToLeft (64), Singleline (16) """
    Compiled: RegexOptions = ...
    CultureInvariant: RegexOptions = ...
    ECMAScript: RegexOptions = ...
    ExplicitCapture: RegexOptions = ...
    IgnoreCase: RegexOptions = ...
    IgnorePatternWhitespace: RegexOptions = ...
    Multiline: RegexOptions = ...
    RightToLeft: RegexOptions = ...
    Singleline: RegexOptions = ...
    value__ = ...


class RegexRunner: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Capture(self, *args): #cannot find CLR method
        """ Capture(self: RegexRunner, capnum: int, start: int, end: int) """
        ...

    def CharInClass(self, *args): #cannot find CLR method
        """ CharInClass(ch: Char, charClass: str) -> bool """
        ...

    def CharInSet(self, *args): #cannot find CLR method
        """ CharInSet(ch: Char, set: str, category: str) -> bool """
        ...

    def CheckTimeout(self, *args): #cannot find CLR method
        """ CheckTimeout(self: RegexRunner) """
        ...

    def Crawl(self, *args): #cannot find CLR method
        """ Crawl(self: RegexRunner, i: int) """
        ...

    def Crawlpos(self, *args): #cannot find CLR method
        """ Crawlpos(self: RegexRunner) -> int """
        ...

    def DoubleCrawl(self, *args): #cannot find CLR method
        """ DoubleCrawl(self: RegexRunner) """
        ...

    def DoubleStack(self, *args): #cannot find CLR method
        """ DoubleStack(self: RegexRunner) """
        ...

    def DoubleTrack(self, *args): #cannot find CLR method
        """ DoubleTrack(self: RegexRunner) """
        ...

    def EnsureStorage(self, *args): #cannot find CLR method
        """ EnsureStorage(self: RegexRunner) """
        ...

    def FindFirstChar(self, *args): #cannot find CLR method
        """ FindFirstChar(self: RegexRunner) -> bool """
        ...

    def Go(self, *args): #cannot find CLR method
        """ Go(self: RegexRunner) """
        ...

    def InitTrackCount(self, *args): #cannot find CLR method
        """ InitTrackCount(self: RegexRunner) """
        ...

    def IsBoundary(self, *args): #cannot find CLR method
        """ IsBoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool """
        ...

    def IsECMABoundary(self, *args): #cannot find CLR method
        """ IsECMABoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool """
        ...

    def IsMatched(self, *args): #cannot find CLR method
        """ IsMatched(self: RegexRunner, cap: int) -> bool """
        ...

    def MatchIndex(self, *args): #cannot find CLR method
        """ MatchIndex(self: RegexRunner, cap: int) -> int """
        ...

    def MatchLength(self, *args): #cannot find CLR method
        """ MatchLength(self: RegexRunner, cap: int) -> int """
        ...

    def Popcrawl(self, *args): #cannot find CLR method
        """ Popcrawl(self: RegexRunner) -> int """
        ...

    def Scan(self, *args): #cannot find CLR method
        """
        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool) -> Match
        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool, timeout: TimeSpan) -> Match
        """
        ...

    def TransferCapture(self, *args): #cannot find CLR method
        """ TransferCapture(self: RegexRunner, capnum: int, uncapnum: int, start: int, end: int) """
        ...

    def Uncapture(self, *args): #cannot find CLR method
        """ Uncapture(self: RegexRunner) """
        ...

    runcrawl = ...
    runcrawlpos = ...
    runmatch = ...
    runregex = ...
    runstack = ...
    runstackpos = ...
    runtext = ...
    runtextbeg = ...
    runtextend = ...
    runtextpos = ...
    runtextstart = ...
    runtrack = ...
    runtrackcount = ...
    runtrackpos = ...


class RegexRunnerFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: RegexRunnerFactory) -> RegexRunner """
        ...


