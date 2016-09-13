# rextract


	Shell tool to extract strings using regular exressions
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
