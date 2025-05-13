import datetime
from odoo import models, fields, api
from odoo.tools import format_datetime


class ReportApartment(models.AbstractModel):
    _name = 'report.ubtracking.report_ubtracking_apartment_main_template'
    _description = 'Apartment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['ubtracking.apartment'].browse(docids)
        user = self.env.user
        return {
            'docs': docs,
            'user': user,
            'format_datetime': format_datetime,
            'now': fields.Datetime.now(),
            'datetime': datetime,
        }
