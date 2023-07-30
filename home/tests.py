from django.test import (
    TestCase,
    RequestFactory
)
from home import views

# Create your tests here.

class HomeTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_health_check_api(self):
        request = self.factory.get("/health_details/")
        response = views.HealthCheckView.as_view()(request)
        self.assertEqual(response.status_code, 200)