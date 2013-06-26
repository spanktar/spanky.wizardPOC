# -*- coding: utf-8 -*-
from Products.Five import BrowserView

from spanky.wizardPOC.forms.working import WorkingFormWizard


class WorkingFormView(BrowserView):

    wizard = None

    def getForm(self):
        self.wizard = WorkingFormWizard(self.context, self.request)
        return self.wizard()
