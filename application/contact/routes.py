from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
from ..forms import ContactForm

# Blueprint Configuration
contact_bp = Blueprint(
    'contact_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        'contact.jinja2',
        form = form,
        title="Contact",
        description="Contact description"
    )