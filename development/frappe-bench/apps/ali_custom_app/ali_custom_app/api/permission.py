import frappe

def has_app_permission():
    """Check if user has permission to access the app"""
    # For now, allow all logged-in users
    return frappe.session.user != "Guest"
