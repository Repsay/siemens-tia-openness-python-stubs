# encoding: utf-8
# module Microsoft.PowerShell.DesiredStateConfiguration.Internal calls itself Internal
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Tuple, Type

from System.Collections import ICollection

from System.Collections.Generic import Dictionary, List

from System.Management.Automation import ErrorRecord, PSModuleInfo

from System.Management.Automation.Language import (DynamicKeyword, 
    IScriptExtent)

from System.Security import SecureString

from typing import Tuple as Tuple_

"""The following names are not found in the module: CimClass, CimInstance
"""

# no functions
# classes

class DscClassCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ClearCache(): # -> 
        """ ClearCache() """
        ...

    @staticmethod
    def ClearImplicitlyImportedFlagFromResourceInClassCache(module:PSModuleInfo, cimClass): # ->  # Not found arg types: {'cimClass': 'CimClass'}
        """ ClearImplicitlyImportedFlagFromResourceInClassCache(module: PSModuleInfo, cimClass: CimClass) """
        ...

    @staticmethod
    def DebugModeShouldHaveOneValue() -> ErrorRecord:
        """ DebugModeShouldHaveOneValue() -> ErrorRecord """
        ...

    @staticmethod
    def DisabledRefreshModeNotValidForPartialConfig(resourceId:str) -> ErrorRecord:
        """ DisabledRefreshModeNotValidForPartialConfig(resourceId: str) -> ErrorRecord """
        ...

    @staticmethod
    def DuplicateResourceIdInNodeStatementErrorRecord(duplicateResourceId:str, nodeName:str) -> ErrorRecord:
        """ DuplicateResourceIdInNodeStatementErrorRecord(duplicateResourceId: str, nodeName: str) -> ErrorRecord """
        ...

    @staticmethod
    def GenerateMofForType(type:Type) -> str:
        """ GenerateMofForType(type: Type) -> str """
        ...

    @staticmethod
    def GetBadlyFormedExclusiveResourceIdErrorRecord(badExclusiveResourcereference:str, definingResource:str) -> ErrorRecord:
        """ GetBadlyFormedExclusiveResourceIdErrorRecord(badExclusiveResourcereference: str, definingResource: str) -> ErrorRecord """
        ...

    @staticmethod
    def GetBadlyFormedRequiredResourceIdErrorRecord(badDependsOnReference:str, definingResource:str) -> ErrorRecord:
        """ GetBadlyFormedRequiredResourceIdErrorRecord(badDependsOnReference: str, definingResource: str) -> ErrorRecord """
        ...

    @staticmethod
    def GetCachedClassByFileName(fileName:str) -> List:
        """ GetCachedClassByFileName(fileName: str) -> List[CimClass] """
        ...

    @staticmethod
    def GetCachedClassByModuleName(moduleName:str) -> List:
        """ GetCachedClassByModuleName(moduleName: str) -> List[CimClass] """
        ...

    @staticmethod
    def GetCachedClassesForModule(module:PSModuleInfo) -> List:
        """ GetCachedClassesForModule(module: PSModuleInfo) -> List[CimClass] """
        ...

    @staticmethod
    def GetCachedKeywords() -> Collection:
        """ GetCachedKeywords() -> Collection[DynamicKeyword] """
        ...

    @staticmethod
    def GetDSCResourceUsageString(keyword:DynamicKeyword) -> str:
        """ GetDSCResourceUsageString(keyword: DynamicKeyword) -> str """
        ...

    @staticmethod
    def GetFileDefiningClass(className:str) -> List:
        """ GetFileDefiningClass(className: str) -> List[str] """
        ...

    @staticmethod
    def GetLoadedFiles() -> Array:
        """ GetLoadedFiles() -> Array[str] """
        ...

    @staticmethod
    def GetPullModeNeedConfigurationSource(resourceId:str) -> ErrorRecord:
        """ GetPullModeNeedConfigurationSource(resourceId: str) -> ErrorRecord """
        ...

    @staticmethod
    def GetResourceMethodsLinePosition(moduleInfo, resourceName, resourceMethodsLinePosition, resourceFilePath) -> Tuple_[bool, Dictionary, str]:
        """ GetResourceMethodsLinePosition(moduleInfo: PSModuleInfo, resourceName: str) -> (bool, Dictionary[str, int], str) """
        ...

    @staticmethod
    def GetStringFromSecureString(value:SecureString) -> str:
        """ GetStringFromSecureString(value: SecureString) -> str """
        ...

    @staticmethod
    def ImportCimKeywordsFromModule(module, resourceName, schemaFilePath, functionsToDefine=None, errors=None) -> Tuple_[bool, str]:
        """
        ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str) -> (bool, str)
        ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary[str, ScriptBlock]) -> (bool, str)
        ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary[str, ScriptBlock], errors: Collection[Exception]) -> (bool, str)
        """
        ...

    @staticmethod
    def ImportClasses(path:str, moduleInfo:Tuple, errors:Collection, importInBoxResourcesImplicitly:bool) -> List:
        """ ImportClasses(path: str, moduleInfo: Tuple[str, Version], errors: Collection[Exception], importInBoxResourcesImplicitly: bool) -> List[CimClass] """
        ...

    @staticmethod
    def ImportClassResourcesFromModule(moduleInfo:PSModuleInfo, resourcesToImport:ICollection, functionsToDefine:Dictionary) -> List:
        """ ImportClassResourcesFromModule(moduleInfo: PSModuleInfo, resourcesToImport: ICollection[str], functionsToDefine: Dictionary[str, ScriptBlock]) -> List[str] """
        ...

    @staticmethod
    def ImportInstances(path:str, schemaValidationOption:int = ...) -> List:
        """
        ImportInstances(path: str) -> List[CimInstance]
        ImportInstances(path: str, schemaValidationOption: int) -> List[CimInstance]
        """
        ...

    @staticmethod
    def ImportScriptKeywordsFromModule(module, resourceName, schemaFilePath, functionsToDefine=None) -> Tuple_[bool, str]:
        """
        ImportScriptKeywordsFromModule(module: PSModuleInfo, resourceName: str) -> (bool, str)
        ImportScriptKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary[str, ScriptBlock]) -> (bool, str)
        """
        ...

    @staticmethod
    def Initialize(errors:Collection = ..., modulePathList:List = ...): # -> 
        """ Initialize()Initialize(errors: Collection[Exception], modulePathList: List[str]) """
        ...

    @staticmethod
    def InvalidConfigurationNameErrorRecord(configurationName:str) -> ErrorRecord:
        """ InvalidConfigurationNameErrorRecord(configurationName: str) -> ErrorRecord """
        ...

    @staticmethod
    def InvalidLocalConfigurationManagerPropertyErrorRecord(propertyName:str, validProperties:str) -> ErrorRecord:
        """ InvalidLocalConfigurationManagerPropertyErrorRecord(propertyName: str, validProperties: str) -> ErrorRecord """
        ...

    @staticmethod
    def InvalidValueForPropertyErrorRecord(propertyName:str, value:str, keywordName:str, validValues:str) -> ErrorRecord:
        """ InvalidValueForPropertyErrorRecord(propertyName: str, value: str, keywordName: str, validValues: str) -> ErrorRecord """
        ...

    @staticmethod
    def LoadDefaultCimKeywords(*__args): # -> 
        """ LoadDefaultCimKeywords()LoadDefaultCimKeywords(modulePathList: List[str])LoadDefaultCimKeywords(errors: Collection[Exception])LoadDefaultCimKeywords(functionsToDefine: Dictionary[str, ScriptBlock])LoadDefaultCimKeywords(errors: Collection[Exception], cacheResourcesFromMultipleModuleVersions: bool) """
        ...

    @staticmethod
    def LoadResourcesFromModule(scriptExtent:IScriptExtent, moduleSpecifications:Array, resourceNames:Array, errorList:List): # -> 
        """ LoadResourcesFromModule(scriptExtent: IScriptExtent, moduleSpecifications: Array[ModuleSpecification], resourceNames: Array[str], errorList: List[ParseError]) """
        ...

    @staticmethod
    def MissingValueForMandatoryPropertyErrorRecord(keywordName:str, typeName:str, propertyName:str) -> ErrorRecord:
        """ MissingValueForMandatoryPropertyErrorRecord(keywordName: str, typeName: str, propertyName: str) -> ErrorRecord """
        ...

    @staticmethod
    def PsDscRunAsCredentialMergeErrorForCompositeResources(resourceId:str) -> ErrorRecord:
        """ PsDscRunAsCredentialMergeErrorForCompositeResources(resourceId: str) -> ErrorRecord """
        ...

    @staticmethod
    def UnsupportedValueForPropertyErrorRecord(propertyName:str, value:str, keywordName:str, validValues:str) -> ErrorRecord:
        """ UnsupportedValueForPropertyErrorRecord(propertyName: str, value: str, keywordName: str, validValues: str) -> ErrorRecord """
        ...

    @staticmethod
    def ValidateInstanceText(instanceText:str): # -> 
        """ ValidateInstanceText(instanceText: str) """
        ...

    @staticmethod
    def ValueNotInRangeErrorRecord(property:str, name:str, providedValue:int, lower:int, upper:int) -> ErrorRecord:
        """ ValueNotInRangeErrorRecord(property: str, name: str, providedValue: int, lower: int, upper: int) -> ErrorRecord """
        ...

    __all__: list = ...


class DscRemoteOperationsClass: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ConvertCimInstanceToObject(targetType:Type, instance, moduleName:str) -> object: # Not found arg types: {'instance': 'CimInstance'}
        """ ConvertCimInstanceToObject(targetType: Type, instance: CimInstance, moduleName: str) -> object """
        ...

    __all__: list = ...


