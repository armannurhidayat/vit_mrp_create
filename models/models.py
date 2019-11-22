# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class CreateLots(models.Model):
	_name = 'mrp.production'
	_inherit = 'mrp.production'

	@api.model
	def create(self, values):
		_logger.info(values)
		res = super(CreateLots, self).create(values)
		lot_data = {
			'name': res.name,
			'product_id': res.product_id.id
		}
		self.env['stock.production.lot'].create(lot_data)
		return res