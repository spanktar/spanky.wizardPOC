# -*- coding: utf-8 -*-
from plone.autoform.form import AutoExtensibleForm

from collective.z3cform.wizard import wizard
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from spanky.wizardPOC.forms import schemas


class BrokenStepOne(AutoExtensibleForm, wizard.Step):

    label = u"Broken Step One"
    schema = schemas.IFormSchemaOne


class BrokenStepTwo(AutoExtensibleForm, wizard.Step):

    label = u"Broken Step Two"
    schema = schemas.IFormSchemaTwo


class BrokenFormWizard(wizard.Wizard):

    __name__ = "BrokenFormWizard"
    steps = BrokenStepOne, BrokenStepTwo
    validate_back = False
    template = ViewPageTemplateFile('../browser/templates/broken.pt')
