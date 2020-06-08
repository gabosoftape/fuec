# -*- coding: utf-8 -*-
# from odoo import http


# class Alistamientos(http.Controller):
#     @http.route('/alistamientos/alistamientos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alistamientos/alistamientos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alistamientos.listing', {
#             'root': '/alistamientos/alistamientos',
#             'objects': http.request.env['alistamientos.alistamientos'].search([]),
#         })

#     @http.route('/alistamientos/alistamientos/objects/<model("alistamientos.alistamientos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alistamientos.object', {
#             'object': obj
#         })

from wialon import Wialon, WialonError

try:
    wialon_api = Wialon()
    # old username and password login is deprecated, use token login
    result = wialon_api.token_login(token='53c45668de3e5399eb7af78a889bd45a4D9DD25ED3B4DDDC261DB138027093247B183718')
    wialon_api.sid = result['eid']

    result = wialon_api.avl_evts()

    wialon_api.core_logout()
except WialonError as e:
    pass
