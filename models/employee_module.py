# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Employee(models.Model):
    __name = 'emex51_module.employee'
    
    salario = fields.Float()
    puesto = fields.Char()
    sector = fields.Char()
    visitante = fields.Char()
    jefe = fields.Char()
