from openerp import fields, models, api


class Event(models.Model):
    _name = 'event.event'
    _rec_name = 'user'

    # @api.model
    #    def default_get(self,field_list):
    #        res = super(Event,self).default_get(field_list)
    #        print "sssssssssssssssssssssssssssssssss",event_place
    #        res.update({'event_place':})
    #        return res

    @api.multi
    def action_completed(self):
        self.state = 'completed'

    @api.multi
    def action_cancel(self):
        self.state = 'cancel'

    # event = fields.Char("Event")
    desc = fields.Text("Details")
    date = fields.Datetime("Date of event")
    # event_place = fields.Char("Place")
    state = fields.Selection([('draft', 'Draft'), ('completed', 'Completed'), ('cancel', 'Cancelled')], default='draft',
                             string="Status")
    user = fields.Many2one('hr.employee')
    reporting_incharge = fields.Many2one('hr.employee',string="Reporting In-Charge")
    family_church = fields.Many2one('family_church_name.model', string='Church Name')
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
    total_devotees_attended = fields.Integer("Total devotees attended", compute='_compute_total',store=True)
    advance = fields.Integer("Advance")
    expense = fields.Integer("Expense")
    balance = fields.Integer("Balance")
    rem_expense = fields.Text("Remark")
    remark = fields.Text("Remark")
    attachment = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id3',
                                  string="Attachment",
                                  help='You can attach the copy of your document', copy=False)
    contact_details=fields.Char()
    revived_samithi=fields.Boolean(string="Revived Samithi")
    time = fields.Float(string="Time")
    guru = fields.Integer(string="Guru")
    male=fields.Integer(string='Male')
    female=fields.Integer(string='Female')
    youth=fields.Integer(string='Youth')

    @api.depends('male','female','youth')
    def _compute_total(self):
        for rec in self:
            rec.total_devotees_attended=rec.male+rec.female+rec.youth
    # event_category = fields.Selection([
    #     ('balvikas', 'Balvikas'),
    #     ('services', 'Services'),
    #     ('education', 'Education'),
    #     ('spiritual', 'Spiritual'),
    #     ('mahila', 'Mahila'),
    #     ('saiyouth', 'Sai Youth'),
    # ], string='Event Category')
    # category = fields.Boolean(string="Guru")

    # @api.onchange('event_category')
    # def onchange_category(self):
    #     if self.event_category.name =='Balvikas':
    #         self.category=  True
    #     else:
    #         self.category=False


    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain':{'event_place':[('event_district','=',record.event_district)]}}

    @api.onchange('event_category')
    def onchange_event_category(self):
        for record in self:
            if record.event_category:
                return {'domain':{'event_type':[('event_category','=',record.event_category.id)]}}


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id', string="Attachment",
                                  invisible=1)


class EventCategory(models.Model):
    _name = 'event.category'
    _rec_name = 'event_category'

    event_category = fields.Selection([
        ('balvikas', 'Balvikas'),
        ('services', 'Services'),
        ('education', 'Education'),
        ('spiritual', 'Spiritual'),
        ('mahila', 'Mahila'),
        ('saiyouth', 'Sai Youth'),
    ], string='Event Category')

class EventType(models.Model):
    _name = 'event.type'
    _rec_name = 'event_type'

    event_type = fields.Char("Event Type")
    event_category = fields.Many2one('event.category')


class EventExpenses(models.Model):
    _name = 'event.expense'

    event = fields.Many2one('event.event')
    advance = fields.Integer("Advance")
    expense = fields.Integer("Expense")
    balance = fields.Integer("Balance")
    rem_expense = fields.Text("Remark")
    state = fields.Selection([('draft', 'Draft'), ('paid', 'Paid')], default='draft',
                             string="Status")
    event_category = fields.Many2one('event.category', "Event Category")
    event_type = fields.Many2one('event.type')

# class Activity(models.Model):
#     _name = 'activity.activity'

#     user = fields.Many2one('event.user')
#     event_place = fields.Many2one('event.place',"Place")
# 	event_district = fields.Many2one('event.district',"District")
#     event_name = fields.Many2one('event.event',"Event")
# 	desc = fields.Text("Details")
#     date_event = fields.Date("Date of event") 




class Place(models.Model):
    _name = 'event.place'
    _rec_name = 'place'

    place = fields.Char('Place')
    church_place_name = fields.Many2one('family_church_name.model',string='Church Name')
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

    date=fields.Date(default=fields.Date.today,required='True')
    place_count = fields.Integer(string='Place Count', compute='_compute_place_count')
    district_place_count = fields.Integer(string='Place Count',compute='_compute_district_wise_count_place')

    @api.depends('event_district')
    def _compute_district_wise_count_place(self):
        for rec in self:
            if rec.event_district == 'TV':
                places = self.env['event.place'].search([('event_district', '=', 'TV')])
                rec.district_place_count= len(places)

            if rec.event_district == 'AL':
                places = self.env['event.place'].search([('event_district', '=', 'AL')])
                rec.district_place_count = len(places)

            if rec.event_district == 'ER':
                places = self.env['event.place'].search([('event_district', '=', 'ER')])
                rec.district_place_count = len(places)

            if rec.event_district == 'ID':
                places = self.env['event.place'].search([('event_district', '=', 'ID')])
                rec.district_place_count = len(places)

            if rec.event_district == 'KN':
                places = self.env['event.place'].search([('event_district', '=', 'KN')])
                rec.district_place_count = len(places)
            if rec.event_district == 'KS':
                places = self.env['event.place'].search([('event_district', '=', 'KS')])
                rec.district_place_count = len(places)

            if rec.event_district == 'KL':
                places = self.env['event.place'].search([('event_district', '=', 'KL')])
                rec.district_place_count = len(places)
            if rec.event_district == 'KT':
                places = self.env['event.place'].search([('event_district', '=', 'KT')])
                rec.district_place_count = len(places)
            if rec.event_district == 'KZ':
                places = self.env['event.place'].search([('event_district', '=', 'KZ')])
                rec.district_place_count = len(places)
            if rec.event_district == 'MA':
                places = self.env['event.place'].search([('event_district', '=', 'MA')])
                rec.district_place_count = len(places)
            if rec.event_district == 'PL':
                places = self.env['event.place'].search([('event_district', '=', 'PL')])
                rec.district_place_count = len(places)
            if rec.event_district == 'PT':
                places = self.env['event.place'].search([('event_district', '=', 'PT')])
                rec.district_place_count = len(places)
            if rec.event_district == 'TV':
                places = self.env['event.place'].search([('event_district', '=', 'TV')])
                rec.district_place_count = len(places)
            if rec.event_district == 'TS':
                places = self.env['event.place'].search([('event_district', '=', 'TS')])
                rec.district_place_count = len(places)
            if rec.event_district == 'WA':
                places = self.env['event.place'].search([('event_district', '=', 'WA')])
                rec.district_place_count = len(places)


    @api.depends('place')
    def _compute_place_count(self):
        for record in self:
            places = self.env['event.place'].search([])
            record.place_count = len(places)
            print(record.place_count, 'count.........................')


    def call_event(self, cr, uid, ids, context):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_activity')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


