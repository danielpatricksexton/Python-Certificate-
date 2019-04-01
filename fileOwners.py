
def group_by_owners(files):
    new_dict = {}
    for pair in files.items():
        if pair[1] not in new_dict.keys():
            new_dict[pair[1]] = []

        new_dict[pair[1]].append(pair[0])

    return new_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
