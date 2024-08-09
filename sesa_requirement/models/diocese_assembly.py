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



class ChruchCreate(models.Model):
    _name = 'church.name'
    _rec_name = 'church_place'

    church_place = fields.Char('Chruch')