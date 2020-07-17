# -*- coding: utf-'8' "-*-"|
from odoo import api, models, fields
from odoo.tools import float_round
import logging
_logger = logging.getLogger(__name__)


class PaymentAcquirerCurrency(models.Model):
    _inherit = 'payment.acquirer'

    currency_ids = fields.Many2many(
        'res.currency',
        string='Currencies',
        help="Use only these allowed currencies."
    )
    force_currency = fields.Boolean(
        string="Force Currency",
    )
    force_currency_id = fields.Many2one(
        'res.currency',
        string='Currency id',
    )

    def compute_fees(self, amount, currency_id, partner_country_id):
        fees_method_name = '%s_compute_fees' % self.provider
        fees_amount = 0
        if hasattr(self, fees_method_name):
            fees = getattr(self, fees_method_name)(amount, currency_id, partner_country_id)
            fees_amount = float_round(fees, 2)
        return fees_amount
