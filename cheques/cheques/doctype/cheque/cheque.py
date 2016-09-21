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


def inactivar_cheque(doc, event):
    """
    Inactivar el cheque en el caso de que el
    payment entry sea del payment_type Pay y
    el mode_of_payment.mode_of_payment sea Cheque.
    """
    if doc.payment_type == "Pay" and doc.mode_of_payment == 'Cheque':
        cheque = frappe.get_doc("Cheque", doc.cheque_en_cartera)
        cheque.estado = 'Inactivo'
        cheque.save()
