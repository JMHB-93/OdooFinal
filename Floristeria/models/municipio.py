from odoo import models, fields, api

class Municipio(models.Model):
    _name = 'floristeria.municipio'
    nombre = fields.Char('Nombre', required = True)
	codigoPostal = fields.Char('Código Postal', required = True)
    numeroFloristerias = fields.Integer('Número de floristerias', required = True)
    provincia = fields.Many2one('floristeria.provincia', 'Provincia')