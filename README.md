# rextract

rextract is a Shell tool to extract strings using regular exressions. 

Think of it like "sed" or "grep", but it outputs and arranges the match, not just output / replace the line.

It supports python extended regular expressions.

Usage
-----

	Usage: rextract (Options) [reg pattern] ([Output Str])
		Reads from stdin and applies regex pattern line-by-line.

		Options:

			--debug     Enable debug mode

	If output str is provided, will output the variables/groups captured in the regex pattern.

	Each pattern contained within parenthesis counts as a group.
	Name a group like: (?P<name>.*)

	Use ${1} or $1 for first group, use ${name} or $name for a name [ defined like (?P<name>.*) ]
	Use ${0} or $0 for entire matched string.

	NOTE: Make sure to single-quote the "output str" or escape dollar [$] signs!

Example
-------

Example, extract all the usernames and UIDs from /etc/passwd of folks who use "/bin/bash" as their shell, and reformat it.

	cat /etc/passwd | rextract '^(?P<username>[^:]+)[:][^:]*[:](?P<uid>[\d]+)' '${username} [${uid}]'

Explaned Expression:

* Match starts at first character of line. First group is named "username", and contains at least 1 character and all characters that are not ':'. 
* Then comes a colon ':'
* Then comes 0 or more characters which are not colon ':'
* Then comes a colon
* Second group is named "uid", and contains one or more digits.

Our output is the username, followed by square brackets enclosing the uid.

Example output:

	root [0]
	bin [1]
	daemon [2]
	mail [8]
	ftp [14]
	http [33]
	uuidd [68]
	dbus [81]
