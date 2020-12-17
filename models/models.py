# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import randint, choice

from odoo.exceptions import ValidationError


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
    country = fields.Selection(
        selection=[
            ("germany", "Germany"),
            ("italy", "Italy"),
            ("cambodia", "Cambodia"),
            ("nigeria", "Nigeria"),
            ("china", "China"),
            ("india", "India"),
        ],
        string="Country"
    )
    year_created = fields.Date("Club created", default='2000-01-01')
    description = fields.Text(string="Club description", default="Lorem ipsum")
    is_active = fields.Boolean(string="Club is active?", compute="_compute_if_active")
    project_name_id = fields.One2many("project.project", "task_item_id", string="Project (O2m)",
                                      default=lambda x: x.env["project.project"].browse([2]))
    project_created = fields.Char(compute="_compute_project_date")
    copied_from = fields.Char(string="Copied From", readonly=True)

    @api.depends("project_name_id")
    def _compute_project_date(self):
        """
        Calculates created date for assigned project.
        """
        query_args = {'id': self.project_name_id.id or 1, }
        query = """
        SELECT create_date
        FROM "project_project"
        WHERE id = %(id)s
        """
        self.env.cr.execute(query, query_args)
        record = self.env.cr.fetchall()
        self.project_created = record[0]

    def _compute_if_active(self):
        for record in self:
            record.is_active = True

    def unlink(self):
        """
        Logs to console that record was delete.
        """
        print("the record been deleted")
        task_sheet = super(FootballClub, self).unlink()

    def write(self, vals):
        """
        Update annual_budget every time when timesheet is updated.
        """
        default_budget = self.default_get(["annual_budget"])
        try:
            vals["annual_budget"] *= 10
        except KeyError:
            vals["annual_budget"] = default_budget["annual_budget"]
        super(FootballClub, self).write(vals)

    def copy(self, default=None):
        """
        Adds '(copy)' to duplicated record name and removes original record.
        """
        new_record = super(FootballClub, self).copy()
        new_record.write({"copied_from": str(self.id), "name": self.name + "(copy)"})
        self.unlink()
        return new_record

    @api.onchange('region')
    def _update_country_selection(self):
        """
        Select default country depending on selected region.
        """
        if self.region == "Asia":
            self.country = "india"
        elif self.region == "Europe":
            self.country = "italy"
        elif self.region == "Africa":
            self.country = "nigeria"

    @api.constrains('club_name', 'description')
    def _check_description(self):
        """
        Validate description is not equal to club_name"
        """
        for record in self:
            if record.club_name == record.description:
                raise ValidationError("Fields name and description must be different")


class FootballPlayer(models.Model):
    """This model describes football club captain."""
    _inherit = 'account.analytic.line'

    selection_options = [
            ("new", "New"),
        ]
    player_name = fields.Char(string="Captain Name", compute="_compute_footballer_name")
    club_id = fields.Many2one("res.partner", ondelete='set null', string="Captain previous club", default=2)
    parent_field = fields.Selection(
        selection=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
        ],
        string="Parent"
    )
    child_field = fields.Selection(
        selection=selection_options,
        string="Child"
    )

    @api.onchange("parent_field")
    def _onchange_parent(self):
        print("parent change")
        print(self.selection_options)
        print(self.__dict__)
        FootballPlayer.selection_options = [
            ("new1", "New1"),
        ]
        print(self.selection_options)
        print(self.__dict__)

    @api.depends("club_id")
    def _compute_footballer_name(self):
        for record in self:
            record.player_name = choice(["Ronaldo", "Shevchenko", "Pele"])


class ProjectInherited(models.Model):
    """Model to test One2many inheritance field"""
    _inherit = "project.project"

    task_item_id = fields.Many2one("account.analytic.line", ondelete='set null', string="Needed for O2M testing")
