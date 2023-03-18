from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint Configuration
projects_bp = Blueprint(
    'projects_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@projects_bp.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    """Projects page."""
    return render_template(
        'projects.jinja2',
        title="Project page.",
        description="Your project."
    )