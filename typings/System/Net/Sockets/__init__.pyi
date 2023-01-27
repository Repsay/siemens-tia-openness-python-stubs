# encoding: utf-8
# module System.Net.Sockets calls itself Sockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Net, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, ArraySegment, AsyncCallback, Enum, EventArgs, 
    IAsyncResult, IDisposable, IEquatable, Int16, Int64, IntPtr, 
    MulticastDelegate)

from System.Collections import IList

from System.ComponentModel import Win32Exception

from System.IO import Stream

from System.Net import (EndPoint, IPAddress, IPEndPoint, 
    IUnsafeWebRequestCreate)

from System.Threading.Tasks import Task

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    SecurityCriticalAction, SocketPolicy, field#)
"""

# no functions
# classes

class AddressFamily(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AddressFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18) """
    AppleTalk: AddressFamily = ...
    Atm: AddressFamily = ...
    Banyan: AddressFamily = ...
    Ccitt: AddressFamily = ...
    Chaos: AddressFamily = ...
    Cluster: AddressFamily = ...
    DataKit: AddressFamily = ...
    DataLink: AddressFamily = ...
    DecNet: AddressFamily = ...
    Ecma: AddressFamily = ...
    FireFox: AddressFamily = ...
    HyperChannel: AddressFamily = ...
    Ieee12844: AddressFamily = ...
    ImpLink: AddressFamily = ...
    InterNetwork: AddressFamily = ...
    InterNetworkV6: AddressFamily = ...
    Ipx: AddressFamily = ...
    Irda: AddressFamily = ...
    Iso: AddressFamily = ...
    Lat: AddressFamily = ...
    Max: AddressFamily = ...
    NetBios: AddressFamily = ...
    NetworkDesigners: AddressFamily = ...
    NS: AddressFamily = ...
    Osi: AddressFamily = ...
    Pup: AddressFamily = ...
    Sna: AddressFamily = ...
    Unix: AddressFamily = ...
    Unknown: AddressFamily = ...
    Unspecified: AddressFamily = ...
    value__ = ...
    VoiceView: AddressFamily = ...


class HttpPolicyDownloaderProtocol: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpPolicyDownloaderProtocol(appUri: Uri, address: IPAddress) """
    @property
    def Result(self): # -> SocketPolicy
        """ Get: Result(self: HttpPolicyDownloaderProtocol) -> SocketPolicy """
        ...


    def Abort(self): # -> 
        """ Abort(self: HttpPolicyDownloaderProtocol) """
        ...

    def BeginDownload(self, callback): # ->  # Not found arg types: {'callback': 'SecurityCriticalAction'}
        """ BeginDownload(self: HttpPolicyDownloaderProtocol, callback: SecurityCriticalAction) """
        ...

    def DownloadCallback(self, ar:IAsyncResult): # -> 
        """ DownloadCallback(self: HttpPolicyDownloaderProtocol, ar: IAsyncResult) """
        ...

    def ReadCallback(self, ar:IAsyncResult): # -> 
        """ ReadCallback(self: HttpPolicyDownloaderProtocol, ar: IAsyncResult) """
        ...

    @staticmethod
    def RegisterUnsafeWebRequestCreator(creator:IUnsafeWebRequestCreate): # -> 
        """ RegisterUnsafeWebRequestCreator(creator: IUnsafeWebRequestCreate) """
        ...


class IOControlCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IOControlCode, values: AbsorbRouterAlert (2550136837), AddMulticastGroupOnInterface (2550136842), AddressListChange (671088663), AddressListQuery (1207959574), AddressListSort (3355443225), AssociateHandle (2281701377), AsyncIO (2147772029), BindToInterface (2550136840), DataToRead (1074030207), DeleteMulticastGroupFromInterface (2550136843), EnableCircularQueuing (671088642), Flush (671088644), GetBroadcastAddress (1207959557), GetExtensionFunctionPointer (3355443206), GetGroupQos (3355443208), GetQos (3355443207), KeepAliveValues (2550136836), LimitBroadcasts (2550136839), MulticastInterface (2550136841), MulticastScope (2281701386), MultipointLoopback (2281701385), NamespaceChange (2281701401), NonBlockingIO (2147772030), OobDataRead (1074033415), QueryTargetPnpHandle (1207959576), ReceiveAll (2550136833), ReceiveAllIgmpMulticast (2550136835), ReceiveAllMulticast (2550136834), RoutingInterfaceChange (2281701397), RoutingInterfaceQuery (3355443220), SetGroupQos (2281701388), SetQos (2281701387), TranslateHandle (3355443213), UnicastInterface (2550136838) """
    AbsorbRouterAlert: IOControlCode = ...
    AddMulticastGroupOnInterface: IOControlCode = ...
    AddressListChange: IOControlCode = ...
    AddressListQuery: IOControlCode = ...
    AddressListSort: IOControlCode = ...
    AssociateHandle: IOControlCode = ...
    AsyncIO: IOControlCode = ...
    BindToInterface: IOControlCode = ...
    DataToRead: IOControlCode = ...
    DeleteMulticastGroupFromInterface: IOControlCode = ...
    EnableCircularQueuing: IOControlCode = ...
    Flush: IOControlCode = ...
    GetBroadcastAddress: IOControlCode = ...
    GetExtensionFunctionPointer: IOControlCode = ...
    GetGroupQos: IOControlCode = ...
    GetQos: IOControlCode = ...
    KeepAliveValues: IOControlCode = ...
    LimitBroadcasts: IOControlCode = ...
    MulticastInterface: IOControlCode = ...
    MulticastScope: IOControlCode = ...
    MultipointLoopback: IOControlCode = ...
    NamespaceChange: IOControlCode = ...
    NonBlockingIO: IOControlCode = ...
    OobDataRead: IOControlCode = ...
    QueryTargetPnpHandle: IOControlCode = ...
    ReceiveAll: IOControlCode = ...
    ReceiveAllIgmpMulticast: IOControlCode = ...
    ReceiveAllMulticast: IOControlCode = ...
    RoutingInterfaceChange: IOControlCode = ...
    RoutingInterfaceQuery: IOControlCode = ...
    SetGroupQos: IOControlCode = ...
    SetQos: IOControlCode = ...
    TranslateHandle: IOControlCode = ...
    UnicastInterface: IOControlCode = ...
    value__ = ...


class IPPacketInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Address(self) -> IPAddress:
        """ Get: Address(self: IPPacketInformation) -> IPAddress """
        ...

    @property
    def Interface(self) -> int:
        """ Get: Interface(self: IPPacketInformation) -> int """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: IPPacketInformation, comparand: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: IPPacketInformation) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IPProtectionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IPProtectionLevel, values: EdgeRestricted (20), Restricted (30), Unrestricted (10), Unspecified (-1) """
    EdgeRestricted: IPProtectionLevel = ...
    Restricted: IPProtectionLevel = ...
    Unrestricted: IPProtectionLevel = ...
    Unspecified: IPProtectionLevel = ...
    value__ = ...


class IPv6MulticastOption: # skipped bases: <type 'object'>, <type 'object'>
    """
    IPv6MulticastOption(group: IPAddress, ifindex: Int64)
    IPv6MulticastOption(group: IPAddress)
    """
    @property
    def Group(self) -> IPAddress:
        """
        Get: Group(self: IPv6MulticastOption) -> IPAddress
        Set: Group(self: IPv6MulticastOption) = value
        """
        ...

    @property
    def InterfaceIndex(self) -> Int64:
        """
        Get: InterfaceIndex(self: IPv6MulticastOption) -> Int64
        Set: InterfaceIndex(self: IPv6MulticastOption) = value
        """
        ...



class LingerOption: # skipped bases: <type 'object'>, <type 'object'>
    """ LingerOption(enable: bool, seconds: int) """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: LingerOption) -> bool
        Set: Enabled(self: LingerOption) = value
        """
        ...

    @property
    def LingerTime(self) -> int:
        """
        Get: LingerTime(self: LingerOption) -> int
        Set: LingerTime(self: LingerOption) = value
        """
        ...



