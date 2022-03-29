import webbrowser

a=input("Please Insert what you want to search:    ")
a=str(a)

webbrowser.open("https://cn.bing.com/search?&q=%s" % a)
