from plone.restapi.controlpanels import RegistryConfigletPanel
from rer.immersivereader.interfaces import (
    IImmersiveReaderControlpanel,
    IImmersiveReaderSettings,
    IRerImmersivereaderLayer,
)
from zope.component import adapter
from zope.interface import implementer, Interface


@adapter(Interface, IRerImmersivereaderLayer)
@implementer(IImmersiveReaderControlpanel)
class ImmersiveReaderControlpanel(RegistryConfigletPanel):
    schema = IImmersiveReaderSettings
    configlet_id = "ImmersiveReaderSettings"
    configlet_category_id = "Products"
    schema_prefix = "rer.immersivereader"
