################################################################################
# Style file for markdownlint.
#
# https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md
#
# This file is referenced by the project `.mdlrc`.
################################################################################

#===============================================================================
# Start with all built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
all

#===============================================================================
# Override default parameters for some built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/creating_styles.md#parameters

# Ignore line length for specific files
rule 'MD013',
  ignore_code_blocks: true,
  files: ['CHANGELOG.md', 'RENOVATE_TESTING.md'],
  line_length: 99999  # Very high number to effectively disable for specified files

# Allow duplicate headers in changelog files
rule 'MD024',
  allow_different_nesting: true,
  files: ['CHANGELOG.md']

#===============================================================================
# Exclude the rules I disagree with.

# IMHO it's easier to read lists like:
# * outmost indent
#   - one indent
#   - second indent
# * Another major bullet
exclude_rule 'MD004'

# Inconsistent indentation for list items is not a problem.
exclude_rule 'MD005'

# Ordered lists are fine.
exclude_rule 'MD029'

# The first line doesn't always need to be a top level header.
exclude_rule 'MD041'

# I find it necessary to use '<br/>' to force line breaks.
exclude_rule 'MD033' # Inline HTML

# Using bare URLs is fine.
exclude_rule 'MD034'

# Allow emphasis to be used as headings (e.g., **Section Title**)
exclude_rule 'MD036'
