#!/bin/bash
#  Put this file in /etc/profile.d and if $HOME/bin exists,
#    then add to PATH. This uses rextract off the passwd file
#    instead of relying on the $HOME variable. This may not be
#    the best way, but is a good example of "rextract"

_MY_PASSWD_LINE="$(grep -E "^(`whoami`)" /etc/passwd)"

_CURRENT_USER_SHELL=$(echo "${_MY_PASSWD_LINE}" | /usr/bin/rextract '(?P<username>[^:]+)[:](?P<pass>[^:]*)[:](?P<uid>[^:]+)[:](?P<gid>[^:]+)[:]([^:]*)[:](?P<home>[^:]*)[:](?P<shell>.+)' '$shell')


if [ ! -z "${_CURRENT_USER_SHELL}" ] && [ "${_CURRENT_USER_SHELL}" = "/bin/bash" ];
then
	_CURRENT_USER_HOME=$(echo "${_MY_PASSWD_LINE}" | /usr/bin/rextract '(?P<username>[^:]+)[:](?P<pass>[^:]*)[:](?P<uid>[^:]+)[:](?P<gid>[^:]+)[:]([^:]*)[:](?P<home>[^:]*)[:](?P<shell>.+)' '$home')
	echo "My home: ${_CURRENT_USER_HOME}"
	if [ -d "${_CURRENT_USER_HOME}/bin" ];
	then
		export PATH="${_CURRENT_USER_HOME}/bin:$PATH"
		echo "Adding home, new PATH: ${PATH}"
	fi
	unset _CURRENT_USER_HOME
fi

unset _CURRENT_USER_SHELL
unset _MY_PASSWD_LINE

