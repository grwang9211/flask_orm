def register_routes(api, app, root="api"):
    from app.issue import register_routes as attach_issue
    from app.user import register_routes as attach_user
    from app.company import register_routes as attach_company
    from app.fizz import register_routes as attach_fizz
    from app.other_api import register_routes as attach_other_api
    from app.third_party.app import create_bp

    # Add routes
    attach_issue(api, app)
    attach_user(api, app)
    attach_company(api, app)
    attach_fizz(api, app)
    attach_other_api(api, app)
    app.register_blueprint(create_bp(), url_prefix="/third_party")
