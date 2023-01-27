# encoding: utf-8
# module System.Web.Mail calls itself Mail
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Collections import IDictionary, IList

from System.Text import Encoding

"""The following names are not found in the module: field#
"""

# no functions
# classes

class MailAttachment: # skipped bases: <type 'object'>, <type 'object'>
    """
    MailAttachment(filename: str)
    MailAttachment(filename: str, encoding: MailEncoding)
    """
    @property
    def Encoding(self) -> MailEncoding:
        """ Get: Encoding(self: MailAttachment) -> MailEncoding """
        ...

    @property
    def Filename(self) -> str:
        """ Get: Filename(self: MailAttachment) -> str """
        ...



class MailEncoding(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MailEncoding, values: Base64 (1), UUEncode (0) """
    Base64: MailEncoding = ...
    UUEncode: MailEncoding = ...
    value__ = ...


class MailFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MailFormat, values: Html (1), Text (0) """
    Html: MailFormat = ...
    Text: MailFormat = ...
    value__ = ...


class MailMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ MailMessage() """
    @property
    def Attachments(self) -> IList:
        """ Get: Attachments(self: MailMessage) -> IList """
        ...

    @property
    def Bcc(self) -> str:
        """
        Get: Bcc(self: MailMessage) -> str
        Set: Bcc(self: MailMessage) = value
        """
        ...

    @property
    def Body(self) -> str:
        """
        Get: Body(self: MailMessage) -> str
        Set: Body(self: MailMessage) = value
        """
        ...

    @property
    def BodyEncoding(self) -> Encoding:
        """
        Get: BodyEncoding(self: MailMessage) -> Encoding
        Set: BodyEncoding(self: MailMessage) = value
        """
        ...

    @property
    def BodyFormat(self) -> MailFormat:
        """
        Get: BodyFormat(self: MailMessage) -> MailFormat
        Set: BodyFormat(self: MailMessage) = value
        """
        ...

    @property
    def Cc(self) -> str:
        """
        Get: Cc(self: MailMessage) -> str
        Set: Cc(self: MailMessage) = value
        """
        ...

    @property
    def Fields(self) -> IDictionary:
        """ Get: Fields(self: MailMessage) -> IDictionary """
        ...

    @property
    def From(self) -> str:
        """
        Get: From(self: MailMessage) -> str
        Set: From(self: MailMessage) = value
        """
        ...

    @property
    def Headers(self) -> IDictionary:
        """ Get: Headers(self: MailMessage) -> IDictionary """
        ...

    @property
    def Priority(self) -> MailPriority:
        """
        Get: Priority(self: MailMessage) -> MailPriority
        Set: Priority(self: MailMessage) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: MailMessage) -> str
        Set: Subject(self: MailMessage) = value
        """
        ...

    @property
    def To(self) -> str:
        """
        Get: To(self: MailMessage) -> str
        Set: To(self: MailMessage) = value
        """
        ...

    @property
    def UrlContentBase(self) -> str:
        """
        Get: UrlContentBase(self: MailMessage) -> str
        Set: UrlContentBase(self: MailMessage) = value
        """
        ...

    @property
    def UrlContentLocation(self) -> str:
        """
        Get: UrlContentLocation(self: MailMessage) -> str
        Set: UrlContentLocation(self: MailMessage) = value
        """
        ...



class MailPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MailPriority, values: High (2), Low (1), Normal (0) """
    High: MailPriority = ...
    Low: MailPriority = ...
    Normal: MailPriority = ...
    value__ = ...


class SmtpMail: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SmtpServer(self) -> str:
        """
        Get: SmtpServer() -> str
        Set: SmtpServer() = value
        """
        ...


    @staticmethod
    def Send(*__args:MailMessage): # -> 
        """ Send(from: str, to: str, subject: str, messageText: str)Send(message: MailMessage) """
        ...



