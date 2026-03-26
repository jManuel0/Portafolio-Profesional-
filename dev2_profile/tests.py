from django.test import TestCase


class PortfolioPageTests(TestCase):
    """Basic tests for the Developer 2 portfolio page."""

    def test_portfolio_page_is_available(self):
        response = self.client.get('/dev2/')
        self.assertEqual(response.status_code, 200)
