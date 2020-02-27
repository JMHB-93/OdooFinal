from odoo import models, fields, api

class flores(models.Model):
    _name = 'floristería.flores'
    codigo = fields.Integer('Codigo', required = True)
    nombreComun = fields.Char('Nombre común', required = True)
	nombreCientifico = fields.Char('Nombre científico', required = True)
	especie = fields.Char('Especie', required = True)
	genero = fields.Char('Género', required = True)
    precio = fields.Float('Precio', required = True)
    precio = fields.Integer()
    cantidadFlores = fields.Integer('Cantidad de Flores', required=True)
    resultado = fields.Integer()
    multiplicar = fields.Integer(compute='multiplicar')
    

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    def suma(self):
        self.resultado = self.cantidadFlores * self.precio
    
