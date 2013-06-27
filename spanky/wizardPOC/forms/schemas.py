# -*- coding: utf-8 -*-
from zope import schema
from plone.directives import form


class IFormSchemaOne(form.Schema):

    tweedle = schema.TextLine(
                                title=u"Tweedle Beetle:",
                                required=True,
                                )

    puddle = schema.TextLine(
                                title=u"Puddle Battle:",
                                required=True,
                                )


class IFormSchemaTwo(form.Schema):

    tweedle = schema.TextLine(
                                title=u"Poodle Noodle:",
                                required=True,
                                )

    puddle = schema.TextLine(
                                title=u"Bottle Battle:",
                                required=True,
                                )
