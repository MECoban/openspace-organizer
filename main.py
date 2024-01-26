from openspace import OpenSpace

file_name = "/Users/mehmet/Desktop/openspace-organizer/openspace-organizer-1/colleagues.txt"
colleagues_names = []
def load_colleagues(file_name):
    with open(file_name, "r") as file:
        for line in file:
            colleagues_names.append(line)
            #print(colleagues_names)


if __name__ == "__main__":
    number_of_tables = 6
    capacity_of_table = 4
    output_filename = "stored_repartition.txt"
    colleagues = load_colleagues(file_name)
    OpenSpace.display()
    OpenSpace.store(output_filename) #In openspace.store I need to handle this 





    