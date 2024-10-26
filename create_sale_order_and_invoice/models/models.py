from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Call the super method to ensure the standard confirmation process
        res = super(SaleOrder, self).action_confirm()

        # Initialize the variable to store the created invoice (if any)
        invoice = None

        # Iterate through the confirmed sale orders
        for order in self:
            if order.state == 'sale':
                # Create the delivery order if the order is confirmed
                picking = order._create_delivery_order()

                # Confirm the delivery (set to waiting state)
                if picking:
                    picking.action_confirm()

                # Create and validate the invoice if invoice is required
                if order.invoice_status == 'to invoice':
                    # Create the invoice as the "Create Invoice" button would
                    invoice = order._create_invoices()

                    # Validate (post) the invoice
                    if invoice and invoice.state == 'draft':
                        invoice.write({
                            'invoice_date': fields.Date.context_today(self),
                            'invoice_payment_term_id': order.payment_term_id.id,
                        })
                        invoice.action_post()

        # After confirming sale order and creating invoice, redirect to the invoice
        if invoice:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Customer Invoice',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': invoice.id,
                'view_id': self.env.ref('account.view_move_form').id,
                'target': 'current',
            }

        return res

    def _create_delivery_order(self):
        """
        Helper method to create delivery (stock picking) for the sale order.
        """
        pickings = self.env['stock.picking'].search([('origin', '=', self.name)])
        if not pickings:
            picking_vals = {
                'partner_id': self.partner_id.id,
                'picking_type_id': self.warehouse_id.out_type_id.id,  # Set delivery picking type
                'location_id': self.warehouse_id.lot_stock_id.id,  # Source location
                'location_dest_id': self.partner_id.property_stock_customer.id,  # Destination location
                'move_lines': self._get_move_lines(),
                'origin': self.name,
            }
            picking = self.env['stock.picking'].create(picking_vals)
            return picking
        return pickings

    def _get_move_lines(self):
        """
        Helper method to prepare stock moves for the delivery order.
        """
        moves = []
        for line in self.order_line:
            move_vals = {
                'name': line.product_id.name,
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_uom_qty,
                'product_uom': line.product_uom.id,
                'location_id': self.warehouse_id.lot_stock_id.id,
                'location_dest_id': self.partner_id.property_stock_customer.id,
                'sale_line_id': line.id,
            }
            moves.append((0, 0, move_vals))
        return moves
