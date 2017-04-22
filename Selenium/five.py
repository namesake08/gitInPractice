import webbrowser

new=2

tabUrl = "http://google.com/?#q=";

term = raw_input("Enter search query: ");

webbrowser.open(tabUrl+term, new=new);