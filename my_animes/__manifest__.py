# -*- coding: utf-8 -*-
{
    'name': "my_animes",
    'summary': "Module de gestion de mes animés",
    'description': """
        Liste des animés, 
        Opening+ending,
        Ma note personelle,
        Suivi des animés regardé + backlog
    """,
    'author': "David 'Weeb' Foot" ,
    'website': "https://www.nautiljon.com/",
    'category': 'Uncategorized',
    'version': '0.0.1',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/views_genre.xml',
        'views/views_theme.xml',
        'views/views_season.xml',
    ],
}

