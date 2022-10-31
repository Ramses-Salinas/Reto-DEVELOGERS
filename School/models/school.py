

from odoo import models, fields, api
from datetime import datetime,date

class subject (models.Model):

    _name = 'subject'
    _description = 'Salon de un curso'

    name = fields.Char(string="Nombre del curso")
    credits = fields.Integer(string="Creditos del curso")
    max_students = fields.Integer(string="Número máximo de estudiantes")
    active = fields.Boolean(string="¿Está el curso activo actualmente")
    teacher_id = fields.Many2one('teacher', string='Profesor')
    student_id = fields.Many2many('student')

class student (models.Model):

    _name = "student"
    _description = "Estdiante de un curso"

    name = fields.Char(string = "Nombre del estudiante")
    birth_date = fields.Date(string = "Cumpleaños del estudiante")
    age = fields.Integer(compute="_computed_age")
    final_exam_grade = fields.Float()
    merito= fields.Integer(string="Orden de merito del estudiante")

    @api.depends('birth_date')
    def _computed_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = (fields.datetime.now()-rec.birth_date).year
            else:
                rec.age = 0


class teacher (models.Model):

    _name = "teacher"
    _description = "Profesor de un curso"

    name = fields.Char()
    profile = fields.Text()

