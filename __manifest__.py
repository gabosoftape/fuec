# -*- coding: utf-8 -*-
{
    'name': "alistamientos",

    'summary': """
        Una aplicacion de gps control para alistamiento de vehiculos""",

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

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/enlist_security.xml',
        # 'views/templates.xml',
        'views/views.xml',
        'views/config.xml',

    ],
    # only loaded in demonstration mode

}
