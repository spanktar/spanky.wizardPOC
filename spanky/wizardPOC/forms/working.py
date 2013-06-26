# -*- coding: utf-8 -*-
from plone.autoform.form import AutoExtensibleForm

from collective.z3cform.wizard import wizard

from spanky.wizardPOC.forms import schemas


class WorkingStepOne(AutoExtensibleForm, wizard.Step):

    label = u"Working Step One"
    schema = schemas.IFormSchema


class WorkingFormWizard(wizard.Wizard):

    __name__ = "WorkingFormWizard"
    steps = (WorkingStepOne,)
    validate_back = False
