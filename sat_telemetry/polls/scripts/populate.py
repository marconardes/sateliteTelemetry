

def run():
    from polls.scripts.DataArrays import DataArrays
    array = DataArrays()
    stringDados1 = "EB90 00002 1 -23.210876 -45.859367 04 12 2019 009 31 33 A"
    stringDados2 = "00002 2 0080 12 000.02 000.00 00631 00 29.6 24.9 27.8 A"
    stringDados3 = "00002 3 0946.72 1020.68 00630 20.00 0 1 1 1 1 1 A -65 A"
    array.populate(stringDados1)
    array.populate(stringDados2)
    array.populate(stringDados3)
    print(array)
