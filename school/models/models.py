from odoo import models, fields, api

# 1. Clase para almacenar a los estudiantes 
class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Estudiante'

    # Campos obligatorios (required) 
    name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    id_number = fields.Char(string="DNI/NIE", required=True)
    
    birthdate = fields.Date(string="Fecha de Nacimiento")
    active = fields.Boolean(string="Activo", default=True)
    age = fields.Integer(string="Edad")
    
    # Relaciones del UML
    class_id = fields.Many2one('school.class', string="Clase")
    event_ids = fields.Many2many('school.event', string="Eventos")

    # Restricción de unicidad para el DNI 
    _sql_constraints = [
        ('dni_unique', 'unique(id_number)', '¡El DNI/NIE ya existe en la base de datos!')
    ]

# 2. Clase para almacenar las clases 
class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Clase Escolar'

    name = fields.Char(string="Nombre de la Clase", required=True) 
    grade = fields.Selection([
        ('first', 'Primero'), 
        ('second', 'Segundo'), 
        ('third', 'Tercero'), 
        ('fourth', 'Cuarto')
    ], string="Grado")
    date_begin = fields.Date(string="Fecha Inicio")
    date_end = fields.Date(string="Fecha Fin")
    student_number = fields.Integer(string="Número de Estudiantes")
    description = fields.Text(string="Descripción")

    # Los profesores usan la clase hr_employee
    tutor_id = fields.Many2one('hr.employee', string="Tutor")
    student_ids = fields.One2many('school.student', 'class_id', string="Estudiantes")

# 3. Clase para almacenar los eventos 
class SchoolEvent(models.Model):
    _name = 'school.event'
    _description = 'Evento Escolar'
    
    # Ordenar por el campo fecha 
    _order = 'date desc'

    name = fields.Char(string="Nombre del Evento")
    date = fields.Date(string="Fecha", required=True)
    type = fields.Selection([
        ('absence', 'Ausencia'), 
        ('delay', 'Retraso'), 
        ('congratulations', 'Felicidades'), 
        ('behavior', 'Comportamiento')
    ], string="Tipo")
    description = fields.Text(string="Descripción")
    
    # Relación Many2many con estudiantes
    student_ids = fields.Many2many('school.student', string="Estudiantes implicados")