from odoo import fields, models, api, _


class AttendanceModificationRequest(models.Model):
    _name = 'attendance.modification.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Attendance Modification Request'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True,
                       default=lambda self: _('REQ'))
    employee = fields.Many2one('hr.employee', string='Employee', required=True)
    date = fields.Date(string="Date")
    type = fields.Selection([('check in', 'Check In'), ('check out', 'Check Out'), ('both', 'Both'),
                             ], required=True, tracking=True)
    action_to_do = fields.Selection([('new record', 'New Record'), ('modification', 'Modification'),
                                     ], required=True, tracking=True)
    attendance = fields.Many2one('hr.attendance', string='Attendance')
    updated_value_checkin = fields.Datetime(string="Updated Value Check In")
    updated_value_checkout = fields.Datetime(string="Updated Value Check Out")
    reason = fields.Text(string='Reason')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Waiting For Approve'),
                              ('approve', 'Approved'), ('reject', 'Rejected'), ('cancel', 'Canceled')], default='draft',
                             string="Status", tracking=True)

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_reject(self):
        for rec in self:
            rec.state = 'reject'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', _('REQ')) == _('REQ'):
            vals['name'] = self.env['ir.sequence'].next_by_code('attendance.modification.request') or _('New')
        res = super(AttendanceModificationRequest, self).create(vals)
        return res


