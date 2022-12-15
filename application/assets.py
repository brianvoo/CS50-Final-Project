# """Compile static assets."""
# from flask import current_app as app
# from flask_assets import Bundle

# def compile_assets(assets):
#     """Configure and build asset bundles."""

#     #Home assets bundle
#     home_style_bundle = Bundle(
#         'src/less/*.less',
#         'home_bp/home.less',
#         filters='less,cssmin',
#         output='dist/css/home.css',
#         extra={'rel': 'stylesheet/css'}
#     )
    
#     assets.register('home_styles', home_style_bundle)
#     if app.config['FLASK_ENV'] == 'development':
#         home_style_bundle.build()