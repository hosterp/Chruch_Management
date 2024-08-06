from openerp import fields, models, api

class CentenaryReport(models.Model):
    _name = 'centenary.report'

    date_from = fields.Date(required='True')
    date_to = fields.Date(required='True')
    Category = fields.Many2one('centenary.celebration', 'Category',)

    @api.multi
    def get_centenary_report(self):
        data = self.env['centenary.form']

        if self.date_from and self.date_to:
            data = data.search([
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
            ])
            if self.Category:
                data = data.filtered(lambda r: r.Category == self.Category)
        return data


    @api.multi
    def get_all_categories(self):
        return self.env['centenary.form'].search([])
    @api.multi
    def get_data_by_category(self):
        all_data = self.get_centenary_report()
        categorized_data = {}
        for category in self.get_all_categories():
            categorized_data[category.Category] = all_data.filtered(lambda r: r.Category == category.Category)
        return categorized_data

    @api.multi
    def print_activity_centenary_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'centenary.form'),
             ('report_name', '=', 'sesa_requirement.activity_centenary_report_template',)])
        if data.download_filename:
            data.download_filename = 'Centenary Report'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_centenary_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }
