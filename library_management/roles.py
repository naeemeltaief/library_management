import frappe


@frappe.whitelist()
def get_roles():
    all_roles = frappe.get_roles()
    filtered_roles = [role for role in all_roles if frappe.get_value("Role", role, "is_custom") == 1]
    return filtered_roles
