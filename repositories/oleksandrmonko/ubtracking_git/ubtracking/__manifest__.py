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
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        #'security/hr_hospital_groups.xml',
        'security/ir.model.access.csv',
        #'security/hr_hospital_security.xml',
        'views/ubtracking_menu.xml',
        #'data/hr_hospital_disease_data.xml',
        'views/ubtracking_apartment_administrator_views.xml',
        #'wizard/hr_hospital_set_personal_doctor_wizard_view.xml',
        #'views/hr_hospital_patient_views.xml',
        #'views/hr_hospital_diagnosis_views.xml',
        #'views/hr_hospital_disease_views.xml',
        #'views/hr_hospital_specialty_views.xml',
        #'views/hr_hospital_visit_views.xml',
        #'wizard/hr_hospital_disease_report_wizard_view.xml',
        #'report/hr_hospital_doctor_report.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],
    'demo': [
        #'demo/hr_hospital_specialties_demo.xml',
        #'demo/hr_hospital_doctor_demo.xml',
        #'demo/hr_hospital_patient_demo.xml',
        #'demo/hr_hospital_visits_demo.xml',
        #'demo/hr_hospital_diagnosis_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    #'i18n': True,
}
