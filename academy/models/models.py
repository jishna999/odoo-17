from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    mark = fields.Integer(string='Mark')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    qualification = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD')
    ], string='Qualification')
    teacher_id = fields.Many2one('academy.teacher', string='Teacher')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='State', default='new')
    tag_ids = fields.Many2many('academy.student.tag', string='Tags')
    hobby_list = fields.Many2many('academy.hobby', string='Hobbies')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                raise ValidationError("Please provide a valid name.")
        return super(Student, self).create(vals_list)

    def unlink(self):
        for rec in self:
            teacher_domain = [('teacher_id', '=', rec.id)]
            teacher = self.env['academy.teacher'].search(teacher_domain)
            if teacher:
                raise UserError("You cannot delete this student as they are associated with a teacher.")
        return super(Student, self).unlink()

    def action_confirm(self):
        self.write({'state': 'in_progress'})

    def action_ongoing(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Teacher Details'

    name = fields.Char(string="Full Name")
    phone_no = fields.Char(string="Mobile No")
    department = fields.Char(string="Department")
    address = fields.Text(string="Address")
    student_list = fields.One2many("academy.student", "teacher_id", string="Students")

    @api.ondelete(at_uninstall=False)
    def delete_teacher(self):
        for rec in self:
            if rec.name == 'Raji':
                raise ValidationError("You cannot delete this teacher because they are the HOD.")


class Hobby(models.Model):
    _name = 'academy.hobby'
    _description = 'Hobbies of the Students'

    name = fields.Char(string='Hobby')


class StudentTag(models.Model):
    _name = 'academy.student.tag'
    _description = 'Student Tag'
    _rec_name = 'name'
    _order = 'sequence'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    mobile = fields.Char(string='Mobile')
    student_tag_line_ids = fields.One2many('academy.student.tag.lines', 'student_tag_id', string='Tag Lines')
    total = fields.Float(compute='_compute_total_qty', string='Total Quantity', store=True)

    @api.depends('student_tag_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total = sum(rec.student_tag_line_ids.mapped('qty'))


class StudentTagLines(models.Model):
    _name = 'academy.student.tag.lines'
    _description = 'Student Tag Lines'

    student_tag_id = fields.Many2one('academy.student.tag', string='Student Tag')
    product_id = fields.Many2one('product.product', string='Student Product')
    qty = fields.Float(string='Quantity')

    display_name = fields.Char(string='Display Name', compute='_compute_display_name')

    @api.depends('qty', 'student_tag_id.name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.qty}] {rec.student_tag_id.name}"
