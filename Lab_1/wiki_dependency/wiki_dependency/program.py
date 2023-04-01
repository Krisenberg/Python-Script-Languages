import wikipedia

articleName = input("Enter the name of the article: ")
lengthOfSummary = input("Enter the number of sentences of the summary to be printed: ")

print("\n{0} sentences of the summary:\n".format(lengthOfSummary))
print(wikipedia.summary(articleName, lengthOfSummary))
print("\nURL of the article is: " + wikipedia.page(articleName).url + "\n\n")
