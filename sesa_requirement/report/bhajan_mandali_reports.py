from openerp import fields, models, api

class BhajanMandaiDetails(models.Model):
    _name = 'bhajan.mandali.details'
    date_from = fields.Date(required='True')
    date_to = fields.Date(required='True')

    @api.multi
    def print_activity_bhajan_mandali_details_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'bhajan.mandali.details'),
             ('report_name', '=', 'sesa_requirement.activity_bhajan_mandali_details_report_template',)])
        if data.download_filename:
            data.download_filename = 'BhajanmandaliDetailsReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_bhajan_mandali_details_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }
