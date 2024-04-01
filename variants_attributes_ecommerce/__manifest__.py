{
    "name": "Variants' attributes e-commerce",
    "summary": """On website, display variants' specific attributes""",
    'version': '17.0.1.0.0',
    "depends": [
        "sale",
        "website_sale_product_configurator",
    ], #Check depends correctly
    "data": [
        "views/templates.xml",
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            'variants_attributes_ecommerce/static/src/js/variant_mixin.js',
        ],
    },
    'application': False,
    'auto_install': True,
    'license': 'OPL-1',
    "author": "Minijump",
    "category": "website",
    "description": """On website, display variants' specific attributes""",
    'price': '7.95',
    #'images': ['./static/description/banner.png'],
    'support': 'ecuyer.duchevalier@gmail.com'
}
