from openerp import fields, models, api

class BalvikasDetails(models.Model):
    _name = 'event.balvikas'

    date = fields.Date(string="Date", default=fields.Date.today)
    balvikas_centers=fields.Integer()
    new_balvikas=fields.Integer()
    total_students=fields.Integer()
    total_guru=fields.Integer()

    @api.multi
    def print_activity_balvikas_details_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.balvikas'),
             ('report_name', '=', 'sesa_requirement.activity_balvikas_details_report_template',)])
        if data.download_filename:
            data.download_filename = 'BalvikasReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_balvikas_details_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }