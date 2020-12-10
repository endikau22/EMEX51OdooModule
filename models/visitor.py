# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
class Visitor (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, añadiremos atributos extra que necesitamos para nuestro módulo
    _name = "emex51.visitor"
    _inherit = 'res.users'
    
    # Declaración de los atributos de tipo básico de en Odoo.
    
    #La clase res.users ya contiene name, email, password, login, login_date (lastConnection) 
    dni = fields.Char(string = "DNI")
    requesteVisitDate = fields.Date(string = "Fecha petición visita")
    visitReply = fields.Boolean(string = "Respuesta a petición")
    visited = fields.Boolean(string = "Visitado")
    visitDate = fields.Date(string = "Fecha visita")
    
    
    #Declaración de los atributos relacionales con otras clases.
    
    #Los visitantes son gestionados por un empleado
    employee = fields.Many2one('emex51.employee',ondelete ='cascade',string="Visitantes")
    #Un visitante visita varios sectores, un sector es visitado por varios  visitantes
    visitedSectors = fields.Many2many('emex51.sector',string="Sectores visitados")