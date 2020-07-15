# -*- coding: utf-8 -*-

{
    'name': 'Khipu Payment Acquirer',
    'category': 'Payment / Chile',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Chilean Khipu Acquirer',
    'website': 'https://globalresponse.cl',
    'version': "1.6.0",
    'description': """Chilean Khipu Payment Acquirer""",
    'depends': [
            'payment',
            'payment_currency',
    ],
    'external_dependencies': {
            'python': [
                'pykhipu',
                'urllib3',
            ],
    },
    'data': [
        'views/khipu.xml',
        'views/payment_acquirer.xml',
        #'views/payment_transaction.xml',
        'data/khipu.xml',
    ],
    'installable': True,
    'application': True,
}
