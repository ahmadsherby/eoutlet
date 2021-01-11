# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductVendor(models.Model):
    _name = 'product.vendor'
    name = fields.Char()


class ProductBrand(models.Model):
    _name = 'product.brand'
    name = fields.Char()


class ProductDepartment(models.Model):
    _name = 'product.department'
    name = fields.Char()


class ProductSeason(models.Model):
    _name = 'product.season'
    name = fields.Char()


class ProductModell(models.Model):
    _name = 'product.modell'
    name = fields.Char()


class ProductCategori(models.Model):
    _name = 'product.categori'
    name = fields.Char()


class ProductCountry(models.Model):
    _name = 'product.country'
    name = fields.Char()


class ProductColor(models.Model):
    _name = 'product.color'
    name = fields.Char()


class ProductSize(models.Model):
    _name = 'product.size'
    name = fields.Char()


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_vendor_id = fields.Many2one('product.vendor', string="Vendor")
    product_brand_id = fields.Many2one('product.brand', string="Brand")
    product_department_id = fields.Many2one('product.department', string="Department")
    product_season_id = fields.Many2one('product.season', string="season")
    product_model_id = fields.Many2one('product.modell', string="product model")
    product_categori_id = fields.Many2one('product.categori', string="category")
    product_country_id = fields.Many2one('product.country', string="country")
    product_color_id = fields.Many2one('product.color', string="color")
    product_size_id = fields.Many2one('product.size', string="size")
