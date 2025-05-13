import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class UBTrackingApartment(models.Model):
    _name = 'ubtracking.apartment'
    _description = 'Apartment'

    name = fields.Char(required=True)
    description = fields.Text()

    apartment_administrator_id = fields.Many2one(
        comodel_name='ubtracking.apartment_administrator', )
    apartment_user_id = fields.Many2one(
        comodel_name='ubtracking.apartment_user', )

    bill_ids = fields.One2many(
        comodel_name='ubtracking.bill',
        inverse_name='apartment_id',
        string='Bills'
    )
    payment_ids = fields.One2many(
        comodel_name='ubtracking.payment',
        inverse_name='apartment_id',
        string='Payments'
    )
