# encoding: utf-8
# module System.Data.Sql calls itself Sql
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Data.Common import DbDataSourceEnumerator


# no functions
# classes

class SqlDataSourceEnumerator(DbDataSourceEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Instance(self) -> SqlDataSourceEnumerator:
        """ Get: Instance() -> SqlDataSourceEnumerator """
        ...




class SqlNotificationRequest: # skipped bases: <type 'object'>, <type 'object'>
    """
    SqlNotificationRequest()
    SqlNotificationRequest(userData: str, options: str, timeout: int)
    """
    @property
    def Options(self) -> str:
        """
        Get: Options(self: SqlNotificationRequest) -> str
        Set: Options(self: SqlNotificationRequest) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: SqlNotificationRequest) -> int
        Set: Timeout(self: SqlNotificationRequest) = value
        """
        ...

    @property
    def UserData(self) -> str:
        """
        Get: UserData(self: SqlNotificationRequest) -> str
        Set: UserData(self: SqlNotificationRequest) = value
        """
        ...



