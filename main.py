from src.openspace import OpenSpace

"""I will use my list for colleagues"""

if __name__ == "__main__":
    file_name = "/Users/mehmet/Desktop/openspace-organizer/openspace-organizer-1/colleagues.txt"
    names = []
    def load_colleagues(file_name):
        with open(file_name, "r") as file:
            for line in file:
                names.append(line)

    openspace = OpenSpace()
    output_filename = "stored_repartition.txt" 
    colleagues = load_colleagues(file_name)
    openspace.display()
    openspace.store(output_filename)





    