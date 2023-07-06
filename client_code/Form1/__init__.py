from ._anvil_designer import Form1Template
from anvil import *
from form_checker import validation

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validator = validation.Validator()
    self.validator.require_text_field(self.answerbox)
    self.validator.enable_when_valid(self.calculate)

    
  def calculate_click(self, **event_args):
    """This method is called when the button is clicked"""
    if int(self.ammonia_factor) < 0 or int(self.ammonia_factor) >1000:
      alert(f'Ammonia must be a positive number less than 1000')
    
    pass

