# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class User (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, añadiremos atributos extra que necesitamos para nuestro módulo
    _name = "res.users"
    _inherit = 'res.users'
    
    # Declaración de los atributos de tipo básico de en Odoo.
     
    #La clase res.users ya contiene name, email, password, login, login_date (lastConnection)
    last_pawword_change = fields.Date()
    
    #Los dos siguientes campos son valores preestablecidos en un enum.
    privilege = fields.Selection(selection=[('user','admin'),])
    status = fields.Selection(selection=[('enabled','disabled'),])
    
    
    
    
    
