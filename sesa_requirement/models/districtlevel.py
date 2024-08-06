from openerp import fields, models, api
from datetime import datetime
class DistrictLevelMeetings(models.Model):
    _name = 'event.district'

    date = fields.Datetime(string="Date", default=lambda self: fields.Date.context_today(self))
    events_planned = fields.Text(string="Programs/Events Planned")
    no_monthily_meeting = fields.Integer(string="Meetings")
    no_family = fields.Integer(string='No. of Families Attend Family Narayana Seva')
    no_saplings = fields.Integer(string='No. of Saplings Planted (Prematharu)')
    missing_activities = fields.Integer(string='Missing Activities')
    remark= fields.Text(string='Remarks')
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
    male = fields.Integer(string='Male')
    female = fields.Integer(string='Female')
    youth = fields.Integer(string='Youth')
    total_devotees_attended = fields.Integer("Total devotees attended", compute='_compute_total', store=True)
    event_category = fields.Many2one('event.category', "Meeting Category")
    event_type = fields.Many2one('event.type','Meeting Type')
    @api.depends('male', 'female', 'youth')
    def _compute_total(self):
        for rec in self:
            rec.total_devotees_attended = rec.male + rec.female + rec.youth

    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain': {'event_place': [('event_district', '=', record.event_district)]}}
    @api.onchange('event_category')
    def onchange_event_category(self):
        for record in self:
            if record.event_category:
                return {'domain': {'event_type': [('event_category', '=', record.event_category.id)]}}
    @api.multi
    def print_activity_district_level_meeting_details_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.district'),
             ('report_name', '=', 'sesa_requirement.activity_district_level_meeting_details_report_template',)])
        if data.download_filename:
            data.download_filename = 'DistrictLevelMeetingReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_district_level_meeting_details_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }

    @api.multi
    def print_District_level_details_report_xlsx_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        return {'type': 'ir.actions.report.xml',
                'report_name': 'sesa_requirement.district_level_details_report_template_xlsx.xlsx',
                'report_type': 'xlsx',
                'datas': datas
                }