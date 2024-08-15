from openerp import models, fields

class FamilyMember(models.Model):
    _name = 'family.member'
    _description = 'Family Member'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    age=fields.Integer(string='Age',required=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',required=True)
    phone_no=fields.Char(string='Phone No')
    email=fields.Char(string='Email')
    relation = fields.Selection([
        ('hof','HOF'),
        ('spouse', 'Spouse'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('other', 'Other')
    ], string='Relation to Head of Family', required=True)
    head_of_family_id = fields.Many2one('hr.employee', string='Head of Family', required=True)
