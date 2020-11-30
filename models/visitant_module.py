# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models

class Visitant(models.Model):
    __name = 'emex51_module.visitant'
    
    dni = fields.Char()
    visita_solicitada = fields.Char()
    visita_respuesta = fields.boolean()
    visitado = fields.boolean()
    empleado = fields.Char()
    sector = fields.Char()
    fecha = fields.Datetime()
