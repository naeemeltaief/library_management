import frappe

@frappe.whitelist(
    allow_guest=True
)
def get_article_details():
    return frappe.db.sql("""select image,name,author,publisher,status from `tabArticle` WHERE owner='Administrator';""", as_dict=True)




