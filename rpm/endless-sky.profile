# -*- mode: sh -*-

# Firejail profile for /usr/bin/endless-sky

# x-sailjail-translation-catalog = endless-sky
# x-sailjail-translation-key-description = permission-la-data
# x-sailjail-description = Endless-Sky data storage
# x-sailjail-translation-key-long-description = permission-la-data_description
# x-sailjail-long-description = Store configuration and save data

### PERMISSIONS


# we need to be able to read
# /home/.local/share
# but no stanza in sailjail prfile will make it work.
# but doing it in firejail config works
#
# use bare name without path here! it will look files in /etc/firejail
include endless-sky.local

# noblacklist /home
# whitelist /home/.local/share/endless-sky
# read-only /home/.local/share/endless-sky

whitelist ${HOME}/.local/share/endless-sky
whitelist ${HOME}/.cache/endless-sky
whitelist ${HOME}/.config/endless-sky

private-bin /usr/bin/endless-sky
