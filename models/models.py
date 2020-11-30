# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class emex51_module(models.Model):
#     _name = 'emex51_module.emex51_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100