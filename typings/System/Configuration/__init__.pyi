# encoding: utf-8
# module System.Configuration calls itself Configuration
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Configuration.Install, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    GenericUriParserOptions, IAsyncResult, ICloneable, Int64, 
    MulticastDelegate, SystemException, TimeSpan, Type, UriIdnScope)

from System.Collections import (Hashtable, ICollection, IEnumerator, 
    ReadOnlyCollectionBase)

from System.Collections.Specialized import (NameObjectCollectionBase, 
    NameValueCollection, StringCollection)

from System.ComponentModel import (CancelEventArgs, INotifyPropertyChanged, 
    ITypeDescriptorContext, TypeConverter)

from System.Configuration.Internal import IConfigErrorInfo

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.Globalization import CultureInfo

from System.Runtime.Versioning import FrameworkName

from System.Security import CodeAccessPermission, IPermission

from System.Security.Cryptography import RSAParameters

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Xml import XmlDocument, XmlNode, XmlTextReader

from typing import Self

"""The following names are not found in the module: BoundEvent, Func, field#
"""

# no functions
# classes

class SettingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingAttribute() """
    pass

class ApplicationScopedSettingAttribute(SettingAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ApplicationScopedSettingAttribute() """
    pass

class SettingsBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Context(self) -> SettingsContext:
        """ Get: Context(self: SettingsBase) -> SettingsContext """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: SettingsBase) -> bool """
        ...

    @property
    def Properties(self) -> SettingsPropertyCollection:
        """ Get: Properties(self: SettingsBase) -> SettingsPropertyCollection """
        ...

    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:
        """ Get: PropertyValues(self: SettingsBase) -> SettingsPropertyValueCollection """
        ...

    @property
    def Providers(self) -> SettingsProviderCollection:
        """ Get: Providers(self: SettingsBase) -> SettingsProviderCollection """
        ...


    def Initialize(self, context:SettingsContext, properties:SettingsPropertyCollection, providers:SettingsProviderCollection): # -> 
        """ Initialize(self: SettingsBase, context: SettingsContext, properties: SettingsPropertyCollection, providers: SettingsProviderCollection) """
        ...

    def Save(self): # -> 
        """ Save(self: SettingsBase) """
        ...

    @staticmethod
    def Synchronized(settingsBase:SettingsBase) -> SettingsBase:
        """ Synchronized(settingsBase: SettingsBase) -> SettingsBase """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ApplicationSettingsBase(SettingsBase, INotifyPropertyChanged): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SettingsKey(self) -> str:
        """
        Get: SettingsKey(self: ApplicationSettingsBase) -> str
        Set: SettingsKey(self: ApplicationSettingsBase) = value
        """
        ...


    def GetPreviousVersion(self, propertyName:str) -> object:
        """ GetPreviousVersion(self: ApplicationSettingsBase, propertyName: str) -> object """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """ OnPropertyChanged(self: ApplicationSettingsBase, sender: object, e: PropertyChangedEventArgs) """
        ...

    def OnSettingChanging(self, *args): #cannot find CLR method
        """ OnSettingChanging(self: ApplicationSettingsBase, sender: object, e: SettingChangingEventArgs) """
        ...

    def OnSettingsLoaded(self, *args): #cannot find CLR method
        """ OnSettingsLoaded(self: ApplicationSettingsBase, sender: object, e: SettingsLoadedEventArgs) """
        ...

    def OnSettingsSaving(self, *args): #cannot find CLR method
        """ OnSettingsSaving(self: ApplicationSettingsBase, sender: object, e: CancelEventArgs) """
        ...

    def Reload(self): # -> 
        """ Reload(self: ApplicationSettingsBase) """
        ...

    def Reset(self): # -> 
        """ Reset(self: ApplicationSettingsBase) """
        ...

    def Upgrade(self): # -> 
        """ Upgrade(self: ApplicationSettingsBase) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, owner: IComponent)
        __new__(cls: type, settingsKey: str)
        __new__(cls: type, owner: IComponent, settingsKey: str)
        """
        ...

    PropertyChanged = ...
    SettingChanging = ...
    SettingsLoaded = ...
    SettingsSaving = ...


class ConfigurationSectionGroup: # skipped bases: <type 'object'>, <type 'object'>
    """ ConfigurationSectionGroup() """
    @property
    def IsDeclarationRequired(self) -> bool:
        """ Get: IsDeclarationRequired(self: ConfigurationSectionGroup) -> bool """
        ...

    @property
    def IsDeclared(self) -> bool:
        """ Get: IsDeclared(self: ConfigurationSectionGroup) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ConfigurationSectionGroup) -> str """
        ...

    @property
    def SectionGroupName(self) -> str:
        """ Get: SectionGroupName(self: ConfigurationSectionGroup) -> str """
        ...

    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection:
        """ Get: SectionGroups(self: ConfigurationSectionGroup) -> ConfigurationSectionGroupCollection """
        ...

    @property
    def Sections(self) -> ConfigurationSectionCollection:
        """ Get: Sections(self: ConfigurationSectionGroup) -> ConfigurationSectionCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ConfigurationSectionGroup) -> str
        Set: Type(self: ConfigurationSectionGroup) = value
        """
        ...


    def ForceDeclaration(self, force:bool = ...): # -> 
        """ ForceDeclaration(self: ConfigurationSectionGroup)ForceDeclaration(self: ConfigurationSectionGroup, force: bool) """
        ...

    def ShouldSerializeSectionGroupInTargetVersion(self, *args): #cannot find CLR method
        """ ShouldSerializeSectionGroupInTargetVersion(self: ConfigurationSectionGroup, targetFramework: FrameworkName) -> bool """
        ...


class ApplicationSettingsGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ApplicationSettingsGroup() """
    pass

class AppSettingsReader: # skipped bases: <type 'object'>, <type 'object'>
    """ AppSettingsReader() """
    def GetValue(self, key:str, type:Type) -> object:
        """ GetValue(self: AppSettingsReader, key: str, type: Type) -> object """
        ...


class ConfigurationElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentConfiguration(self) -> Configuration:
        """ Get: CurrentConfiguration(self: ConfigurationElement) -> Configuration """
        ...

    @property
    def ElementInformation(self) -> ElementInformation:
        """ Get: ElementInformation(self: ConfigurationElement) -> ElementInformation """
        ...

    @property
    def ElementProperty(self):
        ...

    @property
    def EvaluationContext(self):
        ...

    @property
    def HasContext(self):
        ...

    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """ Get: LockAllAttributesExcept(self: ConfigurationElement) -> ConfigurationLockCollection """
        ...

    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """ Get: LockAllElementsExcept(self: ConfigurationElement) -> ConfigurationLockCollection """
        ...

    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """ Get: LockAttributes(self: ConfigurationElement) -> ConfigurationLockCollection """
        ...

    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """ Get: LockElements(self: ConfigurationElement) -> ConfigurationLockCollection """
        ...

    @property
    def LockItem(self) -> bool:
        """
        Get: LockItem(self: ConfigurationElement) -> bool
        Set: LockItem(self: ConfigurationElement) = value
        """
        ...

    @property
    def Properties(self):
        ...


    def DeserializeElement(self, *args): #cannot find CLR method
        """ DeserializeElement(self: ConfigurationElement, reader: XmlReader, serializeCollectionKey: bool) """
        ...

    def Equals(self, compareTo:object) -> bool:
        """ Equals(self: ConfigurationElement, compareTo: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ConfigurationElement) -> int """
        ...

    def GetTransformedAssemblyString(self, *args): #cannot find CLR method
        """ GetTransformedAssemblyString(self: ConfigurationElement, assemblyName: str) -> str """
        ...

    def GetTransformedTypeString(self, *args): #cannot find CLR method
        """ GetTransformedTypeString(self: ConfigurationElement, typeName: str) -> str """
        ...

    def Init(self, *args): #cannot find CLR method
        """ Init(self: ConfigurationElement) """
        ...

    def InitializeDefault(self, *args): #cannot find CLR method
        """ InitializeDefault(self: ConfigurationElement) """
        ...

    def IsModified(self, *args): #cannot find CLR method
        """ IsModified(self: ConfigurationElement) -> bool """
        ...

    def IsReadOnly(self) -> bool:
        """ IsReadOnly(self: ConfigurationElement) -> bool """
        ...

    def ListErrors(self, *args): #cannot find CLR method
        """ ListErrors(self: ConfigurationElement, errorList: IList) """
        ...

    def OnDeserializeUnrecognizedAttribute(self, *args): #cannot find CLR method
        """ OnDeserializeUnrecognizedAttribute(self: ConfigurationElement, name: str, value: str) -> bool """
        ...

    def OnDeserializeUnrecognizedElement(self, *args): #cannot find CLR method
        """ OnDeserializeUnrecognizedElement(self: ConfigurationElement, elementName: str, reader: XmlReader) -> bool """
        ...

    def OnRequiredPropertyNotFound(self, *args): #cannot find CLR method
        """ OnRequiredPropertyNotFound(self: ConfigurationElement, name: str) -> object """
        ...

    def PostDeserialize(self, *args): #cannot find CLR method
        """ PostDeserialize(self: ConfigurationElement) """
        ...

    def PreSerialize(self, *args): #cannot find CLR method
        """ PreSerialize(self: ConfigurationElement, writer: XmlWriter) """
        ...

    def Reset(self, *args): #cannot find CLR method
        """ Reset(self: ConfigurationElement, parentElement: ConfigurationElement) """
        ...

    def ResetModified(self, *args): #cannot find CLR method
        """ ResetModified(self: ConfigurationElement) """
        ...

    def SerializeElement(self, *args): #cannot find CLR method
        """ SerializeElement(self: ConfigurationElement, writer: XmlWriter, serializeCollectionKey: bool) -> bool """
        ...

    def SerializeToXmlElement(self, *args): #cannot find CLR method
        """ SerializeToXmlElement(self: ConfigurationElement, writer: XmlWriter, elementName: str) -> bool """
        ...

    def SetPropertyValue(self, *args): #cannot find CLR method
        """ SetPropertyValue(self: ConfigurationElement, prop: ConfigurationProperty, value: object, ignoreLocks: bool) """
        ...

    def SetReadOnly(self, *args): #cannot find CLR method
        """ SetReadOnly(self: ConfigurationElement) """
        ...

    def Unmerge(self, *args): #cannot find CLR method
        """ Unmerge(self: ConfigurationElement, sourceElement: ConfigurationElement, parentElement: ConfigurationElement, saveMode: ConfigurationSaveMode) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationSection(ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SectionInformation(self) -> SectionInformation:
        """ Get: SectionInformation(self: ConfigurationSection) -> SectionInformation """
        ...


    def DeserializeSection(self, *args): #cannot find CLR method
        """ DeserializeSection(self: ConfigurationSection, reader: XmlReader) """
        ...

    def GetRuntimeObject(self, *args): #cannot find CLR method
        """ GetRuntimeObject(self: ConfigurationSection) -> object """
        ...

    def SerializeSection(self, *args): #cannot find CLR method
        """ SerializeSection(self: ConfigurationSection, parentElement: ConfigurationElement, name: str, saveMode: ConfigurationSaveMode) -> str """
        ...

    def ShouldSerializeElementInTargetVersion(self, *args): #cannot find CLR method
        """ ShouldSerializeElementInTargetVersion(self: ConfigurationSection, element: ConfigurationElement, elementName: str, targetFramework: FrameworkName) -> bool """
        ...

    def ShouldSerializePropertyInTargetVersion(self, *args): #cannot find CLR method
        """ ShouldSerializePropertyInTargetVersion(self: ConfigurationSection, property: ConfigurationProperty, propertyName: str, targetFramework: FrameworkName, parentConfigurationElement: ConfigurationElement) -> bool """
        ...

    def ShouldSerializeSectionInTargetVersion(self, *args): #cannot find CLR method
        """ ShouldSerializeSectionInTargetVersion(self: ConfigurationSection, targetFramework: FrameworkName) -> bool """
        ...


class AppSettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ AppSettingsSection() """
    @property
    def File(self) -> str:
        """
        Get: File(self: AppSettingsSection) -> str
        Set: File(self: AppSettingsSection) = value
        """
        ...

    @property
    def Settings(self) -> KeyValueConfigurationCollection:
        """ Get: Settings(self: AppSettingsSection) -> KeyValueConfigurationCollection """
        ...



class ConfigurationValidatorBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanValidate(self, type:Type) -> bool:
        """ CanValidate(self: ConfigurationValidatorBase, type: Type) -> bool """
        ...

    def Validate(self, value:object): # -> 
        """ Validate(self: ConfigurationValidatorBase, value: object) """
        ...


class CallbackValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ CallbackValidator(type: Type, callback: ValidatorCallback) """
    def __new__(cls, type:Type, callback:ValidatorCallback) -> Self:
        """ __new__(cls: type, type: Type, callback: ValidatorCallback) """
        ...


class ConfigurationValidatorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConfigurationValidatorAttribute(validator: Type) """
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase:
        """ Get: ValidatorInstance(self: ConfigurationValidatorAttribute) -> ConfigurationValidatorBase """
        ...

    @property
    def ValidatorType(self) -> Type:
        """ Get: ValidatorType(self: ConfigurationValidatorAttribute) -> Type """
        ...


    def __new__(cls, validator:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, validator: Type)
        """
        ...


class CallbackValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CallbackValidatorAttribute() """
    @property
    def CallbackMethodName(self) -> str:
        """
        Get: CallbackMethodName(self: CallbackValidatorAttribute) -> str
        Set: CallbackMethodName(self: CallbackValidatorAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: CallbackValidatorAttribute) -> Type
        Set: Type(self: CallbackValidatorAttribute) = value
        """
        ...



class ClientSettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ClientSettingsSection() """
    @property
    def Settings(self) -> SettingElementCollection:
        """ Get: Settings(self: ClientSettingsSection) -> SettingElementCollection """
        ...



class CommaDelimitedStringCollection(StringCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ CommaDelimitedStringCollection() """
    @property
    def IsModified(self) -> bool:
        """ Get: IsModified(self: CommaDelimitedStringCollection) -> bool """
        ...


    def Clone(self) -> CommaDelimitedStringCollection:
        """ Clone(self: CommaDelimitedStringCollection) -> CommaDelimitedStringCollection """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: CommaDelimitedStringCollection) """
        ...

    def ToString(self) -> str:
        """ ToString(self: CommaDelimitedStringCollection) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ConfigurationConverterBase(TypeConverter): # skipped bases: <type 'object'>
    """ no doc """
    pass

class CommaDelimitedStringCollectionConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ CommaDelimitedStringCollectionConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: CommaDelimitedStringCollectionConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: CommaDelimitedStringCollectionConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class Configuration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppSettings(self) -> AppSettingsSection:
        """ Get: AppSettings(self: Configuration) -> AppSettingsSection """
        ...

    @property
    def AssemblyStringTransformer(self): # -> Func
        """
        Get: AssemblyStringTransformer(self: Configuration) -> Func[str, str]
        Set: AssemblyStringTransformer(self: Configuration) = value
        """
        ...

    @property
    def ConnectionStrings(self) -> ConnectionStringsSection:
        """ Get: ConnectionStrings(self: Configuration) -> ConnectionStringsSection """
        ...

    @property
    def EvaluationContext(self) -> ContextInformation:
        """ Get: EvaluationContext(self: Configuration) -> ContextInformation """
        ...

    @property
    def FilePath(self) -> str:
        """ Get: FilePath(self: Configuration) -> str """
        ...

    @property
    def HasFile(self) -> bool:
        """ Get: HasFile(self: Configuration) -> bool """
        ...

    @property
    def Locations(self) -> ConfigurationLocationCollection:
        """ Get: Locations(self: Configuration) -> ConfigurationLocationCollection """
        ...

    @property
    def NamespaceDeclared(self) -> bool:
        """
        Get: NamespaceDeclared(self: Configuration) -> bool
        Set: NamespaceDeclared(self: Configuration) = value
        """
        ...

    @property
    def RootSectionGroup(self) -> ConfigurationSectionGroup:
        """ Get: RootSectionGroup(self: Configuration) -> ConfigurationSectionGroup """
        ...

    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection:
        """ Get: SectionGroups(self: Configuration) -> ConfigurationSectionGroupCollection """
        ...

    @property
    def Sections(self) -> ConfigurationSectionCollection:
        """ Get: Sections(self: Configuration) -> ConfigurationSectionCollection """
        ...

    @property
    def TargetFramework(self) -> FrameworkName:
        """
        Get: TargetFramework(self: Configuration) -> FrameworkName
        Set: TargetFramework(self: Configuration) = value
        """
        ...

    @property
    def TypeStringTransformer(self): # -> Func
        """
        Get: TypeStringTransformer(self: Configuration) -> Func[str, str]
        Set: TypeStringTransformer(self: Configuration) = value
        """
        ...


    def GetSection(self, sectionName:str) -> ConfigurationSection:
        """ GetSection(self: Configuration, sectionName: str) -> ConfigurationSection """
        ...

    def GetSectionGroup(self, sectionGroupName:str) -> ConfigurationSectionGroup:
        """ GetSectionGroup(self: Configuration, sectionGroupName: str) -> ConfigurationSectionGroup """
        ...

    def Save(self, saveMode:ConfigurationSaveMode = ..., forceSaveAll:bool = ...): # -> 
        """ Save(self: Configuration)Save(self: Configuration, saveMode: ConfigurationSaveMode)Save(self: Configuration, saveMode: ConfigurationSaveMode, forceSaveAll: bool) """
        ...

    def SaveAs(self, filename:str, saveMode:ConfigurationSaveMode = ..., forceSaveAll:bool = ...): # -> 
        """ SaveAs(self: Configuration, filename: str)SaveAs(self: Configuration, filename: str, saveMode: ConfigurationSaveMode)SaveAs(self: Configuration, filename: str, saveMode: ConfigurationSaveMode, forceSaveAll: bool) """
        ...


class ConfigurationAllowDefinition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationAllowDefinition, values: Everywhere (300), MachineOnly (0), MachineToApplication (200), MachineToWebRoot (100) """
    Everywhere: ConfigurationAllowDefinition = ...
    MachineOnly: ConfigurationAllowDefinition = ...
    MachineToApplication: ConfigurationAllowDefinition = ...
    MachineToWebRoot: ConfigurationAllowDefinition = ...
    value__ = ...


class ConfigurationAllowExeDefinition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationAllowExeDefinition, values: MachineOnly (0), MachineToApplication (100), MachineToLocalUser (300), MachineToRoamingUser (200) """
    MachineOnly: ConfigurationAllowExeDefinition = ...
    MachineToApplication: ConfigurationAllowExeDefinition = ...
    MachineToLocalUser: ConfigurationAllowExeDefinition = ...
    MachineToRoamingUser: ConfigurationAllowExeDefinition = ...
    value__ = ...


