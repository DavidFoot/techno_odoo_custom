# -*- coding: utf-8 -*-
{
    'name': "my_library",
    'sequence': -100,
    'summary': "Coucou la short description",

    'description': """
Je fais des choses, Description Longue...
    """,

    'author': "Techo Foot David V3",
    'website': "https://www.technocite.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','mail'],
    'data': [
        'views/library_book_views.xml',
        'views/library_book_tag_views.xml',
        'views/library_book_category_views.xml',
        'views/library_loan_views.xml',
        'views/library_member_views.xml',
        'security/ir.model.access.csv',
        'data/cron_library_loan.xml',
    ],
}

