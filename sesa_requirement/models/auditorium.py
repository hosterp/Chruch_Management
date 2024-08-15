from openerp import fields, models, api

class Auditorium(models.Model):
    _name = 'auditorum.fields'

    bookin_date=fields.Datetime('Booking Date')
    booking_details=fields.Text('Booking Details')
    ac_or_non=fields.Selection([('AC','AC'),('Non AC','Non AC')],'AC/Non AC')
    Generator=fields.Boolean('Generator')
    current=fields.Boolean('Current')
    water=fields.Boolean('Water')
    Chair=fields.Boolean('Chair')
    no_of_chair=fields.Integer('Number of chairs')
    sound_sysrem=fields.Boolean('Sound System')
    purpose=fields.Many2one('auditorium.purpose','Purpose')
    total_amount=fields.Float('Total Amount',compute='_compute_total_amount')
    advance=fields.Float('Advance Amount')
    balance=fields.Float('Balance Amount',compute='_compute_total_amount')
    auditorium_name=fields.Many2one('church.auditorium.name','Auditorium Name')
    event_place = fields.Many2one('church.place', "Chruch")
    invoice_ids=fields.One2many('auditorium.invoice','invoice_id')
    state = fields.Selection([('draft', 'Draft'), ('completed', 'Completed'),('postpone','Postpone'),('prepone','Prepone'), ('cancel', 'Cancelled')], default='draft',
                             string="Status")
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

    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain': {'event_place': [('event_district', '=', record.event_district)]}}

    @api.depends('invoice_ids.rent_amount')
    def _compute_total_amount(self):
        for record in self:
            total = sum(invoice.rent_amount for invoice in record.invoice_ids)
            record.total_amount = total
            record.balance=total-record.advance

    @api.model
    def default_get(self, fields):
        res = super(Auditorium, self).default_get(fields)
        active_id = self._context.get('active_id')
        if active_id:
            res['event_place'] = active_id
        return res

    @api.multi
    def action_completed(self):
        self.state = 'completed'

    @api.multi
    def action_postpone(self):
        self.state='postpone'

    @api.multi
    def action_prepone(self):
        self.state='prepone'

    @api.multi
    def action_cancel(self):
        self.state = 'cancel'
class AuditoriumDashboard(models.Model):
    _name = 'auditorium.dashboard'

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    image_kanban = fields.Binary('Image')
    place_count = fields.Integer(string='Place Count', compute='get_place_count_from_event_place')

    @api.depends('place_count')
    @api.one
    def get_place_count_from_event_place(self):
        event_place_model = self.env['event.place']
        place_record = event_place_model.search([], limit=1)
        self.place_count = place_record.place_count if place_record else 0

    def call_place(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'TV')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_auditorium')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_pta(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'PT')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_pta')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_kollam(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'KL')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_kl')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_al(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'AL')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_al')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_er(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'ER')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_er')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_id(self, cr, uid, ids, context):
    #     place_obj = self.pool.get('event.place')
    #     places = place_obj.search(cr, uid, [('event_district', '=', 'ID')], context=context)
    #     tvm_place_count = len(places)
    #     print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_id')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_ks(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'KS')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_ks')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_kt(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'KT')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_kt')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_kz(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'KZ')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_kz')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_ma(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'MA')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_ma')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_pl(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'PL')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_pl')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_ts(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'TS')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_ts')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_wa(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'WA')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_wa')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_kn(self, cr, uid, ids, context):
        # place_obj = self.pool.get('event.place')
        # places = place_obj.search(cr, uid, [('event_district', '=', 'KN')], context=context)
        # tvm_place_count = len(places)
        # print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_dashboard_places_kn')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_admin(self, cr, uid, ids, context):
        return

class ChurchDetails(models.Model):
    _name = 'church.place'
    _rec_name = 'church_place'

    church_place = fields.Char('Place')
    Church_Auditorium_Name = fields.Many2one('church.auditorium.name','Auditorium Name')
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

    def call_event(self, cr, uid, ids, context):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_auditorium_form')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

class AuditoriumPurpose(models.Model):
    _name = 'auditorium.purpose'
    _rec_name = 'purpose'

    purpose = fields.Char('Purpose')

class AuditoriumServices(models.Model):
    _name = 'auditorium.services'
    _rec_name = 'services'

    services=fields.Char('Extra services')

class AuditoriumInvoice(models.Model):
    _name = 'auditorium.invoice'

    invoice_id=fields.Many2one('auditorum.fields')
    services = fields.Many2one('auditorium.services','Extra services')
    amount=fields.Float('Amount')
    rent_amount=fields.Float('Rent Amount')

class Auditorium_name_model(models.Model):
    _name = 'church.auditorium.name'
    _rec_name = 'auditorium_name_church'

    auditorium_name_church = fields.Char('Auditorium Name')