class ConfigurationBuilder(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    def ProcessConfigurationSection(self, configSection:ConfigurationSection) -> ConfigurationSection:
        """ ProcessConfigurationSection(self: ConfigurationBuilder, configSection: ConfigurationSection) -> ConfigurationSection """
        ...

    def ProcessRawXml(self, rawXml:XmlNode) -> XmlNode:
        """ ProcessRawXml(self: ConfigurationBuilder, rawXml: XmlNode) -> XmlNode """
        ...


class ConfigurationBuilderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ConfigurationBuilderCollection() """
    pass

class ConfigurationBuilderSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """ ConfigurationBuilderSettings() """
    @property
    def Builders(self) -> ProviderSettingsCollection:
        """ Get: Builders(self: ConfigurationBuilderSettings) -> ProviderSettingsCollection """
        ...



class ConfigurationBuildersSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ConfigurationBuildersSection() """
    @property
    def Builders(self) -> ProviderSettingsCollection:
        """ Get: Builders(self: ConfigurationBuildersSection) -> ProviderSettingsCollection """
        ...


    def GetBuilderFromName(self, builderName:str) -> ConfigurationBuilder:
        """ GetBuilderFromName(self: ConfigurationBuildersSection, builderName: str) -> ConfigurationBuilder """
        ...


class ConfigurationCollectionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConfigurationCollectionAttribute(itemType: Type) """
    @property
    def AddItemName(self) -> str:
        """
        Get: AddItemName(self: ConfigurationCollectionAttribute) -> str
        Set: AddItemName(self: ConfigurationCollectionAttribute) = value
        """
        ...

    @property
    def ClearItemsName(self) -> str:
        """
        Get: ClearItemsName(self: ConfigurationCollectionAttribute) -> str
        Set: ClearItemsName(self: ConfigurationCollectionAttribute) = value
        """
        ...

    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """
        Get: CollectionType(self: ConfigurationCollectionAttribute) -> ConfigurationElementCollectionType
        Set: CollectionType(self: ConfigurationCollectionAttribute) = value
        """
        ...

    @property
    def ItemType(self) -> Type:
        """ Get: ItemType(self: ConfigurationCollectionAttribute) -> Type """
        ...

    @property
    def RemoveItemName(self) -> str:
        """
        Get: RemoveItemName(self: ConfigurationCollectionAttribute) -> str
        Set: RemoveItemName(self: ConfigurationCollectionAttribute) = value
        """
        ...


    def __new__(cls, itemType:Type) -> Self:
        """ __new__(cls: type, itemType: Type) """
        ...


class ConfigurationElementCollection(ConfigurationElement, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AddElementName(self):
        ...

    @property
    def ClearElementName(self):
        ...

    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """ Get: CollectionType(self: ConfigurationElementCollection) -> ConfigurationElementCollectionType """
        ...

    @property
    def ElementName(self):
        ...

    @property
    def EmitClear(self) -> bool:
        """
        Get: EmitClear(self: ConfigurationElementCollection) -> bool
        Set: EmitClear(self: ConfigurationElementCollection) = value
        """
        ...

    @property
    def RemoveElementName(self):
        ...

    @property
    def ThrowOnDuplicate(self):
        ...


    def BaseAdd(self, *args): #cannot find CLR method
        """ BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement)BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement, throwIfExists: bool)BaseAdd(self: ConfigurationElementCollection, index: int, element: ConfigurationElement) """
        ...

    def BaseClear(self, *args): #cannot find CLR method
        """ BaseClear(self: ConfigurationElementCollection) """
        ...

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: ConfigurationElementCollection, key: object) -> ConfigurationElement
        BaseGet(self: ConfigurationElementCollection, index: int) -> ConfigurationElement
        """
        ...

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """ BaseGetAllKeys(self: ConfigurationElementCollection) -> Array[object] """
        ...

    def BaseGetKey(self, *args): #cannot find CLR method
        """ BaseGetKey(self: ConfigurationElementCollection, index: int) -> object """
        ...

    def BaseIndexOf(self, *args): #cannot find CLR method
        """ BaseIndexOf(self: ConfigurationElementCollection, element: ConfigurationElement) -> int """
        ...

    def BaseIsRemoved(self, *args): #cannot find CLR method
        """ BaseIsRemoved(self: ConfigurationElementCollection, key: object) -> bool """
        ...

    def BaseRemove(self, *args): #cannot find CLR method
        """ BaseRemove(self: ConfigurationElementCollection, key: object) """
        ...

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """ BaseRemoveAt(self: ConfigurationElementCollection, index: int) """
        ...

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: ConfigurationElementCollection, elementName: str) -> ConfigurationElement
        CreateNewElement(self: ConfigurationElementCollection) -> ConfigurationElement
        """
        ...

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: ConfigurationElementCollection, element: ConfigurationElement) -> object """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConfigurationElementCollection) -> IEnumerator """
        ...

    def IsElementName(self, *args): #cannot find CLR method
        """ IsElementName(self: ConfigurationElementCollection, elementName: str) -> bool """
        ...

    def IsElementRemovable(self, *args): #cannot find CLR method
        """ IsElementRemovable(self: ConfigurationElementCollection, element: ConfigurationElement) -> bool """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, comparer: IComparer)
        """
        ...


class ConfigurationElementCollectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationElementCollectionType, values: AddRemoveClearMap (1), AddRemoveClearMapAlternate (3), BasicMap (0), BasicMapAlternate (2) """
    AddRemoveClearMap: ConfigurationElementCollectionType = ...
    AddRemoveClearMapAlternate: ConfigurationElementCollectionType = ...
    BasicMap: ConfigurationElementCollectionType = ...
    BasicMapAlternate: ConfigurationElementCollectionType = ...
    value__ = ...


class ConfigurationElementProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ ConfigurationElementProperty(validator: ConfigurationValidatorBase) """
    @property
    def Validator(self) -> ConfigurationValidatorBase:
        """ Get: Validator(self: ConfigurationElementProperty) -> ConfigurationValidatorBase """
        ...



class ConfigurationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConfigurationException()
    ConfigurationException(message: str)
    ConfigurationException(message: str, inner: Exception)
    ConfigurationException(message: str, node: XmlNode)
    ConfigurationException(message: str, inner: Exception, node: XmlNode)
    ConfigurationException(message: str, filename: str, line: int)
    ConfigurationException(message: str, inner: Exception, filename: str, line: int)
    """
    @property
    def BareMessage(self) -> str:
        """ Get: BareMessage(self: ConfigurationException) -> str """
        ...

    @property
    def Filename(self) -> str:
        """ Get: Filename(self: ConfigurationException) -> str """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: ConfigurationException) -> int """
        ...


    @staticmethod
    def GetXmlNodeFilename(node:XmlNode) -> str:
        """ GetXmlNodeFilename(node: XmlNode) -> str """
        ...

    @staticmethod
    def GetXmlNodeLineNumber(node:XmlNode) -> int:
        """ GetXmlNodeLineNumber(node: XmlNode) -> int """
        ...

    SerializeObjectState = ...


