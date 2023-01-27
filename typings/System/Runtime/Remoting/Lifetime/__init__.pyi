# encoding: utf-8
# module System.Runtime.Remoting.Lifetime calls itself Lifetime
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, MarshalByRefObject, TimeSpan

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ClientSponsor(MarshalByRefObject, ISponsor): # skipped bases: <type 'object'>
    """
    ClientSponsor()
    ClientSponsor(renewalTime: TimeSpan)
    """
    @property
    def RenewalTime(self) -> TimeSpan:
        """
        Get: RenewalTime(self: ClientSponsor) -> TimeSpan
        Set: RenewalTime(self: ClientSponsor) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: ClientSponsor) """
        ...

    def Register(self, obj:MarshalByRefObject) -> bool:
        """ Register(self: ClientSponsor, obj: MarshalByRefObject) -> bool """
        ...

    def Unregister(self, obj:MarshalByRefObject): # -> 
        """ Unregister(self: ClientSponsor, obj: MarshalByRefObject) """
        ...

    def __new__(cls, renewalTime:TimeSpan = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, renewalTime: TimeSpan)
        """
        ...


class ILease: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentLeaseTime(self) -> TimeSpan:
        """ Get: CurrentLeaseTime(self: ILease) -> TimeSpan """
        ...

    @property
    def CurrentState(self) -> LeaseState:
        """ Get: CurrentState(self: ILease) -> LeaseState """
        ...

    @property
    def InitialLeaseTime(self) -> TimeSpan:
        """
        Get: InitialLeaseTime(self: ILease) -> TimeSpan
        Set: InitialLeaseTime(self: ILease) = value
        """
        ...

    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """
        Get: RenewOnCallTime(self: ILease) -> TimeSpan
        Set: RenewOnCallTime(self: ILease) = value
        """
        ...

    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """
        Get: SponsorshipTimeout(self: ILease) -> TimeSpan
        Set: SponsorshipTimeout(self: ILease) = value
        """
        ...


    def Register(self, obj:ISponsor, renewalTime:TimeSpan = ...): # -> 
        """ Register(self: ILease, obj: ISponsor, renewalTime: TimeSpan)Register(self: ILease, obj: ISponsor) """
        ...

    def Renew(self, renewalTime:TimeSpan) -> TimeSpan:
        """ Renew(self: ILease, renewalTime: TimeSpan) -> TimeSpan """
        ...

    def Unregister(self, obj:ISponsor): # -> 
        """ Unregister(self: ILease, obj: ISponsor) """
        ...


class ISponsor: # skipped bases: <type 'object'>
    """ no doc """
    def Renewal(self, lease:ILease) -> TimeSpan:
        """ Renewal(self: ISponsor, lease: ILease) -> TimeSpan """
        ...


class LeaseState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LeaseState, values: Active (2), Expired (4), Initial (1), Null (0), Renewing (3) """
    Active: LeaseState = ...
    Expired: LeaseState = ...
    Initial: LeaseState = ...
    Null: LeaseState = ...
    Renewing: LeaseState = ...
    value__ = ...


class LifetimeServices: # skipped bases: <type 'object'>, <type 'object'>
    """ LifetimeServices() """
    @property
    def LeaseManagerPollTime(self) -> TimeSpan:
        """
        Get: LeaseManagerPollTime() -> TimeSpan
        Set: LeaseManagerPollTime() = value
        """
        ...

    @property
    def LeaseTime(self) -> TimeSpan:
        """
        Get: LeaseTime() -> TimeSpan
        Set: LeaseTime() = value
        """
        ...

    @property
    def RenewOnCallTime(self) -> TimeSpan:
        """
        Get: RenewOnCallTime() -> TimeSpan
        Set: RenewOnCallTime() = value
        """
        ...

    @property
    def SponsorshipTimeout(self) -> TimeSpan:
        """
        Get: SponsorshipTimeout() -> TimeSpan
        Set: SponsorshipTimeout() = value
        """
        ...




