class Container:
  def __init__(self, id, ip):
    self.id = id
    self.job = None
    self.ip = ip

  def get_state(self):
    if self.job:
      return True
    else:
      return False

  def set_job(self, job):
    self.job = job

  def get_job(self):
    return self.job

  def clear(self):
    self.job = None

  def get_id(self):
    return self.id

  def get_ip(self):
    return self.ip
