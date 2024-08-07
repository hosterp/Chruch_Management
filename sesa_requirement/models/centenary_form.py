from openerp import fields, models, api


class CentenaryForm(models.Model):
    _name = 'centenary.form'

    sl=fields.Integer('Sl No')
    name=fields.Char('Name of the Child')
    connect_id=fields.Char('SaiConnect Id')
    phone=fields.Char('Mobile No')
    email=fields.Char('Email')
    date=fields.Date('Date')
    Category=fields.Many2one('centenary.celebration','Category' ,required='True')
    place_of_birth=fields.Char('Place of Birth of the Child')
    gender=fields.Selection([('Male','Male'),('Female','Female')])
    date_of_birth=fields.Date('Date of Birth')
    father=fields.Char('Father')
    mother=fields.Char('Mother')
    address_of_parents=fields.Text('Address of Parents')
    present_parish=fields.Char('Present Parish')
    home_parish=fields.Char('Home Parish')
    god_parents=fields.Text('Name and Address of God-parent')
    denomination=fields.Char('Denomination of God-parent')
    baptism_bool=fields.Boolean('Baptism')
    marrage_ids = fields.One2many('marrage.register', 'marrage_register_id', readonly=False,store=True)

    groom_name = fields.Char('Groom Name')
    bride_name = fields.Char('Bride Name')
    date_of_birth_marrage = fields.Date('Date of Birth')
    address_marrage = fields.Text('Present Address')
    chruch = fields.Char('Church and Parish')
    name_of_parents = fields.Char('Names of Parents')
    address_parents_marrage = fields.Text('Address of Parents')
    married_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'married before?')
    baptized_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'baptized?')
    holycommunion_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'person received Holy Communion?')
    certificate_vicar = fields.Selection([('YES', 'YES'), ('NO', 'NO')],
                                         "Is the parish vicar's certificate available?")
    place = fields.Char('Place where the marriage is to be conducted.')
    time_date = fields.Datetime('The time and date of the marriage.')
    marrage_bool = fields.Boolean('marrage')
    image_field = fields.Binary(string="Image", attachment=True)
    name_death_register=fields.Char('Name')
    parish_death_register=fields.Char('Parish')
    spouses_death_register=fields.Char('Husband/Wife Name')
    children_death_register=fields.Char('Children')
    date_of_birth_death_register=fields.Date('Date of Birth')
    date_of_death_register=fields.Date('Date of Death')
    funeral_date_time=fields.Datetime('funeral dates and times')
    death_bool = fields.Boolean('death register')

    @api.model
    def default_get(self, fields):
        res = super(CentenaryForm, self).default_get(fields)
        active_id = self._context.get('active_id')
        if active_id:
            res['Category'] = active_id
        return res

    @api.onchange('Category')
    def _onchange_category(self):
        baptism_category_id = self.env['centenary.celebration'].search([('name', '=', 'Baptism Register')], limit=1).id
        marrage_category_id = self.env['centenary.celebration'].search([('name', '=', 'Marrage Register')], limit=1).id
        death_bool_category_id = self.env['centenary.celebration'].search([('name', '=', 'Death Register')], limit=1).id

        if self.Category and self.Category.id == baptism_category_id:
            self.baptism_bool = True
        else:
            self.baptism_bool = False
        if self.Category and self.Category.id == marrage_category_id:
            self.marrage_bool = True
        else:
            self.marrage_bool = False

        if self.Category and self.Category.id == death_bool_category_id:
            self.death_bool = True
        else:
            self.death_bool = False

class MarrageRegisterLine(models.Model):
    _name = 'marrage.register'

    marrage_register_id=fields.Many2one('centenary.form')
    groom_name = fields.Char('Groom Name')
    bride_name = fields.Char('Bride Name')
    date_of_birth_marrage = fields.Date('Date of Birth')
    address_marrage = fields.Text('Present Address')
    chruch = fields.Char('Church and Parish')
    name_of_parents = fields.Char('Names of Parents')
    address_parents_marrage = fields.Text('Address of Parents')
    married_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'Has the person been married before?')
    baptized_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'Has the person been baptized?')
    holycommunion_before = fields.Selection([('YES', 'YES'), ('NO', 'NO')], 'Has the person received Holy Communion?')
    certificate_vicar = fields.Selection([('YES', 'YES'), ('NO', 'NO')],
                                         'Has the certificate from the vicar of the concerned parish been produced?')
    place = fields.Char('Place where the marriage is to be conducted.')
    time_date = fields.Datetime('The time and date of the marriage.')

