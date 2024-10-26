# -*- coding: utf-8 -*-
{
    'name': "suggested_product",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'sale_management', 'stock', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_template.xml',
        'views/account_move_template.xml',
        'views/templates.xml',
        'report/sale_order_preview.xml',
        'report/sale_report.xml',
        'report/invoice_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
