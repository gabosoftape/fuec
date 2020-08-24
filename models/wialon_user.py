from odoo import models, fields


class wialon_pseudouser(models.Model):
    _inherit = 'gpscontrol.wialon_pseudouser'

    firma = fields.Binary('Firma')
    logo = fields.Binary('Logo')
    razonsocial = fields.Char("Razon social")
    website = fields.Char("Sitio Web")
    nit = fields.Char("NIT")
    fuec_code_hab = fields.Char("Codigo de habilitacion temporal")
    telefono = fields.Char("Telefono")
    fuec_resolucion = fields.Char("No. de resolucion")
    email = fields.Char("Email")
    fuec_fecha_hab = fields.Date("Fecha de habilitacion")
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