# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Criature(models.Model):
    __name = 'emex51_module.criature'

    id_criatura= fields.Char()
    name = fields.Char()
    fecha_llegada = fields.DateTime()
    sector = fields.Char()