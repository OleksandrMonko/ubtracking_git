
from odoo import models, fields


class UBTrackingPerson(models.AbstractModel):
    _name = 'ubtracking.person.mixin'
    _description = 'Abstract Person'

    name = fields.Char(required=True)
    description = fields.Text()
    phone = fields.Char()
    user_id = fields.Many2one(
        comodel_name='res.users',
        ondelete='set null',
        default=lambda self: self.env.user)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],)
    image_1920 = fields.Image(string="Photo")
