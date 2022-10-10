# This is a sample Python script.

# This is based on the
# https://aosabook.org/en/500L/a-template-engine.html
# look at the readme.md to understand the goal of this project


class CodeBuilder:
    """ Source code builder """
    INDENT_STEP = 4  # pep8 says so

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        """
        Add a new line to the source code.
        Indentation and new line will be added for you. Don't provide them
        :param line:
        :return:
        """
        self.code.extend([" " * self.indent_level, line, "\n"])

    def indent(self):
        """
        Incrase the indent for the following lines
        :return:
        """
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """
        Decrease the indent for the following lines
        :return:
        """
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """
        Add a section, a sub-CodeBuilder
        :return:
        """
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        return "".join(str(chr) for chr in self.code)

    def get_globals(self):
        """
        Execute the code, and return a dictionary of globals it defines
        :return:
        """
        # Check that caller has really finished all the blocks they started
        assert self.indent_level == 0

        # get the python source as a single string. [ Look at __str__ function above ]
        python_src = str(self)

        # Execute the source, defining globals and return them
        global_namespace = {}
        exec(python_src, global_namespace)
        return global_namespace
