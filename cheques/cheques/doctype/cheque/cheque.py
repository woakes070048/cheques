# -*- coding: utf-8 -*-
# Copyright (c) 2015, Diamo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Cheque(Document):
    pass


@frappe.whitelist()
def get_datos_cheque(nro_cheque):
    return frappe.get_doc("Cheque", nro_cheque)
