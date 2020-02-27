from odoo import models, fields, api

class Dueno(models.Model):
    _name = 'floristeria.dueno'
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)
	telefono = fields.Char('Teléfono', required = True)
	email = fields.Char('Email', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res