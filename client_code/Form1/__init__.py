from ._anvil_designer import Form1Template
from anvil import *
from form_checker import validation

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validator = validation.Validator()
    self.validator.require_text_field(self.ammonia_factor)
    #self.validator.require_selected_value(self.protein_factor)
    self.validator.enable_when_valid(self.calculate)
    
    
  def calculate_click(self, **event_args):
    """This method is called when calculate benefit is clicked"""
    if self.protein_factor.selected_value == "Normal":
      self.protein_calc = int(1)
    elif self.protein_factor.selected_value == "Half Protein":
      self.protein_calc = int(2)
    elif self.protein_factor.selected_value == "No Protein":
      self.protein_calc = int(3)
    elif self.protein_factor.selected_value == None:
      alert("Please fill all fields!")
      self.answerbox.text = None
    if self.risk_factor.selected_value == "Normal":
      self.risk_calc = int(1)
    elif self.risk_factor.selected_value == "High":
      self.risk_calc = int(2)
    elif self.risk_factor.selected_value == None:
      alert("Please fill all fields!")
      self.answerbox.text = None
    self.ammonia_calc = self.ammonia_factor.text
    self.benefit_factor = round((self.protein_calc*self.risk_calc*self.ammonia_calc)/140, 2)
    if self.ammonia_calc > 1000:
      alert("Ammonia must be less than 1000!")
      self.ammonia_factor.text = None
      self.answerbox.text = None
    elif self.ammonia_calc < 0:
      alert("Ammonia must be a positive number!")
      self.ammonia_factor.text = None
      self.answerbox.text = None
    else:
      self.answerbox.text = f'Benefit factor is {self.benefit_factor}'
  pass

  def reset_click(self, **event_args):
    """Wipes fields when the reset button is clicked"""
    self.protein_factor.selected_value = None
    self.risk_factor.selected_value = None
    self.ammonia_factor.text = None
    self.answerbox.text = None
  pass


