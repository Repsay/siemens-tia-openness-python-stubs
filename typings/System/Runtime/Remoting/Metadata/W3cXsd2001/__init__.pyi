# encoding: utf-8
# module System.Runtime.Remoting.Metadata.W3cXsd2001 calls itself W3cXsd2001
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, Decimal, TimeSpan


# no functions
# classes

class ISoapXsd: # skipped bases: <type 'object'>
    """ no doc """
    def GetXsdType(self) -> str:
        """ GetXsdType(self: ISoapXsd) -> str """
        ...


class SoapAnyUri(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapAnyUri()
    SoapAnyUri(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapAnyUri) -> str
        Set: Value(self: SoapAnyUri) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapAnyUri:
        """ Parse(value: str) -> SoapAnyUri """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapAnyUri) -> str """
        ...



class SoapBase64Binary(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapBase64Binary()
    SoapBase64Binary(value: Array[Byte])
    """
    @property
    def Value(self) -> Array:
        """
        Get: Value(self: SoapBase64Binary) -> Array[Byte]
        Set: Value(self: SoapBase64Binary) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapBase64Binary:
        """ Parse(value: str) -> SoapBase64Binary """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapBase64Binary) -> str """
        ...



class SoapDate(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapDate()
    SoapDate(value: DateTime)
    SoapDate(value: DateTime, sign: int)
    """
    @property
    def Sign(self) -> int:
        """
        Get: Sign(self: SoapDate) -> int
        Set: Sign(self: SoapDate) = value
        """
        ...

    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapDate) -> DateTime
        Set: Value(self: SoapDate) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapDate:
        """ Parse(value: str) -> SoapDate """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapDate) -> str """
        ...



class SoapDateTime: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapDateTime() """
    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> DateTime:
        """ Parse(value: str) -> DateTime """
        ...

    @staticmethod
    def ToString(value:DateTime = ...) -> str:
        """ ToString(value: DateTime) -> str """
        ...



class SoapDay(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapDay()
    SoapDay(value: DateTime)
    """
    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapDay) -> DateTime
        Set: Value(self: SoapDay) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapDay:
        """ Parse(value: str) -> SoapDay """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapDay) -> str """
        ...



class SoapDuration: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapDuration() """
    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> TimeSpan:
        """ Parse(value: str) -> TimeSpan """
        ...

    @staticmethod
    def ToString(timeSpan:TimeSpan = ...) -> str:
        """ ToString(timeSpan: TimeSpan) -> str """
        ...



class SoapEntities(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapEntities()
    SoapEntities(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapEntities) -> str
        Set: Value(self: SoapEntities) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapEntities:
        """ Parse(value: str) -> SoapEntities """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapEntities) -> str """
        ...



class SoapEntity(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapEntity()
    SoapEntity(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapEntity) -> str
        Set: Value(self: SoapEntity) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapEntity:
        """ Parse(value: str) -> SoapEntity """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapEntity) -> str """
        ...



class SoapHexBinary(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapHexBinary()
    SoapHexBinary(value: Array[Byte])
    """
    @property
    def Value(self) -> Array:
        """
        Get: Value(self: SoapHexBinary) -> Array[Byte]
        Set: Value(self: SoapHexBinary) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapHexBinary:
        """ Parse(value: str) -> SoapHexBinary """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapHexBinary) -> str """
        ...



class SoapId(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapId()
    SoapId(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapId) -> str
        Set: Value(self: SoapId) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapId:
        """ Parse(value: str) -> SoapId """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapId) -> str """
        ...



class SoapIdref(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapIdref()
    SoapIdref(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapIdref) -> str
        Set: Value(self: SoapIdref) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapIdref:
        """ Parse(value: str) -> SoapIdref """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapIdref) -> str """
        ...



class SoapIdrefs(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapIdrefs()
    SoapIdrefs(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapIdrefs) -> str
        Set: Value(self: SoapIdrefs) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapIdrefs:
        """ Parse(value: str) -> SoapIdrefs """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapIdrefs) -> str """
        ...



class SoapInteger(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapInteger()
    SoapInteger(value: Decimal)
    """
    @property
    def Value(self) -> Decimal:
        """
        Get: Value(self: SoapInteger) -> Decimal
        Set: Value(self: SoapInteger) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapInteger:
        """ Parse(value: str) -> SoapInteger """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapInteger) -> str """
        ...



class SoapLanguage(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapLanguage()
    SoapLanguage(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapLanguage) -> str
        Set: Value(self: SoapLanguage) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapLanguage:
        """ Parse(value: str) -> SoapLanguage """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapLanguage) -> str """
        ...



