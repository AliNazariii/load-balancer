import os

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


class Job:
  def __init__(self, id, code, inp, out):
    self.id = id
    if not code.endswith(".py"):
      code = f"programs/{code}.py"
    self.code = os.path.join(WORKING_DIRECTORY, code)
    self.input = os.path.join(WORKING_DIRECTORY, inp)
    self.output = os.path.join(WORKING_DIRECTORY, out)

  def __repr__(self):
    return str(self.id)

  def get_code(self):
    return self.code

  def get_input(self):
    return self.input

  def get_output(self):
    return self.output
