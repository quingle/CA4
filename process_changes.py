
def read_file(any_file):
    # use strip to strip out spaces and trim the line.
    return [line.strip() for line in open('C:/Users/ciara/Desktop/CA4/Input.txt', 'r')]

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'Reference': details[0].strip(),
                'Author': details[1].strip(),
                'Date': details[2].strip().split(' ')[0],
                'Timestamp': details[2].strip().split(' ')[1],
                'Lines_Updated': int(details[3].strip().split(' ')[0])
            }
            change_file_end_index = data.index('', index + 1)
            commit['Path_Updated'] = data[index + 3 : change_file_end_index]
            commit['Author_Comment'] = data[change_file_end_index + 1 : 
                    change_file_end_index + 1 + commit['Lines_Updated']]
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            index = len(data)
    return commits

def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("Reference,Author,Date,Timestamp,Lines_Updated,Author_Comment\n")
    for commit in commits:
        my_file.write(commit['Reference'] + ',' + commit['Author'] +
                ',' + commit['Date'] + ',' + commit['Timestamp'] + ',' +
				str(commit['Lines_Updated']) + ',' + ' '.join(commit['Author_Comment']) + '\n')
    my_file.close()

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'C:/Users/ciara/Desktop/CA4/changes_python.log'
    data = read_file(changes_file)
    print len(data)
    commits = get_commits(data)
    print len(commits)
    print commits[0]
    print commits[0]['Author']
    save_commits(commits, 'C:/Users/ciara/Desktop/CA4/Output.csv')
    
    
    
    
    
    