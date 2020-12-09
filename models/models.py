# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FootballClub(models.Model):
    """This model describes football club."""
    _inherit = 'account.analytic.line'

    club_name = fields.Char(string="Club Name")
    currency_id = fields.Many2one('res.currency', ondelete='set null', string="Currency")
    annual_budget = fields.Monetary(currency_field="currency_id")
    players_count = fields.Integer(string="Number of players")
    region = fields.Selection(
        selection=[
            ("Europe", "Europe"),
            ("Asia", "Asia"),
            ("Africa", "Africa"),
        ],
        string="Region"
    )
    year_created = fields.Date("Club created")
    description = fields.Text(string="Club description")
    is_active = fields.Boolean(string="Club is active?")
    project_name_id = fields.One2many("project.project", "task_item_id", string="Project (O2m)")


class FootballPlayer(models.Model):
    """This model describes football club captain."""
    _inherit = 'account.analytic.line'

    player_name = fields.Char(string="Captain Name")
    club_id = fields.Many2one("res.partner", ondelete='set null', string="Captain previous club")


class ProjectInherited(models.Model):
    """Model to test One2many inheritance field"""
    _inherit = "project.project"

    task_item_id = fields.Many2one("account.analytic.line", ondelete='set null', string="Needed for O2M testing")

