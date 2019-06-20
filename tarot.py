def tarotGetHand(your_name, number_of_cards):
	import random
	tarotCards = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
	tarotHand = random.sample(tarotCards, k = number_of_cards)
	tarotText = "Hello, {name}; hopefully these cards predict a bright future!".format(name = your_name)	
	print(tarotText)
	print(tarotHand}



def tarotGetHandPredict(your_name, number_of_cards):
	import random
	tarotPredictionText = []
	tarotCards = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
	tarotHand = random.sample(tarotCards, k = number_of_cards)
	tarotText = "Hello, {name}; the cards say the following...".format(name = your_name)	
	tarotCardMeanings = {"0":["The fool says this...", "The fool says that..."], "1":["the 1 this", "the 1 that"], "2":["the 2 this", "the 2 that"], "3":["the 3 this", "the 3 that"], "4":["the 4 this", "the 4 that"], "5":["the 5 this", "the 5 that"], "6":["the 6 this", "the 6 that"], "7":["the 7 this", "the 7 that"], "8":["the 8 this", "the 8 that"], "9":["the 9 this", "the 9 that"], "10":["the 10 this", "the 10 that"], "11":["the 11 this", "the 11 that"], "12":["the 12 this", "the 12 that"], "13":["the 13 this", "the 13 that"], "14":["the 14 this", "the 14 that"], "15":["the 15 this", "the 15 that"], "16":["the 16 this", "the 16 that"], "17":["the 17 this", "the 17 that"], "18":["the 18 this", "the 18 that"], "19":["the 19 this", "the 19 that"], "20":["the 20 this", "the 20 that"], "21":["the 21 this", "the 21 that"]}
	for tarotCard in tarotHand:
		tarotCardPredictions = tarotCardMeanings[tarotCard]
		tarotMeaning = random.choice(tarotCardPredictions)
		tarotPredictionText.append(tarotMeaning)
	print(tarotText)
	print(", ".join(tarotPredictionText))
