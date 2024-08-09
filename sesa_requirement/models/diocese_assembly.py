from openerp import fields, models, api

class DioceseAssembly(models.Model):
    _name = 'diocese.assembly'


    name = fields.Char(string="Name")
    church_place = fields.Many2one('church.name','Place')
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


    church_name=fields.Many2one('chruch.model','Chruch Name')
    address=fields.Text('Address')
    vicar=fields.Char('Vicar')
    assist_vicar=fields.Char('Assistant Vicar')
    mobile=fields.Char('Mobile')
    email=fields.Char('Email ID')
    bishop_name=fields.Char('Bishop Name')


class PlaceCreate(models.Model):
    _name = 'church.name'
    _rec_name = 'church_place'

    church_place = fields.Char('Chruch')
class ChruchName(models.Model):
    _name = 'chruch.model'
    _rec_name = 'church_name'


    church_name = fields.Char('Chruch Name')