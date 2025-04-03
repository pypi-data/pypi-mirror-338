from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing.zope import WSGI_SERVER_FIXTURE

import plone.restapi
import rer.immersivereader


class TestLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=rer.immersivereader)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "rer.immersivereader:default")


FIXTURE = TestLayer()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="ImmersiveReaderRestApiLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name="ImmersiveReaderRestApiLayer:FunctionalTesting",
)

RESTAPI_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="ImmersiveReaderRestApiLayer:RestAPITesting",
)
