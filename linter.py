from SublimeLinter.lint import RubyLinter
from SublimeLinter import lint

class Fasterer(RubyLinter):
  """Provides an interface to fasterer."""
  cmd = 'ruby -S fasterer'

  # Message Ex: Using each_with_index is slower than while loop. Occurred at lines: 1469.
  regex = r'^(?P<message>.+). Occurred at lines: (?P<line>\d+)'

  defaults = {
    'selector': 'source.ruby'
  }

  default_type = lint.WARNING
  tempfile_suffix = 'rb'
  multiline = False
