# -*- coding: utf-8 -*-
###################################################################################
# GABRIEL PABON
###################################################################################

from odoo.http import request
from odoo import models, api


class EnlistReportParser(models.AbstractModel):
    _name = 'fuec.fuec_report_template'

    def get_report_values(self, docids, data=None):
        return data
