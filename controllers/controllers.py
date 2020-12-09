# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectFootball(http.Controller):
#     @http.route('/project_football/project_football/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_football/project_football/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_football.listing', {
#             'root': '/project_football/project_football',
#             'objects': http.request.env['project_football.project_football'].search([]),
#         })

#     @http.route('/project_football/project_football/objects/<model("project_football.project_football"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_football.object', {
#             'object': obj
#         })
