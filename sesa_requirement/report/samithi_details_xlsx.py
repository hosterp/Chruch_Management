try:
    from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    class ReportXlsx(object):
        def __init__(self, *args, **kwargs):
            pass
from datetime import datetime
class SamithiDetailsReportXlsx(ReportXlsx):
    def generate_xlsx_report(self, workbook, data, lines):
        format = workbook.add_format({'font_size': 14, 'align': 'vcentre', 'bold': True})
        format1 = workbook.add_format({'font_size': 10, 'align': 'vcentre', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcentre', 'bold': False})
        format3 = workbook.add_format({'font_size': 13, 'align': 'vcentre', 'bold': True})
        format4 = workbook.add_format({'font_size': 8, 'align': 'vcentre', 'bold': False})

        sheet = workbook.add_worksheet('Activity')
        sheet.merge_range('G3:L3', "Samithi Details Report", format)
        # sheet.merge_range('G4:H4', "Stock Order", format)

        # sheet.write(6, 1, "Sl No ", format1)
        sheet.write(6, 6, "Sl No ", format1)
        sheet.write(6, 7, "Samithi ", format1)
        sheet.write(6, 8, "Date ", format1)

        data = lines.env['event.place']

        if lines.date_from and lines.date_to:
            data = data.search([
                ('date', '>=', lines.date_from),
                ('date', '<=', lines.date_to),
            ])
            if lines.place:
                data = data.filtered(lambda r: r.place == lines.place)
            if lines.event_district:
                data = data.filtered(lambda r: r.event_district == lines.event_district)

        row = 7
        slno = 1
        for order in data:
            sheet.write(row, 6, slno , format4)
            sheet.write(row, 7, order.place if order.place else "Nil", format4)
            sheet.write(row, 8, order.date if order.date else "Nil", format4)
            row += 1
            slno += 1


SamithiDetailsReportXlsx('report.sesa_requirement.samithi_details_report_template_xlsx.xlsx', 'samithi.details.report')