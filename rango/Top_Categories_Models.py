from rango.Top_Categories import Top_Categories


class Top_Categories_Models(Top_Categories):

    def __init__(self, categories):
        self.categories = categories

    def getTopCategories(self):
        return self.categories.objects.order_by('-likes')[:5]