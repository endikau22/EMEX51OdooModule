# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Boss (models.Model):
    __name = 'emex51_module.boss'
    
    salario = fields.Float()
    empleado = fields.Char()
