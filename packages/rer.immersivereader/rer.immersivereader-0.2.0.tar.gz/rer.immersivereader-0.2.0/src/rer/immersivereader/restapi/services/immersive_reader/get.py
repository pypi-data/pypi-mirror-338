# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import implementer, Interface


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class ImmersiveReader:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            "immersive-reader": {
                "@id": "{}/@immersive-reader".format(self.context.absolute_url())
            }
        }
        if not expand:
            return result

        enabled = True
        try:
            enabled_types = api.portal.get_registry_record(
                "rer.immersivereader.enabled_types"
            )
            if enabled_types and self.context.portal_type not in enabled_types:
                enabled = False
        except InvalidParameterError:
            enabled = False

        result["immersive-reader"]["enabled"] = enabled
        return result


class ImmersiveReaderGet(Service):
    def reply(self):
        immersive_reader = ImmersiveReader(self.context, self.request)
        return immersive_reader(expand=True)["immersive-reader"]
