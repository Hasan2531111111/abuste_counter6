[app]
title = ط§ط¨ظˆط³ط·ظ‡â€Œط´ظ…ط§ط±
package.name = abustecounter
package.domain = org.abuste

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,db

version = 0.1

# ظ†ع©طھظ‡: sqlite3 ط¨ط®ط´غŒ ط§ط² ع©طھط§ط¨ط®ط§ظ†ظ‡ ط§ط³طھط§ظ†ط¯ط§ط±ط¯ ظ¾ط§غŒطھظˆظ† ط§ط³طھ ظˆ ظ†غŒط§ط²غŒ ط¨ظ‡
# ط§ظپط²ظˆط¯ظ† ط¬ط¯ط§ع¯ط§ظ†ظ‡ ط¨ظ‡ requirements ظ†ط¯ط§ط±ط¯.
requirements = python3==3.11.6,kivy==2.3.1,kivymd==2.0.0,arabic_reshaper,python-bidi

orientation = portrait
fullscreen = 0

# icon.filename = %(source.dir)s/assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.accept_sdk_license = True
android.permissions =
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
