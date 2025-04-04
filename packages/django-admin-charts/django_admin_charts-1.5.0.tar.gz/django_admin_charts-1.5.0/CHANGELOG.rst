Changelog
=========

1.5.0 (2025-04-03)
------------------
* project configuration fixes and updates
* fix none choice in charts
* improve output of recalculate_charts management commands - print process durations
* fix #78: No graph on home page admin only chart header


1.4.0 (2024-08-02)
------------------

* added DashboardStats.queryset_modifiers to allow to modify queryset before it is used in chart, e.g. to add prefetch_related, filters or execute annotation functions. Fixed criteria are now deprecated in favour of queryset_modifiers.
* values in divided chart now are filtered by other criteria choices
* removed support for other JSONFields than Django's native JSONField, removed ADMIN_CHARTS_USE_JSONFIELD setting
* admin charts are loaded by JS including chart controls for quicker admin index load
* --time-until option was added to the `recalculate_charts` management command to recalculate charts only until given date
* CriteriaToStatsM2M.choices_based_on_time_range field changed it's meaning. Now choices are always calculated for whole time range. Value of this choice determines the way how the choices are calculated.

1.3.1 (2024-04-12)
------------------

* fix for Django 5.0 DashboardStats admin add view

1.3.0 (2023-02-10)
------------------

* set BigAutoField as app default
* remove support for Django<=3.1
* fix hardcoded url in admin_charts.js template

1.2.4 (2022-12-01)
------------------

* add recalculate_charts management command
* fix linting
* forbid to insert non-working characters into chart_key

1.2.3 (2022-11-03)
------------------

* add missing migration

1.2.2 (2022-11-03)
------------------

* remove unnecessary (wrongly added) permission and explain which permission to enable in error message

1.2.1 (2022-11-02)
------------------

* add permissions
* add missing migration
* check missing migrations during testing
* remove duplicate black check

1.2.0 (2022-08-21)
------------------
* migrate to django-memoize from unmaintained django-cache-utils
* testing passes in Django 4.1

1.1.0 (2022-08-01)
------------------
* pefrormance fixes
* show info when no dashboard stats are available


1.0.0 (2022-03-17)
------------------
* store chart values in CachedValue table in DB to make charts with more complicated queries faster
* add refresh/refresh all/reload on change controls to the charts
* use unpkg versions of nvd3/d3 libraries as default to simplify initial configuration

  * set ``ADMIN_CHARTS_NVD3_JS_PATH``, ``ADMIN_CHARTS_NVD3_CSS_PATH``, ``ADMIN_CHARTS_D3_JS_PATH`` variables if you want to continue using your internal JS files

0.25.2 (2021-12-30)
-------------------
* fix problem where in queries with count limit the choices could have been shuffled

0.25.1 (2021-12-30)
-------------------
* fix broken admin index page

0.25.0 (2021-12-28)
-------------------
* add support for charts in userspace
  Charts with option `show_for_users` turned on are displayed to users.
  The charts has to have set some `user_field`, this filters data attributed only for the user.
* add support for multiple operation fields (separated by comma)
* improve analytics page - fix loading time, add loading overlay
* fix usage without jsonfield package installed
* Admin charts are now displayed only for users with `view_dashboardstats` permissions set on

0.24.1 (2021-02-23)
-------------------
* add ADMIN_CHARTS_USE_JSONFIELD setting

0.24.0 (2021-02-23)
-------------------
* fixes for MySQL
* add quarter time scale option
* use native Django JSONField if awailable
* tuning of time formats and small fixes

0.23.0 (2020-09-28)
-------------------
* choices can be set to be range dependant and limited by count

0.22.0 (2020-09-15)
-------------------
* fix hourly chart (sorting)
* improve time labels on non-bar charts

0.21.1 (2020-09-11)
-------------------
* add default values for filter and multiple series

0.20.2 (2020-07-05)
------------------
* fix charts not showing on admin index page

0.20.0 (2020-06-20)
------------------
* add analytics page with all charts

0.19.0 (2020-03-05)
------------------
* improvements to the admin interface

0.18.1 (2020-03-04)
------------------
* fix problem with saw-like charts on longer time periods

0.18.0 (2020-03-03)
------------------
* fix problem with saw-like charts arount DST times
* remove dependency on qsstats-magic

0.17.0 (2020-02-20)
------------------
* fixes for DateField and timezones

0.16.0 (2020-02-06)
------------------
* move use_as to the m2m model to make criteria more universal
* add prefix for criteria

0.15.0 (2020-02-04)
------------------
* cleanups and refactoring
* faster queries
* add Django 3.0 support
* invalidate cache on models save
* dropped support of Python 3.5 (in which cache invalidation does not work)
* add AvgCountPerInstance operation type
* allow to set &debug=True GET parameter in chart-data view for easier debugging
* move distinct to separate field

0.14.0 (2020-01-28)
------------------
* fix js cache mismatches

