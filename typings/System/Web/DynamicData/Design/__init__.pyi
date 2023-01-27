# encoding: utf-8
# module System.Web.DynamicData.Design calls itself Design
# from System.Web.DynamicData.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.ComponentModel import ITypeDescriptorContext, StringConverter

from System.ComponentModel.Design import CollectionEditor

from System.Web.UI.Design.WebControls import DataControlFieldDesigner

from System.Windows.Forms.Design import ControlDesigner

"""The following names are not found in the module: (DataBoundControlMode, 
    DataControlField, StandardValuesCollection)
"""

# no functions
# classes

class DataControlReferenceCollectionEditor(CollectionEditor): # skipped bases: <type 'object'>
    """ DataControlReferenceCollectionEditor(type: Type) """
    pass

class DataControlReferenceIDConverter(StringConverter): # skipped bases: <type 'object'>
    """ DataControlReferenceIDConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: DataControlReferenceIDConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: DataControlReferenceIDConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: DataControlReferenceIDConverter, context: ITypeDescriptorContext) -> bool """
        ...


class DynamicDataManagerDesigner(ControlDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ DynamicDataManagerDesigner() """
    pass

class DynamicFieldDesigner(DataControlFieldDesigner): # skipped bases: <type 'object'>
    """ DynamicFieldDesigner() """
    def GetTemplateContent(self, dataControlField, mode) -> str: # Not found arg types: {'dataControlField': 'DataControlField', 'mode': 'DataBoundControlMode'}
        """ GetTemplateContent(self: DynamicFieldDesigner, dataControlField: DataControlField, mode: DataBoundControlMode) -> str """
        ...


