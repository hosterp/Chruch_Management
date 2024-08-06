try:
    from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    class ReportXlsx(object):
        def __init__(self, *args, **kwargs):
            pass
from datetime import datetime
class ActivityReportXlsx(ReportXlsx):
    def generate_xlsx_report(self, workbook, data, lines):
        format = workbook.add_format({'font_size': 14, 'align': 'vcentre', 'bold': True})
        format1 = workbook.add_format({'font_size': 10, 'align': 'vcentre', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcentre', 'bold': False})
        format3 = workbook.add_format({'font_size': 13, 'align': 'vcentre', 'bold': True})
        format4 = workbook.add_format({'font_size': 8, 'align': 'vcentre', 'bold': False})

        sheet = workbook.add_worksheet('Activity')
        sheet.merge_range('G3:L3', "Activity Report", format)
        # sheet.merge_range('G4:H4', "Stock Order", format)

        # sheet.write(6, 1, "Sl No ", format1)
        sheet.write(6, 1, "Name ", format1)
        sheet.write(6, 2, "Reporting In-Charge ", format1)
        sheet.write(6, 3, "	Event Category ", format1)
        sheet.write(6, 4, "Event type", format1)
        sheet.write(6, 5, "Date of event", format1)
        sheet.write(6, 6, "Place", format1)
        sheet.write(6, 7, "Total Attendees", format1)
        sheet.write(6, 8, "Total devotees attended", format1)
        sheet.write(6, 9, "Details", format1)
        sheet.write(6, 10, "Remark", format1)
        sheet.write(6, 11, "Status", format1)

        if lines.date_from and lines.date_to:
            invoice_ids = lines.env['event.event'].search([
                ('date', '>=', lines.date_from),
                ('date', '<=', lines.date_to),
            ])
            if lines.event_district:
                invoice_ids = lines.env['event.event'].search([
                    ('date', '>=', lines.date_from),
                    ('date', '<=', lines.date_to),
                    ('event_district', '=', lines.event_district),
                ])
            if lines.event_place:
                invoice_ids = lines.env['event.event'].search([
                    ('date', '>=', lines.date_from),
                    ('date', '<=', lines.date_to),
                    ('event_place', '=', lines.event_place.id),
                ])
            if lines.event_category:
                invoice_ids = lines.env['event.event'].search([
                    ('date', '>=', lines.date_from),
                    ('date', '<=', lines.date_to),
                    ('event_category', '=', lines.event_category.id),
                ])

            row = 7
            for order in invoice_ids:

                sheet.write(row, 1, order.user.name if order.user else "Nil", format4)
                sheet.write(row, 2, order.reporting_incharge.display_name if  order.reporting_incharge else "Nil" , format4)
                sheet.write(row, 3, order.event_category.display_name if order.event_category else  "Nil" , format4)
                sheet.write(row, 4, order.event_type.display_name if order.event_type else "Nil", format4)
                sheet.write(row, 5, order.date if order.date else "Nil", format4)
                sheet.write(row, 6, order.event_place.display_name if order.event_place else "Nil", format4)
                sheet.write(row, 7, order.total_attendees if order.total_attendees else "Nil", format4)
                sheet.write(row, 8, order.total_devotees_attended if order.total_devotees_attended else "Nil", format4)
                sheet.write(row, 9, order.desc if order.desc else "Nil", format4)
                sheet.write(row, 10, order.remark if order.remark else "Nil", format4)
                sheet.write(row, 11, order.state if order.state else "Nil", format4)
                row += 1

ActivityReportXlsx('report.sesa_requirement.activity_report_template_xlsx.xlsx', 'activity.report')