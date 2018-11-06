import random

random_num = random.randint(1,25)
lowercase_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', \
		  't','u','v','w','x','y','z']
punc = [' ', '.',',']
source_file = "test_file.txt"
am = "r"
output_file = "processed.txt"
encoding_type = "utf-8"
output_text = ""

myFile = open(source_file,am)
input_text = myFile.read()
# look at each character of the message
for i in range(len(input_text)):
	# if current char is punctuation
	# leave it alone-pass it through
	if input_text[i] in punc:
		# i=i+1 => i +=1
		output_text += output_text + input_text[i]
	else:
		alpha_index = lowercase_alphabet.index(input_text[i].lower())
		
		new_index = (alpha_index + random_num) % 26
		# maintain the case of the input message
		if input_text[i].upper() == input_text[i]:
			output_text += lowercase_alphabet[new_index].upper()
		else:
			output_text += lowercase_alphabet[new_index]

print(output_text)

