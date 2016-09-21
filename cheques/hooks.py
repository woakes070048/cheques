# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cheques"
app_title = "Cheques"
app_publisher = "Diamo"
app_description = "App de manejo de cartera de cheques"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "contacto@diamo.com.ar"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cheques/css/cheques.css"
# app_include_js = "/assets/cheques/js/cheques.js"

# include js, css files in header of web template
# web_include_css = "/assets/cheques/css/cheques.css"
# web_include_js = "/assets/cheques/js/cheques.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cheques.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cheques.install.before_install"
# after_install = "cheques.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cheques.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

doc_events = {
    "Payment Entry": {
        "after_insert": "cheques.cheques.doctype.cheque.cheque.inactivar_cheque",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#   "all": [
#       "cheques.tasks.all"
#   ],
#   "daily": [
#       "cheques.tasks.daily"
#   ],
#   "hourly": [
#       "cheques.tasks.hourly"
#   ],
#   "weekly": [
#       "cheques.tasks.weekly"
#   ]
#   "monthly": [
#       "cheques.tasks.monthly"
#   ]
# }

# Testing
# -------

# before_tests = "cheques.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "frappe.desk.doctype.event.event.get_events": "cheques.event.get_events"
# }

