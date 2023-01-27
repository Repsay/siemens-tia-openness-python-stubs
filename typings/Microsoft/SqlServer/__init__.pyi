# encoding: utf-8
# module Microsoft.SqlServer calls itself SqlServer
# from Microsoft.SqlServer.Management.Utility, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Dmf, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SmoExtended, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.ConnectionInfo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.TransferObjectsTask, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, Microsoft.SqlServer.Management.XEvent, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SqlWmiManagement, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.WmiEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.SystemMetadataProvider, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.WizardFramework, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.WizardFrameworkLite, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SqlEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Smo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Dmf.Common, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.SmartAdminPolicies, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Instapi, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.SmoMetadataProvider, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.ExceptionMessageBox, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.XEventDbScoped, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.Collector, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.CustomControls, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.GridControl, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Diagnostics.STrace, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.RegisteredServers, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Types, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.Sdk.Sfc, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SString, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.ServiceBrokerEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.ConnectionInfoExtended, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.SqlTDiagM, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Edition, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Management.HelpViewer, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.RegSvrEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Enum, IAsyncResult, IntPtr, 
    MulticastDelegate, UInt32)

from System.Data.SqlClient import SqlConnection

from System.Text import StringBuilder

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, INST_ID, 
    SQL_SVCS, field#)
"""

# no functions
# classes

class DelegateGetCOMPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetCOMPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetCOMPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetCOMPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetCOMPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstanceIDFromFTSApp(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstanceIDFromFTSApp(object: object, method: IntPtr) """
    def BeginInvoke(self, sFTSApp, pInstanceID, callback, object): # -> Tuple_[IAsyncResult, INST_ID]
        """ BeginInvoke(self: DelegateGetInstanceIDFromFTSApp, sFTSApp: str, callback: AsyncCallback, object: object) -> (IAsyncResult, INST_ID) """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateGetInstanceIDFromFTSApp, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sFTSApp, pInstanceID): # -> Tuple_[bool, INST_ID]
        """ Invoke(self: DelegateGetInstanceIDFromFTSApp, sFTSApp: str) -> (bool, INST_ID) """
        ...


