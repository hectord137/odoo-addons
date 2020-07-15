# -*- coding: utf-8 -*-
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class WebsiteSaleCurrency(WebsiteSale):

    def _get_shop_payment_values(self, order, **kwargs):
        vals = super(WebsiteSaleCurrency, self)._get_shop_payment_values(order)
        pricelist_context = dict(request.env.context)
        pricelist = False
        if not pricelist_context.get('pricelist'):
            pricelist = request.website.get_current_pricelist()
            pricelist_context['pricelist'] = pricelist.id
        else:
            pricelist = request.env['product.pricelist'].browse(
                            pricelist_context['pricelist'])
        form_acquirers = []
        s2s_acquirers = []
        for acq in vals.get('form_acquirers', list()):
            if acq.currency_ids and \
             pricelist.currency_id.id not in acq.currency_ids.ids:
                continue
            form_acquirers.append(acq)
        for acq in vals.get('s2s_acquirers', list()):
            if acq.currency_ids and \
             pricelist.currency_id.id not in acq.currency_ids.ids:
                continue
            s2s_acquirers.append(acq)
        vals.update(
            form_acquirers=form_acquirers,
            s2s_acquirers=s2s_acquirers
        )
        return vals
