from plone.app.testing import (
    setRoles,
    SITE_OWNER_NAME,
    SITE_OWNER_PASSWORD,
    TEST_USER_ID,
)
from plone.restapi.testing import RelativeSession
from rer.immersivereader.testing import RESTAPI_TESTING

import unittest


class ImmersiveReaderControlpanelTest(unittest.TestCase):
    layer = RESTAPI_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        self.controlpanel_url = "/@controlpanels/immersive-reader-settings"

        self.api_session = RelativeSession(self.portal_url)
        self.api_session.headers.update({"Accept": "application/json"})
        self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def tearDown(self):
        self.api_session.close()

    def test_controlpanel_exists(self):
        response = self.api_session.get(self.controlpanel_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Content-Type"), "application/json")

    def test_controlpanel_listed(self):
        response = self.api_session.get("/@controlpanels")

        titles = [x.get("title") for x in response.json()]
        self.assertIn("Immersive Reader Settings", titles)
