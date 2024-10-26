{
    'name': 'add_product',
    'version': '1.0',
    'license': 'LGPL-3',
    'summary': 'Extend product and sale.order models with brand information.',
    'depends': ['base', 'sale_management', 'product'],  
    'data': [

                'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
