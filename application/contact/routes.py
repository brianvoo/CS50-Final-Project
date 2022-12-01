from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint Configuration
contact_bp = Blueprint(
    'contact_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def home():
    """Contact Page."""
    return render_template(
        'contact.jinja2',
        title="Contact",
        description="Contact description"
    )