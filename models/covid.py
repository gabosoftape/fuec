import time
from odoo import models, fields, api


class enlistCovid(models.Model):
     _name = 'gpscontrol.covid'
     _description = 'Encuesta de salud y prevencion covid19'
     _rec_name = 'conductor'

     state = fields.Selection(
          [('borrador', 'Borrador'), ('done', 'Terminado'), ('peligroso','Peligro')], 'Estado', default='borrador')
     conductor = fields.Many2one('gpscontrol.wialon_driver', string='Conductor')
     garganta = fields.Boolean(string="Dolor de garganta")
     temperatura = fields.Char(string="Temperatura corporal")
     congestion = fields.Boolean(string="Congestion")
     tos = fields.Boolean(string="Tos")
     respiracion = fields.Boolean(string="Respiracion")
     fatiga = fields.Boolean(string="Fatiga")
     escalofrio = fields.Boolean(string="Escalosfrios")
     musculos = fields.Boolean(string="Dolor de musculos")
     fecha = fields.Datetime('Fecha y Hora', default=lambda *a: fields.Datetime.now())
