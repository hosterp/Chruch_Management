from openerp import fields, models, api


class SamithidetailsReport(models.Model):
    _name = 'samithi.details.report'

    place = fields.Char('Place')
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

    date_from = fields.Date(required='True')
    date_to=fields.Date(required='True')

    @api.multi
    def print_activity_samithi_details_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.place'), ('report_name', '=', 'sesa_requirement.activity_samithi_details_report_template',)])
        if data.download_filename:
            data.download_filename = 'SamithiDetailsReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_samithi_details_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }

    @api.multi
    def print_samithi_details_report_xlsx_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {'type': 'ir.actions.report.xml',
                'report_name': 'sesa_requirement.samithi_details_report_template_xlsx.xlsx',
                'report_type': 'xlsx',
                'datas': datas
                }

    @api.multi
    def get_samithi_details_report(self):
        data = self.env['event.place']

        if self.date_from and self.date_to:
            data = data.search([
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
            ])
            if self.place:
                data = data.filtered(lambda r: r.place == self.place)
            if self.event_district:
                data = data.filtered(lambda r: r.event_district == self.event_district)

        return data

