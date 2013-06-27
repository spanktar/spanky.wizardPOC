# -*- coding: utf-8 -*-
from plone.autoform.form import AutoExtensibleForm

from collective.z3cform.wizard import wizard
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from spanky.wizardPOC.forms import schemas


class AlmostStepOne(AutoExtensibleForm, wizard.Step):

    label = u"Almost Step One"
    schema = schemas.IFormSchemaOne
    template = ViewPageTemplateFile('../browser/templates/almost.pt')


class AlmostStepTwo(AutoExtensibleForm, wizard.Step):

    label = u"Almost Step Two"
    schema = schemas.IFormSchemaTwo
    template = ViewPageTemplateFile('../browser/templates/almost.pt')


class AlmostFormWizard(wizard.Wizard):

    __name__ = "AlmostFormWizard"
    steps = AlmostStepOne, AlmostStepTwo
    validate_back = False
