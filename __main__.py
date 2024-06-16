"""Module containing code to begin auto liking.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

import threading

from account import *
from website import *

"""Input user account information here:"""
# VK email and password
vk_email = ""
vk_password = ""
# Twinby email and password
twinby_email = ""
twinby_password = ""

# Mamaba email and password
mamba_email = ""
mamba_password = ""

# Initialize dating websites
vk = Vk(Account(email = vk_email, password = vk_password))
twinby = Twinby(Account(email = twinby_email, password = twinby_password))
mamba = Mamba(Account(mamba_email, password=mamba_password))

# Begin login & auto liking sequences in separate threads
threading.Thread(target=vk.run_auto_liker).start()
threading.Thread(target=twinby.run_auto_liker).start()
threading.Thread(target=mamba.run_auto_liker).start()

