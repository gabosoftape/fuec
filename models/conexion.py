from odoo import models, fields
from wialon import Wialon, WialonError
import datetime
import urllib
import xml.dom.minidom
#import xlwt
#from xlrd import open_workbook
import requests
import json
try:
    from urllib2 import Request, urlopen, HTTPError, URLError
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError

from odoo.fields import Datetime


class sync_wialon(models.Model):
    _name = 'gpscontrol.wialon_conexion'
    _description = 'Conexion con wialon data'

    log = fields.Text(string="Log")
    status = fields.Selection([
        ('failed', 'Se encontro Error'),
        ('testing', 'test'),
        ('ok', 'Completado'),
    ], default='testing')
    date = fields.Datetime(string="Fecha Log", default=Datetime.now())

    def sync_users(self):
        try:
            wialon_api = Wialon()
            # old username and password login is deprecated, use token login
            result = wialon_api.token_login(
                token='53dac8bfe1c32941e9a7b7121196dfe262A6A9DF693E8274C23FD67398B9AFDED9E5FE4F')
            wialon_api.sid = result['eid']
            # wialon_api.core_logout()
            if result:
                self.log = wialon_api.sid
            else:
                self.log = 'Nada .. no se conecta'
            url_usuarios = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={%22spec%22:{%22itemsType%22:%22user%22,%22propName%22:%22sys_name%22,%22propValueMask%22:%22%22,%22sortType%22:%22sys_name%22,%22propType%22:%22accounttree%22},%22force%22:1,%22flags%22:4611686018427387903,%22from%22:0,%22to%22:0}&sid=";
            url_test = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&params={%22id%22:16179438,%22flags%22:4611686018427387903}&sid=";
            r = requests.get(url_usuarios + wialon_api.sid)
            # Users = self.env['res.users']
            PseudoUsers = self.env['gpscontrol.wialon_pseudouser']
            logins = r.json()
            print(wialon_api.sid)
            #print(r.text)
            print("--------Cargando----------")
            self.log = logins
            for item in logins['items']:
                rec_units = self.env['gpscontrol.wialon_unit']
                unit_list = []
                usuario = PseudoUsers.create({
                    'name': item['nm'],
                    'id_wia': item['id'],
                    'emails': '',
                    'uacl': item['uacl'],
                    'cls': item['cls'],
                    'crt': item['crt'],
                    'bact': item['bact'],
                })
                if usuario:
                    print('Se agrego correctamente el usuario' + usuario.name)
                    self.status = 'ok'
                else:
                    print('pailas')
                    self.status = 'failed'
        except WialonError as e:
            pass

    def sync_units(self):
        try:
            wialon_api = Wialon()
            # old username and password login is deprecated, use token login
            result = wialon_api.token_login(
                token='53dac8bfe1c32941e9a7b7121196dfe262A6A9DF693E8274C23FD67398B9AFDED9E5FE4F')
            wialon_api.sid = result['eid']
            # wialon_api.core_logout()
            if result:
                self.log = wialon_api.sid
            else:
                self.log = 'Nada .. no se conecta'
            url = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={%22spec%22:{%22itemsType%22:%22avl_unit%22,%22propName%22:%22trailers%22,%22propValueMask%22:%22%22,%22sortType%22:%22trailers%22,%22propType%22:%22propitemname%22},%22force%22:1,%22flags%22:1,%22from%22:0,%22to%22:0}&sid=";
            sid = wialon_api.sid
            res = requests.get(url + sid)
            # Users = self.env['res.users']
            units = self.env['gpscontrol.wialon_unit'].search([('id_wialon', '!=', None)])
            logins = res.json()
            flag = False
            print(sid)
            print(res.text)
            print("------------------")
            for item in logins['items']:
                # Users.create({'name': name['nm'], 'login': login['nm']})
                print(item['nm'])
                print('nice bro, este vehiculo flag abajo por lo tanto se guardara.')
                try:
                    vehiculo = units.create({
                        'name': item['nm'],
                        'id_wialon': item['id'],
                    })
                    if vehiculo:
                        print('Se agrego correctamente el  ' + vehiculo.name)
                        self.status = 'ok'
                    else:
                        print('pailas')
                        self.status = 'failed'
                except:
                    pass

            self.log = units
        except WialonError as e:
            pass

    def sync_groups(self):
        try:
            wialon_api = Wialon()
            # old username and password login is deprecated, use token login
            result = wialon_api.token_login(
                token='53dac8bfe1c32941e9a7b7121196dfe262A6A9DF693E8274C23FD67398B9AFDED9E5FE4F')
            wialon_api.sid = result['eid']
            # wialon_api.core_logout()
            if result:
                self.log = wialon_api.sid
            else:
                self.log = 'Nada .. no se conecta'
            url = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={%22spec%22:{%22itemsType%22:%22avl_unit_group%22,%22propName%22:%22admin_fields%22,%22propValueMask%22:%22%22,%22sortType%22:%22admin_fields%22,%22propType%22:%22propitemname%22},%22force%22:1,%22flags%22:4611686018427387903,%22from%22:0,%22to%22:0}&sid=";
            sid = wialon_api.sid
            res = requests.get(url + sid)
            # Users = self.env['res.users']
            gropus = self.env['gpscontrol.wialon_unit_group']
            logins = res.json()
            print(sid)
            print(res.text)
            print("------------------")
            for item in logins['items']:
                # Users.create({'name': name['nm'], 'login': login['nm']})
                hijosjson = item['u']
                creator = item['crt']
                rec_hijos = self.env['gpscontrol.wialon_unit']
                rec_users = self.env['gpscontrol.wialon_pseudouser']
                hijos_list = []
                for hijo in hijosjson:
                    child = rec_hijos.search([('id_wialon', '=', hijo)])
                    if child:
                        print('se encontro a ' + child.id_wialon)
                        hijos_list.append(child.id)
                    else:
                        print('no se encontro nada')

                # salimos del for
                user = rec_users.search([('id_wia', '=', creator)])
                grupo = gropus.create({
                    'name': item['nm'],
                    'id_wialon': item['id'],
                    'childs_id': hijos_list,
                    'crt': user.id,
                    'bact': item['bact'],
                })
                if grupo:
                    print('Se agrego correctamente el usuario' + grupo.name)
                    self.status = 'ok'
                    self.log = 'todo ok'
                else:
                    print('pailas')
                    self.log = 'algo salio mal :('
                    self.status = 'failed'
        except WialonError as e:
            pass

    def sync_drivers(self):
        try:
            wialon_api = Wialon()
            # old username and password login is deprecated, use token login
            result = wialon_api.token_login(
                token='53dac8bfe1c32941e9a7b7121196dfe262A6A9DF693E8274C23FD67398B9AFDED9E5FE4F')
            wialon_api.sid = result['eid']
            # wialon_api.core_logout()
            if result:
                self.log = wialon_api.sid
            else:
                self.log = 'Nada .. no se conecta'
            url = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={%22spec%22:{%22itemsType%22:%22avl_resource%22,%22propName%22:%22drivers%22,%22propValueMask%22:%22%22,%22sortType%22:%22drivers%22,%22propType%22:%22propitemname%22},%22force%22:1,%22flags%22:256,%22from%22:0,%22to%22:0}&sid=";
            sid = wialon_api.sid
            res = requests.get(url + sid)
            # Users = self.env['res.users']
            driver_rec = self.env['gpscontrol.wialon_driver']
            logins = res.json()
            print(sid)
            print(res.text)
            print("------------------")
            for item in logins['items']:
                if item['drvrs']!={}:
                    print(item['drvrs'])

                # Users.create({'name': name['nm'], 'login': login['nm']})
                #vehiculo = driver_rec.create({
                #    'name': item['nm'],
                #    'id_wialon': item['id'],
                #})
                #if vehiculo:
                #    print('Se agrego correctamente el  ' + vehiculo.name)
                #    self.status = 'ok'
                #else:
                #    print('pailas')
                #    self.status = 'failed'

            self.log = 'ok'
        except WialonError as e:
            pass

