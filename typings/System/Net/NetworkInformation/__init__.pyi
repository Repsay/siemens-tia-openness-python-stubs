# encoding: utf-8
# module System.Net.NetworkInformation calls itself NetworkInformation
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    Int64, InvalidOperationException, MulticastDelegate)

from System.Collections import ICollection, IEnumerator

from System.ComponentModel import (AsyncCompletedEventArgs, Component, 
    Win32Exception)

from System.Net import IPAddress, IPEndPoint

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Threading.Tasks import Task

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DuplicateAddressDetectionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DuplicateAddressDetectionState, values: Deprecated (3), Duplicate (2), Invalid (0), Preferred (4), Tentative (1) """
    Deprecated: DuplicateAddressDetectionState = ...
    Duplicate: DuplicateAddressDetectionState = ...
    Invalid: DuplicateAddressDetectionState = ...
    Preferred: DuplicateAddressDetectionState = ...
    Tentative: DuplicateAddressDetectionState = ...
    value__ = ...


class GatewayIPAddressInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Address(self) -> IPAddress:
        """ Get: Address(self: GatewayIPAddressInformation) -> IPAddress """
        ...



class GatewayIPAddressInformationCollection(ICollection): # skipped bases: <type 'IEnumerable[GatewayIPAddressInformation]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: GatewayIPAddressInformationCollection) -> IEnumerator[GatewayIPAddressInformation] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IcmpV4Statistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AddressMaskRepliesReceived(self) -> Int64:
        """ Get: AddressMaskRepliesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def AddressMaskRepliesSent(self) -> Int64:
        """ Get: AddressMaskRepliesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def AddressMaskRequestsReceived(self) -> Int64:
        """ Get: AddressMaskRequestsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def AddressMaskRequestsSent(self) -> Int64:
        """ Get: AddressMaskRequestsSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def DestinationUnreachableMessagesReceived(self) -> Int64:
        """ Get: DestinationUnreachableMessagesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def DestinationUnreachableMessagesSent(self) -> Int64:
        """ Get: DestinationUnreachableMessagesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def EchoRepliesReceived(self) -> Int64:
        """ Get: EchoRepliesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def EchoRepliesSent(self) -> Int64:
        """ Get: EchoRepliesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def EchoRequestsReceived(self) -> Int64:
        """ Get: EchoRequestsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def EchoRequestsSent(self) -> Int64:
        """ Get: EchoRequestsSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def ErrorsReceived(self) -> Int64:
        """ Get: ErrorsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def ErrorsSent(self) -> Int64:
        """ Get: ErrorsSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def MessagesReceived(self) -> Int64:
        """ Get: MessagesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def MessagesSent(self) -> Int64:
        """ Get: MessagesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def ParameterProblemsReceived(self) -> Int64:
        """ Get: ParameterProblemsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def ParameterProblemsSent(self) -> Int64:
        """ Get: ParameterProblemsSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def RedirectsReceived(self) -> Int64:
        """ Get: RedirectsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def RedirectsSent(self) -> Int64:
        """ Get: RedirectsSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def SourceQuenchesReceived(self) -> Int64:
        """ Get: SourceQuenchesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def SourceQuenchesSent(self) -> Int64:
        """ Get: SourceQuenchesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimeExceededMessagesReceived(self) -> Int64:
        """ Get: TimeExceededMessagesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimeExceededMessagesSent(self) -> Int64:
        """ Get: TimeExceededMessagesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimestampRepliesReceived(self) -> Int64:
        """ Get: TimestampRepliesReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimestampRepliesSent(self) -> Int64:
        """ Get: TimestampRepliesSent(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimestampRequestsReceived(self) -> Int64:
        """ Get: TimestampRequestsReceived(self: IcmpV4Statistics) -> Int64 """
        ...

    @property
    def TimestampRequestsSent(self) -> Int64:
        """ Get: TimestampRequestsSent(self: IcmpV4Statistics) -> Int64 """
        ...



class IcmpV6Statistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DestinationUnreachableMessagesReceived(self) -> Int64:
        """ Get: DestinationUnreachableMessagesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def DestinationUnreachableMessagesSent(self) -> Int64:
        """ Get: DestinationUnreachableMessagesSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def EchoRepliesReceived(self) -> Int64:
        """ Get: EchoRepliesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def EchoRepliesSent(self) -> Int64:
        """ Get: EchoRepliesSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def EchoRequestsReceived(self) -> Int64:
        """ Get: EchoRequestsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def EchoRequestsSent(self) -> Int64:
        """ Get: EchoRequestsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def ErrorsReceived(self) -> Int64:
        """ Get: ErrorsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def ErrorsSent(self) -> Int64:
        """ Get: ErrorsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipQueriesReceived(self) -> Int64:
        """ Get: MembershipQueriesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipQueriesSent(self) -> Int64:
        """ Get: MembershipQueriesSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipReductionsReceived(self) -> Int64:
        """ Get: MembershipReductionsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipReductionsSent(self) -> Int64:
        """ Get: MembershipReductionsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipReportsReceived(self) -> Int64:
        """ Get: MembershipReportsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MembershipReportsSent(self) -> Int64:
        """ Get: MembershipReportsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MessagesReceived(self) -> Int64:
        """ Get: MessagesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def MessagesSent(self) -> Int64:
        """ Get: MessagesSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def NeighborAdvertisementsReceived(self) -> Int64:
        """ Get: NeighborAdvertisementsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def NeighborAdvertisementsSent(self) -> Int64:
        """ Get: NeighborAdvertisementsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def NeighborSolicitsReceived(self) -> Int64:
        """ Get: NeighborSolicitsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def NeighborSolicitsSent(self) -> Int64:
        """ Get: NeighborSolicitsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def PacketTooBigMessagesReceived(self) -> Int64:
        """ Get: PacketTooBigMessagesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def PacketTooBigMessagesSent(self) -> Int64:
        """ Get: PacketTooBigMessagesSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def ParameterProblemsReceived(self) -> Int64:
        """ Get: ParameterProblemsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def ParameterProblemsSent(self) -> Int64:
        """ Get: ParameterProblemsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RedirectsReceived(self) -> Int64:
        """ Get: RedirectsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RedirectsSent(self) -> Int64:
        """ Get: RedirectsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RouterAdvertisementsReceived(self) -> Int64:
        """ Get: RouterAdvertisementsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RouterAdvertisementsSent(self) -> Int64:
        """ Get: RouterAdvertisementsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RouterSolicitsReceived(self) -> Int64:
        """ Get: RouterSolicitsReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def RouterSolicitsSent(self) -> Int64:
        """ Get: RouterSolicitsSent(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def TimeExceededMessagesReceived(self) -> Int64:
        """ Get: TimeExceededMessagesReceived(self: IcmpV6Statistics) -> Int64 """
        ...

    @property
    def TimeExceededMessagesSent(self) -> Int64:
        """ Get: TimeExceededMessagesSent(self: IcmpV6Statistics) -> Int64 """
        ...



class IPAddressCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[IPAddress]'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: IPAddressCollection) -> IEnumerator[IPAddress] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IPAddressInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Address(self) -> IPAddress:
        """ Get: Address(self: IPAddressInformation) -> IPAddress """
        ...

    @property
    def IsDnsEligible(self) -> bool:
        """ Get: IsDnsEligible(self: IPAddressInformation) -> bool """
        ...

    @property
    def IsTransient(self) -> bool:
        """ Get: IsTransient(self: IPAddressInformation) -> bool """
        ...



class IPAddressInformationCollection(ICollection): # skipped bases: <type 'IEnumerable[IPAddressInformation]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: IPAddressInformationCollection) -> IEnumerator[IPAddressInformation] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class IPGlobalProperties: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DhcpScopeName(self) -> str:
        """ Get: DhcpScopeName(self: IPGlobalProperties) -> str """
        ...

    @property
    def DomainName(self) -> str:
        """ Get: DomainName(self: IPGlobalProperties) -> str """
        ...

    @property
    def HostName(self) -> str:
        """ Get: HostName(self: IPGlobalProperties) -> str """
        ...

    @property
    def IsWinsProxy(self) -> bool:
        """ Get: IsWinsProxy(self: IPGlobalProperties) -> bool """
        ...

    @property
    def NodeType(self) -> NetBiosNodeType:
        """ Get: NodeType(self: IPGlobalProperties) -> NetBiosNodeType """
        ...


    def BeginGetUnicastAddresses(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetUnicastAddresses(self: IPGlobalProperties, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndGetUnicastAddresses(self, asyncResult:IAsyncResult) -> UnicastIPAddressInformationCollection:
        """ EndGetUnicastAddresses(self: IPGlobalProperties, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection """
        ...

    def GetActiveTcpConnections(self) -> Array:
        """ GetActiveTcpConnections(self: IPGlobalProperties) -> Array[TcpConnectionInformation] """
        ...

    def GetActiveTcpListeners(self) -> Array:
        """ GetActiveTcpListeners(self: IPGlobalProperties) -> Array[IPEndPoint] """
        ...

    def GetActiveUdpListeners(self) -> Array:
        """ GetActiveUdpListeners(self: IPGlobalProperties) -> Array[IPEndPoint] """
        ...

    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:
        """ GetIcmpV4Statistics(self: IPGlobalProperties) -> IcmpV4Statistics """
        ...

    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:
        """ GetIcmpV6Statistics(self: IPGlobalProperties) -> IcmpV6Statistics """
        ...

    @staticmethod
    def GetIPGlobalProperties() -> IPGlobalProperties:
        """ GetIPGlobalProperties() -> IPGlobalProperties """
        ...

    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:
        """ GetIPv4GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics """
        ...

    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:
        """ GetIPv6GlobalStatistics(self: IPGlobalProperties) -> IPGlobalStatistics """
        ...

    def GetTcpIPv4Statistics(self) -> TcpStatistics:
        """ GetTcpIPv4Statistics(self: IPGlobalProperties) -> TcpStatistics """
        ...

    def GetTcpIPv6Statistics(self) -> TcpStatistics:
        """ GetTcpIPv6Statistics(self: IPGlobalProperties) -> TcpStatistics """
        ...

    def GetUdpIPv4Statistics(self) -> UdpStatistics:
        """ GetUdpIPv4Statistics(self: IPGlobalProperties) -> UdpStatistics """
        ...

    def GetUdpIPv6Statistics(self) -> UdpStatistics:
        """ GetUdpIPv6Statistics(self: IPGlobalProperties) -> UdpStatistics """
        ...

    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """ GetUnicastAddresses(self: IPGlobalProperties) -> UnicastIPAddressInformationCollection """
        ...

    def GetUnicastAddressesAsync(self) -> Task:
        """ GetUnicastAddressesAsync(self: IPGlobalProperties) -> Task[UnicastIPAddressInformationCollection] """
        ...


class IPGlobalStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultTtl(self) -> int:
        """ Get: DefaultTtl(self: IPGlobalStatistics) -> int """
        ...

    @property
    def ForwardingEnabled(self) -> bool:
        """ Get: ForwardingEnabled(self: IPGlobalStatistics) -> bool """
        ...

    @property
    def NumberOfInterfaces(self) -> int:
        """ Get: NumberOfInterfaces(self: IPGlobalStatistics) -> int """
        ...

    @property
    def NumberOfIPAddresses(self) -> int:
        """ Get: NumberOfIPAddresses(self: IPGlobalStatistics) -> int """
        ...

    @property
    def NumberOfRoutes(self) -> int:
        """ Get: NumberOfRoutes(self: IPGlobalStatistics) -> int """
        ...

    @property
    def OutputPacketRequests(self) -> Int64:
        """ Get: OutputPacketRequests(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def OutputPacketRoutingDiscards(self) -> Int64:
        """ Get: OutputPacketRoutingDiscards(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def OutputPacketsDiscarded(self) -> Int64:
        """ Get: OutputPacketsDiscarded(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def OutputPacketsWithNoRoute(self) -> Int64:
        """ Get: OutputPacketsWithNoRoute(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketFragmentFailures(self) -> Int64:
        """ Get: PacketFragmentFailures(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketReassembliesRequired(self) -> Int64:
        """ Get: PacketReassembliesRequired(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketReassemblyFailures(self) -> Int64:
        """ Get: PacketReassemblyFailures(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketReassemblyTimeout(self) -> Int64:
        """ Get: PacketReassemblyTimeout(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketsFragmented(self) -> Int64:
        """ Get: PacketsFragmented(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def PacketsReassembled(self) -> Int64:
        """ Get: PacketsReassembled(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPackets(self) -> Int64:
        """ Get: ReceivedPackets(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsDelivered(self) -> Int64:
        """ Get: ReceivedPacketsDelivered(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsDiscarded(self) -> Int64:
        """ Get: ReceivedPacketsDiscarded(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsForwarded(self) -> Int64:
        """ Get: ReceivedPacketsForwarded(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsWithAddressErrors(self) -> Int64:
        """ Get: ReceivedPacketsWithAddressErrors(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsWithHeadersErrors(self) -> Int64:
        """ Get: ReceivedPacketsWithHeadersErrors(self: IPGlobalStatistics) -> Int64 """
        ...

    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> Int64:
        """ Get: ReceivedPacketsWithUnknownProtocol(self: IPGlobalStatistics) -> Int64 """
        ...



class IPInterfaceProperties: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:
        """ Get: AnycastAddresses(self: IPInterfaceProperties) -> IPAddressInformationCollection """
        ...

    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:
        """ Get: DhcpServerAddresses(self: IPInterfaceProperties) -> IPAddressCollection """
        ...

    @property
    def DnsAddresses(self) -> IPAddressCollection:
        """ Get: DnsAddresses(self: IPInterfaceProperties) -> IPAddressCollection """
        ...

    @property
    def DnsSuffix(self) -> str:
        """ Get: DnsSuffix(self: IPInterfaceProperties) -> str """
        ...

    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:
        """ Get: GatewayAddresses(self: IPInterfaceProperties) -> GatewayIPAddressInformationCollection """
        ...

    @property
    def IsDnsEnabled(self) -> bool:
        """ Get: IsDnsEnabled(self: IPInterfaceProperties) -> bool """
        ...

    @property
    def IsDynamicDnsEnabled(self) -> bool:
        """ Get: IsDynamicDnsEnabled(self: IPInterfaceProperties) -> bool """
        ...

    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:
        """ Get: MulticastAddresses(self: IPInterfaceProperties) -> MulticastIPAddressInformationCollection """
        ...

    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """ Get: UnicastAddresses(self: IPInterfaceProperties) -> UnicastIPAddressInformationCollection """
        ...

    @property
    def WinsServersAddresses(self) -> IPAddressCollection:
        """ Get: WinsServersAddresses(self: IPInterfaceProperties) -> IPAddressCollection """
        ...


    def GetIPv4Properties(self) -> IPv4InterfaceProperties:
        """ GetIPv4Properties(self: IPInterfaceProperties) -> IPv4InterfaceProperties """
        ...

    def GetIPv6Properties(self) -> IPv6InterfaceProperties:
        """ GetIPv6Properties(self: IPInterfaceProperties) -> IPv6InterfaceProperties """
        ...


class IPInterfaceStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BytesReceived(self) -> Int64:
        """ Get: BytesReceived(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def BytesSent(self) -> Int64:
        """ Get: BytesSent(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingPacketsDiscarded(self) -> Int64:
        """ Get: IncomingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingPacketsWithErrors(self) -> Int64:
        """ Get: IncomingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingUnknownProtocolPackets(self) -> Int64:
        """ Get: IncomingUnknownProtocolPackets(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def NonUnicastPacketsReceived(self) -> Int64:
        """ Get: NonUnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def NonUnicastPacketsSent(self) -> Int64:
        """ Get: NonUnicastPacketsSent(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def OutgoingPacketsDiscarded(self) -> Int64:
        """ Get: OutgoingPacketsDiscarded(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def OutgoingPacketsWithErrors(self) -> Int64:
        """ Get: OutgoingPacketsWithErrors(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def OutputQueueLength(self) -> Int64:
        """ Get: OutputQueueLength(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def UnicastPacketsReceived(self) -> Int64:
        """ Get: UnicastPacketsReceived(self: IPInterfaceStatistics) -> Int64 """
        ...

    @property
    def UnicastPacketsSent(self) -> Int64:
        """ Get: UnicastPacketsSent(self: IPInterfaceStatistics) -> Int64 """
        ...



class IPStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IPStatus, values: BadDestination (11018), BadHeader (11042), BadOption (11007), BadRoute (11012), DestinationHostUnreachable (11003), DestinationNetworkUnreachable (11002), DestinationPortUnreachable (11005), DestinationProhibited (11004), DestinationProtocolUnreachable (11004), DestinationScopeMismatch (11045), DestinationUnreachable (11040), HardwareError (11008), IcmpError (11044), NoResources (11006), PacketTooBig (11009), ParameterProblem (11015), SourceQuench (11016), Success (0), TimedOut (11010), TimeExceeded (11041), TtlExpired (11013), TtlReassemblyTimeExceeded (11014), Unknown (-1), UnrecognizedNextHeader (11043) """
    BadDestination: IPStatus = ...
    BadHeader: IPStatus = ...
    BadOption: IPStatus = ...
    BadRoute: IPStatus = ...
    DestinationHostUnreachable: IPStatus = ...
    DestinationNetworkUnreachable: IPStatus = ...
    DestinationPortUnreachable: IPStatus = ...
    DestinationProhibited: IPStatus = ...
    DestinationProtocolUnreachable: IPStatus = ...
    DestinationScopeMismatch: IPStatus = ...
    DestinationUnreachable: IPStatus = ...
    HardwareError: IPStatus = ...
    IcmpError: IPStatus = ...
    NoResources: IPStatus = ...
    PacketTooBig: IPStatus = ...
    ParameterProblem: IPStatus = ...
    SourceQuench: IPStatus = ...
    Success: IPStatus = ...
    TimedOut: IPStatus = ...
    TimeExceeded: IPStatus = ...
    TtlExpired: IPStatus = ...
    TtlReassemblyTimeExceeded: IPStatus = ...
    Unknown: IPStatus = ...
    UnrecognizedNextHeader: IPStatus = ...
    value__ = ...


class IPv4InterfaceProperties: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: IPv4InterfaceProperties) -> int """
        ...

    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:
        """ Get: IsAutomaticPrivateAddressingActive(self: IPv4InterfaceProperties) -> bool """
        ...

    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:
        """ Get: IsAutomaticPrivateAddressingEnabled(self: IPv4InterfaceProperties) -> bool """
        ...

    @property
    def IsDhcpEnabled(self) -> bool:
        """ Get: IsDhcpEnabled(self: IPv4InterfaceProperties) -> bool """
        ...

    @property
    def IsForwardingEnabled(self) -> bool:
        """ Get: IsForwardingEnabled(self: IPv4InterfaceProperties) -> bool """
        ...

    @property
    def Mtu(self) -> int:
        """ Get: Mtu(self: IPv4InterfaceProperties) -> int """
        ...

    @property
    def UsesWins(self) -> bool:
        """ Get: UsesWins(self: IPv4InterfaceProperties) -> bool """
        ...



class IPv4InterfaceStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BytesReceived(self) -> Int64:
        """ Get: BytesReceived(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def BytesSent(self) -> Int64:
        """ Get: BytesSent(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingPacketsDiscarded(self) -> Int64:
        """ Get: IncomingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingPacketsWithErrors(self) -> Int64:
        """ Get: IncomingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def IncomingUnknownProtocolPackets(self) -> Int64:
        """ Get: IncomingUnknownProtocolPackets(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def NonUnicastPacketsReceived(self) -> Int64:
        """ Get: NonUnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def NonUnicastPacketsSent(self) -> Int64:
        """ Get: NonUnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def OutgoingPacketsDiscarded(self) -> Int64:
        """ Get: OutgoingPacketsDiscarded(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def OutgoingPacketsWithErrors(self) -> Int64:
        """ Get: OutgoingPacketsWithErrors(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def OutputQueueLength(self) -> Int64:
        """ Get: OutputQueueLength(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def UnicastPacketsReceived(self) -> Int64:
        """ Get: UnicastPacketsReceived(self: IPv4InterfaceStatistics) -> Int64 """
        ...

    @property
    def UnicastPacketsSent(self) -> Int64:
        """ Get: UnicastPacketsSent(self: IPv4InterfaceStatistics) -> Int64 """
        ...



class IPv6InterfaceProperties: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: IPv6InterfaceProperties) -> int """
        ...

    @property
    def Mtu(self) -> int:
        """ Get: Mtu(self: IPv6InterfaceProperties) -> int """
        ...


    def GetScopeId(self, scopeLevel:ScopeLevel) -> Int64:
        """ GetScopeId(self: IPv6InterfaceProperties, scopeLevel: ScopeLevel) -> Int64 """
        ...


class MulticastIPAddressInformation(IPAddressInformation): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AddressPreferredLifetime(self) -> Int64:
        """ Get: AddressPreferredLifetime(self: MulticastIPAddressInformation) -> Int64 """
        ...

    @property
    def AddressValidLifetime(self) -> Int64:
        """ Get: AddressValidLifetime(self: MulticastIPAddressInformation) -> Int64 """
        ...

    @property
    def DhcpLeaseLifetime(self) -> Int64:
        """ Get: DhcpLeaseLifetime(self: MulticastIPAddressInformation) -> Int64 """
        ...

    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """ Get: DuplicateAddressDetectionState(self: MulticastIPAddressInformation) -> DuplicateAddressDetectionState """
        ...

    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """ Get: PrefixOrigin(self: MulticastIPAddressInformation) -> PrefixOrigin """
        ...

    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """ Get: SuffixOrigin(self: MulticastIPAddressInformation) -> SuffixOrigin """
        ...



class MulticastIPAddressInformationCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[MulticastIPAddressInformation]'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MulticastIPAddressInformationCollection) -> IEnumerator[MulticastIPAddressInformation] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class NetBiosNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetBiosNodeType, values: Broadcast (1), Hybrid (8), Mixed (4), Peer2Peer (2), Unknown (0) """
    Broadcast: NetBiosNodeType = ...
    Hybrid: NetBiosNodeType = ...
    Mixed: NetBiosNodeType = ...
    Peer2Peer: NetBiosNodeType = ...
    Unknown: NetBiosNodeType = ...
    value__ = ...


class NetworkAddressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ NetworkAddressChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: NetworkAddressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArgs): # -> 
        """ Invoke(self: NetworkAddressChangedEventHandler, sender: object, e: EventArgs) """
        ...


class NetworkAvailabilityChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ NetworkAvailabilityChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:NetworkAvailabilityEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: NetworkAvailabilityChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:NetworkAvailabilityEventArgs): # -> 
        """ Invoke(self: NetworkAvailabilityChangedEventHandler, sender: object, e: NetworkAvailabilityEventArgs) """
        ...


class NetworkAvailabilityEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsAvailable(self) -> bool:
        """ Get: IsAvailable(self: NetworkAvailabilityEventArgs) -> bool """
        ...



class NetworkChange: # skipped bases: <type 'object'>, <type 'object'>
    """ NetworkChange() """
    @staticmethod
    def RegisterNetworkChange(nc:NetworkChange): # -> 
        """ RegisterNetworkChange(nc: NetworkChange) """
        ...

    NetworkAddressChanged = ...
    NetworkAvailabilityChanged = ...


class NetworkInformationAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NetworkInformationAccess, values: None (0), Ping (4), Read (1) """
    Ping: NetworkInformationAccess = ...
    Read: NetworkInformationAccess = ...
    value__ = ...


class NetworkInformationException(Win32Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NetworkInformationException()
    NetworkInformationException(errorCode: int)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: NetworkInformationException) -> int """
        ...


    SerializeObjectState = ...


class NetworkInformationPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    NetworkInformationPermission(state: PermissionState)
    NetworkInformationPermission(access: NetworkInformationAccess)
    """
    @property
    def Access(self) -> NetworkInformationAccess:
        """ Get: Access(self: NetworkInformationPermission) -> NetworkInformationAccess """
        ...


    def AddPermission(self, access:NetworkInformationAccess): # -> 
        """ AddPermission(self: NetworkInformationPermission, access: NetworkInformationAccess) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: NetworkInformationAccess)
        """
        ...


class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NetworkInformationPermissionAttribute(action: SecurityAction) """
    @property
    def Access(self) -> str:
        """
        Get: Access(self: NetworkInformationPermissionAttribute) -> str
        Set: Access(self: NetworkInformationPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: NetworkInformationPermissionAttribute) -> IPermission """
        ...


class NetworkInterface: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: NetworkInterface) -> str """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: NetworkInterface) -> str """
        ...

    @property
    def IPv6LoopbackInterfaceIndex(self) -> int:
        """ Get: IPv6LoopbackInterfaceIndex() -> int """
        ...

    @property
    def IsReceiveOnly(self) -> bool:
        """ Get: IsReceiveOnly(self: NetworkInterface) -> bool """
        ...

    @property
    def LoopbackInterfaceIndex(self) -> int:
        """ Get: LoopbackInterfaceIndex() -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: NetworkInterface) -> str """
        ...

    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:
        """ Get: NetworkInterfaceType(self: NetworkInterface) -> NetworkInterfaceType """
        ...

    @property
    def OperationalStatus(self) -> OperationalStatus:
        """ Get: OperationalStatus(self: NetworkInterface) -> OperationalStatus """
        ...

    @property
    def Speed(self) -> Int64:
        """ Get: Speed(self: NetworkInterface) -> Int64 """
        ...

    @property
    def SupportsMulticast(self) -> bool:
        """ Get: SupportsMulticast(self: NetworkInterface) -> bool """
        ...


    @staticmethod
    def GetAllNetworkInterfaces() -> Array:
        """ GetAllNetworkInterfaces() -> Array[NetworkInterface] """
        ...

    def GetIPProperties(self) -> IPInterfaceProperties:
        """ GetIPProperties(self: NetworkInterface) -> IPInterfaceProperties """
        ...

    def GetIPStatistics(self) -> IPInterfaceStatistics:
        """ GetIPStatistics(self: NetworkInterface) -> IPInterfaceStatistics """
        ...

    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:
        """ GetIPv4Statistics(self: NetworkInterface) -> IPv4InterfaceStatistics """
        ...

    @staticmethod
    def GetIsNetworkAvailable() -> bool:
        """ GetIsNetworkAvailable() -> bool """
        ...

    def GetPhysicalAddress(self) -> PhysicalAddress:
        """ GetPhysicalAddress(self: NetworkInterface) -> PhysicalAddress """
        ...

    def Supports(self, networkInterfaceComponent:NetworkInterfaceComponent) -> bool:
        """ Supports(self: NetworkInterface, networkInterfaceComponent: NetworkInterfaceComponent) -> bool """
        ...



class NetworkInterfaceComponent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetworkInterfaceComponent, values: IPv4 (0), IPv6 (1) """
    IPv4: NetworkInterfaceComponent = ...
    IPv6: NetworkInterfaceComponent = ...
    value__ = ...


class NetworkInterfaceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetworkInterfaceType, values: AsymmetricDsl (94), Atm (37), BasicIsdn (20), Ethernet (6), Ethernet3Megabit (26), FastEthernetFx (69), FastEthernetT (62), Fddi (15), GenericModem (48), GigabitEthernet (117), HighPerformanceSerialBus (144), IPOverAtm (114), Isdn (63), Loopback (24), MultiRateSymmetricDsl (143), Ppp (23), PrimaryIsdn (21), RateAdaptDsl (95), Slip (28), SymmetricDsl (96), TokenRing (9), Tunnel (131), Unknown (1), VeryHighSpeedDsl (97), Wireless80211 (71), Wman (237), Wwanpp (243), Wwanpp2 (244) """
    AsymmetricDsl: NetworkInterfaceType = ...
    Atm: NetworkInterfaceType = ...
    BasicIsdn: NetworkInterfaceType = ...
    Ethernet: NetworkInterfaceType = ...
    Ethernet3Megabit: NetworkInterfaceType = ...
    FastEthernetFx: NetworkInterfaceType = ...
    FastEthernetT: NetworkInterfaceType = ...
    Fddi: NetworkInterfaceType = ...
    GenericModem: NetworkInterfaceType = ...
    GigabitEthernet: NetworkInterfaceType = ...
    HighPerformanceSerialBus: NetworkInterfaceType = ...
    IPOverAtm: NetworkInterfaceType = ...
    Isdn: NetworkInterfaceType = ...
    Loopback: NetworkInterfaceType = ...
    MultiRateSymmetricDsl: NetworkInterfaceType = ...
    Ppp: NetworkInterfaceType = ...
    PrimaryIsdn: NetworkInterfaceType = ...
    RateAdaptDsl: NetworkInterfaceType = ...
    Slip: NetworkInterfaceType = ...
    SymmetricDsl: NetworkInterfaceType = ...
    TokenRing: NetworkInterfaceType = ...
    Tunnel: NetworkInterfaceType = ...
    Unknown: NetworkInterfaceType = ...
    value__ = ...
    VeryHighSpeedDsl: NetworkInterfaceType = ...
    Wireless80211: NetworkInterfaceType = ...
    Wman: NetworkInterfaceType = ...
    Wwanpp: NetworkInterfaceType = ...
    Wwanpp2: NetworkInterfaceType = ...


class OperationalStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationalStatus, values: Dormant (5), Down (2), LowerLayerDown (7), NotPresent (6), Testing (3), Unknown (4), Up (1) """
    Dormant: OperationalStatus = ...
    Down: OperationalStatus = ...
    LowerLayerDown: OperationalStatus = ...
    NotPresent: OperationalStatus = ...
    Testing: OperationalStatus = ...
    Unknown: OperationalStatus = ...
    Up: OperationalStatus = ...
    value__ = ...


class PhysicalAddress: # skipped bases: <type 'object'>, <type 'object'>
    """ PhysicalAddress(address: Array[Byte]) """
    def Equals(self, comparand:object) -> bool:
        """ Equals(self: PhysicalAddress, comparand: object) -> bool """
        ...

    def GetAddressBytes(self) -> Array:
        """ GetAddressBytes(self: PhysicalAddress) -> Array[Byte] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PhysicalAddress) -> int """
        ...

    @staticmethod
    def Parse(address:str) -> PhysicalAddress:
        """ Parse(address: str) -> PhysicalAddress """
        ...

    def ToString(self) -> str:
        """ ToString(self: PhysicalAddress) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Ping(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ Ping() """
    def OnPingCompleted(self, *args): #cannot find CLR method
        """ OnPingCompleted(self: Ping, e: PingCompletedEventArgs) """
        ...

    def Send(self, *__args:str) -> PingReply:
        """
        Send(self: Ping, hostNameOrAddress: str) -> PingReply
        Send(self: Ping, hostNameOrAddress: str, timeout: int) -> PingReply
        Send(self: Ping, address: IPAddress) -> PingReply
        Send(self: Ping, address: IPAddress, timeout: int) -> PingReply
        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> PingReply
        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> PingReply
        Send(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply
        Send(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> PingReply
        """
        ...

    def SendAsync(self, *__args): # -> 
        """ SendAsync(self: Ping, hostNameOrAddress: str, userToken: object)SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, userToken: object)SendAsync(self: Ping, address: IPAddress, userToken: object)SendAsync(self: Ping, address: IPAddress, timeout: int, userToken: object)SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], userToken: object)SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], userToken: object)SendAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object)SendAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions, userToken: object) """
        ...

    def SendAsyncCancel(self): # -> 
        """ SendAsyncCancel(self: Ping) """
        ...

    def SendPingAsync(self, *__args:IPAddress) -> Task:
        """
        SendPingAsync(self: Ping, address: IPAddress) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte]) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte]) -> Task[PingReply]
        SendPingAsync(self: Ping, address: IPAddress, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]
        SendPingAsync(self: Ping, hostNameOrAddress: str, timeout: int, buffer: Array[Byte], options: PingOptions) -> Task[PingReply]
        """
        ...

    PingCompleted = ...


class PingCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Reply(self) -> PingReply:
        """ Get: Reply(self: PingCompletedEventArgs) -> PingReply """
        ...



class PingCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PingCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PingCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PingCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PingCompletedEventArgs): # -> 
        """ Invoke(self: PingCompletedEventHandler, sender: object, e: PingCompletedEventArgs) """
        ...


class PingException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PingException(message: str)
    PingException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PingOptions: # skipped bases: <type 'object'>, <type 'object'>
    """
    PingOptions(ttl: int, dontFragment: bool)
    PingOptions()
    """
    @property
    def DontFragment(self) -> bool:
        """
        Get: DontFragment(self: PingOptions) -> bool
        Set: DontFragment(self: PingOptions) = value
        """
        ...

    @property
    def Ttl(self) -> int:
        """
        Get: Ttl(self: PingOptions) -> int
        Set: Ttl(self: PingOptions) = value
        """
        ...



class PingReply: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Address(self) -> IPAddress:
        """ Get: Address(self: PingReply) -> IPAddress """
        ...

    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: PingReply) -> Array[Byte] """
        ...

    @property
    def Options(self) -> PingOptions:
        """ Get: Options(self: PingReply) -> PingOptions """
        ...

    @property
    def RoundtripTime(self) -> Int64:
        """ Get: RoundtripTime(self: PingReply) -> Int64 """
        ...

    @property
    def Status(self) -> IPStatus:
        """ Get: Status(self: PingReply) -> IPStatus """
        ...



class PrefixOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrefixOrigin, values: Dhcp (3), Manual (1), Other (0), RouterAdvertisement (4), WellKnown (2) """
    Dhcp: PrefixOrigin = ...
    Manual: PrefixOrigin = ...
    Other: PrefixOrigin = ...
    RouterAdvertisement: PrefixOrigin = ...
    value__ = ...
    WellKnown: PrefixOrigin = ...


class ScopeLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ScopeLevel, values: Admin (4), Global (14), Interface (1), Link (2), None (0), Organization (8), Site (5), Subnet (3) """
    Admin: ScopeLevel = ...
    Global: ScopeLevel = ...
    Interface: ScopeLevel = ...
    Link: ScopeLevel = ...
    Organization: ScopeLevel = ...
    Site: ScopeLevel = ...
    Subnet: ScopeLevel = ...
    value__ = ...


class SuffixOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SuffixOrigin, values: LinkLayerAddress (4), Manual (1), OriginDhcp (3), Other (0), Random (5), WellKnown (2) """
    LinkLayerAddress: SuffixOrigin = ...
    Manual: SuffixOrigin = ...
    OriginDhcp: SuffixOrigin = ...
    Other: SuffixOrigin = ...
    Random: SuffixOrigin = ...
    value__ = ...
    WellKnown: SuffixOrigin = ...


class TcpConnectionInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """ Get: LocalEndPoint(self: TcpConnectionInformation) -> IPEndPoint """
        ...

    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """ Get: RemoteEndPoint(self: TcpConnectionInformation) -> IPEndPoint """
        ...

    @property
    def State(self) -> TcpState:
        """ Get: State(self: TcpConnectionInformation) -> TcpState """
        ...



class TcpState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TcpState, values: Closed (1), CloseWait (8), Closing (9), DeleteTcb (12), Established (5), FinWait1 (6), FinWait2 (7), LastAck (10), Listen (2), SynReceived (4), SynSent (3), TimeWait (11), Unknown (0) """
    Closed: TcpState = ...
    CloseWait: TcpState = ...
    Closing: TcpState = ...
    DeleteTcb: TcpState = ...
    Established: TcpState = ...
    FinWait1: TcpState = ...
    FinWait2: TcpState = ...
    LastAck: TcpState = ...
    Listen: TcpState = ...
    SynReceived: TcpState = ...
    SynSent: TcpState = ...
    TimeWait: TcpState = ...
    Unknown: TcpState = ...
    value__ = ...


class TcpStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConnectionsAccepted(self) -> Int64:
        """ Get: ConnectionsAccepted(self: TcpStatistics) -> Int64 """
        ...

    @property
    def ConnectionsInitiated(self) -> Int64:
        """ Get: ConnectionsInitiated(self: TcpStatistics) -> Int64 """
        ...

    @property
    def CumulativeConnections(self) -> Int64:
        """ Get: CumulativeConnections(self: TcpStatistics) -> Int64 """
        ...

    @property
    def CurrentConnections(self) -> Int64:
        """ Get: CurrentConnections(self: TcpStatistics) -> Int64 """
        ...

    @property
    def ErrorsReceived(self) -> Int64:
        """ Get: ErrorsReceived(self: TcpStatistics) -> Int64 """
        ...

    @property
    def FailedConnectionAttempts(self) -> Int64:
        """ Get: FailedConnectionAttempts(self: TcpStatistics) -> Int64 """
        ...

    @property
    def MaximumConnections(self) -> Int64:
        """ Get: MaximumConnections(self: TcpStatistics) -> Int64 """
        ...

    @property
    def MaximumTransmissionTimeout(self) -> Int64:
        """ Get: MaximumTransmissionTimeout(self: TcpStatistics) -> Int64 """
        ...

    @property
    def MinimumTransmissionTimeout(self) -> Int64:
        """ Get: MinimumTransmissionTimeout(self: TcpStatistics) -> Int64 """
        ...

    @property
    def ResetConnections(self) -> Int64:
        """ Get: ResetConnections(self: TcpStatistics) -> Int64 """
        ...

    @property
    def ResetsSent(self) -> Int64:
        """ Get: ResetsSent(self: TcpStatistics) -> Int64 """
        ...

    @property
    def SegmentsReceived(self) -> Int64:
        """ Get: SegmentsReceived(self: TcpStatistics) -> Int64 """
        ...

    @property
    def SegmentsResent(self) -> Int64:
        """ Get: SegmentsResent(self: TcpStatistics) -> Int64 """
        ...

    @property
    def SegmentsSent(self) -> Int64:
        """ Get: SegmentsSent(self: TcpStatistics) -> Int64 """
        ...



class UdpStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DatagramsReceived(self) -> Int64:
        """ Get: DatagramsReceived(self: UdpStatistics) -> Int64 """
        ...

    @property
    def DatagramsSent(self) -> Int64:
        """ Get: DatagramsSent(self: UdpStatistics) -> Int64 """
        ...

    @property
    def IncomingDatagramsDiscarded(self) -> Int64:
        """ Get: IncomingDatagramsDiscarded(self: UdpStatistics) -> Int64 """
        ...

    @property
    def IncomingDatagramsWithErrors(self) -> Int64:
        """ Get: IncomingDatagramsWithErrors(self: UdpStatistics) -> Int64 """
        ...

    @property
    def UdpListeners(self) -> int:
        """ Get: UdpListeners(self: UdpStatistics) -> int """
        ...



class UnicastIPAddressInformation(IPAddressInformation): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AddressPreferredLifetime(self) -> Int64:
        """ Get: AddressPreferredLifetime(self: UnicastIPAddressInformation) -> Int64 """
        ...

    @property
    def AddressValidLifetime(self) -> Int64:
        """ Get: AddressValidLifetime(self: UnicastIPAddressInformation) -> Int64 """
        ...

    @property
    def DhcpLeaseLifetime(self) -> Int64:
        """ Get: DhcpLeaseLifetime(self: UnicastIPAddressInformation) -> Int64 """
        ...

    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """ Get: DuplicateAddressDetectionState(self: UnicastIPAddressInformation) -> DuplicateAddressDetectionState """
        ...

    @property
    def IPv4Mask(self) -> IPAddress:
        """ Get: IPv4Mask(self: UnicastIPAddressInformation) -> IPAddress """
        ...

    @property
    def PrefixLength(self) -> int:
        """ Get: PrefixLength(self: UnicastIPAddressInformation) -> int """
        ...

    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """ Get: PrefixOrigin(self: UnicastIPAddressInformation) -> PrefixOrigin """
        ...

    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """ Get: SuffixOrigin(self: UnicastIPAddressInformation) -> SuffixOrigin """
        ...



class UnicastIPAddressInformationCollection(ICollection): # skipped bases: <type 'IEnumerable[UnicastIPAddressInformation]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: UnicastIPAddressInformationCollection) -> IEnumerator[UnicastIPAddressInformation] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


