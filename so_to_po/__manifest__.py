# -*- coding: utf-8 -*-
{
    'name': "sale_order_to_purchase_order",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
 From sale module creating purchase order 
    """,

    'author': "Amzsys private limited",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly

    'depends': ['base', 'sale_purchase', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_wizard_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