class wialon_unit_group(models.Model):
    _name = "gpscontrol.wialon_unit_group"
    _rec_name = "id_wialon"

    name = fields.Char(string="Nombre de grupo")
    id_wialon = fields.Char(string="ID WIALON", required=True)
    childs_id = fields.One2many('gpscontrol.wialon_unit', 'parent_id', string="Hijos")
    crt = fields.Many2one('gpscontrol.wialon_pseudouser', string="Creator ID")
    bact = fields.Text('Id de cuenta')

    def create(self, vals):
        # number = self.env['ir.sequence'].next_by_code('gpscontrol.alistamientos')
        # vals['state'] = 'creado'
        # vals['folio'] = str(number)
        result = super(wialon_unit_group, self).create(vals)
        return result


class wialon_unit(models.Model):
    _name = "gpscontrol.wialon_unit"
    _rec_name = "name"
    _sql_constraints = [
        ('name_uniq', 'unique (id_wialon)',
         'El id wialon no puede repetirse')
    ]

    name = fields.Char(string="Nombre de unidad")
    id_wialon = fields.Char(string="ID WIALON", required=True)
    parent_id = fields.Many2one('gpscontrol.wialon_unit_group', string="Grupo")

    def create(self, vals):
        # number = self.env['ir.sequence'].next_by_code('gpscontrol.alistamientos')
        # vals['state'] = 'creado'
        # vals['folio'] = str(number)
        res = super(wialon_unit, self).create(vals)
        return res

    def setIntervals(self, val):
        self.service_intervals = val

    def setAdminFields(self, val):
        self.admin_fields = val

    def setCustomFields(self, val):
        self.custom_fields = val

