# -*- coding: utf-8 -*-
# from plone.z3cform import layout
from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from rer.immersivereader import _
from rer.immersivereader.interfaces import IImmersiveReaderSettings


class SettingsEditForm(RegistryEditForm):
    """Define form logic"""

    schema = IImmersiveReaderSettings
    schema_prefix = "rer.immersivereader"
    label = _("Immersive Reader Settings")


class SettingsView(ControlPanelFormWrapper):
    """Control Panel form wrapper"""

    form = SettingsEditForm
