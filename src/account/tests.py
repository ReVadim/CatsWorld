from django.test import TestCase


class HomePageTest(TestCase):
    """ Homepage testing
    """
    def test_home_page_returns_correct_html(self):
        """ test: homepage returns right html
        """
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Главная</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'account/index.html')
