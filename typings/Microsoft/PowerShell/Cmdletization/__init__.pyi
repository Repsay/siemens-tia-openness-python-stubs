# encoding: utf-8
# module Microsoft.PowerShell.Cmdletization calls itself Cmdletization
# from Microsoft.PowerShell.Commands.Management, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, IDisposable, Type, Version

from System.Collections import IDictionary, IEnumerable

from System.Collections.ObjectModel import KeyedCollection

from System.Management.Automation import PSCmdlet, SwitchParameter

"""The following names are not found in the module: (MethodParameter, 
    MethodParameterBindings, QueryBuilder, field#)
"""

# no functions
# classes

class BehaviorOnNoMatch(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BehaviorOnNoMatch, values: Default (0), ReportErrors (1), SilentlyContinue (2) """
    Default: BehaviorOnNoMatch = ...
    ReportErrors: BehaviorOnNoMatch = ...
    SilentlyContinue: BehaviorOnNoMatch = ...
    value__ = ...


class CmdletAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClassName(self) -> str:
        """ Get: ClassName(self: CmdletAdapter[TObjectInstance]) -> str """
        ...

    @property
    def ClassVersion(self) -> str:
        """ Get: ClassVersion(self: CmdletAdapter[TObjectInstance]) -> str """
        ...

    @property
    def Cmdlet(self) -> PSCmdlet:
        """ Get: Cmdlet(self: CmdletAdapter[TObjectInstance]) -> PSCmdlet """
        ...

    @property
    def ModuleVersion(self) -> Version:
        """ Get: ModuleVersion(self: CmdletAdapter[TObjectInstance]) -> Version """
        ...

    @property
    def PrivateData(self) -> IDictionary:
        """ Get: PrivateData(self: CmdletAdapter[TObjectInstance]) -> IDictionary[str, str] """
        ...


    def BeginProcessing(self): # -> 
        """ BeginProcessing(self: CmdletAdapter[TObjectInstance]) """
        ...

    def EndProcessing(self): # -> 
        """ EndProcessing(self: CmdletAdapter[TObjectInstance]) """
        ...

    def GetQueryBuilder(self): # -> QueryBuilder
        """ GetQueryBuilder(self: CmdletAdapter[TObjectInstance]) -> QueryBuilder """
        ...

    def Initialize(self, cmdlet:PSCmdlet, className:str, classVersion:str, moduleVersion:Version, privateData:IDictionary): # -> 
        """ Initialize(self: CmdletAdapter[TObjectInstance], cmdlet: PSCmdlet, className: str, classVersion: str, moduleVersion: Version, privateData: IDictionary[str, str]) """
        ...

    def ProcessRecord(self, *__args): # ->  # Not found arg types: {'*__args': 'QueryBuilder'}
        """ ProcessRecord(self: CmdletAdapter[TObjectInstance], query: QueryBuilder)ProcessRecord(self: CmdletAdapter[TObjectInstance], objectInstance: TObjectInstance, methodInvocationInfo: MethodInvocationInfo, passThru: bool)ProcessRecord(self: CmdletAdapter[TObjectInstance], query: QueryBuilder, methodInvocationInfo: MethodInvocationInfo, passThru: bool)ProcessRecord(self: CmdletAdapter[TObjectInstance], methodInvocationInfo: MethodInvocationInfo) """
        ...

    def StopProcessing(self): # -> 
        """ StopProcessing(self: CmdletAdapter[TObjectInstance]) """
        ...


class MethodInvocationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ MethodInvocationInfo(name: str, parameters: IEnumerable[MethodParameter], returnValue: MethodParameter) """
    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: MethodInvocationInfo) -> str """
        ...

    @property
    def Parameters(self) -> KeyedCollection:
        """ Get: Parameters(self: MethodInvocationInfo) -> KeyedCollection[str, MethodParameter] """
        ...

    @property
    def ReturnValue(self): # -> MethodParameter
        """ Get: ReturnValue(self: MethodInvocationInfo) -> MethodParameter """
        ...



class MethodParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ MethodParameter() """
    @property
    def Bindings(self): # -> MethodParameterBindings
        """
        Get: Bindings(self: MethodParameter) -> MethodParameterBindings
        Set: Bindings(self: MethodParameter) = value
        """
        ...

    @property
    def IsValuePresent(self) -> bool:
        """
        Get: IsValuePresent(self: MethodParameter) -> bool
        Set: IsValuePresent(self: MethodParameter) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: MethodParameter) -> str
        Set: Name(self: MethodParameter) = value
        """
        ...

    @property
    def ParameterType(self) -> Type:
        """
        Get: ParameterType(self: MethodParameter) -> Type
        Set: ParameterType(self: MethodParameter) = value
        """
        ...

    @property
    def ParameterTypeName(self) -> str:
        """
        Get: ParameterTypeName(self: MethodParameter) -> str
        Set: ParameterTypeName(self: MethodParameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: MethodParameter) -> object
        Set: Value(self: MethodParameter) = value
        """
        ...



