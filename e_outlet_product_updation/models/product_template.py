# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductZone(models.Model):
    _name = 'product.zone'
    name = fields.Char()


class ProductShelf(models.Model):
    _name = 'product.shelf'
    name = fields.Char()


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


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # @api.model
    # def default_get(self, fields_list):
    #     """get default lines"""
    #     print("LLLLLLLLLLLLLLLLLL", fields_list)
    #     # print("LLLLLLLLLLLLLLLLLL", fields_list['default_code'])
    #     print("LLLLLLLLLLLLLLLLLL", self.default_code)
    #     res = super(ProductProduct, self).default_get(fields_list)
    #     res['default_code'] = str(self.product_tmpl_id.default_code) + '999999999999999999'
    #     return res

    # @api.model
    # def create(self, vals_list):
    #     products = super(ProductProduct, self).create(vals_list)
    #     print(":::::::::::::ProductProduct create:::::::::::::::", products)
    #     return products
    #
    # def write(self, values):
    #     print(":::::::::::::ProductProduct values:::::::::::::::", values)
    #     print(":::::::::::::product_tmpl_id:::::::::::::::", self.product_tmpl_id)
    #     print(":::::::::::::default_code:::::::::::::::", self.product_tmpl_id.default_code)
    #     res = super(ProductProduct, self).write(values)
    #     print(":::::::::::::default_codeeeeeeeeee:::::::::::::::", self.product_tmpl_id.default_code)
    #     if 'active' in values:
    #         if self.product_tmpl_id:
    #            if self.product_tmpl_id.default_code:
    #                 # print("product_template_attribute_value_ids", self.product_template_attribute_value_ids)
    #                 self.default_code = str(self.product_tmpl_id.default_code)
    #            # if self.product_tmpl_id.barcode:
    #            #      # print("product_template_attribute_value_ids", self.product_template_attribute_value_ids)
    #            #      self.barcode = str(self.product_tmpl_id.barcode)
    #                                 # + str(self.product_template_attribute_value_ids[0]['name'])
    #     # print(":::::::::::::ProductProduct res write:::::::::::::::", res)
    #     # raise Warning(_("<<<<<<<<<<<<<<<<<<<"))
    #     return res

    # @api.onchange('product_tmpl_id')
    # def onchange_product_template_id(self):
    #     print(">>>>>>>>>>>>>>>>>>>::::::::::::::::::", self.product_tmpl_id.name)
    #     print(">>>>>>>>>>>>>>>>>>>::::::::::::::::::", self.product_tmpl_id.barcode)
    #     print(">>>>>>>>>>>>>>>>>>>::::::::::::::::::", self.product_tmpl_id.default_code)

    # @api.onchange
    # def write(self, default_code):
    #     res = super(self.product_tmpl_id).write(default_code)
    #     print(" work create")
    #     return res

    # # @api.model
    #  def write(self, values):
    #      res = super(TestStudent, self).write(values)
    #      print("ooooo")
    #      return res


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    available_in_pos = fields.Boolean(string='Available in POS',
                                      help='Check if you want this product to appear in the Point of Sale.',
                                      default=True)

    type = fields.Selection(default='product')
    price_before_discount = fields.Float()

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
        x = products['barcode']
        default_code = products['default_code']
        cost = products['standard_price']
        for p in product:
            if x:
                #                 products['barcode']
                p.update({
                    'barcode': str(x) + '-' + str(p.product_template_attribute_value_ids.name)
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

    # def write(self, values):
    #     print("KKKKKKKKKKKKKKKKKKKKK", values)
    #     res = super(ProductTemplate, self).write(values)
    #     product_obj = self.env['product.product'].search([('product_tmpl_id.id', '=', self.id)])
    #     barcode = self.barcode
    #     default_code = self.default_code
    #     for p in product_obj:
    #         if barcode and not p.barcode:
    #             if p.product_template_attribute_value_ids:
    #                 print("p.product_template_attribute_value_ids", p.product_template_attribute_value_ids)
    #                 p.update({
    #                     'barcode': str(barcode) + '-' + str(p.product_template_attribute_value_ids.name)
    #                 })
    #         if default_code and not p.default_code:
    #             p.update({
    #                 'default_code': str(default_code)
    #             })
    #
    #     return res
