import sublime, sublime_plugin

class EncodingUtfCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "# -*- encoding: utf-8 -*-\n")
