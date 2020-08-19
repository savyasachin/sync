from odoo import models, fields, api, http, _


class KsOffice365Root(models.Model):
    _name = 'ks.office.res.users'
    _rec_name = 'ks_res_user_id'
    _description = "Office 365 Res Users"

    ks_res_user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    ks_code = fields.Char(related='ks_res_user_id.ks_code', store=True)
    ks_scope = fields.Char(related='ks_res_user_id.ks_scope', store=True)
    ks_auth_token = fields.Char(related='ks_res_user_id.ks_auth_token', store=True)
    ks_auth_refresh_token = fields.Char(related='ks_res_user_id.ks_auth_refresh_token', store=True)
    ks_auth_user_name = fields.Char(related='ks_res_user_id.ks_auth_user_name', store=True, readonly=True)
    ks_auth_user_email = fields.Char(related='ks_res_user_id.ks_auth_user_email', store=True, readonly=True)

    ks_is_login_user = fields.Boolean(compute="ks_is_current_user")

    def ks_get_authentication_code(self):
        return self.ks_res_user_id.sudo().get_authentication_code()

    def ks_refresh_token(self):
        return self.ks_res_user_id.sudo().refresh_token()

    def ks_office_root_action(self):
        ks_user = self.env['ks.office.res.users'].search([('ks_res_user_id', '=', self.env.user.id)])
        return {
            'name': _('Office user form'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ks.office.res.users',
            'view_id': self.env.ref('ks_office365_base.ks_office365_root_users_form').id,
            'res_id': ks_user.id,
            'context': self.env.context,
        }

    def ks_clear_token(self):
        self.ks_res_user_id.sudo().ks_clear_token()

    """ For making Token page invisible """
    def ks_is_current_user(self):
        if self.id == self.env.user.id:
            self.ks_is_login_user = True
        else:
            self.ks_is_login_user = False
