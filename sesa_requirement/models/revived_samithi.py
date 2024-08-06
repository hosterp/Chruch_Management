from openerp import fields, models, api


class RevivedSamithidetailsReport(models.Model):
    _name = 'samithi.revived'

    desc = fields.Text("Details")
    date = fields.Datetime("Date of event")
    # event_place = fields.Char("Place")
    state = fields.Selection([('draft', 'Draft'), ('completed', 'Completed'), ('cancel', 'Cancelled')], default='draft',
                             string="Status")
    user = fields.Many2one('hr.employee')
    reporting_incharge = fields.Many2one('hr.employee', string="Reporting In-Charge")
    event_place = fields.Many2one('event.place', "Place")
    # event_district = fields.Many2one('event.district',"District")
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
    event_category = fields.Many2one('event.category', "Event Category")
    event_type = fields.Many2one('event.type')
    total_attendees = fields.Integer("Total Attendees")
    total_devotees_attended = fields.Integer("Total devotees attended")
    advance = fields.Integer("Advance")
    expense = fields.Integer("Expense")
    balance = fields.Integer("Balance")
    rem_expense = fields.Text("Remark")
    remark = fields.Text("Remark")
    attachment = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id3',
                                  string="Attachment",
                                  help='You can attach the copy of your document', copy=False)
    contact_details = fields.Char()
