import base64

import qrcode

from odoo import models, fields, api, _
from io import BytesIO


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
        user = self.env['res.users'].search(['id', '=', user_id.id])
        pseudouser = self.env['gpscontrol.wialon_pseudouser'].sudo().search(
            [('user_id', '=', user.id)])
        array_conductores = []
        array_responsables = []
        my_fuec = fuec
        folio = my_fuec.folio
        contract_id = my_fuec.contract_id
        razonsocial = pseudouser.razonsocial
        direccion = pseudouser.direccion
        telefono = pseudouser.celular
        email = pseudouser.email
        id_type = pseudouser.id_type
        id_document = pseudouser.id_document
        contratista = my_fuec.contratista
        ruta = my_fuec.ruta
        convenio = my_fuec.convenio
        ut_con = my_fuec.ut_externa
        inicio_contrato = my_fuec.fecha_ini
        fin_contrato = my_fuec.fecha_end
        vehi_placa = my_fuec.vehiculo.registration_plate
        vehi_modelo = my_fuec.vehiculo.year
        vehi_marca = my_fuec.vehiculo.brand
        vehi_clase = my_fuec.vehiculo.model
        vehi_interno = my_fuec.vehiculo.vin
        vehi_operacion = my_fuec.vehiculo.noperacion
        date_operacion = my_fuec.vehiculo.voperacion
        logo = pseudouser.logo
        for responsible in my_fuec.responsables:
            array_responsables.append(responsible.id)
        # get data of responsables
        responses = self.env['gpscontrol.responsable_fuec'].sudo().search([('id', 'in', array_responsables
                                                                               )])
        for conductor in my_fuec.conductores:
            array_conductores.append([conductor.name, conductor.cedula,
                                      conductor.licencia, conductor.vencimiento])
        pdf_link = 'https://monitoringinnovation.com/fuec/my/{}?report_type=pdf'.format(fuec.id)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(pdf_link)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        firma = pseudouser.firma
        data = {
            'report_type': 'pdf',
            'folio': folio,
            'logo': logo,
            'razonsocial': razonsocial,
            'direccion': direccion,
            'telefono': telefono,
            'email': email,
            'contract_id': contract_id,
            'id_type': id_type,
            'id_document': id_document,
            'contratista_empresa': contratista.empresa,
            'contratista_nombre': contratista.nombre,
            'contratista_nit': contratista.nit,
            'responsibly': responses,
            'ruta_nombre': ruta.nombre,
            'ruta_det': ruta.detalle,
            'convenio': convenio,
            'ut_con': ut_con,
            'inicio_contrato': inicio_contrato,
            'fin_contrato': fin_contrato,
            'vehi_placa': vehi_placa,
            'vehi_modelo': vehi_modelo,
            'vehi_marca': vehi_marca,
            'vehi_clase': vehi_clase,
            'vehi_interno': vehi_interno,
            'vehi_operacion': vehi_operacion,
            'conductores': array_conductores,
            'qr': qr_image,
            'pseudouser': pseudouser,
            'firma': firma,
            'contract_object': my_fuec.contract_object,
        }
        #Datos
        #print(data)
        return self.env.ref('fuec.report_fuec_pdf').report_action(self, data=data)
