import qrcode

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
        user_id = fuec.create_uid
        pseudouser = self.env['gpscontrol.wialon_pseudouser'].search(
            [('user_id', '=', user_id.id)])
        folio = fuec.folio
        contract_id = fuec.contract_id
        razonsocial = pseudouser.razonsocial
        id_type = pseudouser.id_type
        id_document = pseudouser.id_document
        contratista = fuec.contratista
        responsable = fuec.responsable
        ruta = fuec.ruta
        descripcion_recorrido = fuec.descripcion
        convenio = fuec.convenio
        ut_con = fuec.ut_externa
        inicio_contrato = fuec.fecha_ini
        fin_contrato = fuec.fecha_end
        vehiculo = fuec.vehiculo
        conductores = fuec.conductores
        qr = qrcode.make("Hola desde Recursos Python!")
        firma = pseudouser.firma
        data = {
            'report_type': 'pdf',
            'folio': folio,
            'fuec': fuec,
            'razonsocial': razonsocial,
            'contract_id': contract_id,
            'id_type': id_type,
            'id_document': id_document,
            'contratista': contratista,
            'responsable': responsable,
            'ruta': ruta,
            'descripcion_recorrido': descripcion_recorrido,
            'convenio': convenio,
            'ut_con': ut_con,
            'inicio_contrato': inicio_contrato,
            'fin_contrato': fin_contrato,
            'vehiculo': vehiculo,
            'conductores': conductores,
            'qr': qr,
            'pseudouser': pseudouser,
            'firma': firma,
            'contract_object': fuec.contract_object,
        }
        #Datos
        print(data)
        return self.env.ref('fuec.report_fuec_pdf').report_action(self, data=data)
