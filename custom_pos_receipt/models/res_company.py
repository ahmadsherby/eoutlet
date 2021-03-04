# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    fox_town_logo = fields.Binary()
    fox_town_name = fields.Char(string='Name')
    fox_address = fields.Char(string='Address')
    fox_vat_number = fields.Char(string="Vat Number")
    fox_phone = fields.Char(string="Phone")
    fox_email = fields.Char(string="Email")
