# -*- coding: utf-8 -*-
{
    'name': 'e-outlet Product Info Updation',
    'version': '12.0.1',
    'summary': 'update product info and add some new fields',
    'category': 'product',
    'author': 'Magdy,TeleNoc',
    'description': """
    update product info
    """,
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
    ]
}
