Shortcodes
==========

Shortcodes is a simple Django app to include WordPress-like shortcode
functionality.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1.  Add "shortcodes" to your INSTALLED\_APPS setting like this:
    ```python
    INSTALLED_APPS = [
        ...
        'shortcodes',
    ]
    ```

2.  Create a shortcodes directory in your app to hold your parsers. Be
    sure to create a blank `__init__.py`.
3.  Parser functions should be defined like this:
    ```python
    def shortcodes_command(*args):
      ... parse your command here...

    return html
    ```

    Notice, no imports are required in your parser file.

4.  Load `expand_shortcodes` in your templates to have your shortcodes
    parsed.:
    ```
    {% load shortcodes %}
    ...
    {{ post.body|expand_shortcodes|safe }}
    ...
    ```
