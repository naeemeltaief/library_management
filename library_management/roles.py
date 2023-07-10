import frappe


@frappe.whitelist(allow_guest=True)
def get_roles():
    custom_roles = frappe.get_all("Role", filters={"is_custom": 1}, fields=["name"])
    return custom_roles
