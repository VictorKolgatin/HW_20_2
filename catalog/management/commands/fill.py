from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.truncate()
        Product.truncate()

        categories_list = [
            {'pk': 1, 'name': 'рыба', 'overview': 'Бывает морская, бывает речная, а бывает сушеная'},
            {'pk': 2, 'name': 'птица', 'overview': 'Всегда вкусно'},
            {'pk': 3, 'name': 'Мясо', 'overview': 'Идеально к майским праздникам'},
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        products_list = [
            {"name": "Осетр",
             "overview": "Что то на богатом",
             "image": "",
             "category": categories_for_create[0],
             "purchase_price": 20000},
            {"name": "Курица",
             "overview": "Курица не птица",
             "image": "",
             "category": categories_for_create[1],
             "purchase_price": 500
             },
            {"name": "Свинина",
             "overview": "Хорошо подходит для шашлыка",
             "image": "",
             "category": categories_for_create[2],
             "purchase_price": 600
             },
        ]
        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)