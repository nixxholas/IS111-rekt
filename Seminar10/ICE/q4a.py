def search_headlines(kp):
    print()
    news = open('news.txt', 'r')
    search_res = []
    for article in news:
        if kp.lower() in article.lower():
            search_res.append(str(len(search_res) + 1) + '. ' + article.rstrip())

    if len(search_res) == 0:
        print("There is no matching headline!")
    else:
        print("There are", len(search_res), "headlines:")
        for i in search_res:
            print("\t" + i)
    print()


searched_before = False
while True:
    if input('Do you want to search our news database? [Y|N] :' if not searched_before else "Do you want to search "
                                                                                            "again? [Y|N] :") == 'N':
        break
    if not searched_before:
        searched_before = True
    search_headlines(input("Please enter a keyword or a key phrase:"))
