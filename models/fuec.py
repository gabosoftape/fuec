# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class fuec(models.Model):
    _name = 'gpscontrol.fuec'
    _description = 'Formato Único de Extracto del Contrato (FUEC) para transporte especial. GPS Control'
    _rec_name = 'folio'

    folio = fields.Char('Folio', size=128)
    contract_id = fields.Char('Contrato No.')
    state = fields.Selection(
        [('cancelado', 'Cancelado'), ('nuevo', 'Nuevo'), ('creado', 'Completo'), ('incompleto', 'Con novedades')],
        'Estado', default='nuevo')
    # contratista
    contratista = fields.Many2one('gpscontrol.contratista_fuec', string="Contratista")
    # responsable
    responsable = fields.Many2one('gpscontrol.responsable_fuec', string="Responsable")
    # objeto del contrato
    contract_object = fields.Selection([('1', 'Prestación de servicio... usuarios y/o particulares'),
                                        ('2', 'Prestación de servicio .. empleados, funcionarios o contratistas')], string="Objeto de contrato")
    # ruta
    ruta = fields.Many2one('gpscontrol.ruta_fuec', string="Ruta")
    # Descripcion del recorrido
    descripcion = fields.Char("Descripcion del recorrido")
    # convenios
    convenio = fields.Selection([('cv', 'Convenio'), ('cs', 'Consorcio'), ('ut', 'Union temporal')], string="Convenio")
    ut_externa = fields.Char('Ut con: ')
    # fecha inicio
    fecha_ini = fields.Datetime('Fecha Inicio', default=lambda *a: fields.Datetime.now())
    # fecha terminacion
    fecha_end = fields.Datetime('Fecha Finalizacion', default=lambda *a: fields.Datetime.now())
    vehiculo = fields.Many2one('gpscontrol.wialon_unit', 'Vehiculo', required=True)
    user_rel = fields.Many2one('gpscontrol.wialon_pseudouser', string="Usuario Responsable")
    conductores = fields.Many2many('gpscontrol.wialon_driver', string="Conductores")

    @api.model
    def create(self, vals):
        number = self.env['ir.sequence'].next_by_code('gpscontrol.fuec')
        vals['folio'] = str(number)
        result = super(fuec, self).create(vals)
        return result

    def _get_report_base_filename(self):
        self.ensure_one()
        return '%s' % self.folio
