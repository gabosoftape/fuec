from odoo import models, fields


class wialon_pseudouser(models.Model):
    _inherit = 'gpscontrol.wialon_pseudouser'

    firma = fields.Binary('Firma')
    logo = fields.Binary('Logo')
    razonsocial = fields.Char("Razon social")
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
            ('NT', 'NIT'),
            ('MS', 'MENOR SIN IDENTIFICAR'),
        ],
        required=False,
        help=u'Identificacion del Cliente',
    )
    id_document = fields.Integer(string='No. Documento', default=None)
    celular = fields.Char("Celular")
    email = fields.Char("Email")
    website = fields.Char("Sitio Web")
    direccion = fields.Char('Direccion')
    fuec_code_hab = fields.Char("Codigo de habilitacion temporal")
    fuec_resolucion = fields.Char("No. de resolucion")
    fuec_fecha_hab = fields.Date("Fecha de habilitacion")