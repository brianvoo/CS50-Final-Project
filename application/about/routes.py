from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint Configuration
about_bp = Blueprint(
    'about_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@about_bp.route('/about', methods=['GET', 'POST'])
def home():
    """Homepage."""
    return render_template(
        'About.jinja2',
        title="About",
        description="About description"
    )