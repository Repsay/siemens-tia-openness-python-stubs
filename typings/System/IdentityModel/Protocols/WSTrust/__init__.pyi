# encoding: utf-8
# module System.IdentityModel.Protocols.WSTrust calls itself WSTrust
# from System.IdentityModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, Nullable, Uri

from System.Collections import IList

from System.Collections.Generic import List

from System.IdentityModel import OpenObject, RequestException

from System.IdentityModel.Selectors import SecurityTokenResolver

from System.IdentityModel.Tokens import (EncryptingCredentials, 
    SecurityKeyIdentifier, SecurityKeyIdentifierClause, SecurityToken, 
    SecurityTokenElement, SecurityTokenHandlerCollection, 
    SecurityTokenHandlerCollectionManager)

from System.Xml import XmlElement, XmlReader, XmlWriter

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class AdditionalContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    AdditionalContext()
    AdditionalContext(items: IEnumerable[ContextItem])
    """
    @property
    def Items(self) -> IList:
        """ Get: Items(self: AdditionalContext) -> IList[ContextItem] """
        ...



class BinaryExchange: # skipped bases: <type 'object'>, <type 'object'>
    """
    BinaryExchange(binaryData: Array[Byte], valueType: Uri)
    BinaryExchange(binaryData: Array[Byte], valueType: Uri, encodingType: Uri)
    """
    @property
    def BinaryData(self) -> Array:
        """ Get: BinaryData(self: BinaryExchange) -> Array[Byte] """
        ...

    @property
    def EncodingType(self) -> Uri:
        """ Get: EncodingType(self: BinaryExchange) -> Uri """
        ...

    @property
    def ValueType(self) -> Uri:
        """ Get: ValueType(self: BinaryExchange) -> Uri """
        ...



class ContextItem: # skipped bases: <type 'object'>, <type 'object'>
    """
    ContextItem(name: Uri)
    ContextItem(name: Uri, value: str)
    ContextItem(name: Uri, value: str, scope: Uri)
    """
    @property
    def Name(self) -> Uri:
        """
        Get: Name(self: ContextItem) -> Uri
        Set: Name(self: ContextItem) = value
        """
        ...

    @property
    def Scope(self) -> Uri:
        """
        Get: Scope(self: ContextItem) -> Uri
        Set: Scope(self: ContextItem) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: ContextItem) -> str
        Set: Value(self: ContextItem) = value
        """
        ...



class EndpointReference: # skipped bases: <type 'object'>, <type 'object'>
    """ EndpointReference(uri: str) """
    @property
    def Details(self) -> Collection:
        """ Get: Details(self: EndpointReference) -> Collection[XmlElement] """
        ...

    @property
    def Uri(self) -> Uri:
        """ Get: Uri(self: EndpointReference) -> Uri """
        ...


    @staticmethod
    def ReadFrom(reader:XmlReader) -> EndpointReference:
        """
        ReadFrom(reader: XmlReader) -> EndpointReference
        ReadFrom(reader: XmlDictionaryReader) -> EndpointReference
        """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: EndpointReference, writer: XmlWriter) """
        ...


class ProtectedKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    ProtectedKey(secret: Array[Byte])
    ProtectedKey(secret: Array[Byte], wrappingCredentials: EncryptingCredentials)
    """
    @property
    def WrappingCredentials(self) -> EncryptingCredentials:
        """ Get: WrappingCredentials(self: ProtectedKey) -> EncryptingCredentials """
        ...


    def GetKeyBytes(self) -> Array:
        """ GetKeyBytes(self: ProtectedKey) -> Array[Byte] """
        ...


class Entropy(ProtectedKey): # skipped bases: <type 'object'>
    """
    Entropy(entropySizeInBits: int)
    Entropy(secret: Array[Byte])
    Entropy(secret: Array[Byte], wrappingCredentials: EncryptingCredentials)
    Entropy(protectedKey: ProtectedKey)
    """
    pass

class InvalidRequestException(RequestException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidRequestException()
    InvalidRequestException(message: str)
    InvalidRequestException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class KeyTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Asymmetric: str = ...
    Bearer: str = ...
    Symmetric: str = ...
    __all__: list = ...


class Lifetime: # skipped bases: <type 'object'>, <type 'object'>
    """
    Lifetime(created: DateTime, expires: DateTime)
    Lifetime(created: Nullable[DateTime], expires: Nullable[DateTime])
    """
    @property
    def Created(self) -> Nullable:
        """
        Get: Created(self: Lifetime) -> Nullable[DateTime]
        Set: Created(self: Lifetime) = value
        """
        ...

    @property
    def Expires(self) -> Nullable:
        """
        Get: Expires(self: Lifetime) -> Nullable[DateTime]
        Set: Expires(self: Lifetime) = value
        """
        ...



class Participants: # skipped bases: <type 'object'>, <type 'object'>
    """ Participants() """
    @property
    def Participant(self) -> List:
        """ Get: Participant(self: Participants) -> List[EndpointReference] """
        ...

    @property
    def Primary(self) -> EndpointReference:
        """
        Get: Primary(self: Participants) -> EndpointReference
        Set: Primary(self: Participants) = value
        """
        ...



class Renewing: # skipped bases: <type 'object'>, <type 'object'>
    """
    Renewing()
    Renewing(allowRenewal: bool, okForRenewalAfterExpiration: bool)
    """
    @property
    def AllowRenewal(self) -> bool:
        """
        Get: AllowRenewal(self: Renewing) -> bool
        Set: AllowRenewal(self: Renewing) = value
        """
        ...

    @property
    def OkForRenewalAfterExpiration(self) -> bool:
        """
        Get: OkForRenewalAfterExpiration(self: Renewing) -> bool
        Set: OkForRenewalAfterExpiration(self: Renewing) = value
        """
        ...



class RequestClaim: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestClaim(claimType: str)
    RequestClaim(claimType: str, isOptional: bool)
    RequestClaim(claimType: str, isOptional: bool, value: str)
    """
    @property
    def ClaimType(self) -> str:
        """ Get: ClaimType(self: RequestClaim) -> str """
        ...

    @property
    def IsOptional(self) -> bool:
        """
        Get: IsOptional(self: RequestClaim) -> bool
        Set: IsOptional(self: RequestClaim) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: RequestClaim) -> str
        Set: Value(self: RequestClaim) = value
        """
        ...



class RequestClaimCollection(Collection): # skipped bases: <type 'IReadOnlyCollection[RequestClaim]'>, <type 'IEnumerable'>, <type 'IList[RequestClaim]'>, <type 'IEnumerable[RequestClaim]'>, <type 'IList'>, <type 'IReadOnlyList[RequestClaim]'>, <type 'ICollection[RequestClaim]'>, <type 'ICollection'>, <type 'object'>
    """ RequestClaimCollection() """
    @property
    def Dialect(self) -> str:
        """
        Get: Dialect(self: RequestClaimCollection) -> str
        Set: Dialect(self: RequestClaimCollection) = value
        """
        ...



class RequestedProofToken: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestedProofToken(computedKeyAlgorithm: str)
    RequestedProofToken(secret: Array[Byte])
    RequestedProofToken(secret: Array[Byte], wrappingCredentials: EncryptingCredentials)
    RequestedProofToken(protectedKey: ProtectedKey)
    """
    @property
    def ComputedKeyAlgorithm(self) -> str:
        """ Get: ComputedKeyAlgorithm(self: RequestedProofToken) -> str """
        ...

    @property
    def ProtectedKey(self) -> ProtectedKey:
        """ Get: ProtectedKey(self: RequestedProofToken) -> ProtectedKey """
        ...



class RequestedSecurityToken: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestedSecurityToken(token: SecurityToken)
    RequestedSecurityToken(tokenAsXml: XmlElement)
    """
    @property
    def SecurityToken(self) -> SecurityToken:
        """ Get: SecurityToken(self: RequestedSecurityToken) -> SecurityToken """
        ...

    @property
    def SecurityTokenXml(self) -> XmlElement:
        """ Get: SecurityTokenXml(self: RequestedSecurityToken) -> XmlElement """
        ...



