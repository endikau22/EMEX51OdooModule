# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Army (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51.army'
    _inherit = 'emex51.existence'
    
    # Declaración de los atributos de tipo básico de en Odoo.
    
    #El atributo string es como se ve en el form de la view de odoo. id lo crea odoo. Es un field reserved.
    ammunition = fields.Integer(required = True, string = "Munición Total")

