import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class UBTrackingApartmentAdministrator(models.Model):
    _inherit = 'ubtracking.person.mixin'
    _name = 'ubtracking.apartment_administrator'
    _description = 'Apartment administrator'

    administrator_apartment_ids = fields.One2many(
        comodel_name='ubtracking.apartment',
        inverse_name='apartment_administrator_id')
