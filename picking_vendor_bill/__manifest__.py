# -*- coding: utf-8 -*-
{
    'name': "picking_vendor_bill",

    'summary': "vendor bill From Purchase delivery",

    'description': """
    Created vendor bill after the transfer has created in purchase
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','stock','account'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'wizard/vendor_bill_register_payment.xml',
        'views/stock_picking_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

