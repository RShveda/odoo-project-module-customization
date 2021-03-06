# -*- coding: utf-8 -*-
{
    'name': "project_football",

    'summary': """
        Testing Modules Inheritance""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'account', 'hr_employee_time_clock', 'hr_timesheet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/football_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/reports.xml',
        'data/football_cleanup_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
