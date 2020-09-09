

def run():
    import os
    from sat_telemetry.polls.scripts.DataArrays import DataArrays

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    file = open("ESTACAO.TXT", 'r')
    arrayData = DataArrays()
    for linha in file:
        print(linha)
        arrayData.populate(linha)
    file.close()
    print("aqui vai a persistencia no banco de dados")

    # ToTest
