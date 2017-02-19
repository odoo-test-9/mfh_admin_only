# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#~ from openerp import models, fields, api

# ------------------------
# Models
# ------------------------

from openerp import SUPERUSER_ID
from openerp.osv import fields, osv
from openerp.tools.translate import _

class dropbox_config_settings(osv.TransientModel):
    _name = 'dropbox.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'user_dropbox': fields.char('Usuario', help="Login"),
        'pass_dropbox': fields.char('Contraseña', help="Password")

    }
    def set_user_defaults(self, cr, uid, ids, context=None):
        login_user = self.browse(cr, uid, ids, context=context).user_dropbox
        res = self.pool.get('ir.values').set_default(cr, SUPERUSER_ID, 'dropbox.config.settings', 'user_dropbox', login_user)
        return res
        
    def set_passw_defaults(self, cr, uid, ids, context=None):
        login_passw = self.browse(cr, uid, ids, context=context).pass_dropbox
        res = self.pool.get('ir.values').set_default(cr, SUPERUSER_ID, 'dropbox.config.settings', 'pass_dropbox', login_passw)
        return res


#~ class dropbox_config_settings(models.Model):
    #~ _inherit = 'res.config.settings'
    #~ _name = 'dropbox.config.settings'

    #~ user_dropbox = fields.Char(string="Usuario", help="Login")
    #~ pass_dropbox = fields.Char(string="Contraseña", help="Password")
   
    #~ @api.multi
    #~ def set_defaults(self):
        #~ ir_values = self.env['ir.values']
        #~ value = self.ensure_one()
        #~ if not self.env.user._is_admin():
            #~ raise AccessError(_("Only administrators can change the settings"))
        #~ user_dropbox = value.user_dropbox
        #~ pass_dropbox = value.pass_dropbox
    
        #~ ir_values.sudo().set_default('dropbox.config', 'user_dropbox', user_dropbox)
        #~ ir_values.sudo().set_default('dropbox.config', 'pass_dropbox', pass_dropbox)
   
        #~ res = super(dropbox_config_settings, self).set_defaults()
        #~ return res

    #~ }
