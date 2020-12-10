# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
#Esta clase es la tabla que se crea por la relación * a * entre empleado y sector con el atributo fecha. 
class SectorEmployees (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51.sectoremployees'
    
    # Declaración de los atributos de tipo básico de en Odoo.
    
    #El atributo string es como se ve en el form de la view de odoo. id lo crea odoo. Es un field reserved.
    workDate = fields.Date(string ="Fecha de trabajo")
    
    #Declaración de los atributos relacionales con otras clases.
    empleados = fields.Many2one('emex51.employee',ondelete ='set null',string="Empleados") 
    sectores = fields.Many2one('emex51.sector',ondelete ='set null',string="Sectores")