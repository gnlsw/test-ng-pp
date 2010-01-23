
############################################
class TestScope:
   #########################################
   def __init__(self, inst, expr):
      self.inst = inst
      self.expr = expr
      self.elements = []
      self.sub_scopes = []
      self.siblings = []

   #########################################
   def get_inst(self):
      result = self.inst
      if self.expr:
         result = result + " " + self.inst

      return result

   #########################################
   def get_elements(self):
      return self.elements

   #########################################
   def get_sub_scopes(self):
      return self.sub_scopes
   
   #########################################
   def get_siblings(self):
      return self.siblings

   #########################################
   def is_root_scope(self):
      return self.inst == "ifdef" or \
             self.inst == "ifndef" or \
             self.inst == "if"

   #########################################
   def add_elem(self, elem):
      self.elements.append(elem)

   #########################################
   def add_sub_scope(self, scope):
      self.sub_scopes.append(scope)

   #########################################
   def add_sibling(self, scope):
      self.siblings.append(scope)

############################################