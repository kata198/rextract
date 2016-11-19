rextract
========

rextract is a powerful commandline tool to extract and manipulate strings using regular exressions.

Think of it somewhat similar to "sed" or "grep", except it gives you complete control to rearrange/omit/duplicate

the output, so far as regular expressions support.

It supports python extended regular expressions (compatible with perl-style).

Usage
-----

	Usage: rextract (Options) [regex pattern] ([output format])

		Reads from stdin and applies provided regex pattern line-by-line,

		optionally outputting in a format specified by "output format."


	Options:

	\=\=\=\=\=\=\=\=


			\\--debug     Enable debug mode

			\-\-version   Print version and exit


	Usage:

	\=\=\=\=\=


		Some examples of usage could be:

		* Extracting one or more groups from the input

		* Omitting one or more groups from the input

		* Rearranging the input

		* Using some textual input (csv?) into a series of commands to execute

		* Creating reports

		* Many others!



	Regex Pattern Format/Tips:

	\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

		rextract supports extended regular expression syntax (python/perl-style), specifically

		that provided by the standard python "re" module.

		Some examples can be found at https://docs.python.org/3/howto/regex.html



		Each pattern contained within parenthesis counts as a group.

		Each group left-to-right is assigned a numerical value, starting with 1.


		You can assign a name to a group like so: 


			(?P<my_group_name>[a-zA-Z][a-zA-Z0-9]+)


			^ This creates a group which you can reference as:


			${my_group_name}


		A group must start with a letter a-z or underscore ( '_' ),

		 and must only contain letters a-z (any case), numbers 0-9, or underscore.

		Name a group like: (?P<name>.*)


		The regular expression will match at any point within the line, unless

		'^' (start of line) or '$' (end of line) are present, in which case it

		will have to match with those restrictions.


		Thus, there is no need to prefix with '.*' to be able to match somewhere

		in the center.


        If a line fails to match, it will not be provided to for use as output,

         it will just be silently skipped. You cannot logically format output

         from an unknown input.


       You can specify a "NOT" within your pattern by starting a group with a caret ( '^' )

        For example, to match that a line does not start with a semicolon, you can use a

        pattern line:


          ^([^;].*)


	Output Format

	\=\=\=\=\=\=\=\=\=\=\=\=\=


		The "Output Format" argument can be though of exactly like a bash string -

		characters all have their literal value except those preceded with an

		un-escaped dollar ( $ ) sign. These represent groups, either numeric or

		by-name. See the section above for more info on creating groups.


		If the "Output Format" argument is omitted, the entire matched region will

		be printed, line-by-line. This is equivalent to providing an 

		"Output Format" of '${0}'.


	Numeric Groups

	\-\-\-\-\-\-\-\-\-\-\-\-\-\-


		Use ${1} or $1 for the first group, and ${3} for the third.

		Numerical groups are assigned left-to-right as they appear in the regex,

		even if the group is in a conditional, and despite nesting.


		For example:

			"((yellow|white) cheddar)|((whole|part-skim) mozerella)"

			
		"yellow|white cheddar" is the first group,

		"yellow|white" is the second group

		"whole|part-skim mozerella" is the third group

		"whole|part-skim" is the fourth group.


		If a group is not matched, it is assigned the value of an empty string.


		Use the special group $0 or ${0]} to print the entire matched section.


	Named Groups

	\-\-\-\-\-\-\-\-\-\-\-\-


		If you defined any groups to have a name (see section above on this topic),

		i.e. (?P<my_group>...) , then you can reference that group in the output

		as $my_group or ${my_group}.



	NOTE: Make sure to single-quote the "Output Format" argument,

		or escape dollar [$] signs (by using \$).


	rextract version 1.0.0 by Tim Savannah


Examples
--------


*passwd file*

Example, extract all the usernames and UIDs from /etc/passwd of folks who use "/bin/bash" as their shell, and reformat it.

	cat /etc/passwd | rextract '^(?P<username>[^:]+)[:][^:]*[:](?P<uid>[\d]+).*/bin/bash$' '${username} [${uid}]'


Example output:

	joe55 [1000]

	tjoseph [1009]

	james [1011]



Explained Expression:

* Match starts at first character of line. First group is named "username", and contains at least 1 character and all characters that are not ':'. 
* Then comes a colon ':'
* Then comes 0 or more characters which are not colon ':'
* Then comes a colon
* Second group is named "uid", and contains one or more digits.
* Then, match 0 or more characters
* Then, match the string "/bin/bash" at the end of the line ( represented by '$' )

Our output is the username, followed by square brackets enclosing the uid.



*Logs*

Example, extract a sorted list of all pacman (archlinux) packages updated/installed on a specific date, and versions


	rextract '^(\[2016-11-02).*(upgraded|installed) (?P<what>.*)$' '$what' < /var/log/pacman.log  | sort


