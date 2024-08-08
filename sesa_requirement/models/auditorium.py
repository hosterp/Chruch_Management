from openerp import fields, models, api

class Auditorium(models.Model):
    _name = 'auditorum.fields'

    bookin_date=fields.Char('Booking Date')
    booking_details=fields.Text('Booking Details')
    ac_or_non=fields.Boolean('AC/Non AC')
    Generator=fields.Boolean('Generator')
    current=fields.Boolean('Current')
    water=fields.Boolean('Water')
    Chair=fields.Boolean('Chair')
    no_of_chair=fields.Integer('Number of chairs')
    sound_sysrem=fields.Boolean('Sound System')
    purpose=fields.Char('Purpose')
    total_amount=fields.Float('Total Amount')
    event_place = fields.Many2one('church.place', "Chruch")

    @api.model
    def default_get(self, fields):
        res = super(Auditorium, self).default_get(fields)
        active_id = self._context.get('active_id')
        if active_id:
            res['event_place'] = active_id
        return res

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