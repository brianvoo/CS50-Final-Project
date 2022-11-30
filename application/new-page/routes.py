from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint Configuration
page_bp = Blueprint(
    'page_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@page_bp.route('/page', methods=['GET', 'POST'])
def home():
    """Homepage."""
    return render_template(
        'page.jinja2',
        title="Page",
        description="Page description"
    )