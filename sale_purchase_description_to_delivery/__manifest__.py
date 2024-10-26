# -*- coding: utf-8 -*-
{
    'name': "sale_purchase_description_to_delivery",

    'summary': "Sale Order/Purchase Order Line Description to Delivery/Shipment",

    'description': """
Sale order line description and Purchase order line description  are added to delivery slip report and
 picking operation report through group group on User setting have access to Michell Admin
    """,

    'author': "Amzsys private limited",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_purchase_stock',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
         'security/security.xml',
         'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/stock_move.xml',
        'report/delivery_slip.xml',
        'report/picking_operations.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