class WSTrustMessage(OpenObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowPostdating(self) -> bool:
        """
        Get: AllowPostdating(self: WSTrustMessage) -> bool
        Set: AllowPostdating(self: WSTrustMessage) = value
        """
        ...

    @property
    def AppliesTo(self) -> EndpointReference:
        """
        Get: AppliesTo(self: WSTrustMessage) -> EndpointReference
        Set: AppliesTo(self: WSTrustMessage) = value
        """
        ...

    @property
    def AuthenticationType(self) -> str:
        """
        Get: AuthenticationType(self: WSTrustMessage) -> str
        Set: AuthenticationType(self: WSTrustMessage) = value
        """
        ...

    @property
    def BinaryExchange(self) -> BinaryExchange:
        """
        Get: BinaryExchange(self: WSTrustMessage) -> BinaryExchange
        Set: BinaryExchange(self: WSTrustMessage) = value
        """
        ...

    @property
    def CanonicalizationAlgorithm(self) -> str:
        """
        Get: CanonicalizationAlgorithm(self: WSTrustMessage) -> str
        Set: CanonicalizationAlgorithm(self: WSTrustMessage) = value
        """
        ...

    @property
    def Context(self) -> str:
        """
        Get: Context(self: WSTrustMessage) -> str
        Set: Context(self: WSTrustMessage) = value
        """
        ...

    @property
    def EncryptionAlgorithm(self) -> str:
        """
        Get: EncryptionAlgorithm(self: WSTrustMessage) -> str
        Set: EncryptionAlgorithm(self: WSTrustMessage) = value
        """
        ...

    @property
    def EncryptWith(self) -> str:
        """
        Get: EncryptWith(self: WSTrustMessage) -> str
        Set: EncryptWith(self: WSTrustMessage) = value
        """
        ...

    @property
    def Entropy(self) -> Entropy:
        """
        Get: Entropy(self: WSTrustMessage) -> Entropy
        Set: Entropy(self: WSTrustMessage) = value
        """
        ...

    @property
    def KeySizeInBits(self) -> Nullable:
        """
        Get: KeySizeInBits(self: WSTrustMessage) -> Nullable[int]
        Set: KeySizeInBits(self: WSTrustMessage) = value
        """
        ...

    @property
    def KeyType(self) -> str:
        """
        Get: KeyType(self: WSTrustMessage) -> str
        Set: KeyType(self: WSTrustMessage) = value
        """
        ...

    @property
    def KeyWrapAlgorithm(self) -> str:
        """
        Get: KeyWrapAlgorithm(self: WSTrustMessage) -> str
        Set: KeyWrapAlgorithm(self: WSTrustMessage) = value
        """
        ...

    @property
    def Lifetime(self) -> Lifetime:
        """
        Get: Lifetime(self: WSTrustMessage) -> Lifetime
        Set: Lifetime(self: WSTrustMessage) = value
        """
        ...

    @property
    def ReplyTo(self) -> str:
        """
        Get: ReplyTo(self: WSTrustMessage) -> str
        Set: ReplyTo(self: WSTrustMessage) = value
        """
        ...

    @property
    def RequestType(self) -> str:
        """
        Get: RequestType(self: WSTrustMessage) -> str
        Set: RequestType(self: WSTrustMessage) = value
        """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """
        Get: SignatureAlgorithm(self: WSTrustMessage) -> str
        Set: SignatureAlgorithm(self: WSTrustMessage) = value
        """
        ...

    @property
    def SignWith(self) -> str:
        """
        Get: SignWith(self: WSTrustMessage) -> str
        Set: SignWith(self: WSTrustMessage) = value
        """
        ...

    @property
    def TokenType(self) -> str:
        """
        Get: TokenType(self: WSTrustMessage) -> str
        Set: TokenType(self: WSTrustMessage) = value
        """
        ...

    @property
    def UseKey(self) -> UseKey:
        """
        Get: UseKey(self: WSTrustMessage) -> UseKey
        Set: UseKey(self: WSTrustMessage) = value
        """
        ...



class RequestSecurityToken(WSTrustMessage): # skipped bases: <type 'object'>
    """
    RequestSecurityToken()
    RequestSecurityToken(requestType: str)
    RequestSecurityToken(requestType: str, keyType: str)
    """
    @property
    def ActAs(self) -> SecurityTokenElement:
        """
        Get: ActAs(self: RequestSecurityToken) -> SecurityTokenElement
        Set: ActAs(self: RequestSecurityToken) = value
        """
        ...

    @property
    def AdditionalContext(self) -> AdditionalContext:
        """
        Get: AdditionalContext(self: RequestSecurityToken) -> AdditionalContext
        Set: AdditionalContext(self: RequestSecurityToken) = value
        """
        ...

    @property
    def CancelTarget(self) -> SecurityTokenElement:
        """
        Get: CancelTarget(self: RequestSecurityToken) -> SecurityTokenElement
        Set: CancelTarget(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Claims(self) -> RequestClaimCollection:
        """ Get: Claims(self: RequestSecurityToken) -> RequestClaimCollection """
        ...

    @property
    def ComputedKeyAlgorithm(self) -> str:
        """
        Get: ComputedKeyAlgorithm(self: RequestSecurityToken) -> str
        Set: ComputedKeyAlgorithm(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Delegatable(self) -> Nullable:
        """
        Get: Delegatable(self: RequestSecurityToken) -> Nullable[bool]
        Set: Delegatable(self: RequestSecurityToken) = value
        """
        ...

    @property
    def DelegateTo(self) -> SecurityTokenElement:
        """
        Get: DelegateTo(self: RequestSecurityToken) -> SecurityTokenElement
        Set: DelegateTo(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Encryption(self) -> SecurityTokenElement:
        """
        Get: Encryption(self: RequestSecurityToken) -> SecurityTokenElement
        Set: Encryption(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Forwardable(self) -> Nullable:
        """
        Get: Forwardable(self: RequestSecurityToken) -> Nullable[bool]
        Set: Forwardable(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Issuer(self) -> EndpointReference:
        """
        Get: Issuer(self: RequestSecurityToken) -> EndpointReference
        Set: Issuer(self: RequestSecurityToken) = value
        """
        ...

    @property
    def OnBehalfOf(self) -> SecurityTokenElement:
        """
        Get: OnBehalfOf(self: RequestSecurityToken) -> SecurityTokenElement
        Set: OnBehalfOf(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Participants(self) -> Participants:
        """
        Get: Participants(self: RequestSecurityToken) -> Participants
        Set: Participants(self: RequestSecurityToken) = value
        """
        ...

    @property
    def ProofEncryption(self) -> SecurityTokenElement:
        """
        Get: ProofEncryption(self: RequestSecurityToken) -> SecurityTokenElement
        Set: ProofEncryption(self: RequestSecurityToken) = value
        """
        ...

    @property
    def Renewing(self) -> Renewing:
        """
        Get: Renewing(self: RequestSecurityToken) -> Renewing
        Set: Renewing(self: RequestSecurityToken) = value
        """
        ...

    @property
    def RenewTarget(self) -> SecurityTokenElement:
        """
        Get: RenewTarget(self: RequestSecurityToken) -> SecurityTokenElement
        Set: RenewTarget(self: RequestSecurityToken) = value
        """
        ...

    @property
    def SecondaryParameters(self) -> RequestSecurityToken:
        """
        Get: SecondaryParameters(self: RequestSecurityToken) -> RequestSecurityToken
        Set: SecondaryParameters(self: RequestSecurityToken) = value
        """
        ...

    @property
    def ValidateTarget(self) -> SecurityTokenElement:
        """
        Get: ValidateTarget(self: RequestSecurityToken) -> SecurityTokenElement
        Set: ValidateTarget(self: RequestSecurityToken) = value
        """
        ...


    def __new__(cls, requestType:str = ..., keyType:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, requestType: str)
        __new__(cls: type, requestType: str, keyType: str)
        """
        ...


class RequestSecurityTokenResponse(WSTrustMessage): # skipped bases: <type 'object'>
    """
    RequestSecurityTokenResponse()
    RequestSecurityTokenResponse(message: WSTrustMessage)
    """
    @property
    def IsFinal(self) -> bool:
        """
        Get: IsFinal(self: RequestSecurityTokenResponse) -> bool
        Set: IsFinal(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def RequestedAttachedReference(self) -> SecurityKeyIdentifierClause:
        """
        Get: RequestedAttachedReference(self: RequestSecurityTokenResponse) -> SecurityKeyIdentifierClause
        Set: RequestedAttachedReference(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def RequestedProofToken(self) -> RequestedProofToken:
        """
        Get: RequestedProofToken(self: RequestSecurityTokenResponse) -> RequestedProofToken
        Set: RequestedProofToken(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def RequestedSecurityToken(self) -> RequestedSecurityToken:
        """
        Get: RequestedSecurityToken(self: RequestSecurityTokenResponse) -> RequestedSecurityToken
        Set: RequestedSecurityToken(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def RequestedTokenCancelled(self) -> bool:
        """
        Get: RequestedTokenCancelled(self: RequestSecurityTokenResponse) -> bool
        Set: RequestedTokenCancelled(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def RequestedUnattachedReference(self) -> SecurityKeyIdentifierClause:
        """
        Get: RequestedUnattachedReference(self: RequestSecurityTokenResponse) -> SecurityKeyIdentifierClause
        Set: RequestedUnattachedReference(self: RequestSecurityTokenResponse) = value
        """
        ...

    @property
    def Status(self) -> Status:
        """
        Get: Status(self: RequestSecurityTokenResponse) -> Status
        Set: Status(self: RequestSecurityTokenResponse) = value
        """
        ...


    def __new__(cls, message:WSTrustMessage = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: WSTrustMessage)
        """
        ...


class RequestTypes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Cancel: str = ...
    GetMetadata: str = ...
    Issue: str = ...
    IssueCard: str = ...
    Renew: str = ...
    Validate: str = ...
    __all__: list = ...


class Status: # skipped bases: <type 'object'>, <type 'object'>
    """ Status(code: str, reason: str) """
    @property
    def Code(self) -> str:
        """
        Get: Code(self: Status) -> str
        Set: Code(self: Status) = value
        """
        ...

    @property
    def Reason(self) -> str:
        """
        Get: Reason(self: Status) -> str
        Set: Reason(self: Status) = value
        """
        ...



class UseKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    UseKey()
    UseKey(ski: SecurityKeyIdentifier)
    UseKey(token: SecurityToken)
    UseKey(ski: SecurityKeyIdentifier, token: SecurityToken)
    """
    @property
    def SecurityKeyIdentifier(self) -> SecurityKeyIdentifier:
        """ Get: SecurityKeyIdentifier(self: UseKey) -> SecurityKeyIdentifier """
        ...

    @property
    def Token(self) -> SecurityToken:
        """ Get: Token(self: UseKey) -> SecurityToken """
        ...



class WSTrustRequestSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: WSTrustRequestSerializer, reader: XmlReader) -> bool """
        ...

    def CreateRequestSecurityToken(self) -> RequestSecurityToken:
        """ CreateRequestSecurityToken(self: WSTrustRequestSerializer) -> RequestSecurityToken """
        ...

    def ReadCustomElement(self, *args): #cannot find CLR method
        """ ReadCustomElement(self: WSTrustRequestSerializer, reader: XmlReader, context: WSTrustSerializationContext) """
        ...

    def ReadXml(self, reader:XmlReader, context:WSTrustSerializationContext) -> RequestSecurityToken:
        """ ReadXml(self: WSTrustRequestSerializer, reader: XmlReader, context: WSTrustSerializationContext) -> RequestSecurityToken """
        ...

    def ReadXmlElement(self, reader:XmlReader, requestSecurityToken:RequestSecurityToken, context:WSTrustSerializationContext): # -> 
        """ ReadXmlElement(self: WSTrustRequestSerializer, reader: XmlReader, requestSecurityToken: RequestSecurityToken, context: WSTrustSerializationContext) """
        ...

    def Validate(self, requestSecurityToken:RequestSecurityToken): # -> 
        """ Validate(self: WSTrustRequestSerializer, requestSecurityToken: RequestSecurityToken) """
        ...

    def WriteKnownRequestElement(self, requestSecurityToken:RequestSecurityToken, writer:XmlWriter, context:WSTrustSerializationContext): # -> 
        """ WriteKnownRequestElement(self: WSTrustRequestSerializer, requestSecurityToken: RequestSecurityToken, writer: XmlWriter, context: WSTrustSerializationContext) """
        ...

    def WriteXml(self, request:RequestSecurityToken, writer:XmlWriter, context:WSTrustSerializationContext): # -> 
        """ WriteXml(self: WSTrustRequestSerializer, request: RequestSecurityToken, writer: XmlWriter, context: WSTrustSerializationContext) """
        ...

    def WriteXmlElement(self, writer:XmlWriter, elementName:str, elementValue:object, requestSecurityToken:RequestSecurityToken, context:WSTrustSerializationContext): # -> 
        """ WriteXmlElement(self: WSTrustRequestSerializer, writer: XmlWriter, elementName: str, elementValue: object, requestSecurityToken: RequestSecurityToken, context: WSTrustSerializationContext) """
        ...


class WSTrust13RequestSerializer(WSTrustRequestSerializer): # skipped bases: <type 'object'>
    """ WSTrust13RequestSerializer() """
    def ReadSecondaryParameters(self, *args): #cannot find CLR method
        """ ReadSecondaryParameters(self: WSTrust13RequestSerializer, reader: XmlReader, context: WSTrustSerializationContext) -> RequestSecurityToken """
        ...


class WSTrustResponseSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: WSTrustResponseSerializer, reader: XmlReader) -> bool """
        ...

    def CreateInstance(self) -> RequestSecurityTokenResponse:
        """ CreateInstance(self: WSTrustResponseSerializer) -> RequestSecurityTokenResponse """
        ...

    def ReadXml(self, reader:XmlReader, context:WSTrustSerializationContext) -> RequestSecurityTokenResponse:
        """ ReadXml(self: WSTrustResponseSerializer, reader: XmlReader, context: WSTrustSerializationContext) -> RequestSecurityTokenResponse """
        ...

    def ReadXmlElement(self, reader:XmlReader, requestSecurityTokenResponse:RequestSecurityTokenResponse, context:WSTrustSerializationContext): # -> 
        """ ReadXmlElement(self: WSTrustResponseSerializer, reader: XmlReader, requestSecurityTokenResponse: RequestSecurityTokenResponse, context: WSTrustSerializationContext) """
        ...

    def Validate(self, requestSecurityTokenResponse:RequestSecurityTokenResponse): # -> 
        """ Validate(self: WSTrustResponseSerializer, requestSecurityTokenResponse: RequestSecurityTokenResponse) """
        ...

    def WriteKnownResponseElement(self, requestSecurityTokenResponse:RequestSecurityTokenResponse, writer:XmlWriter, context:WSTrustSerializationContext): # -> 
        """ WriteKnownResponseElement(self: WSTrustResponseSerializer, requestSecurityTokenResponse: RequestSecurityTokenResponse, writer: XmlWriter, context: WSTrustSerializationContext) """
        ...

    def WriteXml(self, response:RequestSecurityTokenResponse, writer:XmlWriter, context:WSTrustSerializationContext): # -> 
        """ WriteXml(self: WSTrustResponseSerializer, response: RequestSecurityTokenResponse, writer: XmlWriter, context: WSTrustSerializationContext) """
        ...

    def WriteXmlElement(self, writer:XmlWriter, elementName:str, elementValue:object, requestSecurityTokenResponse:RequestSecurityTokenResponse, context:WSTrustSerializationContext): # -> 
        """ WriteXmlElement(self: WSTrustResponseSerializer, writer: XmlWriter, elementName: str, elementValue: object, requestSecurityTokenResponse: RequestSecurityTokenResponse, context: WSTrustSerializationContext) """
        ...


class WSTrust13ResponseSerializer(WSTrustResponseSerializer): # skipped bases: <type 'object'>
    """ WSTrust13ResponseSerializer() """
    pass

class WSTrustFeb2005RequestSerializer(WSTrustRequestSerializer): # skipped bases: <type 'object'>
    """ WSTrustFeb2005RequestSerializer() """
    pass

class WSTrustFeb2005ResponseSerializer(WSTrustResponseSerializer): # skipped bases: <type 'object'>
    """ WSTrustFeb2005ResponseSerializer() """
    pass

class WSTrustSerializationContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    WSTrustSerializationContext()
    WSTrustSerializationContext(securityTokenHandlerCollectionManager: SecurityTokenHandlerCollectionManager)
    WSTrustSerializationContext(securityTokenHandlerCollectionManager: SecurityTokenHandlerCollectionManager, securityTokenResolver: SecurityTokenResolver, useKeyTokenResolver: SecurityTokenResolver)
    """
    @property
    def SecurityTokenHandlerCollectionManager(self) -> SecurityTokenHandlerCollectionManager:
        """
        Get: SecurityTokenHandlerCollectionManager(self: WSTrustSerializationContext) -> SecurityTokenHandlerCollectionManager
        Set: SecurityTokenHandlerCollectionManager(self: WSTrustSerializationContext) = value
        """
        ...

    @property
    def SecurityTokenHandlers(self) -> SecurityTokenHandlerCollection:
        """ Get: SecurityTokenHandlers(self: WSTrustSerializationContext) -> SecurityTokenHandlerCollection """
        ...

    @property
    def TokenResolver(self) -> SecurityTokenResolver:
        """
        Get: TokenResolver(self: WSTrustSerializationContext) -> SecurityTokenResolver
        Set: TokenResolver(self: WSTrustSerializationContext) = value
        """
        ...

    @property
    def UseKeyTokenResolver(self) -> SecurityTokenResolver:
        """
        Get: UseKeyTokenResolver(self: WSTrustSerializationContext) -> SecurityTokenResolver
        Set: UseKeyTokenResolver(self: WSTrustSerializationContext) = value
        """
        ...



class WSTrustSerializationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WSTrustSerializationException()
    WSTrustSerializationException(message: str)
    WSTrustSerializationException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


