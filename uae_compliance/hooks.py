from . import __version__ as app_version

app_name = "uae_compliance"
app_title = "UAE Compliance"
app_publisher = "Frappe Technologies Private Limited"
app_description = " ERPNext App that includes regional compliance configuration for UAE"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "diksha@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/uae_compliance/css/uae_compliance.css"
# app_include_js = "/assets/uae_compliance/js/uae_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/uae_compliance/css/uae_compliance.css"
# web_include_js = "/assets/uae_compliance/js/uae_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "uae_compliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "uae_compliance.utils.jinja_methods",
# 	"filters": "uae_compliance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "uae_compliance.install.before_install"
after_install = "uae_compliance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "uae_compliance.uninstall.before_uninstall"
# after_uninstall = "uae_compliance.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "uae_compliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Purchase Invoice": {
		"validate": [
			"uae_compliance.utils.validate_reverse_charge_transaction",
			"uae_compliance.utils.update_itc_availed_fields",
			"uae_compliance.utils.update_grand_total_for_rcm",
			"uae_compliance.utils.validate_returns",
			"uae_compliance.utils.update_taxable_values"
		]
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"uae_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"uae_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"uae_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"uae_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"uae_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "uae_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "uae_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "uae_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"uae_compliance.auth.validate"
# ]

regional_overrides = {
	'United Arab Emirates': {
		'erpnext.controllers.taxes_and_totals.update_itemised_tax_data': 'uae_compliance.utils.update_itemised_tax_data',
		'erpnext.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries': 'uae_compliance.utils.make_regional_gl_entries',
	},
}