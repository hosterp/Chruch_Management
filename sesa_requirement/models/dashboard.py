from openerp import fields, models, api
from datetime import date
from datetime import  datetime,timedelta

from openerp.exceptions import ValidationError


class HRDashboard(models.Model):
    _name = 'event.dashboard'

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    image_kanban=fields.Binary('Image')
    place_count = fields.Integer(string='Place Count', compute='get_place_count_from_event_place')

    @api.depends('place_count')
    @api.one
    def get_place_count_from_event_place(self):
        event_place_model = self.env['event.place']
        place_record = event_place_model.search([], limit=1)
        self.place_count = place_record.place_count if place_record else 0



    def call_place(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'TV')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count,'count................')
        mod_obj = self.pool.get('ir.model.data')
    	act_obj = self.pool.get('ir.actions.act_window')
    	result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places')
    	id = result and result[1] or False
    	result = act_obj.read(cr, uid, [id], context=context)[0]
    	return result


    def call_pta(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'PT')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_pta')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result


    def call_kollam(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kl')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_al(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'AL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_al')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_er(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'ER')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_er')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_id(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'ID')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_id')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_ks(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KS')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ks')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_kt(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KT')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kt')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_kz(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KZ')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kz')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_ma(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'MA')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ma')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_pl(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'PL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_pl')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_ts(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'TS')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ts')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_wa(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'WA')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_wa')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result
    
    def call_kn(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KN')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kn')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result

    def call_admin(self,cr,uid,ids,context):
        return