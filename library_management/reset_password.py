import frappe


@frappe.whitelist(allow_guest=True)
def forget_password(user_email):
    try:
        user = frappe.get_doc("User", user_email)
        user.reset_password(send_email=True)
        print(f"Password reset link sent to {user_email}.")
    except frappe.DoesNotExistError:
        print(f"User with email {user_email} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