0.13.0 (2020-01-16)
------------------
* add x_axis_format as DashboardStats field
* add interactive guideline to StackedAreaChart

0.12.0 (2020-01-16)
------------------

* fix problem with date as Date field
* report errors as javascript alerts

0.11.0 (2019-11-21)
------------------

* added support to display dynamic criteria as multiple series <Petr Dlouhý>
* chart type switcher was added <Petr Dlouhý>
* default values for charts switches can be configured in DashboardStatsAdmin <Petr Dlouhý>
* fix for USE_TZ=False <Petr Dlouhý>
* fix switches action that was not working in some cases <Petr Dlouhý>
* dynamic criteria values are automatically generated if dynamic criteria mapping not filled in (in some cases) <Petr Dlouhý>
* dynamic criteria JSON can now contain filter value <Petr Dlouhý>
* support for Django<2.0 and Python<3.5 was dropped <Petr Dlouhý>

0.10.1 (2019-10-07)
------------------

* removed remaining forced dependency on django-admin-tools <Petr Dlouhý>

0.10.0 (2019-10-04)
------------------

* charts are now loaded through Ajax with live configuration  <Petr Dlouhý>
* charts can now work only with django-admin, dependency on django-admin-tools was made optional <Petr Dlouhý>
* DistinctCount qualifier added <Petr Dlouhý>
* date/operate fields can now contain related reference <Petr Dlouhý>
* fix loading charts on page load <Petr Dlouhý>

0.9.0 (2018-01-08)
------------------

* Count added <Petr Dlouhý>
* fix Travis configuration and Django versions in it <Petr Dlouhý>
* other fixes for Django 2.0 <Petr Dlouhý>
* use djcacheutils for Python 3 compatibility <Petr Dlouhý>

0.8.0 (2017-01-18)
------------------

* make possible to change dateformat of x axis <Petr Dlouhý>
* add example for dynamic criteria <Petr Dlouhý>
* test also dynamic criteria <Petr Dlouhý>
* use django-qsstats-magic that work with Python 3 in tests <Petr Dlouhý>
* test actual chart generation -> increase test coverage <Petr Dlouhý>
* fix: preserve criteria settings of other chart stats <Petr Dlouhý>
* fix duplicate id of dynamic criteria form <Petr Dlouhý>
* reduce size of generated code by reusing load_charts code in function <Petr Dlouhý>
* fix duplication of % sign in template svg tag <Petr Dlouhý>
* catch also TypeError in registration field <Petr Dlouhý>
* rename "Graph key" to "Graph identifier" to be more clear <Petr Dlouhý>
* use save_as=True in admin to allow easier copying of charts <Petr Dlouhý>
* allow to override day intervalse for graphs <Petr Dlouhý>
* reorganize testing to run coverage <Petr Dlouhý>
* remove old import code <Petr Dlouhý>
* checks of DashboardStats field values, report field errors by Django message framework <Petr Dlouhý>



0.7.1 (2016-08-17)
------------------

* fix travis-ci tests Django & Python version


0.7.0 (2016-08-17)
-------------------

* fixes for newer Django and Python versions
* add Travis configuration file
* allow to override get_registration_charts function
* fix Python 3 compatibility
* python manage.py bower_install creates the folder build for src


0.6.6 (2015-12-13)
-------------------

* remove null=True on ManyToManyField


0.6.5 (2015-12-13)
-------------------

* add migrations


0.6.4 (2015-12-12)
-------------------

* fix bower_install creates a the folder build for src


0.6.3 (2015-12-11)
-------------------

* support for django 1.9 - depreciated get_model


0.6.2 (2015-12-10)
-------------------

* remove python-memcached from requirements


0.6.1 (2014-05-30)
-------------------

* support of Aggregation functions


0.5.5 (2014-02-06)
-------------------

* fix setup with requirement.txt file


0.5.4 (2014-02-06)
-------------------

* get rid of dependencies


0.5.3 (2014-01-03)
-------------------

* Fix js async loading with recent jquery version


0.5.2 (2014-01-01)
-------------------

* Fix requirements to not force old version of jsonfield


0.5.1 (2013-10-11)
-------------------

* Fix some bug on the tabs behavior and tooltip of the charts
* Update documentation


0.5.0 (2013-10-09)
-------------------

* Support for Django-NVD3


0.4.3 (2013-03-26)
------------------

* fix requirements - dep to django-admin-tools>=0.5.0


0.4.2 (2013-03-07)
------------------

* Update trans string


0.4.1 (2012-12-19)
------------------

* Fix requirement for switch2bill-common


0.4 (2012-11-19)
------------------

* Fix for Django 1.4 timezone support by vdboor (Diederik van der Boor)


0.3 (2012-10-03)
------------------

* Improve setup.py and update manifest
* Update README.rst
* Fix PEP8


0.2 (2011-05-22)
----------------

* Import project
