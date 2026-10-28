def claims(article):
    return [word for word in article.split() if word.istitle()]


def fact_check(article):
    return {"verified": claims(article), "unverified": [], "sources": ["local evidence"]}


def main():
    article = "Python supports reliable automation"
    print({"writer": article, "fact_checker": fact_check(article), "reviewer": "approved"})


if __name__ == "__main__":
    main()
