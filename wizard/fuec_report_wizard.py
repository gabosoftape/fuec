from odoo import models, fields, api, _


class FuecReportButton(models.TransientModel):
    _name = 'wizard.fuec_report'

    fuec_select = fields.Many2one('gpscontrol.fuec', string="Formato")

    def print_fuec_report_pdf(self, folio_id=None):
        fuec = None
        if folio_id:
            fuec = self.env['gpscontrol.fuec'].search([('folio', '=', folio_id)])
        else:
            folio = self.fuec_select.folio
            fuec = self.env['gpscontrol.fuec'].search([('folio', '=', folio)])

        data = {
            'folio': folio,
            'fuec': fuec,
        }
        #Datos
        print(data)
        return self.env.ref('fuec.report_fuec_pdf').report_action(self, data=data)