class ConfigurationErrorsException(ConfigurationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConfigurationErrorsException(message: str, inner: Exception, filename: str, line: int)
    ConfigurationErrorsException()
    ConfigurationErrorsException(message: str)
    ConfigurationErrorsException(message: str, inner: Exception)
    ConfigurationErrorsException(message: str, filename: str, line: int)
    ConfigurationErrorsException(message: str, node: XmlNode)
    ConfigurationErrorsException(message: str, inner: Exception, node: XmlNode)
    ConfigurationErrorsException(message: str, reader: XmlReader)
    ConfigurationErrorsException(message: str, inner: Exception, reader: XmlReader)
    """
    @property
    def Errors(self) -> ICollection:
        """ Get: Errors(self: ConfigurationErrorsException) -> ICollection """
        ...


    @staticmethod
    def GetFilename(*__args:XmlNode) -> str:
        """
        GetFilename(node: XmlNode) -> str
        GetFilename(reader: XmlReader) -> str
        """
        ...

    @staticmethod
    def GetLineNumber(*__args:XmlNode) -> int:
        """
        GetLineNumber(node: XmlNode) -> int
        GetLineNumber(reader: XmlReader) -> int
        """
        ...

    SerializeObjectState = ...


class ConfigurationFileMap(ICloneable): # skipped bases: <type 'object'>
    """
    ConfigurationFileMap()
    ConfigurationFileMap(machineConfigFilename: str)
    """
    @property
    def MachineConfigFilename(self) -> str:
        """
        Get: MachineConfigFilename(self: ConfigurationFileMap) -> str
        Set: MachineConfigFilename(self: ConfigurationFileMap) = value
        """
        ...



class ConfigurationLocation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Path(self) -> str:
        """ Get: Path(self: ConfigurationLocation) -> str """
        ...


    def OpenConfiguration(self) -> Configuration:
        """ OpenConfiguration(self: ConfigurationLocation) -> Configuration """
        ...


class ConfigurationLocationCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ConfigurationLockCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def AttributeList(self) -> str:
        """ Get: AttributeList(self: ConfigurationLockCollection) -> str """
        ...

    @property
    def HasParentElements(self) -> bool:
        """ Get: HasParentElements(self: ConfigurationLockCollection) -> bool """
        ...

    @property
    def IsModified(self) -> bool:
        """ Get: IsModified(self: ConfigurationLockCollection) -> bool """
        ...


    def Add(self, name:str): # -> 
        """ Add(self: ConfigurationLockCollection, name: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConfigurationLockCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: ConfigurationLockCollection, name: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConfigurationLockCollection) -> IEnumerator """
        ...

    def IsReadOnly(self, name:str) -> bool:
        """ IsReadOnly(self: ConfigurationLockCollection, name: str) -> bool """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ConfigurationLockCollection, name: str) """
        ...

    def SetFromList(self, attributeList:str): # -> 
        """ SetFromList(self: ConfigurationLockCollection, attributeList: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ConfigurationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppSettings(self) -> NameValueCollection:
        """ Get: AppSettings() -> NameValueCollection """
        ...

    @property
    def ConnectionStrings(self) -> ConnectionStringSettingsCollection:
        """ Get: ConnectionStrings() -> ConnectionStringSettingsCollection """
        ...


    @staticmethod
    def GetSection(sectionName:str) -> object:
        """ GetSection(sectionName: str) -> object """
        ...

    @staticmethod
    def OpenExeConfiguration(*__args:ConfigurationUserLevel) -> Configuration:
        """
        OpenExeConfiguration(userLevel: ConfigurationUserLevel) -> Configuration
        OpenExeConfiguration(exePath: str) -> Configuration
        """
        ...

    @staticmethod
    def OpenMachineConfiguration() -> Configuration:
        """ OpenMachineConfiguration() -> Configuration """
        ...

    @staticmethod
    def OpenMappedExeConfiguration(fileMap:ExeConfigurationFileMap, userLevel:ConfigurationUserLevel, preLoad:bool = ...) -> Configuration:
        """
        OpenMappedExeConfiguration(fileMap: ExeConfigurationFileMap, userLevel: ConfigurationUserLevel) -> Configuration
        OpenMappedExeConfiguration(fileMap: ExeConfigurationFileMap, userLevel: ConfigurationUserLevel, preLoad: bool) -> Configuration
        """
        ...

    @staticmethod
    def OpenMappedMachineConfiguration(fileMap:ConfigurationFileMap) -> Configuration:
        """ OpenMappedMachineConfiguration(fileMap: ConfigurationFileMap) -> Configuration """
        ...

    @staticmethod
    def RefreshSection(sectionName:str): # -> 
        """ RefreshSection(sectionName: str) """
        ...

    __all__: list = ...


class ConfigurationPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ ConfigurationPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class ConfigurationPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConfigurationPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: ConfigurationPermissionAttribute) -> IPermission """
        ...


class ConfigurationProperty: # skipped bases: <type 'object'>, <type 'object'>
    """
    ConfigurationProperty(name: str, type: Type)
    ConfigurationProperty(name: str, type: Type, defaultValue: object)
    ConfigurationProperty(name: str, type: Type, defaultValue: object, options: ConfigurationPropertyOptions)
    ConfigurationProperty(name: str, type: Type, defaultValue: object, typeConverter: TypeConverter, validator: ConfigurationValidatorBase, options: ConfigurationPropertyOptions)
    ConfigurationProperty(name: str, type: Type, defaultValue: object, typeConverter: TypeConverter, validator: ConfigurationValidatorBase, options: ConfigurationPropertyOptions, description: str)
    """
    @property
    def Converter(self) -> TypeConverter:
        """ Get: Converter(self: ConfigurationProperty) -> TypeConverter """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: ConfigurationProperty) -> object """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: ConfigurationProperty) -> str """
        ...

    @property
    def IsAssemblyStringTransformationRequired(self) -> bool:
        """ Get: IsAssemblyStringTransformationRequired(self: ConfigurationProperty) -> bool """
        ...

    @property
    def IsDefaultCollection(self) -> bool:
        """ Get: IsDefaultCollection(self: ConfigurationProperty) -> bool """
        ...

    @property
    def IsKey(self) -> bool:
        """ Get: IsKey(self: ConfigurationProperty) -> bool """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: ConfigurationProperty) -> bool """
        ...

    @property
    def IsTypeStringTransformationRequired(self) -> bool:
        """ Get: IsTypeStringTransformationRequired(self: ConfigurationProperty) -> bool """
        ...

    @property
    def IsVersionCheckRequired(self) -> bool:
        """ Get: IsVersionCheckRequired(self: ConfigurationProperty) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ConfigurationProperty) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ConfigurationProperty) -> Type """
        ...

    @property
    def Validator(self) -> ConfigurationValidatorBase:
        """ Get: Validator(self: ConfigurationProperty) -> ConfigurationValidatorBase """
        ...



class ConfigurationPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConfigurationPropertyAttribute(name: str) """
    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: ConfigurationPropertyAttribute) -> object
        Set: DefaultValue(self: ConfigurationPropertyAttribute) = value
        """
        ...

    @property
    def IsDefaultCollection(self) -> bool:
        """
        Get: IsDefaultCollection(self: ConfigurationPropertyAttribute) -> bool
        Set: IsDefaultCollection(self: ConfigurationPropertyAttribute) = value
        """
        ...

    @property
    def IsKey(self) -> bool:
        """
        Get: IsKey(self: ConfigurationPropertyAttribute) -> bool
        Set: IsKey(self: ConfigurationPropertyAttribute) = value
        """
        ...

    @property
    def IsRequired(self) -> bool:
        """
        Get: IsRequired(self: ConfigurationPropertyAttribute) -> bool
        Set: IsRequired(self: ConfigurationPropertyAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ConfigurationPropertyAttribute) -> str """
        ...

    @property
    def Options(self) -> ConfigurationPropertyOptions:
        """
        Get: Options(self: ConfigurationPropertyAttribute) -> ConfigurationPropertyOptions
        Set: Options(self: ConfigurationPropertyAttribute) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ConfigurationPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ConfigurationPropertyCollection() """
    def Add(self, property:ConfigurationProperty): # -> 
        """ Add(self: ConfigurationPropertyCollection, property: ConfigurationProperty) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConfigurationPropertyCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: ConfigurationPropertyCollection, name: str) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConfigurationPropertyCollection) -> IEnumerator """
        ...

    def Remove(self, name:str) -> bool:
        """ Remove(self: ConfigurationPropertyCollection, name: str) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ConfigurationPropertyOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ConfigurationPropertyOptions, values: IsAssemblyStringTransformationRequired (16), IsDefaultCollection (1), IsKey (4), IsRequired (2), IsTypeStringTransformationRequired (8), IsVersionCheckRequired (32), None (0) """
    IsAssemblyStringTransformationRequired: ConfigurationPropertyOptions = ...
    IsDefaultCollection: ConfigurationPropertyOptions = ...
    IsKey: ConfigurationPropertyOptions = ...
    IsRequired: ConfigurationPropertyOptions = ...
    IsTypeStringTransformationRequired: ConfigurationPropertyOptions = ...
    IsVersionCheckRequired: ConfigurationPropertyOptions = ...
    value__ = ...


class ConfigurationSaveMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationSaveMode, values: Full (2), Minimal (1), Modified (0) """
    Full: ConfigurationSaveMode = ...
    Minimal: ConfigurationSaveMode = ...
    Modified: ConfigurationSaveMode = ...
    value__ = ...


class ConfigurationSectionCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def Add(self, name:str, section:ConfigurationSection): # -> 
        """ Add(self: ConfigurationSectionCollection, name: str, section: ConfigurationSection) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConfigurationSectionCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ConfigurationSectionCollection, array: Array[ConfigurationSection], index: int) """
        ...

    def Get(self, *__args:int) -> ConfigurationSection:
        """
        Get(self: ConfigurationSectionCollection, index: int) -> ConfigurationSection
        Get(self: ConfigurationSectionCollection, name: str) -> ConfigurationSection
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: ConfigurationSectionCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ConfigurationSectionCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ConfigurationSectionCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class ConfigurationSectionGroupCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def Add(self, name:str, sectionGroup:ConfigurationSectionGroup): # -> 
        """ Add(self: ConfigurationSectionGroupCollection, name: str, sectionGroup: ConfigurationSectionGroup) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConfigurationSectionGroupCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ConfigurationSectionGroupCollection, array: Array[ConfigurationSectionGroup], index: int) """
        ...

    def Get(self, *__args:int) -> ConfigurationSectionGroup:
        """
        Get(self: ConfigurationSectionGroupCollection, index: int) -> ConfigurationSectionGroup
        Get(self: ConfigurationSectionGroupCollection, name: str) -> ConfigurationSectionGroup
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: ConfigurationSectionGroupCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ConfigurationSectionGroupCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ConfigurationSectionGroupCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class ConfigurationSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AppSettings(self) -> NameValueCollection:
        """ Get: AppSettings() -> NameValueCollection """
        ...


    @staticmethod
    def GetConfig(sectionName:str) -> object:
        """ GetConfig(sectionName: str) -> object """
        ...



class ConfigurationUserLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConfigurationUserLevel, values: None (0), PerUserRoaming (10), PerUserRoamingAndLocal (20) """
    PerUserRoaming: ConfigurationUserLevel = ...
    PerUserRoamingAndLocal: ConfigurationUserLevel = ...
    value__ = ...


class ConfigXmlDocument(IConfigErrorInfo, XmlDocument): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ ConfigXmlDocument() """
    def LoadSingleElement(self, filename:str, sourceReader:XmlTextReader): # -> 
        """ LoadSingleElement(self: ConfigXmlDocument, filename: str, sourceReader: XmlTextReader) """
        ...


class ConnectionStringSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ConnectionStringSettings()
    ConnectionStringSettings(name: str, connectionString: str)
    ConnectionStringSettings(name: str, connectionString: str, providerName: str)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: ConnectionStringSettings) -> str
        Set: ConnectionString(self: ConnectionStringSettings) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ConnectionStringSettings) -> str
        Set: Name(self: ConnectionStringSettings) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: ConnectionStringSettings) -> str
        Set: ProviderName(self: ConnectionStringSettings) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ConnectionStringSettings) -> str """
        ...

    def __new__(cls, name:str = ..., connectionString:str = ..., providerName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, connectionString: str)
        __new__(cls: type, name: str, connectionString: str, providerName: str)
        """
        ...


class ConnectionStringSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ConnectionStringSettingsCollection() """
    def Add(self, settings:ConnectionStringSettings): # -> 
        """ Add(self: ConnectionStringSettingsCollection, settings: ConnectionStringSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConnectionStringSettingsCollection) """
        ...

    def IndexOf(self, settings:ConnectionStringSettings) -> int:
        """ IndexOf(self: ConnectionStringSettingsCollection, settings: ConnectionStringSettings) -> int """
        ...

    def Remove(self, *__args:ConnectionStringSettings): # -> 
        """ Remove(self: ConnectionStringSettingsCollection, settings: ConnectionStringSettings)Remove(self: ConnectionStringSettingsCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ConnectionStringSettingsCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ConnectionStringsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ConnectionStringsSection() """
    @property
    def ConnectionStrings(self) -> ConnectionStringSettingsCollection:
        """ Get: ConnectionStrings(self: ConnectionStringsSection) -> ConnectionStringSettingsCollection """
        ...



class ContextInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HostingContext(self) -> object:
        """ Get: HostingContext(self: ContextInformation) -> object """
        ...

    @property
    def IsMachineLevel(self) -> bool:
        """ Get: IsMachineLevel(self: ContextInformation) -> bool """
        ...


    def GetSection(self, sectionName:str) -> object:
        """ GetSection(self: ContextInformation, sectionName: str) -> object """
        ...


class DefaultSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DefaultSection() """
    pass

class DefaultSettingValueAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultSettingValueAttribute(value: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: DefaultSettingValueAttribute) -> str """
        ...


    def __new__(cls, value:str) -> Self:
        """ __new__(cls: type, value: str) """
        ...


class DefaultValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ DefaultValidator() """
    pass

class DictionarySectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ DictionarySectionHandler() """
    @property
    def KeyAttributeName(self):
        ...

    @property
    def ValueAttributeName(self):
        ...



class ProtectedConfigurationProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    def Decrypt(self, encryptedNode:XmlNode) -> XmlNode:
        """ Decrypt(self: ProtectedConfigurationProvider, encryptedNode: XmlNode) -> XmlNode """
        ...

    def Encrypt(self, node:XmlNode) -> XmlNode:
        """ Encrypt(self: ProtectedConfigurationProvider, node: XmlNode) -> XmlNode """
        ...


class DpapiProtectedConfigurationProvider(ProtectedConfigurationProvider): # skipped bases: <type 'object'>
    """ DpapiProtectedConfigurationProvider() """
    @property
    def UseMachineProtection(self) -> bool:
        """ Get: UseMachineProtection(self: DpapiProtectedConfigurationProvider) -> bool """
        ...


    def Initialize(self, name:str, configurationValues:NameValueCollection): # -> 
        """ Initialize(self: DpapiProtectedConfigurationProvider, name: str, configurationValues: NameValueCollection) """
        ...


class ElementInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> ICollection:
        """ Get: Errors(self: ElementInformation) -> ICollection """
        ...

    @property
    def IsCollection(self) -> bool:
        """ Get: IsCollection(self: ElementInformation) -> bool """
        ...

    @property
    def IsLocked(self) -> bool:
        """ Get: IsLocked(self: ElementInformation) -> bool """
        ...

    @property
    def IsPresent(self) -> bool:
        """ Get: IsPresent(self: ElementInformation) -> bool """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: ElementInformation) -> int """
        ...

    @property
    def Properties(self) -> PropertyInformationCollection:
        """ Get: Properties(self: ElementInformation) -> PropertyInformationCollection """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: ElementInformation) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ElementInformation) -> Type """
        ...

    @property
    def Validator(self) -> ConfigurationValidatorBase:
        """ Get: Validator(self: ElementInformation) -> ConfigurationValidatorBase """
        ...



class ExeConfigurationFileMap(ConfigurationFileMap): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    ExeConfigurationFileMap()
    ExeConfigurationFileMap(machineConfigFileName: str)
    """
    @property
    def ExeConfigFilename(self) -> str:
        """
        Get: ExeConfigFilename(self: ExeConfigurationFileMap) -> str
        Set: ExeConfigFilename(self: ExeConfigurationFileMap) = value
        """
        ...

    @property
    def LocalUserConfigFilename(self) -> str:
        """
        Get: LocalUserConfigFilename(self: ExeConfigurationFileMap) -> str
        Set: LocalUserConfigFilename(self: ExeConfigurationFileMap) = value
        """
        ...

    @property
    def RoamingUserConfigFilename(self) -> str:
        """
        Get: RoamingUserConfigFilename(self: ExeConfigurationFileMap) -> str
        Set: RoamingUserConfigFilename(self: ExeConfigurationFileMap) = value
        """
        ...



class ExeContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExePath(self) -> str:
        """ Get: ExePath(self: ExeContext) -> str """
        ...

    @property
    def UserLevel(self) -> ConfigurationUserLevel:
        """ Get: UserLevel(self: ExeContext) -> ConfigurationUserLevel """
        ...



class GenericEnumConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ GenericEnumConverter(typeEnum: Type) """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: GenericEnumConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: GenericEnumConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...

    def __new__(cls, typeEnum:Type) -> Self:
        """ __new__(cls: type, typeEnum: Type) """
        ...


class IApplicationSettingsProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetPreviousVersion(self, context:SettingsContext, property:SettingsProperty) -> SettingsPropertyValue:
        """ GetPreviousVersion(self: IApplicationSettingsProvider, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue """
        ...

    def Reset(self, context:SettingsContext): # -> 
        """ Reset(self: IApplicationSettingsProvider, context: SettingsContext) """
        ...

    def Upgrade(self, context:SettingsContext, properties:SettingsPropertyCollection): # -> 
        """ Upgrade(self: IApplicationSettingsProvider, context: SettingsContext, properties: SettingsPropertyCollection) """
        ...


class IConfigurationSectionHandler: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, parent:object, configContext:object, section:XmlNode) -> object:
        """ Create(self: IConfigurationSectionHandler, parent: object, configContext: object, section: XmlNode) -> object """
        ...


class IConfigurationSystem: # skipped bases: <type 'object'>
    """ no doc """
    def GetConfig(self, configKey:str) -> object:
        """ GetConfig(self: IConfigurationSystem, configKey: str) -> object """
        ...

    def Init(self): # -> 
        """ Init(self: IConfigurationSystem) """
        ...


class IdnElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IdnElement() """
    @property
    def Enabled(self) -> UriIdnScope:
        """
        Get: Enabled(self: IdnElement) -> UriIdnScope
        Set: Enabled(self: IdnElement) = value
        """
        ...



class IgnoreSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ IgnoreSection() """
    pass

class IgnoreSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ IgnoreSectionHandler() """
    pass

class InfiniteIntConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ InfiniteIntConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: InfiniteIntConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: InfiniteIntConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class InfiniteTimeSpanConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ InfiniteTimeSpanConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: InfiniteTimeSpanConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: InfiniteTimeSpanConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class IntegerValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """
    IntegerValidator(minValue: int, maxValue: int)
    IntegerValidator(minValue: int, maxValue: int, rangeIsExclusive: bool)
    IntegerValidator(minValue: int, maxValue: int, rangeIsExclusive: bool, resolution: int)
    """
    def __new__(cls, minValue:int, maxValue:int, rangeIsExclusive:bool = ..., resolution:int = ...) -> Self:
        """
        __new__(cls: type, minValue: int, maxValue: int)
        __new__(cls: type, minValue: int, maxValue: int, rangeIsExclusive: bool)
        __new__(cls: type, minValue: int, maxValue: int, rangeIsExclusive: bool, resolution: int)
        """
        ...


class IntegerValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IntegerValidatorAttribute() """
    @property
    def ExcludeRange(self) -> bool:
        """
        Get: ExcludeRange(self: IntegerValidatorAttribute) -> bool
        Set: ExcludeRange(self: IntegerValidatorAttribute) = value
        """
        ...

    @property
    def MaxValue(self) -> int:
        """
        Get: MaxValue(self: IntegerValidatorAttribute) -> int
        Set: MaxValue(self: IntegerValidatorAttribute) = value
        """
        ...

    @property
    def MinValue(self) -> int:
        """
        Get: MinValue(self: IntegerValidatorAttribute) -> int
        Set: MinValue(self: IntegerValidatorAttribute) = value
        """
        ...



class IPersistComponentSettings: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SaveSettings(self) -> bool:
        """
        Get: SaveSettings(self: IPersistComponentSettings) -> bool
        Set: SaveSettings(self: IPersistComponentSettings) = value
        """
        ...

    @property
    def SettingsKey(self) -> str:
        """
        Get: SettingsKey(self: IPersistComponentSettings) -> str
        Set: SettingsKey(self: IPersistComponentSettings) = value
        """
        ...


    def LoadComponentSettings(self): # -> 
        """ LoadComponentSettings(self: IPersistComponentSettings) """
        ...

    def ResetComponentSettings(self): # -> 
        """ ResetComponentSettings(self: IPersistComponentSettings) """
        ...

    def SaveComponentSettings(self): # -> 
        """ SaveComponentSettings(self: IPersistComponentSettings) """
        ...


class IriParsingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ IriParsingElement() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: IriParsingElement) -> bool
        Set: Enabled(self: IriParsingElement) = value
        """
        ...



class ISettingsProviderService: # skipped bases: <type 'object'>
    """ no doc """
    def GetSettingsProvider(self, property:SettingsProperty) -> SettingsProvider:
        """ GetSettingsProvider(self: ISettingsProviderService, property: SettingsProperty) -> SettingsProvider """
        ...


class KeyValueConfigurationCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ KeyValueConfigurationCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: KeyValueConfigurationCollection) -> Array[str] """
        ...


    def Add(self, *__args:KeyValueConfigurationElement): # -> 
        """ Add(self: KeyValueConfigurationCollection, key: str, value: str)Add(self: KeyValueConfigurationCollection, keyValue: KeyValueConfigurationElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: KeyValueConfigurationCollection) """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: KeyValueConfigurationCollection, key: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class KeyValueConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ KeyValueConfigurationElement(key: str, value: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: KeyValueConfigurationElement) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: KeyValueConfigurationElement) -> str
        Set: Value(self: KeyValueConfigurationElement) = value
        """
        ...


    def __new__(cls, key:str, value:str) -> Self:
        """ __new__(cls: type, key: str, value: str) """
        ...


class SettingsProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: SettingsProvider) -> str
        Set: ApplicationName(self: SettingsProvider) = value
        """
        ...


    def GetPropertyValues(self, context:SettingsContext, collection:SettingsPropertyCollection) -> SettingsPropertyValueCollection:
        """ GetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyCollection) -> SettingsPropertyValueCollection """
        ...

    def SetPropertyValues(self, context:SettingsContext, collection:SettingsPropertyValueCollection): # -> 
        """ SetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyValueCollection) """
        ...


class LocalFileSettingsProvider(IApplicationSettingsProvider, SettingsProvider): # skipped bases: <type 'object'>
    """ LocalFileSettingsProvider() """
    def Initialize(self, name:str, values:NameValueCollection): # -> 
        """ Initialize(self: LocalFileSettingsProvider, name: str, values: NameValueCollection) """
        ...


class LongValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """
    LongValidator(minValue: Int64, maxValue: Int64)
    LongValidator(minValue: Int64, maxValue: Int64, rangeIsExclusive: bool)
    LongValidator(minValue: Int64, maxValue: Int64, rangeIsExclusive: bool, resolution: Int64)
    """
    def __new__(cls, minValue:Int64, maxValue:Int64, rangeIsExclusive:bool = ..., resolution:Int64 = ...) -> Self:
        """
        __new__(cls: type, minValue: Int64, maxValue: Int64)
        __new__(cls: type, minValue: Int64, maxValue: Int64, rangeIsExclusive: bool)
        __new__(cls: type, minValue: Int64, maxValue: Int64, rangeIsExclusive: bool, resolution: Int64)
        """
        ...


class LongValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ LongValidatorAttribute() """
    @property
    def ExcludeRange(self) -> bool:
        """
        Get: ExcludeRange(self: LongValidatorAttribute) -> bool
        Set: ExcludeRange(self: LongValidatorAttribute) = value
        """
        ...

    @property
    def MaxValue(self) -> Int64:
        """
        Get: MaxValue(self: LongValidatorAttribute) -> Int64
        Set: MaxValue(self: LongValidatorAttribute) = value
        """
        ...

    @property
    def MinValue(self) -> Int64:
        """
        Get: MinValue(self: LongValidatorAttribute) -> Int64
        Set: MinValue(self: LongValidatorAttribute) = value
        """
        ...



class NameValueConfigurationCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ NameValueConfigurationCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: NameValueConfigurationCollection) -> Array[str] """
        ...


    def Add(self, nameValue:NameValueConfigurationElement): # -> 
        """ Add(self: NameValueConfigurationCollection, nameValue: NameValueConfigurationElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: NameValueConfigurationCollection) """
        ...

    def Remove(self, *__args:NameValueConfigurationElement): # -> 
        """ Remove(self: NameValueConfigurationCollection, nameValue: NameValueConfigurationElement)Remove(self: NameValueConfigurationCollection, name: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class NameValueConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ NameValueConfigurationElement(name: str, value: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NameValueConfigurationElement) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: NameValueConfigurationElement) -> str
        Set: Value(self: NameValueConfigurationElement) = value
        """
        ...


    def __new__(cls, name:str, value:str) -> Self:
        """ __new__(cls: type, name: str, value: str) """
        ...


class NameValueFileSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ NameValueFileSectionHandler() """
    pass

class NameValueSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ NameValueSectionHandler() """
    @property
    def KeyAttributeName(self):
        ...

    @property
    def ValueAttributeName(self):
        ...



class NoSettingsVersionUpgradeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NoSettingsVersionUpgradeAttribute() """
    pass

class OverrideMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OverrideMode, values: Allow (1), Deny (2), Inherit (0) """
    Allow: OverrideMode = ...
    Deny: OverrideMode = ...
    Inherit: OverrideMode = ...
    value__ = ...


class PositiveTimeSpanValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ PositiveTimeSpanValidator() """
    pass

class PositiveTimeSpanValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PositiveTimeSpanValidatorAttribute() """
    pass

class PropertyInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Converter(self) -> TypeConverter:
        """ Get: Converter(self: PropertyInformation) -> TypeConverter """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: PropertyInformation) -> object """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: PropertyInformation) -> str """
        ...

    @property
    def IsKey(self) -> bool:
        """ Get: IsKey(self: PropertyInformation) -> bool """
        ...

    @property
    def IsLocked(self) -> bool:
        """ Get: IsLocked(self: PropertyInformation) -> bool """
        ...

    @property
    def IsModified(self) -> bool:
        """ Get: IsModified(self: PropertyInformation) -> bool """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: PropertyInformation) -> bool """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: PropertyInformation) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PropertyInformation) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: PropertyInformation) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: PropertyInformation) -> Type """
        ...

    @property
    def Validator(self) -> ConfigurationValidatorBase:
        """ Get: Validator(self: PropertyInformation) -> ConfigurationValidatorBase """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PropertyInformation) -> object
        Set: Value(self: PropertyInformation) = value
        """
        ...

    @property
    def ValueOrigin(self) -> PropertyValueOrigin:
        """ Get: ValueOrigin(self: PropertyInformation) -> PropertyValueOrigin """
        ...



class PropertyInformationCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PropertyInformationCollection, array: Array[PropertyInformation], index: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PropertyValueOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyValueOrigin, values: Default (0), Inherited (1), SetHere (2) """
    Default: PropertyValueOrigin = ...
    Inherited: PropertyValueOrigin = ...
    SetHere: PropertyValueOrigin = ...
    value__ = ...


class ProtectedConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultProvider(self) -> str:
        """ Get: DefaultProvider() -> str """
        ...

    @property
    def Providers(self) -> ProtectedConfigurationProviderCollection:
        """ Get: Providers() -> ProtectedConfigurationProviderCollection """
        ...


    DataProtectionProviderName: str = ...
    ProtectedDataSectionName: str = ...
    RsaProviderName: str = ...
    __all__: list = ...


class ProtectedConfigurationProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProtectedConfigurationProviderCollection() """
    pass

class ProtectedConfigurationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ProtectedConfigurationSection() """
    @property
    def DefaultProvider(self) -> str:
        """
        Get: DefaultProvider(self: ProtectedConfigurationSection) -> str
        Set: DefaultProvider(self: ProtectedConfigurationSection) = value
        """
        ...

    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: ProtectedConfigurationSection) -> ProviderSettingsCollection """
        ...



class ProtectedProviderSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """ ProtectedProviderSettings() """
    @property
    def Providers(self) -> ProviderSettingsCollection:
        """ Get: Providers(self: ProtectedProviderSettings) -> ProviderSettingsCollection """
        ...



class ProviderSettings(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProviderSettings()
    ProviderSettings(name: str, type: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ProviderSettings) -> str
        Set: Name(self: ProviderSettings) = value
        """
        ...

    @property
    def Parameters(self) -> NameValueCollection:
        """ Get: Parameters(self: ProviderSettings) -> NameValueCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ProviderSettings) -> str
        Set: Type(self: ProviderSettings) = value
        """
        ...


    def __new__(cls, name:str = ..., type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, type: str)
        """
        ...


class ProviderSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProviderSettingsCollection() """
    def Add(self, provider:ProviderSettings): # -> 
        """ Add(self: ProviderSettingsCollection, provider: ProviderSettings) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProviderSettingsCollection) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProviderSettingsCollection, name: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class RegexStringValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ RegexStringValidator(regex: str) """
    def __new__(cls, regex:str) -> Self:
        """ __new__(cls: type, regex: str) """
        ...


class RegexStringValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RegexStringValidatorAttribute(regex: str) """
    @property
    def Regex(self) -> str:
        """ Get: Regex(self: RegexStringValidatorAttribute) -> str """
        ...



class RsaProtectedConfigurationProvider(ProtectedConfigurationProvider): # skipped bases: <type 'object'>
    """ RsaProtectedConfigurationProvider() """
    @property
    def CspProviderName(self) -> str:
        """ Get: CspProviderName(self: RsaProtectedConfigurationProvider) -> str """
        ...

    @property
    def KeyContainerName(self) -> str:
        """ Get: KeyContainerName(self: RsaProtectedConfigurationProvider) -> str """
        ...

    @property
    def RsaPublicKey(self) -> RSAParameters:
        """ Get: RsaPublicKey(self: RsaProtectedConfigurationProvider) -> RSAParameters """
        ...

    @property
    def UseFIPS(self) -> bool:
        """ Get: UseFIPS(self: RsaProtectedConfigurationProvider) -> bool """
        ...

    @property
    def UseMachineContainer(self) -> bool:
        """ Get: UseMachineContainer(self: RsaProtectedConfigurationProvider) -> bool """
        ...

    @property
    def UseOAEP(self) -> bool:
        """ Get: UseOAEP(self: RsaProtectedConfigurationProvider) -> bool """
        ...


    def AddKey(self, keySize:int, exportable:bool): # -> 
        """ AddKey(self: RsaProtectedConfigurationProvider, keySize: int, exportable: bool) """
        ...

    def DeleteKey(self): # -> 
        """ DeleteKey(self: RsaProtectedConfigurationProvider) """
        ...

    def ExportKey(self, xmlFileName:str, includePrivateParameters:bool): # -> 
        """ ExportKey(self: RsaProtectedConfigurationProvider, xmlFileName: str, includePrivateParameters: bool) """
        ...

    def ImportKey(self, xmlFileName:str, exportable:bool): # -> 
        """ ImportKey(self: RsaProtectedConfigurationProvider, xmlFileName: str, exportable: bool) """
        ...

    def Initialize(self, name:str, configurationValues:NameValueCollection): # -> 
        """ Initialize(self: RsaProtectedConfigurationProvider, name: str, configurationValues: NameValueCollection) """
        ...


class SchemeSettingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SchemeSettingElement() """
    @property
    def GenericUriParserOptions(self) -> GenericUriParserOptions:
        """ Get: GenericUriParserOptions(self: SchemeSettingElement) -> GenericUriParserOptions """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SchemeSettingElement) -> str """
        ...



class SchemeSettingElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SchemeSettingElementCollection() """
    def IndexOf(self, element:SchemeSettingElement) -> int:
        """ IndexOf(self: SchemeSettingElementCollection, element: SchemeSettingElement) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class SectionInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowDefinition(self) -> ConfigurationAllowDefinition:
        """
        Get: AllowDefinition(self: SectionInformation) -> ConfigurationAllowDefinition
        Set: AllowDefinition(self: SectionInformation) = value
        """
        ...

    @property
    def AllowExeDefinition(self) -> ConfigurationAllowExeDefinition:
        """
        Get: AllowExeDefinition(self: SectionInformation) -> ConfigurationAllowExeDefinition
        Set: AllowExeDefinition(self: SectionInformation) = value
        """
        ...

    @property
    def AllowLocation(self) -> bool:
        """
        Get: AllowLocation(self: SectionInformation) -> bool
        Set: AllowLocation(self: SectionInformation) = value
        """
        ...

    @property
    def AllowOverride(self) -> bool:
        """
        Get: AllowOverride(self: SectionInformation) -> bool
        Set: AllowOverride(self: SectionInformation) = value
        """
        ...

    @property
    def ConfigSource(self) -> str:
        """
        Get: ConfigSource(self: SectionInformation) -> str
        Set: ConfigSource(self: SectionInformation) = value
        """
        ...

    @property
    def ConfigurationBuilder(self) -> ConfigurationBuilder:
        """ Get: ConfigurationBuilder(self: SectionInformation) -> ConfigurationBuilder """
        ...

    @property
    def ForceSave(self) -> bool:
        """
        Get: ForceSave(self: SectionInformation) -> bool
        Set: ForceSave(self: SectionInformation) = value
        """
        ...

    @property
    def InheritInChildApplications(self) -> bool:
        """
        Get: InheritInChildApplications(self: SectionInformation) -> bool
        Set: InheritInChildApplications(self: SectionInformation) = value
        """
        ...

    @property
    def IsDeclarationRequired(self) -> bool:
        """ Get: IsDeclarationRequired(self: SectionInformation) -> bool """
        ...

    @property
    def IsDeclared(self) -> bool:
        """ Get: IsDeclared(self: SectionInformation) -> bool """
        ...

    @property
    def IsLocked(self) -> bool:
        """ Get: IsLocked(self: SectionInformation) -> bool """
        ...

    @property
    def IsProtected(self) -> bool:
        """ Get: IsProtected(self: SectionInformation) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SectionInformation) -> str """
        ...

    @property
    def OverrideMode(self) -> OverrideMode:
        """
        Get: OverrideMode(self: SectionInformation) -> OverrideMode
        Set: OverrideMode(self: SectionInformation) = value
        """
        ...

    @property
    def OverrideModeDefault(self) -> OverrideMode:
        """
        Get: OverrideModeDefault(self: SectionInformation) -> OverrideMode
        Set: OverrideModeDefault(self: SectionInformation) = value
        """
        ...

    @property
    def OverrideModeEffective(self) -> OverrideMode:
        """ Get: OverrideModeEffective(self: SectionInformation) -> OverrideMode """
        ...

    @property
    def ProtectionProvider(self) -> ProtectedConfigurationProvider:
        """ Get: ProtectionProvider(self: SectionInformation) -> ProtectedConfigurationProvider """
        ...

    @property
    def RequirePermission(self) -> bool:
        """
        Get: RequirePermission(self: SectionInformation) -> bool
        Set: RequirePermission(self: SectionInformation) = value
        """
        ...

    @property
    def RestartOnExternalChanges(self) -> bool:
        """
        Get: RestartOnExternalChanges(self: SectionInformation) -> bool
        Set: RestartOnExternalChanges(self: SectionInformation) = value
        """
        ...

    @property
    def SectionName(self) -> str:
        """ Get: SectionName(self: SectionInformation) -> str """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: SectionInformation) -> str
        Set: Type(self: SectionInformation) = value
        """
        ...


    def ForceDeclaration(self, force:bool = ...): # -> 
        """ ForceDeclaration(self: SectionInformation)ForceDeclaration(self: SectionInformation, force: bool) """
        ...

    def GetParentSection(self) -> ConfigurationSection:
        """ GetParentSection(self: SectionInformation) -> ConfigurationSection """
        ...

    def GetRawXml(self) -> str:
        """ GetRawXml(self: SectionInformation) -> str """
        ...

    def ProtectSection(self, protectionProvider:str): # -> 
        """ ProtectSection(self: SectionInformation, protectionProvider: str) """
        ...

    def RevertToParent(self): # -> 
        """ RevertToParent(self: SectionInformation) """
        ...

    def SetRawXml(self, rawXml:str): # -> 
        """ SetRawXml(self: SectionInformation, rawXml: str) """
        ...

    def UnprotectSection(self): # -> 
        """ UnprotectSection(self: SectionInformation) """
        ...


class SettingChangingEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ SettingChangingEventArgs(settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool) """
    @property
    def NewValue(self) -> object:
        """ Get: NewValue(self: SettingChangingEventArgs) -> object """
        ...

    @property
    def SettingClass(self) -> str:
        """ Get: SettingClass(self: SettingChangingEventArgs) -> str """
        ...

    @property
    def SettingKey(self) -> str:
        """ Get: SettingKey(self: SettingChangingEventArgs) -> str """
        ...

    @property
    def SettingName(self) -> str:
        """ Get: SettingName(self: SettingChangingEventArgs) -> str """
        ...



class SettingChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SettingChangingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SettingChangingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SettingChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SettingChangingEventArgs): # -> 
        """ Invoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs) """
        ...


class SettingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SettingElement()
    SettingElement(name: str, serializeAs: SettingsSerializeAs)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SettingElement) -> str
        Set: Name(self: SettingElement) = value
        """
        ...

    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """
        Get: SerializeAs(self: SettingElement) -> SettingsSerializeAs
        Set: SerializeAs(self: SettingElement) = value
        """
        ...

    @property
    def Value(self) -> SettingValueElement:
        """
        Get: Value(self: SettingElement) -> SettingValueElement
        Set: Value(self: SettingElement) = value
        """
        ...


    def __new__(cls, name:str = ..., serializeAs:SettingsSerializeAs = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, serializeAs: SettingsSerializeAs)
        """
        ...


class SettingElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SettingElementCollection() """
    def Add(self, element:SettingElement): # -> 
        """ Add(self: SettingElementCollection, element: SettingElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SettingElementCollection) """
        ...

    def Get(self, elementKey:str) -> SettingElement:
        """ Get(self: SettingElementCollection, elementKey: str) -> SettingElement """
        ...

    def Remove(self, element:SettingElement): # -> 
        """ Remove(self: SettingElementCollection, element: SettingElement) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class SettingsAttributeDictionary(Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """
    SettingsAttributeDictionary()
    SettingsAttributeDictionary(attributes: SettingsAttributeDictionary)
    """
    pass

class SettingsContext(Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """ SettingsContext() """
    pass

class SettingsDescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsDescriptionAttribute(description: str) """
    @property
    def Description(self) -> str:
        """ Get: Description(self: SettingsDescriptionAttribute) -> str """
        ...


    def __new__(cls, description:str) -> Self:
        """ __new__(cls: type, description: str) """
        ...


class SettingsGroupDescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsGroupDescriptionAttribute(description: str) """
    @property
    def Description(self) -> str:
        """ Get: Description(self: SettingsGroupDescriptionAttribute) -> str """
        ...


    def __new__(cls, description:str) -> Self:
        """ __new__(cls: type, description: str) """
        ...


class SettingsGroupNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsGroupNameAttribute(groupName: str) """
    @property
    def GroupName(self) -> str:
        """ Get: GroupName(self: SettingsGroupNameAttribute) -> str """
        ...


    def __new__(cls, groupName:str) -> Self:
        """ __new__(cls: type, groupName: str) """
        ...


class SettingsLoadedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SettingsLoadedEventArgs(provider: SettingsProvider) """
    @property
    def Provider(self) -> SettingsProvider:
        """ Get: Provider(self: SettingsLoadedEventArgs) -> SettingsProvider """
        ...


    def __new__(cls, provider:SettingsProvider) -> Self:
        """ __new__(cls: type, provider: SettingsProvider) """
        ...


class SettingsLoadedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SettingsLoadedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SettingsLoadedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SettingsLoadedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SettingsLoadedEventArgs): # -> 
        """ Invoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs) """
        ...


class SettingsManageability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SettingsManageability, values: Roaming (0) """
    Roaming: SettingsManageability = ...
    value__ = ...


class SettingsManageabilityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsManageabilityAttribute(manageability: SettingsManageability) """
    @property
    def Manageability(self) -> SettingsManageability:
        """ Get: Manageability(self: SettingsManageabilityAttribute) -> SettingsManageability """
        ...


    def __new__(cls, manageability:SettingsManageability) -> Self:
        """ __new__(cls: type, manageability: SettingsManageability) """
        ...


class SettingsProperty: # skipped bases: <type 'object'>, <type 'object'>
    """
    SettingsProperty(name: str)
    SettingsProperty(name: str, propertyType: Type, provider: SettingsProvider, isReadOnly: bool, defaultValue: object, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: bool, throwOnErrorSerializing: bool)
    SettingsProperty(propertyToCopy: SettingsProperty)
    """
    @property
    def Attributes(self) -> SettingsAttributeDictionary:
        """ Get: Attributes(self: SettingsProperty) -> SettingsAttributeDictionary """
        ...

    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: SettingsProperty) -> object
        Set: DefaultValue(self: SettingsProperty) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: SettingsProperty) -> bool
        Set: IsReadOnly(self: SettingsProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SettingsProperty) -> str
        Set: Name(self: SettingsProperty) = value
        """
        ...

    @property
    def PropertyType(self) -> Type:
        """
        Get: PropertyType(self: SettingsProperty) -> Type
        Set: PropertyType(self: SettingsProperty) = value
        """
        ...

    @property
    def Provider(self) -> SettingsProvider:
        """
        Get: Provider(self: SettingsProperty) -> SettingsProvider
        Set: Provider(self: SettingsProperty) = value
        """
        ...

    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """
        Get: SerializeAs(self: SettingsProperty) -> SettingsSerializeAs
        Set: SerializeAs(self: SettingsProperty) = value
        """
        ...

    @property
    def ThrowOnErrorDeserializing(self) -> bool:
        """
        Get: ThrowOnErrorDeserializing(self: SettingsProperty) -> bool
        Set: ThrowOnErrorDeserializing(self: SettingsProperty) = value
        """
        ...

    @property
    def ThrowOnErrorSerializing(self) -> bool:
        """
        Get: ThrowOnErrorSerializing(self: SettingsProperty) -> bool
        Set: ThrowOnErrorSerializing(self: SettingsProperty) = value
        """
        ...



class SettingsPropertyCollection(ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ SettingsPropertyCollection() """
    def Add(self, property:SettingsProperty): # -> 
        """ Add(self: SettingsPropertyCollection, property: SettingsProperty) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SettingsPropertyCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SettingsPropertyCollection) -> IEnumerator """
        ...

    def OnAdd(self, *args): #cannot find CLR method
        """ OnAdd(self: SettingsPropertyCollection, property: SettingsProperty) """
        ...

    def OnAddComplete(self, *args): #cannot find CLR method
        """ OnAddComplete(self: SettingsPropertyCollection, property: SettingsProperty) """
        ...

    def OnClear(self, *args): #cannot find CLR method
        """ OnClear(self: SettingsPropertyCollection) """
        ...

    def OnClearComplete(self, *args): #cannot find CLR method
        """ OnClearComplete(self: SettingsPropertyCollection) """
        ...

    def OnRemove(self, *args): #cannot find CLR method
        """ OnRemove(self: SettingsPropertyCollection, property: SettingsProperty) """
        ...

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """ OnRemoveComplete(self: SettingsPropertyCollection, property: SettingsProperty) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: SettingsPropertyCollection, name: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: SettingsPropertyCollection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SettingsPropertyIsReadOnlyException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SettingsPropertyIsReadOnlyException(message: str)
    SettingsPropertyIsReadOnlyException(message: str, innerException: Exception)
    SettingsPropertyIsReadOnlyException()
    """
    SerializeObjectState = ...


