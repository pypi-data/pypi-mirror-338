# -*- coding: utf-8 -*-
from plone.restapi.controlpanels import IControlpanel
from rer.immersivereader import _
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import Choice, List


class IRerImmersivereaderLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IImmersiveReaderSettings(Interface):
    """ """

    enabled_types = List(
        title=_("enabled_types_label", default="Enabled portal types"),
        description=_(
            "enabled_types_help",
            default="Select a list of portal types that will have Immersive Reader link enabled.",
        ),
        required=False,
        default=[],
        missing_value=[],
        value_type=Choice(vocabulary="plone.app.vocabularies.PortalTypes"),
    )


class IImmersiveReaderControlpanel(IControlpanel):
    """ """
