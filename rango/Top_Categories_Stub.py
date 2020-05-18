from rango.Top_Categories import Top_Categories
from rango.models import Category


def Add_Cat(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    category.save()


class TopCats(Top_Categories):

    def __init__(self):
        Add_Cat('Test1', 1, 1)
        Add_Cat('Test2', 1, 1)
        Add_Cat('Test3', 1, 1)
        Add_Cat('Test4', 1, 1)
        Add_Cat('Test5', 1, 1)

    def getTopCategories(self):
        return Category.objects.order_by('-likes')[:5]