# recursive `insert` implementation
# does not return anything when executed
# THIS WILL NOT WORK :) 
#   def insert(self, value):
#     # base case: we found a parking spot!
#     # we're in an empty spot in the tree 
#     if self is None:
#         self = BinarySearchTreeNode(value)
#     # if we aren't at the base case, move towards it 
#     else:
#         # self is a node with a value 
#         # compare the value to the value at this node 
#         if value < self.value:
#             # move to the left
#             self.left.insert(value)
#         # otherwise, value >= self.value
#         else:
#             self.right.insert(value)

  def insert(self, value):
      # self.left and/or self.right need to be valid nodes 
      # for us to call `insert` on them 
      if value < self.value:
          # check if self.left is a valid node 
          if self.left:
              self.left.insert(value)
          # the left side is empty 
          else:
              # we've found a valid parking spot 
              self.left = BinarySearchTreeNode(value)
      # otherwise, value >= self.value
      else:
          if self.right:
              self.right.insert(value)
          else:
              self.right = BinarySearchTreeNode(value)