Sample Output:

	asciidoc (8.6.9-3)

	accerciser (3.14.0-4 -> 3.22.0-1)

	accountsservice (0.6.42-1 -> 0.6.43-1)

	adwaita-icon-theme (3.20-2 -> 3.22.0-1)

	aisleriot (3.20.2-1 -> 3.22.0+5+gb3024a2-1)

	akonadi-qt4 (1.13.0-10 -> 1.13.0-11)



Explanation:

Here's a few sample lines from pacman.log:


	[2016-11-02 16:45] [ALPM] installed asciidoc (8.6.9-3)

	[2016-11-02 22:42] [ALPM] upgraded tali (3.20.0-2 -> 3.22.0-1)

	[2016-11-02 22:42] [ALPM] upgraded totem (3.20.1-1 -> 3.22.0+5+ge0bf46e-1)

	[2016-11-02 22:42] [ALPM] warning: directory permissions differ on /etc/unrealircd/

	filesystem: 700  package: 755

	[2016-11-02 22:42] [ALPM] warning: directory permissions differ on /etc/unrealircd/aliases/

	filesystem: 700  package: 755

	[2016-11-02 22:42] [ALPM] upgraded unrealircd (4.0.6-1 -> 4.0.7-1)



As you can see, there's a lot of information here, some relevant, some not.

Basically, this is an example that COULD be done with grep and sed, but

is much more easily accomplished with rextract, and we may actually want to modify

the form of the output (see "More Advanced" below)


So the filter expression says:

* Filter that line starts with the date of interest
* Filter that 0 or more characters occur between that date and either the word "upgraded" or "installed"
* Extract everything after the word "upgraded" or "installed" (excluding the space after), and place into a group called "what"

And our output expression just contains the 'what' portion.


*Strip Comments*

To strip comments from a file, where a "comment" is defined by the character ';' and everything following on a given line:

cat myFile.ini | rextract '(?P<valid>[^;]\*)' > myFile.ini.stripped


*More Advanced:*


Okay, so now let's get more advanced. We want to produce a report that lists what software installations happened today,

what the final version is, and whether it is new software (installation) or old software (upgrade). And we use the same log file.


This is accomplished with the following:

	rextract '^(\[2016-11-02).*(?P<action>[ui])(pgraded|nstalled) (?P<name>[^ ]+)[ ][\(](.+[\-][>][ ]){0,1}(?P<final_version>.+)[\)]$' '$name = $final_version [$action]' < /var/log/pacman.log  | sort


Sample output:

	asciidoc = 8.6.9-3 [i]

	vim = 8.0.0055-1 [u]

	vim-runtime = 8.0.0055-1 [u]

	yelp = 3.22.0+1+gfabd8eb-1 [u]
	
	yelp-tools = 3.18.0+1+g193c2bd-1 [u]

	yelp-xsl = 3.20.1-2 [u]



Here we show the package name, the final version, and a marker if it was an install or an upgrade ( [i] == install, [u] == upgrade ).


Filter Explanation:

* Start with today's date
* This time, split the first letter of "upgraded" and "installed" into its own group, "action".
* Ensure that following the "action" letter is the remainder of the word. Note, in theory this could match 'ipgraded' or 'unstalled', but with this given data, it won't. However, in other cases, it might. For those cases, we can match with an "or" condition, and use two groups (you cannot repeat group names, even in an "or" condition):

		./rextract '^(\[2016-11-02).*\[ ](((?P<a1>[u])pgraded)|((?P<a2>[i])nstalled))[ ](?P<name>[^ ]+)[ ][\(](.+[\-][>][ ]){0,1}(?P<final_version>.+)[\)]$' '$name - $final_version [${a1}${a2}]' < /var/log/pacman.log

So here, note that we no longer can match "ipgraded" or "unstalled". When a group is present in the pattern string, but does not appear in a matched group, its value is assigned as an empty string. Thus, where we used "$action" in the simpler form, we now use "${a1}${a2}", as only one will hold a value ('u' or 'i'), and the other will be blank.

Anyway, I digress. Be sensible, unless lives are on the line, it's OK to take shortcuts (like "(?P\<action\>[ui])(pgraded|nstalled)") which are not "technically" 100% correct, but are 100% accurate with real-world data.

* After the word "upgraded/installed" and the following space, take all non-space characters ("\[^ \]") and assign to group "name". This will be the package name.
* Next follows a space, and an open parenthesis.
* Then, is a conditional group. We match that there are at least one character followed by an arrow ("->") followed by a space, 0 or 1 times. This may be confusing to some, basically, we are making a group of "{anything}-> " and saying you may see that group 0 times, or 1 time. This covers the difference in representations of the "installed" and "upgraded" packages. 'Upgrades' will have matched that group 1 time (ok), 'installs' would have matched that group 0 times (ok).
* Now that we've discarded the first part of the parenthesis in the upgrade case, and remain just inside the paren in the install place, what is left between the cursor and the close-parenthesis is the final version. So we match everything from cursor to the final version.


