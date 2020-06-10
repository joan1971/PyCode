#files={'Input.txt':'Randy','Code.py':'Stan','Output.txt':'John','Report.doc':'John','Graphs.xls':'Stan','TODO.txt':'Jeff','Exercise4.py':'John','GPU.cu':'Jeff','main.c':'Jeff','OldProgram.f90':'Stan'}
def group_by_owners(files):
	new_files = {value:[i for i in files.keys() if files[i] == value ] for key,value in files.items()}
	return new_files


