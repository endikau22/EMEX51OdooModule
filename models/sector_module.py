# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Sector(models.Model):
    __name = 'emex51_module.sector'
    
    id_sector = fields.Char()
    tipo = fields.Char()
    visita = fields.DateTime()
    empleado = fields.Char()
