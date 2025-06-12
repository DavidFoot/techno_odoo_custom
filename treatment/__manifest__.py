# -*- coding: utf-8 -*-
{
    'name': "Treatment",
    'summary': "Oxygen Treatment/Delivery Management Module",
    'description': """
        Oxygen Treatment/Delivery Management Module
    """,
    'author': "David F" ,
    'website': "https://github.com/DavidFoot/",
    'category': 'Uncategorized',
    'version': '18.0.0.1',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/treatment_view.xml',
        'views/therapy_view.xml',
        'views/patient_view.xml',
    ],
    'license': 'LGPL-3',
}

