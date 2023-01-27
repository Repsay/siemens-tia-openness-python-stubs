# encoding: utf-8
# module Microsoft.VisualStudio.Debugger.Interop calls itself Interop
# from Microsoft.VisualStudio.Debugger.Interop, Version=8.0.1.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Enum, Guid, Int64, IntPtr, Type, UInt16, UInt32, 
    UInt64)

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AD_PROCESS_ID: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwProcessId = ...
    dwUnused = ...
    guidProcessId = ...
    ProcessIdType = ...


class BP_CONDITION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrCondition = ...
    bstrContext = ...
    nRadix = ...
    pThread = ...
    styleCondition = ...


class BP_ERROR_RESOLUTION_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpResLocation = ...
    bstrMessage = ...
    dwFields = ...
    dwType = ...
    pProgram = ...
    pThread = ...


class BP_LOCATION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpLocationType = ...
    unionmember1 = ...
    unionmember2 = ...
    unionmember3 = ...
    unionmember4 = ...


class BP_LOCATION_CODE_ADDRESS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrAddress = ...
    bstrContext = ...
    bstrFunction = ...
    bstrModuleUrl = ...


class BP_LOCATION_CODE_CONTEXT: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pCodeContext = ...


class BP_LOCATION_CODE_FILE_LINE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrContext = ...
    pDocPos = ...


class BP_LOCATION_CODE_FUNC_OFFSET: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrContext = ...
    pFuncPos = ...


class BP_LOCATION_CODE_STRING: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrCodeExpr = ...
    bstrContext = ...


class BP_LOCATION_DATA_STRING: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrContext = ...
    bstrDataExpr = ...
    dwNumElements = ...
    pThread = ...


class BP_LOCATION_RESOLUTION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pResolution = ...


class BP_PASSCOUNT: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwPassCount = ...
    stylePassCount = ...


class BP_REQUEST_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpCondition = ...
    bpLocation = ...
    bpPassCount = ...
    bstrProgramName = ...
    bstrThreadName = ...
    dwFields = ...
    dwFlags = ...
    guidLanguage = ...
    pProgram = ...
    pThread = ...


class BP_REQUEST_INFO2: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpCondition = ...
    bpLocation = ...
    bpPassCount = ...
    bstrConstraint = ...
    bstrProgramName = ...
    bstrThreadName = ...
    bstrTracepoint = ...
    dwFields = ...
    dwFlags = ...
    guidLanguage = ...
    guidVendor = ...
    pProgram = ...
    pThread = ...


class BP_RESOLUTION_CODE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pCodeContext = ...


class BP_RESOLUTION_DATA: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrDataExpr = ...
    bstrFunc = ...
    bstrImage = ...
    dwFlags = ...


class BP_RESOLUTION_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpResLocation = ...
    dwFields = ...
    pProgram = ...
    pThread = ...


class BP_RESOLUTION_LOCATION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bpType = ...
    unionmember1 = ...
    unionmember2 = ...
    unionmember3 = ...
    unionmember4 = ...


class BREAKPOINT_STATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BREAKPOINT_STATE, values: BREAKPOINT_DELETED (0), BREAKPOINT_DISABLED (1), BREAKPOINT_ENABLED (2) """
    BREAKPOINT_DELETED: BREAKPOINT_STATE = ...
    BREAKPOINT_DISABLED: BREAKPOINT_STATE = ...
    BREAKPOINT_ENABLED: BREAKPOINT_STATE = ...
    value__ = ...


class BREAKREASON(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BREAKREASON, values: BREAKREASON_BREAKPOINT (1), BREAKREASON_DEBUGGER_BLOCK (2), BREAKREASON_DEBUGGER_HALT (5), BREAKREASON_ERROR (6), BREAKREASON_HOST_INITIATED (3), BREAKREASON_JIT (7), BREAKREASON_LANGUAGE_INITIATED (4), BREAKREASON_STEP (0) """
    BREAKREASON_BREAKPOINT: BREAKREASON = ...
    BREAKREASON_DEBUGGER_BLOCK: BREAKREASON = ...
    BREAKREASON_DEBUGGER_HALT: BREAKREASON = ...
    BREAKREASON_ERROR: BREAKREASON = ...
    BREAKREASON_HOST_INITIATED: BREAKREASON = ...
    BREAKREASON_JIT: BREAKREASON = ...
    BREAKREASON_LANGUAGE_INITIATED: BREAKREASON = ...
    BREAKREASON_STEP: BREAKREASON = ...
    value__ = ...


class BREAKRESUMEACTION(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BREAKRESUMEACTION, values: BREAKRESUMEACTION_ABORT (0), BREAKRESUMEACTION_CONTINUE (1), BREAKRESUMEACTION_IGNORE (5), BREAKRESUMEACTION_STEP_INTO (2), BREAKRESUMEACTION_STEP_OUT (4), BREAKRESUMEACTION_STEP_OVER (3) """
    BREAKRESUMEACTION_ABORT: BREAKRESUMEACTION = ...
    BREAKRESUMEACTION_CONTINUE: BREAKRESUMEACTION = ...
    BREAKRESUMEACTION_IGNORE: BREAKRESUMEACTION = ...
    BREAKRESUMEACTION_STEP_INTO: BREAKRESUMEACTION = ...
    BREAKRESUMEACTION_STEP_OUT: BREAKRESUMEACTION = ...
    BREAKRESUMEACTION_STEP_OVER: BREAKRESUMEACTION = ...
    value__ = ...


class BSTR_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


class BUILT_TYPE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    guidModule = ...
    pUnderlyingField = ...
    ulAppDomainID = ...


class CHECKSUM_DATA: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ByteCount = ...
    pBytes = ...


class CODE_PATH: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrName = ...
    pCode = ...


class COMPUTER_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwOperatingSystemVersion = ...
    wProcessorArchitecture = ...
    wSuiteMask = ...


class CONNECTION_PROTOCOL(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CONNECTION_PROTOCOL, values: CONNECTION_HTTP (5), CONNECTION_LOCAL (2), CONNECTION_NONE (0), CONNECTION_OTHER (6), CONNECTION_PIPE (3), CONNECTION_TCPIP (4), CONNECTION_UNKNOWN (1) """
    CONNECTION_HTTP: CONNECTION_PROTOCOL = ...
    CONNECTION_LOCAL: CONNECTION_PROTOCOL = ...
    CONNECTION_NONE: CONNECTION_PROTOCOL = ...
    CONNECTION_OTHER: CONNECTION_PROTOCOL = ...
    CONNECTION_PIPE: CONNECTION_PROTOCOL = ...
    CONNECTION_TCPIP: CONNECTION_PROTOCOL = ...
    CONNECTION_UNKNOWN: CONNECTION_PROTOCOL = ...
    value__ = ...


class CONNECT_REASON(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CONNECT_REASON, values: CONNECT_ATTACH (1), CONNECT_CAUSALITY (5), CONNECT_DIAGNOSE_WEB_ERROR (6), CONNECT_LAUNCH (2), CONNECT_LOCAL (0), CONNECT_SQL_AUTO_ATTACH (4), CONNECT_WEB_AUTO_ATTACH (3) """
    CONNECT_ATTACH: CONNECT_REASON = ...
    CONNECT_CAUSALITY: CONNECT_REASON = ...
    CONNECT_DIAGNOSE_WEB_ERROR: CONNECT_REASON = ...
    CONNECT_LAUNCH: CONNECT_REASON = ...
    CONNECT_LOCAL: CONNECT_REASON = ...
    CONNECT_SQL_AUTO_ATTACH: CONNECT_REASON = ...
    CONNECT_WEB_AUTO_ATTACH: CONNECT_REASON = ...
    value__ = ...


class Constants(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Constants, values: DBG_ATTRIB_ACCESS_ALL (2031616), DBG_ATTRIB_ACCESS_FINAL (1048576), DBG_ATTRIB_ACCESS_NONE (65536), DBG_ATTRIB_ACCESS_PRIVATE (262144), DBG_ATTRIB_ACCESS_PROTECTED (524288), DBG_ATTRIB_ACCESS_PUBLIC (131072), DBG_ATTRIB_ALL (18446744073709551615), DBG_ATTRIB_BASECLASS (17592186044416), DBG_ATTRIB_CHILD_ALL (280375465082880), DBG_ATTRIB_CLASS (8796093022208), DBG_ATTRIB_DATA (1099511627776), DBG_ATTRIB_INNERCLASS (70368744177664), DBG_ATTRIB_INTERFACE (35184372088832), DBG_ATTRIB_METHOD (2199023255552), DBG_ATTRIB_MOSTDERIVEDCLASS (140737488355328), DBG_ATTRIB_NONE (0), DBG_ATTRIB_OBJ_IS_EXPANDABLE (1), DBG_ATTRIB_OVERLOADED_CONTAINER (128), DBG_ATTRIB_PROPERTY (4398046511104), DBG_ATTRIB_STORAGE_ALL (251658240), DBG_ATTRIB_STORAGE_GLOBAL (33554432), DBG_ATTRIB_STORAGE_NONE (16777216), DBG_ATTRIB_STORAGE_REGISTER (134217728), DBG_ATTRIB_STORAGE_STATIC (67108864), DBG_ATTRIB_TYPE_ALL (133143986176), DBG_ATTRIB_TYPE_CONSTANT (17179869184), DBG_ATTRIB_TYPE_NONE (4294967296), DBG_ATTRIB_TYPE_SYNCHRONIZED (34359738368), DBG_ATTRIB_TYPE_VIRTUAL (8589934592), DBG_ATTRIB_TYPE_VOLATILE (68719476736), DBG_ATTRIB_VALUE_AUTOEXPANDED (4096), DBG_ATTRIB_VALUE_BOOLEAN (256), DBG_ATTRIB_VALUE_BOOLEAN_TRUE (512), DBG_ATTRIB_VALUE_ERROR (32), DBG_ATTRIB_VALUE_INVALID (1024), DBG_ATTRIB_VALUE_NAT (2048), DBG_ATTRIB_VALUE_READONLY (16), DBG_ATTRIB_VALUE_SIDE_EFFECT (64), DBG_ATTRIB_VALUE_TIMEOUT (8192) """
    DBG_ATTRIB_ACCESS_ALL: Constants = ...
    DBG_ATTRIB_ACCESS_FINAL: Constants = ...
    DBG_ATTRIB_ACCESS_NONE: Constants = ...
    DBG_ATTRIB_ACCESS_PRIVATE: Constants = ...
    DBG_ATTRIB_ACCESS_PROTECTED: Constants = ...
    DBG_ATTRIB_ACCESS_PUBLIC: Constants = ...
    DBG_ATTRIB_ALL: Constants = ...
    DBG_ATTRIB_BASECLASS: Constants = ...
    DBG_ATTRIB_CHILD_ALL: Constants = ...
    DBG_ATTRIB_CLASS: Constants = ...
    DBG_ATTRIB_DATA: Constants = ...
    DBG_ATTRIB_INNERCLASS: Constants = ...
    DBG_ATTRIB_INTERFACE: Constants = ...
    DBG_ATTRIB_METHOD: Constants = ...
    DBG_ATTRIB_MOSTDERIVEDCLASS: Constants = ...
    DBG_ATTRIB_NONE: Constants = ...
    DBG_ATTRIB_OBJ_IS_EXPANDABLE: Constants = ...
    DBG_ATTRIB_OVERLOADED_CONTAINER: Constants = ...
    DBG_ATTRIB_PROPERTY: Constants = ...
    DBG_ATTRIB_STORAGE_ALL: Constants = ...
    DBG_ATTRIB_STORAGE_GLOBAL: Constants = ...
    DBG_ATTRIB_STORAGE_NONE: Constants = ...
    DBG_ATTRIB_STORAGE_REGISTER: Constants = ...
    DBG_ATTRIB_STORAGE_STATIC: Constants = ...
    DBG_ATTRIB_TYPE_ALL: Constants = ...
    DBG_ATTRIB_TYPE_CONSTANT: Constants = ...
    DBG_ATTRIB_TYPE_NONE: Constants = ...
    DBG_ATTRIB_TYPE_SYNCHRONIZED: Constants = ...
    DBG_ATTRIB_TYPE_VIRTUAL: Constants = ...
    DBG_ATTRIB_TYPE_VOLATILE: Constants = ...
    DBG_ATTRIB_VALUE_AUTOEXPANDED: Constants = ...
    DBG_ATTRIB_VALUE_BOOLEAN: Constants = ...
    DBG_ATTRIB_VALUE_BOOLEAN_TRUE: Constants = ...
    DBG_ATTRIB_VALUE_ERROR: Constants = ...
    DBG_ATTRIB_VALUE_INVALID: Constants = ...
    DBG_ATTRIB_VALUE_NAT: Constants = ...
    DBG_ATTRIB_VALUE_READONLY: Constants = ...
    DBG_ATTRIB_VALUE_SIDE_EFFECT: Constants = ...
    DBG_ATTRIB_VALUE_TIMEOUT: Constants = ...
    value__ = ...


class ConstructorMatchOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConstructorMatchOptions, values: crAll (0), crNonStatic (1), crStatic (2) """
    crAll: ConstructorMatchOptions = ...
    crNonStatic: ConstructorMatchOptions = ...
    crStatic: ConstructorMatchOptions = ...
    value__ = ...


class CONSTRUCTOR_ENUM(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CONSTRUCTOR_ENUM, values: crAll (0), crNonStatic (1), crStatic (2) """
    crAll: CONSTRUCTOR_ENUM = ...
    crNonStatic: CONSTRUCTOR_ENUM = ...
    crStatic: CONSTRUCTOR_ENUM = ...
    value__ = ...


class CONST_GUID_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


class CONTEXT_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrAddress = ...
    bstrAddressAbsolute = ...
    bstrAddressOffset = ...
    bstrFunction = ...
    bstrModuleUrl = ...
    dwFields = ...
    posFunctionOffset = ...


class CRASHING_PROGRAM_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwProcessId = ...
    guidEngine = ...
    JitFlags = ...
    programId = ...
    pSetEventCallback = ...
    szExceptionText = ...


class DebugPropertyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    m_bstrFullName = ...
    m_bstrName = ...
    m_bstrType = ...
    m_bstrValue = ...
    m_dwAttrib = ...
    m_dwValidFields = ...
    m_pDebugProp = ...


class DebugStackFrameDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwLim = ...
    dwMin = ...
    fFinal = ...
    pdsf = ...
    punkFinal = ...


class DebugStackFrameDescriptor64: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwLim = ...
    dwMin = ...
    fFinal = ...
    pdsf = ...
    punkFinal = ...


class DEBUG_ADDRESS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    addr = ...
    guidModule = ...
    tokClass = ...
    ulAppDomainID = ...


class DEBUG_ADDRESS_UNION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwKind = ...
    unionmember = ...


class DEBUG_CUSTOM_VIEWER: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrDescription = ...
    bstrMenuName = ...
    bstrMetric = ...
    dwID = ...
    guidLang = ...
    guidVendor = ...


class DEBUG_PROPERTY_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrFullName = ...
    bstrName = ...
    bstrType = ...
    bstrValue = ...
    dwAttrib = ...
    dwFields = ...
    pProperty = ...


class DEBUG_REFERENCE_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrName = ...
    bstrType = ...
    bstrValue = ...
    dwAttrib = ...
    dwFields = ...
    dwRefType = ...
    pReference = ...


class DisassemblyData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrAddress = ...
    bstrAddressOffset = ...
    bstrCodeBytes = ...
    bstrDocumentUrl = ...
    bstrOpcode = ...
    bstrOperands = ...
    bstrSymbol = ...
    dwByteOffset = ...
    dwFields = ...
    dwFlags = ...
    posBeg = ...
    posEnd = ...
    uCodeLocationId = ...


class DOCUMENTNAMETYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DOCUMENTNAMETYPE, values: DOCUMENTNAMETYPE_APPNODE (0), DOCUMENTNAMETYPE_FILE_TAIL (2), DOCUMENTNAMETYPE_TITLE (1), DOCUMENTNAMETYPE_URL (3) """
    DOCUMENTNAMETYPE_APPNODE: DOCUMENTNAMETYPE = ...
    DOCUMENTNAMETYPE_FILE_TAIL: DOCUMENTNAMETYPE = ...
    DOCUMENTNAMETYPE_TITLE: DOCUMENTNAMETYPE = ...
    DOCUMENTNAMETYPE_URL: DOCUMENTNAMETYPE = ...
    value__ = ...


class EncUnavailableReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EncUnavailableReason, values: ENCUN_ATTACH (5), ENCUN_EMBEDDED (4), ENCUN_INRUNMODE (10), ENCUN_INTEROP (1), ENCUN_MINIDUMP (3), ENCUN_MODULENOTLOADED (8), ENCUN_MODULERELOADED (9), ENCUN_NONE (0), ENCUN_NOTBUILT (11), ENCUN_REMOTE (12), ENCUN_SQLCLR (2), ENCUN_STOPONEMODE (7), ENCUN_WIN64 (6) """
    ENCUN_ATTACH: EncUnavailableReason = ...
    ENCUN_EMBEDDED: EncUnavailableReason = ...
    ENCUN_INRUNMODE: EncUnavailableReason = ...
    ENCUN_INTEROP: EncUnavailableReason = ...
    ENCUN_MINIDUMP: EncUnavailableReason = ...
    ENCUN_MODULENOTLOADED: EncUnavailableReason = ...
    ENCUN_MODULERELOADED: EncUnavailableReason = ...
    ENCUN_NONE: EncUnavailableReason = ...
    ENCUN_NOTBUILT: EncUnavailableReason = ...
    ENCUN_REMOTE: EncUnavailableReason = ...
    ENCUN_SQLCLR: EncUnavailableReason = ...
    ENCUN_STOPONEMODE: EncUnavailableReason = ...
    ENCUN_WIN64: EncUnavailableReason = ...
    value__ = ...


class ENUMERATED_PROCESS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrUserName = ...
    dwProcessFlags = ...
    dwProcessId = ...
    dwSessionId = ...


class ENUMERATED_PROCESS_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


class enum_ADDRESS_KIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_ADDRESS_KIND, values: ADDRESS_KIND_METADATA_ARRAYELEM (20), ADDRESS_KIND_METADATA_FIELD (17), ADDRESS_KIND_METADATA_LOCAL (18), ADDRESS_KIND_METADATA_METHOD (16), ADDRESS_KIND_METADATA_PARAM (19), ADDRESS_KIND_METADATA_RETVAL (21), ADDRESS_KIND_NATIVE (1), ADDRESS_KIND_UNMANAGED_PHYSICAL (5), ADDRESS_KIND_UNMANAGED_THIS_RELATIVE (2) """
    ADDRESS_KIND_METADATA_ARRAYELEM: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_METADATA_FIELD: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_METADATA_LOCAL: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_METADATA_METHOD: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_METADATA_PARAM: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_METADATA_RETVAL: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_NATIVE: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_UNMANAGED_PHYSICAL: enum_ADDRESS_KIND = ...
    ADDRESS_KIND_UNMANAGED_THIS_RELATIVE: enum_ADDRESS_KIND = ...
    value__ = ...


class enum_AD_PROCESS_ID(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_AD_PROCESS_ID, values: AD_PROCESS_ID_GUID (1), AD_PROCESS_ID_SYSTEM (0) """
    AD_PROCESS_ID_GUID: enum_AD_PROCESS_ID = ...
    AD_PROCESS_ID_SYSTEM: enum_AD_PROCESS_ID = ...
    value__ = ...


class enum_APPBREAKFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_APPBREAKFLAGS, values: APPBREAKFLAG_DEBUGGER_BLOCK (1), APPBREAKFLAG_DEBUGGER_HALT (2), APPBREAKFLAG_IN_BREAKPOINT (2147483648), APPBREAKFLAG_NESTED (131072), APPBREAKFLAG_STEP (65536), APPBREAKFLAG_STEPTYPE_BYTECODE (1048576), APPBREAKFLAG_STEPTYPE_MACHINE (2097152), APPBREAKFLAG_STEPTYPE_MASK (15728640), APPBREAKFLAG_STEPTYPE_SOURCE (0) """
    APPBREAKFLAG_DEBUGGER_BLOCK: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_DEBUGGER_HALT: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_IN_BREAKPOINT: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_NESTED: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_STEP: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_STEPTYPE_BYTECODE: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_STEPTYPE_MACHINE: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_STEPTYPE_MASK: enum_APPBREAKFLAGS = ...
    APPBREAKFLAG_STEPTYPE_SOURCE: enum_APPBREAKFLAGS = ...
    value__ = ...


class enum_ASSEMBLYFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_ASSEMBLYFLAGS, values: ASMF_SHAREDDIR (2), ASMF_USERDIR (1) """
    ASMF_SHAREDDIR: enum_ASSEMBLYFLAGS = ...
    ASMF_USERDIR: enum_ASSEMBLYFLAGS = ...
    value__ = ...


class enum_ASSEMBLYLOCRESOLUTION(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_ASSEMBLYLOCRESOLUTION, values: ALR_BYTES (16), ALR_ERROR (8), ALR_NAME (0), ALR_REMOTEDIR (4), ALR_SHAREDDIR (2), ALR_USERDIR (1) """
    ALR_BYTES: enum_ASSEMBLYLOCRESOLUTION = ...
    ALR_ERROR: enum_ASSEMBLYLOCRESOLUTION = ...
    ALR_NAME: enum_ASSEMBLYLOCRESOLUTION = ...
    ALR_REMOTEDIR: enum_ASSEMBLYLOCRESOLUTION = ...
    ALR_SHAREDDIR: enum_ASSEMBLYLOCRESOLUTION = ...
    ALR_USERDIR: enum_ASSEMBLYLOCRESOLUTION = ...
    value__ = ...


class enum_ATTACH_REASON(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_ATTACH_REASON, values: ATTACH_REASON_AUTO (3), ATTACH_REASON_LAUNCH (1), ATTACH_REASON_USER (2) """
    ATTACH_REASON_AUTO: enum_ATTACH_REASON = ...
    ATTACH_REASON_LAUNCH: enum_ATTACH_REASON = ...
    ATTACH_REASON_USER: enum_ATTACH_REASON = ...
    value__ = ...


class enum_BPERESI_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BPERESI_FIELDS, values: BPERESI_ALLFIELDS (4294967295), BPERESI_BPRESLOCATION (1), BPERESI_MESSAGE (8), BPERESI_PROGRAM (2), BPERESI_THREAD (4), BPERESI_TYPE (16) """
    BPERESI_ALLFIELDS: enum_BPERESI_FIELDS = ...
    BPERESI_BPRESLOCATION: enum_BPERESI_FIELDS = ...
    BPERESI_MESSAGE: enum_BPERESI_FIELDS = ...
    BPERESI_PROGRAM: enum_BPERESI_FIELDS = ...
    BPERESI_THREAD: enum_BPERESI_FIELDS = ...
    BPERESI_TYPE: enum_BPERESI_FIELDS = ...
    value__ = ...


class enum_BPREQI_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BPREQI_FIELDS, values: BPREQI_ALLFIELDS (4095), BPREQI_ALLOLDFIELDS (511), BPREQI_BPLOCATION (1), BPREQI_CONDITION (128), BPREQI_CONSTRAINT (1024), BPREQI_FLAGS (256), BPREQI_LANGUAGE (2), BPREQI_PASSCOUNT (64), BPREQI_PROGRAM (4), BPREQI_PROGRAMNAME (8), BPREQI_THREAD (16), BPREQI_THREADNAME (32), BPREQI_TRACEPOINT (2048), BPREQI_VENDOR (512) """
    BPREQI_ALLFIELDS: enum_BPREQI_FIELDS = ...
    BPREQI_ALLOLDFIELDS: enum_BPREQI_FIELDS = ...
    BPREQI_BPLOCATION: enum_BPREQI_FIELDS = ...
    BPREQI_CONDITION: enum_BPREQI_FIELDS = ...
    BPREQI_CONSTRAINT: enum_BPREQI_FIELDS = ...
    BPREQI_FLAGS: enum_BPREQI_FIELDS = ...
    BPREQI_LANGUAGE: enum_BPREQI_FIELDS = ...
    BPREQI_PASSCOUNT: enum_BPREQI_FIELDS = ...
    BPREQI_PROGRAM: enum_BPREQI_FIELDS = ...
    BPREQI_PROGRAMNAME: enum_BPREQI_FIELDS = ...
    BPREQI_THREAD: enum_BPREQI_FIELDS = ...
    BPREQI_THREADNAME: enum_BPREQI_FIELDS = ...
    BPREQI_TRACEPOINT: enum_BPREQI_FIELDS = ...
    BPREQI_VENDOR: enum_BPREQI_FIELDS = ...
    value__ = ...


class enum_BPRESI_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BPRESI_FIELDS, values: BPRESI_ALLFIELDS (4294967295), BPRESI_BPRESLOCATION (1), BPRESI_PROGRAM (2), BPRESI_THREAD (4) """
    BPRESI_ALLFIELDS: enum_BPRESI_FIELDS = ...
    BPRESI_BPRESLOCATION: enum_BPRESI_FIELDS = ...
    BPRESI_PROGRAM: enum_BPRESI_FIELDS = ...
    BPRESI_THREAD: enum_BPRESI_FIELDS = ...
    value__ = ...


class enum_BP_COND_STYLE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_BP_COND_STYLE, values: BP_COND_NONE (0), BP_COND_WHEN_CHANGED (2), BP_COND_WHEN_TRUE (1) """
    BP_COND_NONE: enum_BP_COND_STYLE = ...
    BP_COND_WHEN_CHANGED: enum_BP_COND_STYLE = ...
    BP_COND_WHEN_TRUE: enum_BP_COND_STYLE = ...
    value__ = ...


class enum_BP_ERROR_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BP_ERROR_TYPE, values: BPET_ALL (4294967295), BPET_GENERAL_ERROR (117440514), BPET_GENERAL_WARNING (117440513), BPET_NONE (0), BPET_SEV_GENERAL (117440512), BPET_SEV_HIGH (251658240), BPET_SEV_LOW (16777216), BPET_SEV_MASK (4294901760), BPET_TYPE_ERROR (2), BPET_TYPE_MASK (65535), BPET_TYPE_WARNING (1) """
    BPET_ALL: enum_BP_ERROR_TYPE = ...
    BPET_GENERAL_ERROR: enum_BP_ERROR_TYPE = ...
    BPET_GENERAL_WARNING: enum_BP_ERROR_TYPE = ...
    BPET_NONE: enum_BP_ERROR_TYPE = ...
    BPET_SEV_GENERAL: enum_BP_ERROR_TYPE = ...
    BPET_SEV_HIGH: enum_BP_ERROR_TYPE = ...
    BPET_SEV_LOW: enum_BP_ERROR_TYPE = ...
    BPET_SEV_MASK: enum_BP_ERROR_TYPE = ...
    BPET_TYPE_ERROR: enum_BP_ERROR_TYPE = ...
    BPET_TYPE_MASK: enum_BP_ERROR_TYPE = ...
    BPET_TYPE_WARNING: enum_BP_ERROR_TYPE = ...
    value__ = ...


class enum_BP_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BP_FLAGS, values: BP_FLAG_DONT_STOP (2), BP_FLAG_MAP_DOCPOSITION (1), BP_FLAG_NONE (0) """
    BP_FLAG_DONT_STOP: enum_BP_FLAGS = ...
    BP_FLAG_MAP_DOCPOSITION: enum_BP_FLAGS = ...
    BP_FLAG_NONE: enum_BP_FLAGS = ...
    value__ = ...


class enum_BP_LOCATION_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BP_LOCATION_TYPE, values: BPLT_ADDRESS (327680), BPLT_CODE_ADDRESS (327681), BPLT_CODE_CONTEXT (196609), BPLT_CODE_FILE_LINE (65537), BPLT_CODE_FUNC_OFFSET (131073), BPLT_CODE_STRING (262145), BPLT_CONTEXT (196608), BPLT_DATA_STRING (262146), BPLT_FILE_LINE (65536), BPLT_FUNC_OFFSET (131072), BPLT_LOCATION_TYPE_MASK (4294901760), BPLT_NONE (0), BPLT_RESOLUTION (393216), BPLT_STRING (262144), BPLT_TYPE_MASK (65535) """
    BPLT_ADDRESS: enum_BP_LOCATION_TYPE = ...
    BPLT_CODE_ADDRESS: enum_BP_LOCATION_TYPE = ...
    BPLT_CODE_CONTEXT: enum_BP_LOCATION_TYPE = ...
    BPLT_CODE_FILE_LINE: enum_BP_LOCATION_TYPE = ...
    BPLT_CODE_FUNC_OFFSET: enum_BP_LOCATION_TYPE = ...
    BPLT_CODE_STRING: enum_BP_LOCATION_TYPE = ...
    BPLT_CONTEXT: enum_BP_LOCATION_TYPE = ...
    BPLT_DATA_STRING: enum_BP_LOCATION_TYPE = ...
    BPLT_FILE_LINE: enum_BP_LOCATION_TYPE = ...
    BPLT_FUNC_OFFSET: enum_BP_LOCATION_TYPE = ...
    BPLT_LOCATION_TYPE_MASK: enum_BP_LOCATION_TYPE = ...
    BPLT_NONE: enum_BP_LOCATION_TYPE = ...
    BPLT_RESOLUTION: enum_BP_LOCATION_TYPE = ...
    BPLT_STRING: enum_BP_LOCATION_TYPE = ...
    BPLT_TYPE_MASK: enum_BP_LOCATION_TYPE = ...
    value__ = ...


class enum_BP_PASSCOUNT_STYLE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_BP_PASSCOUNT_STYLE, values: BP_PASSCOUNT_EQUAL (1), BP_PASSCOUNT_EQUAL_OR_GREATER (2), BP_PASSCOUNT_MOD (3), BP_PASSCOUNT_NONE (0) """
    BP_PASSCOUNT_EQUAL: enum_BP_PASSCOUNT_STYLE = ...
    BP_PASSCOUNT_EQUAL_OR_GREATER: enum_BP_PASSCOUNT_STYLE = ...
    BP_PASSCOUNT_MOD: enum_BP_PASSCOUNT_STYLE = ...
    BP_PASSCOUNT_NONE: enum_BP_PASSCOUNT_STYLE = ...
    value__ = ...


class enum_BP_RES_DATA_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_BP_RES_DATA_FLAGS, values: BP_RES_DATA_EMULATED (1) """
    BP_RES_DATA_EMULATED: enum_BP_RES_DATA_FLAGS = ...
    value__ = ...


class enum_BP_STATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_BP_STATE, values: BPS_DELETED (1), BPS_DISABLED (2), BPS_ENABLED (3), BPS_NONE (0) """
    BPS_DELETED: enum_BP_STATE = ...
    BPS_DISABLED: enum_BP_STATE = ...
    BPS_ENABLED: enum_BP_STATE = ...
    BPS_NONE: enum_BP_STATE = ...
    value__ = ...


class enum_BP_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_BP_TYPE, values: BPT_CODE (1), BPT_DATA (2), BPT_NONE (0), BPT_SPECIAL (3) """
    BPT_CODE: enum_BP_TYPE = ...
    BPT_DATA: enum_BP_TYPE = ...
    BPT_NONE: enum_BP_TYPE = ...
    BPT_SPECIAL: enum_BP_TYPE = ...
    value__ = ...


class enum_BrowsableKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_BrowsableKind, values: BrowsableKind_Collapsed (2), BrowsableKind_Never (4), BrowsableKind_None (1), BrowsableKind_RootHidden (3) """
    BrowsableKind_Collapsed: enum_BrowsableKind = ...
    BrowsableKind_Never: enum_BrowsableKind = ...
    BrowsableKind_None: enum_BrowsableKind = ...
    BrowsableKind_RootHidden: enum_BrowsableKind = ...
    value__ = ...


class enum_CANSTOP_REASON(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_CANSTOP_REASON, values: CANSTOP_ENTRYPOINT (0), CANSTOP_STEPIN (1) """
    CANSTOP_ENTRYPOINT: enum_CANSTOP_REASON = ...
    CANSTOP_STEPIN: enum_CANSTOP_REASON = ...
    value__ = ...


class enum_CONTEXT_COMPARE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_CONTEXT_COMPARE, values: CONTEXT_EQUAL (1), CONTEXT_GREATER_THAN (3), CONTEXT_GREATER_THAN_OR_EQUAL (5), CONTEXT_LESS_THAN (2), CONTEXT_LESS_THAN_OR_EQUAL (4), CONTEXT_SAME_FUNCTION (7), CONTEXT_SAME_MODULE (8), CONTEXT_SAME_PROCESS (9), CONTEXT_SAME_SCOPE (6) """
    CONTEXT_EQUAL: enum_CONTEXT_COMPARE = ...
    CONTEXT_GREATER_THAN: enum_CONTEXT_COMPARE = ...
    CONTEXT_GREATER_THAN_OR_EQUAL: enum_CONTEXT_COMPARE = ...
    CONTEXT_LESS_THAN: enum_CONTEXT_COMPARE = ...
    CONTEXT_LESS_THAN_OR_EQUAL: enum_CONTEXT_COMPARE = ...
    CONTEXT_SAME_FUNCTION: enum_CONTEXT_COMPARE = ...
    CONTEXT_SAME_MODULE: enum_CONTEXT_COMPARE = ...
    CONTEXT_SAME_PROCESS: enum_CONTEXT_COMPARE = ...
    CONTEXT_SAME_SCOPE: enum_CONTEXT_COMPARE = ...
    value__ = ...


class enum_CONTEXT_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_CONTEXT_INFO_FIELDS, values: CIF_ADDRESS (8), CIF_ADDRESSABSOLUTE (32), CIF_ADDRESSOFFSET (16), CIF_ALLFIELDS (63), CIF_FUNCTION (2), CIF_FUNCTIONOFFSET (4), CIF_MODULEURL (1) """
    CIF_ADDRESS: enum_CONTEXT_INFO_FIELDS = ...
    CIF_ADDRESSABSOLUTE: enum_CONTEXT_INFO_FIELDS = ...
    CIF_ADDRESSOFFSET: enum_CONTEXT_INFO_FIELDS = ...
    CIF_ALLFIELDS: enum_CONTEXT_INFO_FIELDS = ...
    CIF_FUNCTION: enum_CONTEXT_INFO_FIELDS = ...
    CIF_FUNCTIONOFFSET: enum_CONTEXT_INFO_FIELDS = ...
    CIF_MODULEURL: enum_CONTEXT_INFO_FIELDS = ...
    value__ = ...


class enum_DBGPROP_ATTRIB_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DBGPROP_ATTRIB_FLAGS, values: DBGPROP_ATTRIB_ACCESS_FINAL (32768), DBGPROP_ATTRIB_ACCESS_PRIVATE (8192), DBGPROP_ATTRIB_ACCESS_PROTECTED (16384), DBGPROP_ATTRIB_ACCESS_PUBLIC (4096), DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS (8388608), DBGPROP_ATTRIB_NO_ATTRIB (0), DBGPROP_ATTRIB_STORAGE_FIELD (262144), DBGPROP_ATTRIB_STORAGE_GLOBAL (65536), DBGPROP_ATTRIB_STORAGE_STATIC (131072), DBGPROP_ATTRIB_STORAGE_VIRTUAL (524288), DBGPROP_ATTRIB_TYPE_IS_CONSTANT (1048576), DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED (2097152), DBGPROP_ATTRIB_TYPE_IS_VOLATILE (4194304), DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE (16), DBGPROP_ATTRIB_VALUE_IS_INVALID (8), DBGPROP_ATTRIB_VALUE_READONLY (2048) """
    DBGPROP_ATTRIB_ACCESS_FINAL: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_ACCESS_PRIVATE: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_ACCESS_PROTECTED: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_ACCESS_PUBLIC: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_NO_ATTRIB: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_STORAGE_FIELD: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_STORAGE_GLOBAL: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_STORAGE_STATIC: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_STORAGE_VIRTUAL: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_TYPE_IS_CONSTANT: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_TYPE_IS_VOLATILE: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_VALUE_IS_INVALID: enum_DBGPROP_ATTRIB_FLAGS = ...
    DBGPROP_ATTRIB_VALUE_READONLY: enum_DBGPROP_ATTRIB_FLAGS = ...
    value__ = ...


class enum_DBGPROP_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DBGPROP_INFO_FLAGS, values: DBGPROP_INFO_ATTRIBUTES (8), DBGPROP_INFO_AUTOEXPAND (134217728), DBGPROP_INFO_DEBUGPROP (16), DBGPROP_INFO_FULLNAME (32), DBGPROP_INFO_NAME (1), DBGPROP_INFO_TYPE (2), DBGPROP_INFO_VALUE (4) """
    DBGPROP_INFO_ATTRIBUTES: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_AUTOEXPAND: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_DEBUGPROP: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_FULLNAME: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_NAME: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_TYPE: enum_DBGPROP_INFO_FLAGS = ...
    DBGPROP_INFO_VALUE: enum_DBGPROP_INFO_FLAGS = ...
    value__ = ...


class enum_DEBUGPROP_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DEBUGPROP_INFO_FLAGS, values: DEBUGPROP_INFO_ALL (4294967295), DEBUGPROP_INFO_ATTRIB (16), DEBUGPROP_INFO_FULLNAME (1), DEBUGPROP_INFO_NAME (2), DEBUGPROP_INFO_NO_NONPUBLIC_MEMBERS (1048576), DEBUGPROP_INFO_NOFUNCEVAL (131072), DEBUGPROP_INFO_NONE (0), DEBUGPROP_INFO_PROP (32), DEBUGPROP_INFO_STANDARD (30), DEBUGPROP_INFO_TYPE (4), DEBUGPROP_INFO_VALUE (8), DEBUGPROP_INFO_VALUE_AUTOEXPAND (65536), DEBUGPROP_INFO_VALUE_NO_TOSTRING (524288), DEBUGPROP_INFO_VALUE_RAW (262144) """
    DEBUGPROP_INFO_ALL: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_ATTRIB: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_FULLNAME: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_NAME: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_NOFUNCEVAL: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_NONE: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_NO_NONPUBLIC_MEMBERS: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_PROP: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_STANDARD: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_TYPE: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_VALUE: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_VALUE_AUTOEXPAND: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_VALUE_NO_TOSTRING: enum_DEBUGPROP_INFO_FLAGS = ...
    DEBUGPROP_INFO_VALUE_RAW: enum_DEBUGPROP_INFO_FLAGS = ...
    value__ = ...


class enum_DEBUGREF_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DEBUGREF_INFO_FLAGS, values: DEBUGREF_INFO_ALL (4294967295), DEBUGREF_INFO_ATTRIB (8), DEBUGREF_INFO_NAME (1), DEBUGREF_INFO_NONE (0), DEBUGREF_INFO_REF (32), DEBUGREF_INFO_REFTYPE (16), DEBUGREF_INFO_TYPE (2), DEBUGREF_INFO_VALUE (4), DEBUGREF_INFO_VALUE_AUTOEXPAND (65536) """
    DEBUGREF_INFO_ALL: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_ATTRIB: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_NAME: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_NONE: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_REF: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_REFTYPE: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_TYPE: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_VALUE: enum_DEBUGREF_INFO_FLAGS = ...
    DEBUGREF_INFO_VALUE_AUTOEXPAND: enum_DEBUGREF_INFO_FLAGS = ...
    value__ = ...


class enum_DEBUG_REASON(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_DEBUG_REASON, values: DEBUG_REASON_AUTO_ATTACHED (3), DEBUG_REASON_CAUSALITY (4), DEBUG_REASON_ERROR (0), DEBUG_REASON_USER_ATTACHED (2), DEBUG_REASON_USER_LAUNCHED (1) """
    DEBUG_REASON_AUTO_ATTACHED: enum_DEBUG_REASON = ...
    DEBUG_REASON_CAUSALITY: enum_DEBUG_REASON = ...
    DEBUG_REASON_ERROR: enum_DEBUG_REASON = ...
    DEBUG_REASON_USER_ATTACHED: enum_DEBUG_REASON = ...
    DEBUG_REASON_USER_LAUNCHED: enum_DEBUG_REASON = ...
    value__ = ...


class enum_DISASSEMBLY_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DISASSEMBLY_FLAGS, values: DF_DATA (8), DF_DISABLED (2), DF_DOCUMENT_CHECKSUM (32), DF_DOCUMENTCHANGE (1), DF_HASSOURCE (16), DF_INSTRUCTION_ACTIVE (4) """
    DF_DATA: enum_DISASSEMBLY_FLAGS = ...
    DF_DISABLED: enum_DISASSEMBLY_FLAGS = ...
    DF_DOCUMENTCHANGE: enum_DISASSEMBLY_FLAGS = ...
    DF_DOCUMENT_CHECKSUM: enum_DISASSEMBLY_FLAGS = ...
    DF_HASSOURCE: enum_DISASSEMBLY_FLAGS = ...
    DF_INSTRUCTION_ACTIVE: enum_DISASSEMBLY_FLAGS = ...
    value__ = ...


class enum_DISASSEMBLY_STREAM_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_DISASSEMBLY_STREAM_FIELDS, values: DSF_ADDRESS (1), DSF_ADDRESSOFFSET (2), DSF_ALL (67583), DSF_BYTEOFFSET (512), DSF_CODEBYTES (4), DSF_CODELOCATIONID (64), DSF_DOCUMENTURL (256), DSF_FLAGS (1024), DSF_OPCODE (8), DSF_OPERANDS (16), DSF_OPERANDS_SYMBOLS (65536), DSF_POSITION (128), DSF_SYMBOL (32) """
    DSF_ADDRESS: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_ADDRESSOFFSET: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_ALL: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_BYTEOFFSET: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_CODEBYTES: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_CODELOCATIONID: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_DOCUMENTURL: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_FLAGS: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_OPCODE: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_OPERANDS: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_OPERANDS_SYMBOLS: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_POSITION: enum_DISASSEMBLY_STREAM_FIELDS = ...
    DSF_SYMBOL: enum_DISASSEMBLY_STREAM_FIELDS = ...
    value__ = ...


class enum_DISASSEMBLY_STREAM_SCOPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_DISASSEMBLY_STREAM_SCOPE, values: DSS_ALL (268435459), DSS_FUNCTION (1), DSS_HUGE (268435456), DSS_MODULE (268435458) """
    DSS_ALL: enum_DISASSEMBLY_STREAM_SCOPE = ...
    DSS_FUNCTION: enum_DISASSEMBLY_STREAM_SCOPE = ...
    DSS_HUGE: enum_DISASSEMBLY_STREAM_SCOPE = ...
    DSS_MODULE: enum_DISASSEMBLY_STREAM_SCOPE = ...
    value__ = ...


class enum_DisplayKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_DisplayKind, values: DisplayKind_Name (2), DisplayKind_Type (3), DisplayKind_Value (1) """
    DisplayKind_Name: enum_DisplayKind = ...
    DisplayKind_Type: enum_DisplayKind = ...
    DisplayKind_Value: enum_DisplayKind = ...
    value__ = ...


class enum_dwTYPE_KIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_dwTYPE_KIND, values: TYPE_KIND_BUILT (3), TYPE_KIND_METADATA (1), TYPE_KIND_PDB (2) """
    TYPE_KIND_BUILT: enum_dwTYPE_KIND = ...
    TYPE_KIND_METADATA: enum_dwTYPE_KIND = ...
    TYPE_KIND_PDB: enum_dwTYPE_KIND = ...
    value__ = ...


class enum_ENUMERATED_PROCESS_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_ENUMERATED_PROCESS_FLAGS, values: EPFLAG_SHOW_SECURITY_WARNING (1), EPFLAG_SYSTEM_PROCESS (2) """
    EPFLAG_SHOW_SECURITY_WARNING: enum_ENUMERATED_PROCESS_FLAGS = ...
    EPFLAG_SYSTEM_PROCESS: enum_ENUMERATED_PROCESS_FLAGS = ...
    value__ = ...


class enum_EVALFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_EVALFLAGS, values: EVAL_ALLOW_IMPLICIT_VARS (16384), EVAL_ALLOWBPS (8), EVAL_ALLOWERRORREPORT (16), EVAL_DESIGN_TIME_EXPR_EVAL (8192), EVAL_FUNCTION_AS_ADDRESS (64), EVAL_NOEVENTS (4096), EVAL_NOFUNCEVAL (128), EVAL_NOSIDEEFFECTS (4), EVAL_RETURNVALUE (2) """
    EVAL_ALLOWBPS: enum_EVALFLAGS = ...
    EVAL_ALLOWERRORREPORT: enum_EVALFLAGS = ...
    EVAL_ALLOW_IMPLICIT_VARS: enum_EVALFLAGS = ...
    EVAL_DESIGN_TIME_EXPR_EVAL: enum_EVALFLAGS = ...
    EVAL_FUNCTION_AS_ADDRESS: enum_EVALFLAGS = ...
    EVAL_NOEVENTS: enum_EVALFLAGS = ...
    EVAL_NOFUNCEVAL: enum_EVALFLAGS = ...
    EVAL_NOSIDEEFFECTS: enum_EVALFLAGS = ...
    EVAL_RETURNVALUE: enum_EVALFLAGS = ...
    value__ = ...


class enum_EVENTATTRIBUTES(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_EVENTATTRIBUTES, values: EVENT_ASYNC_STOP (2), EVENT_ASYNCHRONOUS (0), EVENT_EXPRESSION_EVALUATION (8), EVENT_IMMEDIATE (4), EVENT_STOPPING (2), EVENT_SYNC_STOP (3), EVENT_SYNCHRONOUS (1) """
    EVENT_ASYNCHRONOUS: enum_EVENTATTRIBUTES = ...
    EVENT_ASYNC_STOP: enum_EVENTATTRIBUTES = ...
    EVENT_EXPRESSION_EVALUATION: enum_EVENTATTRIBUTES = ...
    EVENT_IMMEDIATE: enum_EVENTATTRIBUTES = ...
    EVENT_STOPPING: enum_EVENTATTRIBUTES = ...
    EVENT_SYNCHRONOUS: enum_EVENTATTRIBUTES = ...
    EVENT_SYNC_STOP: enum_EVENTATTRIBUTES = ...
    value__ = ...


class enum_EXCEPTION_STATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_EXCEPTION_STATE, values: EXCEPTION_CANNOT_BE_CONTINUED (256), EXCEPTION_CODE_DISPLAY_IN_HEX (8192), EXCEPTION_CODE_SUPPORTED (4096), EXCEPTION_JUST_MY_CODE_SUPPORTED (16384), EXCEPTION_MANAGED_DEBUG_ASSISTANT (32768), EXCEPTION_NONE (0), EXCEPTION_STOP_ALL (255), EXCEPTION_STOP_FIRST_CHANCE (1), EXCEPTION_STOP_FIRST_CHANCE_USE_PARENT (4), EXCEPTION_STOP_SECOND_CHANCE (2), EXCEPTION_STOP_SECOND_CHANCE_USE_PARENT (8), EXCEPTION_STOP_USER_FIRST_CHANCE (16), EXCEPTION_STOP_USER_FIRST_CHANCE_USE_PARENT (64), EXCEPTION_STOP_USER_UNCAUGHT (32), EXCEPTION_STOP_USER_UNCAUGHT_USE_PARENT (128) """
    EXCEPTION_CANNOT_BE_CONTINUED: enum_EXCEPTION_STATE = ...
    EXCEPTION_CODE_DISPLAY_IN_HEX: enum_EXCEPTION_STATE = ...
    EXCEPTION_CODE_SUPPORTED: enum_EXCEPTION_STATE = ...
    EXCEPTION_JUST_MY_CODE_SUPPORTED: enum_EXCEPTION_STATE = ...
    EXCEPTION_MANAGED_DEBUG_ASSISTANT: enum_EXCEPTION_STATE = ...
    EXCEPTION_NONE: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_ALL: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_FIRST_CHANCE: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_FIRST_CHANCE_USE_PARENT: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_SECOND_CHANCE: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_SECOND_CHANCE_USE_PARENT: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_USER_FIRST_CHANCE: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_USER_FIRST_CHANCE_USE_PARENT: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_USER_UNCAUGHT: enum_EXCEPTION_STATE = ...
    EXCEPTION_STOP_USER_UNCAUGHT_USE_PARENT: enum_EXCEPTION_STATE = ...
    value__ = ...


class enum_EX_DBGPROP_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_EX_DBGPROP_INFO_FLAGS, values: EX_DBGPROP_INFO_DEBUGEXTPROP (4096), EX_DBGPROP_INFO_ID (256), EX_DBGPROP_INFO_LOCKBYTES (2048), EX_DBGPROP_INFO_NTYPE (512), EX_DBGPROP_INFO_NVALUE (1024) """
    EX_DBGPROP_INFO_DEBUGEXTPROP: enum_EX_DBGPROP_INFO_FLAGS = ...
    EX_DBGPROP_INFO_ID: enum_EX_DBGPROP_INFO_FLAGS = ...
    EX_DBGPROP_INFO_LOCKBYTES: enum_EX_DBGPROP_INFO_FLAGS = ...
    EX_DBGPROP_INFO_NTYPE: enum_EX_DBGPROP_INFO_FLAGS = ...
    EX_DBGPROP_INFO_NVALUE: enum_EX_DBGPROP_INFO_FLAGS = ...
    value__ = ...


class enum_FIELD_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FIELD_INFO_FIELDS, values: FIF_ALL (4294967295), FIF_FULLNAME (1), FIF_MODIFIERS (8), FIF_NAME (2), FIF_TYPE (4) """
    FIF_ALL: enum_FIELD_INFO_FIELDS = ...
    FIF_FULLNAME: enum_FIELD_INFO_FIELDS = ...
    FIF_MODIFIERS: enum_FIELD_INFO_FIELDS = ...
    FIF_NAME: enum_FIELD_INFO_FIELDS = ...
    FIF_TYPE: enum_FIELD_INFO_FIELDS = ...
    value__ = ...


class enum_FIELD_KIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FIELD_KIND, values: FIELD_KIND_ALL (4294967295), FIELD_KIND_MASK (15), FIELD_KIND_NONE (0), FIELD_KIND_SYMBOL (2), FIELD_KIND_TYPE (1), FIELD_SYM_EXTENED (2147483648), FIELD_SYM_GLOBAL (268435456), FIELD_SYM_LOCAL (33554432), FIELD_SYM_MASK (4278190080), FIELD_SYM_MEMBER (16777216), FIELD_SYM_PARAM (67108864), FIELD_SYM_PROP_GETTER (536870912), FIELD_SYM_PROP_SETTER (1073741824), FIELD_SYM_THIS (134217728), FIELD_TYPE_ARRAY (512), FIELD_TYPE_BITFIELD (65536), FIELD_TYPE_BLOCK (2048), FIELD_TYPE_CLASS (64), FIELD_TYPE_DYNAMIC (524288), FIELD_TYPE_ENUM (8192), FIELD_TYPE_EXTENDED (8388608), FIELD_TYPE_INNERCLASS (2097152), FIELD_TYPE_INTERFACE (128), FIELD_TYPE_LABEL (16384), FIELD_TYPE_MASK (16777200), FIELD_TYPE_METHOD (1024), FIELD_TYPE_MODULE (262144), FIELD_TYPE_NAMESPACE (131072), FIELD_TYPE_POINTER (4096), FIELD_TYPE_PRIMITIVE (16), FIELD_TYPE_PROP (1048576), FIELD_TYPE_REFERENCE (4194304), FIELD_TYPE_STRUCT (32), FIELD_TYPE_TYPEDEF (32768), FIELD_TYPE_UNION (256) """
    FIELD_KIND_ALL: enum_FIELD_KIND = ...
    FIELD_KIND_MASK: enum_FIELD_KIND = ...
    FIELD_KIND_NONE: enum_FIELD_KIND = ...
    FIELD_KIND_SYMBOL: enum_FIELD_KIND = ...
    FIELD_KIND_TYPE: enum_FIELD_KIND = ...
    FIELD_SYM_EXTENED: enum_FIELD_KIND = ...
    FIELD_SYM_GLOBAL: enum_FIELD_KIND = ...
    FIELD_SYM_LOCAL: enum_FIELD_KIND = ...
    FIELD_SYM_MASK: enum_FIELD_KIND = ...
    FIELD_SYM_MEMBER: enum_FIELD_KIND = ...
    FIELD_SYM_PARAM: enum_FIELD_KIND = ...
    FIELD_SYM_PROP_GETTER: enum_FIELD_KIND = ...
    FIELD_SYM_PROP_SETTER: enum_FIELD_KIND = ...
    FIELD_SYM_THIS: enum_FIELD_KIND = ...
    FIELD_TYPE_ARRAY: enum_FIELD_KIND = ...
    FIELD_TYPE_BITFIELD: enum_FIELD_KIND = ...
    FIELD_TYPE_BLOCK: enum_FIELD_KIND = ...
    FIELD_TYPE_CLASS: enum_FIELD_KIND = ...
    FIELD_TYPE_DYNAMIC: enum_FIELD_KIND = ...
    FIELD_TYPE_ENUM: enum_FIELD_KIND = ...
    FIELD_TYPE_EXTENDED: enum_FIELD_KIND = ...
    FIELD_TYPE_INNERCLASS: enum_FIELD_KIND = ...
    FIELD_TYPE_INTERFACE: enum_FIELD_KIND = ...
    FIELD_TYPE_LABEL: enum_FIELD_KIND = ...
    FIELD_TYPE_MASK: enum_FIELD_KIND = ...
    FIELD_TYPE_METHOD: enum_FIELD_KIND = ...
    FIELD_TYPE_MODULE: enum_FIELD_KIND = ...
    FIELD_TYPE_NAMESPACE: enum_FIELD_KIND = ...
    FIELD_TYPE_POINTER: enum_FIELD_KIND = ...
    FIELD_TYPE_PRIMITIVE: enum_FIELD_KIND = ...
    FIELD_TYPE_PROP: enum_FIELD_KIND = ...
    FIELD_TYPE_REFERENCE: enum_FIELD_KIND = ...
    FIELD_TYPE_STRUCT: enum_FIELD_KIND = ...
    FIELD_TYPE_TYPEDEF: enum_FIELD_KIND = ...
    FIELD_TYPE_UNION: enum_FIELD_KIND = ...
    value__ = ...


class enum_FIELD_KIND_EX(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FIELD_KIND_EX, values: FIELD_KIND_EX_NONE (0), FIELD_TYPE_EX_CLASSVAR (2), FIELD_TYPE_EX_METHODVAR (1) """
    FIELD_KIND_EX_NONE: enum_FIELD_KIND_EX = ...
    FIELD_TYPE_EX_CLASSVAR: enum_FIELD_KIND_EX = ...
    FIELD_TYPE_EX_METHODVAR: enum_FIELD_KIND_EX = ...
    value__ = ...


class enum_FIELD_MODIFIERS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FIELD_MODIFIERS, values: FIELD_MOD_ABSTRACT (512), FIELD_MOD_ACCESS_FRIEND (16777216), FIELD_MOD_ACCESS_MASK (251658255), FIELD_MOD_ACCESS_NONE (1), FIELD_MOD_ACCESS_PRIVATE (8), FIELD_MOD_ACCESS_PROTECTED (4), FIELD_MOD_ACCESS_PUBLIC (2), FIELD_MOD_ALL (2147483647), FIELD_MOD_BYREF (262144), FIELD_MOD_CONSTANT (64), FIELD_MOD_FINAL (16384), FIELD_MOD_HIDDEN (524288), FIELD_MOD_HIDEBYSIG (4194304), FIELD_MOD_INNERCLASS (65536), FIELD_MOD_INTERFACE (8192), FIELD_MOD_MARSHALASOBJECT (1048576), FIELD_MOD_MASK (4043309040), FIELD_MOD_NATIVE (1024), FIELD_MOD_NEWSLOT (8388608), FIELD_MOD_NOMODIFIERS (16), FIELD_MOD_NONE (0), FIELD_MOD_OPTIONAL (131072), FIELD_MOD_SENTINEL (32768), FIELD_MOD_SPECIAL_NAME (2097152), FIELD_MOD_STATIC (32), FIELD_MOD_SYNCHRONIZED (2048), FIELD_MOD_TRANSIENT (128), FIELD_MOD_VIRTUAL (4096), FIELD_MOD_VOLATILE (256), FIELD_MOD_WRITEONLY (2147483648) """
    FIELD_MOD_ABSTRACT: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_FRIEND: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_MASK: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_NONE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_PRIVATE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_PROTECTED: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ACCESS_PUBLIC: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_ALL: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_BYREF: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_CONSTANT: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_FINAL: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_HIDDEN: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_HIDEBYSIG: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_INNERCLASS: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_INTERFACE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_MARSHALASOBJECT: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_MASK: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_NATIVE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_NEWSLOT: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_NOMODIFIERS: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_NONE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_OPTIONAL: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_SENTINEL: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_SPECIAL_NAME: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_STATIC: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_SYNCHRONIZED: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_TRANSIENT: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_VIRTUAL: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_VOLATILE: enum_FIELD_MODIFIERS = ...
    FIELD_MOD_WRITEONLY: enum_FIELD_MODIFIERS = ...
    value__ = ...


class enum_FRAMEINFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FRAMEINFO_FLAGS, values: FIF_ARGS (4), FIF_ARGS_ALL (117440512), FIF_ARGS_NAMES (33554432), FIF_ARGS_NO_FUNC_EVAL (268435456), FIF_ARGS_NO_TOSTRING (1073741824), FIF_ARGS_NOFORMAT (134217728), FIF_ARGS_TYPES (16777216), FIF_ARGS_VALUES (67108864), FIF_DEBUG_MODULEP (1024), FIF_DEBUGINFO (128), FIF_DESIGN_TIME_EXPR_EVAL (2147483648), FIF_FILTER_INCLUDE_ALL (524288), FIF_FILTER_NON_USER_CODE (536870912), FIF_FLAGS (512), FIF_FRAME (64), FIF_FUNCNAME (1), FIF_FUNCNAME_ARGS (16384), FIF_FUNCNAME_ARGS_ALL (7340032), FIF_FUNCNAME_ARGS_NAMES (2097152), FIF_FUNCNAME_ARGS_TYPES (1048576), FIF_FUNCNAME_ARGS_VALUES (4194304), FIF_FUNCNAME_FORMAT (4096), FIF_FUNCNAME_LANGUAGE (32768), FIF_FUNCNAME_LINES (131072), FIF_FUNCNAME_MODULE (65536), FIF_FUNCNAME_OFFSET (262144), FIF_FUNCNAME_RETURNTYPE (8192), FIF_LANGUAGE (8), FIF_MODULE (16), FIF_RETURNTYPE (2), FIF_STACKRANGE (32), FIF_STALECODE (256) """
    FIF_ARGS: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_ALL: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_NAMES: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_NOFORMAT: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_NO_FUNC_EVAL: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_NO_TOSTRING: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_TYPES: enum_FRAMEINFO_FLAGS = ...
    FIF_ARGS_VALUES: enum_FRAMEINFO_FLAGS = ...
    FIF_DEBUGINFO: enum_FRAMEINFO_FLAGS = ...
    FIF_DEBUG_MODULEP: enum_FRAMEINFO_FLAGS = ...
    FIF_DESIGN_TIME_EXPR_EVAL: enum_FRAMEINFO_FLAGS = ...
    FIF_FILTER_INCLUDE_ALL: enum_FRAMEINFO_FLAGS = ...
    FIF_FILTER_NON_USER_CODE: enum_FRAMEINFO_FLAGS = ...
    FIF_FLAGS: enum_FRAMEINFO_FLAGS = ...
    FIF_FRAME: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_ARGS: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_ARGS_ALL: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_ARGS_NAMES: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_ARGS_TYPES: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_ARGS_VALUES: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_FORMAT: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_LANGUAGE: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_LINES: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_MODULE: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_OFFSET: enum_FRAMEINFO_FLAGS = ...
    FIF_FUNCNAME_RETURNTYPE: enum_FRAMEINFO_FLAGS = ...
    FIF_LANGUAGE: enum_FRAMEINFO_FLAGS = ...
    FIF_MODULE: enum_FRAMEINFO_FLAGS = ...
    FIF_RETURNTYPE: enum_FRAMEINFO_FLAGS = ...
    FIF_STACKRANGE: enum_FRAMEINFO_FLAGS = ...
    FIF_STALECODE: enum_FRAMEINFO_FLAGS = ...
    value__ = ...


class enum_FRAMEINFO_FLAGS_VALUES(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_FRAMEINFO_FLAGS_VALUES, values: FIFV_ANNOTATEDFRAME (1), FIFV_CANINTERCEPT_EXCEPTION (4), FIFV_FUNCEVALFRAME (8), FIFV_NON_USER_CODE (2) """
    FIFV_ANNOTATEDFRAME: enum_FRAMEINFO_FLAGS_VALUES = ...
    FIFV_CANINTERCEPT_EXCEPTION: enum_FRAMEINFO_FLAGS_VALUES = ...
    FIFV_FUNCEVALFRAME: enum_FRAMEINFO_FLAGS_VALUES = ...
    FIFV_NON_USER_CODE: enum_FRAMEINFO_FLAGS_VALUES = ...
    value__ = ...


class enum_GETASSEMBLY(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_GETASSEMBLY, values: GA_BYTES (1), GA_FLAGS (8), GA_NAME (4), GA_PDBBYTES (2) """
    GA_BYTES: enum_GETASSEMBLY = ...
    GA_FLAGS: enum_GETASSEMBLY = ...
    GA_NAME: enum_GETASSEMBLY = ...
    GA_PDBBYTES: enum_GETASSEMBLY = ...
    value__ = ...


class enum_GETHOSTNAME_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_GETHOSTNAME_TYPE, values: GHN_FILE_NAME (1), GHN_FRIENDLY_NAME (0) """
    GHN_FILE_NAME: enum_GETHOSTNAME_TYPE = ...
    GHN_FRIENDLY_NAME: enum_GETHOSTNAME_TYPE = ...
    value__ = ...


class enum_GETNAME_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_GETNAME_TYPE, values: GN_BASENAME (2), GN_FILENAME (1), GN_MONIKERNAME (3), GN_NAME (0), GN_STARTPAGEURL (6), GN_TITLE (5), GN_URL (4) """
    GN_BASENAME: enum_GETNAME_TYPE = ...
    GN_FILENAME: enum_GETNAME_TYPE = ...
    GN_MONIKERNAME: enum_GETNAME_TYPE = ...
    GN_NAME: enum_GETNAME_TYPE = ...
    GN_STARTPAGEURL: enum_GETNAME_TYPE = ...
    GN_TITLE: enum_GETNAME_TYPE = ...
    GN_URL: enum_GETNAME_TYPE = ...
    value__ = ...


class enum_INTERCEPT_EXCEPTION_ACTION(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_INTERCEPT_EXCEPTION_ACTION, values: IEA_CANCEL_INTERCEPT (0), IEA_INTERCEPT (1) """
    IEA_CANCEL_INTERCEPT: enum_INTERCEPT_EXCEPTION_ACTION = ...
    IEA_INTERCEPT: enum_INTERCEPT_EXCEPTION_ACTION = ...
    value__ = ...


class enum_JIT_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_JIT_FLAGS, values: JIT_FLAG_DEBUGEXE (4), JIT_FLAG_NOCRASH (2), JIT_FLAG_RPC (1), JIT_FLAG_SELECT_ENGINES (8) """
    JIT_FLAG_DEBUGEXE: enum_JIT_FLAGS = ...
    JIT_FLAG_NOCRASH: enum_JIT_FLAGS = ...
    JIT_FLAG_RPC: enum_JIT_FLAGS = ...
    JIT_FLAG_SELECT_ENGINES: enum_JIT_FLAGS = ...
    value__ = ...


class enum_LAUNCH_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_LAUNCH_FLAGS, values: LAUNCH_DEBUG (0), LAUNCH_ENABLE_ENC (2), LAUNCH_MERGE_ENV (4), LAUNCH_NODEBUG (1) """
    LAUNCH_DEBUG: enum_LAUNCH_FLAGS = ...
    LAUNCH_ENABLE_ENC: enum_LAUNCH_FLAGS = ...
    LAUNCH_MERGE_ENV: enum_LAUNCH_FLAGS = ...
    LAUNCH_NODEBUG: enum_LAUNCH_FLAGS = ...
    value__ = ...


class enum_MACHINE_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MACHINE_INFO_FIELDS, values: MCIF_ALL (3), MCIF_FLAGS (2), MCIF_NAME (1) """
    MCIF_ALL: enum_MACHINE_INFO_FIELDS = ...
    MCIF_FLAGS: enum_MACHINE_INFO_FIELDS = ...
    MCIF_NAME: enum_MACHINE_INFO_FIELDS = ...
    value__ = ...


class enum_MACHINE_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MACHINE_INFO_FLAGS, values: MCIFLAG_TERMINAL_SERVICES_AVAILABLE (1) """
    MCIFLAG_TERMINAL_SERVICES_AVAILABLE: enum_MACHINE_INFO_FLAGS = ...
    value__ = ...


class enum_MESSAGETYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MESSAGETYPE, values: MT_MESSAGEBOX (2), MT_OUTPUTSTRING (1), MT_REASON_EXCEPTION (256), MT_REASON_MASK (65280), MT_REASON_TRACEPOINT (512), MT_TYPE_MASK (255) """
    MT_MESSAGEBOX: enum_MESSAGETYPE = ...
    MT_OUTPUTSTRING: enum_MESSAGETYPE = ...
    MT_REASON_EXCEPTION: enum_MESSAGETYPE = ...
    MT_REASON_MASK: enum_MESSAGETYPE = ...
    MT_REASON_TRACEPOINT: enum_MESSAGETYPE = ...
    MT_TYPE_MASK: enum_MESSAGETYPE = ...
    value__ = ...


class enum_MODULE_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MODULE_FLAGS, values: MODULE_FLAG_64BIT (4), MODULE_FLAG_NONE (0), MODULE_FLAG_OPTIMIZED (8), MODULE_FLAG_SYMBOLS (2), MODULE_FLAG_SYSTEM (1), MODULE_FLAG_UNOPTIMIZED (16) """
    MODULE_FLAG_64BIT: enum_MODULE_FLAGS = ...
    MODULE_FLAG_NONE: enum_MODULE_FLAGS = ...
    MODULE_FLAG_OPTIMIZED: enum_MODULE_FLAGS = ...
    MODULE_FLAG_SYMBOLS: enum_MODULE_FLAGS = ...
    MODULE_FLAG_SYSTEM: enum_MODULE_FLAGS = ...
    MODULE_FLAG_UNOPTIMIZED: enum_MODULE_FLAGS = ...
    value__ = ...


class enum_MODULE_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MODULE_INFO_FIELDS, values: MIF_ALLFIELDS (2047), MIF_DEBUGMESSAGE (8), MIF_FLAGS (1024), MIF_LOADADDRESS (16), MIF_LOADORDER (128), MIF_NAME (1), MIF_NONE (0), MIF_PREFFEREDADDRESS (32), MIF_SIZE (64), MIF_TIMESTAMP (256), MIF_URL (2), MIF_URLSYMBOLLOCATION (512), MIF_VERSION (4) """
    MIF_ALLFIELDS: enum_MODULE_INFO_FIELDS = ...
    MIF_DEBUGMESSAGE: enum_MODULE_INFO_FIELDS = ...
    MIF_FLAGS: enum_MODULE_INFO_FIELDS = ...
    MIF_LOADADDRESS: enum_MODULE_INFO_FIELDS = ...
    MIF_LOADORDER: enum_MODULE_INFO_FIELDS = ...
    MIF_NAME: enum_MODULE_INFO_FIELDS = ...
    MIF_NONE: enum_MODULE_INFO_FIELDS = ...
    MIF_PREFFEREDADDRESS: enum_MODULE_INFO_FIELDS = ...
    MIF_SIZE: enum_MODULE_INFO_FIELDS = ...
    MIF_TIMESTAMP: enum_MODULE_INFO_FIELDS = ...
    MIF_URL: enum_MODULE_INFO_FIELDS = ...
    MIF_URLSYMBOLLOCATION: enum_MODULE_INFO_FIELDS = ...
    MIF_VERSION: enum_MODULE_INFO_FIELDS = ...
    value__ = ...


class enum_MODULE_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_MODULE_INFO_FLAGS, values: MIF_SYMBOLS_LOADED (1) """
    MIF_SYMBOLS_LOADED: enum_MODULE_INFO_FLAGS = ...
    value__ = ...


class enum_OBJECT_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_OBJECT_TYPE, values: OBJECT_TYPE_BOOLEAN (0), OBJECT_TYPE_CHAR (1), OBJECT_TYPE_CLASS (14), OBJECT_TYPE_I1 (2), OBJECT_TYPE_I2 (4), OBJECT_TYPE_I4 (6), OBJECT_TYPE_I8 (8), OBJECT_TYPE_NULL (13), OBJECT_TYPE_OBJECT (12), OBJECT_TYPE_R4 (10), OBJECT_TYPE_R8 (11), OBJECT_TYPE_U1 (3), OBJECT_TYPE_U2 (5), OBJECT_TYPE_U4 (7), OBJECT_TYPE_U8 (9) """
    OBJECT_TYPE_BOOLEAN: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_CHAR: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_CLASS: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_I1: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_I2: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_I4: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_I8: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_NULL: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_OBJECT: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_R4: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_R8: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_U1: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_U2: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_U4: enum_OBJECT_TYPE = ...
    OBJECT_TYPE_U8: enum_OBJECT_TYPE = ...
    value__ = ...


class enum_PARSEFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PARSEFLAGS, values: PARSE_DESIGN_TIME_EXPR_EVAL (4096), PARSE_EXPRESSION (1), PARSE_FUNCTION_AS_ADDRESS (2) """
    PARSE_DESIGN_TIME_EXPR_EVAL: enum_PARSEFLAGS = ...
    PARSE_EXPRESSION: enum_PARSEFLAGS = ...
    PARSE_FUNCTION_AS_ADDRESS: enum_PARSEFLAGS = ...
    value__ = ...


class enum_PENDING_BP_STATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_PENDING_BP_STATE, values: PBPS_DELETED (1), PBPS_DISABLED (2), PBPS_ENABLED (3), PBPS_NONE (0) """
    PBPS_DELETED: enum_PENDING_BP_STATE = ...
    PBPS_DISABLED: enum_PENDING_BP_STATE = ...
    PBPS_ENABLED: enum_PENDING_BP_STATE = ...
    PBPS_NONE: enum_PENDING_BP_STATE = ...
    value__ = ...


class enum_PENDING_BP_STATE_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PENDING_BP_STATE_FLAGS, values: PBPSF_NONE (0), PBPSF_VIRTUALIZED (1) """
    PBPSF_NONE: enum_PENDING_BP_STATE_FLAGS = ...
    PBPSF_VIRTUALIZED: enum_PENDING_BP_STATE_FLAGS = ...
    value__ = ...


class enum_PORT_SUPPLIER_DESCRIPTION_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PORT_SUPPLIER_DESCRIPTION_FLAGS, values: PSDFLAG_SHOW_WARNING_ICON (1) """
    PSDFLAG_SHOW_WARNING_ICON: enum_PORT_SUPPLIER_DESCRIPTION_FLAGS = ...
    value__ = ...


class enum_PPROGRAM_DESTROY_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PPROGRAM_DESTROY_FLAGS, values: PROGRAM_DESTROY_CONTINUE_DEBUGGING (1) """
    PROGRAM_DESTROY_CONTINUE_DEBUGGING: enum_PPROGRAM_DESTROY_FLAGS = ...
    value__ = ...


class enum_PROCESS_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PROCESS_INFO_FIELDS, values: PIF_ALL (255), PIF_ATTACHED_SESSION_NAME (32), PIF_BASE_NAME (2), PIF_CREATION_TIME (64), PIF_FILE_NAME (1), PIF_FLAGS (128), PIF_PROCESS_ID (8), PIF_SESSION_ID (16), PIF_TITLE (4) """
    PIF_ALL: enum_PROCESS_INFO_FIELDS = ...
    PIF_ATTACHED_SESSION_NAME: enum_PROCESS_INFO_FIELDS = ...
    PIF_BASE_NAME: enum_PROCESS_INFO_FIELDS = ...
    PIF_CREATION_TIME: enum_PROCESS_INFO_FIELDS = ...
    PIF_FILE_NAME: enum_PROCESS_INFO_FIELDS = ...
    PIF_FLAGS: enum_PROCESS_INFO_FIELDS = ...
    PIF_PROCESS_ID: enum_PROCESS_INFO_FIELDS = ...
    PIF_SESSION_ID: enum_PROCESS_INFO_FIELDS = ...
    PIF_TITLE: enum_PROCESS_INFO_FIELDS = ...
    value__ = ...


class enum_PROCESS_INFO_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PROCESS_INFO_FLAGS, values: PIFLAG_DEBUGGER_ATTACHED (2), PIFLAG_PROCESS_RUNNING (8), PIFLAG_PROCESS_STOPPED (4), PIFLAG_SYSTEM_PROCESS (1) """
    PIFLAG_DEBUGGER_ATTACHED: enum_PROCESS_INFO_FLAGS = ...
    PIFLAG_PROCESS_RUNNING: enum_PROCESS_INFO_FLAGS = ...
    PIFLAG_PROCESS_STOPPED: enum_PROCESS_INFO_FLAGS = ...
    PIFLAG_SYSTEM_PROCESS: enum_PROCESS_INFO_FLAGS = ...
    value__ = ...


class enum_PROCESS_PROPERTY_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_PROCESS_PROPERTY_TYPE, values: PROCESS_PROPERTY_COMMAND_LINE (1), PROCESS_PROPERTY_CURRENT_DIRECTORY (2), PROCESS_PROPERTY_ENVIRONMENT_VARIABLES (3) """
    PROCESS_PROPERTY_COMMAND_LINE: enum_PROCESS_PROPERTY_TYPE = ...
    PROCESS_PROPERTY_CURRENT_DIRECTORY: enum_PROCESS_PROPERTY_TYPE = ...
    PROCESS_PROPERTY_ENVIRONMENT_VARIABLES: enum_PROCESS_PROPERTY_TYPE = ...
    value__ = ...


class enum_PROVIDER_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PROVIDER_FIELDS, values: PFIELD_IS_DEBUGGER_PRESENT (2), PFIELD_PROGRAM_NODES (1) """
    PFIELD_IS_DEBUGGER_PRESENT: enum_PROVIDER_FIELDS = ...
    PFIELD_PROGRAM_NODES: enum_PROVIDER_FIELDS = ...
    value__ = ...


class enum_PROVIDER_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_PROVIDER_FLAGS, values: PFLAG_ATTACHED_TO_DEBUGGEE (4), PFLAG_DEBUGGEE (2), PFLAG_GET_IS_DEBUGGER_PRESENT (32), PFLAG_GET_PROGRAM_NODES (16), PFLAG_NONE (0), PFLAG_REASON_WATCH (8), PFLAG_REMOTE_PORT (1) """
    PFLAG_ATTACHED_TO_DEBUGGEE: enum_PROVIDER_FLAGS = ...
    PFLAG_DEBUGGEE: enum_PROVIDER_FLAGS = ...
    PFLAG_GET_IS_DEBUGGER_PRESENT: enum_PROVIDER_FLAGS = ...
    PFLAG_GET_PROGRAM_NODES: enum_PROVIDER_FLAGS = ...
    PFLAG_NONE: enum_PROVIDER_FLAGS = ...
    PFLAG_REASON_WATCH: enum_PROVIDER_FLAGS = ...
    PFLAG_REMOTE_PORT: enum_PROVIDER_FLAGS = ...
    value__ = ...


class enum_REFERENCE_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_REFERENCE_TYPE, values: REF_TYPE_STRONG (2), REF_TYPE_WEAK (1) """
    REF_TYPE_STRONG: enum_REFERENCE_TYPE = ...
    REF_TYPE_WEAK: enum_REFERENCE_TYPE = ...
    value__ = ...


class enum_REMOTE_PROCESS_FLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_REMOTE_PROCESS_FLAGS, values: RPFLAG_CLR_LOADED (1024), RPFLAG_DEBUGGER_ATTACH (256), RPFLAG_PROCESS_WOW64 (2048), RPFLAG_SQL_LOADED (512) """
    RPFLAG_CLR_LOADED: enum_REMOTE_PROCESS_FLAGS = ...
    RPFLAG_DEBUGGER_ATTACH: enum_REMOTE_PROCESS_FLAGS = ...
    RPFLAG_PROCESS_WOW64: enum_REMOTE_PROCESS_FLAGS = ...
    RPFLAG_SQL_LOADED: enum_REMOTE_PROCESS_FLAGS = ...
    value__ = ...


class enum_REMOTE_PROCESS_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_REMOTE_PROCESS_INFO_FIELDS, values: RPIF_COMMAND_LINE (4), RPIF_CURRENT_DIRECTORY (8), RPIF_DEBUGGER_PRESENT_FLAGS (256), RPIF_ENUMERATED_FLAGS (128), RPIF_ENVIRONMENT_VARIABLES (16), RPIF_MODULE_PATH (2), RPIF_PROGRAM_TYPE_FLAGS (512), RPIF_SESSION_ID (64), RPIF_TITLE (1), RPIF_USER_NAME (32) """
    RPIF_COMMAND_LINE: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_CURRENT_DIRECTORY: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_DEBUGGER_PRESENT_FLAGS: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_ENUMERATED_FLAGS: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_ENVIRONMENT_VARIABLES: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_MODULE_PATH: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_PROGRAM_TYPE_FLAGS: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_SESSION_ID: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_TITLE: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    RPIF_USER_NAME: enum_REMOTE_PROCESS_INFO_FIELDS = ...
    value__ = ...


class enum_SEEK_START(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_SEEK_START, values: SEEK_START_BEGIN (1), SEEK_START_CODECONTEXT (4), SEEK_START_CODELOCID (5), SEEK_START_CURRENT (3), SEEK_START_END (2) """
    SEEK_START_BEGIN: enum_SEEK_START = ...
    SEEK_START_CODECONTEXT: enum_SEEK_START = ...
    SEEK_START_CODELOCID: enum_SEEK_START = ...
    SEEK_START_CURRENT: enum_SEEK_START = ...
    SEEK_START_END: enum_SEEK_START = ...
    value__ = ...


class enum_SESSION_CACHE_PRIORITY(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_SESSION_CACHE_PRIORITY, values: HIGH_CACHE_PRIORITY (1), NORMAL_CACHE_PRIORITY (0) """
    HIGH_CACHE_PRIORITY: enum_SESSION_CACHE_PRIORITY = ...
    NORMAL_CACHE_PRIORITY: enum_SESSION_CACHE_PRIORITY = ...
    value__ = ...


class enum_SESSION_FEATURES(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_SESSION_FEATURES, values: FEATURE_CAUSALITY (2), FEATURE_REMOTE_DEBUGGING (1) """
    FEATURE_CAUSALITY: enum_SESSION_FEATURES = ...
    FEATURE_REMOTE_DEBUGGING: enum_SESSION_FEATURES = ...
    value__ = ...


class enum_SOURCE_TEXT_ATTR(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_SOURCE_TEXT_ATTR, values: SOURCETEXT_ATTR_COMMENT (2), SOURCETEXT_ATTR_FUNCTION_START (64), SOURCETEXT_ATTR_KEYWORD (1), SOURCETEXT_ATTR_NONSOURCE (4), SOURCETEXT_ATTR_NUMBER (16), SOURCETEXT_ATTR_OPERATOR (8), SOURCETEXT_ATTR_STRING (32) """
    SOURCETEXT_ATTR_COMMENT: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_FUNCTION_START: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_KEYWORD: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_NONSOURCE: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_NUMBER: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_OPERATOR: enum_SOURCE_TEXT_ATTR = ...
    SOURCETEXT_ATTR_STRING: enum_SOURCE_TEXT_ATTR = ...
    value__ = ...


class enum_STEPKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_STEPKIND, values: STEP_BACKWARDS (3), STEP_INTO (0), STEP_OUT (2), STEP_OVER (1) """
    STEP_BACKWARDS: enum_STEPKIND = ...
    STEP_INTO: enum_STEPKIND = ...
    STEP_OUT: enum_STEPKIND = ...
    STEP_OVER: enum_STEPKIND = ...
    value__ = ...


class enum_STEPUNIT(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_STEPUNIT, values: STEP_INSTRUCTION (2), STEP_LINE (1), STEP_STATEMENT (0) """
    STEP_INSTRUCTION: enum_STEPUNIT = ...
    STEP_LINE: enum_STEPUNIT = ...
    STEP_STATEMENT: enum_STEPUNIT = ...
    value__ = ...


class enum_SYMBOL_SEARCH_INFO_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_SYMBOL_SEARCH_INFO_FIELDS, values: SSIF_NONE (0), SSIF_VERBOSE_SEARCH_INFO (1) """
    SSIF_NONE: enum_SYMBOL_SEARCH_INFO_FIELDS = ...
    SSIF_VERBOSE_SEARCH_INFO: enum_SYMBOL_SEARCH_INFO_FIELDS = ...
    value__ = ...


class enum_TEXT_POSITION_MAX(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_TEXT_POSITION_MAX, values: TEXT_POSITION_MAX_COLUMN (-1), TEXT_POSITION_MAX_LINE (-1) """
    TEXT_POSITION_MAX_COLUMN: enum_TEXT_POSITION_MAX = ...
    TEXT_POSITION_MAX_LINE: enum_TEXT_POSITION_MAX = ...
    value__ = ...


class enum_THREADPROPERTY_FIELDS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) enum_THREADPROPERTY_FIELDS, values: TPF_ALLFIELDS (4294967295), TPF_ID (1), TPF_LOCATION (32), TPF_NAME (16), TPF_PRIORITY (8), TPF_STATE (4), TPF_SUSPENDCOUNT (2) """
    TPF_ALLFIELDS: enum_THREADPROPERTY_FIELDS = ...
    TPF_ID: enum_THREADPROPERTY_FIELDS = ...
    TPF_LOCATION: enum_THREADPROPERTY_FIELDS = ...
    TPF_NAME: enum_THREADPROPERTY_FIELDS = ...
    TPF_PRIORITY: enum_THREADPROPERTY_FIELDS = ...
    TPF_STATE: enum_THREADPROPERTY_FIELDS = ...
    TPF_SUSPENDCOUNT: enum_THREADPROPERTY_FIELDS = ...
    value__ = ...


class enum_THREADSTATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_THREADSTATE, values: THREADSTATE_DEAD (4), THREADSTATE_FRESH (3), THREADSTATE_FROZEN (5), THREADSTATE_RUNNING (1), THREADSTATE_STOPPED (2) """
    THREADSTATE_DEAD: enum_THREADSTATE = ...
    THREADSTATE_FRESH: enum_THREADSTATE = ...
    THREADSTATE_FROZEN: enum_THREADSTATE = ...
    THREADSTATE_RUNNING: enum_THREADSTATE = ...
    THREADSTATE_STOPPED: enum_THREADSTATE = ...
    value__ = ...


class enum_WATCHFOREVAL(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum enum_WATCHFOREVAL, values: WATCHFOREVAL_LEAF_PROGRAM (268435456) """
    value__ = ...
    WATCHFOREVAL_LEAF_PROGRAM: enum_WATCHFOREVAL = ...


class ERRORRESUMEACTION(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ERRORRESUMEACTION, values: ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller (1), ERRORRESUMEACTION_ReexecuteErrorStatement (0), ERRORRESUMEACTION_SkipErrorStatement (2) """
    ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller: ERRORRESUMEACTION = ...
    ERRORRESUMEACTION_ReexecuteErrorStatement: ERRORRESUMEACTION = ...
    ERRORRESUMEACTION_SkipErrorStatement: ERRORRESUMEACTION = ...
    value__ = ...


class EXCEPTION_BOUNDARY_TYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EXCEPTION_BOUNDARY_TYPE, values: EXCEPTION_BOUNDARY_APPDOMAIN (1), EXCEPTION_BOUNDARY_NONE (0), EXCEPTION_BOUNDARY_UNMANAGED (2) """
    EXCEPTION_BOUNDARY_APPDOMAIN: EXCEPTION_BOUNDARY_TYPE = ...
    EXCEPTION_BOUNDARY_NONE: EXCEPTION_BOUNDARY_TYPE = ...
    EXCEPTION_BOUNDARY_UNMANAGED: EXCEPTION_BOUNDARY_TYPE = ...
    value__ = ...


class EXCEPTION_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrExceptionName = ...
    bstrProgramName = ...
    dwCode = ...
    dwState = ...
    guidType = ...
    pProgram = ...


class ExtendedDebugPropertyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    m_bstrFullName = ...
    m_bstrName = ...
    m_bstrType = ...
    m_bstrValue = ...
    m_dwAttrib = ...
    m_dwValidFields = ...
    m_nDISPID = ...
    m_nType = ...
    m_pDebugExtProp = ...
    m_pDebugProp = ...
    m_plbValue = ...
    m_varValue = ...


class FIELD_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrFullName = ...
    bstrName = ...
    bstrType = ...
    dwFields = ...
    dwModifiers = ...


class FRAMEINFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    m_addrMax = ...
    m_addrMin = ...
    m_bstrArgs = ...
    m_bstrFuncName = ...
    m_bstrLanguage = ...
    m_bstrModule = ...
    m_bstrReturnType = ...
    m_dwFlags = ...
    m_dwValidFields = ...
    m_fHasDebugInfo = ...
    m_fStaleCode = ...
    m_pFrame = ...
    m_pModule = ...


class FUNC_EVAL_ABORT_RESULT(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FUNC_EVAL_ABORT_RESULT, values: ABORT_FAILED (2), ABORT_HUNG (3), ABORT_SUCCEEDED (0), PROCESS_TERMINATED (4), RUDE_ABORT_SUCCEEDED (1) """
    ABORT_FAILED: FUNC_EVAL_ABORT_RESULT = ...
    ABORT_HUNG: FUNC_EVAL_ABORT_RESULT = ...
    ABORT_SUCCEEDED: FUNC_EVAL_ABORT_RESULT = ...
    PROCESS_TERMINATED: FUNC_EVAL_ABORT_RESULT = ...
    RUDE_ABORT_SUCCEEDED: FUNC_EVAL_ABORT_RESULT = ...
    value__ = ...


class GUID_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


class IActiveScript: # skipped bases: <type 'object'>
    """ no doc """
    def AddNamedItem(self, pstrName:str, dwFlags:UInt32) -> int:
        """ AddNamedItem(self: IActiveScript, pstrName: str, dwFlags: UInt32) -> int """
        ...

    def AddTypeLib(self, rguidTypeLib:Guid, dwMajor:UInt32, dwMinor:UInt32, dwFlags:UInt32) -> Tuple_[int, Guid]:
        """ AddTypeLib(self: IActiveScript, rguidTypeLib: Guid, dwMajor: UInt32, dwMinor: UInt32, dwFlags: UInt32) -> (int, Guid) """
        ...

    def Clone(self, ppscript) -> Tuple_[int, IActiveScript]:
        """ Clone(self: IActiveScript) -> (int, IActiveScript) """
        ...

    def Close(self) -> int:
        """ Close(self: IActiveScript) -> int """
        ...

    def GetCurrentScriptThreadID(self, pstidThread) -> Tuple_[int, UInt32]:
        """ GetCurrentScriptThreadID(self: IActiveScript) -> (int, UInt32) """
        ...

    def GetScriptDispatch(self, pstrItemName, ppdisp) -> Tuple_[int, object]:
        """ GetScriptDispatch(self: IActiveScript, pstrItemName: str) -> (int, object) """
        ...

    def GetScriptSite(self, riid, ppvObject) -> Tuple_[int, Guid, IntPtr]:
        """ GetScriptSite(self: IActiveScript, riid: Guid) -> (int, Guid, IntPtr) """
        ...

    def GetScriptState(self, pssState) -> Tuple_[int, Array]:
        """ GetScriptState(self: IActiveScript) -> (int, Array[SCRIPTSTATE]) """
        ...

    def GetScriptThreadID(self, dwWin32ThreadId, pstidThread) -> Tuple_[int, UInt32]:
        """ GetScriptThreadID(self: IActiveScript, dwWin32ThreadId: UInt32) -> (int, UInt32) """
        ...

    def GetScriptThreadState(self, stidThread, pstsState) -> Tuple_[int, Array]:
        """ GetScriptThreadState(self: IActiveScript, stidThread: UInt32) -> (int, Array[SCRIPTTHREADSTATE]) """
        ...

    def InterruptScriptThread(self, stidThread:UInt32, pexcepinfo:Array, dwFlags:UInt32) -> int:
        """ InterruptScriptThread(self: IActiveScript, stidThread: UInt32, pexcepinfo: Array[EXCEPINFO], dwFlags: UInt32) -> int """
        ...

    def SetScriptSite(self, pass_:IActiveScriptSite) -> int:
        """ SetScriptSite(self: IActiveScript, pass: IActiveScriptSite) -> int """
        ...

    def SetScriptState(self, ss:SCRIPTSTATE) -> int:
        """ SetScriptState(self: IActiveScript, ss: SCRIPTSTATE) -> int """
        ...


class IActiveScriptDebug32: # skipped bases: <type 'object'>
    """ no doc """
    def EnumCodeContextsOfPosition(self, dwSourceContext, uCharacterOffset, uNumChars, ppescc) -> Tuple_[int, IEnumDebugCodeContexts]:
        """ EnumCodeContextsOfPosition(self: IActiveScriptDebug32, dwSourceContext: UInt32, uCharacterOffset: UInt32, uNumChars: UInt32) -> (int, IEnumDebugCodeContexts) """
        ...

    def GetScriptletTextAttributes(self, pstrCode, uNumCodeChars, pstrDelimiter, dwFlags, pattr) -> Tuple_[int, Array]:
        """ GetScriptletTextAttributes(self: IActiveScriptDebug32, pstrCode: Array[str], uNumCodeChars: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, Array[UInt16]) """
        ...

    def GetScriptTextAttributes(self, pstrCode, uNumCodeChars, pstrDelimiter, dwFlags, pattr) -> Tuple_[int, Array]:
        """ GetScriptTextAttributes(self: IActiveScriptDebug32, pstrCode: Array[str], uNumCodeChars: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, Array[UInt16]) """
        ...


class IActiveScriptDebug64: # skipped bases: <type 'object'>
    """ no doc """
    def EnumCodeContextsOfPosition(self, dwSourceContext, uCharacterOffset, uNumChars, ppescc) -> Tuple_[int, IEnumDebugCodeContexts]:
        """ EnumCodeContextsOfPosition(self: IActiveScriptDebug64, dwSourceContext: UInt64, uCharacterOffset: UInt32, uNumChars: UInt32) -> (int, IEnumDebugCodeContexts) """
        ...

    def GetScriptletTextAttributes(self, pstrCode, uNumCodeChars, pstrDelimiter, dwFlags, pattr) -> Tuple_[int, Array]:
        """ GetScriptletTextAttributes(self: IActiveScriptDebug64, pstrCode: Array[str], uNumCodeChars: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, Array[UInt16]) """
        ...

    def GetScriptTextAttributes(self, pstrCode, uNumCodeChars, pstrDelimiter, dwFlags, pattr) -> Tuple_[int, Array]:
        """ GetScriptTextAttributes(self: IActiveScriptDebug64, pstrCode: Array[str], uNumCodeChars: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, Array[UInt16]) """
        ...


class IActiveScriptEncode: # skipped bases: <type 'object'>
    """ no doc """
    def DecodeScript(self, pchIn, cchIn, pchOut, cchOut, pcchRet) -> Tuple_[int, str, UInt32]:
        """ DecodeScript(self: IActiveScriptEncode, pchIn: str, cchIn: UInt32, cchOut: UInt32) -> (int, str, UInt32) """
        ...

    def EncodeSection(self, pchIn, cchIn, pchOut, cchOut, pcchRet) -> Tuple_[int, str, UInt32]:
        """ EncodeSection(self: IActiveScriptEncode, pchIn: str, cchIn: UInt32, cchOut: UInt32) -> (int, str, UInt32) """
        ...

    def GetEncodeProgId(self, pbstrOut) -> Tuple_[int, str]:
        """ GetEncodeProgId(self: IActiveScriptEncode) -> (int, str) """
        ...


class IActiveScriptError: # skipped bases: <type 'object'>
    """ no doc """
    def GetExceptionInfo(self, pexcepinfo) -> Tuple_[int, Array]:
        """ GetExceptionInfo(self: IActiveScriptError) -> (int, Array[EXCEPINFO]) """
        ...

    def GetSourceLineText(self, pbstrSourceLine) -> Tuple_[int, str]:
        """ GetSourceLineText(self: IActiveScriptError) -> (int, str) """
        ...

    def GetSourcePosition(self, pdwSourceContext, pulLineNumber, plCharacterPosition) -> Tuple_[int, UInt32, UInt32, int]:
        """ GetSourcePosition(self: IActiveScriptError) -> (int, UInt32, UInt32, int) """
        ...


class IActiveScriptError64(IActiveScriptError): # skipped bases: <type 'object'>
    """ no doc """
    def GetSourcePosition64(self, pdwSourceContext, pulLineNumber, plCharacterPosition) -> Tuple_[int, UInt64, UInt32, int]:
        """ GetSourcePosition64(self: IActiveScriptError64) -> (int, UInt64, UInt32, int) """
        ...


class IActiveScriptErrorDebug(IActiveScriptError): # skipped bases: <type 'object'>
    """ no doc """
    def GetDocumentContext(self, ppssc) -> Tuple_[int, IDebugDocumentContext]:
        """ GetDocumentContext(self: IActiveScriptErrorDebug) -> (int, IDebugDocumentContext) """
        ...

    def GetStackFrame(self, ppdsf) -> Tuple_[int, IDebugStackFrame]:
        """ GetStackFrame(self: IActiveScriptErrorDebug) -> (int, IDebugStackFrame) """
        ...


class IActiveScriptGarbageCollector: # skipped bases: <type 'object'>
    """ no doc """
    def CollectGarbage(self, SCRIPTGCTYPE:SCRIPTGCTYPE) -> int:
        """ CollectGarbage(self: IActiveScriptGarbageCollector, SCRIPTGCTYPE: SCRIPTGCTYPE) -> int """
        ...


class IActiveScriptHostEncode: # skipped bases: <type 'object'>
    """ no doc """
    def EncodeScriptHostFile(self, bstrInFile, pbstrOutFile, cFlags, bstrDefaultLang) -> Tuple_[int, str]:
        """ EncodeScriptHostFile(self: IActiveScriptHostEncode, bstrInFile: str, cFlags: UInt32, bstrDefaultLang: str) -> (int, str) """
        ...


class IActiveScriptParse32: # skipped bases: <type 'object'>
    """ no doc """
    def AddScriptlet(self, pstrDefaultName, pstrCode, pstrItemName, pstrSubItemName, pstrEventName, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, pbstrName, pexcepinfo) -> Tuple_[int, str, Array]:
        """ AddScriptlet(self: IActiveScriptParse32, pstrDefaultName: str, pstrCode: str, pstrItemName: str, pstrSubItemName: str, pstrEventName: str, pstrDelimiter: str, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, str, Array[EXCEPINFO]) """
        ...

    def InitNew(self) -> int:
        """ InitNew(self: IActiveScriptParse32) -> int """
        ...

    def ParseScriptText(self, pstrCode, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, pvarResult, pexcepinfo) -> Tuple_[int, object, Array]:
        """ ParseScriptText(self: IActiveScriptParse32, pstrCode: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object, Array[EXCEPINFO]) """
        ...


class IActiveScriptParse64: # skipped bases: <type 'object'>
    """ no doc """
    def AddScriptlet(self, pstrDefaultName, pstrCode, pstrItemName, pstrSubItemName, pstrEventName, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, pbstrName, pexcepinfo) -> Tuple_[int, str, Array]:
        """ AddScriptlet(self: IActiveScriptParse64, pstrDefaultName: str, pstrCode: str, pstrItemName: str, pstrSubItemName: str, pstrEventName: str, pstrDelimiter: str, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, str, Array[EXCEPINFO]) """
        ...

    def InitNew(self) -> int:
        """ InitNew(self: IActiveScriptParse64) -> int """
        ...

    def ParseScriptText(self, pstrCode, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, pvarResult, pexcepinfo) -> Tuple_[int, object, Array]:
        """ ParseScriptText(self: IActiveScriptParse64, pstrCode: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object, Array[EXCEPINFO]) """
        ...


class IActiveScriptParseProcedure32: # skipped bases: <type 'object'>
    """ no doc """
    def ParseProcedureText(self, pstrCode, pstrFormalParams, pstrProcedureName, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, ppdisp) -> Tuple_[int, object]:
        """ ParseProcedureText(self: IActiveScriptParseProcedure32, pstrCode: str, pstrFormalParams: str, pstrProcedureName: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object) """
        ...


class IActiveScriptParseProcedure2_32(IActiveScriptParseProcedure32): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IActiveScriptParseProcedure64: # skipped bases: <type 'object'>
    """ no doc """
    def ParseProcedureText(self, pstrCode, pstrFormalParams, pstrProcedureName, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, ppdisp) -> Tuple_[int, object]:
        """ ParseProcedureText(self: IActiveScriptParseProcedure64, pstrCode: str, pstrFormalParams: str, pstrProcedureName: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object) """
        ...


class IActiveScriptParseProcedure2_64(IActiveScriptParseProcedure64): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IActiveScriptParseProcedureOld32: # skipped bases: <type 'object'>
    """ no doc """
    def ParseProcedureText(self, pstrCode, pstrFormalParams, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, ppdisp) -> Tuple_[int, object]:
        """ ParseProcedureText(self: IActiveScriptParseProcedureOld32, pstrCode: str, pstrFormalParams: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object) """
        ...


class IActiveScriptParseProcedureOld64: # skipped bases: <type 'object'>
    """ no doc """
    def ParseProcedureText(self, pstrCode, pstrFormalParams, pstrItemName, punkContext, pstrDelimiter, dwSourceContextCookie, ulStartingLineNumber, dwFlags, ppdisp) -> Tuple_[int, object]:
        """ ParseProcedureText(self: IActiveScriptParseProcedureOld64, pstrCode: str, pstrFormalParams: str, pstrItemName: str, punkContext: object, pstrDelimiter: str, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32) -> (int, object) """
        ...


class IActiveScriptProperty: # skipped bases: <type 'object'>
    """ no doc """
    def GetProperty(self, dwProperty, pvarIndex, pvarValue) -> Tuple_[int, object, object]:
        """ GetProperty(self: IActiveScriptProperty, dwProperty: UInt32, pvarIndex: object) -> (int, object, object) """
        ...

    def SetProperty(self, dwProperty:UInt32, pvarIndex:object, pvarValue:object) -> Tuple_[int, object, object]:
        """ SetProperty(self: IActiveScriptProperty, dwProperty: UInt32, pvarIndex: object, pvarValue: object) -> (int, object, object) """
        ...


class IActiveScriptSIPInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetSIPOID(self, poid_sip) -> Tuple_[int, Guid]:
        """ GetSIPOID(self: IActiveScriptSIPInfo) -> (int, Guid) """
        ...


class IActiveScriptSite: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocVersionString(self, pbstrVersion) -> Tuple_[int, str]:
        """ GetDocVersionString(self: IActiveScriptSite) -> (int, str) """
        ...

    def GetItemInfo(self, pstrName, dwReturnMask, ppiunkItem, ppti) -> Tuple_[int, object, Type]:
        """ GetItemInfo(self: IActiveScriptSite, pstrName: str, dwReturnMask: UInt32) -> (int, object, Type) """
        ...

    def GetLCID(self, plcid) -> Tuple_[int, UInt32]:
        """ GetLCID(self: IActiveScriptSite) -> (int, UInt32) """
        ...

    def OnEnterScript(self) -> int:
        """ OnEnterScript(self: IActiveScriptSite) -> int """
        ...

    def OnLeaveScript(self) -> int:
        """ OnLeaveScript(self: IActiveScriptSite) -> int """
        ...

    def OnScriptError(self, pscripterror:IActiveScriptError) -> int:
        """ OnScriptError(self: IActiveScriptSite, pscripterror: IActiveScriptError) -> int """
        ...

    def OnScriptTerminate(self, pvarResult:object, pexcepinfo:Array) -> Tuple_[int, object]:
        """ OnScriptTerminate(self: IActiveScriptSite, pvarResult: object, pexcepinfo: Array[EXCEPINFO]) -> (int, object) """
        ...

    def OnStateChange(self, ssScriptState:SCRIPTSTATE) -> int:
        """ OnStateChange(self: IActiveScriptSite, ssScriptState: SCRIPTSTATE) -> int """
        ...


class IActiveScriptSiteDebug32: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplication(self, ppda) -> Tuple_[int, IDebugApplication32]:
        """ GetApplication(self: IActiveScriptSiteDebug32) -> (int, IDebugApplication32) """
        ...

    def GetDocumentContextFromPosition(self, dwSourceContext, uCharacterOffset, uNumChars, ppsc) -> Tuple_[int, IDebugDocumentContext]:
        """ GetDocumentContextFromPosition(self: IActiveScriptSiteDebug32, dwSourceContext: UInt32, uCharacterOffset: UInt32, uNumChars: UInt32) -> (int, IDebugDocumentContext) """
        ...

    def GetRootApplicationNode(self, ppdanRoot) -> Tuple_[int, IDebugApplicationNode]:
        """ GetRootApplicationNode(self: IActiveScriptSiteDebug32) -> (int, IDebugApplicationNode) """
        ...

    def OnScriptErrorDebug(self, pErrorDebug, pfEnterDebugger, pfCallOnScriptErrorWhenContinuing) -> Tuple_[int, int, int]:
        """ OnScriptErrorDebug(self: IActiveScriptSiteDebug32, pErrorDebug: IActiveScriptErrorDebug) -> (int, int, int) """
        ...


class IActiveScriptSiteDebug64: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplication(self, ppda) -> Tuple_[int, IDebugApplication64]:
        """ GetApplication(self: IActiveScriptSiteDebug64) -> (int, IDebugApplication64) """
        ...

    def GetDocumentContextFromPosition(self, dwSourceContext, uCharacterOffset, uNumChars, ppsc) -> Tuple_[int, IDebugDocumentContext]:
        """ GetDocumentContextFromPosition(self: IActiveScriptSiteDebug64, dwSourceContext: UInt64, uCharacterOffset: UInt32, uNumChars: UInt32) -> (int, IDebugDocumentContext) """
        ...

    def GetRootApplicationNode(self, ppdanRoot) -> Tuple_[int, IDebugApplicationNode]:
        """ GetRootApplicationNode(self: IActiveScriptSiteDebug64) -> (int, IDebugApplicationNode) """
        ...

    def OnScriptErrorDebug(self, pErrorDebug, pfEnterDebugger, pfCallOnScriptErrorWhenContinuing) -> Tuple_[int, int, int]:
        """ OnScriptErrorDebug(self: IActiveScriptSiteDebug64, pErrorDebug: IActiveScriptErrorDebug) -> (int, int, int) """
        ...


class IActiveScriptSiteInterruptPoll: # skipped bases: <type 'object'>
    """ no doc """
    def QueryContinue(self) -> int:
        """ QueryContinue(self: IActiveScriptSiteInterruptPoll) -> int """
        ...


class IActiveScriptSiteWindow: # skipped bases: <type 'object'>
    """ no doc """
    def EnableModeless(self, fEnable:int) -> int:
        """ EnableModeless(self: IActiveScriptSiteWindow, fEnable: int) -> int """
        ...

    def GetWindow(self, phwnd) -> Tuple_[int, IntPtr]:
        """ GetWindow(self: IActiveScriptSiteWindow) -> (int, IntPtr) """
        ...


class IActiveScriptStats: # skipped bases: <type 'object'>
    """ no doc """
    def GetStat(self, stid, pluHi, pluLo) -> Tuple_[int, UInt32, UInt32]:
        """ GetStat(self: IActiveScriptStats, stid: UInt32) -> (int, UInt32, UInt32) """
        ...

    def GetStatEx(self, guid, pluHi, pluLo) -> Tuple_[int, Guid, UInt32, UInt32]:
        """ GetStatEx(self: IActiveScriptStats, guid: Guid) -> (int, Guid, UInt32, UInt32) """
        ...

    def ResetStats(self) -> int:
        """ ResetStats(self: IActiveScriptStats) -> int """
        ...


class IApplicationDebugger: # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstanceAtDebugger(self, rclsid, pUnkOuter, dwClsContext, riid, ppvObject) -> Tuple_[int, Guid, Guid, object]:
        """ CreateInstanceAtDebugger(self: IApplicationDebugger, rclsid: Guid, pUnkOuter: object, dwClsContext: UInt32, riid: Guid) -> (int, Guid, Guid, object) """
        ...

    def onClose(self) -> int:
        """ onClose(self: IApplicationDebugger) -> int """
        ...

    def onDebuggerEvent(self, riid:Guid, punk:object) -> Tuple_[int, Guid]:
        """ onDebuggerEvent(self: IApplicationDebugger, riid: Guid, punk: object) -> (int, Guid) """
        ...

    def onDebugOutput(self, pstr:str) -> int:
        """ onDebugOutput(self: IApplicationDebugger, pstr: str) -> int """
        ...

    def onHandleBreakPoint(self, prpt:IRemoteDebugApplicationThread, br:BREAKREASON, pError:IActiveScriptErrorDebug) -> int:
        """ onHandleBreakPoint(self: IApplicationDebugger, prpt: IRemoteDebugApplicationThread, br: BREAKREASON, pError: IActiveScriptErrorDebug) -> int """
        ...

    def QueryAlive(self) -> int:
        """ QueryAlive(self: IApplicationDebugger) -> int """
        ...


class IApplicationDebuggerUI: # skipped bases: <type 'object'>
    """ no doc """
    def BringDocumentContextToTop(self, pddc:IDebugDocumentContext) -> int:
        """ BringDocumentContextToTop(self: IApplicationDebuggerUI, pddc: IDebugDocumentContext) -> int """
        ...

    def BringDocumentToTop(self, pddt:IDebugDocumentText) -> int:
        """ BringDocumentToTop(self: IApplicationDebuggerUI, pddt: IDebugDocumentText) -> int """
        ...


class IBindEventHandler: # skipped bases: <type 'object'>
    """ no doc """
    def BindHandler(self, pstrEvent:str, pdisp:object) -> int:
        """ BindHandler(self: IBindEventHandler, pstrEvent: str, pdisp: object) -> int """
        ...


class IDebugActivateDocumentEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocument(self, ppDoc) -> Tuple_[int, IDebugDocument2]:
        """ GetDocument(self: IDebugActivateDocumentEvent2) -> (int, IDebugDocument2) """
        ...

    def GetDocumentContext(self, ppDocContext) -> Tuple_[int, IDebugDocumentContext2]:
        """ GetDocumentContext(self: IDebugActivateDocumentEvent2) -> (int, IDebugDocumentContext2) """
        ...


class IDebugAD1Program2_V7: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplication(self, ppApp) -> Tuple_[int, IRemoteDebugApplication]:
        """ GetApplication(self: IDebugAD1Program2_V7) -> (int, IRemoteDebugApplication) """
        ...


class IDebugAddress: # skipped bases: <type 'object'>
    """ no doc """
    def GetAddress(self, pAddress) -> Tuple_[int, Array]:
        """ GetAddress(self: IDebugAddress) -> (int, Array[DEBUG_ADDRESS]) """
        ...


class IDebugAddress2(IDebugAddress): # skipped bases: <type 'object'>
    """ no doc """
    def GetProcessId(self, pProcID) -> Tuple_[int, UInt32]:
        """ GetProcessId(self: IDebugAddress2) -> (int, UInt32) """
        ...


class IDebugAlias: # skipped bases: <type 'object'>
    """ no doc """
    def Dispose(self) -> int:
        """ Dispose(self: IDebugAlias) -> int """
        ...

    def GetICorDebugValue(self, ppUnk) -> Tuple_[int, object]:
        """ GetICorDebugValue(self: IDebugAlias) -> (int, object) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugAlias) -> (int, str) """
        ...

    def GetObject(self, ppObject) -> Tuple_[int, IDebugObject2]:
        """ GetObject(self: IDebugAlias) -> (int, IDebugObject2) """
        ...


class IRemoteDebugApplication: # skipped bases: <type 'object'>
    """ no doc """
    def CauseBreak(self) -> int:
        """ CauseBreak(self: IRemoteDebugApplication) -> int """
        ...

    def ConnectDebugger(self, pad:IApplicationDebugger) -> int:
        """ ConnectDebugger(self: IRemoteDebugApplication, pad: IApplicationDebugger) -> int """
        ...

    def CreateInstanceAtApplication(self, rclsid, pUnkOuter, dwClsContext, riid, ppvObject) -> Tuple_[int, Guid, Guid, object]:
        """ CreateInstanceAtApplication(self: IRemoteDebugApplication, rclsid: Guid, pUnkOuter: object, dwClsContext: UInt32, riid: Guid) -> (int, Guid, Guid, object) """
        ...

    def DisconnectDebugger(self) -> int:
        """ DisconnectDebugger(self: IRemoteDebugApplication) -> int """
        ...

    def EnumGlobalExpressionContexts(self, ppedec) -> Tuple_[int, IEnumDebugExpressionContexts]:
        """ EnumGlobalExpressionContexts(self: IRemoteDebugApplication) -> (int, IEnumDebugExpressionContexts) """
        ...

    def EnumThreads(self, pperdat) -> Tuple_[int, IEnumRemoteDebugApplicationThreads]:
        """ EnumThreads(self: IRemoteDebugApplication) -> (int, IEnumRemoteDebugApplicationThreads) """
        ...

    def GetDebugger(self, pad) -> Tuple_[int, IApplicationDebugger]:
        """ GetDebugger(self: IRemoteDebugApplication) -> (int, IApplicationDebugger) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IRemoteDebugApplication) -> (int, str) """
        ...

    def GetRootNode(self, ppdanRoot) -> Tuple_[int, IDebugApplicationNode]:
        """ GetRootNode(self: IRemoteDebugApplication) -> (int, IDebugApplicationNode) """
        ...

    def QueryAlive(self) -> int:
        """ QueryAlive(self: IRemoteDebugApplication) -> int """
        ...

    def ResumeFromBreakPoint(self, prptFocus:IRemoteDebugApplicationThread, bra:BREAKRESUMEACTION, era:ERRORRESUMEACTION) -> int:
        """ ResumeFromBreakPoint(self: IRemoteDebugApplication, prptFocus: IRemoteDebugApplicationThread, bra: BREAKRESUMEACTION, era: ERRORRESUMEACTION) -> int """
        ...


class IDebugApplication32(IRemoteDebugApplication): # skipped bases: <type 'object'>
    """ no doc """
    def AddGlobalExpressionContextProvider(self, pdsfs, pdwCookie) -> Tuple_[int, UInt32]:
        """ AddGlobalExpressionContextProvider(self: IDebugApplication32, pdsfs: IProvideExpressionContexts) -> (int, UInt32) """
        ...

    def AddStackFrameSniffer(self, pdsfs, pdwCookie) -> Tuple_[int, UInt32]:
        """ AddStackFrameSniffer(self: IDebugApplication32, pdsfs: IDebugStackFrameSniffer) -> (int, UInt32) """
        ...

    def Close(self) -> int:
        """ Close(self: IDebugApplication32) -> int """
        ...

    def CreateApplicationNode(self, ppdanNew) -> Tuple_[int, IDebugApplicationNode]:
        """ CreateApplicationNode(self: IDebugApplication32) -> (int, IDebugApplicationNode) """
        ...

    def CreateAsyncDebugOperation(self, psdo, ppado) -> Tuple_[int, IDebugAsyncOperation]:
        """ CreateAsyncDebugOperation(self: IDebugApplication32, psdo: IDebugSyncOperation) -> (int, IDebugAsyncOperation) """
        ...

    def DebugOutput(self, pstr:str) -> int:
        """ DebugOutput(self: IDebugApplication32, pstr: str) -> int """
        ...

    def FCanJitDebug(self) -> int:
        """ FCanJitDebug(self: IDebugApplication32) -> int """
        ...

    def FireDebuggerEvent(self, riid:Guid, punk:object) -> Tuple_[int, Guid]:
        """ FireDebuggerEvent(self: IDebugApplication32, riid: Guid, punk: object) -> (int, Guid) """
        ...

    def FIsAutoJitDebugEnabled(self) -> int:
        """ FIsAutoJitDebugEnabled(self: IDebugApplication32) -> int """
        ...

    def GetBreakFlags(self, pabf, pprdatSteppingThread) -> Tuple_[int, UInt32, IRemoteDebugApplicationThread]:
        """ GetBreakFlags(self: IDebugApplication32) -> (int, UInt32, IRemoteDebugApplicationThread) """
        ...

    def GetCurrentThread(self, pat) -> Tuple_[int, IDebugApplicationThread]:
        """ GetCurrentThread(self: IDebugApplication32) -> (int, IDebugApplicationThread) """
        ...

    def HandleBreakPoint(self, br, pbra) -> Tuple_[int, Array]:
        """ HandleBreakPoint(self: IDebugApplication32, br: BREAKREASON) -> (int, Array[BREAKRESUMEACTION]) """
        ...

    def HandleRuntimeError(self, pErrorDebug, pScriptSite, pbra, perra, pfCallOnScriptError) -> Tuple_[int, Array, Array, int]:
        """ HandleRuntimeError(self: IDebugApplication32, pErrorDebug: IActiveScriptErrorDebug, pScriptSite: IActiveScriptSite) -> (int, Array[BREAKRESUMEACTION], Array[ERRORRESUMEACTION], int) """
        ...

    def QueryCurrentThreadIsDebuggerThread(self) -> int:
        """ QueryCurrentThreadIsDebuggerThread(self: IDebugApplication32) -> int """
        ...

    def RemoveGlobalExpressionContextProvider(self, dwCookie:UInt32) -> int:
        """ RemoveGlobalExpressionContextProvider(self: IDebugApplication32, dwCookie: UInt32) -> int """
        ...

    def RemoveStackFrameSniffer(self, dwCookie:UInt32) -> int:
        """ RemoveStackFrameSniffer(self: IDebugApplication32, dwCookie: UInt32) -> int """
        ...

    def SetName(self, pstrName:str) -> int:
        """ SetName(self: IDebugApplication32, pstrName: str) -> int """
        ...

    def StartDebugSession(self) -> int:
        """ StartDebugSession(self: IDebugApplication32) -> int """
        ...

    def StepOutComplete(self) -> int:
        """ StepOutComplete(self: IDebugApplication32) -> int """
        ...

    def SynchronousCallInDebuggerThread(self, pptc:IDebugThreadCall32, dwParam1:IntPtr, dwParam2:IntPtr, dwParam3:IntPtr) -> int:
        """ SynchronousCallInDebuggerThread(self: IDebugApplication32, pptc: IDebugThreadCall32, dwParam1: IntPtr, dwParam2: IntPtr, dwParam3: IntPtr) -> int """
        ...


class IDebugApplication64(IRemoteDebugApplication): # skipped bases: <type 'object'>
    """ no doc """
    def AddGlobalExpressionContextProvider(self, pdsfs, pdwCookie) -> Tuple_[int, UInt64]:
        """ AddGlobalExpressionContextProvider(self: IDebugApplication64, pdsfs: IProvideExpressionContexts) -> (int, UInt64) """
        ...

    def AddStackFrameSniffer(self, pdsfs, pdwCookie) -> Tuple_[int, UInt32]:
        """ AddStackFrameSniffer(self: IDebugApplication64, pdsfs: IDebugStackFrameSniffer) -> (int, UInt32) """
        ...

    def Close(self) -> int:
        """ Close(self: IDebugApplication64) -> int """
        ...

    def CreateApplicationNode(self, ppdanNew) -> Tuple_[int, IDebugApplicationNode]:
        """ CreateApplicationNode(self: IDebugApplication64) -> (int, IDebugApplicationNode) """
        ...

    def CreateAsyncDebugOperation(self, psdo, ppado) -> Tuple_[int, IDebugAsyncOperation]:
        """ CreateAsyncDebugOperation(self: IDebugApplication64, psdo: IDebugSyncOperation) -> (int, IDebugAsyncOperation) """
        ...

    def DebugOutput(self, pstr:str) -> int:
        """ DebugOutput(self: IDebugApplication64, pstr: str) -> int """
        ...

    def FCanJitDebug(self) -> int:
        """ FCanJitDebug(self: IDebugApplication64) -> int """
        ...

    def FireDebuggerEvent(self, riid:Guid, punk:object) -> Tuple_[int, Guid]:
        """ FireDebuggerEvent(self: IDebugApplication64, riid: Guid, punk: object) -> (int, Guid) """
        ...

    def FIsAutoJitDebugEnabled(self) -> int:
        """ FIsAutoJitDebugEnabled(self: IDebugApplication64) -> int """
        ...

    def GetBreakFlags(self, pabf, pprdatSteppingThread) -> Tuple_[int, UInt32, IRemoteDebugApplicationThread]:
        """ GetBreakFlags(self: IDebugApplication64) -> (int, UInt32, IRemoteDebugApplicationThread) """
        ...

    def GetCurrentThread(self, pat) -> Tuple_[int, IDebugApplicationThread]:
        """ GetCurrentThread(self: IDebugApplication64) -> (int, IDebugApplicationThread) """
        ...

    def HandleBreakPoint(self, br, pbra) -> Tuple_[int, Array]:
        """ HandleBreakPoint(self: IDebugApplication64, br: BREAKREASON) -> (int, Array[BREAKRESUMEACTION]) """
        ...

    def HandleRuntimeError(self, pErrorDebug, pScriptSite, pbra, perra, pfCallOnScriptError) -> Tuple_[int, Array, Array, int]:
        """ HandleRuntimeError(self: IDebugApplication64, pErrorDebug: IActiveScriptErrorDebug, pScriptSite: IActiveScriptSite) -> (int, Array[BREAKRESUMEACTION], Array[ERRORRESUMEACTION], int) """
        ...

    def QueryCurrentThreadIsDebuggerThread(self) -> int:
        """ QueryCurrentThreadIsDebuggerThread(self: IDebugApplication64) -> int """
        ...

    def RemoveGlobalExpressionContextProvider(self, dwCookie:UInt64) -> int:
        """ RemoveGlobalExpressionContextProvider(self: IDebugApplication64, dwCookie: UInt64) -> int """
        ...

    def RemoveStackFrameSniffer(self, dwCookie:UInt32) -> int:
        """ RemoveStackFrameSniffer(self: IDebugApplication64, dwCookie: UInt32) -> int """
        ...

    def SetName(self, pstrName:str) -> int:
        """ SetName(self: IDebugApplication64, pstrName: str) -> int """
        ...

    def StartDebugSession(self) -> int:
        """ StartDebugSession(self: IDebugApplication64) -> int """
        ...

    def StepOutComplete(self) -> int:
        """ StepOutComplete(self: IDebugApplication64) -> int """
        ...

    def SynchronousCallInDebuggerThread(self, pptc:IDebugThreadCall64, dwParam1:UInt64, dwParam2:UInt64, dwParam3:UInt64) -> int:
        """ SynchronousCallInDebuggerThread(self: IDebugApplication64, pptc: IDebugThreadCall64, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> int """
        ...


class IDebugDocumentInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocumentClassId(self, pclsidDocument) -> Tuple_[int, Guid]:
        """ GetDocumentClassId(self: IDebugDocumentInfo) -> (int, Guid) """
        ...

    def GetName(self, dnt, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugDocumentInfo, dnt: DOCUMENTNAMETYPE) -> (int, str) """
        ...


class IDebugDocumentProvider(IDebugDocumentInfo): # skipped bases: <type 'object'>
    """ no doc """
    def GetDocument(self, ppssd) -> Tuple_[int, IDebugDocument]:
        """ GetDocument(self: IDebugDocumentProvider) -> (int, IDebugDocument) """
        ...


class IDebugApplicationNode(IDebugDocumentProvider): # skipped bases: <type 'IDebugDocumentInfo'>, <type 'object'>
    """ no doc """
    def Attach(self, pdanParent:IDebugApplicationNode) -> int:
        """ Attach(self: IDebugApplicationNode, pdanParent: IDebugApplicationNode) -> int """
        ...

    def Close(self) -> int:
        """ Close(self: IDebugApplicationNode) -> int """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugApplicationNode) -> int """
        ...

    def EnumChildren(self, pperddp) -> Tuple_[int, IEnumDebugApplicationNodes]:
        """ EnumChildren(self: IDebugApplicationNode) -> (int, IEnumDebugApplicationNodes) """
        ...

    def GetParent(self, pprddp) -> Tuple_[int, IDebugApplicationNode]:
        """ GetParent(self: IDebugApplicationNode) -> (int, IDebugApplicationNode) """
        ...

    def SetDocumentProvider(self, pddp:IDebugDocumentProvider) -> int:
        """ SetDocumentProvider(self: IDebugApplicationNode, pddp: IDebugDocumentProvider) -> int """
        ...


class IDebugApplicationNodeEvents: # skipped bases: <type 'object'>
    """ no doc """
    def onAddChild(self, prddpChild:IDebugApplicationNode) -> int:
        """ onAddChild(self: IDebugApplicationNodeEvents, prddpChild: IDebugApplicationNode) -> int """
        ...

    def OnAttach(self, prddpParent:IDebugApplicationNode) -> int:
        """ OnAttach(self: IDebugApplicationNodeEvents, prddpParent: IDebugApplicationNode) -> int """
        ...

    def onDetach(self) -> int:
        """ onDetach(self: IDebugApplicationNodeEvents) -> int """
        ...

    def onRemoveChild(self, prddpChild:IDebugApplicationNode) -> int:
        """ onRemoveChild(self: IDebugApplicationNodeEvents, prddpChild: IDebugApplicationNode) -> int """
        ...


class IRemoteDebugApplicationThread: # skipped bases: <type 'object'>
    """ no doc """
    def EnumStackFrames(self, ppedsf) -> Tuple_[int, IEnumDebugStackFrames]:
        """ EnumStackFrames(self: IRemoteDebugApplicationThread) -> (int, IEnumDebugStackFrames) """
        ...

    def GetApplication(self, pprda) -> Tuple_[int, IRemoteDebugApplication]:
        """ GetApplication(self: IRemoteDebugApplicationThread) -> (int, IRemoteDebugApplication) """
        ...

    def GetDescription(self, pbstrDescription, pbstrState) -> Tuple_[int, str, str]:
        """ GetDescription(self: IRemoteDebugApplicationThread) -> (int, str, str) """
        ...

    def GetState(self, pState) -> Tuple_[int, UInt32]:
        """ GetState(self: IRemoteDebugApplicationThread) -> (int, UInt32) """
        ...

    def GetSuspendCount(self, pdwCount) -> Tuple_[int, UInt32]:
        """ GetSuspendCount(self: IRemoteDebugApplicationThread) -> (int, UInt32) """
        ...

    def GetSystemThreadId(self, dwThreadId) -> Tuple_[int, UInt32]:
        """ GetSystemThreadId(self: IRemoteDebugApplicationThread) -> (int, UInt32) """
        ...

    def Resume(self, pdwCount) -> Tuple_[int, UInt32]:
        """ Resume(self: IRemoteDebugApplicationThread) -> (int, UInt32) """
        ...

    def SetNextStatement(self, pStackFrame:IDebugStackFrame, pCodeContext:IDebugCodeContext) -> int:
        """ SetNextStatement(self: IRemoteDebugApplicationThread, pStackFrame: IDebugStackFrame, pCodeContext: IDebugCodeContext) -> int """
        ...

    def Suspend(self, pdwCount) -> Tuple_[int, UInt32]:
        """ Suspend(self: IRemoteDebugApplicationThread) -> (int, UInt32) """
        ...


class IDebugApplicationThread(IRemoteDebugApplicationThread): # skipped bases: <type 'object'>
    """ no doc """
    def QueryIsCurrentThread(self) -> int:
        """ QueryIsCurrentThread(self: IDebugApplicationThread) -> int """
        ...

    def QueryIsDebuggerThread(self) -> int:
        """ QueryIsDebuggerThread(self: IDebugApplicationThread) -> int """
        ...

    def SetDescription(self, pstrDescription:str) -> int:
        """ SetDescription(self: IDebugApplicationThread, pstrDescription: str) -> int """
        ...

    def SetStateString(self, pstrState:str) -> int:
        """ SetStateString(self: IDebugApplicationThread, pstrState: str) -> int """
        ...

    def SynchronousCallIntoThread32(self, pstcb:IDebugThreadCall32, dwParam1:IntPtr, dwParam2:IntPtr, dwParam3:IntPtr) -> int:
        """ SynchronousCallIntoThread32(self: IDebugApplicationThread, pstcb: IDebugThreadCall32, dwParam1: IntPtr, dwParam2: IntPtr, dwParam3: IntPtr) -> int """
        ...


class IDebugApplicationThread64(IDebugApplicationThread): # skipped bases: <type 'IRemoteDebugApplicationThread'>, <type 'object'>
    """ no doc """
    def SynchronousCallIntoThread64(self, pstcb:IDebugThreadCall64, dwParam1:UInt64, dwParam2:UInt64, dwParam3:UInt64) -> int:
        """ SynchronousCallIntoThread64(self: IDebugApplicationThread64, pstcb: IDebugThreadCall64, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> int """
        ...


class IDebugField: # skipped bases: <type 'object'>
    """ no doc """
    def Equal(self, pField:IDebugField) -> int:
        """ Equal(self: IDebugField, pField: IDebugField) -> int """
        ...

    def GetAddress(self, ppAddress) -> Tuple_[int, IDebugAddress]:
        """ GetAddress(self: IDebugField) -> (int, IDebugAddress) """
        ...

    def GetContainer(self, ppContainerField) -> Tuple_[int, IDebugContainerField]:
        """ GetContainer(self: IDebugField) -> (int, IDebugContainerField) """
        ...

    def GetExtendedInfo(self, guidExtendedInfo, prgBuffer, pdwLen) -> Tuple_[int, Guid, Array, UInt32]:
        """ GetExtendedInfo(self: IDebugField, guidExtendedInfo: Guid) -> (int, Guid, Array[IntPtr], UInt32) """
        ...

    def GetInfo(self, dwFields, pFieldInfo) -> Tuple_[int, Array]:
        """ GetInfo(self: IDebugField, dwFields: UInt32) -> (int, Array[FIELD_INFO]) """
        ...

    def GetKind(self, pdwKind) -> Tuple_[int, UInt32]:
        """ GetKind(self: IDebugField) -> (int, UInt32) """
        ...

    def GetSize(self, pdwSize) -> Tuple_[int, UInt32]:
        """ GetSize(self: IDebugField) -> (int, UInt32) """
        ...

    def GetType(self, ppType) -> Tuple_[int, IDebugField]:
        """ GetType(self: IDebugField) -> (int, IDebugField) """
        ...

    def GetTypeInfo(self, pTypeInfo) -> Tuple_[int, Array]:
        """ GetTypeInfo(self: IDebugField) -> (int, Array[TYPE_INFO]) """
        ...


class IDebugContainerField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    def EnumFields(self, dwKindFilter, dwModifiersFilter, pszNameFilter, nameMatch, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumFields(self: IDebugContainerField, dwKindFilter: UInt32, dwModifiersFilter: UInt32, pszNameFilter: str, nameMatch: NAME_MATCH) -> (int, IEnumDebugFields) """
        ...


class IDebugArrayField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def GetElementType(self, ppType) -> Tuple_[int, IDebugField]:
        """ GetElementType(self: IDebugArrayField) -> (int, IDebugField) """
        ...

    def GetNumberOfElements(self, pdwNumElements) -> Tuple_[int, UInt32]:
        """ GetNumberOfElements(self: IDebugArrayField) -> (int, UInt32) """
        ...

    def GetRank(self, pdwRank) -> Tuple_[int, UInt32]:
        """ GetRank(self: IDebugArrayField) -> (int, UInt32) """
        ...


class IDebugObject: # skipped bases: <type 'object'>
    """ no doc """
    def GetManagedDebugObject(self, ppObject) -> Tuple_[int, IDebugManagedObject]:
        """ GetManagedDebugObject(self: IDebugObject) -> (int, IDebugManagedObject) """
        ...

    def GetMemoryContext(self, pContext:IDebugMemoryContext2) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext(self: IDebugObject, pContext: IDebugMemoryContext2) -> (int, IDebugMemoryContext2) """
        ...

    def GetSize(self, pnSize) -> Tuple_[int, UInt32]:
        """ GetSize(self: IDebugObject) -> (int, UInt32) """
        ...

    def GetValue(self, pValue, nSize) -> Tuple_[int, Array]:
        """ GetValue(self: IDebugObject, nSize: UInt32) -> (int, Array[Byte]) """
        ...

    def IsEqual(self, pObject, pfIsEqual) -> Tuple_[int, int]:
        """ IsEqual(self: IDebugObject, pObject: IDebugObject) -> (int, int) """
        ...

    def IsNullReference(self, pfIsNull) -> Tuple_[int, int]:
        """ IsNullReference(self: IDebugObject) -> (int, int) """
        ...

    def IsProxy(self, pfIsProxy) -> Tuple_[int, int]:
        """ IsProxy(self: IDebugObject) -> (int, int) """
        ...

    def IsReadOnly(self, pfIsReadOnly) -> Tuple_[int, int]:
        """ IsReadOnly(self: IDebugObject) -> (int, int) """
        ...

    def SetReferenceValue(self, pObject:IDebugObject) -> int:
        """ SetReferenceValue(self: IDebugObject, pObject: IDebugObject) -> int """
        ...

    def SetValue(self, pValue:Array, nSize:UInt32) -> int:
        """ SetValue(self: IDebugObject, pValue: Array[Byte], nSize: UInt32) -> int """
        ...


class IDebugArrayObject(IDebugObject): # skipped bases: <type 'object'>
    """ no doc """
    def GetCount(self, pdwElements) -> Tuple_[int, UInt32]:
        """ GetCount(self: IDebugArrayObject) -> (int, UInt32) """
        ...

    def GetDimensions(self, dwCount, dwDimensions) -> Tuple_[int, Array]:
        """ GetDimensions(self: IDebugArrayObject, dwCount: UInt32) -> (int, Array[UInt32]) """
        ...

    def GetElement(self, dwIndex, ppElement) -> Tuple_[int, IDebugObject]:
        """ GetElement(self: IDebugArrayObject, dwIndex: UInt32) -> (int, IDebugObject) """
        ...

    def GetElements(self, ppEnum) -> Tuple_[int, IEnumDebugObjects]:
        """ GetElements(self: IDebugArrayObject) -> (int, IEnumDebugObjects) """
        ...

    def GetRank(self, pdwRank) -> Tuple_[int, UInt32]:
        """ GetRank(self: IDebugArrayObject) -> (int, UInt32) """
        ...


class IDebugArrayObject2(IDebugArrayObject): # skipped bases: <type 'IDebugObject'>, <type 'object'>
    """ no doc """
    def GetBaseIndices(self, dwRank, dwIndices) -> Tuple_[int, Array]:
        """ GetBaseIndices(self: IDebugArrayObject2, dwRank: UInt32) -> (int, Array[UInt32]) """
        ...

    def HasBaseIndices(self, pfHasBaseIndices) -> Tuple_[int, int]:
        """ HasBaseIndices(self: IDebugArrayObject2) -> (int, int) """
        ...


class IDebugAsyncOperation: # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self) -> int:
        """ Abort(self: IDebugAsyncOperation) -> int """
        ...

    def GetResult(self, phrResult, ppunkResult) -> Tuple_[int, int, object]:
        """ GetResult(self: IDebugAsyncOperation) -> (int, int, object) """
        ...

    def GetSyncDebugOperation(self, ppsdo) -> Tuple_[int, IDebugSyncOperation]:
        """ GetSyncDebugOperation(self: IDebugAsyncOperation) -> (int, IDebugSyncOperation) """
        ...

    def QueryIsComplete(self) -> int:
        """ QueryIsComplete(self: IDebugAsyncOperation) -> int """
        ...

    def Start(self, padocb:IDebugAsyncOperationCallBack) -> int:
        """ Start(self: IDebugAsyncOperation, padocb: IDebugAsyncOperationCallBack) -> int """
        ...


class IDebugAsyncOperationCallBack: # skipped bases: <type 'object'>
    """ no doc """
    def onComplete(self) -> int:
        """ onComplete(self: IDebugAsyncOperationCallBack) -> int """
        ...


class IDebugAttachCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugAttachSecurityCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def OnUnsafeAttach(self, pProcess:IDebugProcess2) -> int:
        """ OnUnsafeAttach(self: IDebugAttachSecurityCallback2, pProcess: IDebugProcess2) -> int """
        ...


class IDebugBeforeSymbolSearchEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetModuleName(self, pbstrModuleName) -> Tuple_[int, str]:
        """ GetModuleName(self: IDebugBeforeSymbolSearchEvent2) -> (int, str) """
        ...


class IDebugBinder: # skipped bases: <type 'object'>
    """ no doc """
    def Bind(self, pContainer, pField, ppObject) -> Tuple_[int, IDebugObject]:
        """ Bind(self: IDebugBinder, pContainer: IDebugObject, pField: IDebugField) -> (int, IDebugObject) """
        ...

    def GetFunctionObject(self, ppFunction) -> Tuple_[int, IDebugFunctionObject]:
        """ GetFunctionObject(self: IDebugBinder) -> (int, IDebugFunctionObject) """
        ...

    def GetMemoryContext(self, pField, dwConstant, ppMemCxt) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext(self: IDebugBinder, pField: IDebugField, dwConstant: UInt32) -> (int, IDebugMemoryContext2) """
        ...

    def ResolveDynamicType(self, pDynamic, ppResolved) -> Tuple_[int, IDebugField]:
        """ ResolveDynamicType(self: IDebugBinder, pDynamic: IDebugDynamicField) -> (int, IDebugField) """
        ...

    def ResolveRuntimeType(self, pObject, ppResolved) -> Tuple_[int, IDebugField]:
        """ ResolveRuntimeType(self: IDebugBinder, pObject: IDebugObject) -> (int, IDebugField) """
        ...


class IDebugBinder2: # skipped bases: <type 'object'>
    """ no doc """
    def GetExceptionObjectAndType(self, ppException, ppField) -> Tuple_[int, IDebugObject, IDebugField]:
        """ GetExceptionObjectAndType(self: IDebugBinder2) -> (int, IDebugObject, IDebugField) """
        ...

    def GetMemoryObject(self, pField, dwConstant, ppObject) -> Tuple_[int, IDebugObject]:
        """ GetMemoryObject(self: IDebugBinder2, pField: IDebugField, dwConstant: UInt32) -> (int, IDebugObject) """
        ...


class IDebugBinder3(IDebugBinder): # skipped bases: <type 'object'>
    """ no doc """
    def FindAlias(self, pcstrName, ppAlias) -> Tuple_[int, IDebugAlias]:
        """ FindAlias(self: IDebugBinder3, pcstrName: str) -> (int, IDebugAlias) """
        ...

    def GetAllAliases(self, uRequest, ppAliases, puFetched) -> Tuple_[int, Array, UInt32]:
        """ GetAllAliases(self: IDebugBinder3, uRequest: UInt32) -> (int, Array[IDebugAlias], UInt32) """
        ...

    def GetEEService(self, vendor, language, iid, ppService) -> Tuple_[int, object]:
        """ GetEEService(self: IDebugBinder3, vendor: Guid, language: Guid, iid: Guid) -> (int, object) """
        ...

    def GetExceptionObjectAndType(self, ppException, ppField) -> Tuple_[int, IDebugObject, IDebugField]:
        """ GetExceptionObjectAndType(self: IDebugBinder3) -> (int, IDebugObject, IDebugField) """
        ...

    def GetMemoryContext64(self, pField, uConstant, ppMemCxt) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext64(self: IDebugBinder3, pField: IDebugField, uConstant: UInt64) -> (int, IDebugMemoryContext2) """
        ...

    def GetMemoryObject(self, pField, uConstant, ppObject) -> Tuple_[int, IDebugObject]:
        """ GetMemoryObject(self: IDebugBinder3, pField: IDebugField, uConstant: UInt64) -> (int, IDebugObject) """
        ...

    def GetTypeArgumentCount(self, uCount) -> Tuple_[int, UInt32]:
        """ GetTypeArgumentCount(self: IDebugBinder3) -> (int, UInt32) """
        ...

    def GetTypeArguments(self, Skip, count, ppFields, pFetched) -> Tuple_[int, Array, UInt32]:
        """ GetTypeArguments(self: IDebugBinder3, Skip: UInt32, count: UInt32) -> (int, Array[IDebugField], UInt32) """
        ...


class IDebugBinderDirect: # skipped bases: <type 'object'>
    """ no doc """
    def CanDoFuncEval(self, pda:Array) -> int:
        """ CanDoFuncEval(self: IDebugBinderDirect, pda: Array[DEBUG_ADDRESS]) -> int """
        ...

    def ContinueForFuncEval(self, pCorEval:object, dwEvalFlags:UInt32, dwTimeout:UInt32) -> int:
        """ ContinueForFuncEval(self: IDebugBinderDirect, pCorEval: object, dwEvalFlags: UInt32, dwTimeout: UInt32) -> int """
        ...

    def CreateIDebugObject(self, pCorDebugValue, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateIDebugObject(self: IDebugBinderDirect, pCorDebugValue: object) -> (int, IDebugObject) """
        ...

    def GetAlias(self, pCorValue, ppAlias) -> Tuple_[int, IDebugAlias]:
        """ GetAlias(self: IDebugBinderDirect, pCorValue: object) -> (int, IDebugAlias) """
        ...

    def GetCORDBFrame(self, ppFrame) -> Tuple_[int, object]:
        """ GetCORDBFrame(self: IDebugBinderDirect) -> (int, object) """
        ...

    def GetCORDBModule(self, guid, appDomainID, ppModule) -> Tuple_[int, object]:
        """ GetCORDBModule(self: IDebugBinderDirect, guid: Guid, appDomainID: UInt32) -> (int, object) """
        ...

    def GetDebugProperty(self, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetDebugProperty(self: IDebugBinderDirect) -> (int, IDebugProperty2) """
        ...

    def GetMemoryContext(self, pda, dwConstant, ppMemCxt) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext(self: IDebugBinderDirect, pda: Array[DEBUG_ADDRESS], dwConstant: UInt64) -> (int, IDebugMemoryContext2) """
        ...

    def IsInEmbeddedClrMode(self, pfEmbeddedClrMode) -> Tuple_[int, int]:
        """ IsInEmbeddedClrMode(self: IDebugBinderDirect) -> (int, int) """
        ...

    def IsInSQLCLRMode(self, pfSQLCLRMode) -> Tuple_[int, int]:
        """ IsInSQLCLRMode(self: IDebugBinderDirect) -> (int, int) """
        ...

    def IsUserData(self, pda, pfUser) -> Tuple_[int, int]:
        """ IsUserData(self: IDebugBinderDirect, pda: Array[DEBUG_ADDRESS]) -> (int, int) """
        ...


class IDebugBitField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    def GetStart(self, pdwBitOffset) -> Tuple_[int, UInt32]:
        """ GetStart(self: IDebugBitField) -> (int, UInt32) """
        ...


class IDebugBoundBreakpoint2: # skipped bases: <type 'object'>
    """ no doc """
    def Delete(self) -> int:
        """ Delete(self: IDebugBoundBreakpoint2) -> int """
        ...

    def Enable(self, fEnable:int) -> int:
        """ Enable(self: IDebugBoundBreakpoint2, fEnable: int) -> int """
        ...

    def GetBreakpointResolution(self, ppBPResolution) -> Tuple_[int, IDebugBreakpointResolution2]:
        """ GetBreakpointResolution(self: IDebugBoundBreakpoint2) -> (int, IDebugBreakpointResolution2) """
        ...

    def GetHitCount(self, pdwHitCount) -> Tuple_[int, UInt32]:
        """ GetHitCount(self: IDebugBoundBreakpoint2) -> (int, UInt32) """
        ...

    def GetPendingBreakpoint(self, ppPendingBreakpoint) -> Tuple_[int, IDebugPendingBreakpoint2]:
        """ GetPendingBreakpoint(self: IDebugBoundBreakpoint2) -> (int, IDebugPendingBreakpoint2) """
        ...

    def GetState(self, pState) -> Tuple_[int, UInt32]:
        """ GetState(self: IDebugBoundBreakpoint2) -> (int, UInt32) """
        ...

    def SetCondition(self, bpCondition:BP_CONDITION) -> int:
        """ SetCondition(self: IDebugBoundBreakpoint2, bpCondition: BP_CONDITION) -> int """
        ...

    def SetHitCount(self, dwHitCount:UInt32) -> int:
        """ SetHitCount(self: IDebugBoundBreakpoint2, dwHitCount: UInt32) -> int """
        ...

    def SetPassCount(self, bpPassCount:BP_PASSCOUNT) -> int:
        """ SetPassCount(self: IDebugBoundBreakpoint2, bpPassCount: BP_PASSCOUNT) -> int """
        ...


class IDebugBoundBreakpoint3: # skipped bases: <type 'object'>
    """ no doc """
    def SetTracepoint(self, bpBstrTracepoint:str, bpFlags:UInt32) -> int:
        """ SetTracepoint(self: IDebugBoundBreakpoint3, bpBstrTracepoint: str, bpFlags: UInt32) -> int """
        ...


class IDebugBreakEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugBreakpointBoundEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumBoundBreakpoints(self, ppEnum) -> Tuple_[int, IEnumDebugBoundBreakpoints2]:
        """ EnumBoundBreakpoints(self: IDebugBreakpointBoundEvent2) -> (int, IEnumDebugBoundBreakpoints2) """
        ...

    def GetPendingBreakpoint(self, ppPendingBP) -> Tuple_[int, IDebugPendingBreakpoint2]:
        """ GetPendingBreakpoint(self: IDebugBreakpointBoundEvent2) -> (int, IDebugPendingBreakpoint2) """
        ...


class IDebugBreakpointChecksumRequest2: # skipped bases: <type 'object'>
    """ no doc """
    def GetChecksum(self, guidAlgorithm, pChecksumData) -> Tuple_[int, Guid, Array]:
        """ GetChecksum(self: IDebugBreakpointChecksumRequest2, guidAlgorithm: Guid) -> (int, Guid, Array[CHECKSUM_DATA]) """
        ...

    def IsChecksumEnabled(self, pfChecksumEnabled) -> Tuple_[int, int]:
        """ IsChecksumEnabled(self: IDebugBreakpointChecksumRequest2) -> (int, int) """
        ...


class IDebugBreakpointErrorEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetErrorBreakpoint(self, ppErrorBP) -> Tuple_[int, IDebugErrorBreakpoint2]:
        """ GetErrorBreakpoint(self: IDebugBreakpointErrorEvent2) -> (int, IDebugErrorBreakpoint2) """
        ...


class IDebugBreakpointEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumBreakpoints(self, ppEnum) -> Tuple_[int, IEnumDebugBoundBreakpoints2]:
        """ EnumBreakpoints(self: IDebugBreakpointEvent2) -> (int, IEnumDebugBoundBreakpoints2) """
        ...


class IDebugBreakpointRequest2: # skipped bases: <type 'object'>
    """ no doc """
    def GetLocationType(self, pBPLocationType) -> Tuple_[int, UInt32]:
        """ GetLocationType(self: IDebugBreakpointRequest2) -> (int, UInt32) """
        ...

    def GetRequestInfo(self, dwFields, pBPRequestInfo) -> Tuple_[int, Array]:
        """ GetRequestInfo(self: IDebugBreakpointRequest2, dwFields: UInt32) -> (int, Array[BP_REQUEST_INFO]) """
        ...


class IDebugBreakpointRequest3(IDebugBreakpointRequest2): # skipped bases: <type 'object'>
    """ no doc """
    def GetRequestInfo2(self, dwFields, bBPRequestInfo) -> Tuple_[int, Array]:
        """ GetRequestInfo2(self: IDebugBreakpointRequest3, dwFields: UInt32) -> (int, Array[BP_REQUEST_INFO2]) """
        ...


class IDebugBreakpointResolution2: # skipped bases: <type 'object'>
    """ no doc """
    def GetBreakpointType(self, pBPType) -> Tuple_[int, UInt32]:
        """ GetBreakpointType(self: IDebugBreakpointResolution2) -> (int, UInt32) """
        ...

    def GetResolutionInfo(self, dwFields, pBPResolutionInfo) -> Tuple_[int, Array]:
        """ GetResolutionInfo(self: IDebugBreakpointResolution2, dwFields: UInt32) -> (int, Array[BP_RESOLUTION_INFO]) """
        ...


class IDebugBreakpointUnboundEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetBreakpoint(self, ppBP) -> Tuple_[int, IDebugBoundBreakpoint2]:
        """ GetBreakpoint(self: IDebugBreakpointUnboundEvent2) -> (int, IDebugBoundBreakpoint2) """
        ...

    def GetReason(self, pdwUnboundReason) -> Tuple_[int, UInt32]:
        """ GetReason(self: IDebugBreakpointUnboundEvent2) -> (int, UInt32) """
        ...


class IDebugCanStopEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def CanStop(self, fCanStop:int) -> int:
        """ CanStop(self: IDebugCanStopEvent2, fCanStop: int) -> int """
        ...

    def GetCodeContext(self, ppCodeContext) -> Tuple_[int, IDebugCodeContext2]:
        """ GetCodeContext(self: IDebugCanStopEvent2) -> (int, IDebugCodeContext2) """
        ...

    def GetDocumentContext(self, ppDocCxt) -> Tuple_[int, IDebugDocumentContext2]:
        """ GetDocumentContext(self: IDebugCanStopEvent2) -> (int, IDebugDocumentContext2) """
        ...

    def GetReason(self, pcr) -> Tuple_[int, UInt32]:
        """ GetReason(self: IDebugCanStopEvent2) -> (int, UInt32) """
        ...


class IDebugClassField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def DoesInterfaceExist(self, pszInterfaceName:str) -> int:
        """ DoesInterfaceExist(self: IDebugClassField, pszInterfaceName: str) -> int """
        ...

    def EnumBaseClasses(self, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumBaseClasses(self: IDebugClassField) -> (int, IEnumDebugFields) """
        ...

    def EnumConstructors(self, cMatch, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumConstructors(self: IDebugClassField, cMatch: CONSTRUCTOR_ENUM) -> (int, IEnumDebugFields) """
        ...

    def EnumInterfacesImplemented(self, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumInterfacesImplemented(self: IDebugClassField) -> (int, IEnumDebugFields) """
        ...

    def EnumNestedClasses(self, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumNestedClasses(self: IDebugClassField) -> (int, IEnumDebugFields) """
        ...

    def EnumNestedEnums(self, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ EnumNestedEnums(self: IDebugClassField) -> (int, IEnumDebugFields) """
        ...

    def GetDefaultIndexer(self, pbstrIndexer) -> Tuple_[int, str]:
        """ GetDefaultIndexer(self: IDebugClassField) -> (int, str) """
        ...

    def GetEnclosingClass(self, ppClassField) -> Tuple_[int, IDebugClassField]:
        """ GetEnclosingClass(self: IDebugClassField) -> (int, IDebugClassField) """
        ...


class IDebugCodeContext: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocumentContext(self, ppsc) -> Tuple_[int, IDebugDocumentContext]:
        """ GetDocumentContext(self: IDebugCodeContext) -> (int, IDebugDocumentContext) """
        ...

    def SetBreakPoint(self, bps:BREAKPOINT_STATE) -> int:
        """ SetBreakPoint(self: IDebugCodeContext, bps: BREAKPOINT_STATE) -> int """
        ...


class IDebugMemoryContext2: # skipped bases: <type 'object'>
    """ no doc """
    def Add(self, dwCount, ppMemCxt) -> Tuple_[int, IDebugMemoryContext2]:
        """ Add(self: IDebugMemoryContext2, dwCount: UInt64) -> (int, IDebugMemoryContext2) """
        ...

    def Compare(self, Compare, rgpMemoryContextSet, dwMemoryContextSetLen, pdwMemoryContext) -> Tuple_[int, UInt32]:
        """ Compare(self: IDebugMemoryContext2, Compare: UInt32, rgpMemoryContextSet: Array[IDebugMemoryContext2], dwMemoryContextSetLen: UInt32) -> (int, UInt32) """
        ...

    def GetInfo(self, dwFields, pinfo) -> Tuple_[int, Array]:
        """ GetInfo(self: IDebugMemoryContext2, dwFields: UInt32) -> (int, Array[CONTEXT_INFO]) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugMemoryContext2) -> (int, str) """
        ...

    def Subtract(self, dwCount, ppMemCxt) -> Tuple_[int, IDebugMemoryContext2]:
        """ Subtract(self: IDebugMemoryContext2, dwCount: UInt64) -> (int, IDebugMemoryContext2) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...


class IDebugCodeContext2(IDebugMemoryContext2): # skipped bases: <type 'object'>
    """ no doc """
    def GetDocumentContext(self, ppSrcCxt) -> Tuple_[int, IDebugDocumentContext2]:
        """ GetDocumentContext(self: IDebugCodeContext2) -> (int, IDebugDocumentContext2) """
        ...

    def GetLanguageInfo(self, pbstrLanguage, pguidLanguage) -> Tuple_[int, str, Guid]:
        """ GetLanguageInfo(self: IDebugCodeContext2) -> (int, str, Guid) """
        ...


class IDebugCodeContext3(IDebugCodeContext2): # skipped bases: <type 'IDebugMemoryContext2'>, <type 'object'>
    """ no doc """
    def GetModule(self, ppModule) -> Tuple_[int, IDebugModule2]:
        """ GetModule(self: IDebugCodeContext3) -> (int, IDebugModule2) """
        ...

    def GetProcess(self, ppProcess) -> Tuple_[int, IDebugProcess2]:
        """ GetProcess(self: IDebugCodeContext3) -> (int, IDebugProcess2) """
        ...


class IDebugCOMPlusProgramNode2: # skipped bases: <type 'object'>
    """ no doc """
    def GetAppDomainId(self, pul32Id) -> Tuple_[int, UInt32]:
        """ GetAppDomainId(self: IDebugCOMPlusProgramNode2) -> (int, UInt32) """
        ...


class IDebugSymbolProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetAddressesFromContext(self, pDocContext, fStatmentOnly, ppEnumBegAddresses, ppEnumEndAddresses) -> Tuple_[int, IEnumDebugAddresses, IEnumDebugAddresses]:
        """ GetAddressesFromContext(self: IDebugSymbolProvider, pDocContext: IDebugDocumentContext2, fStatmentOnly: int) -> (int, IEnumDebugAddresses, IEnumDebugAddresses) """
        ...

    def GetAddressesFromPosition(self, pDocPos, fStatmentOnly, ppEnumBegAddresses, ppEnumEndAddresses) -> Tuple_[int, IEnumDebugAddresses, IEnumDebugAddresses]:
        """ GetAddressesFromPosition(self: IDebugSymbolProvider, pDocPos: IDebugDocumentPosition2, fStatmentOnly: int) -> (int, IEnumDebugAddresses, IEnumDebugAddresses) """
        ...

    def GetClassTypeByName(self, pszClassName, nameMatch, ppField) -> Tuple_[int, IDebugClassField]:
        """ GetClassTypeByName(self: IDebugSymbolProvider, pszClassName: str, nameMatch: NAME_MATCH) -> (int, IDebugClassField) """
        ...

    def GetContainerField(self, pAddress, ppContainerField) -> Tuple_[int, IDebugContainerField]:
        """ GetContainerField(self: IDebugSymbolProvider, pAddress: IDebugAddress) -> (int, IDebugContainerField) """
        ...

    def GetContextFromAddress(self, pAddress, ppDocContext) -> Tuple_[int, IDebugDocumentContext2]:
        """ GetContextFromAddress(self: IDebugSymbolProvider, pAddress: IDebugAddress) -> (int, IDebugDocumentContext2) """
        ...

    def GetField(self, pAddress, pAddressCur, ppField) -> Tuple_[int, IDebugField]:
        """ GetField(self: IDebugSymbolProvider, pAddress: IDebugAddress, pAddressCur: IDebugAddress) -> (int, IDebugField) """
        ...

    def GetGlobalContainer(self, pField) -> Tuple_[int, IDebugContainerField]:
        """ GetGlobalContainer(self: IDebugSymbolProvider) -> (int, IDebugContainerField) """
        ...

    def GetLanguage(self, pAddress, pguidLanguage, pguidLanguageVendor) -> Tuple_[int, Guid, Guid]:
        """ GetLanguage(self: IDebugSymbolProvider, pAddress: IDebugAddress) -> (int, Guid, Guid) """
        ...

    def GetMethodFieldsByName(self, pszFullName, nameMatch, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ GetMethodFieldsByName(self: IDebugSymbolProvider, pszFullName: str, nameMatch: NAME_MATCH) -> (int, IEnumDebugFields) """
        ...

    def GetNamespacesUsedAtAddress(self, pAddress, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ GetNamespacesUsedAtAddress(self: IDebugSymbolProvider, pAddress: IDebugAddress) -> (int, IEnumDebugFields) """
        ...

    def GetNextAddress(self, pAddress, fStatmentOnly, ppAddress) -> Tuple_[int, IDebugAddress]:
        """ GetNextAddress(self: IDebugSymbolProvider, pAddress: IDebugAddress, fStatmentOnly: int) -> (int, IDebugAddress) """
        ...

    def GetTypeByName(self, pszClassName, nameMatch, ppField) -> Tuple_[int, IDebugField]:
        """ GetTypeByName(self: IDebugSymbolProvider, pszClassName: str, nameMatch: NAME_MATCH) -> (int, IDebugField) """
        ...

    def Initialize(self, pServices:IDebugEngineSymbolProviderServices) -> int:
        """ Initialize(self: IDebugSymbolProvider, pServices: IDebugEngineSymbolProviderServices) -> int """
        ...

    def Uninitialize(self) -> int:
        """ Uninitialize(self: IDebugSymbolProvider) -> int """
        ...


class IDebugComPlusSymbolProvider(IDebugSymbolProvider): # skipped bases: <type 'object'>
    """ no doc """
    def AreSymbolsLoaded(self, ulAppDomainID:UInt32, guidModule:Guid) -> int:
        """ AreSymbolsLoaded(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid) -> int """
        ...

    def CreateTypeFromPrimitive(self, dwPrimType:UInt32, pAddress:IDebugAddress, ppType:IDebugField) -> Tuple_[int, IDebugField]:
        """ CreateTypeFromPrimitive(self: IDebugComPlusSymbolProvider, dwPrimType: UInt32, pAddress: IDebugAddress, ppType: IDebugField) -> (int, IDebugField) """
        ...

    def GetAddressesInModuleFromPosition(self, ulAppDomainID, guidModule, pDocPos, fStatmentOnly, ppEnumBegAddresses, ppEnumEndAddresses) -> Tuple_[int, IEnumDebugAddresses, IEnumDebugAddresses]:
        """ GetAddressesInModuleFromPosition(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid, pDocPos: IDebugDocumentPosition2, fStatmentOnly: int) -> (int, IEnumDebugAddresses, IEnumDebugAddresses) """
        ...

    def GetArrayTypeFromAddress(self, pAddress, pSig, dwSigLength, ppField) -> Tuple_[int, IDebugField]:
        """ GetArrayTypeFromAddress(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress, pSig: Array[Byte], dwSigLength: UInt32) -> (int, IDebugField) """
        ...

    def GetAssemblyName(self, ulAppDomainID, guidModule, pbstrName) -> Tuple_[int, str]:
        """ GetAssemblyName(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid) -> (int, str) """
        ...

    def GetAttributedClassesForLanguage(self, guidLanguage, pstrAttribute, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ GetAttributedClassesForLanguage(self: IDebugComPlusSymbolProvider, guidLanguage: Guid, pstrAttribute: str) -> (int, IEnumDebugFields) """
        ...

    def GetAttributedClassesinModule(self, ulAppDomainID, guidModule, pstrAttribute, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ GetAttributedClassesinModule(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid, pstrAttribute: str) -> (int, IEnumDebugFields) """
        ...

    def GetEntryPoint(self, ulAppDomainID, guidModule, ppAddress) -> Tuple_[int, IDebugAddress]:
        """ GetEntryPoint(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid) -> (int, IDebugAddress) """
        ...

    def GetFunctionLineOffset(self, pAddress, dwLine, ppNewAddress) -> Tuple_[int, IDebugAddress]:
        """ GetFunctionLineOffset(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress, dwLine: UInt32) -> (int, IDebugAddress) """
        ...

    def GetLocalVariablelayout(self):
        """ no doc """
        ...

    def GetNameFromToken(self, pMetadataImport, dwToken, pbstrName) -> Tuple_[int, str]:
        """ GetNameFromToken(self: IDebugComPlusSymbolProvider, pMetadataImport: object, dwToken: UInt32) -> (int, str) """
        ...

    def GetSymAttribute(self, ulAppDomainID, guidModule, tokParent, pstrName, cBuffer, pcBuffer, buffer) -> Tuple_[int, UInt32, Array]:
        """ GetSymAttribute(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid, tokParent: int, pstrName: str, cBuffer: UInt32) -> (int, UInt32, Array[Byte]) """
        ...

    def GetSymUnmanagedReader(self, ulAppDomainID, guidModule, ppSymUnmanagedReader) -> Tuple_[int, object]:
        """ GetSymUnmanagedReader(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid) -> (int, object) """
        ...

    def GetTypeFromAddress(self, pAddress, ppField) -> Tuple_[int, IDebugField]:
        """ GetTypeFromAddress(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress) -> (int, IDebugField) """
        ...

    def IsFunctionDeleted(self, pAddress:IDebugAddress) -> int:
        """ IsFunctionDeleted(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress) -> int """
        ...

    def IsFunctionStale(self, pAddress:IDebugAddress) -> int:
        """ IsFunctionStale(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress) -> int """
        ...

    def IsHiddenCode(self, pAddress:IDebugAddress) -> int:
        """ IsHiddenCode(self: IDebugComPlusSymbolProvider, pAddress: IDebugAddress) -> int """
        ...

    def LoadSymbols(self, ulAppDomainID:UInt32, guidModule:Guid, baseAddress:UInt64, pUnkMetadataImport:object, bstrModuleName:str, bstrSymSearchPath:str) -> int:
        """ LoadSymbols(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid, baseAddress: UInt64, pUnkMetadataImport: object, bstrModuleName: str, bstrSymSearchPath: str) -> int """
        ...

    def LoadSymbolsFromStream(self):
        """ no doc """
        ...

    def ReplaceSymbols(self):
        """ no doc """
        ...

    def UnloadSymbols(self, ulAppDomainID:UInt32, guidModule:Guid) -> int:
        """ UnloadSymbols(self: IDebugComPlusSymbolProvider, ulAppDomainID: UInt32, guidModule: Guid) -> int """
        ...

    def UpdateSymbols(self):
        """ no doc """
        ...


class IDebugComPlusSymbolProvider2(IDebugComPlusSymbolProvider): # skipped bases: <type 'IDebugSymbolProvider'>, <type 'object'>
    """ no doc """
    def FunctionHasLineInfo(self, pAddress:IDebugAddress) -> int:
        """ FunctionHasLineInfo(self: IDebugComPlusSymbolProvider2, pAddress: IDebugAddress) -> int """
        ...

    def GetTypeFromToken(self, appDomain, guidModule, tdToken, ppField) -> Tuple_[int, IDebugField]:
        """ GetTypeFromToken(self: IDebugComPlusSymbolProvider2, appDomain: UInt32, guidModule: Guid, tdToken: UInt32) -> (int, IDebugField) """
        ...

    def GetTypesByName(self, pszClassName, nameMatch, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ GetTypesByName(self: IDebugComPlusSymbolProvider2, pszClassName: str, nameMatch: NAME_MATCH) -> (int, IEnumDebugFields) """
        ...

    def IsAddressSequencePoint(self, pAddress:IDebugAddress) -> int:
        """ IsAddressSequencePoint(self: IDebugComPlusSymbolProvider2, pAddress: IDebugAddress) -> int """
        ...

    def LoadSymbolsFromCallback(self, ulAppDomainID:UInt32, guidModule:Guid, pUnkMetadataImport:object, pUnkCorDebugModule:object, bstrModuleName:str, bstrSymSearchPath:str, pCallback:object) -> int:
        """ LoadSymbolsFromCallback(self: IDebugComPlusSymbolProvider2, ulAppDomainID: UInt32, guidModule: Guid, pUnkMetadataImport: object, pUnkCorDebugModule: object, bstrModuleName: str, bstrSymSearchPath: str, pCallback: object) -> int """
        ...

    def LoadSymbolsFromStreamWithCorModule(self):
        """ no doc """
        ...

    def LoadSymbolsWithCorModule(self, ulAppDomainID:UInt32, guidModule:Guid, baseAddress:UInt64, pUnkMetadataImport:object, pUnkCorDebugModule:object, bstrModuleName:str, bstrSymSearchPath:str) -> int:
        """ LoadSymbolsWithCorModule(self: IDebugComPlusSymbolProvider2, ulAppDomainID: UInt32, guidModule: Guid, baseAddress: UInt64, pUnkMetadataImport: object, pUnkCorDebugModule: object, bstrModuleName: str, bstrSymSearchPath: str) -> int """
        ...


class IDebugComPlusSymbolSearchInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetLastSymbolSearchInfo(self, ulAppDomainID, guidModule, pbstrPath, phrHRESULT) -> Tuple_[int, str, int]:
        """ GetLastSymbolSearchInfo(self: IDebugComPlusSymbolSearchInfo, ulAppDomainID: UInt32, guidModule: Guid) -> (int, str, int) """
        ...

    def GetSymbolSearchInfo(self, ulAppDomainID, guidModule, ulSearchInfo, pulSearchInfo, prgSearchInfo) -> Tuple_[int, UInt32, Array]:
        """ GetSymbolSearchInfo(self: IDebugComPlusSymbolSearchInfo, ulAppDomainID: UInt32, guidModule: Guid, ulSearchInfo: UInt32) -> (int, UInt32, Array[IntPtr]) """
        ...

    def GetSymbolSearchInfoCount(self, ulAppDomainID, guidModule, pCount) -> Tuple_[int, UInt32]:
        """ GetSymbolSearchInfoCount(self: IDebugComPlusSymbolSearchInfo, ulAppDomainID: UInt32, guidModule: Guid) -> (int, UInt32) """
        ...

    def LoadSymbolsWithoutPDB(self, ulAppDomainID:UInt32, guidModule:Guid, baseAddress:UInt64, pUnkMetadataImport:object, pUnkCorDebugModule:object, bstrModule:str) -> int:
        """ LoadSymbolsWithoutPDB(self: IDebugComPlusSymbolSearchInfo, ulAppDomainID: UInt32, guidModule: Guid, baseAddress: UInt64, pUnkMetadataImport: object, pUnkCorDebugModule: object, bstrModule: str) -> int """
        ...


class IDebugConsoleWindow: # skipped bases: <type 'object'>
    """ no doc """
    def ClearContents(self) -> int:
        """ ClearContents(self: IDebugConsoleWindow) -> int """
        ...

    def CreateToolWindow(self) -> int:
        """ CreateToolWindow(self: IDebugConsoleWindow) -> int """
        ...

    def Hide(self) -> int:
        """ Hide(self: IDebugConsoleWindow) -> int """
        ...

    def NotifyUserPid(self, dwPid:UInt32) -> int:
        """ NotifyUserPid(self: IDebugConsoleWindow, dwPid: UInt32) -> int """
        ...

    def SetFontAndColor(self, logFont:LOGFONTW, foreGroundColor:UInt32, backGroundColor:UInt32) -> int:
        """ SetFontAndColor(self: IDebugConsoleWindow, logFont: LOGFONTW, foreGroundColor: UInt32, backGroundColor: UInt32) -> int """
        ...

    def SetGuidsAndCommandIds(self, _SID_SVsUIShell:Guid, _SID_OleComponentUIManager:Guid, _guidVSStd97:Guid, _guidVSDebugCommand:Guid, _guidVSDebugGroup:Guid, _cmdidCut:UInt32, _cmdidCopy:UInt32, _cmdidPaste:UInt32, _cmdidConsoleSendEndOfFile:UInt32, _cmdidClear:UInt32, _IDM_CONSOLE_CONTEXT:UInt32) -> Tuple_[int, Guid, Guid, Guid, Guid, Guid]:
        """ SetGuidsAndCommandIds(self: IDebugConsoleWindow, _SID_SVsUIShell: Guid, _SID_OleComponentUIManager: Guid, _guidVSStd97: Guid, _guidVSDebugCommand: Guid, _guidVSDebugGroup: Guid, _cmdidCut: UInt32, _cmdidCopy: UInt32, _cmdidPaste: UInt32, _cmdidConsoleSendEndOfFile: UInt32, _cmdidClear: UInt32, _IDM_CONSOLE_CONTEXT: UInt32) -> (int, Guid, Guid, Guid, Guid, Guid) """
        ...

    def SetSite(self):
        """ no doc """
        ...

    def SetToolWindowProperties(self, lpszToolWindowTitle:str, dwBitmapResourceId:UInt32, dwBitmapIndex:UInt32, guidToolWindowId:Guid) -> Tuple_[int, Guid]:
        """ SetToolWindowProperties(self: IDebugConsoleWindow, lpszToolWindowTitle: str, dwBitmapResourceId: UInt32, dwBitmapIndex: UInt32, guidToolWindowId: Guid) -> (int, Guid) """
        ...

    def Show(self) -> int:
        """ Show(self: IDebugConsoleWindow) -> int """
        ...

    def StartListening(self) -> int:
        """ StartListening(self: IDebugConsoleWindow) -> int """
        ...


class IDebugCookie: # skipped bases: <type 'object'>
    """ no doc """
    def SetDebugCookie(self, dwDebugAppCookie:UInt32) -> int:
        """ SetDebugCookie(self: IDebugCookie, dwDebugAppCookie: UInt32) -> int """
        ...


class IDebugCoreServer2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumPorts(self, ppEnum) -> Tuple_[int, IEnumDebugPorts2]:
        """ EnumPorts(self: IDebugCoreServer2) -> (int, IEnumDebugPorts2) """
        ...

    def EnumPortSuppliers(self, ppEnum) -> Tuple_[int, IEnumDebugPortSuppliers2]:
        """ EnumPortSuppliers(self: IDebugCoreServer2) -> (int, IEnumDebugPortSuppliers2) """
        ...

    def GetMachineInfo(self, Fields, pMachineInfo) -> Tuple_[int, Array]:
        """ GetMachineInfo(self: IDebugCoreServer2, Fields: UInt32) -> (int, Array[MACHINE_INFO]) """
        ...

    def GetMachineName(self, pbstrName) -> Tuple_[int, str]:
        """ GetMachineName(self: IDebugCoreServer2) -> (int, str) """
        ...

    def GetMachineUtilities_V7(self, ppUtil) -> Tuple_[int, IDebugMDMUtil2_V7]:
        """ GetMachineUtilities_V7(self: IDebugCoreServer2) -> (int, IDebugMDMUtil2_V7) """
        ...

    def GetPort(self, guidPort, ppPort) -> Tuple_[int, Guid, IDebugPort2]:
        """ GetPort(self: IDebugCoreServer2, guidPort: Guid) -> (int, Guid, IDebugPort2) """
        ...

    def GetPortSupplier(self, guidPortSupplier, ppPortSupplier) -> Tuple_[int, Guid, IDebugPortSupplier2]:
        """ GetPortSupplier(self: IDebugCoreServer2, guidPortSupplier: Guid) -> (int, Guid, IDebugPortSupplier2) """
        ...


class IDebugCoreServer3(IDebugCoreServer2): # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstanceInServer(self, szDll, wLangID, clsidObject, riid, ppvObject) -> Tuple_[int, Guid, Guid, IntPtr]:
        """ CreateInstanceInServer(self: IDebugCoreServer3, szDll: str, wLangID: UInt16, clsidObject: Guid, riid: Guid) -> (int, Guid, Guid, IntPtr) """
        ...

    def DiagnoseWebDebuggingError(self, pszUrl:str) -> int:
        """ DiagnoseWebDebuggingError(self: IDebugCoreServer3, pszUrl: str) -> int """
        ...

    def DisableAutoAttach(self) -> int:
        """ DisableAutoAttach(self: IDebugCoreServer3) -> int """
        ...

    def EnableAutoAttach(self, rgguidSpecificEngines, celtSpecificEngines, pszStartPageUrl, pbstrSessionId) -> Tuple_[int, str]:
        """ EnableAutoAttach(self: IDebugCoreServer3, rgguidSpecificEngines: Array[Guid], celtSpecificEngines: UInt32, pszStartPageUrl: str) -> (int, str) """
        ...

    def GetConnectionProtocol(self, pProtocol) -> Tuple_[int, Array]:
        """ GetConnectionProtocol(self: IDebugCoreServer3) -> (int, Array[CONNECTION_PROTOCOL]) """
        ...

    def GetServerFriendlyName(self, pbstrName) -> Tuple_[int, str]:
        """ GetServerFriendlyName(self: IDebugCoreServer3) -> (int, str) """
        ...

    def GetServerName(self, pbstrName) -> Tuple_[int, str]:
        """ GetServerName(self: IDebugCoreServer3) -> (int, str) """
        ...

    def QueryIsLocal(self) -> int:
        """ QueryIsLocal(self: IDebugCoreServer3) -> int """
        ...


class IDebugCustomAttribute: # skipped bases: <type 'object'>
    """ no doc """
    def GetAttributeBytes(self, ppBlob, pdwLen) -> Tuple_[int, Array, UInt32]:
        """ GetAttributeBytes(self: IDebugCustomAttribute) -> (int, Array[Byte], UInt32) """
        ...

    def GetAttributeTypeField(self, ppCAType) -> Tuple_[int, IDebugClassField]:
        """ GetAttributeTypeField(self: IDebugCustomAttribute) -> (int, IDebugClassField) """
        ...

    def GetName(self, bstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugCustomAttribute) -> (int, str) """
        ...

    def GetParentField(self, ppField) -> Tuple_[int, IDebugField]:
        """ GetParentField(self: IDebugCustomAttribute) -> (int, IDebugField) """
        ...


class IDebugCustomAttributeQuery: # skipped bases: <type 'object'>
    """ no doc """
    def GetCustomAttributeByName(self, pszCustomAttributeName, ppBlob, pdwLen) -> Tuple_[int, Array, UInt32]:
        """ GetCustomAttributeByName(self: IDebugCustomAttributeQuery, pszCustomAttributeName: str) -> (int, Array[Byte], UInt32) """
        ...

    def IsCustomAttributeDefined(self, pszCustomAttributeName:str) -> int:
        """ IsCustomAttributeDefined(self: IDebugCustomAttributeQuery, pszCustomAttributeName: str) -> int """
        ...


class IDebugCustomAttributeQuery2(IDebugCustomAttributeQuery): # skipped bases: <type 'object'>
    """ no doc """
    def EnumCustomAttributes(self, ppEnum) -> Tuple_[int, IEnumDebugCustomAttributes]:
        """ EnumCustomAttributes(self: IDebugCustomAttributeQuery2) -> (int, IEnumDebugCustomAttributes) """
        ...


class IDebugCustomViewer: # skipped bases: <type 'object'>
    """ no doc """
    def DisplayValue(self, hwnd:IntPtr, dwID:UInt32, pHostServices:object, pDebugProperty:IDebugProperty3) -> int:
        """ DisplayValue(self: IDebugCustomViewer, hwnd: IntPtr, dwID: UInt32, pHostServices: object, pDebugProperty: IDebugProperty3) -> int """
        ...


class IDebugDataGrid: # skipped bases: <type 'object'>
    """ no doc """
    def GetGridInfo(self, pX, pY, bpstrTitle) -> Tuple_[int, UInt32, UInt32, str]:
        """ GetGridInfo(self: IDebugDataGrid) -> (int, UInt32, UInt32, str) """
        ...

    def GetGridPropertyInfo(self, x, y, celtX, celtY, celtXtimesY, dwFields, dwRadix, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ GetGridPropertyInfo(self: IDebugDataGrid, x: UInt32, y: UInt32, celtX: UInt32, celtY: UInt32, celtXtimesY: UInt32, dwFields: UInt32, dwRadix: UInt32) -> (int, Array[DEBUG_PROPERTY_INFO], UInt32) """
        ...


class IDebugPort2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumProcesses(self, ppEnum) -> Tuple_[int, IEnumDebugProcesses2]:
        """ EnumProcesses(self: IDebugPort2) -> (int, IEnumDebugProcesses2) """
        ...

    def GetPortId(self, pguidPort) -> Tuple_[int, Guid]:
        """ GetPortId(self: IDebugPort2) -> (int, Guid) """
        ...

    def GetPortName(self, pbstrName) -> Tuple_[int, str]:
        """ GetPortName(self: IDebugPort2) -> (int, str) """
        ...

    def GetPortRequest(self, ppRequest) -> Tuple_[int, IDebugPortRequest2]:
        """ GetPortRequest(self: IDebugPort2) -> (int, IDebugPortRequest2) """
        ...

    def GetPortSupplier(self, ppSupplier) -> Tuple_[int, IDebugPortSupplier2]:
        """ GetPortSupplier(self: IDebugPort2) -> (int, IDebugPortSupplier2) """
        ...

    def GetProcess(self, ProcessId, ppProcess) -> Tuple_[int, IDebugProcess2]:
        """ GetProcess(self: IDebugPort2, ProcessId: AD_PROCESS_ID) -> (int, IDebugProcess2) """
        ...


class IDebugDefaultPort2(IDebugPort2): # skipped bases: <type 'object'>
    """ no doc """
    def GetPortNotify(self, ppPortNotify) -> Tuple_[int, IDebugPortNotify2]:
        """ GetPortNotify(self: IDebugDefaultPort2) -> (int, IDebugPortNotify2) """
        ...

    def GetServer(self, ppServer) -> Tuple_[int, IDebugCoreServer3]:
        """ GetServer(self: IDebugDefaultPort2) -> (int, IDebugCoreServer3) """
        ...

    def QueryIsLocal(self) -> int:
        """ QueryIsLocal(self: IDebugDefaultPort2) -> int """
        ...


class IDebugDisassemblyStream2: # skipped bases: <type 'object'>
    """ no doc """
    def GetCodeContext(self, uCodeLocationId, ppCodeContext) -> Tuple_[int, IDebugCodeContext2]:
        """ GetCodeContext(self: IDebugDisassemblyStream2, uCodeLocationId: UInt64) -> (int, IDebugCodeContext2) """
        ...

    def GetCodeLocationId(self, pCodeContext, puCodeLocationId) -> Tuple_[int, UInt64]:
        """ GetCodeLocationId(self: IDebugDisassemblyStream2, pCodeContext: IDebugCodeContext2) -> (int, UInt64) """
        ...

    def GetCurrentLocation(self, puCodeLocationId) -> Tuple_[int, UInt64]:
        """ GetCurrentLocation(self: IDebugDisassemblyStream2) -> (int, UInt64) """
        ...

    def GetDocument(self, bstrDocumentUrl, ppDocument) -> Tuple_[int, IDebugDocument2]:
        """ GetDocument(self: IDebugDisassemblyStream2, bstrDocumentUrl: str) -> (int, IDebugDocument2) """
        ...

    def GetScope(self, pdwScope) -> Tuple_[int, UInt32]:
        """ GetScope(self: IDebugDisassemblyStream2) -> (int, UInt32) """
        ...

    def GetSize(self, pnSize) -> Tuple_[int, UInt64]:
        """ GetSize(self: IDebugDisassemblyStream2) -> (int, UInt64) """
        ...

    def Read(self, dwInstructions, dwFields, pdwInstructionsRead, prgDisassembly) -> Tuple_[int, UInt32, Array]:
        """ Read(self: IDebugDisassemblyStream2, dwInstructions: UInt32, dwFields: UInt32) -> (int, UInt32, Array[DisassemblyData]) """
        ...

    def Seek(self, dwSeekStart:UInt32, pCodeContext:IDebugCodeContext2, uCodeLocationId:UInt64, iInstructions:Int64) -> int:
        """ Seek(self: IDebugDisassemblyStream2, dwSeekStart: UInt32, pCodeContext: IDebugCodeContext2, uCodeLocationId: UInt64, iInstructions: Int64) -> int """
        ...


class IDebugDocument(IDebugDocumentInfo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugDocument2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocumentClassId(self, pclsid) -> Tuple_[int, Guid]:
        """ GetDocumentClassId(self: IDebugDocument2) -> (int, Guid) """
        ...

    def GetName(self, gnType, pbstrFileName) -> Tuple_[int, str]:
        """ GetName(self: IDebugDocument2, gnType: UInt32) -> (int, str) """
        ...


class IDebugDocumentChecksum2: # skipped bases: <type 'object'>
    """ no doc """
    def GetChecksumAndAlgorithmId(self, pRetVal, cMaxBytes, pChecksum, pcNumBytes) -> Tuple_[int, Guid, Array, UInt32]:
        """ GetChecksumAndAlgorithmId(self: IDebugDocumentChecksum2, cMaxBytes: UInt32) -> (int, Guid, Array[Byte], UInt32) """
        ...


class IDebugDocumentContext: # skipped bases: <type 'object'>
    """ no doc """
    def EnumCodeContexts(self, ppescc) -> Tuple_[int, IEnumDebugCodeContexts]:
        """ EnumCodeContexts(self: IDebugDocumentContext) -> (int, IEnumDebugCodeContexts) """
        ...

    def GetDocument(self, ppsd) -> Tuple_[int, IDebugDocument]:
        """ GetDocument(self: IDebugDocumentContext) -> (int, IDebugDocument) """
        ...


class IDebugDocumentContext2: # skipped bases: <type 'object'>
    """ no doc """
    def Compare(self, Compare, rgpDocContextSet, dwDocContextSetLen, pdwDocContext) -> Tuple_[int, UInt32]:
        """ Compare(self: IDebugDocumentContext2, Compare: UInt32, rgpDocContextSet: Array[IDebugDocumentContext2], dwDocContextSetLen: UInt32) -> (int, UInt32) """
        ...

    def EnumCodeContexts(self, ppEnumCodeCxts) -> Tuple_[int, IEnumDebugCodeContexts2]:
        """ EnumCodeContexts(self: IDebugDocumentContext2) -> (int, IEnumDebugCodeContexts2) """
        ...

    def GetDocument(self, ppDocument) -> Tuple_[int, IDebugDocument2]:
        """ GetDocument(self: IDebugDocumentContext2) -> (int, IDebugDocument2) """
        ...

    def GetLanguageInfo(self, pbstrLanguage, pguidLanguage) -> Tuple_[int, str, Guid]:
        """ GetLanguageInfo(self: IDebugDocumentContext2) -> (int, str, Guid) """
        ...

    def GetName(self, gnType, pbstrFileName) -> Tuple_[int, str]:
        """ GetName(self: IDebugDocumentContext2, gnType: UInt32) -> (int, str) """
        ...

    def GetSourceRange(self, pBegPosition, pEndPosition) -> Tuple_[int, Array, Array]:
        """ GetSourceRange(self: IDebugDocumentContext2) -> (int, Array[TEXT_POSITION], Array[TEXT_POSITION]) """
        ...

    def GetStatementRange(self, pBegPosition, pEndPosition) -> Tuple_[int, Array, Array]:
        """ GetStatementRange(self: IDebugDocumentContext2) -> (int, Array[TEXT_POSITION], Array[TEXT_POSITION]) """
        ...

    def Seek(self, nCount, ppDocContext) -> Tuple_[int, IDebugDocumentContext2]:
        """ Seek(self: IDebugDocumentContext2, nCount: int) -> (int, IDebugDocumentContext2) """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...


class IDebugDocumentHelper32: # skipped bases: <type 'object'>
    """ no doc """
    def AddDBCSText(self, pszText:str) -> int:
        """ AddDBCSText(self: IDebugDocumentHelper32, pszText: str) -> int """
        ...

    def AddDeferredText(self, cChars:UInt32, dwTextStartCookie:UInt32) -> int:
        """ AddDeferredText(self: IDebugDocumentHelper32, cChars: UInt32, dwTextStartCookie: UInt32) -> int """
        ...

    def AddUnicodeText(self, pszText:str) -> int:
        """ AddUnicodeText(self: IDebugDocumentHelper32, pszText: str) -> int """
        ...

    def Attach(self, pddhParent:IDebugDocumentHelper32) -> int:
        """ Attach(self: IDebugDocumentHelper32, pddhParent: IDebugDocumentHelper32) -> int """
        ...

    def BringDocumentContextToTop(self, pddc:IDebugDocumentContext) -> int:
        """ BringDocumentContextToTop(self: IDebugDocumentHelper32, pddc: IDebugDocumentContext) -> int """
        ...

    def BringDocumentToTop(self) -> int:
        """ BringDocumentToTop(self: IDebugDocumentHelper32) -> int """
        ...

    def CreateDebugDocumentContext(self, iCharPos, cChars, ppddc) -> Tuple_[int, IDebugDocumentContext]:
        """ CreateDebugDocumentContext(self: IDebugDocumentHelper32, iCharPos: UInt32, cChars: UInt32) -> (int, IDebugDocumentContext) """
        ...

    def DefineScriptBlock(self, ulCharOffset, cChars, pas, fScriptlet, pdwSourceContext) -> Tuple_[int, UInt32]:
        """ DefineScriptBlock(self: IDebugDocumentHelper32, ulCharOffset: UInt32, cChars: UInt32, pas: IActiveScript, fScriptlet: int) -> (int, UInt32) """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugDocumentHelper32) -> int """
        ...

    def GetDebugApplicationNode(self, ppdan) -> Tuple_[int, IDebugApplicationNode]:
        """ GetDebugApplicationNode(self: IDebugDocumentHelper32) -> (int, IDebugApplicationNode) """
        ...

    def GetScriptBlockInfo(self, dwSourceContext, ppasd, piCharPos, pcChars) -> Tuple_[int, IActiveScript, UInt32, UInt32]:
        """ GetScriptBlockInfo(self: IDebugDocumentHelper32, dwSourceContext: UInt32) -> (int, IActiveScript, UInt32, UInt32) """
        ...

    def Init(self, pda:IDebugApplication32, pszShortName:str, pszLongName:str, docAttr:UInt32) -> int:
        """ Init(self: IDebugDocumentHelper32, pda: IDebugApplication32, pszShortName: str, pszLongName: str, docAttr: UInt32) -> int """
        ...

    def SetDebugDocumentHost(self, pddh:IDebugDocumentHost) -> int:
        """ SetDebugDocumentHost(self: IDebugDocumentHelper32, pddh: IDebugDocumentHost) -> int """
        ...

    def SetDefaultTextAttr(self, staTextAttr:UInt16) -> int:
        """ SetDefaultTextAttr(self: IDebugDocumentHelper32, staTextAttr: UInt16) -> int """
        ...

    def SetDocumentAttr(self, pszAttributes:UInt32) -> int:
        """ SetDocumentAttr(self: IDebugDocumentHelper32, pszAttributes: UInt32) -> int """
        ...

    def SetLongName(self, pszLongName:str) -> int:
        """ SetLongName(self: IDebugDocumentHelper32, pszLongName: str) -> int """
        ...

    def SetShortName(self, pszShortName:str) -> int:
        """ SetShortName(self: IDebugDocumentHelper32, pszShortName: str) -> int """
        ...

    def SetTextAttributes(self, ulCharOffset:UInt32, cChars:UInt32, pstaTextAttr:Array) -> int:
        """ SetTextAttributes(self: IDebugDocumentHelper32, ulCharOffset: UInt32, cChars: UInt32, pstaTextAttr: Array[UInt16]) -> int """
        ...


class IDebugDocumentHelper64: # skipped bases: <type 'object'>
    """ no doc """
    def AddDBCSText(self, pszText:str) -> int:
        """ AddDBCSText(self: IDebugDocumentHelper64, pszText: str) -> int """
        ...

    def AddDeferredText(self, cChars:UInt32, dwTextStartCookie:UInt32) -> int:
        """ AddDeferredText(self: IDebugDocumentHelper64, cChars: UInt32, dwTextStartCookie: UInt32) -> int """
        ...

    def AddUnicodeText(self, pszText:str) -> int:
        """ AddUnicodeText(self: IDebugDocumentHelper64, pszText: str) -> int """
        ...

    def Attach(self, pddhParent:IDebugDocumentHelper64) -> int:
        """ Attach(self: IDebugDocumentHelper64, pddhParent: IDebugDocumentHelper64) -> int """
        ...

    def BringDocumentContextToTop(self, pddc:IDebugDocumentContext) -> int:
        """ BringDocumentContextToTop(self: IDebugDocumentHelper64, pddc: IDebugDocumentContext) -> int """
        ...

    def BringDocumentToTop(self) -> int:
        """ BringDocumentToTop(self: IDebugDocumentHelper64) -> int """
        ...

    def CreateDebugDocumentContext(self, iCharPos, cChars, ppddc) -> Tuple_[int, IDebugDocumentContext]:
        """ CreateDebugDocumentContext(self: IDebugDocumentHelper64, iCharPos: UInt32, cChars: UInt32) -> (int, IDebugDocumentContext) """
        ...

    def DefineScriptBlock(self, ulCharOffset, cChars, pas, fScriptlet, pdwSourceContext) -> Tuple_[int, UInt64]:
        """ DefineScriptBlock(self: IDebugDocumentHelper64, ulCharOffset: UInt32, cChars: UInt32, pas: IActiveScript, fScriptlet: int) -> (int, UInt64) """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugDocumentHelper64) -> int """
        ...

    def GetDebugApplicationNode(self, ppdan) -> Tuple_[int, IDebugApplicationNode]:
        """ GetDebugApplicationNode(self: IDebugDocumentHelper64) -> (int, IDebugApplicationNode) """
        ...

    def GetScriptBlockInfo(self, dwSourceContext, ppasd, piCharPos, pcChars) -> Tuple_[int, IActiveScript, UInt32, UInt32]:
        """ GetScriptBlockInfo(self: IDebugDocumentHelper64, dwSourceContext: UInt64) -> (int, IActiveScript, UInt32, UInt32) """
        ...

    def Init(self, pda:IDebugApplication64, pszShortName:str, pszLongName:str, docAttr:UInt32) -> int:
        """ Init(self: IDebugDocumentHelper64, pda: IDebugApplication64, pszShortName: str, pszLongName: str, docAttr: UInt32) -> int """
        ...

    def SetDebugDocumentHost(self, pddh:IDebugDocumentHost) -> int:
        """ SetDebugDocumentHost(self: IDebugDocumentHelper64, pddh: IDebugDocumentHost) -> int """
        ...

    def SetDefaultTextAttr(self, staTextAttr:UInt16) -> int:
        """ SetDefaultTextAttr(self: IDebugDocumentHelper64, staTextAttr: UInt16) -> int """
        ...

    def SetDocumentAttr(self, pszAttributes:UInt32) -> int:
        """ SetDocumentAttr(self: IDebugDocumentHelper64, pszAttributes: UInt32) -> int """
        ...

    def SetLongName(self, pszLongName:str) -> int:
        """ SetLongName(self: IDebugDocumentHelper64, pszLongName: str) -> int """
        ...

    def SetShortName(self, pszShortName:str) -> int:
        """ SetShortName(self: IDebugDocumentHelper64, pszShortName: str) -> int """
        ...

    def SetTextAttributes(self, ulCharOffset:UInt32, cChars:UInt32, pstaTextAttr:Array) -> int:
        """ SetTextAttributes(self: IDebugDocumentHelper64, ulCharOffset: UInt32, cChars: UInt32, pstaTextAttr: Array[UInt16]) -> int """
        ...


class IDebugDocumentHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetDeferredText(self, dwTextStartCookie, pcharText, pstaTextAttr, pcNumChars, cMaxChars) -> Tuple_[int, Array, UInt32]:
        """ GetDeferredText(self: IDebugDocumentHost, dwTextStartCookie: UInt32, pcharText: IntPtr, cMaxChars: UInt32) -> (int, Array[UInt16], UInt32) """
        ...

    def GetFileName(self, pbstrShortName) -> Tuple_[int, str]:
        """ GetFileName(self: IDebugDocumentHost) -> (int, str) """
        ...

    def GetPathName(self, pbstrLongName, pfIsOriginalFile) -> Tuple_[int, str, int]:
        """ GetPathName(self: IDebugDocumentHost) -> (int, str, int) """
        ...

    def GetScriptTextAttributes(self, pstrCode, uNumCodeChars, pstrDelimiter, dwFlags, pattr) -> Tuple_[int, Array]:
        """ GetScriptTextAttributes(self: IDebugDocumentHost, pstrCode: Array[str], uNumCodeChars: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, Array[UInt16]) """
        ...

    def NotifyChanged(self) -> int:
        """ NotifyChanged(self: IDebugDocumentHost) -> int """
        ...

    def OnCreateDocumentContext(self, ppunkOuter) -> Tuple_[int, object]:
        """ OnCreateDocumentContext(self: IDebugDocumentHost) -> (int, object) """
        ...


class IDebugDocumentPosition2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDocument(self, ppDoc) -> Tuple_[int, IDebugDocument2]:
        """ GetDocument(self: IDebugDocumentPosition2) -> (int, IDebugDocument2) """
        ...

    def GetFileName(self, pbstrFileName) -> Tuple_[int, str]:
        """ GetFileName(self: IDebugDocumentPosition2) -> (int, str) """
        ...

    def GetRange(self, pBegPosition, pEndPosition) -> Tuple_[int, Array, Array]:
        """ GetRange(self: IDebugDocumentPosition2) -> (int, Array[TEXT_POSITION], Array[TEXT_POSITION]) """
        ...

    def IsPositionInDocument(self, pDoc:IDebugDocument2) -> int:
        """ IsPositionInDocument(self: IDebugDocumentPosition2, pDoc: IDebugDocument2) -> int """
        ...


class IDebugDocumentPositionOffset2: # skipped bases: <type 'object'>
    """ no doc """
    def GetRange(self, pdwBegOffset, pdwEndOffset) -> Tuple_[int, UInt32, UInt32]:
        """ GetRange(self: IDebugDocumentPositionOffset2) -> (int, UInt32, UInt32) """
        ...


class IDebugDocumentText(IDebugDocument): # skipped bases: <type 'IDebugDocumentInfo'>, <type 'object'>
    """ no doc """
    def GetContextOfPosition(self, cCharacterPosition, cNumChars, ppsc) -> Tuple_[int, IDebugDocumentContext]:
        """ GetContextOfPosition(self: IDebugDocumentText, cCharacterPosition: UInt32, cNumChars: UInt32) -> (int, IDebugDocumentContext) """
        ...

    def GetDocumentAttributes(self, ptextdocattr) -> Tuple_[int, UInt32]:
        """ GetDocumentAttributes(self: IDebugDocumentText) -> (int, UInt32) """
        ...

    def GetLineOfPosition(self, cCharacterPosition, pcLineNumber, pcCharacterOffsetInLine) -> Tuple_[int, UInt32, UInt32]:
        """ GetLineOfPosition(self: IDebugDocumentText, cCharacterPosition: UInt32) -> (int, UInt32, UInt32) """
        ...

    def GetPositionOfContext(self, psc, pcCharacterPosition, cNumChars) -> Tuple_[int, UInt32, UInt32]:
        """ GetPositionOfContext(self: IDebugDocumentText, psc: IDebugDocumentContext) -> (int, UInt32, UInt32) """
        ...

    def GetPositionOfLine(self, cLineNumber, pcCharacterPosition) -> Tuple_[int, UInt32]:
        """ GetPositionOfLine(self: IDebugDocumentText, cLineNumber: UInt32) -> (int, UInt32) """
        ...

    def GetSize(self, pcNumLines, pcNumChars) -> Tuple_[int, UInt32, UInt32]:
        """ GetSize(self: IDebugDocumentText) -> (int, UInt32, UInt32) """
        ...

    def GetText(self, cCharacterPosition, pcharText, pstaTextAttr, pcNumChars, cMaxChars) -> Tuple_[int, Array, UInt32]:
        """ GetText(self: IDebugDocumentText, cCharacterPosition: UInt32, pcharText: IntPtr, cMaxChars: UInt32) -> (int, Array[UInt16], UInt32) """
        ...


class IDebugDocumentText2(IDebugDocument2): # skipped bases: <type 'object'>
    """ no doc """
    def GetSize(self, pcNumLines, pcNumChars) -> Tuple_[int, UInt32, UInt32]:
        """ GetSize(self: IDebugDocumentText2) -> (int, UInt32, UInt32) """
        ...

    def GetText(self, pos, cMaxChars, pText, pcNumChars) -> Tuple_[int, UInt32]:
        """ GetText(self: IDebugDocumentText2, pos: TEXT_POSITION, cMaxChars: UInt32, pText: IntPtr) -> (int, UInt32) """
        ...


class IDebugDocumentTextAuthor(IDebugDocumentText): # skipped bases: <type 'IDebugDocumentInfo'>, <type 'IDebugDocument'>, <type 'object'>
    """ no doc """
    def InsertText(self, cCharacterPosition:UInt32, cNumToInsert:UInt32, pcharText:str) -> int:
        """ InsertText(self: IDebugDocumentTextAuthor, cCharacterPosition: UInt32, cNumToInsert: UInt32, pcharText: str) -> int """
        ...

    def RemoveText(self, cCharacterPosition:UInt32, cNumToRemove:UInt32) -> int:
        """ RemoveText(self: IDebugDocumentTextAuthor, cCharacterPosition: UInt32, cNumToRemove: UInt32) -> int """
        ...

    def ReplaceText(self, cCharacterPosition:UInt32, cNumToReplace:UInt32, pcharText:str) -> int:
        """ ReplaceText(self: IDebugDocumentTextAuthor, cCharacterPosition: UInt32, cNumToReplace: UInt32, pcharText: str) -> int """
        ...


class IDebugDocumentTextEvents: # skipped bases: <type 'object'>
    """ no doc """
    def onDestroy(self) -> int:
        """ onDestroy(self: IDebugDocumentTextEvents) -> int """
        ...

    def onInsertText(self, cCharacterPosition:UInt32, cNumToInsert:UInt32) -> int:
        """ onInsertText(self: IDebugDocumentTextEvents, cCharacterPosition: UInt32, cNumToInsert: UInt32) -> int """
        ...

    def onRemoveText(self, cCharacterPosition:UInt32, cNumToRemove:UInt32) -> int:
        """ onRemoveText(self: IDebugDocumentTextEvents, cCharacterPosition: UInt32, cNumToRemove: UInt32) -> int """
        ...

    def onReplaceText(self, cCharacterPosition:UInt32, cNumToReplace:UInt32) -> int:
        """ onReplaceText(self: IDebugDocumentTextEvents, cCharacterPosition: UInt32, cNumToReplace: UInt32) -> int """
        ...

    def onUpdateDocumentAttributes(self, textdocattr:UInt32) -> int:
        """ onUpdateDocumentAttributes(self: IDebugDocumentTextEvents, textdocattr: UInt32) -> int """
        ...

    def onUpdateTextAttributes(self, cCharacterPosition:UInt32, cNumToUpdate:UInt32) -> int:
        """ onUpdateTextAttributes(self: IDebugDocumentTextEvents, cCharacterPosition: UInt32, cNumToUpdate: UInt32) -> int """
        ...


class IDebugDocumentTextEvents2: # skipped bases: <type 'object'>
    """ no doc """
    def onDestroy(self) -> int:
        """ onDestroy(self: IDebugDocumentTextEvents2) -> int """
        ...

    def onInsertText(self, pos:TEXT_POSITION, dwNumToInsert:UInt32) -> int:
        """ onInsertText(self: IDebugDocumentTextEvents2, pos: TEXT_POSITION, dwNumToInsert: UInt32) -> int """
        ...

    def onRemoveText(self, pos:TEXT_POSITION, dwNumToRemove:UInt32) -> int:
        """ onRemoveText(self: IDebugDocumentTextEvents2, pos: TEXT_POSITION, dwNumToRemove: UInt32) -> int """
        ...

    def onReplaceText(self, pos:TEXT_POSITION, dwNumToReplace:UInt32) -> int:
        """ onReplaceText(self: IDebugDocumentTextEvents2, pos: TEXT_POSITION, dwNumToReplace: UInt32) -> int """
        ...

    def onUpdateDocumentAttributes(self, textdocattr:UInt32) -> int:
        """ onUpdateDocumentAttributes(self: IDebugDocumentTextEvents2, textdocattr: UInt32) -> int """
        ...

    def onUpdateTextAttributes(self, pos:TEXT_POSITION, dwNumToUpdate:UInt32) -> int:
        """ onUpdateTextAttributes(self: IDebugDocumentTextEvents2, pos: TEXT_POSITION, dwNumToUpdate: UInt32) -> int """
        ...


class IDebugDocumentTextExternalAuthor: # skipped bases: <type 'object'>
    """ no doc """
    def GetFileName(self, pbstrShortName) -> Tuple_[int, str]:
        """ GetFileName(self: IDebugDocumentTextExternalAuthor) -> (int, str) """
        ...

    def GetPathName(self, pbstrLongName, pfIsOriginalFile) -> Tuple_[int, str, int]:
        """ GetPathName(self: IDebugDocumentTextExternalAuthor) -> (int, str, int) """
        ...

    def NotifyChanged(self) -> int:
        """ NotifyChanged(self: IDebugDocumentTextExternalAuthor) -> int """
        ...


class IDebugDynamicField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugDynamicFieldCOMPlus(IDebugDynamicField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def GetTypeFromPrimitive(self, dwCorElementType, ppType) -> Tuple_[int, IDebugField]:
        """ GetTypeFromPrimitive(self: IDebugDynamicFieldCOMPlus, dwCorElementType: UInt32) -> (int, IDebugField) """
        ...

    def GetTypeFromTypeDef(self, ulAppDomainID, guidModule, tokClass, ppType) -> Tuple_[int, IDebugField]:
        """ GetTypeFromTypeDef(self: IDebugDynamicFieldCOMPlus, ulAppDomainID: UInt32, guidModule: Guid, tokClass: int) -> (int, IDebugField) """
        ...


class IDebugENCDocumentContextUpdate: # skipped bases: <type 'object'>
    """ no doc """
    def UpdateDocumentContext(self, pContext:IDebugCodeContext2, pDocContext:IDebugDocumentContext2) -> int:
        """ UpdateDocumentContext(self: IDebugENCDocumentContextUpdate, pContext: IDebugCodeContext2, pDocContext: IDebugDocumentContext2) -> int """
        ...

    def UpdateStatementPosition(self, posBegStatement:TEXT_POSITION, posEndStatement:TEXT_POSITION) -> int:
        """ UpdateStatementPosition(self: IDebugENCDocumentContextUpdate, posBegStatement: TEXT_POSITION, posEndStatement: TEXT_POSITION) -> int """
        ...


class IDebugEncNotify: # skipped bases: <type 'object'>
    """ no doc """
    def NotifyEncEditAttemptedAtInvalidStopState(self) -> int:
        """ NotifyEncEditAttemptedAtInvalidStopState(self: IDebugEncNotify) -> int """
        ...

    def NotifyEncEditDisallowedByProject(self, pProject:object) -> int:
        """ NotifyEncEditDisallowedByProject(self: IDebugEncNotify, pProject: object) -> int """
        ...

    def NotifyEncIsUnavailable(self, reason:EncUnavailableReason, fEditWasApplied:int) -> int:
        """ NotifyEncIsUnavailable(self: IDebugEncNotify, reason: EncUnavailableReason, fEditWasApplied: int) -> int """
        ...

    def NotifyEncUpdateCurrentStatement(self) -> int:
        """ NotifyEncUpdateCurrentStatement(self: IDebugEncNotify) -> int """
        ...


class IDebugEngine2: # skipped bases: <type 'object'>
    """ no doc """
    def Attach(self, rgpPrograms:Array, rgpProgramNodes:Array, celtPrograms:UInt32, pCallback:IDebugEventCallback2, dwReason:UInt32) -> int:
        """ Attach(self: IDebugEngine2, rgpPrograms: Array[IDebugProgram2], rgpProgramNodes: Array[IDebugProgramNode2], celtPrograms: UInt32, pCallback: IDebugEventCallback2, dwReason: UInt32) -> int """
        ...

    def CauseBreak(self) -> int:
        """ CauseBreak(self: IDebugEngine2) -> int """
        ...

    def ContinueFromSynchronousEvent(self, pEvent:IDebugEvent2) -> int:
        """ ContinueFromSynchronousEvent(self: IDebugEngine2, pEvent: IDebugEvent2) -> int """
        ...

    def CreatePendingBreakpoint(self, pBPRequest, ppPendingBP) -> Tuple_[int, IDebugPendingBreakpoint2]:
        """ CreatePendingBreakpoint(self: IDebugEngine2, pBPRequest: IDebugBreakpointRequest2) -> (int, IDebugPendingBreakpoint2) """
        ...

    def DestroyProgram(self, pProgram:IDebugProgram2) -> int:
        """ DestroyProgram(self: IDebugEngine2, pProgram: IDebugProgram2) -> int """
        ...

    def EnumPrograms(self, ppEnum) -> Tuple_[int, IEnumDebugPrograms2]:
        """ EnumPrograms(self: IDebugEngine2) -> (int, IEnumDebugPrograms2) """
        ...

    def GetEngineId(self, pguidEngine) -> Tuple_[int, Guid]:
        """ GetEngineId(self: IDebugEngine2) -> (int, Guid) """
        ...

    def RemoveAllSetExceptions(self, guidType:Guid) -> Tuple_[int, Guid]:
        """ RemoveAllSetExceptions(self: IDebugEngine2, guidType: Guid) -> (int, Guid) """
        ...

    def RemoveSetException(self, pException:Array) -> int:
        """ RemoveSetException(self: IDebugEngine2, pException: Array[EXCEPTION_INFO]) -> int """
        ...

    def SetException(self, pException:Array) -> int:
        """ SetException(self: IDebugEngine2, pException: Array[EXCEPTION_INFO]) -> int """
        ...

    def SetLocale(self, wLangID:UInt16) -> int:
        """ SetLocale(self: IDebugEngine2, wLangID: UInt16) -> int """
        ...

    def SetMetric(self, pszMetric:str, varValue:object) -> int:
        """ SetMetric(self: IDebugEngine2, pszMetric: str, varValue: object) -> int """
        ...

    def SetRegistryRoot(self, pszRegistryRoot:str) -> int:
        """ SetRegistryRoot(self: IDebugEngine2, pszRegistryRoot: str) -> int """
        ...


class IDebugEngine3(IDebugEngine2): # skipped bases: <type 'object'>
    """ no doc """
    def LoadSymbols(self) -> int:
        """ LoadSymbols(self: IDebugEngine3) -> int """
        ...

    def SetAllExceptions(self, dwState:UInt32) -> int:
        """ SetAllExceptions(self: IDebugEngine3, dwState: UInt32) -> int """
        ...

    def SetEngineGuid(self, guidEngine:Guid) -> Tuple_[int, Guid]:
        """ SetEngineGuid(self: IDebugEngine3, guidEngine: Guid) -> (int, Guid) """
        ...

    def SetJustMyCodeState(self, fUpdate:int, dwModules:UInt32, rgJMCSpec:Array) -> int:
        """ SetJustMyCodeState(self: IDebugEngine3, fUpdate: int, dwModules: UInt32, rgJMCSpec: Array[JMC_CODE_SPEC]) -> int """
        ...

    def SetSymbolPath(self, szSymbolSearchPath:str, szSymbolCachePath:str, Flags:UInt32) -> int:
        """ SetSymbolPath(self: IDebugEngine3, szSymbolSearchPath: str, szSymbolCachePath: str, Flags: UInt32) -> int """
        ...


class IDebugEngineCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEngine(self, pEngine) -> Tuple_[int, IDebugEngine2]:
        """ GetEngine(self: IDebugEngineCreateEvent2) -> (int, IDebugEngine2) """
        ...


class IDebugEngineJITSettings2: # skipped bases: <type 'object'>
    """ no doc """
    def Enable(self) -> int:
        """ Enable(self: IDebugEngineJITSettings2) -> int """
        ...

    def GetWrappedDebuggers(self, pWrappedDebuggers) -> Tuple_[int, Array]:
        """ GetWrappedDebuggers(self: IDebugEngineJITSettings2) -> (int, Array[WRAPPED_DEBUGGER_ARRAY]) """
        ...

    def QueryIsEnabled(self) -> int:
        """ QueryIsEnabled(self: IDebugEngineJITSettings2) -> int """
        ...


class IDebugEngineLaunch2: # skipped bases: <type 'object'>
    """ no doc """
    def CanTerminateProcess(self, pProcess:IDebugProcess2) -> int:
        """ CanTerminateProcess(self: IDebugEngineLaunch2, pProcess: IDebugProcess2) -> int """
        ...

    def LaunchSuspended(self, pszServer, pPort, pszExe, pszArgs, pszDir, bstrEnv, pszOptions, dwLaunchFlags, hStdInput, hStdOutput, hStdError, pCallback, ppProcess) -> Tuple_[int, IDebugProcess2]:
        """ LaunchSuspended(self: IDebugEngineLaunch2, pszServer: str, pPort: IDebugPort2, pszExe: str, pszArgs: str, pszDir: str, bstrEnv: str, pszOptions: str, dwLaunchFlags: UInt32, hStdInput: UInt32, hStdOutput: UInt32, hStdError: UInt32, pCallback: IDebugEventCallback2) -> (int, IDebugProcess2) """
        ...

    def ResumeProcess(self, pProcess:IDebugProcess2) -> int:
        """ ResumeProcess(self: IDebugEngineLaunch2, pProcess: IDebugProcess2) -> int """
        ...

    def TerminateProcess(self, pProcess:IDebugProcess2) -> int:
        """ TerminateProcess(self: IDebugEngineLaunch2, pProcess: IDebugProcess2) -> int """
        ...


class IDebugEngineProgram2: # skipped bases: <type 'object'>
    """ no doc """
    def Stop(self) -> int:
        """ Stop(self: IDebugEngineProgram2) -> int """
        ...

    def WatchForExpressionEvaluationOnThread(self, pOriginatingProgram:IDebugProgram2, dwTid:UInt32, dwEvalFlags:UInt32, pExprCallback:IDebugEventCallback2, fWatch:int) -> int:
        """ WatchForExpressionEvaluationOnThread(self: IDebugEngineProgram2, pOriginatingProgram: IDebugProgram2, dwTid: UInt32, dwEvalFlags: UInt32, pExprCallback: IDebugEventCallback2, fWatch: int) -> int """
        ...

    def WatchForThreadStep(self, pOriginatingProgram:IDebugProgram2, dwTid:UInt32, fWatch:int, dwFrame:UInt32) -> int:
        """ WatchForThreadStep(self: IDebugEngineProgram2, pOriginatingProgram: IDebugProgram2, dwTid: UInt32, fWatch: int, dwFrame: UInt32) -> int """
        ...


class IDebugEngineSymbolProviderServices: # skipped bases: <type 'object'>
    """ no doc """
    def EnumCodeContexts(self, rgpAddresses, celtAddresses, ppEnum) -> Tuple_[int, IEnumDebugCodeContexts2]:
        """ EnumCodeContexts(self: IDebugEngineSymbolProviderServices, rgpAddresses: Array[IDebugAddress], celtAddresses: UInt32) -> (int, IEnumDebugCodeContexts2) """
        ...


class IDebugEngineSymbolProviderServices2(IDebugEngineSymbolProviderServices): # skipped bases: <type 'object'>
    """ no doc """
    def GetEngineProvidedDocumentPrefix(self, bstrDocPrefix) -> Tuple_[int, str]:
        """ GetEngineProvidedDocumentPrefix(self: IDebugEngineSymbolProviderServices2) -> (int, str) """
        ...

    def ResolveAssembly(self, ulAppDomainID, guidModule, tokAssemblyReference, pResolvedModules) -> Tuple_[int, Array]:
        """ ResolveAssembly(self: IDebugEngineSymbolProviderServices2, ulAppDomainID: UInt32, guidModule: Guid, tokAssemblyReference: UInt32) -> (int, Array[RESOLVED_MODULES]) """
        ...


class IDebugEntryPointEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugEnumField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def GetStringFromValue(self, value, pbstrValue) -> Tuple_[int, str]:
        """ GetStringFromValue(self: IDebugEnumField, value: UInt64) -> (int, str) """
        ...

    def GetUnderlyingSymbol(self, ppField) -> Tuple_[int, IDebugField]:
        """ GetUnderlyingSymbol(self: IDebugEnumField) -> (int, IDebugField) """
        ...

    def GetValueFromString(self, pszValue, pValue) -> Tuple_[int, UInt64]:
        """ GetValueFromString(self: IDebugEnumField, pszValue: str) -> (int, UInt64) """
        ...

    def GetValueFromStringCaseInsensitive(self, pszValue, pValue) -> Tuple_[int, UInt64]:
        """ GetValueFromStringCaseInsensitive(self: IDebugEnumField, pszValue: str) -> (int, UInt64) """
        ...


class IDebugErrorBreakpoint2: # skipped bases: <type 'object'>
    """ no doc """
    def GetBreakpointResolution(self, ppErrorResolution) -> Tuple_[int, IDebugErrorBreakpointResolution2]:
        """ GetBreakpointResolution(self: IDebugErrorBreakpoint2) -> (int, IDebugErrorBreakpointResolution2) """
        ...

    def GetPendingBreakpoint(self, ppPendingBreakpoint) -> Tuple_[int, IDebugPendingBreakpoint2]:
        """ GetPendingBreakpoint(self: IDebugErrorBreakpoint2) -> (int, IDebugPendingBreakpoint2) """
        ...


class IDebugErrorBreakpointResolution2: # skipped bases: <type 'object'>
    """ no doc """
    def GetBreakpointType(self, pBPType) -> Tuple_[int, UInt32]:
        """ GetBreakpointType(self: IDebugErrorBreakpointResolution2) -> (int, UInt32) """
        ...

    def GetResolutionInfo(self, dwFields, pErrorResolutionInfo) -> Tuple_[int, Array]:
        """ GetResolutionInfo(self: IDebugErrorBreakpointResolution2, dwFields: UInt32) -> (int, Array[BP_ERROR_RESOLUTION_INFO]) """
        ...


class IDebugErrorEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetErrorMessage(self, pMessageType, pbstrErrorFormat, phrErrorReason, pdwType, pbstrHelpFileName, pdwHelpId) -> Tuple_[int, UInt32, str, int, UInt32, str, UInt32]:
        """ GetErrorMessage(self: IDebugErrorEvent2) -> (int, UInt32, str, int, UInt32, str, UInt32) """
        ...


class IDebugEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetAttributes(self, pdwAttrib) -> Tuple_[int, UInt32]:
        """ GetAttributes(self: IDebugEvent2) -> (int, UInt32) """
        ...


class IDebugEventCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def Event(self, pEngine:IDebugEngine2, pProcess:IDebugProcess2, pProgram:IDebugProgram2, pThread:IDebugThread2, pEvent:IDebugEvent2, riidEvent:Guid, dwAttrib:UInt32) -> Tuple_[int, Guid]:
        """ Event(self: IDebugEventCallback2, pEngine: IDebugEngine2, pProcess: IDebugProcess2, pProgram: IDebugProgram2, pThread: IDebugThread2, pEvent: IDebugEvent2, riidEvent: Guid, dwAttrib: UInt32) -> (int, Guid) """
        ...


class IDebugExceptionCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def QueryStopOnException(self, pProcess:IDebugProcess2, pProgram:IDebugProgram2, pThread:IDebugThread2, pEvent:IDebugExceptionEvent2) -> int:
        """ QueryStopOnException(self: IDebugExceptionCallback2, pProcess: IDebugProcess2, pProgram: IDebugProgram2, pThread: IDebugThread2, pEvent: IDebugExceptionEvent2) -> int """
        ...


class IDebugExceptionEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def CanPassToDebuggee(self) -> int:
        """ CanPassToDebuggee(self: IDebugExceptionEvent2) -> int """
        ...

    def GetException(self, pExceptionInfo) -> Tuple_[int, Array]:
        """ GetException(self: IDebugExceptionEvent2) -> (int, Array[EXCEPTION_INFO]) """
        ...

    def GetExceptionDescription(self, pbstrDescription) -> Tuple_[int, str]:
        """ GetExceptionDescription(self: IDebugExceptionEvent2) -> (int, str) """
        ...

    def PassToDebuggee(self, fPass:int) -> int:
        """ PassToDebuggee(self: IDebugExceptionEvent2, fPass: int) -> int """
        ...


class IDebugExpression: # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self) -> int:
        """ Abort(self: IDebugExpression) -> int """
        ...

    def GetResultAsDebugProperty(self, phrResult, ppdp) -> Tuple_[int, int, IDebugProperty]:
        """ GetResultAsDebugProperty(self: IDebugExpression) -> (int, int, IDebugProperty) """
        ...

    def GetResultAsString(self, phrResult, pbstrResult) -> Tuple_[int, int, str]:
        """ GetResultAsString(self: IDebugExpression) -> (int, int, str) """
        ...

    def QueryIsComplete(self) -> int:
        """ QueryIsComplete(self: IDebugExpression) -> int """
        ...

    def Start(self, pdecb:IDebugExpressionCallBack) -> int:
        """ Start(self: IDebugExpression, pdecb: IDebugExpressionCallBack) -> int """
        ...


class IDebugExpression2: # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self) -> int:
        """ Abort(self: IDebugExpression2) -> int """
        ...

    def EvaluateAsync(self, dwFlags:UInt32, pExprCallback:IDebugEventCallback2) -> int:
        """ EvaluateAsync(self: IDebugExpression2, dwFlags: UInt32, pExprCallback: IDebugEventCallback2) -> int """
        ...

    def EvaluateSync(self, dwFlags, dwTimeout, pExprCallback, ppResult) -> Tuple_[int, IDebugProperty2]:
        """ EvaluateSync(self: IDebugExpression2, dwFlags: UInt32, dwTimeout: UInt32, pExprCallback: IDebugEventCallback2) -> (int, IDebugProperty2) """
        ...


class IDebugExpressionCallBack: # skipped bases: <type 'object'>
    """ no doc """
    def onComplete(self) -> int:
        """ onComplete(self: IDebugExpressionCallBack) -> int """
        ...


class IDebugExpressionContext: # skipped bases: <type 'object'>
    """ no doc """
    def GetLanguageInfo(self, pbstrLanguageName, pLanguageID) -> Tuple_[int, str, Guid]:
        """ GetLanguageInfo(self: IDebugExpressionContext) -> (int, str, Guid) """
        ...

    def ParseLanguageText(self, pstrCode, nRadix, pstrDelimiter, dwFlags, ppe) -> Tuple_[int, IDebugExpression]:
        """ ParseLanguageText(self: IDebugExpressionContext, pstrCode: str, nRadix: UInt32, pstrDelimiter: str, dwFlags: UInt32) -> (int, IDebugExpression) """
        ...


class IDebugExpressionContext2: # skipped bases: <type 'object'>
    """ no doc """
    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugExpressionContext2) -> (int, str) """
        ...

    def ParseText(self, pszCode, dwFlags, nRadix, ppExpr, pbstrError, pichError) -> Tuple_[int, IDebugExpression2, str, UInt32]:
        """ ParseText(self: IDebugExpressionContext2, pszCode: str, dwFlags: UInt32, nRadix: UInt32) -> (int, IDebugExpression2, str, UInt32) """
        ...


class IDebugExpressionEvaluationCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetExpression(self, ppExpr) -> Tuple_[int, IDebugExpression2]:
        """ GetExpression(self: IDebugExpressionEvaluationCompleteEvent2) -> (int, IDebugExpression2) """
        ...

    def GetResult(self, ppResult) -> Tuple_[int, IDebugProperty2]:
        """ GetResult(self: IDebugExpressionEvaluationCompleteEvent2) -> (int, IDebugProperty2) """
        ...


class IDebugExpressionEvaluator: # skipped bases: <type 'object'>
    """ no doc """
    def GetMethodLocationProperty(self, upstrFullyQualifiedMethodPlusOffset, pSymbolProvider, pAddress, pBinder, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetMethodLocationProperty(self: IDebugExpressionEvaluator, upstrFullyQualifiedMethodPlusOffset: str, pSymbolProvider: IDebugSymbolProvider, pAddress: IDebugAddress, pBinder: IDebugBinder) -> (int, IDebugProperty2) """
        ...

    def GetMethodProperty(self, pSymbolProvider, pAddress, pBinder, fIncludeHiddenLocals, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetMethodProperty(self: IDebugExpressionEvaluator, pSymbolProvider: IDebugSymbolProvider, pAddress: IDebugAddress, pBinder: IDebugBinder, fIncludeHiddenLocals: int) -> (int, IDebugProperty2) """
        ...

    def Parse(self, upstrExpression, dwFlags, nRadix, pbstrError, pichError, ppParsedExpression) -> Tuple_[int, str, UInt32, IDebugParsedExpression]:
        """ Parse(self: IDebugExpressionEvaluator, upstrExpression: str, dwFlags: UInt32, nRadix: UInt32) -> (int, str, UInt32, IDebugParsedExpression) """
        ...

    def SetLocale(self, wLangID:UInt16) -> int:
        """ SetLocale(self: IDebugExpressionEvaluator, wLangID: UInt16) -> int """
        ...

    def SetRegistryRoot(self, ustrRegistryRoot:str) -> int:
        """ SetRegistryRoot(self: IDebugExpressionEvaluator, ustrRegistryRoot: str) -> int """
        ...


class IDebugExpressionEvaluator2(IDebugExpressionEvaluator): # skipped bases: <type 'object'>
    """ no doc """
    def GetService(self, uid, ppService) -> Tuple_[int, object]:
        """ GetService(self: IDebugExpressionEvaluator2, uid: Guid) -> (int, object) """
        ...

    def PreloadModules(self, pSym:IDebugSymbolProvider) -> int:
        """ PreloadModules(self: IDebugExpressionEvaluator2, pSym: IDebugSymbolProvider) -> int """
        ...

    def SetCallback(self, pCallback:IDebugSettingsCallback2) -> int:
        """ SetCallback(self: IDebugExpressionEvaluator2, pCallback: IDebugSettingsCallback2) -> int """
        ...

    def SetCorPath(self, pcstrCorPath:str) -> int:
        """ SetCorPath(self: IDebugExpressionEvaluator2, pcstrCorPath: str) -> int """
        ...

    def SetIDebugIDECallback(self, pCallback:IDebugIDECallback) -> int:
        """ SetIDebugIDECallback(self: IDebugExpressionEvaluator2, pCallback: IDebugIDECallback) -> int """
        ...

    def Terminate(self) -> int:
        """ Terminate(self: IDebugExpressionEvaluator2) -> int """
        ...


class IDebugExpressionEvaluator3(IDebugExpressionEvaluator2): # skipped bases: <type 'IDebugExpressionEvaluator'>, <type 'object'>
    """ no doc """
    def Parse2(self, upstrExpression, dwFlags, nRadix, pSymbolProvider, pAddress, pbstrError, pichError, ppParsedExpression) -> Tuple_[int, str, UInt32, IDebugParsedExpression]:
        """ Parse2(self: IDebugExpressionEvaluator3, upstrExpression: str, dwFlags: UInt32, nRadix: UInt32, pSymbolProvider: IDebugSymbolProvider, pAddress: IDebugAddress) -> (int, str, UInt32, IDebugParsedExpression) """
        ...


class IDebugExtendedField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    def GetExtendedKind(self, pdwKind) -> Tuple_[int, UInt32]:
        """ GetExtendedKind(self: IDebugExtendedField) -> (int, UInt32) """
        ...

    def IsClosedType(self) -> int:
        """ IsClosedType(self: IDebugExtendedField) -> int """
        ...


class IDebugProperty: # skipped bases: <type 'object'>
    """ no doc """
    def EnumMembers(self, dwFieldSpec, nRadix, refiid, ppepi) -> Tuple_[int, Guid, IEnumDebugPropertyInfo]:
        """ EnumMembers(self: IDebugProperty, dwFieldSpec: UInt32, nRadix: UInt32, refiid: Guid) -> (int, Guid, IEnumDebugPropertyInfo) """
        ...

    def GetExtendedInfo(self, cInfos, rgguidExtendedInfo, rgvar) -> Tuple_[int, Array]:
        """ GetExtendedInfo(self: IDebugProperty, cInfos: UInt32, rgguidExtendedInfo: Array[Guid]) -> (int, Array[object]) """
        ...

    def GetParent(self, ppDebugProp) -> Tuple_[int, IDebugProperty]:
        """ GetParent(self: IDebugProperty) -> (int, IDebugProperty) """
        ...

    def GetPropertyInfo(self, dwFieldSpec, nRadix, pPropertyInfo) -> Tuple_[int, Array]:
        """ GetPropertyInfo(self: IDebugProperty, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, Array[DebugPropertyInfo]) """
        ...

    def SetValueAsString(self, pszValue:str, nRadix:UInt32) -> int:
        """ SetValueAsString(self: IDebugProperty, pszValue: str, nRadix: UInt32) -> int """
        ...


class IDebugExtendedProperty(IDebugProperty): # skipped bases: <type 'object'>
    """ no doc """
    def EnumExtendedMembers(self, dwFieldSpec, nRadix, ppeepi) -> Tuple_[int, IEnumDebugExtendedPropertyInfo]:
        """ EnumExtendedMembers(self: IDebugExtendedProperty, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, IEnumDebugExtendedPropertyInfo) """
        ...

    def GetExtendedPropertyInfo(self, dwFieldSpec, nRadix, pExtendedPropertyInfo) -> Tuple_[int, Array]:
        """ GetExtendedPropertyInfo(self: IDebugExtendedProperty, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, Array[ExtendedDebugPropertyInfo]) """
        ...


class IDebugFirewallConfigurationCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def EnsureDCOMUnblocked(self) -> int:
        """ EnsureDCOMUnblocked(self: IDebugFirewallConfigurationCallback2) -> int """
        ...


class IDebugFormatter: # skipped bases: <type 'object'>
    """ no doc """
    def GetStringForVariant(self, pvar, nRadix, pbstrValue) -> Tuple_[int, object, str]:
        """ GetStringForVariant(self: IDebugFormatter, pvar: object, nRadix: UInt32) -> (int, object, str) """
        ...

    def GetStringForVarType(self):
        """ no doc """
        ...

    def GetVariantForString(self, pwstrValue, pvar) -> Tuple_[int, object]:
        """ GetVariantForString(self: IDebugFormatter, pwstrValue: str) -> (int, object) """
        ...


class IDebugFuncEvalAbortedEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetAbortResult(self, pResult) -> Tuple_[int, Array]:
        """ GetAbortResult(self: IDebugFuncEvalAbortedEvent2) -> (int, Array[FUNC_EVAL_ABORT_RESULT]) """
        ...

    def GetFunctionName(self, pbstrFunctionName) -> Tuple_[int, str]:
        """ GetFunctionName(self: IDebugFuncEvalAbortedEvent2) -> (int, str) """
        ...


class IDebugFunctionObject(IDebugObject): # skipped bases: <type 'object'>
    """ no doc """
    def CreateArrayObject(self, ot, pClassField, dwRank, dwDims, dwLowBounds, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateArrayObject(self: IDebugFunctionObject, ot: UInt32, pClassField: IDebugField, dwRank: UInt32, dwDims: Array[UInt32], dwLowBounds: Array[UInt32]) -> (int, IDebugObject) """
        ...

    def CreateObject(self, pConstructor, dwArgs, pArgs, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateObject(self: IDebugFunctionObject, pConstructor: IDebugFunctionObject, dwArgs: UInt32, pArgs: Array[IDebugObject]) -> (int, IDebugObject) """
        ...

    def CreateObjectNoConstructor(self, pClassField, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateObjectNoConstructor(self: IDebugFunctionObject, pClassField: IDebugField) -> (int, IDebugObject) """
        ...

    def CreatePrimitiveObject(self, ot, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreatePrimitiveObject(self: IDebugFunctionObject, ot: UInt32) -> (int, IDebugObject) """
        ...

    def CreateStringObject(self, pcstrString, ppOjbect) -> Tuple_[int, IDebugObject]:
        """ CreateStringObject(self: IDebugFunctionObject, pcstrString: str) -> (int, IDebugObject) """
        ...

    def Evaluate(self, ppParams, dwParams, dwTimeout, ppResult) -> Tuple_[int, IDebugObject]:
        """ Evaluate(self: IDebugFunctionObject, ppParams: Array[IDebugObject], dwParams: IntPtr, dwTimeout: UInt32) -> (int, IDebugObject) """
        ...


class IDebugFunctionObject2: # skipped bases: <type 'object'>
    """ no doc """
    def CreateObject(self, pConstructor, dwArgs, pArgs, dwEvalFlags, dwTimeout, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateObject(self: IDebugFunctionObject2, pConstructor: IDebugFunctionObject, dwArgs: UInt32, pArgs: Array[IDebugObject], dwEvalFlags: UInt32, dwTimeout: UInt32) -> (int, IDebugObject) """
        ...

    def CreateStringObjectWithLength(self, pcstrString, uiLength, ppObject) -> Tuple_[int, IDebugObject]:
        """ CreateStringObjectWithLength(self: IDebugFunctionObject2, pcstrString: str, uiLength: UInt32) -> (int, IDebugObject) """
        ...

    def Evaluate(self, ppParams, dwParams, dwEvalFlags, dwTimeout, ppResult) -> Tuple_[int, IDebugObject]:
        """ Evaluate(self: IDebugFunctionObject2, ppParams: Array[IDebugObject], dwParams: IntPtr, dwEvalFlags: UInt32, dwTimeout: UInt32) -> (int, IDebugObject) """
        ...


class IDebugFunctionPosition2: # skipped bases: <type 'object'>
    """ no doc """
    def GetFunctionName(self, pbstrFunctionName) -> Tuple_[int, str]:
        """ GetFunctionName(self: IDebugFunctionPosition2) -> (int, str) """
        ...

    def GetOffset(self, pPosition) -> Tuple_[int, Array]:
        """ GetOffset(self: IDebugFunctionPosition2) -> (int, Array[TEXT_POSITION]) """
        ...


class IDebugGenericFieldDefinition: # skipped bases: <type 'object'>
    """ no doc """
    def ConstructInstantiation(self, cArgs, ppArgs, ppConstructedField) -> Tuple_[int, IDebugField]:
        """ ConstructInstantiation(self: IDebugGenericFieldDefinition, cArgs: UInt32, ppArgs: Array[IDebugField]) -> (int, IDebugField) """
        ...

    def GetFormalTypeParams(self, cParams, ppParams, pcParams) -> Tuple_[int, Array, UInt32]:
        """ GetFormalTypeParams(self: IDebugGenericFieldDefinition, cParams: UInt32) -> (int, Array[IDebugGenericParamField], UInt32) """
        ...

    def TypeParamCount(self, pcParams) -> Tuple_[int, UInt32]:
        """ TypeParamCount(self: IDebugGenericFieldDefinition) -> (int, UInt32) """
        ...


class IDebugGenericFieldInstance: # skipped bases: <type 'object'>
    """ no doc """
    def GetTypeArguments(self, cArgs, ppArgs, pcArgs) -> Tuple_[int, Array, UInt32]:
        """ GetTypeArguments(self: IDebugGenericFieldInstance, cArgs: UInt32) -> (int, Array[IDebugField], UInt32) """
        ...

    def TypeArgumentCount(self, pcArgs) -> Tuple_[int, UInt32]:
        """ TypeArgumentCount(self: IDebugGenericFieldInstance) -> (int, UInt32) """
        ...


class IDebugGenericParamField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    def ConstraintCount(self, pcConst) -> Tuple_[int, UInt32]:
        """ ConstraintCount(self: IDebugGenericParamField) -> (int, UInt32) """
        ...

    def GetConstraints(self, cConstraints, ppConstraints, pcConstraints) -> Tuple_[int, Array, UInt32]:
        """ GetConstraints(self: IDebugGenericParamField, cConstraints: UInt32) -> (int, Array[IDebugField], UInt32) """
        ...

    def GetFlags(self, pdwFlags) -> Tuple_[int, UInt32]:
        """ GetFlags(self: IDebugGenericParamField) -> (int, UInt32) """
        ...

    def GetIndex(self, pIndex) -> Tuple_[int, UInt32]:
        """ GetIndex(self: IDebugGenericParamField) -> (int, UInt32) """
        ...

    def GetNameOfFormalParam(self, pbstrName) -> Tuple_[IntPtr, str]:
        """ GetNameOfFormalParam(self: IDebugGenericParamField) -> (IntPtr, str) """
        ...

    def GetOwner(self, ppOwner) -> Tuple_[int, IDebugField]:
        """ GetOwner(self: IDebugGenericParamField) -> (int, IDebugField) """
        ...


class IDebugHelper: # skipped bases: <type 'object'>
    """ no doc """
    def CreatePropertyBrowser(self, pvar, bstrName, pdat, ppdob) -> Tuple_[int, object, IDebugProperty]:
        """ CreatePropertyBrowser(self: IDebugHelper, pvar: object, bstrName: str, pdat: IDebugApplicationThread) -> (int, object, IDebugProperty) """
        ...

    def CreatePropertyBrowserEx(self, pvar, bstrName, pdat, pdf, ppdob) -> Tuple_[int, object, IDebugProperty]:
        """ CreatePropertyBrowserEx(self: IDebugHelper, pvar: object, bstrName: str, pdat: IDebugApplicationThread, pdf: IDebugFormatter) -> (int, object, IDebugProperty) """
        ...

    def CreateSimpleConnectionPoint(self, pdisp, ppscp) -> Tuple_[int, ISimpleConnectionPoint]:
        """ CreateSimpleConnectionPoint(self: IDebugHelper, pdisp: object) -> (int, ISimpleConnectionPoint) """
        ...


class IDebugIDECallback: # skipped bases: <type 'object'>
    """ no doc """
    def DisplayMessage(self, szMessage:str) -> int:
        """ DisplayMessage(self: IDebugIDECallback, szMessage: str) -> int """
        ...


class IDebugIDEJIT2: # skipped bases: <type 'object'>
    """ no doc """
    def AttachJITDebugger(self, pProcess:IDebugProcess2, pJITProgram:IDebugProgram2, JitFlags:UInt32) -> int:
        """ AttachJITDebugger(self: IDebugIDEJIT2, pProcess: IDebugProcess2, pJITProgram: IDebugProgram2, JitFlags: UInt32) -> int """
        ...


class IDebugInterceptExceptionCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetInterceptCookie(self, pqwCookie) -> Tuple_[int, UInt64]:
        """ GetInterceptCookie(self: IDebugInterceptExceptionCompleteEvent2) -> (int, UInt64) """
        ...


class IDebugIteratorFrameProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetIteratorFrames(self, pAddress, pBinder, pSym, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetIteratorFrames(self: IDebugIteratorFrameProvider, pAddress: IDebugAddress, pBinder: IDebugBinderDirect, pSym: IDebugComPlusSymbolProvider) -> (int, IDebugProperty2) """
        ...


class IDebugJIT2: # skipped bases: <type 'object'>
    """ no doc """
    def JITDebug(self, CrashingProgram:CRASHING_PROGRAM_INFO) -> int:
        """ JITDebug(self: IDebugJIT2, CrashingProgram: CRASHING_PROGRAM_INFO) -> int """
        ...


class IDebugLoadCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugLogicalThread2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumFrameInfo(self, dwFieldSpec, nRadix, ppEnum) -> Tuple_[int, IEnumDebugFrameInfo2]:
        """ EnumFrameInfo(self: IDebugLogicalThread2, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, IEnumDebugFrameInfo2) """
        ...


class IDebugMachineEx2_V7: # skipped bases: <type 'object'>
    """ no doc """
    def DisableAutoAttachOnEvent(self, dwCookie:UInt32) -> int:
        """ DisableAutoAttachOnEvent(self: IDebugMachineEx2_V7, dwCookie: UInt32) -> int """
        ...

    def EnableAutoAttachOnProgramCreate(self, pszProcessNames, guidEngine, pszSessionId, pdwCookie) -> Tuple_[int, Guid, UInt32]:
        """ EnableAutoAttachOnProgramCreate(self: IDebugMachineEx2_V7, pszProcessNames: str, guidEngine: Guid, pszSessionId: str) -> (int, Guid, UInt32) """
        ...

    def EnumPortsEx(self, wstrRegistryRoot, ppEnum) -> Tuple_[int, IEnumDebugPorts2]:
        """ EnumPortsEx(self: IDebugMachineEx2_V7, wstrRegistryRoot: str) -> (int, IEnumDebugPorts2) """
        ...

    def EnumPortSuppliersEx(self, wstrRegistryRoot, ppEnum) -> Tuple_[int, IEnumDebugPortSuppliers2]:
        """ EnumPortSuppliersEx(self: IDebugMachineEx2_V7, wstrRegistryRoot: str) -> (int, IEnumDebugPortSuppliers2) """
        ...

    def GetPortEx(self, wstrRegistryRoot, guidPort, ppPort) -> Tuple_[int, Guid, IDebugPort2]:
        """ GetPortEx(self: IDebugMachineEx2_V7, wstrRegistryRoot: str, guidPort: Guid) -> (int, Guid, IDebugPort2) """
        ...

    def GetPortSupplierEx(self, wstrRegistryRoot, guidPortSupplier, ppPortSupplier) -> Tuple_[int, Guid, IDebugPortSupplier2]:
        """ GetPortSupplierEx(self: IDebugMachineEx2_V7, wstrRegistryRoot: str, guidPortSupplier: Guid) -> (int, Guid, IDebugPortSupplier2) """
        ...


class IDebugManagedExceptionInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def GetExceptionBoundaryType(self, pType) -> Tuple_[int, Array]:
        """ GetExceptionBoundaryType(self: IDebugManagedExceptionInfo2) -> (int, Array[EXCEPTION_BOUNDARY_TYPE]) """
        ...

    def GetExceptionMessage(self, pbstrExceptionMessage) -> Tuple_[int, str]:
        """ GetExceptionMessage(self: IDebugManagedExceptionInfo2) -> (int, str) """
        ...


class IDebugManagedObject: # skipped bases: <type 'object'>
    """ no doc """
    def GetManagedObject(self, ppManagedObject) -> Tuple_[int, object]:
        """ GetManagedObject(self: IDebugManagedObject) -> (int, object) """
        ...

    def SetFromManagedObject(self, pManagedObject:object) -> int:
        """ SetFromManagedObject(self: IDebugManagedObject, pManagedObject: object) -> int """
        ...


class IDebugMDMUtil2_V7: # skipped bases: <type 'object'>
    """ no doc """
    def AddPIDToDebug(self, guidEngine:Guid, dwPid:UInt32) -> Tuple_[int, Guid]:
        """ AddPIDToDebug(self: IDebugMDMUtil2_V7, guidEngine: Guid, dwPid: UInt32) -> (int, Guid) """
        ...

    def AddPIDToIgnore(self, guidEngine:Guid, dwPid:UInt32) -> Tuple_[int, Guid]:
        """ AddPIDToIgnore(self: IDebugMDMUtil2_V7, guidEngine: Guid, dwPid: UInt32) -> (int, Guid) """
        ...

    def CanDebugPID(self, guidEngine:Guid, pid:UInt32) -> Tuple_[int, Guid]:
        """ CanDebugPID(self: IDebugMDMUtil2_V7, guidEngine: Guid, pid: UInt32) -> (int, Guid) """
        ...

    def GetDefaultJITServer(self, pClsidJITServer) -> Tuple_[int, Guid]:
        """ GetDefaultJITServer(self: IDebugMDMUtil2_V7) -> (int, Guid) """
        ...

    def GetDynamicDebuggingFlags(self, guidEngine, pdwFlags) -> Tuple_[int, Guid, UInt32]:
        """ GetDynamicDebuggingFlags(self: IDebugMDMUtil2_V7, guidEngine: Guid) -> (int, Guid, UInt32) """
        ...

    def RegisterJITDebugEngines(self, clsidJITServer:Guid, arrguidEngines:Array, arrRemoteFlags:Array, celtEngs:UInt32, fRegister:int) -> Tuple_[int, Guid]:
        """ RegisterJITDebugEngines(self: IDebugMDMUtil2_V7, clsidJITServer: Guid, arrguidEngines: Array[Guid], arrRemoteFlags: Array[int], celtEngs: UInt32, fRegister: int) -> (int, Guid) """
        ...

    def RemovePIDToDebug(self, guidEngine:Guid, dwPid:UInt32) -> Tuple_[int, Guid]:
        """ RemovePIDToDebug(self: IDebugMDMUtil2_V7, guidEngine: Guid, dwPid: UInt32) -> (int, Guid) """
        ...

    def RemovePIDToIgnore(self, guidEngine:Guid, dwPid:UInt32) -> Tuple_[int, Guid]:
        """ RemovePIDToIgnore(self: IDebugMDMUtil2_V7, guidEngine: Guid, dwPid: UInt32) -> (int, Guid) """
        ...

    def SetDefaultJITServer(self, clsidJITServer:Guid) -> Tuple_[int, Guid]:
        """ SetDefaultJITServer(self: IDebugMDMUtil2_V7, clsidJITServer: Guid) -> (int, Guid) """
        ...

    def SetDynamicDebuggingFlags(self, guidEngine:Guid, dwFlags:UInt32) -> Tuple_[int, Guid]:
        """ SetDynamicDebuggingFlags(self: IDebugMDMUtil2_V7, guidEngine: Guid, dwFlags: UInt32) -> (int, Guid) """
        ...


class IDebugMDMUtil3_V7(IDebugMDMUtil2_V7): # skipped bases: <type 'object'>
    """ no doc """
    def DiagnoseASPDebugging(self, szASPUserAccount:str) -> int:
        """ DiagnoseASPDebugging(self: IDebugMDMUtil3_V7, szASPUserAccount: str) -> int """
        ...

    def DiagnoseScriptDebuggingError(self, dwDebuggeeProcessId:UInt32) -> int:
        """ DiagnoseScriptDebuggingError(self: IDebugMDMUtil3_V7, dwDebuggeeProcessId: UInt32) -> int """
        ...

    def DiagnoseWebDebuggingError(self, dwWebType:UInt32, pszUrl:str) -> int:
        """ DiagnoseWebDebuggingError(self: IDebugMDMUtil3_V7, dwWebType: UInt32, pszUrl: str) -> int """
        ...


class IDebugMemoryBytes2: # skipped bases: <type 'object'>
    """ no doc """
    def GetSize(self, pqwSize) -> Tuple_[int, UInt64]:
        """ GetSize(self: IDebugMemoryBytes2) -> (int, UInt64) """
        ...

    def ReadAt(self, pStartContext, dwCount, rgbMemory, pdwRead, pdwUnreadable) -> Tuple_[int, Array, UInt32, UInt32]:
        """ ReadAt(self: IDebugMemoryBytes2, pStartContext: IDebugMemoryContext2, dwCount: UInt32) -> (int, Array[Byte], UInt32, UInt32) """
        ...

    def WriteAt(self, pStartContext:IDebugMemoryContext2, dwCount:UInt32, rgbMemory:Array) -> int:
        """ WriteAt(self: IDebugMemoryBytes2, pStartContext: IDebugMemoryContext2, dwCount: UInt32, rgbMemory: Array[Byte]) -> int """
        ...


class IDebugMessageEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetMessage(self, pMessageType, pbstrMessage, pdwType, pbstrHelpFileName, pdwHelpId) -> Tuple_[int, UInt32, str, UInt32, str, UInt32]:
        """ GetMessage(self: IDebugMessageEvent2) -> (int, UInt32, str, UInt32, str, UInt32) """
        ...

    def SetResponse(self, dwResponse:UInt32) -> int:
        """ SetResponse(self: IDebugMessageEvent2, dwResponse: UInt32) -> int """
        ...


class IDebugMethodField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def EnumAllLocals(self, pAddress, ppLocals) -> Tuple_[int, IEnumDebugFields]:
        """ EnumAllLocals(self: IDebugMethodField, pAddress: IDebugAddress) -> (int, IEnumDebugFields) """
        ...

    def EnumArguments(self, ppParams) -> Tuple_[int, IEnumDebugFields]:
        """ EnumArguments(self: IDebugMethodField) -> (int, IEnumDebugFields) """
        ...

    def EnumLocals(self, pAddress, ppLocals) -> Tuple_[int, IEnumDebugFields]:
        """ EnumLocals(self: IDebugMethodField, pAddress: IDebugAddress) -> (int, IEnumDebugFields) """
        ...

    def EnumParameters(self, ppParams) -> Tuple_[int, IEnumDebugFields]:
        """ EnumParameters(self: IDebugMethodField) -> (int, IEnumDebugFields) """
        ...

    def EnumStaticLocals(self, ppLocals) -> Tuple_[int, IEnumDebugFields]:
        """ EnumStaticLocals(self: IDebugMethodField) -> (int, IEnumDebugFields) """
        ...

    def GetGlobalContainer(self, ppClass) -> Tuple_[int, IDebugClassField]:
        """ GetGlobalContainer(self: IDebugMethodField) -> (int, IDebugClassField) """
        ...

    def GetThis(self, ppClass) -> Tuple_[int, IDebugClassField]:
        """ GetThis(self: IDebugMethodField) -> (int, IDebugClassField) """
        ...

    def IsCustomAttributeDefined(self, pszCustomAttributeName:str) -> int:
        """ IsCustomAttributeDefined(self: IDebugMethodField, pszCustomAttributeName: str) -> int """
        ...


class IDebugModOpt: # skipped bases: <type 'object'>
    """ no doc """
    def GetModOpts(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ GetModOpts(self: IDebugModOpt, celt: UInt32) -> (int, Array[str], UInt32) """
        ...


class IDebugModule2: # skipped bases: <type 'object'>
    """ no doc """
    def GetInfo(self):
        """ no doc """
        ...

    def ReloadSymbols_Deprecated(self, pszUrlToSymbols, pbstrDebugMessage) -> Tuple_[int, str]:
        """ ReloadSymbols_Deprecated(self: IDebugModule2, pszUrlToSymbols: str) -> (int, str) """
        ...


class IDebugModule3(IDebugModule2): # skipped bases: <type 'object'>
    """ no doc """
    def GetSymbolInfo(self, dwFields, pinfo) -> Tuple_[int, Array]:
        """ GetSymbolInfo(self: IDebugModule3, dwFields: UInt32) -> (int, Array[MODULE_SYMBOL_SEARCH_INFO]) """
        ...

    def IsUserCode(self, pfUser) -> Tuple_[int, int]:
        """ IsUserCode(self: IDebugModule3) -> (int, int) """
        ...

    def LoadSymbols(self) -> int:
        """ LoadSymbols(self: IDebugModule3) -> int """
        ...

    def SetJustMyCodeState(self, fIsUserCode:int) -> int:
        """ SetJustMyCodeState(self: IDebugModule3, fIsUserCode: int) -> int """
        ...


class IDebugModuleLoadEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetModule(self, pModule, pbstrDebugMessage, pbLoad) -> Tuple_[int, IDebugModule2, str, int]:
        """ GetModule(self: IDebugModuleLoadEvent2) -> (int, IDebugModule2, str, int) """
        ...


class IDebugModuleManaged: # skipped bases: <type 'object'>
    """ no doc """
    def GetMvid(self, mvid) -> Tuple_[int, Guid]:
        """ GetMvid(self: IDebugModuleManaged) -> (int, Guid) """
        ...


class IDebugNativeExceptionInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetNativeException(self, pExceptionInfo) -> Tuple_[int, Array]:
        """ GetNativeException(self: IDebugNativeExceptionInfo) -> (int, Array[NATIVE_EXCEPTION_INFO]) """
        ...


class IDebugNativePort2: # skipped bases: <type 'object'>
    """ no doc """
    def AddProcess(self, ProcessId, pszProcessName, fCanDetach, ppPortProcess) -> Tuple_[int, IDebugProcess2]:
        """ AddProcess(self: IDebugNativePort2, ProcessId: AD_PROCESS_ID, pszProcessName: str, fCanDetach: int) -> (int, IDebugProcess2) """
        ...


class IDebugNativeSymbolProvider(IDebugSymbolProvider): # skipped bases: <type 'object'>
    """ no doc """
    def LoadSymbols(self, pszFileName:str) -> int:
        """ LoadSymbols(self: IDebugNativeSymbolProvider, pszFileName: str) -> int """
        ...


class IDebugNoSymbolsEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugObject2(IDebugObject): # skipped bases: <type 'object'>
    """ no doc """
    def CreateAlias(self, ppAlias) -> Tuple_[int, IDebugAlias]:
        """ CreateAlias(self: IDebugObject2) -> (int, IDebugAlias) """
        ...

    def GetAlias(self, ppAlias) -> Tuple_[int, IDebugAlias]:
        """ GetAlias(self: IDebugObject2) -> (int, IDebugAlias) """
        ...

    def GetBackingFieldForProperty(self, ppObject) -> Tuple_[int, IDebugObject2]:
        """ GetBackingFieldForProperty(self: IDebugObject2) -> (int, IDebugObject2) """
        ...

    def GetField(self, ppField) -> Tuple_[int, IDebugField]:
        """ GetField(self: IDebugObject2) -> (int, IDebugField) """
        ...

    def GetICorDebugValue(self, ppUnk) -> Tuple_[int, object]:
        """ GetICorDebugValue(self: IDebugObject2) -> (int, object) """
        ...

    def IsEncOutdated(self, pfEncOutdated) -> Tuple_[int, int]:
        """ IsEncOutdated(self: IDebugObject2) -> (int, int) """
        ...

    def IsUserData(self, pfUser) -> Tuple_[int, int]:
        """ IsUserData(self: IDebugObject2) -> (int, int) """
        ...


class IDebugOutputStringEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetString(self, pbstrString) -> Tuple_[int, str]:
        """ GetString(self: IDebugOutputStringEvent2) -> (int, str) """
        ...


class IDebugParsedExpression: # skipped bases: <type 'object'>
    """ no doc """
    def EvaluateSync(self, dwEvalFlags, dwTimeout, pSymbolProvider, pAddress, pBinder, bstrResultType, ppResult) -> Tuple_[int, IDebugProperty2]:
        """ EvaluateSync(self: IDebugParsedExpression, dwEvalFlags: UInt32, dwTimeout: UInt32, pSymbolProvider: IDebugSymbolProvider, pAddress: IDebugAddress, pBinder: IDebugBinder, bstrResultType: str) -> (int, IDebugProperty2) """
        ...


class IDebugPendingBreakpoint2: # skipped bases: <type 'object'>
    """ no doc """
    def Bind(self) -> int:
        """ Bind(self: IDebugPendingBreakpoint2) -> int """
        ...

    def CanBind(self, ppErrorEnum) -> Tuple_[int, IEnumDebugErrorBreakpoints2]:
        """ CanBind(self: IDebugPendingBreakpoint2) -> (int, IEnumDebugErrorBreakpoints2) """
        ...

    def Delete(self) -> int:
        """ Delete(self: IDebugPendingBreakpoint2) -> int """
        ...

    def Enable(self, fEnable:int) -> int:
        """ Enable(self: IDebugPendingBreakpoint2, fEnable: int) -> int """
        ...

    def EnumBoundBreakpoints(self, ppEnum) -> Tuple_[int, IEnumDebugBoundBreakpoints2]:
        """ EnumBoundBreakpoints(self: IDebugPendingBreakpoint2) -> (int, IEnumDebugBoundBreakpoints2) """
        ...

    def EnumErrorBreakpoints(self, bpErrorType, ppEnum) -> Tuple_[int, IEnumDebugErrorBreakpoints2]:
        """ EnumErrorBreakpoints(self: IDebugPendingBreakpoint2, bpErrorType: UInt32) -> (int, IEnumDebugErrorBreakpoints2) """
        ...

    def GetBreakpointRequest(self, ppBPRequest) -> Tuple_[int, IDebugBreakpointRequest2]:
        """ GetBreakpointRequest(self: IDebugPendingBreakpoint2) -> (int, IDebugBreakpointRequest2) """
        ...

    def GetState(self, pState) -> Tuple_[int, Array]:
        """ GetState(self: IDebugPendingBreakpoint2) -> (int, Array[PENDING_BP_STATE_INFO]) """
        ...

    def SetCondition(self, bpCondition:BP_CONDITION) -> int:
        """ SetCondition(self: IDebugPendingBreakpoint2, bpCondition: BP_CONDITION) -> int """
        ...

    def SetPassCount(self, bpPassCount:BP_PASSCOUNT) -> int:
        """ SetPassCount(self: IDebugPendingBreakpoint2, bpPassCount: BP_PASSCOUNT) -> int """
        ...

    def Virtualize(self, fVirtualize:int) -> int:
        """ Virtualize(self: IDebugPendingBreakpoint2, fVirtualize: int) -> int """
        ...


class IDebugPendingBreakpoint3(IDebugPendingBreakpoint2): # skipped bases: <type 'object'>
    """ no doc """
    def GetErrorResolutionInfo(self, dwFields, pErrorResolutionInfo) -> Tuple_[int, Array]:
        """ GetErrorResolutionInfo(self: IDebugPendingBreakpoint3, dwFields: UInt32) -> (int, Array[BP_ERROR_RESOLUTION_INFO]) """
        ...


class IDebugPointerField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def GetDereferencedField(self, ppField) -> Tuple_[int, IDebugField]:
        """ GetDereferencedField(self: IDebugPointerField) -> (int, IDebugField) """
        ...


class IDebugPointerObject(IDebugObject): # skipped bases: <type 'object'>
    """ no doc """
    def Dereference(self, dwIndex, ppObject) -> Tuple_[int, IDebugObject]:
        """ Dereference(self: IDebugPointerObject, dwIndex: UInt32) -> (int, IDebugObject) """
        ...

    def GetBytes(self, dwStart, dwCount, pBytes, pdwBytes) -> Tuple_[int, Array, UInt32]:
        """ GetBytes(self: IDebugPointerObject, dwStart: UInt32, dwCount: UInt32) -> (int, Array[Byte], UInt32) """
        ...

    def SetBytes(self, dwStart, dwCount, pBytes, pdwBytes) -> Tuple_[int, UInt32]:
        """ SetBytes(self: IDebugPointerObject, dwStart: UInt32, dwCount: UInt32, pBytes: Array[Byte]) -> (int, UInt32) """
        ...


class IDebugPointerObject2(IDebugObject): # skipped bases: <type 'object'>
    """ no doc """
    def ComputePointerAddress(self, pdwAddress) -> Tuple_[int, UInt32]:
        """ ComputePointerAddress(self: IDebugPointerObject2) -> (int, UInt32) """
        ...


class IDebugPointerObject3(IDebugPointerObject): # skipped bases: <type 'IDebugObject'>, <type 'object'>
    """ no doc """
    def GetPointerAddress(self, puAddress) -> Tuple_[int, UInt64]:
        """ GetPointerAddress(self: IDebugPointerObject3) -> (int, UInt64) """
        ...


class IDebugPortEvents2: # skipped bases: <type 'object'>
    """ no doc """
    def Event(self, pServer:IDebugCoreServer2, pPort:IDebugPort2, pProcess:IDebugProcess2, pProgram:IDebugProgram2, pEvent:IDebugEvent2, riidEvent:Guid) -> Tuple_[int, Guid]:
        """ Event(self: IDebugPortEvents2, pServer: IDebugCoreServer2, pPort: IDebugPort2, pProcess: IDebugProcess2, pProgram: IDebugProgram2, pEvent: IDebugEvent2, riidEvent: Guid) -> (int, Guid) """
        ...


class IDebugPortEventsEx2: # skipped bases: <type 'object'>
    """ no doc """
    def GetSession(self, ppSession) -> Tuple_[int, IDebugSession2]:
        """ GetSession(self: IDebugPortEventsEx2) -> (int, IDebugSession2) """
        ...


class IDebugPortEx2: # skipped bases: <type 'object'>
    """ no doc """
    def CanTerminateProcess(self, pPortProcess:IDebugProcess2) -> int:
        """ CanTerminateProcess(self: IDebugPortEx2, pPortProcess: IDebugProcess2) -> int """
        ...

    def GetPortProcessId(self, pdwProcessId) -> Tuple_[int, UInt32]:
        """ GetPortProcessId(self: IDebugPortEx2) -> (int, UInt32) """
        ...

    def GetProgram(self, pProgramNode, ppProgram) -> Tuple_[int, IDebugProgram2]:
        """ GetProgram(self: IDebugPortEx2, pProgramNode: IDebugProgramNode2) -> (int, IDebugProgram2) """
        ...

    def LaunchSuspended(self, pszExe, pszArgs, pszDir, bstrEnv, hStdInput, hStdOutput, hStdError, ppPortProcess) -> Tuple_[int, IDebugProcess2]:
        """ LaunchSuspended(self: IDebugPortEx2, pszExe: str, pszArgs: str, pszDir: str, bstrEnv: str, hStdInput: UInt32, hStdOutput: UInt32, hStdError: UInt32) -> (int, IDebugProcess2) """
        ...

    def ResumeProcess(self, pPortProcess:IDebugProcess2) -> int:
        """ ResumeProcess(self: IDebugPortEx2, pPortProcess: IDebugProcess2) -> int """
        ...

    def TerminateProcess(self, pPortProcess:IDebugProcess2) -> int:
        """ TerminateProcess(self: IDebugPortEx2, pPortProcess: IDebugProcess2) -> int """
        ...


class IDebugPortNotify2: # skipped bases: <type 'object'>
    """ no doc """
    def AddProgramNode(self, pProgramNode:IDebugProgramNode2) -> int:
        """ AddProgramNode(self: IDebugPortNotify2, pProgramNode: IDebugProgramNode2) -> int """
        ...

    def RemoveProgramNode(self, pProgramNode:IDebugProgramNode2) -> int:
        """ RemoveProgramNode(self: IDebugPortNotify2, pProgramNode: IDebugProgramNode2) -> int """
        ...


class IDebugPortPicker: # skipped bases: <type 'object'>
    """ no doc """
    def DisplayPortPicker(self, hwndParentDialog, pbstrPortId) -> Tuple_[int, str]:
        """ DisplayPortPicker(self: IDebugPortPicker, hwndParentDialog: IntPtr) -> (int, str) """
        ...

    def SetSite(self):
        """ no doc """
        ...


class IDebugPortRequest2: # skipped bases: <type 'object'>
    """ no doc """
    def GetPortName(self, pbstrPortName) -> Tuple_[int, str]:
        """ GetPortName(self: IDebugPortRequest2) -> (int, str) """
        ...


class IDebugPortSupplier2: # skipped bases: <type 'object'>
    """ no doc """
    def AddPort(self, pRequest, ppPort) -> Tuple_[int, IDebugPort2]:
        """ AddPort(self: IDebugPortSupplier2, pRequest: IDebugPortRequest2) -> (int, IDebugPort2) """
        ...

    def CanAddPort(self) -> int:
        """ CanAddPort(self: IDebugPortSupplier2) -> int """
        ...

    def EnumPorts(self, ppEnum) -> Tuple_[int, IEnumDebugPorts2]:
        """ EnumPorts(self: IDebugPortSupplier2) -> (int, IEnumDebugPorts2) """
        ...

    def GetPort(self, guidPort, ppPort) -> Tuple_[int, Guid, IDebugPort2]:
        """ GetPort(self: IDebugPortSupplier2, guidPort: Guid) -> (int, Guid, IDebugPort2) """
        ...

    def GetPortSupplierId(self, pguidPortSupplier) -> Tuple_[int, Guid]:
        """ GetPortSupplierId(self: IDebugPortSupplier2) -> (int, Guid) """
        ...

    def GetPortSupplierName(self, pbstrName) -> Tuple_[int, str]:
        """ GetPortSupplierName(self: IDebugPortSupplier2) -> (int, str) """
        ...

    def RemovePort(self, pPort:IDebugPort2) -> int:
        """ RemovePort(self: IDebugPortSupplier2, pPort: IDebugPort2) -> int """
        ...


class IDebugPortSupplier3(IDebugPortSupplier2): # skipped bases: <type 'object'>
    """ no doc """
    def CanPersistPorts(self) -> int:
        """ CanPersistPorts(self: IDebugPortSupplier3) -> int """
        ...

    def EnumPersistedPorts(self, PortNames, ppEnum) -> Tuple_[int, IEnumDebugPorts2]:
        """ EnumPersistedPorts(self: IDebugPortSupplier3, PortNames: BSTR_ARRAY) -> (int, IEnumDebugPorts2) """
        ...


class IDebugPortSupplierDescription2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDescription(self, pdwFlags, pbstrText) -> Tuple_[int, UInt32, str]:
        """ GetDescription(self: IDebugPortSupplierDescription2) -> (int, UInt32, str) """
        ...


class IDebugPortSupplierEx2: # skipped bases: <type 'object'>
    """ no doc """
    def SetServer(self, pServer:IDebugCoreServer2) -> int:
        """ SetServer(self: IDebugPortSupplierEx2, pServer: IDebugCoreServer2) -> int """
        ...


class IDebugPortSupplierLocale2: # skipped bases: <type 'object'>
    """ no doc """
    def SetLocale(self, wLangID:UInt16) -> int:
        """ SetLocale(self: IDebugPortSupplierLocale2, wLangID: UInt16) -> int """
        ...


class IDebugPrimitiveTypeField(IDebugField): # skipped bases: <type 'object'>
    """ no doc """
    def GetPrimitiveType(self, pdwType) -> Tuple_[int, UInt32]:
        """ GetPrimitiveType(self: IDebugPrimitiveTypeField) -> (int, UInt32) """
        ...


class IDebugProcess2: # skipped bases: <type 'object'>
    """ no doc """
    def Attach(self, pCallback, rgguidSpecificEngines, celtSpecificEngines, rghrEngineAttach) -> Tuple_[int, Array]:
        """ Attach(self: IDebugProcess2, pCallback: IDebugEventCallback2, rgguidSpecificEngines: Array[Guid], celtSpecificEngines: UInt32) -> (int, Array[int]) """
        ...

    def CanDetach(self) -> int:
        """ CanDetach(self: IDebugProcess2) -> int """
        ...

    def CauseBreak(self) -> int:
        """ CauseBreak(self: IDebugProcess2) -> int """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugProcess2) -> int """
        ...

    def EnumPrograms(self, ppEnum) -> Tuple_[int, IEnumDebugPrograms2]:
        """ EnumPrograms(self: IDebugProcess2) -> (int, IEnumDebugPrograms2) """
        ...

    def EnumThreads(self, ppEnum) -> Tuple_[int, IEnumDebugThreads2]:
        """ EnumThreads(self: IDebugProcess2) -> (int, IEnumDebugThreads2) """
        ...

    def GetAttachedSessionName(self, pbstrSessionName) -> Tuple_[int, str]:
        """ GetAttachedSessionName(self: IDebugProcess2) -> (int, str) """
        ...

    def GetInfo(self):
        """ no doc """
        ...

    def GetName(self, gnType, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugProcess2, gnType: UInt32) -> (int, str) """
        ...

    def GetPhysicalProcessId(self, pProcessId) -> Tuple_[int, Array]:
        """ GetPhysicalProcessId(self: IDebugProcess2) -> (int, Array[AD_PROCESS_ID]) """
        ...

    def GetPort(self, ppPort) -> Tuple_[int, IDebugPort2]:
        """ GetPort(self: IDebugProcess2) -> (int, IDebugPort2) """
        ...

    def GetProcessId(self, pguidProcessId) -> Tuple_[int, Guid]:
        """ GetProcessId(self: IDebugProcess2) -> (int, Guid) """
        ...

    def GetServer(self, ppServer) -> Tuple_[int, IDebugCoreServer2]:
        """ GetServer(self: IDebugProcess2) -> (int, IDebugCoreServer2) """
        ...

    def Terminate(self) -> int:
        """ Terminate(self: IDebugProcess2) -> int """
        ...


class IDebugProcess3(IDebugProcess2): # skipped bases: <type 'object'>
    """ no doc """
    def Continue(self, pThread:IDebugThread2) -> int:
        """ Continue(self: IDebugProcess3, pThread: IDebugThread2) -> int """
        ...

    def DisableENC(self, reason:EncUnavailableReason) -> int:
        """ DisableENC(self: IDebugProcess3, reason: EncUnavailableReason) -> int """
        ...

    def Execute(self, pThread:IDebugThread2) -> int:
        """ Execute(self: IDebugProcess3, pThread: IDebugThread2) -> int """
        ...

    def GetDebugReason(self, pReason) -> Tuple_[int, UInt32]:
        """ GetDebugReason(self: IDebugProcess3) -> (int, UInt32) """
        ...

    def GetENCAvailableState(self, pReason) -> Tuple_[int, Array]:
        """ GetENCAvailableState(self: IDebugProcess3) -> (int, Array[EncUnavailableReason]) """
        ...

    def GetEngineFilter(self, pEngineArray) -> Tuple_[int, Array]:
        """ GetEngineFilter(self: IDebugProcess3) -> (int, Array[GUID_ARRAY]) """
        ...

    def GetHostingProcessLanguage(self, pguidLang) -> Tuple_[int, Guid]:
        """ GetHostingProcessLanguage(self: IDebugProcess3) -> (int, Guid) """
        ...

    def SetHostingProcessLanguage(self, guidLang:Guid) -> Tuple_[int, Guid]:
        """ SetHostingProcessLanguage(self: IDebugProcess3, guidLang: Guid) -> (int, Guid) """
        ...

    def Step(self, pThread:IDebugThread2, sk:UInt32, Step:UInt32) -> int:
        """ Step(self: IDebugProcess3, pThread: IDebugThread2, sk: UInt32, Step: UInt32) -> int """
        ...


class IDebugProcessCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugProcessDestroyEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugProcessEx2: # skipped bases: <type 'object'>
    """ no doc """
    def AddImplicitProgramNodes(self, guidLaunchingEngine:Guid, rgguidSpecificEngines:Array, celtSpecificEngines:UInt32) -> Tuple_[int, Guid]:
        """ AddImplicitProgramNodes(self: IDebugProcessEx2, guidLaunchingEngine: Guid, rgguidSpecificEngines: Array[Guid], celtSpecificEngines: UInt32) -> (int, Guid) """
        ...

    def Attach(self, pSession:IDebugSession2) -> int:
        """ Attach(self: IDebugProcessEx2, pSession: IDebugSession2) -> int """
        ...

    def Detach(self, pSession:IDebugSession2) -> int:
        """ Detach(self: IDebugProcessEx2, pSession: IDebugSession2) -> int """
        ...


class IDebugProcessQueryProperties: # skipped bases: <type 'object'>
    """ no doc """
    def QueryProperties(self, celt, rgdwPropTypes, rgtPropValues) -> Tuple_[int, Array]:
        """ QueryProperties(self: IDebugProcessQueryProperties, celt: UInt32, rgdwPropTypes: Array[UInt32]) -> (int, Array[object]) """
        ...

    def QueryProperty(self, dwPropType, pvarPropValue) -> Tuple_[int, object]:
        """ QueryProperty(self: IDebugProcessQueryProperties, dwPropType: UInt32) -> (int, object) """
        ...


class IDebugProcessSecurity2: # skipped bases: <type 'object'>
    """ no doc """
    def GetUserName(self, pbstrUserName) -> Tuple_[int, str]:
        """ GetUserName(self: IDebugProcessSecurity2) -> (int, str) """
        ...

    def QueryCanSafelyAttach(self) -> int:
        """ QueryCanSafelyAttach(self: IDebugProcessSecurity2) -> int """
        ...


class IDebugProgram2: # skipped bases: <type 'object'>
    """ no doc """
    def Attach(self, pCallback:IDebugEventCallback2) -> int:
        """ Attach(self: IDebugProgram2, pCallback: IDebugEventCallback2) -> int """
        ...

    def CanDetach(self) -> int:
        """ CanDetach(self: IDebugProgram2) -> int """
        ...

    def CauseBreak(self) -> int:
        """ CauseBreak(self: IDebugProgram2) -> int """
        ...

    def Continue(self, pThread:IDebugThread2) -> int:
        """ Continue(self: IDebugProgram2, pThread: IDebugThread2) -> int """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugProgram2) -> int """
        ...

    def EnumCodeContexts(self, pDocPos, ppEnum) -> Tuple_[int, IEnumDebugCodeContexts2]:
        """ EnumCodeContexts(self: IDebugProgram2, pDocPos: IDebugDocumentPosition2) -> (int, IEnumDebugCodeContexts2) """
        ...

    def EnumCodePaths(self, pszHint, pStart, pFrame, fSource, ppEnum, ppSafety) -> Tuple_[int, IEnumCodePaths2, IDebugCodeContext2]:
        """ EnumCodePaths(self: IDebugProgram2, pszHint: str, pStart: IDebugCodeContext2, pFrame: IDebugStackFrame2, fSource: int) -> (int, IEnumCodePaths2, IDebugCodeContext2) """
        ...

    def EnumModules(self, ppEnum) -> Tuple_[int, IEnumDebugModules2]:
        """ EnumModules(self: IDebugProgram2) -> (int, IEnumDebugModules2) """
        ...

    def EnumThreads(self, ppEnum) -> Tuple_[int, IEnumDebugThreads2]:
        """ EnumThreads(self: IDebugProgram2) -> (int, IEnumDebugThreads2) """
        ...

    def Execute(self) -> int:
        """ Execute(self: IDebugProgram2) -> int """
        ...

    def GetDebugProperty(self, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetDebugProperty(self: IDebugProgram2) -> (int, IDebugProperty2) """
        ...

    def GetDisassemblyStream(self, dwScope, pCodeContext, ppDisassemblyStream) -> Tuple_[int, IDebugDisassemblyStream2]:
        """ GetDisassemblyStream(self: IDebugProgram2, dwScope: UInt32, pCodeContext: IDebugCodeContext2) -> (int, IDebugDisassemblyStream2) """
        ...

    def GetENCUpdate(self, ppUpdate) -> Tuple_[int, object]:
        """ GetENCUpdate(self: IDebugProgram2) -> (int, object) """
        ...

    def GetEngineInfo(self, pbstrEngine, pguidEngine) -> Tuple_[int, str, Guid]:
        """ GetEngineInfo(self: IDebugProgram2) -> (int, str, Guid) """
        ...

    def GetMemoryBytes(self, ppMemoryBytes) -> Tuple_[int, IDebugMemoryBytes2]:
        """ GetMemoryBytes(self: IDebugProgram2) -> (int, IDebugMemoryBytes2) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugProgram2) -> (int, str) """
        ...

    def GetProcess(self, ppProcess) -> Tuple_[int, IDebugProcess2]:
        """ GetProcess(self: IDebugProgram2) -> (int, IDebugProcess2) """
        ...

    def GetProgramId(self, pguidProgramId) -> Tuple_[int, Guid]:
        """ GetProgramId(self: IDebugProgram2) -> (int, Guid) """
        ...

    def Step(self, pThread:IDebugThread2, sk:UInt32, Step:UInt32) -> int:
        """ Step(self: IDebugProgram2, pThread: IDebugThread2, sk: UInt32, Step: UInt32) -> int """
        ...

    def Terminate(self) -> int:
        """ Terminate(self: IDebugProgram2) -> int """
        ...

    def WriteDump(self, DUMPTYPE:UInt32, pszDumpUrl:str) -> int:
        """ WriteDump(self: IDebugProgram2, DUMPTYPE: UInt32, pszDumpUrl: str) -> int """
        ...


class IDebugProgram3(IDebugProgram2): # skipped bases: <type 'object'>
    """ no doc """
    def ExecuteOnThread(self, pThread:IDebugThread2) -> int:
        """ ExecuteOnThread(self: IDebugProgram3, pThread: IDebugThread2) -> int """
        ...


class IDebugProgramCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugProgramDestroyEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetExitCode(self, pdwExit) -> Tuple_[int, UInt32]:
        """ GetExitCode(self: IDebugProgramDestroyEvent2) -> (int, UInt32) """
        ...


class IDebugProgramDestroyEventFlags2: # skipped bases: <type 'object'>
    """ no doc """
    def GetFlags(self, pdwFlags) -> Tuple_[int, UInt32]:
        """ GetFlags(self: IDebugProgramDestroyEventFlags2) -> (int, UInt32) """
        ...


class IDebugProgramEngines2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumPossibleEngines(self, celtBuffer, rgguidEngines, pceltEngines) -> Tuple_[int, Array, UInt32]:
        """ EnumPossibleEngines(self: IDebugProgramEngines2, celtBuffer: UInt32) -> (int, Array[Guid], UInt32) """
        ...

    def SetEngine(self, guidEngine:Guid) -> Tuple_[int, Guid]:
        """ SetEngine(self: IDebugProgramEngines2, guidEngine: Guid) -> (int, Guid) """
        ...


class IDebugProgramEx2: # skipped bases: <type 'object'>
    """ no doc """
    def Attach(self, pCallback:IDebugEventCallback2, dwReason:UInt32, pSession:IDebugSession2) -> int:
        """ Attach(self: IDebugProgramEx2, pCallback: IDebugEventCallback2, dwReason: UInt32, pSession: IDebugSession2) -> int """
        ...

    def GetProgramNode(self, ppProgramNode) -> Tuple_[int, IDebugProgramNode2]:
        """ GetProgramNode(self: IDebugProgramEx2) -> (int, IDebugProgramNode2) """
        ...


class IDebugProgramHost2: # skipped bases: <type 'object'>
    """ no doc """
    def GetHostId(self, pProcessId) -> Tuple_[int, Array]:
        """ GetHostId(self: IDebugProgramHost2) -> (int, Array[AD_PROCESS_ID]) """
        ...

    def GetHostMachineName(self, pbstrHostMachineName) -> Tuple_[int, str]:
        """ GetHostMachineName(self: IDebugProgramHost2) -> (int, str) """
        ...

    def GetHostName(self, dwType, pbstrHostName) -> Tuple_[int, str]:
        """ GetHostName(self: IDebugProgramHost2, dwType: UInt32) -> (int, str) """
        ...


class IDebugProgramJIT2: # skipped bases: <type 'object'>
    """ no doc """
    def GetJITCallback(self, ppCallback) -> Tuple_[int, IDebugSetJITEventCallback2]:
        """ GetJITCallback(self: IDebugProgramJIT2) -> (int, IDebugSetJITEventCallback2) """
        ...


class IDebugProgramNameChangedEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugProgramNode2: # skipped bases: <type 'object'>
    """ no doc """
    def Attach_V7(self, pMDMProgram:IDebugProgram2, pCallback:IDebugEventCallback2, dwReason:UInt32) -> int:
        """ Attach_V7(self: IDebugProgramNode2, pMDMProgram: IDebugProgram2, pCallback: IDebugEventCallback2, dwReason: UInt32) -> int """
        ...

    def DetachDebugger_V7(self) -> int:
        """ DetachDebugger_V7(self: IDebugProgramNode2) -> int """
        ...

    def GetEngineInfo(self, pbstrEngine, pguidEngine) -> Tuple_[int, str, Guid]:
        """ GetEngineInfo(self: IDebugProgramNode2) -> (int, str, Guid) """
        ...

    def GetHostMachineName_V7(self, pbstrHostMachineName) -> Tuple_[int, str]:
        """ GetHostMachineName_V7(self: IDebugProgramNode2) -> (int, str) """
        ...

    def GetHostName(self, dwHostNameType, pbstrHostName) -> Tuple_[int, str]:
        """ GetHostName(self: IDebugProgramNode2, dwHostNameType: UInt32) -> (int, str) """
        ...

    def GetHostPid(self, pHostProcessId) -> Tuple_[int, Array]:
        """ GetHostPid(self: IDebugProgramNode2) -> (int, Array[AD_PROCESS_ID]) """
        ...

    def GetProgramName(self, pbstrProgramName) -> Tuple_[int, str]:
        """ GetProgramName(self: IDebugProgramNode2) -> (int, str) """
        ...


class IDebugProgramNodeAttach2: # skipped bases: <type 'object'>
    """ no doc """
    def OnAttach(self, guidProgramId:Guid) -> Tuple_[int, Guid]:
        """ OnAttach(self: IDebugProgramNodeAttach2, guidProgramId: Guid) -> (int, Guid) """
        ...


class IDebugProgramProvider2: # skipped bases: <type 'object'>
    """ no doc """
    def GetProviderProcessData(self, Flags, pPort, ProcessId, EngineFilter, pProcess) -> Tuple_[int, Array]:
        """ GetProviderProcessData(self: IDebugProgramProvider2, Flags: UInt32, pPort: IDebugDefaultPort2, ProcessId: AD_PROCESS_ID, EngineFilter: CONST_GUID_ARRAY) -> (int, Array[PROVIDER_PROCESS_DATA]) """
        ...

    def GetProviderProgramNode(self, Flags, pPort, ProcessId, guidEngine, programId, ppProgramNode) -> Tuple_[int, Guid, IDebugProgramNode2]:
        """ GetProviderProgramNode(self: IDebugProgramProvider2, Flags: UInt32, pPort: IDebugDefaultPort2, ProcessId: AD_PROCESS_ID, guidEngine: Guid, programId: UInt64) -> (int, Guid, IDebugProgramNode2) """
        ...

    def SetLocale(self, wLangID:UInt16) -> int:
        """ SetLocale(self: IDebugProgramProvider2, wLangID: UInt16) -> int """
        ...

    def WatchForProviderEvents(self, Flags:UInt32, pPort:IDebugDefaultPort2, ProcessId:AD_PROCESS_ID, EngineFilter:CONST_GUID_ARRAY, guidLaunchingEngine:Guid, pEventCallback:IDebugPortNotify2) -> Tuple_[int, Guid]:
        """ WatchForProviderEvents(self: IDebugProgramProvider2, Flags: UInt32, pPort: IDebugDefaultPort2, ProcessId: AD_PROCESS_ID, EngineFilter: CONST_GUID_ARRAY, guidLaunchingEngine: Guid, pEventCallback: IDebugPortNotify2) -> (int, Guid) """
        ...


class IDebugProgramPublisher2: # skipped bases: <type 'object'>
    """ no doc """
    def PublishProgram(self, Engines:CONST_GUID_ARRAY, szFriendlyName:str, pDebuggeeInterface:object) -> int:
        """ PublishProgram(self: IDebugProgramPublisher2, Engines: CONST_GUID_ARRAY, szFriendlyName: str, pDebuggeeInterface: object) -> int """
        ...

    def PublishProgramNode(self, pProgramNode:IDebugProgramNode2) -> int:
        """ PublishProgramNode(self: IDebugProgramPublisher2, pProgramNode: IDebugProgramNode2) -> int """
        ...

    def SetDebuggerPresent(self, fDebuggerPresent:int) -> int:
        """ SetDebuggerPresent(self: IDebugProgramPublisher2, fDebuggerPresent: int) -> int """
        ...

    def UnpublishProgram(self, pDebuggeeInterface:object) -> int:
        """ UnpublishProgram(self: IDebugProgramPublisher2, pDebuggeeInterface: object) -> int """
        ...

    def UnpublishProgramNode(self, pProgramNode:IDebugProgramNode2) -> int:
        """ UnpublishProgramNode(self: IDebugProgramPublisher2, pProgramNode: IDebugProgramNode2) -> int """
        ...


class IDebugProperty2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumChildren(self, dwFields, dwRadix, guidFilter, dwAttribFilter, pszNameFilter, dwTimeout, ppEnum) -> Tuple_[int, Guid, IEnumDebugPropertyInfo2]:
        """ EnumChildren(self: IDebugProperty2, dwFields: UInt32, dwRadix: UInt32, guidFilter: Guid, dwAttribFilter: UInt64, pszNameFilter: str, dwTimeout: UInt32) -> (int, Guid, IEnumDebugPropertyInfo2) """
        ...

    def GetDerivedMostProperty(self, ppDerivedMost) -> Tuple_[int, IDebugProperty2]:
        """ GetDerivedMostProperty(self: IDebugProperty2) -> (int, IDebugProperty2) """
        ...

    def GetExtendedInfo(self, guidExtendedInfo, pExtendedInfo) -> Tuple_[int, Guid, object]:
        """ GetExtendedInfo(self: IDebugProperty2, guidExtendedInfo: Guid) -> (int, Guid, object) """
        ...

    def GetMemoryBytes(self, ppMemoryBytes) -> Tuple_[int, IDebugMemoryBytes2]:
        """ GetMemoryBytes(self: IDebugProperty2) -> (int, IDebugMemoryBytes2) """
        ...

    def GetMemoryContext(self, ppMemory) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext(self: IDebugProperty2) -> (int, IDebugMemoryContext2) """
        ...

    def GetParent(self, ppParent) -> Tuple_[int, IDebugProperty2]:
        """ GetParent(self: IDebugProperty2) -> (int, IDebugProperty2) """
        ...

    def GetPropertyInfo(self, dwFields, dwRadix, dwTimeout, rgpArgs, dwArgCount, pPropertyInfo) -> Tuple_[int, Array]:
        """ GetPropertyInfo(self: IDebugProperty2, dwFields: UInt32, dwRadix: UInt32, dwTimeout: UInt32, rgpArgs: Array[IDebugReference2], dwArgCount: UInt32) -> (int, Array[DEBUG_PROPERTY_INFO]) """
        ...

    def GetReference(self, ppReference) -> Tuple_[int, IDebugReference2]:
        """ GetReference(self: IDebugProperty2) -> (int, IDebugReference2) """
        ...

    def GetSize(self, pdwSize) -> Tuple_[int, UInt32]:
        """ GetSize(self: IDebugProperty2) -> (int, UInt32) """
        ...

    def SetValueAsReference(self, rgpArgs:Array, dwArgCount:UInt32, pValue:IDebugReference2, dwTimeout:UInt32) -> int:
        """ SetValueAsReference(self: IDebugProperty2, rgpArgs: Array[IDebugReference2], dwArgCount: UInt32, pValue: IDebugReference2, dwTimeout: UInt32) -> int """
        ...

    def SetValueAsString(self, pszValue:str, dwRadix:UInt32, dwTimeout:UInt32) -> int:
        """ SetValueAsString(self: IDebugProperty2, pszValue: str, dwRadix: UInt32, dwTimeout: UInt32) -> int """
        ...


class IDebugProperty3(IDebugProperty2): # skipped bases: <type 'object'>
    """ no doc """
    def CreateObjectID(self) -> int:
        """ CreateObjectID(self: IDebugProperty3) -> int """
        ...

    def DestroyObjectID(self) -> int:
        """ DestroyObjectID(self: IDebugProperty3) -> int """
        ...

    def GetCustomViewerCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCustomViewerCount(self: IDebugProperty3) -> (int, UInt32) """
        ...

    def GetCustomViewerList(self, celtSkip, celtRequested, rgViewers, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ GetCustomViewerList(self: IDebugProperty3, celtSkip: UInt32, celtRequested: UInt32) -> (int, Array[DEBUG_CUSTOM_VIEWER], UInt32) """
        ...

    def GetStringCharLength(self, pLen) -> Tuple_[int, UInt32]:
        """ GetStringCharLength(self: IDebugProperty3) -> (int, UInt32) """
        ...

    def GetStringChars(self, buflen, rgString, pceltFetched) -> Tuple_[int, str, UInt32]:
        """ GetStringChars(self: IDebugProperty3, buflen: UInt32) -> (int, str, UInt32) """
        ...

    def SetValueAsStringWithError(self, pszValue, dwRadix, dwTimeout, errorString) -> Tuple_[int, str]:
        """ SetValueAsStringWithError(self: IDebugProperty3, pszValue: str, dwRadix: UInt32, dwTimeout: UInt32) -> (int, str) """
        ...


class IDebugPropertyClose2(IDebugProperty2): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self) -> int:
        """ Close(self: IDebugPropertyClose2) -> int """
        ...


class IDebugPropertyCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDebugProperty(self, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetDebugProperty(self: IDebugPropertyCreateEvent2) -> (int, IDebugProperty2) """
        ...


class IDebugPropertyDestroyEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDebugProperty(self, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetDebugProperty(self: IDebugPropertyDestroyEvent2) -> (int, IDebugProperty2) """
        ...


class IDebugPropertyEnumType_All: # skipped bases: <type 'object'>
    """ no doc """
    def GetName(self, name) -> Tuple_[int, str]:
        """ GetName(self: IDebugPropertyEnumType_All) -> (int, str) """
        ...


class IDebugPropertyEnumType_Arguments(IDebugPropertyEnumType_All): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugPropertyEnumType_Locals(IDebugPropertyEnumType_All): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugPropertyEnumType_LocalsPlusArgs(IDebugPropertyEnumType_All): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugPropertyEnumType_Registers(IDebugPropertyEnumType_All): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugPropertyField(IDebugContainerField): # skipped bases: <type 'IDebugField'>, <type 'object'>
    """ no doc """
    def GetPropertyGetter(self, ppField) -> Tuple_[int, IDebugMethodField]:
        """ GetPropertyGetter(self: IDebugPropertyField) -> (int, IDebugMethodField) """
        ...

    def GetPropertySetter(self, ppField) -> Tuple_[int, IDebugMethodField]:
        """ GetPropertySetter(self: IDebugPropertyField) -> (int, IDebugMethodField) """
        ...


class IDebugPropertySafetyWrapper: # skipped bases: <type 'object'>
    """ no doc """
    def AfterPropertyCall(self) -> int:
        """ AfterPropertyCall(self: IDebugPropertySafetyWrapper) -> int """
        ...

    def BeforePropertyCall(self) -> int:
        """ BeforePropertyCall(self: IDebugPropertySafetyWrapper) -> int """
        ...

    def GetRawProperty(self, ppProperty) -> Tuple_[int, IDebugProperty3]:
        """ GetRawProperty(self: IDebugPropertySafetyWrapper) -> (int, IDebugProperty3) """
        ...


class IDebugProviderProgramNode2: # skipped bases: <type 'object'>
    """ no doc """
    def UnmarshalDebuggeeInterface(self, riid, ppvObject) -> Tuple_[int, Guid, IntPtr]:
        """ UnmarshalDebuggeeInterface(self: IDebugProviderProgramNode2, riid: Guid) -> (int, Guid, IntPtr) """
        ...


class IDebugQueryEngine2: # skipped bases: <type 'object'>
    """ no doc """
    def GetEngineInterface(self, ppUnk) -> Tuple_[int, object]:
        """ GetEngineInterface(self: IDebugQueryEngine2) -> (int, object) """
        ...


class IDebugReference2: # skipped bases: <type 'object'>
    """ no doc """
    def Compare(self, dwCompare:UInt32, pReference:IDebugReference2) -> int:
        """ Compare(self: IDebugReference2, dwCompare: UInt32, pReference: IDebugReference2) -> int """
        ...

    def EnumChildren(self, dwFields, dwRadix, dwAttribFilter, pszNameFilter, dwTimeout, ppEnum) -> Tuple_[int, IEnumDebugReferenceInfo2]:
        """ EnumChildren(self: IDebugReference2, dwFields: UInt32, dwRadix: UInt32, dwAttribFilter: UInt64, pszNameFilter: str, dwTimeout: UInt32) -> (int, IEnumDebugReferenceInfo2) """
        ...

    def GetDerivedMostReference(self, ppDerivedMost) -> Tuple_[int, IDebugReference2]:
        """ GetDerivedMostReference(self: IDebugReference2) -> (int, IDebugReference2) """
        ...

    def GetMemoryBytes(self, ppMemoryBytes) -> Tuple_[int, IDebugMemoryBytes2]:
        """ GetMemoryBytes(self: IDebugReference2) -> (int, IDebugMemoryBytes2) """
        ...

    def GetMemoryContext(self, ppMemory) -> Tuple_[int, IDebugMemoryContext2]:
        """ GetMemoryContext(self: IDebugReference2) -> (int, IDebugMemoryContext2) """
        ...

    def GetParent(self, ppParent) -> Tuple_[int, IDebugReference2]:
        """ GetParent(self: IDebugReference2) -> (int, IDebugReference2) """
        ...

    def GetReferenceInfo(self, dwFields, dwRadix, dwTimeout, rgpArgs, dwArgCount, pReferenceInfo) -> Tuple_[int, Array]:
        """ GetReferenceInfo(self: IDebugReference2, dwFields: UInt32, dwRadix: UInt32, dwTimeout: UInt32, rgpArgs: Array[IDebugReference2], dwArgCount: UInt32) -> (int, Array[DEBUG_REFERENCE_INFO]) """
        ...

    def GetSize(self, pdwSize) -> Tuple_[int, UInt32]:
        """ GetSize(self: IDebugReference2) -> (int, UInt32) """
        ...

    def SetReferenceType(self, dwRefType:UInt32) -> int:
        """ SetReferenceType(self: IDebugReference2, dwRefType: UInt32) -> int """
        ...

    def SetValueAsReference(self, rgpArgs:Array, dwArgCount:UInt32, pValue:IDebugReference2, dwTimeout:UInt32) -> int:
        """ SetValueAsReference(self: IDebugReference2, rgpArgs: Array[IDebugReference2], dwArgCount: UInt32, pValue: IDebugReference2, dwTimeout: UInt32) -> int """
        ...

    def SetValueAsString(self, pszValue:str, dwRadix:UInt32, dwTimeout:UInt32) -> int:
        """ SetValueAsString(self: IDebugReference2, pszValue: str, dwRadix: UInt32, dwTimeout: UInt32) -> int """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...


class IDebugRemoteServer2: # skipped bases: <type 'object'>
    """ no doc """
    def CloseRemoteResumeCookie(self, ResumeCookie:RESUME_COOKIE) -> int:
        """ CloseRemoteResumeCookie(self: IDebugRemoteServer2, ResumeCookie: RESUME_COOKIE) -> int """
        ...

    def CloseRemoteWatchCookie(self, WatchCookie:WATCH_COOKIE) -> int:
        """ CloseRemoteWatchCookie(self: IDebugRemoteServer2, WatchCookie: WATCH_COOKIE) -> int """
        ...

    def CreateRemoteInstance(self, szDll, wLangID, clsidObject, riid, ppvObject) -> Tuple_[int, Guid, Guid, IntPtr]:
        """ CreateRemoteInstance(self: IDebugRemoteServer2, szDll: str, wLangID: UInt16, clsidObject: Guid, riid: Guid) -> (int, Guid, Guid, IntPtr) """
        ...

    def DiagnoseRemoteWebDebuggingError(self, szUrl:str) -> int:
        """ DiagnoseRemoteWebDebuggingError(self: IDebugRemoteServer2, szUrl: str) -> int """
        ...

    def EnumRemoteProcesses(self, pProcessArray) -> Tuple_[int, Array]:
        """ EnumRemoteProcesses(self: IDebugRemoteServer2) -> (int, Array[ENUMERATED_PROCESS_ARRAY]) """
        ...

    def GetRemoteComputerInfo(self, pinfo) -> Tuple_[int, Array]:
        """ GetRemoteComputerInfo(self: IDebugRemoteServer2) -> (int, Array[COMPUTER_INFO]) """
        ...

    def GetRemoteProcessInfo(self, dwProcessId, Fields, pinfo) -> Tuple_[int, Array]:
        """ GetRemoteProcessInfo(self: IDebugRemoteServer2, dwProcessId: UInt32, Fields: UInt32) -> (int, Array[REMOTE_PROCESS_INFO]) """
        ...

    def GetRemoteServerName(self, pbstrName) -> Tuple_[int, str]:
        """ GetRemoteServerName(self: IDebugRemoteServer2) -> (int, str) """
        ...

    def LaunchRemoteProcess(self, LaunchInfo, pdwProcessId, pResumeCookie) -> Tuple_[int, UInt32, Array]:
        """ LaunchRemoteProcess(self: IDebugRemoteServer2, LaunchInfo: PROCESS_LAUNCH_INFO) -> (int, UInt32, Array[RESUME_COOKIE]) """
        ...

    def TerminateRemoteProcess(self, dwProcessId:UInt32) -> int:
        """ TerminateRemoteProcess(self: IDebugRemoteServer2, dwProcessId: UInt32) -> int """
        ...

    def WatchForRemoteProcessDestroy(self, pCallback, pProcess, pWatchCookie) -> Tuple_[int, Array]:
        """ WatchForRemoteProcessDestroy(self: IDebugRemoteServer2, pCallback: IDebugPortEvents2, pProcess: IDebugProcess2) -> (int, Array[WATCH_COOKIE]) """
        ...


class IDebugRemoteServerFactory2: # skipped bases: <type 'object'>
    """ no doc """
    def CreateServer(self, pSession, ppRemoteServer) -> Tuple_[int, IDebugRemoteServer2]:
        """ CreateServer(self: IDebugRemoteServerFactory2, pSession: IDebugSession2) -> (int, IDebugRemoteServer2) """
        ...


class IDebugReturnValueEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetReturnValue(self, ppReturnValue) -> Tuple_[int, IDebugProperty2]:
        """ GetReturnValue(self: IDebugReturnValueEvent2) -> (int, IDebugProperty2) """
        ...


class IDebugRuntimeJITServerProvider2: # skipped bases: <type 'object'>
    """ no doc """
    def GetRuntimeJITSession(self, ppJITServer) -> Tuple_[int, IDebugJIT2]:
        """ GetRuntimeJITSession(self: IDebugRuntimeJITServerProvider2) -> (int, IDebugJIT2) """
        ...

    def IsAvailable(self) -> int:
        """ IsAvailable(self: IDebugRuntimeJITServerProvider2) -> int """
        ...


class IDebugSession2: # skipped bases: <type 'object'>
    """ no doc """
    def CauseBreak(self) -> int:
        """ CauseBreak(self: IDebugSession2) -> int """
        ...

    def ClearAllSessionThreadStackFrames(self) -> int:
        """ ClearAllSessionThreadStackFrames(self: IDebugSession2) -> int """
        ...

    def ConnectToServer(self, szServerName, ppServer) -> Tuple_[int, IDebugCoreServer2]:
        """ ConnectToServer(self: IDebugSession2, szServerName: str) -> (int, IDebugCoreServer2) """
        ...

    def CreatePendingBreakpoint(self, pBPRequest, ppPendingBP) -> Tuple_[int, IDebugPendingBreakpoint2]:
        """ CreatePendingBreakpoint(self: IDebugSession2, pBPRequest: IDebugBreakpointRequest2) -> (int, IDebugPendingBreakpoint2) """
        ...

    def Detach(self) -> int:
        """ Detach(self: IDebugSession2) -> int """
        ...

    def DisconnectServer(self, pServer:IDebugCoreServer2) -> int:
        """ DisconnectServer(self: IDebugSession2, pServer: IDebugCoreServer2) -> int """
        ...

    def EnumCodeContexts(self, pProgram, pDocPos, ppEnum) -> Tuple_[int, IEnumDebugCodeContexts2]:
        """ EnumCodeContexts(self: IDebugSession2, pProgram: IDebugProgram2, pDocPos: IDebugDocumentPosition2) -> (int, IEnumDebugCodeContexts2) """
        ...

    def EnumDefaultExceptions(self, pParentException, ppEnum) -> Tuple_[int, IEnumDebugExceptionInfo2]:
        """ EnumDefaultExceptions(self: IDebugSession2, pParentException: Array[EXCEPTION_INFO]) -> (int, IEnumDebugExceptionInfo2) """
        ...

    def EnumMachines__deprecated(self, ppEnum) -> Tuple_[int, IEnumDebugMachines2__deprecated]:
        """ EnumMachines__deprecated(self: IDebugSession2) -> (int, IEnumDebugMachines2__deprecated) """
        ...

    def EnumPendingBreakpoints(self, pProgram, pszProgram, ppEnumBPs) -> Tuple_[int, IEnumDebugPendingBreakpoints2]:
        """ EnumPendingBreakpoints(self: IDebugSession2, pProgram: IDebugProgram2, pszProgram: str) -> (int, IEnumDebugPendingBreakpoints2) """
        ...

    def EnumProcesses(self, ppEnum) -> Tuple_[int, IEnumDebugProcesses2]:
        """ EnumProcesses(self: IDebugSession2) -> (int, IEnumDebugProcesses2) """
        ...

    def EnumSetExceptions(self, pProgram, pszProgram, guidType, ppEnum) -> Tuple_[int, Guid, IEnumDebugExceptionInfo2]:
        """ EnumSetExceptions(self: IDebugSession2, pProgram: IDebugProgram2, pszProgram: str, guidType: Guid) -> (int, Guid, IEnumDebugExceptionInfo2) """
        ...

    def GetENCUpdate(self, pProgram, ppUpdate) -> Tuple_[int, object]:
        """ GetENCUpdate(self: IDebugSession2, pProgram: IDebugProgram2) -> (int, object) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugSession2) -> (int, str) """
        ...

    def GetStoppingModel(self, pdwStoppingModel) -> Tuple_[int, UInt32]:
        """ GetStoppingModel(self: IDebugSession2) -> (int, UInt32) """
        ...

    def IsAlive(self) -> int:
        """ IsAlive(self: IDebugSession2) -> int """
        ...

    def Launch(self, pszMachine, pPort, pszExe, pszArgs, pszDir, bstrEnv, pszOptions, dwLaunchFlags, hStdInput, hStdOutput, hStdError, guidLaunchingEngine, pCallback, rgguidSpecificEngines, celtSpecificEngines, ppProcess) -> Tuple_[int, Guid, IDebugProcess2]:
        """ Launch(self: IDebugSession2, pszMachine: str, pPort: IDebugPort2, pszExe: str, pszArgs: str, pszDir: str, bstrEnv: str, pszOptions: str, dwLaunchFlags: UInt32, hStdInput: UInt32, hStdOutput: UInt32, hStdError: UInt32, guidLaunchingEngine: Guid, pCallback: IDebugEventCallback2, rgguidSpecificEngines: Array[Guid], celtSpecificEngines: UInt32) -> (int, Guid, IDebugProcess2) """
        ...

    def RegisterJITServer(self, clsidJITServer:Guid) -> Tuple_[int, Guid]:
        """ RegisterJITServer(self: IDebugSession2, clsidJITServer: Guid) -> (int, Guid) """
        ...

    def RemoveAllSetExceptions(self, guidType:Guid) -> Tuple_[int, Guid]:
        """ RemoveAllSetExceptions(self: IDebugSession2, guidType: Guid) -> (int, Guid) """
        ...

    def RemoveSetException(self, pException:Array) -> int:
        """ RemoveSetException(self: IDebugSession2, pException: Array[EXCEPTION_INFO]) -> int """
        ...

    def SetEngineMetric(self, guidEngine:Guid, pszMetric:str, varValue:object) -> Tuple_[int, Guid]:
        """ SetEngineMetric(self: IDebugSession2, guidEngine: Guid, pszMetric: str, varValue: object) -> (int, Guid) """
        ...

    def SetException(self, pException:Array) -> int:
        """ SetException(self: IDebugSession2, pException: Array[EXCEPTION_INFO]) -> int """
        ...

    def SetLocale(self, wLangID:UInt16) -> int:
        """ SetLocale(self: IDebugSession2, wLangID: UInt16) -> int """
        ...

    def SetName(self, pszName:str) -> int:
        """ SetName(self: IDebugSession2, pszName: str) -> int """
        ...

    def SetRegistryRoot(self, pszRegistryRoot:str) -> int:
        """ SetRegistryRoot(self: IDebugSession2, pszRegistryRoot: str) -> int """
        ...

    def SetStoppingModel(self, dwStoppingModel:UInt32) -> int:
        """ SetStoppingModel(self: IDebugSession2, dwStoppingModel: UInt32) -> int """
        ...

    def ShutdownSession(self) -> int:
        """ ShutdownSession(self: IDebugSession2) -> int """
        ...

    def Terminate(self, fForce:int) -> int:
        """ Terminate(self: IDebugSession2, fForce: int) -> int """
        ...

    def __deprecated_GetSessionId(self, pCallback, rgguidSpecificEngines, celtSpecificEngines, pszStartPageUrl, pbstrSessionId) -> Tuple_[int, str]:
        """ __deprecated_GetSessionId(self: IDebugSession2, pCallback: IDebugEventCallback2, rgguidSpecificEngines: Array[Guid], celtSpecificEngines: UInt32, pszStartPageUrl: str) -> (int, str) """
        ...

    def __deprecated_RegisterSessionWithServer(self, pwszServerName:str) -> int:
        """ __deprecated_RegisterSessionWithServer(self: IDebugSession2, pwszServerName: str) -> int """
        ...


class IDebugSession3(IDebugSession2): # skipped bases: <type 'object'>
    """ no doc """
    def AddExceptionCallback(self, pException:Array, pCallback:IDebugExceptionCallback2) -> int:
        """ AddExceptionCallback(self: IDebugSession3, pException: Array[EXCEPTION_INFO], pCallback: IDebugExceptionCallback2) -> int """
        ...

    def BlockingShutdownSession(self, dwTimeout:UInt32) -> int:
        """ BlockingShutdownSession(self: IDebugSession3, dwTimeout: UInt32) -> int """
        ...

    def ConnectToServerEx(self, szServerName, ConnectReason, ppServer) -> Tuple_[int, IDebugCoreServer3]:
        """ ConnectToServerEx(self: IDebugSession3, szServerName: str, ConnectReason: CONNECT_REASON) -> (int, IDebugCoreServer3) """
        ...

    def GetRecentServerNames(self, pServers) -> Tuple_[int, Array]:
        """ GetRecentServerNames(self: IDebugSession3) -> (int, Array[BSTR_ARRAY]) """
        ...

    def GetStateForAllExceptions(self, pdwState) -> Tuple_[int, UInt32]:
        """ GetStateForAllExceptions(self: IDebugSession3) -> (int, UInt32) """
        ...

    def InitializeFeatures(self, EnabledFeatures:UInt32) -> int:
        """ InitializeFeatures(self: IDebugSession3, EnabledFeatures: UInt32) -> int """
        ...

    def LoadSymbols(self) -> int:
        """ LoadSymbols(self: IDebugSession3) -> int """
        ...

    def RegisterCallback(self, pCallback:IDebugEventCallback2) -> int:
        """ RegisterCallback(self: IDebugSession3, pCallback: IDebugEventCallback2) -> int """
        ...

    def RemoveExceptionCallback(self, pException:Array, pCallback:IDebugExceptionCallback2) -> int:
        """ RemoveExceptionCallback(self: IDebugSession3, pException: Array[EXCEPTION_INFO], pCallback: IDebugExceptionCallback2) -> int """
        ...

    def SetAllExceptions(self, dwState:UInt32) -> int:
        """ SetAllExceptions(self: IDebugSession3, dwState: UInt32) -> int """
        ...

    def SetJustMyCodeState(self, fUpdate:int, dwModules:UInt32, rgJMCSpec:Array) -> int:
        """ SetJustMyCodeState(self: IDebugSession3, fUpdate: int, dwModules: UInt32, rgJMCSpec: Array[JMC_CODE_SPEC]) -> int """
        ...

    def SetMaxRecentServerNames(self, dwNewMax:UInt32) -> int:
        """ SetMaxRecentServerNames(self: IDebugSession3, dwNewMax: UInt32) -> int """
        ...

    def SetSymbolPath(self, szSymbolSearchPath:str, szSymbolCachePath:str, Flags:UInt32) -> int:
        """ SetSymbolPath(self: IDebugSession3, szSymbolSearchPath: str, szSymbolCachePath: str, Flags: UInt32) -> int """
        ...


class IDebugSessionCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugSessionDestroyEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugSessionEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetSession(self, ppSession) -> Tuple_[int, IDebugSession2]:
        """ GetSession(self: IDebugSessionEvent2) -> (int, IDebugSession2) """
        ...


class IDebugSessionProperty2(IDebugProperty3): # skipped bases: <type 'IDebugProperty2'>, <type 'object'>
    """ no doc """
    def Close(self) -> int:
        """ Close(self: IDebugSessionProperty2) -> int """
        ...

    def GetThread(self, ppThread) -> Tuple_[int, IDebugThread3]:
        """ GetThread(self: IDebugSessionProperty2) -> (int, IDebugThread3) """
        ...


class IDebugSessionProvider: # skipped bases: <type 'object'>
    """ no doc """
    def StartDebugSession(self, pda:IRemoteDebugApplication) -> int:
        """ StartDebugSession(self: IDebugSessionProvider, pda: IRemoteDebugApplication) -> int """
        ...


class IDebugSetJITEventCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def SetJITEvent(self) -> int:
        """ SetJITEvent(self: IDebugSetJITEventCallback2) -> int """
        ...


class IDebugSettingsCallback2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumEEs(self, celtBuffer, rgguidLang, rgguidVendor, pceltEEs) -> Tuple_[int, Array, Array, UInt32]:
        """ EnumEEs(self: IDebugSettingsCallback2, celtBuffer: UInt32) -> (int, Array[Guid], Array[Guid], UInt32) """
        ...

    def GetEELocalObject(self, guidLang, guidVendor, pszMetric, ppUnk) -> Tuple_[int, Guid, Guid, object]:
        """ GetEELocalObject(self: IDebugSettingsCallback2, guidLang: Guid, guidVendor: Guid, pszMetric: str) -> (int, Guid, Guid, object) """
        ...

    def GetEEMetricDword(self, guidLang, guidVendor, pszMetric, pdwValue) -> Tuple_[int, Guid, Guid, UInt32]:
        """ GetEEMetricDword(self: IDebugSettingsCallback2, guidLang: Guid, guidVendor: Guid, pszMetric: str) -> (int, Guid, Guid, UInt32) """
        ...

    def GetEEMetricFile(self, guidLang, guidVendor, pszMetric, pbstrValue) -> Tuple_[int, Guid, Guid, str]:
        """ GetEEMetricFile(self: IDebugSettingsCallback2, guidLang: Guid, guidVendor: Guid, pszMetric: str) -> (int, Guid, Guid, str) """
        ...

    def GetEEMetricGuid(self, guidLang, guidVendor, pszMetric, pguidValue) -> Tuple_[int, Guid, Guid, Guid]:
        """ GetEEMetricGuid(self: IDebugSettingsCallback2, guidLang: Guid, guidVendor: Guid, pszMetric: str) -> (int, Guid, Guid, Guid) """
        ...

    def GetEEMetricString(self, guidLang, guidVendor, pszMetric, pbstrValue) -> Tuple_[int, Guid, Guid, str]:
        """ GetEEMetricString(self: IDebugSettingsCallback2, guidLang: Guid, guidVendor: Guid, pszMetric: str) -> (int, Guid, Guid, str) """
        ...

    def GetMetricDword(self, pszType, guidSection, pszMetric, pdwValue) -> Tuple_[int, Guid, UInt32]:
        """ GetMetricDword(self: IDebugSettingsCallback2, pszType: str, guidSection: Guid, pszMetric: str) -> (int, Guid, UInt32) """
        ...

    def GetMetricGuid(self, pszType, guidSection, pszMetric, pguidValue) -> Tuple_[int, Guid, Guid]:
        """ GetMetricGuid(self: IDebugSettingsCallback2, pszType: str, guidSection: Guid, pszMetric: str) -> (int, Guid, Guid) """
        ...

    def GetMetricString(self, pszType, guidSection, pszMetric, pbstrValue) -> Tuple_[int, Guid, str]:
        """ GetMetricString(self: IDebugSettingsCallback2, pszType: str, guidSection: Guid, pszMetric: str) -> (int, Guid, str) """
        ...


class IDebugSourceServerModule: # skipped bases: <type 'object'>
    """ no doc """
    def GetSourceServerData(self, pDataByteCount, ppData) -> Tuple_[int, UInt32, Array]:
        """ GetSourceServerData(self: IDebugSourceServerModule) -> (int, UInt32, Array[IntPtr]) """
        ...


class IDebugSQLCLRProgramNode2: # skipped bases: <type 'object'>
    """ no doc """
    def GetConnectionId(self, pdwId) -> Tuple_[int, UInt32]:
        """ GetConnectionId(self: IDebugSQLCLRProgramNode2) -> (int, UInt32) """
        ...


class IDebugStackFrame: # skipped bases: <type 'object'>
    """ no doc """
    def GetCodeContext(self, ppcc) -> Tuple_[int, IDebugCodeContext]:
        """ GetCodeContext(self: IDebugStackFrame) -> (int, IDebugCodeContext) """
        ...

    def GetDebugProperty(self, ppDebugProp) -> Tuple_[int, IDebugProperty]:
        """ GetDebugProperty(self: IDebugStackFrame) -> (int, IDebugProperty) """
        ...

    def GetDescriptionString(self, fLong, pbstrDescription) -> Tuple_[int, str]:
        """ GetDescriptionString(self: IDebugStackFrame, fLong: int) -> (int, str) """
        ...

    def GetLanguageString(self, fLong, pbstrLanguage) -> Tuple_[int, str]:
        """ GetLanguageString(self: IDebugStackFrame, fLong: int) -> (int, str) """
        ...

    def GetThread(self, ppat) -> Tuple_[int, IDebugApplicationThread]:
        """ GetThread(self: IDebugStackFrame) -> (int, IDebugApplicationThread) """
        ...


class IDebugStackFrame2: # skipped bases: <type 'object'>
    """ no doc """
    def EnumProperties(self, dwFields, nRadix, guidFilter, dwTimeout, pcelt, ppEnum) -> Tuple_[int, Guid, UInt32, IEnumDebugPropertyInfo2]:
        """ EnumProperties(self: IDebugStackFrame2, dwFields: UInt32, nRadix: UInt32, guidFilter: Guid, dwTimeout: UInt32) -> (int, Guid, UInt32, IEnumDebugPropertyInfo2) """
        ...

    def GetCodeContext(self, ppCodeCxt) -> Tuple_[int, IDebugCodeContext2]:
        """ GetCodeContext(self: IDebugStackFrame2) -> (int, IDebugCodeContext2) """
        ...

    def GetDebugProperty(self, ppProperty) -> Tuple_[int, IDebugProperty2]:
        """ GetDebugProperty(self: IDebugStackFrame2) -> (int, IDebugProperty2) """
        ...

    def GetDocumentContext(self, ppCxt) -> Tuple_[int, IDebugDocumentContext2]:
        """ GetDocumentContext(self: IDebugStackFrame2) -> (int, IDebugDocumentContext2) """
        ...

    def GetExpressionContext(self, ppExprCxt) -> Tuple_[int, IDebugExpressionContext2]:
        """ GetExpressionContext(self: IDebugStackFrame2) -> (int, IDebugExpressionContext2) """
        ...

    def GetInfo(self, dwFieldSpec, nRadix, pFrameInfo) -> Tuple_[int, Array]:
        """ GetInfo(self: IDebugStackFrame2, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, Array[FRAMEINFO]) """
        ...

    def GetLanguageInfo(self, pbstrLanguage, pguidLanguage) -> Tuple_[int, str, Guid]:
        """ GetLanguageInfo(self: IDebugStackFrame2) -> (int, str, Guid) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugStackFrame2) -> (int, str) """
        ...

    def GetPhysicalStackRange(self, paddrMin, paddrMax) -> Tuple_[int, UInt64, UInt64]:
        """ GetPhysicalStackRange(self: IDebugStackFrame2) -> (int, UInt64, UInt64) """
        ...

    def GetThread(self, ppThread) -> Tuple_[int, IDebugThread2]:
        """ GetThread(self: IDebugStackFrame2) -> (int, IDebugThread2) """
        ...


class IDebugStackFrame3(IDebugStackFrame2): # skipped bases: <type 'object'>
    """ no doc """
    def GetUnwindCodeContext(self, ppCodeContext) -> Tuple_[int, IDebugCodeContext2]:
        """ GetUnwindCodeContext(self: IDebugStackFrame3) -> (int, IDebugCodeContext2) """
        ...

    def InterceptCurrentException(self, dwFlags, pqwCookie) -> Tuple_[int, UInt64]:
        """ InterceptCurrentException(self: IDebugStackFrame3, dwFlags: UInt32) -> (int, UInt64) """
        ...


class IDebugStackFrameSniffer: # skipped bases: <type 'object'>
    """ no doc """
    def EnumStackFrames(self, ppedsf) -> Tuple_[int, IEnumDebugStackFrames]:
        """ EnumStackFrames(self: IDebugStackFrameSniffer) -> (int, IEnumDebugStackFrames) """
        ...


class IDebugStackFrameSnifferEx32(IDebugStackFrameSniffer): # skipped bases: <type 'object'>
    """ no doc """
    def EnumStackFramesEx32(self, dwSpMin, ppedsf) -> Tuple_[int, IEnumDebugStackFrames]:
        """ EnumStackFramesEx32(self: IDebugStackFrameSnifferEx32, dwSpMin: UInt32) -> (int, IEnumDebugStackFrames) """
        ...


class IDebugStackFrameSnifferEx64(IDebugStackFrameSniffer): # skipped bases: <type 'object'>
    """ no doc """
    def EnumStackFramesEx64(self, dwSpMin, ppedsf) -> Tuple_[int, IEnumDebugStackFrames64]:
        """ EnumStackFramesEx64(self: IDebugStackFrameSnifferEx64, dwSpMin: UInt64) -> (int, IEnumDebugStackFrames64) """
        ...


class IDebugStepCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugStopCompleteEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugSymbolProviderDirect: # skipped bases: <type 'object'>
    """ no doc """
    def GetAppIDFromAddress(self, pAddress:IDebugAddress, pAppID:UInt32) -> Tuple_[int, UInt32]:
        """ GetAppIDFromAddress(self: IDebugSymbolProviderDirect, pAddress: IDebugAddress, pAppID: UInt32) -> (int, UInt32) """
        ...

    def GetCurrentModulesInfo(self, pCount:UInt32, ppGuids:Guid, pADIds:UInt32, pCurrentState:UInt32, ppCDModItfs:object) -> Tuple_[int, UInt32, Guid, UInt32, UInt32, object]:
        """ GetCurrentModulesInfo(self: IDebugSymbolProviderDirect, pCount: UInt32, ppGuids: Guid, pADIds: UInt32, pCurrentState: UInt32, ppCDModItfs: object) -> (int, UInt32, Guid, UInt32, UInt32, object) """
        ...

    def GetCurrentModulesState(self, pState:UInt32, count:UInt32) -> Tuple_[int, UInt32, UInt32]:
        """ GetCurrentModulesState(self: IDebugSymbolProviderDirect, pState: UInt32, count: UInt32) -> (int, UInt32, UInt32) """
        ...

    def GetMetaDataImport(self, guid:Guid, appID:UInt32, ppImport:object) -> Tuple_[int, Guid, object]:
        """ GetMetaDataImport(self: IDebugSymbolProviderDirect, guid: Guid, appID: UInt32, ppImport: object) -> (int, Guid, object) """
        ...

    def GetMethodFromAddress(self, pAddress:IDebugAddress, pGuid:Guid, pAppID:UInt32, pTokenClass:int, pTokenMethod:int, pdwOffset:UInt32, pdwVersion:UInt32) -> Tuple_[int, Guid, UInt32, int, int, UInt32, UInt32]:
        """ GetMethodFromAddress(self: IDebugSymbolProviderDirect, pAddress: IDebugAddress, pGuid: Guid, pAppID: UInt32, pTokenClass: int, pTokenMethod: int, pdwOffset: UInt32, pdwVersion: UInt32) -> (int, Guid, UInt32, int, int, UInt32, UInt32) """
        ...

    def GetSymUnmanagedReader(self, ulAppDomainID, guidModule, ppSymUnmanagedReader) -> Tuple_[int, object]:
        """ GetSymUnmanagedReader(self: IDebugSymbolProviderDirect, ulAppDomainID: UInt32, guidModule: Guid) -> (int, object) """
        ...


class IDebugSymbolProviderGroup: # skipped bases: <type 'object'>
    """ no doc """
    def CreateGroup(self, ppGroup:object) -> Tuple_[int, object]:
        """ CreateGroup(self: IDebugSymbolProviderGroup, ppGroup: object) -> (int, object) """
        ...

    def SetGroup(self, pGroup:object) -> int:
        """ SetGroup(self: IDebugSymbolProviderGroup, pGroup: object) -> int """
        ...


class IDebugSymbolSearchEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetSymbolSearchInfo(self, pModule, pbstrDebugMessage, pdwModuleInfoFlags) -> Tuple_[int, IDebugModule3, str, UInt32]:
        """ GetSymbolSearchInfo(self: IDebugSymbolSearchEvent2) -> (int, IDebugModule3, str, UInt32) """
        ...


class IDebugSyncOperation: # skipped bases: <type 'object'>
    """ no doc """
    def Execute(self, ppunkResult) -> Tuple_[int, object]:
        """ Execute(self: IDebugSyncOperation) -> (int, object) """
        ...

    def GetTargetThread(self, ppatTarget) -> Tuple_[int, IDebugApplicationThread]:
        """ GetTargetThread(self: IDebugSyncOperation) -> (int, IDebugApplicationThread) """
        ...

    def InProgressAbort(self) -> int:
        """ InProgressAbort(self: IDebugSyncOperation) -> int """
        ...


class IDebugThisAdjust: # skipped bases: <type 'object'>
    """ no doc """
    def GetThisAdjustor(self, pThisAdjust) -> Tuple_[int, int]:
        """ GetThisAdjustor(self: IDebugThisAdjust) -> (int, int) """
        ...


class IDebugThread2: # skipped bases: <type 'object'>
    """ no doc """
    def CanSetNextStatement(self, pStackFrame:IDebugStackFrame2, pCodeContext:IDebugCodeContext2) -> int:
        """ CanSetNextStatement(self: IDebugThread2, pStackFrame: IDebugStackFrame2, pCodeContext: IDebugCodeContext2) -> int """
        ...

    def EnumFrameInfo(self, dwFieldSpec, nRadix, ppEnum) -> Tuple_[int, IEnumDebugFrameInfo2]:
        """ EnumFrameInfo(self: IDebugThread2, dwFieldSpec: UInt32, nRadix: UInt32) -> (int, IEnumDebugFrameInfo2) """
        ...

    def GetLogicalThread(self, pStackFrame, ppLogicalThread) -> Tuple_[int, IDebugLogicalThread2]:
        """ GetLogicalThread(self: IDebugThread2, pStackFrame: IDebugStackFrame2) -> (int, IDebugLogicalThread2) """
        ...

    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugThread2) -> (int, str) """
        ...

    def GetProgram(self, ppProgram) -> Tuple_[int, IDebugProgram2]:
        """ GetProgram(self: IDebugThread2) -> (int, IDebugProgram2) """
        ...

    def GetThreadId(self, pdwThreadId) -> Tuple_[int, UInt32]:
        """ GetThreadId(self: IDebugThread2) -> (int, UInt32) """
        ...

    def GetThreadProperties(self, dwFields, ptp) -> Tuple_[int, Array]:
        """ GetThreadProperties(self: IDebugThread2, dwFields: UInt32) -> (int, Array[THREADPROPERTIES]) """
        ...

    def Resume(self, pdwSuspendCount) -> Tuple_[int, UInt32]:
        """ Resume(self: IDebugThread2) -> (int, UInt32) """
        ...

    def SetNextStatement(self, pStackFrame:IDebugStackFrame2, pCodeContext:IDebugCodeContext2) -> int:
        """ SetNextStatement(self: IDebugThread2, pStackFrame: IDebugStackFrame2, pCodeContext: IDebugCodeContext2) -> int """
        ...

    def SetThreadName(self, pszName:str) -> int:
        """ SetThreadName(self: IDebugThread2, pszName: str) -> int """
        ...

    def Suspend(self, pdwSuspendCount) -> Tuple_[int, UInt32]:
        """ Suspend(self: IDebugThread2) -> (int, UInt32) """
        ...


class IDebugThread3(IDebugThread2): # skipped bases: <type 'object'>
    """ no doc """
    def CanRemapLeafFrame(self) -> int:
        """ CanRemapLeafFrame(self: IDebugThread3) -> int """
        ...

    def IsCurrentException(self) -> int:
        """ IsCurrentException(self: IDebugThread3) -> int """
        ...

    def RemapLeafFrame(self) -> int:
        """ RemapLeafFrame(self: IDebugThread3) -> int """
        ...


class IDebugThreadCall32: # skipped bases: <type 'object'>
    """ no doc """
    def ThreadCallHandler(self, dwParam1:IntPtr, dwParam2:IntPtr, dwParam3:IntPtr) -> IntPtr:
        """ ThreadCallHandler(self: IDebugThreadCall32, dwParam1: IntPtr, dwParam2: IntPtr, dwParam3: IntPtr) -> IntPtr """
        ...


class IDebugThreadCall64: # skipped bases: <type 'object'>
    """ no doc """
    def ThreadCallHandler(self, dwParam1:UInt64, dwParam2:UInt64, dwParam3:UInt64) -> IntPtr:
        """ ThreadCallHandler(self: IDebugThreadCall64, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> IntPtr """
        ...


class IDebugThreadCreateEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugThreadDestroyEvent2: # skipped bases: <type 'object'>
    """ no doc """
    def GetExitCode(self, pdwExit) -> Tuple_[int, UInt32]:
        """ GetExitCode(self: IDebugThreadDestroyEvent2) -> (int, UInt32) """
        ...


class IDebugThreadNameChangedEvent2: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDebugTypeFieldBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def CreatePointerToType(self, pTypeField, pPtrToTypeField) -> Tuple_[int, IDebugField]:
        """ CreatePointerToType(self: IDebugTypeFieldBuilder, pTypeField: IDebugField) -> (int, IDebugField) """
        ...

    def CreatePrimitive(self, dwElementType, pTypeField) -> Tuple_[int, IDebugField]:
        """ CreatePrimitive(self: IDebugTypeFieldBuilder, dwElementType: UInt32) -> (int, IDebugField) """
        ...


class IDebugTypeFieldBuilder2(IDebugTypeFieldBuilder): # skipped bases: <type 'object'>
    """ no doc """
    def CreateArrayOfType(self, pTypeField, rank, pArrayOfTypeField) -> Tuple_[int, IDebugField]:
        """ CreateArrayOfType(self: IDebugTypeFieldBuilder2, pTypeField: IDebugField, rank: UInt32) -> (int, IDebugField) """
        ...


class IDebugWindowsComputerPort2: # skipped bases: <type 'object'>
    """ no doc """
    def GetComputerInfo(self, pinfo) -> Tuple_[int, Array]:
        """ GetComputerInfo(self: IDebugWindowsComputerPort2) -> (int, Array[COMPUTER_INFO]) """
        ...


class IDebugWrappedJITDebugger2(IDebugJIT2): # skipped bases: <type 'object'>
    """ no doc """
    def GetName(self, pbstrName) -> Tuple_[int, str]:
        """ GetName(self: IDebugWrappedJITDebugger2) -> (int, str) """
        ...


class IEEAssemblyRef: # skipped bases: <type 'object'>
    """ no doc """
    def GetCulture(self, bstr) -> Tuple_[int, str]:
        """ GetCulture(self: IEEAssemblyRef) -> (int, str) """
        ...

    def GetName(self, bstr) -> Tuple_[int, str]:
        """ GetName(self: IEEAssemblyRef) -> (int, str) """
        ...

    def GetPublicKey(self, key) -> Tuple_[int, str]:
        """ GetPublicKey(self: IEEAssemblyRef) -> (int, str) """
        ...

    def GetVersion(self, major, minor, build, revision) -> Tuple_[int, UInt16, UInt16, UInt16, UInt16]:
        """ GetVersion(self: IEEAssemblyRef) -> (int, UInt16, UInt16, UInt16, UInt16) """
        ...


class IEEAssemblyRefResolveComparer: # skipped bases: <type 'object'>
    """ no doc """
    def CompareRef(self, cookieFirst, cookieSecond, cookieTarget, firstIsBetter) -> Tuple_[int, int]:
        """ CompareRef(self: IEEAssemblyRefResolveComparer, cookieFirst: UInt32, cookieSecond: UInt32, cookieTarget: UInt32) -> (int, int) """
        ...


class IEEDataStorage: # skipped bases: <type 'object'>
    """ no doc """
    def GetData(self, dataSize, sizeGotten, data) -> Tuple_[int, UInt32, Array]:
        """ GetData(self: IEEDataStorage, dataSize: UInt32) -> (int, UInt32, Array[Byte]) """
        ...

    def GetSize(self, size) -> Tuple_[int, UInt32]:
        """ GetSize(self: IEEDataStorage) -> (int, UInt32) """
        ...


class IEEHelperObject: # skipped bases: <type 'object'>
    """ no doc """
    def GETASSEMBLY(self, assemblyCookie, Flags, flagsOut, name, assemBytes, pdbBytes) -> Tuple_[int, UInt32, str, IEEDataStorage, IEEDataStorage]:
        """ GETASSEMBLY(self: IEEHelperObject, assemblyCookie: UInt32, Flags: UInt32) -> (int, UInt32, str, IEEDataStorage, IEEDataStorage) """
        ...

    def GetAssemblyRefForCookie(self, cookie, ppAssemRef) -> Tuple_[int, IEEAssemblyRef]:
        """ GetAssemblyRefForCookie(self: IEEHelperObject, cookie: UInt32) -> (int, IEEAssemblyRef) """
        ...

    def GetHostAssembly(self, Flags, assemBytes, pdbBytes) -> Tuple_[int, IEEDataStorage, IEEDataStorage]:
        """ GetHostAssembly(self: IEEHelperObject, Flags: UInt32) -> (int, IEEDataStorage, IEEDataStorage) """
        ...

    def GetTargetAssembly(self, name, cookie) -> Tuple_[int, UInt32]:
        """ GetTargetAssembly(self: IEEHelperObject, name: str) -> (int, UInt32) """
        ...

    def GetTargetClass(self, name, assemblyCookie, cookie, valueAttrCount, viewerAttrCount, visualizerAttrCount) -> Tuple_[int, UInt32, UInt32, UInt32, UInt32]:
        """ GetTargetClass(self: IEEHelperObject, name: str, assemblyCookie: UInt32) -> (int, UInt32, UInt32, UInt32, UInt32) """
        ...

    def GetValueAttributeProps(self, classCookie, ordinal, targetedAssembly, assemLocation, name, value, type) -> Tuple_[int, str, UInt32, str, str, str]:
        """ GetValueAttributeProps(self: IEEHelperObject, classCookie: UInt32, ordinal: UInt32) -> (int, str, UInt32, str, str, str) """
        ...

    def GetViewerAttributeProps(self, classCookie, ordinal, targetedAssembly, assemLocation, className, classAssemLocation) -> Tuple_[int, str, UInt32, str, UInt32]:
        """ GetViewerAttributeProps(self: IEEHelperObject, classCookie: UInt32, ordinal: UInt32) -> (int, str, UInt32, str, UInt32) """
        ...

    def GetVisualizerAttributeProps(self, classCookie, ordinal, targetedAssembly, assemLocation, displayClassName, displayClassAssemLocation, proxyClassName, proxyClassAssemLocation, description, uiType) -> Tuple_[int, str, UInt32, str, UInt32, str, UInt32, str, UInt32]:
        """ GetVisualizerAttributeProps(self: IEEHelperObject, classCookie: UInt32, ordinal: UInt32) -> (int, str, UInt32, str, UInt32, str, UInt32, str, UInt32) """
        ...

    def InitCache(self, pResolver:IEEAssemblyRefResolveComparer) -> int:
        """ InitCache(self: IEEHelperObject, pResolver: IEEAssemblyRefResolveComparer) -> int """
        ...


class IEEHostServices: # skipped bases: <type 'object'>
    """ no doc """
    def GetHostValue(self, valueCatagory, valueKind, result) -> Tuple_[int, object]:
        """ GetHostValue(self: IEEHostServices, valueCatagory: str, valueKind: str) -> (int, object) """
        ...

    def SetHostValue(self, valueCatagory:str, valueKind:str, newValue:object) -> int:
        """ SetHostValue(self: IEEHostServices, valueCatagory: str, valueKind: str, newValue: object) -> int """
        ...


class IEELocalObject: # skipped bases: <type 'object'>
    """ no doc """
    def SetCallback(self, pCallback:IDebugSettingsCallback2) -> int:
        """ SetCallback(self: IEELocalObject, pCallback: IDebugSettingsCallback2) -> int """
        ...


class IEEVisualizerDataProvider: # skipped bases: <type 'object'>
    """ no doc """
    def CanSetObjectForVisualizer(self, b) -> Tuple_[int, int]:
        """ CanSetObjectForVisualizer(self: IEEVisualizerDataProvider) -> (int, int) """
        ...

    def GetNewObjectForVisualizer(self, ppObject) -> Tuple_[int, IDebugObject]:
        """ GetNewObjectForVisualizer(self: IEEVisualizerDataProvider) -> (int, IDebugObject) """
        ...

    def GetObjectForVisualizer(self, ppObject) -> Tuple_[int, IDebugObject]:
        """ GetObjectForVisualizer(self: IEEVisualizerDataProvider) -> (int, IDebugObject) """
        ...

    def SetObjectForVisualizer(self, pNewObject, error, pException) -> Tuple_[int, str, IDebugObject]:
        """ SetObjectForVisualizer(self: IEEVisualizerDataProvider, pNewObject: IDebugObject) -> (int, str, IDebugObject) """
        ...


class IEEVisualizerService: # skipped bases: <type 'object'>
    """ no doc """
    def CreateInlineProxy(self, proxy, IsExceptionNotProxy, errorString) -> Tuple_[int, IDebugObject, int, str]:
        """ CreateInlineProxy(self: IEEVisualizerService) -> (int, IDebugObject, int, str) """
        ...

    def GetBrowsableState(self, propertyOrField, BrowsableKind) -> Tuple_[int, UInt32]:
        """ GetBrowsableState(self: IEEVisualizerService, propertyOrField: IDebugField) -> (int, UInt32) """
        ...

    def GetCustomViewerCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCustomViewerCount(self: IEEVisualizerService) -> (int, UInt32) """
        ...

    def GetCustomViewerList(self, celtSkip, celtRequested, rgViewers, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ GetCustomViewerList(self: IEEVisualizerService, celtSkip: UInt32, celtRequested: UInt32) -> (int, Array[DEBUG_CUSTOM_VIEWER], UInt32) """
        ...

    def GetPropertyProxy(self, dwID, proxy) -> Tuple_[int, IPropertyProxyEESide]:
        """ GetPropertyProxy(self: IEEVisualizerService, dwID: UInt32) -> (int, IPropertyProxyEESide) """
        ...

    def GetValueDisplayStringCount(self, DisplayKind, propertyOrField, pcelt) -> Tuple_[int, UInt32]:
        """ GetValueDisplayStringCount(self: IEEVisualizerService, DisplayKind: UInt32, propertyOrField: IDebugField) -> (int, UInt32) """
        ...

    def GetValueDisplayStrings(self, DisplayKind, propertyOrField, celtSkip, celtRequested, rgStrings, rgIsExpression, pceltFetched) -> Tuple_[int, Array, Array, UInt32]:
        """ GetValueDisplayStrings(self: IEEVisualizerService, DisplayKind: UInt32, propertyOrField: IDebugField, celtSkip: UInt32, celtRequested: UInt32) -> (int, Array[str], Array[int], UInt32) """
        ...

    def PossiblyHasInlineProxy(self, mayHaveProxy) -> Tuple_[int, int]:
        """ PossiblyHasInlineProxy(self: IEEVisualizerService) -> (int, int) """
        ...


class IEEVisualizerServiceProvider: # skipped bases: <type 'object'>
    """ no doc """
    def CreateVisualizerService(self, binder, pSymProv, pAddress, dataProvider, ppService) -> Tuple_[int, IEEVisualizerService]:
        """ CreateVisualizerService(self: IEEVisualizerServiceProvider, binder: IDebugBinder, pSymProv: IDebugSymbolProvider, pAddress: IDebugAddress, dataProvider: IEEVisualizerDataProvider) -> (int, IEEVisualizerService) """
        ...


class IEnumCodePaths2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumCodePaths2]:
        """ Clone(self: IEnumCodePaths2) -> (int, IEnumCodePaths2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumCodePaths2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumCodePaths2, celt: UInt32) -> (int, Array[CODE_PATH], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumCodePaths2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumCodePaths2, celt: UInt32) -> int """
        ...


class IEnumDebugAddresses: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugAddresses]:
        """ Clone(self: IEnumDebugAddresses) -> (int, IEnumDebugAddresses) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugAddresses) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugAddresses, celt: UInt32) -> (int, Array[IDebugAddress], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugAddresses) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugAddresses, celt: UInt32) -> int """
        ...


class IEnumDebugApplicationNodes: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, pperddp) -> Tuple_[int, IEnumDebugApplicationNodes]:
        """ Clone(self: IEnumDebugApplicationNodes) -> (int, IEnumDebugApplicationNodes) """
        ...

    def Next(self, celt, pprddp, pceltFetched) -> Tuple_[int, IDebugApplicationNode, UInt32]:
        """ Next(self: IEnumDebugApplicationNodes, celt: UInt32) -> (int, IDebugApplicationNode, UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugApplicationNodes) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugApplicationNodes, celt: UInt32) -> int """
        ...


class IEnumDebugBoundBreakpoints2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugBoundBreakpoints2]:
        """ Clone(self: IEnumDebugBoundBreakpoints2) -> (int, IEnumDebugBoundBreakpoints2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugBoundBreakpoints2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugBoundBreakpoints2, celt: UInt32) -> (int, Array[IDebugBoundBreakpoint2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugBoundBreakpoints2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugBoundBreakpoints2, celt: UInt32) -> int """
        ...


class IEnumDebugCodeContexts: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppescc) -> Tuple_[int, IEnumDebugCodeContexts]:
        """ Clone(self: IEnumDebugCodeContexts) -> (int, IEnumDebugCodeContexts) """
        ...

    def Next(self, celt, pscc, pceltFetched) -> Tuple_[int, IDebugCodeContext, UInt32]:
        """ Next(self: IEnumDebugCodeContexts, celt: UInt32) -> (int, IDebugCodeContext, UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugCodeContexts) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugCodeContexts, celt: UInt32) -> int """
        ...


class IEnumDebugCodeContexts2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugCodeContexts2]:
        """ Clone(self: IEnumDebugCodeContexts2) -> (int, IEnumDebugCodeContexts2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugCodeContexts2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugCodeContexts2, celt: UInt32) -> (int, Array[IDebugCodeContext2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugCodeContexts2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugCodeContexts2, celt: UInt32) -> int """
        ...


class IEnumDebugCustomAttributes: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugCustomAttributes]:
        """ Clone(self: IEnumDebugCustomAttributes) -> (int, IEnumDebugCustomAttributes) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugCustomAttributes) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugCustomAttributes, celt: UInt32) -> (int, Array[IDebugCustomAttribute], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugCustomAttributes) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugCustomAttributes, celt: UInt32) -> int """
        ...


class IEnumDebugErrorBreakpoints2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugErrorBreakpoints2]:
        """ Clone(self: IEnumDebugErrorBreakpoints2) -> (int, IEnumDebugErrorBreakpoints2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugErrorBreakpoints2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugErrorBreakpoints2, celt: UInt32) -> (int, Array[IDebugErrorBreakpoint2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugErrorBreakpoints2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugErrorBreakpoints2, celt: UInt32) -> int """
        ...


class IEnumDebugExceptionInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugExceptionInfo2]:
        """ Clone(self: IEnumDebugExceptionInfo2) -> (int, IEnumDebugExceptionInfo2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugExceptionInfo2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugExceptionInfo2, celt: UInt32) -> (int, Array[EXCEPTION_INFO], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugExceptionInfo2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugExceptionInfo2, celt: UInt32) -> int """
        ...


class IEnumDebugExpressionContexts: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppedec) -> Tuple_[int, IEnumDebugExpressionContexts]:
        """ Clone(self: IEnumDebugExpressionContexts) -> (int, IEnumDebugExpressionContexts) """
        ...

    def Next(self, celt, pprgdec, pceltFetched) -> Tuple_[int, IDebugExpressionContext, UInt32]:
        """ Next(self: IEnumDebugExpressionContexts, celt: UInt32) -> (int, IDebugExpressionContext, UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugExpressionContexts) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugExpressionContexts, celt: UInt32) -> int """
        ...


class IEnumDebugExtendedPropertyInfo: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, pedpe) -> Tuple_[int, IEnumDebugExtendedPropertyInfo]:
        """ Clone(self: IEnumDebugExtendedPropertyInfo) -> (int, IEnumDebugExtendedPropertyInfo) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugExtendedPropertyInfo) -> (int, UInt32) """
        ...

    def Next(self, celt, rgExtendedPropertyInfo, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugExtendedPropertyInfo, celt: UInt32) -> (int, Array[ExtendedDebugPropertyInfo], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugExtendedPropertyInfo) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugExtendedPropertyInfo, celt: UInt32) -> int """
        ...


class IEnumDebugFields: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugFields]:
        """ Clone(self: IEnumDebugFields) -> (int, IEnumDebugFields) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugFields) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugFields, celt: UInt32) -> (int, Array[IDebugField], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugFields) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugFields, celt: UInt32) -> int """
        ...


class IEnumDebugFrameInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugFrameInfo2]:
        """ Clone(self: IEnumDebugFrameInfo2) -> (int, IEnumDebugFrameInfo2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugFrameInfo2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugFrameInfo2, celt: UInt32) -> (int, Array[FRAMEINFO], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugFrameInfo2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugFrameInfo2, celt: UInt32) -> int """
        ...


class IEnumDebugFrameInfoFilter2(IEnumDebugFrameInfo2): # skipped bases: <type 'object'>
    """ no doc """
    def CanFilter(self, pfCanFilter) -> Tuple_[int, int]:
        """ CanFilter(self: IEnumDebugFrameInfoFilter2) -> (int, int) """
        ...

    def IsFiltered(self, pfIsFiltered) -> Tuple_[int, int]:
        """ IsFiltered(self: IEnumDebugFrameInfoFilter2) -> (int, int) """
        ...


class IEnumDebugMachines2__deprecated: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugMachines2__deprecated]:
        """ Clone(self: IEnumDebugMachines2__deprecated) -> (int, IEnumDebugMachines2__deprecated) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugMachines2__deprecated) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugMachines2__deprecated, celt: UInt32) -> (int, Array[IDebugCoreServer2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugMachines2__deprecated) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugMachines2__deprecated, celt: UInt32) -> int """
        ...


class IEnumDebugModules2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugModules2]:
        """ Clone(self: IEnumDebugModules2) -> (int, IEnumDebugModules2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugModules2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugModules2, celt: UInt32) -> (int, Array[IDebugModule2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugModules2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugModules2, celt: UInt32) -> int """
        ...


class IEnumDebugObjects: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugObjects]:
        """ Clone(self: IEnumDebugObjects) -> (int, IEnumDebugObjects) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugObjects) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugObjects, celt: UInt32) -> (int, Array[IDebugObject], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugObjects) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugObjects, celt: UInt32) -> int """
        ...


class IEnumDebugPendingBreakpoints2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugPendingBreakpoints2]:
        """ Clone(self: IEnumDebugPendingBreakpoints2) -> (int, IEnumDebugPendingBreakpoints2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPendingBreakpoints2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPendingBreakpoints2, celt: UInt32) -> (int, Array[IDebugPendingBreakpoint2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPendingBreakpoints2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPendingBreakpoints2, celt: UInt32) -> int """
        ...


class IEnumDebugPorts2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugPorts2]:
        """ Clone(self: IEnumDebugPorts2) -> (int, IEnumDebugPorts2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPorts2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPorts2, celt: UInt32) -> (int, Array[IDebugPort2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPorts2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPorts2, celt: UInt32) -> int """
        ...


class IEnumDebugPortSuppliers2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugPortSuppliers2]:
        """ Clone(self: IEnumDebugPortSuppliers2) -> (int, IEnumDebugPortSuppliers2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPortSuppliers2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPortSuppliers2, celt: UInt32) -> (int, Array[IDebugPortSupplier2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPortSuppliers2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPortSuppliers2, celt: UInt32) -> int """
        ...


class IEnumDebugProcesses2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugProcesses2]:
        """ Clone(self: IEnumDebugProcesses2) -> (int, IEnumDebugProcesses2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugProcesses2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugProcesses2, celt: UInt32) -> (int, Array[IDebugProcess2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugProcesses2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugProcesses2, celt: UInt32) -> int """
        ...


class IEnumDebugPrograms2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugPrograms2]:
        """ Clone(self: IEnumDebugPrograms2) -> (int, IEnumDebugPrograms2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPrograms2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPrograms2, celt: UInt32) -> (int, Array[IDebugProgram2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPrograms2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPrograms2, celt: UInt32) -> int """
        ...


class IEnumDebugPropertyInfo: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppepi) -> Tuple_[int, IEnumDebugPropertyInfo]:
        """ Clone(self: IEnumDebugPropertyInfo) -> (int, IEnumDebugPropertyInfo) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPropertyInfo) -> (int, UInt32) """
        ...

    def Next(self, celt, pinfo, pcEltsfetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPropertyInfo, celt: UInt32) -> (int, Array[DebugPropertyInfo], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPropertyInfo) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPropertyInfo, celt: UInt32) -> int """
        ...


class IEnumDebugPropertyInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugPropertyInfo2]:
        """ Clone(self: IEnumDebugPropertyInfo2) -> (int, IEnumDebugPropertyInfo2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugPropertyInfo2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugPropertyInfo2, celt: UInt32) -> (int, Array[DEBUG_PROPERTY_INFO], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugPropertyInfo2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugPropertyInfo2, celt: UInt32) -> int """
        ...


class IEnumDebugReferenceInfo2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugReferenceInfo2]:
        """ Clone(self: IEnumDebugReferenceInfo2) -> (int, IEnumDebugReferenceInfo2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugReferenceInfo2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugReferenceInfo2, celt: UInt32) -> (int, Array[DEBUG_REFERENCE_INFO], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugReferenceInfo2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugReferenceInfo2, celt: UInt32) -> int """
        ...


class IEnumDebugSessionFrameInfo2(IEnumDebugFrameInfo2): # skipped bases: <type 'object'>
    """ no doc """
    def SetCachePriority(self, cachePriority:SESSION_CACHE_PRIORITY) -> int:
        """ SetCachePriority(self: IEnumDebugSessionFrameInfo2, cachePriority: SESSION_CACHE_PRIORITY) -> int """
        ...


class IEnumDebugStackFrames: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppedsf) -> Tuple_[int, IEnumDebugStackFrames]:
        """ Clone(self: IEnumDebugStackFrames) -> (int, IEnumDebugStackFrames) """
        ...

    def Next(self, celt, prgdsfd, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugStackFrames, celt: UInt32) -> (int, Array[DebugStackFrameDescriptor], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugStackFrames) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugStackFrames, celt: UInt32) -> int """
        ...


class IEnumDebugStackFrames2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugStackFrames2]:
        """ Clone(self: IEnumDebugStackFrames2) -> (int, IEnumDebugStackFrames2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugStackFrames2) -> (int, UInt32) """
        ...

    def GetIndex(self, pStackFrame, pIndex) -> Tuple_[int, UInt32]:
        """ GetIndex(self: IEnumDebugStackFrames2, pStackFrame: IDebugStackFrame2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugStackFrames2, celt: UInt32) -> (int, Array[IDebugStackFrame2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugStackFrames2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugStackFrames2, celt: UInt32) -> int """
        ...


class IEnumDebugStackFrames64(IEnumDebugStackFrames): # skipped bases: <type 'object'>
    """ no doc """
    def Next64(self, celt, prgdsfd, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next64(self: IEnumDebugStackFrames64, celt: UInt32) -> (int, Array[DebugStackFrameDescriptor64], UInt32) """
        ...


class IEnumDebugThreads2: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppEnum) -> Tuple_[int, IEnumDebugThreads2]:
        """ Clone(self: IEnumDebugThreads2) -> (int, IEnumDebugThreads2) """
        ...

    def GetCount(self, pcelt) -> Tuple_[int, UInt32]:
        """ GetCount(self: IEnumDebugThreads2) -> (int, UInt32) """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, UInt32]:
        """ Next(self: IEnumDebugThreads2, celt: UInt32) -> (int, Array[IDebugThread2], UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumDebugThreads2) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumDebugThreads2, celt: UInt32) -> int """
        ...


class IEnumRemoteDebugApplications: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppessd) -> Tuple_[int, IEnumRemoteDebugApplications]:
        """ Clone(self: IEnumRemoteDebugApplications) -> (int, IEnumRemoteDebugApplications) """
        ...

    def Next(self, celt, ppda, pceltFetched) -> Tuple_[int, IRemoteDebugApplication, UInt32]:
        """ Next(self: IEnumRemoteDebugApplications, celt: UInt32) -> (int, IRemoteDebugApplication, UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumRemoteDebugApplications) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumRemoteDebugApplications, celt: UInt32) -> int """
        ...


class IEnumRemoteDebugApplicationThreads: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, pperdat) -> Tuple_[int, IEnumRemoteDebugApplicationThreads]:
        """ Clone(self: IEnumRemoteDebugApplicationThreads) -> (int, IEnumRemoteDebugApplicationThreads) """
        ...

    def Next(self, celt, ppdat, pceltFetched) -> Tuple_[int, IRemoteDebugApplicationThread, UInt32]:
        """ Next(self: IEnumRemoteDebugApplicationThreads, celt: UInt32) -> (int, IRemoteDebugApplicationThread, UInt32) """
        ...

    def Reset(self) -> int:
        """ Reset(self: IEnumRemoteDebugApplicationThreads) -> int """
        ...

    def Skip(self, celt:UInt32) -> int:
        """ Skip(self: IEnumRemoteDebugApplicationThreads, celt: UInt32) -> int """
        ...


class IJITDebuggingHost2: # skipped bases: <type 'object'>
    """ no doc """
    def JITAsLoggedInUser(self, CrashingProgram:CRASHING_PROGRAM_INFO) -> int:
        """ JITAsLoggedInUser(self: IJITDebuggingHost2, CrashingProgram: CRASHING_PROGRAM_INFO) -> int """
        ...


class IMachineDebugManager: # skipped bases: <type 'object'>
    """ no doc """
    def AddApplication(self, pda, pdwAppCookie) -> Tuple_[int, UInt32]:
        """ AddApplication(self: IMachineDebugManager, pda: IRemoteDebugApplication) -> (int, UInt32) """
        ...

    def EnumApplications(self, ppeda) -> Tuple_[int, IEnumRemoteDebugApplications]:
        """ EnumApplications(self: IMachineDebugManager) -> (int, IEnumRemoteDebugApplications) """
        ...

    def RemoveApplication(self, dwAppCookie:UInt32) -> int:
        """ RemoveApplication(self: IMachineDebugManager, dwAppCookie: UInt32) -> int """
        ...


class IMachineDebugManagerCookie: # skipped bases: <type 'object'>
    """ no doc """
    def AddApplication(self, pda, dwDebugAppCookie, pdwAppCookie) -> Tuple_[int, UInt32]:
        """ AddApplication(self: IMachineDebugManagerCookie, pda: IRemoteDebugApplication, dwDebugAppCookie: UInt32) -> (int, UInt32) """
        ...

    def EnumApplications(self, ppeda) -> Tuple_[int, IEnumRemoteDebugApplications]:
        """ EnumApplications(self: IMachineDebugManagerCookie) -> (int, IEnumRemoteDebugApplications) """
        ...

    def RemoveApplication(self, dwDebugAppCookie:UInt32, dwAppCookie:UInt32) -> int:
        """ RemoveApplication(self: IMachineDebugManagerCookie, dwDebugAppCookie: UInt32, dwAppCookie: UInt32) -> int """
        ...


class IMachineDebugManagerEvents: # skipped bases: <type 'object'>
    """ no doc """
    def onAddApplication(self, pda:IRemoteDebugApplication, dwAppCookie:UInt32) -> int:
        """ onAddApplication(self: IMachineDebugManagerEvents, pda: IRemoteDebugApplication, dwAppCookie: UInt32) -> int """
        ...

    def onRemoveApplication(self, pda:IRemoteDebugApplication, dwAppCookie:UInt32) -> int:
        """ onRemoveApplication(self: IMachineDebugManagerEvents, pda: IRemoteDebugApplication, dwAppCookie: UInt32) -> int """
        ...


class IManagedViewerHost: # skipped bases: <type 'object'>
    """ no doc """
    def CreateViewer(self, hwnd:UInt32, hostServices:object, property:IPropertyProxyEESide) -> int:
        """ CreateViewer(self: IManagedViewerHost, hwnd: UInt32, hostServices: object, property: IPropertyProxyEESide) -> int """
        ...


class ISqlDebugServices: # skipped bases: <type 'object'>
    """ no doc """
    def CancelQuery(self) -> int:
        """ CancelQuery(self: ISqlDebugServices) -> int """
        ...

    def Enter(self, pszSqlUrl:str) -> int:
        """ Enter(self: ISqlDebugServices, pszSqlUrl: str) -> int """
        ...

    def GetProcidFromSProcUrl(self, pszSqlUrl, plProcId) -> Tuple_[int, UInt32]:
        """ GetProcidFromSProcUrl(self: ISqlDebugServices, pszSqlUrl: str) -> (int, UInt32) """
        ...

    def GetSPNameFromProcid(self, pszSqlUrl, pbstrProcName) -> Tuple_[int, str]:
        """ GetSPNameFromProcid(self: ISqlDebugServices, pszSqlUrl: str) -> (int, str) """
        ...

    def GetSPText(self):
        """ no doc """
        ...

    def IsDBCaseSensitive(self, pszUrl, pfYes) -> Tuple_[int, int]:
        """ IsDBCaseSensitive(self: ISqlDebugServices, pszUrl: str) -> (int, int) """
        ...

    def Leave(self, pszSqlUrl:str) -> int:
        """ Leave(self: ISqlDebugServices, pszSqlUrl: str) -> int """
        ...


class IOrclDebugServices(ISqlDebugServices): # skipped bases: <type 'object'>
    """ no doc """
    def GetLogonInfo(self, pbstrUserName, pbstrPassword, pbstrServiceName) -> Tuple_[int, str, str, str]:
        """ GetLogonInfo(self: IOrclDebugServices) -> (int, str, str, str) """
        ...


class IPerPropertyBrowsing2: # skipped bases: <type 'object'>
    """ no doc """
    def GetDisplayString(self, dispid, pBstr) -> Tuple_[int, str]:
        """ GetDisplayString(self: IPerPropertyBrowsing2, dispid: int) -> (int, str) """
        ...

    def GetPredefinedStrings(self):
        """ no doc """
        ...

    def MapPropertyToPage(self, dispid, pClsidPropPage) -> Tuple_[int, Guid]:
        """ MapPropertyToPage(self: IPerPropertyBrowsing2, dispid: int) -> (int, Guid) """
        ...

    def SetPredefinedValue(self, dispid:int, dwCookie:UInt32) -> int:
        """ SetPredefinedValue(self: IPerPropertyBrowsing2, dispid: int, dwCookie: UInt32) -> int """
        ...


class IProcessDebugManager32: # skipped bases: <type 'object'>
    """ no doc """
    def AddApplication(self, pda, pdwAppCookie) -> Tuple_[int, UInt32]:
        """ AddApplication(self: IProcessDebugManager32, pda: IDebugApplication32) -> (int, UInt32) """
        ...

    def CreateApplication(self, ppda) -> Tuple_[int, IDebugApplication32]:
        """ CreateApplication(self: IProcessDebugManager32) -> (int, IDebugApplication32) """
        ...

    def CreateDebugDocumentHelper(self, pUnkOuter, pddh) -> Tuple_[int, IDebugDocumentHelper32]:
        """ CreateDebugDocumentHelper(self: IProcessDebugManager32, pUnkOuter: object) -> (int, IDebugDocumentHelper32) """
        ...

    def GetDefaultApplication(self, ppda) -> Tuple_[int, IDebugApplication32]:
        """ GetDefaultApplication(self: IProcessDebugManager32) -> (int, IDebugApplication32) """
        ...

    def RemoveApplication(self, dwAppCookie:UInt32) -> int:
        """ RemoveApplication(self: IProcessDebugManager32, dwAppCookie: UInt32) -> int """
        ...


class IProcessDebugManager64: # skipped bases: <type 'object'>
    """ no doc """
    def AddApplication(self, pda, pdwAppCookie) -> Tuple_[int, UInt32]:
        """ AddApplication(self: IProcessDebugManager64, pda: IDebugApplication64) -> (int, UInt32) """
        ...

    def CreateApplication(self, ppda) -> Tuple_[int, IDebugApplication64]:
        """ CreateApplication(self: IProcessDebugManager64) -> (int, IDebugApplication64) """
        ...

    def CreateDebugDocumentHelper(self, pUnkOuter, pddh) -> Tuple_[int, IDebugDocumentHelper64]:
        """ CreateDebugDocumentHelper(self: IProcessDebugManager64, pUnkOuter: object) -> (int, IDebugDocumentHelper64) """
        ...

    def GetDefaultApplication(self, ppda) -> Tuple_[int, IDebugApplication64]:
        """ GetDefaultApplication(self: IProcessDebugManager64) -> (int, IDebugApplication64) """
        ...

    def RemoveApplication(self, dwAppCookie:UInt32) -> int:
        """ RemoveApplication(self: IProcessDebugManager64, dwAppCookie: UInt32) -> int """
        ...


class IPropertyProxyEESide: # skipped bases: <type 'object'>
    """ no doc """
    def CreateReplacementObject(self, dataIn, dataOut) -> Tuple_[int, IEEDataStorage]:
        """ CreateReplacementObject(self: IPropertyProxyEESide, dataIn: IEEDataStorage) -> (int, IEEDataStorage) """
        ...

    def GetInitialData(self, dataOut) -> Tuple_[int, IEEDataStorage]:
        """ GetInitialData(self: IPropertyProxyEESide) -> (int, IEEDataStorage) """
        ...

    def GetManagedViewerCreationData(self, assemName, assemBytes, assemPdb, className, alr, replacementOk) -> Tuple_[int, str, IEEDataStorage, IEEDataStorage, str, UInt32, int]:
        """ GetManagedViewerCreationData(self: IPropertyProxyEESide) -> (int, str, IEEDataStorage, IEEDataStorage, str, UInt32, int) """
        ...

    def InitSourceDataProvider(self, dataOut) -> Tuple_[int, IEEDataStorage]:
        """ InitSourceDataProvider(self: IPropertyProxyEESide) -> (int, IEEDataStorage) """
        ...

    def InPlaceUpdateObject(self, dataIn, dataOut) -> Tuple_[int, IEEDataStorage]:
        """ InPlaceUpdateObject(self: IPropertyProxyEESide, dataIn: IEEDataStorage) -> (int, IEEDataStorage) """
        ...

    def ResolveAssemblyReference(self, assemName, Flags, assemBytes, assemPdb, assemLocation, alr) -> Tuple_[int, IEEDataStorage, IEEDataStorage, str, UInt32]:
        """ ResolveAssemblyReference(self: IPropertyProxyEESide, assemName: str, Flags: UInt32) -> (int, IEEDataStorage, IEEDataStorage, str, UInt32) """
        ...


class IPropertyProxyProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetPropertyProxy(self, dwID, proxy) -> Tuple_[int, IPropertyProxyEESide]:
        """ GetPropertyProxy(self: IPropertyProxyProvider, dwID: UInt32) -> (int, IPropertyProxyEESide) """
        ...


class IProvideExpressionContexts: # skipped bases: <type 'object'>
    """ no doc """
    def EnumExpressionContexts(self, ppedec) -> Tuple_[int, IEnumDebugExpressionContexts]:
        """ EnumExpressionContexts(self: IProvideExpressionContexts) -> (int, IEnumDebugExpressionContexts) """
        ...


class IRemoteDebugApplicationEvents: # skipped bases: <type 'object'>
    """ no doc """
    def OnBreakFlagChange(self, abf:UInt32, prdatSteppingThread:IRemoteDebugApplicationThread) -> int:
        """ OnBreakFlagChange(self: IRemoteDebugApplicationEvents, abf: UInt32, prdatSteppingThread: IRemoteDebugApplicationThread) -> int """
        ...

    def onClose(self) -> int:
        """ onClose(self: IRemoteDebugApplicationEvents) -> int """
        ...

    def OnConnectDebugger(self, pad:IApplicationDebugger) -> int:
        """ OnConnectDebugger(self: IRemoteDebugApplicationEvents, pad: IApplicationDebugger) -> int """
        ...

    def OnCreateThread(self, prdat:IRemoteDebugApplicationThread) -> int:
        """ OnCreateThread(self: IRemoteDebugApplicationEvents, prdat: IRemoteDebugApplicationThread) -> int """
        ...

    def onDebugOutput(self, pstr:str) -> int:
        """ onDebugOutput(self: IRemoteDebugApplicationEvents, pstr: str) -> int """
        ...

    def OnDestroyThread(self, prdat:IRemoteDebugApplicationThread) -> int:
        """ OnDestroyThread(self: IRemoteDebugApplicationEvents, prdat: IRemoteDebugApplicationThread) -> int """
        ...

    def OnDisconnectDebugger(self) -> int:
        """ OnDisconnectDebugger(self: IRemoteDebugApplicationEvents) -> int """
        ...

    def OnEnterBreakPoint(self, prdat:IRemoteDebugApplicationThread) -> int:
        """ OnEnterBreakPoint(self: IRemoteDebugApplicationEvents, prdat: IRemoteDebugApplicationThread) -> int """
        ...

    def OnLeaveBreakPoint(self, prdat:IRemoteDebugApplicationThread) -> int:
        """ OnLeaveBreakPoint(self: IRemoteDebugApplicationEvents, prdat: IRemoteDebugApplicationThread) -> int """
        ...

    def OnSetName(self, pstrName:str) -> int:
        """ OnSetName(self: IRemoteDebugApplicationEvents, pstrName: str) -> int """
        ...


class ISimpleConnectionPoint: # skipped bases: <type 'object'>
    """ no doc """
    def Advise(self, pdisp, pdwCookie) -> Tuple_[int, UInt32]:
        """ Advise(self: ISimpleConnectionPoint, pdisp: object) -> (int, UInt32) """
        ...

    def DescribeEvents(self, iEvent, cEvents, prgid, prgbstr, pcEventsFetched) -> Tuple_[int, Array, Array, UInt32]:
        """ DescribeEvents(self: ISimpleConnectionPoint, iEvent: UInt32, cEvents: UInt32) -> (int, Array[int], Array[str], UInt32) """
        ...

    def GetEventCount(self, pulCount) -> Tuple_[int, UInt32]:
        """ GetEventCount(self: ISimpleConnectionPoint) -> (int, UInt32) """
        ...

    def Unadvise(self, dwCookie:UInt32) -> int:
        """ Unadvise(self: ISimpleConnectionPoint, dwCookie: UInt32) -> int """
        ...


class ISqlDebugServices2(ISqlDebugServices): # skipped bases: <type 'object'>
    """ no doc """
    def GetDataBaseIdFromName(self, pszSqlUrl, plDataBaseId) -> Tuple_[int, UInt32]:
        """ GetDataBaseIdFromName(self: ISqlDebugServices2, pszSqlUrl: str) -> (int, UInt32) """
        ...

    def GetDataBaseNameFromId(self, pszSqlUrl, dwDBId, pbstrDataBaseName) -> Tuple_[int, str]:
        """ GetDataBaseNameFromId(self: ISqlDebugServices2, pszSqlUrl: str, dwDBId: UInt32) -> (int, str) """
        ...


class ISqlLaunchEvent: # skipped bases: <type 'object'>
    """ no doc """
    def GetDebugString(self, st, pszOption, pbstrExecString) -> Tuple_[int, str]:
        """ GetDebugString(self: ISqlLaunchEvent, st: SERVERTYPE, pszOption: str) -> (int, str) """
        ...

    def SetDebugServiceCallback(self, pService:object) -> int:
        """ SetDebugServiceCallback(self: ISqlLaunchEvent, pService: object) -> int """
        ...


class ISqlInitializeDebuggingEvent(ISqlLaunchEvent): # skipped bases: <type 'object'>
    """ no doc """
    def GetServerToInitialize(self, pbstrServerName) -> Tuple_[int, str]:
        """ GetServerToInitialize(self: ISqlInitializeDebuggingEvent) -> (int, str) """
        ...

    def HandleDebugServerInstance(self, dwCount:UInt32, rgbData:Array) -> int:
        """ HandleDebugServerInstance(self: ISqlInitializeDebuggingEvent, dwCount: UInt32, rgbData: Array[Byte]) -> int """
        ...

    def OnCompleteExecute(self) -> int:
        """ OnCompleteExecute(self: ISqlInitializeDebuggingEvent) -> int """
        ...

    def SetError(self, hrError:int, szUserName:str) -> int:
        """ SetError(self: ISqlInitializeDebuggingEvent, hrError: int, szUserName: str) -> int """
        ...

    def SpecifyDebugServerData(self, dwCount:UInt32, rgbData:Array, dwStatus:UInt32) -> int:
        """ SpecifyDebugServerData(self: ISqlInitializeDebuggingEvent, dwCount: UInt32, rgbData: Array[Byte], dwStatus: UInt32) -> int """
        ...


class ISqlStartExecutionEvent: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ITridentEventSink: # skipped bases: <type 'object'>
    """ no doc """
    def FireEvent(self, pstrEvent, pdp, pvarRes, pei) -> Tuple_[int, object, Array]:
        """ FireEvent(self: ITridentEventSink, pstrEvent: str, pdp: Array[DISPPARAMS]) -> (int, object, Array[EXCEPINFO]) """
        ...


class JMC_CODE_SPEC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrModuleName = ...
    fIsUserCode = ...


class LOGFONTW: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    lfCharSet = ...
    lfClipPrecision = ...
    lfEscapement = ...
    lfFaceName = ...
    lfHeight = ...
    lfItalic = ...
    lfOrientation = ...
    lfOutPrecision = ...
    lfPitchAndFamily = ...
    lfQuality = ...
    lfStrikeOut = ...
    lfUnderline = ...
    lfWeight = ...
    lfWidth = ...


class MACHINE_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrName = ...
    Fields = ...
    Flags = ...


class METADATA_ADDRESS_ARRAYELEM: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwIndex = ...
    tokMethod = ...


class METADATA_ADDRESS_FIELD: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    tokField = ...


class METADATA_ADDRESS_LOCAL: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwIndex = ...
    pLocal = ...
    tokMethod = ...


class METADATA_ADDRESS_METHOD: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwOffset = ...
    dwVersion = ...
    tokMethod = ...


class METADATA_ADDRESS_PARAM: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwIndex = ...
    tokMethod = ...
    tokParam = ...


class METADATA_ADDRESS_RETVAL: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCorType = ...
    dwSigSize = ...
    rgSig = ...
    tokMethod = ...


class METADATA_TYPE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    guidModule = ...
    tokClass = ...
    ulAppDomainID = ...


class MODULE_SYMBOL_SEARCH_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrVerboseSearchInfo = ...
    dwValidFields = ...


class NameMatchOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NameMatchOptions, values: nmCaseInsensitive (2), nmCaseSensitive (1), nmNone (0) """
    nmCaseInsensitive: NameMatchOptions = ...
    nmCaseSensitive: NameMatchOptions = ...
    nmNone: NameMatchOptions = ...
    value__ = ...


class NAME_MATCH(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NAME_MATCH, values: nmCaseInsensitive (2), nmCaseSensitive (1), nmNone (0) """
    nmCaseInsensitive: NAME_MATCH = ...
    nmCaseSensitive: NAME_MATCH = ...
    nmNone: NAME_MATCH = ...
    value__ = ...


class NATIVE_ADDRESS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    unknown = ...


class NATIVE_EXCEPTION_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ExceptionCode = ...
    ExceptionFlags = ...
    ExceptionInformation = ...
    NumberOfParameters = ...


class PDB_TYPE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    guidModule = ...
    symid = ...
    ulAppDomainID = ...


class PENDING_BP_STATE_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Flags = ...
    state = ...


class PROCESS_LAUNCH_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrEnv = ...
    fLaunchSuspended = ...
    pszArgs = ...
    pszDir = ...
    pszExe = ...


class PROGRAM_NODE_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


class PROVIDER_PROCESS_DATA: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Fields = ...
    fIsDebuggerPresent = ...
    ProgramNodes = ...


class REMOTE_PROCESS_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrCommandLine = ...
    bstrCurrentDirectory = ...
    bstrEnvironmentVariables = ...
    bstrModulePath = ...
    bstrTitle = ...
    bstrUserName = ...
    dwSessionId = ...
    Fields = ...
    Flags = ...


class RESOLVED_MODULES: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ctResolvedModules = ...
    pguidResolvedModules = ...


class RESUME_COOKIE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    val = ...


class SCRIPTGCTYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SCRIPTGCTYPE, values: SCRIPTGCTYPE_EXHAUSTIVE (1), SCRIPTGCTYPE_NORMAL (0) """
    SCRIPTGCTYPE_EXHAUSTIVE: SCRIPTGCTYPE = ...
    SCRIPTGCTYPE_NORMAL: SCRIPTGCTYPE = ...
    value__ = ...


class SCRIPTSTATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SCRIPTSTATE, values: SCRIPTSTATE_CLOSED (4), SCRIPTSTATE_CONNECTED (2), SCRIPTSTATE_DISCONNECTED (3), SCRIPTSTATE_INITIALIZED (5), SCRIPTSTATE_STARTED (1), SCRIPTSTATE_UNINITIALIZED (0) """
    SCRIPTSTATE_CLOSED: SCRIPTSTATE = ...
    SCRIPTSTATE_CONNECTED: SCRIPTSTATE = ...
    SCRIPTSTATE_DISCONNECTED: SCRIPTSTATE = ...
    SCRIPTSTATE_INITIALIZED: SCRIPTSTATE = ...
    SCRIPTSTATE_STARTED: SCRIPTSTATE = ...
    SCRIPTSTATE_UNINITIALIZED: SCRIPTSTATE = ...
    value__ = ...


class SCRIPTTHREADSTATE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SCRIPTTHREADSTATE, values: SCRIPTTHREADSTATE_NOTINSCRIPT (0), SCRIPTTHREADSTATE_RUNNING (1) """
    SCRIPTTHREADSTATE_NOTINSCRIPT: SCRIPTTHREADSTATE = ...
    SCRIPTTHREADSTATE_RUNNING: SCRIPTTHREADSTATE = ...
    value__ = ...


class SERVERTYPE(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SERVERTYPE, values: ST_MSSQLSERVER (0), ST_ORACLESERVER (1), ST_REMOTEMSSQLSERVER (2) """
    ST_MSSQLSERVER: SERVERTYPE = ...
    ST_ORACLESERVER: SERVERTYPE = ...
    ST_REMOTEMSSQLSERVER: SERVERTYPE = ...
    value__ = ...


class SESSION_CACHE_PRIORITY(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SESSION_CACHE_PRIORITY, values: HIGH_CACHE_PRIORITY (1), NORMAL_CACHE_PRIORITY (0) """
    HIGH_CACHE_PRIORITY: SESSION_CACHE_PRIORITY = ...
    NORMAL_CACHE_PRIORITY: SESSION_CACHE_PRIORITY = ...
    value__ = ...


class SYMBOL_SEARCH_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrPath = ...
    hrHRESULT = ...


class TEXT_POSITION: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwColumn = ...
    dwLine = ...


class THREADPROPERTIES: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrLocation = ...
    bstrName = ...
    bstrPriority = ...
    dwFields = ...
    dwSuspendCount = ...
    dwThreadId = ...
    dwThreadState = ...


class TYPE_INFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwKind = ...
    unionmember = ...


class UNMANAGED_ADDRESS_PHYSICAL: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    offset = ...


class UNMANAGED_ADDRESS_THIS_RELATIVE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwBitLength = ...
    dwBitOffset = ...
    dwOffset = ...


class WATCH_COOKIE: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    val = ...


class WRAPPED_DEBUGGER_ARRAY: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCount = ...
    Members = ...


