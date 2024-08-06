from openerp import fields, models, api



class CentenaryCelebrations(models.Model):
    _name = 'centenary.celebration'

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    image_kanban = fields.Binary('Image')

    def call_event_form(self, cr, uid, ids, context):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_activity_centenary_form')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result