class SettingsPropertyNotFoundException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SettingsPropertyNotFoundException(message: str)
    SettingsPropertyNotFoundException(message: str, innerException: Exception)
    SettingsPropertyNotFoundException()
    """
    SerializeObjectState = ...


class SettingsPropertyValue: # skipped bases: <type 'object'>, <type 'object'>
    """ SettingsPropertyValue(property: SettingsProperty) """
    @property
    def Deserialized(self) -> bool:
        """
        Get: Deserialized(self: SettingsPropertyValue) -> bool
        Set: Deserialized(self: SettingsPropertyValue) = value
        """
        ...

    @property
    def IsDirty(self) -> bool:
        """
        Get: IsDirty(self: SettingsPropertyValue) -> bool
        Set: IsDirty(self: SettingsPropertyValue) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SettingsPropertyValue) -> str """
        ...

    @property
    def Property(self) -> SettingsProperty:
        """ Get: Property(self: SettingsPropertyValue) -> SettingsProperty """
        ...

    @property
    def PropertyValue(self) -> object:
        """
        Get: PropertyValue(self: SettingsPropertyValue) -> object
        Set: PropertyValue(self: SettingsPropertyValue) = value
        """
        ...

    @property
    def SerializedValue(self) -> object:
        """
        Get: SerializedValue(self: SettingsPropertyValue) -> object
        Set: SerializedValue(self: SettingsPropertyValue) = value
        """
        ...

    @property
    def UsingDefaultValue(self) -> bool:
        """ Get: UsingDefaultValue(self: SettingsPropertyValue) -> bool """
        ...



class SettingsPropertyValueCollection(ICloneable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ SettingsPropertyValueCollection() """
    def Add(self, property:SettingsPropertyValue): # -> 
        """ Add(self: SettingsPropertyValueCollection, property: SettingsPropertyValue) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SettingsPropertyValueCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SettingsPropertyValueCollection) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: SettingsPropertyValueCollection, name: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: SettingsPropertyValueCollection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SettingsPropertyWrongTypeException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SettingsPropertyWrongTypeException(message: str)
    SettingsPropertyWrongTypeException(message: str, innerException: Exception)
    SettingsPropertyWrongTypeException()
    """
    SerializeObjectState = ...


class SettingsProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SettingsProviderAttribute(providerTypeName: str)
    SettingsProviderAttribute(providerType: Type)
    """
    @property
    def ProviderTypeName(self) -> str:
        """ Get: ProviderTypeName(self: SettingsProviderAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, providerTypeName: str)
        __new__(cls: type, providerType: Type)
        """
        ...


class SettingsProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SettingsProviderCollection() """
    pass

class SettingsSavingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SettingsSavingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SettingsSavingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelEventArgs): # -> 
        """ Invoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs) """
        ...


class SettingsSerializeAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SettingsSerializeAs, values: Binary (2), ProviderSpecific (3), String (0), Xml (1) """
    Binary: SettingsSerializeAs = ...
    ProviderSpecific: SettingsSerializeAs = ...
    String: SettingsSerializeAs = ...
    value__ = ...
    Xml: SettingsSerializeAs = ...


class SettingsSerializeAsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsSerializeAsAttribute(serializeAs: SettingsSerializeAs) """
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """ Get: SerializeAs(self: SettingsSerializeAsAttribute) -> SettingsSerializeAs """
        ...


    def __new__(cls, serializeAs:SettingsSerializeAs) -> Self:
        """ __new__(cls: type, serializeAs: SettingsSerializeAs) """
        ...


class SettingValueElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ SettingValueElement() """
    @property
    def ValueXml(self) -> XmlNode:
        """
        Get: ValueXml(self: SettingValueElement) -> XmlNode
        Set: ValueXml(self: SettingValueElement) = value
        """
        ...



class SingleTagSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ SingleTagSectionHandler() """
    pass

class SpecialSetting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SpecialSetting, values: ConnectionString (0), WebServiceUrl (1) """
    ConnectionString: SpecialSetting = ...
    value__ = ...
    WebServiceUrl: SpecialSetting = ...


class SpecialSettingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SpecialSettingAttribute(specialSetting: SpecialSetting) """
    @property
    def SpecialSetting(self) -> SpecialSetting:
        """ Get: SpecialSetting(self: SpecialSettingAttribute) -> SpecialSetting """
        ...


    def __new__(cls, specialSetting:SpecialSetting) -> Self:
        """ __new__(cls: type, specialSetting: SpecialSetting) """
        ...


class StringValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """
    StringValidator(minLength: int)
    StringValidator(minLength: int, maxLength: int)
    StringValidator(minLength: int, maxLength: int, invalidCharacters: str)
    """
    def __new__(cls, minLength:int, maxLength:int = ..., invalidCharacters:str = ...) -> Self:
        """
        __new__(cls: type, minLength: int)
        __new__(cls: type, minLength: int, maxLength: int)
        __new__(cls: type, minLength: int, maxLength: int, invalidCharacters: str)
        """
        ...


class StringValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StringValidatorAttribute() """
    @property
    def InvalidCharacters(self) -> str:
        """
        Get: InvalidCharacters(self: StringValidatorAttribute) -> str
        Set: InvalidCharacters(self: StringValidatorAttribute) = value
        """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: StringValidatorAttribute) -> int
        Set: MaxLength(self: StringValidatorAttribute) = value
        """
        ...

    @property
    def MinLength(self) -> int:
        """
        Get: MinLength(self: StringValidatorAttribute) -> int
        Set: MinLength(self: StringValidatorAttribute) = value
        """
        ...



class SubclassTypeValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ SubclassTypeValidator(baseClass: Type) """
    def __new__(cls, baseClass:Type) -> Self:
        """ __new__(cls: type, baseClass: Type) """
        ...


class SubclassTypeValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SubclassTypeValidatorAttribute(baseClass: Type) """
    @property
    def BaseClass(self) -> Type:
        """ Get: BaseClass(self: SubclassTypeValidatorAttribute) -> Type """
        ...



class TimeSpanMinutesConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ TimeSpanMinutesConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: TimeSpanMinutesConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: TimeSpanMinutesConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class TimeSpanMinutesOrInfiniteConverter(TimeSpanMinutesConverter): # skipped bases: <type 'object'>
    """ TimeSpanMinutesOrInfiniteConverter() """
    pass

class TimeSpanSecondsConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ TimeSpanSecondsConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: TimeSpanSecondsConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: TimeSpanSecondsConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class TimeSpanSecondsOrInfiniteConverter(TimeSpanSecondsConverter): # skipped bases: <type 'object'>
    """ TimeSpanSecondsOrInfiniteConverter() """
    pass

class TimeSpanValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """
    TimeSpanValidator(minValue: TimeSpan, maxValue: TimeSpan)
    TimeSpanValidator(minValue: TimeSpan, maxValue: TimeSpan, rangeIsExclusive: bool)
    TimeSpanValidator(minValue: TimeSpan, maxValue: TimeSpan, rangeIsExclusive: bool, resolutionInSeconds: Int64)
    """
    def __new__(cls, minValue:TimeSpan, maxValue:TimeSpan, rangeIsExclusive:bool = ..., resolutionInSeconds:Int64 = ...) -> Self:
        """
        __new__(cls: type, minValue: TimeSpan, maxValue: TimeSpan)
        __new__(cls: type, minValue: TimeSpan, maxValue: TimeSpan, rangeIsExclusive: bool)
        __new__(cls: type, minValue: TimeSpan, maxValue: TimeSpan, rangeIsExclusive: bool, resolutionInSeconds: Int64)
        """
        ...


class TimeSpanValidatorAttribute(ConfigurationValidatorAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TimeSpanValidatorAttribute() """
    @property
    def ExcludeRange(self) -> bool:
        """
        Get: ExcludeRange(self: TimeSpanValidatorAttribute) -> bool
        Set: ExcludeRange(self: TimeSpanValidatorAttribute) = value
        """
        ...

    @property
    def MaxValue(self) -> TimeSpan:
        """ Get: MaxValue(self: TimeSpanValidatorAttribute) -> TimeSpan """
        ...

    @property
    def MaxValueString(self) -> str:
        """
        Get: MaxValueString(self: TimeSpanValidatorAttribute) -> str
        Set: MaxValueString(self: TimeSpanValidatorAttribute) = value
        """
        ...

    @property
    def MinValue(self) -> TimeSpan:
        """ Get: MinValue(self: TimeSpanValidatorAttribute) -> TimeSpan """
        ...

    @property
    def MinValueString(self) -> str:
        """
        Get: MinValueString(self: TimeSpanValidatorAttribute) -> str
        Set: MinValueString(self: TimeSpanValidatorAttribute) = value
        """
        ...


    TimeSpanMaxValue: str = ...
    TimeSpanMinValue: str = ...


class TypeNameConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ TypeNameConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: TypeNameConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: TypeNameConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


class UriSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ UriSection() """
    @property
    def Idn(self) -> IdnElement:
        """ Get: Idn(self: UriSection) -> IdnElement """
        ...

    @property
    def IriParsing(self) -> IriParsingElement:
        """ Get: IriParsing(self: UriSection) -> IriParsingElement """
        ...

    @property
    def SchemeSettings(self) -> SchemeSettingElementCollection:
        """ Get: SchemeSettings(self: UriSection) -> SchemeSettingElementCollection """
        ...



class UserScopedSettingAttribute(SettingAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UserScopedSettingAttribute() """
    pass

class UserSettingsGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ UserSettingsGroup() """
    pass

class ValidatorCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ValidatorCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, value:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ValidatorCallback, value: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ValidatorCallback, result: IAsyncResult) """
        ...

    def Invoke(self, value:object): # -> 
        """ Invoke(self: ValidatorCallback, value: object) """
        ...


class WhiteSpaceTrimStringConverter(ConfigurationConverterBase): # skipped bases: <type 'object'>
    """ WhiteSpaceTrimStringConverter() """
    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: WhiteSpaceTrimStringConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, data: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: WhiteSpaceTrimStringConverter, ctx: ITypeDescriptorContext, ci: CultureInfo, value: object, type: Type) -> object """
        ...


# variables with complex values

