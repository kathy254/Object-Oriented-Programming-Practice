class Answers():

	contributorAnswers = []

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def _comment(self, answer):
		self.contributorAnswers.append(answer)

		return dict(
			title = Answers.contributorAnswers.append[0].title,
			description = Answers.contributorAnswers.append[0].description
			)

	def _delete(self, answer):
		#contributors can delete answers they posted
		pass