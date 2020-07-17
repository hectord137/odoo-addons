# -*- coding: utf-8 -*-
{
    'name': "Payment Acquirer Currencies",

    'summary': """Payment Acquirer: Allowed Currencies or Force convert to Currency""",

    'description': """Payment Acquirer Currencies or Force convert to Currency""",

    'author': "Hector Daniel",
    'website': "https://www.herobotic.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website / Sale / Payment',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

    # always loaded
    'data': [
        'views/payment_acquirer.xml',
    ],
}