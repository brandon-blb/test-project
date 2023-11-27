from odoo import xyz

from odoo import models, fields, api, exceptions, tools, _

import logging
_logger = logging.getLogger(__name__)

class TestProject(models.Model):

    _name = 'test.project'
    _description = 'Test Project'

    name = fields.Char(string="Name")
    surname = fields.Char(string="Surname")
    id_number = fields.Char(string="ID Number")