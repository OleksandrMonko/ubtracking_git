import logging

from odoo import models, fields, api

# from odoo import datetime

_logger = logging.getLogger(__name__)


class UBTrackingBill(models.Model):
    _name = 'ubtracking.bill'
    _description = 'Bill'

    description = fields.Text()
    service_name = fields.Char(required=False)

    apartment_id = fields.Many2one(comodel_name='ubtracking.apartment',
                                   required=True)
    billing_date = fields.Datetime(
        default=fields.Date.today(),
        required=True)

    billing_period = fields.Date(default=fields.Date.today().replace(day=1))

    amount = fields.Float(digits=(10, 2))

    name = fields.Char(compute='_compute_name', store=True)

    @api.depends('service_name', 'billing_date', 'billing_period', 'amount')
    def _compute_name(self):
        for record in self:
            if (record.service_name
                    and record.billing_period
                    and record.billing_date
                    and record.amount is not None):
                date_str = fields.Date.to_string(record.billing_period)
                record.name = (f'Bill for {date_str} for '
                               f'{record.service_name}.'
                               f' Amount {record.amount:.2f}. '
                               f'Dated {record.billing_date}')
            elif (record.billing_period
                  and record.billing_date
                  and record.amount is not None):
                date_str = fields.Date.to_string(record.billing_period)
                record.name = (f'Bill for {date_str}. '
                               f'Amount {record.amount:.2f}. '
                               f'Dated {record.billing_date}')
            else:
                record.name = ('Billing Period, Amount, and Billing Day '
                               'must be filled')
