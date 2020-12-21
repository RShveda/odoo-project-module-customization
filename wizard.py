# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AssignTimesheet(models.TransientModel):
    _name = 'project_football.wizard'
    _description = "Wizard to quickly assign club to the record"

    def _default_timesheet(self):
        return self.env['account.analytic.line'].browse(self._context.get('active_id'))

    def _default_club(self):
        account = self.env['account.analytic.line'].browse(self._context.get('active_id'))
        return self.env['res.partner'].browse(account.club_id.id)

    timesheet_id = fields.Many2one('account.analytic.line',
                                   string="Timesheet", required=True, default=_default_timesheet)
    club_id = fields.Many2one('res.partner', string="Attendees", default=_default_club)

    def assign(self):
        self.timesheet_id.club_id = self.club_id
        return {}
