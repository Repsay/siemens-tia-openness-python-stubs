# encoding: utf-8
# module Siemens.Engineering.SW.TechnologicalObjects.Motion calls itself Motion
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.HW import Channel, DeviceItem

from Siemens.Engineering.SW.Tags import PlcTag

from Siemens.Engineering.SW.TechnologicalObjects import (
    TechnologicalInstanceDBAssociation, TechnologicalInstanceDBComposition)

from System import Enum, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AxisEncoderHardwareConnectionInterface(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to hardware objects for axis and encoder TechnologicalInstanceDBs """
    @property
    def Channel(self) -> Channel:
        """
        Connected Channel

        Get: Channel(self: AxisEncoderHardwareConnectionInterface) -> Channel
        """
        ...

    @property
    def ConnectOption(self) -> ConnectOption:
        """
        ConnectOption that has been set when the connection was made

        Get: ConnectOption(self: AxisEncoderHardwareConnectionInterface) -> ConnectOption
        """
        ...

    @property
    def InputAddress(self) -> int:
        """
        Raw input bit address

        Get: InputAddress(self: AxisEncoderHardwareConnectionInterface) -> int
        """
        ...

    @property
    def InputModule(self): # ->
        """
        Connected input (sub) module

        Get: InputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def InputOutputModule(self): # ->
        """
        Connected mixed (sub) module that contains input and output addresses

        Get: InputOutputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """
        Indicates whether the interface is connected

        Get: IsConnected(self: AxisEncoderHardwareConnectionInterface) -> bool
        """
        ...

    @property
    def OutputAddress(self) -> int:
        """
        Raw output bit address

        Get: OutputAddress(self: AxisEncoderHardwareConnectionInterface) -> int
        """
        ...

    @property
    def OutputModule(self): # ->
        """
        Connected output (sub) module

        Get: OutputModule(self: AxisEncoderHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def OutputTag(self): # ->
        """
        Connected tag (analog connection)

        Get: OutputTag(self: AxisEncoderHardwareConnectionInterface) -> PlcTag
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AxisEncoderHardwareConnectionInterface) -> IEngineeringObject
        """
        ...

    @property
    def PathToDBMember(self) -> str:
        """
        Path to connected DB member

        Get: PathToDBMember(self: AxisEncoderHardwareConnectionInterface) -> str
        """
        ...

    @property
    def SensorIndexInActorTelegram(self) -> int:
        """
        Connection to sensor part in actor telegram.

        Get: SensorIndexInActorTelegram(self: AxisEncoderHardwareConnectionInterface) -> int
        """
        ...


    def Connect(self, *__args:Channel): # ->
        """
        Connect(self: AxisEncoderHardwareConnectionInterface, channel: Channel)

            Connect with a Channel (e.g. of a TechnologyModule)

            channel: Channel to connect

        Connect(self: AxisEncoderHardwareConnectionInterface, moduleInOut: DeviceItem)

            Connect with a mixed (sub) module that contains input and output addresses

            moduleInOut: Module or submodule that contains input and output addresses

        Connect(self: AxisEncoderHardwareConnectionInterface, outputTag: PlcTag)

            Connect to an output PlcTag in order to establish an analog connection

            outputTag: Output PlcTag to connect

        Connect(self: AxisEncoderHardwareConnectionInterface, pathToDBMember: str)

            Connect to DB member

            pathToDBMember: Path to the DB member

        Connect(self: AxisEncoderHardwareConnectionInterface, moduleIn: DeviceItem, moduleOut: DeviceItem)

            Connect with separate (sub) modules for inputs and outputs, specifying an additional ConnectOption

            moduleIn: Module or submodule that contains the input address

            moduleOut: Module or submodule that contains the output address

        Connect(self: AxisEncoderHardwareConnectionInterface, moduleIn: DeviceItem, moduleOut: DeviceItem, connectOption: ConnectOption)

            Connect with separate (sub) modules for inputs and outputs, specifying an additional ConnectOption

            moduleIn: Module or submodule that contains the input address

            moduleOut: Module or submodule that contains the output address

            connectOption: Additional option for making the connection

        Connect(self: AxisEncoderHardwareConnectionInterface, addressIn: int, addressOut: int, connectOption: ConnectOption)

            Connect specifying input and output bit addresses directly

            addressIn: Input bit address to connect

            addressOut: Output bit address to connect

            connectOption: Additional option for making the connection
        """
        ...

    def Disconnect(self): # ->
        """
        Disconnect(self: AxisEncoderHardwareConnectionInterface)

            Remove an existing connection
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AxisEncoderHardwareConnectionInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AxisEncoderHardwareConnectionInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AxisEncoderHardwareConnectionInterfaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ AxisEncoderHardwareConnectionInterface Composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: AxisEncoderHardwareConnectionInterfaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AxisEncoderHardwareConnectionInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AxisEncoderHardwareConnectionInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AxisEncoderHardwareConnectionInterface](enumerable: IEnumerable[AxisEncoderHardwareConnectionInterface], value: AxisEncoderHardwareConnectionInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AxisHardwareConnectionProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to hardware objects for axis TechnologicalInstanceDBs """
    @property
    def ActorInterface(self) -> AxisEncoderHardwareConnectionInterface:
        """
        Provides access to the connections for the actor interface of the axis

        Get: ActorInterface(self: AxisHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterface
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AxisHardwareConnectionProvider) -> IEngineeringObject
        """
        ...

    @property
    def SensorInterface(self) -> AxisEncoderHardwareConnectionInterfaceComposition:
        """
        Provides access to the connections for the sensor interfaces of the axis

        Get: SensorInterface(self: AxisHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterfaceComposition
        """
        ...

    @property
    def TorqueInterface(self) -> TorqueHardwareConnectionInterface:
        """
        Provides access to the torque connection interface of the axis

        Get: TorqueInterface(self: AxisHardwareConnectionProvider) -> TorqueHardwareConnectionInterface
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AxisHardwareConnectionProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AxisHardwareConnectionProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CamDataFormat(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Describes the format in which a cam object should be Exportet/Imported

    enum CamDataFormat, values: MCD (0), PointList (2), Scout (1)
    """
    MCD: CamDataFormat = ...
    PointList: CamDataFormat = ...
    Scout: CamDataFormat = ...
    value__ = ...


class CamDataFormatSeparator(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Describes a Seperator with which the data should be seperated on Import/Export

    enum CamDataFormatSeparator, values: Comma (0), Tab (1)
    """
    Comma: CamDataFormatSeparator = ...
    Tab: CamDataFormatSeparator = ...
    value__ = ...


class CamDataSupport(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles import export commands for Cam """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CamDataSupport) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CamDataSupport) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def LoadCamData(self, sourceFile:FileInfo, separator:CamDataFormatSeparator): # ->
        """
        LoadCamData(self: CamDataSupport, sourceFile: FileInfo, separator: CamDataFormatSeparator)

            Loads the cam data from the specified file

            sourceFile: Path to the file that will be loaded

            separator: Separator to use
        """
        ...

    def LoadCamDataBinary(self, sourceFile:FileInfo): # ->
        """
        LoadCamDataBinary(self: CamDataSupport, sourceFile: FileInfo)

            Loads the cam data from the specified binary file

            sourceFile: Path to the file that will be loaded
        """
        ...

    def SaveCamData(self, destinationFile:FileInfo, format:CamDataFormat, separator:CamDataFormatSeparator): # ->
        """
        SaveCamData(self: CamDataSupport, destinationFile: FileInfo, format: CamDataFormat, separator: CamDataFormatSeparator)

            Saves the cam data to the specified file in the given format

            destinationFile: Path to the destination file

            format: format in which the data should be stored

            separator: Separator to use
        """
        ...

    def SaveCamDataBinary(self, destinationFile:FileInfo): # ->
        """
        SaveCamDataBinary(self: CamDataSupport, destinationFile: FileInfo)

            Saves the cam data to the specified file in binary format

            destinationFile: Path to the destination file
        """
        ...

    def SaveCamDataPointList(self, destinationFile:FileInfo, separator:CamDataFormatSeparator, samplePoints:int): # ->
        """
        SaveCamDataPointList(self: CamDataSupport, destinationFile: FileInfo, separator: CamDataFormatSeparator, samplePoints: int)

            Saves the cam data to the specified file as a point list

            destinationFile: Path to the destination file

            separator: Separator to use

            samplePoints: Number of sample points
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CamDataSupport) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectOption(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Describes additional options for making a connection

    enum ConnectOption, values: AllowAllModules (1), Default (0)
    """
    AllowAllModules: ConnectOption = ...
    Default: ConnectOption = ...
    value__ = ...


class EncoderHardwareConnectionProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to hardware objects for encoder TechnologicalInstanceDBs """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: EncoderHardwareConnectionProvider) -> IEngineeringObject
        """
        ...

    @property
    def SensorInterface(self) -> AxisEncoderHardwareConnectionInterface:
        """
        Provides access to the connections for the sensor interface of the encoder

        Get: SensorInterface(self: EncoderHardwareConnectionProvider) -> AxisEncoderHardwareConnectionInterface
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: EncoderHardwareConnectionProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: EncoderHardwareConnectionProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MeasuringInputHardwareConnectionProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to hardware objects for measuring input TechnologicalInstanceDBs """
    @property
    def Channel(self) -> Channel:
        """
        Connected Channel

        Get: Channel(self: MeasuringInputHardwareConnectionProvider) -> Channel
        """
        ...

    @property
    def ChannelIndex(self) -> int:
        """
        Index of connected channel with respect to InputModule

        Get: ChannelIndex(self: MeasuringInputHardwareConnectionProvider) -> int
        """
        ...

    @property
    def InputAddress(self) -> int:
        """
        Raw input bit address

        Get: InputAddress(self: MeasuringInputHardwareConnectionProvider) -> int
        """
        ...

    @property
    def InputModule(self): # ->
        """
        Connected input (sub) module

        Get: InputModule(self: MeasuringInputHardwareConnectionProvider) -> DeviceItem
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """
        Indicates whether the interface is connected

        Get: IsConnected(self: MeasuringInputHardwareConnectionProvider) -> bool
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MeasuringInputHardwareConnectionProvider) -> IEngineeringObject
        """
        ...


    def Connect(self, *__args:Channel): # ->
        """
        Connect(self: MeasuringInputHardwareConnectionProvider, channel: Channel)

            Connect with a Channel (e.g. of a TechnologyModule)

            channel: Channel to connect

        Connect(self: MeasuringInputHardwareConnectionProvider, addressIn: int)

            Connect specifying the input bit address directly

            addressIn: Input bit address to connect

        Connect(self: MeasuringInputHardwareConnectionProvider, moduleIn: DeviceItem, channelIndex: int)

            Connect with a (sub) module, specifying an additional channel index

            moduleIn: Module or submodule to connect

            channelIndex: Index of connected channel with respect to moduleIn
        """
        ...

    def Disconnect(self): # ->
        """
        Disconnect(self: MeasuringInputHardwareConnectionProvider)

            Remove an existing connection
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MeasuringInputHardwareConnectionProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MeasuringInputHardwareConnectionProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OutputCamHardwareConnectionProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to hardware objects for output cam and cam track TechnologicalInstanceDBs """
    @property
    def Channel(self) -> Channel:
        """
        Connected Channel

        Get: Channel(self: OutputCamHardwareConnectionProvider) -> Channel
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """
        Indicates whether the interface is connected

        Get: IsConnected(self: OutputCamHardwareConnectionProvider) -> bool
        """
        ...

    @property
    def OutputAddress(self) -> int:
        """
        Raw output bit address

        Get: OutputAddress(self: OutputCamHardwareConnectionProvider) -> int
        """
        ...

    @property
    def OutputTag(self) -> PlcTag:
        """
        Connected tag

        Get: OutputTag(self: OutputCamHardwareConnectionProvider) -> PlcTag
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OutputCamHardwareConnectionProvider) -> IEngineeringObject
        """
        ...


    def Connect(self, *__args:Channel): # ->
        """
        Connect(self: OutputCamHardwareConnectionProvider, channel: Channel)

            Connect with a Channel (e.g. of a TechnologyModule)

            channel: Channel to connect

        Connect(self: OutputCamHardwareConnectionProvider, outputTag: PlcTag)

            Connect to an output PlcTag

            outputTag: Output PlcTag to connect

        Connect(self: OutputCamHardwareConnectionProvider, addressOut: int)

            Connect specifying the output bit address directly

            addressOut: Output bit address to connect
        """
        ...

    def Disconnect(self): # ->
        """
        Disconnect(self: OutputCamHardwareConnectionProvider)

            Remove an existing connection
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OutputCamHardwareConnectionProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OutputCamHardwareConnectionProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OutputCamMeasuringInputContainer(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Container for output cam, cam track and measuring input TOs """
    @property
    def MeasuringInputs(self) -> TechnologicalInstanceDBComposition:
        """
        Contains measuring input TOs

        Get: MeasuringInputs(self: OutputCamMeasuringInputContainer) -> TechnologicalInstanceDBComposition
        """
        ...

    @property
    def OutputCams(self) -> TechnologicalInstanceDBComposition:
        """
        Contains output cam and cam track TOs

        Get: OutputCams(self: OutputCamMeasuringInputContainer) -> TechnologicalInstanceDBComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OutputCamMeasuringInputContainer) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OutputCamMeasuringInputContainer) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OutputCamMeasuringInputContainer) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SynchronousAxisMasterValues(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections between SynchronousAxis Technological Objects and their master values """
    @property
    def ActualValueCoupling(self) -> TechnologicalInstanceDBAssociation:
        """
        Master values that are coupled via actual values

        Get: ActualValueCoupling(self: SynchronousAxisMasterValues) -> TechnologicalInstanceDBAssociation
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SynchronousAxisMasterValues) -> IEngineeringObject
        """
        ...

    @property
    def SetPointCoupling(self) -> TechnologicalInstanceDBAssociation:
        """
        Master values that are coupled via set points

        Get: SetPointCoupling(self: SynchronousAxisMasterValues) -> TechnologicalInstanceDBAssociation
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SynchronousAxisMasterValues) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SynchronousAxisMasterValues) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TorqueHardwareConnectionInterface(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Handles connections to Torque possible hardware objects for axis and encoder TechnologicalInstanceDBs """
    @property
    def ConnectOption(self) -> ConnectOption:
        """
        ConnectOption that has been set when the connection was made

        Get: ConnectOption(self: TorqueHardwareConnectionInterface) -> ConnectOption
        """
        ...

    @property
    def InputAddress(self) -> int:
        """
        Raw input bit address

        Get: InputAddress(self: TorqueHardwareConnectionInterface) -> int
        """
        ...

    @property
    def InputModule(self): # ->
        """
        Connected input (sub) module

        Get: InputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def InputOutputModule(self): # ->
        """
        Connected mixed (sub) module that contains input and output addresses

        Get: InputOutputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """
        Indicates whether the interface is connected

        Get: IsConnected(self: TorqueHardwareConnectionInterface) -> bool
        """
        ...

    @property
    def OutputAddress(self) -> int:
        """
        Raw output bit address

        Get: OutputAddress(self: TorqueHardwareConnectionInterface) -> int
        """
        ...

    @property
    def OutputModule(self): # ->
        """
        Connected output (sub) module

        Get: OutputModule(self: TorqueHardwareConnectionInterface) -> DeviceItem
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TorqueHardwareConnectionInterface) -> IEngineeringObject
        """
        ...

    @property
    def PathToDBMember(self) -> str:
        """
        Path to connected DB member

        Get: PathToDBMember(self: TorqueHardwareConnectionInterface) -> str
        """
        ...


    def Connect(self, *__args:DeviceItem): # ->
        """
        Connect(self: TorqueHardwareConnectionInterface, moduleInOut: DeviceItem)

            Connect with a mixed (sub) module that contains input and output addresses

            moduleInOut: Module or submodule that contains input and output addresses

        Connect(self: TorqueHardwareConnectionInterface, pathToDBMember: str)

            Connect to DB member

            pathToDBMember: Path to the DB member

        Connect(self: TorqueHardwareConnectionInterface, moduleIn: DeviceItem, moduleOut: DeviceItem)

            Connect with separate (sub) modules for inputs and outputs, specifying an additional ConnectOption

            moduleIn: Module or submodule that contains the input address

            moduleOut: Module or submodule that contains the output address

        Connect(self: TorqueHardwareConnectionInterface, moduleIn: DeviceItem, moduleOut: DeviceItem, connectOption: ConnectOption)

            Connect with separate (sub) modules for inputs and outputs, specifying an additional ConnectOption

            moduleIn: Module or submodule that contains the input address

            moduleOut: Module or submodule that contains the output address

            connectOption: Additional option for making the connection

        Connect(self: TorqueHardwareConnectionInterface, addressIn: int, addressOut: int, connectOption: ConnectOption)

            Connect specifying input and output bit addresses directly

            addressIn: Input bit address to connect

            addressOut: Output bit address to connect

            connectOption: Additional option for making the connection
        """
        ...

    def Disconnect(self): # ->
        """
        Disconnect(self: TorqueHardwareConnectionInterface)

            Remove an existing connection
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TorqueHardwareConnectionInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TorqueHardwareConnectionInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
