import frappe
from frappe import ValidationError


@frappe.whitelist(allow_guest=True)
def signup(username, email, password, full_name, role):
    try:
        # Check if email, username, and full name are already used
        if frappe.get_value("User", {"email": email}):
            raise ValidationError("Email address is already in use.")

        if frappe.get_value("User", {"username": username}):
            raise ValidationError("Username is already in use.")

        if frappe.get_value("User", {"full_name": full_name}):
            raise ValidationError("Full name is already in use.")

        # Perform validation checks on the input data
        if not username or not email or not password or not full_name or not role:
            raise ValidationError('All fields are required.')

        if not frappe.db.exists("Role", role):
            raise ValidationError('Role does not exist.')

        # Create a new User document
        user = frappe.new_doc("User")
        user.email = email
        user.username = username
        user.full_name = full_name
        user.first_name = full_name.split(' ')[0]
        user.last_name = full_name.split(' ')[-1]
        user.new_password = password
        user.append_roles(role)
        user.api_key = frappe.generate_hash(length=20)
        user.api_secret = frappe.generate_hash(length=20)

        user.insert(ignore_permissions=True)

        return {
            'status': 'success',
            'message': 'User created successfully.'
        }

    except ValidationError as e:
        frappe.response.http_status_code = 400
        return {
            'status': 'error',
            'message': str(e)
        }

    except Exception as e:
        frappe.response.http_status_code = 500
        return {
            'status': 'error',
            'message': 'Failed to create user. Error: {}'.format(str(e))
        }