class SoapMonth(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapMonth()
    SoapMonth(value: DateTime)
    """
    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapMonth) -> DateTime
        Set: Value(self: SoapMonth) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapMonth:
        """ Parse(value: str) -> SoapMonth """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapMonth) -> str """
        ...



class SoapMonthDay(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapMonthDay()
    SoapMonthDay(value: DateTime)
    """
    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapMonthDay) -> DateTime
        Set: Value(self: SoapMonthDay) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapMonthDay:
        """ Parse(value: str) -> SoapMonthDay """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapMonthDay) -> str """
        ...



class SoapName(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapName()
    SoapName(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapName) -> str
        Set: Value(self: SoapName) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapName:
        """ Parse(value: str) -> SoapName """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapName) -> str """
        ...



class SoapNcName(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNcName()
    SoapNcName(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapNcName) -> str
        Set: Value(self: SoapNcName) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNcName:
        """ Parse(value: str) -> SoapNcName """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNcName) -> str """
        ...



class SoapNegativeInteger(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNegativeInteger()
    SoapNegativeInteger(value: Decimal)
    """
    @property
    def Value(self) -> Decimal:
        """
        Get: Value(self: SoapNegativeInteger) -> Decimal
        Set: Value(self: SoapNegativeInteger) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNegativeInteger:
        """ Parse(value: str) -> SoapNegativeInteger """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNegativeInteger) -> str """
        ...



class SoapNmtoken(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNmtoken()
    SoapNmtoken(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapNmtoken) -> str
        Set: Value(self: SoapNmtoken) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNmtoken:
        """ Parse(value: str) -> SoapNmtoken """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNmtoken) -> str """
        ...



class SoapNmtokens(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNmtokens()
    SoapNmtokens(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapNmtokens) -> str
        Set: Value(self: SoapNmtokens) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNmtokens:
        """ Parse(value: str) -> SoapNmtokens """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNmtokens) -> str """
        ...



class SoapNonNegativeInteger(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNonNegativeInteger()
    SoapNonNegativeInteger(value: Decimal)
    """
    @property
    def Value(self) -> Decimal:
        """
        Get: Value(self: SoapNonNegativeInteger) -> Decimal
        Set: Value(self: SoapNonNegativeInteger) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNonNegativeInteger:
        """ Parse(value: str) -> SoapNonNegativeInteger """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNonNegativeInteger) -> str """
        ...



class SoapNonPositiveInteger(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNonPositiveInteger()
    SoapNonPositiveInteger(value: Decimal)
    """
    @property
    def Value(self) -> Decimal:
        """
        Get: Value(self: SoapNonPositiveInteger) -> Decimal
        Set: Value(self: SoapNonPositiveInteger) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNonPositiveInteger:
        """ Parse(value: str) -> SoapNonPositiveInteger """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNonPositiveInteger) -> str """
        ...



class SoapNormalizedString(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNormalizedString()
    SoapNormalizedString(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapNormalizedString) -> str
        Set: Value(self: SoapNormalizedString) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNormalizedString:
        """ Parse(value: str) -> SoapNormalizedString """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNormalizedString) -> str """
        ...



class SoapNotation(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapNotation()
    SoapNotation(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapNotation) -> str
        Set: Value(self: SoapNotation) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapNotation:
        """ Parse(value: str) -> SoapNotation """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapNotation) -> str """
        ...



class SoapPositiveInteger(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapPositiveInteger()
    SoapPositiveInteger(value: Decimal)
    """
    @property
    def Value(self) -> Decimal:
        """
        Get: Value(self: SoapPositiveInteger) -> Decimal
        Set: Value(self: SoapPositiveInteger) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapPositiveInteger:
        """ Parse(value: str) -> SoapPositiveInteger """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapPositiveInteger) -> str """
        ...



class SoapQName(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapQName()
    SoapQName(value: str)
    SoapQName(key: str, name: str)
    SoapQName(key: str, name: str, namespaceValue: str)
    """
    @property
    def Key(self) -> str:
        """
        Get: Key(self: SoapQName) -> str
        Set: Key(self: SoapQName) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SoapQName) -> str
        Set: Name(self: SoapQName) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapQName) -> str
        Set: Namespace(self: SoapQName) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapQName:
        """ Parse(value: str) -> SoapQName """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapQName) -> str """
        ...



class SoapTime(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapTime()
    SoapTime(value: DateTime)
    """
    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapTime) -> DateTime
        Set: Value(self: SoapTime) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapTime:
        """ Parse(value: str) -> SoapTime """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapTime) -> str """
        ...



class SoapToken(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapToken()
    SoapToken(value: str)
    """
    @property
    def Value(self) -> str:
        """
        Get: Value(self: SoapToken) -> str
        Set: Value(self: SoapToken) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapToken:
        """ Parse(value: str) -> SoapToken """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapToken) -> str """
        ...



class SoapYear(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapYear()
    SoapYear(value: DateTime)
    SoapYear(value: DateTime, sign: int)
    """
    @property
    def Sign(self) -> int:
        """
        Get: Sign(self: SoapYear) -> int
        Set: Sign(self: SoapYear) = value
        """
        ...

    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapYear) -> DateTime
        Set: Value(self: SoapYear) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapYear:
        """ Parse(value: str) -> SoapYear """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapYear) -> str """
        ...



class SoapYearMonth(ISoapXsd): # skipped bases: <type 'object'>
    """
    SoapYearMonth()
    SoapYearMonth(value: DateTime)
    SoapYearMonth(value: DateTime, sign: int)
    """
    @property
    def Sign(self) -> int:
        """
        Get: Sign(self: SoapYearMonth) -> int
        Set: Sign(self: SoapYearMonth) = value
        """
        ...

    @property
    def Value(self) -> DateTime:
        """
        Get: Value(self: SoapYearMonth) -> DateTime
        Set: Value(self: SoapYearMonth) = value
        """
        ...

    @property
    def XsdType(self) -> str:
        """ Get: XsdType() -> str """
        ...


    @staticmethod
    def Parse(value:str) -> SoapYearMonth:
        """ Parse(value: str) -> SoapYearMonth """
        ...

    def ToString(self) -> str:
        """ ToString(self: SoapYearMonth) -> str """
        ...



