from openerp import fields, models, api


class ActivityReport(models.Model):
    _name = 'activity.report'


    date_from =fields.Date('Date From' ,required="True")
    date_to =fields.Date('Date To' ,required="True")
    # event_category = fields.Selection([
    #     ('balvikas', 'Balvikas'),
    #     ('education', 'Education'),
    #     ('spiritual', 'Spiritual'),
    #     ('mahila', 'Mahila'),
    #     ('saiyouth', 'Sai Youth'),
    # ], string='Event Category')
    event_category = fields.Many2one('event.category', "Event Category")
    event_district = fields.Selection([('AL', 'ALAPPUZHA'),
                                       ('ER', 'ERNAKULAM'),
                                       ('ID', 'IDUKKI'),
                                       ('KN', 'KANNUR'),
                                       ('KS', 'KASARAGOD'),
                                       ('KL', 'KOLLAM'),
                                       ('KT', 'KOTTAYAM'),
                                       ('KZ', 'KOZHIKODE'),
                                       ('MA', 'MALAPPURAM'),
                                       ('PL', 'PALAKKAD'),
                                       ('PT', 'PATHANAMTHITTA'),
                                       ('TV', 'THIRUVANANTHAPURAM'),
                                       ('TS', 'THRISSUR'),
                                       ('WA', 'WAYANAD')])

    event_place = fields.Many2one('event.place', "Place")
    revived_samithi = fields.Boolean(string="Revived Samithi")
    event_type = fields.Many2one('event.type')

    @api.multi
    def print_activity_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.event'), ('report_name', '=', 'sesa_requirement.activity_report_template',)])
        if data.download_filename:
            data.download_filename = 'ActivityReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }

    @api.multi
    def print_activity_report_view(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.event'), ('report_name', '=', 'sesa_requirement.activity_report_template',)])
        if data.download_filename:
            data.download_filename = 'ActivityReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_report_template',
            'datas': datas,
            'report_type': 'qweb-html',
        }

    @api.multi
    def print_activity_report_xlsx_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {'type': 'ir.actions.report.xml',
                'report_name': 'sesa_requirement.activity_report_template_xlsx.xlsx',
                'report_type': 'xlsx',
                'datas': datas
                }


    @api.multi
    def get_activity_report(self):
        if self.date_from and self.date_to:
            invoice_ids = self.env['event.event'].search([
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
            ])
            if self.event_district:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_district', '=', self.event_district),
                ])
            if self.event_place:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_place', '=', self.event_place.id),
                ])
            if self.revived_samithi:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('revived_samithi', '=', True),
                ])
            if self.event_district and self.event_place:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_district', '=', self.event_district),
                    ('event_place', '=', self.event_place.id),
                    ('revived_samithi', '=', True),
                ])
            if self.event_type:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_type', '=', self.event_type.id),
                ])
            if self.event_category:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_category', '=', self.event_category.id),
                ])
            if self.event_type and  self.event_district:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_type', '=', self.event_type.id),
                    ('event_district', '=', self.event_district),
                ])
            if self.event_type and self.event_place:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_type', '=', self.event_type.id),
                    ('event_place', '=', self.event_place.id),
                ])
            if self.event_type and self.event_category:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_type', '=', self.event_type.id),
                    ('event_category', '=', self.event_category.id),
                ])
            if self.event_type and self.event_category and self.event_place  and  self.event_district:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_type', '=', self.event_type.id),
                    ('event_category', '=', self.event_category.id),
                    ('event_place', '=', self.event_place.id),
                    ('event_district', '=', self.event_district),
                ])
            if self.event_district and self.revived_samithi:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_district', '=', self.event_district),
                    ('revived_samithi', '=', True),
                ])
            if self.event_district and self.revived_samithi and self.event_category:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_district', '=', self.event_district),
                    ('revived_samithi', '=', True),
                    ('event_category', '=', self.event_category.id),
                ])
            if self.event_district and self.event_place and self.event_category:
                invoice_ids = self.env['event.event'].search([
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('event_district', '=', self.event_district),
                    ('event_place', '=', self.event_place.id),
                    ('event_category', '=', self.event_category.id),

                ])

            return invoice_ids

    @api.onchange('event_category')
    def onchange_event_category(self):
        for record in self:
            if record.event_category:
                return {'domain': {'event_type': [('event_category', '=', record.event_category.id)]}}

    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain': {'event_place': [('event_district', '=', record.event_district)]}}
