def get_num_words(file):
	num_words = len(file)
	return num_words

def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents

def get_num_caracters(filepath):
	text = get_book_text(filepath)
	lower_text = lower(text)
	
	return num_caracters
