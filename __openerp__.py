# -*- encoding: utf-8 -*-

{
    'name': 'CRM mass mailing details',
    'author': 'Andrei Boyanov @ Novatus Ltd.',
    'version': '0.1',
    'depends': ['base', 'crm', 'mass_mailing'],
    'category': 'Marketing',
    'summary':
        'Lists all sent emails in the lead form',
    'description': """
       This module adds detailed list of sent emails to a lead in the CRM module. 
       The list of emails is visible under a new tab 'EMails' in the lead view form.
    """,
    'data': ['views/lead_view.xml', ],
    'demo': [],
    'installable': True,
    'website': 'http://novatus.bg/odoo/mail_crm_stats',
    'application': False,
    'certificate': '',
}