class wialon_service_intervals(models.Model):
    _name = "gpscontrol.wialon_service_intervals"
    _rec_name = "name"


    name = fields.Char(string="Nombre")
    descripcion = fields.Char(string="Descripcion")
    i_kilometraje = fields.Integer(string="intervalo de kilometraje")
    i_dias = fields.Integer(string="Intervalo de Dias")
    i_horas = fields.Integer(string="Intervalo de horas del motor")
    pm = fields.Float(string="Ultimo servicio para el intervalo de kilometraje")
    pt = fields.Integer(string="Ultimo servicio para el intervalo de dias UTC")
    pe = fields.Integer(string="Ultimo servicio para intervalo de horas del motor")
    c = fields.Integer(string="Veces hechas")
    unit = fields.Many2one('gpscontrol.wialon_unit', string="Unidad")
    date_pm = fields.Datetime(string="ULTIMO SERVICIO KILOMETRAJE", compute="_calculate_pm")


    def _calculate_pm(self):
        self.date_pm = datetime.datetime.fromtimestamp(self.pm)



class wialon_admin_fields(models.Model):
    _name = "gpscontrol.wialon_admin_fields"
    _rec_name = "name"

    id = fields.Integer(string="Id")
    name = fields.Char(string="nombre")
    value = fields.Char(string="Valor")
    unit = fields.Many2one('gpscontrol.wialon_unit', string="Unidad")

class wialon_custom_fields(models.Model):
    _name = "gpscontrol.wialon_custom_fields"
    _rec_name = "name"

    id = fields.Integer(string="Id")
    name = fields.Char(string="nombre")
    value = fields.Char(string="Valor")
    unit = fields.Many2one('gpscontrol.wialon_unit', string="Unidad")

class wialon_drivers(models.Model):
    _name = "gpscontrol.wialon_driver"
    _rec_name = "name"
    _sql_constraints = [
        ('tel_uniq', 'UNIQUE (telefono)', '¡No puedes tener dos NAME_FIELD con el mismo nombre!')
    ]

    id_wia = fields.Integer(string="IdWialon", required=True)
    name = fields.Char(string="nombre")
    codigo = fields.Char(string="Codigo")
    password = fields.Char(string="Passsword")
    descripcion = fields.Text(string="Descripcion")
    telefono = fields.Char(string="Telefono", required=True)
    unidad_unida = fields.Integer(string="Unidad Actual")
    unidad_anterior = fields.Integer(string="Unidad anterior")
    ultimo_atracon = fields.Integer(string="Ultimo atracòn")
