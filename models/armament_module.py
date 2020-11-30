# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Armament(models.Model):
    __name = 'emex51_module.armament'
    
    id_armamento = fields.Char()
    name = fields.Char()
    fecha_llegada = fields.DateTime()
    sector = fields.Char()
