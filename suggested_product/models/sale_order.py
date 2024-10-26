from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    suggested_product_ids = fields.One2many(
        comodel_name='suggested.product',
        inverse_name='order_id',
        string="Suggested Products"
    )

    def _create_invoices(self, grouped=False, final=False):

        invoice_vals_list = super(SaleOrder, self)._create_invoices(grouped, final)

        for order in self:

            invoices = self.env['account.move'].search([('invoice_origin', '=', order.name)])

            for invoice in invoices:

                suggested_product_vals = []
                for suggested_product in order.suggested_product_ids:
                    suggested_product_vals.append((
                        0, 0, {
                            'product_id': suggested_product.product_id.id,
                            'product_uom_qty': suggested_product.product_uom_qty,
                            'sale_price': suggested_product.sale_price,
                        }
                    ))

                if suggested_product_vals:
                    invoice.write({'suggested_product_ids': suggested_product_vals})

        return invoice_vals_list
