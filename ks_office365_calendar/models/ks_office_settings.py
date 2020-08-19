from odoo import models, fields, api, _


class OfficeSettings(models.Model):
    _inherit = "ks_office365.settings"

    ks_sync_individual = fields.Boolean("Realtime Syncing (Export)", default=False,
                                        help="This will allow you to sync an event automatically when it is created or "
                                             "updated in odoo calendar and will send instant email notification to the "
                                             "attendees of the event.")
    ks_create_meeting_invite = fields.Boolean("Create Meeting Invitation")
    ks_new_meeting_invite = fields.Boolean("New Meeting")
    ks_update_meeting_invite = fields.Boolean("Update Meeting")

