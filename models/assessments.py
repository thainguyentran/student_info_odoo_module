from odoo import api, fields, models
from odoo.exceptions import UserError, _

import logging

_logger = logging.getLogger(__name__)

def get_grade(marks):
    if marks>=90 and marks<=100:
        return 'A+'
    elif marks>= 80 and marks<90:
        return 'A'
    elif marks>=70 and marks<80:
        return 'B'
    elif marks>=60 and marks<70:
        return 'C'
    elif marks>=50 and marks<60:
        return 'D'
    elif marks>=40 and marks<50:
        return 'E'
    else:
        return 'F'
        
        
class FirstAssestmentItems(models.Model):
    _name = "ev.first.assessment.line.items"
    
    student_info_id = fields.Many2one('ev.student.info', string="Student")
    subject_id = fields.Many2one('ev.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('ev.teacher', string='Teacher', required=True)
    total_marks = fields.Float(string='Total Marks', related='subject_id.subject_marks')
    obtained_marks = fields.Float(string='Obtained Marks', required=True)
    
    percentage = fields.Float(string='Percentage', compute='_compute_marks', store=True, readonly=True)
    grade = fields.Char(string='Grade', compute='_compute_marks', store=True, readonly=True)
    
    @api.onchange('obtained_marks')
    @api.depends('obtained_marks')
    def _compute_marks(self):
        for line in self:
            if line.total_marks > 0 and line.obtained_marks:
                if line.obtained_marks > line.total_marks:
                    raise UserError(_("Obtained Marks cannot be bigger than Total Marks"))
                line.update({
                    'percentage' : line.obtained_marks / line.total_marks,
                    'grade' : get_grade(line.obtained_marks)
                })


class SecondAssestmentItems(models.Model):
    _name = "ev.second.assessment.line.items"
    
    student_info_id = fields.Many2one('ev.student.info', string="Student")
    subject_id = fields.Many2one('ev.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('ev.teacher', string='Teacher', required=True)
    total_marks = fields.Float(string='Total Marks', related='subject_id.subject_marks')
    obtained_marks = fields.Float(string='Obtained Marks', required=True)
    
    percentage = fields.Float(string='Percentage', compute='_compute_marks', store=True, readonly=True)
    grade = fields.Char(string='Grade', compute='_compute_marks', store=True, readonly=True)
    
    @api.onchange('obtained_marks')
    @api.depends('obtained_marks')
    def _compute_marks(self):
        for line in self:
            if line.total_marks > 0 and line.obtained_marks:
                if line.obtained_marks > line.total_marks:
                    raise UserError(_("Obtained Marks cannot be bigger than Total Marks"))
                line.update({
                    'percentage' : line.obtained_marks / line.total_marks,
                    'grade' : get_grade(line.obtained_marks)
                })
                
class FinalExamItems(models.Model):
    _name = "ev.final.exam.line.items"
    
    student_info_id = fields.Many2one('ev.student.info', string="Student")
    subject_id = fields.Many2one('ev.subject', string='Subject', required=True)
    teacher_id = fields.Many2one('ev.teacher', string='Teacher', required=True)
    total_marks = fields.Float(string='Total Marks', related='subject_id.subject_marks')
    obtained_marks = fields.Float(string='Obtained Marks', required=True)
    
    percentage = fields.Float(string='Percentage', compute='_compute_marks', store=True, readonly=True)
    grade = fields.Char(string='Grade', compute='_compute_marks', store=True, readonly=True)
    
    @api.onchange('obtained_marks')
    @api.depends('obtained_marks')
    def _compute_marks(self):
        for line in self:
            if line.total_marks > 0 and line.obtained_marks:
                if line.obtained_marks > line.total_marks:
                    raise UserError(_("Obtained Marks cannot be bigger than Total Marks"))
                line.update({
                    'percentage' : line.obtained_marks / line.total_marks,
                    'grade' : get_grade(line.obtained_marks)
                })