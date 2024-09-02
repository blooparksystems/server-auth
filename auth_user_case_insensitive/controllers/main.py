# Copyright 2015-2017 LasLabs Inc.
# Copyright 2021 Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class AuthSignupHomeCustom(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        """ Lower case login email to make sure no two users have same email for 
        login (even with different letter cases)"""
        res = super().get_auth_signup_qcontext()
        if res.get("login"):
            res.update({
                "login": res["login"].lower().strip()
            })
        return res
