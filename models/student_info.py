from odoo import api, fields, models, _
from odoo.exceptions import UserError
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
        
        
class StudentInfo(models.Model):
    _name = "ev.student.info"
    name = fields.Char(string='Student Name', required=True)
    father_name = fields.Char(string='Father Name', required=True)
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number', required=True)
    image = fields.Binary(string='Image')
    
    roll_number = fields.Char(string='Roll Number', readonly=True)
    student_class = fields.Many2one('ev.class', string='Class', required=True)
    semester = fields.Many2one('ev.semester', string='Semester', required=True)
    section = fields.Many2one('ev.section', string='Section', required=True)
    
    def generate_roll_number(self):
        _logger.debug("Class: %s SEMESTER %s SECTION %s", self.student_class.name, self.semester.name, self.section.name)
        if not self.student_class or not self.semester or not self.section:
            raise UserError(_("Please select Class, Semester and Section First"))
        self.roll_number =  str(self.student_class.name) + "-" + str(self.section.name) + "-" + self.env['ir.sequence'].next_by_code('ev.rn.seq')
        
    #First Assessment
    first_assessment_line_ids = fields.One2many(
        'ev.first.assessment.line.items',
        'student_info_id',
        string='First Assessment',
        copy=True
    )
    
    fa_overall_grade = fields.Char(string='Overall Grade', compute ='_fa_compute_total', store=True, readonly=True)
    fa_total_obtained_marks = fields.Float(string='Total Obtained Marks', compute ='_fa_compute_total', store=True,readonly=True)
    fa_total_percentage = fields.Float(string='Total Percentage', compute ='_fa_compute_total', store=True,readonly=True)
        
    @api.onchange('first_assessment_line_ids.obtained_marks')
    @api.depends('first_assessment_line_ids.obtained_marks')
    def _fa_compute_total(self):
        for assessment in self:
            total_obtained_marks = subject_marks = total_percentage = overall_grade = 0.0
            for line in assessment.first_assessment_line_ids:
                subject_marks += line.total_marks
                total_obtained_marks += line.obtained_marks
            if subject_marks > 0:
                total_percentage = total_obtained_marks / subject_marks
                overall_grade = get_grade(int(total_obtained_marks / len(assessment.first_assessment_line_ids)))
            assessment.update({
                'fa_total_obtained_marks': total_obtained_marks,
                'fa_total_percentage': total_percentage,
                'fa_overall_grade': overall_grade,
            })
            
    #Second Assessment
    second_assessment_line_ids = fields.One2many(
        'ev.second.assessment.line.items',
        'student_info_id',
        string='Second Assessment',
        copy=True
    )
    
    sa_overall_grade = fields.Char(string='Overall Grade', compute ='_sa_compute_total', store=True, readonly=True)
    sa_total_obtained_marks = fields.Float(string='Total Obtained Marks', compute ='_sa_compute_total', store=True,readonly=True)
    sa_total_percentage = fields.Float(string='Total Percentage', compute ='_sa_compute_total', store=True,readonly=True)
        
    @api.onchange('second_assessment_line_ids.obtained_marks')
    @api.depends('second_assessment_line_ids.obtained_marks')
    def _sa_compute_total(self):
        for assessment in self:
            total_obtained_marks = subject_marks = total_percentage = overall_grade = 0.0
            for line in assessment.second_assessment_line_ids:
                subject_marks += line.total_marks
                total_obtained_marks += line.obtained_marks
            if subject_marks > 0:
                total_percentage = total_obtained_marks / subject_marks
                overall_grade = get_grade(int(total_obtained_marks / len(assessment.second_assessment_line_ids)))
            assessment.update({
                'sa_total_obtained_marks': total_obtained_marks,
                'sa_total_percentage': total_percentage,
                'sa_overall_grade': overall_grade,
            })
            
    #Final Exam
    final_exam_line_ids = fields.One2many(
        'ev.final.exam.line.items',
        'student_info_id',
        string='Final Exam',
        copy=True
    )
    
    fe_overall_grade = fields.Char(string='Overall Grade', compute ='_fe_compute_total', store=True, readonly=True)
    fe_total_obtained_marks = fields.Float(string='Total Obtained Marks', compute ='_fe_compute_total', store=True,readonly=True)
    fe_total_percentage = fields.Float(string='Total Percentage', compute ='_fe_compute_total', store=True,readonly=True)
        
    @api.onchange('final_exam_line_ids.obtained_marks')
    @api.depends('final_exam_line_ids.obtained_marks')
    def _fe_compute_total(self):
        for assessment in self:
            total_obtained_marks = subject_marks = total_percentage = overall_grade = 0.0
            for line in assessment.final_exam_line_ids:
                subject_marks += line.total_marks
                total_obtained_marks += line.obtained_marks
            if subject_marks > 0:
                total_percentage = total_obtained_marks / subject_marks
                overall_grade = get_grade(int(total_obtained_marks / len(assessment.final_exam_line_ids)))
            assessment.update({
                'fe_total_obtained_marks': total_obtained_marks,
                'fe_total_percentage': total_percentage,
                'fe_overall_grade': overall_grade,
            })
    
    # TODO: VALIDATE email
    def validate_email(self):
        pass
    
    # TODO: VALIDATE phone number
    def validate_phone_no(self):
        pass
    
        
class StudentClass(models.Model):
    _name = "ev.class"
    
    name = fields.Char(string='Class', required=True)
    
class StudentSemester(models.Model):
    _name = "ev.semester"
    
    name = fields.Char(string='Semester', required=True)
    
    
class Section(models.Model):
    _name = "ev.section"
    
    name = fields.Char(string='Section', required=True) 
            
    
class Teacher(models.Model):
    _name = 'ev.teacher'
    
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number')
    
class Subject(models.Model):
    _name = 'ev.subject'
    
    name = fields.Char(string='Name', required=True)
    subject_marks = fields.Float(string='Subject Marks', required=True)
    
