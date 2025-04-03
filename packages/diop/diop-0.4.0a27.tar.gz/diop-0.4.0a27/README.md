# `D`esktop `I`nfrastructure `Op`erations

`Diop` is a [Django-based][www-django] web application to manage a Virtual
Desktop Infrastructure based on *Citrix Virtual Apps and Desktops* (CVAD).

## 🧱 Components and functional dependencies

The project itself consists of these components:

- The Diop core app.
- Several Diop task queue workers.

To make it fly, several external pieces are required:

- A MySQL database (others may work but are not tested).
- Connection to a [PSyTricks / ResTricks][www-psytricks] interface to fetch
  status information from the CVAD instance and trigger actions.
- Access to a PPMS booking system instance (performed through the
  [pyppms][www-pyppms] package).

## 📝🔩🔧 Development Setup

Please refer to the [DEVELOPMENT](./DEVELOPMENT.md) instructions.

[www-django]: https://www.djangoproject.com/
[www-psytricks]: https://pypi.org/project/psytricks/
[www-pyppms]: https://pypi.org/project/pyppms/
