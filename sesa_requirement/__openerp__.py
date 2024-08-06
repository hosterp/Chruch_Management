{
    'name': 'Hiworth Committee1',
    'version': '1.0',
    'category': 'Committee',
    'sequence': 21,
    'description': """ Committee Management """,
    'depends': ['hr','asn_baby_blue','report_xlsx',],
    'data': [
            'views/requirement_new.xml',
            'views/dashboard_view.xml',
            'views/place.xml',
            'views/menu_odoo_remove.xml',
            'views/hr_employee_view.xml',
            'views/res_partner_view.xml',
            'views/template.xml',
            'report/report.xml',
            'report/district_level_report.xml',
            'report/samithi_details_report.xml',
            'report/bhajan_mandali_report.xml',
            'report/Balvikas_details_report.xml',
            'report/centenary_report.xml',
            'views/revived_samithi.xml',
            'views/District_level_meetings.xml',
            'views/Balvikas_details.xml',
            'views/centenary_celebration.xml',
            'views/centenary_form.xml',
    ],
    # 'css': [
    #     "static/src/css/styles.css",
    #     ],
    'js': [
        'static/src/js/custom_webclient.js',
    ],
    "images": ['img/sssso_logo.png', ],
    # 'css': [
    #     'static/src/css/styles.css',
    # ],
    'qweb': [
        "static/src/xml/*.xml",
        # "static/src/css/styles.css",
            # 'static/src/css/template.xml'
        # 'static/src/xml/popup_notifications.xml',
    ],

    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}