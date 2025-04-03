from plone import api
from plone.app.testing import (
    setRoles,
    SITE_OWNER_NAME,
    SITE_OWNER_PASSWORD,
    TEST_USER_ID,
)
from plone.restapi.testing import RelativeSession
from rer.immersivereader.testing import RESTAPI_TESTING
from transaction import commit

import unittest


class TestExpansion(unittest.TestCase):
    layer = RESTAPI_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.api_session = RelativeSession(self.portal_url)
        self.api_session.headers.update({"Accept": "application/json"})
        self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)

        self.page = api.content.create(
            container=self.portal, type="Document", title="A page"
        )
        self.news = api.content.create(
            container=self.portal, type="News Item", title="A news"
        )

        self.page_url = self.page.absolute_url()
        self.news_url = self.news.absolute_url()
        commit()

    def tearDown(self):
        self.api_session.close()

    def test_expansion_visible(self):
        response = self.api_session.get(self.page_url)
        result = response.json()
        self.assertIn("immersive-reader", result["@components"])

    def test_expansion_not_expanded_by_default(self):
        response = self.api_session.get(self.page_url)
        result = response.json()
        self.assertEqual(
            result["@components"]["immersive-reader"],
            {"@id": f"{self.page_url}/@immersive-reader"},
        )
        self.assertNotIn("enabled", result["@components"]["immersive-reader"])

    def test_expansion_expanded_if_passed_parameter(self):
        response = self.api_session.get(f"{self.page_url}?expand=immersive-reader")
        result = response.json()
        data = result["@components"]["immersive-reader"]

        self.assertEqual(
            data, {"@id": f"{self.page_url}/@immersive-reader", "enabled": True}
        )

    def test_is_enabled_if_no_type_set(self):
        response = self.api_session.get(f"{self.page_url}?expand=immersive-reader")
        result = response.json()["@components"]["immersive-reader"]

        self.assertEqual(result["enabled"], True)

        response = self.api_session.get(f"{self.news_url}?expand=immersive-reader")
        result = response.json()["@components"]["immersive-reader"]

        self.assertEqual(result["enabled"], True)

    def test_check_for_enabled_type(self):
        api.portal.set_registry_record(
            "rer.immersivereader.enabled_types", ["Document"]
        )

        commit()

        response = self.api_session.get(f"{self.page_url}?expand=immersive-reader")
        result = response.json()["@components"]["immersive-reader"]

        self.assertEqual(result["enabled"], True)

        response = self.api_session.get(f"{self.news_url}?expand=immersive-reader")
        result = response.json()["@components"]["immersive-reader"]

        self.assertEqual(result["enabled"], False)
