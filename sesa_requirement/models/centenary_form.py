from openerp import fields, models, api


class CentenaryForm(models.Model):
    _name = 'centenary.form'

    sl=fields.Integer('Sl No')
    name=fields.Char('Name')
    connect_id=fields.Char('SaiConnect Id')
    phone=fields.Char('Mobile No')
    email=fields.Char('Email SI')
    date=fields.Date('Date')
    Category=fields.Many2one('centenary.celebration','Category' ,required='True')


