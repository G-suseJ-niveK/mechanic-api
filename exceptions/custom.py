class CustomException(Exception):

  """
    CustomException

    *Params:
      message: string required
      status_code: int, required
  """
  def __init__(self, message, status_code):
    self.message = message
    self.status_code = status_code
