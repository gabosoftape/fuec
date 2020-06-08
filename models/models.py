# -*- coding: utf-8 -*- #
import time
from odoo import models, fields, api


class alistamientos(models.Model):
     _name = 'gpscontrol.alistamientos'
     _description = 'Alistamientos GPS Control'
     _rec_name = 'folio'

     folio = fields.Char('Folio', size=128)
     state = fields.Selection(
          [('cancelado', 'Cancelado'), ('nuevo', 'Nuevo'), ('creado', 'Completo'), ('incompleto', 'Con novedades')], 'Estado', default='nuevo')
     vehiculo = fields.Many2one('gpscontrol.wialon_unit', 'Vehiculo',  required=True)
     fecha = fields.Datetime('Fecha y Hora', default=lambda *a: fields.Datetime.now())
     documentos_conductor = fields.Boolean(string="Documentos Conductor (Cédula, Licencia Conducción, Carné empresa)")
     documentos_vehiculo = fields.Boolean(string="Documentos del Vehiculo")
     calcomania = fields.Boolean(string="Calcomania Como Conduzco")
     pito = fields.Boolean(string="Pito")
     disp_velocidad = fields.Boolean(string="Dispositivo de velocidad")
     estado_esc_p_conductor = fields.Boolean(string="Estado de escalera puerta de conductor")
     estado_esc_p_pasajero = fields.Boolean(string="Estado escalera puerta de pasajero")
     equipo_carretera = fields.Boolean(string="Equipo de Carretera (Gato, Llave de pernos, 2 señales carretera,   2 Tacos)")
     herramientas = fields.Boolean(string="Herramientas en buen estado")
     linterna = fields.Boolean(string="Linterna")
     extintor = fields.Boolean(string="Extintor (vigente, pasador, manometro, corrosión)")
     botiquin = fields.Boolean(string="Botiquin")
     repuesto = fields.Boolean(string="Llanta de repuesto")
     retrovisores = fields.Boolean(string="Espejos retrovisores (3)")
     cinturones = fields.Boolean(string="Cinturon de seguridad conductor y pasajeros")
     motor = fields.Boolean(string="Motor: No existen fugas")
     llantas = fields.Boolean(string="Estado de llantas (desgaste, presion de aire)")
     baterias = fields.Boolean(string="Baterias: Niveles de Agua, Ajustes de Bornes, Sulfatacion")
     transmision = fields.Boolean(string="Revisar: Transmision, Direccion")
     tension = fields.Boolean(string="Tension de correas")
     tapas = fields.Boolean(string="Tapas: de Radiador, de Combustible, de Hidraulico")
     niveles = fields.Boolean(string="Niveles de: Agua radiador, Aceite Hidraulico, Aceite de")
     filtros = fields.Boolean(string="Revision de filtros")
     parabrisas = fields.Boolean(string="Estado limpiaprabrisas y nivel de agua")
     frenos = fields.Boolean(string="Sistema de Frenos")
     frenos_emergencia = fields.Boolean(string="Frenos de emergancia")
     aire = fields.Boolean(string="Estado Aire Acondicionado")
     luces = fields.Boolean(string="Luces (altas, medias, bajas, direccionales, estacionarias y reversa)")
     silleteria = fields.Boolean(string="Estado silleteria")
     silla_conductor = fields.Boolean(string="Estado y alineación asiento conductor")
     aseo = fields.Boolean(string="Aseo interno y externo")
     celular = fields.Boolean(string="Avantel o Celular con Minutos")
     ruteros = fields.Boolean(string="Ruteros")
     #descripciones
     desc_documentos_conductor = fields.Text(string="Descripcion")
     desc_documentos_vehiculo = fields.Text(string="Descripcion")
     desc_calcomania = fields.Text(string="Descripcion")
     desc_pito = fields.Text(string="Descripcion")
     desc_disp_velocidad = fields.Text(string="Descripcion")
     desc_estado_esc_p_conductor = fields.Text(string="Descripcion")
     desc_estado_esc_p_pasajero = fields.Text(string="Descripcion")
     desc_equipo_carretera = fields.Text(string="Descripcion")
     desc_herramientas = fields.Text(string="Descripcion")
     desc_linterna = fields.Text(string="Descripcion")
     desc_extintor = fields.Text(string="Descripcion")
     desc_botiquin = fields.Text(string="Descripcion")
     desc_repuesto = fields.Text(string="Descripcion")
     desc_retrovisores = fields.Text(string="Descripcion")
     desc_cinturones = fields.Text(string="Descripcion")
     desc_motor = fields.Text(string="Descripcion")
     desc_llantas = fields.Text(string="Descripcion")
     desc_baterias = fields.Text(string="Descripcion")
     desc_transmision = fields.Text(string="Descripcion")
     desc_tension = fields.Text(string="Descripcion")
     desc_tapas = fields.Text(string="Descripcion")
     desc_niveles = fields.Text(string="Descripcion")
     desc_filtros = fields.Text(string="Descripcion")
     desc_parabrisas = fields.Text(string="Descripcion")
     desc_frenos = fields.Text(string="Descripcion")
     desc_frenos_emergencia = fields.Text(string="Descripcion")
     desc_aire = fields.Text(string="Descripcion")
     desc_luces = fields.Text(string="Descripcion")
     desc_silleteria = fields.Text(string="Descripcion")
     desc_silla_conductor = fields.Text(string="Descripcion")
     desc_aseo = fields.Text(string="Descripcion")
     desc_celular = fields.Text(string="Descripcion")
     desc_ruteros = fields.Text(string="Descripcion")
     #images
     img_documentos_conductor = fields.Binary(string="Imagen")
     img_documentos_vehiculo = fields.Binary(string="Imagen")
     img_calcomania = fields.Binary(string="Imagen")
     img_pito = fields.Binary(string="Imagen")
     img_disp_velocidad = fields.Binary(string="Imagen")
     img_estado_esc_p_conductor = fields.Binary(string="Imagen")
     img_estado_esc_p_pasajero = fields.Binary(string="Imagen")
     img_equipo_carretera = fields.Binary(
         string="Imagen")
     img_herramientas = fields.Binary(string="Imagen")
     img_linterna = fields.Binary(string="Imagen")
     img_extintor = fields.Binary(string="Imagen")
     img_botiquin = fields.Binary(string="Imagen")
     img_repuesto = fields.Binary(string="Imagen")
     img_retrovisores = fields.Binary(string="Imagen")
     img_cinturones = fields.Binary(string="Imagen")
     img_motor = fields.Binary(string="Imagen")
     img_llantas = fields.Binary(string="Imagen")
     img_baterias = fields.Binary(string="Imagen")
     img_transmision = fields.Binary(string="Imagen")
     img_tension = fields.Binary(string="Imagen")
     img_tapas = fields.Binary(string="Imagen")
     img_niveles = fields.Binary(string="Imagen")
     img_filtros = fields.Binary(string="Imagen")
     img_parabrisas = fields.Binary(string="Imagen")
     img_frenos = fields.Binary(string="Imagen")
     img_frenos_emergencia = fields.Binary(string="Imagen")
     img_aire = fields.Binary(string="Imagen")
     img_luces = fields.Binary(string="Imagen")
     img_silleteria = fields.Binary(string="Imagen")
     img_silla_conductor = fields.Binary(string="Imagen")
     img_aseo = fields.Binary(string="Imagen")
     img_celular = fields.Binary(string="Imagen")
     img_ruteros = fields.Binary(string="Imagen")
     partner_id = fields.Many2one('gpscontrol.wialon_driver', 'Conductor', required=True)

     @api.model
     def create(self, vals):
          flag = False
          number = self.env['ir.sequence'].next_by_code('gpscontrol.alistamientos')
          vals['folio'] = str(number)
          if vals['documentos_conductor'] == False:
               flag = True
          if vals['documentos_vehiculo']==False:
               flag = True
          if vals['calcomania']==False:
               flag = True
          if vals['pito']==False:
               flag = True
          if vals['disp_velocidad']==False:
               flag = True
          if vals['estado_esc_p_conductor'] ==False:
               flag = True
          if vals['estado_esc_p_pasajero']==False:
               flag = True
          if vals['equipo_carretera'] ==False :
               flag = True
          if vals['herramientas']==False:
               flag = True
          if vals['linterna']==False:
               flag = True
          if vals['extintor']==False:
               flag = True
          if vals['botiquin']==False:
               flag = True
          if vals['repuesto']==False:
               flag = True
          if vals['retrovisores'] ==False:
               flag = True
          if vals['cinturones']==False:
               flag = True
          if vals['motor']==False:
               flag = True
          if vals['llantas'] ==False:
               flag = True
          if vals['baterias']==False:
               flag = True
          if vals['transmision']==False:
               flag = True
          if vals['tension']==False:
               flag = True
          if vals['tapas']==False:
               flag = True
          if vals['niveles']==False:
               flag = True
          if vals['filtros']==False:
               flag = True
          if vals['parabrisas']==False:
               flag = True
          if vals['frenos']==False:
               flag = True
          if vals['frenos_emergencia']==False:
               flag = True
          if vals['aire']==False:
               flag = True
          if vals['luces']==False:
               flag = True
          if vals['silleteria']==False:
               flag = True
          if vals['silla_conductor']==False:
               flag = True
          if vals['aseo']==False:
               flag = True
          if vals['celular']==False:
               flag = True
          if vals['ruteros']==False:
               flag = True
          #aqui valido si flag es true
          if flag == True:
               vals['state'] = 'incompleto'
          elif flag == False:
               vals['state'] = 'creado'

          result = super(alistamientos, self).create(vals)
          return result

