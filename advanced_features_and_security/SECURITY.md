# Security measures implemented

- DEBUG set to False for production.
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE set to True.
- SECURE_BROWSER_XSS_FILTER and SECURE_CONTENT_TYPE_NOSNIFF enabled.
- X_FRAME_OPTIONS set to DENY.
- All forms include `{% csrf_token %}`.
- Views use Django forms and ORM (no raw SQL).
- Content Security Policy (CSP) applied using django-csp or middleware.
- Permissions enforced with `@permission_required` and groups used for role-based access.
