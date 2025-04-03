import json
from typing import List

class FormItem:
  item: dict
  def __init__(self):
    self.item = {}
  
class DataGenItem(FormItem):
  def __init__(self):
    super().__init__()
  
  def store(self, field_name: str):
    self.item['store'] = field_name
    return self
  
class FormCanvas:
  items: List[FormItem] = []
  
  def __init__(self, items: List[FormItem] = None):
    if items:
      self.items = items
        
  def __add__(self, other):
    if isinstance(other, FormItem):
      new_items = self.items.copy()
      new_items.append(other)
      return FormCanvas(new_items)
    else:
      raise TypeError(f"Expected FormItem, got {type(other)}")
   
  def get_items(self):
    l = []
    for i in self.items:
      l.append(i.item)
      
    return l
      
  def __str__(self):
    return json.dumps(self.get_items())
  
class InputItem(DataGenItem):
  def __init__(self, id:str = None, placeholder:str = None, valueType:str = 'text'):
    super().__init__()
    self.item['type'] = 'input'
    self.item['id'] = id
    self.item['placeholder'] = placeholder
    self.item['valueType'] = valueType

class ABButtonsItem(DataGenItem):
  def __init__(self, id:str = None, buttons:List[List[str]] = [["Option A", "a"], ["Option B", "b"]]):
    super().__init__()
    self.item['type'] = 'ab_buttons'
    self.item['id'] = id
    self.item['options'] = []
    
    for button in buttons:
      if len(button) < 1:
        continue
      
      value = None
      if len(button) > 1:
        value = button[1]
      
      self.item['options'].append({
        "text": button[0],
        "value": value
      })
      
class SelectItem(DataGenItem):
  def __init__(self, id:str = None, multiple: bool = None, options:List[List[str]] = [["Option A", "a"], ["Option B", "b"]], autoSubmit:bool = None):
    super().__init__()
    self.item['type'] = 'select'
    self.item['id'] = id
    self.item['multiple'] = multiple
    self.item['options'] = []
    self.item['autoSubmit'] = autoSubmit
    
    for option in options:
      if len(option) < 1:
        continue
      
      value = None
      if len(option) > 1:
        value = option[1]
      
      self.item['options'].append({
        "text": option[0],
        "value": value
      })
    
    
class QuestionItem(FormItem):
  def __init__(self, question:str):
    super().__init__()
    self.item['type'] = 'question'
    self.item['question'] = question
    
class SubmitButtonItem(FormItem):
  def __init__(self, text:str = None):
    super().__init__()
    self.item['type'] = 'submit'
    self.item['text'] = text