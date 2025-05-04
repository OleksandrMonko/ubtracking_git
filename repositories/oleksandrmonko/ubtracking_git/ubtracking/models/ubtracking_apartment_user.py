import logging


from odoo import models, fields

_logger = logging.getLogger(__name__)


class UBTrackingApartmentUser(models.Model):
    _inherit = 'ubtracking.person.mixin'
    _name = 'ubtracking.apartment_user'
    _description = 'Apartment user'

    start_date = fields.Date(required=True, string='Start Date')
    end_date = fields.Date(required=False, string='End Date')

    user_apartment_ids = fields.One2many(
        comodel_name='ubtracking.apartment',
        inverse_name='apartment_user_id')
