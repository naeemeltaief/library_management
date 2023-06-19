# Copyright (c) 2022, Naeem Eltaief and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMember(Document):
    def before_save (self):
        # this method will run every time a document is saved
        self.full_name = f'{self.first_name} {self.last_name or ""}'