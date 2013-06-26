# -*- coding: utf-8 -*-
from zope import schema
from plone.directives import form

class IFormSchema(form.Schema):
    
    tweedle = schema.TextLine(
                                title=u"Tweedle Beetle:",
                                required=True,
                                )
    
    puddle = schema.TextLine(
                                title=u"Puddle Battle:",
                                required=True,
                                )    