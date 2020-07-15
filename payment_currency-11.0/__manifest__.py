# -*- coding: utf-8 -*-

{
    'name': 'Payment Acquirer Currencies',
    'category': 'Website / Sale / Payment',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Allowed Currencies or Force convert to Currency',
    'website': 'https://globalresponse.cl',
    'version': "3.0.0",
    'description': """Payment Acquirer Currencies or Force convert to Currency""",
    'depends': [
                'payment',
            ],
    'external_dependencies': {
            'python': [],
    },
    'data': [
        'views/payment_acquirer.xml',
    ],
    'installable': True,
    'application': True,
}
