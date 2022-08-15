from ctypes import windll
from locale import windows_locale
sys_language = windows_locale[windll.kernel32.GetSystemDefaultUILanguage()]
user_language = windows_locale[windll.kernel32.GetUserDefaultUILanguage()]
print(sys_language)
print(user_language)