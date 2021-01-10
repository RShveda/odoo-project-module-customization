# -*- coding: utf-8 -*-

from odoo import tools
from odoo import api, fields, models


class ClubPlayersAnalysisReport(models.Model):
    _name = "club.players.analysis.report"
    _auto = False

    id = fields.Many2one('account.analytic.line', string="Record ID")
    total_players = fields.Integer(default=0, string="Players in club")
    name = fields.Char(string = "Club Name")

    def init(self):
        print("init method fired")
        tools.drop_view_if_exists(self.env.cr, 'club_players_analysis_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW club_players_analysis_report AS (
                SELECT
                    club.id AS id,
                    club.club_name AS name,
                    club.players_count AS total_players
                FROM
                    account_analytic_line club)
        """)
