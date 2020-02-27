from odoo import models, fields, api

class Provincia(models.Model):
    _name = 'floristeria.provincia'
    nombre = fields.Char('Nombre', required = True)
	codigoPostal = fields.Char('Código Postal', required = True)
    comunidadAutonoma = fields.Many2one('floristeria.comunidadAutonoma', 'Comunidad autónoma')

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res