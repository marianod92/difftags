from dataclasses import dataclass
from datetime import datetime
from pydriller import Repository
import re , sys , argparse , os

regex = r"[rR][bB][\s-]+[0-9]{4}"

def execute_code(from_tag, to_tag):
    pass

# Create the parser
parser = argparse.ArgumentParser(description='from_tag / to_tag')

# Add the arguments
parser.add_argument('from_tag',metavar='from_tag',type=str,help='value of the first/least tag')
parser.add_argument('to_tag',metavar='to_tag',type=str,help='last/highest tag value')

# Execute parse_args()
args = parser.parse_args()
execute_code(args.from_tag, args.to_tag)
from_tag = args.from_tag
to_tag = args.to_tag

# def validator():
#     parser = argparse.ArgumentParser(description='Process some files.')
#     parser.add_argument('from_tag', help='value of the first/least tag', type=str)
#     parser.add_argument('to_tag', help='last/highest tag value', type=str)
#     args = parser.parse_args()
#     execute_code(args.from_tag, args.to_tag)
#     from_tag = args.from_tag
#     to_tag = args.to_tag

@dataclass
class CommitResult:
    jira_ticket: str
    autor: str
    # date: datetime
    
def find_commits():
    for commit in Repository('.',from_tag=from_tag,to_tag=to_tag).traverse_commits():
            if results:= re.search(regex, commit.msg):
                cr = CommitResult(jira_ticket=results.group(0),
                                autor= commit.author.name)
                        
                                            
            print(cr)

def main():
    # validator()
    find_commits()

if __name__ == '__main__':
    main()

    # for commit in Repository('https://github.com/marianod92/difftags',from_tag='v0.1',to_tag='v0.5').traverse_commits():
    # for commit in Repository('.',from_tag='v0.1',to_tag='v0.5').traverse_commits():

    #     regex = r"[rR][bB][\s-]+[0-9]{4}"

    #     if re.search(regex, commit.msg):
    #         print("Autor: ", commit.author.name, " - " , "Message: ", commit.msg)
        # else:
            # print("NO", "Autor: ", commit.author.name, " - " , "Message: ", commit.msg)
            # print("")
            
        # for file in commit.modified_files:
        #     print(file.filename, ' has changed')