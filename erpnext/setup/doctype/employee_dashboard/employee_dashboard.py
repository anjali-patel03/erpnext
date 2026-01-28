# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeeDashboard(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		employee: DF.Data | None
		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_employee_dashboard: DF.Link | None
		rgt: DF.Int
	# end: auto-generated types

	pass
