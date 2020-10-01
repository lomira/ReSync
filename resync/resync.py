import helpers
import time


path_local = "C:\\Users\\jtelmon\\Desktop\\Commercial_JR\\"
path_distant = "O:\\25 - Microeconomix\\Prospection Commerciale\\Propositions commerciales\\Equipe Afrique\\3) EVAL D'IMPACT\\CV_Ref_Plaquette\\"

files_local = helpers.list_file(path_local)
files_distant = helpers.list_file(path_distant)

fnames_local = [f.filename for f in files_local]
fnames_distant = [f.filename for f in files_distant]

new_files = files_local.copy()
updated_files = []

for eloc in files_local:
    for edis in files_distant:
        if eloc == edis:
            new_files.remove(eloc)
        elif eloc.filename == edis.filename and eloc.timestam > edis.timestam:
            updated_files.append(eloc)

print("Nouveaux : ", "\n \t \t ".join([f.path for f in new_files]))
print("Recents : ", "\n \t \t ".join([f.path for f in updated_files]))
