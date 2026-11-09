# -*- coding: utf-8 -*-
{
    "name": "TotalPass / Asaas",
    "summary": "Colaboradores TotalPass e assinaturas recorrentes no Asaas",
    "version": "18.0.1.0.0",
    "category": "Services",
    "author": "AFR",
    "license": "LGPL-3",
    "depends": ["website", "mail"],
    "external_dependencies": {"python": ["requests"]},
    "assets": {
        "web.assets_frontend": [
            "afr_totalpass/static/src/scss/portal_totalpass.scss",
            "afr_totalpass/static/src/js/portal_totalpass_inscricao.js",
        ],
    },
    "data": [
        "security/totalpass_security.xml",
        "security/ir.model.access.csv",
        "data/cron.xml",
        "data/mail_template_data.xml",
        "views/totalpass_asaas_payment_views.xml",
        "views/totalpass_collaborator_views.xml",
        "views/res_config_settings_views.xml",
        "views/menus.xml",
        "views/portal_totalpass_templates.xml",
        "data/website_menu.xml",
    ],
    "installable": True,
    "application": True,
}
