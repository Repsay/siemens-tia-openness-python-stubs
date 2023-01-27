# encoding: utf-8
# module Microsoft.SqlServer.Management.Dmf calls itself Dmf
# from Microsoft.SqlServer.Dmf, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SqlEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Dmf.Common, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Graph import DataTable

from Microsoft.SqlServer.Management.Common import (IRenamable, ISfcConnection, 
    SqlServerManagementException)

from Microsoft.SqlServer.Management.Facets import FacetEvaluationContext

from Microsoft.SqlServer.Management.Sdk.Sfc import (FilterNode, ISfcAlterable, 
    ISfcCreatable, ISfcDomain, ISfcDroppable, ISfcRenamable, ISfcScript, 
    ISfcSerializableUpgrade, ISfcValidate, SfcCollatedDictionaryCollection, 
    SfcConnection, SfcDictionaryCollection, SfcInstance, SfcObjectExtender, 
    SfcObjectFactory, SfcQueryExpression, SqlStoreConnection, UpgradeSession)

from System import (Array, Attribute, DateTime, Enum, Guid, IComparable, 
    IDisposable, Int64, Type)

from System.Collections import IEnumerable, IList

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import (KeyedCollection, 
    ReadOnlyCollection)

from System.Collections.Specialized import StringCollection

from System.ComponentModel import PropertyDescriptorCollection

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    DmfExceptionType, EnumerationMode, Function, Key, ReaderActionType, 
    SqlSmoObject, T, XmlReader, XmlWriter, XmlWriterSettings, field#)
