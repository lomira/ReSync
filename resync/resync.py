import helpers

path_local = "C:\\Users\\jtelmon\\Desktop\\Commercial_JR\\"
path_distant = "O:\\25 - Microeconomix\\Prospection Commerciale\\Propositions commerciales\\Equipe Afrique\\3) EVAL D'IMPACT\\CV_Ref_Plaquette\\"

files_local = helpers.list_file(path_local)
files_distant = helpers.list_file(path_distant)

for eloc in files_local:
    if eloc not in files_distant:
        print(eloc)
