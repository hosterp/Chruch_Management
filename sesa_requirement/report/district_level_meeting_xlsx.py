try:
    from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    class ReportXlsx(object):
        def __init__(self, *args, **kwargs):
            pass
from datetime import datetime
class DistrictlevelDetailsReportXlsx(ReportXlsx):
    def generate_xlsx_report(self, workbook, data, lines):
        format = workbook.add_format({'font_size': 14, 'align': 'vcentre', 'bold': True})
        format1 = workbook.add_format({'font_size': 10, 'align': 'vcentre', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcentre', 'bold': False})
        format3 = workbook.add_format({'font_size': 13, 'align': 'vcentre', 'bold': True})
        format4 = workbook.add_format({'font_size': 8, 'align': 'vcentre', 'bold': False})

        sheet = workbook.add_worksheet('Activity')
        sheet.merge_range('G3:L3', "District level Meeting Report", format)
        # sheet.write(6, 1, "Sl No ", format1)
        sheet.write(6, 5, "Sl No ", format1)
        sheet.write(6, 6, "Date ", format1)
        sheet.write(6, 7, "Monthly Meetings ", format1)
        sheet.write(6, 8, "No. of Families Attend Family Narayana Seva", format1)
        sheet.write(6, 9, "No. of Saplings Planted", format1)
        sheet.write(6, 10, "No of samithies which added missing activities", format1)
        sheet.write(6, 11, "Programs/Events Planned", format1)

        row = 7
        slno = 1
        for order in lines:
            sheet.write(row, 5, slno, format4)
            sheet.write(row, 6, order.date if order.date else "Nil", format4)
            sheet.write(row, 7, order.no_monthily_meeting if order.no_monthily_meeting else "Nil", format4)
            sheet.write(row, 8, order.no_family if order.no_family else "Nil", format4)
            sheet.write(row, 9, order.no_saplings if order.no_saplings else "Nil", format4)
            sheet.write(row, 10, order.missing_activities if order.missing_activities else "Nil", format4)
            sheet.write(row, 11, order.events_planned if order.events_planned else "Nil", format4)
            row += 1
            slno += 1
DistrictlevelDetailsReportXlsx('report.sesa_requirement.district_level_details_report_template_xlsx.xlsx', 'event.district')