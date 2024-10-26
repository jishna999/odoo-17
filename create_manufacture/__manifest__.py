# -*- coding: utf-8 -*-
{
    'name': "create_manufacture_order_from_bom",

    'summary': "creating a new manufacture order from Bil of material",

    'description': """
From Manufacture module new production order for a perticular bill of Material is created
    """,

    'author': "Amzsys Private limited",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/manufacture_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
