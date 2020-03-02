try:
    from urllib import urlopen
except ImportError:
    from urllib2 import urlopen

def read_text():

    quotes = open('/home/roronoa/Documents/Python/movie_quotes.txt')
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    

#read_text()
def check_profanity(text_to_check):
    
    connect = urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connect.read()
    connect.close()
    #print(output)
    
    if(output == "true"):
        print("Profanity Detected!") 
    else:
        print("Good to go.")  
    
read_text()