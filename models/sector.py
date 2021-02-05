# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#Endika Ubierna
from odoo import models,fields,api
from odoo.exceptions import ValidationError
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Sector (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.sector'
    # Declaracion de los atributos de tipo basico de en Odoo.
    #El atributo string es como se ve en el form de la view de odoo.
#id lo crea odoo. Es un field reserved.
    name = fields.Char(required = True, string = "Nombre")
    tipo = fields.Selection(selection=[('creature','Creature'),('army','Army')])
    #Declaracion de los atributos relacionales con otras clases.
    #Un empleado gestiona varios sectores, un sector en gestionado por varios empleados.
# NM con atributos clase intermedia dos 1N
    employees = fields.One2many('emex51_module.sectoremployees','sectors',string="Empleados")
    #Un visitante visita varios sectores, un sector es visitado por varios  visitantes
    visitors = fields.Many2many('emex51_module.visitor',string="Visitantes")
    #En un sector hay varias existencias y una existencia esta en un sector.
# Estas pueden ser armas o criaturas
    creatures = fields.One2many('emex51_module.creature','sector',string="Criaturas")
    armys = fields.One2many('emex51_module.army','sector',string="Armas")
    
    
    @api.constrains('name')
    def _check_name_length(self):
        for sector in self:
            if len(sector.name)<3:
                raise ValidationError('El nombre es muy corto, debe tener al menos 3 caracteres')
            elif len(sector.name)>20:
                raise ValidationError('El nombre es muy largo, debe tener menos de 20 caracteres')

    @api.constrains('tipo')
    def _tipo(self):
        for sector in self:
            if len(sector.creatures)>0:
                if sector.tipo == 'army':
                    raise ValidationError('El sector contiene criaturas, no puede ser de tipo army')
            if len(sector.armys)>0:
                if sector.tipo == 'creature':
                    raise ValidationError('El sector contiene armas, no puede ser de tipo creature')
                