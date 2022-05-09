from pydriller import Repository
import re

# for commit in Repository('https://github.com/marianod92/difftags',from_tag='v0.1',to_tag='v0.5').traverse_commits():
for commit in Repository('.',from_tag='v0.1',to_tag='v0.5').traverse_commits():

    # print(commit.hash)
    print("Message: ", commit.msg)

    regex = r"[rR][bB][\s-]+[0-9]{4}"

    if re.search(regex, commit.msg):
        print("SI", "Autor: ", commit.author.name, " - " , "Message: ", commit.msg)
    # else:
        # print("NO", "Autor: ", commit.author.name, " - " , "Message: ", commit.msg)

    # for file in commit.modified_files:
    #     print(file.filename, ' has changed')