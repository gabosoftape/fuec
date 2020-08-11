# -*- coding: utf-8 -*-
{
    'name': "Fuec",

    'summary': """
        Una aplicacion de gps control para formatos unicos de extracto de contrato""",

    'description': """
        ...
    """,

    'author': "Gabriel Pabon",
    'website': "http://www.gpscontrol.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'fleet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'alistamientos',
    ],
    # always loaded
    'data': [
        'security/fuec_security.xml',
        'report/fuec_report_pdf_view.xml',
        'views/fuec_report.xml',
        'views/user.xml',
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'sequence': 2,
    'price': 300,
    'currency': 'EUR',

}
