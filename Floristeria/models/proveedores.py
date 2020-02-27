from odoo import models, fields, api

class Proveedores(models.Model):
    _name = 'floristería.proveedores'
	codigo = fields.Integer('Código', required = True)
    nombre = fields.Char('Nombre', required = True)
    nombreRepresentante = fields.Char('Nombre Representante', required = True)
    telefono = fields.Char('Teléfono', required = True)
	email = fields.Char('Email', required = True)
	provincia = fields.Many2one('floristeria.municipio', 'Municipio')
    

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
