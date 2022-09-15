# -*- coding: utf-8 -*-
{
    'name': "Website Product Backend",

    'summary': """
        Adds a new menu at website module 
        under the reporting menu 
        which shows all the wishlist products of the customers""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '16.0.1.0.0',
    'depends': ['website_sale_wishlist'],

    'data': [
        'views/website_product_wishlist_views.xml',
    ],
}
