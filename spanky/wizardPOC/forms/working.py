# -*- coding: utf-8 -*-
from plone.autoform.form import AutoExtensibleForm

from collective.z3cform.wizard import wizard

from spanky.wizardPOC.forms import schemas


class WorkingStepOne(AutoExtensibleForm, wizard.Step):

    label = u"Working Step One"
    schema = schemas.IFormSchemaOne


class WorkingStepTwo(AutoExtensibleForm, wizard.Step):

    label = u"Working Step Two"
    schema = schemas.IFormSchemaTwo
    
    
class WorkingFormWizard(wizard.Wizard):

    __name__ = "WorkingFormWizard"
    steps = WorkingStepOne, WorkingStepTwo
    validate_back = False
