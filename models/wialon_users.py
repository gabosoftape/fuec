from odoo import models, fields

class wialon_user(models.Model):
    _inherit = 'res.users'

    id_wialon = fields.Char(string="ID wialon")


class wialon_pseudouser(models.Model):
    _name = 'gpscontrol.wialon_pseudouser'
    _description = 'Data Usuarios get wialon'

    name = fields.Char(string="Nombre")
    id_wia = fields.Char(string="ID Wialon")
    emails = fields.Text(string="Emails Brute")
    uacl = fields.Text(string="Nivel de acceso")
    cls = fields.Text(string="Superclase Usuario")
    crt = fields.Text(string="Creator wialon User")
    bact = fields.Text(string="Id de cuenta")

    def create(self, vals):
        result = super(wialon_pseudouser, self).create(vals)
        return result


