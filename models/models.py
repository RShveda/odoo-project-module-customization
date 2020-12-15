# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import randint, choice


class FootballClub(models.Model):
    """This model describes football club."""
    _inherit = 'account.analytic.line'

    club_name = fields.Char(string="Club Name", default="MyClub")
    currency_id = fields.Many2one('res.currency', ondelete='set null', string="Currency",
                                  default=lambda x: x.env.company.currency_id)
    annual_budget = fields.Monetary(currency_field="currency_id", default=lambda x: randint(1, 10))
    players_count = fields.Integer(string="Number of players", default=lambda x: len(x.env.company.user_ids))
    region = fields.Selection(
        selection=[
            ("Europe", "Europe"),
            ("Asia", "Asia"),
            ("Africa", "Africa"),
        ],
        default="Asia",
        string="Region"
    )
    year_created = fields.Date("Club created", default='2000-01-01')
    description = fields.Text(string="Club description", default="Lorem ipsum")
    is_active = fields.Boolean(string="Club is active?", compute="_compute_if_active")
    project_name_id = fields.One2many("project.project", "task_item_id", string="Project (O2m)", default=None)

    def _compute_if_active(self):
        for record in self:
            record.is_active = True


class FootballPlayer(models.Model):
    """This model describes football club captain."""
    _inherit = 'account.analytic.line'

    player_name = fields.Char(string="Captain Name", compute="_compute_footballer_name")
    club_id = fields.Many2one("res.partner", ondelete='set null', string="Captain previous club", default=2)

    def _compute_footballer_name(self):
        for record in self:
            record.player_name = choice(["Ronaldo", "Shevchenko", "Pele"])


class ProjectInherited(models.Model):
    """Model to test One2many inheritance field"""
    _inherit = "project.project"

    task_item_id = fields.Many2one("account.analytic.line", ondelete='set null', string="Needed for O2M testing")
