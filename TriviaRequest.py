import requests
from Question import Question

BASE_URL = 'https://opentdb.com'

def main():
	token = get_token()
	get_questions(token, 3)


def get_token():
	url = BASE_URL + '/api_token.php?command=request'
	response = requests.get(url).json()
	code = response['response_code']
	if code is 0:
		return response['token']
	else:
		print('Error getting session token')
		exit(1)


def get_questions(token, num):
	url = BASE_URL + '/api.php?amount=' + str(num) + '&token=' + token
	response = requests.get(url)
	json = response.json()

	print(json)
	print('\n\n')

	code = json['response_code']
	if code is 0:
		questions = []
		for i in range(0,len(json['results'])):
			questions.append(Question(json['results'][i]))
		return questions
	elif code is 1:
		print('All questions used')
		exit(1)



main()
