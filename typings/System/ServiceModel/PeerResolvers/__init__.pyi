# encoding: utf-8
# module System.ServiceModel.PeerResolvers calls itself PeerResolvers
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from System import Enum, Guid, TimeSpan

from System.Collections import IList

from System.ServiceModel import (EndpointAddress, PeerNodeAddress, 
    PeerResolver)

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CustomPeerResolverService(IPeerResolverContract): # skipped bases: <type 'object'>
    """ CustomPeerResolverService() """
    @property
    def CleanupInterval(self) -> TimeSpan:
        """
        Get: CleanupInterval(self: CustomPeerResolverService) -> TimeSpan
        Set: CleanupInterval(self: CustomPeerResolverService) = value
        """
        ...

    @property
    def ControlShape(self) -> bool:
        """
        Get: ControlShape(self: CustomPeerResolverService) -> bool
        Set: ControlShape(self: CustomPeerResolverService) = value
        """
        ...

    @property
    def RefreshInterval(self) -> TimeSpan:
        """
        Get: RefreshInterval(self: CustomPeerResolverService) -> TimeSpan
        Set: RefreshInterval(self: CustomPeerResolverService) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: CustomPeerResolverService) """
        ...

    def Open(self): # -> 
        """ Open(self: CustomPeerResolverService) """
        ...


class IPeerResolverContract: # skipped bases: <type 'object'>
    """ no doc """
    def GetServiceSettings(self) -> ServiceSettingsResponseInfo:
        """ GetServiceSettings(self: IPeerResolverContract) -> ServiceSettingsResponseInfo """
        ...

    def Refresh(self, refreshInfo:RefreshInfo) -> RefreshResponseInfo:
        """ Refresh(self: IPeerResolverContract, refreshInfo: RefreshInfo) -> RefreshResponseInfo """
        ...

    def Register(self, registerInfo:RegisterInfo) -> RegisterResponseInfo:
        """ Register(self: IPeerResolverContract, registerInfo: RegisterInfo) -> RegisterResponseInfo """
        ...

    def Resolve(self, resolveInfo:ResolveInfo) -> ResolveResponseInfo:
        """ Resolve(self: IPeerResolverContract, resolveInfo: ResolveInfo) -> ResolveResponseInfo """
        ...

    def Unregister(self, unregisterInfo:UnregisterInfo): # -> 
        """ Unregister(self: IPeerResolverContract, unregisterInfo: UnregisterInfo) """
        ...

    def Update(self, updateInfo:UpdateInfo) -> RegisterResponseInfo:
        """ Update(self: IPeerResolverContract, updateInfo: UpdateInfo) -> RegisterResponseInfo """
        ...


class PeerCustomResolverSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerCustomResolverSettings() """
    @property
    def Address(self) -> EndpointAddress:
        """
        Get: Address(self: PeerCustomResolverSettings) -> EndpointAddress
        Set: Address(self: PeerCustomResolverSettings) = value
        """
        ...

    @property
    def Binding(self) -> Binding:
        """
        Get: Binding(self: PeerCustomResolverSettings) -> Binding
        Set: Binding(self: PeerCustomResolverSettings) = value
        """
        ...

    @property
    def IsBindingSpecified(self) -> bool:
        """ Get: IsBindingSpecified(self: PeerCustomResolverSettings) -> bool """
        ...

    @property
    def Resolver(self) -> PeerResolver:
        """
        Get: Resolver(self: PeerCustomResolverSettings) -> PeerResolver
        Set: Resolver(self: PeerCustomResolverSettings) = value
        """
        ...



class PeerReferralPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerReferralPolicy, values: DoNotShare (2), Service (0), Share (1) """
    DoNotShare: PeerReferralPolicy = ...
    Service: PeerReferralPolicy = ...
    Share: PeerReferralPolicy = ...
    value__ = ...


class PeerResolverMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PeerResolverMode, values: Auto (0), Custom (2), Pnrp (1) """
    Auto: PeerResolverMode = ...
    Custom: PeerResolverMode = ...
    Pnrp: PeerResolverMode = ...
    value__ = ...


class PeerResolverSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ PeerResolverSettings() """
    @property
    def Custom(self) -> PeerCustomResolverSettings:
        """ Get: Custom(self: PeerResolverSettings) -> PeerCustomResolverSettings """
        ...

    @property
    def Mode(self) -> PeerResolverMode:
        """
        Get: Mode(self: PeerResolverSettings) -> PeerResolverMode
        Set: Mode(self: PeerResolverSettings) = value
        """
        ...

    @property
    def ReferralPolicy(self) -> PeerReferralPolicy:
        """
        Get: ReferralPolicy(self: PeerResolverSettings) -> PeerReferralPolicy
        Set: ReferralPolicy(self: PeerResolverSettings) = value
        """
        ...



class RefreshInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RefreshInfo(meshId: str, regId: Guid)
    RefreshInfo()
    """
    @property
    def MeshId(self) -> str:
        """ Get: MeshId(self: RefreshInfo) -> str """
        ...

    @property
    def RegistrationId(self) -> Guid:
        """ Get: RegistrationId(self: RefreshInfo) -> Guid """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: RefreshInfo) -> bool """
        ...


class RefreshResponseInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RefreshResponseInfo()
    RefreshResponseInfo(registrationLifetime: TimeSpan, result: RefreshResult)
    """
    @property
    def RegistrationLifetime(self) -> TimeSpan:
        """
        Get: RegistrationLifetime(self: RefreshResponseInfo) -> TimeSpan
        Set: RegistrationLifetime(self: RefreshResponseInfo) = value
        """
        ...

    @property
    def Result(self) -> RefreshResult:
        """
        Get: Result(self: RefreshResponseInfo) -> RefreshResult
        Set: Result(self: RefreshResponseInfo) = value
        """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: RefreshResponseInfo) -> bool """
        ...


class RefreshResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RefreshResult, values: RegistrationNotFound (1), Success (0) """
    RegistrationNotFound: RefreshResult = ...
    Success: RefreshResult = ...
    value__ = ...


class RegisterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RegisterInfo(client: Guid, meshId: str, address: PeerNodeAddress)
    RegisterInfo()
    """
    @property
    def ClientId(self) -> Guid:
        """ Get: ClientId(self: RegisterInfo) -> Guid """
        ...

    @property
    def MeshId(self) -> str:
        """ Get: MeshId(self: RegisterInfo) -> str """
        ...

    @property
    def NodeAddress(self) -> PeerNodeAddress:
        """ Get: NodeAddress(self: RegisterInfo) -> PeerNodeAddress """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: RegisterInfo) -> bool """
        ...


class RegisterResponseInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RegisterResponseInfo(registrationId: Guid, registrationLifetime: TimeSpan)
    RegisterResponseInfo()
    """
    @property
    def RegistrationId(self) -> Guid:
        """
        Get: RegistrationId(self: RegisterResponseInfo) -> Guid
        Set: RegistrationId(self: RegisterResponseInfo) = value
        """
        ...

    @property
    def RegistrationLifetime(self) -> TimeSpan:
        """
        Get: RegistrationLifetime(self: RegisterResponseInfo) -> TimeSpan
        Set: RegistrationLifetime(self: RegisterResponseInfo) = value
        """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: RegisterResponseInfo) -> bool """
        ...


class ResolveInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResolveInfo(clientId: Guid, meshId: str, maxAddresses: int)
    ResolveInfo()
    """
    @property
    def ClientId(self) -> Guid:
        """ Get: ClientId(self: ResolveInfo) -> Guid """
        ...

    @property
    def MaxAddresses(self) -> int:
        """ Get: MaxAddresses(self: ResolveInfo) -> int """
        ...

    @property
    def MeshId(self) -> str:
        """ Get: MeshId(self: ResolveInfo) -> str """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: ResolveInfo) -> bool """
        ...


class ResolveResponseInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResolveResponseInfo()
    ResolveResponseInfo(addresses: Array[PeerNodeAddress])
    """
    @property
    def Addresses(self) -> IList:
        """
        Get: Addresses(self: ResolveResponseInfo) -> IList[PeerNodeAddress]
        Set: Addresses(self: ResolveResponseInfo) = value
        """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: ResolveResponseInfo) -> bool """
        ...


class ServiceSettingsResponseInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceSettingsResponseInfo()
    ServiceSettingsResponseInfo(control: bool)
    """
    @property
    def ControlMeshShape(self) -> bool:
        """
        Get: ControlMeshShape(self: ServiceSettingsResponseInfo) -> bool
        Set: ControlMeshShape(self: ServiceSettingsResponseInfo) = value
        """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: ServiceSettingsResponseInfo) -> bool """
        ...


class UnregisterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    UnregisterInfo()
    UnregisterInfo(meshId: str, registrationId: Guid)
    """
    @property
    def MeshId(self) -> str:
        """ Get: MeshId(self: UnregisterInfo) -> str """
        ...

    @property
    def RegistrationId(self) -> Guid:
        """ Get: RegistrationId(self: UnregisterInfo) -> Guid """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: UnregisterInfo) -> bool """
        ...


class UpdateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    UpdateInfo(registrationId: Guid, client: Guid, meshId: str, address: PeerNodeAddress)
    UpdateInfo()
    """
    @property
    def ClientId(self) -> Guid:
        """ Get: ClientId(self: UpdateInfo) -> Guid """
        ...

    @property
    def MeshId(self) -> str:
        """ Get: MeshId(self: UpdateInfo) -> str """
        ...

    @property
    def NodeAddress(self) -> PeerNodeAddress:
        """ Get: NodeAddress(self: UpdateInfo) -> PeerNodeAddress """
        ...

    @property
    def RegistrationId(self) -> Guid:
        """ Get: RegistrationId(self: UpdateInfo) -> Guid """
        ...


    def HasBody(self) -> bool:
        """ HasBody(self: UpdateInfo) -> bool """
        ...


