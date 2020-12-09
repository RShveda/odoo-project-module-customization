# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FootballClub(models.Model):
    """Extra fields for project.task model of project standard module. This model describes football club."""
    _inherit = 'project.task'

    club_name = fields.Char(string="Club Name")
    currency = fields.Many2one('res.currency', ondelete='set null', string="Currency")
    annual_budget = fields.Monetary(currency_field="currency")
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
    project_name = fields.One2many("project.project", "task_item", string="Project (O2m)")


class FootballPlayer(models.Model):
    """Extra fields for project.task model of Project standard module. This model describes football club captain."""
    _inherit = 'project.task'

    player_name = fields.Char(string="Captain Name")
    club = fields.Many2one("res.partner", ondelete='set null', string="Captain previous club")


class ProjectInherited(models.Model):
    """model to test One2many inheritance field"""
    _inherit = "project.project"

    task_item = fields.Many2one("project.task", ondelete='set null', string="Needed for O2M testing")

