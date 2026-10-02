from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1> Company Homepage </h1>")

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Company About Page</h1>")
 




class ProductsPageTests(TestCase):

    def test_products_page_status_code(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_products_page_template(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "products.html")

    def test_products_context_contains_products(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertIn("products", response.context)

        products = response.context["products"]

        self.assertIsInstance(products, list)

        self.assertEqual(len(products), 4)

        for product in products:
            self.assertIn("name", product)
            self.assertIn("price", product)

# Create your tests here.
