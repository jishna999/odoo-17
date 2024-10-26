# -*- coding: utf-8 -*-
{
    'name': "order_history",
    'summary': "Manage sale order history and configuration",
    'description': """
        This module provides configuration options for managing sale order history,
        including options for displaying the last number of orders, stages, and reordering.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'sale_management'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'wizard/sale_setting.xml',
        'views/sale_order_history.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'order_history/static/css/setting.css',
            'order_history/static/css/order_history.css',
        ],
    },
    'demo': [
        'demo/demo.xml',
    ],
}
