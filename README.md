# Roboco.dev

![Roboco dev Logo](https://github.com/user-attachments/assets/10ac2345-cc76-41b0-aa6a-b8149b3fb341)

Roboco.dev is a frontend guard for some of my internal services

## Dev

Everything here is inside `nix develop`.

### Tailwind

For dependencies, `cd theme/static_src`, then `npm i`.

For dev, from root, python `manage.py tailwind`.

### Web

For dependencies, `pip install -r requirements.txt`.

For dev, `python manage.py migrate`, then `python manage.py runserver 0.0.0.0:8080`.
