# Django Modern User

Django Modern User is a custom user model for Django projects that replaces the default `username` field with a case-insensitive `email` field for authentication, and removes the requirement for first and last names. This model aims to provide a more practical and modern approach to user management in Django.

## Installation

> [!IMPORTANT]
> The instructions below are intended for integrating `django-modern-user` into new projects. Incorporating this package into existing projects, especially those with existing user data, can be complex and requires careful database migrations and potentially some code adjustments. The integration into projects with existing users is beyond the scope of this documentation.

1. Install `django-modern-user` via pip:
   ```bash
   python -m pip install django-modern-user
   ```

2. Add `django_modern_user` to your `INSTALLED_APPS` in your Django settings:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'django_modern_user',
   ]
   ```

3. Create a new user model in your project by subclassing `django_modern_user.ModernUser`:
   ```python
   # In your models.py
   from django_modern_user.models import ModernUser

   class CustomUser(ModernUser):
       pass
   ```

4. Update your Django settings to use your new user model:
   ```python
   AUTH_USER_MODEL = "<your_app_name>.CustomUser"
   ```

5. To use the provided `ModernUserAdmin` class in your Django admin site, you can subclass it in your `admin.py` file:
   ```python
   from django.contrib import admin
   from django_modern_user.admin import ModernUserAdmin
   from .models import CustomUser

   @admin.register(CustomUser)
   class CustomUserAdmin(ModernUserAdmin):
       pass
   ```

6. Run migrations to create the necessary database table:
   ```bash
   python manage.py migrate
   ```

This setup allows you to further customize your user model and admin interface while benefiting from the features provided by `django-modern-user`.

## Usage

With `django-modern-user` and your subclassed user model, authentication is done using the email field. The email field is case-insensitive, ensuring a user-friendly authentication process.

First, ensure that you have created a subclass of `ModernUser` as described in the [Installation](#installation) section.

Here's an example of how you might create a new user with your subclassed user model:

```python
# Assume you have defined CustomUser in your models.py
from <your_app_name>.models import CustomUser

# Create a new user
user = CustomUser.objects.create_user(email='example@example.com', password='password123')

# Create a superuser
superuser = CustomUser.objects.create_superuser(email='admin@example.com', password='password123')
```

In this example, replace <your_app_name> with the name of your Django app. This way, you're creating users with your project-specific user model, which subclasses django-modern-user's ModernUser.

## Custom User Manager

`django-modern-user` comes with a custom user manager, `ModernUserManager`, which handles user creation and ensures the email field is used for authentication.

## Contributing

Feel free to fork the project, open a PR, or submit an issue if you find bugs or have suggestions for improvements.

### How to release a new version

1. Commit any code changes.
2. Run `poetry version <version>` to update the version number in `pyproject.toml`. `<version>` can be `patch`, `minor`, or `major`.
3. Commit the new version with a the message as it's version number (example: `v4.0.0`).
4. Tag the commit with the version number (example: `git tag v4.0.0`).
5. Push the commit and tag to the repository (example: `git push && git push --tags`).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
