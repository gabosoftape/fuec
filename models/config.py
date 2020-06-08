# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class enlistNotifications(models.Model):
     _name = 'gpscontrol.notificaciones'
     _description = 'Config Notificaciones Alistamientos GPS Control'
     _rec_name = 'user'
     _sql_constraints = [
         ('user_uniq', 'UNIQUE (user)', '¡No puedes tener dos NAME_FIELD con el mismo nombre!')
     ]

     user = fields.Char('Usuario', size=128, required=True)
     state = fields.Selection(
          [('desactivado', 'Desactivado'), ('activo', 'Activado')], 'Estado', default='nuevo')
     vehiculo = fields.Many2many('gpscontrol.wialon_unit', string='Vehiculos',  required=True)
     conductores = fields.Many2many('gpscontrol.wialon_driver', string='Conductores', required=True)
     email1 = fields.Char(string="email 1 ", required=True)
     email2 = fields.Char(string="email 2 ")
     email3 = fields.Char(string="email 3 ")
     mensaje = fields.Text(string="Mensaje de notificacion")




