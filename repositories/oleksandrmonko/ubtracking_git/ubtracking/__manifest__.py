{
    'name': 'Utility Bills Tracking',
    'summary': 'Utility Bills Tracking)',
    'author': 'Oleksandr Monko',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.0.0',

    'depends': [
        'base',
        'web',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/ubtracking_groups.xml',
        'security/ir.model.access.csv',
        'security/ubtracking_security.xml',
        'views/ubtracking_menu.xml',
        'views/ubtracking_apartment_administrator_views.xml',
        'views/ubtracking_apartment_user_views.xml',
        'views/ubtracking_apartment_views.xml',
        'views/ubtracking_bill_views.xml',
        'views/ubtracking_payment_views.xml',
        'report/ubtracking_apartment_report.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],
    'demo': [
        'demo/ubtracking_apartment_administrator_demo.xml',
        'demo/ubtracking_apartment_user_demo.xml',
        'demo/ubtracking_apartment_demo.xml',
        'demo/ubtracking_bill_demo.xml',
        'demo/ubtracking_payment_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'i18n': True,
}
