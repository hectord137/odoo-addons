# -*- coding: utf-8 -*-
import json
import logging
import pprint

import requests
import werkzeug
from werkzeug import urls

from odoo import http
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

try:
    import urllib3
    pool = urllib3.PoolManager()
except:
    pass


class KhipuController(http.Controller):
    _accept_url = '/payment/khipu/test/accept'
    _decline_url = '/payment/khipu/test/decline'
    _exception_url = '/payment/khipu/test/exception'
    _cancel_url = '/payment/khipu/test/cancel'

    @http.route([
        '/payment/khipu/test/notify',
        '/payment/khipu/notify/<model("payment.acquirer"):acquirer_id>',
    ], type='http', auth='public', methods=['POST'], csrf=False)
    def khipu_validate_data(self,acquirer_id=None, **post):
        _logger.warning("post %s, acquirer_id %s" %(post, acquirer_id))
        tx_data = acquirer_id.khipu_getTransaction( post)
        res = request.env['payment.transaction'].sudo().form_feedback(tx_data, 'khipu')
        if not res:
            raise ValidationError("Transacción no esperada")
        return ''

    @http.route([
        '/payment/khipu/return',
        '/payment/khipu/test/return',
    ], type='http', auth='public', csrf=False, website=True)
    def khipu_form_feedback(self, **post):
        return werkzeug.utils.redirect('/shop/confirmation')

    @http.route([
        '/payment/khipu/final',
        '/payment/khipu/test/final',
    ], type='http', auth='none', csrf=False, website=True)
    def final(self, **post):
        return werkzeug.utils.redirect('/shop/confirmation')

    @http.route(['/payment/khipu/redirect'],
        type='http', auth='public', methods=["POST"], csrf=False, website=True)
    def redirect_khipu(self, **post):
        acquirer_id = int(post.get('acquirer_id'))
        acquirer = request.env['payment.acquirer'].browse(acquirer_id)
        result =  acquirer.sudo().khipu_initTransaction(post)
        return werkzeug.utils.redirect(result.payment_url)
        #@TODO render error
        #values={
        #    'khipu_redirect': resp,
        #}
        return request.render('payment_khipu.khipu_redirect', values)
    
    @http.route([
        '/payment/khipu/cancel/<model("payment.acquirer"):acquirer_id>',
        '/payment/khipu/test/cancel',
    ], type='http', auth='public', csrf=False, website=True)
    def khipu_cancel(self, **post):
        return werkzeug.utils.redirect('/shop/payment')

