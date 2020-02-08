# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'memphis',
    package_name = 'montclair-memphis',
    name = 'Go Memphis',
    description = 'Real Time Tracking of the Buses for Memphis, TN',
    url = 'https://memphis.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.4',
        revision = 1,
        title = 'Go Memphis',
        first_run_text = "Welcome to Memphis, TN's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.memphis',
        app_store_id = '1495548729',
        app_store_url = 'https://apps.apple.com/us/app/go-memphis/id1495548729'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.memphis',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.memphis'
    )
)