class DelegateGetInstanceIDFromService(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstanceIDFromService(object: object, method: IntPtr) """
    def BeginInvoke(self, sServiceName, pInstanceID, callback, object): # -> Tuple_[IAsyncResult, INST_ID]
        """ BeginInvoke(self: DelegateGetInstanceIDFromService, sServiceName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, INST_ID) """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateGetInstanceIDFromService, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sServiceName, pInstanceID): # -> Tuple_[bool, INST_ID]
        """ Invoke(self: DelegateGetInstanceIDFromService, sServiceName: str) -> (bool, INST_ID) """
        ...


class DelegateGetInstanceNameFromFTSApp(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstanceNameFromFTSApp(object: object, method: IntPtr) """
    def BeginInvoke(self, sFTSApp, sInstanceName, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstanceNameFromFTSApp, sFTSApp: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstanceNameFromFTSApp, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sFTSApp, sInstanceName, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstanceNameFromFTSApp, sFTSApp: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstanceNameFromID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstanceNameFromID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sInstanceName, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstanceNameFromID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstanceNameFromID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sInstanceName, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstanceNameFromID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstanceNameFromService(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstanceNameFromService(object: object, method: IntPtr) """
    def BeginInvoke(self, sServiceName, sInstanceName, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstanceNameFromService, sServiceName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstanceNameFromService, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sServiceName, sInstanceName, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstanceNameFromService, sServiceName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstancePipeByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstancePipeByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sInstancePipe, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstancePipeByID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstancePipeByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sInstancePipe, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstancePipeByID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstancePipeByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstancePipeByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, instancePipe, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstancePipeByName, sInstanceName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstancePipeByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, instancePipe, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstancePipeByName, sInstanceName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstRegPathByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstRegPathByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, Service, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstRegPathByID, pInstanceID: INST_ID, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstRegPathByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, Service, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstRegPathByID, pInstanceID: INST_ID, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstRegPathByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstRegPathByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstRegPathByName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstRegPathByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstRegPathByName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstRootDirPathByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstRootDirPathByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, dirPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstRootDirPathByID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstRootDirPathByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, dirPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstRootDirPathByID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetInstRootRegPathByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetInstRootRegPathByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetInstRootRegPathByID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetInstRootRegPathByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetInstRootRegPathByID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetRegKeyAccessMask(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetRegKeyAccessMask(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, dwDesiredAccess, dwAccessMask, callback, object) -> Tuple_[IAsyncResult, UInt32]:
        """ BeginInvoke(self: DelegateGetRegKeyAccessMask, sRegPath: str, dwDesiredAccess: UInt32, callback: AsyncCallback, object: object) -> (IAsyncResult, UInt32) """
        ...

    def EndInvoke(self, dwAccessMask, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetRegKeyAccessMask, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, dwDesiredAccess, dwAccessMask) -> Tuple_[bool, UInt32]:
        """ Invoke(self: DelegateGetRegKeyAccessMask, sRegPath: str, dwDesiredAccess: UInt32) -> (bool, UInt32) """
        ...


class DelegateGetSettingValueForSKUAbsolute(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSettingValueForSKUAbsolute(object: object, method: IntPtr) """
    def BeginInvoke(self, setting:UInt32, skuID:UInt32, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateGetSettingValueForSKUAbsolute, setting: UInt32, skuID: UInt32, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> UInt32:
        """ EndInvoke(self: DelegateGetSettingValueForSKUAbsolute, result: IAsyncResult) -> UInt32 """
        ...

    def Invoke(self, setting:UInt32, skuID:UInt32) -> UInt32:
        """ Invoke(self: DelegateGetSettingValueForSKUAbsolute, setting: UInt32, skuID: UInt32) -> UInt32 """
        ...


class DelegateGetSQLBinPathByInstID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLBinPathByInstID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLBinPathByInstID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLBinPathByInstID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLBinPathByInstID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLDataRootByInstID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLDataRootByInstID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLDataRootByInstID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLDataRootByInstID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLDataRootByInstID, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLDataRootByInstName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLDataRootByInstName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLDataRootByInstName, sInstanceName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLDataRootByInstName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLDataRootByInstName, sInstanceName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLInstanceRegStringByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLInstanceRegStringByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, sRegPath, sValueName, sString, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLInstanceRegStringByID, pInstanceID: INST_ID, sRegPath: str, sValueName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLInstanceRegStringByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, sRegPath, sValueName, sString, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLInstanceRegStringByID, pInstanceID: INST_ID, sRegPath: str, sValueName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLReplicationRegPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLReplicationRegPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLReplicationRegPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLReplicationRegPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLReplicationRegPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLRootRegPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLRootRegPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLRootRegPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLRootRegPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLRootRegPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLServerByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLServerByID(object: object, method: IntPtr) """
    def BeginInvoke(self, sHostName, pInstanceID, sSQLServer, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLServerByID, sHostName: str, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLServerByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sHostName, pInstanceID, sSQLServer, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLServerByID, sHostName: str, pInstanceID: INST_ID) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLServerByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLServerByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sHostName, sInstanceName, sSQLServer, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLServerByName, sHostName: str, sInstanceName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLServerByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sHostName, sInstanceName, sSQLServer, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLServerByName, sHostName: str, sInstanceName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLServiceByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLServiceByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, Service, sServiceName, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLServiceByID, pInstanceID: INST_ID, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLServiceByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, Service, sServiceName, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLServiceByID, pInstanceID: INST_ID, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLServiceByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLServiceByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sServiceName, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLServiceByName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLServiceByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sServiceName, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLServiceByName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLToolsDirPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLToolsDirPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLToolsDirPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLToolsDirPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLToolsDirPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLToolsRegPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLToolsRegPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLToolsRegPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLToolsRegPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLToolsRegPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSQLVerSpecificRegString(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSQLVerSpecificRegString(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, sValueName, sString, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSQLVerSpecificRegString, sRegPath: str, sValueName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSQLVerSpecificRegString, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, sValueName, sString, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSQLVerSpecificRegString, sRegPath: str, sValueName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcBinPathByID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcBinPathByID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, Service, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcBinPathByID, pInstanceID: INST_ID, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcBinPathByID, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, pInstanceID, Service, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcBinPathByID, pInstanceID: INST_ID, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcBinPathByInstName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcBinPathByInstName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcBinPathByInstName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcBinPathByInstName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcBinPathByInstName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcBinPathByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcBinPathByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcBinPathByName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcBinPathByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcBinPathByName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcInstanceIDFromName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcInstanceIDFromName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, pInstanceID, callback, object): # -> Tuple_[IAsyncResult, INST_ID]
        """ BeginInvoke(self: DelegateGetSvcInstanceIDFromName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, INST_ID) """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateGetSvcInstanceIDFromName, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sInstanceName, Service, pInstanceID): # -> Tuple_[bool, INST_ID]
        """ Invoke(self: DelegateGetSvcInstanceIDFromName, sInstanceName: str, Service: SQL_SVCS) -> (bool, INST_ID) """
        ...


class DelegateGetSvcInstanceRegStringByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcInstanceRegStringByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sRegPath, sValueName, sString, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcInstanceRegStringByName, sInstanceName: str, Service: SQL_SVCS, sRegPath: str, sValueName: str, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcInstanceRegStringByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sRegPath, sValueName, sString, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcInstanceRegStringByName, sInstanceName: str, Service: SQL_SVCS, sRegPath: str, sValueName: str) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcInstRootDirPathByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcInstRootDirPathByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcInstRootDirPathByName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcInstRootDirPathByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcInstRootDirPathByName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetSvcInstRootRegPathByName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetSvcInstRootRegPathByName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName, Service, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetSvcInstRootRegPathByName, sInstanceName: str, Service: SQL_SVCS, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetSvcInstRootRegPathByName, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sInstanceName, Service, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetSvcInstRootRegPathByName, sInstanceName: str, Service: SQL_SVCS) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetVerSpecificRootDirPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetVerSpecificRootDirPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetVerSpecificRootDirPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetVerSpecificRootDirPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetVerSpecificRootDirPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateGetVerSpecificRootRegPath(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateGetVerSpecificRootRegPath(object: object, method: IntPtr) """
    def BeginInvoke(self, sRegPath, pdwSize, callback, object) -> Tuple_[IAsyncResult, StringBuilder, UInt32]:
        """ BeginInvoke(self: DelegateGetVerSpecificRootRegPath, callback: AsyncCallback, object: object) -> (IAsyncResult, StringBuilder, UInt32) """
        ...

    def EndInvoke(self, pdwSize, result) -> Tuple_[bool, UInt32]:
        """ EndInvoke(self: DelegateGetVerSpecificRootRegPath, result: IAsyncResult) -> (bool, UInt32) """
        ...

    def Invoke(self, sRegPath, pdwSize) -> Tuple_[bool, StringBuilder, UInt32]:
        """ Invoke(self: DelegateGetVerSpecificRootRegPath) -> (bool, StringBuilder, UInt32) """
        ...


class DelegateIsDefaultInstanceID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateIsDefaultInstanceID(object: object, method: IntPtr) """
    def BeginInvoke(self, pInstanceID, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'pInstanceID': 'INST_ID'}
        """ BeginInvoke(self: DelegateIsDefaultInstanceID, pInstanceID: INST_ID, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateIsDefaultInstanceID, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, pInstanceID) -> bool: # Not found arg types: {'pInstanceID': 'INST_ID'}
        """ Invoke(self: DelegateIsDefaultInstanceID, pInstanceID: INST_ID) -> bool """
        ...


class DelegateIsDefaultInstanceName(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateIsDefaultInstanceName(object: object, method: IntPtr) """
    def BeginInvoke(self, sInstanceName:str, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateIsDefaultInstanceName, sInstanceName: str, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateIsDefaultInstanceName, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sInstanceName:str) -> bool:
        """ Invoke(self: DelegateIsDefaultInstanceName, sInstanceName: str) -> bool """
        ...


class DelegateIsNameAgentService(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateIsNameAgentService(object: object, method: IntPtr) """
    def BeginInvoke(self, sServiceName:str, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateIsNameAgentService, sServiceName: str, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateIsNameAgentService, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sServiceName:str) -> bool:
        """ Invoke(self: DelegateIsNameAgentService, sServiceName: str) -> bool """
        ...


class DelegateIsNameSQLService(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateIsNameSQLService(object: object, method: IntPtr) """
    def BeginInvoke(self, sServiceName:str, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateIsNameSQLService, sServiceName: str, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DelegateIsNameSQLService, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sServiceName:str) -> bool:
        """ Invoke(self: DelegateIsNameSQLService, sServiceName: str) -> bool """
        ...


class DelegateQueryProductString(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryProductString(object: object, method: IntPtr) """
    def BeginInvoke(self, skuID, result, callback, object) -> Tuple_[IAsyncResult, IntPtr]:
        """ BeginInvoke(self: DelegateQueryProductString, skuID: UInt32, callback: AsyncCallback, object: object) -> (IAsyncResult, IntPtr) """
        ...

    def EndInvoke(self, result, __result) -> Tuple_[UInt32, IntPtr]:
        """ EndInvoke(self: DelegateQueryProductString, __result: IAsyncResult) -> (UInt32, IntPtr) """
        ...

    def Invoke(self, skuID, result) -> Tuple_[UInt32, IntPtr]:
        """ Invoke(self: DelegateQueryProductString, skuID: UInt32) -> (UInt32, IntPtr) """
        ...


class DelegateQueryProductValue(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryProductValue(object: object, method: IntPtr) """
    def BeginInvoke(self, product, instanceName:str, setting:UInt32, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'product': 'SQL_SVCS'}
        """ BeginInvoke(self: DelegateQueryProductValue, product: SQL_SVCS, instanceName: str, setting: UInt32, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> UInt32:
        """ EndInvoke(self: DelegateQueryProductValue, result: IAsyncResult) -> UInt32 """
        ...

    def Invoke(self, product, instanceName:str, setting:UInt32) -> UInt32: # Not found arg types: {'product': 'SQL_SVCS'}
        """ Invoke(self: DelegateQueryProductValue, product: SQL_SVCS, instanceName: str, setting: UInt32) -> UInt32 """
        ...


class DelegateQueryToolsValue(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryToolsValue(object: object, method: IntPtr) """
    def BeginInvoke(self, setting:UInt32, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DelegateQueryToolsValue, setting: UInt32, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> UInt32:
        """ EndInvoke(self: DelegateQueryToolsValue, result: IAsyncResult) -> UInt32 """
        ...

    def Invoke(self, setting:UInt32) -> UInt32:
        """ Invoke(self: DelegateQueryToolsValue, setting: UInt32) -> UInt32 """
        ...


class DelegateQueryValue2W(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryValue2W(object: object, method: IntPtr) """
    def BeginInvoke(self, setting:UInt32, instanceName:str, product, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'product': 'SQL_SVCS'}
        """ BeginInvoke(self: DelegateQueryValue2W, setting: UInt32, instanceName: str, product: SQL_SVCS, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> UInt32:
        """ EndInvoke(self: DelegateQueryValue2W, result: IAsyncResult) -> UInt32 """
        ...

    def Invoke(self, setting:UInt32, instanceName:str, product) -> UInt32: # Not found arg types: {'product': 'SQL_SVCS'}
        """ Invoke(self: DelegateQueryValue2W, setting: UInt32, instanceName: str, product: SQL_SVCS) -> UInt32 """
        ...


class DelegateQueryValueID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryValueID(object: object, method: IntPtr) """
    def BeginInvoke(self, setting:UInt32, instanceID, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'instanceID': 'INST_ID'}
        """ BeginInvoke(self: DelegateQueryValueID, setting: UInt32, instanceID: INST_ID, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> UInt32:
        """ EndInvoke(self: DelegateQueryValueID, result: IAsyncResult) -> UInt32 """
        ...

    def Invoke(self, setting:UInt32, instanceID) -> UInt32: # Not found arg types: {'instanceID': 'INST_ID'}
        """ Invoke(self: DelegateQueryValueID, setting: UInt32, instanceID: INST_ID) -> UInt32 """
        ...


class DelegateQueryValueWID(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DelegateQueryValueWID(object: object, method: IntPtr) """
    def BeginInvoke(self, instanceID, result, callback, object) -> Tuple_[IAsyncResult, IntPtr]:
        """ BeginInvoke(self: DelegateQueryValueWID, instanceID: INST_ID, callback: AsyncCallback, object: object) -> (IAsyncResult, IntPtr) """
        ...

    def EndInvoke(self, result, __result) -> Tuple_[UInt32, IntPtr]:
        """ EndInvoke(self: DelegateQueryValueWID, __result: IAsyncResult) -> (UInt32, IntPtr) """
        ...

    def Invoke(self, instanceID, result) -> Tuple_[UInt32, IntPtr]:
        """ Invoke(self: DelegateQueryValueWID, instanceID: INST_ID) -> (UInt32, IntPtr) """
        ...


class InstAPI: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetCOMPath(directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetCOMPath(directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstanceIDFromFTSApp(ftsApp:str, instanceID) -> bool: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetInstanceIDFromFTSApp(ftsApp: str, instanceID: INST_ID) -> bool """
        ...

    @staticmethod
    def GetInstanceIDFromService(serviceName:str, instanceID) -> bool: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetInstanceIDFromService(serviceName: str, instanceID: INST_ID) -> bool """
        ...

    @staticmethod
    def GetInstanceNameFromFTSApp(ftsApp:str, instanceName:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetInstanceNameFromFTSApp(ftsApp: str, instanceName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstanceNameFromID(instanceID, instanceName:StringBuilder = ..., bufferSize:UInt32 = ...) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """
        GetInstanceNameFromID(instanceID: INST_ID) -> str
        GetInstanceNameFromID(instanceID: INST_ID, instanceName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32)
        """
        ...

    @staticmethod
    def GetInstanceNameFromServerInstanceName(serverInstanceName:str) -> str:
        """ GetInstanceNameFromServerInstanceName(serverInstanceName: str) -> str """
        ...

    @staticmethod
    def GetInstanceNameFromService(serviceName:str, instanceName:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetInstanceNameFromService(serviceName: str, instanceName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstancePipeByID(instanceID, instancePipe:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetInstancePipeByID(instanceID: INST_ID, instancePipe: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstancePipeByName(instanceName:str, instancePipe:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetInstancePipeByName(instanceName: str, instancePipe: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstRegPathByID(instanceID, product, registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID', 'product': 'SQL_SVCS'}
        """ GetInstRegPathByID(instanceID: INST_ID, product: SQL_SVCS, registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstRegPathByName(instanceName:str, product, registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetInstRegPathByName(instanceName: str, product: SQL_SVCS, registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstRootDirPathByID(instanceID, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetInstRootDirPathByID(instanceID: INST_ID, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetInstRootRegPathByID(instanceID, registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetInstRootRegPathByID(instanceID: INST_ID, registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetMajorVersionSharedCodePath() -> str:
        """ GetMajorVersionSharedCodePath() -> str """
        ...

    @staticmethod
    def GetRegKeyAccessMask(registryPath:str, desiredAccess:UInt32, accessMask:UInt32) -> Tuple_[bool, UInt32]:
        """ GetRegKeyAccessMask(registryPath: str, desiredAccess: UInt32, accessMask: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLBinPathByInstID(instanceID, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetSQLBinPathByInstID(instanceID: INST_ID, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLDataRootByInstID(instanceID, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetSQLDataRootByInstID(instanceID: INST_ID, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLDataRootByInstName(instanceName:str, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLDataRootByInstName(instanceName: str, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLInstanceRegStringByID(instanceID, registryPath:str, valueName:str, data:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """ GetSQLInstanceRegStringByID(instanceID: INST_ID, registryPath: str, valueName: str, data: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLReplicationRegPath(registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLReplicationRegPath(registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLRootRegPath(registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLRootRegPath(registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLServerByID(hostName:str, instanceID, sqlServerName:StringBuilder = ..., bufferSize:UInt32 = ...) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID'}
        """
        GetSQLServerByID(hostName: str, instanceID: INST_ID) -> str
        GetSQLServerByID(hostName: str, instanceID: INST_ID, sqlServerName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32)
        """
        ...

    @staticmethod
    def GetSQLServerByName(hostName:str, instanceName:str, sqlServer:StringBuilder = ..., bufferSize:UInt32 = ...) -> Tuple_[bool, UInt32]:
        """
        GetSQLServerByName(hostName: str, instanceName: str) -> str
        GetSQLServerByName(hostName: str, instanceName: str, sqlServer: StringBuilder, bufferSize: UInt32) -> (bool, UInt32)
        """
        ...

    @staticmethod
    def GetSQLServiceByID(instanceID, product, serviceName:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID', 'product': 'SQL_SVCS'}
        """ GetSQLServiceByID(instanceID: INST_ID, product: SQL_SVCS, serviceName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLServiceByName(instanceName:str, product, serviceName:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSQLServiceByName(instanceName: str, product: SQL_SVCS, serviceName: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLToolsDirPath(directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLToolsDirPath(directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLToolsRegPath(registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLToolsRegPath(registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSQLVerSpecificRegString(registryPath:str, valueName:str, stringData:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetSQLVerSpecificRegString(registryPath: str, valueName: str, stringData: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcBinPathByID(instanceID, product, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'instanceID': 'INST_ID', 'product': 'SQL_SVCS'}
        """ GetSvcBinPathByID(instanceID: INST_ID, product: SQL_SVCS, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcBinPathByInstName(instanceName:str, product, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSvcBinPathByInstName(instanceName: str, product: SQL_SVCS, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcBinPathByName(instanceName:str, product, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSvcBinPathByName(instanceName: str, product: SQL_SVCS, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcInstanceIDFromName(instanceName:str, product, instanceID = ...) -> bool: # Not found arg types: {'instanceID': 'INST_ID', 'product': 'SQL_SVCS'}
        """
        GetSvcInstanceIDFromName(instanceName: str, product: SQL_SVCS) -> INST_ID
        GetSvcInstanceIDFromName(instanceName: str, product: SQL_SVCS, instanceID: INST_ID) -> bool
        """
        ...

    @staticmethod
    def GetSvcInstanceRegStringByName(instanceName:str, product, registryPath:str, valueName:str, data:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSvcInstanceRegStringByName(instanceName: str, product: SQL_SVCS, registryPath: str, valueName: str, data: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcInstRootDirPathByName(instanceName:str, product, directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSvcInstRootDirPathByName(instanceName: str, product: SQL_SVCS, directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetSvcInstRootRegPathByName(instanceName:str, product, registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]: # Not found arg types: {'product': 'SQL_SVCS'}
        """ GetSvcInstRootRegPathByName(instanceName: str, product: SQL_SVCS, registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetVerSpecificRootDirPath(directoryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetVerSpecificRootDirPath(directoryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def GetVerSpecificRootRegPath(registryPath:StringBuilder, bufferSize:UInt32) -> Tuple_[bool, UInt32]:
        """ GetVerSpecificRootRegPath(registryPath: StringBuilder, bufferSize: UInt32) -> (bool, UInt32) """
        ...

    @staticmethod
    def IsDefaultInstanceID(instanceID) -> bool: # Not found arg types: {'instanceID': 'INST_ID'}
        """ IsDefaultInstanceID(instanceID: INST_ID) -> bool """
        ...

    @staticmethod
    def IsDefaultInstanceName(instanceName:str) -> bool:
        """ IsDefaultInstanceName(instanceName: str) -> bool """
        ...

    @staticmethod
    def IsNameAgentService(serviceName:str) -> bool:
        """ IsNameAgentService(serviceName: str) -> bool """
        ...

    @staticmethod
    def IsNameSQLService(serviceName:str) -> bool:
        """ IsNameSQLService(serviceName: str) -> bool """
        ...

    __all__: list = ...


class InstAPIException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstAPIException()
    InstAPIException(message: str)
    InstAPIException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class INST_ID: # skipped bases: <type 'object'>, <type 'object'>
    """ INST_ID() """
    def ToString(self) -> str:
        """ ToString(self: INST_ID) -> str """
        ...


class SharedBins: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def InitSharedBins() -> bool:
        """ InitSharedBins() -> bool """
        ...

    __all__: list = ...


class Sqlboot: # skipped bases: <type 'object'>, <type 'object'>
    """ Sqlboot() """
    @staticmethod
    def GetSettingValueForSKUAbsolute(setting:UInt32, skuID:UInt32) -> UInt32:
        """ GetSettingValueForSKUAbsolute(setting: UInt32, skuID: UInt32) -> UInt32 """
        ...

    @staticmethod
    def QueryProductString(skuID:UInt32) -> str:
        """ QueryProductString(skuID: UInt32) -> str """
        ...

    @staticmethod
    def QueryProductValue(product, instanceName:str, setting:UInt32) -> UInt32: # Not found arg types: {'product': 'SQL_SVCS'}
        """ QueryProductValue(product: SQL_SVCS, instanceName: str, setting: UInt32) -> UInt32 """
        ...

    @staticmethod
    def QueryRemoteSqlProductValue(setting:UInt32, connection:SqlConnection) -> UInt32:
        """ QueryRemoteSqlProductValue(setting: UInt32, connection: SqlConnection) -> UInt32 """
        ...

    @staticmethod
    def QueryToolsValue(setting:UInt32) -> UInt32:
        """ QueryToolsValue(setting: UInt32) -> UInt32 """
        ...

    @staticmethod
    def QueryValueID(setting:UInt32, instanceID:INST_ID) -> UInt32:
        """ QueryValueID(setting: UInt32, instanceID: INST_ID) -> UInt32 """
        ...

    @staticmethod
    def QueryValueWID(instanceID:INST_ID) -> str:
        """ QueryValueWID(instanceID: INST_ID) -> str """
        ...


class SqlbootConst: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlbootConst() """
    DBM_STD: UInt32 = ...
    DBM_UNL: UInt32 = ...
    DBM_WTN: UInt32 = ...
    ENGINE_ENTERPRISE: UInt32 = ...
    ENGINE_EXPRESS: UInt32 = ...
    ENGINE_MSDE: UInt32 = ...
    ENGINE_STANDARD: UInt32 = ...
    PACKAGE_ENTERPRISE: UInt32 = ...
    PACKAGE_EXPRESS: UInt32 = ...
    PACKAGE_MSDE: UInt32 = ...
    PACKAGE_OFFICE: UInt32 = ...
    PACKAGE_STANDARD: UInt32 = ...
    SKU_BI: UInt32 = ...
    SKU_CLOUD: UInt32 = ...
    SKU_DATA_CENTER: UInt32 = ...
    SKU_DESKTOP: UInt32 = ...
    SKU_DEVELOPER: UInt32 = ...
    SKU_DEVELOPER_DESKTOP: UInt32 = ...
    SKU_DEVELOPER_STANDARD: UInt32 = ...
    SKU_ENTERPRISE: UInt32 = ...
    SKU_ENTERPRISE_CORE: UInt32 = ...
    SKU_EVAL: UInt32 = ...
    SKU_EXPRESS: UInt32 = ...
    SKU_EXPRESS_ADVANCED: UInt32 = ...
    SKU_EXPRESS_TOOLS: UInt32 = ...
    SKU_MSDE: UInt32 = ...
    SKU_NO: UInt32 = ...
    SKU_OFFICE: UInt32 = ...
    SKU_PERSONAL: UInt32 = ...
    SKU_PREMIUM: UInt32 = ...
    SKU_SBS: UInt32 = ...
    SKU_SQLMSO: UInt32 = ...
    SKU_SQLWID: UInt32 = ...
    SKU_STANDARD: UInt32 = ...
    SKU_UPGRADE_ALLOWED: UInt32 = ...
    SKU_UPGRADE_EQUAL: UInt32 = ...
    SKU_UPGRADE_PROHIBITED: UInt32 = ...
    SKU_WEB: UInt32 = ...
    SKU_WMSDE: UInt32 = ...
    SKU_WORKGROUP: UInt32 = ...
    SKU_YES: UInt32 = ...
    VALUE_AS_ADVANCED: UInt32 = ...
    VALUE_AS_BISM_MODE: UInt32 = ...
    VALUE_AS_MAXCORES: UInt32 = ...
    VALUE_AS_MAXCPUS: UInt32 = ...
    VALUE_AS_MEMORY_LIMIT_MD: UInt32 = ...
    VALUE_AS_MEMORY_LIMIT_TABULAR: UInt32 = ...
    VALUE_AS_SELFSERVICE_ENGINE: UInt32 = ...
    VALUE_ATTACHEDDB_LIMIT: UInt32 = ...
    VALUE_BACKUP_COMPRESSION: UInt32 = ...
    VALUE_BACKUP_ENCRYPTION: UInt32 = ...
    VALUE_CLR_ENABLED: UInt32 = ...
    VALUE_CORE_LIMIT: UInt32 = ...
    VALUE_DATA_MINING: UInt32 = ...
    VALUE_DAYS_LEFT: UInt32 = ...
    VALUE_DB_MIRRORING: UInt32 = ...
    VALUE_DB_SIZE_LIMIT: UInt32 = ...
    VALUE_DEFAULT_PROTOCOL_LIST: UInt32 = ...
    VALUE_DISPLAY_PID: UInt32 = ...
    VALUE_DISTRIBUTED_QUERIES_ENABLED: UInt32 = ...
    VALUE_DREPLAYCLIENT: UInt32 = ...
    VALUE_DREPLAYCLIENT_NUMBER: UInt32 = ...
    VALUE_DREPLAYCONTROLLER: UInt32 = ...
    VALUE_DTS: UInt32 = ...
    VALUE_DTS_EDITION: UInt32 = ...
    VALUE_DTS_GUI: UInt32 = ...
    VALUE_ENGINE: UInt32 = ...
    VALUE_ENGLISH_QUERY: UInt32 = ...
    VALUE_ERROR: UInt32 = ...
    VALUE_EXPIRED: UInt32 = ...
    VALUE_FAILOVER_CLST: UInt32 = ...
    VALUE_FORCE_PERSEAT: UInt32 = ...
    VALUE_GET_OS_TYPE: UInt32 = ...
    VALUE_GROUP_COMMIT_ENABLED: UInt32 = ...
    VALUE_GUI_TOOLS: UInt32 = ...
    VALUE_HADR: UInt32 = ...
    VALUE_HEKATON_ENABLED: UInt32 = ...
    VALUE_INSTALL_FTS: UInt32 = ...
    VALUE_LICENSE_LIMIT: UInt32 = ...
    VALUE_LICENSE_MODE: UInt32 = ...
    VALUE_LIC_DLG: UInt32 = ...
    VALUE_LOG_SHIPPING: UInt32 = ...
    VALUE_MAKE_MANAGED_ALLOWED: UInt32 = ...
    VALUE_MDS_ENABLED: UInt32 = ...
    VALUE_MEMORY_LIMIT: UInt32 = ...
    VALUE_MI_SUPPORT: UInt32 = ...
    VALUE_MULTILANG_GUI_SUPPORT: UInt32 = ...
    VALUE_NETWORK_PROTOCOLS_ENABLED: UInt32 = ...
    VALUE_NOT_FOUND: UInt32 = ...
    VALUE_OLAP_ENGINE: UInt32 = ...
    VALUE_OLAP_SERVICES: UInt32 = ...
    VALUE_OS_SUPPORTED: UInt32 = ...
    VALUE_PACKAGE: UInt32 = ...
    VALUE_POLYBASE_ENABLED: UInt32 = ...
    VALUE_REPLICATION: UInt32 = ...
    VALUE_R_SCALE: UInt32 = ...
    VALUE_SERVICE_BROKER_PAID: UInt32 = ...
    VALUE_SKU: UInt32 = ...
    VALUE_SKU_STRING: UInt32 = ...
    VALUE_SMP: UInt32 = ...
    VALUE_SOAP_SUPPORTED: UInt32 = ...
    VALUE_SQLAGENT_ALLOWED: UInt32 = ...
    VALUE_SQL_MAIL_ENABLED: UInt32 = ...
    VALUE_SUM_ENABLED: UInt32 = ...
    VALUE_TBU: UInt32 = ...
    VALUE_UCP_ALLOWED: UInt32 = ...
    VALUE_UNLIMITED: UInt32 = ...
    VALUE_USER_INSTANCES_ENABLED: UInt32 = ...
    VALUE_USE_LICENSING: UInt32 = ...
    VALUE_VALIDATE: UInt32 = ...
    VALUE_XP_ACCESS_ENABLED: UInt32 = ...


class SqlbootException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlbootException()
    SqlbootException(message: str)
    SqlbootException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SQL_SVCS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SQL_SVCS, values: SVC_ADHELPER (13), SVC_AGENT (1), SVC_BIDS (15), SVC_BROWSER (12), SVC_CLUSTER (4), SVC_DREPLAYCLIENT (16), SVC_DREPLAYCONTROLLER (17), SVC_DTS (10), SVC_FDLAUNCHER (14), SVC_LAUNCHPAD (22), SVC_MDS (18), SVC_NS (9), SVC_OLAP (3), SVC_PBDMS (20), SVC_PBENGINE (19), SVC_PROVIDERS (7), SVC_REPLICATION (5), SVC_REPORT (8), SVC_SEARCH (2), SVC_SETUP (6), SVC_SQL (0), SVC_SQL_SHARED_MR (21), SVC_TOOLS (11) """
    SVC_ADHELPER: SQL_SVCS = ...
    SVC_AGENT: SQL_SVCS = ...
    SVC_BIDS: SQL_SVCS = ...
    SVC_BROWSER: SQL_SVCS = ...
    SVC_CLUSTER: SQL_SVCS = ...
    SVC_DREPLAYCLIENT: SQL_SVCS = ...
    SVC_DREPLAYCONTROLLER: SQL_SVCS = ...
    SVC_DTS: SQL_SVCS = ...
    SVC_FDLAUNCHER: SQL_SVCS = ...
    SVC_LAUNCHPAD: SQL_SVCS = ...
    SVC_MDS: SQL_SVCS = ...
    SVC_NS: SQL_SVCS = ...
    SVC_OLAP: SQL_SVCS = ...
    SVC_PBDMS: SQL_SVCS = ...
    SVC_PBENGINE: SQL_SVCS = ...
    SVC_PROVIDERS: SQL_SVCS = ...
    SVC_REPLICATION: SQL_SVCS = ...
    SVC_REPORT: SQL_SVCS = ...
    SVC_SEARCH: SQL_SVCS = ...
    SVC_SETUP: SQL_SVCS = ...
    SVC_SQL: SQL_SVCS = ...
    SVC_SQL_SHARED_MR: SQL_SVCS = ...
    SVC_TOOLS: SQL_SVCS = ...
    value__ = ...


# variables with complex values

