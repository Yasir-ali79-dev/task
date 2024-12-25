{
    'name': 'Product Discount Feature',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Add product discounts to Odoo eCommerce',
    'description': '''
        This module allows setting a percentage discount on products,
        displays discounted prices on eCommerce, and ensures discounts 
        are applied in the cart and checkout.
    ''',
    'author': 'Shah Zeb',
    'depends': ['website_sale', 'product'],
    'data': [
        'views/product_template_views.xml',
        'views/website_sale_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
