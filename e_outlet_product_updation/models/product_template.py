# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from random import randint

import logging

_logger = logging.getLogger(__name__)
grey = "\x1b[38;21m"
yellow = "\x1b[33;21m"
red = "\x1b[31;21m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"
green = "\x1b[32m"
blue = "\x1b[34m"


class ProductZone(models.Model):
    _name = 'product.zone'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductShelf(models.Model):
    _name = 'product.shelf'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductVendor(models.Model):
    _name = 'product.vendor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductBrand(models.Model):
    _name = 'product.brand'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductDepartment(models.Model):
    _name = 'product.department'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductSeason(models.Model):
    _name = 'product.season'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductModell(models.Model):
    _name = 'product.modell'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductCategori(models.Model):
    _name = 'product.categori'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductCountry(models.Model):
    _name = 'product.country'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductColor(models.Model):
    _name = 'product.color'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductSize(models.Model):
    _name = 'product.size'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()


class ProductProduct(models.Model):
    _inherit = 'product.product'

    barcode_new_name = fields.Char(string="Barcode")

    def name_get(self):
        """ append new barcode to name """
        res = []
        for record in self:
            name = str(record.name) + str('[') + str(record.default_code) + str('-') + str(record.barcode_new_name) + str(']')
            res.append((record.id, name))
        return res

    def generate_barcode_randomly(self):
        product_obj = self.env['product.product'].search([])
        for i in range(len(product_obj)):
            barcode = product_obj[i].barcode
            #             print(randint(1300000000000, 8000000000000))
            _logger.info(red + "random ::::::::::::::: %s" % randint(130000000000, 800000000000) + reset)
            _logger.info(red + "product ::::::::::::::: %s" % product_obj[i] + reset)
            product_obj[i].barcode = randint(130000000000, 800000000000)
            product_obj[i].barcode_new_name = barcode


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    available_in_pos = fields.Boolean(string='Available in POS',
                                      help='Check if you want this product to appear in the Point of Sale.',
                                      default=True)

    type = fields.Selection(default='product')
    price_before_discount = fields.Float()
    barcode_new_name = fields.Char(string="Barcode")
    product_vendor_id = fields.Many2one('product.vendor', string="Vendor")
    product_brand_id = fields.Many2one('product.brand', string="Brand")
    product_department_id = fields.Many2one('product.department', string="Department")
    product_season_id = fields.Many2one('product.season', string="season")
    product_model_id = fields.Many2one('product.modell', string="product model")
    product_categori_id = fields.Many2one('product.categori', string="category")
    product_country_id = fields.Many2one('product.country', string="country")
    product_color_id = fields.Many2one('product.color', string="color")
    product_size_id = fields.Many2one('product.size', string="size")
    product_zone_id = fields.Many2one('product.zone', string="Product Zone")
    product_shelf_id = fields.Many2one('product.shelf', string="Product Shelf")

    @api.model
    def create(self, vals_list):
        products = super(ProductTemplate, self).create(vals_list)
        product = self.env['product.product'].search([('product_tmpl_id.id', '=', products.id)])
        product_obj = self.env['product.product'].search([]).mapped('barcode_new_name')
        barcode = products['barcode_new_name']
        barcode_new = products['barcode_new_name']
        default_code = products['default_code']
        cost = products['standard_price']
        for p in product:
            random_barcode = randint(130000000000, 800000000000)
            p.update({
                'barcode': random_barcode if random_barcode not in product_obj else ''
            })
            if barcode_new:
                p.update({
                    'barcode_new_name': str(barcode_new) + '-' + str(p.product_template_attribute_value_ids.name)
                })
            if default_code:
                p.update({
                    'default_code': str(default_code)
                })
            if cost:
                p.update({
                    'standard_price': cost
                })
        return products


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_vendor_id = fields.Many2one('product.vendor', strore=True, force_save=True,
                                        string="Vendor", related='product_id.product_vendor_id')
    product_brand_id = fields.Many2one('product.brand', strore=True, force_save=True,
                                       string="Brand", related='product_id.product_brand_id')
    product_department_id = fields.Many2one('product.department', strore=True, force_save=True,
                                            string="Department",
                                            related='product_id.product_department_id')
    product_season_id = fields.Many2one('product.season', strore=True, force_save=True,
                                        string="season", related='product_id.product_season_id')
    product_model_id = fields.Many2one('product.modell', strore=True, force_save=True,
                                       string="product model", related='product_id.product_model_id')
    product_categori_id = fields.Many2one('product.categori', strore=True, force_save=True,
                                          string="category", related='product_id.product_categori_id')
    product_country_id = fields.Many2one('product.country', strore=True, force_save=True,
                                         string="country", related='product_id.product_country_id')
    product_color_id = fields.Many2one('product.color', strore=True, force_save=True,
                                       string="color", related='product_id.product_color_id')
    product_size_id = fields.Many2one('product.size', strore=True, force_save=True,
                                      string="size", related='product_id.product_size_id')
    product_zone_id = fields.Many2one('product.zone', strore=True, force_save=True,
                                      string="Product Zone", related='product_id.product_zone_id')
    product_shelf_id = fields.Many2one('product.shelf', strore=True, force_save=True,
                                       string="Product Shelf", related='product_id.product_shelf_id')