class MethodParameterBindings(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MethodParameterBindings, values: Error (4), In (1), Out (2) """
    Error: MethodParameterBindings = ...
    In: MethodParameterBindings = ...
    Out: MethodParameterBindings = ...
    value__ = ...


class QueryBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddQueryOption(self, optionName:str, optionValue:object): # -> 
        """ AddQueryOption(self: QueryBuilder, optionName: str, optionValue: object) """
        ...

    def ExcludeByProperty(self, propertyName:str, excludedPropertyValues:IEnumerable, wildcardsEnabled:bool, behaviorOnNoMatch:BehaviorOnNoMatch): # -> 
        """ ExcludeByProperty(self: QueryBuilder, propertyName: str, excludedPropertyValues: IEnumerable, wildcardsEnabled: bool, behaviorOnNoMatch: BehaviorOnNoMatch) """
        ...

    def FilterByAssociatedInstance(self, associatedInstance:object, associationName:str, sourceRole:str, resultRole:str, behaviorOnNoMatch:BehaviorOnNoMatch): # -> 
        """ FilterByAssociatedInstance(self: QueryBuilder, associatedInstance: object, associationName: str, sourceRole: str, resultRole: str, behaviorOnNoMatch: BehaviorOnNoMatch) """
        ...

    def FilterByMaxPropertyValue(self, propertyName:str, maxPropertyValue:object, behaviorOnNoMatch:BehaviorOnNoMatch): # -> 
        """ FilterByMaxPropertyValue(self: QueryBuilder, propertyName: str, maxPropertyValue: object, behaviorOnNoMatch: BehaviorOnNoMatch) """
        ...

    def FilterByMinPropertyValue(self, propertyName:str, minPropertyValue:object, behaviorOnNoMatch:BehaviorOnNoMatch): # -> 
        """ FilterByMinPropertyValue(self: QueryBuilder, propertyName: str, minPropertyValue: object, behaviorOnNoMatch: BehaviorOnNoMatch) """
        ...

    def FilterByProperty(self, propertyName:str, allowedPropertyValues:IEnumerable, wildcardsEnabled:bool, behaviorOnNoMatch:BehaviorOnNoMatch): # -> 
        """ FilterByProperty(self: QueryBuilder, propertyName: str, allowedPropertyValues: IEnumerable, wildcardsEnabled: bool, behaviorOnNoMatch: BehaviorOnNoMatch) """
        ...


class SessionBasedCmdletAdapter(IDisposable, CmdletAdapter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AsJob(self) -> SwitchParameter:
        """
        Get: AsJob(self: SessionBasedCmdletAdapter[TObjectInstance, TSession]) -> SwitchParameter
        Set: AsJob(self: SessionBasedCmdletAdapter[TObjectInstance, TSession]) = value
        """
        ...

    @property
    def DefaultSession(self):
        ...

    @property
    def Session(self):
        ...

    @property
    def ThrottleLimit(self) -> int:
        """
        Get: ThrottleLimit(self: SessionBasedCmdletAdapter[TObjectInstance, TSession]) -> int
        Set: ThrottleLimit(self: SessionBasedCmdletAdapter[TObjectInstance, TSession]) = value
        """
        ...


    def GenerateParentJobName(self, *args): #cannot find CLR method
        """ GenerateParentJobName(self: SessionBasedCmdletAdapter[TObjectInstance, TSession]) -> str """
        ...


# variables with complex values

