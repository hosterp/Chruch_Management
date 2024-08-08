from openerp import fields, models, api
import centenary_form


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # user_category = fields.Selection([('admin', 'Administrators'),
    #                                   ('TV', 'THIRUVANANTHAPURAM'),
    #                                   ('KL', 'KOLLAM'),
    #                                   ('PT', 'PATHANAMTHITTA'),
    #                                   ('AL', 'ALAPUZHA'),
    #                                   ('KT', 'KOTTAYAM'),
    #                                   ('ID', 'IDUKKI'),
    #                                   ('ER', 'ERNAKULAM'),
    #                                   ('TS', 'THRISSUR'),
    #                                   ('PL', 'PALAKKAD'),
    #                                   ('MA', 'MALAPPURAM'),
    #                                   ('KZ', 'KOZHIKODE'),
    #                                   ('WA', 'WAYANAD'),
    #                                   ('KN', 'KANNUR'),
    #                                   ('KS', 'KASARAGOD'),
    #                                   ], default='admin', string='District Category', required=True)
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
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", 'State', ondelete='restrict')
    zip = fields.Char('Zip', size=24, change_default=True)
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    aadhar_no = fields.Char(string="Aadhar No")
    event_place = fields.Many2one('event.place', "Place")
    position=fields.Char('Position')
    address=fields.Text('Address')
    # group_of_family=fields.Many2one()
    total_members=fields.Integer('Total Members')
    members_ids=fields.One2many('family.member','head_of_family_id')
    group_name_id=fields.Many2one(comodel_name='centenary.form')
    group_of_family = fields.Selection(selection='_get_group_name_options')

    @api.model
    def _get_group_name_options(self):
        # Fetch the options dynamically from `centenary.form`
        # This is an example and might require adjustments based on your requirements
        centenary_forms = self.env['centenary.form'].search([])
        options = [(form.group_name, form.group_name) for form in centenary_forms]
        return options

    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain': {'event_place': [('event_district', '=', record.event_district)]}}
    @api.onchange('address_id')
    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'street': address.street, 'street2': address.street2, 'city': address.city,
                              'state_id': address.state_id, 'zip': address.zip, 'country_id': address.country_id}}
        return {'value': {'street': '', 'street2': '', 'city': '', 'state_id': '', 'zip': '', 'country_id': ''}}


