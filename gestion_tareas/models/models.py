# -*- coding: utf-8 -*-
from odoo import models, fields, api

class GestionTarea(models.Model):
    """Modelo para la gestión de tareas dentro de Odoo"""
    _name = 'gestion.tarea'
    _description = 'Gestión de tareas'

    # -------------------------------------------------------
    # CAMPOS
    # -------------------------------------------------------

    # Nombre de la tarea
    name = fields.Char(string='Nombre', required=True)

    # Prioridad (entero)
    priority = fields.Integer(string='Prioridad', default=0)

    # Si la tarea está realizada o no
    realizada = fields.Boolean(string='Realizada', default=False)

    # Campo calculado: urgente si prioridad > 10
    urgente = fields.Boolean(
        string='Urgente',
        compute='_compute_urgente',
        store=True
    )

    # -------------------------------------------------------
    # MÉTODO CALCULADO
    # -------------------------------------------------------
    @api.depends('priority')
    def _compute_urgente(self):
        """Marca como urgente si la prioridad es mayor a 10"""
        for record in self:
            record.urgente = record.priority > 10
