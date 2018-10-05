class Question():

	allQuestions = []

	def __init__(self, title, description, questionID):
		self.title = title
		self.description = description
		self.questionID = questionID

	def _save(self, question):
		self.allQuestions.append(question)

		return dict(
			title = Question.allQuestions.append[0].title,
			description = Question.allQuestions.append[0].description,
			questionID = Question.allQuestions.append[0].questionID
			)

	def _delete(self, question):
		self.allQuestions.remove(question)




