from odoo import fields, models, api, _


class AttendanceRejectWizard(models.Model):
    _name = 'attendance.reject.wizard'
    _description = 'Rejection Reason'

    reason = fields.Text(string='Reason', required=True)

    def action_attendance_reject(self):
        vals = {
            'reason': self.reason,
            'employee': 1,
            'type': 'check in',
            'action_to_do': 'new record',
        }
        attendance_rec = self.env['attendance.modification.request'].create(vals)
        return {
            'name': _('Rejection Reason'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'attendance.modification.request',
            'res_id': attendance_rec.id,
        }
