from django.test import TestCase
from django.urls import reverse
from rango.Top_Categories_Stub import TopCats


# Create your tests here.
def Test_Top_Category_Index(self):
    cats = TopCats()
    answer = self.client.get(reverse('rango:index'))
    self.assertEqual(answer.status_code, 100)
    list_cats = cats.getTopCategories()

    for category in list_cats:
        self.assertContains(answer, category.name)