DJGUL: What's new on Django 1.5 (Marc Tamlyn)
=============================================

:date: 2013-12-3 21:30
:tags: djugl, march, django, 1.5

In this talk Marc Tamlyn (`@mjtamlyn <https://twitter.com/mjtamlyn>`_) was
explained to us what where all the change in the new "major" version of django,
django 1.5.

As always you can find the original talks in Internet:
https://speakerdeck.com/mjtamlyn/whats-new-in-django-1-dot-5

Major changes
-------------

- Pluggable user models. Which means that you will need some proxy classes
  magic or similar to extend your users.
- Python 3 support.
- Security improvements.
- ``StreamingHTTPResponse``.
- The {% url %} tag change his behaviour. It seems that using ``future`` you
  can had this behaviour before (1.3?) but... who use ``future``? :)

You can see a better explanation of this points here:

Pluggable user models
~~~~~~~~~~~~~~~~~~~~~

- Solution to schema chnages on the default user model.
- ``AUTH_PROFILE_MODEL`` becomes ``AUTH_USER_MODEL``.

This was a problem since 2014 when Django was created.

If you want to change something this is your first start point:
``auth.models.AbstractUser``. If you want to go one step forward:
``auth.models.PermissionMixin`` & ``auth.models.AbstractBaseUse``.

You can override ``USERNAME_FIELD`` too, to override the standard username
field of the model.

``contrib.admin`` integration. Which I didn't try yet (Álex) but if it works as
they said, it should be just amazing!

Python 3
~~~~~~~~

- 3.2 and 3.3 supported, but python 2.5 was gone.
- Not yet "production ready". You will probably be ok, but it's up to you to
  give it a chance.
- Upgrade your third party apps! You will be able to import compatibility apps
  from django that will help you using this apps.

**Caveats**: MySQL, PIL, Selenium... this all need to be migrated also :(

Armin (`@mitsuhiko <https://twitter.com/mitsuhiko>`_) said that PIL is already
supported \o/


Security
~~~~~~~~

``ALLOWED_HOSTS`` is a whitelist backported to django 1.3.x and 1.4.x but
required in 1.5.

You can read the django documentation about this here:
https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts


StreamingHTTPResponse
~~~~~~~~~~~~~~~~~~~~~

Fixes the handling of streaming http responses. Instead use the normal
``.content`` you need to use ``streamed_content`` if you want to access to the
content.

{% url %}
~~~~~~~~~

- The API was wrong, it was fixed in 1.3 loading from future... but hey, who made that? :)
- Old style is actually gone now.

More new things
---------------

- Caching of related model instances... this will transparently improve the
  performance of your site a lot. It was one of the biggest causes of delay on
  this new django version.
- ``update_fields`` is a new variable received on the save method that allows you
  to know what are the fileds that has changed.
- PostGIS 2.0 is supported now.
- ``{% verbatim %}`` that allows a little bit more easy javascript (for
  example) development in django templates.

Backwards incompatibilities (perhaps)
-------------------------------------

- Context in various class views can break.
- Simplejson could cause incompatibilities since python 2.5 was removed from
  django compatibility.
- Session not saved on 500 errors.

Testing
~~~~~~~

- ``OPTIONS``, ``PUT`` and ``DELETE``.
- DB flushing, it was move from the end of the test to the beginning of the test.
- Ordering of test executing changes, this shouldn't matter because your test
  will be always non dependant, right?
- contrib.localflavor has some changes too.
- contrib.markup usually marked all at safe and hope for the best, now it's not
  doing it.
- ``django-admin.py cleanup`` clear up the sessions, actually, now it's called
  ``django-admin.py clearsessions``.
- depth argument to select related, to don't follow all the possible joins.


Nice things you may have missed
-------------------------------

- ``LOGIN_URL`` can be an url name now, and django will make the ``reverse()``
  for you.
- True, False and None in templates.
- ``user_login_failed`` signal.
- ``assertXMLEqual()``.
- ``index_together``, create a indexes with several fields.
- admin lists customisable by request.
- ``django.utils.text.slugify`` get an string in and returns an slug for you.
