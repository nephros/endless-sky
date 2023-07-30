# -*- mode: sh -*-

# Firejail profile for /usr/bin/endless-sky

# x-sailjail-translation-catalog = endless-sky
# x-sailjail-translation-key-description = permission-la-data
# x-sailjail-description = Endless-Sky data storage
# x-sailjail-translation-key-long-description = permission-la-data_description
# x-sailjail-long-description = Store configuration and save data

### PERMISSIONS

whitelist /home/.local/share/endless-sky
read-only /home/.local/share/endless-sky

whitelist ${HOME}/.local/share/endless-sky
whitelist ${HOME}/.cache/endless-sky
whitelist ${HOME}/.config/endless-sky

private-bin /usr/bin/endless-sky