"""

# no functions
# classes

class DmfException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DmfException()
    DmfException(message: str)
    DmfException(message: str, innerException: Exception)
    """
    @property
    def DmfExceptionType(self): # -> DmfExceptionType
        """ Get: DmfExceptionType(self: DmfException) -> DmfExceptionType """
        ...

    @property
    def ProdVer(self):
        ...


    def Init(self, *args): #cannot find CLR method
        """ Init(self: DmfException) """
        ...

    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: DmfException, resource: str) -> DmfException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class AdapterAlreadyExistsException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AdapterAlreadyExistsException()
    AdapterAlreadyExistsException(message: str)
    AdapterAlreadyExistsException(message: str, innerException: Exception)
    AdapterAlreadyExistsException(interfaceName: str, typeName: str)
    """
    @property
    def Interface(self) -> str:
        """ Get: Interface(self: AdapterAlreadyExistsException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: AdapterAlreadyExistsException) -> str """
        ...

    @property
    def ObjectType(self) -> str:
        """ Get: ObjectType(self: AdapterAlreadyExistsException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: AdapterAlreadyExistsException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class AdapterWrongNumberOfArgumentsException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AdapterWrongNumberOfArgumentsException()
    AdapterWrongNumberOfArgumentsException(message: str, innerException: Exception)
    AdapterWrongNumberOfArgumentsException(adapter: str)
    """
    @property
    def Adapter(self) -> str:
        """ Get: Adapter(self: AdapterWrongNumberOfArgumentsException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: AdapterWrongNumberOfArgumentsException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: AdapterWrongNumberOfArgumentsException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class AdHocPolicyEvaluationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AdHocPolicyEvaluationMode, values: Check (0), CheckSqlScriptAsProxy (2), Configure (1) """
    Check: AdHocPolicyEvaluationMode = ...
    CheckSqlScriptAsProxy: AdHocPolicyEvaluationMode = ...
    Configure: AdHocPolicyEvaluationMode = ...
    value__ = ...


class AssemblyAlreadyRegisteredException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AssemblyAlreadyRegisteredException()
    AssemblyAlreadyRegisteredException(message: str, innerException: Exception)
    AssemblyAlreadyRegisteredException(assemblyName: str)
    """
    @property
    def Assembly(self) -> str:
        """ Get: Assembly(self: AssemblyAlreadyRegisteredException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: AssemblyAlreadyRegisteredException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: AssemblyAlreadyRegisteredException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class AutomatedPolicyEvaluationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AutomatedPolicyEvaluationMode, values: CheckOnChanges (2), CheckOnSchedule (4), Enforce (1), None (0) """
    CheckOnChanges: AutomatedPolicyEvaluationMode = ...
    CheckOnSchedule: AutomatedPolicyEvaluationMode = ...
    Enforce: AutomatedPolicyEvaluationMode = ...
    value__ = ...


class BadEventDataException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    BadEventDataException()
    BadEventDataException(message: str, innerException: Exception)
    BadEventDataException(message: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: BadEventDataException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class BadExpressionTreeException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    BadExpressionTreeException()
    BadExpressionTreeException(message: str, innerException: Exception)
    BadExpressionTreeException(reason: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: BadExpressionTreeException) -> str """
        ...

    @property
    def Reason(self) -> str:
        """ Get: Reason(self: BadExpressionTreeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: BadExpressionTreeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class Condition(IRenamable, ISfcCreatable, ISfcDroppable, ISfcRenamable, SfcInstance, ISfcValidate, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Condition()
    Condition(parent: PolicyStore, name: str)
    """
    @property
    def CreateDate(self) -> DateTime:
        """ Get: CreateDate(self: Condition) -> DateTime """
        ...

    @property
    def CreatedBy(self) -> str:
        """ Get: CreatedBy(self: Condition) -> str """
        ...

    @property
    def DateModified(self) -> DateTime:
        """ Get: DateModified(self: Condition) -> DateTime """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Condition) -> str
        Set: Description(self: Condition) = value
        """
        ...

    @property
    def ExpressionNode(self) -> ExpressionNode:
        """
        Get: ExpressionNode(self: Condition) -> ExpressionNode
        Set: ExpressionNode(self: Condition) = value
        """
        ...

    @property
    def Facet(self) -> str:
        """
        Get: Facet(self: Condition) -> str
        Set: Facet(self: Condition) = value
        """
        ...

    @property
    def HasScript(self) -> bool:
        """ Get: HasScript(self: Condition) -> bool """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Condition) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Condition) -> Key """
        ...

    @property
    def IsEnumerable(self) -> bool:
        """ Get: IsEnumerable(self: Condition) -> bool """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: Condition) -> bool """
        ...

    @property
    def ModifiedBy(self) -> str:
        """ Get: ModifiedBy(self: Condition) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Condition) -> str """
        ...


    def Alter(self): # -> 
        """ Alter(self: Condition) """
        ...

    def Create(self): # -> 
        """ Create(self: Condition) """
        ...

    def Drop(self): # -> 
        """ Drop(self: Condition) """
        ...

    def EnumDependentPolicies(self) -> ReadOnlyCollection:
        """ EnumDependentPolicies(self: Condition) -> ReadOnlyCollection[Policy] """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def GetSupportedEvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """ GetSupportedEvaluationMode(self: Condition) -> AutomatedPolicyEvaluationMode """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def __new__(cls, parent:PolicyStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: PolicyStore, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class ConditionCollection(SfcDictionaryCollection): # skipped bases: <type 'IEnumerable[Condition]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'ICollection[Condition]'>, <type 'object'>
    """ ConditionCollection(parent: PolicyStore) """
    pass

class ConditionExtender(SfcObjectExtender): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    ConditionExtender()
    ConditionExtender(condition: Condition)
    ConditionExtender(policyStore: PolicyStore, name: str)
    """
    @property
    def DependentPolicies(self) -> ReadOnlyCollection:
        """ Get: DependentPolicies(self: ConditionExtender) -> ReadOnlyCollection[Policy] """
        ...

    @property
    def ExpressionNode(self) -> ExpressionNode:
        """
        Get: ExpressionNode(self: ConditionExtender) -> ExpressionNode
        Set: ExpressionNode(self: ConditionExtender) = value
        """
        ...

    @property
    def FacetInfo(self) -> FacetInfo:
        """
        Get: FacetInfo(self: ConditionExtender) -> FacetInfo
        Set: FacetInfo(self: ConditionExtender) = value
        """
        ...

    @property
    def Facets(self) -> ReadOnlyCollection:
        """ Get: Facets(self: ConditionExtender) -> ReadOnlyCollection[FacetInfo] """
        ...

    @property
    def RootFacets(self) -> ReadOnlyCollection:
        """ Get: RootFacets(self: ConditionExtender) -> ReadOnlyCollection[FacetInfo] """
        ...



class ConflictingPropertyValuesException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConflictingPropertyValuesException()
    ConflictingPropertyValuesException(message: str)
    ConflictingPropertyValuesException(message: str, innerException: Exception)
    ConflictingPropertyValuesException(mode: str, type1: str, name1: str, type2: str, name2: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ConflictingPropertyValuesException) -> str """
        ...

    @property
    def Mode(self) -> str:
        """ Get: Mode(self: ConflictingPropertyValuesException) -> str """
        ...

    @property
    def Name1(self) -> str:
        """ Get: Name1(self: ConflictingPropertyValuesException) -> str """
        ...

    @property
    def Name2(self) -> str:
        """ Get: Name2(self: ConflictingPropertyValuesException) -> str """
        ...

    @property
    def Type1(self) -> str:
        """ Get: Type1(self: ConflictingPropertyValuesException) -> str """
        ...

    @property
    def Type2(self) -> str:
        """ Get: Type2(self: ConflictingPropertyValuesException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ConflictingPropertyValuesException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ConnectionEvaluationHistory(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ ConnectionEvaluationHistory() """
    @property
    def EvaluationDetails(self) -> EvaluationDetailCollection:
        """ Get: EvaluationDetails(self: ConnectionEvaluationHistory) -> EvaluationDetailCollection """
        ...

    @property
    def EvaluationId(self) -> int:
        """ Get: EvaluationId(self: ConnectionEvaluationHistory) -> int """
        ...

    @property
    def Exception(self) -> str:
        """ Get: Exception(self: ConnectionEvaluationHistory) -> str """
        ...

    @property
    def ID(self) -> Int64:
        """ Get: ID(self: ConnectionEvaluationHistory) -> Int64 """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ConnectionEvaluationHistory) -> Key """
        ...

    @property
    def Result(self) -> bool:
        """ Get: Result(self: ConnectionEvaluationHistory) -> bool """
        ...

    @property
    def ServerInstance(self) -> str:
        """ Get: ServerInstance(self: ConnectionEvaluationHistory) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(id: Int64)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class ConnectionEvaluationHistoryCollection(SfcDictionaryCollection): # skipped bases: <type 'IEnumerable[ConnectionEvaluationHistory]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'ICollection[ConnectionEvaluationHistory]'>, <type 'object'>
    """ ConnectionEvaluationHistoryCollection(parent: EvaluationHistory) """
    pass

class ConversionNotSupportedException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConversionNotSupportedException()
    ConversionNotSupportedException(message: str)
    ConversionNotSupportedException(message: str, innerException: Exception)
    ConversionNotSupportedException(host: str, typeName: str)
    """
    @property
    def Host(self) -> str:
        """ Get: Host(self: ConversionNotSupportedException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ConversionNotSupportedException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ConversionNotSupportedException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ConversionNotSupportedException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class DmfConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    MICROSOFT_SQLSERVER_PUBLIC_KEY: str = ...
    __all__: list = ...


class DmfExceptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DmfExceptionType, values: AdapterAlreadyExists (2), AdapterWrongNumberOfArguments (3), AssemblyAlreadyRegistered (1), BadEventData (25), BadExpressionTree (12), ConflictingPropertyValues (20), ConversionNotSupported (15), DmfException (0), DmfSecurity (18), ExpressionNodeNotConfigurable (14), ExpressionNodeNotConfigurableOperator (27), ExpressionSerialization (9), ExpressionTypeMistmatch (4), FailedOperation (26), FunctionBadDatePart (35), FunctionNoServer (33), FunctionNotASmoObject (34), FunctionTooManyColumns (36), FunctionWrongArgumentsNumber (7), FunctionWrongArgumentType (6), FunctionWrongReturnType (32), InvalidInOperator (17), InvalidOperand (16), MissingJobSchedule (24), MissingObject (22), MissingProperty (29), MissingTypeFacetAssociation (31), NonConfigurableReadOnlyProperty (28), NonRetrievableProperty (30), NoTargetSetEnabled (40), NullFacet (8), ObjectAlreadyExists (21), ObjectValidation (19), OperatorNotApplicable (5), PolicyEvaluation (23), RestartPending (41), StringPropertyTooLong (37), TargetSetCountMismatch (38), TypeConversion (10), UnsupportedObjectType (13), UnsupportedTargetSetForFacet (39), UnsupportedType (11) """
    AdapterAlreadyExists: DmfExceptionType = ...
    AdapterWrongNumberOfArguments: DmfExceptionType = ...
    AssemblyAlreadyRegistered: DmfExceptionType = ...
    BadEventData: DmfExceptionType = ...
    BadExpressionTree: DmfExceptionType = ...
    ConflictingPropertyValues: DmfExceptionType = ...
    ConversionNotSupported: DmfExceptionType = ...
    DmfException: DmfExceptionType = ...
    DmfSecurity: DmfExceptionType = ...
    ExpressionNodeNotConfigurable: DmfExceptionType = ...
    ExpressionNodeNotConfigurableOperator: DmfExceptionType = ...
    ExpressionSerialization: DmfExceptionType = ...
    ExpressionTypeMistmatch: DmfExceptionType = ...
    FailedOperation: DmfExceptionType = ...
    FunctionBadDatePart: DmfExceptionType = ...
    FunctionNoServer: DmfExceptionType = ...
    FunctionNotASmoObject: DmfExceptionType = ...
    FunctionTooManyColumns: DmfExceptionType = ...
    FunctionWrongArgumentsNumber: DmfExceptionType = ...
    FunctionWrongArgumentType: DmfExceptionType = ...
    FunctionWrongReturnType: DmfExceptionType = ...
    InvalidInOperator: DmfExceptionType = ...
    InvalidOperand: DmfExceptionType = ...
    MissingJobSchedule: DmfExceptionType = ...
    MissingObject: DmfExceptionType = ...
    MissingProperty: DmfExceptionType = ...
    MissingTypeFacetAssociation: DmfExceptionType = ...
    NonConfigurableReadOnlyProperty: DmfExceptionType = ...
    NonRetrievableProperty: DmfExceptionType = ...
    NoTargetSetEnabled: DmfExceptionType = ...
    NullFacet: DmfExceptionType = ...
    ObjectAlreadyExists: DmfExceptionType = ...
    ObjectValidation: DmfExceptionType = ...
    OperatorNotApplicable: DmfExceptionType = ...
    PolicyEvaluation: DmfExceptionType = ...
    RestartPending: DmfExceptionType = ...
    StringPropertyTooLong: DmfExceptionType = ...
    TargetSetCountMismatch: DmfExceptionType = ...
    TypeConversion: DmfExceptionType = ...
    UnsupportedObjectType: DmfExceptionType = ...
    UnsupportedTargetSetForFacet: DmfExceptionType = ...
    UnsupportedType: DmfExceptionType = ...
    value__ = ...


class EvaluationDetail(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ EvaluationDetail() """
    @property
    def EvaluationDate(self) -> DateTime:
        """ Get: EvaluationDate(self: EvaluationDetail) -> DateTime """
        ...

    @property
    def Exception(self) -> str:
        """ Get: Exception(self: EvaluationDetail) -> str """
        ...

    @property
    def HistoryId(self) -> int:
        """ Get: HistoryId(self: EvaluationDetail) -> int """
        ...

    @property
    def ID(self) -> Int64:
        """ Get: ID(self: EvaluationDetail) -> Int64 """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: EvaluationDetail) -> Key """
        ...

    @property
    def Result(self) -> bool:
        """ Get: Result(self: EvaluationDetail) -> bool """
        ...

    @property
    def ResultDetail(self) -> str:
        """ Get: ResultDetail(self: EvaluationDetail) -> str """
        ...

    @property
    def TargetQueryExpression(self) -> str:
        """ Get: TargetQueryExpression(self: EvaluationDetail) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(id: Int64)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class EvaluationDetailCollection(SfcDictionaryCollection): # skipped bases: <type 'ICollection[EvaluationDetail]'>, <type 'IEnumerable[EvaluationDetail]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ EvaluationDetailCollection(parent: ConnectionEvaluationHistory) """
    pass

class EvaluationFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsTypeSupported(type:Type) -> bool:
        """ IsTypeSupported(type: Type) -> bool """
        ...

    @staticmethod
    def IsTypeSupportedForConstant(type:Type) -> bool:
        """ IsTypeSupportedForConstant(type: Type) -> bool """
        ...

    @staticmethod
    def LikeToRegex(likePattern:str) -> str:
        """ LikeToRegex(likePattern: str) -> str """
        ...

    @staticmethod
    def SupportedOperators(*__args:Type) -> List:
        """
        SupportedOperators(type: Type) -> List[OperatorType]
        SupportedOperators(typeClass: TypeClass) -> List[OperatorType]
        """
        ...


class EvaluationHistory(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ EvaluationHistory() """
    @property
    def ConnectionEvaluationHistories(self) -> ConnectionEvaluationHistoryCollection:
        """ Get: ConnectionEvaluationHistories(self: EvaluationHistory) -> ConnectionEvaluationHistoryCollection """
        ...

    @property
    def EndDate(self) -> DateTime:
        """ Get: EndDate(self: EvaluationHistory) -> DateTime """
        ...

    @property
    def Exception(self) -> str:
        """ Get: Exception(self: EvaluationHistory) -> str """
        ...

    @property
    def ID(self) -> Int64:
        """ Get: ID(self: EvaluationHistory) -> Int64 """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: EvaluationHistory) -> Key """
        ...

    @property
    def PolicyName(self) -> str:
        """ Get: PolicyName(self: EvaluationHistory) -> str """
        ...

    @property
    def Result(self) -> bool:
        """ Get: Result(self: EvaluationHistory) -> bool """
        ...

    @property
    def StartDate(self) -> DateTime:
        """ Get: StartDate(self: EvaluationHistory) -> DateTime """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(id: Int64)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class EvaluationHistoryCollection(SfcDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[EvaluationHistory]'>, <type 'ICollection[EvaluationHistory]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ EvaluationHistoryCollection(parent: Policy) """
    pass

class ExpressionNode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LastEvaluationResult(self):
        ...

    @property
    def Tag(self) -> str:
        """
        Get: Tag(self: ExpressionNode) -> str
        Set: Tag(self: ExpressionNode) = value
        """
        ...

    @property
    def Type(self) -> ExpressionNodeType:
        """ Get: Type(self: ExpressionNode) -> ExpressionNodeType """
        ...

    @property
    def TypeClass(self) -> TypeClass:
        """ Get: TypeClass(self: ExpressionNode) -> TypeClass """
        ...


    @staticmethod
    def ConstructNode(obj:object) -> ExpressionNode:
        """ ConstructNode(obj: object) -> ExpressionNode """
        ...

    @staticmethod
    def ConvertFromFilterNode(filterNode:FilterNode, facet:Type = ...) -> ExpressionNode:
        """
        ConvertFromFilterNode(filterNode: FilterNode) -> ExpressionNode
        ConvertFromFilterNode(filterNode: FilterNode, facet: Type) -> ExpressionNode
        """
        ...

    def ConvertFromString(self, *args): #cannot find CLR method
        """ ConvertFromString(stringObjType: str, stringValue: str) -> object """
        ...

    def ConvertToFilterNode(self) -> FilterNode:
        """ ConvertToFilterNode(self: ExpressionNode) -> FilterNode """
        ...

    def ConvertToIntWithCheck(self, *args): #cannot find CLR method
        """ ConvertToIntWithCheck(value: str) -> int """
        ...

    def ConvertToString(self, *args): #cannot find CLR method
        """ ConvertToString(value: object) -> str """
        ...

    def DeepClone(self) -> ExpressionNode:
        """ DeepClone(self: ExpressionNode) -> ExpressionNode """
        ...

    @staticmethod
    def Deserialize(*__args:str) -> ExpressionNode:
        """
        Deserialize(value: str) -> ExpressionNode
        Deserialize(xr: XmlReader) -> ExpressionNode
        """
        ...

    def DeserializeProperties(self, *args): #cannot find CLR method
        """ DeserializeProperties(self: ExpressionNode, xr: XmlReader, includeResult: bool) """
        ...

    def DeserializeResult(self, *args): #cannot find CLR method
        """ DeserializeResult(self: ExpressionNode, xr: XmlReader) """
        ...

    @staticmethod
    def DeserializeWithResult(value:str) -> ExpressionNode:
        """ DeserializeWithResult(value: str) -> ExpressionNode """
        ...

    def DoConvertToFilterNode(self, *args): #cannot find CLR method
        """ DoConvertToFilterNode(self: ExpressionNode) -> FilterNode """
        ...

    def DoEnumAttributes(self, *args): #cannot find CLR method
        """ DoEnumAttributes(self: ExpressionNode, list: List[str]) """
        ...

    def EnumChildren(self) -> IEnumerable:
        """ EnumChildren(self: ExpressionNode) -> IEnumerable[ExpressionNode] """
        ...

    def EqualProperties(self, *args): #cannot find CLR method
        """ EqualProperties(self: ExpressionNode, obj: object) -> bool """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ExpressionNode, obj: object) -> bool """
        ...

    def Evaluate(self, context:FacetEvaluationContext, checkSqlScriptAsProxy:bool = ...) -> object:
        """
        Evaluate(self: ExpressionNode, context: FacetEvaluationContext) -> object
        Evaluate(self: ExpressionNode, context: FacetEvaluationContext, checkSqlScriptAsProxy: bool) -> object
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExpressionNode) -> int """
        ...

    def GetResult(self) -> object:
        """ GetResult(self: ExpressionNode) -> object """
        ...

    def GetResultString(self) -> str:
        """ GetResultString(self: ExpressionNode) -> str """
        ...

    @staticmethod
    def MatchType(value:str): # -> T
        """ MatchType[T](value: str) -> T """
        ...

    def MoveToElementWithCheck(self, *args): #cannot find CLR method
        """ MoveToElementWithCheck(xr: XmlReader, name: str) """
        ...

    @staticmethod
    def Parse(input:str, facet:Type = ...) -> ExpressionNode:
        """
        Parse(input: str) -> ExpressionNode
        Parse(input: str, facet: Type) -> ExpressionNode
        """
        ...

    def ReadElementWithCheck(self, *args): #cannot find CLR method
        """ ReadElementWithCheck(xr: XmlReader, name: str) -> str """
        ...

    def ReadEndElement(self, *args): #cannot find CLR method
        """ ReadEndElement(self: ExpressionNode, xr: XmlReader) """
        ...

    def ReadNodeWithCheck(self, *args): #cannot find CLR method
        """ ReadNodeWithCheck(xr: XmlReader, *elements: Array[str]) -> List[str] """
        ...

    def ReadSimpleNodeWithCheck(self, *args): #cannot find CLR method
        """ ReadSimpleNodeWithCheck(xr: XmlReader, type: ExpressionNodeType, *elements: Array[str]) -> List[str] """
        ...

    def ReadWithCheck(self, *args): #cannot find CLR method
        """ ReadWithCheck(xr: XmlReader, nodeType: XmlNodeType, name: str) """
        ...

    def ResolveEnum(self, *args): #cannot find CLR method
        """ ResolveEnum(stringObjType: str, stringValue: str) -> object """
        ...

    def Serialize(self, xmlWriter): # ->  # Not found arg types: {'xmlWriter': 'XmlWriter'}
        """ Serialize(self: ExpressionNode, xmlWriter: XmlWriter) """
        ...

    @staticmethod
    def SerializeNode(node:ExpressionNode) -> str:
        """ SerializeNode(node: ExpressionNode) -> str """
        ...

    @staticmethod
    def SerializeNodeWithResult(node:ExpressionNode) -> str:
        """ SerializeNodeWithResult(node: ExpressionNode) -> str """
        ...

    def SerializeProperties(self, *args): #cannot find CLR method
        """ SerializeProperties(self: ExpressionNode, xw: XmlWriter, includeResult: bool) """
        ...

    def SerializeResult(self, *args): #cannot find CLR method
        """ SerializeResult(self: ExpressionNode, xw: XmlWriter) """
        ...

    def SetFilterNodeCompatible(self, *args): #cannot find CLR method
        """ SetFilterNodeCompatible(self: ExpressionNode, value: bool) """
        ...

    def SetHasScript(self, *args): #cannot find CLR method
        """ SetHasScript(self: ExpressionNode, value: bool) """
        ...

    def SetNameConditionType(self, *args): #cannot find CLR method
        """ SetNameConditionType(self: ExpressionNode, value: NameConditionType) """
        ...

    def SetNodeType(self, *args): #cannot find CLR method
        """ SetNodeType(self: ExpressionNode, value: ExpressionNodeType) """
        ...

    def SetObjectName(self, *args): #cannot find CLR method
        """ SetObjectName(self: ExpressionNode, value: str) """
        ...

    def SetProperties(self, *args): #cannot find CLR method
        """ SetProperties(self: ExpressionNode) """
        ...

    def SetTypeClass(self, *args): #cannot find CLR method
        """ SetTypeClass(self: ExpressionNode, value: TypeClass) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ExpressionNode) -> str """
        ...

    def ToStringForDisplay(self) -> str:
        """ ToStringForDisplay(self: ExpressionNode) -> str """
        ...

    def ToStringForUrn(self) -> str:
        """ ToStringForUrn(self: ExpressionNode) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ExpressionNodeAttribute(ExpressionNode): # skipped bases: <type 'object'>
    """
    ExpressionNodeAttribute(name: str)
    ExpressionNodeAttribute(name: str, facet: Type)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ExpressionNodeAttribute) -> str """
        ...


    def __new__(cls, name:str, facet:Type = ...) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, facet: Type)
        """
        ...


class ExpressionNodeChildren(ExpressionNode): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChildrenList(self):
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ExpressionNodeChildren) -> int """
        ...

    @property
    def EnumerableChildrenList(self) -> IEnumerable:
        """ Get: EnumerableChildrenList(self: ExpressionNodeChildren) -> IEnumerable[ExpressionNode] """
        ...


    def Add(self, *args): #cannot find CLR method
        """ Add(self: ExpressionNodeChildren, node: ExpressionNode) """
        ...


class ExpressionNodeConfigurationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpressionNodeConfigurationException()
    ExpressionNodeConfigurationException(message: str)
    ExpressionNodeConfigurationException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ExpressionNodeConfigurationException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ExpressionNodeConfigurationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ExpressionNodeConstant(ExpressionNode): # skipped bases: <type 'object'>
    """ ExpressionNodeConstant(obj: object) """
    @property
    def Value(self) -> object:
        """ Get: Value(self: ExpressionNodeConstant) -> object """
        ...


    def __new__(cls, obj:object) -> Self:
        """ __new__(cls: type, obj: object) """
        ...


class ExpressionNodeFunction(ExpressionNodeChildren): # skipped bases: <type 'object'>
    """ ExpressionNodeFunction(functionType: Function, *args: Array[ExpressionNode]) """
    @property
    def FunctionsDefinitions(self) -> Dictionary:
        """ Get: FunctionsDefinitions() -> Dictionary[Function, Array[TypeClass]] """
        ...

    @property
    def FunctionType(self): # -> Function
        """ Get: FunctionType(self: ExpressionNodeFunction) -> Function """
        ...

    @property
    def ReturnType(self) -> TypeClass:
        """ Get: ReturnType(self: ExpressionNodeFunction) -> TypeClass """
        ...


    def DeepClone(self) -> ExpressionNode:
        """ DeepClone(self: ExpressionNodeFunction) -> ExpressionNode """
        ...

    def Function(self, *args): #cannot find CLR method
        """ enum Function, values: Add (11), Array (10), Avg (6), BitwiseAnd (15), BitwiseOr (16), Concatenate (28), Count (7), DateAdd (3), DatePart (4), DateTime (21), Divide (14), Enum (20), Escape (29), ExecuteSql (0), ExecuteWql (1), False (24), GetDate (2), Guid (25), IsNull (9), Len (8), Lower (27), Mod (18), Multiply (13), Power (17), Round (19), String (22), Subtract (12), Sum (5), True (23), Upper (26) """
        ...

    def ToStringForDisplay(self) -> str:
        """ ToStringForDisplay(self: ExpressionNodeFunction) -> str """
        ...

    def __new__(cls, functionType, args:Array) -> Self: # Not found arg types: {'functionType': 'Function'}
        """ __new__(cls: type, functionType: Function, *args: Array[ExpressionNode]) """
        ...



class ExpressionNodeGroup(ExpressionNodeChildren): # skipped bases: <type 'object'>
    """ ExpressionNodeGroup(node: ExpressionNode) """
    @property
    def Group(self) -> ExpressionNode:
        """
        Get: Group(self: ExpressionNodeGroup) -> ExpressionNode
        Set: Group(self: ExpressionNodeGroup) = value
        """
        ...


    def DeepClone(self) -> ExpressionNode:
        """ DeepClone(self: ExpressionNodeGroup) -> ExpressionNode """
        ...

    def __new__(cls, node:ExpressionNode) -> Self:
        """ __new__(cls: type, node: ExpressionNode) """
        ...


class ExpressionNodeNotConfigurableException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpressionNodeNotConfigurableException()
    ExpressionNodeNotConfigurableException(subtype: str)
    ExpressionNodeNotConfigurableException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ExpressionNodeNotConfigurableException) -> str """
        ...

    @property
    def Subtype(self) -> str:
        """ Get: Subtype(self: ExpressionNodeNotConfigurableException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ExpressionNodeNotConfigurableException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ExpressionNodeNotConfigurableOperatorException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpressionNodeNotConfigurableOperatorException()
    ExpressionNodeNotConfigurableOperatorException(message: str)
    ExpressionNodeNotConfigurableOperatorException(propertyName: str, expression: str)
    ExpressionNodeNotConfigurableOperatorException(message: str, innerException: Exception)
    """
    @property
    def Expression(self) -> str:
        """ Get: Expression(self: ExpressionNodeNotConfigurableOperatorException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ExpressionNodeNotConfigurableOperatorException) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: ExpressionNodeNotConfigurableOperatorException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ExpressionNodeNotConfigurableOperatorException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ExpressionNodeOperator(ExpressionNodeChildren): # skipped bases: <type 'object'>
    """ ExpressionNodeOperator(type: OperatorType, left: ExpressionNode, right: ExpressionNode) """
    @property
    def Left(self) -> ExpressionNode:
        """
        Get: Left(self: ExpressionNodeOperator) -> ExpressionNode
        Set: Left(self: ExpressionNodeOperator) = value
        """
        ...

    @property
    def OpType(self) -> OperatorType:
        """ Get: OpType(self: ExpressionNodeOperator) -> OperatorType """
        ...

    @property
    def Right(self) -> ExpressionNode:
        """
        Get: Right(self: ExpressionNodeOperator) -> ExpressionNode
        Set: Right(self: ExpressionNodeOperator) = value
        """
        ...


    def DeepClone(self) -> ExpressionNode:
        """ DeepClone(self: ExpressionNodeOperator) -> ExpressionNode """
        ...

    @staticmethod
    def OperatorTypeFromString(opType:str) -> OperatorType:
        """ OperatorTypeFromString(opType: str) -> OperatorType """
        ...

    @staticmethod
    def OperatorTypeToString(type:OperatorType) -> str:
        """ OperatorTypeToString(type: OperatorType) -> str """
        ...

    @staticmethod
    def SupportedFilterOperators(type:Type, mode:AutomatedPolicyEvaluationMode) -> List:
        """ SupportedFilterOperators(type: Type, mode: AutomatedPolicyEvaluationMode) -> List[OperatorType] """
        ...

    def __new__(cls, type:OperatorType, left:ExpressionNode, right:ExpressionNode) -> Self:
        """ __new__(cls: type, type: OperatorType, left: ExpressionNode, right: ExpressionNode) """
        ...


class ExpressionNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExpressionNodeType, values: Attribute (2), Base (0), Constant (1), Function (4), Group (5), Operator (3) """
    Attribute: ExpressionNodeType = ...
    Base: ExpressionNodeType = ...
    Constant: ExpressionNodeType = ...
    Function: ExpressionNodeType = ...
    Group: ExpressionNodeType = ...
    Operator: ExpressionNodeType = ...
    value__ = ...


class ExpressionSerializationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpressionSerializationException()
    ExpressionSerializationException(message: str)
    ExpressionSerializationException(message: str, innerException: Exception)
    ExpressionSerializationException(nameRead: str, nameExpected: str)
    ExpressionSerializationException(typeRead: str, nameRead: str, typeExpected: str, nameExpected: str)
    """
    @property
    def ActionType(self): # -> ReaderActionType
        """ Get: ActionType(self: ExpressionSerializationException) -> ReaderActionType """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ExpressionSerializationException) -> str """
        ...

    @property
    def NameExpected(self) -> str:
        """ Get: NameExpected(self: ExpressionSerializationException) -> str """
        ...

    @property
    def NameRead(self) -> str:
        """ Get: NameRead(self: ExpressionSerializationException) -> str """
        ...

    @property
    def TypeExpected(self) -> str:
        """ Get: TypeExpected(self: ExpressionSerializationException) -> str """
        ...

    @property
    def TypeRead(self) -> str:
        """ Get: TypeRead(self: ExpressionSerializationException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ExpressionSerializationException, info: SerializationInfo, context: StreamingContext) """
        ...

    def ReaderActionType(self, *args): #cannot find CLR method
        """ enum ReaderActionType, values: Move (1), Read (2), Undefined (0) """
        ...

    SerializeObjectState = ...


class ExpressionTypeMistmatchException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExpressionTypeMistmatchException()
    ExpressionTypeMistmatchException(message: str)
    ExpressionTypeMistmatchException(message: str, innerException: Exception)
    ExpressionTypeMistmatchException(typeLeft: str, typeRight: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ExpressionTypeMistmatchException) -> str """
        ...

    @property
    def TypeLeft(self) -> str:
        """ Get: TypeLeft(self: ExpressionTypeMistmatchException) -> str """
        ...

    @property
    def TypeRight(self) -> str:
        """ Get: TypeRight(self: ExpressionTypeMistmatchException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ExpressionTypeMistmatchException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FacetInfo(IDisposable, IComparable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: FacetInfo) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: FacetInfo) -> str """
        ...

    @property
    def EvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """ Get: EvaluationMode(self: FacetInfo) -> AutomatedPolicyEvaluationMode """
        ...

    @property
    def FacetProperties(self) -> ReadOnlyCollection:
        """ Get: FacetProperties(self: FacetInfo) -> ReadOnlyCollection[PropertyInfo] """
        ...

    @property
    def FacetPropertyDescriptors(self) -> PropertyDescriptorCollection:
        """ Get: FacetPropertyDescriptors(self: FacetInfo) -> PropertyDescriptorCollection """
        ...

    @property
    def FacetType(self) -> Type:
        """ Get: FacetType(self: FacetInfo) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FacetInfo) -> str """
        ...

    @property
    def TargetTypes(self) -> ReadOnlyCollection:
        """ Get: TargetTypes(self: FacetInfo) -> ReadOnlyCollection[Type] """
        ...


    def GetTargetProperty(self, propName:str, target:object) -> object:
        """ GetTargetProperty(self: FacetInfo, propName: str, target: object) -> object """
        ...

    def ToString(self) -> str:
        """ ToString(self: FacetInfo) -> str """
        ...


class FacetInfoCollection(KeyedCollection): # skipped bases: <type 'ICollection[FacetInfo]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[FacetInfo]'>, <type 'IList[FacetInfo]'>, <type 'IEnumerable[FacetInfo]'>, <type 'ICollection'>, <type 'IReadOnlyList[FacetInfo]'>, <type 'object'>
    """ FacetInfoCollection() """
    pass

class FailedOperationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FailedOperationException()
    FailedOperationException(message: str)
    FailedOperationException(message: str, innerException: Exception)
    FailedOperationException(operation: str, failedObjectName: str, failedObjectType: str, innerException: Exception)
    """
    @property
    def FailedObjectName(self) -> str:
        """
        Get: FailedObjectName(self: FailedOperationException) -> str
        Set: FailedObjectName(self: FailedOperationException) = value
        """
        ...

    @property
    def FailedObjectType(self) -> str:
        """
        Get: FailedObjectType(self: FailedOperationException) -> str
        Set: FailedObjectType(self: FailedOperationException) = value
        """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FailedOperationException) -> str """
        ...

    @property
    def Operation(self) -> str:
        """
        Get: Operation(self: FailedOperationException) -> str
        Set: Operation(self: FailedOperationException) = value
        """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FailedOperationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionBadDatePartException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionBadDatePartException()
    FunctionBadDatePartException(message: str, innerException: Exception)
    FunctionBadDatePartException(message: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionBadDatePartException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionNoServerException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionNoServerException()
    FunctionNoServerException(message: str, innerException: Exception)
    FunctionNoServerException(message: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionNoServerException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionNotASmoObjectException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionNotASmoObjectException()
    FunctionNotASmoObjectException(message: str)
    FunctionNotASmoObjectException(message: str, innerException: Exception)
    FunctionNotASmoObjectException(functionName: str, targetType: str)
    """
    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: FunctionNotASmoObjectException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FunctionNotASmoObjectException) -> str """
        ...

    @property
    def TargetType(self) -> str:
        """ Get: TargetType(self: FunctionNotASmoObjectException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionNotASmoObjectException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionTooManyColumnsException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionTooManyColumnsException()
    FunctionTooManyColumnsException(message: str, innerException: Exception)
    FunctionTooManyColumnsException(message: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionTooManyColumnsException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionWrongArgumentsNumberException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionWrongArgumentsNumberException()
    FunctionWrongArgumentsNumberException(message: str)
    FunctionWrongArgumentsNumberException(message: str, innerException: Exception)
    FunctionWrongArgumentsNumberException(functionName: str, receivedCount: int, expectedCount: int)
    """
    @property
    def ExpectedCount(self) -> int:
        """ Get: ExpectedCount(self: FunctionWrongArgumentsNumberException) -> int """
        ...

    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: FunctionWrongArgumentsNumberException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FunctionWrongArgumentsNumberException) -> str """
        ...

    @property
    def ReceivedCount(self) -> int:
        """ Get: ReceivedCount(self: FunctionWrongArgumentsNumberException) -> int """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionWrongArgumentsNumberException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionWrongArgumentTypeException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionWrongArgumentTypeException()
    FunctionWrongArgumentTypeException(message: str)
    FunctionWrongArgumentTypeException(message: str, innerException: Exception)
    FunctionWrongArgumentTypeException(functionName: str, receivedType: str, expectedType: str)
    """
    @property
    def ExpectedType(self) -> str:
        """ Get: ExpectedType(self: FunctionWrongArgumentTypeException) -> str """
        ...

    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: FunctionWrongArgumentTypeException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FunctionWrongArgumentTypeException) -> str """
        ...

    @property
    def ReceivedType(self) -> str:
        """ Get: ReceivedType(self: FunctionWrongArgumentTypeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionWrongArgumentTypeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class FunctionWrongReturnTypeException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    FunctionWrongReturnTypeException()
    FunctionWrongReturnTypeException(message: str)
    FunctionWrongReturnTypeException(message: str, innerException: Exception)
    FunctionWrongReturnTypeException(functionName: str, receivedType: str, expectedType: str)
    """
    @property
    def ExpectedType(self) -> str:
        """ Get: ExpectedType(self: FunctionWrongReturnTypeException) -> str """
        ...

    @property
    def FunctionName(self) -> str:
        """ Get: FunctionName(self: FunctionWrongReturnTypeException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: FunctionWrongReturnTypeException) -> str """
        ...

    @property
    def ReceivedType(self) -> str:
        """ Get: ReceivedType(self: FunctionWrongReturnTypeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: FunctionWrongReturnTypeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ImportPolicyEnabledState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImportPolicyEnabledState, values: Disable (2), Enable (1), Unchanged (0) """
    Disable: ImportPolicyEnabledState = ...
    Enable: ImportPolicyEnabledState = ...
    Unchanged: ImportPolicyEnabledState = ...
    value__ = ...


class InvalidInOperatorException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidInOperatorException()
    InvalidInOperatorException(message: str, innerException: Exception)
    InvalidInOperatorException(opType: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: InvalidInOperatorException) -> str """
        ...

    @property
    def OperatorType(self) -> str:
        """
        Get: OperatorType(self: InvalidInOperatorException) -> str
        Set: OperatorType(self: InvalidInOperatorException) = value
        """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: InvalidInOperatorException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class InvalidOperandException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidOperandException()
    InvalidOperandException(message: str)
    InvalidOperandException(message: str, innerException: Exception)
    InvalidOperandException(nodeType: str, operand: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: InvalidOperandException) -> str """
        ...

    @property
    def NodeType(self) -> str:
        """ Get: NodeType(self: InvalidOperandException) -> str """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: InvalidOperandException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: InvalidOperandException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class MissingJobScheduleException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingJobScheduleException()
    MissingJobScheduleException(message: str)
    MissingJobScheduleException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: MissingJobScheduleException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class MissingObjectException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingObjectException()
    MissingObjectException(message: str)
    MissingObjectException(message: str, innerException: Exception)
    MissingObjectException(objectType: str, objectName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: MissingObjectException) -> str """
        ...

    @property
    def ObjectName(self) -> str:
        """ Get: ObjectName(self: MissingObjectException) -> str """
        ...

    @property
    def ObjectType(self) -> str:
        """ Get: ObjectType(self: MissingObjectException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: MissingObjectException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class MissingPropertyException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingPropertyException()
    MissingPropertyException(propertyName: str)
    MissingPropertyException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: MissingPropertyException) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: MissingPropertyException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: MissingPropertyException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class MissingTypeFacetAssociationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingTypeFacetAssociationException()
    MissingTypeFacetAssociationException(message: str)
    MissingTypeFacetAssociationException(message: str, innerException: Exception)
    MissingTypeFacetAssociationException(typeName: str, facet: str)
    """
    @property
    def Facet(self) -> str:
        """ Get: Facet(self: MissingTypeFacetAssociationException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: MissingTypeFacetAssociationException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: MissingTypeFacetAssociationException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: MissingTypeFacetAssociationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class NameConditionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NameConditionType, values: Equal (1), Like (2), None (0), NotEqual (3), NotLike (4) """
    Equal: NameConditionType = ...
    Like: NameConditionType = ...
    NotEqual: NameConditionType = ...
    NotLike: NameConditionType = ...
    value__ = ...


class NonConfigurableReadOnlyPropertyException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NonConfigurableReadOnlyPropertyException()
    NonConfigurableReadOnlyPropertyException(propertyName: str)
    NonConfigurableReadOnlyPropertyException(message: str, innerException: Exception)
    NonConfigurableReadOnlyPropertyException(message: str, propertyName: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: NonConfigurableReadOnlyPropertyException) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: NonConfigurableReadOnlyPropertyException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: NonConfigurableReadOnlyPropertyException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class NonRetrievablePropertyException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NonRetrievablePropertyException()
    NonRetrievablePropertyException(propertyName: str)
    NonRetrievablePropertyException(propertyName: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: NonRetrievablePropertyException) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: NonRetrievablePropertyException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: NonRetrievablePropertyException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class NoTargetSetEnabledException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NoTargetSetEnabledException()
    NoTargetSetEnabledException(objectSetName: str)
    NoTargetSetEnabledException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: NoTargetSetEnabledException) -> str """
        ...

    @property
    def ObjectSetName(self) -> str:
        """ Get: ObjectSetName(self: NoTargetSetEnabledException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: NoTargetSetEnabledException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class NullFacetException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NullFacetException()
    NullFacetException(facet: str)
    NullFacetException(message: str, innerException: Exception)
    """
    @property
    def Facet(self) -> str:
        """ Get: Facet(self: NullFacetException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: NullFacetException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: NullFacetException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ObjectAlreadyExistsException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ObjectAlreadyExistsException()
    ObjectAlreadyExistsException(message: str)
    ObjectAlreadyExistsException(message: str, innerException: Exception)
    ObjectAlreadyExistsException(objectType: str, objectName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ObjectAlreadyExistsException) -> str """
        ...

    @property
    def ObjectName(self) -> str:
        """ Get: ObjectName(self: ObjectAlreadyExistsException) -> str """
        ...

    @property
    def ObjectType(self) -> str:
        """ Get: ObjectType(self: ObjectAlreadyExistsException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ObjectAlreadyExistsException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ObjectSet(ISfcDroppable, SfcInstance, ISfcValidate, ISfcCreatable, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    ObjectSet()
    ObjectSet(parent: PolicyStore, name: str)
    """
    @property
    def Facet(self) -> str:
        """
        Get: Facet(self: ObjectSet) -> str
        Set: Facet(self: ObjectSet) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ObjectSet) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ObjectSet) -> Key """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: ObjectSet) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ObjectSet) -> str """
        ...

    @property
    def TargetSets(self) -> TargetSetCollection:
        """ Get: TargetSets(self: ObjectSet) -> TargetSetCollection """
        ...


    def Alter(self): # -> 
        """ Alter(self: ObjectSet) """
        ...

    def CalculateTargets(self, *__args:ISfcConnection) -> IEnumerable:
        """
        CalculateTargets(self: ObjectSet, targetConnection: ISfcConnection) -> IEnumerable
        CalculateTargets(targetConnection: ISfcConnection, sfcQueryExpression: SfcQueryExpression) -> IEnumerable
        CalculateTargets(self: ObjectSet, sqlStoreConnection: SqlStoreConnection, policyCategory: str) -> IEnumerable
        CalculateTargets(self: ObjectSet, targetConnection: SqlStoreConnection, condition: Condition, evaluationMode: AdHocPolicyEvaluationMode, policyCategory: str) -> (Array[object], Array[TargetEvaluation])
        """
        ...

    def Create(self): # -> 
        """ Create(self: ObjectSet) """
        ...

    def Drop(self): # -> 
        """ Drop(self: ObjectSet) """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def SetFacetWithDomain(self, facet:str, domain:str): # -> 
        """ SetFacetWithDomain(self: ObjectSet, facet: str, domain: str) """
        ...

    def __new__(cls, parent:PolicyStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: PolicyStore, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class ObjectSetCollection(SfcDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IEnumerable[ObjectSet]'>, <type 'ICollection[ObjectSet]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ ObjectSetCollection(parent: PolicyStore) """
    pass

class ObjectValidationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ObjectValidationException()
    ObjectValidationException(message: str)
    ObjectValidationException(message: str, innerException: Exception)
    ObjectValidationException(objectType: str, objectName: str, innerException: Exception)
    ObjectValidationException(objectType: str, objectName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: ObjectValidationException) -> str """
        ...

    @property
    def ObjectName(self) -> str:
        """ Get: ObjectName(self: ObjectValidationException) -> str """
        ...

    @property
    def ObjectType(self) -> str:
        """ Get: ObjectType(self: ObjectValidationException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ObjectValidationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class OperatorNotApplicableException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    OperatorNotApplicableException()
    OperatorNotApplicableException(message: str)
    OperatorNotApplicableException(message: str, innerException: Exception)
    OperatorNotApplicableException(operatorName: str, typeName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: OperatorNotApplicableException) -> str """
        ...

    @property
    def Operator(self) -> str:
        """ Get: Operator(self: OperatorNotApplicableException) -> str """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: OperatorNotApplicableException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: OperatorNotApplicableException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class OperatorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperatorType, values: AND (1), BEQ (13), BNE (14), EQ (3), GE (8), GT (6), IN (9), LE (7), LIKE (10), LT (5), NE (4), NONE (0), NOT_IN (11), NOT_LIKE (12), OR (2) """
    AND: OperatorType = ...
    BEQ: OperatorType = ...
    BNE: OperatorType = ...
    EQ: OperatorType = ...
    GE: OperatorType = ...
    GT: OperatorType = ...
    IN: OperatorType = ...
    LE: OperatorType = ...
    LIKE: OperatorType = ...
    LT: OperatorType = ...
    NE: OperatorType = ...
    NONE: OperatorType = ...
    NOT_IN: OperatorType = ...
    NOT_LIKE: OperatorType = ...
    OR: OperatorType = ...
    value__ = ...


class Policy(IRenamable, ISfcCreatable, ISfcDroppable, ISfcRenamable, SfcInstance, ISfcValidate, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Policy()
    Policy(parent: PolicyStore, name: str)
    """
    @property
    def AutomatedPolicyEvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """
        Get: AutomatedPolicyEvaluationMode(self: Policy) -> AutomatedPolicyEvaluationMode
        Set: AutomatedPolicyEvaluationMode(self: Policy) = value
        """
        ...

    @property
    def CategoryId(self) -> int:
        """ Get: CategoryId(self: Policy) -> int """
        ...

    @property
    def Condition(self) -> str:
        """
        Get: Condition(self: Policy) -> str
        Set: Condition(self: Policy) = value
        """
        ...

    @property
    def CreateDate(self) -> DateTime:
        """ Get: CreateDate(self: Policy) -> DateTime """
        ...

    @property
    def CreatedBy(self) -> str:
        """ Get: CreatedBy(self: Policy) -> str """
        ...

    @property
    def DateModified(self) -> DateTime:
        """ Get: DateModified(self: Policy) -> DateTime """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Policy) -> str
        Set: Description(self: Policy) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Policy) -> bool
        Set: Enabled(self: Policy) = value
        """
        ...

    @property
    def EvaluationHistories(self) -> EvaluationHistoryCollection:
        """ Get: EvaluationHistories(self: Policy) -> EvaluationHistoryCollection """
        ...

    @property
    def HasScript(self) -> bool:
        """ Get: HasScript(self: Policy) -> bool """
        ...

    @property
    def HelpLink(self) -> str:
        """
        Get: HelpLink(self: Policy) -> str
        Set: HelpLink(self: Policy) = value
        """
        ...

    @property
    def HelpText(self) -> str:
        """
        Get: HelpText(self: Policy) -> str
        Set: HelpText(self: Policy) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Policy) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Policy) -> Key """
        ...

    @property
    def IsSystemObject(self) -> bool:
        """ Get: IsSystemObject(self: Policy) -> bool """
        ...

    @property
    def ModifiedBy(self) -> str:
        """ Get: ModifiedBy(self: Policy) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Policy) -> str """
        ...

    @property
    def ObjectSet(self) -> str:
        """
        Get: ObjectSet(self: Policy) -> str
        Set: ObjectSet(self: Policy) = value
        """
        ...

    @property
    def PolicyCategory(self) -> str:
        """
        Get: PolicyCategory(self: Policy) -> str
        Set: PolicyCategory(self: Policy) = value
        """
        ...

    @property
    def RootCondition(self) -> str:
        """
        Get: RootCondition(self: Policy) -> str
        Set: RootCondition(self: Policy) = value
        """
        ...

    @property
    def ScheduleUid(self) -> Guid:
        """
        Get: ScheduleUid(self: Policy) -> Guid
        Set: ScheduleUid(self: Policy) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: Policy) """
        ...

    def ConnectionProcessingFinishedEventArgs(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def ConnectionProcessingFinishedEventHandler(self, *args): #cannot find CLR method
        """ ConnectionProcessingFinishedEventHandler(object: object, method: IntPtr) """
        ...

    def ConnectionProcessingStartedEventArgs(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def ConnectionProcessingStartedEventHandler(self, *args): #cannot find CLR method
        """ ConnectionProcessingStartedEventHandler(object: object, method: IntPtr) """
        ...

    def Create(self): # -> 
        """ Create(self: Policy) """
        ...

    def Drop(self): # -> 
        """ Drop(self: Policy) """
        ...

    def Evaluate(self, evaluationMode:AdHocPolicyEvaluationMode, *__args:Array) -> bool:
        """
        Evaluate(self: Policy, evaluationMode: AdHocPolicyEvaluationMode, *targetObjects: Array[object]) -> bool
        Evaluate(self: Policy, evaluationMode: AdHocPolicyEvaluationMode, *targetConnections: Array[ISfcConnection]) -> bool
        Evaluate(self: Policy, evaluationMode: AdHocPolicyEvaluationMode, targetQueryExpression: SfcQueryExpression, *targetConnections: Array[ISfcConnection]) -> bool
        """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def PolicyEvaluationFinishedEventArgs(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def PolicyEvaluationFinishedEventHandler(self, *args): #cannot find CLR method
        """ PolicyEvaluationFinishedEventHandler(object: object, method: IntPtr) """
        ...

    def PolicyEvaluationStartedEventHandler(self, *args): #cannot find CLR method
        """ PolicyEvaluationStartedEventHandler(object: object, method: IntPtr) """
        ...

    def ProduceConfigureScript(self, target:object) -> str:
        """ ProduceConfigureScript(self: Policy, target: object) -> str """
        ...

    def ScriptAlterWithObjectSet(self) -> ISfcScript:
        """ ScriptAlterWithObjectSet(self: Policy) -> ISfcScript """
        ...

    def ScriptCreateWithDependencies(self) -> ISfcScript:
        """ ScriptCreateWithDependencies(self: Policy) -> ISfcScript """
        ...

    def ScriptCreateWithObjectSet(self) -> ISfcScript:
        """ ScriptCreateWithObjectSet(self: Policy) -> ISfcScript """
        ...

    def ScriptDropWithObjectSet(self) -> ISfcScript:
        """ ScriptDropWithObjectSet(self: Policy) -> ISfcScript """
        ...

    def TargetProcessedEventArgs(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def TargetProcessedEventHandler(self, *args): #cannot find CLR method
        """ TargetProcessedEventHandler(object: object, method: IntPtr) """
        ...

    def UsesFacet(self, facet:str) -> bool:
        """ UsesFacet(self: Policy, facet: str) -> bool """
        ...

    def __new__(cls, parent:PolicyStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: PolicyStore, name: str)
        """
        ...

    ConnectionProcessingFinished = ...
    ConnectionProcessingStarted = ...
    HelpLinkStringMaxLength: int = ...
    HelpTextStringMaxLength: int = ...
    PolicyEvaluationFinished = ...
    PolicyEvaluationStarted = ...
    propertyChanged = ...
    propertyMetadataChanged = ...
    TargetProcessed = ...


class PolicyCategory(IRenamable, ISfcCreatable, ISfcDroppable, ISfcRenamable, SfcInstance, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    PolicyCategory()
    PolicyCategory(parent: PolicyStore, name: str)
    """
    @property
    def DefaultCategory(self) -> str:
        """ Get: DefaultCategory() -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: PolicyCategory) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: PolicyCategory) -> Key """
        ...

    @property
    def MandateDatabaseSubscriptions(self) -> bool:
        """
        Get: MandateDatabaseSubscriptions(self: PolicyCategory) -> bool
        Set: MandateDatabaseSubscriptions(self: PolicyCategory) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PolicyCategory) -> str """
        ...


    def Alter(self): # -> 
        """ Alter(self: PolicyCategory) """
        ...

    def Create(self): # -> 
        """ Create(self: PolicyCategory) """
        ...

    def Drop(self): # -> 
        """ Drop(self: PolicyCategory) """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def __new__(cls, parent:PolicyStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: PolicyStore, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class PolicyCategoryCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'IEnumerable[PolicyCategory]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection[PolicyCategory]'>, <type 'ICollection'>, <type 'object'>
    """
    PolicyCategoryCollection(parent: PolicyStore)
    PolicyCategoryCollection(parent: PolicyStore, customComparer: IComparer[str])
    """
    pass

class PolicyCategoryInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """ Get: EvaluationMode(self: PolicyCategoryInformation) -> AutomatedPolicyEvaluationMode """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: PolicyCategoryInformation) -> int """
        ...

    @property
    def IsEmptyCategory(self) -> bool:
        """ Get: IsEmptyCategory(self: PolicyCategoryInformation) -> bool """
        ...

    @property
    def IsSubscribed(self) -> bool:
        """ Get: IsSubscribed(self: PolicyCategoryInformation) -> bool """
        ...

    @property
    def MandateDatabaseSubscriptions(self) -> bool:
        """ Get: MandateDatabaseSubscriptions(self: PolicyCategoryInformation) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PolicyCategoryInformation) -> str """
        ...

    @property
    def PolicyEnabled(self) -> bool:
        """ Get: PolicyEnabled(self: PolicyCategoryInformation) -> bool """
        ...

    @property
    def PolicyId(self) -> int:
        """ Get: PolicyId(self: PolicyCategoryInformation) -> int """
        ...

    @property
    def PolicyName(self) -> str:
        """ Get: PolicyName(self: PolicyCategoryInformation) -> str """
        ...



class PolicyCategorySubscription(ISfcDroppable, SfcInstance, ISfcCreatable, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    PolicyCategorySubscription()
    PolicyCategorySubscription(parent: PolicyStore)
    PolicyCategorySubscription(parent: PolicyStore, obj: SqlSmoObject)
    """
    @property
    def ID(self) -> int:
        """ Get: ID(self: PolicyCategorySubscription) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: PolicyCategorySubscription) -> Key """
        ...

    @property
    def PolicyCategory(self) -> str:
        """
        Get: PolicyCategory(self: PolicyCategorySubscription) -> str
        Set: PolicyCategory(self: PolicyCategorySubscription) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: PolicyCategorySubscription) -> str
        Set: Target(self: PolicyCategorySubscription) = value
        """
        ...

    @property
    def TargetType(self) -> str:
        """
        Get: TargetType(self: PolicyCategorySubscription) -> str
        Set: TargetType(self: PolicyCategorySubscription) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: PolicyCategorySubscription) """
        ...

    def Create(self): # -> 
        """ Create(self: PolicyCategorySubscription) """
        ...

    def Drop(self): # -> 
        """ Drop(self: PolicyCategorySubscription) """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(id: int)
        """
        ...

    def ValidateProperties(self, mode:str): # -> 
        """ ValidateProperties(self: PolicyCategorySubscription, mode: str) """
        ...

    def __new__(cls, parent:PolicyStore = ..., obj = ...) -> Self: # Not found arg types: {'obj': 'SqlSmoObject'}
        """
        __new__(cls: type)
        __new__(cls: type, parent: PolicyStore)
        __new__(cls: type, parent: PolicyStore, obj: SqlSmoObject)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class PolicyCategorySubscriptionCollection(SfcDictionaryCollection): # skipped bases: <type 'IEnumerable[PolicyCategorySubscription]'>, <type 'ICollection[PolicyCategorySubscription]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ PolicyCategorySubscriptionCollection(parent: PolicyStore) """
    pass

class PolicyCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'IEnumerable[Policy]'>, <type 'ICollection[Policy]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """
    PolicyCollection(parent: PolicyStore)
    PolicyCollection(parent: PolicyStore, customComparer: IComparer[str])
    """
    pass

class PolicyEffectiveState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PolicyEffectiveState, values: Enabled (1), InCategory (4), InFilter (2), None (0) """
    Enabled: PolicyEffectiveState = ...
    InCategory: PolicyEffectiveState = ...
    InFilter: PolicyEffectiveState = ...
    value__ = ...


class PolicyEvaluationException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PolicyEvaluationException()
    PolicyEvaluationException(message: str, innerException: Exception)
    PolicyEvaluationException(message: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PolicyEvaluationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class PolicyEvaluationResultsWriter(IDisposable): # skipped bases: <type 'object'>
    """ PolicyEvaluationResultsWriter(xmlWriter: XmlWriter) """
    @staticmethod
    def GetXmlWriterSettings(): # -> XmlWriterSettings
        """ GetXmlWriterSettings() -> XmlWriterSettings """
        ...

    def WriteEvaluationHistory(self, history:EvaluationHistory): # -> 
        """ WriteEvaluationHistory(self: PolicyEvaluationResultsWriter, history: EvaluationHistory) """
        ...


class PolicyExtender(SfcObjectExtender): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    PolicyExtender()
    PolicyExtender(policy: Policy)
    PolicyExtender(policyStore: PolicyStore, name: str)
    """
    @property
    def Categories(self) -> List:
        """ Get: Categories(self: PolicyExtender) -> List[PolicyCategory] """
        ...

    @property
    def Category(self) -> PolicyCategory:
        """
        Get: Category(self: PolicyExtender) -> PolicyCategory
        Set: Category(self: PolicyExtender) = value
        """
        ...

    @property
    def ConditionInstance(self) -> Condition:
        """
        Get: ConditionInstance(self: PolicyExtender) -> Condition
        Set: ConditionInstance(self: PolicyExtender) = value
        """
        ...

    @property
    def EnableRootRestriction(self) -> bool:
        """ Get: EnableRootRestriction(self: PolicyExtender) -> bool """
        ...

    @property
    def Filters(self) -> TargetSetCollection:
        """ Get: Filters(self: PolicyExtender) -> TargetSetCollection """
        ...

    @property
    def OfflineMode(self) -> bool:
        """ Get: OfflineMode(self: PolicyExtender) -> bool """
        ...

    @property
    def PolicyFilePath(self) -> str:
        """
        Get: PolicyFilePath(self: PolicyExtender) -> str
        Set: PolicyFilePath(self: PolicyExtender) = value
        """
        ...

    @property
    def RootName(self) -> str:
        """ Get: RootName(self: PolicyExtender) -> str """
        ...

    @property
    def SupportedPolicyEvaluationMode(self) -> AutomatedPolicyEvaluationMode:
        """ Get: SupportedPolicyEvaluationMode(self: PolicyExtender) -> AutomatedPolicyEvaluationMode """
        ...



class PolicyHealthState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PolicyHealthState, values: Critical (1), Healthy (2), NoPolicy (3), Unknown (0) """
    Critical: PolicyHealthState = ...
    Healthy: PolicyHealthState = ...
    NoPolicy: PolicyHealthState = ...
    Unknown: PolicyHealthState = ...
    value__ = ...


class PolicyStore(SfcInstance, ISfcDomain, ISfcValidate, ISfcSerializableUpgrade, ISfcAlterable): # skipped bases: <type 'ISfcDomainLite'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """
    PolicyStore()
    PolicyStore(connection: SfcConnection)
    """
    @property
    def Conditions(self) -> ConditionCollection:
        """ Get: Conditions(self: PolicyStore) -> ConditionCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: PolicyStore) -> bool
        Set: Enabled(self: PolicyStore) = value
        """
        ...

    @property
    def Facets(self) -> FacetInfoCollection:
        """ Get: Facets() -> FacetInfoCollection """
        ...

    @property
    def HistoryRetentionInDays(self) -> int:
        """
        Get: HistoryRetentionInDays(self: PolicyStore) -> int
        Set: HistoryRetentionInDays(self: PolicyStore) = value
        """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: PolicyStore) -> Key """
        ...

    @property
    def LogOnSuccess(self) -> bool:
        """
        Get: LogOnSuccess(self: PolicyStore) -> bool
        Set: LogOnSuccess(self: PolicyStore) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PolicyStore) -> str """
        ...

    @property
    def ObjectSets(self) -> ObjectSetCollection:
        """ Get: ObjectSets(self: PolicyStore) -> ObjectSetCollection """
        ...

    @property
    def Policies(self) -> PolicyCollection:
        """ Get: Policies(self: PolicyStore) -> PolicyCollection """
        ...

    @property
    def PolicyCategories(self) -> PolicyCategoryCollection:
        """ Get: PolicyCategories(self: PolicyStore) -> PolicyCategoryCollection """
        ...

    @property
    def PolicyCategorySubscriptions(self) -> PolicyCategorySubscriptionCollection:
        """ Get: PolicyCategorySubscriptions(self: PolicyStore) -> PolicyCategorySubscriptionCollection """
        ...

    @property
    def SqlStoreConnection(self) -> SqlStoreConnection:
        """
        Get: SqlStoreConnection(self: PolicyStore) -> SqlStoreConnection
        Set: SqlStoreConnection(self: PolicyStore) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: PolicyStore) """
        ...

    def CreatePolicyFromFacet(self, target:SfcQueryExpression, facetName:str, policyName:str, conditionName:str, writer = ...): # ->  # Not found arg types: {'writer': 'XmlWriter'}
        """ CreatePolicyFromFacet(self: PolicyStore, target: SfcQueryExpression, facetName: str, policyName: str, conditionName: str)CreatePolicyFromFacet(self: PolicyStore, target: SfcQueryExpression, facetName: str, policyName: str, conditionName: str, writer: XmlWriter)CreatePolicyFromFacet(self: PolicyStore, target: object, facetName: str, policyName: str, conditionName: str, writer: XmlWriter) """
        ...

    def DeserializePolicy(self, xmlReader, overwriteExistingPolicy:bool, overwriteExistingCondition:bool) -> Policy: # Not found arg types: {'xmlReader': 'XmlReader'}
        """ DeserializePolicy(self: PolicyStore, xmlReader: XmlReader, overwriteExistingPolicy: bool, overwriteExistingCondition: bool) -> Policy """
        ...

    def EnumApplicablePolicies(self, target:SfcQueryExpression) -> DataTable:
        """ EnumApplicablePolicies(self: PolicyStore, target: SfcQueryExpression) -> DataTable """
        ...

    def EnumApplicablePolicyCategories(self, target:SfcQueryExpression) -> ReadOnlyCollection:
        """ EnumApplicablePolicyCategories(self: PolicyStore, target: SfcQueryExpression) -> ReadOnlyCollection[PolicyCategoryInformation] """
        ...

    def EnumConditionsOnFacet(self, facet:str, enumerationMode = ...) -> StringCollection: # Not found arg types: {'enumerationMode': 'EnumerationMode'}
        """
        EnumConditionsOnFacet(self: PolicyStore, facet: str) -> StringCollection
        EnumConditionsOnFacet(self: PolicyStore, facet: str, enumerationMode: EnumerationMode) -> StringCollection
        """
        ...

    @staticmethod
    def EnumDomainFacets(args:Array) -> FacetInfoCollection:
        """ EnumDomainFacets(*args: Array[str]) -> FacetInfoCollection """
        ...

    def EnumerationMode(self, *args): #cannot find CLR method
        """ enum (flags) EnumerationMode, values: All (3), NonSystemOnly (1), SystemOnly (2) """
        ...

    def EnumPoliciesOnFacet(self, facet:str, enumerationMode = ...) -> StringCollection: # Not found arg types: {'enumerationMode': 'EnumerationMode'}
        """
        EnumPoliciesOnFacet(self: PolicyStore, facet: str) -> StringCollection
        EnumPoliciesOnFacet(self: PolicyStore, facet: str, enumerationMode: EnumerationMode) -> StringCollection
        """
        ...

    def EnumPolicyCategories(self) -> ReadOnlyCollection:
        """ EnumPolicyCategories(self: PolicyStore) -> ReadOnlyCollection[PolicyCategoryInformation] """
        ...

    def EnumRootConditions(self, rootType:Type) -> StringCollection:
        """ EnumRootConditions(self: PolicyStore, rootType: Type) -> StringCollection """
        ...

    @staticmethod
    def EnumRootFacets(rootType:Type) -> FacetInfoCollection:
        """ EnumRootFacets(rootType: Type) -> FacetInfoCollection """
        ...

    def EnumTargetSetConditions(self, type:Type, enumerationMode = ...) -> StringCollection: # Not found arg types: {'enumerationMode': 'EnumerationMode'}
        """
        EnumTargetSetConditions(self: PolicyStore, type: Type) -> StringCollection
        EnumTargetSetConditions(self: PolicyStore, type: Type, enumerationMode: EnumerationMode) -> StringCollection
        """
        ...

    def EraseSystemHealthPhantomRecords(self): # -> 
        """ EraseSystemHealthPhantomRecords(self: PolicyStore) """
        ...

    def GetAggregatedHealthState(self, target:SfcQueryExpression) -> PolicyHealthState:
        """ GetAggregatedHealthState(self: PolicyStore, target: SfcQueryExpression) -> PolicyHealthState """
        ...

    def ImportPolicy(self, xmlReader, importEnabledState:ImportPolicyEnabledState, overwriteExistingPolicy:bool, overwriteExistingCondition:bool) -> Policy: # Not found arg types: {'xmlReader': 'XmlReader'}
        """ ImportPolicy(self: PolicyStore, xmlReader: XmlReader, importEnabledState: ImportPolicyEnabledState, overwriteExistingPolicy: bool, overwriteExistingCondition: bool) -> Policy """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key() """
        ...

    def MarkSystemObject(self, obj:object, marker:bool): # -> 
        """ MarkSystemObject(self: PolicyStore, obj: object, marker: bool) """
        ...

    def PurgeHealthState(self, targetTreeRoot:SfcQueryExpression = ...): # -> 
        """ PurgeHealthState(self: PolicyStore)PurgeHealthState(self: PolicyStore, targetTreeRoot: SfcQueryExpression) """
        ...

    def RepairPolicyAutomation(self): # -> 
        """ RepairPolicyAutomation(self: PolicyStore) """
        ...

    def SubscribeToPolicyCategory(self, target:SfcQueryExpression, policyCategory:str) -> PolicyCategorySubscription:
        """ SubscribeToPolicyCategory(self: PolicyStore, target: SfcQueryExpression, policyCategory: str) -> PolicyCategorySubscription """
        ...

    def UnsubscribeFromPolicyCategory(self, target:SfcQueryExpression, policyCategory:str): # -> 
        """ UnsubscribeFromPolicyCategory(self: PolicyStore, target: SfcQueryExpression, policyCategory: str) """
        ...

    def __new__(cls, connection:SfcConnection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connection: SfcConnection)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class PolicyStoreUpgradeSession(UpgradeSession): # skipped bases: <type 'object'>
    """ PolicyStoreUpgradeSession() """
    pass

class PostConfigurationAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PostConfigurationAction, values: None (0), RestartService (1) """
    RestartService: PostConfigurationAction = ...
    value__ = ...


class PostConfigurationActionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PostConfigurationActionAttribute(postConfigurationAction: PostConfigurationAction) """
    @property
    def PostConfigurationAction(self) -> PostConfigurationAction:
        """ Get: PostConfigurationAction(self: PostConfigurationActionAttribute) -> PostConfigurationAction """
        ...


    def __new__(cls, postConfigurationAction:PostConfigurationAction) -> Self:
        """ __new__(cls: type, postConfigurationAction: PostConfigurationAction) """
        ...


class RestartPendingException: # skipped bases: <type 'object'>
    """
    RestartPendingException()
    RestartPendingException(message: str)
    RestartPendingException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: RestartPendingException, info: SerializationInfo, context: StreamingContext) """
        ...

    def Init(self, *args): #cannot find CLR method
        """ Init(self: DmfException) """
        ...

    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: DmfException, resource: str) -> DmfException """
        ...

    def __new__(cls, message:str = ..., innerException:Exception = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class StringPropertyTooLongException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    StringPropertyTooLongException()
    StringPropertyTooLongException(message: str)
    StringPropertyTooLongException(message: str, innerException: Exception)
    StringPropertyTooLongException(propertyName: str, maxLength: int, currentLength: int)
    """
    @property
    def CurrentLength(self) -> int:
        """ Get: CurrentLength(self: StringPropertyTooLongException) -> int """
        ...

    @property
    def MaxLength(self) -> int:
        """ Get: MaxLength(self: StringPropertyTooLongException) -> int """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: StringPropertyTooLongException) -> str """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: StringPropertyTooLongException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: StringPropertyTooLongException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class TargetEvaluation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Result(self) -> ExpressionNode:
        """ Get: Result(self: TargetEvaluation) -> ExpressionNode """
        ...

    @property
    def Target(self) -> object:
        """ Get: Target(self: TargetEvaluation) -> object """
        ...



class TargetSet(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    TargetSet()
    TargetSet(parent: ObjectSet, targetTypeSkeleton: str)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: TargetSet) -> bool
        Set: Enabled(self: TargetSet) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetSet) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TargetSet) -> Key """
        ...

    @property
    def Levels(self) -> TargetSetLevelCollection:
        """ Get: Levels(self: TargetSet) -> TargetSetLevelCollection """
        ...

    @property
    def RootLevel(self) -> str:
        """ Get: RootLevel(self: TargetSet) -> str """
        ...

    @property
    def TargetType(self) -> str:
        """ Get: TargetType(self: TargetSet) -> str """
        ...

    @property
    def TargetTypeSkeleton(self) -> str:
        """ Get: TargetTypeSkeleton(self: TargetSet) -> str """
        ...


    def GetFilter(self) -> str:
        """ GetFilter(self: TargetSet) -> str """
        ...

    def GetLevel(self, skeleton:str) -> TargetSetLevel:
        """ GetLevel(self: TargetSet, skeleton: str) -> TargetSetLevel """
        ...

    def GetLevelsSorted(self) -> IList:
        """ GetLevelsSorted(self: TargetSet) -> IList[TargetSetLevel] """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(targetTypeSkeleton: str)
        """
        ...

    def SetLevelCondition(self, level:TargetSetLevel, condition:str) -> TargetSetLevel:
        """ SetLevelCondition(self: TargetSet, level: TargetSetLevel, condition: str) -> TargetSetLevel """
        ...

    def __new__(cls, parent:ObjectSet = ..., targetTypeSkeleton:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: ObjectSet, targetTypeSkeleton: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class TargetSetCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection[TargetSet]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'IEnumerable[TargetSet]'>, <type 'ICollection'>, <type 'IComparer[Key]'>, <type 'object'>
    """
    TargetSetCollection(parent: ObjectSet)
    TargetSetCollection(parent: ObjectSet, customComparer: IComparer[str])
    """
    pass

class TargetSetCountMismatchException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TargetSetCountMismatchException()
    TargetSetCountMismatchException(message: str)
    TargetSetCountMismatchException(message: str, innerException: Exception)
    TargetSetCountMismatchException(objectSetName: str, facetName: str)
    """
    @property
    def FacetName(self) -> str:
        """ Get: FacetName(self: TargetSetCountMismatchException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: TargetSetCountMismatchException) -> str """
        ...

    @property
    def ObjectSetName(self) -> str:
        """ Get: ObjectSetName(self: TargetSetCountMismatchException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: TargetSetCountMismatchException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class TargetSetLevel(IComparable, SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ TargetSetLevel() """
    @property
    def Condition(self) -> str:
        """
        Get: Condition(self: TargetSetLevel) -> str
        Set: Condition(self: TargetSetLevel) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetSetLevel) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TargetSetLevel) -> Key """
        ...

    @property
    def LevelName(self) -> str:
        """ Get: LevelName(self: TargetSetLevel) -> str """
        ...

    @property
    def TargetType(self) -> Type:
        """ Get: TargetType(self: TargetSetLevel) -> Type """
        ...

    @property
    def TargetTypeSkeleton(self) -> str:
        """ Get: TargetTypeSkeleton(self: TargetSetLevel) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: TargetSetLevel, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TargetSetLevel) -> int """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    @staticmethod
    def GetTypeFilterProperties(skeleton:str) -> Array:
        """ GetTypeFilterProperties(skeleton: str) -> Array[PropertyInfo] """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(targetTypeSkeleton: str)
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class TargetSetLevelCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[TargetSetLevel]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IEnumerable[TargetSetLevel]'>, <type 'IListSource'>, <type 'IComparer[Key]'>, <type 'ICollection'>, <type 'object'>
    """
    TargetSetLevelCollection(parent: TargetSet)
    TargetSetLevelCollection(parent: TargetSet, customComparer: IComparer[str])
    """
    pass

class TypeClass(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TypeClass, values: Array (6), BitmappedEnum (9), Bool (3), DateTime (4), Guid (5), Numeric (1), String (2), Unsupported (0), VarArgs (8), Variant (7) """
    Array: TypeClass = ...
    BitmappedEnum: TypeClass = ...
    Bool: TypeClass = ...
    DateTime: TypeClass = ...
    Guid: TypeClass = ...
    Numeric: TypeClass = ...
    String: TypeClass = ...
    Unsupported: TypeClass = ...
    value__ = ...
    VarArgs: TypeClass = ...
    Variant: TypeClass = ...


class TypeConversionException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TypeConversionException()
    TypeConversionException(message: str)
    TypeConversionException(message: str, innerException: Exception)
    TypeConversionException(inputString: str, typeName: str, innerException: Exception)
    """
    @property
    def InputString(self) -> str:
        """ Get: InputString(self: TypeConversionException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: TypeConversionException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: TypeConversionException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: TypeConversionException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class UnsupportedObjectTypeException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnsupportedObjectTypeException()
    UnsupportedObjectTypeException(message: str)
    UnsupportedObjectTypeException(message: str, innerException: Exception)
    UnsupportedObjectTypeException(typeName: str, host: str)
    """
    @property
    def Host(self) -> str:
        """ Get: Host(self: UnsupportedObjectTypeException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: UnsupportedObjectTypeException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: UnsupportedObjectTypeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: UnsupportedObjectTypeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class UnsupportedTargetSetForFacetException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnsupportedTargetSetForFacetException()
    UnsupportedTargetSetForFacetException(message: str)
    UnsupportedTargetSetForFacetException(message: str, innerException: Exception)
    UnsupportedTargetSetForFacetException(targetSetSkeleton: str, objectSetName: str, facetName: str)
    """
    @property
    def FacetName(self) -> str:
        """ Get: FacetName(self: UnsupportedTargetSetForFacetException) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: UnsupportedTargetSetForFacetException) -> str """
        ...

    @property
    def ObjectSetName(self) -> str:
        """ Get: ObjectSetName(self: UnsupportedTargetSetForFacetException) -> str """
        ...

    @property
    def TargetSetSkeleton(self) -> str:
        """ Get: TargetSetSkeleton(self: UnsupportedTargetSetForFacetException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: UnsupportedTargetSetForFacetException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class UnsupportedTypeException(DmfException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnsupportedTypeException()
    UnsupportedTypeException(message: str)
    UnsupportedTypeException(message: str, innerException: Exception)
    UnsupportedTypeException(node: str, typeName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: UnsupportedTypeException) -> str """
        ...

    @property
    def NodeType(self) -> str:
        """ Get: NodeType(self: UnsupportedTypeException) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: UnsupportedTypeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: UnsupportedTypeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class Utils: # skipped bases: <type 'object'>, <type 'object'>
    """ Utils() """
    @staticmethod
    def GetDescriptionForAdHocEvaluationMode(mode:AdHocPolicyEvaluationMode) -> str:
        """ GetDescriptionForAdHocEvaluationMode(mode: AdHocPolicyEvaluationMode) -> str """
        ...

    @staticmethod
    def GetDescriptionForEvaluationMode(mode:AutomatedPolicyEvaluationMode) -> str:
        """ GetDescriptionForEvaluationMode(mode: AutomatedPolicyEvaluationMode) -> str """
        ...

    @staticmethod
    def GetEvaluationModeByDescription(execModeDescription:str) -> AutomatedPolicyEvaluationMode:
        """ GetEvaluationModeByDescription(execModeDescription: str) -> AutomatedPolicyEvaluationMode """
        ...

    @staticmethod
    def IsValidHelpLink(link:str) -> bool:
        """ IsValidHelpLink(link: str) -> bool """
        ...


# variables with complex values

