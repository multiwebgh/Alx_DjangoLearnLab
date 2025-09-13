# Permissions & Groups Setup

- **Viewers Group** → has `can_view`
- **Editors Group** → has `can_create`, `can_edit`
- **Admins Group** → has `can_view`, `can_create`, `can_edit`, `can_delete`

Views in `views.py` enforce these permissions using `@permission_required`.