class MulticastOption: # skipped bases: <type 'object'>, <type 'object'>
    """
    MulticastOption(group: IPAddress, mcint: IPAddress)
    MulticastOption(group: IPAddress, interfaceIndex: int)
    MulticastOption(group: IPAddress)
    """
    @property
    def Group(self) -> IPAddress:
        """
        Get: Group(self: MulticastOption) -> IPAddress
        Set: Group(self: MulticastOption) = value
        """
        ...

    @property
    def InterfaceIndex(self) -> int:
        """
        Get: InterfaceIndex(self: MulticastOption) -> int
        Set: InterfaceIndex(self: MulticastOption) = value
        """
        ...

    @property
    def LocalAddress(self) -> IPAddress:
        """
        Get: LocalAddress(self: MulticastOption) -> IPAddress
        Set: LocalAddress(self: MulticastOption) = value
        """
        ...



class NetworkStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    NetworkStream(socket: Socket)
    NetworkStream(socket: Socket, ownsSocket: bool)
    NetworkStream(socket: Socket, access: FileAccess)
    NetworkStream(socket: Socket, access: FileAccess, ownsSocket: bool)
    """
    @property
    def DataAvailable(self) -> bool:
        """ Get: DataAvailable(self: NetworkStream) -> bool """
        ...

    @property
    def Readable(self):
        ...

    @property
    def Socket(self):
        ...

    @property
    def Writeable(self):
        ...


    def __new__(cls, socket:Socket, *__args:bool) -> Self:
        """
        __new__(cls: type, socket: Socket)
        __new__(cls: type, socket: Socket, ownsSocket: bool)
        __new__(cls: type, socket: Socket, access: FileAccess)
        __new__(cls: type, socket: Socket, access: FileAccess, ownsSocket: bool)
        """
        ...


class ProtocolFamily(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProtocolFamily, values: AppleTalk (16), Atm (22), Banyan (21), Ccitt (10), Chaos (5), Cluster (24), DataKit (9), DataLink (13), DecNet (12), Ecma (8), FireFox (19), HyperChannel (15), Ieee12844 (25), ImpLink (3), InterNetwork (2), InterNetworkV6 (23), Ipx (6), Irda (26), Iso (7), Lat (14), Max (29), NetBios (17), NetworkDesigners (28), NS (6), Osi (7), Pup (4), Sna (11), Unix (1), Unknown (-1), Unspecified (0), VoiceView (18) """
    AppleTalk: ProtocolFamily = ...
    Atm: ProtocolFamily = ...
    Banyan: ProtocolFamily = ...
    Ccitt: ProtocolFamily = ...
    Chaos: ProtocolFamily = ...
    Cluster: ProtocolFamily = ...
    DataKit: ProtocolFamily = ...
    DataLink: ProtocolFamily = ...
    DecNet: ProtocolFamily = ...
    Ecma: ProtocolFamily = ...
    FireFox: ProtocolFamily = ...
    HyperChannel: ProtocolFamily = ...
    Ieee12844: ProtocolFamily = ...
    ImpLink: ProtocolFamily = ...
    InterNetwork: ProtocolFamily = ...
    InterNetworkV6: ProtocolFamily = ...
    Ipx: ProtocolFamily = ...
    Irda: ProtocolFamily = ...
    Iso: ProtocolFamily = ...
    Lat: ProtocolFamily = ...
    Max: ProtocolFamily = ...
    NetBios: ProtocolFamily = ...
    NetworkDesigners: ProtocolFamily = ...
    NS: ProtocolFamily = ...
    Osi: ProtocolFamily = ...
    Pup: ProtocolFamily = ...
    Sna: ProtocolFamily = ...
    Unix: ProtocolFamily = ...
    Unknown: ProtocolFamily = ...
    Unspecified: ProtocolFamily = ...
    value__ = ...
    VoiceView: ProtocolFamily = ...


class ProtocolType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProtocolType, values: Ggp (3), Icmp (1), IcmpV6 (58), Idp (22), Igmp (2), IP (0), IPSecAuthenticationHeader (51), IPSecEncapsulatingSecurityPayload (50), IPv4 (4), IPv6 (41), IPv6DestinationOptions (60), IPv6FragmentHeader (44), IPv6HopByHopOptions (0), IPv6NoNextHeader (59), IPv6RoutingHeader (43), Ipx (1000), ND (77), Pup (12), Raw (255), Spx (1256), SpxII (1257), Tcp (6), Udp (17), Unknown (-1), Unspecified (0) """
    Ggp: ProtocolType = ...
    Icmp: ProtocolType = ...
    IcmpV6: ProtocolType = ...
    Idp: ProtocolType = ...
    Igmp: ProtocolType = ...
    IP: ProtocolType = ...
    IPSecAuthenticationHeader: ProtocolType = ...
    IPSecEncapsulatingSecurityPayload: ProtocolType = ...
    IPv4: ProtocolType = ...
    IPv6: ProtocolType = ...
    IPv6DestinationOptions: ProtocolType = ...
    IPv6FragmentHeader: ProtocolType = ...
    IPv6HopByHopOptions: ProtocolType = ...
    IPv6NoNextHeader: ProtocolType = ...
    IPv6RoutingHeader: ProtocolType = ...
    Ipx: ProtocolType = ...
    ND: ProtocolType = ...
    Pup: ProtocolType = ...
    Raw: ProtocolType = ...
    Spx: ProtocolType = ...
    SpxII: ProtocolType = ...
    Tcp: ProtocolType = ...
    Udp: ProtocolType = ...
    Unknown: ProtocolType = ...
    Unspecified: ProtocolType = ...
    value__ = ...


class SecurityCriticalAction(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SecurityCriticalAction(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SecurityCriticalAction, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SecurityCriticalAction, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: SecurityCriticalAction) """
        ...


class SelectMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SelectMode, values: SelectError (2), SelectRead (0), SelectWrite (1) """
    SelectError: SelectMode = ...
    SelectRead: SelectMode = ...
    SelectWrite: SelectMode = ...
    value__ = ...


class SendPacketsElement: # skipped bases: <type 'object'>, <type 'object'>
    """
    SendPacketsElement(filepath: str)
    SendPacketsElement(filepath: str, offset: int, count: int)
    SendPacketsElement(filepath: str, offset: int, count: int, endOfPacket: bool)
    SendPacketsElement(buffer: Array[Byte])
    SendPacketsElement(buffer: Array[Byte], offset: int, count: int)
    SendPacketsElement(buffer: Array[Byte], offset: int, count: int, endOfPacket: bool)
    """
    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: SendPacketsElement) -> Array[Byte] """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SendPacketsElement) -> int """
        ...

    @property
    def EndOfPacket(self) -> bool:
        """ Get: EndOfPacket(self: SendPacketsElement) -> bool """
        ...

    @property
    def FilePath(self) -> str:
        """ Get: FilePath(self: SendPacketsElement) -> str """
        ...

    @property
    def Offset(self) -> int:
        """ Get: Offset(self: SendPacketsElement) -> int """
        ...



class Socket(IDisposable): # skipped bases: <type 'object'>
    """
    Socket(socketType: SocketType, protocolType: ProtocolType)
    Socket(addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType)
    Socket(socketInformation: SocketInformation)
    """
    @property
    def AddressFamily(self) -> AddressFamily:
        """ Get: AddressFamily(self: Socket) -> AddressFamily """
        ...

    @property
    def Available(self) -> int:
        """ Get: Available(self: Socket) -> int """
        ...

    @property
    def Blocking(self) -> bool:
        """
        Get: Blocking(self: Socket) -> bool
        Set: Blocking(self: Socket) = value
        """
        ...

    @property
    def Connected(self) -> bool:
        """ Get: Connected(self: Socket) -> bool """
        ...

    @property
    def DontFragment(self) -> bool:
        """
        Get: DontFragment(self: Socket) -> bool
        Set: DontFragment(self: Socket) = value
        """
        ...

    @property
    def DualMode(self) -> bool:
        """
        Get: DualMode(self: Socket) -> bool
        Set: DualMode(self: Socket) = value
        """
        ...

    @property
    def EnableBroadcast(self) -> bool:
        """
        Get: EnableBroadcast(self: Socket) -> bool
        Set: EnableBroadcast(self: Socket) = value
        """
        ...

    @property
    def ExclusiveAddressUse(self) -> bool:
        """
        Get: ExclusiveAddressUse(self: Socket) -> bool
        Set: ExclusiveAddressUse(self: Socket) = value
        """
        ...

    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: Socket) -> IntPtr """
        ...

    @property
    def IsBound(self) -> bool:
        """ Get: IsBound(self: Socket) -> bool """
        ...

    @property
    def LingerState(self) -> LingerOption:
        """
        Get: LingerState(self: Socket) -> LingerOption
        Set: LingerState(self: Socket) = value
        """
        ...

    @property
    def LocalEndPoint(self) -> EndPoint:
        """ Get: LocalEndPoint(self: Socket) -> EndPoint """
        ...

    @property
    def MulticastLoopback(self) -> bool:
        """
        Get: MulticastLoopback(self: Socket) -> bool
        Set: MulticastLoopback(self: Socket) = value
        """
        ...

    @property
    def NoDelay(self) -> bool:
        """
        Get: NoDelay(self: Socket) -> bool
        Set: NoDelay(self: Socket) = value
        """
        ...

    @property
    def OSSupportsIPv4(self) -> bool:
        """ Get: OSSupportsIPv4() -> bool """
        ...

    @property
    def OSSupportsIPv6(self) -> bool:
        """ Get: OSSupportsIPv6() -> bool """
        ...

    @property
    def ProtocolType(self) -> ProtocolType:
        """ Get: ProtocolType(self: Socket) -> ProtocolType """
        ...

    @property
    def ReceiveBufferSize(self) -> int:
        """
        Get: ReceiveBufferSize(self: Socket) -> int
        Set: ReceiveBufferSize(self: Socket) = value
        """
        ...

    @property
    def ReceiveTimeout(self) -> int:
        """
        Get: ReceiveTimeout(self: Socket) -> int
        Set: ReceiveTimeout(self: Socket) = value
        """
        ...

    @property
    def RemoteEndPoint(self) -> EndPoint:
        """ Get: RemoteEndPoint(self: Socket) -> EndPoint """
        ...

    @property
    def SendBufferSize(self) -> int:
        """
        Get: SendBufferSize(self: Socket) -> int
        Set: SendBufferSize(self: Socket) = value
        """
        ...

    @property
    def SendTimeout(self) -> int:
        """
        Get: SendTimeout(self: Socket) -> int
        Set: SendTimeout(self: Socket) = value
        """
        ...

    @property
    def SocketType(self) -> SocketType:
        """ Get: SocketType(self: Socket) -> SocketType """
        ...

    @property
    def SupportsIPv4(self) -> bool:
        """ Get: SupportsIPv4() -> bool """
        ...

    @property
    def SupportsIPv6(self) -> bool:
        """ Get: SupportsIPv6() -> bool """
        ...

    @property
    def Ttl(self) -> Int16:
        """
        Get: Ttl(self: Socket) -> Int16
        Set: Ttl(self: Socket) = value
        """
        ...

    @property
    def UseOnlyOverlappedIO(self) -> bool:
        """
        Get: UseOnlyOverlappedIO(self: Socket) -> bool
        Set: UseOnlyOverlappedIO(self: Socket) = value
        """
        ...


    def Accept(self) -> Socket:
        """ Accept(self: Socket) -> Socket """
        ...

    def AcceptAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ AcceptAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def BeginAccept(self, *__args) -> IAsyncResult:
        """
        BeginAccept(self: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAccept(self: Socket, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAccept(self: Socket, acceptSocket: Socket, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginConnect(self, *__args) -> IAsyncResult:
        """
        BeginConnect(self: Socket, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginConnect(self: Socket, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginConnect(self: Socket, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginConnect(self: Socket, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginDisconnect(self, reuseSocket:bool, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginDisconnect(self: Socket, reuseSocket: bool, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginReceive(self, *__args) -> IAsyncResult:
        """
        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReceive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        BeginReceive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        """
        ...

    def BeginReceiveFrom(self, buffer:Array, offset:int, size:int, socketFlags:SocketFlags, remoteEP:EndPoint, callback:AsyncCallback, state:object) -> Tuple_[IAsyncResult, EndPoint]:
        """ BeginReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint) """
        ...

    def BeginReceiveMessageFrom(self, buffer:Array, offset:int, size:int, socketFlags:SocketFlags, remoteEP:EndPoint, callback:AsyncCallback, state:object) -> Tuple_[IAsyncResult, EndPoint]:
        """ BeginReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> (IAsyncResult, EndPoint) """
        ...

    def BeginSend(self, *__args) -> IAsyncResult:
        """
        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        BeginSend(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, callback: AsyncCallback, state: object) -> (IAsyncResult, SocketError)
        """
        ...

    def BeginSendFile(self, fileName, *__args) -> IAsyncResult:
        """
        BeginSendFile(self: Socket, fileName: str, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginSendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginSendTo(self, buffer:Array, offset:int, size:int, socketFlags:SocketFlags, remoteEP:EndPoint, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Bind(self, localEP:EndPoint): # -> 
        """ Bind(self: Socket, localEP: EndPoint) """
        ...

    @staticmethod
    def CancelConnectAsync(e:SocketAsyncEventArgs): # -> 
        """ CancelConnectAsync(e: SocketAsyncEventArgs) """
        ...

    def Close(self, timeout:int = ...): # -> 
        """ Close(self: Socket, timeout: int)Close(self: Socket) """
        ...

    def Connect(self, *__args:EndPoint): # -> 
        """ Connect(self: Socket, remoteEP: EndPoint)Connect(self: Socket, address: IPAddress, port: int)Connect(self: Socket, host: str, port: int)Connect(self: Socket, addresses: Array[IPAddress], port: int) """
        ...

    def ConnectAsync(self, *__args:SocketAsyncEventArgs) -> bool:
        """
        ConnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool
        ConnectAsync(socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs) -> bool
        """
        ...

    def Disconnect(self, reuseSocket:bool): # -> 
        """ Disconnect(self: Socket, reuseSocket: bool) """
        ...

    def DisconnectAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ DisconnectAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def DuplicateAndClose(self, targetProcessId:int) -> SocketInformation:
        """ DuplicateAndClose(self: Socket, targetProcessId: int) -> SocketInformation """
        ...

    def EndAccept(self, *__args:IAsyncResult) -> Socket:
        """
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> Socket
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte])
        EndAccept(self: Socket, asyncResult: IAsyncResult) -> (Socket, Array[Byte], int)
        """
        ...

    def EndConnect(self, asyncResult:IAsyncResult): # -> 
        """ EndConnect(self: Socket, asyncResult: IAsyncResult) """
        ...

    def EndDisconnect(self, asyncResult:IAsyncResult): # -> 
        """ EndDisconnect(self: Socket, asyncResult: IAsyncResult) """
        ...

    def EndReceive(self, asyncResult, errorCode=None) -> int:
        """
        EndReceive(self: Socket, asyncResult: IAsyncResult) -> int
        EndReceive(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)
        """
        ...

    def EndReceiveFrom(self, asyncResult:IAsyncResult, endPoint:EndPoint) -> Tuple_[int, EndPoint]:
        """ EndReceiveFrom(self: Socket, asyncResult: IAsyncResult, endPoint: EndPoint) -> (int, EndPoint) """
        ...

    def EndReceiveMessageFrom(self, asyncResult, socketFlags, endPoint, ipPacketInformation) -> Tuple_[int, SocketFlags, EndPoint, IPPacketInformation]:
        """ EndReceiveMessageFrom(self: Socket, asyncResult: IAsyncResult, socketFlags: SocketFlags, endPoint: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation) """
        ...

    def EndSend(self, asyncResult, errorCode=None) -> int:
        """
        EndSend(self: Socket, asyncResult: IAsyncResult) -> int
        EndSend(self: Socket, asyncResult: IAsyncResult) -> (int, SocketError)
        """
        ...

    def EndSendFile(self, asyncResult:IAsyncResult): # -> 
        """ EndSendFile(self: Socket, asyncResult: IAsyncResult) """
        ...

    def EndSendTo(self, asyncResult:IAsyncResult) -> int:
        """ EndSendTo(self: Socket, asyncResult: IAsyncResult) -> int """
        ...

    def GetSocketOption(self, optionLevel:SocketOptionLevel, optionName:SocketOptionName, *__args:Array): # -> 
        """
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName) -> object
        GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])GetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int) -> Array[Byte]
        """
        ...

    def IOControl(self, ioControlCode:IOControlCode, optionInValue:Array, optionOutValue:Array) -> int:
        """
        IOControl(self: Socket, ioControlCode: IOControlCode, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int
        IOControl(self: Socket, ioControlCode: int, optionInValue: Array[Byte], optionOutValue: Array[Byte]) -> int
        """
        ...

    def Listen(self, backlog:int): # -> 
        """ Listen(self: Socket, backlog: int) """
        ...

    def Poll(self, microSeconds:int, mode:SelectMode) -> bool:
        """ Poll(self: Socket, microSeconds: int, mode: SelectMode) -> bool """
        ...

    def Receive(self, *__args:Array) -> int:
        """
        Receive(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int
        Receive(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int
        Receive(self: Socket, buffer: Array[Byte]) -> int
        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int
        Receive(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)
        Receive(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)
        """
        ...

    def ReceiveAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ ReceiveAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def ReceiveFrom(self, buffer:Array, *__args:EndPoint) -> Tuple_[int, EndPoint]:
        """
        ReceiveFrom(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        ReceiveFrom(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        ReceiveFrom(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> (int, EndPoint)
        ReceiveFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, EndPoint)
        """
        ...

    def ReceiveFromAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ ReceiveFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def ReceiveMessageFrom(self, buffer, offset, size, socketFlags, remoteEP, ipPacketInformation) -> Tuple_[int, SocketFlags, EndPoint, IPPacketInformation]:
        """ ReceiveMessageFrom(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> (int, SocketFlags, EndPoint, IPPacketInformation) """
        ...

    def ReceiveMessageFromAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ ReceiveMessageFromAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    @staticmethod
    def Select(checkRead:IList, checkWrite:IList, checkError:IList, microSeconds:int): # -> 
        """ Select(checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: int) """
        ...

    def Send(self, *__args:Array) -> int:
        """
        Send(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags) -> int
        Send(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags) -> int
        Send(self: Socket, buffer: Array[Byte]) -> int
        Send(self: Socket, buffers: IList[ArraySegment[Byte]]) -> int
        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> int
        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> int
        Send(self: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> (int, SocketError)
        Send(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags) -> (int, SocketError)
        """
        ...

    def SendAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ SendAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def SendFile(self, fileName:str, preBuffer:Array = ..., postBuffer:Array = ..., flags:TransmitFileOptions = ...): # -> 
        """ SendFile(self: Socket, fileName: str)SendFile(self: Socket, fileName: str, preBuffer: Array[Byte], postBuffer: Array[Byte], flags: TransmitFileOptions) """
        ...

    def SendPacketsAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ SendPacketsAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def SendTo(self, buffer:Array, *__args:EndPoint) -> int:
        """
        SendTo(self: Socket, buffer: Array[Byte], size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        SendTo(self: Socket, buffer: Array[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        SendTo(self: Socket, buffer: Array[Byte], remoteEP: EndPoint) -> int
        SendTo(self: Socket, buffer: Array[Byte], offset: int, size: int, socketFlags: SocketFlags, remoteEP: EndPoint) -> int
        """
        ...

    def SendToAsync(self, e:SocketAsyncEventArgs) -> bool:
        """ SendToAsync(self: Socket, e: SocketAsyncEventArgs) -> bool """
        ...

    def SetIPProtectionLevel(self, level:IPProtectionLevel): # -> 
        """ SetIPProtectionLevel(self: Socket, level: IPProtectionLevel) """
        ...

    def SetSocketOption(self, optionLevel:SocketOptionLevel, optionName:SocketOptionName, optionValue:int): # -> 
        """ SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int)SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool)SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[Byte])SetSocketOption(self: Socket, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object) """
        ...

    def Shutdown(self, how:SocketShutdown): # -> 
        """ Shutdown(self: Socket, how: SocketShutdown) """
        ...



class SocketAsyncEventArgs(IDisposable, EventArgs): # skipped bases: <type 'object'>
    """ SocketAsyncEventArgs() """
    @property
    def AcceptSocket(self) -> Socket:
        """
        Get: AcceptSocket(self: SocketAsyncEventArgs) -> Socket
        Set: AcceptSocket(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: SocketAsyncEventArgs) -> Array[Byte] """
        ...

    @property
    def BufferList(self) -> IList:
        """
        Get: BufferList(self: SocketAsyncEventArgs) -> IList[ArraySegment[Byte]]
        Set: BufferList(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def BytesTransferred(self) -> int:
        """ Get: BytesTransferred(self: SocketAsyncEventArgs) -> int """
        ...

    @property
    def ConnectByNameError(self) -> Exception:
        """ Get: ConnectByNameError(self: SocketAsyncEventArgs) -> Exception """
        ...

    @property
    def ConnectSocket(self) -> Socket:
        """ Get: ConnectSocket(self: SocketAsyncEventArgs) -> Socket """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SocketAsyncEventArgs) -> int """
        ...

    @property
    def DisconnectReuseSocket(self) -> bool:
        """
        Get: DisconnectReuseSocket(self: SocketAsyncEventArgs) -> bool
        Set: DisconnectReuseSocket(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def LastOperation(self) -> SocketAsyncOperation:
        """ Get: LastOperation(self: SocketAsyncEventArgs) -> SocketAsyncOperation """
        ...

    @property
    def Offset(self) -> int:
        """ Get: Offset(self: SocketAsyncEventArgs) -> int """
        ...

    @property
    def ReceiveMessageFromPacketInfo(self) -> IPPacketInformation:
        """ Get: ReceiveMessageFromPacketInfo(self: SocketAsyncEventArgs) -> IPPacketInformation """
        ...

    @property
    def RemoteEndPoint(self) -> EndPoint:
        """
        Get: RemoteEndPoint(self: SocketAsyncEventArgs) -> EndPoint
        Set: RemoteEndPoint(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SendPacketsElements(self) -> Array:
        """
        Get: SendPacketsElements(self: SocketAsyncEventArgs) -> Array[SendPacketsElement]
        Set: SendPacketsElements(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SendPacketsFlags(self) -> TransmitFileOptions:
        """
        Get: SendPacketsFlags(self: SocketAsyncEventArgs) -> TransmitFileOptions
        Set: SendPacketsFlags(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SendPacketsSendSize(self) -> int:
        """
        Get: SendPacketsSendSize(self: SocketAsyncEventArgs) -> int
        Set: SendPacketsSendSize(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol:
        """
        Get: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) -> SocketClientAccessPolicyProtocol
        Set: SocketClientAccessPolicyProtocol(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SocketError(self) -> SocketError:
        """
        Get: SocketError(self: SocketAsyncEventArgs) -> SocketError
        Set: SocketError(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def SocketFlags(self) -> SocketFlags:
        """
        Get: SocketFlags(self: SocketAsyncEventArgs) -> SocketFlags
        Set: SocketFlags(self: SocketAsyncEventArgs) = value
        """
        ...

    @property
    def UserToken(self) -> object:
        """
        Get: UserToken(self: SocketAsyncEventArgs) -> object
        Set: UserToken(self: SocketAsyncEventArgs) = value
        """
        ...


    def OnCompleted(self, *args): #cannot find CLR method
        """ OnCompleted(self: SocketAsyncEventArgs, e: SocketAsyncEventArgs) """
        ...

    def SetBuffer(self, *__args): # -> 
        """ SetBuffer(self: SocketAsyncEventArgs, buffer: Array[Byte], offset: int, count: int)SetBuffer(self: SocketAsyncEventArgs, offset: int, count: int) """
        ...

    Completed = ...


class SocketAsyncOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketAsyncOperation, values: Accept (1), Connect (2), Disconnect (3), None (0), Receive (4), ReceiveFrom (5), ReceiveMessageFrom (6), Send (7), SendPackets (8), SendTo (9) """
    Accept: SocketAsyncOperation = ...
    Connect: SocketAsyncOperation = ...
    Disconnect: SocketAsyncOperation = ...
    Receive: SocketAsyncOperation = ...
    ReceiveFrom: SocketAsyncOperation = ...
    ReceiveMessageFrom: SocketAsyncOperation = ...
    Send: SocketAsyncOperation = ...
    SendPackets: SocketAsyncOperation = ...
    SendTo: SocketAsyncOperation = ...
    value__ = ...


class SocketClientAccessPolicyProtocol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketClientAccessPolicyProtocol, values: Http (1), Tcp (0) """
    Http: SocketClientAccessPolicyProtocol = ...
    Tcp: SocketClientAccessPolicyProtocol = ...
    value__ = ...


class SocketError(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketError, values: AccessDenied (10013), AddressAlreadyInUse (10048), AddressFamilyNotSupported (10047), AddressNotAvailable (10049), AlreadyInProgress (10037), ConnectionAborted (10053), ConnectionRefused (10061), ConnectionReset (10054), DestinationAddressRequired (10039), Disconnecting (10101), Fault (10014), HostDown (10064), HostNotFound (11001), HostUnreachable (10065), InProgress (10036), Interrupted (10004), InvalidArgument (10022), IOPending (997), IsConnected (10056), MessageSize (10040), NetworkDown (10050), NetworkReset (10052), NetworkUnreachable (10051), NoBufferSpaceAvailable (10055), NoData (11004), NoRecovery (11003), NotConnected (10057), NotInitialized (10093), NotSocket (10038), OperationAborted (995), OperationNotSupported (10045), ProcessLimit (10067), ProtocolFamilyNotSupported (10046), ProtocolNotSupported (10043), ProtocolOption (10042), ProtocolType (10041), Shutdown (10058), SocketError (-1), SocketNotSupported (10044), Success (0), SystemNotReady (10091), TimedOut (10060), TooManyOpenSockets (10024), TryAgain (11002), TypeNotFound (10109), VersionNotSupported (10092), WouldBlock (10035) """
    AccessDenied: SocketError = ...
    AddressAlreadyInUse: SocketError = ...
    AddressFamilyNotSupported: SocketError = ...
    AddressNotAvailable: SocketError = ...
    AlreadyInProgress: SocketError = ...
    ConnectionAborted: SocketError = ...
    ConnectionRefused: SocketError = ...
    ConnectionReset: SocketError = ...
    DestinationAddressRequired: SocketError = ...
    Disconnecting: SocketError = ...
    Fault: SocketError = ...
    HostDown: SocketError = ...
    HostNotFound: SocketError = ...
    HostUnreachable: SocketError = ...
    InProgress: SocketError = ...
    Interrupted: SocketError = ...
    InvalidArgument: SocketError = ...
    IOPending: SocketError = ...
    IsConnected: SocketError = ...
    MessageSize: SocketError = ...
    NetworkDown: SocketError = ...
    NetworkReset: SocketError = ...
    NetworkUnreachable: SocketError = ...
    NoBufferSpaceAvailable: SocketError = ...
    NoData: SocketError = ...
    NoRecovery: SocketError = ...
    NotConnected: SocketError = ...
    NotInitialized: SocketError = ...
    NotSocket: SocketError = ...
    OperationAborted: SocketError = ...
    OperationNotSupported: SocketError = ...
    ProcessLimit: SocketError = ...
    ProtocolFamilyNotSupported: SocketError = ...
    ProtocolNotSupported: SocketError = ...
    ProtocolOption: SocketError = ...
    ProtocolType: SocketError = ...
    Shutdown: SocketError = ...
    SocketError: SocketError = ...
    SocketNotSupported: SocketError = ...
    Success: SocketError = ...
    SystemNotReady: SocketError = ...
    TimedOut: SocketError = ...
    TooManyOpenSockets: SocketError = ...
    TryAgain: SocketError = ...
    TypeNotFound: SocketError = ...
    value__ = ...
    VersionNotSupported: SocketError = ...
    WouldBlock: SocketError = ...


class SocketException(Win32Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SocketException()
    SocketException(errorCode: int)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: SocketException) -> int """
        ...

    @property
    def SocketErrorCode(self) -> SocketError:
        """ Get: SocketErrorCode(self: SocketException) -> SocketError """
        ...


    SerializeObjectState = ...


class SocketFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SocketFlags, values: Broadcast (1024), ControlDataTruncated (512), DontRoute (4), MaxIOVectorLength (16), Multicast (2048), None (0), OutOfBand (1), Partial (32768), Peek (2), Truncated (256) """
    Broadcast: SocketFlags = ...
    ControlDataTruncated: SocketFlags = ...
    DontRoute: SocketFlags = ...
    MaxIOVectorLength: SocketFlags = ...
    Multicast: SocketFlags = ...
    OutOfBand: SocketFlags = ...
    Partial: SocketFlags = ...
    Peek: SocketFlags = ...
    Truncated: SocketFlags = ...
    value__ = ...


class SocketInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Options(self) -> SocketInformationOptions:
        """
        Get: Options(self: SocketInformation) -> SocketInformationOptions
        Set: Options(self: SocketInformation) = value
        """
        ...

    @property
    def ProtocolInformation(self) -> Array:
        """
        Get: ProtocolInformation(self: SocketInformation) -> Array[Byte]
        Set: ProtocolInformation(self: SocketInformation) = value
        """
        ...



class SocketInformationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SocketInformationOptions, values: Connected (2), Listening (4), NonBlocking (1), UseOnlyOverlappedIO (8) """
    Connected: SocketInformationOptions = ...
    Listening: SocketInformationOptions = ...
    NonBlocking: SocketInformationOptions = ...
    UseOnlyOverlappedIO: SocketInformationOptions = ...
    value__ = ...


class SocketOptionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketOptionLevel, values: IP (0), IPv6 (41), Socket (65535), Tcp (6), Udp (17) """
    IP: SocketOptionLevel = ...
    IPv6: SocketOptionLevel = ...
    Socket: SocketOptionLevel = ...
    Tcp: SocketOptionLevel = ...
    Udp: SocketOptionLevel = ...
    value__ = ...


class SocketOptionName(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketOptionName, values: AcceptConnection (2), AddMembership (12), AddSourceMembership (15), BlockSource (17), Broadcast (32), BsdUrgent (2), ChecksumCoverage (20), Debug (1), DontFragment (14), DontLinger (-129), DontRoute (16), DropMembership (13), DropSourceMembership (16), Error (4103), ExclusiveAddressUse (-5), Expedited (2), HeaderIncluded (2), HopLimit (21), IPOptions (1), IPProtectionLevel (23), IpTimeToLive (4), IPv6Only (27), KeepAlive (8), Linger (128), MaxConnections (2147483647), MulticastInterface (9), MulticastLoopback (11), MulticastTimeToLive (10), NoChecksum (1), NoDelay (1), OutOfBandInline (256), PacketInformation (19), ReceiveBuffer (4098), ReceiveLowWater (4100), ReceiveTimeout (4102), ReuseAddress (4), ReuseUnicastPort (12295), SendBuffer (4097), SendLowWater (4099), SendTimeout (4101), Type (4104), TypeOfService (3), UnblockSource (18), UpdateAcceptContext (28683), UpdateConnectContext (28688), UseLoopback (64) """
    AcceptConnection: SocketOptionName = ...
    AddMembership: SocketOptionName = ...
    AddSourceMembership: SocketOptionName = ...
    BlockSource: SocketOptionName = ...
    Broadcast: SocketOptionName = ...
    BsdUrgent: SocketOptionName = ...
    ChecksumCoverage: SocketOptionName = ...
    Debug: SocketOptionName = ...
    DontFragment: SocketOptionName = ...
    DontLinger: SocketOptionName = ...
    DontRoute: SocketOptionName = ...
    DropMembership: SocketOptionName = ...
    DropSourceMembership: SocketOptionName = ...
    Error: SocketOptionName = ...
    ExclusiveAddressUse: SocketOptionName = ...
    Expedited: SocketOptionName = ...
    HeaderIncluded: SocketOptionName = ...
    HopLimit: SocketOptionName = ...
    IPOptions: SocketOptionName = ...
    IPProtectionLevel: SocketOptionName = ...
    IpTimeToLive: SocketOptionName = ...
    IPv6Only: SocketOptionName = ...
    KeepAlive: SocketOptionName = ...
    Linger: SocketOptionName = ...
    MaxConnections: SocketOptionName = ...
    MulticastInterface: SocketOptionName = ...
    MulticastLoopback: SocketOptionName = ...
    MulticastTimeToLive: SocketOptionName = ...
    NoChecksum: SocketOptionName = ...
    NoDelay: SocketOptionName = ...
    OutOfBandInline: SocketOptionName = ...
    PacketInformation: SocketOptionName = ...
    ReceiveBuffer: SocketOptionName = ...
    ReceiveLowWater: SocketOptionName = ...
    ReceiveTimeout: SocketOptionName = ...
    ReuseAddress: SocketOptionName = ...
    ReuseUnicastPort: SocketOptionName = ...
    SendBuffer: SocketOptionName = ...
    SendLowWater: SocketOptionName = ...
    SendTimeout: SocketOptionName = ...
    Type: SocketOptionName = ...
    TypeOfService: SocketOptionName = ...
    UnblockSource: SocketOptionName = ...
    UpdateAcceptContext: SocketOptionName = ...
    UpdateConnectContext: SocketOptionName = ...
    UseLoopback: SocketOptionName = ...
    value__ = ...


class SocketPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ SocketPolicy() """
    pass

class SocketReceiveFromResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ReceivedBytes = ...
    RemoteEndPoint = ...


class SocketReceiveMessageFromResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    PacketInformation = ...
    ReceivedBytes = ...
    RemoteEndPoint = ...
    SocketFlags = ...


class SocketShutdown(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketShutdown, values: Both (2), Receive (0), Send (1) """
    Both: SocketShutdown = ...
    Receive: SocketShutdown = ...
    Send: SocketShutdown = ...
    value__ = ...


class SocketTaskExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AcceptAsync(socket:Socket, acceptSocket:Socket = ...) -> Task:
        """
        AcceptAsync(socket: Socket) -> Task[Socket]
        AcceptAsync(socket: Socket, acceptSocket: Socket) -> Task[Socket]
        """
        ...

    @staticmethod
    def ConnectAsync(socket:Socket, *__args:EndPoint) -> Task:
        """
        ConnectAsync(socket: Socket, remoteEP: EndPoint) -> Task
        ConnectAsync(socket: Socket, address: IPAddress, port: int) -> Task
        ConnectAsync(socket: Socket, addresses: Array[IPAddress], port: int) -> Task
        ConnectAsync(socket: Socket, host: str, port: int) -> Task
        """
        ...

    @staticmethod
    def ReceiveAsync(socket, *__args) -> Task:
        """
        ReceiveAsync(socket: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> Task[int]
        ReceiveAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags) -> Task[int]
        """
        ...

    @staticmethod
    def ReceiveFromAsync(socket:Socket, buffer:ArraySegment, socketFlags:SocketFlags, remoteEndPoint:EndPoint) -> Task:
        """ ReceiveFromAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveFromResult] """
        ...

    @staticmethod
    def ReceiveMessageFromAsync(socket:Socket, buffer:ArraySegment, socketFlags:SocketFlags, remoteEndPoint:EndPoint) -> Task:
        """ ReceiveMessageFromAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveMessageFromResult] """
        ...

    @staticmethod
    def SendAsync(socket, *__args) -> Task:
        """
        SendAsync(socket: Socket, buffers: IList[ArraySegment[Byte]], socketFlags: SocketFlags) -> Task[int]
        SendAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags) -> Task[int]
        """
        ...

    @staticmethod
    def SendToAsync(socket:Socket, buffer:ArraySegment, socketFlags:SocketFlags, remoteEP:EndPoint) -> Task:
        """ SendToAsync(socket: Socket, buffer: ArraySegment[Byte], socketFlags: SocketFlags, remoteEP: EndPoint) -> Task[int] """
        ...

    __all__: list = ...


class SocketType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketType, values: Dgram (2), Raw (3), Rdm (4), Seqpacket (5), Stream (1), Unknown (-1) """
    Dgram: SocketType = ...
    Raw: SocketType = ...
    Rdm: SocketType = ...
    Seqpacket: SocketType = ...
    Stream: SocketType = ...
    Unknown: SocketType = ...
    value__ = ...


class TcpClient(IDisposable): # skipped bases: <type 'object'>
    """
    TcpClient(localEP: IPEndPoint)
    TcpClient()
    TcpClient(family: AddressFamily)
    TcpClient(hostname: str, port: int)
    """
    @property
    def Active(self):
        ...

    @property
    def Available(self) -> int:
        """ Get: Available(self: TcpClient) -> int """
        ...

    @property
    def Client(self) -> Socket:
        """
        Get: Client(self: TcpClient) -> Socket
        Set: Client(self: TcpClient) = value
        """
        ...

    @property
    def Connected(self) -> bool:
        """ Get: Connected(self: TcpClient) -> bool """
        ...

    @property
    def ExclusiveAddressUse(self) -> bool:
        """
        Get: ExclusiveAddressUse(self: TcpClient) -> bool
        Set: ExclusiveAddressUse(self: TcpClient) = value
        """
        ...

    @property
    def LingerState(self) -> LingerOption:
        """
        Get: LingerState(self: TcpClient) -> LingerOption
        Set: LingerState(self: TcpClient) = value
        """
        ...

    @property
    def NoDelay(self) -> bool:
        """
        Get: NoDelay(self: TcpClient) -> bool
        Set: NoDelay(self: TcpClient) = value
        """
        ...

    @property
    def ReceiveBufferSize(self) -> int:
        """
        Get: ReceiveBufferSize(self: TcpClient) -> int
        Set: ReceiveBufferSize(self: TcpClient) = value
        """
        ...

    @property
    def ReceiveTimeout(self) -> int:
        """
        Get: ReceiveTimeout(self: TcpClient) -> int
        Set: ReceiveTimeout(self: TcpClient) = value
        """
        ...

    @property
    def SendBufferSize(self) -> int:
        """
        Get: SendBufferSize(self: TcpClient) -> int
        Set: SendBufferSize(self: TcpClient) = value
        """
        ...

    @property
    def SendTimeout(self) -> int:
        """
        Get: SendTimeout(self: TcpClient) -> int
        Set: SendTimeout(self: TcpClient) = value
        """
        ...


    def BeginConnect(self, *__args) -> IAsyncResult:
        """
        BeginConnect(self: TcpClient, host: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginConnect(self: TcpClient, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginConnect(self: TcpClient, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Close(self): # -> 
        """ Close(self: TcpClient) """
        ...

    def Connect(self, *__args:IPEndPoint): # -> 
        """ Connect(self: TcpClient, hostname: str, port: int)Connect(self: TcpClient, address: IPAddress, port: int)Connect(self: TcpClient, remoteEP: IPEndPoint)Connect(self: TcpClient, ipAddresses: Array[IPAddress], port: int) """
        ...

    def ConnectAsync(self, *__args) -> Task:
        """
        ConnectAsync(self: TcpClient, address: IPAddress, port: int) -> Task
        ConnectAsync(self: TcpClient, host: str, port: int) -> Task
        ConnectAsync(self: TcpClient, addresses: Array[IPAddress], port: int) -> Task
        """
        ...

    def EndConnect(self, asyncResult:IAsyncResult): # -> 
        """ EndConnect(self: TcpClient, asyncResult: IAsyncResult) """
        ...

    def GetStream(self) -> NetworkStream:
        """ GetStream(self: TcpClient) -> NetworkStream """
        ...


class TcpListener: # skipped bases: <type 'object'>, <type 'object'>
    """
    TcpListener(localEP: IPEndPoint)
    TcpListener(localaddr: IPAddress, port: int)
    TcpListener(port: int)
    """
    @property
    def Active(self):
        ...

    @property
    def ExclusiveAddressUse(self) -> bool:
        """
        Get: ExclusiveAddressUse(self: TcpListener) -> bool
        Set: ExclusiveAddressUse(self: TcpListener) = value
        """
        ...

    @property
    def LocalEndpoint(self) -> EndPoint:
        """ Get: LocalEndpoint(self: TcpListener) -> EndPoint """
        ...

    @property
    def Server(self) -> Socket:
        """ Get: Server(self: TcpListener) -> Socket """
        ...


    def AcceptSocket(self) -> Socket:
        """ AcceptSocket(self: TcpListener) -> Socket """
        ...

    def AcceptSocketAsync(self) -> Task:
        """ AcceptSocketAsync(self: TcpListener) -> Task[Socket] """
        ...

    def AcceptTcpClient(self) -> TcpClient:
        """ AcceptTcpClient(self: TcpListener) -> TcpClient """
        ...

    def AcceptTcpClientAsync(self) -> Task:
        """ AcceptTcpClientAsync(self: TcpListener) -> Task[TcpClient] """
        ...

    def AllowNatTraversal(self, allowed:bool): # -> 
        """ AllowNatTraversal(self: TcpListener, allowed: bool) """
        ...

    def BeginAcceptSocket(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginAcceptSocket(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginAcceptTcpClient(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginAcceptTcpClient(self: TcpListener, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    @staticmethod
    def Create(port:int) -> TcpListener:
        """ Create(port: int) -> TcpListener """
        ...

    def EndAcceptSocket(self, asyncResult:IAsyncResult) -> Socket:
        """ EndAcceptSocket(self: TcpListener, asyncResult: IAsyncResult) -> Socket """
        ...

    def EndAcceptTcpClient(self, asyncResult:IAsyncResult) -> TcpClient:
        """ EndAcceptTcpClient(self: TcpListener, asyncResult: IAsyncResult) -> TcpClient """
        ...

    def Pending(self) -> bool:
        """ Pending(self: TcpListener) -> bool """
        ...

    def Start(self, backlog:int = ...): # -> 
        """ Start(self: TcpListener)Start(self: TcpListener, backlog: int) """
        ...

    def Stop(self): # -> 
        """ Stop(self: TcpListener) """
        ...


class TransmitFileOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TransmitFileOptions, values: Disconnect (1), ReuseSocket (2), UseDefaultWorkerThread (0), UseKernelApc (32), UseSystemThread (16), WriteBehind (4) """
    Disconnect: TransmitFileOptions = ...
    ReuseSocket: TransmitFileOptions = ...
    UseDefaultWorkerThread: TransmitFileOptions = ...
    UseKernelApc: TransmitFileOptions = ...
    UseSystemThread: TransmitFileOptions = ...
    value__ = ...
    WriteBehind: TransmitFileOptions = ...


class UdpAnySourceMulticastClient(IDisposable): # skipped bases: <type 'object'>
    """ UdpAnySourceMulticastClient(groupAddress: IPAddress, localPort: int) """
    @property
    def MulticastLoopback(self) -> bool:
        """
        Get: MulticastLoopback(self: UdpAnySourceMulticastClient) -> bool
        Set: MulticastLoopback(self: UdpAnySourceMulticastClient) = value
        """
        ...

    @property
    def ReceiveBufferSize(self) -> int:
        """
        Get: ReceiveBufferSize(self: UdpAnySourceMulticastClient) -> int
        Set: ReceiveBufferSize(self: UdpAnySourceMulticastClient) = value
        """
        ...

    @property
    def SendBufferSize(self) -> int:
        """
        Get: SendBufferSize(self: UdpAnySourceMulticastClient) -> int
        Set: SendBufferSize(self: UdpAnySourceMulticastClient) = value
        """
        ...


    def BeginJoinGroup(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginJoinGroup(self: UdpAnySourceMulticastClient, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginReceiveFromGroup(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginReceiveFromGroup(self: UdpAnySourceMulticastClient, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSendTo(self, buffer:Array, offset:int, count:int, remoteEndPoint:IPEndPoint, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSendTo(self: UdpAnySourceMulticastClient, buffer: Array[Byte], offset: int, count: int, remoteEndPoint: IPEndPoint, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSendToGroup(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSendToGroup(self: UdpAnySourceMulticastClient, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BlockSource(self, sourceAddress:IPAddress): # -> 
        """ BlockSource(self: UdpAnySourceMulticastClient, sourceAddress: IPAddress) """
        ...

    def EndJoinGroup(self, result:IAsyncResult): # -> 
        """ EndJoinGroup(self: UdpAnySourceMulticastClient, result: IAsyncResult) """
        ...

    def EndReceiveFromGroup(self, result, source) -> Tuple_[int, IPEndPoint]:
        """ EndReceiveFromGroup(self: UdpAnySourceMulticastClient, result: IAsyncResult) -> (int, IPEndPoint) """
        ...

    def EndSendTo(self, result:IAsyncResult): # -> 
        """ EndSendTo(self: UdpAnySourceMulticastClient, result: IAsyncResult) """
        ...

    def EndSendToGroup(self, result:IAsyncResult): # -> 
        """ EndSendToGroup(self: UdpAnySourceMulticastClient, result: IAsyncResult) """
        ...

    def UnblockSource(self, sourceAddress:IPAddress): # -> 
        """ UnblockSource(self: UdpAnySourceMulticastClient, sourceAddress: IPAddress) """
        ...


class UdpClient(IDisposable): # skipped bases: <type 'object'>
    """
    UdpClient()
    UdpClient(family: AddressFamily)
    UdpClient(port: int)
    UdpClient(port: int, family: AddressFamily)
    UdpClient(localEP: IPEndPoint)
    UdpClient(hostname: str, port: int)
    """
    @property
    def Active(self):
        ...

    @property
    def Available(self) -> int:
        """ Get: Available(self: UdpClient) -> int """
        ...

    @property
    def Client(self) -> Socket:
        """
        Get: Client(self: UdpClient) -> Socket
        Set: Client(self: UdpClient) = value
        """
        ...

    @property
    def DontFragment(self) -> bool:
        """
        Get: DontFragment(self: UdpClient) -> bool
        Set: DontFragment(self: UdpClient) = value
        """
        ...

    @property
    def EnableBroadcast(self) -> bool:
        """
        Get: EnableBroadcast(self: UdpClient) -> bool
        Set: EnableBroadcast(self: UdpClient) = value
        """
        ...

    @property
    def ExclusiveAddressUse(self) -> bool:
        """
        Get: ExclusiveAddressUse(self: UdpClient) -> bool
        Set: ExclusiveAddressUse(self: UdpClient) = value
        """
        ...

    @property
    def MulticastLoopback(self) -> bool:
        """
        Get: MulticastLoopback(self: UdpClient) -> bool
        Set: MulticastLoopback(self: UdpClient) = value
        """
        ...

    @property
    def Ttl(self) -> Int16:
        """
        Get: Ttl(self: UdpClient) -> Int16
        Set: Ttl(self: UdpClient) = value
        """
        ...


    def AllowNatTraversal(self, allowed:bool): # -> 
        """ AllowNatTraversal(self: UdpClient, allowed: bool) """
        ...

    def BeginReceive(self, requestCallback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginReceive(self: UdpClient, requestCallback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSend(self, datagram, bytes, *__args) -> IAsyncResult:
        """
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        BeginSend(self: UdpClient, datagram: Array[Byte], bytes: int, requestCallback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def Close(self): # -> 
        """ Close(self: UdpClient) """
        ...

    def Connect(self, *__args:IPEndPoint): # -> 
        """ Connect(self: UdpClient, hostname: str, port: int)Connect(self: UdpClient, addr: IPAddress, port: int)Connect(self: UdpClient, endPoint: IPEndPoint) """
        ...

    def DropMulticastGroup(self, multicastAddr:IPAddress, ifindex:int = ...): # -> 
        """ DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress, ifindex: int)DropMulticastGroup(self: UdpClient, multicastAddr: IPAddress) """
        ...

    def EndReceive(self, asyncResult:IAsyncResult, remoteEP:IPEndPoint) -> Tuple_[Array, IPEndPoint]:
        """ EndReceive(self: UdpClient, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint) """
        ...

    def EndSend(self, asyncResult:IAsyncResult) -> int:
        """ EndSend(self: UdpClient, asyncResult: IAsyncResult) -> int """
        ...

    def JoinMulticastGroup(self, *__args:IPAddress): # -> 
        """ JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, localAddress: IPAddress)JoinMulticastGroup(self: UdpClient, ifindex: int, multicastAddr: IPAddress)JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress, timeToLive: int)JoinMulticastGroup(self: UdpClient, multicastAddr: IPAddress) """
        ...

    def Receive(self, remoteEP:IPEndPoint) -> Tuple_[Array, IPEndPoint]:
        """ Receive(self: UdpClient, remoteEP: IPEndPoint) -> (Array[Byte], IPEndPoint) """
        ...

    def ReceiveAsync(self) -> Task:
        """ ReceiveAsync(self: UdpClient) -> Task[UdpReceiveResult] """
        ...

    def Send(self, dgram:Array, bytes:int, *__args:IPEndPoint) -> int:
        """
        Send(self: UdpClient, dgram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> int
        Send(self: UdpClient, dgram: Array[Byte], bytes: int, hostname: str, port: int) -> int
        Send(self: UdpClient, dgram: Array[Byte], bytes: int) -> int
        """
        ...

    def SendAsync(self, datagram:Array, bytes:int, *__args:IPEndPoint) -> Task:
        """
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int) -> Task[int]
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, endPoint: IPEndPoint) -> Task[int]
        SendAsync(self: UdpClient, datagram: Array[Byte], bytes: int, hostname: str, port: int) -> Task[int]
        """
        ...


class UdpReceiveResult(IEquatable): # skipped bases: <type 'object'>
    """ UdpReceiveResult(buffer: Array[Byte], remoteEndPoint: IPEndPoint) """
    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: UdpReceiveResult) -> Array[Byte] """
        ...

    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """ Get: RemoteEndPoint(self: UdpReceiveResult) -> IPEndPoint """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: UdpReceiveResult) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UdpSingleSourceMulticastClient(IDisposable): # skipped bases: <type 'object'>
    """ UdpSingleSourceMulticastClient(sourceAddress: IPAddress, groupAddress: IPAddress, localPort: int) """
    @property
    def ReceiveBufferSize(self) -> int:
        """
        Get: ReceiveBufferSize(self: UdpSingleSourceMulticastClient) -> int
        Set: ReceiveBufferSize(self: UdpSingleSourceMulticastClient) = value
        """
        ...

    @property
    def SendBufferSize(self) -> int:
        """
        Get: SendBufferSize(self: UdpSingleSourceMulticastClient) -> int
        Set: SendBufferSize(self: UdpSingleSourceMulticastClient) = value
        """
        ...


    def BeginJoinGroup(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginJoinGroup(self: UdpSingleSourceMulticastClient, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginReceiveFromSource(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginReceiveFromSource(self: UdpSingleSourceMulticastClient, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginSendToSource(self, buffer:Array, offset:int, count:int, remotePort:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginSendToSource(self: UdpSingleSourceMulticastClient, buffer: Array[Byte], offset: int, count: int, remotePort: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndJoinGroup(self, result:IAsyncResult): # -> 
        """ EndJoinGroup(self: UdpSingleSourceMulticastClient, result: IAsyncResult) """
        ...

    def EndReceiveFromSource(self, result, sourcePort) -> Tuple_[int, int]:
        """ EndReceiveFromSource(self: UdpSingleSourceMulticastClient, result: IAsyncResult) -> (int, int) """
        ...

    def EndSendToSource(self, result:IAsyncResult): # -> 
        """ EndSendToSource(self: UdpSingleSourceMulticastClient, result: IAsyncResult) """
        ...


