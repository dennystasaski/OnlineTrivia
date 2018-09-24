import requests
from Question import Question

BASE_URL = 'https://opentdb.com'
NUM_QUESTIONS = 5
ENCODING = 'urlLegacy'


def main():
	token = get_token()
	result = get_questions(token, NUM_QUESTIONS, None)
	if result is None:
		reset_token(token)
		result = get_questions(token, NUM_QUESTIONS, None)
	return result


def get_token():
	url = BASE_URL + '/api_token.php?command=request'
	response = requests.get(url).json()
	code = response['response_code']
	if code is 0:
		return response['token']
	else:
		print('Error getting session token')
		exit(1)


def reset_token(token):
	url = BASE_URL + 'api_token.php?command=reset&token=' + token
	response = requests.get(url).json()
	code = response['response_code']
	if code is not 0:
		print('Error resetting token')
		exit(1)


def get_questions(token, num, category):
	json = req_questions(token, num, category)
	return json
	'''code = json['response_code']
	if code is 0:
		questions = []
		for i in range(0, len(json['results'])):
			questions.append(Question(json['results'][i]))
		return questions
	elif code is 1:
		return None'''


def req_questions(token, num, category):
	url = BASE_URL + '/api.php?amount=' + str(num) \
			+ '&token=' + token + '&encode=' + ENCODING
	if category is not None:
		url += '&category=' + str(category)
	response = requests.get(url)
	return response#.json()


main()
