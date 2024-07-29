class Question:

	def __init__(self, _text, _answer):
		self.text = _text
		self.answer = _answer
		
new_q = Question("1+1=2", True)
print (new_q.text)
print (new_q.answer)
