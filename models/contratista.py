# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class contratistaFuec(models.Model):
     _name = 'gpscontrol.contratista_fuec'
     _rec_name = 'nombre'

     empresa = fields.Char('Empresa')
     nit = fields.Char('Nit')
     id_type = fields.Selection(
          string=u'Tipo de Documento',
          selection=[
               ('CC', 'CEDULA DE CIUDADANÍA'),
               ('CE', 'CEDULA DE EXTRANJERÍA'),
               ('PA', 'PASAPORTE'),
               ('SC', 'SALVO CONDUCTO'),
               ('RC', 'REGISTRO CIVIL '),
               ('PE', 'PERMISO ESPECIAL DE PERMANENCIA'),
               ('TI', 'TARJETA DE IDENTIDAD'),
               ('AS', 'ADULTO SIN IDENTIFICAR'),
               ('MS', 'MENOR SIN IDENTIFICAR'),
          ],
          required=False,
          help=u'Identificacion del Cliente',
     )
     id_document = fields.Integer(string='No. Documento', default=None)
     nombre = fields.Char('Nombre de contacto')
     email = fields.Char("Email")
     telefono = fields.Char("Telefono")
     celular = fields.Char("Celular")
     direccion = fields.Char("Direccion")
     ciudad = fields.Char("Ciudad")


class responsableFuec(models.Model):
     _name = 'gpscontrol.responsable_fuec'
     _rec_name = 'nombre'

     id_type = fields.Selection(
          string=u'Tipo de Documento',
          selection=[
               ('CC', 'CEDULA DE CIUDADANÍA'),
               ('CE', 'CEDULA DE EXTRANJERÍA'),
               ('PA', 'PASAPORTE'),
               ('SC', 'SALVO CONDUCTO'),
               ('RC', 'REGISTRO CIVIL '),
               ('PE', 'PERMISO ESPECIAL DE PERMANENCIA'),
               ('TI', 'TARJETA DE IDENTIDAD'),
               ('AS', 'ADULTO SIN IDENTIFICAR'),
               ('MS', 'MENOR SIN IDENTIFICAR'),
          ],
          required=False,
          help=u'Identificacion del Cliente',
     )
     id_document = fields.Integer(string='No. Documento', default=None)
     nombre = fields.Char('Nombre de contacto')
     email = fields.Char("Email")
     telefono = fields.Char("Telefono")
     celular = fields.Char("Celular")
     direccion = fields.Char("Direccion")
     ciudad = fields.Char("Ciudad")

class rutaFuec(models.Model):
     _name = 'gpscontrol.ruta_fuec'
     _rec_name = 'nombre'

     nombre = fields.Char('Ruta')
     detalle = fields.Text('Detalle')




