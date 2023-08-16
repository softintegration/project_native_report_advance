# -*- coding: utf-8 -*-
{
    "name": """Gantt Native Report for Project""",
    "summary": """Added support Gantt""",
    "category": "Project",
    "images": ['static/description/icon.png'],
    "version": "1.0",
    "description": """
        PDF report

    """,
    "author": "Viktor Vorobjov",
    "license": "Other proprietary",
    "website": "https://straga.github.io",
    "support": "vostraga@gmail.com",

    "depends": [
        "web_gantt_native",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'report/project_native_report_advance_templates.xml',
        'report/project_native_views_main.xml',
        'wizard/project_native_pdf_view.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
        'web.assets_backend': [
            'project_native_report_advance/static/src/css/gantt_native_report.css'
        ]
    },
    "qweb": [],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}
